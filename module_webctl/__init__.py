"""module_webctl — 원격 디버깅 크롬(CDP)을 조작하는 웹 컨트롤 substrate.

목적: 이미 떠 있는 크롬(예: `chrome --remote-debugging-port=9222`)의 탭에 붙어
DOM을 읽고/클릭/입력/대기/스크린샷 한다. 자동매매 어댑터(타임폴리오 등)가
이 위에 얹힌다.

기본 사용:
    from module_webctl import WebController
    w = WebController.attach(match_url="timefolio")
    w.wait_for("#email"); w.fill("#email", "..."); w.fill("#password", "...")
    w.click(".btn-primary")

안전: 이 계층은 범용 프리미티브만 제공(클릭/입력). '주문 제출' 같은
되돌릴 수 없는 액션의 드라이런/승인 게이트는 상위 매매 어댑터가 강제한다.
"""
from __future__ import annotations

import time
from typing import Any, Optional

from ._cdp import CDPClient, CDPError

__all__ = ["WebController", "CDPError"]

# ── React/Vue 친화 값 세팅 + 텍스트 클릭용 JS 스니펫 ─────────────────
_JS_SET_NATIVE = r"""
function __setNativeValue(el, value){
  const proto = el.tagName === 'TEXTAREA' ? window.HTMLTextAreaElement.prototype
                                          : window.HTMLInputElement.prototype;
  const setter = Object.getOwnPropertyDescriptor(proto, 'value').set;
  setter.call(el, value);
  el.dispatchEvent(new Event('input',  {bubbles:true}));
  el.dispatchEvent(new Event('change', {bubbles:true}));
}
"""


def _q(sel: str) -> str:
    """CSS 선택자를 JS 문자열 리터럴로 안전 이스케이프."""
    return sel.replace("\\", "\\\\").replace("'", "\\'")


class WebController:
    def __init__(self, cdp: CDPClient):
        self.cdp = cdp
        self.cdp.enable_domains()

    @classmethod
    def attach(
        cls,
        *,
        host: str = "localhost",
        port: int = 9222,
        match_url: Optional[str] = None,
        match_title: Optional[str] = None,
        index: int = 0,
        timeout: float = 20.0,
    ) -> "WebController":
        cdp = CDPClient.attach(
            host=host, port=port, match_url=match_url,
            match_title=match_title, index=index, timeout=timeout,
        )
        return cls(cdp)

    # ── 상태 읽기 ─────────────────────────────────────────────────
    def url(self) -> str:
        return self.cdp.url()

    def title(self) -> str:
        return self.cdp.title()

    def eval(self, expr: str) -> Any:
        return self.cdp.eval(expr)

    def exists(self, selector: str) -> bool:
        return bool(self.cdp.eval(f"!!document.querySelector('{_q(selector)}')"))

    def count(self, selector: str) -> int:
        return int(self.cdp.eval(f"document.querySelectorAll('{_q(selector)}').length"))

    def text(self, selector: str) -> Optional[str]:
        return self.cdp.eval(
            f"(()=>{{const e=document.querySelector('{_q(selector)}');"
            f"return e?(e.innerText||e.value||'').trim():null;}})()"
        )

    def attr(self, selector: str, name: str) -> Optional[str]:
        return self.cdp.eval(
            f"(()=>{{const e=document.querySelector('{_q(selector)}');"
            f"return e?e.getAttribute('{_q(name)}'):null;}})()"
        )

    def texts(self, selector: str, limit: int = 50) -> list[str]:
        return self.cdp.eval(
            f"Array.from(document.querySelectorAll('{_q(selector)}')).slice(0,{limit})"
            f".map(e=>(e.innerText||e.value||'').trim())"
        ) or []

    # ── 대기 ──────────────────────────────────────────────────────
    def wait_for(self, selector: str, *, timeout: float = 10.0, visible: bool = True) -> bool:
        cond = (
            f"(()=>{{const e=document.querySelector('{_q(selector)}');"
            + ("return !!(e && (e.offsetWidth||e.offsetHeight||e.getClientRects().length));"
               if visible else "return !!e;")
            + "})()"
        )
        deadline = time.time() + timeout
        while time.time() < deadline:
            if bool(self.cdp.eval(cond)):
                return True
            time.sleep(0.25)
        return False

    def wait_gone(self, selector: str, *, timeout: float = 10.0) -> bool:
        deadline = time.time() + timeout
        while time.time() < deadline:
            if not self.exists(selector):
                return True
            time.sleep(0.25)
        return False

    # ── 액션 ──────────────────────────────────────────────────────
    def click(self, selector: str) -> bool:
        """선택자 요소를 클릭(JS .click()). 성공 여부 반환."""
        return bool(self.cdp.eval(
            f"(()=>{{const e=document.querySelector('{_q(selector)}');"
            f"if(!e)return false; e.scrollIntoView({{block:'center'}}); e.click(); return true;}})()"
        ))

    def click_text(self, text: str, *, tag: str = "*", exact: bool = False) -> bool:
        """가시 텍스트로 요소 클릭(매수/매도 버튼처럼 선택자 없을 때)."""
        t = _q(text)
        match = "(el.innerText||'').trim()===t" if exact else "(el.innerText||'').includes(t)"
        return bool(self.cdp.eval(
            f"(()=>{{const t='{t}';"
            f"const els=Array.from(document.querySelectorAll('{tag}'));"
            f"const hit=els.filter(el=>el.offsetParent!==null && {match})"
            f".sort((a,b)=>(a.innerText||'').length-(b.innerText||'').length)[0];"
            f"if(!hit)return false; hit.scrollIntoView({{block:'center'}}); hit.click(); return true;}})()"
        ))

    def fill(self, selector: str, value: str) -> bool:
        """React/Vue 친화 입력: native setter + input/change 이벤트."""
        v = str(value).replace("\\", "\\\\").replace("'", "\\'")
        return bool(self.cdp.eval(
            _JS_SET_NATIVE
            + f"(()=>{{const e=document.querySelector('{_q(selector)}');"
            f"if(!e)return false; e.focus(); __setNativeValue(e,'{v}'); return true;}})()"
        ))

    def focus(self, selector: str) -> bool:
        return bool(self.cdp.eval(
            f"(()=>{{const e=document.querySelector('{_q(selector)}');"
            f"if(!e)return false; e.focus(); return true;}})()"
        ))

    # ── 신뢰 이벤트(isTrusted) 보강 — 일부 위젯이 요구 ─────────────
    def type_native(self, text: str) -> None:
        """현재 포커스된 요소에 실제 키 입력(Input.insertText)."""
        self.cdp.send("Input.insertText", {"text": text})

    def press_key(self, key: str, code: Optional[str] = None) -> None:
        """Enter/Tab 등 특수키 dispatch. key 예: 'Enter'."""
        code = code or key
        common = {"key": key, "code": code, "windowsVirtualKeyCode":
                  {"Enter": 13, "Tab": 9, "Escape": 27}.get(key, 0)}
        self.cdp.send("Input.dispatchKeyEvent", {"type": "keyDown", **common})
        self.cdp.send("Input.dispatchKeyEvent", {"type": "keyUp", **common})

    # ── 편의 ──────────────────────────────────────────────────────
    def navigate(self, url: str, *, wait: float = 1.0) -> None:
        self.cdp.navigate(url, wait=wait)

    def screenshot(self, path: str, **kw) -> str:
        return self.cdp.screenshot(path, **kw)

    def body_text(self, limit: int = 4000) -> str:
        return (self.cdp.eval("document.body.innerText") or "")[:limit]

    def close(self) -> None:
        self.cdp.close()
