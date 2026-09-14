# SECTOR_DEEP_UTIL — Utilities / merchant-IPP sub-leg — industry_US — 2026-08-04 (Tue)
## ★ PREMORTEM-PROMOTED SLOT — FULL FRESH MAP OF THE SUB-LEG

> Flow/RS settled **2026-08-03** (`SECTOR_FLOW_US.json`, `asof 2026-08-03`). Benchmark **SPY inline (C1)**.
> Prior sector-level cover **2026-07-31** (read; its two-leg map is superseded where noted).
> **P4: analytical only — zero buy/sell language, zero sizing.**
> ⚠ **Run-clock note**: the desk clock rolled to **2026-08-05** during execution (`module_fundamentals_us`
> stamps 08-04/08-05). All price/flow numbers below are the **settled 08-03 bar**; both target prints
> (**CEG 08-06 · VST 08-07**) remain forward. Live quotes are marked where used.
> ⚠⚠ **R40 / M313 honoured throughout**: **no S35 FIRED-A and no S47 FIRED-B verdict is cited as evidence
> anywhere in this file.** The regulated groups below are **re-derived from the 15-name sector**, not read
> off the contaminated "regulated seven"; **D and NEE are additionally stripped in a dedicated row** because
> R40 makes D a merger-arb security and NEE its counterparty. Both brackets settle 08-07 on the regulated-SIX
> and are none of this file's business.

---

## 0 · Does the promotion survive its own test?

**Three answers, in descending order of confidence.**

**(a) The sub-leg is not the unit. The signal is ONE NAME, and that is the R32 shape that killed
"Financials is breadth-led."** A permutation test over all **105** two-name draws from the 15-name sector:

| Statistic the promotion rests on | Merchant pair | Random 2-name draw from the same sector | Composition of the qualifying draws |
|---|---|---|---|
| **0 of 2 🔴** | 0 | **P = 21/105 = 0.200** | — |
| **median RS20 ≥ +4.4 vs SPY** | +4.4 | **p = 3/105 = 0.029** | **all 3 contain CEG** (PCG·CEG, CEG·VST, CEG·D) |
| **median flow ≥ +0.267** | +0.267 | **p = 6/105 = 0.057** | **5 of 6 contain PCG — a REGULATED name** |
| **median RS60 ≤ −11.6 vs SPY** | −11.6 | **p = 8/105 = 0.076** *(bottom 8%)* | **all 8 contain CEG** |

⇒ **"0 of 2 red" is a one-in-five coincidence and carries nothing.** The RS20 result is real
(p = 0.029) but **every draw that produces it contains CEG**, and the flow result is mostly produced by
**PCG, which the promotion classified as regulated.** ★ **This is a CEG finding wearing a sub-leg label
(S1: n = 2 is n = 2, and here it is effectively n = 1).**

**(b) The promotion selected the one window where the sign is favourable. On the 60-day window the split
INVERTS.** Merchant median **RS60 −11.6 vs SPY** against regulated **−6.55** — the merchant pair is **5.05pp
WORSE**, and sits in the sector's **bottom 8%** of two-name draws. **PREMORTEM's table shows RS20 only.**
On RS60 the sentence "the leg that is not printing this week is the weak one" reverses.

**(c) The promotion's price quotes are D74-contaminated, and the drawdown depths are wrong.**
`SWEEP_READ` §0 caught D74 on the sweep and trimmed to 08-03; **the promotion re-introduced it on the
price line.** Re-pulled from yfinance with `index <= 2026-08-03`:

| | PREMORTEM quote | **Settled 08-03 close** | Stated drawdown | **Corrected drawdown** |
|---|---|---|---|---|
| CEG | $266.08 | **$273.71** | −35.5% from $412.70 | **−33.7%** |
| VST | $145.77 | **$155.94** | −33.7% from $219.82 | **−29.1%** |

Neither quoted price is any settled close in the last four sessions (CEG 257.95 / 263.56 / 262.75 /
**273.71**; VST 142.81 / 148.62 / 148.19 / **155.94**) ⇒ they are 08-04 intraday. **VST's drawdown is
4.6pp shallower than the argument states**, and — note the arithmetic — **the corrected CEG figure
(−33.7%) is exactly the number PREMORTEM assigned to VST.**
✅ **The flow table itself is clean**: yfinance reproduces CEG +10.47/−18.59 and VST −1.66/−4.86 against
the file's +10.5/−18.5 and −1.7/−4.7. **Only the price/drawdown quotes are contaminated.**

**(d) An undeclared exclusion (C5).** The sector is **15** names; the promotion's table sums to **14**.
The missing name is **PCG — silently dropped from "regulated," and it is the sector's ONLY 🟢**
(flow +0.778, RS20 +2.8, RS60 **+4.4** vs SPY — the best RS60 in the entire sector, better than either
merchant name). Restoring it moves the median only −0.399 → −0.390 (medians are robust, so **the
exclusion is immaterial to the number**) but it is material to the **framing**: the sector's single
accelerating name is regulated.

### ⇒ VERDICT ON THE PROMOTION

**The split is real and unmeasurable at n = 2, and what IS measurable is one name.** Per this DEEP's own
mandate that is a successful outcome, and it is stated plainly rather than argued around.

★ **But the slot earned itself on an axis nobody named.** Testing the promotion surfaced a **dated,
primary-source event that is on neither the sector board nor the sub-leg board**: on **2026-07-14 both
CEG and VST filed 8-Ks disclosing their cleared volumes in the PJM 2028/29 capacity auction** (§5), and
that auction is the **third consecutive clear at the administrative price ceiling** (§2). **The desk had
a merchant-power node on its map with no capacity-market instrument pointed at it.** That, not the
2-name flow spread, is what this slot returns.

---

## 1 · The split, re-derived and robustness-tested

⚠ **C5 — the grouping is MY arbitrary choice and is declared as such.** I assign **CEG · VST** to
"merchant/IPP" on GICS sub-industry (`Utilities - Independent Power Producers`, confirmed by
`module_fundamentals_us` on both) and everything else to "regulated/multi-utility." **PCG is regulated
(it is an IOU in Chapter-11 emergence, not a merchant), and I keep it in.** Reasonable people would
put **NEE** (unregulated NEER renewables ≈ a third of earnings) partly on the merchant side; I do not,
and the row below shows it does not matter.

### 1a · The decomposition, settled 08-03, RS vs SPY

| Group | n | median flow | median RS20 | median RS60 |
|---|---|---|---|---|
| **REG13** — all non-merchant | 13 | −0.390 | **−4.2** | −6.4 |
| **REG12** — PREMORTEM's group (ex PCG) | 12 | −0.399 | **−4.3** | −6.55 |
| **REG11** — ★ R40-clean (ex D, ex NEE) | 11 | −0.408 | **−4.4** | −6.4 |
| **REG10** — R40-clean and ex PCG | 10 | **−0.445** | **−5.15** | −6.55 |
| **MERCHANT** | 2 | +0.267 | **+4.4** | **−11.6** |
| **MERCHANT ex-largest (VST alone)** | 1 | +0.047 | **−1.7** | −4.7 |
| CEG alone | 1 | +0.487 | +10.5 | −18.5 |

