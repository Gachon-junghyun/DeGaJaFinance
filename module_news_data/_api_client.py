# -*- coding: utf-8 -*-
"""뉴스 API 클라이언트 — 서버 PC 의 Server/news_api.py 에 HTTP 로 검색을 끌어온다.

stdlib(urllib)만 사용 — 새 서드파티 없음(CLAUDE.md 규약). DEGAJA_NEWS_API 가 켜졌을 때
`_fts.search` 가 이 모듈을 통해 원격 검색하고, 결과 dict 를 로컬 query_fts 와 동일한
스키마로 돌려준다(그래서 _print_fts 가 로컬/원격을 구분 없이 렌더).
"""
from __future__ import annotations

import json
from urllib.parse import urlencode
from urllib.request import urlopen

_TIMEOUT = 20


def _get(base: str, path: str, params: dict) -> dict:
    q = urlencode({k: v for k, v in params.items() if v not in (None, False, "")}, doseq=True)
    url = f"{base}{path}?{q}" if q else f"{base}{path}"
    try:
        with urlopen(url, timeout=_TIMEOUT) as r:
            return json.loads(r.read().decode("utf-8"))
    except Exception as exc:  # noqa: BLE001
        return {"error": f"뉴스 API 접속 실패({base}{path}): {exc!r} — 서버 PC 수집기/방화벽 확인, "
                         f"또는 DEGAJA_NEWS_API 를 비워 로컬 DB 로 폴백."}


def fts_search(base: str, *, terms, days, scope, mode, use_syn, show_snip, limit,
               show_full=False, kr=False, count_only=False) -> dict:
    """서버의 /fts/search(또는 count_only 면 /fts/count) 호출 → query_fts 동일 스키마 dict."""
    params = {
        "terms": list(terms), "days": days, "scope": scope, "mode": mode,
        "syn": int(bool(use_syn)), "snippet": int(bool(show_snip)),
        "full": int(bool(show_full)), "kr": int(bool(kr)), "limit": limit,
    }
    if count_only:
        return _get(base, "/fts/count", params)
    return _get(base, "/fts/search", params)


def health(base: str) -> dict:
    return _get(base, "/health", {})
