# -*- coding: utf-8 -*-
"""뉴스 검색 API 서버 — 서버 PC 에서 뉴스 DB(news_fts)를 HTTP 로 노출한다.

취지: 서버 PC 한 대가 뉴스를 수집(run_fetch_loop)하고 이 API 로 조회를 서빙한다.
다른 PC(또는 Claude Code)는 DB 파일을 직접 열지 않고 `DEGAJA_NEWS_API` 만 켜서
같은 `module_news_data …` CLI 로 원격 실행한다. 클라이언트 로컬 뉴스 DB 를 지워도 동작.

의존성 = 표준 라이브러리만(http.server) — CLAUDE.md 규약 준수.
쿼리·분석 로직은 재구현하지 않고 **module_news_data 의 파서/함수를 그대로 재사용**(P1):
클라이언트가 보낸 argv 를 같은 CLI 파서로 파싱해 실행하고 stdout 을 캡처해 돌려준다.

엔드포인트:
  GET /health                → {"ok":true, "db":…, "present":…}
  GET /exec?argv=fts&argv=search&argv=Micron&argv=--days&argv=3&argv=--scope&argv=foreign
                             → {"stdout": "<렌더된 텍스트>"}  (조회 서브커맨드만 허용)

실행: python Server/news_api.py            (기본 0.0.0.0:8787, 인자로 포트 변경)
보안: 조회(READ)만 화이트리스트 — fetch·fts build/update(쓰기)는 거부.
"""
from __future__ import annotations

import contextlib
import io
import json
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

# 리포 루트를 path 에 올려 module_news_data 를 import (Server/ 는 하위 폴더)
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from module_news_data._config import FTS_DB, FTS_DB_KR, NEWS_API_PORT, NEWS_DB  # noqa: E402
from module_news_data.__main__ import DB_READ_CMDS, build_parser  # noqa: E402

# 원격 실행 허용 = DB 를 읽는 조회 서브커맨드만. 쓰기(fetch·fts build/update)는 서버 콘솔에서만.
# ⚠ 목록을 여기 다시 적지 않는다(P1) — 예전에 복붙본이 있었고, 클라이언트에 서브커맨드를
# 추가했을 때 이쪽만 안 고쳐져 원격에서 "실행 불가"로 거부되는 사고가 났다. 단일 원본은
# `__main__.DB_READ_CMDS`(CLI 파서와 같은 파일) — 거기 등록하면 서버가 자동으로 따라온다.
READ_CMDS = DB_READ_CMDS


def _run_argv(argv: list[str]) -> dict:
    """argv 를 CLI 파서로 실행하고 stdout+stderr 를 캡처해 반환. 조회만 허용."""
    if not argv:
        return {"error": "argv 비어있음"}
    if argv[0] not in READ_CMDS:
        return {"error": f"'{argv[0]}' 는 원격 실행 불가(조회 전용). 허용: {sorted(READ_CMDS)}"}
    if argv[0] == "fts" and (len(argv) < 2 or argv[1] != "search"):
        return {"error": "fts 는 search 만 원격 허용(build/update 는 서버 콘솔에서)."}
    buf = io.StringIO()
    try:
        ns = build_parser().parse_args(argv)
    except SystemExit:                       # argparse 인자 오류
        return {"error": f"인자 파싱 실패: {' '.join(argv)}"}
    try:
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
            ns.func(ns)
    except Exception as exc:                  # noqa: BLE001
        return {"error": f"실행 오류: {exc!r}", "stdout": buf.getvalue()}
    return {"stdout": buf.getvalue()}


class Handler(BaseHTTPRequestHandler):
    server_version = "DeGaJaNewsAPI/1.1"

    def _send(self, obj, code=200):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        sys.stderr.write("  api %s - %s\n" % (self.address_string(), fmt % args))

    def do_GET(self):  # noqa: N802
        u = urlparse(self.path)
        qs = parse_qs(u.query)
        try:
            if u.path == "/health":
                return self._send({
                    "ok": True,
                    "db": {"news": str(NEWS_DB), "fts": str(FTS_DB), "fts_kr": str(FTS_DB_KR)},
                    "present": {"news": NEWS_DB.exists(), "fts": FTS_DB.exists(),
                                "fts_kr": FTS_DB_KR.exists()},
                    "read_cmds": sorted(READ_CMDS),
                })
            if u.path == "/exec":
                argv = qs.get("argv") or []
                return self._send(_run_argv(argv))
            return self._send({"error": f"unknown path {u.path}"}, 404)
        except Exception as exc:  # noqa: BLE001
            return self._send({"error": f"server error: {exc!r}"}, 500)


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    port = int(sys.argv[1]) if len(sys.argv) > 1 else NEWS_API_PORT
    srv = ThreadingHTTPServer(("0.0.0.0", port), Handler)
    print(f"[news_api] serving on 0.0.0.0:{port}  (DB: {FTS_DB})")
    print(f"[news_api] health: http://127.0.0.1:{port}/health")
    print(f"[news_api] 원격 허용 조회: {sorted(READ_CMDS)}  (fetch·build/update 거부)")
    print("[news_api] Ctrl+C 로 종료")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\n[news_api] stopped")
        srv.shutdown()


if __name__ == "__main__":
    main()
