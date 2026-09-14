# SWEEP_READ — industry_US · 2026-09-14 (Mon) · Stage 4 / L1·SWEEP — the reading, not the data

> Data: `SECTOR_FLOW_US.json` (**`--no-news` re-run 13:19–13:24, asof 2026-09-11**) · `US_LIVE_SHORTLIST.json`
> (13:46) · `../CYCLE_EXPOSURE.md/.json` (13:46). Quarantined: `_SECTOR_FLOW_US.mixed_news_1317.json` (sweep #1).
> ⚠ **The tape is a reprint of the 09-12 run's close** — `flow_score` diff 0/299, `tag` diff 0/299, `delta`
> identical (09-04 → 09-11). This file therefore records **what the instrument did today** and re-states the
> cross-checks only where the MACRO matrix (§E, Monday-delta column) gives them a new counter-party.

## 0 · Instrument health line, read first (`scoring` block, load-bearing file)
`{vel_axis: false, vel_coverage: 0.0, n_axes: 3, scored: 299, dropped_missing_axis: 0}` — **news axis dead this
run, and the cause is the PIPE, measured three ways** (PREFLIGHT G1): remote alive at 13:16 (NVIDIA 1,453 / 7d),
dead from 13:19 (`URLError`, 0/8 retries), local fallback pool `7d == 30d` for every probed name.
🚨 **Sweep #1 (news axis ON) was quarantined**: coverage 62.9% (188/299) → `flow_score` dropped the axis
correctly, **but `flow_tag` kept using it** — 139 names at `velocity ≡ 4.29` (local-pool artifact) produced
**33 🟡→🟢 · 12 🟡→🔴 · 11 🔴→🟡 · `new_green` 4 → 36** on a tape with **zero** score change. The load-bearing
file is the `--no-news` re-run (3-axis, same mode as every run since 08-09). `D603`/`D604` registered at
HANDOVER. ⇒ **Nothing in this run may cite a 🟢 count, `new_green`, or a tag from sweep #1.**

## 1 · Universe headline (3 numbers)
**n = 299** (300 requested; `EA` unscored) · **wflow −0.169** · **🟢 5 / 🔴 129** — identical to 09-12.

## 2 · Cross-checks against the MACRO matrix (§E) — confirm / contradict, and which side the money is on
1. **Energy OW — CONFIRMED on flow, but the tag filter still reads 0 🟢 of 16, and today the live tape adds a
   second split.** 11 of 16 Energy names are **OBV accumulating** (`VLO` +0.37 · `DVN` +0.44 · `MPC` +0.48 · `CVX`
   +0.34 · `PSX` +0.32 · `COP` +0.31 · `OXY` +0.27 · `SLB` +0.25 · `EOG` +0.21 · `FANG` +0.13 · `XOM` +0.09)
   with `vol_surge` 0.85–1.14 — **all 🟡 because none clears surge ≥ 1.2 while velocity is dead** (`D561`/`D11`,
   the 🟢 gate is OBV-*and*-surge-locked). The 0-🟢 is a **filter artifact, not evidence** (measured 07-21 class). RULE D6 exempt: OBV is cited here to diagnose the tag gate (OBV-and-surge lock), not to carry a sector verdict — the verdict stays MACRO's.
   `wflow` +0.470 vs `eqflow` +0.431 — breadth-led, not `XOM`-led (G3: no flip). **New today** (§A-4): barrel
   +2.85% / distillate crack ≈ −6.6 $/bbl **live** — the sweep cannot see it (asof 09-11); ROTATION must read the
   OW as *two legs moving apart*, not as one bucket.
2. **IT N → N+ candidate — the sweep still says the money did not follow the price.** `eqflow` −0.207, 23 🔴 of
   56, only 3 🟢 (`QCOM` `DELL` `HPE`, all OBV accumulating with surge ≥ 1.22) against `exc5` +3.40 / breadth 40/56 on
   price (§E). **Contradiction carried, not resolved**: price ran, flow did not — the same reading as 09-12,
   and `NQ=F` −1.25% live is the first counter-tick. `P111` / `S148` settle tonight.
3. **Utilities / Real Estate / Staples — CONFIRMED as one object on flow too**: `eqflow` −0.273 / −0.351 /
   −0.059, 🟢 0 / 0 / 0, 🔴 9/15 · 6/12 · 7/19. `S135`-A (settled) plus this = the UW trio is one duration bet
   on price *and* on flow. 🚫 STPL on `eqflow` only (G3 flipper: `WMT`).
4. **Financials N− candidate — flow agrees with the price split**: `eqflow` −0.269, 14 🔴 / 47, 1 🟢 (`AIG`,
   the only Financials ignition, FINRA z +1.36 △). The bucket's one 🟢 is an insurer, not an exchange or a
   bank — consistent with §E's rates-sensitivity split.
5. **Industrials UW− — the most 🔴 bucket on the board**: 34 🔴 of 50, 0 🟢, `eqflow` −0.470. Confirms.
6. **Communication Services — unrankable (G3)**; the sector's single 🟢 is `META` (OBV accumulating +0.24, surge 1.22) —
   a **name**, carried as such.
7. **Materials N− — 0 🟢 / 6 🔴 of 12, `eqflow` −0.200**: confirms; `C24` (copper COT 100th) remains the
   contradiction with no equity counterpart.

## 3 · Shortlist — read the absences
`US_LIVE_SHORTLIST.json`: 5 names (`QCOM` `META` `DELL` `HPE` `AIG`; floor $10B, tag 🟢, top 15) — **identical to
09-12**. ✅ clean rise (🟢 ∧ low-short): `DELL` only (z −0.95). Absences:
- **Energy 0 / Health Care 0 / Utilities 0 / Materials 0 / Staples 0 / Discretionary 0 / Industrials 0 / RE 0.**
  Energy's 0 is the **filter artifact** diagnosed in §2-1 (11 OBV-accumulating names tagged 🟡). Industrials',
  Discretionary's, Utilities', RE's zeros are **evidence** (🔴-dominated, negative `eqflow`). Health Care's 0
  is evidence on the week (`eqflow` −0.059, 8 🔴) but `P150`/`S133` are the rows that decide, not the tag.
- ⚠ **`news` column = `n/a` on all five** — the shortlist's news enrichment is dead with the pipe; the FINRA
  proxy is the only enrichment that ran.

## 4 · Held-but-not-in-universe · cycle-exposure GAP
- **Held-but-missing: 0** (11/11 US holdings in `us_top300.csv`, all scored) — but the file is **61 days**
  stale (G5); `LNG` / tankers (`P145`, `P152`) remain **outside** the universe and are scored by direct pull only.
- `CYCLE_EXPOSURE`: rank-1 AI-compute epicenter **17.23%** (need ≥ 12) ✅ · rank-2 Energy/refining **10.71%**
  (≥ 8) ✅ · rank-3 missile-defense 3.6% (no bar). **No GAP flagged.** ⚠ `D592` reproduces: held `AVGO` is
  **not** in the epicenter count (`NVDA`, `ANET` only); `HPE`/`DELL` in no layer; registry 59 days stale;
  the **shipping/tanker leg** (today's `P152`) and the **AI-IPO-supply** cluster (MACRO §B-1 #1) exist in no
  registry entry — carried to ALPHA's action bracket as *unmeasurable*, not as 0%.

## ✅ EXIT CHECK — SWEEP
- [x] `scoring` block quoted; coverage < 80% ⇒ "news axis dead this run", cause = pipe, **probed** (3 ways).
- [x] `top1_flips_sign` list: **Consumer Staples / `WMT` 28.9%** (flag) + **Comm. Services / Alphabet 76.6%**
      (issuer-level, flag `False`) — handed to ROTATION.
- [x] Held-but-not-in-universe check run: 0 missing; universe staleness 61 d stated.
- [x] Sweep done (`--no-news` file load-bearing; sweep #1 quarantined with the reason).
- [x] Shortlist written; FINRA verdicts read; `news` enrichment `n/a` stated.
- [x] CYCLE_EXPOSURE read: no GAP; `D592` reproduction and two unregistered legs handed to ALPHA.
- [x] No table reprinted from the JSONs; ≥1 confirm (UW trio, INDU, FIN) and ≥1 contradiction (IT price vs
      flow; Energy 0-🟢 filter artifact) stated with the side the money is on.
