# PULSE — live diagnostic · 2026-07-22 (Wed)

> L1·PULSE. **Same-day signals only.** The research desks' lagging inputs are *not* used for this
> verdict. One question: **broad crash / sector event / idiosyncratic / noise?**
> Run **2026-07-22 22:56 KST = 09:56 ET — the US regular session opened 26 minutes ago.**

## ⚠ asof caveat (stated first, per the stage rule)

- Prices are **intraday, ~26 minutes into the US session.** They will move. A 26-minute sample is not
  a session, and every 1d% below is a partial-day number.
- This run's own desk output (`llm_outputs/2026-07-22/industry_US/`) was written **before the open**,
  on FRED asof 07-20 and a flow sweep asof **07-21 close**. **This pulse is the first live test of it**
  — that is what makes it worth running today.
- The event brief is **binned by publish time and the day is still filling**: 06:2x ET showed
  1,132 articles → 206 events; 09:5x ET shows **2,485 → 430**. Today's counts are a **floor**, not a total.
- A failed quote is a **blank**, not a red number. None were needed — all quotes returned.

---

## §1 · Price sweep — every book position (`module_paper_book pulse`)

Market context: **S&P 748.4 (+0.0%) · Nasdaq 707.5 (−0.2%) · VIX 17.2 (+1.0%)**

| Ticker | Price | 1d | 5d | stop dist | Theme |
|---|---|---|---|---|---|
| 009150 | 1,345,000 | **+2.7** | +4.3 | +6.7 | IT-substrate/MLCC |
| VST | 165.87 | **+2.2** | +4.7 | +9.8 | AI-power-IPP |
| RTX | 196.24 | **+1.3** | +1.5 | +7.8 | defense-missile |
| KMI | 32.40 | +0.1 | −0.4 | +6.6 | energy-fuel |
| LNG | 262.69 | +0.0 | −0.9 | +16.8 | energy-fuel |
| NVDA | 207.96 | +0.3 | −1.8 | +7.8 | AI-compute epicenter |
| AVGO | 385.92 | −0.2 | −0.8 | +7.2 | AI-compute epicenter |
| MA | 535.41 | −0.5 | −0.5 | — | payments |
| TSM | 419.79 | −1.1 | −0.1 | +6.3 | AI-compute epicenter |

**⚠ Names ≤ −3%: none. No stop hit. Nothing in the book is in trouble.**

---

## §2 · Live tape on the names this morning's run actually concluded on

Not book positions — the run's own conclusions, tested against the open.

| Group | Live 1d | Read |
|---|---|---|
| **Energy / refining (DEEP ①)** | XLE **+1.29% — best sector on the board**; VLO +0.65, MPC +1.18, PSX +1.03, XOM +1.30, SLB +1.94. Brent **+2.71% → $93.48**, WTI +1.92% → $86.54 | **CONFIRMS.** The OW+ is being paid on the first live session after it was written |
| **Defense (DEEP ③, pre-mortem-promoted)** | **NOC +3.56%**, LMT +2.12%, GD +1.38%, RTX +1.31% vs XLI +0.50% | **CONFIRMS, and the promotion was the right call.** The primes beat their own sector by 0.9–3.1pp, one day before the RTX/LMT binary |
| **AXON** (demoted out of the defense bucket by DEEP) | **−2.01%** (5d −7.54%) | **CONFIRMS the carve-out.** It traded opposite the primes on the day the primes ran |
| **Financials non-bank (DEEP ②)** | **GS +1.79%, MS +1.43%**; STT +0.18, USB +0.27, TRV +0.05, PYPL −0.02; **CB −3.61%** | ★ Two live findings, below |
| **Security / observability (§D, promoted this morning)** | **DDOG −3.92%, PANW −2.53%, CRWD −1.80%, FTNT −1.54%** vs XLK −0.35% | 🚩 **The day's worst group among the run's names.** See §4 |
| **Memory / semicap (the re-scoped UW)** | MU −0.11, SNDK −0.90, WDC +1.52; 5d **MU +13.66, WDC +19.27, SNDK +11.63**. Semicap all ≈ −0.8% | UW **not paid today**; memory is holding its 5-day rip |
| **Tonight's binary** | GOOGL **+0.10%** and TSLA −0.04% — both flat into their own prints — while **META −1.75% and MSFT −1.44%** | The market is de-risking the *read-through*, not the printer |
| **Pharma vs managed care** | **LLY −1.32%**; MRK +1.12, ABBV +0.12, PFE +0.58, BMY +0.74. XLV −0.18% | See §4 — the tariff is one name so far |

---

## §3 · Same-day catalyst search (`--days 1`, `--scope foreign`)

