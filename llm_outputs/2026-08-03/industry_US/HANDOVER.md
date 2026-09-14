# HANDOVER — industry_US · 2026-08-03 (Mon) · STAGE 1, runs before MACRO

## 0. Run clock, and the single fact that governs this whole run

**09:13 ET · 22:13 KST · 17 minutes BEFORE the US open.**

This is the cleanest clock this desk has had. **No live US bar exists yet**, so D74 (unsettled-bar
contamination) cannot fire on the price axis — the failure that has fired on four separate US runs
(M171 · M204 · M247 · and the S46 near-mis-score at M-block 08-02) is structurally unavailable today.

**And that same fact is this run's central constraint, stated up front rather than discovered at
SWEEP:**

| | |
|---|---|
| Last settled US session | **2026-07-31 (Fri)** |
| Last settled US session used by the **prior** run (08-02, Sun) | **2026-07-31 (Fri)** |
| ⇒ New settled US price information since the last run | **ZERO** |

⚠⚠ **This run has no new US tape.** Any stage that reports a "change" in a US price, flow, RS or
short reading against the 08-02 run is reporting a **recomputation artifact, not a market move.**
The honest consequences, pre-committed here before SWEEP runs:

1. **SWEEP must reproduce `SECTOR_FLOW_US.json` from 08-02**, and a failure to reproduce is a finding
   about the instrument (D126's oscillating `velocity` join), never about the market.
2. **ROTATION may not change a sector direction on price** this run. It changed zero directions on
   the 08-03 `industry_kr` run for the same reason (a partial bar); here the reason is stronger —
   the bar is not partial, it is *absent*.
3. What **is** new and is therefore where this run's value has to come from: **(a)** the settled KR
   08-03 session, which fired two condition-settled brackets (§2); **(b)** FRED prints published
   since 07-31; **(c)** the foreign news pool over the 08-01→08-03 weekend; **(d)** the forward
   calendar, which is dense — **MPC · AMD · ANET · S50 · S53 all land 08-04, i.e. tomorrow.**

---

## 1. Inheritance read — what was opened

| File | Read | Note |
|---|---|---|
| `handoff/STANDING_VIEW.md` (SHARED SPINE) | ✅ in full | §1 regime call · §2 seed chain M1–M19 · §4 asymmetry · **§5 retracted ledger R1–R41** · §6 contradictions C1–C10 |
| `handoff/STANDING_VIEW_US.md` | ✅ in full | §2 US rows M22–M320 · §3a per-name registry |
| `handoff/SCENARIOS.md` (SHARED SPINE) | ✅ in full | legend · scoring rules · master scoring log · **master index, 64 brackets (42 US · 22 KR)** |
| `handoff/SCENARIOS_US.md` | ✅ | all 42 US brackets, status-scanned; the live ones read in full |
| **`handoff/SCENARIOS_KR.md`** | ✅ **opened deliberately** | **S43 · S44 · S47-KR are past-conditioned or past-dated and are THIS run's to score** — the spine's "ownership confers no exclusivity" rule (§2) |
| `handoff/RESEARCH.md` | ✅ Part A triggers · Part B lenses · Part C dig list | loaded as **binding constraints**, not summarized (§6) |
| `module_report_tags show` | ✅ | reconciled against belief in §5 |

### §5 retracted ledger read BEFORE forming any view — the four that bind this run

- **R38** — *"~8 of UNP's 12 revenue growth points are fuel surcharge"* is dead (the 10-K shows
  surcharge revenue **DECLINED $218M**). ⇒ **no stage may re-argue the rail node as "the Energy bet
  through another income statement" on that magnitude.** The ~2-month lag mechanism survives.
- **R39** — *"XOM is 0% refining"* is dead (its own segment printed **$4.1–5.5bn, a four-year high**).
  ⇒ the 🚨 rank-2 Energy GAP is computed on a **wrong registry tag**; its magnitude is `unknown` (C3)
  until a human corrects the registry. **CYCLE_EXPOSURE's Energy number may not be quoted as a level.**
- **R40** — the **"regulated seven" basket is contaminated**: D is a merger-arb security (NEE/D
  DEFM14A, 07-28), correlating **+0.89 with NEE and −0.21 with SPY**. ⇒ **neither S35's FIRED-A nor
  S47's FIRED-B may be cited downstream as evidence about Utilities.** On the regulated-SIX the UW− is
  *stronger*, not weaker.
- **R41** *(KR-owned, but it is a method retraction and therefore cross-market)* — *"the largest
  crowded short this desk has measured"* is withdrawn: **the superlative was a property of the sample,
  not the market.** ⇒ **this US run may not write "the largest / the maximum / the most X on the
  board" about any short balance, flow score or spread unless it has actually scanned the
  distribution.** Correct form: *"the maximum among names I looked at"* (C1/C5).

⚠ Cross-check performed: **no claim formed in this HANDOVER matches a retracted entry.** The one
that came closest — reading today's KR crash through a "foreign capital flight" frame — is exactly
what **S44 was registered to test**, and it is scored below rather than assumed.

---

## 2. ★★★ Scenarios — TWO condition-settled brackets fired today, and the desk was 4 hours from missing both

> **This is the section the stage exists for.** The desk has now logged this failure shape **three
> times** (S39 07-30 · S29 07-31 · and the S22 hand-forward). The rule that came out of it —
> *"classify every ARMED row as date-settled or condition-settled, and check every condition-settled
> row against today's data"* — has run for three consecutive KR runs. **This is its first US
> execution, and it caught two rows on its first pass.**

### 2a. The trigger

**`069500.KS` settled 2026-08-03 at 99,105 = −8.928%.** The condition shared by **S43** and **S44** is
*"the next session where `069500.KS` closes ≤ −3.0%"*. It has been unmet since registration
(07-27 +1.283 · 07-28 −11.190 · 07-29 −6.344 · 07-30 −2.199 · 07-31 +24.174 — the −11.19 and −6.34
predate registration). **Today it is met, by 5.9pp of margin.**

⚠ **The `industry_kr` run of the same date could not have caught this**: it ran at **08:59 KST**,
one minute before the KR open, and correctly recorded the condition as unmet on the data that
existed then. **The condition was met at the 15:30 KST close, seven hours after that run ended.**
This is not a KR-desk failure — it is precisely the case the shared-spine rule was written for.

### 2b. S43 — ★★ **VOID**, and the anti-signal is why (it was checked FIRST)

**S43** (registered 07-30, KR MACRO): *is the pharma shelter property a NAME or a SECTOR?*
Observable: 068270's beta-adjusted residual vs `069500.KS` on the trigger session.

**Anti-signal, checked before the observable** (the S46-KR precedent): *"a 068270-specific disclosure
(trial data, an order, an equity raise) landing on that session ⇒ the low-beta axis and the news axis
become inseparable ⇒ score `VOID` and re-register on a different session."*

`[PRIMARY — DART]` **rcpNo 20260803800514, filed 2026-08-03 by 셀트리온:**
「**투자판단관련주요경영사항** (CTP44(다잘렉스 바이오시밀러) 한국 임상 3상 시험계획…)」
— a company-specific material disclosure of a **Phase 3 clinical trial plan, landing on the trigger
session itself.** Separately, `주식등의대량보유상황보고서(약식)` from **국민연금공단** also filed
2026-08-03.

⇒ **S43 = `VOID`.** Re-register on a different qualifying session.

⚠⚠ **The interpretive edge is stated rather than resolved in the desk's favour.** The registration's
parenthetical says *"trial data"*, and this is a trial **plan**, not results. But the governing phrase
is *"a 068270-specific disclosure"*, and the stated **mechanism** — the price and news axes becoming
inseparable — applies exactly. **Narrowing an anti-signal after the print to keep a bracket scoreable
is the same violation as widening a threshold after the print** (L3 `scenario_score`). Scored VOID.

★★★ **And this matters, because the observable had already been computed and it would have scored
the other way:**

| Name | 08-03 return | excess vs bench | β (60 sess. ending 07-31) | R² | **residual** | own-window σ |
|---|---|---|---|---|---|---|
| **068270** 셀트리온 | −2.410% | +6.517pp | **0.136** | 0.067 | **−1.194pp** | **2.923pp** |
| 207940 삼성바이오 | −4.175% | +4.753pp | 0.099 | 0.031 | −3.289pp | 3.214pp |
| 128940 한미약품 | +3.598% | +12.526pp | 0.386 | 0.155 | +7.045pp | 5.199pp |
| 326030 SK바이오팜 | −0.759% | +8.168pp | 0.273 | 0.188 | +1.676pp | 3.271pp |

On the frozen arithmetic that is **branch B** (068270 residual < 0) — *"the two-session run was its own
news, not shelter; the shelter claim dies outright and M-16 dies with it."* **That verdict is NOT
recorded**, because the anti-signal fires first and a VOID is not a B.

★ **S43-ANNEX's requirement executed anyway, because it is the more useful output** (the annex asked
for the estimator's own error to be measured *in the same pass*, and explicitly forbade importing the
staples σ — a W1 violation inside one market):

