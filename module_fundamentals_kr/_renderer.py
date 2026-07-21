# -*- coding: utf-8 -*-
"""재무제표 + 수익의 질 → 마크다운. 판정은 쓰지 않는다(P4) — 관측값·출처·신선도만."""
from __future__ import annotations

from typing import Optional

from ._dart_fin import Financials
from ._quality import QualityMetrics

REPRT_LABEL = {
    "11011": "사업보고서(연간)",
    "11012": "반기보고서",
    "11013": "1분기보고서",
    "11014": "3분기보고서",
}


def _won(x: Optional[float]) -> str:
    """원 단위 금액 → 조/억 표기."""
    if x is None:
        return "n/a"
    sign = "-" if x < 0 else ""
    a = abs(x)
    if a >= 1e12:
        return f"{sign}{a / 1e12:,.2f}조원"
    if a >= 1e8:
        return f"{sign}{a / 1e8:,.0f}억원"
    return f"{sign}{a:,.0f}원"


def _pct(x: Optional[float], digits: int = 1) -> str:
    return "n/a" if x is None else f"{x * 100:.{digits}f}%"


def _ratio(x: Optional[float]) -> str:
    return "n/a" if x is None else f"{x:.2f}"


def render_markdown(m: QualityMetrics) -> str:
    fin: Financials = m.fin
    v, p = fin.value, fin.prev
    L: list[str] = []

    title = fin.corp_name or fin.corp_code
    L.append(f"# {title} — 재무제표 · 수익의 질")
    L.append("")
    L.append(
        f"- 출처: DART 전체재무제표 API (fnlttSinglAcntAll), corp_code={fin.corp_code}"
    )
    L.append(
        f"- 기준: {fin.bsns_year}년 {REPRT_LABEL.get(fin.reprt_code, fin.reprt_code)} · "
        f"{'연결(CFS)' if fin.fs_div == 'CFS' else '별도(OFS)'} · 계정 {fin.raw_count}건"
    )
    L.append("")

    L.append("## 손익 · 현금")
    L.append("")
    L.append("| 계정 | 당기 | 전기 |")
    L.append("|---|---|---|")
    for key, label in [
        ("revenue", "매출액"),
        ("gross_profit", "매출총이익"),
        ("operating_income", "영업이익"),
        ("net_income", "당기순이익"),
        ("ocf", "영업활동현금흐름"),
        ("icf", "투자활동현금흐름"),
    ]:
        if v(key) is None and p(key) is None:
            continue
        L.append(f"| {label} | {_won(v(key))} | {_won(p(key))} |")
    L.append("")

    L.append("## 수익의 질 (Block B2)")
    L.append("")
    L.append("| 지표 | 값 | 읽는 법 |")
    L.append("|---|---|---|")
    L.append(
        f"| OCF / 영업이익 | {_ratio(m.ocf_to_op)} | 1.0 근처면 이익이 현금으로 온다. 음수면 안 온다. |"
    )
    L.append(
        f"| 발생액비율 (영업이익-OCF)/자산 | {_pct(m.accrual_ratio)} | 높을수록 장부-현금 간극이 크다. |"
    )
    L.append(f"| 매출채권 / 매출 | {_pct(m.receivables_to_revenue)} | 회수 속도. |")
    L.append(f"| 매출 증가율 | {_pct(m.revenue_growth)} | 아래 증가율들의 기준선. |")
    L.append("")

    if m.is_contract_business:
        L.append("### 수주산업 — 진행률 인식의 잔여물")
        L.append("")
        L.append("| 지표 | 당기 | 전기 |")
        L.append("|---|---|---|")
        L.append(f"| 미청구공사(계약자산) | {_won(v('unbilled'))} | {_won(p('unbilled'))} |")
        L.append(f"| 미청구공사 / 매출 | {_pct(m.unbilled_to_revenue)} | {_pct(m.unbilled_prev_ratio)} |")
        L.append(f"| 초과청구공사(계약부채) | {_won(v('overbilled'))} | {_won(p('overbilled'))} |")
        L.append(f"| 순계약포지션 (미청구-초과청구) | {_won(m.net_contract_position)} | — |")
        L.append(f"| 미청구 증가율 | {_pct(m.unbilled_growth)} | — |")
        L.append(f"| 미청구 증가율 - 매출 증가율 | {_pct(m.unbilled_gap)} | — |")
        L.append("")
        L.append(
            "> 미청구공사는 진행률로 매출을 인식했지만 아직 청구하지 못한 금액이다. "
            "매출보다 빠르게 늘면 공기지연·정산분쟁·원가초과 이연 중 하나이며, "
            "해소되지 않으면 대손으로 간다."
        )
        L.append("")

    if m.flags:
        L.append("## 플래그")
        L.append("")
        for f in m.flags:
            mark = "⚠️" if f.level == "warn" else "ℹ️"
            L.append(f"- {mark} **{f.code}** — {f.message}")
        L.append("")

    L.append("---")
    L.append("")
    L.append(
        "*지표는 결정론 산출이다. 매매 판단은 하지 않는다 — 플래그는 '읽어봐야 할 곳' 표식이지 신호가 아니다.*"
    )
    L.append("")
    return "\n".join(L)
