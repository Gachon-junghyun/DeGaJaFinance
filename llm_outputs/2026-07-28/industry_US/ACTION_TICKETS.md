# ACTION_BRACKET — 2026-07-28  (conditional DRY-RUN tickets · human pulls the trigger)

> Weaves CYCLE_EXPOSURE (gap→core) + CATALYST_WATCH (binary→both-sides) + risk model + live KIS.
> Book total ≈ 15,907,772원 · fx 1465 · per-trade risk 1.5% (core 0.8%) · stop 7.0% · maxpos 25.0%
> ⚠️ DRY-RUN — sizes are illustrative; execution is a separate human `module_kis --order ... --execute`. US = USD limit only.

**Nearest binary:** FOMC decision (Warsh, no SEP) (D-1, axis=rates) — both-sides armed below.

### CORE-STARTER (tape-independent) — NVDA  (BUY)
- **condition:** establish NOW regardless of tape — closes AI-compute / semiconductors epicenter GAP (8.23% < 12.0%)
- **size:** 6 sh @ ~$193.32 (≈$1,159.92 notional, risk $86.84 = 0.8% )
- **stop:** $179.79 (−7.0%) · exch NASD
- **why core:** real-alpha REAL/not-priced, flow 🟡중립=non-chase entry, epicenter bottleneck, fwd PE 16.5 < AVGO 20.1

### CORE-STARTER (tape-independent) — PSX  (BUY)
- **condition:** establish NOW regardless of tape — closes Energy / oil-refining (Hormuz + Russia crack) epicenter GAP (7.67% < 8.0%)
- **size:** 5 sh @ ~$208.775 (≈$1,043.88 notional, risk $86.84 = 0.8% )
- **stop:** $194.16 (−7.0%) · exch NYSE
- **why core:** cheapest large refiner on forward (11.2, PEG 1.17) + the only Energy name with shorts actively exiting (FINRA short-vol z -1.43, 5v5 -16.6▼) = clean structural entry, not an extended one (cf. MPC RSI 85.7). Crack-spread leverage, not crude beta. Human-locked 2026-07-17; evidence: llm_outputs/2026-07-17/industry_US/SECTOR_DEEP_ENRG.md

### BRACKET::A_cool  ★asym-hedge — NVDA  (BUY)
- **condition:** IF FOMC decision (Warsh, no SEP) (D-1) prints toward cool
- **size:** 6 sh @ ~$193.31 (≈$1,159.86 notional, risk $86.84 = 0.8% )
- **stop:** $179.78 (−7.0%) · exch NASD

### BRACKET::B_hot — XLE  (BUY)
- **condition:** IF FOMC decision (Warsh, no SEP) (D-1) prints toward hot
- **size:** 39 sh @ ~$58.5799 (≈$2,284.62 notional, risk $162.83 = 1.5% )
- **stop:** $54.48 (−7.0%) · exch AMEX

*Analytical/scheduling artifact — zero buy/sell advice. Tickets are pre-committed conditionals; no order is sent by this script.*
---

## ⚠ ADDENDUM — appended 2026-07-28 by the `industry_US` ALPHA stage (append-only; nothing above is rewritten)

> ⚠ **`core_pick` is a HUMAN-LOCKED registry field. No stage may rewrite it, and this addendum does
> not.** The corrections below are recorded beside the ticket, per the R8 precedent.

### D19 / D32 fire again — the PSX ticket's `why core` is stale in BOTH of its clauses, on a FOURTH consecutive run

The generated string reads:
> *"cheapest large refiner on forward (11.2, PEG 1.17) + the only Energy name with shorts actively
> exiting (FINRA short-vol z −1.43, 5v5 −16.6▼)"*

| Clause | Measured today (2026-07-28) |
|---|---|
| *"cheapest large refiner on forward (11.2)"* | ⚠ **RETRACTED as R8 on 2026-07-22.** Today's pull: **PSX 11.01 · MPC 11.23 · VLO 12.09** — PSX is marginally the lowest **on this basis**, but the ordering is **basis-dependent** (on FY26 consensus it was MPC 8.8 < VLO 9.4 < PSX 10.8) and **the claim is not re-asserted by this desk** |
| *"z −1.43, 5v5 −16.6▼"* | ⚠ **PSX's measured FINRA z is −0.38 (baseline 40.6%, 5v5 +5.3▲)** — the **fifth different value** this frozen string has been wrong against (+2.01 → +0.01 → +1.03 → −0.38). ★ **And it names the wrong ticker: the Energy name with a readable short move today is VLO, at z +1.56 🔴 — a SURGE, not an exit** |

### A third stale clause, not previously logged

The **NVDA core-starter** ticket reads *"flow 🟡중립=non-chase entry"*. **`SECTOR_FLOW_US.json`
(`asof 2026-07-27 settled`) tags NVDA 🟢가속** — ⚠ **and that green is a VELOCITY path**
(`vol_surge` 0.81, `velocity` 2.72), **not volume confirmation**. Both halves of the string are stale.

⇒ **A ticket whose stated premises are frozen strings is worse than no ticket — it reads as evidence.**
**The fix remains what D32 proposed: recompute the rationale fields at generation time, or stamp each
with its as-of date so staleness is visible instead of authoritative.** A code change; **human.**

### What the brackets themselves are, restated against this run's own registrations

- **The two CORE-STARTERs correctly reflect the two 🚨 GAPs** — AI-compute (**8.23% vs a 12.0% floor,
  margin −3.769pp**) and Energy (**7.67% vs 8.0%, −0.327pp**). ★ **The Energy GAP is one session old:
  it read ✅ at +0.027pp on 07-27 and flipped on mark-to-market drift with nothing traded** — which is
  **M181's pre-registered warning vindicated**, and the live argument for **D61's proposed 0.5pp
  UNRESOLVED band.**
- ⚠ **The registry the GAP is measured against is `updated: 2026-07-17` = 11 days stale with 3 rows**,
  and the artifact's footer cites **`data_build/cycles/`, a path that does not exist (D60)**.
  **DELL (+103.7 RS60) and HPE (+66.4) — the two cleanest measured expressions in the AI-compute
  layer — sit in no registry row at any layer.**
- **The FOMC both-sides bracket (A_cool → NVDA · B_hot → XLE) is genuine** and matches the nearest
  binary. ⚠ **But the book's registered FOMC brackets are S19 (hike), S23 (bear-flattener hold) and
  S9 (dovish real-rate fall), and S23's branch — a hold with further flattening — is the one this
  ticket pair does NOT express.** **T10Y2Y is +0.36 and moved AWAY from its +0.20 trigger.**

**Everything above is analytical. No order is sent by this desk; a human executes separately (P4).**
