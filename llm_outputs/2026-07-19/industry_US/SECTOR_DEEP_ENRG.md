# DEEP · ENRG — 2026-07-19 (Sun) ★US-only · **CONTINUOUS TRACK**

> Stage 6 / L1·DEEP. Runtime `--market us`, `--scope foreign` on every news call. Zero buy/sell
> calls, zero sizing (BET owns sizing).
> **Inputs reread from disk (not memory):** `MACRO_REPORT.md` (§1, §4, §4a P3/P3′) ·
> `SWEEP_READ.md` (§sector ranking, §CYCLE EXPOSURE GAP) · `EVENT_ALPHA.md` (Cards 1, 2) ·
> `SECTOR_ROTATION.md` (§2a) · `BLINDSPOT_PREMORTEM.md` (**Findings A & B, §3 re-tags, §4 GAP**) ·
> `data/cycles/cycle_registry.json`.
> **PRIOR DEEP (continuous-track anchor): `llm_outputs/2026-07-17/industry_US/SECTOR_DEEP_ENRG.md`.**
> Per the continuous-track rule this file **leads with the delta** and **carries unchanged structure
> by reference** — the 7-node map, the KMI/LNG take-or-pay filing work, and the integrated/E&P/services
> split are *not* re-printed; §4 and §6 state exactly what is carried and what changed.
>
> ⚠⚠ **asof = 2026-07-17 close.** The 07-18 US combat deaths in Jordan and the 07-19 US strike on the
> IRGC are **in NO price, no flow tag, and no crack print in this file.** Monday is a gap event.

---

## §0 DELTA since 2026-07-17 — lead

### ★ D1 — The prior DEEP's central claim is **REVERSED**, and I reproduced the reversal from raw data
The 07-17 file (§7B) concluded: *"a Hormuz-driven crude-price collapse would actually **widen** the
crack… refiners are a spread business."* Directionally that is a statement about the ceasefire branch —
and it is **right**. But the file paired it with *"the crack thesis is structurally decoupled from
Hormuz"*, and MACRO P3′ then promoted that into *"anti-fragile to a TACO/ceasefire"*, i.e. **the
escalation branch was never priced.** PREMORTEM Finding A caught it. Recomputed here from yfinance
`CL=F`/`HO=F`, independent of PREMORTEM's table — **it reproduces to the cent**:

| Date | CL=F | HO=F | **Distillate crack $/bbl** | 3-2-1 | Δcrack |
|---|---|---|---|---|---|
| 07-13 | 78.14 | 3.82 | 82.45 | 64.05 | — |
| 07-14 | 79.34 | 4.01 | 89.26 | 67.22 | +6.81 |
| 07-15 | 79.60 | 3.95 | 86.23 | 68.10 | −3.03 |
| **07-16** | 78.95 | **4.03** | **90.34 ← the top** | **69.45 ← the top** | +4.11 |
| **07-17** | **81.78** (+3.6%) | 3.94 | **83.57** | **62.70** | **−6.77 (−2.8σ)** |

**Confirmed: the KPI topped 07-16 and crude rose +3.6% on 07-17 while product fell.**

### ★ D2 — But I must correct Finding A's *generalization*, and the correction makes the answer HARDER
PREMORTEM wrote the consequence as a rule: *"a Monday crude escalation gap is CRACK-NEGATIVE on a
1–5 day horizon."* **Measured against a 1-year base rate, that is not a rule — it is what happened once.**

| Test (1y daily, n=250) | Measured |
|---|---|
| corr(Δcrack $/bbl, crude daily return) | **+0.365** — *positive* |
| Δcrack per +1% crude, OLS | **+0.365 $/bbl** — *positive* |
| Days with crude **> +3%** | **n=33**; Δcrack **positive on 67%**, mean **+1.35/bbl**, median +1.36 |

> **Corrected consequence, and it is the load-bearing sentence of this file:** the Hormuz binary is
> **genuinely two-sided for refiners — it has no clean branch.** A crude-only supply shock (crude
> reprices, product cannot follow) is crack-negative — that was 07-17, and 03-06 (crude +12.2%,
> crack −9.55, **PBF −5.3%**), 03-09 (+4.3%, −5.37, **PBF −11.9%**), 03-30 (+3.3%, −8.75, **MPC −2.7%**).
> A broad complex/product shock is crack-**positive** — that was 07-08 (crude +4.4%, crack **+11.86**,
> PBF +9.2%) and 07-13 (+9.4%, **+4.62**, PBF +8.0%). **Both branches are on this month's own tape.**
> Finding A's *sign for 07-17* stands; its *forward rule* does not. MACRO P3′ was one-sided in one
> direction; the premortem correction was one-sided in the other. **The truth is that this leg is
> short volatility of the crude/product spread, and both gaps are live.**

### ★ D3 — The detachment is real and now **quantified per name** (new; nobody in the run had this)
Two-factor OLS (crude return, Δcrack) fitted on 1y daily, then applied to 07-17:

| Ticker | 07-17 actual | 2-factor predicted | **RESIDUAL (detachment)** |
|---|---|---|---|
| **CVI** | +4.99% | −0.77% | **+5.76pp** |
| **PBF** | +2.97% | −1.69% | **+4.66pp** |
| **VLO** | +3.13% | −0.40% | **+3.53pp** |
| **DINO** | +2.02% | −0.57% | **+2.58pp** |
| **PSX** | +2.75% | +0.03% | **+2.72pp** |
| **MPC** | +2.21% | +0.16% | **+2.05pp** |

★ **The residual is monotonically ordered by extension and by narrative-carry.** The names being sold
as a *geopolitical hedge* detached most; the names with non-crack segments detached least. And the
conditional base rate says this is anomalous: on the 15 prior 1y days with **crude up >2% AND crack
down**, mean returns were **PBF −0.14%, VLO −0.00%, DINO +0.05%** — flat-to-negative, not +3%.
**07-17 is day 1 of detachment, measured, not asserted.**

### ★ D4 — The narrative tell that explains the residual [new, from the tape]
- *"Here's Why Shares in **PBF Energy** Popped Higher (And are a **Great Way to Hedge Geopolitical
  Conflict**)"* [yahoo_finance **07-17**] — the exact day of the −6.77 crack print.
