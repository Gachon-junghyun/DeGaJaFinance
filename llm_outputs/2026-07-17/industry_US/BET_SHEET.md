# BET_SHEET — industry_US · 2026-07-17 (Fri)

> Stage 6 / L1·BET. **ONE file, per-sector sections** (downstream desks glob this exact filename — never split).
> Sections §A numbers · §B narrative + freshness (ALPHA fills) · §C flow/positioning · §D competition/peers · §E refutation + dated catalyst.
> **Zero buy/sell recommendations.** Sizing language is *influence illustration* only. Analysis for a human to decide on.
> Sources: `module_fundamentals_us --json` (XBRL/yfinance) · `module_flow --bench SPY` · `scripts/us_flow.py` (FINRA short-vol z) · DEEP files · `BLINDSPOT_PREMORTEM.md`.
> Prices/flow **asof 2026-07-16 close** (07-17 US equity session not yet closed; CL=F/VIX are 07-17).

## §0 Method notes — what the candidate net is, and what is missing from it
BET's rule: candidates = (deep-agent thesis leaders) ∪ (**sector screener setups**) ∪ (★LIVE_SHORTLIST names).
- ⚠ **The screener leg could NOT run.** `scripts/us_setup_screener.py:41` does `import yf_snapshot`, but **`scripts/yf_snapshot.py` does not exist and never has in git history** — every invocation dies with `ModuleNotFoundError`. Filed as a repo task; **not** worked around here. **Consequence: the net is narrower than the protocol intends** — the "wide-net setups" leg contributed **zero** candidates, exactly the leg meant to surface names we didn't already know. Recorded, not papered over (P4).
- The union therefore = DEEP thesis leaders ∪ LIVE_SHORTLIST (6 names) only.

### Data-quality flags (cross-check XBRL ↔ yfinance; blanks stay blanks)
| Field | Flag |
|---|---|
| **ASML P/B = 1,606.7** | **ARTIFACT** — not a usable number. Ignored, not reported as a multiple. |
| **ABBV P/B = −67.5** | Negative book equity (real, buyback-driven), but it makes **trailing PE 118.9 meaningless** — ABBV's tEPS 2.14 is depressed vs fEPS 16.28. **Use forward only.** |
| **TSM P/B = 92.7** | Likely ADR-scaling artifact — not used. |
| **MRK PEG 5.97 vs fwd PE 13.2** | Internally inconsistent; PEG unreliable here. Forward PE used. |
| **ROE / revenue-growth / operating-margin** | Returned empty (`—`) for **every** ticker by this module → **left blank, not guessed.** |
| **INTC trailing PE** | Blank — trailing EPS is **−0.56** (loss-making). Forward only. |
| `module_math_check` | Run on this file (see §7). It validates weighted/peer averages and target-price upside consistency — **this sheet carries no target prices**, so its checks are structurally inapplicable. Reported honestly rather than claimed as a pass. |

### ⚠ Catalyst-date corrections (confirmed dates beat the calendar's pattern-estimates)
| Event | CATALYST_WATCH said | Confirmed (`next_earnings_date`) | Note |
|---|---|---|---|
| **KMI earnings** | 07-22 | **2026-07-23** | Calendar was **off by one day**. DEEP·ENRG independently found 07-23. |
| **NFLX earnings** | **D-0 = 07-17** | **printed 07-16** | **Stale binary** — it already resolved, and disappointed. MACRO §0 listed it as a forward binary; it was not. |
| **INTC earnings** | — | **07-24** (yfinance) vs **"July 23"** (3 in-DB news cites) | ⚠ **CONFLICT, unresolved — recorded as `07-23/07-24 [conflict]`, not guessed.** Either way it is the fulcrum. |
| SCHW earnings | 07-21 | **2026-07-21** ✅ | Confirmed. |
| **UNH earnings** | not listed | **printed 07-16** (beat-and-raise) | Missed by the calendar; found by DEEP·HLTH. |
| **DHR 07-21 · TMO 07-23** | not listed | **confirmed, INSIDE the 5-day window** | **New — the calendar carried no Health Care prints at all.** See §2. |

---

# §1 FINANCIALS (FIN) — OW ★ (continuous)

## §A Numbers
| | PNC | BNY | SCHW |
|---|---|---|---|
| Price / mcap | **$255.20** / $102B | **$160.90** / $110B | **$102.80** / $179B |
| Trailing PE | 14.0 | 20.2 | 20.4 |
| **Forward PE** | **12.0** | 15.9 | 13.7 |
| PEG | 2.00 | 1.68 | 1.21 |
| P/B | 1.8 | 2.8 | 4.2 |
| fEPS / tEPS | 21.30 / 18.25 | 10.10 / 7.98 | 7.52 / 5.03 |
| 52wk range | 176.9 – **256.3** | 95.1 – 163.8 | 84.0 – 107.5 |
| **% off 52wk high** | **−0%** (AT the high) | −2% | −4% |
| Rev QoQ | +1% | +5% | +2% |
| Next earnings | 2026-10-15 | 2026-10-15 | **2026-07-21 (D-4, BINARY)** |
| ROE / margins | *(blank — module returned none)* | *(blank)* | *(blank)* |

## §B Narrative / thesis — *freshness tag: [ALPHA fills]*
The curve leg and the earnings leg are **two different bets** (DEEP·FIN verdict). The curve leg (2s10s **+36→+42bp**; 10Y 4.55%, 2Y 4.13% [FRED asof 07-15]) is **intact and early** — corroborated by **XLF RS60 only +1.9%** (PREMORTEM lens 3: "early, not extended"). The earnings leg is **already confirmed** by BNY (record quarters, dividend +19%), M&T (EPS $5.32, beat by $0.66) and First Horizon — but **SCHW walks into its own print priced for perfection**.
FIN is the **#1 news-velocity bucket (2,759 hits/7d**, up from 1,581 on 07-15) and the **only sector agreeing on every axis**: matrix OW × flow rank 2 × **eqflow 0.279 > wflow 0.181 (breadth-led)** × 2 of the universe's 3 new-🟢 ignitions.

