# SWEEP_READ — industry_US · 2026-08-23 (Sun) · Stage 4 / L1·SWEEP

> The reading, not a second copy of the data. Numbers live in `SECTOR_FLOW_US.json` ·
> `US_LIVE_SHORTLIST.json` · `llm_outputs/2026-08-23/CYCLE_EXPOSURE.json`. **No sector row and no
> per-name shortlist row is reprinted here** — they are cited by artifact.

## 0 · 🚨 Instrument health line — read BEFORE the numbers

`SECTOR_FLOW_US.json §scoring`: **`n_axes` 3 (`nonews`) · `vel_axis` false · `vel_coverage` 0.0 ·
`scored` 299 · `dropped_missing_axis` 0.**

**The news axis is DEAD this run, and the cause is the pipe, not silence — probed, not assumed.**
Two sweeps four minutes apart on one price frame returned **16.4%** then **0.0%** coverage; the
tunnel answered **3475** on `Nvidia` before them; a 40-name hand probe drawn from the sweep's own
silent set returned **40/40 valid with zero true silences** (`BLK` 258/1119 · `IBM` 96/568 ·
`NOW` 80/362 · `ADI` 68/135). Cumulative: **360 hand-checks, 0 false silences.**
⇒ **No sector or name may be called "quiet" from this file.** Tags are citable as **3-axis
unanimity**, never as news-confirmed.

🚨 **And this run may not compare its breadth to any run before 08-22** (`R96`, filed at HANDOVER).
The persisted sweeps of **08-18 · 08-19 · 08-20 · 08-21** all carry `vel_coverage` **16–17%**, and
partial coverage biases the tag layer **outward in both directions** — measured today on two
persisted runs of one price frame: `MRVL`/`MA`/`CVX` 🟢→🟡, `MS`/`JPM` 🔴→🟡, `WMT` 🟡→🔴.

⚠ **`top1_flips_sign` — the full list, handed to ROTATION: 1 of 11.**
**Consumer Staples · `top1` = `WMT` · `top1_w` 28.9%** (`wflow` −0.013 → `wflow_ex_top1` **+0.116**).
**ROTATION may not promote or demote Consumer Staples on `wflow`.** The other ten print
`top1_flips_sign = false`.

⚠ **Held-but-not-in-universe check: PASS on coverage, FAIL on staleness.** All **11/11** US book
names are inside `us_top300.csv` **and scored**. But the universe file is **39 days old** (limit ≤8),
and **`EA` has no close on any of the last four bars** — 299 scored of 300, **11th consecutive run**.
`EA` is **unmeasured, not quiet**; no flow/RS/OBV/short statement about it is admissible.

## 1 · Universe headline — three numbers

**n = 299 · `wflow` −0.076 · 🟢 6 : 🔴 71.**

⚠ **All three are identical to the 08-22 file, to the decimal.** `asof` **2026-08-21** both runs;
**0 of 299 scores moved, 0 of 299 tags moved, 0 of 11 sector `wflow`s moved.** There was no session.
**This is not a delta and is not presented as one.**

## 2 · ★★★ The cross-check that matters: the 🟢 gate is one axis, and it is the axis measured negative

The MACRO matrix (§E) ranks **Health Care OW** and **Energy OW** on price and `eqflow`. The shortlist
returns **zero names from Energy** and **one from Health Care**. That looks like a contradiction. It
is not — it is a **filter artifact**, and this run quantified it:

| Gate leg | Names passing (of 299) |
|---|---:|
| OBV 매집 **AND** rs20 > 0 | **94** |
| … **AND** `vol_surge` ≥ 1.2 (the 🟢 tag) | **6** |
| ⇒ **blocked on the volume axis alone** | **88 (29.4% of the universe)** |

**Blocked-by-surge, by sector:** Health Care **18** · Information Technology 15 · Financials 13 ·
Consumer Discretionary 11 · Industrials 8 · Communication Services 8 · **Energy 6** ·
Consumer Staples 5 · Materials 2 · Real Estate 2.

★★ **The Energy absence is diagnosed, not cited.** `PSX` (surge **1.11**), `MPC` (**1.06**) and `COP`
(**1.05**) are all OBV-accumulating with rs20 **+13.8 / +13.0 / +8.5** and rs60 **+37.0 / +44.0 /
+15.1**. **All three fail the 🟢 tag on the volume axis and nothing else.** This reproduces the
protocol's own recorded precedent (*"an ENRG shortlist of 0 turned out to be a 🟢-tag filter
artifact"*) for at least the second time. ⇒ **ROTATION must not read Energy's shortlist zero as
evidence against the Energy OW.**

