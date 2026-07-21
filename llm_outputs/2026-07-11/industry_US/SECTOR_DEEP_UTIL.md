# SECTOR DEEP — UTILITIES / POWER (UTIL)
**Phase-2 DEEP · 2026-07-11 · Analytical only (no buy/sell advice; sizing language = influence weighting, not recommendation)**

Driver: **M-09 — AI power demand, structural & accelerating.** UTIL is the cross-chain SINK of the AI-capex cycle: IT capex → power offtake → generation → grid/transformers → interconnection. Macro cross-current: real-10y 2.31% and rising `[FRED]` is a rate-sensitivity headwind for regulated rate-base multiples, **partly offset** by demand-backed rate-base growth and now policy-backed federal financing (Energy Dominance Financing program).

---

## 1. FLOW — news heat + FINRA short-vol divergences

**News window (60d, foreign, body-search).** AND-mode with 8 terms returned 0 (over-constrained); OR-mode returned **240 matches** on the theme set and **1,163** on the IPP/grid set `[news]`. Dominant clusters:
- **VPP / behind-the-meter**: Sunrun–Tesla–Renew Home **16 GW** virtual power plant for data centers, RUN +26–30% `[news]`.
- **Nuclear / SMR mania**: OKLO, NuScale (SMR), Nano Nuclear (NNE), Fermi, Bloom Energy (BE), BWX reactor-design license; "$17.5B DOE loans" nuclear-resurgence framing `[news]`.
- **Gas PPA**: Microsoft "Project Kilby" (Stifel note flags data-center power demand) `[news]`.
- **Grid / transformers**: solid-state transformer upgrade cycle (ENPH), grid-modernization GIS `[news]`. Williams pivot to behind-the-meter (midstream/ENRG-adjacent) `[news]`.

**FINRA Reg SHO daily short-vol z-scores (2026-07-09)** `[FINRA]` — flagging |z|>=1.5:

| Ticker | Short% | Z (vs own 20d) | Read |
|---|---|---|---|
| **NRG** | 27.9% | **-2.72** 🟢 | Short-vol collapse — cover / pressure exit. Strongest divergence in sector. |
| **AEP** | 27.3% | **-1.73** 🟢 | Short-vol collapse — coincides with $3.26B DoE Texas loan close 07-08/09. |
| **NEE** | 57.1% | +1.18 | Mild build, not extreme. |
| SRE | 65.8% | +1.27 | Mild build. |
| **RUN** | 40.8% | **-1.43** (near) | Short cover into 16 GW VPP deal. |
| EXC | 21.7% | -1.29 (near) | Short-vol easing. |
| TLN | 62.1% | +0.67 (+18.1▲ trend) | Elevated absolute short%, rising 5v5 — crowded. |

Note: 40–45% short-vol is normal (MM hedging). The actionable signals are the **negative-z collapses (NRG, AEP, RUN, EXC)** = short covering / de-risking, and TLN's **rising** short-vol trend = the crowded end of the trade. VST/CEG/OKLO/SMR/NNE all sit in the neutral band (no flow edge either way).

---

## 2. PLAYERS

**(a) UTIL members in us_top300** `[us_top300]` (15 names):
NEE (180.9B, Multi-Util), SO (104.9B), CEG (97.9B), DUK (96.6B), AEP (69.5B), D (60.2B), SRE (59.3B), VST (55.2B), ETR (50.9B), XEL (48.3B), EXC (46.9B), PEG (39.8B), ED (39.2B), WEC (36.5B), PCG (36.3B).

**(b) Below-cutoff thematic names — qualified via yfinance (>=2x in window, real US ticker, mcap ~>=$2B)** `[yfinance][news]`:

