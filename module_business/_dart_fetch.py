"""DART 사업보고서 본문 fetch (optional).

corp_descriptions.section_text 가 누락하거나 매출 표가 깔끔히 안 잡힐 때
DART API 직접 호출로 사업보고서 "II. 사업의 내용" 본문을 가져온다.

다른 module_X 와 무관 — module_disclosure._dart_api 와 코드 일부 중복되지만
의도적으로 격리. requests 외 외부 의존성 없음. DART_API_KEY 미설정 시
graceful fallback (None 반환).
"""
from __future__ import annotations

import os
import re
from dataclasses import dataclass
from typing import Optional

import requests


DART_BUSINESS_DOC_TYPES = ["A001", "A002", "A003"]  # 사업/반기/분기 보고서


@dataclass
class DartReport:
    rcept_no: str
    report_nm: str
    rcept_dt: str
    business_section: str = ""  # II. 사업의 내용 본문 (HTML→text)


def _api_key() -> Optional[str]:
    return os.environ.get("DART_API_KEY")


def search_recent_business_report(corp_code: str, *, max_age_months: int = 18) -> Optional[DartReport]:
    """corp_code(8자리 DART code) → 가장 최근 사업/반기/분기 보고서 1건.

    rcept_no 만 채워서 반환. 본문은 fetch_business_section 으로 별도 호출.
    """
    key = _api_key()
    if not key:
        return None
    try:
        # 최근 18개월
        from datetime import datetime, timedelta
        end = datetime.now().strftime("%Y%m%d")
        bgn = (datetime.now() - timedelta(days=max_age_months * 30)).strftime("%Y%m%d")
        for pblntf_detail_ty in DART_BUSINESS_DOC_TYPES:
            r = requests.get(
                "https://opendart.fss.or.kr/api/list.json",
                params={
                    "crtfc_key": key,
                    "corp_code": corp_code,
                    "bgn_de": bgn,
                    "end_de": end,
                    "pblntf_detail_ty": pblntf_detail_ty,
                    "page_count": 5,
                },
                timeout=15,
            )
            r.raise_for_status()
            data = r.json()
            if data.get("status") != "000":
                continue
            for item in data.get("list", []):
                return DartReport(
                    rcept_no=item.get("rcept_no", ""),
                    report_nm=item.get("report_nm", ""),
                    rcept_dt=item.get("rcept_dt", ""),
                )
    except Exception:
        return None
    return None


def fetch_business_section(rcept_no: str) -> str:
    """rcept_no 기반 사업보고서 "II. 사업의 내용" HTML 본문 fetch → 평문.

    DART 본문은 viewer URL 로 HTML 제공. requests + 단순 tag strip.
    실패 시 빈 문자열.
    """
    if not rcept_no:
        return ""
    try:
        # DART 본문 viewer
        url = f"https://dart.fss.or.kr/dsaf001/main.do?rcpNo={rcept_no}"
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        # 본문 HTML — 스크립트/스타일 제거 후 텍스트만
        html = r.text
        html = re.sub(r"<script[\s\S]*?</script>", " ", html, flags=re.I)
        html = re.sub(r"<style[\s\S]*?</style>", " ", html, flags=re.I)
        text = re.sub(r"<[^>]+>", " ", html)
        text = re.sub(r"\s+", " ", text).strip()
        # II. 사업의 내용 ~ III. 직전까지
        m = re.search(r"II\.\s*사업의\s*내용(.+?)III\.", text)
        if m:
            return m.group(1).strip()[:30000]
        return text[:30000]
    except Exception:
        return ""
