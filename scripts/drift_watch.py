# -*- coding: utf-8 -*-
"""drift_watch — 데스크 완주 후 킬스위치 드리프트 감시 (리포트가 거짓말되는 걸 잡는다).

왜: 2026-07-13 실증 — 데스크가 15:59 완주했는데 밤사이 이란/호르무즈가 뒤집혀
MACRO_REPORT M-05("오일 드레인")가 6시간 동안 스테일. 사람이 우연히 잡아 §5 애드덤을
덧댔다. 이 스크립트는 그 "우연"을 결정론 루틴으로 바꾼다 — 완주 시각 이후 뉴스에서
킬스위치 테마의 버스트를 감지해 애드덤 후보를 띄운다. 판단(애드덤 쓸지)은 에이전트 몫.

방법(결정론):
  1. 리포트 파일 mtime = 기준시각 (--since 로 덮어쓰기 가능)
  2. 리포트 본문에서 anti-signal / kill-switch 줄 추출(사람이 읽게 그대로 표시)
  3. 상시 고임팩트 텀셋을 news_fts 에서 기준시각 이후 카운트
  4. 같은 텀의 직전 7일 시간당 평균 대비 버스트 배율 ≥ threshold → 🚨DRIFT? 플래그
     + 샘플 헤드라인 3개 (에이전트가 애드덤 판단할 재료)

사용:
  python -X utf8 scripts/drift_watch.py                                # 오늘 industry_US MACRO_REPORT 기준
  python -X utf8 scripts/drift_watch.py --report llm_outputs/2026-07-13/industry_US/MACRO_REPORT.md
  python -X utf8 scripts/drift_watch.py --threshold 2.5 --json

배선 권장: 데스크 완주 3~6시간 후(저녁) 한 번. 🚨 뜨면 에이전트가 원문 읽고
  MACRO_REPORT 에 ADDENDUM append(§5 스타일, 클로버 금지).
"""
from __future__ import annotations
import argparse
import json
import re
import sqlite3
import sys
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FTS_DB = ROOT / "data" / "news_fts.db"

FOREIGN_SOURCES = sorted({
    "bloomberg", "google_en", "bbc", "scmp", "marketwatch", "upi", "nyt",
    "seekingalpha", "yahoo_finance", "prnewswire", "cnbc", "thediplomat",
    "sec_edgar", "foreignpolicy", "investing_en", "google_news_en", "fxstreet",
})

# 상시 고임팩트 킬스위치 텀셋 — 리포트의 흔한 anti-signal 축들.
# (리포트별 고유 anti-signal은 §2에서 자동 추출해 사람이 대조)
KILL_TERMS = [
    "Strait of Hormuz", "Hormuz closed", "ceasefire", "strikes on Iran",
    "emergency FOMC", "emergency meeting", "rate hike", "rate cut",
    "circuit breaker", "flash crash", "default", "bankruptcy",
    "capex cut", "guidance cut", "export ban", "new tariff",
    "state of emergency", "invasion", "blockade", "downgrade",
]


def count_since(con, term: str, since_iso: str) -> int:
    q = ("SELECT count(*) FROM news_fts WHERE news_fts MATCH ? AND fetched_at >= ? "
         "AND source IN (" + ",".join("?" * len(FOREIGN_SOURCES)) + ")")
    return con.execute(q, [f'"{term}"', since_iso, *FOREIGN_SOURCES]).fetchone()[0]


def samples_since(con, term: str, since_iso: str, n: int = 3) -> list[str]:
    q = ("SELECT title FROM news_fts WHERE news_fts MATCH ? AND fetched_at >= ? "
         "AND source IN (" + ",".join("?" * len(FOREIGN_SOURCES)) + ") "
         "ORDER BY fetched_at DESC LIMIT ?")
    return [r[0] for r in con.execute(q, [f'"{term}"', since_iso, *FOREIGN_SOURCES, n])]


