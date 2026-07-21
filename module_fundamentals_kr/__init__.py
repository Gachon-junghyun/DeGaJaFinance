# -*- coding: utf-8 -*-
"""module_fundamentals_kr — KR 재무제표 + 수익의 질 (DART 전체재무제표).

module_fundamentals_us 의 KR 대응. US 는 yfinance/SEC XBRL 이지만 KR 은 DART
fnlttSinglAcntAll 이 유일한 결정론 원본이라 별도 모듈로 둔다(P3 의 예외가 아니라
데이터 소스 자체가 다름 — 시장 인자로 흡수 불가).

기능 지도:
    _dart_fin   DART 전체재무제표 fetch + 계정 추출 (account_id 우선, 한글명 폴백)
    _quality    수익의 질 — 발생액 · 미청구공사 · 운전자본
    _renderer   마크다운

빠른 사용:
    from module_fundamentals_kr import fetch_by_stock, compute, render_markdown
    fin = fetch_by_stock("000720")
    print(render_markdown(compute(fin)))

CLI:
    python -m module_fundamentals_kr 000720
"""
from ._dart_fin import (
    Account,
    Financials,
    fetch_by_stock,
    fetch_financials,
    REPRT_CODES,
)
from ._quality import Flag, QualityMetrics, compute
from ._renderer import render_markdown

__all__ = [
    "Account",
    "Financials",
    "Flag",
    "QualityMetrics",
    "REPRT_CODES",
    "compute",
    "fetch_by_stock",
    "fetch_financials",
    "render_markdown",
]
