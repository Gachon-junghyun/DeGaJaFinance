"""공시 본문 HTML에서 카테고리별 핵심 필드 추출.

DART HTML은 <table> 격자 구조라 BeautifulSoup의 td 인접 추출이 단순 정규식보다 안전하다.
표가 깨졌거나 키워드가 없는 경우 정규식 fallback을 사용한다.
모든 함수는 dict 반환 (실패 키는 None).
"""
from __future__ import annotations

import re
import warnings
from typing import Optional

try:
    from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
    warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
    _HAS_BS4 = True
except ImportError:
    _HAS_BS4 = False


# ── 공통 헬퍼 ───────────────────────────────────────────────

def _strip_tags(s: str) -> str:
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"<[^>]*$", "", s)
    return re.sub(r"\s+", " ", s).strip()


def _regex_after(html: str, keyword: str, max_len: int = 300) -> Optional[str]:
    """keyword 직후 max_len 문자에서 HTML 태그 제거 후 반환."""
    idx = html.find(keyword)
    if idx == -1:
        return None
    snippet = _strip_tags(html[idx + len(keyword) : idx + len(keyword) + max_len])
    return snippet[:200] if snippet else None


def _extract_number_after(html: str, label_keywords: list[str], window: int = 250) -> Optional[str]:
    """라벨 뒤 window 안의 첫 번째 큰 숫자(콤마 포함, 4자리 이상)를 반환.

    DART 본문은 '취득예정금액(원) | 보통주식 | 130,481,024,000' 식의 다중 셀이라
    라벨 + 인접 셀 추출이 빗나가기 쉽다. 라벨 직후 window 안의 첫 큰 숫자를 잡는 게 더 강건.
    """
    for kw in label_keywords:
        idx = html.find(kw)
        if idx == -1:
            continue
        chunk = html[idx + len(kw) : idx + len(kw) + window]
        chunk = _strip_tags(chunk)
        m = re.search(r"(\d{1,3}(?:,\d{3})+|\d{4,})(?:\s*(?:원|주|%))?", chunk)
        if m:
            return m.group(0)
    return None


def _extract_text_after(html: str, label_keywords: list[str], window: int = 200) -> Optional[str]:
    """라벨 뒤 window 안의 텍스트(숫자 아님)를 반환."""
    for kw in label_keywords:
        idx = html.find(kw)
        if idx == -1:
            continue
        chunk = html[idx + len(kw) : idx + len(kw) + window]
        chunk = _strip_tags(chunk)
        chunk = re.sub(r"^[\s\-:|]+", "", chunk)
        if chunk:
            return chunk[:120]
    return None


def _parse_amount_won(text: str) -> Optional[int]:
    """'85,000,000,000원' 또는 '850억' → 850_0000_0000 (원 단위)."""
    if not text:
        return None
    s = text.replace(",", "").replace(" ", "")

    m = re.search(r"(\d+(?:\.\d+)?)\s*조", s)
    if m:
        return int(float(m.group(1)) * 10**12)
    m = re.search(r"(\d+(?:\.\d+)?)\s*억", s)
    if m:
        return int(float(m.group(1)) * 10**8)
    m = re.search(r"(\d{6,})", s)
    if m:
        return int(m.group(1))
    return None


# ── 카테고리별 파서 ─────────────────────────────────────────

def _to_int(num_str: Optional[str]) -> Optional[int]:
    if not num_str:
        return None
    s = re.sub(r"[^\d]", "", num_str)
    return int(s) if s else None


def parse_contract(html: str) -> dict:
    """단일판매·공급계약 본문에서 핵심 필드 추출."""
    out: dict = {
        "contract_amount":     None,
        "contract_amount_str": None,
        "counterparty":        None,
        "ratio_to_revenue":    None,
        "period":              None,
        "subject":             None,
    }
    if not html:
        return out

    amt_str = _extract_number_after(html, ["계약금액(원)", "계약금액", "공급금액"])
    if amt_str:
        out["contract_amount_str"] = amt_str[:60]
        out["contract_amount"]     = _to_int(amt_str)

    party = _extract_text_after(html, ["계약상대", "거래상대"])
    if party:
        out["counterparty"] = party[:60]

    ratio_str = _extract_number_after(
        html, ["매출액 대비(%)", "매출액대비", "매출액 대비", "최근 매출액 대비"]
    )
    if ratio_str:
        m = re.search(r"(\d+(?:\.\d+)?)", ratio_str)
        if m:
            try:
                out["ratio_to_revenue"] = float(m.group(1))
            except ValueError:
                pass

    period = _extract_text_after(html, ["계약기간", "납기일", "납품기한"])
    if period:
        out["period"] = period[:60]

    subj = _extract_text_after(
        html, ["판매ㆍ공급계약 내용", "판매·공급계약 내용", "계약 내용", "계약내용", "공급내용"]
    )
    if subj:
        out["subject"] = subj[:120]

    return out


def parse_treasury(html: str) -> dict:
    """자기주식 취득/처분/소각 본문."""
    out: dict = {
        "shares":     None,
        "amount":     None,
        "amount_str": None,
        "method":     None,
        "purpose":    None,
        "period":     None,
    }
    if not html:
        return out

    shr_str = _extract_number_after(html, [
        "취득예정주식", "취득할주식", "처분예정주식", "처분할주식",
        "소각할주식", "소각예정주식", "1. 취득예정주식",
    ])
    out["shares"] = _to_int(shr_str)

    amt_str = _extract_number_after(html, [
        "취득예정금액", "취득금액", "처분예정금액", "처분금액",
        "2. 취득예정금액",
    ])
    if amt_str:
        out["amount_str"] = amt_str[:60]
        out["amount"]     = _to_int(amt_str)

    method = _extract_text_after(html, ["6. 취득방법", "취득방법", "처분방법"])
    if method:
        out["method"] = method[:60]

    purp = _extract_text_after(html, ["5. 취득목적", "취득목적", "처분목적", "소각목적"])
    if purp:
        out["purpose"] = purp[:80]

    period = _extract_text_after(html, [
        "3. 취득예정기간", "취득예정기간", "처분예정기간", "소각예정일",
    ])
    if period:
        out["period"] = period[:60]

    return out


def parse_capital(html: str) -> dict:
    """유증/CB/BW/합병/분할 본문에서 발행 규모/사용목적 추출."""
    out: dict = {
        "issue_amount":     None,
        "issue_amount_str": None,
        "shares":           None,
        "purpose":          None,
        "method":           None,
    }
    if not html:
        return out

    amt_str = _extract_number_after(html, [
        "발행총액", "발행금액", "사채의 권면총액", "권면총액", "사채총액",
        "신주발행가액 총액",
    ])
    if amt_str:
        out["issue_amount_str"] = amt_str[:60]
        out["issue_amount"]     = _to_int(amt_str)

    shr_str = _extract_number_after(html, [
        "신주의수", "신주의 수", "발행주식수", "신주발행주식수",
    ])
    out["shares"] = _to_int(shr_str)

    purp = _extract_text_after(html, [
        "자금사용목적", "자금의 사용목적", "자금조달목적",
    ])
    if purp:
        out["purpose"] = purp[:80]

    method = _extract_text_after(html, [
        "증자방식", "발행방식", "신주의 배정방법",
    ])
    if method:
        out["method"] = method[:60]

    return out
