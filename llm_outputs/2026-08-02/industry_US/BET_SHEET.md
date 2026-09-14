# BET_SHEET — industry_US — 2026-08-02 (Sun)

> Phase 3. One file, per-sector sections (§A numbers · §B thesis+freshness · §C flow/positioning ·
> §D peers · §E refutation+dated catalyst). **Downstream desks glob this exact filename — never split
> it.** Prices/flow `asof 2026-07-31 settled`; benchmark **SPY** named inline (**C1**).
> **Analysis only — zero buy/sell, zero position sizing (P4). Any sizing word below is illustration.**

---

## ⚠ 0 · Four instrument caveats binding on every number below

1. **`velocity` is null on 300/300 this run**, so the 🟢 gate is `OBV-accumulation ∧ RS20>0 ∧
   vol_surge ≥ 1.2`, and **69 of 85 accumulation candidates are blocked by `vol_surge` ALONE.**
   **A 🟡 on this sheet is not a verdict.** Proven this run: **`module_flow MPC` returns 🟢 on news
   velocity 2.35× on the same date the sweep returns 🟡, because the sweep's velocity column is
   empty.**
2. **Lens L2 (peak-margin / low-multiple trap) is STRUCTURALLY UNRUNNABLE on six of this sheet's
   names** — `margin_history.py` returns `연간 데이터 없음` for **VLO (6th run, D56) · XOM (3rd) ·
   MET · ICE · CEG · PCG**, and **RTX's series ends FY2017 (M233)**. **No cheapness claim is made on
   any of them (C3).**
3. **`us_top300.csv` is 18 days stale**, so every `wflow` carries a two-and-a-half-week-old market-cap
   weighting. **TSM and LNG are outside the universe entirely** — no flow, RS or short read exists.
4. **Every "cheap" line below carries BOTH the margin percentile AND the estimate-revision trend.**
   A low multiple whose estimates are being revised up steeply is **consensus chasing, not
   cheapness** — and on this sheet that describes the entire refining complex and STX.

---

## §A · Numbers — the whole sheet in one table

| Ticker | Sector | Price | fwd P/E | trail P/E | P/B | to mean target | FY25 gross margin vs its OWN history | +1y EPS /90d | 30d revisions | flow (tag) | RS20 / RS60 vs SPY | days 21-60 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **STX** | IT | 856.13 | **15.65** | 61.73 | 175.4 | **+29.2%** | **35.2% = the MAX of a 17-yr series** (median 27.7, min 14.4) ⇒ **~100th pctile** | **+39.7%** | **4↑:0↓** | +0.799 🟢 `new_green` | **+4.1 / +7.8** | **+3.7** |
| **MU** | IT | 823.03 | **5.35** | 18.59 | 9.23 | **+85.0%** | ⚠ **the two series DISAGREE and both are quoted (C2): ANNUAL FY25 39.8% ≈ 70th pctile** (max 58.9 FY2018, median 32.0) **vs the QUARTERLY 84.6% = 100th pctile (M2/M18)** | **+54.1%** | **30↑:0↓** | **−0.600 🔴분산** | **−15.9 / +25.3** | ★ **+41.2** |
| **MSFT** | IT | 464.72 | 19.96 | 25.90 | 7.80 | +21.2% | not pulled — no cheapness claim made | +3.5% | 1↑:1↓ | +0.850 🟢 | +18.7 / +9.8 | −8.9 |
| **MPWR** | IT | 1,426.03 | **40.98** | 86.95 | 19.05 | +28.3% | 55.2% = **exactly its own median** (max 59.2 FY2009) ⇒ mid-range | +15.4% | **15↑:0↓** | +0.786 🟢 `new_green` | +10.4 / **−13.4** | **−23.8** |
| **FTNT** | IT | — | — | — | — | — | not pulled | — | — | +0.560 🟢 `new_green` | +3.3 / **+76.9** | **+73.6** |
| **MPC** | ENRG | 316.47 | **11.40** | 20.83 | 5.53 | **−4.0%** | **10.0% vs a 10.5% median and a 14.5% max ⇒ ~37th pctile — BELOW its own median, NOT peak margin** | **+35.1%** | 6↑:3↓ | +0.567 🟡 | **+18.5 / +18.3** | −0.2 |
| **VLO** | ENRG | 312.90 | 11.56 | 13.05 | 3.89 | −2.7% | ⛔ **`연간 데이터 없음` — 6th run (D56). NO cheapness claim.** | **+45.0%** | 10↑:3↓ | +0.556 🟡 | +16.6 / **+20.2** | **+3.6** |
| **PSX** | ENRG | 211.68 | 11.15 | 20.92 | 2.97 | −2.9% | **12.3% vs a 12.1% median (max 25.9 FY2016) ⇒ ~55th pctile, mid-cycle** | +25.1% | 5↑:3↓ | +0.600 🟡 | +19.7 / +14.2 | ⛔ **−5.5** |
| **XOM** | ENRG | 155.44 | 14.69 | 26.17 | 2.50 | +7.5% | ⛔ **`연간 데이터 없음` — 3rd run. NO cheapness claim.** | +4.6% | 3↑:1↓ | +0.606 🟡 | +13.1 / **−2.9** | ⛔ **−16.0** |
| **MET** | FIN | 96.13 | **8.75** | 18.59 | 2.27 | **+1.7%** | ⛔ **`연간 데이터 없음` (insurer). NO cheapness claim.** | +0.4% | 3↑:0↓ | +0.800 🟢 | +6.4 / +17.1 | **+10.7** |
| **ICE** | FIN | 152.48 | 17.38 | 21.51 | 2.93 | +19.5% | ⛔ **`연간 데이터 없음`. NO cheapness claim.** | +0.3% | 2↑:1↓ | +0.789 🟢 `new_green` | +14.4 / **−5.0** | ⛔ **−19.4** |
| **RTX** | INDU | 215.22 | 27.55 | 37.89 | 4.37 | +6.8% | ⛔ **series ends FY2017 (M233) ⇒ percentile unobtainable. NO valuation claim.** | +3.5% | 1↑:1↓ | +0.782 🟢 | +7.7 / **+21.3** | ★ **+13.6** |
| **GD** | INDU | — | — | — | — | — | not pulled | — | — | +0.546 🟢 | +2.3 / +6.6 | +4.3 |
| **ITW** | INDU | 286.95 | 23.27 | 25.97 | 25.68 | +4.0% | ⚠ **44.1% against a 44.3% max (FY2024) and a 41.2% median ⇒ ~93rd pctile — essentially AT its own peak** | +1.6% | 1↑:1↓ | +0.793 🟢 | +4.9 / +9.5 | +4.6 |
| **ETN** | INDU | 415.20 | 26.24 | 40.67 | 8.18 | +10.2% | ⚠ **37.6% against a 38.2% max (FY2024) and a 32.8% median ⇒ ~90th pctile** | +2.2% | 3↑:0↓ | +0.701 🟢 `new_green` | +3.9 / **−2.2** | ⛔ **−6.1** |
| **CEG** | UTIL | 262.75 | 19.64 | 22.83 | 2.84 | **+34.3%** | ⛔ **`연간 데이터 없음` (regulated/merchant) ⇒ L2 structurally unrunnable. NO cheapness claim.** | **−1.6%** | 3↑:3↓ | +0.539 🟡 | +9.5 / **−21.2** | ⛔ **−30.7** |
| **VST** | UTIL | 148.19 | 14.35 | 24.74 | 16.05 | **+49.8%** | ⛔ **`연간 데이터 없음`. NO cheapness claim.** | **−0.8%** | 3↑:1↓ | +0.009 🟡 | −2.2 / −10.8 | ⛔ **−8.6** |
| **PCG** | UTIL | 17.38 | 9.63 | 12.50 | 1.18 | **+31.8%** | ⛔ **`연간 데이터 없음` (regulated) ⇒ L2 structurally unrunnable. NO cheapness claim (C3).** | +0.2% | 2↑:3↓ | +0.617 🟢 | +1.6 / +3.2 | +1.6 |

