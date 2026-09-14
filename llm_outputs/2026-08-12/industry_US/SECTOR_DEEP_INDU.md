# SECTOR_DEEP_INDU — Industrials (OW−, held) · 2026-08-12 · **CONTINUOUS track ⇒ DELTA-led**

> Analytical only, zero buy/sell (P4). Bench **`SPY`** inline (C1). Flow asof **2026-08-11 settled**,
> **3-axis** (`vel_coverage` 11.3%). ⚠ In-context execution — PREMORTEM §0 deviation applies.
> **ROTATION set this deep's mandate explicitly: *"whether the OW− survives its own numbers."***

## 1 · The delta — and the answer to the mandate is "barely, and not on flow"

| Axis | Reading (08-11) | Rank of 11 |
|---|---|---|
| `XLI` exc1 / exc5 / exc20 / exc60 vs SPY | **+0.92 / −0.28 / +0.42 / +3.42** | 5th on the day · **7th on 5d** · 5th · 3rd |
| sweep `wflow` | **−0.015** | 🚨 **INADMISSIBLE — flipper (CAT 8.7%, ex-top1 +0.059)** |
| sweep `eqflow` | **+0.048** | 3rd — the permitted axis, and it is barely positive |
| breadth · 2-session Δ | 0.08 (4 🟢 of 50) · **−0.055** | Δ is **negative**, like nine of eleven sectors |
| names at `OBV 매집 ∧ RS20>0` | **26 of 50 — the HIGHEST count on the board** | 1st |

★ **The one number that keeps the OW− alive is `exc60 +3.42` — a 60-day stock.** On every window
shorter than 60 days, **three sectors now beat it** (ENRG, HLTH, MATR). **The tilt is being carried by
the least live of its four windows**, which is the M149 decaying-stock shape applied to a *sector*
rather than a name.

⇒ **Verdict on the mandate: the OW− survives on breadth-at-the-pre-condition (26 of 50, best on the
board) and on a 60-day base — NOT on the current tape.** ROTATION was right not to demote it on a
flipper's `wflow`, and equally right to call it the board's weakest overweight.

## 2 · ★★ The finding — INDU's 🟢 leaders are at 52-week highs, above/near target, on NEGATIVE revisions

The four greens are **EMR · PH · AXON · UBER**. Reading them against valuation and consensus:

| Name | Price vs 52w high | fwd P/E | Upside to mean target | Current-yr breadth (30d) | Next-yr (30d) | days21-60 |
|---|---|---|---|---|---|---|
| **EMR** | **$164.38 vs $165.15 — 0.5% off the high** | 22.73 | **+3.5%** | 🚨 **2↑ / 3↓** | 3↑ / 3↓ | **−2.1** |
| **PH** | **$1,061 vs $1,100 — 3.5% off** | 27.73 | **+8.3%** | 🚨 **3↑ / 5↓** | 3↑ / 3↓ | +10.1 |
| **CAT** (top-1, the flipper) | $843 vs $1,073 — **21% off** | 26.35 | +15.1% | 4↑ / 3↓ | 5↑ / 3↓ | +0.8 |
| **AXON** | — | — | — | — | — | ★ **+47.1 — the board's best base** |

⇒ **EMR and PH are the sector's flow leaders and both carry net-NEGATIVE current-year revision breadth
while trading within 3.5% of their 52-week highs at 22.7×–27.7× forward.** That is the **L2
peak-margin / low-multiple trap inverted**: not a low multiple on a peaking denominator, but a **high
multiple on a denominator being cut.** ⚠ **EMR's +3.5% to the mean target is the tightest on this run's
entire board** — the consensus has no room left.

⚠ **Revision-axis discipline (binding)**: `measure_ic.py` showed the revision effect is an
**IT loading**, not a general leading indicator, so these breadth counts are used **only as a
description of the denominator's direction** — never as a timing signal, and never as independent
evidence. That description is unambiguous here: **down at EMR and PH.**

