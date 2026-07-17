# -*- coding: utf-8 -*-
"""급등어 탐지 — "그날 판을 움직인 단어"를 고정 검색어 없이 뽑는다 (블라인드스팟 제거).

기존 발굴(`_blindspot.emergent_terms`)은 **빈도 top** 이라 보일러플레이트가 이긴다.
그래서 손으로 적은 STOP 리스트로 막는데, 그 리스트 자체가 '안 떠오른 건 못 막는'
고정셋 — 없애려던 블라인드스팟이 그대로 재발한다. 여기선 리스트 없이 코퍼스가 스스로
말하게 한다: **단어마다 자기 자신을 baseline 으로** 두고, 오늘 자기 평소보다 몇 σ 튀었나만 본다.

    z = (오늘 점유율 − 그 단어의 평소 점유율) / 그 단어의 표준편차

점유율(= 그 단어 기사수 ÷ **그날 전체 기사수**)을 쓰는 이유: 원시 카운트는 수집량에
오염된다(실측: 밀렸다 몰린 틱 761건 vs 평소 250건 — 뉴스가 3배 터진 게 아니라 수집이
밀린 것). 분모로 나누면 그 교란이 사라진다.

z 를 쓰면 **수준(DF)이 사라져** 흔한 말도 드문 말도 같은 자로 잰다 — 반도체(3.0%)든
원전(0.08%)든. 그리고 평평한 보일러플레이트(QUOT·종합)는 애초에 z 가 안 떠서 자동 탈락한다.
희소성=신호 가정을 쓰지 않는다(실측 반증: 제목에선 트럼프 1.53% > JTBC 0.08% 로 뒤집힌다).

⚠ **판정하지 않는다(P4).** 이 모듈은 '일상어/신호어'를 가르지 않고, 검증 가능한 후보표만
낸다 — 각 후보에 건수·분모·z·소스분산·근거기사 3건을 붙여서. 의미 판정은 상위(에이전트)가
한다. 설계 근거는 비대칭이다: false positive(사진 같은 잡음이 섞임)는 LLM 이 0.2초에
버리지만, false negative(안 떠오른 테마)는 **영영 안 보인다**. 그러니 여기서 똑똑하게
자르려 들면 손해다.

⚠ 두 축을 더 붙인다 — z 단독으론 사진·속보 같은 잔여 잡음이 남기 때문(실측 CV 0.61/0.41).
  · **소스분산(entropy 0~1)**: 한 매체가 혼자 쏟아내면 낮다(메아리). 진짜 사건은 여러 매체로 퍼진다.
  · **지속성(persist)**: 전날에도 떠 있었나. 보일러플레이트 스파이크는 하루살이다.
  둘 다 '판정'이 아니라 에이전트가 읽을 근거 — 자동으로 자르지 않는다.

사용:
    python -m module_news_data burst --days 1 --scope domestic
    python -m module_news_data burst --date 2026-07-07 --scope foreign --json
"""
from __future__ import annotations

import json
import math
import sqlite3
import statistics as st
from collections import Counter, defaultdict
from datetime import date as _date
from datetime import datetime, timedelta

from ._config import FOREIGN_SOURCES, NEWS_DB, OUT_DIR, utf8_stdout
from ._timeaxis import PUBLISHED_AT_SINCE, market_day
from ._tokenize import tokens
from ._universe import mentions_listed, universe_size

BURST_OUT = OUT_DIR / "news_burst"

BASELINE_DAYS = 30      # 그 단어의 '평소'를 재는 창(대상일 제외).
MIN_BASELINE_DAYS = 10  # 이보다 표본이 적으면 평소를 모른다 → z 계산 안 함.
MIN_COUNT = 3           # 그날 3건 미만은 통계가 아니라 우연.
Z_FLOOR = 2.0           # SPIKE 하한(자르는 게 아니라 '읽을 순서' — 낮추면 더 많이 나온다).