- **068270's own-window residual σ = 2.923pp. The would-be verdict was −1.194pp — 0.41σ.**
  **The bracket's ±1.0pp band sits entirely inside its own estimator's noise**, exactly as
  S43-ANNEX predicted from a *different* cohort. ⇒ **D93 confirmed prospectively, and this is the
  second KR instance of L3-bis** (a bracket whose observable can settle on frozen mechanics).
- **Beta sweep — the verdict flips sign inside the plausible β range:** β 0.00 → −2.410 · **0.24
  (registration) → −0.268** · 0.30 → **+0.268** · 0.40 → +1.161 · 0.50 → +2.054.
  ⇒ **branch B holds at the frozen β 0.24 and at the measured β 0.136, but dies at β ≥ 0.27.**
  R² is **0.067** — the regression is barely a regression.
- ⇒ **Even without the anti-signal this bracket could not have carried a conclusion.** Recorded as a
  registration-quality finding, not as a market finding.

### 2c. S44 — ★★ **FIRED-B**, and it retracts a carried proposition

**S44** (registered 07-30, KR MACRO): *who sold? the crash's agent, read off the KRW sign.*
Two legs, reported **separately and never merged**, per registration.

**Leg 1 — won/dollar close direction on the trigger session** `[measured, yfinance KRW=X]`:
**1,420.60 (07-31) → 1,428.08 (08-03) = +0.527% ⇒ the won WEAKENED.**

