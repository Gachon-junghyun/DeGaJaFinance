# BET_SHEET — industry_US — 2026-08-05 (Wed) · ONE file, per-sector sections

> Downstream desks glob this exact filename. Never split.
> All flow/RS **`asof 2026-08-04 settled`**, benchmark **SPY** inline (C1). Valuation from
> `module_fundamentals_us`. **Zero buy/sell recommendations, zero position sizing (P4).**
> §B freshness tags are placeholders — **ALPHA fills them.**

## 0 · ⚠⚠ The sheet's governing constraints, stated before any name

1. **Exposure state is `방어`** (`exposure_rule.py state`, 2026-08-05 settled): target invested
   **55%**, ledger row **71.1%**, band gap **🚨 +16.1pp OVER-invested.** Per the L3 unit, `방어` means
   **narrow new entry and prioritise holding what exists.** ⇒ **this sheet is deliberately narrow,
   and the reason is the rule, not a shortage of candidates.**
   ⚠⚠ **W1: that is the KR book's rule on a KR benchmark (`069500.KS`). It is NOT a US sizing input
   and no line below is sized off it.** It is quoted because the EXIT CHECK requires the sheet's
   language to be consistent with the carried state — and here the state says *fewer*, not *more*,
   which is the opposite of the `복귀` case where an unfillable target silently leaves cash idle.
2. **The green gate censors this board.** `SWEEP_READ §3` and `BLINDSPOT_PREMORTEM §3b` measured the
   same defect by two independent methods: **VLO · MPC · PSX · ANET all carry OBV 매집 *and* RS20 > 0
   vs SPY *and* a positive days-21-60 segment, and are tagged 🟡 purely because `vol_surge` < 1.2.**
   ⇒ **a 🟡 tag on this sheet is not evidence against a name.**
3. **Conversely, `SECTOR_FLOW`'s 🟢 is a 3-axis conjunction that includes `vol_surge`**, whose IC
   cleared Bonferroni **negative** on the KR ledger this morning (**D161**). **W1 — the KR kill does
   not transfer to the US board** (US ledger: +0.0267, t +1.36, `구분 불가`). **No 🟢 is quoted below
   without its axis decomposition.**

---

## §ENRG — Energy (DEEP continuous · OW−)

**DEEP verdict carried**: the −12.3%/2-session crude move is **war-premium deflation, not demand** —
08-04 WTI **−5.69%** with **both cracks flat** = S8 branch B's signature. **The OW− was never priced
on the crude level.** Crack **level 82.591 = 92.1st percentile of trailing 252**, while the **5-day
rate is −12.487** and the **21d/63d rates are +12.608 / +17.937** (C2 — all halves quoted).

### §A · Numbers

| | **MPC** | **PSX** | **VLO** | XOM |
|---|---|---|---|---|
| Forward P/E | **11.15** | **10.78** | **11.12** | — |
| PEG | 1.57 | 1.23 | **4.08** | — |
| Trailing EPS | $28.85 | $10.13 | $23.56 | — |
| Forward EPS | **$27.77** | **$18.98** | **$27.72** | — |
| **Forward ÷ trailing** | **0.96× — consensus expects earnings to FALL** | **1.87× — nearly double** | 1.18× | — |
| Revision breadth, next Q (30d) | **12↑ / 1↓** | **12↑ / 1↓** | 11↑ / 2↓ | — |

★★ **The three refiners' consensus disagrees with itself, and that IS the finding (C2/lens B2).**
**MPC is being upgraded 12:1 toward a forward number that is still BELOW its trailing EPS**, while
**PSX is being upgraded 12:1 toward a number 1.87× trailing.** ⇒ **the same 12:1 breadth means
opposite things at the two names.** **A revision count without its level is not information.**
⚠ **`margin_history` returns blank on all three** (M233, 61%-failure class) ⇒ **no cheapness claim is
made on any of them.** A forward multiple without a margin percentile is not a valuation.

### §B · Thesis · freshness `[ALPHA fills]`

- **MPC** — Q2 printed 08-04: adj EBITDA **$8.5bn**, R&M adj EBITDA/bbl **$24.84**, refining margin
  **$36.33/bbl vs $17.58 YoY**, **capture 112% of benchmark (1H 108%)** on advantaged crude sourcing,
  yield optimisation and *"strict inventory discipline in a **backwardated** market"*. Management
  guides **"an elevated mid-cycle environment through end-2026 into 2027, on tight global product
  supplies."** ⚠⚠ **And Q2 covers April–June — a window that CLOSED ~5 weeks before the crack move
  this desk is adjudicating.** **The print's information content about TODAY is near zero, and that
  is stated rather than smoothed.** `[thesis: refining-margin capture, not crude level]`
- **PSX** — printed pre-market 08-05: adj EPS **$9.41** beat, adj EBITDA **$5.891bn**, **realised
  margin $24.08/bbl vs $11.25 YoY**, operating cash flow **$7.259bn**, total debt **−$6.6bn**.
  ⚠ **Earnings call 12:00 ET — AFTER this stage.** `[thesis: same node, cleaner balance sheet]`
- **VLO** — no print in window. **Strongest days-21-60 segment of the three (+10.4 vs SPY)** ⇒ the
  only one of the three whose 60-day excess is not front-loaded into the last 20 sessions.
- **XOM** — ⚠ **days-21-60 segment −5.5 ⇒ TURN-OFF-A-HOLE, not a run** (Lens 3). And **S31 reads
  RS20 +5.5, between its own two branches ⇒ structurally `AMBIGUOUS`.**

### §C · Flow / positioning `asof 2026-08-04 settled`

