# SECTOR DEEP DIVE — Information Technology (PROMOTED 4th slot)

**Asof: 2026-07-22 close** (SECTOR_FLOW_US.json). The 2026-07-23 US session was not open at run
time (~09:1x ET) — nothing below is intraday. INTC has **not printed** as of this writing.
Analysis only. Zero buy/sell recommendations, zero position sizing.

---

## 0. Why this file is a SPLIT, not a sector verdict

The standing desk label for Information Technology is a single **Neutral**. That label is wrong on
**both halves at once**, and the premortem promoted this file to say so with numbers instead of
adjectives.

- **Leg 1 (spenders — MSFT, and GOOGL/META by extension though both are GICS Comm Services, see
  §1)**: deserve **more** underweight, on **multiple compression**, not weak demand. GOOGL already
  fired this exact pattern — capex raised, stock fell (S1 FIRED-A, scored).
- **Leg 2 (suppliers — semicap + memory/storage inside the same IT label)**: deserve **less**
  underweight, protected by the very capex raise that compresses Leg 1's multiple.
- **Leg 3 (security/observability — PANW, CRWD, FTNT, DDOG)**: A-grade positive on both RS20 and
  RS60 vs SPY, tagged 🟡 only because of a measurement artifact (M25), not because the flow is weak.

This is the **third instance** of a pattern the desk has already measured twice — Real Estate
(retraction R7, duration REITs vs digital infrastructure, an 18.2pp RS20 spread vs SPY, replicated
on two dates) and Industrials (M26, primes vs capital goods). IT is the only one of the three still
carried as one label. A file that produces a single IT verdict has failed its own mandate; nothing
below rolls up to one number.

**W5 test, applied to the label itself**: inside this one 56-name "Information Technology" sector,
MU's RS60 vs SPY is **+88.5** and AVGO's is **−10.8** — a **99.3pp spread inside one GICS label**,
wider than the sector's own day move (delta +0.319). When the internal spread exceeds the label's
own signal, the label is the wrong unit. §6 quantifies this further.

**Corroborating measurement already on file (R10, `scripts/risk_units.py`, 699 trading days,
SPY-residual correlation)**: the premortem's own headline claim that IT + Real Estate + Utilities
are "one AI-datacenter short" was tested and **not supported in its strong form** — DLR-NVDA
+0.049, EQIX-AVGO −0.074, all below the 0.35 unit threshold. Clustering instead resolves into
**four separate units**, of which **U3 (AVGO/NVDA/TSM — compute) and U7 (MU/AMAT — memory/equipment)
are already distinct clusters inside IT itself.** That is independent, prior evidence that IT's
internal structure does not move as one thing — this file's split is not a new claim, it is the
same structure read at the equity level (RS, not correlation).

---

## 1. Leg 1 — SPENDERS

**GICS note (binding, C1-adjacent discipline)**: MSFT and AAPL are GICS Information Technology.
**META and GOOGL are GICS Communication Services**, not IT — they are included here for context
only because the capex mechanism (S13) treats all four as one economic cohort regardless of GICS
box. Do not read this section as claiming META/GOOGL are "in" the IT sector label.

| Name | GICS sector | flow tag | RS20 vs SPY | RS60 vs SPY | Capex line |
|---|---|---|---|---|---|
| MSFT | Info Tech | 🟢가속 new_green | +2.5 | **−12.8** | guides 2026-07-29 |
| AAPL | Info Tech | 🟢가속 new_green | +8.8 | +15.5 | not a hyperscaler capex name |
| META | Comm Services | 🟢가속 new_green | +9.7 | **−11.8** | guides 2026-07-29 |
| GOOGL | Comm Services | 🔴분산 | −3.1 | −5.4 | **raised** 2026-07-22, S1 FIRED-A |
| DELL | Info Tech (hardware) | 🟢가속 new_green | +1.4 | +99.8 | server/AI infra beneficiary, not a spender |
| HPE | Info Tech (hardware) | 🔴분산 | −3.5 | +66.2 | server/AI infra beneficiary, not a spender |

**The already-scored precedent (S1, FIRED-A)**: GOOGL raised FY26 capex guide to **$195-205B**
from $180-190B; Q2 actual capex **$44.9B, +100% YoY**; management framed it as "a supply-constrained
environment" (2026-07-22 AMC). The stock **fell** on the print despite the raise being unambiguously
bullish for volume. That is the desk's "score the observable, not the price reaction" rule firing in
the wild — a capex raise read by the market as a **margin drag** on the spender, not as good news.

