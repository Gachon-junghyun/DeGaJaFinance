# -*- coding: utf-8 -*-
"""module_paper_book._book — 모의투자 장부의 단일 원본(SQLite).

이 파일이 '장부 상태'의 단일 원본이다(P1): 현금(통화별 슬리브)·포지션·체결원장·
자기자본 스냅샷. 판단은 하지 않는다(P4) — ENTER/EXIT 을 결정하는 건 상위(프로토콜).
여기는 결정론 기입/조회/평가 기계일 뿐. watchlist._db 와 동형의 connect/init 규약.

체결(record_fill)은 항상 명시 호출로만 장부를 바꾼다 — CLI 는 기본 드라이런이고
`--commit` 을 사람이 명시할 때만 이 함수를 실제로 부른다(주문계열 안전규약과 동형).
"""
from __future__ import annotations

import sqlite3
from contextlib import contextmanager
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator, Optional

from ._config import (
    DEFAULT_CAPITAL_KRW,
    DEFAULT_CAPITAL_USD,
    ccy_of,
    default_db_path,
    market_of,
)

_SCHEMA = """
CREATE TABLE IF NOT EXISTS book_meta (
    k TEXT PRIMARY KEY,
    v TEXT
);
CREATE TABLE IF NOT EXISTS cash (
    currency TEXT PRIMARY KEY,          -- 'KRW' | 'USD'
    amount   REAL NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS positions (
    ticker     TEXT PRIMARY KEY,
    market     TEXT NOT NULL,           -- 'KR' | 'US'
    currency   TEXT NOT NULL,
    name       TEXT,
    qty        REAL NOT NULL DEFAULT 0,
    avg_cost   REAL NOT NULL DEFAULT 0, -- 평단(현지통화)
    stop       REAL,                    -- 하드스탑(현지통화)
    theme      TEXT,                    -- 상관단위/테마(집중도 가드용)
    thesis     TEXT,
    source_report TEXT,
    opened_at  TEXT,
    updated_at TEXT
);
CREATE TABLE IF NOT EXISTS transactions (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    ts         TEXT NOT NULL,
    ticker     TEXT NOT NULL,
    market     TEXT NOT NULL,
    currency   TEXT NOT NULL,
    side       TEXT NOT NULL,           -- 'buy' | 'sell'
    qty        REAL NOT NULL,
    price      REAL NOT NULL,           -- 체결가(현지통화)
    fees       REAL NOT NULL DEFAULT 0,
    realized_pnl REAL DEFAULT 0,        -- 매도 시 실현손익(현지통화)
    rationale  TEXT,
    source_report TEXT
);
CREATE TABLE IF NOT EXISTS equity_snapshots (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ts TEXT NOT NULL,
    equity_krw REAL, cash_krw REAL, cash_usd REAL,
    invested_krw REAL, unrealized_krw REAL, fx REAL,
    note TEXT
);
"""


@dataclass
class Position:
    ticker: str
    market: str
    currency: str
    name: Optional[str] = None
    qty: float = 0.0
    avg_cost: float = 0.0
    stop: Optional[float] = None
    theme: Optional[str] = None
    thesis: Optional[str] = None
    source_report: Optional[str] = None
    opened_at: Optional[str] = None
    updated_at: Optional[str] = None

    @property
    def cost_basis(self) -> float:
        return self.qty * self.avg_cost


@dataclass
class Fill:
    ticker: str
    side: str            # 'buy' | 'sell'
    qty: float
    price: float
    fees: float = 0.0
    rationale: str = ""
    source_report: str = ""
    theme: str = ""
    stop: Optional[float] = None
    name: Optional[str] = None
    realized_pnl: float = 0.0
    market: str = field(default="")
    currency: str = field(default="")


def _now() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


