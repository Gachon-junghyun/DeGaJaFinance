# SWEEP_READ — industry_US · 2026-09-05 (Sat) · Stage 4 / L1·SWEEP

> **The reading, not a second copy of the data.** Numbers live in `SECTOR_FLOW_US.json` and
> `US_LIVE_SHORTLIST.json`; this file carries only what those cannot say. Sector rows and per-name
> rows are **cited by artifact, never reprinted**. Not load-bearing — it exists to feed ROTATION §2.

## 0 · Instrument health line, read BEFORE the numbers

`SECTOR_FLOW_US.json §scoring` = `{vel_axis: false, vel_coverage: 0.1639, n_axes: 3, scored: 299,
dropped_missing_axis: 0}`, asof **2026-09-04** (a settled Friday close).

🚨 **The news axis is DEAD this run — and the cause is the PIPE, probed, not assumed.** Coverage
**16.39% (49/299)** against an 80% bar. `PREFLIGHT §G1` ran the falsification: the identical query is
**6/6 alive before the sweep**, **0/4 immediately after**, dead at t+20s and t+40s, and **alive again
at t+60/+80/+100s**. Sweep coverage is universe positions **0–48 and nothing from 49 to 299**, zero
exceptions. ⇒ **the sweep's own burst trips the tunnel at ~49 names / ~98 queries and then hammers a
dead endpoint that needs ~60 idle seconds.** This is not evidence about the news.
⇒ 🚫 **No velocity or freshness number from this file is citable anywhere in this run** — including
the 49 that did score, because they are the 49 largest caps, a size-selected sample.
✅ `n_axes = 3` on both sides of the Δ and `dropped_missing_axis = 0`: **all 299 scored on the same
scale**, and `prev` resolves to 09-03 (`nonews`, 298) ⇒ **the Δ column is a true one-session
difference and is citable** (the 09-04 run's blanket Δ revocation is lifted).

## 1 · Universe headline — three numbers

**n = 299 · `wflow` −0.153 · 10 🟢 / 92 🔴.** (09-03: 12🟢/89🔴.) Breadth deteriorated on both sides.

## 2 · `top1_flips_sign` list, handed to ROTATION in full

**One flipper of eleven: Consumer Discretionary / `AMZN`** (`top1_w` 40.2%), `wflow` −0.255 →
**+0.068** ex-top1. ⇒ ROTATION may not promote or demote CD on `wflow`.
⚠ **And the flag misses the larger case, for an 11th run** (`D459`): Alphabet is **76.6%** of
Communication Services **under two tickers**, so the per-ticker flag prints `False` while
ex-both-classes `wflow` goes **−0.389 → +0.272** (swing **0.661**). ⇒ **ROTATION may not use `wflow`
on Comm. Services either.** `eqflow` is the citable cut for both buckets and must be named on the line.

## 3 · Held-but-not-in-universe check — ✅ clean, freshness ❌

All **11** US book holdings are in `us_top300.csv`; **missing 0** (`PREFLIGHT §G5`). The desk can tag
everything it owns. ⚠ **The file is 52 days old**, so every cap weight in this sweep — including
`top1_w%` — is stale and may not be cited as current size.

## 4 · Cross-checks against the MACRO matrix — where flow CONFIRMS and where it CONTRADICTS

**✅ CONFIRMS — Energy, on every axis at once, and this is the run's strongest agreement.**
Energy is **3 greens of 16 = an 18.75% green rate; every other sector on the board is ≤ 4%**. It is
also the **only sector with ZERO reds** out of eleven. Add MACRO §E's price legs (`exc5` +1.89 with
1/16 negative, `exc20` +12.29) and the flow Δ turning positive, and **five independent instruments
point the same way on the same label.** ★ This also resolves the 09-04 run's flagged tension — level
said rank-1, Δ said rank-11 — **toward the level, in one session** (Δ −0.151 → **+0.054**).
⚠ The one instrument that disagrees is the **narrative** (`crude oil` −14.7%, `refining margin` 0.66×
for a 3rd run), which is exactly why MACRO registered `P136` instead of concluding.

**🚨 CONTRADICTS — Industrials is the worst sector on level and the best on Δ, and the flow breadth
says the level is right.** `2🟢 / 28🔴 of 50` is the board's worst red rate (**56%**), matching
`exc20` −5.04 with 33/50 negative. **The +0.082 Δ is the board's largest and it is not broad** — it
sits in `VRT` +0.444, `NSC` +0.403, `GWW` +0.352, `CAT` +0.352, i.e. four names inside a 50-name
bucket. ⇒ **ROTATION should read the Industrials Δ as a four-name event, not a sector turn.**