def main():
    ap = argparse.ArgumentParser("drift_watch")
    ap.add_argument("--report", default=None,
                    help="기준 리포트 경로(기본: 오늘 industry_US/MACRO_REPORT.md)")
    ap.add_argument("--since", default=None, help="기준시각 ISO 덮어쓰기(기본: 리포트 mtime)")
    ap.add_argument("--threshold", type=float, default=3.0, help="버스트 배율 임계(기본 3x)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if not FTS_DB.exists():
        sys.exit("news_fts.db 없음 — 먼저 scripts/news_fts.py build")

    today = datetime.now().date().isoformat()
    rpt = Path(args.report) if args.report else \
        ROOT / "llm_outputs" / today / "industry_US" / "MACRO_REPORT.md"
    if not rpt.exists():
        sys.exit(f"리포트 없음: {rpt} — --report 로 지정")

    since_dt = datetime.fromisoformat(args.since) if args.since else \
        datetime.fromtimestamp(rpt.stat().st_mtime)
    since_iso = since_dt.isoformat()
    hours = max((datetime.now() - since_dt).total_seconds() / 3600, 0.1)

    # §2 리포트 고유 anti-signal 줄 추출(사람 대조용)
    text = rpt.read_text(encoding="utf-8", errors="replace")
    anti_lines = [ln.strip("- ").strip() for ln in text.splitlines()
                  if re.search(r"anti-signal|kill-?switch|킬스위치", ln, re.I)][:20]

    con = sqlite3.connect(str(FTS_DB))
    week_ago = (since_dt - timedelta(days=7)).isoformat()
    results = []
    for term in KILL_TERMS:
        n_now = count_since(con, term, since_iso)
        if n_now == 0:
            continue
        n_base = count_since(con, term, week_ago) - n_now   # 직전 7일(기준시각 전)
        base_rate = n_base / (7 * 24)                        # 시간당
        now_rate = n_now / hours
        burst = (now_rate / base_rate) if base_rate > 0 else float("inf")
        flagged = burst >= args.threshold and n_now >= 3
        results.append({
            "term": term, "since_count": n_now,
            "burst": None if burst == float("inf") else round(burst, 1),
            "flag": flagged,
            "samples": samples_since(con, term, since_iso) if flagged else [],
        })
    results.sort(key=lambda r: (not r["flag"], -(r["burst"] or 9999)))
    flagged = [r for r in results if r["flag"]]

    if args.json:
        print(json.dumps({"report": str(rpt), "since": since_iso,
                          "hours": round(hours, 1), "threshold": args.threshold,
                          "flagged": flagged, "all": results,
                          "report_anti_signals": anti_lines}, ensure_ascii=False, indent=1))
        return

    print(f"# drift_watch — {rpt.name} 완주({since_iso[:16]}) 이후 {hours:.1f}h 감시")
    if not flagged:
        print("\n✅ 킬스위치 버스트 없음 — 리포트 스테일 신호 없음.")
    else:
        print(f"\n🚨 DRIFT 후보 {len(flagged)}건 (버스트 ≥{args.threshold}x) — 애드덤 판단 필요:")
        for r in flagged:
            b = "∞" if r["burst"] is None else f"{r['burst']}x"
            print(f"\n  [{r['term']}]  완주 후 {r['since_count']}건, 평시 대비 {b}")
            for s in r["samples"]:
                print(f"    - {s[:100]}")
    others = [r for r in results if not r["flag"]][:8]
    if others:
        print("\n(비버스트 활동: " + ", ".join(f"{r['term']} {r['since_count']}" for r in others) + ")")
    if anti_lines:
        print("\n## 리포트 고유 anti-signal (사람 대조용)")
        for ln in anti_lines[:10]:
            print(f"  - {ln[:120]}")
    print("\n다음 행동: 🚨 항목은 news_fts --snippet 으로 원문 확인 → 리포트에 ADDENDUM append(클로버 금지).")


if __name__ == "__main__":
    main()
