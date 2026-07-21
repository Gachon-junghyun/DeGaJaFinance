# MACRO_REPORT — US Industry Desk — Phase 0 (2026-07-14)

> English-only. Sources: FRED (`module_macro_us`, primary `[FRED]`), `news_alert.db` foreign slice (FTS body-inclusive + blindspot `[news]`), US daily anchor `LLM_create_us_2026-07-13` + general `LLM_create_2026-07-14` (`[daily]`), live `[WebSearch]` (oil/Hormuz, 07-14). Analytical artifact — ZERO buy/sell calls. Tilts express *influence*, not advice.

---

## §A — FRED PRIMARIES (the numbers downstream desks cite)

| Series | Latest | ~1mo ago | 120d ago | Read |
|---|---|---|---|---|
| Fed Funds eff. (DFF) | **3.62%** (07-10) | 3.63 | 3.64 | On hold ~8 mo. Warsh Fed: **delayed cuts, hawkish** — no cut delivered. [FRED][news] |
| 2y UST (DGS2) | **4.21%** (07-10) | 4.13 | 3.46 | **+75bp/120d, +8bp/mo — front-end pricing hikes/higher-for-longer, not cuts.** [FRED] |
| 10y UST (DGS10) | **4.56%** (07-10) | 4.53 | 4.14 | +42bp/120d — grinding up, real-rate-led. [FRED] |
| 2s10s curve | **+0.35pp** | +0.40 | +0.68 | Positive, flattening slightly; not inverted. [FRED] |
| Real 10y (DFII10) | **2.32%** (07-10) | 2.20 | 1.91 | **+41bp/120d — restrictive & rising; the rate that bites duration.** [FRED] |
| Core CPI (CPILFESL) | 336.121 (May) | — | — | **~+2.8% ann** — core still contained. [FRED] |
| Headline CPI (CPIAUCSL) | 333.979 (May) | — | — | **Reaccelerating; news flags CPI 3.8% "highest since May-2023"** — headline > core, tariff+energy driven. [FRED][news] |
| Unemployment (UNRATE) | **4.2%** (Jun) | 4.1 | 4.1 | Ticking up; softening-not-cracking — no dovish escape hatch yet. [FRED] |
| Broad Dollar (DTWEXBGS) | **120.50** (07-10) | 119.96 | 119.47 | **King Dollar firm near highs, +0.5%/mo — oil shock + hawkish = "good for USD, bad for bonds."** [FRED] |
| VIX (VIXCLS) | **15.03** (07-10) | 19.44 | 13.60 | ⚠️ **STALE-LOW: this print PREDATES the 07-12→14 Hormuz re-escalation.** Live tape is risk-off; treat calm as expired. [FRED] |
| M2 (M2SL) | **$23,052B** (May) | — | — | Liquidity still expanding — keeps drawdowns rotational, not systemic. [FRED] |

**Live commodity/geo overlay (07-14, `[WebSearch]` CNBC):** WTI **~$80.75** (+3.3% today, after Brent +9.6% the prior session; Brent ~$87). **Trump reinstating the Iran-port blockade + a 20% Hormuz transit toll** — ~1/5 of global oil transits Hormuz. This is a **policy-driven, structural** supply shock, not a one-off spike. Gold *fell* on the shock (priced as inflation, not fear).

### One-paragraph regime read
The Warsh Fed holds at **3.62%** with a hawkish, cut-delaying posture while the front end keeps lifting (**2y 4.21%, +75bp/120d**) and **real-10y 2.32%** stays restrictive-and-rising — the rate that actually bites long-duration. Headline CPI is **reaccelerating (~3.8%, highest since May-2023)** above a contained ~2.8% core; the driver mix has shifted from the AI-memory channel toward **energy**, because the **Hormuz/Iran conflict re-escalated (07-12→14): Trump reinstated the Iran blockade + a 20% strait toll and WTI jumped to ~$80.75**. The macro epicenter today is Hormuz, and — critically — the shock transmits through the **inflation/hawkish channel, not the safe-haven channel**: dollar firm (broad 120.5), gold *down*, bonds sold, rate-hike bets up (BNY: "the core macro channel — keep duration light, trim crowded AI/semi beta"). Labor is firm-but-softening (U 4.2%), M2 +liquidity keeps it rotational. **VIX 15.0 is a stale pre-weekend print** — the live tape is sharply risk-off (SK Hynix ADR record −15%, semis slaughtered on price). Net: a **higher-for-longer, tariff+oil-reflation regime** — punishing to duration/growth-multiple/rate-sensitives, supportive to **energy (esp. refiners), financials, critical-minerals/defense reshoring, and AI-power real-cash-flow** that spends regardless of the front end. The standout divergence (F27): **AI-compute *fundamentals* are thickening even as *price* is macro-slaughtered** — TSMC Q2 +36%/+68%, HBM diverting memory from consumer chips, smartphone shipments 13-yr low.

