# SWEEP_READ — industry_US — 2026-07-30 (Thu)

> The **reading**, not a second copy of the data. Numbers live in
> `llm_outputs/2026-07-30/industry_US/SECTOR_FLOW_US.json` (§`sector_rotation`, §`names`) and
> `US_LIVE_SHORTLIST.json`. **No sector row or per-name row is reprinted here** — only what the JSON
> cannot say. Benchmark **SPY** inline on every relative number (C1).

## 0 · ⚠ D74 FIRED — and was remediated IN-RUN, before any downstream stage read the artifact

The first sweep pass stamped **`asof 2026-07-30`** on a bar taken **~40 minutes into a live US
session**, and **wrote that snapshot into `llm_outputs/sector_flow/history.json`** — the baseline every
future `new_green` diffs against. Executed, not logged:

1. `prices_2026-07-30.pkl` backed up → trimmed **85 → 84 rows (≤ 2026-07-29)**;
2. `history.json` backed up → the **`2026-07-30` key removed**;
3. sweep re-run on the trimmed cache → **`asof 2026-07-29`, n=300.**

★ **This is the 3rd US instance and the 2nd caught pre-read. And it produced a genuine improvement**:
`history.json`'s prior key is **2026-07-28**, so today's `delta` / `new_green` is a **true
one-session diff for the first time in three runs** (07-28 and 07-29 both ran on a two-calendar-day
base). **Any comparison of today's ignition count against those two runs is therefore not
like-for-like, and that is stated rather than assumed away.**

⚠ **A second, new instrument defect was hit and fixed in-run — logged as D105.** Writing the sweep's
stdout through the shell added a **UTF-8 BOM**, and `us_live_shortlist.py` reads with
`encoding="utf-8"` ⇒ **`JSONDecodeError` on the desk's own artifact**, i.e. the P1 chain
(sweep → shortlist) breaks on a byte the producer added. Stripped, then the shortlist ran.

## 1 · Universe headline (3 numbers)

**n = 300 · wflow +0.15 (cap-weighted mean of the 11 sector rows) · 🟢 41 / 🔴 60, with 29 new-🟢.**
Against the 07-29 run's **17🟢 / 61🔴**. ⇒ **the green count went 17 → 41 in one settled session** —
and §2c shows that **a third of that jump is an instrument state change, not a market change.**

## 2 · Cross-checks against the MACRO transmission matrix

### 2a ★★ MATERIALS — the sweep does not confirm the UW; it **refutes the evidence the UW rests on**

**S36 branch A's second leg — *"the green count is still 0"* — is measured this run to be an
instrument artifact, decisively.** Of Materials' 12 names, **5 pass the `OBV-accumulation ∧ RS20 > 0`
pre-condition and ALL 5 are blocked from 🟢 by `vol_surge` alone**; the **highest `vol_surge` in the
sector is 1.14 against a 1.20 gate.** Nothing about Materials is being measured by that zero.

And the axis that *is* A-grade points the other way: the sector's top three flow scores carry
**positive RS20 AND positive RS60 vs SPY** (`SECTOR_FLOW_US.json §names` — NUE, STLD, CTVA), and
**eqflow +0.142 is POSITIVE while wflow −0.031 is negative** — the only sector on the board with that
sign pattern. ⇒ **breadth is positive and the mega-caps (LIN, NEM, FCX) are the drag.**

⇒ **This is exactly the L3-bis failure M238 pre-registered a warning about**, and it has now happened:
**S36's leg can settle on the gate rather than on Materials.** Handed to ROTATION as
*"the UW's third failed deferral, now with its own confirming evidence disqualified"* — **not** as a
reason to flip a tilt, which is ROTATION's call.

### 2b ★★ COMM SERVICES — the sweep contradicts the N− at the sector level and names the drag

**eqflow +0.278 > wflow +0.123** — a **breadth-led** sector wearing a mega-cap-narrow verdict, and the
gap's sign is the opposite of Info Tech's. **3 greens; the only 🔴 in the sector is GOOG**, with GOOGL
the sole other negative-RS20 name.

⇒ **S16's own question is answered on the flow axis before its price observable settles**: the COMM
weakness is **Alphabet's**, and **META is 🟡 with a positive RS20** rather than a red. ⚠ **This does
NOT score S16** — that bracket is an RS20 spread to 08-12 (MACRO §E has it tracking branch B) — and the
two axes currently **disagree**, which is the finding, not a resolution (**C4**).

### 2c ★★★ The 🟢 gate's ARITY changed again — and it manufactured 13 of today's 41 greens

**`velocity` is non-null on 50 of 300** today, against **0 of 300 on 07-28** (M237) and **50 of 300 on
07-27** (M203). ⇒ the gate is a **3-of-4 vote** today and was **3-axis unanimity** yesterday. **D75's
state-dependence is confirmed a second time, on the third distinct state.**

