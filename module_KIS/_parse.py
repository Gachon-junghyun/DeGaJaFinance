# FILE: research_Mvp/module_kis/_parse.py
"""KIS 응답 문자열 → 숫자 변환 헬퍼.

KIS는 모든 수치를 문자열로 준다('72500', '-1500', '', '0.00'). 결측은 ''.
"""
from __future__ import annotations

from typing import Optional


def to_float(s) -> Optional[float]:
    if s is None:
        return None
    s = str(s).replace(",", "").strip()
    if s in ("", "-", "N/A"):
        return None
    try:
        return float(s)
    except ValueError:
        return None


def to_int(s) -> Optional[int]:
    v = to_float(s)
    return int(v) if v is not None else None


def norm_code(code: str) -> str:
    """종목코드를 6자리 zero-pad. '5930' → '005930'."""
    return str(code).strip().zfill(6)
