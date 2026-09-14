# MACRO_REPORT — industry_US · 2026-08-15 (Sat KST) · Stage 3/11 (L1·MACRO)

> Runtime `--market us` · news `--scope foreign` on every call. Prices **asof 2026-08-14 settled**.
> Benchmark named inline on every relative number (**C1**). No sizing, no buy/sell language (P4).

## ⚠⚠ THE DEFINING FACT OF THIS RUN, STATED FIRST

**Two macro prints landed on 08-13 and 08-14 and they pushed the rate path the OPPOSITE way from the
one this desk has carried for three weeks — while oil went UP.** Soft PPI (08-13) and then weak retail
sales + a sharp drop in consumer sentiment (08-14) sank Fed **rate-hike** odds
[`seekingalpha`·`bloomberg`·`nasdaq` 08-14], and they did it in the same five sessions in which the
Hormuz crisis drove **`XLE` +7.271 excess vs `SPY`** and the 3-2-1 crack **+6.67 points**.

**That combination is a direct falsification test of `P57`** — the desk's twice-measured claim that the
Fed-hike premium is an **oil function** (`M69` 07-24, `M658` 08-13). **Oil rose and hike odds fell.**
The coupling did not weaken; it **inverted**, and the named drivers are **demand data**, not oil.
This is scored in §F and it is the reason the transmission matrix in §G moves.

---

## §0 · Instrument state — and this stage's first D48 self-refutation

🚨 **PREFLIGHT G1's revocation is REFUTED for this run, and the refutation reproduces `P60` exactly.**

| Time (KST) | Probe | Result |
|---|---|---|
| **22:14** | `module_news_data fts search Nvidia --days 7 --count --scope foreign` × 5 names | **5/5 FAIL** — `URLError(FileNotFoundError(2))` |
| **22:1x** | local fallback (`DEGAJA_NEWS_API=`) | **`색인 없음`** — `data/news_fts.db` is **0 bytes** |
| **23:0x** | `exec_remote(base, ['fts','search','Nvidia','--days','7','--count','--scope','foreign'])` | ✅ **3,705 hits** |
| **23:1x** | **the identical CLI command, re-run** | ✅ **3,729 hits** — `(via NEWS API @ …ngrok-free.dev)` |
| 23:1x | `exec_remote` at the same moment | ✅ **3,729** — the two agree exactly |

⇒ **The bridge was never down; it flapped.** This is the **second consecutive run** in which a 5/5
failure at ~22:15 became a clean success ~40–50 minutes later (08-14: 5/5 fail 22:15 → 3/3 success
22:34/22:44/22:55). **`P60` — *"single-probe revocation is a measured error"* — is HIT again, and this
run's own PREFLIGHT made the error a second time.**

**What that changes, written here rather than edited into PREFLIGHT** (§4c of HANDOVER, D48 class):

| PREFLIGHT said | Measured here |
|---|---|
| "the CLI path is dead 5/5" | **True at 22:14, false at 23:1x.** A rights table with no timestamp on the probe is not a rights table |
| "`theme_age`/`chain_hop`/`drift_watch` ride the CLI transport ⇒ not citable" | **The transport reason is withdrawn.** `theme-age` runs and returns output. ⚠ **The revocation SURVIVES on a different, stronger ground** — `D260`: its acceleration denominator tracks the **corpus**, not the theme. **Not citable, for the right reason** |
| implied: the desk cannot read news today | **The desk read 38,115 foreign articles over 7 days and ran a full pool-normalised term sweep** (§D) |

★ **New, and it closes a five-run-old dig.** `drift` is refused by the server:
`'drift' 는 원격 실행 불가. 허용: ['blindspot','burst','chain-hop','coverage','export','fts','search','theme-age']`.
But this repo's **client** allow-list `module_news_data/__main__.py:51` **does contain `drift`**.
CLAUDE.md P6 names `__main__.DB_READ_CMDS` as the single source and says `Server/news_api.py` imports
it — **so the server is running an older copy of that set.** ⇒ **`D17` ("`drift` is remote-unrunnable",
logged 5 runs) is not a design limit; it is a stale server checkout needing `git pull` + API restart.**
Registered as **`D267`**.

🚫 **Two instruments are structurally unavailable to this client and always were** — `brief` and
`thread` are marked **클라 전용 (client-only)** in the parser and are refused by the server. The client
has **no `news_alert.db`**. ⇒ **The events pass and the trajectories pass cannot be run on this
machine.** That is a standing architecture fact, not today's outage, and it is stated so no downstream
stage reads "no thread cited" as "no thread existed". Substitute used: the **pool-normalised term
sweep + direct FTS body reads** in §D. Registered as **`D268`**.

**Binding constraints that survive PREFLIGHT unchanged**: `flow_score` is **3-axis** (stated on every
line that uses it) · **no `wflow` promotion/demotion for IT, Industrials, Materials** (G3 flippers) ·
caps are **31 days stale** · no single-number concentration · sizes are "mechanical ¼".

---

## §A · Primaries — `[FRED]`, with both halves of every print

| Series | Value | asof | Δ vs prior obs |
|---|---|---|---|
| `DFF` fed funds | **3.63%** | 08-13 | 0.00 |
| `DGS10` 10y | **4.63%** | 08-13 | **−0.05** |
| `DGS2` 2y | **4.15%** | 08-13 | **−0.05** |
| `DFII10` real 10y | **2.39%** | 08-13 | **−0.03** |
| `T10YIE` breakeven 10y | **2.27%** | **08-14** | **+0.03** |
| `BAMLH0A0HYM2` HY OAS | **2.71%** | 08-13 | 0.00 |
| `BAMLC0A0CM` IG OAS | **0.79%** | 08-13 | 0.00 |
| `NFCI` | **−0.549** | 08-07 | −0.003 (loosening, 6th week) |
| `VIXCLS` | **14.63** | 08-13 | +0.08 |
| `DTWEXBGS` broad dollar | **119.065** | 08-07 | −0.446 |
| `UNRATE` | **4.1%** | 2026-07 | 4.3 → 4.3 → 4.2 → **4.1**, three consecutive falls |
| `CPIAUCSL` / `CPILFESL` | 332.813 / 336.789 | 2026-07 | July CPI **MoM +0.074% / YoY +3.30%**; core **MoM +0.215%** |
| `M2SL` | 23,155.2 | 2026-06 | +99.6 |

