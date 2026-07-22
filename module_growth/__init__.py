"""module_growth — 이익 성장 기업 스크리너(실험 모델).

유니버스(us_top300·kr_all)를 훑어 분기 이익 시계열에서 결정론 성장 지표를 계산하고 랭킹한다.
판단(매수/매도)은 내지 않고 관측값·출처·신선도만 낸다(P4). 무엇을 살지는 상위(에이전트).

재무 fetch 는 재구현하지 않는다(P1): US=module_fundamentals_us, KR=module_valuation.
성장 계산(_metrics)은 순수 함수 — 네트워크 없이 합성 픽스처로 검증 가능.

CLI:
    python -m module_growth --market us --limit 50 --top 20
    python -m module_growth --market us --sector Semiconductors
    python -m module_growth --ticker NVDA AMD AVGO      # 임의 티커 직접
    python -m module_growth --market us --limit 30 --json
"""
from ._metrics import GrowthMetrics, compute_metrics
from ._render import render_detail, render_markdown
from ._screen import ScreenResult, screen
from ._universe import UniverseRow, load_universe

__all__ = [
    "GrowthMetrics",
    "ScreenResult",
    "UniverseRow",
    "compute_metrics",
    "load_universe",
    "render_detail",
    "render_markdown",
    "screen",
]
