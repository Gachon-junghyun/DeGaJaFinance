"""module_webctl CLI — 원격 크롬(CDP) 조작 + 지도 + 채널 점검.

조회(기본):
  python -X utf8 -m module_webctl tabs
  python -X utf8 -m module_webctl info  --match timefolio
  python -X utf8 -m module_webctl dom   --match timefolio --sel "button"
  python -X utf8 -m module_webctl eval  --match timefolio --js "document.title"
  python -X utf8 -m module_webctl goto  "https://…" --until "document.querySelectorAll('tr').length>5"
  python -X utf8 -m module_webctl links --match dart --contains "/dsaf001/"
  python -X utf8 -m module_webctl shot  --match timefolio --out out/webctl/tf.png --full

배치(심부름 한 건을 한 번에 — 왕복이 제일 비싸다):
  python -X utf8 -m module_webctl run "[[\"goto\",\"https://…\",\"cond\"],[\"text\",\"#tbl\"]]" --match dart
  (stdin) echo ... | python -X utf8 -m module_webctl run - --match dart

지도(크롬을 안 띄운다 — 브라우저를 쓸지 말지부터 결정):
  python -X utf8 -m module_webctl find 공시 · go dart 공시검색 · map session · catalog api

채널(포트=계정 경계):
  python -X utf8 -m module_webctl up --site timefolio_contest

★ 조회가 기본값이다. 쓰기(click·fill·key)는 `--allow-write` 를 사람이 명시해야 한다.
  주문·제출 계열은 이 층이 아니라 module_timefolio/module_order_desk 의 게이트를 지난다(P5).
⚠ `--match` 없이 붙으면 **첫 탭**(남의 탭)이 잡힌다. 세션 사이트는 `--port` 도 계정 경계다.
"""
from __future__ import annotations

import argparse
import json
import os
import sys

from . import WebController, _ensure, _fast, _sites
from ._cdp import CDPClient, CDPError

_CONN = ("--host", "--port", "--match", "--title", "--index")


def _strip_conn(argv: list[str]) -> tuple[dict, list[str]]:
    """연결 플래그를 **위치와 무관하게** 뽑아낸다.

    ★ 실측 결함(llm_outputs/2026-08-14/timefolio/CLOSE_CHECK.md): argparse 의 parents 로
    서브커맨드마다 같은 플래그를 달면 `--match` 를 **서브커맨드 앞**에 둔 경우 서브파서의
    기본값이 덮어써서 조용히 **탭 0** 으로 폴백한다(실측: antimetal.com 에 붙었다).
    ARMED 상태와 겹치면 위험하다. 그래서 파싱 전에 여기서 직접 걷어낸다 — 앞·뒤 어디에
    둬도 똑같이 먹는다.
    """
    got, rest, i = {}, [], 0
    while i < len(argv):
        a = argv[i]
        key = next((c for c in _CONN if a == c or a.startswith(c + "=")), None)
        if key is None:
            rest.append(a)
            i += 1
            continue
        if "=" in a:
            got[key[2:]] = a.split("=", 1)[1]
            i += 1
        else:
            got[key[2:]] = argv[i + 1] if i + 1 < len(argv) else ""
            i += 2
    return got, rest


def _resolve_port(given) -> int:
    """`--port` > DEGAJA_CDP_PORT > TIMEFOLIO_CDP_PORT > 9222.

    ★ 실측 결함(2026-08-28): CLI 가 `TIMEFOLIO_CDP_PORT` 를 **안 읽어서** 9223 우회 중에도
    9222 로 갔다. 환경변수를 세팅한 사람은 그게 먹는다고 믿는다 — 그 침묵이 제일 비싸다.
    """
    if given:
        return int(given)
    for var in ("DEGAJA_CDP_PORT", "TIMEFOLIO_CDP_PORT"):
        v = os.environ.get(var)
        if v:
            return int(str(v).split(",")[0])
    return 9222


def _attach(args) -> WebController:
    return WebController.attach(host=args.host, port=args.port, match_url=args.match,
                                match_title=args.title, index=args.index)


def _dump(v) -> None:
    print(json.dumps(v, ensure_ascii=False, indent=2) if not isinstance(v, str) else v)


# ── 크롬 조회 ──────────────────────────────────────────────────────
def cmd_tabs(args) -> int:
    ver = CDPClient.version(args.host, args.port)
    print(f"Browser: {ver.get('Browser')}  (port {args.port})")
    for t in CDPClient.list_targets(args.host, args.port):
        if args.all or t.get("type") == "page":
            print(f"  [{t.get('type'):14}] {(t.get('title') or '')[:45]:45} | {(t.get('url') or '')[:70]}")
    return 0


