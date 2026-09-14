# SECTOR_DEEP_MATR — Materials · industry_US · 2026-09-01 (Tue) · Stage 8 / L1·DEEP
### CONTINUOUS TRACK (slot held from 2026-08-31) — **leads with the DELTA**, prior structure by reference

> ⚠ **Execution constraint declared** (standing, 7th run): the five DEEP sectors were written
> **in-context and serially**, not as a parallel agent fan-out.
> Flow numbers: `SECTOR_FLOW_US_REPAIRED.json`, 3-axis `nonews`, **asof 2026-08-31**. Benchmark `SPY`
> named inline (`C1`). The primary sweep's OBV axis is revoked.
> ⚠ Prices tagged **[live]** were read with the NYSE open and are partial bars.

## 0 · Mandate from ROTATION — one question
> *An OW with **0 greens of 12**, `eqflow` +0.030, `LIN` holding the headline **up** (ex-`LIN` +0.115),
> against **copper spec at the 100th percentile of its year**. **Early, or trap?***

## ★ 1 · The DELTA — and it answers the mandate

**Verdict: TRAP-SHAPED on the metals leg, and the evidence is the second derivative, not the level.**

### 1a. What changed since the 08-31 file
| | 08-31 (repaired) | **09-01 (repaired)** | delta |
|---|---:|---:|---:|
| `wflow` rank on the board | **1 of 11** | **2 of 11** | −1 |
| `eqflow` | **+0.164 (rank 1)** | **+0.030 (rank 3)** | ⚠ cross-file, see below |
| greens / reds of 12 | 0 / 0 | **0 / 2** | 2 reds appeared (`MLM`, `SHW`) |
| engine Δ (like-for-like) | — | **+0.120** | positive |

⚠ **`C5`/G2 honesty**: the `eqflow` fall from +0.164 to +0.030 is a comparison of **two separate
reconstructions** (08-28 vs 08-31 repaired frames) and PREFLIGHT G2 does not license it as a
subtraction. **The engine's own like-for-like Δ is +0.120, positive.** ROTATION declined the demotion
on exactly that ground, correctly. **The bear case below therefore does NOT rest on flow at all.**

### 1b. ★ The second derivative on the sector's best name — `NEM` (lens **B1**)
`NEM` is the bucket's #1 by flow (**+0.772**, rank **6 of 299** universe-wide), `rs20` **+30.9** and
`rs60` **+15.1 vs `SPY`**, OBV **+0.355 매집**. On price it is the strongest thing in Materials.

**Quarterly revenue, and the QoQ RATE beside the level** (`[yfinance]`, XBRL cross-checked 4/4 within
5%):

| quarter end | revenue $B | **QoQ rate** |
|---|---:|---:|
| 2025-06-30 | 5.32 | — |
| 2025-09-30 | 5.52 | **+3.8%** |
| 2025-12-31 | 6.82 | **+23.6%** |
| 2026-03-31 | 7.31 | **+7.2%** |
| **2026-06-30** | **6.12** | **−16.3%** |

★ **`M1199` [measured] — the rate decelerated twice and then the level fell.** +23.6% → +7.2% →
**−16.3%**. The desk's own rule is that **two consecutive declines in the rate is the signal and the
level is the distraction** — here the rate declined twice *and* the level has now followed.
**Both halves cited (`C2`)**: the same quarter is **+15.06% YoY**. A file quoting only the YoY would
read this as growth.

### 1c. Valuation, with the denominator's direction beside it (lens **B2**)
| | `NEM` | `LIN` |
|---|---|---|
| price **[live]** | $123.99 (52w 73.44–135.29) | $484.05 (52w 387.78–548.20) |
| Trailing / **Forward P/E** | 15.86 / **12.29** | 31.19 / **24.73** |
| PEG | 2.78 | 2.07 |
| target mean vs price | $132.87 = **+7.2%** | $547.24 = **+13.1%** |
| recommendations (30d) | 5 SB / 15 B / 2 H / 1 S | 5 SB / 16 B / 5 H / 1 S |

⚠ **`NEM`'s forward 12.29× is NOT "cheap" on this desk's rule** — a multiple without a margin
percentile is not a valuation, and the denominator here is a **gold-price-driven** earnings number
whose revenue rate has just turned negative (§1b). ⚠ **The margin percentile itself is `unknown` (`C3`)**
— `module_fundamentals_us` does not carry a gross-margin history and `scripts/margin_history.py`
**exits 1** (PREFLIGHT G7, KR-only tool). **Stated as unknown rather than asserted.**
★ And the **analyst target is only +7.2% above the price** — consensus has already arrived.

