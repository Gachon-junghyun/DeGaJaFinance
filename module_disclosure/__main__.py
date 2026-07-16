"""CLI 진입점.

사용:
    python -m module_disclosure 034020
    python -m module_disclosure 034020 --days 90
    python -m module_disclosure 034020 --days 90 --guidance 13.3
    python -m module_disclosure 034020 --category contract
    python -m module_disclosure 034020 --json
    python -m module_disclosure 034020 --out llm_outputs/disclosure_034020.md
    python -m module_disclosure 034020 --no-detail   # 본문 파싱 skip (빠름)

DART_API_KEY 환경변수 필수 (.env 또는 셸).
"""
from __future__ import annotations

import argparse
import io
import json
import os
import sys
import time
from pathlib import Path

from . import (
    fetch_disclosures,
    fetch_disclosure_detail,
    parse_capital,
    parse_contract,
    parse_treasury,
    render_markdown,
    summarize_contracts,
)


def _utf8_stdout() -> None:
    if sys.stdout.encoding and sys.stdout.encoding.lower().startswith("utf"):
        return
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


def _maybe_load_dotenv() -> None:
    """프로젝트 루트의 .env 를 단순 파싱해서 환경변수에 주입."""
    if os.environ.get("DART_API_KEY"):
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


def _enrich_detail(rows, only_categories: set[str]) -> None:
    """카테고리에 해당하는 row만 본문 fetch + 파싱.

    정정공시는 변경된 항목만 담겨 있어 라벨-값 매칭이 빗나가기 쉬우므로
    본문 파싱은 건너뛰고 row 자체는 표에 그대로 남긴다.
    """
    fetched = 0
    for r in rows:
        if r.category not in only_categories:
            continue
        if r.is_amend:
            continue
        html = fetch_disclosure_detail(r.rcept_no)
        if not html:
            continue
        if r.category == "contract":
            r.detail = parse_contract(html)
        elif r.category == "treasury":
            r.detail = parse_treasury(html)
        elif r.category == "capital":
            r.detail = parse_capital(html)
        fetched += 1
        time.sleep(0.3)
    sys.stderr.write(f"[detail] {fetched}건 본문 파싱 완료\n")


def main() -> None:
    p = argparse.ArgumentParser(prog="module_disclosure")
    p.add_argument("code", help="6자리 종목코드 또는 기업명 (예: 034020 / 두산에너빌리티)")
    p.add_argument("--days", type=int, default=60, help="조회 기간 (기본 60일)")
    p.add_argument("--guidance", type=float, default=None,
                   help="당해년도 수주 가이던스 (조 단위) — 진척률 자동 계산")
    p.add_argument("--category",
                   choices=["contract", "treasury", "capital", "equity", "earnings", "other"],
                   help="특정 카테고리만 출력")
    p.add_argument("--no-detail", action="store_true",
                   help="본문 파싱 skip (목록만, 빠름)")
    p.add_argument("--business-report", action="store_true",
                   help="공시목록 대신 최근 사업/반기/분기 보고서 'II. 사업의 내용' 본문 fetch")
    p.add_argument("--json", action="store_true", help="JSON 으로 raw rows dump")
    p.add_argument("--out", default="", help="markdown 결과를 저장할 경로 (없으면 stdout)")
    args = p.parse_args()
    # '.KS'/'.KQ' 등 거래소 접미사 자동 strip(6자리 코드일 때만 — 회사명 입력은 그대로 둔다).
    if "." in args.code:
        _stem = args.code.partition(".")[0]
        if _stem.isdigit() and len(_stem) == 6:
            args.code = _stem
    _utf8_stdout()
    _maybe_load_dotenv()

    # 사업보고서 본문 모드 — 공시목록 대신 "II. 사업의 내용" 섹션 fetch.
    if args.business_report:
        from ._business_report import fetch_business_report
        rep = fetch_business_report(args.code)
        if not rep:
            print(f"사업보고서 없음 또는 corp_code 미해결: {args.code} "
                  f"(DART_API_KEY 설정 확인)")
            return
        md = (f"# {args.code} — 사업보고서 본문\n\n"
              f"- 보고서: {rep.report_nm} ({rep.rcept_dt})  rcept_no={rep.rcept_no}\n\n"
              f"## II. 사업의 내용\n\n{rep.business_section or '(본문 추출 실패)'}\n")
        if args.out:
            Path(args.out).parent.mkdir(parents=True, exist_ok=True)
            Path(args.out).write_text(md, encoding="utf-8")
            print(f"saved: {args.out}")
        else:
            print(md)
        return

    rows = fetch_disclosures(args.code, days=args.days)

    enrich_cats = {"contract", "treasury", "capital"}
    if args.category:
        enrich_cats &= {args.category}
    if not args.no_detail and enrich_cats:
        _enrich_detail(rows, enrich_cats)

    if args.json:
        out_rows = []
        for r in rows:
            out_rows.append({
                "rcept_no":  r.rcept_no,
                "rcept_dt":  r.rcept_dt,
                "report_nm": r.report_nm,
                "flr_nm":    r.flr_nm,
                "category":  r.category,
                "is_amend":  r.is_amend,
                "url":       r.url,
                "detail":    r.detail,
            })
        print(json.dumps(out_rows, ensure_ascii=False, indent=2))
        return

    name = rows[0].corp_name if rows else args.code
    display_code = args.code if args.code.isdigit() and len(args.code) == 6 else (
        rows[0].corp_code if rows else args.code
    )
    contract_summary = summarize_contracts(rows, ytd_guidance_jo=args.guidance)
    md = render_markdown(
        code=display_code,
        name=name,
        rows=rows,
        contract_summary=contract_summary,
        days=args.days,
        only_category=args.category,
    )

    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(md, encoding="utf-8")
        print(f"saved: {args.out}")
    else:
        print(md)


if __name__ == "__main__":
    main()
