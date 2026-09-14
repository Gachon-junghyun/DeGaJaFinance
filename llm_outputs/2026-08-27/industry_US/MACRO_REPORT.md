# MACRO_REPORT — industry_US · 2026-08-27 (Stage 3 / L1·MACRO)

> Run clock **2026-08-27 22:1x KST = 09:1x ET — US pre-market.** Terminal **settled** US equity close
> **2026-08-26**; `n_new_sessions_since_prior_run = 1`. Every price number below is on the 08-26 settled
> close unless it is explicitly stamped **LIVE**. `[FRED]` rate series end **2026-08-25** (see §A-0).
> Analytical output only. No sizing, no buy/sell language (P4).

---

## §0 · Instrument-health line — read before any number

`PREFLIGHT.md` (this run): **G1 FAIL · G2 PASS · G3 PASS · G4 FAIL · G5 FAIL · G6 FAIL · G7 PASS.**

**What this report is therefore forbidden to do**, and does not do anywhere below:
1. 🚫 **No theme-freshness or news-velocity citation** (G1). **`theme-age` was not run and is not quoted** —
   its entire output class is barred. Narrative movement below is carried **only** by `thread`'s
   outlet-count curves and `brief`'s denominators, which are counts, not the velocity axis.
2. 🚫 **No "quiet" / "no news" verdict** on any name or sector. Where a bucket is thin, the **denominator
   is quoted** instead (§B-4).
3. 🚫 **No cross-sectional use of the partial velocity subset** — its coverage is `us_top300` ranks 1–51.
4. 🚫 **`wflow` is not a current weighting** (43-day-old caps). This report uses **price excess returns
   measured against `SPY`, named inline at every use** (§E header and every holdings line), computed
   fresh from settled closes rather than from the sweep's cap-weighted flow, so the constraint does not
   bind here. *(RULE C1 — this bullet names the rule the benchmark attaches to; the benchmark itself is
   `SPY` and is stated here and at every point of use.)*
5. 🚫 **No IC-backed sizing language** anywhere.
6. **Consumer Discretionary, Materials, Energy may not be promoted/demoted on the weighted-flow bucket**
   (G3). §E ranks on price excess and breadth, and says so inline.

⚠ **Standing-verdict baseline, restated so this stage cannot silently move it** (`D358-KR`, five firings
across the two desks, twice caused by a MACRO §E inheriting from the run-before-last):
```
ENRG OW · HLTH OW · MATR N · COMM N · DISC N · FIN N · STPL N− · RE N− · INDU UW− · UTIL UW− · IT UW
```
**`STPL` is `N−`** (demoted by the 08-26 ROTATION), **not `N`.** **`MATR` is `N`, not `N+`.**

---

## §A · ★★★ The one thing this report exists to say

**The inflation binary this desk built four rows and a whole 08-28 cluster around had already printed —
two days early, in line, and unchanged — and the desk's own calendar was still counting down to it.**

**`M977`** `[measured]` **July core PCE printed 2026-08-26**: **+3.3% YoY, unchanged from June, matching
forecast; +0.2% MoM, also matching estimates.** Alongside it: **Q2 GDP unrevised at 1.5%**, and
**consumer spending stalled**. Corroborated across **6 outlets** (`bloomberg` *"US Core PCE Rises 0.2%
in July, Consumer Spending Stalls"* · `seekingalpha` body, quoted verbatim above · `wsj` *"Fed's
Preferred Inflation Gauge Remains Above Target Range"* · `investing_en` · `google_en`/FXStreet ·
`yahoo_finance` live coverage). In the 08-26 `brief` head layer it sits at **14 outlets / 44 articles**
(*"Inflation index prized by Fed holds steady in July"*), the day's **6th-largest cluster**.

**`M978`** `[measured]` **The desk was counting down to an event that had already happened.**
`catalyst_calendar --days 12`, run this morning, still prints **`D-1 2026-08-28 July PCE … 🔀binary
[bea~est]`**. `P86`, registered 08-22, reads *"July PCE, **released 2026-08-28**"*. And the **08-26**
`MACRO_REPORT.md` wrote **"July PCE 08-28"** in **three** separate places — on the morning the number
came out, with the print sitting in that same run's own head layer at 14 outlets, and with the run
starting at 09:1x ET, **after** the 08:30 ET release.
⇒ The `~` on the calendar row (pattern-estimate, not official-source-confirmed) was doing exactly the
job it was designed to do, and **three consecutive stages read past it.** Registered as **`D381`**.

**Why this matters more than a date slip.** The 08-26 run's own summary calls 08-28 *"NINE rows on one
date (`D343`)"* — the densest settle-cluster on the board — and **the PCE leg of that cluster is now
resolved into a non-event**: unchanged YoY, in-line MoM. `P86`'s branch A required core PCE MoM ≤ +0.20
**AND** `DGS2` ≤ 4.10; **the PCE conjunct is met at the published rounding** and the rate conjunct is not
yet readable (§D-1). The binary the desk was hedging **did not deliver a surprise**, and the reaction
went the *hawkish* way anyway: `reuters` 08-26 — *"Fed seen a bit more likely to hike after inflation
data"* [9 articles / 5 outlets].

**And the second load-bearing object of the last three runs finished collapsing in the same session.**
**`M980`** `[measured]` `EW{Consumer Staples + Health Care} − EW{Information Technology}`, 5-session
returns, `us_top300` constituents, settled closes:

| settled date | spread | trailing-252 percentile |
|---|---|---|
| 2026-08-24 | **+9.327pp** | **97.6th** |
| 2026-08-25 | +3.905pp | 85.7th |
| **2026-08-26** | **−0.499pp** | **56.7th** |

**−9.83pp in two sessions — a complete round trip from p97.6 to just above the median.** Trailing-252
mean **−1.089**, sd **4.732**. `P98`'s branch B line is **≤ −1.347 (p50)**; the spread now sits
**0.85pp above it**, having been 10.7pp away two sessions ago. `P98` settles **09-03** and is **not**
scored here.
⇒ **`M944`'s finding is confirmed and extended.** The 08-26 run measured a one-day half-life on this
estimator; the second day removed the remainder. **Two percentile-extreme readings this desk called
load-bearing (`P79`'s +7.9pp roll, `P98`'s p97.6 state) have now both been substantially erased by the
sessions immediately following them.** That is a statement about the **estimator**, not about the
rotation: at sd ≈ 4.7pp per 5 sessions, a p97 print carries roughly one session of information.

---

## §A-0 · Primary indicators `[FRED]` — with their observation dates, not today's date

