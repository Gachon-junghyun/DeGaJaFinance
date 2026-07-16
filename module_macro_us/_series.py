"""FRED series 카탈로그.

12개 시리즈를 dict로 박제. fetch / render 모듈에서 import.
각 시리즈: FRED series_id, 한국어/영어 라벨, 단위, 빈도(daily/monthly).
"""
from __future__ import annotations

from typing import Literal, TypedDict


class SeriesSpec(TypedDict):
    fred_id: str
    label_ko: str
    label_en: str
    unit: str
    freq: Literal["daily", "monthly"]


SERIES_CATALOG: dict[str, SeriesSpec] = {
    "us_10y": {
        "fred_id": "DGS10",
        "label_ko": "10년 국채 yield",
        "label_en": "10y Treasury Yield",
        "unit": "%",
        "freq": "daily",
    },
    "us_2y": {
        "fred_id": "DGS2",
        "label_ko": "2년 국채 yield",
        "label_en": "2y Treasury Yield",
        "unit": "%",
        "freq": "daily",
    },
    "us_30y": {
        "fred_id": "DGS30",
        "label_ko": "30년 국채 yield",
        "label_en": "30y Treasury Yield",
        "unit": "%",
        "freq": "daily",
    },
    "us_5y": {
        "fred_id": "DGS5",
        "label_ko": "5년 국채 yield",
        "label_en": "5y Treasury Yield",
        "unit": "%",
        "freq": "daily",
    },
    "fed_funds": {
        "fred_id": "DFF",
        "label_ko": "Fed Funds 유효금리",
        "label_en": "Fed Funds Effective Rate",
        "unit": "%",
        "freq": "daily",
    },
    "cpi": {
        "fred_id": "CPIAUCSL",
        "label_ko": "CPI (모든 도시소비자)",
        "label_en": "CPI All Urban Consumers",
        "unit": "index",
        "freq": "monthly",
    },
    "core_cpi": {
        "fred_id": "CPILFESL",
        "label_ko": "Core CPI",
        "label_en": "Core CPI",
        "unit": "index",
        "freq": "monthly",
    },
    "unemployment": {
        "fred_id": "UNRATE",
        "label_ko": "실업률",
        "label_en": "Unemployment Rate",
        "unit": "%",
        "freq": "monthly",
    },
    "vix": {
        "fred_id": "VIXCLS",
        "label_ko": "VIX (변동성지수)",
        "label_en": "VIX Volatility Index",
        "unit": "index",
        "freq": "daily",
    },
    "dxy": {
        "fred_id": "DTWEXBGS",
        "label_ko": "Broad 달러 인덱스",
        "label_en": "Broad Dollar Index",
        "unit": "index",
        "freq": "daily",
    },
    "real_10y": {
        "fred_id": "DFII10",
        "label_ko": "10년 TIPS 실질금리",
        "label_en": "10y TIPS Real Yield",
        "unit": "%",
        "freq": "daily",
    },
    "m2": {
        "fred_id": "M2SL",
        "label_ko": "M2 통화량",
        "label_en": "M2 Money Stock",
        "unit": "$ billions",
        "freq": "monthly",
    },
}

DEFAULT_KEYS: list[str] = list(SERIES_CATALOG.keys())


def resolve_keys(selected: str | None) -> list[str]:
    """`--series` CLI 인자(쉼표 구분)를 카탈로그 키 리스트로 변환.

    None / 빈 문자열이면 전체 12종.
    알 수 없는 키는 SystemExit.
    """
    if not selected:
        return list(DEFAULT_KEYS)
    keys = [s.strip() for s in selected.split(",") if s.strip()]
    unknown = [k for k in keys if k not in SERIES_CATALOG]
    if unknown:
        raise SystemExit(
            f"Unknown series key(s): {unknown}. "
            f"Valid keys: {list(SERIES_CATALOG.keys())}"
        )
    return keys
