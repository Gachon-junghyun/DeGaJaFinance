# MACRO_REPORT — industry_US — 2026-08-03 (Mon) · run clock 09:1x ET, PRE-OPEN

## ★★ What this stage is obliged to say first

**There is no new settled US information on any axis this desk owns.** Not one. Stated as a table
rather than discovered three stages later:

| Axis | Latest value available | Same as the 08-02 run? |
|---|---|---|
| US equities (sector + name) | **2026-07-31 settled** | ✅ **reproduces to 0.01pp** (§B) |
| FRED rates / credit | **2026-07-30** (T10YIE reaches 07-31) | ✅ identical |
| CFTC COT positioning | **2026-07-28 Tue close** (released 07-31) | ✅ **byte-identical — same release** |
| Foreign news pool | **2026-08-02** (1,523 articles / 261 events) | ❌ **NEW — this is the run's only new axis** |
| Energy futures | 07-31 settled | ❌ **REVISED — and that is this run's largest finding (§D)** |

⇒ **This report's propositions may not claim a US price move.** What it can do — and what §D and §E
actually do — is (i) re-measure a settled bar and find it changed, (ii) read a genuinely new
weekend news pool, and (iii) score the prior run's propositions against both.

⚠ **The one thing a pre-open Monday clock buys**: D74 (unsettled-bar contamination) **cannot fire on
the equity axis**, because no 08-03 equity bar exists. It **did** fire on the commodity axis, where
Globex has been trading since 18:00 ET Sunday — handled explicitly in §D.

---

## §A · Indicators — primaries `[FRED]`

