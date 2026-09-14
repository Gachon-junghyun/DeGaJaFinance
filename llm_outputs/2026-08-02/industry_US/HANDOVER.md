# HANDOVER — industry_US · 2026-08-02 (Sun) · STAGE 1, runs before MACRO

> Inheritance step. Reads the shared spine (`STANDING_VIEW.md` + `SCENARIOS.md`) in full, this desk's
> `STANDING_VIEW_US.md` / `SCENARIOS_US.md`, and `RESEARCH.md`; scores every past-dated and every
> condition-settled bracket; audits both ledgers; carries the view forward.
> Analysis only — no buy/sell, no sizing (P4). `[measured]` / `[inferred]` tags preserved; no
> `[inferred]` claim is passed downstream as evidence.

---

## 0. Run clock, and what it makes admissible

**Run date 2026-08-02 is a Sunday.** The last US settled session is **Friday 2026-07-31**, and it is
fully settled — which is the single most useful property of this run's clock:

- ★ **Every "live intraday" read the 2026-07-31 run was forced to take on an unsettled bar is now
  finalizable on a settled close.** The 07-31 HANDOVER labelled its own tracking table
  *"07-31 intraday KIS/live bars — unsettled, so directional not settled."* This run settles them.
- The prior US run's sweep (`llm_outputs/2026-07-31/industry_US/SECTOR_FLOW_US.json`) carries
  **`asof: 2026-07-31`** — a **same-day** stamp, breaking the one-session-lag convention every earlier
  file used (07-28 file → asof 07-27; 07-29 → 07-28; 07-30 → 07-29). It was written on a live bar
  (**D74**). **Every bracket leg below was therefore re-derived independently from settled yfinance
  daily closes and cross-checked against that JSON (D5).** The two agree on all signs; the largest
  single-name gap is **MU rs20 −12.8 (JSON) vs −15.9 (settled recomputation) = 3.1pp**. Where they
  straddle a threshold, that fact is reported rather than resolved.
- **No US market data exists for 2026-08-01 or 08-02.** Nothing in this run is dated after 07-31.

⚠⚠ **Process failure found at intake, named rather than buried — the 2026-07-31 `industry_US` run's
analytical carry was never written back.** `STANDING_VIEW.md`'s asof chain jumps
**07-31 (industry_kr) → 07-30 (industry_US)**; `STANDING_VIEW_US.md` ends at the *07-30* US block
(**M281**, §3a rows asof 07-29/07-30) with **zero 07-31 US fact rows and zero 07-31 §3a overwrites**;
and `SCENARIOS.md`'s master scoring log has **no "rows added 2026-07-31 by the `industry_US` run"
block** — so **S32's `AMBIGUOUS` verdict and the HUM `reaffirmed` resolution live only in that run's
`HANDOVER.md` on disk, not in the carry.** Only the S50/S51 *registrations* landed in
`SCENARIOS_US.md` and the master index. This is the same class as an unscored past-dated row: work was
done and the ledger does not know it. **This run's writeback repairs both runs and says so.**

---

## 1. Inherited regime call — read before anything was decided

**Memory is a price-cycle industry in rate-of-change deceleration while its level stays tight.**
`[inferred]`, built on the measured chain (M1–M9, M18). The equity tracks the **second derivative of
price**, not the level — which is why "shortage through 2027" (M7) and "price growth decelerating"
(M1) are both true (**C3**). **The governing asymmetry (§4) is unchanged: a hyperscaler capex CUT
rewrites the thesis; a capex RAISE only moves its timing.**

★ **The regime call gained a third independent OEM read-through this weekend** (see §3, S46):
**AAPL guided September-quarter gross margin to 47–48% against a reported 50.1%**, i.e. **−2.1 to
−3.1pp**, and the feed names memory cost as the mechanism. **M141** registered exactly this channel —
*"the OEM gross-margin line is a public read-through of the memory node's private LTA price terms"* —
on DELL and HPE's 10-Qs. **AAPL is the third and the largest.** `[measured]` on the guide figure;
the attribution to memory is `[news]`-grade and is **not** passed downstream as evidence.

