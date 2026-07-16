"""report_nm 키워드 기반 5개 카테고리 분류.

리포트 활용 가치 순으로 정렬:
- contract  : 단일판매·공급계약 (수주) — 직접 catalyst
- treasury  : 자기주식 취득/처분/소각 — 단기 수급 catalyst
- capital   : 유상증자/CB/BW/합병/분할 — 희석·구조 변화
- equity    : 5% 대량보유, 임원 주식 변동 — 큰손/내부자 시그널
- earnings  : 사업/분기/반기보고서 — 실적 발표 일자
- other     : 위 외 주요사항보고서 등
"""
from __future__ import annotations

CATEGORIES = ["contract", "treasury", "capital", "equity", "earnings", "other"]

CATEGORY_LABELS = {
    "contract": "수주 (단일판매·공급계약)",
    "treasury": "자기주식",
    "capital":  "자본변동 (증자·CB·합병·분할)",
    "equity":   "지분변동 (5% 대량보유·임원)",
    "earnings": "실적 (분기·반기·사업보고서)",
    "other":    "기타 주요사항",
}


def categorize(report_nm: str) -> str:
    """공시명(report_nm)을 받아 카테고리 키 반환.

    "정정" 공시는 원본과 같은 카테고리로 분류한다 (caller가 필요시 별도 필터).
    """
    nm = report_nm or ""

    if "단일판매" in nm or "공급계약" in nm:
        return "contract"

    if "자기주식" in nm or "자사주" in nm:
        return "treasury"

    if any(k in nm for k in [
        "유상증자", "무상증자", "전환사채", "신주인수권부사채",
        "교환사채", "합병", "분할", "주식교환", "주식분할", "감자",
    ]):
        return "capital"

    if any(k in nm for k in [
        "주식등의대량보유상황보고서", "임원·주요주주특정증권등소유상황보고서",
        "임원ㆍ주요주주", "최대주주변경", "주식소유",
    ]):
        return "equity"

    if any(k in nm for k in [
        "사업보고서", "분기보고서", "반기보고서",
        "잠정)실적", "잠정실적", "영업(잠정)실적",
    ]):
        return "earnings"

    return "other"
