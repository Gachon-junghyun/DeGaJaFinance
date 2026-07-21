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


@dataclass
class TocNode:
    """사업보고서 목차 한 항목 — viewer.do 를 열기 위한 좌표."""
    text: str
    rcp_no: str
    dcm_no: str
    ele_id: str
    offset: str
    length: str
    dtd: str


_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"

# main.do 의 JS 트리에서 node['key'] = "value" 한 덩어리를 뽑는다.
_NODE_FIELD = re.compile(r"node\d*\[\'(\w+)\'\]\s*=\s*\"([^\"]*)\"")


def fetch_toc(rcept_no: str) -> list[TocNode]:
    """rcept_no → 사업보고서 목차(각 절의 viewer 좌표).

    DART 뷰어(dsaf001/main.do)는 **프레임셋 껍데기**다 — 본문이 아니라 좌측 목차 트리와
    네비게이션 크롬만 들어 있다. 예전 구현은 이 껍데기를 그대로 긁어서 "잠시만 기다려주세요
    · 현재목차 · 전체문서 · 영문보기 · 다운로드…" 같은 UI 텍스트를 본문이라고 반환했다.

    진짜 본문은 `report/viewer.do?rcpNo=&dcmNo=&eleId=&offset=&length=&dtd=` 에 있고,
    그 좌표는 main.do 안의 JS 트리(`node1['offset'] = "141551"` …)에 박혀 있다.
    여기서 그 트리를 파싱한다.
    """
    if not rcept_no:
        return []
    r = requests.get(
        "https://dart.fss.or.kr/dsaf001/main.do",
        params={"rcpNo": rcept_no},
        headers={"User-Agent": _UA},
        timeout=20,
    )
    r.raise_for_status()

    nodes: list[TocNode] = []
    cur: dict[str, str] = {}
    for key, val in _NODE_FIELD.findall(r.text):
        if key == "text":
            # 새 노드 시작 — 직전 노드가 완성됐으면 확정
            if cur.get("text") and cur.get("offset"):
                nodes.append(_to_node(cur))
            cur = {"text": val}
        elif cur:
            cur[key] = val
    if cur.get("text") and cur.get("offset"):
        nodes.append(_to_node(cur))

    if not nodes:
        # 목차 트리가 없는 단일문서 공시(예: "타인에대한채무보증결정")는
        # viewDoc("rcpNo","dcmNo","0","0","0","HTML","") 리터럴 호출 하나만 갖는다.
        m = re.search(
            r"viewDoc\(\s*\"(\d+)\"\s*,\s*\"(\d*)\"\s*,\s*\"(\d*)\"\s*,"
            r"\s*\"(\d*)\"\s*,\s*\"(\d*)\"\s*,\s*\"([^\"]*)\"",
            r.text,
        )
        if m:
            nodes.append(TocNode(
                text="(단일문서)",
                rcp_no=m.group(1), dcm_no=m.group(2), ele_id=m.group(3),
                offset=m.group(4), length=m.group(5), dtd=m.group(6) or "HTML",
            ))
    return nodes


def _to_node(d: dict[str, str]) -> TocNode:
    return TocNode(
        text=d.get("text", "").strip(),
        rcp_no=d.get("rcpNo", ""),
        dcm_no=d.get("dcmNo", ""),
        ele_id=d.get("eleId", ""),
        offset=d.get("offset", ""),
        length=d.get("length", ""),
        dtd=d.get("dtd", "dart4.xsd"),
    )


def fetch_toc_section(node: TocNode) -> str:
    """목차 노드 → 그 절의 실제 본문 평문."""
    r = requests.get(
        "https://dart.fss.or.kr/report/viewer.do",
        params={
            "rcpNo": node.rcp_no,
            "dcmNo": node.dcm_no,
            "eleId": node.ele_id,
            "offset": node.offset,
            "length": node.length,
            "dtd": node.dtd,
        },
        headers={"User-Agent": _UA, "Referer": "https://dart.fss.or.kr/dsaf001/main.do"},
        timeout=30,
    )
    r.raise_for_status()
    return _html_to_text(r.text)


def _html_to_text(html: str) -> str:
    html = re.sub(r"<script[\s\S]*?</script>", " ", html, flags=re.I)
    html = re.sub(r"<style[\s\S]*?</style>", " ", html, flags=re.I)
    # 표/줄바꿈은 구조 정보 — 공백으로 뭉개지 말고 개행으로 살린다
    html = re.sub(r"</\s*(tr|p|div|h\d|table|br)\s*>", "\n", html, flags=re.I)
    html = re.sub(r"<\s*br\s*/?>", "\n", html, flags=re.I)
    html = re.sub(r"</\s*t[dh]\s*>", "\t", html, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", html)
    text = (
        text.replace("&nbsp;", " ").replace("&amp;", "&")
        .replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"')
    )
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s*\n\s*\n+", "\n\n", text)
    return text.strip()


def fetch_business_section(rcept_no: str, *, section: str = "사업의 내용", max_chars: int = 30000) -> str:
    """rcept_no → 사업보고서의 해당 절 본문 평문. 실패 시 빈 문자열.

    기본은 "II. 사업의 내용". `section` 부분일치로 다른 절도 뽑을 수 있다
    (예: "재무제표", "이사의 경영진단", "우발부채").
    """
    if not rcept_no:
        return ""
    try:
        nodes = fetch_toc(rcept_no)
        if not nodes:
            return ""
        want = _norm(section)
        hits = [n for n in nodes if want in _norm(n.text)]
        if not hits:
            return ""
        # 같은 이름이 여러 번이면 본문이 가장 긴 것(하위 절 포함 상위 노드)을 고른다
        node = max(hits, key=lambda n: int(n.length or 0))
        return fetch_toc_section(node)[:max_chars]
    except Exception:
        return ""


def _norm(s: str) -> str:
    return "".join(str(s).split())


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
