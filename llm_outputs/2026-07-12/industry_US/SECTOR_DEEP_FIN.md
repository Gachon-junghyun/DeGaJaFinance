# SECTOR_DEEP_FIN — US Financials

**Date:** 2026-07-12 · **Phase 2 (DEEP)** · English-only runtime · Desk: US Industry
**Sector heat:** FIN flagged this run (freshest rotation). **Tilt:** OW (M-01 NIM + M-08 breadth) with an explicit M-06 credit-cost caveat.
**Sources:** `[SEC]` module_business_us 10-K (period 2025-12-31 unless noted) · `[FINRA]` us_flow.py Reg SHO daily (as of 2026-07-10) · `[news]/[daily-US]` news_alert.db foreign slice · `[WebSearch]` Q2 dates + credit-event specifics · `[FRED]/[COT]` via MACRO_REPORT.

---

## 0. The binding question (state it up front)
The binding question for FIN this run is **NOT loan demand and NOT NIM direction** — both are tailwinds. It is: **do rising credit costs (AI-vendor-finance, private-credit/BDC, CRE, subprime consumer) offset the higher-for-longer NIM tailwind before Q2 earnings prove it either way?**

- **The tailwind (M-01 + M-08):** Fed funds 3.62% flat, 10y 4.54% (+16bp/wk), 2s10s +38bp **bear-steepening** `[FRED]`. A positively-sloped curve + no-cut regime = banks fund cheap short, lend/reinvest dear long → **NIM expansion**. Breadth rotation out of Mag7 (−$2.3T in June) into value pushed the Dow to a record ~52,000; JPM at all-time high, MS pairing a dividend hike with a **$20B buyback** `[news]/[daily-US]`.
- **The tail (M-06):** The **First Brands + Tricolor** collapse is the credit-cost anti-signal made concrete — ~$2B aggregate marked losses across ≥11 institutional lenders (BDCs, CLO equity, SMAs), private-credit receivables fraud, and **JPMorgan carrying direct Tricolor (subprime auto) losses** `[WebSearch]`. Layer on AI's ~$182B borrowing spree + vendor-financing circularity (Nvidia as landlord/lender) `[news]`. A single neocloud/leveraged-loan default that "surprises" turns the NIM story into a **provisioning cycle**.

**Near catalyst (resolves it):** Q2 bank earnings **kick off July 14** (JPM, WFC, C before the bell) and **July 15** (BAC, MS, GS, PNC) `[WebSearch]`. This report is written into that catalyst — the tape has 2–3 days before the thesis is marked to market.

---

## 1. Flow — short-pressure overlay `[FINRA]` (Reg SHO daily short-volume ratio, 2026-07-10)
z = deviation vs each name's own 20-day base; short% 40–45% is normal (includes MM hedging). 5v5 = 5-day-vs-5-day trend.

| Name | Short% | z | 5v5 | Read → thesis translation |
|---|---|---|---|---|
| **BAC** | 52.7% | **+1.70** 🔴 | +3.6▲ | **Short surge into its own base** — the one money-center flashing pre-earnings hedging / credit-worry. Reports **07-15**. Watch NCOs + card credit. |
| **CB** (Chubb) | 37.6% | **−1.59** 🟢 | −19.1▼ | **Short cover / pressure exit** — the cleanest de-risking signal in the panel; insurer float-earnings story getting a bid. |
| CME | 40.3% | +1.40 | +13.3▲ | Elevated + rising, but off a low 25.6% base — reads as volume/volatility positioning, not distress. |
| HOOD | 64.5% | +1.38 | +2.0▲ | Structurally high short%; within its own range — retail-broker beta, not a fresh signal. |
| AXP | 65.3% | +1.38 | +4.0▲ | High short% but in-range for AXP; the card-credit-cost watch name (see §5). |
| SPGI | 52.1% | +0.37 | +14.6▲ | Rising trend post Mobility spin-off (see §4); positioning churn, not stress. |
| PGR | 58.2% | +0.90 | +10.2▲ | Rising but in-range; auto-insurer pricing-cycle name. |
| JPM | 44.8% | −0.24 | +4.3▲ | Normal. No pre-earnings short build despite ATH — market not fading the leader. |
| C / MA / V / COF / BX / BNY / BLK / MS / GS / WFC / SCHW | — | −1.25 … +0.46 | mixed | **All 🟡 normal range** — no divergence. C (−1.25) and V (−0.93) lean short-covered. |
| BRK-B | — | no data | — | Reg SHO feed blank this pull. |

