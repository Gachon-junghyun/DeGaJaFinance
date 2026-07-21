# COMPANY ANALYSIS — CEG (Constellation Energy) · 광기(HYPER) US book

- Date: 2026-07-14 (KST) · as-of tape 2026-07-13 ~11:00 ET (US market OPEN mid-session → **today's bar is INTRADAY/UNSETTLED; volume not read**)
- Horizon: technical/entry = short (1–4wk) · thesis = mid (1–3Q)
- THESIS_SEED: *"Largest US nuclear IPP (55 GW post-Calpine). PTC $43.75/MWh floors the nuclear half; signed 20-yr IG PPAs (MSFT-TMI ~835MW, Meta-Clinton, Walmart). Multiple compressed 50x→21x fwd even as offtake landed → multiple still substantially a Fed/real-rate (duration) variable, not yet insulated on cash flow. CPI-CONTINGENT reclaim bet: fires ONLY on confirmed reclaim >~256.69, self-gated on June CPI (2026-07-14 08:30 ET)."*

> Sources: `[SEC]` CEG 10-K FY2025 (filed 2026-02-24, via SECTOR_DEEP_UTIL SEC-anchored section) · `[fund]` module_fundamentals_us (yfinance↔XBRL 4/4 quarters ≤5% match) · `[yf]` yfinance cashflow/balance/financials · `[FINRA]` us_flow Reg-SHO · `[flow]` flow_read/chart-struct read · `[news]` news_alert. Estimates tagged `[est]`.

---

## Phase 1 — Business model ("what it sells, where the money comes from")

CEG is the **largest US nuclear operator** and, after closing Calpine (Jan 7 2026), the largest US independent power producer (IPP) by capacity. Post-Calpine fleet ≈ **55 GW** = ~**32 GW legacy base** (nuclear ~22 GW + wind/solar/hydro/small gas) **+ ~23 GW Calpine** (72 gas + geothermal + storage assets; nation's largest gas & geothermal generator, TX/CA/NE). `[SEC]` Five segments (Mid-Atlantic, Midwest, New York, ERCOT, Other Power Regions). Revenue engine = **merchant generation sold wholesale + retail C&I/gov load**; the new leg is **20-yr behind-the-meter / co-located PPAs to hyperscalers**.

**Signed offtake — status audited (R-003: "signed/definitive" vs "MOU/plan"):** `[SEC]`
| Deal | MW | Signed | Status |
|---|---|---|---|
| **Microsoft** — TMI Unit 1 restart ("Crane Clean Energy Center") | ~835 MW | Sep 2024, 20-yr PPA | **SIGNED/definitive.** Delivery pending restart (~2027–28). MW not yet flowing. |
| **Meta** — Clinton Clean Energy Center full output | full plant | Jun 2025, 20-yr PPA | **SIGNED/definitive.** Clinton already operating → output largely deliverable/preserved. |
| **Walmart** — 20-yr | n/d | per MACRO overlay | **SIGNED** (definitive language). |
| **Calpine acquisition** | +~23 GW | **CLOSED Jan 7 2026** | Definitive, closed. Adds *dispatchable firm* (gas/geo) to nuclear base. |

All three PPAs are **definitive (서명), not MOU/plan** — this is the strong, verifiable core of the seed. Caveat: the scarce asset is *delivered* MW; TMI is a *restart* (future flow), so CEG's cleanest offtake quality is one notch behind VST's 2,176 MW *already-operating* Meta block. `[SEC]` News velocity confirms the theme is live not fading: "Constellation" 136 foreign hits, but coverage is two-sided — *"Goldman flags valuation"*, *"AI Boom Could Be a Bad Reason to Buy Utility Stocks"*. `[news]`

---

## Phase 2 — Earnings quality / cash flow (★accounting-illusion filter)

**Headline pattern (FY2025) is healthy:** Op-CF **+$4.24B**, Capex **−$2.95B**, FCF **+$1.29B**, Investing-CF **−$3.20B** → the textbook (+ operating / − investing) signature. Net income $2.32B < OCF $4.24B → **OCF > NI, positive accrual quality** in 2025. `[yf]`

**★ THE ONE DECISIVE QoE FINDING — OCF is derivative-collateral distorted, not clean:** operating cash flow swung **−$2.35B (2022) → −$5.30B (2023) → −$2.46B (2024) → +$4.24B (2025)**. `[yf]` A nuclear/retail fleet does not really burn $5B of operating cash — those negatives are **margin/collateral posting on commodity hedges** during the 2022–24 price-volatility regime, which reversed as collateral unwound in 2025. **Implication: no single year's OCF/FCF can be trusted as run-rate; the +$1.29B FCF is partly a collateral-unwind tailwind, not pure core generation.** Normalized EBITDA is the steadier read (~$6.3B FY25 vs $6.95B FY24 — actually *down* YoY). This is the correct place for a trader to be skeptical.

**Leverage post-Calpine — the real bear on the balance sheet:** standalone Total Debt ~$9.0B (2025 BS) but info-level total debt ~**$22.5B** once Calpine's assumed debt + leases consolidate. `[yf]` Net-debt/EBITDA steps up materially into 2026; interest burden rises just as the multiple sits on a duration knife-edge. Stockholders' equity $14.5B, Total assets $57.3B. Receivables $4.27B and inventory $1.74B rose broadly in line with the 63.9% Q1'26 revenue jump (Calpine consolidation) → no standalone working-capital red flag, but Calpine roll-in makes YoY line-items non-comparable for ~4 quarters.

Verdict on quality: **real cash generator, but "quality" is lumpy** — collateral swings + fresh Calpine leverage mean the margin of safety is thinner than the clean FY25 FCF suggests.

---

## Phase 3 — Valuation + catalyst ("what to pay") · "cheap is guilty"

**Current multiples `[fund]`:** Trailing P/E **22.2x**, **Forward P/E 18.8x** (fwd EPS $13.58), PEG **3.74**, P/S 3.05, P/B 2.76, div yield 0.68%. Analyst mean PT **$357.81** (+40% from $255.62; range $296–441; 20 Buy/6 SB/3 Hold/0 Sell).

- **Multiple-compression claim = REAL, and understated.** The seed says 50x→21x; the live fwd is **~18.8x** — the de-rate is even deeper than framed. From the 2024 ~50x peak (price ~$350+ on lower EPS) to ~19x fwd *while* Meta + Walmart + Calpine landed → confirms the seed's core: **the multiple has been priced as a duration/real-rate variable, not yet insulated by contracted cash flow.** `[SEC][MACRO]`
- **"Cheap is guilty" verdict: 18.8x fwd is NOT statistically cheap — it is a de-rated GROWTH multiple, not a value multiple.** Traditional merchant/IPP power historically trades ~8–12x P/E and low-double-digit EV/EBITDA. CEG at 18.8x fwd with **PEG 3.74** is a *premium* to merchant-power history; it looks "cheap" only versus its own 50x peak. Worse, the $13.58 fwd EPS **already borrows Calpine accretion** — the forward estimate is doing the de-risking. So the multiple is "reasonable **if** the growth (PPA EPS + Calpine synergies) delivers," not a margin-of-safety discount. Peers VST/TLN sit in the same duration-sensitive re-rate cohort; CEG carries the *visible* compression scar (Goldman valuation flag) but also the *deepest* de-rate, so it is the highest-torque duration proxy of the three.
- **Floored vs merchant split (key nuance):** the IRA §45U nuclear PTC (~$43.75/MWh effective floor, inflation-adjusted, **nuclear-only**) floors only the **~22 GW nuclear** portion — roughly **~40% of the 55 GW fleet.** The **~23 GW Calpine gas sleeve is UN-floored merchant** (no PTC), fully exposed to spark spreads / gas curves. So "PTC floors the generation half" is *half*-true: it floors the nuclear half; the Calpine half is naked merchant. `[est on GW split; SEC on PTC applicability]`

**★ Dated catalyst (self-gating):** **June CPI print — 2026-07-14 08:30 ET.** The reclaim thesis fires only if rates cooperate; hot CPI → real-10y up → the duration-priced multiple compresses further and the reclaim fails. Next earnings ~**2026-08-06**. Both are hard, dated de-risk/invalidation events.

---

## Phase 4 — Technical setup (reconciled against chart-struct turn-판정)

**Chart-structure anchor (verbatim):** OBV **누적 / +79% 20d slope** (real accumulation) · **bullish RSI divergence** (price lower-low, RSI higher-low → base forming) · **BUT bearish MA stack 5<20<60<120**, price under all 4 MAs · Bollinger expanding 19% · RSI ~35.7 · **턴-판정 = NEUTRAL/CHOP (direction unconfirmed)** · trigger close>**257.13** + OBV→accumulate · stop (swing low) **236.50**.

**Reconciliation (fundamentals AGAINST the turn, not restated):** the accumulation + bullish divergence say smart money is *building a base under a de-rated, funded-offtake asset* — consistent with Phase-1/3 (signed IG PPAs + deepest multiple de-rate = value being quietly accumulated). **But the turn is NOT confirmed**: bearish MA stack + **RS60 −20.8% (severe lag)** = the stock is still *losing* to the market over 60d, exactly the "duration scar" the fundamentals flagged. So structure and fundamentals *agree it is early*: a base, not a breakout. `[flow]`

**Flow confirms, does not contradict `[FINRA][flow]`:** FINRA short-vol **z −1.92, trend −10.4 (strong)** = shorts **covering** into the offtake narrative (cleanest flow/fundamental alignment in the util complex, tied with VST). OBV accumulation, news velocity 1.01x, options P/C 1.19 (mild hedging), short 3.8% float building. Positive tape today (+1.7% while SMH −2.6% / VIX +9% on oil shock) = relative-strength tell *within* today's unsettled bar. **Entry gate satisfied on flow; NOT yet on trend (turn unconfirmed) → entry must gate on the reclaim trigger.**

---

## VERDICT (setup)

**BUY-ON-TRIGGER** (not STRONG — see asymmetry).

- **Direction:** long, **only on confirmed reclaim close > 256.69–257.13** (per desk rule: unconfirmed NEUTRAL/CHOP turn → no anticipatory entry).
- **Entry:** 257.13 (reclaim) · **Stop (invalidation):** **236.50** (swing low; risk −$20.63 / −8.0%) · **T1:** ~296 (analyst low) · **T2:** ~357.81 (analyst mean, +40%).
- **★ Fundamental asymmetry number:**
  - **Stop-gated (traded): ~1.9:1 to T1 (296), ~4.9:1 to mean PT (357.81).** The stop converts a mediocre setup into an acceptable trade.
  - **Unprotected/pure-fundamental: ~0.9:1** (bull re-rate to ~$320 = +$64 vs fundamental bear ~$185 [fwd EPS haircut ~$12.5 × ~15x merchant multiple] = −$71). **Thin — below the 1.5 desk floor without the stop.** Honest read: **the stop is doing the work, not a fat margin of safety.**
- **Thesis 5-slot:** ①de-rated funded nuclear IPP re-rates as duration fear eases; ②signed IG 20-yr PPAs `[SEC]` + PTC nuclear floor + FY25 FCF+; ③check = close>257.13 AND real-10y not rising; ④counter = 18.8x is a growth multiple not a discount, Calpine half un-floored + newly levered, OCF collateral-distorted → re-rate needs *rates* not just deals; ⑤if ④, stock stays a duration proxy and drifts to ~$185–210 (−20 to −30%).
- **★ SINGLE DECISION VARIABLE:** **the June CPI print (2026-07-14 08:30 ET).** Hot → reclaim fails, card never buys, no position. In-line/soft → reclaim can fire, then it's a real stop-gated ~1.9–4.9:1 long. Everything downstream self-gates on this one number.
