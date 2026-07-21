# -*- coding: utf-8 -*-
"""변곡점 ↔ 뉴스 연결 — "그날 그 종목에 대해 무슨 말이 있었나".

읽는 곳은 `data/news_vectors.db`(클라이언트 소유 파생물: 제목·발행일·매체·URL·벡터)
하나뿐이다. 서버 소유 `news_alert.db` 는 이 PC 에 없는 게 정상이고(P6), 본문도 거기
있으므로 **여기서 재는 건 전부 제목 기준**이다.

⚠ **제목 언급의 재현율 한계를 먼저 안다**(MODULE_MAP 실측): '제목에 상장사명이 있나'는
정밀하지만 경제기사 재현율 **10.6%** 다. 7/07 최대 사건 "코스피 급락에 매도 사이드카"는
제목에 회사명이 없다. 그래서 이 파일이 만드는 언급수는 **'그 종목이 헤드라인 주인공이
된 정도'** 이지 '그 종목 관련 뉴스량'이 아니다. 시장 전체 사건(매크로·지수)은 언급수 0
으로 잡히므로, 변곡의 절반은 여기서 안 보이는 게 정상이다 — 분모를 함께 보고한다.

⚠ **최장일치만 센다.** '현대차증권' 기사가 '현대차' 언급으로 새면 대형주 언급수가
계열사 기사로 부풀어 상관이 통째로 가짜가 된다. 매칭된 사명 중 다른 사명의 부분문자열인
것은 버린다.

⚠ 2글자 사명은 제외한다 — `_universe.KR_MIN_NAME_LEN` 의 규칙을 그대로 쓴다(P1,
대상·삼양·농심이 일반어와 충돌). 그 종목들은 이 실험의 분모에서 빠진다.
"""
from __future__ import annotations

import sqlite3
from collections import defaultdict

import pandas as pd

from module_news_data._universe import KR_MIN_NAME_LEN

from ._config import NEWS_MIN_OBS, NEWS_START, NEWS_WINDOW, VEC_DB

_SCHEMA = """
CREATE TABLE IF NOT EXISTS mentions (
    ticker TEXT NOT NULL,
    day    TEXT NOT NULL,
    n      INTEGER NOT NULL,
    PRIMARY KEY (ticker, day)
);
CREATE TABLE IF NOT EXISTS mention_link (
    ticker    TEXT NOT NULL,
    url_hash  TEXT NOT NULL,
    day       TEXT NOT NULL,
    PRIMARY KEY (ticker, url_hash)
);
CREATE INDEX IF NOT EXISTS ix_ml_day ON mention_link(ticker, day);
"""


def ensure_schema(con: sqlite3.Connection) -> None:
    con.executescript(_SCHEMA)


def _name_index(universe: list[dict]) -> dict[str, str]:
    """사명 → 티커. 2글자 미만과 우선주는 뺀다(우선주는 본주와 같은 사건을 두 번 센다)."""
    idx: dict[str, str] = {}
    for r in universe:
        n = r["name"]
        if len(n) < KR_MIN_NAME_LEN:
            continue
        if n.endswith("우") or n.endswith("우B") or n.endswith("1우"):
            continue
        idx[n] = r["ticker"]
    return idx


def build_mentions(con: sqlite3.Connection, universe: list[dict],
                   since: str = NEWS_START) -> dict:
    """제목 전수 1패스 → 티커별 일별 언급수 + 기사링크. 멱등(REPLACE)."""
    ensure_schema(con)
    idx = _name_index(universe)
    names = sorted(idx, key=len, reverse=True)   # 긴 이름 먼저 = 최장일치 판정용

    src = sqlite3.connect(f"file:{VEC_DB}?mode=ro", uri=True)
    rows = src.execute(
        "SELECT url_hash, market_day, title FROM articles "
        "WHERE market_day IS NOT NULL AND market_day >= ?", (since,)).fetchall()
    src.close()

    counts: dict[tuple[str, str], int] = defaultdict(int)
    links: list[tuple[str, str, str]] = []
    scanned = 0
    for url_hash, day, title in rows:
        scanned += 1
        if not title:
            continue
        hit = [n for n in names if n in title]
        if not hit:
            continue
        # 최장일치: 다른 매칭명의 부분문자열인 이름은 버린다
        keep = [n for n in hit if not any(n != m and n in m for m in hit)]
        for n in keep:
            tic = idx[n]
            counts[(tic, day)] += 1
            links.append((tic, url_hash, day))

    con.execute("DELETE FROM mentions")
    con.execute("DELETE FROM mention_link")
    con.executemany("INSERT OR REPLACE INTO mentions(ticker,day,n) VALUES(?,?,?)",
                    [(t, d, n) for (t, d), n in counts.items()])
    con.executemany("INSERT OR REPLACE INTO mention_link(ticker,url_hash,day) VALUES(?,?,?)",
                    links)
    con.commit()
    return {"articles_scanned": scanned, "names": len(idx),
            "ticker_days": len(counts), "links": len(links),
            "tickers_with_any": len({t for t, _ in counts})}


def mention_frame(con: sqlite3.Connection, days: list[str]) -> pd.DataFrame:
    """일 × 티커 언급수 행렬. 언급 0 인 날도 0 으로 채운다(분모 보존)."""
    df = pd.read_sql_query("SELECT ticker,day,n FROM mentions", con)
    if df.empty:
        return pd.DataFrame()
    m = df.pivot(index="day", columns="ticker", values="n")
    return m.reindex(days).fillna(0.0)


def mention_z(m: pd.DataFrame) -> pd.DataFrame:
    """언급수 z — 직전 30일 평균·표준편차(당일 제외). 0 이 많은 계열이라 σ=0 이면 NaN."""
    prev = m.shift(1)
    mu = prev.rolling(NEWS_WINDOW, min_periods=NEWS_MIN_OBS).mean()
    sd = prev.rolling(NEWS_WINDOW, min_periods=NEWS_MIN_OBS).std()
    z = (m - mu) / sd.where(sd > 0)
    return z


def articles_around(con: sqlite3.Connection, ticker: str, date: str,
                    before: int = 3, after: int = 1) -> list[dict]:
    """변곡일 주변 창의 그 종목 기사(제목·매체·URL·발행일). 시간순."""
    d0 = (pd.Timestamp(date) - pd.Timedelta(days=before)).strftime("%Y-%m-%d")
    d1 = (pd.Timestamp(date) + pd.Timedelta(days=after)).strftime("%Y-%m-%d")
    hashes = [r[0] for r in con.execute(
        "SELECT url_hash FROM mention_link WHERE ticker=? AND day BETWEEN ? AND ?",
        (ticker, d0, d1))]
    if not hashes:
        return []
    src = sqlite3.connect(f"file:{VEC_DB}?mode=ro", uri=True)
    q = ("SELECT url_hash, market_day, source, title, url FROM articles "
         f"WHERE url_hash IN ({','.join('?' * len(hashes))})")
    rows = src.execute(q, hashes).fetchall()
    src.close()
    out = [{"url_hash": h, "day": d, "source": s, "title": t, "url": u}
           for h, d, s, t, u in rows]
    out.sort(key=lambda x: (x["day"], x["source"]))
    return out
