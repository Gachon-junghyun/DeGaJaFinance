# MACRO_REPORT — industry_US — 2026-07-25 (Sat)

> Stage 2/10. Wind direction only. **Zero buy/sell language, zero sizing (P4).**
> Every relative number names its benchmark inline (**C1**). Every print quotes both halves (**C2**).
> Flow tags are absent by design — SWEEP owns them and they are C-grade (**D6**).

**Run clock: 2026-07-25 22:0x–22:5x KST = 09:0x–09:5x ET, Saturday. US market CLOSED.**
**Every price number below is the settled 2026-07-24 (Fri) close.** There is no incomplete bar in
this report and none is cited. ★ **The 07-24 session has never been read by any US run** — the three
prior US runs all fired pre-open and inherited the previous close.

---

## §0 · Catalyst injection `[catalyst_calendar --days 10]`

Run at 22:2x KST. **13 binaries in a 10-day window.** Per the protocol, every one ≤48h must be
bracketed both ways by PREMORTEM; nothing here may be tilted one-way.

| Kind | D- | Date | Event |
|---|---|---|---|
| MACRO | **D-4** | 2026-07-29 | **FOMC decision (Warsh, no SEP)** `[fed ✓]` |
| MACRO | D-5 | 2026-07-30 | June PCE `[bea ✓]` |
| MACRO | undated | `[blank]` | Iran "Strait of Hormuz open" statement `[news 👁]` |
| EARN | D-4 | 2026-07-29 | META |
| EARN | D-5 | 2026-07-30 | VLO · STNG · MA |
| EARN | D-10 | 2026-08-04 | AMD · ANET · MPC |
| STRUCT | D-4 | 2026-07-29 | SK hynix ADR↔ordinary conversion `[news ✓]` |
| STRUCT | D-4 | 2026-07-29 | KR financial-holdco governance reform `[news ~est]` |
| STRUCT | D-6 | 2026-07-31 | SK이터닉스 KKR SPA closing `[dart ~est]` |

### ⚠ D18 fires a **SIXTH** consecutive time — and this time it misses the *next* event on the board

Verified by string search of the regenerated `CATALYST_WATCH.json`: **`UPS` absent · `MSFT` absent ·
`AMZN` absent · `AAPL` absent · `KT` absent · no `2026-07-28` row of any kind.**

- The calendar's **earliest binary is D-4 (07-29)**. **`SCENARIOS.md` S20 is UPS Q2 on 2026-07-28 = D-3.**
  The instrument that exists to tell the desk what fires next does not contain what fires next.
- **MSFT and AMZN are two of the three subjects of S13**, the scenario the desk has itself flagged as
  bracketing the branch nothing else in the book brackets. Neither is listed.
- ⇒ **Binding on every downstream stage: `CATALYST_WATCH.json` is a supplement to `SCENARIOS.md`,
  never a substitute.** A stage that reads only the calendar this run reads a board with its first
  three days blank.

### ⚠⚠ NEW — the calendar is propagating a **retracted** claim into today's run

The 07-29 SK hynix row carries, verbatim: *"전환 개시로 차익거래가 열리면 프리미엄이 붕괴한다"*
(conversion opens arbitrage → the premium collapses).

**That is R13**, retracted 2026-07-24 on named primary testimony from the institution that operates
the step (KSD president 이윤수: the ceiling is **2.5%**, not 25%; 07-29 is a **registration** date;
*"because the ADR premium is so high there will be no conversion demand for the time being"*).

This is a **new failure class, distinct from D18**: not a missing row but a **stale row that a
machine regenerates every run**, so a retraction filed in `handoff/` does not reach the artifact
downstream stages actually read. Registered as **dig D51**. The row is **not cited** in this report.

---

## §A · Regime primaries `[FRED]` — pulled this run, 120-day window

| Series | Latest | `asof` | Prev | 120d range | State |
|---|---|---|---|---|---|
| **DGS10** | **4.71%** | 2026-07-23 | 4.67 | [3.97, **4.71**] | **120-day HIGH** |
| **DGS2** | **4.37%** | 2026-07-23 | 4.31 | [3.38, **4.37**] | **120-day HIGH** |
| **DGS5** | **4.46%** | 2026-07-23 | 4.41 | [3.51, **4.46**] | **120-day HIGH** |
| DGS30 | 5.17% | 2026-07-23 | 5.15 | [4.64, 5.18] | 1bp off the high |
| **DFII10 (real 10y)** | **2.43%** | 2026-07-23 | 2.39 | [1.72, **2.43**] | **120-day HIGH** |
| **T10YIE (breakeven)** | **2.26%** | **2026-07-24** | 2.28 (07-23) | [2.18, 2.50] | **FALLING** |
| **BAMLH0A0HYM2 (HY OAS)** | **2.77%** | 2026-07-23 | **2.68** | [2.63, 3.46] | **+9bp — the first material widening in 5 runs** |
| BAMLC0A0CM (IG OAS) | 0.79% | 2026-07-23 | 0.78 | [0.73, 0.94] | +1bp |
| NFCI | −0.552 | 2026-07-17 | −0.539 | [−0.564, −0.454] | still **loosening**, 1.2bp off its loosest |
| VIXCLS | 18.70 | 2026-07-23 | 16.64 | [15.03, 31.05] | +12.4% |
| DFF | 3.63% | 2026-07-23 | 3.63 | [3.62, 3.64] | flat |
| **DTWEXBGS** | **120.5315** | **2026-07-17** | — | [117.44, 121.41] | **UNPRINTED 9 calendar days — S12 still PENDING** |
| CPILFESL (core CPI) | index 336.065 | **2026-06** | 336.121 | — | **−0.02% MoM / +2.57% YoY** (both halves, C2) |
| CPIAUCSL (headline) | index 332.568 | **2026-06** | 333.979 | — | **−0.42% MoM / +3.46% YoY** (C2) |
| UNRATE | 4.2% | **2026-06** | 4.3 | [4.1, 4.5] | −0.1 |

⚠ **Staleness declared, not papered over**: CPI/UNRATE are **June** prints (~1-month lag). NFCI is
weekly, `asof` 07-17. **DGS10/DGS2/DFII10 have no 07-24 print yet** — the H.15 series lag the tape by
a business day, so §A's curve is a **07-23** read while §B's tape is **07-24**. Two `asof` values run
through this report and are labelled at every use.

### §A-1 ★★ The whole curve made a 120-day high together, and the breakeven went the other way

**10y, 5y, 2y and real-10y are all at their 120-day maximum on the same date**, while the 10-year
breakeven **fell** 2.28 → 2.26 (and its `asof` is a day *newer*, 07-24). The move is therefore
**real, not inflation-expectational** — approximately 100% of it, versus ~79% when this was first
decomposed on 07-20 (M20).

- **This does not confirm P1's *cause*, only its *composition*.** A real-yield-led move is consistent
  with a reaction-function repricing (P1) **and** with a term-premium/supply story (R11's dead
  framing) **and** with a growth repricing. The breakeven only rules out the *inflation-expectation*
  channel. **C4: `indistinguishable` among the surviving three.**
- **S9's kill line (real 10y > 2.55%) is 12bp away** and has closed 4bp since 07-22.
- The tape corroborates and then eases: `^TNX` **4.703 (07-23) → 4.679 (07-24)**, i.e. the long end
  gave back 2.4bp on the settled Friday. FRED cannot confirm that until Monday.

### §A-2 ★ Credit moved — for the first time in five runs — and one day is not a trend

**HY OAS 2.68% → 2.77% = +9bp on 2026-07-23.** That is the largest single-day widening in the carried
window and it takes the series **14bp off its 365-day low (2.63)**.

**Both halves (C2), because one number here would mislead:**
- Widening: HY **+9bp**, IG **+1bp**, VIX 16.64 → **18.70 (+12.4%)**.
- Not widening: HY is still at **2.77% against a 120-day max of 3.46%**; IG **0.79%** is 5bp off its
  own 365-day low; **NFCI is still loosening** (−0.552, `asof` 07-17), a 5th consecutive week.