| Branch | Condition | Fired? |
|---|---|---|
| A | index ≤ −3% ∧ won **stronger** ∧ DTWEXBGS > −1.0% | ❌ won weakened |
| **B** | **index ≤ −3% ∧ won weaker** | ✅ **FIRED** |
| C | won stronger but DTWEXBGS ≤ −1.0% | ❌ premise absent |

⇒ **`FIRED-B` — "ordinary capital-flight shape ⇒ M-15 is retracted."**

**Leg 2 — `DTWEXBGS`, reported separately and NOT used to score** (branch B does not require it):
`[FRED]` the series **still stops at 2026-07-24 = 120.7105 — unprinted for 10 calendar days**, the
fourth consecutive run to record it as pending. Next expected ~08-04.

⚠ **Three caveats recorded WITHOUT moving the threshold:**
1. **`KRW=X` is a 24-hour OTC quote, not a KRX-session close.** The registration said *"the won/dollar
   close direction"* without naming a venue — a **registration defect, logged as a new dig**, not a
   reason to substitute a different series now. Direction is corroborated by **DXY 99.800 → 99.783,
   i.e. essentially flat (−0.02%)** ⇒ the won weakened against a **stationary** dollar, which
   strengthens rather than weakens the reading (it is not a dollar-side artifact — the exact
   alternative branch C exists to catch).
