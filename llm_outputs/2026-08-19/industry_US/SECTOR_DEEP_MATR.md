# SECTOR_DEEP_MATR — Materials (N−) · 2026-08-19 (Wed) · all prices SETTLED 2026-08-18

> **benchmark: `SPY`** on every relative-performance number in this file, named inline (C1).
> **ROTATING track ⇒ FULL FRESH MAP.** Last covered **2026-08-13**; that file was read for continuity and
> its four claims that this run breaks are named in §10, not quietly dropped.
> **Analytical only — zero buy/sell language, zero position sizing (P4).**
>
> **Rights inherited and obeyed:**
> - 🚫 **G1** — sweep `velocity` and the 51 survivors are **REVOKED**; `breadth` is news-contaminated and
>   is **not** read as an independent statistic. Every news item below comes from **this file's own
>   `module_news_data` calls**, with the call clock stated.
> - 🚫 **G2** — the terminal settled bar is **2026-08-18**. **No 2026-08-19 price is used anywhere.**
>   Every sweep `delta` is a **TWO-session** change (08-14 → 08-18), never a daily one.
> - 🚫 **G3** — **`wflow` may not carry a promote or a demote in this file.** Materials `wflow` **−0.117**
>   flips to `wflow_ex_top1` **+0.060** on `LIN` (24.7% of sector cap). Admissible flow axes here are
>   **`eqflow` −0.060**, the **two-session `delta` +0.052**, and **per-name** rows. No verdict below rests
>   on `wflow`, and §0 states the one instrument that is structurally immune to the flipper.
> - 🚫 **G5** — sector cap weights are **35 days stale**, and this run found the two cap sources disagree
>   (see §1 note). Weights are used for *description only*, never to carry a sign.
> - **D6** — OBV is a grade-C axis and never carries a claim alone; every OBV state below is paired with
>   an RS20/RS60 momentum reading vs `SPY`.
> - **D1/D2** — where a statistic is **my own reconstruction** rather than the desk's object, it is
>   labelled as a different object.
> - **C3** — where a filing does not disclose the number, the answer is **`unknown`**, never an estimate.
>
> ⚠ **Run clock, and it matters.** The tool calls in §7 and §9 (`module_chart --read`,
> `module_flow --positioning`) were made at **KST 22:58–23:25 = ET 09:58–10:25, with the US cash session
> OPEN.** Those instruments therefore carry an **in-progress 2026-08-19 bar.** They are used only to
> describe *options/short-interest* objects and to diagnose an instrument conflict — **never to carry a
> settled price, OBV or RS claim.** All settled numbers in this file come from `yfinance`
> `auto_adjust=False` closes through **2026-08-18** and from `SECTOR_FLOW_US.json` (`asof` 2026-08-18).

---

## §0 · THE ASSIGNED QUESTION — RESOLUTION VERDICT

**Question**: *the sector has its first NEM-free evidence (`S77`) and a contradicting positioning extreme
(`Copper` COT 100th percentile) in the same run — **which of the two IS the sector?***

### 0a · Verdict, in one line

> **`S77` is the sector. The `Copper` COT is one node's forward positioning, and this run measured that it
> cannot reach the sector observable in either direction at any plausible magnitude — but `S77` is a
> FIVE-SESSION object, and the same eleven names are +0.637 vs `SPY` over sixty sessions, so what it
> confirms is "the underweight is not a `NEM` artifact", NOT "Materials is deteriorating."**

This is a resolution, not a split. Six measurements force it, in order of weight.

### 0b · `S77` recomputed independently — it reproduces to the third decimal

Self-computed, `yfinance` `auto_adjust=False`, five settled sessions **2026-08-11 close → 2026-08-18
close**, `SPY` return over the identical window **−0.404%**. This is an independent reconstruction of the
registered observable, not a re-print of `SECTOR_ROTATION`'s number.

| name | 5-session return | **5-session excess vs `SPY`** | β (252d, vs `SPY`) | **β-adjusted excess vs `SPY`** |
|---|---|---|---|---|
| `CTVA` | +2.217% | **+2.621** | 0.13 | +2.268 |
| `ECL` | −1.627% | −1.223 | 0.50 | −1.427 |
| `APD` | −1.966% | −1.562 | 0.19 | −1.887 |
| `LIN` | −2.410% | −2.006 | 0.10 | −2.371 |
| `NUE` | −2.853% | −2.450 | 0.94 | −2.476 |
| `FCX` | −3.703% | −3.299 | 2.24 | −2.799 |
| `SHW` | −5.255% | −4.851 | 0.82 | −4.925 |
| `STLD` | −5.264% | −4.860 | 1.14 | −4.804 |
| `MLM` | −5.574% | −5.170 | 0.82 | −5.243 |
| `VMC` | −5.608% | −5.205 | 0.77 | −5.299 |
| `CRH` | −7.938% | −7.534 | 1.29 | −7.417 |
| **EW of the 11** | — | **−3.231** | — | **−3.307** |

**`S77` = −3.231, 10 of 11 negative** — identical to the figure `SECTOR_ROTATION §2d` and `MACRO §E`
carry, computed here from raw closes. **Branch B (≤ −2.04) is satisfied by 1.19pp.**
For reference on the same window, `XLB`'s own excess vs `SPY` is **−2.339** and `NEM`'s is **−0.646**.

⚠ One reconciliation, stated because it changes a number: a naïve `dropna()` on the merged frame shifts
`CTVA`'s window by one session and returns **+2.287** instead of **+2.621**. The correct value is the one
computed on `SPY`'s own trading calendar. **The run's per-name figure (+2.62) is right and the naïve one
is wrong**, and the difference is 0.03pp on the EW.

### 0c · ★★★ `S77` is **beta-clean** — the defect that voids `S98` and cripples `S80` does not reach it

This run's own `MACRO §Headline` and `BLINDSPOT §3a` established the board's dominant construction
defect: **in a directional `SPY` tape, a low-beta basket prints excess vs `SPY` by construction.** That
defect voids `S98`'s branch A and flips `S80`'s sign under β-adjustment.

**It cannot produce `S77`.** The window's `SPY` move is **−0.404%**. The single largest beta contribution
available anywhere in the basket is `FCX` at β 2.24 ⇒ **0.90pp**; the EW basket's beta-mechanical
contribution is **+0.34pp**. β-adjusting every leg individually moves the observable from **−3.231 to
−3.307 — i.e. it gets WORSE, not better.**

> ⇒ **`S77` is the only sector-level observable settling on this board tonight whose sign survives the
> defect that broke the other two.** Whatever else is true, the −3.231 is not a beta artifact.

### 0d · `S77` is also **flipper-proof**, which is why it is admissible where `wflow` is not

G3 forbids moving Materials on `wflow` because `LIN` (24.7% of sector cap) inverts its sign. **`S77` is
equal-weighted**, so `LIN` enters at **1/11 = 9.1%**, and the flipper mechanism is structurally absent.
Leave-out tests, self-computed:

| basket | EW 5-session excess vs `SPY` | still branch B (≤ −2.04)? |
|---|---|---|
| **all 11 (`S77` as registered)** | **−3.231** | ✅ |
| ex-`LIN` (removes the G3 flipper) | **−3.353** | ✅ — moves *away* from branch A |
| ex-`FCX` (removes the entire copper node) | **−3.224** | ✅ — **a 0.007pp change** |
| ex-aggregates (`CRH`,`VMC`,`MLM` — the worst sub-sector) | **−2.204** | ✅ |
| ex-`CRH` (the single worst name) | **−2.800** | ✅ |

**No single name and no whole sub-sector removal lifts the observable to branch A.** The reading is not
one name, and it is not one node.

### 0e · ★★★ The arithmetic reach of the `Copper` COT into `S77` — measured, and it is bounded

`Copper` spec net **+80,388 · wk Δ +3,265 ▲ · 27.1% of OI · 100th percentile of its 1-year range** — the
most extreme reading on the whole positioning board (`scripts/us_flow.py`, this run). ⚠ COT is a
Tuesday-dated snapshot published Friday, so it carries a **3–4 day lag**, and the desk's own rule is
stated and obeyed: **an extreme percentile is contrarian ammunition, it is not a direction.**

The sector observable's only copper leg is `FCX`. Its transmission is **measured this run**, not assumed:
regressing `FCX`'s daily excess vs `SPY` on `HG=F`'s daily % over **120 settled sessions to 2026-08-18**
gives **β = +1.177 pp per 1%, r = +0.663** — a strong, real channel. Applying it:

| copper move (`HG=F`) | implied `FCX` excess vs `SPY` | implied `S77` (EW-11) | branch |
|---|---|---|---|
| **−10%** | ≈ −15.1 | **≈ −4.30** | **deeper into B** |
| 0% (as measured) | −3.30 | **−3.231** | **B** |
| +10% | ≈ +8.5 | **≈ −2.16** | still **B** |
| **+49.2%** | ≈ +54.6 | **+2.03** | the *first* copper move that reaches branch A |

