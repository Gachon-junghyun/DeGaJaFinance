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
            # 판정은 반올림 전 값으로 한다. 표시값만 보면 "12.0% < 12.0%" 처럼 자기모순으로 읽혀
            # 툴이 고장난 줄 안다 — 실제 여유를 pp 로 같이 낸다(마진이 0에 가까울수록 중요).
            "margin_pp": round(epi_pct_tot - cyc.get("min_epicenter_pct", 0), 3),
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
        # ⚠ min_epicenter_pct=0 은 '통과'가 아니라 **기준 미설정**이다 — GAP 식이
        #   `epi_pct < 0` 이라 수학적으로 절대 참이 될 수 없다(=검사 자체가 꺼져 있다).
        #   실측 2026-07-17: rank-2 Energy 가 이 상태로 "✅/—" 를 찍어 에피센터 0.0% 를
        #   통과처럼 보이게 했다. 꺼진 검사를 통과로 렌더하지 않는다.
        if not r["min_epicenter_pct"]:
            flag = "⚪ n/a (기준 미설정)"
            need = "—"
        else:
            flag = "🚨 **GAP**" if r["GAP"] else "✅"
            need = f"{r['min_epicenter_pct']}%"
        held = ", ".join(r["epi_names"]) or "*(none)*"
        L.append(f"| {r['cycle']} | {r['rank']} | **{r['epi_pct_of_total']}%** | {need} | "
                 f"{r['any_layer_pct_of_total']}% | {held} | {flag} |")
    gaps = [r for r in rows if r["GAP"]]
    L += ["", "## Verdict"]
    if gaps:
        for r in gaps:
            adj = ", ".join(r["adj_names"] + r["fuel_names"]) or "none"
            L.append(f"- 🚨 **{r['cycle']}** (rank {r['rank']}): epicenter exposure **{r['epi_pct_of_total']}%** "
                     f"< required {r['min_epicenter_pct']}% (margin **{r['margin_pp']:+.3f}pp**). "
                     f"Book touches this cycle only via adjacent/fuel "
                     f"({adj}) — beta to the *consequence*, none to the *engine*. **Establish a small tape-independent "
                     f"core in the epicenter; a crowded tape gates the ADDS, not the core's existence.**")
    else:
        L.append("- ✅ No top-rank cycle GAP: the book holds a core in every rank≤2 cycle's epicenter.")
    # ⚠ 기준 미설정(min=0)인 rank≤2 사이클은 위 '✅ No GAP' 이 **검사하지 않은** 것이다.
    #   침묵하면 '통과'로 읽힌다 — 무엇을 안 봤는지 항상 밝힌다(P4).
    unarmed = [r for r in rows if r["rank"] <= 2 and not r["min_epicenter_pct"]]
    for r in unarmed:
        L.append(f"- ⚪ **{r['cycle']}** (rank {r['rank']}): **검사 안 함 — min_epicenter_pct 미설정(0.0).** "
                 f"현재 에피센터 {r['epi_pct_of_total']}%. 기준이 0 이면 GAP 식(`epi_pct < 0`)이 절대 "
                 f"참이 될 수 없어 이 사이클은 **어떤 노출에서도 GAP 이 뜨지 않는다**. 위 '✅ No GAP' 은 "
                 f"이 줄에 대한 통과가 아니다 — 레지스트리에 실제 하한을 넣어야 검사가 켜진다.")
    L += ["", "*Registry: data_build/cycles/cycle_registry.json · book: KIS fetch_overseas_balance (read-only). "
          "Analytical artifact — zero buy/sell advice.*"]
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=None)
    ap.add_argument("--fx", type=float, default=1380.0, help="KRW per USD for total-asset conversion")
    ap.add_argument("--json", action="store_true",
                    help="(호환용 no-op — CYCLE_EXPOSURE.json 은 이제 항상 쓴다. action_bracket 이 그걸 읽는다)")
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
    # ⚠ JSON 은 **항상** 쓴다(예전엔 --json 일 때만). `action_bracket.py` 가 CORE-STARTER 티켓을
    #   이 파일의 GAP 플래그로 만드는데, .md 만 갱신되면 둘이 조용히 어긋난다 —
    #   실측 2026-07-17: .md 는 🚨GAP 인데 .json 이 옛 GAP=false 라 티켓이 안 나왔다.
    #   사람이 읽는 산출과 다음 스크립트가 읽는 계약이 갈라지면 안 된다.
    payload = {"date": date, "meta": meta, "cycles": rows}
    (outdir / "CYCLE_EXPOSURE.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n[saved] {outdir / 'CYCLE_EXPOSURE.md'} · {outdir / 'CYCLE_EXPOSURE.json'}")


if __name__ == "__main__":
    main()
