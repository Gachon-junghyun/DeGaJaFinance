# BET_SHEET — industry_US — 2026-07-24 (Fri)

> Stage 8/10. **ONE file, per-sector sections** — downstream desks glob this exact filename, never split.
> Every relative figure names **SPY** inline (**C1**). Flow asof **2026-07-23 settled close**.
> Fundamentals pulled **2026-07-24**. Analytical only — **zero buy/sell, zero sizing.**
>
> ⚠ **Run-clock update, binding on everything below.** The run opened at 09:09 ET with the US session
> shut; **the 2026-07-24 US session OPENED mid-run (~09:30 ET) and was live when the DEEP agents
> pulled.** Every 07-24 figure anywhere in this run is therefore an **incomplete bar** and is refused
> for any conclusion (**D31 / D48**). The DEEP-ENRG file proved the point twice on the same day: the
> 07-24 crack bar computed **58.21 (−12.4%)** against a settled 07-23 crack of **66.49**, on RB volume
> of **19,456 vs 27,662** — an unfinished session.

---

## §0 · ★★ THE FINDING THAT REORGANISES THIS SHEET — the two "independent" OW legs are one bet

The run entered BET with two overweights it believed were diversifiers: **Energy (refining)** and the
**Industrials rail node** promoted over Info Tech. **DEEP-INDU measured them to be the same trade.**

| Evidence | Measurement |
|---|---|
| **UNP's Q2 revenue growth composition** | ★ **~8 of 12 revenue growth points are FUEL SURCHARGE**; ex-surcharge freight revenue **+4%** |
| **CSX intermodal** | **+26% revenue on +9% volume**, RPU **+16%**, the company's own words: *"driven by fuel surcharge"* |
| **Base rate** | Q1'26 YoY was **~flat at all three rails** — the inflection is the surcharge, not the freight |

⇒ **The rail leg is a second expression of the Energy OW, not a diversifier. `S8` branch A (crude
falls AND the diesel crack rolls over) would hit three positions on one tick, not one.**

**And PREMORTEM §3b had already measured a third layer of the same concentration** (SPY-residual,
251 sessions to 07-23): **XLE–^TNX +0.326** against **XLU–^TNX −0.227 · XLRE–^TNX −0.302 ·
XLP–^TNX −0.194**, with **XLU–XLRE +0.538 · XLRE–XLP +0.565** — two of the three N− pairs clearing
**R10's own 0.35 unit threshold**. Plus **VLO–MPC residual +0.864** inside the refining node itself.

> **Net: what the sector labels present as OW Energy + OW− Industrials + three separate N− tilts is,
> on measurement, largely ONE macro bet — the oil→rate axis — expressed five ways.** This is stated
> here rather than in a risk appendix because it is the single most decision-relevant number the run
> produced, and because **R10 was retracted for asserting exactly this shape without measuring it.**
> **This time it is measured.** ⚠ Scope, stated: these are *ordinary-session* correlations. They say
> nothing about a day when every leg's discount rate moves at once — which is **S19, five days out.**

---

## §A · ENERGY — the refining node

**Candidate set** = DEEP-ENRG thesis leaders ∪ Energy screener setups ∪ LIVE-shortlist Energy names.
★ **The Energy screener returned ZERO setups across all three baskets** (leader-pullback /
de-rate-snapback / washout) over 16 names — **there is no non-chasing entry structure in this sector
by the screener's own definitions.** That is stated as a finding, not omitted.

### §A-1 · Numbers (`module_fundamentals_us`, pulled 2026-07-24 — ⚠ prices are intraday)

| | Fwd P/E | Fwd EPS | Mean target | Price vs target | CY EPS Δ/90d | Next-Q Δ/90d | Current-Q breadth (7d / 30d) |
|---|---|---|---|---|---|---|---|
| **MPC** | **10.71** | $29.19 | $298.12 | **+5.0% ABOVE** | +65.8% | **+104.2%** | 2↑/0↓ · 5↑/2↓ |
| **PSX** | **11.02** | $18.86 | $203.89 | **+2.2% ABOVE** | +42.0% | +62.2% | 2↑/0↓ · 6↑/2↓ |
| **VLO** | **12.27** | $24.88 | $287.28 | **+6.4% ABOVE** | +33.4% | +78.8% | ★ **6↑/5↓ · 7↑/5↓** |
| XOM *(control)* | 14.64 | $10.73 | $167.14 | **−5.9% (upside)** | +8.6% | +6.1% | **0↑/2↓ · 0↑/4↓** |

★ **R8 holds a third consecutive run: MPC 10.71 < PSX 11.02 < VLO 12.27.** The human-locked
`core_pick` rationale that calls PSX "the cheapest large refiner on forward" remains **wrong on the
numbers** and is not rewritten here (the field is human-locked; the correction is recorded).
★ **All three refiners trade ABOVE mean consensus target while XOM trades below it** — the low
multiple and the exhausted target are one fact seen twice (**lens L2**).

⚠ **The peak-margin half of L2 is NOT settled and the file says so.** Annual gross margin (SEC XBRL):
**MPC FY2025 10.0%** against a 14.5% peak and a 10.5% median; **PSX 12.3%** against a 25.9% peak and a
12.1% median — *below/at* their own medians, not at a peak. **But that table cannot settle the
question**, for two independent reasons: a refiner's annual gross margin is **structurally diluted by
crude passthrough in the revenue denominator** (crude went from a 2025Q4 mean of $59.14 to a 2026Q2
mean of $92.70), and **the 2026 crack spike cannot appear in any FY2025 series at all.**
**`margin_history.py VLO` returns no annual data — a confirmed tool gap**, routed around with five
quarters of XBRL/yfinance.

### §A-2 · Thesis (freshness placeholder — ALPHA fills)

**The margin is real and is being paid in cash by identifiable third parties. What is unresolved is
the second derivative.** Three legs, none of them the futures strip:

1. **A supermajor booked it as realized cash for the exact quarter**: TotalEnergies Q2'26, reported
   2026-07-23 — **European Refining Margin Marker $12.4/bbl, +19% QoQ, against $4.3/bbl in 1H2025**;
   adjusted net income **$6.0B, +12% QoQ / +68% YoY**. Equinor **+93% YoY** the day before.
