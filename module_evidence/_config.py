# -*- coding: utf-8 -*-
"""module_evidence 설정 — 스캔 대상 경로 · ID 계열 · 출처/태그/링크 정규식.

**단일 원본은 md 다.** `data/evidence.db` 는 언제든 지우고 `build` 로 다시 만드는
파생물(`news_vectors.db` 와 같은 지위) — 사실 본문을 DB 에만 두지 않는다.

⚠️ FTS5 를 쓰지 않는다. KR 색인의 trigram 토크나이저는 **2글자 한글(수주·실적)을 0건**
으로 돌려주고(`module_news_data._fts` 상단 경고), 이 코퍼스는 1만 행 규모라 LIKE 스캔이
수십 ms 다 — 정확한 부분일치 + 2자 한글 가능이 색인 속도보다 값어치가 크다.
"""
from __future__ import annotations

import os
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent
DATA_DIR = Path(os.environ.get("DEGAJA_DATA_DIR", REPO_ROOT / "data"))

EVIDENCE_DB = DATA_DIR / "evidence.db"          # 파생물 — 커밋 대상 아님

# 스캔 소스. REPORT_DIR 은 report_tags 와 같은 환경변수를 따른다(같은 폴더를 두 이름으로
# 부르지 않는다 — P1).
HANDOFF_DIR = REPO_ROOT / "handoff"
REPORT_DIR = Path(os.environ.get("DEGAJA_REPORT_DIR", REPO_ROOT / "REPORT"))
RUNS_DIR = REPO_ROOT / "llm_outputs"

# ── ID 계열 ────────────────────────────────────────────────────────────────
# M 측정사실 · D 결함 · R 철회 · P 사전등록 · C 미해결충돌 · S 시나리오 · F 기타
FAMILIES = {
    "M": "측정된 사실",
    "D": "결함/재발",
    "R": "철회",
    "P": "사전등록(브래킷)",
    "C": "미해결 충돌",
    "S": "시나리오",
    "F": "기타",
}

# 점유 스캔용 — **백틱 또는 볼드로 감싼 형태만** 인정한다. 맨 `P50`(백분위)·`M2`(통화량)
# 같은 산문 토큰을 ID 로 오인하면 next-id 가 부풀어 영구히 번호를 건너뛴다.
ID_CORE = r"([MDRPCSF])-?(\d{1,4})(-KR|-US)?"
RE_ID_DECORATED = re.compile(r"(?:`|\*\*`?)" + ID_CORE + r"(?:`?\*\*|`)")
RE_ID_BARE = re.compile(r"\b" + ID_CORE + r"\b")

# ── 출처 토큰 (REPORT 줄 수확의 게이트) ────────────────────────────────────
SOURCE_PATTERNS = [
    r"module_[a-zA-Z_]+",
    r"scripts/[a-z_]+\.py",
    r"rcept_no=\d{10,}",
    r"\bDART\b", r"\bEDGAR\b", r"\bKIS\b", r"\bFRED\b", r"\bKRX\b",
    r"\byfinance\b", r"\bpykrx\b", r"\bSEC\b",
    r"사업보고서", r"반기보고서", r"분기보고서", r"공시",
    r"\b10-[KQ]\b", r"\b8-K\b", r"\b20-F\b",
    r"fts search", r"theme-age", r"chain-hop",
]
RE_SOURCE = re.compile("|".join(SOURCE_PATTERNS))

# 신뢰 태그 — HANDOVER 가 「[inferred] 는 증거로 재인용 금지」라 규정한 바로 그 라벨.
RE_TAG = re.compile(r"\[(measured|unverified|inferred|estimated|assumed)[^\]]{0,40}\]", re.I)

# ── 원자료 링크 ────────────────────────────────────────────────────────────
RE_RCEPT = re.compile(r"rcept_no=(\d{10,})")
RE_URL = re.compile(r"https?://[^\s)\]|>]+")
RE_ACCESSION = re.compile(r"\b(\d{10}-\d{2}-\d{6})\b")
DART_VIEWER = "https://dart.fss.or.kr/dsaf001/main.do?rcpNo={}"

RE_DATE = re.compile(r"\b(20\d{2}-\d{2}-\d{2})\b")
RE_KR_CODE = re.compile(r"\b(\d{6})\b")
RE_TICKER_TICK = re.compile(r"`([A-Z]{1,5})`")      # 백틱 US 티커만 — 산문 대문자어 오탐 차단

# 헤더 키워드 → 필드. 표마다 열 이름이 다르므로(실측 20종+) 키워드로 매핑한다.
HEADER_MAP = {
    "claim": ("fact", "claim", "finding", "dig", "사실", "주장", "증상", "measurement", "측정", "대상", "change", "rule"),
    "evidence": ("value", "why it matters", "killed by", "what killed it", "근거", "새 측정",
                 "positive-form remedy", "remedy", "note", "branch fired", "어떻게 발견됐나",
                 "이 런이 측정한 증거", "carry"),
    "source": ("source", "출처", "owner", "who held it", "누가 들고 있었나", "사람 승인 필요?"),
    "asof": ("asof", "date", "날짜", "registered", "event date", "scored on"),
    "run": ("run", "런"),
    "tag": ("tag", "태그"),
}


def utf8_stdout() -> None:
    """CLI 진입점 UTF-8 고정 (Windows cp949 크래시 방지)."""
    try:
        from module_news_data._config import utf8_stdout as _u
        _u()
    except Exception:                                        # noqa: BLE001
        import sys
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:                                    # noqa: BLE001
            pass


def iter_md(root: Path):
    """root 아래 .md — **점(.)으로 시작하는 경로는 전부 제외.**

    `handoff/.bak_20260805/` · `.RESEARCH.bak_0813us` 같은 백업이 살아있는데, 이걸 넣으면
    같은 ID 가 3~5중으로 잡혀 점유 판정과 인용 카운트가 전부 부풀어 오른다.
    """
    if not root.exists():
        return
    for p in sorted(root.rglob("*.md")):
        if any(part.startswith(".") for part in p.relative_to(root).parts):
            continue
        yield p
