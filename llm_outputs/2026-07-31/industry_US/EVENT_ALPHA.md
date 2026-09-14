# EVENT_ALPHA — industry_US — 2026-07-31 (Fri)

> Stage 4/10. The **bottom-up** complement to MACRO's top-down matrix: which stories ARE building this
> week × is money already following → FORWARD cards, a ROTATION cross-check. **Scope `--scope foreign` on
> every news call** (hard rule — a card citing cross-market feed is VOID). Flow tags asof **07-30 prev
> close** (`SECTOR_FLOW_US.json`, SWEEP asof note); news bodies dated inline; theme-age 90d/foreign asof
> 07-31. Analytical only — no sizing, no buy/sell (P4; BET owns sizing).

## Selection log (no silent truncation)

`thread --days 7 --scope foreign` → **3,844 events / 3,020 threads; 434 multi-day, 2,586 one-day.**
⚠ The window-end **07-31 = 0건** inflated every tag to ENDED — read the per-day denominator, not the tag:
the peak days ran **07-27 796 · 07-28 844 · 07-29 839 · 07-30 782**, and the top threads were **at or near
peak on 07-30** (the last real day). The **alive candidate set** = the 10 peak threads + 2 sub-headline
novelty threads MACRO surfaced = **12 alive threads.**

**SELECTED: 8 threads → 5 cards.**
| Thread | Curve (07-25→07-30) | Peak | → Card |
|---|---|---|---|
| Iran strikes U.S. bases | 2→14→16→15→20→25 | 25 | Card 1 (war-premium leg) |
| Oil slump / US-Iran pause | 5→14→22→19→18→18 | 22 | Card 1 (refining leg) |
| Russia sanctions bill (86-12 Senate) | novelty 🟡ACCEL 4.08× | — | Card 1 (supply leg) |
| Fed holds rates steady | 5→11→9→24→23 | 24 | Card 2 |
| MSFT earnings beat | 3→8→11→3→19→19 | 19 | Card 3 |
| Amazon stock pops | 6→4→14→9→6→18 | 18 | Card 3 |
| CXMT memory chip soar | 20→10 | 20 | Card 4 |
| 8-K Apple Inc. / Q3 earnings | 4→3→9→15→8→16 | 16 | Card 5 |

**NOT SELECTED: 4 alive threads** (counted, not silently dropped) →
- **AI workers call for a slowdown** (peak22, faded 22→9 on 07-30) — sentiment/labor, no clean tradeable money hop → **missed_ledger `Q.확신부족`**, enters-if a named AI-capex layoff hits a tradeable name.
- **Meta/BlackRock $14bn TX data-centre** — already owned by MACRO **P14/S40** (capex-as-lease); not re-carded → **missed_ledger `M.숏리스트탈락`**, enters-if the structure closes as a disclosed operating lease (S40, 09-30).
- **Russia charges Telegram founder Durov** (peak21→15) — legal/geopolitical, no US-equity exposure → not carded.
- **France/Spain wildfires** (peak19→4) — not US-investable, faded → not carded.

---

## CARD 1 — Energy / oil-refining: war premium deflating while the DISTILLATE crunch tightens

- **Thread:** Iran-strikes (BUILDING 2→14→16→15→20→25 · peak25) + Oil-slump/US-Iran-pause (peak22) ·
  denom 07-30 = 782 events / 3,020 threads. Novelty: **`diesel crunch` 🟡ACCELERATING, 25.71× accel, 9
  total, 7d-avg 0.9 (asof 07-31)** — the **precursor-form ≤2-outlet climbing shape**; `refining margins`
  🟡ACCEL 4.29×/104; `Russia sanctions` 🟡ACCEL 4.08×.