★★ **The regulated read is robust to every grouping choice available and gets STRONGER under the R40
strip** (removing the merger-arb pair D/NEE takes the median RS20 from −4.3 to −4.4, and to **−5.15** on
the tightest group). **The merchant read is robust to none.**

### 1b · ★ R32 robustness — remove the largest constituent

- **Merchant, remove CEG ($97.9bn, 63.9% of the pair's cap):** the leg becomes **VST alone — flow +0.047,
  RS20 −1.7, RS60 −4.7.** **The RS20 spread collapses from +8.7pp to +2.6pp and the merchant leg's own
  RS20 turns NEGATIVE.** ⇒ **the entire outperformance claim is CEG.**
- **Regulated, remove NEE ($180.9bn, the sector's largest):** median flow −0.399 → **−0.408**, RS20
  −4.3 → **−4.4**. **Unchanged to two decimals in direction and magnitude.**
- **Regulated, remove the second-largest (SO):** median flow −0.390, RS20 −4.4. **Also unchanged.**

⇒ **Asymmetric robustness is the finding.** One leg survives its largest-constituent test; the other
*is* its largest constituent.

### 1c · Equal-weight vs cap-weight switch

| Group | eq flow | cap flow | eq RS20 | cap RS20 | eq RS60 | cap RS60 |
|---|---|---|---|---|---|---|
| REG12 | −0.396 | −0.382 | −4.53 | −3.93 | −5.08 | −6.03 |
| MERCHANT | +0.267 | **+0.328** | +4.40 | **+6.10** | −11.60 | **−13.52** |
| **Sector (n=15)** | **−0.229** | **−0.234** | −2.85 | −2.19 | −5.32 | −6.79 |

**The RS20 spread survives both weightings; the RS60 inversion survives both too — and cap-weighting
WIDENS both, in opposite directions**, because cap-weighting the 2-name leg is just "weight CEG at 64%."
⚠ **Note against the promotion's own premise**: the sector's **wflow (−0.234) and eqflow (−0.229) are
within 0.005 of each other.** The claim that "XLU is cap-weighted and regulated-heavy, so the UW− is a
claim about the wrong leg" is **not supported by this sweep** — the sector is negative on both axes and
the two axes agree to the third decimal. The merchant leg is **15.0% of sector cap**; excluding it
entirely moves the sector's median flow from −0.387 to −0.390. **The UW− is not a weighting artifact.**

### 1d · What the tag distribution actually says (D6 binds)

Regulated 13 = **8🔴 / 4🟡 / 1🟢**. Merchant 2 = **2🟡 / 0🔴 / 0🟢**. ⚠ **CEG is 🟡 solely because
`vol_surge` 0.73 blocks it**, and `SWEEP_READ` §2 measured that **79 of 79 blocked names across the board
were blocked by `vol_surge` alone.** **The tag is a volume test wearing a flow label — it corroborates
nothing here and carries nothing (D6).** Every judgement in this file is made on the RS20/RS60 pair and
the OBV state read together, never on a tag.

---

## 2 · ★ B1 — Rate of change, not level

**Merchant power is a commodity node, so the level is the distraction.** The level is spectacular and it
is exactly what the narrative quotes. **The rate is the finding, and the rate has died in two separate
series.**

### 2a · RATE #1 — the capacity clearing price: **pinned at zero by an administrative ceiling, three auctions running**

**Source: Fortune, 2026-07-24, reporting PJM's 2026-07-14 announcement** [news-sourced, body-read]:

> **"For the third auction in a row, the price of keeping the lights on across a 13-state swath of the
> country slammed straight into the ceiling."**

- **2028/29 PJM Base Residual Auction cleared at $325.00/MW-day = the maximum allowed under the price
  cap** — confirmed independently at the **primary level** by both 8-Ks (§5): every zone, both companies,
  the identical $325.00.
- **⇒ The clearing price has printed at an administrative parameter for three consecutive auctions.**
  A capped series cannot have a rate of change that means anything. **B1's "two consecutive declines in
  the rate" is satisfied in the degenerate form: the rate has been structurally ZERO twice running,
  and the observable has lost its information content.** ⚠ Prior-cycle levels ($269.92 → $329.17 in
  earlier auctions) are **[prior knowledge, NOT re-verified this run]** and are not used in any inference
  above — the three-consecutive-cap statement is sourced and stands alone.
- **The scarcity rent is measurable and it is not being paid.** PJM's own simulation of the unconstrained
  price: **$554.72/MW-day RTO-wide, $776.69/MW-day in the ComEd zone**, against $325 cleared ⇒
  **$229.72/MW-day (41% of the market-clearing price) withheld RTO-wide; $451.69/MW-day (58%) withheld in
  ComEd.** Applied to the filed volumes (§5), deterministic arithmetic:

| | Cleared MW (PJM 2028/29) | at $325 | at PJM's unconstrained RTO sim | **Gap** |
|---|---|---|---|---|
| **CEG** | 18,875 | **$2.239bn/yr** | $3.822bn/yr | **−$1.583bn/yr** |
| **VST** | 10,924.4 | **$1.296bn/yr** | $2.212bn/yr | **−$0.916bn/yr** |
| CEG ComEd block alone | 10,200 | — | *vs $776.69 sim* | **−$1.682bn/yr** |

⚠ **C3/C4 — what these numbers are and are not.** The $325 column is **contracted revenue from a filed
document**. The "unconstrained" column is **PJM's own counterfactual simulation, not a price anyone
would have paid** — it is quoted to size the administrative wedge, **not** as foregone earnings, and it
is **not** a valuation input. For scale only: at $325 the capacity line is **7.5% of CEG's TTM revenue
($29.86bn)** and **6.7% of VST's ($19.44bn)**.

### 2b · RATE #2 — new supply entering the market: **−50% in six months, and this rate is NOT capped**

- **New generation capacity that cleared this auction: 525 MW — "roughly half of what cleared six months
  earlier"** (Syso Technologies auction analysis, via Fortune).
- **Against a shortfall of ~6.8 GW** below PJM's own reliability requirement.
- **⇒ The auction cleared 7.7% of the gap it exists to close, and the rate at which it clears new supply
  HALVED in two quarters.** This is the one rate in the whole node that is free to move, and it is
  **declining while the level of scarcity rises** — the exact divergence B1 is written to catch.
- **PJM has asked FERC for an emergency "backstop" capacity auction in September** — an administrative
  admission that the price signal has stopped producing supply.

### 2c · RATE #3 — the political derivative, which is the one that moves fastest

- **Peak demand record 168.2 GW on 2026-07-02**, ~3 GW above a record set nearly two decades earlier.
- Of **$16.4bn** in total capacity charges from this auction, **~$6.3bn is attributable to data-centre
  demand; $29.4bn over the last four auctions combined** (PJM's market monitor, Monitoring Analytics,
  via The Hill).
- **Moody's, 2026-07-22 sector report**: the current system *"lacks adequate mechanisms"* to make new
  entrants bear new-build cost, and instead **socialises it across all customers**; other US power
  markets **require large new loads to contract directly**.
- **ICF via Reuters: PJM households and businesses could face rate hikes of up to 60% over five years.**
  Multiple state legislatures are moving against utility profits.

★★ **The synthesis, and it is the inversion the promotion did not consider: the merchant demand story is
TRUE and STRENGTHENING, while the mechanism that converts it into merchant cash flow is CAPPED, is
failing to attract supply, and is under active political attack.** A record-scarcity grid whose price is
an administrative constant is **not** a commodity long — it is **a regulated asset with a merchant
label**, which is the mirror image of the promotion's claim that the regulated label hides a merchant
leg. ⚠ **Stated as the mechanism the prints must speak to (§8), not as a verdict on either name.**

---

## 3 · Value chain and the binding constraint

**Seven nodes, left → right, all flow settled 08-03, RS vs SPY.** Cross-sector chain marked
**AI → power → transformers → copper**.

| # | Node | Instruments on the board | flow · OBV · RS20 / RS60 vs SPY |
|---|---|---|---|
| ① | **Fuel — gas / nuclear fuel** | KMI · WMB · OKE (Energy) | −0.011 중립 −1.8/−3.8 · −0.300 중립 −4.1/−7.8 · −0.073 중립 +0.1/−0.2 · **uranium: no instrument in the 300-name universe (C3)** |
| ② | **Generation — merchant/nuclear** | **CEG · VST** | **+0.487 매집 +10.5/−18.5** · **+0.047 중립 −1.7/−4.7** |
| ②′ | **Generation — regulated** | the other 13 | median **−0.390 · −4.2 / −6.4** (8🔴) |
| ③ | **Turbines / heavy electrical** | **GEV** (Industrials) | **−0.667 분산 −13.5/−13.3** |
| ④ | **Grid & DC electrical equip. (transformers, switchgear, busway)** | **ETN · VRT** (Industrials) | **+0.867 매집 +5.2/+0.8** · **−0.177 분산 −18.3/−30.0** |
| ⑤ | **EPC / interconnection** | **PWR** (Industrials) | +0.340 중립 **+0.1 / −16.6** |
| ⑥ | **The load** | MSFT · AMZN · GOOGL · META + off-BS vehicles (§4) | +0.933🟢 · +0.906🟢 · −0.005🟡 · −0.174🔴 |
| ⑦ | **Upstream commodity — COPPER** | **FCX** — *the only Copper name in the universe* | **−0.193 · OBV 분산 · RS20 +3.5 / RS60 +1.3** |

### 3a · ⚠⚠ The copper node: traced, and it shows NOTHING — the KR-desk retraction shape is refused

**FCX is n = 1, its RS20 (+3.5) and RS60 (+1.3) are both inside a range indistinguishable from SPY, and
its OBV state is 분산 (distribution) against a positive RS.** ⇒ **The AI → power → transformers → copper
chain is TRACED as a structure and is NOT PROPAGATING to the copper node on this tape (C4).**
★ **This file therefore makes no copper read, in either direction.** The KR desk retracted a copper-chain
read on 2026-08-02 when its own ALPHA stage found the driver was a US AI-capex earnings print;
**the way not to repeat that shape is to decline the node at the point of tracing, before a direction is
asserted** — not to assert one and retract it later.

### 3b · The binding constraint is ADMINISTRATIVE, not physical, and demand is explicitly NOT the constraint

Ranked by evidence quality:

1. **[measured, primary+sourced] The capacity market's failure to convert scarcity into new supply.**
   **525 MW cleared against a 6.8 GW shortfall = 7.7% of the gap, at half the prior rate (§2b).** This is
   the binding constraint stated as a *quantity*, and it is the strongest-evidenced item on the board.
2. **[sourced, dated] Load curtailment — the constraint applied to the customer, not the generator.**
   **PJM will curtail data centres of 50 MW or larger during shortages beginning June 2027**
   (TechCrunch, 2026-07-28, body-read; compensated, demand-response style). ⇒ **the grid operator has
   chosen to ration the LOAD.** ★ This is also the mechanism that *creates* §4's behind-the-meter
   bypass: a 50 MW threshold with a firm date is a direct instruction to self-supply.
3. **[inferred, no series] Equipment lead time.** The tape distributes ③ and half of ④ (GEV −13.5,
   VRT −18.3) while accumulating the other half (ETN +5.2). **This repo holds no turbine or transformer
   lead-time series — C3, stated rather than reasoned around.**
4. **NOT the constraint: demand.** Peak demand set a record (168.2 GW) and the auction still cleared at
   a cap with a shortfall. **Strong demand is not a bottleneck (mandate §6), and here it is the one
   variable with no scarcity attached to it.**

⚠ **R41 — an inherited superlative, re-scanned and corrected.** The setup carried *"ETN is the ONLY 🟢 in
the whole AI-power adjacent layer."* **The tag claim is true; the excess claim it implies is not.**
ETN's **RS60 vs SPY is +0.77pp — statistically indistinguishable from the index (C4) — and its
days-21-to-60 segment is −4.26.** Its RS20 (+5.15) is **669% of its RS60**, i.e. **ETN is a 20-day repair
with nothing underneath it, not a 60-day leader.** The superlative is retained only in its tag form.

⚠ **GEV's de-rate is a 20-DAY EVENT, not a grind, and its driver is UNRESOLVED.** GEV RS20 −13.46,
RS60 −13.50, **days-21-to-60 segment +0.37 ⇒ 99.7% of the 60-day damage landed in the last 20 sessions.**
That window is coincident with the AI-capex earnings block. **I do not attribute it to a power cause,
and I do not attribute it to a semis cause — the driver is marked `unknown` (C3).** ★ This is the second
place in this file where the KR-desk shape (right direction, wrong driver) is declined rather than risked.

---

## 4 · ★ W4 — Customers named, and the lease-financing problem (M227)

**The merchant thesis is data-centre offtake, so the customer's DISCLOSED spend is the test.**

### 4a · The four named customers, and how they split on this tape

| Customer | flow | tag | OBV | RS20 / RS60 vs SPY |
|---|---|---|---|---|
| **MSFT** | **+0.933** | 🟢가속 | 매집 | **+25.2 / +14.6** |
| **AMZN** | **+0.906** | 🟢가속 | 매집 | **+15.5 / 0.0** |
| **GOOGL** | −0.005 | 🟡중립 | 중립 | +1.1 / **−9.4** |
| **META** | −0.174 | 🔴분산 | 분산 | −2.5 / −6.9 |

**Aggregate disclosed spend** [news-sourced, FT-cited via Tom's Hardware 2026-07-31, **not** read from a
filing — C3]: the four have committed **>$1.1 trillion** to AI infrastructure since 2023, with
**~$745bn expected to be added in 2026 alone.** ⇒ **The spend is not in question. The QUESTION IS WHOSE
BALANCE SHEET IT SITS ON, and that is where the node breaks.**

### 4b · ★★ M227 — two dated financings in a THREE-DAY window, both moving capacity OFF the customer's balance sheet

**(i) Meta × BlackRock, announced 2026-07-28 (PR Newswire, body-read).** El Paso, TX; **1 GW of compute**;
**~$14bn total development cost**; **BlackRock funds own 80%, Meta 20%**; **a portion of BlackRock's
investment is funded with proceeds from a $12.5bn debt financing**; Meta **leases the entire campus**
(4-year initial term, four extension options, potential 20-year); Meta provides **residual-value
guarantees with an aggregate threshold of ~$13bn**; capacity begins coming online **2028**.
★★ **The cash mechanics, which are the finding**: at financial close **Meta contributes land and
construction-in-progress valued at ~$2.3bn (non-cash), BlackRock contributes ~$4.9bn cash, and Meta
receives a one-time distribution of ~$1bn** to align the 80/20 split. **⇒ One gigawatt of AI capacity
was created with Meta net-RECEIVING roughly $1bn of cash at close.** It will appear in Meta's accounts as
**lease expense and a contingent RVG, not as capex.**

**(ii) Nexus Data Centers / Anthropic / Google, reported 2026-07-30 (WSJ via Reuters, body-read).**
Hubbard, TX; **$15bn raise**; **$14bn bridge loan plus a revolver**, bank group led by Morgan Stanley;
Google guarantees Anthropic's lease **and power-payment** commitments and takes **~20% equity in the
data-centre AND POWER project**; the guarantees explicitly cover **four data-centre leases and the
related power-purchase agreements**.
★★★ **And the line that matters most to this DEEP: the campus "includes a natural-gas-fired power plant
capable of producing 1.6 gigawatts of electricity."**

### 4c · ⇒ Whose demand signal is the merchant generator reading?

**Answer, stated as a mechanism with its evidence attached:**

1. **A 1.6 GW load in ERCOT arrived with its own 1.6 GW of generation, contracted by PPA to a captive
   plant inside the same financing vehicle.** That is **not merchant offtake — it is behind-the-meter
   self-supply that routes around the merchant generator entirely.** **VST is the ERCOT merchant
   incumbent.** ⇒ **the largest named new Texas AI load in this window is structurally not a VST
   customer, and its power counterparty is a Morgan-Stanley-financed plant carrying a Google credit
   wrap.**
2. **This reconciles §2b's otherwise strange number.** New capacity clearing PJM's auction halved to
   525 MW *while* demand set records — because **new supply is increasingly being built behind the
   meter, inside bilateral financings that never touch a capacity auction.** The auction is measuring a
   shrinking share of the build.
3. **And §3b(2) supplies the incentive**: PJM curtailing ≥50 MW loads from June 2027 is a dated, official
   instruction to self-supply.
4. **The credit chain has lengthened by two links.** The merchant generator's counterparty used to be a
   hyperscaler balance sheet. In these two deals it is **an asset-manager-owned JV backed by $12.5bn of
   debt with an RVG behind it**, and **an AI startup's lease obligations wrapped by Google "to the
   minimum level required by lenders."** ⚠ **Neither structure is distressed and neither is an
   accusation — both are investment-grade-sponsored.** The point is narrower and it is about
   *measurement*: **a demand signal read off announced gigawatts no longer tells you whose credit is
   behind them.**

⚠ **[observed, n = 4, NOT causal — C4]** The two hyperscalers that appear in these off-balance-sheet
structures (**META** as lessee, **GOOGL** as guarantor) are the two with negative-to-flat flow
(−0.174 🔴, −0.005 🟡); the two that appear in neither (**MSFT, AMZN**) are the two 🟢가속. **With n = 4
this is an observation, not a mechanism, and it is not carried into any conclusion below.**

---

## 5 · Primary-source PPA / offtake evidence

**Run: `module_disclosure_us CEG --days 60` and `VST --days 60`, then the filings themselves fetched from
SEC EDGAR and read.**

### 5a · ★ WHAT EXISTS — dated, named, contracted MW, from filings, on both names

**CEG 8-K, filed 2026-07-14, Item 8.01** *(Constellation Energy Corp + Constellation Energy Generation LLC,
CIK 0001868275)* — **every one of the Company's PJM plants cleared** the 2028/29 auction; results take
effect **2028-06-01**; volumes held-for-sale excluded:

| Zone | Nuclear MW | Fossil/Other MW | Sub-total | Price |
|---|---|---|---|---|
| COMED | **9,800** | 400 | 10,200 | $325 |
| EMAAC | 4,325 | 2,225 | 6,550 | $325 |
| MAAC | 1,575 | 150 | 1,725 | $325 |
| BGE | — | 375 | 375 | $325 |
| RTO | — | 25 | 25 | $325 |
| **PJM portfolio** | **15,700** | **3,175** | **18,875** | **$325.00** |

**VST 8-K, filed 2026-07-14, Item 8.01** *(Vistra Corp., CIK 0001692819)* — **10,924.4 MW cleared at a
weighted-average $325.00/MW-day**, uniform across every zone: RTO 4,129.9 · COMED 1,174.0 · DEOK 927.5 ·
EMAAC 1,819.0 · MAAC 584.8 · ATSI 2,069.5 · DOM 219.7.

★★ **A genuine asymmetry INSIDE n = 2, and it is disclosed in CEG's own filing.** CEG's 8-K states:
**"Capacity revenues for nuclear units are included in the gross receipts calculation for the Production
Tax Credit."** ⇒ For the **15,700 MW (83%) of CEG's cleared PJM portfolio that is nuclear**, incremental
capacity revenue **feeds the gross-receipts test that phases down the 45U nuclear PTC** — a partial
offset. **VST's PJM fleet carries no equivalent mechanism.** ⇒ **VST is the cleaner and more levered read
on any capacity-price un-capping; CEG's is partially damped by its own credit floor.** **This is W5
biting inside a two-name leg** — the same instrument, the same auction, the same price, **different
transmission to earnings** — and it is a further reason the pair is not one object.

### 5b · ⚠ WHAT DOES NOT EXIST — and it is said plainly

- **CEG: 3 filings in 60 days (1× 8-K, 1× Form 4, 1× 11-K). The 수주/계약/M&A category is EMPTY.**
  **There is NO new dated, named, contracted data-centre PPA from CEG in the last 60 days.** The 07-14
  8-K is a **capacity-market clear, which is NOT a data-centre PPA** — it is a grid-wide obligation to be
  available, sold to the RTO, not an offtake contract with a named customer.
- **VST: 13 filings; the two "Material Definitive Agreements" are an accounts-receivable securitization
  (07-16) and a 06-30 agreement — FINANCINGS, not offtake.** Also **5× Form 144 and 4× Form 4 in the
  window** (insider notices of proposed sale) — noted as a fact on the record, **positioning context only,
  never a signal, and no volumes are read from them here.**
- **The disclosed hyperscaler PPAs the narrative rests on (CEG–Microsoft, Crane Clean Energy Center; CEG–Meta,
  Clinton IL) are PRIOR-PERIOD disclosures** carried forward by the 07-31 file; **nothing has been added
  in 60 days.** ⇒ **The freshest primary-source demand fact available on either name is a CAPACITY CLEAR
  AT AN ADMINISTRATIVE CEILING, not a customer contract.** A demand/PPA update, if it comes, lands on
  **08-06 / 08-07**.

---

## 6 · Valuation vs margin percentile (B2)

### 6a · ⚠⚠ M233 FIRED ON BOTH NAMES — stated, not concluded around

```
scripts/margin_history.py CEG  →  "CEG: 연간 데이터 없음"
scripts/margin_history.py VST  →  "VST: 연간 데이터 없음"
```

**The margin-percentile leg of B2 is UNAVAILABLE for both names (C3).** M233's documented ~61% failure
rate reproduced at 2 of 2 here. **No forward multiple below is placed next to a margin percentile,
because none exists** — and per B2 that means **no cheapness claim can be completed on either name in
either direction.** What follows is the denominator test alone.

### 6b · The denominators, which are moving in OPPOSITE directions

| | Trailing P/E | Fwd P/E | P/B | PEG | Trailing EPS | **Fwd EPS** | Denominator |
|---|---|---|---|---|---|---|---|
| **CEG** | 23.25 | **20.08** | 2.90 | 3.74 | $11.51 | **$13.33** | **+15.8%** |
| **VST** | 23.18 | **14.13** | **15.82** | 0.44 | $6.30 | **$10.34** | **+64.1%** |

| Estimate line (90-day change) | CEG | VST |
|---|---|---|
| Current quarter | **−7.4%** *(30d breadth 1↑:4↓)* | **−11.2%** *(30d 3↑:1↓)* |
| Next quarter | −3.0% | **+4.2%** |
| **Current FY** | **+0.8%** *(30d 2↑:2↓)* | **+11.5%** *(30d 2↑:0↓)* |
| Next year | −1.9% *(30d 3↑:1↓)* | −1.0% |

**★ CEG — the de-rate is a MULTIPLE compression, and the denominator has NOT yet fallen with it.**
This corrects the promotion's framing directly. The setup describes *"a falling multiple whose
denominator is ALSO falling."* **On the FY line that is not what the data says: FY consensus is $11.71
and is +0.8% over 90 days — essentially unmoved.** The cut is **front-loaded into the current quarter
(−7.4%, breadth 1↑:4↓)** and has **not propagated to the year.** ⇒ **CEG is a −33.7% price move against a
flat annual denominator: the market has re-rated the multiple, not the earnings.** ★★ **This sharpens the
kill condition rather than weakening it: because the FY line is intact, a FY guide-down on 08-06 would be
a genuinely NEW fact, not a continuation of a trend already in the tape.** ⚠ **Not called cheap** —
forward EPS $13.33 still sits 15.8% above trailing, so the 20.08x is a growth multiple, and with **no
margin percentile (§6a) the cheapness question cannot be answered at all.**

**★ VST — the peak-margin trap SHAPE, and the balance sheet gives no floor.** Forward P/E 14.13 is low
**only because forward EPS ($10.34) is 64% above trailing ($6.30)** — the single largest denominator
ramp in the pair. **PEG 0.44 is arithmetic on that same ramp, not information.** And **P/B 15.82** means
book value provides essentially no support under the multiple. ⚠ **The FY line is being RAISED (+11.5%)
while the quarter is CUT (−11.2%) — the exact opposite configuration to CEG.** ⇒ **VST's low multiple is
a bet that a 64% earnings ramp lands; nothing in this file confirms or denies it, and the margin
percentile that would test it does not exist (§6a).**

**⇒ B2 verdict: NEITHER name is cheap, and they are not even the same kind of not-cheap.** CEG is a
compressed multiple on a stable year; VST is a low multiple on a steep ramp. **Two names, two
denominators, two directions — n = 2 does not survive its own valuation test either.**

⚠ **Analyst dispersion, quoted as dispersion (W5), not as upside.** CEG: low $296 / mean $351.91 /
high $441 — a **1.49× spread**, 23 covering. **VST: low $106 / mean $221.61 / high $320 — a 3.02× spread,
and one Strong Sell against 19 Buy/Strong Buy.** ★ **A 3× range means the sell side does not agree on
what VST IS**, which is itself the strongest available statement that this node is unresolved.
**Mean-target "upside" (+31.5% / +51.7%) is NOT quoted as a finding** — it is a restatement of the
drawdown, since targets have lagged the de-rate.

---

## 7 · Momentum geometry — broken thesis or cleaned base?

**Re-derived from yfinance, settled ≤ 2026-08-03, excess vs SPY, with the segment decomposed.**

| | RS5 | RS10 | RS20 | RS60 | **days 21–60 segment** | last-20 share of RS60 |
|---|---|---|---|---|---|---|
| **CEG** | **−1.14** | +5.87 | **+10.47** | **−18.59** | **−26.35** | −56.3% *(n/m — sign flip)* |
| **VST** | **−3.24** | **−3.40** | −1.66 | −4.86 | −3.18 | 34.2% |
| GEV | −1.49 | −8.81 | −13.46 | −13.50 | **+0.37** | **99.7%** |
| VRT | **−11.05** | −11.91 | −18.25 | −30.21 | −13.89 | 60.4% |
| ETN | **+7.42** | +7.07 | +5.15 | **+0.77** | −4.26 | 669% *(n/m)* |
| PCG | −3.48 | −2.10 | **+2.78** | **+4.39** | +1.49 | 63.3% |
| XLU | −5.40 | −3.39 | −2.93 | −5.85 | −2.91 | 50.1% |

### 7a · ★ Adjudication — CEG: **NEITHER. It is a 40%-retraced repair whose freshest leg has stalled.**

**The −26.4 segment is neither a broken thesis nor a cleaned base, and the dichotomy is the error.**
The arithmetic: CEG lost **−26.35pp** vs SPY in days 21–60 and has recovered **+10.47pp** in the last 20
⇒ **≈40% retraced, 60% still open.** A cleaned base implies the give-back is complete and the new leg is
building; **CEG's freshest leg is NEGATIVE (RS5 −1.14) and decelerating from RS10 +5.87.** ⇒ **the repair
stopped, five sessions before the print.**

⚠ **And Lens 3's own tag is produced inside the measure's own defect zone.** The lens documented that its
ratio *"is undefined when |RS60| is small"* and *"has no branch for RS20 < 0 < RS60."* **CEG is the
mirror case — RS20 > 0 > RS60 — which the measure also does not branch, and the resulting −56.3% is a
sign artifact, not a share.** ⇒ **CEG's "EXHAUSTED" tag is a measurement output in an unbranched region
and is not carried as evidence here.** The honest statement is the decomposition above.
**This DEEP labels CEG: `REPAIR-STALLED (40% retraced, freshest leg negative)`.**

### 7b · ★ Adjudication — VST: **`DRIFTING` — and the setup's "no base left" framing is the wrong read.**

The setup describes VST as *"a flat, un-crowded start — the harder configuration to dismiss as
momentum."* **The decomposition disagrees on one specific point: VST is not flat, it is BLEEDING SLOWLY
AND UNINTERRUPTEDLY, and its FRESHEST leg is its WORST** (RS5 −3.24 vs RS10 −3.40 vs RS20 −1.66 —
negative at every horizon, with no interval of repair anywhere in 60 sessions). **"No base to give back"
is not the same as "a base being built."** ⚠ **Its RS60 (−4.86) and segment (−3.18) are small enough that
VST is C4-indistinguishable from a slow drift** — and **drift is the state that carries the LEAST
information into a print**, which is the opposite of the setup's claim that it is the harder
configuration to dismiss. **This DEEP labels VST: `DRIFTING (n/m — no measurable momentum state)`.**

### 7c · Positioning context — FINRA short-volume, settled 08-03 *(never a trigger)*

| | short% | 20d base | **z** | **5v5 trend** | verdict |
|---|---|---|---|---|---|
| CEG | 52.9% | 51.3% | **+0.15** | **+4.4 ▲** | 🟡 normal |
| **VST** | 45.5% | 46.0% | **−0.06** | **+13.5 ▲** | 🟡 normal |
| GEV | 57.5% | 54.0% | +0.49 | **−3.3 ▼** | 🟡 normal |
| VRT | 56.7% | 54.1% | +0.36 | **−10.1 ▼** | 🟡 normal |

★ **All four z-scores are inside ±0.5 — there is NO crowding statement available here (C4), and none is
made.** The only readable structure is the **trend sign, and it is cleanly split by node**: short-side
pressure is **rising into both merchant prints** (VST +13.5 the largest of the four) and **falling out of
the equipment layer** (VRT −10.1). ⚠ **Rotation of short exposure from ③④ toward ② ahead of two dated
prints is a description of the last five sessions, not a forecast**, and it is offered as context for
why the 08-06/08-07 tape may be noisier than the z-scores suggest.

### 7d · The sub-leg fails a momentum test too

**CEG `REPAIR-STALLED` and VST `DRIFTING` are two different states.** Add §5a (PTC-damped vs undamped
capacity leverage) and §6b (flat FY vs +11.5% FY). ⇒ **On flow, on RS60, on capacity transmission, on the
denominator, and now on momentum geometry — the two names diverge on every axis this file could measure.
There is no fifth axis left on which "the merchant sub-leg" is one object.**

---

## 8 · Observables for the 08-06 (CEG) and 08-07 (VST) prints

⚠⚠ **NO NEW BRACKET IS REGISTERED.** S35 / S47 / S24 / S40 already own these two prints and PREMORTEM
logged the decision that a fourth row double-counts. **These are OBSERVABLES for whoever scores those
brackets** — read-outs, not a proposition. ⚠ Per **R40/M313** the S35/S47 verdicts remain unusable as
evidence about Utilities and **nothing below is built on either.**

### 8a · CEG — 2026-08-06

1. **★ THE KILL CONDITION, and §6b tells you exactly how to read it.** *FY guided DOWN vs consensus
   **$11.71** ⇒ the leg is a rate-duration trade wearing an AI-power label and the regulated read was
   right for both.* **★ The FY line is the ONE estimate that has NOT been cut (+0.8%/90d) while the
   quarter was cut −7.4% with 1↑:4↓ breadth.** ⇒ **A FY cut would be new information, not a confirmation
   of the tape.** A FY *reaffirm* leaves the kill condition unfired and says the −33.7% was multiple
   compression (§6b).
2. **★★ The most under-covered line on either print: how much of the 18,875 MW at $325 actually reaches
   earnings.** CEG's own 8-K flags that **nuclear capacity revenue enters the 45U PTC gross-receipts
   calculation**, and **83% of the cleared portfolio is nuclear.** **Watch for a quantified net figure.
   If management does not quantify it, that is itself the read** (§5a).
3. **Any NEW dated, named, contracted data-centre MW.** **The 60-day EDGAR contract category is EMPTY
   (§5b)** — so anything disclosed here is genuinely new, and its absence is equally informative.
4. **Whether behind-the-meter / self-supply is named as a demand risk** (§4c). ⇒ *Does the company's own
   demand read agree with the one its investors hold?*
5. **Whether the 2028/29 auction is characterised as scarcity UPSIDE or as a capped/politically-exposed
   revenue line** (§2c: Moody's 07-22, the 60% ratepayer projection, the state legislatures).

### 8b · VST — 2026-08-07

1. **Which line moves — the CUT quarter (−11.2%/90d) or the RAISED year (+11.5%/90d)?** ⚠ **This is the
   opposite configuration to CEG and must be scored separately, not read as a second observation of the
   same fact (S1 — n = 2, and after §7d, arguably n = 1 + 1).**
2. **★ VST is the cleaner capacity read of the pair** — no PTC gross-receipts damping on its PJM fleet
   (§5a). **10,924.4 MW × $325 = $1.296bn/yr from 2028-06-01. Watch whether it is booked as contracted
   or discussed as capped.**
3. **★★ ERCOT self-supply, which is the sharpest question either company will face**: the Hubbard, TX
   campus includes **a 1.6 GW on-site gas plant with its own PPAs, inside VST's home market** (§4b-ii).
   ⇒ *Does management address behind-the-meter generation as competition, as an opportunity, or not at
   all?* **Silence on this is a data point.**
4. **Whether either 07-16 / 06-30 Material Definitive Agreement converts into contracted MW** — both are
   **financings, not offtake, as filed** (§5b).
5. **PJM's September FERC "backstop" auction request** (§2b) — any commentary on it is a direct read on
   whether the capped price is expected to persist.

### 8c · Sector-level cross-checks, same window

- **PCG** — the sector's only 🟢 and the only name with positive RS20 **and** RS60 (+2.8 / **+4.4**) —
  **prints 2026-10-22, out of window.** It cannot be what the sector trades this week, and **no cheapness
  or thesis claim is attached to it** (§0d).
- **GEV 10-28 / VRT 10-21 — both out of window**, per the 07-31 file's own correction. **The equipment
  layer has no in-window print, so ③④ cannot be resolved this week.**
- **NFP 08-07** — duration read on the regulated leg, **owned by S51 and its bull-steepener qualifier;
  not this file's.**

---

## 9 · Track KPIs · anti-signals · dates

| # | Observable (benchmark **SPY** inline) | Settled 08-03 | Resolves / kills |
|---|---|---|---|
| 1 | ★ **CEG FY 2026 guide vs consensus $11.71** | consensus +0.8%/90d, **uncut** | **guided DOWN on 08-06 ⇒ THE KILL CONDITION FIRES**: rate-duration trade wearing an AI-power label |
| 2 | ★ **Merchant median RS20 minus regulated-12 median RS20** | **+8.7pp** | **collapses toward the +2.6pp CEG-excluded value ⇒ the sub-leg was one name (§1b)** |
| 3 | ★★ **Merchant median RS60 minus regulated-12 median RS60** | **−5.05pp (INVERTED)** | **crosses > 0 ⇒ the promotion's window choice is vindicated on a second horizon; stays < 0 ⇒ it was window-selected** |
| 4 | **CEG retracement of its −26.35 segment** | **40% (+10.47 of −26.35), RS5 −1.14** | retrace > 60% with RS5 > 0 ⇒ `cleaned base`; RS20 < 0 ⇒ `repair failed` |
| 5 | **VST RS at every horizon** | −3.24 / −3.40 / −1.66 / −4.86 — **negative at all four** | any horizon crossing > 0 ⇒ drift resolves; unchanged ⇒ `n/m` persists (C4) |
| 6 | ★★ **New generation clearing PJM per auction (the uncapped rate, B1)** | **525 MW, ≈half of 6 months prior, vs a 6.8 GW shortfall** | **a third consecutive halving ⇒ the capacity market has stopped producing supply; a rebound ⇒ the price signal still works.** ⚠ next read: **PJM's September FERC "backstop" auction** |
| 7 | ★ **Consecutive auctions clearing AT the price cap** | **3** | a clear BELOW the cap ⇒ the price series regains information content; a 4th at the cap ⇒ merchant power is administratively priced |
| 8 | **CEG nuclear share of cleared PJM MW subject to 45U gross-receipts** | **15,700 of 18,875 = 83%** | management quantifies the net ⇒ the pair's asymmetry becomes measurable |
| 9 | **PJM ≥50 MW data-centre curtailment start date** | **June 2027** (announced) | delayed/withdrawn ⇒ the behind-the-meter incentive weakens; upheld ⇒ §4c's bypass strengthens |
| 10 | **Copper node — FCX RS20 / RS60 with OBV** | **+3.5 / +1.3, OBV 분산 — indistinguishable from SPY (C4)** | **OBV 매집 AND RS20 > +8 ⇒ the chain reaches ⑦; until then NO copper read is made in either direction** |
| 11 | **ETN RS60** (the layer's only 🟢) | **+0.77 — ≈ index (C4)**, segment −4.26 | RS60 > +8 with the segment positive ⇒ ④ is a real leader, not a 20-day repair |
| 12 | **GEV segment 21–60** | **+0.37 (99.7% of damage in 20 days)** | segment turning negative ⇒ a grind, not an event; **driver remains `unknown` (C3) either way** |
| 13 | **XLU excess vs SPY, 5d / 20d / 60d** | **−5.40 / −2.93 / −5.85** | any horizon > 0 ⇒ the sector UW− itself is in question |
| 14 | **FINRA 5v5 short trend, merchant vs equipment** | **CEG +4.4▲ · VST +13.5▲ vs GEV −3.3▼ · VRT −10.1▼** | ⚠ **all z inside ±0.5 — context only, never a trigger** |

### Anti-signals

- **To THIS file's own §0 verdict**: if VST's 08-07 print moves it decisively positive on RS20 **and**
  RS60 while CEG stalls, the sub-leg becomes a two-name object after all and **§0's "it is one name"
  is wrong.** **One settled session tests it.**
- **To the whole-sector UW−**: the regulated median RS20 crossing > 0 vs SPY. ⚠ **Scored on the groups in
  §1a, NOT on the contaminated regulated-seven (R40).**
- **To §2's administrative-constraint mechanism**: a capacity clear **below** the cap, or FERC denying
  the September backstop with prices then falling — either would say the market is functioning.
- **To §4c's bypass mechanism**: a large new AI load announced with a **merchant PPA** rather than
  on-site generation would show the bypass is deal-specific, not structural. ⚠ **n = 2 deals is the
  entire evidence base for that mechanism — S1 applies to §4 as much as to §1.**

### Dated

**CEG 2026-08-06 · VST 2026-08-07 · NFP 2026-08-07** (owned by S51) · **S35/S47 settle 08-07 on the
regulated-SIX** (not this file's) · **PJM FERC backstop auction: September 2026** · **CPI 08-12 /
PPI 08-13** (outside the window) · **PCG 10-22 · VRT 10-21 · GEV 10-28** (all out of window) ·
**PJM ≥50 MW curtailment effective June 2027** · **2028/29 auction results effective 2028-06-01** ·
**El Paso 1 GW online 2028**.

---

## 10 · What this DEEP hands to BET

1. **★ The promoted sub-leg does not exist as a unit — it is CEG, and CEG is `REPAIR-STALLED`.**
   Permutation-tested over all 105 pairs: **every draw that reproduces the RS20 result contains CEG
   (p = 0.029, 3/3); "0 of 2 🔴" is a 1-in-5 coincidence (p = 0.200); and the flow result is mostly
   produced by PCG, a REGULATED name the promotion silently dropped.** **Remove the largest constituent
   and the leg's RS20 goes NEGATIVE (−1.7)** — the R32 shape that killed "Financials is breadth-led."
2. **★ On the 60-day window the split INVERTS**: merchant −11.6 vs regulated −6.55 vs SPY, **bottom 8%
   of the sector's two-name draws.** The promotion showed RS20 only.
3. **The whole-sector UW− is NOT a weighting artifact and NOT a mega-cap artifact.** wflow −0.234 vs
   eqflow −0.229 (agree to 0.005); the merchant leg is 15.0% of sector cap; **the regulated median gets
   WORSE under every robustness strip available, including the R40-clean ex-D/ex-NEE group (−5.15).**
4. **★★ THE FINDING THE SLOT ACTUALLY RETURNS — B1, and it inverts the promotion's premise.**
   **PJM's 2028/29 auction cleared at $325.00/MW-day = the price CAP, the third consecutive auction at
   the ceiling** (filed by both companies, 07-14), **while new generation clearing collapsed to 525 MW —
   half of six months earlier — against a 6.8 GW shortfall (7.7% of the gap).** **The level is record
   scarcity; the RATE is dead in one series by administrative construction and halving in the other.**
   ⇒ **Merchant demand is real and strengthening while the mechanism that converts it into merchant cash
   flow is capped, failing to attract supply, and politically exposed** (Moody's 07-22; ICF/Reuters 60%
   ratepayer projection; state legislatures; PJM's September FERC backstop request). **A record-scarcity
   grid priced at an administrative constant is a regulated asset wearing a merchant label** — the exact
   mirror of the promotion's claim.
5. **★★ W4/M227 — whose demand signal is the merchant reading? Increasingly, not its own customers'.**
   Two dated financings in three days moved AI capacity off the customer balance sheet: **Meta × BlackRock
   El Paso 1 GW / ~$14bn, 80% asset-manager-owned, $12.5bn debt-funded, leased back with ~$13bn of RVGs
   — with Meta net-RECEIVING ~$1bn cash at close**; and **Nexus/Anthropic/Google Hubbard TX $15bn,
   Google guaranteeing the leases AND the PPAs — including a 1.6 GW ON-SITE gas plant inside VST's home
   ERCOT market.** ⇒ **behind-the-meter self-supply routes around the merchant generator, and it
   explains why auction-cleared new supply halved while demand set records.** ⚠ **n = 2 deals (S1).**
6. **★ Primary source: what exists is a CAPACITY CLEAR, not a PPA.** CEG **18,875 MW** (15,700 nuclear)
   and VST **10,924.4 MW**, both at **$325.00**, effective 2028-06-01, from 07-14 8-Ks. **CEG's 60-day
   contract/M&A category is EMPTY; VST's only Material Definitive Agreements are financings.**
   **★ And the filings disclose an asymmetry inside n = 2**: CEG's nuclear capacity revenue **feeds the
   45U PTC gross-receipts calculation (83% of its cleared MW)** while VST's does not ⇒ **VST is the more
   levered, cleaner capacity read; CEG's is self-damped.**
7. **B2 — neither is cheap, and they are not the same kind of not-cheap.** ⚠ **M233 fired on BOTH
   (`연간 데이터 없음` × 2) so no margin percentile exists and no cheapness claim can be completed (C3).**
   **CEG: the FY line is UNCUT (+0.8%/90d) against a −33.7% price move ⇒ multiple compression, not an
   earnings break — which makes an 08-06 FY guide-down a NEW fact and sharpens the kill condition.**
   **VST: fwd P/E 14.13 rests entirely on forward EPS +64% above trailing, at P/B 15.82, with a 3.02×
   analyst target range and one Strong Sell.**
8. **The binding constraint is ADMINISTRATIVE, not physical** — the capacity market clearing 7.7% of its
   own reliability gap, plus **PJM curtailing ≥50 MW data centres from June 2027.** **Demand is
   explicitly not the constraint** (record 168.2 GW peak, and the auction still capped with a shortfall).
9. **⚠ Two declined reads, both refusing the KR-desk "right direction, wrong driver" shape.**
   **(a) The copper node is traced and shows NOTHING**: FCX is n = 1, RS20 +3.5 / RS60 +1.3 —
   indistinguishable from SPY — with OBV 분산. **No copper read is made in either direction.**
   **(b) GEV's driver is `unknown` (C3)**: 99.7% of its 60-day damage landed in 20 sessions, coincident
   with the AI-capex earnings block, and this file attributes it to neither power nor semis.
10. **⚠ Three inherited numbers were re-measured and TWO were wrong.** **(i) D74 re-contamination in the
    promotion's price line** — $266.08/$145.77 are not settled closes; **corrected drawdowns are CEG
    −33.7% (not −35.5%) and VST −29.1% (not −33.7%).** **(ii) An undeclared n=12-vs-15 exclusion** that
    dropped PCG, the sector's only 🟢 and best RS60 name, from "regulated" (immaterial to the median,
    material to the framing). **(iii) R41 — the inherited superlative "ETN is the ONLY 🟢 in the AI-power
    adjacent layer" is true as a TAG and false as an excess claim**: ETN's RS60 is **+0.77 ≈ index**, its
    segment is −4.26, and its RS20 is 669% of its RS60 — a 20-day repair, not a leader.
11. **⚠ No name in this file carries a 4Phase, and none is a candidate.** CEG and VST are named for the
    ledger and for the 08-06/08-07 read-out only. **No new bracket is registered (S35/S47/S24/S40 own
    these prints).** **No S35/S47 verdict is cited as evidence anywhere (R40/M313).** **No lead/lag claim
    is inherited or asserted (W2).** **No OBV state is cited alone (D6) — every read carries its RS pair.**

---

## ✅ EXIT CHECK

- [x] **§0 tests the promotion instead of justifying it** — and returns *"the split is real but
      unmeasurable at n=2; what is measurable is one name,"* which the mandate defines as a success.
- [x] **Split re-derived independently from `SECTOR_FLOW_US.json`**, grouping declared arbitrary (**C5**),
      **R32 largest-constituent test run on BOTH legs** (merchant fails, regulated survives), **EW vs CW
      switch run**, and a **105-pair permutation test** supplied for every headline statistic.
- [x] **B1 satisfied with RATES, not levels** — clearing price capped 3 auctions running (rate ≡ 0 by
      construction) and new supply clearing halved in 6 months against a 6.8 GW shortfall.
- [x] **W4 satisfied with named customers and DISCLOSED spend**, and **M227 answered as a mechanism**
      (behind-the-meter self-supply routing around the merchant node), **with n=2 declared**.
- [x] **Primary-source hunt run on both names**; **what exists (18,875 / 10,924.4 MW at $325, filed
      07-14) and what does NOT (no data-centre PPA in 60 days) are both stated plainly**, plus a
      filing-disclosed **PTC asymmetry inside n=2**.
- [x] **B2 attempted and its unavailability stated** — **M233 fired on 2 of 2**; no cheapness claim
      completed; every multiple carried with its denominator and revision breadth.
- [x] **Value chain = 7 nodes with the binding constraint named as administrative**, demand explicitly
      excluded as a bottleneck, **cross-sector AI→power→transformers→copper marked and the copper node
      DECLINED (n=1, C4)** — the KR-desk retraction shape refused at the point of tracing.
- [x] **Momentum geometry adjudicated with the segment decomposed**: CEG `REPAIR-STALLED` (40% retraced,
      RS5 negative), VST `DRIFTING` (`n/m`) — **and Lens 3's own tag shown to sit in its own documented
      unbranched region.**
- [x] **Observables only for 08-06/08-07 — NO fourth bracket registered.** Kill condition carried
      verbatim **and sharpened** by the finding that CEG's FY line is the one estimate still uncut.
- [x] **Carry rules**: C1 SPY inline throughout · C2 both halves of every print · C3 unknowns marked
      (copper driver, GEV driver, margin percentiles, uranium instrument, lead-time series) · C4
      "indistinguishable" used where true (FCX, ETN RS60, VST RS60, all four short z) · C5 groupings
      declared · S1 declared on n=2 names AND n=2 deals · W5 dispersion carried inside the pair ·
      D6 every tag graded and none load-bearing · R41 inherited superlative re-scanned and corrected ·
      W2 no lead/lag inherited · **R40/M313 fully honoured** · **P4 — zero buy/sell language, zero sizing.**
- [x] **Three inherited numbers re-measured; two corrected in place and logged, not silently fixed.**
