# -*- coding: utf-8 -*-
"""렌즈 데이터 층 — 가격(KR+US)·기사↔종목 링크·라벨을 `data/lens.db` 한 파일에.

전부 파생물이다. 원본은 yfinance 종가와 `news_vectors.db`(읽기만)이고, `build` 로 언제든 다시 짓는다.

라벨 (한 줄 = 종목 × 세션):
  react  = 세션 당일 수익 − 같은 시장 같은 날 유니버스 평균 (사람들이 그날 어떻게 받았나)
  fwd3   = 세션 종가 기준 +1·+2·+3일 누적수익의 평균 − 같은 날 유니버스 평균
  fwd1·fwd5 = 그 점 하나의 누적 초과 (라벨 변형 실험용, E2)
  prior5 = 직전 5일 누적 초과

세션 = 발행시각이 그 종목 시장의 장 마감 전이면 그날, 아니면 다음 거래일. KR 은 KST 15:30,
US 는 뉴욕 16:00(서머타임 자동). 시장 판정은 기사 출처가 아니라 **종목**이 한다 —
한국 신문이 쓴 엔비디아 기사는 미국 세션에 붙는다.
"""
from __future__ import annotations

import bisect
import json
import re
import sqlite3
from collections import defaultdict
from datetime import datetime
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

from module_inflection._newslink import _name_index
from module_inflection._prices import fetch_panel
from module_inflection._prices import load_universe as kr_universe_rows
from module_news_data._chain_hop import ALIASES_JSON
from module_news_data._chain_hop import load_universe as us_pattern_universe
from module_news_data._timeaxis import parse_published

from ._config import CLOSE, FWD_AVG, FWD_POINTS, KR_MIN_NAME_LEN, LENS_DB, NEWS_START, PRICE_PERIOD, VEC_DB

_SCHEMA = """
CREATE TABLE IF NOT EXISTS universe (ticker TEXT PRIMARY KEY, market TEXT, name TEXT, sector TEXT);
CREATE TABLE IF NOT EXISTS px (ticker TEXT, date TEXT, close REAL, PRIMARY KEY (ticker, date));
CREATE TABLE IF NOT EXISTS links (ticker TEXT, url_hash TEXT, session TEXT, how TEXT,
                                  PRIMARY KEY (ticker, url_hash));
CREATE INDEX IF NOT EXISTS links_session ON links(session);
CREATE TABLE IF NOT EXISTS labels (ticker TEXT, session TEXT, market TEXT, n_arts INTEGER,
                                   react REAL, fwd1 REAL, fwd3 REAL, fwd5 REAL, prior5 REAL,
                                   PRIMARY KEY (ticker, session));
CREATE TABLE IF NOT EXISTS meta (k TEXT PRIMARY KEY, v TEXT);
"""


def connect() -> sqlite3.Connection:
    con = sqlite3.connect(LENS_DB)
    con.executescript(_SCHEMA)
    return con


# ── 유니버스 ───────────────────────────────────────────────────────────────

def universe() -> list[dict]:
    """KR 전체(kr_all.csv) + US 텍스트 탐지 유니버스(상위 300). 목록은 각 CSV 가 단일 원본."""
    out = [{"ticker": r["ticker"], "market": "KR", "name": r["name"], "sector": r["sector"]}
           for r in kr_universe_rows(top=10**6)]
    for tk, m in us_pattern_universe().items():
        out.append({"ticker": tk, "market": "US", "name": m["name"], "sector": m["sector"]})
    return out


def _us_korean_aliases(tickers: set[str]) -> dict[str, str]:
    """US 종목의 한글 별칭(엔비디아·테슬라) → 티커. 한국 신문의 미장 기사를 잡는다.
    `_chain_hop` 은 영문 코퍼스용이라 한글 별칭을 버린다 — 여기서만 쓰는 반쪽이다."""
    if not ALIASES_JSON.exists():
        return {}
    amap = json.load(open(ALIASES_JSON, encoding="utf-8"))
    out = {}
    for tk, names in amap.items():
        if tk not in tickers:
            continue
        for n in names:
            n = n.strip()
            if n and not n.isascii() and len(n) >= KR_MIN_NAME_LEN:
                out[n] = tk
    return out


# ── 가격 ──────────────────────────────────────────────────────────────────

def build_prices(con: sqlite3.Connection, uni: list[dict], period: str = PRICE_PERIOD) -> dict:
    close = fetch_panel([u["ticker"] for u in uni], period=period)
    rows = [(tk, str(dt)[:10], float(v)) for tk in close.columns
            for dt, v in close[tk].dropna().items()]
    con.execute("DELETE FROM px")
    con.executemany("INSERT OR REPLACE INTO px VALUES(?,?,?)", rows)
    # 커밋은 build() 끝에서 한 번 — 중간에 죽으면 세대가 섞이지 않게(검토 R)
    got = set(close.columns)
    return {"rows": len(rows), "tickers": len(got),
            "missing": sorted(u["ticker"] for u in uni if u["ticker"] not in got)}


