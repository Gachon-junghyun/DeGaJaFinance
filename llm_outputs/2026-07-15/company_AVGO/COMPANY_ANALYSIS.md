# COMPANY ANALYSIS — AVGO (Broadcom Inc.)
**Desk:** 광기 (HYPER) US paper book · **Decision:** TRANCHE-ADD (coil-add) · **Date:** 2026-07-15
**Held:** 1.7 sh @ avg 365.86 · stop 360 · target 524 · **Live px 389.11** (asof 2026-07-14 close)
**Add trigger:** settled close > 392.59 + OBV→누적

> Verdict labels: [검증함] = verified against primary/company source · [차트만] = chart-only · [직감] = judgment call.

---

## SEED-NUMBER AUDIT (load-bearing figures) — do first

| Seed claim | Verified? | Finding |
|---|---|---|
| Apple deal ~$30B through 2031 | **[검증함] TRUE, with a caveat** | Announced 2026-07-08. Apple "commits over $30B" — a multi-year **purchase commitment** (stronger than a framework MOU), >15B U.S.-made chips, +$1.5B Colorado FBAR fab expansion. BUT the deal is **RF/wireless connectivity (FBAR filters) + *some* custom ASIC — NOT AI XPU accelerators.** |
| Apple book = "captive-ASIC floor" | **[검증함] partially — floor is REAL but SMALL** | $30B / ~5.5 yrs ≈ **$5.5B/yr ≈ 5–7% of revenue** (TTM rev $75.5B; Q2 run-rate $22.2B/qtr → ~$89B annualized). A rate-agnostic floor, yes — but modest. Its bigger value is **RETENTION**: it reverses Apple's multi-year threat to in-house Broadcom's wireless silicon. De-risks a standing bear case; does *not* by itself carry the thesis. |
| AI-semi revenue run-rate | **[검증함] TRUE** | Q2 FY26 (ended 2026-05-03) **AI semi revenue $10.8B, +143% YoY** (≈$43B annualized and climbing). Semiconductor segment $15.0B; Infra software $7.18B; consolidated $22.19B (XBRL 10-Q: $22,187M [검증함]). |
| Custom-ASIC/XPU backlog | **[검증함] TRUE** | Company cites **~$73B committed customer backlog**; CEO Hock Tan: "line of sight to >$100B AI chip revenue in 2027." Six confirmed custom customers (Google TPU, Meta MTIA, OpenAI, Anthropic + 2). Counterpoint models AVGO ~60% of custom-ASIC market by 2027. |
| VMware / software-mix margin | **[검증함] TRUE** | Infra software $7.18B/qtr (+9% YoY), ~80%+ gross margin, is the margin ballast behind consolidated **non-GAAP op margin 67%** (record). The June Q dip was a *software-growth* miss (VMware decel), not a semi miss. |

**Seed verdict:** The alpha line is *directionally correct* but the framing overweights Apple. The thesis's own structure separates "Apple floor" from "funded-compute XPU leg" — good — but the Apple floor is ~6% of revenue and mostly RF, so **the compute leg (XPU backlog) is doing ~90% of the work.** Trade the ASIC backlog; treat Apple as insurance, not thesis.

---

## PHASE 1 — BUSINESS MODEL & MOAT

Two engines. **(1) Semiconductor Solutions ($15.0B/qtr, 68% of rev):** networking/custom-silicon. The crown jewel is **custom AI accelerators (XPU) + the switch/optical fabric (Tomahawk/Jericho) that ties clusters together** — Broadcom is the merchant-silicon partner hyperscalers use to design *away from* Nvidia's margin. Moat = deep co-design relationships + FBAR/RF filter dominance + serial-M&A scale. **(2) Infrastructure Software ($7.18B/qtr, 32%):** VMware + CA + Symantec, run as a subscription-converted, high-margin annuity.

Moat quality: **wide but customer-concentrated.** The XPU franchise depends on a handful of hyperscaler programs; a single program slip (or a customer insourcing) is a real notch. Offsetting: switching costs on co-designed silicon are enormous, and the fabric (networking) attaches regardless of whose accelerator wins.

