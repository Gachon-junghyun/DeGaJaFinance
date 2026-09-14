# SECTOR DEEP — Financials (FIN) — 2026-08-30

Data asof **2026-08-28** (47 scored names). ⚠ Basis note (stated once, not re-litigated): the 08-28 daily Close was void and repaired with a 5-minute-bar proxy validated at 0.0225% mean / 0.038% max error vs the KIS broker feed (n=9). This is a FULL FRESH MAP — last FIN DEEP was 2026-08-26 (2 runs ago); referenced only where it changes the read, not leaned on.

---

## 0. MANDATE VERDICT — EARLY, TRAP, or the third state?

**THIRD STATE, and the sector label is the wrong unit to answer with a single word.** `XLF`'s +12.19pp exc60 is real, but it is the blended average of three incompatible stories, not one:

1. **Brokers / exchanges-data / asset managers (11 of 47 names, mixed but flow-positive as a bloc) are genuinely EARLY** — OBV accumulating *and* rs60 firmly positive, several still accelerating on rs20 too (`AJG` rs20 +4.3/rs60 +30.1, `BX` +8.4/+27.0, `SCHW` +1.7/+25.2). This bloc is where the 08-28 up-day strength and the 60-day excess actually live.
2. **The Diversified-Banks core (7 names — `BAC` `C` `JPM` `USB` `WFC` `TFC` `PNC`) is the literal THIRD STATE EVENT_ALPHA flagged**: 6 of 7 are OBV-accumulating (매집) while rs20 is flat-to-negative (−0.9 to −6.1pp vs SPY) — money entering, relative strength not yet confirming. `PNC` is the outlier that breaks the pattern: OBV neutral (+0.049, not accumulating) *and* the group's worst rs20 (−6.1). This is quiet re-accumulation, not a breakout and not a distribution — it fails both EARLY (no rs confirmation) and TRAP (no distribution) tests cleanly.
3. **Insurance (P&C + Life/Health + Multi-line, 9 names, $591B combined mcap) is an outright TRAP** — 3 of the sector's 5 total 🔴 red tags live here (`TRV` `ALL` `AFL` `HIG` `AON` all 🔴 or near; `AJG`/`MRSH` insurance-brokers is the exception), OBV distributing across the board (`AON` −0.263, `AFL` −0.393, `HIG` −0.172, `ALL` −0.223, `TRV` −0.149), rs20 negative in every name in the group.

Zero 🟢 names out of 47 and eqflow −0.090 (rank 6/11) are true statements about the **equal-weighted average**, but that average is dragged down entirely by insurance (avg flow −0.512, n=5 P&C alone) and payments (`XYZ`/`PYPL` avg flow −0.466) — it is not evidence against the banks/brokers/exchanges bloc, which never shows red and mostly shows accumulation. `top1_flips_sign` FALSE (no BRK-B sign-flip artifact) confirms the dispersion is real, not an index-construction defect.

---

## 1. Flow read + sub-sector dispersion (the core finding)

Equal-weight avg flow by GICS sub-industry (n=47, this run):

| Sub-industry | n | avg flow | 🟢/🔴 | total mcap |
|---|---|---|---|---|
| Investment Banking & Brokerage | 5 | **+0.210** | 0/0 | $975B |
| Financial Exchanges & Data | 7 | **+0.173** | 0/0 | $497B |
| Asset Management & Custody Banks | 7 | **+0.090** | 0/0 | $668B |
| Diversified Banks | 7 | −0.030 | 0/0 | $2,010B |
| Insurance Brokers | 3 | −0.144 | 0/1 | $201B |
| Regional Banks | 2 | −0.232 | 0/0 | $82B |
| Consumer Finance | 2 | −0.241 | 0/0 | $356B |
| Transaction & Payment Processing | 4 | −0.260 | 0/0 | $1,137B |
| Life & Health Insurance | 3 | −0.333 | 0/1 | $151B |
| Multi-Sector Holdings (BRK-B) | 1 | −0.392 | 0/0 | $1,056B |
| Property & Casualty Insurance | 5 | **−0.512** | 0/3 | $402B |
| Multi-line Insurance (AIG) | 1 | −0.517 | 0/0 | $39B |

