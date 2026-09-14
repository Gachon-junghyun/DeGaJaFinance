# SWEEP_READ — industry_US · 2026-09-07 (Mon, US Labor Day) · Stage 4 / L1·SWEEP

> **A reading, not a report.** Every sector row and every shortlist row lives in
> `SECTOR_FLOW_US.json §sector_rotation` / `§names` and `US_LIVE_SHORTLIST.json` and is **cited, not
> reprinted**. What follows is only what those files cannot say.

## 0 · Instrument health line, read BEFORE the numbers

`SECTOR_FLOW_US.json §scoring` = `{vel_axis: false · vel_coverage: 0.1739 · n_axes: 3 · scored: 299 ·
dropped_missing_axis: 0}`.

**🚨 The news axis is DEAD this run (17.39%, bar 80%) — and the cause is the pipe, not silence.**
Probed, not assumed: **6/6 named probes alive immediately before the sweep**, counts *moving* vs
yesterday (NVIDIA 3,841→**3,761**, samsung 1,590→**1,471**); **0/4 immediately after**; alive again
after ~2 min of probe-free idleness. The velocities that exist map to **universe ranks 1–52,
contiguous, zero gaps** (`us_top300.csv` rank order — **not** the JSON's array order, which is
`flow_score`-sorted). ⇒ **theme-freshness and velocity may not be cited from this file, including
for the 52 that carry one**, and **no sector or name may be called "quiet"** — 247 of 299 were not
measured. That is absolute for **Utilities, Materials and Real Estate: zero measured names each.**

`asof` **2026-09-04**, the third consecutive run on the same settled session (NYSE closed Sat/Sun and
Labor Day). Δflow is the **09-03 → 09-04** change and is not today's.

## 1 · Universe headline

**n = 299 scored** (301 downloaded, `EA` structurally absent, 300 in universe) ·
**cap-weighted flow across all 11 buckets = negative in 8, positive in 3** ·
**🟢가속 11 · 🔴분산 count from `§names`** — and the 🟢 count is the number to distrust, see §3.

## 2 · Cross-checks against the MACRO matrix

**① CONFIRM — Energy.** MACRO's only OW is the sweep's only bucket that is positive on *both* cuts
(`eqflow` +0.562 > `wflow` +0.440 ⇒ **breadth-led, not mega-cap-narrow**) with **15 of 16 names
positive** on 5-session excess. The money and the matrix agree, and they agree on the *broad* cut,
which is the one G5 permits today.
⚠ **But the sweep cannot confirm MACRO's Energy caveat and says so**: the deceleration MACRO found
(`Strait of Hormuz` 0.88× · `refining margin` 0.68×) is a **news-axis** reading, and this file's news
axis is dead. The two instruments are not independent confirmations here — one of them is blind.

**② CONTRADICT — Utilities.** MACRO carries **N−**; the sweep's flow is **positive on both cuts**
(`eqflow` +0.050 / `wflow` +0.071) while the price basket is **7 of 15 positive** with `exc5` mean
**+0.35** and median **−0.13**. **The money says mildly positive, the price says nothing, the matrix
says N−.** ⇒ **the contradiction is real and it is not resolvable by the sweep**: `D537` bars using
this bucket's sweep breadth (0.00) against it, because that zero is a `vol_surge` filter artifact.
**Handed to ROTATION as an open contradiction, not as a demotion.**

**③ CONTRADICT — Industrials.** The sweep's **largest Δflow on the board (+0.082)** sits on MACRO's
**worst 20-session basket** (`exc20` mean −5.04 / median −5.90). ⚠ That Δ is the **09-03→09-04**
change, already reported by two prior runs, so it is **not** evidence of a turn — it is the same
number for the third time. **Stated so ROTATION does not read a stale delta as an ignition.**

**④ CONFIRM — the two barred buckets stay barred, and one of them still supports a verdict.**
`top1_flips_sign` list, handed to ROTATION in full (`§sector_rotation`): **1 of 11 flips — Consumer
Discretionary, `top1` `AMZN`, `top1_w` 40.2%, `wflow` −0.255 → ex-top1 +0.068.** The issuer-level
rescan adds a **second, larger** one the flag cannot see: **Communication Services, issuer Alphabet
across `GOOGL`+`GOOG`, 76.6% of sector cap, `wflow` −0.389 → ex-issuer +0.272, swing 0.661.**
⇒ **ROTATION may not promote or demote either bucket on `wflow`.** For **Cons. Disc.** the
equal-weight cut (−0.280) **agrees with the barred sign**, so a verdict survives on `eqflow`; for
**Comm. Services** `eqflow` is **−0.035 = flat** and the price cuts contradict each other across
windows (`exc5` 2/13 positive, `exc20` median **+3.70**) ⇒ **no verdict is issuable.**
⚠ All `top1_w` figures rest on a **54-day-old** cap vector (G5) and are not current.

## 3 · 🚨 The shortlist's composition — and the finding is a defect, not a name

`US_LIVE_SHORTLIST.json`: **11 names** past the $10B floor and the 🟢가속 filter.

**★ The 🟢 tag applies two different gates depending on market-cap rank, and the looser one is
created by an axis this run declares dropped.** Measured across all 11 greens:

- The **7 greens without a velocity** (ranks 77–230) all carry `vol_surge` **1.21–1.47** — i.e. they
  cleared a ~1.2 surge gate.
- The **4 greens with a velocity** are all at ranks **8 · 34 · 35 · 48** — inside the news wall — and
  **two of them are below that surge gate**: **`PG` surge 0.89** and **`CVX` surge 0.99**.
- The decisive pair: **`PG` (rank 34, flow +0.231, surge 0.89, velocity 1.23) is 🟢**, while
  **`CEG` (rank 124, flow +0.644 — 2.8× higher — surge 0.96, velocity `None`) is 🟡**, and
  **`VST` (rank 220, flow +0.619, surge 1.02, `delta` +0.491 = the board's largest) is 🟡.**

⇒ **`velocity` substitutes for the `vol_surge` gate inside `flow_tag`, and `velocity` exists only for
universe ranks 1–52.** Because `scoring.vel_axis` is **false**, the same axis is simultaneously
excluded from `flow_score` and decisive for `flow_tag`. **The LIVE shortlist is therefore
cap-rank-biased by a dead axis** — `D537`/`M1369` sharpened from "an artifact on one name" to a
**structural rule with a measured cut-point**. Registered as **`D561`**.
⇒ **`PG` and `CVX` carry no citable 🟢 this run**, and **`CEG`/`VST` are absent for an instrument
reason, not a merit reason.** Both facts go to ROTATION and ALPHA.

## 4 · Read the ABSENCES, and diagnose each

| absent from the shortlist | diagnosis |
|---|---|
| **Utilities / independent power** (`CEG` +0.644, `VST` +0.619) | 🚨 **filter artifact, 2nd consecutive run** — blocked by the surge gate that §3 shows is not applied to the top 52. **Not evidence of absence.** |
| **Information Technology — 0 of 56 names** | ⚠ **mixed.** IT's `eqflow` is −0.195 and its `exc5` mean is −0.27 **but its median is +0.27 with 30 of 56 positive** ⇒ the bucket is split, not dead. A 🟢-tag filter cannot represent a split bucket. **Evidence of dispersion, not of weakness.** |
| **The held refiners** (`MPC` +0.694 / `PSX` +0.750, both OBV 매집 +0.62 / +0.43, `rs20` +30.8 / +25.5) | ⚠ **filter artifact** — both are 🟡 on `vol_surge` 1.05 / 1.15, just under the gate, while carrying the board's strongest OBV accumulation. **This is the exact absence class the stage's own field note warns about** (an ENRG shortlist of 0 that was a tag artifact). |
| **`XOM`** (rank 19, velocity 1.1, flow **+0.027**, OBV −0.071 중립) | ✅ **evidence.** A named beneficiary of MACRO's fastest-accelerating supply story sits **dead last of 16 in Energy** on flow, *with* a velocity — so this absence is measured, not filtered. Story-vs-tape contradiction, carried from 09-06 unchanged. |
| **`COP`** (flow +0.639, OBV +0.222 매집, `rs20` +14.6) | ⚠ **filter artifact** — `vol_surge` 0.95. The 09-06 run's only valid `chain-hop` candidate is invisible to the shortlist. |
| **Real Estate · Materials · Comm. Services — 0 names each** | ⚠ **not diagnosable this run.** All three have **zero news-measured names** (§0), so the desk cannot distinguish "no ignition" from "not measured". **Recorded as unknown, not as zero.** |

## 5 · Held-but-not-in-universe check

✅ **0 missing.** All **11** US holdings (`ANET` `AVGO` `ETN` `HPE` `MET` `MPC` `NDAQ` `NUE` `NVDA`
`PSX` `RTX`) are in `data/us_universe/us_top300.csv` **and** all 11 are scored in `§names`.
⚠ The universe file is **54 days stale** (mtime 2026-07-15), so this is a coverage pass on a stale
membership list — a name that entered or left the top 300 since 07-15 would not be reflected.
(The two KR holdings are out of scope for `--market us` by design.)

## 6 · CYCLE_EXPOSURE — no GAP, and the same silent rank-3

`CYCLE_EXPOSURE.md/.json` (day-folder root): **✅ no top-rank GAP.** AI-compute epicenter **17.51%**
(need ≥12.0) via `NVDA`+`ANET`; Energy/refining epicenter **10.49%** (need ≥8.0) via `MPC`+`PSX`.
🚨 **Rank-3 (missile-defense) still has NO bar set in `cycle_registry.json`** ⇒ the GAP check is
**silent on it by construction** while the book holds `RTX` at 3.65% — `M1374`'s exact finding,
reproduced, and it matters more now that `S150` brackets that node.
🚨 **`C23`, 11th reproduction**: `cycle_exposure` reads the real KIS book at **$5,255 invested of
$11,004 ⇒ 52.2% cash**, against `exposure_rule show`'s **stored 85.2% invested** whose *current*
field is **blank** (account query failed). **Nothing to hand to ALPHA's action bracket as a GAP; the
🚨 to hand forward is the instrument disagreement.**

---

> P4 — no sizing, no buy/sell language. Names appear as measurement subjects only.