> ⇒ **`HG=F` would have to rise about 49% for the copper node alone to carry `S77` out of branch B and
> into branch A.** And the adverse reading of the crowded long — the one the contrarian frame actually
> licenses as a *risk* — pushes the observable **further into branch B, not out of it.**
>
> **The positioning extreme cannot be the sector because it cannot move the sector's own observable.**

### 0f · The two instruments are not competing answers — they answer different questions

| | `S77` | `Copper` COT |
|---|---|---|
| object | realised excess return vs `SPY` | a stock of speculative positioning |
| span | **5 settled sessions**, closed | undated; an extreme has no expiry |
| lag | none (settled closes) | **3–4 days** (Tue snapshot, Fri release) |
| coverage | 11 names, 6 of 7 sub-sectors, **88.4% of sector cap** (EW) | 1 node, **1 name, 10.3% of sector cap** |
| what it can falsify | "the Materials weakness was `NEM`-shaped" | "the marginal copper buyer still has room" |

⇒ **`S77` answers the question the sector verdict is about. The COT answers a question about `FCX`'s
forward earnings input.** Reading the COT as a contradiction of the sector verdict is a category error,
and the leave-one-out in §0d is the proof: delete the node the COT describes and the sector observable
does not move.

★ **And the copper node's own tape is not corroborating the crowded long.** `HG=F` settled **6.48** on
2026-08-18: **−1.96% over 5 sessions, −0.44% over 20.** A record spec position that is **still being
added to** (+3,265 on the week) into a price that has gone nowhere for a month is the configuration where
positioning has stopped being paid — stated as a description of the two series, **not** as a direction.

### 0g · ★ The honest counterweight — three measurements that argue *against* over-reading tonight's settle

These are not caveats appended after the verdict; they bound it.

1. **The same eleven names are POSITIVE over sixty sessions.** EW 60-session excess vs `SPY` = **+0.637**
   (20-session: **−1.239**). `S77` is a five-day statement nested inside a flat-to-positive sixty-day one.
   **Branch B says "the last five sessions were broad and negative", and it may not be extended past that.**
2. **The admissible flow axis moved the OTHER WAY over the same two settled sessions.** Materials'
   two-session `delta` is **+0.052 — positive**, and `ECL`'s **+0.628 is rank 5 of all 299 scored names.**
   Over 08-14 → 08-18 the EW price excess vs `SPY` is **−0.686 with 7 of 11 negative**, i.e. price fell
   while the flow axis improved. Both are measured; neither is argued away.
3. 🚨 **`S77`'s threshold sits inside its own basket's implied move — it is LOW-INFORMATION as a band.**
   D2 straddles (expiry 2026-08-21, read this run): `NUE` **±1.8%** · `LIN` **±1.7%** · `STLD` **±3.2%** ·
   `FCX` **±5.5%** · `CRH` **±6.9%** ⇒ average of the five **±3.82%**. Haircutting for an 11-name EW
   basket at the measured mean pairwise correlation (§6, 0.193) gives ≈ **±2.2% over 2 days**, ≈ **±3.4%
   scaled to 5 sessions. `S77`'s ±2.03/±2.04 band is INSIDE that.** ⚠ Only 5 of 11 legs were priced and
   the scaling is an estimate, so this is a **partial** check — but it is the same class of finding
   `BLINDSPOT §6` recorded for `S96`, `P70`/`P75` and `S98`, and it belongs on the same list.
   ★ **The realised −3.231 sits at the outer edge of that estimated implied move, which is the reason it
   is readable at all. The threshold is not.**

### 0h · Verdict table

| claim | status | the measurement that decides it |
|---|---|---|
| **`S77` is the sector** | ✅ **HELD** | −3.231 reproduced; β-adjusted −3.307 (worse); survives every leave-out in §0d |
| **The `Copper` COT is the sector** | ❌ **REJECTED** | ex-`FCX` moves the observable **0.007pp**; needs `HG=F` **+49%** to reach branch A |
| **The COT is a live risk on `FCX`** | ✅ **HELD** | β +1.177 pp per 1% `HG=F`, r **+0.663**, 120 sessions, measured this run |
| **Branch B means Materials is deteriorating** | ❌ **NOT SUPPORTED** | same 11 names **+0.637 vs `SPY` over 60 sessions**; sector `delta` **+0.052** |
| **Branch B means the underweight is not a `NEM` artifact** | ✅ **HELD — and this is the whole content of the settle** | `NEM`'s own 5-session excess vs `SPY` is **−0.646**; it is not carrying either side any more |

---

## §1 · FULL FRESH VALUE-CHAIN MAP — eight nodes, each with its BINDING CONSTRAINT

**Binding constraint = the thing that caps throughput. Strong demand is never listed as one**; where
demand is strong it is recorded as *not* the constraint.

```
[1] INPUTS                [2] EXTRACTION          [3] SMELT / REFINE       [4] PRIMARY CONVERSION
    power · natgas ·   →     NEM (gold)        →    concentrate → metal  →    NUE STLD (EAF steel)
    scrap · air              FCX (copper)           ★★★ BINDING              LIN APD (ASU / SMR gases)
         ↓                        ↓                       ↓                        ↓
[5] FORMULATION           [6] AGGREGATES          [7] FABRICATION          [8] END DEMAND
    SHW (coatings)     →     CRH VMC MLM       →    service centers   →      data centres · fabs ·
    ECL (hygiene)            cement/aggregate       fabricators              nonres construction ·
    CTVA (ag chem)                                  (RS — see note)          refining · food · farms
```

| # | node | names in the scored universe (cap · % of sector) | **BINDING CONSTRAINT** | node EW 5-session excess vs `SPY`, settled 08-18 |
|---|---|---|---|---|
| 1 | **Inputs** | *(none scored)* | **Cost, not capacity — and it is loosening.** `NG=F` quarterly-average rate −14.1% → −15.3% → −2.5%p; `CL=F` +22.9% → +27.6% → −14.0%p (§2). An input whose rate has turned negative does not bind | n/a |
| 2 | **Extraction** | `NEM` $110.8B (11.6%) · `FCX` $98.7B (10.3%) | **Ore grade and mine availability.** Dated this run: *"Lundin Mining cuts copper outlook as Chile storms strike again"* (3 outlets, 2026-08-19) — a guidance cut, i.e. supply removed | `NEM` **−0.646** · `FCX` **−3.299** — 2.65pp apart |
| 3 | **Smelt / refine** | *(no `us_top300` expression)* | ★★★ **STILL THE SECTOR'S BINDING NODE AND STILL UNPRICEABLE HERE.** But this run re-diagnosed *why*: it is a **cap threshold, not an absence of listed companies** — see the note below | **not measurable** |
| 4 | **Primary conversion** | `LIN` $236.8B (24.7%) · `APD` $62.4B (6.5%) · `NUE` $55.5B (5.8%) · `STLD` $36.0B (3.8%) | **Steel: the index-linked contract repricing LAG** (§3b). **Gases: on-site plant capital under a 15–20-year contractual ceiling covering ~half of `APD`'s total sales** (§3a) — in neither case is it demand | gases **−1.784** · steel **−3.655** — **1.87pp apart inside one node** |
| 5 | **Formulation** | `SHW` $79.1B (8.3%) · `ECL` $75.7B (7.9%) · `CTVA` $52.6B (5.5%) | `SHW`/`ECL` **`unknown` (C3)** — not established from filings this run. `CTVA`: the binding item is the **northern-hemisphere season**, which its own revenue rate shows as a ±50pp swing (§2c) | `SHW` −4.851 · `ECL` −1.223 · `CTVA` **+2.621** |
| 6 | **Aggregates** | `CRH` $74.3B (7.8%) · `VMC` $39.3B (4.1%) · `MLM` $36.6B (3.8%) | **Not customer spend** (§5 — the disclosed spend is rising). Constraint **`unknown` (C3)**; what *is* established is that all three sit at or near the top of their own recorded margin range with a falling estimate denominator (§4) | **−5.970 — the worst node, and the basket's largest single drag** |
| 7 | **Fabrication / distribution** | *(none scored)* | Per `NUE`'s 10-K this node is the steel-mills segment's **direct customer**, so its absence is a hole in the demand read, not a curiosity | **not measurable** |
| 8 | **End demand** | *(customers — §5)* | ★ **Demand is NOT the binding constraint at any node measured.** Every disclosed customer capex series in §5 that matters is flat-to-rising | n/a |

### 1a · ★ The "not in universe" nodes are a **cap-threshold artifact**, and that is new this run

