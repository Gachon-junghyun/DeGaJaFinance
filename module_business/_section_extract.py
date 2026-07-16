"""corp_embeddings.db.section_text 에서 사업 모델 구조화 정보 추출.

KOSPI 832 종목 사업보고서의 "II. 사업의 내용" 본문은 표 형식이 회사마다
다소 다르지만 핵심 패턴은 공통:
  1. 사업의 개요 (서술형)
  2. 주요 제품 및 서비스 — 매출 비중 표 (사업부문/품목/매출액/비율)
  3. 원재료 및 생산설비 — 주요 매입처·생산능력
  4. (생략 가능) 매출 및 수주상황 / 시장점유율

본 모듈은 정규식으로 위 4개 블록을 추출한 다음, 매출 표는 행 단위 파싱.
표 추출 실패 시 raw section만 반환 (graceful degradation).
"""
from __future__ import annotations

import re
import sqlite3
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


DB_PATH = Path(__file__).resolve().parent.parent / "data" / "corp_embeddings.db"


@dataclass
class RevenueRow:
    segment: str       # 사업부문 (예: 바이오의약품)
    sales_type: str    # 매출유형 (제품/용역/상품)
    item: str          # 품목 (바이오의약품 등)
    amount_million: Optional[int] = None  # 매출액 (백만원)
    ratio_pct: Optional[float] = None     # 매출 비중 %


@dataclass
class BusinessOverview:
    ticker: str
    corp_name: str
    overview_text: str = ""              # 1. 사업의 개요 발췌 (~4000자)
    revenue_table: list[RevenueRow] = field(default_factory=list)
    revenue_unit: str = ""               # "(단위: 백만원, %)" 같은 표기
    revenue_basis_date: str = ""         # "(기준일: 2025.12.31)"
    revenue_narrative: list[str] = field(default_factory=list)  # 표 실패 시 fallback grep
    raw_capacity_text: str = ""          # 3. 생산능력 raw 발췌
    raw_materials_text: str = ""         # 3. 원재료 raw 발췌
    section_length: int = 0
    extracted_ok: bool = False           # 매출 표 파싱 성공 여부


def _connect() -> sqlite3.Connection:
    if not DB_PATH.exists():
        raise FileNotFoundError(f"corp_embeddings.db 가 없습니다: {DB_PATH}")
    return sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)


def load_section_text(ticker: str) -> tuple[str, str]:
    """ticker → (corp_name, section_text). 없으면 ('', '')."""
    with _connect() as conn:
        cur = conn.execute(
            "SELECT corp_name, section_text FROM corp_descriptions WHERE ticker=?",
            (ticker,),
        )
        row = cur.fetchone()
        if not row:
            return "", ""
        return row[0] or "", row[1] or ""


