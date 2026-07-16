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


def render(macro: list[dict], earn: list[dict], today: _dt.date, horizon: int) -> str:
    L = [f"CATALYST_WATCH — as of {today} — next {horizon} trading-ish days", "=" * 64]
    binaries = [e for e in macro + earn if e.get("binary")]
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
    txt = render(macro, earn, today, horizon)
    print(txt)
    outdir = ROOT / "llm_outputs" / today.isoformat()
    outdir.mkdir(parents=True, exist_ok=True)
    payload = {"as_of": today.isoformat(), "horizon_days": horizon,
               "binaries": [e for e in macro + earn if e.get("binary")],
               "macro": macro, "earnings": earn}
    (outdir / "CATALYST_WATCH.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n[saved] {outdir / 'CATALYST_WATCH.json'}")


if __name__ == "__main__":
    main()
