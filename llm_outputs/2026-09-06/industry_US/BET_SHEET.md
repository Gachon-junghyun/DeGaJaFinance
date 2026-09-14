# BET_SHEET — industry_US · 2026-09-06 (Sun) · Stage 9 / L1·BET

> **ONE file, per-sector sections.** Downstream desks glob this exact filename — never split.
> **P4 — sizing language below is influence illustration only. Zero buy/sell recommendation.**
> Flow/positioning are `asof` **2026-09-04**; fundamentals are pulled live this run and are labelled.

## §0 · What this sheet can and cannot be today, stated before anything else

**The tape has produced no new session since the last run** (`asof 2026-09-04`; **Labor Day 09-07**;
next settled close **09-08**). ⇒ **ROTATION issued 0 deltas of 11 attempts**, and this sheet inherits
a candidate funnel whose price inputs are all Friday's.

⇒ **EVENT_ALPHA handed exactly ONE name to §B as CONFIRMED-EARLY: `SLB`.** Everything else on this
sheet is either (a) a DEEP-sector name carried for measurement, (b) a screener setup that has not
cleared a turn, or (c) a ledger row. **A sheet with one fresh candidate is the honest output of a
weekend run**, and §5 files the funnel rather than leaving it unscored.

★★ **And the one fresh candidate has a fundamental leg pointing the other way.** §A-1 is the finding.

### §0a · Thesis-confirmation gate — consulted, and it returns nothing applicable

`REPORT/COMPANY_SCOREBOARD.md` (2026-08-21, `company_batch` run 1) holds **5 rows, all KR**
(036460 · 011200 · 316140 · 028050 · 000660). **Zero US names have a scoreboard row.**
⇒ **No candidate on this sheet is CONFIRMED-by-citation; every one is re-derived, and that is a
coverage gap, not a choice.** ⚠ Cross-checked per the rule that *"no row ≠ no coverage"*:
`module_report_tags show` carries **303 names / 81 reports**, and the US names below do appear there
(`SLB` and `RTX` both have report history) — but **in `industry_US` run outputs, not in a scored
`company_batch` row**, so none carries a verdict · stop · score · dated observation point.
★ **Filed as a standing gap**: `company_batch` has run **once, on KR only**, and every US BET
candidate for six runs has been re-derived from scratch. **`D542`.**

---

## §A · Energy (DEEP, continuous) — the one CONFIRMED-EARLY name, and its two legs disagree

### A-1 · `SLB` (SLB N.V.) — ★ **the sheet's only fresh candidate, and the sheet's sharpest contradiction**

**§A numbers** (live pull this run; XBRL↔yfinance cross-check `4/4 quarters within 0.0%`):

| metric | value | note |
|---|--:|---|
| price | **$57.51** | 52w **$31.64 – $60.46** ⇒ **near the high end of its own year** |
| market cap | **$85B** | live pull, not the stale sweep vector (`G5`) |
| trailing P/E | 28.05 | |
| **forward P/E** | **17.79** | implied forward EPS **$3.23** (verified: 57.51 / 17.79 = 3.233) |
| PEG | 1.51 | |
| P/S · P/B | 2.35 · 3.27 | |
| beta · yield | 0.77 · 2.05% | |
| **consensus mean target** | **$62.03** | ⇒ **+7.9% above spot** (verified: (62.03−57.51)/57.51 = 7.86%) |
| recommendations (30d) | 7 Strong Buy · 19 Buy · 2 Hold · **1 Sell · 1 Strong Sell** | |
| revenue 2026Q2 | **$8.97B, +4.98% YoY** | XBRL-verified |

🚨 **§A-1's finding — the estimate leg is NEGATIVE and BROAD, in the opposite direction to the flow:**

| horizon | 90-day change | **revision breadth (30d)** |
|---|--:|---|
| this quarter | **−9.7%** | **5↑ / 14↓** |
| next quarter | **−7.9%** | 🚨 **2↑ / 17↓** |
| this year | −4.2% | 9↑ / 12↓ |
| next year | −3.4% | 🚨 **6↑ / 18↓** |

⇒ ★★ **The forward P/E of 17.79 is computed on an EPS that is being CUT.** A falling denominator
makes a forward multiple **rise** over time, so **"17.79× forward" is not a cheapness claim and is
not made here** — it is the current arithmetic on a number moving the wrong way.
⚠⚠ **`RULE` — the revision axis is NOT used as a leading indicator.** Measured 2026-08-09
(`measure_ic.py`, its first-ever invocation): two non-overlapping windows disagreed **in sign**
(+0.403 vs −0.299) and the control arm showed the effect is an **Information-Technology loading** —
**ex-IT 120 names gave +0.074 / −0.064 with a Q5−Q1 spread of −1.1pp.** **Energy is ex-IT**, so this
table carries **no independent predictive weight**; it is a **description of the denominator's
direction** and nothing more. **It is reported because the sheet must not present a multiple without
it, not because it forecasts anything.**

**§B narrative / thesis** — *(freshness tag: ALPHA fills)*

