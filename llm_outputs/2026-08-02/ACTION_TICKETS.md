# ACTION_BRACKET — 2026-08-02  (conditional DRY-RUN tickets · human pulls the trigger)

> Weaves CYCLE_EXPOSURE (gap→core) + CATALYST_WATCH (binary→both-sides) + risk model + live KIS.
> Book total ≈ 14,795,803원 · fx 1441 · per-trade risk 1.5% (core 0.8%) · stop 7.0% · maxpos 25.0%
> ⚠️ DRY-RUN — sizes are illustrative; execution is a separate human `module_kis --order ... --execute`. US = USD limit only.

**Nearest binary:** AMD earnings (D-2, axis=earnings) — both-sides armed below.

### CORE-STARTER (tape-independent) — PSX  (BUY)
- **condition:** establish NOW regardless of tape — closes Energy / oil-refining (Hormuz + Russia crack) epicenter GAP (6.9% < 8.0%)
- **size:** 5 sh @ ~$211.68 (≈$1,058.4 notional, risk $82.14 = 0.8% )
- **stop:** $196.86 (−7.0%) · exch NYSE
- **why core:** cheapest large refiner on forward (11.2, PEG 1.17) + the only Energy name with shorts actively exiting (FINRA short-vol z -1.43, 5v5 -16.6▼) = clean structural entry, not an extended one (cf. MPC RSI 85.7). Crack-spread leverage, not crude beta. Human-locked 2026-07-17; evidence: llm_outputs/2026-07-17/industry_US/SECTOR_DEEP_ENRG.md

*Analytical/scheduling artifact — zero buy/sell advice. Tickets are pre-committed conditionals; no order is sent by this script.*
---

# ADDENDUM — appended 2026-08-02 by the `industry_US` ALPHA stage (append-only; the script's block above is NOT edited)

## ⚠⚠ 0 · D19 fires for an EIGHTH consecutive run, and this time BOTH of its frozen clauses are measurably FALSE

The script's `why core` string above is a **frozen literal** and it now contradicts this run's own
measurements on two independent axes:

| Frozen clause printed above | Measured 2026-07-31 / 2026-08-02 | Status |
|---|---|---|
| *"the only Energy name with **shorts actively exiting** (FINRA short-vol z **−1.43**, 5v5 **−16.6▼**)"* | **PSX FINRA short-vol z = +1.53 — a 🔴 short SURGE, and the ONLY one on this desk's entire pull.** The sign is inverted, not merely stale. Corroborated by its option book: **P/C 1.25, the only fear/hedging profile on the sheet** | ⛔ **FALSE, opposite sign** |
| *"cheapest large refiner on forward (11.2, PEG 1.17)"* | This is **R8's retracted rationale**, still printing 8 runs after the retraction. On today's numbers the three are **PSX 11.15× · MPC 11.40× · VLO 11.56×** — within 0.4× of each other, so **the multiple does not discriminate at all**; and on the axis that does, **PSX's gross margin sits ≈55th percentile of its own 10-year history against MPC's ≈37th (i.e. MPC is further BELOW its own median)** | ⛔ **RETRACTED (R8) and non-discriminating** |

★ **And the header says *"Nearest binary: AMD earnings (D-2) — both-sides armed below"* while
emitting NO both-sides ticket at all.** That is D19's original 2026-07-22 description
(*"announces a bracket it never emits"*) reproducing unchanged. **`core_pick` is a HUMAN-LOCKED
registry field and was NOT modified by this run (P5) — the correction is recorded here instead.**

⇒ **Reading instruction for anyone acting on the block above: the CORE-STARTER's stated REASON is
dead on both clauses. The GAP it addresses is real (rank-2 Energy epicenter 6.9% vs an 8.0% floor,
−1.10pp); the rationale attached to PSX specifically is not.** See §2 for the two expressions this
run measured as the cleanest, neither of which is PSX.

## 1 · Both-sides brackets the script did not emit — the ≤48h binaries, armed both ways

**Protocol rule: a one-way tilt into a known binary is a violation.** Three binaries sit ≤48h out
(**AMD · ANET · MPC, all 2026-08-04**) plus a live geopolitical conditional. All are armed both ways
below. **These are pre-committed CONDITIONALS for a human, not orders; nothing is sent (P4/P5).**

### ① MPC — 2026-08-04 · bracket **S53** (registered by this run's PREMORTEM; MPC had owned no bracket)
- **Implied move ±8.8%, expiry 2026-08-21 (D19) — COVERS the print ⇒ usable.** ⚠ **Any move inside
  ±8.8% is pre-declared NO-INFORMATION and may not be read as confirmation.**
- **Side A (guide confirms crack capture)** → S53 branch A, **confirmatory only**; changes no desk
  conclusion. **No ticket is warranted for a confirmatory branch** — stated rather than manufactured.
- **Side B (guide flags margin compression / hedging-timing lag / turnaround drag)** → S53 branch B.
  **Reads across to VLO and PSX (one risk unit, SPY-residual ρ +0.878) and to the ENRG OW itself.**
  **Invalidation of the read-across: S49 branch B firing first** (the distillate 5-session change
  ≤ −5.0), in which case S49 owns the outcome and this is a footnote.