**Flow read:** The panel is calm — no sector-wide short assault. Two names carry the signal: **BAC short-surge (z+1.70) = the pre-earnings credit-cost worry has a name**, and **CB short-cover (z−1.59) = the insurance-float leg is de-risking**. Everything else is positioning noise. `[COT]` context: Nasdaq crowded-SHORT 4%ile (rebound ammo under the AI-wobble that is *feeding* the breadth rotation into FIN); S&P lean-short 77%ile.

News-velocity (foreign slice, 14–21d, `[news]`): dominant FIN threads are (a) MS dividend+$20B buyback, (b) Dow record "on borrowed strength" breadth rotation, (c) Circle/stablecoin margin compression ("Open USD Is Coming for Circle's Margins," Circle −45% on the month), (d) FS Credit / BDC distribution declarations (private-credit plumbing still paying), (e) S&P Global completed **Mobility spin-off**. Blind-spot: stablecoin/prediction-market plumbing is a *structural* FIN shift (constructive for V/MA rails via Visa Direct; destructive for pure-play issuers like Circle) — under-covered by the fixed bank-earnings search terms.

---

## 2. Players — SEC Item 1 / 1A read `[SEC]` (10-K, period 2025-12-31 unless noted)
Separated into **NIM/breadth beneficiaries** vs **credit-cost-exposed**. Item 1A is the anti-signal lens.

### NIM / breadth beneficiaries (the tailwind names)
- **JPM** — 10-K filed 2026-02-13. $4.4T assets, $362.4B equity; leader across IB / consumer / commercial / transaction processing / asset mgmt. Risk factors are the standard bank stack (market, **credit**, liquidity, capital). **The tell:** the *breadth-rotation leader* (ATH) AND a **named credit-cost carrier** — direct Tricolor subprime-auto losses `[WebSearch]`. Best single lens on "does NIM beat credit." Last earnings 8-K 2026-04-14 (Q1); **Q2 = 07-14**; a 06-24 Reg-FD 8-K (Item 7.01) sits in the window (likely post-CCAR capital/dividend). Est Q2 EPS $5.44, +9.7% y/y `[WebSearch]`.
- **MS** (Morgan Stanley) — 10-K filed 2026-02-19. FY25 net revenue **$70.6B (+14%)**, net income **$16.9B (+26%)**, **ROTCE 21.6%**, CET1 **15.0%**, efficiency 68%. Wealth Mgmt $31.8B + Institutional Securities $33.1B (strong Equity + IB/Advisory). **Cleanest breadth/capital-markets beneficiary** — annuity wealth fees + reviving IB, and the $20B buyback signals excess capital, not credit anxiety. Reports **07-15**.
- **GS** (Goldman) — 10-K filed 2026-02-25. Global Banking & Markets + Asset & Wealth Mgmt. Item 1A is market/volatility/credit-market-liquidity heavy (market-making, "net long positions," credit-spread/funding). Pure capital-markets + trading-volume beta on the breadth rotation; less deposit-NIM, more fee/volatility levered. Reports **07-15**.
- **CB** (Chubb) — insurer; **float earns more at higher-for-longer** (the insurance analog of NIM) and the FINRA short-cover (z−1.59) marks it de-risking. (Read via panel; BRK-B feed blank.)

