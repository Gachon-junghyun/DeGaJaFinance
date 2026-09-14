# BLINDSPOT_PREMORTEM — industry_US — 2026-08-02 (Sun) ★US-only

> Phase 1.5. **Four adversarial lenses argued AGAINST our own tilt, in parallel, BEFORE the deep budget
> was committed.** Anti-tunnel. Every number below carries its benchmark inline (RS is excess vs SPY);
> OBV and the 🟢🟡🔴 tag are C-grade and never carry a claim alone (**D6**).
> Analysis only, zero buy/sell, zero sizing (P4).

---

## 0 · Method limitation, stated at the top rather than buried

⚠ **This run's sweep has `velocity` null on 300/300**, so the 🟢 gate reduces to `vol_surge ≥ 1.2`
and **69 of 85 accumulation candidates are blocked by that single axis** (SWEEP §5). **Every lens was
handed this caveat and none of them read a 🟡 tag as weakness on its own.** Confirmed independently
this run: **`module_flow MPC` returns 🟢가속 on news velocity 2.35× at the same date the sweep returns
🟡, because the sweep's velocity column is empty.** ⇒ **The Energy 🟡 wall is definitively an
instrument state, not a market verdict.**

⚠ **Two of the run's most load-bearing lens findings were re-verified by hand against an independent
yfinance pull before being written here** (TRI/ETN/MU/NVDA/AVGO/AMAT/LRCX/KLAC `rs20`,`rs60`). They
reproduce to ≤0.5pp. **A lens's number was not taken on trust.**

⚠ **The default expectation is that at least one lens surfaces something the deterministic desk
missed. All four did, and three of them attacked decisions taken earlier in THIS run.**

---

## 1 ★★★ · The lenses attacked this run's own verdicts — and these are the findings, not the footnotes

### 1a. ROTATION's Industrials promote rests on 5 greens, and **2 of the 5 have NO 60-day base**

Lens 3 applied the desk's own **M149/M150** method — *days-21-to-60 excess = rs60 − rs20* — to the
five 🟢 names ROTATION cited when promoting **INDU UW− → N**:

| Ticker | rs20 vs SPY | rs60 vs SPY | **days 21-60** | verdict |
|---|---|---|---|---|
| **RTX** | +7.7 | **+21.3** | **+13.6** | base is real |
| ITW | +4.9 | +9.5 | +4.6 | thin but real |
| GD | +2.3 | +6.6 | +4.3 | thin but real |
| ⛔ **TRI** | +9.7 | **−0.4** | **−10.1** | **NO BASE — a pure 20-day event** |
| ⛔ **ETN** | +3.9 | **−2.2** | **−6.1** | **NO BASE — and its `new_green` delta (+1.329) is a single earnings-day beat** |