- *"**Five Oil and Gas Stocks Ready for a Hormuz Spike** and a Hawkish Fed"* [yahoo_finance 07-15]
- *"The **best energy stocks right now** as two major conflicts keep oil prices elevated"* [CNBC 07-16]

> **The instrument is being marketed to the retail bid as a *war* hedge at the moment its actual KPI
> rolled over.** That is the mechanism of the residual, and it is a late-cycle signature, not an early one.

### ★ D5 — Kill-switch proximity, measured (2-year context nobody had)
| Kill switch | Level now | Distance | Verdict |
|---|---|---|---|
| **Crack < $75** (PREMORTEM's own flip level) | **83.57** | **−8.57 = 3.56σ… but only 1.27× the single 07-17 move.** 9 days in 2y had a drop ≥6.77 | **~1.3 adverse sessions away** |
| **Crack percentile** | 83.57 | **96th %ile of 2 years. 2y median = $31.70. 2y max = $95.23.** The crack has been >$75 on **4% of the last 2 years** | ★ **The KPI is not early. It is at 2.6× its own 2-year median** |
| **Russian diesel export ban expiry** | in force | **hard date 2026-07-31 — D+12** | Un-extended = a dated kill |
| **Hormuz binary** | live, undated | `ceasefire\|truce\|Hormuz\|negotiations` = **333 hits/3d** (foreign) | ★ **New: a ceasefire FRAMEWORK exists** — *"Iran says it's **suspending ceasefire commitments** with U.S. after escalating strikes"* [businessinsider **07-18**]. A suspension can be un-suspended; this raises the TACO branch's base rate versus a world with no framework |

### D6 — New mechanism prints since 07-17 (mechanism is **still accelerating**)
- *"Ukraine Says It Hit Russia's **Yanos** Oil Refinery Thursday"* [Bloomberg 07-17] → **3 strikes in 7 days**: Syzran 07-12, Afipsky 07-14, Yanos 07-17.
- *"**India Raises Export Levies on Diesel and Jet Fuel**"* [Bloomberg 07-16] — the marginal export barrel is being withheld by policy. Counter-print same week: *"**India Refiners Reap Fuel Export Windfall** as War Drives Shortages"* [Bloomberg 07-14] — the supply response exists and is being taxed, not prevented.
- *"middle **distillate inventories** have declined, averaging **15% lower than last year**"* [hellenicshipping 07-17] — physical confirmation, sourced.
- *"US Drivers Are Again Paying **More Than $5 a Gallon for Diesel**"* [Bloomberg 07-16] · *"**+33% since start of Iran war**"* [NYT 07-16].
- **Named anti-print, already on the tape:** *"**refineries will eventually return**, BRS said"* [hellenicshipping 07-17]; Commerzbank models *"following the **lifting of the export ban** on oil products"* [FXStreet 07-17].
- ★ **Demand-side print, new:** *"**United Airlines gets hit by a $6 billion added-fuel-cost headwind**"* [MarketWatch 07-16] — the crack has a named counterparty now (§4, §6).

### D7 — Calendar resolved (MACRO §0 flagged **KMI 07-22-or-23** as unresolved)
`yfinance` calendar: **KMI = 2026-07-23** ✓ (resolves the ⚠). Refiner prints: **DINO 07-28 · VLO
07-30 · PBF 07-30 · CVI 07-30 · MPC 08-04 · PSX 08-05 · PARR 08-05 · DK 08-05.**
★ **Structural, not trivia: VLO/PBF/CVI print 07-30 — one day BEFORE the export ban expires.
MPC/PSX/PARR/DK print AFTER (08-04/05), into a resolved kill switch.** This is a dated difference
between expressions and it is used in §6.

### What is CARRIED UNCHANGED BY REFERENCE (not re-derived, not re-printed)
1. **The 7-node value-chain map** and the *bottleneck = refining capacity, not crude, not demand*
   finding — 07-17 §4. Re-tested for falsification in §4 below; **it survives and is now doubly sourced.**
2. **The KMI / LNG primary-filing work** — 10-K take-or-pay language, LNG's $107.7B fixed vs $182.9B
   variable fee split, and the conclusion that **neither has crack participation** — 07-17 §3. Unchanged.
3. **The integrated / E&P / services split** (XOM, CVX, EOG, COP, OXY, DVN, SLB, BKR = crude monetizers
   and laggards, distributing) — 07-17 §1. **Re-measured today and unchanged**: XOM RS60 −6.2%, CVX 분산
   RS60 −4.8%, XLE RS60 −2.3%.
4. **LNG's short-vol z +3.09** standalone anti-signal — 07-17 §6 finding (3). Not re-pulled; carried.
5. **The tanker one-hop is dead** — 07-17 §5 found no breakout; EVENT_ALPHA Card 2 killed it as
   STORY-ONLY (FRO/STNG/TNK all 분산, vol 0.58–0.74×). **Two independent kills. Not revisited.**

---

## §1 Flow — measured today, with the short-z × narrative divergence

`module_flow --bench SPY` + `scripts/us_flow.py` (FINRA Reg SHO, 07-17 session) + yfinance ATR(14).

| Ticker | flow | OBV | RS20 | RS60 | vol | **ATRs > 50dma** | **% off 52w high** | short-vol z / 5v5 | short % float |
|---|---|---|---|---|---|---|---|---|---|
| **PBF** | 🟡중립 | 매집 | **+65.8%** | +48.6% | 1.13× | **5.83** | **0.0%** | +0.94 / **−2.5▼** | **15.9%** |
| **PARR** | 🟡중립 | 매집 | +49.6% | +18.3% | 0.88× | **5.00** | **0.0%** | −1.03 / −1.3▼ | 13.1% |
| **DK** | 🟡중립 | 매집 | +49.1% | **+56.5%** | 1.07× | **5.34** | **0.0%** | −1.14 / −3.7▼ | 13.5% |
| **DINO** | **🟢가속** | 매집 | +34.1% | +43.2% | **1.28×** | **5.95** | **0.0%** | +0.37 / **+4.6▲** | 5.2% |
| **VLO** | 🟡중립 | 매집 | +28.8% | +27.1% | 1.08× | 4.69 | **0.0%** | −0.63 / −1.7▼ | 4.0% |
| **MPC** | 🟡중립 | 매집 | +27.5% | +36.3% | **0.90×** ⚠ | 5.61 | **0.0%** | +0.18 / −2.2▼ | 2.9% |
| **PSX** | 🟡중립 | 매집 | +23.4% | +24.2% | 1.03× | **4.52 ← least** | **0.0%** | −0.98 / **−15.4▼** | **2.3% ← least** |
| **CVI** | 🟡중립 | **중립** | +26.6% | **+7.0%** | 0.97× | **2.18 ← least** | **−12.2% ← only one not at highs** | +0.49 / −3.5▼ | **16.2%** |
| XOM | 🟡중립 | 중립 | +4.4% | −6.2% | 0.93× | 0.44 | −14.1% | — | 1.0% |
| CVX | 🟡중립 | **분산** | +5.2% | −4.8% | 0.72× | 1.45 | −11.3% | — | 1.0% |
| XLE / XOP | 🟡중립 | 매집 | +5.2 / +9.0% | −2.3 / −2.4% | 0.92 / 0.84× | — | — | — | — |

### ★ The divergence this section exists to state: **short-z says the fuel is gone, the narrative says it's starting**
- **Seven of the eight refiners sit at exactly 0.0% off their 52-week high** and **4.5–6.0 ATRs above
  their 50dma.** There is no overhead supply anywhere in the group.
- **Every short base is flat-to-exiting**: PSX **5v5 −15.4▼** (the largest covering print on the board),
  DK −3.7▼, CVI −3.5▼, PBF −2.5▼, MPC −2.2▼, VLO −1.7▼, PARR −1.3▼. **DINO is the sole exception
  (+4.6▲, shorts *adding*) — and DINO is the only 🟢가속 name.** Confirms PREMORTEM's "short base spent":
  at the *daily-flow* level it is spent. ⚠ **Precision the run has been sloppy about: short % of FLOAT
  is still 15.9% (PBF), 16.2% (CVI), 13.5% (DK), 13.1% (PARR).** What is spent is the covering *flow*,
  not the *stock* of shorts. The squeeze fuel is not gone — it is just no longer being lit.
- **Narrative says early** (mechanism accelerating, 3 strikes/7d, inventories −15% y/y, `refining margin`
  30 hits/7d = un-crowded by news). **Price and positioning say late** (0.0% off highs ×7, 5.0–6.0 ATRs,
  covering exhausted, KPI at the 96th %ile of 2y and already rolled over). **This is not a resolvable
  tie — it is the definition of the EARLY-mechanism / LATE-instrument split, and §6 commits on it.**
- **CVI is the lone structural exception and it is measured, not inferred**: only **2.18 ATRs**, **−12.2%
  off its high**, RS60 only **+7.0%**. But it also carries the **largest detachment residual (+5.76pp)**,
  **OBV 중립 not 매집**, the **highest short % float (16.2%)** and **fwd PE 20.2 — the most expensive of
  the eight.** *Less extended is not the same as cheaper or safer.* §6 rules on it.

---

## §2 Players — large-cap universe UNION thematic small-caps
Bar: named ≥2× in the sector news window **AND** a real ticker **AND** mcap ≥ ~$2B. This union is where
the alpha leaks — the 07-17 file's own §5 admitted PBF and CVI were **below the ≥2× bar and logged, not
promoted**, and both then ran +66% / +27%. **The bar was right and the *window* was too short.**

| Ticker | Name | Node | mcap | fwd PE | Named-in-window evidence |
|---|---|---|---|---|---|
| **VLO** | Valero | Pure refining (+renewable diesel, ethanol) | **$91.9B** | 13.9 | Flow epicenter; *"best energy stocks"* [CNBC 07-16]; ⚠ **still 0 title mentions in chain-hop** |
| **MPC** | Marathon Petroleum | Refining + MPLX midstream | **$91.3B** | 12.4 | Flow epicenter, carried |
| **PSX** | Phillips 66 | **5 segments** (§3) | **$82.9B** | **11.5 ← cheapest large** | Flow epicenter; registry `core_pick` |
| **DINO** | HF Sinclair | Refining + lubricants + renewables | **$16.0B** | 10.8 | Promoted 07-17; **only 🟢가속 in the complex** |
| **PBF** | PBF Energy | Pure-play independent refiner | **$7.4B** | 10.6 | ★ *"PBF… **Great Way to Hedge Geopolitical Conflict**"* [yahoo 07-17]; *"PBF: Refining Boom"* [SA 07-16] — **now ≥2×, promoted** |
| **DK** | Delek US | Small independent refiner | **$3.9B** | 26.3 ⚠ | EVENT_ALPHA Card 1 exposure row; PREMORTEM §3 re-tag |
| **PARR** | Par Pacific | Hawaii/Rockies refiner | **$3.8B** | **7.3 ← cheapest of all** | PREMORTEM §4 (RS20 +49.6%); **absent from every prior DEEP** |
| **CVI** | CVR Energy | Refining + **nitrogen fertilizer** + renewables | **$3.5B** | **20.2 ⚠ dearest** | *"CVR Energy: Refining Margin Benefits Are Underpriced"* [SA 07-02] + PREMORTEM §4 — **now ≥2×, promoted** |
| XOM / CVX | Integrateds | Crude monetizers | $610.8B / $373.2B | 13.9 / 15.0 | **Counter-sign to the crack** — carried by reference |
| **DAL** | Delta Air Lines | ★ **The crack's counterparty** | **$55.4B** | **9.5** | *"UAL hit by **$6B added-fuel-cost headwind**"* [MarketWatch 07-16]; chain-hop headline-named (1 title / 2 body) |
| KMI / LNG | Midstream / LNG export | **Zero crack participation** (07-17 §3, primary filings) | — | — | Held book; **KMI prints 07-23** |

⚠ **Tool-floor finding, stated for the third consecutive run:** `chain-hop`'s universe is `us_top300`.
**PBF ($7.4B), DK ($3.9B), PARR ($3.8B), CVI ($3.5B) are structurally invisible to it** — and those four
are the run's four biggest movers. **The bounded-union bar above is the ONLY mechanism in this pipeline
that can see them, which is why §2 must be a union and not a screen output.**

---

## §3 IR anchor — primary sources

### PSX — 10-K FY2025, filed **2026-02-20** [EDGAR, `psx-20251231.htm`] — ★ new work, not carried
> *"Our businesses are organized into **five operating segments**: 1) **Midstream**… 2) **Chemicals** —
> Consists of our **50% equity investment in Chevron Phillips Chemical Company LLC (CPChem)**… 3)
> **Refining** — Refines crude oil and other feedstocks into petroleum products, such as gasoline and
> **distillates, including aviation fuels**. At December 31, 2025, this segment included **10 refineries
> in the United States and Europe**. 4) **Marketing and Specialties**…"*

