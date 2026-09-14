# SECTOR_DEEP_INDU — Industrials — industry_US — 2026-08-07 (Fri) · delta-led, rotation-rule broken

> ⚠⚠ **This slot broke the recency rule, stated rather than smuggled**: INDU was DEEP'd **08-05 AND
> 08-06**, and ROTATION's "recency-starved fallback" (`SECTOR_ROTATION.md`, Rotating 1) invokes it
> anyway **because INDU is the only remaining OW-family sector** — every other candidate is N or worse.
> Working as designed, not an oversight.
> ⇒ **Carried by reference, NOT reprinted.** `llm_outputs/2026-08-06/industry_US/SECTOR_DEEP_INDU.md`
> already resolved EMR-vs-Lens-4 on the primary-filing axis, decomposed the sub-node arithmetic, tested
> M91 against five 10-Ks, and mapped the ERCOT receipt both ways. None re-derived here. This file exists
> for one new question: **electricals or defence?**
> Flow/RS **`asof 2026-08-06 settled`** (`SECTOR_FLOW_US.json`, D74). Benchmark **SPY** inline (C1).
> **Analysis only — zero buy/sell, zero sizing (P4).**

---

## 0 · The mandate answered in one line

**Defence, not electricals — the OW− is better supported by the five-name defence node (broad, positive
revision books, uniform 매집, and a headline substitution risk the primary filings show is structurally
insulated) than by the three-name electrical node, where the names carrying price (EMR, AME) have
flat-to-negative revisions and the one leg with genuine revision acceleration (PWR) is the leg price
abandoned — and by primary-filing customer disclosure only ETN and PWR are actually
AI-datacenter-object-correct.** S62 does not adjudicate this: its basket is pure electrical-vs-utility
and says nothing about defence.

---

## 1 · Delta since 2026-08-06 — five things, numbers only

| # | What moved | 08-06 | 08-07 | Source |
|---|---|---|---|---|
| **D1** | **VST's session timing corrected** | assumed AMC | **printed PRE-MARKET** — `[nasdaq 08-06]`: *"Pre-Market Earnings Report for August 7"*; lands on the exact bar S62 freezes on, plus four more power names (PPL, EMA, AQN, OKLO) `CATALYST_WATCH.json` never carried | PREMORTEM §1 |
| **D2** | **A new bracket defect, D206** | S62 "beyond 85th-pct tail" at registration | Branch A needs **XLU RS20 to move 18.96pp relative in one session** vs a **±0.5%** straddle ⇒ **arithmetically unreachable.** Tonight's near-certain branch-B print is **not** confirmation the bracket earned | PREMORTEM §3c |
| **D3** | **AME's short book is the only 🟢 collapse in the FINRA pull** | not measured | **z −2.03 (5v5 −2.2▼)** — the cleanest B-grade corroborant in the basket, on the name whose revisions are least bad of the three (§2) | ROTATION Rotating-1 |
| **D4** | **EVENT_ALPHA filed an adverse leg on the defence carrier** | not present | **Card 5**: Saudi–Pakistan–Türkiye pact, body-read as a substitution story, against uniform 매집 across all five primes | EVENT_ALPHA Card 5 |
| **D5** | **Electrical carrier's revision book, re-measured on breadth** | flow tags only | **EMR CY +0.7%/90d, CQ 0↑/2↓; ETN CY +1.4%, CQ 3↑/4↓; AME CY +2.2%, CQ 2↑/1↓; PWR CY +19.3%, RS20 −2.3/RS60 −18.5** | PREMORTEM §3b, below |

**Sector line (unchanged framing, current numbers)**: n=50 · **wflow +0.088 / eqflow +0.110** ⇒
breadth-led · breadth **0.120** · Δ **−0.038** · **6🟢 / 11🔴**.

---

## 2 · The electrical carrier tested at the primary level — EMR vs ETN vs AME vs PWR

**Re-pulled `module_business_us --json` for all four (fresh full-text scan, not carried from 08-06);
counts below are on the combined Item 1 + MD&A text.**

| Name | Filing | "data center" hits | "hyperscale" hits | What the primary actually says |
|---|---|---|---|---|
| **EMR** | 10-K, filed **2025-11-10** | **0** | **0** | Zero. Only power language is segment-level: *"Sales for Final Control increased... reflecting strength in power end markets"* — **Final Control is process valves/actuators**, not data-centre gear |
| **ETN** | 10-K, filed **2026-02-26** | **6** | **2** | *"We make products for the data center, utility, industrial…"* — first sentence of Item 1. Fibrebond bought for *"hyperscale data center customers"*; Boyd Thermal for *"data center customers… hyperscale and colocation"* |
| **AME** | 10-K, filed **2026-02-17** | **1** | 0 | One clause in a ~12-item end-market list: power-conditioning products *"for smart grid... and data centers"* |
| **PWR** | 10-K, filed **2026-02-19** | **16** | **2** | ★ **Deepest data-centre language of the four.** *"Build out of data centers by technology customers… to develop AI training and inference"*; names *"hyperscaler, data center colocation"* customers directly; acquisition CEI *"resulted in increased demand... from the technology and data center industry"* |

