# -*- coding: utf-8 -*-
"""블라인드스팟 발굴 — 고정 검색어가 못 보는 풀을 드러낸다 (옛 news_blindspot.py 포팅).

본문검색을 켜도 '내가 질의한 단어'의 recall만 오른다 — 안 떠오른 테마(unknown
unknowns)는 영원히 안 보인다. 이 엔진은 그 사각을 productive 하게:
  ① 커버리지 ② 블라인드 풀 ③ 랜덤 샘플 N(에이전트가 읽음)
  ④ 토큰0 신흥어(블라인드 풀 제목의 티커/고유명사 빈도 top)

사용:
    python -m module_news_data blindspot nuclear tariff --days 14 --scope foreign --json
    python -m module_news_data blindspot --days 7 --scope foreign    # 순수 발굴
"""
from __future__ import annotations

import json
import random
import re
import sqlite3
from collections import Counter
from datetime import datetime, timedelta

from ._config import FOREIGN_SOURCES, NEWS_DB, OUT_DIR, utf8_stdout

BLINDSPOT_OUT = OUT_DIR / "news_blindspot"

# 신흥어 추출 노이즈 컷 — 흔한 영어/금융 일반어(고유명사·티커만 남기려고).
STOP = {
    "THE", "A", "AN", "AND", "OR", "OF", "TO", "IN", "ON", "AT", "FOR", "BY", "AS", "IS",
    "ARE", "WAS", "WILL", "WITH", "FROM", "THAT", "THIS", "IT", "ITS", "BE", "HAS", "HAVE",
    "NEW", "SAYS", "SAID", "AFTER", "OVER", "AMID", "INTO", "UP", "DOWN", "OUT", "MORE",
    "STOCK", "STOCKS", "MARKET", "MARKETS", "SHARES", "SHARE", "REPORT", "NEWS", "US", "U.S",
    "Q1", "Q2", "Q3", "Q4", "CEO", "CFO", "INC", "CORP", "LTD", "ETF", "IPO", "GDP", "CPI",
    "HOW", "WHY", "WHAT", "WHO", "WHEN", "TOP", "BEST", "VS", "YEAR", "WEEK", "DAY", "DEAL",
    "HIGH", "LOW", "BIG", "CAN", "MAY", "GET", "NOW", "ONE", "TWO", "RISE", "FALL", "GAIN",
    "FILER", "BUY", "SELL", "HOLD", "HERE", "CALL", "PUT", "TRANSCRIPT", "INVESTORS",
    "PRICE", "FUND", "FUNDS", "GROWTH", "UPDATE", "ALERT", "WATCH", "LIST", "GUIDE", "REVIEW",
    "YOU", "YOUR", "NOT", "COULD", "WOULD", "SHOULD", "TODAY", "THESE", "THOSE",
    "WHILE", "BEFORE", "ABOUT", "JUST", "STILL", "EVEN", "MOST", "SOME", "MANY", "SUCH",
    "THAN", "THEN", "WHERE", "WHICH", "THERE", "THEIR", "THEY",
    "AMONG", "AGAINST", "DURING", "BETWEEN", "ANALYSIS", "OUTLOOK", "FORECAST",
}
TICKER_RE = re.compile(r"\b[A-Z]{2,5}\b")          # ALLCAPS 2-5 = 티커 후보
PROPER_RE = re.compile(r"\b[A-Z][a-zA-Z]{2,}\b")    # 대문자시작 = 고유명사 후보


def _scope_where(scope, params):
    ph = ",".join("?" * len(FOREIGN_SOURCES))
    if scope == "foreign":
        params.extend(FOREIGN_SOURCES); return f"s.source IN ({ph})"
    if scope == "domestic":
        params.extend(FOREIGN_SOURCES); return f"(s.source IS NULL OR s.source NOT IN ({ph}))"
    return "1=1"


def _kw_titlesum(kws, params):
    parts = []
    for kw in kws:
        k = f"%{kw}%"; parts.append("(s.title LIKE ? OR s.summary LIKE ?)"); params.extend([k, k])
    return "(" + " OR ".join(parts) + ")"


def emergent_terms(titles: list[str], top: int) -> list[tuple[str, int]]:
    """블라인드 풀 제목에서 티커/고유명사 빈도 top — 토큰0 신흥어 발굴."""
    tick, prop = Counter(), Counter()
    for t in titles:
        for m in set(TICKER_RE.findall(t)):
            if m not in STOP:
                tick[m] += 1
        for m in set(PROPER_RE.findall(t)):
            u = m.upper()
            if u not in STOP and not TICKER_RE.fullmatch(m):
                prop[m] += 1
    merged = Counter()
    for w, c in tick.items():
        merged[f"{w} (ticker?)"] = c
    for w, c in prop.items():
        merged[w] += c
    return merged.most_common(top)


