# -*- coding: utf-8 -*-
"""yf_snapshot — 일봉 OHLCV 한 종목 → 셋업 스크리너가 쓰는 **스칼라 지표 묶음**.

왜 있나: `us_setup_screener.py` 가 `import yf_snapshot` 로 이 파일의 compute() 를 부르는데,
이 파일이 리포에 **한 번도 커밋된 적이 없었다**(`git log --all -- scripts/yf_snapshot.py` → 0건).
옛 research_Mvp 에서 스크리너만 옮겨오고 헬퍼를 두고 온 것. 그래서 스크리너는 기동 즉시
ModuleNotFoundError 로 죽었고 — 실측 2026-07-17 industry_us 런에서 BET 스테이지의
'넓은 그물' 한 다리(= 이미 아는 이름 **밖**을 훑으라고 있는 다리)가 조용히 0건을 기여했다.
후보 union 이 (DEEP 리더 ∪ 스크리너 셋업 ∪ LIVE 숏리스트) 인데 가운데가 통째로 빠져 있었다.

⚠ 지표 산식은 여기서 새로 짜지 않는다(P1) — **`module_chart` 가 RSI·MA 의 단일 원본**이다.
이 파일은 그 시계열을 스크리너가 원하는 '마지막 값 스칼라'로 접는 **얇은 어댑터**일 뿐이다.
(RSI 산식은 이미 module_chart 안에서 두 번 복제돼 있었고, 여기서 직접 구현하면 세 번째가
된다 → `_indicators.rsi_series` 로 합쳐 그걸 부른다.)

반환 키는 us_setup_screener.classify() 가 읽는 것과 1:1:
    last · rsi14 · sma50 · sma200 · px_vs_sma200   (l52w 는 호출자가 붙인다)

값이 안 나오는 지표(봉 부족)는 **None** — 빈칸은 빈칸으로 둔다(추정 금지, P4).
"""
from __future__ import annotations

import pandas as pd

import _repo_path  # noqa: F401  — sys.path 에 리포 루트 삽입(아래 module_chart import 전에)
from module_chart._indicators import add_ma, rsi_series
from module_chart._utils import _norm


def _last_valid(s: pd.Series) -> float | None:
    """시계열의 마지막 유효값(NaN 제외). 전부 NaN 이면 None."""
    s = s.dropna()
    return float(s.iloc[-1]) if len(s) else None


def compute(df: pd.DataFrame) -> dict:
    """일봉 OHLCV DataFrame → 스크리너용 스칼라 지표.

    입력: `close` 컬럼을 가진 일봉(대소문자 무관 — module_chart._norm 이 정규화).
    출력: {"last", "rsi14", "sma50", "sma200", "px_vs_sma200"}
          px_vs_sma200 = 200일선 대비 이격도 **퍼센트** (스크리너 DERATE_MAX=-12.0 과 같은 단위).
    """
    close = _norm(df)["close"].astype(float).dropna()
    if close.empty:
        return {"last": None, "rsi14": None, "sma50": None,
                "sma200": None, "px_vs_sma200": None}

    last = float(close.iloc[-1])
    ma = add_ma(df, [50, 200])                 # SMA 단일 원본
    sma50 = _last_valid(ma["MA50"])
    sma200 = _last_valid(ma["MA200"])
    rsi14 = _last_valid(rsi_series(df, 14))    # RSI 단일 원본

    return {
        "last": last,
        "rsi14": rsi14,
        "sma50": sma50,
        "sma200": sma200,
        # 200일선이 아직 안 잡히면(봉<200) 이격도는 없는 것 — 0 으로 채우지 않는다.
        "px_vs_sma200": None if not sma200 else (last / sma200 - 1.0) * 100.0,
    }
