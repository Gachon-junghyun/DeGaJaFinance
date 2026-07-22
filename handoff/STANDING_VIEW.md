# STANDING_VIEW — the live thesis carried between runs

> Read at HANDOVER (run start). Updated at HANDOVER (run end). Every claim tagged `[measured]`
> (a number we pulled from a primary source) or `[inferred]` (our reading of those numbers).
> **Inferred claims may be carried; they may not be cited as evidence.** Not advice.

**asof 2026-07-22** · next mandatory refresh: after the 2026-07-29 cluster (see SCENARIOS.md)

---

## 1. Regime call

**Memory is a price-cycle industry in rate-of-change deceleration while its level stays tight.**
`[inferred]` — built on the measured chain below.

The distinction that drives everything: in a commodity-cycle industry the equity tracks the
**second derivative of price**, not the level. Level and rate are currently pointing opposite ways,
which is why "shortage persists" and "stocks struggle" are both true and not contradictory.

## 2. The measured chain (this is the evidence; the rest is reading)

| # | Fact | Value | Source | asof |
|---|---|---|---|---|
| M1 | Server DRAM contract price, QoQ | 1Q26 +90~95% → 2Q26 +58~63% → **3Q26 +13~18%** | TrendForce | 2026-07 |
| M2 | Micron gross margin, quarterly | 37.7 → 44.7 → 56.0 → 74.4 → **84.6%** | yfinance x SEC XBRL (4/4 quarters agree <5%) | FQ3'26 |
| M3 | Micron gross margin, annual | FY22 45.2% · **FY23 −9.1%** · FY24 22.4% · FY25 39.8% | same | FY25 |
| M4 | Prior-cycle GM peak | **59%** (Q4 2018) | press | 2018 |
| M5 | Micron FQ3 revenue | $41.5B, +74% QoQ, +346% YoY; FQ4 guide $50B / GM ~86% | company release | 2026-06-24 |
| M6 | Micron forward P/E · forward EPS | **6.31x** · $153.74 (price $970.82) | module_fundamentals_us | 2026-07-22 |
| M7 | New DRAM capacity online | SK M15X + Micron Idaho **mid-2027**; Samsung P5 **2028** | press | 2026-07 |
| M8 | Hyperscaler 2026 capex | **>$800B** (consensus ~$1T for 2027); Alphabet guide $180–190B, 2027 "significantly increase" | press / Alphabet Q1 | 2026-04 |
| M9 | Memory share of hyperscaler capex | ~8% (CY23-24) → **~30% (CY26)** → 48% est. CY27 | SemiAnalysis / CLSA `[est]` | 2026-07 |
| M10 | KR 20d investor flow | 005930 foreign **−40.13M sh** vs retail +31.16M · 000660 −7.22M vs +7.74M · 042700 foreign **+1.40M** | KIS (matches Naver + KRX exactly) | 2026-07-21 |
| M11 | KR short-interest (%float) | 005930 **0.01%** · 000660 **0.01%** · 042700 **5.32% covering** | KRX | 2026-07-22 |
| M12 | KR exports, 1–20th of month | Jul $54.93B (semis $22.11B, +180.6% YoY) vs **Jun $61.9B = −11.3% MoM** | Korea Customs | 2026-07-21 |
| M13 | EDA lead-lag vs SOXX/SMH | same-month **+0.63**; lag-12 **+0.05**; lag-18 **−0.05** (SPY-excess: +0.24 / +0.02 / −0.06) | own calc, 199 monthly obs 2010–2026 | 2026-07-22 |
| M14 | **MU estimate revisions** | +1y EPS **100.53 → 150.91 over 90d (+50.1%)**; breadth **30↑ : 0↓** (30d) | module_fundamentals_us (new axis) | 2026-07-22 |
| M15 | **GOOGL estimate revisions** | Current quarter **1↑ : 4↓** (30d), next quarter 2↑ : 3↓; +1y level +9.7% | module_fundamentals_us | 2026-07-22 |
| M16 | **Credit spreads** | HY OAS **2.69%** (365d low 2.63, −16bp/90d) · IG OAS 0.78% · NFCI −0.54 | module_macro_us (new axis) | 2026-07-20 |
| M18 | **MU gross margin, 17-year series** | peak FY2018 **58.9%** · trough FY2009 −9.2% (FY2023 −9.1%) · median 32.0% → current **84.6% = 100th percentile, +25.7pp over peak** | own calc, SEC XBRL (`scripts/margin_history.py`) | 2026-07-22 |
| M17 | **Implied moves** | GOOGL **±7.1%** (0DTE) · MU ±4.5% · AMD ±3.6% | module_flow --positioning (new axis) | 2026-07-22 |

## 3. Per-name standing theses

