# -*- coding: utf-8 -*-
"""⑦ 투자자별 순매수 (개인/외국인/기관) — KIS, 국내 전용. OBV가 못 가리는 '누가'.

OBV는 가격×거래량 추론이라 외국인 매집인지 개인이 물량 받는지 구분 못 한다.
이건 실측(KRX 투자자별 매매동향)이라 스마트머니(외국인·기관) 방향을 직접 본다.
반환: None = KR 아님(US 등, 무영향) · {"error":..} = KR인데 조회 실패(크레덴셜/네트워크→n/a).
"""
from __future__ import annotations

from ._config import kr_code, load_kis_env


def investor_flow(tk: str, days: int = 20) -> dict | None:
    code = kr_code(tk)
    if not code:
        return None
    try:
        load_kis_env()
        from module_KIS._investor import fetch_investor_trend, net_summary
    except Exception as e:
        return {"error": f"module_KIS 로드 실패: {str(e)[:40]}"}
    try:
        rows = fetch_investor_trend(code, days=days)
        if not rows:
            return {"error": "no data"}
        cum = net_summary(rows)                              # 기간 누적(주)
        recent = rows[-5:] if len(rows) >= 5 else rows
        f5 = sum(r.foreign_qty or 0 for r in recent)         # 최근5일 외국인
        i5 = sum(r.institution_qty or 0 for r in recent)
        f20, inst20, indiv20 = cum["foreign"], cum["institution"], cum["individual"]
        smart20 = f20 + inst20                               # 외국인+기관 = 스마트머니
        distribution = (f20 < 0 and indiv20 > 0)             # 외국인 이탈+개인 흡수 = 분배(약한손)
        if smart20 > 0:
            state = "외국인/기관 순매수"
        elif distribution:
            state = "⚠개인 흡수(외국인 이탈)"                 # ← OBV '매집' 오독의 진원
        else:
            state = "혼조"
        return {
            "foreign_20": f20, "inst_20": inst20, "indiv_20": indiv20,
            "foreign_5": f5, "inst_5": i5,
            "smart_buy": smart20 > 0,
            "distribution_to_retail": distribution,
            "foreign_turning": (f20 < 0 and f5 > 0),         # 20일 매도인데 최근5일 매수전환=턴 신호
            "state": state, "days": cum["days"],
        }
    except Exception as e:
        return {"error": str(e)[:60]}