| | flow_score | OBV | RS20 | RS60 | seg 21-60 | surge | tag |
|---|---|---|---|---|---|---|---|
| MPC | +0.589 | 매집 +0.369 | **+14.2** | **+23.6** | **+7.7** | 0.86 | 🟡 **(censored)** |
| VLO | +0.628 | 매집 +0.222 | +12.8 | **+25.2** | **+10.4** | 0.93 | 🟡 **(censored)** |
| PSX | +0.656 | 매집 +0.195 | +12.0 | +16.9 | +4.1 | 0.98 | 🟡 **(censored)** |
| XOM | +0.496 | 매집 +0.173 | +5.5 | −0.4 | **−5.5** | 0.88 | 🟡 |

**PSX positioning, re-pulled today**: **short 2.3% of float, `covering`, DTC 2.6 · options P/C 0.26
(call-dominant) · skew +11.6 · implied move ±4.5% (expiry 08-07, D2).**
🚨 **This is a REVERSAL of S53's registration state.** At registration PSX carried **P/C 1.25 — "the
only fear profile on the desk's pull" — plus FINRA short z +1.53, "the only 🔴 short surge."**
⇒ **S53's registered note *"if branch B fires anywhere in this duo, PSX is the name already
positioned for it"* is VOID by positioning change.** **The bearish setup unwound before the print.**

### §D · Competition / peers — sub-sector dispersion (W5)

**Refining > integrated > E&P > services > midstream**, and the spread is larger than the sector's
own move: on 08-04 **WTI −5.69%, XLE −0.46%, XOP −1.34%, OIH +2.62%** — **a 3.96pp intraday spread
inside one label on one day.** Midstream is the sector's only outright red bucket (**KMI −0.422,
OKE −0.493 — OBV 분산 on both, quoted with their RS20 vs SPY of −6.6 and −6.5 so the OBV leg does not
carry the claim alone, RULE D6**). ⇒ **"Energy" is the wrong unit; the tiers must be quoted separately.**

### §E · Refutation + dated catalyst

- **Kills the refining leg**: **S55 branch A** — HO% − CL% ≤ **−3.0pp** over 08-04 → **08-11** ⇒ the
  distillate weakens independently of crude and the OW− loses its refining leg structurally.
  **Current running value: +2.94pp on the 08-04 single session = branch B's direction.**
- **Kills the war-premium reading**: **S52 branch A** — a **dated** Strait-reopening term in a
  **primary** text by **08-06**. **Not fired today** (CENTCOM's "free and open" describes the
  *southern route under escort*; Bessent's date attaches to the *deal*).
- **A non-Hormuz supply falsifier, checked and REJECTED as insufficient**: *"Russia's Oil Exports
  Slip as Lull in Drone Strikes Boosts Refining"* [bloomberg 08-04] — **DEEP-ENRG adjudicated this
  does NOT clear S55's VOID bar**: title-only/single-source, describes *tempo* not a **dated regime
  change**, and is contradicted the next day by fresh strike headlines. **Named and refused, not
  used.**
- **Dates**: **S31 today · S53 today (PSX call 12:00 ET) · S52 08-06 · S55 08-11 · S60 08-11 ·
  S61 08-12.**

---

## §INDU — Industrials (DEEP continuous · promoted N → OW− this run)

### 🚨 §0 · The sheet must lead with the promotion's own refutation

**ROTATION promoted INDU on breadth carried by ETN · EMR · AME · PWR. Three independent measurements
now argue that promotion is a 20-day repair, not a cycle ignition:**

1. **PREMORTEM Lens 3 — days-21-60 segment vs SPY is NEGATIVE on all four**: EMR **−4.5** ·
   ETN **−3.1** · AME **−3.5** · PWR **−14.7**. DEEP-INDU reproduced these independently.
2. **DEEP-INDU's cross-node split** — on the same theme and date, **ETN/EMR/AME accumulate while
   GEV (turbines) is 🔴분산 and VRT (data-centre integration) carries RS20 −14.8 / RS60 −26.0 on the
   board's 3rd-highest volume surge (1.87).** **A chain-wide ignition does not look like that.**
3. ★★★ **NEW HERE — the estimate table contradicts the tape on two of the three carriers**:

| | Forward P/E | PEG | Fwd ÷ trailing EPS | **Revision breadth, next Q (30d)** |
|---|---|---|---|---|
| **ETN** | 28.19 | 3.13 | 1.56× | **5↑ / 2↓** — positive |
| **EMR** | 22.69 | 2.09 | 1.58× | 🚨 **0↑ / 2↓** — **zero upgrades, net downgrades** |
| **AME** | 28.29 | 3.13 | 1.32× | 🚨 **0↑ / 1↓** — **zero upgrades** |

⇒ **EMR carries the cluster's LARGEST OBV accumulation (+0.631) and a NEW-🟢 tag while consensus has
made zero upward revisions to its next quarter in 30 days.** **AME the same.** ⚠ **Revisions turn
before price does** — a tape accumulating into a flat-to-down estimate line is the shape the desk's
own carry rule flags, and **it is the third independent reason not to call this an ignition today.**

### §A/§C · Numbers + flow `asof 2026-08-04 settled`

| | flow | OBV | RS20 | RS60 | seg 21-60 | surge | FINRA z | tag |
|---|---|---|---|---|---|---|---|---|
| ETN | +0.978 | 매집 +0.274 | +9.2 | +6.0 | −3.1 | 1.56 | +0.14 | 🟢 (3-axis) |
| EMR | +0.867 | 매집 +0.631 | +12.0 | +7.1 | −4.5 | 1.36 | +0.34 | 🟢 (3-axis) · NEW |
| AME | +0.788 | 매집 +0.215 | +6.5 | +2.8 | −3.5 | 1.33 | −0.46 | 🟢 (3-axis) · NEW |
| PWR | +0.654 | 매집 +0.138 | +2.4 | **−13.1** | **−14.7** | 1.48 | −0.34 | 🟢 · NEW |
| TRI | +0.944 | 매집 +0.230 | +17.1 | +11.5 | −5.0 | 1.50 | +1.39 | 🟢 |
| — | — | — | — | — | — | — | — | — |
| ROK | +0.183 | 매집 | −8.2 | −6.2 | — | 1.54 | — | 🟡 |
| VRT | +0.019 | 중립 | **−14.8** | **−26.0** | — | **1.87** | — | 🟡 |
| GEV | −0.681 | 분산 | −8.6 | −8.0 | — | 0.88 | — | 🔴 |

### §B · Thesis `[ALPHA fills freshness]`
**Value chain (DEEP-INDU, primary-anchored)**: generation (GEV) → grid (PWR) → **switchgear &
distribution (ETN)** → automation (EMR · ROK · AME) → DC integration (VRT) → the compute load.
**BINDING CONSTRAINT = switchgear/transformer manufacturing capacity, not demand** — anchored on
**GEV's own filing** (*"customer lead-times have increased as a result of demand outstripping
supply"* in Grid Solutions) and **ETN's three 2025-26 acquisitions (Resilient, Fibrebond, Boyd
Thermal), all buying capacity at that same node.** ★ **The accumulating names sit at the constrained
node; the nodes on either side of it are both distributing.**