**Known primary gap:** HY/IG OAS credit spread not in FRED catalog — proxied by VIX (stale) + idiosyncratic credit headlines. Track as `[R6-K-credit — n/a]`.

---

## §B — BLIND-SPOT PASS (Step B+, mandatory)
`news_blindspot.py` · 14d · foreign · sample 500 · **coverage 18.3%** (query-limited to 16 OR-terms vs full §2.1 ~100; not a true miss-rate), blind_pool 17,664 of 21,608.
- **Emergent top ranks** — "AI"(1634, ticker/topic noise), Trump(450), Earnings(372), **SpaceX(370, already bucketed SPCX)**, Meta/Tesla/Apple/Nvidia/Microsoft (single-name mega-cap, bucketed under AI capex), Billion, **Iran(318, bucketed)**, Energy(253), Hong Kong(211, SCMP geo-cluster). **No absent macro theme; nothing demanding a mandatory body-read.** The sample row-read surfaced only earnings/dividend/single-name boilerplate + extensions of existing buckets (rare-earth, nuclear, oil already covered by the FTS pass).
- **§2.1 term-set delta this run: none required.** Iran/Hormuz, rare earth, export control, SpaceX, AI capex, nuclear/SMR are all already in §2.1 (added over the 06-27→07-07 calibration runs). Term set remains sufficient.

---

## §C — PROPOSITIONS (falsifiable, source-anchored) + ★ TRANSMISSION MATRIX

**M-01 — Rates/Policy: the Warsh Fed's next move is a hawkish-hold or hike, not a cut — and the oil shock *locks it in*.** *(confidence: [verified])*
- anchor: fed funds **3.62%** unmoved (07-10); **2y 4.21% (+75bp/120d)**, real-10y 2.32% rising [FRED]; news "Warsh era starts with cautious stance and delayed cuts," "higher-for-longer despite softer core" [news]; the Hormuz oil shock raises the inflation path, removing any near-term cut room [daily 07-13].
- prob: base 58% hawkish-hold / 27% hike-by-Q1-27 / 15% cut-on-labor-break.
- anti-signal: a benign core-PCE **and** a sub-50K NFP that pulls 2y <4.00% (front-end capitulates); oil rolling back <$65. [R5v4-F35-regimeflip]
- KPI: 2y UST, real-10y, Sept hike-odds. catalyst: Warsh Hill testimony + this week's CPI print.
- → **OW FIN** (NIM/curve) · **UW REAL, COND** (rate-sensitive duration) · **UW high-multiple growth** (discount-rate duration).

**M-02 — Inflation: headline stays hot ABOVE core — driver mix rotating from memory to ENERGY.** *(confidence: [verified])*
- anchor: headline CPI ~3.8% "highest since May-2023" vs ~2.8% core [FRED][news]; tariffs ≈10.9% of headline PCE [news]; now **WTI ~$80.75 + Hormuz blockade/toll** stacks an energy leg on top of tariffs [WebSearch 07-14].
- prob: base 62% sticky 3.5–4.5% / 26% re-accel >4.5% (if oil sticks >$85) / 12% cools <3.5%.
- anti-signal: Hormuz de-escalates and WTI rolls <$70 **and** the headline-core gap narrows two prints. [R5v4-F13-costpush]
- KPI: CPI MoM, WTI/Brent, DRAM/HBM contract px. catalyst: this week's CPI; Hormuz status.
- → **OW ENRG** (the inflation IS their revenue — esp. refiners/crack spreads) · **UW CONS** (input pass-through lag) · supports M-01.