**Spread across sub-industries = 0.72 (from +0.210 to −0.512), roughly 8x the sector's own equal-weight average of −0.090.** By the mandate's own test, this means **the sector-label unit is the wrong one** — "Financials" is netting a genuine bull market in market-infrastructure/wealth-management franchises against a genuine bear market in underwriters. The two are driven by different mechanisms (fee/AUM/transaction-volume economics vs. loss-ratio/reserve economics) and should not be reasoned about as one book.

**Testing "Financials is working = the brokers are working":** partially true but too narrow. `COIN` (+0.750) and `HOOD` (+0.561) are indeed the top two scores and are crypto/retail-brokerage, not banks — but Investment Banking & Brokerage as a *group* (+0.210 avg, including `MS`/`GS` near flat) is not carrying the sector alone. Financial Exchanges & Data (+0.173) and Asset Management & Custody Banks (+0.090) are comparably strong blocs with different economics (subscription/index data for `MCO`/`SPGI`/`ICE`, AUM/perpetual-capital fees for `BX`/`BLK`). The accurate statement is: **"Financials is working" = retail-brokerage + market-infrastructure + AUM-fee franchises are working; balance-sheet-heavy financials (banks, insurers, card issuers) are not** — three different economic engines, one accidentally shares a GICS label with the other two.