★ **And the single most important primary-source line found this run:**
> *"In the **fourth quarter 2025, we ceased fuel production and began idling the facilities at our Los
> Angeles Refinery**."*

**Verdict — and it cuts two ways, both stated:** (i) PSX is *shrinking* the very asset the thesis is long,
so its own barrel count falls; (ii) **it is simultaneously a permanent, company-confirmed reduction in
US West Coast conversion capacity — a bottleneck contributor that no ceasefire reverses and no export-ban
expiry undoes.** This is the only piece of the mechanism in this file sourced from a 10-K rather than a
war headline, and it is therefore the only piece immune to both kill switches. **It matters far more for
§4 and §6 than for PSX's own EPS.**

### CVI — 10-K FY2025, filed **2026-02-18** [EDGAR, `cvi-20251231.htm`]
> *"**three reportable segments**: •**Petroleum Segment** includes the refining and marketing of high
> value transportation fuels which consist of gasoline, **diesel, jet fuel, and distillates**… •**Renewables
> Segment**… •**Nitrogen Fertilizer Segment** includes the production and distribution of nitrogen
> fertilizer products, primarily in the form of **ammonia and urea ammonium nitrate (UAN)**, for the
> farming industry."*
> *"Coffeyville Refinery… name plate crude oil capacity of **132,000 bpd**"* (+ Wynnewood).
> ★ *"In **December 2025**, the Company **reverted the renewable diesel unit ("RDU") at the Wynnewood
> Refinery back to hydrocarbon processing service**, considering the unfavorable economics of the
> renewables business."*
> *"As of December 31, 2025, **Icahn Enterprises L.P.**… owned approximately **70% of our outstanding
> common stock**."*