⇒ **The breadth is real in flow terms (eqflow +0.048 above wflow, 5🟢 of the board's 16) and it is
NOT equally real on the continuation axis.** ROTATION's stated DEEP mandate was *"early or trap"* —
**this narrows it: the trap risk is concentrated in TRI and ETN, and DEEP-INDU must report the
3-of-5 split rather than the 5.** ⚠ **The promote is NOT reversed here** — a flow-carried delta is
this stage's to attack, not to overturn — but **it may not be quoted downstream as "5 greens."**

### 1b. EVENT_ALPHA handed STX forward and dropped MU — **on the desk's own base test the ranking inverts**

| Ticker | rs20 | rs60 | **days 21-60** | this run's treatment |
|---|---|---|---|---|
| **MU** | −15.9 | **+25.3** | ★ **+41.2 — the strongest base in the basket** | ⛔ **explicitly NOT handed forward** (🔴분산, flow −0.600) |
| **STX** | +4.1 | +7.8 | **+3.7 — one of the thinnest positive readings on the board** | ✅ handed forward as CONFIRMED-EARLY |

⇒ **The desk carried the name with direction and dropped the name with the base.** Both readings are
defensible on their own axis — **STX has the A-grade 20-day turn and the flow; MU has the 60-day
foundation and neither** — and that is precisely why **`indistinguishable` (C4) is the honest verdict
and neither name may be quoted as "the memory turn."** ⚠ **W5 binds hard: this basket spans flow
+0.799 (STX) to −0.600 (MU) and RS20 +4.1 to −30.7 (SNDK).**

### 1c. **"The equipment did not participate" was used as bearish evidence — on this method it reads bullish**

MACRO §D-P3 and SWEEP both leaned on AMAT/LRCX/KLAC failing to join the storage turn. Their bases:
**AMAT +36.5 · KLAC +25.0 · LRCX +19.9** (days 21-60, vs SPY). ⇒ **All three are pullback-inside-an-
uptrend by the desk's own arithmetic, not confirmation of a de-rate.** **P3's registered anti-signal
— *"the equipment three turning positive on RS20 while storage rolls over"* — is the test to watch,
and it has not been run yet.** The narration ran ahead of it.

### 1d. ★★ **The AI-compute epicenter — the book's largest conviction bucket — has no live base on 2 of 3 names, and is instrumentally blind on the third**

**NVDA rs60 −1.1** (flat to SPY over 60 days) · **AVGO rs60 −12.1** (net underperforming) ·
**TSM has no row in `SECTOR_FLOW_US.json` at all.**
⇒ **M146's finding — that the cycle-exposure ✅ has been mark-to-market drift with nothing traded —
is now corroborated from a completely independent direction (the RS-base test).** The rank-1 cycle
clears its 12.0% floor by **+1.02pp**, which sits **inside** that drift band.

### 1e. ⚠ **The lens's own reference case broke, and it is flagged rather than smoothed**

**AXON** — this desk's canonical decaying-stock shape (**R9**) — currently scores
**days 21-60 = +47.4 (rs20 −11.9 / rs60 +35.5)**, i.e. **EXTENDED-BUT-LIVE by the mechanical test.**
Either the reference predates today's tape, or **the test needs a magnitude floor on the rs20
drawdown** (a −11.9pp 20-day give-back is not nothing even when the base holds).
**Flagged, NOT resolved — new dig D127.**

---

## 2 · Lens 1 — UNDER-COMPUTED LEGS

| Leg | Names + numbers (vs SPY) | Dated catalyst ≤5 sessions | Verdict |
|---|---|---|---|
| ★ **Utilities / AI-power** | **CEG** flow +0.539, rs20 **+9.5** / rs60 −21.2, **delta +0.306** · **VST** flow +0.009, rs20 −2.2 / rs60 −10.8, **delta +0.573 — the sector's largest** · comps GEV −0.611 (delta −0.419) and VRT −0.233 | **CEG 08-06 · VST 08-07** | ★★ **PROMOTE-TO-DEEP** |
| Health-care compounders | **BMY** rs20 +12.0 / rs60 +11.5 · **REGN** +16.3 / +5.4 · **TMO** +9.4 / +19.8 · **ABT** +10.5 / +18.0 — **all four positive on BOTH windows**, all four blocked from 🟢 by `vol_surge` alone | ⚠ **none** — only the desk's internal C7 re-check 08-06 | **WITHIN-RUN-WATCH** |
| RE / data-centre REITs | DLR +8.5 / −7.4 · PLD +3.4 / −0.1 · **IRM +4.1 / −10.3, delta +0.623 (sector's largest)** · CBRE +3.4 / −0.2 | none in window (DELL/HPE guides land 09-04) | **WITHIN-RUN-WATCH** |

★ **The strongest pure PRICE signal in the whole un-slotted set is the health-care compounder basket
(4 of 4 positive on both windows) — and it has no catalyst.** That asymmetry is stated rather than
resolved: **the leg with the best signal is not the leg being promoted, and the reason is the
calendar, not the evidence.**

## 3 · Lens 4 — CYCLE EXPOSURE, and it converges with Lens 1 independently

| Cycle | Rank | Epicenter % | GAP | Cleanest UN-HELD epicenter expressions |
|---|---|---|---|---|
| AI-compute / semis | 1 | **13.02%** vs 12.0% floor | ✅ (margin **+1.02pp** — inside M146's drift band) | **ANET flow +0.628, rs20 +12.4, delta +1.093 — higher flow AND higher delta than either held name.** ⚠ its straddle expired 07-31, **before** its 08-04 print ⇒ not event-priced |
| **Energy / oil-refining** | 2 | **6.9%** vs 8.0% | 🚨 **GAP −1.10pp** | **XOM flow +0.606 — the highest flow of ANY Energy epicenter name, held or not** · **VLO rs60 +20.2 — the best 60-day of the refining group and the only refiner with a positive delta (+0.054)**. Both blocked from 🟢 by `vol_surge` alone (0.89 / 0.80 vs a 1.20 gate) |
| Missile-defence | 3 | 8.03% (RTX) | ⚪ no floor set | **GD is a second 🟢 in the same 5-name epicenter list, unheld: flow +0.546, rs20 +2.3 / rs60 +6.6** |

**Registry rows that DO NOT EXIST, ranked by the tape they fail to see:**
1. ⛔ **AI-security / agent containment** — **the #1 event of the entire foreign feed on 07-31 by
   outlet count (46 articles / 20 outlets)**, and **D20 means a 0% book exposure cannot raise a GAP
   because there is no row to raise it from.**
2. ⛔ **Yen intervention / BOJ duration channel** — **`theme_age` 5.31×, the fastest-accelerating term
   on the board**, on a quantified **¥8.45tn** intervention with an explicit US Treasury warning.
   **No registry row for an FX/duration channel exists at all.**
3. ⛔ **AI-funding / private credit** — CoreWeave repricing $2.6bn upward while IG OAS *tightened*;
   a margin-called AI fund down 67%; $15bn / $12.3bn / Blue Owl structures. **A distinct engine
   (cost of capital for the build-out) from the compute epicenter, with no row.**
4. ⚠ **A defect INSIDE an existing row: the AI-compute epicenter list names MU but not STX, WDC or
   SNDK** — i.e. **the registry names the wrong half of the memory node**, and the half it names is
   the one that is 🔴분산 at flow −0.600.

⚠⚠ **DEEP coverage vs the ranked cycles**: rank 1 ✅ (IT slot), rank 2 ✅ (ENRG slot),
**rank 3 (missile-defence) has NO dedicated mandate** — RTX and GD ride along inside DEEP-INDU only
by sector coincidence, and DEEP-INDU's stated question is capital-goods breadth, not rearmament.

★★ **Lens 1 and Lens 4 converged independently on the same un-slotted layer** (Utilities / AI-power,
CEG+VST, both printing inside 5 sessions) **without seeing each other's output.** That convergence is
the reason for the promotion in §6.

---

## 4 · Lens 2 — BOTH-SIDES BRACKETS (registered, frozen, indexed)

**ID collision check performed against EVERY existing row in BOTH files (the D76 class): highest
existing ID is S51 (US) / S47-KR (KR). S52 and S53 are free.** ⚠ **The shared-counter proposal for a
human now stands for an EIGHTH run.**

### **S52 — Iran: a dated Strait reopening vs resumed strikes on Iranian ENERGY INFRASTRUCTURE** · ARMED · → **2026-08-06**

**Why it is not a duplicate of S8.** S8 brackets the *generic* de-escalation on price-keyed branches
and is undated by construction. Today's post adds two things S8 never had: a **named precondition
structure** (deal → dated opening), and a **named alternative** — per CBS via the BBC, the cancelled
plan targeted **Iranian energy infrastructure specifically**, which is a supply shock with a
*different transmission* (fuel cost into INDU, not just crude level into ENRG).

| Branch | Frozen observable | Meaning |
|---|---|---|
| **A (against ENRG OW)** | A **dated** Strait-reopening term in a **primary text** — a signed-agreement text, an official US Treasury/State statement, or a direct Iran-government statement carrying a date or "effective" language. **NOT a headline paraphrase and NOT a repeat of the 08-02 conditional wording** | The war premium gets a falsifiable exit; **XOM · CVX · OXY · COP lose the leg S31 already says they are standing on** |
| **B (against INDU N and the P16 breadth read)** | A reported strike on **named** Iranian energy infrastructure (refinery, export terminal, storage/processing), corroborated by ≥2 independent outlets reading the **same** primary event — not rhetoric repeated | Supply shock the other way: ENRG OW gets a harsher confirmation while the **fuel-cost leg M91 names (UNP: ~8 of 12 revenue-growth points are fuel surcharge)** and the risk-on breadth read take the hit |
| **C** | Neither by 08-06 | S8 stays ARMED unchanged; no conclusion changes; rolls forward undated |

- **Starter lists** (rs20 / rs60 vs SPY, flow): **branch A rips against** OXY **+16.4 / −7.0** (0.556) ·
  COP **+14.7 / −5.5** (0.628) · CVX **+16.0 / −1.0** (0.600) · XOM **+13.1 / −2.9** (0.606) — the
  four with the largest 20-vs-60 gap, i.e. the most premium to give back.
  **Branch B rips against** UAL **−9.3 / +26.3** (🔴 −0.850) · DAL **−6.0 / +20.2** (🔴 −0.674) ·
  CAT **−15.7 / −13.1** (🔴 −0.589) · UNP **+3.2 / +7.4** (+0.436).
- **Implied move: NONE EXISTS and none is invented.** No straddle prices a Truth Social conditional.
  **Scored on primary text and event confirmation, never on price** — the same treatment S9/S51 get.
- **Information content: BOTH branches falsify a currently-held conclusion ⇒ symmetric, high
  information.** This is why it is written rather than dropped.
- **Invalidation**: an actual signed multilateral agreement supersedes this bracket entirely —
  re-register against a state-department verification standard rather than scoring A off a signature.

### **S53 — MPC (08-04) + PSX (08-05): the equity-EXECUTION leg S49 cannot see** · ARMED · → **2026-08-05**

**Why it fills the named gap.** **S49's frozen observable is the COMMODITY 5-session distillate-crack
change** — a market-level number that says nothing about whether MPC's or PSX's own **realised crack
capture** (hedging lag, turnaround downtime, inventory timing) tracks the spot. The 07-31 run dropped
a standalone bracket here on the reasoning *"S49 already owns the refining print"* — **true for the
commodity, false for company execution**, and **MACRO §0 and EVENT_ALPHA §10 both named this the gap
PREMORTEM must fill.**

| Branch | Frozen observable | Meaning |
|---|---|---|
| **A (confirmatory, LOW information)** | Guide/commentary describes sequential crack **capture** as stable-to-improving, consistent with the spot distillate crack | Only confirms what S49 branch A already assumes at the commodity level — **no conclusion changes** |
| **B (against us, INFORMATIVE)** | Guide/commentary flags margin **compression**, a hedging-timing lag against spot cracks, **or** unplanned turnaround/maintenance drag | New negative information **at the execution level S49 cannot reach** — threatens the ENRG OW's refining leg *independently* of whether the commodity crack holds |
| **C** | Mixed (one confirms, one compresses) | `AMBIGUOUS`. ⚠ **n≈1: the two prints are date-clustered (08-04/08-05) and are not independent samples** |

- **Implied moves, taken from the market and registered as a SEPARATE, LABELLED price-reaction test
  (the D28 fix — they are NOT inside the branch conditions)**: **MPC ±8.8%, expiry 2026-08-21 (D19) —
  COVERS its print.** **PSX ±5.3%, expiry 2026-08-07 (D5) — COVERS its print.**
- ★ **The positioning split is itself a finding**: **MPC's option book is internally contradictory —
  skew +33.0 (heavy downside-tail demand) against P/C 0.44 (call-dominant)** ⇒ `indistinguishable`
  (C4). **PSX's is coherent and bearish-leaning — P/C 1.25, the only fear profile on the desk's pull,
  PLUS FINRA short z +1.53, the only 🔴 short surge.** ⇒ **if branch B fires anywhere in this duo,
  PSX is the name already positioned for it.**
- **Information content: asymmetric in the useful direction — branch B can falsify, branch A can only
  confirm.**
- **Invalidation**: an M&A/restructuring announcement at either name ⇒ idiosyncratic, re-register.
  ⚠ **And if S49 branch B fires BEFORE these prints** (it is one session of its current rate away),
  **S49 owns the outcome and this bracket collapses to a name-level footnote — noted so a later stage
  cannot double-count them.**

### Binaries DROPPED, each with its information-content reason

| Candidate | Reason dropped |
|---|---|
| **AMD 08-04** | **Already owned by S50.** ⚠ Logged: its straddle is **±4.0% expiring 2026-08-03, D1 — BEFORE the print** ⇒ **no magnitude threshold is obtainable and none was invented.** S50's direction-only design anticipated exactly this |
| **ANET 08-04** | **Not a new bracket — an ANNEX candidate for S50.** ANET's **±11.3% (expiry 08-07, D5) now COVERS its print**, which was **not true at S50's 07-31 registration** (*"no options instrument covers this"*). **Recorded so the annex can be attached; S50 is NOT re-frozen by this stage** |
| **CEG · LNG 08-06 · VST 08-07** | **S35 · S47 · S24 · S40 already own this print cluster in full.** Ownership has not changed since 07-31 ⇒ a new bracket adds no falsifying power. ⚠ **The DEEP promotion in §6 is the correct response to this cluster, not another bracket** |
| **July NFP 08-07** | **S51 already owns the regime flip it threatens.** A headline payrolls axis without the curve reaction is the non-actionable shape (D6 class) |
| **July CPI 08-12** | **P1 (breakeven/real), S26 (HY) and S41 (IG) already own every transmission channel CPI would move.** No incremental falsifying power |

---

## 5 · The single biggest UN-BRACKETED regime-flip risk — and this stage does not bracket it either

**Japan.** `theme_age "yen intervention"` = **5.31×, the fastest-accelerating term on the entire
board**, against a **quantified ¥8.45tn (~$59bn) intervention**, a **US Treasury statement that it may
itself intervene**, and a wire-described **"rare Japan-Korea joint intervention"** called a *"new
normal in coordination."* **MACRO's P7 carries it with zero desk coverage — no bracket, no thesis.**

The mechanism matters because **it sits directly under the one thing propping up the FIN OW−**: the
30y-led steepening (**DGS30 +12bp, 30y−10y +5bp**) that **P1/P13 attribute entirely to *domestic* Fed
credibility.** If the intervention channel is real, that term-premium story is **at least partly
foreign-official selling** — a different and less durable driver. And the classic tail is a
**carry-trade unwind**: a discontinuous deleveraging in exactly the long-duration, high-beta
AI-momentum stack, with **VIX at 17.09 — down 17.3% on the very session the long end sold off** —
i.e. a market not paying for it at all.

⚠⚠ **It is deliberately NOT bracketed, and the reason is a rule, not an oversight: D22 is open —
there is no lag table**, so any threshold linking a JPY intervention print to DGS30 would be
fabricated. **Registering a bracket on an unmeasured mechanism is exactly the failure W2 punishes.**
⇒ **It is escalated instead: D22 needs a human, and until it is closed this desk's largest
regime-flip risk is un-scoreable by construction.**

---

## 6 · Injections — what this stage CHANGES, not just notes

### 6a. ★ DEEP set updated: a 5th slot is PROMOTED

**Final DEEP set (5): continuous = [ENRG, FIN] · rotating = [IT, INDU] · ★ promoted = [UTIL].**

**Reason, stated against the recency rule it overrides**: UTIL held the rotating slot on 07-31 and
ROTATION correctly benched it to avoid repeating the previous run. **Two independent lenses that
could not see each other's work converged on it anyway** — Lens 1 as the only un-slotted leg with a
dated catalyst inside five sessions (**CEG 08-06, VST 08-07**), Lens 4 as **rank-1's adjacent power
layer with no slot at all** — and the sector carries **two of the desk's own brackets that fired in
OPPOSITE directions within 48 hours (S35 FIRED-A vs S47 FIRED-B, same seven names).**
**DEEP-UTIL's mandate is therefore not "which leg wins" but "is a 20-day RS median a usable
instrument on this tape at all" (D121)** — plus the S24 branch-B question CEG/VST's prints settle.

⚠ **Not promoted, and named so the choice is visible**: the **health-care compounder basket** carries
the best pure price signal in the un-slotted set (4 of 4 positive on both windows) and was passed over
**because it has no catalyst inside the window**, not because the evidence was weaker.

### 6b. Momentum re-tags injected (the full table is Lens 3's; these are the ones that change something)

| Name | Re-tag | Flip condition |
|---|---|---|
| **TRI · ETN** | ⛔ **NO-BASE** (rs60 −0.4 / −2.2) | rs60 > 0 on a settled close by **08-12**. Until then they may not be counted in INDU's breadth evidence |
| **MU** | **EXTENDED-BUT-LIVE** (days 21-60 **+41.2**) | the {STX, MU, WDC} median RS20 back below 0 before **08-05** (S30's own anti-signal) |
| **AMAT · LRCX · KLAC** | **EXTENDED-BUT-LIVE** (+36.5 / +19.9 / +25.0) | P3's registered anti-signal: the equipment three turning positive on RS20 while storage rolls over |
| **PSX** | ⛔ **EXHAUSTED** (days 21-60 **−5.5**), corroborated independently by **FINRA z +1.53** | a beat on 08-05 that fails to re-widen the distillate crack |
| **NDAQ** | **EXHAUSTED** (rs60 +2.6, days 21-60 −8.4) | rs60 < 0 by **08-07** |
| **NVDA · AVGO** | ⛔ **NO-BASE** (rs60 −1.1 / −12.1) | rs60 > +5 / > 0 by **08-12** |
| **XOM · CVX · COP · OXY · BKR** | ⛔ **NO-BASE** — **5 of 8 Energy names are still net negative vs SPY over 60 days**; only MPC/VLO/PSX have a base, and PSX's is decaying | rs60 > 0 by **08-14** |
| **GRMN** | **EXTENDED-BUT-LIVE** — rs20 +22.1 / rs60 +22.0, **the cleanest linear base on the board, zero deceleration signature, #1 flow of all 300** | rs20 diverging below rs60 by >10pp by **08-16** |
| **HUM** | **EXTENDED-BUT-LIVE** (days 21-60 **+57.3**, the largest measured) | rs60 < +25 by 08-12. ⚠ It was `reaffirmed` out of the candidate pool on 07-31 on a value-exhaustion read — **that read is not contradicted, but this is the arithmetic on the other side of it** |

★ **The costliest "it already ran" avoidance on this board is GRMN** — #1 flow of 300, the cleanest
base measured, and **three consecutive runs with no thesis and an explicitly declined bracket.** ⚠ The
07-30 decline reason (*"a bracket needs a proposition to threaten and there is none"*) is a **statement
about the desk's coverage, not about the name**, and it has now been made three times.

### 6c. Handed onward

- **→ ALPHA's action bracket**: **S52** and **S53** (both sides, frozen, dated) · the 🚨 **rank-2
  Energy GAP (6.9% vs 8.0%, −1.10pp)** · and the note that **XOM and VLO are the highest-flow /
  best-60-day un-held epicenter expressions and are 🟡 by artifact, not by verdict.**
- **→ BET**: the momentum re-tags in 6b are **hard-stop-relevant tags, not sizing** — every NO-BASE
  name above carries a hard-stop stamp by construction. **BET owns sizing; this stage never sizes.**
- **→ DEEP-INDU**: report the **3-of-5** base split, not "5 greens."
- **→ DEEP-IT**: the STX-vs-MU inversion (1b) and the equipment re-tag (1c) are the mandate's two
  hardest questions.
- **→ a human**: **D20** (no AI-security registry row) · **D22** (no BOJ lag table — it blocks the
  board's largest regime-flip risk) · **D127** (the momentum test needs a drawdown floor — AXON) ·
  **the registry's memory-node epicenter names MU but not STX/WDC/SNDK.**

---

## ✅ EXIT CHECK

- [x] **4 lenses fanned out in parallel, in one message**; each returned named tickers + dated catalysts.
- [x] **Every bracket names its observable + frozen threshold + date and carries BOTH branches.**
      S52 and S53 registered in `handoff/SCENARIOS_US.md` and indexed in the `SCENARIOS.md` spine.
      **No one-way bracket was written.**
- [x] **Every magnitude threshold is stated against the implied move with its `D±n`** — MPC ±8.8%
      (D19, covers) · PSX ±5.3% (D5, covers) · ANET ±11.3% (D5, covers, annex candidate) ·
      **AMD ±4.0% expiring D1 BEFORE its print ⇒ declared unusable and no threshold fabricated** ·
      **S52 has no options instrument and says so.**
- [x] **Each branch graded by information content.** Five binaries dropped with the reason stated;
      **S53 branch A is explicitly labelled confirmatory-only.**
- [x] `BLINDSPOT_PREMORTEM.md` written — legs · brackets · re-tags · cycle GAP.
- [x] **Every catalyst-bearing leg promoted or logged**; brackets handed to ALPHA; GAP handed to BET.
- [x] **DEEP set updated and stated: [ENRG, FIN] + [IT, INDU] + ★[UTIL] = 5.**
- [x] **The ≤48h binaries were bracketed both ways**: AMD/ANET (S50, annex noted), **MPC (S53 — the
      gap this stage was told to fill)**, and the Iran conditional (**S52**). **No one-way tilt into a
      known binary.**

---

*asof 2026-08-02 · 4 lenses, all four dissented · 3 of this run's own verdicts attacked with the
desk's own method · 2 brackets registered (S52 · S53), 5 dropped with reasons · DEEP 4 → 5 (UTIL
promoted on independent two-lens convergence) · the board's largest regime-flip risk (Japan) named and
deliberately NOT bracketed because D22 makes any threshold fabricated.
Analysis only, zero buy/sell, zero sizing (P4).*
