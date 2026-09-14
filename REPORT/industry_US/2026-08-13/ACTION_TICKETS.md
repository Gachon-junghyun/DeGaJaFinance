# ACTION_BRACKET — 2026-08-13  (conditional DRY-RUN tickets · human pulls the trigger)

> Weaves CYCLE_EXPOSURE (gap→core) + CATALYST_WATCH (binary→both-sides) + risk model + live KIS.
> Book total ≈ 16,034,268원 · fx 1415 · per-trade risk 1.5% (core 0.8%) · stop 7.0% · maxpos 25.0%
> ⚠️ DRY-RUN — sizes are illustrative; execution is a separate human `module_kis --order ... --execute`. US = USD limit only.

**Nearest binary:** July PPI (D-0, axis=inflation) — both-sides armed below.

### BRACKET::A_cool — NVDA  (BUY)
- **condition:** IF July PPI (D-0) prints toward cool
- **size:** 10 sh @ ~$226.05 (≈$2,260.5 notional, risk $169.97 = 1.5% )
- **stop:** $210.23 (−7.0%) · exch NASD

### BRACKET::B_hot  ★asym-hedge — MPC  (BUY)
- **condition:** IF July PPI (D-0) prints toward hot
- **size:** 3 sh @ ~$349.925 (≈$1,049.78 notional, risk $90.65 = 0.8% )
- **stop:** $325.43 (−7.0%) · exch NYSE

*Analytical/scheduling artifact — zero buy/sell advice. Tickets are pre-committed conditionals; no order is sent by this script.*
---

# ═══ §ALPHA-EXT — appended 2026-08-13 23:40 KST by L1·ALPHA (industry_US) ═══

> **DRY-RUN conditional tickets. No order is sent by any stage of this desk. A human executes
> separately via `module_KIS ... --execute`.** Analytical artifact, zero buy/sell advice (P4).

## 1 · What the script produced, and its two limitations — stated, not hidden

`action_bracket.py` armed the nearest binary (**July PPI, D-0**) both ways:
**`BRACKET::A_cool` NVDA · 10sh @ ~$226.05 · stop $210.23 (−7.0%) · risk 1.5%** and
**`BRACKET::B_hot` ★asym-hedge MPC · 3sh @ ~$349.925 · stop $325.43 · risk 0.8% (core).**

