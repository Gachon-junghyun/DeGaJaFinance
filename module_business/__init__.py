"""사업 모델 추출 모듈 (Phase B' / 2번 프롬프트).

corp_embeddings.db 의 section_text(사업의 내용 본문)를 정규식 + 휴리스틱으로
파싱해서 매출 비중 표·핵심 제품·생산능력을 구조화 데이터로 반환한다.
news_alert.db 에서 1Q IR 보도자료 본문도 grep 발췌해 매출 모멘텀 보강.

다른 module_X 와 결합도 0:
- module_disclosure / module_valuation / module_embedding 모두 import 안 함.
- DART API 는 자체 _dart_fetch.py 로 직접 호출 (module_disclosure._dart_api 와 격리).

CLI:
    python -m module_business 068270 --include-ir
    python -m module_business 068270 --include-ir --include-dart --out llm_outputs/.../business_068270.md

Public API:
    extract(ticker, *, include_dart=False, include_ir=True)
        → dict {overview: BusinessOverview, ir_articles: list[IRArticle]?}

    render_markdown(extracted) → str
"""
from __future__ import annotations

from typing import Optional

from ._section_extract import (
    BusinessOverview,
    RevenueRow,
    extract_business_overview,
    load_section_text,
)
from ._ir_news import IRArticle, find_q1_ir_articles, render_ir_summary
from ._renderer import (
    render_business_model,
    render_revenue_table,
    render_state_report_block,
)

__all__ = [
    "BusinessOverview",
    "RevenueRow",
    "IRArticle",
    "extract",
    "render_markdown",
    "render_business_model",
    "render_state_report_block",
]


def extract(
    ticker: str,
    *,
    include_dart: bool = False,
    include_ir: bool = True,
    ir_days: int = 60,
) -> dict:
    """ticker → 구조화 데이터.

    Returns:
        {
            "overview": BusinessOverview | None,
            "ir_articles": list[IRArticle] | None,
            "dart_section": str | None,
        }
    """
    overview = extract_business_overview(ticker)
    ir_articles: Optional[list[IRArticle]] = None
    dart_section: Optional[str] = None

    if overview is None:
        return {"overview": None, "ir_articles": None, "dart_section": None}

    if include_ir:
        ir_articles = find_q1_ir_articles(overview.corp_name, days=ir_days)

    if include_dart:
        try:
            from ._dart_fetch import search_recent_business_report, fetch_business_section
            # corp_descriptions 에서 corp_code 가져옴 (DART 8자리)
            from ._section_extract import _connect
            with _connect() as conn:
                cur = conn.execute(
                    "SELECT corp_code FROM corp_descriptions WHERE ticker=?",
                    (ticker,),
                )
                row = cur.fetchone()
            if row and row[0]:
                rep = search_recent_business_report(row[0])
                if rep and rep.rcept_no:
                    dart_section = fetch_business_section(rep.rcept_no)
        except Exception:
            dart_section = None

    return {
        "overview": overview,
        "ir_articles": ir_articles,
        "dart_section": dart_section,
    }


def render_markdown(extracted: dict, **kwargs) -> str:
    """extract() 결과를 markdown 으로 렌더."""
    overview = extracted.get("overview")
    if overview is None:
        return "_section_text 매치 실패 — corp_embeddings.db 미빌드 또는 종목 코드 불일치._\n"
    return render_business_model(
        overview,
        ir_articles=extracted.get("ir_articles"),
        **kwargs,
    )