### 1d. The positioning half, which is where "trap" comes from
`[COT 08-25]` **Copper spec net +85,266 = the 100th percentile of its year**, +5,518 WoW, 30.1% of OI
— **the single most crowded reading on the entire positioning board.** Gold spec **66th %ile**.
`[FINRA 08-31]` `LIN` short-vol **43.0%, z +0.13** — no pressure either way.
`[news]` *"Nvidia just lined up $500 billion. Frank Holmes says the thing that's scarce isn't money,
it's copper"* [yahoo_finance, **1 outlet**, 08-31] — ⚠ single-source, used as a **frame**, not evidence.

⇒ **The story (copper is the AI bottleneck) is arriving at a position that is already maximally
held.** That is the LATE-MONEY shape, and it is why the mandate's answer is **trap-shaped** rather
than **early** — *for the metals leg*.

## 2 · Dispersion — the sector label is the wrong unit (lens **B5**)
Spread inside Materials on `flow_score`: **`NEM` +0.772 to `SHW` −0.744 = 1.516**, against a sector
`eqflow` of **+0.030**. **The intra-sector spread is 50× the sector's own reading.**

| sub-node | names | flow | read |
|---|---|---|---|
| **Precious/base metals** | `NEM` +0.772 · `FCX` +0.700 | **the only positive leg** | both OBV 매집, both `rs20` > +17 — **and both missed the 🟢 tag by 0.01–0.14 of `vol_surge`** |
| **Ag/industrial gases** | `CTVA` +0.606 (**Δ +0.98 = the largest positive Δ in the 299-name universe**) · `APD` +0.394 · `LIN` +0.246 | mid | `LIN`'s `rs60` is **−4.8 vs `SPY`** — the 24.7% top-1 is the sector's *drag*, not its engine |
| **Construction materials** | `VMC` −0.220 · `CRH` −0.282 · `MLM` −0.471 🔴 | **negative, uniformly** | three names, three negatives — a housing/infra read, not a metals read |
| **Steel** | `STLD` −0.426 · **`NUE` −0.482 (HELD)** | negative | `NUE` `rs60` **−6.1 vs `SPY`**, Δ **−0.452** |
| **Specialty chem** | `ECL` +0.263 · `SHW` −0.744 🔴 | split | |

★ **`M1200` [measured] — "Materials OW" is four different bets and only one of them is working.**
Metals positive, construction uniformly negative, steel negative, chemicals split. **The book's
Materials position is `NUE` — a steel name at −0.482 with Δ −0.452 — i.e. the desk owns the leg the
sector's own numbers rank second-worst.**

## 3 · Value chain — 6 nodes, left → right, bottleneck marked
`mine / concentrate` → **`smelt & refine`** → `semis & shapes` → `fabrication` → **`grid & datacenter
electricals`** → `end demand (construction · autos · AI buildout)`

- ⚠ **Binding constraint is NOT demand.** The corpus's own claim is that copper *supply* is the
  scarce input to the AI buildout. But the desk **cannot verify the smelting/refining node** —
  `module_industry_map` returns 0 for English seeds against a KR corpus (known, PREFLIGHT-adjacent),
  and no US smelter capacity series is wired. ⇒ **the bottleneck node is `unknown` (`C3`)**, and the
  chain map stops at the layer the desk can measure.
- **Cross-sector chain named**: AI → power → transformers → **copper**. Its other end is measured in
  `SECTOR_DEEP_ENRG` and `BLINDSPOT_PREMORTEM` Lens 4, and **that end says the power layer has no
  money in it** (every AI-power name 🟡/🔴). ⇒ **the copper thesis's demand leg is being contradicted
  at the node one hop downstream.**

**chain-hop** (`chain-hop "gold miners" --days 7 --scope foreign`): candidates returned were
`XYZ`/`AMD`/`AMGN`/`DIS`/`XOM` — ⚠ **all from generic market-wrap articles, none body-proximate to a
metals mechanism.** ⇒ **zero admissible chain-hop candidates from Materials this run**, stated rather
than passing noise to BET.

