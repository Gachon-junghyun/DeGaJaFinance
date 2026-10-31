"""Contract §§4/6: automatic settlement and derived outcome measurements.

Prices are read only. Peer returns use the target's exact endpoint dates,
including the target in its market's equal-weight universe. Missing peers are
omitted; an empty peer set, an incomplete 60-return window, or zero sample
standard deviation yields NULL. Public writers preserve the caller's transaction.
"""
from __future__ import annotations

import csv
import io
import json
import math
import sqlite3
import statistics
from datetime import date, datetime, timezone
from urllib.parse import urlencode
from urllib.request import urlopen

from module_lens._config import LENS_DB


def _ensure_schema(con):
    """Only the five tables this layer needs; exact contract §2 columns/DDL."""
    statements = (
        """CREATE TABLE IF NOT EXISTS questions (
          id TEXT PRIMARY KEY, legacy TEXT, asked_at TEXT NOT NULL, desk TEXT,
          market TEXT, subject TEXT, title TEXT NOT NULL, settle TEXT,
          observable TEXT, branches TEXT, status TEXT NOT NULL DEFAULT 'open',
          note TEXT, link TEXT, backfilled INTEGER NOT NULL DEFAULT 0,
          created TEXT NOT NULL, updated TEXT NOT NULL)""",
        """CREATE TABLE IF NOT EXISTS evidence (
          id INTEGER PRIMARY KEY AUTOINCREMENT, question TEXT NOT NULL,
          method TEXT NOT NULL, kind TEXT NOT NULL, key TEXT, reading TEXT,
          supports TEXT, weight REAL NOT NULL DEFAULT 0, impact REAL, dead TEXT,
          note TEXT, link TEXT, backfilled INTEGER NOT NULL DEFAULT 0,
          at TEXT NOT NULL)""",
        "CREATE INDEX IF NOT EXISTS evidence_q ON evidence(question)",
        """CREATE TABLE IF NOT EXISTS outcomes (
          question TEXT PRIMARY KEY, fired TEXT NOT NULL, value TEXT,
          scored_at TEXT NOT NULL, scorer TEXT NOT NULL,
          price_1d REAL, price_3d REAL, price_5d REAL, price_20d REAL,
          brier REAL, note TEXT, link TEXT)""",
        """CREATE TABLE IF NOT EXISTS credit (
          level TEXT, name TEXT, n INTEGER, hits INTEGER, misses INTEGER,
          wsum REAL, cred REAL, beta_mean REAL, lo80 REAL, hi80 REAL,
          updated TEXT, PRIMARY KEY(level, name))""",
        """CREATE TABLE IF NOT EXISTS impact (
          kind TEXT, key TEXT, mult REAL, n INTEGER, src TEXT,
          PRIMARY KEY(kind, key))""",
    )
    for statement in statements:
        con.execute(statement)


def _rows(con, sql, params=()):
    cursor = con.execute(sql, params)
    names = [column[0] for column in cursor.description]
    return [dict(zip(names, row)) for row in cursor.fetchall()]


def _number(value):
    try:
        value = float(value)
        return value if math.isfinite(value) else None
    except (TypeError, ValueError, OverflowError):
        return None


def _branches(value):
    try:
        value = json.loads(value) if isinstance(value, str) else value
        if isinstance(value, list) and all(isinstance(x, dict) for x in value):
            return value
    except (TypeError, ValueError):
        pass
    return []


def _day(value):
    try:
        return date.fromisoformat(str(value)[:10]).isoformat()
    except (TypeError, ValueError):
        return None


def parse_observable(s) -> dict:
    """Return {kind, ticker|series_id, h}; invalid input has a reason."""
    if not isinstance(s, str):
        return {"kind": None, "reason": "missing observable"}
    parts = s.strip().split(":", 2)
    kind = parts[0]
    if kind == "text":
        return {"kind": "text", "text": s.strip()[5:]}
    if kind not in ("px", "pxx", "fred") or len(parts) != 3:
        return {"kind": None, "reason": "invalid observable grammar"}
    try:
        h = int(parts[2])
        if h < 1 or not parts[2].isdigit() or not parts[1].strip():
            raise ValueError
    except ValueError:
        return {"kind": None, "reason": "h must be a positive observation count"}
    return {"kind": kind, "series_id" if kind == "fred" else "ticker":
            parts[1].strip(), "h": h}


def brier(branches, fired) -> float | None:
    branches = _branches(branches)
    keys = [x.get("k") for x in branches]
    if not keys or fired not in keys or len(set(keys)) != len(keys):
        return None
    probabilities = [_number(x.get("p")) for x in branches]
    if any(p is None for p in probabilities):
        return None
    return sum((p / 100.0 - (branch.get("k") == fired)) ** 2
               for branch, p in zip(branches, probabilities))


