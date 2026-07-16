# -*- coding: utf-8 -*-
"""module_flow — 수급·기대감 리더 (돈·관심의 흐름을 결정론으로).

가치(4Phase)·차트(CHART_READ)가 못 보는 '지금 돈이 들어오나/내러티브가 가속하나'.
4Phase가 바닥(살아남나/얼마짜리냐)이면 이건 방아쇠(지금 사나). AI는 기대감이 곧
트레이드라 펀더가 따라오기 전에 흐름이 먼저 가격을 민다.

축 (전부 기존 데이터 재사용, 새 소스 0):
    ① 뉴스속도    _news_velocity   news_fts 기사량 가속비 (module_news_data 색인 재사용)
    ②③④ 가격흐름  _price_flow      OBV 매집/분산 · 상대강도 RS · 거래량 서지
    ⑦ 투자자수급  _investor        외국인/기관/개인 순매수 (module_KIS, KR 전용)
    ⑧⑤⑥ 포지셔닝  _short           KR 공매도잔고 · US 공매도%float · 옵션 P/C·IV스큐
    합성          _synthesize      flow_tag → 🟢가속 / 🟡중립 / 🔴분산

⚠️ 🟢가속이라도 진입은 하드스탑 필수(기대감=꼭지위험). 4Phase '바닥'과 교차.

CLI:
    python -m module_flow NVDA GEV VRT MU --bench SPY --json
    python -m module_flow 005930.KS --names "삼성전자"      # KR = ⑦수급·⑧공매도 자동
"""
from ._config import FOREIGN_SOURCES, FTS_DB, kr_code
from ._investor import investor_flow
from ._news_velocity import news_query, news_velocity
from ._price_flow import price_flow
from ._short import positioning, short_flow
from ._synthesize import flow_tag

__all__ = [
    "news_query", "news_velocity",
    "price_flow",
    "investor_flow",
    "short_flow", "positioning",
    "flow_tag",
    "kr_code", "FOREIGN_SOURCES", "FTS_DB",
]