_OVERVIEW_PAT = re.compile(
    r"(?:^|\n)\s*(?:[가1]\.|1\))?\s*사업의\s*(?:개요|내용)\s*\n+(.+?)"
    r"(?:\n+\s*(?:[나2]\.|2\.|2\))\s*(?:[\(（][^\)）]*[\)）])?\s*(?:주요\s*제품|영업|매출))",
    re.S,
)
# "2. 주요 제품" / "2. (제조서비스업)주요 제품" / "나. 주요 제품 및 서비스" 등 다양한 변형 매치
_PRODUCT_PAT = re.compile(
    r"(?:^|\n)\s*(?:[나2]\.|2\.|2\))\s*(?:[\(（][^\)）]{0,30}[\)）])?\s*주요\s*제품(?:\s*등)?(?:\s*및\s*서비스)?[^\n]*\n+(.+?)"
    r"(?:\n+\s*(?:[다3]\.|3\.|3\))\s*(?:원재료|매출|매입|생산|시장)|\Z)",
    re.S,
)
_MATERIAL_PAT = re.compile(
    r"(?:^|\n)\s*(?:[다3]\.|3\.|3\))\s*(?:원재료|매입)[^\n]*\n+(.+?)"
    r"(?:\n+\s*(?:[나2]\.|2\.|2\))\s*생산능력|\n+\s*(?:[라4]\.|4\.|4\)))",
    re.S,
)
_CAPACITY_PAT = re.compile(r"생산능력[^\n]*\n+(.+?)(?:\n+\s*\d\.\s)", re.S)
# 매출 정보 grep — 표 추출 실패 시 본문에서 매출 관련 문장 후보 추출
# V0.8 — 금융사·보험사 패턴 추가 (영업수익·이자수익·수수료수익·보험료수익)
_REVENUE_SENT_PAT = re.compile(
    r"[^\.\n]*?(?:매출|영업이익|영업수익|이자수익|수수료수익|보험료수익|운용수익|"
    r"당기\s*매출|연결\s*매출|매출액|매출\s*비중|점유율|총자산|"
    r"가동률|수주잔액|순이익|당기순이익)[^\.\n]*?"
    r"(?:[\d,]+\s*(?:조|억|백만|억\s*원|조\s*원)|\d+\.\d+\s*%)[^\.\n]{0,80}\."
)
_BASIS_DATE_PAT = re.compile(r"기준일\s*[:：]\s*(\d{4}[\.\-]\d{1,2}[\.\-]\d{1,2})")
_UNIT_PAT = re.compile(r"\(단위\s*[:：]\s*([^\)]+)\)")

# 매출 표 한 행 추정 — "사업부문 ... 품목 ... 숫자(매출액) ... 숫자(비율)"
# section_text 는 표가 줄바꿈으로 흩어져 있어 row 재조립이 필요. 휴리스틱:
# - "합계" 또는 "소계" 키워드 전후로 row 단위 split
# - 숫자 두 개 (매출액, 비율) 이 같은 row 안에 있어야 valid
_NUMBER_PAT = re.compile(r"([\d,]+)\s*\n\s*(\d+\.\d+)")


def _extract_overview(section_text: str) -> str:
    """1. 사업의 개요 발췌 (~4000자). 패턴 미매치 시 fallback 으로 raw 첫 부분."""
    m = _OVERVIEW_PAT.search(section_text)
    if not m:
        # fallback: section_text 시작부 발췌. 단 표지·목차로 시작하는 경우 skip
        # "Ⅰ. 회사의 개요", "Ⅲ. 재무에 관한 사항" 같은 목차 패턴 포함 시 그 이후로 jump
        toc_skip = re.search(r"II\.\s*사업의\s*내용[^\n]*\n", section_text)
        start = toc_skip.end() if toc_skip else 0
        return re.sub(r"\n+\s*", "\n", section_text[start:start + 4000]).strip()
    txt = m.group(1).strip()
    txt = re.sub(r"\n+\s*", "\n", txt)
    return txt[:4000]


def _extract_revenue_narrative(section_text: str, max_sentences: int = 8) -> list[str]:
    """매출 표 실패 시 fallback — 본문에서 매출 관련 문장 grep."""
    found = _REVENUE_SENT_PAT.findall(section_text)
    if not found:
        # 폭넓게 — "매출" 또는 "영업이익" 들어간 문장 발췌
        sents = re.split(r"(?<=[\.。])\s+", section_text)
        found = [
            s.strip() for s in sents
            if ("매출" in s or "영업이익" in s)
            and re.search(r"[\d,]+\s*(?:조|억|백만|%)", s)
        ]
    seen = set()
    result: list[str] = []
    for s in found:
        s = re.sub(r"\s+", " ", s).strip()
        if 30 <= len(s) <= 400 and s not in seen:
            seen.add(s)
            result.append(s)
        if len(result) >= max_sentences:
            break
    return result


def _extract_product_section(section_text: str) -> str:
    m = _PRODUCT_PAT.search(section_text)
    if not m:
        return ""
    return m.group(1)