| Series | 07-27 | 07-28 | 07-29 | 07-30 | 07-31 |
|---|---|---|---|---|---|
| **DGS10** 10y | 4.65 | 4.61 | 4.67 | **4.68** | *(unpublished)* |
| **DGS2** 2y | 4.31 | 4.26 | 4.22 | **4.23** | *(unpublished)* |
| **DGS30** 30y | 5.12 | 5.09 | 5.20 | **5.21** | *(unpublished)* |
| **DFII10** real 10y | 2.44 | 2.41 | 2.41 | **2.41** | *(unpublished)* |
| **T10YIE** breakeven | — | 2.20 | 2.26 | 2.27 | **2.28** |
| **HY OAS** | 2.81 | 2.84 | 2.87 | **2.84** | *(unpublished)* |
| **IG OAS** | 0.81 | 0.81 | 0.81 | **0.80** | *(unpublished)* |
| **NFCI** (weekly) | — | — | — | **−0.554** (07-24) | — |
| **VIX** | 18.67 | 18.21 | 20.66 | **17.09** | *(unpublished)* |
| **DTWEXBGS** (the desk's `dxy`) | — | — | — | — | **120.7105 asof 07-24** |

**Derived** (`DGS10 − DGS2`, derivation stated — the catalog carries no `T10Y2Y`, **C5**):
2s10s **07-23 +0.34 · 07-24 +0.36 · 07-27 +0.34 · 07-28 +0.35 · 07-29 +0.45 · 07-30 +0.45**.
30y−10y: **07-27 +0.47 · 07-28 +0.48 · 07-29 +0.53 · 07-30 +0.53**.

⚠⚠ **M267's asymmetry reproduces a SECOND time and is now a pattern, not an incident.** FRED publishes
**T10YIE one business day ahead of DGS10 / DGS2 / DGS30 / DFII10** — on 07-30 the desk logged
*"published the 07-29 breakeven but not the 07-29 real yield, 2y or 10y"*; today, at 09:1x ET on a
Monday, **the breakeven carries 07-31 and every nominal and real yield stops at 07-30.**
⇒ **the real/breakeven decomposition is unsatisfiable on the newest print by construction, and no
proxy is substituted (D5).** Registered below as **D139**.

**Staleness stated rather than papered over**: `core_cpi` and `cpi` are **monthly, June prints**
(CPILFESL 336.065 · CPIAUCSL 332.568); `unemployment` is **June 4.2%** (from 4.3%). **July CPI prints
08-12 and July NFP 08-07 — both inside the calendar window, neither in hand.**

### Positioning `[CFTC COT]` — and it is the SAME release, established by value-diff

| Instrument | Net-spec | Wk Δ | 1y %ile | Read |
|---|---|---|---|---|
| **Nasdaq-100** | −9,914 | −222▼ | **5%** | crowded SHORT |
| S&P 500 | −17,196 | −412▼ | **82%** | crowded long |
| Russell 2000 | −1,379 | −8,137▼ | 57% | neutral |
| UST 10Y | −876,119 | +3,587▲ | 13% | crowded short |
| UST 2Y | −1,124,574 | +30,023▲ | 55% | neutral |
| USD Index | +17,197 | +1,583▲ | 72% | neutral |
| **WTI Crude** | +19,758 | −281▼ | **10%** | crowded short |
| **Nat Gas** | −190,799 | −19,661▼ | **3%** | crowded short |
| **Copper** | +67,281 | −6,696▼ | **96%** | crowded long |

⚠⚠ **Every one of these eleven numbers is byte-identical to M308** (the 08-02 run's read of the 07-31
release covering the 07-28 Tuesday close). ⇒ **This is the same release, not a new one.**
**D104 is unfixed — the tool still prints no `asof`** — so freshness had to be established by
value-diffing for the **second consecutive run**. The 08-02 run quantified D104's cost as *"one
scoreable bracket, missed by ~24 hours"*; this run adds that **the same defect now costs a
value-diff every run just to learn whether the axis moved at all.** Next release ~**08-07 Fri**
(08-04 Tue close).
⚠ **Not citable as a signal by any stage** (D6's REJECTED row: COT crowded-long/short contrarian;
S32's own registration repeats the prohibition).

---

## §B · The US equity axis reproduces exactly — and that is a control, not a filler

Settled 2026-07-31, **benchmark SPY, named inline**, n=72 aligned sessions:

| Sector | ETF | exc5d | **exc20d** | exc60d |
|---|---|---|---|---|
| **Energy** | XLE | −1.21 | **+11.59** | −3.05 |
| **Financials** | XLF | +0.02 | **+2.07** | **+7.16** |
| Real Estate | XLRE | −3.01 | +0.57 | −1.18 |
| Cons. Staples | XLP | −0.00 | −0.23 | −2.04 |
| Health Care | XLV | −1.11 | −1.03 | **+8.66** |
| **Cons. Disc.** | XLY | **+5.01** | −1.18 | −4.89 |
| Comm. Services | XLC | +0.73 | −1.54 | **−9.60** |
| Industrials | XLI | −2.64 | −2.52 | +1.10 |
| Info Tech | XLK | −1.40 | −3.20 | +2.65 |
| Materials | XLB | −2.72 | −3.34 | −5.35 |
| **Utilities** | XLU | **−5.29** | **−3.38** | **−7.57** |

*(SPY absolute: 5d +1.10% · 20d +0.30% · 60d +3.21%.)*

✅ **Every figure reproduces the 08-02 run to 0.01pp.** This is worth a line because §D shows the
**futures** axis did *not* reproduce on the same re-pull, from the same provider, on the same day.
**Equity closes are stable; energy-futures closes are revised.** That contrast is the run's method
finding and it is what makes §D's number credible rather than a pull error.

---

## §C · The news axis — one genuinely new pool, and the trajectory axis is UNREADABLE

**Denominator, corrected**: **2026-08-02 · 1,523 articles → 261 events → 261 market (0 non-market)**,
`--scope foreign`, `--body 2`. Head layer 32 events, body 229, tail 0.
⚠ **`tail = 0` is NOT a coverage claim** (the measured 07-23 case: tail 0 with 45.6% still unseen).
Recovery sections read: **`single_source` shown 10 / 10** at the default `min_nb` — and the honest
note the tool prints itself is that **all 10 are unscored, because the classifier is Korean-only**,
so on a `--scope foreign` run the single-source tier is a **random sample, not a ranked tier**.
`excluded_nonmarket` **0 / 0** (band nb > −3.0). `subevents` recovered: **21 `└` lines**.

⚠ **Today's own pool (08-03) is 10 articles** — the US session has not happened. Any "quiet"
claim about 08-03 would be a claim about the collection clock, not the market, and none is made.

### The three events that matter, with outlet counts

1. ★★★ **[36 articles / 20 outlets — the day's #1 by dispersion]** *"Trump holds off Iran strikes
   after Middle East allies outline…"*, with sub-events **[10/8]** *"Trump says he's cancelling
   strikes on Iran as 'perimeters…'"* and **[3/3]** *"Trump says new talks with Iran to begin on
   **Monday** after ca…"*
2. ★★★ **[28 articles / 9 outlets]** *"Japan to announce Tokyo and Washington took **joint action**
   on…"* → **[5/3]** *"Japan confirms **joint yen intervention with US**, signals rea…"* · **[4/3]**
   *"Japan to vow coordination with US on weak yen in historic…"* · **[3/3]** *"U.S. joins Japan in
   coordinated effort to support yen"* · **[2/2]** *"Yen Traders Brace for More Intervention…"*
3. ★★ **[9 articles / 5 outlets]** *"**OPEC+ Agree To Boost Oil Output.** It May Not Reflect In
   Marke…"* → **[3/2]** *"OPEC, Allies Increase Oil Output for **Sixth Time in a Row**"*

Also in the head, recorded and not built on: *"The Bond Market Just Called Fed Chair Kevin Warsh's
Bluff on…"* [6/6] · *"Big Tech's $2 trillion AI shakeout just changed everything"* [6/5] · *"AI isn't
a catch-all trade for stocks in this earnings season"* [7/6] · *"AstraZeneca said to have explored
Bristol Myers merger"* [5/5] · *"SpaceX vs. the 'Magnificent Seven': How the New Nasdaq-100 M…"*
[7/5] — ⚠ **the last one describes an index reconstitution and `catalyst_calendar`'s STRUCTURAL block
reads "(none in window)"**, i.e. **D13's structural schedule is unpopulated while an index event is
in the head layer.** Logged, not scored.

### ⚠⚠ Trajectories (`thread --days 7`) — read, and found UNREADABLE, with the reason

Per-day denominators, read **first** as the stage requires:
**07-28 846 · 07-29 846 · 07-30 840 · 07-31 774 · 08-01 275 · 08-02 261 · 08-03 0.**

The tool reports **463 multi-day threads and ZERO alive** — i.e. *every* thread tagged ENDED.
**That is an artifact of the window terminating on a pre-open Monday with a zero denominator**, and
the stage's own warning names this case exactly (*"윈도우 끝이 휴일/저물량이면 FADING 이 과대해진다"*).
⇒ **No proposition in this report cites an ENDED tag**, and no staleness flag is raised from one.

**What IS readable is the curve shape inside the window**, and one curve is unambiguous:

| Thread | Outlet curve 07-28 → 08-02 | Peak | Read |
|---|---|---|---|
| **Trump holds off Iran strikes** | **2 → 4 → 20** | 20 | ★ **the only thread accelerating INTO the window edge** |
| US launches new wave of strikes against Iran | 15→20→24→11→7→7 | 24 | peaked 07-30, decayed |
| Oil prices fall to one-week low on US-Iran hopes | 19→18→18→14→7→5 | 19 | decaying ⚠ partly denominator |
| The Fed holds rates steady, Dow drops | 9→28→17→15→6→6 | 28 | spent |
| Apple earnings top expectations, but the stock… | 15→9→18→15→7→4 | 18 | spent |

### Term sweep — raw counts, and the denominator is stated as MISSING

`fts search <term> --scope foreign --days 2 --count`, **every term passed as separate argv** (a quoted
multi-word bucket returns ~0 silently — R25):

`Hormuz 313` · `tariff 347` · `memory 468` · `capex 246` · `yen intervention 188` · `credit spread 108`
· `refinery 91` · `recession 83` · `OPEC 69` · `layoffs 60`.

⚠⚠ **These are RAW counts and are NOT pool-normalized.** The vowel-token pool probe returned 20, i.e.
it is not a valid normalizer on this index. **Rather than invent a denominator, the counts are
reported as raw and no "elevated / flat / quiet" verdict is drawn from them** (P4). The one
normalized instrument that *is* available is `theme_age`, below.

### `theme_age` — and the fastest accelerator on the board is a CURRENCY event

| Theme | Verdict | Age | 7d mean | **Accel** | n |
|---|---|---|---|---|---|
| **yen intervention** | 🟡ACCELERATING | ≥90d | 9.3 | **11.14×** | **121** |
| memory pricing | 🟡ACCELERATING | 82d | 28.4 | 4.22× | 524 |
| refining margin | 🟡ACCELERATING | **66d** | 7.7 | 3.40× | 127 |
| AI capex | 🟡ACCELERATING | 74d | 25.1 | 2.29× | 736 |
| OPEC | 🟡ACCELERATING | ≥90d | 22.4 | 2.05× | 807 |
| Hormuz | ⚪ECHO | ≥90d | 137.1 | 1.60× | 6,266 |
| data center power | ⚪ECHO | 72d | 8.3 | 1.29× | 384 |
| short squeeze | ⚪ECHO | 67d | 0.9 | 0.63× | **71 — thin, unusable** |

★★★ **`yen intervention` went 5.31× (07-31, M320) → 11.14× (today) = +110% in two runs**, and it is
**backed by a 9-outlet head event naming a confirmed joint US–Japan action** — i.e. the ratio and the
event axis agree, which is not usually the case (M244/M186: the term axis has been blind to the day's
#1 event on three consecutive US runs; **today it is not**).
⚠ **n = 121 is the second-thinnest on the board.** The ratio is real; it is measured on a small base.
★ **Hormuz at 1.60× on n=6,266 is the mirror image** — the largest pool, decelerating, consistent
with the de-escalation head event rather than with a supply shock.

⚠ **ZERO 🟢FRESH for a 10th consecutive foreign-feed measurement.** **F1 restated as arithmetic, not
as a complaint**: 🟢FRESH needs **age ≤14d ∧ accel ≥2×**, and **the youngest theme on the board is
66 days** (`refining margin`). **🟢LIVE cannot fire by construction**, and the gate was **not**
loosened (a live-gate change needs a human, D11-class).

---

## §D · ★★★ The run's largest finding: a SETTLED bar was revised, and it moved a live bracket's own tracking number by 3.37 points

The 08-02 run's **M309** recorded, from settled yfinance daily bars:
> *3-2-1 crack 71.860 (07-29) → 67.313 → **59.865** = −16.7% in two sessions … RB 3.398 → **3.114***

**Re-pulled today, same provider, same "settled" bars, two days later:**

| Date | RB=F close | HO=F close | CL=F close | **3-2-1 crack** | **distillate crack** |
|---|---|---|---|---|---|
| 07-27 | 3.327 | 4.112 | 82.61 | 68.117 | 90.077 |
| 07-28 | 3.335 | 4.151 | 79.26 | 72.219 | 95.078 |
| 07-29 | 3.398 | 4.370 | 84.46 | 71.860 | 99.084 |
| 07-30 | 3.285 | 4.209 | 83.59 | 67.313 | 93.205 |
| **07-31** | **3.2216** *(was 3.114)* | **4.1215** *(was ~4.096)* | 84.67 | **63.236** *(was 59.865)* | **88.433** *(was 87.341)* |

⇒ **The 07-31 3-2-1 crack was revised +3.371 points and the distillate crack +1.092 points, on a bar
that was already two calendar days old when the prior run read it.**

**Why this is not a pull error, and the control that proves it**: **§B's eleven equity ETFs
reproduced to 0.01pp on the same day, from the same provider.** The instability is specific to the
CME product legs. **And the mechanism is visible**: RB volume is **13,997 on BOTH 07-30 and 07-31**,
HO **12,325 on both**, CL **235,395 on both** — **byte-identical forward-filled volume, D86 / M202 /
M236 reproducing a FOURTH time**, exactly as S49's own registration warned.

### What it does to S49, scored honestly in both directions

S49's frozen observable is the **5-session change in the settled distillate crack (HO×42 − WTI),
yfinance DAILY settled bars only**. Registration state **+9.007**. Branches: **A > 0** · **B ≤ −5.0**
· **C** between.

| Reading | 5-session change at 07-31 | Buffer to branch B (−5.0) |
|---|---|---|
| **08-02 run (M309/P4)** | **+1.066** | 6.07 points — *"the anti-signal is ~1 session away"* |
| **Today, revised** | **+2.158** | **7.16 points** |

⇒ **S49 stays ARMED in branch A, with MORE margin than the prior run believed.** The revision moved
the observable **away** from the bracket's own falsifier.

★★★ **And this is a finding about S49's construction, not a lucky escape.** S49 was written
*specifically* to survive R30/D95 — the reasoning was *"a level cannot be the observable on this
data; a CHANGE can, because a constant granularity offset cancels in a difference computed on one bar
type."* **That reasoning is correct about granularity and silent about revision.** A change is a
difference of two levels; **if one endpoint is revised by 1.09 points, the change moves by 1.09
points**, and nothing cancels. **The bracket is more robust than S8 and it is not robust.** Its own
registration already said so (*"a better observable than S8's, not a clean one — C4"*); this run
supplies the number that was missing.
⇒ Registered below as **D140**. **S49 is NOT re-frozen** (thresholds are frozen at registration);
the fact is recorded so its 08-06 scoring carries it.

### The live 08-03 bar — recorded for DIRECTION ONLY, and not scoreable

Globex has traded since 18:00 ET Sunday, so an 08-03 bar exists at this pre-open clock:
**CL 78.85 (−6.9% vs 07-31) · RB 3.004 · HO 3.967 · 3-2-1 60.808 · distillate 87.756.**
The 5-session changes on that bar would read **3-2-1 −7.308** and **distillate −2.322**.

⚠⚠ **NOT USED.** CL volume is **111,520 against a 235k–368k full session ⇒ ~30–47% of a bar**, and
S49 says *"settled bars ONLY, never mixed with intraday."* **Scoring branch B off this would be the
M201/D83 error the desk has already made twice** (a 07-28 electronic tick labelled 07-27).
★ Recorded because the **direction is corroborated by named causes in §C**: OPEC+ raising output a
sixth consecutive time, and strikes on Iran cancelled with talks starting today. **Crude down on
supply-up plus de-escalation is a coherent two-source read, and the desk will know tonight.**

---

## §E · Propositions

> Each carries direction **both ways**, a **mandatory anti-signal**, a tracked KPI, and a dated
> catalyst. Anchors `[FRED]` > `[news]`. `[inferred]` claims are tagged and are not evidence.

**P1 — The long-end configuration is unchanged and is ~100% inflation compensation. `[FRED]`**
DFII10 **2.41 for a fourth consecutive print**; T10YIE **2.20 → 2.28 (+8bp)**; DGS30 **+12bp to
5.21** with 30y−10y **0.48 → 0.53**. *Against*: DGS2 **fell 3bp to 4.23** — the front end is not
confirming an inflation scare. **KPI**: DFII10 with T10YIE, never alone. **Anti-signal**: DFII10
≥ **2.55** (S9's kill line, **14bp away and flat four prints**) ⇒ the move re-becomes real and the
duration read flips. **Catalyst**: the 07-31 nominal prints, still unpublished (**D139**); CPI 08-12.

**P13 — The bear STEEPENER is holding; S23's flattener is receding. `[FRED, derived — C5]`**
2s10s **+0.45 on two consecutive settled prints**, against S23's **≤ +0.20** line ⇒ **25bp away.**
*Against*: only two prints, and **07-31 is unpublished**, so this is `n=2 dates` (**S1**).
**Anti-signal**: 2s10s ≤ +0.20 ⇒ the FIN OW−'s stated mechanism dies. **Catalyst**: **NFP 08-07
(S51)** · **S23's window closes 08-05, i.e. before NFP** — the date arithmetic S49's drop-log
already flagged.

**P2 — Credit is elevated, not deteriorating, and conditions are still loosening. `[FRED]`**
HY OAS **2.81 → 2.84 → 2.87 → 2.84** (a spike and a retrace, **not monotone widening**); IG
**0.81 → 0.80**; NFCI **−0.554, loosening a 6th week**. Buffers: **S26 needs HY ≥ 3.10 ⇒ 26bp**;
**S41 needs IG ≥ 0.90 ⇒ 10bp (was 9bp — it widened by tightening)**. *Against*: `credit spread`
returned **108 raw hits** with **no usable denominator**, so the narrative axis cannot corroborate
either way. **Anti-signal**: HY ≥ 3.10 on a close. **Catalyst**: the 07-31 print (unpublished).

**P4 — ★★ RESTATED ON REVISED DATA: the distillate bottleneck did NOT break, and the prior run's
magnitude was 28% too large. `[own calc, yfinance DAILY settled, one source]`**
See §D. The two-session 3-2-1 fall is **−12.0%**, not −16.7%; S49's observable reads **+2.158**, not
+1.066. **Direction of the prior read (gasoline-led weakness) SURVIVES** — RB fell 3.398 → 3.222
(−5.2%) while CL *rose* 84.46 → 84.67. **Magnitude is withdrawn.** *Against*: the live 08-03 bar is
sharply lower on both legs with two named supply/de-escalation causes. **Anti-signal**: S49 branch B
(5-session distillate change ≤ −5.0) on a **settled** bar. **Catalyst**: **MPC 08-04 · PSX 08-05
(S53)** · **S49 window 08-06**.

**P7 — ★★★ UPGRADED: the yen channel fired a CONFIRMED JOINT US–JAPAN action, and it is now the
fastest-accelerating theme on the board — while the desk's own dollar series is blind. `[news, 9
outlets, bodies not yet read] + [own measurement]`**
Event: **[28 articles / 9 outlets]** joint US–Japan action, with **four independent sub-events**
including *"Japan confirms joint yen intervention with US"* and *"U.S. joins Japan in coordinated
effort to support yen."* Instrument: **`theme_age` 11.14× on n=121, up from 5.31× on 07-31.**
⚠⚠ **The desk cannot see the dollar**: **`DTWEXBGS` has not printed since 2026-07-24 — 10 calendar
days**, which is the *same series* S44 leg 2 needs and the same one S12's only remaining scoreable
axis needs. **Three separate obligations are blocked on one unpublished series.**
*Against*: **n=121 is thin**; the 08-03 single-source tier carries *"Yen Weakens Slightly on Likely
Technical Correction"* [wsj], i.e. the intervention did not hold the pair on day one; and
**D22 is still open — "BOJ tightening leads US long-end yields" has NO lag table**, so this remains
**`[unverified]` as a transmission claim and event-grade only (W2).** It may not be cited as
evidence for a duration conclusion.
**KPI**: DTWEXBGS's next print vs **120.7105**. **Anti-signal**: DTWEXBGS printing **≥ +1.0%** ⇒ the
intervention failed and the dollar-strength channel dominates. **Catalyst**: next FRED print ~08-04.

**P18 — ★ NEW · The Iran axis inverted from escalation to negotiation, and the desk's own bracket
says do NOT score it. `[news, 20 outlets]`**
The day's #1 event by dispersion is **strikes cancelled**, with **talks beginning Monday 08-03**, and
the thread is **the only one accelerating into the window edge (2 → 4 → 20)**. `Hormuz` reads
**⚪ECHO 1.60× on n=6,266** — the narrative is decelerating, not spiking.
⚠⚠ **S52 tracks branch C ("neither by 08-06"), and this is a deliberate refusal, not an oversight.**
Branch A needs *"a **dated** Strait-reopening term in a **primary text** … NOT a headline paraphrase,
NOT a repeat of the 08-02 conditional wording."* **A date for TALKS is not a dated reopening**, and
*"talks begin Monday"* is an extension of the exact conditional S52 was registered on. Branch B needs
a strike on **named** Iranian energy infrastructure with ≥2 outlets on the same primary — **absent**.
★ **The 07-27 run refused to score S8 branch A off a precondition, and S52's registration says that
refusal binds here. It binds.**
*Against the de-escalation read*: the same window carries *"Iran war live: Tehran warns of 'decisive'
response to any US…"* [12/7] and the US strike thread peaked at 24 outlets on 07-30 — **both
branches are live**. **Anti-signal**: a primary text with a date ⇒ S52-A ⇒ **OXY · COP · CVX · XOM
lose the leg S31 says they stand on**. **Catalyst**: talks 08-03 · **S52 window 08-06**.

**P19 — ★ NEW · OPEC+ raised output a SIXTH consecutive time, which is a supply leg the desk's Energy
OW has never bracketed. `[news, 5 outlets + 2]`**
*"OPEC, Allies Increase Oil Output for **Sixth Time in a Row**"*, with the head item itself hedging
*"It May Not Reflect In Market…"*. `OPEC` theme **2.05× on n=807** — a large, corroborated base.
⚠ **Every registered Energy bracket (S8 · S31 · S49 · S52 · S53) is written on cracks, war premium or
issuer execution. NONE is written on OPEC supply.** With **WTI COT at the 10th percentile
(crowded short)**, a supply increase into an already-short market is a configuration the book has no
observable for. *Against*: crude *rose* through the previous five increases; the sixth may be equally
inert, which is what the headline itself says. **KPI**: settled WTI vs the crack, not WTI alone —
**a supply-led crude fall is crack-POSITIVE, a demand-led one is crack-negative, and the 08-03 live
bar shows crude −6.9% with the crack ALSO down**, i.e. it currently looks demand/margin-led rather
than supply-led. **Anti-signal**: settled distillate crack change ≤ −5.0 ⇒ S49-B and this proposition
resolve together. **Catalyst**: the 08-03 settled close, tonight.

**P8 — Housing/consumer rate transmission remains unmeasurable in this repo. MISS by construction,
NINTH consecutive run.** `MORTGAGE30US` is not in the catalog (D99). Stated so the gap does not read
as a quiet channel.

---

## §F · ★ Self-backtest — the prior run's propositions scored

| ID | KPI | Verdict today |
|---|---|---|
| **P1** | DFII10 · T10YIE · 2s10s | ★ **HIT, held.** Real 10y flat a **4th** print, breakeven +8bp, 30y−10y +0.53. Nothing moved because nothing published. |
| **P13** | 2s10s ≤ +0.20 | ★ **HIT, held.** +0.45 on both available prints; falsifier 25bp away. |
| **P2** | HY OAS · NFCI | ★ **HIT, held.** 2.84 retrace confirmed; NFCI loosening. **IG buffer widened 9 → 10bp.** |
| **P11** | IG OAS ≥ 0.90 | **HELD.** IG tightened to 0.80. No new AI-issuer pricing event in the 08-02 pool. |
| **P4** | settled distillate crack direction | ⚠⚠ **RE-SCORED AGAINST THE PRIOR RUN — see §D.** Direction **HIT**; the *"anti-signal ~1 session away"* claim is **WITHDRAWN** (7.16 points of buffer, not 6.07). **The prior run's HALF was scored on a bar that has since been revised by 3.37 crack points.** ★ **This is a D48-class correction across runs rather than inside one — the first time this desk has caught a prior run's scoring changed by a data revision rather than by a later stage.** |
| **P7** | a second intervention print | ★★★ **HIT, and upgraded again.** Not a print but a **confirmed joint US–Japan action across 9 outlets and 4 sub-events**, with theme acceleration **doubling 5.31× → 11.14×.** ⚠ **Still no lag table (D22) ⇒ event-grade only.** |
| **P10** | median RS20 of {STX, MU, WDC} | **UNCHANGED — no new settled bar.** S30 window 08-05. |
| **P15** | OEM gross-margin read-through | **HELD, not advanced.** No new OEM print in the 08-02 pool. |
| **P3** | supplier−spender spread | **UNCHANGED — no new settled bar.** |
| **P16** | breadth, two windows | **UNCHANGED.** XLY still **+5.01 exc5d / −1.18 exc20d** — the two windows still disagree, on a bar that has not moved. |
| **P17** | AI-security registry gap | **HELD.** **D20 unfixed** — no registry row exists, so a 0% book exposure still cannot raise a GAP. |
| **P6** | tariff implementation date | **`[blank]` unchanged** for a 3rd run. |
| **P5** | S25's observable | **UNCHANGED.** Already scored zero-information (D122). |
| **P8** | `MORTGAGE30US` | ★ **MISS by construction, NINTH run.** |

**Running hit-rate, this run: 6 HIT · 1 HIT-with-a-withdrawn-magnitude (P4) · 5 unchanged-by-construction
· 1 blank · 1 structural MISS.**
⚠⚠ **The honest reading of that line is that it is mostly not a score.** **Five propositions are
"unchanged" because their KPI is a US settled price and no US settled price moved** — scoring them as
HIT would be counting a stationary instrument as a correct forecast. **They are recorded as
unchanged, not as hits**, and the hit-rate is stated with that split visible rather than collapsed
into a percentage.

---

## §G · ★ Sector transmission matrix — the deliverable

> ROTATION's input. **Wind direction only.** ⚠⚠ **Binding constraint from §0: no tilt may CHANGE on
> price this run, because no US settled price moved.** A Δ column entry of "hold" below therefore
> means *"the evidence did not move"*, not *"the evidence was re-confirmed."*

| # | GICS Sector | Tilt | Δ vs prior | Driving prop. | Evidence (settled 07-31, vs SPY) |
|---|---|---|---|---|---|
| 1 | **Energy** | **OW−** | hold | **P4 · P19 · S49 · S52 · S31** | **XLE +11.59pp exc20d, the board's best by 9.4pp; −1.21pp exc5d.** ★ **§D REVISION: the crack break was 28% smaller than the prior run recorded and S49 sits 7.16 points from its falsifier, not 6.07** ⇒ the OW−'s commodity leg is **stronger** than yesterday's file says. ⚠⚠ **But two NEW supply legs arrived that no bracket owns**: OPEC+ 6th consecutive increase (P19) and Iran talks starting today (P18). ⚠ **R39 binds: XOM is NOT 0% refining, so the Energy cycle-GAP figure is `unknown` (C3).** **MPC 08-04 · PSX 08-05 · S31/S49/S52 all settle 08-05/08-06** |
| 2 | **Financials** | **OW−** | hold | **P13 · P2 · S23 · S51** | **XLF is the only sector positive on all three windows (+0.02 / +2.07 / +7.16pp).** Mechanism = the bear steepener (2s10s +0.45, two prints); S23 25bp away and receding; credit did not break. ⚠ **R32 stands — "breadth-led" is dead as a reason** and M316 measured 74% of the surviving statistic to be one row (BRK-B). ⚠ **W3: the NIM leg migrated to markets/financing (M138).** ⚠ **M317: the OW's stated carrier has changed in three consecutive runs — an instability, not a discovery.** **NFP 08-07** |
| 3 | **Info Tech** | **N (split, asymmetric)** | hold | **P3 · P10 · P15** | **XLK −3.20pp exc20d / −1.40pp exc5d.** S30 FIRED-A on 08-02 but **DEEP-IT measured the median decaying on its first re-test (+1.7 → +0.8)**, 0.8pp from its own anti-signal. ⚠ **C8 stands: one label over three legs wanting opposite verdicts (W5).** **AMD 08-04 · S30 window 08-05** |
| 4 | **Health Care** | **N−** | hold | — | **exc60d +8.66pp is the board's 2nd best, on exc20d −1.03.** ⚠ **C7 unresolved and its resolving observable is still undefined by a human (M278: the same test returns 1 or 2 depending on an undocumented cap-block choice, C5).** ★ New, unbuilt-on: **AstraZeneca/Bristol Myers merger exploration [5 outlets]** — a sector M&A leg no desk file carries. **C7 re-check 08-06** |
| 5 | **Cons. Discretionary** | **N+** | hold | P16 | **+5.01pp exc5d, the board's biggest 5-day, against −1.18pp exc20d.** ⚠ **n≈1 event (AMZN's print), declared.** The two windows still disagree and neither moved |
| 6 | **Comm. Services** | **N** | hold | S16 · P11 | **exc60d −9.60pp = the board's worst 60-day**, exc20d −1.54. P11's AI-funding channel runs through this sector's largest spender |
| 7 | **Industrials** | **N** | hold | **P18 · S42 · S50** | **XLI −2.64 / −2.52 / +1.10pp.** ⚠⚠ **R38 binds: the "8 of UNP's 12 growth points are fuel surcharge" magnitude is DEAD** — the 10-K shows surcharge revenue **fell $218M**. The mechanism (≈2-month lag) survives; **the read-across that made S49-B and S52-B "hit two tilts at once" is re-anchored, not re-scored.** ⚠ **S42's branch-B second leg is FAILING (needs ≥2 of 4 still 🟢, has 1). ANET 08-04. S42 → 08-12** |
| 8 | **Real Estate** | **OW−** | hold | S25 · S41 | **+0.57pp exc20d / −3.01pp exc5d.** ⚠ **S25 already scored ZERO-INFORMATION (D122)** — its threshold was true on its own registration bar. **The binding variable is CREDIT: IG 0.80 vs S41's 0.90 = 10bp.** **S25 08-08 · S41 08-12** |
| 9 | **Cons. Staples** | **N** | hold | — | **−0.23 / −0.00 / −2.04pp — the flattest sector on the board.** ADM sits on the missed ledger (`U.발굴부재`, recheck 08-16) precisely because no proposition claims this sector |
| 10 | **Materials** | **UW−** | hold | S36 | **−3.34pp exc20d.** ⚠⚠ **S36's CONFIRMING leg is disqualified (M273/M238): the "green count still 0" is a `vol_surge` artifact — 5 of 12 pass the accumulation pre-condition and all 5 are blocked by the gate alone.** ⇒ **the bracket can only FALSIFY the UW, never confirm it.** ⚠ **Copper COT 96th percentile = crowded long** is context, not a signal (D6). **S36 → 08-05** |
| 11 | **Utilities** | **UW−** | hold | S24 · S35-ANNEX | **XLU is the board's worst on ALL THREE windows (−5.29 / −3.38 / −7.57pp)** — the cleanest single-sector read on the board. ⚠⚠ **R40 binds absolutely: S35's FIRED-A and S47's FIRED-B may NOT be cited as evidence about Utilities** (D is a merger-arb security). ⚠ **M313: the instrument both brackets are written on has σ 2.08pp and crosses zero 10 times in 40 sessions — noise at its own threshold.** ★ **The UW− survives on XLU itself, which needs neither basket.** **CEG 08-06 · VST 08-07 · S24 → 08-12** |

---

## §H · New digs registered by this stage

> ⚠ IDs checked at **WRITE time** against BOTH files (M319's measured requirement). Highest existing:
> **D137** (08-03 `industry_kr`); **D138** was taken by this run's own HANDOVER.

| # | Dig | Why it matters | Owner |
|---|---|---|---|
| **D139** | **FRED publishes `T10YIE` one business day ahead of `DGS10`/`DGS2`/`DGS30`/`DFII10`, systematically.** Observed 07-30 (M267) and again 08-03 — **two independent occurrences, opposite ends of a week.** | The desk's headline decomposition (*"how much of the long-end move is real vs breakeven"*) is **unsatisfiable on the newest print by construction, every run.** Not a lag to complain about — a **known offset to build the read around**: quote the decomposition on the newest *common* date and say so, rather than pairing a fresh breakeven with a stale real yield. | MACRO / L2 indicators |
| **D140** ★★★ | **A CHANGE observable does not survive REVISION, only granularity.** S49 was built on R30/D95's finding that *levels* differ 5.80 points across bar type, reasoning that a constant offset cancels in a difference. **It does — and revision does not cancel.** Measured: the settled 07-31 distillate crack moved **+1.092** and the 3-2-1 **+3.371** between two pulls two days apart, shifting S49's own tracking number from **−4.439 to −1.068** (3-2-1) and **+1.066 to +2.158** (distillate). | **The desk now has two brackets (S8, S49) defeated by two different properties of the same series.** The general remedy is not a third threshold — it is **stamping every futures-derived observable with its pull date and re-pulling the whole window at scoring, never trusting a carried value.** Cheap, mechanical, and it would have caught this. ⚠ **S49 is NOT re-frozen.** | PREMORTEM (registration) · MACRO (scoring) |
| **D141** | **`catalyst_calendar`'s STRUCTURAL block reads "(none in window)" while an index reconstitution sits in the news head layer** (*"SpaceX vs. the 'Magnificent Seven': How the New Nasdaq-100 M…"*, 7 articles / 5 outlets). | **D13 was closed 2026-07-22** by adding the STRUCTURAL block — but the block reads `data/catalysts/structural_schedule.json`, which **a human must populate and nobody has.** A closed dig with an empty data file is an open dig wearing a checkmark. ⚠ Needs a human (data edit). | `data/catalysts` / human |

---

## §I · Hand-forward to SWEEP

1. **Expect `SECTOR_FLOW_US.json` to reproduce 08-02.** A non-reproduction is **D126** (the
   oscillating `velocity` join), testable this run as a **controlled experiment** — same input data,
   same day, second pull.
2. **Do not trim the price cache for D74 on the equity axis** — there is no 08-03 equity bar to trim.
   **Do** confirm `asof` reads **2026-07-31**.
3. **The 🟢 count is a volume test wearing a flow label** (M144/M237/M272/M314, 7 replications, two
   markets). **D6 binds: it may corroborate, never carry.**
4. **R41 binds this desk now**: no superlative ("the largest / the maximum on the board") about any
   short balance, flow score or spread without having scanned the distribution.

## §J · Post-run DRIFT hook

**S49 is the bracket most likely to move tonight** — the live 08-03 bar reads **−2.322** on its
observable against a **−5.0** line, with two named supply/de-escalation causes. **DRIFT re-pulls the
settled 08-03 close and appends an ADDENDUM to this section, append-only.**

---

# ★ ADDENDUM — DRIFT (post-run, append-only · appended 2026-08-03 09:5x ET)

> ⚠ **Nothing above this line was modified.** The original call stays visible next to its correction —
> that asymmetry is the self-backtest's food.

## A-1 · Instrument failure, logged and substituted

**`drift_watch.py` failed twice** (retried once per the unattended-run rule):
`'drift' 는 원격 실행 불가(조회 전용)` — **D17, unchanged and now ~13 runs old.** The stage that exists
to stop the report lying overnight **remains unrunnable from this client.**
**Substitute applied** (the documented one): `fts search <term> --scope foreign` over the kill-term
set, **normalized by each term's own d1 ÷ (d7/7) baseline** — the method the 07-22 run validated.

| Term | d1 | d7 | **d1 ÷ (d7/7)** |
|---|---|---|---|
| **OPEC** | 57 | 170 | **2.35×** ← elevated |
| **intervention** | 191 | 671 | **1.99×** ← elevated |
| Hormuz | 212 | 1,132 | 1.31× |
| credit stress | 21 | 114 | 1.29× |
| recession | 58 | 324 | 1.25× |
| ceasefire | 51 | 327 | 1.09× |
| guidance cut | 124 | 838 | 1.04× |
| escalation | 151 | 1,068 | 0.99× |

**No kill-switch fired.** ★ **And the two elevated terms are exactly the two this run built cards on
(EVENT_ALPHA Cards 2 and 3)** — a confirmation that the term axis and the event axis agreed today,
which M186/M244 recorded as *failing* on three consecutive prior US runs. **`escalation` at 0.99× and
`ceasefire` at 1.09× are both flat**, i.e. the Iran axis is being narrated as *negotiation*, not as
either escalation or truce — consistent with **S52 tracking branch C**.

## A-2 · ⚠⚠ The one number that moved, and it moved AGAINST this report

**S49's observable deteriorated 1.69 points inside this run's own 38-minute window**, on the
unsettled 08-03 bar:

| Clock (ET) | CL | RB | HO | 3-2-1 | distillate | **S49's 5-sess distillate change** |
|---|---|---|---|---|---|---|
| **09:13** | 78.85 | 3.004 | 3.967 | 60.808 | 87.756 | **−2.322** |
| **09:51** | **78.53** | **2.973** | **3.919** | **59.591** | **86.068** | **−4.009** |

⇒ **It is now 0.99 points from S49's branch-B line (≤ −5.0)**, against a settled-07-31 buffer of
**+2.158** that §D reported four stages ago.

⚠⚠ **STILL NOT SCOREABLE, and the discipline holds**: CL volume is **124,777 against a 235k–368k full
session (~35–50%)**, and **S49's registration says settled daily bars only, never mixed with
intraday.** Scoring branch B here would be **M201/D83's error a third time**.

★★★ **But the 38-minute move is itself a measurement worth keeping**, and it sharpens **D140**:
**§D established that a settled bar can be REVISED by 3.37 crack points; this addendum establishes
that the same observable can travel 1.69 points in half an hour while unsettled.** ⇒ **the frozen
"5-session change" is a stable *definition* sitting on an unstable *series*, in two independent ways.
S49 is a better observable than S8 and it is not a clean one — its own registration said so (C4);
this run has now supplied both numbers behind that caveat.**

⇒ **Handed to the 2026-08-04 run as its #1 scoring job**: pull the **settled** 08-03 close and score
S49 against **−5.0**. **Do not carry today's intraday figure forward as if it were the observable.**

## A-3 · What did NOT change

**No verdict in this report is revised.** The transmission matrix, the DEEP verdicts and the BET
sheet all rest on **settled 07-31** data, which drift cannot touch. **The Energy OW− stays held** —
and **the reason it is at risk is now dated and quantified rather than narrative**: MPC prints
**08-04**, S31 and S53 settle **08-05**, S49 and S52 settle **08-06**.