**Both halves, as the rule requires:**
- **July CPI**: the benign sequential (**+0.074% MoM**) sits on a **June base of −0.42% MoM**, and
  **core MoM ACCELERATED −0.017% → +0.215%**. Quoting the headline alone reverses the meaning.
- **Curve**: `2s10s` = 4.63 − 4.15 = **+0.48**, *identical* to 08-12's +0.48 — **but the level shifted
  down 5bp in parallel.** ★ **This breaks `M653`'s stated premise.** `M653` (08-14) read *"the move is
  entirely long-end, with `DGS2` unchanged (4.26 → 4.20)."* **`DGS2` is now 4.15 — the front end moved
  −5bp in one session.** The term-premium story is not dead, but its distinguishing feature — a pinned
  front end — **stopped holding on 08-13**, and the 08-14 news names why (§D).
- **Real vs inflation**: `DFII10` **2.39** + `T10YIE` **2.24** (08-13) = 4.63 exactly. The real leg fell
  3bp and the breakeven then rose to **2.27 on 08-14** ⇒ the most recent single move available is
  **inflation-compensation UP while the real leg came down.** ⚠ That is one observation on a
  one-day-longer series (S1); it is *not* a regime statement.
- **Credit refuses to confirm anything, for a 4th run**: HY OAS **2.71% flat**, 8bp off its 365-day low
  (2.63); IG **0.79% flat**; `NFCI` loosening. **Any risk-off claim in this run is labelled
  narrative-only** — credit does not carry it.

⚠ **Staleness stated, not papered over**: the H.15 block ends **08-13**. The 08-14 session — the very
one that moved rate expectations — **is not in `[FRED]` yet** except for `T10YIE`. Everything said
about 08-14 rates below is `[news]`, tagged as such.

---

## §B · Positioning — CFTC COT (Tue 08-11 close, released 08-14). Context, never a trigger.

| Instrument | Net spec | Weekly Δ | 1y %ile | Read |
|---|---|---|---|---|
| **S&P 500 e-mini** | **+11,280** | **+38,538 ▲** | **88th** | 🟢 crowded LONG |
| **Nasdaq-100** | **−42,905** | −7,899 ▼ | **0th** | 🔴 crowded SHORT |
| Russell 2000 | −13,943 | −5,044 ▼ | 18th | 🔴 crowded short |
| **UST 10Y** | −915,053 | **+64,190 ▲** | **7th** | 🔴 crowded short (covering) |
| UST 2Y | −1,021,043 | −16,815 ▼ | 63rd | 🟡 neutral |
| **USD Index** | +21,409 | −1,090 ▼ | **80th** | 🟢 crowded long |
| WTI crude | +23,226 | +193 ▲ | 18th | 🔴 crowded short |
| Nat gas | −197,135 | +411 ▲ | **2nd** | 🔴 crowded short |
| **Copper** | +80,388 | +3,265 ▲ | **100th** | 🟢 crowded long |
| Gold | +217,940 | +20,306 ▲ | 49th | 🟡 neutral |
| Silver | +23,646 | +1,366 ▲ | 33rd | 🟡 neutral |

★★ **The intra-equity split widened to its largest measured value.** `M125` (07-25) recorded a
**79-percentile-point** spread between Nasdaq-100 and the S&P 500 inside one asset class. Today it is
**88 vs 0 = 88 points**, and it widened **from both ends in one week**: S&P **+38,538 contracts added**
(the largest weekly change on the board) while Nasdaq-100 went **further short**. ⇒ **speculators are
buying the index and selling its largest component's benchmark.** ⚠ This is positioning, not demand
(**D6**) — it is rebound ammunition on the tech side and crowding risk on the index side, and it dates
to **Tuesday 08-11**, i.e. **before both prints** in §D.

★ **WTI at the 18th percentile SHORT while the Hormuz axis escalates** (§D) is the single most
asymmetric cell on this board.
⚠ **Copper 100th percentile long against `FCX` being the worst Materials name at −4.894 excess vs
`SPY`** — `P59`'s configuration, replicated (§F).

---

## §C · The tape — settled through 2026-08-14, benchmark `SPY` named inline

**`SPY`: 08-12 772.49 · 08-13 777.88 · 08-14 776.34.**
★ **08-13 was a record close** [`investing_en` 08-14: *"S&P 500 hits record high on soft PPI"*], and
**08-14 gave back −0.20%** as consumer sentiment printed weak. `SPY` +0.40% / 5d · **+4.45% / 20d** ·
+5.81% / 60d.

★★ **And it is happening on a thinning tape.** Last-bar volume ÷ prior-20-day average, median across
300 names: **08-13 = 0.732 → 08-14 = 0.649**. Two consecutive sessions at roughly two-thirds of normal
volume, the second one making and then giving back a record. PREFLIGHT **G0 PASS** licenses reading
this as real rather than as a clock artifact (weekend run ⇒ the bar cannot be a stub).

### Sector excess vs `SPY` (%, settled 08-14)

| ETF | exc5 | exc20 | exc60 |
|---|---|---|---|
| **RSPT** (EW tech) | **+2.030** | **+6.979** | **+9.800** |
| XLK | +0.687 | +3.766 | +3.873 |
| **XLE** | **+7.271** | +2.887 | −4.796 |
| RSP (EW 500) | +0.819 | −0.041 | +4.683 |
| XLB | −1.004 | −0.469 | +1.330 |
| XLI | +0.320 | −0.489 | +4.724 |
| XLV | +0.622 | −0.548 | +7.803 |
| XLF | +0.574 | −1.069 | **+8.009** |
| XLY | −1.783 | −2.056 | −3.052 |
| XLC | +1.130 | −2.368 | **−8.311** |
| XLP | +0.741 | −3.390 | −5.807 |
| XLRE | +0.246 | −4.777 | −2.780 |
| XLU | +1.207 | **−6.350** | −5.875 |