`data/us_universe/us_top300.csv` carries **12** Materials names. `data/us_universe/us_all_v2_candidate.csv`
carries **77**. The 65 excluded include **`RS` (steel service centers — node 7's direct expression)**,
**`AA` (aluminium)**, **`CLF` (integrated steel)**, **`ALB` (lithium)**, **`CF`/`MOS` (fertilizer)**,
**`DOW`/`LYB`/`DD`/`EMN`/`PPG` (chemicals)**, **`IP`/`PKG`/`AMCR`/`SW` (packaging)**.

> ⇒ The 08-13 map recorded nodes 3 and 7 as *"not in universe"*. That was right about the scored universe
> and wrong about the market. **The listed expressions exist; the desk's own $10bn-class cap cut removes
> them.** This is `N.유니버스부재` **by construction**, and it is a repairable gap rather than a
> structural one. It also means **"Materials" as this desk scores it is 12 names covering one-sixth of the
> listed sector's name count** — a fact that belongs next to every sector-level statement below.

⚠ **Cap-weight vintage conflict, found this run (G5).** `SECTOR_FLOW_US.json` (`asof` 08-18) and
`us_top300.csv` disagree on the same companies' market caps — e.g. `NUE` **$55.53B vs $62.09B**, `LIN`
**$236.79B vs $225.87B**, `SHW` **$79.12B vs $89.75B**. The percentages above use the JSON. **They are
descriptive only; no sign in this file rests on a cap weight.**

---

## §2 · ★★★ QoQ RATE-OF-CHANGE SERIES — every commodity node

**Price-cycle rule, obeyed: the LEVEL is the distraction; two consecutive declines in the RATE is the
signal.** Quarterly average of settled daily closes (`yfinance`, `auto_adjust=False`), then the QoQ % change
of that average. ⚠ **The 2026-09-30 bucket is a PARTIAL quarter (2026-07-01 → 2026-08-18), marked `p`. It
is shown and it is never counted as a completed decline.**

### 2a · Traded nodes

| quarter | **Copper** `HG=F` | rate | **Gold** `GC=F` | rate | **Steel** `HRC=F` | rate | **Lithium** `LIT`† | rate | *Oil* `CL=F` | rate | *NatGas* `NG=F` | rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2024-12 | 4.23 | +0.0% | 2661.8 | +7.6% | 697.4 | +2.0% | 44.09 | +15.7% | 70.32 | −6.6% | 2.98 | +33.5% |
| 2025-03 | 4.57 | +8.1% | 2867.9 | +7.7% | 805.4 | +15.5% | 41.00 | −7.0% | 71.42 | +1.6% | 3.87 | +30.1% |
| 2025-06 | 4.72 | +3.2% | 3279.8 | +14.4% | 895.8 | +11.2% | 36.92 | −9.9% | 63.68 | −10.8% | 3.51 | −9.4% |
| 2025-09 | 4.84 | +2.7% | 3461.8 | +5.5% | 838.8 | −6.4% | 45.97 | +24.5% | 64.99 | +2.1% | 3.08 | −12.3% |
| 2025-12 | 5.15 | +6.3% | 4147.3 | **+19.8%** | 860.1 | +2.5% | 61.63 | **+34.0%** | 59.14 | −9.0% | 4.04 | +31.4% |
| 2026-03 | 5.79 | **+12.5%** | 4863.4 | +17.3% | 984.4 | **+14.5%** | 71.58 | +16.2% | 72.67 | +22.9% | 3.47 | −14.1% |
| 2026-06 | 6.16 | **+6.4%** ▼1 | 4514.0 | **−7.2%** ▼2 | 1088.9 | **+10.6%** ▼1 | 82.74 | **+15.6%** ▼1 | 92.70 | +27.6% | 2.94 | −15.3% ▼2 |
| **2026-09p** | **6.39** ← series high | **+3.7%** ▼2p | 4151.9 | **−8.0%** ▼3p | **1172.7** ← series high | **+7.7%** ▼2p | 71.75 | **−13.3%** ▼2p | 79.75 | −14.0% | 2.87 | −2.5% |

† ⚠ **`LIT` is an equity ETF, not a lithium price.** No lithium spot or futures series is reachable in this
toolchain, and **`ALB`, the sector's listed lithium expression, is outside the scored universe (§1a)**. The
row is labelled as a proxy and is not treated as a commodity print. **The traded lithium rate is `unknown` (C3).**

### 2b · What the rate says that the level hides

| node | two consecutive declines on **completed** quarters? | read, with the level stated so it can be dismissed explicitly |
|---|---|---|
| **GOLD** | ✅ **YES — fully qualified** (+19.8 → +17.3 → **−7.2**), and the rate is **negative**, extending to −8.0%p | Fired on 08-13 and **still fired**. The quarterly-average gold price is *falling* |
| **COPPER** | ⚠ **one complete (+12.5 → +6.4), second only on the partial** | **Level at a series high (6.39) · spec positioning at the 100th percentile · rate down 70% from its Q1 peak.** ★ **Level extreme + positioning extreme + decelerating rate is the same observation seen three ways, and only the rate is the desk's signal** |
| **STEEL (HRC)** | ⚠ **one complete (+14.5 → +10.6), second only on the partial** | **Level at a series high (1,172.7 quarterly avg; 1,196.0 at the 08-18 settle, +3.64% over 20 sessions).** ★ This is the number §7 turns on: the LEVEL feeds `NUE`'s contracted book, the RATE feeds its estimates |
| **LITHIUM (proxy)** | ⚠ one complete (+16.2 → +15.6), second only on the partial — **and the partial is negative (−13.3%)** | Proxy only (C3). Flagged because the *shape* matches copper and steel and the desk holds no expression of it |
| **OIL / NATGAS (inputs)** | oil: rate turned **−14.0%p**; natgas: ✅ two complete declines (−14.1 → −15.3) | **Input costs are loosening at both gas-fed nodes** — relevant to `LIN`/`APD` (SMR feedstock) and to `NUE`/`STLD` (EAF power) |

> ### ⇒ Three of the five commodity nodes carry the SAME shape: level at a series high, rate in its second decline. Not one of them is a *level* story, and the sector's price is trading the level.

### 2c · The nodes with no traded price — revenue rate instead

Quarterly Total Revenue, QoQ rate (`yfinance` `quarterly_income_stmt`, oldest → newest).
⚠ **`NUE` and `CTVA`'s 2026-06 quarters are absent from this source** even though both companies have
reported — the source's latest is 2026-03. Their most recent rate is **`unknown` (C3)**, not flat.
⚠ **`CRH`/`VMC`/`MLM`/`SHW` are strongly seasonal** (Q1 trough, Q2 peak); their QoQ revenue rate is a
season, not a cycle, and is **not** read as a rate-of-change signal. It is shown so the seasonality is
visible rather than smuggled.

| node | name | QoQ revenue rate (5 quarters) | amplitude | two consecutive declines? |
|---|---|---|---|---|
| **Gases** | **`LIN`** | +1.4% → +1.7% → +0.2% → **+5.8%** | **5.6pp** | ❌ no — re-accelerating |
| **Gases** | **`APD`** | +4.8% → −2.0% → +2.2% → **−0.3%** | **6.8pp** | ❌ no — choppy inside a narrow band |
| **Copper** | **`FCX`** | −8.0% → −19.2% → +10.7% → **+12.8%** | **32.0pp** | ❌ **opposite — two consecutive RISES** |
| **Gold** | `NEM` | +3.9% → +23.4% → +7.2% → **−16.3%** | 39.7pp | ✅ **yes, ending negative** |
| **Steel** | `STLD` | +5.8% → −8.6% → +17.9% → **+17.0%** | 26.5pp | ❌ no |
| **Steel** | `NUE` | +8.0% → +0.8% → −9.8% → +23.5% → **`unknown`** | 33.3pp | ❌ no (latest quarter unavailable) |
| **Coatings** | `SHW` | +0.7% → −12.0% → +1.3% → +19.8% | seasonal | *not read* |
| **Hygiene** | `ECL` | +3.5% → +0.7% → −3.1% → +8.6% | 11.7pp | ❌ no |
| **Ag-chem** | `CTVA` | +46.2% → −59.4% → +49.4% → +25.4% → **`unknown`** | seasonal | *not read* |
| **Aggregates** | `CRH` · `VMC` · `MLM` | +46.2% · +22.8% · +43.0% latest | seasonal | *not read* |

★ **The gases/commodity amplitude gap reproduces and is the §3 frame-transfer measurement**: `LIN` **5.6pp**
and `APD` **6.8pp** against `FCX` **32.0pp** — **the two contracted names' revenue rate moves in a band
roughly one-fifth as wide as the one commodity-priced name.**

---

## §3 · CONTRACT TERMS read from the filings — and the FRAME-TRANSFER QUESTION, answered

🚨 **Rule obeyed (C3): no margin is claimed to mean-revert anywhere in this file without the terms, and
where the contracted share is not disclosed it is marked `unknown`.**

### 3a · ★★★ FRAME-TRANSFER: does take-or-pay / RPO lock-in apply to any Materials node?

> **Q: take-or-pay and RPO lock-in are load-bearing elsewhere on this desk. Does the frame transfer to
> Materials — and if it does, how much revenue does it actually lock?**

**A: it transfers to exactly one node — industrial gases — and this run finally put a NUMBER on it, on
one of the two names. The RPO half of the frame does NOT transfer at all.**

**`APD`** — `python -X utf8 -m module_business_us APD --json` → **10-K, filed 2025-11-20, period
2025-09-30** (`0000002969-25-000055`). Quoted from Item 1:

> *"These sale of gas arrangements are generally governed by long-term contracts ranging from 15- to
> 20-years. We also deliver smaller quantities of product through small on-site plants (cryogenic or
> non-cryogenic generators), generally under 10- to 15-year contracts. Contracts in this supply mode
> commonly include fixed monthly charges and/or minimum purchase requirements with price escalation
> provisions that are typically based on external indices. **Our on-site supply mode generates
> approximately half our total company sales.**"*

and on the cost side:

> *"We mitigate electricity, natural gas, and hydrocarbon price fluctuations contractually through pricing
> formulas, surcharges, cost pass-through provisions, and tolling arrangements."*

★ **This resolves the `unknown` the 08-13 file had to carry.** **Approximately half of `APD`'s total
company sales sit under 15–20-year contracts carrying fixed monthly charges and/or minimum purchase
requirements with index-linked escalation.** ⚠ **Precision (D1/D2): the literal phrase "take-or-pay" does
not appear in the filing** — `grep` returns **0 hits** for both "take-or-pay" and "take or pay". The
*mechanism* is present and quantified; the *term* is absent, and it is reported that way.

**`LIN`** — `module_business_us LIN --json` → **10-K, filed 2026-02-25, period 2025-12-31**
(`0001628280-26-011430`):

> *"On-site product supply contracts generally are total requirement contracts with terms typically ranging
> from 10-20 years and containing minimum purchase requirements and price escalation provisions."*

⚠ **`LIN`'s on-site share of total revenue is NOT disclosed in the sections read ⇒ `unknown` (C3)**, for
the second consecutive run. "take-or-pay": **0 hits.**

★ **The RPO half of the frame fails, and the reason is specific.** `LIN`'s MD&A discloses *"Linde's sale of
gas backlog of large projects under construction was approximately **$7.3 billion**"* at 2025-12-31 — and
the same sentence defines it: *"This represents the total estimated **capital cost** of large plants under
construction."* **That is a capex figure, not contracted future revenue.** "Remaining performance
obligation": **0 hits in `LIN`; 0 hits and no backlog disclosure at all in `APD`.**

> ⇒ **Take-or-pay transfers to Materials in substance and, at `APD`, in size (~half of total sales).
> RPO/backlog-as-locked-revenue does NOT transfer — the one number that looks like it ($7.3bn) is a
> capital cost. Any "locked revenue" framing imported from the energy or software books would be wrong
> here, and this is the measurement that says so.**

★ **And the frame has a price consequence that is visible in `S77` itself**: the two contractually
insulated names are **`APD` −1.562** and **`LIN` −2.006** excess vs `SPY` — **ranks 3 and 4 of 11 from the
top, i.e. the two least-punished names after `CTVA` and `ECL`**, in a window where the basket EW is −3.231.
⚠ Stated as an association measured this run on n=2, **not** as a proven mechanism.

### 3b · `NUE` — the contracts are a LAG, not a ceiling (re-verified, and the 08-13 prediction is broken)

`module_business_us NUE --json` → **10-K, filed 2026-02-25, period 2025-12-31** (`0001193125-26-071575`):

> *"We estimate that approximately 85% of our sheet steel sales in 2025 were to contract customers. These
> sheet sales contracts are noncancellable agreements that generally incorporate monthly or quarterly price
> adjustments reflecting changes in the current market-based indices and/or raw material cost, and typically
> have terms ranging from six to 12 months."*

⚠ **Scope (C3): 85% is of SHEET sales only.** Steel mills is 62% of sales to external customers (same
10-K). **The contracted share of `NUE`'s TOTAL revenue is `unknown` (C3).**

**A terms-grounded lead/lag claim, and the price-based half of it was MEASURED this run rather than assumed.**
Regressing daily excess vs `SPY` on the commodity's daily %, **120 settled sessions to 2026-08-18**:

| pair | β (pp per 1%) | **r** | read |
|---|---|---|---|
| `FCX` ~ `HG=F` | **+1.177** | **+0.663** | the copper equity **is** a daily expression of copper |
| `NEM` ~ `GC=F` | **+1.131** | **+0.687** | the gold equity **is** a daily expression of gold |
| **`NUE` ~ `HRC=F`** | **−0.018** | **−0.007** | ★ **no daily relationship at all** |
| **`STLD` ~ `HRC=F`** | +0.080 | +0.029 | ★ **no daily relationship at all** |

⚠ **Clock caveat, stated rather than exploited**: pairing `NUE`'s close-to-close excess vs `SPY` with the
**next** `HRC=F` print raises the correlation to **+0.310** (`STLD` +0.162). `HRC=F` settles at 13:30 ET and
the equity closes at 16:00 ET, so **this is a settlement-clock offset, not evidence that the equity leads
steel**, and it is reported as an offset.

> ⇒ **Even after the clock correction, the steel equities' link to the steel price (+0.31 / +0.16) is less
> than half the copper and gold equities' link to theirs (+0.66 / +0.69).** That is exactly what the terms
> predict: `FCX`/`NEM` sell at spot, `NUE` sells **~85% of sheet on monthly-or-quarterly index resets**, so
> its transmission is **quarterly, not daily.**

🚨 **The 08-13 prediction built on those terms is FALSIFIED at the 7-day margin, and it is left standing
with what broke it (§10).** That file predicted continued deterioration in `NUE`'s revision breadth as
`HRC`'s rate decelerated, citing **0↑/1↓ over 7 days**. Today the same field reads **11↑ / 0↓ over 7 days**,
with the current-year consensus moving **16.99 → 18.80 (+10.6%) in seven days.** The rate did decelerate;
the denominator went the other way — **because the LEVEL, not the rate, is what reprices into a
monthly-index contract, and the level is at a series high.**

---

## §4 · ★★★ PEAK-MARGIN + ESTIMATE-REVISION TABLE — every "cheap" claim carries both axes

**Rule obeyed**: no "cheap on forward multiple" statement appears without (i) where gross margin sits in
**that name's own history** (`scripts/margin_history.py <TK>`, SEC XBRL) and (ii) the **estimate-revision
trend** — which is a **description of the direction the denominator is moving, and is never used as a
leading indicator.** Forward P/E is `[live 2026-08-19, INTRADAY quote — labelled, and no price claim in
this file rests on it]`. Estimate fields: `yfinance` `eps_trend` / `eps_revisions`, read this run.

| name | fwd P/E | FY2025 gross margin | **position in its OWN history** (record length) | current-yr consensus, 90d | breadth, last 7d | **verdict on "cheap"** |
|---|---|---|---|---|---|---|
| **`NUE`** | **14.25** | **11.9%** | ★ **exactly its 19-yr median 11.9%** (FY2007–2025; max 30.2 FY2021, min 1.4 FY2009) | **14.62 → 18.80 = +28.6%** | ★ **11↑ / 0↓** | ★★★ **The one name where "cheap" is contradicted by neither axis** — median margin, not peak; denominator rising hard and broadly |
| **`STLD`** | **13.22** — the sector's lowest | **13.2%** | **BELOW its median 14.8%** (FY2007–2025; max 29.1 FY2021, min 9.6 FY2015) | 15.11 → 16.76 = **+11.0%** | **8↑ / 4↓** | ★★ **Below-median margin + rising denominator + the lowest multiple in the sector.** The cleanest pass of the peak-margin test here — and its 5-session excess vs `SPY` is **−4.860**, the 3rd worst in the basket |
| **`FCX`** | 16.45 | **26.1%** | **BELOW its median 28.9%** (15-yr; max 47.7 FY2011, min −87.7 FY2015) | 2.62 → 3.00 = **+14.6%** | **13↑ / 1↓** on the year — but **2↑ / 5↓ on the current quarter** | Below-median margin, rising full-year denominator, **near-quarter being cut.** "Cheap" is not contradicted by the margin axis; the near-quarter split is stated rather than averaged away |
| **`CRH`** | **14.30** | **36.1%** | 🚨 **the HIGHEST in its record — but the record is only 5 years (FY2021–2025)**, median 34.2% | 5.95 → 5.87 = **−1.2%** | **2↑ / 3↓**; next-yr **3↑ / 7↓** | 🚨 ★★★ **The textbook trap the peak-margin rule exists to catch**: the second-lowest multiple in the sector sitting on the top of its own (short) margin record with a falling denominator — **and the sector's worst 5-session excess vs `SPY`, −7.534.** ⚠ **No mean-reversion claim is made**: `CRH`'s contract terms were not read this run, so the **contracted share is `unknown` (C3)** |
| **`MLM`** | 24.74 | **30.7%** | 🚨 **the HIGHEST of an 18-year record** (FY2008–2025), median 23.1% | 19.32 → 18.40 = **−4.8%**; next-yr **23.02 → 21.52 = −6.5%** | 🚨 **2↑ / 10↓**; next-yr **2↑ / 14↓ — the sector's worst** | 🚨 **Peak margin on a long record + the sector's most negative revision breadth + a 24.7× multiple. No "cheap" claim is available and none is made.** ⚠ Contracted share **`unknown` (C3)** ⇒ no mean-reversion claim |
| **`CTVA`** | 19.19 | **47.3%** | 🚨 **the HIGHEST of its 8-year record** — which is its entire public life (FY2018–2025), median 41.1% | 3.73 → 3.76 = **+1.0%** | current-quarter **2↑ / 12↓** | 🚨 ★ **The ONLY positive name in `S77` (+2.621 vs `SPY`) is at the top of its own margin history with its near quarter being cut 12-to-2.** The single name holding branch B off 11-of-11 is the one carrying this configuration |
| **`SHW`** | 26.04 | **48.8%** | **near its own max 49.9% (FY2016)**, median 45.0% | 11.74 → 12.09 = **+3.0%** | ★ **21↑ / 0↓** — the sector's cleanest | **Peak-area margin BUT a uniformly rising denominator.** The two axes disagree, and neither is suppressed; no "cheap" claim at 26.0× regardless |
| **`VMC`** | 25.60 | **27.4%** | near its own max 28.6% (FY2007), median 25.0% | 9.23 → 9.15 = −0.9% | **9↑ / 3↓** | No "cheap" claim available at 25.6× |
| **`APD`** | 21.10 | **31.4%** | **above** its median 28.5% (max 33.9 FY2020, min 26.0 FY2014) | 13.17 → 13.44 = +2.1% | **2↑ / 0↓** (30d: **19↑ / 0↓**) | Above-median margin, rising denominator, **no cuts at all in 30 days.** No "cheap" claim made |
| **`ECL`** | **30.14** — the sector's highest | **44.5%** | ★ **exactly its median 44.5%** (max 50.8 FY2007, min 37.8 FY2022) | 8.44 → 8.17 = **−3.1%** | 2↑ / 1↓ | Median margin, falling denominator, highest multiple. ⚠ **And it holds the sector's best two-session flow `delta`, +0.628 (rank 5 of 299)** — the sharpest instrument disagreement in the sector |
| **`LIN`** | 24.63 | ⚠ **`margin_history.py` returns *"연간 데이터 없음"* — the XBRL gross-margin tag does not resolve. TOOLING GAP, `unknown` (C3), for the second consecutive run** | `unknown` | ⚠ current-yr field reads **0.00 — the "−100%" it produces is an ARTIFACT and is not reported as a collapse.** ★ **Next-year IS measurable: 18.24 → 18.29 = +0.3%, flat** | next-yr **3↑ / 5↓** | **No "cheap" claim is possible** — the margin axis is unavailable. ★ *Improvement on 08-13*: the next-year field is usable, so the denominator direction is **flat**, not `unknown` |
| **`NEM`** | **11.77** — the sector's lowest | ⚠ **`unavailable`, same tooling gap (C3)** | `unknown` | **10.30 → 9.38 = −9.0%** | **1↑ / 1↓** (30d: **1↑ / 11↓**) | ★★ **NOT established as cheap, for the second consecutive run.** The lowest multiple in the sector is falling because the **denominator** is being cut, and the one axis that could tell "cheap" from "peak-earnings" is missing |

> ### ⇒ ★★★ The cross-tab that the sector label hides
>
> **Sort the eleven `S77` names by where their margin sits in their own history and the price ordering
> largely inverts.** The three names at or nearest the top of their own margin record — **`CRH` (5-yr
> high), `MLM` (18-yr high), `CTVA` (8-yr high)** — are the ones whose estimate denominators are being cut
> hardest, and two of them are the basket's worst prices vs `SPY` (`CRH` −7.534, `MLM` −5.170). The two at
> or below their own median — **`NUE` (median) and `STLD` (below median)** — carry the two lowest multiples
> **and** the two cleanest rising denominators, and are still down 2.45 and 4.86 vs `SPY` on the window.
> **`S77`'s −3.231 is therefore NOT a single fundamental statement. It is a peak-margin de-rate and a
> momentum give-back happening in the same five sessions.**

---

## §5 · THE NODES' CUSTOMERS — named from the filings, then their DISCLOSED spend

**Customers named from the filings, not from the theme.** `APD`'s 10-K: it serves *"refining, chemicals,
metals, electronics, manufacturing, medical, and food."* `LIN`'s 10-K: *"healthcare, chemicals and energy,
manufacturing, metals and mining, food and beverage, and electronics."* `NUE`'s 10-K: the steel mills
segment *"sells its products primarily to steel service centers, fabricators and manufacturers"*, with end
markets *"tied to … nonresidential construction, durable goods and capital spending."*
⚠ **`FCX` and `NEM` customer disclosure remains `unknown` (C3)** — not established this run.

Spend is read from the customers' **own disclosed quarterly capital expenditure**, as a QoQ rate (§2's
discipline), with the **period end** and the **next print date** stated so nothing is asserted past the data.