**Verdict:** CVI added distillate-capable capacity back in Dec-2025, one quarter before this cycle — a
genuine operational tailwind nobody in the run had. **But three disqualifying facts sit next to it:**
70% Icahn ownership (float **29M shares**, the smallest in the set, against 16.2% short interest — a
structurally violent tape), **fwd PE 20.2 — the most expensive of the eight refiners**, and
`module_disclosure_us CVI` returns **three Item 5.02 management-change 8-Ks in 90 days** (management
churn at a controlled company). **CVI is less extended for reasons that are partly idiosyncratic, not
because the market has failed to notice the crack.**

### MPC / VLO — 10-K language **carried by reference** from 07-17 §3
Unchanged and not re-pulled: MPC ~3.0m bpd, three segments incl. midstream; VLO 15 refineries / ~3.2m bpd,
**no midstream fee buffer**; MPC's Item 1A explicitly names *"temporary and permanent **closures**,
utilization levels and capacities of **other refineries** in our markets and globally"* as a driver of
its own margin. ★ **That risk factor is now being satisfied by PSX's own LA idling** — a US-domestic,
filed-not-reported instance of the bottleneck.

### `module_disclosure_us` — **exists and was run** (PSX, CVI). Result: **no order/contract/guidance
8-K in either name in 90 days.** No filing-level catalyst in window; the catalysts are all earnings (D7).

---

## §4 Value-chain map — 6 nodes, bottleneck marked
*(The 7-node map from 07-17 §4 is carried; this is the **corrected and compressed** version — the change
is that node 3 is now split into "throughput" vs "conversion", which is where the constraint actually binds.)*

```
[1 CRUDE SUPPLY]      [2 CRUDE LOGISTICS]   [3 ★★ CONVERSION      [4 PRODUCT LOGISTICS]  [5 END-USE / OFFTAKE]      [6 CO-PRODUCT
 not scarce            fee-based, insulated   CAPACITY —            terminals, jobbers,     the crack's COUNTERPARTY     SPILLOVERS]
 CL=F 81.78, IEA        (carried by ref.)     diesel-capable         export levies           — pays the $5.00/gal        cross-sector
 sees demand FALLING                          hydrocracking/coking]                                                     
 XOM CVX EOG COP        KMI WMB OKE TRGP      VLO MPC PSX DINO      (mostly unlisted;       DAL UAL LUV (jet)          CVI→UAN/ammonia
 OXY FANG DVN           LNG                   PBF DK PARR CVI        India levies 07-16)     FDX UPS (diesel)           → ag inputs
 ⚠ COUNTER-SIGN                               ↑ THE BOTTLENECK                               ⚠ COUNTER-SIGN             PSX→50% CPChem
 to the crack                                                                                to the crack               → petchem
        [ SERVICES layer, cross-cutting nodes 1–2: SLB 분산 RS60 −16.5% · HAL 분산 −13.2% · BKR — worst node, not part of the thesis ]
```

### ★ BOTTLENECK = node 3, **diesel-capable CONVERSION capacity** — binding constraint, re-tested
The 07-17 file called this correctly and it is **re-tested rather than inherited**, against the standard
that *strong demand is NOT a bottleneck*:
- **Crude is not the constraint.** CL=F 81.78 with WTI specs still **10%ile crowded-SHORT**; the IEA
  print in the window is *"Global oil demand set for **first annual drop** since the COVID-19 pandemic"*
  [euronews 07-10]. A barrel is available.
- **Demand is not the constraint** — and I checked the counterparty rather than assuming: UAL is eating a
  **$6B fuel headwind** and DAL/UAL/LUV still carry **RS60 +14.3 / +13.3 / +11.9%**. Demand is *paying*,
  which is what makes it a price, not a bottleneck.
