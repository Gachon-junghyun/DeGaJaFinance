# SECTOR_DEEP_INDU — Industrials — industry_US — 2026-08-06 (Thu) · CONTINUOUS, **delta-led**

> **Carry by reference, not by reprint.** `llm_outputs/2026-08-05/industry_US/SECTOR_DEEP_INDU.md`
> is **not sparse** — it is a complete six-section file (9.6 KB) whose §1 segment test, §3 value-chain
> map (generation → transmission → switchgear → automation → DC integration → compute) and §5 chain-hop
> sweep are **still standing and are NOT re-derived here.** Everything in that file remains the
> structural base; this file carries only what moved and what the mandate asks.
> Flow/RS **`asof 2026-08-05 settled`** (`SECTOR_FLOW_US.json`). **D74 honoured**: the 2026-08-06 bar is
> partial and carries **no verdict** anywhere below; every price number is trimmed to ≤ 2026-08-05 and
> was reproduced independently in `yfinance` (`auto_adjust=False`). Benchmark **SPY** inline (C1).
> **Analysis only — zero buy/sell, zero sizing, no order language (P4).**

---

## 0 · The one-line answer

**Both pre-mortem lenses are right about different objects and the conflict resolves by disaggregation,
not by averaging: Lens 3 is correct that EMR's cycle KPI is dead, Lens 4 is correct that an
unregistered AI-power equipment cycle is being bid — but EMR is the wrong name to express it, because
EMR's own FY2025 10-K contains ZERO mentions of "data center" or "hyperscale" while ETN's names the
data-center market in Item 1's first sentence and names hyperscale customers by acquisition (A6).
The third axis neither lens used — the primary filing's customer disclosure — breaks the tie against
EMR. And the sector-level claim that INDU is "breadth-led" survives, but not for the stated reason:
47% of the eqflow>wflow gap is one 🔴 mega-cap (GEV) dragging the cap-weighted number down, and the
real breadth is in defense (9/10 names OBV 매집) and other capital goods — NOT in electrical
equipment, whose entire node signal is three names (EMR+ETN+AME eqflow +0.857; the other seven
+0.046).**

---

## 1 · Delta since 2026-08-05 — five things moved, everything else carries

| # | What changed | 08-05 read | 08-06 read | source |
|---|---|---|---|---|
| **D1** | **PWR decayed further** | RS20 **+2.4** | RS20 **−0.8**, delta **−0.401 = the worst delta in the sector** | `SECTOR_FLOW_US.json` |
| **D2** | **EMR/ETN both printed** — the 08-05 file did not have these | no earnings in window | **ETN 8-K Item 2.02 filed 2026-07-31**; **EMR 8-K Item 2.02 + 10-Q filed 2026-08-04**; **AME 8-K 2026-08-04** | `module_disclosure_us` |
| **D3** | **The two prints did OPPOSITE things to the revision books** | not measured | **ETN: NQ +3.0%/90d, NY +2.2%, 30d NY 5↑/0↓. EMR: CQ −0.0%, NQ +0.1%, CY +0.1%, NY +0.3%; 7d 0↑/1↓ on CQ, NQ AND NY** | `module_fundamentals_us` |
| **D4** | **The 08-05 verdict ("repair at one node, not a chain-wide ignition") is CONFIRMED and sharpened** | GEV/VRT distributing while ETN/EMR/AME accumulate | **unchanged and wider**: GEV **−0.664 🔴 분산**, VRT **−0.067 🟡, RS60 −22.6**; the three carriers still 🟢 volume-lit | JSON |
| **D5** | **The mandate's own sector-level claim is new** | not asked | INDU is the **only** OW-family sector with eqflow > wflow — verified across all 11 rows: gaps are INDU **+0.053**, MATR +0.096, COMM +0.010, RE +0.016, UTIL +0.006; **FIN −0.127, IT −0.245, ENRG −0.285, HLTH −0.020** | JSON `sector_rotation` |

**Unchanged and carried by reference (do not re-derive):** the 08-05 §1 segment test (EMR −4.5, ETN
−3.1, AME −3.5, PWR −14.7, defense median +2.3, rails median +4.7), the §3 chain map, the §3 binding
constraint (switchgear/transformer manufacturing capacity, from GEV's and ETN's own 10-Ks), and the
§5 negative chain-hop result. **§2's "repair, not ignition" verdict stands.**

---

## 2 · ★★★ The EMR conflict, resolved — this is the file's reason to exist

### 2a · The two claims, stated exactly

- **Lens 4 (PREMORTEM §4 / §4b)**: EMR is *"the cleanest expression of an unregistered
  AI-datacenter-POWER cycle"* — flow **+0.917**, OBV **매집**, `vol_surge` **1.45**, RS20 **+15.8** vs SPY.
- **Lens 3 (PREMORTEM §3)**: EMR is ⛔ **EXHAUSTED** — **CY +0.1%/90d**, **7d 0↑/1↓ on current-quarter,
  next-quarter AND next-year**, **days-21-60 vs SPY of −5.2**.

