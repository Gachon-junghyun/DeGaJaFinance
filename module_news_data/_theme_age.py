# -*- coding: utf-8 -*-
"""theme_age — 테마 신규성 점수, 첫 보도 vs 메아리 판별 (옛 theme_age.py 포팅).

velocity(지금 시끄러운가)에 없는 축 — "언제부터 시끄러웠나"로 소비된 서사(메아리)와
갓 태어난 서사(알파)를 가른다. news_fts 색인 재사용, 신규 수집 0.

판정: FRESH(나이≤14d+가속≥2x, 골든존) / ACCELERATING(재점화) / ECHO(0.5~2x 메아리)
     / FADING(<0.5x 소멸) / SILENT(매칭 0)
FRESH + RS 아직 안 늘어남 = 서사가 가격보다 앞선 셋업(VRTX형).

사용:
    python -m module_news_data theme-age "Strait of Hormuz" humanoid --scope foreign
    python -m module_news_data theme-age geothermal --window 120 --json
"""
from __future__ import annotations

import json
import sqlite3
import sys
from datetime import datetime, timedelta, timezone

from ._config import FOREIGN_SOURCES, FTS_DB, utf8_stdout
from ._timeaxis import market_day, parse_published


def daily_counts(con: sqlite3.Connection, term: str, days: int, scope: str,
                 asof: str | None = None) -> dict[str, int]:
    """테마 텀의 일별 기사 수 {market_day: n}.

    2026-10-31 sim/news 수선: ①일자를 `fetched_at` 앞 10자가 아니라 `_timeaxis.market_day`
    (발행시각)로 센다 — 수집이 밀렸다 몰리면 수집 공백이 가짜 «갓 태어난 테마»가 된다(MODULE_MAP ⚠).
    ②`asof`(YYYY-MM-DD 또는 ISO 시각)를 주면 그 시각까지 발행된 것만 센다 — 과거 시점 재현용.
    발행시각이 빈 행(2026-05 이전)은 예전처럼 fetched_at 일자로 센다.
    """
    end = datetime.fromisoformat(asof) if asof else datetime.now()
    if len(asof or "") == 10:
        end = end + timedelta(days=1)            # 날짜만 주면 그날 끝까지
    since = (end - timedelta(days=days + 1)).isoformat()
    where = ["news_fts MATCH ?", "fetched_at >= ?"]
    params: list = [f'"{term}"', since]
    if scope == "foreign":
        where.append("source IN (" + ",".join("?" * len(FOREIGN_SOURCES)) + ")")
        params += FOREIGN_SOURCES
    elif scope == "domestic":
        where.append("source NOT IN (" + ",".join("?" * len(FOREIGN_SOURCES)) + ")")
        params += FOREIGN_SOURCES
    q = f"""SELECT published_at, source, fetched_at FROM news_fts
            WHERE {' AND '.join(where)}"""
    out: dict[str, int] = {}
    end_utc = end.astimezone(timezone.utc) if end.tzinfo else end.replace(tzinfo=timezone.utc)
    for pub, src, fx in con.execute(q, params):
        dt = parse_published(pub)
        if dt is not None:
            if asof and dt > end_utc:
                continue                          # 미래 엿보기 금지
            d = market_day(pub, src)
        else:
            d = (fx or "")[:10] or None
        if d:
            out[d] = out.get(d, 0) + 1
    return out