**Arithmetic cross-checks performed**: `days 21-60 = rs60 − rs20` re-derived from the JSON and
independently reproduced from a yfinance settled pull to ≤0.5pp; `to mean target = target_mean/price − 1`
computed from the raw fields, not quoted. **Blanks above are blanks, not guesses.**

---

## §B · Thesis + freshness (⚠ freshness tags are ALPHA's to fill — placeholders here)

### ENRG — **the sheet's most active section, and its thesis is now SPLIT BY SUB-NODE**
**Thesis**: refining margin, not crude beta. **DEEP-ENRG resolved the equity-vs-commodity divergence
to the sub-node level rather than leaving it `indistinguishable`**: on a fast (2–5 session) window the
**crude-linked names (XOM, OXY, COP) are already rolling over negative vs SPY while the refiners
(MPC, VLO, PSX) remain positive** — so ROTATION's "#1 flow, zero reds" is a **20-day window
mechanically lagging a 2-session commodity shock.**
⚠⚠ **The commodity's RATE has turned on both series (lens L1, mandatory here)**: the distillate
crack's 5-session change ran **+11.665 → +3.048 → +1.066**, and the **3-2-1's own 5-session rate is
already NEGATIVE (+4.995 → +0.822 → −4.439).** **Two consecutive declines in the rate is the signal;
the level is the distraction — and the level is not quotable anyway (R30/D95).**
★ **DEEP-ENRG settled the registry contradiction rather than parking it**: **XOM's "0% refining" tag
(M146) is WRONG** — XOM's Energy Products/refining segment printed **$4.1–5.5bn, a four-year high**,
comparable to or above CVX's $4.9bn. **The XOM-miss/CVX-beat split is maintenance-cost timing and a
consensus gap, not an exposure difference.** ⇒ **a registry defect to fix, and it means the book's
Energy epicenter % is measured on a wrong tag.**
**Freshness**: `[ALPHA]`

