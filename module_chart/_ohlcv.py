from __future__ import annotations

import pandas as pd
import yfinance as yf


def fetch_ohlcv(ticker: str, period: str = "1y") -> pd.DataFrame:
    """yfinance 로 OHLCV 다운로드. 컬럼명 소문자, 빈 결과는 빈 DF.

    ticker 는 yfinance 그대로 — KOSPI 면 ``"005930.KS"`` 처럼 suffix 포함해서 호출.
    """
    df = yf.download(ticker, period=period, progress=False)
    if df is None or df.empty:
        return pd.DataFrame()
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    df.columns = [str(c).lower() for c in df.columns]
    return df