@contextmanager
def connect(db_path: Optional[Path] = None) -> Iterator[sqlite3.Connection]:
    path = Path(db_path) if db_path else default_db_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(path))
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def init_db(conn: sqlite3.Connection, capital_krw: float = DEFAULT_CAPITAL_KRW,
            capital_usd: float = DEFAULT_CAPITAL_USD, reset: bool = False) -> None:
    conn.executescript(_SCHEMA)
    if reset:
        for t in ("positions", "transactions", "equity_snapshots", "cash", "book_meta"):
            conn.execute(f"DELETE FROM {t}")
    # 현금 슬리브 초기화(이미 있으면 유지)
    row = conn.execute("SELECT COUNT(*) c FROM cash").fetchone()
    if row["c"] == 0 or reset:
        conn.execute("INSERT OR REPLACE INTO cash(currency, amount) VALUES('KRW', ?)", (capital_krw,))
        conn.execute("INSERT OR REPLACE INTO cash(currency, amount) VALUES('USD', ?)", (capital_usd,))
        conn.execute("INSERT OR REPLACE INTO book_meta(k, v) VALUES('created_at', ?)", (_now(),))
        conn.execute("INSERT OR REPLACE INTO book_meta(k, v) VALUES('init_krw', ?)", (str(capital_krw),))
        conn.execute("INSERT OR REPLACE INTO book_meta(k, v) VALUES('init_usd', ?)", (str(capital_usd),))


def get_cash(conn: sqlite3.Connection, currency: str) -> float:
    r = conn.execute("SELECT amount FROM cash WHERE currency=?", (currency,)).fetchone()
    return float(r["amount"]) if r else 0.0


def _set_cash(conn: sqlite3.Connection, currency: str, amount: float) -> None:
    conn.execute("INSERT OR REPLACE INTO cash(currency, amount) VALUES(?, ?)", (currency, amount))


def get_positions(conn: sqlite3.Connection, open_only: bool = True) -> list[Position]:
    rows = conn.execute("SELECT * FROM positions ORDER BY ticker").fetchall()
    out = []
    for r in rows:
        if open_only and (r["qty"] or 0) == 0:
            continue
        out.append(Position(
            ticker=r["ticker"], market=r["market"], currency=r["currency"], name=r["name"],
            qty=r["qty"], avg_cost=r["avg_cost"], stop=r["stop"], theme=r["theme"],
            thesis=r["thesis"], source_report=r["source_report"],
            opened_at=r["opened_at"], updated_at=r["updated_at"],
        ))
    return out


def get_position(conn: sqlite3.Connection, ticker: str) -> Optional[Position]:
    ps = [p for p in get_positions(conn, open_only=False) if p.ticker == ticker.upper()]
    return ps[0] if ps else None