The Energy sector's **#1 flow name** (`flow_score` **+0.88**), and **the one green on the whole board
that cannot be a `D537` artifact**: it sits at universe position **173** with **`velocity = None`**,
i.e. **no news axis was available to it**, so it earned the tag on `vol_surge` 1.39 / OBV +0.44 /
rs20 +14.2 alone. **Named beneficiary** of the Venezuela arrangement [*"SLB's Venezuela bet: massive
opportunity or risky gamble?"*, yahoo_finance 2026-08-29]. ★ **`rs20` +14.2 on a NEGATIVE `rs60`
(−2.6)** — the shape of a **new** catalyst rather than a continuing trend.

**§C flow / positioning cross-read**

| instrument | reading |
|---|---|
| sweep | flow **+0.88** · `obv_norm` **+0.44 매집** · `vol_surge` **1.39** · rs20 **+14.2** · rs60 **−2.6** · Δ −0.07 |
| `module_chart` | **CONFIRMED-TURN** · OBV 누적 **+87% 20d slope** · **no divergence** · RSI 64.1 · 3 of 4 MAs · ★ **ignition trigger `close > 57.94` UNFIRED** (spot 57.51, **0.75% away**) · swing-low stop **51.79** |
| `us_flow` `[FINRA 09-04]` | short **4.3% float, COVERING**, DTC 4.6, z **−1.21** ⇒ ✅ **저숏/숏커버 (clean rise)** |
| `module_flow --positioning` | implied move **±3.5%** (expiry 09-11, D5) · P/C OI **0.44** · IV skew **+0.6** ⇒ **complacent, little squeeze fuel** |
| `C25` check | ✅ **the two OBV instruments AGREE** (+0.44 sweep / +87% chart) — unlike `NEM`, which is why `NEM` is not on this sheet |

**§D competition / peers** — inside its own node, `SLB` vs `BKR`: **+0.88 vs +0.31**, a **0.575 flow
spread on n=2** ⇒ 🚫 **"oilfield services" is NOT a node at that dispersion** (`W5`), and no peer
comparison is drawn from it. Cross-node: the refiners (`MPC` +0.69 · `PSX` +0.75 · `VLO` +0.70) carry
**far stronger `rs60`** (+34 to +42) — `SLB` is early where they are extended.

**§E refutation + dated catalyst**

| # | what would refute it |
|---|---|
| R1 | ★ **The estimate leg already refutes the cheapness reading** (§A-1) and is the strongest thing standing against this name |
| R2 | 🚨 **`P139` settles 2026-09-14** and `SLB` is in its **branch-A leg**. The DEEP-ENRG body-read established the Venezuela upstream payoff is **mid-2030s**, which **lowers** branch A's probability ⇒ **the row this name sits inside is more likely to print against it than for it** |
| R3 | **Ignition unfired.** `close > 57.94` has not printed; a CONFIRMED-TURN chart with an unfired trigger is a setup, not an event |
| R4 | **Only +7.9% below the consensus mean** — the thinnest upside-to-target of any candidate on this sheet (`RTX` 16.9%, `MDT` 11.2%) |
| **dated catalyst** | `P139` **09-14** · `S149` (WTI) **09-11** · weekly EIA **09-09** |

⇒ **§E verdict: the name is measured, its two legs disagree, and the disagreement is written rather
than resolved.** Flow, chart, short-pressure and a named catalyst all agree; **consensus earnings
revisions and the target gap both disagree.** ⚠ **No size, no action** (P4).

### A-2 · Carried Energy names — cited, not re-derived

`MPC` (held) · `PSX` (held) · `VLO` · `XOM` · `WMB` · `OKE` · `COP` — numbers in
`SECTOR_DEEP_ENRG §4`, positioning in `MACRO §C`. **Deltas only:**
- 🚨 **`MPC`** carries the sheet's **largest `[FINRA]` 5v5 short build (+8.9)** at an unremarkable
  z (+0.43), IV skew **+42.0** and P/C OI **1.19** on a **09-18** expiry (implied **±6.9%**) —
  **the highest downside fear on the sheet by an order of magnitude.** PREMORTEM Lens 3:
  **EXTENDED-BUT-LIVE** (RSI 76.0, **no divergence**).
- ⚠ **`PSX`** carries a **bearish divergence** `MPC` does not ⇒ Lens 3: **EXHAUSTION-WATCH.**
  ★ **The desk treats these two as one node everywhere; only one of them carries the divergence.**
- **`COP`** is this run's only valid `chain-hop` candidate (23 proximity / 24 body hits, never
  headline-named) — **logged, NOT promoted**: the rule wants OBV accumulating with RS *not yet*
  moved, and `COP`'s rs20 is already **+14.6**.

### A-3 · Energy screener setups — both dropped, with reasons

`us_setup_screener --sector Energy --limit 300` (16-name universe): **2 candidates, both bucket A
(leader pullback), 0 in buckets B and C.**

| ticker | RSI | px/200 | ~50DMA | flow | dropped because |
|---|--:|--:|--:|--:|---|
| `FANG` | 39.1 | +10% | +2% | **+0.43, OBV +0.046 중립** | The setup is a price shape; the flow axis reads **중립, not 매집** ⇒ no confirmation. Filed to the missed ledger |
| `KMI` | 41.7 | +1% | −2% | **+0.17, OBV +0.042 중립, rs60 −7.6** | Same, and weaker: the sector's **second-worst rs60**. Filed to the missed ledger |

---

## §B · Health Care (DEEP, continuous) — one green, and it sits in the weak node

### B-1 · `MDT` (Medtronic) — carried, not promoted

**§A numbers** (live pull this run):

| metric | value | note |
|---|--:|---|
| price | **$94.17** | 52w $73.31 – $106.33 |
| market cap | $120B | live |
| trailing / **forward P/E** | 23.19 / **14.72** | implied forward EPS **$6.40** (verified: 94.17 / 14.72 = 6.397) |
| PEG · P/S · P/B | 1.68 · 3.21 · 2.44 | |
| beta · yield | **0.57** · **3.06%** | the lowest beta on this sheet |
| consensus mean | **$104.76** ⇒ **+11.2%** | verified: (104.76−94.17)/94.17 = 11.246% |
| recommendations | 3 Strong Buy · 17 Buy · 9 Hold · 0 Sell | |

★ **The estimate leg is FLAT, not falling** — this quarter **−0.0%**, next year **−0.2%**, breadth
**3↑/2↓ (30d)** on next year. ⇒ **forward 14.72× on a stable denominator is a genuinely different
object from `SLB`'s 17.79× on a falling one**, and the sheet states the contrast rather than ranking
the two multiples against each other.

