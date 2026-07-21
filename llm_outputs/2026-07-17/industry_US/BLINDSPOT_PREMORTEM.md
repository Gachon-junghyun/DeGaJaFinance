# BLINDSPOT_PREMORTEM — industry_US · 2026-07-17 (Fri) ★US-only

> Stage 4 / L1·PREMORTEM. Four adversarial lenses fanned out **in parallel, in one message**, each
> briefed to argue AGAINST our own tilt BEFORE the deep budget is committed. Anti-tunnel.
> **Verdict: the draft tilt did NOT survive intact.** 3 of 4 lenses independently attacked the same
> load-bearing proposition (P2 AI-capex sign-flip), and lens 4 found a **defect in a deterministic
> guard**. Injections below are binding on DEEP/BET/ALPHA — nothing here is "noted and dropped".

---

## §0 Headline: what the pre-mortem changed
| # | Change | Driver |
|---|---|---|
| 1 | **P2 narrowed** — the capex sign-flip is NOT uniform; it is a *foundry/memory capital-intensity* verdict, not a hyperscaler-capex verdict | Lens 3 (META's capex **rewarded** the same week TSM's was punished) |
| 2 | **DEEP set 3 → 4** — `SEMI` promoted (the sign-flip + INTC 07-23) | Lens 1 PROMOTE-TO-DEEP, corroborated by lens 3 |
| 3 | **COMM's UW re-labelled** — it is a **GOOGL-regulatory + NFLX-miss** bet, not an AI-capex bet | Lens 2 |
| 4 | **Energy cycle GAP is REAL** — the tool's ✅ is an **artifact of an unsatisfiable rule** | Lens 4 (verified in source) |
| 5 | **AI-compute epicenter carved OUT of the IT-UW's operational scope** | Lens 4 |
| 6 | **P4 retirement narrowed** — the primes failed; the **RTX leg did not** | Lens 4 |
| 7 | **NFLX "D-0 binary" is stale** — it printed **07-16** and disappointed | Lens 2, verified |

---

## §1 ★ The deterministic guard is broken (lens 4 — verified in source, not taken on trust)
`scripts/cycle_exposure.py:87`
```python
gap = (cyc["rank"] <= 2) and (epi_pct_tot < cyc.get("min_epicenter_pct", 0))
```
`data/cycles/cycle_registry.json` sets **`min_epicenter_pct = 0.0`** for the **rank-2** cycle
(Energy / oil-refining). An exposure percentage is always ≥ 0, so **`epi_pct_tot < 0.0` can never be
true** — the rank-2 cycle's GAP is **mathematically unsatisfiable**. It cannot fire at any exposure.

**Consequence:** Stage 2 reported *"✅ No top-rank cycle GAP"* while the book holds **0.0% of the rank-2
epicenter**. That ✅ is not evidence of coverage; it is the absence of a working check. This is the exact
failure the tool's own docstring says it exists to prevent (*"postmortem 2026-07-14: aggressive book held 0%
of the AI-compute epicenter… Judgment can't skip a fact"*).

**Handled:** filed as a repo task (do not hot-patch a deterministic guard's threshold mid-run — the floor
is a human decision). **This run treats the Energy GAP as REAL** on the evidence below, not on the flag.

### The Energy hole is substantive, not just formal
- **Book (live KIS, lens 4):** AVGO 4.6% · NVDA 2.54% · TSM 4.91% · **KMI 14.1%** · **LNG 9.87%** ·
  MA 14.0% · RTX 9.9% · VST 5.7% · **cash 34.4%** ($2,716 — dry powder, not a constrained book).
- The 23.97% "any-layer" Energy exposure is **100% KMI (fee-based midstream) + LNG (export terminal)** —
  both **take-or-pay contracted**, i.e. structurally insulated from crack-spread economics *by design*.
  Volume names, not margin names. **Epicenter exposure is genuinely zero.**
- The epicenter thesis is **live and dated**: *"Diesel Prices Hit $5 a Gallon Again, **Up 33%** Since Start
  of Iran War"* [NYT 07-16] · *"Russian Refinery Runs Plunge to **Lowest in More Than Two Decades**"*
  [Bloomberg 07-13] · *"Russia's diesel export ban deals fresh blow"* [SCMP 07-11]. Textbook crack widening.
