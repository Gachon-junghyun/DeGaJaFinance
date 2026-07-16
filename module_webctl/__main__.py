"""module_webctl CLI — 원격 크롬(CDP) 조작.

예:
  python -X utf8 -m module_webctl tabs
  python -X utf8 -m module_webctl info --match timefolio
  python -X utf8 -m module_webctl dom  --match timefolio --sel "button"
  python -X utf8 -m module_webctl eval --match timefolio --js "document.title"
  python -X utf8 -m module_webctl fill --match timefolio --sel "#email" --val "..."
  python -X utf8 -m module_webctl click --match timefolio --sel ".btn-primary"
  python -X utf8 -m module_webctl shot --match timefolio --out shot.jpg
"""
from __future__ import annotations

import argparse
import json
import sys

from ._cdp import CDPClient, CDPError
from . import WebController


def _attach(args) -> WebController:
    return WebController.attach(
        host=args.host, port=args.port,
        match_url=args.match, match_title=args.title, index=args.index,
    )


def cmd_tabs(args) -> int:
    ver = CDPClient.version(args.host, args.port)
    print(f"Browser: {ver.get('Browser')}")
    for t in CDPClient.list_targets(args.host, args.port):
        if args.all or t.get("type") == "page":
            print(f"  [{t.get('type'):14}] {(t.get('title') or '')[:45]:45} | {(t.get('url') or '')[:70]}")
    return 0


def cmd_info(args) -> int:
    w = _attach(args)
    try:
        print("URL   :", w.url())
        print("TITLE :", w.title())
        print("BODY  :", w.body_text(300).replace("\n", " ")[:300])
    finally:
        w.close()
    return 0


def cmd_dom(args) -> int:
    w = _attach(args)
    try:
        js = f"""Array.from(document.querySelectorAll('{args.sel}')).slice(0,{args.limit}).map(e=>({{
          tag:e.tagName, type:e.type||'', id:e.id||'',
          cls:(e.className||'').toString().slice(0,45),
          txt:(e.innerText||e.value||e.placeholder||'').trim().replace(/\\s+/g,' ').slice(0,40)
        }}))"""
        for e in (w.eval(js) or []):
            print(f"  [{e['tag']}/{e['type']}] #{e['id']} .{e['cls']} :: {e['txt']}")
    finally:
        w.close()
    return 0


def cmd_eval(args) -> int:
    w = _attach(args)
    try:
        val = w.eval(args.js)
        print(json.dumps(val, ensure_ascii=False, indent=2) if not isinstance(val, str) else val)
    finally:
        w.close()
    return 0


def cmd_text(args) -> int:
    w = _attach(args)
    try:
        print(w.text(args.sel))
    finally:
        w.close()
    return 0


def cmd_click(args) -> int:
    w = _attach(args)
    try:
        ok = w.click_text(args.text, exact=args.exact) if args.text else w.click(args.sel)
        print("clicked" if ok else "NOT FOUND")
        return 0 if ok else 1
    finally:
        w.close()


def cmd_fill(args) -> int:
    w = _attach(args)
    try:
        ok = w.fill(args.sel, args.val)
        if ok and args.enter:
            w.press_key("Enter")
        print("filled" if ok else "NOT FOUND")
        return 0 if ok else 1
    finally:
        w.close()


def cmd_wait(args) -> int:
    w = _attach(args)
    try:
        ok = w.wait_for(args.sel, timeout=args.timeout)
        print("present" if ok else "TIMEOUT")
        return 0 if ok else 1
    finally:
        w.close()


def cmd_shot(args) -> int:
    w = _attach(args)
    try:
        print("saved:", w.screenshot(args.out))
    finally:
        w.close()
    return 0


def build_parser() -> argparse.ArgumentParser:
    conn = argparse.ArgumentParser(add_help=False)
    conn.add_argument("--host", default="localhost")
    conn.add_argument("--port", type=int, default=9222)
    conn.add_argument("--match", help="타깃 URL 부분매칭")
    conn.add_argument("--title", help="타깃 타이틀 부분매칭")
    conn.add_argument("--index", type=int, default=0, help="매칭 없을 때 page 인덱스")

    p = argparse.ArgumentParser(prog="module_webctl", parents=[conn],
                                description="원격 크롬(CDP) 웹 컨트롤")
    sub = p.add_subparsers(dest="cmd", required=True)

    def add(name, help):
        return sub.add_parser(name, help=help, parents=[conn])

    s = add("tabs", "열린 타깃 목록"); s.add_argument("--all", action="store_true"); s.set_defaults(func=cmd_tabs)
    s = add("info", "현재 탭 URL/타이틀/본문"); s.set_defaults(func=cmd_info)
    s = add("dom", "선택자 요소 나열"); s.add_argument("--sel", required=True); s.add_argument("--limit", type=int, default=30); s.set_defaults(func=cmd_dom)
    s = add("eval", "JS 실행"); s.add_argument("--js", required=True); s.set_defaults(func=cmd_eval)
    s = add("text", "선택자 텍스트"); s.add_argument("--sel", required=True); s.set_defaults(func=cmd_text)
    s = add("click", "클릭(선택자 또는 --text)"); s.add_argument("--sel"); s.add_argument("--text"); s.add_argument("--exact", action="store_true"); s.set_defaults(func=cmd_click)
    s = add("fill", "입력 채우기"); s.add_argument("--sel", required=True); s.add_argument("--val", required=True); s.add_argument("--enter", action="store_true"); s.set_defaults(func=cmd_fill)
    s = add("wait", "선택자 등장 대기"); s.add_argument("--sel", required=True); s.add_argument("--timeout", type=float, default=10.0); s.set_defaults(func=cmd_wait)
    s = add("shot", "스크린샷"); s.add_argument("--out", default="webctl_shot.jpg"); s.set_defaults(func=cmd_shot)
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    try:
        return args.func(args)
    except CDPError as e:
        print("CDP 오류:", e, file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
