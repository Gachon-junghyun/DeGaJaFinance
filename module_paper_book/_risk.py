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
    REPO_ROOT,
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


def load_measured_units(max_age_days: int = 14) -> tuple[dict, dict]:
    """가장 최근 `RISK_UNITS.json` 의 실측 위험단위를 읽는다 — **재계산하지 않는다**(P1).

    그 산출은 `scripts/risk_units.py` 소유. 없으면 `({}, {...})` 를 돌려주고 호출부는 라벨
    기준으로만 동작한다 — 조용한 폴백이 아니라 **사유를 meta 에 실어** 보낸다(P4).
    """
    import json as _json
    from datetime import date as _date

    root = REPO_ROOT / "llm_outputs"
    cands = sorted(root.glob("*/RISK_UNITS.json"), reverse=True) if root.exists() else []
    if not cands:
        return {}, {"note": "RISK_UNITS.json 없음 — `python -X utf8 scripts/risk_units.py --book` 먼저"}
    try:
        d = _json.loads(cands[0].read_text(encoding="utf-8"))
    except Exception as e:
        return {}, {"note": f"RISK_UNITS.json 읽기 실패: {e}", "path": str(cands[0])}
    meta = {"path": str(cands[0]), "date": d.get("date"), "bench": d.get("bench"),
            "threshold": d.get("threshold"), "ari": d.get("ari_half_vs_half"),
            "n_days": d.get("n_days_aligned")}
    try:
        age = (_date.today() - _date.fromisoformat(str(d.get("date")))).days
        meta["age_days"] = age
        if age > max_age_days:
            meta["stale"] = True
            meta["note"] = f"{age}일 경과 — 위험단위는 창 선택에 민감하다(--days). 재측정 권장"
    except Exception:
        pass
    return (d.get("units") or {}), meta


def measured_unit_exposure(positions: list[Position], marks: dict, fx: float,
                           units: dict[str, list[str]]) -> dict[str, float]:
    """**실측** 위험단위별 노출 — 손으로 붙인 테마 라벨이 아니라 벤치 잔차상관 군집으로 묶는다.

    `units` 는 `scripts/risk_units.py` 가 쓰는 `RISK_UNITS.json` 의 `units` 필드 형식
    (`{"0": ["AVGO","NVDA","TSM"], "1": ["KMI","LNG"], …}`) — 재계산하지 않고 읽어 쓴다(P1).
    """
    member_of: dict[str, str] = {}
    for uid, members in (units or {}).items():
        for t in members:
            member_of[t] = str(uid)
    agg: dict[str, float] = {}
    for pos in positions:
        px = marks.get(pos.ticker) or pos.avg_cost
        rate = 1.0 if pos.currency == "KRW" else fx
        val = px * pos.qty * rate
        key = member_of.get(pos.ticker, f"(unmeasured:{pos.ticker})")
        agg[key] = agg.get(key, 0.0) + val
    return agg


def label_unit_mismatch(positions: list[Position], units: dict[str, list[str]]) -> list[dict]:
    """**D9** — 라벨이 세는 단위와 시장이 움직이는 단위가 갈리는 지점을 낸다.

    `MAX_THEME_PCT` 가 세는 것은 사람이 포지션에 적어 넣은 `theme` 문자열이다. 그래서
    **모회사와 자회사가 서로 다른 테마 라벨을 달면 서로 다른 위험단위로 계산된다** —
    PLAY15 실측: 상위 20개 상관쌍 중 **6개가 지주–자회사**(LS · 한미사이언스 · 영원무역홀딩스 ·
    HD한국조선해양 ×2 · GS)이고, KRX 가 지주를 *금융*으로 분류해 섹터 축에서도 섞인다.

    ★ 그런데 **지주 매핑표를 만들 필요가 없다.** 잔차상관이 임계를 넘으면 지주든 아니든
    `risk_units` 가 자동으로 한 단위로 병합한다. 빠져 있던 것은 표가 아니라 **배선**이다.
    이 함수는 그 두 세는 법이 **갈리는 곳만** 돌려준다 — 어느 쪽이 옳은지는 말하지 않는다(P4).
    ⚠ 실측된 단위 자체가 `--days` 선택에 민감하다(2026-08-09: 250일이면 5단위, 500/750일이면
    7단위로 갈린다) ⇒ 라벨을 **대체**하지 않고 **나란히 놓는다.**
    """
    member_of: dict[str, str] = {}
    for uid, members in (units or {}).items():
        for t in members:
            member_of[t] = str(uid)

    out: list[dict] = []
    # ① 한 실측단위가 여러 테마 라벨에 걸친다 = 라벨이 과다분할(지주–자회사 전형)
    by_unit: dict[str, set[str]] = {}
    for pos in positions:
        uid = member_of.get(pos.ticker)
        if uid is None:
            continue
        by_unit.setdefault(uid, set()).add(pos.theme or "(untagged)")
    for uid, themes in by_unit.items():
        if len(themes) > 1:
            out.append({"kind": "unit_split_across_labels", "unit": uid,
                        "labels": sorted(themes),
                        "members": sorted(units.get(uid, [])),
                        "note": "시장은 한 단위로 움직이는데 라벨은 나뉘어 있다 — 상한이 헐거워진다"})
    # ② 한 테마 라벨이 여러 실측단위에 걸친다 = 라벨이 과다병합
    by_label: dict[str, set[str]] = {}
    for pos in positions:
        uid = member_of.get(pos.ticker)
        if uid is None:
            continue
        by_label.setdefault(pos.theme or "(untagged)", set()).add(uid)
    for lbl, uids in by_label.items():
        if len(uids) > 1:
            out.append({"kind": "label_split_across_units", "label": lbl,
                        "units": sorted(uids),
                        "note": "라벨은 하나인데 시장은 여러 단위로 움직인다 — 상한이 과하게 조인다"})
    return out


def concentration_check(positions: list[Position], marks: dict, equity_krw: float,
                        fx: float, params: Optional[RiskParams] = None,
                        units: Optional[dict[str, list[str]]] = None) -> list[dict]:
    """단일종목·단일테마 비중 상한 위반을 플래그(premortem one-risk-unit 가드).

    `units` 를 주면 **실측 위험단위 기준 집중도**를 같은 상한으로 한 번 더 재고(D9),
    라벨과 실측이 갈리는 지점을 함께 낸다. 주지 않으면 이전과 동일하게 동작한다.
    """
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
    # 테마별(라벨)
    for theme, val in theme_exposure(positions, marks, fx).items():
        pct = val / equity_krw * 100
        if pct > p.max_theme_pct:
            flags.append({"kind": "theme_correlated", "key": theme,
                          "pct": round(pct, 1), "limit": p.max_theme_pct})
    # 실측 위험단위별 (D9) — 라벨을 대체하지 않고 나란히
    if units:
        for uid, val in measured_unit_exposure(positions, marks, fx, units).items():
            pct = val / equity_krw * 100
            if pct > p.max_theme_pct:
                flags.append({"kind": "measured_unit", "key": uid,
                              "members": sorted(units.get(uid, [])),
                              "pct": round(pct, 1), "limit": p.max_theme_pct})
        flags.extend(label_unit_mismatch(positions, units))
    return flags