| series | value | date | 365d percentile | range |
|---|---|---|---|---|
| `DGS30` | **5.17** | **2026-08-25** | 92.0 | 4.54 – 5.31 |
| `DGS10` | **4.64** | 2026-08-25 | 92.0 | 3.97 – 4.75 |
| `DGS2` | **4.17** | 2026-08-25 | 86.5 | 3.38 – 4.37 |
| `DFII10` (real 10y) | **2.32** | 2026-08-25 | 88.3 | 1.67 – 2.47 |
| `T10YIE` (10y breakeven) | **2.32** | **2026-08-26** | **48.4** | 2.18 – 2.50 |
| `BAMLH0A0HYM2` (HY OAS) | **2.70%** | 2026-08-25 | **6.9** | 2.63 – 3.46 |
| `BAMLC0A0CM` (IG OAS) | 0.81% | 2026-08-25 | 68.4 | 0.73 – 0.94 |
| `VIXCLS` | 15.45 | 2026-08-25 | 18.4 | 13.47 – 31.05 |
| `DTWEXBGS` (broad dollar) | **118.06** | **2026-08-21** | **8.1** | 117.44 – 121.92 |
| `NFCI` | **−0.566** | 2026-08-21 | **0.0** (loosest of the series) | −0.566 – −0.459 |
| `SOFR` | 3.64 | 2026-08-26 | 25.9 | 3.50 – 4.51 |
| `DFF` | 3.63 | 2026-08-25 | — | — |

- **`real_10y` is quoted with `breakeven_10y`, per the standing rule.** Real **2.32 at the 88.3rd
  percentile** against a breakeven **2.32 at the 48.4th** ⇒ **the elevated nominal is essentially all
  real.** The market is not pricing more inflation; it is pricing a higher real cost of money. That is
  the same decomposition the 08-25 run made (`P97`), and one settled session later it is unchanged.
- **Credit axis cited explicitly, and it refuses the risk-off story**: **HY OAS 2.70% at the 6.9th
  percentile of 365 days**, 7bp off its own low; **`NFCI −0.566` is the loosest reading in the entire
  57-observation series (0.0th percentile).** 🚫 **Any "financial conditions are tightening" claim in
  this run would be narrative-only, and none is made.** The tightening is **in the long rate alone**,
  not in credit or in aggregate financial conditions — those are two different objects and they
  currently disagree.
- **Curve**: `30y − 2y` = **+1.00** at the last joint date (08-25).
- ⚠ **`D333` reproduces for a 10th time and it is now blocking a row twice.** The rate block ends
  **08-25** while `T10YIE` and `SOFR` carry **08-26** and `DTWEXBGS` stops at **08-21** — a five-day
  spread across one "macro snapshot". **`P77` cannot be read** (needs a `DGS30` bar covering 08-26);
  **`P97` cannot be read** (needs dollar and `DGS10` on a *joint* date ≥ 08-28, and the dollar leg is
  seven days behind). Both stay `ARMED`. See §D-1.
- ⚠ **CPI and M2 are monthly and lag ~1 month.** They are not quoted as current conditions anywhere.

---

## §B · The tape, read before it is ranked

### B-1 · Denominator, corrected and quoted (`brief --date 2026-08-26 --scope foreign --body 2`)
| field | value |
|---|---|
| `denominator.articles` | **5,026** |
| `excluded_not_news` | **{} — empty; nothing was removed, so 5,026 is the corrected figure** |
| clusters | 1,424 |
| `events_2src_plus` / `market_events` | **792 / 792** (`nonmarket_events` 0) |
| head (≥5 outlets) / body (≥2 outlets) / **tail** | 102 / 690 / **0** |
| `single_source_clusters` | **632**, of which **15 shown** |
| `subevents_recovered` | **259** |

🚨 **`tail = 0` is NOT the coverage claim, and here is what was still withheld**: **617 of 632
single-source clusters (97.6%) were not displayed**, and the non-market band showed **0 of 0**. The
head+body layers cover **792 of 792 market events (100%)**, so the two-outlet-plus universe is fully
seen; **the unseen mass is entirely the one-outlet tier.** ⇒ **no claim anywhere in this report that a
bucket was empty rests on the tail count**; §B-4 quotes bucket denominators instead.
⚠ This is the **`D339` class on the foreign feed** — the single-source display cap, not a Korean-
classifier artifact, because `nonmarket_events` is 0 here.

**Today's own day (2026-08-27) is a PARTIAL DAY and is labelled as such** (`D373-KR`'s rule, applied):
`thread`'s per-day denominators read **08-21 771 · 08-22 288 · 08-23 323 · 08-24 792 · 08-25 829 ·
08-26 792 · 08-27 409** ⇒ **08-27 is 51.6% of the prior settled day, below the ~60% bar.** Every
`FADING` tag below is therefore checked against whether it also falls on the **full** 08-26 day.

### B-2 · The 08-26 head layer — what actually happened (102 clusters, top by outlet count)
| # | outlets | cluster | axis |
|---|---|---|---|
| 1–2 | **19 / 18** | Meta settles social-media-addiction suits, **$16.7–18bn** + heavy teen-user restrictions | regulatory / COMM |
| 4 | 15 | **"Oil falls as Strait of Hormuz talks advance"** | oil |
| 5 / 10 / 14 / 52 / 102 | 14 / 13 / 12 / 6 / 5 | **`NVDA` FQ2 print**: beats, **guides $108bn next quarter**, **projects ~70% FY2028 revenue growth** | AI-compute |
| 6 / 20 / 80 | **14 / 9 / 5** | **July core PCE holds steady; GDP unrevised 1.5%; "Fed seen a bit more likely to hike"** | inflation |
| 7 / 82 | 14 / 5 | **US–Canada bracing for a prolonged trade dispute**; *"Canadians unite in fury"* | trade |
| 11 | 13 | **"Iran, Oman Agree to Temporary Strait of Hormuz Deal"** | oil |
| 12 | 13 | Wheat rallying to new highs as Russia escalates | commodities |
| 30 / 73 | 12 / 5 | **Australia inflation overshoots, boosting hike bets**; **"ECB may raise rates in September as Iran war fuels inflation"** | global inflation |
| 39 / 45 / 71 / 55 | 7 / 7 / 5 / 6 | **Long-end sell-off**; *"a chorus of market pros is criticizing the Treasury's plan to tame the bond market"* | rates |
| 41 / 44 | 7 / 7 | **Warsh's Jackson Hole debut**; peers to highlight global inflation risk | Fed |
| 62 | 6 | **"Soaring Diesel Prices Are Helping Oil Companies and Hurting Consumers"** | refining |
| 89 | 5 | **"Marvell Reports Thursday"** — i.e. **today** | AI-semis |
| 33 / 68 / 26 | 8 / 6 / 8 | Anthropic–Nscale **$45bn** compute deal · SoftBank mulls **$20bn** bond for OpenAI · SpaceX **$100bn** Starship spaceport | AI capex |
| 17 | 10 | FDA approves a pancreatic-cancer drug | HLTH |

