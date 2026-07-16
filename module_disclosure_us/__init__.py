"""module_disclosure_us — SEC EDGAR 필링 fetch + 카테고라이즈 + markdown.

KR module_disclosure의 미국판. DART API 대신 EDGAR submissions API,
공시 카테고리 대신 8-K Item code 기반 분류.

CLI: `python -m module_disclosure_us AAPL --days 90 --out report_AAPL.md`

원래 PLAYGROUND/PLAY27_edgar_fetch에서 검증 후 박제.
"""
from ._categorizer import (
    CATEGORY_LABELS,
    CATEGORY_ORDER,
    categorize_filing,
    extract_items_from_html,
)
from ._edgar_api import fetch_filings
from ._renderer import Filing, render_markdown
from ._ticker_cik import load_ticker_cik_map, ticker_to_cik

__all__ = [
    "CATEGORY_LABELS",
    "CATEGORY_ORDER",
    "Filing",
    "categorize_filing",
    "extract_items_from_html",
    "fetch_filings",
    "load_ticker_cik_map",
    "render_markdown",
    "ticker_to_cik",
]
