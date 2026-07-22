"""FundamentalsSnapshot → markdown 렌더링."""
from __future__ import annotations

from datetime import date
from typing import Optional

from ._yfinance_fetch import FundamentalsSnapshot


def _fmt_money(v: Optional[float], digits: int = 2, suffix: str = "") -> str:
    if v is None:
        return "—"
    return f"{v:,.{digits}f}{suffix}"


def _fmt_market_cap(v: Optional[int]) -> str:
    if v is None:
        return "—"
    if v >= 1_000_000_000_000:
        return f"${v / 1_000_000_000_000:,.2f}T"
    if v >= 1_000_000_000:
        return f"${v / 1_000_000_000:,.0f}B"
    if v >= 1_000_000:
        return f"${v / 1_000_000:,.0f}M"
    return f"${v:,}"


def _fmt_price(v: Optional[float]) -> str:
    if v is None:
        return "—"
    return f"${v:,.2f}"


def _fmt_revenue_b(v: Optional[float]) -> str:
    if v is None:
        return "—"
    return f"{v / 1_000_000_000:,.2f}"


def _fmt_pct(v: Optional[float], digits: int = 2) -> str:
    if v is None:
        return "—"
    return f"{v:+.{digits}f}%"


def _fmt_ratio(v: Optional[float], digits: int = 2) -> str:
    if v is None:
        return "—"
    return f"{v:,.{digits}f}"


def _compute_yoy(rows: list[tuple[str, float]]) -> dict[str, Optional[float]]:
    """rows = [(date_str, value), ...] 최신순. 각 분기에 대해 4분기 전 대비 yoy% 산출."""
    by_date = {d: v for d, v in rows}
    sorted_desc = sorted(by_date.keys(), reverse=True)
    out: dict[str, Optional[float]] = {}
    for i, d in enumerate(sorted_desc):
        target = i + 4
        if target < len(sorted_desc):
            prior_d = sorted_desc[target]
            prior_v = by_date.get(prior_d)
            curr = by_date.get(d)
            if prior_v and curr and prior_v != 0:
                out[d] = (curr / prior_v - 1.0) * 100.0
                continue
        out[d] = None
    return out


def _recs_aggregate(recs: list[dict]) -> dict[str, int]:
    """가장 최근 period(0m) 또는 첫 row 기준 집계."""
    if not recs:
        return {}
    # period == '0m' 우선
    chosen = None
    for r in recs:
        if r.get("period") == "0m":
            chosen = r
            break
    if chosen is None:
        chosen = recs[0]
    out: dict[str, int] = {}
    for k in ("strongBuy", "buy", "hold", "sell", "strongSell"):
        v = chosen.get(k)
        if v is None:
            continue
        try:
            out[k] = int(v)
        except (TypeError, ValueError):
            pass
    return out


def _render_consensus(snap: FundamentalsSnapshot) -> str:
    lines: list[str] = ["## 애널리스트 컨센서스"]
    tm = snap.target_mean
    tl = snap.target_low
    th = snap.target_high
    tmd = snap.target_median
    if tm is not None or tl is not None or th is not None:
        parts = []
        if tl is not None:
            parts.append(f"${tl:,.2f} (low)")
        if tm is not None:
            parts.append(f"**${tm:,.2f} (mean)**")
        if th is not None:
            parts.append(f"${th:,.2f} (high)")
        line = "- 목표주가: " + " / ".join(parts)
        if tmd is not None:
            line += f" | median ${tmd:,.2f}"
        lines.append(line)
        if snap.price and tm:
            upside = (tm / snap.price - 1.0) * 100.0
            lines.append(f"- 현재가 대비 상승 여력: {upside:+.1f}% (mean 기준)")
    else:
        lines.append("- 목표주가: 데이터 없음")

    agg = _recs_aggregate(snap.recommendations)
    if agg:
        lines.append("- 추천 (최근 30일):")
        label_map = [
            ("strongBuy", "Strong Buy"),
            ("buy", "Buy"),
            ("hold", "Hold"),
            ("sell", "Sell"),
            ("strongSell", "Strong Sell"),
        ]
        for k, label in label_map:
            if k in agg:
                lines.append(f"  - {label}: {agg[k]}")
    else:
        lines.append("- 추천: 데이터 없음")
    lines.append("")
    return "\n".join(lines)


_PERIOD_KO = {"0q": "당분기", "+1q": "다음분기", "0y": "당해년", "+1y": "내년"}


