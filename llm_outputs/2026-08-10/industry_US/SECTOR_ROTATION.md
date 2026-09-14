# SECTOR_ROTATION — industry_US · 2026-08-10 · Stage 6/11 (L1·ROTATION)

> Delta-only. MACRO owns the 11-sector verdict; `SECTOR_FLOW_US.json` owns the flow numbers. Both are
> on disk. This file writes **only what changes and why** — and today what changes is **nothing**,
> for reasons that are themselves the output. Analytical only (P4).

## §0 · The axis count this run scored on — read before any number below

`SECTOR_FLOW_US.json §scoring`: **`n_axes` 3 · `vel_coverage` 0.0 · `scored` 299 ·
`dropped_missing_axis` 1.**

**The news axis is dead in this run.** Therefore, per the EXIT CHECK:
- **No delta may cite theme freshness or news velocity.** None does.
- **Δ vs the prior snapshot may only be read against a snapshot of the same axis count.** The only
  other 3-axis snapshot in `history.json` is **2026-07-20, which holds FIVE tickers** ⇒
  **Δ is disqualified entirely this run (`D232`)**, and **the `신규🟢` list with it.**
- ⚠⚠ **And a stronger constraint that SWEEP measured**: **levels are not comparable across runs
  either.** Three runs on the *identical* settled 08-07 bar produced ENRG wflow **+0.342 → +0.342 →
  +0.286**, IT eqflow **−0.092 → −0.103 → −0.160**, STPL eqflow **−0.165 → −0.173 → −0.184**.
  **Nothing moved but the scoring mode.** ⇒ **only WITHIN-run, cross-sector comparisons are used below.**

## §1 · Inherited — one line, verbatim

**MACRO holds:** `INDU OW− · ENRG N+ · FIN N+ · IT N · HLTH N · DISC N · MATR N− · COMM UW · UTIL UW ·
STPL UW− · RE UW` — **one overweight on the board and it is OW−.**

## §2 · Deltas — **ZERO**, and four declines with their numbers

**No sector verdict changes this run.** The protocol states that a zero-delta run is a valid,
informative output; this one is, because **the reading that would have produced deltas is measurably
an instrument artifact**, and refusing it is the work.

### 2a. 🚨 The demotes this stage DECLINED, and why declining them is the finding

A naive read of today's board demotes Energy and Financials: **ENRG's greens went 2 → 0 and FIN's
went 4 → 1** against the 08-08 run. **Both would be wrong.**

SWEEP §2 ran the comparison as a controlled ablation — **three runs, identical settled 08-07 prices,
identical universe file, only the velocity axis differing** — and the 08-08 run had **pre-registered
the exact mechanism** (M513): *both Energy greens (XOM `vol_surge` 0.88, CVX 0.96) and three of four
Financials greens (JPM 0.65, BAC 0.73, BRK-B 0.85) are velocity-lit on below-average volume.*

| | 08-08 | 08-10 | M513 predicted |
|---|---|---|---|
| ENRG 🟢/16 | 2 | **0** | **2 → 0** ✅ |
| FIN 🟢/47 | 4 | **1** | **4 → 1** ✅ |

⇒ **the green collapse is the axis being removed, not money leaving.** A demote carried by it would
be a **Δ citation on mismatched scales (G2)** wearing a level's clothes.

| Sector | Matrix | Attempted delta | Flow evidence | **Verdict** |
|---|---|---|---|---|
| **Energy** | N+ | → N | **wflow +0.286 = rank 1 of 11** but **breadth 0🟢/16** and eqflow +0.063 | ❌ **DECLINED.** The breadth number is the ablation above. **N+ held.** The *real* open question — does the N+ have a macro carrier after P4⁗'s withdrawal — is contested by two physical refinery strikes (EVENT_ALPHA Card 2) and **belongs to S55 (settles 08-11), not to a flow delta** |
| **Financials** | N+ | → N | **wflow +0.082 = rank 2** with **breadth 1🟢/47 = 2%** | ❌ **DECLINED**, same mechanism. ★ **What survives as a genuine within-run fact**: the one surviving green is **PRU**, reproducing DEEP-FIN's 08-08 result (exactly one of 47 clears volume-confirmed accumulation) **by a different route** |
| **Comm Services** | UW | → UW− | wflow **−0.262 = 2nd worst of 11** against **eqflow +0.050 (positive)** | ❌ **DECLINED on R56.** The sector's 2 greens must be re-derived ex-**EA**, and **EA is still in `us_top300.csv` at row 236 and still tagged 🟢가속 with the board's highest `vol_surge` (3.66) on a security that went private 08-04/05.** D207's liveness assertion caught it again: **15 shortlist names tested, 1 FAIL (EA), 0 false positives — 4th consecutive run** |
| **Information Technology** | N | → N− | **eqflow −0.160 = worst of 11** with 3🟢/56 | ❌ **DECLINED and handed to DEEP.** The contradiction is at maximum width — the sector's own ETF was **the best on the week (XLK exc5 +3.69 vs SPY)** while its breadth is the board's worst. **A delta cannot resolve a contradiction; a deep-dive can.** IT takes a DEEP slot (§3) |

