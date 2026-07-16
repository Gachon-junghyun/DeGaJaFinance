"""markdown 출력 렌더러."""
from __future__ import annotations

from ._edgar import ExtractResult


def _section_or_note(body: str, note: str = "") -> str:
    if body.strip():
        return body.strip()
    return f"_{note or '본문 추출 실패.'}_"


def render_markdown(result: ExtractResult, *, full: bool = False) -> str:
    """ExtractResult -> markdown 문서."""
    lines: list[str] = []
    title = f"# {result.ticker} 사업 모델"
    if result.company_name and result.company_name.upper() != result.ticker:
        title += f" ({result.company_name})"
    lines.append(title)
    lines.append("")

    # metadata 줄.
    src_bits = [f"{result.form} filed {result.filing_date}"]
    if result.accession_no:
        src_bits.append(f"accession {result.accession_no}")
    if result.period_of_report:
        src_bits.append(f"period {result.period_of_report}")
    lines.append(f"출처: {' | '.join(src_bits)}")
    if result.filing_url:
        lines.append(f"링크: {result.filing_url}")
    if result.homepage_url and result.homepage_url != result.filing_url:
        lines.append(f"인덱스: {result.homepage_url}")
    lines.append("")

    # === Item 1: Business ===
    if result.form == "10-K":
        lines.append("## Item 1 — Business (사업 설명)")
        lines.append("")
        lines.append("### 주요 제품·시장")
        lines.append("")
        lines.append(_section_or_note(result.business_primary, "Item 1 본문 추출 실패."))
        lines.append("")
        if result.business_customer:
            lines.append("### 주요 고객·경쟁")
            lines.append("")
            lines.append(result.business_customer)
            lines.append("")
        if full and result.business:
            lines.append("### --full: Item 1 전체 본문")
            lines.append("")
            lines.append(result.business)
            lines.append("")
    else:
        # 10-Q : Item 1 본문 없음.
        lines.append("## Item 1 — Business")
        lines.append("")
        lines.append("_10-Q 에는 Item 1 (Business) 가 포함되지 않습니다. `--form 10-K` 사용 권장._")
        lines.append("")

    # === Item 1A: Risk Factors ===
    lines.append("## Item 1A — Risk Factors")
    lines.append("")
    lines.append("### 요약 (편집자 추가)")
    lines.append("")
    if result.risk_summary_bullets:
        for b in result.risk_summary_bullets:
            lines.append(f"- {b}")
    else:
        lines.append("_Risk Factors bullet 추출 실패 (본문 비표준 포맷)._")
    lines.append("")
    if full:
        lines.append("### 전체 본문 (--full)")
        lines.append("")
        lines.append(_section_or_note(result.risk_factors, "Risk Factors 본문 추출 실패."))
        lines.append("")
    else:
        lines.append("_`--full` 옵션으로 Risk Factors 전체 본문을 표시할 수 있습니다._")
        lines.append("")

    # === Item 7: MD&A ===
    mdna_title = (
        "## Item 7 — Management's Discussion & Analysis"
        if result.form == "10-K"
        else "## Part I, Item 2 — Management's Discussion & Analysis"
    )
    lines.append(mdna_title)
    lines.append("")
    lines.append("### 매출 성장 동인 (자동 추출)")
    lines.append("")
    lines.append(_section_or_note(result.mdna_revenue, "MD&A 매출 단락 추출 실패."))
    lines.append("")
    if result.mdna_outlook:
        lines.append("### 향후 전망 / 가이던스 (자동 추출)")
        lines.append("")
        lines.append(result.mdna_outlook)
        lines.append("")
    if full and result.mdna:
        lines.append("### --full: MD&A 전체 본문")
        lines.append("")
        lines.append(result.mdna)
        lines.append("")

    # === footer ===
    lines.append("## 데이터 source")
    lines.append("")
    src_note = "edgartools (MIT) -> SEC EDGAR " + result.form + " filing"
    if result.fallback_used:
        src_note += " (BeautifulSoup fallback 동원)"
    lines.append(src_note)
    if result.notes:
        lines.append("")
        lines.append("### 가정 & 제약")
        for n in result.notes:
            lines.append(f"- {n}")
    lines.append("")

    return "\n".join(lines)
