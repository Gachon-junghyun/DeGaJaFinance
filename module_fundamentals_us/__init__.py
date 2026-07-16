"""module_fundamentals_us — yfinance + SEC XBRL 펀더멘털/밸류에이션/컨센서스.

KR module_valuation(Naver) 의 미국판. 단일 ticker → 펀더멘털 markdown.

CLI:
    python -m module_fundamentals_us NVDA
    python -m module_fundamentals_us NVDA --out llm_outputs/nvda_fund.md
    python -m module_fundamentals_us NVDA --json
    python -m module_fundamentals_us AAPL --no-xbrl
"""
from ._renderer import render_markdown
from ._xbrl_fetch import fetch_xbrl_quarterly_revenue
from ._yfinance_fetch import FundamentalsSnapshot, fetch_fundamentals

__all__ = [
    "FundamentalsSnapshot",
    "fetch_fundamentals",
    "fetch_xbrl_quarterly_revenue",
    "render_markdown",
]