★ **This settles a half-scored pre-registration from the 07-24 run.** That run wrote: *"VIX +12.4%
while HY fell 1bp ⇒ equity-only stress so far; HY's 07-23 print is unpublished, score the other half
next run (C3 — `unknown`, not `resolved`)."* **The print has now arrived and it scores against the
provisional reading**: HY widened **+9bp on the same session** the VIX rose. **There was no
dispersion — there was a publication lag.** Recorded as a scored half, not quietly dropped.

⇒ **P2's kill line (HY OAS > 3.10%) is un-tripped** and P2 survives a 6th run — but for the first
time its KPI is moving against it rather than making new lows. **C3: whether 07-23 is a turn or a
tick is `unknown`; the 07-24 HY print resolves it and does not exist yet.**

---

## §B · Positioning `[COT, CFTC — Tue-close, 3–4d lag ⇒ context, never a trigger]` + `[FINRA]`

| Instrument | Net spec | Wk Δ | 1yr %ile | Read |
|---|---|---|---|---|
| **Nasdaq-100** | −9,691 | +621▲ | **5%ile** | 🔴 **crowded SHORT** |
| **S&P 500 (E-mini)** | −16,784 | +22,154▲ | **84%ile** | 🟢 crowded long |
| Russell 2000 | +6,758 | +6,655▲ | 88%ile | 🟢 crowded long |
| **UST 10Y** | −879,706 | −48,031▼ | **12%ile** | 🔴 **crowded SHORT** |
| UST 2Y | −1,154,597 | +2,880▲ | 53%ile | 🟡 neutral |
| USD Index | +15,614 | +2,441▲ | 66%ile | 🟡 neutral |
| **WTI Crude** | +20,039 | +256▲ | **11%ile** | 🔴 **crowded SHORT** |
| **Nat Gas** | −171,138 | +7,474▲ | **11%ile** | 🔴 crowded SHORT |
| **Copper** | +73,977 | +9,592▲ | **98%ile** | 🟢 crowded long |
| Gold / Silver | +183,910 / +23,465 | ▼ / ▼ | 23 / 32%ile | 🟡 neutral |

### ★★ The board's sharpest positioning fact is *inside* equities, not between assets

**Nasdaq-100 sits at the 5th percentile of a year (crowded short) while the S&P 500 sits at the 84th
(crowded long) — a 79-percentile-point spread inside the same asset class**, four days before
MSFT/META/AMZN print. Speculators are positioned for the index and against the thing that dominates
the index.

⚠ **Read as context, per the module's own caveat and the REJECTED-ledger precedent on Copper.** An
extreme percentile is contrarian *ammunition*, not a direction. It is registered here because it is
the cleanest available statement of **what the market is not positioned for** going into S13/S16/S19,
which is precisely PREMORTEM's input.

- **UST 10Y at the 12th percentile, and shorts ADDED 48,031 into the week** — speculators pressed a
  short into a 120-day-high yield. Same structure: crowded, therefore ammunition in both directions.
- **WTI at the 11th percentile (crowded short) — and this week the tape went the shorts' way**:
  Brent $100.69 → **$96.78 (−3.88%)**, WTI $92.19 → **$89.31 (−3.12%)** on the settled 07-24. A
  crowded short that starts working is not a squeeze setup; it is a trend the desk is on the wrong
  side of if it holds the OW for the war-premium reason.

### FINRA short-volume `[demoted to a note per M95 — baseline artifact, `[inferred]`]`

`asof` 2026-07-24. **MSFT z −2.82** and **META z −2.35** (both 🟢 short-vol collapse, 5v5 trend
falling) **into their own 07-29 prints**; **DLR z −2.44** on its earnings day; **UNP z −2.41**
(5v5 −11.8▼). Refiners are unremarkable (VLO −0.10, MPC −1.15, PSX +0.18, XOM −0.32).

⚠ M95 measured this axis to be a **baseline artifact** — MPC and PSX printed identical short-volume
shares on one day and scored z −3.29 vs −0.25. **No proposition in this report rests on it.**

---

## §C · Narrative axis `[news, --scope foreign, hard rule]`

### §C-0 · Denominator, stated before any "quiet"/"loud" claim

`brief --body 2 --scope foreign`: **828 articles → 144 events → 144 market / 0 non-market.**
Tiers: head (≥5 outlets) **16** · body (2–4) **128** · tail (2 outlets) **0** · single-outlet
**15 shown of 239** · non-market boundary band **0 of 0** · sub-events recovered **31**.

⚠⚠ **`tail = 0` is NOT a coverage claim, and on this desk the gap is structural.** The tool states
plainly that the **239 single-outlet rows have no score at all** — the classifier is Korean-only, so
on the US feed the single-source tier is not "low-ranked", it is **unmeasured**, and only a random
15 are displayed. ⇒ **93.7% of the tier where FX and rates primaries habitually print is unseen this
run, by construction, not by truncation.** Any "nothing in bucket X" claim below is bounded by that.

⚠ **Saturday denominator.** 07-25 carried **144 events against 764–949 on the surrounding weekdays**
(07-21 949 · 07-22 816 · 07-23 860 · 07-24 764). That is **~17% of a weekday**. Per the L2's own
warning this **inflates FADING and deflates outlet counts** — so a 6-outlet event today is
proportionally a far larger event than a 6-outlet event on Thursday, and no FADING tag in §C-2 is
treated as informative.

### §C-1 ★★★ The day's regime item — $950bn of US–Korea memory supply commitments

