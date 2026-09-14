# SWEEP_READ — industry_US — 2026-07-27 (Mon)

> The reading, not a second copy of the data. Numbers live in `SECTOR_FLOW_US.json` ·
> `US_LIVE_SHORTLIST.json` · `../CYCLE_EXPOSURE.md`. **No sector row or shortlist row is reprinted here.**

## 0 · ⚠⚠ The sweep had to be run TWICE, and the first result was universe-wide contaminated

**`scripts/sector_flow.py` has no settled-bar guard, and this is the first US run ever to fire inside a
live session.** The first execution returned **`asof: 2026-07-27`** — today's bar, ~2 minutes old.

Measured from its own price cache (`llm_outputs/sector_flow/prices_2026-07-27.pkl`), 07-27 volume as a
share of the last full session (07-24):

| | SPY | DLR | MU | VLO | WAT |
|---|---|---|---|---|---|
| 07-27 vol ÷ 07-24 vol | **8.6%** | **2.0%** | 13.6% | 12.7% | 4.5% |

⇒ **Every RS20, RS60, OBV state and `vol_surge` in that first JSON was computed on a 2–14%-of-session
bar.** That is the **R17 / R17-b failure class at 300-name scale** — the exact thing the desk has
retracted twice and made a standing rule about ("settled-only is a rule, not a preference").

**What was done, and it is stated rather than buried**: the unsettled row was trimmed from the price
cache, the contaminated `2026-07-27` snapshot was removed from `llm_outputs/sector_flow/history.json`,
and the sweep was re-run. **The delivered `SECTOR_FLOW_US.json` is `asof 2026-07-24`, settled.** The raw
first-pass cache is preserved outside the repo. The history edit was **necessary, not cosmetic**: that
snapshot is the baseline every *future* run diffs `new_green` against, so leaving it would have poisoned
tomorrow's ignition read with a 2%-volume bar.

★ **Why no prior run hit this**: the KR desk runs pre-open (its market is closed), and the last four US
runs fired **before** the US open (07-22/23/24) or on a **Saturday** (07-25). **The defect is structural
and dormant, not new** — registered as dig **D74**.

## 1 · Universe headline — 3 numbers

**n = 300 · wflow +0.109 · 🟢 25 / 🔴 72**, `asof` **2026-07-24**.

⚠ **This is the same session the 2026-07-25 run swept** (that file: wflow **+0.108**, 🟢 **24**, 🔴 **72**).
The 0.001 / one-name difference is provider revision noise. ⇒ **the sweep contributes NO new flow
information this run, exactly as HANDOVER §0 predicted.** Its value here is the three cross-checks below,
not a delta. **`new_green` (RTX · NOC · PLD · PCG · AMZN · NVDA) is a 07-24-vs-07-23 comparison the prior
run already made — it is NOT a fresh ignition and must not be presented downstream as one.**

## 2 · Cross-checks against the MACRO matrix — where the money agrees and where it does not

**① CONFIRMS — Energy's wflow is the board's highest, and its breadth is not.**
`SECTOR_FLOW_US.json §sector_rotation` puts **Energy first on wflow with the second-highest eqflow**, on
**1 🟢 / 1 🔴 of 16**. The tilt (OW−) and the money agree on direction. ⚠ But the sector's flow is
**mega-cap-led with essentially no breadth signal** (breadth 0.06 on n=16), which is precisely the
condition under which §D-P4's *decomposition* — gasoline breaking while distillate holds — matters more
than the sector aggregate. **Flow cannot see inside a crack spread; the matrix's gasoline-vs-distillate
split is the load-bearing read, not this row.**

**② CONTRADICTS the sharpest — Information Technology is two opposite sectors under one label, and the
sweep states it more starkly than the matrix does.** IT carries a **positive wflow against a negative
eqflow**, with **25 🔴 against 4 🟢 of 56 — the worst red count and the worst breadth on the board.**
⇒ **the mega-caps are holding the label up while the median IT name is being sold.** This is **W5** and
it is the direct quantitative form of **C8** (one label, three legs wanting opposite verdicts). The money
is on the *spenders*, not the *suppliers* — and **S13's cross-condition on 07-29 is the registered test.**
★ **Consumer Discretionary shows the identical signature** (positive wflow, negative eqflow, 8 🔴 / 1 🟢),
so this is a two-sector mega-cap-narrow pattern, not an IT quirk.

**③ CONTRADICTS, and it is the one the matrix should hear — Financials is the board's only genuinely
breadth-led sector, and the gap has re-opened.** It is the **only sector where eqflow exceeds wflow**
(`§sector_rotation`). Carried context: **M40 measured this gap narrowing +0.145 → +0.067** on 07-22.
It has **widened again** on the 07-24 close. ⇒ **the FIN OW's surviving leg (breadth, after R11 removed
the steepener) is measurably stronger on this session than when it was last examined.** ⚠ This does
**not** touch **S23**, whose risk is a *bear-flattener hold* that kills NIM without tripping S19 or S9 —
breadth in a flow score and net interest margin are different objects.

