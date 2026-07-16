# -*- coding: utf-8 -*-
"""module_report_tags 설정 — REPORT 폴더·인수인계 원장 경로 + 티커 유니버스.

REPORT_DIR = 데스크 산출물(.md)이 쌓이는 폴더. 여기서 태그를 추출해 인수인계
원장(HANDOFF.md + _tags.json)을 증분 갱신한다. 다운스트림은 매번 재검색하지 않고
이 원장을 읽는다. 티커 검증은 로컬 유니버스 CSV 재사용(module_news_data 와 동일 소스).
"""
from __future__ import annotations

import csv
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent
DATA_DIR = Path(os.environ.get("DEGAJA_DATA_DIR", REPO_ROOT / "data"))

# 데스크 산출물 폴더 — 기본 REPORT/, 환경변수로 llm_outputs 등으로 바꿔 스캔 가능.
REPORT_DIR = Path(os.environ.get("DEGAJA_REPORT_DIR", REPO_ROOT / "REPORT"))
HANDOFF_MD = REPORT_DIR / "HANDOFF.md"        # 사람이 읽는 인수인계 원장
TAGS_JSON = REPORT_DIR / "_tags.json"          # 기계 인덱스(증분 상태 + 역인덱스)

US_UNIVERSE = DATA_DIR / "us_universe" / "us_top300.csv"
KR_UNIVERSE = DATA_DIR / "kr_universe" / "kr_all.csv"

# 섹터 약어(SECTOR_DEEP_* 파일명·헤더에서 실측) — 태그 정규화용.
KNOWN_SECTORS = {
    "COMM", "DEF", "DISC", "ENRG", "ENER", "FIN", "HLTH", "HEALTH", "INDU",
    "IT", "MATR", "MAT", "ROBO", "ROBOT", "STPL", "UTIL", "SEMI", "SHIP", "TECH",
}

# 평결/상태 태그 — 데스크 공통 어휘(실측).
VERDICT_TAGS = {
    "LIVE", "PARTIAL", "RESOLVED", "REAL", "INFLATED", "BROKEN",
    "REAL-but-PRICED", "CONFIRMED", "FRESH", "ECHO", "FADING",
    "GO", "WAIT", "STAND DOWN", "🟢", "🟡", "🔴",
}


def load_us_tickers() -> dict[str, str]:
    """ticker -> name (us_top300). 대문자 토큰 티커 검증에 사용."""
    out: dict[str, str] = {}
    if US_UNIVERSE.exists():
        with open(US_UNIVERSE, encoding="utf-8-sig") as f:
            for row in csv.DictReader(f):
                tk = (row.get("ticker") or "").strip().upper()
                if tk:
                    out[tk] = (row.get("name") or "").strip()
    return out


def load_kr_names() -> dict[str, str]:
    """6자리코드 -> 종목명 (kr_all). 코드↔이름 양방향 태깅에 사용."""
    out: dict[str, str] = {}
    if KR_UNIVERSE.exists():
        with open(KR_UNIVERSE, encoding="utf-8-sig") as f:
            for row in csv.DictReader(f):
                tk = (row.get("ticker") or "").strip()
                code = tk.split(".")[0]
                if code.isdigit() and len(code) == 6:
                    out[code] = (row.get("name") or "").strip()
    return out