def record_fill(conn: sqlite3.Connection, fill: Fill) -> dict:
    """체결 1건을 장부에 반영(현금·평단·실현손익 갱신). 판단 없음 — 순수 기입.

    buy  : 현금 감소, 평단 가중평균 갱신, qty 증가.
    sell : 현금 증가, 실현손익 = (매도가-평단)*수량, qty 감소(0이면 청산).
    """
    t = fill.ticker.upper()
    fill.market = fill.market or market_of(t)
    fill.currency = fill.currency or ccy_of(t)
    ccy = fill.currency
    pos = get_position(conn, t)
    now = _now()
    notional = fill.qty * fill.price

    if fill.side == "buy":
        # 현금 검증(음수 방지는 상위 SIZE 가 하지만 여기서도 가드)
        cash = get_cash(conn, ccy)
        cost = notional + fill.fees
        _set_cash(conn, ccy, cash - cost)
        if pos and pos.qty > 0:
            new_qty = pos.qty + fill.qty
            new_avg = (pos.cost_basis + notional) / new_qty
            conn.execute(
                "UPDATE positions SET qty=?, avg_cost=?, stop=COALESCE(?,stop), "
                "theme=COALESCE(?,theme), thesis=COALESCE(?,thesis), "
                "source_report=COALESCE(?,source_report), updated_at=? WHERE ticker=?",
                (new_qty, new_avg, fill.stop, fill.theme or None, fill.rationale or None,
                 fill.source_report or None, now, t),
            )
        else:
            conn.execute(
                "INSERT OR REPLACE INTO positions(ticker,market,currency,name,qty,avg_cost,"
                "stop,theme,thesis,source_report,opened_at,updated_at) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                (t, fill.market, ccy, fill.name, fill.qty, fill.price, fill.stop,
                 fill.theme or None, fill.rationale or None, fill.source_report or None, now, now),
            )
        realized = 0.0
    else:  # sell
        if not pos or pos.qty <= 0:
            raise ValueError(f"{t}: 보유 없음 — 매도 불가")
        sell_qty = min(fill.qty, pos.qty)
        realized = (fill.price - pos.avg_cost) * sell_qty
        cash = get_cash(conn, ccy)
        _set_cash(conn, ccy, cash + (sell_qty * fill.price) - fill.fees)
        remaining = pos.qty - sell_qty
        if remaining <= 1e-9:
            conn.execute("UPDATE positions SET qty=0, updated_at=? WHERE ticker=?", (now, t))
        else:
            conn.execute("UPDATE positions SET qty=?, updated_at=? WHERE ticker=?", (remaining, now, t))
        fill.realized_pnl = realized

    conn.execute(
        "INSERT INTO transactions(ts,ticker,market,currency,side,qty,price,fees,realized_pnl,"
        "rationale,source_report) VALUES(?,?,?,?,?,?,?,?,?,?,?)",
        (now, t, fill.market, ccy, fill.side, fill.qty, fill.price, fill.fees,
         fill.realized_pnl, fill.rationale, fill.source_report),
    )
    return {"ticker": t, "side": fill.side, "qty": fill.qty, "price": fill.price,
            "currency": ccy, "realized_pnl": fill.realized_pnl,
            "cash_after": get_cash(conn, ccy)}


def snapshot_equity(conn: sqlite3.Connection, marks: dict, fx: float, note: str = "") -> dict:
    """현재 장부를 마크 결과(marks: ticker->price)로 평가해 자기자본 스냅샷 기록.

    marks 는 _mark.mark_book 이 만든 현지통화 현재가 dict. 총자산은 원화환산.
    """
    cash_krw = get_cash(conn, "KRW")
    cash_usd = get_cash(conn, "USD")
    invested_krw = 0.0
    unreal_krw = 0.0
    for p in get_positions(conn, open_only=True):
        px = marks.get(p.ticker)
        rate = 1.0 if p.currency == "KRW" else fx
        invested_krw += p.cost_basis * rate
        if px is not None:
            unreal_krw += (px - p.avg_cost) * p.qty * rate
    equity_krw = cash_krw + cash_usd * fx + invested_krw + unreal_krw
    now = _now()
    conn.execute(
        "INSERT INTO equity_snapshots(ts,equity_krw,cash_krw,cash_usd,invested_krw,"
        "unrealized_krw,fx,note) VALUES(?,?,?,?,?,?,?,?)",
        (now, equity_krw, cash_krw, cash_usd, invested_krw, unreal_krw, fx, note),
    )
    return {"ts": now, "equity_krw": equity_krw, "cash_krw": cash_krw, "cash_usd": cash_usd,
            "invested_krw": invested_krw, "unrealized_krw": unreal_krw, "fx": fx}


def book_summary(conn: sqlite3.Connection) -> dict:
    """마크 없이 장부 원장 요약(현금·포지션·실현손익 누계)."""
    positions = get_positions(conn, open_only=True)
    realized = conn.execute("SELECT COALESCE(SUM(realized_pnl),0) s FROM transactions").fetchone()["s"]
    meta = {r["k"]: r["v"] for r in conn.execute("SELECT k,v FROM book_meta").fetchall()}
    return {
        "cash_krw": get_cash(conn, "KRW"),
        "cash_usd": get_cash(conn, "USD"),
        "positions": positions,
        "n_positions": len(positions),
        "realized_pnl_native_sum": realized,
        "meta": meta,
    }
