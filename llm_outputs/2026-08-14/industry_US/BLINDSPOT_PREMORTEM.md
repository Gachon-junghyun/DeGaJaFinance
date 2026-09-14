# BLINDSPOT_PREMORTEM — industry_US · 2026-08-14 · Stage 7/11 (L1·PREMORTEM) ★US-only

> Four adversarial lenses argue **AGAINST our own tilt** before the deep budget is committed.
> Analytical only, zero buy/sell (P4). Draft tilt and DEEP picks are inherited from
> `SECTOR_ROTATION.md` and are the *target*, not the premise.

## §0 · ⚠ Execution mode, stated first because it is this stage's weakness

**The four lenses were executed IN-CONTEXT, not as a parallel adversarial agent fan-out.** The L1
specifies an Agent fan-out; this session's operating constraints forbid spawning subagents unless
explicitly requested, so the documented in-context path was used (the same deviation the 08-03 and
08-04 runs logged as their own honest weakness). ⇒ **the independence of the four lenses is weaker
than the protocol intends**, and any place where they agree should be discounted accordingly.
**Where they disagree with the draft — and three of four do — that disagreement is still real,
because it is carried by numbers rather than by rhetoric.**

## §0b · 🚨 An ID collision this stage caught in its OWN run, recorded not edited away

Doing the mandated write-time 3-grep against `RESEARCH.md` revealed that **`D242`–`D256` were already
taken by the 2026-08-13 `industry_US` run.** This run's HANDOVER §7, MACRO §I, SWEEP §2 and
EVENT_ALPHA §0 had allocated **D254 · D255 · D256 · D257 · D258 · D259** — **six colliding IDs.**
Renumbered to **`D257`–`D262`** across all four files. **This is the `D137` class, and it happened
because HANDOVER §4c read the highest D from a `STANDING_VIEW` mention (`D253`) instead of opening
`RESEARCH.md`** — the exact correction the 08-12 RUN-2 had to make in place.

★★ **And the collision surfaced something worse than a numbering clash.** The pre-existing **`D256`**
already says: *"the news failures are per-query **COST**, not availability… the sweep issues 300
SEQUENTIAL `news_velocity` calls — a client-side timeout under server load produces exactly a partial
failure like 17.0% coverage."* ⇒ **this run's MACRO §0 re-derived an "availability window" diagnosis
that a prior run had already SUPERSEDED with a better one.**
- **What survives**: the timestamps are new and real (5/5 fail at 22:15 → 3/3 succeed at
  22:34:57 / 22:44:59 / 22:55:00, identical counts of 3,835).
- **What is withdrawn**: the claim that "availability window" is the *diagnosis*. `URLError` at 22:15
  is a connection failure, not a timeout, so **neither D256's cost story nor this run's availability
  story explains both observations** — and saying so is more honest than picking one.
- **`D259` is therefore re-scoped**: it is not a new diagnosis, it is the **operational rule** —
  *G1 must probe ≥3 times spaced ≥10 minutes, cheap AND expensive queries, before revoking anything.*

---

## §1 · LENS 1 — UNDER-COMPUTED LEGS

**Question**: what did we not deep-dive that has a catalyst inside ~5 trading days?
Not deep-dived this run: **IT · HLTH · MATR · DISC · UTIL · STPL · RE**.
Catalysts inside the window: **08-19** (`S75` ENRG · `S76` HLTH · `S77` MATR · `S78` FIN · `S80`
UTIL/RE/STPL) · **08-20** (`S82` HLTH · `S83` ANET/HPE).

### 1a · ★★★ The strongest bull case the desk did not compute: the optical / interconnect layer

| | Measured |
|---|---|
| `COHR` | **`flow_score` +1.000 — the maximum on the 300-name board** · OBV 매집 +0.27 · RS20 **+14.5** · `vol_surge` **1.77** · ✅ **3-axis-admissible green** |
| `LITE` | flow +0.844 · OBV 매집 +0.28 · RS20 **+21.0** · `vol_surge` 1.32 · ✅ **admissible green** |
| `CIEN` | flow +0.273 · RS20 +10.3 · **Δflow +0.622 = 2nd largest on the entire board** |
| **RS60, all three** | **−15.1 · −5.8 · −20.9 — all NEGATIVE** |