- **Conversion capacity IS the constraint, and it now has FOUR independent sources — of which only two
  are war-dependent:**
  1. Russian refinery destruction — **3 strikes in 7 days, accelerating** (Syzran 07-12, Afipsky 07-14,
     Yanos 07-17); *"every one of Russia's largest refineries"* struck [ForeignPolicy 07-15]. ⚠ **war-dependent**
  2. Russia's diesel export ban — ⚠ **war-dependent AND dated: expires 2026-07-31**
  3. **India raising diesel/jet export levies** [Bloomberg 07-16] — policy withholding the marginal
     export barrel. ⚠ *partly* war-dependent
  4. ★ **US permanent closures — PSX idling its LA refinery, from PSX's own 10-K.** **NOT war-dependent,
     not reversible by a ceasefire, not expiring on 07-31.**
- **Physical confirmation:** *"middle distillate inventories… **15% lower than last year**"* [hellenic 07-17],
  while *"**Fujairah's fuel-oil inventories rise massively**"* — **the tightness is specific to the middle
  of the barrel, which is exactly the bottleneck's signature** and rules out a generic "oil is tight" read.

### Cross-sector chains marked
- **Node 3 → node 5 (INDU / DISC):** the crack is a *transfer*, not a creation. Airlines and freight are
  the short side. **Both sides of this chain are in one book — see §6.**
- **CVI's nitrogen segment → MATR/STPL ag-inputs**, which is exactly the leg PREMORTEM §1 logged as a
  WITHIN-RUN-WATCH (CTVA/CF/ADM). **The chain is real and it runs through a refiner's balance sheet.**
- **PSX's 50% CPChem → MATR petchem.** PSX's crack exposure is diluted by a MATR-sector asset — relevant
  to §6, since MATR is the run's hardest UW.

---

## §5 Chain-hop candidates — **NONE qualify this run. Stated, not padded.**

`module_news_data chain-hop refinery distillate --days 14 --scope foreign` (112 articles scanned):
- **★ CHAIN-HOP 후보 section returned EMPTY (zero candidates).**
- HEADLINE-NAMED returned **GOOGL 21 · GOOG 21 · NVDA 11 · META 7 · AAPL 3 · AMZN 5 · MU 5** — the
  identical mega-cap token-collision failure the 07-17 file logged. **Root cause now identified precisely:
  the FTS terms `crack` and `distillate` collide with AI vocabulary** — my own `fts` run surfaced
  *"China's use of model **distillation**"* [SCMP], *"Palantir CTO Warns AI **Distillation** Threat"*,
  *"Chinese firms allegedly **distill** those models"* [semafor]. **This is MACRO §5 failure-class 6
  (a contaminated bucket) inside a different tool.** Fix-forward for the next run: use
  `refinery diesel gasoil` — never `crack` or `distillate` — in any US chain-hop.
- The only genuine energy names it surfaced were **XOM (2 title / 3 body)** and **DAL (1 title / 2 body)** —
  both **headline-named, therefore disqualified as chain-hop candidates by the rule.**

**Manually-derived body-proximate candidates, cross-checked against flow before promotion (the rule):**

| Candidate | Why proposed | Flow cross-check | **Verdict** |
|---|---|---|---|
| **NEU** (NewMarket, fuel additives, $7.1B) | Node-3 consumable; textbook chain-hop profile: **OBV 매집, RS60 +14.4% while RS20 is only +0.6%** — accumulation without extension, exactly what the tool says to look for | ✅ flow qualifies | ❌ **REJECTED — fails the news bar.** `fts NewMarket Innospec lubricant --days 14` returned **15 hits, ZERO about NEU** (the one "Newmarket" hit is a **horse race** [upi 07-13]). **A flow signal with no body-proximate co-mention is not a chain-hop candidate — it is a screen artifact.** Logged so the next run does not re-discover it as new. |
| **IOSP** (Innospec, $2.1B) | Same node | **분산, vol 0.65×** | ❌ Rejected on flow *and* news |
| **APD / LIN** (refinery hydrogen) | Node-3 input | APD 중립 RS60 −5.3%, LIN 분산 | ❌ Rejected on flow |
| **ALB / HON** (catalysts / UOP licensing) | Node-3 input | **ALB 🔴분산 RS20 −27.8% / RS60 −44.7%**; HON 매집 but **RS20 −6.5%, vol 0.58×** | ❌ Rejected on flow |
| **UPS** ($100.1B) | Node-5 diesel counterparty | **매집, RS20 +11.7%** | ⚪ Logged only — it is the *counterparty*, i.e. the crack-KILL side, not a chain-hop of the thesis. Belongs to §6's kill lane, not here |

> **Honest result: this run produces ZERO promoted chain-hop candidates.** Every proposed name failed
> either flow or the ≥2× body-proximity bar. **Nothing is padded into BET.** The value-chain adjacency
> for this cycle appears genuinely empty at US-listed scale — which is a *finding* (the crack is a spread,
> and a spread has no supply chain of its own), not a search failure.

---

## §6 ★ VERDICT

### A. The mandated question: **which expression survives BOTH kill switches?**

**First, the honest structural answer: no single long refiner survives both, and the file must say so.**
- Kill switch 1 (**Hormuz**) is **two-sided, not one-signed** (D2). A crude-only escalation gap is
  crack-negative; a broad product shock is crack-positive. Both are on July's own tape. **There is no
  refiner expression that is long one branch and flat the other** — every one of the eight carries
  crude beta between +0.24 (DINO) and +0.48 (PBF) *and* crack beta between +0.20%/$ (PSX) and +0.58%/$ (PBF).
- Kill switch 2 (**the crack's own kill**) is **~1.3 adverse sessions away** ($83.57 vs $75; the 07-17
  move alone was −6.77) with a **hard date on 07-31** — and the KPI is at the **96th percentile of two
  years against a $31.70 median.**

**Given that, the surviving expression is defined by which name's P&L is LEAST conditional on both
switches resolving favorably. Measured, that is PSX — and the ranking is not close:**

