"""US 사업 모델 추출 모듈 (KR `module_business` 의 US판).

edgartools 로 SEC EDGAR 에서 10-K / 10-Q 본문(Item 1 Business, Item 1A Risk Factors,
Item 7 MD&A) 을 추출해 markdown 으로 렌더한다.

다른 module 와의 결합도 0:
- module_disclosure_us / module_macro_us / module_valuation 모두 import 안 함.
- SEC_USER_AGENT 환경변수는 공유하지만 edgartools 의 set_identity 로 별도 주입.

CLI:
    python -m module_business_us NVDA
    python -m module_business_us NVDA --full --out llm_outputs/.../nvda_business.md
    python -m module_business_us NVDA --form 10-Q
    python -m module_business_us NVDA --json

Public API:
    extract(ticker, *, form="10-K", full=False) -> ExtractResult | None
    render_markdown(result, *, full=False) -> str
"""
from __future__ import annotations

from typing import Optional

from ._edgar import ExtractResult, extract_business_us, EdgartoolsMissingError
from ._renderer import render_markdown

__all__ = [
    "ExtractResult",
    "EdgartoolsMissingError",
    "extract",
    "render_markdown",
]


def extract(
    ticker: str,
    *,
    form: str = "10-K",
    full: bool = False,
) -> Optional[ExtractResult]:
    """ticker -> ExtractResult.

    Args:
        ticker: US 티커 (예: "NVDA").
        form: "10-K" (default) or "10-Q".
        full: 본문 전체 cap (50K) 까지 보존. False 면 Risk Factors 는 bullet 요약만.

    Returns:
        ExtractResult on success, None when ticker unknown / no filing found.
    """
    return extract_business_us(ticker, form=form, full=full)