- **Cleanest epicenter expressions → BET's starter module:** **MPC · PSX · VLO** (flow 0.45–0.70,
  RS20 +17–23%, RS60 +23–37% — the strongest-flowing names in Energy; the thesis is already in the tape).
- **NOT the clean expression:** XOM · CVX · EOG · OXY (flow −0.16 to −0.42, negative RS60) — integrateds/E&P
  monetize *crude*, not refining margin. This distinction is the whole point of an epicenter audit.
- ⚠ This also **resolves ROTATION §3a's ENRG "early or trap?" question in a way ROTATION could not see**:
  ENRG's weak sector wflow (−0.151) is an *aggregate* artifact — the **crack sub-leg is already working**
  (MPC/PSX/VLO RS60 +23–37%) while the majors drag the average down. **→ binding on DEEP·ENRG.**

## §2 ★ P2 (the AI-capex sign-flip) does not survive as written
Three lenses attacked it independently. The refutation is **not** "the selloff isn't real" — it is that our
*mechanism* was too broad.

**The falsifying observation (lens 3, news-verified):** *"Meta's Sudden Stock Rebound Shows Investors
Endorse AI Plans"* [07-15]. **META's AI capex was REWARDED the same week TSM's capex raise was PUNISHED**
— and META is the index's biggest hyperscaler capex spender, currently **+0.79 flow, 🟢ACCEL, OBV
accumulating, RS20 +10.7%**, sitting *inside the sector we UW'd*. If the market had flipped the sign on
"AI capex" as such, META is the name that should have broken. It went the other way.

**Second refutation (lens 1, news-verified):** Barron's framed TSMC's $100bn as TSMC **"fighting the Intel
Challenge"** [07-16] — i.e. the raise is partly **defensive against Intel Foundry share gains**, not pure
demand confirmation. Our clean "capex = demand-signal → now repriced as cost" reading skipped this.

**Third (lens 1, flow-verified):** the "capex → equipment orders" chain is **not decoupling** — AMAT
−0.087, LRCX −0.438, KLAC −0.594, all red, trading as one basket with memory/GPU. So the sign-flip is *not*
confirmed by the equipment tape either. It is currently an **indiscriminate complex-wide de-rate**.

### → P2 REWRITTEN (binding on DEEP·SEMI and BET)
> **P2′ — Capital-intensity de-rate (narrow).** The market is de-rating the *capital-intensive* leg of the
> AI chain (foundry + memory: TSM, MU, and the semicap basket) on an **expectations/"high bar" reset**, while
> **rewarding** hyperscaler capex where the spender owns the demand (META). This is a **valuation/positioning
> event in one leg**, not a regime-wide repricing of AI capex.
> **Anti-signal (unchanged, still binding):** MU holds **853.20** and SMH RS20 turns positive → even the
> narrow leg was just a dip. **Second anti-signal (new):** if META rolls over (RS20 negative + OBV flips to
> distribution), then the *broad* sign-flip we originally wrote **is** right after all and P2′ was too timid.
> **Track:** MU 853.20 · SMH RS20 (−7.7%) · META RS20 (+10.7%) · INTC print 07-23.

## §3 Both-sides brackets — one per binary (→ ALPHA's action bracket)