**§C flow** — flow **+0.928** (the sector's best) · OBV **+0.327 매집** · `vol_surge` **1.47** ·
rs20 **+8.4** · rs60 **+11.2** · **the sector's ONLY 🟢**, earned at universe position 118 with
`velocity = None` ⇒ **also artifact-free** (`D537`). `[FINRA]` z **+1.43**, △정상숏.

**§D peers / node** — 🚨 **`MDT` sits INSIDE the sector's weakest node.** Health Care Equipment (n=8)
is the only multi-name node negative on **both** windows (`eqflow` **−0.044**, `exc5` −1.95, `exc20`
−1.15) while **Biotechnology (n=6, `eqflow` +0.519, 6/6 accumulating, `exc20` +10.56) has ZERO
greens.** ⇒ **the sector's one green is in its worst neighbourhood and its best neighbourhood has
none** — `M1319` reproduced.

**§E refutation + dated catalyst** — `S133` (constituents vs `XLV`) settles **2026-09-14**.
Refutations: (R1) the node it sits in is the drag; (R2) its green depends on `vol_surge` 1.47, an axis
under `C29`; (R3) three same-node peers (`ISRG`, `EW`, `ABT`) appear in the screener as **pullbacks
or de-rates**, i.e. the node's price action is broadly stressed.

### B-2 · Health Care screener setups — 4 surfaced, 4 set aside

| ticker | bucket | RSI | px/200 | node | set aside because |
|---|---|--:|--:|---|---|
| `ISRG` | **B de-rate snapback** | 33.6 | **−21%** | Equipment | The deepest de-rate in the sector — **and it is in the drag node**, so the setup and the node point opposite ways. **Missed ledger** |
| `EW` | A leader pullback | 44.3 | +6% | Equipment | Same node. ⚠ `EW` also carries a **`BROKEN` verdict** in the report-tag ledger. **Missed ledger** |
| `ABT` | A leader pullback | 44.9 | +2% | Equipment | Same node. **Missed ledger** |
| 🚨 **`LLY`** | A leader pullback | 43.4 | +8% | Pharmaceuticals | ★ **The sector's `top1` (19.4%) and its biggest DRAG** — flow **−0.46, OBV −0.15 분산**, and it holds the sector's `wflow` down (+0.098 → ex-top1 **+0.232**). **A price-shape pullback on a name whose flow axis is dispersing is the exact `B.모멘텀only` shape. Rejection ledger, not missed** |

★ **Three of four screener hits are in the same weak node.** That is not four candidates; it is one
node observation seen four times, and the sheet says so rather than listing four names.

---

## §C · Defense (PREMORTEM-promoted DEEP) — an ANALYSIS section, not a candidate section

**Full map in `SECTOR_DEEP_DEFENSE.md`; cited, not re-printed.** The node: **`eqflow` −0.622, 16th of
Industrials' 19 industries, 0 of 10 accumulating, every `rs20` between −4.8 and −10.3**, and
`EW{RTX,LMT,NOC,GD,LHX}` − `SPY` over 5 sessions at **−5.166 = the 7.1st percentile of trailing 252**.

★★★ **A third independent instrument agrees, and it is new to this stage.**
`us_setup_screener --sector Industrials` puts **5 of the 10 defense names in its two most-stressed
buckets**, and the screener knows nothing about flow:

| ticker | bucket | RSI | above 52w low | flow | note |
|---|---|--:|--:|--:|---|
| `LHX` | **C washout** | **19.6** | ★ **+0%** | −0.65 | **AT its 52-week low.** ⚠ Idiosyncratic cause on file: CEO replaced after a conduct investigation [yahoo, 2026-08-17] |
| `GD` | **C washout** | **18.8** | +15% | −0.52 | The node's **worst OBV (−0.44)** |
| `TDG` | C washout | 26.5 | +3% | −0.64 | Aftermarket leg, `rs60` −10.3 |
| `NOC` | C washout | 26.5 | +4% | −0.72 | The only "기존" (previously surfaced) name of the five |
| ★ **`RTX`** (held) | A leader pullback | ★ **21.8** | +32% | 🚨 **−0.79** | **RSI 21.8 in a LEADER-PULLBACK bucket** — i.e. deeply oversold **while still above its 200DMA** |

⇒ **Flow, 5-session excess return VS `SPY` (`RULE C1` — the bench is `SPY`, stated inline; the sign
does not survive a different one), and an RSI/price screener — three instruments with no shared
input — put the same node in the same place.**

### C-1 · `RTX` (HELD) — numbers, and the sheet's second contradiction

| metric | value | note |
|---|--:|---|
| price | $200.79 | 52w $150.61 – $226.88 |
| market cap | **$271B** live | ⚠ the sweep's stale vector says **$250B** (`G5`, 53 days) |
| trailing / **forward P/E** | 35.35 / **25.56** | implied forward EPS **$7.86** (verified) |
| **PEG** | **2.34** | ⇒ **not cheap on any reading — the `L2` peak-margin trap does NOT fire** |
| consensus mean | **$234.82** ⇒ **+16.9%** | the widest target gap on this sheet |
| recommendations | 4 Strong Buy · 11 Buy · 8 Hold · **0 Sell** | |
| revenue 2026Q2 | **$24.71B, +14.49% YoY** | XBRL cross-check **4/4 within 0.0%** |
| ★ **backlog** [10-Q, 2026-06-30] | **$289B total · $119B defense** | defense **+11.2% in six months**; total **1.07× the live market cap** |

🚨 **The contradiction, and it is the mirror image of `SLB`'s:**

| | `SLB` | **`RTX`** |
|---|---|---|
| flow | **+0.88 accumulating** | 🚨 **−0.79 dispersing (node-worst)** |
| 30-day revision breadth (next year) | 🚨 **6↑ / 18↓** | ★ **23↑ / 0↓** |
| FY revision, 90d | **−3.4%** | **+3.9%** |
| upside to consensus mean | +7.9% | **+16.9%** |

⇒ ★★ **Two ex-IT names, both with flow and fundamentals pointing opposite ways — in opposite
directions.** ⚠⚠ **Neither is used as a forecast**: the revision axis has **no independent weight
ex-IT** (Q5−Q1 **−1.1pp**), so this table is **two descriptions of two denominators**, not a ranking.
**Stated because presenting either one alone would smuggle in a prediction.**

**§C flow** — chart: **RSI 21.8**, price at the **lower** Bollinger band, **1 of 4** MAs, OBV 분배
**−35% 20d slope**, momentum **−10.1%**, turn **NEUTRAL/CHOP**, ignition `close > 203.32` **UNFIRED**,
swing-low stop **200.78** (⚠ **above spot** — a `feedback_stop_raise_sanity` shape, and it is why no
stop is quoted as actionable here). `[FINRA]` 1.0% float **covering**, DTC 2.6, implied **±2.1%**
(09-11), P/C OI **0.57**, skew +2.6 ⇒ **안일 (little fuel)**.

**§E refutation + dated catalyst** — **`S150` settles 2026-09-14** (A ≥ +2.902 / B ≤ −3.611, state
**−5.166 already below B** ⇒ **A and C carry the information, B does not**). ★ **The node's real
dated risk is OUTSIDE that window**: the customer's **spending authority expires 2026-09-30**
[`RTX` 10-Q], with a **$1.5tn FY27 request** and a **$67bn supplemental (incl. $21bn munitions)**
pending. **Stated now rather than argued at scoring** (`D450`).

⚠⚠ **§C issues NO verdict on `RTX` and no size.** It is **held**, the node is **n≈1 on five
correlated sessions** (`B3`), and the narrative axis is **empty** (0 of 44 alive threads). **The book
flag raised at `EVENT_ALPHA §3` stands; `S150` is the instrument that settles it.**

### C-2 · The other four primes — **NOT candidates, and NOT rejected**

`GD` · `LHX` · `NOC` · `TDG` are **measurement subjects inside `S150`'s basket** (`GD`/`LHX`/`NOC`
are; `TDG` is not — see `SECTOR_DEEP_DEFENSE §7`). ⚠ **Filing a rejection on a name that is currently
inside a live bracket's observable would double-count the same judgement**, so they are neither
promoted nor ledgered. **`S150` is their record.** Stated so the funnel is not silently short four
names.