2. **n = 1 (S1)**, as the registration itself pre-stated (*"score the sign pair, not the magnitude"*).
   The magnitude (+0.53%) is small next to 07-31's −1.50% strengthening and is **not** cited.
3. The registration's supporting evidence for the *domestic-liquidation* alternative (credit-financing
   balance, 증안펀드, term deposits) is **not re-litigated** — branch B is scored on the frozen sign
   pair, and the surviving evidence does not get to override a pre-registered observable.

### 2d. S47-KR — **still NOT scoreable, and NOT `EXPIRED`** (carried, with the reason)

The 08-03 `industry_kr` run named this *"the 2026-08-04 run's #1 scoring job"*: read
「재고관련이익 ÷ 정유부문 영업이익」 for 010950 S-Oil from the IR pack or the 반기보고서, score
A(≥50%) / B(<50%) / C(non-disclosure), **and do not substitute an estimate (D95)**.

**Status at this run's clock:** the 09:29 KST 공정공시 (`rcpNo 20260803800274`) carries **no segment
split and no inventory-gain figure** — verified by the KR run at five separate clocks. The 10:00 KST
conference-call pack is the carrier. **This US desk did not reach the IR pack**, and per D95 an
estimate is not admissible. ⇒ **carried forward to the 2026-08-04 `industry_kr` run as its #1 job,
exactly as that run designated it. Not `EXPIRED`, and named here so the hand-forward is visible in
both files rather than living only in the KR run's own report.**

### 2e. Every other ARMED row — classified and checked

**Date-settled, all future — no action, dates recorded:**
S3 (~09/10) · S4 (~09 late) · S5 (**08-11**, KR semi exports 1–10 Aug) · S9 (**08-05**) · S13 (08-12) ·
S14/S14-num (**08-06**) · S16 (08-05) · S19 (08-05) · S23 (08-05) · S24 (08-12) · S25 (08-08) ·
S26 (08-12) · S30 (**08-05**) · S31 (**08-05**) · S36 (08-05) · S37 (09-30) · S40 (09-30) ·
S41 (08-12) · S42 (08-12) · S46 (08-13) · S48 (09-30) · S49 (**08-06**) · S50 (**08-06**, AMD/ANET
print **08-04**) · S51 (08-10, NFP 08-07) · S53 (**08-05**, MPC **08-04** + PSX **08-05**).

**Condition-settled — checked against today's data, this is the check being performed not skipped:**

| ID | Condition | Status at 09:13 ET |
|---|---|---|
| **S8** | Hormuz "Strait open" — **undated `[blank]`** | ⚠ **superseded in practice by S49** (a crack observable that survives its own data), and **R30/D95 measured S8's own 60/84 kill lines to be un-scoreable on this data**. **Carried as un-scoreable, named rather than dropped — this is its 2nd consecutive run in that state and it should be formally `VOID`ed or re-registered by a human.** |
| **S49** | crack **CHANGE** ≤ −5.0 (branch B) | ⚠ **M309 measured the 3-2-1's own 5-session rate already NEGATIVE (+4.995 → +0.822 → −4.439) at 07-31 and said branch B was "one to two sessions away".** **No new settled bar exists** ⇒ unchanged, still ARMED, **and it is the single most likely bracket to fire on the 08-03 close tonight.** Flagged to MACRO. |
| **S52** | Iran: dated Strait reopening **vs** resumed strikes on Iranian energy infrastructure | Condition-settled ≤48h class. **Checked at MACRO with the fresh foreign pool** (this stage does not pull news). Window 08-06. |
| **S26 / S41** | credit lines HY OAS ≥3.10 / IG ≥0.90 | last settled `[FRED]` reads carried at **HY 2.84 · IG 0.81** ⇒ buffers **26bp / 9bp**. **Re-pulled at MACRO** — FRED may have published since 07-31. |
| **S9** | real 10y ≥ 2.55 kill line | **DFII10 2.41, flat for three prints** ⇒ 14bp away. Re-pulled at MACRO. |
| **S23** | 2s10s ≤ +0.20 | derived **+0.45** at 07-30 ⇒ **25bp away and receding.** Re-pulled at MACRO. |
| **S43 · S44** | `069500.KS` ≤ −3.0% | ✅ **FIRED TODAY — see §2b/§2c.** |

