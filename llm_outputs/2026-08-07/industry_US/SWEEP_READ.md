# SWEEP_READ — industry_US · 2026-08-07 · asof **2026-08-06 settled**

> The numbers live in `SECTOR_FLOW_US.json §sector_rotation / §names` and `US_LIVE_SHORTLIST.json`.
> **This file reprints none of them.** It holds the three things the JSON cannot say.

## 0 · ⚠⚠ D74 handled BEFORE the sweep ran, not after — and the trim is stated

**The US market was OPEN (09:39 ET, 9 minutes in) when this stage started.** A raw `sector_flow` run
would have set `asof = 2026-08-07` off a 9-minute partial bar and **saved that snapshot as the
baseline every future `new_green` diffs against — D184's fourth occurrence.**

⇒ **The price cache was pre-built truncated to 2026-08-06 and `sector_flow` reused it.** Verified:
`asof 2026-08-06`, and **`llm_outputs/sector_flow/history.json` carries no 08-07 key.**
**Measured size of what was excluded**: SPY's partial bar held **9.05% of the prior session's volume**
(the 08-06 run's pre-open bar held a 2.61% median) and printed **771.01 vs the 768.56 settle** — so
this contamination was **3.5× heavier** than the one that inverted four sectors' flow sign in M419.
⇒ **the trim was pre-emptive, and it is the right way round: prevent the orphan rather than delete it
by hand afterwards.**

## 1 · Universe headline — three numbers

**n = 300 · wflow +0.127 · 27🟢 / 78🔴.**
Against the 08-05 sweep (**+0.175 · 28🟢 / 69🔴**): **the level fell, greens held, and reds rose by
nine.** ⇒ **breadth deteriorated while the headline barely moved** — the sort of divergence that a
single wflow figure hides.

## 2 · ★★★ Cross-checks against the MACRO matrix — three contradictions, two confirmations

### 2a · 🚨 **Energy — the sweep CONTRADICTS the level, on the exact metric the downgrade was re-argued onto**
The 08-06 ROTATION cut Energy **OW− → N+**, and **R51 retracted its stated reason** (the wflow/eqflow
gap = an arithmetic identity), replacing it with *"the informative number is **Δ −0.129, last of 11**,
and it is the refiners' own."* **That number is now +0.196 and Energy is rank 1 on BOTH axes with
eqflow POSITIVE for the first time since the cut.** ⇒ **the replacement reason has reversed on its own
metric in one session.** ⚠ **n = 1 (S1)**, and it is the session WTI rose +2.75%. **ROTATION owns
whether that is a change or a bounce — it may not be waved through in either direction.**

★ **And the intra-sector mis-tag the 08-06 ROTATION explicitly declined to act on is now WIDER, not
narrower.** Energy's only two 🟢 are **XOM and CVX, both velocity-lit with `vol_surge` below 1.03**,
while the names carrying the 60-day money — **VLO · MPC · PSX · COP · OXY, RS60 −2.9 to +18.2, four of
five OBV 매집** — are all 🟡. **The sector's largest positive deltas belong to the 🟡 names (OXY, COP,
VLO), not to either 🟢.** ⇒ **the tag filter is pointing at the two names MACRO §0-c says do NOT book
the export rent.** DEEP-ENRG owns it.

### 2b · 🚨 **Financials — the sweep CONTRADICTS the OW promotion, and this is R50's prospective test**
R50 retracted the leg that carried **FIN OW− → OW** by showing the `velocity` axis blinks and FIN's
breadth tracks it 1:1. **The axis did NOT blink this run — it stayed on (51 → 50 names) — and FIN's
numbers fell anyway**: rank 1 → **rank 2** on wflow, eqflow down, breadth down, and **Δ is negative**.
★★★ **And one of the five `new_green`s the promotion cited has fallen out of the green set entirely:
WFC is now 🟡 with RS20 −1.5 and the sector's most negative delta among the five.** Three of the four
survivors (JPM `vol_surge` 0.68 · BAC 0.74 · BRK-B 0.86) **are still velocity-only.**
⇒ **R50's diagnosis is confirmed prospectively, on a run where the artifact it named was absent.**
Combined with MACRO §0-b (the bull-steepener disarm), **Financials is the single most exposed tilt on
the board and both of its legs are now measured against it.**