def fred_series(series_id) -> list[tuple[str, float]]:
    """FRED CSV without an API key; unavailable series/network returns []."""
    try:
        url = "https://fred.stlouisfed.org/graph/fredgraph.csv?" + urlencode({"id": series_id})
        with urlopen(url, timeout=20) as response:
            reader = csv.reader(io.StringIO(response.read().decode("utf-8-sig")))
            result = {}
            for row in reader:
                if len(row) < 2:
                    continue
                day, value = _day(row[0]), _number(row[1])
                if day and value is not None:
                    result[day] = value
            return sorted(result.items())
    except (OSError, ValueError, UnicodeError):
        return []


def settleable(observable) -> str | None:
    """Why a numeric observable can never auto-settle, or None. text: is always allowed.

    2026-10-31: KR codes without .KS and tickers outside the lens.db universe (SPY, TSM)
    were asked, would have stayed open forever, and starved the scoring loop.
    """
    obs = parse_observable(observable)
    if obs["kind"] in ("text", "fred"):
        return None
    if obs["kind"] is None:
        return obs["reason"]
    con = _open_px()
    if con is None:
        return None  # 가격 DB 가 없는 기계에선 막지 않는다
    try:
        row = con.execute("SELECT market FROM universe WHERE ticker=?", (obs["ticker"],)).fetchone()
    except sqlite3.Error:
        return None
    finally:
        con.close()
    if row is None:
        hint = f" — 국내는 '{obs['ticker']}.KS' 꼴" if obs["ticker"].isdigit() else " — 지수는 fred:SP500 처럼 FRED 로"
        return f"{obs['ticker']} 가 가격 유니버스(data/lens.db)에 없어 자동 정산이 안 된다{hint}"
    return None


def _open_px():
    try:
        return sqlite3.connect(LENS_DB.resolve().as_uri() + "?mode=ro", uri=True)
    except (OSError, sqlite3.Error):
        return None


class _Prices:
    def __init__(self, con, today=None):
        self.prices, self.markets = {}, {}
        if con is None:
            return
        try:
            for ticker, market in con.execute("SELECT ticker, market FROM universe"):
                self.markets[ticker] = market
            sql = "SELECT ticker, date, close FROM px"
            params = ()
            if today:
                sql += " WHERE date <= ?"
                params = (today,)
            for ticker, day, close in con.execute(sql, params):
                # Retain missing closes in the calendar: do not shorten horizons.
                self.prices.setdefault(ticker, {})[day] = _number(close)
        except sqlite3.Error:
            self.prices, self.markets = {}, {}

    def _find_breaks(self):
        """One-day close ratio > 3x or < 1/3 is a data break (split, bad tick), not a return.

        2026-10-31 sim fundamentals: 011810.KS 3,530 → 410,465 lifted the KR equal-weight
        mean by +13.8pp and shaved every KR pxx score in that window. Any window that
        spans a break returns None, for the target and for each peer.
        """
        self.breaks = {}
        for ticker, series in self.prices.items():
            prev = None
            for day in sorted(series):
                close = series[day]
                if prev and close and (close / prev > 3 or close / prev < 1 / 3):
                    self.breaks.setdefault(ticker, []).append(day)
                if close:
                    prev = close

    def window(self, ticker, settle, h):
        prices = self.prices.get(ticker, {})
        days = sorted(prices)
        before = [i for i, day in enumerate(days) if day < settle]
        if not before:
            return None
        b = before[-1]
        if b + h >= len(days):
            return None
        return days, b

    def raw(self, ticker, start, end):
        if not hasattr(self, "breaks"):
            self._find_breaks()
        if any(start < day <= end for day in self.breaks.get(ticker, ())):
            return None
        prices = self.prices.get(ticker, {})
        a, b = prices.get(start), prices.get(end)
        if a is None or b is None or a <= 0 or b <= 0:
            return None
        return b / a - 1.0

    def excess(self, ticker, start, end):
        raw = self.raw(ticker, start, end)
        market = self.markets.get(ticker)
        if raw is None or market is None:
            return None
        peers = [self.raw(peer, start, end) for peer, m in self.markets.items()
                 if m == market]
        peers = [x for x in peers if x is not None]
        return raw - statistics.mean(peers) if peers else None

    def standardized(self, ticker, settle, h):
        window = self.window(ticker, settle, h)
        if window is None:
            return None, "missing base or horizon prices"
        days, b = window
        if b < 60:
            return None, "fewer than 60 daily excess returns"
        daily = [self.excess(ticker, days[i - 1], days[i])
                 for i in range(b - 59, b + 1)]
        excess = self.excess(ticker, days[b], days[b + h])
        if excess is None or any(x is None for x in daily):
            return None, "missing target or same-market peer returns"
        sd = statistics.stdev(daily)
        if sd <= 0:
            return None, "zero sd60"
        return excess / (sd * math.sqrt(h)), None