| Ticker | Mcap | yf Sector | Bucket | Qualifies |
|---|---|---|---|---|
| TLN | 18.6B | Utilities | Nuclear IPP | ✔ (behind top300 cutoff but large) |
| NRG | 29.7B | Utilities | IPP+retail | ✔ |
| OKLO | 8.4B | Utilities | SMR (pre-rev) | ✔ (optionality, not fundamentals) |
| SMR (NuScale) | 3.1B | Industrials | SMR (pre-rev) | ✔ (optionality) |
| BE (Bloom) | ~ (news 1,410% run) | Industrials | Fuel-cell BTM | ✔ (borderline — INDU, on-site power) |
| RUN (Sunrun) | 3.0B | Technology | Solar+storage VPP | ✔ |
| FSLR | 24.4B | Technology | Solar modules | ✔ (theme-adjacent, TECH-classified) |
| NNE (Nano Nuclear) | 1.0B | Industrials | Micro-reactor | ✘ mcap <$2B — **watch only** |
| LEU (Centrus) | 3.4B | Energy | HALEU fuel | ✔ (fuel-cycle, ENRG) |
| BWXT | 17.1B | Industrials | Reactor components | ✔ (INDU) |
| CCJ (Cameco) | 41.7B | Energy | Uranium | ✔ (ENRG fuel node) |

SMR-classified names (OKLO, SMR/NuScale, NNE) are **pre-revenue optionality** — SEC confirms below.

---

## 3. IR / WHO-DOES-WHAT (SEC 10-K, English extract) `[SEC]`

**CEG — Constellation Energy** (10-K FY2025, filed 2026-02-24). Post-**Calpine acquisition (closed Jan 7, 2026)** it is "the largest private-sector power producer in the world," **55 GW** across nuclear, gas, geothermal, hydro, wind, solar. Nuclear-heavy clean baseload = the premier clean-firm counterparty for hyperscaler PPAs. Bucket: **Nuclear IPP (merchant + PPA)**.

**VST — Vistra** (10-K FY2025). Integrated retail + merchant generation, California→Maine. Item 1A anti-signals `[SEC]`: revenue exposed to **wholesale price + Market Heat Rate swings**; **can't fully hedge commodity/heat-rate**; forced-retirement risk on underperforming units; and explicitly — *"if electricity demand does not grow at the rate expected, or if we are unable to execute on large load offtake opportunities including under long-term [contracts]"* the thesis breaks. So VST's AI-demand story is **self-identified as the swing variable**. Bucket: **Merchant IPP + retail (levered to load-offtake execution)**.

**OKLO** (10-K FY2025, filed 2026-03-17). Aurora fast-fission "powerhouses"; fuel-recycling optionality. Item 1A / risk bullets `[SEC]` are textbook pre-revenue: *"early-stage company with a history of financial losses (negative cash flows)… expect to incur significant expenses"*; reliance on **HALEU / plutonium-based fuel** not yet fabricated at scale; **limited specialized suppliers, first-of-a-kind components**; and *"customers… may rescind or back out of non-binding agreements"* — i.e. the order book is LOIs, not revenue. MD&A shows no product revenue. Bucket: **SMR pre-revenue optionality**.

**AEP** — WebSearch-confirmed `[WebSearch]`: DOE closed **up to $3.26B** loan to **AEP Texas** (07-08/09) via the **Energy Dominance Financing** program — ~100 transmission projects / ~2,800 miles reconductor+new-build, projected $685M customer savings/30yr, and AEP Texas holds **letters of agreement for up to 41 GW** of new load through 2030. This is the cleanest *regulated* AI-load story with a federal-financing catalyst. Bucket: **Regulated T&D (grid rate-base)**.

**Cross-check on the gas node** `[WebSearch]`: Chevron–Microsoft **Project Kilby** = **2.67 GW** co-located West-Texas plant, 20-yr PPA, first power ~2028, ~$9B, **majority generation from GE Vernova turbines** (+ Caterpillar Solar Turbines). Confirms the UTIL→INDU (turbines) and UTIL→ENRG (gas) chains below.

---

## 4. VALUE-CHAIN DENSITY MAP (left → right)

