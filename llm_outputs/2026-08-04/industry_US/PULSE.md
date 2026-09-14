# PULSE — "지금 무슨 일?" · 2026-08-04 19:55 ET / 2026-08-05 08:55 KST

> **The US regular session has CLOSED (16:00 ET).** Every number below is the **settled 2026-08-04
> bar**, not an intraday tick — **D74 does not apply to this read**, which is the opposite of the
> constraint that governed last night's run.
> **P4: analytical only. Zero buy/sell language, zero sizing.**

## 0 · ⚠⚠ FIRST — the settled bar falsified a number in THIS DESK'S OWN DRIFT addendum, 8 hours old

Last night's `MACRO_REPORT` §A-3 (DRIFT) quoted a **🟡live 11:2x ET** bar and wrote:

> *"the distillate−gasoline spread … **38.241 (08-03 settled) → 48.686 (08-04 live)**, **+10.445** …
> **It has now expanded a further +10.4 points inside one live session.**"*

**On the settled 08-04 close it did not expand. It narrowed.**

| | 08-03 settled | **08-04 🟡live (11:2x ET)** | **08-04 SETTLED** | live vs settled error |
|---|---|---|---|---|
| WTI `CL=F` | 80.34 | 76.91 | **75.20** | −1.71 |
| HO `HO=F` | 3.877 | 3.769 | **3.726** | −0.043 |
| distillate crack | 82.502 | 81.367 | **81.275** | −0.092 |
| **gasoline crack** | 44.261 | **32.681** | **43.971** | ⚠⚠ **+11.29** |
| **distillate − gasoline spread** | 38.241 | **48.686** | **37.304** | ⚠⚠ **−11.38** |

⇒ **The claim "the spread widened a further +10.4 points" is WITHDRAWN. The settled move is
38.241 → 37.304 = −0.937, i.e. a slight NARROWING.**

★ **What survives, and it is the part that carried the argument**: **DEEP-ENRG's finding is a
SETTLED-BAR measurement on the 08-03 firing session** — the spread widened **+5.300 to 38.241** there,
and **that is untouched.** The error is confined to the 08-04 *live* extrapolation.
⚠ **The guard worked and was not enough.** The addendum stamped the figure **🟡live · D74-contaminated ·
DIRECTION ONLY · NO VERDICT** — and the *direction* was still wrong, because **the gasoline leg alone
mis-read by 11.29 points intraday.** ⇒ **A "direction only" label is not a licence to state a
direction on an unsettled futures product leg.** Registered below as **D156**.

**A correction addendum has been appended to `MACRO_REPORT.md` (append-only — the original stays
visible next to it).**

---

## 1 · Price sweep — the book, ranked by the day's move

`module_paper_book pulse`, settled 2026-08-04. **Market context: S&P 500 771.3 (+1.8%) · Nasdaq
723.8 (+3.4%) · VIX 16.5 (+4.0%, but at a 120-day-low LEVEL).**

| Ticker | price | 1d% | 5d% | theme | stop |
|---|---|---|---|---|---|
| **AVGO** | 418.16 | **+6.6** | +9.1 | AI-compute EPICENTER | — |
| **096770** SK이노 | 111,300 | **+3.1** | −4.6 | energy-refining | — |
| **TSM** | 417.17 | **+2.7** | +4.5 | AI-compute EPICENTER | — |
| **NVDA** | 211.94 | **+2.6** | +7.9 | AI-compute EPICENTER | — |
| RTX | 217.93 | +0.6 | −0.2 | defense/missile | — |
| 009150 삼성전기 | 1,185,000 | +0.3 | −10.6 | IT-substrate/MLCC | — |
| MA | 571.10 | +0.0 | +3.5 | payments/FIN | — |
| KMI | 31.38 | −0.1 | −0.2 | energy-fuel/AI-power | — |
| LNG | 257.29 | −0.3 | +0.6 | energy-fuel/AI-power | — |
| **VST** | **143.23** | ⚠ **−8.2** | **−8.8** | **AI-power IPP** | — |

⚠ **One name ≤ −3%: VST. Zero ⛔ stop-hits — because ZERO stops are set** (every `stop%` cell is `—`).
**That is a book-hygiene fact, not a market fact, and it is stated rather than passed over.**

⚠ **This is the PAPER book.** The **real KIS book** that `cycle_exposure` reads held **$0.00 of the
AI-power adjacent layer** as of last night (PREMORTEM Lens 4). **The −8.2% lands in the paper book
only. Two different objects — do not merge them.**