| node served | customer | disclosed capex QoQ (4 most recent reported quarters) | latest period | **next print** | read |
|---|---|---|---|---|---|
| **aggregates + steel** | **`MSFT`** | +14% → **+54%** → +3% → **+16%** | 2026-06-30 | **2026-10-28** | ★ accelerating |
| | **`AMZN`** | +29% → +9% → +13% → **+12%** | **2026-03-31** ⚠ | **2026-10-29** | ★ steady double-digit. ⚠ **The June quarter is NOT in the cash-flow source used** (latest 2026-03) although `AMZN` reported 2026-07-30 — instrument lag, named |
| **gases — electronics** | **`MU`** | +93% → −5% → +19% → **+23%** | 2026-05-31 | **2026-09-23** | ★ accelerating |
| | `INTC` | −32% → +44% → +4% → **−30%** | 2026-06-30 | — | choppy, no trend |
| **gases — chemicals** | `DOW` | −15% → +2% → −12% → **+26%** | 2026-06-30 | — | small base ($0.63B), choppy |
| | `LYB` | −24% → +10% → −40% → **+0%** | 2026-06-30 | — | ★ **$0.27B and flat — this customer is not spending** |
| **gases — refining** | `MPC` · `VLO` | +36 → +24 → −23 → **+31%** · +20 → +22 → −27 → **+44%** | 2026-06-30 | — | ★ **both accelerating** — a node the 08-13 map did not measure |
| **copper — wire / utility** | `NEE` | +20% → −10% → +44% → **−10%** | 2026-06-30 | **2026-10-27** | choppy, latest negative |
| | `ETN` | +33% → −10% → **+117%** → **−51%** | **2026-03-31** | **2026-11-03** | very lumpy on a $0.19B base; latest negative |
| **ag-chem** | `DE` (farm-capex proxy) | +3% → +30% → −50% → **+54%** | 2026-04-30 | — | lumpy; no trend established |

