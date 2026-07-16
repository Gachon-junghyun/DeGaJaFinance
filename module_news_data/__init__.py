# -*- coding: utf-8 -*-
"""module_news_data — 뉴스 데이터 소비층 (읽기/검색/분석).

수집(fetch/scrape)은 옛 mvp 리포의 매시 cron 이 라이브 소유 — 이 모듈은 그
DB(news_alert.db / news_fts*.db)를 읽는 소비층이다 (CLAUDE.md §3, P5 라이브 보호).
경로는 DEGAJA_MVP_ROOT 환경변수로 이동 가능 (_config.py 단일 원본).

기능 지도 (기능 하나 = 파일 하나):
    _rss_feeds  RSS 수집 (국내/해외 피드 → 헤드라인+요약)
    _scraper    본문 스크랩 (source별 셀렉터)
    _repository news_alert.db 저장소 (seen_news + article_contents)
    _fetch      수집 오케스트레이션 (fetch→dedupe→scrape→FTS 증분) — bat 루프의 1틱
    _search     LIKE 키워드 검색 (title/summary/body)
    _fts        FTS5 전문검색 (BM25·동의어·snippet) + 색인 build/update
    _coverage   검색어 커버리지 % (분모 포함 3층 분해)
    _blindspot  못 본 풀 랜덤샘플 + 토큰0 신흥어
    _theme_age  테마 나이·가속 (FRESH/ECHO)
    _chain_hop  US 사슬-홉 (제목 미명명 + 본문 근접 공동언급)

빠른 사용:
    from module_news_data import search, fts_search, theme_analyze

CLI:
    python -m module_news_data <search|fts|coverage|blindspot|theme-age|chain-hop> ...
"""
from ._blindspot import emergent_terms
from ._blindspot import run as blindspot_run
from ._chain_hop import load_universe
from ._chain_hop import run as chain_hop_run
from ._config import DATA_DIR, FOREIGN_SOURCES, FTS_DB, FTS_DB_KR, NEWS_DB, origin_tag
from ._coverage import run as coverage_run
from ._fetch import fetch_and_store, run_once
from ._fts import build as fts_build
from ._fts import search as fts_search
from ._rss_feeds import RSS_FEEDS, fetch_news
from ._search import search
from ._theme_age import analyze as theme_analyze
from ._theme_age import daily_counts as theme_daily_counts

__all__ = [
    # 설정 (단일 원본)
    "DATA_DIR", "NEWS_DB", "FTS_DB", "FTS_DB_KR", "FOREIGN_SOURCES", "origin_tag",
    # 수집
    "RSS_FEEDS", "fetch_news", "fetch_and_store", "run_once",
    # 검색
    "search", "fts_build", "fts_search",
    # 분석
    "coverage_run", "blindspot_run", "emergent_terms",
    "theme_analyze", "theme_daily_counts",
    "chain_hop_run", "load_universe",
]
