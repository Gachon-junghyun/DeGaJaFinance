# -*- coding: utf-8 -*-
"""뉴스 API 클라이언트 — 서버 PC 의 Server/news_api.py 에 HTTP 로 조회를 넘긴다.

stdlib(urllib)만 사용 — 새 서드파티 없음(CLAUDE.md 규약). `DEGAJA_NEWS_API` 가 켜졌을 때
`__main__` 이 DB 를 읽는 조회 서브커맨드의 argv 를 그대로 서버 `/exec` 로 보내고, 서버가
자기 로컬 DB 로 실행한 결과 텍스트를 받아 출력한다. 그래서 클라이언트는 뉴스 DB 가 없어도
(지웠어도) search·fts·coverage·blindspot·theme-age·chain-hop 이 전부 동작한다.
"""
from __future__ import annotations

import base64
import json
import os
from urllib.parse import urlencode
from urllib.request import Request, urlopen

_TIMEOUT = 60  # coverage/blindspot 등은 무거울 수 있어 넉넉히


def _headers() -> dict:
    """요청 헤더. 터널(ngrok) 노출 시 인증·경고우회 헤더를 자동 부착 — 없으면 기존과 동일.

    DEGAJA_NEWS_API_AUTH="user:pass" 가 있으면 HTTP Basic 헤더를 붙인다(서버 앞단
    ngrok --basic-auth 와 짝). ngrok-skip-browser-warning 은 무료 ngrok 의 브라우저
    인터스티셜을 건너뛴다 — 터널이 아닐 땐 서버가 무시하므로 붙어 있어도 무해.
    """
    h = {"ngrok-skip-browser-warning": "true"}
    auth = (os.environ.get("DEGAJA_NEWS_API_AUTH", "") or "").strip()
    if auth:
        token = base64.b64encode(auth.encode("utf-8")).decode("ascii")
        h["Authorization"] = f"Basic {token}"
    return h


def _get(base: str, path: str, params: dict, timeout: int | None = None) -> dict:
    q = urlencode(params, doseq=True)
    url = f"{base}{path}?{q}" if q else f"{base}{path}"
    try:
        req = Request(url, headers=_headers())
        with urlopen(req, timeout=timeout or _TIMEOUT) as r:
            return json.loads(r.read().decode("utf-8"))
    except Exception as exc:  # noqa: BLE001
        return {"error": f"뉴스 API 접속 실패({base}{path}): {exc!r} — 서버 PC 수집기/방화벽/"
                         f"DEGAJA_NEWS_API 확인. (비우면 로컬 DB 폴백)"}


def exec_remote(base: str, argv: list[str], timeout: int | None = None) -> dict:
    """조회 서브커맨드 argv 를 서버 /exec 에 넘겨 실행 → {"stdout": 텍스트} 또는 {"error":…}.

    `timeout` — 대량 반출(export)은 기본 60초로 모자라다. 호출부가 명령별로 넘긴다.
    """
    return _get(base, "/exec", {"argv": list(argv)}, timeout=timeout)


def health(base: str) -> dict:
    return _get(base, "/health", {})