★ **Finding 1 — demand is not the binding constraint at any node measured.** Every node whose customers
could be measured shows flat-to-rising disclosed spend, and the two weakest equity nodes (aggregates
−5.970, coatings/hygiene −3.037 excess vs `SPY`) sit in front of the strongest customer series in the
table (`MSFT` +16%, `AMZN` +12%). **The market is not selling these names on their customers' budgets.**

★★ **Finding 2 — and it is the only customer-side point that touches the mandate.** **The copper node is
the ONE node in this table whose own listed customers are not accelerating** (`NEE` −10%, `ETN` −51% on the
latest disclosed quarter) — while copper positioning sits at the 100th percentile. ⚠ **Both series are
lumpy on small bases and neither is a trend**; this is offered as the absence of corroboration for the
crowded long, **not** as evidence against copper.

⚠ **Node 7 (`RS`, service centers) is `NUE`'s named direct customer and is outside the scored universe
(§1a)** — so the one customer `NUE`'s own filing names cannot be measured here at all.

---

## §6 · SUB-SECTOR DISPERSION — is "Materials" the right unit this run?

Equal-weight 5-session excess vs **`SPY`**, settled 2026-08-18, with each sub-sector's share of scored
sector cap (G5 vintage caveat, §1a):

| sub-sector | names | % of sector cap | **5-session excess vs `SPY`** | 20-session vs `SPY` | 60-session vs `SPY` |
|---|---|---|---|---|---|
| **Ag-chem** | `CTVA` | 5.5% | **+2.621** | −12.948 | −4.759 |
| **Gold** | `NEM` | 11.6% | −0.646 | **+22.835** | +3.732 |
| **Gases** | `LIN`,`APD` | **31.2%** | −1.784 | −4.013 | −4.562 |
| **Coatings / hygiene** | `SHW`,`ECL` | 16.2% | −3.037 | +4.638 | +8.438 |
| **Copper** | `FCX` | 10.3% | −3.299 | +3.448 | +3.106 |
| **Steel** | `NUE`,`STLD` | 9.6% | −3.655 | +7.570 | **+8.881** |
| **Aggregates** | `CRH`,`VMC`,`MLM` | 15.7% | **−5.970** | −6.839 | −5.619 |
| | | | **SPREAD (max − min) 8.591 pp** | 35.783 pp | 14.643 pp |
| | **`XLB`, the "sector move"** | | **−2.339 pp** | +0.791 | +0.189 |