### B-3 · Trajectories (`thread --days 7 --scope foreign`) — every proposition below carries one
4,204 daily events → 3,221 threads (528 multi-day, **154 alive**, 2,693 one-day of which 244 new today).

| thread | curve (outlets/day) | tag | reading |
|---|---|---|---|
| **Canada retaliatory tariffs** | 11→24→20→21→**29**→14→7 | **FADING** | ✅ **not** a partial-day artifact — it halves on the **full** 08-26 day (29→14). The peak was 08-25 |
| **US threatens toughest sanctions yet against Iran** | 9→6→6→**17**→14→4 | **ENDED** | `S119`'s subject; the presser cycle is over |
| **Iran, Oman temporary Hormuz deal** | 9→**13** | **ENDED** | a two-day burst that ended at its peak — a resolution, not a fade |
| **Inflation index prized by Fed holds steady in July** | 2→3→**14** | **ENDED** | the PCE print itself, ending at its peak = a completed event |
| **Bond yields rise despite Treasury efforts to curb borrowing** | 5→2→3 | **REIGNITED** | `P77`'s subject is **alive again**, not resolved |
| **Iran threatens 45 tankers with fines/confiscation** | 5→3 | **REIGNITED** | the escalation leg survives the ceasefire headline |
| **Soaring diesel prices helping oil companies** | 3→6→3 | **FADING** | `P83`'s subject; the fade is on the full 08-26 day |
| **`NVDA` 70% FY2028 growth forecast** | 5→6 | **BUILDING** | the print's *forward guide*, not the print, is what is still spreading |
| **Stock market today (index wrap)** | 4→6→7 | **BUILDING** | index-wrap boilerplate; carried for denominator only, not read as content |

🚨 **The ENDED tags on the two Iran threads are the single most important trajectory fact in this
table, and they point in opposite directions to each other**: the *sanctions-escalation* thread ended
after peaking at 17 outlets, while the *Hormuz-deal* thread ended **at** its peak of 13 — and a
**REIGNITED** tanker-threat thread sits underneath both. ⇒ **the oil-geopolitics variable is
oscillating, and this report registers both branches rather than banking one** (the recurring failure
class this stage is told to watch).

### B-4 · Seven-bucket sweep — **terms passed as separate argv**, OR-mode, `--scope foreign`, 3 days
| bucket | terms (separate argv) | hits |
|---|---|---|
| inflation | `PCE` `inflation` `price index` | **1,869** |
| rates | `Treasury` `yield` `bond market` | **2,870** |
| Fed | `Warsh` `Jackson Hole` `FOMC` | **775** |
| oil | `Hormuz` `OPEC` `crude` `refinery` | **1,164** |
| trade | `tariff` `Canada` `trade war` | **1,627** |
| AI capex | `data center` `AI capex` `accelerator` | **2,605** |
| credit | `credit spread` `high yield` `default` | **418** |

⚠ **No bucket is near zero, so no "quiet bucket" claim is made or needed.** The lowest is credit at
**418 hits over three days** — 🚫 **this is NOT written as "credit is quiet"**; it is written as *"the
credit bucket's denominator is 418, and the credit **instrument** (HY OAS at the 6.9th percentile,
§A-0) is what refuses the stress story."* Narrative and instrument agree here, which is the only reason
the conclusion is admissible.
⚠ Terms were passed as **separate argv**, never quoted as one string — the failure mode that silently
returns ~0 and gets read as calm.

### B-5 · Blind-spot pass (`blindspot --days 2 --scope foreign`)
Emerging-token table is dominated by proper nouns already in the term set (`Trump` 422 · `Iran` 414 ·
`China` 384 · `Bitcoin` 284 · `Canada` 247 · `Meta` 224 · `Fed` 221 · `Inflation` 171). The random
sample surfaced nothing that overturns a bucket. **One item is worth folding into the living term
table**: `investing_en` 08-26 *"Retail margin ceilings: who still has room to grow and who has already
peaked"* — a **peak-margin** framing arriving on the consumer complex from outside this desk's terms,
on the same day `L2`'s peak-margin lens fired on `NVDA` (§C-2). ⇒ **term added: `margin ceiling`.**
🚫 No freshness score is attached to it (G1).

---

## §C · Propositions

### C-1 · Inherited propositions — status, not re-argument

| id | settles | status this morning |
|---|---|---|
| `P77` | first `[FRED]` close covering **08-26** | 🚫 **UNREADABLE for a 2nd run** — `DGS30` ends 08-25 (`D333`, 10th). Last published **5.17, which sits 1bp inside branch A (≤5.18)** — **stated, not scored** |
| `P83` | **08-27 close** | ⚠ **at severe artifact risk — see §C-3** |
| `P86` | July PCE + `DGS2` at first close covering 08-28 | **PCE conjunct MET** (+0.2% MoM ≤ +0.20). Rate conjunct unreadable. **`DGS2` 4.17 vs A ≤ 4.10 / B ≥ 4.32** — 7bp from A, 15bp from B. Stays ARMED |
| `P90` | the 08-26 print | ✅ **SCORED `FIRED-A`** by this run's HANDOVER — see §C-2 |
| `P91` | first business-day run on/after **08-31** | not due (`D309` clause) |
| `P96` | **08-27 close** | ⚠ **at severe artifact risk — see §C-3** |
| `P97` | first joint date ≥ 08-28 | unreadable; the dollar leg is at **08-21** |
| `P98` | **09-03** | state **−0.499pp (p56.7)**, **0.85pp above branch B**. See §A |
| `P100` `P101` `P102` | 09-01 / 09-04 / 09-09 | armed, not due |

### C-2 · `P90` scored `FIRED-A` — and it is the regime call's first forward test

**`M979`** `[measured]` `NVDA` FQ2 FY2027 (quarter ended 2026-07-26), printed 08-26 AMC:
- Revenue **$96.22bn** — **SEC XBRL primary**, against the press figure $96.2bn (`module_fundamentals_us`
  also reports **yfinance ↔ XBRL agreement on 4 of 4 quarters within 5%**). More than doubled YoY.
