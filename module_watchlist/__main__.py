"""CLI 진입점. `python -m module_watchlist <subcommand> --help` 로 사용법 확인."""
from __future__ import annotations

import argparse
import io
import json
import sys
from pathlib import Path
from typing import Optional

from . import _db
from ._db import (
    IMPORTANCE_VALUES,
    STATUS_VALUES,
    THESIS_IMPACT_VALUES,
    WatchlistItem,
)
from ._ingest import ingest_file
from ._renderer import (
    render_history,
    render_list_table,
    render_show,
    render_thesis_updates,
)


def _utf8_stdout() -> None:
    if sys.stdout.encoding and sys.stdout.encoding.lower().startswith("utf"):
        return
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


def _split_csv(value: Optional[str]) -> list[str]:
    if not value:
        return []
    return [v.strip() for v in value.split(",") if v.strip()]


def _resolve_target(conn, target: str) -> Optional[WatchlistItem]:
    """숫자면 id, 아니면 item LIKE 매칭으로 단일 후보 반환."""
    if target.isdigit():
        return _db.get_by_id(conn, int(target))
    matches = _db.find(conn, text=target, limit=10)
    if len(matches) == 1:
        return matches[0]
    if not matches:
        return None
    print(f"여러 항목이 매칭됨 ({len(matches)}건). id 로 다시 호출:", file=sys.stderr)
    print(render_list_table(matches), file=sys.stderr)
    return None


# ─────────────────────────────── subcommand handlers ───────────────────────────────


def cmd_init(args: argparse.Namespace) -> int:
    path = _db.init_db(Path(args.db) if args.db else None)
    print(f"watchlist.db ready at {path}")
    return 0


def cmd_add(args: argparse.Namespace) -> int:
    item = WatchlistItem(
        thesis=args.thesis,
        item=args.item,
        trigger_criteria=args.trigger,
        importance=args.importance,
        status=args.status or "open",
        tickers=_split_csv(args.tickers),
        resolution_note=args.resolution_note,
        thesis_impact=args.thesis_impact,
    )
    with _db.connect(Path(args.db) if args.db else None) as conn:
        try:
            wid = _db.add(conn, item, source=args.source or "cli:add")
        except Exception as exc:  # noqa: BLE001
            print(f"add 실패: {exc}", file=sys.stderr)
            return 2
    print(f"created id={wid}")
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    with _db.connect(Path(args.db) if args.db else None) as conn:
        items = _db.find(
            conn,
            thesis=args.thesis,
            status=args.status,
            importance=args.importance,
            ticker=args.ticker,
            limit=args.limit,
        )
        if args.json:
            print(json.dumps([i.to_dict() for i in items], ensure_ascii=False, indent=2))
        else:
            print(render_list_table(items))
    return 0


def cmd_show(args: argparse.Namespace) -> int:
    with _db.connect(Path(args.db) if args.db else None) as conn:
        item = _resolve_target(conn, args.target)
        if not item:
            print(f"not found: {args.target}", file=sys.stderr)
            return 1
        if args.json:
            print(json.dumps(item.to_dict(), ensure_ascii=False, indent=2))
        else:
            print(render_show(item))
    return 0


def cmd_update(args: argparse.Namespace) -> int:
    tickers = _split_csv(args.tickers) if args.tickers is not None else None
    with _db.connect(Path(args.db) if args.db else None) as conn:
        item = _resolve_target(conn, args.target)
        if not item:
            print(f"not found: {args.target}", file=sys.stderr)
            return 1
        try:
            updated = _db.update(
                conn,
                item.id,  # type: ignore[arg-type]
                thesis=args.thesis,
                item=args.item,
                trigger_criteria=args.trigger,
                importance=args.importance,
                status=args.status,
                tickers=tickers,
                resolution_note=args.resolution_note,
                thesis_impact=args.thesis_impact,
                source=args.source or "cli:update",
            )
            if (
                args.thesis_update_before is not None
                or args.thesis_update_after is not None
            ):
                _db.add_thesis_update(
                    conn,
                    updated.thesis,
                    item=updated.item,
                    before_text=args.thesis_update_before,
                    after_text=args.thesis_update_after,
                    source=args.source or "cli:update",
                )
        except Exception as exc:  # noqa: BLE001
            print(f"update 실패: {exc}", file=sys.stderr)
            return 2
    print(render_show(updated))
    return 0


