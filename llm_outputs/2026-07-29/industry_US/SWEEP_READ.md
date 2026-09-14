# SWEEP_READ — industry_US — 2026-07-29 (Wed)

> **The reading, not a second copy of the data.** Every sector row and every per-name row lives in
> `SECTOR_FLOW_US.json` (§`sector_rotation`, §`names`) and `US_LIVE_SHORTLIST.json` and is **cited,
> not reprinted**. This file holds only what those JSONs cannot say. Benchmark **SPY** inline (C1).

## 0 · ⚠ D74 FIRED, and it was caught and remediated in-run

The first pass stamped **`asof: 2026-07-29`** on a bar **three minutes old** (the US session opened at
09:30 ET; the sweep ran at 09:33) **and wrote that snapshot into `llm_outputs/sector_flow/history.json`**
— the baseline every future `new_green` diffs against.

**Remediation executed, not logged**: the price cache `prices_2026-07-29.pkl` was backed up
(`.contaminated.bak`), trimmed from 84 to **83 rows (≤2026-07-28)**, the `2026-07-29` key was removed
from `history.json` (backed up as `.bak_0729`), and the sweep was re-run. **Second pass: `asof
2026-07-28`, n=300.** Everything below is the settled bar.
⇒ **D74's 2nd US occurrence, and the 1st in which the guard was applied before any downstream stage
read the artifact.** ⚠ `history.json`'s prior key is **2026-07-27** — there is no 07-28 key — so
`delta` and `new_green` below are a **one-session** diff only after this run writes 07-28.

## 1 · Universe headline — three numbers

**n 300 · wflow −0.035 · 🟢 17 / 🔴 61.**
Against 07-28's **+0.121 / 24 / 65** (`SECTOR_FLOW_US.json` of that date): **the board's cap-weighted
flow went negative and the green count fell a third.**

## 2 · Cross-checks against the MACRO transmission matrix

**① CONFIRMS Info Tech's Neutral, and sharpens it into the board's single worst reading.**
IT is **0 🟢 of 56 with 29 🔴 — 48% of the board's entire red count sits in one sector** — and its
**eqflow (−0.303) is 4.5× worse than its wflow (−0.068)**. That ordering is the *inverse* of a
breadth-led sector: **the mega-caps are holding up a collapsing tail.** Composition of the 29 reds:
**15 are semiconductors or semi equipment**, 4 application software, 3 electronic components.
⇒ MACRO's P3/P10 said the supplier leg is in a 20-day drawdown; the sweep says **the drawdown is the
sector's median, not its tail.**

**② CONTRADICTS the Energy tape and CONFIRMS the Energy flow — the contradiction is a filter artifact.**
Energy carries the **board's #1 wflow (+0.380)** and a positive eqflow (+0.253) while **XLE was the
2nd-worst 5-day sector (−1.59%)** and it produced **0 🟢 of 16**. Diagnosed below (§3): **8 of its 16
names are OBV-accumulating with positive RS20 and are blocked by `vol_surge` alone.** ⇒ **the money is
arriving in Energy without a volume surge**, which the tag cannot express. **MACRO's P4 (kill line
12.22 points away) and the sweep agree; the ETF tape is the dissenter.**

**③ CONTRADICTS the Materials UW on the axis MACRO said was overdue — and the contradiction now has
TWO legs.** Materials carries the **board's largest positive delta (+0.301)** and **eqflow +0.128 >
wflow −0.027** (breadth better than cap-weight, and the only sector where the two straddle zero in
that direction). **NUE +16.2/+14.8 and STLD +10.9/+10.5 vs SPY, both OBV-accumulating.**
★ **This is S36's second leg**: its branch A needs *"5-day excess >0 AND green count still 0."*
**Excess is +5.46pp (MACRO §E) and the green count is 0.** ⚠ **But see §4 — the "green count 0" leg is
partly a measurement of the gate, not of Materials.**

**④ CONFIRMS Industrials OW− and RELOCATES it.** **9 of the board's 17 greens are Industrials**, and
**4 of them are capital goods — WAB · PCAR · MMM · ITW** (`SECTOR_FLOW_US.json §names`). That is the
node **M174** measured at **flow −0.193 with 0 🟢 / 16 🔴** five days ago. **5 of the 8 `new_green`
names are Industrials** (PCAR · MMM · ITW · LMT, plus WAB already green).
⇒ **M174's three-way split (primes +0.667 / rails +0.368 / capital goods −0.193) may be inverting at
the capital-goods end.** The OW− is no longer only a rail-and-defense story, and **that is a DEEP
question, not a sweep verdict.**

**⑤ ANSWERS the question MACRO handed SWEEP on Health Care — and the answer is "still no".**
C7's resolving observable is *"one 🟢 from OUTSIDE the top-6 by market cap."* Health Care produced
**exactly one green, TMO — which is inside the named top-6 block (LLY·JNJ·ABBV·MRK·TMO·UNH).**
⇒ **C7's observable reads ZERO for a fourth consecutive run**, even though eqflow (+0.241) again
exceeds wflow (+0.162) and **XLV was the 2nd-best 5-day sector.** The belief-vs-money gap widened on
the price axis and did **not** widen on the axis C7 registered. **C7 stays carried, not resolved.**

**⑥ SPLITS Comm Services N−.** wflow **−0.197** against **eqflow +0.110** with **2 greens (T, EA)**,
and the board's **most negative delta (−0.306)**. ⇒ the sector's cap-weighted drag is its two largest
constituents; its tail is positive. **W5 applies to the N− exactly as it applied to IT.**

**⑦ Financials is still the only sector where breadth exceeds cap-weight AND both are positive**
(eqflow +0.374 > wflow +0.294). ⚠ **M173's caveat is unretired**: 56% of that gap was BRK-B last time
it was decomposed, and this run did not re-decompose it.

