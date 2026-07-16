"""CLI 진입점.

사용:
    python -m module_fundamentals_us NVDA
    python -m module_fundamentals_us NVDA --out llm_outputs/2026-05-27/nvda_fundamentals.md
    python -m module_fundamentals_us NVDA --json
    python -m module_fundamentals_us NVDA --no-xbrl
"""
from __future__ import annotations

import argparse
import io
import json
import os
import sys
from dataclasses import asdict
from pathlib import Path

from ._renderer import render_markdown
from ._xbrl_fetch import fetch_xbrl_quarterly_revenue
from ._yfinance_fetch import fetch_fundamentals


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
    """프로젝트 루트의 .env 를 단순 파싱해 환경변수에 주입.

    SEC_USER_AGENT override 등을 위해. module_disclosure 패턴 그대로.
    """
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


def main() -> None:
    _utf8_stdout()
    _maybe_load_dotenv()

    p = argparse.ArgumentParser(prog="module_fundamentals_us")
    p.add_argument("ticker", help="US 티커 (예: NVDA, AAPL)")
    p.add_argument("--no-xbrl", action="store_true", help="SEC XBRL skip (yfinance만, 빠른 모드)")
    p.add_argument("--json", action="store_true", help="snapshot JSON dump")
    p.add_argument("--out", default="", help="markdown 결과 저장 경로 (없으면 stdout)")
    args = p.parse_args()

    ticker = args.ticker.upper().strip()
    sys.stderr.write(f"[{ticker}] fetching yfinance...\n")
    snap = fetch_fundamentals(ticker)

    # Unknown ticker 가드 — 핵심 필드 모두 None & 회사명 없으면 알 수 없는 티커.
    if (
        snap.company_name is None
        and snap.price is None
        and snap.market_cap is None
        and snap.sector is None
        and not snap.quarterly_revenue
    ):
        sys.stderr.write(f"Unknown ticker: {ticker} (yfinance 에 데이터 없음 — 오타?)\n")
        sys.exit(1)

    if not args.no_xbrl:
        sys.stderr.write(f"[{ticker}] fetching SEC XBRL...\n")
        snap.quarterly_revenue_xbrl = fetch_xbrl_quarterly_revenue(ticker, limit=8)

    if args.json:
        d = asdict(snap)
        print(json.dumps(d, ensure_ascii=False, indent=2, default=str))
        return

    md = render_markdown(snap, xbrl_included=(not args.no_xbrl))
    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(md, encoding="utf-8")
        print(f"saved: {args.out}")
    else:
        print(md)

    # 일치율 보고 (fuzzy align ±7d)
    if not args.no_xbrl and snap.quarterly_revenue and snap.quarterly_revenue_xbrl:
        from ._renderer import _fuzzy_align

        aligned = _fuzzy_align(snap.quarterly_revenue, snap.quarterly_revenue_xbrl)
        paired = [(yv, xv) for _, yv, xv in aligned if yv is not None and xv is not None]
        match = sum(1 for yv, xv in paired if xv and abs(yv / xv - 1.0) < 0.05)
        sys.stderr.write(
            f"[{ticker}] yfinance<->XBRL 교차 검증: {match}/{len(paired)} 분기 5% 이내 일치\n"
        )

    sys.stderr.write(f"DONE: {ticker}\n")


if __name__ == "__main__":
    main()
