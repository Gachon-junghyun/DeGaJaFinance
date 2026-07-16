# -*- coding: utf-8 -*-
"""뉴스 검색 API 서버 — 서버 PC 에서 뉴스 DB(news_fts) 를 HTTP 로 노출한다.

취지: 서버 PC 한 대가 뉴스를 수집(run_fetch_loop)하고 이 API 로 검색을 서빙한다.
다른 PC(또는 Claude Code)는 DB 파일을 직접 열지 않고 `DEGAJA_NEWS_API` 만 켜서
같은 `module_news_data fts search …` CLI 로 원격 검색을 끌어온다.

의존성 = 표준 라이브러리만(http.server) — CLAUDE.md 규약(서드파티 추가 전 사람 확인) 준수.
쿼리 로직은 재구현하지 않고 module_news_data._fts.query_fts 를 그대로 재사용(P1).

엔드포인트:
  GET /health                          → {"ok":true, "db":…, "counts":…}
  GET /fts/search?terms=A&terms=B&days=14&scope=foreign&mode=and&snippet=1&limit=40[&kr=1][&syn=1][&full=1]
  GET /fts/count?terms=…&days=…&scope=…  → {"count":N}

실행: python Server/news_api.py            (기본 0.0.0.0:8787, DEGAJA_NEWS_API_PORT 로 변경)
"""
from __future__ import annotations

import json
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

# 리포 루트를 path 에 올려 module_news_data 를 import (Server/ 는 하위 폴더)
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from module_news_data._config import (  # noqa: E402
    FTS_DB, FTS_DB_KR, NEWS_API_PORT, NEWS_DB,
)
from module_news_data._fts import query_fts  # noqa: E402


def _one(qs: dict, key: str, default=None):
    v = qs.get(key)
    return v[0] if v else default


def _int(qs: dict, key: str, default=None):
    v = _one(qs, key)
    try:
        return int(v) if v is not None else default
    except (TypeError, ValueError):
        return default


def _bool(qs: dict, key: str) -> bool:
    return _one(qs, key, "0") in ("1", "true", "True", "yes")


class Handler(BaseHTTPRequestHandler):
    server_version = "DeGaJaNewsAPI/1.0"

    def _send(self, obj, code=200):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):  # quieter, one-line
        sys.stderr.write("  api %s - %s\n" % (self.address_string(), fmt % args))

    def do_GET(self):  # noqa: N802
        u = urlparse(self.path)
        qs = parse_qs(u.query)
        try:
            if u.path == "/health":
                return self._send({
                    "ok": True,
                    "db": {"news": str(NEWS_DB), "fts": str(FTS_DB), "fts_kr": str(FTS_DB_KR)},
                    "present": {"news": NEWS_DB.exists(), "fts": FTS_DB.exists(), "fts_kr": FTS_DB_KR.exists()},
                })
            if u.path in ("/fts/search", "/fts/count"):
                terms = qs.get("terms") or []
                if not terms:
                    return self._send({"error": "terms 파라미터 필요"}, 400)
                data = query_fts(
                    terms=terms,
                    days=_int(qs, "days"),
                    scope=_one(qs, "scope", "all"),
                    mode=_one(qs, "mode", "and"),
                    use_syn=_bool(qs, "syn"),
                    show_snip=_bool(qs, "snippet"),
                    limit=_int(qs, "limit", 40),
                    show_full=_bool(qs, "full"),
                    kr=_bool(qs, "kr"),
                    count_only=(u.path == "/fts/count"),
                )
                return self._send(data)
            return self._send({"error": f"unknown path {u.path}"}, 404)
        except Exception as exc:  # noqa: BLE001
            return self._send({"error": f"server error: {exc!r}"}, 500)


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    port = NEWS_API_PORT
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    srv = ThreadingHTTPServer(("0.0.0.0", port), Handler)
    print(f"[news_api] serving on 0.0.0.0:{port}  (DB: {FTS_DB})")
    print(f"[news_api] health: http://127.0.0.1:{port}/health")
    print("[news_api] Ctrl+C 로 종료")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\n[news_api] stopped")
        srv.shutdown()


if __name__ == "__main__":
    main()