### 2b. 🚨 `top1_flips_sign` — reproduced in full even though it changes nothing

**One sector of eleven flips sign when its largest name is removed:**

| Sector | wflow | ex-top1 | top1 | share of sector cap | n |
|---|---|---|---|---|---|
| **Materials** | **−0.038** | **+0.173** | **LIN (Linde)** | **24.7%** | 12 |

🚫 **Materials may not carry a promotion or a demotion on `wflow` today. Its sign is Linde at 24.7%.**
Its non-cap-weighted numbers are **eqflow +0.040** and **breadth 0🟢/12** — which disagree with each
other in sign, so neither substitutes cleanly. ⇒ **N− held**, and the sector's real question is
handed to DEEP (§3) because a **second, independent** reason not to trust the aggregate arrived today:
**85% of the observable that decides Materials (S57's XLB 5-session excess, +1.31, 0.59pp from firing)
is NEM alone (+17.05pp excess), and NEM's driver printed this morning as a $1.95bn JV settlement in
which Newmont PAYS Barrick** (MACRO §C-1, EVENT_ALPHA Card 6).

For the record, the largest non-flipping ex-top1 shifts: **Consumer Discretionary −0.033 → −0.273
(AMZN)** · **Energy +0.286 → +0.151 (XOM)** · **IT −0.008 → −0.110 (NVDA)** · **Industrials +0.041 →
+0.105 (CAT)**. **Concentration is not a flip** — none of these four changes sign, and none is
rejected for being top-heavy.

### 2c. Divergences named, each with a resolution owner

| Divergence | Money is on | Owner |
|---|---|---|
| **ENRG: flow rank 1 vs price rank 11** (XLE exc5 −6.95, worst of 11) | flow says weight, price says exit; **breadth (0/16) cannot arbitrate today** | **S55 (08-11) · S67 (08-13)**, not ROTATION |
| **IT: worst eqflow (−0.160) vs best sector ETF week (XLK +3.69)** | undecided at maximum width | **DEEP-IT (§3)** |
| **INDU: eqflow (+0.098) > wflow (+0.041), 5🟢/50** | **breadth — the only sector where the board's single OW is corroborated by breadth rather than by weight**; 3 of 15 shortlist names are Industrials (EMR, PH, AME), none mega-cap | **DEEP-INDU (§3), continuous** |
| **MATR: aggregate vs one name** | the aggregate is 85% NEM | **DEEP-MATR (§3) + PREMORTEM (S57-ANNEX)** |
| **UTIL: loudest news velocity on the board (VST 2.27× · CEG 1.86× · NRG 3.18×) vs 분산 on all three** | money — story without money | **PREMORTEM / ledger re-checks 08-14, 08-20**; ⚠ UTIL is one of the three sectors the instrument **cannot move** (§2d), so a delta here would be uninformative by construction |

### 2d. A structural note that limits three sectors' readability

SWEEP §2a measured that **Materials, Real Estate and Utilities are byte-identical across all three
runs on this bar** (−0.038/+0.040 · −0.032/−0.025 · −0.395/−0.381) — and they are **exactly the three
sectors with zero names in the market-cap top 50**, i.e. zero velocity-whitelisted names. **11 of 11
agreement.** ⇒ for these three, today's flow numbers are **the same reading three runs running, not
three observations (S1)**, and no amount of re-reading will move them.

## §3 · DEEP picks and DEEP_LOG — **N = 4** (protocol DEEP budget: 2 continuous + 2 rotating)

⚠⚠ **The rotating rule is DEGENERATE again, for a second consecutive run, and the deviation is
declared rather than hidden.** The rule says *continuous = today's top OW ranks* and *rotating =
next-highest OW not covered in ~3 runs*. **The board holds exactly ONE overweight (INDU OW−).**
⇒ one continuous slot can be filled by the rule; **the other three are declared fallbacks**, each
with its stated basis.

| Slot | Sector | Basis |
|---|---|---|
| **Continuous 1** | **INDU (OW−)** | **By the rule.** The board's only OW; held a continuous slot on 08-08 and is still top-OW ⇒ **anti-thrash APPLIES and the slot is KEPT.** Its flow case is the board's only breadth-led one (eqflow +0.098 > wflow +0.041, 5🟢/50) |
| **Continuous 2** | **IT (N)** | **Declared fallback — no second OW exists.** Chosen on a within-run flow number: **eqflow −0.160, worst of 11**, 3🟢/56, against **XLK exc5 +3.69, the best sector on the week** — the widest matrix×flow contradiction on the board, and the only one a deep-dive can resolve. **Last covered 2026-08-05 — 4 runs.** ★ It also carries the run's one **un-bracketed** exposure of the desk's own regime call (EVENT_ALPHA Card 3, CXMT) |
| **Rotating 1** | **STPL (UW−)** | ★★ **A written pre-commitment honoured on its first ask.** `DEEP_LOG 2026-08-08` wrote *"STPL — ★next run's first rotating pick"*, and **STPL has NEVER received a DEEP slot in this desk's recorded history.** Today it is **worst of 11 on both non-cap-weighted axes (eqflow −0.184) and on wflow (−0.220)**, 0🟢/18. ⚠ **Composition note it must diagnose**: n fell 19 → 18 — **MNST** was the single `dropped_missing_axis` name, and since MNST scored **−0.60** on 08-08, **removing it should have made STPL less negative; STPL got worse.** The deterioration is scoring-mode, not composition |
| **Rotating 2** | **MATR (N−)** | **Recency filter deliberately broken and stated** (covered 08-08, one run ago). Basis: **S57 settles 2026-08-12 at 0.59pp from branch A**, **85% of its observable is one name**, and **that name's driver changed this morning** ($1.95bn, direction of payment reversed vs the headline). The 08-08 DEEP predates the disclosure entirely. **A bracket that decides a sector verdict in two days, whose carrier's cause was published today, outranks a one-run recency filter** |

**Not selected, with reasons** — so "we looked and passed" stays distinguishable from "we never looked":

- **ENRG (N+)** — the most eventful sector in the run (EVENT_ALPHA Cards 1 & 2), **covered 08-08 as a
  continuous slot**, and its live question settles on a **price bracket (S55, 08-11)** rather than on
  anything a deep-dive produces this week. **Handed to PREMORTEM and BET instead of to DEEP.**
- **FIN (N+)** — covered 08-08 (rotating). Its 08-08 deep-dive already produced the finding today
  reproduced independently (PRU as the only accumulation-gate pass). **A second dive on the same bar
  would be one observation counted twice (S1).**
- **HLTH (N)** — covered 08-06; breadth rank 3 today (4🟢/32, eqflow +0.096, **positive and 2nd-best
  of 11**). ⚠ **Carried forward with the 08-08 log's own instruction**: its promotion has now been
  declined on an anti-signal whose magnitude weakened **−6.78 → −3.05 → −1.59pp** across three runs.
  **A fourth firing at a smaller magnitude should re-examine the anti-signal, not the sector.**
- **UTIL (UW)** — covered 08-05, but §2d shows the instrument cannot move it, and **S62's fire was
  degenerate (D206)**. **DISC (N)** — covered 08-03 (longest gap) but its 4-run window disagreement
  **CLOSED on 08-08 with both windows at ≈zero (C3, no signal)**. **RE (UW)** — covered 08-04, 0🟢/12
  and eqflow −0.025, no signal in either direction. **COMM (UW)** — covered 08-07; **its un-owned
  telecom node (T/VZ/CMCSA) is still un-owned for a 3rd run**, and R56 blocks any aggregate read.

## DEEP_LOG 2026-08-10: continuous=[INDU, IT] rotating=[STPL, MATR] · N=4/4 · **ZERO verdict deltas, and that is the output** — the two demotes the board's face invites (ENRG N+→N on 2🟢→0, FIN N+→N on 4🟢→1) were **DECLINED because SWEEP's controlled ablation showed the green collapse is the velocity axis being removed, on an identical price bar, exactly as M513 pre-registered (predicted 2→0 and 4→1; observed 2→0 and 4→1)** · **two further attempts declined with numbers: COMM UW→UW− on R56 (EA still 🟢 at `vol_surge` 3.66 and still delisted; D207 liveness = 15 tested, 1 FAIL, 0 false positives, 4th run), IT N→N− because a matrix×flow contradiction at maximum width (eqflow −0.160 worst of 11 vs XLK exc5 +3.69 best of 11) is a DEEP question, not a delta** · **Δ and 신규🟢 DISQUALIFIED entirely (`D232` — the only same-mode baseline in `history.json` is 2026-07-20 with FIVE tickers, 18 days stale; 294 of 299 names carry `delta=null`)** · **flip list: 1 of 11 — Materials / LIN / 24.7% of sector cap / n=12 ⇒ MATR may not move on wflow** · ★ **structural limit recorded: MATR, RE and UTIL are byte-identical across three runs on this bar and are exactly the three sectors with ZERO names in the mcap top-50 (11/11 agreement) — for these three the instrument cannot produce a new reading** · **INDU continuous by the rule (anti-thrash APPLIED — only OW, held continuous 08-08)** · **IT continuous by declared fallback (no 2nd OW exists; 4 runs uncovered; widest contradiction on the board; carries the un-bracketed CXMT exposure of the regime call)** · **STPL rotating — the 08-08 written pre-commitment HONOURED on its first ask, and it has NEVER been deep-dived in recorded history** · **MATR rotating — recency filter deliberately broken (covered 08-08) because S57 settles 08-12 at 0.59pp, 85% of its observable is NEM, and NEM's driver was disclosed THIS MORNING ($1.95bn paid BY Newmont TO Barrick — the WSJ headline reverses it)** · uncovered=[**ENRG(N+, covered 08-08 continuous — deliberately not re-dived; its question settles on S55 08-11 / S67 08-13 and was handed to PREMORTEM+BET; two physical refinery strikes in four days contest P4⁗'s withdrawal)**, **FIN(N+, covered 08-08 rotating; its 08-08 finding (PRU the only accumulation pass of 47) was independently reproduced today; S65 08-11, S51/S66/S70 BLOCKED by FRED for a 4th run)**, **HLTH(N, covered 08-06 — 3 runs; eqflow +0.096 = 2nd best of 11 and 4🟢/32; ★the 08-08 instruction stands: its anti-signal has weakened −6.78→−3.05→−1.59 across three firings and a 4th should re-examine the ANTI-SIGNAL, not the sector — ★next run's first rotating pick)**, UTIL(UW, covered 08-05; **instrument-frozen (§2d)**; loudest news velocity on the board (NRG 3.18× · VST 2.27× · CEG 1.86×) against 분산 on all three = story without money; ledger re-checks 08-14 GEV/CAT/EMR and 08-20 VST), COMM(UW, covered 08-07; **telecom node T/VZ/CMCSA un-owned for a 3rd run**; R56 blocks the aggregate), DISC(N, covered 08-03 = longest gap, but its 4-run window disagreement CLOSED 08-08 at ≈zero both windows ⇒ C3 no signal), RE(UW, covered 08-04, 0🟢/12 · eqflow −0.025, no signal either direction (C3))]

## ✅ EXIT CHECK

- [x] **§1 is ONE line**, MACRO's matrix verbatim. No unchanged sector gets a row, paragraph or restated flow number
- [x] **Every §2 entry cites a flow number** — and since the delta count is **zero**, what §2 contains
      is **four declines**, each carried by a flow number (breadth 0/16 · 1/47 · eqflow +0.050 vs wflow
      −0.262 · eqflow −0.160). **No verdict was moved by a macro argument**; the two macro arguments
      available (Hormuz conditions, refinery strikes) were **explicitly routed to S55/PREMORTEM, not
      used as deltas**
- [x] 🚨 **No promotion or demotion rests on a `top1_flips_sign` bucket** — Materials is the only
      flipper and is **declined in both directions with its top-1 share written out (LIN, 24.7%)**.
      **The flip list is reproduced in §2b even though it changes nothing**
- [x] **The axis count is stated first** (`n_axes 3`, `vel_coverage 0.0`); **no delta cites theme
      freshness or news velocity**; **Δ is disqualified against a 5-ticker 18-day-old same-mode
      snapshot** and is not read at all
- [x] **Every matrix×flow divergence named with a resolution owner** (§2c, five of them)
- [x] **N=4 DEEP targets picked by the rule where the rule can operate**, with the **degenerate
      rotating fallback declared**, continuity stated (INDU anti-thrash APPLIED), recency stated
      (IT 4 runs · STPL never · MATR deliberately broken with its reason). **No padding**; **every
      uncovered sector named in DEEP_LOG with its last-covered date and its dated catalyst**
- [x] **Linter run on this stage's own output**
- [x] **DEEP_LOG line appended**
- [x] **No position sizing, no buy/sell language (P4)**
