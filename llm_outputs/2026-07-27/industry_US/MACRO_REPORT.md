# MACRO_REPORT — industry_US — 2026-07-27 (Mon)

> Stage 2/10. Wall clock **2026-07-27 22:3x KST = 09:3x ET**. US session **1 minute old**.
> Last settled US close **Friday 2026-07-24** — *identical to the prior US run's data*.
> News `--scope foreign` on every call (hard rule). Zero buy/sell language (P4).

## ★★ The framing this stage is obliged to state first

**No US trading session has occurred since the last US run.** Every price-derived number available to
this stage is the same 07-24 number the 2026-07-25 run already published. Therefore:

- **No tilt in §E is changed on a price axis this run.** A matrix that reports "Δ" without a new bar
  is reporting an artifact — the R17 / R17-b failure class.
- **Almost every KPI the prior run registered is unscoreable at this clock**, and §F says so per KPI
  rather than narrating around it.
- **The narrative axis is the only live axis — and it delivered two regime-relevant events.** That is
  where this run's information content sits, and it is unusually high: **a Hormuz de-escalation
  headline that does not survive its own body read**, and **a funded new DRAM entrant that the
  standing view's capacity clock does not contain.**

---

## §0 · Catalyst injection `[catalyst_calendar --days 10]`

**16 binaries in window.** Confirmed macro: **FOMC 2026-07-29 14:00 ET (D-2, fed✓)** ·
**June PCE 2026-07-30 08:30 ET (D-3, bea✓)** · undated **Iran "Strait of Hormuz open" (TACO trigger)**.
Earnings the calendar carries: META 07-29 · VLO / STNG / MA 07-30 · AMD / ANET / MPC 08-04 · PSX 08-05 ·
CEG / LNG 08-06.

### ⚠ D18 fires a **SEVENTH** consecutive time — and this time it misses tomorrow's binary

**UPS prints 2026-07-28 — D-1 — and it is absent from `CATALYST_WATCH.json` for a 7th consecutive run.**
UPS is not an incidental name here: it is **S20 + S20-ANNEX**, simultaneously the desk's registered
falsifier of the rail node *and* dig **D23**'s fifth and last unread refiner customer (W4). It also
carries **the only genuinely event-priced straddle on the board** (±6.9% = 1.81× √5·σ20).

Also absent, all inside 4 sessions: **MSFT · AMZN · V · EQIX · FTNT · XOM · STX**. A `--days 10` pull
was run (not the 5-day default) and still returned none of them. ⇒ **The defect is confirmed again as
source coverage of single-name earnings, not window length.** The desk's bracket book is more complete
than the machine calendar that is supposed to seed it, which is the wrong way round.

### ⚠ D61 fires a **THIRD** consecutive time — the calendar is still regenerating a retracted claim

The STRUCTURAL block still reads, verbatim: *"2026-07-29 SK하이닉스 **ADR ↔ 원주 양방향 전환 개시** …
전환 개시로 차익거래가 열리면 프리미엄이 붕괴한다."* **This is R13, retracted 2026-07-24** on the named
on-record testimony of the KSD president — the ceiling is **2.5%, not 25%**, and 07-29 is a *share
registration* date, not a conversion opening. It was replaced by **S17** (the premium as a running
observable). The retraction lives in `handoff/`; the machine artifact downstream stages read
regenerates the killed claim every run. **Fix is a data edit to `data/catalysts/structural_schedule.json`
and needs human approval — not made here. Flagged for the third time.**

---

## §A · Regime primaries `[FRED]` — pulled this run

| Series | Value | `asof` | vs prior run |
|---|---|---|---|
| DGS10 | **4.71%** | 2026-07-23 | **unchanged — no new print** |
| DGS2 | **4.37%** | 2026-07-23 | **unchanged** |
| DGS5 · DGS30 | 4.46% · 5.17% | 2026-07-23 | unchanged |
| DFII10 (real 10y) | **2.43%** | 2026-07-23 | unchanged |
| T10YIE (breakeven) | **2.26%** | **2026-07-24** | **advanced one day, flat in level** |
| HY OAS | **2.77%** | 2026-07-23 | **unchanged — the 07-24 print still does not exist** |
| IG OAS | 0.79% | 2026-07-23 | unchanged |
| NFCI | **−0.552** | 2026-07-17 | unchanged (weekly) |
| VIX | 18.70 | 2026-07-23 | unchanged |
| RRPONTSYD · SOFR | 0.675 · 3.64% | **2026-07-24** | advanced one day |
| DFF | 3.63% | 2026-07-23 | unchanged |
| **DTWEXBGS** | **120.5315** | **2026-07-17** | ⚠ **unchanged for 10 calendar days — see §F/S12** |
| CPI · core CPI | 332.568 · 336.065 | 2026-06 | monthly, ~1 month lag — stated, not dressed as fresh |
| UNRATE | 4.2% | 2026-06 | monthly |

### §A-1 ⚠ Three registered tests are unscoreable for a second consecutive run, by publication lag

The daily curve block and HY OAS both still end **2026-07-23**. That is *expected* (Friday's values
publish Monday afternoon ET and it is 09:3x ET) and is **not logged as a defect**. But it has a
consequence the run must state rather than route around:

- **P1's registered oil→2y pass-through test** (*"oil fell 3.1–3.9% on 07-24; if M69's causal claim is
  right the front end must give some of this back"*) — **still `unknown` (C3), 2nd consecutive run.**
- **P2's pre-registered numeric score** (*"HY OAS on 2026-07-24 ≥2.85% ⇒ turn; ≤2.72% ⇒ tick;
  in between ⇒ AMBIGUOUS"*) — **the observable has not printed. Not scored, not narrated.**
- ★ The decomposition that *is* readable moved **for** P1's framing again: **T10YIE advanced to 07-24
  and stayed 2.26%** against a real 10y at a 120-day high ⇒ the whole move remains **real, not
  inflation-expectation**. That is one clean day of new data and it is all §A has.

### §A-2 · What §A can honestly claim

**Nothing about the curve changed this run.** The regime state carried from 07-25 stands verbatim:
whole curve at 120-day highs on one date, breakeven flat and falling, **S9's kill line (real 10y 2.55)
12bp away**, credit 14bp off its 365-day low after its first material widening in six runs, NFCI
easing a 5th week. **Any downstream stage citing a "rate move" this run is citing 07-23 data.**

---

## §B · Positioning `[CFTC COT — Tue close, 3–4d lag ⇒ context, never a trigger]` + `[FINRA]`

**COT pulled this run is byte-identical to M125** (2026-07-21 Tuesday close; next release covers 07-28):

| Instrument | Net-spec | 1y %ile | Read |
|---|---|---|---|
| **Nasdaq-100** | −9,691 | **5th** | crowded SHORT |
| **S&P 500 (E-mini)** | −16,784 | **84th** | crowded long |
| Russell 2000 | +6,758 | 88th | crowded long |
| **UST 10Y** | −879,706 | **12th** | crowded short, **48,031 shorts ADDED into a 120-day-high yield** |
| UST 2Y | −1,154,597 | 53rd | neutral |
| USD Index | +15,614 | 66th | neutral |
| **WTI Crude** | +20,039 | **11th** | crowded short |
| **Nat Gas** | −171,138 | **11th** | crowded short |
| **Copper** | +73,977 | **98th** | crowded long |

