# FILE: research_Mvp/scripts/action_bracket.py
"""
ACTION_BRACKET — weave CYCLE_EXPOSURE + CATALYST_WATCH + risk model + live KIS → conditional DRY-RUN tickets.

The 오답노트 finding (2026-07-14): the desk had the right reads (semi F27 divergence, cool-CPI relief,
cycle-exposure gap) but never converted them into an EXECUTABLE plan before the catalyst → "saw it,
couldn't bet it." This script closes that gap deterministically:
  • CYCLE_EXPOSURE GAP  → a small TAPE-INDEPENDENT CORE-STARTER ticket in the epicenter core_pick.
  • CATALYST_WATCH near binary → a BOTH-SIDES bracket (branch A / branch B starters) from branch_map.
  • risk model (total% × stop-distance) + KIS fetch_us_buyable (integrated-margin max_qty, real fx)
    → concrete share counts + USD limit reference.
Output = pre-committed conditional tickets. ⚠️ DRY-RUN ONLY — never sends orders (human pulls --execute
in module_kis separately). Analytical/scheduling artifact.

Usage: python -X utf8 scripts/action_bracket.py [--date YYYY-MM-DD] [--risk-pct 1.5]
         [--core-risk-pct 0.8] [--stop-pct 7] [--max-pos-pct 25]
"""
from __future__ import annotations
import argparse, json, math, os, sys, datetime as _dt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "data" / "cycles" / "cycle_registry.json"
BMAP = ROOT / "data" / "catalysts" / "branch_map.json"


def _load_dotenv() -> None:
    if os.environ.get("KIS_APP_KEY") and os.environ.get("KIS_APP_SECRET"):
        return
    for c in (ROOT / ".env", ROOT.parent / ".env"):
        if c.exists():
            for line in c.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                k, v = k.strip(), v.strip().strip('"').strip("'")
                if k and v and k not in os.environ:
                    os.environ[k] = v
            return


def _first_clean(names: list[str]) -> str | None:
    for n in names:
        n = n.strip()
        if n.isalpha() and 1 <= len(n) <= 5 and n.isupper():
            return n
    return None


def _size(total_krw: float, risk_pct: float, stop_pct: float, price: float,
          fx: float, max_qty: int | None, max_pos_pct: float) -> dict:
    """shares from risk budget; capped by integrated-margin max_qty and a max position %."""
    risk_usd = total_krw * (risk_pct / 100.0) / fx
    stop_frac = stop_pct / 100.0
    raw = risk_usd / (price * stop_frac) if price and stop_frac else 0
    shares = int(math.floor(raw))
    cap_reason = ""
    pos_cap = int(math.floor((total_krw * (max_pos_pct / 100.0) / fx) / price)) if price else 0
    if shares > pos_cap:
        shares, cap_reason = pos_cap, f"maxpos {max_pos_pct}%"
    if max_qty is not None and shares > max_qty:
        shares, cap_reason = max_qty, "buyable"
    shares = max(shares, 0)
    return {"shares": shares, "risk_usd": round(risk_usd, 2),
            "notional_usd": round(shares * price, 2), "cap": cap_reason,
            "stop_price": round(price * (1 - stop_frac), 2)}


def _quote(sym: str):
    from module_KIS import fetch_us_quote, us_order_to_dict, fetch_us_buyable
    d = us_order_to_dict(fetch_us_quote(sym))
    price, exch = d.get("price"), d.get("exchange")
    buy = {}
    try:
        buy = fetch_us_buyable(exch, price, sym)
    except Exception:
        pass
    return price, exch, buy


