# SECTOR_DEEP_FIN — Financials · industry_US · 2026-08-04 · **CONTINUOUS track → DELTA ONLY**

> Structure carried **by reference** to `llm_outputs/2026-08-03/industry_US/SECTOR_DEEP_FIN.md`.
> The value-chain map is **not** re-printed. Benchmark is **SPY, inline** on every relative number (**C1**).
> **P4 — analytical only.** No position language, no sizing, no entry/exit anywhere in this file.
> Prices: yfinance, **settled bar 2026-08-03** (the live 08-04 bar is excluded, D74). Rates/credit: `[FRED]`, **settled 2026-07-31** (nominals publish one business day behind; **D139** holds again this run — VIX and T10YIE have 08-03 prints, DGS2/DGS10/DGS30 do not).

---

## 0 · The one-line answer: is one leg enough?

**No — and this run does not have to argue it as a judgement, because the leg fails two measurements that were run against it directly.**

**(a) The leg cannot resolve on the date it is scheduled to resolve.** Its two registered thresholds, measured against the full 1-year distribution of the derived 2s10s:

| Registered observable | Line | Sessions in last 249 that satisfy it | 5-day move required from +0.47 | Base rate of that 5-day move (1y) |
|---|---|---|---|---|
| **S23** — flattener breaks the mechanism | **≤ +0.20** | **0 of 249 (0%)** | **−27bp** | **0 of 244 (0.0%)** — all-year max 5d flattening is **−13bp** |
| **S51 branch A** — steepener confirms it | **≥ +0.35** | **235 of 249 (94%)** | +0bp (already satisfied) | — (satisfied unless −12bp, **2.0%**) |

⇒ ★★ **Between them, S23 and S51-A bracket a region containing 94% of the past year.** One threshold has never been touched; the other is satisfied on ~19 of every 20 sessions. **On the 08-07 close, this pair produces approximately zero bits of information about the mechanism.** Stated positively: **the leg needs a falsifier inside its own observed distribution before the print can mean anything** — §7 registers one, calibrated.

**(b) The leg's transmission is unmeasurable in the names the tilt is expressed in.** Over 60 settled sessions to 08-03, regressing each name's SPY-excess return on Δ`DGS2` and Δ`2s10s` jointly (§2): **all 9 banks, plus KRE and XLF, have a slope beta statistically indistinguishable from zero** (|t| ≤ 1.5, R² ≤ 0.05 for every one) (**C4**). The slope beta that *is* significant sits in **exchanges / market-data / payroll** — the sub-node this desk resolved 🔴 — and those names carry a **level** beta of comparable size, which is precisely what makes the S51-A-BULL branch bite.

**So the honest formulation is not "the OW− fails" — DEEP does not set the tilt.** It is: **as currently instrumented, Financials has zero legs that both (i) can resolve on their scheduled date and (ii) transmit to the names the tilt is held in.** §7 and §8 hand BET the repaired instruments rather than a verdict.

⚠ **C2, the half that argues the other way:** the *direction* is real and is not being denied. 2s10s went **+0.34 (07-27) → +0.47 (07-31), +13bp in 4 sessions**, which is a **99th-percentile 5-day steepening** (1y P99 = +10bp). The defect is in the measuring instrument, not in the observation.

---

## 1 · The slope leg, measured (P13′ / S23 / S51)

**Derivation stated as a choice (C5): 2s10s ≡ `DGS10 − DGS2`, both nominal constant-maturity, no interpolation.** `[FRED]`

| Date (settled) | DGS2 | DGS10 | **2s10s** | DGS30 | 30s10s |
|---|---|---|---|---|---|
| 2026-07-27 | 4.31 | 4.65 | **+0.34** | 5.12 | +0.47 |
| 2026-07-28 | 4.26 | 4.61 | +0.35 | 5.09 | +0.48 |
| 2026-07-29 | 4.22 | 4.67 | +0.45 | 5.20 | +0.53 |
| 2026-07-30 | 4.23 | 4.68 | +0.45 | 5.21 | +0.53 |
| **2026-07-31** | **4.28** | **4.75** | **+0.47** | **5.27** | **+0.52** |

**Confirmed against the prompt: +0.47 at the settled 07-31 close.** ⚠ **S1 binds — this is 5 dates, not 5 weeks**, and the 08-03 nominal is unpublished, so **no new curve information has arrived since 07-31** (**C3**).

★★ **The delta this run adds, which prior runs did not compute: the LEVEL of the leg, not just its direction.**
**2s10s at +0.47 sits at the 19th percentile of the trailing year** (1y range **0.27 – 0.74**; **25th pct 0.50, median 0.54, 75th 0.59**). ⇒ **The curve is in its bottom quartile of the past year.** The "steepener" the tilt rests on is a **13bp bounce off the 4th percentile (+0.34 on 07-27)**, not a move into steep territory. **Both halves stated (C2): the 4-session *change* is a 1y-P99 event; the resulting *level* is a bottom-quintile reading.** Which of those two the mechanism needs is the unresolved question, and the desk has never written down which — **that is the specification gap, and it is why "the carrier changed three times" (M317) keeps happening.**