### §D · Peers / screener setups (wide net, `us_setup_screener --sector Industrials`)
**Leader pullback**: WM (RSI 22.1) · GWW (31.6) · ODFL (30.8) · UPS (34.5) · CARR (42.0) · FDX (44.6).
**De-rate snapback**: UBER (35.0, px/200 −13%). **Washout**: RSG (RSI 17.5).
⚠ **None carries a DEEP thesis and none is handed forward.** **CARR** is the only one adjacent to the
electrical/HVAC chain and it is logged, not adopted.

### §E · Refutation + dated catalyst
**S62 settles 2026-08-07** on (median RS20 of {EMR,ETN,AME,PWR}) − XLU RS20 · **branch A ≤ −5.9pp**
(the tilt is one bet with UTIL and must be sized as one) · **branch B ≥ +7.4pp** · **currently
+14.51pp.** ★ **Both DEEP-INDU and DEEP-UTIL independently deferred their central question to this
same bracket** — which is what a registered falsifier is for.
**Second falsifier**: **EMR or AME printing a first upward next-quarter revision** would remove the
§0 item 3 objection; **a second name turning OBV 분산 with RS20 ≤ 0 vs SPY** would confirm it.

---

## §IT — Information Technology (DEEP rotating · N)

### §A · Numbers

| | **LITE** | **ANET** |
|---|---|---|
| Forward P/E | 45.95 | 40.34 |
| PEG | **0.63** | 2.30 |
| Trailing EPS | $5.69 | $2.91 |
| Forward EPS | **$18.73 = 3.29× trailing** | $4.84 = 1.66× |
| Revision breadth, next Q (30d) | 2↑ / 0↓ (**n small**) | 1↑ / 1↓ |

⚠⚠ **LITE's PEG 0.63 is the exact B2 shape the desk logged on MET**: *"a low multiple whose
denominator is racing upward is consensus CHASING, not cheapness."* **Forward EPS is 3.29× trailing.**
⚠ **`margin_history` is not a field `module_fundamentals_us` returns at all** — DEEP-IT checked the
raw `--json` for both names. ⇒ **no cheapness or richness claim is made on either (M233).**

### §B · Thesis + the re-grade this sheet is obliged to carry

**DEEP-IT's answer to the sector question: NEITHER the +5.13pp XLK excess NOR the 0.05 breadth is
"the sector."** The best-to-worst sub-industry spread is **13.4pp**, which is **2.6× XLK's own 5-day
excess** ⇒ **the GICS label is the wrong unit (W5).** **Semiconductors is the board's worst
sub-industry: median RS20 −7.7, median RS60 −9.2, 0🟢 / 8🔴 of 14.**

