"""module_macro_us — FRED 미국 매크로 시계열 fetch + markdown 리포트.

12개 시리즈 (Treasury yield curve, Fed Funds, CPI, Core CPI, 실업률,
VIX, Dollar Index, TIPS, M2 등)를 FRED API에서 끌어와
요약 헤더 + 시리즈별 상세 markdown 으로 정리한다.

요구사항:
    - 환경변수 FRED_API_KEY (https://fred.stlouisfed.org/docs/api/api_key.html)
    - (옵션) `pip install fredapi` — 없으면 requests REST 폴백 자동 사용

CLI:
    python -m module_macro_us
    python -m module_macro_us --series us_10y,cpi,vix --days 365
    python -m module_macro_us --days 90 --out llm_outputs/2026-05-26/macro_us.md
    python -m module_macro_us --series us_10y --json

Public API:
    fetch_series(keys, days)  -> list[SeriesData]
    build_report(rows)        -> str  (markdown)
    SERIES_CATALOG            -> dict (12종 메타)
"""
from ._fetch import MacroFetchError, Observation, SeriesData, fetch_series
from ._renderer import render_markdown as build_report
from ._series import DEFAULT_KEYS, SERIES_CATALOG, resolve_keys

__all__ = [
    "DEFAULT_KEYS",
    "MacroFetchError",
    "Observation",
    "SERIES_CATALOG",
    "SeriesData",
    "build_report",
    "fetch_series",
    "resolve_keys",
]
