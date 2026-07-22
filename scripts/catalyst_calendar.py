# FILE: research_Mvp/scripts/catalyst_calendar.py
"""
CATALYST_CALENDAR — deterministic feed of known binary catalysts (macro + earnings) in the next N days.

The 오답노트 finding (2026-07-14): the desk one-way-tilted into "inflation-hot" and got caught when
cool CPI ripped semis; and it dropped GS right before a bank-earnings blowout. Both were KNOWN dated
binaries the desk simply didn't put in front of itself. This script injects them at run-start so the
desk can't NOT see "PPI in 18h" / "TSM prints Thu / bank cluster this week", forcing STAGE 025's
both-sides bracket instead of a one-way tilt.

Macro:    data_build/catalysts/econ_schedule.json  (human-maintained; BLS/Fed publish ~1yr ahead)
Earnings: yfinance next earnings date per a watchlist (candidates ∪ blind-spot names).
Writes:   llm_outputs/{date}/CATALYST_WATCH.json  + prints a table.

Usage: python -X utf8 scripts/catalyst_calendar.py [--days 5] [--date YYYY-MM-DD] \
         [--tickers NVDA,TSM,...]  (default watchlist below)
Analytical/scheduling artifact only.
"""
from __future__ import annotations
import argparse, json, datetime as _dt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHED = ROOT / "data" / "catalysts" / "econ_schedule.json"
STRUCT = ROOT / "data" / "catalysts" / "structural_schedule.json"

# default watchlist = our book + BET candidates + blind-spot legs (TSM/ASML/NFLX/SCHW/MS…)
DEFAULT_TICKERS = ["NVDA", "TSM", "ASML", "AMD", "MU", "META", "AVGO", "ANET",
                   "MS", "SCHW", "BLK", "NFLX", "TSLA",
                   "PSX", "MPC", "VLO", "FRO", "STNG", "RTX", "LMT",
                   "CEG", "VST", "LNG", "KMI", "MA"]


def _days_until(d: str, today: _dt.date) -> int:
    return (_dt.date.fromisoformat(d) - today).days


def macro_events(today: _dt.date, horizon: int) -> list[dict]:
    sched = json.loads(SCHED.read_text(encoding="utf-8"))
    out = []
    for e in sched.get("events", []):
        du = _days_until(e["date"], today)
        if 0 <= du <= horizon:
            out.append({**e, "days_until": du, "kind": "macro"})
    # undated geopolitical triggers always surfaced
    for g in sched.get("geopolitical_watch", []):
        out.append({**g, "days_until": None, "kind": "geopolitical"})
    return sorted(out, key=lambda x: (x["days_until"] is None, x["days_until"] if x["days_until"] is not None else 0))


def _nth_weekday(y: int, m: int, weekday: int, n: int) -> _dt.date:
    """그 달의 n번째 특정요일 (weekday: 월0…일6)."""
    d = _dt.date(y, m, 1)
    d += _dt.timedelta(days=(weekday - d.weekday()) % 7)
    return d + _dt.timedelta(weeks=n - 1)


def _last_business_day(y: int, m: int) -> _dt.date:
    d = _dt.date(y + (m == 12), (m % 12) + 1, 1) - _dt.timedelta(days=1)
    while d.weekday() >= 5:                      # 토/일이면 앞으로 당김
        d -= _dt.timedelta(days=1)
    return d


def structural_events(today: _dt.date, horizon: int) -> list[dict]:
    """구조적/기업행위 캘린더 — 락업·블록딜·지수리밸런스·전환 등.

    econ_schedule 이 거시 발표만 담아 데스크가 KR 최대 바이너리를 2런 연속 놓쳤다(자기 로그).
    이 축은 **날짜가 미리 알려진다**는 점에서 가장 싼 촉매다.
    수기 이벤트 + 규칙기반 리밸런스 날짜(계산)를 합쳐서 낸다.
    """
    if not STRUCT.exists():
        return []
    sched = json.loads(STRUCT.read_text(encoding="utf-8"))
    out: list[dict] = []

    for e in sched.get("events", []):
        du = _days_until(e["date"], today)
        if 0 <= du <= horizon:
            out.append({**e, "days_until": du, "kind": "structural"})

    # 규칙기반 리밸런스 — 이번 달과 다음 달만 계산해 창 안에 드는 것만 남긴다
    rules = {k: v for k, v in sched.get("rebalance_rules", {}).items() if not k.startswith("_")}
    for name, spec in rules.items():
        for off in (0, 1):
            y, m = divmod((today.year * 12 + today.month - 1) + off, 12)
            m += 1
            if m not in spec.get("months", []):
                continue
            r = spec.get("rule")
            if r == "last_business_day":
                d = _last_business_day(y, m)
            elif r == "third_friday":
                d = _nth_weekday(y, m, 4, 3)
            elif r == "second_thursday":
                d = _nth_weekday(y, m, 3, 2)
            else:
                continue
            du = (d - today).days
            if 0 <= du <= horizon:
                out.append({"date": d.isoformat(), "event": name.replace("_", " "),
                            "ticker": None, "axis": "rebalance", "binary": False,
                            "source": "derived", "confidence": "pattern",
                            "note": spec.get("note", ""), "days_until": du, "kind": "structural"})
    return sorted(out, key=lambda x: x["days_until"])


