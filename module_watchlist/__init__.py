"""thesis 단위 watchlist DB 모듈 (research_Mvp/watchlist.db).

CLUSTER_SCENARIO_WORKFLOW.md §6-6 (Phase D 외부 검증)의 watchlist 라이프사이클을
DB로 영속화한다. 한 항목은 (thesis, item) 으로 식별되며 status 가
open → partial → resolved (또는 split / rejected) 으로 흘러간다.

빠른 사용:
    from module_watchlist import connect, add, find, upsert, ingest_file, WatchlistItem

    with connect() as conn:
        add(conn, WatchlistItem(thesis="전력인프라", item="한수원 SMR 6월 부지 결정",
                                 trigger_criteria="6/25 부지 평가위 결정",
                                 importance="high", tickers=["052690"]))

CLI:
    python -m module_watchlist init
    python -m module_watchlist add --thesis 전력인프라 --item "..." --trigger "..." --importance high
    python -m module_watchlist list [--thesis X] [--status open]
    python -m module_watchlist show <id|item-substring>
    python -m module_watchlist update <id> --status resolved --resolution-note "..." --thesis-impact 강화
    python -m module_watchlist remove <id>
    python -m module_watchlist search <free-text>
    python -m module_watchlist history <id>
    python -m module_watchlist updates [--thesis X]
    python -m module_watchlist ingest <json_path>

DB 위치: WATCHLIST_DB_PATH 환경변수 우선, 없으면 research_Mvp/watchlist.db.
"""
from ._db import (
    DB_FILENAME,
    HistoryRow,
    IMPORTANCE_VALUES,
    STATUS_VALUES,
    THESIS_IMPACT_VALUES,
    ThesisUpdate,
    WatchlistItem,
    add,
    add_thesis_update,
    connect,
    default_db_path,
    find,
    get_by_id,
    get_by_key,
    history,
    init_db,
    list_thesis_updates,
    remove,
    update,
    upsert,
)
from ._ingest import IngestResult, ingest_data, ingest_file
from ._renderer import (
    render_history,
    render_list_table,
    render_show,
    render_thesis_updates,
)

__all__ = [
    "DB_FILENAME",
    "HistoryRow",
    "IMPORTANCE_VALUES",
    "STATUS_VALUES",
    "THESIS_IMPACT_VALUES",
    "ThesisUpdate",
    "WatchlistItem",
    "IngestResult",
    "add",
    "add_thesis_update",
    "connect",
    "default_db_path",
    "find",
    "get_by_id",
    "get_by_key",
    "history",
    "init_db",
    "list_thesis_updates",
    "remove",
    "update",
    "upsert",
    "ingest_data",
    "ingest_file",
    "render_history",
    "render_list_table",
    "render_show",
    "render_thesis_updates",
]
