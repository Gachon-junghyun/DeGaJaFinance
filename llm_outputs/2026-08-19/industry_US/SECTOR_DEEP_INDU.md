# SECTOR_DEEP_INDU — Industrials (OW−) · industry_US · 2026-08-19 · **CONTINUOUS track ⇒ DELTA-led**

> **Structure carried BY REFERENCE from `llm_outputs/2026-08-17/industry_US/SECTOR_DEEP_INDU.md`.**
> Sections 0–6 of that file (mandate-rebuttal-first · the `LHX` delta · the `M704` ex-`LHX` table ·
> the three-object `M708` split · the flow cross-check · the `HII`/`EMCOR` measurement gap · KPIs)
> are not re-printed. **This file writes only what changed and what the mandate asked.**
>
> **Benchmark declared file-wide: `SPY`.** Every relative figure also names its benchmark inline.
> Terminal settled bar **2026-08-18**; **no 08-19 prices exist in any price series here.** Every
> sweep `delta` is a **TWO-session** move (08-14 → 08-18, PREFLIGHT G2).
> `velocity` and the 51 survivors are **REVOKED (G1)**; `breadth` is **not** news-independent.
> `wflow` may **NOT** carry a promote/demote for this sector (**G3 flipper, `CAT` 8.7%**).
> Sector market-cap weights are **35 days stale** (G5) and every cap-share below inherits that.
> Analytical only — **zero buy/sell, zero sizing (P4).**

---

## 0 · ⛔ The mandate's own premise is false on this run's JSON — read this before §1

The mandate as handed down states: ***"Only `RTX` clears the `vol_surge` 1.2 gate."***
**Measured, `SECTOR_FLOW_US.json` `asof` 2026-08-18, all 50 Industrials rows:**

| claim | measured |
|---|---|
| `RTX` `vol_surge` | **0.83** |
| Industrials names with `vol_surge` ≥ 1.2 | **0 of 50** |
| the sector's maximum `vol_surge` | **`AME` 1.16**, then `LHX` 1.14 · `WAB` 1.02 · `NSC` 1.01 |

🚨 **So the whole premise inverts. `RTX` did not clear the volume gate; it is 0.83, and nothing in
this sector cleared it.** The correction matters because the 08-17 file used exactly that gate to
file `NOC` to `missed_ledger` (`D270`, enters-if `vol_surge ≥ 1.2`) — a rule that, applied
consistently, excludes `RTX` too.

**Then where did `RTX`'s 🟢 come from?** From `module_flow/_synthesize.py:flow_tag`, which is a
**4-axis** tag while `flow_score` is a **3-axis** score this run. Re-deriving every green from its own
JSON row:

| green axis | `RTX` |
|---|---|
| `obv_state == 매집` | ✅ |
| `rs20 > 0` (**vs `SPY`**, +13.9) | ✅ |
| `vol_surge ≥ 1.2` | ❌ **0.83** |
| **`velocity ≥ 1.2`** | ✅ **1.55 — and this axis is REVOKED by G1** |

