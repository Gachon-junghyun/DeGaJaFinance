# BLINDSPOT_PREMORTEM — industry_US — 2026-07-25 (Sat) ★US-only

> Stage 6/10. Four adversarial lenses fanned out in parallel against this run's own tilt.
> Benchmark **SPY** inline on every relative number (C1). OBV = **C-grade (D6)**.
> **Zero sizing, zero buy/sell (P4).** All thresholds below are **frozen 2026-07-25, pre-event.**

**Draft tilt attacked:** `FIN OW · ENRG OW− · RE OW− · IT N · COMM N · STPL N · HLTH N− · INDU N ·
DISC N− · UTIL UW · MATR UW` · DEEP picks `[FIN, ENRG] + [RE]`, no 4th.

**Result: the lenses did NOT rubber-stamp.** Three of the four returned findings that change this run's
output, and **two of them falsify reasoning written earlier today by this same desk.**

---

## 0 · ⚠ Provider disagreement on the event dates themselves — declared, not resolved (rule D5)

Pulled fresh from `yfinance` calendar and set against the dates this run has been carrying:

| Name | Carried by this run / `CATALYST_WATCH` | `yfinance` calendar | State |
|---|---|---|---|
| **UPS** | 2026-07-28 (S20) | **2026-07-28** | ✅ agree |
| **MSFT** | 2026-07-29 (S13) | **2026-07-30** | ⚠ **1-day conflict** |
| **META** | 2026-07-29 (S16) | **2026-07-30** | ⚠ **1-day conflict** |
| **AMZN** | 2026-07-30 `[news, 2 outlets]` | **2026-07-31** | ⚠ **1-day conflict** |
| VLO · MA · STNG | 2026-07-30 | 2026-07-30 | ✅ agree |
| MPC | 2026-08-04 | 2026-08-04 | ✅ agree |
| **EQIX** | **`[blank]` — dig D54** | **2026-07-30** | ★ **D54 CLOSED** |
| V | — | 2026-07-29 | new (S14-ANNEX subject) |
| STX | — | 2026-07-29 (one body says 07-28) | ⚠ conflict |
| XOM · PSX | — | 07-31 · 08-05 | new |

★ **If `yfinance` is right, the desk's "2026-07-29 six-trigger cluster" is mis-dated**: 07-29 becomes
FOMC + V + STX, and **07-30 becomes the real cluster — PCE + MSFT + META + VLO + STNG + MA + EQIX.**
**Both sets are recorded. Neither is silently picked.** Every bracket below is written on an
**observable with a window**, not on a single calendar day, precisely so a 1-day error cannot void it.

★★ **D54 is closed: EQIX prints 2026-07-30** — which is **P5's own second settling point**, five days
out. It was `[blank]` in every calendar this morning.

---

## 1 · LENS 1 — UNDER-COMPUTED LEGS

### ★★ PROMOTE-TO-DEEP — the AI-server hardware leg: **HPE · DELL · STX**

| Measure | HPE | DELL | STX |
|---|---|---|---|
| RS60 vs **SPY** (independently re-derived) | **+67.0** | **+108.7** | +43.1 |
| Revision breadth, current quarter (30d) | **17↑:0↓** | **20↑:0↓** | 4↑:0↓ (next-q) |
| Current-year EPS, 90d | **+60.9%** | **+64.9%** | — |
| Next-year EPS, 90d | +46.8% | **+58.1%** | +38.3% |
| Forward P/E · PEG | **11.90 · 0.85** | 20.02 · 0.72 | 29.91 · **0.63** |
| % to mean target | **+34.5%** | +14.5% | +18.4% |

