"""edgartools wrapper: ticker -> 10-K / 10-Q sections.

API 사용 (edgartools 5.31.5 기준, 2026-05 검증):
    Company(ticker)                                  # CompanyNotFoundError on bad ticker
    Company.get_filings(form="10-K").latest()        # -> EntityFiling (metadata)
    EntityFiling.accession_no / filing_date / filing_url / homepage_url
    EntityFiling.obj()                               # -> TenK | TenQ
    TenK.business / .risk_factors / .management_discussion   # str
    TenK.items                                       # list[str]
    TenK.get_item_with_part(part, item, markdown=True)
    TenQ.get_item_with_part(part, item)              # 10-Q 는 직접 attribute 없음

fallback (edgartools API 깨질 때):
    https://www.sec.gov/Archives/... 본문 HTML 직접 다운로드 -> BS4 -> regex
    "Item 1[A]?\\. " anchor 로 split.
"""
from __future__ import annotations

import os
import re
import sys
import time
from dataclasses import dataclass, field
from typing import Optional

SEC_USER_AGENT = os.environ.get(
    "SEC_USER_AGENT",
    "mvp Research fivepeople201@gmail.com",
)
SEC_RATE_SLEEP_SEC = 0.5

# 각 섹션의 자수 cap (--full 옵션 적용 시).
_FULL_CAP = 50_000
# 비-full 모드일 때 본문에서 잘라낼 자수.
_BUSINESS_PRIMARY_CHARS = 1500
_BUSINESS_CUSTOMER_CHARS = 800
_MDNA_REVENUE_CHARS = 1500
_MDNA_OUTLOOK_CHARS = 800
# Risk Factors 요약에서 추출할 bullet 개수.
_RISK_BULLET_COUNT = 10


class EdgartoolsMissingError(RuntimeError):
    """edgartools 미설치 시 raise."""


@dataclass
class ExtractResult:
    ticker: str
    company_name: str
    form: str
    filing_date: str
    accession_no: str
    period_of_report: str
    filing_url: str
    homepage_url: str
    # 섹션 본문 (full=True 면 통째 / full=False 면 비-Risk 섹션은 잘림).
    business: str = ""
    risk_factors: str = ""
    risk_summary_bullets: list[str] = field(default_factory=list)
    mdna: str = ""
    # 추가 derived 본문 — render 시 사용.
    business_primary: str = ""
    business_customer: str = ""
    mdna_revenue: str = ""
    mdna_outlook: str = ""
    # debug.
    fallback_used: bool = False
    notes: list[str] = field(default_factory=list)


def _ensure_edgartools():
    try:
        from edgar import Company, set_identity  # noqa: F401
        return Company, set_identity
    except ImportError as e:
        raise EdgartoolsMissingError(
            "edgartools 가 설치되지 않았습니다. `pip install edgartools` 실행 후 다시 시도하세요."
        ) from e


def _normalize_text(s: str) -> str:
    """edgartools 결과의 (��) 같은 깨진 문자/제어문자/연속공백 정리."""
    if not s:
        return ""
    # smart quote 깨짐을 ASCII 대체.
    s = s.replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"')
    s = s.replace("–", "-").replace("—", "--")
    s = s.replace("…", "...")
    # � (��) 는 인용부호 깨짐 -> 그냥 ' 로.
    s = re.sub(r"�+", "'", s)
    # 연속 빈 줄 3+ -> 2.
    s = re.sub(r"\n{3,}", "\n\n", s)
    # tab -> space.
    s = s.replace("\t", "    ")
    return s.strip()


def _slice_paragraphs(text: str, *, max_chars: int) -> str:
    """단락 경계에서 잘라 max_chars 이내로."""
    text = text.strip()
    if len(text) <= max_chars:
        return text
    cut = text[:max_chars]
    # 마지막 단락 break 에서 자른다.
    idx = cut.rfind("\n\n")
    if idx > max_chars * 0.6:
        return cut[:idx].rstrip()
    # 문장 단위 fallback.
    idx = cut.rfind(". ")
    if idx > max_chars * 0.7:
        return cut[: idx + 1].rstrip()
    return cut.rstrip() + "..."


