# SECTOR_DEEP_IT — industry_US · 2026-08-10 · Continuous slot 2 (declared fallback) · **full fresh map**

> Scope: Information Technology, GICS-labelled, `us_top300` universe (56 names). Bench **SPY** named
> inline throughout (C1). Flow `asof settled 2026-08-07`; anything dated 2026-08-08 through today is
> tagged `[live]` and does not carry a verdict. **TRACK: ROTATING — last DEEP coverage of the sector as
> a whole was 2026-08-05; the 08-08 DEEP_IT was scoped narrowly to optical/interconnect only** and is
> not treated as covering this ground. P4 — analytical only, zero buy/sell language, zero sizing.

## §0 · THE VERDICT — three questions, one shared cause

**Q1 (the eqflow/XLK contradiction) and Q2 (CXMT) both trace back to the same fact: "Information
Technology" is not one population this run, and treating it as one is the error.** The sector-level
number (eqflow **−0.160**, worst of 11; wflow **−0.008**, near-flat) is an average across three
sub-groups whose flow scores span more than a full point (**+0.359 to −0.689**) — a spread **6.5× the
eqflow reading it produces and 130× the wflow reading**. Per the stage rule (`RESEARCH.md` W5): **the
spread between sub-nodes exceeds the sector's own move, so IT is the wrong unit of analysis, and this
file says so rather than writing one verdict for both halves.**

## §1 · Flow — the sub-node dispersion, measured from `SECTOR_FLOW_US.json` (56 names, settled 08-07)

| Cluster | n | mcap share | avg `flow_score` | tags | OBV mix |
|---|---|---|---|---|---|
| **Mega-cap compute platform** — NVDA · AAPL · MSFT · AVGO | 4 | **54.2%** | **+0.359** | 4× 🟡중립 | **4/4 매집** |
| **Semi equipment + memory + chip-design** — MU · AMD · INTC · AMAT · LRCX · ARM · KLAC · SNDK · TXN · QCOM · IBM · ADI · GLW · CDNS · SNPS · NXPI · CIEN · MCHP · ON · Q · ASML · WDC · STX · MRVL | 24 | **30.6%** | **−0.689** | 21× 🔴분산, 3× 🟡중립 | **21/24 분산** |
| **Software / applications / networking-integration** — PLTR, SHOP, COHR (the 3 greens) + CRM, ADBE, ORCL, PANW, NOW, ANET, ACN, INTU, DELL, HPE, CSCO, MSTR, MSI, FTNT, MPWR, TEL, APH, DDOG, CRWD, KEYS, TER, JBL, APP, ADSK, LITE | 28 | **15.2%** | +0.219 | 3× 🟢, 24× 🟡, 1× 🔴 | 16/28 매집 |

**Reading**: the cap-weighted number (wflow −0.008) and XLK's price return are both being carried by the
54.2%-of-cap mega-cap cluster, which is uniformly OBV **매집** this settled bar and averages a
**positive** flow score (+0.359 vs SPY, C1). The equal-weighted number (eqflow −0.160) counts that same
cluster as **4 names out of 56** — its true influence on eqflow is 4/56 ≈ 7%, while the 24-name
semi/equipment/memory cluster (30.6% of cap but **43% of the name count**) drags the equal-weighted
average hard negative. **Both numbers are correct measurements of different things — a cap-weighted
average and a name-count average — and neither is an error.** The instrument answering "how did the
sector trade" (XLK, cap-weighted) and the instrument answering "how many constituents are
participating" (eqflow, breadth) are reporting on different populations by construction, and this run's
±3.7pp size disagrees enough that the two must be read separately from here on, not reconciled into one
IT verdict.

