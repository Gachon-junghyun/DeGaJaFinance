# SWEEP_READ — industry_US · 2026-08-25 (Tue) · Stage 4 / L1·SWEEP

> The reading, not a second copy of the data. Numbers live in `SECTOR_FLOW_US.json`,
> `US_LIVE_SHORTLIST.json`, `CYCLE_EXPOSURE.json`. **No sector row and no per-name row is reprinted here.**

---

## 🚨 §0 · Instrument health line — read BEFORE the numbers

**`SECTOR_FLOW_US.json §scoring`: `n_axes` 3 · `vel_coverage` 0.1706 (51/299) · `scored` 299 ·
`dropped_missing_axis` 0 · `vel_axis` false.**

**The news axis is DEAD this run** (17.1% against an 80% bar) and **the cause is the pipe, not silence** —
probed, not assumed: `fts search … --days 7 --count --scope foreign` returned **Nvidia 4137 · Nucor 27 ·
Marathon Petroleum 25 · Nasdaq Inc 6** this morning, i.e. the index answers *and discriminates across
three orders of magnitude*. The sweep's own log says the same thing in its 🚨 line.

★★ **And the 51 measured names are POSITIONALLY identified, not random**: mapped against
`us_top300.csv` row order they are **universe ranks 0–50, contiguous from rank 1** — verified
`rk == range(0, 51)`. `M856`'s finding reproduces exactly, one rank wider (49 → 51 names).
⇒ **the news coverage is a deterministic mega-cap block, and yesterday's overlap with it is ZERO**
(08-24's snapshot measured 0 names). **Any "which names got news" comparison across those two runs is
comparing 51 names against none.**

### 🚨🚨 §0b · NEW DEFECT — this run's sweep ran on an UNSETTLED bar, and it moved the one axis that has a measured sign

`llm_outputs/sector_flow/prices_2026-08-25.pkl` carries a **2026-08-25 bar** created at **09:1x ET,
before the US cash open**. Measured across all 300 names:

- **08-25 volume ÷ 08-24 volume: median `0.0318`, mean `0.0408`, p90 `0.0744`. ZERO of 300 names reach
  even 50% of the prior session.** It is a pre-market stub, not a session.
- Price contamination is small (median stub change **−0.048%**), so `rs20`/`rs60` are only lightly moved.
- **Volume contamination is not small.** `vol_surge` across the universe:
  **median `0.820 → 0.670` (−18.3%)**, mean 0.866 → 0.716, and the count clearing **`vol_surge ≥ 1.2`
  falls `22 → 12` — a 45% drop** — against the 08-24 snapshot's settled 08-21 terminal bar.

⇒ **This matters more than a generic staleness note.** `vol_surge` is the **only axis in this desk's
own US IC ledger with a Bonferroni-passing positive sign** (`h=1`, `IC +0.0398`, `t(NW) +3.40`,
`n_eff 34.0`). The sweep systematically **depresses** it whenever the run happens before the close,
and this desk runs pre-market **every day**. ⇒ **new dig `D355`** (§4).

⚠ **Consequence for this file, applied not merely noted**: the `Δflow` column computable against the
08-24 snapshot spans **08-21 settled → 08-25 stub**, i.e. two settled sessions *plus* a stub — it is
**not a one-session ignition read** and is not used as one anywhere below. `n_axes` matches (3 vs 3),
so G2's scale test passes; **G2 does not test terminal-bar regime, and this is the gap.**

---

## §1 · Universe headline — three numbers

**n = 299 scored · universe `wflow` is negative in 9 of 11 sectors · tags 🟢 8 / 🟡 217 / 🔴 74.**
(For contrast the 08-21 settled snapshot carried 🟢 6 / 🔴 ~5x fewer in the leaders. The 🔴 count of
**74 = 24.7% of the universe** is the run's blunt headline: a quarter of the top 300 is distributing.)

---

## §2 · Cross-checks against the MACRO matrix — CONFIRM / CONTRADICT

### ✅ CONFIRM — Industrials and Utilities. Flow and price agree, and so do their breadths.
`SECTOR_FLOW_US.json §sector_rotation`: Industrials is the board's worst on **both** `wflow` and
`eqflow` with **18 🔴 of 50 and 0 🟢**; Utilities is second-worst on both with **10 🔴 of 15**.
MACRO's own price frame put them at `exc5` **−1.881** (30/50 negative) and **−1.011** (13/15 negative).
⇒ **two independent instruments, same ordering, same breadth story.** The `UW−` on both stands.

### 🚨 CONTRADICT #1 — Health Care. The board's 2nd-best price sector is now the board's flipper.
MACRO put HLTH at `exc5` **+4.295 / median +4.668, 3 of 32 negative, `exc20 +3.318`** — positive on
both windows, the only sector that was.
The sweep now reads HLTH **`wflow −0.035`, `eqflow +0.004`, 1 🟢 / 5 🔴**, collapsed from
`+0.196 / +0.229` on the 08-21 snapshot — **and `top1_flips_sign` is now TRUE (`LLY`, 19.4%).**

★ **This is a flipper-list CHANGE and it invalidates a constraint PREFLIGHT inherited.** PREFLIGHT
read the 08-24 snapshot and wrote *"the run's only flipper is Consumer Staples (`WMT`)."*
**On today's own snapshot, STPL no longer flips and Health Care does.** The correction is appended
here rather than edited into PREFLIGHT (§4c).
⇒ **Flipper list handed to ROTATION: `Health Care` (top1 `LLY`, `top1_w` 19.4%) — 1 of 11.
ROTATION may not promote or demote HLTH on the weighted-flow bucket.** It may use `eqflow` (**+0.004**,
i.e. flat) and price breadth (**29 of 32 positive**), and must say which.
⚠ **And `D297` binds here too**: the flipper test is per-ticker, so it cannot see share-class pairs —
COMM's `GOOGL`+`GOOG` (38.3% each = 76.6%) still prints `false`. **No `wflow` claim is made on COMM.**

### 🚨 CONTRADICT #2 — the money and the price disagree about who is winning, everywhere except the losers.
Rank the 11 sectors by `eqflow` and by MACRO's `exc5` and the two lists agree at the **bottom**
(INDU, UTIL) and disagree at the **top**: Consumer Staples is **1st on price (+5.048) and 8th on
`eqflow` (−0.217)**; Health Care is **2nd on price and 2nd-from-flat on flow**; **Energy is 1st on
`eqflow` (+0.227, the only positive sector) and only 7th on price (+1.620)**.
⇒ **The defensive bid MACRO measured is a PRICE move that the flow instrument does not corroborate,
while Energy is the one sector where money and price point the same way and money points harder.**
Stated as a contradiction, not resolved: the flow axes are OBV (C-grade, `D6`) plus two
relative-strength axes the desk's own ledger ranks **negatively** at h=5 (`rs60`, `IC −0.1310`,
`t −5.46`). **Neither side of this disagreement is graded high enough to overrule the other.**

### ✅ CONFIRM — Energy, on both instruments, and it is the run's cleanest agreement.
Only positive `wflow` **and** only positive `eqflow` (**+0.149 / +0.227**), **1 🟢 / 0 🔴 — the only
sector on the board with zero reds.** MACRO has ENRG `OW` with the board's best `exc20` (**+5.062**)
and the only sector whose median beats its mean.
⚠ **Counter-weight, stated in the same breath:** MACRO's `P96` records that the commodity leg is
breaking on the **LIVE** 08-25 print (Brent −4.65%, crack −8.21). **The sweep cannot see that** — its
last real bar is 08-24. This is the field note's exact case: *a same-day shock is not in the flow
numbers yet.*

---

## §3 · Shortlist composition — the ABSENCES, diagnosed

`US_LIVE_SHORTLIST.json`: **8 names** pass `mcap ≥ $10B ∧ tag 🟢가속`.

### 🚨 The finding is that the 🟢 set splits 4/4 by MECHANISM, and one half is built on a revoked axis.

| Half | Names | `vol_surge` | What made them 🟢 |
|---|---|---|---|
| **OBV ∧ RS ∧ surge** | `MSTR` 1.67 · `COIN` 1.72 · `MRK` 1.53 · `TGT` 1.31 | **all ≥ 1.2** | the three price/volume axes, unaided |
| **velocity-derived** | `MRVL` 0.74 · `ORCL` 0.47 · `CVX` 0.73 · `MA` 0.68 | **all < 1.0** | the **news-velocity** leg (`MRVL` 1.92 · `CVX` 1.71 · `ORCL` 1.33 · `MA` 1.26) |

★★ **All four velocity-derived greens sit inside the top-51 news bucket — and so does every name that
got a velocity number at all.** ⇒ **their ignition is positionally determined: they are 🟢 because they
were among the 51 names the pipe had budget to query, not because a market event distinguished them.**
★★★ **And all four are ALSO this run's entire `new_green` list (`MRVL` `ORCL` `CVX` `MA`).**
⇒ **100% of the day-over-day "ignitions" are velocity-derived, on an axis G1 revoked, in a bucket
defined by market-cap rank.**

⇒ **Applied, not merely noted: the four velocity-derived greens are WITHDRAWN for this run.**
The citable 🟢 set handed to ROTATION/EVENT_ALPHA is **`MSTR` · `COIN` · `MRK` · `TGT`**.
★ This is `R81`/`R78` **pre-empted by measurement instead of reproduced** — the 2026-08-19 run wrote
that it had pre-empted the lesson and then used the tag three times. Here the withdrawal is executed
at the stage that produces the tag.
⚠ **What survives unaided**: `MRVL`'s `rs20 +36.7` (the board's best) and `ORCL`'s `rs20 +17.7` are
price facts and carry themselves; `CVX` and `MA` have **nothing** left once the velocity leg is
removed (`rs20 +3.8` and **+2.8**, `vol_surge` 0.73 / 0.68).