def cmd_remove(args: argparse.Namespace) -> int:
    with _db.connect(Path(args.db) if args.db else None) as conn:
        item = _resolve_target(conn, args.target)
        if not item:
            print(f"not found: {args.target}", file=sys.stderr)
            return 1
        ok = _db.remove(conn, item.id)  # type: ignore[arg-type]
    print(f"{'removed' if ok else 'no-op'} id={item.id}")
    return 0 if ok else 1


def cmd_search(args: argparse.Namespace) -> int:
    with _db.connect(Path(args.db) if args.db else None) as conn:
        items = _db.find(conn, text=args.query, limit=args.limit)
        if args.json:
            print(json.dumps([i.to_dict() for i in items], ensure_ascii=False, indent=2))
        else:
            print(render_list_table(items))
    return 0


def cmd_history(args: argparse.Namespace) -> int:
    with _db.connect(Path(args.db) if args.db else None) as conn:
        item = _resolve_target(conn, args.target)
        if not item:
            print(f"not found: {args.target}", file=sys.stderr)
            return 1
        rows = _db.history(conn, item.id)  # type: ignore[arg-type]
        print(render_history(item, rows))
    return 0


def cmd_updates(args: argparse.Namespace) -> int:
    with _db.connect(Path(args.db) if args.db else None) as conn:
        rows = _db.list_thesis_updates(conn, thesis=args.thesis, item=args.item, limit=args.limit)
        if args.json:
            print(
                json.dumps(
                    [
                        {
                            "id": u.id,
                            "thesis": u.thesis,
                            "item": u.item,
                            "before_text": u.before_text,
                            "after_text": u.after_text,
                            "source": u.source,
                            "changed_at": u.changed_at,
                        }
                        for u in rows
                    ],
                    ensure_ascii=False,
                    indent=2,
                )
            )
        else:
            print(render_thesis_updates(rows))
    return 0


def cmd_ingest(args: argparse.Namespace) -> int:
    path = Path(args.path)
    if not path.exists():
        print(f"file not found: {path}", file=sys.stderr)
        return 1
    with _db.connect(Path(args.db) if args.db else None) as conn:
        result = ingest_file(conn, path, source=args.source)
    print(
        f"ingested: created={result.created} updated={result.updated} "
        f"noop={result.noop} thesis_updates={result.thesis_updates}"
    )
    if result.errors:
        print("errors:", file=sys.stderr)
        for e in result.errors:
            print(f"  - {e}", file=sys.stderr)
        return 2 if not result.total else 0
    return 0


# ────────────────────────────────── parser build ──────────────────────────────────


