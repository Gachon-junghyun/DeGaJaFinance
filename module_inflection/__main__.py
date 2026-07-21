# -*- coding: utf-8 -*-
"""module_inflection CLI.

    python -m module_inflection build --top 200            # 가격+언급+변곡+지문 (파생DB 재생성)
    python -m module_inflection stats --json               # 리드/래그·리프트·순열검정·뉴스유무 분할
    python -m module_inflection events --top 20            # 큰 변곡 목록(제목 근거 포함)
    python -m module_inflection analog --text "원전 수주"   # 과거 유사국면 + 그 후 실제 수익
    python -m module_inflection analog --id 042660|2026-06-12|shock_up

⚠ `analog --text` 만 GPU 모델을 쓴다(질의문 인코딩). 나머지는 CPU·stdlib+pandas.
"""
from __future__ import annotations

import argparse
import json
import sys

import numpy as np
import pandas as pd

from . import _analog, _detect, _lexicon, _newslink, _prices, _stats
from ._config import NEWS_LAG_AFTER, NEWS_LAG_BEFORE, NEWS_START, utf8_stdout


def _p(obj, as_json: bool) -> None:
    if as_json:
        print(json.dumps(obj, ensure_ascii=False, indent=2, default=str))
    else:
        print(obj)


def cmd_build(args) -> int:
    con = _prices.connect()
    _newslink.ensure_schema(con)
    _analog.ensure_schema(con)

    uni = _prices.load_universe(args.top)
    _prices.save_universe(con, uni)
    print(f"[1/5] 유니버스 {len(uni)}종목 (KOSPI 시총순)")

    if not args.skip_px:
        close = _prices.fetch_panel([u["ticker"] for u in uni], period=args.period)
        n = _prices.store_panel(con, close)
        print(f"[2/5] 가격 {n:,}행 · {close.shape[1]}종목 × {close.shape[0]}일")
    else:
        print("[2/5] 가격 재사용(--skip-px)")

    st = _newslink.build_mentions(con, uni, since=NEWS_START)
    print(f"[3/5] 제목 {st['articles_scanned']:,}건 스캔 → "
          f"언급 {st['links']:,}건 · {st['tickers_with_any']}/{st['names']}종목")

    panel = _prices.read_panel(con)
    meta = {u["ticker"]: u for u in uni}
    events: list[dict] = []
    for tic in panel.columns:
        for e in _detect.detect_ticker(tic, panel[tic], args.shock_z, args.pivot_z):
            d = e.as_dict()
            d["name"] = meta.get(tic, {}).get("name")
            d["sector"] = meta.get(tic, {}).get("sector")
            events.append(d)
    events = [e for e in events if e["date"] >= NEWS_START]   # 뉴스축이 없는 구간은 제외
    print(f"[4/5] 변곡 {len(events):,}건 (뉴스축 구간 {NEWS_START}~)")

    mean = _analog.corpus_mean()
    _analog.save_mean(con, mean)
    con.execute("DELETE FROM events")
    with_news = 0
    for e in events:
        arts = _newslink.articles_around(con, e["ticker"], e["date"],
                                         NEWS_LAG_BEFORE, NEWS_LAG_AFTER)
        vec = _analog.fingerprint(
            _analog.fetch_vectors([a["url_hash"] for a in arts]), mean)
        if vec is not None:
            with_news += 1
        _analog.store_event(con, e, [{"d": a["day"], "s": a["source"], "t": a["title"],
                                      "u": a["url"]} for a in arts], vec)
    con.commit()
    print(f"[5/5] 이벤트 저장 {len(events):,} · 그중 제목근거 있는 것 {with_news:,} "
          f"({with_news / max(1, len(events)):.1%})")
    return 0


def _frames(con):
    panel = _prices.read_panel(con)
    days = list(panel.index)
    retz = pd.DataFrame({t: _detect.z_series(panel[t]) for t in panel.columns})
    ment = _newslink.mention_frame(con, sorted(set(
        pd.date_range(NEWS_START, days[-1]).strftime("%Y-%m-%d"))))
    folded = _stats.fold_to_trading_days(ment, [d for d in days if d >= NEWS_START])
    newsz = _newslink.mention_z(folded)
    retz = retz.reindex(folded.index)
    common = [c for c in retz.columns if c in newsz.columns]
    return retz[common], newsz[common]