### Absences, each diagnosed as evidence vs artifact

- **Energy produces 1 shortlist name (`CVX`) and it is the withdrawn kind** — while `MPC` (`flow +0.578`,
  OBV 매집, `rs60 +43.3`) and `PSX` (`+0.556`, 매집, `rs60 +35.5`) are **🟡, blocked on `vol_surge`
  alone** (0.84 / 0.80). ⇒ **FILTER ARTIFACT, `M866`'s 2nd replication — and §0b makes it worse this
  run**, because the stub bar cut universe `vol_surge` by 18%. **The sector with the board's only
  positive flow and zero reds contributes no citable shortlist name.**
- **Industrials: 0 of 50, and this IS evidence.** 0 🟢, 18 🔴, `eqflow −0.313`, breadth 0.00, and
  MACRO's price cut agrees (30/50 negative). Nothing is being filtered out here.
- **Utilities: 0 of 15, also evidence.** 10 🔴, breadth 0.00, `exc20 −8.401`. Same as INDU.
- **Real Estate: 0 of 12.** `eqflow −0.410`, 3 🔴, breadth 0.00 — evidence, but ⚠ MACRO measured its
  **median `exc5` (+2.782) at 2.1× its mean**, so the sector's *price* is better than its aggregate.
  **Absence on flow, presence on price — handed to ROTATION as unresolved.**
