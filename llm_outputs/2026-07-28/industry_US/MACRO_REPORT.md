# MACRO_REPORT — industry_US — 2026-07-28 (Tue)

> Stage 2/10. Sets wind direction only; ROTATION owns the sector verdicts.
> All news `--scope foreign` (hard rule). All FRED values `[FRED]`. Benchmark named inline on every
> relative number (C1). **Zero buy/sell language, zero sizing (P4).**

---

## ★★ The framing this stage is obliged to state first

**This run has a settled US session to read, and the last two runs did not.** The 07-25 run fired on a
Saturday and the 07-27 run fired one minute into a live session — both could only read the 07-24 close.
**2026-07-27 settled**, so every price-derived axis below is a genuine new observation, not a re-print.

**And the single most important thing that happened is not on the US price axis at all.** While this
desk's prior run was writing, **the Korean market settled −10.84% (KOSPI) / −11.55% (KOSPI200)** on a
memory-led rout whose named driver, in both feeds, is **CXMT** — the funded fourth DRAM entrant this
desk registered as **P9** yesterday and which **S34** (registered by the KR desk the same morning)
brackets. **The desk wrote the supply-side proposition on 07-27 and the market traded it on 07-28.**
That sequence is recorded here because it is the first time in this file's history that a newly-opened
proposition was tested by the tape within 24 hours.

⚠ **Run clock**: this stage executes **2026-07-28 ~09:2x ET, pre-open.** The 07-28 US bar does not
exist. **Per D74, no downstream stage may hand an agent a live `module_flow` RS number once 09:30 ET
passes** — the sweep must stamp `asof 2026-07-27`.

---

## §0 · Catalyst injection `[catalyst_calendar --days 10]`

**18 binary catalysts in the window.** PREMORTEM must bracket every ≤48h binary both ways.

| When | Event | Axis |
|---|---|---|
| **D-0 (today)** | **UPS Q2 — PRINTED pre-market** (S20 + S20-ANNEX) | freight / refiner-customer |
| **D-1 2026-07-29** | **FOMC (Warsh, no SEP)** · **META** · **V** · **STX** · **GD** · KR: SK hynix conversion date, FSC governance package | rates · earnings · structural |
| **D-2 2026-07-30** | **June PCE** · **VLO** · **STNG** · **MA** · **EQIX** · **ICE** · **FTNT** | inflation · earnings |
| **D-3 2026-07-31** | **XOM** · **Russia's diesel export ban EXPIRES** · **SK이터닉스 KKR SPA closing (S22)** · **CFTC COT covering today's close (S32)** | earnings · physical · structural · positioning |
| D-7→D-10 | AMD · ANET · **MPC** (08-04) · **PSX** (08-05) · CEG · LNG (08-06) · VST · **July NFP** (08-07) | — |
| undated | Iran "Strait of Hormuz open" statement | oil |

### ⚠ D18 fires a **NINTH** consecutive time — and this time it missed a **D-0** binary

`CATALYST_WATCH.json` (`--days 10`, as-of 2026-07-28) was checked **by string search, not by eye**.
It **does not contain UPS**, which printed **this morning** and is the registered falsifier of the rail
node. It also does not contain **MSFT · AMZN · XOM · EQIX · STX · SPGI · FTNT · ICE · GD**, nor any of
the six utility prints on 07-29/07-30 (**WEC · ETR · EXC · SO · XEL · AEP**). It **does** carry META,
VLO, STNG, MA, AMD, ANET, MPC, PSX, CEG, LNG, VST.

⇒ **The defect is single-name earnings source coverage, not window length** — a `--days 10` pull was
run and returned none of them. **The desk's own bracket book is more complete than the machine calendar
that seeds it**, which is the wrong way round for an anti-tunnel guard.

### ⚠ D61 fires a **FIFTH** consecutive time — a retracted claim is still being regenerated, dated *tomorrow*

The STRUCTURAL block still reads, verbatim:
> *"2026-07-29 SK하이닉스 ADR ↔ 원주 양방향 전환 개시 … 전환 개시로 차익거래가 열리면 프리미엄이 붕괴한다"*

This is **R13**, retracted 2026-07-24 on the named on-record testimony of **KSD's president 이윤수** —
the ceiling is **2.5%, not 25%**, and 07-29 is a *share-registration* date. It was replaced by **S17**
(the premium as a daily-printing observable). **The fix is a data edit to
`data/catalysts/structural_schedule.json` and needs human approval — not made here.**
★ **It settles itself tomorrow**: S17's premium prints daily from 07-29, so the R13-vs-donga dispute
resolves in numbers rather than in words.

---

## §A · Regime primaries `[FRED]` — pulled this run

| Series | Value | `asof` | Δ30d | 120d range | Note |
|---|---|---|---|---|---|
| Fed funds (DFF) | **3.63%** | 07-24 | 0.00 | 3.62–3.64 | |
| 2y (DGS2) | **4.33%** | 07-24 | **+0.22** | 3.38–4.37 | **fell 4bp** off the 120-day high |
| 5y (DGS5) | 4.43% | 07-24 | +0.26 | 3.51–4.46 | fell 3bp |
| 10y (DGS10) | **4.69%** | 07-24 | +0.28 | 3.97–4.71 | fell 2bp |
| 30y (DGS30) | 5.16% | 07-24 | +0.30 | 4.64–5.18 | |
| **real 10y (DFII10)** | **2.43%** | 07-24 | **+0.20** | 1.72–**2.43 = the 120-day maximum** | **S9's kill line 2.55 is 12bp away** |
| **breakeven (T10YIE)** | ★ **2.21%** | **07-27** | 0.00 | **2.18–2.50** | ★★ **fell 5bp in one session, to 3bp off its 120-day LOW** |
| HY OAS | **2.79%** | 07-24 | +0.01 | 2.63–3.46 | **+2bp** on the day |
| IG OAS | 0.80% | 07-24 | +0.04 | 0.73–0.94 | +1bp |
| NFCI | −0.552 | **07-17** | −0.03 | −0.564 to −0.454 | **11 days stale — outside its own ≤7-day lag** |
| DTWEXBGS | **120.71** | 07-24 | −0.70 | 117.44–121.41 | ★ **printed after 11 days** (S12 closed) |
| VIX (VIXCLS) | 18.58 | 07-24 | −0.31 | 14.49–31.05 | `^VIX` settled **18.67** on 07-27 |
| RRP | 1.38 | 07-27 | −4.34 | 0.03–26.9 | rose from 0.675; immaterial at this level |
| SOFR | 3.64 | 07-27 | 0.00 | 3.50–3.73 | |
| CPI / core CPI / unemployment / M2 | 332.568 / 336.065 / **4.2%** / 23,052.3 | **06-01 / 05-01** | — | — | ⚠ **monthly, ~1–2 months stale — stated, not dressed as fresh** |

### §A-1 ★★ The one thing the curve did that nobody registered: the inflation component fell, alone

**T10YIE is the only rate series that advanced to 07-27, and it fell 2.26 → 2.21 = −5bp**, putting it
**3bp above its 120-day low (2.18)** while the 120-day *high* is 2.50.

- **Arithmetic, not a print** (C3): DFII10's 07-27 value has not published. If the nominal 10y were
  unchanged at 4.69, the implied real 10y would be **4.69 − 2.21 = 2.48% — a new 120-day maximum and
  7bp from S9's 2.55 kill line.** ⚠ **This is a subtraction, not an observation, and is labelled as
  such.** It is not carried as evidence; it is carried as the reason to re-pull DFII10 first tomorrow.
