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


# 결측 표기 — 빈칸과 크래시는 다른 물건이다(D119).
# 네이버 페이지에 항목이 없으면 스크래퍼가 None 을 남기는데, 헤더가 그 None 에
# ':,.0f' 포맷을 걸어 TypeError 로 죽었다(실측 042700: per_fwd·eps_fwd 결측).
_MISSING = "—"


def _num(v, spec: str = ",.0f") -> str:
    """숫자를 포맷하되 None/비수치는 빈칸으로. 값이 있으면 기존 출력과 동일."""
    if v is None:
        return _MISSING
    try:
        return format(v, spec)
    except (TypeError, ValueError):
        return _MISSING


def _val(v) -> str:
    """포맷 스펙 없이 그대로 찍던 자리(기존 동작 유지) — None 만 빈칸으로."""
    return _MISSING if v is None else str(v)


# 헤더가 실제로 찍는 필드만 결측 점검한다(표시하지 않는 값은 보고하지 않는다).
_HEADER_FIELDS = [
    ("name", "종목명"),
    ("price", "현재가"),
    ("market_cap_eok", "시총"),
    ("target_price", "컨센 목표주가"),
    ("per_fwd", "12M Fwd PER"),
    ("eps_fwd", "추정 EPS"),
    ("per_ttm", "TTM PER"),
    ("pbr", "PBR"),
    ("foreign_pct", "외국인 소진율"),
    ("industry_per", "동일업종 PER"),
]


def _missing_fields(snap) -> list:
    return [f for f, _ in _HEADER_FIELDS if getattr(snap, f, None) is None]


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
        payload = to_dict(snap)
        miss = _missing_fields(snap)
        payload["missing_fields"] = miss
        payload["missing_reason"] = (
            "naver finance item page did not carry these fields (null != 0)"
            if miss
            else ""
        )
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return

    peers = [c.strip() for c in args.peers.split(",") if c.strip()]

    df = build_peer_table(args.code, peers)
    df = add_peer_avg(df)

    snap = fetch_naver_snapshot(args.code)

    header = (
        f"# {_val(snap.name)} ({snap.code}) — Valuation Snapshot\n\n"
        f"- 현재가: {_num(snap.price)}원 / 시총: {_num(snap.market_cap_eok)}억원\n"
        f"- 컨센 목표주가: {_num(snap.target_price)}원 "
        f"(상승여력 {_num(snap.upside_pct(), '+.2f')}%)\n"
        f"- 12M Fwd PER: {_val(snap.per_fwd)}배 / EPS: {_num(snap.eps_fwd)}원\n"
        f"- TTM PER: {_val(snap.per_ttm)}배 / PBR: {_val(snap.pbr)}배\n"
        f"- 외국인 소진율: {_val(snap.foreign_pct)}% / 동일업종 PER: {_val(snap.industry_per)}배\n\n"
    )
    miss = _missing_fields(snap)
    if miss:
        labels = {f: ko for f, ko in _HEADER_FIELDS}
        header += (
            f"> ⚠ 결측 {len(miss)}개 — {', '.join(labels[f] for f in miss)}: "
            "네이버 금융 종목페이지에 해당 항목이 없다(수집 실패가 아니라 미제공). "
            "빈칸은 0 이 아니다.\n\n"
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
