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
    _timeaxis   published_at → UTC 정규화 (시계열 비닝의 축 — 수집시각 아님)
    _tokenize   텍스트 → 단어 집합 (한글 조사절단 + 영문; 형태소분석기 0)
    _universe   상장사 언급 판정 (뉴스풀 62%가 종합지 — '시장 얘기냐'를 가리는 축)
    _burst      그날 평소보다 튄 단어 + 근거 (고정 검색어·STOP 리스트 없이)
    _export     제목 벌크 반출(증분) — 서버(수집)→클라이언트(GPU 임베딩) 동기화 통로
    _embed      제목 → 문장벡터 (ko-sroberta·GPU, **클라 전용**) — 사건 클러스터의 재료
    _cluster    하루 기사 → **사건**(중복 압축·매체수 랭킹, k 없음, **클라 전용**)
                + 큰 사건이 삼킨 `subevents` · 자격미달 `singles` · `excluded_noise`(분모 정정)
    _classify   제목 → 시장/비시장 (NB·의존성0·URL 섹션 라벨 자가학습·근거어 감사)
    _brief      하루 → **계층 브리핑**(머리/몸통/꼬리/1매체/비시장경계+분모) — LLM 이 먹을 크기로
                ⚠ 회수율은 실측 대상이다(`scripts/brief_recall.py`) — 54.4%→64.6%(2026-07-23)

빠른 사용:
    from module_news_data import search, fts_search, theme_analyze

CLI:
    python -m module_news_data <search|fts|coverage|blindspot|theme-age|chain-hop> ...
"""
from ._blindspot import emergent_terms
from ._blindspot import run as blindspot_run
from ._brief import build as brief_build
from ._burst import analyze as burst_analyze
from ._burst import run as burst_run
from ._chain_hop import load_universe
from ._chain_hop import run as chain_hop_run
from ._classify import evaluate as classify_evaluate
from ._classify import section_of
from ._classify import train as classify_train
from ._cluster import cluster_day
from ._config import DATA_DIR, FOREIGN_SOURCES, FTS_DB, FTS_DB_KR, NEWS_DB, origin_tag
from ._coverage import run as coverage_run
from ._embed import load_vectors
from ._embed import status as embed_status
from ._embed import sync as embed_sync
from ._export import pull as export_pull
from ._export import run as export_run
from ._fetch import fetch_and_store, run_once
from ._fts import build as fts_build
from ._fts import search as fts_search
from ._rss_feeds import RSS_FEEDS, fetch_news
from ._search import search
from ._theme_age import analyze as theme_analyze
from ._theme_age import daily_counts as theme_daily_counts
from ._timeaxis import PUBLISHED_AT_SINCE, market_day, parse_published, utc_day, utc_hour
from ._tokenize import tokens
from ._universe import kr_names, mentions_listed, universe_size

__all__ = [
    # 설정 (단일 원본)
    "DATA_DIR", "NEWS_DB", "FTS_DB", "FTS_DB_KR", "FOREIGN_SOURCES", "origin_tag",
    # 시간축 (단일 원본)
    "parse_published", "market_day", "utc_day", "utc_hour", "PUBLISHED_AT_SINCE",
    # 수집
    "RSS_FEEDS", "fetch_news", "fetch_and_store", "run_once",
    # 검색
    "search", "fts_build", "fts_search",
    # 토큰화 (단일 원본)
    "tokens",
    # 유니버스 언급 판정
    "mentions_listed", "kr_names", "universe_size",
    # 분석
    "coverage_run", "blindspot_run", "emergent_terms",
    "theme_analyze", "theme_daily_counts",
    "burst_run", "burst_analyze",
    "chain_hop_run", "load_universe",
    # 동기화·임베딩 (embed 는 클라 전용 — 서버는 torch 없음)
    "export_run", "export_pull",
    "embed_sync", "embed_status", "load_vectors",
    # 사건·브리핑 (클라 전용)
    "cluster_day", "brief_build",
    # 분류 (의존성 0 — 서버에서도 돈다)
    "classify_train", "classify_evaluate", "section_of",
]
