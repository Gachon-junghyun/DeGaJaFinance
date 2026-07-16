"""CLI: python -m module_business {ticker} [--include-ir] [--include-dart] [--out FILE]

기본은 corp_embeddings.section_text 에서 매출 표 + 사업 개요 발췌만.
--include-ir 추가 시 news_alert.db 에서 1Q IR 보도자료 본문 발췌 (~60일).
--include-dart 추가 시 DART 사업보고서 본문 fetch (DART_API_KEY 필요).
"""
from __future__ import annotations

import argparse
import io
import sys
from pathlib import Path

from . import extract, render_markdown


def main() -> int:
    parser = argparse.ArgumentParser(prog="module_business")
    parser.add_argument("ticker", help="6자리 종목코드 (예: 068270)")
    parser.add_argument("--include-ir", action="store_true", help="1Q IR 보도자료 발췌")
    parser.add_argument("--no-ir", action="store_true", help="IR 발췌 생략 (default = --include-ir)")
    parser.add_argument("--include-dart", action="store_true", help="DART 사업보고서 본문 fetch (DART_API_KEY 필요)")
    parser.add_argument("--ir-days", type=int, default=60, help="IR 보도자료 검색 기간 (일). 기본 60.")
    parser.add_argument("--out", type=str, help="출력 파일 경로. 미지정 시 stdout.")
    args = parser.parse_args()
    # '.KS'/'.KQ' 등 거래소 접미사 자동 strip — 6자리 코드일 때만.
    if "." in args.ticker:
        _stem = args.ticker.partition(".")[0]
        if _stem.isdigit() and len(_stem) == 6:
            args.ticker = _stem

    include_ir = args.include_ir or not args.no_ir
    if args.no_ir:
        include_ir = False

    extracted = extract(
        args.ticker,
        include_dart=args.include_dart,
        include_ir=include_ir,
        ir_days=args.ir_days,
    )
    md = render_markdown(extracted)

    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(md, encoding="utf-8")
        print(f"[module_business] wrote {out_path}", file=sys.stderr)
    else:
        # Windows console UTF-8
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8")
        sys.stdout.write(md)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
