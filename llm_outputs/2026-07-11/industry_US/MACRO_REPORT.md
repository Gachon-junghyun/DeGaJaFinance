# MACRO_REPORT — US DESK — 2026-07-11

> Phase 0 of the US industry pipeline. Primary numbers `[FRED]`, positioning `[COT]`,
> narrative from `news_alert.db` (foreign slice) + 2026-07-09 US daily anchor.
> Analytical only — zero buy/sell calls. Sizing language downstream = *influence*, not advice.

---

## 0. Primary snapshot (the hard readings first)

| Metric | Latest | Date | Read |
|---|---|---|---|
| Fed Funds (eff) | **3.62%** | 07-08 | `[FRED]` cuts already delivered; now flat-to-lower |
| 10y UST | **4.56%** | 07-08 | `[FRED]` +0.38 over 120d — long end selling off |
| 2y UST | **4.21%** | 07-08 | `[FRED]` +0.73 over 120d |
| 2s10s | **+0.35** | 07-08 | steepening (bear-steepener) |
| Real 10y (TIPS) | **2.31%** | 07-08 | `[FRED]` +0.37 over 120d — **restrictive real rates rising** |
| CPI YoY | **+4.17%** | May | `[FRED]` **headline HOT** |
| Core CPI YoY | **+2.82%** | May | `[FRED]` core moderating → wide headline-core wedge (~1.35pp) |
| Unemployment | **4.2%** | Jun | `[FRED]` ticked up from 4.1%; NFP 57K miss (07-04 `[news]`) |
| Broad Dollar | **120.69** | 07-02 | `[FRED]` strong / near cycle high |
| VIX | **15.84** | 07-09 | `[FRED]` calm — down from 22.2 a month ago |
| M2 YoY | **+5.58%** | May | `[FRED]` liquidity still expanding |

**One-line regime:** *Hawkish-of-neutral hold with rising real yields and a hot headline-CPI wedge driven by a rate-insensitive supply source (memory/tariff/energy); labor cracking without dovish relief = stagflation-lite; risk assets calm on the surface (VIX 15.8) but the AI mega-cap complex is de-rating as a rotation, not a rupture.*

### Positioning `[COT]` (Tue-close / 3–4d lag — contrarian ammo, not a trigger)
| Instrument | 1yr %ile | Read |
|---|---|---|
| Nasdaq-100 | **1%ile** | 🔴 crowded-SHORT → **rebound ammo** (caps the AI-selloff downside) |
| S&P 500 | 78%ile | 🟡 mild net-short |
| WTI crude | **17%ile** | 🔴 crowded-short → rebound ammo (Iran re-escalation asymmetry) |
| Nat gas | **12%ile** | 🔴 crowded-short → rebound ammo |
| Copper | **95%ile** | 🟢 crowded-LONG → **overheated, downside risk** (MATR caution) |
| Gold | 27%ile | 🟡 net-long but room to run despite the rally |
| USD Index | 59%ile | 🟡 neutral (narrow ICE gauge; broad DTWEXBGS is the strong one) |

---

## 1. Blind-spot pass (term-set refresh) — 2026-07-11

Ran `news_blindspot.py` over the §2.1 term set: window 19,225 foreign rows / 14d, **coverage 24.0%**, blind pool 14,616, sample 500 read row-by-row (spike rule).