2. **The physical rate is at the ceiling** — EIA week to 2026-07-17: **US refinery utilization 96.2%**
   (94.7% a year earlier), **PADD2 and PADD4 at 100%**; commercial crude stocks 6% below the 5-year
   average. *A war premium is paid for feared future scarcity while throughput is normal; a margin is
   what you earn when you are physically sold out.*
3. **The settled WEEKLY distillate crack is still rising**: 56.42 → 61.91 → 67.63 → 74.81 → 87.30 →
   **88.94** over six settled weeks, with the diesel-minus-gasoline gap **10.78 → 31.81**.

★ **The primary-source mechanism, body-read this run**: **Russia banned diesel exports on 2026-07-08,
running to 2026-07-31**, after Ukrainian strikes on its refineries (Moscow, TANECO) that shifted
middle-distillate output toward **HSGO rather than ULSD**. Russian diesel exports ran **214 kbd in the
week from June 29 — down 492 kbd YoY and 615 kbd vs the 5-year average.** The 2023 precedent quantifies
the transmission: **Brazil's Russian imports fell 66 kbd m/m while US deliveries rose 71 kbd m/m**, with
*"the US maintaining maximum refinery runs over 17mn bbl/d against seasonally weak domestic diesel
demand"* [Kpler]. Morgan Stanley: European diesel inventories *"falling to multi-year lows toward
year-end… the picture is genuinely tight."*

⚠⚠ **And the mechanism that ends it is already running, quantified, and named by PSX's own 10-K
Item 1A before the desk named it** — its first-listed margin risks are *"production levels of refined
products by competitors"* and *"import and export capabilities."* Measured: **India is on track for
1.55M bpd of light/middle distillate exports in July against 866k bpd in May — nearly double
sequentially, the second-highest month in Kpler's series since 2017.**
★ **Plus a DATED one the desk did not have: the Russian export ban EXPIRES 2026-07-31**, and the same
source records the **2023 ban was partially lifted after two weeks**. That is three days after VLO
prints and one day after STNG prints.

### §A-3 · Flow / positioning cross-read

| | flow | RS20 vs SPY | RS60 vs SPY | OBV | vol_surge | tag | FINRA z (07-23) |
|---|---|---|---|---|---|---|---|
| MPC | +0.617 | +26.0 | **+34.2** | 매집 | 0.91 | 🟡 | −3.29 ⚠ see below |
| VLO | +0.594 | +25.2 | +24.9 | 매집 | 0.87 | 🟡 | +0.38 |
| PSX | +0.667 | +22.1 | +22.9 | 매집 | 1.00 | 🟡 | −0.33 |
| XOM | +0.696 | +13.9 | **+2.7** | 매집 | 0.87 | **🟢** | **+3.13** |

★ **All three refiners are 🟡 solely because `vol_surge` < 1.2** — the M25/M38/M55 gate, now measured
on four dates in two markets (**92 names pass OBV ∧ RS20>0, only 22 are 🟢, all 71 blocked by
`vol_surge` alone**). **The 🟡 is a volume test, not a flow statement.**