🚨 **`RTX` is green on three axes only if the revoked news axis is counted. Strip it and
`green = 2` ⇒ `🟡중립`.** The same audit disqualifies **5 of the run's 8 greens** (`RTX ORCL MA BAC
WMT` all sit below `vol_surge` 1.2 and are carried by `velocity`); only `KKR` 1.32, `LITE` 1.25 and
`CSCO` 1.43 are green without it.
⇒ **`M25`'s standing rule — "the 🟢 count is a `vol_surge` count, not a flow count" — is wrong on this
run**, and `SWEEP_READ §1` and `MACRO §C` both repeat it. It is a `velocity` count for 5 of 8.
**`RTX` is not admissible as a new-🟢, and Industrials' green count under G1 is `0`, not `1`.**

★ **And the number is not even reproducible within its own run-day.** `module_flow RTX --positioning`,
run three times tonight after the sweep: **velocity 1.04 / 1.04 / 1.04 → `🟡중립`**, against the
sweep's 1.55 at 21:53. `NOC` on the same instrument: **1.25 / 1.25 → `🟢가속`.**
⇒ **On a live re-read the green name inside defense is `NOC`, not `RTX` — an exact inversion.**
Both greens are `velocity`-derived, so under G1 **neither is green**; the useful finding is that the
axis that separates them is *unstable on the same calendar day*, which is what G1 says it is.

---

## 1 · ★★★ THE MANDATE, ANSWERED: **No. Industrials is not a defense sector wearing a machinery label — it is a machinery-and-electricals sector with a defense object bolted on that does not co-move with it.**

Two numbers decide it, and they point in the same direction.

### 1a · Cap share says the sector is not defense

| object | names | share of Industrials cap *(35-day-stale weights, G5)* |
|---|---|---|
| Aerospace & Defense (full GICS group) | 10 | **26.1%** |
| **the five pure primes `RTX LMT NOC GD LHX`** | 5 | **11.3%** |
| Machinery (all 3 GICS machinery codes) | 8 | 20.7% |
| Electrical equipment (incl. Heavy Electrical) | 6 | 15.0% |
| Transport (rail/air-freight/ground/airlines) | 9 | 14.5% |

⇒ **The primes are one-ninth of the label.** No cap-weighted instrument can be "a defense read."

### 1b · Correlation says defense is not in this sector at all — measured this run

**Raw 60-day daily-return correlations, settled closes through 2026-08-18** (raw, not excess — the
excess axis carries the common IT-vs-rest factor PREMORTEM §3c measured, so it would manufacture
coupling):

| pair | raw 60d corr | reading |
|---|---|---|
| **defense EW{`RTX LMT NOC GD LHX`} vs the other 40 Industrials names, EW** | **+0.082** | **≈ 0 — defense does not co-move with its own sector** |
| machinery EW(8) vs `XLI` | **+0.862** | machinery **is** the label |
| electricals EW(6) vs `XLI` | **+0.836** | electricals **is** the label |
| transport EW(9) vs `XLI` | +0.598 | mostly the label |
| **defense EW(5) vs `XLI`** | **+0.268** | **the outlier** |
| **machinery EW(8) vs electricals EW(6)** | **+0.754** | 🚨 **these are ONE object, not two** |
| defense EW(5) vs machinery EW(8) | +0.106 | independent |
| defense EW(5) vs electricals EW(6) | −0.067 | independent |
| defense EW(5) vs `SPY` | **−0.053** | |
| defense EW(5) vs `XLK` | **−0.259** | |

🚨 **This overturns the 08-17 file's own three-object split.** That file measured
*defense / electricals / machinery* as three sub-objects on a **performance spread**. On the **risk
axis** measured today, **machinery and electricals are a single object (+0.754)** and the second
object is defense (+0.08 to the rest of the label). **Three performance legs, two risk objects.**

**Answer to the mandate, stated positively:** *the sector label is a defense object and a cyclical
object filed under one code.* It is not "defense wearing a machinery label" — defense is too small
(11.3% of cap) to be the sector. It is **a cyclical sector carrying an uncorrelated defense annex**,
and the desk's Industrials thesis (`M704`/`M719`/`S97`/EVENT_ALPHA Card 8) is **100% about the annex**.

### 1c · Sub-sector dispersion — and yes, the label is the wrong unit of analysis

`flow_score` EW by sub-object, `asof` 2026-08-18 (`vol_surge`/OBV/RS20/RS60, 3 axes, no `velocity`):

| sub-object | n | cap% | EW flow | EW RS20 **vs `SPY`** | EW RS60 **vs `SPY`** | OBV 매집 | max `vol_surge` |
|---|---|---|---|---|---|---|---|
| Distributors (`URI FAST`) | 2 | 2.3% | **+0.558** | +9.4 | +15.4 | 2/2 | 0.84 |
| HR services (`ADP PAYX`) | 2 | 2.3% | +0.438 | +5.7 | +21.4 | 2/2 | 0.86 |
| **Aerospace & Defense** | 10 | 26.1% | **+0.371** | **+8.1** | **+12.5** | **9/10** | 1.14 |
| Conglomerates (`MMM HON`) | 2 | 4.4% | +0.069 | −0.1 | +4.8 | 1/2 | 0.78 |
| Construction & Engineering | 4 | 5.0% | −0.006 | +1.2 | −7.9 | 1/4 | 0.87 |
| Electrical equipment | 6 | 15.0% | −0.074 | −2.3 | +0.2 | 3/6 | 1.16 |
| **Machinery** | 8 | 20.7% | **−0.182** | −1.1 | +6.5 | 3/8 | 1.02 |
| Building Products | 3 | 4.9% | −0.281 | −3.8 | +0.9 | 1/3 | 0.72 |
| **Transport** | 9 | **14.5%** | **−0.314** | −3.5 | +4.8 | **0/9** | 1.01 |
| Environmental (`RSG WM`) | 2 | 2.9% | −0.403 | −4.1 | +0.1 | 0/2 | 0.88 |

- **A&D − machinery spread = 0.554 flow units. A&D − transport spread = 0.685.**
- The sector's own **two-session move is +0.019** and its `eqflow` is **−0.002**.
- ⇒ **The internal spread is 36× the sector's own two-session move**, and ~340× its `eqflow`.

✅ **Stated as the constraint demands: the sector label is the wrong unit of analysis for Industrials.
Any verdict written at the `INDU` level is an average of objects that are 36× further apart than the
thing being averaged has moved.** `eqflow −0.002` is not "no signal" — it is **two signals cancelling**.

### 1d · ★ The object the 08-17 three-way split omitted: **Transport, 14.5% of cap, 0 of 9 accumulating**

The 08-17 file measured *defense / electricals / machinery* and called machinery the drag. **Measured
today, machinery is not the worst leg — Transport is** (EW flow −0.314 vs machinery −0.182), and it is
the **only sub-object with zero OBV accumulation across every one of its names** (`NSC CSX UNP UPS FDX
ODFL UAL DAL UBER`; RS20 EW −3.5 **vs `SPY`**). Machinery's headline (`CAT` −0.657 🔴 · `CMI` −0.756 🔴)
is loud; Transport's uniformity is quieter and covers **nearly as much cap**. **Named, not worked
around.** ⚠ Its OBV column is grade C on its own (`D6`) and is paired here with RS20 vs `SPY` and the
`flow_score` axis, both A/B-grade.

---

## 2 · ★★★ The defense accumulation pattern is real — and the one name it fails on is the one the desk holds

### 2a · Two-instrument OBV test (`D6`: OBV is grade C and never carries a claim alone)

`module_chart <TK> --read`, full panel citable today (PREFLIGHT G7 retains the bare `<TK> --read`
form and G0 is clean), against the sweep's `obv_state`:

| ticker | sweep `obv_state` | `module_chart` 20d OBV slope | agree? | turn-verdict | RS20 **vs `SPY`** | RS60 **vs `SPY`** |
|---|---|---|---|---|---|---|
| **`RTX`** *(HELD)* | **매집 +0.368** | 🚨 **분배 −25%** | ❌ **CONFLICT** | BREAKOUT · RSI 72.5 · upper band | **+13.9** | **+24.8** |
| `LMT` | 매집 +0.493 | 누적 **+41%** | ✅ | CONFIRMED-TURN · RSI 61.4 | **+17.2** | +12.8 |
| `NOC` | 매집 +0.568 | 누적 **+33%** | ✅ | CONFIRMED-TURN · RSI 75.6 | **+12.4** | +3.5 |
| `GD` | 매집 +0.467 | 누적 **+43%** | ✅ | CONFIRMED-TURN · RSI 66.2 | +4.4 | +12.8 |
| `BA` | 매집 +0.252 | 누적 **+31%** | ✅ | PULLBACK-TO-SUPPORT · RSI 50.0 | +6.4 | −1.8 |
| `AXON` | 매집 +0.323 | 누적 **+88%** | ✅ | CONFIRMED-TURN · RSI 63.8 | **+18.7** | **+55.7** |

🚨 **The mandate's "6 of 6 accumulating" is 5 of 6 on the two-instrument test, and the failure is
`RTX`** — the run's claimed new-🟢, the desk's only held Industrials defense name, and the name the
mandate leads with. ⚠ **RULE D6 held throughout**: OBV is grade C and never carries this alone — every
row above is paired with its **RS20 and RS60 vs `SPY`** columns and its `flow_score`, both A/B-grade,
and `RTX`'s RS20 **+13.9 vs `SPY`** is the reason the conflict is a *caution*, not a reversal.
This is not a new discovery of mine: **PREMORTEM §4b already named `RTX` as one of
the 5 names where the two OBV instruments flip sign**, and then EVENT_ALPHA Card 8 and the ROTATION
mandate cited `RTX`'s 매집 anyway.
⇒ **`RTX` fails BOTH independent audits this run: its 🟢 is `velocity`-derived on a revoked axis (§0),
and its OBV accumulation does not replicate on the second instrument.** ★ **Everything else in the
defense group replicates cleanly on both.** The pattern is real; the desk's leg is the exception.

### 2b · The full group, not the hand-picked six

The mandate's basket (`RTX LMT NOC GD BA AXON`) is a **selection**. The full GICS Aerospace & Defense
group is 10 names, and the unselected read is *stronger evidence* because it was not chosen:

`RTX` +0.572 · `GE` +0.568 · `LMT` +0.528 · `AXON` +0.511 · `NOC` +0.483 · `BA` +0.411 ·
`LHX` +0.332 · `HWM` +0.274 · `GD` +0.256 · `TDG` −0.222
⇒ **9 of 10 OBV-accumulating · 8 of 10 positive RS20 vs `SPY` · 8 of 10 on both.**
The two the six omitted (`GE`, `HWM`) both pass; the two that fail are `LHX` (RS20 −1.9 vs `SPY`) and
`TDG` (OBV 중립).

### 2c · 🚨 "the broadest pattern on the board" — measured board-wide, and it is rank 2

Share of names passing **`OBV 매집 ∧ RS20 > 0` vs `SPY`**, every GICS industry with n ≥ 5, all 299:

| industry | pass | rate |
|---|---|---|
| **Asset Management & Custody Banks** (Financials) | **6/7** | **86%** |
| **Aerospace & Defense** (Industrials) | **8/10** | **80%** |
| Pharmaceuticals (Health Care) | 4/5 | 80% |
| Biotechnology | 4/6 | 67% |
| Health Care Equipment | 5/8 | 62% |
| Electrical Components & Equipment (Industrials) | 3/5 | 60% |

⇒ EVENT_ALPHA Card 8's *"the broadest single pattern in this sweep"* is **not correct as written**.
Defense is **the broadest among groups of n ≥ 10** — a real and worth-stating qualification — but
**PREMORTEM Lens 1 LEG C measured `KKR APO BX BLK SCHW CME ICE` at 7/7 accumulating and 7/7 positive
RS20 vs `SPY` this same run**, which strictly beats 8/10. **Two stages of one run produced the same
finding about two different sectors and only one of them was promoted into a mandate.** Stated, not
resolved here — DEEP does not allocate slots.

---

## 3 · ★★ `M719` re-measured at the 08-18 settle, and `S97`'s tape

Excess **vs `SPY`**, settled closes through **2026-08-18** (reproduces the sweep's `rs20`/`rs60`
columns to 0.1pp, which confirms `SPY` is the sweep benchmark):

| basket | 20d excess vs `SPY` | 60d excess vs `SPY` |
|---|---|---|
| defense EW, all five | +9.20 | +8.37 |
| **defense EW, ex-`LHX`** | **+11.98** | **+13.48** |
| **Δ from removing `LHX`** | **+2.78pp** | **+5.11pp** |
| *(08-17 measurement of the same Δ)* | *+2.04pp* | *+4.32pp* |

★ **`M719` is not just intact — it strengthened by 0.79pp on 60 days over two sessions.** The defense
thesis continues not to depend on its broken leg. Same result in the `M704` form (benchmark **`XLI`**
instead of `SPY`): defense ex-`LHX` **+11.79 / +9.17** on 20d/60d vs `XLI`, Δ from removing `LHX`
identical at **+2.78 / +5.11pp**.

**`S97` (settles 08-21) pre-settle**: `LHX` exc5 **−1.862 vs `SPY`** at the 08-18 close — **mid-band**
between A ≤ −4.0 and B ≥ 0, unchanged from the value handed down. exc3 −1.751. **No branch reachable
from the tape yet.**

### 3a · The 08-17 "the tape was there three days early" claim — its follow-through, measured

08-17 recorded `LHX` **FINRA short-vol z +1.86 🔴 building** at 2026-08-14, three days before the CEO
exit, and correctly flagged it as **one observation, not a lead-time estimate**. Re-measured tonight
(`us_flow.py`, FINRA Reg SHO daily, **2026-08-18**):

| ticker | short% | base20 | **z** | 5v5 trend |
|---|---|---|---|---|
| **`LHX`** | 36.5% | 41.7% | **−0.54** | **−4.5 ▼** |
| `RTX` | 42.7% | 39.9% | +0.30 | −15.8 ▼ |
| `GD` | 48.0% | 38.8% | **+1.32** | +6.1 ▲ |
| `CAT` | 55.4% | 44.7% | **+1.37** | −4.3 ▼ |
| `LMT` −0.07 · `NOC` −0.10 · `BA` −0.18 · `AXON` −0.58 · `ETN` −1.08 · `CMI` +0.70 | | | | |

⇒ **`LHX`'s short-vol z went `+1.86` → `−0.54` in two settled sessions and the 5v5 trend is falling.**
The pressure was **event-specific and has unwound**; it is not a standing bear position into `S97`'s
settle. ⚠ **D6-class caveat carried**: FINRA short-**volume** includes market-maker hedging and is
context, never a trigger — and this is now **two observations, still not a lead-time estimate.**

---

## 4 · 🚨 `S99` / PREMORTEM Lens 2 — **`ETN` is NOT in the wrong sector, and the bracket has a missing branch**

The mandate requires engagement with `ETN`–`ANET` raw 60d **+0.722** vs `ETN`–`RTX` **−0.040**.
**I reproduced both exactly** (settled to 2026-08-18): `ETN`–`ANET` **+0.722** · `AVGO`–`ANET`
**+0.596** · `NVDA`–`AVGO` **+0.495** · `ETN`–`RTX` **−0.040**. The measurement is right.
**The inference drawn from it — *"`ETN` trades as AI-compute"* — is not, and the control that breaks
it was never run.**

### 4a · The controls Lens 2 did not run

| `ETN` raw 60d vs | corr |
|---|---|
| **`VRT`** (electrical/thermal) | **+0.815** |
| **`CMI`** (machinery) | **+0.811** |
| **`CAT`** (machinery) | **+0.807** |
| **`XLI`** | **+0.764** |
| `AME` | +0.735 | 
| `GEV` | +0.732 |
| **`XLK`** | **+0.731** |
| **`ANET`** | **+0.722** ← the figure Lens 2 built on |
| **EW{`CAT DE CMI PCAR GWW ITW PH WAB`} (machinery)** | **+0.717** |
| **EW{`ANET AVGO NVDA`} (AI-compute)** | **+0.722** |
| `SPY` | +0.648 |
| `EMR` | +0.628 |
| **`RTX` −0.040 · `LMT` −0.035 · `GD` −0.034 · `NOC` −0.122** | |

🚨 **`ETN`–machinery `+0.717` and `ETN`–AI-compute `+0.722` differ by 0.005.** At n = 60 the standard
error of a correlation near 0.72 is ≈ 0.066 — **the two are 0.08 SE apart and statistically
indistinguishable.** `ETN`–`CMI` and `ETN`–`CAT` are both **higher** than `ETN`–`ANET`.

### 4b · The joint regression settles the sector question

Daily returns, 60 sessions to 2026-08-18, `ETN ~ XLK + XLI`:

| | coefficient | t |
|---|---|---|
| `XLK` | **0.62** | 5.12 |
| **`XLI`** | **1.40** | **6.00** |
| R² | 0.715 | |

*(univariate: β to `XLK` 1.03, R² 0.535 · β to `XLI` **2.07**, R² **0.584**)*

⇒ **Controlling for both, `ETN` loads roughly 2.3× more on Industrials than on Tech.**
**`ETN` is in the right sector.** What it is *not* is a diversifier: it is a **high-beta cyclical that
correlates with everything cyclical**, AI-compute included. Its `ANET` correlation is a cyclical-beta
correlation, not an AI-compute identity.

For contrast, the same regression on **`RTX`**: `XLK` **−0.51** (t −4.96) · `XLI` **+1.06** (t 5.40),
R² only **0.377**. **`RTX` carries a *negative* tech beta.**
⇒ **The book's genuine diversifier inside Industrials is `RTX`, not `ETN` — the exact opposite of the
role the two names occupy in the desk's own framing.**

### 4c · What this does to `S99` (settles 08-21) — **construction note, thresholds NOT re-set**

`S99` asks A = *`ETN` is a 5th AI-compute unit* vs B = *`ETN` is a genuine electrical leg*.
**Neither branch contains the measured answer**, which is *`ETN` is a machinery-correlated cyclical
whose AI-compute and machinery correlations are indistinguishable*. Because `ETN`–AI and
`ETN`–machinery are the same number, **a same-sign co-move with EW{`ANET AVGO HPE`} fires branch A
without excluding the machinery explanation.** `S99` **cannot separate its own hypotheses.**

⚠ **And its `E` leg is further inside the implied move than PREMORTEM stated.** Lens 2 compared the
1.5pp `E` threshold to *"`RTX`-class ±1.9% D2."* **`ETN`'s own straddle reads ±8.3% (expiry
2026-08-21, D2)** on `module_flow ETN --positioning` — so the 1.5pp band sits inside **±8.3%**, not
±1.9%. The **LOW-RESOLUTION declaration Lens 2 already made is correct and understated by ~4×.**
⚠ ±8.3% at D2 with no scheduled `ETN` print is itself suspect (thin-strike artifact); flagged, not
relied on. **Pre-settle state re-measured, 08-14 → 08-18 close (3 of 5 sessions): M = −5.687pp,
E = −3.512pp, same sign, |M| ≥ 3.0 already cleared ⇒ tracking A.** Reported as inherited state.
**Thresholds are frozen. This section changes nothing about `S99`; it records that branch A, if it
fires, will not mean what the row says it means.**

---

## 5 · The customers, and their disclosed spend — with print dates

**The node's customer is the U.S. Government.** Disclosed concentration, from each issuer's own 10-K
(`module_business_us`), all periods ending **2025-12-31** except `LHX` (fiscal year ended 2026-01-02):

| name | filed | U.S. Gov. as % of sales | trend | total backlog |
|---|---|---|---|---|
| **`RTX`** *(HELD)* | 2026-02-06 | **38%** ($33,279m) | **46% (2023) → 40% (2024) → 38%** — falling | **$268bn**, vs $218bn 2024 (**+23%**) |
| `LMT` | 2026-01-29 | **72%**, of which **63% DoW** | — | **$193bn**; ~37% to revenue in 12m, ~60% in 24m |
| `GD` | 2026-01-30 | **68%** ($35,757m; DoW $29,788m) | 72% → 69% → 68% — falling | 14 Virginia-class subs to 2034 · 11 ships to 2032 |
| `NOC` | 2026-01-27 | — | — | **$95bn**, stated as *"equivalent to remaining performance obligations"* |
| `LHX` | 2026-02-12 | — | — | **$38bn**; ~45% to revenue by FY2026, ~70% by FY2027 |

★ **`RTX` is the least government-exposed name in its own basket — 38% and falling for three straight
years.** Nearly two-thirds of `RTX` is commercial aerospace aftermarket (Collins / Pratt & Whitney).
⇒ **A "defense" thesis expressed through `RTX` is ~38% a defense thesis.** That is consistent with
§4b's finding that `RTX` is the group's cleanest diversifier, and it is the same fact seen twice.

**The customer's disclosed spend, with dates** (`LMT` 10-K §Government Budget Environment — the only
one of the five that restates the budget line):
- FY2026 budget request published **June 2025**: **$848.3bn** base discretionary + **$113.3bn**
  reconciliation (mandatory).
- **One Big Beautiful Bill Act signed 2025-07-04**: >**$150bn** mandatory for DoW, available until
  **2029-09-30**.
- **NDAA FY2026 signed into law 2025-12-18**: authorises **$901bn** for Defense, **+$8bn** over request.
- CR signed **2025-11-12** funding DoW through **2026-01-30**.
- Final Appropriations package unveiled **2026-01-20**: Defense Appropriations conference report
  **$839.2bn**, **+$8.4bn** over the President's topline.

🚨 **The freshest disclosed customer-spend figure available to this desk carries a print date of
2026-01-20, restated in a filing dated 2026-01-29 — 203 days before this run.** There is **no FY2027
appropriations event, no new DoD budget line and no dated contract award** in the last 7 days:
`fts search "defense budget" --days 10` returned 36 items and **not one is an appropriations or
award print** (`RTX` `module_disclosure_us --days 120`: **27 filings, 0 in the 수주/계약/M&A
category**). The two dated tape items in the window are **2026-08-14 "Trump orders tariffs on
foreign-made [drone] components"** and **2026-08-14 "Trump orders Navy to return to older system of
launching jets off aircraft carriers"** — the second is a programmatic reversal whose most exposed
listed name is **`HII`, which remains outside `us_top300` and unmeasurable on this desk (`D274`,
carried unchanged from 08-17)**.
⇒ **The accumulation in §2 is happening against a customer whose spending the desk last measured
203 days ago.** That is the honest state, and it is the one thing about this thesis that has not
changed in any of the four consecutive DEEP slots.
⚠ `module_news_data chain-hop` scanned **0 articles** on both attempts tonight (G1 transport); `fts
search` returned 25/204 counts on the same bridge. **The chain-hop leg of this section is unrun, not
empty.**

---

## 6 · ✅ Frame-transfer test (mandatory) — three frames this desk trusts elsewhere, against defense backlog

| frame the desk trusts elsewhere | does it transfer to defense backlog? |
|---|---|
| **Take-or-pay** (the desk's Energy/midstream frame — you are paid whether or not volume is lifted) | 🚫 **NO — and the 10-K says so in terms.** `LMT` risk factors: *"The U.S. Government … may terminate any of our government contracts and subcontracts either at their convenience or for default … If a contract is terminated for convenience, we generally are protected by provisions covering reimbursement for costs incurred on the contract, up to termination, and profit on those costs."* **Termination-for-convenience pays costs-to-date plus profit on those costs — not the remaining contract value.** Take-or-pay pays the unlifted volume; T4C explicitly does not. **The frame does not transfer, and this is the decisive disanalogy.** |
| **RPO lock-in** (the desk's software frame — contracted revenue not yet recognised) | ⚠ **PARTIALLY, and unevenly across the five names.** `NOC` states its backlog **"is equivalent to the company's remaining performance obligations"** and **excludes** unexercised options and IDIQ task orders — that **is** the ASC 606 RPO object, conservatively drawn. `LMT`'s backlog explicitly **includes unfunded amounts** — *"firm orders for which funding has not been appropriated"* — which is **weaker than RPO**: appropriation risk sits inside the number. ⇒ **`NOC`'s $95bn and `LMT`'s $193bn are not the same kind of object and may not be summed or compared.** |
| **Regulated return** (the desk's utility frame — a fee set on an allowed cost base) | ⚠ **PARTIALLY.** Cost-type contracts are functionally a fee on allowable cost. `NOC`: *"cost-type contracts have less financial risk associated with unanticipated cost growth but generally provide lower profit margins than fixed-price contracts."* ⇒ the frame transfers to the **cost-type** portion only, and it transfers the **cap on upside** along with the floor on downside. **Neither issuer discloses a clean cost-type/fixed-price revenue split in the extracted text**, so the mix that would size this is **not measurable here.** |

✅ **"Checked, does not apply" is recorded for take-or-pay** — the strongest of the three frames and
the one the desk uses most confidently elsewhere. **Defense backlog is not contracted cash.**

---

## 7 · Valuation — no cheapness claim is made on `RTX`, and here is the arithmetic that forbids it

Forward multiples on **+1y consensus EPS**, `data/estimates/eps_2026-08-19.json` (snapshot **2026-08-19**;
G6 FAIL — 11 files / 29 days, 0.38/day, **no `kelly_size --ic` size may be derived from this**):

| ticker | +1y EPS now | vs 90d ago | up/down revisions, 30d | close (08-18) | forward P/E |
|---|---|---|---|---|---|
| **`RTX`** | 7.853 | **+4.02%** | **22 up / 0 down** | 225.49 | **28.7×** |
| `LMT` | 32.688 | +1.79% | 18 up / 0 down | 607.17 | **18.6×** |
| `ETN` | 16.022 | +1.90% | 15 up / 2 down | 431.33 | 26.9× |
| **`CAT`** | 32.160 | **+7.69%** | **20 up / 2 down** | 840.87 | 26.1× |
| `GE` | 9.717 | +5.65% | 9 up / 0 down | 375.09 | 38.6× |
| `DE` | 22.622 | −1.72% | 2 up / 4 down | 588.72 | 26.0× |
| `BA` | 4.121 | −2.68% | 5 up / 11 down | 223.06 | 54.1× |
| `NOC` `GD` `LHX` `AXON` `EMR` **NOT COVERED** — the 120-name snapshot does not carry them | | | | | |
| ⚠ `HON` shows −56.29% over 90d (22.966 → 10.038) — a **share-count/definition artifact**, not a revision. Excluded. | | | | | |

**`RTX` at 28.7× forward is the most expensive of the covered defense names — 54% above `LMT`'s
18.6×. No "cheap on forward multiple" claim is made anywhere in this file for `RTX`.**

**If anyone wants to call `LMT`'s 18.6× cheap, the constraint's two required disclosures are:**
- **Margin percentile in its own history**: `scripts/margin_history.py LMT` — FY2025 gross margin
  **10.2%** against a 19-year range **8.1% (FY2011) – 14.0% (FY2019)**, median 11.1%. **10.2% is the
  8th-lowest of 19 observations ⇒ ~37th percentile of its own history — a depressed margin base, not
  a peak one.** ⚠ **`RTX` and `NOC` cannot be given this disclosure at all**: the XBRL series ends at
  **FY2017** for both (tag change), so **their margin percentile is unmeasurable on this instrument**
  and no cheapness claim about them is admissible. ⚠ Cross-name gross-margin comparison is invalid
  here regardless (`LMT` 8–14% vs `RTX` 44–47% vs `NOC` 52–58% is a definition difference, not
  economics) — **only the within-name percentile is usable.**
- **Estimate-revision trend**: `LMT` +1.79% over 90 days, **18 up / 0 down** in 30 days.

### 7a · 🚨 The revision table describes the denominator — demonstrated inside this sector

**`CAT` carries the strongest 90-day revision in the entire Industrials set: +7.69%, 20 up / 2 down —
and `CAT` is the sector's worst tape** (`flow_score` **−0.657 🔴분산**, OBV 분산 −0.086, **RS20 −8.1
vs `SPY`**, the G3 flipper at 8.7% weight). **The name with the best revisions is the name with the
worst money.** ⇒ **The revision column is a DESCRIPTION of where the denominator is going, never a
leading indicator** — consistent with the desk's own measurement that the effect is an IT loading
(**ex-IT Q5−Q1 = −1.1pp**). It is reported here as a denominator description and **carries nothing.**

---

## 8 · Cycle registry, rank-3 — the floor is unarmed **by declaration**, and the entry's own reason is now falsified

PREMORTEM Lens 4 flags `min_epicenter_pct: 0.0` on the rank-3 defense cycle as *"a disarmed guard,
for a second consecutive audit."* **Reading `data/cycles/cycle_registry.json` (`updated 2026-07-17`,
33 days stale) directly, the entry says so on purpose**: *"`min_epicenter_pct` stays 0.0 deliberately
= no floor asserted (and the GAP rule only checks rank≤2 anyway) — this records the epicenter name,
it does not arm a guard."* ⇒ **It is a declared-unarmed slot, not an accidental one.** The correction
does not weaken Lens 4's hand-off to P5 (arming it is still a human decision) — it changes what the
hand-off is *for*.

★ **The stronger finding is that the entry's stated justification is now measurably false.** Its
`core_pick_why` reads: *"`RTX` … the one leg of this cycle that fired … re-confirmed 07-17 (`RTX`
flow 0.317 neutral vs `LMT` −0.742 / `NOC` −0.683, **both distributing**; `LMT` vol 0.58× = **no
interest**)."*

| name | registry, 2026-07-15/17 | **measured 2026-08-18** |
|---|---|---|
| `RTX` | flow +0.317, the leg that fired | +0.572, **OBV conflicted between instruments (§2a)** |
| `LMT` | **−0.742, distributing** | **+0.528, OBV 매집 +0.493 · `module_chart` +41% · RS20 +17.2 vs `SPY`** |
| `NOC` | **−0.683, distributing** | **+0.483, OBV 매집 +0.568 — the sector's highest · RS20 +12.4 vs `SPY`** |

🚨 **The bifurcation the registry locked in 33 days ago has inverted.** `LMT` and `NOC` are no longer
distributing; both now out-rank `RTX` on OBV, and both replicate on the second instrument where
`RTX` does not. **This is the single most consequential delta in this file for anything downstream of
the registry**, and it is a *registry-maintenance* fact (P5, human), not a position call. Stated, not
acted on.

---

## 9 · Prior-run KPIs — pre-settle readings at the 08-18 close

The 08-17 file registered four KPIs and two anti-signals. Carried forward and re-measured:

| # | KPI (08-17) | threshold | **measured 2026-08-18** | status |
|---|---|---|---|---|
| 1 | `LHX` 5-session excess **vs `SPY`** | ≤ −4.0 discontinuity · ≥ 0 orderly | **−1.862** | **mid-band, `S97` settles 08-21** |
| 2 | defense EW **ex-`LHX`** 20d excess **vs `SPY`** | ≥ +5.0pp ⇒ `M704` holds | **+11.98pp** | ✅ **HOLDS, 2.4× the threshold** |
| 3 | electricals EW − machinery EW, 60d **vs `SPY`** *(08-17 definitions: `EMR`+`ETN` vs `CAT`+`DE`)* | ≥ +10pp ⇒ genuinely two objects | **+11.06pp** *(was 18.80pp)* | ⚠ **HOLDS, but narrowed 7.74pp in two sessions** |
| 4 | `NOC` `vol_surge` | ≥ 1.2 with OBV still accumulating | **0.67** (OBV 매집 +0.568 ✅, paired per RULE D6 with **RS20 +12.4 / RS60 +3.5 vs `SPY`** and `flow_score` +0.483 — OBV never stands alone) | ❌ **still far; re-check 08-25 stands** |
| 🚨 | **Anti-signal 1** — a DoD award/budget headline naming `LHX` in-window ⇒ `S97` VOID | | **not fired** (§5: no award or appropriations print in 10 days) | `S97` remains scoreable |
| 🚨 | **Anti-signal 2** — a `CAT`/`DE` guidance event in-window ⇒ do not re-measure the spread | | **not fired** (`RTX` disclosure sweep found 0 계약/실적 filings; no `CAT`/`DE` guidance print surfaced) | KPI 3 re-measure admissible |

★ **KPI 3's narrowing is a delta the 08-17 file could not have seen and it cuts against that file's
headline.** On the 08-17 definitions the spread is still >10pp, **but the leadership crossed over**:
defense ex-`LHX` 60d excess vs `SPY` is now **+13.48** against electricals-2 (`EMR`+`ETN`) at
**+11.68**. On 08-14, electricals-2 led at +17.35 vs defense's +10.47. ⇒ **The 08-17 file's warning —
*"the desk owns the second-best leg of a three-legged label"* — has expired on its own measurement.
Defense is now the leading leg.** And §1b says the "three legs" were two objects all along.
⚠ On the **full** 6-name electricals group the picture is far worse (EW flow −0.074, RS60 **+0.18 vs
`SPY`**, 3/6 accumulating) — `ROK` −0.463, `VRT` −0.615, `GEV` −0.683 were never in the 08-17 proxy.

---

## 10 · Lead/lag ledger — every claim in this file, sourced

| claim | status |
|---|---|
| `LHX` short-z +1.86 (08-14) preceded the 08-17 CEO exit | **carried from 08-17 · one observation · follow-through measured this run (§3a): z now −0.54** |
| defense OBV accumulation "leads" price | **NOT CLAIMED.** `D6`: OBV is grade C, r ≈ 0.49 to real flow, t = 1.00 on lead. Every OBV figure here is paired with RS20/RS60 vs `SPY` and `flow_score` |
| the revision table leads the tape | **REFUTED this run (§7a): `CAT` best revisions, worst tape.** Reported as denominator description only |
| `ETN`–`ANET` +0.722 ⇒ `ETN` is AI-compute | **REFUTED this run (§4): `ETN`–`CMI` +0.811, `ETN`–machinery +0.717, joint β to `XLI` 1.40 > `XLK` 0.62** |
| `RTX` new-🟢 = volume-confirmed acceleration | **REFUTED this run (§0): `vol_surge` 0.83, green is `velocity`-derived on a revoked axis, unreproducible same-day** |
| defense = "broadest pattern on the board" | **QUALIFIED this run (§2c): rank 2 of industries n ≥ 5; broadest among n ≥ 10** |
| Transport is the sector's weakest object | **[measured this run]** EW flow −0.314, 0/9 accumulating, 14.5% of cap |
| `HII` exposure to the 08-14 Navy/EMALS reversal | **[unverified]** — `HII` outside `us_top300`, unmeasurable (`D274`) |
| DoD FY2027 spending direction | **[unverified]** — no print since 2026-01-20; the 203-day gap is the finding |

---

## ✅ Verdict for BET

**OW− held. No axis on this desk can promote or demote it, and this run that is a stronger statement
than usual because two of the three axes that *looked* like signals turned out not to be.**

1. **`wflow` −0.028 is INADMISSIBLE** (G3 flipper; `wflow_ex_top1` **+0.032** flips the sign on `CAT`
   at **8.7%**). **`eqflow` −0.002 ≈ 0** and, per §1c, is **two objects cancelling**, not an absence
   of signal. **`breadth` 0.02 is news-contaminated (G1) and unusable.**
2. **The `RTX` evidence the mandate was built on does not survive: `vol_surge` 0.83 (0 of 50
   Industrials names clear 1.2), a `velocity`-derived 🟢 on a REVOKED axis that does not reproduce
   same-day, and an OBV reading that flips sign on the second instrument.** Industrials' admissible
   green count this run is **0**.
3. **The defense accumulation itself is real and it is not `RTX`'s**: `LMT` `NOC` `GD` `BA` `AXON` all
   replicate on both OBV instruments, 9/10 of the full A&D group accumulate, 8/10 are positive on RS20
   **vs `SPY`**, and `M719` **strengthened to +5.11pp on 60 days** (from +4.32pp).
4. **Mandate answer: NO.** Defense primes are **11.3% of the sector's cap** and correlate **+0.082**
   with the other 40 names in the label, while machinery (+0.862) and electricals (+0.836) **are** the
   label and are **one object with each other (+0.754)**. **The sector label is the wrong unit of
   analysis** — its internal spread is **36×** its own two-session move.
5. **`ETN` is in the right sector; `RTX` is the diversifier.** `ETN` loads 2.3× more on `XLI` than on
   `XLK`; `RTX` carries a **negative** tech beta (−0.51, t −4.96). **`S99`'s two branches do not
   contain the measured answer** — recorded as a construction note, thresholds untouched.
6. **The customer has not been measured in 203 days.** ⚠ **That, and not the flow, is the open
   exposure in this thesis** — and it is unchanged across all four consecutive DEEP slots.

⚠ **Direction held; the *reason* has moved from `RTX` to the group.** BET owns sizing; this file
states neither size nor direction on any name.

---

## ✅ EXIT CHECK
- [x] **Delta-led**; 08-17 structure carried **by reference**, not re-printed.
- [x] Mandate answered **explicitly** (§1, restated in Verdict ④), with the cap-share and the
      correlation that decide it.
- [x] **`wflow` used for NO promote/demote** — declared inadmissible in the header, §1c and Verdict ①.
- [x] **Sub-sector dispersion stated**, and the conclusion drawn: **label = wrong unit** (36× ratio).
- [x] **`ETN` risk-sector question engaged and answered against the premortem's inference**, with the
      control it omitted and a joint regression.
- [x] Benchmark (**`SPY`**, plus **`XLI`** where the `M704` form requires it) named inline on every
      relative figure; declared file-wide in the header.
- [x] Sweep `velocity` + 51 survivors treated as REVOKED — **and §0 shows the mandate's own headline
      depended on them.** `breadth` never used as a statistic.
- [x] Terminal bar **2026-08-18** stated; **no 08-19 price appears**; every Δ labelled two-session.
- [x] Sector weights flagged **35 days stale** at first use.
- [x] Every valuation figure carries **margin percentile in the name's own history + revision trend**,
      or states that the instrument cannot supply it (`RTX`/`NOC` margin series ends FY2017).
      **No cheapness claim on `RTX`.** Revision table framed as denominator description and
      **demonstrated non-leading in-sector** (`CAT`).
- [x] **Frame-transfer test run on three frames**; take-or-pay recorded as **"checked, does not
      apply"** with the termination-for-convenience clause that decides it.
- [x] **Customers named (U.S. Government) and their disclosed spend checked with print dates** —
      and the **203-day staleness** reported as the finding.
- [x] Every lead/lag claim **measured this run or tagged `[unverified]`** (§10).
- [x] **`python -X utf8 scripts/report_lint.py` run (rules C1,C2,S6,D6): first pass returned 2 × `D6`
      (§2a prose, §9 KPI-4 cell). Both FIXED in place by pairing the OBV claim with its A/B-grade
      axes (RS20/RS60 vs `SPY` + `flow_score`), not by carrying an exemption. Re-run: ✅ 0 findings.**
- [x] **Zero buy/sell, zero sizing (P4).**
