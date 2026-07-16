"""CLI: python -m module_business_us {ticker} [--full] [--form 10-K|10-Q] [--out FILE] [--json]

사용:
    python -m module_business_us NVDA
    python -m module_business_us NVDA --full
    python -m module_business_us NVDA --form 10-Q
    python -m module_business_us NVDA --full --out llm_outputs/2026-05-27/nvda_business.md
    python -m module_business_us NVDA --json

기본은 최신 10-K + Risk Factors bullet 요약만 (본문은 derived 단락).
`--full` 시 Item 1 / 1A / 7 전체 본문 (각 최대 50K자).

SEC EDGAR Fair Access: User-Agent 에 이메일 식별자 필수.
환경변수 SEC_USER_AGENT 로 override (default: mvp Research fivepeople201@gmail.com).
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import asdict
from pathlib import Path


def _utf8_stdout() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass


def _maybe_load_dotenv() -> None:
    """research_Mvp/.env 가 있으면 로드 (없어도 무방).

    module_disclosure 와 동일 패턴 — dotenv 없으면 silently skip.
    """
    try:
        from dotenv import load_dotenv
    except ImportError:
        return
    # 작업 디렉토리 또는 research_Mvp 기준.
    here = Path(__file__).resolve().parent.parent
    for p in (Path.cwd() / ".env", here / ".env"):
        if p.exists():
            load_dotenv(p, override=False)
            break


def main() -> int:
    _utf8_stdout()
    _maybe_load_dotenv()

    p = argparse.ArgumentParser(prog="module_business_us")
    p.add_argument("ticker", help="US 티커 (예: NVDA, AAPL)")
    p.add_argument("--full", action="store_true", help="Risk Factors / Business / MD&A 전체 본문 출력 (각 50K자 cap)")
    p.add_argument(
        "--form",
        choices=["10-K", "10-Q"],
        default="10-K",
        help="공시 폼 (기본 10-K)",
    )
    p.add_argument("--out", default="", help="markdown 저장 경로 (없으면 stdout)")
    p.add_argument("--json", action="store_true", help="JSON dump (ExtractResult)")
    args = p.parse_args()

    # edgartools import & 실행.
    try:
        from . import extract, render_markdown
        from ._edgar import EdgartoolsMissingError
    except EdgartoolsMissingError as e:
        print(f"[module_business_us] {e}", file=sys.stderr)
        return 2

    try:
        result = extract(args.ticker, form=args.form, full=args.full)
    except EdgartoolsMissingError as e:
        print(f"[module_business_us] {e}", file=sys.stderr)
        return 2
    except Exception as e:
        print(f"[module_business_us] 추출 실패: {e}", file=sys.stderr)
        return 1

    if result is None:
        print(
            f"[module_business_us] ticker '{args.ticker}' 에서 {args.form} 본문을 찾을 수 없습니다.",
            file=sys.stderr,
        )
        return 1

    if args.json:
        out = asdict(result)
        text = json.dumps(out, ensure_ascii=False, indent=2)
        if args.out:
            Path(args.out).parent.mkdir(parents=True, exist_ok=True)
            Path(args.out).write_text(text, encoding="utf-8")
            print(f"[module_business_us] wrote {args.out}", file=sys.stderr)
        else:
            sys.stdout.write(text + "\n")
        return 0

    md = render_markdown(result, full=args.full)
    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(md, encoding="utf-8")
        print(
            f"[module_business_us] wrote {out_path} ({len(md):,} chars)",
            file=sys.stderr,
        )
    else:
        sys.stdout.write(md)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