🚨 **EVENT_ALPHA Card 1's `CONFIRMED-EARLY` hand-off on LITE is RE-GRADED to `EARLY, NOT YET
CONFIRMED`** — **DEEP-IT's reason: LITE's RS20 +18.4 sits on a days-21-60 hole of −23.9pp (the worst
in Lens 3's whole set), and the card's own registered KPI (RS60 crossing above 0) is unmet at −10.3.**
**A stage re-grading a hand-off from an earlier stage of the same run, on a measurement that earlier
stage did not have.**

### §C · Flow `asof 2026-08-04 settled`
LITE 🟡 +0.694 · 매집 +0.215 · **+18.4 / −10.3** · surge 1.05 · **FINRA z −0.12** ·
ANET 🟡 +0.728 · 매집 +0.309 · **+11.3 / +29.0 · seg +15.2** · surge **1.11 (misses the gate by
0.09)** · **z −1.45 (clean)** · CSCO 🟡 +0.532 · 매집 · +5.7 / +26.7 · COHR 🟡 +0.330 · 매집 ·
−0.1 / −4.0 · **CIEN 🔴분산 −0.538 · −5.0 / −29.1.**

★ **ANET is the cleanest name on this sheet by construction**: **both windows positive, a positive
segment (+15.2 vs SPY), a clean short reading (z −1.45), with OBV 매집 as the fourth leg rather than
the first (RULE D6) — and it is 🟡 only because `vol_surge` missed 1.2 by 0.09.** ⚠ **Forward P/E 40.34 with PEG 2.30 and no margin percentile available.**

### §D · Peers / screener (`--sector "Information Technology"`) — **AAPL · ASML · APP.**
⚠ **TSM is absent from `us_top300` entirely** — DEEP-IT flags the foundry/logic node as **a real
measurement gap, not a resolved constraint.** **It is a held book name with no flow axis (M252).**

### §E · Refutation + dated catalyst
**S30 settles on today's close** — median RS20 {STX, MU, WDC} = **−1.0 on the 08-04 bar, 1.0pp from
flipping.** ★★ **Its registered control pair (DELL +8.8/+97.5, HPE +17.4/+71.0) has ALREADY turned**,
so by S30's own logic **a branch-A flip today reads as an IT-BETA event, not a memory event.**
**Pre-committed here so no later stage can claim a memory call it did not make.**
**S50 settles 08-06**: **AMD beat with record revenue and an upbeat outlook and the stock sold off.**
**S50 was written asymmetric ("only the CUT branch changes a conclusion") ⇒ a beat-and-sell-off
leaves the bracket formally UNCHANGED while flow independently re-tags AMD DECAYING-STOCK
(RS20 −2.7, seg +24.2, OBV 중립, FINRA z +0.09).** ⇒ **a structural blind spot in the bracket, named
rather than treated as an error.** **S48 (optical layer) settles 09-30 and now has its first live
news driver.** ⚠ **The DRAM QoQ second-derivative source is ABSENT this run** — DEEP-IT declined to
re-assert the carried 07-31 TrendForce figures. **Stated as missing, not carried.**

---

## §UTIL — Utilities (DEEP rotating · UW)

### §A/§C · Numbers + flow
**Sector: wflow −0.353 · eqflow −0.349 · 🟢 0 of 15 · 🔴 10 of 15 · breadth 0.00 · XLU exc5 vs SPY
−7.21 · exc20 −6.64.** ⚠ **The four names with the HIGHEST `vol_surge` (PEG 1.32 · VST 1.30 ·
DUK 1.26 · SO 1.25) are ALL 🔴분산 with OBV 분산 and RS20 ≤ 0 vs SPY** — high volume goes with
distribution here, which is the same direction the KR IC ledger measured on `vol_surge` and is
recorded as corroboration, not proof (D6 · S1).

### §B/§E · The two bracket verdicts, pre-committed on the 08-04 settled bar

| | Registration | **08-04 settled** | Heading to |
|---|---|---|---|
| **S35** regulated median RS20 vs SPY | −3.2 (seven) | **−7.3 (seven) · −8.0 (R40-corrected SIX)** | **branch B** |
| **S47** spread reg − AI-power | **+14.74pp** | **+2.6pp (seven) · +1.9pp (SIX)** | **branch B already satisfied (≤ +7.0)** |

🚨 **DEEP-UTIL's answer to (A): S35 does NOT survive R40** — on the six-name basket the median is
**−8.0, WORSE than the contaminated seven's −7.3**, and the desk's own **S35-ANNEX** shows the
earlier **"FIRED-A" reading (07-29, +0.39 on the seven) was a basket artifact: recomputed on the six
it reads −0.99 and never crossed zero.** ⇒ **a prior verdict on this bracket rested on the
contaminated name.**
⚠ **S47's branch B is weak confirmation**: S35-ANNEX's own 40-session distribution makes **branch B
the ~70% base rate.**

★★★ **The synthesis, argued both ways and DEFERRED rather than decided** — *"S47's branch B may be
firing precisely BECAUSE the AI-power money left the Utilities label altogether for Industrials
electrical equipment; the label became defensible by both halves getting equally bad."*
**For it**: XLU worst on the board on both axes; ETN/EMR/AME accumulating.
**Against it**: DEEP-UTIL confirmed via primary filings (`module_disclosure_us` on **SO** and **AEP**:
**zero rate-case or regulatory-order 8-Ks in 90 days**) that **the regulated leg has an INDEPENDENT
duration mechanism** — its weakness is rate-driven, not a rotation artifact; and INDU's carriers are
Lens-3 repairs, not fresh inflow.
⇒ **Deferred to `S62`, 2026-08-07.** ★ **DEEP-INDU and DEEP-UTIL reached that deferral
independently.**

### §D · Contamination notice (S14-ANNEX / S33-ANNEX style — **S35 and S47 are NOT re-frozen**)
🚨 **CEG prints 2026-08-06 and VST prints 2026-08-07 — the exact settle date — and both are members
of S47's AI-power leg.** ⇒ **S47's spread will be measured on a leg with an earnings event inside its
own settlement window.** **Recorded as a reading caveat. Neither bracket's threshold is moved.**
**Invalidation for both: HY OAS ≥ 3.10 on a close — currently 2.78, a 32bp buffer.**

### §D-2 · Screener (`--sector Utilities`) — D · ED · ETR · AEP · SO · VST · **SRE (RSI 25.2) ·
PEG (RSI 27.5, at its 52-week low)**. ⚠ **All are washout/pullback setups inside the board's worst
sector with no thesis. Logged, none adopted.**

---

## §HLTH — Health Care (★ PREMORTEM-PROMOTED 5th slot · UW)

### §B · The promotion under test — and BOTH things are true at once

**C7's raw green-count observable reads 1 today, unambiguous under BOTH competing top-6 definitions
(a genuine first for this bracket).** ⚠⚠ **And C7's OWN second registered anti-signal FIRED today:
XLV's 5-day excess vs SPY is −7.20 while SPY rose 4.11% over the same 5 sessions** — verbatim the
condition the 07-30 file wrote as its trigger for *"this was defensive rotation, not sector demand."*
⇒ **The promotion survives only on the LETTER of the rule.** Recorded as such.

★ **And the observable's substance rotated entirely**: **HCA — the name C7's 07-30 positive read hung
on — has reversed hard (flow −0.572, RS20 −8.4, RS60 −12.0, both windows negative = a genuine decline,
not a repair)** and has been **replaced in the count by BMY, a name this desk rejected 24 hours ago.**

### §A · Numbers — BMY
**Forward P/E 9.77 · PEG 2.51 · trailing EPS $4.55 → forward $6.54 (1.44×) · revision breadth next Q
30d 12↑ / 1↓ but current-year 12↑ / 6↓** (C2 — both, and they disagree).
★ **`margin_history` IS runnable on BMY — contra the 07-30 file's sector-wide "unrunnable" claim.**
**FY2025 gross margin 71.1% ≈ 25th percentile of its own 19-year range** ⇒ **the sub-10× forward
multiple is a MODERATE cheapness signal, not a clean one** (the denominator is not at a peak, but the
margin is not depressed either). **TMO's series remains truncated at FY2017 — the 07-30 finding holds
for TMO specifically, and no cheapness claim is made there.**

### §C · Flow + cause-check
**BMY 🟢가속 · OBV 매집 +0.527 · RS20 +10.5 / RS60 +11.7 · seg 21-60 +0.9 · surge 1.52 ·
FINRA z −2.50 (the board's cleanest clean-rise).**
**Cause, graded**: **B-grade** — a **primary 07-30 8-K earnings beat drove +10.4% of the run before
any M&A headline existed.** **C-grade** — the *"AstraZeneca–BMY megadeal"* story is **talk only**:
`module_disclosure_us BMY` returns an **empty M&A/contract category**; the coverage is CNBC and
SeekingAlpha citing an FT report, **not company disclosure.** **M&A TALK IS NOT AN M&A EVENT.**
⚠ **BMY's segment is +0.9 — razor-thin.** The reject ledger recorded **−1.3** on the same date ⇒
**a sign flip inside one session on the measurement that separates a run from a repair.**

### §D · Sub-sector dispersion (W5) + screener
**Every Health Care industry bucket is negative except the one BMY-driven pharma group — and strip
BMY out and pharma is negative too (−0.140).** ⇒ **the "sector" is one name.**
Screener (`--sector "Health Care"`): CVS · HUM · UNH · ABBV · GILD · ALNY · ISRG. **None adopted.**

### §E · Refutation + dated catalyst
**C7's second observable is due 2026-08-06 — tomorrow.** Its registered anti-signal (the
outside-top-6 🟢 count returning to 0) is the kill. **Already-live counter-signal: XLV exc5 −7.20 on
a rising SPY.**
⚠⚠ **BMY's `revives_if` conditions in the rejection ledger appear ALREADY MET, two weeks before its
scheduled 2026-08-18 recheck. NO LEDGER ROW WAS RESOLVED** — resolving it here would be firing a
revival on one session's flow, the exact overreaction the ledger exists to prevent. **The tension is
reported and handed to the next HANDOVER's `due` audit.**

---

## §LIVE — cross-sector shortlist names (outside the DEEP sectors)

`US_LIVE_SHORTLIST.json` carries 13. Those inside a DEEP sector are covered above. The rest:

| Ticker | Sector | Flow `asof 08-04` | seg 21-60 | Disposition |
|---|---|---|---|---|
| **GRMN** | DISC | +0.987 (board #1) · 매집 · **+20.4 / +21.6** · surge 1.78 · z −0.15 | **+0.6** | **Set aside** — Lens 1 declined it: **79% of the 20-day excess is ONE session (07-29)**, no dated catalyst, and its own recheck is **08-18**, outside the window. **Declining the board's #1 flow score on a stated rule.** |
| **MSFT** | IT | +0.972 · 매집 +0.443 · **+23.6 / +11.7** · surge 1.55 · **z +2.44 crowded-short** | **−9.8** | **Set aside** — TURN-OFF-A-HOLE. The RS20 reads like acceleration; the prior 40 sessions were **−9.8 vs SPY**. |
| **PLTR** | IT | +0.967 · 매집 · +17.9 / +13.3 · **z −1.40 clean** | −4.2 | **Set aside** — the 1-day move was **+29.5% ≈ 4× its own 20-day sigma (7.27%)**, i.e. an earnings gap. **n = 1; the tag needs 2–3 more settled sessions.** |
| **KKR** | FIN | +0.783 · 매집 +0.502 · +10.6 / +2.4 · NEW-🟢 | −7.4 | **Set aside** — Lens 1's WITHIN-RUN-WATCH; **RS60 flips to −0.2 intraday**, the 60-day leg is not robust to one session. Decisive measurement = **HY OAS buffer at S26's 08-12 settle**. |
| **IRM** | RE | +0.726 · 매집 +0.360 · +5.3 / **−6.5** · NEW-🟢 | −10.9 | **Set aside** — RS60 negative; RE is the board's **worst day-over-day deceleration (Δ −0.246)**. |
| **FTNT** | IT | +0.643 · 매집 · **+2.9 / +50.4** · **z +2.07 crowded-short** | **+44.8** | **Re-filed, not dropped** — a genuine two-window run that is **decelerating** (weakest RS20 of the greens). New thesis line: *decaying 60-day excess, not a fresh ignition.* Dated re-check **08-19**. |
| **MET** | FIN | +0.435 · 매집 **+0.087 (barely above the 0.08 gate)** · +1.7 / +16.5 | **+14.1** | **Held name, bracketed by S58 (settles 08-11).** ⚠ **MET is on `_US_STOP` (M152)** — a zero-coverage reading on it is **uninformative, not evidence**, and S58's scoring must not read silence as signal. Largest single-day flow_score drop of the greens (−0.309). |
| **TRI** | INDU | +0.944 · 매집 · +17.1 / +11.5 · **z +1.39** | −5.0 | Covered in §INDU. TURN-OFF-A-HOLE. |

## §EPICENTER-STARTER — the cycle GAP module

🚨 **`CYCLE_EXPOSURE` flags rank-2 Energy/oil-refining epicenter exposure BELOW its floor** (book
touches the cycle only via LNG, an adjacent/fuel name). **Three disclosures are attached and none is
optional:**
1. ⚠⚠ **The GAP's MAGNITUDE is `unknown` (C3)** — **R39** retracted the registry's Energy tag, so the
   number may be reported as a direction of travel and **not as a level.**
2. ⚠ **The denominator is ambiguous (D170, new this run)** — with **30.3% idle cash**, the epicenter
   share on *total* assets vs *deployed* capital differ by ~1.4× (**2.88% vs 4.1%**). **Both are
   defensible; publishing neither label is not.**
3. ★ **The gap WIDENED because the book fully exited XLE on 2026-08-04** — and **S60** exists because
   **this desk has no ledger that scores a sale (D159).**
**Cleanest measured epicenter expressions that exist inside `us_top300`**: **MPC** (held) · **PSX**
(the registry's `core_pick`, not held) — both §ENRG above. **NVDA** for rank-1 (held; ⚠ **seg −9.1,
RS60 −5.2 — a turn off a hole**). **EMR** as the cleanest expression of the electrical layer —
⚠⚠ **carried with BOTH its Lens-3 TURN-OFF-A-HOLE tag and its 0↑/2↓ revision breadth attached, not
stripped**, and **absent from the cycle registry entirely (D169).**

---

## §LEDGER — what this stage wrote

**Rejections filed: 3** (each with a reason class, a `--revives-if` and a `--recheck-date` — `add`
refuses to run without both):

| Ticker | Class | Why | `revives-if` | recheck |
|---|---|---|---|---|
| **EMR** | `H.밸류소진` | 🟢 with the cluster's largest OBV accumulation, **but 0↑/2↓ next-Q revisions in 30 days AND a days-21-60 segment of −4.5 vs SPY** | a first upward next-quarter revision **AND** segment 21-60 vs SPY turning ≥ 0 | 2026-08-19 |
| **AME** | `H.밸류소진` | same shape, thinner: **0↑/1↓ revisions, segment −3.5, RS60 only +2.8** | same as EMR | 2026-08-19 |
| **MSFT** | `C.차트붕괴` | RS20 +23.6 on a **−9.8** prior-40 segment ⇒ repair not run, **plus FINRA z +2.44 crowded-short** (squeeze fuel is turn-conditional, not a thesis) | segment 21-60 vs SPY ≥ 0 **AND** FINRA z back inside ±1.5 | 2026-08-19 |

**Missed entries filed: 2** (EVENT_ALPHA filed PWR and COHR earlier this run; these are new):

| Ticker | Class | Why | `enters-if` | recheck |
|---|---|---|---|---|
| **VLO** | `M.숏리스트탈락` | **strongest segment of the three refiners (+10.4 vs SPY), OBV 매집, RS20 +12.8 — excluded from the shortlist ONLY by `vol_surge` 0.93** | `vol_surge` ≥ 1.2 with OBV 매집 held, **or** the green gate's volume conjunct is changed by a human | 2026-08-19 |
| **ANET** | `M.숏리스트탈락` | **misses the gate by 0.09 `vol_surge` points** with segment +15.2, OBV 매집, FINRA z −1.45 clean | `vol_surge` ≥ 1.2 with RS20 > 0 vs SPY held | 2026-08-19 |

⚠ **GRMN and BMY are NOT filed to either ledger** — **both already carry live rejection rows from
2026-08-04 with unexpired recheck dates.** Filing again would double-count the same decision.
**Reported in §HLTH and §LIVE, resolved nowhere.**

⚠ **No name was removed on narrative grounds while its measured flow still passed.** **FTNT** is the
one that came closest and it is **re-filed under a new thesis line with a dated re-check**, per the
475150 precedent (+41.2pp and +26.9pp, both narrative-class removals).

---

# §B-FRESHNESS — filled by ALPHA (stage 9), 2026-08-05

> Gate order: **`theme_age` deterministic novelty FIRST** (token-0), then positioning, then the
> targeted live check. A tag follows the **NAME**, not its sector's turn in the rotation.

## B-0 · ⚠⚠ The gate that structurally cannot fire — F1, measured again

**`theme_age` on every theme this sheet bets on, `--scope foreign`:**

| Theme | verdict | age (d) | 7d avg | accel | n |
|---|---|---|---|---|---|
| `refining margin` | 🟡ACCELERATING | 68 | 10.1 | **3.95×** | 153 |
| `optical transceiver` | 🟡ACCELERATING | 70 | 4.4 | **3.69×** | 88 |
| `AstraZeneca` | 🟡ACCELERATING | 78 | 15.3 | 3.16× | 280 |
| `grid` | 🟡ACCELERATING | ≥90 | 110.1 | 2.42× | 2,816 |
| `margin capture` | 🟡ACCELERATING | 70 | 1.0 | 7.5× | ⚠ **13 — unusable at that n (S5)** |
| **`switchgear`** | **⚪ECHO** | 75 | 1.4 | **1.07×** | 64 |
| `windfall tax` | 🟡ACCELERATING | 43 | 2.9 | 10.71× | ⚠ 29 |
| `Hormuz` · `OPEC` · `distillate` · `data center` | ⚪ECHO | ≥90 | — | 1.64–1.93× | large |

**🟢FRESH count: ZERO — for a 12th consecutive foreign-feed measurement.**
⇒ **🟢LIVE cannot be issued by this desk today, and the reason is arithmetic, not judgement**:
🟢LIVE requires **age ≤14d AND accel ≥2×**, and **the foreign board has produced no theme under 14
days old for twelve straight runs.** **A gate that never fires looks identical to a universe with
nothing in it (F1).** ⇒ **every tag below is 🟡PARTIAL or 🔴RESOLVED by construction, and that is
reported as an instrument property rather than as a verdict about the names.**

## B-1 · ★★★ The novelty axis contradicts this run's own headline promotion — a FOURTH independent time

**`switchgear` — the exact node DEEP-INDU identified as the AI-power chain's BINDING CONSTRAINT,
anchored on GEV's own filing — reads ⚪ECHO with acceleration 1.07×, i.e. FLAT.**

⇒ The INDU promotion now has **four** independent objections, from four different instruments:

| # | Instrument | Finding |
|---|---|---|
| 1 | days-21-60 segment vs SPY (PREMORTEM Lens 3, reproduced by DEEP-INDU) | **negative on all four carriers** (−3.1 to −14.7) |
| 2 | cross-node flow split | **GEV 🔴분산 and VRT RS20 −14.8 / RS60 −26.0 vs SPY** on the same theme and date |
| 3 | consensus revisions (BET §INDU) | **EMR 0↑/2↓ · AME 0↑/1↓** next quarter, 30 days |
| 4 | **`theme_age` (this stage)** | **the binding node's own theme is ECHO and not accelerating** |

⚠⚠ **The breadth measurement that produced the promotion is still true** (eqflow +0.156 > wflow
+0.116; 5 of 13 greens; 3 of 7 new-🟢). **Four instruments say it is a 20-day repair; one says it is
the board's only broadening sector. That disagreement is not resolved here — `S62` settles it on
2026-08-07**, and both DEEPs deferred to it independently.

## B-2 · Tags

| Name | Tag | Evidence label + date | Residual / re-check |
|---|---|---|---|
| **MPC** | **🟡PARTIAL** | `refining margin` 🟡ACCEL 3.95× on n=153 [theme_age 08-05] · Q2 print **08-04** [primary] · capture **112%** | ⚠ **The print measures Apr–Jun, a window that CLOSED ~5 weeks before the crack move being adjudicated** ⇒ **residual = S55's HO%−CL% over 08-04→08-11.** **Re-check 2026-08-11.** |
| **PSX** | **🟡PARTIAL** | Q2 print **08-05 pre-market** [primary]: realised margin **$24.08 vs $11.25 YoY** | 🚨 **The earnings CALL is 12:00 ET — after this stage.** Residual = the call's forward commentary. **Re-check 2026-08-06.** ⚠ **And its positioning REVERSED vs S53's registration** (P/C 1.25 → **0.26**, short z +1.53 → **covering**) ⇒ **the "already positioned for branch B" note is void.** |
| **VLO** | **🟡PARTIAL** | strongest segment of the three (**+10.4 vs SPY**), no print in window | Residual = **S55 08-11**. Filed to `missed_ledger` (gate-censored). **Re-check 2026-08-19.** |
| **XOM** | **🔴RESOLVED** | **S31 reads RS20 +5.5 vs SPY — between its own two branches** ⇒ structurally `AMBIGUOUS`; segment **−5.5 vs SPY** ⇒ turn-off-a-hole | **Dropped from the bettable list.** ★ **NOT filed as a new rejection row** — the defect is in the BRACKET's construction (its branches do not partition the observable), not in the name, and **PREMORTEM owns S31's re-registration.** Filing a name-level rejection here would mislabel a scenario defect as a stock verdict. |
| **ETN** | **🟡PARTIAL** | 🟢 3-axis · revisions **5↑/2↓** (the only positive of the three) | Residual = segment 21-60 vs SPY turning ≥ 0. **Re-check 2026-08-19.** |
| **EMR** | **🔴RESOLVED** | **0↑/2↓ revisions · segment −4.5 vs SPY · `switchgear` ⚪ECHO 1.07×** | **Dropped. Ledger row filed** (`H.밸류소진`, revives-if a first upward next-Q revision **AND** segment ≥ 0, **recheck 2026-08-19**). |
| **AME** | **🔴RESOLVED** | **0↑/1↓ revisions · segment −3.5 vs SPY · RS60 only +2.8 vs SPY** | **Dropped. Ledger row filed** (same class and condition, **recheck 2026-08-19**). |
| **PWR** | **🟡PARTIAL** | 🟢 NEW · but **RS60 −13.1 / segment −14.7 vs SPY** | Residual = **RS60 crossing above 0**. Already on `missed_ledger` (`Q.확신부족`). **Re-check 2026-08-19.** |
| **LITE** | **🟡PARTIAL** ⬇ **re-graded from EVENT_ALPHA's `CONFIRMED-EARLY`** | `optical transceiver` 🟡ACCEL **3.69× on n=88** [theme_age 08-05] · **the ban is DRAFTED, no named instrument exists** | ⚠ **DEEP-IT's re-grade adopted**: RS20 +18.4 vs SPY sits on a **−23.9pp** hole and the card's own KPI (RS60 > 0) is unmet at −10.3. **Residual = a named instrument (Federal Register / BIS rule / EO number) in a primary text.** **Kill date 2026-08-19.** |
| **ANET** | **🟡PARTIAL** | first **$3bn** quarter **08-04** [primary 8-K] · both windows positive vs SPY · segment **+15.2 vs SPY** · FINRA z **−1.45** | ⚠ **Implied move ±6.0% (expiry 08-07, D2)** with **P/C 0.13, skew +2.0 ⇒ "complacent, little fuel."** **Residual = `vol_surge` clearing 1.2** (it missed by 0.09). Filed to `missed_ledger`. **Re-check 2026-08-19.** |
| **COHR** | **🔴RESOLVED** | headline-named in the same ban story with **RS20 −0.1 vs SPY** ⇒ **story without money** | Already on `missed_ledger` (`M.숏리스트탈락`) from EVENT_ALPHA. **No duplicate row.** |
| **CIEN** | **🔴RESOLVED** | 🔴분산 with **RS20 −5.0 / RS60 −29.1 vs SPY** — headline-absent and broken on both windows | **Dropped.** Not filed: **the name never entered a candidate list**, so a rejection row would overstate the work done. **Named here instead.** |
| **BMY** | **🟡PARTIAL** | **B-grade**: a primary 07-30 8-K beat drove **+10.4%** of the run · **C-grade**: the AstraZeneca "megadeal" is **talk only** — `module_disclosure_us BMY` returns an **empty M&A category** | ⚠ **Segment +0.9 vs SPY, razor-thin** (the ledger recorded −1.3 the same date ⇒ a sign flip inside one session). **Residual = C7's 08-06 observable.** ⚠⚠ **Its `revives_if` looks already met, 13 days before the scheduled 08-18 recheck — NOT resolved here.** **Re-check 2026-08-06 then 2026-08-18.** |
| **MSFT** | **🔴RESOLVED** | segment **−9.8 vs SPY** · FINRA short z **+2.44 crowded-short** | **Dropped. Ledger row filed** (`C.차트붕괴`, **recheck 2026-08-19**). ⚠ **Crowded-short is turn-conditional squeeze fuel, never a standalone thesis — hard-stop stamp required if it is ever revived.** |
| **FTNT** | **🟡PARTIAL, re-filed** | **RS60 +50.4 / segment +44.8 vs SPY** — a real two-window run that is **decelerating** (RS20 only +2.9, weakest of the greens) · **z +2.07 crowded-short** | **New thesis line: a decaying 60-day excess, not a fresh ignition.** **Momentum-only flag: hard-stop required.** **Re-check 2026-08-19.** |
| **GRMN** | **🟡PARTIAL** | board's **#1** flow score; **79% of the 20-day excess vs SPY is ONE session (07-29)**; no dated catalyst | **Declined on a stated rule, not on a view.** A live rejection row already exists. **Re-check 2026-08-18.** |
| **PLTR** | **🟡PARTIAL** | 1-day move **+29.5% ≈ 4× its own 20-day sigma (7.27%)** ⇒ an earnings gap, **n=1** | **Residual = 2–3 more settled sessions before the tag means anything.** **Re-check 2026-08-10.** |
| **KKR** | **🟡PARTIAL** | NEW-🟢 · RS20 **+10.6 vs SPY** with OBV 매집 as the second leg · but **RS60 flips to −0.2 intraday** | **Residual = the HY OAS buffer (32bp) at S26's settle.** **Re-check 2026-08-12.** |
| **IRM** | **🔴RESOLVED** | **RS60 −6.5 / segment −10.9 vs SPY**, inside the board's worst-decelerating sector (RE, Δ −0.246) | **Dropped.** Not filed as a rejection: **RE holds no DEEP slot and the name was never worked to a thesis** ⇒ it is a **coverage** absence, not a judgement. Named. |
| **MET** | **🟡PARTIAL** | held; **S58 settles 08-11** | ⚠⚠ **MET is on `_US_STOP` (M152)** — **a zero-coverage reading on it is uninformative, not evidence**, and S58 must not score silence as signal. **Re-check 2026-08-11.** |
| **TRI** | **🟡PARTIAL** | 🟢 · RS20 **+17.1 vs SPY** but **segment −5.0 vs SPY** · **z +1.39** | Residual = segment ≥ 0. **Re-check 2026-08-19.** |

**Tally: 🟢LIVE 0 (structurally impossible today — B-0) · 🟡PARTIAL 13 · 🔴RESOLVED 7.**
**Every 🟡 carries a dated re-check. Every 🔴 that is a NAME-level judgement carries a ledger row;
the three that do not (XOM, CIEN, IRM) each state why a row would MISREPRESENT the work done.**

## B-3 · Carry-forward independent of sector rotation

**These tags follow the name into the next run's inheritance packet even though their sectors lose
their DEEP slots**: **BMY · MET · KKR · IRM · GRMN · PLTR** (HLTH, FIN, RE, DISC and IT all rotate).
★ **Measured reason this line exists**: 006360 carried an ALPHA tag with real-hands flow on 07-20,
its sector rested, nothing tracked it — **+12.3% over the next five sessions, unowned.**

## B-4 · `ACTION_TICKETS.md` — ⚠⚠ two defects, reported not patched

`scripts/action_bracket.py` wrote **`llm_outputs/2026-08-05/ACTION_TICKETS.md`** — **14 lines, ONE
ticket.**

1. 🚨 **It printed *"Nearest binary: PSX earnings (D-0) — both-sides armed below"* and then armed
   NOTHING.** **`CATALYST_WATCH.json` carries EIGHT binaries in window** (NFP 08-07 · CPI 08-12 ·
   PPI 08-13 · the undated Hormuz statement · PSX 08-05 · CEG 08-06 · LNG 08-06 · VST 08-07).
   ⇒ **the both-sides section is empty against 8 live binaries.** **Same family as D155** (a script
   resolving state from the wall clock rather than from a run-stamped date). ⚠⚠ **The brackets DO
   exist — S52 · S53 · S35 · S47 · S51 · S56 · S61 · S62 — they are simply not in this file.**
   **The ticket file understates the desk's own both-sides coverage; it does not mean the coverage
   is missing.** Stated so no reader concludes the protocol was violated. **Registered as `D171`.**
2. ⚠ **The single ticket is the human-locked `CORE-STARTER PSX (BUY)`, dated 2026-07-17 — D19 firing
   for a 9th consecutive run.** Its stated rationale (*"cheapest large refiner on forward 11.2,
   PEG 1.17"*) has **drifted from today's pull (forward 10.78, PEG 1.23)** and its lineage still
   descends from **R8, retracted 2026-07-22.** ★ **And today it points at a name that printed this
   morning, whose call has not happened, and whose bearish positioning has fully unwound.**
   **`core_pick` is HUMAN-LOCKED and was NOT modified.**

⚠ **The Energy GAP the ticket cites (2.88% < 8.0%) is quoted by the script as a level — which
`R39` forbids and `D170` shows is denominator-ambiguous.** **The ticket is reproduced as the script
wrote it; this note is the correction, and the script is a human-gated item.**