def build(date: str, risk_pct: float, core_risk_pct: float, stop_pct: float,
          max_pos_pct: float, fx_override: float | None) -> str:
    _load_dotenv(); sys.path.insert(0, str(ROOT))
    from module_KIS import fetch_overseas_balance
    registry = json.loads(REG.read_text(encoding="utf-8"))
    bmap = json.loads(BMAP.read_text(encoding="utf-8"))
    outdir = ROOT / "llm_outputs" / date
    cyc = json.loads((outdir / "CYCLE_EXPOSURE.json").read_text(encoding="utf-8")) if (outdir / "CYCLE_EXPOSURE.json").exists() else None
    cal = json.loads((outdir / "CATALYST_WATCH.json").read_text(encoding="utf-8")) if (outdir / "CATALYST_WATCH.json").exists() else None

    bal = fetch_overseas_balance()
    total_krw = getattr(bal, "total_asset_krw", 0) or 0
    # real fx from a buyable probe (uses NVDA); fallback to override/1380
    fx = fx_override or 1380.0
    tickets = []

    # ---- 1) CORE STARTER from cycle GAP (tape-independent, small) ----
    gap_cycles = []
    if cyc:
        gap_cycles = [c for c in cyc["cycles"] if c.get("GAP")]
    for gc in gap_cycles:
        reg_c = next((c for c in registry["cycles"] if c["name"] == gc["cycle"]), None)
        core = (reg_c or {}).get("core_pick")
        if not core:
            continue
        try:
            price, exch, buy = _quote(core)
            if buy.get("exrt"):
                fx = buy["exrt"]
            s = _size(total_krw, core_risk_pct, stop_pct, price, fx, buy.get("max_qty"), max_pos_pct)
            tickets.append({
                "type": "CORE-STARTER (tape-independent)", "ticker": core, "side": "BUY",
                "condition": f"establish NOW regardless of tape — closes {gc['cycle']} epicenter GAP ({gc['epi_pct_of_total']}% < {gc['min_epicenter_pct']}%)",
                "price_ref": price, "exch": exch, "why": (reg_c or {}).get("core_pick_why", ""),
                **s, "risk_pct": core_risk_pct})
        except Exception as e:
            tickets.append({"type": "CORE-STARTER", "ticker": core, "error": str(e)[:80]})

    # ---- 2) BOTH-SIDES bracket for the nearest dated binary ----
    near = None
    if cal:
        dated = [b for b in cal.get("binaries", []) if b.get("days_until") is not None]
        near = min(dated, key=lambda x: x["days_until"]) if dated else None
    if near:
        axis = near.get("axis", "inflation")
        amap = bmap["axes"].get(axis, {})
        branch_keys = [k for k in amap if k.startswith(("A_", "B_"))]
        asym = amap.get("asymmetric", "")
        for bk in branch_keys:
            pick = _first_clean(amap[bk])
            if not pick:
                continue
            is_asym = (bk == asym)
            try:
                price, exch, buy = _quote(pick)
                if buy.get("exrt"):
                    fx = buy["exrt"]
                # asymmetric tail = smaller convex hedge; primary branch = full risk
                rp = core_risk_pct if is_asym else risk_pct
                s = _size(total_krw, rp, stop_pct, price, fx, buy.get("max_qty"), max_pos_pct)
                tickets.append({
                    "type": f"BRACKET::{bk}" + ("  ★asym-hedge" if is_asym else ""),
                    "ticker": pick, "side": "BUY",
                    "condition": f"IF {near['event']} (D-{near['days_until']}) prints {'toward '+bk[2:] if len(bk)>2 else bk}",
                    "price_ref": price, "exch": exch, **s, "risk_pct": rp})
            except Exception as e:
                tickets.append({"type": f"BRACKET::{bk}", "ticker": pick, "error": str(e)[:80]})

    # ---- render ----
    L = [f"# ACTION_BRACKET — {date}  (conditional DRY-RUN tickets · human pulls the trigger)",
         "",
         f"> Weaves CYCLE_EXPOSURE (gap→core) + CATALYST_WATCH (binary→both-sides) + risk model + live KIS.",
         f"> Book total ≈ {total_krw:,}원 · fx {fx:.0f} · per-trade risk {risk_pct}% (core {core_risk_pct}%) · stop {stop_pct}% · maxpos {max_pos_pct}%",
         f"> ⚠️ DRY-RUN — sizes are illustrative; execution is a separate human `module_kis --order ... --execute`. US = USD limit only.",
         ""]
    if near:
        L.append(f"**Nearest binary:** {near['event']} (D-{near['days_until']}, axis={near.get('axis')}) — both-sides armed below.\n")
    if not tickets:
        L.append("_No tickets — no cycle GAP and no dated binary in window._")
    for t in tickets:
        if t.get("error"):
            L.append(f"- ❌ {t['type']} {t['ticker']}: {t['error']}")
            continue
        cap = f" (capped: {t['cap']})" if t.get("cap") else ""
        L.append(f"### {t['type']} — {t['ticker']}  ({t['side']})")
        L.append(f"- **condition:** {t['condition']}")
        L.append(f"- **size:** {t['shares']} sh @ ~${t['price_ref']} (≈${t['notional_usd']:,} notional, risk ${t['risk_usd']} = {t['risk_pct']}% ){cap}")
        L.append(f"- **stop:** ${t['stop_price']} (−{stop_pct}%) · exch {t.get('exch')}")
        if t.get("why"):
            L.append(f"- **why core:** {t['why']}")
        L.append("")
    L.append("*Analytical/scheduling artifact — zero buy/sell advice. Tickets are pre-committed conditionals; "
             "no order is sent by this script.*")
    md = "\n".join(L)
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "ACTION_TICKETS.md").write_text(md, encoding="utf-8")
    return md


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=None)
    ap.add_argument("--risk-pct", type=float, default=1.5)
    ap.add_argument("--core-risk-pct", type=float, default=0.8)
    ap.add_argument("--stop-pct", type=float, default=7.0)
    ap.add_argument("--max-pos-pct", type=float, default=25.0)
    ap.add_argument("--fx", type=float, default=None)
    a = ap.parse_args()
    date = a.date or _dt.date.today().isoformat()
    md = build(date, a.risk_pct, a.core_risk_pct, a.stop_pct, a.max_pos_pct, a.fx)
    print(md)
    print(f"\n[saved] {ROOT / 'llm_outputs' / date / 'ACTION_TICKETS.md'}")


if __name__ == "__main__":
    main()
