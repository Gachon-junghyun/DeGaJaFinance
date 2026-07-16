"""저수준 CDP(Chrome DevTools Protocol) 클라이언트.

원격 디버깅 포트(기본 9222)로 떠 있는 크롬에 붙어 페이지 타깃을 조작한다.
의존성: requests(타깃 목록 HTTP) + websocket-client(명령 채널). pychrome 불필요.

설계 원칙:
- 동기식(요청→응답 매칭). 이벤트는 큐에 쌓아두고 필요 시 소비.
- 대부분의 상호작용은 Runtime.evaluate(JS 주입)로 — DOM 인지·React 친화.
- 신뢰 이벤트(isTrusted)가 필요한 위젯은 Input.dispatch*로 보강(_native).
"""
from __future__ import annotations

import json
import time
from typing import Any, Optional

import requests
import websocket  # websocket-client


class CDPError(RuntimeError):
    pass


class CDPClient:
    """단일 페이지 타깃에 붙는 CDP 세션."""

    def __init__(self, ws_url: str, timeout: float = 20.0):
        # 크롬 111+/149는 Origin 헤더 있는 WS를 403 거부(브라우저 위장 차단).
        # 비브라우저 CDP 클라이언트는 Origin을 빼야 허용된다(suppress_origin).
        self._ws = websocket.create_connection(ws_url, max_size=None, suppress_origin=True)
        self._ws.settimeout(timeout)
        self._id = 0
        self._timeout = timeout

    # ── 연결 팩토리 ────────────────────────────────────────────────
    @classmethod
    def endpoint(cls, host: str = "localhost", port: int = 9222) -> str:
        return f"http://{host}:{port}"

    @classmethod
    def list_targets(cls, host: str = "localhost", port: int = 9222) -> list[dict]:
        r = requests.get(f"{cls.endpoint(host, port)}/json", timeout=5)
        r.raise_for_status()
        return r.json()

    @classmethod
    def version(cls, host: str = "localhost", port: int = 9222) -> dict:
        r = requests.get(f"{cls.endpoint(host, port)}/json/version", timeout=5)
        r.raise_for_status()
        return r.json()

    @classmethod
    def attach(
        cls,
        host: str = "localhost",
        port: int = 9222,
        *,
        match_url: Optional[str] = None,
        match_title: Optional[str] = None,
        index: int = 0,
        timeout: float = 20.0,
    ) -> "CDPClient":
        """조건에 맞는 page 타깃에 붙는다. match_* 없으면 index번째 page."""
        pages = [t for t in cls.list_targets(host, port) if t.get("type") == "page"]
        if not pages:
            raise CDPError("page 타깃이 없다 (크롬에 열린 탭이 없음?)")
        picked = None
        if match_url:
            picked = next((t for t in pages if match_url.lower() in (t.get("url") or "").lower()), None)
        if picked is None and match_title:
            picked = next((t for t in pages if match_title.lower() in (t.get("title") or "").lower()), None)
        if picked is None:
            if match_url or match_title:
                raise CDPError(f"매칭 타깃 없음 (url~{match_url} title~{match_title})")
            picked = pages[index]
        ws = picked.get("webSocketDebuggerUrl")
        if not ws:
            raise CDPError("webSocketDebuggerUrl 부재 — 다른 devtools가 이미 붙어있을 수 있음")
        cli = cls(ws, timeout=timeout)
        cli.target = picked
        return cli

    # ── 명령 채널 ──────────────────────────────────────────────────
    def send(self, method: str, params: Optional[dict] = None) -> dict:
        self._id += 1
        mid = self._id
        self._ws.send(json.dumps({"id": mid, "method": method, "params": params or {}}))
        deadline = time.time() + self._timeout
        while time.time() < deadline:
            try:
                raw = self._ws.recv()
            except websocket.WebSocketTimeoutException:
                raise CDPError(f"{method} 응답 타임아웃")
            if not raw:
                continue
            msg = json.loads(raw)
            if msg.get("id") == mid:
                if "error" in msg:
                    raise CDPError(f"{method} 실패: {msg['error']}")
                return msg.get("result", {})
            # 그 외는 이벤트 — 지금은 버림(필요 시 확장)
        raise CDPError(f"{method} 응답 못 받음")

    def enable_domains(self) -> None:
        for d in ("Page", "Runtime", "DOM"):
            try:
                self.send(f"{d}.enable")
            except CDPError:
                pass

    # ── JS 실행 ───────────────────────────────────────────────────
    def eval(self, expression: str, *, await_promise: bool = True, return_by_value: bool = True) -> Any:
        res = self.send(
            "Runtime.evaluate",
            {
                "expression": expression,
                "returnByValue": return_by_value,
                "awaitPromise": await_promise,
                "userGesture": True,
            },
        )
        if res.get("exceptionDetails"):
            exc = res["exceptionDetails"]
            txt = exc.get("exception", {}).get("description") or exc.get("text")
            raise CDPError(f"JS 예외: {txt}")
        return res.get("result", {}).get("value")

    # ── 네비게이션 ────────────────────────────────────────────────
    def navigate(self, url: str, *, wait: float = 0.0) -> None:
        self.send("Page.navigate", {"url": url})
        if wait:
            time.sleep(wait)

    def url(self) -> str:
        return self.eval("location.href")

    def title(self) -> str:
        return self.eval("document.title")

    # ── 스크린샷 ──────────────────────────────────────────────────
    def screenshot(self, path: str, *, fmt: str = "jpeg", quality: int = 70) -> str:
        import base64

        params = {"format": fmt}
        if fmt == "jpeg":
            params["quality"] = quality
        res = self.send("Page.captureScreenshot", params)
        data = base64.b64decode(res["data"])
        with open(path, "wb") as f:
            f.write(data)
        return path

    def close(self) -> None:
        try:
            self._ws.close()
        except Exception:
            pass