| Name | Thesis | Tag | Contamination / caveat |
|---|---|---|---|
| **MU / SNDK / WDC** | Revenue keeps growing on volume; **margin passes its peak**. The 6.31x forward P/E is the arithmetic signature of unsustainable margin, not cheapness. ★ **M14 strengthens this**: the "cheap" denominator rose **+50.1% in 90 days on 30↑ : 0↓** — that is consensus chasing, and revisions turn before price. **A first downgrade in a 30:0 name is a bigger event than the multiple.** | `[inferred]` on M1–M6, M14 | Micron management counters that long-term-agreement **price floors** hold GM above any prior cycle peak. Unverified, and it is the single best counterargument on file. |
| **005930 Samsung Electronics** | The clean bearish flow read of the KR complex — no ADR exists, so M10's −40.13M sh has no venue explanation. | `[measured]` flow, `[inferred]` read | Benchmark-sensitive: **RS20 is +10.1% vs `^KS11` but −12.1% vs SPY.** Always state which. |
| **000660 SK hynix** | **Flow read SUSPENDED until 2026-07-29.** Nasdaq ADR listed 07-10 ($26.5B, largest-ever foreign US listing); ADR traded to +50% over the home line, ~25% now, because two-way conversion is blocked. Foreign "selling" in Seoul is substantially venue migration. | `[measured]` premium, `[inferred]` split | EWY took **$1.1B single-day inflow** as US money bought Seoul shares via the ETF to avoid the ADR premium. Conversion opens **07-29** — the distortion resolves on a known date. |
| **042700 Hanmi Semiconductor** | Different clock: revenue is **capex-driven, not price-driven**. The three DRAM makers are raising 2026 capex +11~23% and fabs run to mid-2027. Equipment cycles lag price cycles and last longer. | `[inferred]` | Only name of the four with foreign buying AND a crowded-short covering (M11). Also RS60 −29.7%, realized vol ~142% annualized. |
| **009150 Samsung Electro-Mechanics** | **UNOWNED — no proposition covers it.** Money leaving (flow −0.811) while RS60 +64.1% sits near the board top. Unresolved, carried deliberately. | — | Flagged by the 2026-07-21 KR desk as an explicit coverage gap. |
| **NVDA / AVGO** | Separate boat from memory. Participated least in the 07-21 memory rally (+2.0% / +2.2% vs SNDK +14.3%). Hyperscaler capex is their driver and it is still rising. | `[inferred]` | Do **not** fold them into a memory verdict. The 07-21 tape separated them by ~10pp in one session. |

## 4. The asymmetry that governs every upcoming print

> **A hyperscaler capex CUT changes the thesis. A capex RAISE only moves its timing.**

A cut breaks both the volume leg and the price leg at once. A raise confirms volume only — it cannot
un-measure M1, because the long-term agreements that cap price increases are signed **by those same
buyers**. Volume up, price-per-unit capped is their explicit strategy.

Encode this before each print, not after.

## 5. Retracted ledger (append-only — these must not resurface)

| # | Claim once made | Killed by | Date |
|---|---|---|---|
| R1 | "SK hynix foreign selling is the strongest bearish datapoint" | ADR venue migration; 07-10 Nasdaq listing, +25~50% premium, conversion blocked until 07-29 | 2026-07-22 |
| R2 | "Semi exports +180.6% is a strong bullish catalyst" | Same release: **−11.3% MoM** on a like-for-like 1–20th window | 2026-07-22 |
| R3 | "Low VIX implies 20d underperformance (t −3.5)" | The source study is **KR-measured**; the same document records **US replication failure**. Cross-market transfer is invalid. | 2026-07-22 |
| R4 | "20-day excess returns are all deeply negative" | Unstated benchmark. Sign flips: 005930 is −12.1% vs SPY, **+10.1% vs `^KS11`**. | 2026-07-22 |
| R5 | "EDA weakness leads semis by 12–18 months" | M13 — lag-12 ≈ 0.02–0.05, same-month 0.63. **Coincident, not leading.** Also SNPS's −66.7% 12m relative is company-specific (guide cut 40%→36%, China −22%, $35B Ansys amortization, open-source EDA demo), not a cycle signal. | 2026-07-22 |
| R6 | "Semiconductor demand is real, therefore the sector turns" | Demand realness was never the disputed variable. The disputed variable is whether the rate of price increase holds. | 2026-07-22 |

## 6. Open contradictions carried deliberately (do not resolve by picking a side)

- **C1 — LTA price floors.** They cap the upside (TrendForce's stated reason for deceleration) *and*
  floor the downside (Micron management's stated reason margins hold). Both cannot be dismissed;
  the cycle's amplitude in both directions depends on which dominates. **Unmeasured.**
- **C2 — 009150 Samsung Electro-Mechanics.** Flow out, relative strength top-quartile. No thesis fits.
- **C3 — Level vs rate.** "Shortage through 2027" (M7) and "price growth decelerating" (M1) are both
  true. Any proposition citing only one is quoting half the state.
