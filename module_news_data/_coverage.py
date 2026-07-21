# -*- coding: utf-8 -*-
"""커버리지 미터 — 검색어가 DB 풀의 몇 %를 실제로 보는지, 분모 포함 (옛 news_coverage.py 포팅).

title+summary 검색은 본문에만 있는 관련기사(~72~84%)를 놓친다(실측). 이 도구는
같은 쿼리를 3층으로 분해: ①현재 검색 커버리지 ②본문 블라인드(복구 가능 누락)
③본문 가용률. 판정 🔴≥60% / 🟡≥30% / 🟢양호.

사용:
    python -m module_news_data coverage nuclear "data center" --days 30 --scope foreign
    python -m module_news_data coverage 변압기 HVDC --days 14 --json
"""
from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timedelta

from ._config import BODY_MIN, FOREIGN_SOURCES, NEWS_DB, utf8_stdout


def _scope_clause(scope: str, params: list) -> str:
    ph = ",".join("?" * len(FOREIGN_SOURCES))
    if scope == "foreign":
        params.extend(FOREIGN_SOURCES)
        return f"s.source IN ({ph})"
    if scope == "domestic":
        params.extend(FOREIGN_SOURCES)
        return f"(s.source IS NULL OR s.source NOT IN ({ph}))"
    return "1=1"


def _kw_clause(field: str, kws: list[str], mode: str, params: list) -> str:
    joiner = " AND " if mode == "and" else " OR "
    parts = []
    for kw in kws:
        k = f"%{kw}%"
        if field == "title_sum":
            parts.append("(s.title LIKE ? OR s.summary LIKE ?)")
            params.extend([k, k])
        elif field == "body":
            parts.append("a.body LIKE ?")
            params.append(k)
        else:  # any = title|sum|body
            parts.append("(s.title LIKE ? OR s.summary LIKE ? OR a.body LIKE ?)")
            params.extend([k, k, k])
    return "(" + joiner.join(parts) + ")"


def run(kws: list[str], days: int | None, scope: str, mode: str, as_json: bool) -> None:
    utf8_stdout()
    con = sqlite3.connect(str(NEWS_DB))
    c = con.cursor()

    def count(where: str, params: list, need_body=False) -> int:
        join = "JOIN article_contents a ON s.url_hash=a.url_hash" if need_body else ""
        return c.execute(f"SELECT COUNT(*) FROM seen_news s {join} WHERE {where}", params).fetchone()[0]

    def base():
        p: list = []
        w = [_scope_clause(scope, p)]
        if days is not None:
            cutoff = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
            w.append("s.fetched_at >= ?")
            p.append(cutoff)
        return w, p

    # 분모: 윈도우+scope 전체
    w, p = base()
    total = count(" AND ".join(w), p)
    # 본문 보유(윈도우 전체 중)
    w, p = base()
    w.append(f"LENGTH(a.body) >= {BODY_MIN}")
    body_avail = count(" AND ".join(w), p, need_body=True)

    # ① 현재 검색(title+summary)
    w, p = base()
    w.append(_kw_clause("title_sum", kws, mode, p))
    ts = count(" AND ".join(w), p)
    # ② 본문 매칭
    w, p = base()
    w.append(_kw_clause("body", kws, mode, p))
    body = count(" AND ".join(w), p, need_body=True)
    # ③ 본문엔 있는데 title/sum엔 없음 = 현재 검색이 놓친 것
    w, p = base()
    w.append(_kw_clause("body", kws, mode, p))
    w.append("NOT " + _kw_clause("title_sum", kws, mode, p))
    body_only = count(" AND ".join(w), p, need_body=True)
    union = ts + body_only

    def pct(a, b):
        return (100.0 * a / b) if b else 0.0

    rep = {
        "query": kws, "days": days, "scope": scope, "match_mode": mode,
        "window_total": total,
        "body_available": body_avail, "body_available_pct": round(pct(body_avail, total), 1),
        "title_sum_hits": ts,
        "body_hits": body,
        "body_only_missed": body_only,
        "recoverable_union": union,
        "current_recall_pct": round(pct(ts, union), 1),
        "body_blind_pct": round(pct(body_only, union), 1),
        "share_of_window_pct": round(pct(ts, total), 1),
    }

    if as_json:
        print(json.dumps(rep, ensure_ascii=False, indent=2))
        con.close()
        return

    sc = {"all": "국내+해외", "foreign": "해외만", "domestic": "국내만"}[scope]
    rng = f"최근 {days}일" if days else "전체기간"
    print(f"\n# 뉴스 커버리지 — {', '.join(kws)}  [{rng}/{sc}/{mode.upper()}]")
    print(f"  윈도우 전체 풀(분모)          : {total:>7}건   (본문 보유 {body_avail}건 = {rep['body_available_pct']}%)")
    print(f"  ① 현재 검색(title+summary)    : {ts:>7}건")
    print(f"  ② 본문 매칭                   : {body:>7}건")
    print(f"  ③ 본문엔 있는데 놓침          : {body_only:>7}건")
    print(f"  ─ 복구 시 도달 가능(합집합)   : {union:>7}건")
    print(f"  ▶ 현재 recall(본문 기준)      : {rep['current_recall_pct']:>6}%   ← 지금 보는 비율")
    print(f"  ▶ 본문 블라인드(놓치는 비율)  : {rep['body_blind_pct']:>6}%   ← 본문검색만 켜면 복구")
    verdict = ("🔴 심각" if rep["body_blind_pct"] >= 60 else
               "🟡 주의" if rep["body_blind_pct"] >= 30 else "🟢 양호")
    print(f"  판정: {verdict} — 본문검색 미적용 시 관련기사의 {rep['body_blind_pct']}%가 안 보임.")
    con.close()


def cli_register(sub) -> None:
    p = sub.add_parser("coverage", help="검색어 커버리지 %%  (분모 포함 3층 분해)")
    p.add_argument("keywords", nargs="+")
    p.add_argument("--days", type=int, default=None)
    p.add_argument("--scope", choices=["all", "foreign", "domestic"], default="all")
    p.add_argument("--match-mode", choices=["or", "and"], default="or", dest="match_mode")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=lambda a: run(a.keywords, a.days, a.scope, a.match_mode, a.json))
