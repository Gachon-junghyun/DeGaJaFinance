# SECTOR_DEEP_COMM — Communication Services (UW) · 2026-08-19 · ROTATING ⇒ **FULL FRESH MAP**

> **Benchmark for every relative number in this file: `SPY`**, named inline anyway (C1).
> **Terminal settled bar = 2026-08-18.** There are no 08-19 prices here. **Every sweep `delta` is a
> TWO-session change (08-14 → 08-18)**, not a daily one (PREFLIGHT G2).
> Last covered **2026-08-14** (`llm_outputs/2026-08-14/industry_US/SECTOR_DEEP_COMM.md`) — read for
> continuity, chain rebuilt from scratch. **Analytical only. Zero buy/sell, zero sizing (P4).**

---

## §0 · Instrument state — what this file is allowed to use

| Instrument | Status | Consequence here |
|---|---|---|
| `velocity` / 51 survivors / theme freshness | 🚫 **REVOKED (G1)** — news pipe, not silence | No news statistic carries weight. `chain-hop` output below is colour, tagged as such |
| `breadth` | 🚫 **REVOKED (G1)** — not news-independent | The sector's `breadth 0.00` is **never cited as evidence** below |
| `wflow` **alone** | 🚫 barred by the mandate | Used only decomposed, never as a headline |
| `eqflow` · per-name `flow_score` · `obv_norm` · `rs20/rs60` · `vol_surge` | ✅ admissible, `asof` **08-18** | Load-bearing |
| Settled closes (`prices_2026-08-19.pkl`, `yfinance` cut 08-18) | ✅ | All price/beta arithmetic below is mine, run this session |
| FINRA Reg SHO daily short-volume (`us_flow.py`) | ✅ news-independent, print **date 2026-08-18** | **The third instrument that breaks the mandate's tie** |
| CFTC COT (`us_flow.py --cot`) | ⚪ **no COMM instrument exists** | Positioning gives this sector **nothing**; stated, not glossed. COT is also 3–4 days lagged by construction |
| Sector mcap weights (`us_top300.csv`) | ⚠️ **35 days stale** — file mtime **2026-07-15 18:04** | Quantified in §1.4 rather than carried as a warning |
| `module_chart --read` · `module_flow --positioning` · `module_fundamentals_us` | ⚠️ **contaminated by a live 08-19 bar — measured, not assumed** | Shape only, never level. See below |

🚨 **The intraday contamination is measured, not asserted.** Two identical `module_chart T --read`
calls minutes apart returned **RSI 75.5 → 75.9** and Bollinger width **11.3% → 11.4%**; `module_flow T`
printed `vol_surge` **0.41×** against the settled sweep's **0.49** and RS20 **+6.9%** against the
sweep's **+9.3**. The panels are moving on an unsettled 2026-08-19 bar (run 22:52–23:05 KST ≈ 09:52–10:05
ET, US session open). ⇒ **Every load-bearing number in this file comes from the settled 08-18 sweep or
from my own arithmetic on settled closes. The chart panels are used for *shape* only** (turn-judgement,
divergence, MA stack), and where they conflict with the settled sweep the conflict is written down (§3.3).

---

## §1 · ★★★ THE MANDATE — which reading owns the sector's sign?

