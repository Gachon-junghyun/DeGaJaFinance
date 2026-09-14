# SECTOR_DEEP_RE — Real Estate — industry_US — 2026-07-25 (Sat)

**benchmark: SPY throughout.** Data asof settled session **2026-07-24** (US closed 07-25).
Universe = the desk's 12 RE names in `SECTOR_FLOW_US.json` (sector cap $865.4bn), extended where
stated. Analytical artifact only — no positions, no sizing, no execution.

---

## §0 · Mandate (A) — is R7 five observations or one?

**Verdict: the DIRECTION replicates independently; the MAGNITUDE is one observation.**

I first reproduced the pre-mortem's own figure. Excess return vs **SPY** over the trailing 60
sessions, decomposed into the last 20 vs days 21–60:

| | exc60 vs SPY | last 20 | days 21–60 | share in last 20 |
|---|---|---|---|---|
| WELL | +13.97pp | +12.04 | +1.35 | **86.2%** |
| VTR | +11.38pp | +15.03 | **−3.60** | **132.1%** |

Reproduced to the decimal. Now the test the replications never ran. I cut the last two years into
**26 non-overlapping 20-session blocks** and measured the same spread — duration (WELL, VTR) minus
towers (AMT, CCI) — in each:

- Current block (2026-06-26 → 07-24): **+17.68pp — rank 26 of 26. The largest in two years.**
- Prior 25 blocks: mean **+3.17pp**, stdev 7.33, **17 of 26 positive**, t = 2.3.
- The current print sits **+1.98σ** above that mean.

So the advertised **18.2–24.3pp spread is 5.7x–7.7x the independently-measured per-20-session mean
of +3.17pp.** Within the 60-day window itself, **69% of the spread (17.69 of 25.58pp) was earned in
the final third of the calendar — a 2.1x concentration.**

⇒ **Five replications taken on overlapping 60-day windows that all contain this one block are one
observation about magnitude.** The desk did not measure a persistent 20pp regime five times; it
measured a single 20-session outlier five times. C4: the underlying tilt is *not rejected* — it is
real, positive in 17 of 26 independent blocks, at roughly **one-fifth** the size being carried.

One asymmetry the pre-mortem missed: the two legs have **different time signatures.** Only 18.9%
(AMT) and 39.9% (CCI) of the tower leg's 60-day shortfall vs SPY landed in the last 20 sessions —
the tower weakness is a slow 60-day bleed, not part of the burst. **The burst is entirely on the
duration leg.** Whatever happened in the last 20 sessions happened to WELL and VTR, not to towers.

---

## §1 · Full player map (12 names, asof 2026-07-24, benchmark SPY)

| Ticker | Sub-industry | mcap $bn | flow | tag | OBV state | RS20 | RS60 | delta | 07-24 % | % off 52wH | short %fl |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PLD | Industrial | 131.0 | +0.706 | 🟢 new_green | accum. | +4.4 | **+0.5** | +0.337 | — | −3.7 | 1.66 |
| WELL | Health Care | 145.9 | +0.528 | 🟡 | accum. | +12.0 | **+13.8** | +0.017 | +2.03 | **−0.3** | 3.07 |
| VTR | Health Care | 39.7 | +0.489 | 🟡 | accum. | +14.4 | **+11.0** | −0.011 | +2.67 | **−0.3** | **5.89** |
| DLR | Data Center | 66.1 | +0.427 | 🟡 | neutral | +2.8 | −1.5 | **+1.099** | **+11.01** | −4.4 | **0.01** |
| PSA | Self-Storage | 55.9 | +0.335 | 🟡 | neutral | −0.1 | +4.7 | +0.116 | — | −2.8 | 4.99 |
| SPG | Retail | 68.5 | +0.178 | 🟡 | accum. | +1.3 | +9.5 | −0.018 | — | −0.8 | n/a |
| IRM | Other Spec. | 38.0 | +0.076 | 🟡 | accum. | −2.7 | +10.1 | +0.070 | +3.02 | −4.7 | 3.77 |
| CCI | Telecom Tower | 35.8 | −0.249 | 🟡 | neutral | −6.5 | **−16.9** | +0.316 | +0.44 | **−33.6** | 3.28 |
| CBRE | RE Services | 38.5 | −0.250 | 🟡 | distrib. | +3.0 | −8.9 | +0.050 | — | −20.0 | 1.85 |
| O | Retail | 56.2 | −0.299 | 🟡 | distrib. | +5.1 | −0.6 | +0.002 | — | −3.4 | 4.89 |
| AMT | Telecom Tower | 82.0 | −0.321 | 🟡 | distrib. | −1.8 | −10.4 | +0.341 | +1.23 | **−27.2** | 1.89 |
| EQIX | Data Center | 107.7 | −0.449 | 🟡 | distrib. | −0.9 | −3.1 | +0.258 | +4.90 | −3.9 | 2.18 |