**A second, independent dispersion inside the mega-cap cluster itself, same paragraph so C1 is
satisfied against SPY**: MSFT's RS20 is **+27.4 vs SPY** — the desk's largest 20-day excess of any IT
name — while NVDA (19.4% of the whole sector's cap, `top1` in `SECTOR_FLOW_US.json`) is barely positive
at **+3.7 vs SPY**, and its RS60 is **negative (−3.3)**. `wflow_ex_top1` (NVDA removed) is **−0.110**,
materially more negative than the unadjusted **−0.008** — confirming the cap-weighted tape's positive
lean this week is not "NVDA alone" but is concentrated in **MSFT's** 20-day move specifically, layered
on top of NVDA/AAPL/AVGO holding roughly flat. This also supplies a plausible mechanical answer to the
**exc5 (+3.69) vs exc20 (−1.25) sign flip** MACRO flagged: a **fast, top-heavy, last-5-session** rally
(MSFT-led) sits on top of a **flatter-to-negative 20-day base** for the same names — the shape is
consistent with the breadth read (3/56 green), not in conflict with it. This is offered as the most
parsimonious explanation available on this run's data, **not as a re-scored bracket** — no bracket in
this desk's registry owns the exc5/exc20 sign disagreement, and none is opened here.

**Resolution stated plainly**: the eqflow/XLK contradiction **cannot be resolved into a single sector
verdict, and that is the correct output, not a failure to resolve it.** What can be said with the
numbers in hand: (i) the mega-cap compute layer is flow-positive and accumulating and is what XLK's
price is measuring; (ii) the semi-equipment/memory/chip-design layer — the plurality of the sector by
name count — is in outright distribution and is what eqflow is measuring; (iii) **ROTATION's N verdict,
which reads the aggregate, is not contradicted by either sub-read individually** — it is simply not
informative about which of the two populations an investor would actually be exposed to.

## §2 · IR anchor and the binding carry rule — MU FY26Q3 10-Q, primary source (`module_disclosure_us`)

**This closes `RESEARCH.md` D117's open question (`C1`: do LTA price floors hold margin?) with a US
primary filing, where the prior evidence was an outlet paraphrase of a Samsung earnings call.**
`module_disclosure_us MU --days 120` lists **one 10-Q, filed 2026-06-25, period ended 2026-05-28
(FY26Q3)**: `sec.gov/Archives/edgar/data/723125/000072312526000015/mu-20260528.htm`. Fetched and read
directly (not the press summary). The filing's own words, Item 2 MD&A, **Strategic Customer
Agreements**:

- **"Strategic customer agreements are structured as take-or-pay agreements, with binding commitments
  for specific volumes over the multi-year contract terms."**
- **"The largest agreements generally have a ceiling price for existing products that approximates the
  market price in the second calendar quarter of 2026, and a floor price through the term of the
  agreement."**
- Management: **"We expect gross margins from our strategic customer agreements with price bands, even
  at floor pricing levels, to yield gross margins well above our peak quarterly margins in any past
  cycle."**

**Answering the task directly — share of volume contracted: `unknown` (C3), and the filing itself
explains why it cannot be recovered from what MU discloses.** The only quantified figure is **remaining
performance obligations ("RPO") of approximately $5.0bn as of 2026-05-28**, of which **$422mn is booked
as contract liabilities** and **roughly one-third is expected to convert to revenue over the next twelve
months**. That $5.0bn is a **floor, not the total contracted book** — MU's own text excludes from RPO
(i) contracts with an original term of one year or less (practical expedient) and (ii) "a minority of
agreements" priced purely at market with no fixed pricing or price bands. Scaled against annualized
Q3-run-rate revenue (**$41.456bn × 4 ≈ $165.8bn**), $5.0bn RPO is **~3.0% of annualized revenue** —
but because of the two exclusions above this is a **lower bound on a narrower base (multi-year,
fixed/banded-price contracts only), not an estimate of total contracted volume share.** No further
disclosure narrows it. **Marked `unknown` per the task's own instruction, not zero and not "small."**

**Why this matters to the desk's regime call — the mechanism, stated once, carefully**: `M1`
(`STANDING_VIEW.md`, TrendForce, seed 2026-07) reads server DRAM contract price QoQ as **1Q26 +90–95% →
2Q26 +58–63% → 3Q26 +13–18%** — a decelerating second derivative, which is the empirical basis for the
desk's "rate-of-change deceleration, level stays tight" regime framing. **A ceiling struck at the 2Q
CY2026 market price on MU's largest agreements caps how much of any FURTHER spot-price acceleration
those specific contracts can pass through** — meaning a slowing *reported* QoQ series is consistent with
**either** genuinely slowing spot demand **or** an unknown share of volume hitting its contractual
ceiling and mechanically stopping contributing to the reported rate, **and the filing does not disclose
enough to tell the two apart.** Symmetrically, the **floor** protects the *downside* of the same
unknown share — which is the mechanism `RESEARCH.md` L2 flagged as an open counter to the peak-margin
trap (**MU margin 84.6% GM, 100th percentile of a 17-year XBRL series, `M143`, 2026-07-25**) and which
management's own 10-Q language ("well above our peak quarterly margins in any past cycle," at floor
pricing) now directly corroborates from the issuer's side, not the desk's inference. **Net: the
contractual band is real, measured on a primary filing, and cuts both ways — it dampens both how far
up and how far down MU's reported numbers can move relative to spot — but its SIZE (the contracted
share) is undisclosed, so it can be named as a contaminating factor on the second-derivative read and
cannot be sized into that read.**