**④ Utilities and Materials are the only two sectors negative on BOTH wflow and eqflow with zero-to-one
🟢** — the UW tilts on both are flow-consistent. ⚠ **But the Materials UW's own deferred test is still
deferred**: the 07-25 run pre-committed to *"if XLB beats SPY again next session the UW needs
re-argument,"* and **there has been no next session.**

## 3 · Shortlist composition — the absences, each diagnosed

`US_LIVE_SHORTLIST.json` (mcap ≥ $10B ∧ 🟢가속 ∧ top-15 by flow, `asof 2026-07-24`).

**The two absences that are findings, not noise:**

- ★★ **Energy contributes exactly ONE name (XOM) — and it is the one with 0% refining exposure.**
  **VLO, MPC and PSX are all absent.** Diagnosed: **filter artifact, not evidence.** The refiners are
  blocked by the 🟢 gate (§4), which is a volume test — the identical diagnosis the protocol's own field
  note records from a prior run (*"an ENRG shortlist of 0 turned out to be a 🟢-tag filter artifact… the
  refiners were OBV-accumulating but tagged 🟡"*). ⇒ **the sector this run's matrix flags as
  nearest-to-kill has one representative on the shortlist and it is the wrong one.** This is **M146's
  Energy leg replicating from a second direction**: the registry's human-locked `core_pick` is **PSX**,
  and the only name the instruments surface is **XOM**.
- ★ **Information Technology contributes ZERO names of 56** despite the largest sector count in the
  universe. Diagnosed: **evidence, not artifact** — it is consistent with 25 🔴 / 4 🟢 and a negative
  eqflow. The four IT greens simply do not clear the flow-rank top-15 cut.

**What the shortlist is actually made of, read as composition rather than as names**: it is dominated by
**defense/aerospace (LMT, RTX, NOC), rails (UNP, CSX), insurance (CB, TRV) and defensive
large-cap health care (TMO, JNJ)** — i.e. **the OW− Industrials and OW− Financials tilts, plus the N
Health Care one.** ⚠ **Three of those names print or settle a registered bracket inside four sessions**
(**UNP and CSX are S20's frozen observable, tomorrow**; **TRV carries M150's exhaustion geometry** —
98.6% of its 60-day excess in the last 20 sessions).

⚠ **D52/D73 blocks the positioning read on the two names that matter most tomorrow.** The shortlist tags
**UNP ✅"low-short/short-covering (clean rise)" on z −2.41** — but UNP's own 20-day baseline is **52.2%**,
**7pp above the tool's stated 40–45% normal band**, so that verdict is a statement about UNP's own
history, not about covering. **The verdict string is suppressed here and reported as unreadable.**

## 4 · The 🟢 gate replicates a SIXTH time — and on the US path it is now strictly a volume test

Computed on this run's own JSON: **98 names pass `OBV-매집 ∧ RS20 > 0`; 25 are 🟢; 73 are blocked, and
100% of the 73 are blocked by `vol_surge < 1.2` alone.**

★ **New, and it sharpens M25/M144**: **`velocity` is null on 300 of 300 names — not 250 of 300.** So on
the US path there is **no news-velocity substitution available at all**, and 🟢 requires 3-axis
unanimity, of which the third axis is raw volume. ⚠ **The axis exists and is simply not wired into the
sweep**: `us_live_shortlist` computed real news velocity for **5 of its 15 names** (RTX 3.30 · XOM 3.08 ·
JNJ 2.64 · PLTR 1.97 · AAPL 1.83) from the same corpus, in the same run. ⇒ **this is a wiring gap in
`sector_flow`, not missing data** — registered as dig **D75**.

**Prior measurements of the same mechanism**: US 07-22 **99** · US 07-23 **68** · KR 07-24 **191** ·
US 07-24 **71** · US 07-25 **74** · **US 07-27 73**. **Two markets, six dates ⇒ code structure**, and
open dig **D11/D37** (a scoring change needs human approval) is still the blocker.

## 5 · RS baseline — M74/M145 replicates a THIRD time, byte-identically

**RS20 > 0 on 155/300 = 51.7% (median +0.65) · RS60 > 0 on 148/300 = 49.3% (median −0.35), benchmark
SPY.** Identical to M145. ⇒ **a positive RS vs SPY carries information in this universe and no baseline
subtraction is applied to US RS numbers.** ⚠ **R20's KR correction (subtract the *size-cohort* median,
not the universe median) does not transfer here and must not be imported** — that is rule **W1** in the
direction it is usually not applied.