```
FUEL / INPUTS        GENERATION / IPP        TRANSMISSION+GRID      INTERCONNECT        DATACENTER OFFTAKE
─────────────        ─────────────────       ─────────────────      ────────────        ──────────────────
Uranium: CCJ         Nuclear IPP: CEG,TLN     Grid rate-base:        PJM capacity        Behind-the-meter:
HALEU: LEU           Merchant IPP: VST,NRG    AEP,ETR,PEG,ED,        market /            RUN(VPP),BE(fuel cell),
Gas (→ENRG):         Regulated gen: SO,DUK,   XEL,D,PCG              interconnection     Sunrun-Tesla 16GW
  CVX Kilby,           NEE(+renew),EXC        Transformers/          queue = the         Williams(BTM,ENRG)
  Williams(BTM)      SMR pre-rev:            switchgear (→INDU):     BINDING gate        Hyperscaler PPAs:
Reactor parts:         OKLO,SMR,NNE           GEV,ETN,ENPH(SST)                          MSFT,GOOG,Chevron
  BWXT (→INDU)       Solar+storage:                                                      counterparties
                       FSLR,RUN,ENPH
```

**Cross-sector chains (marked):**
- **UTIL ← IT** — hyperscaler AI capex is the demand source (MSFT/GOOG/Amazon PPAs). Demand-side origin sits in IT/COMM.
- **UTIL → INDU** — gas turbines & transformers: **GEV** (Kilby turbines, $291.9B mcap), ETN, and reactor components **BWXT**. This is where the physical bottleneck monetizes.
- **UTIL → ENRG** — feed-gas & fuel cycle: **CVX** (Kilby), **Williams** (behind-the-meter pivot), uranium **CCJ**, HALEU **LEU**.
- **UTIL → MATR** — copper/grid metals for 2,800-mi reconductor programs (AEP) — implied, not a UTIL ticker.

**BELOW-RADAR layer (do NOT converge on NEE/CEG):**
1. **Behind-the-meter / VPP developers** — RUN (16 GW Tesla VPP), BE (on-site fuel cells). Under-covered vs. the big IPPs; RUN flow shows short-cover (z≈-1.43).
2. **Transformer / switchgear & solid-state-transformer bottleneck** — ENPH upgrade, GEV/ETN grid gear. The interconnection constraint's real chokepoint is *hardware lead-time*, not generation.
3. **SMR pre-revenue optionality** — OKLO/SMR/NNE: pure narrative/optionality, SEC-confirmed no revenue.
4. **Regulated T&D with federal financing** — AEP's DoE loan is the under-appreciated *regulated* path to AI load (41 GW LOAs) that the market discusses less than merchant IPPs.

---

## 5. BOTTLENECK · KPI · ANTI-SIGNAL

**Binding constraints (in order):**
1. **Interconnection queue** — PJM/ERCOT queue length is the #1 gate; a datacenter-power interconnection *pause* would freeze the whole thesis.
2. **Transformer & gas-turbine lead-times** — multi-year backlog (GEV order book); the physical bottleneck that caps how fast offtake converts to MW.
3. **SMR regulatory + pre-revenue** — OKLO/SMR/NNE need NRC licensing + first-of-a-kind fabrication (HALEU supply); timeline slippage is the base-rate outcome `[SEC]`.

**KPI readings now:**
- DoE loan flow **live** — AEP $3.26B closed; "$17.5B" nuclear-loan program framing `[WebSearch][news]`.
- 41 GW of signed load-LOAs at AEP Texas through 2030 `[WebSearch]`.
- Kilby FID expected end-2026; first power 2028 `[WebSearch]`.
- Real-10y **2.31% and rising** `[FRED]` — watch the rate-base discount.