def cmd_stats(args) -> int:
    con = _prices.connect()
    retz, newsz = _frames(con)
    events = [dict(zip([c[0] for c in con.execute("SELECT * FROM events LIMIT 1").description], r))
              for r in con.execute("SELECT * FROM events")]

    nz = {(t, d): v for t in newsz.columns
          for d, v in newsz[t].items() if np.isfinite(v)}

    def lookup(tic, date):
        return nz.get((tic, date))

    panel = _prices.read_panel(con, since=NEWS_START)
    base = _stats.baseline_forward(panel.pct_change(fill_method=None))
    out = {
        "window": {"first_day": str(retz.index[0]), "last_day": str(retz.index[-1]),
                   "tickers": int(retz.shape[1]), "trading_days": int(retz.shape[0])},
        "baseline": base,
        "lead_lag": _stats.lead_lag(retz, newsz),
        "lift": _stats.lift_table(retz, newsz),
        "permutation_per_ticker": _stats.permutation_null(retz, newsz, iters=args.iters,
                                                          mode="per_ticker"),
        "permutation_common": _stats.permutation_null(retz, newsz, iters=args.iters,
                                                      mode="common"),
        "events_by_kind": {k: int(v) for k, v in
                           pd.Series([e["kind"] for e in events]).value_counts().items()},
        "day_clustered": _stats.day_clustered(events),
        "news_split": _stats.split_by_news(events, lookup, thr=args.news_thr, baseline=base),
    }
    if args.json:
        _p(out, True)
    else:
        w = out["window"]
        print(f"창: {w['first_day']} ~ {w['last_day']} · {w['tickers']}종목 × {w['trading_days']}거래일\n")
        print("── 무조건부 기준선(아무 종목·아무 날) — 조건부 수익은 이것과의 차이로만 읽는다")
        for k, v in out["baseline"].items():
            print(f"  {k}: 평균 {v['mean_pct']:+.2f}% 중앙 {v['median_pct']:+.2f}% "
                  f"승률 {v['win_rate']:.0%} (n={v['n']:,})")
        print()
        print("── 리드/래그 상관  corr(뉴스z[t+k], |수익z[t]|)")
        for r in out["lead_lag"]:
            bar = "█" * max(0, int(round(r["corr"] * 200))) if r["corr"] == r["corr"] else ""
            print(f"  k={r['lag']:+d} ({r['meaning']:>6})  {r['corr']:+.4f}  n={r['n']:,}  {bar}")
        print("\n── 리프트")
        for k, v in out["lift"].items():
            print(f"  {k}: {v}")
        print("\n── 순열검정(뉴스계열 순환이동) — 귀무 두 개")
        for tag, label in (("permutation_per_ticker", "종목마다 다른 이동(시장 동시성까지 깬다 — 느슨)"),
                           ("permutation_common", "전 종목 같은 이동(시장 구조 보존 — 엄격)")):
            v = out[tag]
            print(f"  [{label}]")
            print(f"    관측 {v['observed_corr']:+.4f} · 귀무 {v['null_mean']:+.4f}±{v['null_sd']:.4f} "
                  f"· p={v['p_two_sided']:.4f} ({v['iters']}회)")
        print("\n── 변곡 종류")
        for k, v in out["events_by_kind"].items():
            print(f"  {k}: {v}")
        print("\n── 날짜로 묶은 이후 5일 수익 (★기본 보고 단위 — 변곡은 종목별 독립사건이 아니다)")
        print(f"  {'종류':<12}{'건':>5}{'날':>5}{'최대날비중':>10}{'pooled':>9}{'날평균':>9}{'SE':>7}{'t':>7}")
        for k, v in out["day_clustered"].items():
            print(f"  {k:<12}{v['n_events']:>5}{v['n_days']:>5}{v['largest_day_share']:>10.0%}"
                  f"{v['pooled_mean_pct']:>+9.2f}{v['day_mean_pct']:>+9.2f}"
                  f"{v['day_se_pp']:>7.2f}{v['day_t']:>+7.2f}")
        print("  → pooled 와 '날평균'이 크게 벌어지면 그 결과는 **소수의 시장 사건**이 만든 것이다.")
        print("\n── 뉴스 동반 여부별 이후 수익")
        print("  ⚠ pivot_* 의 fwd5/fwd20 은 **정의상 순환논리**다(변곡 판정이 미래 10일을 쓴다).")
        print("     비순환 결과는 shock_* 행뿐 — pivot 행은 '얼마나 큰 전환이었나'의 기술통계로만 읽는다.")
        for kind, row in out["news_split"].items():
            print(f"  [{kind}]")
            for tag, s in row.items():
                if not s.get("n"):
                    print(f"    {tag}: 표본 0")
                    continue
                ex5 = s.get("fwd5_excess_pp")
                ex20 = s.get("fwd20_excess_pp")
                print(f"    {tag:>7}: n={s['n']:<4} fwd5 {s['fwd5_mean_pct']:+.2f}% "
                      f"(초과 {ex5:+.2f}pp) 승률 {s['fwd5_win_rate']:.0%} | "
                      f"fwd20 {s['fwd20_mean_pct'] if s['fwd20_mean_pct'] is not None else float('nan'):+.2f}% "
                      f"(초과 {ex20 if ex20 is not None else float('nan'):+.2f}pp, n={s['n20']})")
    return 0


