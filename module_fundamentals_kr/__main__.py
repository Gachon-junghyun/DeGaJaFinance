# -*- coding: utf-8 -*-
"""CLI 진입점.

사용:
    python -m module_fundamentals_kr 000720                    # 현대건설 재무 + 수익의 질
    python -m module_fundamentals_kr 현대건설 --period half
    python -m module_fundamentals_kr 047040 --year 2025 --json
    python -m module_fundamentals_kr 000720 --fs-div OFS       # 별도재무제표
    python -m module_fundamentals_kr 000720 --out out/hdec_fin.md
"""
from __future__ import annotations

import argparse
import io
import json
import os
import sys
from dataclasses import asdict
from pathlib import Path

from ._dart_fin import REPRT_CODES, fetch_by_stock
from ._quality import compute
from ._renderer import render_markdown


def _utf8_stdout() -> None:
    for stream_name in ("stdout", "stderr"):
        s = getattr(sys, stream_name, None)
        if s is None:
            continue
        if hasattr(s, "reconfigure"):
            try:
                s.reconfigure(encoding="utf-8")
                continue
            except Exception:
                pass
        if getattr(s, "encoding", None) and s.encoding.lower().startswith("utf"):
            continue
        try:
            setattr(sys, stream_name, io.TextIOWrapper(s.buffer, encoding="utf-8"))
        except Exception:
            pass


def _maybe_load_dotenv() -> None:
    """프로젝트 루트의 .env 를 단순 파싱해 환경변수에 주입 (module_disclosure 패턴)."""
    here = Path(__file__).resolve().parent
    for p in [here / ".env", here.parent / ".env", here.parent.parent / ".env"]:
        if not p.exists():
            continue
        try:
            for line in p.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                k, _, v = line.partition("=")
                k, v = k.strip(), v.strip().strip('"').strip("'")
                if k and v and k not in os.environ:
                    os.environ[k] = v
        except Exception:
            pass
        break


def main() -> int:
    _utf8_stdout()
    _maybe_load_dotenv()

    p = argparse.ArgumentParser(prog="module_fundamentals_kr")
    p.add_argument("stock", help="종목코드 6자리 또는 기업명 (예: 000720, 현대건설)")
    p.add_argument("--year", help="사업연도 (기본: 올해부터 뒤로 탐색)")
    p.add_argument(
        "--period",
        default="annual",
        choices=sorted(REPRT_CODES),
        help="보고서 종류 (기본 annual=사업보고서)",
    )
    p.add_argument("--fs-div", default="CFS", choices=["CFS", "OFS"], help="연결/별도 (기본 CFS, 비면 OFS 폴백)")
    p.add_argument("--json", action="store_true", help="지표 JSON dump")
    p.add_argument("--out", help="마크다운 저장 경로")
    args = p.parse_args()

    if not os.environ.get("DART_API_KEY", "").strip():
        print("DART_API_KEY 미설정 — .env 를 확인하라", file=sys.stderr)
        return 2

    fin = fetch_by_stock(
        args.stock, year=args.year, period=args.period, fs_div=args.fs_div
    )
    if fin is None:
        print(
            f"재무제표를 찾지 못했다: {args.stock} "
            "(corp_code 해석 실패이거나 해당 연도 공시 없음 — --year 로 지정해보라)",
            file=sys.stderr,
        )
        return 1

    metrics = compute(fin)

    if args.json:
        payload = {
            "corp_code": fin.corp_code,
            "corp_name": fin.corp_name,
            "bsns_year": fin.bsns_year,
            "reprt_code": fin.reprt_code,
            "fs_div": fin.fs_div,
            "accounts": {k: asdict(a) for k, a in fin.accounts.items()},
            "metrics": {
                k: getattr(metrics, k)
                for k in (
                    "ocf_to_op", "accrual_ratio", "unbilled_to_revenue",
                    "unbilled_prev_ratio", "unbilled_growth", "revenue_growth",
                    "unbilled_gap", "overbilled_to_revenue", "net_contract_position",
                    "receivables_to_revenue", "receivables_growth",
                )
            },
            "flags": [asdict(f) for f in metrics.flags],
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0

    md = render_markdown(metrics)
    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(md, encoding="utf-8")
        print(f"저장: {out}")
    else:
        print(md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