---

## §D · Cross-sector LIVE shortlist — the names from outside the DEEP sectors

`US_LIVE_SHORTLIST.json` carries **11 names**. `SLB` (§A) and `MDT` (§B) have sections above.
The remaining **9**, each with an explicit disposition:

| ticker | sector | flow · OBV · rs20 | `[FINRA]` | disposition |
|---|---|---|---|---|
| `DELL` | IT | **+1.00** · +0.25 매집 · +15.9 · surge **2.48** | −0.46 △ | **DROPPED — sector, not name.** IT is `N` with `W5` barring any IT-wide verdict at a 20.07pp sub-node spread; `DELL` is the node's only green and its **Δ is exactly 0.000**. **Missed ledger** |
| `DE` | Industrials | +0.91 · +0.18 매집 · +12.1 · surge 1.44 | −0.47 △ | **DROPPED — contradicts its own sector** (`INDU UW−`, 33/50 negative on `exc5`). ⚠ **DTC 5.1, the highest days-to-cover on the sheet.** Carried recheck **09-19** |
| `CTVA` | Materials | +0.86 · +0.27 매집 · +14.8 | −0.23 △ | **DROPPED — `MATR N` and `P102` settles 09-09.** Acting three days before a bracket that asks whether Materials is two names would make that row unscoreable-as-designed (`D343`) |
| `TSLA` | Cons. Disc. | +0.83 · +0.17 매집 · +8.2 | +1.19 △ | 🔴 **Standing rejection `K.본문반증`, recheck 09-19** — a 🟢 on three failing measured axes (sector `eqflow` −0.280 with 21/28 negative, own `rs60` −13.4, and a body-read that refutes its headline: Cybercab launch → NHTSA probe within 24h). **Surfaced, not overturned** (`D463`) |
| `HOOD` | Financials | +0.78 · +0.21 매집 · **+31.3** · rs60 +35.2 | −0.64 ✅ | ⚠ **EXHAUSTION-WATCH** (Lens 3): CONFIRMED-TURN and OBV +80%, **but a bearish divergence with the band EXPANDING at the upper edge**. Its sector was promoted `UW→N` two sessions ago. **Missed ledger, recheck 09-11** |
| `WMB` | Energy | +0.77 · +0.15 매집 · +5.7 · **Δ +0.35 (sector's largest)** | −1.16 ✅ | **Carried in §A-2.** Green earned at position 129 with `velocity = None` ⇒ artifact-free. ⚠ `rs60` **−3.6** |
| `CVX` | Energy | +0.66 · +0.37 매집 · +12.2 | +0.78 △ | 🚨 **Its 🟢 TAG is partly a `D537` artifact** (position 34, `velocity` 1.46, `vol_surge` **0.99** — below the gate). **Its 3-axis `flow_score` is not.** Cited on the score, never on the tag. Named Venezuela beneficiary; inside `P139`'s branch-A leg |
| `RSG` | Industrials | +0.63 · +0.16 매집 · +4.2 | **+2.61** ⚡ | ⚡ **crowded-short (squeeze fuel, turn-conditional — NOT a buy signal on its own).** The only ⚡ on the shortlist. `INDU UW−` sector. **Missed ledger** |
| 🚨 `PG` | Cons. Staples | +0.23 · +0.12 매집 · **+0.8** · surge **0.89** | −0.55 ✅ | 🚨 **EXCLUDED AS AN ARTIFACT, not dropped on merit.** `PG` flipped 🟡→🟢 between two runs reading the **same settled session**, on a **news-velocity change alone** (1.13 → 1.26), with `flow_score` 0.231, OBV +0.124, `vol_surge` 0.89 and rs20 +0.8 **all byte-identical** (`D537`). **It is on the shortlist because the tag is broken, and it may not be treated as a candidate in either direction** |

---

## §E · Epicenter-starter module — **not invoked**

`cycle_exposure` reports **no top-rank cycle GAP**: AI-compute epicenter **17.48%** (bar ≥12%),
Energy/refining **10.47%** (bar ≥8%), missile-defense 3.64% (no bar set). ⇒ **the starter module does
not fire.**

⚠⚠ **But PREMORTEM Lens 4 established that ✅ here means "not measured," not "covered," and this
sheet carries that forward rather than accepting the green:**
1. **The AI-power cycle is not in `cycle_registry.json` at all** (`M1308`, 3rd run), so its absence
   reads ✅. The lane's money is in **generation** (`CEG` +0.64, `VST` +0.62, both 매집, **both blocked
   from this sheet by `vol_surge` alone**) and the book's only holding is **`ETN`, the lane's single
   distributing name** (−0.66 🔴, rs20 −8.0). **`S146` settles 09-14.**
