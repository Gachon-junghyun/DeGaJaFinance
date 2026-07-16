"""CLI 진입점.

사용:
    python -m module_disclosure_us AAPL
    python -m module_disclosure_us AAPL --days 90
    python -m module_disclosure_us AAPL --days 90 --out llm_outputs/disclosure_aapl.md
    python -m module_disclosure_us AAPL --json

SEC EDGAR Fair Access: User-Agent에 이메일 식별자 필수.
환경변수 SEC_USER_AGENT로 override 가능 (default는 mvp Research 식별자).
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict
from pathlib import Path

from ._edgar_api import fetch_filings
from ._renderer import render_markdown


def _utf8_stdout() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass


def main() -> None:
    _utf8_stdout()
    p = argparse.ArgumentParser(prog="module_disclosure_us")
    p.add_argument("ticker", help="US 티커 (예: AAPL)")
    p.add_argument("--days", type=int, default=90, help="조회 기간 (기본 90일)")
    p.add_argument("--json", action="store_true", help="JSON raw rows dump")
    p.add_argument("--out", default="", help="markdown 결과 저장 경로 (없으면 stdout)")
    args = p.parse_args()

    rows, cik, name = fetch_filings(args.ticker, days=args.days)

    if args.json:
        out_rows = [asdict(r) for r in rows]
        print(json.dumps(out_rows, ensure_ascii=False, indent=2))
        return

    md = render_markdown(args.ticker.upper(), cik, rows, args.days, company_name=name)
    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(md, encoding="utf-8")
        print(f"saved: {args.out}")
    else:
        print(md)
    print(f"DONE: {len(rows)} filings", file=sys.stderr)


if __name__ == "__main__":
    main()
