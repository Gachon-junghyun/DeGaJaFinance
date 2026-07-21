# -*- coding: utf-8 -*-
"""수익의 질(Quality of Earnings) — 이익이 현금으로 오는가.

이 파일이 답하는 질문은 하나다: **장부 이익과 실제 현금의 간극이 어디서 벌어지나.**
수주산업(건설·조선·플랜트)에서 그 간극은 대개 **미청구공사(계약자산)** 에 고인다 —
진행률로 매출을 먼저 인식했지만 발주처에 아직 청구하지 못한 금액이다. 매출보다 빨리
늘면 (a) 공기 지연 (b) 발주처와의 정산 분쟁 (c) 원가 초과의 이연 중 하나이고, 결국
대손으로 털린다. 그래서 **미청구공사/매출 비율과 그 YoY 방향**이 건설사 수익의 질의
1번 지표다.

판정은 하지 않는다(P4) — 지표와 근거만 낸다. 임계값은 '주의를 어디로 돌릴지'의
휴리스틱이지 매매 신호가 아니며, 각 플래그는 무엇이 참이면 발동했는지 문장으로 남긴다.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from ._dart_fin import Financials

# 휴리스틱 임계값 — 업계 통념(미청구/매출 20%↑면 수주산업에서 통상 경고) 기준.
# 절대선이 아니라 '읽어봐야 할 곳' 표식이다.
UNBILLED_RATIO_WARN = 0.20
UNBILLED_GROWTH_GAP_WARN = 0.10   # 미청구 증가율 - 매출 증가율
ACCRUAL_RATIO_WARN = 0.10         # (영업이익-OCF)/자산


def _safe_div(a: Optional[float], b: Optional[float]) -> Optional[float]:
    if a is None or b is None or b == 0:
        return None
    return a / b


def _growth(cur: Optional[float], prev: Optional[float]) -> Optional[float]:
    if cur is None or prev is None or prev == 0:
        return None
    return (cur - prev) / abs(prev)


@dataclass
class Flag:
    level: str        # "warn" | "info"
    code: str
    message: str      # 무엇이 참이라 발동했는지


@dataclass
class QualityMetrics:
    fin: Financials

    # 발생액 — 이익과 현금의 간극
    ocf_to_op: Optional[float] = None          # 영업현금흐름 / 영업이익
    accrual_ratio: Optional[float] = None      # (영업이익 - OCF) / 총자산

    # 수주산업 전용
    unbilled_to_revenue: Optional[float] = None
    unbilled_prev_ratio: Optional[float] = None
    unbilled_growth: Optional[float] = None
    revenue_growth: Optional[float] = None
    unbilled_gap: Optional[float] = None       # 미청구 증가율 - 매출 증가율
    overbilled_to_revenue: Optional[float] = None
    net_contract_position: Optional[float] = None  # 미청구 - 초과청구

    # 운전자본
    receivables_to_revenue: Optional[float] = None
    receivables_growth: Optional[float] = None

    flags: list[Flag] = field(default_factory=list)

    @property
    def is_contract_business(self) -> bool:
        """미청구/초과청구 계정이 잡히면 수주산업으로 본다."""
        return self.fin.value("unbilled") is not None or self.fin.value("overbilled") is not None


def compute(fin: Financials) -> QualityMetrics:
    m = QualityMetrics(fin=fin)
    v, p = fin.value, fin.prev

    revenue, op, ocf = v("revenue"), v("operating_income"), v("ocf")
    assets = v("total_assets")
    unbilled, overbilled, receivables = v("unbilled"), v("overbilled"), v("receivables")

    m.ocf_to_op = _safe_div(ocf, op)
    if op is not None and ocf is not None and assets:
        m.accrual_ratio = (op - ocf) / assets

    m.revenue_growth = _growth(revenue, p("revenue"))
    m.unbilled_to_revenue = _safe_div(unbilled, revenue)
    m.unbilled_prev_ratio = _safe_div(p("unbilled"), p("revenue"))
    m.unbilled_growth = _growth(unbilled, p("unbilled"))
    if m.unbilled_growth is not None and m.revenue_growth is not None:
        m.unbilled_gap = m.unbilled_growth - m.revenue_growth
    m.overbilled_to_revenue = _safe_div(overbilled, revenue)
    if unbilled is not None and overbilled is not None:
        m.net_contract_position = unbilled - overbilled

    m.receivables_to_revenue = _safe_div(receivables, revenue)
    m.receivables_growth = _growth(receivables, p("receivables"))

    m.flags = _flags(m)
    return m


def _pct(x: Optional[float]) -> str:
    return "n/a" if x is None else f"{x * 100:.1f}%"


def _flags(m: QualityMetrics) -> list[Flag]:
    out: list[Flag] = []

    if m.ocf_to_op is not None and m.ocf_to_op < 0:
        out.append(Flag(
            "warn", "ocf_negative",
            f"영업이익은 흑자인데 영업활동현금흐름이 음수 (OCF/영업이익 {m.ocf_to_op:.2f}) "
            "— 이익이 현금으로 돌아오지 않았다.",
        ))
    elif m.ocf_to_op is not None and m.ocf_to_op < 0.5:
        out.append(Flag(
            "warn", "ocf_thin",
            f"영업이익 대비 영업현금흐름이 절반 미만 (OCF/영업이익 {m.ocf_to_op:.2f}).",
        ))

    if m.accrual_ratio is not None and m.accrual_ratio > ACCRUAL_RATIO_WARN:
        out.append(Flag(
            "warn", "accrual_high",
            f"발생액비율 {_pct(m.accrual_ratio)} > {_pct(ACCRUAL_RATIO_WARN)} "
            "— 총자산 대비 이익-현금 간극이 크다.",
        ))

    if m.unbilled_to_revenue is not None and m.unbilled_to_revenue > UNBILLED_RATIO_WARN:
        out.append(Flag(
            "warn", "unbilled_heavy",
            f"미청구공사/매출 {_pct(m.unbilled_to_revenue)} > {_pct(UNBILLED_RATIO_WARN)} "
            "— 인식했으나 청구 못 한 매출 비중이 높다.",
        ))

    if m.unbilled_gap is not None and m.unbilled_gap > UNBILLED_GROWTH_GAP_WARN:
        out.append(Flag(
            "warn", "unbilled_outpacing",
            f"미청구공사 증가율({_pct(m.unbilled_growth)})이 매출 증가율({_pct(m.revenue_growth)})을 "
            f"{_pct(m.unbilled_gap)}p 앞선다 — 공기지연·정산분쟁·원가초과 이연 의심 구간.",
        ))
    elif m.unbilled_growth is not None and m.unbilled_growth < 0:
        out.append(Flag(
            "info", "unbilled_declining",
            f"미청구공사가 전기 대비 {_pct(m.unbilled_growth)} 감소 — 청구·회수가 진행됐다.",
        ))

    if m.receivables_growth is not None and m.revenue_growth is not None and \
            m.receivables_growth - m.revenue_growth > UNBILLED_GROWTH_GAP_WARN:
        out.append(Flag(
            "warn", "receivables_outpacing",
            f"매출채권이 매출보다 {_pct(m.receivables_growth - m.revenue_growth)}p 빠르게 움직였다 "
            f"(매출채권 {_pct(m.receivables_growth)} vs 매출 {_pct(m.revenue_growth)}) "
            "— 매출 대비 채권 비중이 늘었다(회수 지연).",
        ))

    missing = [k for k in ("revenue", "operating_income", "ocf") if m.fin.value(k) is None]
    if missing:
        out.append(Flag("info", "missing_accounts", f"핵심 계정 결측: {', '.join(missing)} — 지표 일부 계산 불가."))

    return out
