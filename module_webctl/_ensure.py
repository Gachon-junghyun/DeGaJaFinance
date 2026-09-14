"""채널 점검·복구 — **포트가 곧 계정(프로필)이다.**

이 리포에서 반복 기록된 실패가 전부 여기 하나로 모인다(llm_outputs/*/timefolio/CLOSE_CHECK.md):

| 증상 | 진짜 원인 |
|---|---|
| `WinError 10061` 연결 거부 | 그 포트에 크롬이 없다 |
| 붙었는데 타임폴리오 탭이 없다 | **9222 를 다른 프로필의 크롬이 점유**했다. `start_timefolio_chrome.bat` 은 "9222 already listening → skip" 이라 조용히 아무것도 안 한다 |
| 셀렉터가 하나도 안 잡힌다 | `--match` 없이 붙어 **첫 탭**(남의 탭)을 잡았다 |

그래서 이 파일은 "포트가 살아 있나"가 아니라 **"그 포트에 내가 원하는 세션이 있나"**를 묻는다.
`site_map.json` 의 `ports`·`profile` 이 그 경계의 단일 원본이다.

    python -X utf8 -m module_webctl up --site timefolio_contest    # 점검 → 필요하면 기동/탭 열기
    python -X utf8 -m module_webctl up --want timefolio --no-launch   # 점검만

⚠ 크롬 기동은 하지만 **로그인은 대신 하지 않는다.** 로그인 벽이면 사람을 부르고 멈춘다
(자동 로그인 재시도 금지 — 계정 잠기는 게 답 못 찾는 것보다 훨씬 비싸다).
"""
from __future__ import annotations

import os
import socket
import subprocess
import time
from pathlib import Path

from . import _sites
from ._cdp import CDPClient

DEFAULT_PORTS = (9222, 9223)
_CHROME_CANDIDATES = (
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
)


def candidate_ports(ports=None) -> list[int]:
    """후보 포트. `--port`/사이트 지도 > DEGAJA_CDP_PORTS > TIMEFOLIO_CDP_PORT > 9222,9223."""
    if ports:
        return [int(p) for p in ports]
    env = os.environ.get("DEGAJA_CDP_PORTS") or os.environ.get("TIMEFOLIO_CDP_PORT")
    if env:
        return [int(p) for p in str(env).replace(" ", "").split(",") if p]
    return list(DEFAULT_PORTS)


def listening(port: int, host: str = "127.0.0.1", timeout: float = 0.4) -> bool:
    try:
        with socket.create_connection((host, int(port)), timeout=timeout):
            return True
    except OSError:
        return False


def describe(port: int, host: str = "localhost") -> dict:
    """그 포트가 살아 있나 + **누가 점유 중인가**(탭 제목/URL). 점유자 확인이 요점이다."""
    if not listening(port):
        return {"port": port, "listening": False, "tabs": []}
    try:
        tabs = [{"title": (t.get("title") or "")[:70], "url": (t.get("url") or "")[:110]}
                for t in CDPClient.pages(host, port)]
    except Exception as e:                       # 살아 있는데 /json 이 안 열리는 경우
        return {"port": port, "listening": True, "tabs": [], "error": f"{type(e).__name__}: {e}"}
    return {"port": port, "listening": True, "tabs": tabs}


def _has(tabs: list[dict], want: str) -> bool:
    w = want.lower()
    return any(w in (t["title"] + " " + t["url"]).lower() for t in tabs)


def chrome_exe() -> str:
    exe = os.environ.get("DEGAJA_CHROME")
    if exe and Path(exe).exists():
        return exe
    for c in _CHROME_CANDIDATES:
        if Path(c).exists():
            return c
    raise FileNotFoundError("chrome.exe 를 못 찾았다 — 환경변수 DEGAJA_CHROME 에 경로를 줘라")