**Retracted ledger (§5) read BEFORE today's view formed.** Killed claims that must not resurface,
most binding on a US run: **R8** (PSX cheapest refiner — `core_pick` is human-locked and was NOT
modified; **D19** still prints the retracted string), **R10** (IT+RE+UTIL are one AI-datacentre
correlation — false for the RE leg, true for the UTIL leg, M148), **R11** (long end is
bear-steepening), **R12** (the crack-detachment counter is continuous), **R23** (STX +15.1pp over its
prior peak — a quarterly/annual mix), **R31** (`theme_age` structurally uninformative), **R32**
(Financials is breadth-led — the eqflow−wflow gap flips sign on removing BRK-B). Cross-market:
**R13** (000660 ADR ceiling is 2.5% not 25%; the suspension is EXTENDED), **R30** (the US-Gulf crack
is wrong-signed as a KR proxy, and **S8's absolute 60/84 lines are not scoreable on this data**).
**No claim in this HANDOVER re-argues a retracted entry.** ⚠ §3's S49 reading is written on a
**change**, not a level, precisely because R30/D95 withdrew levels on this series.

**Open contradictions carried, not resolved (§6):** **C1** (LTA floors cap upside and floor
downside — now primary-sourced from the seller, M228, still with no disclosed price term),
**C4** (refining node: margin or war premium), **C5** (security momentum vs an unmeasured valuation
axis), **C6** (the un-narrated capex-cut branch), **C7** (Health Care belief-vs-money, re-check 08-06;
⚠ its resolving observable's *definition* was never written down — a human must fix it before a second
reading is scoreable), **C8** (IT is one label over three legs wanting opposite verdicts).
★ **C8 is the contradiction this run's scoring moves most** — see S30.

---

## 2. Per-name US carry, re-read on settled 2026-07-31 closes

Full rows in `STANDING_VIEW_US.md §3a` (asof 07-29/07-30 — the 07-31 run wrote none). RS = excess
vs **SPY** over the stated number of sessions, own calc on settled daily closes, benchmark inline (**C1**).

| Name / node | Standing thesis | Tag | Settled 07-31 read |
|---|---|---|---|
| **MU · STX · WDC** | Memory suppliers; **3 names had lost the 60-day cushion** | `[measured]` | ★★ **RS20 STX +4.1 · MU −15.9 · WDC +0.8 ⇒ median +0.8 — CROSSED ABOVE ZERO. S30 FIRED-A (§3).** 07-30 was the turn: STX +11.4% · MU +18.4% · WDC +15.4% vs SPY +1.68% in one session |
| **AMAT · LRCX · KLAC** | "A pullback inside an uptrend"; the live axis is the revision book | `[measured]` | RS20 −16.1 / −16.9 / −22.7 against RS60 +20.4 / +3.0 / +2.3 — **still the M149 geometry, and they did NOT participate in the 07-30 turn the way STX/WDC did.** The stack is not moving as one (**W5**) |
| **DELL · HPE** | S30's registered **control pair** — the only two whose 60-day excess sits in days 21–60 | `[measured]` | **DELL RS20 +2.5 (registration +6.2, falling) · HPE +15.9 (registration +1.4, rising)** ⇒ **the pair SPLIT.** S30's own control test ("memory event vs IT-beta event") is therefore **indistinguishable (C4)** — recorded, not decided |
| **AAPL** | ⚠ Revived on the reject ledger 07-30 with an **arithmetically zero base** (days 21–60 = +0.16) | `[measured]` | ★★ **−7.35% on 07-31, far outside S46's pre-declared ±3.3% no-information band ⇒ the move IS information.** Sept-quarter **GM guide 47–48% vs 50.1% reported = DOWN** ⇒ **S46 branch A's first leg is MET**; its second leg straddles the line (§3) |
| **QCOM** | Guided weak on cost inflation + Apple modem loss | `[measured]` | RS20 **−16.6** / RS60 −24.1 — the board's worst pair among carried names. Ledger `K.본문반증`, recheck 08-13 |
| **XOM** | The control; **927% of its 60-day excess earned in the last 20 sessions** | `[measured]` | **RS20 +13.1 / RS60 −2.9 ⇒ days 21–60 = −15.9.** S31 branch A (**against us**) still tracking; XOM printed 07-31, inside its own window as declared at registration |
| **VLO · MPC · PSX** | Refining margin, distillate leg leading | `[measured]` | RS20 **+16.6 / +18.5 / +19.7**, RS60 +20.2 / +18.3 / +14.2 — all three still positive on both windows. ⚠⚠ **But the commodity moved hard against the thesis on 07-31: see §3 S49 and the 3-2-1 note** |
| **The regulated seven** (WEC·ETR·EXC·SO·XEL·AEP·D) | The leg the 07-28 UW demote swept up with AI-power | `[measured]` | **Median RS20 −4.89**, from **+0.39 on 07-29** ⇒ **the cross that fires S35-A lasted one session and reverted** (§3) |
| **VST · CEG · GEV · VRT** | The AI-power leg | `[measured]` | **Median RS20 −6.77**, from −14.35 ⇒ **improved 7.6pp.** S24 threshold is >0 by 08-12; not met |
| **DLR / PLD · AMT · WELL** | RE turn off a **weak base** (all greens carry a negative 60-day base) | `[measured]` | **DLR RS20 +8.5 vs the {PLD +3.4, AMT +4.1, WELL −1.0} median +3.4 ⇒ DLR is now ABOVE the median**, having been below it for four consecutive settled sessions. **S25's frozen threshold already fired (§3)** |
| **WAB · PCAR · MMM · ITW** | The capital-goods ignition, momentum-only, hard-stop stamped | `[measured]` | Median RS20 **+10.65** (registration +13.2), control **CAT −14.9** ⇒ S42 branch B tracking, and the sub-node reading (**W5**) holds |
| **MA · V · PYPL** | The payments leg of the FIN OW | `[measured]` | RS20 **+6.0 / +0.8 / +25.5** — all three positive ⇒ S14 tracking branch A. **MA moved +2.49% on its 07-30 print, INSIDE the pre-declared ±3.9% band ⇒ pre-committed NO INFORMATION** (S14-num) |
| **TRV · CB** | The FIN OW's internal hedge | `[measured]` | TRV RS20 +9.1 / RS60 +21.0; CB −3.2 / +5.5. Re-check 08-06 |
| **HUM** | Deepest 60-day base measured anywhere; the money is leaving it | `[measured]` | RS20 **−8.6** / RS60 **+48.7** ⇒ days 21–60 **+57.3**. Ledger `H.밸류소진`, **resolved `reaffirmed` on the 07-31 run** — that resolution is in this run's writeback |
| **NVDA · AVGO** | A separate boat from memory (hyperscaler-capex driven) | `[inferred]` | RS20 +2.7 / +7.7; RS60 −1.1 / −12.1. Held epicenter names; S41 hits both |
| **TSM · LNG** | ⚠ Held book names **outside `us_top300`** — no flow, RS or short axis exists (M252) | `[measured]` gap | **27% of the US book still sits on no measured axis.** Unchanged; carried as an instrument gap, not a view |

★ **Coverage-gap rows carried with numbers rather than prose** (the M183/D60 mitigation): **GRMN
RS20 +22.1 / RS60 +22.0** (the sweep's #1 flow score of all 300, no thesis anywhere) · **CTAS +12.5 /
+17.7** · **TRI +9.7 / −0.4** · **SPG +1.2 / +10.2** · **HCA −2.2 / −9.3** · **TMO +9.4 / +19.8**.
**None has a 4Phase ⇒ none has a thesis.**

---

## 3. Scenarios scored this run

> ★★ **This section executes the rule the desk re-staged after S39 and S29 —** *classify every ARMED
> row as **date-settled** or **condition-settled**, and check every condition-settled row against
> today's data.* Both prior instances were failures found one run late. **Applying it today fires
> five brackets that were sitting in "tracking" tables, three of them on conditions met days ago.**
> Every verdict below is scored against the **frozen** threshold in the registered text; **no
> threshold was widened and no proxy was substituted.**

### 3a. Verdicts

| ID | Event / condition | Verdict | Basis (frozen observable only) |
|---|---|---|---|
| **S21** STNG Q2 | print **2026-07-30** — **past-dated and unscored by the 07-30 and 07-31 runs** | **FIRED-C** | Branch C = *"inside ±10.0% either way — no information, pre-committed so an in-band reaction cannot later be read as confirmation."* **STNG 78.53 (07-29) → 75.53 (07-30) = −3.82%**, and −0.85% cumulative through 07-31. **Comfortably inside the frozen ±10.0%** ⇒ **C.** ⚠ **Branches A/B could NOT be read**: their legs are **Q2 TCE $/day** and **% of Q3 days already booked**, both of which the press release presents **in tables** that the body scraper does not capture (the release's prose says *"Below is a summary of the average daily TCE revenue…"* and the table is absent). ⇒ **the fundamental legs are instrument-blind, the price leg is clean, and C is the branch that fires.** ★ **Directional context recorded and explicitly NOT used to score**: adjusted net income **$243.7m = "the strongest performance in the history of the company"**, adjusted EBITDA $300.5m, cash break-even **below $11,000/day**, Q3-to-date product-tanker rates *"above $30,000 per day"* — none of which reads as branch A's *"the rerouting rent has already peaked."* ⚠⚠ **Registration defect, D28's family, third instance**: S21's grid puts a **fundamental** observable in A/B and a **pure price-reaction band** in C, so the branches are not on one axis and can be simultaneously true. Logged, not used to re-score |
| **S30** memory suppliers | *"median RS20 vs SPY of {STX, MU, WDC} **crosses above 0 by 2026-08-05**"* — **condition-settled** | ★★ **FIRED-A (against us)** | **Median +0.78 on settled 2026-07-31** (STX +4.1 · MU −15.9 · WDC +0.8), reproduced independently by the desk's own instrument at **+0.6** (07-31 sweep JSON). Registration median **−23.7**; path **−16.5 (07-27) → −28.3 (07-28) → −25.3 (07-29) → −10.4 (07-30) → +0.8 (07-31)**. The cross happened on **07-31**. **Invalidation checked and NOT triggered: HY OAS 2.84% @ 07-30 < the 3.10% line**, so this is an IT event and not S26's. ⇒ **Branch A's stated meaning: the 60-day run was pausing, not topping; M149's decaying-stock reading is falsified; and the IT-Neutral's implicit "wait for the 08-19→09-07 roll-off" defence is wrong for the whole stack.** ⚠ **The bracket's own control test does NOT corroborate a clean read**: DELL fell (+6.2 → +2.5) while HPE rose (+1.4 → +15.9), so "memory event" vs "IT-beta event" is **indistinguishable (C4)** — recorded, not decided. ⚠ **STX's own 07-30 move (+11.4%) sits inside its frozen ±14.6% no-information band**, so it may not be read as confirmation |
| **S35** regulated utilities | *branch B = median RS20 vs SPY **stays ≤ 0 through 2026-08-07***; branch A = **> 0 by 08-07** — **condition-settled** | ★★ **FIRED-A (against us) — and caught LATE** | **The median crossed to +0.39 on the settled 2026-07-29 close** (WEC −2.38 · ETR −3.84 · EXC +3.20 · SO +2.67 · XEL +0.39 · AEP −3.10 · D +5.63), independently reproduced here at **+0.39**. Branch B is a *"stays … through"* condition and **one crossing breaks it** ⇒ A fires, dated **2026-07-29**. ⚠⚠ **The 2026-07-30 run measured exactly +0.39, wrote *"the branch that says the 07-28 UW demote was WRONG is now live on settled data"*, and then filed it *"Not scored — window runs to 08-07."* That is the S39/S29 shape a THIRD time and the FIRST on the US desk.** ★ **Honest qualification, recorded with the verdict and NOT used to soften it**: the cross lasted **one session** — the median went **+0.39 (07-29) → −1.30 (07-30) → −4.89 (07-31)**. **The threshold is frozen and the verdict stands; the economic content is thin.** ⇒ **new defect D121: a sign test on a median with no persistence requirement fires on a single-session crossing that immediately reverts.** Branch A's stated meaning (a **W5** label collapse of the M26/M174 shape) is therefore **registered as fired but weakly evidenced**, and it is **directly contradicted by S47 below — which is the finding, not a problem to resolve** |
| **S47** the Utilities SPREAD | *branch B = the spread **narrows to +7.0pp or less by 2026-08-07*** — **condition-settled** | ★★ **FIRED-B (with the label)** | **(regulated-7 median RS20) − (AI-power-4 median RS20) = −4.89 − (−6.77) = +1.88pp on settled 2026-07-31**; the desk's own JSON gives **+2.3pp**. Registration state **+14.74pp** (07-29); path **+5.06 (07-24) → +2.44 (07-27) → +8.31 (07-28) → +14.74 (07-29) → +6.35 (07-30) → +1.88 (07-31)** — my recomputation reproduces the registration's own *"same construction on 07-28: +8.32pp"* to 0.01pp (**D5 ✅**). ⇒ **Branch B: the legs re-converged; one sector verdict is defensible and the N− stands on its own terms.** ★★ **S47's registration text pre-committed to this outcome: *"if this bracket and those two disagree, the disagreement is the finding."* It does disagree — S35-A says the label collapsed, S47-B says it re-converged — and both were scored on their own frozen thresholds within 48 hours of each other. ⇒ The honest joint reading is that BOTH thresholds are too twitchy for a two-day-old post-crash tape, not that one leg is right.** Both are handed to ROTATION as a *pair*, with **neither used alone** |
| **S25** RE OW− / DLR | *"**by 2026-08-08**, DLR RS20 vs SPY **falls below** that {PLD, AMT, WELL} median while the median stays positive"* — **condition-settled** | **FIRED (threshold met) — ⚠ but ZERO-INFORMATION** | Met on **four consecutive settled sessions**: 07-24 DLR **+2.82** < median +4.42 · 07-27 **+0.04** < +3.82 · 07-28 **+1.38** < +5.94 · 07-29 **+7.11** < +9.70, median positive throughout. **Reversed 07-30 (+10.11 > +5.59) and 07-31 (+8.48 > +3.41)** — post-fire context that does **not** un-fire a frozen threshold. ⚠⚠ **New defect D122, and it is the more important half of this row: the condition was ALREADY TRUE on the registration bar.** S25 was registered 2026-07-25 on numbers `asof 2026-07-24 settled`, and on that very bar DLR **+2.82 < +4.42** with the median positive. **A branch that is satisfied by the data on the day it is frozen cannot discriminate** — it records a state, not a forecast. **The verdict is logged as FIRED for the record and is NOT cited by any downstream stage as evidence about Real Estate** |
| **S36** Materials | *branch A = 5-day XLB excess vs SPY **still > 0** AND green count **still 0**, by 2026-08-05* — **condition-settled (persistence)** | **FIRED-B (with us)** | **XLB 5-day excess vs SPY = −2.72pp on settled 2026-07-31** (path +3.12 at registration → +5.46 → +4.21 → +2.21 → **−2.72**), and the **green count is still 0 of 12** on the 07-31 sweep. Branch A requires the excess to be **"still > 0"**; that persistence is broken ⇒ **B fires: the divergence resolved itself and the 07-27 move was noise.** ⚠⚠ **Consequence that runs against a decision this desk already took**: the 07-30 ROTATION moved **Materials UW → N** on the *disqualification* of A's green-count leg (M238/M273 — the 🟢 gate is a `vol_surge` artifact). **The surviving price leg has now settled the other way**, so the N sits on ground the bracket no longer supports. **Handed to ROTATION as an open re-argument, not as an instruction (P4)** |

### 3b. Recorded, not scored (annexes and reaction tests — pre-registered, so they cannot be re-read later)

- **S14-num** — MA's print-day move **+2.49% on 2026-07-30**, **inside the pre-declared ±3.9% band**
  ⇒ **NO INFORMATION**, exactly as pre-committed. It **may not be read as confirming the FIN OW.**
  S14 itself scores **2026-08-06** on cross-border volume + {MA, V, PYPL} RS20; all three are
  currently positive (**+6.0 / +0.8 / +25.5**), and the **{MA, V}-only** ANNEX reading agrees in sign.
  ⚠ **PYPL's +25.5 is still the Stripe merger-arb spread (S14-ANNEX / D50), not payments breadth.**
- **S46 reaction test** — AAPL **−7.35% on 07-31 vs the pre-declared ±3.3% band ⇒ OUTSIDE, the move
  is information.** Registered separately from the branch conditions (the **D28 fix**), so it is
  recorded here and not folded into a branch.
- **S32** was scored **AMBIGUOUS** by the 07-31 run and is **append-only closed**; this run does not
  re-score it. For the record only: **QQQ RS5 vs SPY = −0.55% on settled 07-31**, which is branch B's
  price leg — the percentile leg remains unreadable (**D104**).

### 3c. Checked and correctly NOT fired (the check is the record, not a skip)

| ID | Condition | Measured 07-31 settled | Status |
|---|---|---|---|
| **S31** XOM | A = RS20 **holds > +10% through 08-05** (a persistence condition, cannot fire early) · B = **≤ 0 by 08-05** | RS20 **+13.1** / RS60 −2.9 | **ARMED**, tracking A. Correct not to score |
| **S49** distillate crack | A = 5-session change **stays > 0 through 08-06** · B = **≤ −5.0 by 08-06** | **5-session change +1.066** (99.084 → 93.205 → **87.341**) | **ARMED.** ⚠⚠ **The buffer to branch B collapsed from +11.67 (07-29) → +3.05 → +1.07 in two sessions.** The **Russian diesel-ban expiry (07-31) is now past** and the bottleneck did not release on the day, but the *rate* is one session from B |
| **S24** AI-power | median RS20 **> 0 by 08-12** | **−6.77** (from −14.35) | **ARMED**, improving toward the line but 6.8pp away |
| **S42** capital goods | A = median **at or below 0 by 08-12** · B = **above 0 through** 08-12 AND ≥2 still 🟢 | median **+10.65**, CAT control **−14.9**, greens: ITW 🟢 only (1 of 4) on the 07-31 sweep | **ARMED**, tracking B on the median leg; ⚠ **B's second leg (≥2 of 4 still 🟢) is currently 1 of 4** |
| **S26 · S41** credit | HY OAS ≥ **3.10%** / IG line | **HY 2.84% · IG 0.80% @ 07-30** | **ARMED**, both inside. This also confirms the **invalidation clause on S30, S35, S42, S46, S47 did not trigger** |
| **S19 · S23 · S9** rates | numeric legs → 08-05 | **DGS2 4.23 · DGS10 4.68 @ 07-30 ⇒ 2s10s +0.45**; **DFII10 2.41** | **ARMED.** ★ The post-FOMC prints published: **2s10s +0.35 (07-28) → +0.45 (07-30) = a 10bp STEEPENING**, so **S23's ≤ +0.20 flattener line moved further away, not closer** — the second consecutive run in which this direction is corrected. **S9's 2.55% real-10y kill line is 14bp away.** ⚠ **No 07-31 curve print exists; no proxy substituted (D5)** |
| **S13 · S16 · S40** capex | → 08-12 / 09-30 | unchanged since 07-30 | **ARMED**; S13's registration defect (no cell for *"one holds while the other raises"*) stands, **S13 is NOT re-frozen** |
| **S5** KR semi exports | ~2026-08-11 | not due | **ARMED** |
| **S3 · S4 · S34 · S37 · S48** | 09/10, 09, CXMT ramp, 09-30, 09-30 | not due | **ARMED** |
| **S50** AMD/ANET | 2026-08-04 → 08-06 | not due | **ARMED** |
| **S51** NFP | 2026-08-07 → 08-10 | not due | **ARMED** |

### 3d. KR-owned rows this desk could not score, named rather than skipped (W1)

- **S22** (SK이터닉스 KKR SPA closing, event **2026-07-31**) — the 07-31 `industry_kr` run named it its
  **own #1 next-run scoring job** after the observable had not printed at its 09:1x KST re-check.
  Its observable is a **DART filing / domestic-news** read, which this desk's `--scope foreign`
  runtime cannot reach (**W1**). **Carried, assigned to KR, and this is its second HANDOVER — if the
  next KR run does not settle it, it is an `EXPIRED` row.**
- **S11** (FSC governance package) — **PENDING**, deadline **2026-08-06**; the 07-31 KR run recorded a
  third documented slip (간담회 cancelled, *"무기한 연기"*). **An `AMBIGUOUS` verdict at 08-06 is the
  likely outcome and the threshold will not be widened.**
- **S17 / S17-ANNEX** (SK hynix ADR premium) → **08-05**. **S18** already **FIRED-B** (07-31 KR run).

---

## 4. Still-armed scenarios and their dates

**US-owned**: S3 (~09/10) · S4 (~09) · S5 (08-11) · S8 (undated, **levels unscoreable per R30/D95 —
superseded in practice by S49**) · S9 · S19 · S23 · S31 (all → **08-05**) · S36 *(scored today)* ·
S49 · S50 (→ **08-06**) · S47 *(scored today)* (→ 08-07) · S25 *(scored today)* (→ 08-08) · S51
(→ 08-10) · S13 · S16 · S24 · S26 · S41 · S42 (→ **08-12**) · S46 (→ 08-13) · S34 · S37 · S40 · S48
(→ 09-30) · S32 (re-pull at the next fresh COT).
**KR-owned that this desk may not skip if they mature**: **S22 (07-31, overdue)** · S17 (→08-05) ·
S11 (→08-06).

**The next 96 hours are dense**: **08-04 MPC + AMD/ANET (S50)** · **08-05 PSX + the S9/S19/S23/S30/S31
window closes** · **08-06 S49, S50, S14, C7, S11** · **08-07 S35/S47 window + NFP (S51)**.

---

## 5. Ledger audit — both run, this HANDOVER

- **`reject_ledger.py due`** → `전체 87건 · 해소됨 28 · 부활조건 없는 레거시 **0** · 재확인일 도래/경과 **1**`.
  **The one due row was resolved this run, not carried**: **005490 POSCO홀딩스** (filed 07-24,
  `A.flow미도착`, recheck 07-24+). Re-pulled per the §4 rule
  (`module_flow 005490.KS --bench 069500.KS`): its `revives_if` is an **AND**, and **its first leg
  fails on measurement** — 20d investor actuals are **foreign +38.0만 · institution −16.8만 ·
  retail −21.3만**, i.e. **still foreign-only, with no institutional sign flip**; OBV distribution,
  **RS60 −41.1** vs the benchmark, short 0.11% float flat. **The second leg (a Korean steel tariff-rate
  finalisation) is a domestic observable and was NOT substituted (W1).** ⇒ **`resolve --outcome
  reaffirmed`** — stays out on fresh evidence rather than stale. ⚠ Ownership note: a KR name resolved
  by the US desk is permitted (ownership confers no exclusivity), and the resolution rests on a
  KIS/KRX **flow measurement**, not on a domestic-narrative read.
- **Legacy (no-`revives_if`) count = 0**, held at **0 for a 3rd consecutive run** (…→2→1→0→0→0).
  ⚠ **A clean `due` is not read as a healthy ledger** — the legacy trend line is the evidence, and it
  is holding rather than merely quiet.
- **`missed_ledger.py due`** → `전체 33건 · 해소됨 0 · 레거시 0 · 도래/경과 0` — nothing due.
  ⚠ Its `excess` sign is **inverted** relative to `reject_ledger`; **the two are never summed without
  aligning signs**. ⚠ Its `score` block still carries the seeded, **outcome-selected** first six rows
  and its class means are quoted as **accumulation, never as an edge** (D106).
- **Mechanical ledger cross-read** (`module_report_tags show`): the reconciliation gap is unchanged and
  structural — **28 real universe tickers are silently unindexable** (`_US_STOP`: A, AIG, ALL, C, CAT,
  CB, COST, D, F, FAST, GS, ICE, KR, LOW, MA, MET, MS, NOW, O, ON, PEG, PM, Q, SO, T, TT, V, WELL —
  **M152/M249**). **A zero from that tool on any of those names is `unknown` (C3), not "no coverage".**
  Of today's carried names this hits **D, MA, V, CB, CAT, SO, WELL, GS, ICE** directly.

---

## 6. Exposure state — inherited as SIZE CONTEXT only, never as an instruction (P4)

**`exposure_rule.py state` (settled) = `복귀` (RETURN), previous `방어`.** Target invested **90%**,
cash target **10%**. **Not a cold start** — 26 ledger rows on the backfilled path.

- **Fire basis, and the bar behind it is real**: 20d-high **−16.94%** ≤ −10.0 ∧ 20d-low **+24.17%**
  ≥ 3.0 ∧ volume **1.40×** ≥ 1.0 ∧ day **+24.17%** > 0. ⚠ The +24.17% day return is extraordinary
  and was verified directly against the price series — **069500.KS 87,635 (07-30) → 108,820 (07-31)**
  — i.e. a genuine post-crash rebound bar, not a data artifact. **The state machine is path-dependent,
  so a single rebound bar of that size moves the target a long way.**
- **Cash/selection split (n=1, live backfilled path):** total excess **−13.74pp = cash −6.86pp +
  selection −6.88pp**; NAV 0.76%, invested **52.7%** against a 90% target.
- 🚨 **Flags carried into BET/ALPHA as size context:** (i) **🚨🚨 `TIMEFOLIO_EXECUTE=1` is ARMED** —
  `--execute` would submit live orders; **human confirmation required (P5), and no stage of this run
  passes that flag.** (ii) **🚨 band breach −37.3pp** (invested far below the 복귀 target).
  (iii) ⚠ **the invested % came from a live intraday KIS bar and the account-query legs are absent**,
  so the split is `[inferred]` at **n = 1**.
- ⚠⚠ **This is a KR-benchmark instrument.** It is the desk's only exposure state machine and is
  carried as such, but **it is not a US size read**, and no US tilt is derived from it (**W1**).

---

## 7. Stale flags

| Series / object | State | Consequence |
|---|---|---|
| **COT positioning** (`us_flow --cot`) | Byte-identical to M125's **2026-07-21** read as of the 07-31 run ⇒ **12+ calendar days stale**, across an FOMC and six mega-cap prints. **D104: the tool prints no `asof`**, so stale is indistinguishable from fresh | Made **S32 unscoreable**. **SWEEP must hand-match the snapshot before quoting it** |
| **FRED daily curve** | DGS2/DGS10/DGS30/DFII10/HY/IG all print to **2026-07-30**; T10YIE to **07-31** ⇒ **D103 reproduces — the two-series rule is unsatisfiable on the latest print** | Blocks the numeric legs of **S19/S23/S9**. **No proxy substituted (D5)** |
| **DTWEXBGS** (S12's frozen observable) | **120.7105 @ 2026-07-24** — 9 calendar days unprinted, the same chronic lag that ran S12 to five carries | Any dollar claim this run makes is **`[unknown]` (C3)** |
| **07-31 sweep JSON** | **`asof: 2026-07-31`** — a same-day live-bar stamp breaking the prior one-session-lag convention (**D74**) | **Every bracket leg in §3 was re-derived from settled closes and cross-checked (D5).** SWEEP must re-run on settled data |
| **STANDING_VIEW_US §3a** | Rows are **asof 07-29 / 07-30**; the 07-31 US run wrote none (§0) | This run's §2 read is the live substitute, and the writeback repairs it |
| **042700 한미반도체** §3b | asof **07-22**, `[inferred]`, carried in a **W2**-shaped form (a rack-correlation table never measured) | KR-side; flagged for the KR desk again |
| **000660 ADR suspension** | Nominal clear date (07-29 two-way conversion) **passed but did NOT clear** — R13's 2.5% ceiling extends it; **S17** replaces the date with the daily premium | **NOT converted to a dig** (a *cleared* suspension would be; this one is still live). The pre-07-29 series stays **not retroactively clean (D1)** |
| **`ic_ledger`** | **180 rows, `market=kr` only — the US desk has NO IC scoreboard at all** | ★ Standing item reported every run: **`vol_surge` h=1 IC −0.044, t(NW) −2.08, n_eff 14, 필요n 14 (reached)**, with h=5 the same sign (−0.046) but **n_eff 1.8 ⇒ unquotable**. **Bonferroni on 21 tests requires \|t\| > 2.8, so nothing is confirmed** — and **`sector_flow`'s 🟢 verdict still weights `vol_surge` POSITIVELY.** **The gate is not flipped before the sign clears (P4).** ⚠ **That this desk's own market has zero IC rows is itself the finding** — the US board is ranked every day by axes with no scoreboard behind them |

---

## 8. RESEARCH triggers loaded as binding constraints (not a summary), and which stage each binds

| Group | Fires when | Binds |
|---|---|---|
| **C** — C1 baseline · C2 both halves · C3 unknown column · C4 "indistinguishable" · C5 arbitrary choice | you cite a number | **MACRO · every stage** |
| **S** — S1 date-fold · S2 diagnose the null · S3 power first · S4 in-sample≠done · S5 short samples · S6 future labels | you make a statistical claim | **any stage citing a test** |
| **D** — D1 second venue · D2 proxy sign · D3 signed vs unsigned · D4 regime contamination · D5 cross-provider · **D6 signal grade (A/B/C — OBV is C)** | you read data | **SWEEP · ALPHA · L2 indicators · L2 money_trail** |
| **W** — W1 cross-market transfer · W2 inherited lead/lag · W3 real≠profitable · W4 name the customers · W5 sub-sector dispersion · W6 reader's-market spine | you write a conclusion | **DEEP · BET · ROTATION** |
| **L** — L1 second derivative · L2 peak-margin trap · L3 branch information content | lenses, not triggers | **DEEP · PREMORTEM** |

**Binding notes specific to today**: **S1 (n≈1)** binds §3 hardest — **S30, S35, S47 and S36 all
fired on one or two settled sessions of a post-crash tape**, and every one of those brackets declared
its own n≈1 at registration. **C4** binds S30's control-pair split. **W5** binds any Utilities or IT
verdict ROTATION writes. **L2 is unrunnable on the majority of the sheet (M233: 11 of 18 names)**, so
**no cheapness claim may be made on VLO, XOM, CSX, UNP, NSC, PLD, RTX, TMO, T, GM or CAT.**

**Open code defects carried forward — all need human approval to change code, none silently
re-discovered**: **D9** (holdco concentration in risk-unit clustering) · **D10** (news-body
boilerplate) · **D17** (`drift` not on the remote API allow-list) · **D18** (`catalyst_calendar`
misses same-day binaries — 11th consecutive run) · **D19** (`action_bracket` still prints R8's
retracted PSX rationale — 7th run) · **D102** · **D103** · **D104** · **D105** · **D106**.
**New this run**: **D121** (a sign test with no persistence requirement fires on a one-session
crossing that immediately reverts — S35) · **D122** (**a branch condition already satisfied by the
data on its own registration bar — S25; the bracket recorded a state, not a forecast**) ·
**D123** (a bracket whose grid mixes a fundamental observable with a price-reaction band, so two
branches can be true at once — S21, the D28 family's third instance).

---

## 9. Dig list ranked for today (candidate DEEP assignments)

Ranked by **live bracket activity × how badly this run's own scoring hurt a carried verdict**.

1. **IT — memory / equipment suppliers (MU · STX · WDC · AMAT · LRCX · KLAC).** ★★ **S30 FIRED-A
   against the desk today.** The IT-Neutral's stated defence (wait for the 08-19→09-07 roll-off) is
   the thing the branch says is wrong, and **the stack did not move as one**: STX/WDC turned violently
   on 07-30 while AMAT/LRCX/KLAC did not, and the DELL/HPE control **split**. **C8 is live in exactly
   the form it was written.** ⚠ And the regime call's own channel gained a third OEM read-through
   (**AAPL GM guide 47–48% vs 50.1%**) pointing the *other* way on margins. **Highest-activity node.**
2. **Energy / refining (VLO · MPC · PSX · XOM) — and it is now a commodity emergency, not a tilt
   question.** On settled one-source daily bars the **3-2-1 crack fell 71.860 (07-29) → 67.313 →
   59.865 (07-31), i.e. −16.7% in two sessions**, driven by **gasoline (RB 3.398 → 3.114, −8.4%)**
   while crude *rose*. **S49's 5-session distillate change is +1.066, one session from its −5.0
   branch-B line.** ⚠⚠ **S21's own cross-check KPI — "the settled 3-2-1 crack holding ≥65 through
   08-06 invalidates branch A's read-across to refining" — reads 59.865 on the one named daily
   source, i.e. below 65. ⚠ But it is an ABSOLUTE LEVEL, and R30/D95 measured absolute crack levels
   to differ by 5.80 points across bar granularity ⇒ the correct statement is that S21's cross-check
   KPI is itself UNSCOREABLE on this data (C3), not that it failed.** Either way the invalidation
   cannot be asserted. **C4 (margin vs war premium) and W4 (name the refiners' customers)
   are the open tests.** ⚠ **Absolute crack levels remain granularity-contaminated (R30/D95) — DEEP
   must argue on changes, one bar type, one named source.**
3. **Utilities — and the mandate is now a contradiction this desk created itself.** **S35 FIRED-A
   (the label collapsed) and S47 FIRED-B (the legs re-converged) within 48 hours, on the same seven
   names.** S47's registration pre-committed that **the disagreement is the finding**. The DEEP
   question is not "which leg wins" but **"is a 20-day RS median on a post-crash tape a usable
   instrument at all"** — which is D121's general form.
4. **Materials.** **S36 FIRED-B**, which argues *back toward* the UW that the 07-30 ROTATION had
   already abandoned (it moved UW → N on the disqualification of the green-count leg). **The N now
   sits on ground the bracket no longer supports** and needs re-argument on a surviving reason —
   the same shape as **R32** did to the Financials OW last week.
5. *(secondary)* **Financials.** **R32 killed the OW's "breadth-led" reason**; the tape-level OW
   survives only on the **insurance node**. The 07-31 sweep gives FIN **wflow +0.163 / eqflow +0.121,
   3🟢 / 4🔴 of 47, delta −0.222** — **the gap is mega-cap-led again**, so the retracted reason has
   not been replaced. **S14 (08-06), S23, S26, S41 all touch it.**
6. *(secondary)* **Health Care C7** — **zero greens of 32 and breadth 0.00 on the 07-31 sweep**, so
   the "money without narrative" gap has closed from the money side. ⚠ **Its resolving observable's
   block definition (TMO vs AMGN) was never written down (C5) — a human must fix that before the
   08-06 reading is scoreable.**

**D9 / D10 carried forward as open code defects** — both need human approval to change code.

### 9b. `RESEARCH.md` Part C surfaced — the HANDOVER-owned digs, and what this run did with them

| # | Dig | Owner | Status this run |
|---|---|---|---|
| **D4** | *Score S1–S5 (and every registered bracket) as their dates pass — "unscored scenarios are how a desk keeps wins and forgets losses."* | **HANDOVER** | ✅ **Executed, and it is the whole of §3.** Six verdicts, three of them on conditions met days ago. **S5 is the only S1–S5 row still open (event ~08-11).** |
| **D6** | *Re-run the 000660 flow read after 2026-07-29.* | **HANDOVER** | ⚠ **Executed as a check and correctly produced NO read**: the 07-29 conversion window **passed without clearing** (**R13** — the ceiling is 2.5%, not 25%), so the suspension is extended and **S17** replaces the date with the daily premium. **A suspension that has not cleared is not converted into a dig (§7).** |
| **D1 · D3 · D8 · D22** | mechanism / lead-lag claims the standing view carries as `[inferred]` | **DEEP · MACRO** | **Untested, carried, and named** — per **W2** each is cheap to test and expensive to keep assuming. **None is cited as evidence anywhere in this HANDOVER.** |
| **D5** | 009150 — resolve C2 | **DEEP (KR)** | KR-side; **C2's mechanism closed, its persistence question runs to the 08-22 kill line.** |
| **D11 · D15 · D16 · D33** | the C-grade-veto defect · PLAY23 (closed 07-31) · the estimate-snapshot series · `REPORT/` not date-partitioned | mixed | Carried unchanged; **D11 is the code-level statement of C9/M144's `vol_surge` mechanism, now measured on two markets and six dates.** |

---

*asof 2026-08-02 · industry_US HANDOVER · **scored this run: S21 FIRED-C · S30 FIRED-A · S35 FIRED-A
(late, dated 07-29) · S47 FIRED-B · S25 FIRED (zero-information) · S36 FIRED-B** · recorded: S14-num
no-information, S46 reaction outside band · resolved: **005490 reaffirmed** · reject legacy count 0
(3rd run) · missed due 0 · exposure `복귀` / target 90% / band breach −37.3pp 🚨 / EXECUTE armed 🚨🚨 ·
**process failure named: the 2026-07-31 `industry_US` carry writeback is missing and is repaired by
this run**. No buy/sell language, no sizing (P4). `handoff/*.md` writeback occurs at run end
(append-only for §5).*

---

# ADDENDUM — SECOND SCHEDULED FIRE, 2026-08-02 22:38 KST (append-only; nothing above is edited)

## 1 · What happened, and what was deliberately NOT done

The `industry-us` scheduled task fired a **second time on the same calendar day**, six minutes after
the first run's last write. State at 22:38, all verified on disk before anything was written:

| Evidence | Reading |
|---|---|
| `llm_outputs/2026-08-02/industry_US/` | **14 files, complete** — all 10 stages' outputs present (HANDOVER → DRIFT) |
| `MACRO_REPORT.md §K` | DRIFT ADDENDUM written 22:32 — stage 10/10 genuinely executed |
| `REPORT/industry_US/` | 12 finalized reports copied **22:36** |
| `module_report_tags show` | ledger `갱신: 2026-08-02T22:36:37 · 37 reports · 231 tickers` — handoff step done |
| `handoff/*.md` | US carry written back 22:32–22:36 (`SCENARIOS_US` 22:32 · `STANDING_VIEW` 22:33 · `STANDING_VIEW_US` 22:35 · `RESEARCH` 22:36) |
| `report_lint.py` on all 7 written reports | **0 findings** (C1 · C2 · S6 · D6) |
| Calendar | **2026-08-02 is a Sunday** — no US session between the two fires; **zero new market data exists** |

⇒ **The pipeline was NOT re-run.** Per the desk's own same-day collision rule (2026-06-30: *a
completed file is never clobbered; a second same-day pass may only APPEND breadth*), re-running would
have overwritten twelve finished reports with a re-derivation built on **identical inputs** — pure
loss. This second fire is recorded as a **verification pass**, and its one substantive finding is §2.

⚠ **One side effect, caused and repaired by this pass**: `--start` reset the runner checkpoint
`out/pipeline_runs/industry_us.json` to `stage 1/10, passed=[false ×10]`, erasing the completed run's
record. It was restored to `stage 10/10, passed=[true ×10]` — which is what the on-disk evidence
above supports. **A `--start` on an already-complete same-day run is destructive to the checkpoint and
nothing warns about it.**

## 2 ★★ · A HANDOVER EXIT-CHECK item the first run skipped — the budget reading was never taken

`handoff/README.md` makes the size reading a **HANDOVER-time obligation**: *"Run
`handoff_compact.py --budget-only` at HANDOVER; a breach is a **finding to report**, not an error."*
The first run's `HANDOVER.md` contains **no budget line at all** (grepped: zero hits for
`budget` / `OVER by` / `handoff_compact`). The `industry_kr` run reported its reading at 22:0x; the
`industry_US` run did not — so the number below has **never been reported by this desk in its
post-writeback state**:

```
US run reads   631.9 KB   budget 250 KB   OVER by 382 KB
  RESEARCH.md        224.6 KB  (budget  85) — the largest single breach, still never compacted
  STANDING_VIEW_US   133.5 KB  (budget  50)
  SCENARIOS_US       137.8 KB  (budget  50)
  STANDING_VIEW       87.1 KB  (budget  45)
  SCENARIOS           37.4 KB  (budget  20)
  §2 fact rows: 254   avg 0.52 KB/row   (rule ≤ 0.35)
```

★ **The trend is the finding, and this is now its third consecutive run.** US read:
**437.7 (07-30) → 523.6 (07-31) → 590.8 (08-02, measured by the KR run BEFORE the US writeback) →
631.9 (08-02, after it)**. ⇒ **this single `industry_US` writeback added +41.1 KB** (8 fact rows
M301–M308-class, 8 digs D121–D128, six §3a rewrites, two brackets S52/S53, six scoring rows), and the
run that produced it **did not read its own meter**. The KR run's warning — *"at this rate the KR read
passes 560 KB next run"* — is understated for the US side, which crossed **630 KB today**.

⚠ **Nothing was compacted by this pass, deliberately.** `README.md` is explicit that the archive
*move* is mechanically safe but **choosing what is still load-bearing is not a mechanical call**, and
P4 forbids an unattended run from making that judgment across five files. **Reported, not fixed** —
the same disposition the KR run took, now with the post-writeback number attached.

## 3 · What this ADDENDUM does NOT change

- **No proposition, sector verdict, DEEP pick, bracket, or freshness tag is touched.** The 11-sector
  line (`ENRG OW · FIN OW− · IT N · INDU N · … · MATR UW · UTIL UW−`), the 5 DEEP files, S52/S53 and
  the §B-TAGS block all stand exactly as the first run wrote them.
- **No scenario is re-scored** — no observable moved on a closed Sunday market.
- **No new dig ID is assigned**, on purpose: **D128** measured this run that IDs must be checked at
  *write* time, and a second concurrent process assigning D-IDs is precisely that failure. This is
  filed as a reported breach, not a numbered dig.

*Second fire 2026-08-02 22:38 KST · verification only · zero buy/sell, zero sizing (P4) · append-only.*