★ **M125's headline fact is carried unchanged into the print week and cannot be refreshed before it**:
a **79-percentile-point spread inside one asset class** (NDX 5th vs SPX 84th), two days before
MSFT/META. ⚠ COT-extreme contrarian reading sits in the **REJECTED** ledger (D6) — this is crowding
context, not a direction.

### FINRA short-volume, 2026-07-24 — reported **with baselines**, per D52

| Ticker | short% | base20 | z | 5v5 | Readable? |
|---|---|---|---|---|---|
| UPS | 52.0% | **57.7%** | −1.12 | −0.0· | ❌ baseline **12.7pp above** the tool's 40–45% normal band — verdict suppressed (D52) |
| UNP | 31.8% | **52.2%** | −2.41 | −11.8▼ | ❌ baseline out of band — the "🟢 short-covering" string is **suppressed**, not reported |
| MPC | 46.6% | **55.1%** | −1.15 | −0.4▼ | ❌ baseline out of band — suppressed |
| CSX | 37.7% | 35.9% | +0.18 | −10.2▼ | ✅ in band — neutral z, pressure easing on trend |
| NSC | 48.0% | 42.6% | +0.78 | −1.8▼ | ✅ in band — neutral |
| VLO | 41.9% | 42.5% | −0.10 | +0.7▲ | ✅ in band — neutral |
| **PSX** | 41.8% | 40.2% | +0.18 | **+13.8▲** | ✅ in band — **the set's only material short build**, and it is on the one refiner whose print is furthest out (08-05) |
| XOM | 38.5% | 40.9% | −0.32 | +5.4▲ | ✅ in band — mild build |

⇒ **D52 is not a footnote here: 3 of 8 names in the pre-event set carry chronically out-of-band
baselines, so their z-verdicts are statements about their own history, not about covering.** This is
the US desk's only "who is trading" axis and it is unreadable on three of the eight names that matter
into tomorrow's binary.

---

## §C · Narrative axis `[news, --scope foreign, hard rule]` — the only live axis this run

### §C-0 · Denominator, stated before any "quiet" or "loud" claim

`brief --date 2026-07-27 --scope foreign --body 2`:
**2,095 articles → 329 clusters → 329 market events, 0 non-market.**
**Head (≥5 outlets) 34 · body 295 · tail 0.**

⚠ **`tail = 0` is NOT the coverage claim.** The recovery sections:
- `single_source`: **15 shown of 379** ⇒ **364 withheld = 96.0% of the single-outlet tier unseen**,
  and the module states these 379 **have no score at all** (the classifier is Korean-only), so they
  are *unmeasured*, not *low*.
- `excluded_nonmarket`: **0 of 0** shown (band nb ≤ −3.0).
- `subevents` (`└`): **72 recovered** — separate events that a 0.65 similarity threshold had swallowed.

⇒ **Every "nothing happened in bucket X" claim below is bounded by a 96%-unseen single-outlet tier
and is written as `unknown`, never as "quiet" (C3).**

### §C-1 ★★★ The day's largest event — and the headline and the body say different things

**"Oil prices plunge as US and Iran pause strikes over Strait of Hormuz"** — **54 articles / 19 outlets,
the day's #1 event**, with sub-events *"Global oil stocks tumble as crude prices retreat"*,
*"Dow Jumps 575 Points On U.S.-Iran Hope"*, *"European indexes climb"*, *"Indian Shares Rally As Oil
Prices Crash On US-Iran Truce Hope"*, *"Dollar pulls back"*.

**Body-read, and the correction matters more than the headline** `[cnbc · euronews · bbc · dw · ft]`:

- ★★ **The Strait of Hormuz is STILL CLOSED.** cnbc, verbatim: *"The strait, through which a fifth of
  global oil supply flowed before the conflict, **remains closed** as the U.S. maintains its ongoing
  blockade."* dw headline, independently: *"Iran rules out US talks as **Hormuz Strait remains closed**."*
- What actually happened is a **pause in strikes, now in its third night** (after **13 consecutive
  nights** of US strikes), to *"give diplomacy some space"* (US Amb. Waltz on Fox/CBS). **Iran
  reciprocated by halting retaliatory operations.** Oman is pursuing a **provisional transit
  arrangement**; an Omani delegation was in Tehran Fri–Sat.
- **Talks are not formally resumed** (dw: *"Tehran and Washington are not currently holding talks, but
  mediators remain active"*), and **military assets are still moving in** (Waltz: *"locked and loaded"*).
- **Escalation continued on side fronts inside the same 48 hours**: Saudi strikes on Houthi targets in
  Yemen after Red Sea shipping attacks; **Ukraine struck an Iranian vessel in the Caspian**, killing a
  sailor, which Tehran called *"hostile and criminal"*; **US CENTCOM redirected 12 commercial vessels,
  disabled 2 and boarded 2** as of Saturday.
- **Named analyst read, Monday note** `[Deutsche Bank, quoted by cnbc]`: *"Traffic through Hormuz
  remains severely disrupted, while the conflict has broadened into the Red Sea… a welcome pause from
  the main actors but a fragile one, especially with side battles still ongoing."*

⇒ **The tape repriced a war premium; the physical observable is unchanged.** That distinction is
exactly what **S8** was written to enforce, and §D-P4 carries it as a pre-registered score rather than
a conclusion.

⚠ **Trajectory context (C1-adjacent, and it cuts against reading the pause as a trend):** the
escalation thread **"Trump warns of largest strikes on Iran yet"** is tagged FADING but sits at
**14→11→16→11→14→11 outlets** — *still 11 outlets on the pause day*. And **two Hormuz threads ENDED
inside the window** at peaks of 18 and 15 outlets. The oil thread's own curve
(18→15→27→19→**5→13**→19) dips only where the **weekend denominator** does (07-25 297 events, 07-26
277, vs 781–949 on weekdays) — **the tool's own warning that a low-volume window-end inflates FADING
applies to every tag in this window.**

### §C-2 ★★★ CXMT — a funded new DRAM entrant, and the standing view's capacity clock does not contain it

**"China's memory chipmaker CXMT shares soar in its blockbuster [Shanghai debut]" — 36 articles /
16 outlets, the day's #2 event.**

Primary-sourced from the **IPO prospectus**, via Reuters `[news, multi-outlet]`:

| Fact | Value |
|---|---|
| IPO raise | **¥57.92bn = $8.6bn — Asia's largest IPO of 2026** |
| Debut | opened **¥49.50 vs ¥8.66 IPO price = +470%** |
| Market cap | **≈¥3.3tn = $487bn**, passing ICBC ⇒ **China's most valuable listed company** |
| Position | **World's 4th-largest DRAM producer, ~7.7% global share (2025, prospectus)** |
| Revenue | **Q1 +719% YoY to ¥50.8bn ($7.51bn)**; H1 **expected** ¥110–120bn ≈ **~2× FY2025's ¥61.8bn** |
| Ownership | state shareholders **36.29%** pre-IPO (Hefei/Anhui + the "Big Fund") |
| **Use of proceeds** | **"expand production capacity, improve manufacturing technology, increase R&D"** |
| Constraints | lags badly in **HBM**; approved by a US interagency committee for possible **Entity List** addition (not implemented); **DoD designated it a "Chinese Military Company"** |

★★ **Why this is a regime item and not a China-market item.** STANDING_VIEW **M7** — the supply half of
the entire memory thesis — reads: *"New DRAM capacity online: SK M15X + Micron Idaho **mid-2027**;
Samsung P5 **2028**."* **It names three suppliers and no fourth.** A **$8.6bn cash raise explicitly
earmarked for capacity expansion**, by the **#4 producer growing revenue at triple digits**, is a
supply-side variable that clock does not contain. It also sits directly on **C1** (do LTA price floors
hold?) — a state-funded entrant with a domestic captive market is the classic mechanism by which a
price floor stops binding.

⚠ **Tagged honestly, because three of those numbers invite over-reading (C2/C3/S1):**
- 7.7% share is a **2025** figure; the +719% is **one quarter off a small base**; the H1 ¥110–120bn is
  a **company expectation in a prospectus, not a print**.
- **This does not change 2026 supply.** Fabs take years; the IPO changes the **funding** of the back
  end of the cycle, not the current quarter. It bears on the *shape*, and on C1, not on M1.
- **`[news]` grade throughout** — no issuer filing was read by this desk. It may be carried; it may
  not be cited as a measurement.

★★★ **And the blind-spot finding, which is the more uncomfortable half.** `thread --days 7` shows this
as **REIGNITED across four days: 3 → 6 → 3 → 16 outlets** — *"Z.ai powers up a 1-gigawatt AI data
center"* (07-21, 3), **"Chip firm priced as China's most valuable company before [listing]" (07-23,
6 outlets)**, *"China's memory chip makers ride AI boom to new power"* (07-24, 3). ⇒ **The largest
supply-side event for the desk's own regime call was visible in this feed at 3–6 outlets for four
days, and neither the 07-25 US run nor the 07-27 KR run carried it.** The desk's own protocol text
already used *"CXMT's HBM-moat bypass"* as its worked example of a 2-outlet event that mattered — and
then missed the same company's IPO week. **Registered as a new dig (D71).**