### Credit-cost-exposed (the tail names)
- **BAC** (Bank of America) — 10-K filed 2026-02-25; streamlining legal-entity structure. Item-1A bullets didn't parse cleanly this pull, but the **FINRA short-surge (z+1.70)** flags it as the pre-earnings worry name — the market is hedging BAC's consumer-credit / NCO print. Reports **07-15**, est EPS $1.12 (+~25% y/y) `[WebSearch]`.
- **COF** (Capital One) — 10-K filed 2026-02-19. **Just completed the Discover acquisition** → now a diversified issuer **AND owns the Discover payments network** (a 4th US network alongside V/MA/AXP). Item 1A is dominated by **Discover-integration risk** ("may fail to realize benefits," "substantial expenses") **plus** the raw consumer-credit stack: "increases in delinquencies and credit losses, or… incorrectly estimate expected losses → inadequate reserves," "fluctuations in interest rates." The single most integration-AND-credit-exposed name in the panel — subprime-consumer NCOs are its P&L.
- **AXP** (American Express) — 10-K filed 2026-02-06. Premium-spend card network + lender; the "Synchrony credit numbers improving even as inflation bites" `[news]` cross-read is constructive, but AXP carries direct card-credit-cost exposure and a structurally high short% (65%).
- **BX** (Blackstone) — 10-K filed 2026-02-27. **World's largest alt manager, $1.3T+ AUM**, incl. a large **credit** strategy. Item 1A this pull is competition-framed (fee pressure, cost-of-capital), but BX is the **direct read-through on the private-credit cycle** (the M-06 epicenter). An earlier Apollo-fund gate + First Brands/BDC marks are the tape; BX's credit AUM is where a private-credit provisioning cycle would first show. Fee-related earnings are annuity-like; realizations are cyclical.
- **PGR** (Progressive) — 10-K filed 2026-03-02. Auto/property/commercial insurer. Risk stack = insurance (loss-reserve accuracy), market (portfolio value), **credit**, liquidity. Higher rates lift investment income on float (tailwind) but the binding variable is loss-cost/severity trend, not NIM.

**One-line separation:** NIM/breadth compounders = **JPM (leader), MS/GS (capital markets), CB (float)**. Credit-cost tail = **COF (subprime + Discover integration), BAC (consumer NCO worry, FINRA-flagged), AXP (card), BX (private-credit epicenter)**.

---

## 3. IR / filings `[SEC]` + Q2 calendar `[WebSearch]`
- **JPM disclosure pull:** 90-day window shows Q1 earnings 8-K (04-14, Item 2.02), two Reg-FD 8-Ks (06-24 + 04-14, Item 7.01 — the 06-24 is the CCAR/capital-return signal), 3 mgmt-change 8-Ks. No M&A 8-K. 6,674 total filings dominated by 424B2 debt-shelf issuance (**IG issuance machine running** — corroborates M-06 record-issuance backdrop).
- **Q2 earnings calendar (the near catalyst):** **07-14** JPM, WFC, C (pre-bell) · **07-15** BAC, MS, GS, PNC · then USB/COF/regionals into the week. Consensus: JPM $5.44 (+9.7%), BAC $1.12 (+~25%) `[WebSearch]`. The market treats the money-center prints as a read on the whole earnings season and on consumer/credit health.
- **SPGI:** completed **separation of Mobility (automotive data)** into a standalone NYSE-listed company (07-01, `[news]`) — SPGI now a purer ratings+indices+market-intelligence compounder; the FINRA rising-short trend (§1) is spin-off repositioning.

---

## 4. Value-chain / segment map (FIN plumbing, 7 nodes) — AI-credit cross-exposure marked
Map of where a dollar flows through the system, with names and the **AI-credit / private-credit cross-exposure flag ⚠️**.

| # | Node (plumbing) | Names (panel) | NIM lever | ⚠️ AI-/private-credit / CRE cross-exposure |
|---|---|---|---|---|
| 1 | **Deposits / funding** | JPM BAC WFC C USB PNC BNY | Cheap short-end funding = NIM numerator engine | Low direct; deposit-beta/outflow risk if curve re-inverts |
| 2 | **Lending — C&I / consumer / CRE** | JPM BAC WFC C COF | Reprices at higher rates (NIM) | ⚠️⚠️ **CRE + subprime consumer (COF/Discover) + C&I to leveraged borrowers**; warehouse lines to private-credit funds |
| 3 | **Capital markets / IB / trading** | MS GS JPM(CIB) C | Fee + volatility beta (breadth rotation) | ⚠️ leveraged-loan underwriting / bridge risk (First Brands-type BSL) |
| 4 | **Payments rails** | V MA AXP **COF(+Discover)** | Volume/spend beta; rate-agnostic tolls | ⚠️ AXP/COF card-credit; **stablecoin plumbing** (Visa Direct = constructive; Circle-type issuers = margin-compressed) |
| 5 | **Asset mgmt & private credit / alts** | **BX** BLK BNY (+BDCs: FSCO/FSSL) | Fee-related earnings (annuity) | ⚠️⚠️⚠️ **the M-06 epicenter** — BX credit AUM, BDC marks, First Brands/Tricolor $2B losses, neocloud/vendor-finance direct lending |
| 6 | **Insurance float** | BRK-B CB PGR | Float reinvested at higher rates (NIM analog) | ⚠️ credit-portfolio marks; loss-cost/severity is the real binding variable |
| 7 | **Exchanges / data / ratings** | CME SPGI ICE | Volume + volatility tolls; issuance = ratings fees | Low direct; **benefits from the volatility a credit event would cause** (natural hedge) |