> ### ⇒ **The dispersion is 3.7× the sector move. "Materials" is still the wrong unit — but it is TEN TIMES less wrong than it was on 2026-08-13 (36.5×), and that change is itself the finding.**

**And the compression is in the returns only, not in the structure.** Pairwise correlation of the seven
sub-sectors' **daily excess-vs-`SPY`** series, trailing 60 settled sessions:

| | gold | copper | steel | gases | coat/hyg | aggreg | ag |
|---|---|---|---|---|---|---|---|
| **gold** | 1.00 | **0.68** | 0.10 | 0.00 | −0.10 | 0.15 | −0.06 |
| **copper** | **0.68** | 1.00 | 0.22 | −0.15 | **−0.25** | 0.00 | −0.11 |
| **steel** | 0.10 | 0.22 | 1.00 | 0.08 | 0.31 | 0.36 | 0.15 |
| **gases** | 0.00 | −0.15 | 0.08 | 1.00 | 0.44 | 0.30 | **0.59** |
| **coat/hyg** | −0.10 | **−0.25** | 0.31 | 0.44 | 1.00 | **0.69** | 0.38 |
| **aggreg** | 0.15 | 0.00 | 0.36 | 0.30 | **0.69** | 1.00 | 0.24 |
| **ag** | −0.06 | −0.11 | 0.15 | **0.59** | 0.38 | 0.24 | 1.00 |

**Mean off-diagonal 0.193** (max +0.69, min −0.25) — against **0.202** measured on 2026-08-13. **The
co-movement structure did not change at all.** Correlation with `DX-Y.NYB`'s daily return over the same 60
sessions: **gold −0.496 · copper −0.344 · ag +0.179 · gases +0.201 · aggregates +0.132 · coat/hyg +0.080 ·
steel −0.031** — the same two-object split the 08-13 file found, reproduced independently:
**(i) a dollar-priced metals complex** (gold–copper +0.68 to each other, −0.50/−0.34 to the dollar) and
**(ii) a domestic-industrial complex** (gases, coatings, aggregates, ag: +0.24 to +0.69 among themselves,
±0.20 to the dollar), with **steel straddling both**.

★★★ **This is what makes tonight's settle worth more than a sector print, and it is the deepest point in
the file.** The eleven names went 10-of-11 negative **while sharing almost no common factor** (mean
pairwise 0.193). Counting sub-sectors instead of names, **6 of 7 are negative.** Deflating for the measured
correlation, the effective number of independent observations in the basket is **n_eff = 7 / (1 + 6×0.193)
≈ 3.2**.

> ⇒ **`S77`'s branch B is neither one observation (which a single-factor sector move would be) nor eleven
> (which the raw name count implies). It is about THREE quasi-independent observations pointing the same
> way.** That is a real but modest evidential weight — and it is exactly the honesty the mandate's
> "NEM-free confirmation" framing needs, because a `NEM`-free basket that co-moves at 0.19 cannot be
> claimed as eleven witnesses.

★ **One more instrument note the sector label hides.** `SECTOR_FLOW_US.json` shows **0 🟢 of 12** for
Materials — and **`SWEEP_READ §3`'s artifact table does not carry a Materials row.** Computed here:
**5 of 12 names pass `OBV 매집 ∧ RS20>0` vs `SPY`** (`NEM` RS20 +22.8 · `NUE` +10.7 · `SHW` +5.9 · `STLD`
+4.4 · `ECL` +3.4, each paired with an accumulating OBV state — D6), and **0 of those 5 clear `vol_surge`
1.2; the sector's maximum `vol_surge` is 0.99 (`ECL`).**
⇒ **Materials is the SIXTH replication of the volume-gate artifact in this run's own data, and it was not
listed. Its `0 🟢` may not be cited as sector weakness**, exactly as `SWEEP` ruled for Energy and Health Care.
⚠ **And the same decay signature the 08-13 file identified reproduces on different names**: of the 5 that
pass the 20-day accumulation screen, the 4 inside `S77` are **all negative** on the 5-session excess vs
`SPY` (`NUE` −2.450 · `ECL` −1.223 · `SHW` −4.851 · `STLD` −4.860). **A 20-day screen is not a 5-day signal.**

---

## §7 · `NUE` — the book holding, and EVENT_ALPHA Card 4's driver question, RESOLVED BY DATING THE MOVE

**Card 4 asks whether `NUE`'s driver is mis-identified: a Canada tariff PAUSE should pressure domestic
steel, and `NUE` is accumulating instead. This run answers it by dating the move, which no prior run did.**

### 7a · The move is a post-earnings re-rate that PREDATES the tariff thread by twelve sessions

`NUE` cumulative excess vs **`SPY`**, self-computed to the 2026-08-18 settle:

| window | `NUE` excess vs `SPY` | `STLD` excess vs `SPY` | window starts |
|---|---|---|---|
| 2-session | **−0.61** | −1.19 | 2026-08-14 |
| 3-session | **−1.63** | −2.77 | 2026-08-13 ← **the tariff thread's first outlet** |
| 5-session (`S77`) | **−2.45** | −4.86 | 2026-08-11 |
| 10-session | **−3.09** | −5.26 | 2026-08-04 |
| **15-session** | **−4.13** | −7.41 | 2026-07-28 |
| **20-session** | ★ **+10.73** | +4.41 | 2026-07-21 |
| 30-session | +13.53 | +6.15 | 2026-07-07 |

★★★ **The entire RS20 of +10.7 vs `SPY` was earned in sessions 16–20 back — between 2026-07-22 and
2026-07-28 — and the single largest day is 2026-07-28 at +6.93pp excess vs `SPY`, the biggest single
session in forty.** `NUE` **reported after the close on 2026-07-27: EPS 4.84 against a 4.53 estimate, a
+6.94% surprise** (`yfinance` `earnings_dates`). The 2026-07-28 session is the print's reaction.

**EVENT_ALPHA Card 4's thread begins 2026-08-13** (*"U.S. says Canada among China's biggest enablers"*),
peaks 2026-08-19 on the pause.

> ⇒ **The steel bid was complete twelve sessions before the tariff thread's first outlet. The tariff cannot
> be its driver, and Card 4's suspicion is CONFIRMED — the driver was mis-identified.** Since the thread
> started, `NUE`'s excess vs `SPY` is **−1.63 (3 sessions) and −2.45 (5 sessions)**: the name has been
> *giving back*, not bidding, across the entire life of the tariff story.

🚨 **A KPI defect handed back to EVENT_ALPHA, not argued around.** Card 4's IF-branch reads *"at 2026-08-31,
`NUE` 10-day excess vs `SPY` ≤ 0 ⇒ the steel bid WAS the tariff, and it unwinds."* **That condition is
already satisfied at the 08-18 close: −3.091.** ⇒ **The KPI will fire the tariff branch for a reason that
has nothing to do with tariffs — post-earnings drift decay is indistinguishable from a tariff unwind under
this observable.** The card's binary cannot separate its own two hypotheses, and the dating above is what
separates them.

### 7b · The driver that survives the dating — level, not rate, transmitted by the contract terms

`HRC=F` settled **1,196.0** on 2026-08-18: **+3.64% over 20 sessions**, a series high on the quarterly
average (§2a), while its QoQ **rate** is in its second decline (+14.5 → +10.6 → +7.7p). Per §3b's terms,
**~85% of `NUE`'s sheet book reprices monthly-or-quarterly to market indices on six-to-twelve-month
contracts.** A record index level therefore keeps repricing *upward* into the book for one to two quarters
**regardless of what the rate is doing** — and the estimate axis is doing exactly that: current-year
consensus **14.62 → 16.88 → 18.80** across 90/30/current, **11↑ / 0↓ over the last 7 days.**

> ⇒ **`NUE`'s driver is the HRC LEVEL arriving through index-linked contracts, confirmed by a beat, and it
> is neither the tariff nor the HRC rate.** The rate is what bites later; the level is what is in the book
> now. **This is the price-cycle rule working in both directions on the same name.**

### 7c · The OBV question — and the instrument conflict `BLINDSPOT` flagged is most likely a CLOCK artifact

`BLINDSPOT §4b` reported that the sweep's `obv_state` and `module_chart --read`'s 20-day OBV slope **flip
sign on 5 of 22 names, `NUE` among them**, and ruled any tag resting on OBV alone unsafe for those five.
Reproduced here at ET 09:58: **`module_chart NUE --read` returns `OBV: 분배 (20d 기울기 −31%)`** against the
sweep's **`매집 +0.452`**.

