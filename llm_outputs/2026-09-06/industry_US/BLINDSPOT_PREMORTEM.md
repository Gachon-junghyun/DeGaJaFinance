# BLINDSPOT_PREMORTEM — industry_US · 2026-09-06 (Sun) · Stage 7 / L1·PREMORTEM ★US-only

> Four adversarial lenses argue **AGAINST this run's own tilt** before the DEEP budget is committed.
> **P4 — no sizing, no buy/sell language.**

## §0a · ⚠⚠ Declared weakness — the lenses ran IN-CONTEXT and SERIALLY, not as a parallel agent fan-out

The stage specifies *"an Agent fan-out, 4 lenses in ONE message (parallel)."* **This run did not do
that.** The four lenses below were executed **in-context and serially by the same reasoning process
that wrote the draft tilt they are meant to attack.** This is the **10th consecutive run** on this
desk with the same substitution and it is declared here rather than omitted, because an adversary
who shares the defendant's priors is a weaker adversary and the reader is entitled to price that in.
**Mitigation actually applied**, so the declaration is not merely an alibi: **every lens verdict
below is required to rest on a number this run pulled, not on an argument** — and two of the four
(Lens 1, Lens 3) reach conclusions that **contradict** the draft tilt and one (Lens 2) **registers
the against-us branch as the informative one**.

## §0b · The condition that makes this pre-mortem unusual, and it cuts against the desk

**The price tape has produced no new session since the last run** (`asof 2026-09-04`; **2026-09-07 is
Labor Day**, so the next settled close is **2026-09-08**). ⇒ **ROTATION correctly issued 0 deltas of
11 attempts**, and the desk therefore enters this stage carrying **verdicts set on Friday's tape
against events that happened on Saturday and Sunday.**

★★ **That is precisely the tunnel this stage exists to break.** A run with no new prices has no
mechanism to *revise* a tilt and every incentive to *repeat* it. The four lenses are therefore aimed
at the carried tilt, not at a fresh one.

## §0c · Catalysts injected, and one of them was invisible to the desk's own calendar

`catalyst_calendar --days 12` returned **4 binaries**: Aug **PPI 09-10** ✓ · Aug **CPI 09-11** ~est ·
**FOMC 09-16** ✓ · an **undated** Hormuz-open statement 👁 — plus the S&P rebalance **09-18**.
**None is ≤48h** (nearest is D-4), so the protocol's **mandatory ≤48h both-sides bracket does not
trigger on a date**. ⚠ But the standing instruction survives: *a one-way tilt into a known binary is
a violation*, and there are four known binaries.

🚨 **The calendar's EARNINGS block printed `(none in window / yfinance unavailable)` — and it is
wrong.** `Ticker.earnings_dates` returns:

| name | mcap | prints | implied move |
|---|--:|---|--:|
| **`ORCL`** | ~$1.0T class | **2026-09-10 16:00 ET** | ★ **±11.8%** (expiry 09-11, D5) |
| **`ADBE`** | ~$180B class | **2026-09-10 16:00 ET** | **±8.1%** (expiry 09-11, D5) |

⇒ **2026-09-10 carries THREE US binaries in one session** — Aug PPI at 08:30 ET and two large-cap
software prints at 16:00 ET — **and the desk's own calendar saw one of them.** Registered as
**`D540`**: *the calendar's earnings block fails silently (`yfinance unavailable`) while the same
library, called directly, returns the dates — so an empty EARNINGS block must be treated as UNKNOWN,
never as "none."* ★ Also note **`P127`'s window closes at the 09-10 close**, i.e. **before** the
16:00 ET prints ⇒ they are **not** a contaminant for it, which is recorded now rather than argued at
scoring (`D450`).

---

## LENS 1 · UNDER-COMPUTED LEGS — the strongest bull/bear case for something we did NOT deep-dive

**Verdict: 2 legs surfaced. 1 → PROMOTE-TO-DEEP. 1 → WITHIN-RUN-WATCH. Neither was in the draft tilt.**

