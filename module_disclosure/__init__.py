"""DART 공시 카테고리별 수집·요약 모듈.

리포트 파이프라인의 §6 (뉴스 검색) / §7-A (밸류에이션) 옆에 끼워 넣어
종목별 단기 catalyst (수주·자사주·자본변동·지분변동·실적)를 한 번에 본다.

빠른 사용:
    from module_disclosure import fetch_disclosures, render_markdown, summarize_contracts

    rows = fetch_disclosures("034020", days=60)
    contracts = summarize_contracts(rows, ytd_guidance_jo=13.3)
    print(render_markdown("034020", "두산에너빌리티", rows, contracts))

CLI:
    python -m module_disclosure 034020 --days 60
    python -m module_disclosure 034020 --days 60 --guidance 13.3 --out llm_outputs/disclosure_034020.md
    python -m module_disclosure 034020 --category contract --json

데이터 소스: OpenDART API (https://opendart.fss.or.kr).
DART_API_KEY 환경변수가 필요하다 (.env 또는 셸 환경).
"""
from ._dart_api import (
    DisclosureRow,
    fetch_disclosures,
    fetch_disclosure_detail,
    fetch_disclosure_detail_all,
)
from ._corp_codes import resolve_corp_code, refresh_corp_codes
from ._categorizer import categorize, CATEGORIES, CATEGORY_LABELS
from ._detail_parser import (
    parse_contract,
    parse_treasury,
    parse_capital,
    parse_guarantee,
)
from ._renderer import (
    render_markdown,
    summarize_contracts,
    ContractSummary,
)
from ._business_report import (
    DartReport,
    TocNode,
    fetch_business_report,
    search_recent_business_report,
    fetch_business_section,
    fetch_toc,
    fetch_toc_section,
)

__all__ = [
    "CATEGORY_LABELS",
    "TocNode",
    "fetch_toc",
    "fetch_toc_section",
    "parse_guarantee",
    "DisclosureRow",
    "fetch_disclosures",
    "fetch_disclosure_detail",
    "fetch_disclosure_detail_all",
    "resolve_corp_code",
    "refresh_corp_codes",
    "categorize",
    "CATEGORIES",
    "parse_contract",
    "parse_treasury",
    "parse_capital",
    "render_markdown",
    "summarize_contracts",
    "ContractSummary",
    # DART 사업보고서 "II. 사업의 내용" (옛 module_business 흡수)
    "DartReport",
    "fetch_business_report",
    "search_recent_business_report",
    "fetch_business_section",
]
