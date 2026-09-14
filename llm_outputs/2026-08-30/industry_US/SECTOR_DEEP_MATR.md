# SECTOR DEEP — MATERIALS (MATR) — FULL FRESH MAP
asof 2026-08-28 (repaired basis) · run date 2026-08-30 · analyst: DEEP/MATR · P4 — analytical only, zero buy/sell, zero sizing

⚠ **Repaired basis note (stated once):** the 2026-08-28 Close in the daily feed was void and was replaced with a 5-minute-bar proxy validated at 0.0225% mean / 0.038% max error vs the KIS broker feed (n=9). All flow_score/OBV/RS figures below inherit this repair. Not re-litigated further in this file.

---

## 0. Mandate — one line

**Not a contradiction — decomposition shows it's the same trade twice.** MATR's +0.164 eqflow is not a diversified rotation; FCX (copper) and NEM (gold) alone supply 1.411 of the 1.967 sum of all 12 flow_scores (71.7%), and pulling them out drops eqflow from +0.164 to +0.056 — so the "OW, zero reds" board signal is functionally a leveraged **copper+gold** call wearing a sector label, and copper is exactly the node MACRO flags at 100th-percentile crowded-long. Gold's own COT (66th pctile) is not crowded — so the resolution is precise, not blanket: **the crowding risk lives in FCX/copper specifically, not in "Materials," and not in NEM/gold.**

---

## 1. Flow read

