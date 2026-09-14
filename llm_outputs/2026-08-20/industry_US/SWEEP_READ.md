# SWEEP read — industry_US · 2026-08-20 (Thu) · Stage 2 / L1·SWEEP

> **A reading, not a second copy of the data.** The numbers live in
> `SECTOR_FLOW_US.json` · `US_LIVE_SHORTLIST.json` · `../CYCLE_EXPOSURE.json` and stay there.
> Nothing below reprints a table those files already hold. Input to ROTATION §2.
> `asof` **2026-08-19** (settled). Analytical only — no buy/sell, no sizing (P4).

---

## 0 · 🚨 The instrument's own health line, read BEFORE its numbers

`SECTOR_FLOW_US.json §scoring`: **`vel_axis false` · `vel_coverage 0.1639` · `n_axes 3` ·
`scored 299` · `dropped_missing_axis 0`.**

**The news axis is DEAD in this run — coverage 16.39% (49 of 299), for the 8th consecutive run — and
it is the PIPE, not silence.** Probed, not assumed (`PREFLIGHT_US §G1`): the **same 40 names the sweep
returned `None` for came back 40/40 valid in 18.4 s** when re-asked by hand at 22:14 KST, and the CLI
returned **3651** three times for `Nvidia --days 7 --count --scope foreign`. Cumulative across six runs
of that probe: **0 of 240** sweep silences have ever survived falsification.

Consequences carried into ROTATION:
- All 299 names are scored on the **same 3 axes** (`dropped_missing_axis 0`), so the `+0.305`
  inflation class of 2026-08-09 is **not** present. The scale is internally consistent.
- `n_axes 3` today vs `n_axes 3` in the `2026-08-18` history snapshot ⇒ **the Δ subtraction is legal**,
  and it spans exactly **one session** — the first clean single-session Δ since 08-12.
- 🚫 **No theme-freshness, news-velocity or "it went quiet" reading may be taken from this file.**

---

## 1 · Universe headline — three numbers

**n = 299 · `wflow` −0.162 · 🟢 7 / 🔴 63** (🟡 229). Median `vol_surge` **0.740**.

---

## 2 · ★ The tag is not evidence today, and it decides who is on the shortlist

`R81`/`D290` replicate for the **10th** consecutive run, and this run measured the split:

- **7 greens. Only 3 clear `vol_surge ≥1.2`** — `MRK` 1.28 · `TGT` 1.27 · `KKR` 1.20.
- **4 are velocity-derived** — `LLY` (vel 1.20 / surge 0.86) · `MRVL` (1.35 / 0.69) · `MA` (1.28 /
  0.80) · `WMT` (1.34 / 0.93) — i.e. their 🟢 rests on **the axis `G1` revoked**.
- From the other side: **12 names clear `vol_surge ≥1.2` and 9 of them are 🟡 or 🔴** (`MNST` 1.64 ·
  `COHR` 1.51 · `KEYS` 1.47 🔴 · `NKE` 1.31 · `SNDK` 1.30 🔴 · `CSCO` 1.28 · `TJX` 1.23 · `EBAY` 1.20 ·
  `MO` 1.20).

🚨 **`US_LIVE_SHORTLIST.json` is built by filtering on the 🟢 tag ⇒ 4 of its 7 rows are inadmissible
as evidence this run.** The admissible three are `MRK`, `TGT`, `KKR`. Stated here so ROTATION does not
inherit the list as a quality signal — the same error `R78` and `R81` each caught after the fact.
Also `new_green` = 4 (`MRK`, `TGT`, `LLY`, `MRVL`), and **two of those four (`LLY`, `MRVL`) are
velocity-derived ignitions** ⇒ **the admissible new-🟢 count is 2, not 4.**

⚠ `M718`/`D270` replicates a **ninth** time: **105 names pass `OBV 매집 ∧ RS20>0`; exactly 3 also
clear `vol_surge ≥1.2` ⇒ 102 blocked, 97.1% of them on `vol_surge` alone.** The gate, not the money,
is producing the scarcity of greens.

---

## 3 · Cross-checks against the MACRO transmission matrix

### ✅ CONFIRMS — the two OW calls are the only two sectors where flow and price agree

`SECTOR_FLOW_US.json §sector_rotation` ranks **Health Care `eqflow` +0.252 (1st)** and
**Energy +0.182 (2nd)**; MACRO §C-1's 5-session excess vs `SPY` ranks **`XLV` +4.742 (1st)** and
**`XLE` +4.622 (2nd)**. **Two independent instruments, same top two, same order.** No other sector
appears in the top two of both.

