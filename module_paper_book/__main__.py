# -*- coding: utf-8 -*-
"""module_paper_book CLI — 모의투자 장부 서브커맨드.

기본 드라이런: fill 은 `--commit` 없으면 장부를 바꾸지 않고 미리보기만 한다.
"""
from __future__ import annotations

import argparse
from pathlib import Path

from ._book import Fill, book_summary, connect, get_positions, init_db, record_fill, snapshot_equity
from ._config import DEFAULT_CAPITAL_KRW, DEFAULT_CAPITAL_USD, DEFAULT_FX_USDKRW, utf8_stdout
from ._intake import read_actionable, summarize
from ._journal import log_decision, recent, track_record
from ._mark import mark_book, position_pnl
from ._risk import RiskParams, concentration_check, size_position, theme_exposure


def _equity_krw(conn, fx: float) -> float:
    s = book_summary(conn)
    marks = mark_book(conn)
    inv = unreal = 0.0
    for p in get_positions(conn, open_only=True):
        px = marks.get(p.ticker) or p.avg_cost
        rate = 1.0 if p.currency == "KRW" else fx
        inv += p.cost_basis * rate
        unreal += (px - p.avg_cost) * p.qty * rate
    return s["cash_krw"] + s["cash_usd"] * fx + inv + unreal


def cmd_init(a):
    with connect(a.db) as conn:
        init_db(conn, capital_krw=a.capital_krw, capital_usd=a.capital_usd, reset=a.reset)
        s = book_summary(conn)
    print(f"✅ 장부 초기화 — KRW {s['cash_krw']:,.0f} · USD {s['cash_usd']:,.0f}"
          f"{' (reset)' if a.reset else ''}")


def cmd_intake(a):
    rd = Path(a.dir) if a.dir else None
    cands = read_actionable(rd)
    summ = summarize(cands)
    print(f"# INTAKE — 실행가능 후보 {summ['n']}건  (source: {a.dir or 'REPORT/'})")
    print(f"  프레시니스: {summ['by_freshness']}")
    print(f"  🟢LIVE: {', '.join(summ['live']) or '—'}")
    print(f"  🔴RESOLVED(드롭): {', '.join(summ['resolved_drop']) or '—'}")
    print(f"  ★코어(epicenter): {', '.join(summ['core']) or '—'}")
    print(f"\n{'TICKER':7s} {'MKT':4s} {'FRESH':9s} {'STOP':>9s} {'CORE':5s} THEME / SOURCE")
    print("  " + "─" * 78)
    order = {"LIVE": 0, "PARTIAL": 1, "RESOLVED": 2}
    for c in sorted(cands, key=lambda c: (order.get(c.freshness, 3), c.ticker)):
        stop = f"{c.stop:.2f}" if c.stop else "—"
        print(f"{c.ticker:7s} {c.market:4s} {c.freshness:9s} {stop:>9s} "
              f"{'★' if c.is_core else ' ':5s} {c.theme[:18]:18s} {c.source_report}")


def cmd_status(a):
    with connect(a.db) as conn:
        s = book_summary(conn)
        marks = mark_book(conn)
        eq = _equity_krw(conn, a.fx)
        print(f"# BOOK STATUS  (fx {a.fx:.0f})")
        print(f"  현금  KRW {s['cash_krw']:,.0f} · USD {s['cash_usd']:,.0f}")
        print(f"  실현손익 누계(현지): {s['realized_pnl_native_sum']:,.2f}")
        print(f"  ★ 총자산(원화환산): {eq:,.0f} KRW")
        print(f"\n{'TICKER':7s} {'QTY':>8s} {'AVG':>10s} {'PRICE':>10s} {'UNREAL%':>8s} {'STOP%':>7s}  THEME")
        print("  " + "─" * 74)
        for p in s["positions"]:
            pl = position_pnl(p, marks.get(p.ticker))
            up = f"{pl['unrealized_pct']:+.1f}" if pl["unrealized_pct"] is not None else "—"
            sd = f"{pl['stop_dist_pct']:+.1f}" if pl["stop_dist_pct"] is not None else "—"
            px = f"{pl['price']:.2f}" if pl["price"] is not None else "n/a"
            flag = " ⛔STOP" if pl.get("stop_hit") else ""
            print(f"{p.ticker:7s} {p.qty:>8.0f} {p.avg_cost:>10.2f} {px:>10s} {up:>8s} {sd:>7s}  {(p.theme or '')[:14]}{flag}")


def cmd_size(a):
    with connect(a.db) as conn:
        eq = a.equity if a.equity else _equity_krw(conn, a.fx)
    # US 종목은 원화 equity 를 USD 로 환산해 사이징(현지통화 일관성)
    from ._config import ccy_of
    eq_native = eq / a.fx if ccy_of(a.ticker) == "USD" else eq
    r = size_position(eq_native, a.price, stop=a.stop, is_core=a.core, params=RiskParams())
    print(f"# SIZE {a.ticker.upper()}  (equity_native≈{eq_native:,.0f} {ccy_of(a.ticker)})")
    for k, v in r.items():
        print(f"  {k:20s}: {v}")