### 1a · 🚨 **DEFENSE — PROMOTE-TO-DEEP.** The book holds a position inside a node at a one-year price extreme, and nobody has looked

The draft tilt has `INDU UW−` and treats Industrials as one bucket. **It is not.** Measured this run
on the settled tape:

| ticker | flow | OBV | rs20 | rs60 | held? |
|---|--:|--:|--:|--:|:--:|
| **`RTX`** | 🚨 **−0.79** | −0.29 분산 | **−9.6** | +7.0 | ★ **YES** |
| `LMT` | −0.74 | −0.24 분산 | −10.3 | −6.1 | — |
| `NOC` | −0.72 | −0.34 분산 | −9.5 | −11.2 | — |
| `LHX` | −0.65 | −0.19 분산 | −10.1 | −21.5 | — |
| `EME` | −0.63 | −0.11 분산 | −7.3 | −9.1 | — |
| `GD` | −0.52 | **−0.44** 분산 | −7.9 | −0.8 | — |
| `HWM` | −0.32 | −0.19 분산 | −7.6 | −2.3 | — |

**Seven of seven negative on flow · six of seven 분산 · every `rs20` between −7.6 and −10.3.**

★★ **And the price instrument says it is a one-year extreme, not a drift**: `EW{RTX,LMT,NOC,GD,LHX}`
− `SPY` over 5 sessions = **−5.166 = the 7.1st percentile of trailing 252**.

★★★ **The discriminating measurement, which changes the target of the finding.**
`EW{LMT,NOC,GD,LHX}` − `RTX` = **+0.127 = the 57.5th percentile** ⇒ **on PRICE, `RTX` is not
meaningfully worse than its peers**, even though on **flow** it is the worst of seven.
⇒ **The flow says "the book holds the worst name"; the price says "the node is the event."** The
correct object is the node, and `S150` is written on the node — **which is a correction to this
run's own EVENT_ALPHA §3 framing**, made inside the same run (see §5.2).

⚠⚠ **The narrative side is entirely absent**: **no defense thread appears in the 44-thread alive
set**, and `catalyst_calendar` carries no defense event. **The flow moved and the wires did not** —
which is either an early signal or a `D6` C-axis artifact, and the desk cannot currently tell which.
`RTX`'s chart corroborates the sweep on a second instrument (**RSI 21.8, price at the lower Bollinger
band, 1 of 4 MAs, OBV −35% 20d slope, momentum −10.1%**).

⇒ **PROMOTE-TO-DEEP** as the **5th DEEP** (ROTATION left both rotating slots unfilled). Bracket:
**`S150`**, settles **2026-09-14**.

### 1b · **UTILITIES / the AI-power lane — WITHIN-RUN-WATCH, and its case got stronger this run**