⇒ **On the customer-disclosure axis, the ranking is PWR > ETN ≫ AME > EMR — the inverse of the flow
tag's ranking (EMR +0.950 🟢, ETN +0.789 🟢, AME +0.726 🟢, PWR −0.151 🟡).** The weakest primary-filing
case (EMR) carries the strongest flow tag; the strongest primary-filing case (PWR) carries none.

**Cross-checked against the revision books** (`module_fundamentals_us`, fresh pull):

| | CY 90d | CQ breadth (30d) | Fwd P/E | RS20 / RS60 vs SPY |
|---|---|---|---|---|
| **EMR** | +0.7% | 🚨 0↑/2↓ | 21.98 | +11.6 / +8.6 |
| **ETN** | +1.4% | 3↑/4↓ | 28.07 | +8.2 / +3.0 |
| **AME** | +2.2% | 2↑/1↓ | 28.20 | +5.7 / +4.3 |
| **PWR** | ★ +19.3% | 2↑/1↓ | 35.15 | 🚨 −2.3 / −18.5 |

⇒ **The three names the tape is buying (EMR, ETN, AME) have estimates within a point of flat; the one
name whose estimates are actually re-rating is the one the tape sold hardest.** Read with the filing
table: **EMR's 🟢 tag describes a process-automation name (08-06 file §2c-iv already isolated
two-thirds of EMR's RS20 to a single common-factor session), not an AI-power name.** ETN and AME are
genuinely in the node by disclosure, but estimates have not caught up to price. PWR is the only name
where filing, acquisition trail (CEI) and estimate book **all** agree — and it is the one de-rated
18.5 points on RS60. That is not confirmation of the electricals thesis; it is a name-level inversion
inside it, extending the 08-06 file's EMR-specific tie-break to all four: the same instrument —
customer disclosure — now separates PWR from the other three the way it separated ETN from EMR.

---

## 3 · The defence carrier tested against EVENT_ALPHA Card 5