| Criterion (all measured in this file) | PSX | VLO | MPC | DINO | PBF | CVI |
|---|---|---|---|---|---|---|
| ATRs above 50dma | **4.52 ← least of the majors** | 4.69 | 5.61 | 5.95 | 5.83 | 2.18* |
| **Detachment residual 07-17** | **+2.72pp** | +3.53 | **+2.05pp** | +2.58 | **+4.66** | **+5.76 ← worst** |
| Beta to Δcrack (per $1/bbl) | **+0.20% ← least conditional** | +0.32% | +0.22% | +0.27% | **+0.58% ← most** | +0.37% |
| Non-crack earnings segments | **4 of 5** (Midstream, CPChem 50%, M&S, Renewables) | 2 (renew. diesel, ethanol) | 1 (MPLX) | 1 (lubricants) | **0** | 2 (N-fert, renew.) |
| Short base state | **z −0.98, 5v5 −15.4▼** | −0.63 / −1.7▼ | +0.18 | **+0.37 / +4.6▲** | +0.94 / −2.5▼ | +0.49 |
| fwd PE | **11.5 ← cheapest large** | 13.9 | 12.4 | 10.8 | 10.6 | **20.2 ← dearest** |
| ★ **Prints relative to the 07-31 ban expiry** | **08-05 = AFTER** | **07-30 = 1 day BEFORE** | 08-04 AFTER | 07-28 BEFORE | 07-30 BEFORE | 07-30 BEFORE |

\* CVI's 2.18 ATRs is the one number that favors it, and §3 disqualifies the reason: 70% Icahn control,
29M float against 16.2% short interest, **fwd PE 20.2**, and three management-change 8-Ks in 90 days.
**CVI is cheap-looking on extension and expensive on everything else.**

> **★ ANSWER: PSX is the only expression that survives both kill switches with its thesis intact —
> and it survives them for a reason that is NOT "the crack stays high."** Four of its five segments
> are non-crack; its crack beta (+0.20%/$1) is the lowest measured; it is the least extended major; its
> shorts are exiting hardest (−15.4▼); it is the cheapest large refiner on forward (11.5); it detached
> least from its KPI on 07-17 outside MPC; **and it is the only large refiner that reports (08-05) into a
> world where the 07-31 export-ban question is already answered, rather than one day before it.**
> ⚠ **The cost of that survival is stated, not hidden: PSX has the least crack UPSIDE too.** It is the
> expression that survives, precisely because it participates least. **PBF is the inverse — maximum
> crack leverage (+0.58%/$1), zero non-crack segments, 5.83 ATRs, at its 52w high, the largest detachment
> residual outside CVI, and it is the name being sold to the retail bid as a "geopolitical hedge" [yahoo
> 07-17]. PBF is the run's trap candidate and this file confirms PREMORTEM's tag with numbers.**
>
> ★ **And the genuinely two-switch-proof expression is not a refiner at all — it is the SPREAD.**
> **DAL** ($55.4B, **fwd PE 9.5**, **OBV 매집**, **RS60 +14.3%**, **0.85 ATRs above its 50dma, −10.1% off
> its 52w high**) wins on the exact branch that kills every refiner: the crack collapsing back toward its
> $31.70 two-year median. It has outperformed **through** a +14.5% crude week while absorbing the $6B
> industry fuel headwind. **The desk is currently long node 3 and holds nothing at node 5, i.e. long one
> side of a transfer.** Naming this is analysis; **whether and how to hold both sides is BET's, and no
> sizing is expressed here.**

### B. The ROTATION §2a divergence — **EARLY or LATE? I commit: LATE.**

ROTATION asked: matrix ranks ENRG #1 OW, the sweep ranks it **6th by level** but **#1 by delta (+0.181,
~2× any other sector)**. ROTATION resolved the *arithmetic* (composition artifact — integrateds drag,
refiners carry) and deferred the *verdict*. **The verdict, with the decisive test:**

> **An early sector move BROADENS. This one NARROWS. That is the test, and it fails it.**

- The **entire** +0.181 delta is generated by **eight names that are all at 0.0% off their 52-week highs**.
  There is not one name in the complex that is *starting*. The other half of the sector is broken and
  getting worse: **XOM RS60 −6.2%, CVX 분산 −4.8%, EOG 분산, OXY −8.2%, SLB 분산 −16.5%, HAL 분산 −13.2%,
  KMI −3.3%, LNG −3.7%, XLE RS60 −2.3%.** A rank-6-by-level sector whose delta comes **entirely from names
  at all-time highs while its other half distributes** is a *narrowing* move, i.e. late-stage concentration.
- **The KPI is late on its own terms, and this is the number that settles it: the crack sits at the 96th
  percentile of two years, at 2.6× its $31.70 two-year median, having spent only 4% of two years above
  $75 — and it already topped, on 07-16.** Nothing about a 96th-percentile spread is early.
- **Positioning is late:** covering is exhausted in 7 of 8 names (5v5 negative); the only name where
  shorts are still adding (DINO +4.6▲) is the only 🟢가속 tag — the last un-squeezed name is the last
  one working.
- **The narrative is late:** the instrument is being retailed as a war hedge [yahoo 07-15, 07-17; CNBC
  07-16] at the moment its KPI rolled over, and D3 measures the resulting detachment at **+2.05 to +5.76pp
  in a single session**.