def panels(con: sqlite3.Connection) -> dict[str, pd.DataFrame]:
    """시장별 종가 패널(일 × 종목). 시장마다 거래일이 달라 따로 둔다."""
    px = pd.read_sql_query(
        "SELECT p.ticker, p.date, p.close, u.market FROM px p JOIN universe u USING(ticker)", con)
    out = {}
    for mk, g in px.groupby("market"):
        P = g.pivot(index="date", columns="ticker", values="close").sort_index()
        # 그 시장 종목의 절반 이상이 값이 있는 날만 거래일로 본다(휴장일 잔여 행 제거)
        out[mk] = P[P.notna().mean(axis=1) >= 0.5]
    return out


# ── 기사 ↔ 종목 링크 ───────────────────────────────────────────────────────

def _session(pub: str | None, market: str, days: list[str]) -> str | None:
    dt = parse_published(pub)
    if dt is None:
        return None
    tz, cut = CLOSE[market]
    loc = dt.astimezone(ZoneInfo(tz) if isinstance(tz, str) else tz)
    d = loc.strftime("%Y-%m-%d")
    i = bisect.bisect_left(days, d)
    if i < len(days) and days[i] == d and loc.time() < cut:
        return d
    j = bisect.bisect_right(days, d)
    return days[j] if j < len(days) else None


def build_links(con: sqlite3.Connection, uni: list[dict], since: str = NEWS_START) -> dict:
    """제목 전수 1패스 → (종목, 기사, 세션). KR = 사명 최장일치(3글자+), US = 영문 별칭·티커
    정규식(`_chain_hop`) + 한글 별칭."""
    mk_of = {u["ticker"]: u["market"] for u in uni}
    kr_idx = _name_index([u for u in uni if u["market"] == "KR"])
    kr_idx = {n: t for n, t in kr_idx.items() if len(n) >= KR_MIN_NAME_LEN}
    us_ko = _us_korean_aliases({u["ticker"] for u in uni if u["market"] == "US"})
    ko_names = {**kr_idx, **us_ko}
    # 이름마다 따로 대면 90만 제목 × 1,100 이름이 30분을 넘는다(2026-10-31 실측) → 정규식 하나로 묶는다.
    # 긴 이름을 앞에 둬서 같은 자리에선 최장일치가 먼저 잡힌다.
    ko_rx = re.compile("|".join(re.escape(n) for n in sorted(ko_names, key=len, reverse=True)))
    # US 는 `_chain_hop` 의 낱말 경계 패턴(\b이름\b)을 그대로 쓰되 하나로 묶는다. 키는 이스케이프된 이름.
    us_name = {p.pattern[2:-2]: tk for tk, m in us_pattern_universe().items() for p in m["patterns"]}
    us_rx = re.compile(r"\b(?:" + "|".join(sorted(us_name, key=len, reverse=True)) + r")\b")
    pdays = {mk: list(P.index) for mk, P in panels(con).items()}

    src = sqlite3.connect(f"file:{VEC_DB}?mode=ro", uri=True)
    rows = src.execute("SELECT url_hash, published_at, title FROM articles "
                       "WHERE market_day >= ? AND title IS NOT NULL", (since,)).fetchall()
    src.close()

    links = []
    by = defaultdict(int)
    for h, pub, title in rows:
        hits: dict[str, str] = {}
        if not title.isascii():
            found = {m.group(0) for m in ko_rx.finditer(title)}
            for n in [n for n in found if not any(n != m and n in m for m in found)]:
                hits[ko_names[n]] = "ko"
        for m in us_rx.finditer(title):
            tk = us_name.get(re.escape(m.group(0)))
            if tk and tk not in hits:
                hits[tk] = "en"
        for tk, how in hits.items():
            mk = mk_of.get(tk)
            if mk not in pdays:
                continue
            s = _session(pub, mk, pdays[mk])
            if s:
                links.append((tk, h, s, how))
                by[mk] += 1
    con.execute("DELETE FROM links")
    con.executemany("INSERT OR REPLACE INTO links VALUES(?,?,?,?)", links)
    # (커밋은 build() 끝에서)
    return {"scanned": len(rows), "links": len(links), "by_market": dict(by)}


# ── 라벨 ──────────────────────────────────────────────────────────────────

