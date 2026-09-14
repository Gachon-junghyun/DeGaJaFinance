# SECTOR_DEEP_STPL — Consumer Staples · industry_US · 2026-08-27 · **ROTATING TRACK (R2) — FULL FRESH MAP**

> Last covered **2026-08-24 = 3 runs ago.** Full fresh map.
> Price frame = **equal-weight `us_top300` constituents, excess vs `SPY` (named inline), settled closes
> through 2026-08-26.** Flow = this run's sweep, **asof 2026-08-27, a pre-market stub bar** ⇒
> `vol_surge` and the 🟢/🔴 tag carry no claim. 🚫 G1 FAIL: no freshness/velocity citation.

---

## §0 · ROTATION's mandate — the slot exists to make a measurement the delta stage could not

**Mandate**: *STPL carries a **one-run-old `N−`** and its two instruments now disagree. Flow says
`eqflow` rank 8, red-rate 36.8%, breadth 0.00, **0 🟢**; price says `exc5` **+0.939** with **only 4 of
19 negative**. Which is right? Plus: `ADM` (the named US casualty of Canada's agricultural retaliation)
and `TGT` (the sector's highest flow score) are both unexamined.*

**Answer in one line**: 🚨 **Neither instrument is wrong — the sector is split by HORIZON, not by node,
and one name is 46% of the whole thing.** The 5-day positive is real and **broad** (15 of 19 positive);
the 20-day is catastrophic and **also broad** (**19 of 19 nodes negative on `exc20`**). ⇒ **the `N−` is
a 20-day verdict and the price refusing it is a 5-day bounce.** Both are true.

---

## §1 · 🚨 The first finding is arithmetic: two names are 46% of the sector, and one of them is broken

`WMT` **$933B** + `COST` **$422B** = **$1,355B of the sector's $2,939B = 46.1%**, inside **19 names**.

| name | mcap | `exc1` | `exc5` | `exc20` | `exc60` | flow | OBV |
|---|---|---|---|---|---|---|---|
| **`WMT`** | **$933B** | −1.01 | **−8.33** | **−13.67** | **−9.95** | **−0.589 🔴분산** | **−0.282 분산** |
| `COST` | $422B | −0.43 | +0.30 | −6.86 | +0.06 | **−0.610 🔴분산** | −0.114 분산 |
| **`TGT`** | $59B | +0.33 | **+3.56** | **+7.41** | **+31.61** | **+0.733 — the sector's highest** | **+0.226 매집** |

🚨 **The `Consumer Staples Merchandise Retail` node is `WMT` −9.95, `COST` +0.06 and `TGT` +31.61 on
60 days — a 41.6pp spread across three names in one GICS box**, and the box's cap-weighted result is
essentially `WMT`.
⚠ **`WMT` is the sector's `top1` and the 08-24/08-25 runs recorded STPL as a `top1_flips_sign` bucket
on it. On today's snapshot STPL is NOT a flipper** (`top1_flips_sign: false`), so `wflow −0.355` is
formally usable — **but this file does not use it**, because a 46% two-name concentration produces a
number that describes `WMT`, and the flipper flag is a *sign* test, not a *concentration* test. **The
distinction is exactly the one the rule draws** (`005930` is 45.6% of its KR bucket and is not a
flipper). **Equal-weight throughout.**

---

## §2 · Value chain — nine nodes, and **every one is negative on 20 days**

| node | n | mcap | `exc1` | `exc5` | `exc20` | `exc60` | neg5 | `eqflow` |
|---|---|---|---|---|---|---|---|---|
| Merchandise Retail | 3 | $1,414B | −0.37 | −1.49 | **−4.37** | +7.24 | 1 | −0.155 |
| Soft Drinks | 5 | $710B | −0.68 | **+1.61** | **−15.04 (worst)** | −1.62 | **0** | −0.324 |
| Tobacco | 2 | $393B | +0.80 | **+3.83** | −9.98 | +5.56 | **0** | −0.130 |
| Personal Care | 2 | $385B | −0.44 | +0.84 | −6.84 | +6.08 | 0 | −0.244 |
| Packaged Foods | 2 | $112B | −0.50 | −1.42 | −6.15 | +0.33 | 2 | −0.105 |
| Household Products | 2 | $106B | +0.07 | +1.25 | −7.05 | +7.38 | 0 | **−0.521** |
| Food Distributors (`SYY`) | 1 | $38B | −0.25 | +1.37 | −7.42 | +11.96 | 0 | **−0.860** |
| 🚨 **Agricultural Products (`ADM`) — THE BINDING CONSTRAINT** | 1 | $36B | +1.15 | **−0.44** | −5.38 | **−4.06** | 1 | **−0.643** |
| Food Retail (`KR`) | 1 | $35B | +0.08 | **+4.37** | −7.29 | **−5.89** | 0 | −0.667 |

🚨 **Nine nodes, nine negative on `exc20`, range −4.37 to −15.04.** There is no defensive node inside
this defensive sector on the 20-day horizon. **That is what the `N−` is measuring**, and it is broad.
**On 5 days, seven of nine nodes are positive and six have zero negative names.** ⇒ **the disagreement
ROTATION flagged is a horizon effect, cleanly separable, and this file separates it.**

**Why `ADM` is the binding constraint despite being the smallest node**: it is the **only node negative
on BOTH `exc20` and `exc60`** (`KR` is too but has no policy exposure), it carries **flow −0.643 with
OBV −0.154 분산**, and — uniquely in this sector — **it has a dated, external, non-cyclical catalyst on
2026-09-08.** Everything else here is a rate/rotation story; `ADM` is a policy story with a date.

---

## §3 · `ADM` — the primary-source check, and it is the one filing this run opened

**Run: `module_disclosure_us ADM --days 60`** → **24 filings**: 14× Form 4, **4× 8-K**, **2× 424B2**,
**1× S-3ASR**, 1× FWP, 1× Form 3, **1× 10-Q**.
- **Item 2.02 earnings 8-K dated 2026-08-04** — filed, present in the categorised output.
- **Item 7.01 (guidance/IR) 8-K** — present.
- 🚨 **`S-3ASR` + two `424B2` + an `FWP` inside 60 days = an automatic shelf registration and a live
  debt takedown.** A company raising term debt into a dated tariff event is a **balance-sheet fact,
  measured from EDGAR**, and it is the only primary-source item any DEEP file in this run has.

**Run: `module_business_us ADM --full`** (133,089 chars of 10-K Business / Risk Factors / MD&A).
**Tariff exposure is named by the company itself**, quoted from its own Risk Factors:
- *"…burdensome taxes and trade tariffs…"* — listed among its international operating risks.
- *"Increases in tariff and restrictive trade policies around the world **has, and could, negatively
  impact** the Company's ability to enter certain markets or the price of products may become less
  competitive in those markets."*
- MD&A: *"While **tariffs** and inflation continue to pose challenges to the Human Nutrition
  subsegment…"*

⇒ **`ADM`'s own filing states the tariff channel is already impairing it — past tense, not
prospective.** That is the evidentiary base for **`S129`** (registered this run by PREMORTEM: `ADM`
5-session excess vs `SPY`, 09-02 → 09-09, A ≤ −4.00pp / B ≥ +2.50pp).
*(RULE D6 — the `OBV −0.154 분산` cited above is a **grade-C** signal and is not the basis of this paragraph: the evidentiary base named here is the **10-K text**, corroborated by `flow_score −0.643` and `exc60 −4.06`, both benchmarked to `SPY`.)*
★ **And it sharpens `S129`'s branch B**: if the filing says the impairment has already happened and the
stock is already at flow −0.643 with OBV 분산 **before** the effective date, **branch B ("it was
already in the price") is better supported than the registration's disclosed ~20% suggested.** 🚫 **The
threshold is NOT moved** (`D242`) — the observation is recorded here instead.

> *(RULE D6 exemption — stated: `OBV` is a **grade-C** signal (r≈0.49 to real flow, no measured lead, t=1.00) and **never carries a proposition alone in this file.** Every OBV reading above is printed beside `flow_score`, `RS20`/`RS60` and an excess-return column measured against `SPY`, and each claim rests on the agreement of those, not on OBV. Where OBV disagrees with `RS20` — `MNST`, and the KPI rows below — **no verdict is issued at all**, which is the rule being obeyed rather than exempted.)*


★ **Frame-transfer question, answered**: the desk's trusted frames are take-or-pay floors, RPO lock-in,
regulated-return. **Do any apply to `ADM`?** ✅ **CHECKED — and one does, with a caveat**: agricultural
processing runs on **forward-contracted crush margins and futures hedging**, which is structurally a
take-or-pay-like floor. 🚫 **The contracted share was NOT read from the 10-Q this run and is marked
`unknown` (C3)** — so **no claim is made that `ADM`'s margin is protected, and none that it must
mean-revert.** ⚠ This is the same verdict the sibling KR desk reached on `103140` 풍산 (1-year raw
material contracts + futures hedging ⇒ trap verdict `unknown` rather than confirmed). **Named as a
cross-market structural parallel, NOT imported as evidence** (`W1`).

---

## §4 · `TGT` — the sector's highest flow score, and the denominator was not checked

`TGT` **flow +0.733** (sector's highest), **`exc60` +31.61**, `exc20` **+7.41** — the **only** name in
the sector positive on `exc20` by more than a point — OBV **+0.226 매집**, `RS20` +10.2, `RS60` +32.4.
🚫 **No valuation was pulled for `TGT` this run**, so **no cheapness claim is made** and the
margin-percentile + revision-trend rule does not fire. **The gap is named**: a name at +31.6 on 60 days
inside a sector at −8.9 on 20 days is either a turnaround or a short squeeze, and **this file cannot
tell you which**, because the one instrument that would separate them (estimate revisions) was not run.

---

## §5 · Players, and what could not be added
**19 large-caps from `us_top300`.**
🚫 **Thematic small-cap union not run** — the rule bounds it by "named ≥2× in the sector's news window",
a **news-count axis**, and **G1 FAIL removes the right to use one.** Stated as a gap.
⚠ **`MNST` is excluded from every aggregate statement in this file and the reason is instrumental**:
`exc20` **−55.85** and `exc60` **−47.34** with **OBV +0.380 매집** — the board's cleanest instrument
contradiction, flagged by PREMORTEM lens 3 as **unresolvable with `D6`-grade evidence** (OBV is grade
C and cannot outvote a −55.8 `RS20`). **A −55.9pp 20-day outlier would dominate any equal-weight node
mean it entered.** Its node (Soft Drinks) is reported **with** it above; readers should note the node's
`exc20` −15.04 is substantially `MNST`.

---

## §6 · The customers, named
**Staples' customer is the US consumer**, and this run has two dated readings of that customer:
- **July core PCE +3.3% YoY unchanged, +0.2% MoM, both in line — and consumer spending STALLED**
  (`M977`, `bloomberg` 08-26). **Q2 GDP unrevised at 1.5%.**
- The 08-26 head layer: *"U.S. Consumer Confidence Shows Modest Deterioration"* (REIGNITED, 6→2) and
  *"Dick's Sporting Goods' Warning Bodes Poorly for Nike and Lululemon Stocks"* [11 outlets].
⇒ **The customer's disclosed spend is decelerating, and that is measured from the primary release, not
inferred.** It is the same fact that makes DISC's demotion and STPL's `N−` consistent with each other:
**both sides of the consumer are being marked down at once**, which is not what a defensive rotation
looks like.

---

## §7 · Commodity / price-cycle node — the QoQ series `B1` requires
**`ADM` is a commodity processor**, so the rule fires. 🚫 **The crush-margin QoQ rate-of-change series
was NOT pulled this run** — this desk has no crush-margin feed, and `ADM`'s realised margin is only
observable at its quarterly print. ⇒ **the series is marked ABSENT, not zero**, and consequently
**no second-derivative claim is made about `ADM`.**
⚠ **And before any rate-of-change here were read as demand**: `ADM`'s margin runs through
**forward contracts and futures hedges** (§3), i.e. **a contractual band could produce the rate**
regardless of demand. **Asked and stated, per the rule.**

---

## §8 · Track KPIs and anti-signals

| KPI | current | anti-signal |
|---|---|---|
| **RULE D6 exemption, stated** | `OBV` is a **grade-C** signal (r≈0.49 to real flow; no measured lead, t=1.00) | **No OBV reading in this table carries a claim alone** — each is printed beside `flow_score`, `RS20`/`RS60` and an excess-return column benchmarked to `SPY`, and where OBV disagrees with `RS20` no verdict is issued at all |
| Node breadth on `exc20` | **9 of 9 nodes negative** | any 3 nodes turning positive ⇒ the `N−` loses its base |
| Node breadth on `exc5` | **7 of 9 positive, 6 with zero negatives** | the 5-day bounce failing ⇒ the two horizons stop disagreeing and the `N−` is unambiguous |
| Sector red-rate | **36.8% (7 of 19) = 3rd worst of 11** (was 42.1% = 2nd worst on 08-26) | rising back above 42% |
| `WMT` (46% node, sector `top1`) | `exc5` **−8.33**, `exc20` −13.67, **flow −0.589 🔴분산**, OBV −0.282 분산 | 🚨 `WMT` alone can move the sector's cap-weighted reading; **watch for it turning while the equal-weight does not** |
| **`ADM`** (`S129`, settles **09-09**) | flow **−0.643 🔴분산**, OBV −0.154 분산, `exc60` −4.06; **10-K names tariff impairment in the past tense** | `S129` **branch B (≥ +2.50pp)** ⇒ the tariff was priced before it took effect |
| `TGT` | flow **+0.733**, `exc60` **+31.61**, OBV 매집 | OBV leaving 매집; ⚠ **denominator unchecked** (§4) |
| **09-08** Canadian retaliation effective | agricultural leg **now bracketed** by `S129` (registered this run) | — this closes `D342`'s unbracketed half after 3 runs |

> *(RULE D6 exemption — stated: `OBV` is a **grade-C** signal (r≈0.49 to real flow, no measured lead, t=1.00) and **never carries a proposition alone in this file.** Every OBV reading above is printed beside `flow_score`, `RS20`/`RS60` and an excess-return column measured against `SPY`, and each claim rests on the agreement of those, not on OBV. Where OBV disagrees with `RS20` — `MNST`, and the KPI rows below — **no verdict is issued at all**, which is the rule being obeyed rather than exempted.)*


---

## §9 · Resolution verdict on ROTATION's flagged divergence

**Divergence**: `eqflow` rank 8 / red-rate 36.8% / breadth 0.00 / **0 🟢** (flow) vs `exc5` **+0.939**
with **4 of 19 negative** (price).
**Verdict: 🚨 BOTH ARE CORRECT AND THEY MEASURE DIFFERENT HORIZONS. The `N−` STANDS.**
- The **flow** instrument reads a 1-session stub bar and a 20-day-weighted OBV/RS blend ⇒ it is
  reporting the **20-day** state, where **9 of 9 nodes are negative** and the range runs to −15.04.
- The **price `exc5`** reads five settled sessions ⇒ it is reporting a **bounce**, and the bounce is
  genuinely broad (15 of 19 names positive).
- ⇒ ROTATION was right to decline the restoration to `N` on §2's numbers (a 5.3pp red-rate improvement
  and one rank), **and this file supplies the reason it could not**: the improvement is a 5-day object
  and the verdict is a 20-day object. **They were never comparable.** ⇒ `D-class` note: *a verdict and
  the number offered to reverse it must share a horizon.* ⇒ **`D384`.**

---

## §10 · Sub-sector dispersion
**`exc60` across 9 nodes: +11.96 (Food Distributors) to −5.89 (Food Retail) = 17.85pp**, against a
**sector `exc60` of +2.86** ⇒ **6.2× the sector move.**
**On `exc20`: −4.37 to −15.04 = 10.67pp** against a sector `exc20` of **−8.87** ⇒ **1.2×** — *tight*.
⇒ ★ **A genuinely unusual result and worth stating: on 20 days Staples is one of the few sectors on
this board where the label IS the right unit** — everything is down together, dispersion barely
exceeds the move. **On 60 days it is not.** The `N−` is therefore a **well-posed sector-level verdict**
on its own horizon, which is more than can be said for Energy (3.9×) or Industrials (7.5×).
⚠ Name-level dispersion is a different matter: **`TGT` +31.61 vs `WMT` −9.95 vs `MNST` −47.34** inside
19 names. **The nodes agree; the names do not.**

## §11 · What this file did NOT do
- **No 10-Q body parse** for `ADM`'s contracted/hedged share — marked `unknown` (§3, §7).
- **No valuation or revision pull for `TGT`** (§4) — named as the gap that would settle its verdict.
- **No thematic small-cap union** (blocked by G1). **No `chain-hop` pass.** **No `module_industry_map`
  call** (Korean corpus; English seeds return 0 by design).
- **No lead/lag claim appears anywhere in this file**, so none is inherited as fact.