**Event axis, re-run at 09:5x ET (2,485 articles → 430 events):**

| Rank | Event | Coverage | vs 06:2x ET |
|---|---|---|---|
| **1** | **"OpenAI says its AI model went rogue and hacked startup"** | **28 articles / 20 outlets** | **was 4→8 outlets. Now 20.** The fastest-accelerating thread on the board, and now the day's #1 |
| 2 | **"Oil Prices Extend Rally As Mideast Tensions Escalate"** + "Oil prices rise after US announces new round of strikes" | 28/11 + 17/13 | Escalating |
| 3 | **"Trump vows to hit an Iranian bridge or power plant for every [attack]"** | 7/7 | **New since this morning** |
| 4 | **"AMD to invest up to $5bn in Anthropic in chip deal"** | 16/8 | **New since this morning** |
| 5 | "Alphabet Earnings Put Big Tech AI Spending Under Scrutiny" | 20/8 | Was 6/5 |
| 6 | "Pharma stocks bleed after Trump announces up to 200% tariff" | 13/8 | Was 11/7 |
| 7 | "AI investment boom puts Big Tech's free cash flow under pressure" | 8/7 | Holding |

**Per-name searches on the three biggest movers — no single-name trigger found:**
- **DDOG (−3.92%)**: the only same-day hit is index boilerplate — *"…Adobe (ADBE), **Datadog (DDOG)** and
  Autodesk (ADSK) closed down…"*. That names a **software-group move**, not a Datadog event.
- **CB (−3.61%)**: hits are earnings-preview listings only (*"results are expected from Interactive
  Brokers, Chubb and Capital One"*). No adverse story surfaced.
- **NOC (+3.56%)**: hits are ticker-listing furniture. **No news explains it.** The likeliest reading is
  the tape catching up to **NOC's own 07-21 guidance raise ($28.60–29.10)** — the raise this morning's
  DEEP flagged as **not yet reflected in vendor consensus (27.9501)**.
- Sector-term check: `"software selloff"` = **2 hits — n too small to be a measurement**. `cybersecurity`
  = 213 hits, but the bodies are about a Chinese-AI-model ban push and vendor security models, **not a
  sector selloff catalyst**.

**Honest result: for the biggest single-name moves, no same-day catalyst exists in the feed.** That is a
finding, not a gap to fill with a story.

---

## §4 · The two live corrections to this morning's run

### 🚩 1. The node the pre-mortem promoted is the day's worst — while its narrative went 4 → 20 outlets

This morning the pre-mortem pulled **PANW/CRWD/FTNT/DDOG** out of the Info Tech underweight, on the
grounds that a blanket UW would short the cleanest live instances of the desk's only A-grade signal
(RS60 +66 to +94 vs SPY, all with positive RS20). ALPHA tagged FTNT and DDOG **🟢LIVE**.

**On the first live session the whole node fell 1.5–3.9%, underperforming XLK by 1.2–3.6pp — on the same
day its catalyst thread more than doubled its outlet count and became the #1 story of the day.**

- **Narrative accelerating, money leaving.** That is precisely the configuration EVENT_ALPHA's own card
  format is meant to catch, inverted.
- The **kill condition was pre-registered and is not yet met**: *"RS20 vs SPY crossing below 0."* Five-day
  moves are DDOG −6.68, CRWD −7.87, PANW −5.79, FTNT −3.18 — the 20-day relative still has a large
  cushion (+8 to +19 vs SPY as of 07-21). **Not tripped. Moving toward it.**
- ⚠ **n = 1 partial session, and no name-level catalyst was found.** This is logged as a live
  counter-observation, **not** as a reversal of the finding. The honest statement: *the promotion is
  being sold on day one, for no reason the feed can name.*

### 🚩 2. The correlated-underweight finding takes a one-day counter-observation

This morning's headline pre-mortem finding: **IT + Real Estate + Utilities are one AI-datacenter short**,
because RE's reds were digital infrastructure while duration REITs were bid, and Utilities' red was CEG.

**Today the tape ran the other way:**

| | Live 1d |
|---|---|
| Digital infra (the "reds") | AMT **+0.52**, DLR +0.08, EQIX **+0.54**, CCI **+0.81** — all **up** |
| Duration REITs (the "bid" ones) | WELL **−0.53**, VTR −0.37, SPG −0.35, PLD **−1.71** — all **down** |
| CEG (the Utilities red) | **+2.54% — the best utility on the board**; XLU +1.24% |

**That is the inverse of the 20-day pattern the finding rests on.** One session does not overturn a
20-day cross-section (S1: this is n=1), but it is exactly the observation that would, repeated. The
finding stands; **the counter is recorded rather than quietly dropped.**

### Two things that went the desk's way, stated with the same discipline
- **GS +1.79% / MS +1.43%.** ALPHA registered the falsifier as *"RS20 vs SPY crosses 0 while revisions
  hold → the de-rate was a post-print air pocket."* Today is a step toward that falsifier firing — i.e.
  toward the "dislocation" having been an air pocket rather than a signal. **Recorded as progress toward
  the falsifier, not as a win.**
- **CB −3.61% was the worst financial on the board.** The crowded short (FINRA z **+1.61**) did **not**
  squeeze; it went down. ⚠ Consistent with the rejected-ledger entry that crowded-short extremes are
  **not** a contrarian trigger.

### One correction to this morning's read on Health Care
**"Pharma stocks bleed"** (13 articles / 8 outlets) is, on the tape, **one name**: **LLY −1.32%**, while
MRK **+1.12**, BMY +0.74, PFE +0.58, ABBV +0.12 and XLV −0.18%. The morning's split of the sector into
tariff-exposed pharma vs managed care was right in structure — but so far the hit is **idiosyncratic to
LLY**, not a pharma-node event. Managed care is flat-to-soft (HUM −0.74, UNH −0.32), so it is not
absorbing a rotation either.

---

## §5 · The crack question — cannot be advanced today, and here is why

Crude is up (**WTI +1.92%, Brent +2.71%**) while the product contracts are **down**: **RB=F −4.10%,
HO=F −1.42%.** Mechanically that is crude-up / crack-down, which would take the DEEP·ENRG **detachment
counter from 3 to 4** (at 5, the equity is priced off something other than its KPI).

**It is not counted.** This morning's DEEP explicitly excluded the **07-22** product prints as a
**contract-roll artifact** (it measured `BZ=F` printing *below* `CL=F` and `RB=F` −4.4% on 7,232 lots).
Today *is* 07-22 — this is the same print DEEP already threw out. Brent has since normalised above WTI
($93.48 vs $86.54), so the roll is passing, but the gasoline contract is still the excluded one.
**The counter stays at 3. Next clean reading: tomorrow's session.** Recording a 4 off a roll artifact is
exactly the kind of number that would then be quoted back as evidence.

---

## §6 · Verdict

**NOISE — no crash, at the book level or the market level.**

- **Not a broad crash**: SPY +0.0%, VIX **17.2**, and **17.2 is below the 18.65 that this morning's
  MACRO §A carried** — the vol tape is *calmer* than the report's own baseline, nowhere near the >24
  anti-signal.
- **Not a sector event against the book**: the book's two largest thematic exposures (AI-compute
  epicenter, energy-fuel) are flat-to-up, and its best names today are **009150 +2.7%, VST +2.2%,
  RTX +1.3%**.
