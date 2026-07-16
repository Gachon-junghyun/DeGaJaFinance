"""SEC XBRL CompanyFacts — 분기 매출 (최근 N분기) 추출.

yfinance 분기 매출과 교차 검증용. 두 GAAP 키를 모두 시도 후 end 일자 dedup.
- us-gaap:Revenues  (NVDA 등 일부 기업의 신규 표기)
- us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax (AAPL 등 ASC 606)
"""
from __future__ import annotations

import sys
import time
from datetime import datetime
from typing import Optional

import requests

from module_disclosure_us._ticker_cik import USER_AGENT, ticker_to_cik

COMPANY_FACTS_URL = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json"

_HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate",
    "Host": "data.sec.gov",
}

_REVENUE_KEYS = (
    "Revenues",
    "RevenueFromContractWithCustomerExcludingAssessedTax",
)


def _is_quarterly(start: str, end: str) -> bool:
    """start-end 간격이 약 80~100일이면 분기로 판정."""
    try:
        s = datetime.strptime(start, "%Y-%m-%d")
        e = datetime.strptime(end, "%Y-%m-%d")
    except Exception:
        return False
    days = (e - s).days
    return 80 <= days <= 100


def _extract_quarterly(units: list[dict]) -> dict[str, tuple[float, str]]:
    """USD 엔트리 list → {end_date: (val, form)} 중복은 10-Q 우선."""
    out: dict[str, tuple[float, str]] = {}
    for entry in units:
        start = entry.get("start")
        end = entry.get("end")
        val = entry.get("val")
        form = entry.get("form", "")
        if not start or not end or val is None:
            continue
        if not _is_quarterly(start, end):
            continue
        try:
            v = float(val)
        except (TypeError, ValueError):
            continue
        existing = out.get(end)
        if existing is None:
            out[end] = (v, form)
            continue
        # 10-Q 가 10-K 보다 우선 (10-K 의 분기 표기는 보통 prior-year 보조)
        if form.startswith("10-Q") and not existing[1].startswith("10-Q"):
            out[end] = (v, form)
    return out


def fetch_xbrl_quarterly_revenue(
    ticker: str,
    limit: int = 8,
    timeout: int = 30,
) -> list[tuple[str, float]]:
    """SEC XBRL 에서 최근 N분기 매출 [(end_date, value), ...] 반환.

    실패 시 빈 리스트. 메시지는 stderr 로.
    """
    cik = ticker_to_cik(ticker)
    if cik is None:
        sys.stderr.write(f"[xbrl] unknown ticker {ticker} (no CIK)\n")
        return []
    url = COMPANY_FACTS_URL.format(cik=cik)
    try:
        r = requests.get(url, headers=_HEADERS, timeout=timeout)
        r.raise_for_status()
        data = r.json()
    except Exception as e:
        sys.stderr.write(f"[xbrl] {ticker} fetch failed: {e}\n")
        return []
    time.sleep(0.2)  # SEC fair access
    gaap = data.get("facts", {}).get("us-gaap", {})
    if not gaap:
        return []

    merged: dict[str, tuple[float, str]] = {}
    for key in _REVENUE_KEYS:
        block = gaap.get(key)
        if not block:
            continue
        units = block.get("units", {}).get("USD", [])
        partial = _extract_quarterly(units)
        for end, (val, form) in partial.items():
            existing = merged.get(end)
            if existing is None:
                merged[end] = (val, form)
                continue
            # 10-Q form 을 우선
            if form.startswith("10-Q") and not existing[1].startswith("10-Q"):
                merged[end] = (val, form)

    rows = [(end, val) for end, (val, _) in merged.items()]
    rows.sort(key=lambda x: x[0], reverse=True)
    return rows[:limit]