def _render_estimate_momentum(snap: FundamentalsSnapshot) -> str:
    """추정치 모멘텀 — 밸류에이션의 '분모가 어디로 가고 있나'.

    ⚠ 이 표를 밸류에이션 표와 **반드시 같이** 읽어라. forward P/E 가 낮은데 추정치가
    가파르게 상향 중이면 '싸다'가 아니라 '분모가 정점을 향해 달리는 중'일 수 있다
    (handoff/RESEARCH.md 렌즈 L2 — peak-margin / low-multiple trap).
    """
    lines: list[str] = ["## 추정치 모멘텀 (컨센서스가 움직이는 방향)"]
    tr = {d.get("period"): d for d in (snap.eps_trend or [])}
    rv = {d.get("period"): d for d in (snap.eps_revisions or [])}
    if not tr and not rv:
        lines.append("- 데이터 없음")
        lines.append("")
        return "\n".join(lines)

    if tr:
        lines.append("")
        lines.append("| 기간 | 현재 | 7일전 | 30일전 | 60일전 | 90일전 | 90일 변화 |")
        lines.append("|---|---|---|---|---|---|---|")
        for p in ("0q", "+1q", "0y", "+1y"):
            d = tr.get(p)
            if not d:
                continue
            cur, d90 = d.get("current"), d.get("90daysAgo")
            chg = "—"
            if cur is not None and d90 not in (None, 0):
                chg = f"**{(cur / d90 - 1.0) * 100:+.1f}%**"
            lines.append(
                f"| {_PERIOD_KO.get(p, p)} | {_fmt_ratio(cur)} | {_fmt_ratio(d.get('7daysAgo'))} | "
                f"{_fmt_ratio(d.get('30daysAgo'))} | {_fmt_ratio(d.get('60daysAgo'))} | "
                f"{_fmt_ratio(d90)} | {chg} |"
            )

    if rv:
        lines.append("")
        lines.append("**리비전 브레드스 (상향 : 하향)**")
        for p in ("0q", "+1q", "0y", "+1y"):
            d = rv.get(p)
            if not d:
                continue
            u7, d7 = d.get("upLast7days"), d.get("downLast7Days")
            u30, d30 = d.get("upLast30days"), d.get("downLast30days")
            def _n(x):
                return "—" if x is None else f"{int(x)}"
            lines.append(
                f"- {_PERIOD_KO.get(p, p)}: 7일 {_n(u7)}↑ / {_n(d7)}↓ · 30일 {_n(u30)}↑ / {_n(d30)}↓"
            )

    lines.append("")
    lines.append(
        "> ⚠ 밸류에이션 표와 **같이** 읽어라. forward P/E 가 낮은데 추정치가 가파르게 상향 중이면 "
        "'싸다'가 아니라 **분모가 정점을 향해 달리는 중**일 수 있다 (peak-margin / low-multiple trap). "
        "추정치 방향은 컨센서스의 **모멘텀**이지 사실이 아니다 — 사이클이 꺾이면 가격보다 먼저 꺾인다."
    )
    lines.append("")
    return "\n".join(lines)


def _render_qrev_yfinance(snap: FundamentalsSnapshot) -> str:
    lines: list[str] = [f"## 분기 매출 (yfinance {len(snap.quarterly_revenue)}분기)"]
    if not snap.quarterly_revenue:
        lines.append("_데이터 없음._\n")
        return "\n".join(lines)
    yoy = _compute_yoy(snap.quarterly_revenue)
    lines.append("| 분기 (end) | 매출 ($B) | yoy |")
    lines.append("|---|---|---|")
    for d, v in snap.quarterly_revenue:
        lines.append(f"| {d} | {_fmt_revenue_b(v)} | {_fmt_pct(yoy.get(d))} |")
    lines.append("")
    return "\n".join(lines)


def _fuzzy_align(
    yf_rows: list[tuple[str, float]],
    xbrl_rows: list[tuple[str, float]],
    window_days: int = 7,
) -> list[tuple[str, Optional[float], Optional[float]]]:
    """yfinance/XBRL 분기 매출을 ±window_days 내 fuzzy 매칭.

    yfinance 는 보통 calendar 월말 (예: 2026-04-30),
    XBRL 은 실제 fiscal 종료일 (예: 2026-04-26) 이라 며칠 어긋난다.
    반환: [(label_date, yf_val, xbrl_val), ...] 최신순.
    label_date 는 yf 가 있으면 yf, 없으면 xbrl 의 date.
    """
    from datetime import datetime

    def _parse(s: str):
        try:
            return datetime.strptime(s, "%Y-%m-%d").date()
        except Exception:
            return None

    yf_parsed = [(d, _parse(d), v) for d, v in yf_rows]
    xb_parsed = [(d, _parse(d), v) for d, v in xbrl_rows]
    xb_used: set[str] = set()
    out: list[tuple[str, Optional[float], Optional[float]]] = []
    for d, pd, v in yf_parsed:
        if pd is None:
            out.append((d, v, None))
            continue
        match = None
        match_diff = window_days + 1
        for xd, xpd, xv in xb_parsed:
            if xd in xb_used or xpd is None:
                continue
            diff = abs((pd - xpd).days)
            if diff <= window_days and diff < match_diff:
                match = (xd, xv)
                match_diff = diff
        if match is not None:
            xb_used.add(match[0])
            out.append((d, v, match[1]))
        else:
            out.append((d, v, None))
    # XBRL only (매칭 안된 것)
    for xd, xpd, xv in xb_parsed:
        if xd in xb_used:
            continue
        out.append((xd, None, xv))
    # 최신순
    out.sort(key=lambda x: x[0], reverse=True)
    return out[:8]


