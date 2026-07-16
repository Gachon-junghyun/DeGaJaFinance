"""작업 산출물(.md 등)을 마운트된 외부 폴더(예: 동기화된 Google Drive)로 단방향 복사.

폰/태블릿 등 외부 디바이스에서 결과물을 열어보기 위한 "퍼블리시" 모듈.
양방향 sync 아님, 호출 시점에 한 번 push.

사용:
    from module_publish import publish_to_drive
    publish_to_drive(src, dst, exts=[".md"])

CLI:
    python -m module_publish <source> --drive-root <root>
"""
from ._copy import DEFAULT_EXTS, publish_to_drive

__all__ = ["publish_to_drive", "DEFAULT_EXTS"]