- **What it settles about the decomposition** (P1's own two-series rule): the curve's move has been
  ~100% real for three consecutive measurements, and this session **extends it in the same direction on
  the only leg that printed.** The falling breakeven arrived **on the day oil made its lowest close in
  over a week** — the two are the same story, and the narrated Fed-hike trigger was oil (M69/M185).

### §A-2 · The registered thresholds, with their distances

| Bracket | Frozen threshold | Now | Distance |
|---|---|---|---|
| **S19-H** | DGS2 **>4.45%** by 08-05 | **4.33%** | **12bp away** (and moving away — fell 4bp) |
| **S19-D** | DGS2 **<4.15%** by 08-05 | 4.33% | 18bp away |
| **S19-M** | DGS2 inside 4.15–4.45 | **inside** | branch M is the live state |
| **S9 kill** | real 10y **>2.55%** | **2.43%** | 12bp away |
| **S23-B** | **T10Y2Y ≤ +0.20** with DGS2 inside 4.15–4.45 | **+0.36** (4.69 − 4.33) | ⚠ **0.16pp away, and it moved AWAY** — the 07-27 US run read +0.34; the curve **steepened 2bp** |
| **S26-B** | HY OAS **≥3.10%** on a close, NFCI turning positive WoW | **2.79%**, NFCI −0.552 | **31bp away**; NFCI still loosening |
| **P2's own pre-registered score** | HY OAS 07-24 **≥2.85 ⇒ "turn" · ≤2.72 ⇒ "tick" · else `AMBIGUOUS`** | **2.79%** | ★ **SCOREABLE AT LAST — see §F** |

---

## §B · Positioning `[CFTC COT — Tue close, 3–4d lag]` + `[FINRA Reg SHO, 2026-07-27]`

### COT — **unchanged, and that is the finding**

The release still covers the **2026-07-21** Tuesday close; the one covering **today's** close publishes
**2026-07-31**. Every value reproduces M125 exactly:

| Instrument | Net-spec | Wk Δ | 1y %ile | |
|---|---|---|---|---|
| **Nasdaq-100** | −9,691 | +621 | **5th** | 🔴 crowded SHORT |
| **S&P 500 (E-mini)** | −16,784 | +22,154 | **84th** | 🟢 crowded long |
| Russell 2000 | +6,758 | +6,655 | 88th | 🟢 crowded long |
| **UST 10Y** | −879,706 | **−48,031** | **12th** | 🔴 crowded short |
| UST 2Y | −1,154,597 | +2,880 | 53rd | neutral |
| USD Index | +15,614 | +2,441 | 66th | neutral |
| **WTI Crude** | +20,039 | +256 | **11th** | 🔴 crowded short |
| Nat Gas | −171,138 | +7,474 | 11th | 🔴 crowded short |
| **Copper** | +73,977 | +9,592 | **98th** | 🟢 crowded long |
| Gold / Silver | +183,910 / +23,465 | −2,772 / −1,609 | 23rd / 32nd | neutral |

⇒ **M125's 79-percentile-point spread inside one asset class is intact and unre-measured**, and
**S32 is therefore NOT scoreable today** — its observable is the release that lands 07-31. Scoring it
off today's tape would be scoring a price reaction, which S32's own registration text forbids.

### FINRA short-volume, 2026-07-27 — reported **with baselines**, per D52/D73

⚠ **Baseline discipline applied first.** The tool's stated normal band is 40–45%. Names whose own
20-day baseline sits materially outside it produce a z about their own history, not about covering, and
their verdict strings are **suppressed**: **UPS 57.3 · TRV 59.2 · MPC 54.3 · PLD 52.0 · UNP 50.8 ·
DLR 50.8 · COP 50.0** (high side) and **AMZN 31.1 · LRCX 31.2 · CVX 31.4 · STX 32.1 · MSFT 32.6 ·
stx/CSX 35.7** (low side).

**Readable and material:**

| Ticker | short% | base20 | z | 5v5 | Read |
|---|---|---|---|---|---|
| **MA** | 54.8% | 38.2% | **+2.12** 🔴 | **+6.9▲** | ★ **A short surge into the 07-30 print**, on the name M178 already called *"the least-supported of Financials' five green tags"* (388% of its 60-day excess in 20 sessions, on a flat book) |
| **VLO** | 50.7% | 41.9% | **+1.56** 🔴 | +3.8▲ | ★ Short surging into the **07-30** print, in-band baseline ⇒ readable |
| **META** | 19.8% | 39.6% | **−3.43** 🟢 | −2.9▼ | Shorts collapsing into the 07-29 print |
| MSFT · AMZN | 20.7 / 16.2% | 32.6 / 31.1% | −2.56 / −2.55 🟢 | −5.5▼ / −6.5▼ | Same direction; ⚠ both low-baseline |
| **Memory + equipment** | — | — | z **−0.14 to −1.12** | **ALL ▲**: AMAT **+13.1** · SNDK **+11.5** · WDC **+9.3** · STX **+9.0** · MU +5.4 · LRCX +5.2 | Shorts **building** across the whole complex |
| **AI-compute / server** | — | — | — | **DELL −6.3▼ · AVGO −6.0▼ · NVDA −2.8▼** | Shorts **leaving** — the opposite sign, same GICS sector |
| CSX | 19.3% | 35.7% | −1.59 🟢 | −11.7▼ | Shorts leaving ahead of the S20-ANNEX window |

⚠ **"Short building = bearish" is in this desk's REJECTED signal ledger (D6/D11).** The memory-vs-server
split above is reported as **liquidity-supply dispersion inside one sector**, not as a direction.
★ **The one genuinely new positioning fact** is that the three mega-cap spenders show a simultaneous
short-volume collapse on the last settled day, which is the **mechanism S32 branch A describes** — a
crowded short covering into the prints. **S32 forbids citing this as a signal**; it is recorded so that,
if the prints are overwhelmed by an unwind, the record shows it was foreseeable (the C6 discipline).

---

## §C · Narrative axis `[news, --scope foreign — hard rule]`

### §C-0 · Denominator, stated before any "quiet" or "loud" claim

`brief --date 2026-07-28 --scope foreign --body 2`:
**2,475 articles → 393 events → 393 market (0 non-market).**
Tiers: **head (≥5 outlets) 35 · body (2–4) 358 · tail 0 · subevents recovered 70.**

⚠⚠ **`tail = 0` is NOT the coverage claim, and on the foreign feed the recovery tiers are structurally
unavailable.** Measured this run:

| Recovery tier | Shown / total | Usable? |
|---|---|---|
| `single_source` (1 outlet) | **15 / 442** | ❌ **The module states these 442 have NO score — the non-market classifier is Korean-only.** They are not low-scoring, they are **unmeasured** |
| `excluded_nonmarket` (band nb > −3) | **0 / 0** | ❌ Empty for the same reason — nothing was classified |
| `subevents` (`└`) | 70 recovered | ✅ read |

⇒ **442 of 2,475 articles (17.9%) sit in a tier this desk can neither rank nor filter on the foreign
feed, and 3.4% of it was sampled.** Every "quiet in bucket X" claim below is therefore tagged
**`unknown`, not "quiet" (C3)**. ★ **This is a new dig (D87)** — the EXIT CHECK mandates reading three
recovery sections that only exist on the KR feed.

### §C-1 ★★ The day's #1 event is oil DOWN, and the term axis was blind to it — a second consecutive measurement of M186

**Head, 33 articles / 15 outlets:** *"Oil prices at lowest in over a week as pause in attacks brings…"*
with sub-events *"WTI Oil flirts with the $80 level"*, *"Treasury Yields Tick Lower Alongside Oil
Prices"*, *"US Stock Futures Retreat Amid Chip Pressure Even As Oil Pu[lls back]"*.

Against that, the pool-normalized bucket sweep (`fts --mode or --syn`, **separate argv**, pool velocity
**1.69×**):

| Bucket | d1 | d7 | vel | **Pool-normalized** |
|---|---|---|---|---|
| **Memory/semi** | 1,059 | 3,951 | 1.88 | **1.11×** ← the only elevated bucket |
| Rates/Fed | 1,971 | 8,197 | 1.68 | 1.00× |
| Oil/energy | 710 | 2,957 | 1.68 | **1.00× — FLAT on the day of a 15-outlet oil event** |
| Credit | 885 | 3,709 | 1.67 | 0.99× |
| AI-capex | 503 | 2,214 | 1.59 | 0.94× |
| Tariff/trade | 1,484 | 6,592 | 1.58 | 0.93× |
| **Shipping/geo** | 455 | 2,193 | 1.45 | **0.86× — the LOWEST bucket on the board** |

⇒ **M186 replicates**: *a term spikes when it is new; an event ranks when it is big.* On 07-27 the
Oil/energy bucket read **1.01×** on a 19-outlet oil event; today it reads **1.00×** on a 15-outlet oil
event that is the day's #1 story, and the geopolitical bucket that contains it is the board's **lowest**.
**Any stage gating on term velocity this week is gating on an instrument measured blind twice running.**

### §C-2 ★★★ C6's own probe is a QUERY-FORM ARTIFACT — measured, and it reverses six runs of readings

The desk has carried **`capex cut` d1 ≈ 0 across six consecutive measurements** as the empirical basis
for contradiction **C6** (*"absence of narrative is not evidence of absence"*), and **D52** proposed
retiring the term because *"the probe is measuring the desk's vocabulary, not the market's."*

**Measured this run, on today's corpus, same window, same scope:**

| Query form | `capex cut` d1 | `capex cut` d7 | `AI spending` d1 |
|---|---|---|---|
| **Quoted phrase (1 argv)** | **0** | **0** | 202 |
| **Two argv, AND-mode** | **66** | **273** | **690** |

The repo's own CLI documentation already warns about exactly this: *"Never quote a multi-word bucket —
it fails silently to ~0. `terms` is `nargs='+'`: one argv = one term"* (measured there at 1 hit vs
31,698). **`"capex cut"` never occurs as an adjacent bigram in financial English — writers say "cut
capex", "capex cuts", "cutting capital expenditure" — so the phrase form returns a structural zero
while the term pair returns 273 over a window that overlaps the runs which reported `d7 = 1`.**