_HEADER_TOKENS = {
    "사업부문", "사업 부문", "매출유형", "매출 유형", "품목", "품 목",
    "매출액", "매 출 액", "비율", "비 율", "비중", "비 중",
    "구분", "구 분", "부문", "부 문", "주요 제품", "제품",
    "금액", "기간", "공급", "용도",
}
_SUBTOTAL_TOKENS = {"소계", "소 계", "합계", "합 계", "총계", "총 계", "총합계", "전 체"}
_SALES_TYPE_TOKENS = {
    "제품", "상품", "용역", "기타", "서비스",
    "제품 및 상품 등", "제품 및 상품", "제 품상 품",
    "제품(상품)", "임대", "수수료",
}

# 매출액(비율) 합쳐진 케이스 분리 — 예: "11,522,251(42%)" → 두 셀로
_AMOUNT_RATIO_SPLIT = re.compile(r"([\d,]+)\s*[\(（]\s*(\d+(?:\.\d+)?)\s*%?\s*[\)）]")
# 비율 셀 — 숫자 + 선택적 %
_RATIO_CELL = re.compile(r"^\d+(?:\.\d+)?%?$")
# 비율 셀 with %
_RATIO_PCT_PAT = re.compile(r"^(\d+(?:\.\d+)?)%?$")

# 다양한 헤더 패턴으로 표 본문 시작 찾기
_TABLE_HEAD_PATTERNS = [
    # "사업부문 ... 매출액 ... 비율"
    r"(?:사업\s*부문|부\s*문|구\s*분)[\s\S]*?매출(?:액)?[\s\S]*?(?:비\s*율|비\s*중)[\s\S]*?\n",
    # "사업부문 ... 품목 ... 매출액(비율)"  - 결합 셀
    r"(?:사업\s*부문|부\s*문|구\s*분)[\s\S]*?매출액\s*[\(（][\s\S]*?[\)）][\s\S]*?\n",
    # "구분 ... 금액 ... 비중" (현대자동차 형)
    r"구\s*분[\s\S]*?금\s*액[\s\S]*?비\s*중[\s\S]*?\n",
]


def _preprocess_table_body(text: str) -> str:
    """매출액(비율) 합쳐진 셀을 두 셀로 분리."""
    return _AMOUNT_RATIO_SPLIT.sub(r"\1 | \2", text)


def _is_ratio_cell(cell: str) -> tuple[bool, Optional[float]]:
    """셀이 비율(0-100)인지 + 값."""
    m = _RATIO_PCT_PAT.match(cell.strip())
    if not m:
        return False, None
    try:
        v = float(m.group(1))
    except ValueError:
        return False, None
    if 0 <= v <= 100:
        return True, v
    return False, None


