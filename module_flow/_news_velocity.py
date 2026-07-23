# -*- coding: utf-8 -*-
"""① 뉴스속도 (기대감) — 기사량 최근 vs 베이스 → 관심 가속비. >1 = 가속.

수정 이력 (2026-07-23) — 이 축은 **KR 에서 구조적으로 항상 n/a 였다.** 두 개의 독립 버그:

  ① **스코프 고정 버그(P3 위반).** 소스 필터가 `source IN (FOREIGN_SOURCES)` 로 하드코딩돼
     있었다. KR 종목의 뉴스는 전부 국내지(yonhap·mk·sedaily·chosun…)이므로 **로컬 색인이
     멀쩡해도 모든 KR 티커가 0건 → velocity None → "n/a"**. 모듈은 이미 `kr_code()` 로
     KR 을 자동판별하는데 이 축만 그 판별을 쓰지 않았다.
  ② **API 경로 미사용(P6 위반).** `FTS_DB` sqlite 파일을 **직접** 열었다. 클라이언트는
     뉴스 DB 를 소유하지 않고 `DEGAJA_NEWS_API` 로 서버에 넘긴다(CLAUDE.md P6) —
     실측 `data/news_fts.db` **부재**. 그래서 API 가 켜져 있어도 이 축만 로컬 파일을
     찾다가 조용히 None 을 뱉었다.

수정 방침: 전송은 `module_news_data._api_client.exec_remote` 를 **재사용**(P1, 재구현 0),
스코프는 `kr` 플래그로 흡수(P3), 로컬 폴백은 `source NOT IN (foreign)` = 국내로 뒤집는다
(국내 소스 목록을 여기 복제하지 않는다 — 복제하면 두 곳이 갈라진다).
그리고 **불가할 때 조용히 None 을 주지 않고 `note` 로 이유를 남긴다**(P4: 모르면 모른다고).
"""
from __future__ import annotations

import os
import re
import sqlite3
from datetime import datetime, timedelta

from ._config import FOREIGN_SOURCES, FTS_DB, STOPWORD_TICKERS


def news_query(ticker: str, name: str | None) -> str:
    """뉴스속도 검색어 — 단어형/짧은 티커는 회사명만(오염 방지), 안전한 티커는 티커|명.

    KR 은 두 가지를 더 흡수한다(실측 2026-07-23, 국내 7일):
      · **접미사를 뗀 6자리 코드가 살아있는 검색어다** — 기사 본문/제목이 "기아(000270)"
        형태로 코드를 싣는다. `000270` **18건** vs `000270.KS` 0건.
      · **2글자 국문명은 트라이그램 색인에 없다** — `기아` **0건**(색인 부재이지 무기사 아님)
        vs `기아차` 5건. 그래서 2글자 이하 이름은 검색어에서 빼고 **코드가 그 몫을 진다**.
    """
    from ._config import kr_code  # 지연 import(순환 방지)

    code = kr_code(ticker)
    if code:                       # KR: 코드(접미사 제거) + 3글자 이상 이름
        parts = [code]
        if name and len(name.strip()) >= 3:
            parts.append(name.strip())
        return "|".join(parts)

    safe = len(ticker) >= 4 and ticker.upper() not in STOPWORD_TICKERS
    if name:
        return f"{ticker}|{name}" if safe else name
    return ticker  # 명 없음 = 티커 best-effort(짧으면 노이즈 가능)


def _api_base() -> str:
    return (os.environ.get("DEGAJA_NEWS_API", "") or "").strip().rstrip("/")


def _terms(query: str) -> list[str]:
    """'A|B' → ['A','B']. ⚠ 다중어를 따옴표로 묶어 한 argv 로 넘기면 트라이그램 색인에서
    조용히 ~0 이 된다(실측: 3어 묶음 1건 vs 분리 31,698건) — 반드시 분리 argv."""
    return [q.strip() for q in query.split("|") if q.strip()]