## 4 · Customers named, and their disclosed spend (rule **A6**)
- `NEM`'s buyer is **the gold price**, not a nameable customer — central banks and ETFs. `GC=F` fell
  **4,609.7 → 4,431.1 over three sessions to 08-31** (and 4,388.2 on 09-01 **[live]**) **while
  `DTWEXBGS` rose** ⇒ the demand-side variable moved **against** the name in the same window its
  `rs20` read +30.9. **Named, and it disagrees.**
- `FCX`/copper's buyers are grid + datacenter electricals: **`ETN` −0.339 · `VRT` −0.215 · `PWR`
  −0.597🔴 · `HUBB` (not in universe)**. **Their disclosed spend is not in a print this window** —
  next relevant dates are the utility/industrial Q3 season (late October). **Said with the date rather
  than concluded around.**
- `LIN`'s buyers are industrial gas offtakers under long contracts — see §5.

## 5 · Frame-transfer question — answered
> *Does the take-or-pay / contracted-revenue frame the desk trusts on `KMI` (RPO), `LNG` (tolling) and
> `MU` (floor/ceiling) apply to this node?*

**Checked, and it SPLITS the sector — which is the useful answer.**
- **`LIN` (industrial gases): YES, structurally.** On-site industrial-gas plants run on long-term
  take-or-pay contracts with fixed-fee and pass-through components — the same shape the desk credits
  in midstream. ⇒ `LIN`'s `wflow` weight is attached to the **least** cyclical cash flow in the
  bucket, which is a reason its `rs60` (−4.8 vs `SPY`) lags in a metals rally **and** a reason it will
  not crack with metals. ⚠ **The contracted share is `unknown` (`C3`)** — the 10-K was not opened this
  run; `module_disclosure_us LIN` was not called. **Named as a gap, not filled with an estimate.**
- **`NEM`/`FCX` (miners): NO. Checked, does not apply.** Miners sell at spot; there is no floor. ⇒
  lens **B2**'s mechanism (peaking denominator) applies **in full** and has **no contractual escape
  hatch** — the opposite of `MU`, where `R111` established a floor/ceiling band. **This is the
  transferable point**: the desk has been carrying "take-or-pay protects the margin" as a general
  comfort; it protects `MU` and `LIN`, and it protects **neither** name that is actually driving
  Materials' positive flow.

## 6 · Track KPIs and anti-signals (observables, not opinions)
| KPI | now | what would change the verdict |
|---|---|---|
| Copper spec 1-year %ile `[COT]` | **100** | **< 80 while `FCX` holds OBV 매집 AND `rs20` > 0 vs `SPY`** (RULE D6 — OBV is C-grade and never carries a line alone) ⇒ crowding unwound without the price = the only configuration that makes the metals leg ownable |
| `NEM` QoQ revenue rate | **−16.3%** (Q2) | **a positive QoQ in the 2026-09-30 quarter** (reports ~late Oct) ⇒ the deceleration was one quarter, not a turn |
| `NEM` `vol_surge` | **1.19** | **≥ 1.20** with 매집 held ⇒ 🟢 tag; **filed to `missed_ledger` this run**, recheck **2026-09-08** |
| Sector greens | **0 of 12** | **≥ 2** ⇒ the OW gets an ignition it has never had |
| `GC=F` | 4,431.1 (08-31) | **stops falling with `DTWEXBGS` still rising** ⇒ the demand leg re-couples |

**Anti-signals that would kill this file's TRAP reading**: (i) copper spec %ile falling below 80 with
price held; (ii) a positive `NEM` QoQ revenue rate next print; (iii) a named smelting/refining
capacity constraint from a primary source — which would move the bottleneck from `unknown` to real.

## 7 · Handed forward
- **To BET**: **no Materials name is handed as CONFIRMED-EARLY.** `NEM` and `FCX` are logged as
  **LATE-MONEY** (crowded underlying, `NEM` filed to `missed_ledger`). `NUE` (held) is flagged: it is
  the sector's 2nd-worst flow row and the only Materials exposure the book has.
- **To the next ROTATION**: the mandate's answer is **trap-shaped on metals, structurally different on
  gases** ⇒ *"Materials OW"* is not one verdict. `C24` is **not** resolved by this file; it is
  **relocated** — the contradiction is not flow-vs-positioning, it is **metals-vs-gases inside one
  label**.