Sector: n=12, wflow +0.163, eqflow +0.098, **delta +0.226 = #1 of 11 sectors, 2.57x the runner-up
(Cons. Disc. +0.088)**, and the only sector with **zero 🔴**. XLRE **+2.22%** on 07-24, best on the board.

**W5 — dispersion.** On 07-24 the sub-node range was DLR **+11.01%** to SBAC **−0.73%** = **11.74pp
against a sector move of 2.22% — 5.3x.** The label "Real Estate" is the wrong unit for that day.

**★ No thematic small-cap clears the bar.** But the *universe* does not clear one either: it is a
top-300 S&P cap screen, not a sector census, and **six of the eight sub-industry nodes have n ≤ 2**
(four have n=1: PLD, PSA, IRM, CBRE — zero measurable internal dispersion by construction). Omitted
at ≥$2bn: **SBAC $18.4bn (the third tower REIT)**, EXR $32.6bn, VICI $29.4bn, AVB $27.1bn, EQR
$26.2bn, INVH $17.7bn, WY $17.3bn, HST $17.0bn, OHI $16.1bn, SUI $15.6bn, DOC $15.4bn, AMH $13.7bn,
GLPI $13.2bn, BXP $12.3bn, CPT $11.3bn. ⇒ The desk graded "Telecom Tower REITs" from **2 of the
node's 3 members**. §4 uses SBAC as the out-of-sample test.

---

## §2 · Value chain, left → right

1. **Capital / rates** — 10y real yield, HY OAS 2.77%, equity issuance windows.
2. **Land + entitlement + grid interconnect** ← ★ **BINDING CONSTRUCTION CONSTRAINT for data centres.**
3. **Power generation & transmission** ← ★ **BINDING CONSTRAINT overall** (cross-sector: AI → power → DC → REIT). EQIX joined a 200-firm US AI power-usage pledge alongside NextEra and Duke (07-22).
4. **Shell / build** — PLD, DLR development book, CBRE as agent.
5. **The REIT (asset owner)** — the 12 names.
6. **Tenant / operator** — hyperscalers (DC), carriers (towers), senior-housing operators (WELL/VTR RIDEA), 3PLs (PLD).
7. **End demand** — AI inference, mobile data, the 80+ population cohort, e-commerce throughput.

**Demand is not the bottleneck and must not be marked as one.** For data centres the binding
constraint is node 3 → 2 (power and interconnect), not leasing appetite — DLR's own release
attributes the guide raise to "resilient leasing momentum". For **towers it is node 6, tenant
count**, and it is contractual rather than physical. For **health-care REITs it is node 6 labour**
(operator staffing), which is why that node behaves like an operating business, not a bond (§4).

---

## §3 · Mandate (C) — one bucket, two, or three?

Measured: `scripts/risk_units.py`, SPY-residual correlation, **499 aligned days**, threshold sweep
reported (C5). **Answer: THREE units, and the desk's 4-name "digital infrastructure" bucket cuts
across two of them.**

Residual correlations, within the proposed groupings:

| Pair | resid corr |
|---|---|
| **AMT–CCI** | **+0.822** (highest pair measured) |
| **WELL–VTR** | **+0.793** |
| **DLR–EQIX** | **+0.641** · DLR–IRM **+0.600** · EQIX–IRM **+0.526** |

Now the bucket the desk carried, across its own seam:

- towers ↔ data centres: AMT–DLR +0.260, AMT–EQIX +0.326, CCI–DLR +0.241, CCI–EQIX +0.263 → **mean +0.273**
- towers ↔ duration: AMT–WELL +0.330, AMT–VTR +0.320, CCI–WELL +0.332, CCI–VTR +0.302 → **mean +0.321**

⇒ **The towers are more correlated with the duration REITs they are cast as the mirror image of
(+0.321) than with the data centres they are bucketed with (+0.273).** "Digital infrastructure" as a
4-name unit does not exist in the data; it is anti-correlated with its own construction logic. This
extends retracted-ledger R10, which had already measured AMT into the duration group — **CCI belongs
there too.**

Agglomerative clustering at corr ≥ 0.35 returns **8 units**, of which the RE-relevant ones are
**U0 {AMT, CCI, O, PLD, PSA, SPG, VTR, WELL, XLRE}** and **U1 {DLR, EQIX, IRM}**, with CBRE alone.
**IRM — GICS "Other Specialized REITs" — trades in the data-centre unit and the desk's map has it
filed elsewhere.** The real data-centre node is a *three*-name unit.

I reproduce S25's numbers exactly (XLRE–PLD +0.714 · XLRE–AMT +0.712 · XLRE–WELL +0.652 · XLRE–DLR
+0.456 · DLR–PLD +0.213 · DLR–AMT +0.260 · DLR–WELL +0.254), so S25's separation of {DLR, EQIX} is
sound — it is simply **incomplete without IRM**.

⚠ **S5, stated because the tool reports it: ARI (first half vs second half) = 0.5987.** Membership is
only moderately stable — the three *pairs* survive it, the nine-name U0 blob is not something to
lean on. **C5 — the 0.35 threshold is an arbitrary choice.** Sweep: corr ≥0.60 → 13 units; ≥0.50 →
10; ≥0.45 → 9; ≥0.40 → 8; ≥0.35 → 8; ≥0.30 → 7; ≥0.25 → 6. **The three-way split is present at every
threshold from 0.60 to 0.40**; towers merge into U0 with duration only at ≤0.40. Not
threshold-fragile.

---

## §4 · Mandate (B) — the measurement vs its stated driver

**The measurement survives. The stated driver dies at the primary level, on both legs.**

**Survives.** Extending to the omitted third tower confirms the node, and strengthens it: 60-day
excess vs SPY — AMT **−9.78pp**, CCI **−16.16pp**, **SBAC −23.84pp** (worst in the extended set), all
three negative, mean −16.6pp. On 07-24, when XLRE rose 2.22%, **SBAC was the only REIT in the
extended set that fell (−0.73%).** Towers are down 26–34% from 52-week highs while every other RE
name except CBRE sits within ~5% of its high. **Tower underperformance is a genuine node property,
not a 2-name artifact.**

**Driver death #1 — "digital infrastructure is sold because the AI-datacentre narrative is topping."**
Refuted three ways at the primary level:
- **DLR Q2 (release body-read):** revenue **$1.92bn, +29% YoY and +17.4% QoQ** off Q1'26's $1.635bn,
  vs $1.66bn consensus; adjusted FFO **$2.65 vs $1.86**; FY26 AFFO guide **raised** to $8.15–8.20 from
  $8.00–8.10; FY revenue guide raised to $6.85–6.95bn — attributed to "resilient leasing momentum
  from cloud and AI customers," plus a **$3.5bn** purchase of a larger stake in three Northern
  Virginia data centres from Blackstone.
- **EQIX has the strongest estimate revisions in the sector**: FY+1 consensus **+9.6% over 90 days**
  (17.618 → 19.313), breadth **4↑:0↓** — while carrying the sector's *worst* flow score (−0.449).
  Estimates up hardest, flow tag worst; those cannot both be a topping narrative.
- **The largest disclosed customer print is three sessions old and goes the other way** (§5).