def _add_db_arg(p: argparse.ArgumentParser) -> None:
    p.add_argument("--db", help="watchlist.db 경로 (기본: WATCHLIST_DB_PATH 또는 research_Mvp/watchlist.db)")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="module_watchlist",
        description=(
            "thesis 단위 watchlist DB. "
            "status: open|partial|resolved|split|rejected, "
            "importance: high|mid|low, "
            "thesis_impact: 강화|부분|부정|정보공백."
        ),
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("init", help="watchlist.db 스키마 생성/갱신")
    _add_db_arg(p)
    p.set_defaults(func=cmd_init)

    p = sub.add_parser("add", help="새 watchlist 항목 추가")
    p.add_argument("--thesis", required=True, help="thesis 라벨 (예: 전력인프라)")
    p.add_argument("--item", required=True, help="항목 본문 (예: 한수원 SMR 6월 부지 결정)")
    p.add_argument("--trigger", help="trigger_criteria")
    p.add_argument("--importance", choices=IMPORTANCE_VALUES, help="중요도")
    p.add_argument("--status", choices=STATUS_VALUES, help="기본 open")
    p.add_argument("--tickers", help="콤마 구분 (예: 052690,298040)")
    p.add_argument("--resolution-note", dest="resolution_note", help="검증 결과 메모")
    p.add_argument("--thesis-impact", dest="thesis_impact", choices=THESIS_IMPACT_VALUES)
    p.add_argument("--source", help="history 의 note 컬럼 (기본 cli:add)")
    _add_db_arg(p)
    p.set_defaults(func=cmd_add)

    p = sub.add_parser("list", help="필터 조건으로 목록 조회")
    p.add_argument("--thesis")
    p.add_argument("--status", choices=STATUS_VALUES)
    p.add_argument("--importance", choices=IMPORTANCE_VALUES)
    p.add_argument("--ticker", help="해당 ticker 가 포함된 항목만")
    p.add_argument("--limit", type=int, default=200)
    p.add_argument("--json", action="store_true")
    _add_db_arg(p)
    p.set_defaults(func=cmd_list)

    p = sub.add_parser("show", help="단일 항목 상세 (id 또는 item 부분일치)")
    p.add_argument("target", help="id (숫자) 또는 item 부분 문자열")
    p.add_argument("--json", action="store_true")
    _add_db_arg(p)
    p.set_defaults(func=cmd_show)

    p = sub.add_parser("update", help="필드 갱신 + history 자동 기록")
    p.add_argument("target", help="id 또는 item 부분 문자열")
    p.add_argument("--thesis")
    p.add_argument("--item")
    p.add_argument("--trigger")
    p.add_argument("--importance", choices=IMPORTANCE_VALUES)
    p.add_argument("--status", choices=STATUS_VALUES)
    p.add_argument("--tickers", help="콤마 구분 — 빈 문자열도 reset 으로 인식 안 됨, --tickers '' 미지원")
    p.add_argument("--resolution-note", dest="resolution_note")
    p.add_argument("--thesis-impact", dest="thesis_impact", choices=THESIS_IMPACT_VALUES)
    p.add_argument(
        "--thesis-update-before",
        dest="thesis_update_before",
        help="thesis_updates 테이블에 변경 전 텍스트 추가",
    )
    p.add_argument(
        "--thesis-update-after",
        dest="thesis_update_after",
        help="thesis_updates 테이블에 변경 후 텍스트 추가",
    )
    p.add_argument("--source")
    _add_db_arg(p)
    p.set_defaults(func=cmd_update)

    p = sub.add_parser("remove", help="항목 삭제 (history도 같이 삭제)")
    p.add_argument("target", help="id 또는 item 부분 문자열")
    _add_db_arg(p)
    p.set_defaults(func=cmd_remove)

    p = sub.add_parser("search", help="자유 텍스트 검색 (item/trigger/resolution/thesis)")
    p.add_argument("query")
    p.add_argument("--limit", type=int, default=50)
    p.add_argument("--json", action="store_true")
    _add_db_arg(p)
    p.set_defaults(func=cmd_search)

    p = sub.add_parser("history", help="필드 변경 로그")
    p.add_argument("target", help="id 또는 item 부분 문자열")
    _add_db_arg(p)
    p.set_defaults(func=cmd_history)

    p = sub.add_parser("updates", help="thesis_updates 표 (변경 전/후)")
    p.add_argument("--thesis")
    p.add_argument("--item")
    p.add_argument("--limit", type=int, default=200)
    p.add_argument("--json", action="store_true")
    _add_db_arg(p)
    p.set_defaults(func=cmd_updates)

    p = sub.add_parser(
        "ingest",
        help="JSON 일괄 import (Form A items / Form B verifications)",
        description=(
            "JSON 형식 예시는 module_watchlist/_ingest.py docstring 참조. "
            "(thesis, item) 으로 upsert."
        ),
    )
    p.add_argument("path", help="JSON 파일 경로")
    p.add_argument("--source", help="history note (기본 ingest:<filename>)")
    _add_db_arg(p)
    p.set_defaults(func=cmd_ingest)

    return parser


def main(argv: Optional[list[str]] = None) -> int:
    _utf8_stdout()
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
