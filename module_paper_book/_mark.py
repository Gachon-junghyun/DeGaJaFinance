# -*- coding: utf-8 -*-
"""module_paper_book._mark — 장부 시가평가(mark-to-market).

가격 소스는 재사용(P1): KR 6자리 → module_KIS.fetch_quote(인증 소스), US 티커 →
yfinance(빠르고 거래소코드 불필요; module_chart 도 yfinance 사용). KIS US 시세는
거래소코드(excd) 매핑이 필요해 마크 용도로는 yfinance 가 실용적 — 주문이 아니라
평가이므로 무인증 채널로 충분(주문계열만 KIS 인증 필수).

판단 없음(P4): 현재가만 돌려준다. 손익 해석은 상위.
"""
from __future__ import annotations

import sqlite3
from typing import Optional

from ._book import Position, get_positions
from ._config import is_kr_ticker


def get_price(ticker: str) -> Optional[float]:
    """현지통화 현재가. 실패하면 None(블랭크는 블랭크 — 추정 금지)."""
    t = ticker.strip().upper()
    if is_kr_ticker(t):
        try:
            from module_KIS import fetch_quote
            q = fetch_quote(t)
            return float(q.price) if getattr(q, "price", None) is not None else None
        except Exception:
            return None
    # US → yfinance
    try:
        import yfinance as yf
        hist = yf.Ticker(t).history(period="5d")
        if len(hist) and not hist["Close"].dropna().empty:
            return float(hist["Close"].dropna().iloc[-1])
    except Exception:
        return None
    return None


def price_move(ticker: str) -> dict:
    """현재가 + 당일(1d)·5일 등락 — '지금 나락인가' 라이브 진단용.

    yfinance 7d 일봉으로 last / 1d% / 5d% 산출. 실패 시 값 None(추정 금지).
    KR 6자리는 .KS 접미사로 조회(무인증 라이브 진단이라 yfinance 사용).
    """
    t = ticker.strip().upper()
    yq = f"{t}.KS" if (len(t) == 6 and t.isdigit()) else t
    try:
        import yfinance as yf
        h = yf.Ticker(yq).history(period="7d")["Close"].dropna()
        if len(h) < 2:
            return {"ticker": t, "price": None, "chg_1d": None, "chg_5d": None}
        last = float(h.iloc[-1])
        return {"ticker": t, "price": last,
                "chg_1d": (last / float(h.iloc[-2]) - 1) * 100,
                "chg_5d": (last / float(h.iloc[0]) - 1) * 100}
    except Exception:
        return {"ticker": t, "price": None, "chg_1d": None, "chg_5d": None}


def mark_book(conn: sqlite3.Connection, fallback: Optional[dict] = None) -> dict:
    """열린 포지션 전부를 시가평가. 반환: ticker -> price(현지통화).

    fallback: {ticker: price} — 시세 실패 시 리포트 진입가 등으로 대체(있으면).
    """
    fallback = fallback or {}
    marks: dict[str, Optional[float]] = {}
    for p in get_positions(conn, open_only=True):
        px = get_price(p.ticker)
        if px is None:
            px = fallback.get(p.ticker)
        marks[p.ticker] = px
    return marks


def position_pnl(p: Position, price: Optional[float]) -> dict:
    """포지션 1개의 손익/스탑거리(현지통화). price None 이면 미평가."""
    if price is None:
        return {"ticker": p.ticker, "price": None, "unrealized": None,
                "unrealized_pct": None, "stop_dist_pct": None}
    unreal = (price - p.avg_cost) * p.qty
    unreal_pct = (price / p.avg_cost - 1) * 100 if p.avg_cost else None
    stop_dist = None
    if p.stop:
        stop_dist = (price / p.stop - 1) * 100
    return {"ticker": p.ticker, "price": price, "unrealized": unreal,
            "unrealized_pct": unreal_pct, "stop_dist_pct": stop_dist,
            "stop_hit": (p.stop is not None and price <= p.stop)}