**Both were independently reproduced before being adjudicated.** My own `yfinance` pull to the 08-05
settle gives **EMR RS20 +15.77 / RS60 +10.61 ⇒ d21-60 = −5.16** (Lens 3's −5.2 ✅) and my own
`module_fundamentals_us EMR` pull gives **CQ −0.0% · NQ +0.1% · CY +0.1% · NY +0.3% over 90d**
(Lens 3's book ✅). **The flow row is Lens 4's ✅.** *Neither lens mis-measured anything.*

### 2b · ★★★ The tie-breaker neither lens used: A6 — name the customer, from the primary

`module_business_us --json`, full Item 1 + MD&A + customer sections, word-count on the primary text:

| Name | "data center" hits | "hyperscale" hits | Filing | What the filing actually says about the power end-market |
|---|---|---|---|---|
| **ETN** | **6** | **2** | 10-K, filed **2026-02-26** | *"We make products for the **data center**, utility, industrial…"* — **the first sentence of Item 1.** Fibrebond bought for *"multi-tenant and **hyperscale data center customers**"*; Resilient for solid-state transformers *"in **data centers** and energy storage"*; Boyd Thermal *"for **data center** customers"* |
| **AME** | **1** | 0 | 10-K, filed **2026-02-17** | one clause: UPS systems / power conditioning *"for smart grid applications, renewable energy applications and **data centers**"* — inside a list of ~12 end markets |
| **EMR** | **0** | **0** | 10-K, filed **2025-11-10** | ⚠⚠ **zero.** The only "power" language is segment-level: *"Sales for **Final Control** increased $176, or 4 percent, reflecting strength in **power end markets**"* — **Final Control is process valves and actuators**; the FY2025 growth line is *"**Measurement & Analytical** increased $466, or 13 percent"*. **The company's own disclosure attributes its power exposure to process industry, and never once to a data center.** |

⇒ **On the axis that decides what cycle a name belongs to, EMR fails and ETN passes.**
**Lens 4's node call is right; its name pick is wrong.** ETN's filing *is* an AI-datacenter-power
document; EMR's is a process-automation document that happens to sit in the same GICS sub-industry.

### 2c · Corroboration — three more independent axes, all pointing the same way

**(i) The cycle KPI that isn't a consensus estimate — revenue, XBRL-verified (B1, second derivative):**

| | latest qtr (end 2026-06-30) | y/y | prior qtr y/y | 2 qtrs back y/y | second derivative |
|---|---|---|---|---|---|
| **ETN** | **$8.53bn** | **+21.4%** | +16.8% (7.45 vs 6.38) | — | **accelerating, at 3× EMR's level** |
| **EMR** | **$4.87bn** | **+7.0%** | +2.9% (4.56 vs 4.43) | +4.3% (4.35 vs 4.17) | **accelerating — this is the strongest pro-Lens-4 fact in the file** |

`module_fundamentals_us`, yfinance↔SEC-XBRL cross-check **5/5 quarters within 0.0%** for EMR, **4/4**
for ETN. ⚠ **Stated honestly: EMR's top line IS re-accelerating.** But **it moved no EPS line** —
which means the sell side is reading the acceleration as mix / FX / acquired revenue rather than
cycle. ⚠ **C3**: this repo cannot separate EMR's organic from acquired growth — `unknown`, not
assumed.

**(ii) The prints themselves — same week, opposite consequence.** ETN reported **07-31**, EMR **08-04**
(both 8-K Item 2.02, EDGAR). ETN's book moved *after* its print (NQ +3.0%/90d, 7d NQ **3↑/0↓**,
CY 2↑/0↓, NY 2↑/0↓, 30d NY **5↑/0↓**). **EMR's did not** — and the one line with positive 7-day
breadth, current-year **2↑/0↓**, has a **mean that still fell, $6.51 → $6.50.** ⚠ **Report the
contradiction rather than pick a side (C2): breadth counter says up, the level says down.**

**(iii) The tape's microstructure disagrees with the OBV tag on EMR specifically.**
`scripts/us_flow.py` FINRA Reg SHO daily, **2026-08-05**: **EMR short-volume ratio 74.3% against its
own 20-day base of 62.5%, z +1.18 — the only positive z of the three carriers** (AME **−1.28**,
ETN **−0.24**). ⚠ **D6 / C4**: short-volume ratio includes market-maker hedging and is *not* a
directional verdict — but **OBV 매집 is a derived proxy and this is a measured print, and they point
opposite on EMR and the same way on AME.** Recorded as a contradiction, not resolved.

**(iv) Where EMR's RS20 actually came from.** Daily excess vs SPY, settled: EMR's single largest day
in the window is **2026-07-23 at +5.01pp — eleven sessions BEFORE its print** — and on that same day
**ETN +3.26 · AME +2.94 · PWR +2.89** all moved together. Decomposed: **RS20 +15.77 = +10.37 earned
before the last three sessions, +5.40 in the print window.** ⇒ **EMR's move is two-thirds a common
factor day and one-third an earnings response** — it is neither a clean company event nor a slow
accumulation.

### 2d · ⚠ The verdict — and what it is NOT

**Lens 3 is right about EMR as a NAME. Lens 4 is right about the NODE. They are not averaged and
neither is discarded**, because the resolving evidence shows they graded different objects:
**Lens 4 graded the tape (flow / OBV / RS / volume), Lens 3 graded the book, and neither graded the
filing.** On the filing — the only one of the three axes that can say *which cycle a name belongs to*
— **EMR is not an AI-datacenter-power name at all.**

- **EMR = price-live · KPI-dead · customer-unnamed.** ⛔ **Lens 3's EXHAUSTED tag holds.**
  **D154 checked, not assumed**: RS60 **+10.6 > 0**, so a base exists and "EXHAUSTED" is available.
- **ETN = the object-correct expression of Lens 4's node** — customer named in the primary, revenue
  +21.4% y/y and accelerating, revision book that moved *after* its own print, FINRA z −0.24.
- ⚠ **The honest counterweight to my own conclusion (C2):** ETN carries the **higher** multiple
  (fwd P/E **28.44** vs EMR **22.62**, PEG 3.13 vs 2.09) and the **lower** RS20 (+8.7 vs +15.8), and
  its short-pressure 5-day-vs-5-day trend is **+12.0▲** (rising). **B2 binds and is not satisfied:
  this repo has no margin-percentile instrument, so neither multiple is a valuation and neither name
  gets a valuation verdict — `unknown` (C3), and C5 forbids the multiple deciding it.** What the
  multiple *is* permitted to do here is be read **with** estimate momentum, and on that pairing the
  two names separate cleanly: **ETN = higher multiple with a rising book; EMR = lower multiple with a
  flat book.**
- **D6 signal grade**: the resolution rests on **primary filings (highest)** + **XBRL-verified
  revenue (highest)** + **consensus revision breadth (medium — it is sell-side opinion, not fact)** +
  **flow tags (medium — derived)**. **S1 does not bind**: this is four independent axes, not one
  observation.

---

## 3 · Sub-node decomposition — is the breadth real, or one sub-node?

**Method**: all **50** `Industrials` rows in `SECTOR_FLOW_US.json` (`asof 2026-08-05`), partitioned by
GICS sub-industry into the five nodes the mandate names. `eqflow` = simple mean of `flow_score`;
`wflow` = market-cap-weighted mean; both computed by me from the raw rows and **reproducing the
file's own sector line exactly (eqflow +0.179 / wflow +0.126) — the partition is arithmetically
complete.**

| node | n | **eqflow** | **wflow** | cap | cap share | flow > 0 | OBV 매집 | 🟢 | `vol_surge` ≥1.2 | median RS20 | median RS60 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Defense primes & aero** (LMT GD NOC LHX RTX HWM TDG BA GE AXON) | 10 | **+0.243** | **+0.276** | $1,360bn | 26.1% | **9/10** | **9/10** | 1 | 3 | +1.4 | +4.9 |
| **Electrical equipment** (EMR ETN AME ROK VRT GEV PWR JCI TT CARR) | 10 | **+0.289** | +0.125 | $1,142bn | 21.9% | 6/10 | 5/10 | **3** | **7** | **−0.9** | **−2.9** |
| **Capital goods, other** (20 names: TRI CTAS ITW ADP PAYX MMM PH FAST HON URI FER PCAR EME CMI CAT FIX DE GWW WM RSG) | 20 | +0.201 | +0.117 | $1,915bn | 36.7% | 12/20 | 11/20 | 1 | 5 | +3.9 | +4.3 |
| **Rails & freight** (UNP CSX NSC UPS FDX ODFL DAL UAL UBER WAB) | 10 | **−0.039** | **−0.103** | $804bn | 15.4% | 5/10 | 4/10 | **0** | **0** | +1.8 | +6.2 |
| **SECTOR** | **50** | **+0.179** | **+0.126** | $5,220bn | 100% | 32/50 | 29/50 | 5 | 15 | +1.9 | — |

### 3a · ★★ The gap is 47% one 🔴 mega-cap — the "breadth-led" label is half arithmetic

The eqflow−wflow gap decomposes exactly as **Σ (1/n − w_i)·flow_i = +0.0525**. The largest single
contributors:

| name | cap | cap weight | flow | **contribution to the gap** | share of gap |
|---|---|---|---|---|---|
| **GEV** | $298bn | 5.71% | **−0.664 🔴** | **+0.0247** | **47%** |
| TRI | $34bn | 0.66% | +0.937 🟢 | +0.0126 | 24% |
| **CAT** | $454bn | 8.70% | **−0.112 🔴** | +0.0075 | 14% |
| GE | $374bn | 7.16% | +0.229 | **−0.0118** | −22% |
| ETN | $164bn | 3.14% | +0.878 | **−0.0100** | −19% |

⇒ **"eqflow > wflow" is not primarily small names being bought; it is two large 🔴 names (GEV, CAT =
14.4% of sector cap) pulling the cap-weighted mean down.** GEV alone is nearly half the gap.
⚠ **The label "breadth-led" is still defensible — but on a different number**: **32 of 50 names carry
positive flow and 29 of 50 are OBV 매집**, and that is real breadth measured directly rather than
inferred from a weighting difference.

### 3b · Leave-one-node-out — the gap is NOT a single-node artifact, but its size is

| drop | eqflow | wflow | gap |
|---|---|---|---|
| drop defense | +0.163 | +0.074 | **+0.089** |
| drop rails & freight | +0.233 | +0.168 | **+0.065** |
| **drop electrical equipment** | +0.151 | +0.126 | **+0.025** |
| drop other capital goods | +0.164 | +0.132 | **+0.032** |

**The sign survives every deletion ⇒ the gap is not an artifact of one sub-node.** But it **halves**
when electrical is removed — because GEV leaves with it. **Answer to the mandate: real in sign,
overstated in size, and the node that supplies most of its magnitude supplies it through a name
that is being SOLD.**

### 3c · ★★★ "Electrical equipment" is not a node. It is three names.

| sub-group | n | **eqflow** | cap | cap share of sector |
|---|---|---|---|---|
| **EMR + ETN + AME** | 3 | **+0.857** | $303bn | **5.8%** |
| **the other seven** (ROK VRT GEV PWR JCI TT CARR) | 7 | **+0.046** | $839bn | 16.1% |

**The node's +0.289 eqflow is entirely three names; the remaining seven are flat.** This is the
08-05 file's §4 finding, now quantified: the bid is at one point of the chain, not along it.

### 3d · B5 — dispersion, re-tested against M174

- Name-level **RS20 range 31.6pp** (EMR +15.8 → VRT −15.8), **sd 7.00pp**, **mean +1.14pp**.
- The **sector's own move**: **XLI 20-session excess vs SPY = +0.01pp** (my pull), 5-session **−0.04pp**.
- **range ÷ sector mean = 27.8× · sd ÷ sector mean = 6.2×.** **M174 measured this split at 21×; on
  today's settled bar it is 27.8× — the split has WIDENED, not converged.**
- ⇒ **B5 binds and is stated plainly: "Industrials" is the wrong unit.** The sector line (+0.01pp of
  excess) contains a 31.6-point internal range. Every conclusion in this file is a node conclusion or
  a name conclusion; **none is a sector conclusion**, and the OW− should not be read as a statement
  about 50 names.

### 3e · What actually carries the breadth — and it is not the story anyone is telling

**Defense: 9/10 positive flow, 9/10 OBV 매집, median RS60 +4.9 — the broadest and quietest node in
the sector, with exactly one 🟢 tag (BA, new-🟢, `vol_surge` 1.23).** ★ This directly corroborates
**PREMORTEM §4 finding C**: the cycle registry bifurcates RTX from the primes on a 2026-07-17
observation (*"LMT −0.742 / NOC −0.683, both distributing"*) that **today's tape falsifies —
LMT +0.576 · LHX +0.356 · GD +0.271 · NOC +0.111, all 매집, and LMT's flow now exceeds RTX's
(+0.196, delta −0.369).** **C4: the bifurcation is indistinguishable on today's tape.** The
breadth-led claim is true, and its carrier is the node with **no** 🟢 tags — which is precisely why
the 🟢 filter did not find it (**PREMORTEM §3 finding 2, same shape**).

---

## 4 · S62's mechanism read — ⚠ NOT re-scored, it settles on its own frozen construction

**Independent reproduction (my own `yfinance` pull, settled ≤ 08-05, SPY inline):**
EMR **+15.77** · ETN **+8.67** · AME **+6.85** · PWR **−0.77** ⇒ **median +7.76**; **XLU −7.02**
⇒ **spread +14.78** against the premortem's +14.8 and **+14.51 at registration**. **Reproduced to
0.02 by a second method. Bands: A ≤ −5.9 (one bet) · B ≥ +7.4 (survives). It settles 2026-08-07.**

**Which branch the mechanism favours: B — but for a reason the observable cannot see, and the
"survives" reading it will produce is weaker than it looks.**

**FOR branch B (two bets), evidence-ranked:**
1. ★★ **Composition.** The S62 basket is **3 electrical names + PWR = 5.8% of INDU's cap and 6% of
   its names** (§3c). Removing electrical entirely **leaves INDU's flow positive on both axes
   (eqflow +0.151 / wflow +0.126)** and leaves 26 of 40 remaining names with positive flow.
   ⇒ **the INDU OW− does not depend on the S62 basket at all.** Whatever S62 settles, it is testing a
   three-name node against a whole sector — **it cannot falsify "INDU OW− ≠ UTIL UW inverted", because
   94% of INDU is not in the observable.**
2. ★★ **PWR is the tell, and it points against a single AI-power trade.** PWR is the sector's purest
   interconnection/build-out contractor. If the two legs were one rotation out of power *ownership*
   into power *build*, PWR should be on the strong side. It is the **weakest leg of the basket
   (RS20 −0.8, RS60 −12.7) and carries the worst delta in the entire sector (−0.401)**, and it
   **decayed from +2.4 to −0.8 since 08-05**. The build leg is being sold alongside the utilities.
3. **Node span.** UTIL's UW is unanimous across names with no AI offtake at all — **SO −0.338,
   DUK −0.367, AEP −0.617, D −0.835, all 🔴 분산** — while the INDU carriers are three names with a
   named data-center customer base. **A single bet requires one mechanism; a regulated-utility
   selloff and a switchgear bid do not share one.**

**AGAINST branch B / the honest crack (C2):**
1. ⚠⚠ **A rotation produces divergence, and divergence is exactly what this observable rewards.**
   The premortem's own finding — **EMR 1.45 / ETN 1.38 / AME 1.28 volume-lit accumulation against
   VST 1.36 / SO 1.24 / DUK 1.39 volume-confirmed DISTRIBUTION** — is the signature of *one* trade
   with two sides. **S62 will read that as "two bets survive" while it is economically one book
   rotating.** ★ **This is the sharpest thing this file can say about S62: the construction cannot
   distinguish "two independent ideas" from "one rotation", and it will settle B either way.**
2. ⚠ **The rates evidence removes the alternative explanation for the UTIL leg.** `MACRO P1‴` has
   the long end **falling** (DGS10 −7bp, T10YIE 2.22 near the bottom of a 2.18–2.50 365-day range).
   **Utilities are the worst sector on every axis while yields fall** ⇒ **the UW UTIL is not a
   duration bet**, which is what would have made it independent of the power theme. Removing duration
   makes the two legs *more* likely to be one power trade, not less.
   ⚠ **This also matters for S63** (`DUR = (XLU RS20 + XLRE RS20)/2 − XLF RS20`, settles 08-13):
   **if XLU's weakness is not rate-driven, S63's duration framing is carrying a leg that isn't a
   duration leg.** Flagged for the FIN/RE owners; **not re-scored here.**
3. **A5 — `[unverified]`**: no lead/lag between the equipment leg and the utility leg has been tested
   in this repo. The claim "money is rotating from one to the other" is a **co-movement observation,
   not a measured lead/lag**, and is tagged as such.

**Net read, for the record before it settles:** ⇒ **the mechanism favours B, and B should be read
narrowly — "the 3-name equipment node and the utility complex kept diverging", NOT "Industrials and
Utilities are independent ideas."** The two GICS labels overlap in **~6% of INDU**, and inside that
6% the overlap is real. ⚠ **The `enters-if` failure to watch is PWR**: it is the only basket member
that belongs to the utilities' own supply chain, and it is failing on both windows.

---

## 5 · ★★★ M91 tested against primary filings — the mechanism transmits with the WRONG SIGN

**§G row 7's claim**: *"XLI exc5 −0.04 / exc20 +0.01 — the flattest sector on the board, on both
windows. A 12% crude fall is a direct input-cost tailwind (M91) and the sector produced zero relative
move."* **S64 brackets exactly this forward (08-05 → 08-13).**
⚠ **R38 respected: UNP's retracted "~8 of 12 growth points are surcharge" magnitude is NOT re-imported
below. Every number here is read fresh from a filing.**

### 5a · First, a measurement error in the framing itself

| window | crude (`CL=F`, settled) | XLI excess vs SPY |
|---|---|---|
| 3 sessions | **−11.16%** | — |
| 5 sessions | **−10.94%** | **−0.04pp** |
| 10 sessions | **−13.37%** | — |
| **20 sessions** | **+2.31% — crude is UP** | **+0.01pp** |
| from the 07-23 high ($92.19) | **−18.41%** | — |

⇒ **§G paired a ~10-session crude move with a 20-session sector excess. Over the 20-session window
crude ROSE 2.3%, so `exc20 +0.01` is not evidence about fuel at all.** The only window that tests the
mechanism is **exc5 (−0.04pp on a −10.9% crude move)**. ★ **S64's forward 6-session construction is
the right window and §G's exc20 is the wrong one** — a second, independent instance of the D122 shape
the premortem already caught once in S64's own registration.

### 5b · The filings — `module_business_us --json`, MD&A, quoted

| name | filing | fuel surcharge REVENUE | fuel EXPENSE | the disclosed mechanism |
|---|---|---|---|---|
| **UNP** | 10-K **2026-02-06** (FY2025) | **$2.3bn** in 2025 vs **$2.6bn** in 2024; *"Fuel surcharge revenues in 2025 **decreased $218 million**"* | **$2,390m** vs $2,474m = **−$84m** | *"there will be a **timing impact on earnings**, as our fuel surcharge programs **trail** increases or decreases in fuel prices by **approximately two months**"* |
| **NSC** | 10-K **2026-02-09** (FY2025) | **$828m** (2025) vs **$962m** (2024) vs **$1.2bn** (2023) = **−$134m** | **$932m** vs $987m = **−$55m** | *"Approximately **95% of our revenue base is covered by contracts that include negotiated fuel surcharges**"*; 366m gallons consumed |
| **CSX** | 10-K **2026-02-12** (FY2025) | not dollar-disclosed in MD&A ⇒ **`unknown` (C3)**; total revenue **−$448m (−3%)** attributed partly to *"lower fuel recovery"* | *"Fuel expense **decreased $73 million** primarily due to a **7% decrease** in locomotive fuel prices"* | same pass-through structure, magnitude undisclosed |
| **UPS** | 10-K **2026-02-17** (FY2025) | *"Fuel surcharge revenue **increased $282 million** in 2025, as a result of **revenue quality actions**"* | *"Fuel expense **decreased $50 million** mainly attributable to lower prices for jet fuel, diesel and gasoline"* | US Domestic revenue-driver table: **Fuel Surcharge +0.5pp** of a −1.4% total; International **+0.2pp** of +3.4% |
| **FDX** | 10-K **2026-07-20** (FY ended May 2026) | not separately dollar-disclosed ⇒ **`unknown` (C3)**; revenue +8% *"due to … **higher fuel surcharges**"* | **$4,052m = 4.3% of revenue**, vs $3,775m = **4.3%** prior year; *"Fuel expense increased 7% … due to **higher fuel prices**"* | *"approximately **61% of our jet fuel is purchased based on the index price for the preceding week**"* |

### 5c · ⇒ The verdict on M91

**M91's mechanism is REAL and its magnitude was OVERSTATED — and on the two names that disclose both
sides in dollars, the full-year NET sign is NEGATIVE, not positive:**

| | surcharge revenue Δ | fuel expense Δ | **net pre-tax** |
|---|---|---|---|
| **UNP FY2025** | **−$218m** | **−$84m** | **−$134m** |
| **NSC FY2025** | **−$134m** | **−$55m** | **−$79m** |

**Two independent primaries, same direction: a year of falling fuel COST RAILS MONEY**, because the
surcharge revenue falls faster than the fuel expense does. **Fuel is a large gross line** — UNP's
$2,390m is **16.3% of total operating expense and 9.8% of revenue**, and UNP's surcharge revenue is
**96% of its own fuel expense**; NSC's surcharge covers **89%** of its fuel bill on a **95%-contracted
revenue base**; FDX's fuel ratio was **4.3% in both directions** — **and precisely because it is
contractually passed through, it is a near-zero NET lever.** The only real earnings lever is the
**~2-month lag**, which is **transitory and sign-flipping**, not a re-rating.

⚠ **C2, the other half — parcel is not rail.** **UPS is the one counter-case**: surcharge revenue
**+$282m** while fuel expense **−$50m** ⇒ **+$332m net**, because UPS's surcharge is set by
*"revenue quality actions"* rather than purely by index. ⇒ **the pass-through is tighter at the rails
than at the parcel carriers**, and M91 should never have been applied to the two groups as one lever.

**⇒ The answer to §G row 7: XLI's flatness is not a failure to transmit. It is the CORRECT response.**
A move would have been the anomaly. **The flow agrees**: the rails & freight node is the **only** node
in the sector with **negative eqflow (−0.039), zero 🟢 tags and zero names at `vol_surge` ≥ 1.2**
(UNP +0.099 중립 · CSX +0.297 · NSC +0.414 · UPS −0.319 · FDX −0.658 🔴) — **the tape is not pricing a
fuel windfall because the filings say there isn't one.**

**Read on S64 (settles 08-13, NOT scored here):** the mechanism predicts **neither branch** — a null
in the dead zone between −1.8pp and +1.9pp. ⚠ **The way S64 resolves A or B is if something OTHER
than fuel moves XLI**, and the two candidates are the defense node (26% of cap, 9/10 매집) and CPI
08-12. **If S64 settles B, do not attribute it to fuel without re-reading this section.**
⚠ **The one true fuel effect to watch is DELAYED**: UNP's own two-month lag puts the transient margin
benefit of the July–August crude fall in the **fiscal-Q4 prints (late Jan 2027)**, not in an
August tape.

---

## 6 · The ERCOT receipt — both branches, argued

**The receipt, re-verified independently** (`module_news_data fts search ERCOT interconnection
--mode and --days 5 --scope foreign --full`, 9 matches): **techcrunch 2026-08-04** carries the
primary quote — *"In January, ERCOT had **233 gigawatts** of projects waiting to connect… Today,
Abbott's office said ERCOT is tracking **474 gigawatts** of new connection requests. About **90%** of
those are data centers… more than **five times ERCOT's total peak demand**"*, with PUCT+ERCOT audits
covering *"on- and off-site demand for electricity and water, noise mitigation, light controls, use of
tax incentives, and ownership details."* **A second outlet (tomshardware, 2026-08-04, citing the Texas
Tribune) independently calls it a *"moratorium on all data center approvals … until the agencies have
completed an audit"* and puts the count at ~1,800 data centers.** ⚠ **D5 partial**: both bodies trace
to Abbott's office as the single primary source.