★★ **The measurement that makes this a promotion rather than a mention** — and it is Lens 3's, cross-
checked against Lens 1's: **only 5.9% of DELL's +108.7pp and 2.2% of HPE's +67.0pp was earned in the
last 20 sessions.** The R9/AXON failure shape is **~98% of the 60-day excess in the last 20 days on a
CUT estimate.** This is the exact inverse: the move was earned in days 21–60 **and the estimates are
still being raised** (DELL's next-year book moved **+5.9% in the last 30 days alone**).

★ **And it is a W5 split the desk would have collapsed**: five-quarter gross margin
**HPE 28.4 → 36.5% (+8.1pp)** against **DELL 21.1 → 17.8% (−3.3pp)**, on revenue +40% and +87.5% YoY.
HPE's operating margin went 3.8% → 7.7%; its 10-K names Juniper integration as a live Item 1A risk.
**"Same layer, second vendor" is wrong — they are opposite margin engines.**

**Dated catalyst in window: STX 2026-07-29 (⚠ one body says 07-28 — conflict declared).**
DELL and HPE print **2026-09-04**, outside it.

⚠ **The strongest argument against, and it corrects EVENT_ALPHA Card 1**: the "un-named / in no
thread title" crowding claim is **refuted at the article level** — `fts --scope foreign --days 7`
returns **DELL 181 · STX 110 · HPE 58** matches, including *"Dell Technologies (DELL) Climbs 9.3% on
Booming Demand for Nvidia-Powered AI Servers"* [07-23] and *"Hewlett Packard Enterprise: Networking
Is Now The Profit Engine, And Nobody Repriced It"* [07-21]. **The leg is un-threaded, not
undiscovered** — the clustering tool missed it, which is a tool finding, not an alpha finding.
⚠ Second argument against: **STX's gross margin 35.2 → 46.5% is the same price-cycle signature the
desk's own regime call treats as a peak marker.**

⇒ **PROMOTED. Final DEEP set = 4: ENRG · FIN · RE · IT (AI-server hardware leg).**

### WITHIN-RUN-WATCH — the AI-datacentre physical layer

★★ **The finding here outranks the leg**: `yfinance` gives **CARR 07-28 · VRT 07-29 · JCI 07-29 ·
PWR 07-30 · TT 07-30 · ETN 07-31 — six dated binaries inside four sessions**, and
**EVENT_ALPHA Card 3 set its resolving horizon at 2026-08-08, after every one of them.**
**Card 3's horizon is re-cut to 2026-07-31.**
- Card 3's "seven of eight negative deltas" is **one session ⇒ n≈1 (S1)**. σ-normalized on 07-24
  (SPY +0.14σ): **PWR −1.81 · VRT −1.08 · ETN −1.00 · CIEN −0.91 · GEV −0.40 · ANET −0.38 ·
  CARR −0.22 · JCI +0.03 · TT +0.16.** **Only PWR is beyond −1.5σ.** And **ANET is +4.5pp/20d and
  +1.2pp/60d vs SPY** while Card 3 filed it as distribution.
- ⚠ **But the revision axis — independent of OBV — corroborates Card 3 rather than refuting it**:
  **VRT current-quarter +0.0%/90d (2↑:0↓) · ETN −1.4%/90d · PWR +5.3%/90d**, against DELL +64.9% and
  HPE +60.9%, at 25.6–37.9× forward. **Ninety days of record announcements produced no estimate
  response at the names that have to build it.**

### WITHIN-RUN-WATCH — Utilities' regulated leg

★ **The UW was set on the leg with no information in the window.** UTIL was cut N−→UW on Δ −0.105
carried entirely by **VST −0.470 · NEE −0.229 · CEG −0.212** — and **none of those three reports in
the window** (VST 08-07, CEG 08-06, NEE already printed 07-24), while **the regulated leg reports en
masse: WEC 07-29 · ETR 07-29 · EXC 07-30 · SO 07-30 · XEL 07-30 · AEP 07-30 · D 07-31.**
**PCG** is the sector's only 🟢 and a `new_green` with **`vol_surge` 1.33 — so it is not an M75
volume-gate artifact** — RS60 **+6.0 vs SPY**, forward P/E 9.89, **+28.7% to mean target**, beta 0.27.
⚠ Against it: PCG's revision book **contradicts its flow** — current-quarter **1↑:5↓ (7d) / 3↑:4↓
(30d)**, revenue +0.07% YoY — and it does not print until **2026-10-22**. **Watch, not promote.**

---

## 2 · LENS 2 — REGIME-FLIP / BOTH-SIDES BRACKETS

### ★★ The implied moves, normalized — this upgrades a qualitative claim to a measurement

| Name | own σ20 (daily) | implied | in σ20 | vs √5·σ20 | verdict |
|---|---|---|---|---|---|
| **MSFT** | 2.02% | ±1.7% (exp **07-27**) | **0.84σ** | — | **prices less than ONE ordinary day** |
| **META** | 3.42% | ±2.1% (exp **07-27**) | **0.61σ** | — | same |
| **AMZN** | 1.82% | ±1.6% (exp **07-27**) | **0.88σ** | — | same |
| **UPS** | 1.71% | **±6.9%** | 4.04σ | **1.81×** | **genuinely event-priced** |
| VLO | 2.47% | ±6.6% | 2.67σ | 1.20× | mildly event-priced |
| MA | 1.60% | ±3.9% | 2.44σ | **1.09×** | ~nothing charged for the print |
| DLR | 3.04% | ±3.9% | 1.28σ | **0.57×** | prices 57% of its own realized |

★ **M89 splits for the first time in four runs.** The three hyperscaler straddles **still expire
before their events** (07-27 vs a 07-29/30 print) *and* price **below one normal session** — so **no
price threshold taken from them is admissible, and this is now measured rather than asserted.**
Conversely **UPS, VLO, MA and MPC now carry event-covering straddles**, where three prior runs had
only two on the whole board.

### Brackets registered (frozen 2026-07-25) — full text in `handoff/SCENARIOS.md`

| ID | Event · date | Branch B (**against us**) | Frozen observable · threshold | Tilt hit | Rips on B |
|---|---|---|---|---|---|
| **S20-ANNEX** | UPS Q2 · 07-28 | guidance cut on **VOLUME**, not fuel | median **RS20 vs SPY** of {CSX,UNP,NSC} **turns negative by 2026-08-04**. **Any UPS same-day move inside ±6.9% is pre-declared no-information** | **INDU N is false comfort** — the downgrade was on the *label*; the rail node is untouched by it | CSX·UNP·NSC·ODFL — *downside*; **UNP double-hit** (≈8 of 12 revenue-growth points are fuel surcharge) |
| **S23** ★new | FOMC · 07-29 | **hold + BEAR-FLATTENER.** S19 brackets a *hike*, S9 a *dovish* real-rate fall; **neither contains "hold, DGS2 stays 4.15–4.45%, and the curve flattens further"** — NIM dies without tripping either threshold | **T10Y2Y ≤ +0.20 on a close by 2026-08-05**, with **DGS2 quoted alongside**. No options instrument exists for an FOMC decision — stated, not dressed up | **FIN OW (both remaining legs)** — the steepener leg already broke 07-23, leaving breadth alone. ★ **UTIL UW loses on the same tick** ⇒ they are one rate bet carried with opposite signs | WELL·PLD·AMT·PCG·DUK |
| **S24** ★new | MSFT/META/AMZN capex · 07-29→31 | capex **raised** and the physical layer **re-rates**, inverting Card 3 | median **RS20 vs SPY** of {VST,CEG,GEV,VRT} **> 0 by 2026-08-12**. ⚠ **n≈1** — measured SPY-residual **VST–CEG +0.768 · GEV–VRT +0.601 · VST–GEV +0.490**, so this is **one unit's return, not four observations**. **No price threshold — the straddles price 0.61–0.88σ** | **UTIL UW**, which is a levered short on AI capex. S13/S16 aim at IT and COMM, both **N**, so neither moves much | VST·CEG·GEV·VRT·ANET (2nd tier PWR·CIEN·NEE) |
| **S14-num** | MA Q2 · 07-30 | volume miss | **numeric annex only — S14 is NOT re-frozen.** MA's straddle charges **1.09× ordinary realized**: **any same-day move inside ±3.9% carries no information and may not be read as confirming FIN OW** | FIN OW | WELL·PLD·AMT·SPG·VTR — ★ and **MA/V is a different residual unit from JPM/TRV/CB** (MA–JPM +0.238, TRV–MA +0.382) |
| **S21/S8** | VLO + STNG · 07-30 | crude falls **AND** the diesel crack rolls together | VLO same-day **outside ±6.6%** *and* settled 3-2-1 crack **< 65 by 2026-08-06**. Inside ±6.6% = no information | ENRG OW− | DAL·UAL·LUV·FDX·UPS (fuel +66–84% YoY, D23). ⚠ **Crude falls but cracks HOLD = S8 branch B, explicitly NOT against us** |
| **S25** ★new | RE OW− · undated | **the tilt is carried by the least representative name.** DLR has **no event in the window** — it already printed — yet RE went N→OW− largely on **DLR Δ +1.099** | Report **DLR RS20 vs SPY** and the **{PLD,AMT,WELL} median RS20 vs SPY separately, never merged**. Trip: **by 2026-08-08 DLR falls below that median while the median stays positive** | RE OW− | WELL·VTR·SPG·IRM·PLD |
| **S26** ★★new | credit · undated | see §5 — **the escape hatch** | **HY OAS ≥ 3.10% on a close by 2026-08-12, with NFCI turning positive WoW** | **all three OW tilts at once** | WELL(β 0.224)·AMT(β −0.054)·XOM(0.256)·CB(0.125)·TRV(0.339) |

**★ S25's measurement**: SPY-residual, 499 days — **XLRE–PLD +0.714 · XLRE–AMT +0.712 ·
XLRE–WELL +0.652**, but **XLRE–DLR only +0.456**, and DLR–PLD +0.213 / DLR–AMT +0.260 /
DLR–WELL +0.254. **{DLR,EQIX} is a separate unit at every threshold ≤ 0.65.** DLR is simultaneously
the board's most complacent instrument (**0.57× its own realized**, short **0.0% float**, P/C 0.08).

### Brackets DROPPED, with the information-content reason (L3)

1. **June PCE (S15) standalone** — S19 already pre-registered that FOMC 07-29 and PCE 07-30 **share one
   driver (oil), one day apart, and are not two observations.** Folded into S23. **S15 stays armed as frozen.**
2. **AMZN standalone** — its only tilt link is DISC N−, which was declined-to-UW on Δ +0.088 being 2nd
   best on the board; a print does not address that. **Neither branch changes a conclusion.**
3. **S19 branch H** — it attacks *"the OW Health Care."* **HLTH is N− today**, downgraded twice since
   registration. Low information **for this board**. Scoring note only; **S19 is not re-frozen.**
4. **MATR UW · STPL N** — no binary in the window touches either. Stated rather than manufactured.

---

## 3 · LENS 3 — MOMENTUM RE-TAGS, and two falsifications of this desk's own reasoning

### ★★★ Falsification 1 — ROTATION declined the IT downgrade for a reason that does not survive

`SECTOR_ROTATION.md §2` declined **IT N→UW** "on rule D6 — the C-grade reds may not override A-grade
RS60 of +78.8 / +39.5 / +36.9 / +29.1 / +22.9 / +17.7."

**Every one of those six RS60 readings has a NEGATIVE last-20-session contribution:**
**MU −31.5% · SNDK −99.7% · WDC −81.9% · AMAT −55.3% · MRVL −139.1% · LRCX −141.2%.**

⇒ **A positive RS60 whose entire content was earned more than 20 sessions ago and is currently being
given back is a decaying stock of past excess, not a live A-grade signal.**
**The decline was RIGHT; the stated reason was WRONG.** What actually carries it is the **revision
book** — MU **25↑:0↓** (30d) and **24↑:1↓** still in the last 7 days, AMAT **25↑:0↓ (30d) and 26↑:0↓
(7d)** — **a B-grade fundamental axis `SECTOR_ROTATION.md` never cites.**
⚠ **And the defence has an expiry date**: if the desk keeps resting on RS60, it **expires
arithmetically around mid-August**, when the days-21-to-60 segment rolls out of the window.
★ This is the fifth instance this run of the desk's own recurring failure class — **direction right,
driver wrong** — and the first where the target is a file written earlier the same day.

### ★★★ Falsification 2 — R7/M88's "five replications" may be ONE observation, and it lands on the slot just promoted

**WELL and VTR earned 86.2% and 132.1% of their 60-day excess vs SPY in the last 20 sessions**, with
revision books of **0↑:1↓ and 0↑:2↓** and VTR's current-quarter estimate **cut −33.3% over 90 days**.
⇒ **Five replications taken on overlapping 60-day windows that all contain the SAME 20-session move
are one observation, not five.** **This goes in front of the RE DEEP mandate before it spends the slot.**

### ★ Falsification 3 — L2 (peak-margin trap) is being transferred by association

- **MU**: canonical — 84.6% gross margin = **100th percentile of a 17-year series, +25.7pp over its own
  prior peak**, at **6.0× forward.** L2 applies.
- **WDC**: FY25 gross margin **38.8% against a prior peak of 37.3% — only +1.5pp over peak** on a
  9-year series, at **28.0× forward**. **Not a low-multiple-on-peak-margin trap at all.**
- **SNDK**: the series is **3 years long (FY23–25, post-spin) and contains no cycle** ⇒ **L2 is
  UNMEASURABLE, not confirmed** (C3/C5).

### Re-tags — the ones that change something

| Verdict | Names | The measurement |
|---|---|---|
| **Most wrongly avoided by an "it already ran" reflex** | **DELL · HPE · AMAT** | DELL 5.9% / HPE 2.2% of the 60-day excess in the last 20 days, on 20↑:0↓ and 17↑:0↓. **AMAT's up-count ROSE through its drawdown (25↑:0↓ over 30d → 26↑:0↓ over 7d) while price fell 25.8% off its high** — a de-rating, not an exhaustion, and the cleanest instance on the board of the R9 test correctly failing to fire |
| **Genuinely EXHAUSTED** | **VTR · WELL · VLO** | VTR: **132.1%** of the excess in 20 sessions (days 21–60 are **negative**), 0q estimate **−33.3%/90d**, **0↑:2↓**, above target, 118.7× — canonical R9. WELL: 86.2%, **0↑:1↓**, next-year **−7.4%/90d**, 75.0×, above target. **VLO: 80.2%, and its current-quarter book is a coin-flip — 7↑:5↓ (30d), 6↑:5↓ (7d) — the only refiner being actively cut, 4.3% above target. It prints 07-30, which resolves it** |
| **EXHAUSTED, hitting the FIN OW directly** | **TRV** | **98.6%** of its 60-day excess in the last 20 sessions, 0q breadth **2↑:1↓ (30d) → 0↑:1↓ (7d)**, **−8.2% to target**. Its 0y book moved **+18.8% in one week = one print, n≈1 (S1).** TRV is one of the five 🟢 the FIN upgrade was written on |
| **EXTENDED-BUT-LIVE** | **FTNT (38↑:0↓, 1.4% in last 20, prints 07-30)** · DDOG · DELL · HPE | Flip: any down-revision entering FTNT's 7-day column |
| **Near-book EXHAUSTED** | **CRWD** | 0q **29↑:11↓**, and **0↑:5↓ in the last 7 days**. ★ Confirms M28's set-aside **on the measured axis, not on the 117× multiple — C5 stands unbroken** |
| **INDISTINGUISHABLE, with a caveat that matters** | CSX · UNP · RTX · TMO · AAPL | CSX **83.0%** and UNP **125.5%** of the 60-day excess in the last 20 days on **+5.3% / +3.0%** estimate moves — **deal-driven, and a direct corroboration of C-B.** **RTX's 120-day excess is −0.7 and TMO's is −8.9** — 20-day re-rates off flat bases. **AAPL 107.2% in 20 sessions, above target, 7-day breadth frozen 0↑:0↓** |

### ★ The memory complex — the lens contradicts the desk, and the contradiction is recorded

**MU/SNDK/WDC read EXTENDED-BUT-LIVE on the KPI and rolled on the tape — two different windows the
desk is collapsing into one.** R9's shape is *price up, estimate cut*. Here it is **price down,
estimate violently up**: MU next-year **+52.9%/90d and +30.3% in the last 30 days**, SNDK
**+86.2%/90d**, WDC **+30.2%/90d**, while price fell **24.1% / 38.5% / 30.3%** off their 60-day highs.
**Consensus does not believe margin has peaked; the tape does.**
★ **The desk is siding with the tape against the estimate book — the exact inverse of what it did at
AXON, where it sided with the estimate book against the tape.** **That inconsistency is the finding,
and it is named here rather than smoothed.** It does **not** overturn §1's regime call (M1/M2/M18 are
untouched by a consensus opinion) — it says the desk's *procedure* has been applied in opposite
directions on two occasions and owes an explanation.

