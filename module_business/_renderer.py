"""BusinessOverview + IR articles → State Report 블록 5 markdown 자동 생성."""
from __future__ import annotations

from typing import Optional

from ._section_extract import BusinessOverview
from ._ir_news import IRArticle, render_ir_summary


def _format_amount(amount_million: Optional[int]) -> str:
    """백만원 단위 → 한국 통화 표기.

    1조 = 1,000,000 백만원
    1억 = 100 백만원
    """
    if amount_million is None:
        return "—"
    if amount_million >= 1_000_000:  # 1조 이상
        return f"{amount_million / 1_000_000:,.2f}조"
    if amount_million >= 100:  # 1억 이상
        return f"{amount_million / 100:,.0f}억"
    return f"{amount_million:,}백만"


def render_revenue_table(overview: BusinessOverview) -> str:
    """매출 비중 표 → markdown 표. 표 추출 실패 시 narrative grep fallback."""
    if not overview.revenue_table:
        if overview.revenue_narrative:
            bullets = "\n".join(f"- {s}" for s in overview.revenue_narrative)
            return (
                "_매출 분해 표 자동 추출 실패 — section_text 본문에서 매출 관련 문장 grep:_\n\n"
                f"{bullets}\n"
            )
        return "_매출 분해 표 추출 실패 — section_text 또는 DART 본문 직접 확인 필요._\n"

    head = "| 사업부문 | 매출유형 | 품목 | 매출액 | 비중 |\n|---|---|---|---:|---:|\n"
    rows: list[str] = []
    for r in overview.revenue_table:
        amount_str = _format_amount(r.amount_million)
        ratio_str = f"{r.ratio_pct:.2f}%" if r.ratio_pct is not None else "—"
        rows.append(
            f"| {r.segment} | {r.sales_type or '—'} | {r.item or '—'} | {amount_str} | {ratio_str} |"
        )
    meta = []
    if overview.revenue_basis_date:
        meta.append(f"기준일 {overview.revenue_basis_date}")
    if overview.revenue_unit:
        meta.append(f"단위 {overview.revenue_unit}")
    meta_str = f" ({', '.join(meta)})" if meta else ""
    return f"### 매출 분해{meta_str}\n\n{head}{chr(10).join(rows)}\n"


def render_business_model(
    overview: BusinessOverview,
    ir_articles: Optional[list[IRArticle]] = None,
    *,
    include_overview: bool = True,
    include_capacity: bool = True,
    include_materials: bool = False,
) -> str:
    """전체 markdown 렌더 (State Report 블록 5 직접 paste 용)."""
    parts: list[str] = []
    parts.append(f"# {overview.corp_name} ({overview.ticker}) — 사업 모델 (Phase B' 산출물)")
    parts.append(f"_section_text 길이 {overview.section_length:,}자, 매출 표 추출: {'OK' if overview.extracted_ok else 'FAIL'}_\n")

    if include_overview and overview.overview_text:
        parts.append("## 1. 사업의 개요\n")
        parts.append(overview.overview_text)
        parts.append("\n")

    parts.append("## 2. 매출 구조\n")
    parts.append(render_revenue_table(overview))

    if include_capacity and overview.raw_capacity_text:
        parts.append("## 3. 생산능력\n")
        parts.append("```")
        parts.append(overview.raw_capacity_text[:1500])
        parts.append("```\n")

    if include_materials and overview.raw_materials_text:
        parts.append("## 4. 주요 원재료·매입처\n")
        parts.append("```")
        parts.append(overview.raw_materials_text[:1500])
        parts.append("```\n")

    if ir_articles is not None:
        parts.append("## 5. Q1 매출 모멘텀 (IR/실적 보도자료)\n")
        parts.append(render_ir_summary(ir_articles))

    return "\n".join(parts)


def render_state_report_block(overview: BusinessOverview) -> str:
    """State Report 블록 5에 한 행으로 들어갈 표용 한 줄 발췌.

    형식: `| {종목} | {매출구조 요약} | {핵심제품} | {판로} | {모멘텀} |`
    """
    if overview.revenue_table:
        # 비중 큰 순 top-3
        top3 = sorted(overview.revenue_table, key=lambda r: r.ratio_pct or 0, reverse=True)[:3]
        rev_struct = " / ".join(
            f"{r.segment} {r.ratio_pct:.0f}%" if r.ratio_pct else r.segment for r in top3
        )
        items = " · ".join(r.item for r in top3 if r.item)
    else:
        rev_struct = "공백 (추출 실패)"
        items = "공백"

    return (
        f"| {overview.corp_name} ({overview.ticker}) "
        f"| {rev_struct} | {items} | (판로 — section_text 검토 필요) | (Q1 모멘텀 — IR 보도자료 참조) |"
    )