🚨 **Per the run's binding instruction, this section does not write "revisions turn before price does."**
MU's own revision table (`module_fundamentals_us MU`, pulled this run) is cited here **only as a
description of the denominator's direction, not as an independent signal**: current-quarter EPS
consensus 30d breadth **26↑/0↓**, next-year 30d **30↑/0↓**, next-year EPS **90d +53.2%**
(this run's live pull; `STANDING_VIEW M14`'s 2026-07-22 seed measurement was +50.1% over the same
window — the direction has continued, not reversed). **This is reported as where the denominator sits,
not as forward evidence on the memory cycle** — the 2026-08-09 test that killed the "revisions lead
price" framing on IT names governs, and this table is not re-opened as a leading indicator here.

**QoQ revenue, tabulated per L1's own instruction, offered as a proxy with its limits stated**: MU
quarterly revenue **$9.30bn → $11.31bn (+21.6% QoQ) → $13.64bn (+20.6% QoQ) → $23.86bn (+75.0% QoQ) →
$41.46bn (+73.7% QoQ)**, FQ3'25 through FQ3'26. The **QoQ growth rate is roughly flat at an extreme
level (75.0% → 73.7%), not decelerating in the way M1's ASP series is** — but revenue growth mixes
volume, mix and price and is **not a substitute for the ASP series M1 already measures**; it is shown
here only as an independently-pulled check that nothing in MU's own top line contradicts M1's reading,
and it does not resolve which share of the ASP deceleration is contract-band mechanics versus real
demand softening.

## §3 · Value chain — 5 nodes, binding constraint named

| Node | Names (in `us_top300`) | Reading |
|---|---|---|
| **1. AI-accelerator / platform design** | NVDA · AVGO (mega-cap cluster) · AMD · ARM (semi cluster) | Bimodal even within one node: NVDA/AVGO flow-positive and accumulating; AMD/ARM 🔴분산. AMD is also the **body-proximate chain-hop node for CXMT** (§5) |
| **2. Foundry (advanced logic)** | **TSM — not measured, outside universe (hard constraint, not "no signal")** | No US-universe substitute exists for this node; any capex/utilization read is a gap, not a zero |
| **3. Semicap equipment** | AMAT · LRCX · KLAC · ASML | All 🔴 or 🟡; **AMAT −0.911 is the sector's single most negative flow score**. This node prices *future* wafer starts, one to two cycles ahead of node 4's realized ASP |
| **4. Memory (DRAM/NAND) — BINDING CONSTRAINT NODE** | MU · SNDK · WDC · STX | **The take-or-pay ceiling/floor band (§2) sits here.** External entrant **CXMT — not in `us_top300` (unlisted, Chinese) — is a new node-4 supply source the chain has never modelled** (P43); on current evidence (§4 below) it enters at the **client/consumer** sub-segment, not the server/HBM sub-segment this node's contracts price |
| **5. System OEM / buyer / demand anchor** | AAPL (the named CXMT tester) · DELL · HPE. **SMCI — not measured, outside universe** | AAPL is `[settled]` 🟡중립 +0.027, RS20 **−3.1 vs SPY** — the buyer itself is not flow-confirming a shortage-driven pivot this bar |

**Binding constraint, stated once**: node 4's realized pricing for an undisclosed share of volume is
**contractually banded** (ceiling ≈ 2Q CY2026 spot, floor for the contract term), which mechanically
compresses the pass-through from nodes 1–3's demand signal into node 4's *reported* QoQ series by an
amount this filing does not size. Everything downstream of node 4 (software/apps cluster, §1) is priced
off the AI-buildout narrative generally and is the least mechanically linked to this specific
constraint — which is also why that cluster's flow read (+0.219 avg, 16/28 매집) does not move with the
memory cluster's (−0.689).

**Two-node dispersion inside the chain, restated in one line**: node 3 (equipment, forward-priced) and
node 4 (memory, present-priced) are **both negative and directionally aligned (🔴/🔴)** — the divergence
this run is between nodes 1+5 (mega-cap design + buyer, positive-to-flat) and nodes 3+4
(equipment + memory, negative), not between adjacent chain links.