---

## 4 · LENS 4 — CYCLE EXPOSURE: the ✅ is an artifact, measured two ways

**Registry**: actual path is **`data/cycles/cycle_registry.json`** — the script's own footer cites
`data_build/cycles/`, **which does not exist. The provenance string is wrong** (dig D60).
**Last updated 2026-07-17 — 8 days stale — with exactly 3 rows.** D20 unremediated.

★ **Four of the top six RS60 names on the entire 300-name board are in NO registry row at any layer**:
**DELL +108.6 (#1) · DDOG +83.8 (#2) · PANW +75.1 (#4) · FTNT +73.9 (#5)** (HPE +66.8 is #6).
Missing rows the week's evidence demands: **AI-server/OEM assembly · AI-security/systems software ·
the memory/HBM supply-agreement leg · the datacentre physical split (REIT vs electrical)**.

**M81 replicates on both legs:**
- **AI-compute** — measurable bucket ranked: MU +78.8 · AMD +57.7 · AMAT +36.9 · ASML +23.1 ·
  MRVL +22.9 · LRCX +17.7 · KLAC +12.5 · ANET +1.4 · **NVDA −6.8 (9/10)** · **AVGO −8.3 (10/10)**.
  The book holds **AVGO, NVDA, TSM**. **Held measurable mean −7.55 vs bucket mean +23.59 = 31.1pp
  below its own bucket average.** ⚠ **TSM's RS60 is `unknown` — it is not in `us_top300`**, so one of
  three held epicenter names is unmeasurable by this desk.
- **Energy** — MPC +29.1 · VLO +22.1 · PSX +21.4 · EOG +4.0 · **XOM +0.4 (5/6)** · CVX −0.4.
  **Refining exposure 0%.** Sharper: **the registry's own human-locked `core_pick` is PSX and the book
  holds none of it.**
- **Defense is fine** — but the brief handed to the lens **omitted GD, which is actually #1 (+19.5)**,
  ahead of the held RTX (+17.3) by 2.2pp — inside noise. **No finding; the omission is the note.**

### ★★★ The ✅ is price drift, not construction

The AI-compute margin over its 12.0% floor, across five consecutive runs, **with the held set
(AVGO/NVDA/TSM) unchanged throughout**:

`07-21 −0.001 (GAP=True) → 07-22 +0.252 → 07-23 +0.254 → 07-24 +0.136 → 07-25 +0.011`

**Nothing was bought. The flag flipped from FAIL to PASS and back toward zero purely on
mark-to-market drift, and today it clears by 1.1 basis points** — a fraction of one day's move in one
name. Energy shows the same in reverse: 07-23 read **0.00% / GAP=True**, and the gap "closed" to
11.33% ✅ via **XOM — the 5th-of-6 name and not the registry's own core_pick.**

**And a threshold satisfied by a bucket's weakest members is not a threshold.** `min_epicenter_pct`
counts dollars inside a ticker list and is **blind to rank within it** — across an 87.1pp intra-bucket
span, its answer is nearly independent of the question it purports to ask.

**Better specification, handed to BET (dig D61):**
1. **Rank-weighted**: require the held position's median RS60 vs SPY to sit at or above its bucket
   median. **AI-compute would read −7.55 vs +20.4 ⇒ FAIL by 27.9pp today.**
2. **Sub-layer coverage floor**: ≥1 position in each named sub-layer. **Energy would read 0/1 refining
   ⇒ FAIL despite 11.4% of dollars.**
3. Report **`margin_pp` as a first-class field** and treat **|margin| < 0.5pp as UNRESOLVED, not PASS.**

⚠ **Reconciliation defect (dig D62)**: `RISK_UNITS.json` (2026-07-24) enumerates the book as
**AVGO, KMI, LNG, MA, NVDA, RTX, VST, XOM — TSM is absent**, while `cycle_exposure` has counted TSM
in epicenter dollars every day 07-21 → 07-25. **One of the two is wrong about a position inside the
rank-1 epicenter, and which is `[unknown]`.** The 12.01% should not be trusted until it is reconciled.

---

## 5 · ★★ The scariest scenario nobody had bracketed — the credit escape hatch

**Every bracket in the book — S19, S9, and four of the six written today — lists `HY OAS > 3.10%` as
an *invalidation*:** *"then it is a credit event and the rate attribution is void."*

**That converts the desk's single largest correlated exposure into a get-out-of-jail card.**

The correlated-tilt audit (`scripts/risk_units.py`, SPY-residual, **499 aligned days, ARI 1.00**)
says the three OW tilts are **genuinely three units**: **XLF–XLE +0.188 · XLF–XLRE +0.307 ·
XLE–XLRE +0.134**; between-group 0.118 vs within-group 0.576; they never merge at any threshold from
0.55 to 0.85. **The labels are honest.**

⚠ **But independence is conditional on SPY, and a credit shock IS the SPY factor.** Betas:
**JPM 0.932 · XLF 0.789 · DLR 0.769 · PLD 0.766 · PSX 0.747 · MPC 0.689.** Residualizing removes
exactly the factor that would deliver the shock. **Three units, one shared beta — and the registered
response to the one event that hits all three is to declare the brackets void rather than to record
being wrong.**

⇒ **Registered as scenario S26, a BRANCH and not an invalidation.** Frozen observable **HY OAS
(FRED `BAMLH0A0HYM2`) with NFCI quoted alongside**; frozen threshold **HY OAS ≥ 3.10% on a close by
2026-08-12 with NFCI turning positive WoW**. **No options instrument covers this — stated.**
State today: **HY OAS 2.77% (already +9bp this week, §MACRO A-2), NFCI −0.552 loosening a 5th week —
the only direction with room is wider.**
★ **Rips on it**: the low-beta side — **WELL (β 0.224) · AMT (β −0.054) · XOM (0.256) · CB (0.125) ·
TRV (0.339)**. ★ **CB and TRV sit INSIDE the FIN OW: the FIN OW carries an internal hedge its label
hides, and it is the only one on the board.**

### And the sub-unit structure differs per tilt — it flips two verdicts

- **ENRG OW− is one bet repeated four times**: **MPC–VLO +0.878** (desk carried +0.864),
  VLO–PSX +0.848, MPC–PSX +0.846, **XOM–XLE +0.911**. **No internal breadth exists.**
- **FIN OW's breadth is real**: it splits into **{JPM,XLF} / {MA,V} / {CB,TRV}** at threshold ≤0.55 —
  three genuine sub-units. **This independently supports the eqflow>wflow promotion.**
- **RE OW− is two units and was granted by the minority one** (S25).
- ★ **Bonus falsification**: the carried 07-22 claim *"IT + RE + UTIL are one bet — the AI-datacentre
  build-out"* is **FALSE for the RE leg** (**DLR–MSFT −0.061 · DLR–META −0.037 · DLR–NVDA +0.090 ·
  EQIX–NVDA −0.056**) and **TRUE for the UTIL leg** (VST–CEG +0.768, GEV–VRT +0.601).
  ⚠ That second clustering run's **ARI is 0.239 (unstable)**, so only the **pairwise** numbers are
  cited and its unit memberships are not.