### ✅ CONFIRMS — the IT underweight, and it is breadth, not a mega-cap artifact

IT is **last but two on `eqflow` (−0.197) with 19 red of 56 and 1 green** — and `eqflow` is *above*
`wflow` (−0.283), so removing the cap weighting makes it **less** bad, not more. The weakness is
therefore **broad and also cap-concentrated**, which is the worst combination available. `NVDA` at
19.4% is the `top1` and does **not** flip the sign.

### 🚨 CONTRADICTS — Utilities and Real Estate: the price is up and the flow is last

| | `eqflow` (rank of 11) | 5-session excess vs `SPY` (MACRO §C-1) |
|---|---|---|
| **Utilities** | **−0.545 (11th)**, `ex_top1` −0.578, **0🟢 / 8🔴 of 15** | **+0.855** |
| **Real Estate** | **−0.252 (10th)**, **0🟢 / 4🔴 of 12** | **+1.568** |

**Both duration-labelled underweights RALLIED on price while their flow sits at the bottom of the
board.** This is the single most decision-relevant contradiction in the sweep, and it cuts **against**
reading the 08-19 tape as a duration bid: if the Treasury's long-end intervention were being
expressed through the duration complex, the purest leg would not be the worst-accumulated sector in
the universe. **MACRO `P78` is registered on exactly this disagreement.**

⇒ **ROTATION should treat the UTIL/RE underweights as flow-supported and price-contradicted, and say
which side it is taking.** The desk has been on the flow side; today the price argued back.

### 🚨 CONTRADICTS — Financials: `eqflow` is now BELOW `wflow`, inverting the July reading

`eqflow` **−0.127** against `wflow` **−0.009**. The desk carried Financials for weeks as *"the board's
only breadth-led sector"* (`M40`, eqflow > wflow). **That relationship has flipped**: the cap-weighted
half is now the better half, with **2🟢 / 8🔴 of 47**. Whatever Financials is today, it is not a
breadth story, and any argument still resting on `M40`'s shape needs re-measuring.

### ⚠ NEITHER — Materials cannot be read on `wflow` at all

The run's **only** `top1_flips_sign` bucket: **Materials · `LIN` · 24.7% · `wflow` −0.099 →
`wflow_ex_top1` +0.063** (swing 0.162). The other **ten sectors have zero flippers**, so this is the
only place the restriction binds. On the admissible axes Materials reads `eqflow` **−0.064** with
**0🟢 / 4🔴**. **ROTATION may not promote or demote Materials on its `wflow` sign** (`G3`).

### ⚠ Energy's `Δ` disagrees with Energy's level — and the level is the admissible half

Energy's one-session Δ is **−0.157**, the second-worst on the board, against `eqflow` **+0.182** (2nd
best) and `wflow_ex_top1` **+0.257**. Per `D293` a Δ mixes earned excess with roll-off and the sweep
publishes neither leg ⇒ **the Δ is not used as a verdict**, and the level is. Recorded so the
divergence is visible rather than resolved by picking the convenient half.

---

## 4 · Shortlist composition — read the ABSENCES, and diagnose each one

The shortlist is **7 names** (`mcap ≥ $10B` ∧ tag 🟢 ∧ flow-desc top-15). Sector coverage:
**Health Care 2 · Consumer Staples 1 · Financials 2 · Information Technology 1 · Consumer
Discretionary 1** — the two names are cited from `US_LIVE_SHORTLIST.json`, not reprinted.

**The four sectors that produced NOTHING, each diagnosed:**

| Sector | Absent because | Evidence or artifact? |
|---|---|---|
| **Energy** | **0🟢 and 0🔴 of 16 — every name is 🟡.** No name can clear a 🟢 filter when the sector's entire tag distribution is neutral | 🚩 **ARTIFACT.** Energy is the board's **2nd-best `eqflow` (+0.182)** and 2nd-best price excess (+4.622). Its top names (`MPC` surge 1.00, `PSX` 1.03) sit **just under** the 1.2 gate. **This is the `M144`/`D270` gate, not an absence of money** — and it is the 3rd consecutive run this desk has had to write that sentence about Energy |
| **Industrials** | 0🟢 / 10🔴 of 50 | ✅ **EVIDENCE.** `eqflow` −0.073 and price −1.670 agree. ⚠ But the desk's actual Industrials position is **defense**, and `RTX` reads `flow +0.617 · rs20 +10.2 · rs60 +21.3 · OBV 매집` — **the sub-node is not the label** |
| **Real Estate** · **Utilities** | 0🟢 of 12 and of 15 | ✅ **EVIDENCE on flow** — both are bottom-two on `eqflow` with zero accumulation clearing any gate. ⚠ **Contradicted on price** (§3). The absence is real; what it means is contested |
| **Materials** | 0🟢 / 4🔴 of 12 | ✅ **EVIDENCE**, and it is the only sector whose absence is *also* corroborated by a scored bracket: `S77` settled **FIRED-C** at −1.589, of which `STLD` **−11.78** and `NUE` **−8.04** are the whole residual |