| Binary | Against-us branch | What rips (named) | Which OW of ours gets hit | Trigger | Invalidation |
|---|---|---|---|---|---|
| **NFLX** ⚠ **STALE — already printed 07-16 and disappointed** (NFLX $74.35, flow −0.442 🔴, RS20 −5.6%, RS60 −27.5%; *"Netflix's earnings disappointed"* [DB 07-17]) | Oversold snapback on ad-tier/subscriber detail; drags GOOGL/META/QQQ up | NFLX, GOOGL, META, QQQ | **UW-COMM / UW-IT** squeezed on beta; a broad tech-relief bid unwinds the flight-to-quality behind OW-FIN | NFLX reclaims ~$78–80 on vol_surge >1.3× + OBV distributing→accumulating | close >$80 |
| **SCHW 07-21** (D-4) — *the direct test of the FIN OW earnings leg* | **Beat-but-fade.** The pattern already fired this week: *"Bank of America's stock falls **despite** blockbuster earnings"*; *"Big Banks Smash Earnings Records, but 'Tectonic' Risks Loom"*. SCHW has **already run** (RS20 +9.7%) = the same "high bar" that hit TSM | — (this is a fade, not a rip) | **OW-FIN directly** — ripples through the exact breadth (PNC/BNY/PYPL/USB) the OW rests on | SCHW beats consensus but closes red | SCHW <$98 on an in-line-or-better print |
| **TSLA 07-22** (D-5) | Low bar (missed robotaxi guidance 3 prints running) → robotaxi/Optimus beat = high-beta hope trade | TSLA, then the crowded-short Nasdaq complex by contagion | **UW-IT / UW-COMM** squeezed on beta (⚠ TSLA's own short-vol z is −0.67 = *not* a crowded-short squeeze candidate; the risk is **contagion, not TSLA**) | TSLA >$420–430 on vol_surge >1× | that level |
| **KMI 07-22** (D-5) | Sell-the-news even on in-line: **short pressure rising into the print** (short-vol 62.2%, z **0.92**, 5v5 **+5.2▲**) | — | **OW-ENRG directly**, and the *held* book position (KMI = 14.1%) | miss/guide-down + short-vol z climbing post-print | KMI <$31 |
| **Hormuz TACO** (undated, live) — **the highest-payoff against-us scenario in the book** | Durable "strait open / blockade lifted" → oil gives back the **full +10.2%** toward **$70–72**. ⚠ **Because WTI is 13%ile crowded-short, residual shorts ADD rather than cover — that ACCELERATES the drop instead of cushioning it** (the mirror of the squeeze we just won) | — | **OW-ENRG**, and MPC/VLO/PSX (RS20 +17–23%) give back; KMI/LNG held in book | Trump/Centcom "open"/"blockade lifted"/"ceasefire" language **surviving >24h** (⚠ the toll-plan reversal already fired and faded in <48h — the bar is a **durable** statement, not a headline) | CL=F <$72 and XLE giving back >half its +3.5% |

⚠ **KMI and Hormuz are NOT independent** — both hit the same OW leg. Treat as one correlated exposure, not two brackets.

### §3a Correlated-UW check (the 07-15 field note) — **verdict: NOT one bet, but one label was wrong**
Lens 2 decomposed the UW set: **IT** = genuine broad rot (0 green / 21 red; eqflow −0.339 ≪ wflow −0.094).
**COMM** = *not the same story* — the cap-weighted −0.443 is **GOOGL-specific regulatory** news (Gemini
delay, EU Android access order, Swiss antitrust probe) **+ the NFLX miss**, while **META is +0.79 accelerating**
and eqflow is only −0.03. **RE + MATR** = the duration/reflation story (P1), not AI. And **copper at 95%ile
crowded-LONG actually *favours* the MATR UW** (crowded longs are downside squeeze-out risk).
→ **Three distinct wagers. Diversified.** But **COMM's UW must be re-labelled**: it is a *GOOGL-regulatory +
NFLX-earnings* bet — **thinner, more binary, and directly exposed to the NFLX bracket above**. Our original
"COMM UW = P2 sign-flip" framing was **not supported by the data**.

### §3b The mirror-image question — **the sharpest finding of the run**
*Is UW-IT the mirror of 07-15's OW-IT mistake — the same 4%ile short read in the opposite direction?*
**Lens 2's verdict: not the identical logical error — but the same landmine is under it.** Our UW-IT rests
on fundamentals (breadth 0-green/21-red, the TSM reaction), *not* on positioning, so it is not a literal
repeat. **But the Nasdaq-100 4%ile crowded-short is STILL LOADED and unresolved**, and deteriorating breadth
is exactly the setup that produces violent mean-reversion squeezes.
> **The UW-IT book sits on the same unresolved fuel that just burned the OW-IT call — with the P&L sign
> flipped.** Our own failure class ("positioning is ammunition, not a trigger — the differentiator is a
> catalyst") **cuts both ways**: absent a catalyst that resolves the squeeze, UW-IT must be **sized and
> hedged for the same tail we should have priced into OW-IT on 07-15**. → binding on BET sizing.

## §4 Momentum re-tags (lens 3) — "already ran" is not a reason to avoid
| Name | Tag | Cycle-KPI evidence | Flip condition |
|---|---|---|---|
| **NVDA** | **EXTENDED-BUT-LIVE** ★ | −1.7%, RS20 ≈flat while the complex broke. **The bellwether held up BEST — if the cycle were ending it should crack hardest.** Evidence *against* exhaustion | RS20 <−5% on a volume surge |
| **MU** | **EXTENDED-BUT-LIVE** | OBV 🟡 **not distributing**; DRAM/HBM = *"unprecedented supply shortage"* [07-16]; $250B AI-memory investment [07-11]; $100B Ford backlog [07-13]. **No MU-specific KPI miss exists** — it fell on the tape-wide headline | OBV→distributing **and** RS20 <−20%, or an HBM contract-price rollover |
| **TSM** | **EXTENDED-BUT-LIVE** (fundamentals) — technical risk flagged | KPI accelerating (record profit + raised capex/revenue + $265B total US commitment). But the **only** genuine 🔴distribution + **only** volume surge (1.13×) on the board | RS60 negative **and** distribution persists 2+ sessions on rising surge |
| **META** | **EXTENDED-BUT-LIVE / re-accelerating** ★ | 🟢ACCEL, OBV accumulating, vol 1.22×, RS20 +10.7% turning up against RS60 −6.9% = reversal signature. Capex **endorsed** [07-15] | RS20 rolls negative + OBV→distribution |
| **GEV** | **EXTENDED-BUT-LIVE** | OBV 🟢**accumulating while price fell −5.1%** — smart-money-buys-the-dip signature; RS20 +5.4% | OBV→distributing or RS20 negative |
| **CL=F** | **EXTENDED-BUT-LIVE — arguably EARLY, not extended** | **RS60 still −20.6%** → oil was *lagging* into this move = fresh reversal off a beaten base, not a tired extension. 13%ile shorts **not yet flushed** | TACO headline, or COT flipping to crowded-long |
| **PNC** | EXTENDED-BUT-LIVE | RS20 +8.7%, RS60 +6.5%, OBV accumulating | SCHW 07-21 read-through |
| **XLF** | **EARLY, not extended** | RS60 only **+1.9%** — the FIN OW has not run yet | — |
| **AVGO** | **EXHAUSTED** | RS60 already **−12.2%** — it was *not* leading; the honest counter-example that the complex isn't monolithic | RS60 positive + OBV accumulating |
| **VRT** | **EXHAUSTED** | genuine 🔴distribution, RS60 −12.4%, short-vol z +1.25 | OBV→accumulating, RS60 positive |
| **PYPL** | ⚠ **CAUTION / pending-KPI-confirm** | RS20 +29.9% and **vol surge 1.83× (largest on the board)** but RS60 only +4.3% — compressed move, **no PYPL-specific catalyst found**. Do not treat dips as buys before a take-rate/volume KPI check | — |

**Lens 3's blanket verdict** ("the whole AI complex is EXTENDED-BUT-LIVE; the UW is selling the dip of a live
cycle") is **accepted in part, rejected in part**: accepted for **NVDA/MU/META/GEV** (KPI accelerating, OBV not
distributing) — **rejected** as a sector call, because it cannot explain **IT breadth 0-green/21-red**. A cycle
can be live at the epicenter *and* rotting at the periphery; that is precisely what eqflow −0.339 measures.
**→ IT stays UW as a breadth/new-money call. The epicenter is carved out (§5).**

## §5 ★ Cycle-exposure injections (→ BET)
1. **CARVE-OUT (binding).** The **AI-compute epicenter (AVGO · NVDA · TSM)** is **out of the IT-UW's
   operational scope.** Two different objects were being conflated: GICS-IT-as-rotation-entry (a *breadth*
   call about where **new** money goes → UW stands) vs the cycle-registry **AI-compute epicenter** (a
   deliberately **tape-independent core**, built 07-15 in answer to the 07-14 GAP).
   ⚠ **The book is at 12.06% vs a 12.0% floor — 0.06pp of margin.** Mark-to-market erosion alone
   (AVGO RS60 −12.2%, TSM −5.6%) can breach it **without a single trade**. **Reclassify ✅ → WATCH.**
   > **Any trim of AVGO/NVDA/TSM under the UW-IT banner would silently manufacture the 07-14 failure in
   > reverse — not "never built the core" but "dismantled it under cover of a sector call that was never
   > about the core."** The hard rule stands: **a 🔴 tape gates ADD timing; it never justifies 0% core.**
2. **ENERGY epicenter starter (→ BET):** **MPC · PSX · VLO**. Rank-2 cycle, **0.0% epicenter held**, thesis
   live and dated (diesel +33%, Russian runs at a 2-decade low), **34.4% cash available**. ⚠ Bracket against
   the Hormuz TACO branch (§3) — this is the *same* exposure, and the 13%ile short makes the downside
   **accelerate**, not cushion.
3. **P4 correction (binding on MACRO §4a):** our MACRO retired the defense proposition **too broadly**. The
   failed leg is the **platform primes** (LMT flow −0.742/RS60 −17.6%/vol 0.58×; NOC −0.683/RS60 −27.0%; both
   🔴distributing). **RTX is a different leg**, correctly bifurcated on 07-15 and held at 9.9% — still 🟡NEUTRAL
   and cleanly separated from the primes. **Retire the primes, not the cycle.** ⚠ RTX momentum *has* cooled
   since 07-15 (flow 0.317, RS60 −6.7%) → re-verify OBV before any add; the existing core is not invalidated.
4. **Scope note (lens 4):** **MA (14.0%, the largest non-Energy position)** and **both FIN and HLTH** sit
   **outside the 3-cycle registry entirely** → this audit's "no GAP" coverage is **narrower than the book**.
   Two of our three OW sectors have **zero cycle-registry linkage**. Logged — the registry is not a map of the book.

## §6 Under-computed legs — every one promoted or logged (none silently dropped)
| Leg | Named tickers | Dated catalyst | Verdict |
|---|---|---|---|
| **Intel oversold-into-print** | **INTC** | **Q2 earnings 07-23** (confirmed 3× in-DB: *"scheduled to report second-quarter results on July 23"* [Yahoo 07-10]; *"Here's the Clear Reason to Buy Intel Before Its July 23 Earnings"* [07-15]; *"Intel's AI-Driven Data Center Growth Set To Power Q2 Earnings"* [SA 07-17]) | **PROMOTE-TO-DEEP** → folded into DEEP·SEMI. flow −0.575 with **RS20 −17.2% vs RS60 +41.7%** (the same violent 20d de-rate as MU) + short-vol z −1.14 (**not** a crowded short = a genuine oversold-vs-narrative gap, not squeeze fuel). **Falsifier:** in-line/miss on data-center/foundry revenue + RS20 making new lows post-print |
| Semicap equipment | AMAT · LRCX · KLAC | KLAC "ahead of earnings" [SA 07-15] — **exact date NOT confirmable in-DB → recorded as `[blank]`, not guessed** | **WITHIN-RUN-WATCH.** The bull mechanism is real and tape-proven (*"Applied Materials, KLA, Lam Research Take Off on Meta's Chip Plans"* [07-09]) but all three are red/distributing now = no clean decoupling yet. **Falsifier:** KLAC prints an OK order book and still fails to outperform SMH → the complex is one systemic basket, no equipment alpha |
| INDU ignition | **CTAS · FAST** | **none forward** — both **already reported** (FAST 8-K 07-14; CTAS 8-K 07-15 Item 2.02) | **WITHIN-RUN-WATCH.** This is **PEAD drift off a beat, not anticipation** — which is *why* they are the only 🟢 industrials. Confirms ROTATION's "watch-promote, not DEEP". **Falsifier:** 5–10 more sessions of green on no news = a real standalone momentum leg |
| AI-power single-name | **GEV** (vs VRT/ETN) | GEV Q2 "imminent" — **date unconfirmable → `[blank]`** | **WITHIN-RUN-WATCH.** The *only* positive-flow name in the AI-infra trio (flow +0.324, OBV accumulating) vs VRT (−0.474, distributing, short z +1.25) and ETN (−0.268). The *"AI Trade Is Rotating From Chips to Infrastructure"* [07-11] story is **a single name, not a sector green light** — vindicates Neutral-INDU |
| Healthcare REITs | **WELL · VTR** | Q2 late-July — **date unconfirmable → `[blank]`** | **WITHIN-RUN-WATCH → binding on DEEP·HLTH + DEEP-adjacent RE.** WELL 0.517 (RS20 +13.1), VTR 0.483 (RS20 +13.2), both OBV accumulating — vastly stronger than RE's −0.046. **Our blanket RE-UW is capturing office/retail weakness while mispricing a sub-leg that trades on the HLTH OW thesis.** Directly sharpens ROTATION's RE divergence |
| Staples idiosyncratic | **MNST** | none found in-window | **WITHIN-RUN-WATCH.** flow 0.601, RS20 +7.5, RS60 +23.5, OBV accumulating in a −0.247 sector = real idiosyncratic divergence |

## §7 Did any lens agree with the draft? (the stage demands this be stated)
**Partially — and the agreements are informative:**
- **IT-UW survives** as a *breadth* call (0 green / 21 red; eqflow −0.339) — but only after carving out the epicenter and narrowing P2 to P2′.
- **MATR-UW survives and is strengthened**: copper 95%ile crowded-**long** = downside squeeze-out risk, which *favours* the UW (lens 2).
- **FIN-OW survives and is upgraded on quality**: XLF RS60 only +1.9% → **early, not extended** (lens 3). The risk is not that it ran; it is **SCHW's beat-but-fade** on 07-21 (lens 2).
- **Neutral-INDU survives** — vindicated at name level (GEV accumulating vs VRT/ETN distributing = no sector thaw).
**No lens rubber-stamped the tilt.** The default expectation held: each surfaced something the deterministic desk missed.

---

## §8 FINAL DEEP SET (updated — stage requires this be stated)
> **4 targets: `FIN` · `HLTH` · `ENRG` · `SEMI`** ← SEMI is the **pre-mortem-promoted** addition
> (ROTATION had 3; the rule forbids padding from Neutral/UW, but PREMORTEM may promote a leg — and 3 of 4
> lenses converged on this one). File: `SECTOR_DEEP_SEMI.md`.

**Question each DEEP must now answer (amended by this stage):**
1. **DEEP·FIN** — earnings leg or curve leg? (unchanged) **+ new:** is SCHW's 07-21 "high bar" the BAC beat-but-fade pattern? XLF RS60 +1.9% says early, not extended.
2. **DEEP·HLTH** — money-with-no-story: durable or parking lot? **+ new:** does the **WELL/VTR** healthcare-REIT sub-leg belong to this OW rather than to the RE-UW?
3. **DEEP·ENRG** — **question CHANGED.** "Early or trap?" is **partly answered**: the crack sub-leg is *already working* (MPC/PSX/VLO RS60 +23–37%); the weak sector wflow is a majors-drag artifact. **New question:** is the **crack spread** (diesel +33%, Russian runs at 2-decade lows) durable enough to justify epicenter exposure **given** the Hormuz TACO branch accelerates on 13%ile shorts?
4. **DEEP·SEMI** (new) — **is P2′ right?** Resolve: capital-intensity de-rate (foundry/memory only) vs a broad AI-capex sign-flip vs a plain dip in a live cycle. **INTC 07-23** is the dated fulcrum. Must reconcile: MU/NVDA OBV not distributing + KPI accelerating **against** IT breadth 0-green/21-red.

---
**EXIT CHECK:** ✅ 4 lenses fanned out **in parallel in one message**; each returned **named tickers + dated
catalysts** (undated ones recorded `[blank]`, never guessed) · ✅ BLINDSPOT_PREMORTEM.md written (legs ·
brackets · re-tags · cycle GAP) · ✅ **every** catalyst-bearing leg promoted (INTC→DEEP·SEMI) or logged
(§6 — none dropped); brackets → ALPHA (§3); GAP + epicenter starters → BET (§5) · ✅ **DEEP set updated and
stated: FIN · HLTH · ENRG · SEMI** · ✅ correlated-UW field note checked (§3a — not one bet; COMM re-labelled) ·
✅ deterministic-guard defect verified **in source** and filed, not hot-patched mid-run.
**→ proceed to DEEP.**