def analyze(term: str, counts: dict[str, int], days: int, asof: str | None = None) -> dict:
    # asof: 판정 기준일(YYYY-MM-DD). 없으면 오늘. 2026-10-31 sim/news 수선 — 예전엔 늘 «오늘»이라
    # 과거 시점으로 되돌려 잴 수 없었다. 기준일 뒤 칸은 버린다(미래 엿보기 금지).
    today = datetime.fromisoformat(asof[:10]).date() if asof else datetime.now().date()
    lo = (today - timedelta(days=days)).isoformat()
    # 창 밖(기준일 뒤 = 미래, 창 앞 = 옛 발행일이 늦게 수집된 것)은 버린다 — 옛 발행 1건이 first_seen 을 2024 로 끌었다(실측)
    counts = {d: n for d, n in counts.items() if lo <= d <= today.isoformat()}
    if not counts:
        return {"term": term, "verdict": "SILENT", "age_days": None,
                "recent7_avg": 0.0, "prior30_avg": 0.0, "accel": None, "total": 0}
    first = min(counts)
    first_d = datetime.strptime(first, "%Y-%m-%d").date()
    age = (today - first_d).days
    win_start = today - timedelta(days=days)
    censored = (first_d - win_start).days <= 7   # 윈도 첫 주에 이미 존재 → 더 오래됐을 수 있음

    def avg(d0: int, d1: int) -> float:
        span = [today - timedelta(days=i) for i in range(d1, d0)]
        return sum(counts.get(d.isoformat(), 0) for d in span) / max(len(span), 1)

    r7 = avg(7, 0)
    p30 = avg(37, 7)
    accel = (r7 / p30) if p30 > 0 else (float("inf") if r7 > 0 else 0.0)

    if r7 == 0:
        v = "FADING"
    elif accel >= 2:
        v = "FRESH" if (age <= 14 and not censored) else "ACCELERATING"
    elif accel >= 0.5:
        v = "ECHO"
    else:
        v = "FADING"
    return {"term": term, "verdict": v,
            "age_days": f">={days}" if censored else age,
            "first_seen": first, "recent7_avg": round(r7, 1),
            "prior30_avg": round(p30, 1),
            "accel": None if accel == float("inf") else round(accel, 2),
            "total": sum(counts.values())}


def run(terms: list[str], window: int, scope: str, as_json: bool, asof: str | None = None) -> None:
    utf8_stdout()
    if not FTS_DB.exists():
        sys.exit("news_fts.db 없음 — 먼저 `fts build`")
    con = sqlite3.connect(str(FTS_DB))

    results = [analyze(t, daily_counts(con, t, window, scope, asof), window, asof) for t in terms]
    results.sort(key=lambda r: ({"FRESH": 0, "ACCELERATING": 1, "ECHO": 2,
                                 "FADING": 3, "SILENT": 4}[r["verdict"]],
                                -(r["recent7_avg"] or 0)))

    if as_json:
        print(json.dumps({"window_days": window, "scope": scope,
                          "themes": results}, ensure_ascii=False, indent=1))
        return

    icon = {"FRESH": "🟢", "ACCELERATING": "🟡", "ECHO": "⚪", "FADING": "🔴", "SILENT": "⚫"}
    print(f"# theme_age — 신규성 점수 ({window}d/{scope})")
    print(f"  {'테마':28s} {'판정':14s} {'나이':>8s} {'7d평균':>7s} {'가속':>6s} {'총건수':>6s}")
    for r in results:
        a = "-" if r["accel"] is None else f"{r['accel']}x"
        age = "-" if r["age_days"] is None else str(r["age_days"])
        print(f"  {r['term']:28s} {icon[r['verdict']]}{r['verdict']:12s} {age:>8s} "
              f"{r['recent7_avg']:7.1f} {a:>6s} {r['total']:6d}")
    print("\n  🟢FRESH=갓 태어나 가속(골든존) 🟡ACCEL=옛 테마 재점화 ⚪ECHO=메아리 🔴FADING=소멸")
    print("  다음 행동: FRESH 테마 → chain-hop 으로 안 명명된 수혜자 발굴 → 수급 교차.")


def cli_register(sub) -> None:
    p = sub.add_parser("theme-age", help="테마 나이·가속 (FRESH/ECHO 판별)")
    p.add_argument("terms", nargs="+", help="테마 텀(구문은 따옴표)")
    p.add_argument("--window", type=int, default=90, help="관측 윈도(일)")
    p.add_argument("--scope", choices=["all", "foreign", "domestic"], default="foreign")
    p.add_argument("--json", action="store_true")
    p.add_argument("--asof", default=None, help="판정 기준일 YYYY-MM-DD(과거 시점 재현, 기본 오늘)")
    p.set_defaults(func=lambda a: run(a.terms, a.window, a.scope, a.json, a.asof))