> **★ COMMITTED VERDICT: the MECHANISM is early-to-mid (destruction rate accelerating — 3 strikes in
> 7 days; inventories −15% y/y; and one leg, PSX's LA idling, is permanent and non-war-dependent).
> The INSTRUMENT is LATE. The ROTATION §2a divergence resolves LATE, and the level/delta pattern is the
> evidence for it, not against it.**
>
> **Consequence for the pipeline, stated plainly: "the mechanism is intact" is a true statement that
> does not license the instrument.** SWEEP's 🚨 GAP (rank-2 cycle, epicenter 0.0% vs an 8.0% floor) is
> real and this file does not soften it — but **the GAP is a statement about a missing core, and this
> file's finding is that the core must be established in the expression that survives both switches
> (PSX-like: low crack beta, non-crack segments, post-07-31 print), not in the expression with the most
> crack leverage (PBF-like).** **The floor can be satisfied correctly or incorrectly, and §8 exists
> because the registry currently permits the incorrect way.**

### C. On MACRO P3′ — the final ruling
P3′ said refining is *"the anti-fragile half of the OW."* **Half-right, and the half it got wrong is the
half it was written for.** Refining is **anti-fragile to a ceasefire** (correct, and the 07-17 DEEP proved
it from spread mechanics) and **fragile to a crude-only escalation gap** (missed, now measured at −6.77 on
07-17) — **and it is fragile to its own KPI's mean reversion regardless of Hormuz**, which is the risk
neither MACRO nor PREMORTEM sized. **P3′ should be rewritten as: "refining is short the crude/product
spread's volatility and long its level; the level is at the 96th percentile."**

---

## §7 Track KPIs + anti-signals — dated observables

| # | Observable | Reading now (asof 07-17) | Falsifier / trigger level | Date |
|---|---|---|---|---|
| 1 | ★ **Distillate crack** ($/bbl, `HO=F`×42 − `CL=F`) | **83.57**, topped **90.34 on 07-16** | **< $75 = the leg's own kill** (3.56σ, but 1.27× the 07-17 single-day move) | daily |
| 2 | ★ **Crack percentile (2y)** | **96th; 2y median $31.70; >75 on only 4% of 2y** | Return toward the median is the base case, not the tail | daily |
| 3 | ★ **Detachment: 2 consecutive sessions where the crack falls and PBF/VLO still rise** | **07-17 = day 1** (residuals +4.66 / +3.53pp) | **Day 2 = the equity has decoupled from its KPI → treat as narrative-priced** | 07-20 |
| 4 | ★ **Russian diesel export ban** | in force | **Not renewed / lifted on 2026-07-31 = hard dated kill.** Commerzbank already models the lift [FXStreet 07-17]; *"refineries will eventually return, BRS said"* | **07-31** |
| 5 | **Russian refinery strike rate** | **3 in 7 days, accelerating** (Syzran 07-12 · Afipsky 07-14 · Yanos 07-17) | A 14-day gap with no new named strike = mechanism decelerating | rolling |
| 6 | **Middle-distillate inventories** | **−15% y/y** [hellenic 07-17]; Fujairah **fuel oil** rising | Distillate stocks rebuilding toward y/y flat | weekly |
| 7 | **US retail diesel** | **$5.00/gal, +33% since the war began** [NYT/Bloomberg 07-16] | Sustained move back under $4.50 | weekly |
| 8 | **Hormuz / ceasefire denominator** | `ceasefire\|truce\|Hormuz\|negotiations` **333 hits/3d**; ★ **a ceasefire framework EXISTS and was "suspended" 07-18** [businessinsider] | ≥5-outlet "strait open"/ceasefire **or** an IEA/SPR release headline. Confirm with **CL=F < 78.69** | undated, LIVE |
| 9 | **Extension** | **7 of 8 refiners at 0.0% off 52w highs; 4.5–6.0 ATRs over 50dma** | First close back below the 50dma (VLO ≈ 258) | daily |
| 10 | **Short fuel** | Covering exhausted (PSX **−15.4▼**, 6 others negative); ⚠ short-of-float still **PBF 15.9% / CVI 16.2%** | **DINO's +4.6▲ flipping to covering = the last fuel spent** | daily |
| 11 | **Earnings — the dated confirm/deny** | **KMI 07-23 ✓ (date resolved)** · **DINO 07-28** · **VLO / PBF / CVI 07-30 (1 day pre-expiry)** · **MPC 08-04** · **PSX / PARR / DK 08-05 (post-expiry)** | Q3 crack guidance on the calls; a *"cracks normalizing"* guide kills the leg from the inside | dated |
| 12 | **Counterparty (node 5)** | **DAL RS60 +14.3% 매집 · UAL +13.3% · LUV +11.9%**, through a **$6B** UAL fuel headwind | Airlines rolling over = the crack is finally destroying demand → a *different*, worse regime for everyone | daily |

**Anti-signals, ranked by proximity:**
1. ★ **The crack's own mean reversion, unconditional on any headline.** 96th %ile, median $31.70, already
   topped. **This is closer than either named kill switch and neither MACRO nor PREMORTEM priced it.**
2. ★ **Detachment day 2** (KPI 3). One more session of crack-down/equity-up converts this from a
   fundamentals trade into a positioning trade.
3. **07-31 export-ban expiry**, with **three of the eight names printing earnings the day before it.**
4. **PBF/CVI specifically:** highest crack beta / largest residual / dearest forward multiple / smallest
   float — the trap layer, named with numbers.
5. **MPC vol 0.90×** on a +36.3% RS60 — new highs on falling volume, the group's weakest hand (carried
   from PREMORTEM §3 and re-measured today).
6. **DINO shorts adding (+4.6▲)** into the only 🟢가속 tag.
7. **Carried by reference:** LNG short-vol **z +3.09** (07-17 §6) — unresolved, on a held book position.

---

## §8 ★ Recommended registry epicenter correction — **recommendation only, file NOT edited**

**Current** `data/cycles/cycle_registry.json:22`:
`"epicenter": ["MPC","PSX","VLO","XOM","CVX","EOG","FRO","STNG","INSW","DHT"]`