Measured consequence: **13 of the 41 greens carry `vol_surge` below the 1.20 gate and cleared on the
velocity path** — among them **MSFT (0.82), AAPL (0.87), JPM (0.85), MA (0.75), V (0.88), XOM (0.87),
CVX (0.83), JNJ (0.96), LLY (0.68)**. ⇒ **had `velocity` been null as it was yesterday, today's count
would be 28, not 41.** Any "ignition breadth exploded" reading must subtract this first.

**The blocked side replicates an EIGHTH time and is unaffected by the arity change**: **84 of 84**
pre-condition names blocked from 🟢 are blocked **by `vol_surge` alone**, and the **highest
`vol_surge` among all 84 is 1.16** against a 1.20 gate. Two markets, eight dates ⇒ code structure.

### 2d · UTILITIES — the sweep CONFIRMS the sector UW and CONTRADICTS its uniformity

Utilities is **the only sector negative on BOTH wflow and eqflow**, which is the strongest single
sector-level confirmation on the board. **But the four 🔴 are two AI-power names and two regulated
names, and four regulated names carry positive RS20** — so the sweep reproduces the same
**two-legs-one-label** split MACRO §E measured on price, from an independent axis.
★ **Cross-provider agreement worth recording (D5)**: the regulated-seven median RS20 vs SPY computed
from this JSON matches the independent yfinance computation in MACRO §E to **0.01pp (+0.4 vs +0.39)**
⇒ **S35's observable is not a provider artifact.**
⚠ **D (Dominion) carries the sector's lowest `vol_surge` (0.48) with positive RS20 and RS60** —
accumulation on no volume, which is why it is 🟡 and not 🟢. Unchanged from its registry row.

### 2e · INFO TECH — the sweep confirms MACRO's P3 on the widest margin on the board

**wflow +0.085 against eqflow −0.195 = a 0.280 gap, the widest of the 11**, with **32 of 56 red — more
reds than the next three sectors combined.** ⇒ the mega-caps are holding a sector whose breadth is
negative. ★ **And the four IT greens are the tell, not a counter-argument**: three of them (AAPL,
MSFT, PLTR) cleared on the **velocity** path (§2c) and the fourth (NOW) is not a memory name. **There
is still no 🟢 anywhere in memory or semi-equipment** — M246's observation replicates a 2nd run.

### 2f · HEALTH CARE — C7's resolving observable prints non-zero for the FIRST time, with a caveat

C7's registered resolver is *"one 🟢 from OUTSIDE the top-6 by cap."* Measured on this JSON: the
Health Care top-6 by market cap is **{ABBV, AMGN, JNJ, LLY, MRK, UNH}**, and **two greens sit outside
it — TMO (flow +0.88, the sector's #1) and HCA (+0.61, `new_green`).**

⚠⚠ **Stated rather than claimed as a resolution (C5 — the choice is arbitrary and the two versions
disagree):** the **desk's named block** in `STANDING_VIEW_US §3a` is **{LLY, JNJ, ABBV, MRK, TMO,
UNH}** — it contains **TMO and not AMGN**. **Under the desk's own list, TMO is INSIDE and only HCA is
outside; under the cap ranking, both are outside.** ⇒ **C7 reads "1 or 2, depending on an undocumented
definition."** **The definition must be fixed by a human before this is scored** — the sweep's job here
is to show that the number is no longer unambiguously zero, and that the ambiguity is the desk's, not
the market's.

### 2g · ENERGY — the sweep is the board's #1 on BOTH axes, and the cycle flag says the book is short of it

Energy leads on **wflow (+0.558) and eqflow (+0.477)** with **3 greens and breadth 0.190**.
Against that, `cycle_exposure` flags **🚨 GAP on the rank-2 Energy cycle: epicenter 6.88% vs a required
8.0% (−1.119pp)**, held epicenter now **{MPC, PSX}**.
⚠ **BKR is the sector's #1 flow score (+0.93, `new_green`, delta +0.56) and it is ON THE REJECT LEDGER**
(`A.flow미도착`, filed 07-27, **recheck 2026-08-14**). Its stated rejection basis — *"the only negative
flow score of 11 Energy names"* — **is now false on the settled tape.** ⚠⚠ **It is NOT resolved early**:
its recheck date has not arrived, and pulling it forward on one session is the S1 error. **Named here
so the 08-14 audit cannot claim it was unforeseen**, and flagged to PREMORTEM.

### 2h · REAL ESTATE — the board's best breadth, and the three names R7 fought over turned together

**breadth 0.330 = best of 11, 4 greens, ZERO reds.** ★ **AMT, DLR and CCI all flipped to `new_green` in
the same session**, with the board's largest deltas (+0.70 / +0.50 / +0.82) — and **all three still
carry NEGATIVE RS60 vs SPY**, i.e. this is a **turn off a weak base**, not a continuation.
These are precisely the three names **R10/M131** re-clustered (AMT and CCI into duration, DLR into the
data-centre unit) — **and they turned on the same day, which is what the re-clustering said should NOT
happen.** ⚠ Recorded as a contradiction for PREMORTEM, **not resolved here**: n = 1 session (**S1**).