### 6a · FOR the electrical-equipment leg

1. **A queue at 5× peak demand cannot be met by generation on any timeline; it can only be rationed
   by grid hardware** — and rationing at a bottleneck raises lead times and price *at the bottleneck*.
   The 08-05 file's §3 already located that bottleneck in the primaries: **GEV's 10-K flags Grid
   Solutions lead-times "increased as a result of demand outstripping supply"; ETN's three 2025–26
   acquisitions all buy capacity at the switchgear/modular-power/cooling nodes.**
2. **The audit's burden falls on the developer and the utility, not the equipment maker.** The
   deliverable list is unchanged; **equipment already ordered still ships** (Card 3's own branch).
3. ★ **The behind-the-meter response is content-additive.** If grid interconnection is gated,
   projects move to on-site generation — which **increases** switchgear, paralleling gear and
   distribution content per MW rather than removing it. **This is the branch under which the receipt
   is genuinely bullish for the node.**

### 6b · AGAINST

1. ⚠⚠ **A queue is not a build, and the body says so**: *"Some of those projects are simply paper
   proposals… Many projects fizzle out."* **474 GW is an application count.** **A6 fails**: no
   equipment maker has disclosed a Texas- or ERCOT-attributable backlog figure — the receipt **cannot
   be converted into a disclosed order at any name in the universe.**
2. **The audit gates the step that PRECEDES the order.** Medium-voltage gear is ordered after an
   interconnection agreement. A permitting slip moves order dates right — hitting **2027 revenue**,
   which is exactly the line the market has been paying for (**ETN next-year +2.2%/90d, 30d 5↑/0↓**).
3. ★★ **The money is already on this side, and the clearest tell is inside INDU, not utilities.**
   **PWR — the sector's purest interconnection-build contractor — carries the worst delta in the
   sector (−0.401), RS60 −12.7, RS20 decayed +2.4 → −0.8.** Every Texas-proximate name is 🔴 or 🟡:
   **ETR −0.581 🔴 · VST −0.315 🔴 (`vol_surge` 1.36 = volume-confirmed distribution) · GEV −0.664 🔴 ·
   CEG +0.167 🟡 RS60 −17.0 · VRT −0.067 🟡 RS60 −22.6.**
4. ⚠ **C3, the honest gap:** **none of EMR, ETN or AME discloses Texas or ERCOT exposure in the
   filings read for this file.** The transmission from this receipt to the three carriers is
   **`unknown`, not positive.**

### 6c · Net

**The receipt cuts AGAINST the interconnection/build and offtake legs — and that verdict is already
paid for in the tape (PWR, ETR, VST, GEV, CEG). It is `unknown` for the equipment leg, not
supportive.** The one branch on which it is genuinely FOR — behind-the-meter distribution gear —
**has no clean expression inside `us_top300`**: the names the theme's own bodies keep surfacing
(**nVent, Atkore, Prysmian**) are **outside the universe ⇒ `unknown` (C3)**. ★ This is the same hole
**PREMORTEM §4 finding D** identified from the other direction: *"no exposure guard can ever fire on
it."* **Confirmed here from the news side as well as the registry side.**

---

## 7 · Chain-hop candidates, each flow cross-checked

### 7a · ⚠⚠ Tool-integrity incident — reported, not hidden

**The first two `chain-hop` invocations with my arguments (`"data center" power --days 7`) returned
ANOTHER concurrent stage's query**: the header echoed **`테마: steel scrap (506 articles)`** and the
candidate list was Buffett/beverage names. **The shared NEWS API (ngrok) multiplexed a concurrent
run's result into mine.** A third call returned the correct `terms` echo. ⇒ **every chain-hop output
below was re-run and its `terms` echo verified against what I passed.** ⚠ **Any chain-hop result in
this run's other files that was not echo-verified should be treated as suspect** — this is the same
class of hazard as the 08-06 `industry_US` D74 incidents, but on the news side.

### 7b · `chain-hop "data center" power --days 7 --mode and --scope foreign` (1,308 articles, verified echo)

Headline-named (crowded, excluded by construction): NVDA 66 · AMZN 63 · AMD 60 · MSFT 51 · MU 39 ·
AAPL 37 · GOOGL 33 · PLTR 20.

| candidate | near / body hits | flow cross-check (`asof 08-05`) | verdict |
|---|---|---|---|
| **MMM** | 8 / 45 | fs **+0.517** 🟡 · OBV **매집** · RS20 **+14.4** · RS60 **+22.7** · ⚠ `vol_surge` **0.73 = velocity-lit (D6, lower grade)** · FINRA z **−1.38** (short pressure below base) | ⚠ **WEAK-PASS on flow, FAIL on provenance.** The sample title is a Meta-capex article — the proximity is consistent with 3M appearing as an index constituent, not as a supplier. **Not handed forward.** |
| **FIX** (Comfort Systems — DC mechanical contractor, the object-correct trade) | 6 / 6 | fs **−0.260** · OBV **분산** · RS60 **−15.4** · delta **−0.349** · sample title literally *"3 Construction Picks Set for More Gains … on AI-Data Center Boom"* | 🚫 **FAILS.** **The theme names it and the money is leaving it** — the same shape as the 08-05 file's GS result. |
| **HON** | 3 / 10 | fs **+0.483** 🟡 · 매집 · RS20 +9.3 · RS60 +6.6 · ⚠ `vol_surge` **0.67 velocity-lit** · FINRA z −1.17 | 🟡 **weak-positive, low grade.** Not distinguishable from the sector's own capital-goods breadth. |
| **EQIX** | 4 / 4 | fs +0.361 🟡 · 매집 · RS20 **+0.7** · RS60 **−5.8** · `vol_surge` 1.14 · delta +0.219 · FINRA **z +1.15** (short pressure rising) | ⚠ **MIXED, and not Industrials.** Accumulation with negative 60-day RS and rising short pressure. **C4: indistinguishable.** |
| **ETR** | 5 / 5 | fs **−0.581 🔴 분산**, RS20 −9.8 | 🚫 **FAILS** — already in EVENT_ALPHA Card 3, already 🔴. |
| KO · CCEP · PEP · NFLX · CTVA · CMG · NEM | 3–8 | — | 🚫 **Instrument noise.** These are ticker/name-pattern false positives inside the matcher (Buffett articles, earnings-call transcripts). **Named so the next run does not re-discover them as signal.** |

### 7c · ★ The real chain-hop finding is a hole, not a name

**The bodies name the object-correct beneficiaries and the instrument cannot see them.** Sample
titles surfaced in this very sweep include *"nVent Electric Q2 Earnings Beat Estimates"*, *"Why nVent
Electric Crushed Estimates Again"*, *"Atkore Stock Surged Because Prysmian Agreed To Buy It For
Cash"*, *"AI Power Crunch Drives Huge Expansion in Off-Grid BESS"*, *"Big Tech's AI Data Centers Are
Turning to Bloom Energy for Power"*. **NVT, ATKR and Prysmian are all outside `us_top300` ⇒ no flow,
RS or OBV row exists ⇒ `unknown` (C3), not a level.** ⇒ **the chain-hop universe is structurally
blind to the mid-cap electrical layer this theme is actually naming**, which is the same universe
hole that makes §6c's "FOR" branch unexpressable. **Stated as a negative result and a tooling gap,
not padded with a candidate that only passes because it is large.**

---

## 8 · Track KPIs and anti-signals — dated observables

**Registered brackets (owned elsewhere, NOT re-scored here):** **S62 settles 2026-08-07**
(running +14.78, branch B) · **S64 settles 2026-08-13** (forward XLI 6-session excess) ·
**S63 settles 2026-08-13.**

**KPIs — the EMR/ETN adjudication (§2):**
1. **EMR's CY or NY consensus rising > 1%** on a settled pull ⇒ **Lens 3's EXHAUSTED tag flips and
   §2d is wrong.** Recheck **2026-08-13** and **2026-08-20** (Lens 3's own flip condition, adopted
   unchanged).
2. **EMR filing a document that names a data-center customer or end market** (next 10-K due ~Nov 2026;
   any 8-K sooner) ⇒ **the A6 tie-breaker in §2b is voided and Lens 4's name pick is rehabilitated.**
   ⚠ **No date exists for this and none is invented.**
3. **ETN's next-year estimate breadth staying net-positive** (today 30d **5↑/0↓**) at the
   **2026-08-20** pull ⇒ the object-correct read holds. **A 2nd consecutive weekly cut to ETN's NY
   line ⇒ the node's book is rolling and §2d's ETN half fails with it.**
4. **EMR's revenue second derivative (B1)**: y/y went **+4.3% → +2.9% → +7.0%**. **The next print
   (fiscal Q4, ~Nov 2026) below +7.0% y/y ⇒ the acceleration was one quarter**, and the only pro-Lens-4
   fundamental fact in this file expires.

**KPIs — sector structure (§3):**
5. **GEV's flow turning positive** ⇒ **47% of the eqflow>wflow gap disappears and the "breadth-led"
   label must be re-derived from the 32/50 count instead.** Watch on any settled bar; formal recheck
   **2026-08-13**.
6. **Defense node holding ≥ 8/10 OBV 매집** at the **2026-08-13** flow file ⇒ the real carrier of the
   breadth persists. **Falling below 6/10 ⇒ INDU's OW− loses the node that actually supports it**,
   regardless of what the three electrical names do.
7. **B5 re-measure**: RS20 range ÷ sector mean, today **27.8×** (M174: 21×). **Below 15× by
   2026-08-20 ⇒ the label starts becoming the right unit again.**

**Anti-signals — dated, and each one kills something specific:**
- 🔻 **Two of {EMR, ETN, AME} turning OBV 분산** on a settled bar ⇒ §3c's three-name node collapses to
  "two earnings pops", and EVENT_ALPHA Card 4's own kill condition fires. Recheck **2026-08-13**.
- 🔻 **XLU printing any 🟢** (today **0 of 15**) ⇒ Card 4's kill; and S62's spread compresses toward
  branch A from the other side.
- 🔻 **PWR RS20 falling below −5** ⇒ the build leg is being sold outright and §4's point 2 hardens
  from "tell" to "confirmed"; **PWR RS60 crossing above 0** ⇒ the 08-05 file's `enters-if` clears and
  §6b point 3 is wrong. Recheck **2026-08-19**.
- 🔻 **UNP/CSX/NSC posting a fuel-surcharge revenue INCREASE alongside a fuel-expense decrease** in
  any quarterly filing ⇒ §5c's negative-sign finding is wrong and M91's original direction is right.
  **Next rail prints: mid-October 2026 (Q3).** ⚠ **No sooner — this cannot be settled on an August
  tape.**
- 🔻 **An ERCOT/PUCT statement that the audit is procedural with no queue impact, or CEG/VST guiding
  contracted demand UP** ⇒ §6c is wrong. **VST printed 2026-08-07; CEG 2026-08-06** — both
  post-date this file's data.
- 🔻 **A concurrent-run `chain-hop` result appearing without a verified `terms` echo** ⇒ §7's
  candidate list is unusable. **Verify the echo every run** (§7a).

**Stated as unmeasured rather than guessed (C3):**
- **EMR's organic vs acquired revenue split** — no instrument in this repo. `unknown`.
- **Margin percentiles for every name in this file** — **B2 cannot be satisfied**, so **no valuation
  verdict is issued for EMR, ETN or AME.** The multiples appear only paired with estimate momentum.
- **EMR's 2026-08-04 8-K guidance text** — **SEC returned HTTP 403** to the fetch; the print's
  guidance language is **unread**, and the §2 verdict deliberately does not lean on it.
- **CSX's and FDX's fuel-surcharge revenue in dollars** — not disclosed in the MD&A sections read.
- **NVT · ATKR · Prysmian** — outside `us_top300`; **no flow/RS/OBV row exists.** `unknown`.
- **A5 `[unverified]`** — no lead/lag test exists between the equipment leg and the utility leg; the
  rotation language in §4 is co-movement, not measured causation.

---

*asof 2026-08-06 · flow/RS settled **2026-08-05**, D74 honoured throughout · S62 spread reproduced
independently at **+14.78** (registration +14.51) and **not re-scored** · the EMR conflict resolved on
a third axis (primary-filing customer disclosure, A6) rather than averaged (C4) · sub-node
decomposition arithmetically complete against the file's own sector line · M91 tested against five
primary filings and found **real in mechanism, wrong in sign on a full-year basis** · one tool-integrity
incident reported (§7a) · six items reported as unmeasured rather than guessed.
**Analysis only — zero buy/sell, zero sizing (P4).***
