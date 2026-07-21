# -*- coding: utf-8 -*-
"""가격 패널 — 유니버스 N종목의 일봉을 한 번에 받아 로컬 캐시.

⚠ P1 메모: 단일 종목 OHLCV 의 단일 원본은 `module_chart.fetch_ohlcv` 다(지표·차트가
그걸 쓴다). 여기서 그걸 안 쓰는 건 **호출 단위가 다르기 때문**이다 — 800종목을 한 건씩
받으면 HTTP 800회(실측 수십 분)라 실험이 불가능하다. yfinance 는 티커 리스트를 한 번에
받는 배치 경로가 따로 있어 그 경로만 여기서 쓴다. 단일 종목이 필요한 소비자는
`module_chart.fetch_ohlcv` 를 그대로 쓸 것(여기 함수는 패널 전용).

지표 산식(RSI·MA 등)은 **하나도 여기서 만들지 않는다** — 필요하면
`module_chart._indicators` 를 import 한다.
"""
from __future__ import annotations

import csv
import sqlite3
from typing import Iterable

import pandas as pd

from ._config import INFLECTION_DB, KR_UNIVERSE_CSV

_SCHEMA = """
CREATE TABLE IF NOT EXISTS px (
    ticker TEXT NOT NULL,
    date   TEXT NOT NULL,
    close  REAL NOT NULL,
    volume REAL,
    PRIMARY KEY (ticker, date)
);
CREATE INDEX IF NOT EXISTS ix_px_date ON px(date);
CREATE TABLE IF NOT EXISTS universe (
    ticker TEXT PRIMARY KEY,
    name   TEXT,
    sector TEXT,
    rank   INTEGER,
    mcap   REAL
);
"""


def connect() -> sqlite3.Connection:
    INFLECTION_DB.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(str(INFLECTION_DB))
    con.executescript(_SCHEMA)
    return con


def load_universe(top: int = 200) -> list[dict]:
    """kr_all.csv 상위 N(시총순). CSV 가 단일 원본이라 여기서 종목을 새로 열거하지 않는다."""
    rows: list[dict] = []
    with open(KR_UNIVERSE_CSV, encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            rows.append({
                "ticker": r["ticker"].strip(),
                "name": (r.get("name") or "").strip(),
                "sector": (r.get("sector") or "").strip(),
                "rank": int(r.get("rank") or 0),
                "mcap": float(r.get("market_cap_krw") or 0),
            })
    rows.sort(key=lambda x: x["rank"] or 10**9)
    return rows[:top]


def save_universe(con: sqlite3.Connection, rows: Iterable[dict]) -> None:
    con.executemany(
        "INSERT OR REPLACE INTO universe(ticker,name,sector,rank,mcap) VALUES(?,?,?,?,?)",
        [(r["ticker"], r["name"], r["sector"], r["rank"], r["mcap"]) for r in rows],
    )
    con.commit()


def fetch_panel(tickers: list[str], period: str = "1y", chunk: int = 60) -> pd.DataFrame:
    """티커→일별 종가 패널(wide). 배치 다운로드 — 실패 티커는 조용히 빠진다(열 없음)."""
    import yfinance as yf   # 무거운 import 는 함수 안에서(서버 기동 보호 규약과 동형)

    frames = []
    for i in range(0, len(tickers), chunk):
        part = tickers[i:i + chunk]
        df = yf.download(part, period=period, progress=False,
                         auto_adjust=True, group_by="column", threads=True)
        if df is None or df.empty:
            continue
        if isinstance(df.columns, pd.MultiIndex):
            close = df["Close"]
            vol = df["Volume"]
        else:                     # 단일 티커면 MultiIndex 가 아니다
            close = df[["Close"]].rename(columns={"Close": part[0]})
            vol = df[["Volume"]].rename(columns={"Volume": part[0]})
        frames.append((close, vol))
    if not frames:
        return pd.DataFrame()
    close = pd.concat([c for c, _ in frames], axis=1)
    vol = pd.concat([v for _, v in frames], axis=1)
    close.attrs["volume"] = vol
    return close


def store_panel(con: sqlite3.Connection, close: pd.DataFrame) -> int:
    vol = close.attrs.get("volume")
    rows = []
    for tic in close.columns:
        s = close[tic].dropna()
        v = vol[tic] if vol is not None and tic in vol.columns else None
        for dt, px in s.items():
            d = str(dt)[:10]
            vv = float(v[dt]) if v is not None and dt in v.index and pd.notna(v[dt]) else None
            rows.append((tic, d, float(px), vv))
    con.executemany("INSERT OR REPLACE INTO px(ticker,date,close,volume) VALUES(?,?,?,?)", rows)
    con.commit()
    return len(rows)


def read_panel(con: sqlite3.Connection, since: str | None = None) -> pd.DataFrame:
    q = "SELECT ticker,date,close FROM px"
    params: list = []
    if since:
        q += " WHERE date >= ?"
        params.append(since)
    df = pd.read_sql_query(q, con, params=params)
    if df.empty:
        return df
    return df.pivot(index="date", columns="ticker", values="close").sort_index()
