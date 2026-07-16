"""DisclosureRow 리스트를 markdown 표로 렌더링.

리포트 §6 (뉴스) / §7-A (밸류에이션) 사이에 끼우기 좋은 형식.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from ._categorizer import CATEGORIES, CATEGORY_LABELS
from ._dart_api import DisclosureRow


def _fmt_won(amount: Optional[int]) -> str:
    """원 단위 정수를 '8,500억' / '1.2조' 식으로 표기."""
    if amount is None:
        return "—"
    if amount >= 10**12:
        return f"{amount / 10**12:.2f}조"
    if amount >= 10**8:
        return f"{amount / 10**8:,.0f}억"
    return f"{amount:,}원"


def _fmt_jo(amount_won: Optional[int]) -> str:
    if amount_won is None:
        return "—"
    return f"{amount_won / 10**12:.2f}조"


@dataclass
class ContractSummary:
    count: int
    total_amount_won: int
    ytd_guidance_jo: Optional[float] = None

    @property
    def progress_pct(self) -> Optional[float]:
        if self.ytd_guidance_jo is None or self.ytd_guidance_jo <= 0:
            return None
        return self.total_amount_won / (self.ytd_guidance_jo * 10**12) * 100


def summarize_contracts(
    rows: list[DisclosureRow],
    ytd_guidance_jo: Optional[float] = None,
) -> ContractSummary:
    """수주(contract) 카테고리만 합산. 정정공시는 제외."""
    total = 0
    cnt = 0
    for r in rows:
        if r.category != "contract" or r.is_amend:
            continue
        amt = (r.detail or {}).get("contract_amount")
        if isinstance(amt, (int, float)) and amt > 0:
            total += int(amt)
            cnt += 1
    return ContractSummary(count=cnt, total_amount_won=total, ytd_guidance_jo=ytd_guidance_jo)


def _table_contract(rows: list[DisclosureRow]) -> str:
    if not rows:
        return "_해당 기간 수주 공시 없음._\n"
    header = "| 일자 | 계약상대방 | 계약금액 | 매출 대비 | 계약기간 | 비고 |\n"
    sep    = "|---|---|---|---|---|---|\n"
    lines = [header, sep]
    for r in rows:
        d = r.detail or {}
        amt = _fmt_won(d.get("contract_amount"))
        ratio = d.get("ratio_to_revenue")
        ratio_s = f"{ratio:.2f}%" if isinstance(ratio, (int, float)) else "—"
        party = (d.get("counterparty") or "—")[:30]
        period = (d.get("period") or "—")[:24]
        tag = "정정" if r.is_amend else ""
        lines.append(
            f"| {r.date_iso} | {party} | {amt} | {ratio_s} | {period} | {tag} [원문]({r.url}) |\n"
        )
    return "".join(lines)


def _table_treasury(rows: list[DisclosureRow]) -> str:
    if not rows:
        return "_해당 기간 자기주식 공시 없음._\n"
    header = "| 일자 | 보고서명 | 주식수 | 예상금액 | 방법 | 목적 | 원문 |\n"
    sep    = "|---|---|---|---|---|---|---|\n"
    lines = [header, sep]
    for r in rows:
        d = r.detail or {}
        shr = f"{d['shares']:,}" if isinstance(d.get("shares"), int) else "—"
        amt = _fmt_won(d.get("amount"))
        method = (d.get("method") or "—")[:20]
        purpose = (d.get("purpose") or "—")[:30]
        lines.append(
            f"| {r.date_iso} | {r.report_nm[:40]} | {shr} | {amt} | {method} | {purpose} | [보기]({r.url}) |\n"
        )
    return "".join(lines)


def _table_capital(rows: list[DisclosureRow]) -> str:
    if not rows:
        return "_해당 기간 자본변동 공시 없음._\n"
    header = "| 일자 | 보고서명 | 발행규모 | 발행주식수 | 사용목적 | 원문 |\n"
    sep    = "|---|---|---|---|---|---|\n"
    lines = [header, sep]
    for r in rows:
        d = r.detail or {}
        amt = _fmt_won(d.get("issue_amount"))
        shr = f"{d['shares']:,}" if isinstance(d.get("shares"), int) else "—"
        purpose = (d.get("purpose") or "—")[:40]
        lines.append(
            f"| {r.date_iso} | {r.report_nm[:40]} | {amt} | {shr} | {purpose} | [보기]({r.url}) |\n"
        )
    return "".join(lines)


def _table_simple(rows: list[DisclosureRow]) -> str:
    if not rows:
        return "_해당 기간 공시 없음._\n"
    header = "| 일자 | 보고서명 | 제출인 | 원문 |\n"
    sep    = "|---|---|---|---|\n"
    lines = [header, sep]
    for r in rows:
        lines.append(
            f"| {r.date_iso} | {r.report_nm[:60]} | {r.flr_nm[:20]} | [보기]({r.url}) |\n"
        )
    return "".join(lines)


def render_markdown(
    code: str,
    name: str,
    rows: list[DisclosureRow],
    contract_summary: Optional[ContractSummary] = None,
    *,
    days: Optional[int] = None,
    only_category: Optional[str] = None,
) -> str:
    """전체 markdown 리포트 생성."""
    out: list[str] = []
    out.append(f"# {name} ({code}) — DART 공시 스냅샷\n\n")

    period_str = f"최근 {days}일" if days else f"총 {len(rows)}건"
    out.append(f"- 조회 범위: {period_str}\n")
    out.append(f"- 총 공시: **{len(rows)}건** (정정 포함)\n")

    by_cat = {c: [r for r in rows if r.category == c] for c in CATEGORIES}
    cat_dist = " / ".join(f"{CATEGORY_LABELS[c].split('(')[0].strip()} {len(by_cat[c])}" for c in CATEGORIES)
    out.append(f"- 카테고리 분포: {cat_dist}\n\n")

    if contract_summary and contract_summary.count > 0:
        out.append("## 누적 수주 합계 (정정 제외)\n\n")
        out.append(f"- 합산 건수: {contract_summary.count}건\n")
        out.append(f"- 합산 금액: **{_fmt_jo(contract_summary.total_amount_won)}** ({_fmt_won(contract_summary.total_amount_won)})\n")
        if contract_summary.ytd_guidance_jo is not None:
            pct = contract_summary.progress_pct
            pct_s = f"{pct:.1f}%" if pct is not None else "—"
            out.append(
                f"- 2026 가이던스: {contract_summary.ytd_guidance_jo:.1f}조 → "
                f"**진척률 {pct_s}**\n"
            )
        out.append("\n")

    sections = [
        ("contract", _table_contract),
        ("treasury", _table_treasury),
        ("capital",  _table_capital),
        ("equity",   _table_simple),
        ("earnings", _table_simple),
        ("other",    _table_simple),
    ]

    for cat, fn in sections:
        if only_category and cat != only_category:
            continue
        items = by_cat.get(cat, [])
        out.append(f"## {CATEGORY_LABELS[cat]} — {len(items)}건\n\n")
        out.append(fn(items))
        out.append("\n")

    return "".join(out)