def _xs(df: pd.DataFrame) -> pd.DataFrame:
    """같은 날 횡단면 평균을 뺀다 — 시장 전체가 빠진 날을 «나쁜 뉴스»로 읽지 않게."""
    return df.sub(df.mean(axis=1), axis=0)


def build_labels(con: sqlite3.Connection) -> dict:
    lk = pd.read_sql_query("SELECT ticker, session, count(*) n FROM links GROUP BY 1,2", con)
    out, stat = [], {}
    for mk, P in panels(con).items():
        P = P.ffill(limit=2)
        react = _xs(P.pct_change(fill_method=None))
        cum = {h: P.shift(-h) / P - 1 for h in range(1, max(FWD_AVG, *FWD_POINTS) + 1)}
        fwd3 = _xs(sum(cum[h] for h in range(1, FWD_AVG + 1)) / FWD_AVG)
        pts = {h: _xs(cum[h]) for h in FWD_POINTS}
        prior5 = _xs(P / P.shift(5) - 1)
        sub = lk[lk.ticker.isin(P.columns) & lk.session.isin(P.index)]
        n = 0
        for tk, s, k in sub.itertuples(index=False):
            def g(F):
                v = F.at[s, tk]
                return None if pd.isna(v) else float(v)
            out.append((tk, s, mk, int(k), g(react), g(pts[1]), g(fwd3), g(pts[5]), g(prior5)))
            n += 1
        stat[mk] = {"rows": n, "days": int(sub.session.nunique()),
                    "first": min(sub.session) if n else None, "last": max(sub.session) if n else None}
    con.execute("DELETE FROM labels")
    con.executemany("INSERT OR REPLACE INTO labels VALUES(?,?,?,?,?,?,?,?,?)", out)
    # (커밋은 build() 끝에서)
    return stat


def build(skip_px: bool = False, period: str = PRICE_PERIOD) -> dict:
    con = connect()
    uni = universe()
    con.execute("DELETE FROM universe")
    con.executemany("INSERT INTO universe VALUES(?,?,?,?)",
                    [(u["ticker"], u["market"], u["name"], u["sector"]) for u in uni])

    rep = {"universe": {mk: sum(u["market"] == mk for u in uni) for mk in ("KR", "US")}}
    rep["prices"] = None if skip_px else build_prices(con, uni, period)
    rep["links"] = build_links(con, uni)
    rep["labels"] = build_labels(con)
    con.execute("INSERT OR REPLACE INTO meta VALUES('built_at', ?)", (datetime.now().isoformat(timespec="seconds"),))
    con.commit()
    con.close()
    return rep


def status() -> dict:
    if not LENS_DB.exists():
        return {"db": str(LENS_DB), "exists": False}
    con = connect()
    r = {"db": str(LENS_DB),
         "built_at": (con.execute("SELECT v FROM meta WHERE k='built_at'").fetchone() or [None])[0]}
    for mk, n, a, b, d in con.execute(
            "SELECT market, count(*), min(session), max(session), count(distinct session) "
            "FROM labels WHERE fwd3 IS NOT NULL GROUP BY market"):
        r[mk] = {"labels_with_fwd3": n, "first": a, "last": b, "days": d}
    con.close()
    return r


def article_frame(con: sqlite3.Connection, market: str | None = None) -> pd.DataFrame:
    """기사 단위 행(종목·세션·제목·라벨) — 렌즈 계산의 입력. 벡터는 붙이지 않는다(메모리)."""
    q = ("SELECT l.ticker, l.url_hash h, l.session s, l.how, b.market, b.react, b.fwd1, b.fwd3, "
         "b.fwd5, b.prior5, b.n_arts FROM links l JOIN labels b ON b.ticker=l.ticker AND b.session=l.session")
    df = pd.read_sql_query(q + (" WHERE b.market=?" if market else ""), con,
                           params=[market] if market else [])
    src = sqlite3.connect(f"file:{VEC_DB}?mode=ro", uri=True)
    titles = {}
    hs = sorted(set(df.h))
    for i in range(0, len(hs), 900):
        part = hs[i:i + 900]
        titles.update(src.execute(
            f"SELECT url_hash,title FROM articles WHERE url_hash IN ({','.join('?' * len(part))})", part))
    src.close()
    df["title"] = df.h.map(titles).fillna("")
    return df


def vectors(hashes: list[str]) -> dict[str, np.ndarray]:
    src = sqlite3.connect(f"file:{VEC_DB}?mode=ro", uri=True)
    out = {}
    for i in range(0, len(hashes), 900):
        part = hashes[i:i + 900]
        for h, b in src.execute(
                f"SELECT url_hash,vec FROM vectors WHERE url_hash IN ({','.join('?' * len(part))})", part):
            out[h] = np.frombuffer(b, dtype=np.float16).astype(np.float32)
    src.close()
    return out