def cmd_newtab(args) -> int:
    t = CDPClient.new_tab(args.url, args.host, args.port)
    _dump({"id": t.get("id"), "url": t.get("url")})
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
        _dump(w.eval(args.js))
    finally:
        w.close()
    return 0


def cmd_text(args) -> int:
    w = _attach(args)
    try:
        print(w.text(args.sel) if args.sel else w.body_text(args.limit))
    finally:
        w.close()
    return 0


def cmd_goto(args) -> int:
    w = _attach(args)
    try:
        _dump(w.goto(args.url, until=args.until, timeout=args.timeout))
    finally:
        w.close()
    return 0


def cmd_until(args) -> int:
    w = _attach(args)
    try:
        _dump(w.until(args.js, timeout=args.timeout))
    finally:
        w.close()
    return 0


def cmd_links(args) -> int:
    w = _attach(args)
    try:
        _dump(w.links(args.contains, args.limit))
    finally:
        w.close()
    return 0


def cmd_alts(args) -> int:
    w = _attach(args)
    try:
        _dump(w.alts(args.limit))
    finally:
        w.close()
    return 0


def cmd_probe(args) -> int:
    """클릭이 왜 안 먹는지만 진단한다 — 누르지 않는다."""
    w = _attach(args)
    try:
        _dump(w.probe_click(args.sel))
    finally:
        w.close()
    return 0


def cmd_shot(args) -> int:
    w = _attach(args)
    try:
        print("saved:", w.shot(args.out, full=args.full))
    finally:
        w.close()
    return 0


# ── 쓰기 (사람이 명시할 때만) ───────────────────────────────────────
def cmd_click(args) -> int:
    w = _attach(args)
    try:
        if args.native:
            _dump(w.click_native(args.sel))
            return 0
        ok = w.click_text(args.text, exact=args.exact) if args.text else w.click(args.sel)
        if not ok and args.sel:
            print("NOT CLICKED — 진단:", json.dumps(w.probe_click(args.sel), ensure_ascii=False))
            return 1
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


# ── 배치 ───────────────────────────────────────────────────────────
def cmd_run(args) -> int:
    if args.steps == "-":
        # ★ Windows 는 stdin 을 cp949 로 디코딩한다 — 한글이 든 조건문이 조용히 깨져
        #   영영 참이 안 되고 timeout 으로만 드러난다. 규약의 "UTF-8" 은 stdin 에도 걸린다.
        try:
            sys.stdin.reconfigure(encoding="utf-8")
            raw = sys.stdin.read()
        except (AttributeError, OSError):
            raw = sys.stdin.buffer.read().decode("utf-8")
    else:
        raw = args.steps
    res = _fast.run(json.loads(raw), host=args.host, port=args.port, match=args.match,
                    title=args.title, index=args.index, allow_write=args.allow_write)
    _dump(res)
    return 0 if all(r["ok"] for r in res) else 1