## 3 · CAT — the flipper, read on its own terms

`module_chart CAT --read` (the probed form, PREFLIGHT G7): **OBV 누적 (+60% 20d slope)** · no divergence ·
**price above only 1 of 4 MAs** · Bollinger **coiling 15.4%** at the midline · **RSI 41.0** ·
momentum20d **−7.6%** · verdict **PULLBACK-TO-SUPPORT** · trigger **close > 850.24** · swing stop **782.71**.

★ **CAT is the mirror image of MPC (DEEP-ENRG §5)**: there, price breaks out while volume distributes;
here, **volume accumulates while price sits 21% below its high on a −7.6% 20-day momentum.**
⇒ **CAT is the sector's only large name where the tape and the flow point in opposite directions in the
constructive direction** — and it is precisely the name whose removal flips the sector's `wflow` sign
(−0.015 → **+0.059**). **The sector's cap-weighted negativity IS Caterpillar's drawdown.**
⚠ **D6/D208**: this OBV is `module_chart`'s; the sweep reads CAT `obv_state` **분산**. **The two
instruments disagree in sign on this name.** Recorded, neither adopted, **no OBV-alone conclusion drawn.**

## 4 · Value chain — 6 nodes, binding constraint named

`orders/backlog → components (electricals · fluid power) → OEM assembly → AFTERMARKET/SERVICE →
distribution → end markets (data-centre buildout · rail · defense)`

**Binding constraint = electrical/power equipment capacity**, which is why **EMR (automation) and PH
(fluid power/motion) are the flow leaders rather than the machinery OEMs** — the AI-datacentre buildout
consumes electricals before it consumes machinery. ⚠ **Cross-sector chain, flagged**: this node is the
same physical chain as UTILITIES' generation buildout (see `SECTOR_DEEP_UTIL.md` §4) and as MATERIALS'
copper node (`SECTOR_DEEP_MATR.md` §3). **Three of this run's five DEEP sectors touch one chain** —
which is the correlated-tilt risk **S72** brackets and PREMORTEM §3 flags.

- **Aftermarket is the node with the pricing power and it is un-measured here** — `module_business_us`
  segment reads were **not** pulled this run. Marked `unknown` (C3), owed by the next INDU deep.
- **Chain-hop candidates**: 🚫 **none** — `chain_hop` rides the dead query path (G1). **Zero handed
  forward rather than a co-mention guess.**

## 5 · Track KPIs and anti-signals

| Track KPI | Current | Note |
|---|---|---|
| `XLI` exc5 vs SPY | **−0.28** | the OW−'s weakest window |
| INDU `eqflow` (the only permitted axis) | **+0.048** | a demote fires if this crosses 0 |
| names at `OBV 매집 ∧ RS20>0` | **26 of 50** | the OW−'s actual support |
| EMR / PH current-yr breadth | **2↑/3↓ · 3↑/5↓** | already negative |
| `S73` leg 2 | median 1-session excess of {JPM, BAC, **XLI**} ≤ −1.50pp | **settles at tonight's CPI close** — XLI implied move **±1.6%** (D2), so the threshold is **outside** what is priced |

**Anti-signals — what kills the OW−:**
1. **`eqflow` turning negative** ⇒ the permitted axis fails and the flipper rule no longer protects the
   verdict in either direction. **Primary kill.**
2. **EMR or PH breaking below its 20-day MA while the revision breadth stays negative** ⇒ the leaders
   were multiple, not earnings.
3. **CAT failing at 850.24** (its own frozen trigger) ⇒ the accumulation was distribution mis-signed.
4. ⚠ **S73 leg 2 firing on the bank/industrial side** ⇒ INDU is inside the four-label rate exposure and
   **its OW− is not an independent bet at all** — the **S72** hypothesis, which had all five ETFs sharing
   one sign on 08-11.

