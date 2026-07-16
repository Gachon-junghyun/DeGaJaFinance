# -*- coding: utf-8 -*-
"""module_epistemics 설정 — 인식 루프의 원장·레지스트리 경로.

epistemics/ = 지식 vault(민감도 원장·verify 레지스트리·감사 로그). 코드가 아니라
축적되는 마크다운/JSON. 종목 id = 티커/6자리 코드 그대로(canon 그래프 미빌드라 단순화).
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent
EPI_DIR = Path(os.environ.get("DEGAJA_EPISTEMICS_DIR", REPO_ROOT / "epistemics"))

SENSITIVITY_DIR = EPI_DIR / "sensitivity"      # {id}.md — 종목별 민감도 원장
VERIFY_DIR = EPI_DIR / "verify"                # registry.json + units/
VERIFY_REGISTRY = VERIFY_DIR / "registry.json"
REGISTRY_JSON = EPI_DIR / "registry.json"      # 코드↔맵 capability 맵(감사 시드)
AUDIT_MD = EPI_DIR / "REGISTRY_AUDIT.md"
AUDIT_LOG = EPI_DIR / "REGISTRY_AUDIT_LOG.jsonl"

# 감사 대상 = 이 리포의 실행 표면
MODULE_GLOB = "module_*"
SCRIPTS_DIR = REPO_ROOT / "scripts"
MODULE_MAP = REPO_ROOT / "MODULE_MAP.md"        # 사람이 관리하는 문서 맵(문서화 판정 소스)


def canon(token: str) -> str:
    """종목 토큰 정규화 — .KS/.KQ 접미사 제거, 대문자(US)/6자리(KR) 유지."""
    t = token.strip()
    if "." in t:
        stem = t.split(".")[0]
        if stem.isdigit():
            return stem
    return t if t.isdigit() else t.upper()


def utf8_stdout() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
