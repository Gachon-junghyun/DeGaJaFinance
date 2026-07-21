# -*- coding: utf-8 -*-
"""drift — 기준시각 이후 킬스위치 텀 버스트 감지 (리포트가 밤사이 거짓말되는 걸 잡는다).

왜 여기 있나 (P6): 원래 `scripts/drift_watch.py` 가 `sqlite3.connect(data/news_fts.db)` 로
**서버 소유 DB 파일을 직접 열었다.** 클라이언트는 로컬 뉴스 DB 를 지운 상태가 정상이라
(CLAUDE.md "뉴스 접근 = API 우선") 그 스크립트는 클라이언트에서 기동 즉시 죽었다 —
실측 2026-07-17: DRIFT 스테이지(US 전용, "리포트가 밤사이 거짓말하지 않게" 하는 사후 가드)가
정작 그 스테이지를 돌리는 기계에서 실행 불가였다.

그래서 **DB 를 만지는 부분만** 이 모듈로 옮긴다. `DB_READ_CMDS` 에 등록돼 있으므로
`DEGAJA_NEWS_API` 만 켜면 `__main__` 이 argv 를 서버 `/exec` 로 넘겨 서버가 자기 DB 로
실행한다(전송 분기 재구현 0, P1). 리포트 파일 읽기·렌더는 클라이언트 몫이라
`scripts/drift_watch.py` 에 남는다(서버엔 그 리포트 파일이 없다).

⚠ `FOREIGN_SOURCES` 도 drift_watch 가 복붙해 갖고 있었다 → `_config` 의 단일 원본을 쓴다(P1).

방법(결정론):
  1. 기준시각(=리포트 완주 시각) 이후 각 킬텀의 건수
  2. 같은 텀의 직전 7일(기준시각 이전) 시간당 평균 = 평시 레이트
  3. 버스트 = 지금레이트 / 평시레이트 ≥ threshold 이고 건수 ≥ 3 → 🚨 플래그 + 샘플 제목
  ⚠ `hours` 는 **서버 시계**로 잰다 — `fetched_at` 을 찍는 게 서버라 그쪽이 맞는 시계다.

사용:
    python -m module_news_data drift --since 2026-07-17T18:00:00 --json
    python -m module_news_data drift --since 2026-07-17T18:00:00 --terms "Strait of Hormuz" ceasefire
"""
from __future__ import annotations

import json
import sqlite3
import sys
from datetime import datetime, timedelta

from ._config import FOREIGN_SOURCES, FTS_DB, utf8_stdout

# 상시 고임팩트 킬스위치 텀셋 — 리포트의 흔한 anti-signal 축들.
# (리포트별 고유 anti-signal 은 drift_watch 가 리포트 본문에서 따로 뽑아 사람에게 대조시킨다)
KILL_TERMS = [
    "Strait of Hormuz", "Hormuz closed", "ceasefire", "strikes on Iran",
    "emergency FOMC", "emergency meeting", "rate hike", "rate cut",
    "circuit breaker", "flash crash", "default", "bankruptcy",
    "capex cut", "guidance cut", "export ban", "new tariff",
    "state of emergency", "invasion", "blockade", "downgrade",
]


def _scope_clause(scope: str) -> tuple[str, list]:
    """scope → (SQL 조각, 파라미터). _theme_age 와 같은 규약."""
    if scope == "foreign":
        return ("source IN (" + ",".join("?" * len(FOREIGN_SOURCES)) + ")", list(FOREIGN_SOURCES))
    if scope == "domestic":
        return ("source NOT IN (" + ",".join("?" * len(FOREIGN_SOURCES)) + ")", list(FOREIGN_SOURCES))
    return ("", [])


def count_since(con: sqlite3.Connection, term: str, since_iso: str, scope: str) -> int:
    where = ["news_fts MATCH ?", "fetched_at >= ?"]
    params: list = [f'"{term}"', since_iso]
    clause, p = _scope_clause(scope)
    if clause:
        where.append(clause)
        params += p
    q = f"SELECT count(*) FROM news_fts WHERE {' AND '.join(where)}"
    return con.execute(q, params).fetchone()[0]