**Three readings, each with its own number:**

1. ★★★ **Equal-weight tech beats cap-weight tech on all three windows** — `RSPT − XLK` = **+1.343
   (5d) · +3.213 (20d) · +5.927 (60d)**. This is **`S85`'s registered observable** (settles 08-21,
   branches A ≤ −0.994 / B ≥ +2.046). **Live state +1.343 ⇒ branch C**, i.e. the IT N+ promotion is
   currently **neither confirmed nor falsified** by its own falsifier. Reported, **not scored** — the
   settle is 08-21.
2. ★★★ **`S84`, the mandatory Hormuz bracket, is already sitting in branch-B territory.** Its
   observable is `[XLE exc5] − [EW{XLU,XLRE} exc5]`, branches **A ≤ −3.174 · B ≥ +5.544**, settle
   **08-21**. Today: **+7.271 − (+1.207 + 0.246)/2 = +6.545 ⇒ ABOVE branch B by 1.00pp**, four
   trading sessions before it settles. ⚠ **Reported as a live state, NOT scored** (D242 — the row
   settles on its terminal date, and improvising an early read is exactly what this desk forbids).
3. **The duration complex turned up on the 5-day window while still being the worst on 20 days** —
   `XLU` exc5 **+1.207** (2nd best of 11) against exc20 **−6.350** (worst of 11); `XLRE` +0.246 vs
   −4.777. **That turn is dated to the two sessions in which hike odds fell.** It is the single
   observation that most threatens `P56`, and it is put here rather than buried in §F.

### Energy's internals — the crack, decomposed (own calc, settled `CL=F`/`RB=F`/`HO=F`)

| | Value |
|---|---|
| 3-2-1 crack, 08-14 | **66.72** (08-10 64.32 → 08-11 64.16 → 08-12 65.29 → 08-13 65.84 → **08-14 66.72**) |
| 5-session change | **+6.67 points** (from 60.04) |
| 20 sessions ago | 69.41 ⇒ **the rate turned up; the level has not recovered** (lens B1) |
| Percentile | **86.7th of 90 days · 95.2nd of 250 days** |
| Legs, 5d | **`HO=F` +9.75% > `RB=F` +6.66% > `CL=F` +5.40%** |
| Legs, 20d | **`HO=F` +5.37% · `CL=F` −0.11% · `RB=F` −6.15%** |

★★ **The 20-day decomposition is the finding**: over a month **crude is flat and gasoline is down,
while distillate is up 5.4%.** The margin's strength is a **distillate** phenomenon, not a barrel
phenomenon — and a named third party says the same thing independently: **Jefferies — *"Hormuz Shock
Manifesting Itself In Cracks, Not Crude"*** [`zerohedge` 08-13].

---

## §D · News — pool-normalised, `--scope foreign`, and what could NOT be read

**Denominator first (corrected pool, from `coverage`):** foreign window pool **d1 = 9,705 · d7 =
38,115 · d30 = 143,925**. 7-day daily average **5,445**; 30-day daily average **4,798** ⇒ the week is
running **1.135×** the month. **Today's pool ratio d1 ÷ avg7 = 1.782×** — every velocity below is
divided by it (**`D255`**). Body-holding share of the pool: **68.4%**; measured recall of an 8-term
desk search against body matches: **53.2%, i.e. 46.8% body-blind** — quoted so no "quiet" claim below
is read as complete.

### D-1 · Term sweep, pool-normalised (d1 vs d7 daily average ÷ 1.782)

| Term | d1 | d7 | raw | **pool-norm** |
|---|---|---|---|---|
| **PPI** | 115 | 253 | 3.18× | **1.79×** |
| **term premium** | 4 | 10 | 2.80× | **1.57×** |
| **trade deal** | 10 | 27 | 2.59× | **1.45×** |
| tariff | 516 | 1,710 | 2.11× | 1.19× |
| default | 98 | 348 | 1.97× | 1.11× |
| DRAM | 65 | 251 | 1.81× | 1.02× |
| high yield · rate hike · hyperscaler · capex · rate cut · Nvidia | — | — | — | 0.95–0.99× |
| Fed · FOMC · inflation · data center | — | — | — | 0.91–0.93× |
| tanker · memory · oil price · refinery · AI capex | — | — | — | 0.82–0.87× |
| **Iran** | 459 | 2,322 | 1.38× | **0.78×** |
| **Hormuz** | 265 | 1,527 | 1.21× | **0.68×** |
| CPI · CXMT · credit spread | — | — | — | 0.60–0.66× |
| China export | 0 | 13 | — | 0.00× |

**Nothing approaches a 3× burst. The highest reading on the board is 1.79×.**
⚠ **And the ranking inverts the tape.** `Hormuz` is **0.68× — decelerating** in coverage while `XLE`
posts **+7.271 excess vs `SPY`** and Trump escalates to a territorial claim (D-2). ⇒ **term velocity
did not find this run's largest sector move**, which is the `M196` failure mode replicated on the US
desk. **Any stage tempted to rank by term velocity should read this line first.**
★ **`term premium` has 10 articles in 38,115 (0.026%)** while the curve executes the board's largest
structural move. `M659` measured "0 title hits in 49,722" on the client store; this is a **different
instrument** (FTS, body-inclusive) and so it is a **corroboration of the substance, not a repeat of the
number** — the desk's central macro object remains essentially unwritten-about.

### D-2 · The two threads that moved this week (direct body reads, dated, with outlets)

**(a) The rate path inverted — and the drivers are DEMAND data, not oil.**
- *"Producer Price Index: Flat, At Lowest Level In 4 Months"* [`seekingalpha` 08-13]; *"Dollar is
  Undercut by Dovish US PPI Report"* [`nasdaq` 08-13]; *"softer US PPI data reduces September Fed hike
  bets"* [`fxstreet` 08-13].