# ⚠ 평소를 **아는** 단어에만 z 를 쓴다. baseline 30일 중 등장일이 이 비율 미만이면
# 그 단어의 '평소'는 대부분 0 이라 표준편차가 0 에 붙고 z 가 폭발한다 — 하루 뜬 연예인
# 이름이 37σ 로 1등을 먹고, 정작 엔비디아(28/30일 등장, z≈3)가 묻힌다(실측).
# 그런 단어는 '튀었다'가 아니라 '처음 본다'가 맞는 서술 → NEW 로 분리해 건수로 세운다.
# 두 질문("평소 있던 게 튀었나" vs "처음 보는 게 떴나")을 한 척도로 재려던 게 오류였다.
MIN_BASELINE_PRESENCE = 0.4   # baseline 등장일 비율 하한(SPIKE 자격)
NEW_MIN_SOURCES = 2           # NEW 는 최소 2개 매체 — 한 매체 연재물이 신생 테마인 척 하는 걸 막는다

# 시장관련도 하한 — 그 단어의 그날 기사 중 상장사를 언급한 비율(_universe).
# 뉴스 풀의 62%가 종합지라 이게 없으면 폭우·송파구가 반도체를 이긴다(실측).
# 0 이면 전부 통과(순수 발굴 모드) — 자르는 게 아니라 '어느 판을 읽을지' 고르는 손잡이.
MIN_MKT_PCT = 40.0

BODY_CAP = 3000         # 본문 앞 N자만 — 평균 1,662자라 대부분 전문. 꼬리 저작권문구 절약.
EVIDENCE_SNIPPET = 220  # 근거기사에 붙일 본문 앞머리(리드) — 제목만으론 방향을 모른다.


def _norm_entropy(counts: list[int]) -> float:
    """소스 분포의 정규화 엔트로피 0~1. 1=여러 매체에 고르게 퍼짐, 0=한 매체 독점."""
    n = sum(counts)
    if n <= 0 or len(counts) <= 1:
        return 0.0
    h = -sum((c / n) * math.log(c / n) for c in counts if c > 0)
    return h / math.log(len(counts))


def _load(con: sqlite3.Connection, since: str, scope: str, field: str):
    """(market_day, source, title, url_hash, has_listed, text) 스트리밍.

    ⚠⚠ **`field='any'`(본문 포함)는 지금 신뢰할 수 없다 — 기본이 'title' 인 이유.**
    스크래퍼가 사이트 사이드바('많이 본 뉴스' 헤드라인 목록)를 본문에 같이 담고 있다.
    실측 본문 중 보일러플레이트 비율: **asiae 55.6%** · donga 32.2% · sedaily 16.6% ·
    marketwatch 18.7% (mt·hankyung·mk·seekingalpha 는 0% = 깨끗).
    결과: asiae 기사 874건 전부가 같은 사이드바를 공유해 `사랑해`(130σ)·`교도관`·`갑니다`
    같은 유령 급등어가 1등을 먹고, 사이드바에 늘 있는 SK하이닉스(298건)·현대차(182건)
    때문에 시장관련도가 전부 100% 로 붙어 판별력이 죽는다. 증거는 분산 0.00(=1개 매체).
    스크래퍼가 고쳐지면 기본을 'any' 로 되돌려라 — 본문은 제목의 40배 정보량이고,
    본문 보일러플레이트(기자 54%·무단/전재 45%)는 평평해서 z 가 알아서 죽인다.
    """
    rows = con.execute(
        "SELECT s.published_at, s.source, s.title, s.url_hash, a.body "
        "FROM seen_news s LEFT JOIN article_contents a ON a.url_hash = s.url_hash "
        "WHERE s.published_at IS NOT NULL AND s.published_at != '' AND s.title IS NOT NULL "
        "AND s.title != '' AND s.fetched_at >= ?",
        (since,),
    )
    for pub, src, title, uh, body in rows:
        foreign = (src or "") in FOREIGN_SOURCES
        if scope == "foreign" and not foreign:
            continue
        if scope == "domestic" and foreign:
            continue
        d = market_day(pub, src)      # ⚠ fetched_at 아님 — 수집공백이 가짜 스파이크가 된다
        if not d:
            continue
        body = (body or "")[:BODY_CAP]
        # ⚠ 상장사 판정도 **제목만** — 본문으로 넓히면 사이드바의 SK하이닉스(298건)·현대차(182건)에
        # 전부 걸려 시장관련도가 무의미해진다(실측: 나토 11%→67%, 농업 0%→50% 로 오염).
        # 스크래퍼가 고쳐지면 본문까지 넓혀라 — 진짜 이득은 거기 있다(제목만 보면 시장기사를 놓친다).
        has_co = mentions_listed(title, foreign)
        text = title if field == "title" else (title + " " + body)
        yield d, src or "?", title, uh, has_co, text, body