---

## 2 · The same-day catalyst — and it is NOT VST's own news

**VST's own news axis is EMPTY**: `fts search Vistra --days 1 --scope foreign` returns **3 hits**, and
**none is about Vistra** (a 08-03 comparison piece, an ETF-movers wrap, and a PSEG earnings item).
**A −8.2% move with no name-level trigger is a read-through, and the source is one ticker over.**

### ★★★ The trigger: NRG −15.5% to a 52-week low, on INTEREST COSTS

`[PRIMARY-adjacent — RTTNews/nasdaq, full body]` **NRG Q2**: net income **$506m vs a −$104m loss** YoY ·
revenue **$7.48bn from $6.74bn** · **adjusted EBITDA $1.22bn, UP from $909m** — **and adjusted EPS
DOWN to $1.49 from $1.73.** **2026 guidance REAFFIRMED**, $1.0bn of buybacks + $407m of dividends.
Corroborated: *"NRG Energy **slumps to 52-week low after Q2 miss as interest costs climb**"*
[seekingalpha] · *"NRG Energy **misses quarterly profit estimates as interest costs rise**"* [Reuters].

★★★ **EBITDA up +34%, EPS down −14%. The gap is the interest line.** The operating business did what
the AI-power thesis says it should; **the capital structure took it away.**

### The cross-section says SUB-SECTOR, not sector — and it is the exact split this desk measured 8 hours ago

| | 1d% |
|---|---|
| **NRG** (merchant) | **−15.48** |
| **VST** (merchant) | **−8.15** |
| **CEG** (merchant/nuclear) | **−2.36** |
| TLN (merchant) | −1.30 |
| **XLU** (the sector) | **−0.56** |
| PEG (regulated) | −0.46 |
| AEP (regulated) | +0.02 |
| GEV (equipment) | **+1.17** · VRT **+2.62** · ETN **+1.49** |

⇒ **The merchant/IPP leg was repriced by 8–15 points while the regulated leg and the equipment leg
were flat-to-up.** ⚠ **Every % above is an ABSOLUTE 1-day move, not an excess return — against
SPY +1.80% the merchant leg's excess is roughly −10 to −17pp and the regulated leg's about −2.4pp
(C1, benchmark named).** Corroborating body `[nasdaq 08-04, ETF movers]`: the Virtus Reaves
**Utilities** ETF was the day's weakest of the ETFs that wrap surveyed, *"down about 1.9%"*, its
weakest components being *"**NRG, lower by about 15%**, and **Vistra, lower by about 6.9%**."*
⚠ **That source ranks against an unstated ETF set — quoted for its component detail, not for its
ranking claim (R41).**