Head, **12 articles / 6 outlets** on a 144-event Saturday, with two sub-events
(*"Samsung Elec wins $200 billion Broadcom AI chip partnership"* 4/3 · *"SK Group and NVIDIA Expand
Strategic Partnership Across AI"* 3/3). Body-read in full `[news — Reuters, citing South Korean
presidential adviser Kim Yong-beom; NOT a company disclosure, NOT an 8-K]`:

- Samsung + SK hynix will pursue US memory supply partnerships valued at a **combined $950 billion**.
- **SK hynix ≈ $750bn** to US companies including NVIDIA, **"through long-term agreements."**
- **Samsung ≈ $200bn** to **Broadcom (AVGO)**.
- A **separate SK hynix initiative >$500bn** with NVIDIA and others, covering next-generation memory
  and large AI data centres.
- **SK Telecom to build a 2-gigawatt facility** on NVIDIA Vera Rubin + SK hynix **HBM4**, **phase 1
  operating 2027**.
- Samsung and SK hynix have **also discussed supply agreements with Anthropic**.
- Korean officials: **US companies account for 80–90%** of the demand behind Korea's planned
  semiconductor expansion.
- Context: announced at President Lee Jae Myung's San Francisco AI summit (NVIDIA, OpenAI, Anthropic,
  Broadcom attending); the "San Francisco AI Declaration."

**Thread: BUILDING, 3 days, outlets 3 → 2 → 6, 23 items** (07-20 *"AMD, Micron, SK Hynix lead chip
stock recovery"* → 07-24 *"Samsung, SK Hynix to Ink Large Chip Supply Deals with US"* → today). Early
in its runway by the L2's own criterion, not a day-5 crowded story.

**What this is, and what it is not — the regime call turns on this distinction (STANDING_VIEW §4):**

- ✅ **It is the fifth independent confirmation of the VOLUME leg** (after 2Q GDP, 1–20th exports,
  Alphabet's capex raise, and CSP demand — M58). It is by some distance the largest.
- ❌ **It cannot un-measure M1/M2/M18.** The disclosed figures are **notional volume/value; no price
  term, no ASP, no floor and no escalator is disclosed anywhere in the body.** Per §4's asymmetry, a
  volume commitment moves the *timing* of the margin call, never the call itself.
- ★★ **It is nonetheless the single largest datapoint C1 has ever had.** C1 is the open contradiction
  *"LTA price floors cap the upside (TrendForce) and floor the downside (Micron management) —
  unmeasured."* A **$750bn** book "through long-term agreements" is exactly the instrument C1 is
  about. **It remains unmeasured**: the announcement tells us the LTAs are enormous and tells us
  nothing about their price terms. **C1 is carried, not resolved — and dig D1 just became the highest-
  value open dig on the board.**
- ⚠ **Grade and reflexivity.** `[news]`, one wire (Reuters) re-syndicated, sourced to a **government
  adviser** rather than to either issuer. No DART/8-K confirmation exists at run time. A $950bn number
  announced at a state summit is a **political artifact until an issuer discloses it**, and this desk
  has been burned once already this month by a headline number that did not survive its primary
  (R17). **Registered as scenario input, not as evidence.**
- ⚠⚠ **Do not read the price stubs in the article.** The body's quote widget shows SKHY −8.81% /
  005930.KS −7.59% / 005935.KS −7.33%. Those are the **2026-07-24 KR closes** (they match M114's
  삼성전자 −7.6% exactly) — i.e. **the session BEFORE the announcement.** They are not a reaction to
  it. Flagged because this is precisely the mismatched-bar trap that produced R17.

### §C-2 ★★ C6 measured a FOURTH time — and the probe is now measuring the desk, not the market

| Probe term | d1 | d7 | 90d total | 7d avg |
|---|---|---|---|---|
| **`capex cut`** (C6's registered probe) | **0** | **1** | **5** | 0.1 |
| `margin drag` | **0** | 1 | 2 | 0.1 |
| `spending discipline` | 0 | 2 | — | — |
| `capex discipline` | 1 | — | — | — |
| **`overbuild`** | **7** | **32** | — | — |
| **`digestion`** | **84** | — | — | — |
| **`AI spending`** | **259** | — | 1,403 | 93.1 |
| `capex` | — | — | 2,154 | 129.6 |
| `free cash flow` | — | — | 2,586 | 180.4 |

**And the branch acquired a front page today**: *"Corporate America Has Suddenly Decided to Stop
Blowing Money on AI"* — **WSJ, 2026-07-25** (carried by wsj + google_en syndication ⇒ effectively
**one source**, `[news, title-only — WSJ bodies are not scraped]`).

⇒ **C6's registered observable has returned ~0 for four consecutive measurements while the branch it
was built to detect is being narrated at 259 hits in 24 hours under a different name and on the front
page of the WSJ.** M82 predicted this in general terms ("the un-narrated branch has acquired a
vocabulary, and it is not the desk's"); today it is specific and quantified.

**This is a measurement defect, not a market observation. Registered as dig D52.** The correct
restatement: C6's *finding* — that this branch cannot be anticipated from the desk's news axis —
**stands and is stronger than ever**; C6's *instrument* — the literal phrase `capex cut` — should be
retired in favour of the measured vocabulary (`AI spending`, `overbuild`, `digestion`,
`spending discipline`). ⚠ **The retirement is not executed in this report** (it changes a carried
contradiction's definition and belongs to a human/HANDOVER decision); the defect is logged.

⚠ **What does NOT change**: S13's observable is a **line item** (MSFT/META capex guidance), not a
term count. Nothing here makes the news axis a substitute for it.

### §C-3 · The rest of the day, by tier — every head line read, not the top of it

**Head (16 events, ≥5 outlets):**
- **Warsh/FOMC — REIGNITED, 6 days, outlets 5→5→5→9→5→5, 62 items.** Today: *"Prediction: Kevin Warsh
  and the FOMC…"* [9/5] with a sub-event *"Kevin Warsh Just Vowed to Bring a 'Regime Change' to the
  Fed"* [3/3]. **The only continuously-alive macro thread into D-4.**
- **Houthi missile strikes on southern Saudi Arabia** [9/7], sub-event *"Saudi-led coalition attacks
  Yemen's Hodeida port"* [3/2]. The oil-risk axis is alive on the event tier while the price fell.
- **NAVER, NVIDIA and Brookfield to expand Korea's National AI [infrastructure]** [9/5] — BUILDING
  2 days (3→5), alongside *"India's HCLTech to invest $1.48 billion in AI data centres"* [6/3].
- SpaceX Starship launch [8/7] · Bitcoin 30-day high >$65,000 [13/6] · *"The AI jobs apocalypse
  probably isn't coming anytime soon"* [8/7] · *"Better AI Buy: Micron vs …"* [6/6] · India education
  minister resigns [12/8] · wildfires France/Spain [5/5].

**Body (128 events, 2–4 outlets) — the tier that carries this run's price-relevant items:**
- ★ **"Oil Slips From $100 As OPEC Signals More Supply"** [6/4] `[news, title-only]`, alongside
  **"OPEC+ Set to Raise Output Again — Even as Members Can't Pump It"** [yahoo_finance/oilprice,
  07-23]. **This is the only narrative on the board that matches the tape's direction** (§B, §D-P4).
- *"Why Apple Stock Is Up Today"* [8/4] — AAPL was the day's 2nd-best large cap (+1.49σ), with a
  sub-event *"Trump Caught Between Apple and Micron in Fight Over Chinese [chips]"* [2/2].
- *"Verizon Just Signed a More Than $1 Billion Dark Fiber Deal"* [5/3] · *"Blackstone, KKR and
  Brookfield take Kuwait pipelines stake"* [4/4] · *"Oracle Is Spending Billions on AI. Why It Might
  Not Pay Off."* [4/3] — a third distinct instance of the §C-2 vocabulary.
- *"Amazon CEO Jassy may deliver a July 30 AWS earnings shock"* [2/2] — ⚠ **and it dates AMZN to
  07-30, which the catalyst calendar does not contain at all** (§0).
- *"Iran war live: Trump says US 'locked and loaded'"* [4/3] · *"China economic growth set to slow in
  H2"* [4/3].

**Single-outlet (15 of 239 shown — a random sample of an unscored tier):** *"Defense tech investors
thought the war in Iran could make [them rich]"* [fortune] · *"A Rogue Hack and China at the Door
Spark a Great AI Panic"* [wsj] · *"Can Japan avoid a Liz Truss-style shock as its PM embarks…"*
[guardian] — the **third** consecutive run in which the Japan-duration channel (P6) appears only in
the unscored tier. · *"Heat Bakes Central US, Raising Energy Demand"* [bloomberg].

**Blind-spot pass.** `blindspot --scope foreign` ran (122,611-article blind pool, 400-row random
sample); its emergent-token list is dominated by generic tokens (AI 9,963 · Iran 4,977 · Earnings
4,671) and produced **no new macro term** at day resolution. One sample row is worth carrying:
*"Tesla Misses Badly on Earnings as Free Cash Flow Turns Negative"* [yahoo_finance, 07-23] — a fourth
instance of the §C-2 vocabulary, on a name already carrying −14.52%.
⚠ **`burst --scope foreign` FAILED twice (read timeout to the news API).** Retried once per the run
rules; logged as a failed lookup. The day-resolution burst axis is **missing from this run**, so the
"no new term" claim above rests on `blindspot` alone and is weaker than a normal run's.

---

## §D · Macro propositions — falsifiable · both branches · anti-signal · KPI · dated catalyst

**P1 — The front-end repricing is a real-rate reaction-function trade; its narrated trigger is oil,
and that trigger just reversed without the rates having yet responded.** *(carried, 4th framing)*
- Anchor `[FRED, 07-23]`: **2y 4.37% · 5y 4.46% · 10y 4.71% · real 10y 2.43% — all four at 120-day
  highs on the same date**, against **breakeven 2.26% and FALLING** (`asof` 07-24). Against **core CPI
  −0.02% MoM / +2.57% YoY** and **headline −0.42% MoM / +3.46% YoY** (both halves, C2), UNRATE 4.2%.
- Anchor `[news]`: the Warsh thread is REIGNITED at 62 items over 6 days, the only continuously-alive
  macro thread into the 07-29 FOMC. Carried `[news]`: CME hike odds **10.7% → 34.7%** (M69), TD
  Securities on record that the driver is oil and that the pricing is *"the second-largest deviation
  between market pricing and actual Fed action in the past decade."*
- ★ **What is new, and it is a live test rather than a restatement**: **oil fell 3.1–3.9% on the
  settled 07-24** (§D-P4). If M69's causal claim (oil → hike pricing) is right, the front end must
  give some of this back. **FRED has no 07-24 print, so this is UNSCOREABLE at this run's clock —
  logged as `unknown` (C3), not as either outcome.** The tape's partial answer: `^TNX` 4.703 → 4.679.
- **Both branches (mandatory — oscillating variable):** (a) the FOMC holds, oil keeps falling and the
  2y retraces → this was positioning into an event and TD was right; (b) **the 2y closes >4.45% or
  real 10y >2.55%** → duration de-rate becomes a regime call and S9 fires.
- **Anti-signal (kills P1):** 2y **<4.15%**, **or** the decomposition flips to real-down/breakeven-up.
  Neither fired; the breakeven leg moved further *for* P1 (2.28 → 2.26).
- KPI: **DGS2 daily** · DFII10 quoted **with** T10YIE · 2s10s · CME hike odds · **the oil→2y
  pass-through test above**.
- Catalyst: **FOMC 2026-07-29 (D-4, = S19's hike branch)** · **June PCE 2026-07-30 (D-5, = S15)**.

**P2 — Credit is still the loudest narrative and the quietest market — but its KPI moved against the
proposition for the first time in six runs.** *(carried, 6th run, first adverse tick)*
- Anchor `[FRED]`: **HY OAS 2.68% → 2.77% = +9bp (07-23)**, IG 0.78 → 0.79, **NFCI −0.552 still
  loosening** (`asof` 07-17), VIX 16.64 → 18.70.
- ★ **A pre-registered half is scored here, not dropped**: the 07-24 run recorded *"VIX +12.4% while
  HY fell 1bp ⇒ equity-only stress"* and flagged HY's 07-23 print as unpublished. It has printed.
  **HY widened +9bp on the same session. There was no dispersion — there was a publication lag**, and
  the provisional reading is corrected.
- Direction: **still no credit-market warrant for a risk-off discount** — 2.77% against a 120-day max
  of 3.46% and an NFCI that is still easing. Any credit-stress claim downstream that does not cite HY
  OAS or NFCI is labelled **narrative-only**.
- **Both branches:** (a) spreads hold <3.00% → cyclicals and financials keep the benefit of the doubt;
  (b) **HY OAS >3.10%** → the narrative was early and the earnings-now tilt is re-cut.
- **Anti-signal:** HY OAS **>3.10%** on a close, **or** NFCI rising two consecutive weeks.
- ⚠ **C3 — the honest state is `unknown`:** one +9bp day is a tick, two is a turn, and the 07-24 print
  does not exist yet. **Pre-registered now so the next run scores it rather than narrating it:**
  **HY OAS on 2026-07-24 ≥ 2.85% ⇒ "turn"; ≤ 2.72% ⇒ "tick"; in between ⇒ `AMBIGUOUS`.**
- KPI: HY OAS daily · NFCI weekly. Catalyst: FOMC 07-29 · PCE 07-30.

**P3 — ★★ SELF-SCORING: the 07-23 supplier/spender split reversed sign the very next session. The
"structural split" reading is not supported; `indistinguishable` was the correct call.**
- **What was written 07-24** (P3): suppliers **median +2.98pp vs SPY**, spenders **mean −3.09pp**,
  **spread +6.07pp**, tagged **n≈1 (S1)** and **`indistinguishable` (C4)**.
- **What the settled 07-24 session says** `[measured, own calc, benchmark **SPY +0.10%** named inline
  per C1]`:

| Leg | Names | Session | Excess vs **SPY** |
|---|---|---|---|
| **Suppliers** | MU **−6.99%** · AMAT **−4.72%** · LRCX **−4.56%** · KLAC **−3.75%** | all negative | **median −4.74pp** |
| **Spenders** | GOOGL **+0.65%** · MSFT **+0.03%** · AMZN **−0.66%** · META **−1.80%** | mixed | **mean −0.55pp** |
| **Spread** | | | **−4.20pp** |

⇒ **+6.07pp → −4.20pp: a 10.27pp sign reversal in one session.** The KPI P3 registered flipped
against it immediately.
- ★ **This is a win for the process, not for the proposition.** The C4 tag and the n≈1 warning were
  attached at registration; had P3 been written as a verdict, the desk would have carried a
  "structural split" into ROTATION on evidence that lasted exactly one day. **Logged as the first
  case in this ledger where the C4 discipline demonstrably prevented a bad carry.**
- ⚠ **And the σ correction (M72) applies to the reversal too**: SOXX **−4.40% = −1.13σ**, MU
  **−6.99% = −1.09σ**, AMAT −0.77σ, LRCX −0.82σ, KLAC −0.61σ **on their own 20-day σ of 3.9–6.4%.**
  In σ terms this was **an ordinary day for the supplier leg**, not a rout. Anyone quoting "semis
  −4.4%" without its σ is repeating the error M72 was written to stop.
- Direction: **Info Tech's single label is NOT resolved in either direction and the tilt stays N.**
  The split mandate handed to ROTATION is **weakened, not withdrawn** — the registered test is S13's
  cross-condition on **07-29**, which is 4 days away and unaffected by two contradictory sessions.
- **Both branches:** (a) MSFT/META raise capex 07-29 and the spender multiple compresses while
  suppliers hold → S13 branch A, IT must be split; (b) the spenders re-rate on the same raise → the
  single label survives and both the 07-23 and 07-24 sessions were noise.
- **Anti-signal (kills P3):** a capex **cut** at MSFT or META — which breaks the volume and price legs
  together (§4) and would hit suppliers harder than spenders. ⚠ **Un-narrated by the desk's probe and
  loudly narrated by the market's** (§C-2): watch the **line item**, not the feed.
- KPI: the **supplier-minus-spender excess-vs-SPY spread, σ-normalized**, tracked daily.
- Catalyst: **MSFT + META 2026-07-29 (D-4)** · **AMZN 2026-07-30** `[news: "July 30 AWS earnings
  shock", 2 outlets — and absent from CATALYST_WATCH]`.

**P4 — ★★ The refining margin's RATE has turned negative on settled weekly closes for the first time
in the six-week run-up, and the bottleneck that the thesis rests on narrowed for the first time.**
*(carried from 07-24, direction unchanged, state materially changed)*
- Anchor `[measured, own calc, **settled** yfinance CL/RB/HO continuous — settled-only is now a rule,
  not a preference (R17)]`:

```
              WTI     Brent    3-2-1 crack   gasoline crack   distillate crack   diesel−gas gap
2026-07-22    86.83    94.07      66.865          56.587            87.420           30.83
2026-07-23    92.19   100.69      66.492          54.659            90.157           35.50
2026-07-24    89.31    96.78      64.304          53.318            86.275           32.96
   07-24 Δ   −3.12%   −3.88%     −3.29%          −2.45%            −4.31%           −7.16%
```

- ★★ **The distillate leg fell HARDER than the gasoline leg (−4.31% vs −2.45%), so the diesel-minus-
  gasoline gap NARROWED 35.50 → 32.96.** Every prior session in this stretch widened it. **The
  Atlantic-basin middle-distillate bottleneck — the mechanism the entire refining thesis rests on —
  loosened for the first time.** Independently corroborated across desks: the KR run measured the same
  session as *"crack −11.27% with diesel bottleneck −7.90%, first co-fall"* (M114) on its own basis.
- ★★ **Weekly, settled**: the complete trading week **07-20→07-24 mean 67.043 vs 67.647 = −0.89% WoW**,
  acceleration **+9.21% → −0.89% = −10.10pp**. ⚠⚠ **Stated with R17-b's correction built in**: this is
  **the first negative weekly delta of the six-week run-up (06-08→07-19: +4.43, +4.68, +13.03, +7.56,
  +3.48, +9.21)** — it is **NOT** "the first in the series." Since April there have been **7 negative
  weeks of 17**. R17-b was retracted for exactly the claim this sentence is careful not to make.
- **The level is still high**: crack **64.30 = 88.9th percentile of 90 days** (250d percentile 96.0).
  **Level at the top, rate at zero and now below it** — lens **L1**, the same second-derivative
  structure as memory (M1/M18), in a second industry.
- Anchor `[news, title-only]`: *"Oil Slips From $100 As OPEC Signals More Supply"* [6/4] ·
  *"OPEC+ Set to Raise Output Again — Even as Members Can't Pump It."* Anchor `[COT]`: WTI net-spec at
  the **11th percentile**, i.e. speculators were crowded short into a price that then fell.
- ★ **A C4-shaped observation, logged and deliberately NOT counted**: on 07-24 the crack fell −3.29%
  while the refiners were **flat** (MPC −0.49σ, VLO −0.34σ, PSX −0.05σ vs SPY +0.10%). That is the
  "crack down, refiners don't follow" shape. **M96 measured this counter to be under-powered** — the
  link is same-day-only at r≈0.22–0.30 and a 3-day sign disagreement occurs ~6.5% of the time by
  chance. **The observation is recorded; the counter is not incremented.** (R12 is why.)
- ⚠ **A registration flaw in this proposition's own anti-signal, declared:** it reads *"a settled
  crack below 60 **with crude above $90**."* **Crude settled at $89.31 — below $90 — so the
  conjunction is now unreachable as written**, and a crack collapse arriving *with* falling crude
  would not trip it. **Same defect class as D35** (a grid that cannot cover what actually happens).
  **Restated for the next run, on one axis:** *kill = a settled 3-2-1 crack below 60, regardless of
  the crude level.* Distance to it today: **4.30 points**, the closest it has been.
- **Both branches:** (a) the crack stabilises ≥65 and the diesel gap re-widens → 07-24 was OPEC
  headline noise into VLO's print; (b) **the crack breaks <60 on settled closes, or the diesel gap
  makes a second consecutive narrowing** → the margin engine is rolling and the Energy tilt must sit
  on crude/integrated alone, into a WTI already at the 11th COT percentile.
- KPI: **3-2-1 crack on SETTLED closes only** · **the diesel-minus-gasoline gap** (promoted to primary
  KPI this run) · weekly-mean acceleration · WTI COT percentile.
- Catalyst: **VLO 2026-07-30 (D-5)** · **STNG 2026-07-30 (= S21, one of only two event-covering
  straddles on the board, ±10.0%)** · **MPC 2026-08-04** · Hormuz statement `[blank]`.

**P5 — ★★ NEW · The digital-infrastructure underweight's stated mechanism was refuted at the primary
level, and the desk's most-replicated finding lost its explanation while keeping its measurement.**
- **What was carried**: R7/M24/M37/M88 — *duration REITs are bid while digital infrastructure is sold*
  — an 18.2–24.3pp RS spread, **replicated on four independent dates**, and read as *"a third copy of
  the AI-datacenter short."*
- **What the settled 07-24 session says** `[measured, own calc, σ on each name's own trailing 20d,
  benchmark **SPY +0.10%** named inline]`:

| Name | Session | vs SPY | σ | Bucket |
|---|---|---|---|---|
| **DLR** | **+11.01%** | **+10.91pp** | **+6.05σ** | data centre |
| **EQIX** | **+4.90%** | +4.80pp | **+3.22σ** | data centre |
| VTR | +2.67% | +2.56pp | +2.03σ | duration |
| WELL | +2.03% | +1.93pp | +1.53σ | duration |
| AMT | +1.23% | +1.13pp | +0.60σ | tower |
| CCI | +0.44% | +0.34pp | +0.18σ | tower |

**XLRE +2.22% was the best sector on the board** on a **flat SPY (+0.10%)**.
- **The cause is primary-adjacent and dated** `[Reuters on the company release; 8-K filed 2026-07-23;
  Q2 call 07-23 17:00 ET]`: **DLR Q2 revenue $1.92bn, +29% YoY, vs $1.66bn consensus (a 15.7% beat);
  adjusted FFO $2.65 vs $1.86 (a 42.5% beat); FY26 AFFO guide raised to $8.15–8.20 from $8.00–8.10;
  FY revenue guide raised to $6.85–6.95bn from $6.65–6.75bn** — attributed to *"resilient leasing
  momentum from cloud and AI customers"* — plus a **$3.5bn cash-and-stock acquisition of a larger
  stake in three Northern Virginia data centres from Blackstone.**
- ⚠⚠ **The C-B discipline is applied to this finding, not waived for it.** DLR's move **is an
  earnings event**, filed 8-K 07-23, one session before the flow date. **EQIX has NO 8-K in seven days
  and no earnings coverage in the feed ⇒ its +3.22σ is sympathetic spillover, not its own event.** So:
  **n = 1 event, 1 sympathetic name.** This is the exact shape the desk retracted C-B for last run,
  and it is labelled as such **before** any conclusion is drawn from it.
- ★ **What survives and what dies, stated separately (the R15/C-A pattern):**
  - **SURVIVES: the measurement.** R7's RS spread was real and replicated four times. Nothing here
    unmeasures it.
  - **DIES: the stated driver.** The spread was explained as *"the AI-datacenter narrative topping."*
    The largest listed pure-play datacentre landlord just reported **+29% revenue, a 42.5% FFO beat
    and a guidance raise on AI/cloud leasing**, and bought $3.5bn more of it. **Demand is not topping
    in the primary source.** Direction right, driver wrong — the failure class the desk has now
    logged for the KR utilities leg, the refining leg and the bank NIM leg.
- ★ **W5 dispersion, and it corrects the bucket itself**: the "digital infrastructure" 4-name bucket
  **splits into towers (AMT +0.60σ, CCI +0.18σ — did not participate) and data centres (DLR +6.05σ,
  EQIX +3.22σ)**. R10 already measured AMT as mis-assigned (it groups with the duration names,
  AMT–DUK +0.500). ⇒ **The correct unit is data centres, n=2**, and every prior "digital infra"
  aggregate mixed two things.
- **Both branches:** (a) DLR/EQIX hold their RS gains past the print week and AMT/CCI stay flat →
  the bucket was wrong, the RE underweight is a **tower/duration** call and not an AI-datacenter
  short; (b) DLR round-trips inside 5 sessions → it was an earnings pop and R7's four replications
  keep their explanation.
- **Anti-signal (kills P5):** DLR's excess vs SPY fully retracing by **2026-07-31**, **or** EQIX
  reporting its own quarter with a *cut* guide.
- KPI: **DLR and EQIX RS vs SPY, tracked from the 07-24 close** · AMT/CCI as the control pair ·
  EQIX's own print date `[blank — not in the calendar]`.
- Catalyst: **EQIX Q2 `[blank]`** · **the 07-29/07-30 hyperscaler capex prints, which are the demand
  side of DLR's own guide.**

**P6 — The tariff axis is enacted and cross-sector.** *(carried from 07-24, no new information)*
- Anchor `[news, 07-24]`: 60 countries, forced-labor rationale; Korea and Singapore both **12.5%**
  (S10 **FIRED-B**). No new tariff print on a 144-event Saturday — and per §C-0 that absence is
  bounded by a 93.7%-unseen single-outlet tier, so it is **`unknown`, not "quiet" (C3)**.
- **Both branches / anti-signal / KPI / catalyst:** unchanged from 07-24. `[blank]` implementation date.

**P7 — Japan is still the un-priced global-duration channel, and it is now in the unscored tier for a
third consecutive run.** *(carried, status unchanged)*
- Anchor `[news]`: *"Can Japan avoid a Liz Truss-style shock as its PM embarks…"* [guardian] — in the
  **single-outlet unscored tier**. The yen thread REIGNITED but weakened to **2 outlets**, on a
  Saturday denominator that deflates outlet counts (§C-0).
- ⚠⚠ **Still `[unverified]` under W2 and NOT admissible as evidence.** *"BOJ tightening leads US
  long-end yields"* has **no lag table in this repo (dig D22, open)**. DEEP and BET may not cite it.
- ★ **Flat for a third consecutive run is now itself the finding**: either D22 gets built or P7 should
  be retired rather than carried as permanent scenery. **Escalated to the dig list.**

**P8 — The rate shock's housing/consumer transmission strengthened its precondition and is still
unmeasurable in this repo.** *(carried from 07-24)*
- Anchor `[FRED]`: **10y 4.71% = a 120-day high**, i.e. the precondition moved further in P8's
  direction. Anti-signal (10y back below 4.45%) **did not fire**.
- ⚠ **`MORTGAGE30US` is still not wired into `module_macro_us`'s catalog** — the KPI this proposition
  needs cannot be pulled. It remains a **channel registered for test, not evidence.** Carried
  unchanged so the omission stays visible.

---

## §E · ★ SECTOR TRANSMISSION MATRIX — the deliverable (ROTATION's input)

> Wind direction only, one line per GICS sector. **Not** an equal-weight analysis of 11 sectors.
> All session numbers are the **settled 2026-07-24** close vs 07-23, **benchmark SPY +0.10%** (C1).
> ⚠ **Read the sector tape correctly: 07-24 was a rotation OUT of technology into everything else on
> a flat index — not a risk-off day.** XLRE +2.22 · XLB +1.93 · XLP +1.11 · XLC +0.87 · XLF +0.86 ·
> XLV +0.70 · XLY +0.60 · XLE +0.40 · XLI +0.40 · XLU +0.22 · **XLK −1.44 (worst)**. Nine of eleven
> sectors beat a flat SPY.

| # | GICS Sector | Tilt | Δ vs 07-24 | Driving prop. | One-line why |
|---|---|---|---|---|---|
| 1 | **Energy** | **OW → OW−** | **DOWNGRADE** | **P4** | ★ The OW's own KPI turned: **Brent back below $100 (96.78, −3.88%)**, crack **−3.29% to 64.30**, and the **diesel-minus-gasoline gap NARROWED for the first time in the run-up (35.50 → 32.96)** with the **first negative settled weekly delta of the six-week advance (−0.89%)**. Level still 88.9th pctile; **rate now below zero (L1)**. Held at OW− only because **WTI COT sits at the 11th percentile** — crowded-short is ammunition, not a floor. **VLO prints 07-30** |
| 2 | **Info Tech** | **N (split flagged) → N (split UNCONFIRMED)** | driver weakened | **P3** | ★ The 07-23 supplier/spender spread **reversed sign in one session (+6.07pp → −4.20pp)**. `indistinguishable` (C4) was the right call and the "structural split" reading is not supported. ⚠ In σ terms the supplier selloff was **ordinary** (SOXX −1.13σ, MU −1.09σ) — M72. **The split mandate to ROTATION is weakened, not withdrawn; S13 lands 07-29** |
| 3 | **Financials** | **OW−** | hold | P1, P2 | 2y at a **120-day high** pays the front book; **XLF +0.86% vs SPY +0.10%**; and the 07-24 leaders match the desk's own measured nodes — **TRV +1.19σ, CB +0.89σ** (insurance, M106) and **ICE +0.90σ, NDAQ +0.72σ, SPGI +0.54σ** (exchanges, M103/M107). ⚠ **Credit widened +9bp for the first time in six runs** (§A-2) — the leg the OW rests on made its first adverse tick. **S14 lands 07-30** |
| 4 | **Industrials** | **OW−** | hold | P4, S7, S20 | No new information. **LMT +0.87σ · RTX +0.84σ · CSX +0.48σ · UNP +0.63σ · NSC +0.38σ**, all modest, all positive. ⚠ **UPS prints 2026-07-28 (D-3)**, which is S20 — the **registered falsifier of the promoted rail DEEP** *and* the refiners' last unread customer (W4/D23) — and the foreign feed carries **zero UPS pre-print coverage in 4 days**. ⚠ M91 stands: ~8 of UNP's 12 revenue growth points are **fuel surcharge**, so the rail leg is the Energy bet through a different income statement |
| 5 | **Health Care** | **N− → N** | **UPGRADE** | C7 | ★ **A fourth consecutive independent session of outperformance**: XLV **+0.70% vs SPY +0.10%**, with **ABT +0.78σ (the sector's best) · JNJ +0.82σ · ABBV +0.48σ · LLY +0.36σ**. ★★ **ABT is C7's own pre-registered resolving observable** ("one 🟢 from outside the top-6 by market cap"), and it led. Still **`indistinguishable` (C4)** on n — but a belief-vs-money gap carried against **four** independent dates has become a statement about the desk, not the market |
| 6 | **Comm Services** | **N−** | hold | P7-prior, P3 | XLC +0.87%; **GOOGL +0.25σ** recovered slightly. **META prints 07-29 (S16)** with a **FINRA short-vol z of −2.35 into the print** (demoted grade, M95). No regulatory print today. Held N− with S16 explicitly unsettled |
| 7 | **Utilities** | **N−** | hold | P1 | Bond proxy into a **120-day-high real yield (2.43%)**. XLU +0.22% (10th of 11), and ⚠ the two-legs problem **inverted** this session — **VST −1.42σ and CEG −0.18σ**, i.e. the *AI-power* leg was sold while the regulated leg carried the sector. Same label, two behaviours, third consecutive run (W5) |
| 8 | **Real Estate** | **N− → N** | **UPGRADE** | **P5** | ★★ **XLRE +2.22% = the board's best sector**, and the underweight's **stated mechanism was refuted at the primary level**: DLR reported **+29% revenue, a 42.5% FFO beat, a raised FY guide on "robust data center demand"** and a **$3.5bn Blackstone datacentre acquisition** — while printing **+6.05σ**. ⚠ **Upgraded one notch only**: it is **an earnings event, n=1** (EQIX has no 8-K ⇒ sympathetic), and the C-B retraction is four days old. **R7's measurement survives; its explanation does not** |
| 9 | **Materials** | **UW** | hold, **tape disagreement declared** | P1, P6 | ⚠ **XLB +1.93% was the 2nd-best sector on 07-24 — against the tilt.** Held UW on **Copper at the 98th COT percentile** (crowded-long, context-only per the REJECTED ledger), a 60-country import tax (P6) and China's export-control retaliation. **The disagreement is stated, not suppressed**; if XLB beats SPY again next session the UW needs re-argument, not repetition |
| 10 | **Cons. Discretionary** | **N−** | hold | P1, P8, P6 | The most rate-sensitive consumption there is, into a 2y at a 120-day high and an unmeasurable 7-handle mortgage channel (P8). XLY +0.60%; **AAPL +1.49σ** on its own headline (GICS IT, noted here only to prevent double-counting) |
| 11 | **Cons. Staples** | **N** | hold | P1, P6 | XLP **+1.11%**, 3rd best — consistent with the day's rotation-out-of-tech read rather than with a defensive bid, since **nine of eleven sectors beat SPY**. Import-tax overlay unchanged |

**Wind summary.** **Two downgrades-in-substance and two upgrades.** Energy's OW is cut to **OW−**
because its own KPI (the crack's *rate*, and the diesel bottleneck) turned for the first time. Info
Tech's split thesis **lost its evidence in one session** and the label stays N with the mandate
weakened. **Real Estate and Health Care are both upgraded a notch** — RE because the underweight's
stated mechanism was refuted by a primary print, HC because a fourth independent date arrived and
C7's own resolving observable (ABT) led it. **Three sectors (IT, Utilities, Real Estate) each carry a
measured two-legs problem**, which is the W5 shape for the fourth and fifth time.

⚠ **The single most important framing for ROTATION**: on 07-24 **nine of eleven sectors beat a flat
SPY while XLK fell 1.44%.** A sector matrix read as "defensives bid" would be wrong — the index was
flat because one sector fell, not because money hid.

**DEEP candidates handed to ROTATION** (ROTATION owns the final pick):
**① Real Estate / data centres (P5)** — the desk's **most-replicated finding just lost its stated
driver to a primary source**, and HANDOVER §7a measured the node at **four replications and ZERO
report coverage**. Highest information value on the board.
**② Energy (P4)** — the OW's KPI rolled: negative weekly rate, narrowing diesel gap, Brent <$100,
OPEC signalling supply, WTI COT at the 11th percentile. **VLO 07-30, STNG 07-30 (S21).**
**③ Info Tech (P3)** — the KPI sign-flipped; **S13 lands 07-29**; and **$950bn of LTAs (§C-1) is a
fifth volume confirm that touches no price term**, which is the whole regime question (C1/D1).
**④ Health Care (C7)** — fourth independent date, and the pre-registered resolving observable led.
**Swing, flagged to PREMORTEM: Financials** — credit made its first adverse tick in six runs and
**S14 lands 07-30**.

---

## §F · Self-backtest

### +1d kill-line audit of the 2026-07-24 propositions (a state check *and*, where a threshold was pre-registered, a score)

| Prop | Registered kill-line | Measured today | Verdict |
|---|---|---|---|
| **P1** front-end reaction-function, oil trigger | 2y **<4.15%** or real 10y **>2.55%** | 2y **4.37% = new 120d high**; real **2.43% = new 120d high**, 12bp of room; breakeven **2.26, falling** | **Un-tripped; strengthened on the composition leg.** ★ Its *causal* leg (oil→rates) now has a live test that is **unscoreable at this clock (C3)** — oil fell 3.1% on 07-24 and FRED has no 07-24 curve |
| **P2** credit narrative ≠ credit market | HY OAS **>3.10%** | **2.77%, +9bp — the first material widening in six runs**; IG +1bp; NFCI still loosening | **Un-tripped, but its KPI moved against it for the first time.** ★ **A pre-registered half is SCORED**: the 07-24 "equity-only stress" read is **corrected** — HY widened the same day the VIX rose; it was a publication lag, not dispersion |
| **P3** the AI complex has split | capex **cut** at MSFT/META | `capex cut` **d1 = 0** (4th consecutive) — **but the registered KPI, the supplier-minus-spender spread, went +6.07pp → −4.20pp** | ★★ **HALF-MISS, self-scored.** The anti-signal is un-tripped; **the proposition's own KPI reversed sign in one session.** The C4/`n≈1` tags attached at registration are what stopped this becoming a carried verdict |
| **P4** war premium hostile to refining margin | settled crack **<60 with crude >$90** | crack **64.30 (−3.29%)**, crude **$89.31 — below $90** | **Un-tripped — and the anti-signal is measured DEFECTIVE**: crude fell below the conjunction's own threshold, so a crack collapse arriving with falling crude cannot trip it. **Restated on one axis in §D-P4.** Distance to the restated kill: **4.30 points, the closest yet** |
| **P5(07-24)** tariffs enacted | carve-out list exempting large importers | no print (144-event Saturday) | **Un-tripped; `unknown`, not "quiet" (C3, §C-0)** — renumbered **P6** this run |
| **P6(07-24)** Japan duration channel | yen retraces with no policy change | thread REIGNITED but 2 outlets on a deflated denominator; item in the **unscored** single-outlet tier | **Un-tripped and flat a THIRD run** — renumbered **P7**. The flatness is escalated: build D22 or retire the proposition |
| **P7(07-24)** regulatory tax on Big Tech | appealed and stayed, no remedy | no print today | **Un-tripped, no new data** — folded into Comm Services' line rather than carried as a standalone |
| **P8** 7%-mortgage channel | 10y back **<4.45%** | **10y 4.71% = 120d high** | **Un-tripped; precondition strengthened.** ⚠ `MORTGAGE30US` **still not wired** — the KPI cannot be pulled |

**Running hit-rate note (P4 discipline — accrual, not a score to bank).** Of the eight propositions
carried into today, **zero tripped an anti-signal**, **one (P3) had its own KPI reverse**, **one (P2)
had a pre-registered half scored against its provisional reading**, and **one (P4) was found to carry
a structurally untrippable anti-signal**. ⇒ **The failure mode this run is not wrong direction — it
is defective registration**, which is the same finding §3b of HANDOVER made about S12/S28/S35/S46.
**Three of the last five defects the desk has logged are about how a test was written, not about what
the market did.**

### Failure classes logged this run

1. **A retracted claim living inside a machine-regenerated artifact** (§0, D51) — retractions filed
   in `handoff/` do not propagate to `CATALYST_WATCH.json`.
2. **A probe term that measures the desk's vocabulary rather than the market's** (§C-2, D52) — four
   consecutive ~0 readings while the branch runs at 259 hits/day under other words.
3. **An anti-signal written as a conjunction on a variable that then moved** (§D-P4) — the same class
   as D35's single-axis grid defect.
4. **A single-outlet tier that is unscored rather than low-scored on the US feed** (§C-0) — 93.7% of
   the tier where FX/rates primaries print is invisible by construction on this desk.

---

## §G · Corrections and retractions filed by this stage

**No new retraction (`R`) is filed.** Two carried claims are **narrowed**, and both are recorded here
rather than in §5 because neither was a standing-view row:

- **The 07-24 run's provisional "equity-only stress" reading is corrected** to "publication lag"
  (§A-2). It was explicitly tagged `unknown (C3)` at the time and is scored, not retracted.
- **P4's anti-signal is restated on one axis** (§D-P4). The proposition survives; the test does not.

★ **One carried belief is put at risk but NOT retracted**: R7/M24/M37/M88's *explanation* (digital
infrastructure is being sold because the AI-datacenter narrative is topping) is contradicted by DLR's
own print (§D-P5). **It is not retracted this run** because the contradicting evidence is a single
earnings event on one name — the C-B lesson applied to the desk's own new finding. **DEEP owns the
resolution.**

---

## §H · Rule-linter result

`python -X utf8 scripts/report_lint.py` — result recorded in §I of the run log below.
The linter checks **form only** (C1 benchmark · C2 both halves · S6 future label · D6 OBV-alone); a
clean run is not a correct report.

---

## §I · New digs registered by this stage

| # | Dig | Why | Owner |
|---|---|---|---|
| **D51** | `CATALYST_WATCH.json` regenerates the **R13-retracted** SK hynix conversion claim every run | A retraction that does not reach the machine artifact is not a retraction for downstream stages | ALPHA / next HANDOVER |
| **D52** | Retire `capex cut` as C6's probe; measure `AI spending` / `overbuild` / `digestion` / `spending discipline` | The probe has returned ~0 four times while the branch runs at 259 hits/day and made the WSJ front page | HANDOVER (definition change, human-visible) |
| **D53** | ★ **Build the data-centre vs tower split as a real unit**: DLR+EQIX vs AMT+CCI, SPY-residual correlation, and re-run R7's spread on the corrected buckets | R10 already showed AMT is mis-assigned; every "digital infra" aggregate to date mixed two things | DEEP / PREMORTEM |
| **D54** | Pull **EQIX's Q2 date** — it is in no calendar and it is P5's own resolving event | P5 registered an anti-signal against an event with a `[blank]` date | EVENT_ALPHA |
| **D55** | `module_news_data burst` failed twice (read timeout) — the **day-resolution blind-spot axis is missing from this run** | The "no new macro term" claim rests on `blindspot` alone | ALPHA |
| **D56** | Wire **`MORTGAGE30US`** into `module_macro_us` — carried unbuilt for a second run while P8's precondition strengthens | A proposition whose KPI cannot be pulled cannot be scored | (module change — human) |
| **D57** | **D22 (Japan lead/lag) or retire P7** — flat for three consecutive runs and only ever visible in the unscored tier | Permanent scenery is not a proposition | DEEP |

---

## ✅ EXIT CHECK

- [x] Catalysts injected (`--days 10`, 13 binaries); narrative read as **events + trajectories +
      term sweep + blind-spot**; indicators read (**FRED primaries + COT positioning + FINRA**);
      continuity anchor = the 2026-07-24 `industry_US/MACRO_REPORT.md`, read in full including its
      propositions and DRIFT addendum.
- [x] Events read via `--body 2`; **tail = 0**.
- [x] **`tail = 0` is explicitly NOT claimed as coverage** (§C-0): `single_source` **15 shown / 239
      total, and the 239 are UNSCORED because the classifier is Korean-only** ⇒ 93.7% of that tier is
      invisible on this desk by construction; `excluded_nonmarket` **0 / 0**; `subevents_recovered`
      **31**. Every "no print today" claim in §D is written as `unknown` (C3), not as "quiet".
- [x] Denominator quoted and corrected: **828 articles → 144 events → 144 market / 0 non-market**, and
      the **Saturday deflation (144 vs 764–949 weekday, ~17%)** is stated before any tier claim.
- [x] Trajectories read (`thread --days 7`): the $950bn thread is **BUILDING 3d, 3→2→6**; the
      Warsh/FOMC thread is **REIGNITED 6d, 62 items**; the Japan thread's weakening is explicitly
      discounted against the Saturday denominator.
- [x] Every "nothing happened" claim carries its denominator (§C-0, P6, P7).
- [x] **Bucket terms passed as separate argv**, one `theme-age` / `fts` invocation per term (§C-2) —
      no multi-word bucket was quoted as a single query.
- [x] **Both halves cited on every headline print**: core CPI **−0.02% MoM / +2.57% YoY**, headline
      **−0.42% MoM / +3.46% YoY**, HY **+9bp against a 3.46% 120-day max**, the crack's **level (88.9th
      pctile) against its rate (−0.89% WoW)**.
- [x] **Every relative-performance number names its benchmark inline** — **SPY +0.10%** on every
      session figure in §D/§E; no statistical result carried across markets (the KR M114 corroboration
      is cited as an independent measurement on its own basis, not transferred).
- [x] **Credit axis read and cited**: HY OAS **2.77%**, IG **0.79%**, NFCI **−0.552**. The one
      risk-off-shaped claim in this report (§A-2) cites all three, and P2 labels any uncited
      credit-stress claim **narrative-only**.
- [x] **`real_10y` quoted with `breakeven_10y`** — 2.43% with 2.26% falling, at every use.
- [x] Linter run (§H).
- [x] **Transmission matrix produced, all 11 sectors, one line each** (§E) — ROTATION's input.
- [x] `MACRO_REPORT.md` written with primary numbers explicit; **self-backtest appended with two
      scored items and one measured registration defect** (§F); new terms folded into §C-2's table.
- [x] **No sizing, no buy/sell language.** (P4)

---
> Next: `python pipeline/run_protocol.py industry_us --next` → **SWEEP**.

---

## §5 · DRIFT ADDENDUM — appended 2026-07-25 by stage 10 (append-only; nothing above is rewritten)

**Baseline of the report being watched: 2026-07-25 ~22:1x–22:5x KST (09:1x–09:5x ET, Saturday).**

### ⚠ The instrument failed, and the substitute is declared rather than hidden

`python -X utf8 scripts/drift_watch.py --report llm_outputs/2026-07-25/industry_US/MACRO_REPORT.md`
**failed twice** (retried once per the run rules):

```
drift 질의 실패 (rc=2): 'drift' 는 원격 실행 불가(조회 전용).
허용: ['blindspot','burst','chain-hop','coverage','export','fts','search','theme-age']
```

`drift` is **not on the remote news API's allow-list**, so the desk's dedicated kill-switch instrument
**cannot run at all while the news backend is remote.** This is the **second tool on this axis to
fail in one run** — `module_news_data burst` also timed out twice (§C-3). ⇒ **Both of the desk's
"find what I did not think to query" instruments were unavailable today.** Registered as dig **D64**;
`burst`'s timeout is **D55**.

**Substitute run instead** — a manual `fts --scope foreign` kill-switch sweep on the terms the
report's own anti-signals name. It is **weaker than `drift_watch`**: it can only test phrases the
desk already thought of, which is precisely the blind spot `drift`/`burst` exist to cure.

### Kill-switch sweep — the substitute's result

| Term | d1 | d7 | Read |
|---|---|---|---|
| **`capex cut`** | **0** | 1 | **A FOURTH consecutive zero.** C6 holds on the term axis, and §C-2's finding stands: the probe is measuring the desk's vocabulary, not the market's |
| **`Hormuz open`** | **0** | — | **S8's own trigger phrase did not print.** The undated branch stays undated |
| `credit stress` | 2 | 20 | **Flat, and this one matters**: HY OAS widened **+9bp on 07-23** (§A-2) with **no corresponding narrative burst.** The move is in the market and not in the feed — the mirror image of the P2 pattern, and it is the first time this run the *market* has led the *narrative* on credit |
| **`guidance cut`** | **10** | 25 | The only elevated term (d1 ≈ 2.8× the 7-day daily mean of 3.57) — **body-read below** |
| `ceasefire` · `recession` · `default` · `downgrade` | 88 · 94 · 91 · 76 | — | High-baseline generic tokens. **`default` catches software defaults and `downgrade` catches analyst actions** — poisoned tokens, not signals, and not treated as such |

### The one elevated term, body-read rather than counted

`guidance cut` d1 = 10 resolves to **three known and non-regime items**:
1. **Walmart de México Q2** — *"revenue beats but guidance cut on weak demand"* [investing_en ×2,
   title-only]. **This is the same item M113 body-read on 2026-07-24** — it is being counted a second
   time, not appearing a second time.
2. **Otis** — *"Is Otis Stock Attractive After Guidance Cuts and Its 19% YTD Slide?"* [yahoo_finance,
   nasdaq]. A **retrospective** commentary piece on an already-known slide, not a new print.
3. A **shareholder-litigation notice** (GPGI) — the stale-dated legal-notice class already logged as
   **D29**.

⇒ **No 🚨 fires. No ADDENDUM correction is required to any proposition above.** Every anti-signal
registered in §D remains un-tripped as of this timestamp.

### ⚠ Two caveats on this verdict, so it is not read as stronger than it is

- **The denominator is a Saturday.** 07-25 carried **144 market events against 764–949 on the
  surrounding weekdays (~17%)**. A d1 count on this base is not comparable to a weekday d1, and the
  `guidance cut` ratio above is inflated by that alone.
- **The substitute cannot find an unnamed term.** Both instruments that could have — `drift` and
  `burst` — were unavailable. **A clean sweep here means "none of the phrases we already knew to
  watch fired", not "nothing happened."** Stated per C3: this is an `unknown` column, not a null result.

### What the next run must re-read first

**`DTWEXBGS` (S12) — deadline 2026-07-28**, one business day after the next run. If it has still not
printed, score **`AMBIGUOUS` with the reason** and **substitute no proxy**.
**And UPS prints 2026-07-28 (S20 + S20-ANNEX)** — the window's first binary, still absent from
`CATALYST_WATCH.json` (D18, 6th occurrence).