**Resolved with settled bars only.** ⚠ **D1/D2: what follows is MY OWN reconstruction** (sign-of-close ×
volume, cumulative, 20-session change normalised by 20-day mean volume), **not** the desk's `obv_norm` — a
different object, labelled as one. Computed on closes through **2026-08-18** with no 08-19 bar:

| ticker | my 20-day OBV change (normalised) | sweep `obv_norm` | agree? |
|---|---|---|---|
| `NUE` | **+45.2%** | **+0.452** | ✅ |
| `STLD` +31.7% · `APD` +29.3% · `NEM` +24.1% · `SHW` +17.4% · `ECL` +14.4% · `VMC` +3.4% | — | +0.317 / +0.293 / +0.241 / +0.174 / +0.144 / +0.034 | ✅ all |
| `FCX` −2.0% · `CRH` −9.2% · `MLM` −11.0% · `LIN` −12.8% · `CTVA` −15.4% | — | −0.020 / −0.092 / −0.110 / −0.128 / −0.154 | ✅ all |

**12 of 12 agree in sign on settled bars.** The one instrument that disagrees is the one that was run
**with the 2026-08-19 US session open (ET 09:58)** and therefore carries an in-progress bar.
⇒ **The `NUE` OBV "flip" is best explained as a clock artifact, not an instrument disagreement**, and the
same explanation is available for the other four names on `BLINDSPOT`'s list. ⚠ **This does not promote OBV:
per D6 it stays grade C and carries nothing alone.** `NUE`'s accompanying momentum reading is **RS20 +10.7 /
RS60 +13.3 vs `SPY`** — and §7a has just shown that RS20 is a July object.

### 7d · Positioning on the two names the mandate names

⚠ Options and short-interest fields below are **live-quote objects read at ET ~10:00–10:25 with the session
open**; they are not settled prices and no settled claim rests on them.

| ticker | short % float | trend | DTC | implied move (expiry 2026-08-21, **D2**) | note |
|---|---|---|---|---|---|
| `NUE` | 2.1% | covering | 2.6 | **±1.8%** | the basket's tightest implied move |
| `FCX` | 2.0% | covering | 1.8 | **±5.5%** | the copper leg is priced for the widest move in the sector after `CRH` |
| `STLD` | **3.6%** | ★ **building — the only name in the sector where short interest is rising** | 3.4 | ±3.2% | ★ the sector's cheapest multiple, below-median margin and rising estimates (§4) is also the only one being shorted more. **Stated as a disagreement, unresolved** |
| `LIN` | 1.2% | covering | 2.6 | ±1.7% | |
| `CRH` | 2.4% | covering | 3.5 | **±6.9%** | the widest in the sector |

---

## §8 · NEWS — this file's own calls, with the clock, and two nulls that are reported as nulls (G1)

All items below come from **`module_news_data` calls made by this file at KST 2026-08-19 23:05–23:12
(ET 10:05–10:12)**. The sweep's `velocity` column is revoked (G1) and is **not** used.

**`chain-hop` returned nothing usable, and the reason is an instrument defect that is now reproducing:**

| call | articles scanned | headline-named | chain-hop candidates |
|---|---|---|---|
| `chain-hop "copper smelter" --days 7` | **0** | 0 | 0 |
| `chain-hop "steel tariff" --days 7` | **1** | 0 | 0 |

**Against the same corpus, in the same minutes, `search --days 7 --scope foreign` returns `copper` **114
hits** and `steel` **68 hits**.** ⇒ 🚨 **The `chain-hop` scanner and the FTS index disagree on the same
corpus, for the second consecutive Materials run** (first logged 2026-08-13: 0 scanned against 453 `copper`
hits). This is an instrument defect, **not** an absence of the theme, and **no Materials chain-hop candidate
is measurable this run.**

**What the FTS corpus does carry, dated 2026-08-19, direction read from each item's own full sentence:**

- 🚨 ★ **The copper tape is being told two opposite stories on the same day.**
  Supply removed: *"Lundin Mining cuts copper outlook as Chile storms strike again"* `[mining]` and
  *"Lundin Mining Lowers 2026 Copper Production Guidance After Chile Storms"* `[nasdaq]`, plus *"Copper
  prices run signals deeper supply squeeze: Sprott"* `[mining, body 11,349 chars]`.
  Supply restored: *"Copper: **LME stock jump eases supply squeeze** – ING"* `[fxstreet]` and *"Copper
  **Holds Loss** as Deliveries to LME Mitigate Supply Crunch"* `[bloomberg]`.
  ⇒ **The most extreme positioning reading on the board sits on a theme whose own day's news is two-sided,
  and whose price is −1.96% over 5 sessions and −0.44% over 20 (§0e).** No direction is inferred from the
  news; the two-sidedness is the observation.
- ✅ **`steel` returns 68 hits and effectively none is a US steel story** — the set is dominated by JSW
  Steel (India), a bank named Steele, and a Chinese launch vehicle's steel booster. ⇒ **The Canada tariff
  event does not surface as a *steel* story in this corpus at all; it surfaces as a trade story.**
  Consistent with §7a's dating, and reported as corroboration of an absence rather than as evidence.
- **`industrial gases` / aggregates**: no dated item this run. **Null, reported as null.**

---

## §9 · TRACK-KPIs AND ANTI-SIGNALS — dated observables, both branches

| # | observable | reads at settled 2026-08-18 | what it confirms / falsifies |
|---|---|---|---|
| 1 | ★★★ **`S77`** — EW 5-session excess vs `SPY` of the 11 non-`NEM` names, settles **tonight 2026-08-19** | **−3.231, 10 of 11 negative** (β-adjusted −3.307) | **Branch B by 1.19pp.** ⚠ **Its ±2.03/±2.04 band is inside the basket's estimated implied move (§0g.3) ⇒ the THRESHOLD is low-information; only the realised magnitude reads** |
| 2 | ★★ **`Copper` QoQ rate, 2nd COMPLETE decline** — Q3 2026 average, **prints 2026-10-01** | +12.5 → +6.4 (1 complete) → **+3.7%p** | A completed second decline fires the price-cycle signal **while the level sits at a series high and spec net at the 100th percentile** |
| 3 | ★★ **Steel HRC QoQ rate, 2nd COMPLETE decline** — Q3 2026, **prints 2026-10-01** | +14.5 → +10.6 (1 complete) → **+7.7%p** | Per §3b this reprices into ~85% of `NUE`'s **sheet** book within 1–2 quarters. **The LEVEL (1,196.0, +3.64% / 20 sessions) is what is in the book now** |
| 4 | ★★★ **`NUE` current-yr revision breadth** — the axis that broke the 08-13 prediction | **11↑ / 0↓ over 7 days**; consensus 16.99 → 18.80 (+10.6% in 7 days) | A turn back to net-down is the first evidence the rate has started to beat the level. **Next issuer datapoint: 2026-10-26** |
| 5 | 🚨 **`MLM` next-yr revision breadth** — the sector's worst | **2↑ / 14↓ over 7 days**, next-yr 23.02 → 21.52 (−6.5% / 90d) | On an 18-year-record gross margin (30.7%). If breadth turns up on a record margin, §4's peak-margin read on aggregates is wrong |
| 6 | 🚨 **`CTVA` current-quarter breadth** — the ONLY positive name in `S77` | **2↑ / 12↓ over 7 days** | The single name keeping branch B off 11-of-11 is being cut at the near quarter. If it turns, `S77`'s one positive leg has a fundamental basis; if not, it was a 5-day price event |
| 7 | ★ **`ECL` two-session flow `delta`** | **+0.628 — rank 5 of all 299 scored names**, against a 5-session excess vs `SPY` of −1.223 | The sharpest price-vs-flow disagreement in the sector. Resolution either way tests whether `delta` leads price at 2-session horizon |
| 8 | **`Copper` spec net COT**, next Tuesday snapshot | **+80,388 · +3,265 ▲ · 27.1% OI · 100th %ile** | ⚠ **It cannot rise in percentile by definition.** Any decline = the crowded long capping, against a decelerating rate. **Contrarian ammunition, not direction** |
| 9 | ★ **`USD Index` spec net COT** | **+21,409 · 80th %ile 🟢 crowded long** | ★ **Two crowded longs pointed at each other**: copper's excess vs `SPY` carries **−0.344** correlation to `DX-Y.NYB` (gold −0.496). Both cannot pay |
| 10 | **`Gold` spec net COT** | **+217,940 · 49th %ile — neutral** (was 29th on 08-13) | ★ Gold positioning is **not** crowded, so `NEM`'s risk stays an earnings-quality risk (revisions **1↑/11↓ over 30d**), not a positioning unwind |
| 11 | ★★ **The sector's issuer vacuum** | **All 12 names last reported 2026-07-20 → 2026-07-31. The next print is 2026-10-19 (`STLD`) and the last is 2026-11-05 (`APD`)** | ⇒ **There is no dated issuer catalyst in Materials for roughly nine weeks.** Anything that moves the sector before late October is commodity, macro or positioning — which is precisely the window in which a 100th-percentile spec position has no issuer news to be corrected by |
| 12 | **Customer capex next prints** | `MU` **2026-09-23** · `NEE` **2026-10-27** · `MSFT` **2026-10-28** · `AMZN` **2026-10-29** · `ETN` **2026-11-03** | **Demand is not the binding constraint (§1).** A QoQ rate turning negative at `MSFT` *or* `MU` would be the first evidence it might become one |
| 13 | **`STLD` short interest** | **3.6% of float, BUILDING, DTC 3.4** — the only name in the sector with rising short interest | Against the sector's lowest multiple, a below-median margin and 8↑/4↓ revisions. One of the two sides is wrong and the resolution is dated by #11 |
| 14 | 🚨 **`LIN` and `NEM` gross-margin tags** | **`margin_history.py` returns "연간 데이터 없음" on both, second consecutive run** | **31.2% of sector cap (gases) and the sector's lowest multiple (`NEM` 11.77×) cannot be tested against their own margin history.** A tooling gap, stated not skipped, and it is the largest single hole in §4 |
| 15 | **`chain-hop` vs FTS disagreement** | 0–1 articles scanned against 114/68 FTS hits, **2nd consecutive Materials run** | An instrument defect. Until it is fixed, **no Materials chain-hop null may be read as theme absence** |