★ **The most important absence is Energy's, and it is a filter artifact for the third run running.**
A desk reading only the shortlist would conclude the run's 2nd-ranked sector has no candidates.

---

## 5 · Held-but-not-in-universe — the invariant, checked on BOTH books (`T22`)

| Book | n | Not in `us_top300` | Not scored in the sweep |
|---|---|---|---|
| **paper** (`module_paper_book`) | 11 | **NONE** | **NONE** |
| **real** (`module_KIS.fetch_overseas_balance`) | 12 | **NONE** | **NONE** |
| union of both | 14 | **NONE** | **NONE** |

✅ **The desk can tag everything it owns, on either definition of "the book".** This is the first
stage in this run to state it for both books rather than one.

⚠ **`EA` remains the universe's one hole** — in `us_top300`, absent from the sweep (299 of 300), with
no close on any of the last three bars. **8th consecutive run.** Not held, so it is a coverage gap and
not an invariant breach; and per `G5` the desk **cannot measure** `EA`, which is a different sentence
from `EA` having no flow.

---

## 6 · Cycle exposure — no GAP, and the number that says so is still under-counted

`../CYCLE_EXPOSURE.md` (real KIS book, read-only): **AI-compute rank 1 — epicentre 19.78% vs a 12.0%
floor ✅** · **Energy rank 2 — 9.89% vs 8.0% ✅** · **Missile-defense rank 3 — 5.89%, ⚪ n/a (no floor
set).** Verdict: **no top-rank cycle GAP.**

⚠ **Two caveats travel with that ✅, both inherited and both re-confirmed today:**
1. **`M731` — the registry misses 5 of the real book's 12 names** (`LITE` `COHR` `HPE` `T` `NUE`), so
   "any-layer 23.56%" is an **under-count**. Under-counting can only fail to raise a flag; it cannot
   manufacture a false ✅. **The verdict is safe; the printed percentage is not.**
2. **Rank-3 has no floor**, so it **cannot fail** — ⚪ n/a is not a pass. Registry maintenance is a
   human item (P5).
★ And the AI-compute ✅ should be read next to MACRO §C-3: the epicentre exposure is **above its
floor** while that basket's 5-session excess sits at the **0.8th percentile of two years**. **The GAP
check is a floor on ownership, not a statement about whether owning it is working.**

---

## ✅ EXIT CHECK — self-audit

- ✅ `scoring` block read and quoted first; coverage **16.39% < 80%** ⇒ stated **"news axis dead this
  run"** with the cause **probed** (pipe, 40/40 on re-ask), not assumed.
- ✅ Every `top1_flips_sign` sector listed with `top1` and `top1_w` — **one: Materials / `LIN` / 24.7%**
  (and "the other ten are zero" is stated explicitly).
- ✅ Held-but-not-in-universe run on **both** book definitions; result **NONE / NONE**, `EA` noted as a
  universe hole rather than an invariant breach.
- ✅ Sweep artifact present (`SECTOR_FLOW_US.json`, `asof` 2026-08-19); sector ranking and new-🟢 read
  — **and the new-🟢 count corrected from 4 to an admissible 2.**
- ✅ `US_LIVE_SHORTLIST.json` written; short-pressure verdicts read (2 clean-rise, 2 crowded-short,
  3 normal) — **with 4 of 7 rows flagged inadmissible on the tag.**
- ✅ `CYCLE_EXPOSURE` GAP read: **none**; the two caveats handed forward to ALPHA.
- ✅ **No table reprinted from the JSONs** — sector rows and per-name rows are cited by artifact.
- ✅ Four cross-checks against the MACRO matrix, two confirming and two contradicting, each naming
  which side the money is on; all four shortlist absences diagnosed as evidence vs artifact.
