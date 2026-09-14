# -*- coding: utf-8 -*-
"""module_evidence — 출처 저장소(색인) + ID 브로커.

**단일 원본은 md 다.** 이 모듈은 `handoff/*.md` 의 원장 표와 `REPORT/**.md` 의 출처 달린
줄을 수확해 `data/evidence.db`(파생물, 언제든 재생성)에 색인하고, 한 단어로 되찾게 한다.
근거를 새로 저작하지 않는다 — 있는 것을 찾을 수 있게만 만든다.
"""
from ._config import EVIDENCE_DB, FAMILIES
from ._harvest import harvest_ledger, harvest_refs_and_ids, harvest_report
from ._ids import next_id, scan_occupancy
from ._store import build, cite, show, stats, where_ticker

__all__ = [
    "EVIDENCE_DB", "FAMILIES",
    "build", "cite", "where_ticker", "show", "stats",
    "next_id", "scan_occupancy",
    "harvest_ledger", "harvest_report", "harvest_refs_and_ids",
]
