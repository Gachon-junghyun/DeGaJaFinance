# SECTOR_DEEP_COMM — Communication Services · industry_US · 2026-08-24 (Mon) · Stage 8 / L1·DEEP
### Rotating slot ① — last covered **2026-08-19 ≈ 5 runs** ⇒ **FULL FRESH MAP.**

> All flow figures `asof 2026-08-21`; `exc` = excess return vs **`SPY`** (named inline).
> ⚠ Declared deviation, 7th run: in-context serial execution, not a parallel agent fan-out.

## 0 · ROTATION's mandate — and the answer overturns a guard, not a grade

*"`participation` 66.7% (rank 1) against `green_rate` 0.0% (joint last). Is the 66.7% real breadth or
an artifact of a sector whose participating names all accumulate on sub-0.83 `vol_surge`? Handle
`D297` explicitly — compute ex-`GOOGL`-and-`GOOG`."*

★★★ **Answer: the breadth is real AND the guard is broken, and the second finding is bigger than the
first. `top1_flips_sign` reports `false` for this sector. Removing BOTH Alphabet share classes flips
`wflow` from `+0.108` to `−0.193`. The sector IS a flipper and the instrument cannot see it.**

## 1 · ★★★ `D297` is load-bearing for the first time — the sign flips when the real top holding leaves (`M877`)

| Cut | n | **wflow** | eqflow | exc5 vs `SPY` | exc20 vs `SPY` | participation | share of sector mcap |
|---|---:|---:|---:|---:|---:|---:|---:|
| **COMM as graded** | 12 | **+0.108** | +0.095 | +1.12 | +3.44 | **66.7%** | 100.0% |
| **ex-`GOOGL` ex-`GOOG`** | 10 | 🚨 **−0.193** | +0.075 | +1.15 | +3.36 | 60.0% | **23.4%** |
| ex-Alphabet **ex-`META`** | 9 | **+0.194** | +0.142 | +1.88 | +4.98 | 66.7% | **10.9%** |

- `SECTOR_FLOW_US.json` prints `top1 = GOOGL`, `top1_w = 38.3%`, `wflow_ex_top1 = +0.022`,
  **`top1_flips_sign = false`.** ✅ Arithmetically correct — and **wrong about the sector**, because
  `GOOG` is a **second 38.3% row for the same company**. **The Alphabet complex is 76.6%.**
- **Removing the complex: `+0.108 → −0.193`. The sign flips.** ⇒ **`D297` is no longer a
  hypothetical hole in the guard; it is a demonstrated false negative on a live sector, and it is this
  run's R1 DEEP pick precisely on a breadth number both Alphabet rows sit inside.** **5th run unfixed.**
- ★ **Then removing `META` (12.5%, flow −0.530 🔴, exc20 −11.23) flips it BACK to +0.194.**
  ⇒ **Three names decide this sector's sign in two directions, and the other nine names are 10.9% of
  its market capitalisation.** **`wflow` is not a usable instrument on COMM at any cut.**
- 🚫 **Consequence for ROTATION, already applied**: COMM's `N` stands. It stands **not** because the
  flow confirms it but because **the flow cannot be read** — and that is a different sentence, which
  BET must carry verbatim.

## 2 · Is the 66.7% participation real? — yes on the count, and it is uniformly volume-starved

The 8 participating names (`OBV 매집` ∧ `rs20 > 0`), with their `vol_surge`:

| Ticker | wt | flow | rs20 | rs60 | exc20 vs `SPY` | `vol_surge` |
|---|---:|---:|---:|---:|---:|---:|
| `WBD` | 0.6% | +0.539 | +7.2 | +3.2 | +7.16 | **0.83** ← the sector's maximum |
| `NFLX` | 2.8% | +0.483 | +9.9 | −10.9 | +9.93 | 0.67 |
| `DIS` | 1.5% | +0.478 | +10.0 | +1.4 | +10.01 | 0.66 |
| `CMCSA` | 0.7% | +0.461 | +16.8 | +4.4 | ★ **+16.78** | 0.63 |
| `GOOGL` | 38.3% | +0.245 | +4.2 | −13.4 | +4.22 | 0.62 |
| `VZ` | 1.6% | +0.197 | +3.0 | +0.5 | +2.99 | 0.53 |
| `GOOG` | 38.3% | +0.154 | +3.5 | −13.2 | +3.48 | 0.67 |
| `T` | 1.3% | +0.089 | +1.2 | −0.4 | +1.18 | **0.47** |

★ **Not one name in the sector reaches `vol_surge` 0.85, let alone the 🟢 gate's 1.20.** The
participation is genuine on OBV and RS and **structurally unable to green**. ⇒ **SWEEP's diagnosis
holds: `green_rate 0.0%` here is a filter artifact, not an absence of money.**
⚠ **But the horizon caveat from HANDOVER §6 binds hardest here**: the US ledger measures
**`vol_surge` h=1 as POSITIVE (`t +3.40`)**, so on US data the gate the sector fails is *selecting
for* 1-day forward returns. **"Blocked only by `vol_surge`" is not the same as "should have been
green."** Stated so it is not laundered downstream.
★ **The real leaders are the media/cable names, not Alphabet**: `CMCSA` **exc20 +16.78**, `DIS`
+10.01, `NFLX` +9.93 — all three above the sector's +3.44, and together **5.0% of its market cap.**