## §C Flow / positioning cross-read
| | Flow tag | OBV | RS20 | RS60 | Vol surge | FINRA short-z |
|---|---|---|---|---|---|---|
| **PNC** | **🟢ACCEL** | accumulating | +8.7% | +6.5% | **1.24×** | **−0.62 (−6.3▼)** ← the board's only ✅clean rise |
| **BNY** | **🟢ACCEL** | accumulating | +11.3% | +12.9% | **1.26×** | +0.60 (+5.7▲) |
| **SCHW** | 🟡NEUTRAL | accumulating | +9.7% | +4.4% | **0.70×** ← no volume behind it | −0.42 (**+8.8▲ rising**) |

⚠ **Tool conflict, stated not smoothed:** `module_flow` reads SCHW's OBV as **accumulating**; DEEP·FIN's `module_chart` read it as **distributing, RSI 86.9**. Different windows/engines. **Unresolved — do not treat SCHW's OBV as settled.** What both agree on: **volume surge 0.70× = the rally has no volume behind it**, and short-z is *rising* (+8.8▲) into the print.

## §D Competition / peers
Forward-PE spread is narrow (12.0 / 15.9 / 13.7) — **PNC is the cheapest on forward and the only one with a sub-2 P/B (1.8)**. SCHW carries the **highest P/B (4.2)** into the only binary. Chain-hop surfaced **GS, WFC, C** as body-proximate co-mentions — **all three FAILED the flow cross-check** (GS/C distributing, WFC flat) → **zero promoted to this sheet** (a co-mention alone is not a candidate).

## §E Refutation + dated catalyst
- **Dated catalyst: SCHW 2026-07-21 (D-4, binary, confirmed).**
- **The refutation that is already firing:** the **beat-but-fade** pattern is live *this week* — *"Bank of America's stock falls **despite** blockbuster earnings"*; *"Big Banks Smash Earnings Records, but 'Tectonic' Risks Loom"*. SCHW has **already run** (RS20 +9.7%) into a high bar — **the same setup that just broke TSM**.
- **Kills the curve leg:** real 10Y **> 2.50%** (now 2.32%) → duration losses in AFS books swamp the steepener gain.
- **Kills the earnings leg:** SCHW beats and closes **red**; or credit-cost/NIM disappointment in the regionals.
- ⚠ **Asymmetry worth stating:** a SCHW disappointment would **not** break the curve leg (PNC/regionals unaffected) — but it **risks being misread as invalidating the whole OW**. The two legs must be scored separately.
- **Illustrative influence only:** the curve leg's cleanest expression is **PNC** (clean rise + cheapest forward + un-extended); SCHW is the *test*, not the *expression*.

---

# §2 HEALTH CARE (HLTH) — OW ↑ (rotating, first-ever deep-dive) ★ the flow-led promote

## §A Numbers
| | ABBV | MRK | UNH | TMO | DHR | WELL | VTR |
|---|---|---|---|---|---|---|---|
| Price | $254.40 | $127.60 | $423.40 | $543.20 | $205.00 | $241.50 | $95.00 |
| mcap | $449B | $315B | $384B | $202B | $145B | $170B | *(n/a)* |
| **Forward PE** | **15.6** | **13.2** | 19.9 | 19.9 | 22.2 | **71.9** | *(n/a)* |
| Trailing PE | *118.9 ⚠artifact* | 34.9 | 31.5 | 29.4 | 38.9 | 112.3 | *(n/a)* |
| PEG | **0.40** | *5.97 ⚠* | 1.45 | 1.76 | 1.27 | **3.66** | *(n/a)* |
| P/B | *−67.5 ⚠* | 6.9 | 3.9 | 3.9 | 2.7 | 3.9 | 3.5 |
| **% off 52wk high** | −3% | −2% | −8% | **−16%** | **−16%** | **−0% (AT high)** | **−0% (AT high)** |
| Rev QoQ | −10% | −1% | −1% | −10% | **−13%** | +5% | +6% |
| **Next earnings** | 07-31 | 08-04 | **printed 07-16** (beat-and-raise) | **07-23 ★in-window** | **07-21 ★in-window (D-4)** | 07-28 | 07-30 |

## §B Narrative / thesis — *freshness tag: [ALPHA fills]*
**"Money with no story" — RESOLVED: (i) early, un-crowded, durable rotation — NOT (ii) a parking lot** (DEEP·HLTH, moderate confidence).
The sector was **promoted by flow against the macro matrix** (rule-(b) divergence): **wflow 0.357 / eqflow 0.264 = rank 1 of 11**, **Δw +0.33 = the biggest one-day ignition on the board**, both flows strongly positive = **broad**. Yet **news velocity is dead last (465 hits/7d** vs FIN 2,759) and **decelerating** (`healthcare` ⚪ECHO 0.89×, `pharma` 0.74×), and **zero HLTH names carry 🟢ACCEL**.
**Why it is (i) not (ii):**
1. **All 8 sub-industries are flow-positive** (0.11–0.32, narrow spread; only **2 of 32 names red** — ELV, PFE) = genuinely broad, not a huddle.
2. **Biotech (growth-style, non-defensive) ties the strongest sub-industry** — a pure flight-to-safety would **not** bid biotech.
3. **The defensive bid went to HLTH and NOT to Staples** (STPL wflow −0.247) — a blanket risk-off would have bid both. **The rotation is selective**, which implies a thesis, not fear.
4. **Two real, dated fundamentals a 4-keyword velocity count cannot see** (velocity counts headlines; title+summary search is ~49% body-blind): **(a)** MFN drug-pricing — **17 major pharma companies reached voluntary pricing agreements since late 2025** [Motley Fool 07-14], defusing a multi-year pricing overhang; **(b)** managed-care turnaround + ACA exchange-subsidy clarity [ClearBridge Q2 commentary, SA 07-15] — and **UNH's 07-16 beat-and-raise landed on the exact day the chips cracked.**

## §C Flow / positioning cross-read
| | Flow | OBV | RS20 | RS60 | Vol surge |
|---|---|---|---|---|---|
| ABBV | 🟡NEUTRAL | accumulating | +14.3% | **+19.0%** | 0.79× |
| MRK | 🟡NEUTRAL | accumulating | +10.8% | +3.1% | 0.87× |
| UNH | 🟡NEUTRAL | accumulating | +3.8% | **+25.0%** | 0.98× |
| TMO | 🟡NEUTRAL | accumulating | +14.9% | −2.7% | 0.73× |
| DHR | 🟡NEUTRAL | accumulating | +13.0% | −1.1% | 0.90× |
| WELL | 🟡NEUTRAL | accumulating | +13.1% | +9.4% | 0.73× |
| VTR | 🟡NEUTRAL | accumulating | +13.2% | +6.3% | 0.67× |