- **Direction (BODY-READ):** the tradeable leg is refined-product tightness, not the oscillating crude
  premium. *"Diesel Crunch Is Now the Biggest Threat in Oil Markets"* (Goldman, oilprice 07-30);
  *"Record U.S. Refinery Runs Fail to Ease Global Fuel Crunch"* (07-30); ★ *"Russia Extends Diesel and
  Gasoline Export Bans **Into 2027**"* (07-30) — **the bottleneck was EXTENDED, not released on the
  07-31 ban-expiry**; *"Chevron earnings beat forecast as **refining margins soar**, rival Exxon misses
  estimates"* (07-31). The crude war-premium leg oscillates and is deflating: *"Oil prices ease as
  recovering Hormuz Strait traffic tempers war premium"* (cnbc 07-31) vs *"Oil Prices Inch Higher as Iran
  Strikes U.S. Bases"* (07-31). ⇒ **S49 branch A (refining margin) is the durable leg; S31/S8 war premium
  is the fading one.**
- **Exposure** (one hop past the XOM/CVX headline layer):
  - `VLO` · pure-play refiner, bottleneck beneficiary · **🟡중립(07-30)** flow +0.48 / OBV +0.17 매집 / RS20 +16.7 · ⚠ 🟡 is a **news-velocity demotion artifact** (rank 176, velocity n/a) — OBV says 매집
  - `MPC` · refiner · **🟡중립(07-30)** flow +0.50 / OBV +0.33 매집 / RS20 +18.3 · book holds; cycle-epicenter UNDER min (SWEEP gap −1.135pp)
  - `PSX` · refiner · **🟡중립(07-30)** flow +0.48 / OBV +0.36 매집 / RS20 +20.2 · ⚠ **R8 retracted (cheapest-refiner) — do NOT re-argue on valuation**; `core_pick` human-locked
  - `XOM` · integrated · **🟢가속(07-30)** but RS60 −3.3 — **headline/crowded layer**; the war-premium leg, **MISSED Q2 on refinery maintenance** (07-31), softening
  - `CVX` · integrated · **🟢가속(07-30)** flow +0.62 — headline layer; **beat on refining margins soaring**
- **Crowding:** XOM/CVX = the crowded layer (every outlet + their Q2 prints). The alpha layer = **VLO/MPC/PSX, accumulating but 🟡 tag-suppressed** (the exact 2026-07-21 ENRG precedent SWEEP flagged).
- **Future — IF** diesel-crunch theme keeps accelerating (25.71×) **AND** refiner OBV stays 매집 → refiners re-rate on margin and **MPC/PSX 🟡→🟢 lift once the oil news bucket is served**; **track KPI:** distillate crack 5-session change stays >0 (currently +5.355) + refiner tags green; **horizon: MPC 08-04 · PSX 08-05 prints.**
- **ELSE (kill):** crude below **$80 AND** a settled distillate crack below its 20-session mean **together** → S49 branch B won (war premium was the whole story) → drop the refiner-margin thesis. ⚠ absolute crack lines unscoreable on this data (R30/D95) — direction only.
- **Cell + hand-off:** **CONFIRMED-EARLY** (BUILDING × integrated 🟢 + refiner OBV-매집) → **ROTATION cross-evidence (Energy OW−) + BET §B candidates = the refiner layer VLO/MPC/PSX**, integrateds noted as crowded. ⚠ **Caveat:** the clean refiner tags are 🟡 by news-demotion, not confirmed 🟢 (OBV is grade-C, D6) — **dated re-check: do the refiner tags lift to 🟢 when the news-velocity axis serves them (re-run SWEEP with oil bucket active).**

---

## CARD 2 — Fed credibility shock → bear steepener → Financials (NIM mechanism)

- **Thread:** Fed-holds-rates (BUILDING 5→11→9→24→23 · peak24) · denom 07-29 = 839 / 07-30 = 782.
  Novelty: **`credibility shock` 🟢FRESH, age 1, 7 total (asof 07-31)** — golden-zone fresh.
