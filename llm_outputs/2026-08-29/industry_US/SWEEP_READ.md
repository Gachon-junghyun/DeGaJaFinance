# SWEEP_READ — industry_US · 2026-08-29 (Stage 4 / L1·SWEEP)

> The reading, not a second copy of the data. Numbers live in `SECTOR_FLOW_US.json` and
> `US_LIVE_SHORTLIST.json`; **no table from either is reprinted here** (the 2026-07-21 measurement:
> 100% of tickers and 97% of numbers were restatement).

## 0 · 🚨 Instrument health line — read before any number below

`SECTOR_FLOW_US.json §scoring` = **`n_axes` 3 · `vel_coverage` 0.0% · `scored` 299 ·
`dropped_missing_axis` 0.**

**The news axis is DEAD this run at 0.0%, and this run caused it.** Measured, not inferred:

| attempt | time | `vel_coverage` | what happened in between |
|---|---|---|---|
| sweep run 1 | ~22:45 KST | **16.72%** (50/299) | — |
| sweep run 2 | ~22:52 KST | **0.0%** (0/299) | **run 1's own 299 velocity queries** |

⇒ **`M1060`** `[measured]` **The velocity coverage of a sweep is a function of the request load that
preceded it, not of the news.** Nothing else changed between the two runs but the queries run 1 made.
This is `M1027`'s rate-dependent sticky ban observed from the other side, and it explains why the
covered prefix has been a stable ~50 for five runs: **each run gets one pre-ban budget, and the sweep
spends it in its first ~50 calls.**
🚫 **"No news" is not available as a reading.** The pipe answered `Marvell` **482** and `Broadcom`
**549** by hand today (PREFLIGHT G1, HANDOVER §2b). Every G1 removed right binds, and binds harder
than the 16.7% baseline PREFLIGHT scored: **this run's own file is at zero.**

## 1 · Universe headline — three numbers

**n = 299 / 300 · `wflow` −0.114 · 🟢 8 / 🔴 75.** `asof` **2026-08-27** (settled).

⚠ **`asof` is 08-27, not 08-28, and that is deliberate.** See §2.

## 2 · 🚨 The sweep died once before it produced this file, and the repair is a measurement

**`M1059`** `[measured]` **The first sweep of the day returned `scored: 0 / dropped_missing_axis: 299
/ n: 0` — a complete kill — and its `asof` still printed `2026-08-28`.** Cause, measured in the
sweep's own price cache (`llm_outputs/sector_flow/prices_2026-08-29.pkl`, backed up before touching):
the **2026-08-28 row carries `Close` on 0 of 301 tickers while `Volume` is present on 300 of 301.**
The 08-27 row carries `Close` on 300/301.

- This is the **US-universe-scale** version of what HANDOVER §2e found on nine names, and the
  **KR desk's `M1026`** found on 831 of 833 KR names this morning. ⚠ **Not a transfer — measured here,
  on this universe** — and the **signature still differs from KR's**: KR lost all of OHLC; **US loses
  `Close` only and keeps Volume on 300/301**, so the phantom row looks like a real session to any
  check that counts rows or looks at volume.
- **Repair applied, and it is the KR run's own valid path**: truncate the phantom row and score the
  **08-27 settled bars** with the native bench. Re-run: **299 scored, `asof` 2026-08-27.**
- ★ **`D401` is confirmed by this, not merely asserted**: the dead file's `asof` said **08-28** while
  scoring **nothing**, because `asof` is taken from the bench frame's last index date and a
  Close-less row satisfies it. **The `asof` field cannot distinguish a settled bar from a phantom one.**
- 🚫 **Δflow is NOT usable this run and no Δ is cited below.** The 299 `delta` values in the JSON
  difference **today's settled 08-27 bar** against **the 08-27 file's intraday 08-27 bar** — two
  different measurements of the same date (`D401`). The field is populated; it is not comparable.

## 3 · 🚨 The flipper list handed to ROTATION — it GREW from 2 to 4, on the same desk, in four hours

PREFLIGHT G3 read the 08-28 baseline (intraday bar) and found **2 of 11**: IT/`NVDA`, HLTH/`LLY`.
**Today's own file (settled bar) finds 4 of 11** — `SECTOR_FLOW_US.json §sector_rotation`:

| sector | `top1` | `top1_w` (wflow) |
|---|---|---|
| Information Technology | `NVDA` | +0.008 |
| Health Care | `LLY` | −0.027 |
| **Energy** | `XOM` | −0.051 |
| **Consumer Discretionary** | `AMZN` | −0.136 |

⇒ **`M1061`** `[measured]` **`R108`'s class reproduces on the US desk, under a different
perturbation.** `R108` (filed this morning, KR) showed the flipper set moving **5 → 3** when only the
**bench bar** was aligned. Here the flipper set moves **2 → 4** when only the **terminal bar** is
moved from intraday to settled — same universe, same axes, same formulas, same session label.
**This is a US-side measurement, not a `W1` transfer of the KR magnitudes.**
🚫 **ROTATION may not promote or demote IT, Health Care, Energy or Consumer Discretionary on the
weighted-flow bucket**, and per `R108` may not treat the other seven as clean on that basis either —
the flipper list withholds, it does not clear.

## 4 · Cross-checks against the MACRO transmission matrix — where the money disagrees with the wind

★★ **The structural finding, and it is one sentence**: **`eqflow` is positive in only 3 of 11 sectors
— Health Care (+0.102), Energy (+0.092), Information Technology (+0.060) — and all three are
`top1_flips_sign` = True.** Every sector with positive breadth is a sector where the flipper guard
forbids a weighted-flow move. The guard is biting on exactly the buckets that carry the information.

| MACRO said | sweep says | verdict |
|---|---|---|
| **Health Care `N`** (worst `exc5` on the board, −2.456pp vs `SPY`) | **the board's HIGHEST `eqflow`, +0.102**, on the widest breadth read | 🚨 **Sharpest contradiction on the board.** The ETF is the worst performer and the median constituent has the best money flow. G5 says prefer `eqflow`; G3 forbids moving it on `wflow`. **Handed to ROTATION unresolved rather than split by picking a side** |
| **Energy `N`** (`exc5` −1.983pp vs `SPY`) | **`eqflow` +0.092, 2nd-highest**, `wflow_ex_top1` **+0.168** = the largest ex-top1 positive of 11 | **Contradiction, same shape**: `XOM` alone carries the sector negative. Consistent with `M952`'s refiners-vs-E&P split |
| **Info Tech `N`** | `eqflow` **+0.060** (positive) but `wflow_ex_top1` **−0.121** (negative) | **Confirms MACRO's `N`, and explains it**: equal-weighted positive, cap-weighted-ex-`NVDA` negative. `M1050`'s "worst 1-day, best 5-day" is the same object |
| **Financials `OW−`** (`exc5` +0.605pp vs `SPY`) | `wflow` −0.144 **and** `eqflow` −0.144, identical, no flipper | 🚨 **Contradiction with no instrument defect to hide behind** — both flow reads agree and both are negative, while the settled tape is positive. **ROTATION must resolve this or downgrade the `OW−`** |
| **Comm Svcs `OW`** (best on both windows) | `wflow` −0.260 but `eqflow` **−0.004** ≈ flat | **Partial contradiction that the G5 rule resolves**: the cap-weighted read is 45-day-stale-weighted; on breadth the sector is flat, not negative. **The `OW` survives on `eqflow`, weakened** |
| **Materials `UW`** (Copper spec at the **100th** percentile) | the **only positive `wflow` (+0.028)** but `eqflow` **−0.020** | **Contradiction inside the sweep itself** — mega-cap-led up, breadth down. G5 ⇒ `eqflow` is citable ⇒ **the `UW` holds**, and `FCX` is a new-🟢 inside a negative-breadth sector |
| **Utilities · Real Estate · Cons Staples · Industrials `UW`** | the four worst `wflow`/`eqflow` pairs on the board, both negative in every case | ✅ **Confirmed, unanimously.** The only part of the matrix where flow and wind agree without qualification |
| **Cons Disc `N`** | `eqflow` **−0.325**, 2nd-worst; flipper (`AMZN`) | Contradicts MACRO's `exc1` +1.375pp read; the 1-day pop is not in the money flow |

## 5 · Shortlist composition — read the ABSENCES, and both big ones are the same artifact

