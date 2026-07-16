# -*- coding: utf-8 -*-
"""module_news_data 통합 CLI — 기능별 서브커맨드.

각 기능 파일이 cli_register(subparsers) 로 자기 서브커맨드를 등록한다.
새 기능 추가 = _파일 작성 + 아래 REGISTRARS 에 한 줄 (CLAUDE.md P2).

    python -m module_news_data search "변압기" HVDC --days 14
    python -m module_news_data fts search "rate cut" --days 14 --scope foreign
    python -m module_news_data coverage nuclear --days 30 --scope foreign
    python -m module_news_data blindspot --days 7 --scope foreign
    python -m module_news_data theme-age humanoid --scope foreign
    python -m module_news_data chain-hop "data center" power --days 14

원격(서버 PC) 모드: `DEGAJA_NEWS_API` 가 켜져 있으면 **DB 를 읽는 모든 조회
서브커맨드**(search·fts search·coverage·blindspot·theme-age·chain-hop)를 서버의
`/exec` 로 넘겨 실행하고 결과를 그대로 출력한다 — 로컬 뉴스 DB 가 없어도(지웠어도)
동작한다. 쓰기(fetch·fts build/update)는 서버 PC 에서만.
"""
from __future__ import annotations

import argparse
import sys

from ._blindspot import cli_register as _reg_blindspot
from ._chain_hop import cli_register as _reg_chain_hop
from ._config import NEWS_API_BASE, utf8_stdout
from ._coverage import cli_register as _reg_coverage
from ._fetch import cli_register as _reg_fetch
from ._fts import cli_register as _reg_fts
from ._search import cli_register as _reg_search
from ._theme_age import cli_register as _reg_theme_age

REGISTRARS = [_reg_fetch, _reg_search, _reg_fts, _reg_coverage, _reg_blindspot,
              _reg_theme_age, _reg_chain_hop]

# DB 를 직접 읽는 조회 서브커맨드 — 원격 모드에서 서버 /exec 로 라우팅된다.
DB_READ_CMDS = {"search", "fts", "coverage", "blindspot", "theme-age", "chain-hop"}


def build_parser() -> argparse.ArgumentParser:
    """CLI 파서 단일 원본 — CLI 와 서버 /exec 가 같은 파서를 쓴다(P1)."""
    ap = argparse.ArgumentParser(
        prog="module_news_data",
        description="뉴스 데이터 — 검색·색인·커버리지·발굴 (수집=Server/, 원격검색=DEGAJA_NEWS_API)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    for reg in REGISTRARS:
        reg(sub)
    return ap


def _is_write(raw: list[str]) -> bool:
    """쓰기 계열(클라이언트에서 원격 라우팅 대상 아님)."""
    if not raw:
        return False
    if raw[0] == "fetch":
        return True
    if raw[0] == "fts" and len(raw) > 1 and raw[1] in ("build", "update"):
        return True
    return False


def main() -> None:
    utf8_stdout()
    raw = sys.argv[1:]
    cmd = raw[0] if raw else None

    # ── 원격 모드: DB 읽는 조회는 서버에서 실행 ─────────────────────────
    if NEWS_API_BASE and cmd in DB_READ_CMDS and not _is_write(raw):
        from ._api_client import exec_remote
        res = exec_remote(NEWS_API_BASE, raw)
        if res.get("error"):
            print(res["error"], file=sys.stderr)
            sys.exit(2)
        sys.stderr.write(f"(via NEWS API @ {NEWS_API_BASE})\n")
        out = res.get("stdout", "")
        sys.stdout.write(out if (not out or out.endswith("\n")) else out + "\n")
        return
    if NEWS_API_BASE and _is_write(raw):
        print(f"'{' '.join(raw[:2])}' 는 쓰기 계열 — 서버 PC(Server/)에서 실행하라. "
              f"클라이언트(DEGAJA_NEWS_API 설정)는 조회만 한다.", file=sys.stderr)
        sys.exit(2)

    # ── 로컬 모드(단일 PC 또는 서버 자신) ──────────────────────────────
    args = build_parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