**Diagnosis — the list does not encode the cycle its own name describes** (*"Energy / oil-refining
(Hormuz + Russia crack)"*):
- **3 of 10 are refiners.**
- **XOM · CVX · EOG are COUNTER-SIGN, not merely weak.** They monetize the crude price; the cycle's
  engine is the crude/product *spread*. **On 07-17 the crack fell −6.77 while crude rose +3.6% — that is
  the day XOM's exposure and VLO's exposure pointed in opposite directions.** Measured: XOM 중립 RS60
  **−6.2%**, CVX **분산** RS60 −4.8%, EOG **분산**. ⚠ **The live consequence: the 8.0% floor is
  satisfiable today by buying XOM and CVX, and `cycle_exposure.py` would print ✅ on a book holding 0%
  of the crack.** That is the exact failure the 07-17 fix was supposed to close, one level deeper.
- **FRO · STNG · INSW · DHT are dead twice over** — the 07-17 DEEP found no breakout in a direct price
  pull, and EVENT_ALPHA Card 2 killed them as **STORY-ONLY** (all 분산, vol 0.58–0.74×). Keeping them
  lets a tanker headline satisfy a refining floor.
- **The actual movers are absent entirely: PBF +65.8% · PARR +49.6% · DK +49.1% · DINO +34.1% (the only
  🟢가속) · CVI +26.6%** — all OBV 매집-or-중립, all RS60 positive.

### Recommended replacement

```json
"epicenter": ["PSX","VLO","MPC","DINO","PBF","DK","PARR","CVI"],
"adjacent":  ["LNG","KMI","WMB","OKE"],
"counter_sign": ["XOM","CVX","EOG","DAL","UAL","LUV"],
"core_pick": "PSX"
```

| Action | Names | Reasoning (measured in this file) |
|---|---|---|
| **KEEP in epicenter** | PSX · VLO · MPC | Crack is the primary earnings driver; all 매집; RS60 +24.2 / +27.1 / +36.3% |
| **ADD to epicenter** | **DINO · PBF · DK · PARR · CVI** | All five have refining conversion as the **primary** earnings driver (§3 for CVI; 10-K-verified for DINO on 07-17). All ≥$3.5B mcap. All 매집-or-중립, all RS60 positive (+7.0 → +62.1). **These five ARE the cycle's price action and the registry cannot see any of them.** ⚠ **PARR/DK/CVI/PBF sit below `us_top300`, so `chain-hop` and `sector_flow` will never propose them — this list must be human-maintained, and that limitation belongs in the `_note`** |
| **REMOVE from epicenter → new `counter_sign` bucket** | **XOM · CVX · EOG** | **Do not delete — relabel.** They are the cycle's *internal hedge* (they win on the crude-up/crack-down branch that hurts node 3). Deleting loses that information; leaving them in epicenter lets the guard pass on the wrong exposure. **A `counter_sign` bucket must never count toward `min_epicenter_pct`.** |
| **ADD to `counter_sign`** | **DAL · UAL · LUV** | ★ Node 5, the crack's counterparty (§4). They win on exactly the branch that kills the epicenter (**DAL fwd PE 9.5, 매집, RS60 +14.3%, only 0.85 ATRs over its 50dma**). Registering them makes the cycle's two-sidedness machine-visible instead of prose-only |
| **DELETE entirely** | **FRO · STNG · INSW · DHT** | Killed independently by two stages; all 분산; not refining exposure under any branch |
| **KEEP `adjacent`, but annotate** | LNG · KMI · WMB · OKE | Correct as *adjacent*. ⚠ Annotate: **zero crack participation, verified from the 10-Ks on 07-17** — this is the "$1,886 double-counted as 23.87% any-layer" defect PREMORTEM §4.3 found; the note should live in the registry so the renderer's number stops being read as participation |
| **`core_pick`: keep PSX**, update `core_pick_why` | | The 07-17 rationale (cheapest large refiner, shorts exiting) **survives re-measurement and strengthens**: fwd PE **11.5** (still cheapest large), short-vol **5v5 −15.4▼** (still the largest covering print), **4.52 ATRs = least-extended major**, **crack beta +0.20%/$1 = least conditional**, **4 of 5 segments non-crack**, **prints 08-05 = after the 07-31 kill date.** Add the §6 caveat verbatim: *it survives because it participates least* |

⚠ **One defect this file can NOT fix and must escalate as-is:** even a corrected list satisfies a
percentage floor, and **§6·B's verdict is that the correct core and the extended chase are the same
tickers at different prices.** A registry floor cannot encode "establish, don't chase." **Recommend
adding a free-text `entry_note` field to the cycle record** carrying KPI 3 (the detachment-day-2 test)
and the **07-31** date, so the guard's ✅ is read alongside its timing caveat rather than instead of it.

---

**EXIT CHECK:** ✅ **Continuous-track discipline** — led with §0 DELTA (6 deltas incl. a reversal I
reproduced from raw data and a **correction to PREMORTEM's own generalization**), and the unchanged
structure carried **BY REFERENCE** in 5 numbered items (7-node map, KMI/LNG filings, integrated/E&P split,
LNG short-z, dead tankers), **not re-printed** · ✅ **Flow measured today** (`module_flow`, `us_flow.py`
FINRA, yfinance ATR) with the **short-z × narrative divergence stated explicitly** (covering exhausted in
7 of 8 vs a mechanism still accelerating) · ✅ **§2 Players = large-cap UNION thematic small-caps**,
bounded (≥2× named · real ticker · mcap ≥$2B) — **PBF and CVI promoted after failing the bar on 07-17;
PARR added for the first time**; the `us_top300` tool floor named as the reason the union is required ·
✅ **§3 IR anchor from primary EDGAR text** — **new** PSX 10-K work (5 segments + **the LA refinery idling**,
the only non-war bottleneck source in the file) and CVI 10-K (3 segments, RDU reversion, 70% Icahn),
plus `module_disclosure_us` **run on both** (exists; no order/guidance 8-K in 90d) · ✅ **§4 6-node map,
bottleneck marked and RE-TESTED** (crude not scarce — IEA sees demand *falling*; demand is paying, not
constraining; conversion capacity binds, **4 sources of which only 2 are war-dependent**), **3 cross-sector
chains marked** · ✅ **§5 chain-hop — ZERO candidates promoted, and not padded**; NEU rejected on the news
bar despite a qualifying flow profile (the "Newmarket" hit is a horse race); **the `crack`/`distillate` ×
AI-distillation token collision identified as the tool's root cause with a fix-forward** · ✅ **§6 VERDICT
committed** — the surviving expression (**PSX**, on 7 measured criteria, with its cost stated) and the
ROTATION §2a divergence **committed as LATE** on the broadening-vs-narrowing test + the 96th-percentile
KPI · ✅ **§7 12 dated observables + 7 ranked anti-signals**, incl. the one neither prior stage priced
(unconditional mean reversion) · ✅ **§8 concrete epicenter recommendation with per-name reasoning,
`counter_sign` bucket proposed, file NOT edited** · ✅ **Zero buy/sell calls, zero sizing.**
