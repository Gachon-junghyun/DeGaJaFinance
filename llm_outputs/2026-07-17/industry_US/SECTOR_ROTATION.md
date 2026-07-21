# SECTOR_ROTATION — industry_US · 2026-07-17 (Fri)

> Stage 3 / L1·ROTATION. **MACRO transmission matrix (thesis = *why*) × SECTOR_FLOW (money = *now*)**
> → 11-sector OW/UW + DEEP targets + DEEP_LOG. Zero buy/sell calls.
> Inputs on disk: `MACRO_REPORT.md` §4 · `SECTOR_FLOW_US.json` (asof **2026-07-16**, us_top300) ·
> `US_LIVE_SHORTLIST.json` · `CYCLE_EXPOSURE.md`.
> ⚠ **The sweep is asof the previous close (07-16)** — today's crude move and today's NFLX print are
> NOT in these flow numbers. Flagged per-sector where it bites (ENRG).

---

## §0 Universe state — the backdrop the table sits on
`us_top300`: **wflow −0.09 · 🟢green 6 · 🔴red 59** (of 300).
Breadth underneath is **weak**: red outnumbers green ~10:1 while SPY is −0.56%/5d. This is an
**intra-equity rotation on a thin green list**, not a broad advance — it constrains how strongly any
OW can be read. Only 6 names in the whole universe carry 🟢ACCEL.

## §1 The two headline reads (this run's structure in one line each)
- **Health Care = money with no story.** Flow rank **#1** (wflow 0.357, Δw **+0.33** — the biggest
  one-day ignition on the board) while its **news velocity is dead last (465 hits/7d** vs FIN 2,759)
  and decelerating (`healthcare` ⚪ECHO **0.89×**, `pharma` ⚪ECHO **0.74×**).
- **Information Tech = story with no money.** The AI bucket is loud (2,312 hits/7d) while IT's
  **eqflow is −0.339 against wflow −0.094** — the mega-caps are masking a broad collapse underneath.

Those are the same fact seen twice: capital is leaving a narrated sector for an un-narrated one.

---

## §2 ★ 11-SECTOR OW/UW TABLE — matrix × flow

| # | Sector | Matrix (why) | wflow | eqflow | Δw | Flow rank | **Verdict** | AGREE / DIVERGE |
|---|---|---|---|---|---|---|---|---|
| 1 | **Financials (FIN)** | **OW** | 0.181 | **0.279** | +0.023 | **2** | **OW** ★ | **AGREE (strongest)** — and **eqflow > wflow = BREADTH-led**, not mega-cap-narrow. 3 of 6 shortlist names (PYPL/PNC/BNY), **2 of 3 new-🟢** (PYPL, BNY), the only ✅clean-rise on the board (PNC, shortZ −0.62), #1 velocity (2,759). Every axis agrees. |
| 2 | **Health Care (HLTH)** | Neutral | **0.357** | **0.264** | **+0.33** | **1** | **OW** ↑ | **DIVERGE (b) — PROMOTE.** Money moved before the thesis. Breadth: both wflow and eqflow strongly positive = **broad**, not narrow. ⚠ But **zero 🟢ACCEL names** and velocity last → a *drift*, not an ignition. **→ DEEP owns this.** |
| 3 | **Energy (ENRG)** | **OW** | −0.151 | −0.092 | **+0.159** | 8 | **modest OW** ↓ | **DIVERGE (a) — rotate DOWN a notch per rule.** Right thesis (CL=F **+10.2%/5d** realized), money not here yet. ⚠ **But the sweep is asof 07-16 and lags the crude move**, and Δw +0.159 is the **2nd-best ignition** = money starting to arrive. **→ DEEP must resolve early-vs-trap.** |
| 4 | **Utilities (UTIL)** | Neutral | 0.049 | 0.037 | −0.094 | 3 | Neutral | AGREE. Flow-rank 3 flatters it — wflow ~0 and **Δw −0.094 is falling**. No wind. |
| 5 | **Consumer Disc (DISC)** | Neutral | 0.02 | **−0.117** | +0.072 | 4 | Neutral | AGREE, with a **narrowness flag**: wflow +0.02 vs eqflow −0.117 = **mega-cap-narrow** (the average DISC name is being sold). Retail sales up a 5th month [2 outlets] does not show up in breadth. |
| 6 | **Real Estate (RE)** | **UW** | −0.046 | −0.04 | +0.092 | 5 | **UW** (soft) | **DIVERGE (mild) — named.** Matrix says UW on real 10Y 2.32% (+42bp/120d); flow says RE is **not** being sold (≈flat, Δw +0.092 positive). Thesis leads, flow lags. **Not DEEP-worthy — logged as a watch**; if real 10Y breaks <2.20% this UW is wrong. |
| 7 | **Information Tech (IT)** | **UW** | −0.094 | **−0.339** | −0.053 | 6 | **UW** ★ | **AGREE — and flow STRENGTHENS the matrix.** eqflow ≪ wflow = mega-caps propping a rotting breadth. Rank-6 wflow **understates** the damage. Recently deep-dived (07-15) → not re-picked. |
| 8 | **Industrials (INDU)** | Neutral | −0.107 | −0.081 | −0.038 | 7 | Neutral ↓ | AGREE. **Lost its 07-15 continuous slot** — both legs that justified OW failed (AI-power GEV −5.1%; defense LMT RS60 −17.6%, vol 0.58×). One lone new-🟢 (**FAST**, volsurge 1.54) = an (c)-ignition inside a Neutral sector → **watch-promote, not DEEP**. |
| 9 | **Consumer Staples (STPL)** | Neutral | −0.247 | −0.011 | +0.001 | 9 | Neutral | AGREE. wflow −0.247 vs eqflow −0.011 = the mega-caps drag, breadth flat. The defensive bid went to **HLTH, not STPL** — a useful discriminator: this rotation is selective, not blanket risk-off. |
| 10 | **Materials (MATR)** | **UW** | −0.304 | −0.253 | +0.041 | 10 | **UW** | AGREE on both axes + **Copper still 95%ile crowded-long**. Broad weakness (both flows negative). |
| 11 | **Comm Services (COMM)** | Neutral→UW | **−0.443** | **−0.03** | **−0.226** | 11 | **UW** | **AGREE — but the resolution matters.** Worst wflow AND worst Δw on the board, yet **eqflow only −0.03**. Cause: **GOOGL −0.68 / GOOG −0.70 🔴distribution at $4.49tn + $4.48tn combined** drag the entire mcap-weighted number, while **META is +0.79 🟢ACCEL**. This is a **Google-specific verdict, not a sector one.** |

