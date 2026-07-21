# -*- coding: utf-8 -*-
"""module_news_data 설정 — 경로·소스집합의 **단일 원본** (CLAUDE.md P1).

옛 mvp 리포에서 FOREIGN_SOURCES 가 4개 파일에, DB 경로가 스크립트마다 복붙돼
있었다. 여기 한 곳에만 정의하고 모든 기능 파일이 import 한다.

뉴스 DB는 옛 리포가 라이브 소유(매시 cron 수집) — 이 모듈은 읽기 전용 소비층.
경로는 DEGAJA_MVP_ROOT 환경변수로 옮길 수 있다(기본: OneDrive mvp 리포).
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

# ── 리포 루트 ────────────────────────────────────────────────────────────
HERE = Path(__file__).resolve().parent          # module_news_data/
REPO_ROOT = HERE.parent                          # DeGaJaFinance/
DATA_DIR = Path(os.environ.get("DEGAJA_DATA_DIR", REPO_ROOT / "data"))

# ── 데이터 소스 (이 리포 소유 — 수집·색인·검색 전부 로컬) ─────────────────
NEWS_DB = DATA_DIR / "news_alert.db"             # seen_news + article_contents
FTS_DB = DATA_DIR / "news_fts.db"                # 영문: porter unicode61 (어형)
FTS_DB_KR = DATA_DIR / "news_fts_kr.db"          # 한글: trigram (3글자+ 토큰만 매칭)
SYN_FILE = DATA_DIR / "news_synonyms.json"
SYN_FILE_KR = DATA_DIR / "news_synonyms_kr.json"
UNIVERSE_CSV = DATA_DIR / "us_universe" / "us_top300.csv"
ALIASES_JSON = DATA_DIR / "us_universe" / "us_aliases.json"
KR_UNIVERSE_CSV = DATA_DIR / "kr_universe" / "kr_all.csv"   # rank,ticker,name,…,sector,market

# ── 이 리포 산출물 ────────────────────────────────────────────────────────
OUT_DIR = REPO_ROOT / "out"

# ── .env 주입 (module_disclosure·module_KIS 와 동일 패턴, stdlib 전용) ─────
# 뉴스 API 설정(DEGAJA_NEWS_API·..._AUTH)을 setx(OS 환경변수) 없이도 프로젝트
# 루트 `.env` 한 곳에 적어두면 되도록. OS 환경변수가 이미 있으면 그쪽이 이긴다
# (`k not in os.environ`). 서버 PC 는 .env 의 DEGAJA_NEWS_API 를 비워두므로 무해.
# P6: 서버도 이 모듈을 import 하지만 stdlib(os·pathlib)만 써서 기동에 안전.
def _maybe_load_dotenv() -> None:
    for p in (REPO_ROOT / ".env", REPO_ROOT.parent / ".env"):
        if not p.exists():
            continue
        try:
            for line in p.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                k, _, v = line.partition("=")
                k = k.strip()
                v = v.strip().strip('"').strip("'")
                if k and v and k not in os.environ:
                    os.environ[k] = v
        except Exception:
            pass
        break


_maybe_load_dotenv()

# ── 뉴스 API (서버 PC 수집기 → 클라이언트 검색) ───────────────────────────
# 서버 PC가 Server/news_api.py 로 뉴스 DB 를 HTTP 로 노출한다. 클라이언트에서
# 이 환경변수만 켜면 `fts search` 가 로컬 DB 대신 그 API 로 검색을 끌어온다
# (명령어 동일 — Claude Code 는 로컬/원격 구분 없이 같은 CLI 를 쓴다).
#   예) DEGAJA_NEWS_API="http://192.168.0.50:8787"  를 .env 에 (또는 setx 로 OS 환경변수)
# 비어 있으면 로컬 DB 직접 읽기(단일 PC 모드). 서버 PC 자신은 이 값을 비운다.
NEWS_API_BASE = (os.environ.get("DEGAJA_NEWS_API", "") or "").rstrip("/") or None
NEWS_API_PORT = int(os.environ.get("DEGAJA_NEWS_API_PORT", "8787"))

# ── 해외(영문) 소스 집합 — scope=foreign/domestic 분류의 단일 원본 ────────
# 새 해외 소스 추가 시 여기만. (2026-07-19 해외 대량 확장 — _rss_feeds.py 참조)
FOREIGN_SOURCES = sorted({
    "bloomberg", "google_en", "bbc", "scmp", "marketwatch", "upi", "nyt",
    "seekingalpha", "yahoo_finance", "prnewswire", "cnbc", "thediplomat",
    "sec_edgar", "foreignpolicy", "investing_en", "google_news_en", "fxstreet",
    # ⚠ 여기는 _rss_feeds.RSS_FEEDS 와 **짝**이다 — 해외 피드를 넣고 여기 빠뜨리면
    #   그 소스가 KR 로 태깅돼 국내 스코프로 새고, 한국어 학습 분류기가 영문을
    #   시장/비시장 판정하게 된다.
    # US 마켓/종합
    "wsj", "fortune", "forbes", "businessinsider", "thestreet", "benzinga",
    "zerohedge", "fool", "axios", "semafor", "nasdaq", "globenewswire",
    # 영국/유럽
    "ft", "economist", "guardian", "skynews", "independent", "dw", "france24",
    "euronews", "politico",
    # 아시아/월드
    "nikkei", "japantimes", "aljazeera", "cna", "straitstimes", "toi",
    "economictimes", "digitimes",
    # 중앙은행/공식
    "federalreserve", "ecb", "boe",
    # 원자재/크립토/물류
    "oilprice", "mining", "coindesk", "cointelegraph", "cryptoslate",
    "hellenicshipping", "eia",
    # 테크
    "techcrunch", "theverge", "arstechnica", "venturebeat", "tomshardware",
    "eetimes", "theregister", "wired", "mittr",
})

BODY_MIN = 200   # 본문 '있음' 판정 최소 글자수 (coverage/fts has_body 공통)


def origin_tag(source: str | None) -> str:
    """소스 국적 태그. 해외=EN, 그 외=KR."""
    return "EN" if (source or "") in FOREIGN_SOURCES else "KR"


def utf8_stdout() -> None:
    """Windows cp949 콘솔에서 한글/기호 크래시 방지 (CLAUDE.md §5)."""
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
