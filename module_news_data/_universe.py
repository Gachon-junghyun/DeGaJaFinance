# -*- coding: utf-8 -*-
"""상장사 언급 판정 — "이 기사가 우리 유니버스의 회사를 말하나".

왜 있나: 뉴스 풀은 금융 코퍼스가 아니다(실측: 국내 62%가 종합지 — yonhap·chosun·
google_kr·donga). 그래서 '평소보다 튄 단어'를 뽑으면 폭우·송파구·아이들이 반도체·수주를
경쟁에서 이긴다. 지표가 틀린 게 아니라 **읽는 신문이 종합지**인 것.

소스로 자르는 건 반쪽이었다(실측: 경제지만 남겨도 폭우 6σ·남편 7σ가 살아남고, 정작
한화오션 특종은 yonhap 에 있었다 — 종합지를 버리면 기사를 버린다). 그래서 소스가 아니라
**기사 내용**으로 잰다: 그 기사가 상장사를 언급하나.

⚠ 이건 '고정 검색어'가 아니다. 종목 유니버스는 **이미 가진 자산**(kr_all.csv·us_top300)이라
열거 가능하고, 무엇이 뜰지 미리 안 정해도 된다 — 테마를 이름으로 찍는 게 아니라 '시장
얘기인지'만 본다. 안 떠오른 테마도 상장사를 말하면 그대로 잡힌다(블라인드스팟 안 생김).

⚠ 3글자 미만 한글 사명은 뺀다 — 대상·삼양·농심 같은 사명은 일반어와 충돌해 오탐을 만든다
(`_chain_hop.AMBIGUOUS_*` 와 같은 문제의 KR판). US 는 `_chain_hop.load_universe` 를
그대로 재사용한다(중복 0 — 별칭·모호티커 처리가 이미 거기 있다).
"""
from __future__ import annotations

import csv
from functools import lru_cache

from ._config import KR_UNIVERSE_CSV

KR_MIN_NAME_LEN = 3   # 2글자 사명은 일반어 충돌(대상·삼양·농심) → 제외


@lru_cache(maxsize=1)
def kr_names() -> frozenset[str]:
    """KR 상장사명 집합(3글자+). 유니버스 CSV 가 없으면 빈 집합(= 판정 불가)."""
    if not KR_UNIVERSE_CSV.exists():
        return frozenset()
    out = set()
    with open(KR_UNIVERSE_CSV, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            n = (row.get("name") or "").strip()
            if len(n) >= KR_MIN_NAME_LEN:
                out.add(n)
    return frozenset(out)


@lru_cache(maxsize=1)
def _us_patterns() -> tuple:
    """US 는 기존 로더 재사용(P1) — 별칭·모호티커 규칙을 다시 짓지 않는다."""
    from ._chain_hop import load_universe
    try:
        return tuple(p for meta in load_universe().values() for p in meta["patterns"])
    except (OSError, KeyError):
        return ()


def mentions_listed(text: str | None, foreign: bool) -> bool:
    """제목/본문이 유니버스 상장사를 언급하나. 유니버스가 없으면 False(모름=아님 아니다 —
    호출부가 커버리지를 함께 보고해야 한다)."""
    if not text:
        return False
    if foreign:
        return any(p.search(text) for p in _us_patterns())
    return any(n in text for n in kr_names())


def universe_size(foreign: bool) -> int:
    """판정 근거의 크기 — 0 이면 시장관련도는 전부 0 이 되므로 반드시 함께 보고한다."""
    return len(_us_patterns()) if foreign else len(kr_names())