**M-03 — Geopolitics: the Hormuz oil-supply premium has RE-INFLATED into a structural (policy-driven) regime.** *(confidence: [verified], reverses the 06-30 "premium stayed deflated" call — see §E)*
- anchor: **Trump reinstated the Iran-port blockade + 20% Hormuz transit toll (07-14)**; Brent +9.6% then WTI +3.3% to ~$80.75; ~1/5 of global oil transits Hormuz [WebSearch]; daily desk names Hormuz "the core macro channel," oil +10% intraday, KRW to 1500s, SK Hynix ADR record −15% [daily 07-13/07-14].
- prob: base 55% premium persists (regime, 2–8 wks) / 30% one-off spike cools (semi rebounds on fundamentals) / 15% rapid de-escalation.
- anti-signal: a ceasefire/toll-suspension headline + WTI back <$70 within days (the premium is policy-reversible — this is the fastest-moving proposition).
- KPI: WTI/Brent, tanker-transit headlines, VIX (expect it to catch up from 15). catalyst: any Iran/US diplomacy or fresh strike.
- → **OW ENRG (refiners, integrated, E&P)** · **OW INDU-defense** (geopolitics realized — but "sold-the-news" near-term; tactical not immediate) · **UW crowded IT/semi beta** (risk-off + FX + duration) · mild **OW aerospace/airlines paradox** watch.

**M-04 — Structural: US-China rare-earth clash 2.0 forces a critical-minerals/defense-reshoring capex cycle.** *(confidence: [verified])*
- anchor: "US-China rare earth clash 2.0," China widening export curbs to Japan/allies (drones, nuclear, defense firms) [news scmp/cnbc]; **Pentagon $25M into ReElement, US Army contracting critical-minerals processing at military bases**; MP Materials & USA Rare Earth bid on China's ban; **$17.5B US nuclear-comeback package** [news].
- prob: base 60% multi-quarter reshoring capex / 25% accelerates (fresh China curb) / 15% truce cools it.
- anti-signal: a durable US-China rare-earth truce with verified export resumption. [R5v4-F-structural-reshoring]
- KPI: MP/USA-Rare-Earth flow, DoD/DOE award headlines, China export-license data.
- → **OW MATR** (critical minerals/rare earth) · **OW INDU-defense** (supply-chain reshoring) · nuclear policy-tailwind but pure-play SMRs valuation-reset (see M-05).

**M-05 — Power/Nuclear: AI-power demand is real and policy-backed, but pure-play SMRs are in a valuation reset — barbell it.** *(confidence: [verified])*
- anchor: **$17.5B US nuclear package**, S.Korea-US-Japan SMR export alliance, DOE backing [news]; BUT NuScale −75–83%/12mo, Oklo −27% dilution "pre-revenue," Eaton DC growth "consistent, not explosive" [news][daily 07-13]; **Constellation cheap at 21x with 20-yr Meta/Walmart PPAs** = the funded/cash-flow leg [daily 07-13].
- prob: base 55% funded-cash-flow power holds / pure-play SMR stays volatile / 30% policy re-rates the whole complex / 15% rising-real-yield headwind caps bond-proxy utilities.
- anti-signal: real-10y >2.6% (utility bond-proxy leg breaks) OR an SMR pure-play delivering revenue/first-power.
- KPI: real-10y, PPA-signing headlines, SMR cash-burn/dilution.
- → **OW UTIL-with-AI-demand** (CEG-type PPA cash flow) · **UW UTIL bond-proxy** (real-yield headwind) · **OW INDU electrical-equipment** (datacenter power, selective).

### ★ TRANSMISSION MATRIX (Phase-0 deliverable → STAGE-02 input)