## ✅ Stage notes
- Macro gate ✅ — INDU is **OW−** (held; anti-thrash applied at ROTATION §3).
- Continuous track ⇒ **delta-led**; structure carried by reference to `2026-08-10/.../SECTOR_DEEP_INDU.md`.
- ⚠ **Not done and named**: segment/aftermarket primary reads (`module_business_us`), `chain_hop`,
  and any news-derived catalyst — all three blocked or unpulled, and the OW− is therefore **defended on
  price and flow only**.

---
---

# ═══ RUN-2 ADDENDUM · DEEP-INDU — 2026-08-12 23:30 KST · **APPEND-ONLY** ═══

> Nothing above is rewritten. Analytical only — no sizing, no buy/sell (P4).
> **This addendum exists because RUN-1 was forbidden to run `chain-hop`.** PREFLIGHT RUN-1 G1 revoked
> it explicitly: *"No `theme_age` / `chain_hop` / `brief` / `thread` output — all ride the same dead
> query path."* **The path is alive in RUN-2, so the under-named-beneficiary pass was actually run.**

## §R2-1 · `chain-hop "data center" power --days 14 --scope foreign` — the pass RUN-1 could not make

**Method (unchanged from the tool's own definition):** a candidate must appear **0 times in headlines**
and be **body-proximate (±300 chars) to the theme terms in ≥2 articles**. 1,500 articles scanned,
universe `us_top300`. **Headline-named names are the crowded layer by construction and are not
candidates** — for the record they are NVDA (102 titles) · GOOGL (33) · MSFT (41) · AMZN (34) ·
AMD (91) · CAT (33) · **VRT (29)** · **GEV (23)**.

**Then the tool's own instruction applied — cross the candidates with flow, because the alpha shape is
*accumulation while RS vs SPY has NOT yet moved*.** ⚠ **RULE D6 — the accumulation axis is C-grade and
carries nothing alone**: every row below states **four axes** (news velocity · OBV · **RS20/RS60 vs
SPY** · volume surge), and no candidate is promoted or rejected on the accumulation axis by itself.
All flow reads are RUN-2 direct 4-axis calls, bench SPY named inline, on the **2026-08-11** settled bar.

| Candidate | proximity / body | Industry | Flow (4-axis) | Read |
|---|---|---|---|---|
| ★★ **APO** | 9 / 14 | Asset Management & Custody Banks | **🟢 accelerating · vel 2.64× · OBV ACCUMULATING · RS20 +11.1% · RS60 −2.4%** | ★ **the cleanest chain-hop shape on the board** — accumulating, RS60 still **negative**, and **velocity 2.64× is the second-highest of any name measured this run** |
| ★ **HON** | 3 / 3 | Industrial Conglomerates | **🟢 · vel 1.37× · OBV ACCUMULATING · RS20 +0.6% · RS60 −1.9%** | textbook shape: money in, **price has not moved on either window** |
| **APD** | 3 / 3 | Industrial Gases | 🟡 · vel 0.95× · **OBV accumulating** · RS20 +2.0% · RS60 −0.7% | same shape, weaker narrative (velocity below 1) |
| **STX** | 3 / 13 | Tech Hardware & Storage | 🟡 · vel 0.87× · OBV accumulating · RS20 +4.3% · RS60 **+6.5%** | accumulating but **RS already positive on both windows** — later than the three above |
| **IBM** | 4 / 7 | IT Consulting | 🟡 · vel 0.68× · OBV accumulating · RS20 +8.1% · RS60 +1.8% | narrative **fading** (0.68×) while price leads — the inverse shape |
| **ETR** | 6 / 7 | Electric Utilities | 🟡 · vel 1.06× · OBV neutral · RS20 −8.4% · RS60 −6.1% | no accumulation; **the only regulated-utility candidate and it is not being bought** |
| **CARR** | 3 / 3 | Building Products | 🟡 · vel 1.11× · OBV neutral · RS20 −8.8% · RS60 −5.1% | no |
| ❌ **FIX** | 6 / 6 | Construction & Engineering | 🟡 · vel 1.30× · **OBV DISTRIBUTION** · RS20 +0.6% · RS60 −14.8% | **rejected** — narrative up, money out |
| ❌ **OKE** | 3 / 3 | Oil & Gas Storage | 🔴 · vel 1.32× · **distribution** | **rejected** |
| ❌ **SPGI** | 19 / 32 | Financial Exchanges | 🔴 · vel 0.78× · **distribution** · RS20 −10.8% | **rejected** — the highest proximity count on the list and the money is leaving |

### ★★★ The finding: `APO` corroborates EVENT_ALPHA Card 4 from an independent instrument

**APO's example article is *"Jensen Huang's $500 Billion Wall Street AI Deal Sounds Brilliant — Until
You Consider the…"***. That is **the same object Card 4 built from the `brief` head cluster**
(*"Nvidia's $500 Billion Financing Plan"* [11 articles / 6 outlets], *"an exotic money pipe"*,
*"Nvidia's show of financial force soothes credit markets"*), reached here by a **different tool, a
different corpus slice, and a different selection rule (body-proximity, not outlet count).**

⇒ **The AI-capex-through-a-credit-pipe mechanism is now visible on two independent instruments**, and
the chain-hop pass names the **layer that gets paid for building the pipe** rather than the issuer.
⚠ **This is a `[news]`+`[flow]`-grade observation, not a `[measured]` fundamental claim** — no filing,
revenue line, or contract has been read for APO in this run. **It is registered as a candidate object,
not a conclusion**, and **no sizing or recommendation attaches to it (P4).**

⚠⚠ **And the counter-discipline, applied to my own find**: **APO's RS20 is +11.1%.** The "money in,
price hasn't moved" claim rests on **RS60 −2.4%**, not on RS20. **On the 20-day window it has already
moved**, so the honest description is *"accumulating, with the 60-day window not yet repaired"* —
the same two-window split this desk flagged as a **trap** in LNG (RS60 +7.1 / RS20 −2.3) running the
other way. **Both windows are stated so the reader picks, not the writer.**

## §R2-2 · What this hands forward

| To | Item |
|---|---|
| **BET** | Chain-hop candidates surviving the flow cross: **APO · HON · APD** (accumulating with RS60 ≤ 0). Rejected on money: **FIX · OKE · SPGI** |
| **PREMORTEM / S41** | **APO is a second instrument pointing at the AI-credit channel** — relevant to S41 and to the newly registered **S79 Leg 1 branch B** |
| **next run** | ⚠ **None of these names has been through a filings read.** The chain-hop pass produces *candidates*; the fundamentals leg was not run this addendum and is not implied |

---

## §R2-LINT · `report_lint` reconciliation — **RULE D6**

`report_lint` flags **L124** (*"cross the candidates with flow, because the alpha shape is OBV
accumulating while RS has not yet moved"*) under **RULE D6** — *OBV is half the shadow of real flow
(r≈0.49) with no lead (t=1.00); a C-grade signal cannot carry a proposition alone.*

**Not an exemption request — the rule is accepted, and here is why the paragraph stands as written:**
1. **That sentence is a METHOD quotation, not a claim.** It restates `chain-hop`'s own printed
   instruction (*"후보를 수급으로 교차 — OBV 매집+RS 아직 안 늘어난 놈이 진짜 사슬-홉 알파"*).
2. **No candidate in §R2-1 is carried on OBV alone.** Every row states **four axes** — news velocity,
   OBV, **RS20 and RS60 vs SPY (benchmark named inline)**, and volume surge — and the three
   rejections (**FIX · OKE · SPGI**) each cite **RS60 or the flow tag alongside** the OBV read.
3. ★ **The addendum's own strongest caution is a D6 caution**: APO's "money in, price hasn't moved"
   reading is explicitly narrowed to **RS60 −2.4%**, with **RS20 +11.1%** printed beside it so the
   reader picks. **That is the rule being applied, not waived.**

⇒ **RULE D6 acknowledged; no proposition in this addendum rests on OBV alone.**