---

## 6 · What this stage changes

| # | Change | Owner |
|---|---|---|
| 1 | ★ **DEEP set goes to 4: ENRG · FIN · RE · IT (AI-server hardware leg: HPE/DELL/STX)** | DEEP |
| 2 | ★ **RE's DEEP mandate is amended**: it must first test whether R7's five replications are one 20-session observation (§3 Falsification 2) before it spends the slot on the spread | DEEP |
| 3 | ★ **ROTATION's stated reason for declining the IT downgrade is corrected** — the verdict stands, the reason is replaced by the revision book, and its RS60-based defence has a **mid-August arithmetic expiry** | recorded here; STANDING_VIEW at run end |
| 4 | **EVENT_ALPHA Card 3's horizon re-cut 08-08 → 07-31** (six physical-layer binaries land 07-28→07-31) | ALPHA |
| 5 | **EVENT_ALPHA Card 1's "un-named" crowding claim is corrected** — DELL 181 / STX 110 / HPE 58 article matches; the leg is **un-threaded, not undiscovered** | recorded here |
| 6 | **Seven brackets** (S20-ANNEX · S23 · S24 · S14-num · S21/S8 · S25 · S26) registered with frozen observables and thresholds; **four brackets dropped with information-content reasons** | ALPHA (action bracket) |
| 7 | **Cycle-GAP verdict overturned in substance**: the ✅ clears by **1.1bp on mark-to-market drift with nothing bought**; a better-specified threshold **FAILS on both rank-1 and rank-2** | BET |
| 8 | **Three new digs**: D60 (registry provenance path wrong) · D61 (rank-weighted + sub-layer cycle threshold) · D62 (RISK_UNITS vs cycle_exposure disagree on TSM) | next HANDOVER |
| 9 | ⚠ **TRV, one of the five 🟢 the FIN upgrade rests on, is re-tagged EXHAUSTED (R9 shape, 98.6% in 20 sessions, 0↑:1↓ over 7d, −8.2% to target)** — handed to DEEP FIN, not acted on here | DEEP |

## ✅ EXIT CHECK
- [x] **4 lenses fanned out in parallel**; each returned named tickers and dated catalysts.
- [x] **Every bracket names its observable + frozen threshold + date, with BOTH branches**, registered
      in `handoff/SCENARIOS.md`. **No one-way bracket exists.**
- [x] **Every magnitude threshold is stated against the implied move**, normalized to each name's own
      σ20 (§2). **MSFT/META/AMZN are pre-declared no-information (0.61–0.88σ, and their straddles
      expire before their events)**; UPS/VLO/MA same-day moves inside their implied bands are
      pre-declared no-information.
- [x] **Each branch graded by information content**; **four binaries DROPPED with the reason stated**
      (PCE double-count · AMZN · S19 branch H · MATR/STPL).
- [x] `BLINDSPOT_PREMORTEM.md` written — legs, brackets, re-tags, cycle GAP.
- [x] Every catalyst-bearing leg **promoted or logged as within-run watch**; nothing silently dropped.
- [x] **DEEP set updated and stated: ENRG · FIN · RE · IT (AI-server hardware leg).**
- [x] No sizing, no buy/sell language (P4).

---
> Next: `python pipeline/run_protocol.py industry_us --next` → **DEEP**.