**8 names** (`US_LIVE_SHORTLIST.json`; filter mcap ≥$10bn ∧ tag `🟢가속` ∧ flow-desc top-15).
**4 of the 8 are Information Technology** — the sector MACRO set to `N`.

**6 of 11 sectors produced ZERO**, and the two that matter were diagnosed before being cited:

- 🚨 **Energy: 0 names, and it is a FILTER ARTIFACT, not evidence.** Energy has the board's 2nd-highest
  `eqflow` and **`MPC` `SLB` `PSX` `COP` `VLO` `WMB` `OXY` `CVX` are ALL `OBV 매집` with positive
  `rs20`** — and every one is tagged `🟡중립` because **`vol_surge` < 1.00 on all of them**
  (`MPC` 0.99, `SLB` 0.83, `PSX` 0.84, `VLO` 0.69). The 🟢 tag needs a volume surge; the sector never
  gets one. **This is the exact artifact logged on 2026-07-21 and it has reproduced.**
- 🚨 **Comm Svcs: 0 names, same artifact, and it is MACRO's `OW`.** `WBD` +0.56 / `DIS` +0.59 /
  `CMCSA` +0.39 / `META` +0.29 are all `OBV 매집` with positive `rs20`, all `🟡중립`, all
  `vol_surge` < 1.00 (0.79 / 0.79 / 0.55 / 0.91). ⇒ **the sector MACRO ranked best on the settled
  tape cannot produce a shortlist name by construction.**
- **Utilities · Real Estate: 0 names, and this one IS evidence** — both sit at the bottom of the board
  on `wflow` **and** `eqflow`, so their absence agrees with their flow rather than being produced by
  the filter.

★★ **`M1062`** `[measured]` **The shortlist gate is `vol_surge`, and `vol_surge` is the one axis this
desk has measured as NEGATIVELY predictive at a Bonferroni-passing significance** (`ic_ledger score`:
h=1, n=39, n_eff 39.0, mean IC **−0.0444**, t(NW) **−3.84**, **★유의(다중비교 통과)**; h=5 agrees in
sign). ⇒ **the filter that decides which names reach ROTATION is gated on a signal whose measured
sign is the wrong way round**, which would systematically drop the accumulating-without-a-surge names
— which is precisely what Energy and Comm Svcs look like today.
🚫 **`W1` binds and is not evaded**: that IC ledger is **KR-labelled**. The US-side measurement does
not exist and is registered as `D395` (unmet, 2nd run). **This is carried as a KR-measured result with
an unmeasured US implication** — but the *filter code is shared*, so it is named here rather than
withheld. **No gate is changed** (P4).

## 6 · Invariants checked

- ✅ **Held-but-not-in-universe: 0.** All 11 US book names (`ANET AVGO ETN HPE MET MPC NDAQ NUE NVDA
  PSX RTX`) are inside `us_top300` (n=300) — PREFLIGHT G5 coverage leg, re-cited not re-run.
  ⚠ The **freshness** leg still fails: the universe file is **45 days** old, so `wflow`'s weights and
  the coverage frontier are both stale (G5).
- ✅ **Cycle-exposure GAP: none.** `cycle_exposure --json` — AI-compute epicenter **16.93%** (need
  ≥12.0%, holds `NVDA`/`ANET`), Energy/oil-refining **9.97%** (need ≥8.0%, holds `MPC`/`PSX`),
  missile-defense 3.83% (⚪ no threshold set — **`RTX`'s cycle still has no bar, and `W4` is unpaid on
  it for 210 days**). **No 🚨 to hand to ALPHA's action bracket this run.**

## 7 · What ROTATION inherits from this stage

1. **Four restricted buckets** (§3), not two — and the restriction withholds, it does not clear (`R108`).
2. **Three contradictions to resolve**: Health Care (tape worst / breadth best), Financials (tape
   positive / both flow reads negative, no instrument defect available), Cons Disc (1-day pop absent
   from the flow).
3. **Two sectors that cannot produce a candidate by construction** (Energy, Comm Svcs) — so their
   absence from any shortlist-derived ranking is **not** information.
4. **No Δflow.** Any "it improved / deteriorated" claim this run has no legal instrument behind it.