**Cross-exposure verdict:** the AI-credit / private-credit risk concentrates in **nodes 2 + 5** (leveraged/subprime lending and alt-credit AUM) — names **COF, BX, and the BDC layer (FSCO/FSSL), plus JPM via Tricolor**. The **rails + exchanges/data (nodes 4 top-half, 7)** are the *rate-and-credit-agnostic tolls* — V/MA/CME/SPGI collect on volume regardless of who wins the NIM-vs-credit fight (CME/SPGI actually benefit from the volatility a credit scare produces).

---

## 5. Bottleneck + KPI + anti-signal
**Bottleneck (binding constraint):** not loan demand — **the credit-cost trajectory**. Specifically, whether Q2 provisioning (NCOs + reserve builds) stays contained while NIM expands, OR whether a private-credit / AI-vendor-finance / subprime-consumer crack (First Brands/Tricolor as the template) forces a reserve-build cycle that eats the NIM beat.

**KPI dashboard (track through Q2 prints):**
| KPI | Why it binds | Live value |
|---|---|---|
| **NIM** (money-center) | The tailwind's proof; needs to expand with the steepening curve | report card 07-14/15 |
| **Net charge-offs / reserve build** | The tail's proof; subprime-consumer (COF) + card (AXP/BAC) first | report card 07-14/15 |
| **HY & IG OAS** | The single cleanest systemic-credit gauge | **[homeless — R6-K n/a]**; name it, proxy via VIX 15.84 calm + IG issuance running |
| **CET1 / buyback pace** | Excess-capital signal = no credit anxiety (MS $20B, JPM post-CCAR) | MS CET1 15.0%; JPM CCAR 06-24 8-K |
| **Private-credit / BDC marks** | M-06 epicenter; First Brands/Tricolor $2B already marked | BX credit AUM; FSCO/FSSL distributions still paid |

**Anti-signal (what flips OW→UW):**
1. A **credit event** — a neocloud/leveraged-loan/private-credit default (another First Brands/Tricolor) that forces sector-wide reserve builds and turns the NIM tailwind into a provisioning cycle. The FINRA **BAC short-surge (z+1.70)** is the market pre-positioning for exactly this at the Q2 print.
2. A **dovish Fed pivot** (M-01 anti-signal: soft CPI + cooling labor lets Warsh signal a cut) that **flattens the curve and compresses NIM** — kills the tailwind from the other direction. This week's CPI is that fork.

---

## Handoff to Phase 3 (3 lines)
1. **Binding question:** does higher-for-longer NIM expansion (steep +38bp curve, no-cut Warsh Fed) survive rising credit costs (First Brands/Tricolor ~$2B marked, AI-vendor-finance, subprime-consumer) — resolved at the **07-14/15 Q2 bank prints**; CPI this week is the offsetting dovish-pivot fork.
2. **Cleanest NIM/breadth beneficiary → carry: JPM** — the breadth-rotation leader (ATH), NIM + capital-return (post-CCAR) engine, no pre-earnings short build (FINRA normal); **MS is the cleaner *pure* capital-markets/buyback alt** (ROTCE 21.6%, CET1 15.0%, $20B buyback) if you want capital-return without direct subprime credit exposure.
3. **Most credit-exposed name → carry: COF** — subprime-consumer NCO engine **plus** unabsorbed Discover-integration risk (Item 1A dominated by both); **BX is the systemic private-credit-cycle read-through** and **BAC the FINRA-flagged (z+1.70) money-center worry** — watch all three provisioning lines at the Q2 prints.