def analyze(target: str, days_back: int, scope: str, min_mkt: float = MIN_MKT_PCT,
            field: str = "title") -> dict:
    """대상일의 급등어 후보표. 판정 없음 — 근거만.

    `min_mkt`=0 이면 순수 발굴(전부). `field`='title'(기본) / 'any'=제목+본문(⚠ `_load` 참조 —
    스크래퍼 사이드바 오염으로 현재 신뢰불가).
    """
    con = sqlite3.connect(f"file:{NEWS_DB}?mode=ro", uri=True)
    # 수집이 늦게 붙는 기사가 있어 넉넉히 읽고 발행일로 다시 자른다.
    since = (datetime.strptime(target, "%Y-%m-%d")
             - timedelta(days=days_back + BASELINE_DAYS + 10)).strftime("%Y-%m-%d")

    day_total: Counter = Counter()
    day_term: defaultdict = defaultdict(Counter)          # day → term → docs
    term_day_src: defaultdict = defaultdict(Counter)      # (day,term) → source → docs
    ev: defaultdict = defaultdict(list)                   # (day,term) → 근거기사
    term_mkt: defaultdict = defaultdict(int)              # (day,term) → 상장사 언급 기사수

    for d, src, title, uh, has_co, text, body in _load(
            con, max(since, PUBLISHED_AT_SINCE), scope, field):
        day_total[d] += 1
        ts = tokens(text)
        for t in ts:
            day_term[d][t] += 1
            term_day_src[(d, t)][src] += 1
            if has_co:
                term_mkt[(d, t)] += 1
        # 근거는 **대상일만** 모은다 — baseline 30일치까지 쌓으면 메모리가 터진다.
        # 리드(본문 앞 220자)는 사이드바 오염 전 구간이라 안전하고, 방향(호재/악재)이 여기 있다.
        if d == target:
            lede = " ".join(body[:EVIDENCE_SNIPPET].split()) or None
            for t in ts:
                if len(ev[(d, t)]) < 3:
                    ev[(d, t)].append({"source": src, "title": title,
                                       "url_hash": uh, "lede": lede})
    con.close()

    base_days = [(datetime.strptime(target, "%Y-%m-%d") - timedelta(days=i)).strftime("%Y-%m-%d")
                 for i in range(1, BASELINE_DAYS + 1)]
    base_days = [d for d in base_days if day_total.get(d, 0) > 0]   # 표본 없는 날 제외
    prev = (datetime.strptime(target, "%Y-%m-%d") - timedelta(days=1)).strftime("%Y-%m-%d")

    tot_t = day_total.get(target, 0)
    n_avg = st.mean([day_total[d] for d in base_days]) if base_days else 0
    out: list[dict] = []
    if tot_t and len(base_days) >= MIN_BASELINE_DAYS:
        for term, cnt in day_term[target].items():
            if cnt < MIN_COUNT:
                continue
            mkt_pct = 100.0 * term_mkt[(target, term)] / cnt
            if mkt_pct < min_mkt:
                continue          # 시장 얘기가 아님 — 폭우·송파구류가 여기서 빠진다
            share = cnt / tot_t
            hist = [day_term[d].get(term, 0) / day_total[d] for d in base_days]
            presence = sum(1 for h in hist if h > 0) / len(hist)
            mean, sd = st.mean(hist), st.pstdev(hist)

            src_counts_pre = list(term_day_src[(target, term)].values())
            if presence < MIN_BASELINE_PRESENCE:
                # 평소를 모르는 단어 — z 를 매기면 거짓말이 된다. 처음 보는 것으로 취급.
                if len(src_counts_pre) < NEW_MIN_SOURCES:
                    continue
                z, kind = None, "NEW"
            else:
                # 관측 sd 가 표본잡음보다 작으면 그건 '안정'이 아니라 표본이 작은 것 —
                # 이항 표본편차를 하한으로 깔아 z 가 부풀지 않게 한다.
                sd_floor = math.sqrt(mean * (1 - mean) / n_avg) if n_avg else 0.0
                sd_eff = max(sd, sd_floor)
                if sd_eff <= 0:
                    continue
                z, kind = (share - mean) / sd_eff, "SPIKE"
                if z < Z_FLOOR:
                    continue

            src_counts = src_counts_pre
            pc = day_term.get(prev, {}).get(term, 0)
            pshare = pc / day_total[prev] if day_total.get(prev) else 0.0
            out.append({
                "term": term, "kind": kind,
                "count": cnt, "denom": tot_t, "share_pct": round(100 * share, 4),
                "z": round(z, 2) if z is not None else None,
                "baseline_mean_pct": round(100 * mean, 4),
                "baseline_presence": round(presence, 2),
                "baseline_days": len(base_days),
                "mkt_pct": round(mkt_pct, 1),
                "src_entropy": round(_norm_entropy(src_counts), 2),
                "n_sources": len(src_counts),
                "persist": bool(pshare > mean) if mean or pshare else False,
                "prev_count": pc,
                "evidence": ev[(target, term)],
            })

    # 두 갈래는 척도가 달라 한 줄로 못 세운다 — SPIKE 는 z 로, NEW 는 건수로.
    spikes = sorted((r for r in out if r["kind"] == "SPIKE"),
                    key=lambda r: r["z"], reverse=True)
    news = sorted((r for r in out if r["kind"] == "NEW"),
                  key=lambda r: (r["count"], r["src_entropy"]), reverse=True)
    return {
        "date": target, "scope": scope, "denom_docs": tot_t,
        "baseline_days_used": len(base_days), "baseline_window": BASELINE_DAYS,
        "params": {"min_count": MIN_COUNT, "z_floor": Z_FLOOR,
                   "min_baseline_days": MIN_BASELINE_DAYS,
                   "min_baseline_presence": MIN_BASELINE_PRESENCE,
                   "new_min_sources": NEW_MIN_SOURCES, "min_mkt_pct": min_mkt,
                   "field": field, "body_cap": BODY_CAP},
        "universe_size": universe_size(scope == "foreign"),
        "spikes": spikes, "new_terms": news,
        "terms": spikes + news,     # 하위호환 — 전체 후보
    }


