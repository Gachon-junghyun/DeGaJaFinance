# -*- coding: utf-8 -*-
"""합성 흐름태그 — 4축(②③④+①) + KR 실측 수급 ⑦ + 공매도잔고 ⑧ 보정 → 🟢/🟡/🔴.

★ ⑦ 실측 투자자별 수급(KR)이 OBV 추론을 덮어쓴다 — '누가' 사는지가 우선.
⚠️ 🟢가속이라도 진입은 하드스탑 필수(기대감=꼭지위험). 4Phase '바닥'과 교차해서 봐라.
"""
from __future__ import annotations


def flow_tag(p: dict, vel, inv: dict | None = None, sh: dict | None = None) -> str:
    if "error" in p:
        return "?"
    green = sum([
        p["obv_state"] == "매집",
        (p["rs20"] or 0) > 0,
        p["vol_surge"] >= 1.2,
        (vel or 0) >= 1.2,
    ])
    red = sum([
        p["obv_state"] == "분산",
        (p["rs20"] or 0) < -2,
        (vel is not None and vel < 0.7),
    ])
    # 🟢 게이트: 단순 4축 다수결이 아니라, 수급(OBV 매집) 또는 관심(뉴스속도) 중 하나는 반드시 +
    # (순수 가격추격 — RS+서지만 green — 은 🟡로 강등; 검증 보정).
    has_conviction = (p["obv_state"] == "매집") or ((vel or 0) >= 1.2)

    # ★ ⑦ 실측 투자자별 수급(KR)이 OBV 추론을 덮어쓴다.
    if inv and "error" not in inv:
        if inv.get("distribution_to_retail"):
            # 외국인 이탈 + 개인 흡수 = 분배. OBV '매집'은 약한손 물량이므로 green에서 박탈하고
            # 컨비션 불인정(뉴스 열기만으론 🟢 불가). red 가중.
            if p["obv_state"] == "매집":
                green -= 1
            has_conviction = False
            red += 1
        elif inv.get("smart_buy"):
            # 외국인/기관 순매수 = 실측 컨비션(OBV 중립이어도 진짜 돈 유입).
            has_conviction = True
            green += 1

    # ★ ⑧ 공매도잔고(KR) — building+notable이면 하락압력.
    if sh and "error" not in sh:
        if sh.get("trend") == "building" and sh.get("notable"):
            red += 1

    if green >= 3 and has_conviction:
        return "🟢가속"
    if red >= 2 and green <= 1:
        return "🔴분산"
    return "🟡중립"