## §4 · CXMT / Apple — Q2, graded honestly

**Claim** `[news — WSJ via aggregators, 43 hits/3d, 5+ outlets, 08-09/08-10; tomshardware body 08-08]`:
Apple is **testing** (not sourcing at volume) CXMT DRAM for iPhone and MacBook, framed by the reporting
as shortage-driven pull; separately, CXMT **cleared DDR5-8800 qualification on an AMD platform**.

**Consumer DDR5 only, or does it reach HBM/AI-server — assessed on the technical content of the claim
itself, `[inferred]` from `[news]` facts, not `[measured]`**: **both named facts point at the
client/consumer segment specifically.** DDR5-8800 is a **JEDEC client/desktop DRAM speed bin**, not an
HBM part — HBM is a physically different product (TSV-stacked dies, wide-I/O, CoWoS-class advanced
packaging integrated directly onto an AI accelerator substrate) with no qualification pathway that
overlaps a "DDR5-8800 on an AMD platform" claim. iPhone and MacBook both consume **mobile/client
memory** (LPDDR-class and client DDR5/SO-DIMM), not server DRAM or HBM. **On the facts as reported, this
is a client-memory-only story; nothing in the two cited items describes a server or AI-accelerator
qualification.** That reading tracks EVENT_ALPHA's own Direction A (~60%, "consumer-DRAM story, M1's
price path unaffected").

**What would have to be true for it to matter to M1's price path**: a **named CXMT HBM qualification at
any hyperscaler or GPU vendor** — the explicit anti-signal already registered against Direction A in
`EVENT_ALPHA` P43. Absent that, the mechanism this card describes cannot reach the node the desk's
regime call actually prices (server/AI DRAM and HBM), even if it is real and growing in its own
(client) lane.

**Grade, stated as instructed**: `[news]`, second-hand via aggregators, **zero issuer filing** — same
grade as `M122`. **Not handed to BET** (already so marked in `EVENT_ALPHA`); this section adds no new
citable evidence, only a technical read of what the existing claim can and cannot mean. **Dated
re-check: 2026-08-19** (carried from `EVENT_ALPHA` Card 3, unchanged).

## §5 · Chain-hop candidates — body-proximate only

**`chain-hop` is not attempted here.** `RESEARCH.md D90` measured it structurally unusable on the US
feed (3-token queries return 0 hits; single-token queries pull in unrelated mega-caps via embedded
market-data tables; `DRAM` collides with a listed inverse-ETF ticker). Using it without that caveat
would manufacture false candidates, so this section is built by hand from what is already body-read in
`EVENT_ALPHA` Card 3, as the desk's stated discipline requires.

- **AMD** — named body-proximate to CXMT's DDR5-8800 qualification (*"cleared DDR5-8800 on an AMD
  platform"*, `[tomshardware body 08-08]`). AMD is **already in `us_top300`** (§1, semi cluster, 🔴분산
  flow −0.589, RS20 **−15.8 vs SPY**) — it is a **platform validator for a client-memory qualification,
  not a memory maker itself**, and its own flow read is negative regardless of this story. **Not
  promoted** — the connection is a qualification credit, not a revenue or demand fact about AMD.
- **No other body-proximate name cleared the bar this pass.** CXMT itself has no US listing and no
  `us_top300` row; it cannot receive a flow cross-check by construction.

## §6 · `D208` — a third instance, already surfaced by PREMORTEM, restated here because the name is IT

> **RULE D6 — exemption, stated with its reason.** This paragraph names an OBV state as the *subject* of
> a producer disagreement, not as evidence supporting a proposition — D6 forbids a C-grade signal from
> carrying a claim alone; the claim here is "two producers disagree," which cannot be written without
> naming both readings, and neither reading is used to support anything downstream.

