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


# PF 사업의 우발채무 — 시행사(PFV·조합)의 차입에 시공사가 보증을 서는 구조라
# 재무제표 부채에는 안 잡히고 "타인에대한채무보증결정" 공시로만 드러난다.
# 건설사 리스크의 본체가 여기 있는데 지금까지 금액이 파싱되지 않았다.
# 채무자 **이름만** 보는 휴리스틱이다 — PF 시행사는 대개 SPC/PFV/조합 형태로 이름에
# 흔적이 남는다. 이름에 안 드러나는 SPC 는 놓친다(false negative). 판정이 아니라
# '이건 PF 냐'를 사람이 확인할 후보 표식으로만 쓴다.
_PF_HINTS = (
    "PFV", "피에프브이", "프로젝트금융", "PF", "정비사업조합", "조합", "개발",
    "유한회사", "(유)", "제일차", "제이차", "유동화", "SPC", "에스피씨", "위탁관리",
)

# 다음 항목 라벨 — 값이 뒤 라벨까지 흘러넘치는 걸 여기서 자른다.
_G_NEXT_LABEL = re.compile(
    r"\s*(?:\d+\.\s*)?(?:회사와의\s*관계|채권자|채무자|채무\(차입\)금액|채무보증내역|"
    r"채무보증금액|자기자본|자기자본대비|대규모법인여부|채무보증기간|채무보증\s*총\s*잔액|"
    r"시작일|종료일|이사회결의일|기타)"
)


def _cut_at_next_label(s: Optional[str]) -> Optional[str]:
    """라벨 뒤 텍스트에서 '다음 라벨' 이후를 잘라낸다."""
    if not s:
        return s
    m = _G_NEXT_LABEL.search(s)
    return (s[: m.start()] if m else s).strip(" :·-") or None


def _extract_ratio_after(text: str, labels: list[str], window: int = 80) -> Optional[float]:
    """라벨 뒤의 퍼센트 값(소수 허용) 추출.

    _extract_number_after 는 4자리 이상/콤마 숫자만 잡으므로 '9.5' 같은 비율을 건너뛰고
    뒤따르는 날짜의 연도(2026)를 집어온다 — 비율은 전용 추출기가 필요하다.
    """
    for kw in labels:
        idx = text.find(kw)
        if idx == -1:
            continue
        chunk = text[idx + len(kw) : idx + len(kw) + window]
        m = re.search(r"(\d{1,3}(?:\.\d+)?)\s*%?", chunk)
        if m:
            try:
                return float(m.group(1))
            except ValueError:
                continue
    return None


def parse_guarantee(html: str) -> dict:
    """타인에대한채무보증결정 본문 → 보증 금액·상대·기간·총잔액.

    핵심 필드는 **채무보증 총 잔액**이다 — 건당 금액이 아니라 이 회사가 지금 지고 있는
    우발채무의 총합이고, 자기자본과 대비해야 의미가 산다.
    """
    out: dict = {
        "debtor":               None,   # 채무자 (시행사)
        "debtor_relation":      None,   # 회사와의 관계
        "creditor":             None,   # 채권자 (금융기관)
        "debt_amount":          None,   # 채무(차입)금액
        "guarantee_amount":     None,   # 채무보증금액
        "guarantee_amount_str": None,
        "equity":               None,   # 자기자본
        "ratio_to_equity":      None,   # 자기자본대비(%)
        "total_guarantee_balance": None,  # 채무보증 총 잔액 ★
        "period_start":         None,
        "period_end":           None,
        "is_pf":                None,   # 채무자명으로 본 PF 추정
    }
    if not html:
        return out

    text = _strip_tags(html) if "<" in html else html

    out["debtor"] = _cut_at_next_label(
        _extract_text_after(text, ["1. 채무자", "채무자"], window=120)
    )
    out["debtor_relation"] = _cut_at_next_label(
        _extract_text_after(text, ["회사와의 관계", "회사와의관계"], window=80)
    )
    out["creditor"] = _cut_at_next_label(
        _extract_text_after(text, ["2. 채권자", "채권자"], window=120)
    )

    out["debt_amount"] = _to_int(
        _extract_number_after(text, ["채무(차입)금액(원)", "채무(차입)금액", "채무금액"])
    )

    g_str = _extract_number_after(text, ["채무보증금액(원)", "채무보증금액"])
    if g_str:
        out["guarantee_amount_str"] = g_str[:60]
        out["guarantee_amount"] = _to_int(g_str)

    out["equity"] = _to_int(_extract_number_after(text, ["자기자본(원)", "자기자본"]))

    out["ratio_to_equity"] = _extract_ratio_after(
        text, ["자기자본대비(%)", "자기자본대비", "자기자본 대비"]
    )

    out["total_guarantee_balance"] = _to_int(
        _extract_number_after(
            text, ["채무보증 총 잔액(원)", "채무보증총잔액(원)", "채무보증 총 잔액", "채무보증총잔액"]
        )
    )

    # 날짜만 받는다 — 못 찾으면 None. (예전엔 다음 항목 텍스트를 날짜라고 넣었다.)
    for label, key in (("시작일", "period_start"), ("종료일", "period_end")):
        val = _extract_text_after(text, [label], window=60)
        if val:
            m = re.search(r"\d{4}[-.]\d{2}[-.]\d{2}", val)
            out[key] = m.group(0).replace(".", "-") if m else None

    if out["debtor"]:
        out["is_pf"] = any(h in out["debtor"] for h in _PF_HINTS)

    return out