## 3 · Value chain, 7 nodes left → right, binding constraint marked

`content production` → `content rights / sports` → **`distribution: streaming vs cable` ← BINDING** →
`advertising demand` → `ad tech / measurement` → `connectivity (`T` `VZ` `TMUS`)` → `device / endpoint`

- **Binding constraint = distribution economics, not content supply.** The evidence is internal to the
  sector: the three names with the best 20-session excess (`CMCSA` cable, `DIS` and `NFLX` streaming)
  span **both sides** of the distribution question, while the two ad-funded platforms diverge violently
  — `GOOGL`/`GOOG` **exc60 −13.4/−13.2** and `META` **exc60 −15.47, flow −0.530 🔴, OBV 분산** *(RULE D6 — grade-C, cited here beside `exc60 −15.47` and flow −0.530, never alone)*.
- ⚠ **`A6` (name the customers, check their disclosed spend) is UNMET.** The customers of the
  advertising node are the rest of the S&P's marketing budgets; **no capex/opex disclosure was opened
  this run**, and with `AMZN`'s FCF at **−$7.6bn** (`brief` 08-23 head, 25 articles / 5 outlets) the
  buyer side is visibly cash-constrained. **Stated as unmeasured, with the date it would be measurable
  (`META`/`GOOGL` next prints) rather than concluded around.**
- 🚨 **The connectivity node contains the book's orphan.** `T` is **9.74% of the REAL account's
  invested capital for a 7th consecutive run**, with **no cycle label, no card, and no report** — and
  `module_report_tags` still cannot index it (`M152`). Its own numbers are the sector's weakest of the
  eight: flow **+0.089**, `vol_surge` **0.47**, exc20 **+1.18**, exc60 **−0.43**.
  ⇒ **The largest single un-owned position in the book sits in this sector, at the node the chain map
  marks as downstream of the binding constraint.** That is this DEEP's most actionable finding and it
  is handed to BET as an **ownership** question, not a trade.

## 4 · Chain-hop candidates — none admissible

`chain-hop` was run on this run's themes; **the COMM proximity candidates it returned (`GOOGL`/`GOOG`
against a *copper backwardation* article, `META` against a *Treasury-buyback/bitcoin* article) are
ticker-collision noise**, and both names are **headline-named** in their own right — the crowded layer
by construction. **Zero body-proximate, non-headline candidates survived.** ⇒ **No name is handed to
BET from this leg** (a news co-mention alone is not a candidate).

## 5 · Track KPIs and anti-signals (observables, dated)

| KPI | Reading now | Kills the thesis if |
|---|---|---|
| `wflow` ex-Alphabet | 🚨 **−0.193** | *(this IS the finding)* — recheck at the next run: if it turns positive **without** a price move, the sweep's weights changed, not the sector |
| Media trio `exc20` (`CMCSA` `DIS` `NFLX`) | **+16.78 / +10.01 / +9.93** | all three ≤ **+3.44** (the sector line) by **2026-09-08** ⇒ the leadership was sector beta |
| Participation | **66.7% (8/12)** | < 50% by 09-08 |
| Max `vol_surge` in sector | **0.83** (`WBD`) | ≥ 1.20 on ≥2 names ⇒ the volume-starvation reading is void and the 🟢 gate becomes informative here |
| `META` | flow −0.530 🔴, exc60 −15.47, OBV 분산 *(RULE D6 — grade-C, paired with the two axes to its left)* | `META` turns OBV 매집 **with rs20 > 0** ⇒ the ex-META cut stops flipping the sign and the sector becomes readable |
| **`T` orphan** | **9.74% of real invested, 7th run, no thesis** | *(not a market KPI)* — **a human must assign it a thesis or a disposition (P5)** |

## 6 · Verdict for BET (analysis only — no sizing, P4)

**COMM stays `N`, and the reason is that the sector's headline instrument is unreadable, not that the
money is neutral.** Any BET sentence about COMM must carry **one of these two lines**:
- *"`wflow` +0.108 becomes **−0.193** ex-both-Alphabet-classes and **+0.194** ex-META as well — three
  names decide the sign in two directions, and the other nine are 10.9% of the sector's cap"*, or
- *"read on `eqflow` +0.095 / participation 66.7%, which are not cap-weighted."*

**Two items escalated out of this file:**
1. 🚨 **`D297` — 5th run unfixed and now demonstrated to produce a false negative.** Positive-form
   remedy: **group `SECTOR_FLOW`'s top-1 test by ISSUER, not by ticker row** (a `share_class_group`
   column keyed on CIK), so the guard tests the 76.6% it should have tested. Scope: `GOOGL`/`GOOG` is
   the only dual-class pair in `us_top300` today — **and that is exactly why it has survived five runs.**
2. 🚨 **`T` — 7th run as an unlabelled 9.74% of real invested capital.** Human call (P5).

---
*Analytical output only. No buy/sell recommendation, no sizing (P4).*