`BLINDSPOT_PREMORTEM.md §3e` measured, on **PLTR** (the sector's only board-wide top-flow green,
flow **1.000**, RS20 **+33.2 vs SPY**): `SECTOR_FLOW_US.json` (sweep, settled 08-07) reads OBV **매집,
+0.242**; `module_chart --read` reads OBV **중립, +12% slope**. **Class: magnitude disagreement, not a
sign flip** (contrast MPC and PRU in the same table, both of which DO flip sign). Two named producers,
one settled instrument and one independently-computed read, disagreeing on the same name the same day.
**Neither reading is treated as confirmation of anything in this file** — PLTR's own flow strength
already rests on RS20 and vol_surge (1.91), not on OBV alone, and its 60-day base is separately flagged
elsewhere (`BLINDSPOT_PREMORTEM §3c`) as the weakest OBV-confirmation of any 🟢 this run. Carried here
only because IT is this run's DEEP sector and the name belongs to it.

## §7 · Track-KPIs and anti-signals — dated observables

- **MU next earnings: 2026-09-24** (`module_fundamentals_us`, this run's own pull). The 10-Q's RPO
  disclosure (§2) will not be updated before then; **the next opportunity to narrow the "unknown"
  contracted-share figure is that print's own MD&A, not a news item.**
- **Any Apple or CXMT filing/confirmation** (not press) — the sole event that would upgrade Card 3 out
  of `[news]` grade. None exists as of this run.
- **A named CXMT HBM qualification at any hyperscaler** — kills Direction A (§4); absence is not
  evidence of absence, only the standing default.
- **COHR earnings 2026-08-13; LITE earnings 2026-08-12** (one day ahead, precursor read) — both already
  tracked in the 08-08 optical-scoped DEEP file; not re-derived here.
- **STX earnings 2026-08-13** (per this run's constraint sheet) — the fourth storage/memory-adjacent
  print inside one week alongside COHR.
- ⚠ **Anti-signal on the mega-cap cluster's positive read**: NVDA's RS60 is **negative (−3.3 vs SPY)**
  under a positive RS20 (**+3.7 vs SPY**) — this week's strength sits on a soft 60-day base for the
  single largest name in the sector (19.4% of cap). A second confirming sweep is needed before reading
  the mega-cap cluster's +0.359 avg flow as a sustained re-rating rather than a one-week bounce.
- ⚠ **Anti-signal on the memory/equipment cluster's negative read**: **AMAT (−0.911), AMAT RS60 +20.3**
  and **MU RS60 +9.7** both carry **positive 60-day excess vs SPY under negative 20-day and negative
  flow scores** — i.e. the distribution cluster's own longer base is not uniformly weak, only its most
  recent window is. **Do not read the 🔴 cluster as a multi-month breakdown without checking RS60
  individually per name** — several names in it (MU, AMAT, ARM, IBM, KLAC) carry positive RS60 next to
  negative flow scores.

## ✅ EXIT CHECK

- [x] **Q1 answered**: sub-node spread (1.048, top4 vs semi/memory cluster) exceeds the sector's own
      move (eqflow −0.160, wflow −0.008) by 6.5×–130× ⇒ IT is named the wrong unit of analysis, per the
      stage rule, rather than forcing one verdict
- [x] **Q2 answered**: CXMT/Apple assessed as client/consumer-only on the facts as reported (DDR5-8800
      is a client bin, iPhone/MacBook are client/mobile buyers); graded `[news]`, no issuer filing, not
      handed to BET, dated re-check 2026-08-19 carried unchanged from `EVENT_ALPHA`
- [x] **Q3 answered**: MU FY26Q3 10-Q read directly via `module_disclosure_us` → fetched primary filing;
      take-or-pay/ceiling/floor structure confirmed verbatim; **contracted volume share marked `unknown`
      (C3)**, not fabricated; RPO $5.0bn (~3.0% of annualized revenue) given as a stated lower bound
      with its exclusions named
- [x] **"Revisions turn before price does" NOT written**; MU's revision table used only to describe the
      denominator's direction, explicitly flagged as such
- [x] **D6 exemption written in the same paragraph as its flagged text** (§6)
- [x] **C1 (benchmark) named inline on every excess/RS mention in prose** (SPY, throughout)
- [x] **TSM and SMCI marked "not measured"**, never "no signal" (§3)
- [x] **EA not cited** — not an IT-universe name this run
- [x] **Δ and "new 🟢" not cited anywhere in this file**
- [x] **Sweep news-velocity axis not cited**; `module_flow`'s live velocity producer named explicitly
      where used (EVENT_ALPHA Card 3, inherited, not re-pulled here)
- [x] **D208 named with both producers, on the IT name it applies to (PLTR)**, magnitude-only class
      stated correctly (not a sign flip, contrast MPC/PRU)
- [x] **No position sizing, no buy/sell language (P4)**