⚠⚠ **Two things the script cannot know, and they matter tonight:**
1. **The PPI has ALREADY PRINTED** (2026-08-13 08:30 ET, ~40 min before this run's MACRO stage). The
   script's condition *"IF July PPI prints toward cool/hot"* is therefore **not a forward condition —
   it is a reading of a known print.** ⇒ **the correct forward condition is the 08-13 SETTLED CLOSE**,
   which is what every bracket below uses.
2. **The print was SPLIT, not cool or hot**: headline final demand **0.0% MoM** with **goods −0.7%**,
   against **core ex-food/energy/trade services +0.4% MoM and +4.7% over 12 months.**
   ⇒ **neither of the script's two branches describes the observable**, and this stage does not force
   one. **Both tickets stay armed on their price conditions, not on the print's label.**

⚠ **Sizing note (PREFLIGHT G6 FAIL, 2.6× slow accrual)**: every size here is **"mechanical ¼"** and
**no `kelly_size --ic` figure is reported as evidence-backed.** The accompanying concentration figure
is **`--days 500`, largest measured unit {AVGO, NVDA} = 12.04% of total assets vs a 40% cap** — the
window is stated because **G4 FAILED and no single concentration number is admissible.**

## 2 · The PPI both-sides bracket, re-based on tonight's close (PREMORTEM §3a)

| | Condition (frozen) | What it would mean |
|---|---|---|
| **AGAINST-US (the tape trades the HEADLINE half)** | `XLU` 1-session excess vs `SPY` **≥ +1.80pp** on the **2026-08-13 settled close** **AND** `XLRE` **and** `XLP` excess **both > 0** | **Four tilts hit by ONE driver**: UTIL UW · RE UW · STPL UW− directly, and ENRG OW− via the −0.7% goods leg. **Starter list**: `NEE` · `AMT` · `PG` · `TLT` · `MPC` (the leg that unwinds — and `S67`'s own subject) |
| **INVALIDATION of that read** | `XLU` ≥ +1.80 while `XLRE` **and** `XLP` are **both ≤ 0** | An idiosyncratic utility move, **not** a duration bid ⇒ the UW stands |
| **FOR-US** | see **`S80`**, which replaces `S71`'s job on a 4-session window | — |

⚠ **Implied move, checked not assumed** (`module_flow --positioning`, this run, all expiries
**2026-08-14, D1**): **`XLU` ±1.1% with P/C 4.89 = hedged/fear** · **`XLI` ±1.1% with P/C 0.54 =
complacent** · `XLE` ±1.6% · `XLB` ±1.2% (P/C 0.26) · `XLV` ±1.5% · `GD` ±1.4% · `ANET` ±3.0% ·
`HPE` ±4.2%. ★ **The stateable asymmetry: utilities are heavily hedged into tonight and industrials
are not.** ⛔ **`XLK` returned ±8.8% on a D1 expiry — implausible for a mega-cap sector ETF. DISCARDED
as a thin-chain artifact; no ticket rests on it.**

## 3 · The registered brackets this run added (full text in `handoff/SCENARIOS_US.md`)

| ID | Observable | A | B | Settles |
|---|---|---|---|---|
| **S80** | EW{`XLU`,`XLRE`,`XLP`} **4-session** excess vs `SPY` | **≥ +1.85pp** (against us — three UWs wrong together) | **≤ −2.29pp** (first multi-session confirmation) | **2026-08-19** |
| **S81** | EW{`AVGO`,`ANET`,`HPE`} **2-session** excess vs `SPY`, NVDA **excluded** | **≥ +3.66pp** | **≤ −2.86pp** (the book's 4-of-11 concentration is ONE loss) | **2026-08-27** |
| **S82** | [`XLV` 5-session exc] **minus** [EW{XLU,XLRE,XLP} 5-session exc], both vs `SPY` | **≥ +2.45pp** (idiosyncratic med-tech leg) | **≤ −1.62pp** (HLTH is the 4th duration leg) | **2026-08-20** |
| **S83** | [`ANET` 5-session exc] **minus** [`HPE` 5-session exc], both vs `SPY` | **≥ +7.16pp** | **≤ −9.68pp** | **2026-08-20** |

⚠ **Correlated-tail flags, so nothing is double-counted**: **`S82`-B and `S80`-A are the same
underlying event** (the duration complex rallying and dragging XLV with it) — if both fire that is
**ONE regime read**. **`S81` and `S79` are correlated by construction** — same event, two lenses.

## 4 · The tape-independent core-starter — the cycle GAP

**PREMORTEM Lens 4 found a rank-2 flow sector at 0.00% of the book: HEALTH CARE**, unregistered in
`data/cycles/cycle_registry.json`, **so no GAP could ever fire.** The standing rule is explicit: a
crowded or distributing tape **gates ADD TIMING; it never justifies 0% core in a top-rank cycle.**

**Cleanest expressions, each with the Lens-2 caveat attached** — they may *be* the duration factor,
and **`S82` settles that on 2026-08-20**:
**`BMY`** (OBV +0.590 · FINRA **z −2.61 shorts actively exiting** · exc60 **+8.24 = least extended**) ·
**`REGN`** (highest flow in HC · **rs60 only +9.8** = accumulation without the 60-day move) ·
**`ABT`** (**highest OBV of all 300, +0.691** · at its own 19-yr median margin · FY breadth 19↑/2↓) ·
**`BDX`** (**1.5pp below its own 19-yr median margin on a 13.87 forward** · freshest 5-day leg +7.22).
⛔ **`BSX` is explicitly EXCLUDED from the starter** despite the best exc5 in the leg — **FINRA z
+3.95, 5v5 +11.7▲: the rise is short fuel.** `ISRG` carries the same signature.

⚠⚠ **The honest limit on this starter, stated here rather than discovered later**: **no Health Care
print lands inside either bracket window** (`S76` → 08-19, `S82` → 08-20) ⇒ **both settle on tape
alone, with no fundamental event to attribute a move to.** And the leg's **customer node is
🔴FADING** — `hospital capex` returns **2 articles in 90 days**, while hospital capex/revenue is
**below its Q4-2025 peak at 4 of 4 operators measured (THC −58%)**.

## 5 · What is NOT armed, and why

- ⛔ **No ticket on `NEM`, `HPE`, `TMO`, `WAT` or `ALL`** — all tagged **🔴RESOLVED** by ALPHA §B-3.
- ⛔ **No ticket on `DELL`, `CSCO`, `BSX`, `ISRG`** — ⚡ crowded-short; **squeeze fuel is never a
  standalone entry**, and a hard stop is stamped on any future consideration.
- ⛔ **No ticket on `EA`** — **it is not a trading security** (`R56`, day 29).
- ⛔ **No ticket sized from `kelly_size --ic`** — G6 FAIL, so no such figure is evidence-backed.
