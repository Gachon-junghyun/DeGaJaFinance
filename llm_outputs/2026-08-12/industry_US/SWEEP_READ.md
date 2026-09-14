# SWEEP_READ — industry_US · 2026-08-12 · Stage 4/11 (L1·SWEEP)

> **The reading, not a second copy of the data.** Numbers live in `SECTOR_FLOW_US.json` ·
> `US_LIVE_SHORTLIST.json` · `../CYCLE_EXPOSURE.md`. No sector-ranking row and no per-name shortlist
> row is reprinted here (measured 2026-07-21: this file had become 97% restatement).
> Sweep **asof 2026-08-11** (settled). Analytical only, no buy/sell (P4).

## 1. Universe headline — three numbers

**n = 300 · wflow −0.148 · 🟢 17 / 🔴 81** (🟡 202).
The board is **net-negative on cap-weighted flow with a 4.8:1 red-to-green ratio**, and it is the
**third** consecutive run in which the negative aggregate coexists with a positive price tape
(`SPY` +2.49% over 20 sessions).

## 2. 🚨 The instrument's own health line, read BEFORE its numbers

`§scoring` → **`vel_axis: false` · `vel_coverage: 0.1133` (34/300) · `n_axes: 3` · `scored: 300` ·
`dropped_missing_axis: 0`.**

⇒ **The news axis is dead this run** and the sweep says so on line 1 of its own stderr. **It is the PIPE,
not silence** — verified, not assumed (PREFLIGHT G1): the remote query API returns `URLError`, the local
FTS index is **0 bytes**, and the client article store holds **50,234 foreign articles for 08-04→08-11**.
✅ **The D225-KR fix held**: `dropped_missing_axis: 0`, so all 300 names were scored on the **same three
axes** and no name received the +0.305 free bonus that defect used to hand out.

### 2a. ★★★ But the SCORE path and the TAG path disagree about whether news exists — and the tag path won on 6 names

This is the finding of this stage, and it is new:

| | Count |
|---|---|
| Names passing the pre-condition **OBV 매집 ∧ RS20 > 0** | **111** |
| …of which tagged 🟢 | **17** |
| …**blocked** | **94** — and **94 of 94 (100%) fail on `vol_surge` < 1.2 ALONE** |
| 🟢 names carrying a `velocity` value | **6 of 17 (35%)** |
| Those 6 | **CVX** (surge 0.98, vel 1.64) · **BRK-B** (0.92 / 1.51) · **NVDA** (0.83 / 1.25) · **CSCO** (0.74 / 1.60) · **ORCL** (0.68 / 1.26) · **JPM** (0.56 / 1.27) |
| The other 11 | all `velocity: null`, all `vol_surge ≥ 1.21` |

**Read it in one line: `flow_score` excluded velocity for all 300 names, and then `flow_tag` used
velocity anyway for the 34 names that happened to have it — so 35% of today's 🟢 bucket is lit by the
axis this same run declared dead, on an 11.3% subsample, at volumes BELOW the gate.**

★ **And two of those six are S65's own basket.** S65 was registered 2026-08-06 precisely because *"four
of the five new-🟢 (JPM · BAC · WFC · BRK-B) are VELOCITY-lit greens with `vol_surge` below 1.2."*
**JPM (0.56) and BRK-B (0.92) reproduce that exact shape today with velocity coverage at 11.3%** — i.e.
the mechanism S65 brackets is not only alive, it is now running on a **near-empty** news axis.
⇒ registered as **`D236`**. ✅ **M144 replicates a SIXTH time** (US 07-22 · 07-23 · 07-24 · 07-25 · KR
07-24 · today) — two markets, six dates, so it is code structure, not a market state.

**🚫 Binding consequence for downstream stages**: **no 🟢 may be cited as a money signal for CVX, BRK-B,
NVDA, CSCO, ORCL or JPM today.** Their tag rests on an axis PREFLIGHT G1 revoked. The other eleven greens
are volume-confirmed and citable **as 3-axis levels**.

## 3. Cross-checks against the MACRO transmission matrix — what CONFIRMS and what CONTRADICTS

