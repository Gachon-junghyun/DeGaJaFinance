# -*- coding: utf-8 -*-
"""module_news_data 설정 — 경로·소스집합의 **단일 원본** (CLAUDE.md P1).

옛 mvp 리포에서 FOREIGN_SOURCES 가 4개 파일에, DB 경로가 스크립트마다 복붙돼
있었다. 여기 한 곳에만 정의하고 모든 기능 파일이 import 한다.

뉴스 DB는 옛 리포가 라이브 소유(매시 cron 수집) — 이 모듈은 읽기 전용 소비층.
경로는 DEGAJA_MVP_ROOT 환경변수로 옮길 수 있다(기본: OneDrive mvp 리포).
"""
from __future__ import annotations

import os
import re
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

# ── 자유 텍스트에서 **티커를 탐지하는** 소비자용 상한 (단일 원본) ─────────────
# ⚠ 숫자 스윕(`sector_flow`·스크리너·IC)은 유니버스 **전체**를 쓴다. 여기서 자르는 것은
#   **기사·리포트 본문에서 대문자 토큰을 티커로 판정하는** 경로뿐이다.
# 왜: 유니버스를 S&P 1500 으로 넓히면 4자 이하 티커가 **1,201개** 늘고, 그중 **최소 26개가
#   일반 영어 단어와 철자가 같다** — CASH · FORM · POST · TECH · UNIT · WAY · PLUS · RUN ·
#   ROAD · ROCK · SAFE · STEP · PATH · POOL … (2026-08-10 실측. 손으로 센 값이라 **하한**).
#   이 단어들은 금융 기사에 매 문단 나오므로 **유니버스 확장 = 오탐 폭증**이 된다.
#   기존 방어(`_chain_hop.AMBIGUOUS_TICKERS` + `len(tk) < 3`)는 하드코딩 ~50개라 못 막는다.
# 기본 300 = **확장 이전 `us_top300` 과 동일한 동작**(회귀 0). 낮추는 것은 사람의 명시적 결정.
US_TEXT_TOP_N = 300


def us_text_universe_rows() -> list[dict]:
    """티커 탐지용 US 유니버스 — 시총 상위 `US_TEXT_TOP_N`. 파일이 커져도 동작이 고정된다.

    `market_cap_usd` 열이 없으면 자르지 않고 원본 순서를 그대로 쓴다(옛 스키마 하위호환).
    """
    import csv as _csv

    if not UNIVERSE_CSV.exists():
        return []
    with open(UNIVERSE_CSV, encoding="utf-8-sig") as f:
        rows = list(_csv.DictReader(f))
    if rows and "market_cap_usd" in rows[0]:
        def _cap(r):
            try:
                return float(r.get("market_cap_usd") or 0)
            except (TypeError, ValueError):
                return 0.0
        rows.sort(key=_cap, reverse=True)
    return rows[:US_TEXT_TOP_N] if US_TEXT_TOP_N else rows

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

# ── '뉴스가 아닌 것' 판정 — 분모 정정의 단일 원본(P1) ─────────────────────
# 왜 필요한가(실측 2026-07-23 국내 1,821건): 사건 클러스터가 못 묶어 '1매체 단독'으로
# 남는 638건 중 **140건(21.9%)이 애초에 뉴스가 아니었다** — 같은 기사의 일본어 번역판
# 61 · 포토캡션 59 · 부동산 실거래 자동기사 20. 이걸 분모에 넣어두면 "오늘 기사의 46%를
# 못 봤다"가 실제보다 나쁘게 나오고, 동시에 진짜 사각(매크로 단독기사)이 잡동사니에 묻힌다.
# ⚠ **자르는 게 아니라 분류해서 센다.** 호출부는 개수를 산출물에 실어야 한다(P4) —
#    "안 봤다"와 "볼 게 없었다"는 다른 말이고, 그 차이는 숫자로만 증명된다.
_JP_EDITION = re.compile(r"/jp/", re.I)      # chosun 일본어판 = 한국어 기사의 번역 중복
_PHOTO_LEAD = re.compile(r"^\s*\[(포토|사진|화보|한번에쓱)")
_REALESTATE_BOT = re.compile(r"\d+\s*㎡.{0,40}(거래|원에)")


# 비시장 경계밴드 — 분류기가 '비시장'으로 본 사건 중 **이 점수 위는 전부 보여준다**.
# 여기(설정)에 두는 이유: `_brief`(하루)와 `_thread`(주간)가 **같은 규칙**을 써야 하는데
# 둘은 같은 층의 형제라 한쪽이 다른 쪽을 import 하면 옆으로 가는 의존이 된다(pipeline
# README 의 "calls go one way"). 공용 상수는 아래층에 둔다 = P1 + 층 규칙 동시 충족.
# 왜 개수 컷이 아니라 점수 밴드인가는 `_brief.NONMARKET_BAND` 의 ⚠ 참조(실측 근거).
NONMARKET_BAND = -3.0


def noise_class(title: str | None, url: str | None = None) -> str | None:
    """이 기사는 '사건'의 재료가 되나. 아니면 왜 아닌지 라벨을, 맞으면 None 을 준다.

    ⚠ 판정 근거를 URL 에 두는 게 제목보다 튼튼하다 — 실측으로 chosun `/jp/` 경로 551건과
      일본어 제목 550건이 3건 차이로 일치했다. 일본어 '글자'로 거르면 일본을 인용한
      한국어 기사가 같이 날아간다.

    ⚠ **이 필터의 실측 비용**(2026-07-17·21·23 국내, 필터 유/무 클러스터를 구성기사 단위로 대조):
      구성기사가 전부 노이즈여서 **통째로 사라진 사건**이 하루 1~13개, 그중 **시장분류는 0·0·1개**.
      유일한 실측 손실은 「한병도 "수사·기소 분리…"」[2매체·nb 2.5] — 그 사건이 `[포토]` 캡션으로만
      존재했다. 하루 155~444건의 가구를 걷어내는 대가로 2매체짜리 한계 사건 0~1개를 잃는다.
      제목 기준으로 세면 훨씬 나쁘게 보이지만(60~126개) 그건 medoid 가 바뀐 것이지 소멸이 아니다
      — 「[포토] 코스피, 7000선 회복」이 「코스피 7000 재탈환…」으로 바뀌는 식(오히려 개선).
      ⚠ 이 비용은 **다시 잴 수 있어야 한다** — 필터를 건드리면 같은 대조를 다시 돌려라.
    """
    if url and _JP_EDITION.search(url):
        return "translation_dup"
    t = title or ""
    if _PHOTO_LEAD.match(t):
        return "photo"
    if _REALESTATE_BOT.search(t):
        return "realestate_bot"
    return None


def origin_tag(source: str | None) -> str:
    """소스 국적 태그. 해외=EN, 그 외=KR."""
    return "EN" if (source or "") in FOREIGN_SOURCES else "KR"


def utf8_stdout() -> None:
    """Windows cp949 콘솔에서 한글/기호 크래시 방지 (CLAUDE.md §5)."""
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