**`EXPIRED` = 0 · silent skips = 0.**

---

## 3. Both ledgers audited — and both are clean, which is itself reported rather than assumed

```
reject_ledger.py due  → 96 rows · 29 resolved · legacy (no revives_if) 0 · recheck-date due 0
missed_ledger.py due  → 42 rows ·  0 resolved · legacy (no enters_if)  0 · recheck-date due 0
```

- **Rejection ledger: legacy count 0 for a 6th consecutive run.** The practice that took it from
  **24/25 empty** (2026-07-23) to zero is holding. ⚠ Per `carryover.md` §3b the correct reading of a
  clean `due` is *not* "the ledger is healthy" — it is **"the legacy count is 0 and the next recheck
  dates are 08-12/08-13/08-16"**, i.e. the audit load is *scheduled*, not *absent*.
- **Missed ledger: 42 rows, 0 legacy, 0 due.** ⚠ **`resolved = 0 of 42` is the number to watch** — no
  missed-entry row has yet been closed by any run. The first rechecks fall **08-14 (KR: 073240,
  000150)** and **08-16 (US: ADM, CTAS)**. If those pass unresolved, that is the same process failure
  on the opportunity-cost side that the rejection ledger already learned once.
- ⚠ **Signs are opposite and are NOT summed** (`excess > 0` = *rejection cost us* vs *missing cost
  us*). No combined figure appears anywhere in this run.
- ⚠ **`missed_ledger score`'s first six rows remain `outcome_selected`** (harvested from
  `leak_scan --top`, i.e. from names that had already risen). Per D106 those class means are
  **accumulation, never an edge**, and are not quoted in this run.

---

## 4. Exposure state — carried as SIZE CONTEXT for BET/ALPHA

```
python -X utf8 scripts/exposure_rule.py state   → 2026-08-03 (settled), bench 069500.KS
```

| Field | Value |
|---|---|
| Rule state | **복귀 (복귀 held)** — with `⚠전이 보류(복귀→방어) — 최소유지 1/3세션` |
| Bench | close 99,105 · day **−8.928%** · vs 20d high **−23.84%** · vs 20d low **+13.09%** · volume 1.093× |
| Target invested | **90%** |
| Current invested | **54.2%** |
| **Band gap** | **🚨 −35.8pp (밴드이탈)** |
| Ledger depth | **27 rows**, of which only **n=2 carry a usable decomposition** |

**What this means for the stages that pick names**, stated as the L3 unit requires rather than left
implicit: the rule says **복귀**, which is the state whose stated implication is *"신규·증량 후보가
필요하다 — 목표 비중이 크게 오르므로 BET 이 후보를 못 내면 현금이 남는다."* The book is **35.8pp
below** that target.

⚠⚠ **Four caveats, and they are load-bearing:**
1. **The transition is 보류, not absent.** The engine wants to move **복귀 → 방어** and is holding it
   for the 3-session minimum (1/3 elapsed). Per the L3 unit: *"보류를 '조건 미충족'으로 읽지 마라 —
   조건은 충족됐고 집행만 미룬 것이다."* ⇒ **the 90% target is the state the rule is LEAVING.**
   A stage that reads "복귀 ⇒ go wide" off this line is reading a state with one session of life left.
2. **This is the KR book's exposure rule** (`069500.KS`, KR contest bands). It is carried here as
   context because it is the desk's only exposure instrument — **it is not a US sizing input**, and
   no US stage may size off it (**W1**).
3. **Cumulative decomposition is n=2**: total excess **−7.09pp = cash −2.48pp + selection −4.60pp**.
   ⚠ **n=2 is indistinguishable from zero (C4)** and is quoted only to keep the counter visible.
