# -*- coding: utf-8 -*-
"""리포트 .md 한 개 → 태그 추출 (결정론). tickers · sectors · verdicts · themes · date.

판단 없이 표면 신호만 뽑는다(P4: 태그는 데이터, 해석은 상위 몫). 티커는 유니버스로
검증해 오탐(일반 대문자어)을 거른다. 테마는 헤더/볼드 문구에서.
"""
from __future__ import annotations

import re
import string
from collections import Counter

from ._config import KNOWN_SECTORS, VERDICT_TAGS

# 모호 티커 필터는 chain_hop 이 이미 튜닝한 집합을 재사용(P1 재사용) + 단일문자 전부.
try:
    from module_news_data._chain_hop import AMBIGUOUS_TICKERS as _CHAIN_AMBIG
except Exception:
    _CHAIN_AMBIG = set()

_KR_CODE = re.compile(r"\b(\d{6})\b")
_US_TOKEN = re.compile(r"\b([A-Z]{1,5})\b")
_HEADER = re.compile(r"^#{1,3}\s+(.+)$", re.M)
_BOLD = re.compile(r"\*\*(.+?)\*\*")
_DATE = re.compile(r"\b(20\d{2}-\d{2}-\d{2})\b")
_SECTOR_HINT = re.compile(r"\b(" + "|".join(sorted(KNOWN_SECTORS, key=len, reverse=True)) + r")\b")

# 티커로 오탐되기 쉬운 일반 대문자어 — 유니버스에 있어도 제외.
# 단일문자(A·C·D·F·O·V…) 전부 + chain_hop 모호셋 + 리포트 상투 약어.
_US_STOP = set(string.ascii_uppercase) | _CHAIN_AMBIG | {
    "THE", "AND", "FOR", "USD", "CEO", "CFO", "GDP", "CPI", "AI", "US", "EPS",
    "PER", "PEG", "ROE", "ROIC", "OBV", "RSI", "YTD", "YOY", "QOQ", "FY", "DTC",
    "LIVE", "GO", "REAL", "NEW", "KR", "II", "III", "IV", "OW", "UW", "RR", "TP",
}


def extract_tags(text: str, us_tickers: dict[str, str], kr_names: dict[str, str]) -> dict:
    """리포트 본문 → 태그 dict. 빈도 상위만 남겨 노이즈 억제."""
    # ── 티커(KR 6자리, 유니버스 검증) ──────────────────────────────────────
    kr_hits = Counter(c for c in _KR_CODE.findall(text) if c in kr_names)
    # ── 티커(US 대문자, 유니버스 멤버십 검증) ───────────────────────────────
    us_hits = Counter()
    for tk in _US_TOKEN.findall(text):
        if tk in _US_STOP:
            continue
        if tk in us_tickers:
            us_hits[tk] += 1
    # 볼드/표 강조는 가중(제목에 불린 종목이 진짜 주제).
    for m in _BOLD.findall(text):
        for tk in _US_TOKEN.findall(m):
            if tk in us_tickers and tk not in _US_STOP:
                us_hits[tk] += 2
        for c in _KR_CODE.findall(m):
            if c in kr_names:
                kr_hits[c] += 2

    # ── 섹터 ───────────────────────────────────────────────────────────────
    sectors = sorted({m.upper() for m in _SECTOR_HINT.findall(text)})

    # ── 평결/상태 ──────────────────────────────────────────────────────────
    verdicts = sorted({v for v in VERDICT_TAGS if v in text})

    # ── 테마(헤더 문구 — 노이즈 컷: 3자+ , 표/구분선 제외) ──────────────────
    themes = []
    for h in _HEADER.findall(text):
        h = re.sub(r"[#*`]", "", h).strip()
        if 3 <= len(h) <= 80 and not h.startswith(("§", "|", "---")):
            themes.append(h)

    # ── 날짜 ───────────────────────────────────────────────────────────────
    dates = sorted(set(_DATE.findall(text)))

    return {
        "kr_tickers": [{"code": c, "name": kr_names[c], "hits": n} for c, n in kr_hits.most_common(15)],
        "us_tickers": [{"ticker": t, "name": us_tickers[t], "hits": n} for t, n in us_hits.most_common(15)],
        "sectors": sectors,
        "verdicts": verdicts,
        "themes": themes[:12],
        "dates": dates[-3:],   # 리포트 내 최신 날짜 몇 개
    }
