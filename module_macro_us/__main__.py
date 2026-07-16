"""CLI 진입점.

사용:
    python -m module_macro_us
    python -m module_macro_us --series us_10y,cpi,vix --days 365
    python -m module_macro_us --days 90 --out llm_outputs/2026-05-26/macro_us.md
    python -m module_macro_us --series us_10y --json

FRED_API_KEY 환경변수 필수 (.env 또는 셸).
의존성:
    requests (필수, mvp 공용)
    fredapi  (옵션, 없으면 REST 폴백 자동 사용)
"""
from __future__ import annotations

import argparse
import io
import json
import os
import sys
from dataclasses import asdict
from pathlib import Path

from ._fetch import MacroFetchError, fetch_series
from ._renderer import render_markdown
from ._series import resolve_keys


def _utf8_stdout() -> None:
    if sys.stdout.encoding and sys.stdout.encoding.lower().startswith("utf"):
        return
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            return
        except Exception:
            pass
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


def _maybe_load_dotenv() -> None:
    """프로젝트 루트의 .env 를 단순 파싱해서 환경변수에 주입.

    module_disclosure._maybe_load_dotenv 와 동일 패턴.
    """
    if os.environ.get("FRED_API_KEY"):
        return
    here = Path(__file__).resolve().parent
    candidates = [here / ".env", here.parent / ".env", here.parent.parent / ".env"]
    for p in candidates:
        if not p.exists():
            continue
        try:
            for line in p.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                k, _, v = line.partition("=")
                k = k.strip()
                v = v.strip().strip('"').strip("'")
                if k and v and k not in os.environ:
                    os.environ[k] = v
        except Exception:
            pass
        break


def main() -> int:
    _utf8_stdout()
    _maybe_load_dotenv()

    p = argparse.ArgumentParser(prog="module_macro_us")
    p.add_argument(
        "--series",
        default="",
        help="쉼표 구분 시리즈 키 (예: us_10y,cpi,vix). 미지정 시 12종 전체.",
    )
    p.add_argument(
        "--days",
        type=int,
        default=365,
        help="조회 기간 (기본 365일). 월별 시리즈는 yoy 계산 위해 내부적으로 더 끌어옴.",
    )
    p.add_argument("--json", action="store_true", help="JSON raw 시리즈 dump")
    p.add_argument("--out", default="", help="markdown 결과 저장 경로 (없으면 stdout)")
    args = p.parse_args()

    try:
        keys = resolve_keys(args.series)
    except SystemExit as e:
        print(f"[macro_us] {e}", file=sys.stderr)
        return 1

    try:
        rows = fetch_series(keys, days=args.days)
    except MacroFetchError as e:
        print(f"[macro_us] {e}", file=sys.stderr)
        return 1
    except Exception as e:  # noqa: BLE001
        print(f"[macro_us] unexpected: {type(e).__name__}: {e}", file=sys.stderr)
        return 1

    # 전체 시리즈가 모두 실패한 경우 (예: invalid API key)
    if rows and all(r.error is not None for r in rows):
        first_err = rows[0].error or "all series failed"
        print(
            f"[macro_us] 전체 시리즈 fetch 실패. 첫 에러: {first_err}",
            file=sys.stderr,
        )
        return 1

    if args.json:
        dump = []
        for r in rows:
            dump.append({
                "key": r.key,
                "spec": dict(r.spec),
                "error": r.error,
                "observations": [asdict(o) for o in r.observations],
            })
        print(json.dumps(dump, ensure_ascii=False, indent=2))
        return 0

    md = render_markdown(rows)
    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(md, encoding="utf-8")
        print(f"saved: {args.out}")
    else:
        print(md)
    n_ok = sum(1 for r in rows if r.error is None)
    print(f"DONE: {n_ok}/{len(rows)} series", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