2. **The rank-1 cycle's held epicenter is on the non-accumulating side of its own node** — `NVDA`
   OBV −0.08 분산, `ANET` 중립 with `vol_surge` 0.60 (its tag *cannot* fire), `AVGO` −0.45 분산 with
   rs20 −15.9 — **while storage/memory, carrying the board's two largest Δflows (`STX` +0.73,
   `WDC` +0.72), is 0% of the book.** `S145` settles **09-11**.
3. **The rank-3 cycle (missile-defense) has NO bar set**, so the GAP check is silent on it **at the
   exact moment its node printed a one-year extreme** (`M1374`, §C).

⇒ **No starter is proposed** (P4, and there is no GAP to answer). **The three items above are handed
to ALPHA as the reasons the ✅ should not be read as coverage.**

---

## §F · Sizing language vs the carried exposure state

**HANDOVER §6 carried**: KR contest book verdict **정상**, target **95%**, **current % BLANK today**
(account query failed, `M1358`), stored `show` value **85.2%**, band gap **−9.8pp**, cumulative
**−9.79pp = cash −5.32 + selection −4.47**, **n=18 and stalled 5 days**. Real KIS book: **52.3% cash**,
no cycle GAP.

- **The state is `정상`, not `복귀`**, so the sheet is **not** under an obligation to supply enough
  candidates to reach a target.
- ⚠ **And it could not be if it were.** This sheet has **one** fresh candidate. **If the state were
  `복귀`, this run would have to say plainly that it cannot fill it** — which is stated here
  conditionally so the next run inherits the answer rather than re-deriving it.
- 🚫 **`kelly_size --ic` is not used anywhere on this sheet.** PREFLIGHT `G6` FAILED (accrual
  **0.55/day = 1.8× slow**) and any `--ic` output would have to be labelled **"mechanical 1/4"** with
  no IC claim. **It is simply not invoked.**
- ⚠ `exposure_rule` prints **🚨🚨ARMED (`TIMEFOLIO_EXECUTE=1`)** on all 48 ledger rows. Recorded
  because it is on the instrument's own output. **This run issues no order of any kind.**

---

## §G · Funnel scoring — the ledger writes this stage performed

⚠ **The EXIT CHECK requires that a multi-name sweep produce rejections and/or missed entries.**
This run's funnel: **299 swept → 11 shortlisted → 8 EVENT_ALPHA cards → 1 CONFIRMED-EARLY.**

**Written at EVENT_ALPHA (5 missed + 2 reject)** — `NEM`, `AMD`, `CEG`, `VST`, `XOM` (missed);
`GEV`, `PWR` (reject). **Written at BET (this stage):**

| ledger | ticker | class | recheck | condition |
|---|---|---|---|---|
| **reject** | **`LLY`** | `B.모멘텀only` | **2026-09-14** | revives if `flow_score` > 0 **AND** OBV turns 매집 on a settled close |
| missed | `FANG` | `M.숏리스트탈락` | 2026-09-14 | enters if OBV turns 매집 with rs20 > 0 |
| missed | `KMI` | `M.숏리스트탈락` | 2026-09-14 | enters if OBV 매집 **and** rs60 > 0 |
| missed | `ISRG` | `R.타이밍대기` | 2026-09-14 | enters if the Equipment node's `eqflow` turns positive **and** its own OBV turns 매집 |
| missed | `EW` | `M.숏리스트탈락` | 2026-09-14 | same node condition + its own OBV 매집 |
| missed | `ABT` | `M.숏리스트탈락` | 2026-09-14 | same |
| missed | `DELL` | `S.테마회피` | 2026-09-11 | enters if `S145`/`S140` resolve IT's sub-node question and `DELL`'s Δ turns positive |
| missed | `HOOD` | `Q.확신부족` | 2026-09-11 | enters if the bearish divergence clears with OBV still 누적 |
| missed | `RSG` | `Q.확신부족` | 2026-09-19 | enters if the crowded short covers **and** the turn confirms |

★ **`LLY` is a REJECTION, not a miss, and the boundary is deliberate**: a reason was stated (a
price-shape pullback on a **dispersing** flow axis) and the name was set aside on it. Everything else
above never reached a stated reason — it was filtered.

⚠ **`TSLA`, `CTVA`, `DE`, `CVX`, `WMB`, `PG` are NOT filed** — `TSLA` and `DE` carry **live** rejection
rows (09-19); `CTVA` is deferred by `D343` to `P102` (09-09); `CVX` and `WMB` are carried in §A;
**`PG` is an instrument artifact and filing it either way would record a judgement nobody made.**
🚫 **`missed_ledger add` refuses any ticker×date already in the rejection ledger (exit 1)**, so the
boundary is machine-enforced, not a judgment call.

★ **No name was removed on narrative grounds while its measured flow still passed.** The one name
that fits that pattern — `GEV` (narrative BUILDING, flow −0.19) — was **re-filed as a
thesis-rewrite** at EVENT_ALPHA with a new thesis line and a dated recheck, **not deleted** (the
475150 precedent: two narrative rejections cost **+41.2pp** and **+26.9pp**).

---

## ✅ EXIT CHECK — BET

- [x] **Company scoreboard consulted BEFORE any re-derivation** (§0a). It holds **5 rows, all KR** ⇒
      **zero applicable rows**; every candidate is re-derived and **that gap is filed as `D542`**,
      with the *"no row ≠ no coverage"* cross-check run (`module_report_tags`: `SLB`/`RTX` have
      report history but no scored row).
- [x] **Every DEEP sector has a section** (§A Energy · §B Health Care · §C Defense), and the
      **cross-sector LIVE shortlist names each carry an explicit disposition** (§D, all 9).