- *"**Fed rate hike odds sink further as retail sales, consumer sentiment fall**"* [`seekingalpha`
  08-14]; *"**Treasuries Rise as Weak Retail Sales Dampen Fed Rate-Hike Expectations**"* [`bloomberg`
  08-14]; *"U.S. Consumer Sentiment Slumps **Much More Than Expected** In August"* [`nasdaq` 08-14];
  *"Dow, S&P 500, Nasdaq slip after stocks hit record high, consumer sentiment declines"*
  [`yahoo_finance` 08-14].
- Counterweight, stated: *"Despite Lower Odds of a September Fed Rate Hike, One Sinister Inflation
  Metric Remains Problematic"* [`fool`·`yahoo_finance` 08-14] — the disinflation read is **not
  unanimous**, and core CPI MoM accelerating (§A) agrees with the dissent.
⚠ **`[news]`-tagged**: neither the retail-sales nor the sentiment primary was pulled (Census/UMich).
**No primary number is quoted for either**, only the direction and the reaction. This is the same
omission class as the 08-14 run's unpulled PPI primary, and it is named rather than hidden.

**(b) Hormuz escalated to a territorial claim, and the market took it to the CRACK.**
- *"**Trump vows to make Hormuz US territory 'pretty soon'**"* [`aljazeera` **08-15**]; *"Trump says
  he'll soon declare Strait of Hormuz to be US territory"* [`scmp` 08-14].
- *"**UAE accuses Iran of attacks on two ADNOC vessels** in Strait of Hormuz"* [`aljazeera` 08-14].
- *"Strait of Hormuz ship traffic **near three-month low** as U.S.–Iran deal in doubt"* [`cnbc` 08-12];
  *"'Hormuz remains blocked': Iran disputes Trump claims as traffic sinks to near 3-month lows"*
  [`cnbc` 08-13]; *"Iran's military rejects Trump's claims of US control … as 'lies'"* [`euronews` 08-13].
- *"**Hormuz Shock 'Manifesting Itself In Cracks, Not Crude,' Jefferies Says**"* [`zerohedge` 08-13].
- *"Gulf states scramble for Strait of Hormuz alternatives"* [`dw` 08-12]; *"Gulf Oil Giants Are
  Spending Billions to Build Ways Around Strait of Hormuz"* [`nyt` 08-12]; *"Panama Canal Fees Hit
  Record As El Niño, Hormuz Crisis Choke Global Shipping"* [`zerohedge` 08-13].