### IT — **a bracket fired against the desk, and the sheet must carry BOTH sides of it**
**Thesis**: `[contested]`. **S30 FIRED-A** — the {STX, MU, WDC} median RS20 crossed above 0. But
**DEEP-IT measured it decaying on its first re-test: +1.7 (07-30) → +0.8 (07-31), i.e. 0.8pp from its
own anti-signal, having been 25pp away at registration**, and **the mega-cap wflow leg HALVED
(+0.199 → +0.081)** ⇒ **a fading quartet, not a strengthening sector.**
★★ **The sheet carries STX and MU as an explicitly unresolved pair (C4)**, because the two axes rank
them in opposite orders: **STX has the direction and the flow (🟢 `new_green`, RS20 +4.1) on the
board's thinnest positive base (+3.7); MU has the board's strongest base (+41.2) with the worst flow
(🔴분산 −0.600, RS20 −15.9).** **DEEP-IT named the two separators**: MU's flow turning 🟢 while its
RS20 closes on RS60; and STX's short-z +1.23 build resolving into covering rather than continuing.
⚠⚠ **STX's L2 reading is the trap shape in its purest form on this sheet: gross margin at the MAX of
a 17-year series, a 15.65× forward multiple, and +1y EPS +39.7% in 90 days on 4↑:0↓.** **The multiple
is low BECAUSE the denominator is being revised up that hard. That is chasing, not cheapness.**
★ **The sector's biggest new fact is a buy-side one**: **Tim Cook called memory pricing *"a hundred
year flood"* on his final earnings call** [3 outlets, bodies], **Apple guided Sept-quarter gross
margin 47–48% vs 50.1% reported**, and **"MU, SNDK, WDC, SKHY jumped AFTER-HOURS on 07-31 as Amazon
and Apple management flagged soaring costs"** — **an event in no settled bar, landing 08-03.**
⚠ **A "memory costs surge SIXFOLD" headline exists and does NOT verify** (title-only, boilerplate
body, and the same word in the same window belongs to **SK hynix's Q2 PROFIT** rising sixfold).
**The magnitude is not cited anywhere on this sheet.**
**Freshness**: `[ALPHA]`

### FIN — **the OW's stated reason has now changed three times in three runs, and that is the finding**
**DEEP-FIN's verdict: the OW survives on the INSURANCE node, not on banks.** Bank NII did **not**
confirm — **BAC and JPM both slipped 🟢 → 🟡 with negative deltas**, and the front-end fall that would
drive NIM did not repeat on the 07-30 print (**DGS2 +1bp, not −4bp**). The **insurance node
re-measures at 2.4–2.9× the sector's eqflow** (vs the 1.48× previously cited) and fits the **30y-led**
steepening (reinvestment yield) better than front-end bank NIM. ⚠ **W3 binds — real ≠ profitable**:
M138 measured the NII leg migrating to markets/financing balances, so a steepener does not reach every
bank.
⚠⚠ **Flagged as an instability, not sold as a discovery: "breadth-led" (R32, retracted) → "the
steepener" (W3-constrained) → "the insurance node" is three carriers in three runs.**
★ **The exchanges node has SPLIT and the split inverted vs July** — venue **(ICE + NDAQ + CME) flow
+0.632** against ratings/index **(SPGI + MCO + MSCI) −0.518**. **DEEP-FIN tied ICE's `new_green` to
its own earnings week via EDGAR (07-30 earnings = 07-30 Reg FD 8-K = `new_green` the same day, with
ZERO M&A-category 8-Ks on file)** ⇒ **D51: the flow IS the event.** **Proposed replacement for M135's
structurally broken RS60 test: the venue-minus-ratings equal-weight flow spread, currently +1.150,
dated 08-07.**
**Freshness**: `[ALPHA]`

### INDU — **promoted on 5 greens; the sheet carries 3**
**DEEP-INDU reported the 3-of-5 split**: **RTX (+13.6) real · ITW (+4.6) and GD (+4.3) thin but real ·
TRI (−10.1) and ETN (−6.1) NO BASE.** ★ **And it re-tested an inherited claim rather than repeating
it: M91's *"~8 of UNP's 12 revenue growth points are FUEL SURCHARGE"* does NOT hold on the FY2025
10-K — fuel-surcharge revenue DECLINED $218M in 2025 against total growth of 1–2%.** The structural
2-month lag mechanism is confirmed; **the magnitude is not.** ⇒ **tagged `[unverified→revised]` and
carried to §5 of the standing view as a retraction candidate**, because **S49 branch B and S52 branch
B both use M91 as a premise.**
★ **W4 executed on primaries**: **RTX backlog +23% YoY to $268bn** (US-government share down to 38%
from 46%); **GD backlog +30% to $118bn** including **$20.1bn of Navy submarine awards**. **AXON's
10-K still contains zero "backlog" mentions — R9's caveat holds.**
⚠ **S42's branch-B second leg is FAILING and this sheet says so: the median RS20 is healthy (+10.1)
but the green-count leg needs 2 of 4 and has 1 (ITW only)**, with the in-bracket control **CAT at
RS20 −15.7 / RS60 −13.1, 🔴 −0.589** — still diverging, which supports the sub-node reading (W5).
**ETN adjudicated: an AI-power name wearing an Industrials tag** — its `new_green` is a same-day
earnings print (D51), its base is negative, and its short-z level (+1.49) and 5v5 trend (−6.7▼)
disagree (C4).
**Freshness**: `[ALPHA]`

### UTIL — **promoted to a 5th DEEP slot, and it returned the run's single best finding**
★★★ **`D` (Dominion) is a MERGER-ARBITRAGE security, not a rate-sensitive regulated utility.**
NextEra is acquiring Dominion all-stock at a 0.8138 NEE/D ratio; **the DEFM14A was filed 2026-07-28 —
one day before the close on which S35's branch A fired.** D correlates **+0.89 with NEE and −0.21
with SPY**, and its D/NEE ratio has converged from a ~20% deal discount to **2.2%**. ★ **This
explains the "accumulation on no volume" (vol_surge 0.42) that two separate desk files flagged and
neither could account for — a converging arb spread trades on little volume by construction.**
★★ **And it changes the fired verdict's arithmetic: on the regulated-SIX basket the 07-29 median
never crossed zero (−0.99, not +0.39).** ⚠ **The correction runs AGAINST the desk, not for it — the
07-31 six-name median is −5.85 vs −4.89 with D included, so the UW− case is STRONGER without D.**
★★ **D121 substantiated with numbers**: over 40 settled sessions the regulated-7 median RS20 vs SPY
**crosses zero 10 times**, its **daily σ is 2.08pp**, and **60% of readings sit within 1σ of zero** ⇒
**the +0.39 print that fired S35 is a 1.1σ one-day wobble.** Separately **S47's branch-B condition is
the MODAL state, true 70% of the time** ⇒ **firing it is the base rate, not a resolution.**
⇒ **DEEP-UTIL's verdict: the whole-sector UW− STANDS, on cleaner grounds than 07-31.**
⚠ **Both AI-power names are NO-BASE — CEG days 21-60 = −30.7, VST = −8.6 ⇒ bouncing, not turning**,
and CEG/VST's EDGAR carries **zero fresh hyperscaler PPA disclosures.**
**Freshness**: `[ALPHA]`

---

## §C · Flow / positioning cross-read (A-grade price · B-grade short pressure · C-grade OBV)

**FINRA Reg SHO z, 2026-07-31** — the divergences that matter:
- ⚠⚠ **PSX z +1.53 = 🔴 short SURGE, the only one on the desk's pull, into an 08-05 print**, on top
  of **P/C 1.25 — the only fear/hedging option profile on the sheet.** **The two B-grade axes agree
  and they agree AGAINST the name**, while PSX's A-grade base is the one PREMORTEM re-tagged
  **EXHAUSTED (days 21-60 −5.5).** **Three axes pointing one way is the sheet's clearest single read.**
- **STX z +1.23 and WDC z +1.46 — shorts BUILDING into the memory turn — but both 5v5 trends are
  −9.3▼ / −8.5▼**, i.e. the level and the trend disagree ⇒ **`indistinguishable` (C4)**, recorded.
- **ETN z +1.49 (the shortlist's highest build) with 5v5 −6.7▼** — same disagreement.
- **Clean-rise set (🟢 ∧ low-short/covering): MET · ITW · MPWR · RTX · TRI · EA.** ⚠ **TRI and EA are
  both filed to the reject ledger below** — a clean-rise tag is not a thesis.
- **NUE z −1.40 / 5v5 −7.7▼ = the cleanest short-collapse on the pull**, on a Materials name carrying
  **RS20 +16.3 vs SPY** inside a sector this run reverted to **UW**. **Named, not acted on.**
- **MPC option skew +33.0 against P/C 0.44** — the book is paying for a fat downside tail while
  leaning call-heavy on direction ⇒ **`indistinguishable` (C4)**, not a read.
- **COT context only, never a signal (D6, and S32's own registration forbids it)**: NDX 5th %ile ·
  R2K **88th → 57th** (the board's largest de-risking) · NatGas **3rd** · Copper 96th · WTI 10th.

---

## §D · Peers / competition

- **Refining**: MPC ~11.40× · VLO ~11.56× · PSX ~11.15× forward — **within 0.4× of each other, so the
  multiple does not discriminate**; the discriminators are the **margin percentile** (MPC ~37th =
  below its own median; PSX ~55th; **VLO unmeasurable**) and the **base** (VLO days 21-60 +3.6 is the
  only clearly positive one). ⚠ **One risk unit — SPY-residual ρ +0.878 (M147).**
- **Memory/storage**: STX (100th-pctile margin, 15.65×) vs MU (annual ~70th / quarterly 100th, 5.35×,
  30↑:0↓, +85% to target) vs WDC. **Not peers on the same axis** — see §B.
- **Exchanges**: venue (ICE, NDAQ, CME) vs ratings/index (SPGI, MCO, MSCI) — **flow +0.632 vs
  −0.518**, the split is the peer set.
- **Defence primes**: RTX +21.3 / GD +6.6 / LMT +11.3 / NOC −6.1 / LHX −11.7 RS60 vs SPY = **a 33pp
  spread inside five names (W5)**. Backlogs: **RTX $268bn (+23%) · GD $118bn (+30%)**.
- **AI-power**: CEG / VST (Utilities) vs GEV / VRT (Industrials) — **the basket straddles two GICS
  sectors and the file says so.**

---

## §E · Refutation + dated catalyst — what kills each section

| Section | What kills it | Date |
|---|---|---|
| **ENRG** | **S49 branch B: the settled 5-session distillate-crack change turning ≤ −5.0.** It is **+1.066** after +11.665 → +3.048, i.e. **one to two sessions from the line at the current ~−5.9/session pace** ⇒ **hits ENRG and INDU on the same tick.** ⚠ **The M91 premise behind that dual hit was WEAKENED by DEEP-INDU this run — quote the mechanism, not the magnitude.** | **08-06** |
| **ENRG (names)** | **S53 branch B**: MPC or PSX guiding **margin compression / hedging-timing lag / turnaround drag.** | **08-04 · 08-05** |
| **ENRG (regime)** | **S52**: a dated Strait reopening in a primary text (branch A) **or** a strike on named Iranian energy infrastructure (branch B). **Both branches falsify something the desk holds.** | **08-06** |
| **IT** | **S30's own anti-signal**: the {STX, MU, WDC} median RS20 falling back below 0 — **it is at +0.8, from +1.7 one session earlier.** | **08-05** |
| **IT (name)** | **S46**: the AAPL−QCOM RS20 spread. Leg 1 (GM guide down) is MET; leg 2 needs <+15pp and **it is +16.4pp**. | **08-13** |
| **FIN** | **S23 / S51**: derived 2s10s ≤ +0.20. It is **+0.45**, held two settled prints ⇒ **25bp away and receding.** ⚠ **And the OW's carrier changed for a third time — if the insurance node does not hold, there is no fourth reason on the shelf.** | **08-05 · 08-10** |
| **FIN (credit)** | **S41**: IG OAS ≥ 0.90%. It is **0.80% — 10bp away** — while a named AI issuer (**CoreWeave, $2.6bn**) had to **raise the spread to clear.** | **08-12** |
| **INDU** | **S42 branch A**: the {WAB, PCAR, MMM, ITW} median RS20 at or below 0. It is **+10.1**; ⚠ **branch B's SECOND leg (≥2 of 4 still 🟢) is already failing at 1 of 4.** | **08-12** |
| **UTIL** | **S24**: the {VST, CEG, GEV, VRT} median RS20 turning > 0. It is **−6.75**. ⚠ **DEEP-UTIL measured this as the ONE genuinely live bracket in the cluster — S35 and S47 both fired inside a noise band.** | **08-12** |

---

## §F · 🚨 Epicenter-starter module (PREMORTEM flagged a cycle GAP — this section exists because of it)

**`cycle_exposure` reads rank-2 Energy/oil-refining at 6.9% epicenter against an 8.0% floor —
a −1.10pp GAP.** The standing rule: **a crowded or 🔴 tape gates ADD timing; it never justifies zero
core in a top-rank cycle.**

**The cleanest UN-HELD epicenter expressions, named with numbers and NOT recommended (P4):**
- **XOM — flow +0.606, the highest of any Energy epicenter name held or unheld**, RS20 +13.1 /
  RS60 −2.9. ⚠ **NO-BASE (days 21-60 −16.0)** and **its refining tag in the registry is WRONG
  (DEEP-ENRG).**
- **VLO — RS60 +20.2, the best 60-day in the refining group, and the only refiner with a positive
  delta (+0.054).** ⚠ **L2 unrunnable (6th run) ⇒ no cheapness claim.**
- **Both are blocked from 🟢 by `vol_surge` alone (0.89 / 0.80 against a 1.20 gate), not by weak RS.**

⚠⚠ **Three facts are handed forward TOGETHER because separating them would flatter the GAP:**
(i) the registry says the book is under-exposed to the engine; (ii) **the engine's own commodity rate
has turned negative on the 3-2-1 and is one session from S49's branch-B line**; (iii) **the two
cleanest expressions are both NO-BASE on the desk's own test.** **No sizing follows from any of this
here (P4) — ALPHA owns the action bracket.**

⚠ **Rank-1 AI-compute reads ✅ at 13.02% vs a 12.0% floor, but the margin is +1.02pp and M146
measured these ✅s to be mark-to-market drift with nothing traded — and PREMORTEM confirmed it from a
second direction: NVDA rs60 −1.1, AVGO rs60 −12.1, TSM unmeasurable.** ✅ **is not a construction
claim.**

---

## §G · Set-aside names — every one is a SCORED record, none is silently absent

**Filed to `reject_ledger` (each with a reason class, a `--revives-if` and a `--recheck-date` — the
script refuses to run without the last two):**

| Ticker | Class | Why (measured) | Revives if | Recheck |
|---|---|---|---|---|
| **GRMN** | `H.밸류소진` | ★ **The first fundamental evidence filed on this name in three runs.** It is the sweep's **#1 flow of all 300 (+0.915)** with the **cleanest RS base on the board (+22.1 / +22.0, days 21-60 ≈ 0)** — **and the fundamental axis is exhausted**: FY25 gross margin **58.7% vs a 59.5% series max and a 55.9% median ⇒ ~90th pctile**, forward **27.02×**, **30d revisions 2↑:3↓ (turning DOWN)**, and the price is **3.4% ABOVE the mean target** | 30d revision breadth turns net positive, **OR** price falls below the mean target while RS20 vs SPY stays > +15 | **08-16** |
| **EA** | `H.밸류소진` | On the LIVE shortlist as a clean-rise (🟢, z −0.93) **but the revision book is the worst on the sheet at 30d 1↑:6↓**, +1y EPS only +3.7%/90d, price **1.9% ABOVE** the mean target, RS60 vs SPY only +0.9, and **no thesis exists in any desk file** | 30d revision breadth turns net positive, **OR** RS60 vs SPY clears +10 with the 🟢 tag intact | **08-16** |
| **TRI** | `C.차트붕괴` | Cited by ROTATION as one of the 5 Industrials greens carrying the promote — **PREMORTEM measured NO BASE on the desk's own M149 method: +9.7 / −0.4 ⇒ days 21-60 = −10.1, a pure 20-day event.** Revisions 1↑:2↓, +1y EPS −1.6%/90d | RS60 vs SPY turns positive on a settled close (a real days-21-60 base appears) while the 🟢 tag holds | **08-12** |

**Filed to `missed_ledger` — names that surfaced upstream and never reached a rejection** (⚠ the
sign is INVERTED vs the rejection ledger: `excess > 0` here means *missing it cost us*):

| Ticker | Class | Why | Enters if | Recheck |
|---|---|---|---|---|
| **ADM** | `U.발굴부재` | A **`new_green` on this run's sweep** (flow +0.510, `vol_surge` 1.36, +2.9 / −3.1) inside **Consumer Staples — a sector no MACRO proposition claims and which got no DEEP slot.** It appears in **no desk file, no thesis, no bracket**: surfaced by the instrument and never examined | Staples is promoted above N on a flow number, **OR** ADM's RS60 vs SPY turns positive with the 🟢 tag intact | **08-16** |
| **CTAS** | `Q.확신부족` | Carried as a coverage-gap row for a **third consecutive run** with numbers but no thesis: **+12.5 / +17.7 (days 21-60 +5.2 = a real base)**, flow +0.772, **blocked from 🟢 by `vol_surge` alone**, and **no 4Phase exists so no thesis can be written** | A 4Phase company analysis is produced, **OR** it clears the 🟢 gate with RS60 vs SPY above +15 | **08-16** |

**Re-filed rather than removed (the 475150 rule — a name whose measured flow still passes is not
deleted on narrative grounds):**
- **MU** — the story ("the memory turn") was handed to STX instead, but **MU's measured base is the
  basket's strongest (+41.2)**. It stays on the sheet under a **new thesis line — *"the base without
  the flow"*** — with a dated re-check at **08-05** (S30's window). **Not rejected, not dropped.**
- **BKR** — **#2 on the LIVE shortlist (+0.872) and its reject-ledger basis is already known-false**
  (filed 07-27 as *"the only negative flow score of 11 Energy names"*; it has since been the sector's
  #1). Its recheck date has not arrived so it is **not `due`** — **named here so a second run cannot
  pass it silently**, and it will surface at the next HANDOVER.

---

## §H · Sizing language and the exposure state — the honest answer is that this sheet cannot fill the target

**HANDOVER §6 carried the exposure state as `복귀` (RETURN) with a target invested 90%, cash 10%,
against a live invested read of 52.7% ⇒ a −37.3pp band breach.** The rule the EXIT CHECK sets is that
a `복귀` sheet must **either supply enough candidates to reach the target or say plainly that it
cannot.**

**It cannot, and here is why, stated rather than papered over:**
1. ⚠⚠ **The exposure state is measured on a KR benchmark (`069500.KS`) and the book it sizes is the
   KR contest book. This is the US sheet. Applying a KR-derived target to US names would be a W1
   cross-market transfer** — the exact failure this desk logs. **No US name on this sheet is sized
   against that target, and no US tilt is derived from it.**
2. **On this sheet's own merits the candidate set is thin, and the thinness is measured**: of the 17
   names in §A, **7 are NO-BASE or worse on the desk's own days-21-60 test** (XOM, ICE, ETN, CEG,
   VST, MPWR, PSX), **6 cannot be valued at all because L2 is structurally unrunnable**, and **3 were
   filed to the reject ledger.**
3. **The one section with a fired bracket in the desk's favour (UTIL) resolved AGAINST adding
   anything** — DEEP-UTIL's verdict is that the UW− stands on cleaner grounds.

⇒ **The correct statement is: this sheet does not produce a `복귀`-sized candidate list, and the
reason is evidence, not caution.** **No sizing, no buy/sell language, anywhere above (P4).**

---

## ✅ EXIT CHECK

- [x] **Every DEEP sector has a section** (ENRG · IT · FIN · INDU · UTIL); **cross-sector LIVE
      shortlist names are included (MET, ITW, MPWR, RTX, TRI, EA, GRMN, BKR, ICE, ETN, PCG, FTNT, GD,
      MSFT, STX) or explicitly dropped with a reason (§G).**
- [x] **Numbers cross-checked** — `days 21-60` re-derived two ways (desk JSON + independent yfinance)
      and agreeing to ≤0.5pp; `to mean target` computed from raw fields. **Blanks are blanks: six
      names carry `연간 데이터 없음` and no cheapness claim is made on any of them.**
- [x] Flow/positioning cross-read present per candidate (§C); **BET_SHEET.md written as ONE file.**
- [x] **Every set-aside name is in the ledger with a class AND a `--revives-if` AND a
      `--recheck-date`** (§G). **No permanent bans were filed.**
- [x] **No name was removed on narrative grounds while its measured flow still passed** — **MU and
      BKR are re-filed under new thesis lines with dated re-checks, not absent.**
- [x] **Names that surfaced upstream but never reached a rejection are in `missed_ledger`** with a
      class and an `--enters-if` (ADM, CTAS). **This sheet produced 3 rejections AND 2 missed entries
      — the funnel is scored on both sides.**
- [x] **Sizing language is consistent with the carried exposure state** — and §H states plainly that
      this sheet **cannot** fill a `복귀` target, with the W1 reason why it should not try.
- [x] Linter — run below.

---

*asof 2026-08-02 · sheet on settled 2026-07-31 data · 5 DEEP sections + cross-sector shortlist ·
3 rejections filed, 2 missed entries filed, 2 names re-filed rather than removed · L2 unrunnable on
6 of 17 names and said so · zero buy/sell, zero sizing (P4).*

---

# §B-TAGS · ALPHA freshness gate — appended 2026-08-02 by the `industry_US` ALPHA stage

> Separates "interesting" from "bettable NOW". Deterministic novelty (`theme_age --scope foreign`)
> runs FIRST, before any judgement. **Zero buy/sell, zero sizing (P4).**

## 0 · ⚠⚠ The gate itself did not fire, for a NINTH consecutive foreign-feed measurement — and that is F1

`theme_age --scope foreign`, this run's probes:

| Theme | Verdict | Accel | age (d) | n(90d) |
|---|---|---|---|---|
| **memory pricing** | 🟡ACCELERATING | **4.33×** | 81 | 501 |
| **refining margin** | 🟡ACCELERATING | **4.29×** | 65 | 125 |
| backlog | 🟡ACCELERATING | 2.72× | ≥90 | 2,637 |
| insurance | 🟡ACCELERATING | 2.69× | ≥90 | 3,939 |
| data center power | ⚪ECHO | 1.36× | 71 | 380 |
| short squeeze | ⚪ECHO | 0.61× | 66 | **71 — thin** |
| *(from MACRO §C-1)* yen intervention | 🟡ACCELERATING | **5.31×** | ≥90 | 89 |
| *(from MACRO §C-1)* Hormuz | ⚪ECHO | 1.67× | ≥90 | 6,161 |

**ZERO 🟢FRESH.** 🟢FRESH requires **age ≤14d AND acceleration ≥2×**; **the youngest theme on the
entire board is 65 days old.**

⇒ ★★ **This is F1 stated as arithmetic rather than as a complaint: 🟢LIVE has fired 0 times in 9
consecutive runs because the gate's age clause is one the foreign feed structurally cannot satisfy
for a theme this desk would ever bet on.** A theme reaches this desk's sheet by being *already
narrated*, which by construction makes it older than 14 days. **A gate that never fires is
indistinguishable from a universe with nothing in it, and neither leaves a row.**
⚠ **The gate is NOT loosened here** — changing a live gate needs a human (D11-class). **It is
reported, with the measurement, for the third consecutive escalation.** ⇒ **every tag below is
therefore 🟡PARTIAL or 🔴RESOLVED by construction, and no 🟢LIVE is issued.**
★ **R31's surviving half also holds**: the tool DID discriminate (**2 ⚪ECHO / 6 🟡ACCELERATING**), so
the verdict column is informative even though the 🟢 bucket is empty.

## 1 · Tags — every name from `BET_SHEET §A`, with evidence label, date and a re-check

**⚠ A 🟡PARTIAL is a dated appointment, not a shelf.** Every residual below carries an explicit
re-check date and is handed to `carryover` for the next run's inheritance packet.
**⚠ Every tagged name is carried forward INDEPENDENTLY of whether its sector holds a DEEP slot next
run** (the 006360 lesson: a tagged name lost its tracker when its sector rested and ran +12.3%
unowned).

| Ticker | Tag | Residual — what is missing for it to be more than 🟡 | Evidence label · date | Re-check |
|---|---|---|---|---|
| **STX** | 🟡**PARTIAL** · ⚠ **momentum-only, HARD-STOP stamped** | The A-grade base is the board's thinnest positive (**days 21-60 +3.7**) and **L2 reads the peak-margin trap in its purest form — gross margin at the MAX of a 17-year series against a 15.65× forward multiple with +1y EPS +39.7%/90d on 4↑:0↓ = consensus chasing.** ⚠ **B-grade disagrees with A-grade: FINRA z +1.23 (building) vs 5v5 −9.3▼ (falling) ⇒ `indistinguishable` (C4)** | `[measured]` sweep + `margin_history` + FINRA · 07-31 | **08-05** (S30 window) |
| **MU** | 🟡**PARTIAL** · re-filed, **not dropped** | ★ **The board's strongest base (days 21-60 +41.2) with the worst flow (🔴분산 −0.600).** Separator named by DEEP-IT: **MU's flow turning 🟢 while RS20 closes on RS60.** ⚠ **C2 on the margin: the ANNUAL series reads ~70th pctile while the QUARTERLY reads 100th — both quoted, neither alone** | `[measured]` · 07-31 | **08-05** |
| **MSFT** | 🟡**PARTIAL** | The only mega-cap spender that is 🟢 (+0.850, +18.7 / +9.8) — but **days 21-60 = −8.9**, i.e. the 60-day excess is a last-20 event, and no desk thesis owns it | `[measured]` · 07-31 | **08-12** (S13) |
| **MPWR** | 🟡**PARTIAL** · ⚠ **momentum-only, HARD-STOP stamped** | `new_green` with the board's 2nd-largest delta (+1.457) and **15↑:0↓ revisions — but RS60 −13.4 ⇒ days 21-60 = −23.8, NO BASE**, at a **40.98× forward multiple on a median-percentile margin** | `[measured]` · 07-31 | **08-12** |
| **FTNT** | 🟡**PARTIAL** | `new_green` and **RS60 +76.9 with days 21-60 +73.6 — the deepest real base on the sheet.** Residual: **C5 is unresolved** (this desk has never measured a valuation factor) and **the AI-security theme that would be its demand catalyst has NO registry row (D20)** | `[measured]` flow + `[news]` theme · 07-31 | **09-02** (CRWD ledger) |
| **MPC** | 🟡**PARTIAL** | Margin **below its own median (~37th pctile)** — the one refiner where the multiple is *not* a peak-margin artifact. Residual: **the commodity's rate has turned and S49 is 1–2 sessions from branch B.** ⚠ **Option book internally contradictory: skew +33.0 vs P/C 0.44 ⇒ `indistinguishable`** | `[measured]` · 07-31 · print **08-04** | **08-06** |
| **VLO** | 🟡**PARTIAL** | **Best 60-day of the refining group (+20.2) and the only refiner with a positive delta.** Residual: **L2 structurally unrunnable for a 6th run (D56) ⇒ no cheapness claim is available at all** | `[measured]` · 07-31 | **08-06** |
| **PSX** | 🔴**RESOLVED — dropped from the bettable list** | ⛔ **Three axes agree against it: A-grade days 21-60 −5.5 (EXHAUSTED) · B-grade FINRA z +1.53 = the only 🔴 short surge on the pull · options P/C 1.25 = the only fear profile.** ⚠⚠ **And the `action_bracket` CORE-STARTER still names it on R8's retracted rationale plus a short-flow clause whose SIGN IS NOW INVERTED (D19, 8th run).** ⚠ **`core_pick` is HUMAN-LOCKED and was NOT modified (P5)** | `[measured]` · 07-31 · print **08-05** | ledger row below |
| **XOM** | 🟡**PARTIAL** | Highest flow of any Energy epicenter name. Residual: **NO BASE (days 21-60 −16.0)**, **L2 unrunnable (3rd run)**, and ★ **its registry "0% refining" tag was measured WRONG this run** | `[measured]` · 07-31 | **08-05** (S31) |
| **MET** | 🟡**PARTIAL** | **The insurance node is the FIN OW's third stated carrier in three runs** (breadth-led → steepener → insurance). MET is 🟢 clean-rise with a real base (+10.7). Residual: **only +1.7% to its mean target**, and **L2 unrunnable on an insurer** | `[measured]` · 07-31 | **08-06** (S14) |
| **ICE** | 🔴**RESOLVED — dropped** | ⛔ **DEEP-FIN tied the `new_green` to its OWN earnings week via EDGAR (07-30 earnings = 07-30 Reg FD 8-K = `new_green` same day, ZERO M&A-category 8-Ks on file) ⇒ D51, the flow IS the event** — and **days 21-60 = −19.4, NO BASE** | `[measured]` + EDGAR · 07-31 | ledger row below |
| **RTX** | 🟡**PARTIAL** | ★ **The sheet's best A-grade shape: RS60 +21.3 with days 21-60 +13.6, 🟢, FINRA clean, and backlog +23% YoY to $268bn from the primary.** Residual: **L2 unobtainable (series ends FY2017) at 27.55× ⇒ no valuation claim can be made either way** | `[measured]` + 10-K · 07-31 | **08-12** |
| **GD** | 🟡**PARTIAL** | 🟢 with a thin real base (+4.3) and **backlog +30% to $118bn incl. $20.1bn of Navy submarine awards.** Residual: **the missile-defence cycle has NO dedicated DEEP mandate anywhere on this desk** | `[measured]` + 10-K · 07-31 | **08-12** |
| **ITW** | 🟡**PARTIAL** | 🟢 clean-rise with a thin real base (+4.6). Residual: ⚠ **margin at ~93rd percentile (44.1% vs a 44.3% max) with a FLAT book (1↑:1↓) at 23.27× and only +4.0% to target — peak margin, no revision momentum, full multiple.** It is also **the ONLY one of S42's four still carrying 🟢, so branch B's second leg is failing at 1 of 4** | `[measured]` · 07-31 | **08-12** (S42) |
| **ETN** | 🟡**PARTIAL** · ⚠ **momentum-only, HARD-STOP stamped** | ⛔ **NO BASE (days 21-60 −6.1)**; the `new_green` is a **same-day earnings print (D51)**; **z +1.49 vs 5v5 −6.7▼ ⇒ `indistinguishable`**; margin ~90th pctile at 26.24×. ★ **DEEP-INDU adjudicated it an AI-power name wearing an Industrials tag** | `[measured]` · 07-31 | **08-12** |
| **CEG** | 🟡**PARTIAL** | +34.3% to target, but ⛔ **NO BASE (days 21-60 −30.7) — bouncing, not turning** — with a **NEGATIVE +1y EPS trend (−1.6%/90d, 3↑:3↓)**, **L2 structurally unrunnable**, and **zero fresh hyperscaler PPA disclosures on EDGAR** | `[measured]` + EDGAR · 07-31 · print **08-06** | **08-12** (S24) |
| **VST** | 🟡**PARTIAL** | +49.8% to target (the sheet's largest) but ⛔ **NO BASE (−8.6)**, **negative revision trend**, **L2 unrunnable** | `[measured]` · 07-31 · print **08-07** | **08-12** (S24) |
| **PCG** | 🟡**PARTIAL** | Utilities' only 🟢 for a **4th consecutive run**, with a small real base (+1.6) and +31.8% to target. Residual: ⚠⚠ **a regulated utility has NO comparable gross-margin series ⇒ L2 structurally unrunnable, so the 9.63× forward is NOT a valuation claim (C3)**; **revisions 2↑:3↓**; **no 4Phase ⇒ no thesis**; and it **does not report until 2026-10-22**, so it cannot be what the sector is trading | `[measured]` · 07-31 | **08-07** (S35 window) |

**Tag counts: 🟢LIVE 0 · 🟡PARTIAL 15 · 🔴RESOLVED 2.**

## 2 · 🔴RESOLVED — dropped from the bettable list AND filed as ledger rows

Per the EXIT CHECK a 🔴 is dropped **and** logged with a reason class, a `--revives-if` and a
`--recheck-date`, so that "it's cheap" cannot resurface next run on memory rather than on evidence.

- **PSX** → `reject_ledger` `B.모멘텀only` — *"three axes agree against it into its own 08-05 print:
  days 21-60 −5.5 (EXHAUSTED), FINRA z +1.53 = the only 🔴 short surge on the desk's pull, and
  P/C 1.25 = the only fear/hedging option profile. The `action_bracket` CORE-STARTER still names it
  on R8's retracted rationale plus a short-flow clause whose sign is now inverted (D19, 8th run)."*
  **`--revives-if`**: *the FINRA short-vol z falls back below 0 (the surge reverses) **AND** days
  21-60 turns positive* · **`--recheck-date` 2026-08-12.**
  ⚠ **This does NOT touch the human-locked `core_pick` registry field (P5).**
- **ICE** → `reject_ledger` `B.모멘텀only` — *"the `new_green` is its own earnings week (07-30 print =
  07-30 Reg FD 8-K = `new_green` same day, zero M&A-category 8-Ks on EDGAR) ⇒ D51, and days 21-60 =
  −19.4 = no base. The venue-vs-ratings split it sits inside is real; ICE as a name is not the way to
  express it on today's numbers."* **`--revives-if`**: *RS60 vs SPY turns positive on a settled close
  while the 🟢 tag survives past the earnings-week window* · **`--recheck-date` 2026-08-12.**

## 3 · ★ Names carried INTO ALPHA that received no tag — filed to `missed_ledger`, not left silent

The L1's own instruction: *a name that receives no tag at all is not a 🔴, it is a MISSED entry, and
it leaves no record unless you write one.* Two such names, both already filed at BET:
**ADM** (`U.발굴부재`) and **CTAS** (`Q.확신부족`), each with an `--enters-if` and a **08-16** recheck.
★ **And the structural version of the same gap is named rather than buried: because 🟢LIVE cannot
fire (§0), EVERY name on this sheet is capped at 🟡 — so the distinction between "we looked and it
was only partial" and "the gate could not express better" is invisible in the tag column alone.**
**That is F1's cost, and it is why §0 carries the arithmetic.**

## 4 · Carry-forward list for the next run's inheritance packet (independent of DEEP slots)

**🟡PARTIAL, all 15**: STX · MU · MSFT · MPWR · FTNT · MPC · VLO · XOM · MET · RTX · GD · ITW · ETN ·
CEG · VST · PCG. **Nearest re-checks: 08-05 (STX, MU, XOM) · 08-06 (MPC, VLO, MET, CEG-print) ·
08-07 (PCG, VST-print) · 08-12 (the rest) · 09-02 (FTNT).**
**🔴 ledger rows to surface at `due`: PSX and ICE on 08-12; GRMN, EA on 08-16; TRI on 08-12.**
