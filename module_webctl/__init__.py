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
from pathlib import Path
from typing import Any, Optional

from ._cdp import CDPClient, CDPError
from ._sites import (  # noqa: F401  지도는 크롬을 안 띄운다 — "어디로 가나"만 알고 싶은 소비자용
    catalog, find_site, get_site, load_map, site_ports, site_url,
)

__all__ = ["WebController", "CDPClient", "CDPError",
           "load_map", "find_site", "get_site", "site_url", "site_ports", "catalog"]

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

    # ── 심부름 프리미티브 — until·goto·수확·진단클릭 ─────────────────
    # sleep 을 박지 마라. 고정 대기는 빠른 페이지에서 통째로 낭비고 느린 페이지에선
    # 그래도 모자란다. "내가 필요한 것이 보일 때까지" 만 기다린다.
    def until(self, js: str, *, timeout: float = 20.0, poll: float = 0.05):
        """`js` 가 truthy 를 낼 때까지 폴링하고 그 값을 반환. 못 채우면 CDPError."""
        deadline = time.time() + timeout
        last = None
        while time.time() < deadline:
            try:
                v = self.cdp.eval(js)
                if v:
                    return v
            except CDPError as e:      # 이동 중엔 실행 컨텍스트가 잠깐 사라진다
                last = e
            time.sleep(poll)
        raise CDPError(f"{timeout}s 안에 조건 미충족: {js[:120]} (마지막 오류: {last})")

    def goto(self, url: str, *, until: Optional[str] = None, timeout: float = 30.0) -> dict:
        """이동하고 **새 문서가 실제로 뜬 뒤에** `until` 을 기다린다.

        ★ 순진하게 폴링하면 **직전 페이지의 DOM 을 읽고 조건을 만족시켜 버린다.** 그래서
        이동 전에 옛 문서에 도장(`window.__degaja_nav`)을 찍고 그 도장이 사라지는 것으로
        문서 교체를 확인한다(도장은 새 문서에 안 따라온다). SPA 의 pushState 라우팅은
        문서를 안 갈아치우므로 도장이 남는다 — 그 경우엔 `until` 만으로 판정된다.
        """
        t0 = time.time()
        try:
            self.cdp.eval("window.__degaja_nav = 1")
        except CDPError:
            pass
        self.cdp.navigate(url)
        swapped = None
        while time.time() - t0 < timeout:
            try:
                if not self.cdp.eval("window.__degaja_nav"):
                    swapped = round(time.time() - t0, 3)
                    break
            except CDPError:
                pass
            time.sleep(0.03)
        got = None
        if until:
            got = self.until(until, timeout=max(1.0, timeout - (time.time() - t0)))
        return {"url": self.url(), "title": self.title(), "swapped_s": swapped,
                "elapsed_s": round(time.time() - t0, 3), "until": got}

    # 여러 값이 필요하면 요소마다 왕복하지 말고 eval 하나에 배열로 받아라.
    def links(self, contains: str = "", limit: int = 60) -> list[list[str]]:
        """[[텍스트, href], ...] — 한 번의 eval 로 전부."""
        return self.cdp.eval(
            "Array.from(document.querySelectorAll('a'))"
            f".filter(a=>(a.getAttribute('href')||'').includes({contains!r}))"
            ".map(a=>[a.innerText.trim().slice(0,80), a.href])"
            f".filter(x=>x[0]).slice(0,{int(limit)})") or []

    def alts(self, limit: int = 60) -> list[str]:
        """img 의 alt. 표·수치가 이미지인 IR/리포트 페이지에서 텍스트를 건지는 값싼 경로."""
        return self.cdp.eval(
            "Array.from(document.querySelectorAll('img')).map(i=>i.alt)"
            f".filter(a=>a&&a.length>3).slice(0,{int(limit)})") or []

    def probe_click(self, selector: str) -> dict:
        """클릭이 **왜** 안 먹는지 1회에 판별한다 — 누르지는 않는다.

        `elementFromPoint` 로 재서 «가려짐 ← 누가 덮었는지» / «크기 0» / «뷰포트 밖» 을
        가른다. 셋 다 증상은 똑같이 "클릭이 안 먹는다"인데 대응이 전혀 다르다 —
        덮였으면 모달을 닫고, 0크기·화면밖이면 셀렉터가 틀린 것이다.
        """
        return self.cdp.eval(
            f"(()=>{{const e=document.querySelector({selector!r});if(!e)return{{err:'no-element'}};"
            "e.scrollIntoView({block:'center'});const r=e.getBoundingClientRect();"
            "if(r.width===0||r.height===0)return{err:'zero-size'};"
            "const x=r.left+r.width/2,y=r.top+r.height/2;"
            "if(!(x>=0&&y>=0&&x<=innerWidth&&y<=innerHeight))return{err:'offscreen',x:x,y:y};"
            "const t=document.elementFromPoint(x,y);"
            "return{x:x,y:y,ok:!!t&&(e===t||e.contains(t)),"
            "by:t?((t.tagName+'.'+(t.className||'')+'#'+(t.id||'')).slice(0,80)):'(없음)'}})()")

    def click_native(self, selector: str) -> dict:
        """요소 중앙에 **진짜 마우스 이벤트**를 쏜다(가로채임 진단 포함).

        `click()`(JS .click())이 조용히 씹히는 위젯용. 되돌릴 수 없는 버튼에는 쓰지 마라 —
        확인과 클릭은 다른 실행에서 한다(CLAUDE.md 규약).
        """
        info = self.probe_click(selector)
        err = info.get("err")
        if err == "no-element":
            raise CDPError(f"요소 없음: {selector}")
        if err == "zero-size":
            raise CDPError(f"크기가 0인 요소다: {selector} (숨은 요소를 잡았다 — 셀렉터를 의심해라)")
        if err == "offscreen":
            raise CDPError(f"뷰포트 밖이다: {selector} @({info['x']:.0f},{info['y']:.0f})"
                           " — sticky 헤더/푸터에 가렸거나 스크롤 컨테이너 안이다")
        if not info.get("ok"):
            raise CDPError(f"가려져 있다: {selector} ← '{info['by']}' 가 덮음 (모달/오버레이 먼저 닫아라)")
        for typ in ("mousePressed", "mouseReleased"):
            self.cdp.send("Input.dispatchMouseEvent",
                          {"type": typ, "x": info["x"], "y": info["y"],
                           "button": "left", "clickCount": 1})
        return info

    def shot(self, path: Optional[str] = None, *, full: bool = False) -> str:
        """예상과 다르게 굴면 즉시 찍어라 — DOM 을 20번 더듬는 것보다 한 장이 싸다.

        경로를 안 주면 `out/webctl/shot_NNN.png`(모듈 산출은 out/ 아래 — 규약).
        ⚠ 스크린샷엔 계좌·개인정보가 찍힌다. 커밋·공유 금지.
        """
        if path is None:
            base = Path("out") / "webctl"
            base.mkdir(parents=True, exist_ok=True)
            path = str(base / f"shot_{len(list(base.glob('shot_*.png'))) + 1:03d}.png")
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        fmt = "png" if str(path).lower().endswith(".png") else "jpeg"
        return self.cdp.screenshot(path, fmt=fmt, full=full)

    def close(self) -> None:
        self.cdp.close()
