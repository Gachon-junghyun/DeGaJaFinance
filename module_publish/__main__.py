"""CLI: md 산출물을 마운트된 드라이브 폴더로 퍼블리시.

사용법:
    python -m module_publish [<source>] [--drive-root <root>]
                             [--dest-name <name>] [--exts md,pdf] [--recursive]

환경변수:
    MVP_DRIVE_ROOT — 마운트된 드라이브 루트. --drive-root 인자로 덮어쓰기 가능.

기본 동작:
    source 기본값    : research_Mvp/llm_outputs/2026-05-15/bio_2026q2
    exts 기본값      : md
    dest-name 기본값 : source 디렉토리명 (예: bio_2026q2)

예:
    set MVP_DRIVE_ROOT=G:\내 드라이브\MVP_PUBLISH
    python -m module_publish
    python -m module_publish llm_outputs/2026-05-15/bio_2026q2 --dest-name bio_2026q2_yuhan
    python -m module_publish docs --exts md,pdf --recursive
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from ._copy import publish_to_drive

# 이번 작업 기본 산출물 위치 — 자주 호출될 곳을 기본값으로
DEFAULT_SOURCE = (
    Path(__file__).resolve().parent.parent
    / "llm_outputs" / "2026-05-15" / "bio_2026q2"
)


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="module_publish",
        description="md 산출물을 마운트된 드라이브 폴더로 퍼블리시",
    )
    parser.add_argument(
        "source",
        nargs="?",
        default=str(DEFAULT_SOURCE),
        help=f"원본 폴더 (기본: {DEFAULT_SOURCE})",
    )
    parser.add_argument(
        "--drive-root",
        default=os.environ.get("MVP_DRIVE_ROOT"),
        help="드라이브 루트 (환경변수 MVP_DRIVE_ROOT 대체 가능)",
    )
    parser.add_argument(
        "--dest-name",
        default=None,
        help="드라이브 안 목적 폴더명 (기본: source 디렉토리명)",
    )
    parser.add_argument(
        "--exts",
        default="md",
        help="복사할 확장자 (콤마 구분, 기본: md)",
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="하위 폴더까지 검색",
    )
    args = parser.parse_args()

    if not args.drive_root:
        print(
            "[ERROR] 드라이브 루트가 지정되지 않았습니다.\n"
            "  방법 1) 환경변수: set MVP_DRIVE_ROOT=<드라이브경로>\n"
            "  방법 2) 인자:     --drive-root \"<드라이브경로>\"",
            file=sys.stderr,
        )
        return 2

    source = Path(args.source).expanduser().resolve()
    if not source.is_dir():
        print(f"[ERROR] 원본 폴더가 없습니다: {source}", file=sys.stderr)
        return 2

    dest_name = args.dest_name or source.name
    dest = Path(args.drive_root).expanduser() / dest_name
    exts = [e.strip() for e in args.exts.split(",") if e.strip()]

    print(f"[publish] source : {source}")
    print(f"[publish] dest   : {dest}")
    print(f"[publish] exts   : {exts}")
    print(f"[publish] recur  : {args.recursive}")
    print()

    copied = publish_to_drive(
        source_dir=source,
        dest_dir=dest,
        exts=exts,
        recursive=args.recursive,
    )

    print(f"[publish] {len(copied)}개 파일 복사 완료 → {dest}")
    for p in copied:
        print(f"  - {p.name}")

    return 0 if copied else 1


if __name__ == "__main__":
    sys.exit(main())