def launch(port: int, profile: str, url: str = "about:blank", wait: float = 20.0) -> bool:
    """전용 디버그 프로필로 크롬을 띄우고 포트가 열릴 때까지 기다린다.

    ⚠ **그 프로필을 쓰는 크롬이 이미 떠 있으면** 새 창만 열리고 디버그 포트는 안 열린다
    (크롬 제약). 그때는 False 를 돌려주니 사람이 그 창을 닫아야 한다.
    """
    prof = Path(os.path.expandvars(os.path.expanduser(profile)))
    subprocess.Popen(
        [chrome_exe(), f"--remote-debugging-port={int(port)}",
         f"--user-data-dir={prof}", "--no-first-run", "--no-default-browser-check",
         "--restore-last-session=false", url],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    deadline = time.time() + wait
    while time.time() < deadline:
        if listening(port):
            return True
        time.sleep(0.5)
    return False


def ensure(*, site: str | None = None, want: str | None = None, ports=None,
           profile: str | None = None, url: str | None = None,
           do_launch: bool = True, open_tab: bool = True) -> dict:
    """원하는 세션이 있는 포트를 찾아 돌려준다. 없으면(허용 시) 띄우고 탭을 연다.

    반환: `{"port":…, "action":…, "tabs":[…], "scanned":[…], "hint":…}`
    `action` 은 `found`(그대로 쓰면 됨) · `opened_tab` · `launched` · `blocked`(사람 필요).
    """
    entry = {}
    if site:
        entry = _sites.get_site(site)
        want = want or site.split("_")[0]
        profile = profile or entry.get("profile")
        ports = ports or entry.get("ports")
        if url is None and entry.get("go"):
            url = next(iter(entry["go"].values()))
    # 지도에 프로필이 없는 사이트(open)는 이 리포 전용 디버그 프로필로 띄운다 —
    # 남의 일상 크롬 프로필을 디버그 포트로 열지 않기 위해서다.
    profile = profile or os.environ.get("DEGAJA_CHROME_PROFILE")         or str(Path.home() / "chrome-debug-degaja")
    cands = candidate_ports(ports)
    scanned = [describe(p) for p in cands]

    if want:
        for d in scanned:
            if d["listening"] and _has(d["tabs"], want):
                return {"port": d["port"], "action": "found", "tabs": d["tabs"],
                        "scanned": scanned}
    else:                                        # 원하는 게 없으면 살아 있는 첫 포트
        for d in scanned:
            if d["listening"]:
                return {"port": d["port"], "action": "found", "tabs": d["tabs"],
                        "scanned": scanned}

    # 살아 있지만 그 세션이 없다 = 다른 프로필이 점유 중일 수 있다.
    live = [d for d in scanned if d["listening"]]
    if live and open_tab and url:
        d = live[0]
        # 점유자가 남의 크롬이면 탭을 여는 것도 남의 창을 건드리는 것이다 — 그래서
        # 세션 사이트(로그인 필요)는 프로필이 맞는 포트에서만 연다.
        if entry.get("access") != "session" or profile is None:
            CDPClient.new_tab(url, port=d["port"])
            return {"port": d["port"], "action": "opened_tab",
                    "tabs": describe(d["port"])["tabs"], "scanned": scanned}

    if do_launch and profile:
        free = next((d["port"] for d in scanned if not d["listening"]), None)
        if free is None:
            return {"port": None, "action": "blocked", "scanned": scanned,
                    "hint": f"후보 포트 {cands} 가 전부 다른 크롬에 점유됐다. 점유자 탭을 보고 "
                            "(위 scanned) 그 창을 닫거나 --port 로 빈 포트를 하나 더 줘라."}
        if launch(free, profile, url or "about:blank"):
            return {"port": free, "action": "launched", "tabs": describe(free)["tabs"],
                    "scanned": scanned, "hint": f"profile={profile}"}
        return {"port": None, "action": "blocked", "scanned": scanned,
                "hint": f"{free} 로 기동했으나 포트가 안 열렸다 — 그 프로필({profile})을 쓰는 "
                        "크롬이 이미 떠 있을 가능성이 높다. 그 창을 닫고 다시."}

    return {"port": None, "action": "blocked", "scanned": scanned,
            "hint": "원하는 세션이 있는 포트가 없다. 지도에 profile 이 없으면 사람이 한 번 "
                    "로그인해줘야 한다(자동 로그인 금지)."}