## 6 · 🚨 CYCLE-EXPOSURE GAP — the flag flipped, and nothing was bought

`../CYCLE_EXPOSURE.md` (book read-only via KIS):

- **AI-compute / semiconductors, rank 1: epicenter 8.55% vs required 12.0% ⇒ 🚨 GAP, margin −3.447pp.**
- Energy / oil-refining, rank 2: **8.03% vs required 8.0% ⇒ ✅ by 0.03pp.**
- Missile-defense, rank 3: 7.53%, **no threshold set** ⇒ ⚪ n/a.

★★ **This is a state change and it is the one M146 predicted.** M146 measured the AI-compute margin over
its floor across five consecutive runs with the **held set unchanged** (AVGO, NVDA, TSM):
**−0.001 → +0.252 → +0.254 → +0.136 → +0.011.** It has now moved to **−3.447pp.** **Nothing was bought
or sold; the flag is mark-to-market drift**, which is exactly why **D61** asked for `margin_pp` to be a
first-class field. ⚠ **Under D61's own proposed rule the two flags read oppositely**: AI-compute's
|margin| = 3.447pp is **well outside** the 0.5pp noise band ⇒ **the GAP is real**; Energy's |margin| =
**0.03pp is inside it** ⇒ **that ✅ is UNRESOLVED, not a pass.** ⚠ Caveat stated: the book leg is fetched
live and therefore carries today's partial mark; the **registry** leg is `data/cycles/cycle_registry.json`,
**`updated: 2026-07-17` — 10 days stale, 3 rows.**

★ **M146's Energy leg replicates independently of the arithmetic**: the only held Energy epicenter name
is **XOM, with 0% refining**, while the registry's human-locked `core_pick` is **PSX**, unheld — and §3
above shows the shortlist surfaces XOM and not the refiners. **Three instruments, one blind spot.**

⚠ **D60(old) confirmed again**: the report footer cites **`data_build/cycles/`**, and that directory
**does not exist** (verified this run). The registry is at `data/cycles/`.

**🚨 handed to ALPHA's action bracket**, per this stage's EXIT CHECK. **No sizing, no buy/sell language —
the GAP is a coverage measurement (P4).**

## 7 · New digs registered by this stage

| # | Dig | Why it matters | Owner |
|---|---|---|---|
| **D74** ★★★ | **`scripts/sector_flow.py` has no settled-bar guard.** Run inside a live session it silently stamps `asof: <today>` and computes all four axes on a partial bar (measured: **SPY 8.6%, DLR 2.0% of session volume**), **and writes that snapshot into `history.json`**, poisoning the next run's `new_green` baseline. | The desk has retracted **two** claims (R17, R17-b) for exactly this at single-name scale and made settled-only a rule; the universe-wide instrument does not enforce it. It was dormant only because every prior US run fired pre-open or on a weekend. **Minimum fix: drop the final bar when its volume is < ~60% of the trailing-20 median, or expose `--asof`; and refuse to write a history snapshot for an unsettled date.** | `scripts/sector_flow.py` / human |
| **D75** ★ | **`sector_flow` reports `velocity` null on 300/300 while `us_live_shortlist` computes real news velocity for 5 of 15 names from the same corpus in the same run.** | The 🟢 gate is a 3-of-N vote in which the news axis is one option; with it null the gate collapses to a **volume test wearing a flow label** (C9), and **73/73 blocked names fail on `vol_surge` alone**. The axis is not missing — it is unwired on one call path. **Minimum fix: pass the same velocity source `us_live_shortlist` already uses.** | `scripts/sector_flow.py` / human |

## ✅ EXIT CHECK

- [x] Sweep done → `SECTOR_FLOW_US.json`, **`asof 2026-07-24` (settled)**; sector ranking and
      `new_green` read — and `new_green` explicitly labelled as *not* fresh.
- [x] `US_LIVE_SHORTLIST.json` written; short-pressure verdicts read **with baselines**, and the
      out-of-band verdict (UNP) suppressed per D52/D73.
- [x] `CYCLE_EXPOSURE` GAP read; **🚨 AI-compute handed to ALPHA's action bracket**, with Energy's
      ✅ flagged as UNRESOLVED under D61's own band.
- [x] **No table that exists in the JSONs is reprinted here** — every sector row and name row is cited
      by artifact.
- [x] **Four cross-checks against the MACRO matrix**, two confirming and two contradicting, with the
      side the money is on named in each.
- [x] **Shortlist absences diagnosed**: Energy = **filter artifact** (refiners blocked by the volume
      gate); IT = **evidence** (0 of 56, consistent with 25 🔴 and negative eqflow).
- [x] Zero buy/sell language, zero sizing (P4). English-pure.