★ **Two of the desk's SIX admissible greens are in this layer, and the desk has no position, no DEEP
slot and no sector tilt that contains it** (they sit inside IT, whose promotion was argued on
`eqflow`, not on these names). **RS20 strongly positive against RS60 strongly negative is a turn
inside a drawdown — the early shape, not the crowded one.**
⚠ **The adversarial half, which the bull case must survive**: `COHR` carries **5.4% of float short and
BUILDING** (DTC 1.9) with an implied move of **±3.8%** — the layer is not un-contested. And **`GLW`,
whose thread was the week's cleanest precursor, is 🔴 distributing on both windows** (EVENT_ALPHA
Card 4), i.e. the layer is **not** uniformly accumulating.
**Verdict: WITHIN-RUN-WATCH, escalated to a registered bracket (`S86`)** rather than PROMOTE-TO-DEEP —
the DEEP budget is N=4 and both rotating slots are already recency-starved deviations. **`S48` (→09-30)
is the desk's standing bracket on this layer; `S86` gives it a dated 5-session leg.**

### 1b · The memory-supplier leg, which the IT promotion does NOT actually contain
`MU` **Δflow +0.585** · `SNDK` **+0.757** · `WDC` **+0.510` — **the three largest positive deltas on
the board**, all inside IT, none 🟢, none in the shortlist, none deep-dived. ⇒ IT was promoted to N+
on `eqflow`, and **this is where the `eqflow` came from.**
**Verdict: WITHIN-RUN-WATCH.** Already carried by EVENT_ALPHA Card 1 with a dated kill (08-21).

### 1c · What Lens 1 declines to promote, with the reason
**HLTH** has two brackets settling inside the window (`S76` 08-19, `S82` 08-20) and `S82` is **already
above its branch A at +3.091**. **Adding a DEEP slot to a question that settles on a frozen observable
in three trading days spends budget to pre-empt an answer.** Declined.

---

## §2 · LENS 2 — REGIME-FLIP / BOTH-SIDES (the MANDATORY binary)

`CATALYST_WATCH.json` carries **one 🔀 binary: "Iran 'Strait of Hormuz open' statement (TACO trigger)",
axis oil, UNDATED.** The protocol makes a both-sides bracket mandatory.

### 2a · The against-us branch, spelled out
If Hormuz reopens: crude collapses → the **crack compresses** → **ENRG (our OW−) is hit on its only
positive `wflow`**; simultaneously **hike bets are pared further** (P57's measured coupling —
*"Traders Pare Bets on Fed Rate Hike This Year **as Oil Prices Fall**"* [`bloomberg` 08-13]) → the
long end rallies → **UTIL (UW) · RE (UW) · STPL (UW−) all rip together**, and **IT (N+) rips too**.
⇒ **one headline hits our single OW-side conviction and four of our underweights at once.** That is
the correlated-tilt pattern the field note warns about, and **nothing in the current bracket set
measures the SPREAD between the two sides** — `S80` measures the duration basket alone, `S75` measures
Energy alone.

### 2b · ★ The measurement that makes this urgent
`[XLE 5-session excess vs SPY] − [EW{XLU,XLRE} 5-session excess vs SPY]`, trailing 252:
**mean +0.634 · sd 3.474 · p15 −3.174 · p85 +3.899 · p95 +5.544.**
**STATE = +3.880 — i.e. the war-premium-vs-duration spread is sitting essentially AT its own 252-day
85th percentile.** ⇒ **the premium is already maximally expressed in the relative tape.** A
reopening does not have to be *bad* for Energy to hurt; it only has to be *less good*.
⇒ **`S84` registered** (§5).

### 2c · The second against-us branch nobody has bracketed: the hike actually arrives
`rate hike` **2.79× accelerating** with **Hammack backing an increase** and `UNRATE` at **4.1%** on
three consecutive falls (MACRO §A-3). If the Fed hikes, the **front end** sells off — and this run's
whole P56 read is that the move has been **long-end only** (`DGS2` unchanged at 4.20 while `DGS30`
+16bp). **A front-end selloff falsifies P56's term-premium reading and simultaneously kills the IT N+
promotion** (a discount-rate *level* event, not a *path* event).
⚠ **B4 — information content, graded BEFORE the event**: this branch **can falsify two live calls at
once**, so it is worth a bracket. Covered inside `S85`'s branch A rather than given its own row,
because the observable (equal-weight vs cap-weight tech) responds to exactly that mechanism.

---

## §3 · LENS 3 — MOMENTUM-CONTINUATION ("already ran" ≠ avoid)

Re-tagging every runner on the board, with the flip condition rather than a feeling:

| Name | Run | Re-tag | Flip condition |
|---|---|---|---|
| **`DELL`** | **RS60 +102.4** · RS20 +22.7 · Δflow **+0.289** · OBV 매집 | **EXTENDED-BUT-LIVE** | Δflow turns negative **or** RS20 < +10 |
| **`HPE`** *(held)* | **RS60 +76.0** · RS20 **+28.9** · **OBV +0.48 = the strongest accumulation in the book** | **EXTENDED-BUT-LIVE** | OBV state leaves 매집 **or** `S83` fires branch B (ANET−HPE ≤ −9.68, 08-20) |
| **`ANET`** *(held)* | RS60 +38.4 · RS20 +17.2 · OBV +0.36 · **Δflow +0.005 = flat** | ⚠ **EXTENDED, DECELERATING** | the Δ is the tell — flat while the price leads |
| **`MU`** | RS60 +34.1 · RS20 +7.7 · **Δflow +0.585** | **EXTENDED-BUT-LIVE — the cycle KPI is still accelerating** (the pass-through is arriving at retail, Card 1) | `MU` FY revision breadth turns net-down |
| **`MPC`** *(held)* | RS60 +32.0 · RS20 +12.9 · the book's **only admissible 🟢** | **EXTENDED-BUT-LIVE** | crack falls ≥5 points while crude holds ±3% (P58 anti-signal b) |
| **`NEM`** | **exc20 +22.101** · exc5 +7.096 | ⚠ **EXTENDED — and it IS the sector** (ex-NEM EW exc5 −1.893, 1 of 12 positive) | `S77`, 08-19 |
| **`NVDA`** *(held)* | RS20 +5.0 · **RS60 −4.0** | 🚨 **NOT a runner — this is the desk's assumption, and it is false.** `NVDA` is **negative on 60 days** while `MRVL` is **+26.2** | — |

### 3a · ★ The measurement Lens 3 forces
`EW{DELL, HPE} 5-session excess vs SPY`, trailing 252: **mean +2.248 · sd 8.429 · p15 −4.961 ·
p85 +7.734 · p95 +16.143. STATE = +12.331 — between p85 and p95.**
⇒ **the two biggest runners in and around the book are at roughly the 90th percentile of their own
5-session distribution.** That is not "avoid"; it is a **measured position in the distribution** that
the desk has never written down. ⇒ **`S87` registered** (§5).

---

## §4 · LENS 4 — CYCLE-EXPOSURE

`cycle_exposure.py` returns ✅ **no GAP**: AI-compute **16.68%** vs a 12.0% floor (`AVGO·NVDA·ANET`),
Energy **11.1%** vs 8.0% (`MPC·PSX`), missile-defense **5.7%** (`RTX`).
**Lens 4's job is to attack that ✅, and there is a lot to attack:**

1. **The ✅ is computed on 2 armed tests, not 3.** Rank-3's floor is **`0.0`** ⇒ that check is
   **silently OFF** (pre-existing `D250`).
2. **`R66` unchanged**: **`HPE` is not in the epicentre registry**, so 16.68% is understated by an
   unknown amount, and **four holdings — `HPE` · `MET` · `NDAQ` · `NUE` — map to NO registered cycle
   at all.** The ✅ covers part of the book.
3. **The registry is 28 days old** and its `core_pick_why` for PSX **still quotes `R8`, a retracted
   claim** (pre-existing `D250`).
4. ★★★ **The registry has no entry for the two cycles this run actually found.** **Optical/
   interconnect** (§1a — 2 of 6 admissible greens) and **custom AI silicon / Maia 300** (EVENT_ALPHA
   Card 2 — a named product, a September date, a 300,000-unit target) are **not cycles in the
   registry**, so `cycle_exposure` **cannot report a GAP against either.** ⇒ **the ✅ means "no gap
   against the cycles we wrote down in July", not "no gap".**
5. ★★ **And inside the one cycle it does track, the book is long BOTH SIDES of an active
   displacement**: `NVDA` (merchant GPU, **RS60 −4.0**) and `AVGO` (custom ASIC, Δflow **+0.300**)
   with `MRVL` (**RS60 +26.2**, the named Maia beneficiary) **not held.** ⇒ **the epicentre percentage
   is satisfied while the epicentre's internal composition is moving against the held half.**
   `S81` (→08-27) brackets the correlation; **nothing brackets the composition.**

---

## §5 · Brackets registered — every one with BOTH branches, a frozen observable, and a date

> **ID 3-grep at WRITE time (D137/D76)** across all seven files (`SCENARIOS*.md` ×3,
> `STANDING_VIEW*.md` ×3, `RESEARCH.md`): `S84` `S85` `S86` `S87` returned **0 hits in all seven**;
> highest existing **S83 (US) / S61-KR (KR)** ⇒ this run takes **S84 – S87**.
> **Every band is measured on a trailing-252 distribution of the estimator itself (D93), before freezing.**

> ⚠⚠ **Implied-move disclosure, and it is a LIMIT rather than a check.** `module_flow --positioning`
> returns `XLU ±0.7% · XLE ±1.9% · NVDA ±1.2% · COHR ±3.8% · MU ±2.3%` — **every one at expiry
> 2026-08-14, `D0`.** A **D0 straddle prices the remainder of today**, not a 5-session window, so it
> is a **FLOOR on the multi-day implied move, not an estimate of it.** ⇒ **no threshold below is
> claimed to sit "outside the implied move"** — the desk does not have the instrument to say so today.
> Stated rather than smuggled, per the L1's own `D±n` rule.

### S84 — ★★★ The mandatory Hormuz both-sides bracket: the SPREAD no existing row measures · → settle **2026-08-21**

**Frozen observable**: `[XLE 5-session excess vs SPY] − [EW{XLU, XLRE} 5-session excess vs SPY]`,
settled daily closes, `yfinance`, `auto_adjust=False`, benchmark **`SPY` named inline (C1)**.
**State at registration (2026-08-13 settled): +3.880.**

| Branch | Threshold at the 2026-08-21 settle | Meaning |
|---|---|---|
| **A (AGAINST US — one headline hits five tilts)** | **≤ −3.174** (measured p15) | Hormuz de-escalates ⇒ ENRG's only positive `wflow` compresses **while** the duration underweights rip. **Falsifies the ENRG OW− and the UTIL/RE UW simultaneously**, and confirms P57's oil→hike-odds coupling as the dominant channel |
| **B (with us)** | **≥ +5.544** (measured p95) | Escalation ⇒ the premium extends beyond an already-85th-percentile state |
| **C** | between | Modal. No conclusion changes |

- **D93, executed before freezing**: trailing-252 mean **+0.634** · sd **3.474** · p15 **−3.174** ·
  p85 **+3.899** · p95 **+5.544**. **Base rates: A 15.1% · B 5.2% · C ~80%.**
- ★ **Branch B is deliberately set at p95 rather than p85, and the reason is disclosed**: the state
  **+3.880** is already **at p85 (+3.899)**, so a p85 branch would fire on **no move at all** — the
  `D122` zero-information class. **The asymmetry (15.1% vs 5.2%) is stated, not hidden.**
- **Information content (L3): HIGH and asymmetric.** **A falsifies two live tilts at once**; B only
  confirms. Registered because A is the branch the desk has no other instrument for.
- **Settlement mode, stated explicitly (`D242`'s remedy, first application on this desk)**: **BOTH
  branches settle on the TERMINAL bar (2026-08-21) only.** Neither is an `ANY`-bar branch.
- **Anti-signal**: if a **non-Hormuz** energy event dominates the window (an OPEC emergency meeting, a
  US SPR action) evidenced by a filing or two independent outlets ⇒ **`AMBIGUOUS`**, not scored.
- **Owner**: `industry_US`.

### S85 — ★★★ The falsifier for THIS RUN'S OWN IT promotion, on the axis the promotion used · → settle **2026-08-21**

**Why it exists.** ROTATION promoted **IT N → N+ today** on one argument: *`eqflow` flipped positive
(−0.100 → +0.034), so the median IT name turned.* **Nothing tests that claim** — `P52`'s anti-signal
uses `XLK`, which is **cap-weighted and therefore cannot distinguish the median name from `NVDA`.**

**Frozen observable**: `RSPT` (equal-weight technology) **5-session return minus `XLK`
(cap-weighted technology) 5-session return**, in percentage points, settled closes.
**This is a direct test of the promotion's own logic**: if the median name really turned, equal-weight
must beat cap-weight. **State at registration (2026-08-13): +1.980.**

| Branch | Threshold at the 2026-08-21 settle | Meaning |
|---|---|---|
| **A (AGAINST US)** | **≤ −0.994** (measured p15) | Cap-weight reasserts ⇒ **the IT N+ was a megacap artifact and the `eqflow` flip was one session of noise.** Also the branch a **front-end rate shock** (Lens 2c) would produce |
| **B (with us)** | **≥ +2.046** (measured p95) | Breadth extends beyond an already-extreme state ⇒ the promotion was early and right |
| **C** | between | No conclusion changes |

- **D93**: trailing-252 mean **+0.226** · sd **1.221** · p15 **−0.994** · p85 **+1.446** · p95 **+2.046**.
  Base rates **A 15.1% · B 5.2%**.
- 🚨 **Disclosed at registration, and it is uncomfortable**: **STATE +1.980 is ALREADY ABOVE p85
  (+1.446).** ⇒ **the IT promotion was made at the 85th–95th percentile of the very estimator that
  justifies it.** Branch B is therefore set at p95 and is **near-degenerate**; **branch A is the
  informative one**, which is the correct shape for a falsifier of our own call.
- **Information content (L3): HIGH on branch A** — it kills a tilt this run created.
- **Settlement mode**: **TERMINAL bar only**, both branches.
- **Anti-signal**: an `RSPT` or `XLK` index reconstitution inside the window ⇒ **`VOID`**.
- **Owner**: `industry_US`.

### S86 — ★★ The optical/interconnect layer: the desk's own maximum flow score, with zero exposure · → settle **2026-08-21**

**Frozen observable**: `EW{COHR, LITE, CIEN} 5-session excess vs SPY`, settled closes.
**State at registration (2026-08-13): +2.997.**

| Branch | Threshold at the 2026-08-21 settle | Meaning |
|---|---|---|
| **A (the layer is a real new leg)** | **≥ +12.584** (measured p85) | The turn extends ⇒ a genuine un-owned leg of the AI build-out, and the **cycle registry has no entry for it** (Lens 4.4) |
| **B (it was a bounce in a downtrend)** | **≤ −5.948** (measured p15) | RS60 (−15.1 / −5.8 / −20.9) was the honest window and RS20 was noise |
| **C** | between | No conclusion changes |

- **D93**: mean **+3.276** · **sd 8.998 — the widest estimator registered on this board today, and it
  is disclosed** ⇒ **C is the heavy favourite** (base rates A 15.1% · B 15.1% · C ~70%).
- **Registered anyway** because the desk has **two of its six admissible greens here and no position,
  no tilt and no registry entry** — an un-measured exposure is worth a dated observation even at a
  low fire rate.
- ⚠ **Adversarial note carried into the row**: `COHR` short interest is **5.4% of float and BUILDING**
  (DTC 1.9). **Crowded-short is turn-conditional squeeze fuel, never a buy signal on its own (D6).**
- **Settlement mode**: **TERMINAL bar only.**
- **Owner**: `industry_US`.

### S87 — ★★ Are the book's biggest runners EXTENDED-BUT-LIVE or EXHAUSTED? · → settle **2026-08-21**

**Frozen observable**: `EW{DELL, HPE} 5-session excess vs SPY`, settled closes.
**State at registration (2026-08-13): +12.331.**

| Branch | Threshold at the 2026-08-21 settle | Meaning |
|---|---|---|
| **A (EXHAUSTED)** | **≤ −4.961** (measured p15) | The 90th-percentile state mean-reverted ⇒ Lens 3's EXTENDED-BUT-LIVE tag was wrong and *"the cycle KPI is still accelerating"* is not a defence |
| **B (EXTENDED-BUT-LIVE, confirmed)** | **≥ +16.143** (measured p95) | The runners extend from an already-extreme state |
| **C** | between | No conclusion changes |

- **D93**: mean **+2.248** · sd **8.429** · p15 **−4.961** · p85 **+7.734** · p95 **+16.143**.
  Base rates **A 15.1% · B 5.2%**.
- **Disclosed**: STATE **+12.331 sits between p85 and p95**, so branch B again requires extension from
  an extreme and **branch A is the informative one.**
- ⚠ **`HPE` is also an `S83` object** (ANET−HPE, settles 08-20). **The observables are different and
  NEITHER row is re-frozen** — if they disagree, **the disagreement is the finding** (the S14-ANNEX /
  S35-ANNEX precedent).
- **Settlement mode**: **TERMINAL bar only.**
- **Owner**: `industry_US`.

---

## §6 · What this stage changes, and what it declines to change

| | |
|---|---|
| **No 5th DEEP slot promoted** | Lens 1's strongest leg (optical) is escalated to a **dated bracket** instead. The DEEP budget is N=4 and **both rotating slots are already declared recency-starved deviations** — adding a fifth would spend budget the board cannot justify |
| **No tilt changed by this stage** | Three lenses disagree with the draft, and **all three disagreements are now dated observables (`S84` `S85` `S86`) rather than notches.** A pre-mortem that moves the tilt it was asked to attack has become a second rotation stage |
| **★ The one call this stage does make** | 🚨 **`NVDA` is not a runner and the desk has been treating it as one.** RS60 **−4.0** against `MRVL` **+26.2**, its 🟢 is **disqualified** (`SWEEP_READ §2` / `D261`), and its customer has a **named, dated, unit-counted substitute** (Maia 300, September, 300k units). **This is stated as a measurement, not a position change (P4)** |
| **Handed to ALPHA** | `S84`'s both-sides bracket → the action-bracket module. The **undated** binary means the bracket has a settle date but the *event* does not — ALPHA must carry both |
| **Handed to BET** | Nothing new. EVENT_ALPHA's CONFIRMED-EARLY list (`MU` `SNDK` `WDC` `MRVL` `VLO` `COHR` `LITE`) stands unchanged; this stage adds **`MRVL`'s adversarial context** (it is the beneficiary of a displacement that hits a held name) |

## ✅ EXIT CHECK

- [x] **4 lenses executed**, each returning named tickers and dated catalysts.
      ⚠ **In-context rather than a parallel agent fan-out — declared in §0 as this stage's weakness**,
      not omitted.
- [x] **Every bracket names its observable + frozen threshold + date, with BOTH branches.**
      `S84` `S85` `S86` `S87` — **no one-way brackets.** Registration into
      `handoff/SCENARIOS_US.md` + the `SCENARIOS.md` MASTER INDEX is performed at run-end writeback.
- [x] **The ≤48h/undated binary has a both-sides bracket** (`S84`), and it measures the **spread**
      that the existing rows (`S75` Energy-only, `S80` duration-only) cannot.
- [x] **Every magnitude threshold stated against the implied move** — and the implied moves are
      **all `D0`**, so they are declared a **floor, not a check**, and **no threshold is claimed to
      sit outside what is priced.**
- [x] **Branch information content graded BEFORE the event** (B4): `S84`-A and `S85`-A are the
      falsifying branches; `S85`-B and `S87`-B are declared **near-degenerate** because the state is
      already past p85, with base rates printed.
- [x] **Settlement mode (`ANY` vs `TERMINAL`) stated explicitly on all four rows** — the first
      application of `D242`'s remedy on this desk.
- [x] **Date-clustered moves treated as n≈1** — Lens 3 normalises every runner against its own
      trailing-252 distribution rather than calling a level "exceptional".
- [x] **Under-computed legs are PROMOTED or logged, never silently dropped** (§1a → `S86`;
      §1b → EVENT_ALPHA Card 1's 08-21 kill; §1c → declined **with a reason**).
- [x] **Cycle-GAP audited adversarially**: the ✅ is shown to rest on **2 armed tests of 3**, over
      **82% of the book**, against a **28-day-old registry with no entry for either cycle this run
      found**.