**On the same 07-22 close, four of five mega-caps ignited new-green (MSFT, AAPL, META, plus AMZN in
Consumer Discretionary) and GOOGL alone printed red** — RS20 −3.1 / RS60 −5.4 vs SPY. This is a
single-name event (n≈1, rule S1) that the desk must not generalize into "AI capex names are all
falling" — three of four adjacent names are green.

**MSFT specifically carries the RS60 signature of the S13 thesis already**: RS20 +2.5 (short-term
green, consistent with new_green) but **RS60 −12.8 vs SPY** — a name whose medium-term relative trend
is already negative heading into a capex print that consensus expects to raise again (07-29). If the
S13 cross-condition fires branch A (capex raised AND spender NTM P/E compresses AND supplier median
RS20 turns positive), MSFT is the name most likely to show it first, because it is the only pure-play
GICS-IT hyperscaler spender in this file.

**S13 (registered 2026-07-23, ARMED, event 2026-07-29)** is the frozen test of this leg. Its
cross-condition (three legs, 10 sessions post-print, ~2026-08-12): (1) capex guide raised/held/cut at
MSFT and META; (2) spenders' NTM P/E change; (3) suppliers' median RS20 vs SPY (MU, AMAT, LRCX, KLAC).
⚠ No usable implied move exists for MSFT/META — `module_flow --positioning` straddles (META ±4.4%,
MSFT ±2.9%) expire 2026-07-24, **before** the 07-29 event, so they are not event-priced and no
threshold is taken from them (S13's own flagged limitation, carried here unmodified).

---

## 2. Leg 2 — SUPPLIERS: semicap + memory/storage

### 2a. The pullback-vs-downtrend question (D6, the decisive rule for this leg)

Every semicap/memory name below is tagged 🔴분산 (C-grade) while carrying a **positive RS60 vs SPY**
(A-grade). Per **D6**, RS20/RS60 momentum is the desk's only A-grade verified signal; OBV and the
🟢🟡🔴 tag are C-grade, corroborant only, and **may never override a disagreeing A-grade signal**.
The 🔴 tags below are therefore **not admissible** as evidence the equipment/memory leg is broken —
they are a 20-day pullback sitting inside a 60-day uptrend, which is a distinct animal from a
downtrend, and the RS60 sign is what carries evidentiary weight here.

| Ticker | flow_score | tag (C-grade) | RS20 vs SPY (A-grade) | RS60 vs SPY (A-grade) | Signature |
|---|---|---|---|---|---|
| AMAT | −0.268 | 🔴분산 | −7.3 | **+28.1** | pullback-in-uptrend |
| LRCX | −0.308 | 🔴분산 | −15.9 | **+14.5** | pullback-in-uptrend |
| KLAC | −0.308 | 🔴분산 | −14.1 | **+6.3** | pullback-in-uptrend |
| INTC | −0.325 | 🔴분산 | **−24.3** | **+19.6** | pullback-in-uptrend, deepest 20d drawdown |
| MU | −0.309 | 🔴분산 | −10.7 | **+88.5** | pullback-in-uptrend, strongest 60d |
| MRVL | −0.166 | 🟡중립 | −26.3 | +23.7 | pullback-in-uptrend |
| SNDK | −0.167 | 🟡중립 | −20.4 | +56.9 | pullback-in-uptrend |
| WDC | −0.088 | 🟡중립 | −18.9 | +33.1 | pullback-in-uptrend |
| STX | +0.026 | 🟡중립 | −14.4 | +50.2 | pullback-in-uptrend |

All nine names show the same signature: negative RS20, positive (often strongly positive) RS60, all
vs SPY. That consistency across nine independent tickers, two sub-industries (semicap equipment and
memory/storage), and one 20-day window is a stronger basis for "pullback" than any single name would
be on its own — though it remains one dated observation (asof 2026-07-22 close), not a multi-date
replication.

### 2b. The QoQ contract-price RATE series (LENS L1 — second derivative, not the level)

TrendForce server DRAM contract price, quarter-over-quarter: **1Q26 +90~95% → 2Q26 +58~63% → 3Q26
+13~18%**. This is a rate that has **decelerated for two consecutive quarters** — the L1 signal is
this deceleration, not the level ("shortage into 2027" is the distraction the lens exists to filter
out). New capacity coming online: SK M15X and Micron Idaho **mid-2027**; Samsung P5 **2028** — both
more than a year out, so the deceleration in the rate is happening well before any new supply hits.

**Open contradiction C1 (carried, not resolved)**: long-term-agreement price floors both cap the
upside and floor the downside on contract pricing. This is unmeasured in this repo and is not
resolved by anything in this file — it is the single best counterargument to reading the QoQ
deceleration as bearish, because a floor could make the deceleration purely mechanical (base effect)
rather than demand-driven.

### 2c. Margin percentile and revision breadth (LENS L2 — never call a multiple cheap alone)

**MU** (binding standing thesis, not re-derived): forward P/E **6.39x** (fresh pull 2026-07-23,
consistent with the carried 6.31x). Gross margin **84.6% = 100th percentile of its own 17-year SEC
XBRL history (FY2009-FY2025)**, +25.7pp above the FY2018 prior peak of 58.9%, median 32.0% across
the sample, with **two negative-margin years inside the 17** (FY2009 −9.2%, FY2023 −9.1%). The
margin_history.py rerun today (`--current 84.6`) confirms the series and percentile unchanged. **The
6.39x forward multiple is the arithmetic signature of a margin at its historical ceiling, not of
cheapness.**

Estimate-revision momentum, refreshed 2026-07-23: MU's +1y EPS estimate moved **100.53 → 153.74 over
90 days (+52.9%)** with revision breadth **28↑ : 0↓ (30-day, next-year column)** and **25↑ : 0↓
(current-quarter)** — consensus is still chasing upward, unanimously. Per the standing thesis: **a
first downgrade in a 30:0-type name is a bigger event than the multiple** — none has occurred yet as
of this pull.

**AMAT** — thesis line (previously absent, per the coverage-gap flag below): forward P/E 33.51x,
PEG 1.43, revision breadth **26↑ : 0↓ current-quarter (30d)**, **6↑ : 0↓ next-year (30d)**, +1y EPS
+19.0% over 90 days. Unlike MU, AMAT's multiple is not at a "cheap-looking" extreme (33.5x fwd vs
MU's 6.4x) — the peak-margin trap is less acute here because the market is not pricing AMAT as
statistically cheap. The unanimous upward revision breadth (0 downgrades across all four horizons) is
the same consensus-chasing signature as MU's, at lower magnitude. Next print 2026-08-14.

**LRCX** — thesis line (previously absent): forward P/E 39.59x, PEG 1.86, +1y EPS +12.8%/90d,
revision breadth **6↑ : 0↓ next-year (30d)**, no downgrades on any horizon. Reports **2026-07-30**,
the nearest print among the three unowned semicap names — the first live test of whether the
unanimous-upgrade pattern in this leg holds through an actual print.

**KLAC** — thesis line (previously absent): forward P/E 41.99x, PEG 2.24 — the richest multiple and
weakest revision breadth of the three equipment names: current-quarter 30d is **3↑ : 1↓** and
7-day is **0↑ : 1↓** (the only negative near-term revision print across AMAT/LRCX/KLAC/MU). Next-year
breadth is still positive (9↑ : 2↓, 30d) but this is the first crack in an otherwise unanimous
upgrade cohort — worth flagging exactly because the standing thesis says a first downgrade matters
more than the multiple. Reports **2026-07-29**, one day before LRCX.

**Unowned coverage gap closed**: `module_report_tags` flagged AMAT, LRCX and KLAC as carrying 4
reports each with no per-name thesis line in STANDING_VIEW.md. The three lines above are written to
close that gap; they are new to this file, not re-derivations of a prior desk view.

### 2d. INTC as its own line (not folded into the memory/equipment average)

INTC shows the deepest RS20 drawdown of the whole leg (−24.3 vs SPY) alongside a solidly positive
RS60 (+19.6). Forward P/E 63.14x on a **negative trailing EPS** (no trailing P/E computable), PEG
1.36 — the PEG looks reasonable only because +1y EPS estimate has moved **+161.2% over 90 days on
the current-quarter line and +102.4% on the current-year line**, off a very low base (current-quarter
estimate $0.08 → $0.22). This is the sharpest revision-momentum re-rating in the entire IT list, and
it is happening off depressed 2025 base-year comps, which caution against reading the percentage
alone as a demand signal — the base effect is doing real work here.

---

## 3. Leg 3 — SECURITY / OBSERVABILITY

**PANW, CRWD, FTNT, DDOG** are the clean A-grade case inside IT. RS60 vs SPY: **PANW +83.1 · CRWD
+63.5 · FTNT +79.2 · DDOG +85.1** (asof 07-22 close; consistent in direction and magnitude with the
07-21 pull already on file, M28: DDOG +93.7, PANW +91.9, FTNT +85.4, CRWD +66.0 — the numbers moved a
few points day to day but the ranking and the "all four strongly positive" fact did not). RS20 vs
SPY: **PANW +13.4 · CRWD +8.8 · FTNT +2.9 · DDOG +9.5** — all four positive at 20 days too, meaning
this is not a stale 60-day tailwind riding on a dead 20-day window; the momentum is live on both
clocks. Three of four (PANW, CRWD, DDOG) show OBV 매집 (accumulation); FTNT shows OBV 중립.

**All four are tagged 🟡중립, not 🟢가속, solely because vol_surge sits at 0.68-0.78** (PANW 0.77,
CRWD 0.68, FTNT 0.78, DDOG 0.70) — below the M25 gate threshold of 1.2. Per **M25**, the 🟢 tag
requires OBV **and** RS20>0 **and** vol_surge≥1.2 in a 3-axis unanimity test, and `velocity` (the
alternative path to 🟢) is None on all 300 rows in this universe. All four names here pass two of
three axes and are blocked by vol_surge alone — 🟡 in this dataset means "not volume-surging," **not**
"no flow," and per D6 this C-grade tag cannot veto the A-grade RS signal above it.

**C5 (carried, explicitly NOT resolved here)**: the strongest measured momentum in this file meets
the weakest measured valuation discipline. Forward multiples: PANW 78.81x (PEG 3.79), CRWD 118.64x
(PEG 6.22 — fresh pull, consistent with the carried "up to 6.6" figure), FTNT 44.83x (PEG 3.57),
DDOG 85.70x (PEG 1.59, the cheapest of the four on this axis). **This repo has never measured a
valuation factor.** Resolving C5 by "gate on valuation" would let an unmeasured axis veto a measured
one (the RS signal); resolving it by "momentum wins" ignores that the experiment designed to test
exactly this trade-off (PLAY23) has never produced a result. Per the binding instruction: **carry
C5, do not resolve it** — no verdict is offered on whether the multiple caps the trade.

**Revision breadth detail, fresh pull**: PANW current-quarter 40↑:1↓ (30d) but next-year is
**3↑:8↓ (30d)** — a genuine two-sided book, not unanimous. FTNT current-quarter 38↑:0↓, current-year
39↑:0↓ — cleanly unanimous on the near-term lines. CRWD's near-term book flipped negative in the
last 7 days (0↑:5↓ current-quarter) after 30-day breadth of 29↑:11↓ — worth watching but a 7-day
window is thin (verify-before-conclude discipline: flag, do not conclude). DDOG's 30-day breadth is
strongly positive on both near-term lines (37↑:0↓, 36↑:0↓).

**⚠ FTNT reports 2026-07-30.** This print is also the first live test of a connection this file
surfaces between Leg 2 and Leg 3: on 2026-07-21/22, Fortinet was named as **Intel's first foundry
customer** for security-chip ASICs on the **Intel 4 node** (CNBC, Tom's Hardware — "Fortinet becomes
Intel 4's first foundry customer, following firewall ASIC deal"). This is a genuine cross-leg link —
a Leg 3 name (FTNT) as a disclosed customer of a Leg 2 name's foundry business (INTC) — but it is
**Intel 4, a mature node, not 18A**, so it does not by itself satisfy S6's frozen "18A/foundry
customer" observable (§4). It is reported here as a named, dated fact, not as a resolution of S6.

---

## 4. Compute — NVDA, AVGO, AMD (separate boat)

**STANDING_VIEW is explicit and this file does not contradict it**: NVDA and AVGO participated least
in the recent memory-driven rally and should not be folded into a memory verdict. Confirmed on the
07-22 close: NVDA flow_score +0.362 🟡, RS20 +4.1 / **RS60 −2.9** vs SPY — its 60-day relative trend
is flat-to-negative even as memory names post RS60 of +30 to +88. AVGO flow_score +0.322 🟡, RS20
+2.5 / **RS60 −10.8** — the widest negative RS60 of any name discussed in this file among the
"AI-adjacent" cohort. AMD flow_score +0.379 🟡, RS20 +4.4 / **RS60 +54.1** — AMD's profile looks more
like the memory/equipment pullback-in-uptrend signature than like NVDA/AVGO's flat-to-negative one,
despite AMD being grouped with NVDA/AVGO as "Compute, Semiconductors" by GICS industry. **Their
driver is hyperscaler capex directly (demand for their own product), not the memory-supply chain
that drives Leg 2** — which is exactly why NVDA/AVGO's RS60 sign diverges from MU/AMAT/LRCX/KLAC's
even though all sit inside the same "Semiconductors" GICS industry classification.

---

## 5. Tonight's INTC test — read-through KPIs per leg (S6 frozen observable, NOT altered)

**S6 is registered, ARMED, event 2026-07-23. Its frozen observable is unchanged here**: an
externally named 18A/foundry customer, **or** capex/utilisation guided up. Branch A (named customer
or capex-up) reads as "the semicap drawdown was a pullback, not a downtrend — the industry_US IT
underweight is short the wrong thing." Branch B (no customer, capex flat) reads as company-specific,
consistent with R5's kill of any EDA-leads-semis claim.

**The implied-move sharpening this file adds, per instruction, without touching the frozen
observable**: S6's registered implied move of **±4.4%** was tagged **D0** — the options contract
priced it **expired before the print**, and was explicitly logged as "a FLOOR, not a fair estimate."
A fresh options pull today (2026-07-23) shows **±12.7%, expiry 2026-07-24 (D1), which covers the
event** — **2.9x the registered floor figure**. The floor caveat registered against this scenario was
measured to be correct: the market is pricing roughly three times the move the original (expired)
contract implied. This raises, not lowers, the bar for what counts as a large surprise tonight.

**Per-leg read-through, if INTC fires branch A or B**:

- **Leg 2 (suppliers)**: branch A on INTC (named 18A customer or capex/utilisation up) directly
  supports the pullback reading for AMAT/LRCX/KLAC/MU too, since INTC shares the same RS20-negative/
  RS60-positive signature (§2a) and the same capex-cycle logic. Branch B does not automatically
  extend to the others — INTC's foundry-customer narrative is idiosyncratic (Intel is the only
  merchant foundry story in this cohort); a company-specific INTC miss does not, on its own, falsify
  AMAT/LRCX/KLAC's cleaner pure-equipment-demand thesis.
- **Leg 1 (spenders)**: no direct read-through. INTC is not a hyperscaler capex spender in the S13
  sense; its capex is its own fab-building capex, a different mechanism.
- **Leg 3 (security)**: the FTNT/Intel-4-foundry-customer fact (§3) sits adjacent to this print but
  does not satisfy S6's 18A-specific observable — watch for whether tonight's call upgrades that
  relationship toward 18A or leaves it at Intel 4.
- **Note on the earnings-date discrepancy**: `module_fundamentals_us` (pulled 2026-07-23) lists
  INTC's next event as **2026-07-24**, one calendar day after this task's registered 2026-07-23
  after-close date — most likely a timezone/calendar-field artifact in the feed (an after-close US
  print lands as the next calendar date in some sources). S6's registered date is used as
  authoritative here per instruction; flagged so a later scorer is not confused by the mismatch.

---

## 6. Dispersion (W5)

The internal spread inside "Information Technology" on 2026-07-22:

- **RS60 vs SPY, full range**: MU **+88.5** to AVGO **−10.8** = **99.3pp spread**, and DELL +99.8 to
  INTU −32.8 = **132.6pp spread** if hardware/software extremes are included. Either framing is wider
  than the sector's own single-day delta (+0.319, the largest on the board) or its breadth (0.07).
- **flow_score, full range**: AAPL +0.721 to QCOM −0.894 = a **1.615-point spread** inside one label,
  on a scale where the entire sector's wflow is +0.201.
- **The sector-level wflow/eqflow divergence itself is the headline dispersion fact**: wflow +0.201
  but eqflow **−0.144**, a **0.345 spread — the widest wflow/eqflow divergence of any of the 11
  GICS sectors** on this board, on 4 green / 22 red of 56 names (breadth 0.07). A reader looking at
  wflow alone, or at the day's delta alone (+0.319, also the largest on the board), would call IT the
  improving sector; breadth and eqflow say the opposite. Both readings are correct for different
  subsets — that is precisely why one IT verdict cannot hold.

**W5 conclusion**: when the RS60 range inside one GICS label (99-133pp) exceeds the label's own
day-move by two orders of magnitude, the label is not describing one thing. Three legs, three
verdicts, one file.

---

## 7. Track KPIs and anti-signals, per leg (observables, not recommendations)

**Leg 1 — Spenders**
- KPI: MSFT and META capex guide direction at 2026-07-29 print (raised/held/cut) — the S13 categorical line.
- KPI: MSFT/META NTM P/E change over the 10 sessions following the print (to ~2026-08-12) — S13 leg 2.
- KPI: GOOGL RS20 vs SPY, tracking whether the 07-22 red print (−3.1) is a persistent divergence from META/MSFT/AAPL or a single-day event (S16, event 2026-07-29).
- Anti-signal: capex **cut** at either MSFT or META (S13 branch C) — would break both the volume leg and the price leg together, and per S13 extends past memory into AVGO/NVDA/TSM.

**Leg 2 — Suppliers**
- KPI: median RS20 vs SPY across MU/AMAT/LRCX/KLAC over the 10 sessions post-07-29 print (S13 leg 3) — turning positive is the "less underweight" signal.
- KPI: INTC's S6 branch outcome tonight (2026-07-23), read alongside the fresh ±12.7% implied move (D1, covers the event).
- KPI: LRCX print 2026-07-30, KLAC print 2026-07-29 — first live tests of the unanimous-upgrade pattern in equipment names.
- KPI: server DRAM QoQ contract price for 4Q26, when published — a third consecutive deceleration would strengthen the L1 reading; a re-acceleration would break it.
- Anti-signal: a first downgrade in MU's 30:0 (or AMAT/LRCX's similarly unanimous) revision book — per standing thesis, this is a bigger event than any multiple.

