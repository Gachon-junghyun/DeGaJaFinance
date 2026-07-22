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
    # weekly 는 2026-07-22 신용·유동성 축과 함께 추가. 소비처 규약:
    #   · lookback  — monthly 만 400일(yoy 계산용), 그 외는 200일 (weekly 포함, 충분)
    #   · yoy 표기  — monthly 전용 (weekly 는 52주 비교가 아니라 30d/90d 델타로 읽는다)
    #   · 신선도    — daily 는 최근 영업일, weekly 는 최대 7일, monthly 는 최대 ~1개월 지연.
    #                 P4 상 "지연을 밝히고 쓴다" 가 원칙이므로 렌더러가 freq 를 그대로 찍는다.
    freq: Literal["daily", "weekly", "monthly"]


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
    # ── 신용·유동성 축 (2026-07-22 추가) ────────────────────────────────
    # 왜: 기존 12개에 신용 스프레드가 하나도 없었다. 2026-07-21 US 데스크가
    # "credit surprise stack"(NY연준 신용신청률·학자금 디폴트·Dimon 발언)을 **서사로만**
    # 쌓았는데, 실측 HY OAS 는 2.69% = 역사적 초타이트(스트레스 0)였다.
    # 확인할 숫자가 없어서 서사가 그대로 통과했다 — P4 위반이 일어나는 지점.
    "hy_oas": {
        "fred_id": "BAMLH0A0HYM2",
        "label_ko": "하이일드 스프레드(OAS)",
        "label_en": "US High Yield OAS",
        "unit": "%",
        "freq": "daily",
    },
    "ig_oas": {
        "fred_id": "BAMLC0A0CM",
        "label_ko": "투자등급 스프레드(OAS)",
        "label_en": "US IG Corporate OAS",
        "unit": "%",
        "freq": "daily",
    },
    "breakeven_10y": {
        "fred_id": "T10YIE",
        "label_ko": "10년 기대인플레이션",
        "label_en": "10y Breakeven Inflation",
        "unit": "%",
        "freq": "daily",
    },
    "nfci": {
        "fred_id": "NFCI",
        "label_ko": "금융상황지수(시카고연준)",
        "label_en": "Chicago Fed NFCI",
        "unit": "index",
        "freq": "weekly",
    },
    "rrp": {
        "fred_id": "RRPONTSYD",
        "label_ko": "연준 역레포 잔고",
        "label_en": "Fed Overnight Reverse Repo",
        "unit": "$ billions",
        "freq": "daily",
    },
    "fed_assets": {
        "fred_id": "WALCL",
        "label_ko": "연준 총자산",
        "label_en": "Fed Total Assets",
        "unit": "$ millions",
        "freq": "weekly",
    },
    "sofr": {
        "fred_id": "SOFR",
        "label_ko": "SOFR 자금금리",
        "label_en": "SOFR",
        "unit": "%",
        "freq": "daily",
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