def cmd_fill(a):
    with connect(a.db) as conn:
        f = Fill(ticker=a.ticker, side=a.side, qty=a.qty, price=a.price, fees=a.fees,
                 stop=a.stop, theme=a.theme or "", rationale=a.rationale or "",
                 source_report=a.source or "", name=a.name)
        if not a.commit:
            notional = a.qty * a.price
            print(f"[DRY-RUN] {a.side.upper()} {a.ticker.upper()} {a.qty} @ {a.price} "
                  f"= {notional:,.2f} — 반영하려면 --commit")
            log_decision(conn, a.ticker, a.side.upper(), a.rationale or "(dry-run)",
                         source_report=a.source or "", committed=False)
            return
        res = record_fill(conn, f)
        log_decision(conn, a.ticker, a.side.upper(), a.rationale or "",
                     source_report=a.source or "", committed=True)
        print(f"✅ COMMIT {res['side'].upper()} {res['ticker']} {res['qty']} @ {res['price']} "
              f"{res['currency']} · 실현손익 {res['realized_pnl']:,.2f} · 현금 {res['cash_after']:,.2f}")


def cmd_mark(a):
    with connect(a.db) as conn:
        positions = get_positions(conn, open_only=True)
        marks = mark_book(conn)
        eq = _equity_krw(conn, a.fx)
        flags = concentration_check(positions, marks, eq, a.fx)
        snap = snapshot_equity(conn, marks, a.fx, note=a.note or "mark")
        print(f"# MARK  총자산 {snap['equity_krw']:,.0f} KRW (미실현 {snap['unrealized_krw']:,.0f})")
        hits = [p.ticker for p in positions if (position_pnl(p, marks.get(p.ticker)).get("stop_hit"))]
        print(f"  ⛔ 스탑히트: {', '.join(hits) or '없음'}")
        print(f"  테마노출(원화): " + " · ".join(f"{k}:{v:,.0f}" for k, v in theme_exposure(positions, marks, a.fx).items()))
        if flags:
            for fl in flags:
                print(f"  ⚠ 집중도 초과 [{fl['kind']}] {fl['key']} {fl['pct']}% > {fl['limit']}%")
        else:
            print("  ✅ 집중도 한도 내")


def cmd_snapshot(a):
    with connect(a.db) as conn:
        marks = mark_book(conn)
        snap = snapshot_equity(conn, marks, a.fx, note=a.note or "")
        print(f"📸 스냅샷 — 총자산 {snap['equity_krw']:,.0f} KRW @ {snap['ts']}")


def cmd_pulse(a):
    """라이브 진단 — '지금 나락인가'. 책 전 종목 현재가+당일등락 + 시장맥락 + 스탑근접."""
    from ._mark import price_move, position_pnl
    with connect(a.db) as conn:
        positions = get_positions(conn, open_only=True)
    # 시장 맥락
    print("# LIVE PULSE  (오늘 뭔일? — 당일 데이터)")
    print("  시장맥락:", end=" ")
    ctx = []
    for tk, lab in [("SPY", "S&P500"), ("QQQ", "Nasdaq"), ("^VIX", "VIX")]:
        m = price_move(tk)
        if m["price"] is not None:
            ctx.append(f"{lab} {m['price']:.1f}({m['chg_1d']:+.1f}%)")
    print(" · ".join(ctx))
    print(f"\n{'TKR':7s} {'price':>9} {'1d%':>7} {'5d%':>7} {'stop%':>7} {'테마':<16}")
    print("  " + "─" * 62)
    worst = []
    for p in positions:
        mv = price_move(p.ticker)
        pl = position_pnl(p, mv["price"])
        d1 = f"{mv['chg_1d']:+.1f}" if mv["chg_1d"] is not None else "—"
        d5 = f"{mv['chg_5d']:+.1f}" if mv["chg_5d"] is not None else "—"
        sd = f"{pl['stop_dist_pct']:+.1f}" if pl.get("stop_dist_pct") is not None else "—"
        flag = " ⛔" if pl.get("stop_hit") else ""
        px = f"{mv['price']:.2f}" if mv["price"] is not None else "n/a"
        print(f"{p.ticker:7s} {px:>9s} {d1:>7s} {d5:>7s} {sd:>7s} {(p.theme or '')[:16]:<16}{flag}")
        if mv["chg_1d"] is not None:
            worst.append((mv["chg_1d"], p.ticker))
    worst.sort()
    if worst:
        big = [f"{t} {c:+.1f}%" for c, t in worst if c <= -3]
        print(f"\n  ⚠ 당일 −3%↓: {', '.join(big) if big else '없음 (책 기준 나락 아님)'}")
    print("  → 촉매 확인: python -X utf8 -m module_news_data fts search <종목/테마> --scope foreign --days 1 --snippet")