**The disagreement as handed down:** `wflow` **−0.439** vs `eqflow` **−0.009** (a **0.430** gap, the
board's widest) says *"one name, `GOOGL` at 38.3%"*; MACRO §C's β-adjusted excess vs `SPY` puts `XLC`
at **−0.930, the board's worst**, and says *"the whole sector."*

### **VERDICT: NEITHER. The sector does not have a sign — and the two "opposing" instruments are not two readings, they are the same cap-weighted reading run twice through different beta assumptions. The object that has a sign is `META`.**

Four measured steps get there. None uses `breadth`, none uses `wflow` alone.

### 1.1 · The flipper test that "did not block" is **void in this sector** — the rule tests tickers, not issuers

ROTATION cleared a move because `wflow_ex_top1` is **−0.432, no sign flip**. **That test removed
`GOOGL` and left `GOOG` — the other share class of the same company, at the same 38.3% weight.**
Computed from `SECTOR_FLOW_US.json §names` this session:

| removal | `wflow` | `eqflow` | n |
|---|---|---|---|
| none | **−0.439** | **−0.008** | 12 |
| ex-`GOOGL` (the rule's own test) | **−0.432** | +0.032 | 11 |
| **ex-Alphabet (both classes)** | **−0.289** | +0.087 | 10 |
| **ex mega-platform (`GOOGL`+`GOOG`+`META`, 89.1% of sector cap)** | ★ **+0.222** | ★ **+0.178** | 9 |

⇒ **A sign flip does exist. The G3 flipper rule cannot see it because it removes top-1 *ticker*, not
top-1 *issuer*.** In a sector where one issuer holds two of the twelve tickers, `top1_flips_sign:
false` is an artifact of share-class structure and is **not** evidence of breadth. Registered below as
a dig. **True issuer concentration is 76.6% Alphabet / 89.1% mega-platform, not 38.3%.**

### 1.2 · The price instrument sits on the cap-weighted side **by construction**, and its beta is wrong for this basket

MACRO's formula reproduces exactly: β-adj excess = raw − β×`SPY`. `XLC`: −1.839 − 0.68×(−1.341) =
**−0.927 ≈ −0.930** ✅. But that applies **one blended β of 0.68** to a basket whose per-name betas are
**bimodal, not dispersed around a mean**. Measured by me this session, 252 daily returns to
**2026-08-18**, vs `SPY`:

`META` **1.43** · `GOOGL` **1.38** · `GOOG` **1.36** · `DIS` 0.68 · `TTWO` 0.67 · `LYV` 0.66 ·
`WBD` 0.60 · `NFLX` 0.27 · `CMCSA` 0.12 · `VZ` **−0.28** · `T` **−0.35** · `TMUS` **−0.39**.

A single blended β **under-credits the market decline to exactly the three names that caused the
drawdown**. Re-run per-name and re-aggregated:

| construction | raw, 08-13→08-18 | β used | **β-adj excess vs `SPY`** |
|---|---|---|---|
| `XLC` (MACRO's row) | **−1.839%** | 0.68 blended | **−0.930** |
| 12-name basket, **sweep cap weights**, per-name β | **−1.613%** | per-name | ★ **+0.049** |
| 12-name basket, **equal weight**, per-name β | **−0.854%** | per-name | ★ **−0.166** |
| 12-name basket, equal weight, blended β (0.51 measured) | −0.854% | 0.51 blended | −0.170 |

⇒ **Under a per-name beta the "board's worst sector" reading disappears in BOTH weightings.** The
−0.930 is a property of the blended-beta construction meeting a bimodal-beta basket, not a property of
the sector. This is the same defect class MACRO §H itself wrote down before its own settle.

### 1.3 · Attribution — where the −1.613% actually came from

Settled closes 2026-08-13 → 2026-08-18, `SPY` **−1.341%** (three sessions; the sweep's two-session Δ
window is 08-14→08-18 and is stated separately wherever used):

| | contribution to the cap-weighted −1.613% | share of it |
|---|---|---|
| **`META` alone** (12.5% weight, **−8.622%**) | **−1.078pp** | **67%** |
| Alphabet, both classes (76.6% weight, −0.624% / −0.773%) | −0.535pp | 33% |
| **the other nine names (10.9% of sweep cap weight)** | ★ **−0.0002pp** | ★ **0%** |

**Nine of twelve names contributed nothing to the sector's move, to four decimal places.** Per-name
β-adjusted excess vs `SPY` over the same window ranks: `WBD` **+3.436** · `GOOGL` **+1.227** ·
`TTWO` +1.101 · `GOOG` **+1.051** · `T` +0.833 · `VZ` +0.289 · `CMCSA` +0.237 · `DIS` +0.101 ·
`NFLX` −0.239 · `TMUS` −0.867 · `LYV` −2.458 · **`META` −6.704.**

🚨 **Alphabet — the name the 0.430 gap is attributed to — is POSITIVE on the exact axis MACRO used to
call this the board's worst sector (+1.227 / +1.051 vs `SPY`).** The 08-14 file called the UW "a short
of Alphabet and Meta." **Today it is a short of Meta.** That is a real change and it is the finding.

### 1.4 · Weight staleness — quantified instead of warned about

The 38.3% is built on **2026-07-15** market caps, **35 days stale (G5)**. I rebuilt the weights by
holding 07-15 implied share counts fixed and re-pricing at the **08-18 settled close**:

| | `GOOGL` | `META` | `T` | `VZ` | telecom ex-`TMUS` |
|---|---|---|---|---|---|
| stale (07-15) weight | **38.33%** | **12.51%** | 1.31% | 1.62% | **3.61%** |
| re-priced 08-18 weight | **38.47%** | **10.79%** | 1.64% | 1.98% | **4.44%** |
| drift | +0.13pp | ★ **−1.71pp** | +0.33pp | +0.36pp | +0.83pp |

`wflow` at fresh weights = **−0.420** vs the published **−0.439** — a **0.019** difference, immaterial
to the sign. ⇒ **The staleness does not break the 38.3%; it is right (38.47% today). What the staleness
hides is the direction of drift**: since 07-15 `META` is **−20.20%** and has shed 1.71pp of sector
weight, while every telecom and media name has gained weight (`T` **+16.19%**, `VZ` **+13.33%**,
`CMCSA` **+11.54%**). **The sector is de-concentrating away from the name that owns its sign, and a
35-day-stale weight file cannot show that.**

### 1.5 · The tie-breaker: a third instrument, news-independent, settled — and it sides with `eqflow`

FINRA Reg SHO daily short-**volume** z vs each name's own 20-day base, print **date 2026-08-18**:

| falling short pressure | z | 5v5 | | rising short pressure | z | 5v5 |
|---|---|---|---|---|---|---|
| `TMUS` | **−2.46** 🟢 | −4.2▼ | | `TTWO` | **+1.89** 🔴 | +4.5▲ |
| `GOOGL` | **−2.00** 🟢 | −10.1▼ | | `NFLX` | +1.01 | +10.3▲ |
| `T` | **−1.98** 🟢 | −3.7▼ | | `WBD` | +1.00 | +10.4▲ |
| `VZ` | −1.43 | −9.6▼ | | `DIS` | +0.90 | +2.4▲ |
| `GOOG` | −1.15 | −7.2▼ | | `CMCSA` | +0.40 | −7.3▼ |
| `META` | −0.84 | −4.8▼ | | `LYV` | −1.18 | −5.1▼ |

At the ETF level `XLC` reads **+0.80 with 5v5 −3.7▼** — against **+2.15 / +12.4▲** in the 08-14 file's
own KPI table. ⇒ **the marginal short seller is leaving this sector, not arriving**, and it is leaving
fastest in the two largest names. That is inconsistent with "the board's worst sector" and consistent
with "one name did it."

⚠️ **`D289` applies and is not glossed**: short *volume* and short *stock* are different objects.
`module_flow --positioning` reads `T` at **1.9% of float short and BUILDING, DTC 1.5**, while its
short-**volume** z is −1.98 falling. **Both are true.** No squeeze or capitulation claim is made from
either.

### 1.6 · The answer, in one paragraph

**`eqflow` owns the sector reading; `wflow` and the `XLC` β-adjusted print are the same reading twice.**
Both are cap-weighted; they differ only because `XLC`'s blended β of 0.68 mis-credits the market move
in a basket whose betas run −0.39 to +1.43. Corrected for that, the cap-weighted sector is **+0.049**
and the equal-weighted sector is **−0.166** — **both flat**. And `eqflow` itself *understates* the
non-mega sector: the median `flow_score` is **+0.148** (not "flat" — ROTATION's word), **6 of 12 names
are positive**, **6 of 12 are OBV-accumulating with `RS20` positive vs `SPY`** (`WBD` `NFLX` `CMCSA`
`VZ` `T` `DIS`), and ex-mega `eqflow` is **+0.178**. ⇒ **The UW is a single-stock short of `META`
carrying an eleven-sector label. Held UW is the right verdict for the wrong reason, and the reason
matters because the sector's cap weight is drifting away from the name the verdict rests on (§1.4).**

---

## §2 · Sub-sector dispersion — **the sector label is the wrong unit of analysis**, plainly

All figures `asof` 2026-08-18, weights on the 07-15 cap base (§1.4 shows the drift):

| Node | n | cap w | `wflow` | `eqflow` | med RS20 vs `SPY` | med RS60 vs `SPY` | med 2-sess Δ | OBV 매집 | med `vol_surge` |
|---|---|---|---|---|---|---|---|---|---|
| **Mega platform** `GOOGL GOOG META` | 3 | **89.1%** | **−0.519** | **−0.567** | −4.0 | **−14.3** | +0.022 | **0 / 3** | 0.64 |
| **Telecom ex-`TMUS`** `T VZ CMCSA` | 3 | 3.6% | **+0.399** | ★ **+0.404** | **+8.3** | −2.8 | +0.056 | ★ **3 / 3** | **0.52** |
| **Media/streaming** `NFLX DIS WBD LYV` | 4 | 5.2% | **+0.433** | **+0.349** | **+6.7** | −0.6 | +0.024 | 3 / 4 | 0.72 |
| `TMUS` alone | 1 | 1.7% | −0.696 | −0.696 | −6.8 | −7.6 | +0.099 | 0 / 1 | 0.64 |
| **Gaming** `TTWO` (+`EA` **not measurable**) | 1 | 0.4% | −0.311 | −0.311 | +0.2 | −1.5 | −0.101 | 0 / 1 | 0.68 |

★★★ **Dispersion exceeds the sector move by orders of magnitude, and here are the three numbers that
say so:**
1. **Node `eqflow` spread = 0.971** (telecom-ex-`TMUS` **+0.404** to mega **−0.567**) against a sector
   `eqflow` of **−0.008** and a sector two-session **Δ of −0.002**.
2. **Name-level `flow_score` spread = 1.337** (`WBD` **+0.604** → `META` **−0.733**), σ **0.486**,
   against a sector level of −0.008.
3. **Price spread over the same window = 11.25pp** (`WBD` **+2.631%** → `META` **−8.622%**) against a
   cap-weighted sector move of **−1.613%** and a **median name of −0.472%**, both vs `SPY` **−1.341%**.

⇒ **Stated plainly, as the mandate requires: "Communication Services" is not a unit of analysis this
run. Every sector-level statistic in the sweep for this bucket is a statement about `META`, plus noise
worth 10.9% of the weight and 0.0% of the move.** Any downstream stage that reads `COMM UW` as a
statement about telecom, media or gaming is reading a label, not a measurement.

---

## §3 · 🚨 FORCED QUESTION 1 — `T` is 9.59% of invested capital inside the sector the desk is UW

**The facts, from PREFLIGHT §G5-ADDENDUM and BLINDSPOT §5:** the **real KIS book** (not the paper book
— `D288`) holds `T` at **9.59% of the $7,059.28 invested**. It maps to **no cycle in
`CYCLE_EXPOSURE`**, **no `EVENT_ALPHA` card**, **no news thread**. Its settled 08-18 flow:
**+0.383 🟡중립 · OBV 매집 +0.291 · RS20 +9.3 vs `SPY` · RS60 −5.1 vs `SPY` · `vol_surge` 0.49.**

### 3.1 · Verification I ran rather than inherited

✅ **`EVENT_ALPHA` names ZERO Communication Services tickers across all 8 cards** (ticker census run on
the file: `SPY ETN MU LITE TSLA NUE ANET RTX COHR PWR WDC VRT STX PSX NVDA MPC LHX HBM GEV CAT XOM
STLD SNDK NOC NDAQ MET LMT INTC HPE GLW GD DE CVX COP CIEN BA AXON AVGO`). ⇒ the gap is **stronger
than reported**: it is not that `T` has no card — **the entire sector has no card.**

✅ **News surface, `module_news_data chain-hop`, run 22:55:38 KST** — `"AT&T fiber"` 7d returned
**3 articles scanned**, `T` appearing at 3 proximate / 3 body, and its single surfacing example is a
yield-screen listicle (*"5 of JP Morgan's Top Stock Picks Pay Big Dividends…"*). `"telecom"` 7d returned
162 articles with `T` at 4 title / 19 body, below `NVDA` (6/31), `GOOGL` (3/29) and `MSFT` (4/25).
⚠️ **This is colour only — G1 revokes every news statistic this run**, and the first call at 22:55:11
returned **0 articles** on the identical pipe. It is recorded because it *corroborates* an
independently-derived absence, never as evidence on its own.

### 3.2 · The resolution — the UW and the holding are not in conflict; the **label** is

The desk is not underweight the thing it owns. Decomposed (§1, §2): the UW is a short of `META`
(β-adj **−6.704** vs `SPY`); `T` sits in a 3.6%-weight node whose `eqflow` is **+0.404**, whose three
names are **3 of 3 OBV-accumulating with RS20 +8.3 median vs `SPY`**, and whose own β-adjusted excess
is **+0.833 vs `SPY`** — the **5th best of the twelve**. **`T` and the UW are pointed at different
objects and the GICS label hides that.**

⚠️ **But that is a justification, not an endorsement, and the honest reading is worse for the desk:**
`T` is an **orphan position**. It has no cycle, no card, no thread, no bracket, and no KPI in any live
artifact. **It is not an expression of the sector view in either direction — it is unlabelled risk that
happens to be working.** The desk cannot claim credit for a position it has no thesis for, and it
cannot manage one either. **P4 holds: no size, no direction, no action is proposed here.**

### 3.3 · 🚨 The counterweight — three instruments disagree about `T`'s accumulation, and I am not picking

| instrument | window | reading |
|---|---|---|
| Sweep `obv_norm` (settled 08-18) | long | **매집 +0.291** |
| `module_flow T` | mixed, live 08-19 bar | **매집**, RS20 +6.9% vs `SPY`, `vol_surge` 0.41× |
| `module_chart T --read` | **20-day OBV slope** | 🚨 **분배 −55%**, with **bearish divergence (price HH · RSI LH)** |

`VZ` shows the identical pattern (sweep `obv_norm` **+0.180 매집**; chart 20d OBV slope **−28% 분배**,
same bearish divergence). ⇒ **The coherent read is that the accumulation in `T`/`VZ` is OLDER than 20
days, and the last 20 sessions are price-up-on-declining-OBV.** Both names are **BREAKOUT** on the turn
judgement with **RSI 75.9 / 75.1**, price **4/4 MAs above**, and Bollinger widths of **11.4% / 9.8%
(coiling at the upper band)** — a shape that is extended, not early. `CMCSA` reads **RSI 78.9,
momentum20d +22.1%**. ⚠️ **RULE D6 stated, not dodged**: OBV is grade-C and supports nothing alone —
every OBV line above is paired with RS20/RS60 vs `SPY` and momentum, and the three-way conflict is left
open rather than resolved to the convenient side.

### 3.4 · Valuation — the claim the constraint would require is **NOT MADE**, and here is why

The tempting sentence is *"`T` is cheap at a forward P/E of 9.86."* **The constraint requires the
margin percentile in `T`'s own history. That number is not computable with the desk's instrument:**
`scripts/margin_history.py T` returns **FY2007–FY2014 only** (8 years · peak FY2007 **60.6%** · trough
FY2008 **54.1%** · median **58.7%**) — the series **stops eleven fiscal years before the current one**
and pre-dates the entire DirecTV / Time Warner / Discovery acquire-and-divest cycle. ⇒ **No
forward-multiple cheapness claim is made in this file.**
🚩 **Correction to the 08-14 file**, which cited *"`T` gross-margin median 58.7%"* without stating that
the window ends FY2014. The number is real; the window is not usable.

**What can be said mechanically, with no percentile required:** `T` trades at **trailing P/E 8.35 vs
forward P/E 9.86** because **forward EPS $2.56 < trailing EPS $3.03** — consensus expects EPS to
**fall ~15.5%**, so the multiple *expands* forward. That is arithmetic, not a valuation judgement.
**Estimate-revision trend (direction only, never a leading indicator, zero independent weight):**
bifurcated — next quarter **−3.9% over 90d** with 7d breadth **2↑ / 12↓**, while current year is
**+0.9%** (**15↑ / 3↓** over 30d) and next year **+0.3%** (**13↑ / 5↓**). Near-term cuts, full-year
raises. ⚪ `T` is **not** an IT-adjacent name, so the desk's no-independent-weight rule for IT-adjacent
revisions is not the binding constraint here — the constraint that binds is simply that a revision
trend describes consensus momentum, not the business.

---

## §4 · FORCED QUESTION 2 — `EA` is **not measurable**, and what that does to every statistic here

**Never "no signal." `EA` (Electronic Arts, Interactive Home Entertainment, `us_top300` rank 235,
07-15 mcap $50.69bn) is NOT MEASURABLE.** PREFLIGHT G5: **0 non-null fields on every row of the 84-row
price frame** — not a stale bar, an absence. The sector's composition is **12 of 13**.

### 4.1 · The replication count is **2, not 7** — measured across the artifact series

PREFLIGHT calls this the **7th consecutive run**. Reading the `SECTOR_FLOW_US.json` series directly:

| run | `asof` | COMM `n` | `EA` in sweep |
|---|---|---|---|
| 08-13 | 2026-08-12 | 13 | ✅ flow +0.671 |
| 08-14 | 2026-08-13 | 13 | ✅ flow +0.617 |
| 08-15 / 08-16 / 08-17 / 08-18 | **2026-08-14 (frozen, identical file)** | **12** | ❌ |
| **08-19** | **2026-08-18** | **12** | ❌ |

⇒ **7 runs, but only TWO distinct settled tapes** (`asof` 08-14 and 08-18) in which `EA` is absent,
because the tape was frozen for four runs. **The defect has replicated twice, not seven times**, and
the run-count overstates the evidence. ✅ It also **reconciles the two artifacts**: the 08-14 file's
`EA` numbers (flow +0.617, `vol_surge` 3.44) were real at `asof` 08-13; `EA` left the sweep at the very
next `asof`. They do not contradict.

### 4.2 · Effect on each statistic in this file, stated per statistic

| statistic | effect of `EA` being not measurable |
|---|---|
| `n = 12` | The denominator of **every mean below** is 12. Not 13 |
| `eqflow −0.008` | A mean over 12 with an **unknown 13th term**. Its error bar is **unknown, not zero** — `EA`'s last measured flow (+0.671 at `asof` 08-12) would have *raised* it, but that value is stale and inadmissible |
| Cap weights (§1.4) | **Immaterial.** Restoring `EA` to the denominator moves `GOOGL` **38.33% → 38.17%** (−0.16pp) and every other weight by <0.05pp |
| Two-session Δ **−0.002** | ✅ **Uncontaminated** — `EA` was already absent at both endpoints (`asof` 08-14 and 08-18) |
| 🚨 **The gaming node** | **Destroyed.** "Interactive Home Entertainment" is 2 of 13 names; one is not measurable and the other (`TTWO`, **0.4% weight**) is the only survivor. ⇒ **This file makes NO characterisation of gaming as a sub-sector.** The §2 row exists to show the hole, not to describe the node |
| Run-over-run continuity vs the 08-14 file | ⚠️ **A composition break sits between them.** That file's `eqflow` was **−0.107 with `EA`** and **−0.167 ex-`EA`** — the break is worth **0.060** on `eqflow`. Any 08-14 → 08-19 comparison crosses it, and every such comparison below says so |
| `breadth 0.00` | Irrelevant — revoked by G1 regardless |

---

## §5 · FRAME-TRANSFER (mandatory) — take-or-pay / RPO / regulated-return: **CHECKED, DOES NOT APPLY**, and the nearest analogue runs the other way

This desk leans on contracted lock-in elsewhere (RPO, take-or-pay, regulated return). **Tested against
primary filings, not assumed.**

### 5.1 · Telecom — `T` FY2025 10-K (filed **2026-02-09**, period **2025-12-31**, accession 0000732717-26-000120)

Term-by-term hit counts across Item 1 + Risk Factors + MD&A (51,500 chars):

| term | hits |
|---|---|
| `remaining performance obligation` | **0** |
| `take-or-pay` | **0** |
| `backlog` | **0** |
| `tower` | **0** |
| `IRU` / `indefeasible` | **0 / 0** |
| `regulated rate` | **0** |
| `rate of return` | 2 — **both are pension assumptions** (7.75% plan assets, 4.00% postretirement), not a regulated utility return |

⇒ **None of the three structures exists in the filing.** Wireless revenue is month-to-month subscriber
revenue; there is no contracted backlog to lock in.

🚨 **And the closest measurable substitute — churn — is deteriorating, disclosed by the company:**
postpaid churn **1.05% (2025) vs 0.92% (2024) vs 0.98% (2023)** = **+13bp**; postpaid phone churn
**0.90% vs 0.76% vs 0.81%** = **+14bp**; Mobility net subscriber additions **2,314k vs 4,168k
= −44.5%**, total phone net adds **1,159 vs 1,525 vs 1,801 = −24.0%**. Total Mobility subscribers grew
to **120,105k, +1.9%**. ⇒ **The annuity frame that take-or-pay would supply is not merely absent — the
retention metric that would proxy for it is worsening while the base still grows.**

### 5.2 · The one telecom-adjacent structure that DOES carry the lock-in **is not in this sector**

Tower ground leases and master lease agreements with contractual escalators are the genuine
take-or-pay analogue in connectivity. In `us_top300` they are classified **`AMT` (rank 148) and `CCI`
(rank 289) — GICS "Telecom Tower REITs", sector Real Estate**, which this desk holds **UW** at a
β-adjusted excess of **−0.719 vs `SPY`**. (`SBAC` is not in the universe.) Their own settled 08-18
flow: `AMT` **+0.232, OBV 매집, RS20 +2.9 vs `SPY`**; `CCI` **−0.369, OBV 중립, RS20 −5.4 vs `SPY`**.
⇒ **The frame transfers to a different GICS sector than the one the mandate asked about, and it does
not transfer into COMM at all.**

### 5.3 · Streaming — `NFLX` FY2025 10-K (filed **2026-01-23**, period **2025-12-31**): the lock-in exists and points the **wrong way**

| term | hits |
|---|---|
| `remaining performance obligation` / `take-or-pay` / `backlog` / `month-to-month` | **0 / 0 / 0 / 0** |
| `content obligation` | **2 — and this is the finding** |

Disclosed contractual obligations: **content obligations $24.0bn** ($4.1bn current content liabilities
+ $1.6bn non-current on the balance sheet + **$18.4bn NOT reflected on the balance sheet**), debt
$18.1bn, operating leases $2.9bn — **total $45.0bn, of which $13.8bn falls due within one year.**
Content obligations include *"non-cancelable commitments under creative talent and employment
agreements."*

⇒ ★ **In streaming the contractual lock-in is a PAYABLE, not a receivable.** Take-or-pay elsewhere on
this desk means the *customer* is committed to pay the node. Here the *node* is committed to pay its
suppliers **$24.0bn** while its own revenue side carries **zero** contracted backlog and cancel-any-time
subscriptions. **That is negative operating leverage into a demand shock — the exact inverse of the
frame.**

### 5.4 · ⇒ Frame-transfer verdict

**It does not apply to telecom (0 RPO / 0 take-or-pay / 0 tower / 0 IRU / 0 regulated rate, with churn
deteriorating), and it applies to streaming only with the sign reversed (a $24.0bn obligation owed BY
the node).** **No claim anywhere in this file leans on contracted lock-in in Communication Services.**
The `T` / `VZ` / `CMCSA` positive flow is a **price-and-carry** reading, not a scarcity or contract
reading, and the 08-14 file's identical caution is carried forward unchanged and now with filing
receipts.

---

## §6 · Value chain, node customers, and their **disclosed spend or print dates**

`content creation → aggregation/platform → AD DEMAND · SUBSCRIPTION → distribution/CDN → CONNECTIVITY → device`

**Bottleneck = ad demand at the platform node**, and it is binding against exactly one company.

### 6.1 · Mega-platform node — customers are advertisers; **no ticker-level disclosed spend exists, so print dates are given**

Advertiser spend is not disclosed at a level any desk instrument can check. **Print dates instead, as
the mandate permits.** The measurable proxy that *is* checkable is what the sell-side is doing to the
node's own numbers, and it separates the two names completely:

| | `META` | `GOOGL` |
|---|---|---|
| current-quarter estimate, 90d change | **−4.3%** | −0.1% |
| current-quarter revision breadth, 7d | 🚨 **9↑ / 31↓** | 19↑ / 18↓ |
| current-year breadth, 7d · 30d | 🚨 **5↑ / 44↓ · 8↑ / 43↓** | 2↑ / 0↓ · 47↑ / 0↓ |
| next-year, 90d change · breadth 7d | **−2.3% · 6↑ / 39↓** | +2.4% · 4↑ / 4↓ |
| price, 08-13→08-18 vs `SPY` −1.341% | **−8.622%** | −0.624% |
| turn judgement (`module_chart --read`, shape only) | **NEUTRAL/CHOP**, bearish MA stack 5<20<60<120, **0/4 MAs above**, lower band, momentum20d **−10.0%** | **NEUTRAL/CHOP**, 0/4 MAs above, OBV 20d **+16% 누적**, RSI 54.5, momentum20d **+7.6%**, trigger 344.48 vs settled close **344.20** |

⚠️ **Direction only, and it carries no independent weight — these are IT-adjacent names and the desk's
rule is explicit about that.** ⚠️ **Data-hygiene flag, not a signal**: `GOOGL`'s current-year estimate
jumped **14.23 → 20.59 (+44.7%) in 30 days with breadth 47↑/0↓**, while its own forward EPS reads
$14.75. A 45% consensus jump with zero downgrades is a **definition change or a one-off inclusion**,
not a revision trend. **It is not used as evidence anywhere in this file.**
⇒ **The coincidence is the point: the one name whose estimates are being cut across all four horizons
is the one name that produced 67% of the sector's drawdown.** No lead/lag claim is made — I did not
measure whether revisions led price, and per the rule I will not assert it. **[unverified]** if anyone
downstream wants that ordering.

### 6.2 · Connectivity node — customers ARE disclosed, and their spend is checkable

`T`'s customers are **120,105k Mobility subscribers** (consumer) plus **Business Wireline** enterprise
customers (advanced ethernet-based fiber, fixed wireless, IP Voice, managed professional services).
**No customer concentration is disclosed — no single customer is named in the 10-K** ⇒ the checkable
form of "customer spend" is the node's own reported revenue.

**Disclosed spend, with print dates:** Q2 2026 revenue **$31.56bn**, **+2.30% YoY** and **+0.16%
QoQ** vs Q1 2026's $31.51bn (C2 satisfied — the sequential is given alongside the year-on-year, and it
is the flatter of the two). **XBRL cross-verified: 4/4 quarters within 5%, 0.0% difference on both
2026 quarters.** Prints: **10-Q filed 2026-07-22** (period 2026-06-30) · **8-K Item 2.02 earnings
2026-07-22** · **8-K Item 7.01 Reg FD 2026-07-28** · **next earnings 2026-10-21**. 90-day EDGAR
census: **56 filings — 35 Form 4, 5 8-K, 1 10-Q — and ZERO in the 수주/계약/M&A category.**
⇒ **No contract, award or M&A event underpins `T`'s move. There is nothing in the filings to explain
it; the move is price and flow.**

### 6.3 · What the chain says

⚠️ **Strong flow ≠ bottleneck.** The connectivity node has **no capacity constraint** — its positive
`eqflow` (+0.404) is a carry-and-rotation reading, not scarcity, and §5 removes the contract frame that
would have dressed it as one. **The single binding constraint in this chain is ad-demand risk at
`META`**, and it is a one-company constraint, not a sector one — which is the same conclusion §1 and
§2 reach from price and flow independently. ★ **Three independent routes, one answer.**

---

## §7 · The 08-14 anti-signals, scored — ⚠️ across a composition break (§4.2)

| # | Registered 08-14 | Measured now (settled 08-18) | Status |
|---|---|---|---|
| **1** | Mega-platform median Δ **≥ +0.20** for three consecutive settled sessions **AND** median RS60 rises above **−10** ⇒ the "less bad" leg is a turn | median Δ **+0.022** (was +0.244) · median RS60 **−14.3 vs `SPY`** (was −17.8) | ❌ **NOT FIRED — leg 1 collapsed.** The "less bad" leg stopped; RS60 improved 3.5pp but stayed 4.3pp short |
| **2** | `XLC` FINRA z falls **below +0.5** while exc5 **stays positive** ⇒ the marginal seller has left | z **+0.80** (was +2.15), 5v5 **−3.7▼** (was +12.4▲); `XLC` exc5 vs `SPY` = **−0.498, NEGATIVE** | ❌ **NOT FIRED on both legs** — z is falling fast but still above +0.5, and the excess leg has the wrong sign |
| **3** | 🚨 Telecom-ex-`TMUS` `eqflow` **> +0.25 for three sessions** while the sector stays UW ⇒ the desk is underweighting a bucket in which a positive node is structurally invisible to its own gate | Across **six distinct settled tapes**: 08-07 **+0.513** · 08-11 **+0.477** · 08-12 **+0.347** · 08-13 **+0.286** · 08-14 **+0.352** · 08-18 **+0.404**. **All six above +0.25. Sector held UW at every one** | 🚨 ★ **FIRED — 6 of 6, and it is the one that fired** |

★ **Anti-signal 3 fired and its diagnosis is now mechanical, not rhetorical.** The gate cannot see this
node because **the entire sector's maximum `vol_surge` is 0.91** — below the 🟢 threshold of 1.2 — and
the three telecom names hold the **three lowest readings in the sector (`T` 0.49 · `VZ` 0.52 ·
`CMCSA` 0.61)**. Six of twelve names pass `OBV 매집 ∧ RS20>0 vs SPY` (`WBD` `NFLX` `CMCSA` `VZ` `T`
`DIS`) and **0 of 6 clear the volume gate**. This is the same `M144` volume-gate artifact SWEEP §3
diagnosed in Energy (max 1.06) and Health Care (max 1.00) — **its 8th sector instance** — and in COMM
it has been suppressing the same three names for six consecutive tapes. **Low-turnover mega-cap telcos
structurally cannot clear a volume-surge gate.** ⚠️ The artifact is diagnosed, and **diagnosing an
artifact is not the same as having the signal it hid** — nothing is promoted on it.

---

## §8 · Track KPIs and anti-signals for the next COMM slot

| Track KPI | Current (settled 08-18) | What it reads |
|---|---|---|
| `META` β-adj excess vs `SPY` | **−6.704** | **the whole sector verdict, in one number** |
| Alphabet (`GOOGL`/`GOOG`) β-adj excess vs `SPY` | **+1.227 / +1.051** | the half of the UW that is already wrong |
| ex-mega `wflow` · `eqflow` | **+0.222 · +0.178** | what "the sector" is once the label is removed |
| telecom-ex-`TMUS` `eqflow` | **+0.404** (6th straight tape > +0.25) | anti-signal 3, now fired |
| sector max `vol_surge` | **0.91** | the gate that makes 6 accumulating names invisible |
| `XLC` FINRA short z / 5v5 | **+0.80 / −3.7▼** | the marginal seller leaving |
| `META` current-year revision breadth 7d | **5↑ / 44↓** | direction only, no independent weight |
| `EA` not measurable | **2 distinct tapes** (not 7 runs) | the correct replication count |
| `T` in `CYCLE_EXPOSURE` | **still absent** | 9.59% of invested, unlabelled |

**Anti-signals — what would falsify the readings in this file:**
1. **`META`'s β-adjusted excess vs `SPY` turns positive over a settled 5-session window while ex-mega
   `eqflow` stays above +0.15** ⇒ §1's "one name owns the sign" survives but the sign inverts, and the
   UW is short a bottoming asset with a broadening tail.
2. 🚨 **`GOOGL` closes above 344.48 (its own `module_chart` trigger; settled 08-18 close 344.20, i.e.
   0.08% below) with OBV turning 누적 and RS60 vs `SPY` rising above −10** ⇒ Alphabet's β-adjusted
   positivity (§1.3) becomes a price fact, and the cap-weighted UW is short two-thirds of a sector that
   is working.
3. **Telecom-ex-`TMUS` `eqflow` falls below +0.25 while `T`/`VZ` 20-day OBV slopes stay negative**
   ⇒ §3.3's "the accumulation is older than 20 days" resolves against the node, and the RSI-75 breakout
   shape was the top of the move, not the start.
4. **Sector max `vol_surge` clears 1.2 on any name** ⇒ the `M144` gate artifact stops binding here and
   the sector's shortlist absence becomes readable as evidence for the first time.
5. **`EA` returns to the sweep with non-null fields on two consecutive distinct `asof` tapes** ⇒ the
   gaming node becomes characterisable and §2's blank row can be filled.

---

## §9 · Digs and corrections registered by this file

- **`D290` — the G3 flipper rule tests top-1 TICKER, not top-1 ISSUER.** In COMM, `wflow_ex_top1`
  removes `GOOGL` and leaves `GOOG` at the same 38.3% weight, producing `top1_flips_sign: false` on a
  sector where removing the issuer's two tickers moves `wflow` **−0.439 → −0.289**, and removing the
  mega node **flips it to +0.222**. **The rule should test issuer, or print a share-class-adjusted
  `top1_w`.** → human (P5).
- **`D291` — a single blended beta applied to a bimodal-beta basket manufactures a sector verdict.**
  `XLC`'s β 0.68 across per-name betas of −0.39 to +1.43 produces **−0.930**; per-name betas produce
  **+0.049 (cap) / −0.166 (equal)**. The **"board's worst sector"** label is a construction output.
  Same defect class MACRO §H flagged on `S98`. → human (P5).
- **Correction to `SECTOR_DEEP_COMM` 2026-08-14**: `T` gross-margin median **58.7%** is real but the
  `margin_history.py` series **ends FY2014**; it cannot support a percentile and no valuation claim may
  rest on it (§3.4).
- **Correction to `SECTOR_ROTATION` 2026-08-19**: *"the median name is flat"* — the measured median
  `flow_score` is **+0.148**, with 6 of 12 positive and 6 of 12 OBV-accumulating with RS20 positive vs
  `SPY`. The median name is **mildly positive**, and `eqflow`'s −0.008 is itself pulled to zero by
  `META`'s −0.733.
- **Refinement to PREFLIGHT G5**: `EA`'s **"7th consecutive run"** is 7 runs but **2 distinct settled
  tapes** (§4.1). The replication count is 2.

---

## ✅ EXIT CHECK

- [x] **The mandate is answered explicitly and in one sentence** (§1.6): **neither reading owns the
      sign; `wflow` and the `XLC` β-adjusted print are the same cap-weighted reading twice, and the
      object with a sign is `META`, not the sector.**
- [x] Resolved **without `breadth`** (G1 — its 0.00 is cited only to say it is unusable) and
      **without `wflow` alone** (used only decomposed; a third instrument, FINRA short-volume, breaks
      the tie, and a fourth route — filings/revisions — reaches the same place).
- [x] **Sub-sector dispersion stated with three numbers, and the "sector label is the wrong unit"
      conclusion drawn plainly** (§2).
- [x] **`T` resolved** (§3): the UW and the 9.59% holding point at different objects; `T` is an
      **orphan** with no cycle, no card (verified: the whole sector has no card), no thread — and the
      counterweight that three instruments disagree about its accumulation is written down (§3.3).
- [x] **`EA` handled as "not measurable", never "no signal"**, with a per-statistic effect table and a
      corrected replication count (§4).
- [x] **Frame-transfer question answered** (§5): does not apply to telecom (0/0/0/0/0 hits, churn
      worsening), applies to streaming with the sign reversed ($24.0bn payable), and the genuine
      lock-in structure sits in Real Estate.
- [x] **Node customers named and their disclosed spend checked** for connectivity (120,105k subscribers
      + Business Wireline; Q2 2026 revenue $31.56bn, +2.30% YoY / +0.16% QoQ, XBRL 4/4 verified;
      prints 07-22, 07-28, next 10-21); **print dates given** for the platform node where no
      ticker-level customer spend is disclosable.
- [x] **Every relative-performance number names `SPY` inline**; every β carries its 252-day window and
      its 2026-08-18 endpoint.
- [x] **Weight staleness quantified, not warned about** (§1.4): 35 days moves `wflow` by 0.019 and the
      38.3% is right, but it conceals a −1.71pp `META` weight decay.
- [x] **No "cheap on forward multiple" claim is made** — the required margin percentile is not
      computable and that is stated instead of the claim (§3.4). Revision trends appear as direction
      only, with no independent weight, and one is flagged as a data-hygiene artifact.
- [x] **No unmeasured lead/lag claim.** The one ordering a reader might want (revisions → price) is
      tagged **[unverified]** (§6.1).
- [x] **Live-bar contamination measured** (two identical calls, RSI 75.5→75.9) and quarantined: chart
      panels used for shape only, all levels from settled 08-18.
- [x] **Zero buy/sell, zero sizing (P4).** `T`'s 9.59% is quoted as an existing book fact the mandate
      required, never as a size.
- [x] `python -X utf8 scripts/report_lint.py llm_outputs/2026-08-19/industry_US/SECTOR_DEEP_COMM.md`
      ⇒ **총 0건 · ✅ clean**, and `--strict` exits **0**. Rules C1 (benchmark named) · C2 (YoY paired
      with sequential) · S6 (future-using label tagged) · D6 (OBV never cited alone) — **no findings,
      so no rule ID is carried with a reason.**