- **Gross margin 75.0%**, vs **74.9%** the prior quarter and **72.4%** a year earlier ⇒ **+10bp QoQ.**
- **FQ3 gross-margin guide ~74.0%** ⇒ **−100bp from the quarter just reported.**
- Next-quarter revenue guide **$108bn**; FY2028 revenue growth guided **~70%** against a street **44%**.
- **Long-run gross-margin outlook reset to 72–73%** (earnings-call transcript, `seekingalpha` 08-26).
- The cause is **named in the documents, not inferred**: memory/DRAM cost, quantified in one body as
  *"a 2% gross margin hit from DRAMs."*

⇒ **Branch A on both conjuncts** (guide ≤ reported: −100bp ✅; reported ≤ prior + 50bp: +10bp ✅).
**Pass-through, not pricing power. The cost curve is binding.**

★ **This is the first forward observation that tests the standing regime call**, which is carried
`[inferred]` and predicts exactly this: *memory's level is tight while its rate decelerates ⇒
pass-through.* **It agreed.** 🚫 **One observation is `n = 1` (`S5`) and does not promote the call from
`[inferred]` to `[measured]`** — the call's own designated test remains **`MU`'s 09-24 print**. But the
direction of the evidence is recorded, and the desk's own `L2` (peak-margin trap) has now fired on the
**epicenter of the #1 cycle**, not merely on the refiners.
⚠ **`S115`'s joint-scoring obligation is outstanding** — branch A *with* margin expansion falsifies
`P90`; branch A *with* flat margin confirms it. `S115` needs tonight's close. **Named, not dropped.**

### C-3 · 🚨🚨 `P103` — REGISTERED: the two rows settling tonight will settle on a contract roll

> Registered **before** the settle, not discovered at scoring. **No threshold is re-banded** (`D242`):
> `P96` and `P83` settle **exactly as registered**. What is registered here is the **artifact**, with
> its decomposition, so tonight's verdicts are read with their contamination already measured.

**`M981`** `[measured]` **The RBOB Sept→Oct roll landed on the 2026-08-27 bar.** Settled futures
closes, `yfinance`, `auto_adjust=False`:

| | 08-25 | 08-26 (settled) | **08-27 (LIVE)** | 1-session Δ |
|---|---|---|---|---|
| `CL=F` | 82.36 | 82.23 | 82.49 | **+0.32%** |
| `HO=F` | 4.2438 | 4.2600 | 4.0910 | **−3.97%** |
| `RB=F` | 3.2529 | **3.3201** | **2.9591** | **−10.87%** |

**Gasoline falls 10.87% on a day crude rises 0.32% — an 11.2pp one-session divergence between a refined
product and its own feedstock.** That is a contract change, not a margin event. It is the **same class**
the 08-26 run identified as `D368` on its own LIVE bar and withdrew its figure over; **the roll has now
arrived in the bar the two rows settle on.**

**Leg decomposition of the 3-2-1 crack's one-session move** (70.373 → 57.672 = **−12.701**), each leg
moved alone:
- **`RB=F` leg −10.069 = 79.3% of the entire move**
- `HO=F` leg −2.342 = 18.4% · `CL=F` leg −0.290 = **2.3%**

**Consequence for `P96`** (5-session crack rate on settled closes; branch A ≤ **−2.887**, B ≥ **+0.468**):

| computed on the 08-27 bar | 5-session rate | which branch |
|---|---|---|
| **as printed** | **−8.584** | **deep inside A** |
| with `RB=F` held at its 08-26 level | **+1.485** | **inside B** |
| with `RB=F` and `HO=F` both held flat | +3.827 | inside B |

🚨 **The roll alone moves `P96` across the entire C band, from branch B to branch A.**

**Consequence for `P83`** (distillate−gasoline spread `(HO−RB)×42`, change from the 08-20 settle of
**51.131**; A ≥ **+4.0**, B ≤ **−4.0**):

| | spread | change from 08-20 | branch |
|---|---|---|---|
| settled 08-26 | 39.476 | **−11.655** | **deep inside B** |
| **LIVE 08-27** | 47.594 | **−3.578** | **C** |
| 08-27 with `RB=F` flat | — | −18.682 | B |

🚨 **And the roll moves the two rows in OPPOSITE directions**: `P96` toward **A** ("the refining kill
deepens") and `P83` out of **B** into **C** ("no capacity-destruction verdict"). **Both would be
artifacts of one contract change**, and read together they would tell a story that is not in the data.
**Neither row's anti-signal contains a roll clause** — this class was not anticipated at registration.

**`P103` — ★★★ Was the 08-27 refining signal the margin, or the contract?**
| | |
|---|---|
| **Frozen observable** | the 3-2-1 crack **5-session rate on settled closes**, at the **2026-09-02** close — by which date the 08-27 roll is **four sessions behind** and no longer inside the 5-session window |
| **Branch A (the collapse is real)** | ≤ **−2.887** (the same trailing-252 p15 `P96` uses) — the margin is genuinely being repriced and `P96`'s tonight-verdict, whatever it is, was pointing at something |
| **Branch B (it was the contract)** | ≥ **+0.468** (trailing-252 p50) — the whole move was the roll, and `P96` will have settled on an artifact |
| **Branch C** | between |
| **`D93` executed BEFORE freezing** | trailing 252 of the 5-session crack rate, computed this run on settled bars to 08-26: **mean +0.785 · sd 4.563 · p15 −2.887 · p50 +0.463**. Current settled reading **+2.728 = 71.8th percentile** ⇒ **A ≈15% · B ≈50% · C ≈35%. B is the favourite and is disclosed** — and B is *also* the branch that would indict this desk's own instrument, which is why it is registered |
| **State at registration** | **settled 08-26 rate +2.728**, i.e. **already above branch B's line** — disclosed. ⚠ The observable is the **forward** 09-02 reading and this value is not it |
| **Anti-signal (VOID)** | an **OPEC+ emergency production decision** or a **US SPR action** inside 08-27 → 09-02. ⚠ **Base rate**: no OPEC+ ministerial is scheduled in the window. **The Hormuz negotiation is deliberately NOT an anti-signal — it is the event** (the designed-to-void defect that killed `S91`/`S93`) |
| **Information content (`L3`)** | **Both branches change a conclusion.** A says the refining thesis has a real commodity signal and the roll merely amplified it. **B says the desk's crack instrument produced a false regime marker on the exact night two registered rows settled on it** — which retires the 5-session-rate counter as a usable trigger for the third time in six weeks |
| **Non-redundancy (`D343`)** | 09-02 currently carries **`AVGO`'s print and `S109`**, both single-name equity rows. **`P103` is the only commodity row on that date**, and it deliberately avoids 08-28 (nine rows) and 09-01/09-04/09-09 (`P100`/`P101`/`P102`) |
| **Owner** | `industry_US` |

★ **Note what this row does NOT do.** It does not re-band `P96` or `P83`, does not void them, and does
not pre-judge tonight's verdicts. It creates a **second, roll-free observation** of the same underlying
question, so that a contaminated settle is detectable rather than authoritative.

### C-4 · `P104` — ★★ The inflation print was a non-event; did the front end believe it?

**Claim.** July core PCE came in **exactly as forecast and unchanged** (`M977`), and the tape's read was
**hawkish** (*"Fed seen a bit more likely to hike after inflation data"*, `reuters`, 5 outlets), with
**Australia's CPI overshooting** and **ECB September-hike chatter** in the same 24 hours (12 and 5
outlets). Against that, `DGS2` **fell** 7bp into the print (4.24 → **4.17** on 08-25). **The narrative
and the front end are pointing opposite ways**, and `P86` cannot arbitrate because its rate leg is
unreadable.

