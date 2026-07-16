"""CLI 진입점.

사용:
    python -m module_math_check llm_outputs/REPORT_삼성전자_005930_2026-05-01.md
    python -m module_math_check <path> --strict   # 실패 시 exit 1
"""
from __future__ import annotations

import argparse
import io
import sys
from pathlib import Path

from . import check_all


def _utf8_stdout() -> None:
    if sys.stdout.encoding and sys.stdout.encoding.lower().startswith("utf"):
        return
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


def main() -> None:
    p = argparse.ArgumentParser(prog="module_math_check")
    p.add_argument("path", help="검증할 리포트 markdown 파일")
    p.add_argument("--strict", action="store_true",
                   help="실패 1건이라도 있으면 exit code 1 (CI/hook 용도)")
    args = p.parse_args()
    _utf8_stdout()

    passed, failed = check_all(Path(args.path))
    print(f"\n=== Math Check: {args.path} ===\n")

    if passed:
        print(f"✓ {len(passed)} check(s) passed")
        for c in passed:
            print(f"  ✓ {c.name} @ {c.location}: {c.actual:,.2f} (산식 일치)")
        print()

    if failed:
        print(f"✗ {len(failed)} FAILURE(S):")
        for c in failed:
            print(f"  ✗ {c.name} @ {c.location}")
            print(f"      expected: {c.expected:,.4f}")
            print(f"      actual  : {c.actual:,.4f}")
            print(f"      delta%  : {c.delta_pct:+.3f}%")
            if c.detail:
                print(f"      detail  : {c.detail}")
        print()

    if not failed:
        print("ALL MATH CHECKS PASSED.")
        return
    print(f"{len(failed)} check(s) FAILED — fix before publishing.")
    if args.strict:
        sys.exit(1)


if __name__ == "__main__":
    main()