## 3 · Shortlist composition — the ABSENCES, each diagnosed

`US_LIVE_SHORTLIST.json`: 15 names, **9 of them Industrials.** The names are in the artifact; the
finding is what is missing.

| Absent sector | 🟢 | pass OBV-매집 ∧ RS20>0 | blocked by `vol_surge` alone | Verdict |
|---|---|---|---|---|
| **Energy** | 0 / 16 | **8** | **8 (100%)** | ★ **FILTER ARTIFACT.** MPC (RS20 +18.1 / RS60 +20.2, surge 0.96) · PSX (+18.3 / +11.8, 0.95) · XOM (+12.5 / −3.9, 0.85) are all 🟡 on the volume axis alone |
| **Materials** | 0 / 12 | **5** | **5 (100%)** | ★ **FILTER ARTIFACT.** NUE (surge 1.02) · STLD (1.00) · SHW (1.15) |
| **Consumer Staples** | 0 / 19 | **5** | **5 (100%)** | ★ **FILTER ARTIFACT**, and it matters — **XLP was the 3rd-best 5-day sector (+3.57%)**. CCEP (0.98) · ADM (0.97) · KO (1.00) |
| **Information Technology** | 0 / 56 | **9** | **9 (100%)** | ⚠ **NOT an artifact.** Only **9 of 56** even reach the OBV∧RS20 pre-condition (Financials 32/47, Industrials 21/50), and **29 are red.** The absence is evidence |
| **Utilities** | 1 / 15 | 2 | 1 | Mixed — thin either way (6 reds) |

★ **And the accumulation that DOES exist inside IT is not in semis.** The 9 names that pass are led by
**ACN (RS20 +32.0) · ADSK (+21.6) · AAPL (+20.7 / RS60 +22.2) · ADBE (+20.7) · SHOP (+14.1)** — IT
services and software. ⇒ **a single IT verdict is a verdict across a live software bid and a dead
semis tape (W5).** **AAPL is in that list, still carries no thesis anywhere, and is one of the 28
tickers `module_report_tags` silently cannot index (M152/D65).**

## 4 · ⚠ The 🟢 gate mechanism replicates a SEVENTH time — and today its ARITY changed

- **95 names pass `OBV-매집 ∧ RS20>0` and are not 🟢. 95 of 95 — 100% — fail on `vol_surge` alone**,
  and the **highest `vol_surge` among all 95 blocked names is 1.16**, against a 1.20 gate.
  Prior instances: US 07-22 **99** · US 07-23 **68** · KR 07-24 **191** · US 07-24 **71** ·
  US 07-25 **74** · US 07-27 **70**. **Two markets, seven dates ⇒ code structure, not a market fact.**
- ★★ **New this run: `velocity` is null on 300 of 300**, against **M203's measured 50/300 on 07-27.**
  ⇒ **the gate is 3-axis unanimity today, not the 3-of-4 vote M203 described** — and **all 17 greens
  cleared on a volume path (`vol_surge` 1.21–1.84); not one cleared on velocity.**
  **M203 is not retracted — it is state-dependent**: the gate's arity depends on whether `velocity` is
  wired on that call path, which is exactly **dig D75** (*"the axis is not missing, it is unwired on
  one call path"*). **Today it is unwired. State it with every 🟢 read downstream.**
- ⚠⚠ **Consequence for S36, and it is a bracket-construction problem, not a market one.**
  S36's branch A requires *"green count still 0"* in Materials. **The green count is 0 because five
  accumulating names sit at `vol_surge` 0.88–1.15 — i.e. the leg can settle on the gate rather than on
  Materials.** That is the **L3-bis family** (*a bracket whose observable can settle on frozen
  mechanics is not a test*). **Handed to PREMORTEM. S36 is NOT re-frozen and is not re-read here.**

## 5 · Cycle-exposure GAP — handed to ALPHA's action bracket

`CYCLE_EXPOSURE.json` (live read-only KIS book): **both ranked cycles flag 🚨 GAP.**
**AI-compute 8.32% vs a 12.0% floor (−3.683pp)** · **Energy 7.72% vs 8.0% (−0.277pp)**.
Held epicenter **AVGO, NVDA, TSM** and **MPC, PSX, XOM**; book ≈ **$11,582 total, $4,332 invested
⇒ ~62.6% cash**.

★ **M146/M181 replicate an EIGHTH time: nothing was traded and both margins drifted** (AI-compute
−3.769 → −3.683pp; Energy −0.327 → −0.277pp). ⚠ **Under D61's proposed ±0.5pp band the two flags read
differently: AI-compute's 3.68pp is outside it ⇒ the GAP is real; Energy's 0.277pp is INSIDE it ⇒
that GAP is `unresolved`, not a fail.** ★ **MPC now reads as held epicenter for the first time**,
joining PSX and XOM.

## ✅ EXIT CHECK

- [x] Sweep done → `SECTOR_FLOW_US.json` (**asof 2026-07-28**, n=300); sector ranking and the
      8 `new_green` names read from the artifact.
- [x] `US_LIVE_SHORTLIST.json` written (15 names; FINRA short-pressure verdicts read — 6 clean-rise).
- [x] `CYCLE_EXPOSURE` GAP read; **two 🚨 handed to ALPHA's action bracket**, with the ±0.5pp band
      caveat attached to the smaller one.
- [x] **No table in this file exists in the JSONs** — sector rows and per-name rows are cited by
      artifact. The only per-name figures reproduced are the ones carrying a *diagnosis* (§3, §4).
- [x] Seven cross-checks stated, each **confirming or contradicting** the MACRO matrix (§2), and every
      shortlist absence diagnosed as **evidence vs filter artifact** (§3).
