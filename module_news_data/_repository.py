# -*- coding: utf-8 -*-
"""news_alert.db 저장소 — seen_news(중복이력) + article_contents(본문).

옛 pipeline_bot/storage/news_repository.py 의 fetch 경로만 포팅. 텔레그램 봇의
users/keywords/sent_news·scenario 헬퍼는 은퇴(2026-06-22)라 제외 — 다만 init_db 의
스키마 CREATE 는 복사한 DB와 정확히 맞추려고 그대로 둔다(IF NOT EXISTS, 무해).
DB 경로는 _config.NEWS_DB 단일 원본.
"""
from __future__ import annotations

import hashlib
import sqlite3
from datetime import datetime
from typing import Dict, List, Optional

from ._config import NEWS_DB


def _get_conn(db_path: str | None = None) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path or str(NEWS_DB), timeout=30.0)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON")
    conn.execute("PRAGMA busy_timeout=30000")   # fetch↔검색 동시접근 시 30s 대기
    return conn


def _url_hash(url: str) -> str:
    return hashlib.md5(url.strip().encode("utf-8")).hexdigest()


def init_db(db_path: str | None = None) -> None:
    conn = _get_conn(db_path)
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS seen_news (
            url_hash     TEXT PRIMARY KEY,
            url          TEXT NOT NULL,
            title        TEXT,
            source       TEXT,
            fetched_at   TEXT,
            published_at TEXT,
            summary      TEXT
        );
        CREATE TABLE IF NOT EXISTS article_contents (
            url_hash    TEXT PRIMARY KEY,
            url         TEXT NOT NULL,
            body        TEXT,
            scraped_at  TEXT,
            status      TEXT DEFAULT 'ok'
        );
    """)
    conn.commit()
    for col, typedef in [("published_at", "TEXT"), ("summary", "TEXT")]:
        try:
            conn.execute(f"ALTER TABLE seen_news ADD COLUMN {col} {typedef}")
            conn.commit()
        except sqlite3.OperationalError:
            pass
    conn.close()


def filter_new_articles(articles: List[Dict], db_path: str | None = None) -> List[Dict]:
    """새 기사만 seen_news 에 INSERT 하고 그 목록을 반환(중복 제거)."""
    if not articles:
        return []
    conn = _get_conn(db_path)
    new_articles = []
    for art in articles:
        url = art.get("url", "")
        if not url:
            continue
        h = _url_hash(url)
        if conn.execute("SELECT 1 FROM seen_news WHERE url_hash = ?", (h,)).fetchone() is None:
            conn.execute(
                "INSERT OR IGNORE INTO seen_news "
                "(url_hash, url, title, source, fetched_at, published_at, summary) "
                "VALUES (?, ?, ?, ?, ?, ?, ?)",
                (h, url, art.get("title", ""), art.get("source", ""),
                 datetime.now().isoformat(), art.get("published", "") or "",
                 (art.get("summary", "") or "")[:300]),
            )
            new_articles.append(art)
    conn.commit()
    conn.close()
    return new_articles


def save_article_content(url: str, body: str, status: str = "ok", db_path: str | None = None) -> None:
    h = _url_hash(url)
    conn = _get_conn(db_path)
    conn.execute(
        "INSERT OR REPLACE INTO article_contents "
        "(url_hash, url, body, scraped_at, status) VALUES (?, ?, ?, ?, ?)",
        (h, url, body, datetime.now().isoformat(), status),
    )
    conn.commit()
    conn.close()


def get_scraped_urls(urls: set, db_path: str | None = None) -> set:
    """이미 본문(status='ok')이 있는 url 집합 — 재스크랩 skip 판정."""
    if not urls:
        return set()
    hashes = {_url_hash(u): u for u in urls}
    placeholders = ",".join("?" * len(hashes))
    conn = _get_conn(db_path)
    rows = conn.execute(
        f"SELECT url_hash FROM article_contents WHERE url_hash IN ({placeholders}) AND status = 'ok'",
        list(hashes.keys()),
    ).fetchall()
    conn.close()
    return {hashes[r["url_hash"]] for r in rows}


def get_unscraped_articles(keyword: Optional[str] = None, limit: int = 50,
                           db_path: str | None = None) -> List[Dict]:
    """본문이 없거나 error 인 기사 목록 — 수동 backfill 용."""
    conn = _get_conn(db_path)
    if keyword:
        rows = conn.execute(
            "SELECT s.url, s.title, s.source FROM seen_news s "
            "LEFT JOIN article_contents a ON s.url_hash = a.url_hash "
            "WHERE (a.url_hash IS NULL OR a.status = 'error') AND s.title LIKE ? "
            "ORDER BY s.fetched_at DESC LIMIT ?",
            (f"%{keyword}%", limit),
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT s.url, s.title, s.source FROM seen_news s "
            "LEFT JOIN article_contents a ON s.url_hash = a.url_hash "
            "WHERE a.url_hash IS NULL OR a.status = 'error' "
            "ORDER BY s.fetched_at DESC LIMIT ?",
            (limit,),
        ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_stats(db_path: str | None = None) -> Dict:
    conn = _get_conn(db_path)
    total_news = conn.execute("SELECT COUNT(*) FROM seen_news").fetchone()[0]
    with_body = conn.execute("SELECT COUNT(*) FROM article_contents WHERE status='ok'").fetchone()[0]
    conn.close()
    return {"total_news": total_news, "with_body": with_body}