def _find_anchor_paragraph(
    text: str,
    keywords: list[str],
    *,
    max_chars: int,
) -> str:
    """text 에서 keywords 중 하나가 처음 등장하는 단락부터 max_chars 분량 추출."""
    if not text:
        return ""
    low = text.lower()
    best_pos = -1
    for kw in keywords:
        p = low.find(kw.lower())
        if p == -1:
            continue
        if best_pos == -1 or p < best_pos:
            best_pos = p
    if best_pos == -1:
        return ""
    # 단락 시작으로 back-fill.
    para_start = text.rfind("\n\n", 0, best_pos)
    if para_start == -1:
        para_start = 0
    else:
        para_start += 2
    chunk = text[para_start : para_start + max_chars]
    return _slice_paragraphs(chunk, max_chars=max_chars)


# Risk Factors 의 *bold 헤더 또는 itemize* 첫 줄 추출.
# edgartools 결과의 risk_factors 텍스트는 일반적으로 각 리스크 헤더를 단락 첫 줄에 배치.
# 예: "Demand for our products may not grow as expected."
#     followed by 2-3 paragraphs of explanation.
_RISK_HEADER_LINE_PAT = re.compile(r"^[A-Z][^.\n]{20,200}[.?!]$", re.MULTILINE)


def _extract_risk_summary_bullets(risk_text: str, count: int = _RISK_BULLET_COUNT) -> list[str]:
    """Risk Factors 본문에서 *각 리스크의 헤더 한 줄*들을 추출.

    전략 (우선순위):
        1) 명시적 bullet 마커 (•, ▪, ●, ■) 로 시작하는 줄 — 많은 10-K 가
           Risk Factors Summary 섹션에 이런 bullet list 를 제공한다.
        2) 단락 첫 줄이 헤더 모양 (대문자 시작, 마침표/물음표로 끝, 20-250자).
    """
    if not risk_text:
        return []
    bullets: list[str] = []
    seen: set[str] = set()

    # --- 1) explicit bullet marker (•, ▪, ●, ■, *, -) ---
    bullet_pat = re.compile(r"^\s*[•▪●■\*\-]\s*(.+)$", re.MULTILINE)
    for m in bullet_pat.finditer(risk_text):
        line = m.group(1).strip()
        # 너무 짧거나 너무 김 skip.
        if len(line) < 15 or len(line) > 400:
            continue
        # 마침표 없으면 추가.
        if not line.endswith((".", "?", "!")):
            # 다음 줄에 이어지는지 — 단순화: 무시.
            line = line.rstrip(",;:") + "."
        key = line.lower()[:80]
        if key in seen:
            continue
        seen.add(key)
        bullets.append(line)
        if len(bullets) >= count:
            return bullets

    # --- 2) header-line heuristic ---
    for para in re.split(r"\n\s*\n", risk_text):
        para = para.strip()
        if not para:
            continue
        first_line = para.split("\n", 1)[0].strip()
        low = first_line.lower()
        if "item 1a" in low or low.startswith("the following") or low.startswith("additional risks"):
            continue
        if low.startswith("risk factors") or low.startswith("risks related"):
            continue
        if len(first_line) < 20 or len(first_line) > 250:
            continue
        if not first_line[0].isupper():
            continue
        if not first_line.rstrip().endswith((".", "?", "!")):
            continue
        if len(para) <= len(first_line) + 50:
            continue
        key = first_line.lower()[:80]
        if key in seen:
            continue
        seen.add(key)
        bullets.append(first_line)
        if len(bullets) >= count:
            break
    return bullets


# --------------------------------------------------------------------------- #
# Fallback: raw EDGAR HTML 다운로드 -> BS4 -> regex.
# --------------------------------------------------------------------------- #

