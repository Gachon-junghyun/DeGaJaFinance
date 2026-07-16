# FILE: research_Mvp/module_kis/__init__.py
"""module_kis — 한국투자증권(KIS) Open API 조회 모듈.

국내주식 현재가·밸류에이션·기간별 OHLCV·투자자별 수급·계좌잔고를 KIS 공식 API로 수집한다.
yfinance(.KS/.KQ 추정)·네이버 스크랩의 무인증 채널 대비 더 안정적인 인증 소스.

조회(시세/잔고)는 자유. 주문(place_order)은 **휴먼 트리거 전용** — 기본 드라이런이고
execute=True(CLI --execute)를 사람이 명시할 때만 발사한다. 자동매매/스케줄 자동발사 아님.
정정/취소/이체 등은 포함하지 않음. 계좌·주문은 KIS_ACCOUNT_NO 환경변수가 추가로 필요.

요구사항:
    - 환경변수 KIS_APP_KEY / KIS_APP_SECRET (https://apiportal.koreainvestment.com)
    - KIS_ENV: prod(실전, 기본) | vps(모의)
    - 의존성은 requests 뿐(이미 mvp 공용).

빠른 사용:
    from module_kis import fetch_quote, fetch_ohlcv, fetch_investor_trend

    q = fetch_quote("005930")                 # 삼성전자 현재가/밸류에이션
    print(q.price, q.per, q.foreign_pct)

    bars, name = fetch_ohlcv("005930", "D", count=120)   # 일봉 120개
    rows = fetch_investor_trend("005930", days=20)        # 외국인/기관 수급

CLI:
    python -m module_kis 005930                          # 시세 스냅샷
    python -m module_kis 005930 --ohlcv D --count 120    # 일봉
    python -m module_kis 005930 --investor 20            # 수급
    python -m module_kis 005930 --all --out llm_outputs/kis_005930.md
    python -m module_kis 005930 --json
"""
from ._account import Balance, Holding, fetch_balance
from ._account import to_dict as balance_to_dict
from ._auth import KisConfig, KisError, get_access_token, load_config
from ._order import OrderPreview, OrderResult, place_order
from ._order import to_dict as order_to_dict
from ._overseas_order import (
    UsOrderPreview,
    UsOrderResult,
    UsQuote,
    fetch_us_buyable,
    fetch_us_quote,
    place_us_order,
)
from ._overseas_order import to_dict as us_order_to_dict
from ._overseas import (
    ForeignCash,
    OverseasBalance,
    OverseasHolding,
    fetch_overseas_balance,
)
from ._overseas import to_dict as overseas_to_dict
from ._chart import KisBar, fetch_ohlcv
from ._chart import to_dicts as ohlcv_to_dicts
from ._investor import InvestorDay, fetch_investor_trend, net_summary
from ._investor import to_dicts as investor_to_dicts
from ._quote import KisQuote, fetch_quote, to_dict
from ._ranking import RankRow, fetch_fluctuation, fetch_volume_rank
from ._renderer import (
    render_balance,
    render_investor,
    render_ohlcv,
    render_order,
    render_quote,
    render_wallet,
)

__all__ = [
    # 설정/인증
    "KisConfig",
    "KisError",
    "load_config",
    "get_access_token",
    # 시세/밸류에이션
    "KisQuote",
    "fetch_quote",
    "to_dict",
    # OHLCV
    "KisBar",
    "fetch_ohlcv",
    "ohlcv_to_dicts",
    # 수급
    "InvestorDay",
    "fetch_investor_trend",
    "net_summary",
    "investor_to_dicts",
    # 순위(읽기 전용)
    "RankRow",
    "fetch_fluctuation",
    "fetch_volume_rank",
    # 계좌 잔고(읽기 전용)
    "Balance",
    "Holding",
    "fetch_balance",
    "balance_to_dict",
    # 해외/외화 잔고(읽기 전용)
    "OverseasBalance",
    "OverseasHolding",
    "ForeignCash",
    "fetch_overseas_balance",
    "overseas_to_dict",
    # 주문(휴먼 트리거 — execute=True 일 때만 발사)
    "place_order",
    "OrderPreview",
    "OrderResult",
    "order_to_dict",
    # 미국주식 시세/주문(휴먼 트리거)
    "fetch_us_quote",
    "fetch_us_buyable",
    "UsQuote",
    "place_us_order",
    "UsOrderPreview",
    "UsOrderResult",
    "us_order_to_dict",
    # 렌더러
    "render_quote",
    "render_ohlcv",
    "render_investor",
    "render_balance",
    "render_wallet",
    "render_order",
]
