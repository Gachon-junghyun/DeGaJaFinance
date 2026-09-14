# ACTION_BRACKET — 2026-08-31  (conditional DRY-RUN tickets · human pulls the trigger)

> Weaves CYCLE_EXPOSURE (gap→core) + CATALYST_WATCH (binary→both-sides) + risk model + live KIS.
> Book total ≈ 15,248,979원 · fx 1380 · per-trade risk 1.5% (core 0.8%) · stop 7.0% · maxpos 25.0%
> ⚠️ DRY-RUN — sizes are illustrative; execution is a separate human `module_kis --order ... --execute`. US = USD limit only.

**Nearest binary:** AVGO earnings (D-2, axis=earnings) — both-sides armed below.

_No tickets — no cycle GAP and no dated binary in window._
*Analytical/scheduling artifact — zero buy/sell advice. Tickets are pre-committed conditionals; no order is sent by this script.*
---

# ADDENDUM — industry_US ALPHA (Stage 10), 2026-08-31

> Appended, never clobbered. The block above is the script's own output and is left verbatim.

## 1 · 🚨 `D421` reproduces for a THIRD consecutive run — the script contradicts itself in one output

The block above prints **both** of these, four lines apart:

> **Nearest binary:** AVGO earnings (**D-2**, axis=earnings) — **both-sides armed below.**
> _No tickets — **no cycle GAP and no dated binary in window**._

**`AVGO` at D-2 is inside any reasonable window**, so the second line is false on the first line's own
evidence. `D421`'s prescription — *the "nearest binary" line and the in-window test use the same
window* — remains unwired. **Third run, named rather than worked around.**
⚠ Consequence for reading this file: **"no tickets" here does NOT mean "no binary to bracket."**
It means the ticket generator's window test rejected a binary its own header announced.

## 2 · Why zero tickets is nevertheless the correct output today

Even with `D421` fixed, this run would issue **no core-starter and no new equity ticket**:

1. **No cycle GAP.** `cycle_exposure.py` (REAL KIS book): AI-compute epicenter **16.91%** vs a 12.0%
   floor (margin **+4.91pp**), Energy/refining **10.17%** vs 8.0% (**+2.17pp**). **A tape-independent
   core-starter fires only on a GAP, and there is none.** ⚠ Its three stated weaknesses stand
   (`BLINDSPOT_PREMORTEM` Lens 4): AI-power and optical have **no registry row**, so 0% there is
   *unstatable*; **`TSM`/`SMCI` sit outside the universe**; the audit covers **one of three books**.
2. **Every binary in the window is already bracketed both ways** — six of six
   (`S131` MSCI D-0 · `S132`+`S127` AVGO D-2/D-3 · `S126`+`P114`+`S134` NFP D-4 · `P108`+`P116`+`P120`
   CPI D-11 · PPI **dropped on information grade for a 4th run, by decision** · `P107`+`P112`+`P117`+`P118`
   Hormuz). **Issuing a ticket on any of them would re-freeze a live threshold** (`D242`).
3. **The exposure rule reads `정상`, not `복귀`** — there is **no target-filling obligation** today, so
   no ticket is required to close a band gap. ⚠ And the band gap itself belongs to a **different
   book** (`C23`): the KR-contest ledger is **85.3% invested vs 95%**, while the **real US account is
   53.0% cash**. **A ticket sized against the wrong book is worse than no ticket.**

## 3 · The pre-committed conditionals this run DOES hand forward (as brackets, not tickets)

Nothing below is an order, a size, or a recommendation. They are the **frozen observables** a later
run reads:

| id | observable | A / B | settles |
|---|---|---|---|
| **`S136`** | `EW{SLB,MPC,PSX,VLO,COP}` − `EW{XOM,EOG,FANG}`, 5-session sum | **≥ +3.90pp** / **≤ −3.90pp** | 2026-09-09 |
| **`S137`** | `EW{LITE,COHR}` − `SMH`, 5-session sum | **≥ +9.00pp** / **≤ −9.00pp** | 2026-09-09 |
| **`P118`** | `DCOILWTICO` `[FRED]` spot (roll-immune) | **≥ 91.00** / **≤ 82.00** | 2026-09-11 |
| **`P119`** | `JPY=X` settled close, any bar 09-01→09-18 | **≥ 164.00** / **≤ 156.00** | 2026-09-18 |
| **`P120`** | `BAMLC0A0CM` IG OAS | **≤ 0.76** / **≥ 0.88** | 2026-09-25 |

## 4 · 🚨 The ticket this run would have wanted, and why it was not written

`SLB` is the run's cleanest chain-hop shape — **OBV +0.318 매집 with `rs60` still −1.2 vs `SPY`**
(accumulation that has not yet produced a 60-day leg), **FINRA short-vol z +2.40 — the board's
extreme — with 5v5 +9.0▲**, and a **$3.4bn data-centre acquisition announced today**.
**No ticket is written**, for three stated reasons:
1. ⚡ **A crowded short is turn-conditional squeeze fuel, never a standalone entry.** The desk's own
   rule; a ticket here would violate it.
2. 🚨 **Its estimate book is the worst in the entire BET sheet — 3 up : 14 down (0q), 1 up : 14 down
   (+1q)** — against **+3.0%** consensus upside at **−0.5%** from its 52-week high.
3. **`P118`-A (spot WTI ≥ 91.00) would make the move the barrel**, not the thesis — the ambiguity is
   already written into `EVENT_ALPHA` card 8.
⇒ **Filed to `missed_ledger` upstream rather than ticketed**, so that if it runs, the cost is scored
rather than forgotten.

*Analytical artifact — zero buy/sell advice. No order is sent by this desk.*