ROTATION declined `UTIL UW→N` for a **6th** time — **but on one reason instead of two**, because
`SWEEP_READ §3` killed the breadth leg: `CEG` (surge 0.96, **OBV +0.19 매집, rs20 +11.2, rs60 +17.2**)
and `VST` (surge 1.02, OBV +0.21, rs20 +6.6, **Δ +0.49 = the board's 3rd-largest**) meet every merit
condition and are excluded from 🟢 **by `vol_surge` alone**. ⇒ **the sector's breadth 0.00 is a
filter artifact, not evidence** — and the artifact sits on the axis this desk's own KR IC ledger
scores **IC −0.0414 / t(NW) −3.61 / n_eff 45, Bonferroni-negative for a 4th run**, while the gate
weights it positive (`C29`).

⚠ **Why WATCH and not PROMOTE**: the lane already carries **four** dated rows (`P123` 09-08 ·
`P127` 09-10 · `S146` 09-14 · plus `S135` 09-11 on the duration trio), and the 5th DEEP slot is
better spent on the leg with **zero** rows (defense). **Promoting a leg that is already
quadruple-bracketed is padding.** Stated so the decision is checkable.

### ⚠ Legs considered and NOT surfaced, with the number that stopped them

- **Real Estate** (8-run recency gap, the longest on the board): its four best names *are* OBV 매집
  (`WELL` +0.17 · `AMT` +0.17 · `DLR` +0.14 · `VTR` +0.10) — **but their `flow_score` tops out at
  0.360**, below the gate on the **non-news** axes, so unlike Utilities its breadth 0.00 is
  **evidence**. 11 of 12 negative on `exc5` agrees. **No case.**
- **Comm. Services** (16 runs unrankable): its four best names are **all 매집 with positive `rs20`**
  (`WBD` +0.34/+5.9 · `META` +0.30/+4.6 · `T` +0.38/+8.3 · `VZ` +0.13/+6.9) and `exc20` median
  **+3.70** vs mean +1.27. ⚠ **This is a real bull case and it is barred, not rejected** — `D459`,
  12th run: Alphabet is **76.6%** of the bucket across two share classes and the per-ticker flag
  prints `False`. **A leg this desk cannot aggregate cannot be promoted, and saying so for a 16th
  time is the finding.**

---

## LENS 2 · REGIME-FLIP / BOTH-SIDES — for each known binary, the against-us branch

**Verdict: 4 binaries assessed. 2 bracketed both ways. 3 explicitly declined with reasons (`B4`).**

### 2a · ★★★ The undated binary that matters most: **the against-us branch is named by a policymaker on the record**

The desk carries **`ENRG OW+`** — its only top-notch overweight — and **every flow number supporting
it predates both weekend events.** The against-us branch is not hypothetical:

| against-us evidence | source · date |
|---|---|
| ★ **US Treasury Secretary Bessent forecasts $40 crude and lower yields post-war** | economictimes · seekingalpha, **09-05** |
| **OPEC+ met 09-06 and left policy UNCHANGED** | 7 outlets, **09-06** |
| Trump calls the conflict **"small potatoes"** | 3 outlets, 09-05 |
| Bloomberg reframes it as **"economic endurance"** (attrition, not shock) | 09-06 |
| **Iraq is sourcing tankers for Hormuz runs** — the workaround is being built | bloomberg, 09-04 |
| ★★ **Venezuela: 65bn barrels opened, `CVX` $7bn to double output, SPR refill from Venezuelan crude** — a **structural supply ADDITION** running at **2.95× acceleration** | ~15 outlets, 08-29 → 09-05 |

**⇒ The de-escalation/supply-addition side is LARGER in outlet count than the escalation side.**

★ **What rips if it fires, and which of our OWs gets hit** — `ENRG OW+` directly (the sector is
rank-1 on every flow axis the desk owns and rank-1 exposure to a war premium unwinding), and
**`MPC`/`PSX` are held.** Second-order: a B print also removes the input-cost leg of `P140`'s
compression case, so **`P140` and `S149` can fire in ways that disagree, and that disagreement is
informative** rather than a defect.

⇒ **`S149` REGISTERED** (settles **2026-09-11**): `CL=F` 5-session % change · **A ≥ +8.343** (p85) ·
**B ≤ −5.734** (p15) · state **+9.688% = 87.7th percentile**.
⚠⚠ **Disclosed at registration**: the *level* is already above A's line, but the observable is the
change over the **next** five sessions, so it does not pre-fire — and a +9.7% base makes **B the more
reachable branch**. **That is deliberate.** `B4` says the informative branch is the one that would
change the conclusion, and **B is the one that breaks the desk's only OW+.**
⚠ Threshold source stated: `XLE`'s straddle is **±1.6% expiring 09-09**, i.e. **before the row
settles**, so it cannot bound the window ⇒ thresholds come from `D93` on the observable itself. This
is the `M1305` scope error (corrected by `M1326`) being avoided rather than repeated.

### 2b · ★★★ The 09-10 triple binary — bracketed on the OBJECT, not on the magnitude

**PPI 08:30 ET + `ORCL` 16:00 ET + `ADBE` 16:00 ET, one session.** The against-us branch here attacks
`P101`'s settle, which the 09-05 run called its most informative of that run: software −4.458% vs
hardware +2.053%, participation inverting **91.7%/16.7% → 21.1%/73.0%**.

⇒ **`S148` REGISTERED** (settles **2026-09-14**): `EW{SW n=19}` − `EW{HW n=37}`, 5 sessions,
09-04 → 09-14 · **A ≥ +3.927** (p85) · **B ≤ −7.906** (p15) · state **−6.511 = 21.0th percentile**.
★ **`ORCL` and `ADBE` are both IN the 19-name software leg** — the leg is tested by its own
constituents, not by beta. **Reconstruction verified: 19 and 37 exactly, and it reproduces `P101`'s
settle value (−6.511) on this run's independent price frame.**
⚠ **Disclosed**: the state sits **1.40pp from B and 10.4pp from A** ⇒ **A is the informative branch**;
a B print is the near one.

### 2c · ⚠ Binaries DECLINED, each with its number (`B4` — "if neither branch would change the conclusion, say so and spend the bracket elsewhere")

| binary | date | declined because |
|---|---|---|
| **`ORCL`/`ADBE` MAGNITUDE** | 09-10 | 🚫 **NO-INFORMATION at any settable threshold.** Implied **±11.8% / ±8.1%**; the observable's trailing-252 **p85/p15 vs `SMH` are +3.153 / −3.660** — a third of the implied move, so **C is guaranteed**. A threshold placed *outside* ±10% has a near-zero base rate, so **neither tail can fire either**. ★ **Measured precedent, not judgement**: `S132` (±9.00) and `S138` (±11.00) **both fired C on the identical −3.792pp `AVGO` realization** — the same print, two band widths, zero information difference (`D503`) |
| **US August PPI, standalone** | 09-10 | Its transmission already sits **inside `S148`'s window** and inside `S149`'s CPI/PPI energy leg. A standalone row would duplicate `P121`/`P125`'s leg question, and those are **blocked on `D427`** — not absent, blocked |
| **FOMC + SEP/dot plot** | 09-16 | **Outside every window this run opens**, 10 days out, and the next run will have a **settled tape** and a **fresh COT (Friday 09-11)** to set thresholds from. Deliberately deferred — deferring with a reason is not the same as missing |
| **S&P rebalance / quad witching** | 09-18 | **Structural, not directional.** It moves volume, and the desk has no volume-conditioned proposition; **neither branch would change a sector verdict.** `P124` already settles that date |
| **KOSPI200 quad witching** | 09-10 | 🚫 **Out of scope for a `--market us` runtime (`W1`).** The 09-06 KR run asked the next US run to bracket it because KR has no PREMORTEM block. ⚠ **This run records that a US-pure desk cannot discharge it either** — a KOSPI200 observable on a `--scope foreign` desk is exactly the cross-market transfer `W1` bars. ⇒ **`D533` stays OPEN** and needs a human or a KR protocol change (**P5**). Naming it as undischargeable is more useful than pretending it was handled |

### 2d · ★ The correlated-UW check (the 2026-07-15 field note)

`RE` + `STPL` + `UTIL` remain **one duration bet under three labels** — all three carry breadth
**0.00** against a rate complex at the 96th–99th percentile, and **`S135` (09-11) already brackets
them as ONE object.** ⚠ **New wrinkle this run**: the three are **not** symmetric any more —
Utilities' zero is now measured as a **filter artifact** while Real Estate's is **evidence**
(Lens 1). ⇒ **`S135`'s equal-weight construction is now known to average one measured bucket with one
mis-measured one**, which is recorded as a **construction note on a live row**, not a re-threshold
(`D242` — the row is not touched). Filed as **`M1372`**.

---

## LENS 3 · MOMENTUM-CONTINUATION — "already ran" ≠ avoid. Re-tag every runner.

**Verdict: 7 runners re-tagged. 3 EXTENDED-BUT-LIVE · 2 EXHAUSTION-WATCH · 1 EXHAUSTED · 1 REJECTED
BY ITS OWN SECOND INSTRUMENT. Each with its flip condition.**

⚠ **`D6` applied throughout**: the sweep's `obv_norm` and `module_chart`'s OBV slope are the **same
C-grade axis on two implementations**, so agreement between them is corroboration of the *reading*,
not promotion of the *grade*. Where they disagree, that is a `C25` instance and is written out.

| name | 20d momentum | RSI | OBV (sweep / chart) | divergence | turn-verdict | **re-tag** | **flip condition** |
|---|--:|--:|---|---|---|---|---|
| **`MPC`** (held) | **+21.7%** | **76.0** | +0.62 매집 / **누적 +52%** ✅agree | **none** | **CONFIRMED-TURN** | ★ **EXTENDED-BUT-LIVE** | RSI 76 with **no divergence** and a coiling band is extension *without* deterioration. **Flips to EXHAUSTED if a bearish RSI divergence appears OR the distillate crack's 5-session change breaks `P140`'s p15 (−4.209)** — the cycle KPI, not the price |
| **`PSX`** (held) | +19.0% | 68.6 | +0.43 매집 / 누적 **+58%** ✅agree | 🚨 **BEARISH** (price HH, RSI LH) | CONFIRMED-TURN | ⚠ **EXTENDED, EXHAUSTION-WATCH** | ★ **This is the discrimination the lens exists for: `MPC` and `PSX` are treated as one node everywhere in this desk's carry, and only `PSX` carries a bearish divergence.** Flips to EXHAUSTED if the divergence persists through the **09-08** settled close |
| **`SNDK`** | ★ **+40.6%** | **46.7** | +0.35 매집 / **누적 +121%** (the strongest slope measured) ✅agree | none | **PULLBACK-TO-SUPPORT** | ★★ **EXTENDED-BUT-LIVE, cleanest on the board** | +40.6% momentum with **RSI only 46.7** means it ran and then *consolidated* — the textbook shape the lens's own spec describes. ⚠ `rs60 −0.3`: **the run is 20 days old, not 60.** Flips if OBV slope turns negative on a settled close |
| **`MSTR`** | ★ **+46.7%** | 71.2 | +0.33 매집 / 🚨 **중립 +2%** ⚠**DISAGREE** | none | **NEUTRAL/CHOP**, band **expanding 60.9%** | 🚨 **EXHAUSTED** | **The board's largest 20-day momentum with essentially NO OBV confirmation on the chart instrument (+2% slope).** Price ran 46.7% and the volume did not follow. ⚠ It also carries **two standing rejections that give opposite answers** (`C27`, recheck 09-18/09-22) and `D463` says surface them. **Flips to LIVE only if the chart OBV slope exceeds +20% on a settled close** |
| **`HOOD`** | +29.2% | 68.1 | +0.21 매집 / 누적 **+80%** ✅agree | 🚨 **BEARISH** | CONFIRMED-TURN, band **expanding**, upper band | ⚠ **EXTENDED, EXHAUSTION-WATCH** | Bearish divergence **plus** an expanding band at the upper edge. Its sector (`FIN`) was promoted `UW→N` only two sessions ago. Flips to EXHAUSTED if it closes below the 20DMA with the divergence intact |
| **`SLB`** | +8.7% | 64.1 | +0.44 매집 / 누적 **+87%** ✅agree | **none** | **CONFIRMED-TURN**, **ignition trigger `close > 57.94` UNFIRED** | ★ **EARLY, NOT EXTENDED** | The only name here where momentum (+8.7%) is *small* relative to OBV (+87%) — **accumulation ahead of price**, and `rs60 −2.6` says the move is 20 days old. **This is the opposite of an exhaustion profile**, and it is the one name EVENT_ALPHA handed to BET |
| **`NEM`** | +9.5% | 58.4 | 🚨 **+0.14 매집 / 분배 −58%** ⚠⚠ **OUTRIGHT DISAGREEMENT** | 🚨 **BEARISH** | NEUTRAL/CHOP | 🚨 **REJECTED BY ITS OWN SECOND INSTRUMENT** | see `C25` note below |

### ★★ `C25` — the first US instance where the two OBV instruments DISAGREE, and it kills a card's exposure name

The desk carries `C25` (*two instruments read OBV's sign oppositely*) with the note that the US half
**cannot be narrowed** the way the KR desk narrowed its own (no US investor-type feed, `W1`). The
09-05 run checked two US instances (`MPC`, `ETN`) and **both agreed**. **This run checked seven:**

| result | names |
|---|---|
| ✅ **agree** (5) | `MPC` (+0.62 / 누적 +52%) · `PSX` (+0.43 / +58%) · `SLB` (+0.44 / +87%) · `HOOD` (+0.21 / +80%) · `SNDK` (+0.35 / +121%) · `RTX` (−0.29 분산 / 분배 −35%) — **6 including `RTX`** |
| ⚠ **partial** (1) | `MSTR` — sweep **매집 +0.33** vs chart **중립 +2%** |
| 🚨 **outright opposite** (1) | **`NEM`** — sweep **매집 +0.14** vs chart **분배, 20d slope −58%** |

⇒ **6 agree, 1 partial, 1 opposite out of 8 checks. `C25`'s US half now has a measured disagreement
rate, which it did not have before** (`M1373`). ★ **And it has a consequence**: `NEM` is the **sole
exposure name** on `EVENT_ALPHA` Card 4 (gold repatriation). The card's verdict was already
**STORY-ONLY**; this **hardens** it — the one instrument that made the name look accumulating is
contradicted by the other, **and the name also carries a bearish divergence.** The missed-ledger
`--enters-if` written at EVENT_ALPHA (*a second central-bank relocation ≥4 outlets AND rs20 > +15*)
is **left unchanged** rather than tightened after the fact (`D242`), and this contradiction is
attached to the row as context.

---

## LENS 4 · CYCLE-EXPOSURE — registry vs coverage vs the REAL book

**Verdict: no GAP by the registry, and the registry is the problem.**

`cycle_exposure` on the real KIS book (total ≈ **$11,022** · invested **$5,255** ⇒ **52.3% cash**):

| cycle | rank | epicenter % | bar | held epicenter | GAP |
|---|--:|--:|--:|---|:--:|
| AI-compute / semiconductors | 1 | **17.48%** | ≥12% | `NVDA`, `ANET` | ✅ |
| Energy / oil-refining | 2 | **10.47%** | ≥8% | `MPC`, `PSX` | ✅ |
| Missile-defense / rearmament | 3 | 3.64% | — | `RTX` | ⚪ no bar set |

### 4a · 🚨 The rank-1 cycle's held epicenter is on the non-accumulating side of its own node

Carried from `M1309` and **unchanged because no new session exists**: `NVDA` **OBV −0.08 분산** ·
`ANET` **중립 with `vol_surge` 0.60** (its 🟢 tag *cannot* fire regardless of price) · `AVGO` **−0.45
분산 with rs20 −15.9** — while **storage/memory, which carries the board's two largest Δflows
(`STX` +0.73, `WDC` +0.72), is 0% of the book.** ⇒ **17.48% of "AI-compute epicenter" exposure sits
entirely in the half that is not accumulating.** ⚠ **Repeating this is not new evidence** — it is the
same measurement, and `S145` (09-11) is the row that tests it.

### 4b · ★★ The GAP the registry structurally cannot see

**The AI-power cycle is not in `cycle_registry.json` at all** (`M1308`), so its absence reads **✅
no-GAP** rather than as a gap. The lane is coherent and measurable across **three** GICS labels, its
money is in **generation** (`CEG` +0.64, `VST` +0.62, both 매집) and leaving **electrical equipment**
(`ETN` −0.66 🔴 · `PWR` −0.51 · `GEV` −0.19, four of five 분산), and **the book's only exposure to it
is `ETN` — the lane's single distributing name.**

⇒ **A registry that cannot see a cycle cannot flag a gap in it, so ✅ here means "not measured",
not "covered."** This is the third consecutive run recording it. ⚠ **Adding the cycle to the registry
is a human-approval item (P5)** — this stage does not edit the registry.

### 4c · ⚠ The rank-3 cycle now has a flow finding and no bar

`RTX` at **3.64%** sits under **"no bar set"**, so the GAP check is silent on it by construction —
**at the same moment Lens 1 finds its node at the 7.1st percentile of a year.** ⇒ **the one cycle
whose exposure the registry does not police is the one whose node just printed a one-year extreme.**
Filed as **`M1374`**. **`S150`** gives it the price observable it lacked.

### 4d · The cleanest epicenter expressions, named (P4 — identification, not a recommendation)

- **Rank-2 (Energy/refining)** — ✅ **correctly placed and this run confirms it on a third
  instrument**: `MPC`/`PSX` are the chain's highest-OBV names (+0.62 / +0.43) with `rs20` +30.8/+25.5,
  and both charts read **CONFIRMED-TURN** with OBV slopes +52%/+58%. ⚠ `PSX` carries a **bearish
  divergence** the sweep cannot see (Lens 3).
- **Rank-1 (AI-compute)** — the accumulating half is **storage/memory** (`STX`, `WDC`, `SNDK`, `MU`),
  **0% held**, and **structurally invisible to the 🟢 gate** (`vol_surge` 0.59–0.94 against a 1.2
  bar). `S145` settles **09-11**.
- **AI-power (unregistered)** — the accumulating node is **generation** (`CEG`, `VST`), both blocked
  from the shortlist by `vol_surge` alone and both filed to the missed ledger this run.

---

## §2 · Synthesis — what this pre-mortem changes

| item | change |
|---|---|
| **DEEP set** | ROTATION delivered **2 of 4** (continuous `ENRG`, `HLTH`; both rotating slots unfilled). ⇒ **PREMORTEM promotes ONE: `DEFENSE` (as an INDU sub-node)**, on Lens 1's 7.1st-percentile price extreme plus a held position. ★ **FINAL DEEP SET = `ENRG` · `HLTH` · `DEFENSE` (INDU sub-node) = 3 of 4.** ⚠ **The 4th slot stays UNFILLED and is not padded** — `IT` and `UTIL` were both deep-dived on 09-05 (0 runs ago) and both are already multiply bracketed; promoting a quadruple-bracketed leg is padding, and `M1371` (n=3 runs unable to fill N=4) is the measurement the protocol's budget line asks for |
| **Brackets → ALPHA's action bracket** | **`S148`** (09-14) · **`S149`** (09-11) · **`S150`** (09-14) — all three **registered in `handoff/SCENARIOS_US.md` AND indexed in the `SCENARIOS.md` spine INSIDE this stage**, both branches, frozen thresholds, `D93` executed before freezing, thresholds stated against the implied move |
| **Momentum re-tags → BET §B** | `SLB` **EARLY-NOT-EXTENDED** (the one BET candidate) · `MPC` **EXTENDED-BUT-LIVE** · `SNDK` **EXTENDED-BUT-LIVE** · `PSX`/`HOOD` **EXHAUSTION-WATCH** · `MSTR` **EXHAUSTED** · `NEM` **rejected by its own second instrument** |
| **Cycle GAP → BET's epicenter module** | **No registry GAP** — and §4b says why that ✅ is unreliable. The two real exposure findings are (i) the rank-1 epicenter's held half is the non-accumulating half, (ii) the rank-3 cycle has no bar at the moment its node hit a one-year extreme |
| **Digs registered** | **`D540`** (the calendar's earnings block fails silently) |
| **Facts filed** | `M1372` (`S135` averages a measured bucket with a mis-measured one) · `M1373` (`C25`'s US disagreement rate: 6 agree / 1 partial / 1 opposite of 8) · `M1374` (the unpoliced rank-3 cycle) |

---

## §3 · ⚠ Where the four lenses AGREED with the draft tilt — stated, because agreement is evidence too

The stage's default expectation is that at least one lens surfaces something the deterministic desk
missed. **Two did** (Lens 1's defense node, Lens 3's `MPC`/`PSX` divergence split). **Two largely
agreed**, and pretending otherwise would be manufacturing adversarialism:

- **Lens 2 agreed that `ENRG OW+` should stand today** — it registered the against-us branch
  (`S149`-B) rather than arguing for a demotion, because ROTATION's rule and the absence of a new
  session both bar acting on it. **The lens's contribution is the bracket, not a reversal.**
- **Lens 4 found no new GAP** — its two findings (`M1308`'s unregistered lane, `M1309`'s
  non-accumulating held half) are both **carried, not new**, because there is no new session to move
  them. **Re-stating them is not evidence and this section says so.**

---

## ✅ EXIT CHECK — PREMORTEM

- [x] **4 lenses executed, each returning named tickers and dated catalysts.** ⚠⚠ **NOT as a parallel
      agent fan-out — in-context and serially, 10th consecutive run, declared in §0a with the
      mitigation actually applied** (every verdict rests on a number pulled this run).
- [x] **Every bracket names its observable + frozen threshold + date, both branches, and is
      registered in `handoff/SCENARIOS_US.md` AND indexed in the `SCENARIOS.md` spine** — done
      **inside this stage** (verified: `S148`/`S149`/`S150` present in both files). **Zero one-way
      brackets.**
- [x] **Every magnitude threshold stated against the implied move.** `S148`: `ORCL` ±11.8% / `ADBE`
      ±8.1% vs the observable's p85/p15 of +3.15/−3.66 ⇒ the 1-session magnitude bracket is
      **pre-declared NO-INFORMATION and NOT registered**. `S149`: `XLE`'s straddle **expires before
      the row settles** ⇒ thresholds from `D93`, stated. `S150`: p85/p15 sit **outside** a
      diversified 5-name basket move.
- [x] **Each branch graded by information content** (`B4`): `S148` A informative / B near · `S149`
      **B is the against-us and informative branch** / A near-pre-fired on level · `S150` **B carries
      little information (state already below it), A and C carry it**. **Five binaries dropped with
      the reason written out** (§2c).
- [x] **`BLINDSPOT_PREMORTEM.md` written** — legs (§Lens 1) · brackets (§Lens 2) · re-tags (§Lens 3)
      · cycle GAP (§Lens 4).
- [x] **Every catalyst-bearing leg promoted or logged**: `DEFENSE` **promoted**, `UTIL`/AI-power
      **logged WITHIN-RUN-WATCH with the reason it was not promoted**, `RE` and `COMM` **logged with
      the number that stopped them**. Brackets handed to ALPHA; GAP findings handed to BET.
- [x] **DEEP set updated and stated: `ENRG` · `HLTH` · `DEFENSE` (INDU sub-node) = 3 of 4, 4th
      deliberately unfilled and not padded.**

---

## 📋 Stage run log — open decisions resolved without a human

1. **Parallel agent fan-out vs in-context serial** — resolved as **in-context serial**, matching the
   documented practice of the last 9 runs, **declared as a weakness in §0a** rather than omitted.
2. **Whether to promote a 4th DEEP to reach N=4** — resolved as **no**. `IT` and `UTIL` were both
   deep-dived 0 runs ago and carry 4+ dated rows each; padding to hit a budget is the failure the
   budget line exists to prevent. `M1371` (n=3) is the measurement instead.
3. **Whether to bracket the `ORCL`/`ADBE` magnitude** — resolved as **no, with the measured
   precedent** (`S132`/`S138` both fired C on the same realization at ±9 and ±11 bands). The bracket
   was **spent on `S148`**, which measures the leg spread the prints bear on.
4. **Whether a US desk can discharge the KR desk's 09-10 quad-witching request** — resolved as **no**
   (`W1`), and **`D533` is left OPEN and named** rather than closed with a token row.
5. **Whether Lens 3's `NEM` disagreement should retighten the missed-ledger `--enters-if`** —
   resolved as **no** (`D242`): the condition was written at EVENT_ALPHA and stands; the
   contradiction is attached as context.
