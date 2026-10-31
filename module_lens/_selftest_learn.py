"""Deterministic, synthetic-only contract test; no A-layer or live DB imports.

Run: python -X utf8 -m module_lens._selftest_learn
The config module is replaced *only in this test* with a temporary price path:
the checkout's config currently imports optional news dependencies transitively.
All numerical oracles below are independent of the scoring/learning helpers.
"""
from __future__ import annotations

import io
import json
import math
import random
import sqlite3
import sys
import tempfile
import types
from contextlib import closing
from datetime import date, timedelta
from pathlib import Path


def _close(actual, expected, tol=2e-11):
    if expected is None:
        assert actual is None, (actual, expected)
    else:
        assert actual is not None and abs(actual - expected) <= tol, (actual, expected)


def _quantile(a, b, q):
    # Integer Beta CDF = binomial upper tail, independently of continued fractions.
    n = a + b - 1
    left, right = 0.0, 1.0
    for _ in range(70):
        x = (left + right) / 2
        cdf = sum(math.comb(n, j) * x ** j * (1 - x) ** (n - j)
                  for j in range(a, n + 1))
        if cdf < q:
            left = x
        else:
            right = x
    return (left + right) / 2


def _fixture(con, px):
    rng = random.Random(20261031)
    dates, d = [], date(2026, 1, 1)
    while len(dates) < 120:
        if d.weekday() < 5:
            dates.append(d.isoformat())
        d += timedelta(days=1)
    markets = {f"T{i}": "US" if i < 3 else "KR" for i in range(6)}
    prices = {}
    px.executescript("""CREATE TABLE universe(ticker,market,name,sector);
                       CREATE TABLE px(ticker,date,close,PRIMARY KEY(ticker,date));""")
    for i, (ticker, market) in enumerate(markets.items()):
        px.execute("INSERT INTO universe VALUES (?,?,?,?)", (ticker, market, ticker, "synthetic"))
        prices[ticker], close = {}, 80.0 + i * 13
        for day in dates:
            close *= 1.0 + rng.gauss(0.0004 * (i - 2), 0.009 + i * 0.001)
            prices[ticker][day] = close
            px.execute("INSERT INTO px VALUES (?,?,?)", (ticker, day, close))
    px.commit()
    series = {"F1": [(day, 2 + i * 0.012 + 0.02 * math.sin(i)) for i, day in enumerate(dates)],
              "F2": [(day, 5 - i * 0.014) for i, day in enumerate(dates)]}
    con.executescript("""
        CREATE TABLE questions (
          id TEXT PRIMARY KEY, legacy TEXT, asked_at TEXT NOT NULL, desk TEXT,
          market TEXT, subject TEXT, title TEXT NOT NULL, settle TEXT, observable TEXT,
          branches TEXT, status TEXT NOT NULL DEFAULT 'open', note TEXT, link TEXT,
          backfilled INTEGER NOT NULL DEFAULT 0, created TEXT NOT NULL, updated TEXT NOT NULL);
        CREATE TABLE evidence (
          id INTEGER PRIMARY KEY AUTOINCREMENT, question TEXT NOT NULL,
          method TEXT NOT NULL, kind TEXT NOT NULL, key TEXT, reading TEXT, supports TEXT,
          weight REAL NOT NULL DEFAULT 0, impact REAL, dead TEXT, note TEXT, link TEXT,
          backfilled INTEGER NOT NULL DEFAULT 0, at TEXT NOT NULL);
        CREATE TABLE outcomes (
          question TEXT PRIMARY KEY, fired TEXT NOT NULL, value TEXT, scored_at TEXT NOT NULL,
          scorer TEXT NOT NULL, price_1d REAL, price_3d REAL, price_5d REAL,
          price_20d REAL, brier REAL, note TEXT, link TEXT);
    """)
    questions, evidence, existing = [], [], {}
    for i in range(50):
        ticker, base_index, h = f"T{i % 6}", 69 + i % 15, (1, 3, 5, 20)[i % 4]
        kind = ("px", "pxx", "fred", "text")[i % 4]
        p = (0, 20, 40, 60, 80, 100, None)[i % 7]
        branches = [{"k": "A", "p": p, "lo": None, "hi": 0},
                    {"k": "B", "p": 100 - p if p is not None else 100, "lo": 0, "hi": None}]
        if i == 4:  # Deliberate overlap.
            branches[0]["hi"], branches[1]["lo"] = 1e6, -1e6
        if i == 8:  # Deliberate gap.
            branches[0]["hi"], branches[1]["lo"] = -1e6, 1e6
        sid = "F1" if i % 8 == 2 else "F2"
        observable = f"{kind}:{sid if kind == 'fred' else ticker}:{h}"
        if kind == "text":
            observable = "text:synthetic desk judgment"
        q = dict(id=f"Q{i + 1}", desk=f"desk{i % 2}", market=markets[ticker],
                 subject=ticker if kind != "fred" else sid,
                 settle=dates[base_index + 1] + (" AMC" if i % 2 else " BMO"),
                 observable=observable, branches=branches, b=base_index, h=h,
                 kind=kind, sid=sid, backfilled=int(i % 5 == 0))
        questions.append(q)
        con.execute("""INSERT INTO questions
            (id,asked_at,desk,market,subject,title,settle,observable,branches,backfilled,created,updated)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
                    (q["id"], dates[0], q["desk"], q["market"], q["subject"], "synthetic question",
                     q["settle"], observable, json.dumps(branches), q["backfilled"], dates[0], dates[0]))
        if kind == "text" or i in (0, 12, 16):
            fired = "VOID" if i % 11 == 0 else "AMBIGUOUS" if i % 11 == 1 else ("A" if i % 3 else "B")
            existing[q["id"]] = fired
            con.execute("INSERT INTO outcomes(question,fired,scored_at,scorer) VALUES (?,?,?,?)",
                        (q["id"], fired, dates[-1], "synthetic"))
        for j in range(3):
            e = dict(question=q["id"], method=f"method{j}", kind=("flow", "news")[j % 2],
                     key=f"key{(i + j) % 2}", supports="A" if (i + j) % 3 else "B",
                     weight=(50, 30, 20)[j], dead=None, backfilled=int((i + j) % 3 == 0))
            if j == 2 and i % 13 == 0:
                e.update(dead="synthetic unusable", weight=0)
            if j == 1 and i % 9 == 0:
                e["weight"] = 0
            if j == 2 and i % 7 == 0:
                e["supports"] = ""
            if i == 9 and j == 2:
                e["key"] = None
            evidence.append(e)
            con.execute("""INSERT INTO evidence
                (question,method,kind,key,supports,weight,dead,backfilled,at)
                VALUES (:question,:method,:kind,:key,:supports,:weight,:dead,:backfilled,:at)""",
                        dict(e, at=dates[0]))
    con.commit()
    return dates, markets, prices, series, questions, evidence, existing


def _run(score, learning, con, px):
    dates, markets, prices, series, questions, evidence, existing = _fixture(con, px)
    # The oracle computes endpoint returns directly from fixture arrays.
    def excess(ticker, start, end):
        raw = prices[ticker][end] / prices[ticker][start] - 1
        peer_returns = [prices[t][end] / prices[t][start] - 1
                        for t in prices if markets[t] == markets[ticker]]
        return raw - sum(peer_returns) / len(peer_returns)

    def normalized(q, h):
        ticker, b = q["subject"], q["b"]
        if ticker not in prices:
            return None
        daily = [excess(ticker, dates[j - 1], dates[j]) for j in range(b - 59, b + 1)]
        mean = sum(daily) / 60
        sd = math.sqrt(sum((v - mean) ** 2 for v in daily) / 59)
        return excess(ticker, dates[b], dates[b + h]) / (sd * math.sqrt(h))

    fired_by_q, values = dict(existing), {}
    for q in questions:
        if q["id"] in existing or q["kind"] == "text":
            continue
        b, h, ticker = q["b"], q["h"], q["subject"]
        if q["kind"] == "fred":
            levels = dict(series[q["sid"]])
            value = levels[dates[b + h]] - levels[dates[b]]
        elif q["kind"] == "pxx":
            value = 100 * excess(ticker, dates[b], dates[b + h])
        else:
            value = 100 * (prices[ticker][dates[b + h]] / prices[ticker][dates[b]] - 1)
        matches = [branch["k"] for branch in q["branches"]
                   if (branch["lo"] is None or branch["lo"] <= value)
                   and (branch["hi"] is None or value < branch["hi"])]
        fired_by_q[q["id"]] = matches[0] if len(matches) == 1 else "AMBIGUOUS"
        values[q["id"]] = value
    calls = []
    def fake_fred(sid):
        calls.append(sid)
        return series[sid]
    original = con.execute("SELECT * FROM outcomes WHERE question='Q1'").fetchone()
    scored = score.score_due(con, today=dates[-1], px_con=px, fetch_fred=fake_fred)
    assert len(scored) == len(values)
    assert sorted(calls) == ["F1", "F2"]
    assert con.execute("SELECT * FROM outcomes WHERE question='Q1'").fetchone() == original
    for row in scored:
        qid = row["question"]
        assert row["fired"] == fired_by_q[qid], row
        _close(float(row["value"]), values[qid])
        assert row["scorer"] == "auto"
        status = con.execute("SELECT status FROM questions WHERE id=?", (qid,)).fetchone()[0]
        assert status == ("ambiguous" if row["fired"] == "AMBIGUOUS" else "scored")
    assert score.score_due(con, dates[-1], px, fake_fred) == []
    assert "AMBIGUOUS" in fired_by_q.values() and "VOID" in fired_by_q.values()
    print(f"PASS auto-score: {len(scored)} outcomes; px/pxx/FRED values, overlap/gap, existing/text untouched")

    expected_briers = {}
    price_checks = 0
    for q in questions:
        fired = fired_by_q[q["id"]]
        bs = q["branches"]
        expected = None
        if fired in [x["k"] for x in bs] and all(x["p"] is not None for x in bs):
            expected = sum((branch["p"] / 100 - int(branch["k"] == fired)) ** 2 for branch in bs)
        expected_briers[q["id"]] = expected
        row = score.fill_outcome(con, q["id"], px)
        _close(row["brier"], expected)
        # All 4 horizons for every ticker question, exceeding the 5-value requirement.
        for h in (1, 3, 5, 20):
            _close(row[f"price_{h}d"], normalized(q, h))
            price_checks += q["subject"] in prices
        stored = con.execute("SELECT * FROM outcomes WHERE question=?", (q["id"],)).fetchone()
        score.fill_outcome(con, q["id"], px)
        assert con.execute("SELECT * FROM outcomes WHERE question=?", (q["id"],)).fetchone() == stored
    print(f"PASS derived: {price_checks} price_h values; all 50 Briers; fill idempotence")

    expected_credit = {}
    for e in evidence:
        fired = fired_by_q[e["question"]]
        if fired in ("VOID", "AMBIGUOUS") or e["dead"] is not None or e["weight"] <= 0 or not e["supports"]:
            continue
        w = e["weight"] / 100 / (2 if e["backfilled"] else 1)
        hit = e["supports"] == fired
        for level in ("method", "kind", "key"):
            if e[level]:
                expected_credit.setdefault((level, e[level]), []).append((hit, w))
    con.execute("INSERT INTO credit(level,name,n) VALUES ('method','stale',999)")
    actual_credit = learning.learn(con)
    assert len(actual_credit) == 7  # 3 methods, 2 kinds, 2 keys
    assert {(r["level"], r["name"]) for r in actual_credit} == set(expected_credit)
    for row in actual_credit:
        entries = expected_credit[row["level"], row["name"]]
        n, hits, wsum = len(entries), sum(int(hit) for hit, _ in entries), sum(w for _, w in entries)
        misses = n - hits
        assert (row["n"], row["hits"], row["misses"]) == (n, hits, misses)
        _close(row["wsum"], wsum)
        _close(row["cred"], sum(w if hit else -w for hit, w in entries) / (wsum + 5))
        _close(row["beta_mean"], (1 + hits) / (2 + n))
        _close(row["lo80"], _quantile(1 + hits, 1 + misses, 0.1))
        _close(row["hi80"], _quantile(1 + hits, 1 + misses, 0.9))
    repeat = learning.learn(con)
    assert [{k: v for k, v in r.items() if k != "updated"} for r in repeat] == [
        {k: v for k, v in r.items() if k != "updated"} for r in actual_credit]
    print("PASS credit: 3 methods / 2 kinds / 2 keys; counts, backfill x0.5, K=5, Beta mean/80%; rebuild")

    impacts = [{"kind": "macro", "key": "key0", "mult": 200, "n": 15, "src": "synthetic"},
               {"kind": "news", "key": "key1", "mult": 1, "n": 20, "src": "synthetic"}]
    learning.set_impact(con, [dict(impacts[0], mult=2)])
    learning.set_impact(con, impacts)
    assert con.execute("SELECT mult FROM impact WHERE kind='macro' AND key='key0'").fetchone()[0] == 200
    assert con.execute("SELECT COUNT(*) FROM impact").fetchone()[0] == 2
    items = [{"kind": "macro", "key": "key0", "method": "method0", "supports": "A"}] + [
        {"kind": "news", "key": "key1", "method": f"method{i}", "supports": "B"} for i in range(3)]
    reference_scores = []
    for item in items:
        entries = next((expected_credit[level, item[level]] for level in ("key", "method", "kind")
                        if (level, item[level]) in expected_credit), [])
        numerator = sum(w if hit else -w for hit, w in entries)
        denominator = 5 + sum(w for _, w in entries)
        credit = max(numerator / denominator if entries else 0.05, 0.05)
        impact = next((r["mult"] for r in impacts if (r["kind"], r["key"]) == (item["kind"], item["key"])), 1)
        reference_scores.append(impact * credit)
    assert reference_scores[0] / sum(reference_scores) * 100 > 40
    # First item saturates; identical remaining keys share the 60% equally.
    expected_advice = [40.0, 20.0, 20.0, 20.0]
    advice = learning.advise(con, items)
    assert [r["weight"] for r in advice] == expected_advice
    assert sum(r["weight"] for r in advice) == 100
    # 수급·포지셔닝 상한(FLOW_CAP 30) — 같은 항목에서 첫 항목만 수급이면 40 → 30 으로 묶이고 넘친 10 은 나머지에 비례해 간다
    learning.set_impact(con, [{"kind": "flow", "key": "key0", "mult": 200, "n": 15, "src": "synthetic"}])
    capped = learning.advise(con, [dict(items[0], kind="flow")] + items[1:])
    assert capped[0]["weight"] == 30.0 and sum(r["weight"] for r in capped) == 100, [r["weight"] for r in capped]
    print("PASS advise: independent impact x credit/floor calculation, 40% cap and redistribution; impact upsert; flow cap 30")

    calibration = learning.calib(con)
    for bucket in calibration["buckets"]:
        entries = []
        for q in questions:
            fired = fired_by_q[q["id"]]
            if fired not in ("A", "B"):
                continue
            for branch in q["branches"]:
                p = branch["p"]
                if p is not None and bucket["lo"] <= p and (p < bucket["hi"] or p == 100 == bucket["hi"]):
                    entries.append((p / 100, int(branch["k"] == fired)))
        assert bucket["count"] == len(entries)
        _close(bucket["predicted_mean"], sum(p for p, _ in entries) / len(entries) if entries else None)
        _close(bucket["observed_frequency"], sum(hit for _, hit in entries) / len(entries) if entries else None)
    for group, label in (("by_desk", "desk"), ("by_kind", "kind")):
        for row in calibration[group]:
            numbers = []
            for q in questions:
                value = expected_briers[q["id"]]
                present = q["desk"] == row[label] if label == "desk" else any(
                    e["question"] == q["id"] and e["dead"] is None and e["kind"] == row[label] for e in evidence)
                if value is not None and present:
                    numbers.append(value)
            assert row["count"] == len(numbers)
            _close(row["mean_brier"], sum(numbers) / len(numbers))
    print("PASS calib: all 5 buckets (0/20/40/60/80/100 boundaries), desk/kind means, distinct alive kinds")
    _edge_tests(score, learning, con, px, dates)


def _edge_tests(score, learning, con, px, dates):
    assert score.parse_observable("px:T0:3") == {"kind": "px", "ticker": "T0", "h": 3}
    assert score.parse_observable("fred:DGS10:2")["series_id"] == "DGS10"
    assert score.parse_observable("text:a:b")["text"] == "a:b"
    for obs in (None, "", "px:T0:0", "px:T0:-1", "px:T0:x", "bogus:X:1", "px::3"):
        assert score.parse_observable(obs).get("reason"), obs
    assert score.brier(None, "A") is None
    assert score.fill_outcome(con, "missing", px)["reason"]
    assert learning.beta_interval(None, 1, 0.1) is None
    for a, b in ((1, 1), (1, 30), (30, 1), (2, 9), (50, 70)):
        for q in (0.1, 0.9):
            _close(learning.beta_interval(a, b, q), _quantile(a, b, q))
    _close(learning.beta_interval(1, 1, 0.1), 0.1)
    assert learning.beta_interval(2, 3, 0) == 0 and learning.beta_interval(2, 3, 1) == 1
    # All additional ledger cases are rolled back: the primary fixture stays 50 questions.
    con.execute("SAVEPOINT edge_cases")
    def question(qid, obs, settle=dates[80]):
        con.execute("""INSERT INTO questions
          (id,asked_at,title,settle,observable,branches,subject,created,updated)
          VALUES (?,?,?,?,?,?,?,?,?)""", (qid, dates[0], "synthetic edge", settle, obs,
          json.dumps([{"k": "A", "p": 40, "lo": None, "hi": 0},
                      {"k": "B", "p": 60, "lo": 0, "hi": None}]), "T0", dates[0], dates[0]))
    question("missing_px", "px:ABSENT:1")
    question("missing_fred", "fred:ABSENT:1")
    question("future", "px:T0:20", dates[110])
    question("early", "px:T0:1", dates[10])
    question("boundary", "fred:ZERO:1")
    question("no_settle", "px:T0:1", None)
    assert all(r.get("reason") for r in score.score_due(con, dates[90], px,
               lambda sid: [] if sid != "ZERO" else [(dates[79], 1), (dates[80], 1)] )
               if r["question"] != "boundary")
    assert con.execute("SELECT fired FROM outcomes WHERE question='boundary'").fetchone()[0] == "B"
    assert con.execute("SELECT COUNT(*) FROM outcomes WHERE question='future'").fetchone()[0] == 0
    early = score.fill_outcome(con, "early", px)
    assert all(early[f"price_{h}d"] is None for h in (1, 3, 5, 20))
    assert score.fill_outcome(con, "missing_px", px)["reason"] == "missing outcome"
    question("fred_future", "fred:ZERO:20", dates[85])
    rows = score.score_due(con, dates[90], px, lambda sid: [(d, float(i)) for i, d in enumerate(dates)])
    assert next(r for r in rows if r["question"] == "fred_future")["status"] == "skipped"
    con.execute("ROLLBACK TO edge_cases")
    con.execute("RELEASE edge_cases")

    # Test downloader against synthetic CSV bytes; no network call occurs.
    saved = score.urlopen
    seen = []
    def fake_urlopen(url, timeout):
        seen.append((url, timeout))
        return io.BytesIO(b"observation_date,F1\n2026-01-01,1\n2026-01-02,.\n2026-01-03,\n2026-01-04,2.5\n")
    try:
        score.urlopen = fake_urlopen
        assert score.fred_series("F1") == [("2026-01-01", 1.0), ("2026-01-04", 2.5)]
        assert seen == [("https://fred.stlouisfed.org/graph/fredgraph.csv?id=F1", 20)]
        def offline(*args, **kwargs):
            raise OSError("synthetic offline")
        score.urlopen = offline
        assert score.fred_series("F1") == []
    finally:
        score.urlopen = saved

    with closing(sqlite3.connect(":memory:")) as empty:
        assert learning.learn(empty) == []
        assert score.score_due(empty, dates[-1], px, lambda _: []) == []
        assert learning.calib(empty)["by_kind"] == []
        assert learning.advise(empty, []) == []
        items = [{"kind": "unknown", "key": "unknown", "method": "unknown"} for _ in range(7)]
        equal = learning.advise(empty, items)
        assert [r["weight"] for r in equal] == [13.0] + [14.5] * 6  # residual on largest (first tie)
        assert all("n<10" in r["reason"] for r in equal)
        assert [r["weight"] for r in learning.advise(empty, items[:2])] == [50, 50]
        assert learning.advise(empty, items[:1])[0]["weight"] == 100
        assert learning.set_impact(empty, [{"kind": "x"}])[0]["reason"]
        assert score.fill_outcome(empty, "unknown", px)["reason"]
        # Fallback priority, negative-credit floor, all-level n<10 rule.
        empty.executemany("INSERT INTO credit(level,name,n,cred) VALUES (?,?,?,?)",
                          [("method", "method", 20, 0.5), ("kind", "kind", 20, 0.2),
                           ("key", "key", 2, -0.5)])
        items = [{"key": "key", "method": "method", "kind": "kind"},
                 {"key": "none", "method": "method", "kind": "kind"},
                 {"key": "none", "method": "none", "kind": "kind"},
                 {"key": "none", "method": "none", "kind": "none"}]
        advice = learning.advise(empty, items)
        # Scores .05,.5,.2,.05 -> cap second at 40, then third at 40 -> 10/40/40/10.
        assert [r["weight"] for r in advice] == [10, 40, 40, 10]
        empty.execute("UPDATE credit SET n=9")
        assert [r["weight"] for r in learning.advise(empty, items)] == [25] * 4

    # Rounding/cap stress over deterministic inputs, including saturated residual repair.
    rng = random.Random(2026)
    for count in range(3, 25):
        for _ in range(80):
            weights = learning._weights([10 ** rng.uniform(-4, 4) for _ in range(count)])
            assert sum(weights) == 100 and max(weights) <= 40 and min(weights) >= 0, weights
            assert all(w * 2 == int(w * 2) for w in weights)
    for count in (201, 250, 400):
        weights = learning._weights([1] * count)
        assert sum(weights) == 100 and 0 <= min(weights) <= max(weights) <= 40
    # NULL/zero daily volatility and sparse same-date peers never produce NaN.
    with closing(sqlite3.connect(":memory:")) as sparse:
        sparse.executescript("CREATE TABLE universe(ticker,market); CREATE TABLE px(ticker,date,close);")
        sparse.execute("INSERT INTO universe VALUES ('FLAT','US')")
        sparse.executemany("INSERT INTO px VALUES ('FLAT',?,100)", [(d,) for d in dates])
        p = score._Prices(sparse)
        assert p.standardized("FLAT", dates[80], 1) == (None, "zero sd60")
        sparse.execute("UPDATE px SET close=NULL WHERE date=?", (dates[79],))
        assert score._Prices(sparse).standardized("FLAT", dates[80], 1)[0] is None
        assert score._Prices(sparse).excess("ABSENT", dates[79], dates[80]) is None
    saved_path = score.LENS_DB
    try:
        score.LENS_DB = saved_path.with_name("absent.db")
        assert score._open_px() is None and not score.LENS_DB.exists()
    finally:
        score.LENS_DB = saved_path
    print("PASS edges: grammar, missing data, future cutoff, half-open bounds, CSV/offline, Beta tails,")
    print("            fresh DBs, zero sd60, equal n<10, fallback/floor, infeasible cap, 1763 rounding/cap cases")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.dont_write_bytecode = True
    with tempfile.TemporaryDirectory(prefix="lens_synthetic_") as folder:
        # Synthetic config isolates tests from live paths and optional news imports.
        config = types.ModuleType("module_lens._config")
        config.LENS_DB = Path(folder) / "prices.db"
        previous = sys.modules.get("module_lens._config")
        sys.modules["module_lens._config"] = config
        try:
            from module_lens import _score as score
            from module_lens import _learn as learning
            with closing(sqlite3.connect(Path(folder) / "ledger.db")) as con, closing(sqlite3.connect(config.LENS_DB)) as px:
                _run(score, learning, con, px)
                # Default price connection is actually read-only and uses synthetic config.
                default_px = score._open_px()
                assert default_px is not None
                try:
                    try:
                        default_px.execute("CREATE TABLE forbidden(x)")
                    except sqlite3.OperationalError as exc:
                        assert "readonly" in str(exc).lower()
                    else:
                        raise AssertionError("default px connection is writable")
                finally:
                    default_px.close()
                assert score.fill_outcome(con, "Q2")["price_1d"] is not None
                assert con.execute("SELECT COUNT(*) FROM questions").fetchone()[0] == 50
                print("PASS default px: read-only URI; only synthetic temporary DBs; 50 questions / 6 tickers / 120 days")
        finally:
            if previous is None:
                sys.modules.pop("module_lens._config", None)
            else:
                sys.modules["module_lens._config"] = previous
    print("ALL TESTS PASSED")


if __name__ == "__main__":
    main()