**Verdict: 4th consecutive clean read — no absent macro event, no private company at a surprise rank** (SpaceX #2/309 is persistent and already bucketed; the rest of the emergent list = mega-caps + securities-lawsuit boilerplate noise). Two *extensions* of existing buckets promoted (not a term-set overhaul):

1. **DeepSeek own-chip → chip selloff** (body-confirmed 07-08: "Nvidia Stock Slides. DeepSeek Develops Its Own AI Chip"; same day "China greenlights Nvidia H200"). Moat-erosion-at-the-margin — folds into the existing IT / AI-trade-fragility read, not new.
2. **Fusion entering the AI-power layer** — "Google Invests in Proxima Fusion as Startup Plans Fusion Plant." A long-dated new node below the nuclear/gas/solar-storage power stack; added as a **Power/Grid watch term**.

Also body-corroborated (already-bucketed): **Iran ceasefire "over" (07-08) → oil jumped, index futures tumbled** — confirms the 07-09 anchor's Hormuz-as-rate-weapon; **Meta faces potential $1.4T EU penalties** (COMM regulatory tail); **Euro-area inflation 2.80% June** (ECB easing vs US hawkish divergence).

*Term-set action:* add watch terms `DeepSeek chip`, `fusion / Proxima Fusion` to §2.1 (Power/Grid + AI-trade fragility). No structural gap found.

---

## 2. Propositions (falsifiable directional claims)

**M-01 — Rates/Policy.** *The Fed holds hawkish-of-neutral; the next-move risk through Q3 is a HIKE, not a cut.*
- current anchor: FF 3.62%, real-10y 2.31% rising, 2s10s +0.35 `[FRED]`; Warsh's first FOMC minutes tilted the dot toward a hike + named AI capex as an inflation input (07-09 `[daily-US]`); markets earlier priced ~66% Sept HIKE (07-04 `[news]`)
- base 55 / bull(cut) 15 / bear(hike) 30
- anti-signal: real-10y rolls back below ~2.0% **and** a second sub-70K NFP with cooling headline CPI → cut door reopens
- track KPI: real-10y, 2s10s, headline CPI YoY `[R6-K??? — HY/IG OAS still n/a]`
- catalyst: next FOMC + CPI print
- → transmission: **OW FIN** (higher-for-longer NIM + steep curve); **UW RE** (rate-sensitive REITs); **OW gold/MATR** (Fed-credibility discount)

**M-02 — Inflation.** *Headline CPI stays hot (>~4%) on a rate-insensitive supply wedge (memory/tariff/energy) while core moderates — the Fed can't cut into it.*
- current anchor: CPI +4.17% vs core +2.82% YoY (May, `[FRED]`); memory DRAM contract +55–60%, Apple/Microsoft device price hikes (`[news]`)
- base 60 / bull(cools) 20 / bear(hotter) 20
- anti-signal: headline-core wedge compresses back under ~0.5pp (energy + memory both roll over)
- track KPI: headline-core CPI wedge, DRAM contract price
- → transmission: **OW IT(memory)** (pricing power), **UW DISC/STPL** (input-cost + demand squeeze)

**M-03 — Growth/Labor.** *Labor is cracking (NFP 57K, U-rate 4.2%) but buys no dovish relief — stagflation-lite, not a soft landing.*
- current anchor: U 4.2% (Jun, `[FRED]`, +0.1); NFP 57K vs 110K exp, Apr/May revised down (07-04 `[news]`); ADP +98K two-sided (07-07 `[news]`)
- base 55 / bull(reaccelerates) 20 / bear(recession break) 25
- anti-signal: jobless claims spike + ISM services < 48 → demand break, not stagflation
- track KPI: NFP trend, jobless claims, ISM
- → transmission: **UW DISC** (affordability/cost-of-living), **OW STPL/HLTH** (defensive bid if break deepens)

**M-04 — Dollar/FX + Gold.** *Broad dollar stays strong on higher-for-longer; gold co-rises on a Fed-credibility/independence discount (the unusual both-up regime).*
- current anchor: broad DXY 120.69 (07-02, `[FRED]`, near high); gold ~$4,111–4,174 (07-04 `[news]`); COT gold net-long only 27%ile
- base 60 / bull(dollar breaks) 20 / bear(dollar spikes) 20
- anti-signal: broad DTWEXBGS < ~118 with gold rolling → normal risk-on, thesis void
- track KPI: DTWEXBGS, gold, real-10y
- → transmission: **OW MATR(gold/silver miners)**; **headwind EM/DISC exporters**

**M-05 — Commodities/Oil (kill-switch lane).** *The oil war-premium oscillates on Iran/Hormuz; the ceasefire is "over" (07-08) and re-escalation tails are fat both ways.*
- current anchor: Trump says US-Iran ceasefire over → oil jumped, index futures tumbled (07-08 `[news]`, body-confirmed); Red Sea/Yemen shipping attacks recur; WTI COT 17%ile / gas 12%ile (crowded-short = rebound ammo)
- base(oscillate) 55 / bull(spike on closure) 25 / bear(drain to peace) 20
- anti-signal: Hormuz traffic normalizes + WTI COT rebuilds longs → premium drains monotonically
- track KPI: WTI, Brent, Hormuz/Red-Sea transit headlines
- → transmission: **tactical OW ENRG** (E&P cash flow + crowded-short asymmetry); **UW INDU(airlines)** (fuel)

**M-06 — Credit/Liquidity.** *Surface calm (VIX 15.8, tight spreads) masks idiosyncratic cracks — vendor-financing circularity + record IG supply funding AI capex.*
- current anchor: VIX 15.84 `[FRED]`; First Brands leveraged-loan distribution failure, Nvidia turning lender/landlord (neocloud revenue-share), record June IG issuance (AI-capex-financed-by-debt) (`[news]`); HY/IG OAS still un-instrumented `[R6-K??? — n/a]`
- base(contained) 55 / bull(heals) 20 / bear(contagion) 25
- anti-signal: a second First-Brands-type name + IG new-issue concessions widening → contagion, not idiosyncratic
- track KPI: HY OAS (add FRED series — still the homeless signal), IG new-issue concession, BDC discounts
- → transmission: **UW low-quality FIN/BDC**; **caution neocloud (COMM/IT rental layer)**

**M-07 — AI capex / Compute (continuous core).** *Datacenter capex persists and is now a named inflation input; the market pays for contracted physical backlog over crowded multiples.*
- current anchor: Apple-Broadcom $30B captive silicon through 2031 signed (07-09 `[daily-US]`); Meta cloud/compute-reseller pivot; DeepSeek own-chip = marginal moat erosion (07-08 `[news]`)
- base 60 / bull(re-accelerates) 25 / bear(capex air-pocket) 15
- anti-signal: a hyperscaler guides capex DOWN on an earnings call → the whole physical chain re-rates
- track KPI: hyperscaler capex guides, Broadcom/Nvidia backlog, ODM orders
- → transmission: **OW IT (compute + memory + custom silicon)**, cross-chain **OW UTIL/INDU (power)**

**M-08 — AI-trade fragility / concentration.** *The AI mega-cap complex de-rates as a ROTATION, not a rupture; extreme crowded-short positioning caps the downside.*
- current anchor: ~$1T off Nvidia on the hawkish tape as rotation (07-09 `[daily-US]`); Nasdaq-100 COT **1%ile crowded-short** (rebound ammo); semis ~19.7% of S&P (record concentration, 07-01 `[news]`); Burry re-short, BofA bubble gauge ~0.9
- base(rotation) 55 / bull(melt-up resumes) 20 / bear(systemic unwind) 25
- anti-signal: equal-weight RSP breaks DOWN with cap-weight (not diverging up) + VIX > 25 → systemic, not rotational
- track KPI: RSP/SPY ratio, VIX, semis % of index, Nasdaq COT %ile
- → transmission: **rotation INTO INDU/FIN/ENRG/UTIL**, OUT of crowded IT/COMM multiples; **OW STPL** (defensive-ready)

**M-09 — Power/Grid (rotating OW).** *AI power demand is structural and accelerating; grid + gas + nuclear + solar-storage + (now) fusion buildout gets policy-backed financing.*
- current anchor: AEP $3.26B DoE grid loan signed (07-09 `[daily-US]`); Chevron-Microsoft 20yr gas PPA, DOE emergency PJM order, Tesla-Sunrun 16GW VPP; Google→Proxima Fusion (07-11 blind-spot)
- base 60 / bull(accelerates) 25 / bear(rate-cost caps rate-base) 15
- anti-signal: 10y > ~5% chokes utility rate-base economics + a datacenter-power interconnection pause
- track KPI: DoE loan flow, PJM capacity prices, PPA signings, interconnection queue
- → transmission: **OW UTIL**, cross-chain **OW INDU(electrical equipment)** + **MATR(copper)**

**M-10 — Memory / AI-inflation channel.** *HBM demand strands consumer DRAM → device price hikes; a rate-insensitive inflation source AND a memory-name re-rating.*
- current anchor: DRAM contract +55–60%, Apple negotiating CXMT/YMTC sourcing, memory "hundred-year flood," Micron profit growth ~1,000% (`[news]`); UBS: memory to out-earn the hyperscalers that buy it
- base 60 / bull(shortage extends) 25 / bear(capacity floods) 15
- anti-signal: CXMT/YMTC/new fab capacity ramps → DRAM contract price rolls over
- → transmission: **OW IT(memory/HBM)**; feeds **M-02** headline-CPI wedge

**M-11 — Defense (continuous core).** *Allied rearmament super-cycle signs contracted, policy-backed backlog — funded software leads, undelivered hardware lags.*
- current anchor: NATO $50bn Deep Strike + Patriot co-production signed (07-09 `[daily-US]`); Lockheed $35B THAAD 7yr interceptor award; counter-drone $500M Army award (AVAV +40%/3d); GAO flags prime slippage (`[news]`)
- base 65 / bull(budgets ratchet) 20 / bear(CR/slippage) 15
- anti-signal: a continuing-resolution freeze + more prime delivery withholds → backlog ≠ revenue
- → transmission: **OW INDU(defense/aerospace)**; bifurcation funded-software > undelivered-hardware

**M-12 — Geopolitics / China chips.** *Export-control regime oscillates; DeepSeek own-chip + selective H200 greenlight = moat erosion at the margin, not collapse.*
- current anchor: DeepSeek own AI chip (07-08); China greenlights limited Nvidia H200 buys (07-08 `[news]`); quantum EOs, critical-minerals processing (`[news]`)
- base 55 / bull(controls tighten, moat holds) 25 / bear(China self-sufficiency accelerates) 20
- → transmission: **caution IT(Nvidia China rev)**; **OW MATR(rare earth/critical minerals)**

---

## 3. ★ Transmission matrix (Phase 0 → Phase 1 input)

| Sector | Tilt | Driver | One-line rationale |
|--------|------|--------|--------------------|
| **IT** | **OW** | M-07 / M-10 | AI capex persists + memory re-rating; M-08 concentration caps but crowded-short = rebound ammo |
| **INDU** | **OW** | M-11 / M-09 | Defense super-cycle signed backlog + grid/electrical buildout — contracted, policy-backed |
| **UTIL** | **OW** | M-09 | AI power demand structural; DoE-financed grid + gas + nuclear + solar-storage + fusion |
| **ENRG** | **OW (tactical)** | M-05 | Iran/Hormuz re-escalation + WTI/gas crowded-short → asymmetric rebound; decorrelates the AI book |
| **FIN** | **OW (watch)** | M-01 / M-06 | Higher-for-longer NIM + steep 2s10s + payments/stablecoin plumbing; UW low-quality BDC/credit |
| **MATR** | Neutral→OW (selective) | M-04 / M-09 | Gold (Fed-credibility) + copper (grid) OW, but copper COT 95%ile crowded-long = overheated |
| **COMM** | Neutral | M-07 / M-08 | AI/platform tailwind offset by Meta $1.4T EU penalty tail + crowded multiple |
| **HLTH** | Neutral (light watch) | M-03 | Defensive bid + M&A (Vertex-Crinetics $10B) but no macro driver |
| **STPL** | Neutral (defensive-ready) | M-08 / M-03 | The "defensives roar if AI falters" hedge; input-cost caps upside |
| **DISC** | **UW** | M-02 / M-03 | Affordability + cost-of-living + input-cost squeeze; robotaxi/Tesla idiosyncratic only |
| **RE** | UW / Neutral (split) | M-01 / M-09 | Higher-for-longer hurts REITs; **datacenter-RE OW** on power demand; housing-bill catalyst |

**Gate → the 4 DEEP targets (2 continuous + 2 rotating):**
- **Continuous:** **IT** (AI compute/memory) · **INDU** (defense + grid/electrical)
- **Rotating:** **UTIL** (power buildout — hottest structural leg this week) · **ENRG** (tactical Iran/oil + crowded-short asymmetry, and the *decorrelating kill-switch lane* — 3 of 4 picks are AI-cycle-correlated, ENRG is the hedge)
- FIN is the strongest honorable-mention (clean, decorrelated OW) → carried as a Phase-1 watch, not gated to DEEP this run.

---

## 4. Self-backtest (prior-anchor continuity)

- **Rotation-vs-rupture (07-09 call): HELD.** Nvidia shed ~$1T but Nasdaq-100 COT sits at 1%ile crowded-short and VIX is *15.8* (calm) — the de-rate is rotational positioning, not a systemic VIX-25 unwind. M-08 anti-signal (RSP breaking down *with* cap-weight) not triggered.
- **Hawkish-of-neutral: CONFIRMED.** Real-10y rose to 2.31% (+0.37/120d), 2s10s bear-steepened to +0.35 — primary data ratifies the Warsh-minutes read; no dovish pivot despite the NFP miss (M-01/M-03 stagflation-lite intact).
- **Memory-inflation wedge: LIVE.** Headline-core CPI gap ~1.35pp with DRAM +55–60% — M-02/M-10 mechanism visible in the print, not just narrative.
- **Prior miss carried:** the earlier "software de-rates under hawkish" call stays **refuted** — AI internal rotation kept draining hardware INTO software (Palantir upgraded/rallied) through 07-04; I do not re-assert it. Software leadership is the live intra-AI tell.
- **Inherited-tape check (per desk rule):** the 07-09 "Iran/Hormuz reopened" and "$1T off Nvidia" figures were cross-checked against the fresh 14d foreign news DB and confirmed (ceasefire-over 07-08, chip selloff 07-08) — not propagated unverified.

*Deliverable complete: §2 proposition table + §3 transmission matrix. Feeds Phase 1 ranking.*

---

## ADDENDUM — 2nd same-day run reconciliation (19:34, intraday freshness)

> The scheduled `industry-us` task re-fired ~18h after the 01:36 run that produced this file and
> the full downstream chain (ROTATION + 4× SECTOR_DEEP + BET_SHEET). Per the same-day collision
> rule, the completed files are **NOT clobbered** — this is an append-only freshness check. Filenames
> preserved for downstream globs (광기 propose/execute, apex strategy-us/real).

**FRED re-pull (fresh vs the 01:36 snapshot):** unchanged within one extra day of data.
| Metric | 01:36 report | 19:34 re-pull | Δ |
|---|---|---|---|
| Fed Funds | 3.62% | **3.62%** @07-09 | flat |
| 10y UST | 4.56% @07-08 | **4.54%** @07-09 | −0.02 (still restrictive) |
| 2y UST | 4.21% | **4.16%** @07-09 | −0.05 |
| Real 10y | 2.31% | **2.31%** @07-09 | flat |
| Broad DXY | 120.69 @07-02 | **120.69** @07-02 | flat |
| VIX | 15.84 @07-09 | **15.84** @07-09 | flat |
CPI/core (May), U-rate (Jun), M2 (May) are monthly — no new print. **Primary regime unchanged.**

**Intraday news scan (fresh 2-day blind-spot, 220-row sample + market-moving grep):** no new absent
macro event, no credit rupture, no CPI/NFP/Fed surprise in the ~18h window. The two fresh tape reads
both *ratify* the morning propositions rather than break them:
- *"Chip Stocks Join in Broad Selloff"* → **M-08 rotation/de-rate intact** (not a VIX-25 systemic unwind; VIX still 15.8).
- *"WTI slips below $74 after recent rally, Middle East tensions limit the downside"* → **M-05 oscillation intact** (oil two-sided, Hormuz premium capping the downside; crowded-short ammo still live).
- Emergent terms (Hynix, Broadcom, Energy, Data) all already-bucketed (memory/IPO, custom silicon, power).

**Verdict:** the 2026-07-11 morning run remains valid intraday. No re-derivation of Phase 1–4 warranted;
the ROTATION / SECTOR_DEEP / BET_SHEET files stand as the day's deliverables. Anti-signals for M-01
(real-10y < 2.0%), M-05 (Hormuz normalizes), and M-08 (RSP breaks down *with* cap-weight + VIX > 25)
remain un-triggered.