### §2a Divergence register (every one named, with a resolution owner)
| Type | Sector | Divergence | Resolution owner |
|---|---|---|---|
| **(a)** matrix-OW, flow-absent | **ENRG** | Thesis realized in the commodity (+10.2%) but equity flow rank 8 | **DEEP · ENRG** — early or trap? |
| **(b)** flow-led, matrix under-rated | **HLTH** | Flow #1 + biggest Δw, but zero narrative and zero ignitions | **DEEP · HLTH** — durable rotation or parking lot? |
| **(c)** new-🟢 ignition | FIN ×2 (PYPL, BNY) | Confirms the FIN OW | **DEEP · FIN** (folded in) |
| **(c)** new-🟢 ignition | INDU ×1 (FAST) | Lone ignition in a Neutral sector | **Watch-promote** — logged, not DEEP |
| **(mild)** matrix-UW, flow-flat | RE | Thesis leads flow | **Watch** — falsifier: real 10Y <2.20% |
| **(structural)** | COMM | Sector verdict is one name (GOOGL) | Logged here; **no DEEP** (UW sectors are not DEEP targets) |

---

## §3 DEEP target selection (by the rule — never by gut)

**Recency input:** `DEEP_LOG 2026-07-15: continuous=[INDU] rotating=[FIN,IT,UTIL]` (+ a premortem-promoted
5th, SEMI). Covered in the last run: **INDU, FIN, IT, UTIL, SEMI**. Only one prior US DEEP_LOG exists, so
the "~3 runs" recency window currently holds exactly one run.

**① Continuous-track 2 = today's top-2 OW → `FIN`, `HLTH`.**
- ⚠ **Continuity rule checked and NOT applied:** the previous run's continuous slot was **INDU**. The rule
  keeps a slot only if that sector is *still top-4 OW today* — **INDU is Neutral today**, so it **loses the
  slot**. Stated explicitly per the rule.