def _extract_revenue_table(product_section: str) -> tuple[list[RevenueRow], str, str]:
    """2.가 매출 표 → list[RevenueRow]. V0.3 — 헤더 다양화 + 결합 셀 분리.

    전처리:
      1) 매출액(비율) 결합 셀 → 두 셀로 분리
      2) 다양한 헤더 패턴으로 table body 시작 찾기
    행 재조립:
      3) 비율 셀(% 포함) 발견 시 매출액 셀 발견 시 한 행 종료
      4) head 셀에서 헤더 토큰·숫자 제거 후 segment / sales_type / item 매핑
      5) rowspan 처리 — head 첫 셀이 매출유형이면 직전 segment 이어받음
    """
    if not product_section:
        return [], "", ""

    unit_m = _UNIT_PAT.search(product_section)
    unit = unit_m.group(1).strip() if unit_m else ""
    basis_m = _BASIS_DATE_PAT.search(product_section)
    basis = basis_m.group(1) if basis_m else ""

    # 결합 셀 전처리
    section = _preprocess_table_body(product_section)

    # 다양한 헤더 패턴 시도
    table_body = ""
    for pat in _TABLE_HEAD_PATTERNS:
        m = re.search(pat + r"([\s\S]+?)(?:\n\s*나\.|\n\s*\d\.\s|\Z)", section)
        if m:
            table_body = m.group(1)
            break
    if not table_body:
        return [], unit, basis

    cells = [c.strip() for c in re.split(r"\n+|\s{2,}|\|", table_body) if c.strip()]
    cells = [c for c in cells if c not in ("-", "—")]

    rows: list[RevenueRow] = []
    buf: list[str] = []
    last_segment: str = ""
    cumulative_ratio: float = 0.0  # V0.6 — 100% 도달 시 추출 종료

    for cell in cells:
        buf.append(cell)
        is_ratio, ratio_val = _is_ratio_cell(cell)
        if not is_ratio:
            continue
        if len(buf) < 3:
            buf = []
            continue

        ratio = ratio_val
        # 매출액 셀 — 비율 직전. 콤마 포함 정수.
        amount_cell = buf[-2].replace(",", "")
        try:
            amount = int(amount_cell)
        except ValueError:
            # 결합 셀일 경우 분리 결과를 다시 시도
            am = re.match(r"([\d,]+)", buf[-2])
            if not am:
                buf = []
                continue
            try:
                amount = int(am.group(1).replace(",", ""))
            except ValueError:
                buf = []
                continue

        head = [
            b for b in buf[:-2]
            if b not in _HEADER_TOKENS and not re.fullmatch(r"[\d,\.\s%년기제]+", b)
        ]
        is_subtotal = any(t in _SUBTOTAL_TOKENS for t in head)
        if is_subtotal:
            buf = []
            last_segment = ""
            # 소계는 누적 비율 reset 안 함 — 다음 그룹 시작 신호로만
            continue

        if not head:
            buf = []
            continue

        if head[0] in _SALES_TYPE_TOKENS:
            seg = last_segment
            stype = head[0]
            item = head[1] if len(head) >= 2 else stype
        elif len(head) >= 3:
            seg = head[0]
            stype = head[1]
            item = head[2]
            last_segment = seg
        elif len(head) == 2:
            seg = head[0]
            stype = head[1] if head[1] in _SALES_TYPE_TOKENS else ""
            item = head[1] if not stype else seg
            last_segment = seg
        else:  # len == 1
            seg = last_segment or head[0]
            stype = ""
            item = head[0]

        rows.append(
            RevenueRow(
                segment=seg, sales_type=stype, item=item,
                amount_million=amount, ratio_pct=ratio,
            )
        )
        cumulative_ratio += ratio
        buf = []
        # V0.7 — 누적 비율 95% 이상 도달 시 즉시 종료 (다년치 false positive 방지)
        if cumulative_ratio >= 95:
            break

    # V0.7 후처리 sanity — 누적 비율 80% 미만이면 false positive 의심 → reject
    if rows and cumulative_ratio < 80:
        return [], unit, basis

    return rows, unit, basis


def _extract_material_text(section_text: str) -> str:
    m = _MATERIAL_PAT.search(section_text)
    if not m:
        return ""
    txt = m.group(1).strip()
    return re.sub(r"\n+\s*", "\n", txt)[:2500]


def _extract_capacity_text(section_text: str) -> str:
    m = _CAPACITY_PAT.search(section_text)
    if not m:
        return ""
    txt = m.group(1).strip()
    return re.sub(r"\n+\s*", "\n", txt)[:2000]


def extract_business_overview(ticker: str) -> Optional[BusinessOverview]:
    """ticker → BusinessOverview. DB miss 시 None."""
    corp_name, section_text = load_section_text(ticker)
    if not section_text:
        return None

    overview = _extract_overview(section_text)
    product_section = _extract_product_section(section_text)
    rows, unit, basis = _extract_revenue_table(product_section)
    narrative = [] if rows else _extract_revenue_narrative(section_text)
    materials = _extract_material_text(section_text)
    capacity = _extract_capacity_text(section_text)

    return BusinessOverview(
        ticker=ticker,
        corp_name=corp_name,
        overview_text=overview,
        revenue_table=rows,
        revenue_unit=unit,
        revenue_basis_date=basis,
        revenue_narrative=narrative,
        raw_capacity_text=capacity,
        raw_materials_text=materials,
        section_length=len(section_text),
        extracted_ok=bool(rows),
    )