def samples_since(con: sqlite3.Connection, term: str, since_iso: str, scope: str,
                  n: int = 3) -> list[str]:
    where = ["news_fts MATCH ?", "fetched_at >= ?"]
    params: list = [f'"{term}"', since_iso]
    clause, p = _scope_clause(scope)
    if clause:
        where.append(clause)
        params += p
    q = (f"SELECT title FROM news_fts WHERE {' AND '.join(where)} "
         "ORDER BY fetched_at DESC LIMIT ?")
    return [r[0] for r in con.execute(q, [*params, n])]


def analyze(since_iso: str, terms: list[str], scope: str, threshold: float) -> dict:
    """기준시각 이후 버스트 분석. DB 를 읽는 유일한 지점."""
    since_dt = datetime.fromisoformat(since_iso)
    hours = max((datetime.now() - since_dt).total_seconds() / 3600, 0.1)
    week_ago = (since_dt - timedelta(days=7)).isoformat()

    con = sqlite3.connect(str(FTS_DB))
    try:
        results = []
        for term in terms:
            n_now = count_since(con, term, since_iso, scope)
            if n_now == 0:
                continue
            n_base = count_since(con, term, week_ago, scope) - n_now   # 직전 7일(기준시각 전)
            base_rate = n_base / (7 * 24)                              # 시간당
            now_rate = n_now / hours
            burst = (now_rate / base_rate) if base_rate > 0 else float("inf")
            flagged = burst >= threshold and n_now >= 3
            results.append({
                "term": term,
                "since_count": n_now,
                "baseline_count_7d": n_base,
                "burst": None if burst == float("inf") else round(burst, 1),
                "flag": flagged,
                "samples": samples_since(con, term, since_iso, scope) if flagged else [],
            })
    finally:
        con.close()

    results.sort(key=lambda r: (not r["flag"], -(r["burst"] or 9999)))
    return {
        "since": since_iso,
        "hours": round(hours, 1),
        "scope": scope,
        "threshold": threshold,
        "terms_checked": len(terms),
        "flagged": [r for r in results if r["flag"]],
        "all": results,
    }


def run(since: str, terms: list[str] | None, scope: str, threshold: float, as_json: bool) -> None:
    utf8_stdout()
    if not FTS_DB.exists():
        sys.exit("news_fts.db 없음 — 서버에서 `scripts/news_fts.py build`, "
                 "또는 클라이언트면 DEGAJA_NEWS_API 를 켜라(그러면 서버가 자기 DB 로 실행한다).")
    res = analyze(since, terms or KILL_TERMS, scope, threshold)

    if as_json:
        print(json.dumps(res, ensure_ascii=False, indent=1))
        return

    print(f"# drift — 기준 {res['since'][:16]} 이후 {res['hours']}h · {res['scope']} "
          f"· 텀 {res['terms_checked']}개 · 임계 {res['threshold']}x")
    if not res["flagged"]:
        print("\n✅ 킬스위치 버스트 없음 — 리포트 스테일 신호 없음.")
    else:
        print(f"\n🚨 DRIFT 후보 {len(res['flagged'])}건 — 애드덤 판단 필요:")
        for r in res["flagged"]:
            b = "∞" if r["burst"] is None else f"{r['burst']}x"
            print(f"\n  [{r['term']}]  기준 후 {r['since_count']}건, 평시 대비 {b}")
            for s in r["samples"]:
                print(f"    - {s[:100]}")
    others = [r for r in res["all"] if not r["flag"]][:8]
    if others:
        print("\n(비버스트 활동: " + ", ".join(f"{r['term']} {r['since_count']}" for r in others) + ")")
    print("\n⚠ 판정 아님 — 🚨 는 원문(fts search --snippet)을 읽고 애드덤 여부를 사람/에이전트가 정한다.")


def cli_register(sub) -> None:
    p = sub.add_parser("drift", help="기준시각 이후 킬스위치 텀 버스트(리포트 스테일 감지)")
    p.add_argument("--since", required=True, help="기준시각 ISO(보통 리포트 완주 mtime)")
    p.add_argument("--terms", nargs="+", default=None,
                   help=f"검사할 텀(기본: 내장 킬텀 {len(KILL_TERMS)}개)")
    p.add_argument("--scope", choices=["all", "foreign", "domestic"], default="foreign")
    p.add_argument("--threshold", type=float, default=3.0, help="버스트 배율 임계(기본 3x)")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=lambda a: run(a.since, a.terms, a.scope, a.threshold, a.json))
