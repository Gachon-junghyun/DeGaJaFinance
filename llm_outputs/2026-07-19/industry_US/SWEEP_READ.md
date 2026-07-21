# SWEEP read — industry_US · 2026-07-19 (Stage 2 / L1·SWEEP)

> Non-load-bearing scratch note so ROTATION can reread the sweep instead of trusting memory.
> Load-bearing artifacts written by this stage: `SECTOR_FLOW_US.json` · `US_LIVE_SHORTLIST.json` ·
> `../CYCLE_EXPOSURE.md/.json`.
> **asof = 2026-07-17 close.** ⚠ The 07-18 US combat deaths and the 07-19 US strike on the IRGC are
> **not in these numbers.** Same caveat as MACRO §"most important".

## Universe (us_top300)
`n=300 · universe wflow **−0.084** · 🟢 9 / 🔴 69`
**The whole board is red.** 69 red vs 9 green with a negative universe wflow — this is the number
that qualifies MACRO's "rotation, not de-risking" read. It is a rotation *inside a falling tape*.

## Sector ranking (wflow desc) — `sector_flow.py --market us --json`
| Rank | Sector | n | wflow | eqflow | 🟢 | 🔴 | breadth | **delta** | Read vs MACRO §4 matrix |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **Health Care** | 32 | **+0.429** | +0.314 | 1 | 2 | 0.03 | +0.072 | ★ **AGREE — strongest agreement in the run.** Matrix promoted HLTH to OW on flow (P7); the sweep independently ranks it #1 by a wide margin, and eqflow +0.314 says it is **broad, not one-name** |
| 2 | **Financials** | 47 | +0.174 | **+0.316** | **5** | 6 | **0.11** | −0.008 | **AGREE on tilt, DISAGREE on driver** — eqflow > wflow = **broad, not mega-cap-narrow**; best breadth on the board. But **delta −0.008 = the only negative-delta sector** (cooling) |
| 3 | **Utilities** | 15 | +0.105 | +0.098 | 0 | 0 | 0.00 | +0.056 | ⚠ **DIVERGE (b): flow-led sector the matrix under-rated** (matrix = "Neutral, weak"). Zero 🟢, zero 🔴 — quiet accumulation, not ignition |
| 4 | Consumer Disc | 28 | +0.088 | **−0.035** | 0 | 6 | 0.00 | +0.069 | **AGREE with the matrix's Neutral→UW** — positive wflow with **negative eqflow = mega-cap-narrow**, 6 red |
| 5 | **Real Estate** | 12 | +0.045 | +0.056 | 1 | 3 | 0.08 | **+0.091** | ⚠⚠ **DIVERGE (a) — now confirmed by a 2nd independent source.** Matrix says UW on real 10Y 2.35%; sweep says **2nd-fastest delta** + a new-🟢 (PSA) |
| 6 | **Energy** | 16 | +0.030 | +0.033 | 0 | 2 | 0.00 | **+0.181** | ⚠⚠ **DIVERGE (c) — the run's sharpest.** Matrix ranks ENRG the **#1 OW**; the sweep ranks it **6th by level** — but its **delta +0.181 is nearly 2× any other sector**. Level = late; delta = igniting |
| 7 | Industrials | 50 | −0.121 | −0.072 | 1 | **13** | 0.02 | −0.014 | **Matrix "Neutral" is generous** — 13 red of 50 |
| 8 | **Information Tech** | 56 | −0.147 | **−0.313** | 0 | **24** | 0.00 | −0.052 | ★ **AGREE, emphatically.** Worst eqflow and worst breadth on the board (24 red / 56). UW confirmed by flow |
| 9 | Consumer Staples | 19 | −0.164 | **+0.077** | 0 | 4 | 0.00 | +0.083 | **Split**: mega-cap drag, positive breadth. Matrix Neutral survives |
| 10 | Materials | 12 | −0.280 | −0.234 | 0 | 4 | 0.00 | +0.024 | ★ **AGREE — UW confirmed both ways** |
| 11 | **Comm Services** | 13 | **−0.416** | **+0.017** | 1 | 5 | 0.08 | +0.027 | ⚠ **Worst wflow on the board is a MEGA-CAP problem, not a sector problem** (eqflow +0.017). And META itself is fs 0.678 / OBV accumulating / RS20 +13.5. The matrix's flat UW is too blunt — **DIVERGE (d)** |

## new-🟢 ignitions (day-over-day) — 7 names, and they tell one story
| Ticker | Sector | Industry | flow | RS20 | vol |
|---|---|---|---|---|---|
| TRV | Financials | **P&C Insurance** | 0.828 | +20.2 | 1.29 |
| CB | Financials | **P&C Insurance** | 0.774 | +7.1 | 1.26 |
| PGR | Financials | **P&C Insurance** | 0.553 | +1.4 | 1.29 |
| NDAQ | Financials | **Financial Exchanges & Data** | 0.753 | +9.7 | 1.20 |
| ABT | Health Care | Health Care Equipment | 0.744 | +13.4 | 1.39 |
| EA | Comm Services | Interactive Home Entertainment | 0.619 | +2.6 | 1.32 |
| PSA | Real Estate | Self-Storage REITs | 0.460 | +1.4 | 1.21 |

