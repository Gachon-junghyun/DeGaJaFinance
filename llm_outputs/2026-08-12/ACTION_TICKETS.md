# ACTION_BRACKET — 2026-08-12  (conditional DRY-RUN tickets · human pulls the trigger)

> Weaves CYCLE_EXPOSURE (gap→core) + CATALYST_WATCH (binary→both-sides) + risk model + live KIS.
> Book total ≈ 15,924,263원 · fx 1415 · per-trade risk 1.5% (core 0.8%) · stop 7.0% · maxpos 25.0%
> ⚠️ DRY-RUN — sizes are illustrative; execution is a separate human `module_kis --order ... --execute`. US = USD limit only.

**Nearest binary:** July CPI (D-0, axis=inflation) — both-sides armed below.

### BRACKET::A_cool — NVDA  (BUY)
- **condition:** IF July CPI (D-0) prints toward cool
- **size:** 11 sh @ ~$217.5 (≈$2,392.5 notional, risk $168.81 = 1.5% )
- **stop:** $202.27 (−7.0%) · exch NASD

### BRACKET::B_hot  ★asym-hedge — MPC  (BUY)
- **condition:** IF July CPI (D-0) prints toward hot
- **size:** 3 sh @ ~$336.42 (≈$1,009.26 notional, risk $90.03 = 0.8% )
- **stop:** $312.87 (−7.0%) · exch NYSE

*Analytical/scheduling artifact — zero buy/sell advice. Tickets are pre-committed conditionals; no order is sent by this script.*
---

# ═══ RUN-2 ADDENDUM — 2026-08-12 23:50 KST · **APPEND-ONLY** ═══

> ⚠️ **Still DRY-RUN. Nothing below sends an order, and nothing below is advice (P4).**
> The tickets above were written at 11:41 KST, **~10 hours before the print**, as pre-committed
> conditionals. **RUN-2's only job here is to record which antecedent resolved** — not to pull anything.

## ★ The conditional's antecedent has RESOLVED

| Ticket | Condition as written | Resolution |
|---|---|---|
| `BRACKET::A_cool` — NVDA | *"IF July CPI (D-0) prints toward cool"* | ✅ **MATCHED, on the print as reported**: headline **+0.1% m/m · 3.4% y/y, down from 3.5%, in line with consensus**; core **+0.2% m/m / 2.5% y/y**; traders **tilted to HOLD from a ~50-50 hold-vs-hike split** `[WebSearch ×2 outlets]` |
| `BRACKET::B_hot` — MPC | *"IF July CPI (D-0) prints toward hot"* | ❌ **NOT matched on the print** |

**🚩 Three qualifications, and they are the point of writing this instead of just marking the box:**

1. **The print is `[WebSearch]`-grade, not `[FRED]`.** `module_macro_us` still returns **CPI 332.568 @
   2026-06-01** — **the desk's own primary instrument does not carry the July print.** A conditional
   resolved on a secondary source is resolved **provisionally.**
2. ⚠⚠ **"Cool" is a label about the print, not about inflation.** MACRO §R2-C registers the opposite
   reading as a falsifiable proposition (**`P-R2-1`**): **the benign headline is energy-led *downward*
   (gasoline −2.9% m/m) and measures the last month BEFORE the supply shock compounds** — while the
   same day's tape carries **Hormuz at 28 articles / 14 outlets, an IEA 1.8 mb/d quarterly deficit,
   Libya refinery strikes and Black Sea terminal strikes.** ⇒ **the ticket that matched is the one
   whose framing this run's own MACRO stage argues is stale.** ★ Note what that implies about the
   pair: **`B_hot`'s underlying (MPC, a refiner) is the leg that `P-R2-1` favours**, so the two
   tickets are **not** a clean cool/hot split — **B_hot is closer to an energy-supply ticket than an
   inflation-print ticket.** That mismatch is recorded, not resolved.
3. ⛔ **No price confirmation exists.** The 08-12 bar is absent on every interval; **NVDA's quoted
   ~$217.5 and MPC's ~$336.42 are 08-11 marks.** Both tickets' sizes remain **illustrative** —
   and **PREFLIGHT G4 + G6 FAIL means no size in this run may be called grounded** (any size is
   **"mechanical 1/4"**, never `--ic`-based).

⇒ **Status: `A_cool` antecedent provisionally satisfied; execution remains a separate human action;
the desk records the match and its three caveats and stops there.**

## Binaries still standing after tonight

| When | Binary | Bracket |
|---|---|---|
| **08-13** | **July PPI** | **S71** (CPI→PPI divergence) |
| **08-19** | ENRG / HLTH / MATR / FIN tilt falsifiers | **S75 · S76 · S77 · S78** |
| **08-24** | Hormuz reopening conditions | **S74** (S8 still undated, 11th run) |
| **08-26** | **NVDA earnings** | ★ **S79 — registered by THIS run** (2 legs; Leg 2 tests the G4 risk-unit question) |