- **Direction (BODY-READ):** the hold was received **hawkish-but-not-credible** → *"Treasury yields
  continue to rise as Wall Street calls out Fed's 'inflation credibility shock'"* (07-30); *"United
  States Dollar Index turns upside down on Fed rate hike doubts"* (07-30); three dissents FOR a hike
  (*"Something We Haven't Seen in 10 Years"*, 07-31). ⇒ **bear steepener** (MACRO: derived 2s10s
  +0.35→+0.45) = **NIM-positive for asset-sensitive lenders; the flattener that kills NIM (S23) is 25bp
  away and receding.** ⚠ **Read the mechanism, not the tape:** the equity index SOLD OFF on FOMC day
  (*"Wall Street's Worst Day Since April 2025"*) — the thread is bank-NIM bullish, duration/long-bond
  bearish; the two are not the same trade.
- **Exposure:**
  - `BAC` · most asset-sensitive money-center to a steepener · **🟢가속(07-30)** flow +0.57 / OBV +0.18 매집 / RS60 +14.1 · less crowded than JPM
  - `JPM` · money-center · **🟢가속(07-30)** flow +0.53 / OBV +0.30 매집 / velo 2.54 · shortlist ✅clean-rise (moderately crowded — headline layer)
  - `TRV · CB` · insurance node, float reinvested at higher long yields · **[not in shortlist]** — MACRO/HANDOVER flag insurance as the **surviving FIN-OW reason** (eq-mean +0.603 = 1.48× sector) after R32 killed the breadth reason; TRV EXTENDED-BUT-LIVE, recheck 08-06
  - ⚠ contra layer: `C` **🔴분산(07-30)** flow −0.68, `GS` **🟡(07-30)** — the steepener helps lenders, **not** capital-markets names; not all banks are the trade
- **Future — IF** the steepener persists (derived 2s10s > +0.20) **AND** BAC/JPM OBV stays 매집 → **FIN OW− confirmed on the NIM mechanism, not the retracted breadth reason (R32)**; **track KPI:** derived 2s10s + BAC/JPM RS20 vs SPY; **horizon: NFP 08-07, then S26/S41 → 08-12.**
- **ELSE (kill):** derived **2s10s ≤ +0.20 on a settled close by 08-05** (S23 fires — its own registered falsifier) **OR** HY OAS > 2.90% (credit breaks, banks de-rate regardless of NIM) → drop.
- **Cell + hand-off:** **CONFIRMED-EARLY** (BUILDING × 🟢 on BAC/JPM) → **ROTATION (Financials OW−) + BET §B candidates BAC/JPM.** Insurance node inherited from HANDOVER (recheck 08-06), not fresh.

---

## CARD 3 — Hyperscaler AI-capex VALIDATED (MSFT + AMZN) — and the "consumer" label is a misread

- **Thread:** MSFT-beats (BUILDING 3→8→11→3→19→19 · peak19) + Amazon-pops (REIGNITED final day 6→4→14→9→6→18 · peak18) · denom 07-29 = 839 / 07-30 = 782.
- **Direction (BODY-READ):** AI **demand** validated and capex **NOT cut** → *"Microsoft Surges 9% as
  Azure Tops $100B"*, *"**Unchanged 2026 Capex Outlook**, Strong Azure Sales"* (07-29); *"biggest one-day
  gain since 2008, adding $480B"* (07-30); AMZN *"AWS Beat: CEO Says **Even Higher CapEx Won't Be Enough**
  To Meet Soaring Cloud Demand"* (07-31), *"Amazon Sits Atop the AI Hyperscaler Pedestal."* ★ **W4/W5
  cross-read:** MACRO §E logged XLY (Cons Disc) as the day's leader **on AMZN** — but AMZN's driver is
  **AWS/cloud-capex, not the consumer**; the "Cons Disc leadership" is a **GICS-label artifact**. The real
  signal transmits down the capex chain (compute → networking → power). Governing asymmetry (HANDOVER §4):
  a capex **CUT** rewrites the thesis, a **hold/raise** only moves timing — MSFT held, AMZN raised ⇒
  timing-favorable, thesis intact.