★ **The single most useful finding of this stage: 4 of the 7 ignitions are Financials, and NOT ONE of
them is a bank.** Three P&C insurers + one exchange. The MACRO §4x(b) divergence — "FIN's flow is
intact but its steepener thesis is broken" — is **resolved by composition**: the money entering FIN is
going to **insurance (underwriting/float, which a hike HELPS) and exchanges (volatility volume, which
VIX +24.9% HELPS)**, not to the lending-spread trade the steepener thesis described.
**This is a different FIN bet than the one the OW was written for.** → hand to DEEP.

Secondary: **ABT** (new-🟢, vol 1.39 — the run's highest) independently corroborates P7/HLTH after
07-17 DRIFT's ISRG burst. **PSA** corroborates the RE divergence. **EA** is the one COMM green — an
un-AI, un-capex COMM name igniting while the mega-caps drag: the (d) divergence in a single ticker.

## LIVE shortlist — `US_LIVE_SHORTLIST.json` (mcap≥$10B · 🟢가속 · top15 → 9 names)
| Ticker | flow | OBV | RS20 | FINRA short z | verdict |
|---|---|---|---|---|---|
| PYPL | +1.00 | +0.50 | 34.1 | +0.06 | △ normal |
| CTAS | +0.93 | +0.34 | 20.2 | −0.13 | △ normal |
| TRV | +0.83 | +0.50 | 20.2 | +0.28 | △ normal |
| CB | +0.77 | +0.23 | 7.1 | +1.14 | △ normal |
| NDAQ | +0.75 | +0.15 | 9.7 | +0.93 | △ normal |
| ABT | +0.74 | +0.09 | 13.4 | +0.80 | △ normal |
| EA | +0.62 | +0.31 | 2.6 | −0.30 | △ normal |
| **PGR** | +0.55 | +0.31 | 1.4 | **−1.44** | ★ **✅ low-short / short-cover (clean rise)** |
| PSA | +0.46 | +0.14 | 1.4 | +0.08 | △ normal |

★ **Clean-rise (🟢 AND low-short): PGR only.**
⚠ Protocol reminder honored: the US has **no investor-type feed** — FINRA short-z is a *positioning*
proxy, and `crowded-short` is squeeze fuel **conditional on a turn**, never a standalone buy. Nothing
here is a recommendation; these are candidates handed to DEEP/BET.
⚠ **Note what the shortlist does NOT contain: not one refiner, not one energy name.** The filter is
`tag == 🟢가속`, and VLO/MPC/PSX sit at 🟡중립 despite RS20 +23–29%. **The strongest price lane in the
report is structurally invisible to this screen.** Named, not hidden — DEEP must reach ENRG by the
matrix, not by this list.

## 🚨 CYCLE EXPOSURE GAP → hand to ALPHA's action bracket
`cycle_exposure.py --json` → `llm_outputs/2026-07-19/CYCLE_EXPOSURE.md`
Book ≈ **$7,902** total · $5,186 invested.

| Cycle | rank | epicenter % | need ≥ | any-layer % | held | GAP |
|---|---|---|---|---|---|---|
| AI-compute / semiconductors | 1 | 12.3% | 12.0% | 42.07% | AVGO, NVDA, TSM | ✅ |
| **Energy / oil-refining (Hormuz + Russia crack)** | **2** | **0.0%** | **8.0%** | 23.87% | *(none)* | 🚨 **GAP −8.00pp** |
| Missile-defense / rearmament | 3 | 9.8% | — | 9.8% | RTX | ⚪ n/a (no threshold set) |

★ **The 07-17 DRIFT flagged this cycle as an unconfigured stub (`min_epicenter_pct = 0.0`,
`core_pick = None`) and said "the Energy epicenter GAP is REAL". It has since been configured, and
the GAP prints for real: 0.0% against a required 8.0%.** The book touches the cycle only via
adjacent/fuel names (KMI, LNG) — *"beta to the consequence, none to the engine."*

**Why this is the run's most actionable line:** the epicenter of that cycle is exactly **P3′** —
refining — which is **the strongest price lane in the whole report** (VLO RS20 +28.8%, MPC +27.5%,
PSX +23.4%, record margins) and the one MACRO argued is **anti-fragile to a TACO/ceasefire** because
destroyed refining capacity does not return in a session.
⚠ Per the rule: a 🔴 tape gates ADD *timing*; it never justifies zero core in a rank≤2 cycle.
⚠ Counter-weight for PREMORTEM: the tape is **pre-escalation**, RS20 is already +23–29%, and a
ceasefire is a live undated binary. "Establish core" ≠ "chase Monday's gap".

## ✅ EXIT CHECK
- [x] sector_flow sweep → `SECTOR_FLOW_US.json`; 11-sector ranking read (wflow **and** eqflow), new-🟢 read (7, composition analyzed)
- [x] `US_LIVE_SHORTLIST.json` written; FINRA short-pressure verdicts read (PGR the only clean rise); the screen's ENRG blind spot named
- [x] CYCLE_EXPOSURE GAP read — **🚨 Energy/oil-refining rank-2, 0.0% vs 8.0% → handed to ALPHA's action bracket**
- [x] asof (2026-07-17) stated and the post-close escalation flagged against every number
**→ proceed to EVENT_ALPHA.**