**Card 5's claim**: the Saudi–Pakistan–Türkiye pact is headline-bullish for US rearmament but
body-reads as a **substitution** story — Riyadh's reference procurement is Turkish drones (*"Ankara's
largest defence export contract"*), and the pact *"raises big questions on the reliability of
[Saudi's] longstanding US security umbrella."*

**Tested against fresh `module_business_us --json` pulls on all five primes:**

| Name | US-Government share | FMS / international share | Named Saudi programme | Backlog |
|---|---|---|---|---|
| **LMT** | 72% of $75.0bn | **28% intl, 77% of that FMS** (≈21.6% of sales) — **highest FMS exposure** | **MMSC combatant ships; Black Hawk/Seahawk** — named directly | **$193.6bn**, up from $176.0bn (+9.9% y/y) |
| **RTX** | 38% direct + 8% FMS | FMS **$6,702M = 8%** of $88.6bn; DCS +7% | not named | not isolated |
| **GD** | 68% of revenue | **FMS $1,015M ≈ 1.9%** — smallest of the group | not named | 34 backlog mentions, $ not isolated |
| **NOC** | ~86% | **Intl $5,990M ≈ 14.3%** — smallest intl share measured | not named | not isolated |
| **LHX** | majority US government | not quantified here | not named | not isolated |

⇒ **The mechanism Card 5 worries about is government-to-government FMS, and FMS-to-any-single-country
is a low-single-to-low-double-digit share of consolidated revenue across the group** — GD's is under
2%, RTX's is 8%, LMT's (highest, named on two Saudi programmes) is bounded by a 21.6%-of-total
FMS-international figure, most of which is not Saudi. **A precedent sits in RTX's own 10-K**: China
sanctioned an RTX unit over **Taiwan** FMS sales and did not reverse the already-booked backlog — the
closest analogue this filing set offers, and the answer there was no.
**No DSCA notification or 8-K, for or against, was found** in a fresh 60-day foreign-scope search
(`Saudi`, `DSCA`, `Lockheed`, `Raytheon`, OR-mode) — **the kill condition has not fired either way
(C3, `unknown`)**.

**Flow, reproduced against the JSON**: RTX 🟡 +0.606 (RS20 +12.1/RS60 +21.0, Δ +0.410) · LMT 🟡 +0.594
(+10.2/+9.8) · NOC 🟡 +0.344 (+4.4/−0.4, Δ +0.233) · GD 🟡 +0.297 (+1.0/+8.5) · LHX 🟡 +0.406
(−2.4/−8.2, surge 1.31) — **five 🟡, five OBV 매집, zero 🟢**, cross-checked with revision breadth:
**RTX (CQ 30d 13↑/2↓, NY 18↑/1↓) and NOC (CY 30d 16↑/0↓) carry the strongest books; LMT and GD show a
near-term wobble (CQ/NQ negative) inside a positive full-year; LHX is thinly covered (CQ 30d 1↑/1↓).**
⇒ **the substitution risk is real as a narrative and unconfirmed as a fact, on top of a node whose
fundamentals — unlike the electrical node's — are broadly, not narrowly, positive.**

---

## 4 · B2 executed per name

Margin percentile could not be computed for **RTX, NOC, GD, LHX**: `margin_history.py` returns a
stale/pre-merger window for all four (RTX/NOC terminate FY2017, GD FY2019, LHX a 74.2%-discrepant
XBRL row) — a measured tool gap, stated `unknown` (C3), flagged for a human (same class as KR's D70).

| Name | Fwd P/E | Margin percentile | CY revision (90d) |
|---|---|---|---|
| **EMR** | 21.98 | **100th** (52.8% FY2025 = 18-yr high) | +0.7%, CQ breadth negative |
| **ETN** | 28.07 | **~90th+** (37.6% vs 38.2% FY2024 peak) | +1.4%, mild |
| **AME** | 28.20 | **~95th** (36.0% vs 36.1% FY2023 peak) | +2.2%, positive across horizons |
| **PWR** | **35.15** (richest) | **100th** (15.0% ties FY2021 peak) | **+19.3%**, accelerating hardest |
| **RTX** | 28.20 | `unknown` | +4.9%, near-unanimous positive breadth |
| **LMT** | **17.73** (cheapest) | **~30th** (10.2% vs 11.1% median, 14.0% peak — a margin *trough*, not a peak) | +1.7% FY, CQ/NQ negative |
| **NOC** | 18.52 | `unknown` | +3.9%, strong breadth |
| **GD** | 20.84 | `unknown` | +2.0% FY, NQ negative |
| **LHX** | 21.29 | `unknown` | +1.9% FY, CQ/NQ negative, thin coverage |

⇒ **The electrical node is where L2's peak-margin/low-multiple trap actually applies**: EMR, AME and
especially PWR sit at or near an 18-year margin ceiling carrying multiples at or above their own
historical range, with only PWR's estimates confirming it. **LMT is the opposite case** — the cheapest
multiple of either node sits on a margin trough, not a peak, so its low multiple is not manufactured
by a denominator about to fall; its near-term estimate cuts are a separate, real caution on their own
terms.

---

## 5 · W5 — dispersion by sub-node

| Sub-node | Names | Flow / RS spread |
|---|---|---|
| **Electricals** | EMR/ETN/AME/PWR | flow +0.950 to −0.151; **RS20 range 13.9pp, RS60 range 27.1pp** |
| **Defence** | RTX/LMT/NOC/GD/LHX | flow +0.297 to +0.606 (tight); **RS20 range 14.5pp, RS60 range 29.2pp** |
| **Rails** | UNP +0.099·CSX +0.297·NSC +0.414·UPS −0.319·FDX −0.658 | flow spans 🔴 to 🟡, no 🟢 |
| **Freight/airlines** | DAL 🟡 −0.063 (RS60 **+25.2**) · UAL 🟡 −0.369 (RS60 **+29.7**) | ★ **widest RS60/flow mismatch in the sector** — the two best 60-day excess returns in INDU carry negative-to-flat flow: the money that built the move has already rotated out even as the base holds |
| **Machinery** | CAT 🔴 −0.115 (RS20/RS60 both ≈−11) · PCAR 🟡 +0.072 (OBV 분산) | uniformly weak, no 🟢 |

⇒ **B5 binds again**: electricals and defence each carry an internal RS60 range above 27 points against
a sector `wflow +0.088` — **"Industrials" remains the wrong unit**, and within it "the OW− rests on X"
is only answerable node-by-node, which is why this file exists.

---

## 6 · S62 / D206 — what tonight's settle can and cannot establish

**Independently reproduced** (fresh `yfinance` pull, trimmed to the 08-06 settle, D74 honoured):
EMR **+11.626** · ETN **+8.196** · AME **+5.651** · PWR **−2.291** ⇒ median **+6.924**; XLU
**−6.119** ⇒ spread **+13.043** — matches the handed +13.045 to 0.002pp.

**What it CAN establish**: whether the three-name electrical basket and XLU stay divergent through a
session already containing VST's pre-market print plus four more power names the desk's catalyst file
did not carry. A spread holding near +13 is a narrow, genuine read on that rotation surviving a loaded
news day.

**What it CANNOT establish**: **anything about defence.** S62's basket contains zero defence names.
A branch-B settle tonight says nothing about Card 5's substitution risk, and nothing about whether the
INDU OW− as a whole is better read through electricals or defence — that is this file's question, and
S62 was never built to answer it.

**Per D206, the contest itself is compromised**: branch A needs an 18.96pp one-session swing against
XLU's own ±0.5% straddle — **arithmetically unreachable**. Tonight's near-certain branch-B print is the
adversarial branch having **drifted out of reach before settle, not a contest won.** Log it as
**inconclusive by construction**, not as confirmation the split is durable — the exact misreading S62's
own registration text pre-warned against.

---

## 7 · Track KPIs and anti-signals — dated observables

1. **A DSCA/FMS notification to Saudi Arabia, or its absence through 2026-10-06** — Card 5's own kill
   window. A notification ⇒ substitution read is wrong; silence ⇒ neither confirms nor denies.
2. **PWR's estimate book vs its price**: a second consecutive weekly cut to its CY line ⇒ the one
   electrical name with filing AND estimate support loses the estimate leg too. **RS20 back above 0**
   ⇒ the price/filing gap starts closing. Recheck **2026-08-14**.
3. **EMR filing any document naming a data-centre customer or end market** (next 10-K ~Nov 2026; any
   interim 8-K sooner) ⇒ voids §2's tie-break.
4. **LMT's CQ/NQ estimate cuts**: a third consecutive negative revision on either near-term line ⇒
   re-test the margin-trough/cheap-multiple read against a genuine deceleration. Recheck **2026-08-20**.
5. **RTX/NOC revision breadth holding ≥80% positive** at the next 30d pull ⇒ defence's fundamental
   case strengthens further vs. electricals; falling below 50% on either weakens §0's read.
6. **`margin_history.py`'s stale-window defect on RTX/NOC/GD/LHX** — human-gated fix; until closed,
   those four B2 rows stay `unknown`.

**Stated as unmeasured rather than guessed (C3)**: Saudi-specific dollar exposure inside LMT's 28%
international figure · GD/RTX/NOC's exact FMS-to-Saudi dollar figures (only aggregate lines disclosed)
· margin percentiles for RTX/NOC/GD/LHX (tool gap, above).

---

## 8 · Hand-off to BET — names, flow tags, asof dates, no sizing

- **Electricals, ranked by primary-filing object-correctness (not flow tag)**: PWR (deepest data-centre
  disclosure, richest multiple, best revisions, worst price — RS20 −2.3/RS60 −18.5, 🟡, `asof 08-06`) ·
  ETN (second-strongest disclosure, 🟢가속 +0.789) · AME (thin disclosure, best revision breadth of the
  three tape-favoured names, 🟢가속 +0.726) · EMR (no data-centre disclosure, strongest flow tag, dead
  revisions, 🟢가속 +0.950).
- **Defence, uniform tag class**: RTX 🟡 +0.606 · LMT 🟡 +0.594 · NOC 🟡 +0.344 · GD 🟡 +0.297 ·
  LHX 🟡 +0.406 — all OBV 매집, `asof 08-06`, books ranked RTX≈NOC (strong) > LMT≈GD (mixed) > LHX
  (thin). **Card 5's substitution risk is unconfirmed either way** — an open narrative flag, not a
  scored fact.
- **Sub-node context, not fresh candidates**: DAL/UAL's RS60/flow inversion (§5) is worth BET's own
  read, not an INDU call. Rails/machinery carry no signal either direction this run.
- **S62/D206**: do not read tonight's settle as adjudicating electricals-vs-defence — it tests neither
  the defence question nor, per D206, a genuinely two-sided electricals-vs-utilities one.

**No position sizing and no buy/sell language appears anywhere in this file (P4).**

---

*asof 2026-08-07 · flow/RS settled **2026-08-06**, D74 honoured · primary filings re-pulled fresh for
EMR/ETN/AME/PWR/RTX/LMT/NOC/GD · S62 spread independently reproduced at **+13.043** (handed +13.045),
**not re-scored** · margin percentile `unknown` on RTX/NOC/GD/LHX (tool gap) · no DSCA/FMS Saudi
notification found in a 60-day foreign-scope pull, stated as unmeasured rather than assumed.
**Analysis only — zero buy/sell, zero sizing (P4).***