## PHASE 2 — QUALITY OF EARNINGS (the skeptic's phase)

All figures FY2025 (ended 2025-10-31), yfinance/XBRL [검증함]:

- **Cash conversion is pristine.** Operating CF **$27.5B** > Net income **$23.1B** → CF *exceeds* GAAP earnings (accruals clean; the gap is non-cash VMware amortization added back, not aggressive accruals). FCF **$26.9B** (capex only $0.6B — fabless).
- **Capital return covered 1.5x.** Dividends $11.1B + buybacks $6.3B = **$17.4B returned vs $26.9B FCF.** Dividend is not stretched (payout ~41%).
- **VMware debt load is serviceable.** Total debt **$65.1B** (down from $67.6B), cash $16.2B → net debt ~$49B. Net-debt/EBITDA ~**1.4x** (lower on TTM EBITDA). Interest expense $3.2B is **covered ~8x by FCF.** Debt is not a constraint on the add.
- **★ The decisive QoE finding — the scary trailing PE is an accounting artifact, not a quality problem.** Trailing GAAP EPS $5.99 → **PE 65**; forward EPS $19.4 → **PE 20**. The gap is ~$8–9B/yr of VMware intangible amortization depressing GAAP net income (FY2024 net income was only $5.9B for the same reason). **Tangible book is negative** (goodwill $97.8B + other intangibles $32.3B = $130B > equity $81.3B), so P/B 21x is meaningless noise. This is normal for a serial acquirer — but it means: **ignore trailing PE and P/B; the honest lens is forward PE 20 + FCF yield ~1.5%.**
- **Balance-sheet hygiene clean:** inventory only $2.27B on $63.9B rev (lean DIO, no channel bloat); receivables in line. No one-time distortions beyond the standard acquisition-amortization drag.

**QoE grade: HIGH.** Earnings are cash-backed; the only "distortion" is the GAAP/non-GAAP amortization wedge, which flatters neither cash nor the forward number.

## PHASE 3 — VALUATION & "CHEAP IS GUILTY UNTIL PROVEN"

Peer screen [검증함] (yfinance):

| | fwd PE | trail PE | P/S | PEG | op margin | rev |
|---|---|---|---|---|---|---|
| **AVGO** | **20.1** | 65.0 | 24.5 | 0.45 | 49% | $75.5B |
| NVDA | 16.5 | 32.4 | 20.2 | 0.65 | **66%** | $253B |
| MRVL | 36.0 | 76.4 | 22.9 | 1.33 | 14% | $8.7B |
| AMD | 41.1 | 183 | 23.9 | 1.34 | 14% | $37.5B |
| QCOM | 16.2 | 19.2 | 4.2 | 0.60 | 22% | $44.5B |

**AVGO is NOT cheap and is already re-rated.** P/S 24.5x is the richest in the group; forward PE 20 *looks* reasonable and PEG 0.45 *looks* cheap — **but both embed the $100B-AI-by-2027 narrative** (forward EPS $19.4 requires backlog to convert ~2.5x from here). That is circular: the multiple is "cheap" only if the story it's pricing lands. **The trap is live:** within AI-semi, **NVDA is actually cheaper on forward PE (16.5 vs 20.1) with far higher margins (66% vs 49%)** — so AVGO is *not* the value pick; it is priced for **ASIC share-gain**, i.e., paying up for the merchant-XPU thesis specifically. If AI revenue tops out at ~$60–70B instead of $100B, the forward multiple re-rates down, not up.

## PHASE 4 — TECHNICAL / CHART-STRUCTURE READ (verbatim desk read)

```
OBV: 누적(매수압력↑) (20d기울기 +91%)   [STRONG accumulation]
다이버전스: 강세(가격 저점↓ · RSI 저점↑)   [BULLISH divergence]
MA정렬: 혼조 · 가격 2/4 MA 위   [mixed, price above 2 of 4 MAs]
볼린저: 수축(코일링) 13.5% · 중단   [coiling]
RSI: 53.8 · 모멘텀20d −1.1%
턴-판정: PULLBACK-TO-SUPPORT (추세 눌림목)
트리거(점화): close>392.59 + OBV→누적 / 스탑(스윙저점): 360.45
```
Multi-axis flow: 🟡중립 · OBV 중립 · RS20 +0.5% / RS60 −9.5% · vol 0.84x · short 1.5% float building · options P/C 1.03, skew +7.2 (fear-hedged pullback).

