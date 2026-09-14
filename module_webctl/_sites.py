"""지도 레이어 — "그 정보가 어디 있고, 거기서 뭘 할 수 있나".

`_cdp`/`WebController` 가 "어떻게 조작하나" 를 답한다면 여기는 **"어디로 가서 뭘 하나,
그리고 애초에 브라우저를 써야 하나"** 를 답한다. 브라우저를 띄우기 전에 이걸 먼저 본다.

설계는 세 가지가 전부다:

1. **`access` 가 행동을 정한다.** open=그냥 간다 / session=로그인된 프로필 포트로 붙는다 /
   api=**브라우저 쓰지 마라**(`prefer` 에 이 리포가 이미 소유한 경로가 있다 — P1) /
   blocked=하지 마라(`why`). 이 네 글자를 안 보고 크롬을 띄우면 이미 있는 모듈을 다시 짓거나
   레이트리밋·캡차를 산다.
2. **`can` 은 되돌릴 수 없는 것의 표시다.** `has`(볼 수 있는 것)만 있으면 읽기 전용,
   `can`(주문 제출 등)에 닿으면 실행 직전에 사람에게 묻는다(CLAUDE.md 규약: 기본 드라이런).
3. **`ports`/`profile` 은 계정 경계다.** 세션 사이트는 어느 디버그 프로필에 로그인돼 있는지가
   포트로 갈린다 — 포트를 빠뜨리면 조용히 9222(남의 크롬)로 간다. `_ensure.py` 가 이걸 쓴다.

이 파일엔 비밀이 없다. 경로 재정의는 환경변수 `DEGAJA_SITE_MAP`.

    python -X utf8 -m module_webctl map [open|session|api|blocked]
    python -X utf8 -m module_webctl find 공시
    python -X utf8 -m module_webctl go dart 공시검색
    python -X utf8 -m module_webctl catalog session
"""
from __future__ import annotations

import json
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
ACCESS = ("open", "session", "api", "blocked")


def map_path(path=None) -> Path:
    if path:
        return Path(path)
    return Path(os.environ.get("DEGAJA_SITE_MAP", HERE / "site_map.json"))


def load_map(path=None) -> dict:
    """`_` 로 시작하는 주석 키를 걸러낸 {사이트키: 항목}."""
    raw = json.loads(map_path(path).read_text(encoding="utf-8"))
    return {k: v for k, v in raw.items() if not k.startswith("_")}


def get_site(site: str, sites: dict | None = None, path=None) -> dict:
    sites = sites if sites is not None else load_map(path)
    if site not in sites:
        raise KeyError(f"'{site}' 없음. 등록된 것: {sorted(sites)}")
    return sites[site]


def _haystack(key: str, e: dict) -> str:
    """검색 대상. note/why 는 일부러 뺀다 — 주의사항 단어로 오탐되면 안 되니까."""
    return " ".join([key, e.get("label", ""), *e.get("has", []), *e.get("can", []),
                     *(e.get("go") or {}).keys()]).lower()


def find_site(query: str, sites: dict | None = None, path=None) -> list[tuple[str, dict, int]]:
    """공백으로 나눈 단어가 몇 개 걸리는지로 점수. blocked 는 뒤로 민다."""
    sites = sites if sites is not None else load_map(path)
    words = [w for w in query.lower().split() if w]
    hits = []
    for key, e in sites.items():
        score = sum(1 for w in words if w in _haystack(key, e))
        if score:
            hits.append((key, e, score - (10 if e.get("access") == "blocked" else 0)))
    return sorted(hits, key=lambda t: (-t[2], t[0]))


def site_url(site: str, task: str | None = None, sites: dict | None = None, path=None) -> str:
    """목적지 URL. task 를 안 주면 첫 번째 것. 부분 일치도 받는다."""
    e = get_site(site, sites, path)
    urls = e.get("go") or {}
    if not urls:
        raise KeyError(f"'{site}' 에는 go URL 이 없다"
                       + (f" — 대신: {e['prefer']}" if e.get("prefer") else ""))
    if task is None:
        return next(iter(urls.values()))
    if task in urls:
        return urls[task]
    t = task.lower().replace(" ", "")
    for k, v in urls.items():
        if t in k.lower().replace(" ", ""):
            return v
    raise KeyError(f"'{site}' 에 '{task}' 없음. 있는 것: {sorted(urls)}")


def site_ports(site: str, sites: dict | None = None, path=None) -> list[int]:
    """세션 사이트가 로그인돼 있는 디버그 포트 후보. 없으면 [](= 호출부 기본값)."""
    return [int(p) for p in (get_site(site, sites, path).get("ports") or [])]


def catalog(access: str | None = None, sites: dict | None = None, path=None) -> str:
    """프롬프트에 넣을 압축본. blocked 는 '왜 안 되는지' 만 남긴다."""
    sites = sites if sites is not None else load_map(path)
    lines = []
    for key, e in sorted(sites.items()):
        acc = e.get("access", "?")
        if access and acc != access:
            continue
        if acc == "blocked":
            lines.append(f"- {key} [금지]: {e.get('why', '')[:80]}")
            continue
        bits = [f"- {key} ({e.get('label', key)}) [{acc}]"]
        if e.get("has"):
            bits.append("  볼 수 있는 것: " + ", ".join(e["has"]))
        if e.get("can"):
            bits.append("  ★되돌릴 수 없는 것(사람 확인): " + ", ".join(e["can"]))
        if e.get("ports"):
            bits.append(f"  포트(=계정 경계): {e['ports']} profile={e.get('profile', '?')}")
        if e.get("go"):
            bits.append("  바로가기: " + " | ".join(f"{k}={v}" for k, v in e["go"].items()))
        if e.get("prefer"):
            bits.append("  ▶ 더 싼 경로(이걸 먼저): " + e["prefer"])
        lines.append("\n".join(bits))
    return "\n".join(lines) if lines else "(해당 없음)"


# ── CLI (module_webctl.__main__ 가 호출) ───────────────────────────
def cmd_map(args) -> int:
    want = getattr(args, "access", None)
    if want and want not in ACCESS:
        print(f"access 는 {ACCESS} 중 하나")
        return 2
    for key, e in sorted(load_map().items()):
        acc = e.get("access", "?")
        if want and acc != want:
            continue
        print(f"  {key:20s} [{acc:7s}] {e.get('label', '')}")
    return 0


def cmd_find(args) -> int:
    hits = find_site(" ".join(args.query))
    if not hits:
        print("(지도에 없다 — 그냥 가되, 끝나고 site_map.json 에 등록해라)")
        return 1
    for key, e, score in hits:
        print(f"  {key:20s} [{e.get('access', '?'):7s}] {e.get('label', '')}  (일치 {score})")
        for k, v in (e.get("go") or {}).items():
            print(f"      {k}: {v}")
        if e.get("prefer"):
            print(f"      ▶ 더 싼 경로: {e['prefer']}")
        if e.get("can"):
            print(f"      ★되돌릴 수 없음: {', '.join(e['can'])}")
        if e.get("why"):
            print(f"      ✗ 금지 이유: {e['why']}")
    return 0


def cmd_go(args) -> int:
    try:
        print(site_url(args.site, args.task))
    except KeyError as e:
        print(e.args[0])
        return 1
    return 0


def cmd_catalog(args) -> int:
    print(catalog(getattr(args, "access", None)))
    return 0