### 2c · 🚨 **Communication Services — the sweep CONTRADICTS the UW**
**eqflow EXCEEDS wflow** (breadth-led), **breadth is 2nd of 11**, and **both of its 🟢 are `new_green`
(DIS, EA)** — **the only sector on the board with two fresh ignitions, out of five board-wide.**
⚠ **EA's `vol_surge` is 3.78, by far the highest of any green** — a volume event, not a drift.
⇒ **the desk carries UW on the sector that just produced 40% of the board's new ignitions**, while its
two named UW reasons have both decayed (**P28′**: the Alphabet thread ENDED and GOOGL's exc5 turned
positive; the new Meta legal event has no observable). **ROTATION must answer this rather than carry
it.** ⚠ **C2, the other half: GOOGL is 🟡 with RS20 −2.6 / RS60 −11.9 and META is 🔴분산** — the two
largest names in the sector are not what lit it.

### 2d · ✅ **Utilities — the sweep CONFIRMS the UW, harder than the matrix claims**
**0🟢 / 9🔴 of 15, breadth 0.000**, and its wflow sits **0.347 below the next-worst sector.** ⚠ Its
**Δ is marginally POSITIVE**, which is recorded so the next run reads it as a second observation
rather than a first — **the same discipline the 08-06 ROTATION applied when it declined a Staples
promotion on a one-day delta.** ★ Internal split intact, and stated **A-grade first (D6)**: on RS20 /
RS60 vs SPY, **CEG reads +1.9 / −16.8 with Δ −0.378** while **PCG reads −3.3 / +0.9 with `vol_surge`
1.57** — the C-grade OBV axis (CEG 분산, PCG 매집) **agrees with that ordering rather than carrying
it**. ⇒ the regulated leg is still being bought while the AI-power leg is sold (W5).

### 2e · ✅ **Information Technology — the sweep CONFIRMS the N**
**eqflow is NEGATIVE against a positive wflow, with 24🔴 of 56 — the worst red count on the board.**
⇒ mega-cap-narrow, which is exactly what a Neutral that "does work rather than hedge" should look
like. ★ And the two names P27′ is long — **NVDA (`vol_surge` 0.91, velocity-lit, RS60 −4.2)** and
**ANET (surge 1.40, RS60 +37.0)** — **sit on opposite sides of the volume gate**, so the supplier leg
is not one object.

### 2f · ⚠ **Health Care — the sweep pushes N upward again, through the same flaw that produced R49**
HLTH now carries **the board's highest breadth (0.160) with 5🟢/5🔴 and two `new_green` (WAT, MRK)**.
⇒ **the same "promote HLTH on breadth" pull that R49 withdrew yesterday is back one day later.**
⚠⚠ **And the flaw is present again: MRK's green is velocity-only (`vol_surge` 0.91).** WAT's is
volume-lit (1.21). ⇒ **any promotion argument must decompose the five greens by axis first** — the
interim rule from §9 of HANDOVER, binding here.

## 3 · Shortlist composition — the absences, each diagnosed

`US_LIVE_SHORTLIST.json`: 15 names, filter `mcap ≥ $10B ∧ 🟢가속 ∧ flow desc top-15`.

**Four sectors produced ZERO shortlist names. They are not the same kind of zero:**

| Sector | Zero because | Verdict |
|---|---|---|
| **Utilities** | 0🟢 of 15 with 9🔴 and breadth 0.000, worst wflow by 0.347 | **EVIDENCE** — the absence *is* the signal |
| **Materials** | 0🟢 — but **NUE (RS20 +20.1, OBV 매집) and STLD (+15.5, 매집) are blocked by `vol_surge` alone (1.01 / 0.88)** | 🚨 **FILTER ARTIFACT.** This is the M422 / C9 gate mechanism on the exact two issuers M435 measured a rising metal spread for. **The Materials N− may NOT cite "no greens" as evidence** |
| **Real Estate** | 0🟢, but also only **1🔴 of 12**, with wflow −0.025 and eqflow +0.003 ≈ flat | **NEITHER.** The sector has no signal in either direction ⇒ `unknown` (**C3**), not confirmation of the UW. ★ **DLR is 🟡 with OBV 매집 and RS20 +5.1, blocked by `vol_surge` 0.67** |
| **Consumer Staples** | 0🟢 / 4🔴; **wflow positive but eqflow NEGATIVE**, and **Δ is the 2nd-highest positive on the board** | ⚠⚠ **THE SECOND OBSERVATION THE 08-06 RUN ASKED FOR.** It declined a Staples UW → N− promotion because *"the only carrier is a one-day delta = n ≈ 1"* and recorded that the next run's delta should be read as a second observation. **It is again high, and the levels are again split.** ⇒ **ROTATION owes this an answer, not a third deferral** |

