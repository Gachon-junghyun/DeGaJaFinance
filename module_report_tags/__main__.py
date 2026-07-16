# -*- coding: utf-8 -*-
"""module_report_tags CLI.

    python -m module_report_tags update          # REPORT/ 증분 스캔 → 인수인계 갱신
    python -m module_report_tags show            # HANDOFF.md 출력
    python -m module_report_tags ticker GEV      # 그 종목 다룬 리포트 역검색
"""
from __future__ import annotations

import argparse
import sys

from ._config import HANDOFF_MD, REPORT_DIR
from ._handoff import query_ticker, update


def _utf8() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def main() -> None:
    _utf8()
    ap = argparse.ArgumentParser(prog="module_report_tags")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("update", help="REPORT/ 증분 스캔 → 인수인계 원장 갱신")
    sub.add_parser("show", help="HANDOFF.md 출력")
    pt = sub.add_parser("ticker", help="종목 다룬 리포트 역검색")
    pt.add_argument("token", help="티커(GEV) 또는 6자리(005930)")
    args = ap.parse_args()

    if args.cmd == "update":
        s = update()
        print(f"인수인계 갱신 — 신규 {s['new']} / 변경 {s['changed']} / 유지 {s['kept']} "
              f"→ 총 {s['total']}건  (원장 {HANDOFF_MD})")
    elif args.cmd == "show":
        if HANDOFF_MD.exists():
            print(HANDOFF_MD.read_text(encoding="utf-8"))
        else:
            print(f"인수인계 원장 없음 — 먼저 `update` (REPORT_DIR={REPORT_DIR})")
    elif args.cmd == "ticker":
        hits = query_ticker(args.token)
        if not hits:
            print(f"{args.token} 를 다룬 리포트 없음 (또는 아직 update 안 함)")
            return
        print(f"# {args.token} 인수인계 — {len(hits)}개 리포트")
        for h in hits:
            v = " ".join(h["verdicts"][:4]) or "—"
            print(f"  [{h['desk']}] {h['report']}  · 평결 {v}  · {' / '.join(h['themes'])}")


if __name__ == "__main__":
    main()