★★ **This is DEEP-UTIL's regulated-vs-merchant split, arriving as a live event one session after the
desk measured it.** ⚠ **And it does NOT overturn that stage's verdict — it adds to it.** DEEP-UTIL's
permutation test killed the *statistical* claim that CEG+VST form a unit (*"a CEG finding wearing a
sub-leg label"*, p=0.200 on the 🔴 count). **Today is NEW evidence, arriving after the test, that the
merchant leg is a distinct object with its own driver.** **The test was about whether last week's
numbers proved it; today is a different question and a different date (S1).**

★★★ **And the driver is the one three separate stages converged on last night, from three directions:**
- **DEEP-UTIL**: PJM cleared at the **price cap** a third straight time while new supply **halved** ⇒
  *"the mechanism that converts merchant demand into merchant cash flow is capped."*
- **DEEP-RE**: the bottleneck is **the price of competing third-party capital**, with Goldman's
  *">1/3 of AI capex funded by debt in 2027."*
- **EVENT_ALPHA Card 5 / Fitch**: the AI channel into corporate credit is *"re-evaluation of long-run
  returns potential."*
⇒ **The AI-power node repriced on the COST OF CAPITAL, not on demand. Demand was up; the interest
line ate it.** ⚠ **n = 1 print (S1), on a name the desk does not hold in either book.**

---

## 3 · What else settled tonight — three of last night's brackets now have observables

⚠ **Recorded as observations for their scorers. NOTHING is scored here** — PULSE is a diagnostic
stage and does not settle brackets.

| Bracket | What printed | Reads toward |
|---|---|---|
| **S50** (AMD + ANET, → 08-06) | **ANET *"forecasts upbeat quarterly revenue on AI-driven networking demand"*** [Reuters via yahoo_finance]; **AMD +7.00%** on the settled bar, ANET **+3.04%** | **branch A on the ANET leg** (the pre-declared *confirmatory, low-information* branch). ⚠ **AMD's guide line itself is not yet body-read — the observable is the GUIDE, not the price (D28).** ⚠ **Reaction test, separately labelled: AMD's settled move +7.00% against the ±8.2% band pulled 08-04 ⇒ INSIDE the band.** |
| **S53** (MPC 08-04 + PSX 08-05, → 08-05) | **MPC beat**; Reuters: *"Marathon Petroleum posts **highest profit since 2022** as **supply disruptions lift margins**"*; MPC **+1.82%** | ⚠⚠ **This is branch A language — and it is the OPPOSITE of S49's registered meaning.** *"Supply disruptions lift margins"* is a **bottleneck-intact** statement from the issuer's own coverage on the session after the bottleneck was declared releasing. **S53 remains collapsed to a name-level footnote by its own registration (S49-B fired first) and may not be double-counted.** |
| **S49 / S55** | the **settled 08-04** crack | **S49's observable deepened to −13.803** (from −7.575) — further into branch B, already fired. ★ **S55's registration anchor is now SET at the 08-04 settle: HO%−CL% = −5.124.** **The window runs to the 08-11 settle; this is the anchor, not a verdict.** |

★ **The AI-compute epicenter had its best day of the window** — AVGO +6.61 · AMD +7.00 · ANET +3.04 ·
TSM +2.72 · NVDA +2.56 · QQQ +3.40 — **while the AI-POWER leg took −8 to −15.** **The same theme,
opposite signs, one session.** ⚠ **That is the cleanest single-session evidence yet that "AI" is not
one unit (W5), and it is n=1.**

---

## 4 · VERDICT

# ⇒ **NOT a crash. NOT a broad event. A SUB-SECTOR repricing on one name's interest line, with the book's largest leg having its best day of the window.**

- **Broad crash?** ❌ **SPY +1.80%, QQQ +3.40%, VIX 16.5 at a 120-day-low level.** The tape is risk-ON.
- **Sector event?** ⚠ **Half.** It is a **sub-sector** event — merchant/IPP power — with the GICS sector
  (**XLU −0.56%**) and the regulated leg essentially flat. **Calling it "utilities" would be the exact
  W5 unit error this desk logged three times last night.**
- **Idiosyncratic?** ✅ **for NRG** (its own Q2 miss, primary-sourced, interest costs). **VST is a
  read-through with an EMPTY own-news axis and its own print still ahead on 2026-08-07.**
- **Noise?** ❌ — a −15.5% 52-week low on a named, body-read cause is not noise.

**Book-level: 4 of 10 names up ≥ +2.6%, one down −8.2%, nothing else beyond ±1%.** **No stop was hit
because no stop is set.**

⚠ **asof caveat**: settled 2026-08-04 US closes, pulled 19:55 ET — **after the regular close but
during the after-hours session**, so a real-time screen may differ. **`096770` and `009150` are KR
closes from the 08-04 KRX session and are ~18 hours older than the US rows.**

---

## 5 · New dig registered by this stage

> ⚠ ID checked at write time against all `handoff/*.md`; highest existing is **D155** (this run's ALPHA).

| # | Dig | Why it matters | Owner |
|---|---|---|---|
| **D156** ★★ | **A "🟡live / direction-only" label does not make an unsettled FUTURES PRODUCT leg safe to state a direction from.** Measured tonight: between an 11:2x ET pull and the settle, **WTI moved −1.71, HO −0.043, the distillate crack −0.092 — and the GASOLINE crack moved +11.29**, flipping the distillate−gasoline spread from *"+10.4 points of further widening"* to **−0.937, a slight narrowing.** ⇒ **the desk's own DRIFT addendum stated a wrong direction while carrying every warning label correctly.** | **The product legs are far more intraday-unstable than the crude leg or than the composite — RB alone accounted for essentially the whole error.** ⇒ **Remedy: a DRIFT observation on a crack or spread quotes the CRUDE leg and the composite intraday if it must, and reports product-leg spreads as `[pending settle]` with no direction at all.** Same family as **D74 · D31 · D140** — but the new content is that **a labelled guard was insufficient; the fix has to be "do not state it", not "state it with a warning".** | DRIFT · MACRO |
