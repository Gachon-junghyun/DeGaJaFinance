# -*- coding: utf-8 -*-
"""module_report_tags — REPORT 폴더 태그추출 + 인수인계 원장.

문제: 데스크마다 매번 뉴스·공시를 재검색하고 리포트를 새로 만들면 중복·낭비.
해법: 산출된 리포트(.md)에서 태그(종목·섹터·평결·테마·날짜)를 한 번 추출해
인수인계 원장(REPORT/HANDOFF.md)을 **증분 갱신**하고, 다운스트림은 그걸 읽는다.

기능 지도:
    _extract    리포트 1개 → 태그 (결정론, 티커는 유니버스 검증)
    _handoff    증분 스캔(mtime 추적) → HANDOFF.md + _tags.json 갱신 + 역인덱스

CLI:
    python -m module_report_tags update          # REPORT/ 증분 스캔 → 인수인계 갱신
    python -m module_report_tags show            # HANDOFF.md 출력
    python -m module_report_tags ticker GEV      # 그 종목 다룬 리포트 역검색
"""
from ._config import HANDOFF_MD, REPORT_DIR, TAGS_JSON
from ._extract import extract_tags
from ._handoff import query_ticker, update

__all__ = ["extract_tags", "update", "query_ticker", "REPORT_DIR", "HANDOFF_MD", "TAGS_JSON"]