Sector row: wflow +0.225, eqflow +0.164 (rank 1/11 sectors), breadth 0.00, green 0, red 0 of 12, top1 LIN 24.7% of weighted flow, wflow_ex_top1 +0.233 (**higher** than wflow — LIN is a drag on the weighted number, not the driver; top1_flips_sign FALSE confirms LIN removal doesn't invert the read).

But **breadth 0.00 with green 0 / red 0 is not "broad and calm" — it means every one of the 12 names sits in the same 🟡중립 tag bucket despite a flow_score range of 0.767 (FCX) to −0.398 (SHW), a 1.165-point spread against a sector average of +0.164.** The dispersion is ~7x the sector-level signal. **The sector label is the wrong unit here** — "Materials +0.164" describes an average that no actual sub-industry sits near:

| Sub-industry | Names | Flow_score range | Read |
|---|---|---|---|
| Copper/Gold miners | FCX +0.767, NEM +0.644 | +0.644 to +0.767 | Strongly accumulating, best RS in sector |
| Ag-chem | CTVA +0.394 | — | Accumulating, moderate |
| Specialty chem | ECL +0.340, SHW −0.398 | **0.738-pt spread inside one sub-industry** | Split — not a coherent group call |
| Industrial gases | APD +0.268, LIN +0.199 | — | Mildly accumulating, weak RS (both negative RS60) |
| Aggregates | VMC +0.193, CRH +0.101, MLM −0.047 | — | Mildly positive to flat, all RS60 negative (−5.7 to −11.5) |
| Steel | STLD −0.187, NUE −0.307 | — | Distributing away, RS60 −16.7 / −4.8 |

Ex-metals (10 names, dropping FCX+NEM): mean flow_score ≈ +0.056 — near-flat. **The entire "OW" case is two names.** Everything downstream of this file should read "MATR OW" as "copper+gold OW, rest of the sector neutral-to-soft," not as a Materials-wide call.

XLB (sector ETF) vs SPY confirms the medium-term tailwind but also shows the tape cooling into the print: exc1 +0.11pp, exc5 **−1.17pp**, exc20 +2.44pp, exc60 +0.98pp. The 5-day number going negative while 20-day stays positive is consistent with a short-term pause after a run, not a reversal yet — flagged as a KPI in §12.

---

## 2. Players (mcap ≥ ~$2B, real tickers, grouped by sub-industry)

**Industrial gases:** LIN (Linde, $236.8B) · APD (Air Products, $62.4B)
**Copper & gold miners:** FCX (Freeport-McMoRan, $98.7–109.8B depending on source/date) · NEM (Newmont, $110.8–134.9B)
**Aggregates / construction materials:** VMC (Vulcan Materials, $39.3B) · CRH (CRH plc, $74.3B) · MLM (Martin Marietta, $36.6B)
**Steel:** STLD (Steel Dynamics, $36.0B) · NUE (Nucor, $55.5B) — **NUE is a paper-book holding only, not in the real KIS account.**
**Specialty & ag chemicals:** ECL (Ecolab, $75.7B) · SHW (Sherwin-Williams, $79.1B) · CTVA (Corteva, $52.6B)

All 12 are the given universe (n=12 in the sector row). No thematic add beyond this set met the mcap/ticker bar this run — chain-hop (§5) returned zero body-proximate candidates outside it.

---

## 3. IR anchor — primary filings, ≥2 names read from source

**LIN — read from its FY2025 10-K (filed 2026-02-25, accession 0001628280-26-011430), Item 1 Business, via `module_business_us`:** "Linde is the largest industrial gas company worldwide." FY2025 sales $33,986mm (2024: $33,005mm, 2023: $32,854mm — low-single-digit top-line growth, not a cyclical business). Two channels: **on-site** (largest-volume products — oxygen/nitrogen/hydrogen — piped directly to a customer's plant under "total requirement contracts... typically ranging from 10-20 years and containing minimum purchase requirements and price escalation provisions") and **merchant** (tanker-truck delivery of liquid O2/N2/Ar/H2/He/CO2, Linde-owned storage leased to the customer, distribution-radius-constrained). Served industries named explicitly: healthcare, chemicals and energy, manufacturing, metals and mining, food and beverage, **electronics**.

**FCX — read from EDGAR filing index via `module_disclosure_us` (24 filings, last 90 days, CIK 0000831259):** 16 of 24 filings are Form 4 insider transactions (last dated 2026-08-28, i.e. the same day as this file's repaired asof) — a high cadence of insider Form 4s but no accompanying 8-K/13D cluster or Item 3.02/2.03 (no capital-raise or debt disclosure this window). One 10-Q filed 2026-08-06 (period 2026-06-30). One Item 2.02 earnings 8-K dated 2026-07-23. No 8-K/M&A activity in the window.

**FCX — also read from its FY2025 10-K (filed 2026-02-13, accession 0000831259-26-000012), Items 1&2 Business and Properties, via `module_business_us` (a delayed background fetch that landed after the first draft of this file — folded in here rather than left unverified):** mines copper, gold, molybdenum, silver across Grasberg (Indonesia), Morenci/Bagdad/Safford/Sierrita/Miami (AZ), Chino/Tyrone (NM), Henderson/Climax (CO), Cerro Verde (Peru), El Abra (Chile). Pricing mechanism, quoted directly — U.S. cathode/rod: "sold... under U.S. dollar-denominated annual contracts... generally based on the COMEX monthly average settlement prices for the month of shipment and include a premium." South America concentrate/cathode: "annual and multi-year contracts" but "final copper pricing in a specified future month (generally one to four months from the shipment date) primarily based on quoted LME monthly average settlement copper prices," net of smelter treatment charges "generally negotiated annually." FY2025 LME averaged $4.51/lb (range $3.87–$5.68, closed $5.67 on 12/31/25); COMEX averaged $4.82/lb (range $3.99–$5.80, closed $5.63). This directly updates §7/§8 below from `unknown` to checked-and-confirmed.

**STLD business summary (via `module_fundamentals_us`):** four segments — Steel Operations, Metals Recycling Operations, Steel Fabrication Operations, Aluminum Operations. End markets named: construction, automotive, manufacturing, transportation, heavy/ag equipment, energy, pipe & tube.

**NEM business summary:** gold producer, also explores copper/silver/lead/zinc.

FCX's copper pricing mechanism **was** verified from the 10-K text above (index-linked to COMEX/LME monthly average settlement, no fixed price, no floor/ceiling). NEM's gold offtake structure was **not** verified in a primary filing this run — flagged as `unknown` rather than asserted, per §6/§7.

---

## 4. Value-chain map (5–8 nodes, left → right) and bottleneck

```
Ore/mineral body (Grasberg, Morenci, Cerro Verde...)
        │
Mine + concentrator (FCX, NEM)
        │
Smelter/refiner (mostly 3rd-party — not vertically integrated in this universe)
        │
   ┌────┴─────────────────────────────┐
Copper cathode/rod              Gold doré/bullion
   │                                   │
Wire & cable, transformer            Bullion banks, jewelry,
windings, EV/grid buildout           central-bank/ETF demand
   │
[AI → power buildout → transformers → COPPER]  ← cross-sector chain node
   │
End-use: grid/transformer OEMs, EV OEMs, construction wiring
```
Parallel chain (industrial gases): **Air separation (LIN/APD on-site plants) → piped O2/N2/H2 → semiconductor fabs, refineries, steel mills, healthcare** — LIN's own 10-K names electronics as a served industry, tying it to the same AI-capex chain from a different angle (fab gas supply, not grid copper).
Parallel chain (aggregates): **Quarry (VMC/MLM/CRH) → crushed stone/cement → ready-mix/asphalt → highway, data-center-shell, and reshoring construction spend.**

**Bottleneck = smelting/refining capacity, not ore supply and not demand.** Strong copper demand (AI/grid) is not itself a bottleneck by the desk's definition — it's the binding constraint upstream of the demand pull. The "US Tariff Fears Drive Copper Stockpile Rush" headline (Nasdaq, 2026-08-26) is a symptom of this: importers pulling refined copper into the US ahead of a potential Section 232 tariff, i.e., **physical logistics/refining-capacity squeeze**, not a demand-side story. None of FCX/NEM in this universe control smelting capacity as their primary economics — they are miners, so the bottleneck sits **outside** the two names carrying the sector's flow signal. This matters for the mandate: the crowded COT long is a bet on a bottleneck (refined-metal availability) that FCX equity does not directly control the resolution of.

---

## 5. Chain-hop candidates

`chain-hop "copper transformer grid AI datacenter power"` (--days 7): **0 headline-named, 0 candidates** ("근접 텀 근접 문단 공동언급 ≥2건" returned nothing in the 7-day US-top300 universe). No body-proximate, non-headline copper/grid/AI-adjacent name cleared the bar this run. This is a negative result, stated as such — no candidate is promoted to BET on this pass. Re-run at a longer window if the desk wants a second look; do not substitute a headline-named ticker (e.g., something already in wire/cable coverage) for a chain-hop candidate — that would violate the "never headline-named" rule.

---

## 6. 🚨 Price-cycle rule — second-derivative read (QoQ revenue as rate-of-change proxy; no chart tool available this run)

Quarterly revenue was pulled via `module_fundamentals_us --json` for the three commodity-sensitive names. QoQ growth, then the **change in that QoQ growth rate** (the second derivative):

**FCX** (revenue, $mm): Q2'25 7,582 → Q3'25 6,972 → Q4'25 5,633 → Q1'26 6,234 → Q2'26 7,029
QoQ%: −8.05 → −19.18 → +10.67 → +12.75
Δ(QoQ%) [rate-of-change]: −11.13pp → **+29.85pp → +2.08pp**
→ **Two consecutive quarters of accelerating growth** (Q1'26 and Q2'26 both show the rate itself increasing). This is a real, verified acceleration, not just "growth" — it lines up with FCX's top flow_score and positive EPS revisions (below).

**NEM**: Q2'25 5,317 → Q3'25 5,524 → Q4'25 6,818 → Q1'26 7,307 → Q2'26 6,118
QoQ%: +3.89 → +23.42 → +7.17 → −16.27
Δ(QoQ%): +19.53pp → **−16.25pp → −23.44pp**
→ **Two consecutive quarters of decelerating growth**, the second one flipping to outright contraction (−16.27% QoQ). This is exactly the rule's trigger pattern — and it is happening in the name carrying the best RS in the entire sector (RS20 +33.5%, RS60 +17.0% vs SPY). Price and the second derivative of revenue are pointing opposite ways in NEM specifically.

**STLD**: Q2'25 4,565 → Q3'25 4,828 → Q4'25 4,414 → Q1'26 5,205 → Q2'26 6,092
QoQ%: +5.76 → −8.58 → +17.92 → +17.04
Δ(QoQ%): −14.34pp → **+26.50pp → −0.88pp**
→ Growth reaccelerated hard in Q1'26 and held (only a marginal −0.88pp deceleration, still +17% QoQ) — revenue momentum is *not* the deteriorating variable for STLD; the equity flow is negative despite this. Points to margin/spread or forward-guidance concerns, not top-line, driving STLD's flow_score −0.187 / RS60 −16.7% — a genuine fundamental-vs-price divergence, opposite in direction to NEM's.

Gold and copper **spot price** QoQ series were not independently pulled this run (no FRED/COT price-level series was fetched beyond the percentile figures given) — revenue is used as the rate-of-change proxy and is a mix of price and volume; this is flagged, not presented as a pure price series. One anchor point is now sourced (§3/§7): FCX's FY2025 10-K puts LME copper's full-year-2025 average at $4.51/lb (range $3.87–$5.68, closing the year at $5.67) and COMEX's average at $4.82/lb (range $3.99–$5.80, closing at $5.63) — i.e., 2025 closed near the top of its own annual range, consistent with (not proof of) the acceleration read above continuing into the Aug-2026 "record price" headline in §4/§12, but this is a single annual data point, not a QoQ series, and is not stretched further than that.

---

## 7. 🚨 Contract-terms rule

**LIN — checked in the 10-K text.** On-site contracts are "total requirement contracts... 10-20 years... containing **minimum purchase requirements** [a take-or-pay-style floor] **and price escalation provisions**" [an upward-only mechanism]. No ceiling/cap language appears in the Item 1 business description at the level of detail disclosed — a per-contract cap cannot be ruled out from this text, so **ceiling = unknown**, floor = confirmed. Because the disclosed mechanism only describes a floor and an escalator, a QoQ deceleration in LIN's own numbers is **not** explained by a contractual ceiling on this evidence — if LIN decelerates, the more likely reading is contract-mix/volume, not a price cap kicking in. (LIN's own RS is weak — RS20 −0.7%, RS60 −5.6% — despite this floor structure; that softness is not explained by the take-or-pay language either way and is left as an open item, not force-fit to a bullish "floor protects it" narrative.)

**FCX — checked in the 10-K text (§3).** U.S. cathode/rod sold under annual contracts priced "generally based on the COMEX monthly average settlement prices for the month of shipment and include a premium"; South America concentrate/cathode under annual/multi-year contracts with "final copper pricing in a specified future month (generally one to four months from the shipment date)" off LME monthly averages, net of smelter treatment charges renegotiated annually. **No floor, no ceiling, on either leg** — "contract" here means volume/logistics commitment and premium/treatment-charge terms, not a price band; the metal price itself passes through almost fully (with only a 1-4 month lag on the South America leg). This is a clean, sourced "no" on the contract-ceiling question: **a QoQ deceleration in FCX would reflect the actual COMEX/LME price and/or shipped-volume trend, not a contractual cap** — which strengthens, not weakens, the §6 read that FCX's two-quarter revenue acceleration is a real market-price/volume signal. It also means no "must mean-revert" claim can be grounded in contract terms either way — FCX's margin is exposed to the full amplitude of the LME/COMEX cycle, unsmoothed.

**NEM — not checked this run.** I did not pull the 10-K/10-Q revenue-recognition note that would show whether gold sales carry any offtake/streaming structure versus pure spot. Per rule C3: **contracted share = unknown.** No "must mean-revert" claim is made for NEM's margin. This directly bears on §6: NEM's two-quarter revenue deceleration is read as a genuine (price-and/or-volume) signal precisely *because* there is no known contractual mechanism that would produce a mechanical ceiling — but that absence-of-evidence is not the same as a confirmed absence-of-ceiling; it is an unverified gap, narrower now than before (FCX resolved, NEM still open).

**STLD** — steel pricing is generally understood to be spot/index-linked rather than long-dated fixed contracts, but this was not verified in STLD's own 10-K this run either. Marked unknown; the accelerating revenue in §6 is not attributed to any contract mechanism.

---

## 8. Frame-transfer question

**Frame this desk trusts elsewhere: take-or-pay floors (used routinely on midstream energy names).** Does it apply to a MATR node? **Checked, and yes — it applies directly to LIN's on-site industrial-gas segment**, per the 10-K language quoted in §7 (minimum purchase requirements = a take-or-pay floor by another name, plus a price escalator that behaves like a regulated-return cost pass-through). It does **not** apply to FCX — now **confirmed, not just assumed**: the 10-K text (§3/§7) shows COMEX/LME index-linked pass-through pricing with no floor or ceiling, the structural opposite of a take-or-pay band. It remains unverified (not "does not apply," just not checked) for NEM, STLD, and the aggregates names (VMC/CRH/MLM). So the take-or-pay frame is a genuine partial fit inside MATR — it explains why LIN's flow/RS is muted rather than swinging (a floor-and-escalator business doesn't re-rate on a commodity headline the way FCX does), and the FCX side of that contrast is now sourced rather than inferred: FCX's full amplitude to the LME/COMEX cycle is exactly why it, not LIN, carries the sector's flow signal.

---

## 9. Customers named, disclosed spend checked

This is a structural gap for most of MATR, stated plainly rather than papered over: **copper, gold, and steel in this universe are sold into fungible, exchange-referenced markets (LME/COMEX-linked copper, spot gold, index-linked HRC steel) through smelters/refiners/distributors, not to named counterparties with individually disclosed capex budgets** — unlike, e.g., a semis-capex chain where TSMC/hyperscaler capex is the direct demand read. That fungibility is itself a fact about the sector, not an oversight.

The one name where "customers" are named at the industry level with a traceable capex proxy is **LIN**: healthcare, chemicals & energy, manufacturing, metals & mining, food & beverage, **electronics** (10-K, §3 above). The electronics/semiconductor line is the closest tie to the AI-capex chain this file's mandate is framed around (industrial gas demand for fab construction/operation) — but I did not pull hyperscaler or fab-specific capex print dates this run to check that link quantitatively. **Flagged [unverified]** — the next DEEP MATR pass should pull semiconductor capex guidance (e.g., next major fab operator print dates) against LIN's electronics-segment commentary rather than assume the AI-gas linkage from the served-industries list alone.

Ag-chem (CTVA) sells through distributors to farmers; the macro-proxy would be USDA net farm income / planted-acreage data, not fetched this run. Aggregates (VMC/MLM/CRH) customers are state DOTs and private construction — next-check would be state infrastructure-spend releases, not fetched this run.

---

## 10. "Cheap on forward multiple" — margin history + revision trend required

**FCX**: trailing PE 37.5 → forward PE 18.5 (a ~50% multiple compression on the forward number). EPS trend supports it: FY estimate (0y) has risen from 2.79 (60 days ago) to 3.01 (7 days ago/current-ish); FY+1 risen from 3.95 to 4.13 over the same window. **Revisions and price/flow agree in direction.** Margin history (gross/EBITDA trend over multiple years) was not pulled this run — the P/S of 4.24 is noted as a level, not benchmarked against FCX's own 3-5yr P/S range, so the "cheap" framing rests on the forward-PE-vs-trailing-PE gap and the revision direction only, not a full margin-history check. **Partial pass.**

**NEM**: trailing PE 16.1 → forward PE 12.7 — looks cheap on the same logic, but the EPS trend is moving the **opposite** way from FCX: FY estimate (0y) has been cut from 10.22 (60 days ago) to 9.15 (current); FY+1 cut from 11.35 to 10.08 over the same window; the 0q (current-quarter) estimate was cut hardest, from 2.64 (60d ago) to 1.92 (current), a ~27% cut. **Revisions and price/flow disagree** — NEM's stock is up (best RS in sector) while consensus is cutting the numbers underneath it. The "forward multiple looks cheap" read for NEM is therefore misleading on its own: the forward EPS denominator has itself been falling, so part of the apparent cheapness is the estimate catching down, not the price failing to catch up. **Fails the combined test — flagged, not treated as a value signal.**

**STLD**: trailing PE 21.3 → forward PE 12.4. EPS trend is being revised **up** (0y from 15.02 90 days ago to 16.85 current; FY+1 from 17.01 to 18.95) — revisions agree with "cheap," but price/flow (RS60 −16.7%) disagrees with revisions. This is the mirror image of NEM: fundamentals improving, price not confirming. Margin-history not pulled this run. **Partial, flagged as a genuine open divergence, not resolved by this file.**

---

## 11. Lead/lag claims — measured this run or `[unverified]`

**[measured this run]** FCX's Q2'26 earnings 8-K was filed 2026-07-23 (per §3 disclosure pull). The RS20 window behind FCX's +19.1% (vs SPY) runs roughly 2026-08-01 to 2026-08-28, i.e., entirely **after** the print. FCX's OBV-accumulation and RS strength are therefore a **post-print continuation**, not an earnings-day pop showing up in a 20-day lookback — the flow kept building for a month after the numbers were already public. This is a real, dated observation from this run's own sourcing, not inherited.

**[unverified]** Any causal read of "US tariff fears → copper stockpile rush → record price → squeeze easing" (the two Aug 26 headlines) as a lead/lag chain was not measured against FCX's own price/flow series this run — the headlines and the flow_score are contemporaneous in the data window, not sequenced.

**[unverified]** No claim is made about whether NEM's RS strength led or lagged the run-up in real yields (DFII10, 89th pctile) — the FRED macro figures given are as-of 2026-08-27, one day before the repaired MATR asof; a same-window co-occurrence is not a lead/lag measurement.

**[unverified]** The 2026-08-28 hawkish Jackson Hole event (Warsh) falls on the same day as this file's repaired price basis. Any read of NEM/gold reacting to that speech is **not** captured in the rs20/rs60 figures given (those windows close as of 08-28 but are built from data mostly *predating* the speech) — this is stated explicitly as a forward-looking gap, not backfilled.

---

## 12. Track KPIs + anti-signals (dated observables — what would kill each read)

- **Copper/FCX**: next COT report — anti-signal if spec net stays pinned at/near the 100th percentile *despite* the "squeeze easing" headline (2026-08-26); that would mean positioning risk is not actually unwinding. Kill-the-acceleration-thesis signal: a third consecutive FCX quarterly print (next due ~late Oct 2026) showing Δ(QoQ%) turn negative again would break the two-quarter acceleration pattern found in §6.
- **Gold/NEM**: 09-10 PPI and 09-11 CPI (Aug prints) — a hot core print pushing DFII10 further above its current 89th percentile is the textbook gold headwind; watch whether NEM's flow_score/RS20 rolls over in the days after 08-28 in response to the hawkish Jackson Hole repricing (this file's RS window pre-dates that speech, per §11). Kill signal for the demand-side read: a **third** consecutive QoQ revenue deceleration at NEM's next print would confirm §6's two-quarter pattern as trend rather than noise.
- **Steel/STLD**: anti-signal for the "market is right to sell it" read — if STLD's next print continues the +17%-handle QoQ revenue growth (§6) and flow_score stays negative anyway, that is a standing, unresolved divergence worth escalating, not explaining away.
- **Sector-wide**: 08-31 MSCI review — mechanical index-flow risk concentrated in LIN (24.7% of wflow weight); a rebalance-driven move in LIN should not be read as a fundamental or flow-driven signal if it hits within days of 08-31.
- **XLB/SPY**: exc5 is already negative (−1.17pp) while exc20 is positive (+2.44pp) — if exc5 stays negative through the next several sessions and exc20 starts compressing toward it, that is the tell that the 20-day tailwind cited in §1 is rolling over, not just pausing.
- **Credit backdrop**: HY OAS at a 1-year low (0.0 pctile) and NFCI at the loosest level of the year (0.0 pctile) are a genuinely supportive backdrop for capex-linked cyclicals (steel, aggregates) — if either widens materially, the STLD/NUE/VMC/MLM negative-to-flat flow reading would have a credit-market confirmation it currently lacks; watch for OAS widening as an anti-signal that would make the steel/aggregates softness look more justified rather than like a standalone-equity-flow quirk.
- **Dollar**: DTWEXBGS (broad dollar) is 9 days stale as of the macro cut given (last print 2026-08-21) — no dollar level/direction claim is made anywhere in this file. First fresh DTWEXBGS print after 08-28 should be checked against the post-Jackson-Hole "dollar jumped" AP characterization before any gold/copper dollar-linkage claim is made in the next MATR pass.

---

**Verdict summary (6 lines):**
1. The MATR "OW, zero reds" signal is real in the data but is not a sector-wide call — FCX + NEM alone supply **71.7% of the NET sum** of all 12 flow scores (1.411 of 1.967) behind eqflow +0.164 — ⚠ **denominator corrected by the orchestrator: against the POSITIVE-only sum (2.906) the share is 48.6%.** Both are stated because the two denominators answer different questions, and the derived figure that carries the verdict (ex-metals eqflow) is unaffected; ex-metals eqflow is ~+0.056, essentially flat.
2. The apparent flow-vs-positioning contradiction resolves cleanly: the equity flow strength and the crowded COT copper long are the **same** trade (copper), not opposing signals — gold (NEM, COT 66th pctile) is not crowded and should not inherit copper's crowding risk.
3. Sharpest finding: **NEM — the sector's best RS/flow performer — just printed two consecutive quarters of decelerating QoQ revenue growth, the second an outright −16.27% contraction, while consensus EPS estimates were cut ~10-27% across the curve over the same 60-90 day window.** Price is not confirming the fundamental second derivative.
4. STLD shows the mirror-image divergence — accelerating revenue, rising EPS estimates, but negative flow and RS60 −16.7% — an unresolved, dated open item for the next pass.
5. LIN's on-site contracts (10-20yr, minimum-purchase floor + price escalator) are a genuine take-or-pay analog inside MATR, but they explain LIN's muted flow/RS, not the sector's OW driver — and FCX's 10-K (a delayed fetch, folded in post-draft) confirms the structural opposite: COMEX/LME index-linked pass-through, no floor or ceiling, which is exactly why FCX carries the sector's flow signal instead of LIN.
6. Chain-hop returned zero AI/grid/copper candidates this run (0 body-proximate hits in 7 days) — no promotion to BET from that lane this pass.
