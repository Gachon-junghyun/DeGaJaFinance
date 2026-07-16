# COPIED FROM: HAN_LAB/core/publish.py
# COPIED AT: 2026-05-15
# REASON: mvp가 HAN_LAB 모듈 의존 회피. 단순 shutil 로직이라 self-contained가 깔끔
# REMERGE?: no
"""작업 산출물(.md/.pptx/.pdf 등)을 외부 폴더(Google Drive 등)로 단방향 복사.

양방향 동기화가 아니라 "퍼블리시" 패턴 — 호출 시점에 한 번 push.
폰/태블릿에서 외부 디바이스로 작업 결과만 보고 싶을 때 사용.
"""
from __future__ import annotations

import shutil
from pathlib import Path
from typing import Iterable

# 기본 확장자 — 문서/보고서/슬라이드만 (이미지, 로그, 임시 파일 제외)
DEFAULT_EXTS = (".md", ".txt", ".pptx", ".ppt", ".pdf", ".docx")


def publish_to_drive(
    source_dir: str | Path,
    dest_dir: str | Path,
    exts: Iterable[str] = DEFAULT_EXTS,
    recursive: bool = False,
) -> list[Path]:
    """source_dir 안의 지정 확장자 파일만 dest_dir로 복사 (덮어쓰기).

    - `~$` 접두 파일(Office 락 파일)은 자동 스킵
    - recursive=False(기본)면 최상위만, True면 하위 폴더까지 평탄화 복사
    - dest_dir이 없으면 생성

    Returns:
        복사된 파일의 목적지 경로 리스트
    """
    src = Path(source_dir).expanduser()
    dst = Path(dest_dir).expanduser()

    if not src.is_dir():
        raise FileNotFoundError(f"source_dir not found: {src}")

    dst.mkdir(parents=True, exist_ok=True)

    exts_set = {
        (e if e.startswith(".") else f".{e}").lower() for e in exts
    }
    pattern = "**/*" if recursive else "*"

    copied: list[Path] = []
    for path in src.glob(pattern):
        if not path.is_file():
            continue
        if path.name.startswith("~$"):  # 오피스 락 파일
            continue
        if path.suffix.lower() not in exts_set:
            continue
        target = dst / path.name
        shutil.copy2(path, target)
        copied.append(target)

    return copied
