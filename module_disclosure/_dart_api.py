"""OpenDART list.json + document.json 호출 래퍼.

list.json 한 호출로 페이지네이션 일괄 수집,
document.json + viewer.do 로 본문 HTML 까지 받아온다.
"""
from __future__ import annotations

import io
import os
import re
import time
import zipfile
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Optional

import requests

from ._categorizer import categorize
from ._corp_codes import resolve_corp_code

_BASE = "https://opendart.fss.or.kr/api"
_DOC_LIST_URL = "https://dart.fss.or.kr/dsaf001/main.do"


def _api_key() -> str:
    key = os.environ.get("DART_API_KEY", "").strip()
    if not key:
        raise RuntimeError(
            "DART_API_KEY 환경변수가 필요합니다. "
            "https://opendart.fss.or.kr 에서 발급 후 .env 또는 셸에 설정하세요."
        )
    return key


@dataclass
class DisclosureRow:
    rcept_no:  str
    corp_code: str
    corp_name: str
    report_nm: str
    rcept_dt:  str           # YYYYMMDD
    flr_nm:    str           # 제출인
    category:  str = ""      # contract/treasury/capital/equity/earnings/other
    is_amend:  bool = False  # 정정공시 여부

    detail: dict = field(default_factory=dict)

    @property
    def url(self) -> str:
        return f"{_DOC_LIST_URL}?rcpNo={self.rcept_no}"

    @property
    def date_iso(self) -> str:
        d = self.rcept_dt
        return f"{d[:4]}-{d[4:6]}-{d[6:8]}" if len(d) == 8 else d


def fetch_disclosures(
    stock_or_name: str,
    days: int = 60,
    end_date: Optional[str] = None,
    pblntf_ty: Optional[str] = None,
) -> list[DisclosureRow]:
    """종목코드 또는 기업명을 받아 최근 N일 공시 목록을 반환.

    - days: 조회 기간 (오늘 기준 N일 전까지)
    - end_date: YYYYMMDD (기본 오늘)
    - pblntf_ty: A=정기공시, B=주요사항보고서, C=발행공시 등 (None=전체)
    """
    resolved = resolve_corp_code(stock_or_name)
    if resolved is None:
        raise ValueError(f"corp_code 매핑 실패: {stock_or_name!r}")
    corp_code, corp_name = resolved

    end_dt = datetime.strptime(end_date, "%Y%m%d") if end_date else datetime.today()
    bgn_dt = end_dt - timedelta(days=days)
    bgn_de = bgn_dt.strftime("%Y%m%d")
    end_de = end_dt.strftime("%Y%m%d")

    rows: list[dict] = []
    page_no = 1
    while True:
        params = {
            "crtfc_key":  _api_key(),
            "corp_code":  corp_code,
            "bgn_de":     bgn_de,
            "end_de":     end_de,
            "page_no":    page_no,
            "page_count": 100,
        }
        if pblntf_ty:
            params["pblntf_ty"] = pblntf_ty

        resp = requests.get(f"{_BASE}/list.json", params=params, timeout=20)
        data = resp.json()

        status = data.get("status")
        if status == "013":
            break
        if status != "000":
            raise RuntimeError(f"DART API 오류 status={status} message={data.get('message')}")

        items = data.get("list", []) or []
        if not items:
            break
        rows.extend(items)

        total = int(data.get("total_count", 0))
        if page_no * 100 >= total:
            break
        page_no += 1
        time.sleep(0.2)

    out: list[DisclosureRow] = []
    for r in rows:
        nm = r.get("report_nm") or ""
        out.append(
            DisclosureRow(
                rcept_no  = (r.get("rcept_no") or "").strip(),
                corp_code = corp_code,
                corp_name = corp_name,
                report_nm = nm,
                rcept_dt  = (r.get("rcept_dt") or "").strip(),
                flr_nm    = (r.get("flr_nm") or "").strip(),
                category  = categorize(nm),
                is_amend  = "정정" in nm,
            )
        )
    return out


def _decode_bytes(raw: bytes) -> str:
    for enc in ("utf-8", "euc-kr", "cp949"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace")


def fetch_disclosure_detail(rcept_no: str, timeout: int = 20) -> Optional[str]:
    """공시 본문(XML/HTML 텍스트)을 반환. 실패 시 None.

    OpenDART /api/document.xml 은 ZIP을 반환하며 ZIP 안에 공시 원문 XML/HTML 파일이 들어 있다.
    파일 인코딩은 EUC-KR 인 경우가 많아 cp949 → utf-8 디코드 fallback 처리.

    수주·자사주·자본변동 등 단일 사건 공시는 ZIP 안에 파일이 1개라 첫 파일만 읽음.
    여러 파일로 구성되는 사업보고서 등은 fetch_disclosure_detail_all 을 사용.
    """
    try:
        resp = requests.get(
            f"{_BASE}/document.xml",
            params={"crtfc_key": _api_key(), "rcept_no": rcept_no},
            timeout=timeout,
        )
        if resp.status_code != 200 or len(resp.content) < 200:
            return None

        ctype = resp.headers.get("content-type", "")
        if "json" in ctype:
            return None

        try:
            with zipfile.ZipFile(io.BytesIO(resp.content)) as z:
                names = z.namelist()
                if not names:
                    return None
                raw = z.read(names[0])
        except zipfile.BadZipFile:
            raw = resp.content

        return _decode_bytes(raw)
    except Exception:
        return None


def fetch_disclosure_detail_all(rcept_no: str, timeout: int = 30) -> Optional[str]:
    """공시 본문 ZIP 안의 *모든 파일* 텍스트를 합쳐서 반환. 실패 시 None.

    사업보고서·반기보고서처럼 ZIP 안에 여러 XML/HTML 파일로 분할된 보고서용.
    파일은 정렬된 이름 순서로 합치며, 파일 사이엔 \\n\\n 을 넣는다.
    파일별로 utf-8 → euc-kr → cp949 순으로 디코딩 시도.
    """
    try:
        resp = requests.get(
            f"{_BASE}/document.xml",
            params={"crtfc_key": _api_key(), "rcept_no": rcept_no},
            timeout=timeout,
        )
        if resp.status_code != 200 or len(resp.content) < 200:
            return None

        ctype = resp.headers.get("content-type", "")
        if "json" in ctype:
            return None

        try:
            with zipfile.ZipFile(io.BytesIO(resp.content)) as z:
                names = sorted(z.namelist())
                if not names:
                    return None
                parts = [_decode_bytes(z.read(n)) for n in names]
        except zipfile.BadZipFile:
            return _decode_bytes(resp.content)

        return "\n\n".join(parts)
    except Exception:
        return None