| GICS Sector | Tilt | Driver (which proposition) |
|---|---|---|
| **Energy (ENRG)** | **OW+ (top)** | M-02/M-03 oil shock + Hormuz blockade; refiners/crack spreads the sharpest leg |
| **Financials (FIN)** | **OW** | M-01 higher-for-longer, positive curve, firm dollar → NIM |
| **Materials (MATR)** | **OW (selective)** | M-04 rare-earth/critical-minerals reshoring (MP, USA Rare Earth); gold *not* the clean hedge here |
| **Industrials (INDU)** | **OW (barbell)** | M-03/M-04 defense (geopolitics realized, but sold-the-news near-term) + M-05 electrical equipment for DC power |
| **Utilities (UTIL)** | **Neutral→OW (barbell)** | M-05 AI-power PPA cash flow OW / bond-proxy UW on real-yield |
| **Info Tech (IT)** | **Neutral / tactical UW** | M-03 crowded semi beta risk-off + M-01 duration headwind; BUT F27 divergence — funda thick, price slaughtered → funded compute holds, high-multiple UW |
| **Comm Services (COMM)** | **Neutral** | Mega-cap ad resilient but crowded; duration-sensitive |
| **Health Care (HLTH)** | **Neutral (mild OW defensive)** | Under-owned defensive; policy risk |
| **Cons. Staples (CONS)** | **Neutral / mild UW** | M-02 tariff+oil input pass-through lag |
| **Cons. Discretionary (COND)** | **UW** | M-01 higher-for-longer + oil tax on consumer + affordability strain |
| **Real Estate (REAL)** | **UW (bottom)** | M-01/M-05 real-10y 2.32% rising = direct rate-sensitive headwind |

**§2.5 reality corrections applied:** (1) VIX 15.0 is a *stale pre-weekend* print — do NOT read calm; the live tape is risk-off. (2) Gold *fell* on the geopolitical shock (inflation-channel, not fear-channel) → gold is **not** the clean hedge; energy is. (3) Defense = geopolitics realized but broad risk-off ate the hedge bid ("gap-up-then-fade" / sold-the-news) → tactical, not immediate. (4) Semi: **price ≠ fundamentals** (F27 divergence) — the drawdown is macro/FX/positioning, not demand destruction; don't confuse the two.

---

## §E — SELF-BACKTEST (prior MACRO_REPORTs scored)

**+7d — 2026-07-07 report:**
- M-01 (rates resolve hawkish-hold/hike, not cut): **HIT** — fed funds still 3.62%, 2y rose to 4.21%, Warsh delayed-cuts confirmed.
- M-02 (headline CPI sticky > core, memory/goods channel): **HIT** on headline>core persisting; driver mix has since rotated toward energy (partial evolution, not miss).
- → **2/2 HIT.**

**+14d — 2026-06-30 report:**
- M-01 (Fed done cutting, next move a hike): **HIT** — on hold 3.62%, front-end elevated.
- M-02 (inflation reaccelerating, energy + AI-component): **STRONG HIT** — the *energy* leg was prescient; headline now oil-driven.
- M-03 (labor firm enough): **HIT** — U 4.2%, no crack.
- M-04 (strong-dollar persists): **HIT** — broad dollar 120.5, firm near highs.
- M-05 (oil premium deflated and *stayed* deflated; "the Strait is open"): **❌ MISS / REVERSED within 14d** — Hormuz re-closed (Trump blockade + 20% toll), WTI to $80+. **Lesson logged:** the geopolitical oil premium is *regime-switching*, not a stable deflation — today's M-03 explicitly reverses it and today's VIX-stale correction stems from this miss.
- → **4/5 HIT.**

**Running visible hit-rate: 6/7 (86%).** The single miss (oil-premium stability) is the highest-conviction lesson feeding today's report: geopolitical premiums re-inflate fast and policy-driven; never bank a deflation as durable.

---

## 🚨 ADDENDUM — intraday update (2026-07-14, post-run · CPI print + Hormuz deep-dig + real-alpha overlay)
> Appended after the main run per the STAGE-05 drift-watch rule (never clobber). Two regime bursts landed after MACRO_REPORT mtime: the June CPI print (08:30 ET) and a confirmed Hormuz re-escalation. Both partially revise the main run's tilts.

### A) June CPI printed COOLER than expected — a partial anti-signal to M-01
- **Headline 3.5% YoY** (vs 3.8% exp, from 4.2% May), MoM **−0.4%** (gasoline −9.7%). **Core 2.6% YoY, MoM 0.0% FLAT** (vs 2.9%/+0.2% exp) — the genuinely dovish leg (energy-independent) [WebSearch CNBC/CBS/BLS].
- **Impact:** direct anti-signal to **M-01 (hawkish-hold/hike)** — 2y should ease, cut-odds rise, real-yield headwind relaxes. This RELIEVES the names the main run had UW purely on yields (long-duration growth/semi, rate-sensitive utility bond-proxy) and softens (not breaks) the FIN "higher-for-longer NIM" thesis (a bull-steepener is still fine for bank NIM).
- **★The trap (why M-02/M-03 still stand):** this is **June, backward-looking, gasoline-driven**. It's now mid-July with WTI ~$80 on the Hormuz blockade → the **July CPI (mid-Aug) re-accelerates on oil pass-through.** The disinflation trade has a ~4-week shelf life. **M-02 (headline sticky via energy) and M-03 (Hormuz premium structural) are UNCHANGED.**

