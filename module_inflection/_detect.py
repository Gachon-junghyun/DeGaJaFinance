# -*- coding: utf-8 -*-
"""변곡점 판정 — 전부 **표준편차 단위**의 결정론 라벨러 (판단 아님, P4).

두 종류를 판정한다. 둘은 대체재가 아니다(`burst` vs `cluster` 가 다른 축인 것과 같은 이유):

  · **shock**  |r_t| ≥ Z·σ  — "그날 하루가 평소의 몇 배였나". 사건에 대한 즉각 반응.
    σ 는 t 를 **뺀** 직전 60거래일로 잰다(t 를 넣으면 자기 자신으로 자기를 정규화해
    큰 날일수록 z 가 줄어드는 look-ahead 편향이 생긴다).

  · **pivot**  추세의 부호가 뒤집히는 날 — "여기서 흐름이 바뀌었다". 앞 10일 누적수익과
    뒤 10일 누적수익의 **부호가 반대**이고 그 격차가 σ·√2n 대비 Z 이상이며, 종가가
    ±10일 구간의 최저/최고여야 한다(진짜 꼭짓점만).

⚠ **pivot 은 미래 10일을 쓴다 — 실시간 신호가 아니다.** 사후 라벨러다. 이 모듈의 목적은
'변곡점을 미리 맞히는 것'이 아니라 **이미 확정된 변곡점 주변에 어떤 말이 있었나를 학습**
하는 것이므로 사후 라벨이 맞다. 이걸 그대로 진입신호로 쓰면 완벽한 백테스트가 나오고
실전에서 0 이 된다 — 소비자는 반드시 이 경고를 함께 읽어야 한다.

⚠ shock 은 미래를 안 쓰므로 그날 장 마감 시점에 계산 가능하다(그래도 '오늘 터진 걸
오늘 아는' 것이지 예측이 아니다).
"""
from __future__ import annotations

import math
from dataclasses import dataclass, asdict

import numpy as np
import pandas as pd

from ._config import PIVOT_WINDOW, PIVOT_Z, SHOCK_Z, VOL_MIN_OBS, VOL_WINDOW


@dataclass
class Event:
    ticker: str
    date: str
    kind: str          # shock_up | shock_down | pivot_up | pivot_down
    z: float           # 표준편차 단위 크기 (부호 포함)
    ret: float         # 당일 수익률 (pivot 이면 전환 격차)
    sigma: float       # 판정에 쓴 일간 σ
    fwd1: float | None
    fwd5: float | None
    fwd20: float | None
    prior5: float | None
    prior20: float | None

    def as_dict(self) -> dict:
        return asdict(self)


def _fwd(rets: np.ndarray, i: int, n: int) -> float | None:
    """i 다음날부터 n일 누적수익(단순합, 로그아님 — 소수점 단위라 차이 무시가능)."""
    if i + n >= len(rets):
        return None
    seg = rets[i + 1:i + 1 + n]
    return float(np.nansum(seg))


def _prior(rets: np.ndarray, i: int, n: int) -> float | None:
    if i - n < 0:
        return None
    return float(np.nansum(rets[i - n:i]))


def detect_ticker(ticker: str, close: pd.Series,
                  shock_z: float = SHOCK_Z, pivot_z: float = PIVOT_Z) -> list[Event]:
    """한 종목의 종가 시계열 → 변곡 이벤트 목록."""
    s = close.dropna()
    if len(s) < VOL_WINDOW + PIVOT_WINDOW + 5:
        return []
    dates = [str(d)[:10] for d in s.index]
    rets = s.pct_change().to_numpy()
    out: list[Event] = []
    pw = PIVOT_WINDOW

    for i in range(VOL_MIN_OBS + 1, len(s)):
        lo = max(1, i - VOL_WINDOW)
        window = rets[lo:i]                       # t 제외 — look-ahead 차단
        window = window[~np.isnan(window)]
        if len(window) < VOL_MIN_OBS:
            continue
        sigma = float(np.std(window, ddof=1))
        if sigma <= 0:
            continue
        r = rets[i]
        if np.isnan(r):
            continue

        # ① shock
        z = r / sigma
        if abs(z) >= shock_z:
            out.append(Event(ticker, dates[i], "shock_up" if z > 0 else "shock_down",
                             round(z, 3), round(float(r), 5), round(sigma, 5),
                             _fwd(rets, i, 1), _fwd(rets, i, 5), _fwd(rets, i, 20),
                             _prior(rets, i, 5), _prior(rets, i, 20)))

        # ② pivot — 미래 10일 필요
        if i - pw < 0 or i + pw >= len(s):
            continue
        pre = float(np.nansum(rets[i - pw:i]))
        post = float(np.nansum(rets[i + 1:i + 1 + pw]))
        if pre == 0 or post == 0 or (pre > 0) == (post > 0):
            continue                              # 부호가 안 뒤집히면 변곡이 아니다
        score = (post - pre) / (sigma * math.sqrt(2 * pw))
        if abs(score) < pivot_z:
            continue
        seg = s.iloc[i - pw:i + pw + 1]
        px = float(s.iloc[i])
        is_low = px <= float(seg.min()) * 1.0000001
        is_high = px >= float(seg.max()) * 0.9999999
        if score > 0 and not is_low:              # 상승전환인데 바닥이 아니면 통과 못함
            continue
        if score < 0 and not is_high:
            continue
        out.append(Event(ticker, dates[i], "pivot_up" if score > 0 else "pivot_down",
                         round(score, 3), round(post - pre, 5), round(sigma, 5),
                         _fwd(rets, i, 1), _fwd(rets, i, 5), _fwd(rets, i, 20),
                         _prior(rets, i, 5), _prior(rets, i, 20)))
    return out


def z_series(close: pd.Series) -> pd.Series:
    """일별 수익률 z (σ 는 직전 60일, t 제외). 정량검증(상관·리프트)의 재료."""
    s = close.dropna()
    rets = s.pct_change()
    sig = rets.shift(1).rolling(VOL_WINDOW, min_periods=VOL_MIN_OBS).std()
    return (rets / sig).replace([np.inf, -np.inf], np.nan)
