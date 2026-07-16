"""EDGAR submissions API 호출 + 8-K 본문 enrich."""
from __future__ import annotations

import sys
import time
import warnings
from datetime import date, datetime
from typing import Optional

import requests
from bs4 import BeautifulSoup

try:
    from bs4 import XMLParsedAsHTMLWarning
    warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
except Exception:
    pass

from ._categorizer import categorize_filing, extract_items_from_html
from ._renderer import Filing
from ._ticker_cik import USER_AGENT, ticker_to_cik

SUBMISSIONS_URL = "https://data.sec.gov/submissions/CIK{cik:010d}.json"
ARCHIVE_URL = "https://www.sec.gov/Archives/edgar/data/{cik}/{accession_no_clean}/{primary_doc}"
FILING_DETAIL_URL = "https://www.sec.gov/Archives/edgar/data/{cik}/{accession_no_clean}/"

# data.sec.gov / www.sec.gov 호스트 별 헤더 분리 (Host 헤더 명시).
_HEADERS_DATA = {
    "User-Agent": USER_AGENT,
    "Accept-Encoding": "gzip, deflate",
    "Host": "data.sec.gov",
}
_HEADERS_WEB = {
    "User-Agent": USER_AGENT,
    "Accept-Encoding": "gzip, deflate",
    "Host": "www.sec.gov",
}


def _get_submissions(cik: int) -> dict:
    url = SUBMISSIONS_URL.format(cik=cik)
    r = requests.get(url, headers=_HEADERS_DATA, timeout=30)
    r.raise_for_status()
    return r.json()


def _within_days(filing_date_str: str, days: int) -> bool:
    try:
        d = datetime.strptime(filing_date_str, "%Y-%m-%d").date()
    except Exception:
        return False
    return (date.today() - d).days <= days


def _build_filing_rows(
    ticker: str, cik: int, sub_json: dict, days: int
) -> list[Filing]:
    recent = sub_json.get("filings", {}).get("recent", {})
    forms = recent.get("form", [])
    dates = recent.get("filingDate", [])
    accs = recent.get("accessionNumber", [])
    docs = recent.get("primaryDocument", [])
    n = min(len(forms), len(dates), len(accs), len(docs))
    rows: list[Filing] = []
    for i in range(n):
        if not _within_days(dates[i], days):
            continue
        acc_clean = accs[i].replace("-", "")
        primary = docs[i]
        url = ARCHIVE_URL.format(cik=cik, accession_no_clean=acc_clean, primary_doc=primary)
        idx_url = FILING_DETAIL_URL.format(cik=cik, accession_no_clean=acc_clean)
        rows.append(
            Filing(
                ticker=ticker,
                cik=cik,
                form=forms[i],
                filing_date=dates[i],
                accession_no=accs[i],
                primary_doc=primary,
                url=url,
                filing_index_url=idx_url,
            )
        )
    return rows


def _fetch_8k_body_and_categorize(row: Filing) -> None:
    if not row.form.upper().startswith("8-K"):
        cat, label = categorize_filing(row.form, [])
        row.category = cat
        row.label = label
        return

    items: list[str] = []
    summary = ""
    try:
        r = requests.get(row.url, headers=_HEADERS_WEB, timeout=20)
        if r.status_code == 200:
            html = r.text
            items = extract_items_from_html(html)
            try:
                soup = BeautifulSoup(html, "lxml")
                text = soup.get_text(" ", strip=True)
                if items:
                    first_item = items[0]
                    idx = text.lower().find(f"item {first_item}".lower())
                    snippet = text[idx : idx + 240] if idx >= 0 else text[:240]
                else:
                    snippet = text[:240]
                summary = " ".join(snippet.split())[:200]
            except Exception:
                summary = ""
    except Exception as e:
        sys.stderr.write(f"[warn] {row.ticker} {row.accession_no} body fetch failed: {e}\n")

    row.items = items
    cat, label = categorize_filing(row.form, items)
    row.category = cat
    row.label = label
    row.summary = summary


def fetch_filings(ticker: str, days: int = 90) -> tuple[list[Filing], int, Optional[str]]:
    """EDGAR submissions + 8-K 본문 enrich. 반환: (rows, cik, company_name)."""
    cik = ticker_to_cik(ticker)
    if cik is None:
        raise SystemExit(f"Unknown ticker: {ticker}")
    sub = _get_submissions(cik)
    company_name = sub.get("name")
    time.sleep(0.2)
    rows = _build_filing_rows(ticker, cik, sub, days)
    eightk = [r for r in rows if r.form.upper().startswith("8-K")]
    sys.stderr.write(f"[{ticker}] {len(rows)} filings total, {len(eightk)} 8-K (fetching bodies)\n")
    for r in rows:
        _fetch_8k_body_and_categorize(r)
        if r.form.upper().startswith("8-K"):
            time.sleep(0.2)
    return rows, cik, company_name