**Leg 3 — Security/Observability**
- KPI: vol_surge crossing 1.2 on any of PANW/CRWD/FTNT/DDOG while RS20 stays positive — the M25 gate that would flip the C-grade tag to 🟢 without needing any new A-grade evidence.
- KPI: FTNT print 2026-07-30 — the nearest live test of this leg, and adjacent to whether the Intel-4 foundry relationship deepens toward 18A.
- Anti-signal: RS20 turning negative at two or more of the four names simultaneously — would break the "all four positive on both clocks" premise this leg's inclusion rests on.

---

## 8. What I could not measure

- **C1 (long-term-agreement price floors)**: whether LTA floors cap the memory upside and floor the downside is not measured in this repo. It is the single best counterargument to the L1 deceleration reading and is carried unresolved.
- **C5 (security valuation vs momentum)**: no valuation factor exists in this repo to weigh against the RS momentum signal. Explicitly not resolved, per instruction.
- **PLAY23**: the experiment that would test whether momentum or valuation wins in names like the Leg 3 cohort has never produced a result (dig D15, per STANDING_VIEW). Its absence is why C5 stays open.
- **S13's implied-move gap**: no options-implied threshold exists for MSFT/META that covers the 07-29 event window; the straddles on file expire 07-24. This file did not attempt to fabricate one.
- **INTC's foundry-customer count precision**: the Fortinet deal is confirmed as Intel 4, not 18A; whether any 18A-specific customer will be named tonight is unknown at time of writing.
- **A second, independent replication date for this file's own W5/dispersion claim**: everything here is asof one close (2026-07-22). Real Estate's split (R7) was validated on two independent dates; this IT split has one.
- **Whether the U7 (MU/AMAT) correlation cluster from R10 extends to LRCX/KLAC/INTC/SNDK/WDC/STX** — R10's clustering only named MU/AMAT explicitly; this file's Leg 2 grouping by RS signature (§2a) is a distinct, looser test (nine names, one date) than R10's correlation-based unit test (two names, 699 days).
