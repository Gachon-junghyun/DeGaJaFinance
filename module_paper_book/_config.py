# -*- coding: utf-8 -*-
"""module_paper_book._config — 경로·기본값·공통 헬퍼 (단일 원본, P1).

모의투자 장부의 DB 위치·기본 자본·리스크 파라미터를 한 곳에서 정의한다. 다른 _파일은
여기서 import 해서 쓴다(복제 금지). utf8_stdout 은 Windows cp949 콘솔 크래시 방지용.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

# 리포 루트 = 이 파일의 부모의 부모 (module_paper_book/ 의 상위)
REPO_ROOT = Path(__file__).resolve().parent.parent

# 데이터 디렉토리(다른 모듈과 동일 규약): DEGAJA_DATA_DIR 우선, 없으면 리포 data/
DATA_DIR = Path(os.environ.get("DEGAJA_DATA_DIR", REPO_ROOT / "data"))

# 장부 DB — PAPER_BOOK_DB_PATH 환경변수 우선(watchlist 규약과 동형)
DB_FILENAME = "paper_book.db"


def default_db_path() -> Path:
    env = os.environ.get("PAPER_BOOK_DB_PATH")
    return Path(env) if env else (DATA_DIR / DB_FILENAME)


# 산출물 루트(리포트/저널). 산업데스크와 동일하게 llm_outputs/{date}/paper_desk/
def out_dir(date: str) -> Path:
    return REPO_ROOT / "llm_outputs" / date / "paper_desk"


# ── 기본 자본·리스크 모델 (action_bracket.py 와 동형의 리스크 규약) ──────────────
DEFAULT_CAPITAL_KRW = 10_000_000.0   # 초기 원화 슬리브
DEFAULT_CAPITAL_USD = 0.0            # 초기 달러 슬리브(원하면 init 에서 지정)
DEFAULT_FX_USDKRW = 1380.0          # 총자산 원화환산용 기본 환율(cycle_exposure 관행)

# 리스크 파라미터(1트레이드 위험·코어 위험·스탑·최대비중) — 사람이 CLI 로 덮어씀
RISK_PCT = 1.5          # 일반 베팅 1트레이드당 자본대비 위험 %
CORE_RISK_PCT = 0.8     # tape-independent 코어 스타터 위험 %
STOP_PCT = 7.0          # 스탑 미지정 시 기본 하드스탑 %
MAX_POS_PCT = 25.0      # 단일 종목 최대 비중 %
MAX_THEME_PCT = 40.0    # 단일 테마/상관단위 최대 비중 % (premortem 'one risk unit' 가드)


def utf8_stdout() -> None:
    """Windows cp949 콘솔에서 이모지/한글 출력 크래시 방지."""
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except Exception:
        pass


def is_kr_ticker(ticker: str) -> bool:
    """6자리 숫자 = KR 종목코드, 그 외 = US 티커 (P3 시장 자동감지)."""
    t = ticker.strip().upper()
    return len(t) == 6 and t.isdigit()


def market_of(ticker: str) -> str:
    return "KR" if is_kr_ticker(ticker) else "US"


def ccy_of(ticker: str) -> str:
    return "KRW" if is_kr_ticker(ticker) else "USD"