## 3 · Shortlist composition — the absences, each diagnosed

`US_LIVE_SHORTLIST.json`: **15 names, mcap ≥ $10B, 🟢 only, top-15 by flow score** (cut at **+0.79**).
The names are in the JSON; what follows is what the JSON cannot say.

- ⚠⚠ **The single most important fact about this list is structural, and it is new: 0 of 15 names came
  via the velocity path, though 13 of 41 greens did.** Every velocity-path green scores **≤ +0.71**
  because its `vol_surge` is below the gate, and the top-15 cut sits at **+0.79**. ⇒ **the shortlist is
  arithmetically incapable of surfacing a velocity-path name** — so **MSFT, AAPL, XOM, JPM, MA, V, CVX,
  JNJ and LLY were all excluded by construction, not by judgement.** **This is a filter artifact of
  exactly the class the stage doc warns about, and it has never been named before.**
- **Info Tech: 0 of 15.** Diagnosed: **artifact.** IT has four greens; the best (NOW, +0.75) sits below
  the cut, and the other three are velocity-path.
- **Materials: 0 of 15.** Diagnosed: **artifact, twice over** — 0 greens exist, and §2a shows the 0 is
  itself a `vol_surge` artifact.
- **Comm Services: 0 of 15.** Diagnosed: **artifact** — three greens exist (best +0.78, one basis point
  under the cut).
- **Energy: 1 of 15 (BKR).** Diagnosed: **partly real, partly artifact** — the sector's other two
  greens are velocity-path.
- **Utilities: 1 of 15 (PCG).** Diagnosed: **evidence.** The sector has exactly one green and it is the
  same name it has been for three runs; nothing is being hidden by the filter here.
- **Financials: 3 of 15 (BX, TRV, MRSH) from 8 greens and 32 pre-condition names — the deepest
  accumulation base on the board (24 blocked names, the most of any sector).** Diagnosed: **real, and
  under-represented** — the sector's other greens (JPM, MA, V, BAC, MET) are velocity-path.

**Clean-rise names (🟢 ∧ low-short / short-covering), from the FINRA proxy**: **GRMN · MDLZ · PLD ·
GD · NSC.** ⚠ **The US has no investor-type feed** — this is a short-pressure proxy, **context, never a
trigger** (D6), and `us_flow`'s own output says so.

## 4 · Cycle-exposure GAP — handed to ALPHA

- **AI-compute (rank 1): 12.98% vs a 12.0% floor ⇒ ✅, margin +0.98pp.**
- **Energy (rank 2): 6.88% vs 8.0% ⇒ 🚨 GAP, −1.119pp.** Held epicenter **{MPC, PSX}**.
- Missile-defense (rank 3): 7.9%, no floor set ⇒ ⚪ n/a.

⚠⚠ **The important reading is not the flags, it is that they moved with nothing traded — a NINTH
consecutive mark-to-market reading.** The AI-compute margin over its floor has now run
**−0.001 → +0.252 → +0.254 → +0.136 → +0.011 → −3.447 → −3.769 → −3.683 → +0.980pp** with the held set
(**AVGO, NVDA, TSM**) **unchanged throughout** — and this run's flip from 🚨 to ✅ happened on a session
when **NVDA fell 3.55% and AVGO 2.78%**, i.e. **the numerator fell and the flag improved**, because the
book's total fell faster ($11,575 → $10,654). **The metric is dominated by its denominator.**
★ **Energy's GAP widened for the same reason, in the same direction**: −0.277 → −0.327 → **−1.119pp**,
and **XOM has dropped out of the held-epicenter set** (07-29 read {PSX, XOM}).
⇒ **Handed to ALPHA as a flag whose movement is not information.** ⚠ **And M252 still binds: TSM and
LNG are outside `us_top300`, so a material part of the book carries no flow, RS or short read at all.**

## ✅ EXIT CHECK

- [x] Sweep done → `SECTOR_FLOW_US.json` (**asof 2026-07-29** after in-run D74 remediation); sector
      ranking and the 29 new-🟢 read.
- [x] `US_LIVE_SHORTLIST.json` written; FINRA short-pressure verdicts read and labelled as a proxy.
- [x] `CYCLE_EXPOSURE` GAP read (🚨 Energy −1.119pp) and handed to ALPHA, **with the finding that its
      movement is denominator drift**.
- [x] **No table that exists in the JSONs is reprinted here.** Every per-name and per-sector figure is
      either cited by artifact or used inside a cross-check that the JSON cannot express.
- [x] **Cross-checks that confirm or contradict the MACRO matrix, with the side the money is on**:
      **contradicts** Materials UW (§2a) and Comm Services N− (§2b); **confirms** Info Tech's split
      (§2e) and Utilities UW at sector level while contradicting its uniformity (§2d).
- [x] **Shortlist absences read and each diagnosed as evidence vs filter artifact** (§3) — including a
      **new structural artifact**: the top-15 cut excludes every velocity-path green.
