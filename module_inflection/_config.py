# -*- coding: utf-8 -*-
"""module_inflection 설정 — 경로·임계의 단일 원본 (P1).

경로·utf8·유니버스 CSV 는 **다시 정의하지 않는다** — `module_news_data._config` 가
그 단일 원본이므로 그대로 import 한다. 여기서 소유하는 건 이 모듈만의 것:
파생 DB 경로와 변곡점 판정 임계.
"""
from __future__ import annotations

from module_news_data._config import (  # noqa: F401  (재수출 = 단일 원본 그대로)
    DATA_DIR,
    KR_UNIVERSE_CSV,
    OUT_DIR,
    utf8_stdout,
)

# 클라이언트 소유 파생물. 서버(수집 PC)는 이 파일의 존재를 모른다 — 언제든 지우고
# `build` 로 다시 만들 수 있어야 한다(news_vectors.db 와 같은 규약).
INFLECTION_DB = DATA_DIR / "inflection.db"
VEC_DB = DATA_DIR / "news_vectors.db"      # 읽기 전용 소비(제목·벡터·market_day)

# ── 변곡점 임계 (전부 표준편차 단위 — 절대 % 는 종목마다 뜻이 달라 못 쓴다) ──
VOL_WINDOW = 60        # 변동성 추정 창(거래일). t 는 제외한다(look-ahead 차단)
VOL_MIN_OBS = 30       # 이보다 표본이 적으면 σ 를 못 믿는다 → 판정 안 함
SHOCK_Z = 2.0          # |r_t| ≥ Z·σ → 충격
PIVOT_WINDOW = 10      # 전/후 추세를 재는 창(거래일)
PIVOT_Z = 2.0          # (post-pre)/(σ·√n) ≥ Z → 추세 전환
NEWS_WINDOW = 30       # 뉴스 언급량 baseline 창(달력일)
NEWS_MIN_OBS = 10

# 뉴스 창: 변곡일 기준 며칠을 함께 읽나. 앞을 길게 두는 건 '선행했나'를 보기 위해서다.
NEWS_LAG_BEFORE = 3
NEWS_LAG_AFTER = 1

# published_at 이 신뢰 가능한 최초 시점 — `_timeaxis.PUBLISHED_AT_SINCE` 와 같은 이유.
# 그 이전 구간은 뉴스 축이 통째로 비어 있어 '뉴스 없음'이 아니라 '측정 불가'다.
NEWS_START = "2026-05-01"
