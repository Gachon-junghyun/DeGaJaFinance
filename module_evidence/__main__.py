# -*- coding: utf-8 -*-
"""module_evidence CLI.

    python -m module_evidence build                  # md → data/evidence.db 재생성
    python -m module_evidence cite 수주               # 한 단어 → 근거 행(출처·날짜·링크)
    python -m module_evidence cite PF --tag measured --market KR
    python -m module_evidence where 000720            # 그 종목이 걸린 근거 전부
    python -m module_evidence show M1032              # 정의 + 어디서 인용됐나
    python -m module_evidence next-id M --count 13    # ID 발급(3-grep 대체)
    python -m module_evidence stats                   # 색인 현황
"""
from __future__ import annotations

import argparse
import json
import sys

from ._config import FAMILIES, utf8_stdout
from ._ids import next_id
from ._store import build, cite, show, stats, where_ticker

_DECOR = "*`"


def _flat(s: str, n: int) -> str:
    s = " ".join((s or "").split())
    for ch in _DECOR:
        s = s.replace(ch, "")
    return s if len(s) <= n else s[: n - 1] + "…"


def _print_rows(rows, width: int = 96, show_evidence: bool = True) -> None:
    for r in rows:
        head = r["cid"] or f"{r['file'].split('/')[-1]}:{r['line']}"
        badge = {"ledger": "원장", "registry": "등록부", "report": "리포트"}.get(r["kind"], r["kind"])
        tag = f" [{r['tag']}]" if r["tag"] else ""
        inherited = " ⤴상속" if r["scope"] == "section" else ""
        print(f"\n  {head}  · {badge}{tag}{inherited}")
        print(f"    {_flat(r['claim'], width)}")
        if show_evidence and r["evidence"]:
            print(f"    └ {_flat(r['evidence'], width)}")
        meta = f"    출처 {_flat(r['source'], 46) or '—'}  · asof {r['asof'] or '—'}"
        if r["run"]:
            meta += f"  · run {_flat(r['run'], 18)}"
        print(meta)
        print(f"    {r['file']}:{r['line']}" + (f"  · {r['link'].split(' ')[0]}" if r["link"] else ""))


