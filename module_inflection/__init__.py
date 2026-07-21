# -*- coding: utf-8 -*-
"""module_inflection — 가격 변곡점 ↔ 뉴스 정렬 연구실.

"이런 말이 나올 때 이렇게 흘렀다"를 **관측으로** 만드는 모듈. 세 부분이다.
  ① 변곡 판정(`_detect`) — 전부 표준편차 단위. shock(하루 충격) / pivot(추세 전환, 사후라벨)
  ② 뉴스 정렬(`_newslink`) + 정량검증(`_stats`) — 리드/래그·리프트·순열검정
  ③ 전례 검색(`_analog`) — 이벤트 지문(제목 임베딩 평균)으로 과거 유사국면 + 그 후 실제 수익

판단은 하지 않는다(P4). 벡터·뉴스 DB·차트 지표는 각각의 소유 모듈에서 가져온다(P1).
"""
from ._analog import search as search_analogs
from ._detect import Event, detect_ticker, z_series
from ._newslink import articles_around, build_mentions, mention_z
from ._stats import lead_lag, lift_table, permutation_null, split_by_news

__all__ = [
    "Event", "detect_ticker", "z_series",
    "build_mentions", "mention_z", "articles_around",
    "lead_lag", "lift_table", "permutation_null", "split_by_news",
    "search_analogs",
]