- **Communication Services: 0 of 12** — and this one is **NOT citable in either direction**, because
  `D297` makes every `wflow`/`eqflow` number on COMM unusable (76.6% of the sector is one issuer in
  two rows). **Recorded as un-measurable, not as absence.**

### Short-pressure read (`US_LIVE_SHORTLIST.json`, FINRA z — the US substitute for KR's investor feed)
Clean-rise (low-short / covering): **`MRK` −0.72 · `MRVL` −0.95 · `CVX` −1.22.**
Crowded-short (turn-conditional squeeze fuel, **never a buy signal alone**, `D6`): **`ORCL` +1.75.**
Normal: `MSTR` +0.28 · `COIN` +0.05 · `TGT` +0.71 · `MA` +0.90.
⚠ **`MRK` is the only name whose 🟢 survives the velocity withdrawal AND carries a clean short read** —
and MACRO's carry flags it as *"the sheet's strongest refutation datum"* (RSI 86.7, revisions **1↑/5↓**).
**The two readings are opposite and both stand.**

---

## §4 · Held-name coverage, cycle GAP, and the flippers handed forward

- ✅ **Held-but-not-in-universe: ZERO.** All **11** US book names (`ANET AVGO ETN HPE MET MPC NDAQ NUE
  NVDA PSX RTX`) are tagged by this sweep. The `TSM`/`LNG` invariant holds. ⚠ But `us_top300.csv` is
  **41 days old**, which is what decides the news bucket (§0) — coverage is clean, **freshness is not**.