### §C-3 ★★ Fed hike pricing — a second named source, and a new, sharper number

| Observable | Value | Source |
|---|---|---|
| Hike probability **by the Sept 16 FOMC** | **52.4% (07-16) → 82.4% (07-27)** | CME FedWatch, quoted `[nasdaq 07-27]` |
| Hike probability at **this week's meeting** | **12% → 36% in one week (07-23)** | **Liz Ann Sonders (Schwab), on record** |
| Carried (M69) | 10.7% (07-15) → **34.7%** (07-22) | CME FedWatch |

★ **The 12%→36% line independently corroborates M69 from a second named source** — same instrument,
same direction, one day later. **M69's own caveat is unchanged**: TD Securities on record that this is
*"the second-largest deviation between market pricing and actual Fed action in the past decade"* and
that *"pricing for rate hikes moved alongside **oil**."*

★★ **The live tension, and it is the whole of §D-P1.** The stated driver of the hike repricing is
**oil**. Oil just fell hard (§C-1). **The hike pricing was set before that move and the curve has not
printed since.** So the desk is carrying a rate proposition whose narrated cause reversed and whose
KPI cannot be read for at least another session.

The named causal stack in that piece is worth recording because it is **not** only oil `[nasdaq 07-27]`:
(i) the Iran energy supply shock; (ii) **"Trumpflation has entered its next phase" — headline
inflation fell in June while the *core PCE forecast* has hardly budged**, i.e. pass-through into the
non-energy basket; (iii) AI-driven power/infrastructure costs. **Both halves of the print, per C2:
headline CPI YoY 4.2% (May) → 3.5% (June); core 2.6% (June)** `[news, corroborating the FRED-derived
−0.42% MoM / +3.46% YoY headline and −0.02% MoM / +2.57% YoY core carried from 07-25]`.

⚠ **Counter-source on file, same window**: a syndicated piece running at **fool / nasdaq / yahoo
(one article, three outlets — D10, counted as ONE source)** argues the FOMC **will not hike in 2026**,
on the grounds that *"rate hikes are less effective at solving supply-driven shocks"* and that
Warsh's preferred **trimmed-mean** measure reads ~50bp below headline PCE. Also on file:
*"Bond Traders on Edge as Risks of Fed Rate Hike This Week Mount"* `[bloomberg 07-26, title-only]`.
**Both branches are live in the feed; neither is a measurement.**

### §C-4 · C6 measured a **FIFTH** time — the probe is measuring the desk, not the market

`fts --count`, `--scope foreign`, **d1**:

| Term | d1 | Term | d1 |
|---|---|---|---|
| **`capex cut`** (C6's registered probe) | **0** | **`AI spending`** | **140** |
| `spending discipline` | 1 | **`digestion`** | **50** |
| `overbuild` | 2 | `rate hike` | 142 |
| `guidance cut` | 1 | `memory shortage` | 10 |
| `credit stress` | **0** | `DRAM capacity` | 1 |
| `Hormuz open` | **0** | `diesel crack` | **0** |

★ **`capex cut` returns 0 for a fifth consecutive measurement** while the branch it exists to detect is
loudly narrated under other words — and the **thread axis confirms it independently**: live threads
*"Tech Stocks Tumble On **Spending Worries**"* (4→4→3), *"**CapEx Is Exploding** as Alphabet Goes On a
Spending Spree"* (4→3→4), *"OpenAI to spend more on data centers"* (3→3), *"Google's profits are
outrunning its AI spending boom"* (12→16→14→4→3→3), *"Nvidia in Talks With OpenAI to Guarantee $250
Billion"* (4→6→5). ⇒ **D52's recommendation is now supported on five independent measurements plus a
trajectory cross-check.** ⚠ **Changing C6's probe term is a definition change to a carried
contradiction and needs a human — it is escalated, not executed.**

⚠ **`Hormuz open` d1 = 0 on the day of the largest Hormuz headline of the month** is the same defect in
miniature: the desk's kill-phrase probe is a phrase nobody writes. **A 0 here is not evidence of
absence** (D68's US analogue).

### §C-5 · Bucket sweep, pool-normalized `[fts --mode or --syn, separate argv]`

Pool: **d1 4,707 · d7 33,903 articles.**

| Bucket | d1 | d1 share | d7 share | **normalized** |
|---|---|---|---|---|
| **Rates / Fed** | 1,082 | 22.99% | 18.46% | **1.25× — the only materially elevated bucket** |
| **Memory / semi** | 485 | 10.30% | 8.94% | **1.15×** |
| Credit | 184 | 3.91% | 3.58% | 1.09× |
| Shipping / geopolitics | 715 | 15.19% | 14.12% | 1.08× |
| AI-capex | 845 | 17.95% | 17.11% | 1.05× |
| **Oil / energy** | 595 | 12.64% | 12.51% | **1.01× — flat** |
| Tariff / trade | 334 | 7.10% | 7.85% | 0.90× |

★ **The oil bucket is FLAT (1.01×) on the day of the board's largest oil event.** That is the two-axes
lesson working exactly as documented: *a term spikes when it is **new**; an event ranks when it is
**big**.* Oil vocabulary has been saturated for six weeks, so the term axis is blind to a 19-outlet
oil event. **Any stage that ranks by term velocity this week will rank today's #1 event nowhere.**

### §C-6 · Blind-spot pass, with its own denominator

`blindspot --scope foreign --days 2`: window **8,678 articles**, **400 randomly sampled = 4.6%**.
Token-0 emergent terms are entirely inside the existing set (AI 783 · Earnings 594 · Iran 275 ·
Trump 261 · China 219 · Nvidia 196 · Oil 184 · Fed 181). **Two sit outside the desk's term table and
neither has a vehicle in `us_top300`: SpaceX (129) and Bitcoin (126).** **Japan (99)** is inside P7's
channel and is corroborated by four live threads (below).
⇒ **No new macro term is folded into the term table this run** — and at a 4.6% sample that claim is
**weak by construction and is labelled as such (C3), not reported as a clean sweep.**

### §C-7 · The rest of the day, by tier — read, not skimmed

- ★ **P7's channel woke up.** Four live threads: *"Japan's Takaichi defends policy as underpinning
  yen"* (7→3) · *"Yen steadies near 40-year low on rate-hike bets, intervention…"* (2→2) ·
  *"Japanese Yen: Hawkish BoJ signals versus Fed risk"* (3→2) · *"Japanese utilities seek long-term
  LNG supply as existing [contracts expire]"* (5→3→3→2), plus *"Japan considers foreign bank
  financing for $33 billion US power [project]"* [4/4]. **P7 had been flat in the unscored
  single-outlet tier for three consecutive runs (D57-old).** It is now in the scored tier — which
  **strengthens the case for building D22's lag table, and does not make the unverified lead/lag claim
  citable (W2)**.
- **ECB REIGNITED**: *"Kazimir Says ECB Must Hike at Least Once More to Quell Inflation"* [2/2, 07-27],
  after a 5-day curve 8→5→17→8→2. Consistent with S12's decision axis already being `AMBIGUOUS`
  (hold-with-hawkish-tilt). **Singapore delivered back-to-back tightening** [4/4]. ⇒ **the global
  policy direction in the feed is hawkish, on three central banks, into a US FOMC.**
- **Hyperscaler capex, corroborating §4's asymmetry**: *"Alphabet, Amazon, and Meta Will Spend Over
  $500 Billion on AI"* [9/4] with sub-event *"SK Group, Nvidia sign $500bn deal for AI
  infrastructure"* [3/2] — **a third independent corroboration of M122's volume commitments, still
  with no price term anywhere in the body (C1 untouched)**. And *"Nvidia Weighs $250 Billion Backstop
  for OpenAI Data Center [Projects]"* [9/4] — a **funding-structure** item, which is M134's axis (the
  data-centre node's live variable is cost of capital, not the AI narrative).
- **Refining-margin counter-evidence accumulated on the physical axis**, three separate items:
  *"Singapore's fuel oil stocks increase amid higher net imports"* [5/5] — **a second of M128's five
  named hubs inverting, after Fujairah's +35%**; *"Russia's Novorossiysk Resumed Crude Loadings After
  Days of [disruption]"*; *"Saudi oil exports increasingly depend on Suez as Red Sea [routes close]"*.
  ⚠ M93's dated item is **live this week**: **Russia's diesel export ban expires 2026-07-31.**
- **Bab el-Mandeb**: *"Chinese Tankers Push Through Bab el-Mandeb Despite Houthi [threats]"*
  (4→4→2→2). **M45's blockade is being transited.**
- **Defense**: *"L3Harris signs seven-year deals to expand Patriot, THAAD [manufacturing]"*
  — **single-outlet, unscored tier**; recorded, not promoted.
- **Macro data, single-outlet tier**: *"Durable goods orders rise less than expected in June"*
  [seekingalpha, 1 outlet]. **This is the tier §C-0 says is 96% unseen** — a US macro print sitting
  where the desk cannot systematically see it.
- **Credit, idiosyncratic**: *"German battery maker Varta files insolvency application"*. Single-issuer
  ⇒ **explicitly not an index-level credit event (S26's own invalidation clause)**.

---

## §D · Macro propositions — falsifiable · both branches · anti-signal · KPI · dated catalyst

**P1 — The front-end repricing is a real-rate reaction-function trade whose narrated trigger is oil;
that trigger has now reversed TWICE with the rates still unable to answer.** *(carried, 5th framing)*
- Anchor `[FRED]`: 2y **4.37%** · 10y **4.71%** · real 10y **2.43%** · breakeven **2.26% (asof 07-24,
  flat)** — **all curve values unchanged, `asof` 07-23**. The move remains ~100% **real**.
- Anchor `[news]`: hike odds **by Sept-16 52.4% → 82.4%**; **12% → 36%** for this week's meeting on a
  second named source (§C-3); Rates/Fed is the **only elevated bucket (1.25×)**.
- ★ **New this run**: the oil→rates test is now **doubly unscoreable** — oil fell again (intraday,
  §D-P4) on top of the 07-24 fall, and **FRED has printed neither session.** Logged `unknown` (C3).
- **Both branches (mandatory — oscillating variable):** (a) the FOMC holds, oil keeps falling, the 2y
  retraces → positioning into an event, and TD's fade was right; (b) **DGS2 closes >4.45% or real 10y
  >2.55%** → duration de-rate becomes a regime call and **S19/S9 fire**.
- **Anti-signal (kills P1):** DGS2 **<4.15%**, **or** the decomposition flipping to real-down /
  breakeven-up. Neither can fire before the next FRED publication.
- KPI: DGS2 daily · DFII10 **quoted with** T10YIE · 2s10s · CME hike odds · the oil→2y pass-through.
- Catalyst: **FOMC 2026-07-29 (D-2)** · **June PCE 2026-07-30 (D-3)**.

**P2 — Credit is still the loudest narrative and the quietest market; its pre-registered score could
not be taken.** *(carried, 7th run)*
- Anchor `[FRED]`: **HY OAS 2.77% (07-23), IG 0.79%, NFCI −0.552** — all unchanged, **the 07-24 print
  still absent**. `credit stress` d1 = **0**; the credit bucket is 1.09× = unremarkable.
- ⚠ **The 07-25 run pre-registered the exact numbers for this score and the observable did not print.
  It is NOT re-thresholded and NOT substituted.** The registered line stands verbatim for the next run:
  **HY OAS 07-24 ≥2.85% ⇒ "turn"; ≤2.72% ⇒ "tick"; between ⇒ `AMBIGUOUS`.**
- The only credit item in the feed is **single-issuer (Varta)**, which S26's own text excludes.
- **Both branches:** (a) spreads hold <3.00% → the three OW tilts remain three bets (S26 branch A);
  (b) **HY OAS ≥3.10% with NFCI turning positive WoW** → S26 branch B, and **all three OW carriers lose
  together on one shared beta**.
- **Anti-signal:** HY OAS >3.10% on a close, or NFCI rising two consecutive weeks.
- KPI: HY OAS daily · NFCI weekly. Catalyst: FOMC 07-29 · PCE 07-30.

**P3 — Info Tech's single label is still unresolved, and this run adds no evidence in either
direction.** *(carried, state deliberately frozen)*
- The registered KPI is the **supplier-minus-spender excess-vs-SPY spread, σ-normalized**. **No session
  has occurred. The KPI has no new value. Nothing is claimed.**
- Carried state, unchanged: the spread went **+6.07pp (07-23) → −4.20pp (07-24)**, a 10.27pp sign
  reversal in one session, correctly tagged `indistinguishable` (C4) and n≈1 (S1) at registration.
- **Both branches:** (a) MSFT/META raise capex 07-29 and the spender multiple compresses while
  suppliers hold → **S13 branch A**, IT must be split; (b) the spenders re-rate on the same raise →
  the single label survives and both sessions were noise.
- **Anti-signal (kills P3):** a capex **cut** at MSFT or META (§4 — breaks volume and price legs
  together). ⚠ **Un-narrated by the desk's probe for a 5th time and loudly narrated by the market's**
  (§C-4) — **watch the line item, not the feed.**
- Catalyst: **MSFT + META 2026-07-29 (D-2)** · **AMZN 2026-07-30** ⚠ **date-provider dispute declared
  (D5): `yfinance` says MSFT 07-30 / META 07-30 / AMZN 07-31.** Every bracket is written on a window.

**P4 — ★★ The refining margin's composite is 1.67 points from its restated kill line, and the leg that
is breaking is GASOLINE while the diesel bottleneck WIDENED.** *(carried, materially advanced)*

Settled series `[measured, own calc, yfinance CL/RB/HO continuous — settled-only is a rule (R17)]`:

```
              WTI     Brent   3-2-1 crack  gasoline crack  distillate crack  diesel−gas gap
2026-07-22   86.83    94.07      66.865         56.587          87.420           30.83
2026-07-23   92.19   100.69      66.492         54.659          90.157           35.50
2026-07-24   89.31    96.78      64.304         53.318          86.275           32.96   ← LAST SETTLED
──────────────────────────────────────────────────────────────────────────────────────────
2026-07-27   84.02    90.64      61.665         49.691          85.614           35.92   ⚠ INTRADAY
```

- ⚠⚠ **The 07-27 row is UNSETTLED and is NOT a measurement.** CL volume **174,048 vs 401,934** on the
  last full session (43%). It is printed here **only** so the next run scores it instead of discovering
  it, and **no conclusion in this file rests on it.** This is the R17 discipline applied prospectively.
- ★ **What the intraday row would mean if it settles near there, pre-registered rather than argued**:
  the composite would sit **1.67 points above the restated kill line (settled 3-2-1 < 60)** — the
  closest of the entire advance — **and the diesel-minus-gasoline gap would WIDEN to 35.92, the widest
  in the visible series**, because the distillate crack barely moved (86.28 → 85.61, −0.8%) while the
  gasoline crack collapsed (53.32 → 49.69, −6.8%).
- ★★ **That shape is S8 branch B, not branch A.** S8's frozen text: branch A = *crude below its
  pre-escalation range **AND** the diesel crack rolling over*; branch B = ***crude falls but cracks
  hold*** = *"NOT against us — input-cost relief."* **The distillate leg is holding.** ⚠ But the
  observable is a **settled** comparison and today is not settled ⇒ **S8 stays ARMED and is NOT scored
  this run.** (See §F for the pre-registered scoring line.)
- ⚠ **R19's lesson is applied at registration**: the gap has narrowed on **10 of 24 sessions** since
  06-19, so **neither a widening nor a narrowing is "the first" of anything.** No unprecedentedness
  claim is made.
- **Physical counter-evidence accumulated this run** (§C-7): **Singapore fuel-oil stocks rising** = a
  **second** of M128's five named hubs inverting (after Fujairah +35%); Novorossiysk crude loadings
  resumed; and **M93's dated item lands this week — Russia's diesel export ban expires 2026-07-31.**
- **Both branches:** (a) the composite stabilises ≥62 on settled closes with the diesel gap holding
  above 33 → the margin engine is intact and the fall is a gasoline/war-premium event, i.e. **input-cost
  relief**; (b) **a settled 3-2-1 below 60**, or **the distillate crack breaking below 80** → the
  bottleneck itself is going and the Energy tilt must sit on crude/integrated alone, into a WTI already
  at the **11th COT percentile**.
- **Anti-signal (kills P4), restated on ONE axis per the 07-25 correction:** a **settled 3-2-1 crack
  below 60, regardless of the crude level.** Distance on the last settled close: **4.30 points**.
- KPI: **3-2-1 crack on SETTLED closes only** · **the diesel-minus-gasoline gap** · weekly-mean
  acceleration · WTI COT percentile (next print covers 07-28).
- Catalyst: **VLO 2026-07-30** · **STNG 2026-07-30 (S21 — delivers S8 branch A without a Hormuz
  statement)** · **Russian diesel ban expiry 2026-07-31** · **MPC 08-04 · PSX 08-05**.

**P5 — The digital-infrastructure underweight's stated mechanism stays refuted; its own anti-signal
cannot be read this run.** *(carried, frozen)*
- Registered anti-signal: *"DLR's excess vs SPY fully retracing by 2026-07-31."* **No session ⇒ no
  reading.** Carried state: DLR +6.05σ on 07-24 on a 42.5% FFO beat, raised FY guide and a $3.5bn
  Blackstone datacentre acquisition; EQIX +3.22σ with **no 8-K ⇒ sympathetic, n=1 event**.
- ★ **One corroborating item this run** `[news, embedded market table, `[news]` grade]`: the 07-24 S&P
  500 leaderboard reproduces **Digital Realty 199.08 (+11.01%)** — identical to the price M151 used to
  correct DLR's multiple to **24.4× AFFO** (from the GAAP 67.87 category error). A third-party table
  and the desk's own pull agree to the cent.
- **Both branches / KPI / catalyst** unchanged. **EQIX prints 2026-07-30** (D54 closed) — S25's second
  settling point.

**P6 — The tariff axis is enacted and cross-sector.** *(carried, no new information)*
- Tariff/trade is the **only bucket below its own 7-day share (0.90×)**. Feed items are second-order
  (China ↔ EU export controls; a Greek shipping carve-out; a lower US tariff for India). **Per §C-0
  this absence is bounded by a 96%-unseen single-outlet tier ⇒ `unknown`, not "quiet" (C3).**

**P7 — Japan is the un-priced global-duration channel, and after three flat runs it is back in the
scored tier.** *(carried, status CHANGED)*
- Anchor `[news]`: **five threads** (§C-7), including the yen at a **40-year low** on BoJ rate-hike
  bets and a **$33bn US power project seeking Japanese bank financing**.
- ⚠⚠ **Still `[unverified]` under W2 and NOT admissible as evidence.** *"BOJ tightening leads US
  long-end yields"* has **no lag table in this repo (D22, open)**. DEEP and BET may not cite it.
- ★ **The 07-25 escalation ("either D22 gets built or P7 is retired") is now decidable in P7's favour**:
  it left the unscored tier on its own, so the retirement argument weakens and the build argument
  strengthens. **The decision is still a human's; carried, not resolved.**

**P8 — The rate shock's housing/consumer transmission is still unmeasurable in this repo.** *(carried)*
- **`MORTGAGE30US` is still not wired into `module_macro_us`'s catalog — a third run.** A proposition
  whose KPI cannot be pulled cannot be scored. Carried unchanged so the omission stays visible.

**P9 — ★★★ NEW · The memory cycle's supply side acquired a funded fourth entrant, and the standing
view's capacity clock (M7) names only three.**
- Anchor `[news, prospectus-sourced via Reuters, multi-outlet]`: §C-2 — **$8.6bn raised, explicitly for
  capacity**; **#4 DRAM producer at ~7.7% share (2025)**; **$487bn market value**; **36.29% state-owned
  pre-IPO**; **lags in HBM**; **DoD "Chinese Military Company", possible Entity-List candidate.**
- **What it does NOT do (stated first, so the proposition is not over-read):** it does not change 2026
  supply, it does not touch **M1** (the contract-price second derivative), and it is **`[news]` grade
  with no issuer filing read**. Under **L1** this is a *level*-and-*funding* fact, not a *rate* fact.
- **What it does do:** it puts a **state-funded, captive-demand entrant** against **C1** — the open
  contradiction about whether LTA price floors hold. A floor is a commercial agreement; a subsidised
  entrant with a domestic captive market is the standard mechanism by which one stops binding. **C1
  moves from "unmeasured" to "unmeasured, with a named new counterparty."**
- **Both branches:** (a) CXMT's capex lands in commodity DDR while HBM stays a three-supplier market →
  the AI-memory node is insulated and this is a China-domestic substitution story; (b) **CXMT's
  proceeds compress commodity DRAM pricing into 2027–28 while hyperscaler LTAs reset** → the *trough*
  of the next cycle is deeper than M18's 17-year series implies, and **L2's peak-margin read on MU
  strengthens rather than weakens**.
- **Anti-signal (kills P9):** an actual **Entity List designation** that blocks CXMT's equipment access
  (the capacity money then cannot be spent), **or** a disclosed CXMT capex plan materially below the
  raise.
- KPI: CXMT's disclosed capex plan · DRAM contract price QoQ (**M1**, the existing series) · whether
  any 2027 capacity guide from SK/Micron/Samsung cites a fourth supplier.
- Catalyst: **`[blank]` — no date is guessed.** Nearest scheduled read-through: **MU FQ4, ~2026-09
  (S4)**; **4Q26 DRAM contract guidance ~2026-09/10 (S3)**.

---

## §E · ★ SECTOR TRANSMISSION MATRIX — the deliverable (ROTATION's input)

> ⚠⚠ **ZERO tilt changes this run, and that is a decision, not an omission.** There has been **no US
> session** since the matrix was last set, so there is **no Δ column** — every sector's price evidence
> is the 07-24 evidence the prior run already used. Changing a tilt on an unsettled bar or on a
> headline would be the R17/R19 failure class, twice retracted. **What changed is the *watch state* of
> three sectors, which is recorded in the last column.**

| # | GICS Sector | Tilt | Δ | Driving prop. | Watch state after today's news axis |
|---|---|---|---|---|---|
| 1 | **Energy** | **OW−** | **hold** | **P4, P9-adjacent** | ⚠ **The nearest-to-kill tilt on the board.** Settled crack 64.30 vs a kill line of 60; the unsettled 07-27 print sits at **61.67**. ★ But the leg breaking is **gasoline** — the **distillate crack held (−0.8%) and the diesel gap widened to 35.92 intraday**, which is **S8 branch B (input-cost relief), not branch A**. ⚠ Physical counter-evidence added: **Singapore fuel-oil stocks rising = a 2nd of M128's five hubs inverting**; **Russia's diesel export ban expires 07-31**. **VLO 07-30 · STNG 07-30** |
| 2 | **Info Tech** | **N (split unconfirmed)** | hold | **P3, P9** | ★★ **P9 is new and it is a supply-side fact the sector's own regime call does not contain** (CXMT: $8.6bn for capacity, #4 DRAM producer, $487bn cap). It bears on **C1/C3**, not on this week's tape. **S13's cross-condition lands 07-29** and is unaffected by a run with no session |
| 3 | **Financials** | **OW−** | hold | P1, P2 | Front-end still at a 120-day high (07-23). ⚠ **S23's bear-flattener-hold branch is the live risk**, not S19's hike — it kills NIM without tripping either registered threshold. Credit's first adverse tick is **unscored** because HY OAS 07-24 has not printed. **S14/S14-num 07-30** |
| 4 | **Industrials** | **OW−** | hold | P4, S20 | ⚠⚠ **UPS prints TOMORROW and is absent from the calendar for a 7th run.** It is the registered falsifier of the rail node **and** W4/D23's last customer. ⚠ **D52 blocks the short-vol read on both UPS (base 57.7%) and UNP (base 52.2%)** — the two names that matter most tomorrow are the two whose only "who is trading" axis is unreadable. **M91 stands: ~8 of UNP's 12 growth points are fuel surcharge**, so a falling crack hits the rail leg through the same tick |
| 5 | **Health Care** | **N** | hold | C7 | No new information. C7's resolving observable (one 🟢 from outside the top-6 by cap) is unchanged at **zero of 26**; horizon **08-06** |
| 6 | **Comm Services** | **N−** | hold | P3, S16 | **META prints 07-29 (S16).** No regulatory print in the feed. Held N− with S16 explicitly unsettled |
| 7 | **Utilities** | **N−** | hold | P1, **S24** | ⚠ **S24 is the live bracket here** — a capex raise that **re-rates the physical layer** inverts this UW. Feed corroborates the demand side three ways (**$500bn+ hyperscaler capex**, **SK–Nvidia $500bn**, **Nvidia's $250bn OpenAI backstop**) ⚠ with **n≈1 declared at registration** (VST–CEG +0.768) |
| 8 | **Real Estate** | **N** | hold | P5 | Anti-signal unreadable without a session. **EQIX prints 07-30** = S25's second settling point. ★ **K8 — R7's replacement 20-session block — opens today (≈07-27 → 08-21)**; DEEP RE may not re-cite the old block as fresh |
| 9 | **Materials** | **UW** | hold, **disagreement still declared** | P1, P6 | The 07-25 run declared *"if XLB beats SPY again next session the UW needs re-argument."* **There has been no next session.** The test is **deferred, not passed** — stated so it cannot silently lapse. Copper still 98th COT percentile |
| 10 | **Cons. Discretionary** | **N−** | hold | P1, P8, P6 | Rate-sensitive into a 2y at a 120-day high; **P8's KPI still unpullable** (`MORTGAGE30US` unwired, 3rd run) |
| 11 | **Cons. Staples** | **N** | hold | P1, P6 | No new information |

**Wind summary.** **Direction unchanged on all eleven.** The two facts that move the *board's* state
are both off the price axis: **(i) the oil de-escalation is a strike pause, not a strait reopening —
the physical observable is unchanged and the composite crack is breaking on gasoline while distillate
holds**, which is the branch of S8 that is *not* against the Energy tilt; **(ii) a funded fourth DRAM
entrant arrived (P9)**, which touches the memory regime call's supply clock and C1 rather than this
week's tape. **Three sectors carry a binary inside four sessions with a currently-unreadable
positioning axis** (Industrials/UPS via D52, Financials/S23 via the unprinted HY OAS, Utilities/S24
via an n≈1 unit).

**DEEP candidates handed to ROTATION** (ROTATION owns the final pick):
**① Energy (P4)** — the nearest-to-kill tilt, with a **gasoline-vs-distillate decomposition that
points the opposite way from its own composite**, two dated prints (VLO/STNG 07-30) and a dated
physical catalyst (Russian ban expiry 07-31).
**② Info Tech / memory (P3 + P9)** — a supply-side entrant the standing view does not contain, plus
**S13 on 07-29**, plus C1 finally having a named counterparty.
**③ Industrials / rail–freight (S20)** — the only sector whose registered falsifier **fires tomorrow**,
and whose two key names are exactly the two D52 makes unreadable.
**④ Financials (S23)** — the bear-flattener-hold branch that kills NIM without tripping S19 or S9,
plus **S14 07-30**.
**Swing, flagged to PREMORTEM: Utilities (S24)** — a levered short on AI capex, two days before the
capex prints, with n≈1 declared.

---

## §F · Self-backtest

### Scoring the 2026-07-25 propositions — per KPI, with `unknown` where the observable did not print

| Prop | Registered KPI / threshold | Verdict this run |
|---|---|---|
| **P1** | oil → 2y pass-through | **`unknown` (C3), 2nd consecutive run** — FRED has printed neither 07-24 nor 07-27 |
| **P2** | **HY OAS 07-24 ≥2.85 ⇒ turn / ≤2.72 ⇒ tick / else AMBIGUOUS** | **UNSCOREABLE — the observable did not print.** Threshold **not** moved, proxy **not** substituted |
| **P3** | supplier−spender σ-normalized spread | **No new value — no session.** Nothing claimed |
| **P4** | settled 3-2-1 crack <60 (restated, one axis) | **NOT triggered on the last settled close (64.30, 4.30 away).** Intraday 61.67 is **not admissible** |
| **P5** | DLR excess vs SPY fully retracing by 07-31 | **No new value — no session** |
| **P6** | `[blank]` implementation date | unchanged |
| **P7** | presence in the scored news tier | ★ **STATE CHANGE — left the single-outlet tier after three flat runs** (5 threads) |
| **P8** | `MORTGAGE30US` | **still unwired — unscoreable by construction, 3rd run** |

★ **Six of eight KPIs are unscoreable at this clock, and none of them was narrated into a verdict.**
That is the correct outcome for a run with no session, and it is recorded as such rather than papered
over with a "state check."

### Scenario scoring — S12, and the two brackets that could have been over-scored today

- **S12 — STILL PENDING, 5th check, and logged as the pre-declared process failure.** `DTWEXBGS` reads
  **120.5315 asof 2026-07-17**, byte-identical for **10 calendar days**; range unchanged
  **[117.4396, 121.412]**. The 07-27 KR run pre-declared *"a 5th carry IS a scoring failure and must be
  logged as one"* — **it is logged.** ⚠ **Not scored early**: the frozen deadline is **2026-07-28** and
  a print tomorrow could still carry a post-event value. **The next desk to run on or after 07-28
  scores it `AMBIGUOUS` if unprinted — no proxy, no 6th carry.** The decision axis is already
  `AMBIGUOUS` (D35). Root cause remains **D46** (a 3-session window on a ~5-business-day-lag series).
- ★ **S8 — deliberately NOT scored, and this is the run's most important act of restraint.** The day's
  #1 event is a Hormuz de-escalation headline. **S8's frozen observable is "crude below its
  pre-escalation range AND the diesel crack" — a settled-price comparison — and there is no settled
  bar.** Beyond the clock, the body read says the **strait remains closed** and Deutsche Bank says
  traffic remains *"severely disrupted"* ⇒ scoring branch A off a strike pause would be scoring the
  **price reaction instead of the observable**, which L3 `scenario_score` forbids in writing.
  **Pre-registered so the next run scores rather than discovers**: on the **settled 2026-07-27 close** —
  *branch A* if 3-2-1 < 60 **and** the distillate crack < 80; *branch B* if crude falls while the
  **distillate crack holds ≥ 84**; otherwise **AMBIGUOUS**. Thresholds frozen now, pre-outcome.
- **S19 / S23 context, not a score**: hike pricing rose to **82.4% by Sept-16** on a driver (oil) that
  reversed after the pricing was set. **Neither bracket's observable (the decision; T10Y2Y with DGS2)
  exists until 07-29.**

### Failure classes logged this run

1. **A headline that inverts on its body read.** "Oil plunges as US and Iran pause strikes over the
   Strait of Hormuz" reads as a strait reopening; the primary text in **two independent outlets** says
   it **remains closed**. A desk ranking events by outlet count and stopping there would have scored
   S8 branch A today. **The body read is what stopped it.**
2. **The term axis was blind to the day's biggest event** (oil bucket **1.01×**). Documented behaviour,
   measured again — and a warning to any stage that gates on term velocity this week.
3. **The desk's own feed carried the CXMT story for four days at 3–6 outlets and two runs missed it**
   (§C-2). **New dig D71.**
4. **D57 reproduces**: yfinance reports **byte-identical volumes for 07-23 and 07-24** on all four legs
   (CL 401,934 · BZ 48,567 · HO 22,882 · RB 25,390) while the closes differ. The volume column is the
   desk's only settled-vs-unsettled defence; it worked today (07-27 volume is clearly partial) but it
   is duplicating across adjacent days again.

---

## §G · Corrections and retractions filed by this stage

**None.** No claim from a prior run is retracted here. Two are **narrowed**, and both narrowings are
about *scope*, not direction:

- **M45's Bab el-Mandeb blockade** is being **transited** — *"Chinese Tankers Push Through Bab
  el-Mandeb Despite Houthi [threats]"* (4→4→2→2 outlets). M45's measured fact (the tanker names did not
  rally on the news) is untouched; the *"declared blockade"* framing around it is weaker.
- **M128's "inventories below the 5-year range in PADD1, PADD3, ARA, Fujairah AND Singapore"** now has
  **two of its five named hubs inverted** — Fujairah (+35%, already on file) and **Singapore (fuel-oil
  stocks rising, this run)**. ⚠ **Fuel oil is not middle distillate**, so this is a **directional
  corroboration of an inventory build, not a like-for-like refutation (C2)**. Recorded at that strength
  and no stronger.

---

## §H · Rule-linter result

`python -X utf8 scripts/report_lint.py llm_outputs/2026-07-27/industry_US/MACRO_REPORT.md` →
**✅ 0 findings** (rules C1 · C2 · S6 · D6). ⚠ **Form-only. A clean linter run is not a correct
report** — it cannot see that S8 was left unscored on purpose, that six of eight KPIs are
unscoreable, or that the 07-27 crack row is an unsettled bar. Those are §D/§F's job, not the linter's.

## §I · New digs registered by this stage

| # | Dig | Why it matters | Owner |
|---|---|---|---|
| **D71** ★★ | **The desk missed a four-day, 3→6→3→16-outlet build on the single largest supply-side event for its own regime call** (CXMT's IPO week). The event axis carried it on 07-21/07-23/07-24 and neither the 07-25 US run nor the 07-27 KR run read it. | The `thread` tool exists precisely to convert "day 1 at 3 outlets" into a lead, and it was run on 07-25. **The gap is not the instrument — it is that no stage owns "a BUILDING thread with no matching bucket."** MACRO's own L2 text names this as use-case (c) and no EXIT CHECK enforces it. **Minimum fix: MACRO must list every BUILDING/REIGNITED thread that maps to no term bucket, and either open a bucket or state why not.** | MACRO / EXIT CHECK |
| **D72** ★ | **`Hormuz open` d1 = 0 on the day of the month's largest Hormuz event.** The kill-phrase probe is a phrase no outlet writes. | The **US analogue of D68** (the KR kill-switch's false all-clear). `CATALYST_WATCH` carries the undated *"Iran 'Strait of Hormuz open' statement"* as a watched binary, and the term that would detect it returns 0 on the day it nearly happened. **Minimum fix: define the trigger as a set of single tokens (`reopen`, `transit`, `de-escalation`, `blockade lifted`) and report the hit count beside every verdict.** | DRIFT / `catalyst_calendar` |
| **D73** | **`us_flow.py`'s FINRA verdict is unreadable on 3 of the 8 names in this week's pre-event set** (UPS base 57.7% · UNP 52.2% · MPC 55.1%, all far outside the tool's own 40–45% band). | This is **D52 with a cost attached**: it is not a general caveat any more, it is the reason the desk cannot read positioning on **UPS and UNP the day before S20 settles on them**. **Minimum fix (unchanged from D52): print the baseline beside the z and suppress the verdict string when the baseline is out of band.** | `scripts/us_flow.py` / human |

---

## ✅ EXIT CHECK

- [x] Catalysts injected (`--days 10`, not the 5-day default, because ARMED dates run to 08-12);
      **16 binaries logged; D18's 7th and D61's 3rd occurrence named.**
- [x] Events read via `--body 2`; **tail = 0**.
- [x] **`tail = 0` is not treated as the coverage claim**: `single_source` **15/379 = 364 withheld
      (96.0%)**, `excluded_nonmarket` **0/0**, `subevents` **72 recovered** — all quoted, and every
      absence claim in §D is written as `unknown` (C3) rather than "quiet".
- [x] **Denominator quoted**: 2,095 articles → 329 clusters → 329 market events (non-market 0).
- [x] Trajectories read (`thread --days 7`); every proposition carries a thread state or says "no
      thread"; **P7's tier change and the CXMT REIGNITED curve both came from this pass**; the
      weekend-denominator caveat on FADING tags is stated with the per-day counts.
- [x] 7-bucket sweep run **with terms as separate argv** and **pool-normalized**; the flat oil bucket
      (1.01×) is reported as a finding, not as quiet.
- [x] Blind-spot pass run **with its own denominator** (400 of 8,678 = 4.6%); the "no new term" claim
      is explicitly labelled weak at that sample.
- [x] **Both halves cited** on the headline print (headline CPI 4.2% → 3.5% YoY **with** core 2.6%;
      the FRED-derived MoM pair carried alongside).
- [x] **Every relative-performance number names its benchmark inline**; ⚠ this run has **no** new
      relative-performance numbers, because there is no session — stated rather than manufactured.
- [x] **Credit axis read and cited** (HY OAS 2.77% · IG 0.79% · NFCI −0.552), and the one credit item
      in the feed is labelled **single-issuer**, i.e. explicitly not index-level.
- [x] **`real_10y` quoted with `breakeven_10y`** (2.43% vs 2.26%) — the move remains ~100% real.
- [x] Transmission matrix produced, **all 11 sectors, zero tilt changes, with the reason for zero
      changes stated up front.**
- [x] Self-backtest appended **per KPI**, with six of eight recorded `unknown`/unscoreable rather than
      narrated; **S12 logged as the pre-declared 5th-carry process failure**; **S8 deliberately not
      scored, with its settled-close thresholds frozen now.**
- [x] New blind-spot terms folded back: **none admitted** (SpaceX/Bitcoin have no vehicle in
      `us_top300`; Japan is already P7's channel) — stated, not silently skipped.
- [x] **Zero buy/sell language, zero sizing (P4). English-pure.**

---

## §5 · DRIFT ADDENDUM — appended 2026-07-27 by stage 10 (append-only; nothing above is rewritten)

**Verdict: NO kill-switch fired.** The elevated terms are both sides of the same event §C-1 already
body-read, and the body read that mattered survives the re-check.

### ⚠ The instrument failed for a FIFTH consecutive run, and its backup failed too

- `scripts/drift_watch.py --report …` → **`rc=2: 'drift' 는 원격 실행 불가(조회 전용)`** — **D17/D64,
  5th consecutive occurrence.** The client-side `DB_READ_CMDS` edit has never been deployed to the
  running server (**P6**: a `git pull` + API restart, pending five runs).
- `module_news_data burst --scope foreign` → **`TimeoutError` on the remote news API** — **D55, third
  consecutive failure.** ⇒ **Both "find what I did not think to query" instruments were down again.**
- ⇒ The substitute below can only test phrases **already thought of**. **A clean sweep here means
  "none of the known phrases fired", NOT "nothing happened."** Stated, because that distinction is the
  whole reason this stage exists.

### Kill-switch sweep — the substitute's result

Pool **d1 = 5,078** articles (up ~8% from the 4,707 read at §C-5, i.e. this is a genuinely later
snapshot, not a re-read of the same window).

| Term | d1 | Term | d1 |
|---|---|---|---|
| **escalation** | **202** | recession | 65 |
| **AI spending** | **148** | rate cut | 32 |
| **ceasefire** | **78** | glut | 14 |
| oversupply | 5 | Hormuz reopen | 2 |
| guidance cut | 1 | **capex cut** | **0** |
| **credit stress** | **0** | blockade lifted | 0 |

★ **`ceasefire` (78) and `escalation` (202) are elevated together and point opposite ways** — which is
not a regime flip, it is the same 07-27 event carrying both of its branches, exactly as §C-1 read it.
★ **`capex cut` returns 0 for a SIXTH consecutive measurement** while `AI spending` runs **148** on the
same window. **D52's case is now six measurements deep** — the probe is measuring the desk's
vocabulary, not the market's.
★ **`credit stress` = 0** with HY OAS unprinted since 07-23 ⇒ **P2's state is unchanged and still
unscoreable**; no narrative-only credit claim is admissible.

### The three items body-read rather than counted

1. ★★ **A concrete Hormuz mechanism appeared, and it is the first one with a shape**
   `[fortune, 2026-07-26]`: *"A deal is being negotiated that centers around having **Iran run vessel
   transit through the Strait of Hormuz with fewer restrictions on ships**"* — both sides reportedly
   wanting to return to the interim ceasefire deal. ⇒ **This is S8's undated trigger acquiring a
   described mechanism for the first time.** It remains a **negotiation, not a reopening**, at low
   outlet count, and **the strait is still closed.** ⚠ It is also **D72 in miniature**: the desk's
   registered probe `Hormuz reopen` returned **d1 = 2** on the day this printed — the phrase nobody
   writes, again.
2. ⚠ **Escalation did not stop while the pause held** `[guardian 07-25 · fortune 07-25]`: the Houthis
   claimed a missile attack on Saudi Arabia and called the exchange a *"dangerous escalation"*; the US
   military went **silent** on Iran airstrikes while Houthi–Saudi exchanges continued over Red Sea
   shipping. **The pause is between two of the actors, not among all of them** — consistent with
   Deutsche Bank's *"fragile… with side battles still ongoing"* quoted in §C-1.
3. **Europe's strain persists past the relief** `[euronews 07-27, title]`: *"Hormuz crisis puts
   Europe's oil market under further strain following post-ceasefire relief."*
   And, intraday and therefore **inadmissible as a measurement**: *"Futures Jump As **Brent Tumbles
   Below $90** On Fresh Round Of Iran Ceasefire Optimism"* `[zerohedge, title-only]` — a further leg
   below the 90.64 intraday print recorded in §D-P4. **Logged as an observation for the next run's
   settled score, not as a number this run uses.**

### What did NOT change, and is therefore re-affirmed

**§C-1's body read survives the re-check on fresh articles**: the pause is real, the strait is closed,
side-fronts are live, and no primary source anywhere in this window says the waterway reopened.
**S8 stays ARMED with the thresholds MACRO §F froze pre-outcome for the settled 07-27 close.**

### What the next run must re-read first

1. **The settled 2026-07-27 close** — it scores **S8** against a frozen line, and it is the first new
   US price data this desk will have had in three calendar days.
2. **`DTWEXBGS`** — **S12's deadline is 2026-07-28. A 6th carry is not available.**
3. **HY OAS for 07-24** — P2 pre-registered its exact numeric score and the observable still has not
   printed.
4. **UPS, 2026-07-28** — S20 + S20-ANNEX, and the two names it settles on (UPS, UNP) are the two whose
   positioning axis D52/D73 makes unreadable.