**Scope discipline (C4).** This does **not** prove every prior run used the quoted form — that is not
verifiable from here. What is measured is stronger than needed: **a 0 from that probe is not evidence
of absence**, and the six carried zeros cannot be distinguished from this artifact.
⇒ **Filed as retraction R25 (§G).** What survives of **C6** is its conclusion, on *independent*
evidence (the KOSPI −8% circuit-breaker day ranking nowhere on term velocity; today's Shipping/geo
0.86× on the #1 event). **What is withdrawn is the `capex cut` = 0 datapoint that six runs cited.**
★ And **D52's remedy is now wrong in its stated form**: the probe does not need retiring, it needs
**calling correctly**. On the correct form it reads **1.00× pool-normalized — present and running at
exactly the pool rate**, which is a different finding from "absent".

### §C-3 ★★★ CXMT is the only term on the board that separates, and its own thread is BUILDING

| Instrument | Reading | vs next-best |
|---|---|---|
| **Term sweep, pool-normalized** | **CXMT 3.51×** (d1 177 / d7 209 ⇒ **85% of the week's coverage is today**) | next: `de-escalation` 1.80×, `China chip` 1.63× |
| **`theme_age --scope foreign`** | **CXMT 🟡 17.74× on n=273, age 75d** | next: `backlog` 5.32×, `capex` 5.25× ⇒ **CXMT is 3.3× the runner-up** |
| **07-27's reading of the same probe** | 10.98× on n=187 | **+62% acceleration, +46% n, in one day** |
| **`thread --days 7`** | `[BUILDING] 2→2 "Micron Rival CXMT's Stock Soars 466% After IPO"` · `[BUILDING] 3→5 "China is using the steel playbook on AI"` · `[REIGNITED] 3→4 "China's reported chip breakthrough…"` | three separate live threads on one axis |
| **Event tier** | *"Asian chip stocks slide as **China competition fears** rattle AI"* [11/9] · *"SK Hynix, Samsung Drag Down KOSPI as **China Chip Fears** Spread"* [11/6] · *"The Chips Rout Goes Global"* · *"China accuses U.S. of 'AI hegemonism'"* [5/5] | |
| **The tape it moved** | KOSPI **−10.84%**, KOSPI200 **−11.55%**, SK hynix **−13%**, Samsung Electronics −6.89% `[KIS primary]`; Nikkei −4%; *"Kospi index sinks 10%"* | |

⚠ **`theme_age` produced ZERO discrimination for a FIFTH consecutive foreign run** — ten probes, **all
🟡ACCELERATING, zero 🟢FRESH, zero 🔴FADING** (M112/M154/M180 replicate; per M163 this is a **feed**
property, not a tool property). **The verdict column is therefore not used as a gate anywhere in this
file; only the ratio beside its n is read**, and on that axis CXMT separates cleanly.

★ **D78 is executed rather than logged this run.** Its instruction — *"MACRO must list every
BUILDING/REIGNITED thread that maps to no bucket, and either open a bucket or state why not"* — is
carried out in §C-5. CXMT is exactly the case D78 was written from: the desk measured itself missing a
four-day 3→6→3→16-outlet build on this story, then opened P9 on 07-27, and the tape traded it on 07-28.

### §C-4 · Trajectories `[thread --days 7, foreign]` — 4,209 daily events → 3,223 threads (157 alive)

Per-day denominators: **07-22 816 · 07-23 863 · 07-24 780 · 07-25 297 · 07-26 287 · 07-27 773 ·
07-28 393.** ⚠ Today's 393 is **half** the prior weekday's and the run fired pre-open — **a low
denominator inflates nothing but it does hide things; the D84 lesson (a morning sweep cannot see an
intraday regime event) applies to the US session too.**

| Thread | Tag · curve | What it does to a proposition |
|---|---|---|
| *"Oil prices jump back above $100 per barrel"* | **🔴FADING** 15→27→19→5→14→22→**15** | The 7-day oil thread has rolled over. **P4's war-premium leg is the one fading, not its margin leg** |
| *"U.S. and Iran edge toward talks" → "Iran and Oman Seek Agreement on the Hormuz"* | **BUILDING** 3→5 | The de-escalation thread is **building for the first time**; `de-escalation` 1.80× pool-normalized |
| *"Red Sea tanker traffic… → Tankers Divert to Egypt as Houthi Threat Upends Red Sea Trade"* | **BUILDING** 4→4→2→2→5 | ⚠ **Physical disruption is BUILDING while the price thread FADES.** Saudi Red Sea crude exports **−41% since March**. **These are opposite-signed and both are true** |
| *"Asia Stocks Slide, Weighed Down by Chip"* | **BUILDING** 5→2→**10** | The rout |
| *"SK Hynix, Samsung Drag Down KOSPI as China Chip Fears"* | **REIGNITED** 3→6 | §C-3 |
| *"Dollar hits one-month high on lingering chances of Fed hike"* | **BUILDING** 2→6 | P1's narrated trigger, alive |
| *"BOJ Is Said to Be Open to Faster Pace of Rate Hikes"* · *"Japanese Yen… Fed, BoJ seen on hold but ha[wkish]"* | **REIGNITED 4→2** · **BUILDING 3→3→3→2→4** | **P7 stays in the scored tier a second run** |
| *"Tech Stocks Tumble On Spending Worries"* **vs** *"'The AI trade is still on': Wall Street sees Big Tech'[s]…"* | **REIGNITED 4→2** vs **REIGNITED 5→5** | ★ **Two opposite-signed AI-capex threads alive on the same day.** P3's `indistinguishable` is corroborated on the narrative axis, not only on price |
| *"Amazon winds down most flagship AI models in strategy overhaul"* [15/9] | head | ⚠ **A spender changing its AI product strategy one day before its own print.** Read as an event, not a capex number |
| *"Nvidia behind $50bn lease on Texas data centre"* · *"The Price to Finance the AI Data Center Boom Is Rising"* | body 4-outlet | The physical-layer demand side, and its **cost of capital** — M134's axis |
| *"SkyWest Q2 Profit Falls On Higher Fuel Costs"* | REIGNITED 3→4→2→2 | ★ **A sixth refiner customer**, same direction as DAL/UAL/FDX/LUV — and the opposite of UPS (§F) |
| *"China hits back at criticism over excess industrial capacity"* · *"China opposes US 'forced labor' tariffs"* | **BUILDING** 4→3→3→3→5 | P6, and it now touches the **supply** side of P9 |
| *"Zhongji Innolight raises $8.8 billion in Asia's second-largest listing"* | BUILDING 3→3 | ★ A **second** Chinese AI-hardware capital raise inside a week — the same mechanism as CXMT, a different layer |
| *"Boeing posts larger-than-expected Q2 loss as Air Force One c[osts]"* [9/5] | head | Industrials, name-level |
| *"Johnson & Johnson to pay up to $5.5B to settle talc lawsuits"* [10/10] | head | Health Care, name-level, **10 of 10 outlets = maximum dispersion** |
| *"Centene Raises 2026 Outlook"* [6/6] | head | Managed care — the sub-node C7 keeps failing to surface |

★ **ENDED threads under an open proposition: none found.** No inherited proposition is stale on this axis.

### §C-5 · D78 compliance — BUILDING/REIGNITED threads with **no matching term bucket**

| Thread | Bucket? | Decision |
|---|---|---|
| **CXMT / China chip competition** | ⚠ partially — inside "Memory/semi", which cannot separate it | ★ **OPEN A BUCKET**: `China-supply` = {CXMT, Innolight, overcapacity, "paid weights", export controls}. Folded into the living term table below |
| **Red Sea / Bab el-Mandeb physical disruption** | inside "Shipping/geo", which read 0.86× | ★ **Split needed**: the price leg and the physical leg are moving in opposite directions inside one bucket (D78's exact shape). **Stated, not built — a bucket redefinition mid-run would make today's sweep non-comparable to the prior five** |
| **Data-centre financing cost** (*"The Price to Finance the AI Data Center Boom Is Rising"*) | no bucket | **State why not**: it is M134's axis (HY OAS is its live variable) and is already covered by the Credit bucket + P2. **No new bucket** |
| **BOJ / yen** | no bucket | **State why not**: P7 is `[unverified]` under W2 pending D22. **A bucket would give an unverified claim a measurement slot it has not earned** |
| **Anthropic / AI-lab governance** (BUILDING 5→5) | no bucket | **State why not**: no listed instrument in `us_top300`; not actionable for a sector matrix |

**New terms folded into the living table this run:** `CXMT` · `overcapacity` · `paid weights` ·
`AI fatigue` · `de-escalation`. ⚠ `overcapacity` (d1 4) and `AI fatigue` (d1 8) are **at unusable n**
and are entered for future comparability only, with their n stated (the `tower REIT` 17.14×-on-7-hits
lesson, D63).

### §C-6 · Blind-spot pass, with its own denominator

`blindspot --days 1 --scope foreign`: window **9,382 articles**, blind pool **9,382**, random sample 400.
Token-0 emergent terms (top, excluding pure furniture): **AI 790 · Earnings 615 · Iran 308 · China 308 ·
Fed 244 · Nvidia 212 · Oil 203 · SpaceX 115 · Bitcoin 109.**

★ **Three sample rows are directly load-bearing and would not have been reached by any bucket:**
1. *"Hewlett Packard Enterprise (HPE) Rose on Strong AI Server Demand and Juniper Integration"* — an
   **independent corroboration of §3a's DELL/HPE thesis**, and HPE is the strongest 5-day RS in IT (§D-P3).
2. *"Sandisk and More Chip Stocks Hit China Roadblocks"* — SNDK, the board's **worst RS20 (−40.25)**.
3. *"S&P 500 On Track To Post Best Net Profit Margin Since 2009"* — ⚠ a **direct L2 (peak-margin)
   datapoint at index level**, and this desk has never measured the index-level margin percentile.

---

## §D · Macro propositions — falsifiable · both branches · anti-signal · KPI · dated catalyst

**P1 — The front-end repricing is a real-rate reaction-function trade whose narrated trigger is oil;
oil has now reversed three times and the curve has finally answered — by taking the INFLATION leg out.**
*(carried, 6th framing, materially advanced)*
- Anchor `[FRED]`: 2y **4.33% (−4bp)** · 10y **4.69% (−2bp)** · real 10y **2.43% = the 120-day max** ·
  **breakeven 2.21% (07-27, −5bp, 3bp off its 120-day LOW)**. 2s10s **+0.36, steepened 2bp.**
- ★ **The decomposition is now unambiguous on the only leg that printed**: nominal down, breakeven down
  more ⇒ **the real component is doing all the work, extended.** ⚠ **The implied real 10y of 2.48% is
  arithmetic, not a print (C3)** and is not carried as evidence.
- Anchor `[news]`: *"Dollar hits one-month high on lingering chances of Fed hike"* [16/6, BUILDING 2→6];
  *"8 Words From Fed Chair Kevin Warsh"* [6/6]; *"Wall Street divided on Fed as rising crude pr[ices]"*.
  Rates/Fed bucket **1.00× = exactly the pool rate.**
- **Both branches (mandatory — oscillating variable):** (a) the FOMC holds, oil keeps falling and the 2y
  retraces further → this was positioning into an event and TD's fade was right (**S19-M**, the live
  state); (b) **DGS2 closes >4.45% or real 10y >2.55% by 08-05** → duration de-rate becomes a regime
  call and **S19-H / S9 fire**. Distances: **12bp and 12bp.**
- **Anti-signal (kills P1):** DGS2 **<4.15%**, **or** the decomposition flipping to real-down /
  breakeven-up. ⚠ **The second half is now 5bp closer to being testable**, since breakeven moved alone.
- KPI: DGS2 daily · **DFII10 quoted with T10YIE** (S9's two-series rule) · 2s10s · the oil→2y pass-through.
- Catalyst: **FOMC 2026-07-29 (D-1)** · **June PCE 2026-07-30 (D-2)**. ⚠ **n≈1 pre-registered in S19:
  these two share one driver (oil), one day apart — they are not two observations.**

**P2 — Credit is the loudest narrative and the quietest market, and its pre-registered score finally
took: `AMBIGUOUS`.** *(carried, 8th run — now SCORED, see §F)*
- Anchor `[FRED]`: **HY OAS 2.79% (07-24, +2bp)** · IG **0.80% (+1bp)** · **NFCI −0.552, 11 days stale.**
- The 07-25 run pre-registered **≥2.85 ⇒ "turn" · ≤2.72 ⇒ "tick" · between ⇒ `AMBIGUOUS`.**
  **2.79% is between. `AMBIGUOUS`, exactly as frozen. No threshold moved, no proxy substituted.**
- ★ **The direction is not nothing**: HY OAS has now risen **2.68 → 2.77 → 2.79** over three prints
  = **+11bp off the 365-day low**, its first sustained widening in the carried window, **while NFCI
  keeps loosening.** Two conditioning variables disagreeing is **C4 territory, and it is written as
  `indistinguishable`, not as a turn.**
- **Both branches:** (a) spreads hold <3.00% → the three OW tilts stay three bets (**S26-A**);
  (b) **HY OAS ≥3.10% on a close with NFCI turning positive WoW** → **S26-B**, and all three OW carriers
  lose together on one shared beta (JPM 0.932 · DLR 0.769 · PLD 0.766 · PSX 0.747).
- **Anti-signal:** HY OAS >3.10% on a close, or NFCI rising two consecutive weeks.
- ⚠ **NFCI is 11 days old against its own ≤7-day lag.** Any financial-conditions claim this week must
  quote that staleness. KPI: HY OAS daily · NFCI weekly. Catalyst: FOMC 07-29 · PCE 07-30.

**P3 — Info Tech's single label is still unresolved, and this run's new data makes the spread's SIGN
depend on the window — which strengthens `indistinguishable` rather than resolving it.**
*(carried, materially advanced)*
- **Construction stated explicitly (C5 — the choice is arbitrary and is exposed, not hidden):**
  suppliers = mean of **{MU, AMAT, LRCX, KLAC}**, spender = **MSFT** (the only GICS-IT spender;
  META/GOOGL are Comm Services). Benchmark **SPY** on both legs. Settled **2026-07-27**.

| Window | Suppliers (mean) | MSFT | **Spread** |
|---|---|---|---|
| **RS20 vs SPY** | **−21.22** | +2.94 | **−24.16pp** |
| **RS5 vs SPY** | −0.76 | −2.87 | **+2.12pp** |

- ★★ **The spread's sign flips with the window** — suppliers 24pp *behind* over 20 sessions and 2pp
  *ahead* over 5. ⚠ **The prior run's carried scale (+6.07 → −4.20pp) is not reproducible without its
  construction, which was not recorded; this run states its own rather than inheriting an unstated
  one (C1/R20's lesson).**
- Corroborating dispersion inside the same sector: **DELL RS20 +5.48 / RS60 +103.71** and
  **HPE +8.86 / +66.42** against **SNDK −40.25 / +16.24**, **LRCX −24.46 / +13.36**, **MU −21.89 /
  +69.76**. **A single IT verdict is arithmetically a verdict on a 144pp RS20 range.**
- **Both branches:** (a) MSFT/META raise capex 07-29 and the spender multiple compresses while
  suppliers hold → **S13-A**, IT must be split; (b) the spenders re-rate on the same raise → the single
  label survives and the 20-day supplier drawdown was a memory-specific event.
- **Anti-signal (kills P3):** a capex **cut** at MSFT or META (§4 of STANDING_VIEW — it breaks the volume
  and price legs together). ⚠ **The probe that was supposed to detect this branch is retracted this run
  (§C-2, R25) — watch the line item, and do not read the feed's silence as anything.**
- KPI: the two-window spread above, **both windows reported, never one**. Catalyst: **MSFT + META
  2026-07-29** ⚠ **date-provider dispute declared and unresolved (D5)**: `yfinance` says MSFT 07-30 /
  META 07-30 / AMZN 07-31. **Every bracket is written on a window, so a 1-day error cannot void it.**

**P4 — ★★ The refining margin's kill line moved AWAY, not closer, and the settled series says the
opposite of what the last two runs' intraday reads said.** *(carried, materially advanced)*

Settled series `[own calc, yfinance CL/RB/HO/BZ continuous; settled-only is a rule (R17)]`:

```
              WTI     Brent   3-2-1 crack  gasoline crack  distillate crack  diesel−gas gap   CL vol
2026-07-22   86.83    94.07      66.865         56.587          87.420           30.83       358,021
2026-07-23   92.19   100.69      66.492         54.659          90.157           35.50       401,934
2026-07-24   89.31    96.78      64.304         53.318          86.275           32.96       365,438
2026-07-27   82.61    88.36    ★ 68.117         57.137        ★ 90.077           32.94      [365,438]⚠
──────────────────────────────────────────────────────────────────────────────────────────────────────
2026-07-28   81.36    86.67      63.823         51.788          87.892           36.10       119,919 ⚠UNSETTLED
```

- ★★ **On the settled 07-27 close the composite ROSE to 68.117 while crude fell 7.5%** — the highest
  since 07-20. **P4's anti-signal (a settled 3-2-1 below 60) is now 8.12 points away, up from 4.30 on
  07-24.** The kill line moved **away**, and the last two runs — both reading unsettled bars — reported
  it moving *closer* (61.665 intraday on 07-27, an implied ~61 on 07-28's KR re-pull).
- ★★★ **This is S8 branch B in its cleanest form yet: crude −7.5%, distillate crack +4.4% to 90.077.**
  It **independently corroborates the KR desk's `FIRED-B` verdict from a different reading of the same
  day** — they read distillate 85.1, this run reads 90.08; **both are ≥84, so the verdict is invariant
  across a 5-point input disagreement.**
- ⚠⚠ **But their stated buffer is not reproducible, and the cause is measurable** (§G, correction 1):
  the KR run reported a distillate buffer of **~1.075** over the 84 floor. On the true 07-27 settle the
  buffer is **6.08**; on today's unsettled 07-28 electronic bar it is **3.89**. Their inputs
  (WTI 81.560 / distillate 85.075) reconstruct to **HO ≈ 3.9675**, which sits between today's 07-28
  **low (3.9392) and open (3.9750)** ⇒ **they were reading a 2026-07-28 electronic tick labelled
  07-27. That is D83, and it is the sixth time this desk has mis-read a settled bar.**
- ★ **A new, concrete defect that breaks D83's own detector (D86, §H)**: on 2026-07-27 **all four
  contracts carry a Volume byte-identical to their own 07-24 value** (CL 365,438 · HO 23,447 ·
  RB 27,562 · BZ 33,923). Four independent contracts repeating a prior session's volume exactly is a
  **forward-filled field**, not a market event — the OHLC differ and are internally consistent.
  ⇒ **"check the volume to see whether the bar settled" cannot be applied to 07-27.**
- **Physical vs price, moving opposite ways** (§C-4): the **price** thread is 🔴FADING (7 days) while
  the **physical** thread is BUILDING — *Tankers Divert to Egypt*, **Saudi Red Sea crude exports −41%
  since March**, Red Sea traffic at a multi-month low, and **Japan backing overseas pipelines to reduce
  Hormuz dependence** [11/7]. ⚠ **Counter-evidence on the desk's own side is also live**: **Russia's
  diesel export ban expires 2026-07-31** (M93) and Singapore/Fujairah stock builds are two of M128's
  five named hubs inverting.
- **Both branches:** (a) the composite holds ≥62 on settled closes with the diesel gap above 33 → the
  margin engine is intact and the fall was a gasoline/war-premium event, i.e. **input-cost relief**;
  (b) **a settled 3-2-1 below 60**, or **the distillate crack breaking below 80** → the bottleneck
  itself is going, into a WTI already at the **11th COT percentile**.
- **Anti-signal (kills P4), one axis:** **a settled 3-2-1 crack below 60.** Distance: **8.12 points.**
- ⚠ **The counter-observation this run must carry against its own proposition**: the KR refiners
  (096770 / 010950) **underperformed their own betas by a median 3.57pp on 07-28 — on the first session
  that opened with the crack's recovery public.** See HANDOVER §2 (S33). **That is one vote for the
  war-premium reading of C4, from the market that trades the same margin.**
- KPI: **3-2-1 crack on SETTLED closes only** · the diesel-minus-gasoline gap · WTI COT percentile.
- Catalyst: **VLO 07-30** · **STNG 07-30 (S21)** · **Russian diesel ban expiry 07-31** · **XOM 07-31**
  · **MPC 08-04 · PSX 08-05**.

**P5 — The digital-infrastructure underweight's stated mechanism stays refuted, and its own anti-signal
has now been read: DLR's 20-day excess has fully retraced.** *(carried, ADVANCED)*
- Registered anti-signal: *"DLR's excess vs SPY fully retracing by 2026-07-31."* **Read on the settled
  07-27 close: DLR RS20 vs SPY = +0.04pp — flat to the benchmark.** ⚠ **But RS5 = +11.47pp**, i.e. the
  entire 20-day position is the 07-24 +6.05σ event and the days before it were negative. **Both windows
  are reported; neither alone is the answer (C2).**
- ★ **S25's own condition is currently SATISFIED on the settled bar**: **DLR RS20 +0.04 sits below the
  {PLD, AMT, WELL} median RS20 of +3.82, and that median is positive.** S25's window runs to
  **2026-08-08**, so this is reported as **tracking branch B, not scored** — moving a verdict forward
  to tidy the ledger is the same class of act as moving a threshold. **EQIX prints 07-30** = S25's
  second settling point; EQIX RS20 **−5.46**.
- **Both branches / KPI unchanged.**

**P6 — The tariff axis is enacted, cross-sector, and has acquired a SUPPLY-side leg.** *(carried, advanced)*
- Tariff/trade **0.93× pool-normalized**, and the thread is **BUILDING 4→3→3→3→5**: *"China opposes US
  'forced labor' tariffs"* [18/5, 07-27] → *"China hits back at criticism over excess industrial
  capacity"* [6/5, today]; *"China accuses U.S. of 'AI hegemonism,' threatens countermeasures"* [5/5];
  *"US probes Chinese factories in Vietnam"*; *"Chinese AI developers may shift to 'paid weights'"*.
- ★ **New**: the axis now touches **P9** — "excess industrial capacity" is the same argument as CXMT's
  capacity build, made by the two governments about each other. **Per §C-0 the absence of anything
  larger is bounded by an 82%-unmeasurable single-outlet tier ⇒ `unknown`, not "quiet" (C3).**

**P7 — Japan is the un-priced global-duration channel, and it holds the scored tier a second run.**
*(carried, status HELD)*
- Anchor `[news]`: **BUILDING 5-day yen/BoJ thread (3→3→3→2→4)** plus **REIGNITED *"BOJ Is Said to Be
  Open to Faster Pace of Rate Hikes"* (4→2)**; *"Japanese Market Sharply Lower, Tumbles 4%"* and
  *"Losses May Accelerate For Japan Stock Market"* on today's rout.
- ⚠⚠ **Still `[unverified]` under W2 and NOT admissible as evidence.** *"BOJ tightening leads US
  long-end yields"* has **no lag table in this repo (D22, open)**. DEEP and BET may not cite it.
- The 07-25 escalation (*"either D22 gets built or P7 is retired"*) now has **two consecutive runs in
  the scored tier** on its side. **Still a human's decision; carried, not resolved.**

**P8 — The rate shock's housing/consumer transmission is still unmeasurable in this repo.** *(carried)*
- **`MORTGAGE30US` is still not wired into `module_macro_us`'s catalog — a FOURTH run.** A proposition
  whose KPI cannot be pulled cannot be scored. Carried unchanged so the omission stays visible.

**P9 — ★★★ The supply-side entrant proposition opened yesterday and the tape traded it today; the
proposition is UPGRADED from `[news]`-grade to `[news + tape]`, and its bracket now exists (S34).**
*(opened 2026-07-27, advanced)*
- **What is new since yesterday**: (i) **CXMT is the only term on the board that separates** — 3.51×
  pool-normalized, `theme_age` **17.74× on n=273** against a runner-up of 5.32×, with **85% of the
  week's coverage printing today** (§C-3); (ii) **the KR market settled −10.84% / −11.55% with SK hynix
  −13%**, and both feeds name CXMT; (iii) **S34** now brackets it on a **primary-source capacity
  observable** (300k → 350k wpm by year-end, settling 2026-10-31) rather than on price; (iv) a **second**
  Chinese AI-hardware raise landed — **Zhongji Innolight $8.8bn, Asia's second-largest listing**.
- **What it still does NOT do (stated first, so it is not over-read):** it does not change 2026 supply,
  it does not touch **M1** (the contract-price second derivative), and **every capacity figure is
  `[news]`-grade with no issuer filing read** — which is precisely why S34's observable is written
  *"from a primary source"*. Under **L1** this remains a *level*-and-*funding* fact, not a *rate* fact.
- ★ **The constraint the counter-argument rests on, carried in full (C2)**: **no EUV ⇒ DUV
  multi-patterning; ~2 process generations behind; HBM 3–4 years behind (HBM3E mass production 2027)**
  — and a measured **2.2% price PREMIUM** for a CXMT-based RDIMM over Samsung/SK-based at JD.com,
  which is **single-outlet, cross-confirmation failed, and uses a level to argue about a rate.**
- **Both branches:** (a) CXMT's capex lands in commodity DDR while HBM stays a three-supplier market →
  the AI-memory node is insulated and this is a China-domestic substitution story; (b) **the proceeds
  compress commodity DRAM pricing into 2027–28 while hyperscaler LTAs reset** → the *trough* of the
  next cycle is deeper than M18's 17-year series implies, and **L2's peak-margin read on MU strengthens.**
- **Anti-signal (kills P9):** an actual **Entity List designation** blocking equipment access, **or** a
  disclosed CXMT capex plan materially below the raise.
- ⚠ **Do NOT score P9 on the KOSPI.** A −10.8% index session is a price reaction, not this proposition's
  observable — **S34 says so explicitly at registration.**
- KPI: **CXMT wafer capacity from a primary source (S34)** · DRAM contract price QoQ (M1) · whether any
  2027 capacity guide from SK/Micron/Samsung names a fourth supplier.
- Catalyst: **S34 settles 2026-10-31** · MU FQ4 ~2026-09 (S4) · 4Q26 DRAM contract guidance ~09/10 (S3).

**P10 — ★ NEW · The memory complex's 20-day drawdown is now large enough that "pullback inside an
uptrend" and "the top" have measurably different observables, and the desk has a registered bracket for
exactly one of them.**
- Anchor `[measured, settled 2026-07-27, benchmark SPY inline]`: RS20 / RS60 —
  **SNDK −40.25 / +16.24 · LRCX −24.46 / +13.36 · MU −21.89 / +69.76 · KLAC −19.60 / +8.10 ·
  AMAT −18.93 / +31.24 · WDC −16.48 / +16.77 · STX −10.60 / +23.13.**
  **All seven: RS20 deeply negative, RS60 positive.** Median RS20 of S30's basket {STX, MU, WDC} =
  **−16.48** (registration −23.7 ⇒ improved 7.2pp but still ≤0 ⇒ **S30 branch B holding**).
- ★ **S30's own control pair separates cleanly**: **DELL RS20 +5.48 / RS60 +103.71** and
  **HPE +8.86 / +66.42**, with days-21-60 excess of **+98.24 / +57.55** — the only two names whose
  60-day excess is *not* a last-20 event. **S30 pre-registered the disambiguation: if the memory median
  turns while DELL/HPE do not, it is a memory event; if both turn, it is an IT-beta event. Neither has
  turned, and DELL/HPE are still positive ⇒ this is a memory event, not IT beta.**
- **Both branches:** (a) **S30-A** — the median crosses above 0 by 2026-08-05 → the 60-day run was
  pausing, and M149's decaying-stock reading is falsified; (b) **S30-B** — it stays ≤0 → M149 holds
  and the IT-Neutral's "wait for the 08-19→09-07 roll-off" defence stands.
- **Anti-signal (kills P10):** HY OAS ≥3.10% on a close — then it is **S26**, not an IT event.
- ⚠ **What P10 deliberately does NOT claim**: the direction. **`indistinguishable` (C4)** — a −24pp
  RS20 with a +70pp RS60 is compatible with both branches, which is why it is registered as a bracket
  rather than argued as a view. n on the "seven names" is **1 date (S1)**, not 7.
- KPI: median RS20 vs SPY of {STX, MU, WDC}, with **DELL/HPE quoted alongside every time**.
- Catalyst: **STX 2026-07-29** (⚠ **±14.6% pre-declared no-information band, S30**) · MU FQ4 ~09.

---

## §E · ★ SECTOR TRANSMISSION MATRIX — the deliverable (ROTATION's input)

> Settled **2026-07-27**, benchmark **SPY** inline. Sector ETF day/5-day: XLE **−2.11 / +0.72** ·
> XLF **+1.01 / +1.50** · XLK **−0.90 / −0.80** · XLU **−1.32 / +1.65** · XLRE **−0.41 / +1.17** ·
> XLI **+0.30 / +2.85** · XLV **+0.51 / +2.61** · XLY **+1.31 / −3.29** · XLP **+1.46 / +0.59** ·
> XLB **+0.25 / +2.72** · XLC **+1.28 / −2.83** · SPY **+0.02 / −0.40** · QQQ **−0.31 / −2.00**.

| # | GICS Sector | Tilt | Δ | Driving prop. | Evidence this run |
|---|---|---|---|---|---|
| 1 | **Energy** | **OW−** | **hold** | **P4** | ★ **The kill line moved AWAY**: settled 3-2-1 **64.30 → 68.117**, buffer **4.30 → 8.12**, on crude **−7.5%** ⇒ **S8-B**. But the leg is splitting internally: **XLE −2.11% on the day**, and **days-21-60 excess is negative at every integrated/services name** (XOM −15.77 · CVX −14.71 · COP −21.44 · SLB −19.61 · BKR −21.55) while the refiners are near zero (**VLO +1.29 · MPC +3.75 · PSX −3.76**) ⇒ **M177's clean split is DEGRADING — PSX has flipped negative.** ⚠ **VLO short-vol z +1.56 🔴 into its 07-30 print** (in-band baseline ⇒ readable) |
| 2 | **Info Tech** | **N (split unconfirmed)** | hold | **P3, P9, P10** | ★★ **The largest measured dispersion on the board — a 144pp RS20 range inside one label** (DELL +5.48 · HPE +8.86 vs SNDK −40.25). **P10 registered.** ⚠ **P9's supply-side entrant is now a traded fact, not only a filing fact** — but on a KOSPI session, which S34 forbids scoring on. **S13 lands 07-29 · STX 07-29 (±14.6% no-information band)** |
| 3 | **Financials** | **OW−** | hold | P1, P2, **S23** | **XLF the best 5-day sector (+1.50%)**, and the front end **eased** (2y −4bp). ⚠ **S23's bear-flattener-hold is 0.16pp away but moved AWAY — T10Y2Y +0.34 → +0.36.** ★ **New adverse fact: MA short-vol z +2.12 🔴, 5v5 +6.9▲, into a 07-30 print, on the weakest of the five green tags (M178).** P2 scored `AMBIGUOUS` |
| 4 | **Industrials** | **OW−** | hold | P4, **S20** | ★★ **S20 scored `FIRED-B` this morning — see §F.** UPS **raised** FY guidance (revenue $91.2bn, adj EPS ~$7.22) ⇒ **branch C (a volume cut) did NOT fire, so the rail node's registered falsifier did not fire either.** **S20-ANNEX's median RS20 of {CSX, UNP, NSC} = +8.38** (prior +11.7) — still positive, settles 08-04. ⚠ **W4/D23 closes at 4 of 5 with the 5th REFUTING the other four** ⇒ this is now a **dispersion** finding (W5), not a closure |
| 5 | **Health Care** | **N** | hold | C7 | **XLV +2.61% over 5 days = 2nd-best sector.** C7's resolving observable (one 🟢 from outside the top-6 by cap) is SWEEP's to read; **ABT carries RS20 +9.63 / RS60 +10.54** and is the standing watch name. Feed: **JNJ $5.5bn talc settlement [10/10 outlets]**, **Centene raises 2026 outlook [6/6]** — both name-level, neither a sector driver. Horizon **08-06** |
| 6 | **Comm Services** | **N−** | hold | P3, **S16** | **XLC +1.28% on the day but −2.83% over 5.** **META RS20 +6.54 with RS5 −7.64** — rolling over into its own print; **short-vol z −3.43 🟢** = shorts collapsing into it. **S16 lands 07-29** |
| 7 | **Utilities** | **N−** | hold | P1, **S24** | ★ **S24's frozen observable read on the settled bar: median RS20 vs SPY of {VST, CEG, GEV, VRT} = −5.68** (VST −5.31 · CEG +0.88 · GEV −6.04 · VRT −6.76) ⇒ **threshold is >0 by 08-12; branch A (the UW is right) is holding.** ⚠ **XLU −1.32% on the day** on a falling real-rate-adjacent tape. ⚠ **n≈1 declared at registration** (VST–CEG +0.768) |
| 8 | **Real Estate** | **N** | hold | P5 | ★ **P5's anti-signal READ for the first time: DLR RS20 +0.04 = fully retraced**, and **S25's condition is currently satisfied** (DLR below the {PLD, AMT, WELL} median of +3.82, median positive) — **tracking branch B, not scored; window to 08-08.** **EQIX 07-30** is the second settling point (RS20 −5.46). ★ **K8, R7's replacement non-overlapping block, is one session old** |
| 9 | **Materials** | **UW** | **hold, disagreement now RESOLVED against the tilt's favour** | P1, P6 | ⚠ **The deferred test finally ran.** The 07-25 run declared *"if XLB beats SPY again next session the UW needs re-argument."* **Settled 07-27: XLB +2.72% vs SPY −0.40% over 5 sessions and +0.25% vs +0.02% on the day — XLB beat SPY on both windows.** ⇒ **the UW's re-argument is now DUE, and ROTATION owns it.** Copper still **98th COT percentile** |
| 10 | **Cons. Discretionary** | **N−** | hold | P1, P8, P6 | **XLY −3.29% over 5 days = the worst sector**, on a 2y that just *eased*. **P8's KPI still unpullable** (`MORTGAGE30US` unwired, 4th run) ⇒ the transmission cannot be tested |
| 11 | **Cons. Staples** | **N** | hold | P1, P6 | **XLP +1.46% = the best single-day sector** on a risk-off tape. No proposition claims it; recorded, not interpreted |

**Wind summary.** **Direction unchanged on all eleven — and this run has a settled session, so that is
a decision rather than an absence.** Three facts move the board's state:
**(i) the refining kill line moved AWAY, not closer** — the two prior runs' "closest of the advance"
readings were both unsettled bars (P4, §G);
**(ii) a 144pp RS20 dispersion opened inside Info Tech**, with the memory/equipment complex in a −16
to −40 drawdown while the AI-server pair holds positive on both windows (P10);
**(iii) the supply-side proposition opened yesterday was traded today**, on the only term that
separates from the pool (P9/§C-3).
⚠ **And one tilt now owes a re-argument**: **Materials**, whose own deferred test ran and went against it.

**DEEP candidates handed to ROTATION** (ROTATION owns the final pick):
**① Info Tech / memory (P3 + P9 + P10)** — the largest dispersion on the board, a supply-side entrant
the standing view's capacity clock does not contain, **S13 + STX on 07-29**, and C1 finally with a named
counterparty.
**② Energy (P4)** — the kill line moved away on settled data while the *KR* market voted the other way
on the same margin (S33); **M177's clean integrated-vs-refiner split is degrading**; **VLO 07-30 ·
STNG 07-30 · Russian ban expiry 07-31 · XOM 07-31**.
**③ Financials (P2 + S23)** — the bear-flattener-hold branch that kills NIM without tripping S19 or S9,
**plus a fresh adverse positioning read on MA two days before its print**.
**④ Real Estate (P5 + S25)** — the only tilt whose registered anti-signal has actually been read, and
it read **in favour of the falsifier**; **EQIX 07-30**.
**Swing, flagged to PREMORTEM: Materials** — the tilt whose own deferred test just ran against it, into
a copper COT at the 98th percentile.

---

## §F · Self-backtest

### Scoring the 2026-07-27 propositions — per KPI, with `unknown` where the observable did not print

| Prop | Registered KPI / threshold | Verdict this run |
|---|---|---|
| **P1** | oil → 2y pass-through | ★ **HALF-SCOREABLE at last.** Oil fell; **the 2y fell 4bp and the 10y 2bp** ⇒ the pass-through is **present and directionally consistent** on the 07-24 print. ⚠ The 07-27 curve has not published, so the *magnitude* stays `unknown` (C3, 3rd run) |
| **P2** | **HY OAS 07-24 ≥2.85 ⇒ turn · ≤2.72 ⇒ tick · else `AMBIGUOUS`** | ★ **SCORED `AMBIGUOUS` — 2.79%, between the frozen bounds.** Registered on 07-25, unscoreable for two runs, **taken exactly as written.** No threshold moved, no proxy substituted |
| **P3** | supplier−spender σ-normalized spread | ★ **NEW VALUE, and the finding is that its SIGN depends on the window**: RS20 **−24.16pp** vs RS5 **+2.12pp**. ⚠ The prior scale is not reproducible without its construction; this run states its own (C5) |
| **P4** | settled 3-2-1 crack <60 | ★ **NOT triggered, and the distance INCREASED 4.30 → 8.12.** The prior two runs' "closest of the advance" readings were **unsettled bars** ⇒ **MISS on the direction of travel, correct on the verdict** |
| **P5** | DLR excess vs SPY fully retracing by 07-31 | ★ **HIT — read for the first time. DLR RS20 vs SPY = +0.04pp = fully retraced**, 4 days early. ⚠ RS5 **+11.47** ⇒ both windows reported (C2) |
| **P6** | `[blank]` implementation date | unchanged; the axis gained a **supply-side leg** |
| **P7** | presence in the scored news tier | **HELD a second run** (BUILDING 5-day thread + a REIGNITED BoJ thread) |
| **P8** | `MORTGAGE30US` | **still unwired — unscoreable by construction, 4th run** |
| **P9** | CXMT capacity from a primary source | ★ **The KPI did not print, and the term did**: 3.51× pool-normalized, `theme_age` 17.74× on n=273. ⚠ **Term velocity is not the registered KPI and is not scored as one** |

**Running hit-rate, this run:** scoreable KPIs = 5 (P1-half, P2, P3, P4, P5). **HIT 2 (P5, P4-verdict)
· AMBIGUOUS 1 (P2, as pre-registered) · NEW-VALUE-NO-VERDICT 2 (P1-half, P3).** Unscoreable by
construction: **P8 (4th run)**. ⚠ **P4 records a half-miss the desk would otherwise not have logged**:
the *verdict* was right for three runs, but the *direction of travel* reported on 07-25 and 07-27 was
wrong, and both wrong readings came from unsettled bars.

### Scenario scoring done at HANDOVER (§2 of `HANDOVER.md`), summarised here

| ID | Verdict | One line |
|---|---|---|
| **S20** | **FIRED-B** | UPS **raised** FY guidance ⇒ branches A and C cannot fire; fuel absent from all five outlet write-ups. **W4/D23 stalls at 4 of 5 with the 5th refuting the other four** |
| **S28** | **FIRED-A** | Both KKR nominees elected (**99.4% / 99.5%**, DART primary). The S22 condition precedent clears — **not itself a closing** |
| **S33** | **FIRED-A raw / branch-B beta-adjusted** | ★★ **The two pre-registered readings disagree, and that disagreement is the verdict** — L3-bis instance #2 |
| **S32** | **not scoreable** | The COT release covering today's close publishes **07-31** |
| **S25 · S24 · S30 · S31 · S20-ANNEX** | **tracking, not scored** | Frozen observables read on the settled bar (§E); every window is still open |

---

## §G · Corrections and retractions filed by this stage

**R25 (new retraction) — *"`capex cut` has returned ~0 for six consecutive measurements, therefore the
capex-as-margin-drag branch is un-narrated."*** Killed by measurement, §C-2: on today's corpus the
**quoted-phrase form returns 0 (d1 and d7) while the two-argv AND form returns 66 / 273** over a window
that overlaps the runs which reported `d7 = 1`. The repo's own CLI documentation warns that a quoted
multi-word bucket **fails silently to ~0**, and `"capex cut"` is a bigram financial English does not
write. **What survives: C6's conclusion, on independent evidence.** **What is withdrawn: the six
`capex cut ≈ 0` datapoints, and D52's stated remedy (retire the term) — the correct remedy is to call
it correctly.** ⚠ **Scope (C4)**: this does not prove which form each prior run used; it proves the
readings are not admissible as evidence of absence.

**Correction 1 (not a retraction — it never entered the carry).** The 2026-07-28 `industry_kr` run
scored **S8** with **WTI 81.560 / distillate crack 85.075 labelled 07-27**, and reported a branch-B
buffer of **~1.075**. Measured here: the settled 07-27 values are **WTI 82.61 / distillate crack
90.077** (buffer **6.08**), and today's unsettled 07-28 electronic bar gives **87.892** (buffer 3.89).
Their inputs reconstruct to **HO ≈ 3.9675**, between today's **low 3.9392** and **open 3.9750**.
⇒ **They read a 07-28 electronic tick wearing 07-27's date — D83, the sixth instance.**
★ **The verdict `FIRED-B` is invariant across all readings and is not disturbed.** **The buffer is.**

**Correction 2.** This run's own §A first wrote the implied real 10y (2.48%) as if it were a print. It
is **4.69 − 2.21, arithmetic on two series with different `asof` dates**, and is now labelled `[C3]`
and excluded from evidence. Caught inside the stage.

---

## §H · New digs registered by this stage

| # | Dig | Why it matters | Owner |
|---|---|---|---|
| **D86** ★★ | **The daily futures bar's Volume field can be forward-filled, which breaks D83's own detector.** Measured 2026-07-27: **CL=F 365,438 · HO=F 23,447 · RB=F 27,562 · BZ=F 33,923 — every one byte-identical to its own 07-24 value**, while all four OHLC sets differ and are internally consistent | D83's minimum fix was *"treat a daily bar as unsettled until volume confirms."* **On this date the volume cannot confirm anything.** A stage applying D83 mechanically would have rejected a genuinely settled bar — or, worse, accepted an unsettled one whose stale volume looked full. **Minimum fix: cross-check the bar's date against the exchange clock (settle ≈17:00 ET + 1h), not against its own volume; and flag any volume identical to the prior session's** | any stage quoting a futures settle / human |
| **D87** ★★ | **The three `brief` recovery tiers the MACRO EXIT CHECK mandates do not exist on the foreign feed.** Measured: `single_source` **15 shown / 442 total, and the module states those 442 have NO score because the non-market classifier is Korean-only**; `excluded_nonmarket` is **0/0** for the same reason | The EXIT CHECK requires quoting `single_source.count − shown` and `excluded_nonmarket.count − shown` before any "quiet" claim. **On the US desk one of those numbers is unmeasurable and the other is structurally zero**, so **17.9% of the day's articles sit in a tier that cannot be ranked or filtered** and every US "quiet in bucket X" claim is `unknown` by construction. **Minimum fix: either an English-capable classifier path, or an explicitly different (and honest) EXIT CHECK for the US desk** | `module_news_data._brief` / EXIT CHECK / human |
| **D88** ★ | **The `capex cut` class of defect is not one term — no stage validates that a multi-token probe was passed as separate argv.** Six runs of a carried contradiction rested on a probe whose failure mode the repo already documents | ★ **A one-line guard is available and cheap**: `fts search` could **warn when a single argv contains whitespace**. That would have fired on `"capex cut"`, on `"AI 서버 MLCC"` (M68) and on `coverage "반도체,금리,환율"` — three separately-documented instances of the same defect across two markets | `module_news_data._fts` / human |

**Reproduced without change this run:** **D18 (9th)** · **D61 (5th)** · **D52/D73** (7 of the pre-event
names carry out-of-band FINRA baselines; verdict strings suppressed) · **D22** (P7 still `[unverified]`)
· **D56** (`MORTGAGE30US` unwired, 4th run) · **D5** (the MSFT/META/AMZN date-provider dispute is
declared and still unresolved).

---

## ✅ EXIT CHECK

- [x] Catalysts injected (`--days 10`, cross-checked against every ARMED `SCENARIOS.md` date); narrative
      (**events + trajectories + 7-bucket + blindspot**) and indicators (FRED primaries + COT + FINRA)
      read; daily anchor = `llm_outputs/2026-07-27/industry_US/MACRO_REPORT.md` read in full, plus
      `module_report_tags show`.
- [x] Events read via `brief --body 2`; **tail = 0**.
- [x] **`tail = 0` is NOT claimed as coverage.** `single_source` **15 / 442 (427 withheld, and the 442
      are UNSCORED — the classifier is Korean-only)**; `excluded_nonmarket` **0 / 0**; `subevents` **70
      recovered**. **Every "quiet" claim in §D is tagged `unknown` (C3)** and D87 is filed.
- [x] **Denominator corrected and quoted**: 2,475 articles → 393 events → 393 market, 0 non-market.
- [x] Trajectories read (`thread --days 7`); every proposition carries a thread tag+curve or states
      "no thread"; **no ENDED thread sits under an inherited proposition**.
- [x] Every "nothing happened in bucket X" claim carries its denominator.
- [x] **Every bucket passed as separate argv** — and this run **measured what happens when it is not**
      (§C-2, R25).
- [x] **Both halves cited**: UPS (adj EPS $1.76 beat **and** GAAP net income −53% YoY); CPI/M2/unemployment
      flagged as 1–2 months stale; P5 reported on RS20 **and** RS5; the crack reported on settled **and**
      unsettled bars with both labelled.
- [x] **Every relative-performance number names SPY (or `069500.KS` for the KR cross-reference) inline.**
      No statistical result carried across markets without replication — the S33 KR result is reported
      as a KR measurement bearing on C4, **not transferred to US names**.
- [x] **Credit axis read and cited**: HY OAS **2.79% (07-24)**, IG 0.80%, NFCI **−0.552 (07-17, flagged
      11 days stale)**. P2's pre-registered score taken.
- [x] **`real_10y` quoted with `breakeven_10y`** — and this run's headline rate finding *is* that pairing.
- [x] Linter run on this file — see §I.
- [x] Transmission matrix produced, all 11 sectors, one line each.
- [x] MACRO_REPORT.md written with primary numbers explicit; self-backtest hit-rate appended; new
      blind-spot terms folded into the living table (§C-5).

---

## §I · Rule-linter result

```
# REPORT_LINT — 1개 파일 · 규칙 C1,C2,S6,D6
  ✅ MACRO_REPORT.md
총 0건.
```
⚠ It checks **form only** (C1 benchmark · C2 both halves · S6 future label · D6 OBV-alone);
**a clean run is not a correct report.** The substantive checks this run actually turned on were done
by hand: the S33 betas were re-measured rather than inherited (C1), the crack series was re-pulled on
settled bars and disagreed with two prior runs (§G), and the `capex cut` probe was tested against its
own documented failure mode (§C-2).

---

## §5 · DRIFT ADDENDUM — appended 2026-07-28 by stage 10 (append-only; nothing above is rewritten)

> Baseline: this report was written ~09:2x–10:0x ET, **pre-open**. This addendum measures the window
> after it, with **the US regular session now open**.

### ⚠ The instrument failed for a SIXTH consecutive run, and its backup failed too

- **`scripts/drift_watch.py` → `rc=2: 'drift' 는 원격 실행 불가`** — the client-side `DB_READ_CMDS`
  edit has **still never been deployed to the running server** (P6, pending **six** runs). **D17/D64.**
- **`module_news_data burst` TIMED OUT on the remote API** — *"뉴스 API 접속 실패 … read operation
  timed out"*. **D55, fourth consecutive run.**
⇒ ★ **Both "find what I did not think to query" instruments were down again in one run.** The
substitute below can only test phrases already thought of, so **a clean sweep means "none of the known
phrases fired", NOT "nothing happened."**

### Kill-switch sweep — the substitute's result, pool-normalized

Pool (`the·a·of·in·to`, `--scope foreign`): **d1 5,315 · d7 22,367 ⇒ pool velocity 1.66×.**
⚠ The pool's d1 fell from **8,884** at MACRO to **5,315** here because `--days 1` is a rolling
`fetched_at` window; **the pool was re-measured rather than inherited, so the ratios are comparable.**

| Term | d1 | d7 | vel | **pool-normalized** |
|---|---|---|---|---|
| ★ **CXMT** | **177** | 209 | 5.93 | ★★★ **3.56× — 🚨 the only alarm** |
| overbuild | 10 | 34 | 2.06 | 1.24 ⚠ **n=10, unusable** |
| downgrade | 87 | 315 | 1.93 | 1.16 |
| reopen | 73 | 272 | 1.88 | 1.13 |
| default | 98 | 385 | 1.78 | 1.07 |
| guidance cut | 200 | 791 | 1.77 | 1.06 |
| strike · transit fee · Entity List | 485 · 47 · 72 | — | — | 1.05 · 1.05 · 1.03 |
| **capex cut** | **66** | **273** | 1.69 | **1.02** |
| AI spending | 690 | 2,864 | 1.69 | 1.01 |
| ceasefire · recession | 120 · 84 | — | — | 0.97 · 0.97 |
| Hormuz open · escalation · credit stress | 94 · 301 · 28 | — | — | 0.92 · 0.84 · **0.83** |
| inventory build · layoffs | 61 · 30 | — | — | 0.79 · **0.57** |

★ **`capex cut` at 1.02× is its SECOND correctly-formed measurement** (the first was §C-2's). **It sits
at exactly the pool rate — present, not accelerating.** ⇒ **R25 is confirmed on a second window: the
six carried zeros were a query-form artifact, and the correctly-queried probe says "ordinary", not
"absent".**
★ **`credit stress` 0.83× and `layoffs` 0.57× while HY OAS has widened +11bp over three prints** —
**the market is again leading the narrative**, the same shape M153 measured.

### The one 🚨, body-read rather than counted

**CXMT is the report's own #1 story, and it ESCALATED rather than reversed** — which makes this
addendum a confirmation, not a correction. New items in the window:

- *"Chinese DRAM Maker CXMT Is Now Worth More Than **Intel** After Blistering Shanghai Debut:
  **SanDisk, Micron Feel The Heat**"* [yahoo_finance] · *"**Micron (MU) Faces New China Memory
  Pressure As CXMT IPO Tests AI Lead**"* · *"AI Memory Stocks on Rocky Ground: 3 Reasons SK Hynix
  Fell 13%"* · *"What is CXMT, the chipmaker that just became China's most valuable listed company?"*
  [cna, 9,973-char body].
- ★★ **The single most important item is one this desk could NOT read**: **ft, *"The unexpected
  winners from China's blockbuster chip IPO"* — headline only, no body in the corpus.** ⚠ **That
  headline is precisely the shape of S37 branch A** (a funded entrant that *re-rates* rather than
  de-rates). **It is flagged as unread, not summarised from its title** — the D29 discipline.

### ⚠ Two new provider disagreements, declared not resolved (D5)

| Figure | Source A | Source B | Status |
|---|---|---|---|
| CXMT's provincial windfall | **$248bn** [straitstimes] | **$192bn** [bloomberg] | **Same day, same event, a 29% gap. Neither adopted; no windfall figure is used anywhere in this run** |
| CXMT's raise | **$8.6bn** (¥57.92bn, prospectus-sourced via Reuters) | **$9.8bn** [yahoo_finance 07-26] | ★ **RESOLVED, and by a KR measurement**: **M195 measured ¥66.6bn including the greenshoe = ¥57.92bn × 1.1499 = exactly a 15% greenshoe.** $8.6bn is the base, $9.8bn is with-greenshoe. **This run cites the base and says so** |
| (carried from EVENT_ALPHA Card 7) Innolight's HK listing | **$6.8bn** [bloomberg] | **$8.8bn** [thread title] | **Unresolved. The card was written on the direction (priced below max), which both agree on** |

### The US session, live — what changed after the report was written

*"Nasdaq opens lower as **AI worries mount ahead of pivotal earnings**"* · *"S&P 500, Dow Jones trade
flat; **Nasdaq drops over 1% as chip stocks drop**"* · *"**Dow Rises, Nasdaq Sinks As Chipmakers
Dive; Coca-Cola Surges**"* · *"European stocks trade flat as tech selloff offsets earnings boost from
consumer, luxury firms."*

⇒ ★ **A rotation, not a broad risk-off** — the chip complex is down while the Dow and consumer names
are up, which is **consistent with, not contrary to, this report's central reading** (IT's 144pp
internal dispersion; Staples the best single-day sector on the settled bar).
⚠ **These are LIVE intraday observations and are NOT admissible as measurements** (R17/D74). **No
number above is carried into `handoff/`; no verdict in this report is changed by them.**

### What did NOT change, and is therefore re-affirmed

- **P4** — no crack term fired; the settled 3-2-1 buffer of **8.12 points** is untouched.
- **P1/P2** — `credit stress` **0.83×** and no rates term elevated; **HY OAS 2.79%, 31bp from S26's line.**
- **The Hormuz axis** — `Hormuz open` **0.92×**, `ceasefire` 0.97×, `escalation` **0.84× (decelerating)**,
  `transit fee` 1.05×. ⇒ **EVENT_ALPHA Card 2's toll-booth reading is not contradicted**, and the
  de-escalation thread has not accelerated further.
- **S20's verdict** — `guidance cut` 1.06× with no UPS-specific reversal in the window.

### What the next run must re-read first

1. ★ **The ft item *"The unexpected winners from China's blockbuster chip IPO"*** — it is S37 branch
   A's shape and its body is not in the corpus. **Fetch or re-pull it before scoring anything on P9.**
2. **DFII10 and DGS10/DGS2 for 2026-07-27** — they had not published at this run's clock, and **the
   breakeven moved alone (2.26 → 2.21)**. §A-1's implied real 10y of **2.48%** is **arithmetic, not a
   print**, and must be replaced by the actual value.
3. **The eleven brackets settling 07-29 → 08-12**, starting with **FOMC + META + STX + V + GD on
   2026-07-29.**
4. **The UPS earnings-call transcript** — S20's fuel leg is `[partially verified]` (D85).