- [x] **Numbers cross-checked**: every derived figure re-computed independently — `SLB` +7.86%,
      `MDT` +11.246%, `RTX` +16.948%, backlog growth +11.215% / +7.836%, backlog/RPO 3.336×, and the
      three implied forward EPS (3.233 / 6.397 / 7.856) all reconcile. **Blanks are blanks**: peer
      backlogs, contracted throughput share and `HCA` capex are marked `unknown` (`C3`), not guessed.
      ⚠ **A stale-vs-live market-cap discrepancy was found and corrected in-run** (`RTX` $250B stale
      vs $271B live ⇒ backlog/mcap 1.16× vs **1.07×**; the live figure is used).
- [x] **Flow/positioning cross-read present per candidate** (§A-1 §C, four instruments each);
      **BET_SHEET.md written as ONE file** with per-sector sections.
- [x] **Every set-aside name is in a ledger with a class AND a `--revives-if` / `--enters-if`
      condition AND a recheck date** (§G — 9 rows this stage, 7 more at EVENT_ALPHA). No permanent
      bans were filed.
- [x] **No name removed on narrative grounds alone while its flow passed** — `GEV` was **re-filed**
      as a thesis-rewrite, not deleted (§G).
- [x] **Names that surfaced upstream but never reached a rejection are in `missed_ledger`** (§G).
      **The funnel is scored: 299 → 11 → 8 → 1**, with 16 ledger rows across two stages.
- [x] **Sizing language is consistent with the carried exposure state** (§F): state is `정상`, so no
      fill obligation; **and the sheet states plainly that it could not fill a `복귀` target with one
      candidate** rather than leaving that discoverable only next run. `kelly_size --ic` **not
      invoked** (G6 FAIL).
- [x] Linter run — result appended below.

---

## 📋 Stage run log — open decisions resolved without a human

1. **Whether `SLB` survives its own §A numbers** — resolved as **keep it on the sheet with the
   contradiction written out**, not drop it. The flow, chart, short-pressure and catalyst legs all
   agree; the estimate and target legs disagree. **P4 forbids a size either way**, so the useful
   output is the disagreement, dated to `P139` (09-14).
2. **Whether `GD`/`LHX`/`NOC`/`TDG` get ledger rows** — resolved as **no**: three of the four sit
   inside `S150`'s live observable, and filing a rejection on a name inside a live bracket would
   double-count the same judgement. **`S150` is their record**, and §C-2 says so.
3. **Whether `PG` counts as a Staples candidate** — resolved as **excluded as an instrument
   artifact**, and **not ledgered in either direction**, because filing it would record a judgement
   nobody made.
4. **Whether to file the four Health-Care screener hits as four names** — resolved as **file them,
   but state that three of four are the same node observation**, so the count is not read as breadth.

---

> **Linter** (`scripts/report_lint.py`, C1·C2·S6·D6): **0 findings** after one fix (a `SPY` benchmark
> named inline in §C). **`module_math_check`: ALL MATH CHECKS PASSED.**
> ⚠ Both are form checks. A clean lint and a clean arithmetic pass do not make the sheet correct —
> §A-1 and §C-1 each carry a contradiction this stage could not resolve, and says so.

---

# §B · ALPHA freshness tags — filled by Stage 10 / L1·ALPHA (2026-09-06)

## §B-0 · 🚨 The pipe was falsified BEFORE the freshness verdict, and it is alive

`preflight` `G1` **FAILED on the sweep axis** (`vel_coverage` 16.72%), and the rule is explicit: when
`G1` fails, **ALPHA may not issue a freshness verdict at all** unless it establishes the pipe
independently. **Run at ALPHA time, after every other news call this run:**

| probe | count |
|---|--:|
| `fts search NVIDIA --days 7 --scope foreign --count` | **3,860** |
| `fts search Tesla --days 7 --scope foreign --count` | **808** |
| `fts search oil --days 7 --scope foreign --count` | **3,188** |

⇒ **3/3 alive. The direct path is working and every `theme-age` reading below returned a real age and
a real base.** The 16.72% is the sweep's own burst outage (`D502`), not the index. **The freshness
verdict below is therefore admissible**, and this paragraph is the reason it is.

## §B-1 · Novelty — 🟢FRESH fires ZERO for a 13th run, and **one leg of the gate passed for the first time**

`theme-age --scope foreign`, 90d, direct calls this run:

| theme | verdict | age | 7d avg | **accel** | base | bets it carries |
|---|---|--:|--:|--:|--:|---|
| ★ **`Venezuela`** | 🟡 **ACCELERATING** | ≥90 | 63.9 | ★★ **2.95×** | 1,562 | **`SLB`** · `CVX` · `XOM` |
| `payrolls` | ⚪ECHO | ≥90 | 82.7 | 1.89× | 2,600 | (macro) |
| `rate hike` | ⚪ECHO | ≥90 | 178.9 | 1.74× | 7,570 | (macro) |
| `heavy crude` | ⚪ECHO | ≥90 | 4.7 | 1.55× | 140 | `MPC`/`PSX`/`VLO` — ⚠ base 140, thin |
| `gas turbine` | ⚪ECHO | ≥90 | 11.0 | 1.39× | 498 | `VST`/`CEG`/`GEV` |
| `OPEC` | ⚪ECHO | ≥90 | 25.3 | 1.27× | 1,322 | Energy-wide |
| `oil tanker` | ⚪ECHO | ≥90 | 16.0 | 1.20× | 1,168 | Energy-wide |
| `Iran` | ⚪ECHO | ≥90 | 331.7 | 1.09× | 21,747 | Energy-wide |
| `data center` | ⚪ECHO | ≥90 | 311.9 | 0.99× | 19,799 | `DELL`/`VST`/`CEG` |
| `Strait of Hormuz` | ⚪ECHO | ≥90 | 133.1 | 0.94× | 9,118 | Energy-wide |
| `credit spread` | ⚪ECHO | ≥90 | 7.9 | **0.74×** | 753 | (`P128`, macro) |
| **`refining margin`** | ⚪ECHO | **80** | 4.0 | ★ **0.65×** | 315 | **`MPC`/`PSX`** |
| **`distillate`** | ⚪ECHO | ≥90 | 17.0 | ★ **0.64×** | 1,346 | **`MPC`/`PSX`** |