_ITEM_HEADER_PAT = re.compile(
    r"\bItem\s+(?P<num>1A?|7)\.?\s*[\-–—:]?\s*"
    r"(?P<title>Business|Risk Factors|Management[''’]s Discussion|Management Discussion)",
    re.IGNORECASE,
)


def _fallback_fetch_html(filing_url: str) -> str:
    import requests  # noqa: F401  (local import to keep top-level light)
    headers = {
        "User-Agent": SEC_USER_AGENT,
        "Accept-Encoding": "gzip, deflate",
        "Host": "www.sec.gov",
    }
    r = requests.get(filing_url, headers=headers, timeout=30)
    r.raise_for_status()
    time.sleep(SEC_RATE_SLEEP_SEC)
    return r.text


def _fallback_extract_sections(html: str) -> dict[str, str]:
    """HTML 에서 Item 1 / 1A / 7 본문 추출 (BS4)."""
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text("\n", strip=True)
    # 모든 anchor 매치.
    matches = list(_ITEM_HEADER_PAT.finditer(text))
    out: dict[str, str] = {}
    if not matches:
        return out
    for i, m in enumerate(matches):
        num = m.group("num").upper()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        key = {"1": "business", "1A": "risk_factors", "7": "mdna"}.get(num)
        if key and (key not in out or len(body) > len(out[key])):
            out[key] = body
    return out


# --------------------------------------------------------------------------- #
# Main entry.
# --------------------------------------------------------------------------- #