- **Not idiosyncratic**: no book name is ≤ −3%; no stop is threatened (nearest is TSM at **+6.3%** of
  headroom).
- The only cluster worth naming is **software/observability −1.5 to −3.9%**, and **the book does not own
  any of it** — it is a research conclusion from this morning, not a position.

**Live status of the pre-registered brackets** — none moved, none scored:

| Scenario | State at 09:5x ET |
|---|---|
| **S1** GOOGL capex | Prints tonight. **GOOGL +0.10% — flat inside its own ±7.1%.** Nothing to score |
| **S6** INTC 07-23 | INTC +0.48% (5d **+9.26%**) — pending |
| **S7** RTX+LMT 07-23 | RTX +1.31 / LMT +2.12 — pending; **one binary, n≈1** |
| **S8** Hormuz | **Branch C (escalation) still the live pointer.** Brent +2.71%, and *"Trump vows to hit an Iranian bridge or power plant for every [attack]"* is **new since this morning**. Branch A requires crude **down** with cracks rolling — crude is up |
| **S9** dovish real-rate | XLU +1.24 and XLRE −0.15 point in **opposite** directions today; nothing decided |

⚠ **No fabricated crash.** The data says calm, and the two soft spots (cyber, CB) are named as soft
spots with no catalyst found rather than dressed up as a selloff.

## ✅ EXIT CHECK
- [x] `pulse` run — every book position's 1d/5d/stop-distance read, plus SPY/Nasdaq/VIX context.
- [x] Same-day (`--days 1`) catalyst pulled for the biggest movers; top hits **body-read**, and the
      result reported honestly as **"no single-name trigger found."**
- [x] Event axis re-run at 09:5x ET to surface what the term search would have missed — it surfaced two
      new head events (**AMD–Anthropic $5bn**, **Trump's bridge/power-plant threat**) and the
      OpenAI thread's jump to **20 outlets**.
- [x] Verdict stated (**noise**) with the asof-time caveat stated first, and the 26-minute-sample
      limitation carried into every 1d number.