**What KILLS the thesis:**
- **10y > ~5%** → chokes regulated rate-base economics (multiple de-rate for NEE/DUK/SO/AEP).
- **A datacenter-power interconnection pause / moratorium** (grid-reliability or ratepayer-backlash driven) → removes the offtake growth premium across IPPs.
- **SMR timeline slippage / failed licensing** → OKLO/SMR/NNE optionality re-prices to ~0; these are *not* fundamentals.
- **Demand growth undershoot** — VST's own 10-K names "if electricity demand does not grow at the rate expected" as the break `[SEC]`.

---

## SHORTLIST (ranked, for Phase 3)

1. **CEG** — Largest private power producer post-Calpine (55 GW), nuclear-heavy clean-firm; premier hyperscaler-PPA counterparty. Node: Nuclear IPP/generation. Bucket: **IPP (nuclear)**. Freshness: 10-K FY2025 fresh `[SEC]`; flow neutral (z+0.14).
2. **AEP** — Regulated T&D with $3.26B DoE loan + 41 GW load-LOAs; cleanest *regulated* AI-load path. Node: Transmission/grid. Bucket: **Regulated**. Freshness: catalyst 07-08/09 `[WebSearch]`; flow z=-1.73 🟢 short-cover.
3. **VST** — Merchant IPP+retail levered to large-load offtake execution (self-identified swing variable). Node: Generation/IPP. Bucket: **IPP (merchant)**. Freshness: 10-K FY2025 `[SEC]`; flow neutral.
4. **NRG** — IPP+retail; strongest flow divergence (short-vol z=-2.72). Node: Generation/IPP. Bucket: **IPP (merchant)**. Freshness: flow 07-09 🟢 `[FINRA]`; watch for the catalyst behind the cover.
5. **TLN** — Nuclear IPP, direct datacenter-adjacent (behind-the-meter nuclear narrative). Node: Nuclear IPP. Bucket: **IPP (nuclear)**. Freshness: crowded — short-vol 62%, 5v5 +18▲ `[FINRA]` = the packed end of the trade.
6. **RUN** — Sunrun 16 GW Tesla/Renew VPP for datacenters; below-radar BTM/VPP developer. Node: Datacenter offtake / behind-the-meter. Bucket: **Solar+storage/VPP**. Freshness: deal 06-24, flow z≈-1.43 short-cover `[news][FINRA]`.
7. **NEE** — Largest regulated+renewables platform; rate-sensitivity headwind but demand-backed rate base. Node: Regulated gen + renewables. Bucket: **Regulated**. Freshness: flow z+1.18 mild build `[FINRA]`.
8. **OKLO** — Aurora SMR + fuel recycling. **Pre-revenue optionality, NOT fundamentals** — SEC: negative cash flow, LOI-not-revenue order book, HALEU supply risk `[SEC]`. Node: SMR gen (pre-rev). Bucket: **SMR**. Freshness: 10-K 2026-03-17; narrative-driven.
9. **GEV** *(cross-sector, INDU)* — Gas-turbine + grid-gear bottleneck monetizer; supplies Kilby. Node: Transformers/turbines (UTIL→INDU). Bucket: **Equipment (cross-sector)**. Freshness: Kilby-confirmed `[WebSearch]`.
10. **SMR (NuScale)** — SMR pre-revenue optionality (INDU-classified). Node: SMR gen (pre-rev). Bucket: **SMR**. Freshness: heavy news mania `[news]`; flow neutral. *(Watch-only sibling: NNE — mcap <$2B.)*

*Buckets legend: Regulated (rate-base, rate-sensitive) · IPP merchant/nuclear (load-offtake levered) · SMR (pre-revenue optionality) · Solar+storage/VPP (behind-the-meter) · Equipment (cross-sector INDU bottleneck).*

Evidence tags: `[FRED]` real-10y · `[SEC]` 10-K Item 1/1A/7 · `[news]` search_news_alert body-search · `[FINRA]` us_flow short-vol · `[yfinance]` sector/mcap · `[WebSearch]` deal confirmation · `[us_top300]` universe.