def _render_qrev_xbrl(snap: FundamentalsSnapshot) -> str:
    lines: list[str] = ["## 분기 매출 — SEC XBRL 교차 검증"]
    if not snap.quarterly_revenue_xbrl:
        lines.append("_XBRL 데이터 없음 또는 skip._\n")
        return "\n".join(lines)

    aligned = _fuzzy_align(snap.quarterly_revenue, snap.quarterly_revenue_xbrl)
    lines.append("| 분기 (end, yfinance 기준) | yfinance ($B) | XBRL ($B) | 차이 |")
    lines.append("|---|---|---|---|")
    for d, yv, xv in aligned:
        if yv is not None and xv is not None and xv != 0:
            diff = (yv / xv - 1.0) * 100.0
            mark = " ⚠️" if abs(diff) >= 5.0 else ""
            diff_str = f"{diff:+.1f}%{mark}"
        elif yv is None and xv is not None:
            diff_str = "(yf 없음)"
        elif yv is not None and xv is None:
            diff_str = "(xbrl 없음 — Q4 가능성)"
        else:
            diff_str = "—"
        lines.append(
            f"| {d} | {_fmt_revenue_b(yv)} | {_fmt_revenue_b(xv)} | {diff_str} |"
        )
    lines.append("")
    return "\n".join(lines)


def _render_business_summary(snap: FundamentalsSnapshot, max_len: int = 500) -> str:
    if not snap.business_summary:
        return "## 사업 요약\n_데이터 없음._\n"
    text = " ".join(snap.business_summary.split())
    if len(text) > max_len:
        text = text[:max_len].rsplit(" ", 1)[0] + " ..."
    return f"## 사업 요약 (yfinance longBusinessSummary, ~{max_len}자)\n{text}\n"


def render_markdown(
    snap: FundamentalsSnapshot,
    xbrl_included: bool = True,
    today: Optional[str] = None,
) -> str:
    if today is None:
        today = date.today().isoformat()

    sector_line = " / ".join(x for x in (snap.sector, snap.industry) if x) or "—"
    name = snap.company_name or "—"

    head = f"# {snap.ticker} 펀더멘털 ({name})\n업데이트: {today} | Sector: {sector_line}\n\n"

    # 가격 & 시총
    price_str = _fmt_price(snap.price)
    hi = _fmt_price(snap.fifty_two_week_high)
    lo = _fmt_price(snap.fifty_two_week_low)
    div = "—"
    if snap.dividend_yield is not None:
        # yfinance 1.3.x 의 dividendYield 는 이미 percent 단위 (예: 0.02 = 0.02%, 2.6 = 2.6%).
        div = f"{snap.dividend_yield:.2f}%"
    beta = _fmt_ratio(snap.beta)

    price_block = (
        "## 가격 & 시총\n"
        f"- 주가: {price_str} (52w high {hi} / low {lo})\n"
        f"- 시가총액: {_fmt_market_cap(snap.market_cap)}\n"
        f"- Beta: {beta}\n"
        f"- Dividend yield: {div}\n\n"
    )

    # 밸류에이션
    val_block = (
        "## 밸류에이션\n"
        "| 지표 | 값 |\n"
        "|---|---|\n"
        f"| Trailing P/E | {_fmt_ratio(snap.trailing_pe)} |\n"
        f"| Forward P/E | {_fmt_ratio(snap.forward_pe)} |\n"
        f"| PEG | {_fmt_ratio(snap.peg_ratio)} |\n"
        f"| Price/Sales | {_fmt_ratio(snap.price_to_sales)} |\n"
        f"| Price/Book | {_fmt_ratio(snap.price_to_book)} |\n"
        f"| Trailing EPS | {_fmt_price(snap.trailing_eps)} |\n"
        f"| Forward EPS | {_fmt_price(snap.forward_eps)} |\n\n"
    )

    consensus_block = _render_consensus(snap) + "\n"
    est_mom_block = _render_estimate_momentum(snap) + "\n"
    qrev_yf_block = _render_qrev_yfinance(snap) + "\n"
    qrev_xbrl_block = _render_qrev_xbrl(snap) + "\n" if xbrl_included else ""

    next_e = snap.next_earnings_date or "—"
    event_block = "## 다음 이벤트\n" f"- 다음 실적 발표: {next_e}\n\n"

    biz_block = _render_business_summary(snap) + "\n"

    src = "## 데이터 source\n"
    src += "- yfinance (Yahoo Finance) — Ticker.info / analyst_price_targets / recommendations / quarterly_income_stmt / calendar\n"
    if xbrl_included:
        src += "- SEC XBRL CompanyFacts — data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json (us-gaap:Revenues, RevenueFromContractWithCustomerExcludingAssessedTax)\n"

    return (
        head
        + price_block
        + val_block
        + consensus_block
        + est_mom_block
        + qrev_yf_block
        + qrev_xbrl_block
        + event_block
        + biz_block
        + src
    )