def extract_business_us(
    ticker: str,
    *,
    form: str = "10-K",
    full: bool = False,
) -> Optional[ExtractResult]:
    """ticker -> ExtractResult."""
    ticker = ticker.upper().strip()
    if form.upper() not in ("10-K", "10-Q"):
        raise ValueError(f"form must be 10-K or 10-Q, got {form!r}")
    form = form.upper()

    Company, set_identity = _ensure_edgartools()
    set_identity(SEC_USER_AGENT)

    # 1) Company lookup.
    try:
        company = Company(ticker)
    except Exception as e:
        # CompanyNotFoundError 또는 네트워크 에러.
        print(f"[module_business_us] ticker '{ticker}' lookup failed: {e}", file=sys.stderr)
        return None

    # 2) latest filing.
    try:
        filings = company.get_filings(form=form)
        time.sleep(SEC_RATE_SLEEP_SEC)
        filing = filings.latest()
    except Exception as e:
        print(f"[module_business_us] {ticker} get_filings({form}) failed: {e}", file=sys.stderr)
        return None
    if filing is None:
        print(f"[module_business_us] {ticker}: no {form} filing found", file=sys.stderr)
        return None

    accession = getattr(filing, "accession_no", "") or getattr(filing, "accession_number", "")
    filing_date = str(getattr(filing, "filing_date", ""))
    filing_url = getattr(filing, "filing_url", "") or ""
    homepage_url = getattr(filing, "homepage_url", "") or ""

    company_name = getattr(company, "display_name", "") or getattr(company, "name", "") or ticker

    result = ExtractResult(
        ticker=ticker,
        company_name=company_name,
        form=form,
        filing_date=filing_date,
        accession_no=accession,
        period_of_report="",
        filing_url=filing_url,
        homepage_url=homepage_url,
    )

    # 3) section access — TenK vs TenQ.
    business_raw = risk_raw = mdna_raw = ""
    try:
        obj = filing.obj()
        time.sleep(SEC_RATE_SLEEP_SEC)
        result.period_of_report = str(getattr(obj, "period_of_report", "") or "")

        if form == "10-K":
            # direct attributes.
            business_raw = getattr(obj, "business", None) or ""
            risk_raw = getattr(obj, "risk_factors", None) or ""
            mdna_raw = getattr(obj, "management_discussion", None) or ""
            # fallback to get_item_with_part if 빈 값.
            if not business_raw and hasattr(obj, "get_item_with_part"):
                business_raw = obj.get_item_with_part("Part I", "Item 1") or ""
            if not risk_raw and hasattr(obj, "get_item_with_part"):
                risk_raw = obj.get_item_with_part("Part I", "Item 1A") or ""
            if not mdna_raw and hasattr(obj, "get_item_with_part"):
                mdna_raw = obj.get_item_with_part("Part II", "Item 7") or ""
        else:  # 10-Q
            # 10-Q 에는 Item 1 (Business) 가 없음.
            # MD&A = Part I, Item 2. Risk Factors = Part II, Item 1A.
            if hasattr(obj, "get_item_with_part"):
                mdna_raw = obj.get_item_with_part("Part I", "Item 2") or ""
                risk_raw = obj.get_item_with_part("Part II", "Item 1A") or ""
            # business 는 없음.
            business_raw = ""
            result.notes.append(
                "10-Q 는 Item 1 (Business) 본문이 없습니다. "
                "사업 설명 본문은 10-K (`--form 10-K`) 에서만 추출 가능합니다."
            )
    except Exception as e:
        print(f"[module_business_us] {ticker} section extract failed: {e}; trying fallback", file=sys.stderr)
        result.notes.append(f"edgartools section access failed: {e}")

    # 4) Fallback (edgartools 결과가 비어있을 때).
    need_fallback = (
        (form == "10-K" and not (business_raw and risk_raw and mdna_raw))
        or (form == "10-Q" and not (mdna_raw or risk_raw))
    )
    if need_fallback and filing_url:
        try:
            html = _fallback_fetch_html(filing_url)
            secs = _fallback_extract_sections(html)
            if not business_raw:
                business_raw = secs.get("business", business_raw)
            if not risk_raw:
                risk_raw = secs.get("risk_factors", risk_raw)
            if not mdna_raw:
                mdna_raw = secs.get("mdna", mdna_raw)
            result.fallback_used = True
            result.notes.append("edgartools section 본문 비어 BS4 fallback 동원.")
        except Exception as e:
            result.notes.append(f"fallback fetch 실패: {e}")

    # 5) normalize.
    business_raw = _normalize_text(business_raw)
    risk_raw = _normalize_text(risk_raw)
    mdna_raw = _normalize_text(mdna_raw)

    # 6) derived 본문 추출 (비-full 모드용).
    if business_raw:
        # 주요 제품·시장 = 본문 앞 N자.
        result.business_primary = _slice_paragraphs(business_raw, max_chars=_BUSINESS_PRIMARY_CHARS)
        # 주요 고객·경쟁 = anchor keyword.
        result.business_customer = _find_anchor_paragraph(
            business_raw,
            ["competition", "competitors", "customers", "principal customers"],
            max_chars=_BUSINESS_CUSTOMER_CHARS,
        )
    if mdna_raw:
        result.mdna_revenue = _find_anchor_paragraph(
            mdna_raw,
            ["revenue", "net sales", "results of operations"],
            max_chars=_MDNA_REVENUE_CHARS,
        )
        result.mdna_outlook = _find_anchor_paragraph(
            mdna_raw,
            ["outlook", "guidance", "forward-looking", "fiscal year", "going forward"],
            max_chars=_MDNA_OUTLOOK_CHARS,
        )

    if risk_raw:
        result.risk_summary_bullets = _extract_risk_summary_bullets(risk_raw, _RISK_BULLET_COUNT)

    # 7) cap 적용 (--full 시 50K, 그 외 비-Risk 섹션은 그대로 보존하지만 render 시 derived 만 사용).
    if full:
        result.business = business_raw[:_FULL_CAP]
        result.risk_factors = risk_raw[:_FULL_CAP]
        result.mdna = mdna_raw[:_FULL_CAP]
    else:
        # store 원본은 작게 — derived 만 출력.
        result.business = business_raw[:_FULL_CAP]
        result.risk_factors = ""  # render 가 bullets 만 출력하도록.
        result.mdna = mdna_raw[:_FULL_CAP]

    return result