| MACRO §G argument | Sweep says | Verdict |
|---|---|---|
| **ENRG → argues for promotion** | **rank-1 on BOTH axes** (wflow +0.360 · eqflow +0.163), the only sector positive on both, Δ **+0.074**, no G3 flipper, **7 of 16 at the OBV∧RS20 pre-condition** | ✅ **CONFIRMED — the money and the price agree, which they did not on 08-07** |
| **HLTH → argues for promotion** | headline **breadth 0.0 (0 🟢 of 32)** — reads as a flat contradiction | ⚠ **CONTRADICTION DISSOLVES on decomposition: 18 of 32 pass OBV∧RS20 — the 3rd-highest count on the board — and every one is blocked by `vol_surge` alone.** The breadth column is the **wrong instrument** for HLTH today; wflow +0.230 / eqflow +0.217 (rank 2, and the tightest cap-vs-equal agreement on the board) is the right one. **MACRO's argument survives** |
| **MATR → its UW leg is refuted** | headline **wflow −0.069** — contradicts | ⚠ **The dissent is single-name-owned: `wflow_ex_top1` +0.168** (LIN, 24.7% of sector cap, 🔴분산). **G3 forbids a MATR call on `wflow` today.** With eqflow +0.018 and 6 of 12 at the pre-condition, the sweep **does not contradict** MACRO's ex-NEM measurement (+1.203) once the flipper is removed |
| **UTIL → UW held** | **0 of 15 at the OBV∧RS20 pre-condition · 13 reds of 15 · wflow −0.475 · eqflow −0.482 — worst on every flow measure** | ✅ **CONFIRMED HARDER THAN PRICE.** XLU was the best sector on the 08-11 session (+1.48 exc1); the flow says that bid has no accumulation under it |
| **IT → N held, "breadth 0.11 highest of 11"** | **eqflow −0.218 is WORSE than wflow −0.151** | 🚨 **CONTRADICTION, and the breadth column is the misleading half**: a green *count* of 6 sits on top of an average name that is doing **worse** than the cap-weighted index, with **23 reds of 56**. **Breadth-as-count and breadth-as-eqflow disagree in IT and only in IT** |
| **RE → UW held** | wflow −0.222 · eqflow −0.182 · breadth 0.0 · **Δ −0.190 (2nd worst)** · 2 of 12 at the pre-condition | ✅ **CONFIRMED on every axis** — the most internally consistent verdict on the board |

★ **The one genuinely new cross-market shape**: **eqflow > wflow in Energy, Industrials, Materials,
Consumer Discretionary and Communication Services** — five sectors where the average name beats the
mega-cap aggregate — **against IT, Utilities, Real Estate and Staples where it is the reverse.** The
board is **breadth-led in cyclicals and mega-cap-led (downward) in the defensives and IT**.

⚠ **Δ is a 2-session change (08-07 → 08-11), never "today"** — PREFLIGHT G2 restored Δ this run
(same-mode 299-name baseline, 99.7% coverage) but only on that label. `new_green` (11 names: ABNB ·
AXON · DASH · KKR · UBER · CVX · ORCL · BRK-B · JPM · CSCO · NVDA) is citable **with R9's standing
caveat on AXON** (it is not a defense name) **and with §2a's caveat on the five velocity-lit members.**

## 4. Shortlist — read the ABSENCES, and they split into two measurable classes

15 names cleared `mcap ≥ $10B ∧ 🟢 ∧ top-15 by flow`. **Six of eleven sectors produced ZERO.**
The absences are **not one phenomenon**, and the pre-condition count is what separates them:

| Absence | Names at **OBV∧RS20** | Diagnosis |
|---|---|---|
| **Health Care (0 shortlist)** | **18 of 32** | 🚨 **FILTER ARTIFACT, and the largest on the board.** 18 names are accumulating with positive relative strength and **not one clears the volume gate.** An "HLTH has no money" reading is unsupported |
| **Materials (0)** | **6 of 12** | 🚨 **FILTER ARTIFACT.** Consistent with the independent ex-NEM price measurement (8 of 12 positive on exc5) |
| **Comm Svcs (0)** | 4 of 13 | mixed — thin at the pre-condition **and** blocked. ⚠ R56: EA still in the universe |
| **Staples (0)** | 3 of 19 | mostly real — the pre-condition itself is thin |
| **Real Estate (0)** | 2 of 12 | **essentially real** |
| **Utilities (0)** | ★ **0 of 15** | ✅ **A REAL ABSENCE — the only one.** Nothing is accumulating; the filter is not what produced this zero |