def cmd_mirror(a):
    import json
    from ._book import init_db
    from ._mirror import MirrorPosition, apply_mirror
    d = json.loads(Path(a.from_json).read_text(encoding="utf-8"))
    poss = [MirrorPosition(ticker=p["ticker"], qty=p["qty"], avg_cost=p["avg_cost"],
                           name=p.get("name"), theme=p.get("theme"), stop=p.get("stop"),
                           source=p.get("source", "KIS-mirror")) for p in d.get("positions", [])]
    with connect(a.db) as conn:
        init_db(conn)  # 스키마 보장(자본은 건드리지 않음)
        res = apply_mirror(conn, poss, cash_krw=d.get("cash_krw"), cash_usd=d.get("cash_usd"),
                           reset_positions=not a.no_reset, note=d.get("note", "KIS mirror"))
        marks = mark_book(conn)
        snap = snapshot_equity(conn, marks, a.fx, note="mirror")
    print(f"🪞 미러링 완료 — 보유 {res['mirrored']}건 시드 · 현금 KRW {res['cash_krw']:,.0f} / USD {res.get('cash_usd') or 0:,.0f}")
    print(f"   총자산(원화환산 @fx{a.fx:.0f}): {snap['equity_krw']:,.0f} KRW")


def cmd_stage(a):
    import json
    from ._mirror import stage_to_kis
    intents = json.loads(Path(a.from_json).read_text(encoding="utf-8"))
    res = stage_to_kis(intents, clear_first=a.clear)
    if not res.get("ok"):
        print(f"❌ {res.get('error')}"); return
    print(f"📥 KIS 주문 스택에 {res['staged']}건 적재 (총 {res['total_in_stack']}건) → {res['path']}")
    print("   ⚠ 계획(intent)만 저장 — 데스크에서 사람이 [체결]로 하나씩 발사(자동 아님).")


def cmd_journal(a):
    with connect(a.db) as conn:
        for r in recent(conn, a.limit):
            c = "✓" if r["committed"] else "·"
            print(f"  {c} {r['ts'][:19]} {r['action']:6s} {r['ticker'] or '':7s} {r['rationale'][:70]}")


def cmd_track(a):
    with connect(a.db) as conn:
        tr = track_record(conn)
    print("# TRACK RECORD")
    for k, v in tr.items():
        print(f"  {k:18s}: {v}")


def main():
    utf8_stdout()
    ap = argparse.ArgumentParser(prog="module_paper_book", description="모의투자 장부 엔진")
    ap.add_argument("--db", default=None, help="장부 DB 경로(기본 data/paper_book.db)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("init"); p.add_argument("--capital-krw", type=float, default=DEFAULT_CAPITAL_KRW)
    p.add_argument("--capital-usd", type=float, default=DEFAULT_CAPITAL_USD)
    p.add_argument("--reset", action="store_true"); p.set_defaults(fn=cmd_init)

    p = sub.add_parser("intake"); p.add_argument("--dir", default=None); p.set_defaults(fn=cmd_intake)

    p = sub.add_parser("status"); p.add_argument("--fx", type=float, default=DEFAULT_FX_USDKRW)
    p.set_defaults(fn=cmd_status)

    p = sub.add_parser("size"); p.add_argument("ticker"); p.add_argument("--price", type=float, required=True)
    p.add_argument("--stop", type=float, default=None); p.add_argument("--core", action="store_true")
    p.add_argument("--equity", type=float, default=None); p.add_argument("--fx", type=float, default=DEFAULT_FX_USDKRW)
    p.set_defaults(fn=cmd_size)

    p = sub.add_parser("fill"); p.add_argument("--ticker", required=True)
    p.add_argument("--side", required=True, choices=["buy", "sell"]); p.add_argument("--qty", type=float, required=True)
    p.add_argument("--price", type=float, required=True); p.add_argument("--fees", type=float, default=0.0)
    p.add_argument("--stop", type=float, default=None); p.add_argument("--theme", default="")
    p.add_argument("--rationale", default=""); p.add_argument("--source", default=""); p.add_argument("--name", default=None)
    p.add_argument("--commit", action="store_true"); p.set_defaults(fn=cmd_fill)

    p = sub.add_parser("mark"); p.add_argument("--fx", type=float, default=DEFAULT_FX_USDKRW)
    p.add_argument("--note", default=""); p.set_defaults(fn=cmd_mark)

    p = sub.add_parser("snapshot"); p.add_argument("--fx", type=float, default=DEFAULT_FX_USDKRW)
    p.add_argument("--note", default=""); p.set_defaults(fn=cmd_snapshot)

    p = sub.add_parser("pulse"); p.set_defaults(fn=cmd_pulse)

    p = sub.add_parser("mirror"); p.add_argument("--from-json", required=True, dest="from_json")
    p.add_argument("--fx", type=float, default=DEFAULT_FX_USDKRW); p.add_argument("--no-reset", action="store_true")
    p.set_defaults(fn=cmd_mirror)

    p = sub.add_parser("stage"); p.add_argument("--from-json", required=True, dest="from_json")
    p.add_argument("--clear", action="store_true"); p.set_defaults(fn=cmd_stage)

    p = sub.add_parser("journal"); p.add_argument("--limit", type=int, default=30); p.set_defaults(fn=cmd_journal)
    p = sub.add_parser("track"); p.set_defaults(fn=cmd_track)

    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
