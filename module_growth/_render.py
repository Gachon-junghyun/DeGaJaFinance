"""ScreenResult → 마크다운 랭킹 표. 결론은 안 낸다(P4) — 관측·신선도·커버리지만."""
from __future__ import annotations

from ._metrics import GrowthMetrics
from ._screen import ScreenResult


def _pct(v) -> str:
    return "—" if v is None else f"{v * 100:+.1f}%"


def _num(v) -> str:
    return "—" if v is None else f"{v:.3f}"


def render_markdown(res: ScreenResult, *, top: int = 20) -> str:
    L: list[str] = []
    L.append(f"# 이익 성장 스크리너 — {res.market.upper()}")
    L.append("")
    cov = f"{res.n_scored}/{res.n_requested}"
    L.append(f"- **asof**: {res.asof or '—'}  ·  최신 관측분기: {res.latest_quarter_seen or '—'}")
    L.append(f"- **커버리지**: 점수산출 {cov} 종목  (fetch성공 {res.n_fetched})")
    L.append(f"- **점수 = 대략 연 YoY %.** 실현 순이익 성장 1순위 → 없으면 매출·선행으로 강등. 등급 A≥30% B≥15% C≥5%.")
    for n in res.notes:
        L.append(f"- ⚠️ {n}")
    L.append("")
    L.append("| # | 티커 | 이름 | 등급 | 점수 | 점수근거 | 순이익YoY | 매출YoY | 가속 | 선행EPS | 밸류 | 메모 |")
    L.append("|--:|---|---|:--:|--:|---|--:|--:|--:|--:|---|---|")

    ranked = [m for m in res.rows if m.score is not None][:top]
    for i, m in enumerate(ranked, 1):
        flags = "; ".join(m.flags) if m.flags else ""
        L.append(
            f"| {i} | {m.ticker} | {m.name[:16]} | {m.grade} | {_pct(m.score)} "
            f"| {m.score_source} | {_pct(m.earnings_yoy)} | {_pct(m.revenue_yoy)} "
            f"| {_pct(m.earnings_accel)} | {_pct(m.fwd_eps_growth)} | {m.value_tag or '—'} | {flags} |"
        )

    unscored = [m for m in res.rows if m.score is None]
    if unscored:
        L.append("")
        L.append(f"**관측 불가 {len(unscored)}종목** (재무 없음/429): "
                 + ", ".join(m.ticker for m in unscored[:30])
                 + (" …" if len(unscored) > 30 else ""))
    L.append("")
    L.append("> 판단(매수/매도)은 이 표가 내지 않는다 — 관측값·출처·신선도만(P4). "
             "라이브 진입은 촉매·흐름·차트와 교차 확인.")
    return "\n".join(L)


def render_detail(m: GrowthMetrics) -> str:
    """단일 종목 상세(디버그·검증용)."""
    L = [f"## {m.ticker} {m.name}  [{m.grade}]  {m.sector}"]
    L.append(f"- score={_num(m.score)} (src: {m.score_source})  {m.value_tag}")
    L.append(f"- 순이익 YoY={_pct(m.earnings_yoy)} · TTM={_pct(m.earnings_ttm_yoy)} · 가속={_pct(m.earnings_accel)}")
    L.append(f"- 매출 YoY={_pct(m.revenue_yoy)} · TTM={_pct(m.revenue_ttm_yoy)}")
    L.append(f"- EPS YoY={_pct(m.eps_yoy)} · 선행EPS성장={_pct(m.fwd_eps_growth)} · PEG={_num(m.peg)}")
    L.append(f"- 분기수={m.n_quarters} · 흑자분기={m.profitable_quarters} · 최신분기={m.latest_quarter}")
    if m.flags:
        L.append(f"- flags: {'; '.join(m.flags)}")
    return "\n".join(L)