★★★ **`M1378` — the F1 zero is now measured as DOUBLY arithmetic, and one leg passed for the first
time in 13 runs.** The gate requires **age ≤14d AND accel ≥2×**. Historically the desk has explained
the zero with the **age** leg alone (*"a theme old enough to have a name cannot be FRESH"*, `M1323`).
**Today the ACCELERATION leg passed** — `Venezuela` at **2.95×**, against a prior maximum of **1.95×**
(`robotaxi`, 09-05) across every foreign `theme-age` table this desk has produced.

⇒ ★★ **`D543`** [registered here]: *`theme-age`'s AGE leg measures the age of the WORD, not the age
of the EVENT.* **`Venezuela` scores age ≥90 because the country has been in the news for decades —
while the deal driving the 2.95× is EIGHT DAYS OLD** (first carried 2026-08-29). ⇒ **the gate cannot,
by construction, ever mark a new event on an old proper noun as FRESH**, which covers most
macro-driven supply shocks. **This is a specific, fixable defect** — age should be measured on the
*burst onset*, which the tool already computes elsewhere — **and it is a better explanation of 13
consecutive zeros than "no fresh themes exist."**

🚨 **`M1379` — and the theme behind the book's largest-conviction position is still the most
decelerating on the sheet, a 4th consecutive run.** `distillate` **0.64×** (base 1,346) ·
`refining margin` **0.65×** (base 315, age **80** — the youngest theme measured) · while the physical
print sits at the **95.6th percentile**. ⇒ **every Energy tag below is capped at 🟡 for this reason
alone**, and an ECHO-and-decelerating thesis needs *stronger* live evidence to survive.

## §B-2 · The tags