def cmd_events(args) -> int:
    con = _prices.connect()
    q = "SELECT id,ticker,name,sector,date,kind,z,fwd5,fwd20,n_arts,titles FROM events"
    params: list = []
    where = []
    if args.ticker:
        where.append("ticker=?"); params.append(args.ticker)
    if args.kind:
        where.append("kind=?"); params.append(args.kind)
    if args.min_arts:
        where.append("n_arts>=?"); params.append(args.min_arts)
    if where:
        q += " WHERE " + " AND ".join(where)
    q += " ORDER BY ABS(z) DESC LIMIT ?"
    params.append(args.top)
    rows = con.execute(q, params).fetchall()
    out = []
    for r in rows:
        titles = json.loads(r[10] or "[]")
        out.append({"id": r[0], "ticker": r[1], "name": r[2], "sector": r[3],
                    "date": r[4], "kind": r[5], "z": r[6], "fwd5": r[7],
                    "fwd20": r[8], "n_arts": r[9],
                    "titles": [f"{t['d']} [{t['s']}] {t['t']}" for t in titles[:args.n_titles]]})
    if args.json:
        _p(out, True)
        return 0
    for o in out:
        f5 = f"{o['fwd5']*100:+.1f}%" if o["fwd5"] is not None else "—"
        print(f"\n{o['date']} {o['name']}({o['ticker']}) {o['kind']} z={o['z']:+.2f} "
              f"→ 5일 {f5} · 기사 {o['n_arts']}건 [{o['sector']}]")
        for t in o["titles"]:
            print(f"    · {t}")
    return 0


def cmd_phrases(args) -> int:
    con = _prices.connect()
    panel = _prices.read_panel(con, since=NEWS_START)
    base = _stats.baseline_forward(panel.pct_change(fill_method=None))
    rows = _lexicon.phrase_table(con, panel, base, min_n=args.min_n)
    if args.json:
        _p({"baseline": base, "rows": rows}, True)
        return 0
    print(f"기준선(무조건부): 5일 {base['fwd5']['mean_pct']:+.2f}% · "
          f"20일 {base['fwd20']['mean_pct']:+.2f}%  ← 아래는 이걸 뺀 초과\n")
    print(f"{'유형':<14}{'n':>6}{'1일':>8}{'5일초과':>9}{'±2SE':>8}{'유의':>5}{'승률':>7}{'20일초과':>10}{'n20':>6}")
    for r in rows:
        f1 = f"{r['fwd1_pct']:+.2f}" if r["fwd1_pct"] is not None else "—"
        e20 = f"{r['fwd20_excess_pp']:+.2f}" if r["fwd20_excess_pp"] is not None else "—"
        se2 = 2 * r["fwd5_se_pp"]
        sig = "◯" if abs(r["fwd5_excess_pp"]) > se2 else "·"
        print(f"{r['kind']:<14}{r['n']:>6}{f1:>8}{r['fwd5_excess_pp']:>+9.2f}"
              f"{se2:>8.2f}{sig:>5}{r['fwd5_win']:>7.0%}{e20:>10}{r['n20']:>6}")
    print("\n◯ = |초과| > 2SE (독립가정 하한선; 같은 날 종목들이 함께 움직이므로 실제 불확실성은 더 크다)")
    return 0