**Driver death #2 — the towers' problem is not AI at all.** CCI printed Q2 on **2026-07-22** (8-K
Item 2.02) — **an event the desk's file set never mentions.** Body-read from the release: **AFFO
$1.13/share vs $1.02, +11% YoY**; FY26 AFFO dollars guided **up** $5m to $1,975m; organic contribution
to site-rental billings **3.9%, or 4.2% ex-DISH vs 3.7% in the year-ago comparable — accelerating.**
Site rental revenue fell 4.1% YoY (QoQ **[blank]** — Q1'26 site-rental is not separable in our
series) **because of $49m of DISH terminations and $5m of Sprint cancellations**, and CCI closed the
sale of Fiber and Small Cells on 05-01 for **$8.4bn**, repaying >$7bn of debt and repurchasing $1bn
of stock. **CCI is now a pure-play US tower operator with no AI exposure whatsoever.** Its
underperformance cannot be a data-centre narrative; it is contractual tenant loss (DISH/EchoStar).

**Driver death #3 — "duration" is the wrong word for the winners.** If this were a rates/duration
rotation, the lowest-beta, most bond-like names in the sector would lead. They are last. SPY-residual
betas: **AMT −0.054 · CCI +0.086 · O +0.110 · VTR +0.156 · WELL +0.224** vs **EQIX +0.648 · PLD
+0.766 · DLR +0.769 · IRM +0.930.** The towers are the *most* bond-proxy names on the board and they
are the worst performers. Meanwhile, extending the 60-day excess-vs-SPY board beyond the desk's
12 names puts **DOC +36.72pp (healthcare facilities), HST +17.39pp (hotels) and BXP +13.96pp
(office)** at or above WELL's +13.97pp. Hotels and office are the *least* duration-like, most
operationally-levered REITs in existence.

⇒ **The last 20 sessions contained an operating-recovery rotation, not a duration rotation** —
senior-housing occupancy/rate momentum (WELL, VTR, DOC, OHI) plus hotel and office recovery — while
the nodes whose cash flows are *contractually fixed* (towers; net-lease O at RS60 −0.6 vs SPY)
lagged. Senior housing under RIDEA is an operating business with labour costs, not a bond. **The
tape is the same; the story attached to it was backwards.** ⚠ Corroborating, not carrying: VTR runs
the sector's **highest short interest at 5.89% of float** and sits 0.3% off its 52-week high after a
+15.03pp 20-session excess run vs SPY — a squeeze is one available explanation for why 132% of its
60-day excess landed in 20 sessions. Untested here.

---

## §5 · Customers (W4)

**Data-centre node — hyperscalers.** Quarterly capex, $bn:

| | latest qtr | YoY | QoQ | next print |
|---|---|---|---|---|
| **GOOGL** | **44.92** (Q2'26, settled 07-22/23) | **+100.1%** vs 22.45 | **+25.9%** vs 35.67 | reported |
| MSFT | 30.88 (Q1'26) | +84.5% vs 16.74 | +3.3% | **2026-07-29 or 07-30** |
| META | 19.00 (Q1'26) | +46.8% vs 12.94 | −11.1% | **2026-07-29 or 07-30** |
| AMZN | 44.20 (Q1'26) | +76.7% vs 25.02 | +11.8% | **2026-07-30 or 07-31** |

★ **The one settled datapoint, one day before DLR's print, shows the largest customer's capex
doubling year-on-year.** Two further primary facts from Alphabet's Q2 exhibit: **Q2 free cash flow
was NEGATIVE −$5.855bn** (operating cash flow $39.069bn against $44.924bn of PP&E purchases; TTM
capex $132.402bn), and in **June 2026 Alphabet raised $49.6bn** in Class A/C stock and mandatory
convertible preferred "including capital expenditures to scale AI infrastructure and global
compute," plus a $40bn ATM programme.

That is a **funding-mode change, not a demand change** — self-funded capex has become
externally-funded capex at the largest buyer. It confirms data-centre demand near-term (the money is
raised and committed) while identifying where the node's real risk lives: **the cost of external
capital, not the AI narrative.** Three of four customers print inside six days; this file does not
conclude around them.

**Tower node — US carriers.** Quarterly capex, $bn: **T $5.70 (Q2'26) vs $4.90 (Q2'25) = +16.3% YoY,
+16.8% QoQ vs $4.88** · **TMUS $3.19 vs $3.24 = −1.5% YoY, +20.4% QoQ** · **VZ = [blank]** — Q2'26
not present in our series (last available Q1'26 $4.28bn vs Q1'25 $4.27bn, +0.2%); C3, this stays
unknown rather than being folded into "flat." All three carriers next print in **October 2026**, so
**no disclosed carrier-capex update lands inside any bracket window on this board.**

⇒ Carrier spend is flat-to-up, and CCI's own organic growth accelerated to 4.2% ex-DISH. **The tower
node's problem is a named, disclosed, contractual tenant loss (DISH terminations, $49m in the
quarter), not a customer-spending contraction.** That is a fact with an expiry date, which is a
different object from a demand thesis.

---

## §6 · Valuation on the right metric (L2)

**The category error runs in both directions and the desk has so far only caught one of them.**

DLR's screen "forward P/E 67.87" is GAAP-EPS-based and meaningless for a REIT; on the raised AFFO
guide it is **199.08 / 8.175 = 24.4x AFFO**. That much the handoff caught. But the *same* error
produced the pre-mortem's strongest bear datapoint on the winners: **VTR's "current-quarter estimate
cut −33.3% over 90 days" is GAAP EPS 0.165 → 0.110 — a $0.055 move on a company whose FFO run-rate
is roughly $3.4–3.6/share, i.e. ~1.6% of the metric that matters.** WELL's "0↑:1↓" and VTR's "0↑:2↓"
books are GAAP-EPS books. And CCI's headline consensus fell because **GAAP EPS dropped 67% YoY
($0.22 vs $0.67) on a divestiture** while **AFFO/share rose 11%.** Read on the right metric, the
revision picture inverts for the loser.

| | price | P/AFFO (own guide) | AFFO/share trend | 30d revision breadth (GAAP est.) | to mean target |
|---|---|---|---|---|---|
| **CCI** | 74.90 | **16.3x** (FY26 $4.59) | **+11% YoY in Q2**, FY $ guide raised | 0y 2↑:2↓ | **+28.0%** |
| **DLR** | 199.08 | **24.4x** (FY26 $8.15–8.20, raised) | guide **raised twice-over** | 0y 0↑:1↓ | +10.6% |
| **AMT** | 166.67 | [blank] — AFFO guide not pulled | flat | **1↑:0↓ all four periods** | **+28.8%** |
| **EQIX** | 1,084.24 | [blank] | FY+1 est **+9.6%/90d** | **4↑:0↓** | +10.6% |
| **WELL** | 252.07 | [blank] | — | 0↑:2↓ (GAAP) | **−3.4% (above target)** |
| **VTR** | 100.53 | [blank] | — | 0↑:7↓ across periods (GAAP) | **−2.2% (above target)** |
| **PLD** | 147.63 | [blank] | 3 of 4 periods **negative** over 90d (−2.5%, −5.5%, −2.9%) | **0↑:0↓ — no analyst has touched it** | +6.9% |

**The winners-priced-out / losers-carry-the-gap pattern is confirmed and is stronger than described.**
WELL and VTR trade **above** consensus mean targets (−3.4%, −2.2%) at 0.3% off 52-week highs; the
entire analyst gap sits on the towers (AMT +28.8%, CCI +28.0%) at 27–34% below their highs. PLD — the
sector's only 🟢 and its top flow score at +0.706 — has **RS60 of just +0.5 vs SPY, negative revisions
on three of four periods, and a completely frozen analyst book (0↑:0↓, 8 Buy / 8 Hold), 3.7% off its
high with only +6.9% to target.** Its flow rank and its fundamental momentum point opposite ways;
that gap is the single least-examined thing in this sector.

★ The cleanest right-metric fact on the board: **CCI at 16.3x AFFO with AFFO/share +11% YoY, versus
DLR at 24.4x AFFO** — the name the desk classified as structurally impaired is growing the REIT
metric faster than the name that just gapped 6σ, and at two-thirds the multiple.

---

## §7 · Chain-hop candidates (body-proximate only, never headline-named)

`module_news_data chain-hop`, 372 foreign articles / 7 days / ±300-char proximity. Candidates
returned, each cross-checked against flow before being allowed to travel:

| Candidate | proximity / body | flow cross-check | disposition |
|---|---|---|---|
| **T** (Integrated Telecom) | 6 / 22 — example body: "Crown Castle: The Pivotal Unknown" | **flow +0.958 🟢 accelerating, OBV accumulation corroborating RS20 +7.0 vs SPY** (RS60 −11.2), delta +0.208 | ★ **PASSES.** The tower node's largest customer, capex **+16.3% YoY**, body-proximate and never headline-named. The only genuine outward hop this sector produced. |
| EQIX, WELL | 14/19, 11/14 | — | **Not candidates** — already core names in §1. Their appearance is a symptom of a closed chain, not a discovery. |
| GEV | 4 / 7 | **flow −0.151 🔴 distributing, OBV distribution consistent with RS20 −7.1 vs SPY** | **REJECTED.** Proximity source is a Canadian retail-REIT earnings call — false adjacency. Fails flow check independently. |
| AVGO · HD · MSCI | 4/31, 5/7, 4/12 | AVGO +0.077 🟡, HD +0.060 🟡, MSCI n/a | **REJECTED** — all three trace to dividend-listicle and ETF-comparison boilerplate, not to a chain. |

⇒ **One candidate, T, and it is a customer-leg hop, not a new node.** A news co-mention alone is not
a candidate and none of the rejected four may reach a BET sheet. Separately flagged as a
**universe gap, not a chain-hop**: **SBAC ($18.4bn)** — a full member of a node the desk grades, absent
from the screen, and the worst-performing REIT in the extended set at −23.84pp vs SPY over 60 days.

---

## §8 · Track KPIs and anti-signals, as dated observables

**Engaging S25 directly — and reporting a confound in its own design.**

★ **S25's frozen threshold is not clean.** It asks whether, by **2026-08-08**, DLR's RS20 vs SPY falls
below the **{PLD, AMT, WELL} median** while that median stays positive. But **AMT prints 2026-07-28
and WELL prints 2026-07-28** — two of the three control names have earnings events *inside* the
measurement window, while the treated name (DLR, printed 07-23) and PLD (next print 2026-10-14) have
none. The test will therefore be resolved substantially by two control-leg earnings reactions rather
than by the mislabelling question it was written to answer. **Recommend the observable be recorded
with AMT and WELL flagged, and PLD — the only event-free control — reported separately.** S1: this
does not invalidate S25; it means a threshold breach on 08-08 will be ambiguous between two causes.

| # | Dated observable | Reads which way |
|---|---|---|
| K1 | **AMT Q2, 2026-07-28** — AFFO/share and *tenant-count/churn commentary*, not GAAP EPS | If AMT's AFFO holds like CCI's did (+11%), the tower node is a valuation/churn story, not an impairment |
| K2 | **WELL Q2, 2026-07-28** and **VTR Q2, 2026-07-30** — senior-housing **same-store occupancy and RevPOR/ExpPOR** | Tests §4's operating-recovery reading directly. Occupancy accelerating ⇒ driver is operations; flat ⇒ the +17.68pp block needs another explanation |
| K3 | **EQIX Q2, 2026-07-30** — the second settling point. Does the sector's best revision book (4↑:0↓) convert into a guide raise, and does EQIX's 🟡 distribution flow tag survive it | n≈1 either way; EQIX's 07-24 +4.90% was sympathetic (no 8-K in 10 days, confirmed) |
| K4 | **MSFT + META 07-29 or 07-30, AMZN 07-30 or 07-31** — capex guide, and specifically **how it is funded** | GOOGL set the marker: capex +100.1% YoY with **negative FCF** and a $49.6bn equity raise. Watch for the same funding pivot |
| K5 | **2026-08-08 (S25)** — DLR RS20 vs SPY against the {PLD, AMT, WELL} median, **reported separately, never merged**, with AMT/WELL flagged per above | — |
| K6 | **CCI DISH termination run-off** — $49m/quarter drag, from CCI's own disclosure | A dated, contractual, *expiring* headwind. Its roll-off date is the tower node's real clock |
| K7 | **HY OAS (FRED `BAMLH0A0HYM2`), NFCI alongside** — currently 2.77% | §5's funding-mode finding makes this the data-centre node's true sensitivity, not the AI narrative |
| K8 | **Next 20-session block (≈2026-07-27 → 08-21)**: re-measure duration-minus-tower on a **fresh non-overlapping window** | ★ The single highest-value observation on this page. +3.17pp ⇒ §0's base rate holds. Another +17pp ⇒ R7's magnitude was real and I was wrong. Near zero or negative ⇒ the whole spread was one block |

**Anti-signals — what would falsify this file:**
- **A1** WELL/VTR print accelerating occupancy *and* towers rally on AMT's 07-28 print ⇒ §4's operating-recovery reading is wrong; a common rate driver is back in play.
- **A2** SBAC's −23.84pp proves idiosyncratic (leverage, international mix) ⇒ my out-of-sample confirmation collapses back to n=2.
- **A3** DLR re-prints or a second Blackstone-scale deal lands before 08-08 ⇒ S25 re-registers; n≈1 becomes uninterpretable.
- **A4** PLD's frozen 0↑:0↓ book breaks *upward* ⇒ §6's flow-vs-fundamentals flag resolves benignly.
- **A5** The next block prints +15pp or more ⇒ §0's verdict is wrong; treat 20pp as the regime.

⚠ **Coverage gap, worse than briefed.** `module_report_tags ticker` returns **zero reports for 11 of
the 12 names**; the exception, VTR, has two hits that are this same run's own PREMORTEM and SWEEP
files — self-citation, not coverage. **The Real Estate sector has never had a company report written
against it**, which is precisely how one 20-session block came to be carried as a five-times-
replicated structural belief.

---

## ✅ EXIT CHECK

- **Mandate (A) — answered first, with my own number.** R7 is **one observation on magnitude, ~25 on direction.** Current 20-session block +17.68pp = **rank 26/26 in two years, +1.98σ**; independent per-block mean **+3.17pp**, i.e. the carried 18.2–24.3pp is **5.7x–7.7x** the base rate. Pre-mortem's 86.2%/132.1% reproduced exactly.
- **Mandate (B) — measurement and driver separated explicitly.** Measurement **survives and strengthens** out-of-sample (SBAC −23.84pp, third tower). Stated driver **dies three times**: DLR guide raised, EQIX revisions +9.6%/90d, GOOGL capex +100.1% YoY; CCI has zero AI exposure post-divestiture; and the lowest-beta names lead the *downside*, which no duration story permits.
- **Mandate (C) — settled: THREE units**, stable from corr ≥0.60 to ≥0.40. Towers–duration (+0.321) **exceeds** towers–data-centres (+0.273). **IRM belongs in the data-centre unit** and the desk's map does not have it there.
- **C1** SPY declared at file head and named inline at every excess-return claim. **C2** DLR revenue +29% YoY **and** +17.4% QoQ; GOOGL capex both halves; CCI QoQ **[blank]**. **C3** unknown column kept — VZ Q2 capex and five AFFO multiples **[blank]**, never guessed. **C4** "not rejected / indistinguishable" used on the surviving direction and on S5 instability. **C5** threshold sweep reported (0.60→0.25). **S1** 07-24 treated as n≈1; DLR isolated as its own earnings event, EQIX as sympathetic (no 8-K in 10 days, verified). **S5** ARI 0.5987 disclosed.
- **D2** proxy sign verified — chain-hop's GEV/AVGO/HD/MSCI hits traced to source articles and rejected as false adjacency. **D6** every OBV mention paired with RS20/RS60 vs SPY; OBV never carries a proposition (VTR squeeze note marked untested). **L2** FFO/AFFO used and GAAP EPS quarantined **symmetrically** — DLR's 67.87 and VTR's −33.3% are the *same* error.
- **W4** hyperscaler capex with real numbers plus print dates (both provider dates carried); carrier capex from filings, VZ blank. **W5** dispersion with the ratio: **11.74pp sub-node range vs 2.22% sector move = 5.3x** ⇒ said the label is the wrong unit.
- **STANDING_VIEW §5** — R7 treated as the hypothesis under test, never as input; R10 cited only as a prior *measurement* this file extends.
- **Analytical only** — no buy/sell language, no sizing, no execution, nothing run with `--execute`.