⇒ **Two sectors MACRO argued for promotion produced almost no shortlist presence, and in both cases the
sweep's tag — not the market — is why.** The shortlist's composition (IT 4 · INDU 4 · FIN 4 · DISC 2 ·
ENRG 1) is therefore a statement about **which sectors have high-volume names**, not about where money is.

★ Positively, the one shortlist signal that survives every caveat: **five "clean-rise" names** (🟢 **and**
low-short/short-covering on the independent FINRA axis) — **ABNB (z −3.50) · DASH (−2.15) · PH (−0.79) ·
PRU (−0.75) · AXON (−0.67)** — and **all five are volume-confirmed, not velocity-lit.** That is the
subset the instrument gates leave intact today.

## 5. 🚨 Invariant — can the desk tag what it holds?

**Paper book (10 positions): `LNG` and `TSM` are OUTSIDE `us_top300` for a TWELFTH consecutive run.**
They have **no flow, RS, OBV or short row in any artifact this stage produced.** Per PREFLIGHT G5 they
are **"not measured," never "no signal."** Both **are** present in `us_all_v2_candidate.csv` (1,522
names) ⇒ **a wiring gap, not a data gap** (human, P5). Every other holding is covered: AVGO 🟡 · NVDA 🟢
(⚠ **velocity-lit, §2a**) · MA 🟡 · RTX 🟡 · KMI 🟡 · VST 🔴.

**Real KIS book (`cycle_exposure`): every held name is inside the universe** — AVGO · NVDA · ANET 🟡 ·
MPC 🟡 · PSX 🟡 · RTX. ⚠ **The two books hold different names** (paper: KMI/LNG/VST; real: ANET/MPC/PSX)
and this stage does not merge them.

## 6. Cycle-exposure GAP — ✅ no GAP, and the margin is healthy for the first time in weeks

`CYCLE_EXPOSURE.md`: **AI-compute rank 1 — 16.46% epicenter vs a 12.0% floor (+4.46pp)** · **Energy
rank 2 — 10.69% vs 8.0% (+2.69pp)** · missile-defense rank 3, no threshold set (⚪).
★ **This is the reading that matters**: M146 recorded 2026-07-25 that the same ✅ *"cleared by 1.1 basis
points"* and was mark-to-market drift rather than construction. **Today both margins are multiples of
that** — the ✅ is no longer a rounding artifact. ⚠ It remains a **REAL-book** measurement (W1: not a
paper-book statement, and not a sizing input).
**No 🚨 GAP is handed to ALPHA's action bracket this run.**

---

**Size discipline check**: this file contains **no sector-ranking row and no per-name shortlist row**
from the JSONs. Everything above is a decomposition, a diagnosis, or a cross-check that the JSONs
cannot express.

---
---

# ═══ RUN-2 ADDENDUM · SWEEP — 2026-08-12 22:50 KST · **APPEND-ONLY** ═══

> Nothing above is rewritten. Interpretation only — no table the JSON already holds is reprinted.

## §R2-1 · No new sweep was run, and the reason is a measurement rather than an omission

**`SECTOR_FLOW_US.json` on disk is RUN-1's** (`asof 2026-08-11`, `_mode nonews`, `n_axes 3`,
300 scored, `vel_coverage 0.1133`). RUN-2 did **not** overwrite it. Three grounds, recorded in
`PREFLIGHT_US.md §RUN-2 G2`:

1. **No new settled price bar exists** — 08-12 is absent on every yfinance interval. Three of the
   sweep's four axes (OBV · RS · volume surge) would be **byte-identical**.
2. **The `history.json` ledger is keyed by DATA date, not run time** — a second sweep today would
   **replace** the `2026-08-11` key that RUN-1's SWEEP_READ, ROTATION, PREMORTEM, five DEEPs and
   BET_SHEET all cite, leaving the day's chain pointing at a file that no longer says what they quote.