**W3 / M138 carried unsoftened.** The NII leg's migration is not re-litigated here and nothing this run found reverses it: **WFC held FY26 NII ~$50B and missed at $12.32B (+5% YoY) on interest-bearing deposit mix; JPM raised to ~$105.5B on markets-related NII.** §2's regression is the independent confirmation from the price side — **WFC's slope beta is +1.97 (t +0.2) and JPM's is −2.24 (t −0.3)**, i.e. the two banks that made the guidance statements both show **no measurable slope transmission at all.**

---

## 2 · Level vs slope — which names separate them (the S51-A-BULL question)

**Method, stated as a choice (C5):** for each ticker, OLS of daily **SPY-excess log return** on **Δ`DGS2`** and **Δ`2s10s`** (in percentage points), **60 settled sessions ending 2026-08-03**. Reparameterising Δ`DGS10` = Δ`DGS2` + Δ`2s10s` makes `b_lvl` the response to a front-end move **holding slope fixed** and `b_slp` the response to a steepening **holding the 2y fixed**. Units: **excess-return % per +100bp**. `corr(Δ2y, Δslope) = −0.48` (1d) / **−0.33 (5d)** — the regressors are negatively correlated but **not collinear**, so the two coefficients are separately identified; they are, however, jointly estimated and should be read as a pair (**C3**).