`KRE` (regional banks, +0.17/−1.21/−5.29/**+7.47** at exc1/5/20/60) shows the identical 20d-negative/60d-positive shape as `XLF`, confirming this is not an `XLF`-composition artifact (e.g., BRK-B's 13.9% weight) — it is a genuine, sector-wide stall-after-run pattern. `wflow_ex_top1` (−0.020) vs `wflow` (−0.072) shows BRK-B's own weakness (flow −0.392) is making the cap-weighted read look worse than the ex-BRK-B sector, not better — so the drag is broad-based, not a single mega-cap artifact.

---

## 2. Players ∪ thematic map (mcap ≥ ~$2B, from FIN.json)

- **Money-center/GSIB banks**: `JPM` $871B, `BAC` $399B, `WFC` $252B, `C` $244B, `GS` $324B, `MS` $352B, `USB` $91B, `PNC` $93B, `TFC` $60B — the balance-sheet core, rate-sensitive.
- **Super-regionals**: `HBAN` $34B, `FITB` $48B — smaller, wider dispersion (HBAN +0.085 vs FITB −0.549).
- **Retail/discount brokerage + market makers**: `SCHW` $160B, `HOOD` $97B, `IBKR` $43B, `COIN` $43B — the flow leaders.
- **Pure IB/trading**: `GS`, `MS` — flat-to-slightly-negative flow despite the majors' accumulation pattern; deal/trading-revenue-driven, not deposit-franchise-driven, so they sit apart from the banks bloc mechanically even though GICS groups them with brokerage.
- **Asset managers / alternatives**: `BX` $151B, `BLK` $163B, `KKR` $87B, `APO` $79B, `AMP` $42B, `BNY` $99B, `STT` $47B — AUM/perpetual-capital-fee economics, largely accumulating (`APO`/`KKR` are the negative outliers — private-equity-fee-carry names, not credit).
- **Exchanges & data/ratings**: `ICE` $76B, `CME` $89B, `NDAQ` $47B, `MCO` $79B, `SPGI` $122B, `MSCI` $42B — transaction-volume + subscription hybrids; `MSCI` is the sub-industry's clear laggard (rs60 −8.9, the only negative rs60 in the group).
- **Insurance — P&C**: `PGR` $119B (outlier positive, +0.044), `CB` $125B, `TRV` $66B, `ALL` $57B, `HIG` $35B — all distributing except PGR.
- **Insurance — Life/Health/Multi-line**: `PRU` $37B, `MET` $55B (paper-book holding), `AFL` $59B, `AIG` $39B — worst OBV prints in the sector (`AFL` −0.393).
- **Insurance brokers**: `AJG` $55B (flow leader in the group, +0.446), `MRSH` $78B, `AON` $68B (sector's single worst flow score, −0.806).
- **Payments/consumer finance**: `V` $622B, `MA` $433B, `AXP` $231B, `COF` $125B, `XYZ` $45B, `PYPL` $38B — `V` is flow-neutral-positive, everything else negative; `XYZ`/`PYPL` the two worst OBV distributors outside insurance.
- **Conglomerate**: `BRK-B` $1,056B, top1 at 13.9% XLF weight, flow −0.392 — a standalone story (insurance float + equities + Berkshire Hathaway Energy), not representative of any sub-industry average.

---

## 3. IR anchor — primary filings (Item 1A anti-signals + MD&A mechanics)

**`PNC` (10-K filed 2026-02-20, period 2025-12-31)** — chosen because it is the Diversified-Banks outlier that breaks the "6-of-7 accumulating" pattern.
- Item 1A risk-summary bullets name the exact NIM-mechanics anti-signal this run needs: *"Changes in interest rates or interest rate spreads affect the difference between the interest that we earn on assets... and the interest that we pay on liabilities"*; *"[rate changes] can decrease the demand for interest rate-based products and services, including loans and deposit accounts"*; *"Increases in interest rates likely lower the price we would receive on fixed-rate customer obligations if we were to sell them"* — i.e., PNC's own filing flags both a demand-destruction channel and an AFS/HTM mark-to-market channel from further hikes, directly relevant given Warsh's 08-28 hawkish turn.
- MD&A (Item 7) states, verbatim mechanics: **NIM rose to 2.83% in FY2025 from 2.66% in FY2024 (and 2.76% in FY2023) — "reflected lower funding costs, the continued benefit of fixed rate asset repricing and loan growth."** Average loans grew only +1% ($3.6B) in 2025 — i.e., the NIM improvement is overwhelmingly a repricing/funding-cost mechanical effect, not a loan-demand story. This is the direct evidence for item 7 below.

**`SCHW` (10-K filed 2026-02-25, period 2025-12-31)** — chosen because it is the sub-industry's rs60 leader (+25.2) and the name whose 2023 funding-cost crisis is the sector's best-known anti-signal precedent.
- MD&A shows the crisis has structurally reversed, in the filing's own words: *"bank supplemental funding [reduced] by $44.8 billion, or 90%, to $5.1 billion at year-end 2025"*; *"Client sweep cash trends improved in 2025, with bank sweep deposits and payables to brokerage clients increasing by a total of $36.6 billion, or 12%"*. Margin loans ended 2025 at $112.3B, +34% YoY.
- Item 1A bullets are mostly generic stock-price-volatility risk factors (collateral concentration, analyst coverage) rather than a fresh funding-cost warning — consistent with the underlying repair being real, not merely a market read.

**`BX` (10-K, business section)** — used for the frame-transfer test (§8). Filing's own term, **"Perpetual Capital"**: *"assets under management with an indefinite term, that are not in liquidation and for which there is no requirement to return capital to investors through redemption requests in the ordinary course of business... Perpetual Capital strategies represent a significant and growing portion of our overall business, and the management fees and performance revenues we receive."*

**`JPM` (10-K filed 2026-02-13, period 2025-12-31)** — business overview only (Item 7/MD&A is an incorporation-by-reference stub to the annual-report exhibit, so no mechanical NIM text was extractable this run — noted as a source gap, not treated as a null finding). Risk-summary bullets confirm the standard GSIB taxonomy (market/credit/liquidity/capital/strategic/conduct/reputation/country/people risk) with nothing FIN-DEEP-specific beyond PNC's more granular language.

---

## 4. Value-chain map (FIN core: deposits → funding cost → NIM → loan growth → credit cost → capital return)

1. **Deposits/funding mix** — DFF at 3.63 (8.3rd percentile of its year, ~70bp of cuts already delivered) is lowering banks' cost of interest-bearing deposits and wholesale funding mechanically, independent of loan demand.
2. **Funding cost → NIM** — confirmed at `PNC`: NIM +17bp YoY (2.66%→2.83%) attributed by the filing itself to "lower funding costs" + "fixed rate asset repricing," not loan growth (+1% only). This is the mechanism, not a demand signal (see §7).
3. **NIM → loan growth appetite** — decoupled this cycle: `PNC` grew loans +1% despite NIM expansion; **the bottleneck is not loan demand or funding availability, it is curve shape.** 2s10s at 20.5th percentile and 10s30s at 16.5th percentile (both near one-year flats) cap how much further the deposit-cost tailwind can translate into forward NIM once fixed-rate asset repricing catches up to the current curve — i.e., the repricing tailwind is a **stock, not a flow**: it runs down as the back-book finishes rolling into current yields, and the flat curve means the *new* NIM produced by these repriced assets is not itself widening further.
4. **Credit cost** — HY OAS at 0.0th percentile of its year (1-year low) is the cleanest available read that credit-cycle stress is not yet visible in market pricing; no credit-cost anti-signal surfaced in the filings read this run (flagged as a gap, not a clean bill of health — provision commentary was not pulled for banks beyond PNC's "$779 million for 2025... driven by a net increase" without further granularity captured this run) `[unverified — provision trend not decomposed]`.
5. **Capital return** — not read from filings this run; flagged as a gap for the next FIN DEEP.
6. **Bottleneck named explicitly**: **the binding constraint on further bank NIM expansion is the flat 2s10s/10s30s curve, not deposit availability, not credit losses (currently benign per HY OAS), and not capital.** Strong short-end funding-cost relief (DFF cuts) is not a bottleneck — it is the one clean tailwind currently working; the curve shape is what stops it from compounding into forward quarters.
7. **Cross-sector chain (confirmed live, 08-28, 5 outlets)**: AI-capex → private credit → BDC/asset-manager fee pools. Blue Owl-managed funds led a $2.4B debt financing for IREN's AI-factory buildout (Nvidia chip purchases); separately, "BDCs Are Selling Investment-Grade Bonds Again After a Frozen Quarter" (Fool/Nasdaq, 08-27) — the private-credit funding market that froze earlier in the year is re-opening. `BX`'s own filing confirms its Credit & Insurance segment (BXSL, BCRED) sits structurally inside this chain via "Perpetual Capital" vehicles (§3, §8).
8. **Node feeding node 7**: insurance float. `BX`'s Perpetual Capital explicitly includes "assets managed for certain of our insurance clients" — i.e., the asset-manager fee pool at the AI-capex financing end of the chain is partly funded by insurance-company general-account allocations, which links back to the (currently distributing) insurance sub-industry in an indirect, non-price way worth flagging as a research thread, not a conclusion `[unverified]`.

---

## 5. Chain-hop candidates (body-proximate only, cross-checked against flow)

Ran `chain-hop "private credit" "compute financing" "AI factory financing" --days 10` (215 articles scanned, ±300-char proximity window). Headline-named results (`NVDA`, `GS`, `BX`, `KKR`, `BLK`, `JPM`, `MS`, `COIN`, `HOOD`, `APO`, `NDAQ`, `BRK-B` — all already discussed above, so not "candidates" by definition) excluded per the mandate.

**True candidates (title 0 hits, ≥2 body-proximate co-mentions):**
- **`BAC`** — 2 proximity hits, 11 total body mentions in the 10-day theme window. Cross-check: `BAC` flow +0.138 (top of Diversified Banks bloc), OBV +0.125 (매집), rs20 −2.4 — **passes the cross-check**: it is exactly a member of the "6-of-7 accumulating, rs stalled" bloc, and its body-proximity to the AI-financing/private-credit theme is corroborated by a separate, directly on-point headline: **"How Bank of America and three other lenders could win big from Scott Bessent's and Kevin Warsh's bond-market machinations"** (MarketWatch, 08-28) — i.e., BAC is independently named (not just chain-hop-inferred) as a beneficiary of the Treasury-market/Fed dynamics this DEEP's mandate is about. Full body text of that MarketWatch piece was not extractable via the available search tools this run (headline + 1543-char body length only) — treat the mechanism (likely primary-dealer/underwriting or duration-book related) as `[unverified]` pending a direct read.
- **`C`** — 2 proximity hits, 4 body mentions. Cross-check: `C` flow +0.082, OBV +0.377 (매집, the **strongest OBV print of the seven majors**), rs20 −2.7 — also passes the cross-check and sits in the same third-state bloc.

Both candidates independently corroborate §0's finding: the majors-bank OBV-accumulation pattern is showing up in the AI-capex-adjacent financing narrative specifically, not just as a generic rate-cut beneficiary story.

---

## 6. Valuation / estimate-revision checks (forward multiple ⇒ margin/ROTCE history ⇒ revision trend)

- **`SCHW`**: trailing P/E 20.1x, forward P/E 14.1x (17.8x fwd P/E discount to trailing implies the Street expects ~42% EPS growth to fwd EPS $7.80 from trailing $5.49). Revision trend is unambiguously supportive across every horizon pulled today: FY+1 EPS estimate rose from $7.27 (60d ago) → $7.80 (current), and 0y EPS revisions show 20 analysts revising up in the last 7 and 30 days, **zero down**. This is the cleanest "cheap-and-getting-cheaper-on-a-rising-numerator" read in the sector, consistent with the funding-cost repair documented in §3.
- **`MCO`**: trailing P/E 32.7x, forward P/E 27.2x — expensive on either basis, priced for durable double-digit EPS growth (fwd EPS $18.91 vs trailing $15.76). Revision trend is **internally contradictory across horizons, the exact "denominator direction only, not leading" caveat this mandate flags**: the current-quarter (0q) EPS estimate was cut from $4.37 (30d ago) to $4.25 (current, −2.7%) with 19 down-revisions vs 1 up in the last 30 days — but the full-year (0y) estimate simultaneously *rose* from $16.89 (30d ago) to $16.97, with 22 up-revisions vs 1 down in the same 30-day window. **A near-quarter cut and a full-year raise happening at the same time, in the same name, in the same 30-day window is a direct, dated instance of the two-non-overlapping-windows-disagree-in-sign pattern already flagged sector-wide** — do not read `MCO`'s positive full-year revision trend as confirmation of the quarter print; the quarter number itself is being cut.
- Read together, `SCHW`'s revision trend is unanimous across horizons (a real signal of denominator health) while `MCO`'s is horizon-dependent (illustrates why the revision table is diagnostic of direction only, never predictive) — the two names are a useful in-sector control pair for this caveat.

---

## 7. "Margin must mean-revert" claims — structural terms actually checked

**Claim tested: PNC's NIM expansion (2.66%→2.83%) should be read as demand recovering.** Structural check (from the filing, §3): **NO — the repricing schedule mechanically produces this.** The MD&A explicitly attributes the +17bp move to "lower funding costs" (deposit-beta relief as DFF falls, 8.3rd percentile) and "the continued benefit of fixed rate asset repricing" (back-book securities/loans originated at old, lower yields continuing to roll into current, higher yields as they mature) — while average loan balances grew only 1%. This is req. C3's exact test applied and answered: **before reading this NIM trend as a demand signal, the repricing schedule was checked and it is producing the trend mechanically, not loan demand.**

**Contract/structural terms actually named**: deposit-cost relief (DFF direction) and fixed-rate asset repricing cadence (from PNC's own MD&A) are the two named mechanical drivers. Deposit beta itself (the specific % pass-through of Fed cuts to PNC's deposit costs) was **not** disclosed in the extracted MD&A text (mdna field truncated at 50,000 chars) — flagged as `unknown`, not assumed. Hedge/swap book detail and regulatory-capital-floor detail were not pulled this run for any bank — also `unknown`, not assumed favorable or unfavorable.

**Implication for the flat-curve bottleneck (§4.3)**: because the *current* NIM tailwind is confirmed mechanical/back-book rather than organic, the flat 2s10s (20.5th percentile) matters more than it would if NIM were being driven by fresh loan spread — a mechanical repricing tailwind runs out as the back-book finishes catching up to the curve, and a flat curve means there is little room for the *next* vintage of repriced assets to widen NIM further. This is consistent with, not contradictory to, the "majors accumulating on OBV while rs20 stalls" pattern: the market may be quietly accumulating on a real but *finite* mechanical tailwind, waiting for either curve steepening or the FOMC's actual September decision (hawkish per Warsh, dated 08-28) to resolve which way NIM trends next.

---

## 8. Frame-transfer test

**Frame borrowed**: RPO/lock-in (the desk trusts this frame for SaaS/industrials revenue visibility) → **does it apply to a FIN node? Tested against `BX`'s "Perpetual Capital."**

**Result: APPLIES, with caveats — PASS, not "never asked."** `BX`'s own 10-K defines Perpetual Capital as AUM "with an indefinite term... for which there is no requirement to return capital to investors through redemption requests in the ordinary course of business," explicitly including BREIT/BEPIF (real estate), BIP/BXPE/BXINFRA/GP Stakes (private equity), and BXSL/BCRED (credit) vehicles, and the filing states this pool is "a significant and growing portion of our overall business, and the management fees and performance revenues we receive." This is functionally an RPO-analog: locked-in, redemption-gated (or redemption-limited) capital that converts to a recurring fee stream, exactly like backlog converting to recognized revenue.

**Caveat that breaks the pure-RPO analogy**: unlike SaaS RPO, Perpetual Capital is not contractually non-cancelable in the same sense — BREIT-style vehicles have historically imposed *gates* on redemption requests (the 2022-23 BREIT redemption-gating episode is the sector's own precedent for this frame's limits) rather than prohibiting redemption outright. The frame applies to the **fee-earning AUM stickiness** claim (this part is genuinely RPO-like and supports treating `BX`'s $151B mcap as more annuity-like than a typical asset manager) but does **not** extend to a "guaranteed forward revenue" claim the way true RPO does — gates are a release valve the filing itself acknowledges exists.

Exchanges/index-licensing stickiness (`MSCI`, `SPGI`) was named as the "obvious candidate" in the mandate but **not independently source-checked this run** — flagged as a gap; `MSCI`'s weak flow/rs60 (−8.9, the sub-industry's only negative rs60) makes this the more urgent name to check next, since a locked-in-revenue frame would argue its price weakness is a flow/technical air-pocket rather than a fundamental re-rating, and that thesis needs the filing check to stand.

---

## 9. Customers named, disclosed spend checked

- **`SCHW`'s customers** are RIA and retail brokerage clients; disclosed spend proxy = client margin-loan and sweep-cash balances (§3): margin loans $112.3B (+34% YoY), sweep deposits +$36.6B (+12%) in FY2025 — both are hard, filed numbers, not estimates, and both point the same direction (client risk appetite and cash re-engagement both rising into FY2025 year-end, period ended 2025-12-31).
- **`MCO`/`SPGI`'s customers** are debt issuers (corporates, sovereigns, structured-finance sponsors) whose "spend" is ratings/index fees tied to issuance volume. Indirect confirmation: HY OAS at 0.0th percentile (1-year low, 2026-08-27 FRED read) is the macro condition that historically encourages issuance; `MCO` quarterly revenue rose from $1,889M (Q4-2025) to $2,185M (Q2-2026) per the fundamentals pull today — consistent with, though not proof of, an issuance-volume tailwind. Print date for the next read: `MCO`/`SPGI` next quarterly filings will show whether this continues once the hawkish Warsh repricing (08-28) works through primary-market calendars.
- **`BX`'s customers** are institutional LPs (pensions, sovereign wealth funds, insurers) — the insurance-client linkage into Perpetual Capital AUM (§4.8, §8) is the one disclosed-spend thread tying the asset-manager bloc back to the (distressed) insurance bloc; not further quantified this run.

---

## 10. Lead/lag claims — measured this run or tagged [unverified]

- **"Banks lead the cycle"** — **not tested this run, explicitly tagged `[unverified]`.** No lead/lag regression or historical-turn comparison was run against this dataset; do not inherit as fact.
- **"2s10s leads NIM"** — **not tested this run, explicitly tagged `[unverified]`.** §4 and §7 establish a *mechanical* (repricing/funding-cost) linkage from the curve/DFF level to PNC's realized NIM, which is a same-period accounting relationship read directly from the MD&A, not a lagged-leading-indicator claim — this is a different, weaker claim than "2s10s leads NIM by N quarters," which was not measured.
- **exc20 vs exc60 divergence (`XLF` −0.97 / +12.19, `KRE` −5.29 / +7.47)** — measured this run directly from the ETF context provided; this is a same-run fact, not a lead/lag inference. No claim is made here about which window "leads" the other; both are stated as the shape to be explained (done in §0/§1), not sequenced causally.
- **FINRA short-volume check (measured this run, `us_flow.py`, 2026-08-28 data)**: `PNC` short% 45.0% vs 20d base 42.5%, z +0.23, 5v5 trend −7.4 (falling) — normal range, no distribution signal. `XLF` short% 64.1% vs base 58.8%, z +0.38, 5v5 trend **+16.8 (rising)** — still "정상범위"/normal range per the tool's own threshold, but the rising trend on the ETF itself is worth a re-check next run given the exc20 stall. `KRE` short% 79.6% vs base 73.4%, z +0.87, 5v5 trend −2.4 — ETF short% run structurally higher than single names due to AP/market-maker hedging mechanics (noted by the tool itself), not read as a bearish signal.

---

## 11. KPI + anti-signal tracker (dated observables)

| Observable | Value | Date | Read |
|---|---|---|---|
| `XLF` exc60 / exc20 vs SPY | +12.19pp / −0.97pp | 2026-08-28 | Stalled-after-run shape, sector-wide (KRE confirms) |
| `XLF` exc1 (08-28 session) | +0.59pp vs SPY | 2026-08-28 | Up on a hawkish day; eqflow −0.090 same day argues this is narrow/top-heavy, not broad confirmation |
| Diversified Banks OBV pattern | 6/7 매집 (accumulating), PNC neutral | 2026-08-28 | Third state — money in, rs20 not yet confirming |
| PNC FY2025 NIM | 2.83% vs 2.66% (FY24) / 2.76% (FY23) | filed 2026-02-20 | Mechanical (funding cost + repricing), loans +1% only |
| SCHW bank supplemental funding | $5.1B, −90% YoY | filed 2026-02-25 | 2023 funding-cost crisis structurally repaired |
| SCHW sweep deposits | +$36.6B / +12% FY2025 | filed 2026-02-25 | Client cash re-engaging bank balance sheet |
| SCHW FY+1 EPS revision | $7.27→$7.80 (60d), 20 up/0 down (30d) | pulled 2026-08-30 | Unanimous positive across horizons |
| MCO 0q vs 0y EPS revision sign | 0q: 19 down/1 up (cut); 0y: 22 up/1 down (raise) | pulled 2026-08-30 | Contradictory across windows — denominator-direction-only caveat, live example |
| Insurance sub-industry OBV | 5/9 names 🔴, all rs20 negative | 2026-08-28 | Confirmed distribution, not a flow-tool artifact |
| BAC/C chain-hop co-mention | 2 proximity hits each, AI-financing/private-credit theme | scanned 2026-08-30 (10d window) | Corroborates majors-accumulation-in-AI-capex-adjacent-lending thread; BAC also independently headline-named (MarketWatch 08-28) |
| BDC funding market | "BDCs selling IG bonds again after frozen quarter" | Fool/Nasdaq 2026-08-27 | Private-credit funding thaw, upstream of BX/APO/KKR fee pools |
| FINRA short-vol z-score | PNC +0.23 (↓trend) / XLF +0.38 (↑trend) / KRE +0.87 (↓trend) | 2026-08-28 | All in normal range; XLF's rising 5v5 trend is the one to re-check |
| Implied vs realized vol | XLF 09-04 ±1.36%, 09-11 ±2.17%, vs realized 5-session 1.41% | pulled 2026-08-30 | 09-04 (NFP day) implied move roughly in line with recent realized — not obviously pricing event risk richly |
| S134 (XLF 5-session excess, A≥+2.00/B≤−2.00, window 08-28→09-04) | Not yet resolvable — 2 of 5 sessions elapsed; exc5 +0.58 is a loose same-metric proxy, **not a score** | running | Do not re-freeze |
| S135 (max pairwise spread XLU/XLRE/XLP, window 09-04→09-11) | Not started — registered today | pending | Do not re-freeze |
| Deposit beta (bank-specific pass-through %) | Not disclosed in extracted MD&A text this run | — | `unknown`, flagged not assumed |
| Provision-for-credit-loss trend detail | Not decomposed beyond PNC's aggregate FY2025 $779M | — | `[unverified]`, gap for next FIN DEEP |
| MSCI/SPGI index-licensing lock-in (RPO-frame) | Not source-checked this run | — | Gap; MSCI's weak rs60 (−8.9, group's only negative) makes this the priority next name |

---

**Sources used this run**: `module_business_us` (JPM, PNC, SCHW, BX, all `--json`), `module_fundamentals_us` (SCHW, MCO, `--json`), `scripts/us_flow.py` (PNC, XLF, KRE), `module_news_data chain-hop`, `module_news_data fts search` / `search --field any`, FIN.json (47-name scored dataset, asof 2026-08-28), provided FRED macro context (2026-08-27) and ETF/implied-vol context (pulled today). No `module_chart` or `sector_flow.py` calls made (excluded per mandate — 0/3 render rate on US tickers).
