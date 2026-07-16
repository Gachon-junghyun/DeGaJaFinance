# -*- coding: utf-8 -*-
"""module_chart — 텍스트(ASCII) 차트 + 결정론 구조판정 (CHART_READ).

가격을 LLM이 읽는 ASCII 캔들 차트로 렌더하고(캔들+MA+볼린저+거래량+RSI+OBV),
사람이 눈대중하던 구조 신호(OBV 누적/분배·다이버전스·턴 판정)를 기계가 매번
동일하게 판정해 CHART_READ 블록으로 낸다. yfinance OHLCV 기반, self-contained.

기능 지도 (기능 하나 = 파일 하나):
    _ohlcv       yfinance OHLCV 다운로드
    _indicators  MA·볼린저·RSI 라인
    _renderer    ASCII 차트 렌더 (캔들+오버레이+서브차트)
    _metadata    메타데이터 텍스트 + generate_chart_read (결정론 구조판정)
    _make_chart  티커 1개 → 차트 파일 저장 (공개 진입점)
    _constants   캔들/지표 문자   _utils   가격↔행 변환·포맷

빠른 사용:
    from module_chart import save_text_chart, fetch_ohlcv, plot_combined_chart
    save_text_chart("005930.KS")                 # → output/005930_KS_chart.txt

CLI:
    python -m module_chart 005930.KS             # 차트 파일 저장
    python -m module_chart AAPL --read           # CHART_READ 블록만(에이전트 브리프 임베드용)
"""
from ._make_chart import save_text_chart
from ._renderer import plot_text_chart, plot_combined_chart
from ._indicators import add_ma, add_bollinger, add_rsi_line
from ._metadata import generate_metadata
from ._ohlcv import fetch_ohlcv

__all__ = [
    "save_text_chart",
    "plot_text_chart",
    "plot_combined_chart",
    "add_ma",
    "add_bollinger",
    "add_rsi_line",
    "generate_metadata",
    "fetch_ohlcv",
]