### 9a · ★ Anti-signals against **this file's own** verdict — registered so §0 is falsifiable

1. **If `S77` settles branch A (≥ +2.03) tonight**, §0 is wrong on its central claim and the 08-18
   pre-settle reading was a one-session artifact — noting the observable would have to move **+5.26pp in a
   single session** to get there.
2. **If the 11-name EW 20-session excess vs `SPY` turns positive within 10 settled sessions** while
   `Copper`'s percentile stays ≥90, then branch B was a five-day give-back inside an intact uptrend and
   §0a's own hedge ("not deteriorating") should have been the headline rather than the qualifier.
3. **If `CRH`, `MLM` and `CTVA`'s revision breadth turns net-positive** while their gross margins stay at
   the top of their own records, §4's peak-margin cross-tab is describing noise and the aggregates drag has
   another cause.
4. **If `FCX`'s excess vs `SPY` decouples from `HG=F` (rolling 60-session r falls below +0.30)**, then
   §0e's arithmetic — which is what rejects the COT as the sector — loses its transmission coefficient and
   the rejection must be re-derived.
5. **If `NUE`'s 10-day excess vs `SPY` rises above 0 by 2026-08-31 with the pause in force**, EVENT_ALPHA
   Card 4 fires its ELSE branch and §7a's dating still holds — **but the card would then be right for a
   reason it did not state**, and that coincidence should be flagged rather than counted as a confirmation.

---

## §10 · ★ §4c — claims from the 2026-08-13 MATR file that THIS run breaks, left standing with what broke them

**Not edited away. Each is the prior run's claim, followed by this run's measurement.**

1. **08-13 claimed the accumulation window was "a 20-day trailing artifact that has ALREADY inverted."**
   ✅ **Reproduced on new names**: 5 of 12 pass `OBV 매집 ∧ RS20>0` vs `SPY`, and the 4 inside `S77` are all
   negative on the 5-session excess vs `SPY` (§6). **Held.**
2. **08-13 predicted `NUE`'s revision breadth would keep deteriorating** on the contract-lag mechanism,
   citing **0↑/1↓ over 7 days**. 🚨 **BROKEN.** It now reads **11↑ / 0↓ over 7 days** with the current-year
   consensus **+10.6% in seven days**. **The mechanism was right and the sign was wrong: index-linked
   contracts transmit the LEVEL, and the level is at a series high (§7b).**
3. **08-13 recorded nodes 3 and 7 as "not in universe."** ⚠ **CORRECTED**: they are not in the *scored*
   universe. `RS`, `AA`, `CLF`, `ALB`, `DOW`, `LYB`, `CF` and 58 others sit in the candidate file and are
   removed by the cap cut (§1a). **`N.유니버스부재` by construction, and repairable.**
4. **08-13 marked `LIN`'s on-site share `unknown` and left the gases node's contract size unquantified.**
   ✅ **PARTIALLY RESOLVED**: `APD`'s 10-K discloses **"approximately half our total company sales"** under
   15–20-year minimum-purchase contracts (§3a). **`LIN`'s share remains `unknown` (C3)**, and the RPO half of
   the frame is now positively **refuted** — `LIN`'s $7.3bn "backlog" is a capital cost, not contracted revenue.
5. **08-13's dispersion verdict was "36.5× the sector move ⇒ Materials is not a unit of analysis."**
   ⚠ **QUALIFIED**: the ratio is now **3.7×** — still >1, so the label is still the wrong unit, but the
   returns converged by an order of magnitude **while the correlation structure did not move at all**
   (mean off-diagonal 0.193 vs 0.202). **The convergence is in the outcome, not in the object.**

---

## ✅ EXIT CHECK

- [x] **The assigned mandate is answered explicitly in §0a and settled in §0h**: **`S77` is the sector; the
      `Copper` COT is one node's forward positioning**, rejected on a measured arithmetic reach (ex-`FCX`
      changes the observable **0.007pp**; branch A needs `HG=F` **+49%**), with the extreme treated as
      contrarian ammunition and **never as a direction**.
- [x] **ROTATING ⇒ full fresh map**: 8 nodes rebuilt with binding constraints (§1), the prior file read for
      continuity and its five claims adjudicated in §10 rather than repeated.
- [x] **G1 obeyed** — `velocity`, the 51 survivors and `breadth` are unused; every news item is from this
      file's own calls with the clock stated, and both `chain-hop` nulls are reported as instrument nulls.
- [x] **G2 obeyed** — terminal settled bar **2026-08-18**; no 08-19 price anywhere; every sweep `delta`
      described as **two sessions**; the intraday-instrument calls are fenced and their contamination is
      used only to *diagnose* (§7c), never to carry a claim.
- [x] 🚨 **G3 obeyed** — `wflow` carries no promote or demote; §0d shows why `S77` is structurally immune to
      the `LIN` flipper (equal weight; ex-`LIN` = −3.353, no sign flip); admissible axes named as
      `eqflow` −0.060, `delta` +0.052, per-name.
- [x] **Benchmark `SPY` named inline on every relative-performance number**, and β-adjusted figures carry
      their β and its 252-session window.
- [x] **Price-cycle rule** — §2 tabulates QoQ **rate** series for copper, gold, steel, lithium (proxy,
      labelled), oil and natgas; the partial quarter is marked `p` and never counted; the level is stated
      only to be dismissed explicitly.
- [x] **Peak-margin rule** — §4 gives every name its gross margin, **its position in its own history with
      the record length**, and its estimate-revision trend, **described only as the denominator's
      direction**. Two names (`LIN`, `NEM`) are marked `unknown` (C3) on a tooling gap rather than skipped.
- [x] 🚨 **C3 obeyed** — **no margin is claimed to mean-revert anywhere.** Where contract terms were read
      (`APD`, `LIN`, `NUE`) the terms are quoted with filing date and accession number; where they were not
      (`CRH`, `MLM`, `CTVA`, `SHW`, `ECL`, `VMC`) the contracted share is marked **`unknown`** and no
      mean-reversion claim is made about them.
- [x] **Frame-transfer question asked and answered with filings** (§3a): take-or-pay transfers to industrial
      gases and is **quantified at `APD` (~half of total sales)**; **RPO does not transfer**, and the
      $7.3bn that looks like it is a capital cost.
- [x] **Customers named from the filings and their disclosed spend measured**, each with its period end and
      **next print date** (§5); the one customer `NUE`'s filing names (`RS`) is flagged as unmeasurable.
- [x] **Every lead/lag claim measured this run** (§3b: 120-session betas and correlations, with the
      `HRC=F` settlement-clock offset disclosed) — **no lead/lag claim is carried as `[unverified]`.**
- [x] **Sub-sector dispersion stated** (§6): spread **8.591pp** vs an `XLB` sector move of **−2.339pp**
      ⇒ **3.7×, so the sector label is the wrong unit** — with the effective-independence deflation
      (n_eff ≈ 3.2) applied to `S77` so the "10 of 11" is not over-counted.
- [x] **`SWEEP_READ §3`'s missing Materials row computed here** (5 of 12 accumulate, 0 of 5 clear
      `vol_surge` 1.2, sector max 0.99) ⇒ the sector's `0 🟢` is a **volume-gate artifact** and is not
      cited as weakness.
- [x] **Both branches and dated horizons on every KPI** (§9), plus **five anti-signals against this file's
      own verdict** (§9a).
- [x] **`scripts/report_lint.py` run against this file** (rules `C1,C2,S6,D6`) — **0 findings, clean**.
      No rule ID is carried with an exemption reason because none was needed.
- [x] **No position sizing and no buy/sell language appears anywhere in this file (P4).**