★★★ **And the axis doing all the blocking is the one the desk's own scoreboard measures as
significantly NEGATIVE.** `ic_ledger score`, re-run this morning: `vol_surge` **h=1 t(NW) −3.86
(`n_eff` 34.0)** and **h=5 −3.38 (`n_eff` 5.4)**, both past Bonferroni **|t| > 2.8**, same sign.
🚫 **`W1` bars this desk from acting on it** — the ledger is **`market=kr`, 729 rows**, and the US
desk has no IC accrual of its own (`D310`, open two runs).
⇒ **What may be said, and it is now quantified rather than asserted:** *the discovery gate admits
6 of 94 otherwise-qualifying names, and the 88 it rejects are rejected by an axis whose only
measurement — in another market — says it predicts the wrong way.* **Every 🟢 cited downstream today
carries that sentence.**

## 3 · Shortlist composition — read as absences

**6 names** clear `mcap ≥ $10B` **AND** 🟢 (see `US_LIVE_SHORTLIST.json`). **Six sectors return zero:
Energy · Consumer Discretionary · Communication Services · Industrials · Real Estate · Utilities.**

Diagnosis, per sector, because an absence is only evidence once its cause is named:

- **Energy (0)** — **filter artifact.** Six names blocked on `vol_surge` alone, including both held
  refiners (§2). **Not evidence.**
- **Industrials (0) · Real Estate (0) · Utilities (0)** — **evidence.** These are the three worst
  `eqflow` sectors (−0.231 / −0.446 / −0.621) with 🔴 counts of **15 / 6 / 13**. Utilities is 🔴 on
  **13 of 15 names.** The absence agrees with the tape.
- **Consumer Discretionary (0)** — **mixed.** 11 names blocked on surge, and `eqflow` is positive
  (+0.103), but breadth is **0.000** and 🔴 = 5. Absence is **half filter, half tape**; ROTATION
  should treat it as undecided rather than as either.
- **Communication Services (0)** — **structurally unreadable.** 8 names blocked on surge in a
  12-name sector, and `D297` is unfixed: `GOOG` is a **second 38.3% row**, so the Alphabet complex is
  **76.6%** of the sector while `top1_w` reports 38.3%. **The flipper guard is blind here by
  construction**, so no absence claim is made at all.

⚠ **Two of the six shortlist names are bitcoin beta** (`COIN` Financials, `MSTR` classified
Information Technology). That extends `M805`'s Financials observation to the whole universe:
**a third of this run's entire green set is one factor.** The lone "clean rise" verdict (🟢 + short
covering) is `MSTR` — i.e. **the cleanest name on the board is the most factor-concentrated one.**

⚠ **`TGT` is on the shortlist while `WMT` is the flipper that owns Consumer Staples' sign** — a
**17.1pp** intra-sector spread on one window (`W5`). The shortlist and the sector verdict point
opposite ways **and both are correct**; this is the sector ROTATION may not resolve on `wflow`.

## 4 · CYCLE_EXPOSURE — no GAP, and one cycle that cannot be measured at all

`cycle_exposure.py` (book read-only, total ≈ **$11,067** / 15,272,249원, invested **$5,126**):
**AI-compute epicenter 16.52%** (need ≥12.0) ✅ · **Energy/refining 9.84%** (need ≥8.0) ✅ ·
Missile-defense 3.79% ⚪ (no threshold set). **Verdict: no top-rank cycle GAP.**

🚨 **But the registry still has NO ROW for the optical/interconnect cycle** (`D250`/`M731`, unfixed
for weeks). `S86` and `S96` both settled **B**, and the three names have re-converged downward
(`LITE` +0.639 — **and `LITE` is itself in the blocked-88, surge 0.95** — `COHR` +0.158,
`CIEN` −0.380 🔴 rs60 −34.0). ⇒ **Exposure to that cycle is UNMEASURABLE, not zero**, and the ✅
verdict above is a statement about three registered cycles, not about the book.

## 5 · What this file hands ROTATION

1. **Consumer Staples is un-promotable and un-demotable on `wflow`** (`WMT` 28.9%, sole flipper).
2. **Energy's shortlist zero is a filter artifact and must not count against the Energy OW.**
3. **Industrials / Real Estate / Utilities absences ARE evidence** and agree with `eqflow` and 🔴 counts.
4. **Every 🟢 today is a `vol_surge` selection**, on an axis measured negative in the KR ledger
   (`W1`-blocked). 88 names were rejected by that axis alone.
5. **No breadth comparison to any run before 08-22** (`R96`), and **no delta of any kind** — the frame
   is byte-identical to the prior run's.