4. 🚨 **`ARMED(TIMEFOLIO_EXECUTE=1)` is set in the environment.** This is a **read-only research run**
   and issues **no orders, no `--execute`, and no order-desk staging** — recorded because the flag
   being armed at all is a standing condition a human should see.

**Not cold-starting** (27 rows present) ⇒ the verdict is quotable, unlike the 07-31 case.

---

## 5. Reconciliation — belief vs coverage (`module_report_tags show`)

| Class | Finding |
|---|---|
| **Belief without coverage** | **TSM and LNG** — held book names, **outside `us_top300`** (M252/M287) ⇒ no flow, RS or short axis exists, and `module_report_tags` carries no sector row for either. **TSM is a rank-1-cycle epicenter holding the grading instrument cannot see.** Unchanged for 5 runs; needs a universe change (human). |
| **Coverage without belief** | **SPG · ADM · CTAS · TRI · GM** — all carry measured flow rows and **no 4Phase anywhere** ⇒ no thesis may be built on any of them, and they are filed as coverage gaps, **not rejected** (*"we have not written a thesis"* is not a rejection reason). |
| **Resolved-but-live** | **PSX** — filed **🔴RESOLVED at ALPHA on 08-02** (exhausted base, FINRA z +1.53, P/C 1.25) **while `ACTION_TICKETS.md` still carries it as a `CORE-STARTER (BUY)` with a 08-05 date.** ⚠⚠ **`core_pick` is HUMAN-LOCKED and was NOT modified.** This is **D19 firing for a 7th consecutive run** — the ticket's rationale still descends from **R8**, retracted 2026-07-22. **Named, not fixed.** |
| **Silently unindexable** | **28 of 300 universe tickers** return 0 from `module_report_tags` regardless of coverage (M152's `_US_STOP` block: A · AIG · ALL · C · CAT · CB · COST · **D** · F · FAST · **GS** · **ICE** · KR · LOW · **MA** · MET · MS · NOW · O · ON · PEG · PM · Q · SO · **T** · TT · **V** · **WELL**). ⚠ **A "zero coverage" reading on any of these names is uninformative**, and **TRI reads 0 from a table row for a cause still `[unknown]` (D101/M249).** |

---

## 6. RESEARCH triggers loaded as binding constraints — which group binds which stage

| Group | Fires when | IDs | Binds this run |
|---|---|---|---|
| **C** | you cite a number | C1 baseline · C2 both halves · C3 unknown column · C4 "indistinguishable" · C5 arbitrary choice | **MACRO · every stage.** ★ **C1 is on special watch**: R41 was filed 08-03 for exactly a C1/C5 failure (a superlative from an unsampled distribution). |
| **S** | you make a statistical claim | S1 date-fold · S2 diagnose the null · S3 power first · S4 in-sample≠done · S5 short samples · S6 future labels | **Any stage citing a test.** ★ **S1 binds hardest today** — with zero new settled US sessions, every US cross-section is **n≈1 date**. |
| **D** | you read data | D1 second venue · D2 proxy sign · D3 signed vs unsigned · D4 regime contamination · D5 cross-provider · **D6 signal grade (OBV is C)** | **SWEEP · ALPHA · L2 indicators.** ★ **D6 binds SWEEP**: the 🟢 gate is an OBV∧volume construct (M144/M237/M272/M314, 7 replications, 2 markets) — **a 🟢 count is a volume test wearing a flow label** and may corroborate, never carry. |
| **W** | you write a conclusion | W1 cross-market · W2 inherited lead/lag · W3 real≠profitable · W4 name the customers · W5 sub-sector dispersion · W6 reader's-market spine | **DEEP · BET · ROTATION.** ★ **W1 binds §4 above** (the KR exposure rule is not a US input) and **W5 binds every sector verdict** — the desk has now measured the label-is-the-wrong-unit shape **five** times (R7 · M26/M174 · IT/C8 · Utilities · Financials). |
| **L** | lenses, not triggers | L1 second derivative · L2 peak-margin trap · L3 branch information content | **DEEP · PREMORTEM.** ⚠ **L2 is unrunnable on 61% of names attempted (M233)** — no cheapness claim may be made where `margin_history` is blank (VLO · XOM · PLD · CSX · UNP · NSC, and truncated at RTX · TMO · T · GM). |

---

## 7. Stale flags and cleared suspensions

| Row | `asof` | Flag |
|---|---|---|
| Seed chain **M1–M19** | 2026-07 / 07-22 | ⚠ **M6 (MU fwd P/E 6.31×) is 12 days stale and already superseded twice** (M206: 5.15–5.31×). Cite M206, not M6. |
| **M22** 3-2-1 crack 99.5th pctile | 07-21 | ⚠⚠ **DEAD as a level** — R30/D95: absolute crack levels differ by **5.80 points** across bar granularity. **Changes only, never a level with a distance.** |
| **000660 ADR flow suspension** (D1/R13) | ongoing | **STILL ON.** R13 converted its expiry from a *date* to an *observable* (the ADR premium, S17). **S17 settles 08-05** — the KR run has rebuilt its series twice and it reproduces to the decimal (07-31 **+18.85% = branch C territory**, the window's first non-B). **Not a US-desk read.** |
| **`DTWEXBGS`** | 07-24 | ⚠ **unprinted 10 calendar days**, 4th run pending. Blocks S44 leg 2 and S12's only remaining scoreable axis. |
| **`CATALYST_WATCH.json`** | 08-03 | ⚠ **D18 has now fired 14 times across both desks.** Not trusted as the binary source; MACRO re-pulls at **≥10 days** (D26). |

**Cleared suspensions converted to dig instructions:** none cleared this run. The one live suspension
(000660) is explicitly still on.

---

## 8. Dig list ranked for today — candidate DEEP assignments

| Rank | Dig | Why it is today's shape |
|---|---|---|
| **1** | **D19** *(defect)* — `action_bracket` ticket rationale is a frozen string descending from retracted **R8** | **7th consecutive run.** The desk's only "BUY"-shaped artifact points at **PSX**, which its own ALPHA stage filed 🔴RESOLVED yesterday. Needs a human (`core_pick` is locked). |
| **2** | **D126** *(defect)* — the `velocity` join oscillates 0/300 ↔ 50/300 **between runs on the same data** | With **zero new US bars**, this run can test it as a **controlled experiment**: same input, same day. Assigned to SWEEP. |
| **3** | **R39's consequence** — the Energy cycle-registry tag is wrong | The 🚨 rank-2 GAP is computed on it, so a headline exposure number is currently `unknown` (C3). Registry edit needs a human. |
| **4** | **D1** — do LTA price floors hold margin? | **Now half-answered from the seller** (M228: ~10 LTAs, ≤5 years, deposits + volume commitments, *"to keep prices steady"*, **no price term disclosed**) and **from the buyer** (M310: Apple's *"hundred year flood"*, GM guided −2.1 to −3.1pp, four OEMs raising end prices). **C1 is measurable from both sides for the first time.** DEEP-IT. |
| **5** | **D3** — hyperscaler capex → memory revenue lead-lag, tested the way W2 demands | M8/M9 remain a two-firm estimate; **W2 exists because this exact claim class was carried on authority and turned out coincident.** |
| **6** | **D9 · D10 · D11** *(open code defects, human-gated)* | Carried forward, **not silently re-discovered**: holdco concentration · news-body boilerplate · the C-grade-signal veto in `_synthesize.py`. |

**New dig registered by this stage** (ID checked against **both** files at write time per M319 —
highest existing is **D137**, taken by the 08-03 `industry_kr` run):

> **D138** — **A currency-sign observable must name its venue and its bar convention.** S44 froze
> *"the won/dollar **close** direction"* with no venue. `KRW=X` is a 24-hour OTC quote; a KRX-session
> close and a 24h close are different objects on a day when the KR session and the US session move
> the pair in opposite directions. **The verdict was unaffected here** (the move is +0.527% against a
> flat DXY), **and that is luck, not design.** Same family as **D50** (check each leg for a live
> corporate action) and **D93** (measure the estimator's error) — all three are *pre-registration*
> hygiene. Owner: PREMORTEM, at registration time.

---

## 9. What this stage hands forward

1. ⚠⚠ **No new US settled tape.** SWEEP must reproduce 08-02; ROTATION may not move a direction on
   price; any "change" is an instrument finding.
2. ✅ **S44 FIRED-B ⇒ M-15 retracted** — write it to §5 at run end.
3. ✅ **S43 VOID** on a primary-sourced anti-signal — re-register on a different qualifying session,
   **and record that its ±1.0pp band was measured to sit inside its own 2.92pp estimator σ.**
4. **S47-KR handed to the 08-04 `industry_kr` run as its #1 job** (visible in both files now).
5. **S49 is the bracket most likely to fire next** — its rate condition was already negative at 07-31
   and tonight's 08-03 close is the first bar that can settle it. **MACRO checks it first.**
6. **Tomorrow is dense: MPC · AMD · ANET · S50 · S53 all land 08-04.** PREMORTEM must produce
   **both-sides brackets** — a one-way tilt into a known binary is a protocol violation.
7. **Exposure: 복귀 with a held 복귀→방어 transition, 90% target vs 54.2% actual, −35.8pp band
   breach.** Carried as size context only; **not a US sizing input (W1).**

**No position sizing, no buy/sell language appears anywhere in this carry (P4).**


---

## 10 · ⚠⚠ Retention budget — BREACHED, and reported as a finding rather than treated as an error

`python -X utf8 scripts/handoff_compact.py --budget-only`, run at writeback:

```
RESEARCH.md         244.4 KB   budget  85 KB   OVER by 159
SCENARIOS_US.md     143.6 KB   budget  50 KB   OVER by  94
STANDING_VIEW_US.md 145.1 KB   budget  50 KB   OVER by  95
STANDING_VIEW.md    100.9 KB   budget  45 KB   OVER by  56
SCENARIOS.md         48.4 KB   budget  20 KB   OVER by  28
--------------------------------------------------------------
US run reads        694.0 KB   budget 250 KB   OVER by 444 KB
KR run reads        580.9 KB   budget 250 KB   OVER by 331 KB

§2 fact rows: 277 · avg 0.55 KB/row · rule is <= 0.35 KB/row
```

**The `handoff/` retention rule was written on 2026-07-25 from a measurement** (the file had grown to
286 KB read at every HANDOVER, ~30 KB per run, 76% un-curated append blocks). **It has not held.**
**A US run now reads 694 KB — 2.8× its budget and 2.4× the size that triggered the rule's creation.**

⚠⚠ **And this run is part of the cause, not an observer of it.** Measured at writeback:
- **`M340` is the single fattest fact row in the entire file at 1.21 KB** — **3.5× the 0.35 KB
  limit** — and it was written by this stage's own run.
- The average row is **0.55 KB, 57% over** the rule, and **277 rows** now exist.

★ **Stated positively, because the rule's own framing is that a breach is a finding**: the compaction
instrument exists (`handoff_compact.py`), it is **non-destructive by design** (facts *move* to
`ARCHIVE_FACTS.md` and stay greppable — the 07-25 pass lost **0 of 154**), and the 07-25 precedent
shows it works. **What is missing is that nobody is running it.** ⇒ **This is the highest-value
mechanical item on the desk's list that needs no new code, and it is named here rather than left to
the next run to rediscover.**

⚠ **Not acted on by this run**, because compaction is a bulk rewrite of the shared spines while the
`industry_kr` desk may run concurrently — **and this repo has now measured two same-day concurrent-write
incidents (D76's ID collisions, and M319's dig-counter collision).** **A human should schedule it
between runs.**