| | |
|---|---|
| **Frozen observable** | `DGS2` `[FRED]`, at the **first published close dated ≥ 2026-09-02** |
| **Branch A (the front end prices a hike)** | `DGS2` ≥ **4.32** (its 274-obs max is 4.37) |
| **Branch B (the front end reads the print as benign)** | `DGS2` ≤ **4.08** |
| **Branch C** | between — **the favourite, disclosed** |
| **`D93` executed BEFORE freezing** | `DGS2` trailing 274 obs: range **3.38 – 4.37**, current **4.17 = 86.5th percentile**. Its own 5-observation change over the trailing window has sd ≈ 7bp ⇒ **±15bp / −9bp bands are ≈1–2σ**; **A ≈12% · B ≈20% · C ≈68%.** ⚠ **The bands are deliberately asymmetric because the state is not centred** — 4.17 sits nearer B's line than A's, and that is disclosed rather than hidden by a symmetric band |
| **Anti-signal (VOID)** | an **intermeeting Fed action**, or a **BLS/BEA restatement of the July PCE**. ⚠ Base rate low; keyed to a **publication or policy event**, not to commentary. **Warsh's Jackson Hole speech content is explicitly NOT a voider** — it is the mechanism under test |
| **Information content (`L3`)** | **A** falsifies the "benign print" reading and puts a hike back on the desk's rate axis, which would move every duration-sensitive verdict (`RE N−`, `UTIL UW−`). **B** says the hawkish tape was noise and `P86`'s branch A completes |
| **Non-redundancy (`D343`)** | `P86` uses `DGS2` at *the first close covering 08-28* with a **PCE conjunct**; `P104` uses a **later, clean date and no conjunct**, so it is readable even if `D333` blocks `P86` again. **`P91` (08-31+) pairs `DGS2` with `DGS30`**; this row is front-end-only. 09-02 avoids the 08-28 nine-row cluster |
| **Thread** | *"Bond yields rise despite Treasury efforts to curb borrowing"* — **REIGNITED, 5→2→3 outlets** |
| **Owner** | `industry_US` |

### C-5 · `P105` — ★★ Information Technology's two horizons say opposite things, and the desk is `UW`

**Claim.** On this run's own settled 08-26 frame (§D), **IT is the board's best 20-session sector
(`exc20` +6.708) and its worst 60-session sector (`exc60` −9.176)** — a **15.9pp** gap between two
windows of the same basket, with **41 of 56 names negative on 60d** but **only 20 of 56 on 20d**. The
desk carries **`IT UW`**, and `C16` is exactly this disagreement in a different pair of instruments.

| | |
|---|---|
| **Frozen observable** | `EW{us_top300 Information Technology, n=56}` **20-session excess vs `SPY`**, settled closes, at the **2026-09-09** close |
| **Branch A (the 20-day leadership is a turn)** | ≥ **+7.50pp** — it extends beyond today's reading |
| **Branch B (the 60-day trend reasserts)** | ≤ **+1.00pp** |
| **Branch C** | between |
| **`D93` executed BEFORE freezing** | current **+6.708**; the sector's own `exc5` is **+0.955** and `exc1` **+0.901**, i.e. the 20-day figure is **not** being driven by the last session. Branch A asks for roughly +0.8pp of further widening over 9 sessions; branch B asks for a 5.7pp give-back. On the sector's realised 20-day excess dispersion this run (**median +0.715 vs mean +0.955**, right-skewed), **A ≈30% · B ≈25% · C ≈45% — disclosed, and C is the favourite** |
| **Anti-signal (VOID)** | a **GICS reclassification moving ≥3 of the 56 constituents**, or a **trading halt** in the sector's top-5 names. ⚠ **MSCI's 08-31 quarterly review falls inside the window and is explicitly NOT a voider** — it does not change GICS assignment (the same ruling `P98` made) |
| **Information content (`L3`)** | **A falsifies `IT UW` outright** on the horizon the desk's own DEEP work uses. **B falsifies the 20-day reading that `C16`'s `eqflow` half rests on**, and would resolve `C16` by measurement rather than by preference — which is what `C16` says it needs |
| **⚠ `W5`** | this is a sector aggregate; the 08-26 DEEP measured a **10.36pp software−hardware gap** inside it. **A and B are both readable at the aggregate**, but neither may be read as a statement about a node |
| **Non-redundancy (`D343`)** | 09-09 carries `P102` (Materials two-name spread) and `S128` (`rs60` reversal basket). **`P105` is the only single-sector-aggregate row on that date**, and `S128`'s basket is cross-sector by construction |
| **Thread** | no single thread owns this — **stated explicitly** rather than assigned a proxy. The `NVDA` FY2028-guide thread (**BUILDING 5→6**) touches it but is one name |
| **Owner** | `industry_US` |

---

## §D · Positioning, and the two instruments that keep disagreeing with their own labels

**`M984`** `[measured]` CFTC COT (Tuesday close, **3–4 day lag — context, not a trigger**):

| instrument | net spec | weekly Δ | 1yr %ile | tool's label |
|---|---|---|---|---|
| S&P 500 e-mini | **−10,560** | **−21,840▼** | **84** | 🟢 crowded-long |
| Nasdaq-100 | −12,067 | +30,838▲ | **4** | 🔴 crowded-short |
| Russell 2000 | −15,706 | −1,763▼ | 15 | 🔴 crowded-short |
| **UST 10Y** | **−946,961** | −31,908▼ | **5** | 🔴 crowded-short |
| UST 2Y | −927,337 | +93,706▲ | 70 | 🟡 neutral |
| USD Index | +19,079 | −2,330▼ | 76 | 🟡 neutral |
| WTI | +29,164 | +5,938▲ | 36 | 🟡 neutral |
| Nat Gas | −203,503 | −6,368▼ | **0** | 🔴 crowded-short |
| **Copper** | +79,748 | −640▼ | **100** | 🟢 crowded-long |
| Gold | +222,189 | +4,249▲ | 48 | 🟡 neutral |

