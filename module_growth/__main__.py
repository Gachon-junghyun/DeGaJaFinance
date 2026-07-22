"""CLI 진입점 — 이익 성장 스크리너.

    python -m module_growth --market us --limit 50 --top 20
    python -m module_growth --market us --sector Semiconductors --limit 40
    python -m module_growth --ticker NVDA AMD AVGO          # 유니버스 대신 임의 티커
    python -m module_growth --market us --limit 30 --json
    python -m module_growth --market kr --limit 40          # 선행 성장만(실현 히스토리 없음)
"""
from __future__ import annotations

import argparse
import io
import json
import sys
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path

from ._metrics import compute_metrics
from ._render import render_detail, render_markdown
from ._screen import ScreenResult, screen


def _utf8_stdout() -> None:
    for name in ("stdout", "stderr"):
        s = getattr(sys, name, None)
        if s is None:
            continue
        if hasattr(s, "reconfigure"):
            try:
                s.reconfigure(encoding="utf-8")
                continue
            except Exception:
                pass
        try:
            setattr(sys, name, io.TextIOWrapper(s.buffer, encoding="utf-8"))
        except Exception:
            pass


def _asof() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%MZ")


def _screen_tickers(tickers: list[str], market: str, retries: int, backoff: float,
                    sleep: float) -> ScreenResult:
    """임의 티커 리스트를 유니버스 없이 직접 스크린(디버그·즉석 비교용)."""
    from ._screen import _fetch_kr, _fetch_us

    res = ScreenResult(market=market, n_requested=len(tickers), asof=_asof())
    for i, t in enumerate(tickers, 1):
        sys.stderr.write(f"[{i}/{len(tickers)}] {t} ...\n")
        fetched = _fetch_us(t, retries, backoff) if market == "us" \
            else _fetch_kr(t, retries, backoff)
        if fetched is None:
            from ._metrics import GrowthMetrics
            m = GrowthMetrics(ticker=t)
            m.flags.append("fetch 실패(빈 응답/429)")
            res.rows.append(m)
            continue
        rev, ni, eps, te, fe, peg = fetched
        m = compute_metrics(t, revenue=rev, net_income=ni, diluted_eps=eps,
                            trailing_eps=te, forward_eps=fe, peg=peg)
        res.rows.append(m)
        res.n_fetched += 1
        if m.score is not None:
            res.n_scored += 1
        if m.latest_quarter:
            res.latest_quarter_seen = max(res.latest_quarter_seen or "", m.latest_quarter)
    res.rows.sort(key=lambda x: (x.score is not None, x.score or -1e18), reverse=True)
    return res


def main() -> None:
    _utf8_stdout()
    p = argparse.ArgumentParser(prog="module_growth", description="이익 성장 기업 스크리너(실험 모델)")
    p.add_argument("--market", choices=["us", "kr"], default="us")
    p.add_argument("--ticker", nargs="+", help="유니버스 대신 임의 티커 직접(예: NVDA AMD)")
    p.add_argument("--limit", type=int, default=30, help="유니버스 상위 N종목(시총순)")
    p.add_argument("--sector", default=None, help="섹터 부분일치 필터(예: Semiconductors)")
    p.add_argument("--min-cap", type=float, default=None, help="최소 시총(us=USD, kr=KRW)")
    p.add_argument("--top", type=int, default=20, help="표에 출력할 상위 N")
    p.add_argument("--sleep", type=float, default=0.4, help="종목간 대기(초, 429 완화)")
    p.add_argument("--retries", type=int, default=2, help="빈응답/429 재시도 횟수")
    p.add_argument("--detail", action="store_true", help="상위 종목 상세 블록도 출력")
    p.add_argument("--json", action="store_true", help="JSON 덤프")
    p.add_argument("--out", default="", help="마크다운 저장 경로(없으면 stdout)")
    args = p.parse_args()

    if args.ticker:
        res = _screen_tickers([t.upper() for t in args.ticker], args.market,
                              args.retries, 1.5, args.sleep)
    else:
        res = screen(
            market=args.market, limit=args.limit, sector=args.sector,
            min_market_cap=args.min_cap, sleep=args.sleep, retries=args.retries,
            asof=_asof(),
        )

    if args.json:
        payload = {
            "market": res.market, "asof": res.asof,
            "n_requested": res.n_requested, "n_fetched": res.n_fetched,
            "n_scored": res.n_scored, "latest_quarter": res.latest_quarter_seen,
            "notes": res.notes,
            "rows": [asdict(m) for m in res.rows],
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2, default=str))
        return

    md = render_markdown(res, top=args.top)
    if args.detail:
        md += "\n\n---\n\n" + "\n\n".join(
            render_detail(m) for m in res.rows if m.score is not None
        )
    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(md, encoding="utf-8")
        print(f"saved: {args.out}")
    else:
        print(md)


if __name__ == "__main__":
    main()