# ── 채널 ───────────────────────────────────────────────────────────
def cmd_up(args) -> int:
    r = _ensure.ensure(site=args.site, want=args.want,
                       ports=[args.port] if args.port_given else None,
                       do_launch=not args.no_launch)
    _dump(r)
    return 0 if r.get("port") else 3


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="module_webctl", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    # 연결 플래그는 _strip_conn 이 위치와 무관하게 먼저 걷어간다(여긴 도움말용).
    p.add_argument("--host", default="localhost", help="(어디에 둬도 먹는다)")
    p.add_argument("--port", type=int, help="CDP 포트 = 계정 경계. 기본 DEGAJA_CDP_PORT/TIMEFOLIO_CDP_PORT/9222")
    p.add_argument("--match", help="타깃 URL 부분매칭 — ★ 안 주면 첫 탭(남의 탭)이 잡힌다")
    p.add_argument("--title", help="타깃 타이틀 부분매칭")
    p.add_argument("--index", type=int, default=0, help="매칭 없을 때 page 인덱스")
    sub = p.add_subparsers(dest="cmd", required=True)

    def add(name, help):
        return sub.add_parser(name, help=help)

    s = add("tabs", "열린 타깃 목록"); s.add_argument("--all", action="store_true"); s.set_defaults(func=cmd_tabs)
    s = add("newtab", "새 탭(남의 탭을 안 건드리는 시작점)"); s.add_argument("url", nargs="?", default="about:blank"); s.set_defaults(func=cmd_newtab)
    s = add("info", "현재 탭 URL/타이틀/본문"); s.set_defaults(func=cmd_info)
    s = add("dom", "선택자 요소 나열"); s.add_argument("--sel", required=True); s.add_argument("--limit", type=int, default=30); s.set_defaults(func=cmd_dom)
    s = add("eval", "JS 실행(여러 값은 배열로 한 방에)"); s.add_argument("--js", required=True); s.set_defaults(func=cmd_eval)
    s = add("text", "선택자 텍스트(없으면 body)"); s.add_argument("--sel"); s.add_argument("--limit", type=int, default=4000); s.set_defaults(func=cmd_text)
    s = add("goto", "이동 + 조건 대기(sleep 금지)"); s.add_argument("url"); s.add_argument("--until"); s.add_argument("--timeout", type=float, default=30.0); s.set_defaults(func=cmd_goto)
    s = add("until", "조건이 참이 될 때까지"); s.add_argument("js"); s.add_argument("--timeout", type=float, default=20.0); s.set_defaults(func=cmd_until)
    s = add("links", "[텍스트,href] 수확"); s.add_argument("--contains", default=""); s.add_argument("--limit", type=int, default=60); s.set_defaults(func=cmd_links)
    s = add("alts", "img alt 수확(표가 이미지일 때)"); s.add_argument("--limit", type=int, default=60); s.set_defaults(func=cmd_alts)
    s = add("probe", "클릭이 왜 안 먹는지 진단(누르지 않음)"); s.add_argument("--sel", required=True); s.set_defaults(func=cmd_probe)
    s = add("wait", "선택자 등장 대기"); s.add_argument("--sel", required=True); s.add_argument("--timeout", type=float, default=10.0); s.set_defaults(func=cmd_wait)
    s = add("shot", "스크린샷(기본 out/webctl/)"); s.add_argument("--out"); s.add_argument("--full", action="store_true"); s.set_defaults(func=cmd_shot)
    s = add("click", "클릭 — 되돌릴 수 없는 버튼에 쓰지 마라"); s.add_argument("--sel"); s.add_argument("--text"); s.add_argument("--exact", action="store_true"); s.add_argument("--native", action="store_true", help="진짜 마우스 이벤트 + 가로채임 진단"); s.set_defaults(func=cmd_click)
    s = add("fill", "입력 채우기"); s.add_argument("--sel", required=True); s.add_argument("--val", required=True); s.add_argument("--enter", action="store_true"); s.set_defaults(func=cmd_fill)
    s = add("run", "스텝 배열을 한 세션에서(JSON 또는 -)"); s.add_argument("steps"); s.add_argument("--allow-write", action="store_true", dest="allow_write", help="click/fill/key 허용(사람이 명시)"); s.set_defaults(func=cmd_run)

    s = add("map", "지도 목록"); s.add_argument("access", nargs="?"); s.set_defaults(func=_sites.cmd_map)
    s = add("find", "어디로 가야 하나"); s.add_argument("query", nargs="+"); s.set_defaults(func=_sites.cmd_find)
    s = add("go", "목적지 URL"); s.add_argument("site"); s.add_argument("task", nargs="?"); s.set_defaults(func=_sites.cmd_go)
    s = add("catalog", "프롬프트용 압축본"); s.add_argument("access", nargs="?"); s.set_defaults(func=_sites.cmd_catalog)
    s = add("up", "채널 점검·복구(포트=계정 경계)"); s.add_argument("--site"); s.add_argument("--want"); s.add_argument("--no-launch", action="store_true", dest="no_launch"); s.set_defaults(func=cmd_up)
    return p


def main(argv=None) -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, OSError):
            pass
    conn, rest = _strip_conn(list(sys.argv[1:] if argv is None else argv))
    args = build_parser().parse_args(rest)
    args.host = conn.get("host") or "localhost"
    args.port_given = "port" in conn
    args.port = _resolve_port(conn.get("port"))
    args.match = conn.get("match")
    args.title = conn.get("title")
    args.index = int(conn.get("index") or 0)
    try:
        return args.func(args)
    except (CDPError, PermissionError) as e:
        print(f"{type(e).__name__}: {e}", file=sys.stderr)
        return 2
    except (ConnectionError, OSError) as e:
        print(f"연결 실패({args.port}): {e}\n"
              f"  → python -X utf8 -m module_webctl up --want <원하는탭>  으로 점유자부터 확인해라",
              file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