- **FIN** is top-2 OW *and* was rotating-covered on 07-15. It is picked on **today's rank (①), not on
  continuity** — the rule's ② recency bar applies to *rotating* picks only, and FIN is the single
  strongest AGREE on the board (breadth-led flow + 2 ignitions + the only clean-rise + #1 velocity).
  Re-covering it is a rank outcome, not a thrash.

**② Rotating 2 = next-highest OW not deep-dived in the last ~3 runs → `ENRG` only.**
- **ENRG** qualifies cleanly: it is the next-highest OW (modest OW) and was **explicitly NOT deep-dived on
  07-15** ("Energy→premortem not padded"). It also carries the run's (a)-divergence → highest-value DEEP.
- **No second rotating pick exists.** After FIN/HLTH/ENRG, the board holds **no further OW** — everything
  remaining is Neutral (UTIL, DISC, INDU, STPL) or UW (IT, MATR, RE, COMM).

**→ 3 DEEP targets: `FIN`, `HLTH`, `ENRG`. NOT padded to 4.**
Per the rule — *"Never pad with Neutral/UW to reach 4 — fewer is fine if stated."* — a 4th would have to
come from a Neutral or UW sector, which the rule forbids. **Stated: this run deep-dives 3.**
(IT is the run's biggest *change* and carries the core P2 proposition, but it is **UW** — not a DEEP target
by the rule — **and** it was covered on 07-15. It is handed to PREMORTEM instead, where the sign-flip's
both-sides bracket belongs.)

### §3a The question each DEEP must answer (set here, not in DEEP)
1. **DEEP · FIN** — Is the breadth-led bid (eqflow 0.279 > wflow 0.181) an *earnings* leg or a *curve* leg?
   They fail differently: SCHW on **07-21 (binary)** tests earnings; a real-10Y break >2.50% tests the curve.
   Which one is PNC's ✅clean rise actually paying for?
2. **DEEP · HLTH** — **Money with no story: durable or parking lot?** Zero 🟢ACCEL names, velocity 465 and
   *decelerating* (0.89×/0.74×), yet the largest Δw on the board and broad (eqflow +0.264). Distinguish
   (i) early un-crowded rotation the narrative hasn't reached, from (ii) defensive parking that unwinds
   the moment MU stabilizes above 853.20. **Name the falsifier.**
3. **DEEP · ENRG** — **Early or trap?** The commodity moved +10.2% and the equities did not follow
   (wflow −0.151). Either the equity is late (→ Δw +0.159 is the leading edge) or the market disbelieves
   the crude move (→ the TACO branch, and WTI's 13%ile short covers into a collapse). ⚠ Resolve using data
   **newer than the 07-16 sweep** — this divergence may be an artifact of the sweep's asof date.

### §3b Handed forward (not DEEP)
- **→ PREMORTEM:** the **P2 AI-capex sign-flip** both-sides bracket; **NFLX today (D-0 binary)**; the
  **Hormuz/TACO** binary; and the ⚠ **book tension** from `CYCLE_EXPOSURE.md` — no 🚨 GAP fired
  (AI-compute epicenter **12.06%** vs need ≥12.0%, holding **NVDA/TSM/AVGO**), but the book's core sits in
  **exactly the cycle this run downgraded to UW**. The 07-14 postmortem's failure was *zero* exposure to a
  top cycle; the symmetric risk today is *held* exposure into a de-rating one. PREMORTEM owns that bracket.
- **→ ALPHA:** the ENRG substantive-exposure observation — `cycle_exposure` reports **rank-2 Energy at 0.0%
  epicenter**, and **no 🚨 fired only because that cycle's `need≥` is 0.0%**. The rule did not trip; the
  substance is still a rank-2 cycle with zero epicenter exposure while its commodity ran +10.2%. Reported
  as an observation, not a GAP (P4: the tool said ✅).
- **→ Watch:** FAST (INDU ignition, volsurge 1.54) · RE (falsifier: real 10Y <2.20%) · GOOGL (the whole
  COMM verdict rests on it).

---

## DEEP_LOG 2026-07-17: continuous=[FIN, HLTH] rotating=[ENRG] (3 picks — no 4th OW existed; NOT padded. INDU lost its 07-15 continuous slot: Neutral today. IT/UTIL/SEMI rested: covered 07-15 and not OW today.)

---
**EXIT CHECK:** ✅ 11-sector OW/UW table written; **every** matrix×flow divergence named with a resolution
owner (§2a register: ENRG→DEEP, HLTH→DEEP, FIN-ignitions→DEEP, FAST→watch, RE→watch, COMM/GOOGL→logged) ·
✅ DEEP targets picked by the rule with continuity **checked and explicitly not applied** (INDU) and
recency stated (ENRG not covered 07-15); **3 picks, no padding, reason stated** · ✅ DEEP_LOG appended ·
✅ sweep asof-07-16 caveat carried onto the sector it actually bites (ENRG).
**→ proceed to PREMORTEM.**