- **Exposure** (one hop past the MSFT/AMZN/NVDA crowded layer):
  - `ANET` · datacenter networking/switching, bottleneck-adjacent · **🟡중립(07-30)** flow +0.48 / OBV +0.13 매집 / RS20 +11.9 · prints **08-04** — the un-crowded pick-and-shovel
  - `CEG` · AI-power (nuclear datacenter PPA) · **🟡중립(07-30)** flow +0.49 / OBV +0.20 매집 (rank 123, news-demoted) · SWEEP: **CEG bifurcates UP vs GEV/VRT 🔴** — the accumulating power leg
  - `AVGO` · custom AI silicon / networking · **🟡중립(07-30)** flow +0.44 / OBV +0.07 / RS60 −12.2 — weak 60d base, momentum-only
  - `NVDA` · compute · **🟢가속(07-30)** new-🟢 flow +0.43 — **headline/crowded**, held epicenter
  - `MSFT` · spender · **🟢가속(07-30)** flow +0.80 / OBV +0.26 — **most-printed, crowded**
- **Crowding:** MSFT/AMZN/NVDA = crowded. Alpha layer = **ANET/CEG (accumulating, 🟡, less printed).**
- **Future — IF** hyperscaler capex guides keep rising **AND** ANET/CEG OBV stays 매집 → the downstream pick-and-shovel layer re-rates as capex flows through; **track KPI:** ANET 08-04 print + CEG 08-06 print + memory-supplier median RS20 (S30, 08-05); **horizon: 08-06.**
- **ELSE (kill):** a hyperscaler **capex CUT** on any next print (the un-narrated branch, HANDOVER C6/S1) **OR** AI-credit fear reignites (NVDA CDS, IG OAS ≥ 0.90% = S41) → the whole capex chain de-rates.
- **Cell + hand-off:** **NODE = CONFIRMED-EARLY** (demand validated, MSFT/NVDA 🟢) → **ROTATION cross-evidence (IT/Comm-Svc capex leg).** ⚠ **The clean fresh exposure (ANET/CEG) is 🟡, not 🟢 → STORY-ONLY on the alpha layer, dated re-check 08-06; do NOT leak ANET/CEG as fresh BET candidates until they green.** MSFT/NVDA are already-crowded/held, not fresh.

---

## CARD 4 — Memory supply: CXMT panic vs Apple's shortage reality → the LEVEL is TIGHT

- **Thread:** CXMT-memory-soar (peak20, 20→10 two-day) + Apple memory-shortage buyer-signal (cross-thread) · denom 07-27 = 796 / 07-28 = 844. Novelty: **`memory shortage` 🟡ACCELERATING, 2.07× accel, 295 total (asof 07-31)** — reignited, building.
- **Direction (BODY-READ — headline REVERSED by body):** the CXMT headline reads panic/threat, the body
  says the threat is **limited** → *"Wall Street Sees Little Threat to Micron From China's Memory Giant"*
  (07-27); *"China's CXMT IPO Jolts U.S. AI Memory Stocks: **Is the Panic Justified?**"* (07-29);
  tomshardware *"Chinese CXMT DRAM ... **prices still track the big three**"* — CXMT is a Shanghai
  IPO/valuation event (+466–500%), **not a supply glut.** ★ **Buyer-side cross-confirm:** Apple (07-31)
  *"CEO Tim Cook flags '**increasing impact**' from **memory shortage**"* — a downstream memory BUYER
  reporting shortage = the LEVEL is TIGHT (M7 confirmed); **the 07-27 supplier rout (MU −5%, SNDK −12%,
  WDC −8%) was a sentiment shock, not a demand/supply change.** Rate-of-change decel (M1) is real; the
  level is tighter than the panic priced.
- **Exposure:**
  - `STX` · storage/HDD (near-line, differentiated from DRAM) · **🟢가속(07-30)** new-🟢 flow +0.71 / OBV +0.27 매집 — the **one ignited** memory name (beat+guided). ⚠ HANDOVER: **pre-committed to read STX as no-info inside the ±14.6% band (R23 quarterly-mix)**; shortlist ⚡squeeze-fuel, NOT clean
  - `MU` · DRAM, the CXMT-panic epicenter, buyer-confirmed tight · **🔴분산(07-30)** flow −0.25 / RS20 −12.8 but RS60 +29.6 — **money still distributing on the panic; has NOT turned**
  - `WDC` · storage/flash · **🟡중립(07-30)** flow +0.19 / OBV +0.11 매집 / RS60 +13.6 — accumulating quietly, less crowded than MU
  - crowded/contra layer: `MU · SNDK` (headline panic names, still 🔴)
