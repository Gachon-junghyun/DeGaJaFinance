# -*- coding: utf-8 -*-
"""module_lens 설정 — 이 모듈만의 경로·창·장 마감 시각 (P1).

경로·utf8·유니버스는 `module_news_data._config` 가 단일 원본이라 다시 정의하지 않는다.
"""
from __future__ import annotations

import importlib.util
from datetime import time, timedelta, timezone
from pathlib import Path

_REPO = Path(__file__).resolve().parent.parent


def _news_config():
    """`module_news_data/_config.py`(표준 라이브러리만 쓴다)를 **비공개 이름으로** 읽는다.

    정식 import(`module_news_data._config`)는 그 패키지의 `__init__` 이 feedparser·requests·bs4 를 끌고 와
    이 PC 에서 약 1초가 든다(2026-10-31 실측) — 훅(2초 제한)과 stdlib 만 쓰는 장부 층엔 무겁다.
    정식 이름으로 sys.modules 에 끼워 넣던 첫 방식은 나중의 정식 import 에서 부모 패키지 속성이 빠지는
    결함이 있었다(검토 R, 2026-10-31). 비공개 이름이면 정식 패키지와 서로 안 건드린다. 값의 원본은 그대로 그 파일이다.
    """
    spec = importlib.util.spec_from_file_location("module_lens._news_config_leaf",
                                                  _REPO / "module_news_data" / "_config.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_nc = _news_config()
DATA_DIR, OUT_DIR, utf8_stdout = _nc.DATA_DIR, _nc.OUT_DIR, _nc.utf8_stdout

# 클라이언트 소유 파생물(P6) — 서버는 존재를 모른다. 지우고 `build` 로 다시 만든다.
LENS_DB = DATA_DIR / "lens.db"
VEC_DB = DATA_DIR / "news_vectors.db"          # 읽기 전용(제목·발행시각·벡터)


def __getattr__(name):
    """NEWS_START = 발행시각을 믿을 수 있는 첫날(`_timeaxis.PUBLISHED_AT_SINCE`). 그 앞은 «뉴스 없음»이 아니라
    «잴 수 없음». `_timeaxis` 는 패키지 상대 import 를 써서 정식 import 가 필요하다 — 쓰는 쪽(데이터 층)에서만 부른다."""
    if name == "NEWS_START":
        from module_news_data._timeaxis import PUBLISHED_AT_SINCE
        return PUBLISHED_AT_SINCE
    raise AttributeError(name)


# 라벨 창(거래일). FWD_AVG 는 사람이 정한 «이후 3일 동안 평균 높낮이» = +1…+3일 누적의 평균.
FWD_AVG = 3
FWD_POINTS = (1, 3, 5)

KST = timezone(timedelta(hours=9))
# 장 마감 — 발행시각이 이 전이면 그날 세션, 아니면 다음 거래일 세션.
CLOSE = {"KR": (KST, time(15, 30)), "US": ("America/New_York", time(16, 0))}

KR_MIN_NAME_LEN = 3      # `_universe.KR_MIN_NAME_LEN` 과 같은 이유(대상·삼양·농심). 한글 별칭에도 쓴다
PRICE_PERIOD = "2y"      # 직전 수익·변동성 창을 위해 뉴스 축보다 길게 받는다

# ── 장부 층 (DESIGN.md) ─────────────────────────────────────────────
# 🔴 원본 기록이다 — lens.db(지워도 되는 파생물)와 파일을 나눈다. 백업은 EXPORT_DIR 의 JSONL 덤프(git 추적).
LEDGER_DB = DATA_DIR / "lens_ledger.db"
# 수급·포지셔닝 근거의 비중 합 상한(%) — 결론이 수급만으로 서지 않게(2026-10-31 사람: «결국 수급만 남더라»,
# 장부 첫 학습 수급 0.18). `think` 가 넘으면 거절하고 `advise` 는 이 안에서만 권한다. 30% 는 사람 결정(2026-10-31).
FLOW_KINDS = ("flow", "positioning")
FLOW_CAP = 30.0
EXPORT_DIR = _REPO / "handoff" / "lens"     # 리포 기준 — DATA_DIR 이 옮겨져도 git 이 추적하는 자리에 남는다