def run(target: str | None, days_back: int, scope: str, top: int, as_json: bool,
        min_mkt: float = MIN_MKT_PCT, field: str = "title") -> None:
    utf8_stdout()
    if field == "any":
        print("  ⚠ field=any: 본문에 스크래퍼가 사이드바를 섞어놨다(asiae 55.6%·donga 32.2%) — "
              "유령 급등어가 섞인다. 분산(entropy)이 0 에 가까우면 그 사이드바다.")
    target = target or _date.today().strftime("%Y-%m-%d")
    rep = analyze(target, days_back, scope, min_mkt, field)

    if as_json:
        BURST_OUT.mkdir(parents=True, exist_ok=True)
        fp = BURST_OUT / f"{target}_{scope}.json"
        fp.write_text(json.dumps(rep, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps({k: v for k, v in rep.items() if k != "terms"}, ensure_ascii=False, indent=2))
        print(f"\n(후보 {len(rep['terms'])}개 + 근거 → {fp})")
        return

    sc = {"all": "국내+해외", "foreign": "해외만", "domestic": "국내만"}[scope]
    print(f"\n# 급등어 — {rep['date']} [{sc}]  (분모 {rep['denom_docs']:,}건 · "
          f"baseline {rep['baseline_days_used']}일 · 시장관련도≥{min_mkt:.0f}% · "
          f"유니버스 {rep['universe_size']:,}사 · field={field})")
    if not rep["universe_size"] and min_mkt > 0:
        print("  ⚠ 유니버스 비었음 — 시장관련도가 전부 0 이라 후보가 안 나온다(--min-mkt 0 으로 우회).")
    if not rep["denom_docs"]:
        print("  ⚠ 그날 발행 기사 0건 — 판정 불가(빈칸이지 '조용함'이 아님).")
        return
    if rep["baseline_days_used"] < MIN_BASELINE_DAYS:
        print(f"  ⚠ baseline 표본 부족({rep['baseline_days_used']}일 < {MIN_BASELINE_DAYS}) — z 미산출.")
        return
    if not rep["terms"]:
        print("  후보 0개 — 평소와 다른 단어가 없다(조용한 날).")
        return

    print(f"\n  ── ① 평소 있던 단어가 튐 (z 순) — 아는 단어의 온도 ──")
    print(f"  {'단어':<12} {'z':>6} {'건수':>5} {'점유%':>7} {'평소%':>7} {'시장%':>6} {'분산':>5} {'매체':>4} {'지속':>4}")
    print("  " + "─" * 73)
    for r in rep["spikes"][:top]:
        print(f"  {r['term']:<12} {r['z']:>6.1f} {r['count']:>5} {r['share_pct']:>7.3f} "
              f"{r['baseline_mean_pct']:>7.3f} {r['mkt_pct']:>5.0f}% {r['src_entropy']:>5.2f} "
              f"{r['n_sources']:>4} {'○' if r['persist'] else '·':>4}")
    if not rep["spikes"]:
        print("     (없음)")

    print(f"\n  ── ② 평소 없던 단어가 등장 (건수 순) — 모르는 단어의 발굴 ──")
    print(f"  {'단어':<12} {'건수':>6} {'점유%':>7} {'평소등장':>8} {'시장%':>6} {'분산':>5} {'매체':>4}")
    print("  " + "─" * 73)
    for r in rep["new_terms"][:top]:
        print(f"  {r['term']:<12} {r['count']:>6} {r['share_pct']:>7.3f} "
              f"{r['baseline_presence']*100:>7.0f}% {r['mkt_pct']:>5.0f}% {r['src_entropy']:>5.2f} "
              f"{r['n_sources']:>4}")
    if not rep["new_terms"]:
        print("     (없음)")

    print("\n  ①z=자기 평소 대비 σ (평소 40%+ 등장한 단어만 — 그래야 '평소'가 실재)")
    print("  ②평소등장=baseline 30일 중 나온 날 비율. 낮을수록 처음 보는 말.")
    print("  시장%=그 단어 기사 중 상장사를 언급한 비율(뉴스풀 62%가 종합지라 이걸로 판을 고른다)")
    print("  분산=소스 고르기(1=여러매체 확산, 0=한매체 독점=메아리) · 지속=전날에도 평소 이상")
    print("  ⚠ 판정 아님 — 방향(호재/악재)은 근거기사(--json)를 읽어야 안다.")


def cli_register(sub) -> None:
    p = sub.add_parser("burst", help="그날 평소보다 튄 단어 + 근거(고정 검색어 없이)")
    p.add_argument("--date", default=None, help="대상일 YYYY-MM-DD (기본: 오늘)")
    p.add_argument("--days", type=int, default=1, dest="days_back", help="(예약) 대상 구간")
    p.add_argument("--scope", choices=["all", "foreign", "domestic"], default="all")
    p.add_argument("--top", type=int, default=25)
    p.add_argument("--min-mkt", type=float, default=MIN_MKT_PCT, dest="min_mkt",
                   help=f"시장관련도 하한%% (기본 {MIN_MKT_PCT:.0f}; 0=순수발굴, 종합뉴스 전부)")
    p.add_argument("--field", choices=["any", "title"], default="title",
                   help="title=제목만(기본) / any=제목+본문(⚠ 스크래퍼 사이드바 오염 — 유령급등어)")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=lambda a: run(a.date, a.days_back, a.scope, a.top, a.json,
                                      a.min_mkt, a.field))
