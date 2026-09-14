# SECTOR_DEEP_ENRG — Energy / oil-refining · industry_US · 2026-08-29 (Stage 8 / L1·DEEP)

> **CONTINUOUS TRACK** — ENRG takes the continuous slot `MATR` vacated (`SECTOR_ROTATION §3`).
> **LEADS with the delta**; the structural map is carried by reference to
> `REPORT/industry_US/SECTOR_DEEP_ENRG.md` (2026-08-27).
> ⚠ Fan-out executed **in-line, not as parallel subagents** (`BLINDSPOT_PREMORTEM §0`).
> P4 — analytical only, no sizing.

## §0 · The mandate ROTATION handed this file, and the constraint it came with

> *"`XOM` alone carries the sector negative (`wflow` −0.051 vs `wflow_ex_top1` +0.168). Is the sector
> the refiners?"* — **with a hard constraint attached**: 🚫 ***`R89` is retracted and its successor
> `P83` FIRED-B. The desk has NO surviving instrument separating refining margin from the barrel.
> This DEEP may not re-assert separation; it must either build a new instrument or state the claim
> is unavailable.***

**Answer: yes, the sector is the refiners — and the separation claim stays unavailable.**
What this file does instead of re-asserting it is **read the crack as a price cycle on its second
derivative**, which is the one thing the desk's own rules say to do with a commodity node and which
neither `R89` nor `P83` attempted.

## §1 · The delta — what changed since 2026-08-27

| | 08-27 file said | today | delta |
|---|---|---|---|
| sector verdict | `N` (MACRO) | **`OW`** | 🔴 **CHANGED** on `eqflow` +0.092 only |
| 3-2-1 crack | *"as printed **−8.584** = deep inside `P96` branch A"* — read off a **LIVE intraday** 08-27 bar | **settled 08-27 = +4.874, branch B, 13.5 points away** | 🚨 **The prior file was on the wrong branch.** `D355` on a registered row; `P96` landed **`FIRED-B`** |
| separation instrument | `P83` armed as `R89`'s successor | **`P83` `FIRED-B`** — the spread collapsed **13.562 points in five sessions** | 🔴 **DEAD.** No successor exists |
| Hormuz | reopening priced | **Iran–Oman temporary transit deal 08-26**, but **Qatar LNG force majeure extended, traffic "remains halved"** | 🆕 contested, `P112` registered |

## §2 · ★★★ The crack read as a PRICE CYCLE — rate of change, not level (lens B1)

The desk's own rule: *"for any commodity node, tabulate the QoQ change series. Level and rate
routinely point opposite ways. **Two consecutive declines in the rate is the signal; the level is the
distraction.**"* **This has never been done for the crack on this desk.** Doing it now:

**3-2-1 crack (`(2·RB + HO)·42 − 3·CL)/3`, settled `yfinance` continuous futures, quarterly means:**

| quarter | level ($/bbl) | **QoQ rate** |
|---|---|---|
| 2025 Q3 | 26.447 | +8.42% |
| 2025 Q4 | 25.299 | −4.34% |
| 2026 Q1 | 32.065 | +26.74% |
| **2026 Q2** | **50.958** | **+58.92%** |
| 2026 Q3 (partial) | 65.313 | +28.17% |

⚠ **C2 / A1 — the partial quarter is compared LIKE-FOR-LIKE, not against a full one.** Q3 covers
07-01 → 08-27 (n=41 sessions). Measured against the **identical window position** in Q2
(04-01 → 05-27, n=39): **Q2 51.288 → Q3 65.313 = +27.34% QoQ like-for-like.** The partial and the
like-for-like agree to within 0.8pp, so the reading is not an artifact of the window.

★★★ **`M1071`** `[measured]` **The 3-2-1 crack's rate of change has decelerated ONCE, not twice:
+58.92% → +27.34% (like-for-like). By the desk's own stated rule, that is NOT yet the signal —
two consecutive declines in the rate is.** The prior decline (Q4 2025 −4.34%) is separated from this
one by two accelerations.

★★ **And the level says the opposite of the rate, which is exactly the shape the rule predicts:**
the **last settled daily crack is 71.129 (08-27)** — *above* the Q3 mean of 65.313, i.e. still
climbing **inside** the decelerating quarter. Monthly means confirm the noise the quarterly frame
smooths: **+81.15% (Mar) → +5.08% → +11.87% → −6.98% → +30.07% (Jul) → −0.82% (Aug, partial).**

🚨 **`M1072`** `[measured]` **The refiners' equity is tracking the LEVEL, not the rate — and the
desk's regime doctrine says it should track the rate.** `MPC` `rs60` **+36.7**, `PSX` **+29.8**,
`VLO` **+32.7**, all `OBV 매집`, while the rate has already made its first deceleration.
⇒ **Two readings, and this file refuses to pick between them without a second decline:**
- (a) the equity is early to the level and will de-rate when the rate declines a second time;
- (b) the refining equity is not a pure second-derivative asset because **capacity closures are a
  level story**, and the second-derivative rule was derived on **memory contract prices**, a different
  contracting regime.
**Neither is asserted.** ⇒ **Registered as the sector's #1 open question and the KPI in §7 is the
next quarterly rate print.**

## §3 · Flow — the sector is the refiners, and the number says so

`asof 2026-08-27` settled, n=16 (`SECTOR_FLOW_US.json`):

| ticker | flow | OBV | `rs20` | `rs60` | `vol_surge` |
|---|---|---|---|---|---|
| `MPC` | **+0.661** | **매집** | +11.8 | **+36.7** | 0.99 |
| `SLB` | **+0.572** | **매집** | +8.5 | −4.3 | 0.83 |
| `PSX` | +0.455 | **매집** | +9.9 | **+29.8** | 0.84 |
| `COP` | +0.378 | **매집** | +4.8 | +9.3 | 0.93 |
| `VLO` | +0.338 | **매집** | +7.2 | **+32.7** | 0.69 |
| `WMB` | +0.248 | **매집** | +0.7 | +2.5 | 1.00 |
| `OXY` | +0.193 | 중립 | +1.8 | — | 0.74 |
| `CVX` | +0.160 | **매집** | −0.1 | +5.0 | 0.85 |
| **`XOM`** | **−0.551** | **분산** | −4.3 | +3.1 | 0.93 |

- **`eqflow` +0.092** (2nd-highest of 11) · **`wflow` −0.051** · **`wflow_ex_top1` +0.168 = the largest
  ex-top1 positive on the board** · breadth 0.00.
- ⇒ **`XOM` is the entire negative.** It is a `top1_flips_sign` bucket, so the promotion was made on
  `eqflow` and **not** on `wflow` (G3). `XOM` is in the reject ledger (`K.본문반증`, recheck **09-09**).
- 🚨 **breadth = 0.00 and ZERO shortlist names, and the diagnosis is a filter artifact, not absence**:
  **every one of the top eight is `OBV 매집` with positive-or-flat `rs20`, and every one has
  `vol_surge < 1.00`.** The 🟢가속 tag requires a volume surge the whole sector lacks. **`SWEEP_READ §5`
  measures this; `M1062` adds that `vol_surge` is the axis whose measured IC sign is negative.**
- ★ **Sub-sector dispersion (B5), and it is 41pp**: `MPC` `rs60` **+36.7** against `SLB` **−4.3** —
  refining and oilfield services are **not one trade**, and the sector's own move (+0.092 `eqflow`) is
  smaller than the spread inside it. **The label "Energy" is the wrong unit; "refining" is the right one.**

## §4 · Value chain — 6 nodes, binding constraint marked

`crude supply → transit (Hormuz) → midstream → REFINING → distillate/gasoline offtake → end demand`

| # | node | who | state |
|---|---|---|---|
| 1 | E&P / crude | `XOM` `CVX` `COP` `OXY` | `XOM` **분산**; the others 매집 but `rs20` ≈ 0 |
| 2 | **transit** | (not a ticker) | 🚨 **contested — see §5** |
| 3 | midstream | `WMB` `KMI` `OKE` | `WMB` 매집 but **`rs20` +0.7 ≈ flat**; `KMI` `vol_surge` **1.16** = the sector's only >1 reading |
| 4 | 🚨 **REFINING — the binding constraint** | `MPC` `PSX` `VLO` | **all 매집, `rs60` +29.8…+36.7** |
| 5 | product offtake | (distillate vs gasoline) | 🚨 **the two legs split — see §6** |
| 6 | services / capacity rebuild | `SLB` | **매집, `rs20` +8.5, `rs60` −4.3** = accumulation before the trend |

**Binding constraint = node 4, refining capacity.** Not demand (demand is not a bottleneck, per the
L1's own warning) and not crude — crude is at 83.53 with WTI spec positioning at the **43rd
percentile**, i.e. unremarkable. **What is scarce is conversion**, which is what a 71-dollar crack
measures and what `M1071` tabulates the rate of.

## §5 · The transit node — two head-layer items that contradict each other

| says reopening | says still closed |
|---|---|
| *"Crude heads for weekly losses as **Hormuz fl[ows recover]**"* — **14 outlets** | *"**Qatar Extends LNG Force Majeure** as Hormuz Traffic **Remains Ha[lved]**"* — 6 outlets |
| *"Gulf Oil Exports **Rebound** Despite Iran War"* — 7 outlets | *"**Hormuz Tanker Traffic Drops** Despite Recovery in Oil Flows"* |
| Iran–Oman **temporary** transit deal, 2026-08-26 | *"Natural Gas: Hormuz risks and Qatari LNG disruption"* |

★ **`M1073`** `[measured]` **The liquids reopened and the LNG force majeure did not lift.** The crude
tape and the gas tape are pricing **different straits**, and the desk's `WMB` (gas midstream) is
`rs20` **+0.7 ≈ flat** — i.e. **the gas leg is not trading the force-majeure story at all.**
⇒ **`P112` (Brent ≤84.00 / ≥94.50 through 09-11)** is registered on exactly this contest, with
**Venezuela as its live VOID at 14 outlets.** Brent settled 08-28 = **88.10**, 4.10 above A and 6.40
below B — **inside C, and closer to A.**

## §6 · 🚨 The product split, and it contradicts the loudest body in the sector

`P83` was `(HO − RB)×42` and it **collapsed 13.562 points in five sessions** — composition disclosed:
**`HO=F` 4.480 → 4.279 (−4.5%)** while **`RB=F` 3.263 → 3.384 (+3.7%)**. **The distillate leg fell.**

Against that, the `chain-hop` body pass returns, repeatedly and across market-cap-unrelated tickers,
one headline: ***"Diesel Crisis Threatens to Outlast the Middle East War."***

🚨 **`M1074`** `[measured]` **The narrative says a structural diesel crisis; the settled distillate
futures fell 4.5% in five sessions while gasoline rose 3.7%.** ⇒ **Either the "crisis" is already in
the level (71-dollar crack) and the marginal news is not moving the marginal barrel, or the narrative
is lagging.** **This file does not resolve it — it names it**, because resolving it by picking the
narrative is what `R89` did and `R89` is retracted.
🚫 **And this is where the separation claim would go, so it is stated as unavailable**: with `R89`
retracted and `P83` `FIRED-B`, **the desk has no instrument that shows the refining excess is
independent of the barrel.** Per §0's constraint, **this file does not build one either** — a third
spread invented under time pressure would be the `M47` defect. **What it does instead is §2**: read
the crack's own rate of change, which is a property of the margin and needs no separation claim.

## §7 · Chain-hop — flow-crossed, and most of it rejected

`chain-hop refinery "crack spread" diesel --days 7 --scope foreign`:

| candidate | proximity / body | flow cross-check | verdict |
|---|---|---|---|
| **`KMI`** | 2 / 3 | `vol_surge` **1.16 = the sector's only >1.0**, but flow −0.092 and **OBV 중립, `rs20` −4.3** | ⚠ **Recorded, NOT promoted** — the one volume reading in the sector sits on a name with no accumulation. Example body: *"Eight petroleum liquids pipeline projects have been completed since the start of 2025"* |
| **`CMI`** (Cummins) | 4 / 4 | not in this sector's flow table (Industrials) | ⚠ **Genuinely chain-adjacent** to a diesel story, but Industrials is `UW−` and has no DEEP slot. **Logged, not promoted** |
| `GOOGL` `GOOG` `META` `MSFT` `BAC` `KO` `AXP` `DAL` `SPGI` `F` | 2–4 | — | 🚫 **Rejected as tool noise.** All surface through one cross-topic article (*"Diesel Crisis Threatens to Outlast the Middle East War"* mentions megacaps in an unrelated paragraph). **A news co-mention alone is not a candidate** — none reaches BET |

## §8 · Customers and their disclosed spend (rule A6)

**Named**: the refining node's customers are **road/air freight and industrial diesel users**, not a
capex line. ✅ **One disclosed, dated demand data point in-window**: *"Warren Buffett Called Airlines
the 'Worst Sort of Business'…"* and *"Should You Dump Airline Stocks With the Iran War Still
Sim[mering]"* (3 outlets, 08-28) — **airlines are the visible jet-fuel buyer and the tape is asking
whether to sell them.** ⚠ **`DAL`'s spend is `unknown` from this run's instruments (`C3`)** — no
airline fuel-cost disclosure was pulled, and no conclusion is drawn around it.

## §9 · Track KPIs and anti-signals — stated as observables

| # | KPI / anti-signal | observable | kills what |
|---|---|---|---|
| 1 | ★ **the second decline** | **3-2-1 crack QoQ rate at the 2026 Q3 close (09-30)**, like-for-like. Today **+27.34%** after **+58.92%**. **A second consecutive decline is the desk's own stated signal** | `M1072` reading (b), and with it the refiners' `OW` |
| 2 | `P112` | Brent settled ≤ **84.00** (A) or ≥ **94.50** (B) on any settled bar through **09-11**. Today **88.10** | the transit contest (§5) |
| 3 | `P107` | Brent ≤84.00 / ≥96.00 through 09-08 — **NOT re-frozen**, runs beside `P112`; **if the two disagree, the disagreement is the finding** | — |
| 4 | refining accumulation | `MPC`/`PSX`/`VLO` `OBV` turning **분산** on any settled sweep | the `OW`, immediately |
| 5 | `L2` peak-margin, **not waived** | **`VLO` trades 8.4% ABOVE its mean target** on the carried §3a row. **No forward multiple is quoted in this file without a margin percentile**, so **no cheapness claim is made about any refiner** | any valuation argument |
| 6 | 🚨 **VOID for the whole sector view** | a **Venezuela supply event** — *"Venezuela weighs OPEC exit"* (14 outlets), *"US has deal for control of 65 billion barrels"*, *"Chevron in talks to expand in Venezuela"* (7 outlets). **A western-hemisphere barrel shock moves Brent for a reason unrelated to Hormuz.** Base rate checked and **NOT remote** | `P112`'s scoreability and §5's read |

## §10 · What this file could NOT do, stated rather than worked around

1. **It did not build a replacement separation instrument.** `R89` retracted, `P83` `FIRED-B`;
   inventing a third spread under time pressure is `M47`. **The claim "refining margin is independent
   of the barrel" is UNAVAILABLE to every downstream stage this run.**
2. **It did not read contract terms.** The `RESEARCH.md` rule — *"before calling a cyclical's margin
   unsustainable, read its CONTRACT terms from the filing, not the press"* — was **not executed** here:
   no `module_disclosure_us` 10-Q pass was run on `MPC`/`PSX`/`VLO`. ⇒ **the share of refining volume
   under term contract is `unknown` (`C3`)**, and per the rule **no margin-collapse assertion is made.**
   ★ **This is the rule's own generalisation biting**: the desk applied take-or-pay to `KMI`, `LNG`
   and `VST` and to memory, and **has still never pointed it at refining.** Registered as a dig (`D406`).
3. **It did not use `module_chart`'s OBV** (`M1067`, `SECTOR_DEEP_HLTH §9`) — its two implementations
   disagree because they read different terminal bars.

## ✅ EXIT CHECK (this file)
- [x] flow → players → chain map (6 nodes, bottleneck = **refining capacity**, marked) → chain-hop (10 of 12 rejected as noise, both survivors logged not promoted) → KPIs + anti-signals.
- [x] **Continuous-track: LED with the delta** (§1) — including that the prior file's crack read was on the **wrong branch** off a live bar.
- [x] **ROTATION's flagged divergence resolved explicitly** (§0/§3): the sector is the refiners; `XOM` alone carries it negative; promotion made on `eqflow`, never `wflow`.
- [x] 🚨 **Commodity node carries a QoQ RATE-OF-CHANGE series, not just levels** (§2) — quarterly, monthly, **and a like-for-like partial-quarter control** so the incomplete quarter is not compared against a full one.
- [x] **Sub-sector dispersion stated (B5)** — 41pp between refining and services inside one label (§3).
- [x] `L2` peak-margin applied and **not waived**; **no cheapness claim made** without a margin percentile (§9).
- [x] **The constraint the mandate imposed was honoured**: the separation claim is stated as **unavailable**, and the file says what it could not do (§10) instead of routing around it.
