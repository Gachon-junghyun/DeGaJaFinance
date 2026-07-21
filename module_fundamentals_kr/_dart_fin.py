# -*- coding: utf-8 -*-
"""DART 전체 재무제표(fnlttSinglAcntAll) fetch — KR 재무제표의 단일 원본.

왜 이 파일이 있나: module_fundamentals_us 는 US 전용(yfinance/SEC XBRL)이라 KR 종목의
재무제표를 볼 수단이 리포에 **아예 없었다**. 그래서 "수익의 질"(발생액·미청구공사)을
검증 못 하고 LLM 이 손으로 추정해 왔다(llm_outputs/*/real_alpha_kr/*).

계정 식별은 **account_id(IFRS 표준태그) 우선, 한글명은 폴백**이다 — 실측 결과 현대건설
209개 계정 중 표준코드 미사용은 12개뿐이고, 반대로 한글명은 회사마다 제각각이다
("매출액" vs "수익(매출액)", IS 가 비고 CIS 만 있는 회사 등). 이름으로 매칭하면 조용히
빗나간다.

의존성: requests + 표준라이브러리. corp_code 해석은 module_disclosure 재사용(P1).
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Optional

import requests

API_URL = "https://opendart.fss.or.kr/api/fnlttSinglAcntAll.json"

# 보고서 코드 (DART)
REPRT_CODES = {
    "annual": "11011",   # 사업보고서
    "half": "11012",     # 반기보고서
    "q1": "11013",       # 1분기보고서
    "q3": "11014",       # 3분기보고서
}

# 표준 IFRS/DART 태그 → 우리가 쓰는 키.
# 실측(현대건설 000720 / 대우건설 047040 2025 사업보고서)으로 확인한 태그만 넣는다.
ACCOUNT_IDS: dict[str, tuple[str, ...]] = {
    "revenue": ("ifrs-full_Revenue",),
    "operating_income": ("dart_OperatingIncomeLoss", "ifrs-full_ProfitLossFromOperatingActivities"),
    "gross_profit": ("ifrs-full_GrossProfit",),
    "net_income": ("ifrs-full_ProfitLoss",),
    "ocf": ("ifrs-full_CashFlowsFromUsedInOperatingActivities",),
    "icf": ("ifrs-full_CashFlowsFromUsedInInvestingActivities",),
    "fcf_fin": ("ifrs-full_CashFlowsFromUsedInFinancingActivities",),
    # 건설·조선 등 수주산업의 핵심 — 진행률 인식의 잔여물
    "unbilled": ("ifrs-full_CurrentContractAssets",),          # 미청구공사(계약자산)
    "overbilled": ("dart_ShortTermDueToCustomersForContractWork",),  # 초과청구공사(계약부채)
    "receivables": ("ifrs-full_CurrentTradeReceivables", "dart_ShortTermTradeReceivable"),
    "inventory": ("ifrs-full_Inventories",),
    "total_assets": ("ifrs-full_Assets",),
    "total_equity": ("ifrs-full_Equity",),
    "total_liabilities": ("ifrs-full_Liabilities",),
}

# account_id 가 '-표준계정코드 미사용-' 인 회사용 한글명 폴백.
#
# **정확일치**로 본다(정규화 후 ==). 부분일치는 조용히 틀린다 — 실측으로 확인:
#   "계약자산"  ⊂ "보험계약자산"(ifrs-full_InsuranceContractsIssuedThatAreAssets) → 은행/보험사에
#                 있지도 않은 미청구공사가 잡혔다
#   "영업수익"  ⊂ "기타영업수익"(dart_OtherOperatingIncome) → 매출이 통째로 틀렸다
# 계정 209개 중 표준코드 미사용은 12개뿐이라 폴백은 예외 경로다. 못 찾으면 None 이 낫다
# (지표가 비는 건 보이지만, 틀린 숫자는 안 보인다).
ACCOUNT_NAMES: dict[str, tuple[str, ...]] = {
    "revenue": ("수익(매출액)", "매출액", "매출", "영업수익"),
    "operating_income": ("영업이익(손실)", "영업이익", "영업이익(손실)"),
    "gross_profit": ("매출총이익", "매출총이익(손실)"),
    "net_income": ("당기순이익(손실)", "당기순이익", "분기순이익", "반기순이익"),
    "ocf": ("영업활동현금흐름", "영업활동으로인한현금흐름", "영업활동으로 인한 현금흐름"),
    "icf": ("투자활동현금흐름", "투자활동으로인한현금흐름", "투자활동으로 인한 현금흐름"),
    "fcf_fin": ("재무활동현금흐름", "재무활동으로인한현금흐름", "재무활동으로 인한 현금흐름"),
    # "계약자산"만 단독으로 두지 않는다 — 보험계약자산과 구분이 안 된다.
    "unbilled": ("미청구공사", "미청구공사(계약자산)", "계약자산(미청구공사)"),
    "overbilled": ("초과청구공사", "초과청구공사(계약부채)", "계약부채(초과청구공사)"),
    "receivables": ("매출채권", "매출채권및기타채권", "매출채권 및 기타채권"),
    "inventory": ("재고자산",),
    "total_assets": ("자산총계",),
    "total_equity": ("자본총계",),
    "total_liabilities": ("부채총계",),
}


@dataclass
class Account:
    key: str
    account_nm: str
    account_id: str
    sj_div: str
    current: Optional[float]   # 당기
    previous: Optional[float]  # 전기
    matched_by: str            # "id" | "name"


@dataclass
class Financials:
    corp_code: str
    corp_name: str
    stock_code: str
    bsns_year: str
    reprt_code: str
    fs_div: str                       # CFS(연결) | OFS(별도)
    accounts: dict[str, Account] = field(default_factory=dict)
    raw_count: int = 0

    def value(self, key: str) -> Optional[float]:
        a = self.accounts.get(key)
        return a.current if a else None

    def prev(self, key: str) -> Optional[float]:
        a = self.accounts.get(key)
        return a.previous if a else None


def _api_key() -> Optional[str]:
    return os.environ.get("DART_API_KEY", "").strip() or None


def _num(raw: object) -> Optional[float]:
    """DART 금액 문자열 → float. 빈값/'-'/'−' 는 None."""
    if raw is None:
        return None
    s = str(raw).strip().replace(",", "").replace("−", "-")
    if not s or s in {"-", "--"}:
        return None
    try:
        return float(s)
    except ValueError:
        return None


def _norm(s: str) -> str:
    return "".join(str(s).split())


def _fetch_raw(corp_code: str, year: str, reprt_code: str, fs_div: str) -> list[dict]:
    key = _api_key()
    if not key:
        raise RuntimeError("DART_API_KEY 미설정 — .env 를 확인하라")
    r = requests.get(
        API_URL,
        params={
            "crtfc_key": key,
            "corp_code": corp_code,
            "bsns_year": year,
            "reprt_code": reprt_code,
            "fs_div": fs_div,
        },
        timeout=30,
    )
    r.raise_for_status()
    data = r.json()
    if data.get("status") != "000":
        return []
    return data.get("list", []) or []


def _extract(rows: list[dict]) -> dict[str, Account]:
    """계정 행 → 우리 키 사전. account_id 우선, 없으면 한글명 부분일치."""
    by_id: dict[str, dict] = {}
    for row in rows:
        aid = (row.get("account_id") or "").strip()
        if aid and aid not in by_id:
            by_id[aid] = row

    out: dict[str, Account] = {}
    for key, ids in ACCOUNT_IDS.items():
        for aid in ids:
            row = by_id.get(aid)
            if row is None:
                continue
            out[key] = Account(
                key=key,
                account_nm=row.get("account_nm", ""),
                account_id=aid,
                sj_div=row.get("sj_div", ""),
                current=_num(row.get("thstrm_amount")),
                previous=_num(row.get("frmtrm_amount")),
                matched_by="id",
            )
            break

    # 표준코드 미사용 회사 폴백
    for key, names in ACCOUNT_NAMES.items():
        if key in out:
            continue
        for want in names:
            wn = _norm(want)
            for row in rows:
                if wn and wn == _norm(row.get("account_nm", "")):
                    out[key] = Account(
                        key=key,
                        account_nm=row.get("account_nm", ""),
                        account_id=(row.get("account_id") or "").strip(),
                        sj_div=row.get("sj_div", ""),
                        current=_num(row.get("thstrm_amount")),
                        previous=_num(row.get("frmtrm_amount")),
                        matched_by="name",
                    )
                    break
            if key in out:
                break
    return out


def fetch_financials(
    corp_code: str,
    *,
    corp_name: str = "",
    stock_code: str = "",
    year: Optional[str] = None,
    period: str = "annual",
    fs_div: str = "CFS",
    year_fallback: int = 2,
) -> Optional[Financials]:
    """corp_code(8자리) → 전체 재무제표.

    연결(CFS)이 비면 별도(OFS)로, 요청 연도가 비면 최대 `year_fallback` 년 뒤로 물러난다
    (사업보고서는 회계연도 종료 후 3개월 뒤 공시 → 연초엔 당해 연도가 항상 빈다).
    """
    from datetime import datetime

    reprt_code = REPRT_CODES.get(period, period)
    base_year = int(year) if year else datetime.now().year

    for back in range(year_fallback + 1):
        y = str(base_year - back)
        for div in ([fs_div, "OFS"] if fs_div == "CFS" else [fs_div]):
            rows = _fetch_raw(corp_code, y, reprt_code, div)
            if not rows:
                continue
            accounts = _extract(rows)
            if not accounts:
                continue
            return Financials(
                corp_code=corp_code,
                corp_name=corp_name,
                stock_code=stock_code,
                bsns_year=y,
                reprt_code=reprt_code,
                fs_div=div,
                accounts=accounts,
                raw_count=len(rows),
            )
    return None


def fetch_by_stock(
    stock_or_name: str,
    **kwargs,
) -> Optional[Financials]:
    """종목코드/기업명 → 재무제표. corp_code 해석은 module_disclosure 재사용(P1)."""
    from module_disclosure import resolve_corp_code

    resolved = resolve_corp_code(stock_or_name)
    if not resolved:
        return None
    corp_code, corp_name = resolved
    return fetch_financials(
        corp_code,
        corp_name=corp_name,
        stock_code=stock_or_name if stock_or_name.isdigit() else "",
        **kwargs,
    )
