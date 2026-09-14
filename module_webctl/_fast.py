"""배치 실행 — **한 번의 호출로 심부름 한 건을 끝낸다.**

왜 있나. 이동→대기→추출→다음 이동을 CLI 호출 3번으로 나누면 프로세스 시작(×3) +
탭 붙기(×3) + 에이전트 왕복(×3)을 전부 낸다. 왕복이 이 층에서 제일 비싼 자원이다.
스텝 배열을 한 번에 부으면 **붙기 한 번**으로 끝나고, 중간에 실패해도 **거기까지 건진 건
돌려준다**(처음부터 다시 하는 게 제일 비싸다).

전송은 `_cdp.CDPClient`, 프리미티브는 `WebController` 를 그대로 쓴다 — 여기서 CDP 를
다시 구현하지 않는다(P1). 이 파일이 더하는 것은 **순서·부분성공·쓰기 게이트** 뿐이다.

    [["goto","https://…","document.querySelectorAll('.item').length>=10"],
     ["eval","Array.from(document.querySelectorAll('.item')).map(e=>e.innerText)"],
     ["text","#tbl"], ["links","/report/"], ["shot"]]

★ 기본은 **조회만**이다. 쓰기 스텝(click·click_native·fill·key)은 `--allow-write` 없이는
거부한다 — 되돌릴 수 없는 버튼 앞에서 확인과 클릭을 같은 실행에 넣지 않기 위해서다
(CLAUDE.md 규약: 기본 드라이런, 사람이 명시). 주문 계열은 이 층이 아니라
`module_timefolio`·`module_order_desk` 의 게이트를 지나야 한다.
"""
from __future__ import annotations

import time
from typing import Any, Optional

from . import WebController
from ._cdp import CDPError

WRITE_OPS = {"click", "click_native", "fill", "key"}
OPS = WRITE_OPS | {"goto", "until", "eval", "text", "body", "links", "alts", "shot", "sleep"}


def _apply(w: WebController, op: str, args: list) -> Any:
    if op == "goto":
        return w.goto(args[0], until=args[1] if len(args) > 1 else None)
    if op == "until":
        return w.until(args[0])
    if op == "eval":
        return w.eval(args[0])
    if op == "text":
        return w.text(args[0]) if args else w.body_text()
    if op == "body":
        return w.body_text(int(args[0]) if args else 4000)
    if op == "links":
        return w.links(*(args or [""]))
    if op == "alts":
        return w.alts(*args)
    if op == "shot":
        return w.shot(args[0] if args else None, full=bool(args[1]) if len(args) > 1 else False)
    if op == "sleep":
        time.sleep(float(args[0]))
        return None
    if op == "click":
        return w.click(args[0])
    if op == "click_native":
        return w.click_native(args[0])
    if op == "fill":
        return w.fill(args[0], args[1])
    if op == "key":
        w.press_key(args[0])
        return True
    raise ValueError(f"모르는 스텝: {op} (있는 것: {sorted(OPS)})")


def run(steps: list, *, host: str = "localhost", port: int = 9222,
        match: Optional[str] = None, title: Optional[str] = None, index: int = 0,
        allow_write: bool = False) -> list[dict]:
    """스텝 목록을 한 세션에서 순서대로 실행하고 결과 목록을 돌려준다.

    ⚠ `match` 를 안 주면 **첫 탭**이 잡힌다 — 내가 연 탭이 아니다. 실측으로 이 리포에서
    엉뚱한 탭(antimetal.com)에 붙은 이력이 있다(SITES.md ②). 심부름 중이면 꼭 줘라.
    """
    bad = [s[0] for s in steps if s and s[0] in WRITE_OPS]
    if bad and not allow_write:
        raise PermissionError(
            f"쓰기 스텝이 있다: {sorted(set(bad))}. 기본은 조회만이다 — 정말 필요하면 "
            "`--allow-write` 를 사람이 명시한다. 되돌릴 수 없는 버튼(주문·제출)은 "
            "이 층에서 누르지 않는다.")
    w = WebController.attach(host=host, port=port, match_url=match,
                             match_title=title, index=index)
    out: list[dict] = []
    try:
        for i, st in enumerate(steps):
            op, args = st[0], list(st[1:])
            t0 = time.time()
            try:
                r = _apply(w, op, args)
                out.append({"step": i, "op": op, "ok": True,
                            "s": round(time.time() - t0, 3), "result": r})
            except (CDPError, Exception) as e:   # noqa: B014  — 부분 성공을 지키는 게 목적
                out.append({"step": i, "op": op, "ok": False,
                            "s": round(time.time() - t0, 3),
                            "error": f"{type(e).__name__}: {e}"})
                break
    finally:
        w.close()
    return out
