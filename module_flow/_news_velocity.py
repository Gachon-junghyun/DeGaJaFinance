# -*- coding: utf-8 -*-
"""① 뉴스속도 (기대감) — news_fts 기사량 최근 vs 베이스 → 관심 가속비. >1 = 가속."""
from __future__ import annotations

import sqlite3
from datetime import datetime, timedelta

from ._config import FOREIGN_SOURCES, FTS_DB, STOPWORD_TICKERS


def news_query(ticker: str, name: str | None) -> str:
    """뉴스속도 검색어 — 단어형/짧은 티커는 회사명만(오염 방지), 안전한 티커는 티커|명."""
    safe = len(ticker) >= 4 and ticker.upper() not in STOPWORD_TICKERS
    if name:
        return f"{ticker}|{name}" if safe else name
    return ticker  # 명 없음 = 티커 best-effort(짧으면 노이즈 가능)


def news_velocity(query: str, recent: int, base: int) -> dict:
    """news_fts에서 query(티커/이름) 기사량 최근 vs 베이스 → 관심 가속비."""
    if not FTS_DB.exists():
        return {"recent": None, "base_rate": None, "velocity": None, "note": "no FTS index"}
    con = sqlite3.connect(str(FTS_DB))
    ph = ",".join("?" * len(FOREIGN_SOURCES))
    match = " OR ".join(f'"{q.strip()}"' for q in query.split("|") if q.strip())

    def cnt(days):
        cut = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
        sql = f"SELECT COUNT(*) FROM news_fts WHERE news_fts MATCH ? AND source IN ({ph}) AND fetched_at >= ?"
        try:
            return con.execute(sql, [match] + FOREIGN_SOURCES + [cut]).fetchone()[0]
        except Exception:
            return 0
    r, b = cnt(recent), cnt(base)
    con.close()
    rr, br = r / recent, b / base
    vel = (rr / br) if br > 0 else (None if r == 0 else 9.99)
    return {"recent": r, "base": b, "recent_rate": round(rr, 2), "base_rate": round(br, 2),
            "velocity": round(vel, 2) if vel is not None else None}
