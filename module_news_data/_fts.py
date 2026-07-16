# -*- coding: utf-8 -*-
"""FTS5 전문검색 — title+summary+BODY, BM25 랭킹·구문·불리언·동의어 (옛 news_fts.py 포팅).

LIKE 검색(_search) 대비: 본문까지 색인, porter 스테밍(영문 어형), BM25 관련도순,
snippet 발췌, 동의어 확장. 색인은 옛 리포의 news_fts.db(append-only 증분) —
build/update 를 여기서 돌려도 라이브 news_alert.db 는 읽기만 하므로 안전.

⚠️ KR 색인은 trigram — 2글자 한글(실적·수주 등)은 0 반환(부재 아님). 3글자+ 대체어로.

사용:
    python -m module_news_data fts update                    # 새 기사만 증분 색인
    python -m module_news_data fts search "rate cut" Fed --days 14 --scope foreign
    python -m module_news_data fts search "rare earth" --syn --snippet
    python -m module_news_data fts search 이차전지 --kr --count
"""
from __future__ import annotations

import json
import sqlite3
import sys
from datetime import datetime, timedelta

from ._config import (
    FOREIGN_SOURCES, FTS_DB, FTS_DB_KR, NEWS_API_BASE, NEWS_DB, SYN_FILE, SYN_FILE_KR,
    utf8_stdout,
)


def _connect_fts(kr: bool = False) -> sqlite3.Connection:
    con = sqlite3.connect(str(FTS_DB_KR if kr else FTS_DB))
    con.row_factory = sqlite3.Row
    return con


def build(rebuild: bool, kr: bool = False) -> None:
    src = sqlite3.connect(str(NEWS_DB)); src.row_factory = sqlite3.Row
    fts = _connect_fts(kr)
    tokenizer = "trigram" if kr else "porter unicode61"
    if rebuild:
        fts.execute("DROP TABLE IF EXISTS news_fts")
    fts.execute(f"""
        CREATE VIRTUAL TABLE IF NOT EXISTS news_fts USING fts5(
            url_hash UNINDEXED, source UNINDEXED, fetched_at UNINDEXED, published_at UNINDEXED,
            has_body UNINDEXED, title, summary, body,
            tokenize='{tokenizer}'
        )""")
    row = fts.execute("SELECT MAX(fetched_at) FROM news_fts").fetchone()
    watermark = row[0] if row and row[0] else None
    where = ["s.fetched_at > ?"] if watermark else []
    params: list = [watermark] if watermark else []
    if kr:   # KR 색인은 국내 소스만(한글)
        where.append("(s.source IS NULL OR s.source NOT IN (" + ",".join("?" * len(FOREIGN_SOURCES)) + "))")
        params += FOREIGN_SOURCES
    wclause = ("WHERE " + " AND ".join(where)) if where else ""
    q = f"""
        SELECT s.url_hash, s.source, s.fetched_at, s.published_at, s.title, s.summary,
               a.body AS body
        FROM seen_news s LEFT JOIN article_contents a ON s.url_hash=a.url_hash
        {wclause}
        ORDER BY s.fetched_at
    """
    n = 0
    batch = []
    for r in src.execute(q, params):
        body = r["body"] or ""
        batch.append((r["url_hash"], r["source"] or "", r["fetched_at"] or "",
                      r["published_at"] or "", 1 if len(body) > 200 else 0,
                      r["title"] or "", r["summary"] or "", body))
        if len(batch) >= 2000:
            fts.executemany("INSERT INTO news_fts(url_hash,source,fetched_at,published_at,has_body,title,summary,body) VALUES (?,?,?,?,?,?,?,?)", batch)
            n += len(batch); batch = []
            print(f"  ...{n} 색인", file=sys.stderr)
    if batch:
        fts.executemany("INSERT INTO news_fts(url_hash,source,fetched_at,published_at,has_body,title,summary,body) VALUES (?,?,?,?,?,?,?,?)", batch)
        n += len(batch)
    fts.commit()
    total = fts.execute("SELECT COUNT(*) FROM news_fts").fetchone()[0]
    mode = "증분 추가" if watermark else "전체 색인"
    print(f"{mode} 완료: +{n}건 (총 {total}건)  → {(FTS_DB_KR if kr else FTS_DB).name}")
    src.close(); fts.close()