★ **Energy contributes exactly ONE name (CVX)** — and only because the `--top 15` cut excludes XOM at
flow-rank 17. ⇒ **for the second documented time the refiners are absent from an Energy shortlist as a
🟢-tag artifact, not as evidence** (the measured precedent is in this stage's own field notes).

**Short-pressure read (FINRA z, B-grade, confirmation only — never a standalone):**
**5 clean-rise (✅ low-short / short-covering): BMY · PH · ETN · AME · MA.** **2 crowded-short
(⚡ squeeze fuel, turn-conditional, NOT a buy): MSFT · IDXX.**
★★ **AME at z −2.03 is the single strongest short-collapse on the pull, and it is one of S62's four
INDU legs — on the day S62 settles.** Named so BET does not discover it late.

## 4 · ★★★★ Instrument finding — the mechanism behind R49/R50/D183 is NOT what the desk wrote, and the correction makes the defect PERMANENT

The 08-06 run measured, and **R49 was retracted on**, this statement:

> *"`velocity` is populated on **EXACTLY universe mcap-ranks 1–51, zero exceptions** (rank 51 RTX
> populated, rank 52 C `None`)."*

**Measured on both files this run:**

| Test | Result |
|---|---|
| Is `names` sorted by market cap? | ❌ **No** — verified false on **both** the 08-06 and 08-07 files |
| Is `names` sorted by `flow_score` descending? | ✅ **Yes**, on both files |
| Velocity-populated set, 08-06 vs 08-07 | **51 vs 50 names, overlap 50. The only difference is RTX dropping out** |
| Today's populated positions | **2, 7, 13, 14, 17, 23, 45, 49, 52, 59, … 293, 294** — non-contiguous, spanning the whole array |
| Cap of a "rank 294" member | **ASML $744bn.** Position 113 is **AAPL, $4.38 trillion**; position 263 is **TSLA, $1.50tn** |

⇒ ★★★ **"mcap-ranks 1–51" was a misreading of the array's ordering.** Those were **flow ranks**, and
on 08-06 the flow ordering happened to place the velocity-covered mega-caps in the top 51 — RTX sat at
flow-rank 51 that day and at flow-rank 31 today, **with no velocity either day's rule would predict.**

★ **What this does to R49: the VERDICT survives, the stated MECHANISM is corrected — and the corrected
version is stronger.** R49's conclusion was *"the property was a coverage boundary, not a sector
characteristic,"* and that is confirmed: **AMGN, BMY and IDXX carry no velocity today either.** But the
boundary is a **stable ~50-name coverage whitelist**, not a rank cutoff. ⇒ **a sector whose names sit
outside that list can NEVER produce a velocity-lit green, on any run** — the "🟢 means two different
things" defect is **structural and permanent**, not run-dependent as D183 implied.
⚠ **And it changes what a fix must do.** D183 proposed guarding the axis count; **the real defect is
that the gate is name-conditional**, so a run-level guard cannot see it (which is exactly why all four
of R50's runs stamped `"news"` and passed). **Registered as `D205`; the code change stays human-gated
(P5).**
⚠ **C4 scope**: this does **not** retract R49, R50 or D183's cost measurements. It corrects one
sentence of mechanism inside them, and the correction was only findable because the array was
re-tested rather than re-quoted.

## 5 · Cycle exposure — ✅ no GAP, and two registry defects still open

`cycle_exposure.py --json` → **no rank≤2 GAP**: AI-compute epicenter **23.67% vs a 12.0% floor**
(AVGO · NVDA · ANET · TSM); Energy/refining **10.06% vs 8.0%** (MPC · PSX).
⚠ **D189 unchanged, both halves**: the rank-2 cycle's NAME still reads **"(Hormuz + Russia crack)"** —
an **R46** violation now contradicted by the object's own operator (**M418**) *and* by MACRO §0-c,
which names a **third** object (US export drain) the registry does not contain; and **rank 3
(missile-defense) has no `min%`, so it renders ⚪ n/a and is inert by construction.**

## 6 · Ledger actions owned by this stage

**None due.** Both `reject_ledger.py due` and `missed_ledger.py due` returned empty at HANDOVER
(0 legacy, 0 recheck-date). The 08-06 run's one in-run deferral (**JNJ**) was **resolved `revived` on
08-06** and is verified in `out/reject_ledger_resolutions.jsonl`. ⇒ **nothing is carried silently.**
