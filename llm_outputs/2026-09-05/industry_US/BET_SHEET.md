# BET_SHEET — industry_US · 2026-09-05 (Sat) · Stage 9 / L1·BET

> **ONE file, per-sector sections.** Downstream desks glob this exact filename — never split it.
> Flow asof **2026-09-04 settled close**. Fundamentals pulled **2026-09-05**.
> **Analytical output only. Sizing language is influence illustration; zero buy/sell recommendation (P4).**
> §B freshness tags are **placeholders — ALPHA fills them** (the sweep's news axis is dead, `G1`).

## §0 · Company scoreboard — consulted first, and it does not reach this sheet

`REPORT/COMPANY_SCOREBOARD.md`, `company_batch` run 1, dated **2026-08-21**.
**Zero US names carry a row** — all five entries are KR (036460, 011200, 316140, 028050, 000660).
The file is also **10 settled sessions old** (08-21 → 09-04 inclusive), i.e. **at the age test's
boundary** even for the names it does cover.
⇒ **No candidate below is CONFIRMED-by-citation; every one is derived here, and the reason is
coverage, not a failed test.** ⚠ **`No row ≠ no coverage`**: `module_report_tags show` was
cross-queried at HANDOVER (80 reports, 297 names) and the US names below **do** carry report history
there — the scoreboard is a different object from the tag ledger and only the former was empty.
⚠ Its own two reading rules are honoured and none of its scores appears here: the score measures
research quality, not expected return, and **its top row is a `PASS`**.

## §0b · The instrument caveats that bind every section

| | |
|---|---|
| 🚫 **Green tags** | The 🟢 gate needs `vol_surge ≥ 1.2` alongside OBV and RS (`M25`). **`C29` is open**: the KR `ic_ledger` scores that axis at **IC −0.0414 · t(NW) −3.61 · n_eff 45**, clearing Bonferroni for a **third** run with a **negative** sign, while the gate weights it **positively**. `W1` bars importing the verdict. ⇒ **every 🟢/🟡 below is reported with the axis that produced it, and no name is promoted or set aside on a tag.** `S145` (09-11) is the US-market test |
| 🚫 **Cap weights** | universe file is **52 days** old (`G5`) — **no `top1_w%` or cap-weighted number below is cited as current size** |
| 🚫 **Sweep velocity** | `vel_coverage` **16.39%**, axis dead (`G1`). **No §B freshness number comes from the sweep**; ALPHA fills them from direct calls |
| ⚠ **Concentration** | measured risk units are **12 / 11 / 10 at `--days` 250 / 500 / 750** with differing membership; at 500 and 750 **`ANET`+`ETN` merge into ONE unit spanning two book theme labels** (`G4`). **No single-number concentration claim appears below** |
| ✅ **Earnings dates** | every print date below is from **`Ticker.earnings_dates`**, not the forward-calendar field (`D488`) |

★ **`M1321` [measured] — and that check immediately corrected a carried date.** The desk's carry
lists *"`MU` FQ4, 2026-09-24"*; `module_fundamentals_us` says **2026-10-01**; **`Ticker.earnings_dates`
says 2026-09-30 16:00 ET**. Three sources, three dates. **The `D488`-mandated one is 09-30.**
✅ **And it clears the brackets**: no candidate on this sheet prints inside `S145`'s window
(09-05 → 09-11) — `STX` **10-27**, `WDC` **11-05**, `AMD` **11-03** — so **`S145`'s VOID clause is
verified not to fire**. Nor inside `S146`/`S147`'s (to 09-14): `VST` 11-05, `CEG` 11-09, `ETN` 11-03,
`MPC` 11-03.

---

# §ENRG — Energy (`OW+`, continuous DEEP)

## §A · Numbers

| | `MPC` (held) | `PSX` (held) | `VLO` (rejected) | `SLB` | `WMB` | `XOM` |
|---|---:|---:|---:|---:|---:|---:|
| price | **$388.90** | $255.09 | $370.69¹ | $57.51 | $74.15 | — |
| fwd P/E | **12.24** | — | 11.88¹ | 17.79 | 28.51 | — |
| trailing P/E | 13.48 | — | — | 28.05 | 29.54 | — |
| PEG | 1.86 | — | — | 1.51 | 2.13 | — |
| consensus mean target | **$326.83** | — | $319.63¹ | $62.03 | $85.47 | — |
| **implied vs price** | 🚨 **−16.0%** | — | 🚨 **−13.8%¹** | +7.9% | +15.3% | — |
| next print (`earnings_dates`) | **2026-11-03** | — | — | 2026-10-23 | 2026-11-03 | — |
| **quarterly op margin, last 5** | 5.61 → 4.81 → 5.67 → 3.03 → **13.42%** | 3.57 → 2.80 → 4.75 → 0.35 → **8.39%** | 3.34 → 4.69 → 5.19 → 5.35 → **11.68%** | — | — | — |
| **annual op margin, 2022→2025** | 10.69 · 8.48 · 3.78 · 4.35 | 5.66 · 5.39 · 1.22 · 2.55 | 8.93 · 8.19 · 2.89 · 3.51 | — | — | — |
| estimate momentum, 90d | curr qtr **+117.8%**, next qtr **+83.5%**; breadth **14↑/0↓** (30d) | — | — | — | — | — |

¹ `VLO` figures are **carried from the 2026-09-04 rejection re-check, not re-pulled this run** — labelled, not refreshed.
**Blanks are blanks.** `PSX`, `VLO`, `XOM` valuation was **not pulled this run** (budget allocation, stated) and is **not estimated** (`C3`).

★ **`M1313` restated for BET: all three refiners are at their highest quarterly operating margin in
the visible five-year series, and the quarter that set it (2Q26, ended 06-30) PRE-DATES the current
crack spike.** 2Q26 was earned on a distillate crack averaging **64.47**; 3Q26 QTD averages
**90.59, +40.5% QoQ**. **The peak is not in the printed numbers yet, and the next print is 11-03** —
outside every bracket this run holds.

⚠⚠ **`L2` peak-margin trap, stated and NOT resolved in the thesis's favour.** A **12.24×** forward
multiple on a denominator at a five-year high, with estimates revised **+117.8% in 90 days on 14↑/0↓
breadth**, is **consensus chasing, not cheapness** — and the tape sits **16.0% ABOVE** the consensus
mean with **8 of 19 analysts at Hold**. This is the exact basis on which `VLO`'s rejection was
reaffirmed on 09-04, and it applies identically to the two names the book holds.

## §B · Thesis (freshness: **ALPHA fills**)

**Re-specified this run: this is a DISTILLATE trade, not a barrel trade.** 5-session into 09-04:
WTI **+8.08** · distillate crack **−0.37** (holding at **99.21 = 95.6th pctile**) · gasoline crack
**−19.64** · blended 3-2-1 **−13.22** · **distillate−gasoline spread 55.68 = 98.4th pctile**.
The mechanism is **capacity destruction with a structurally blocked supply response**
(*"Why Oil Majors Don't Want to Build New U.S. Refineries"* 09-03; *"Refining capacity will not come
back"* 09-03). **The narrative is decelerating on every news instrument** (`crude oil` **−14.7%**,
`Strait of Hormuz` **−10.4%**, `refining margin` **0.66× for a 3rd run**) while the physical print is
at an extreme — **the divergence that `P136` and `S147` are registered to settle on 09-14.**

## §C · Flow / positioning cross-read

| name | flow · tag | OBV | rs20 / rs60 | `vol_surge` | `[FINRA]` z (09-04) |
|---|---|---|---:|---:|---:|
| `MPC` | +0.694 🟡 | **+0.621 매집** — the chain's strongest | **+30.8 / +41.5** | **1.05** | +0.43 |
| `PSX` | +0.750 🟡 | **+0.434 매집** | +25.5 / +34.2 | **1.15** | −0.36 |
| `VLO` | +0.700 🟡 | **+0.482 매집** | +24.7 / +37.5 | **1.06** | — |
| `SLB` | +0.883 **🟢** | +0.439 매집 | +14.2 / **−2.6** | 1.39 | ✅ **−1.21** short-cover |
| `WMB` | +0.769 **🟢** (Δ **+0.347**, new-🟢) | +0.151 매집 | +5.7 / **−3.6** | 1.39 | — |
| `XOM` | **+0.027 🟡** | **−0.071 중립** | +4.6 / −0.3 | 0.97 | +0.47ⁱ |

🚨 **`M1298` — the tag is selecting on the wrong axis.** The three 🟡 refiners carry OBV **+0.43 to
+0.62** and rs20 **+24.7 to +30.8**; the two 🟢 carry OBV +0.15/+0.44 and rs20 +5.7/+14.2 **with
negative rs60**. The separator is `vol_surge` (**1.05–1.15** vs the 1.2 gate). ⇒ `M25`'s ENRG
artifact measured live. **No stage may read the refiners' 🟡 as weakness.**
Sector context: `eqflow` **+0.562 rank 1**, Δ **+0.054**, breadth **0.19 rank 1**, **3🟢/0🔴 of 16 —
the board's only zero-red sector**; non-flipper (`XOM` 30.5%, `wflow` +0.440 → ex-top1 **+0.621**).
ⁱ carried from the 09-01 `[FINRA]` read, not re-pulled — labelled.

## §D · Competition / peers — the structural contrast that runs through this whole sheet

★★ **`M1322` [measured] — the names this book HOLDS trade above consensus targets; the names it does
NOT hold trade 30–49% below them.**

| held? | name | fwd P/E | implied vs mean target |
|:--:|---|---:|---:|
| ✅ | `MPC` | 12.24 | **−16.0%** |
| ✗ | `VLO` | 11.88¹ | **−13.8%¹** |
| ✗ | `MU` | **6.56** | **+48.8%** |
| ✗ | `VST` | 14.40 | **+45.6%** |
| ✗ | `STX` | 15.34 | **+32.5%** |
| ✗ | `CEG` | 22.41 | +16.5% |

⇒ **This is `M1253`'s carried claim reproduced on a wider set**: *"the same input is priced in
opposite directions in Energy and IT."* ⚠ **`C4`: consensus targets are analyst opinion, not a
measurement**, and a "below target" name is not thereby cheap. It is used here **only** as the
`L2` peak-margin diagnostic the stage rule requires, not as a ranking.

## §E · Refutation + dated catalyst

**Kill conditions, as observables:** ① 🚨 **a US federal policy action against refiner margins or
fuel pricing** — the live thread is *"U.S. diesel price soars… **as Trump ramps up pressure on
refiners**"* [seekingalpha 09-01]. **This is NOT in `P136`'s VOID clause and IS in `S147`'s.**
② distillate−gasoline spread **below its 50th percentile**. ③ **`MPC` or `PSX` OBV leaves 매집**.
④ an OPEC+ emergency production decision, or an announced Hormuz-open statement (**undated**,
written `[blank]`).
**Dated catalysts:** **PPI 09-10** · **CPI 09-11** · `P136` settles **09-14** · `S147` settles
**09-14** · `MPC`/`WMB` print **11-03**, `SLB` **10-23**.
🚨 **The primary-source negative, carried into BET rather than left in the DEEP:** Form 144 insider-sale
notices are running **4.2× `MPC`'s own 365-day base rate (7 in 30 days)** and **2.9× `PSX`'s (6)**,
while **`VLO` — the one NOT held — is at zero** (`M1312`). ⚠ Form 144 is a *notice of proposed sale*,
often a scheduled 10b5-1 execution; **share counts and values are `unknown` in this instrument
(`C3`)** and a rising base rate is partly mechanical in a rising price. **`n` = 7 and 6.**

---

# §HLTH — Health Care (`OW`, continuous DEEP)

## §A · Numbers

| | `MDT` | `MRK` |
|---|---:|---:|
| price | $94.17 | $150.33 |
| fwd P/E | **14.72** | 15.75 |
| trailing P/E | 23.19 | **122.22** |
| PEG | 1.68 | 2.92 |
| consensus mean target | $104.76 | $148.73 |
| implied vs price | **+11.2%** | **−1.1%** (at target) |
| next print (`earnings_dates`) | 2026-11-17 | 2026-10-29 |

**Blanks are blanks**: no margin-percentile series or estimate-revision table was pulled for either
name this run (budget allocation, stated). ⇒ **no "cheap" claim is made about either** — the stage
rule requires a margin percentile with any forward multiple, and this run does not have one (`C3`).

## §B · Thesis (freshness: **ALPHA fills**)

**The sector's engine is Biotechnology and its drag is Equipment, and the desk had neither named.**
Node `eqflow`: **Biotechnology +0.519** (6/6 positive, 20d **+10.17%**) vs **Health Care Equipment
−0.044** (8 names, negative on **both** windows). `MDT` is the sector's **only** 🟢 and it sits
**inside the weak node** — its seven peers drag it (`SYK` 🔴 −0.706, `IDXX` 🔴 −0.692,
`ISRG` rs60 −17.2). The binding constraint is **pricing policy, not capacity**: MFN pricing extended
to nine mid-sized drugmakers [5 outlets] ⚠ **carried at its 09-02 date and NOT refreshed this run.**

## §C · Flow / positioning cross-read

| name | flow · tag | OBV | rs20 / rs60 | node |
|---|---|---|---:|---|
| **`MDT`** | **+0.928 🟢** | **+0.327 매집** | +8.4 / +11.2 | Equipment (the node's only strong name) |
| **`MRK`** | +0.567 🟡 | +0.185 매집 | **+17.3 / +20.1** | Pharma — **the node's best** |
| `ALNY` | +0.683 🟡 | +0.359 매집 | **+21.8** / −14.8 | Biotech |
| `GILD` | +0.561 🟡 | **+0.361 매집** | +13.8 / +18.1 | Biotech |
| `REGN` | +0.513 🟡 | +0.194 매집 | +5.9 / **+31.4** | Biotech |
| `AMGN` | +0.533 🟡 | +0.157 매집 | +6.8 / **+23.3** | Biotech |
| `LLY` (`top1`, 19.4%) | **−0.462 🔴분산** | −0.149 | −2.7 / −5.0 | Pharma — **holds the sector DOWN** |

★★ **`M1318` — 22 of 32 names are OBV 매집 and exactly ONE is 🟢: a 68.8% accumulation rate against
a 3.1% green rate, the widest gap on the board.** ⚠ `RULE D6`: OBV is C-grade and carries nothing
alone — paired here with `exc20` **+3.63 mean / +3.74 median** (median ≥ mean = broad) and **12 of 32
negative on `exc5`**, the second-lowest negative rate after Energy.
✅ Non-flipper, and the `top1` holds it **down**: `wflow` +0.098 → **ex-`LLY` +0.232**.

## §D · Competition / peers

Node dispersion **11.72pp** (Biotech +10.17% vs Equipment −1.55%, 20d) against the sector's own
`exc20` **+3.63** ⇒ **~3.2×** — material, but **an order of magnitude smaller than IT's ~75×**.
⇒ **`Health Care` survives as a unit of analysis; `Information Technology` does not.** The `OW` is
admissible at the sector level with a composition qualifier, not a notch.

## §E · Refutation + dated catalyst

**Kill conditions:** ① a **new dated MFN/payer pricing action** naming further manufacturers.
② **Biotech's node `eqflow` turns negative** — the engine stops and the sector is left with a
negative Equipment node and a dragging `top1`. ③ **Δflow prints a second consecutive negative**
(today **−0.043**, the first) ⇒ HLTH enters the same two-axis-disagreement state ROTATION declined
`UTIL` on. ④ **`HCA` and Managed Care both turn 분산** ⇒ the demand-side witness flips from
corroborating an equipment problem to a sector-wide payer squeeze.
**Dated catalysts:** `S133` settles **2026-09-14** (constituents vs ETF — the direct test of §D's
dispersion) · `MRK` prints **10-29** · `MDT` **11-17**.

📌 **Ledger hand-off — `MRK`.** The 09-04 HANDOVER deferred `MRK`'s miss row to ALPHA *within this
run*: *"appears in a `SECTOR_DEEP_HLTH` value-chain node with a named driver, **or** rs20 > 0 while a
Health Care DEEP slot is taken."* **Both legs are satisfied** (leg A: named as the Pharma node's best
name in `SECTOR_DEEP_HLTH` §Δ3/§Δ5; leg B: rs20 **+17.3** and the HLTH slot **is** taken).
⇒ **ALPHA resolves it as `entered`.** BET does not write the ledger row (`D463`) and implies no size.

---

# §IT — Information Technology (`N`, PREMORTEM-promoted DEEP)

## §A · Numbers

| | `MU` | `STX` |
|---|---:|---:|
| price | $1,016.59 | $849.28 |
| **fwd P/E** | **6.56** | 15.34 |
| trailing P/E | 22.99 | 60.97 |
| **PEG** | **0.14** | 0.46 |
| consensus mean target | $1,513.11 | $1,125.00 |
| implied vs price | **+48.8%** | **+32.5%** |
| **next print (`earnings_dates`)** | **2026-09-30 16:00 ET** | 2026-10-27 |
| gross-margin history (`MU`) | 37.7 → 44.7 → 56.0 → 74.4 → **84.6%** = **the 100th percentile of a 17-year series, +25.7pp above the prior-cycle peak of 58.9%** (`M2`/`M18`) | — |
| estimate momentum (`MU`) | +1y EPS **100.53 → 150.91 over 90d (+50.1%)**, breadth **30↑ : 0↓** (`M14`) | — |

⚠⚠ **The revision table carries ZERO independent weight here and that is a measured rule, not
caution.** `scripts/measure_ic.py` (2026-08-09): two non-overlapping windows disagreed **in sign**
(W1 **+0.403**, W2 **−0.299**), both clearing the power floor; the **ex-IT 120-name control** gave
**+0.074 / −0.064** with Q5−Q1 collapsing **+9.4pp → −1.1pp**. ⇒ **the effect is an IT loading, not a
revision axis**, and `MU` is an IT name. It is used **only** to describe the denominator's direction.
⇒ **A 6.56× forward multiple on a 100th-percentile gross margin is a peaking denominator (`L2`), not
cheapness — and no claim of cheapness is made.**

🚨 **The contract check that must precede any "the margin must mean-revert" claim — and it BLOCKS
one.** `MU`'s FY26Q3 10-Q (SEC primary, read 2026-08-10): strategic customer agreements are
**take-or-pay with binding multi-year volumes**, carry a **ceiling at ~the 2Q CY2026 market price and
a floor for the term**, and management states that at **floor** pricing gross margin runs **above any
prior cycle's peak**. **The FY2025 10-K said the opposite.**
⇒ (a) **`L2`'s collapse mechanism does not apply to contracted volume, and the contracted SHARE is
`unknown` (`C3`) — this run did not re-open the filing body and does not estimate it.** **No
mean-reversion claim is made.**
⇒ (b) 🚨 **The ceiling flattens the desk's own regime evidence.** The carried chain's evidence #1 is
the DRAM contract-price QoQ series **+90~95% → +58~63% → +13~18%** (`M1`). If price renegotiates
inside a band whose ceiling is pinned to a **dated** market price, **that deceleration is arithmetic
hitting a cap, not demand weakening.** **The second-derivative reading is not admissible on this node
until the contracted share is read.**

## §B · Thesis (freshness: **ALPHA fills**)

**The sector label is the wrong unit by ~75×, and the money is in one node.** 5-session equal-weight
by sub-node: **memory/storage +7.56%** · hardware OEM +4.79 · GPU/ASIC +2.30 · semicap +1.33 ·
analog +0.59 · app software −2.95 · networking/optical −3.45 · security/systems sw −5.32 ·
**EDA −12.51%**. Spread **20.07pp** against a sector move of ~−0.16% absolute (`SPY` +0.11).
**`P101` settled `FIRED-C` today at −6.511pp from a +6.228 = 89.7th-percentile registration**, with
participation inverting from **91.7%/16.7%** to **21.1%/73.0%** — **`M1251`'s "IT's weak half is
semicap" is dated.**

## §C · Flow / positioning cross-read — and the node is invisible to the green gate

| name | flow · tag | **Δflow** | OBV | rs20 / rs60 | **`vol_surge`** |
|---|---|---:|---|---:|---:|
| **`STX`** | +0.047 🟡 | **+0.728 — #1 of 299** | +0.034 중립 | +4.9 / −2.1 | **0.59** |
| **`WDC`** | +0.068 🟡 | **+0.718 — #2** | −0.042 중립 | +8.0 / −10.8 | **0.68** |
| **`AMD`** | −0.245 🟡 | **+0.566 — #3** | +0.005 중립 | −0.8 / −0.6 | **0.60** |
| `SNDK` | +0.633 🟡 | +0.061 | **+0.351 매집** | **+43.9** / −0.3 | 0.94 |
| `MU` | +0.478 🟡 | +0.231 | **+0.194 매집** | +16.2 / +7.8 | **0.66** |
| `DELL` | **+1.000 🟢** | **0.000** | +0.252 매집 | +15.9 / +35.6 | **2.48** |
| `NVDA` (held) | −0.032 🟡 | −0.040 | **−0.084 분산** | +3.3 / +8.8 | 1.01 |
| `ANET` (held) | +0.047 🟡 | **+0.404** | +0.067 중립 | +3.1 / +21.5 | **0.60** |
| `AVGO` (held) | **−0.356 🟡** | +0.077 | **−0.454 분산** | **−15.9** / −10.0 | 1.56 |
| `HPE` (held) | +0.379 🟡 | **−0.421** | +0.060 중립 | −1.9 / +8.1 | 2.18 |

🚨 **`M1300` — the board's three largest Δflows are all here and NOT ONE is 🟢, because every one
prints `vol_surge` below 0.70.** The node's only 🟢 passed on surge **2.48** with a Δ of **exactly
0.000**.
🚨 **And the book is on the non-accumulating side of its own epicenter**: `NVDA` **분산**,
`ANET` **중립** (surge 0.60, so its tag cannot fire regardless), `AVGO` **분산 with rs20 −15.9**.
**Wide-net cross-check (independent instrument):** `us_setup_screener --sector "Information
Technology"` returns **`STX` in the leader-pullback bucket — RSI 31.2, +43% above its 200DMA, at the
50DMA** — a second instrument locating the same name.
**Chart (`MU`)**: OBV 누적 **+60%** but **BEARISH divergence** (price higher high, RSI lower high),
turn **PULLBACK-TO-SUPPORT**, RSI 50.7, stop **861.00**. ⚠ `RULE D6`: the OBV leg is paired with rs20
+16.2, Δflow +0.231 and the node's +7.56%; it carries nothing alone, and the divergence is printed
beside it rather than after it.

## §D · Competition / peers

**Semicap is genuinely weak and that is a different statement from "the hardware leg lost"**:
`AMAT` **🔴 −0.817** · `KLAC` **🔴 −0.645** · `TER` −0.592 · `ASML` −0.455 · `Q` −0.464.
**Networking/optical is the worst 20-session node** (−11.24): `COHR` **🔴 −0.778, rs20 −25.3** ·
`CIEN` **🔴 −0.361, rs60 −32.3** (its rejection was reaffirmed 09-04 on rs60 −32.6 — **unchanged**).
🚨 **`TSM` is not in `us_top300`** — the chain's largest node is **unmeasurable by this desk** and is
marked `unknown` (`C3`), not zero.

## §E · Refutation + dated catalyst

**Kill conditions:** ① **`MU` or `SNDK` OBV leaves 매집**. ② **`P137` fires branch B**
(`SMH` 4-session excess ≤ −2.886) ⇒ the 09-04 `[FINRA]` z **+2.99** on a **+2.61%** session was
distribution, not hedging. ③ a **semiconductor-specific US export-control ACTION** (a published
rule; a draft is pre-declared non-voiding). ④ 🚨 **the narrative anti-signal is ALREADY LIVE and
bearish** — *"China Is Grabbing Memory Market Share. This Stock Could Be a Big Loser"* [09-03],
*"Is the Memory Supercycle Peak Near?"*, *"Druckenmiller Kicked Micron to the Curb"*.
**Dated catalysts:** `S140` **09-08** · **`S145` 09-11** (`EW{STX,WDC,AMD}` − `SMH`; A ≥ +6.825,
B ≤ −3.406) · `P137` **09-11** · **`MU` prints 2026-09-30 16:00 ET**.

---

# §UTIL — Utilities / the AI-POWER LANE (`UW`, PREMORTEM-promoted DEEP)

## §A · Numbers

| | `VST` | `CEG` |
|---|---:|---:|
| price | $149.30 | $298.96 |
| fwd P/E | **14.40** | 22.41 |
| trailing P/E | 24.32 | 29.25 |
| **PEG** | **0.36** | 3.74 |
| consensus mean target | $217.42 | $348.30 |
| implied vs price | **+45.6%** | +16.5% |
| next print (`earnings_dates`) | 2026-11-05 | 2026-11-09 |

**Blanks are blanks**: no margin-percentile series was pulled for either (`C3`), so **neither is
called cheap**. ⚠ **`VST`'s PEG 0.36 and +45.6% implied upside are exactly the shape `L2` warns about
in reverse** — a low multiple on a denominator the desk has **not** located in its own history.

## §B · Thesis (freshness: **ALPHA fills**)

**Utilities is two buckets and the lane spans three GICS labels.** Merchant/nuclear generation
(`CEG` +0.644, `VST` +0.619) are the sector's top two and **the only two names in it with a positive
rs20**; every regulated name below carries **rs60 between −6.5 and −20.6** and all three 🔴 are
regulated. The gap `CEG` → `DUK` is **1.157 flow points inside one label**.
★ **The mechanism is the constraint the desk already identified and had not connected to the node
map**: if **permission to build** is binding (ERCOT interconnection halt; PJM removing a Meta-backed
750MW project; PJM clearing at the price cap for a third auction against a 6.8 GW shortfall, `M367`),
then **existing generation gets scarcity-priced and new equipment orders get deferred.**

## §C · Flow / positioning cross-read

| name | GICS | flow · tag | Δflow | OBV | rs20 / rs60 |
|---|---|---|---:|---|---:|
| `CEG` | Utilities | +0.644 🟡 | +0.050 | +0.188 매집 | **+11.2 / +17.2** |
| **`VST`** | Utilities | +0.619 🟡 | ★ **+0.491** | +0.207 매집 | +6.6 / +1.6 |
| `VRT` | **Industrials** | +0.129 🟡 | ★ **+0.444** | +0.082 매집 | +3.4 / −6.3 |
| `GEV` | **Industrials** | −0.186 🟡 | +0.245 | +0.022 중립 | −4.5 / +2.5 |
| 🚨 **`ETN`** (**held**) | **Industrials** | **−0.662 🔴분산** | +0.012 | **−0.115 분산** | **−8.0** / +3.3 |
| `AME`·`PH`·`CMI` | Industrials | **−0.424 / −0.628 / −0.522, all 🔴** | — | all 분산 (`CMI` **−0.558**) | rs20 −5.9 / −10.0 / −12.6 |

★★★ **`M1317` — the lane's money is in GENERATION and it is leaving ELECTRICAL EQUIPMENT, node-wide,
not name-wide.** Four of five components names are 🔴분산 with rs20 negative at all five.
📌 **BOOK FLAG (carried from EVENT_ALPHA Card 6 and verified on two instruments):** `ETN` is held;
the sweep says **분산 −0.115** and `module_chart --read` says **OBV 분배, 20d slope −63%, RSI 30.5,
turn NEUTRAL/CHOP, ignition `close > 413.73`, stop 390.71**. ✅ **`C25` does not fire — the two OBV
instruments agree.** ⚠ `[FINRA]` z **+2.16** on a **+3.46%** session is the one ambiguous reading and
is ambiguous by construction (`D6`).
**Chart (`VST`)**: OBV 누적 **+148%** — the strongest slope measured this run — with a **BULLISH**
divergence, turn **NEUTRAL/CHOP**, **ignition unfired at `close > 151.17`** (price 149.30), stop
**135.66**. ⚠ **An accumulating name that has not ignited is a different object from a runner.**

## §D · Competition / peers

The **frame-transfer answer** is the competitive structure: a merchant generator with a **contracted
PPA floor** captures scarcity pricing above the floor with contracted downside — **long optionality**.
An electrical-equipment maker sells into a **backlog**, which can be deferred or cancelled — **no
floor**. ⇒ the two nodes have **structurally different downside** and the flow has just separated them
along exactly that line. 🚨 **`C3`: the contracted MW share of `VST`/`CEG` and the `ETN` data-centre
backlog are `unknown` — this run did not open the 10-Q bodies and does not estimate them (`D516`).**
⚠ **`VST` Form 144 notices went from ~4.1/month (49 in 365d) to ZERO in the last 30 days** — same
direction as its flow, **recorded as a coincidence of sign, not as evidence**: counts only, values
`unknown`, and an absence of filings is weak in any case.

## §E · Refutation + dated catalyst

**Kill conditions:** ① **`VST` and `CEG` both leave OBV 매집** ⇒ the generation leg was two names.
② **`ETN` returns to OBV 매집 with rs20 > 0** ⇒ the split was one week of noise (= `S146` branch B).
③ **a PJM/ERCOT capacity-auction result or emergency order** inside 09-05 → 09-14 (`S146`'s VOID;
**base rate checked — no scheduled auction falls in the window**). ④ 🚨 **a regulatory reversal on
data-centre siting** — if interconnection queues clear, **equipment re-rates and generation
de-rates**; the split inverts rather than closes.
**Dated catalysts:** `P123` **09-08** · `P122` **09-08** · **`S146` 09-14** (`EW{VST,CEG,VRT}` −
`ETN`; A ≥ **+7.651** at p95 because the state is already at the **92.9th** percentile, B ≤ −5.037) ·
`ETN` prints **11-03**, `VST` **11-05**, `CEG` **11-09**.
⚠ **`VST` carries a standing rejection** (08-14 `G.섹터중립`), reaffirmed 09-04 because OBV missed the
0.05 accumulation cut **by 0.003** (`C5`). Today `obv_norm` is **+0.207 — four times the cut.**
**This stage does not overturn a rejection** (`D463`/ALPHA owns that); it records that the leg the
reaffirmation rested on has moved.

---

# §LIVE — cross-sector shortlist names outside the DEEP sectors

`US_LIVE_SHORTLIST.json`: 10 names. Four sit inside DEEP sectors and are covered above
(`SLB`, `WMB`, `CVX` in §ENRG; `MDT` in §HLTH; `DELL` in §IT). **The remaining five are handled here
— included or explicitly dropped with a reason, none silently omitted.**

| name | sector | flow · OBV · rs20/rs60 · surge | `[FINRA]` | disposition |
|---|---|---|---|---|
| **`HOOD`** | Financials (`N`, promoted today) | +0.783 🟢 · +0.215 매집 · **+31.3 / +35.2** · 1.21 | ✅ **−0.64** low-short | ★ **INCLUDED as a §LIVE candidate.** New-🟢 ignition this session (Δ +0.039); the only shortlist name whose sector verdict this run *raised*. Best rs pair among the non-DEEP names |
| **`DE`** | Industrials (`UW−`) | +0.911 🟢 · +0.176 매집 · +12.1 / +17.7 · **1.44** | −0.47 | ★ **INCLUDED with a flag.** One of only three 🟢 with genuine surge **and** OBV **and** a positive Δ. ⚠ **Its sector is `UW−` with 28🔴 of 50** — the name contradicts its label, which is the `W5` problem, not a reason to drop it |
| **`CTVA`** | Materials (`N`) | +0.861 🟢 · +0.265 매집 · +14.8 / +11.8 · 1.35 | −0.23 | ★ **INCLUDED with a flag.** Same three-axis quality as `DE`. ⚠ **`P102` settles Materials' "is it two names" question on 09-09** — a Materials name entering this sheet two sessions before that would pre-empt the bracket, so it is included **as a watch row only** |
| `TSLA` | Cons. Disc. (`UW`) | +0.828 🟢 · +0.169 매집 · +8.2 / **−13.4** · 1.29 | +1.19 | **DROPPED, with reason.** Its sector is the board's 2nd-worst on `eqflow` (−0.251) with **21 of 28 negative** on exc5, its **rs60 is −13.4**, and its live thread is a **negative** one (Cybercab launch → **NHTSA probe within 24 hours**, 13 + 6 outlets). ⇒ **narrative refuted the headline** — filed to the **rejection** ledger, class `K.본문반증` |
| `RSG` | Industrials (`UW−`) | +0.631 🟢 · +0.160 매집 · +4.2 / −1.4 · 1.22 | ⚡ **z +2.61 crowded-short** | **DROPPED, with reason.** ⚠ Its new-🟢 came with a **NEGATIVE Δ (−0.091)** — *it crossed the tag threshold while its own score fell*, which is a tag change, not a flow change. `⚡crowded-short` is squeeze **fuel on a turn condition**, never a standalone read. Filed to the **missed** ledger, class `Q.확신부족` |

⚠ **`TSLA` goes to the REJECTION ledger and `RSG` to the MISSED ledger, and the boundary is not a
judgement call**: a name set aside **with a stated reason** is a rejection; a name that simply did not
make the sheet is a miss. `missed_ledger add` refuses any ticker×date already in the rejection ledger
(exit 1), so the split is machine-enforced.

---

# §EPICENTER-STARTER MODULE

**`cycle_exposure` reports NO top-rank cycle GAP** — AI-compute epicenter **17.48%** (bar ≥12%),
Energy/refining **10.47%** (bar ≥8%), missile-defense 3.64% (no bar). ⇒ **the deterministic module is
not triggered and no starter is required by it.**

🚨 **But PREMORTEM Lens 4 found two things the flag cannot see, and BET carries them rather than the
✅:**
1. **`M1308`/`D513` — the AI-POWER cycle is not in the registry, so its absence reads as "no gap."**
   The lane is coherent and measurable (`CEG`, `VST`, `VRT` accumulating across two GICS sectors) and
   **the book's only exposure to it is `ETN`, the lane's single distributing name.** A registry that
   does not contain a cycle cannot flag a gap in it.
2. **`M1309` — the rank-1 cycle's held epicenter is on the wrong side of its own node's flow.**
   `NVDA` **분산**, `ANET` **중립**, while the node that actually moved — storage/memory, carrying the
   board's three largest Δs — is **0% of the book**. **17.48% of "AI-compute epicenter" exposure sits
   entirely in the half that is not accumulating.** The registry counts the label; the flow counts
   the node.
✅ **`M1310`, stated because a sheet that only finds problems is not adversarial:** the rank-2 cycle's
exposure IS correctly placed — `MPC`+`PSX` are the highest-OBV names in the entire Energy chain
(+0.621, +0.434) with rs20 +30.8/+25.5, on a cycle KPI at the 95.6th percentile.

⇒ **Handed to ALPHA and to the book desk as two named structural observations. No starter position,
no size, no recommendation is expressed here (P4).**

---

## ✅ EXIT CHECK — BET

- [x] **Company scoreboard consulted before any re-derivation** (§0). **Zero US rows**, and the file
      is at the 10-session age boundary. Every candidate is derived here **with that reason stated**;
      none is marked CONFIRMED-by-citation, and `module_report_tags` was cross-queried so "no row" is
      not read as "no coverage."
- [x] **Every DEEP sector has a section** (§ENRG, §HLTH, §IT, §UTIL) **and cross-sector LIVE
      shortlist names are included or explicitly dropped with a reason** (§LIVE — 3 included, 2
      dropped, both dropped names ledgered).
- [x] **Numbers cross-checked; blanks are blanks.** `module_math_check` run on this file. `PSX`/`VLO`/
      `XOM` valuation, all HLTH margin percentiles, and `VST`/`CEG` margin percentiles are marked
      **not pulled / `unknown` (`C3`)** and are **not estimated** — and **no "cheap" claim is made
      about any name whose margin percentile is missing.**
- [x] **Flow/positioning cross-read present per candidate** (§C in every section), with the axis that
      produced each tag named, per `C29`.
- [x] **`BET_SHEET.md` written as ONE file** with per-sector sections.
- [x] **Every set-aside name goes to a ledger with a class and both required fields** — `TSLA`
      (`K.본문반증`) to the rejection ledger, `RSG` (`Q.확신부족`) to the missed ledger; written by
      this stage (see §LIVE). **Names whose stored conditions have come true are surfaced**: `MRK`
      (both legs satisfied → ALPHA resolves `entered`) and `VST` (the 0.003 OBV leg its reaffirmation
      rested on has moved to +0.207) — **surfaced, not overturned here** (`D463`).
- [x] **No name was removed on narrative grounds alone while its measured flow still passed.**
      `TSLA` is dropped on **three measured axes** (sector `eqflow` −0.251 with 21/28 negative, rs60
      −13.4, and a body-read that refutes its own headline) — not on the thread going quiet.
      `RSG` is dropped on a **measured** contradiction (a new-🟢 on a **negative** Δ).

---

# §B-TAGS — filled by Stage 10 / L1·ALPHA (2026-09-05)

> The §B placeholders above are resolved here. **Every tag carries its evidence label and date.**
> **Analytical output only — no sizing, no buy/sell language (P4).**

## §B-0 · The gate's own health, checked BEFORE any freshness verdict is issued

🚨 **`G1` FAILED on the sweep axis (`vel_coverage` 16.39%), and the stage rule says a failed `G1`
bars a freshness verdict.** ⇒ **The falsification probe was run, and it is what re-opens the gate:**

| probe | result |
|---|---|
| pre-sweep, 6 named queries | **6 / 6 alive** (`NVIDIA` 4,102 · `Apple` 1,299 · `Tesla` 822 · `삼성전자` 1,565 · `SK하이닉스` 1,165) |
| immediately post-sweep | **0 / 4** — `URLError` on the endpoint |
| recovery clock, same query | ❌ t+0s · ❌ t+20s · ❌ t+40s · ✅ **t+60s** · ✅ t+80s · ✅ t+100s (identical count) |
| sweep coverage shape | universe positions **0–48** and **nothing from 49 to 299**, zero exceptions |

⇒ **The zero is the INSTRUMENT, and it is self-inflicted**: the sweep's own burst trips the tunnel at
~49 names / ~98 queries and then hammers a dead endpoint that needs ~60 idle seconds. **The pipe is
alive; this desk knocks it down** (`D502`).
✅ **Consequence for this stage, stated exactly:** **no freshness number below comes from the sweep**,
and **every one comes from a direct `theme-age` / `fts` call made outside a sweep burst** — which
`PREFLIGHT §G1` explicitly permits and names as the required path. **The gate is open on the direct
path only.**

## §B-1 · Deterministic novelty first (`theme-age`, 90d, `--scope foreign`, direct calls)

| theme | verdict | age | 7d avg | **accel** | base | bet it serves |
|---|---|---:|---:|---:|---:|---|
| `brokerage` | ⚪ECHO | ≥90 | 133.9 | **1.51×** | 4,800 | `HOOD` |
| `HBM` | ⚪ECHO | ≥90 | 31.7 | 1.21× | 1,596 | `MU` |
| `nuclear power` | ⚪ECHO | ≥90 | 23.4 | 1.17× | 1,284 | `CEG` |
| `biotech` | ⚪ECHO | ≥90 | 46.0 | 1.00× | 2,690 | `ALNY`/`GILD`/`REGN`/`AMGN` |
| `refinery` | ⚪ECHO | ≥90 | 38.3 | 0.95× | 2,074 | `MPC`/`PSX` |
| `NAND` | ⚪ECHO | ≥90 | 23.3 | 0.91× | 1,456 | `STX`/`WDC`/`SNDK` |
| `merchant power` | ⚪ECHO | **57** | 0.6 | 0.71× | **32** | `VST` — ⚠ base 32, **thin** |
| **`distillate`** | ⚪ECHO | ≥90 | 17.4 | **0.64×** | 1,345 | `MPC`/`PSX` |
| `obesity drug` | ⚪ECHO | ≥90 | 2.3 | 0.54× | 230 | (`LLY`, not a candidate) |

★ **`M1323` [measured] — ZERO 🟢FRESH for a 12th consecutive foreign-feed measurement, and this run
can finally say the zero is arithmetic rather than an outage.** The gate needs **age ≤ 14 days AND
accel ≥ 2×**. **The youngest theme measured is 57 days.** ⇒ **a theme old enough to have a name is
structurally incapable of being FRESH**, which is `F1` stated as arithmetic. ⚠ **And the difference
from prior runs is that the pipe was falsified this time** (§B-0): all nine calls returned real ages
and real bases, so the zero is not a silent tunnel.

🚨 **`M1324` — the theme behind this run's strongest thesis is the most DECELERATING one on the
sheet.** `distillate` **0.64×** on a base of 1,345, alongside `refining margin` **0.66×** (third
consecutive run) and `refinery` **0.95×**. **Three independent narrative instruments agree the
refined-product story is draining while its physical print sits at the 95.6th percentile.**
⇒ **Every Energy tag below is capped at 🟡 for this reason alone** — an ⚪ECHO thesis needs *stronger*
live evidence to survive, and this one is ECHO **and decelerating**.

## §B-2 · Positioning read (`module_flow --positioning`, 2026-09-05)

| name | short %float · trend · DTC | P/C OI | IV skew | implied move (expiry) |
|---|---|---:|---:|---|
| **`MPC`** | 2.7% **BUILDING** DTC 2.9 | 1.19 | 🚨 **+41.5** | **±6.9%** (09-18, D13) |
| `PSX` | 1.4% covering DTC 1.9 | 1.20 | +0.1 | ±3.6% (09-11, D6) |
| `MU` | 2.7% covering DTC 0.7 | **2.20** | +10.9 | ±4.4% (09-09, D4) |
| **`STX`** | **4.1% BUILDING** DTC 1.5 | 🚨 **7.13** | −1.1 | **±7.1%** (09-11, D6) |
| `VST` | 3.3% covering DTC 2.0 | 0.29 *(complacent)* | −2.4 | ±4.3% (09-11, D6) |
| `CEG` | 3.0% covering DTC 3.4 | 0.32 *(complacent)* | +1.0 | ±4.9% (09-11, D6) |
| `MDT` | 1.1% covering DTC 2.0 | 0.25 *(complacent)* | +16.1 | ±2.8% (09-11, D6) |
| `MRK` | 1.0% covering DTC 2.8 | **0.06** | −9.1 | ±2.6% (09-11, D6) |
| `HOOD` | 4.2% covering DTC 1.8 | 0.84 | −6.2 | ±6.5% (09-11, D6) |
| `DE` | 1.9% covering DTC **5.1** | 1.00 | +4.1 | ±2.7% (09-11, D6) |

🚨 **`M1325` [measured] — the two names carrying this run's two strongest flow findings are the only
two with shorts BUILDING, and both carry an extreme option signature.** `MPC` (the promoted sector's
best OBV) has **shorts building at 2.7% of float with an IV skew of +41.5** — the highest downside
fear on the sheet by an order of magnitude. `STX` (the board's **#1 Δflow**) has **shorts building at
4.1% of float with put/call OI at 7.13**. **Everything else on the sheet is covering.**
⇒ **This is the sharpest adversarial reading in the run and it is stamped on both names below.**

★ **`M1326` — and this CORRECTS `M1305` from PREMORTEM, in the same run.** PREMORTEM measured
`SPY` ±0.5% / `SMH` ±1.8% (expiry **09-08**) and `XLE` ±1.6% (**09-09**) and concluded *"every
available straddle EXPIRES BEFORE both binaries… no threshold could be taken from the options
market."* **That is true of the three ETFs measured and NOT true in general**: every single name
above carries a **2026-09-11 expiry**, which **does** cover the CPI. **`M1305`'s scope was ETFs and
its wording was universal.** Corrected here, appended not edited (`D48`). ⚠ **The registered
thresholds are not changed** (`D242`) — they came from `D93` dispersion and stay there; what changes
is that a future name-level bracket **can** be checked against a real implied move.
⇒ **`S145`'s branch A (+6.825 on `EW{STX,WDC,AMD}` − `SMH`) sits at roughly `STX`'s own single-name
implied move (±7.1%)** — i.e. it is a threshold the options market considers a full-sized move, which
is the property a bracket is supposed to have. Stated now rather than discovered at scoring.

## §B-3 · The tags

| name | tag | evidence label + date | residual / stamp |
|---|:--:|---|---|
| **`MPC`** (held) | 🟡 **PARTIAL** | flow `SECTOR_FLOW_US.json` **09-04** (OBV +0.621 매집, rs20 +30.8) · crack `CL=F/HO=F/RB=F` settles **09-04** (distillate 95.6th pctile) · theme `distillate` **0.64× ECHO** 09-05 | **Residual: the narrative leg is absent and decelerating.** ⚠ **Momentum-only? NO** — RS *and* accumulation agree. ⚠ But the accumulation read is **C-grade (OBV only)**; the US has no investor-type feed, so it cannot be upgraded (`D6`). 🚨 **Positioning stamp: shorts BUILDING + IV skew +41.5.** 🚨 **Insider stamp: Form 144 at 4.2× its own base.** **Re-check 2026-09-14** (`P136`+`S147`) |
| **`PSX`** (held) | 🟡 **PARTIAL** | same, **09-04** · shorts **covering**, skew +0.1 | Same residual. Cleaner positioning than `MPC`. ⚠ Insider 144s at **2.9×** base. **Re-check 2026-09-14** |
| `VLO` | 🔴 **RESOLVED — already ledgered** | rejection 08-21 `H.밸류소진`, **reaffirmed 09-04** (price above consensus mean target) | **Not re-dropped.** A standing rejection with `--revives-if` and a recheck date already exists; a second row would double-count. Filed to the **missed** ledger this run instead (`M.숏리스트탈락`, recheck **09-19**) |
| **`MRK`** | 🟢 **LIVE** | `SECTOR_DEEP_HLTH` §Δ3/§Δ5 **09-05** — named as the Pharma node's best name with a driver · rs20 **+17.3** · OBV +0.185 매집 · shorts **covering**, P/C **0.06** | ★ **The ledger row's BOTH legs are satisfied and this stage resolves it: `entered`.** ⚠ **`obesity drug` theme is ⚪ECHO 0.54×** and `MRK`'s own theme is not FRESH — **the 🟢 here is the LEDGER-CONDITION verdict, not a `theme-age` FRESH verdict**, and the two are different objects. Stated so nobody reads a 🟢FRESH into it |
| `MDT` | 🟡 **PARTIAL** | flow **09-04** (the sector's only 🟢: +0.928, OBV +0.327, surge 1.47) · news velocity **2.01×** 09-05 | **Residual: it is the strong name inside the sector's WEAK node** (Health Care Equipment, `eqflow` −0.044, negative on both windows). ⚠ P/C 0.25 = complacent. **Re-check 2026-09-14** (`S133`) |
| `MU` | 🟡 **PARTIAL** | flow **09-04** (OBV +0.194 매집, Δ +0.231) · `HBM` **1.21× ECHO** 09-05 · contract terms FY26Q3 10-Q, read **2026-08-10** | 🚨 **Residual is a NUMBER, not a condition: the contracted share is `unknown` (`C3`)**, and until it is read the second-derivative regime evidence is not admissible on this node. ⚠ Chart shows **bearish divergence** against OBV 누적 +60%. **Re-check 2026-09-30** (its own print, `earnings_dates`) |
| **`STX`** | 🟡 **PARTIAL** | flow **09-04** (**Δ +0.728 = #1 of 299**) · screener leader-pullback **09-05** (RSI 31.2, at 50DMA, +43% over 200DMA) · `NAND` **0.91× ECHO** | ⚠ **MOMENTUM-ONLY FLAG: RS/Δ are green and the accumulation axis is NEUTRAL (`obv_norm` +0.034), not accumulating.** Per `D6` this is a **C-grade disagreement ⇒ it downgrades to 🟡 and is reported as a disagreement — it does NOT by itself make this a tape trade.** 🚨 **Positioning stamp: shorts BUILDING 4.1% float, P/C OI 7.13.** **Hard-stop required.** **Re-check 2026-09-11** (`S145`) |
| `WDC` | 🟡 **PARTIAL** | flow **09-04** (Δ +0.718 = #2) | Same momentum-only flag (**OBV −0.042 중립/negative**), same C-grade downgrade, **hard-stop required**. **Re-check 2026-09-11** (`S145`) |
| `SNDK` | 🟡 **PARTIAL — already ledgered** | flow **09-04** (rs20 **+43.9**, OBV +0.351 매집) | Filed to the **missed** ledger this run (`Q.확신부족`) because the memory thread's direction body-read is **bearish** while the tape accumulates. **Re-check 2026-09-19** |
| **`VST`** | 🟡 **PARTIAL** | flow **09-04** (Δ +0.491, OBV +0.207 매집) · chart **09-05** (OBV +148%, bullish divergence, **ignition UNFIRED at `close > 151.17`**, price 149.30) · `merchant power` **0.71×, base 32** | ⚠ **Residual is a price level and it is 1.25% away.** ⚠ **Standing rejection** (08-14 `G.섹터중립`) reaffirmed 09-04 on an OBV cut missed **by 0.003**; today `obv_norm` is **+0.207**. **This stage does NOT overturn it** (`D463`) — it records that the leg has moved and hands it to a human. ⚠ theme base **32 is too thin to carry a freshness verdict** — said, not used. **Re-check 2026-09-14** (`S146`) |
| `CEG` | 🟡 **PARTIAL** | flow **09-04** (+0.644, OBV +0.188 매집, rs60 **+17.2**) · `nuclear power` **1.17× ECHO** | Residual: the lane has **no registry row, no price series, and no read filing** (`D416`/`D517`/`D516`). ⚠ P/C 0.32 complacent. **Re-check 2026-09-14** (`S146`) |
| 🚨 **`ETN`** (held) | 🔴 **RESOLVED — thesis, not position** | flow **09-04** (**−0.662 🔴분산**, rs20 −8.0) · chart **09-05** (OBV **분배 −63%**, RSI 30.5, NEUTRAL/CHOP) · lane peers all accumulating | **The AI-power *thesis* on `ETN` is dropped as a reason to add**, and it is **already ledgered** — no new row is written because `S146` (09-14) is the registered scoreable object and a rejection row would duplicate it. ⚠⚠ **This is a THESIS verdict on a HELD name. It is not a sell, not a size, not advice (P4)** — it is the book flag EVENT_ALPHA raised, carried to its conclusion and handed to the book desk |
| `HOOD` | 🟡 **PARTIAL** | flow **09-04** (🟢 +0.783, OBV +0.215 매집, rs20 **+31.3**, new-🟢) · `brokerage` **1.51× ECHO**, the sheet's highest accel · shorts **covering** 4.2% | **Residual: its sector (`FIN`) was promoted `UW→N` TODAY on two axes that had just reversed** — the verdict is one session old. ⚠ implied ±6.5%. **Re-check 2026-09-11** (`S142` + CPI) |
| `DE` | 🟡 **PARTIAL** | flow **09-04** (🟢 +0.911, OBV +0.176 매집, surge 1.44) | **Residual: it contradicts its own sector** (`INDU UW−`, 28🔴 of 50). ⚠ **DTC 5.1 — the highest days-to-cover on the sheet.** **Re-check 2026-09-19** |
| `CTVA` | 🟡 **PARTIAL — watch only** | flow **09-04** (🟢 +0.861, OBV +0.265 매집) | **Residual: `P102` settles Materials' "is it two names" question on 09-09** and a Materials candidate entering before that pre-empts the bracket. **Re-check 2026-09-09** |
| `TSLA` | 🔴 **RESOLVED — dropped + ledgered** | body-read **09-04**: Cybercab launch [13] → **NHTSA probe within 24h** [6] · rs60 **−13.4** · sector `eqflow` −0.251 | **Rejection row filed this run** (`K.본문반증`, `--revives-if` "rs60 turns positive vs SPY AND the NHTSA probe closes or CD `eqflow` turns positive", recheck **2026-09-19**). ⚠ `robotaxi` is **1.95× ECHO** — the *theme* is the sheet's second-most-accelerating, and the name still fails on three measured axes. **A hot theme is not a tag** |
| `RSG` | 🔴 **no tag issued — MISSED, not rejected** | flow **09-04**: new-🟢 on a **NEGATIVE Δ (−0.091)** · ⚡ `[FINRA]` z **+2.61** | **Missed row filed this run** (`Q.확신부족`, recheck **09-19**). ⚡ **crowded-short is turn-conditional squeeze fuel, never a standalone read — hard-stop stamp if it is ever revisited** |

**Tally: 🟢LIVE 1 · 🟡PARTIAL 11 · 🔴RESOLVED 3 · no-tag-and-ledgered 1.**
⚠ **The single 🟢 is a LEDGER-CONDITION resolution (`MRK`), not a `theme-age` FRESH verdict** — the
FRESH gate issued **zero** for a 12th run and §B-1 says why in arithmetic.

## §B-4 · Carry-forward list — tags follow the NAME, not the sector's turn

Measured origin: `006360` carried an ALPHA tag with +64.40% consensus upside, its sector rested, and
**+12.3% over five sessions went untracked.** ⇒ **every tagged name below is handed to the next run's
inheritance packet regardless of whether its sector holds a DEEP slot**, each with its re-check date:

**09-09** `CTVA` · **09-11** `STX`, `WDC`, `HOOD` · **09-14** `MPC`, `PSX`, `MDT`, `VST`, `CEG` ·
**09-19** `SNDK`, `DE`, `VLO`, `TSLA`, `RSG` · **09-30** `MU`.
**Also carried:** `ETN` (🔴 thesis verdict on a **held** name — `S146` settles 09-14) and `MRK`
(🟢, resolved `entered`).

## §B-5 · Ledger writes by this stage

**Zero new rows.** Every drop and every no-tag on this sheet was **already written at its own stage**
— `TSLA` and `RSG` at BET, `MP` / the `NVDA`-thread at EVENT_ALPHA, `VLO` / `SNDK` / `VST` at
EVENT_ALPHA. ⇒ **ALPHA writes nothing rather than duplicating**, and says so instead of leaving a
silent gap.
⚠ **`ETN`'s 🔴 is deliberately NOT ledgered**: `S146` (09-14) is a **registered scoreable bracket** on
exactly that question, and a rejection row would be a second, weaker record of the same thing.

## ✅ EXIT CHECK — ALPHA

- [x] **Every §B tag filled with an evidence label and a date** (§B-3, 16 rows). **Every 🔴 is
      dropped AND ledgered with a reason class, a `--revives-if` and a `--recheck-date`** — `TSLA`
      written this run; `VLO` and `ETN` are covered by an existing row / an existing registered
      bracket respectively, **and the reason for not writing a duplicate is stated** (§B-5).
- [x] **Every 🟡PARTIAL carries an explicit re-check date**, and §B-4 lists **every** tagged name for
      carry-forward **independently of its sector's DEEP slot** — the `006360` failure mode.
- [x] **Momentum-only and positioning flags stamped where they apply** — `STX` and `WDC` carry the
      momentum-only flag with the `D6` **C-grade downgrade** stated explicitly (a C-grade
      disagreement demotes to 🟡; it does not by itself convert a bet into a tape trade); `RSG`
      carries the ⚡crowded-short hard-stop stamp; `MPC` and `STX` carry the shorts-BUILDING stamp.
- [x] **(US) `ACTION_TICKETS.md` written** — `action_bracket` produced both-sides PPI tickets
      (`D294` **did not reproduce**, first clean run in 8) and ALPHA appended the six registered
      information brackets, the `action_bracket`-vs-PREMORTEM disagreement (`D518`), and the two
      cycle observations that stand in for a core-starter the GAP flag did not trigger.
- [x] 🚨 **The `G1` gate was falsified before any freshness verdict was issued** (§B-0) — the zero is
      shown to be the instrument on the sweep path and arithmetic on the direct path, and the two are
      separated rather than conflated.
