# FILE: research_Mvp/scripts/cycle_exposure.py
"""
CYCLE_EXPOSURE — deterministic GAP flag: dominant secular cycles (registry) vs the REAL KIS book.

The 오답노트 finding (2026-07-14): an aggressive book held 0% of the AI-compute epicenter
(all exposure was one layer off = power/gas) and structurally lagged every epicenter-up day.
The model kept rationalizing "crowded, wait for the dip." This script removes the rationalization:
it computes the exposure % as a NUMBER and raises a 🚨 GAP when the book holds < min_epicenter_pct
of a top-ranked cycle. Judgment can't skip a fact.

Reads:  data_build/cycles/cycle_registry.json  (human/find-cycle-curated layers)
        KIS overseas balance via module_kis.fetch_overseas_balance()  (the real book)
Writes: llm_outputs/{date}/CYCLE_EXPOSURE.md   (md-ledger)  + optional --json

Usage:  python -X utf8 scripts/cycle_exposure.py [--date YYYY-MM-DD] [--json] [--book-json PATH]
        --book-json lets you pass a saved balance dict (offline / testing) instead of hitting KIS.
Analytical artifact only — ZERO buy/sell advice. Read-only (never orders).
"""
from __future__ import annotations
import argparse, json, os, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]          # research_Mvp/
REG = ROOT / "data" / "cycles" / "cycle_registry.json"


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


def _fetch_book(book_json: str | None) -> dict:
    """Return {holdings:[{code,eval_usd}], total_asset_krw, cash_krw}. Live KIS or a saved dict."""
    if book_json:
        d = json.loads(Path(book_json).read_text(encoding="utf-8"))
        return d
    _load_dotenv()
    sys.path.insert(0, str(ROOT))
    from module_KIS import fetch_overseas_balance
    b = fetch_overseas_balance()
    holds = [{"code": h.code, "name": getattr(h, "name", h.code),
              "eval_usd": float(getattr(h, "eval_frcr", 0) or 0)} for h in b.holdings]
    return {"holdings": holds,
            "total_asset_krw": getattr(b, "total_asset_krw", 0),
            "cash_krw": getattr(b, "krw_deposit", 0),
            "withdrawable_krw": getattr(b, "withdrawable_krw", 0)}


def _classify(code: str, cyc: dict) -> str | None:
    if code in cyc["epicenter"]:
        return "epicenter"
    if code in cyc.get("adjacent", []):
        return "adjacent"
    if code in cyc.get("fuel", []):
        return "fuel"
    return None


def analyze(book: dict, registry: dict, fx: float) -> list[dict]:
    holds = book.get("holdings", [])
    invested_usd = sum(h["eval_usd"] for h in holds) or 0.0
    total_krw = book.get("total_asset_krw", 0) or 0
    total_usd = total_krw / fx if total_krw else invested_usd
    out = []
    for cyc in registry["cycles"]:
        layers = {"epicenter": [], "adjacent": [], "fuel": []}
        for h in holds:
            lyr = _classify(h["code"], cyc)
            if lyr:
                layers[lyr].append(h)
        epi_usd = sum(h["eval_usd"] for h in layers["epicenter"])
        adj_usd = sum(h["eval_usd"] for h in layers["adjacent"])
        fuel_usd = sum(h["eval_usd"] for h in layers["fuel"])
        epi_pct_tot = 100 * epi_usd / total_usd if total_usd else 0.0
        any_pct_tot = 100 * (epi_usd + adj_usd + fuel_usd) / total_usd if total_usd else 0.0
        gap = (cyc["rank"] <= 2) and (epi_pct_tot < cyc.get("min_epicenter_pct", 0))
        out.append({
            "cycle": cyc["name"], "rank": cyc["rank"],
            "min_epicenter_pct": cyc.get("min_epicenter_pct", 0),
            "epi_pct_of_total": round(epi_pct_tot, 2),
            "any_layer_pct_of_total": round(any_pct_tot, 2),
            "epi_usd": round(epi_usd, 2), "adj_usd": round(adj_usd, 2), "fuel_usd": round(fuel_usd, 2),
            "epi_names": [h["code"] for h in layers["epicenter"]],
            "adj_names": [h["code"] for h in layers["adjacent"]],
            "fuel_names": [h["code"] for h in layers["fuel"]],
            "GAP": gap,
        })
    return out, {"invested_usd": round(invested_usd, 2), "total_usd": round(total_usd, 2),
                 "total_krw": total_krw, "cash_krw": book.get("cash_krw", 0)}


def render_md(rows: list[dict], meta: dict, date: str, fx: float) -> str:
    L = [f"# CYCLE_EXPOSURE — {date}  (dominant cycles ↔ REAL KIS book)",
         "",
         "> Deterministic GAP flag (오답노트 2026-07-14: aggressive book held 0% of the AI-compute epicenter).",
         "> A tape-🔴/crowded reading gates ADD timing — it does NOT justify zero core exposure to a top-rank cycle.",
         f"> Book: total ≈ ${meta['total_usd']:,.0f} ({meta['total_krw']:,}원) · invested ${meta['invested_usd']:,.0f} · cash {meta['cash_krw']:,}원 · fx {fx:.0f}",
         "", "| Cycle | rank | epicenter % | (need≥) | any-layer % | held epicenter | GAP |",
         "|---|---|---|---|---|---|---|"]
    for r in rows:
        flag = "🚨 **GAP**" if r["GAP"] else ("✅" if r["epi_pct_of_total"] > 0 else "—")
        held = ", ".join(r["epi_names"]) or "*(none)*"
        L.append(f"| {r['cycle']} | {r['rank']} | **{r['epi_pct_of_total']}%** | {r['min_epicenter_pct']}% | "
                 f"{r['any_layer_pct_of_total']}% | {held} | {flag} |")
    gaps = [r for r in rows if r["GAP"]]
    L += ["", "## Verdict"]
    if gaps:
        for r in gaps:
            adj = ", ".join(r["adj_names"] + r["fuel_names"]) or "none"
            L.append(f"- 🚨 **{r['cycle']}** (rank {r['rank']}): epicenter exposure **{r['epi_pct_of_total']}%** "
                     f"< required {r['min_epicenter_pct']}%. Book touches this cycle only via adjacent/fuel "
                     f"({adj}) — beta to the *consequence*, none to the *engine*. **Establish a small tape-independent "
                     f"core in the epicenter; a crowded tape gates the ADDS, not the core's existence.**")
    else:
        L.append("- ✅ No top-rank cycle GAP: the book holds a core in every rank≤2 cycle's epicenter.")
    L += ["", "*Registry: data_build/cycles/cycle_registry.json · book: KIS fetch_overseas_balance (read-only). "
          "Analytical artifact — zero buy/sell advice.*"]
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=None)
    ap.add_argument("--fx", type=float, default=1380.0, help="KRW per USD for total-asset conversion")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--book-json", default=None, help="saved balance dict (offline/testing)")
    a = ap.parse_args()
    date = a.date or __import__("datetime").date.today().isoformat()
    registry = json.loads(REG.read_text(encoding="utf-8"))
    book = _fetch_book(a.book_json)
    rows, meta = analyze(book, registry, a.fx)
    md = render_md(rows, meta, date, a.fx)
    outdir = ROOT / "llm_outputs" / date
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "CYCLE_EXPOSURE.md").write_text(md, encoding="utf-8")
    print(md)
    if a.json:
        payload = {"date": date, "meta": meta, "cycles": rows}
        (outdir / "CYCLE_EXPOSURE.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n[saved] {outdir / 'CYCLE_EXPOSURE.md'}")


if __name__ == "__main__":
    main()