def run(kws, days, scope, sample_n, top_kw, as_json, sample_pct=None) -> None:
    utf8_stdout()
    con = sqlite3.connect(str(NEWS_DB)); con.row_factory = sqlite3.Row; c = con.cursor()

    def where(extra):
        p: list = []; w = [_scope_where(scope, p)]
        if days is not None:
            p.append((datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d"))
            w.append("s.fetched_at >= ?")
        if extra:
            w.append(extra(p))
        return " AND ".join(w), p

    total_w, total_p = where(None)
    total = c.execute(f"SELECT COUNT(*) FROM seen_news s WHERE {total_w}", total_p).fetchone()[0]

    if kws:
        m_w, m_p = where(lambda p: _kw_titlesum(kws, p))
        matched = c.execute(f"SELECT COUNT(*) FROM seen_news s WHERE {m_w}", m_p).fetchone()[0]
        blind_w, blind_p = where(lambda p: "NOT " + _kw_titlesum(kws, p))
    else:
        matched = 0
        blind_w, blind_p = total_w, total_p

    blind_rows = c.execute(
        f"SELECT s.url_hash, s.title, s.source, COALESCE(s.published_at,s.fetched_at) d "
        f"FROM seen_news s WHERE {blind_w}", blind_p).fetchall()
    blind_n = len(blind_rows)

    titles = [r["title"] or "" for r in blind_rows]
    terms = emergent_terms(titles, top_kw)

    # 샘플 크기: --sample-pct 주면 블라인드 풀의 N%, 아니면 고정 --sample.
    target_n = int(blind_n * sample_pct / 100.0) if sample_pct else sample_n
    target_n = max(1, min(target_n, blind_n)) if blind_n else 0
    random.seed(f"{datetime.now():%Y-%m-%d}-{scope}")   # 일내 재현, 일별 회전
    sample = random.sample(blind_rows, target_n) if blind_n else []

    cov = round(100.0 * matched / total, 1) if total else 0.0
    rep = {
        "date": f"{datetime.now():%Y-%m-%d}", "query": kws, "days": days, "scope": scope,
        "window_total": total, "matched_titlesum": matched, "coverage_pct": cov,
        "blind_pool": blind_n, "sample_size": len(sample),
        "emergent_terms": [{"term": t, "count": n} for t, n in terms],
        "sample": [{"url_hash": r["url_hash"], "date": (r["d"] or "")[:10],
                    "source": r["source"], "title": r["title"]} for r in sample],
    }

    if as_json:
        BLINDSPOT_OUT.mkdir(parents=True, exist_ok=True)
        fp = BLINDSPOT_OUT / f"{rep['date']}.json"
        fp.write_text(json.dumps(rep, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps({k: v for k, v in rep.items() if k != "sample"}, ensure_ascii=False, indent=2))
        print(f"\n(sample {len(sample)}건 + 전체 JSON → {fp})")
        con.close(); return

    sc = {"all": "국내+해외", "foreign": "해외만", "domestic": "국내만"}[scope]
    rng = f"최근 {days}일" if days else "전체기간"
    print(f"\n# 뉴스 블라인드스팟 — {', '.join(kws) or '(고정셋 없음=순수발굴)'}  [{rng}/{sc}]")
    print(f"  윈도우 전체(분모)      : {total}건")
    if kws:
        print(f"  현재 검색어 매칭       : {matched}건  → 커버리지 {cov}%  (나머지 {100-cov:.1f}%가 블라인드 풀)")
    print(f"  블라인드 풀            : {blind_n}건  (랜덤 샘플 {len(sample)}건 발췌)")
    print(f"\n  ── 토큰0 신흥어 top{top_kw} (블라인드 풀 제목 빈도 — 고정셋에 없는 '뜨는 단어') ──")
    for t, n in terms:
        print(f"     {n:>4}  {t}")
    print(f"\n  ── 랜덤 샘플 {min(8, len(sample))}건 미리보기 (전체는 --json) ──")
    for r in sample[:8]:
        print(f"     {(r['d'] or '')[:10]} [{r['source']:>13}] {r['title']}")
    print("\n  → 다음: 신흥어/샘플에서 '뜨는데 고정셋에 없는' 테마 잡고, 중요한 건")
    print("    search --field any 로 본문까지 집중조사 → 고정셋 추가어 환류.")
    con.close()


def cli_register(sub) -> None:
    p = sub.add_parser("blindspot", help="못 본 풀 랜덤샘플 + 토큰0 신흥어 발굴")
    p.add_argument("keywords", nargs="*", help="데스크 현재 검색어(생략=순수 발굴)")
    p.add_argument("--days", type=int, default=None)
    p.add_argument("--scope", choices=["all", "foreign", "domestic"], default="all")
    p.add_argument("--sample", type=int, default=400, help="고정 샘플 수(--sample-pct 없을 때)")
    p.add_argument("--sample-pct", type=float, default=None, dest="sample_pct",
                   help="블라인드 풀의 N%% 샘플")
    p.add_argument("--top-kw", type=int, default=30, dest="top_kw")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=lambda a: run(
        a.keywords, a.days, a.scope, a.sample, a.top_kw, a.json, a.sample_pct))