- ✅ **`CYCLE_EXPOSURE`: no top-rank cycle GAP.** AI-compute (rank 1) epicenter **16.59% ≥ 12.0%** need,
  Energy/refining (rank 2) **9.82% ≥ 8.0%**. Missile-defense (rank 3, `RTX` 3.8%) has **no threshold
  set** and is reported ⚪ n/a rather than passed. ⚠ **`D250`, 11th run: there is still no
  optical/interconnect row in the registry**, so `LITE`/`COHR` exposure is **unmeasurable, not zero** —
  on the day those two are the board's worst 5-session names (MACRO §C).
- **Flipper list → ROTATION: `Health Care` only (top1 `LLY`, 19.4%).** 10 sectors print `false`.
  ⚠ Carried with `D297`'s caveat: the test is per-ticker and cannot see `GOOGL`/`GOOG`.
- **Book tape, from this sweep**: `RTX` is now **🔴분산** with `delta −0.629`, the book's largest
  negative — the carried downgrade deepens. `MPC` **+0.578** and `PSX` **+0.556** are the book's best
  flow scores, both OBV 매집, both blocked from 🟢 by `vol_surge` alone.

### New dig registered by this stage

| # | Finding | Positive-form remedy |
|---|---|---|
| **`D355`** | 🚨🚨 **The sweep includes an unsettled pre-market bar and it depresses the desk's only positively-measured axis.** Measured 2026-08-25 at 09:1x ET: the 08-25 bar carries **median 3.18% of the prior session's volume (0 of 300 names above 50%)**, and against the last settled snapshot universe `vol_surge` falls **median 0.820 → 0.670 (−18.3%)** with the `≥1.2` count **22 → 12 (−45%)**. `vol_surge` h=1 is the **only** US IC cell with a Bonferroni-passing positive sign (`t(NW) +3.40`). **This desk runs pre-market every day**, so the depression is systematic, not incidental — and `n_axes` continuity (G2) does not detect it because the axis count is unchanged | **① Have `sector_flow` DROP any terminal bar whose volume is below a stated fraction (e.g. 20%) of the trailing-20 median, and print `terminal_bar` + `dropped_partial: true/false` into `§scoring`. ② Add `terminal_bar` to the `scoring` block so a snapshot-to-snapshot Δ can check bar regime, not just axis count. ③ Until then, every `vol_surge`-derived statement on a pre-market run carries "stub-bar depressed".** (Human approval: scoring-path change, P5) |

### ⚠ What this stage asserted earlier in the run and now corrects (§4c, `D48`)

**PREFLIGHT (stage −1) wrote: *"the run's only flipper is Consumer Staples (top1 `WMT`)"*, and named a
removed citation right on that basis.** It read the **08-24** snapshot because today's did not exist yet.
**On today's own snapshot the flipper is `Health Care` (`LLY`) and Consumer Staples does not flip.**
The PREFLIGHT sentence is **left standing** and this is the correction: **the STPL restriction is
lifted, and an equivalent restriction now attaches to Health Care.** Recorded rather than edited away.
