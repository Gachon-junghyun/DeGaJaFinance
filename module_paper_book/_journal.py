# -*- coding: utf-8 -*-
"""module_paper_book._journal — 결정 저널 + 트랙레코드(사후검증 먹이).

매 결정(ENTER/ADD/HOLD/TRIM/EXIT)의 '왜'를 append-only 로 남긴다. 원본 판단을 정정
옆에 남기는 산업데스크 규약과 동형 — 나중 자기채점(module_epistemics·alert-postmortem)의
먹이가 된다. equity_snapshots(_book)로 자기자본 곡선을 읽어 트랙레코드를 만든다.
"""
from __future__ import annotations

import sqlite3
from datetime import datetime, timezone
from typing import Optional

_JOURNAL_SCHEMA = """
CREATE TABLE IF NOT EXISTS journal (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ts TEXT NOT NULL,
    ticker TEXT,
    action TEXT,            -- ENTER|ADD|HOLD|TRIM|EXIT|REVIEW
    conviction TEXT,        -- high|med|low
    freshness TEXT,         -- LIVE|PARTIAL|RESOLVED (근거 리포트 태그)
    rationale TEXT,
    source_report TEXT,
    committed INTEGER DEFAULT 0   -- 실제 장부에 반영(--commit)됐는지
);
"""


def _now() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def _ensure(conn: sqlite3.Connection) -> None:
    conn.executescript(_JOURNAL_SCHEMA)


def log_decision(conn: sqlite3.Connection, ticker: str, action: str, rationale: str,
                 conviction: str = "med", freshness: str = "", source_report: str = "",
                 committed: bool = False) -> int:
    _ensure(conn)
    cur = conn.execute(
        "INSERT INTO journal(ts,ticker,action,conviction,freshness,rationale,source_report,committed)"
        " VALUES(?,?,?,?,?,?,?,?)",
        (_now(), ticker.upper() if ticker else None, action, conviction, freshness,
         rationale, source_report, 1 if committed else 0),
    )
    return int(cur.lastrowid)


def recent(conn: sqlite3.Connection, limit: int = 30) -> list[dict]:
    _ensure(conn)
    rows = conn.execute("SELECT * FROM journal ORDER BY id DESC LIMIT ?", (limit,)).fetchall()
    return [dict(r) for r in rows]


def track_record(conn: sqlite3.Connection) -> dict:
    """자기자본 스냅샷 → 수익률·MDD·승률(실현손익 기준)."""
    snaps = conn.execute(
        "SELECT ts, equity_krw FROM equity_snapshots ORDER BY id"
    ).fetchall()
    curve = [(r["ts"], r["equity_krw"]) for r in snaps if r["equity_krw"] is not None]
    ret_pct = mdd = None
    if len(curve) >= 2 and curve[0][1]:
        ret_pct = (curve[-1][1] / curve[0][1] - 1) * 100
        peak = curve[0][1]
        mdd = 0.0
        for _, e in curve:
            peak = max(peak, e)
            mdd = min(mdd, (e / peak - 1) * 100)
    # 실현손익 기준 승/패
    tx = conn.execute(
        "SELECT realized_pnl FROM transactions WHERE side='sell' AND realized_pnl IS NOT NULL"
    ).fetchall()
    closed = [t["realized_pnl"] for t in tx]
    wins = sum(1 for x in closed if x > 0)
    losses = sum(1 for x in closed if x < 0)
    win_rate = (wins / (wins + losses) * 100) if (wins + losses) else None
    return {
        "snapshots": len(curve),
        "return_pct": round(ret_pct, 2) if ret_pct is not None else None,
        "max_drawdown_pct": round(mdd, 2) if mdd is not None else None,
        "closed_trades": len(closed),
        "wins": wins, "losses": losses,
        "win_rate_pct": round(win_rate, 1) if win_rate is not None else None,
        "first": curve[0] if curve else None,
        "last": curve[-1] if curve else None,
    }
