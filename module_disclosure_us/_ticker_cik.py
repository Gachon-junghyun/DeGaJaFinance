"""티커 <-> CIK 매핑.

SEC 공식 파일(https://www.sec.gov/files/company_tickers.json)을
첫 호출 시 한 번 받아 `_cache/ticker_cik_map.json`에 캐싱.
"""
from __future__ import annotations

import json
import os
import time
from pathlib import Path
from typing import Optional

import requests

# SEC Fair Access: User-Agent에 실명/이메일 식별자 필수.
# 환경변수 SEC_USER_AGENT로 override 가능.
USER_AGENT = os.environ.get(
    "SEC_USER_AGENT",
    "mvp Research fivepeople201@gmail.com",
)
TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"
CACHE_PATH = Path(__file__).parent / "_cache" / "ticker_cik_map.json"


def _download_tickers() -> dict[str, int]:
    headers = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    r = requests.get(TICKERS_URL, headers=headers, timeout=30)
    r.raise_for_status()
    raw = r.json()
    out: dict[str, int] = {}
    for v in raw.values():
        t = str(v.get("ticker", "")).upper().strip()
        cik = v.get("cik_str")
        if t and isinstance(cik, int):
            out[t] = cik
    return out


def load_ticker_cik_map(force_refresh: bool = False) -> dict[str, int]:
    if CACHE_PATH.exists() and not force_refresh:
        try:
            data = json.loads(CACHE_PATH.read_text(encoding="utf-8"))
            if isinstance(data, dict) and data:
                return {k.upper(): int(v) for k, v in data.items()}
        except Exception:
            pass
    data = _download_tickers()
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CACHE_PATH.write_text(json.dumps(data, indent=2), encoding="utf-8")
    time.sleep(0.2)
    return data


def ticker_to_cik(ticker: str, cache: Optional[dict[str, int]] = None) -> Optional[int]:
    if cache is None:
        cache = load_ticker_cik_map()
    return cache.get(ticker.upper().strip())