**🚨 CONTRADICTS — IT's single-session leadership is not in the flow object at all.** MACRO §E has IT
at the board's best `exc1` (**+1.52**, `SMH` +2.61% on the payroll session), yet IT scores
**1🟢 / 17🔴 of 56** and `eqflow` −0.195. **The reconciliation is in the Δ column and it is specific:
the board's three largest positive Δs are `STX` +0.728, `WDC` +0.718 and `AMD` +0.566 — storage and
semis.** ⇒ **the payroll-session rip is a memory/storage/semis event inside a sector whose other 53
names did not participate.** That is a node call, not a sector call (`W5`), and it is the same object
`P101` just settled from the other side (software −4.46% vs hardware +2.05%).

**⚠ CONTRADICTS — the largest single-name Δ reversal on the board is on a name the ledger is
watching.** `AXON` carried the board's **largest positive clean Δ (+0.838)** on 09-03 — the 09-04
HANDOVER named it and told EVENT_ALPHA to look deliberately — and today it is **−0.702, the board's
worst**. A **1.54 swing in one session.** Handed to EVENT_ALPHA as a fact, not a verdict (P4).

**⚠ Utilities: the flow says nothing, and the one number that moved is a single name.** `eqflow`
+0.050 with **0 greens / 3 reds of 15** and breadth 0.00, while `VST` carries **Δ +0.491**, the
board's 4th largest — on a name that sits under a **standing rejection** (`VST`, 08-14 `G.섹터중립`,
reaffirmed 09-04 because its OBV missed the accumulation cut by **0.003**, `C5`). ⇒ **the AI-power
object is again split across two labels** (`ETN` in Industrials, `VST` and `VRT` elsewhere) — `D416`,
and `P123` settles 09-08.

## 5 · Shortlist composition — the ABSENCES, each diagnosed

`US_LIVE_SHORTLIST.json`: **10 names** at mcap ≥ $10B, tag 🟢가속 (filter is stated in the artifact).

- **Energy supplies 3 of 10 from a 16-name sector.** Every other sector supplies ≤ 2 from 12–56
  names. This is the sharpest composition fact on the board and it is **evidence, not a filter
  artifact** — the sector also has the board's only zero-red row.
- **Four sectors supply ZERO: Utilities, Consumer Staples, Communication Services, Real Estate.**
  **Diagnosed, not cited raw:** all four have **0 greens in the underlying JSON**, so the absence is
  upstream of the shortlist filter, not caused by it. ⚠ But three of the four are the
  **rate-sensitive** buckets, and MACRO §A has nominal yields at the **96th–99th percentile** — so
  the absence has a mechanism and is not noise. **Comm. Services is the exception and is a
  measurement absence, not an economic one**: its aggregate is unusable at all (`D459`), so "zero
  greens" there is a fact about 12 names, 76.6% of which are one company.
- **IT supplies 1 of 56.** ⚠ **This is the absence most at risk of being over-read.** The 🟢 gate
  requires `vol_surge ≥ 1.2` alongside OBV and RS (`M25`), and MACRO's own COT read has
  Nasdaq-100 spec longs at the **82nd percentile** while `vix` sits at the **2.4th** — a low-volume
  melt-up produces exactly this shape. ⇒ **IT's 1-of-56 should be read with the surge axis named**,
  not as breadth evidence on its own.
- **⚠ The 🟢 gate's own axis is under an open contradiction.** `C29` (opened this run): the KR
  `ic_ledger` scores `vol_surge` h=1 at **IC −0.0414, t(NW) −3.61, n_eff 45**, clearing Bonferroni
  for a third run — **a significantly NEGATIVE sign on the axis this gate weights positively.**
  `W1` bars importing that conclusion to the US board and the US desk has no ledger of its own
  (`D395`/`D428`). ⇒ **every 🟢 tag in this shortlist is reported with that caveat attached**, and
  no stage may treat a 🟢 as evidence without saying which axis lit it.

**New-🟢 ignitions (day-over-day): `HOOD` (FIN, Δ +0.039) · `WMB` (ENRG, Δ +0.347) · `RSG` (INDU,
Δ −0.091).** ⚠ Only `WMB` ignited on a **rising** Δ; `RSG`'s Δ is **negative**, i.e. it crossed the
tag threshold while its own score fell — a tag change that is not a flow change.

## 6 · Cycle-exposure GAP (`CYCLE_EXPOSURE.md`, written to the day-folder root)

✅ **No top-rank cycle GAP.** Real KIS book: total ≈ **$11,022**, invested **$5,255** (52.3% cash).
AI-compute epicenter **17.48%** (bar ≥12%) · Energy/refining **10.47%** (bar ≥8%) ·
missile-defense 3.64% (no bar set). **Nothing is handed to ALPHA's action bracket from this axis.**

---

> Analytical artifact. No sizing, no buy/sell language (P4). `⚡crowded-short` in the shortlist is
> squeeze **fuel on a turn condition**, never a standalone read — and `[FINRA]` short volume includes
> market-maker hedging (`D6`), which is the exact ambiguity `P137` was registered to test.
