"""CLI 진입점.

사용:
    python -m module_valuation 267260
    python -m module_valuation 267260 --peers 298040,010120
    python -m module_valuation 267260 --json
    python -m module_valuation 267260 --peers 298040,010120 --out llm_outputs/valuation_267260.md
"""
from __future__ import annotations

import argparse
import io
import json
import sys
from pathlib import Path

from . import (
    add_peer_avg,
    build_peer_table,
    fetch_naver_snapshot,
    render_markdown,
    to_dict,
)


def _utf8_stdout() -> None:
    if sys.stdout.encoding and sys.stdout.encoding.lower().startswith("utf"):
        return
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


def main() -> None:
    p = argparse.ArgumentParser(prog="module_valuation")
    p.add_argument("code", help="대상 종목 6자리 코드 (예: 267260)")
    p.add_argument(
        "--peers",
        default="",
        help="comma-separated peer 코드 (예: 298040,010120)",
    )
    p.add_argument("--json", action="store_true", help="JSON 으로 단일 종목 dump (peer 무시)")
    p.add_argument("--out", default="", help="markdown 결과를 저장할 경로 (없으면 stdout)")
    args = p.parse_args()
    # '.KS'/'.KQ' 등 거래소 접미사 자동 strip — flow/차트는 티커에 접미사를 붙이지만
    # DART/밸류 계열은 6자리 코드만 받는다(포맷 불일치로 조용히 크래시하던 지점).
    if "." in args.code:
        _stem = args.code.partition(".")[0]
        if _stem.isdigit() and len(_stem) == 6:
            args.code = _stem
    _utf8_stdout()

    if args.json:
        snap = fetch_naver_snapshot(args.code)
        print(json.dumps(to_dict(snap), ensure_ascii=False, indent=2))
        return

    peers = [c.strip() for c in args.peers.split(",") if c.strip()]

    df = build_peer_table(args.code, peers)
    df = add_peer_avg(df)

    snap = fetch_naver_snapshot(args.code)

    header = (
        f"# {snap.name} ({snap.code}) — Valuation Snapshot\n\n"
        f"- 현재가: {snap.price:,.0f}원 / 시총: {snap.market_cap_eok:,.0f}억원\n"
        f"- 컨센 목표주가: {snap.target_price:,.0f}원 (상승여력 {snap.upside_pct():+.2f}%)\n"
        f"- 12M Fwd PER: {snap.per_fwd}배 / EPS: {snap.eps_fwd:,.0f}원\n"
        f"- TTM PER: {snap.per_ttm}배 / PBR: {snap.pbr}배\n"
        f"- 외국인 소진율: {snap.foreign_pct}% / 동일업종 PER: {snap.industry_per}배\n\n"
    )
    header += "## Peer Multiple Comparison\n\n"

    body = render_markdown(df, target_code=args.code)
    out = header + body + "\n"

    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(out, encoding="utf-8")
        print(f"saved: {args.out}")
    else:
        print(out)


if __name__ == "__main__":
    main()
