# -*- coding: utf-8 -*-
"""module_paper_book._risk — 리스크 기반 포지션 사이징(결정론).

action_bracket.py 와 동형의 리스크 규약(1트레이드 위험 % · 스탑거리 · 최대비중)을
장부 맥락으로 옮긴 것. 판단(무엇을 살지)은 상위(프로토콜)가 하고, 여기는 '얼마나'만
계산한다(P4). 상관단위(테마) 집중도 가드 = premortem 의 'one risk unit' 교훈을 코드화.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from ._book import Position
from ._config import (
    CORE_RISK_PCT,
    MAX_POS_PCT,
    MAX_THEME_PCT,
    RISK_PCT,
    STOP_PCT,
)


@dataclass
class RiskParams:
    risk_pct: float = RISK_PCT
    core_risk_pct: float = CORE_RISK_PCT
    stop_pct: float = STOP_PCT
    max_pos_pct: float = MAX_POS_PCT
    max_theme_pct: float = MAX_THEME_PCT


def size_position(equity: float, price: float, stop: Optional[float] = None,
                  is_core: bool = False, params: Optional[RiskParams] = None) -> dict:
    """스탑까지의 리스크로 주식수 산출.

    risk_amount = equity * risk_pct/100
    per_share_risk = price - stop (스탑 미지정 시 price * stop_pct/100)
    qty = floor(risk_amount / per_share_risk), 단 max_pos_pct 로 상한.
    """
    p = params or RiskParams()
    if price <= 0:
        return {"qty": 0, "reason": "price<=0"}
    rp = p.core_risk_pct if is_core else p.risk_pct
    risk_amount = equity * rp / 100.0
    if stop and stop < price:
        per_share_risk = price - stop
        stop_used = stop
    else:
        per_share_risk = price * p.stop_pct / 100.0
        stop_used = round(price * (1 - p.stop_pct / 100.0), 4)
    qty_by_risk = int(risk_amount // per_share_risk) if per_share_risk > 0 else 0
    # 최대비중 상한
    max_notional = equity * p.max_pos_pct / 100.0
    qty_by_cap = int(max_notional // price)
    qty = max(0, min(qty_by_risk, qty_by_cap))
    binding = "risk" if qty == qty_by_risk else "max_pos_cap"
    return {
        "qty": qty,
        "price": price,
        "stop": stop_used,
        "per_share_risk": round(per_share_risk, 4),
        "risk_amount": round(risk_amount, 2),
        "notional": round(qty * price, 2),
        "risk_pct_used": rp,
        "binding_constraint": binding,
        "is_core": is_core,
    }


def theme_exposure(positions: list[Position], marks: dict, fx: float) -> dict[str, float]:
    """테마(상관단위)별 원화환산 노출 합계 — 집중도 가드용."""
    agg: dict[str, float] = {}
    for p in positions:
        px = marks.get(p.ticker) or p.avg_cost
        rate = 1.0 if p.currency == "KRW" else fx
        val = px * p.qty * rate
        key = (p.theme or "(untagged)")
        agg[key] = agg.get(key, 0.0) + val
    return agg


def concentration_check(positions: list[Position], marks: dict, equity_krw: float,
                        fx: float, params: Optional[RiskParams] = None) -> list[dict]:
    """단일종목·단일테마 비중 상한 위반을 플래그(premortem one-risk-unit 가드)."""
    p = params or RiskParams()
    flags = []
    if equity_krw <= 0:
        return flags
    # 종목별
    for pos in positions:
        px = marks.get(pos.ticker) or pos.avg_cost
        rate = 1.0 if pos.currency == "KRW" else fx
        pct = px * pos.qty * rate / equity_krw * 100
        if pct > p.max_pos_pct:
            flags.append({"kind": "single_name", "key": pos.ticker,
                          "pct": round(pct, 1), "limit": p.max_pos_pct})
    # 테마별
    for theme, val in theme_exposure(positions, marks, fx).items():
        pct = val / equity_krw * 100
        if pct > p.max_theme_pct:
            flags.append({"kind": "theme_correlated", "key": theme,
                          "pct": round(pct, 1), "limit": p.max_theme_pct})
    return flags