3. **The one axis that changed cannot be mixed anyway** — with news alive a fresh sweep scores in
   `news` mode (4 axes), and differencing that against a 3-axis score is the arithmetic G2 forbids.

⚠ **The universe headline therefore stands as RUN-1 measured it and is not restated here** — cite
`SECTOR_FLOW_US.json §scoring` and `§sector_rotation` directly.

---

## §R2-2 · ★★★ What the restored news axis is worth, measured on identical prices

This is the cross-check RUN-2 can make and RUN-1 could not. **Same 08-11 prices, same engine, one
difference: the news axis is alive.** 20 names re-scored by a **direct 4-axis `module_flow` call**
(22:45 KST) against RUN-1's **3-axis sweep tags**:

| Result | Count |
|---|---|
| **Tags AGREE** (3-axis vs 4-axis) | **14 / 18** |
| **Tags DISAGREE** | **4 / 18 = 22%** |
| Not in the universe at all (G5) | **2** — `TSM` · `LNG` |

**Every disagreement, in full — each line carries both axis counts, as G2 requires:**

| Name | RUN-1 sweep, **3-axis** | RUN-2 direct, **4-axis** | The news axis that moved it |
|---|---|---|---|
| **CVX** | **+0.560 🟢 accelerating** | **🟡 neutral** | vel **0.85×** (below 1) |
| **JPM** | **+0.218 🟢 accelerating** | **🟡 neutral** | vel **1.06×** (barely above 1) |
| **KMI** | **−0.433 🟡 neutral** | **🔴 distributing** | vel **0.40×** — the lowest in the sample |
| **VST** | **−0.447 🔴 distributing** | **🟡 neutral** | vel **2.21×** — the **highest** in the sample |

★★ **Three of the four disagreements run in the same direction: the news-blind sweep was the more
BULLISH instrument** (CVX 🟢→🟡, JPM 🟢→🟡, KMI 🟡→🔴; only VST goes the other way). **That is the
`+0.305` inflation defect — the one that created this whole preflight protocol — reproducing on live
data at name level.** It is recorded here as a measurement, not an inference.

**Binding on ROTATION and BET, stated positively:** where a name's tag matters to a conclusion today,
**say which instrument produced it.** `CVX 🟢` and `CVX 🟡` are both true statements about different
axis counts, and a sentence that does not name the count is defective.

⚠ **Sample caveat, stated rather than hidden**: 20 names, chosen as the book's holdings plus the
largest sweep 🟢/🔴 names — **not a random draw**. The 22% is a disagreement rate **on this sample**,
not an estimate of the universe's rate. **It may not be extrapolated to the other 280 names.**

---

## §R2-3 · The two names the sweep cannot see (G5), now measured directly

Both book holdings absent from `us_top300` were scored by ticker, which the sweep's universe gate
prevents. **Warrant: direct `module_flow` call, 4-axis, 2026-08-12 22:45 KST — NOT a sweep output,
and not rankable inside any sweep sector table.**

| Name | flow | vel | OBV | RS20 | RS60 | vol surge |
|---|---|---|---|---|---|---|
| **LNG** | 🔴 distributing | 1.18× | **distribution** | −2.3% | **+7.1%** | 0.88× |
| **TSM** | 🔴 distributing | 0.87× | **distribution** | −2.1% | −2.0% | 0.75× |

⚠ **Read the split in LNG rather than the headline**: **RS60 +7.1% vs SPY against RS20 −2.3% vs SPY**
(RULE C1 — bench named inline; both figures are excess vs `SPY`) ⇒ the outperformance **vs SPY** is in
the **older** window and the recent 20 days are giving it back, with OBV in distribution.
**This is a description of two windows disagreeing, not a verdict** (P4).
★ **After 13 runs of "not measured," these two names now have a number. The wiring gap is unchanged** —
`us_all_v2_candidate.csv` (1,522 names, built 08-10) holds both; `sector_flow --market us` does not
read it. **Repair is a human-approved item, not this stage's.**

---

## §R2-4 · Cycle-exposure GAP — carried from RUN-1, not re-run

`CYCLE_EXPOSURE.md` (11:14 KST) is a day-root artifact and was **not** regenerated — its inputs (the
KIS book and the cycle registry) have not changed, and re-running would overwrite RUN-1's record for
no new information. Carried verdict:

| Cycle | rank | epicenter % | need ≥ | held | GAP |
|---|---|---|---|---|---|
| AI-compute / semiconductors | 1 | 16.46% | 12.0% | AVGO · NVDA · ANET | ✅ |
| Energy / oil-refining (Hormuz + Russia crack) | 2 | 10.69% | 8.0% | MPC · PSX | ✅ |
| Missile-defense / rearmament | 3 | 5.82% | — | RTX | ⚪ threshold unset |

**✅ No top-rank cycle GAP.** ⚠ One RUN-2 note that does **not** change the verdict: the rank-2 cycle's
narrative intensified today on the event axis (**Hormuz/Iran 28 articles / 14 outlets · IEA 1.8 mb/d
deficit · Libya refinery strikes**, MACRO §R2-C) — **and the exposure test is a position test, which
this stage does not restate as a recommendation (P4).**

---

## §R2-5 · Cross-checks against the MACRO matrix — what confirms, what contradicts

| MACRO §R2 object | Sweep-side reading | Verdict |
|---|---|---|
| Energy supply shock intensifying (§R2-C) | ENRG is the **only** clearly positive sector on RUN-1's sweep (**wflow +0.360 · eqflow +0.163 · ex-top1 +0.257**, breadth **0.06**) | **CONFIRMS direction, CONTRADICTS breadth** — the money agrees, but **breadth 0.06 means almost none of the 16 names carry it.** ⚠ And the two direct 4-axis energy reads disagree with each other: **KMI 🔴, LNG 🔴, CVX 🟡, XOM 🟡** — **no energy name in this sample is 🟢 on 4 axes** |
| Rate-hike odds plunging (§R2-C counter-evidence) | **UTIL −0.475** is the weakest of 11 and **RE −0.222** is 8th | **CONFIRMS the sweep, CONTRADICTS the news** — duration-sensitive sectors are where the money is *least* present, on a day the market cut hike odds. **This is precisely the object S73 branch C is frozen on**, and it settles tonight |
| AI-capex financed through a credit pipe (NVDA $500bn, §R2-D) | **IT −0.151 · ex-top1 −0.220** (NVDA 19.4% of the sector) — the sector is negative and **more** negative without its largest name | **CONTRADICTS any "AI money is broadening" reading.** ⚠ 3-axis, news-blind — and on 4 axes NVDA is still **🟢** while **MU · AMD · GEV are 🔴** |

★ **The single most useful line for ROTATION**: **7 of 11 sectors have breadth ≤ 0.06 and four are
exactly 0.00** (`§sector_rotation`). **This tape's sector signs are owned by very few names**, which is
the same fact G3's flipper list reports from the other side. **Neither a promotion nor a demotion today
can be justified on `wflow` alone** — and for **Financials · Industrials · Materials** it is forbidden
outright (G3).

---

## §R2-LINT · `report_lint` reconciliation — **RULE C1**

`report_lint` flags **L199** (*"the outperformance is in the older window"*, on LNG) under **RULE C1** —
*state the benchmark or the sign can invert; measured: 005930 is −12.1% vs SPY and +10.1% vs `^KS11`
over the same 20 days.*

**The flag is correct and the benchmark is now stated in the sentence's own scope:**
**every RS figure in §R2-3 — LNG RS20 −2.3% / RS60 +7.1%, TSM RS20 −2.1% / RS60 −2.0% — is excess vs
`SPY`**, the bench passed to `module_flow --bench SPY` for that call. The word *"outperformance"* in
L199 refers to **LNG's RS60 of +7.1% vs SPY** and to nothing else.

⚠ **And the C1 rule is exactly why that paragraph exists**: the sentence's point is that **a single
unlabelled "LNG is outperforming" is defective in a second way too — not only the benchmark but the
WINDOW inverts the sign** (+7.1% on 60 days vs −2.3% on 20). ⇒ **the same claim needs both its bench
and its window**, and this addendum's own EVENT_ALPHA/DEEP sections apply that to APO in the opposite
direction (RS20 +11.1% vs RS60 −2.4%).

⇒ **RULE C1 acknowledged; benchmark = `SPY`, named inline, on every RS figure in this addendum.**
