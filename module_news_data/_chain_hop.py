# -*- coding: utf-8 -*-
"""chain_hop — US 밸류체인 사슬-홉 발굴 (옛 chain_hop.py 포팅).

헤드라인이 명명한 종목의 알파는 이미 크라우디드. 진짜 알파는 같은 테마 기사
**본문에는 등장하는데 제목에는 안 불린** 이름에 있다(WMB 오라벨 vs MPC 실측,
2026-07-14). 시황 랩업 노이즈는 테마 텀 ±window자 근접 공동언급으로 컷.

유니버스 = 옛 리포 us_top300 + us_aliases (스몰캡·비상장은 이 도구 밖).

사용:
    python -m module_news_data chain-hop Hormuz oil tanker --days 7
    python -m module_news_data chain-hop "data center" power grid --days 14 --min-hits 3
    python -m module_news_data chain-hop HBM memory shortage --days 14 --json
"""
from __future__ import annotations

import csv
import json
import re
import sqlite3
import sys
from datetime import datetime, timedelta

from ._config import ALIASES_JSON, FOREIGN_SOURCES, FTS_DB, UNIVERSE_CSV, utf8_stdout

# 일반 영단어와 충돌하는 티커 — 티커 문자열 자체로는 매칭하지 않는다(별칭 이름으로만).
AMBIGUOUS_TICKERS = {
    "A", "IT", "ALL", "SO", "ON", "NOW", "ARE", "FAST", "COST", "KEY", "CAT",
    "MET", "AIG", "ICE", "WELL", "ANY", "SEE", "PEG", "O", "L", "DAY", "GAP",
    "HAS", "BIG", "TAP", "MA", "V", "CB", "RE", "AN", "IP", "IR", "GS", "MS",
    "PM", "AM", "TT", "IN", "OUT", "UP", "LOW", "NICE", "REAL", "LIVE", "OPEN",
}
# 이름이 너무 일반어인 별칭 제외 (Target/Progressive 실질 위험)
AMBIGUOUS_NAMES = {"Target", "Progressive"}