### ② PSX — 2026-08-05
- **Implied move ±5.3%, expiry 2026-08-07 (D5) — COVERS the print ⇒ usable.** Inside ±5.3% = no
  information.
- ⚠⚠ **This is the name the script's CORE-STARTER points at, and it is the name where all three
  measurable axes currently disagree with that ticket**: **A-grade** — days 21-60 = **−5.5**, re-tagged
  **EXHAUSTED** by PREMORTEM; **B-grade** — **FINRA z +1.53 short surge**; **options** — **P/C 1.25**,
  the only fear profile on the board. **Three axes, one direction, against the ticket's stated reason.**

### ③ AMD — 2026-08-04 · bracket **S50** (direction-only, by design)
- ⚠ **Implied move ±4.0%, expiry 2026-08-03 (D1) — EXPIRES BEFORE the print ⇒ NO usable magnitude
  threshold exists and none is fabricated.** S50 is scored on guide direction only.
- **Both sides**: a capex/AI-guide **CUT** is the branch that changes a conclusion (it breaks both the
  volume and the price leg of the memory thesis — STANDING_VIEW §4); a **RAISE** confirms volume only
  and **cannot un-measure the contract-price series**, because the same buyers signed the price caps.
  ⇒ **asymmetric: only the cut branch is worth a ticket.**

### ④ ANET — 2026-08-04
- ★ **NEW this run: ANET's straddle is ±11.3%, expiry 2026-08-07 (D5) — it now COVERS its print**,
  which was **not true when S50 was registered on 07-31** (*"no options instrument covers this"*).
  **Recorded as an annex candidate for S50; S50 is NOT re-frozen here.**
- ANET carries **RS20 +12.4 / RS60 +2.7 vs SPY with delta +1.093** (the board's 4th-largest) — and
  **days 21-60 = −9.7, i.e. EXHAUSTED on the desk's own test.**

### ⑤ Iran — undated conditional, fired 2026-08-02 · bracket **S52** (registered this run)
- ⚠ **No options instrument prices a Truth Social conditional — no magnitude threshold exists and
  none is invented.** Scored on **primary text**, never on price.
- **Side A (a DATED Strait reopening in a primary text)** → the war premium gets an exit; **rips
  against** OXY (+16.4 / −7.0) · COP (+14.7 / −5.5) · CVX (+16.0 / −1.0) · XOM (+13.1 / −2.9) — the
  four with the most 20-vs-60 premium to give back.
- **Side B (a strike on NAMED Iranian energy infrastructure)** → supply shock the other way; **rips
  against** the fuel-cost leg — UAL (−9.3 / +26.3, 🔴 −0.850) · DAL (−6.0 / +20.2, 🔴 −0.674) ·
  CAT (−15.7 / −13.1, 🔴 −0.589) · UNP (+3.2 / +7.4, +0.436). ⚠⚠ **The M91 premise behind that leg
  was WEAKENED this run — DEEP-INDU re-tested it on UNP's FY2025 10-K and fuel-surcharge revenue
  DECLINED $218M against 1–2% total growth. Quote the mechanism, not the "8 of 12 points" magnitude.**

## 2 · The cycle GAP, re-stated with the expressions this run actually measured

**`cycle_exposure`: rank-2 Energy / oil-refining epicenter 6.9% vs an 8.0% floor = −1.10pp GAP.**
The standing rule holds — **a crowded or 🔴 tape gates ADD timing; it never justifies zero core in a
top-rank cycle.**

**The two cleanest un-held epicenter expressions, named with numbers and explicitly NOT recommended:**
- **XOM — flow +0.606, the highest of ANY Energy epicenter name held or unheld** (RS20 +13.1 /
  RS60 −2.9). ⚠ **NO-BASE (days 21-60 −16.0)**, and ★ **this run's DEEP-ENRG measured its registry
  "0% refining" tag to be WRONG** — XOM's Energy Products segment printed **$4.1–5.5bn, a four-year
  high**, comparable to or above CVX's $4.9bn. **The GAP arithmetic itself rests on a wrong tag.**
- **VLO — RS60 +20.2, the best 60-day in the refining group and the only refiner with a positive
  delta (+0.054).** ⚠ **L2 structurally unrunnable for a 6th run (D56) ⇒ no cheapness claim.**
- **Both are blocked from 🟢 by `vol_surge` ALONE (0.89 / 0.80 against a 1.20 gate), not by weak RS.**

⚠⚠ **Three facts are handed forward TOGETHER, because separating them would flatter the GAP**:
(i) the registry says the book is under-exposed to the engine; (ii) **the engine's own commodity rate
has turned — the 3-2-1's 5-session rate is already NEGATIVE (+4.995 → +0.822 → −4.439) and S49's
distillate line is one to two sessions away**; (iii) **both of the cleanest expressions are NO-BASE
or unvaluable on the desk's own tests.**

## 3 · Ticket discipline

**No ticket in this addendum carries a size, a share count or a stop.** The script's block above does,
and those are the script's own illustrative DRY-RUN numbers under a human-locked field. **This desk
produces analysis; a human executes separately, and no order is sent by anything in this run (P4/P5).**