⇒ **This is the undated binary `CATALYST_WATCH.json` carries** (*"Iran 'Strait of Hormuz open'
statement (TACO trigger)"*, `🔀binary`, **undated**). **PREMORTEM must bracket it both ways.**

### D-3 · Blind-spot pass — the one thread nothing in the desk's term table would have found

★ **Navy shipbuilding was opened to foreign yards, and it lands on the desk's own INDU OW−.**
- *"**Trump orders Navy shipbuilding overhaul and new shipyard**"* [`investing_en` 08-14]
- *"**Hanwha, Fincantieri shares rise after Trump opens Navy shipbuilding to foreign yards**"*
  [`cna`/`reuters` **08-15**, i.e. today]
- *"Hanwha makes bid to acquire **Austal USA**"* [`upi` 08-11]
`shipbuilding` returns **30 articles / 3 days** — far too small to register on any velocity screen, and
**no term in this desk's bucket table would have surfaced it.** It is a **structural, policy-set change
to a defense sub-industry the desk is overweight**, and the desk holds `RTX`. ⚠ Direction is **not**
asserted here (P4): opening US Navy work to allied yards is plausibly negative for protected domestic
yard economics and positive for allied builders, and **the desk has measured neither.** Registered as
a dig (**`D269`**) and handed to DEEP-INDU, which already owns the unresolved `D249`.

### D-4 · What could NOT be read, with its denominator

- **`brief` (events) and `thread` (trajectories): STRUCTURALLY UNAVAILABLE** on this client (§0,
  `D268`). ⇒ **No proposition below carries a thread tag/curve.** Per the stage rule that absence is
  stated explicitly rather than left blank, and it is an architecture fact, not today's weather.
- **`theme_age`: runs, but not citable** — `D260` (its accel denominator tracks the corpus).
- **`drift_watch`: server-refused** (`D267`). DRIFT will have to substitute and say so.
- **46.8% of body-relevant articles are invisible** to a title+summary search on this desk's own term
  set (measured above). **No "quiet" claim in this report rests on term counts alone.**

---

## §E · Propositions — falsifiable, both directions, mandatory anti-signal

> ID 3-grep at write time: highest existing **P60** ⇒ this run takes **P61–P64**.

### P61 — ★★★ The Fed-hike premium detached from oil, and the driver is DEMAND
**Claim.** The oil↔hike coupling (`M69`, `M658`, proposition `P57`) **broke on 2026-08-14**: hike odds
fell while crude rose 5.4% in five sessions and the Hormuz axis escalated. The live driver of the front
end is **US demand data** (retail sales, consumer sentiment), not the barrel.
**Direction A (this is a regime change):** the front end keeps easing on demand prints. Observable —
`DGS2` at the **08-21** settle: **A ≤ 4.05%** (a further ≥10bp fall from 4.15).
**Direction B (the coupling reasserts):** oil-driven hike pricing returns. Observable —
`DGS2` **≥ 4.30%** at 08-21 **while** `CL=F` is above its 08-14 close of 82.40.
**Between = C, no information.**
**🚨 Mandatory anti-signal:** if a **September FOMC-dated** event or an inflation print lands inside
the window, the read is confounded and the row is **VOID** — the window must contain only demand data.
**⚠ Confidence:** `[news]`-anchored on both prints; **no Census/UMich primary was pulled.** The
`[FRED]` leg (`DGS2` 4.15) is one session old and does not yet contain 08-14.

### P62 — ★★ Energy's strength is DISTILLATE, and the 20-day window is where it is visible
**Claim.** The crack's advance is a middle-distillate event, not a crude event: over 20 sessions
`HO=F` **+5.37%** while `CL=F` is **−0.11%** and `RB=F` is **−6.15%**. Third-party corroboration:
Jefferies, *"cracks, not crude"* [`zerohedge` 08-13].
**Direction A (distillate-led, holds):** `HO=F` 20-day return stays **> `CL=F` 20-day + 4pp** at the
**08-21** settle.
**Direction B (it was a barrel move after all):** the gap closes to **≤ 0pp**.
**🚨 Mandatory anti-signal:** a **US refinery outage** or a **hurricane** landfall in PADD3 inside the
window makes distillate strength a domestic-supply artifact rather than a Hormuz read ⇒ **VOID**.
**⚠** The level is **86.7th percentile of 90 days** and **20 sessions ago it was HIGHER (69.41)** —
this is a rate claim, not a level claim (**lens B1**).

### P63 — ★★★ The index is being bought and its growth engine is being sold, at the widest spread yet
**Claim.** Speculative positioning is at an **88-point percentile spread inside equities** (S&P 88th
crowded long, **+38,538 added in one week**; Nasdaq-100 **0th**), the widest this desk has measured
(`M125` had 79 points). Directionally this is **rebound ammunition on tech and crowding risk on the
index**, and it dates to **08-11 — before both prints**.
**Direction A:** `RSPT − XLK` **and** `XLK − SPY` both positive at the **08-21** settle ⇒ the short
side covered into tech breadth.
**Direction B:** `SPY` outperforms `XLK` by **≥ 2pp** over the same window ⇒ the index crowding paid
and the tech short was right.
**Between = C.**
**🚨 Mandatory anti-signal:** COT is **Tuesday-close data with a 3–4 day lag**; if the next COT release
(08-21) shows the S&P add **reversing by more than half**, the premise was stale when written ⇒ the
row is scored on the **observable only** and the positioning rationale is struck.
**⚠ D6:** positioning is context, **never** a demand axis. No sector verdict in §G rests on this row.

### P64 — ★★ Two record-adjacent sessions ran on two-thirds of normal volume
**Claim.** The 08-13 record close and the 08-14 give-back both printed with median last-bar volume at
**0.732×** and **0.649×** the trailing 20-day average. A tape making highs on thinning participation is
a **fragility** observation, not a direction.
**Direction A (thin and fragile):** median `vol_surge` stays **< 0.85** through the **08-21** settle
**and** `SPY` fails to close above **777.88**.
**Direction B (participation returns):** median `vol_surge` **≥ 1.00** with `SPY` **> 777.88**.
**🚨 Mandatory anti-signal:** **08-21 is August monthly opex.** Expiry week mechanically inflates
volume ⇒ **the settle must use 08-20, not 08-21**, and this row states that at registration rather
than discovering it afterwards.
**⚠ C4:** two sessions is n=2. This is registered to be measured, not to be believed.

---

## §F · Self-backtest — scoring the 08-14 propositions on their own registered KPIs

| # | Registered claim | KPI | Measured today (settled 08-14) | Verdict |
|---|---|---|---|---|
| **P56** (08-14) | The long end is repricing **term premium**; `DGS2` pinned ⇒ UTIL/RE/STPL exposed | `XLU`/`XLRE` exc20 vs `SPY`; curve shape | `XLU` exc20 **−6.763 → −6.350** (improved) · `XLRE` **−4.366 → −4.777** (worse) ⇒ **split**. ★ **And the premise broke: `DGS2` 4.20 → 4.15**, a 5bp *front-end* move, with `2s10s` unchanged at +0.48 ⇒ **a parallel shift, not a long-end move.** `XLU` exc5 is **+1.207** | ⚠ **HALF — sign survives on 20 days, mechanism contested.** `P61` names the competing driver |
| **P57** (08-14) | The Fed-hike premium is an **OIL** function (2 independent measurements) | hike-odds direction vs crude | **Crude +5.40%/5d and Hormuz escalating, while hike odds SANK** on retail sales + sentiment [`bloomberg`·`seekingalpha` 08-14] | 🚨 **MISS — and it is the run's most useful miss.** The coupling **inverted**, not weakened. Superseded by **`P61`** |
| **P58** (08-14) | Energy's strength is the **CRACK**, and it survived the barrel | crack level/rate | Crack **65.84 → 66.72**, **+6.67 points / 5 sessions**, **95.2nd percentile of 250 days**; `XLE` exc5 **+3.774 → +7.271** | ★ **HIT, strengthened** — and refined by **`P62`**: it is specifically **distillate** |
| **P59** (08-14) | Materials is **one name**, and positioning is on the other side of it | ex-`NEM` EW exc5; copper %ile | ex-`NEM` EW exc5 **−2.097 with 1 of 11 positive** (only `APD` +1.424); `NEM` **+3.833**; **copper spec 100th %ile** while **`FCX` is the worst name at −4.894** | ★ **HIT, replicated on a second date** |
| **P60** (08-14) | The news instrument's availability window is **minutes**; single-probe revocation is a measured error | ≥3 probes ≥10 min apart | **5/5 fail 22:14 → identical command succeeds 23:1x** (3,729 hits). **Second consecutive run** | ★★ **HIT — and this run's own PREFLIGHT repeated the error** |
| **P52** (08-13) | The in-line print sent money to **growth**, not defensives | `XLK` exc5 ≤0 **while** `XLU` exc5 >0 ⇒ A refuted | `XLK` exc5 **+0.687** (positive) and `XLU` exc5 **+1.207** (positive) ⇒ the refuting conjunction **still cannot fire** | **CARRIED, running in A's favour.** Settles 08-19 |
| **P53** (08-13) | Materials' broad leg lasted two sessions | ex-`NEM` EW exc5 positive on any close ⇒ A wrong | **−2.097, 1 of 11 positive** | ★ **HIT (interim)**, anti-signal has not fired. `S77` settles 08-19 |

**Running hit-rate on propositions scored against a named KPI: 5 HIT · 1 HALF · 1 MISS** this run
(`P58` `P59` `P60` `P53` + `P51` carried from 08-14 · `P56` half · **`P57` miss**).
★ **The MISS is reported first in this document, not buried here.** A desk whose backtest never prints
a miss has a scoring problem, not a forecasting record — and `P57` had **two** prior independent
measurements behind it, which is exactly the kind of claim that gets over-trusted.

---

## §G · ★ SECTOR TRANSMISSION MATRIX — wind direction only, all 11 GICS

> This is ROTATION's input. It sets **wind**, not verdicts. Every relative number names `SPY`.
> **`flow_score` figures are 3-axis** (velocity axis revoked). **G3 flippers — IT · Industrials ·
> Materials — may NOT be moved on `wflow`.**

| # | Sector | Driving prop | Wind | The number, and the counter-number |
|---|---|---|---|---|
| **1** | **Energy** | **P62** · P61-B | ★ **OW-side, and it strengthened** | exc5 **+7.271 = best of 11** · exc20 +2.887 · crack **95.2nd %ile of 250d** with distillate the lead leg · **WTI spec 18th %ile short**. ⚠ **exc60 −4.796 still negative**, and coverage is **decelerating (`Hormuz` 0.68×)** while the price runs. *The tape is ahead of the narrative here, which is the opposite of the usual failure* |
| **2** | **Information Technology** | **P63** · P61-A | **OW-side wind, on BREADTH not on the megacaps** | **`RSPT` is the only ETF positive on all three windows (+2.030 / +6.979 / +9.800)** and beats `XLK` on each ⇒ the **median** tech name is leading. **NDX spec 0th %ile.** ⚠⚠ **G3: `wflow +0.023` is `NVDA` alone — ex-top1 −0.082**; breadth 0.09, 5🟢/6🔴 of 56. *The equal-weight leg is the admissible one; the cap-weight leg is one name* |
| **3** | **Financials** | P61-A | **neutral** | exc60 **+8.009 = best of 11** against exc20 −1.069 and exc5 +0.574. `wflow −0.031` with **`eqflow −0.126`** (breadth still worse than the megacaps, `R69`). ⚠ **A falling front end is not the steepener the 08-14 read assumed** — `2s10s` is **unchanged at +0.48**. *The 60-day says it happened; the 20-day says it stopped* |
| **4** | **Health Care** | — | **neutral** | exc60 **+7.803 (2nd best)** · exc20 −0.548 · exc5 +0.622. `wflow −0.115`, **breadth 0.00, 0🟢/3🔴 of 32**. ★ **`LLY` no longer flips the sign** (ex-top1 −0.031) ⇒ **`wflow` is admissible for HLTH again this run.** `S76` 08-19 · `S82` 08-20 |
| **5** | **Industrials** | **D269** · P61-A | **neutral** | exc20 −0.489 · exc60 +4.724 · exc5 +0.320. **breadth 0.00, 0🟢/10🔴 of 50.** ⚠⚠ **G3 flipper this run (`CAT`, only 8.7% weight) ⇒ `wflow −0.047` inadmissible.** ⚠ **`D249` unresolved for a 4th run** — the bracket measures `XLI`, the position is **defense**. ★ **NEW: the Navy shipbuilding order (§D-3) is a policy-set change inside that exact node, direction unmeasured** |
| **6** | **Materials** | **P59** | **UW-side wind** | ex-`NEM` EW exc5 **−2.097, 1 of 11 positive**; `NEM` +3.833; **copper spec 100th %ile long while `FCX` is the basket's worst at −4.894**. ⚠ **G3 flipper (`LIN` 24.7%)** ⇒ `wflow` inadmissible; `eqflow −0.114`, breadth 0.00. `S77` 08-19 |
| **7** | **Consumer Discretionary** | **P61-A** | **neutral, and the wind just changed under it** | exc5 **−1.783 = worst of 11** · exc20 −2.056. `wflow −0.378` (`AMZN` 40.2% of cap), breadth 0.04. ★ **The two prints that moved rates were CONSUMER prints** — weak retail sales and sentiment — *and this is the sector that owns that read.* **`XLY` was the worst 5-day performer on the board on exactly that news** |
| **8** | **Communication Services** | P56-A | **UW wind** | exc60 **−8.311 = worst of 11**, `wflow −0.436` = worst, breadth 0.08 — yet **exc5 +1.130** and Δ +0.092. ⚠ **`EA` has now dropped OUT of the scored set** (299/300) after 8 runs inside it, so this bucket's numbers changed composition, not just level (`R56`) |
| **9** | **Consumer Staples** | P56-A | **UW− wind** | exc20 **−3.390**, exc60 −5.807, `wflow −0.242`, breadth 0.00. ⚠ **`D249`: at 252 days STPL — not FIN — is the measured third duration leg**, so a STPL move is a `P56`/`P61` move wearing a defensive label |
| **10** | **Utilities** | **P56-A ⚠ contested** | **UW wind, weakening** | exc20 **−6.350 = worst of 11**, `wflow −0.445`, **0🟢/7🔴 of 15**. ⚠⚠ **But exc5 is +1.207, the 2nd best on the board, and it happened in the two sessions hike odds fell.** *If `P61-A` is right, this underweight's mechanism is being removed* |
| **11** | **Real Estate** | P56-A | **UW wind** | exc20 **−4.777, deteriorated from −4.366**; `wflow −0.280`, breadth 0.00, exc60 −2.780. **The only duration-complex leg that did NOT turn up on the 5-day window (+0.246 vs `XLU` +1.207)** ⇒ the cleanest remaining expression of `P56-A` |

★ **The matrix's single organising claim, and it changed this run.** The 08-14 matrix was organised by
`P56` (term premium) **×** `P57` (hike risk is an oil function). **`P57` is scored MISS.** The
replacement organising pair is **`P61` (the front end now trades on US demand data) × `P62` (Energy's
strength is distillate, not the barrel)** — and the two are now **independent**, where the old pair was
one story told twice. **The practical consequence is that the four duration underweights (UTIL, RE,
STPL, and the FIN steepener leg) no longer share a single driver with Energy**, so a Hormuz shock and a
rate shock are, for the first time in three weeks, **separable tests** — which is precisely what `S84`
was registered to measure.

---

## ✅ EXIT CHECK

- [x] **Catalysts injected** — `catalyst_calendar --days 10` run (beyond the default, because `S84`–`S87`
      settle 08-21). **1 binary in window: the UNDATED Hormuz statement** ⇒ **PREMORTEM must bracket it
      both ways.** `CATALYST_WATCH.json` saved to the day-folder root. EARNINGS and STRUCTURAL blocks
      both empty — STRUCTURAL because `data/catalysts/structural_schedule.json` is human-maintained and
      empty (`D253-KR` class, named not hidden).
- [x] **Indicators read** — `[FRED]` 14 series `--json` + `us_flow --cot`. Staleness flagged: H.15 ends
      **08-13**; monthly series lag one month; COT is **Tue 08-11** with a 3–4 day lag.
- [x] **Daily anchor read** — the previous run's `llm_outputs/2026-08-14/industry_US/MACRO_REPORT.md`
      (propositions `P51`–`P60`, transmission matrix) and `module_report_tags show`.
- [ ] 🚨 **Events via `brief --body 2`: NOT RUN — structurally impossible on this client.** `brief` and
      `thread` are parser-marked **client-only** and **server-refused**; the client owns no
      `news_alert.db`. **Stated, with the substitute named** (§D, `D268`). This box is left unticked
      deliberately rather than ticked on a substitute.
- [ ] **Trajectories via `thread --days 7`: NOT RUN**, same cause. **No proposition claims a thread tag
      or curve**; every dated claim carries an outlet and a date instead.
- [x] **`tail = 0` is not treated as the coverage claim** — the substitute's own blindness is
      **measured and quoted**: pool **38,115**, body-holding **68.4%**, desk-term recall **53.2%**,
      **46.8% body-blind**.
- [x] **Denominator is the corrected pool**, and the **pool ratio 1.782×** is printed beside every
      velocity (`D255`).
- [x] **Every "nothing happened" claim carries its denominator** — the sweep's top reading is **1.79×**
      against a 3× threshold, on a stated pool.
- [x] **No bucket's 0/near-0 is trusted from a mis-passed CLI** — every term was passed as a single
      quoted argv and its **d1 and d7 raw counts are printed**, so a zero is visible as a zero.
      `China export` d1 = 0 / d7 = 13 is shown rather than silently dropped.
- [x] **Both halves of every headline print** — July CPI (MoM +0.074% **on a −0.42% June base**, core
      MoM **accelerating** to +0.215%); the curve (`2s10s` +0.48 **unchanged** *and* a −5bp parallel
      shift); the crack (**rate +6.67 / 5d** *and* **level still below 20 sessions ago**).
- [x] **Every relative-performance number names `SPY` inline**; no cross-market statistical transfer
      (the KR IC ledger is **not** used to move any US axis — **W1**, HANDOVER §8).
- [x] **Credit axis read and cited** — HY OAS **2.71% flat**, IG 0.79% flat, `NFCI` −0.549 loosening.
      **No risk-off claim is made**; the Hormuz row is explicitly a *price* claim, not a credit claim.
- [x] **`real_10y` quoted with `breakeven_10y`** — 2.39 + 2.24 = 4.63, and the 08-14 breakeven print
      (2.27) is flagged as the only 08-14 rate observation available.
- [x] **Transmission matrix produced — all 11 sectors, one line each**, with the flipper constraint
      applied and the counter-number stated on every row.
- [x] **Self-backtest appended with a running hit-rate** (§F) — **including one MISS, promoted to the
      top of the document.**
- [x] **New blind-spot term folded back**: `shipbuilding` (30 articles / 3 days — below any velocity
      screen) added to the living term table via **`D269`**.
- [x] **Linter** — see §H below.

## §H · Linter

`python -X utf8 scripts/report_lint.py llm_outputs/2026-08-15/industry_US/MACRO_REPORT.md`
→ **✅ 0 findings** on rules **C1, C2, S6, D6**. Nothing exempted, nothing suppressed.

⚠ **Form-only, and this run has a live reason to say so.** The linter checks that a benchmark is
named, that both halves of a print appear, that no future label leaks, and that OBV is not cited
alone. It cannot see that **`P57` was scored MISS**, that **`brief`/`thread` never ran**, or that the
retail-sales and consumer-sentiment numbers behind `P61` are `[news]`-tagged with **no primary
pulled**. **A clean lint is not a correct report** — those three weaknesses are this report's, and
they are named in §D-4, §F and §P61 rather than left for the checker to miss.

---

# §5 · POST-RUN DRIFT ADDENDUM — appended 2026-08-15 by Stage 11 (L1·DRIFT) ★US-only

> **APPEND-ONLY.** Nothing above this line is edited. The original call stays visible next to its
> correction — that asymmetry is what the self-backtest eats.

## §5-0 · 🚨 The instrument, reported FIRST (PREFLIGHT G1 binds this stage explicitly)

**`drift_watch.py` DID NOT RUN.** Exit 2:
`'drift' 는 원격 실행 불가(조회 전용). 허용: ['blindspot','burst','chain-hop','coverage','export','fts','search','theme-age']`

★ **And this run identified the cause, closing a dig that has been logged as "remote-unrunnable" for
five runs (`D17`).** This repo's **client** allow-list — `module_news_data/__main__.py:51`,
`DB_READ_CMDS` — **does contain `drift`**. `CLAUDE.md` **P6** names that set as the single source and
states that `Server/news_api.py` **imports** it. ⇒ **The server is running an older checkout of that
set.** `D17` is not a design limit; it is **a stale server needing `git pull` + API restart**.
Registered as **`D267`**.

**Second instrument failure, same stage**: `module_news_data burst --days 1 --scope foreign` →
**`TimeoutError('The read operation timed out')`**. That reproduces **`D256`** (expensive queries
exceed the client read timeout while cheap ones succeed through the same tunnel) — and it happened in
the same minutes that `fts search` and `coverage` returned normally.

⇒ **Both of this stage's designed instruments were unavailable. This section is a SUBSTITUTE, and per
PREFLIGHT G1 an empty burst list today would NOT be "no drift".**

## §5-1 · The substitute, run against the LIVE server index with the pool ratio as a GATE (`D264`)

`D264` (registered 08-14) required two things after the 08-14 false all-clear: **publish the pool
ratio beside every burst verdict**, and **refuse an all-clear below a stated floor**, routing through
the live index when the client snapshot is thin. Both done:

| | Value |
|---|---|
| **Live-index foreign pool** | **d1 = 9,705 · d7 = 38,115** ⇒ 7-day daily average **5,445** |
| **POOL RATIO (d1 ÷ avg7)** | **1.782×** |
| **Thin-pool floor** | ✅ **PASSED with wide margin.** The 08-14 false all-clear ran on a client-store pool of **487 = 0.069× a normal day**; today's pool is **19.9× that**, and it is the **server's live index**, not the frozen client store (whose sync cursor is stuck at 2026-08-14T07:59 — PREFLIGHT G1c) |

⇒ **This all-clear is powered at the pool level.** Individual thin terms are flagged separately below.

## §5-2 · Kill-switch sweep — 16 terms, pool-normalised

| Term | d1 | d7 | raw | **pool-norm** |
|---|---|---|---|---|
| **`capex cut`** | **2** | **2** | 7.00× | 🚨 **3.93×** |
| `yields surge` | 2 | 5 | 2.80× | **1.57×** |
| `credit stress` | 3 | 10 | 2.10× | 1.18× |
| `Strait reopened` | 1 | 4 | 1.75× | 0.98× |
| `rate cut` | 35 | 144 | 1.70× | 0.95× |
| `ceasefire` | 46 | 205 | 1.57× | 0.88× |
| `guidance cut` | 7 | 34 | 1.44× | 0.81× |
| `recession` · `hurricane` · `refinery outage` · `circuit breaker` | — | — | — | 0.56–0.77× |
| `Iran deal` · `OPEC output` | — | — | — | 0.14–0.35× |
| **`Hormuz open`** | **0** | 7 | 0.00× | **0.00×** |
| `Russia ceasefire` · `oil plunge` | 0 | 0 | — | n/a |

**Only ONE term clears the 3× threshold, and it is body-read below rather than counted.**

## §5-3 · 🚨 `capex cut` at 3.93× — body-read, and it is NOT a fire, but it is NOT nothing either

**Both articles are the SAME syndicated commentary piece on two outlets:**
> *"Microsoft and Tesla Share a Common Concern, but Here's Why One Is Much More Justified"*
> [`yahoo_finance` **08-14**] · [`fool` **08-13**]

**Verdict: NO kill-switch fired.** It is **opinion, not an announcement** — no company cut capex, and
`n = 2` articles is precisely the underpowered case `D264` warned about (at a 1.78× pool a term
averaging ~0.3/day needs ~1 article to "burst").

★ **But it is recorded as a WATCH, not dismissed, for one specific reason.** The carried measurements
have `capex cut` at **0.00× for FOUR consecutive readings** (`M113` 07-24 · `M153` 07-25 · and twice
since). **This is its first non-zero print in five measurements, and the named company is Microsoft** —
the hyperscaler whose capex underpins this desk's **regime call** (memory RoC deceleration) and whose
Maia 300 programme is EVENT_ALPHA Card 6. **A first pulse on a five-run-dead kill switch is worth a
line even when the line says "commentary".**
**Watch condition**: `capex cut` ≥ **3.0× pool-normalised on n ≥ 8 articles** — the count leg is what
today's reading fails, and it is stated so the next run cannot re-fire on n=2.

## §5-4 · ★ What the substitute found that the report above did NOT contain

**`yields surge` 1.57× surfaced a dated, primary-adjacent corroboration of `P56` that MACRO §A missed:**
> *"**U.S. set to pay most for 30-year debt in a quarter of a century**"* [`fortune` **08-13**]

`P56` (08-14) claimed the long-end repricing is **term premium**, and `M653` built it from
`30y−10y +0.48 → +0.56 with DGS2 unchanged`. **This is an independent, dated observation of the same
thing at the auction level**, and it landed **inside this run's own window** while §A quoted only the
FRED series. ⇒ **`P56`'s mechanism gains a source it did not have.**
⚠ **And the same thread carries the other side**: *"The Market Now Says a Rate HIKE Is Coming"*
[`yahoo_finance` **08-11**] — the view that `P61` measured **inverting two days later** on soft PPI
and weak retail sales. **The thread contains both states of the week's regime flip, three days apart.**
That is corroboration of `P61`'s dating, not a contradiction of it.

**`credit stress` 1.18× — narrative-only, and the credit axis refuses it:**
> *"Still Seeing Credit Stress Under Surface: Cudzil"* [`bloomberg` **08-13**]

**HY OAS is 2.71%, flat, 8bp off its 365-day low** `[FRED]` 08-13; IG 0.79% flat; `NFCI` −0.549
loosening. ⇒ **Labelled narrative-only in the text, per the stage rule** — the same class as the
2026-07-21 "credit surprise stack" that was built entirely from prose while HY sat 6bp off its low.

**`Hormuz open` = 0 hits in the last day (7 over 7 days) — and this is the reading that matters most**,
because it is `S84` branch A's trigger term. ⚠ **A zero here is NOT an all-clear on its own**; it is
one term on a healthy pool. The corroborating reads are that `ceasefire` is **0.88× (decelerating)**
and `Iran deal` **0.35×**, while the escalation side printed a **territorial claim on 08-15**
(`aljazeera`). **Branch A's trigger is not forming today.**

## §5-5 · Verdict

**NO KILL-SWITCH FIRED. The report above does not lie overnight.**
No proposition (`P61`–`P64`), no verdict delta (ENRG OW− → OW), and no bracket (`S88`–`S91`) is
changed by this addendum.

**Three things are added rather than changed:**
1. **`P56` gains a dated auction-level source** it did not have (§5-4).
2. **`capex cut` is armed as a watch** with an explicit **n ≥ 8** count leg (§5-3).
3. **`D17` is re-diagnosed as a stale server checkout, not a design limit** (§5-0, `D267`).

⚠ **Stated plainly, as this stage is required to**: **both designed instruments failed** — `drift`
server-refused, `burst` timed out — and everything above is a hand-built substitute. **It is powered
at the pool level (1.782×, 19.9× the pool that produced the 08-14 false all-clear) and it is still a
substitute.**