**Fundamentals vs the turn — RECONCILED, CONFIRMING.** The pullback is **multiple digestion, not thesis-break**: Q2 was a *record* (op margin 67%, AI +143%); the only blemish was VMware software-growth decel — a mix issue, not deterioration. OBV +91% accumulation *into* a coil, with the fresh Apple commitment (July 8) landing into the base, means strong hands are absorbing supply while the front-end de-rate plays out. RS60 −9.5% shows the name has *lagged* the AI-semi complex — consistent with a coil that hasn't yet fired, not a top. **The chart turn and the fundamental record are pointing the same way.** No contradiction to flag.

---

## TRADING VERDICT

**CONDITIONAL GO — arm the coil-add; fire only on a settled close > 392.59 with OBV confirming. STAND DOWN below.**

The XPU-backlog thesis is verified and cash-backed (QoE HIGH), the pullback is digestion not deterioration, and the fundamental and chart reads confirm each other. This clears the add gate — **but sized modestly**, because (a) valuation is re-rated (NVDA is cheaper per unit of AI), and (b) the Apple "floor" is smaller than the seed implies.

**Asymmetry — honest numbers (push back on the ~6:1 claim):**
- **Chart-stop R/R** at entry 392.59, stop 360.45 (risk $32.14) to target 524 (reward $131.41) = **4.1:1** — *not 6:1*. The tight swing stop mechanically flatters it; to reach 6:1 you'd need a ~$553 target.
- **Fundamental-value asymmetry** from 389: bull ~$620 (FY27 non-GAAP EPS ~$28–32 @ ~22x if $100B AI lands) = +59%; bear ~$300 (backlog converts slow, multiple compresses to ~15x on ~$20 EPS) = −23%. → **~2.6:1.** The real business asymmetry is closer to **2.5–3:1, not 6:1.** The Apple floor removes some left-tail (retention win) but is ~6% of revenue — it does *less* work than the thesis claims.

**Decision:** the 6:1 headline is inflated; the *tradeable* edge is a ~4:1 chart-stop bet on a confirmed coil-break, riding a ~2.6:1 fundamental tailwind. That is enough for a **core-add, not a max-add.**

### Required summary fields
1. **Verdict:** CONDITIONAL GO — arm coil-add, fire on settled close > 392.59 + OBV→누적; stand down below. Size modest (core-add, not max).
2. **Fundamental asymmetry NUMBER:** **~2.6:1** business-value (bull $620 / bear $300 from 389); ~4.1:1 chart-stop. **The desk's ~6:1 is inflated** by the tight swing stop.
3. **Decisive QoE finding:** Op-CF $27.5B **> net income $23.1B** (cash-backed, clean accruals) and FCF $26.9B covers dividend+buyback 1.5x AND services $65B VMware debt (interest covered 8x). The scary trailing PE 65 is a **VMware-amortization artifact** (tangible book negative); honest lens = forward PE 20.
4. **Dated catalyst:** **Q3 FY2026 earnings — Sept 4, 2026** [검증함, yfinance calendar]. Guided rev ~$29.4B (+84% YoY), non-GAAP op margin ~67%. Next backlog-conversion proof point toward the $100B-AI/2027 line.
5. **The ONE decision variable:** **Does a settled close > 392.59 print with OBV still accumulating?** (Fundamentals/QoE already clear the gate; the only open question is trigger confirmation.) The secondary, slower variable: does AI backlog convert toward $100B — judged Sept 4.

---
*Sources: yfinance (px/financials/cashflow/balance sheet/calendar), SEC XBRL companyconcept (10-Q/10-K revenue), Apple-Broadcom deal coverage (CNBC/Yahoo/Supply Chain Dive, 2026-07-08), Broadcom Q2 FY2026 8-K/PRNewswire (2026-06-03). Verified 2026-07-15.*