def _load_syn(kr: bool = False) -> dict:
    f = SYN_FILE_KR if kr else SYN_FILE
    if f.exists():
        try:
            return json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def _expand(term: str, syn: dict) -> str:
    """term → FTS 그룹 ('term' OR 'syn1' OR ...). 동의어 사전의 키/값 어느 쪽이든 그룹 채택."""
    low = term.lower()
    group = {term}
    for canon, alts in syn.items():
        pool = {canon.lower()} | {a.lower() for a in alts}
        if low in pool:
            group = {canon} | set(alts)
            break
    # 모든 항을 "phrase"로 감쌈(하이픈·특수문자 파싱 오류 방지). OR로 묶음.
    parts = [f'"{t}"' for t in sorted(group)]
    return "(" + " OR ".join(parts) + ")"


def query_fts(terms, days, scope, mode, use_syn, show_snip, limit,
              show_full=False, kr=False, count_only=False) -> dict:
    """순수 로컬 DB 검색 — 출력 안 하고 구조화 dict 반환. 서버 API 와 CLI 가 공유하는
    단일 원본 쿼리(P1). {"match","scope","days","mode","use_syn","count","limit","rows":[…]}
    또는 count_only 면 {"count":N}. 색인 없으면 {"error":…}."""
    fts = _connect_fts(kr)
    if not fts.execute("SELECT name FROM sqlite_master WHERE name='news_fts'").fetchone():
        fts.close()
        return {"error": f"색인 없음 — 먼저 `fts build{' --kr' if kr else ''}` 실행."}
    syn = _load_syn(kr) if use_syn else {}
    groups = [_expand(t, syn) for t in terms]
    match = (" AND " if mode == "and" else " OR ").join(groups)

    where = ["news_fts MATCH ?"]; params: list = [match]
    if scope == "foreign":
        where.append("source IN (" + ",".join("?" * len(FOREIGN_SOURCES)) + ")"); params += FOREIGN_SOURCES
    elif scope == "domestic":
        where.append("source NOT IN (" + ",".join("?" * len(FOREIGN_SOURCES)) + ")"); params += FOREIGN_SOURCES
    if days is not None:
        params.append((datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d"))
        where.append("fetched_at >= ?")

    if count_only:   # 카운트 숫자만 (테마 velocity 비교용)
        cnt = fts.execute(f"SELECT COUNT(*) FROM news_fts WHERE {' AND '.join(where)}", params).fetchone()[0]
        fts.close()
        return {"count": cnt}
    snip = "snippet(news_fts, 7, '《', '》', ' … ', 12) AS snip" if show_snip else "'' AS snip"
    bodycol = ", body" if show_full else ""
    sql = f"""SELECT url_hash, source, COALESCE(NULLIF(published_at,''),fetched_at) d, has_body, title, {snip}{bodycol}
              FROM news_fts WHERE {' AND '.join(where)} ORDER BY bm25(news_fts) LIMIT ?"""
    params.append(limit)
    rows = fts.execute(sql, params).fetchall()
    cnt = fts.execute(f"SELECT COUNT(*) FROM news_fts WHERE {' AND '.join(where)}", params[:-1]).fetchone()[0]
    fts.close()
    return {"match": match, "scope": scope, "days": days, "mode": mode, "use_syn": use_syn,
            "count": cnt, "limit": limit, "show_snip": show_snip, "show_full": show_full,
            "rows": [dict(r) for r in rows]}


def _print_fts(data: dict, show_snip: bool, show_full: bool) -> None:
    """query_fts / API 결과 dict 를 사람이 읽는 형식으로 출력 (로컬·원격 동일 렌더)."""
    if data.get("error"):
        print(data["error"], file=sys.stderr); return
    scope, days, mode = data["scope"], data.get("days"), data["mode"]
    sc = {"all": "국내+해외", "foreign": "해외만", "domestic": "국내만"}[scope]
    rng = f"최근 {days}일" if days else "전체기간"
    src = " ·via API" if NEWS_API_BASE else ""
    print(f"🔎 FTS [{rng}/{sc}/{mode.upper()}{'/syn' if data.get('use_syn') else ''}{src}] MATCH: {data['match']}")
    print(f"   매칭 {data['count']}건 (BM25 관련도순 상위 {min(data['limit'], data['count'])})")
    print("=" * 100)
    for r in data["rows"]:
        bf = "본문" if r.get("has_body") else "제목만"
        print(f"  {(r.get('d') or '')[:10]} [{r.get('source',''):>13}] [{bf}] {r.get('title','')}")
        if show_snip and r.get("snip"):
            print(f"        … {r['snip']}")
        if show_full and r.get("has_body"):   # 중요한 것 깊이 — 풀본문
            print("        " + "─" * 80)
            for line in (r.get("body") or "").strip().splitlines():
                if line.strip():
                    print(f"        | {line.strip()}")
            print("        " + "─" * 80)


def search(terms, days, scope, mode, use_syn, show_snip, limit,
           show_full=False, kr=False, count_only=False) -> None:
    """CLI 진입 — DEGAJA_NEWS_API 있으면 서버에서, 없으면 로컬 DB 에서 검색해 동일 형식 출력."""
    utf8_stdout()
    if NEWS_API_BASE:
        from ._api_client import fts_search as _remote
        data = _remote(NEWS_API_BASE, terms=terms, days=days, scope=scope, mode=mode,
                       use_syn=use_syn, show_snip=show_snip, limit=limit,
                       show_full=show_full, kr=kr, count_only=count_only)
    else:
        data = query_fts(terms, days, scope, mode, use_syn, show_snip, limit,
                         show_full=show_full, kr=kr, count_only=count_only)
    if count_only:
        print(data.get("count", data.get("error", 0)) if not data.get("error") else 0)
        if data.get("error"):
            print(data["error"], file=sys.stderr)
        return
    _print_fts(data, show_snip, show_full)


def cli_register(sub) -> None:
    p = sub.add_parser("fts", help="FTS5 전문검색 (본문+BM25). build/update/search")
    fsub = p.add_subparsers(dest="fts_cmd", required=True)
    pb = fsub.add_parser("build", help="최초 1회 전체 색인")
    pb.add_argument("--rebuild", action="store_true", help="기존 색인 드롭 후 재색인")
    pb.add_argument("--kr", action="store_true", help="KR 색인(trigram, 국내소스)")
    pb.set_defaults(func=lambda a: build(rebuild=a.rebuild, kr=a.kr))
    pu = fsub.add_parser("update", help="새 기사만 증분 추가 (매일/수집 후, 안전)")
    pu.add_argument("--kr", action="store_true")
    pu.set_defaults(func=lambda a: build(rebuild=False, kr=a.kr))
    s = fsub.add_parser("search")
    s.add_argument("terms", nargs="+")
    s.add_argument("--days", type=int, default=None)
    s.add_argument("--scope", choices=["all", "foreign", "domestic"], default="all")
    s.add_argument("--mode", choices=["and", "or"], default="and")
    s.add_argument("--syn", action="store_true", help="동의어 확장(news_synonyms[_kr].json)")
    s.add_argument("--snippet", action="store_true", help="매칭 본문 발췌 표시")
    s.add_argument("--full", action="store_true", help="상위 결과 풀본문 출력")
    s.add_argument("--kr", action="store_true", help="KR 색인(trigram) 검색")
    s.add_argument("--count", action="store_true", help="매칭 카운트 숫자만")
    s.add_argument("--limit", type=int, default=40)
    s.set_defaults(func=lambda a: search(
        a.terms, a.days, a.scope, a.mode, a.syn, a.snippet, a.limit,
        a.full, a.kr, a.count))
