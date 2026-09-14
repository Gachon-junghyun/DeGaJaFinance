# ACTION_BRACKET — 2026-07-30  (conditional DRY-RUN tickets · human pulls the trigger)

> Weaves CYCLE_EXPOSURE (gap→core) + CATALYST_WATCH (binary→both-sides) + risk model + live KIS.
> Book total ≈ 14,687,355원 · fx 1450 · per-trade risk 1.5% (core 0.8%) · stop 7.0% · maxpos 25.0%
> ⚠️ DRY-RUN — sizes are illustrative; execution is a separate human `module_kis --order ... --execute`. US = USD limit only.

**Nearest binary:** June PCE (Personal Income & Outlays) (D-0, axis=inflation) — both-sides armed below.

### CORE-STARTER (tape-independent) — PSX  (BUY)
- **condition:** establish NOW regardless of tape — closes Energy / oil-refining (Hormuz + Russia crack) epicenter GAP (6.88% < 8.0%)
- **size:** 5 sh @ ~$210.19 (≈$1,050.95 notional, risk $81.03 = 0.8% )
- **stop:** $195.48 (−7.0%) · exch NYSE
- **why core:** cheapest large refiner on forward (11.2, PEG 1.17) + the only Energy name with shorts actively exiting (FINRA short-vol z -1.43, 5v5 -16.6▼) = clean structural entry, not an extended one (cf. MPC RSI 85.7). Crack-spread leverage, not crude beta. Human-locked 2026-07-17; evidence: llm_outputs/2026-07-17/industry_US/SECTOR_DEEP_ENRG.md

### BRACKET::A_cool — NVDA  (BUY)
- **condition:** IF June PCE (Personal Income & Outlays) (D-0) prints toward cool
- **size:** 11 sh @ ~$195.04 (≈$2,145.44 notional, risk $151.93 = 1.5% )
- **stop:** $181.39 (−7.0%) · exch NASD

### BRACKET::B_hot  ★asym-hedge — MPC  (BUY)
- **condition:** IF June PCE (Personal Income & Outlays) (D-0) prints toward hot
- **size:** 3 sh @ ~$313.23 (≈$939.69 notional, risk $81.03 = 0.8% )
- **stop:** $291.3 (−7.0%) · exch NYSE

*Analytical/scheduling artifact — zero buy/sell advice. Tickets are pre-committed conditionals; no order is sent by this script.*
---

## ⚠ ADDENDUM — appended by ALPHA (stage 9), 2026-07-30 · append-only, nothing above is rewritten

**Three corrections to the generated tickets above. None of them changes a ticket; all of them change
what a reader may conclude from one.**

### 1 · ⚠⚠ The "nearest binary" this file brackets HAS ALREADY PRINTED, and it printed COOL

`action_bracket` armed both sides of **June PCE (D-0)**. **That release printed at 08:30 ET today**:
**core PCE +0.1% MoM** (after a revised +0.3%), **3.3% YoY** from 3.4%; headline **−0.1% MoM / 3.7%
YoY** from 4.1%. ⇒ **branch `A_cool` is the branch that occurred, and `B_hot` is void.**
**This was scored as `S15 FIRED-B` at this run's HANDOVER.** The bracket generator has no way to know
a same-day binary already settled — **stated here so the file is not read as forward-looking on that
row.**

### 2 · ⚠⚠ The CORE-STARTER's `why core` string is a RETRACTED claim — **D19, SIXTH consecutive run**

The rationale printed above reads *"cheapest large refiner on forward (11.2, PEG 1.17) … FINRA
short-vol z −1.43, 5v5 −16.6▼"*. **That string was retracted as R8 on 2026-07-22** and has been
carried unchanged ever since:

- **The "cheapest" clause has no stated basis.** Measured live today on one like-for-like basis
  (yfinance forward P/E): **MPC 11.28 · VLO 12.30**. The desk measured **PSX 11.06 < MPC 11.27 <
  VLO 12.24** on 07-29 — so the ordering happens to favour PSX **on this basis**, which is exactly
  D19's point: **the number is close and its basis is still unstated.**
- **The FINRA clause is a frozen string.** It has been wrong in two different directions on two
  consecutive runs (measured 07-20 **z +2.01**, 07-21 **z +0.01**) and is not re-measured by the
  generator.

⚠ **`core_pick` is a HUMAN-LOCKED registry field and was NOT modified.** The claim is flagged; the
field awaits a human.

### 3 · ★ The ticket's own subject is this run's WEAKEST refiner on the axis the DEEP measured

`SECTOR_DEEP_ENRG.md §0`, settled 2026-07-29, days-21-60 excess vs **SPY**:
**VLO +2.8 · MPC +1.1 · PSX −8.5.** **PSX's base has deteriorated for three consecutive runs
(+1.6 → −5.91 → −8.5)** and is **the only refiner with a decaying 60-day foundation.**
Separately, **PSX's straddle (±2.7%, expiry 2026-07-31) expires BEFORE its 2026-08-05 print**, so it
is **not event-priced**, while **MPC's (±9.4%, expiry 08-21, D22) covers its 08-04 print.**

⇒ **The cycle-GAP that justifies a core-starter is real** (Energy epicenter **6.88% vs an 8.0% floor,
−1.119pp**), **and the instrument the generator selected for it is the one the desk's own deep-dive
measured as the weakest of the three.** ⚠ **This desk does not choose the instrument — that is a
human decision on a human-locked field.** It records the disagreement.

### 4 · ⚠ The GAP's movement is denominator drift, not information

The Energy epicenter gap ran **−0.277 → −0.327 → −1.119pp** across three readings, and the AI-compute
flag flipped **🚨 → ✅ (+0.98pp)** on a session when **NVDA fell 3.55% and AVGO 2.78%** — because the
book's total fell faster (**$11,575 → $10,654**). **Ninth consecutive mark-to-market reading with the
held set unchanged.** **A ticket generated off a flag whose movement is drift should be read as an
exposure observation, not as a signal.**

*Analytical artifact — zero buy/sell advice. No order is sent by this desk under any branch.*
