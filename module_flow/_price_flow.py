# -*- coding: utf-8 -*-
"""②③④ 가격 기반 결정론 수급 — OBV 매집/분산 · 상대강도 RS · 거래량 서지.

df 주입 시 다운로드 생략 — 유니버스 배치스윕이 동일 수식을 재사용할 수 있게(과거 sector_flow 패턴).
"""
from __future__ import annotations

import numpy as np
import pandas as pd
import yfinance as yf


def price_flow(tk: str, bench_close: pd.Series, df: pd.DataFrame | None = None) -> dict:
    if df is None:
        df = yf.download(tk, period="4mo", progress=False, auto_adjust=False)
    if df is None or df.empty:
        return {"error": "empty"}
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    df.columns = [str(c).lower() for c in df.columns]
    close = df["close"].astype(float)
    vol = df["volume"].astype(float)
    n = len(close)
    if n < 60:
        return {"error": "short history"}

    # ② OBV 매집/분산: 최근20일 순매집 / 20일 총거래량 (-1..+1)
    obv = (np.sign(close.diff()).fillna(0) * vol).cumsum()
    obv_chg = float(obv.iloc[-1] - obv.iloc[-21])
    vol20 = float(vol.tail(20).sum())
    obv_norm = round(obv_chg / vol20, 3) if vol20 else 0.0
    obv_state = "매집" if obv_norm > 0.08 else "분산" if obv_norm < -0.08 else "중립"

    # ③ 상대강도: 20·60일 수익률 − 벤치
    # 2026-10-31 sim/flow: 벤치를 종목 날짜에 맞춘다. 예전엔 위치(iloc)로 셌는데 종목과 벤치의
    # 거래일 줄이 다르면(KR 휴장 전후·거래정지) 서로 다른 20일을 뺐다 — 실측 KR 표본 400건 중 10건 어긋남.
    try:
        b = bench_close.copy()
        b.index = pd.to_datetime(b.index).tz_localize(None) if getattr(b.index, "tz", None) else pd.to_datetime(b.index)
        ci = pd.to_datetime(close.index).tz_localize(None) if getattr(close.index, "tz", None) else pd.to_datetime(close.index)
        b = b.reindex(ci, method="ffill")
        b.index = close.index
    except Exception:
        b = bench_close

    def ret(s, d):
        return float(s.iloc[-1] / s.iloc[-1 - d] - 1.0) * 100 if len(s) > d else None

    def diff(a, c):                                   # 한쪽이 짧으면 None — TypeError 로 죽지 않는다
        return round(a - c, 1) if a is not None and c is not None else None
    rs20 = diff(ret(close, 20), ret(b, 20))
    rs60 = diff(ret(close, 60), ret(b, 60))

    # ④ 거래량 서지: 5일/50일
    vsurge = round(float(vol.tail(5).mean() / vol.tail(50).mean()), 2)

    return {"last": round(float(close.iloc[-1]), 2),
            "obv_norm": obv_norm, "obv_state": obv_state,
            "rs20": rs20, "rs60": rs60, "vol_surge": vsurge}
