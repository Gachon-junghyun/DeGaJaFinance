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
"""
from __future__ import annotations

import argparse

from ._blindspot import cli_register as _reg_blindspot
from ._chain_hop import cli_register as _reg_chain_hop
from ._config import utf8_stdout
from ._coverage import cli_register as _reg_coverage
from ._fetch import cli_register as _reg_fetch
from ._fts import cli_register as _reg_fts
from ._search import cli_register as _reg_search
from ._theme_age import cli_register as _reg_theme_age

REGISTRARS = [_reg_fetch, _reg_search, _reg_fts, _reg_coverage, _reg_blindspot,
              _reg_theme_age, _reg_chain_hop]


def main() -> None:
    utf8_stdout()
    ap = argparse.ArgumentParser(
        prog="module_news_data",
        description="뉴스 데이터 소비층 — 검색·색인·커버리지·발굴 (수집은 옛 리포 cron 소유)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    for reg in REGISTRARS:
        reg(sub)
    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
