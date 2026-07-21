# -*- coding: utf-8 -*-
"""drift_watch — 데스크 완주 후 킬스위치 드리프트 감시 (리포트가 거짓말되는 걸 잡는다).

왜: 2026-07-13 실증 — 데스크가 15:59 완주했는데 밤사이 이란/호르무즈가 뒤집혀
MACRO_REPORT M-05("오일 드레인")가 6시간 동안 스테일. 사람이 우연히 잡아 §5 애드덤을
덧댔다. 이 스크립트는 그 "우연"을 결정론 루틴으로 바꾼다 — 완주 시각 이후 뉴스에서
킬스위치 테마의 버스트를 감지해 애드덤 후보를 띄운다. 판단(애드덤 쓸지)은 에이전트 몫.

역할 분담 (2026-07-17 P6 수리):
  · **뉴스 DB 질의·버스트 산식** = `module_news_data drift` (거기 한 곳). 예전엔 이 파일이
    `sqlite3.connect(data/news_fts.db)` 로 **서버 소유 DB 를 직접 열어서**, 로컬 뉴스 DB 를
    지운 정상 클라이언트에서 기동 즉시 죽었다("news_fts.db 없음") — DRIFT 스테이지가
    정작 그 스테이지를 돌리는 기계에서 실행 불가. `DEGAJA_NEWS_API` 만 켜면 그 서브커맨드가
    서버 `/exec` 로 라우팅된다(CLAUDE.md P6, 전송 분기 재구현 0).
  · **리포트 파일 읽기(mtime·anti-signal 추출)·렌더** = 이 파일. 서버엔 이 리포트가 없으니
    클라이언트에 남아야 한다.

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
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _drift_via_module(since_iso: str, scope: str, threshold: float) -> dict:
    """뉴스 DB 질의는 module_news_data 에 위임 — `DEGAJA_NEWS_API` 면 서버 /exec 로 자동 라우팅.

    ⚠ import 가 아니라 서브프로세스인 이유: 원격 라우팅 분기가 `module_news_data.__main__`
    에 있다(거기가 단일 원본). 함수를 직접 부르면 그 분기를 건너뛰어 로컬 DB 를 찾다 죽는다.
    """
    cmd = [sys.executable, "-X", "utf8", "-m", "module_news_data", "drift",
           "--since", since_iso, "--scope", scope, "--threshold", str(threshold), "--json"]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", cwd=str(ROOT))
    out = (r.stdout or "").strip()
    if r.returncode != 0 or not out:
        sys.exit(f"drift 질의 실패 (rc={r.returncode}): {(r.stderr or out or '')[:300]}")
    try:
        return json.loads(out[out.index("{"):])       # 원격 헤더(· via API) 앞머리 무시
    except (ValueError, json.JSONDecodeError) as e:
        sys.exit(f"drift 응답 파싱 실패: {e}\n{out[:300]}")


def main():
    ap = argparse.ArgumentParser("drift_watch")
    ap.add_argument("--report", default=None,
                    help="기준 리포트 경로(기본: 오늘 industry_US/MACRO_REPORT.md)")
    ap.add_argument("--since", default=None, help="기준시각 ISO 덮어쓰기(기본: 리포트 mtime)")
    ap.add_argument("--scope", choices=["all", "foreign", "domestic"], default="foreign")
    ap.add_argument("--threshold", type=float, default=3.0, help="버스트 배율 임계(기본 3x)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    today = datetime.now().date().isoformat()
    rpt = Path(args.report) if args.report else \
        ROOT / "llm_outputs" / today / "industry_US" / "MACRO_REPORT.md"
    if not rpt.exists():
        sys.exit(f"리포트 없음: {rpt} — --report 로 지정")

    since_dt = datetime.fromisoformat(args.since) if args.since else \
        datetime.fromtimestamp(rpt.stat().st_mtime)
    since_iso = since_dt.isoformat()

    # §2 리포트 고유 anti-signal 줄 추출(사람 대조용) — 리포트는 클라이언트에만 있다.
    text = rpt.read_text(encoding="utf-8", errors="replace")
    anti_lines = [ln.strip("- ").strip() for ln in text.splitlines()
                  if re.search(r"anti-signal|kill-?switch|킬스위치", ln, re.I)][:20]

    res = _drift_via_module(since_iso, args.scope, args.threshold)
    flagged = res["flagged"]

    if args.json:
        print(json.dumps({"report": str(rpt), **res,
                          "report_anti_signals": anti_lines}, ensure_ascii=False, indent=1))
        return

    print(f"# drift_watch — {rpt.name} 완주({since_iso[:16]}) 이후 {res['hours']}h 감시")
    if not flagged:
        print("\n✅ 킬스위치 버스트 없음 — 리포트 스테일 신호 없음.")
    else:
        print(f"\n🚨 DRIFT 후보 {len(flagged)}건 (버스트 ≥{args.threshold}x) — 애드덤 판단 필요:")
        for r in flagged:
            b = "∞" if r["burst"] is None else f"{r['burst']}x"
            print(f"\n  [{r['term']}]  완주 후 {r['since_count']}건, 평시 대비 {b}")
            for s in r["samples"]:
                print(f"    - {s[:100]}")
    others = [r for r in res["all"] if not r["flag"]][:8]
    if others:
        print("\n(비버스트 활동: " + ", ".join(f"{r['term']} {r['since_count']}" for r in others) + ")")
    if anti_lines:
        print("\n## 리포트 고유 anti-signal (사람 대조용)")
        for ln in anti_lines[:10]:
            print(f"  - {ln[:120]}")
    print("\n다음 행동: 🚨 항목은 news_fts --snippet 으로 원문 확인 → 리포트에 ADDENDUM append(클로버 금지).")


if __name__ == "__main__":
    main()
