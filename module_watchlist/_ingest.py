"""JSON ingest — Form A (신규 등록) / Form B (검증 결과) 둘 다 지원.

Form A:
    {
      "thesis": "전력인프라",
      "items": [
        {"item": "...", "trigger_criteria": "...", "importance": "high",
         "status": "open", "tickers": ["052690"]}
      ]
    }

Form B:
    {
      "thesis": "전력인프라",
      "verifications": [
        {"item": "한수원 SMR 6월 부지 결정",
         "status": "resolved", "thesis_impact": "강화",
         "resolution_note": "...",
         "thesis_update": {"before": "추정", "after": "6/25 확정"}}
      ]
    }

Form C: 두 키를 한 파일에 함께 둬도 됨.
다중 thesis: 최상위가 list 면 각 원소를 위 형태로 처리.
"""
from __future__ import annotations

import json
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional

from . import _db
from ._db import WatchlistItem


@dataclass
class IngestResult:
    created: int = 0
    updated: int = 0
    noop: int = 0
    thesis_updates: int = 0
    errors: list[str] = None  # type: ignore[assignment]

    def __post_init__(self):
        if self.errors is None:
            self.errors = []

    @property
    def total(self) -> int:
        return self.created + self.updated + self.noop


def _coerce_tickers(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(v).strip() for v in value if str(v).strip()]
    if isinstance(value, str):
        return [t.strip() for t in value.split(",") if t.strip()]
    return [str(value)]


def _build_spec(thesis: str, raw: dict) -> WatchlistItem:
    return WatchlistItem(
        thesis=thesis,
        item=str(raw.get("item", "")).strip(),
        trigger_criteria=raw.get("trigger_criteria") or raw.get("trigger"),
        importance=raw.get("importance"),
        status=raw.get("status") or "open",
        tickers=_coerce_tickers(raw.get("tickers")),
        resolution_note=raw.get("resolution_note"),
        thesis_impact=raw.get("thesis_impact"),
    )


def _process_block(
    conn: sqlite3.Connection,
    block: dict,
    *,
    source: Optional[str],
    result: IngestResult,
) -> None:
    thesis = block.get("thesis")
    if not thesis:
        result.errors.append("missing 'thesis' in block")
        return

    items = block.get("items") or []
    for raw in items:
        try:
            spec = _build_spec(thesis, raw)
            _, action = _db.upsert(conn, spec, source=source)
            if action == "created":
                result.created += 1
            elif action == "updated":
                result.updated += 1
            else:
                result.noop += 1
        except Exception as exc:  # noqa: BLE001
            result.errors.append(f"items[{raw.get('item','?')}]: {exc}")

    verifications = block.get("verifications") or []
    for raw in verifications:
        try:
            spec = _build_spec(thesis, raw)
            # verifications 는 보통 status 가 명시되며 resolution_note·thesis_impact 가 있음
            wid, action = _db.upsert(conn, spec, source=source)
            if action == "created":
                result.created += 1
            elif action == "updated":
                result.updated += 1
            else:
                result.noop += 1

            tu = raw.get("thesis_update")
            if isinstance(tu, dict):
                before = tu.get("before") or tu.get("before_text")
                after = tu.get("after") or tu.get("after_text")
                if before is not None or after is not None:
                    _db.add_thesis_update(
                        conn,
                        thesis,
                        item=spec.item,
                        before_text=before,
                        after_text=after,
                        source=source,
                    )
                    result.thesis_updates += 1
        except Exception as exc:  # noqa: BLE001
            result.errors.append(f"verifications[{raw.get('item','?')}]: {exc}")


def ingest_data(
    conn: sqlite3.Connection,
    data: Any,
    *,
    source: Optional[str] = None,
) -> IngestResult:
    result = IngestResult()
    blocks = data if isinstance(data, list) else [data]
    for block in blocks:
        if not isinstance(block, dict):
            result.errors.append(f"block is not a dict: {type(block).__name__}")
            continue
        _process_block(conn, block, source=source, result=result)
    return result


def ingest_file(
    conn: sqlite3.Connection,
    path: Path,
    *,
    source: Optional[str] = None,
) -> IngestResult:
    raw = path.read_text(encoding="utf-8")
    data = json.loads(raw)
    if source is None:
        source = f"ingest:{path.name}"
    return ingest_data(conn, data, source=source)