def main() -> None:
    utf8_stdout()
    ap = argparse.ArgumentParser(prog="module_evidence",
                                 description="출처 저장소 색인 + ID 브로커")
    sub = ap.add_subparsers(dest="cmd", required=True)

    pb = sub.add_parser("build", help="md 전량 재수확 → 색인 재생성")
    pb.add_argument("--include-runs", action="store_true",
                    help="llm_outputs/ 런 사본도 주장으로 넣는다(기본 꺼짐 — 중복)")

    pc = sub.add_parser("cite", help="한 단어 → 근거 행")
    pc.add_argument("term", help="검색어(2자 한글 가능) 또는 ID")
    pc.add_argument("--limit", type=int, default=15)
    pc.add_argument("--kind", default="", choices=["", "ledger", "registry", "report"])
    pc.add_argument("--market", default="", choices=["", "KR", "US"])
    pc.add_argument("--tag", default="", help="measured / unverified / inferred …")
    pc.add_argument("--since", default="", help="asof >= YYYY-MM-DD")
    pc.add_argument("--json", action="store_true")

    pw = sub.add_parser("where", help="종목이 걸린 근거 전부")
    pw.add_argument("token", help="6자리(000720) 또는 티커(RTX)")
    pw.add_argument("--limit", type=int, default=20)
    pw.add_argument("--json", action="store_true")

    ps = sub.add_parser("show", help="ID 정의 + 인용 백링크")
    ps.add_argument("cid")
    ps.add_argument("--json", action="store_true")

    pn = sub.add_parser("next-id", help="다음 ID 발급 (파일에 쓰지는 않는다)")
    pn.add_argument("family", help="/".join(f"{k}={v}" for k, v in FAMILIES.items()))
    pn.add_argument("--count", type=int, default=1)
    pn.add_argument("--market", default="", help="KR/US 접미사를 붙일 때만")
    pn.add_argument("--fast", action="store_true", help="라이브 스캔 대신 DB(빠르지만 색인 시점까지만)")
    pn.add_argument("--json", action="store_true")

    pt = sub.add_parser("stats", help="색인 현황")
    pt.add_argument("--json", action="store_true")

    a = ap.parse_args()

    if a.cmd == "build":
        s = build(include_runs=a.include_runs)
        f = s["files"]
        print(f"색인 재생성 — 주장 {s['claims']:,} · 인용 {s['refs']:,} · 고유ID {s['ids']:,} "
              f"({s['secs']}초)")
        print(f"  스캔: handoff {f['handoff']} · REPORT {f['report']} · llm_outputs {f['runs']} md")
        return

    if a.cmd == "cite":
        rows = cite(a.term, limit=a.limit, kind=a.kind, market=a.market,
                    tag=a.tag, since=a.since)
        if a.json:
            print(json.dumps([dict(r) for r in rows], ensure_ascii=False, indent=1))
            return
        if not rows:
            print(f"「{a.term}」 근거 0건 — 색인이 비었으면 `build` 먼저. "
                  f"없다는 것이 부재의 증거는 아니다(어휘 불일치일 수 있다).")
            return
        print(f"# 「{a.term}」 근거 {len(rows)}건")
        _print_rows(rows)
        return

    if a.cmd == "where":
        rows = where_ticker(a.token, limit=a.limit)
        if a.json:
            print(json.dumps([dict(r) for r in rows], ensure_ascii=False, indent=1))
            return
        if not rows:
            print(f"{a.token} 근거 0건")
            return
        print(f"# {a.token} 근거 {len(rows)}건")
        _print_rows(rows)
        return

    if a.cmd == "show":
        defs, refs = show(a.cid)
        if a.json:
            print(json.dumps({"defs": [dict(d) for d in defs], "refs": [dict(r) for r in refs]},
                             ensure_ascii=False, indent=1))
            return
        if not defs and not refs:
            print(f"{a.cid} 없음")
            return
        print(f"# {a.cid.upper()} — 정의 {len(defs)} · 인용 {len(refs)}")
        if len(defs) > 1:
            print("  ⚠ 정의가 2개 이상이다 — 같은 번호가 두 뜻을 갖고 있을 수 있다(충돌 후보).")
        _print_rows(defs)
        if refs:
            print(f"\n  ── 인용된 곳 {len(refs)} ──")
            for r in refs[:40]:
                print(f"    {r['file']}:{r['line']}  {_flat(r['context'], 84)}")
        return

    if a.cmd == "next-id":
        try:
            r = next_id(a.family, count=a.count, market=a.market, fast=a.fast)
        except ValueError as e:
            print(e)
            sys.exit(2)
        if a.json:
            print(json.dumps(r, ensure_ascii=False))
            return
        print(f"# {r['family']} 계열 — {r['meaning']}")
        print(f"  현재 최고 {r['highest']}" + (f"  ({r['highest_at']})" if r["highest_at"] else ""))
        print(f"  스캔 범위: {r['scanned']}")
        print(f"  발급: {r['ids'][0]}" + (f" – {r['ids'][-1]}  ({len(r['ids'])}개)"
                                          if len(r["ids"]) > 1 else ""))
        return

    if a.cmd == "stats":
        s = stats()
        if a.json:
            print(json.dumps(s, ensure_ascii=False, indent=1))
            return
        print(f"# 근거 색인 — 생성 {s['built_at'] or '(없음)'}")
        print(f"  주장 {s['claims']:,}  = 원장 {s['ledger']:,} · 등록부 {s['registry']:,} "
              f"· 리포트 {s['report']:,}")
        print(f"  리포트 출처 범위: 줄 {s['report_line_scope']:,} · 헤더상속 {s['report_sec_scope']:,}")
        print(f"  원자료 링크 있는 행 {s['with_link']:,} · 인용 백링크 {s['refs']:,}")
        print(f"  고유 ID {s['unique_ids']:,} — " +
              " · ".join(f"{k}{v}" for k, v in s["families"].items()))
        return


if __name__ == "__main__":
    main()