def cmd_analog(args) -> int:
    con = _prices.connect()
    mean = _analog.load_mean(con)
    if mean is None:
        print("먼저 `build` 를 돌려라(코퍼스 평균 없음).", file=sys.stderr)
        return 2
    if args.id:
        row = con.execute("SELECT vec,date FROM events WHERE id=?", (args.id,)).fetchone()
        if not row or row[0] is None:
            print("그 이벤트에 지문이 없다(제목 근거 0건).", file=sys.stderr)
            return 2
        qv = np.frombuffer(row[0], dtype=np.float32)
        before = args.before or row[1]
        exclude = args.id.split("|")[0]
    elif args.text:
        qv = _analog.encode_query(args.text, mean)
        before, exclude = args.before, None
    else:
        print("--text 또는 --id 중 하나가 필요하다.", file=sys.stderr)
        return 2
    res = _analog.search(con, qv, k=args.k, exclude_ticker=exclude, before=before)
    if args.json:
        _p(res, True)
        return 0
    if "error" in res:
        print(res["error"]); return 2
    s = res["summary"]
    print(f"전례 {s['k']}건 · 이후 5일 평균 {s['fwd5_mean_pct']}% "
          f"중앙 {s['fwd5_median_pct']}% 승률 {s['fwd5_win_rate']} (n={s['n_fwd5']}) "
          f"| 20일 평균 {s['fwd20_mean_pct']}% (n={s['n_fwd20']})\n")
    for h in res["hits"]:
        f5 = f"{h['fwd5']*100:+.1f}%" if h["fwd5"] is not None else "—"
        print(f"[{h['sim']:.3f}] {h['date']} {h['name']}({h['ticker']}) {h['kind']} "
              f"z={h['z']:+.2f} → 5일 {f5}")
        for t in h["titles"][:3]:
            print(f"      · {t['t']}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(prog="module_inflection",
                                 description="가격 변곡점 ↔ 뉴스 정렬 연구실")
    sub = ap.add_subparsers(dest="cmd", required=True)

    b = sub.add_parser("build", help="파생 DB 재생성(가격·언급·변곡·지문)")
    b.add_argument("--top", type=int, default=200)
    b.add_argument("--period", default="1y")
    b.add_argument("--shock-z", type=float, default=2.0)
    b.add_argument("--pivot-z", type=float, default=2.0)
    b.add_argument("--skip-px", action="store_true", help="가격 재다운로드 생략")
    b.set_defaults(fn=cmd_build)

    s = sub.add_parser("stats", help="정량검증(리드래그·리프트·순열·뉴스분할)")
    s.add_argument("--json", action="store_true")
    s.add_argument("--iters", type=int, default=200)
    s.add_argument("--news-thr", type=float, default=1.5)
    s.set_defaults(fn=cmd_stats)

    e = sub.add_parser("events", help="변곡 목록 + 제목 근거")
    e.add_argument("--top", type=int, default=20)
    e.add_argument("--ticker")
    e.add_argument("--kind")
    e.add_argument("--min-arts", type=int, default=0)
    e.add_argument("--n-titles", type=int, default=6)
    e.add_argument("--json", action="store_true")
    e.set_defaults(fn=cmd_events)

    ph = sub.add_parser("phrases", help="말의 종류별 이후 초과수익 표")
    ph.add_argument("--min-n", type=int, default=25)
    ph.add_argument("--json", action="store_true")
    ph.set_defaults(fn=cmd_phrases)

    a = sub.add_parser("analog", help="과거 유사국면 검색")
    a.add_argument("--text")
    a.add_argument("--id")
    a.add_argument("--k", type=int, default=10)
    a.add_argument("--before", help="이 날짜 이전 전례만(컨닝 방지)")
    a.add_argument("--json", action="store_true")
    a.set_defaults(fn=cmd_analog)
    return ap


def main(argv=None) -> int:
    utf8_stdout()
    args = build_parser().parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    raise SystemExit(main())