- **Future — IF** buyer-side shortage signals spread (memory-shortage theme keeps accelerating) **AND** S30 median RS20 of {STX,MU,WDC} vs SPY crosses **above 0** → the panic reverses, suppliers re-rate on confirmed tightness; **track KPI:** S30 median (08-05) + a 2nd downstream buyer flagging shortage; **horizon: 08-05.**
- **ELSE (kill):** CXMT ships at-scale DRAM **below** big-three pricing (tomshardware's watch) **OR** MU's next guide cuts on demand → oversupply branch (S34 supply-threat) won → drop the tight thesis.
- **Cell + hand-off:** **money is SPLIT** — STX 🟢 (with the no-info-band caveat), MU 🔴 (not turned), WDC 🟡 → **STORY-ONLY on the DRAM core (MU): watchlist + dated re-check 08-05; do NOT leak MU into candidate handoff.** STX is 🟢 but ring-fenced by R23 (no-info band) → not a fresh BET candidate either. Narrative BUILDING, money not yet confirming = the textbook STORY-ONLY cell.

---

## CARD 5 — Apple: "beat" headline, weak-guide reality (the LOSS the headline didn't say)

- **Thread:** 8-K Apple Inc. / Q3 earnings (BUILDING 4→3→9→15→8→16 · peak16, climbing on the last real day) · denom 07-30 = 782.
- **Direction (BODY-READ — classic headline reversal):** *"Apple beats estimates as iPhone revenue jumps
  22%"* (07-30) **but** *"Apple shares drop despite a stellar earnings beat"* / *"weak revenue forecast as
  CEO Tim Cook flags 'increasing impact' from memory shortage"* (07-31); *"Beats Earnings but **Services,
  China Disappoint**."* ⇒ the beat is backward-looking; the FORWARD signal is a **weak guide + memory-cost
  squeeze + soft China/Services** → **bearish AAPL near-term (S46).** This is the *"biggest measured thread
  was a LOSS the headline never said"* pattern — the beat is NOT the signal.
- **Exposure:**
  - `AAPL` · headline/crowded · **🟡중립(07-30)** flow +0.42 / OBV +0.16 / RS20 −1.6 — **flipped 🟢→🟡** (HANDOVER S46: RS20 +19.2→−2.0 live); **money faded BEFORE the print**
  - (cross) memory suppliers BENEFIT from AAPL's shortage flag → see Card 4 (MU/STX confirm tight)
  - `QCOM` · Apple modem loss + memory-cost inflation · **🔴분산** [HANDOVER: RS20 −15.2, ledger `K.본문반증`, recheck 08-13]
- **Future — IF** the guide-down is confirmed by price (AAPL RS20 vs SPY stays negative) **AND** flow 🟡→🔴 → S46 branch A (value-exhaustion + memory-cost squeeze validated); **track KPI:** AAPL−QCOM RS20 spread (currently +13.2pp, <+15 branch-A leg met) + AAPL RS20 vs SPY; **horizon: S46 → 08-13.**
- **ELSE (kill):** AAPL RS20 vs SPY **re-crosses above 0 on a settled close** (the guide was conservative, buyers return) → re-file, S46 branch B.
- **Cell + hand-off:** quiet/fading × **🟡** (not 🔴; OBV still +0.16 mild-매집) ⇒ **NOT DEAD** — this is a fade-WATCH, not a drop. **STORY-ONLY / re-file with dated re-check 08-13. AAPL must NOT leak into the candidate hand-off** (it is a kill-watch, not a buy).

---

## Book cross-check — ENDED threads an open position rides on

- **No genuinely ENDED thread (FADING/ENDED × 🔴 dispersing) carries a book position this run.** The truly
  faded threads (AI-workers-slowdown, Durov/Telegram, wildfires) have **zero book exposure** — nothing to flag.
- ⚠ **Direction-mismatch flag (not an ENDED flag) → book desk:** **AAPL was revived on the ledger 07-30 on
  an arithmetically ZERO base** (HANDOVER §2). Its revival thesis now rides on a thread that **body-reads
  bearish** (weak guide + memory-cost squeeze, Card 5). The thread is not ENDED (peak16, climbing), but the
  **forward direction is against the revival** — the position must re-justify on something alive, or accept
  the S46 fade read. Handed to paper_desk / 미러링.
- ✅ **MPC/PSX (book, Energy refining)** ride Card 1 which is **BUILDING** — position supported; the book is
  UNDER-exposed to this exact epicenter (SWEEP cycle-gap −1.135pp), consistent with the card's CONFIRMED-EARLY read.
- ✅ **TSM/LNG/NVDA/AVGO (book, AI-capex epicenter)** ride Card 3 which is **BUILDING** — supported.

## Handoff to ROTATION / BET

- **CONFIRMED-EARLY → ROTATION + BET §B:**
  - **Card 1 Energy/refining** — refiner alpha layer **VLO/MPC/PSX** (integrateds XOM/CVX crowded). ⚠ refiner tags 🟡-artifact → BET must note the news-velocity confirmation is pending.
  - **Card 2 Financials steepener** — **BAC/JPM** (NIM mechanism, not the retracted breadth reason).
  - **Card 3 hyperscaler capex NODE** (demand validated) → ROTATION cross-evidence only; **NVDA/MSFT already held/crowded.**
- **STORY-ONLY — DO NOT leak into candidate hand-off:** Card 3 alpha **ANET/CEG** (🟡 until greened, re-check 08-06) · Card 4 **MU** (🔴, not turned, re-check 08-05) · Card 5 **AAPL** (fade-watch, re-check 08-13).
- **Body-read discipline applied:** **2 threads had their headline direction REVERSED by the body-read** —
  CXMT ("panic"→limited-threat/sentiment) and Apple ("beat"→weak-guide loss). Neither became a bullish card
  on its headline. **No thread was fully killed** (both survived with corrected direction).

## Ledger writeback (intended — reconciled at run-end handoff)

- **missed_ledger add:** `AI-workers-slowdown` (`Q.확신부족`, enters-if a named AI-capex layoff hits a
  tradeable name); `Meta/BlackRock $14bn TX DC` (`M.숏리스트탈락`, enters-if it closes as a disclosed
  operating lease — S40, 09-30).
- **reject_ledger add:** none — no thread was dropped as DEAD (no BUILDING/FADING thread sat in the
  ENDED × 🔴 cell with a card this run).

## ✅ EXIT CHECK

- [x] Scope market-correct — **`--scope foreign` on every news call**; no cross-market feed cited.
- [x] Selection logged — **12 alive threads → 8 selected (5 cards) → 4 not selected, counted** (AI-workers, Meta/BlackRock, Durov, wildfires).
- [x] Every card has a **direction body-read** with a quoted evidence line — 2 headline reversals caught (CXMT, Apple).
- [x] Every exposure name carries a **flow tag with asof (07-30 prev close)**; STORY-ONLY names (ANET/CEG/MU/AAPL) explicitly walled out of the candidate hand-off.
- [x] Every card has **both branches + a kill condition + a dated horizon** (P4).
- [x] `EVENT_ALPHA.md` written; **CONFIRMED-EARLY (Cards 1/2, node 3) handed to ROTATION/BET**; ENDED-thread book flags emitted (none strict; AAPL direction-mismatch flagged); ledger writeback intents noted.
- ⚠ Flow tags are asof **07-30 prev close** — a same-day 07-31 catalyst is not in them (SWEEP caveat); refiner/CEG 🟡 tags are **news-velocity demotion artifacts** (rank>48), OBV-매집 read as build-lean not confirmed 🟢 (D6, grade-C).