def _fill(con, q, prices):
    outcomes = _rows(con, "SELECT * FROM outcomes WHERE question=?", (q["id"],))
    if not outcomes:
        return {"question": q["id"], "reason": "missing outcome"}
    result = outcomes[0]
    result["brier"] = brier(q.get("branches"), result["fired"])
    reasons = {}
    settle = _day(q.get("settle"))
    for h in (1, 3, 5, 20):
        column = f"price_{h}d"
        if settle:
            result[column], reason = prices.standardized(q.get("subject"), settle, h)
        else:
            result[column], reason = None, "missing/invalid settle date"
        if reason:
            reasons[column] = reason
    con.execute("""UPDATE outcomes SET price_1d=?,price_3d=?,price_5d=?,
                   price_20d=?,brier=? WHERE question=?""",
                tuple(result[k] for k in ("price_1d", "price_3d", "price_5d",
                                          "price_20d", "brier", "question")))
    if result["brier"] is None:
        reasons["brier"] = "missing probabilities or fired is not a branch key"
    if reasons:
        result["reason"] = reasons
    return result


def fill_outcome(con, qid, px_con=None) -> dict:
    """Recompute derived columns, never change the adjudication; idempotent."""
    _ensure_schema(con)
    questions = _rows(con, "SELECT * FROM questions WHERE id=?", (qid,))
    if not questions:
        return {"question": qid, "reason": "missing question"}
    owned = px_con is None
    if owned:
        px_con = _open_px()
    try:
        return _fill(con, questions[0], _Prices(px_con))
    finally:
        if owned and px_con is not None:
            px_con.close()


def _matches(branch, value):
    lo, hi = branch.get("lo"), branch.get("hi")
    if lo is not None and _number(lo) is None:
        return False
    if hi is not None and _number(hi) is None:
        return False
    return (lo is None or value >= float(lo)) and (hi is None or value < float(hi))


def score_due(con, today=None, px_con=None, fetch_fred=None) -> list[dict]:
    """Judge open numeric questions. Skips have reason; text/existing are absent.

    today limits *both* price and FRED observations (no look-ahead). fetch_fred
    is series_id -> iterable of (ISO date, level); failures leave questions open.
    Writers do not commit: the caller controls the ledger transaction.
    """
    _ensure_schema(con)
    today = _day(today if today is not None else date.today())
    if today is None:
        return [{"reason": "invalid today date"}]
    owned = px_con is None
    if owned:
        px_con = _open_px()
    try:
        prices, fred_cache, results = _Prices(px_con, today), {}, []
        questions = _rows(con, """SELECT q.* FROM questions q
            WHERE q.status='open' AND NOT EXISTS
            (SELECT 1 FROM outcomes o WHERE o.question=q.id) ORDER BY q.id""")
        for q in questions:
            obs = parse_observable(q.get("observable"))
            if obs["kind"] == "text":
                continue
            skip = {"question": q["id"], "status": "skipped"}
            settle = _day(q.get("settle"))
            if obs["kind"] is None:
                results.append(dict(skip, reason=obs["reason"]))
                continue
            if settle is None or settle > today:
                results.append(dict(skip, reason="missing settle date or not due"))
                continue
            h, value = obs["h"], None
            if obs["kind"] == "fred":
                sid = obs["series_id"]
                if sid not in fred_cache:
                    series = {}
                    try:
                        for day, level in (fetch_fred or fred_series)(sid):
                            day, level = _day(day), _number(level)
                            if day and day <= today and level is not None:
                                series[day] = level
                    except (OSError, ValueError, TypeError, sqlite3.Error):
                        series = {}
                    fred_cache[sid] = sorted(series.items())
                series = fred_cache[sid]
                before = [i for i, (day, _) in enumerate(series) if day < settle]
                if before and before[-1] + h < len(series):
                    b = before[-1]
                    value = series[b + h][1] - series[b][1]
            else:
                ticker = obs["ticker"]
                window = prices.window(ticker, settle, h)
                if window:
                    days, b = window
                    func = prices.raw if obs["kind"] == "px" else prices.excess
                    raw = func(ticker, days[b], days[b + h])
                    if raw is not None:
                        value = raw * 100.0
            if value is None or not math.isfinite(value):
                results.append(dict(skip, reason="missing base/horizon observations or universe"))
                continue
            branches = _branches(q.get("branches"))
            matches = [x.get("k") for x in branches if x.get("k") and _matches(x, value)]
            fired = matches[0] if len(matches) == 1 else "AMBIGUOUS"
            status = "scored" if fired != "AMBIGUOUS" else "ambiguous"
            now = datetime.now(timezone.utc).isoformat()
            note = None if status == "scored" else f"{len(matches)} matching branch intervals"
            con.execute("""INSERT INTO outcomes
                (question,fired,value,scored_at,scorer,note) VALUES (?,?,?,?,?,?)""",
                        (q["id"], fired, str(value), now, "auto", note))
            con.execute("UPDATE questions SET status=?, updated=? WHERE id=?",
                        (status, now, q["id"]))
            result = _fill(con, q, prices)
            result["status"] = status
            if note:
                result["reason"] = note
            results.append(result)
        return results
    finally:
        if owned and px_con is not None:
            px_con.close()