def _count_remote(base: str, terms: list[str], days: int, kr: bool) -> int | None:
    """서버 /exec 에 CLI argv 를 그대로 넘긴다 — 재구현 0(P1).

    argv 는 사람이 치는 것과 동일: `fts search <t1> <t2> --scope … --days N --count`.
    """
    from module_news_data._api_client import exec_remote  # 지연 import (P6)

    argv = ["fts", "search", *terms,
            "--scope", "domestic" if kr else "foreign",
            "--days", str(days), "--mode", "or", "--count"]
    if kr:
        argv.append("--kr")   # 국문 트라이그램 색인(2글자어는 0 = 색인 부재)
    res = exec_remote(base, argv)
    if not isinstance(res, dict) or "stdout" not in res:
        return None
    nums = re.findall(r"\b(\d+)\b", res.get("stdout", ""))
    return int(nums[-1]) if nums else None


def _count_local(terms: list[str], days: int, kr: bool) -> int | None:
    """로컬 FTS 폴백. 스코프를 소스집합으로 흡수 — 국내는 'foreign 이 아닌 것'으로 정의해
    국내 소스 목록 복제를 피한다(P1)."""
    db = FTS_DB
    if kr:
        try:
            from module_news_data._config import FTS_DB_KR  # 국문 트라이그램 색인
            if FTS_DB_KR.exists():
                db = FTS_DB_KR
        except Exception:
            pass
    if not db.exists():
        return None
    cut = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    ph = ",".join("?" * len(FOREIGN_SOURCES))
    op = "NOT IN" if kr else "IN"
    match = " OR ".join(f'"{t}"' for t in terms)
    sql = (f"SELECT COUNT(*) FROM news_fts WHERE news_fts MATCH ? "
           f"AND source {op} ({ph}) AND fetched_at >= ?")
    try:
        con = sqlite3.connect(str(db))
        try:
            return con.execute(sql, [match] + FOREIGN_SOURCES + [cut]).fetchone()[0]
        finally:
            con.close()
    except Exception:
        return None


def news_velocity(query: str, recent: int, base: int, kr: bool = False) -> dict:
    """기사량 최근 vs 베이스 → 관심 가속비.

    `kr=True` 면 국내 스코프(+국문 트라이그램 색인)로 센다. 호출부는 `kr_code(ticker)` 로
    자동판별해 넘긴다 — 시장별 파일 미러링 금지(P3).
    """
    terms = _terms(query)
    if not terms:
        return {"recent": None, "base_rate": None, "velocity": None, "note": "빈 검색어"}

    api = _api_base()
    src = "api" if api else "local"
    if api:
        r, b = _count_remote(api, terms, recent, kr), _count_remote(api, terms, base, kr)
        if r is None or b is None:          # 서버 실패 → 로컬 폴백(설계상 허용 경로)
            r2, b2 = _count_local(terms, recent, kr), _count_local(terms, base, kr)
            if r2 is None or b2 is None:
                return {"recent": None, "base_rate": None, "velocity": None,
                        "note": "뉴스 API 응답 실패 + 로컬 FTS 색인 없음"}
            r, b, src = r2, b2, "local(폴백)"
    else:
        r, b = _count_local(terms, recent, kr), _count_local(terms, base, kr)
        if r is None or b is None:
            return {"recent": None, "base_rate": None, "velocity": None,
                    "note": f"로컬 FTS 색인 없음({FTS_DB.name}) — DEGAJA_NEWS_API 를 켜라"}

    rr, br = r / recent, b / base
    vel = (rr / br) if br > 0 else (None if r == 0 else 9.99)
    out = {"recent": r, "base": b, "recent_rate": round(rr, 2), "base_rate": round(br, 2),
           "velocity": round(vel, 2) if vel is not None else None,
           "scope": "domestic" if kr else "foreign", "source": src}
    if vel is None:
        out["note"] = "해당 기간 기사 0건 (색인 부재가 아니라 실제 무기사)"
    return out