def load_universe() -> dict[str, dict]:
    """ticker -> {name, sector, industry, patterns[list[re.Pattern]]}"""
    alias_map: dict[str, list[str]] = {}
    if ALIASES_JSON.exists():
        alias_map = json.load(open(ALIASES_JSON, encoding="utf-8"))
    out: dict[str, dict] = {}
    with open(UNIVERSE_CSV, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            tk = row["ticker"].strip()
            names: set[str] = set()
            for a in alias_map.get(tk, [tk, row["name"]]):
                a = a.strip()
                if not a or not a.isascii():   # 한국어 별칭은 영문 코퍼스에 불필요
                    continue
                if a == tk:
                    if tk in AMBIGUOUS_TICKERS or len(tk) < 3:
                        continue
                    names.add(tk)              # 3자+ 비모호 티커는 그대로
                else:
                    if a in AMBIGUOUS_NAMES:
                        continue
                    names.add(a)
            pats = [re.compile(r"\b" + re.escape(n) + r"\b") for n in names]
            out[tk] = {
                "name": row["name"], "sector": row["gics_sector"],
                "industry": row["gics_industry"], "patterns": pats,
            }
    return out


def fetch_theme_articles(terms: list[str], days: int, scope: str, mode: str, limit: int):
    con = sqlite3.connect(str(FTS_DB)); con.row_factory = sqlite3.Row
    joiner = " AND " if mode == "and" else " OR "
    match = joiner.join(f'"{t}"' for t in terms)
    since = (datetime.now() - timedelta(days=days)).isoformat()
    where = ["news_fts MATCH ?", "fetched_at >= ?"]
    params: list = [match, since]
    if scope == "foreign":
        where.append("source IN (" + ",".join("?" * len(FOREIGN_SOURCES)) + ")")
        params += FOREIGN_SOURCES
    elif scope == "domestic":
        where.append("source NOT IN (" + ",".join("?" * len(FOREIGN_SOURCES)) + ")")
        params += FOREIGN_SOURCES
    q = f"""SELECT title, summary, body, source, fetched_at FROM news_fts
            WHERE {' AND '.join(where)} ORDER BY rank LIMIT ?"""
    params.append(limit)
    return con.execute(q, params).fetchall()


def run(terms, days, scope, mode, limit, min_hits, window, top, as_json) -> None:
    utf8_stdout()
    if not FTS_DB.exists():
        sys.exit("news_fts.db 없음 — 먼저 `fts build`")

    rows = fetch_theme_articles(terms, days, scope, mode, limit)
    uni = load_universe()

    # 같은 "기사"가 아니라 같은 "문단"(±window자)에서 테마와 공동언급돼야 사슬 신호.
    theme_pats = [re.compile(re.escape(t), re.IGNORECASE) for t in terms]

    counts: dict[str, dict] = {tk: {"title": 0, "body": 0, "near": 0, "sample": ""} for tk in uni}
    for r in rows:
        title = r["title"] or ""
        text = " ".join(filter(None, [r["summary"], r["body"]]))
        theme_spans = [m.start() for p in theme_pats for m in p.finditer(text)] if text else []
        for tk, info in uni.items():
            in_title = any(p.search(title) for p in info["patterns"])
            if in_title:
                counts[tk]["title"] += 1
                continue
            if not text:
                continue
            if not any(p.search(text) for p in info["patterns"]):
                continue
            counts[tk]["body"] += 1
            pos_list = [mm.start() for p in info["patterns"] for mm in p.finditer(text)][:20]
            if any(abs(cp - tp) <= window for cp in pos_list for tp in theme_spans):
                counts[tk]["near"] += 1
                if not counts[tk]["sample"]:
                    counts[tk]["sample"] = title[:90]

    headline = sorted(
        ((tk, c) for tk, c in counts.items() if c["title"] >= 1),
        key=lambda x: -(x[1]["title"] + x[1]["body"]))
    hidden = sorted(
        ((tk, c) for tk, c in counts.items()
         if c["title"] == 0 and c["near"] >= min_hits),
        key=lambda x: -x[1]["near"])

    if as_json:
        print(json.dumps({
            "terms": terms, "days": days, "n_articles": len(rows),
            "window_chars": window,
            "headline_named": [
                {"ticker": tk, "title_hits": c["title"], "body_hits": c["body"],
                 "industry": uni[tk]["industry"]} for tk, c in headline[:top]],
            "chain_hop_candidates": [
                {"ticker": tk, "near_hits": c["near"], "body_hits": c["body"],
                 "industry": uni[tk]["industry"],
                 "sample_title": c["sample"]} for tk, c in hidden[:top]],
        }, ensure_ascii=False, indent=1))
        return

    print(f"# chain_hop — 테마: {' '.join(terms)}  ({days}d/{scope}/{mode}, 기사 {len(rows)}건 스캔, 근접 ±{window}자)")
    print(f"\n## HEADLINE-NAMED (제목에 등장 = 이미 명명·크라우디드) top {min(top, len(headline))}")
    print(f"  {'TCK':6s} {'제목':>4s} {'본문':>4s}  산업")
    for tk, c in headline[:top]:
        print(f"  {tk:6s} {c['title']:4d} {c['body']:4d}  {uni[tk]['industry']}")
    print(f"\n## ★ CHAIN-HOP 후보 (제목 0회 + 테마 텀 근접 문단 공동언급 ≥{min_hits}건)")
    print(f"  {'TCK':6s} {'근접':>4s} {'본문':>4s}  {'산업':40s} 예시 기사")
    for tk, c in hidden[:top]:
        print(f"  {tk:6s} {c['near']:4d} {c['body']:4d}  {uni[tk]['industry']:40s} {c['sample']}")
    print("\n  다음 행동: 후보를 수급으로 교차 — OBV 매집+RS 아직 안 늘어난 놈이 진짜 사슬-홉 알파.")
    print("  (universe = us_top300 — 스몰캡 사슬-홉은 이 도구 밖. 유니콘/비상장은 잡지 않음.)")


def cli_register(sub) -> None:
    p = sub.add_parser("chain-hop", help="US 사슬-홉: 제목 미명명+본문 근접 공동언급 후보")
    p.add_argument("terms", nargs="+", help="테마 텀(구문은 따옴표)")
    p.add_argument("--days", type=int, default=7)
    p.add_argument("--scope", choices=["all", "foreign", "domestic"], default="foreign")
    p.add_argument("--mode", choices=["and", "or"], default="or")
    p.add_argument("--limit", type=int, default=1500, help="스캔할 최대 기사 수")
    p.add_argument("--min-hits", type=int, default=2, dest="min_hits", help="근접 최소 기사 수")
    p.add_argument("--window", type=int, default=300, help="테마 텀 근접 판정 거리(자)")
    p.add_argument("--top", type=int, default=25)
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=lambda a: run(
        a.terms, a.days, a.scope, a.mode, a.limit, a.min_hits, a.window, a.top, a.json))