- 🚨 **`D327` reproduces for a 6th run**: the S&P 500 row is labelled **🟢 crowded-long on a net spec of
  −10,560, i.e. net SHORT**, while carrying the largest weekly swing on the board (−21,840). **The label
  is not used anywhere in this report; only the percentile and the net figure are.**
- **Copper sits at the 100th percentile for a 5th consecutive run** — `P102` (09-09) owns it.
- **The rates picture is internally consistent for once and it cuts against the tape**: `UST 10Y` specs
  are at the **5th percentile (crowded short)** while `DGS10` sits at the **92nd percentile of yield**.
  🚫 Context, not a trigger — but it means the long-end sell-off narrative (§B-2, four head clusters) is
  arriving into positioning that is **already** maximally on that side.
- ⚠ **US has no investor-type feed.** This is the substitute, and it is **positioning, not flow.**

**`M982`** `[measured]` 🚨 **A new silent instrument defect, found while decomposing the roll**: the
**2026-08-26 futures volume row is byte-identical to 2026-08-25 on all three legs** — `CL=F` **282,408**,
`HO=F` **20,491**, `RB=F` **28,601**, twice. Daily volume does not repeat to the unit across two
sessions. **The provider is carrying 08-25's volume forward onto the 08-26 bar.** The *closes* differ
(82.36 → 82.23), so the price series is not obviously duplicated — but **any volume-derived reading on
the 08-26 futures bar is unusable**, and this run makes none. ⇒ **`D382`**.

---

## §E · ★ Sector transmission matrix — all 11 GICS, one line each

> **ROTATION's input. Wind direction only — not a ranking, and not a verdict.**
> **`exc*` are equal-weight `us_top300` constituent baskets, excess vs `SPY` (named inline), computed by
> this run from settled closes through 2026-08-26.** `SPY` itself: **+0.022% (1) · −0.387% (5) ·
> +5.020% (20) · +0.994% (60).**
> 🚫 **The sweep's `wflow`/`eqflow` are NOT used here** — G5 makes the cap weights 43 days old and G3
> bars three sectors from the weighted bucket entirely. Ranking below is on **price excess + breadth**,
> which both constraints leave intact. **The standing verdict column is the 08-26 ROTATION's, restated;
> this stage proposes a wind direction and does not move a verdict.**