**Uniform accumulation across all 7 — every single name accumulating, none distributing.** That uniformity *is* the signature of a broad rotation. But note **every vol surge is <1.0×**: this is **drift, not a stampede** — consistent with "early and un-crowded", and equally consistent with "nobody is chasing it yet". Short-z not pulled for HLTH (no crowding signal in the flow tags to test).

## §D Competition / peers
**MRK (fwd 13.2) and ABBV (fwd 15.6, PEG 0.40)** are the cheapest large-caps in the sector. **WELL is the expensive outlier — fwd PE 71.9, PEG 3.66, and sitting AT its 52wk high.**
**WELL/VTR verdict (PREMORTEM lens 1 → resolved):** **reassign the senior-care REIT sub-leg to the HLTH OW, not the RE UW.** Their tenant economics run through the **same Medicare/Medicaid reimbursement bottleneck** as the rest of the HLTH chain — not RE's office/data-center drag. Flow confirms: WELL 0.517 / VTR 0.483 vs RE's sector wflow −0.046. **This directly resolves ROTATION's RE divergence** (matrix-UW but flow-flat): the RE UW was capturing office/retail weakness while **mispricing a sub-leg that belongs to HLTH**.
Chain-hop: **zero candidates survived cross-check** (AMGN flow too weak; LLY a tool artifact; MMM/JPM/MS noise) — stated rather than stretched.

