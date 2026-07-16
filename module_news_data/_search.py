# -*- coding: utf-8 -*-
"""LIKE 키워드 검색 — news_alert.db 전체 기사 풀 (옛 search_news_alert.py 포팅).

title+summary(기본) 또는 body 까지(--field any) substring 매칭. 정밀·랭킹이
필요하면 _fts(BM25) 를 쓰고, 이건 '있는 그대로 다 보기' 용도.
옛 scenario.db nodes 제외 로직은 은퇴(2026-06-22)라 포팅에서 제거함.

사용:
    python -m module_news_data search "변압기" HVDC 송전망 --days 14
    python -m module_news_data search humanoid Optimus --days 90 --scope foreign
    python -m module_news_data search 삼성전자 HBM --field any --match-mode and
"""
from __future__ import annotations

import sqlite3
from datetime import datetime, timedelta

from ._config import FOREIGN_SOURCES, NEWS_DB, origin_tag, utf8_stdout


def search(
    query_keywords: list[str],
    limit: int = 80,
    days: int | None = None,
    scope: str = "all",
    field: str = "both",
    match_mode: str = "or",
) -> None:
    utf8_stdout()
    nc = sqlite3.connect(str(NEWS_DB))
    nc.row_factory = sqlite3.Row

    # 키워드 매칭. or(기본)=하나라도, and=모든 키워드가 같은 레코드에.
    # and + 종목명+한정어 조합으로 OR 단일토큰 노이즈(ESG·마케팅 기사) 억제.
    joiner = " AND " if match_mode == "and" else " OR "
    if field == "title":
        per_kw = ["s.title LIKE ?"] * len(query_keywords)
        params: list = [f"%{kw}%" for kw in query_keywords]
    elif field == "any":  # title|summary|body — 본문까지(누락 ~76% 복구). and 모드 권장.
        per_kw = ["(s.title LIKE ? OR s.summary LIKE ? OR a.body LIKE ?)"] * len(query_keywords)
        params = []
        for kw in query_keywords:
            params.extend([f"%{kw}%"] * 3)
    else:  # both (기본) — title 또는 summary
        per_kw = ["(s.title LIKE ? OR s.summary LIKE ?)"] * len(query_keywords)
        params = []
        for kw in query_keywords:
            params.extend([f"%{kw}%"] * 2)
    where_parts = ["(" + joiner.join(per_kw) + ")"]

    fs = FOREIGN_SOURCES
    if scope == "foreign":
        where_parts.append("s.source IN (" + ",".join("?" * len(fs)) + ")")
        params.extend(fs)
    elif scope == "domestic":
        where_parts.append("(s.source IS NULL OR s.source NOT IN (" + ",".join("?" * len(fs)) + "))")
        params.extend(fs)

    if days is not None:
        cutoff = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
        where_parts.append("s.fetched_at >= ?")
        params.append(cutoff)

    sql = f"""
        SELECT s.url_hash, s.url, s.title, s.source, s.published_at, s.fetched_at,
               COALESCE(LENGTH(a.body), 0) AS body_len, a.status
        FROM seen_news s
        LEFT JOIN article_contents a ON s.url_hash = a.url_hash
        WHERE {' AND '.join(where_parts)}
        ORDER BY COALESCE(s.published_at, s.fetched_at) DESC
    """
    rows = nc.execute(sql, params).fetchall()

    n_en = sum(1 for r in rows if origin_tag(r["source"]) == "EN")
    n_kr = len(rows) - n_en

    range_str = f"최근 {days}일" if days is not None else "전체 기간"
    scope_str = {"all": "국내+해외", "foreign": "해외만", "domestic": "국내만"}[scope]
    print(f'🔍 news 검색 [{range_str}] [{scope_str}/{field}/{match_mode.upper()}]: {", ".join(query_keywords)}')
    print(f"매칭: {len(rows)}건  (국내 {n_kr} / 해외 {n_en})  — 최신순 상위 {min(limit, len(rows))}개")
    print("=" * 100)

    for r in rows[:limit]:
        dt = (r["published_at"] or r["fetched_at"] or "")[:10]
        src = r["source"] or "-"
        body_info = f"body={r['body_len']}자" if r["status"] == "ok" else f"[{r['status'] or 'no body'}]"
        print(f"  {dt}  [{origin_tag(r['source'])}] [{src:>13}] {body_info:>14}  {r['title']}")

    nc.close()


def cli_register(sub) -> None:
    p = sub.add_parser("search", help="LIKE 키워드 검색 (title+summary 기본, --field any=본문까지)")
    p.add_argument("keywords", nargs="+")
    p.add_argument("--days", type=int, default=None, help="최근 N일 (fetched_at 기준)")
    p.add_argument("--limit", type=int, default=80)
    p.add_argument("--scope", choices=["all", "foreign", "domestic"], default="all")
    p.add_argument("--field", choices=["both", "title", "any"], default="both")
    p.add_argument("--match-mode", choices=["or", "and"], default="or", dest="match_mode")
    p.set_defaults(func=lambda a: search(
        a.keywords, limit=a.limit, days=a.days, scope=a.scope,
        field=a.field, match_mode=a.match_mode))