| GICS sector | standing | exc1 | exc5 | exc20 | exc60 | med5 | neg5/n | wind, and the proposition driving it |
|---|---|---|---|---|---|---|---|---|
| **Energy** | **OW** | **+1.109** *(best on board)* | **−1.040** *(worst)* | +2.084 | **+10.102** | −0.706 | 9/16 | **Both-sided and deliberately so.** The barrel sold on the Hormuz deal (ENDED at peak, 13 outlets) while the tanker-threat thread REIGNITED. `P100` owns the 20-day leadership question; **`P103` now owns whether the refining signal is real or a contract roll** |
| **Health Care** | **OW** | −0.462 | +0.170 | −0.315 | **+14.028** *(best)* | +0.252 | 14/32 | **Hold the direction.** The 60-day leadership is the board's largest and is not a one-session artifact; the 5-day is flat. FDA approval at 10 outlets is idiosyncratic, not a sector driver. No proposition moves it this run |
| **Information Technology** | **UW** | +0.901 | +0.955 | **+6.708** *(best)* | **−9.176** *(worst)* | +0.715 | 22/56 | 🚨 **The board's sharpest internal contradiction and the desk is short it. `P105` registered** to settle it on 09-09. `C16` is the same disagreement in the flow instruments |
| **Financials** | **N** | −0.045 | **+2.105** | −2.211 | **+12.469** | +1.446 | 11/47 | **Positive wind, unowned.** 2nd-best on both exc5 and exc60 with the board's 2nd-best 5-day breadth (11 of 47 negative = 23.4%). Nothing this run brackets it |
| **Materials** | **N** | +0.187 | **+3.144** *(best)* | −0.796 | +4.091 | +2.215 | **3/12** *(best breadth)* | **Positive wind.** ⚠ **G3 flipper** (`LIN`) — the weighted-flow bucket may not carry it; this line is price-and-breadth only, stated inline. **Copper COT at the 100th %ile for a 5th run** is the other half. `P102` (09-09) owns it |
| **Consumer Staples** | **N−** | −0.192 | +0.939 | **−8.867** *(worst)* | +2.859 | +0.858 | 4/19 | ⚠ **The 08-26 demotion and this frame disagree on the short horizon**: `exc5 +0.939` with only 4 of 19 negative, against the worst `exc20` on the board. **Not re-litigated here** — flagged for ROTATION with both numbers |
| **Comm Services** | **N** | −0.602 | +1.379 | −0.635 | −0.151 | +1.546 | 5/12 | **Un-measurable by rule for a 9th run** (`D297`: `GOOGL`+`GOOG` ≈ 76.6% of 12 names). The Meta settlement (**$16.7–18bn, 19 outlets, the day's #1 cluster**) lands here and is **not** priced into a sector claim |
| **Real Estate** | **N−** | −0.522 | +0.230 | −6.427 | +3.927 | +0.786 | 5/12 | **Neutral-to-soft wind.** The duration story is contradicted by `exc60 +3.927`; the 08-26 DEEP already found the binding constraint is **not** rates |
| **Consumer Discretionary** | **N** | **−0.866** *(worst)* | −0.067 | −4.220 | +3.430 | **−1.227** | 16/28 | **Soft wind.** ⚠ **G3 flipper** (`AMZN`) — weighted-flow bucket barred; price and breadth are what carry this line, stated inline |
| **Industrials** | **UW−** | +0.803 | −0.678 | −3.184 | +4.490 | −0.062 | **26/50** *(worst breadth)* | **Soft, and the trade thread is FADING off a 29-outlet peak.** ⚠ **The 09-08 Canadian retaliation date is bracketed only by `S123` (09-12)** — `D342`'s gap, 3rd run |
| **Utilities** | **UW−** | +0.436 | −0.643 | −7.735 | +0.060 | −1.338 | 11/15 | **Soft on every horizon that matters.** 2nd-worst `exc20`, worst-but-one 5-day breadth. Nothing disagrees; nothing to resolve |

**Wind summary for ROTATION** — *not verdicts*: positive wind on **Materials, Financials, Health Care**;
negative wind on **Utilities, Industrials, Consumer Discretionary**; **Energy and IT are the two sectors
where the horizons disagree with each other**, and both now carry a registered row (`P103`, `P105`).

---

## §F · Self-backtest — this desk's own hit rate, and it says the bands are too tight

**`M986`** `[measured]` Parsed the **MASTER scoring log** in `handoff/SCENARIOS.md` for every row that
carries a verdict, latest verdict per row ID:

| verdict | rows | share |
|---|---|---|
| `FIRED-A` | **19** | 27.5% |
| `FIRED-B` | **18** | 26.1% |
| `FIRED-C` | **21** | 30.4% |
| `VOID` | 8 | 11.6% |
| `EXPIRED` | 3 | 4.3% |
| **total distinct scored rows** | **69** | |

🚨 **Reading, and it is uncomfortable: excluding voids and expiries, the tails fire 37 of 58 = 63.8% of
the time, while a typical registration discloses C at 35–80%.** Row after row in this desk's own files
says *"C is the heavy favourite"* — and **C is the least common outcome.** Two readings, both live:
**(a)** the `D93` baselines are computed on trailing windows whose volatility is lower than the realised
regime, so ±1σ bands are effectively ±0.6σ; **(b)** the regime genuinely is more volatile than the
trailing 252 sessions it is calibrated against. **Either way, "C is the favourite" is a claim this desk
has been making and its own scoreboard has been refuting.** ⇒ registered as **`D383`**.
⚠ **Method limit, stated (`C3`)**: this is a regex extraction over a markdown log, taking the **latest**
verdict per ID. It cannot see rows recorded in prose rather than a table, and it does not distinguish
US-owned from KR-owned rows. **It is quoted as an order-of-magnitude self-check, not as a precise hit
rate**, and the two desks' rows are pooled — which `W1` would forbid if this were a market claim. It is
a claim about **this repo's registration practice**, which is shared, so pooling is admissible here.

---

## §G · Catalysts injected (`catalyst_calendar --days 12`) — and one the calendar cannot see

**5 binaries in window ⇒ PREMORTEM must bracket each both ways.**

| when | event | source flag |
|---|---|---|
| **D-1 2026-08-28** | **July PCE** | 🚨 **`[bea~est]` — and it ALREADY PRINTED 08-26** (`M977`/`M978`). The remaining 08-28 content is the rate leg of `P86`, not a new print |
| **D-1 2026-08-28** | `FRO` earnings | 🔀 binary; `S109` armed. `FRO` is **outside `us_top300`** (`D341`) |
| **D-6 2026-09-02** | `AVGO` earnings | 🔀 binary; **held name**; `S127` armed; **`P103` now also settles 09-02** |
| **D-8 2026-09-04** | Aug NFP | 🔀 binary; `P101`/`S126` settle |
| undated | Iran "Strait of Hormuz open" statement (TACO trigger) | 🚨 **arguably FIRED**: *"Iran, Oman Agree to Temporary Strait of Hormuz Deal"*, 13 outlets, 08-26 (§B-3). The row is undated by construction and **cannot be scored**; recorded as a state change |
| D-4 2026-08-31 | MSCI quarterly review | structural; **explicitly not a GICS reclassification**, so it voids nothing |

🚨 **`MRVL` reports TODAY (2026-08-27) and the calendar does not carry it** — `S116` brackets it
(settles 08-28) and the 08-26 `brief` head layer carries *"Marvell Reports Thursday"* at 5 outlets.
**`D294`'s family, 9th run**: the calendar misses a dated print on a name the desk has an armed row for.
**Recovered from the tape, not from the tool.**

---

## §H · IDs registered this run (MACRO stage)

> ⚠ **ID 3-grep executed at WRITE time** across `handoff/*.md` · `llm_outputs/**` · `REPORT/**`,
> excluding this run's own files: **`P103` `P104` `P105` → 0 hits · `M977`–`M986` → 0 hits ·
> `D381` `D382` `D383` → 0 hits.** Highest before this append: **`P102`** · **`M976`** (allocated by
> this morning's `industry_kr` run — **`D76`'s collision class checked and avoided for a 4th day**) ·
> **`D380`** (allocated by this run's own HANDOVER).

- **Measured**: `M977` PCE print · `M978` the calendar/row date error · `M979` `NVDA` FQ2 · `M980` the
  defensive−AI spread round trip · `M981` the RBOB roll decomposition · `M982` duplicated futures volume ·
  `M983` the settled sector frame (§E) · `M984` COT · `M985` `[FRED]` percentiles (§A-0) · `M986` self-backtest.
- **Propositions**: `P103` (09-02) · `P104` (09-02) · `P105` (09-09). **All three deliberately avoid
  08-28** (`D343`, nine rows) and each states its non-redundancy inline.
- **Digs**: `D381` (the desk counted down to a print it had already published), `D382` (duplicated
  futures volume), `D383` (C is disclosed as the favourite and is the least common outcome).

---

## ✅ EXIT CHECK
- [x] Catalysts injected (`--days 12`, extended past the default because armed rows sit beyond it);
      narrative read as **events + trajectories + 7-bucket + blind-spot**; indicators read (FRED
      primaries + COT positioning); **daily anchor = the previous run's `MACRO_REPORT.md`, read** (§0
      restates its verdict line; §A measures how much of its governing fact survived).
- [x] Events read via **`brief --body 2`, `tail = 0`** — and **`tail = 0` is explicitly NOT claimed as
      coverage** (§B-1): 617 of 632 single-source clusters withheld, 792 of 792 market events shown.
- [x] **Denominator quoted after `excluded_not_news`** — which was **empty**, so 5,026 is the corrected
      figure, and that is stated rather than assumed.
- [x] Trajectories read (`thread --days 7`): **every proposition carries a thread tag + curve or states
      "no thread" explicitly** (`P105` does the latter). The two **ENDED** threads under live oil
      propositions are flagged as staleness signals, and today's 51.6% partial-day denominator is
      quoted before any FADING tag is used.
- [x] **Every "nothing in bucket X" claim carries its denominator** — and none is made; the thinnest
      bucket (credit, 418) is written as a denominator plus an instrument, not as "quiet".
- [x] **No bucket's hit count came from a quoted multi-word string** — all terms passed as separate argv.
- [x] **Both halves of the headline print cited**: core PCE **+3.3% YoY *and* +0.2% MoM**, on the same
      release; GDP unrevised 1.5% quoted beside it; `NVDA` **75.0% GM *and* the 74% forward guide.**
- [x] **Every relative-performance number names its benchmark inline** (`vs SPY`, stated in §E's header
      and on each holding). No statistical result is carried across markets — `C15` is explicitly left
      un-transferred (`W1`).
- [x] **Credit axis read and cited**: HY OAS **2.70% at the 6.9th percentile**, NFCI **−0.566 at the
      0.0th**. The report's only credit statement is that the stress story is **refused** by these.
- [x] **`real_10y` quoted with `breakeven_10y`** — 2.32 (p88.3) vs 2.32 (p48.4) ⇒ the move is real, not
      inflationary.
- [x] Transmission matrix produced — **all 11 sectors, one line each** (§E), on price excess and breadth,
      with the two G3-barred sectors flagged inline.
- [x] Self-backtest computed and appended with its method limit (§F).
- [x] New blind-spot term folded into the living table (`margin ceiling`), with **no freshness score
      attached** (G1).
- [x] Linter — see the ADDENDUM below.

---

## §5 · POST-RUN ADDENDUM — appended by the DRIFT stage (append-only; nothing above is rewritten)

> `drift_watch.py --report llm_outputs/2026-08-27/industry_US/MACRO_REPORT.md`
> ⚠⚠ **Declared deviation, 9th consecutive run: the watch ran at +0.6h, not the +3–6h the stage
> specifies.** Consequence, stated rather than implied: **tonight's `MRVL` print — this run's own D-0
> binary — falls entirely outside the window by construction**, as do the seven rows settling at the
> 08-27 close. **The window is short because the run is scheduled pre-market, which is `D355`'s clock
> defect seen from the other end.**

### §5.1 · Kill-switch burst: ✅ NONE
`drift_watch` reports **no kill-switch term burst** in the 0.6h since the report's baseline. No
regime-flip early warning fired. ⇒ **no correction to §A, §C or §E is triggered by a burst.**

### §5.2 · Every registered VOID clause probed — **none fired**, and two were body-read rather than counted

| row | clause | probe | verdict |
|---|---|---|---|
| **`P103`** | OPEC+ **emergency production decision** or a **US SPR action**, 08-27 → 09-02 | `OPEC`+`emergency` **13 hits**; `Strategic Petroleum Reserve` **27 hits** | 🚫 **DOES NOT FIRE — body-read, not counted.** The `OPEC`/`emergency` hits are **`fxstreet` boilerplate** (*"How does OPEC influence the price of WTI Oil?"* repeated inside three price-forecast pieces) — the `D367` class. The SPR hits are commentary on the reserve's **level**, not an action: `reuters` 08-24 *"Oil stocks in US Strategic Petroleum Reserve fall by 3.7 million barrels to lowest level since 1982"*; `yahoo_finance` 08-25 *"America's Strategic Petroleum Reserve Is Running on Fumes."* **A depleted reserve is not an SPR release.** |
| **`P104`** | **intermeeting Fed action**, or a **BLS/BEA restatement of the July PCE** | `intermeeting` **0 hits**; `PCE`+`revision` **44 hits** | 🚫 **DOES NOT FIRE.** Zero intermeeting hits. The revision hits are **Q2 GDP price-index revisions, not a July-PCE restatement** — see §5.3, which is a correction to this report rather than a void |
| **`P105`** | GICS reclassification moving ≥3 of 56 IT constituents, or a **trading halt** in the top-5 names | `trading halt` **78 hits** | 🚫 **DOES NOT FIRE.** No hit names an IT top-5 constituent; the term is generic market vocabulary. ⚠ Probed by count only — **stated as the weaker test it is** |
| **`S129`** | agricultural **carve-out announced before 09-08**, confirmed in ≥2 outlets, or an `ADM`-specific dated corporate action | `carve-out`+`agricultural` **1 hit** | 🚫 **DOES NOT FIRE** — one hit is below the ≥2-outlet bar the clause sets |
| **`S130`** | a **company statement** denying the deal, or a separate `NVDA` transaction ≥$10bn | the four 08-27 bodies (`cnbc`, `techcrunch`, `fortune`, `yahoo_finance`) all read *"report says"/"reports"* | 🚫 **DOES NOT FIRE.** ⚠ **And the absence of a company statement is the row's own leg 1**, not a void — that distinction was written into `S130` at registration precisely so this ambiguity could not be improvised at scoring |

### §5.3 · 🚨 This stage REFUTED a sentence this report wrote three sections earlier — appended, not edited (`§4c`, `D48`)

**What §A asserted**: *"Alongside it: **Q2 GDP unrevised at 1.5%**"* — sourced from the 08-26 headline
*"US inflation remains sticky in July; 2nd-quarter GDP unrevised at 1.5%"* [9 outlets].

**What the VOID probe turned up one stage later**: `fxstreet` 08-26, *"Dow Jones Industrial Average
ignores a revision made of inflation"*, body: **"Every second-quarter price line revised up, real growth
left at 1.5%."**

⇒ **Both statements are true and mine was the incomplete half.** "GDP unrevised at 1.5%" refers to
**real** growth. **The Q2 price deflators WERE revised UP**, and that is the hawkish half of the same
release — **the half a report arguing "the print was a non-event" most needed to state.** §A's sentence
is **left standing** with this correction attached beneath it.
⚠ **It does not overturn §A's conclusion** — core PCE was still +3.3% YoY unchanged and +0.2% MoM in
line, which is what "non-event" was about — **but it does strengthen the hawkish reading §A already
flagged** (`reuters`: *"Fed seen a bit more likely to hike after inflation data"*) and therefore
**strengthens `P104`'s branch A** without moving its threshold (`D242`). ⇒ **`M996`.**
★ **Note where it came from**: not from a burst detector, but from **body-reading a VOID clause's own
hits.** The anti-signal probe found a fact about the report rather than about the market — which is an
argument for body-reading every clause even when the counts look like noise.

### §5.4 · One structural asymmetry that no registered row owns — carried, not bracketed
`reuters` 08-24: the **SPR is at its lowest level since 1982**, down 3.7m barrels. `P103` correctly does
**not** fire on it (a level is not an action), and no other row owns it either.
⇒ **A depleted SPR removes the government's principal instrument for capping an oil spike**, which is a
one-sided change to the **upside tail** of the desk's Energy `OW`. **The 08-26 run recorded the identical
gap (`M957`) and it is unowned for a 2nd consecutive run.** 🚫 **Not bracketed here** — a bracket needs a
dated observable and this has none. **Named so it stays visible rather than being rediscovered.**

### §5.5 · What DRIFT did not reach
- 🚨 **Tonight's `MRVL` print, and the seven rows settling at the 08-27 close** (`S79` `S81` `S115`
  `S117` `S119` `P83` `P96`) — **all outside a +0.6h window by construction.**
- 🚨 **The RBOB roll contaminating `P96`/`P83` at that settle** (`M981`) is a **pre-registered** warning
  from §C-3, not a DRIFT finding — DRIFT confirms only that nothing has changed it in 0.6h.
- **No WebSearch was run** at any point in this run; every body above came from the local/remote news
  index.