def earnings_events(tickers: list[str], today: _dt.date, horizon: int) -> list[dict]:
    try:
        import yfinance as yf
    except Exception:
        return []
    out = []
    for t in tickers:
        nd = None
        try:
            edf = yf.Ticker(t).get_earnings_dates(limit=8)
            if edf is not None and len(edf):
                fut = [d for d in edf.index if d.date() >= today]
                if fut:
                    nd = min(fut).date()
        except Exception:
            pass
        if nd is None:
            try:  # fallback to .calendar
                cal = yf.Ticker(t).calendar
                ed = cal.get("Earnings Date") if isinstance(cal, dict) else None
                if ed:
                    nd = (ed[0] if isinstance(ed, (list, tuple)) else ed)
                    nd = nd.date() if hasattr(nd, "date") else _dt.date.fromisoformat(str(nd)[:10])
            except Exception:
                pass
        if nd is not None:
            du = (nd - today).days
            if 0 <= du <= horizon:
                out.append({"date": nd.isoformat(), "event": f"{t} earnings", "ticker": t,
                            "axis": "earnings", "binary": True, "days_until": du, "kind": "earnings"})
    return sorted(out, key=lambda x: x["days_until"])


def render(macro: list[dict], earn: list[dict], today: _dt.date, horizon: int,
           struct: list[dict] | None = None) -> str:
    L = [f"CATALYST_WATCH — as of {today} — next {horizon} trading-ish days", "=" * 64]
    struct = struct or []
    binaries = [e for e in macro + earn + struct if e.get("binary")]
    L.append(f"⚠️ {len(binaries)} BINARY catalyst(s) in window — STAGE 025 both-sides bracket REQUIRED for each.\n")
    L.append("[MACRO]  (✓=official source confirmed · ~=pattern/estimate, verify)")
    _CONF = {"confirmed": "✓", "pattern": "≈", "estimate": "~est", "watch": "👁"}
    for e in macro:
        du = "undated" if e["days_until"] is None else f"D-{e['days_until']}"
        b = "🔀binary" if e.get("binary") else " "
        tag = f"[{e.get('source','?')}{_CONF.get(e.get('confidence',''),'?')}]"
        L.append(f"  {du:>7}  {e.get('date','—'):10} {e['event']:40} axis={e['axis']:10} {b} {tag}")
    L.append("\n[EARNINGS]")
    if earn:
        for e in earn:
            L.append(f"  D-{e['days_until']:<5} {e['date']:10} {e['event']:42} 🔀binary")
    else:
        L.append("  (none in window / yfinance unavailable)")
    L.append("\n[STRUCTURAL]  락업·블록딜·지수리밸런스·전환 — 날짜가 미리 알려진 촉매")
    if struct:
        for e in struct:
            b = "🔀binary" if e.get("binary") else "       "
            tag = f"[{e.get('source','?')}{_CONF.get(e.get('confidence',''),'?')}]"
            tk = e.get("ticker") or "market"
            L.append(f"  D-{e['days_until']:<5} {e['date']:10} {str(e['event'])[:44]:44} {tk:8} {b} {tag}")
            if e.get("note"):
                L.append(f"           └ {e['note'][:108]}")
    else:
        L.append("  (none in window — data/catalysts/structural_schedule.json 을 사람이 갱신한다)")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=5)
    ap.add_argument("--date", default=None)
    ap.add_argument("--tickers", default=None, help="comma-sep; default = book+candidates+blindspot")
    ap.add_argument("--no-earnings", action="store_true")
    a = ap.parse_args()
    today = _dt.date.fromisoformat(a.date) if a.date else _dt.date.today()
    horizon = a.days
    tickers = [t.strip().upper() for t in a.tickers.split(",")] if a.tickers else DEFAULT_TICKERS
    macro = macro_events(today, horizon)
    earn = [] if a.no_earnings else earnings_events(tickers, today, horizon)
    struct = structural_events(today, horizon)
    txt = render(macro, earn, today, horizon, struct)
    print(txt)
    outdir = ROOT / "llm_outputs" / today.isoformat()
    outdir.mkdir(parents=True, exist_ok=True)
    payload = {"as_of": today.isoformat(), "horizon_days": horizon,
               "binaries": [e for e in macro + earn + struct if e.get("binary")],
               "macro": macro, "earnings": earn, "structural": struct}
    (outdir / "CATALYST_WATCH.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n[saved] {outdir / 'CATALYST_WATCH.json'}")


if __name__ == "__main__":
    main()