| name | tag | evidence label + date | residual / stamp |
|---|:--:|---|---|
| ★ **`SLB`** | 🟡 **PARTIAL** | flow `SECTOR_FLOW_US.json` **09-04** (+0.88 sector #1, OBV +0.44 매집, surge 1.39, rs20 +14.2 / rs60 **−2.6**) · chart **09-06** (CONFIRMED-TURN, OBV +87%, no divergence) · `[FINRA 09-04]` z **−1.21** covering · theme `Venezuela` **2.95× ACCELERATING** 09-06 | ⚠⚠ **TWO residuals, and the second is new this run.** ① **Ignition UNFIRED** at `close > 57.94` (spot 57.51, **0.75% away**). ② 🚨 **The estimate leg is CUTTING and broad — next-year breadth 6↑/18↓, −3.4%/90d** — so the forward 17.79× sits on a falling denominator. ⚠ **Momentum-only? NO** — RS *and* accumulation agree; but the accumulation read is **C-grade (OBV only)** and the US has no investor-type feed (`D6`). ⚠ Only **+7.9%** below the consensus mean, the thinnest on this sheet. **Re-check 2026-09-14** (`P139`) |
| **`MPC`** (held) | 🟡 **PARTIAL** | flow **09-04** (OBV +0.621 매집, rs20 +30.8) · crack settles **09-04** (distillate 95.6th pctile) · theme `distillate` **0.64× ECHO** 09-06 | Residual carried unchanged: the narrative leg is absent and decelerating (4th run). 🚨 **Positioning stamp: shorts BUILDING, 5v5 trend +8.9 — the largest build on the sheet — IV skew +42.0.** 🚨 **Insider stamp: Form 144 at 4.2× base** (`M1312`, not re-measured — no new session). ★ **Lens-3 re-tag: EXTENDED-BUT-LIVE** (RSI 76.0, **no divergence**). **Re-check 2026-09-14** (`P136`+`S147`) |
| **`PSX`** (held) | 🟡 **PARTIAL** | same, **09-04** · shorts covering, skew +0.1 | ★ **NEW this run, and it splits the pair the desk treats as one node:** `PSX`'s chart carries a **BEARISH DIVERGENCE** (price higher high, RSI lower high) that `MPC` does not ⇒ **Lens-3 re-tag: EXHAUSTION-WATCH.** ⚠ Insider 144s at **2.9×** base. **Re-check 2026-09-14** |
| **`RTX`** (held) | 🟡 **PARTIAL** | flow **09-04** (🚨 **−0.79, node-worst**, OBV −0.29 분산, rs20 −9.6 / **rs60 +7.0**) · chart **09-06** (RSI **21.8**, lower band, 1/4 MAs, OBV −35%) · screener **09-06** (A-bucket, RSI 21.8) · 10-Q **07-23** | 🚨 **Residual is a NODE, not a name**: `EW{RTX,LMT,NOC,GD,LHX}` − `SPY` at the **7.1st percentile of a year**, 0 of 10 accumulating, and **ZERO narrative carriage** (0 of 44 alive threads). ⚠ **Momentum-only? NO — both axes agree negative.** ⚠ **`B3`: ten names on five correlated sessions is n≈1.** ★ Counter-evidence on file: **defense backlog $119B, +11.2%/6m**, revisions **23↑/0↓**. **Re-check 2026-09-14** (`S150`) |
| `CVX` | 🟡 **PARTIAL** | flow **09-04** (+0.66, OBV +0.37 매집, rs20 +12.2) · theme `Venezuela` **2.95×** | 🚨 **TAG-ARTIFACT STAMP: its 🟢 is partly a `D537` artifact** (position 34, `velocity` 1.46, `vol_surge` **0.99 — below the 1.2 gate**). **Cited on `flow_score`, never on the tag.** Named Venezuela beneficiary, inside `P139`'s branch-A leg — which the DEEP body-read made **less** likely. **Re-check 2026-09-14** |
| `WMB` | 🟡 **PARTIAL** | flow **09-04** (+0.77, OBV +0.15 매집, **Δ +0.35 = the sector's largest**) · green earned at position 129 with `velocity = None` ⇒ artifact-free | Residual: **`rs60` −3.6** — the Δ is 20-day and the 60-day is still negative. **Re-check 2026-09-14** |
| `COP` | 🟡 **PARTIAL — watch only** | `chain-hop "Venezuela"` **09-06**: **23 proximity / 24 body hits, title 0** · flow **09-04** (+0.64, OBV +0.222 매집, rs20 +14.6) | **Residual: the chain-hop rule wants OBV accumulating with RS NOT YET moved, and `rs20` is already +14.6.** ⇒ a valid candidate whose alpha shape has partly passed. **Not promoted. Re-check 2026-09-14** |
| `MDT` | 🟡 **PARTIAL** | flow **09-04** (the sector's only 🟢: +0.928, OBV +0.327, surge 1.47) · fundamentals **09-06** | Residual carried: **it is the strong name inside the sector's WEAK node** (Equipment, `eqflow` −0.044). ★ **New supporting number**: its estimate leg is **FLAT** (next year −0.2%, breadth 3↑/2↓), so forward **14.72×** sits on a **stable** denominator — a materially different object from `SLB`'s. **Re-check 2026-09-14** (`S133`) |
| `STX` · `WDC` | 🟡 **PARTIAL** | flow **09-04** (Δ **+0.73 / +0.72 = #1 and #2 of 299**) | ⚠ **MOMENTUM-ONLY FLAG carried unchanged** — RS/Δ green, accumulation **NEUTRAL** (`obv_norm` +0.03 / −0.04). Per `D6` a **C-grade disagreement downgrades to 🟡 and is reported as a disagreement**; it does **not** convert either into a tape trade. 🚨 `STX` shorts **BUILDING 4.1%, P/C OI 7.13**. **Hard-stop required. Re-check 2026-09-11** (`S145`) |
| `MU` | 🟡 **PARTIAL** | flow **09-04** (OBV +0.19 매집, rs20 +16.2) · *"Spot Memory Prices Are Running 4 Times Contract Prices"* **5 outlets, 09-05** | 🚨 **Residual unchanged and now CHALLENGED FROM OUTSIDE**: the contracted share is still `unknown` (`C3`), and a 5-outlet trade-press claim that spot runs 4× contract **argues the deceleration is arithmetic** — but **a trade-press ratio does not convert an `[inferred]` carry into a `[measured]` one**. **Re-check 2026-09-30** (its own print, 16:00 ET) |
| 🔴 **`LLY`** | 🔴 **RESOLVED — dropped + ledgered THIS RUN** | screener **09-06** (A-bucket pullback, RSI 43.4) vs flow **09-04** (**−0.46, OBV −0.15 분산**, rs20 −2.7) | **Rejection row filed** (`B.모멘텀only`, revives if *"flow_score > 0 AND obv_state turns 매집 on a settled close"*, recheck **2026-09-14**). ★ It is also the sector `top1` **holding the sector down** (+0.098 → ex-top1 +0.232) |
| 🚫 **`PG`** | 🚫 **TAG REVOKED — not a 🟢, and not a 🔴 either** | flow **09-04** identical to 09-05 on every scored axis; **only `velocity` moved (1.13 → 1.26)** | 🚨 **`D537`: the 🟢 was issued by a news axis `flow_score` had already dropped.** ⚠ **Deliberately NOT ledgered in either direction** — a rejection or a missed row would record a judgement nobody made about the company. **The revocation IS the record, and this line is it** |
| `MRK` · `VST` · `CEG` · `HOOD` · `DE` · `CTVA` · `SNDK` · `VLO` · `TSLA` · `RSG` · `ETN` | **carried unchanged from 2026-09-05** | no new session ⇒ no axis moved | ⚠ **Re-stating them would be manufacturing evidence.** Their tags, residuals and re-check dates stand verbatim in `llm_outputs/2026-09-05/industry_US/BET_SHEET.md §B-3` and are carried by **name**, not by sector (§B-3) |

**Tally this run: 🟢LIVE 0 · 🟡PARTIAL 10 · 🔴RESOLVED 1 · tag-revoked 1 · carried-unchanged 11.**
⚠ **Zero 🟢LIVE.** Unlike 09-05 — which issued one on a **ledger-condition** resolution (`MRK`) — no
ledger condition matured this run, because **no settled session existed for one to mature against.**

## §B-3 · Carry-forward — tags follow the NAME, not the sector's turn

Measured origin: `006360` carried an ALPHA tag with +64.40% consensus upside, its sector rested, and
**+12.3% over five sessions went untracked.** Every tagged name is handed to the next run's
inheritance packet **regardless of whether its sector holds a DEEP slot**:

**2026-09-09** `CTVA` · **09-11** `STX`, `WDC`, `HOOD` · **09-14** ★`SLB`, `MPC`, `PSX`, ★`RTX`,
`CVX`, `WMB`, `COP`, `MDT`, `VST`, `CEG`, ★`LLY` (revival check) · **09-19** `SNDK`, `DE`, `VLO`,
`TSLA`, `RSG` · **09-30** `MU`.
🚫 **`PG` is on no list** — its tag was revoked as an instrument artifact, and re-checking an artifact
on a date would give it a standing it never earned.

## ✅ EXIT CHECK — ALPHA

- [x] 🚨 **The pipe was falsified BEFORE any freshness verdict** (§B-0, 3/3 alive at ALPHA time). `G1`
      FAILED on the sweep axis, so this step was mandatory, and the verdict is admissible because of it.
- [x] **Every §B tag filled with an evidence label + date**; the one 🔴 (`LLY`) is **dropped AND
      ledgered** with a reason class, a `--revives-if` condition and a `--recheck-date`.
- [x] **Every 🟡PARTIAL carries an explicit re-check date**, and **every tagged name is listed for
      carry-forward independently of its sector's DEEP slot** (§B-3).
- [x] **Momentum-only and positioning flags stamped where they apply**: `STX`/`WDC` momentum-only with
      **hard-stop required** and the `D6` C-grade downgrade stated; `MPC` shorts-building + skew +42.0;
      `STX` shorts-building + P/C 7.13; `RSG` ⚡crowded-short (carried).
- [x] **(US) `ACTION_TICKETS.md` written** — see its own addendum for the `D518` reconciliation.
- [x] **Names that received no tag are recorded** — `PG`'s tag is **revoked with the reason**, and the
      revocation is the record; every other untagged name that surfaced upstream is in a ledger (§G).