**Scenario columns.** `bull_stp` = Δ2y **−15bp**, Δslope **+10bp** (Lens 2's branch). `bear_stp` = Δ2y **0bp**, Δslope **+10bp** (the variety the NIM mechanism needs).

### 2a · The significant loaders — none of them is a bank

| Ticker | node | **b_lvl** | t | **b_slp** | t | R² | **bull_stp %** | bear_stp % |
|---|---|---|---|---|---|---|---|---|
| **CME** | Exchange | **+26.31** | **+4.2** | **+45.03** | **+4.3** | 0.30 | **+0.56** | +4.50 |
| **NDAQ** | Exchange | +9.67 | +1.7 | **+33.22** | **+3.4** | 0.17 | **+1.87** | +3.32 |
| **ADP** *(not GICS Financials)* | Payroll/float | **+20.05** | **+2.9** | **+29.76** | **+2.5** | 0.15 | **−0.03** | +2.98 |
| **ICE** | Exchange | +10.34 | +1.9 | **+27.97** | **+3.0** | 0.14 | **+1.25** | +2.80 |
| **MRSH** | Ins. broker | **+13.83** | **+2.0** | **+24.03** | **+2.1** | 0.09 | +0.33 | +2.40 |
| **SCHW** | Brokerage | **+17.49** | **+3.2** | **+20.29** | **+2.2** | 0.16 | **−0.59** | +2.03 |
| **V** | Payments | **+11.23** | **+2.4** | **+18.29** | **+2.3** | 0.11 | +0.14 | +1.83 |
| **PGR** | P&C | **+18.39** | **+2.4** | +18.01 | +1.4 | 0.09 | **−0.96** | +1.80 |
| **ALL** | P&C | **+17.90** | **+2.6** | +17.66 | +1.5 | 0.11 | **−0.92** | +1.77 |
| **MET** | Life | +9.11 | +1.9 | **+17.28** | **+2.1** | 0.09 | +0.36 | +1.73 |
| **CB** | P&C | **+18.01** | **+3.0** | +15.55 | +1.5 | 0.14 | **−1.15** | +1.55 |
| **AFL** | Life | **+14.67** | **+3.1** | **+15.44** | **+2.0** | 0.15 | **−0.66** | +1.54 |
| **AIG** | Multi-line | **+11.81** | **+2.2** | +14.88 | +1.6 | 0.08 | −0.28 | +1.49 |
| **HIG** | P&C | **+13.72** | **+2.5** | +13.97 | +1.5 | 0.10 | **−0.66** | +1.40 |
| **MA** | Payments | **+9.98** | **+2.0** | +15.72 | +1.8 | 0.08 | +0.08 | +1.57 |
| **BRK-B** | Multi-sector | **+8.58** | **+2.4** | +10.06 | +1.6 | 0.09 | −0.28 | +1.01 |
| **GS** | IB | **−12.05** | **−2.1** | −15.22 | −1.5 | 0.07 | +0.29 | **−1.52** |
| **XYZ** | Payments | **−23.44** | **−3.7** | −14.35 | −1.3 | 0.20 | **+2.08** | **−1.43** |

### 2b · The banks — the result that matters

| Ticker | b_lvl | t | b_slp | t | R² |
|---|---|---|---|---|---|
| JPM | +1.66 | +0.4 | **−2.24** | **−0.3** | 0.01 |
| BAC | +2.37 | +0.6 | +5.90 | +0.8 | 0.01 |
| WFC | +4.19 | +0.8 | +1.97 | +0.2 | 0.01 |
| C | −0.16 | −0.0 | −12.14 | −1.5 | 0.05 |
| USB | −0.96 | −0.2 | +4.37 | +0.5 | 0.01 |
| PNC | +3.20 | +0.7 | +7.01 | +0.9 | 0.02 |
| TFC | −4.27 | −0.8 | +2.93 | +0.3 | 0.02 |
| FITB | −1.68 | −0.3 | +3.04 | +0.4 | 0.01 |
| HBAN | −4.17 | −0.9 | +1.96 | +0.2 | 0.02 |
| **KRE** *(regional ETF)* | −2.28 | −0.6 | +6.45 | +0.9 | 0.04 |
| **XLF** *(sector ETF)* | +4.60 | +1.5 | +6.54 | +1.2 | 0.04 |

★★ **Every one of the 11 is indistinguishable from zero on both axes (C4).** The R² column is the honest summary: **1–5% of these names' SPY-excess variance is explained by the entire nominal curve.** ⇒ **The mechanism the Financials OW− rests on has no measurable price transmission to the bank complex over the last 60 sessions.** That is an independent, price-side arrival at the same place M138 reached from the guidance side.

⚠ **C2 — the half that argues the other way:** a 60-day window with 4.5bp/day of DGS2 variation has low power; **absence of a measurable beta is not proof of no mechanism**, and NIM transmits with a lag no lag-table on this desk covers (**W2 / C3, unchanged from 08-03**). The 120-day window was also run and does not overturn any sign or significance call above.

### 2c · ★★ Which names separate LEVEL from SLOPE — and the answer to Lens 2

**Slope-dominant (slope significant, level not; `b_slp / b_lvl` ≈ 3×):** **NDAQ (33.2 / 9.7 = 3.4×)** and **ICE (28.0 / 10.3 = 2.7×)**. Adding the insignificant-but-directionally-clean: MSCI (2.9×), MCO (2.6×), CME (1.7×), **KRE (b_lvl −2.3, b_slp +6.5 — the only name in the set with a *negative* level beta and a positive slope beta, though both are indistinguishable from zero)**.
**Level-dominant (level significant, slope not):** **TRV (9.2 / 0.7 = 13×)**, **CB (1.16×)**, **PGR (1.02×)**, **ALL (1.01×)**, **HIG (0.98×)**, **AFL (0.95×)**, **SCHW (0.86×)**.

★★★ **The S51-A-BULL adjudication.** Under Lens 2's branch (Δ2y −15bp, Δslope +10bp), the **ten worst-positioned names in the 51-ticker set are, in order: TRV −1.31, C −1.19, CB −1.15, PGR −0.96, ALL −0.92, AFL −0.66, HIG −0.66, SCHW −0.59, JPM −0.47, WFC −0.43** — **six of the eight worst are P&C/life insurers.** The ten best-positioned are **XYZ +2.08, NDAQ +1.87, PYPL +1.78, TRI +1.68, ICE +1.25, KRE +0.99, TFC +0.93, BX +0.86, COIN +0.85, HBAN +0.82** — **led by exchanges and payments.**

⇒ ★★ **Lens 2's failure mode is not merely real; it is inverted against the carrier the desk named 24 hours ago.** The **08-03 file named the insurance/custody node as the OW's carrier**. Under S51-A-BULL, **that node is the worst-positioned group in the sector, and the exchanges node the desk resolved 🔴 is the best-positioned.** **A branch that scores "with the tilt" while the tilt's own named carrier takes the loss is exactly the defect Lens 2 registered — and it has now been quantified rather than asserted.**

**Base rates, so the branch is weighted rather than feared (1y, 244 overlapping 5-day windows):**

| Branch | Definition (5d, 07-31 → 08-07) | Occurrences | Base rate |
|---|---|---|---|
| **Bull steepener (S51-A-BULL)** | Δ2y ≤ −15bp **and** Δslope > 0 | **4 / 244** | **1.6%** |
| **Bear steepener (mechanism-consistent)** | Δ2y ≥ 0 **and** Δslope > 0 | **50 / 244** | **20.5%** |
| Δ2y ≤ −15bp in a **single** session | — | **0 / 248** (1d min **−12bp**, σ 4.5bp) | **0.0%** |

⇒ **The qualifier is correctly registered and correctly low-probability — ~1/13 the frequency of the bear variety.** ⚠ **Specification gap the qualifier must close (C3):** as written, *"DGS2 has fallen ≥15bp from 4.28"* does not say over what horizon. **Single-session: 0/248 precedent. Cumulative 07-31→08-07: 4/244 = 1.6%.** BET should read it as the **cumulative** version; the single-session version is unfalsifiable-by-construction and would repeat the S23 error.

---

## 3 · Sub-node dispersion re-measured (M40 / M136, C5 stated)

**★ C5 — the grouping is a choice, not a fact.** Prior run's partition (banks n=9 · capital markets n=5 · payments+insurance n=16 · other n=17) is **re-stated and re-used unchanged for comparability**, and its arbitrariness is named: **"other" (n=17) is a residual bucket containing asset managers, custodians, exchanges, consumer finance and BRK-B**, which is why it is the second-largest gross-flow contributor. Any conclusion below that depends on the boundary between "other" and "payments+insurance" is **not robust.**

Sector, `asof 2026-08-03 settled`: **n=47 · wflow +0.093 · eqflow +0.101 · 4🟢 / 7🔴 · breadth 0.09 · delta −0.121** — **4th of 11 sectors on wflow.**

### 3a · M40 — **HOLDS**

| Group | n | % of names | gross **+** flow | % of sector gross+ | eqflow | **× sector eqflow** |
|---|---|---|---|---|---|---|
| **payments + insurance** | 16 | **34.0%** | 5.076 | **42.9%** | **+0.242** | **2.39×** |
| other *(residual)* | 17 | 36.2% | 5.017 | 42.4% | +0.136 | 1.35× |
| banks | 9 | 19.1% | 1.385 | 11.7% | +0.038 | 0.38× |
| **capital markets** | 5 | 10.6% | 0.350 | **3.0%** | **−0.354** | **−3.49×** |

⇒ **M40 holds on fresh data: 34.0% of names / 42.9% of gross positive flow / 2.39× the sector mean** (prior: 34% / 45% / 2×). ⚠ **C2 — the half that weakens it:** the *concentration* multiple is only **1.26×** (42.9% of flow on 34.0% of names), and the residual "other" bucket produces **almost identical gross flow (42.4%) from 36.2% of names**. **The claim that survives is "payments+insurance has the highest per-name flow"; the claim that does not survive is "payments+insurance is where the sector's flow is concentrated."**

### 3b · M136 — **HALF BROKEN**, and the break is the informative half

12 sub-industries, mean flow spanning **+0.562 to −0.354 = 0.916 range ≈ 9× the sector's own eqflow (+0.101)** (**W5**):

| Sub-industry | n | eqflow | RS20 vs SPY | RS60 vs SPY |
|---|---|---|---|---|
| Life & Health Insurance | 3 | **+0.562** | +5.6 | **+15.0** |
| Asset Mgmt & Custody | 7 | +0.359 | +7.0 | +7.2 |
| Transaction & Payment Proc. | 4 | +0.275 | +9.6 | +14.7 |
| Property & Casualty Ins. | 5 | +0.246 | +0.8 | +10.1 |
| Multi-Sector Holdings (BRK-B) | 1 | +0.119 | +0.4 | +6.0 |
| Diversified Banks | 7 | +0.076 | −0.2 | +7.0 |
| **Insurance Brokers** | 3 | +0.046 | +2.4 | **+16.6 (best)** |
| Consumer Finance | 2 | −0.033 | +0.3 | +6.6 |
| **Financial Exchanges & Data** | 7 | **−0.035** | +0.2 | **−5.9 (worst)** |
| Regional Banks | 2 | −0.091 | −3.2 | +4.9 |
| Multi-line Insurance | 1 | −0.285 | −3.3 | −1.8 |
| **Investment Banking & Brokerage** | 5 | **−0.354 (lowest)** | −7.6 | +6.5 |

- **The IB half HOLDS**: Investment Banking & Brokerage is still **lowest flow (−0.354)** with a **positive RS60 (+6.5)**.
- ★ **The exchanges half BROKE**: exchanges were the **highest**-flow sub-node; they are now **9th of 12 at −0.035** while still holding the **worst RS60 (−5.9)**. ⇒ **M136's "mirror image" framing is retired as of this run** — it is now simply *"the worst RS60 node also has weak flow"*, which is not a mirror image and carries no tension.
- **The reason the exchanges node broke is internal dispersion, not a level shift**: within n=7, **ICE +0.811 → MSCI −0.726, a 1.537 range** — the widest intra-sub-industry spread in the sector. **ICE is the single highest-flow name in all 47 Financials; four of the other six exchanges are 🔴** (SPGI −0.519, MCO −0.568, MSCI −0.726, COIN −0.334). ⇒ ★ **"Exchanges" is not a usable unit of analysis this run; the node's headline is one name.**

**W5 restated at sector level, unchanged in force from 08-03: "Financials" remains the wrong unit.** Spread across the 47 names runs **ICE +0.811 to C −0.783**.

### 3c · R32 re-tested — the sign did **not** flip this run, and that is not a rehabilitation

**Convention stated (C5): `gap ≡ eqflow − wflow`; positive = breadth-led. (ROTATION's `−0.008` is the same statistic under the opposite convention, `wflow − eqflow`.)**

| Cut | wflow | eqflow | **gap (eq − w)** |
|---|---|---|---|
| all 47 | +0.0927 | +0.1014 | **+0.0087** |
| ex-BRK-B (n=46) | +0.0884 | +0.1010 | **+0.0126** |
| ex top-2 by mcap (BRK-B, JPM) | +0.0497 | +0.0957 | +0.0460 |
| ex top-5 (BRK-B, JPM, V, MA, BAC) | **−0.0182** | +0.0823 | **+0.1005** |

Three-run series of the all-47 gap: **+0.0214 (R32's original) → +0.0370 (08-03, M316) → +0.0087 (this run)**; ex-BRK-B: **−0.0166 → +0.0095 → +0.0126**.
⇒ ★ **The sign is stable this run and no longer flips on removing BRK-B — but the magnitude has collapsed to +0.0087 on an eqflow of +0.1014, i.e. 8.6% of the level, and the all-47 statistic has now taken values of −0.0166, +0.0095, +0.0214, +0.0370 and +0.0087 across five measurements.** **"Breadth-led" is not rebuilt as a reason here (R32 stands).** The correct statement is **C4: on this run's data the breadth-led and mega-cap-led readings are indistinguishable** — both wflow and eqflow are near zero, and **stripping the five largest names drives wflow negative (−0.018)**, which is the only durable fact in the table: **BRK-B is 13.94% of a $7,573.9bn sector at a flow score of +0.119, and JPM is another 11.51%.**

---

## 4 · M135's replacement observable on the settled 08-03 bar

**M135 is the defect I own, and this run found that its replacement inherited the original's disease.**

**Registered replacement:** equal-weight excess of **{NDAQ, SPGI, ICE, CME, MCO, MSCI, COIN}** vs **SPY**, recorded as **−3.00pp (07-24) → +3.17pp (07-27)**.

★★ **That pair is not reproducible from settled prices under any fixed-window or fixed-base derivation, and the reason is arithmetic:** 07-24 (Fri) → 07-27 (Mon) is **one trading session**, and **the basket's single-session equal-weight excess on 07-27 was +2.80pp** — **less than half the +6.17pp the recorded pair implies.** No window ending on those two dates can move by more than that basket's own one-day excess unless **the window itself changed between the two readings.** ⇒ **The replacement observable was measured with an advancing base date — the exact defect it was created to fix.** ⚠ **C3: the derivation was never written down, so this is diagnosed, not accused.** Stated positively: **the fix is to write the window into the register**, done below.

**Fully specified and re-measured, so it is reproducible from here (C5 — the window is a choice, all five are given):**
EW basket = simple mean of the 7 names' simple % price change (auto-adjusted close, yfinance), minus SPY's over the same window, **windows counted in trading sessions ending at the stated settled bar**.

| asof (settled) | 10d | 20d | 40d | 60d | 90d |
|---|---|---|---|---|---|
| 2026-07-24 | +2.84 | +11.21 | −0.55 | −8.82 | −14.77 |
| 2026-07-27 | +3.42 | +11.81 | +1.70 | −5.61 | −13.08 |
| 2026-07-29 | +3.77 | **+16.02** | +3.51 | −2.78 | −11.96 |
| 2026-07-31 | −1.88 | +1.63 | +3.72 | −6.35 | −16.84 |
| **2026-08-03** | **−3.53** | **+0.24** | **+1.52** | **−5.92** | **−15.33** |

★ **The reading on the settled 08-03 bar: 20d +0.24pp · 60d −5.92pp · 90d −15.33pp.**
⇒ **The 20d excess has fully decayed — +16.02pp (07-29) → +0.24pp (08-03), a 15.8pp give-back in three sessions**, driven by daily excesses of **−1.51 (07-30), −3.00 (07-31), −1.21 (08-03)**. ★ **On every window of 60 sessions or longer the node has been and remains a negative-excess node.** This is the same conclusion §3b reached from flow and RS60 (−5.9), by an independent route, and it is **consistent with Lens 3's EXHAUSTED tag on ICE.**

**Recommended register wording for BET (positive form): *"M135-R: EW excess of the 7-name exchange/data basket vs SPY over a fixed 60-session window ending at the settled bar; value on 2026-08-03 = −5.92pp; re-read on the same 60-session convention."*** Naming the window is what makes it re-readable.

⚠ **M152 acknowledged: ICE, C, GS, MA, MET, MS, V, ALL and AIG are silently unindexable by `module_report_tags`.** **No news-coverage or zero-coverage claim is made anywhere in this file** — `module_report_tags` was not used, so M152 constrains nothing here beyond forbidding an inference I did not make.

---

## 5 · The insurance / exchanges node the wide sweep surfaced, with Lens 3's re-tags

**Re-measured independently on the settled 08-03 bar, SPY benchmark inline (C1).** `share` = RS20 / RS60; `seg 21-60` = RS60 − RS20 (the base built *before* the last 20 sessions). FINRA short-vol z re-run by me today, `date 2026-08-03`.

| Ticker | in FIN 47? | flow | RS5 | RS20 | RS60 | **seg 21-60** | **share** | short z | Lens 3 tag | **My verdict** |
|---|---|---|---|---|---|---|---|---|---|---|
| **MET** | ✅ | +0.744 🟢 | −1.3 | +5.6 | **+17.6** | **+11.9** | **32.0%** | **−1.55** ✅ | EXT-BUT-LIVE | **CONFIRMED** — base built before the last 20d, RS5 only −1.3 |
| **TRV** | ✅ | +0.713 🟢 | **−6.7** | +9.4 | **+21.0** | **+11.6** | **44.7%** | **−3.34** ✅ | round-tripped from EXHAUSTED (M149, 07-24) | **CONFIRMED** — the round-trip reproduces (Lens 3 had RS5 −6.8; I get **−6.7**) |
| **MRSH** | ✅ | +0.709 🟢 | +2.7 | +10.1 | +14.8 | **+4.7** | 68.5% | **+2.01 ⚡** | *(untagged)* | ★ **thinnest base of the four** — seg +4.7 vs MET +11.9; not exhausted, but **not a base** |
| **ICE** | ✅ | **+0.811 🟢 (#1 of 47)** | −0.4 | +11.7 | **−4.2** | **−15.9** | n/m | **+2.74 ⚡** | EXHAUSTED (denominator n/m) | **CONFIRMED** — Lens 3 had seg −14.4; I get **−15.9**, same sign and order |
| **TRI** | ❌ *(not GICS Fin)* | +0.87 🟢 | +1.4 | **+14.8** | +8.1 | **−6.7** | **183.4%** | +1.61 ⚡ | EXHAUSTED | **CONFIRMED** — Lens 3 had seg −6.2; I get **−6.7** |
| **ADP** | ❌ *(not GICS Fin)* | +0.73 🟢 | +3.3 | +11.8 | **+27.7** | **+15.9** | 42.6% | +0.34 | *(untagged)* | ★ **the strongest base on the shortlist**, and it is **not a Financials name** |

★ **Two structural facts about the shortlist that the sweep's framing obscures:**
1. **Only 4 of the 7 shortlist names are GICS Financials.** TRI, ADP and BMY are not. **A "Financials node" read off this shortlist is reading a cross-sector shortlist** (**C5** — the sector attribution is the sweep's grouping choice, not a property of the names).
2. ★★ **The node splits cleanly along the §2c axis, and the split is the same one.** **MET / TRV** are **level-dominant** (TRV b_lvl 9.23 vs b_slp 0.71 — the most level-pure name in the 51-ticker set). **ICE / NDAQ** are **slope-dominant** (2.7×–3.4×). ⇒ **The node the sweep surfaced contains both sides of the S51-A-BULL trade simultaneously**, which is why "the insurance node carries the OW" and "S51-A confirms the OW" cannot both be safe statements about the same print.

⚠ **D6 — signal grade, binding.** Flow tags (🟢/🔴), OBV states and FINRA short-vol z are **grade B/C: positioning context only, never a carrier.** **The US desk has NO investor-type feed; FINRA short-vol z is a PROXY and cannot be read as "foreigners/institutions did X."** MET's −1.55 and TRV's −3.34 are consistent with short pressure leaving; MRSH +2.01, ICE +2.74 and TRI +1.61 are consistent with crowded-short. **None of these is evidence of the rate mechanism**, which is the only thing §0–§2 turn on.

★ **The one contradiction worth naming rather than smoothing: GS.** Flow **−0.485 🔴**, OBV **분산**, RS20 **−3.5** — yet short-vol z **−1.92 (🟢 pressure leaving, 5v5 −14.9▼)**, and it is the only name in the sector with a **statistically significant level beta that is negative (b_lvl −12.05, t −2.1)**. **Distribution on the tape, short covering in the positioning proxy, and an inverted rate sign — three readings that do not compose.** **Stated as unresolved (C3)** rather than resolved toward whichever one supports a story.

**HSBC / Dimon / Fitch — §5 of the brief, body-read:**

★★ **HSBC H1 corroborates the LEVEL leg and the FEE leg. It does not corroborate the SLOPE leg — and it independently re-confirms M138's migration on a second continent.** From the bodies `[cnbc · independent · cna, 2026-08-04]`:
- **PBT +23% YoY to $19.5bn; attributable profit +27% to $14.6bn; Q2 PBT $10.1bn vs $9.51bn cons.; Q2 NII +9% YoY to $9.29bn; FY NII guidance raised to exceed $46bn; RoTE target held at 17%, reported ex-items 19.1%.**
- ★ **The attribution in the bank's own words is "higher net interest income and increased fee income, particularly from wealth management and banking services," with wealth revenue +18% YoY** — and the sector framing in the same body is **"a surge in trading activity and resilient interest income *despite dips in central bank rates*."** ⇒ **This is the JPM pattern, not the WFC pattern: earnings driven by fees, wealth and markets, explicitly described as resilient *against* falling policy rates.** **A bear steepener is not the stated driver anywhere in the print.**
- ⚠ **W3 binds hard — real ≠ profitable, and headline ≠ underlying.** The +23%/+60% headlines are **inflated by notable items of +$2.6bn net favourable including a one-off $1.3bn gain**, against **$200m of restructuring cost**. **The clean read is the +9% NII and +18% wealth, not the headline.**
- ★ **The print also carries a credit deterioration the headline hides: ECL $2.4bn, +$400m vs H1-2025**, itemised as **a $400m loss on a UK financial-sponsor fraud and $200m in Hong Kong commercial property.**
- ⚠ **C3 — transferability is limited and marked.** HSBC funds on BoE/HKMA curves and is Asia-weighted; **its read on the US 2s10s mechanism is analogical, not direct.** It is admissible as **a non-US primary reading the same *channel*** and is **not** admissible as a measurement of the US leg.

**Dimon `[6 outlets, 2026-08-04]`** — body: he *"wouldn't buy"* the S&P 500 or long-dated Treasuries, and argues **the 10y "should probably yield 4% to 4.5%, roughly where it already sits."** ⚠ **The observable contradicts the quoted anchor: DGS10 settled at 4.75 on 07-31, above his own stated fair range.** His stated preference is **short-term cash / short-duration** — i.e. **a statement about the long end that does not endorse a front-end rally**, which is **inconsistent with the S51-A-BULL branch and mildly consistent with the bear variety.** **D6/grade: this is a single named opinion, not an observable; it is reported, not weighted.**

**Fitch `[5 outlets]`** — AI-related corporate credit risk; Fitch estimates **AI-related investment added 1.4% to US Q1-2026 GDP growth** and flags a *"re-evaluation of long-run returns potential"* as the transmission to HY. Separately in the pool: ***"Fitch's Private Credit Default Rate Hit Record in Second Quarter"* `[bloomberg, 2026-07-30, title-only — body not retrieved, C3]`.** See §6 for how far these may be carried.

---

## 6 · Credit

`[FRED]`, settled **2026-07-31** (⚠ `ig_oas` returned a **502 on first call and succeeded on retry** — the value below is the retry, and the retry is the only reading, **C3**):

| Series | Level | Registered line | Distance | **1y percentile** | **20d change** |
|---|---|---|---|---|---|
| **HY OAS** | **2.85** | S26 **3.10** | **25bp** | **50th** (1y 2.63 – 3.46) | **+0.11 — WIDER** |
| **IG OAS** | **0.79** | S41 **0.90** | **11bp** | **46th** (1y 0.73 – 0.94) | **+0.04 — wider** |
| **NFCI** | **−0.554** | — | — | near **1y loosest (min −0.564)** | **6th consecutive week of loosening** (−0.497 six weeks ago) |

★ **The delta this run adds is the sign of the 20-day change, which the level readings hide.** Both spread series are at **mid-distribution, not tight** (HY exactly 50th percentile of its own year), and **both have widened over the last 20 sessions while NFCI loosened for a 6th week.** ⇒ ★ **Price-based credit and index-based financial conditions are pointing in opposite directions.** **C2 — both halves stated, neither suppressed:** the **level** reading is benign (25bp and 11bp of headroom to the registered lines, nothing triggered); the **direction** reading is mildly adverse (HY +11bp/20d).

⚠ **Binding rule applied literally.** Fitch's AI-credit report and the record private-credit default rate are **narrative-only** and are **labelled as such** — they cite neither HY OAS nor NFCI, and private-credit default rates are a different market from the HY index. **The only credit-stress claim this file makes with a citable observable is: HY OAS has widened 11bp over 20 settled sessions to 2.85, its 50th percentile.** HSBC's **+$400m YoY ECL with two named idiosyncratic losses** is a **single-issuer datapoint, not an index**, and is likewise narrative-only.

---

## 7 · Track KPIs · anti-signals · dates

| KPI | State (settled) | Anti-signal | Date |
|---|---|---|---|
| **P13′ / S23** — derived 2s10s | **+0.47** (19th pct of 1y; +13bp in 4 sessions = 1y-P99) | ⛔ **S23's ≤ +0.20 is BROKEN AS A TEST — 0 of 249 sessions, requires a −27bp 5d move vs an all-year max of −13bp** | 08-07 |
| ★ **S23-R — proposed repaired falsifier** | **2s10s ≤ +0.40** on a settled close | needs **−7bp/5d, base rate 9.0% (22/244), 12th pct of level** — **inside the observed distribution, so it can actually fire** | 08-07, then weekly |
| ★ **S51-A-R — proposed repaired confirm** | **2s10s ≥ +0.54** (the 1y median) | needs **+7bp/5d, base rate ≈5%**; **the registered ≥ +0.35 is satisfied on 94% of the past year and is near-tautological** | 08-07 |
| **S51-A-BULL** (Lens 2's qualifier) | **armed, and now quantified** | flag `S51-A-BULL` if at the settled 08-07 close **2s10s ≥ +0.35 AND DGS2 ≤ 4.13** (**cumulative from 4.28**, base rate **1.6%**; the single-session reading is **0/248** and must not be used) | **08-07** |
| ★ **Bank slope transmission** (new, this run) | **b_slp indistinguishable from zero for all 9 banks + KRE + XLF** (|t| ≤ 1.5, R² ≤ 0.05) | a re-run at 60d showing **any bank with |t| ≥ 2.0 on b_slp** would revive the bank-carrier leg | 08-11 |
| ★ **M135-R** — exchange/data EW excess vs SPY | **60d −5.92pp · 20d +0.24pp** (20d gave back **15.8pp in 3 sessions**) | ⛔ **the registered pair (−3.00 → +3.17) is NOT reproducible** — implies +6.17pp on a session whose actual basket excess was **+2.80pp**; **window must be fixed at 60 sessions to be re-readable** | 08-07 |
| **M40** — payments+insurance per-name flow | **34.0% names / 42.9% gross+ / 2.39× sector eqflow** | falls below **1.5×** the sector eqflow | 08-11 |
| **M136** — exchanges ↔ IB mirror | ⛔ **HALF BROKEN** — IB half holds (lowest flow −0.354, RS60 +6.5); **exchanges half broke** (flow fell from highest to 9th/12 at −0.035, RS60 still worst at −5.9) | **retire the "mirror image" framing**; the node's headline is one name (ICE +0.811 vs MSCI −0.726, range 1.537) | — |
| **R32 / breadth** | all-47 gap **+0.0087**, ex-BRK-B **+0.0126** (convention eq−w) | ★ **C4 — breadth-led and mega-cap-led are indistinguishable this run**; five measurements have spanned −0.0166 to +0.0370 | 08-11 |
| **Lens 3 re-tags** | **MET EXT-BUT-LIVE ✓ · TRV round-trip ✓ · TRI EXHAUSTED ✓ · ICE EXHAUSTED ✓** — all four reproduce on my independent 08-03 measure | MET's seg-21-60 (+11.9) turning negative | 08-11 |
| **Credit** | HY **2.85** (50th pct, **+11bp/20d**) · IG **0.79** (46th pct, +4bp/20d) · NFCI **−0.554**, 6th week loosening | HY ≥ **3.10** (25bp) or IG ≥ **0.90** (11bp) | rolling |
| ⚠ **`ig_oas` feed reliability** | **502 on first call, succeeded on retry** | a second consecutive run needing a retry ⇒ treat IG OAS as **unconfirmed** | 08-05 |
| ⚠ **D139** — FRED nominal publication lag | reconfirmed a **third** time (VIX/T10YIE have 08-03; DGS2/10/30 do not) | — | standing |

---

## 8 · What this DEEP hands to BET

1. ★★ **The answer to the question asked: one leg is not enough, but the binding reason is instrumentation, not conviction.** **S23 (0% of the year) and S51-A (94% of the year) cannot jointly produce information on 08-07.** **§7 hands over two calibrated replacements — S23-R at ≤ +0.40 (9.0% base rate) and S51-A-R at ≥ +0.54 (≈5%) — both inside the observed distribution.** Until one of them is registered, **the 08-07 print cannot move the Financials tilt in either direction, and BET should treat the date as non-informative rather than as a scheduled resolution.**
2. ★★ **The measured fact BET should carry forward regardless of the tilt: the sector's rate exposure does not live in the banks.** **Every one of the 9 banks + KRE + XLF has a slope beta indistinguishable from zero over 60 sessions (R² ≤ 0.05).** The significant loaders are **CME (+45.0, t+4.3), NDAQ (+33.2, t+3.4), ADP (+29.8, t+2.5), ICE (+28.0, t+3.0), MRSH (+24.0), SCHW (+20.3)** — **exchanges, market data and payroll float.** ⚠ **C2: low power over 60 days with 4.5bp/day of DGS2 variation; absence of measured beta is not proof of no mechanism, and no lag table exists (W2/C3).**
3. ★★ **Lens 2's branch is quantified and inverted against the 08-03 carrier.** Under S51-A-BULL, **six of the eight worst-positioned names in the 51-ticker set are P&C/life insurers (TRV −1.31, CB −1.15, PGR −0.96, ALL −0.92, AFL −0.66, HIG −0.66)** — the node the desk named as the carrier one run ago — **while the exchanges node it resolved 🔴 is best-positioned (NDAQ +1.87, ICE +1.25).** Base rate **1.6%** vs the bear variety's **20.5%**: **carry it as a weighted tail flag, and read the qualifier's "−15bp" as cumulative, since the single-session version has 0/248 precedent.**
4. ★ **The names that actually separate level from slope, for anyone needing the distinction:** **slope-dominant NDAQ (3.4×) and ICE (2.7×)**; **level-dominant TRV (13×), CB, PGR, ALL, HIG, AFL, SCHW.** ⚠ **ICE is simultaneously the sector's #1 flow score and Lens-3 EXHAUSTED (RS60 −4.2, seg −15.9)** — the two readings are both reported and **not reconciled (C3)**.
5. ★ **M135 is not yet fixed; it is now diagnosable.** The replacement observable's registered pair is arithmetically impossible on a fixed window, so **it was measured with an advancing base date — the original defect.** **The 60-session value on the settled 08-03 bar is −5.92pp, and the 20-session excess has given back 15.8pp in three sessions to +0.24pp.** **Fix the window in the register (M135-R) and the observable becomes re-readable.**
6. **M40 holds (2.39×); M136 should be retired as a mirror image.** **W5 stands unchanged: sub-industry mean flow spans 0.916 ≈ 9× the sector's own eqflow, so "Financials" remains the wrong unit of analysis.**
7. **HSBC corroborates the LEVEL/FEE channel, not the SLOPE channel** — **NII +9%, guidance raised past $46bn, wealth +18%, explicitly "resilient interest income *despite dips in central bank rates*"** — **a second-continent replication of M138's migration.** ⚠ **W3: strip the $2.6bn of notable items before using the +23% headline; and the same print carries ECL +$400m YoY.**
8. **Credit is benign in level and mildly adverse in direction: HY 2.85 (50th pct) but +11bp over 20 sessions, IG 0.79 (+4bp), NFCI −0.554 loosening a 6th week.** **Fitch's AI-credit and record private-credit-default items are labelled narrative-only** and are not carried as credit stress.

⚠ **R41 — superlative scope declared.** Every "highest / worst / only / best" above is scoped to a set that was fully scanned: **the 47 GICS Financials in `SECTOR_FLOW_US.json` (asof 2026-08-03)**, **the 12 sub-industries within them**, or **the 51-ticker regression set** listed in §2. **No superlative in this file ranges over an unscanned universe.**