★★ **The FINRA z-spread is DEMOTED to a baseline note by this run's own measurement, and must not be
carried as positioning.** Decisive test from DEEP-ENRG: **MPC and PSX printed the IDENTICAL 36.4%
short-volume share on the identical day** and scored **z −3.29 vs −0.25** — the entire difference is
the denominator (MPC's baseline **53.9–57.1%**, chronically 10–13pp above the tool's own stated 40–45%
normal band; PSX's **37.2–43.9%**). *A statistic that assigns opposite labels to identical readings is
describing the baseline, not the day.* And MPC's own 5-vs-5 trend is **+3.9 ▲**, i.e. pointing the
other way. **XOM's +3.13 is real in magnitude but arrived on a session XOM beat SPY by +2.81pp** —
consistent with market-maker delta hedging, which FINRA's definition includes `[inferred]`.

⚠ **Risk-unit note (binding for any downstream sizing, which this desk does not do):** **VLO–MPC
SPY-residual correlation +0.864 over 251 sessions** — *on price these are one risk unit with three
tickers.* **On fundamentals they are three businesses**: crack-beta of gross profit **VLO +0.836 ·
MPC +0.307 · PSX +0.238** (n=5; MPC/PSX `indistinguishable` from zero), because VLO is 15 refineries
plus renewables/ethanol while **PSX runs five segments including a 50% CPChem JV** and MPC three
including Midstream. **They move together on the crack headline and separate on their own print dates.**

### §A-4 · Competition / peers

XOM is the **control, and is now measured as one**: its same-day correlation to the crack is **+0.078,
`indistinguishable` from zero** (n=535). It carries no measurable crack exposure — which is precisely
why the crude-vs-refining split is a split between **two different KPIs**, not two flavours of one.
**Chain-hop on `refining ∪ diesel` (14d, foreign) produced ZERO promotable candidates**: WMB, CME,
SPGI, CEG, GEV surfaced as body-proximate, and **the flow cross-check kills WMB immediately**
(flow −0.115, RS20 −1.5 / RS60 +1.9 vs SPY). **A co-mention is not a candidate** — this is the
**seventh consecutive run** in which this node's chain-hop promotes nobody.

### §A-5 · Refutation + dated catalysts

| Anti-signal | Threshold | State | Distance |
|---|---|---|---|
| MACRO P4 / S8's registered kill | **settled crack < 60.00 with WTI > $90** | crack **66.49**, WTI 92.19 | **$6.49 — armed** |
| ★ The distillate bottleneck releases | gap (dist − gas) below **$15** | **31.81**, widened 5 weeks | far, moving away |
| ★ Competitor supply response | 2nd month of Indian/Asian export ramp **coinciding with a falling weekly distillate crack** | India +79% sequentially **but the crack is still rising — the halves disagree, so it has NOT fired** | monitor monthly |
| ★ **New, dated** | **The Russian diesel export ban lapses 2026-07-31 and is not renewed** | ban live | **D-7** |
| ★ This node's own falsifier | **VLO reports gross margin < 10.0% on 2026-07-30** | consensus **EPS $10.127 / rev $38.429B implies gross margin going 6.30% → ~12.6%**, where 6.30% is VLO's own **5-quarter maximum** | **D-6** |
| A7 | If VLO/MPC/PSX print within ~1pp of each other on gross margin across 07-30 / 08-04 / 08-05, the "three businesses" reading is wrong | — | 2026-08-05 |

★★ **The L1 rate-of-change finding, which is what actually governs this section**: the crack's **level**
is the highest weekly mean in the series (67.73) and the 89th percentile of 90 days; its **rate** is
**+0.12% WoW, arithmetically flat**, down from +9.21%, with the quarterly second derivative at
**−31.94** on the partial Q3. **Level makes the headline; the second derivative makes the decision.**
⚠ But the flat composite is **a stalling gasoline leg (57.82 → 57.12, −1.2%) netting a still-rising
distillate leg (87.30 → 88.94, +1.9%)** — not a margin that stopped.

★ **The C4 detachment counter is re-graded `indistinguishable`, not "rejected."** Measured n=535,
lags −4..+4: the crack↔refiner link is **same-day only** (VLO +0.301, MPC +0.238, PSX +0.219) and every
lagged cell is inside ±0.07. At r=0.30 a **three-day sign disagreement happens ~6.5% of the time by
chance** — the counter is **under-powered as constructed** and needs a magnitude condition, not a
5-day count. And the rolling-60 correlation is **rising** (VLO 0.235 → 0.404): the equities are
tracking their KPI **more** closely, which is the opposite of detachment.

**Dated calendar**: **UPS 07-28 (S20)** · **VLO 07-30** · **STNG 07-30 (S21, ±10.0% D28 — usable)** ·
**XOM 07-31** · **MPC 08-04 (±11.2% D28 — usable)** · **PSX 08-05**.

---

## §B · INDUSTRIALS — the rail node (promoted 4th slot)

### §B-1 · Numbers and the verdict that reorganises the section

| Node (own re-aggregation, 50 rows) | n | mcap share | wflow | med RS20 vs SPY | med RS60 vs SPY | 🟢 | 🔴 |
|---|---|---|---|---|---|---|---|
| **RAIL (CSX, UNP, NSC)** | 3 | 5.8% | ★ **+0.848** | **+14.0** | **+10.0** | 2 | **0** |
| 5 primes (GD RTX NOC LMT LHX) | 5 | 11.3% | +0.655 | +10.2 | +7.5 | 1 | 0 |
| Capital goods + electricals | 29 | **66.3%** | **−0.150** | −0.6 | −0.6 | 1 | 7 |
| Other freight/logistics (UPS FDX ODFL DAL UAL UBER) | 6 | 8.7% | **−0.302** | −4.2 | +1.8 | 0 | 2 |
| **All Industrials** | 50 | 100% | +0.019 | +1.8 | +2.0 | 4 | 9 |

★★ **THREE legs, not two — and M36 is corrected, not confirmed.** The primes-vs-capital-goods spread
is **0.805** on the 07-23 close, **above M26's original 0.705**. M36's *"decayed to 0.285"* measured a
**one-session trough the day before both primes printed.** The genuine finding underneath M36 was never
decay: **leadership had rotated to a third node the desk was not measuring.**

★★★ **The promotion's own stated reason is RETRACTED (correction C-B).** PREMORTEM Lens 1 promoted
this node on the words *"the rails next print 2026-10-22/23, so this accumulation is post-print and
event-free."* **Primary filings say otherwise: CSX 8-K Item 2.02 on 2026-07-22; UNP and NSC 8-Ks on
2026-07-23** — 0–1 sessions before the flow snapshot. **The flow score, OBV state and 1.18–1.63 volume
surge are the event's own footprint, counted a second time as independent confirmation of it.**
⚠ **This is the SAME failure class as D50** (PYPL's RS20 being a takeover spread read as breadth) —
**an event spread read as a flow signal, replicating in a second sector on the same date, uncaught by
any earlier stage.** The promotion stands (the divergence was real and orphaned); **its reason does not.**

★★ **And it is a RAIL trade, not a freight trade.** σ-normalized on 07-23 (benchmark **SPY −1.23%**):
**CSX +4.91σ · NSC +4.54σ · UNP +2.97σ** — while **KNX −2.41σ on its own beat-and-raise**, ODFL −0.50σ,
JBHT −0.42σ, UPS −0.85σ, LUV −3.47σ. **No freight-demand cycle was bought.**

### §B-2 · Thesis, and why it is not a diversifier

**Binding constraint = rail terminal dwell / network fluidity** — not demand, and not truck capacity.
Demand is *contracting*: **Cass Freight shipments −4.1% YoY and −3.1% MoM in June.** Truck capacity is
a constraint on the **substitute** mode (KNX: revenue/tractor +6% on a **3% decline in trucks in
service**), which is an opportunity, not a bottleneck. CSX's COO on the record: velocity +3% YoY but
**dwell increased** and *"service metrics aren't where we want them to be."*

⚠⚠ **See §0: ~8 of UNP's 12 revenue growth points are fuel surcharge; CSX intermodal RPU +16%
"driven by fuel surcharge"; Q1'26 YoY was ~flat at all three.** **This node's earnings inflection is
the Energy thesis arriving through a different income statement.**

### §B-3 · Flow / positioning · §B-4 · Chain-hop and peers

CSX **+0.878 / RS20 +14.0 / RS60 +13.0 / OBV 매집 / surge 1.38 / 🟢** · UNP **+0.867 / +16.4 / +10.0 /
매집 / 1.36 / 🟢 new_green** · NSC **+0.767 / +14.0 / +6.1 / 매집 / 1.18 / 🟡** · WAB (node 5)
**+0.758 / +8.7 / +8.3 / 중립 / 1.63 / 🟡**. FINRA z: **CSX −1.00, UNP −1.42 = clean-rise.**
CSX and UNP sit at the **99.3rd / 99.0th percentile of flow across all 300 names**.

**Chain-hop: ZERO PASS**, with two named tool defects — **`EMR` collided with East Midlands Railway**
in a BBC UK strike story, and **`rail` is a poisoned FTS token (~40% fintech "payment rails")**. The
real chain (JBHT, KNX, SNDR, XPO, GATX, TRN, CNI, CP) is **entirely outside `us_top300`**.

★ **L2 inverted here: the only cheap name is the only one the money is not in.** **UPS 14.25× forward,
+0.6% to mean target, 5.75% yield, zero Strong Buys — the node's lowest flow, its only negative delta,
and the only one that fell.** The five names the money is in trade **20.3–25.0×**, three above target.
⚠ **NSC's 16-of-21 Hold book with PEG 4.83 is a deal price, not an earnings price** — and **UNP's
Item 1A returned 10 bullets, all merger risk** (the UNP–NSC merger's STB settlement leg advanced 07-22).

### §B-5 · Refutation + dated catalyst

**S20 (UPS, 2026-07-28)** is the node's only in-window observable, and its three branches are carried
unmoved. **Implied move ±1.3–1.7%, expiry 2026-07-24 = D0 — NOT event-priced, declared unusable**, so
the observable is categorical. **New measured prior**: UPS is priced at **+0.6% to mean target — the
Street expects nothing.** ⚠ **Branch C must be scored on the rails' own dwell KPI, not on UPS's price
reaction** (**D28**: never put a price reaction inside an observable's branch).

---

## §C · HEALTH CARE

### §C-1 · The verdict that governs the section

★★ **"Breadth 0.19 = best on the board" and "wflow +0.396 > eqflow +0.197" are ONE concentration fact
written twice.** DEEP-HLTH's re-aggregation: **the six 🟢 names {LLY, JNJ, ABBV, UNH, MRK, TMO} are
exactly the six largest names in the sector by market cap, ranked 1–6, with zero members drawn from
ranks 7–32.** Top-5 = **50.6% of sector cap but 77% of sector wflow**; **LLY alone 27%**. The other
**27 names**: eqflow **+0.121**, **1🟢 / 4🔴**.
⇒ **ROTATION moved this tilt to OW on a breadth argument that does not survive the re-aggregation.**
The **delta flip is real** (−0.102 → **+0.045**) and is the part of the OW that stands; **the breadth
half is withdrawn here.** **C7 is NOT resolved** — it is restated, because two of its three "against"
legs are now false and a contradiction cannot be adjudicated on retired evidence.

### §C-2 · The three C7 legs, and the MRK verdict

| C7 leg | Status | Measurement |
|---|---|---|
| Deceleration (Δ −0.102) | **FALSE** | Δ **+0.045**. ⚠ But **11 of 32 names carry a negative delta** — say *"no longer decelerating"*, not *"accelerating"* |
| "No health-care narrative" | **FALSE** | Novo-v-Lilly **34 art / 10 outlets on 07-21**, REIGNITED today; **plus TMO's own Q2 print** |
| "Revision books are flat" | **PARTLY FALSE, and dispersed** | **TMO next-quarter 15↑:2↓** and **UNH next-year 8↑:0↓ with CY EPS +9.8%/90d**, both from dated prints — against **ABBV next-year 1↑:4↓ (30d), 0↑:5↓ (7d)** and **MRK 0↑:0↓ at every horizon** |

★★ **MRK's −46.0% CY revision is an accounting-basis artifact, not a business deterioration.** The
arithmetic: **Terns (~$5.8B pending) ÷ 2.4698B shares = $2.35/share against the −$2.34/share
current-quarter consensus swing — a 0.4% match.** Cidara ($9.0B) booked Q1'26; management's own
non-GAAP FY guide **$5.04–5.16 vs a $2.77 consensus**; the 90-day window contains **one earnings 8-K
and zero adverse 8-Ks**; **0↑:0↓ is not "the worst revision book" — it is no revision book.** Revenue,
Keytruda (+12%), Winrevair (+88%) and the dividend all rose.
⚠ **Three residuals, not laundered**: the charge sizes are **`[news]`-grade** (no 8-K carries them;
**resolves 2026-08-04**), **$3.66/share of FY arithmetic is unexplained** `[unverified]`, and
**Keytruda is 48.7% of FY2025 sales — a charge verdict is not an LOE verdict.**

★ **The sector's largest 07-23 move was an earnings print, not a defensive rotation**: **TMO +8.71%
= +9.95pp vs SPY = +5.64σ**, and **MRK +1.70σ** — both larger than LLY's +1.36σ and ABBV's +1.35σ,
which this run had carried as the board's largest. **Corrected.**

### §C-3 · Litigation scope, and §C-4 · dispersion

**Advertising only.** *Novo Nordisk Inc. v. Eli Lilly*, **D.N.J.**, Lanham Act, filed 2026-07-21; PI
motion **2026-07-24**. Subject: comparative DTC ads pitting **Zepbound 10/15 mg against Wegovy
1.7/2.4 mg**, omitting the **7.2 mg Wegovy approved March 2026**; one commercial cited at **>700M
impressions**. Relief: injunction + **corrective advertising** + disgorgement. **No product, label,
patent or approval is at issue; the transmission to revenue is indirect and one hop. Hearing date
[blank] — absent from 118 bodies over 14 days, and not guessed.** ⇒ **It gives LLY a name-specific
cause and explains none of the other five greens.**

★ **W5: the sector label is the wrong unit.** Sub-node wflow spread **0.633** (Tools +0.641 vs
Equipment +0.008) = **1.6× the sector's own level**; RS60 spread **HUM +73.2 → ISRG −32.7 = 105.9pp =
42× the sector's 07-23 move vs SPY**. **Equipment is the hole**: 14.2% of cap, **eqflow negative, zero
greens, three of the sector's four reds.** The screener agrees independently — **BSX −41% vs its
200DMA, ISRG −31%, ALNY −24%, IDXX −14%**, all washed out while pharma is 🟢.

### §C-5 · Refutation + dated catalysts

**Three dated resolvers, none of which lands before 2026-07-31:** (1) the **eqflow−wflow gap, today
−0.199** → narrows to ≥ −0.05 ⇒ *sector*; stays ≤ −0.15 ⇒ *concentration*. (2) ★ **one 🟢 from outside
the top-6 by market cap — today ZERO of 26 such names** (watch **ABT**, flow +0.667, blocked by
`vol_surge` 1.00 alone); this is worth more than a fifth #1–#2 wflow print because it is the only
observable the concentration reading cannot also produce. (3) **Health Care Equipment RS60 vs SPY
after EW (07-24), BSX (07-29), SYK (07-31).**
⚠ **S19 exposure, qualified**: PREMORTEM named Health Care as the first tilt hit on the hike branch.
DEEP-HLTH's own measurement puts **XLV at −0.198 vs Δ^TNX, behind XLRE −0.293 and XLU −0.220** —
**HC is not the most rate-sensitive tilt**, so S19's "hit first" must rest on the **concentration**
leg, not on rate beta. And **the rate relationship is entirely same-session** (±1/±2 day ≤ 0.075):
**a rate move gives zero advance warning here.**
**Dated**: HCA + EW **07-24 (today)** · **HUM 07-29** (reject-ledger recheck 07-31) · BSX 07-29 ·
CI 07-30 · **ABBV + SYK 07-31** · **MRK 08-04 (where the charge numbers become `[primary]`)** ·
LLY + CVS 08-05.

---

## §D · FINANCIALS

### §D-1 · The mandate's stated alternative is REJECTED by measurement

Own re-aggregation of all 47 rows into six buckets (grouping stated, alternative computed, C5):

| Bucket | n | share of names | mean flow | cap-wtd | share of Σ+ | mean RS20 vs SPY | mean RS60 vs SPY |
|---|---|---|---|---|---|---|---|
| **Exchanges & data** | 7 | 14.9% | ★ **+0.487** | **+0.482** | 19.2% | +6.3 | ★ **−8.8** |
| **Insurance** | 12 | 25.5% | +0.462 | +0.418 | ★ **33.0%** | +6.6 | **+8.5** |
| **Payments** | 4 | ★ **8.5%** | +0.460 | +0.525 | ★ **10.3%** | +10.8 | +6.3 |
| Banks | 9 | 19.1% | +0.297 | +0.337 | 18.9% | +1.6 | +5.9 |
| Other | 10 | 21.3% | +0.162 | −0.017 | 13.5% | +4.3 | +2.3 |
| Capital markets | 5 | 10.6% | +0.081 | +0.112 | 5.1% | +1.8 | +12.6 |

★ **Payments is 8.5% of names and 10.3% of gross positive flow — below its 15.0% share of sector
market cap. It is not the concentration.** The bucket that actually leads is **Financial Exchanges &
Data**, which every prior pass buried inside a 17-name "other" residual.
★ **Correction to this run's own upstream stages**: SWEEP §3 and ROTATION §3 both said *"money-centers
are absent from the entire 🟢 shortlist."* **JPM is one of Financials' five greens** (flow +0.576,
RS20 +4.3 / RS60 +9.1 vs SPY); it is missing from `US_LIVE_SHORTLIST.json` only because that file is
**top-15 truncated at PM +0.631**. The five greens are **2 insurance + 2 payments + 1 money-center bank.**
★ **The "breadth-led" signature is a large-cap DRAG, not a small-cap surge**: cap-ranks **#6–10
(MS, GS, WFC, C, AXP — ~$1.40T, 18.5% of sector cap) average flow −0.166**, while the 37 names outside
the top 10 average **+0.386**.

**Verdict: `indistinguishable` (C4), because two definitions give opposite answers on the same rows.**
*Risk-unit breadth* = **YES** — all pairwise SPY-residual correlations **0.124–0.313, every one below
R10's own 0.35 threshold** ⇒ four genuinely separate legs. *Business-model breadth* = **NO** —
fee/float earners (23 names) take **62.5%** of gross positive flow at mean +0.469, against
balance-sheet earners (24 names) at **37.5%** and mean +0.195, with **1 vs 8** negative-flow names.

### §D-2 · What is left holding the OW−

| Leg | Status |
|---|---|
| ① 2s10s steepener | ★ **DEAD** (R11) — 2s10s **+0.36, flattening a second session**; 2y **4.31% = 120-day high** |
| ② The rate-sensitivity wedge (S9's premise) | ★★ **PREMISE UNSUPPORTED** — **TRV–^TNX −0.129, CB–^TNX −0.010**, both **positively** correlated to XLRE (TRV +0.386). The P&C leg is a mild duration **long** that **offsets** the short-UTIL/RE leg. **Same shape as retracted R10** |
| ③ Breadth | **The survivor, re-characterised not confirmed** — and one of its named legs (payments) has a **takeover spread inside it** (D50), while another (exchanges & data) is **7-for-7 negative on RS60 vs SPY** |

⇒ **The OW− is held by the re-characterised breadth plus credit refusing stress for a 5th run**
(**HY OAS 2.68%, 5bp off a 365-day low; IG 0.78%; NFCI −0.552, loosening a 5th week**). **P2's kill
line is untouched: HY OAS > 3.10% on a close.**

### §D-3 · Numbers, flow and the named constraints

**MA** fwd 23.35, **+21.0% to mean target — the largest upside in Financials**, CY breadth 4↑:0↓ but
current-quarter 0↑:1↓ · **V** fwd 23.69, +14.3% upside, **CY 7↑:0↓**, next-year 6↑:0↓, **FINRA z +1.68
spike** · **TRV** fwd 12.80, **−7.8% (above target)**, CY EPS **+21.1%/90d with almost all of it in the
last 7 days** — price and estimates moved together and price got there first · **GS** fwd 14.63,
+5.7% upside, **CY EPS +19.5%/90d on 9↑:0↓ both years** — the sector's best revision book, attached to
flow −0.062 and RS20 −0.9 vs SPY (RS60 **+11.4**) · **C** fwd **10.39, PEG 0.72, +16.1% upside** —
cheapest with the most upside and **the only one whose revisions are outright negative** (next-quarter
−5.6%/90d), which is the coherent half of its 🔴.

★ **The exchanges bid has a named cause on BOTH signs.** Up: **NDAQ Q2, 2026-07-23** — net revenue
**$1.5B +15%**, **Market Services a record $340M**, **Index ETP AUM through $1 trillion**, 26 IPOs
raising **$106B including SpaceX at $86B**. Down: the **CFTC allowed Kalshi and Coinbase to offer
perpetual crypto futures**, and *"shares of Nasdaq, CME Group and ICE have declined between 5.4% and
12.6% so far this year."* ⇒ **The sector's highest-mean bucket is bid on a volatility rent while being
de-rated on a structural market-share threat.**
★ **The insurance constraint is quantified by a named CEO, on the record.** Chubb Q2 (07-21/22):
core operating EPS **$7.26 (+18.2%)**, combined ratio **83.8%** — against **Evan Greenberg**: soft
conditions *"have begun to extend beyond property into more casualty lines,"* pricing *"is not keeping
pace with loss costs,"* and *"there is zero evidence across the industry that loss costs have abated."*
**North America commercial rate −1.4%** (the +1.3% headline is +2.7% exposure), **property −6%**,
**NA commercial premiums −2.3%**, major account & specialty **−9%**.

★ **The CRE headline is body-refuted** (EVENT_ALPHA Card 5): the 9-outlet, 5-day-BUILDING head event
carries **no body in the pool**, and the only bodied member that quantified lending volume —
**BankUnited, 07-22** — **cut** FY core loan growth to **4–5%** *"because of tougher competition and
tighter pricing in lending."* **The one leg that could have made this OW− about lending is the leg the
body-read removed.**

★ **W5 is CONDITIONAL, and that is the finding.** Payments-minus-money-centers RS20 spread =
**11.03pp vs SPY = 2.25× the sector's median move (+4.90)** — **but 0.87×, i.e. below noise, with
PYPL removed.** The 07-23 session version is **0.89pp ex-PYPL, smaller than SPY's own move that day.**
⇒ **The dispersion that survives removing the deal name is the fee/float-vs-balance-sheet split, not
payments-versus-banks. That is the unit this sector should be discussed in.**

**Lead/lag measured and rejected** (266 sessions, SPY-residual, lags ±5): lag-0 dominates in 3 of 4
pairs and every lagged term is ≤ |0.16|. **No sub-group of Financials leads another.**

**Dated**: **MA 07-30 (S14 + S14-ANNEX)** · FOMC 07-29 (S19) · June PCE 07-30 (S15).
**S14's pre-registered baseline, from the filing rather than sell-side**: MA FY2025 **cross-border
volume +15% local currency**, GDV $10.6T +9%, switched transactions 175.5B +10%.

---

## §E · CROSS-SECTOR — the LIVE shortlist, every name resolved

`US_LIVE_SHORTLIST.json` (15 names, `mcap ≥ $10B ∧ 🟢가속 ∧ flow desc top15`). **Every name is either
carried into a section above or explicitly dropped with a reason — none is silently omitted.**

| Ticker | Disposition |
|---|---|
| CSX · UNP | **§B** — the rail node |
| TRV · CB | **§D** — the insurance leg (33.0% of the sector's positive flow) |
| TMO · JNJ · ABBV | **§C** — three of the six mcap-ranked greens |
| XOM | **§A** — the crude control; **RS60 only +2.7 vs SPY**, revisions **0↑:2↓ / 0↑:4↓**, FINRA z +3.13 |
| LMT | Carried as **S7's completed observable** (backlog leg + band leg both fired, +6.10σ on 07-23). **Defense was deep-dived 2026-07-22; not re-opened this run** |
| **URI** | ★ **DROPPED and filed.** GICS *Trading Companies & Distributors* = **construction/industrial capex, not freight**; its +11.35pp vs SPY on 07-23 is its own **07-22 earnings print**. Including it would attribute a construction cash flow to a freight thesis |
| **T** | ★ **DROPPED and filed.** 🟢 reached via **`vol_surge` 1.82 alone**; **RS60 −13.2 vs SPY**; FINRA z **+1.64** |
| **PLTR** | ★ **DROPPED and filed.** flow +0.650 🟢 with **RS60 −17.0 vs SPY** — a 20-day inflection inside a 60-day downtrend, and no DEEP mandate covers it |
| **META** | **NOT dropped, and NOT promoted here.** It is **S16's live observable** (META 🟢 RS20 +8.0 vs SPY against GOOGL 🔴 −8.7 — a 16.7pp intra-industry spread) and **S13's counterparty on 07-29/30**. ⚠ **Both names carry negative RS60 vs SPY (−13.9 / −12.5)** = a 20-day inflection, the weakest admissible A-grade form (C4). **Owned by PREMORTEM/SCENARIOS, not by a BET section** |
| **AAPL** | Not promoted: 🟢 with RS20 +9.1 / RS60 +17.0 vs SPY, but **Info Tech was deliberately NOT given a DEEP slot** and AAPL's own binary (07-31) was **dropped for lack of information content** — neither branch moves a tilt |
| **PM** | Not promoted: Consumer Staples was cut to **N−** this run (wflow −0.159, Δ −0.095, 1🟢/8🔴). A single 🟢 inside a demoted sector with no mandate is a name without a thesis |
| **PYPL** | ★ **DROPPED and filed** — see §D and **D50**. Its +31.2 RS20 vs SPY is an **unaccepted $53B Stripe bid** while estimates are cut **0↑:4↓ next-quarter** and it trades **5.5% above** target |

### §E-1 · Set-aside ledger — four US rows filed this run (**D27 satisfied**)

```
2026-07-24  URI   United Rentals  [K.본문반증]  revives-if: argued on its own construction/industrial-capex
                                                thesis, OR a rail read-across is measured  ·  recheck 2026-10-22
2026-07-24  PYPL  PayPal          [H.밸류소진]  revives-if: the Stripe bid is accepted or lapses AND next-quarter
                                                revision breadth turns non-negative        ·  recheck 2026-08-06
2026-07-24  T     AT&T            [B.모멘텀only] revives-if: RS60 vs SPY turns positive while OBV stays accumulating
                                                                                           ·  recheck 2026-08-21
2026-07-24  PLTR  Palantir        [B.모멘텀only] revives-if: RS60 vs SPY turns positive OR a DEEP mandate covers it
                                                                                           ·  recheck 2026-08-21
```
Ledger now **44 rows · 3 resolved · 21 legacy · 0 due**. ⚠ **All 21 legacy rows remain KR** and carry
into a further HANDOVER unresolved — **named, not waved through** (D42's priority four: 000500, 161890,
008930, 073240).

★ **No name was removed on narrative grounds while its measured flow still passed.** The test case is
**VLO**: it is the **only refiner with analysts cutting its current quarter (6↑/5↓ over 7 days,
7↑/5↓ over 30)** and it prints first — a strong narrative case for setting it aside. **It is kept**,
with conviction lowered and the cut breadth stated, because **RS20 +25.2 / RS60 +24.9 vs SPY and OBV
accumulation all still pass.** That is the 475150 precedent (+41.2pp and +26.9pp lost to
narrative-only rejections) applied deliberately.

---

## §F · Sizing

**None.** This desk produces analytical output only — no position sizing, no buy/sell language, and no
epicenter-starter tickets. **No cycle GAP was flagged** (`CYCLE_EXPOSURE.json`: AI-compute 12.14% ≥
12.0%, Energy 11.33% ≥ 8.0%), so the pre-mortem's starter module is not triggered.
⚠ **But the ✅ is "no gap the registry can see"**, and PREMORTEM Lens 4 measured why that is weaker
than it reads: the AI-compute epicenter bucket spans **95.0pp of RS60 vs SPY** and the book's held
names rank **AVGO 10/10 and NVDA 9/10 — the two worst**; Energy's ✅ is satisfied by **XOM, which ranks
5/6 and is the leg with +2.7pp of 60-day excess** while the excluded refining leg carries +22.9 to
+34.2pp. **Refining exposure, AI-security exposure and memory/storage exposure are each 0%**, and two
of those three are **invisible to the guard because no registry row exists.** Seven registry edits are
proposed to a human in `BLINDSPOT_PREMORTEM.md` §5.

---

---

## §B-ALPHA · Freshness tags — filled by stage 9 (ALPHA), 2026-07-24

> 🟢LIVE / 🟡PARTIAL (residual + **dated re-check**) / 🔴RESOLVED (dropped **and** ledger-logged).
> Evidence label and date on every row. **Tags follow the NAME, not the sector's turn in the rotation**
> — every row below is carried into the next run's inheritance packet **whether or not its sector holds
> a DEEP slot** (measured origin: 006360 carried a tag, INDU rested, and **+12.3% over five sessions went
> untracked**).

| Name | Tag | Evidence label · date | Residual / re-check |
|---|---|---|---|
| **MPC** | 🟡**PARTIAL** | `[measured]` RS20 +26.0 / RS60 **+34.2 vs SPY**, OBV accumulating, settled crack **66.49 = 89th pctile of 90d**, next-Q revisions **+104.2%/90d** · 07-23/24 | **Residual: the crack's RATE is flat (+0.12% WoW, accel −9.09)** while its level is at the top. **Re-check 2026-08-04** (its own print; ±11.2% D28 straddle is usable) |
| **PSX** | 🟡**PARTIAL** | `[measured]` RS20 +22.1 / RS60 +22.9 vs SPY, OBV accumulating, 5 segments incl. a 50% CPChem JV ⇒ crack-beta only **+0.238** · 07-23/24 | **Residual: R8 — it is NOT the cheapest (11.02 vs MPC 10.71), and the human-locked `core_pick` still says it is. Re-check 2026-08-05** |
| **VLO** | 🟡**PARTIAL, conviction lowered** | `[measured]` RS20 +25.2 / RS60 +24.9 vs SPY, OBV accumulating, **crack-beta +0.836 = the crack instrument** · 07-23/24 | ⚠ **Residual: the ONLY refiner being cut (6↑/5↓ 7d, 7↑/5↓ 30d), current-Q increment 0.00 for two runs, and it prints FIRST. Re-check 2026-07-30** — kept deliberately because the measured axes still pass (the 475150 precedent) |
| **XOM** | 🟡**PARTIAL · momentum-only flag NOT stamped** | `[measured]` 🟢가속 but **RS60 only +2.7 vs SPY**; revisions **0↑:2↓ (7d) / 0↑:4↓ (30d)** — cut on both quarters; crack correlation **+0.078 = indistinguishable from zero** · 07-23/24 | **Residual: it is the CONTROL, not a refining expression.** FINRA z +3.13 is **demoted to a baseline note**, not read as positioning. **Re-check 2026-07-31** |
| **CSX · UNP · NSC** | 🟡**PARTIAL** | `[measured]` flow +0.878 / +0.867 / +0.767 (CSX & UNP at the **99.3rd / 99.0th percentile of all 300**), both RS windows positive vs SPY, FINRA **clean-rise** · 07-23 | ⚠⚠ **Residual: the flow IS the earnings event** (8-Ks 07-22/07-23, correction C-B), **and ~8 of UNP's 12 revenue growth points are fuel surcharge** ⇒ this is the Energy bet again, not a diversifier. **Re-check 2026-07-28 (S20)** |
| **TMO** | 🟢**LIVE** | `[measured]` **+8.71% = +9.95pp vs SPY = +5.64σ on its own 07-23 Q2 beat + raise**, `new_green`, next-quarter breadth **15↑:2↓ — best in the sector**, FINRA z −1.33 clean-rise · 07-23/24 | **The one row in this run where narrative, flow, revisions and a dated primary cause all point the same way.** Re-check 2026-08-06 (does RS20 vs SPY hold past the print day, or was it `n≈1`) |
| **UNH** | 🟢**LIVE** | `[measured]` **post-print raise on 2026-07-16** (adj EPS $6.38 vs $4.90 exp; MBR 86.7% vs 88.5% exp; FY guide raised to $19.50–20.00), **next-year 8↑:0↓**, CY EPS **+9.8%/90d**, **+12.5% to target — the largest in the sector** · 07-16/24 | ⚠ It is the one 🟢 that **LOST** to SPY on 07-23 (−0.56pp) — the best revision book is the name the flow did not buy. Re-check 2026-08-06 |
| **MRK** | 🟡**PARTIAL** | `[measured]` flow +0.615 🟢 with RS20 +7.5 / RS60 +15.2 vs SPY; **the −46.0% CY revision is an acquired-IPR&D charge artifact** — Terns ~$5.8B ÷ 2.4698B sh = **$2.35/sh against a −$2.34/sh consensus swing, a 0.4% match** · 07-24 | **Residual: the charge sizes are `[news]`-grade, not `[primary]`. Re-check 2026-08-04** (the 10-Q/8-K promotes or retracts the verdict). Separately: **Keytruda is 48.7% of FY2025 sales — a charge verdict is not an LOE verdict** |
| **LLY · JNJ · ABBV** | 🟡**PARTIAL** | `[measured]` all 🟢 with positive RS20 and RS60 vs SPY; **LLY has the only name-specific narrative** (Novo PI motion 07-24, **advertising channel only**) · 07-23/24 | ⚠ **Residual: all three are top-6-by-market-cap members of a 🟢 set that IS the mcap ranking.** **ABBV's far book is being cut (1↑:4↓ 30d, 0↑:5↓ 7d) — re-check 2026-07-31.** LLY/JNJ re-check 2026-08-06 |
| **MA · V** | 🟡**PARTIAL** | `[measured]` both 🟢; **MA +21.0% to target (largest in FIN)**, **V CY breadth 7↑:0↓**; MA FY2025 cross-border **+15% local currency** pre-registered as S14's baseline · 07-24 | **Residual: S14's own observable is contaminated by PYPL (D50); the {MA,V}-only reading is pre-registered.** ⚠ MA's two C-grade OBV sources **disagree on the same day** (chart 분배 −22% vs JSON 매집) — **D43; neither may override RS20 +6.6 / RS60 +1.5 vs SPY**. **Re-check 2026-08-06** |
| **TRV · CB** | 🟡**PARTIAL** | `[measured]` the sector's #1 and #5 flow, insurance = **33.0% of Financials' gross positive flow**, 11 of 12 insurers positive on RS60 vs SPY · 07-23 | ⚠ **Residual: the constraint is quantified by a named CEO** — Chubb's Greenberg: **NA commercial rate −1.4%, property −6%, premiums −2.3%**, *"zero evidence across the industry that loss costs have abated."* **TRV also trades 7.8% ABOVE target on a +21.1%/90d book that moved almost entirely in the last 7 days.** Re-check 2026-07-31 |
| **JPM** | 🟡**PARTIAL** | `[measured]` flow +0.576 🟢, RS20 +4.3 / RS60 +9.1 vs SPY — **the money-center green that SWEEP §3 and ROTATION §3 both said did not exist** (top-15 truncation artifact) · 07-23 | **Residual: the bank bucket has no volume leg** — the CRE headline was body-refuted (BankUnited **cut** FY core loan growth to 4–5%). **Re-check 2026-08-08** |
| **GS** | 🟡**PARTIAL** | `[measured]` **the sector's best revision book — CY EPS +19.5%/90d on 9↑:0↓ both years, 8↑:0↓ current quarter** — attached to flow −0.062 and RS20 −0.9 vs SPY (RS60 **+11.4**) · 07-24 | **Residual: the de-rate-against-an-activity-peak read is unchanged on fresh numbers. Re-check 2026-08-06** |
| **Exchanges & data** (NDAQ · SPGI · ICE · CME · MCO · MSCI · COIN) | 🟡**PARTIAL — newly surfaced** | `[measured]` **the sector's highest mean flow (+0.487), and it was invisible in every prior pass** (buried in a 17-name residual); **6 of 7 positive on RS20 vs SPY, 7 of 7 NEGATIVE on RS60** · 07-23 | ⚠ **Residual: a 20-day inflection inside a 60-day downtrend — the weakest admissible A-grade form (C4)** — with a named cause on **both** signs (NDAQ's record Q2 vs the CFTC/Kalshi-Coinbase perps de-rate). **Confirm = ≥3 of 7 cross to positive RS60 vs SPY by 2026-08-08; falsify = ≥4 roll to negative RS20** |
| **STNG** | 🟡**PARTIAL** (on the ledger, `A.flow미도착`) | `[measured]` RS20 +5.8 / RS60 −4.8 vs SPY, news velocity **0.00×**, short **5.4% float BUILDING**; ★ **one of only two usable straddles on the board (±10.0%, D28)** · 07-24 | **Residual: S21 prints 2026-07-30.** Ledger recheck **2026-08-06** |
| **HUM** | 🔴**RESOLVED — already dropped and ledger-logged 2026-07-23** (`H.밸류소진`, recheck 07-31) | PREMORTEM Lens 3 re-tagged **EXHAUSTED**: next-quarter consensus **−0.14 from +0.50 (−128.2%)**, **+13.4% above mean target — the only top-10 RS60 name above it** · 07-24 | Prints **2026-07-29**. **Not re-filed** (the row exists); carried so it cannot re-enter as "the highest-momentum health-care name" |
| **URI · PYPL · T · PLTR** | 🔴**RESOLVED — dropped and filed this run** | see §E-1 for each row's class, `--revives-if` and `--recheck-date` | **All four have expiries. None is a permanent ban** |

### ⚠ Momentum-only and positioning flags

- **Stamped momentum-only (hard-stop required if ever acted on): T and PLTR** — both reached 🟢 with
  **negative RS60 vs SPY** (−13.2 / −17.0), i.e. a 20-day tape move inside a 60-day downtrend. Both are
  now 🔴 and filed.
- **NOT stamped, and the distinction is the point (rule D6): MU, AMAT, LRCX, KLAC, SNDK, STX, HPE.**
  Their 🔴/🟡 tags come from **OBV, a C-grade signal with r≈0.49 vs real flow and no leading power
  (t = 1.00)**, disagreeing with **positive RS60 vs SPY (+11.9 to +100.2)**, which is A-grade.
  **A C-grade disagreement downgrades to 🟡 and is reported as a disagreement — it does not convert a
  bet into a tape trade.** 10 of Information Technology's 26 reds are exactly this shape, so the sector's
  red count **overstates by ~38%** at the grade the signals were measured at.
- **US positioning gate**: **⚡crowded-short is turn-conditional squeeze fuel, never a standalone
  reason.** ★ And this run **demoted the instrument itself**: MPC and PSX printed the **identical 36.4%**
  short-volume share on the identical day and scored **z −3.29 vs −0.25** purely on their own baselines
  (MPC's 53.9–57.1%, chronically 10–13pp above the tool's stated 40–45% band). **FINRA z is a baseline
  note this run, not a positioning read.**

### Carry-forward list (independent of next run's DEEP rotation)

**MPC · PSX · VLO · XOM · CSX · UNP · NSC · TMO · UNH · MRK · LLY · JNJ · ABBV · MA · V · TRV · CB ·
JPM · GS · STNG · the 7-name exchanges-&-data bucket** — 26 names, each with the dated re-check above.
**HUM · URI · PYPL · T · PLTR** are carried on the reject ledger with their own revival conditions.

## ✅ EXIT CHECK

- [x] **Every DEEP sector has a section** (§A Energy · §B Industrials-rail · §C Health Care · §D
      Financials), and **every cross-sector LIVE-shortlist name is resolved in §E** — carried, or
      dropped with a stated reason. **None silently omitted.**
- [x] **Numbers cross-checked; blanks are blanks.** Named tool gaps: `margin_history.py VLO` (no annual
      data), VLO's Item 1A returns empty from `module_business_us`, MA/V Item 1A likewise empty, CME's
      Q2 body returns 0 matches, no EIA module. **No figure was guessed to fill any of them.**
- [x] **Flow/positioning cross-read per candidate**; `BET_SHEET.md` written as **ONE file**.
- [x] **Four US set-aside rows filed with a class, a `--revives-if` and a `--recheck-date`**
      (script-enforced) — **D27's "≥1 US row per run" satisfied for the second consecutive run.**
- [x] **No name removed on narrative grounds alone while its measured flow passed** — VLO is the
      explicit test case and is kept with lowered conviction.
- [x] Linter run on this file (result in the run log).
- [x] **Zero sizing, zero buy/sell language.**

> ✅ → ALPHA.