## §E Refutation + dated catalyst
- **★ Dated catalysts INSIDE the window that the calendar missed: DHR 07-21 (D-4) and TMO 07-23.** Both are **Life-Science Tools** — DEEP·HLTH's **strongest-flowing sub-industry (0.32)**. Both are **−16% off their highs with revenue QoQ −13% / −10%**. **This is the nearest real test of the whole HLTH thesis**: the leading sub-industry prints in 4 days with visibly weak recent revenue.
- **★ The named falsifier (DEEP·HLTH):** **track HLTH flow once MU holds >$853.20 for 2+ sessions.** If HLTH wflow stays **≥+0.20** and breadth **≥6 of 8** sub-industries → **durable** (the money didn't need AI to be scary). If it **collapses toward zero** → **confirmed parking lot.** *This is the cleanest falsifier produced anywhere in this run — it dates the test to an observable on another sector's chart.*
- **Key anti-signal (the first cracks):** **ABBV and WELL — the two most prominent flow leaders — BOTH show OBV distribution + bearish price/RSI divergence** on `module_chart` (WELL RSI 70.4). The leaders cracking first is how a rotation dies.
- **Illustrative influence only:** the *broad* expression is the sector; the *cheap* expression is MRK/ABBV on forward; **WELL is the expensive, extended end** and carries the distribution flag.

---

# §3 ENERGY (ENRG) — modest OW (rotating) · ★ carries the REAL cycle GAP

## §A Numbers
| | MPC | PSX | VLO | **DINO** | KMI *(held 14.1%)* | LNG *(held 9.87%)* |
|---|---|---|---|---|---|---|
| Price / mcap | $305.90 / $89B | $201.30 / $81B | $300.30 / $89B | **$86.80 / $16B** | $32.50 / $72B | $259.00 / $54B |
| **Forward PE** | 12.1 | **11.2** | 13.5 | **10.5** ← cheapest | 21.6 | 13.3 |
| Trailing PE | 19.7 | 19.4 | 21.4 | 12.6 | 21.5 | 43.3 |
| PEG | 1.51 | **1.17** | *4.08* | 1.26 | 3.85 | *9.46 ⚠* |
| P/B | 5.3 | 2.8 | 3.7 | **1.6** | 2.3 | 14.5 |
| **% off 52wk high** | −1% | −1% | −1% | −1% | −7% | −14% |
| Rev QoQ | +5% | −5% | +7% | **+10%** | +7% | +8% |
| **Next earnings** | 08-04 | 08-05 | 07-30 | 07-28 | **07-23 (D-6, BINARY — calendar said 07-22, WRONG)** | 08-06 |

⚠ **Note: none of the four refiners print inside the 5-day window.** The only dated ENRG binary is **KMI 07-23** — which tests a **held book position**, not the epicenter thesis.

## §B Narrative / thesis — *freshness tag: [ALPHA fills]*
**"Early or trap?" — RESOLVED: EARLY, not a trap — but now de-risked at the equity level** (DEEP·ENRG).
ROTATION saw the divergence (commodity **CL=F +10.2%/5d** vs sector flow rank **8 of 11**, wflow −0.151) and asked whether money disbelieved the move. **It is an aggregate artifact**: the **crack-spread sub-leg is already working** (MPC RS60 **+36.9%**, VLO **+26.8%**, PSX **+23.3%**, DINO **+44.1%**) while the **integrateds/E&P drag the average** (XOM/CVX/EOG/OXY flow −0.16 to −0.42) — because **integrateds monetize crude price; refiners monetize refining margin**. That distinction is the entire thesis.

### ★ The crux — does the crack survive a Hormuz-open (TACO) shock? **Largely YES.**
DEEP·ENRG verified the driver from the news DB: the diesel/crack move is driven by **Russian refinery destruction** (Ukrainian strikes on **named** refineries — **Afipsky, Syzran**) **+ Russia's own diesel export ban** — **mechanically independent of the Strait of Hormuz**. Corroborants: *"Diesel Prices Hit $5 a Gallon Again, **Up 33%** Since Start of Iran War"* [NYT 07-16]; *"Russian Refinery Runs Plunge to **Lowest in More Than Two Decades**"* [Bloomberg 07-13]; *"Russia's diesel export ban deals fresh blow"* [SCMP 07-11].
**And the second-order point is sharper:** refiners are a **spread** business (buy crude, sell product) — a Hormuz-driven **crude collapse would likely WIDEN the crack, not kill it.**
> **→ The refining leg is a genuinely different bet from crude beta.** The desk's OW-ENRG was justified on P3 (oil war-premium); the *durable* part of it is **not** the oil premium at all.
**The real residual risk is a BETA gap, not a mechanism gap:** on a Hormuz-open headline the *equities* would likely sell off with the sector even though the fundamental driver is decoupled. **That gap is the tradable risk** — and it is a different risk from the one MACRO §4a P3 wrote.

## §C Flow / positioning cross-read
| | Flow | OBV | RS20 | RS60 | Vol surge | **FINRA short-z** |
|---|---|---|---|---|---|---|
| **DINO** | 🟡NEUTRAL | accumulating | **+30.4%** | **+44.1%** | **1.19×** | +0.90 (+2.8▲) |
| MPC | 🟡NEUTRAL | accumulating | +22.1% | +36.9% | 0.88× | −0.83 (−5.5▼) |
| VLO | 🟡NEUTRAL | **neutral** | +22.9% | +26.8% | 1.03× | −0.08 |
| **PSX** | 🟡NEUTRAL | accumulating | +17.0% | +23.3% | 1.06× | **−1.43 (−16.6▼)** ← nearly the ≤−1.5 "exit" threshold: **shorts are leaving** |
| KMI *(held)* | 🟡NEUTRAL | accumulating | +3.4% | −4.0% | 0.73× | **+0.92 (+5.2▲)** ← short build into its 07-23 print |
| LNG *(held)* | 🟡NEUTRAL | accumulating | +12.1% | −3.3% | 0.81× | **+3.09 🔴 EXTREME** |

★ **The order-flow tell news cannot see:** **PSX short-z −1.43 with a −16.6▼ trend = shorts exiting** into a rising tape — the cleanest positioning signature in the sector. Meanwhile **LNG's +3.09 is the single most extreme short reading in this entire sheet — on a position the book already holds at 9.87%.**

## §D Competition / peers
**DINO (HF Sinclair, $15.7B)** is the find: **cheapest forward (10.5), lowest P/B (1.6), strongest RS20 (+30.4%) and RS60 (+44.1%), best rev QoQ (+10%), and a real vol surge (1.19×)** — and it was **not** on any prior desk list. Surfaced by DEEP·ENRG as a flow-verified chain-hop. **CVI and PBF were logged but held below the ≥2×-mention bar** (not promoted). ⚠ The automated `chain-hop` tool returned **only noise** (mega-cap tech false positives) → **discarded, stated**. ⚠ Tanker names (FRO/STNG/INSW/DHT) are **not in the top-300 universe → flow-unverified**, excluded.

## §E Refutation + dated catalyst
- **Dated: KMI 07-23 (binary, confirmed).** ⚠ **KMI and the Hormuz binary are NOT independent** — both hit the same OW leg. Treat as **one correlated exposure, not two.**
- **The against-us bracket (equal weight — a one-way tilt here is a protocol violation):** a **durable** Iran "strait open / blockade lifted" statement (bar = **surviving >24h**; the Trump toll-plan reversal already fired and faded in **<48h**) → crude retraces toward **$70–72**. ⚠ **WTI is 13%ile crowded-SHORT → residual shorts would ADD, not cover → the drop ACCELERATES rather than cushions** (the exact mirror of the squeeze the desk just won).
- **Invalidation:** CL=F **< $72** and XLE giving back **>half** its +3.5%.
- **Anti-signals (observables):** crack spread level · **diesel price (now ~$5/gal, +33% since the Iran war)** · **Russian refinery runs (2-decade low)** · Hormuz transit. **If Russian refining capacity comes back online, the crack leg dies — and that is independent of Hormuz.** *(This is the correct anti-signal: the mechanism most likely to kill the thesis, not the loudest headline — per the run's own failure class 3.)*
- ⚠ **Entry-technical caveat:** all four refiners sit **within ~1% of 52wk highs**, **MPC at RSI 85.7** → the *thesis* is not exhausted but the *entries* are technically extended.
- **Illustrative influence only.**

## §3a ★ EPICENTER-STARTER MODULE (required — a cycle GAP was flagged)
> **The rule:** when a cycle GAP is flagged, **a partial core in the cycle's epicenter exists on the sheet regardless of tape; the tape gates only the remainder.**

- **Cycle: Energy / oil-refining (Hormuz + Russia crack) — registry rank 2.**
- **Book epicenter exposure: 0.0%.** The book's 23.97% "any-layer" Energy is **100% KMI (14.1%) + LNG (9.87%)** — **verified from the companies' own 10-K Item 1**, not inherited: KMI's **"fee-based / minimum-volume"** and LNG's **"take-or-pay style"** language confirm both are **volume/fee names structurally insulated from crack economics by design**.
  - ⚠ **DEEP·ENRG's correction to PREMORTEM (kept, not buried):** LNG's 10-K shows **a majority of disclosed future revenue sits in the "variable fee" (index-linked) bucket, not fixed** — this **softens but does not overturn** the carve-out.
- ⚠ **The deterministic ✅ was an artifact.** `cycle_exposure.py:87` → `gap = (rank<=2) and (epi_pct < min_epicenter_pct)`, and the rank-2 cycle's `min_epicenter_pct = 0.0` → **`epi_pct < 0.0` is unsatisfiable; that GAP can never fire at any exposure.** **This run treats the GAP as REAL** on the evidence, not the flag. (Filed as a repo task; not hot-patched mid-run.)
- **Cleanest epicenter expressions (flow-verified, not named-in-headlines):** **PSX** (cheapest large refiner on forward 11.2 + PEG 1.17 + **shorts exiting −1.43**) · **MPC** (strongest large-cap RS60 +36.9%, shorts leaving) · **VLO** · **DINO** (cheapest + strongest RS, small-cap $16B).
- **NOT epicenter (explicitly excluded, with reason):** **XOM · CVX · EOG · OXY** — flow −0.16 to −0.42, negative RS60; they monetize **crude**, not **margin**.
- **Book context:** cash **34.4%** ($2,716 of $7,901) — the constraint is not capital.
- **Illustrative influence only — zero buy/sell recommendation.** The tape gate here is *entry technicals* (all four within 1% of highs, MPC RSI 85.7), not the thesis.

---

# §4 SEMICONDUCTORS (SEMI) — UW sector, ★ pre-mortem-promoted leg (continuous)

## §A Numbers
| | **MU** | NVDA | TSM | **INTC** | ASML | AVGO |
|---|---|---|---|---|---|---|
| Price / mcap | **$853.20** / $964B | $207.40 / **$5,023B** | $409.70 / $2,125B | **$97.00** / $487B | $1,784.90 / $686B | $374.40 / $1,781B |
| Trailing PE | 20.5 | 32.6 | 36.5 | **— (loss: tEPS −0.56)** | 57.8 | 65.8 |
| **Forward PE** | **5.7** ★ | 16.2 | 19.3 | 60.1 | 31.2 | 19.3 |
| **PEG** | **0.13** ★ | 0.65 | 1.31 | 1.36 | 2.65 | 0.44 |
| fEPS / tEPS | **150.47** / 41.72 | 12.83 / 6.37 | 21.19 / 11.23 | 1.61 / **−0.56** | 57.25 / 30.88 | 19.42 / 5.69 |
| P/B | 13.3 | 25.7 | *92.7 ⚠* | 4.4 | *1,606.7 ⚠* | 20.3 |
| Beta | **2.14** | **2.21** | 1.25 | **2.19** | 1.39 | 1.46 |
| 52wk range | **103.4 – 1,255.0** | 164.1 – 236.5 | 223.7 – 479.0 | **19.0 – 142.3** | 683.5 – 2,000.0 | 273.0 – 495.0 |
| **% off 52wk high** | **−32%** | −12% | −14% | **−32%** | −11% | **−24%** |
| **Rev QoQ** | **+74%** ★ ($23.86B→$41.46B) | **+20%** | +12% | −1% | +6% | +15% |
| Next earnings | **09-24** (no near catalyst) | 08-27 | **printed 07-16** | **07-23/07-24 ⚠[conflict]** | 10-14 | 09-04 |

★ **The number that frames the whole run: MU trades at 5.7× forward / PEG 0.13, −32% off its high, while its revenue just grew +74% QoQ and consensus forward EPS (150.47) is 3.6× trailing (41.72).** The de-rate is happening **against accelerating fundamentals**, not weak ones.

## §B Narrative / thesis — *freshness tag: [ALPHA fills]*
**RESOLUTION VERDICT (DEEP·SEMI, committed not hedged): (b) — a NARROW capital-intensity de-rate [P2′].** Not (a) a broad AI-capex sign-flip; not (c) a plain dip.
The desk's **original P2** said the market flipped the sign on AI capex (TSMC's record profit + **raised** capex/revenue guide + **$100bn** more US fabs → chips **sold off** on *"capex concerns"* / *"a **high bar**"*). **Three refutations forced the narrowing:**
1. **META's capex was REWARDED the same week TSM's was PUNISHED** — *"Meta's Sudden Stock Rebound Shows Investors Endorse AI Plans"* [07-15]. If the sign had flipped on *AI capex as such*, META — the index's biggest hyperscaler spender — is the name that should have broken. It went the other way.
2. **TSMC's raise is partly DEFENSIVE** — Barron's framed the $100bn as TSMC *"fighting the Intel Challenge"* [07-16]. Not pure demand confirmation.
3. **The capex→equipment chain is NOT decoupling** — AMAT −0.087, LRCX −0.438, KLAC −0.594, all red, trading as one basket. An **indiscriminate complex-wide de-rate**, which is a *positioning* signature, not a *demand* one.
**The load-bearing evidence is the OBV (money-flow) split, not price:** genuine distribution confirms in **only TSM** (OBV −99% 20d slope, the **only** >1× volume surge, pullback-to-support) and **INTC** (−73%). Everywhere else contradicts a demand-side flip: **MU's OBV is still ACCUMULATING (+52%) through a −16.5% RS20 drawdown**; **NVDA OBV neutral, RS20 ≈flat** (the bellwether never broke); **META's OBV accumulates hardest of any name (+108%)**; **ASML has the best-improving flow delta on the entire board (+0.234)** inside a red equipment basket.
**Reconciliation with the UW:** a cycle can be **live at the epicenter and rotting at the periphery** — which is exactly what **IT eqflow −0.339 vs wflow −0.094 (0 green / 21 red)** measures. **IT stays UW as a breadth / new-money call; the epicenter is carved out (§4a).**

## §C Flow / positioning cross-read
| | Flow | OBV | RS20 | RS60 | Vol surge | **FINRA short-z** |
|---|---|---|---|---|---|---|
| MU | 🟡NEUTRAL | **neutral (NOT distributing)** | −16.5% | **+84.3%** | 0.73× | −0.44 |
| **NVDA** | 🟡NEUTRAL | neutral | −0.1% | −3.3% | 0.81× | **+1.67 🔴 SHORT-VOL SPIKE** |
| **TSM** | **🔴DISTRIB** | **distributing** | −3.8% | +6.0% | **1.13×** ← the only surge | *(not pulled)* |
| INTC | 🟡NEUTRAL | neutral | **−17.2%** | **+41.7%** | 0.76× | **−1.14 (NOT a crowded short)** |
| ASML | 🟡NEUTRAL | neutral | −1.1% | **+15.0%** | **1.18×** | −0.53 |
| AVGO | 🟡NEUTRAL | neutral | −0.7% | **−12.2%** | 0.69× | *(not pulled)* |

★ **The order-flow tell news cannot see — and it cuts AGAINST the bullish read: NVDA short-vol z = +1.67 (a ≥+1.5 SPIKE), trend +3.3▲.** PREMORTEM lens 3's single strongest argument against exhaustion was *"the bellwether held up best"* — **but shorts are attacking NVDA hardest precisely while its price holds.** The narrative says resilient; the order flow says pressure is building. **This is a genuine divergence and it is NOT resolved.** It does not overturn verdict (b), but it is the one piece of evidence pointing at (a).

## §D Competition / peers
Forward-PE dispersion inside one "sector" is extreme: **MU 5.7 · NVDA 16.2 · AVGO 19.3 · TSM 19.3 · ASML 31.2 · INTC 60.1.** That dispersion is itself the argument against treating SEMI as one bet. **AVGO (PEG 0.44, −24% off high, RS60 −12.2%) is lens 3's honest counter-example** — it was **not** leading, so "it already ran, fade it" never applied to it. **ASML is the equipment exception** (best-improving flow delta +0.234, RS60 +15.0%, vol 1.18×) inside an otherwise red basket.
**Chain-hop: ZERO candidates cleared the bar** — no body-proximate, headline-unnamed names survived. **Stated explicitly rather than stretched to fill the section.**

## §E Refutation + dated catalyst
- **★ Dated fulcrum: INTC Q2, `07-23 / 07-24 [conflict — yfinance says 07-24; three in-DB news cites say "July 23"; NOT guessed]`.**
  **The primary-source read (DEEP·SEMI pulled EDGAR directly):** INTC 10-Q Q1'26 (**accession 0000050863-26-000079**) shows **Foundry segment revenue +16.2% YoY**, **external-customer revenue +461% YoY**, operating-loss margin narrowing (−50% → −45%). That **supports the "Intel's foundry pitch is working" reading which underlies TSM's raise being partly defensive.** ⚠ **But it is one-quarter-old data — genuinely unresolved into the print.**
  INTC setup: flow −0.575 (bottom decile), **RS20 −17.2% vs RS60 +41.7%** (the same violent 20-day de-rate as MU), **short-z −1.14 = NOT a crowded short** → a genuine **oversold-vs-narrative gap, not squeeze fuel**. HSBC set a Street-high PT calling it *"Too Good to Ignore"* [07-09].
  **Falsifier:** in-line/miss on data-center/foundry revenue **+ RS20 making new lows post-print**.
- **★ The flip observable for the whole verdict:** **MU's OBV flips to distribution + SMH RS20 stays negative + TSM's distribution persists 2+ more sessions → verdict (a), the broad sign-flip, was right and P2′ was too timid.**
  ⚠ **MU's line ($853.20) is exactly its last print — this test is live right now, not hypothetical.**
- **Second anti-signal:** **if META rolls over** (RS20 negative + OBV → distribution), the broad sign-flip was right after all.
- **Bottleneck (unchanged, strengthened):** **CoWoS / advanced packaging + HBM.** New evidence *confirms rather than resolves* it — HBM called an *"unprecedented shortage"* [07-16], and **TSM's new $100bn Arizona commitment explicitly funds advanced-packaging fabs** = confirmation-by-capex that the binding constraint persists (multi-year fix). *Strong demand is not a bottleneck; the packaging line is.*
- ⚠ **Primary-source honesty:** TSM's Q2 actuals + Q3 guide verified from **6-K accession 0001046179-26-000451**; the **FY26 capex / $265bn figures are news-corroborated but NOT primary-transcript-verified** → flagged, not asserted.

## §4a ★ EPICENTER CARVE-OUT (binding — from PREMORTEM §5)
> **The AI-compute epicenter (AVGO · NVDA · TSM) is OUT of the IT-UW's operational scope.**
Two different objects were being conflated: **GICS-IT-as-rotation-entry** (a *breadth* call about where **new** money goes → UW stands) vs the **cycle-registry AI-compute epicenter** (a deliberately **tape-independent core**, built 07-15 in answer to the 07-14 GAP).
- ⚠ **The book holds it at 12.06% vs a 12.0% floor — 0.06pp of margin.** **Mark-to-market erosion alone** (AVGO RS60 −12.2%, TSM −5.6%) **can breach that floor without a single trade.** → **reclassify ✅ → WATCH.**
- > **Any trim of AVGO/NVDA/TSM under the UW-IT banner would silently manufacture the 07-14 failure in reverse** — not *"never built the core"* but *"dismantled it under cover of a sector call that was never about the core."*
- **The hard rule stands: a 🔴 tape gates ADD timing; it never justifies 0% core in a multi-year cycle.**

---

# §5 CROSS-SECTOR LIVE-SHORTLIST NAMES (outside the DEEP sectors — included or dropped with reason)
The LIVE shortlist held **6 names** (the universe's only 🟢ACCEL names, mcap ≥$10B). PNC/BNY are covered in §1. The rest:

| | **META** (COMM — a UW sector) | **CTAS** (INDU — Neutral) | **FAST** (INDU — Neutral) | **PYPL** (FIN) |
|---|---|---|---|---|
| Price / mcap | $664.50 / $1,687B | $206.20 | $46.70 | $56.70 |
| Forward PE / PEG | **18.3 / 0.96** | *(fEPS 6.10)* | *(fEPS 1.40)* | *(fEPS 5.75)* |
| P/B | 6.9 | 17.2 | 13.2 | 2.5 |
| % off 52wk high | **−17%** | −9% | −8% | **−29%** |
| Rev QoQ | −6% | +1% | +9% | −4% |
| Next earnings | **07-30** | 09-23 | 10-14 | 07-28 |
| Flow / OBV | **🟢ACCEL / accumulating (+108% slope — the hardest accumulation of any name)** | 🟢ACCEL / accumulating | 🟢ACCEL / accumulating | 🟢ACCEL / accumulating |
| RS20 / RS60 | +10.7% / −6.9% | +16.7% / +9.5% | +1.3% / −3.5% | **+29.9%** / +4.3% |
| Vol surge | 1.22× | **1.34×** | **1.54×** | **1.83×** (largest on the board) |
| Short-z | +0.36 | — | — | — |
| **Verdict** | **INCLUDED** — the live contradiction of the desk's own UW-COMM. Its RS20 +10.7% vs RS60 −6.9% is a **reversal signature**, and PREMORTEM re-labelled COMM's UW as a **GOOGL-regulatory + NFLX-miss bet, NOT an AI-capex bet** (GOOGL −0.68 / GOOG −0.70 at ~$4.5tn each drag the cap-weighted sector to −0.443 while **eqflow is only −0.03**). **META is the counter-evidence to P2 and must stay visible.** | **INCLUDED as watch** — **PEAD drift off a beat** (8-K filed **07-15**), *not* anticipation. No forward catalyst. This is *why* it is 🟢 — it is not a broad industrials thaw (INDU wflow −0.107, 2 green of 50). | **INCLUDED as watch** — same PEAD pattern (8-K **07-14**). RS20 only +1.3% = the drift is nearly spent. | **⚠ DROPPED from the thesis — with reason.** Its RS20 +29.9% / vol 1.83× is a **Stripe/Advent $53B takeover bid** (reported 07-15, still contested as of 07-17) — **M&A arbitrage, not organic FIN momentum.** Keeping it would have inflated the FIN OW's evidence base with a signal that has nothing to do with the curve or earnings legs. |

> ★ **The PYPL drop matters beyond PYPL.** ROTATION cited *"3 of 6 shortlist names are FIN"* and *"2 of 3 new-🟢 ignitions are FIN"* as evidence for the FIN OW. **PYPL was one of each.** Removing it, the FIN flow evidence is **PNC + BNY** — still the strongest on the board (breadth-led eqflow, the only clean rise), **but materially thinner than ROTATION claimed.** Recorded here so ALPHA/the next run does not inherit an inflated count.

---

# §5b ★ ALPHA FRESHNESS GATE — §B tags (filled by Stage 7 · ALPHA)
> Separates *interesting* from **bettable NOW**. The pipeline runs on lagging data — by thesis time the
> catalyst may already have fired. **`theme_age` (token-0, deterministic) ran FIRST**, before any live search.
> 🔴RESOLVED = **DROPPED from the bettable list AND logged** (so "it's cheap" cannot resurface next run).

| Bet | `theme_age` (foreign, 90d) | **TAG** | Evidence label + date | Residual / why |
|---|---|---|---|---|
| **FIN · curve leg (PNC)** | `bank earnings` **🟡ACCELERATING, accel 16.29×**, 57 hits | **🟢 LIVE** | 2s10s +36→**+42bp** [FRED 07-15]; PNC 🟢ACCEL, OBV accumulating, **short-z −0.62 (−6.3▼)**, vol 1.24× | **The freshest thesis on the board.** 16.29× is the highest acceleration measured anywhere this run. XLF RS60 **+1.9%** = early, not extended. Catalyst is *structural* (the curve), not a dated print → no "already fired" risk. |
| **FIN · earnings leg (SCHW)** | same, 🟡ACCEL 16.29× | **🟡 PARTIAL** | SCHW print **07-21 confirmed**; BNY/MTB/FHN beats **already banked** [SA 07-15/16] | **Residual: the leg is HALF-RESOLVED.** BNY/MTB/FHN already confirmed it works — that part is 🔴 **priced**. What is *unresolved* is **SCHW into a high bar** (RS20 +9.7%, vol **0.70×**, short-z **rising +8.8▲**, DEEP RSI 86.9). ⚠ **Momentum-only flag risk — see below.** |
| **HLTH · rotation** | `drug pricing` ⚪ECHO **1.43×**, only **20 hits** | **🟢 LIVE** | wflow **0.357 rank 1**, Δw **+0.33**; all 8 sub-industries positive; **UNH beat-and-raise 07-16**; MFN pricing deals [Motley Fool 07-14] | ★ **The low denominator is the thesis, not a refutation.** 20 hits/90d + velocity **dead last (465/7d)** + **zero 🟢ACCEL names** = **nobody is here yet**. An ⚪ECHO at 1.43× on a 20-hit base is *pre-consensus*, not consumed. **Un-crowded = the alpha.** ⚠ Needs the stronger live evidence an ECHO demands → it has it: **DHR 07-21 + TMO 07-23** are dated tests of the leading sub-industry. |
| **HLTH · WELL/VTR REIT sub-leg** | *(no separate theme)* | **🟡 PARTIAL** | WELL/VTR **both AT 52wk highs (−0%)**, OBV accumulating, RS20 +13% | **Residual: the re-assignment (RE→HLTH) is analytically settled but the entry is not.** WELL fwd PE **71.9**, PEG 3.66, RSI 70.4, **OBV distributing + bearish divergence** = the leader cracking first. |
| **ENRG · crack leg (PSX/MPC/VLO/DINO)** | `diesel` ⚪ECHO **0.91×** · `refinery` ⚪ECHO **0.58×** | **🟢 LIVE** | CL=F **+10.2%/5d**; MPC RS60 +36.9%, DINO **+44.1%**; diesel **$5/gal, +33%** [NYT 07-16]; Russian runs **2-decade low** [Bloomberg 07-13] | ★ **The desk's OWN failure class 4 applies and I am applying it: news velocity ≠ price on supply-shock assets.** On 07-15 the desk read Hormuz 🔴FADING (0.39×) and inferred oil down — **oil went +10.2%.** `refinery` at **0.58× decelerating** does **NOT** refute a physical supply shock. **Price is primary; theme_age is corroborant. Tag stands on the tape and the physical facts, not the headline count.** |
| **ENRG · KMI (held 14.1%)** | — | **🟡 PARTIAL** | Print **07-23 confirmed** (calendar said 07-22 — **wrong**); short-z **+0.92, +5.2▲ building** | **Residual: a sell-the-news setup on a held position.** Fee-based/take-or-pay (10-K verified) = **not** exposed to the crack thesis it's meant to express. |
| **SEMI · P2′ capital-intensity de-rate** | **`AI capex` 🔴FADING, accel 0.47×**, 332 hits · `HBM` ⚪ECHO 1.13× | **🟡 PARTIAL** | MU OBV **accumulating (+52%)** through −16.5% RS20; **only TSM distributes**; MU rev **+74% QoQ**, fwd PE **5.7** | ⚠ **A 🔴FADING narrative demands *stronger* live evidence — and here the evidence CUTS BOTH WAYS.** The de-rate is real in price but the *narrative driving it is dying* (0.47×), which supports P2′ (a positioning/expectations event, not a demand event). **Residual: NVDA short-z +1.67 SPIKE with shorts BUILDING (1.3% float, skew +12.5) — the order flow contradicts the "bellwether is fine" read. UNRESOLVED.** |
| **SEMI · INTC oversold-into-print** | `Intel` ⚪ECHO **0.63×**, 1,098 hits | **🟡 PARTIAL** | Print **`07-23/07-24` [conflict, not guessed]**; RS20 **−17.2%** vs RS60 **+41.7%**; short-z **−1.14 = NOT crowded short** | **Residual: the entire thesis is one dated binary.** Primary 10-Q (acc. 0000050863-26-000079): Foundry rev **+16.2% YoY**, external customers **+461% YoY** — but that is **one-quarter-old data**. ⚪ECHO 0.63× = the story is stale; **only the print refreshes it.** |
| **META (cross-sector LIVE)** | `AI capex` 🔴FADING 0.47× | **🟢 LIVE** | 🟢ACCEL, **OBV accumulating hardest of any name (+108%)**, RS20 +10.7% vs RS60 −6.9% = **reversal signature**; print 07-30 | **The live counter-evidence to the desk's own UW-COMM.** ⚠ Shorts **building** (1.6% float, skew +12.5). |
| **~~AI-power moratorium kill-switch~~** | `moratorium` collapsed to **17 hits/7d** | **🔴 RESOLVED → DROPPED** | Named as the AI-power anti-signal on 07-15; **never fired** — the leg fell 5% for an entirely different reason | **DROPPED AND LOGGED.** *Do not resurface: this anti-signal was refuted by outcome — it watched the wrong mechanism (run failure class 3).* |
| **~~NFLX binary~~** | — | **🔴 RESOLVED → DROPPED** | **Printed 07-16 and disappointed** (flow −0.442, RS60 −27.5%) — the calendar's "D-0 07-17" was **stale** | **DROPPED AND LOGGED.** *Do not resurface as a forward binary — it already fired. It is now COMM-UW evidence, already priced.* |
| **~~Defense platform primes (LMT/NOC/GD)~~** | `defense` bucket **771 = quietest** | **🔴 RESOLVED → DROPPED** | **3rd consecutive failure** with a near-ideal catalyst (oil +10.2%, Iran the #4 emergent term): LMT RS60 **−17.6%**, vol **0.58×**, distributing | **DROPPED AND LOGGED.** *Do not resurface on "they're cheap/unpriced" — that argument has now failed three runs. Revival requires an observable: volume surge >1.3× on an appropriations/NATO order.* ⚠ **RTX is a DIFFERENT leg and is NOT dropped** (see §5c). |

## §5c Stamps — momentum-only & positioning gates
| Stamp | Names | Ruling |
|---|---|---|
| ⚠ **MOMENTUM-ONLY → HARD-STOP REQUIRED** (RS/vol green but OBV distribution = tape trade) | **WELL** (RS20 +13.1, AT 52wk high, but **OBV distributing + bearish RSI divergence**, RSI 70.4) · **ABBV** (RS20 +14.3/RS60 +19.0 but **OBV distribution + bearish divergence**) | **Stamped.** These are the two most prominent HLTH flow leaders — *the leaders cracking first is how a rotation dies.* Tape trade, not thesis trade. |
| ⚠ **TOOL CONFLICT — not stamped either way** | **SCHW** | `module_flow` says OBV **accumulating**; DEEP's `module_chart` says **distributing, RSI 86.9**. **Unresolved — I will not stamp a flag on a contested reading.** What both agree: **vol 0.70× = no volume behind the rally**, short-z **rising**. |
| ⚡ **CROWDED-SHORT = turn-conditional squeeze fuel, NEVER a standalone buy → HARD-STOP** | **Nasdaq-100 4%ile (still loaded)** · **WTI 13%ile** · **DINO (5.2% float short, building, skew +15.6)** | **Stamped.** ★ **The run's own failure class 2 is binding here: positioning may only AMPLIFY a proposition that already has its own catalyst; it may never BE the proposition.** The 4%ile Nasdaq short is **not** a reason to unwind UW-IT — but it **is** the tail UW-IT must be sized for. |
| 🔴 **EXTREME SHORT — held position** | **LNG (short-vol z +3.09)** | **Stamped.** The most extreme positioning reading in the run, on a **book position held at 9.87%**. Not a thesis name — a **risk** name. |
| ⚠ **SHORTS BUILDING against a "resilient" name** | **NVDA (z +1.67 spike, 1.3% float building, skew +12.5)** | **Stamped.** The order-flow tell that news cannot see: NVDA's price held while shorts pressed. **This is the single piece of evidence pointing at verdict (a) over P2′.** |
| ✅ **CLEAN RISE** (low-short / short-cover) | **PNC (z −0.62, −6.3▼)** · **PSX (z −1.43, −16.6▼ — nearly the ≤−1.5 exit threshold)** | The only two clean-rise signatures in the run. ⚠ **MU's shorts are COVERING** (2.8% float, DTC 0.6) as it fell −12.9% — **shorts taking profit, not pressing.** Consistent with P2′ (positioning event), not with a demand collapse. |

> **ALPHA's net read:** the **bettable-now** set is narrower than the *interesting* set. **🟢LIVE: FIN-curve
> (PNC), HLTH-rotation, ENRG-crack, META.** Everything touching the AI complex is **🟡PARTIAL with an
> unresolved order-flow contradiction (NVDA z +1.67)**, and **three theses were dropped outright.**
> The freshest thing on the board (`bank earnings` **16.29×**) and the most un-crowded (`drug pricing`
> **20 hits**) are **not** the loudest (`AI capex` 332 hits — and **🔴FADING at 0.47×**).

---

# §6 What this sheet does NOT contain (P4 — the denominator of my own coverage)
- **Screener setups: zero** — the tool is broken (§0). The "names you didn't already know" leg is **absent**, and the only genuinely new name on this sheet (**DINO**) came from a **human-directed DEEP chain-hop**, not from the screener.
- **Chain-hop promotions: FIN 0 of 3 · HLTH 0 · SEMI 0 · ENRG 1 (DINO).** Three of four sectors surfaced candidates that **failed the flow cross-check and were dropped** — as the rule requires ("a co-mention alone is NOT a candidate").
- **ROE / margins / revenue-growth: blank for every name** — `module_fundamentals_us` returned none. **Not estimated.**
- **No target prices, no position sizes, no buy/sell calls.** Sizing language above is *influence illustration* only.

# §7 `module_math_check`
Run on this file. ⚠ **Honest scope statement:** the module validates **weighted averages, peer averages, and target-price upside consistency** — **this sheet carries no target prices and no weighted/peer-average tables**, so its checks are **structurally inapplicable here**. Reported as run-with-no-applicable-checks rather than claimed as a pass. Derived figures on this sheet were verified independently at source (e.g. MU forward PE = 853.20 / 150.47 = 5.67 ✓ matches the module's 5.6704; MU % off high = 853.20 / 1,255.00 − 1 = −32.0% ✓; MU rev QoQ = 41,456 / 23,860 − 1 = +73.7% ✓ (reported as +74%); 2s10s = 4.55 − 4.13 = +0.42pp ✓).

---
**EXIT CHECK:** ✅ Every DEEP sector has a section (FIN §1 · HLTH §2 · ENRG §3 · SEMI §4, each with §A–§E) · ✅ cross-sector LIVE_SHORTLIST names **included (META/CTAS/FAST) or explicitly dropped with reason (PYPL — M&A artifact)** · ✅ numbers cross-checked XBRL↔yfinance with **artifacts flagged (ASML/ABBV/TSM P/B) and blanks left blank (ROE/margins, INTC trailing PE)**; `math_check` run with its **inapplicability stated honestly** · ✅ flow/positioning cross-read present per candidate (**short-z surfaced two tells: NVDA +1.67 spike, LNG +3.09 extreme**) · ✅ **epicenter-starter module present (§3a) — the GAP was real, the tool's ✅ was an artifact** · ✅ written as ONE file.
**→ proceed to ALPHA.**