### B) Hormuz re-escalation CONFIRMED structural — M-03 strengthened
Deep-dig (07-14) findings, all corroborating M-03:
- **Strait effectively closed Day 135** — tanker transits **~13/day** (vs ~88 baseline), 443 vessels anchored. Fresh 07-14 strikes: 2 Emirati tankers (cruise missile, casualties) + US struck Bandar Abbas (5 explosions), Bushehr, Jask, Abu Musa (3rd wave, 140 targets); Iran retaliated on Gulf bases [straits.live, CNN, Al Jazeera].
- **★SPR at 319.5M bbl — −23% pre-war, LOWEST since 1983.** The US downside-cap on oil is nearly spent → structural floor under the oil/refiner trade [CNN].
- **War-risk insurance ~30× premium** ($5–7.5M/transit vs $150–225K); **VLCC TD3C $296K/day (>2× pre-crisis)** [Lloyd's List].
- **Refining margins still at RECORD** — US 3-2-1 $64.58 (07-08), European diesel >$60, gasoline +$41/4-yr high; refiner 6mo: MPC +60%, VLO +51%, PSX +33% [IndexBox].
- **Iran Kharg (90% of exports, mostly China) disrupted → Asia crude imports −22% YoY (2016 low)** = record alt-barrel premiums keeping cracks bid.
- **Analyst asymmetry:** Goldman "closure +1mo → Brent $120 Q3/$115 Q4; through-2027 → $130+"; base/ceasefire → $80 (JPM Q4 $80). **Current ~$86 not yet pricing full disruption** = two-way optionality remains.
- **Kill-switch (M-03 anti-signal) refined:** the de-escalation tail is **alive** (Trump declared the June MoU "over" 07-08, but Qatar-mediated talks continue). The earliest warnings are **war-risk premium + diesel crack rolling over** — NOT news headlines. Ceasefire → $80 snapback.

### C) Real-alpha forensic overlay (13 US company reports read) — "REAL but mostly PRICED"
Cross-referencing the real-alpha desk verdicts against the BET_SHEET:
- **Only 4 are REAL-and-not-priced-out: NVDA, META, VST, TLN.** The other 9 (CEG, MU, AMD, GEV, EOG, GD, KMI, LNG, ANET) are **REAL_BUT_PRICED** = buy-the-dip, don't chase.
- **Compute re-rank: NVDA ↑ over ANET ↓.** ANET = REAL_BUT_PRICED (fwd 50x, target +5%, buyback $0, entry only on pullback to ~163); NVDA = REAL ("market pressed it as risk, core under-rated," stop 192.53). For the cool-CPI relief bounce, NVDA is the better risk/reward — but flow is 🟡 reactive → gate on opening-range hold.
- **Energy caveat:** the big-cap energy real-alpha names (EOG/KMI/LNG) are all "priced/below-trigger." **★CORRECTION (a PSX real-alpha report DOES exist, 2026-07-14 — an earlier ADDENDUM claim of "no report" was wrong):** PSX verdict = **REAL_BUT_PRICED / "눌림 대기 목록행"** — price already ABOVE analyst target ($198), RSI 82, 3m +27% rally prices the Q2 +193% consensus, next-yr EPS is negative-growth (market prices mean-reversion). The "cheap 11x" framing is the report's flagged "windfall × run-rate" trap. **★TACO amplifier:** PSX short-term debt exploded $1.0B→$8.4B (all ≤1yr, variable 29%), Q1 returns 100% debt-financed — the report's #1 risk is "war-premium unwind × short-debt rollover," so PSX is MORE TACO-fragile, not resilient (corrects the earlier "PSX TACO-resilient" claim). Report favors **MPC** as the quality refiner (PSX worst-in-class $1.15/bbl vs MPC $1.79 vs VLO $6.89). → PSX = momentum-only 2wk scalp with hard stop, NOT a "cheap clean lead"; the clean entry is the pullback.
- **★TLN divergence flagged:** real-alpha (07-11) says REAL/cheap-13x/asymmetric; flow (07-13) says crowded-extreme (76% short-vol). Prefer VST for the clean AI-power REAL.

### D) New actionable vehicles surfaced (same theme, different risk) — for the watchlist, not the DEEP set
- **Tanker pure-plays (FRO/STNG/INSW/DHT/EURN)** — highest-beta pure Hormuz-disruption bet (TD3C 2×, war-risk 30×); ⚠️ fastest to unwind on ceasefire (Lloyd's flagged some MEG rates as "imaginary").
- **Missile defense (RTX/LMT)** — Iran hitting bases → RTX $35B THAAD (4× production) + Stinger 2×, LMT $4.8B PAC-3; US defense $1T→$1.5T. Structural replenishment real; near-term "sold-the-news" on broad risk-off.
- **Cheniere (LNG)** — Qatari LNG carrier struck 07-07; Europe 12–14% LNG via Hormuz → US LNG alt-supply premium (overlaps the gas-to-power leg).

**Net regime revision:** cool CPI eases the RATES leg (relief for growth/semi UW, softer FIN NIM) but is backward/gasoline-driven with a July oil-reversal coming; the **oil/refiner leg (M-02/M-03) is strengthened, not weakened** (SPR floor, record cracks, $120 upside path). Barbell stands: **oil-wins (refiners/tankers) + rates-win (compute/NVDA)** — one side pays in every outcome. Daily kill-switch = **war-risk premium + diesel crack.**

### E) ★ TACO risk — the Trump-pivot de-escalation scenario (M-03's real downside, NOT a tail)
"TACO" (Trump Always Chickens Out): a sudden Trump→Iran de-escalation that collapses the oil premium. **This is a live ~30–40% scenario over the 2-week window, not a tail** — it corrects this desk's escalation tilt and mirrors the 2026-06-30 self-backtest MISS (that oil-deflation call was reversed by exactly this dynamic).
- **Base rate (it already happened this cycle):** Feb-28 strike → Apr blockade → **Jun 17–18 MoU/ceasefire/"Strait reopens" (a full Trump pivot to a deal)** → Jul-08 "ceasefire over" → re-escalation. One complete escalate→deal→re-escalate loop in ~4 months = manic on/off, not one-way. The June MoU is the TACO instance (it's what made Goldman cut forecasts / "Strait open" upgrades appear as stale search results).
- **Why the pivot incentive is unusually loaded NOW:** (1) oil/gas is Trump's political kryptonite — $86 oil reverses the very cool-CPI win he wants (CNN: "playing with economic fire"); (2) **SPR at 1983-low → diplomacy is the only remaining lever to cap gas prices** → structurally pushes toward a deal; (3) Qatar-mediated talks actively continuing; (4) a "made peace, oil crashes, gas cheap" outcome is a politically ideal Trump win.
- **Trade construction implication:** doesn't kill the (currently escalating) oil trade but demands **survive-the-gap** design. A ceasefire tweet gaps oil $86→$80 overnight → refiners/tankers gap DOWN through stops (gap risk = the stop may not fill at level). **Tankers (FRO/STNG) are the WORST TACO exposure** (highest beta, "imaginary" MEG rates, fastest unwind, −15–20% overnight possible). **PSX is more TACO-resilient** — the Russia diesel-ban leg (07-31, Hormuz-independent) survives a Hormuz de-escalation. **The NVDA/compute leg IS the TACO hedge** — a de-escalation crashes oil but rips risk-on/lower-yields/semis. Size the oil leg smaller than conviction; keep the barbell.
- **TACO early-warning (the kill-switch dials in reverse, fastest first):** (1) Truth Social / Witkoff / Qatar "deal close" headline; (2) war-risk insurance premium FALLING; (3) diesel crack / backwardation flattening; (4) tanker transit count rising. **One or two firing → exit oil BEFORE the news confirms.** Timing note: the 2-week horizon overlaps precisely the window in which a deal is most probable (June cycle ran escalate→deal in weeks; re-escalation is ~1 week old).
