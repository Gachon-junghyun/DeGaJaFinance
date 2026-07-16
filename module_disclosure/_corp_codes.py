"""DART 전체 기업코드(corp_code) 다운로드/캐시.

OpenDART는 6자리 종목코드(stock_code)와 8자리 corp_code를 분리 관리하므로
list.json 호출 전에 매핑 테이블이 필요하다. 5MB 정도라 한 번 받아서 CSV로 캐시.

캐시 위치: 모듈 폴더 내 corp_codes.csv (TTL 7일).
"""
from __future__ import annotations

import io
import os
import zipfile
from pathlib import Path
from typing import Optional
from xml.etree import ElementTree as ET

import requests

_BASE = "https://opendart.fss.or.kr/api"
_CACHE_PATH = Path(__file__).resolve().parent / "corp_codes.csv"
_TTL_DAYS = 7


def _api_key() -> str:
    key = os.environ.get("DART_API_KEY", "").strip()
    if not key:
        raise RuntimeError(
            "DART_API_KEY 환경변수가 필요합니다. "
            "https://opendart.fss.or.kr 에서 발급 후 .env 또는 셸에 설정하세요."
        )
    return key


def _is_fresh(path: Path) -> bool:
    if not path.exists():
        return False
    import time
    age_sec = time.time() - path.stat().st_mtime
    return age_sec < _TTL_DAYS * 86400


def refresh_corp_codes(force: bool = False) -> Path:
    """corp_codes.csv 캐시를 다운로드/갱신하고 경로를 반환."""
    if not force and _is_fresh(_CACHE_PATH):
        return _CACHE_PATH

    resp = requests.get(
        f"{_BASE}/corpCode.xml",
        params={"crtfc_key": _api_key()},
        timeout=30,
    )
    resp.raise_for_status()

    with zipfile.ZipFile(io.BytesIO(resp.content)) as z:
        xml_bytes = z.read(z.namelist()[0])

    root = ET.fromstring(xml_bytes)
    rows = []
    for item in root.findall("list"):
        rows.append(
            (
                (item.findtext("corp_code") or "").strip(),
                (item.findtext("corp_name") or "").strip(),
                (item.findtext("stock_code") or "").strip(),
                (item.findtext("modify_date") or "").strip(),
            )
        )

    _CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with _CACHE_PATH.open("w", encoding="utf-8", newline="") as f:
        f.write("corp_code,corp_name,stock_code,modify_date\n")
        for r in rows:
            f.write(",".join(r) + "\n")
    return _CACHE_PATH


def _load_cache() -> list[dict]:
    if not _CACHE_PATH.exists():
        refresh_corp_codes()
    rows: list[dict] = []
    with _CACHE_PATH.open("r", encoding="utf-8") as f:
        next(f)
        for line in f:
            parts = line.rstrip("\n").split(",")
            if len(parts) < 4:
                continue
            rows.append(
                {
                    "corp_code": parts[0],
                    "corp_name": parts[1],
                    "stock_code": parts[2],
                    "modify_date": parts[3],
                }
            )
    return rows


def resolve_corp_code(stock_or_name: str) -> Optional[tuple[str, str]]:
    """6자리 종목코드 또는 기업명을 받아 (corp_code, corp_name) 을 반환.

    상장사가 아닌 corp_code 도 캐시에 섞여 있어 stock_code 일치를 우선한다.
    """
    s = stock_or_name.strip()
    rows = _load_cache()

    if s.isdigit() and len(s) == 6:
        for r in rows:
            if r["stock_code"] == s:
                return r["corp_code"], r["corp_name"]
        return None

    exact = [r for r in rows if r["corp_name"] == s and r["stock_code"]]
    if exact:
        return exact[0]["corp_code"], exact[0]["corp_name"]
    partial = [r for r in rows if s in r["corp_name"] and r["stock_code"]]
    if partial:
        return partial[0]["corp_code"], partial[0]["corp_name"]
    return None
