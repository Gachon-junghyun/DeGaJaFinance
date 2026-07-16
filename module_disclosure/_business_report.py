# -*- coding: utf-8 -*-
"""DART 사업보고서 본문 fetch — "II. 사업의 내용" 섹션.

옛 module_business/_dart_fetch.py 를 이 리포로 흡수(그 모듈의 코어는 corp_embeddings.db
라 DART 아님 → 제외, DART 부분만 여기로). corp_code(8자리 DART code)는 이 모듈의
resolve_corp_code(corp_codes.csv)로 얻는다. requests 외 의존성 0, DART_API_KEY 미설정 시 None.
"""
from __future__ import annotations

import os
import re
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Optional

import requests

from ._corp_codes import resolve_corp_code

DART_BUSINESS_DOC_TYPES = ["A001", "A002", "A003"]  # 사업/반기/분기 보고서


@dataclass
class DartReport:
    rcept_no: str
    report_nm: str
    rcept_dt: str
    business_section: str = ""  # II. 사업의 내용 본문 (HTML→text)


def _api_key() -> Optional[str]:
    return os.environ.get("DART_API_KEY", "").strip() or None


def search_recent_business_report(corp_code: str, *, max_age_months: int = 18) -> Optional[DartReport]:
    """corp_code(8자리 DART) → 가장 최근 사업/반기/분기 보고서 1건 (rcept_no만 채움)."""
    key = _api_key()
    if not key:
        return None
    try:
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
    """rcept_no → 사업보고서 "II. 사업의 내용" HTML 본문 fetch → 평문. 실패 시 빈 문자열."""
    if not rcept_no:
        return ""
    try:
        url = f"https://dart.fss.or.kr/dsaf001/main.do?rcpNo={rcept_no}"
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        html = r.text
        html = re.sub(r"<script[\s\S]*?</script>", " ", html, flags=re.I)
        html = re.sub(r"<style[\s\S]*?</style>", " ", html, flags=re.I)
        text = re.sub(r"<[^>]+>", " ", html)
        text = re.sub(r"\s+", " ", text).strip()
        m = re.search(r"II\.\s*사업의\s*내용(.+?)III\.", text)
        if m:
            return m.group(1).strip()[:30000]
        return text[:30000]
    except Exception:
        return ""


def fetch_business_report(stock_or_name: str) -> Optional[DartReport]:
    """종목코드/기업명 → 최근 사업보고서 + "II. 사업의 내용" 본문까지 채워 반환.

    편의 함수: resolve_corp_code → search_recent_business_report → fetch_business_section 체인.
    """
    resolved = resolve_corp_code(stock_or_name)
    if not resolved:
        return None
    corp_code, _corp_name = resolved
    rep = search_recent_business_report(corp_code)
    if rep and rep.rcept_no:
        rep.business_section = fetch_business_section(rep.rcept_no)
    return rep
