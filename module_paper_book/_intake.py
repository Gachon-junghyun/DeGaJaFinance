# -*- coding: utf-8 -*-
"""module_paper_book._intake — 데스크 리포트 → 실행가능 thesis 후보(결정론).

내가(데스크가) 만든 리포트를 읽어 '무엇이 지금 베팅가능한가'의 후보 원장을 뽑는다.
티커 유니버스 검증·태그 추출은 module_report_tags 재사용(P1, 복제 없음). 그 위에
프레시니스(🟢LIVE/🟡PARTIAL/🔴RESOLVED)·하드스탑·테마(섹션)·코어여부를 표면 파싱한다.

판단 없음(P4): 후보와 그 표면신호만 만든다. ENTER/EXIT 결정은 상위(프로토콜 DECIDE).
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from ._config import REPO_ROOT, market_of

# 프레시니스 이모지 → 라벨
_FRESH = {"🟢": "LIVE", "🟡": "PARTIAL", "🔴": "RESOLVED"}
# US 티커 오탐 방지용 대문자 토큰 stopword (report_tags 규약과 동형 + 확장)
_STOP = {
    "LIVE", "GO", "REAL", "NEW", "KR", "US", "II", "III", "IV", "OW", "UW", "RR", "TP",
    "OBV", "RSI", "MA", "RS", "COT", "PPI", "CPI", "FRED", "FX", "PEG", "EPS", "ETF",
    "AI", "DC", "MW", "GW", "SEMI", "FIN", "IT", "UTIL", "INDU", "ENRG", "MATR", "HLTH",
    "STPL", "DISC", "COMM", "RE", "GICS", "SPY", "NIM", "CRE", "ARR", "NRR", "YTD",
    "TACO", "PPA", "IPP", "EUV", "HBM", "GPU", "ASIC", "FY", "Q", "B", "A", "TX", "VA", "NY",
    "PARTIAL", "RESOLVED", "DRY", "RUN", "BUY", "SELL", "ADD", "TRIM", "EXIT", "HOLD",
}
_US_TOKEN = re.compile(r"\b[A-Z]{1,5}\b")
_KR_CODE = re.compile(r"\b\d{6}\b")
_STOP_NUM = re.compile(r"(?:스탑|stop)\D{0,4}\$?\s*([0-9]+(?:\.[0-9]+)?)", re.IGNORECASE)
_SECTION = re.compile(r"^#{1,4}\s*§?\s*([A-Z][A-Za-z /—\-]+)")


@dataclass
class Candidate:
    ticker: str
    market: str
    freshness: str                 # LIVE | PARTIAL | RESOLVED
    theme: str = ""                 # 섹션(SEMI/FIN/...) = 상관단위 태그
    stop: Optional[float] = None
    thesis: str = ""
    source_report: str = ""
    is_core: bool = False           # epicenter/tape-independent 코어 스타터 여부
    line: str = field(default="", repr=False)


def _validated(token: str, us_tickers: dict, kr_names: dict) -> bool:
    if token in _STOP:
        return False
    if token.isdigit():
        return token in kr_names
    return token in us_tickers


def _load_universe():
    """report_tags 의 유니버스 로더 재사용(P1). 실패 시 빈 dict(→ stopword-only)."""
    try:
        from module_report_tags._config import load_kr_names, load_us_tickers
        return load_us_tickers(), load_kr_names()
    except Exception:
        return {}, {}


def read_actionable(report_dir: Optional[Path] = None,
                    prefer=("BET_SHEET.md", "ACTION_TICKETS.md")) -> list[Candidate]:
    """리포트 디렉토리를 스캔해 실행가능 후보 원장을 만든다.

    report_dir 미지정 시 REPORT/ 아래 전부(인수인계 원장 소스). BET_SHEET/ACTION_TICKETS
    를 우선순위로 읽되, 발견되는 모든 .md 에서 프레시니스+티커 라인을 뽑는다.
    """
    us_tickers, kr_names = _load_universe()
    base = Path(report_dir) if report_dir else (REPO_ROOT / "REPORT")
    files = sorted(base.rglob("*.md"))
    # prefer 파일을 앞으로
    files.sort(key=lambda p: (0 if p.name in prefer else 1, str(p)))

    seen: dict[tuple, Candidate] = {}  # (ticker, source) 중복 억제
    for fp in files:
        try:
            text = fp.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        rel = str(fp.relative_to(base)) if str(fp).startswith(str(base)) else fp.name
        section = ""
        is_core_block = False
        for raw in text.splitlines():
            msec = _SECTION.match(raw.strip())
            if msec:
                section = msec.group(1).strip()[:24]
                is_core_block = "EPICENTER" in raw.upper() or "CORE-STARTER" in raw.upper()
            fresh = next((_FRESH[e] for e in _FRESH if e in raw), None)
            core_line = is_core_block or "CORE-STARTER" in raw.upper() or "tape-independent" in raw.lower()
            if not fresh and not core_line:
                continue
            fresh = fresh or "LIVE"  # 코어 스타터는 기본 LIVE
            stop_m = _STOP_NUM.search(raw)
            stop = float(stop_m.group(1)) if stop_m else None
            # 티커 추출(라인 내 + 볼드 강조 우선)
            toks = set(_US_TOKEN.findall(raw)) | set(_KR_CODE.findall(raw))
            for tk in toks:
                if not _validated(tk, us_tickers, kr_names):
                    continue
                key = (tk, rel)
                if key in seen:
                    # 더 강한 프레시니스로 승격(LIVE>PARTIAL>RESOLVED)
                    order = {"LIVE": 3, "PARTIAL": 2, "RESOLVED": 1}
                    if order[fresh] > order[seen[key].freshness]:
                        seen[key].freshness = fresh
                    continue
                seen[key] = Candidate(
                    ticker=tk, market=market_of(tk), freshness=fresh,
                    theme=section, stop=stop, source_report=rel,
                    is_core=bool(core_line), thesis=raw.strip()[:200], line=raw.strip(),
                )
    return list(seen.values())


def summarize(cands: list[Candidate]) -> dict:
    """후보 원장 요약(프레시니스별 카운트 + 코어 후보)."""
    by_fresh: dict[str, int] = {}
    for c in cands:
        by_fresh[c.freshness] = by_fresh.get(c.freshness, 0) + 1
    return {
        "n": len(cands),
        "by_freshness": by_fresh,
        "live": sorted({c.ticker for c in cands if c.freshness == "LIVE"}),
        "resolved_drop": sorted({c.ticker for c in cands if c.freshness == "RESOLVED"}),
        "core": sorted({c.ticker for c in cands if c.is_core}),
    }
