# HANDOVER — industry_US · 2026-08-04 (Tue) · STAGE 1, runs before MACRO

## 0. Run clock, and the fact that governs this run

**10:01 ET · 23:01 KST · 31 minutes AFTER the US open.**

| | |
|---|---|
| Last settled US session | **2026-08-03 (Mon)** |
| Last settled US session used by the **prior** run (08-03) | **2026-07-31 (Fri)** |
| ⇒ New settled US price information since the last run | **ONE FULL SESSION — and it is a large one** |

This inverts yesterday's constraint. The 08-03 run opened by declaring it had **zero** new US tape and
built its value from instrument work. **Today there is a settled 08-03 bar, and it moved the single
observable this desk flagged as most likely to fire.** It did fire — §2a.

⚠⚠ **But the clock is worse than yesterday's in the other direction: the US market is OPEN.**
**D74 (unsettled-bar contamination) is live for the first time in three runs.** Pre-committed here,
before SWEEP runs:

1. **SWEEP must trim its price cache to ≤ 2026-08-03** and say so. A `module_flow`/`sector_flow` call
   at 10:0x ET carries ~5–10% of a session's volume, which is exactly the axis the US 🟢 gate turns
   on (D31 · M204 · M247). **`vol_surge` and OBV from an untrimmed pull are unusable today.**
2. **Every price, RS and flow figure in this run is stamped `asof 2026-08-03 settled`**, never
   "today". Where an intraday number is quoted at all it is labelled 🟡live and may not carry a verdict.
3. What is genuinely new: **(a)** the settled 08-03 US session; **(b)** `DTWEXBGS` has printed for the
   first time in 11 calendar days — the series that blocked two brackets across four runs;
   **(c)** MPC prints tonight and AMD/ANET print tonight, so **S50 and S53 both have their trigger
   event inside this session**.

---

## 1. Inheritance read — what was opened

| File | Read | Note |
|---|---|---|
| `handoff/STANDING_VIEW.md` (SHARED SPINE) | ✅ in full | §1 regime call · §2 seed chain M1–M19 · §4 asymmetry · **§5 retracted ledger R1–R43** · §6 contradictions C1–C10 |
| `handoff/STANDING_VIEW_US.md` | ✅ | §2 US fact rows · §3a per-name registry |
| `handoff/SCENARIOS.md` (SHARED SPINE) | ✅ in full | legend · scoring rules · master scoring log · **master index, 68 brackets (44 US · 24 KR)** |
| `handoff/SCENARIOS_US.md` | ✅ | all 44 US brackets status-scanned; **S49 · S50 · S51 · S52 · S53 · S54 read in full** (the live ones) |
| `handoff/SCENARIOS_KR.md` | ✅ **checked for past-dated rows this desk owes** | **ZERO** — the 08-04 `industry_kr` run scored S47-KR (FIRED-B) itself and closed the KR condition-settled class entirely (S39·S43·S44 all settled). Remaining KR rows are all date-settled and all future (08-05 → 10-30). |
| `handoff/RESEARCH.md` | ✅ Part A triggers · Part B lenses · Part C dig list (through D148) | loaded as **binding constraints**, not summarized (§6) |
| `module_report_tags show` | ✅ | reconciled against belief in §5 |

### §5 retracted ledger read BEFORE forming any view — the five that bind this run

- **R43** *(new, filed 08-04 by the KR desk — cross-market because it is a KPI retraction)* — M-19's
  generalisation that **KR refining 2Q profit is inventory-and-oil-level rather than crack margin** is
  dead: **the 86% was SK-specific**; S-Oil printed **21.36%** (₩113.7bn ÷ ₩532.4bn) and the company
  attributed its refining OP to **정제마진 rising**. ⇒ ⚠⚠ **This binds today's ENRG work directly.**
  **No stage may argue "the refining print is an inventory artifact" as a general property**, and
  **`정제마진` is NOT dropped as the node's KPI** — branch A's consequence did not happen. The
  read-across to MPC/PSX is a *hypothesis to test tonight*, not an inherited fact (**W1** — this was
  measured on Korean refiners).
- **R42** — M-15's **domestic-liquidation** reading of the KR crash is dead (S44 FIRED-B on its frozen
  sign pair). ⇒ no stage may re-import "domestic liquidation, not foreign flight" as background.
- **R41** — *"the largest crowded short / the maximum on the board"* is withdrawn as a **method**:
  a superlative is a property of the sample unless the distribution was actually scanned. ⇒ **this run
  may not write "the largest / the most X on the board"** about any flow score, short reading or spread
  without stating the population it scanned (**C1/C5**).
- **R40** — the **"regulated seven" basket is contaminated** (D is a merger-arb security post
  NEE/D DEFM14A). ⇒ **neither S35's FIRED-A nor S47's FIRED-B may be cited as evidence about
  Utilities.** Both settle 08-07 and must be scored on the regulated-**six**.
- **R39** — *"XOM is 0% refining"* is dead. ⇒ the 🚨 rank-2 Energy GAP in `CYCLE_EXPOSURE` is computed
  on a **wrong registry tag** and its magnitude is `unknown` (C3) until a human fixes the registry.
  **CYCLE_EXPOSURE's Energy number may not be quoted as a level.**

⚠ Cross-check performed: **no claim formed in this HANDOVER matches a retracted entry.** The claim
that came closest — reading tonight's MPC print through "the refining margin is really inventory
timing" — is exactly what **R43 just killed on the KR side**, and it is therefore written as
**S53's open question**, not as a premise.

---

## 2. ★★★ Scenarios — S49 FIRED-B on the settled 08-03 close, exactly where the prior run pointed

> The 08-03 HANDOVER's hand-forward item 5 read: *"S49 is the bracket most likely to fire next — its
> rate condition was already negative at 07-31 and tonight's 08-03 close is the first bar that can
> settle it. MACRO checks it first."* **It fired. This is the first time this desk has pre-named the
> next bracket to fire and been right on the next session.**

### 2a. S49 — ★★★ **FIRED-B**, and it is the highest-information verdict on the US board

**S49** (registered 2026-07-30, US PREMORTEM Lens 2, as S8's successor).
**Frozen observable**: the **5-session change in the settled distillate crack (HO×42 − WTI)**, on
**yfinance DAILY settled bars only, one named source, never mixed with intraday.**

**D140's remedy executed rather than cited** — the whole window was **re-pulled**, not carried:

| Settled date | HO=F | CL=F | distillate crack | 5-session change |
|---|---|---|---|---|
| 2026-07-24 | 4.181 | 89.31 | 86.275 | −1.948 |
| 2026-07-27 | 4.112 | 82.61 | 90.077 | +0.309 |
| 2026-07-28 | 4.151 | 79.26 | 95.078 | +6.671 |
| 2026-07-29 | 4.370 | 84.46 | 99.084 | +11.665 |
| 2026-07-30 | 4.209 | 83.59 | 93.205 | +3.048 |
| 2026-07-31 | 4.122 | 84.67 | 88.433 | **+2.158** |
| **2026-08-03** | **3.877** | **80.34** | **82.502** | **−7.575** |

| Branch | Condition | Fired? |
|---|---|---|
| A | 5-session change stays **> 0** through 08-06 | ❌ |
| **B** | that change turns **≤ −5.0 points** by 08-06 | ✅ **FIRED at −7.575, 2.6 points past the line** |
| C | −5.0 to 0 | ❌ |

⇒ **`FIRED-B`** — the registered meaning, quoted verbatim rather than re-worded:
*"The bottleneck is releasing — **S8 branch A's economics arriving WITHOUT a Hormuz statement.**
⚠⚠ Per the correlated-tilt check, **this hits ENRG OW− and INDU OW− on the same tick**"* (M91: the
rail node's fuel-surcharge leg).

★ **Invalidation checked BEFORE the observable** (the S43/S46-KR precedent, now standing practice):
S49's registered invalidation is *"a Hormuz reopening statement ⇒ **S8** owns that as a narrative
event, not this."* **No such statement exists** — S52's branch A requires a **dated** Strait-reopening
term in a primary text and the 08-03 US run recorded branch A as unmet with only the 08-02 conditional
Truth Social post on file. **MACRO re-checks the foreign pool for a post-08-03 statement and this
verdict is contingent on that check** (recorded as the one open leg, not assumed away).

★★ **D140 reproduces and this time it is benign.** The 07-31 value was carried at **+1.066** by one
pull and **+2.158** by another two days later. **Today's independent re-pull returns +2.158** — the
revision has settled and the carried number is the revised one. **The remedy (re-pull the window at
scoring) worked; it is not a coincidence that it worked, it is why it was written.**

⚠ **Three honest caveats recorded WITHOUT moving the threshold:**
1. **n = 1 session (S1).** The verdict is on a pre-registered threshold crossing, not on a trend.
2. **The 3-2-1 composite moved further** (5-session change **−11.108**, level 57.008) and is **not
   the frozen observable.** It is recorded as corroboration on a *different* series, never merged.
3. **The move is on both legs**: HO fell 4.122 → 3.877 (−5.9%) while WTI fell 84.67 → 80.34 (−5.1%),
   so the crack compression is **product-led, not a crude artifact** — the distillate leg gave up more
   than the barrel. Gasoline fell harder still (crack 50.637 → 44.261).

### 2b. S53 — collapses to a name-level footnote by its OWN registration, and that is recorded now

S53's registration text pre-committed: *"if S49 branch B fires **BEFORE** these prints — it is one
session of its current rate away — **S49 owns the outcome and this bracket collapses to a name-level
footnote.** Noted at registration so no later stage double-counts them."*

**S49-B fired on the 08-03 settled close. MPC prints 2026-08-04 (tonight).** ⇒ **the pre-commitment
binds: S53 stays ARMED to 08-05 and is scored on its own execution-level observable, but its result
may NOT be re-counted as independent evidence about the refining node.** Registered here so PREMORTEM
and BET cannot re-inflate it.

### 2c. Every other ARMED row — classified and checked (this is the check being performed, not skipped)

**Date-settled, all future — dates recorded, no action:**
S3 (~09/10) · S4 (~09 late) · S5 (**08-11**) · S9 (**08-05**) · S13 (08-12) · S14/S14-num (**08-06**) ·
S16 (08-05) · S19 (08-05) · S23 (08-05) · S24 (08-12) · S25 (08-08) · S26 (08-12) · S30 (**08-05**) ·
S31 (**08-05**) · S35 + S35-ANNEX (**08-07**) · S36 (08-05) · S37 (09-30) · S40 (09-30) · S41 (08-12) ·
S42 (08-12) · S46 (08-13) · S47 (**08-07**) · S48 (09-30) · **S50 (08-06 — AMD/ANET print TONIGHT)** ·
S51 (08-10 — NFP 08-07) · **S53 (08-05 — MPC TONIGHT + PSX 08-05)** · S54 (08-10).

**Condition-settled — each compared against today's data:**

| ID | Condition | Status at 10:0x ET on settled data |
|---|---|---|
| **S49** | distillate 5-session change ≤ −5.0 | ✅ **FIRED-B — §2a.** Leaves the condition-settled class. |
| **S8** | Hormuz "Strait open" — **undated `[blank]`** | ⚠ **3rd consecutive run carried as un-scoreable.** R30/D95 measured its 60/84 absolute kill lines to be undecidable across bar granularity. ★ **And S49-B has now delivered S8 branch A's *economics* without S8's *narrative trigger*** — i.e. the bracket is not merely unscoreable, its question has been answered by a different instrument. **It should be formally `VOID`ed or re-registered by a human. Named for the third time, not dropped.** |
| **S52** | dated Strait reopening **vs** named-infrastructure strike | Condition-settled ≤48h class, window **08-06**. **This stage does not pull news; MACRO checks it against the fresh foreign pool — and today that check is load-bearing because S49's invalidation depends on the same object.** |
| **S9** | real 10y (DFII10) ≥ **2.55** kill line | ⚠⚠ **`[FRED]` DFII10 = 2.47 (07-31), up from 2.41 held flat for four prints.** ⇒ **the buffer halved, 14bp → 8bp, in one print.** Re-pulled at MACRO; **this is the closest any US kill line now sits.** |
| **S23 / S51** | derived 2s10s ≤ +0.20 | `[FRED]` DGS10 **4.75** − DGS2 **4.28** = **+0.47** (07-31), from +0.45 at 07-29 ⇒ **27bp away and still steepening.** S51 branch A (≥ +0.35) currently satisfied; it settles on the **08-07** close, not now. |
| **S26** | HY OAS ≥ 3.10 | `[FRED]` **2.85** (07-31) ⇒ **25bp buffer**, essentially unchanged. |
| **S41** | IG OAS ≥ 0.90 | `[FRED]` **0.79** (07-31) ⇒ **11bp buffer.** ⚠ `ig_oas` **failed with a FRED 502** on the first call and succeeded on retry — logged as a lookup failure that recovered. |
| **S44 leg 2** *(KR-owned, already FIRED-B on leg 1)* | `DTWEXBGS` | ★★ **IT PRINTED.** The series was frozen at **120.7105 asof 07-24** for four consecutive runs; it now carries **07-28 120.6247 · 07-29 120.7892 · 07-30 119.6753 · 07-31 119.7034**. ⇒ 07-24 → 07-31 = **−0.83%**. **Recorded, NOT used to re-score** — branch B fired on leg 1 alone and a settled verdict is not reopened by a late-arriving leg (L3). |

**`EXPIRED` = 0 · silent skips = 0 · past-dated rows unscored = 0.**

⚠ **S12 checked explicitly rather than assumed**, because `DTWEXBGS` printing could look like it
reopens it: **S12 was already scored FIRED-B (observable) / AMBIGUOUS (decision axis) on 2026-07-28.**
It is closed and stays closed.

---

## 3. Both ledgers audited — both clean, and the clean result is reported rather than assumed

```
reject_ledger.py due  → 98 rows · 29 resolved · legacy (no revives_if) 0 · recheck-date due 0
missed_ledger.py due  → 48 rows ·  0 resolved · legacy (no enters_if)  0 · recheck-date due 0
```

- **Rejection ledger: legacy count 0 for a 7th consecutive run**, and the row count rose 96 → 98
  (the 08-03/08-04 runs are still filing). Per `carryover.md` §3b the correct reading of a clean `due`
  is **not** "healthy" — it is *"legacy is 0 and the audit load is **scheduled** at 08-12/08-13/08-16/08-18"*.
- **Missed ledger: 48 rows (42 → 48), 0 legacy, 0 due.** ⚠ **`resolved = 0 of 48` is the number to
  watch and it is now worse in absolute terms than yesterday.** The first rechecks fall **08-14 (KR:
  073240, 000150)** and **08-16 (US: ADM, CTAS)**, then **08-18**. **If 08-14/08-16 pass unresolved,
  that is the same process failure on the opportunity-cost side the rejection ledger already paid for
  once** — named now, ten days early, so it cannot be discovered late.
- ⚠ **Signs are opposite and are NOT summed.** No combined figure appears anywhere in this run.
- ⚠ `missed_ledger score`'s first six rows remain `outcome_selected`; per **D106** those class means
  are **accumulation, never an edge**, and are not quoted.

---

## 4. Exposure state — carried as SIZE CONTEXT only

```
python -X utf8 scripts/exposure_rule.py state   → 2026-08-04, bench 069500.KS
```

| Field | Value |
|---|---|
| Rule state | **복귀 (복귀 held)** — with `⚠전이 보류(복귀→방어) — 최소유지 **2/3**세션` |
| Bench | close **100,330** · day **+1.236%** · vs 20d high **−18.9%** · vs 20d low **+14.49%** · volume **0.86× [정착]** |
| Target invested | **90%** |
| Current invested (ledger row, 08-04) | **70.6%** |
| **Band gap** | **🚨 −19.4pp (밴드이탈)** — narrowed from −35.8pp yesterday |
| Ledger depth | **28 rows**; cumulative decomposition **n=3** |

**Cumulative: total excess −6.55pp = cash −2.68pp + selection −3.87pp (n=3).**
⚠ **n=3 is indistinguishable from zero (C4)** and is quoted only to keep the counter visible and rising.

⚠⚠ **Four caveats, load-bearing:**
1. **The 복귀→방어 transition is at 2/3 sessions and executes tomorrow unless the state changes.**
   Per the L3 unit: *"보류를 '조건 미충족'으로 읽지 마라 — 조건은 충족됐고 집행만 미룬 것이다."*
   ⇒ **the 90% target is the state the rule is LEAVING, with one session of life left.** A stage that
   reads "복귀 ⇒ go wide" off this line is reading a number that is about to be replaced.
2. **This is the KR book's exposure rule** (`069500.KS`, KR contest bands). **It is not a US sizing
   input and no US stage may size off it (W1).**
3. **`exposure_rule.py state` returned `투자비중미상`** (no account query) while `show` carries a
   70.6% row from the timefolio accrual task. **The two are different objects and the `show` figure is
   the one quoted**, with the discrepancy stated rather than smoothed.
4. 🚨 **`ARMED(TIMEFOLIO_EXECUTE=1)` is set in the environment.** This is a **read-only research run**:
   **no orders, no `--execute`, no order-desk staging.** Recorded because the flag being armed at all
   is a standing condition a human should see — 2nd consecutive run.

**Not cold-starting** (28 rows) ⇒ the verdict is quotable.

---

## 5. Reconciliation — belief vs coverage (`module_report_tags show`)

| Class | Finding |
|---|---|
| **Belief without coverage** | **TSM and LNG** — held book names **outside `us_top300`** (M252/M287) ⇒ **no flow, RS or short axis exists for either**, and the ledger carries no sector row. **TSM is a rank-1-cycle epicenter holding the grading instrument cannot see.** Unchanged for **6 runs**; needs a universe change (human). |
| **Coverage without belief** | **SPG · ADM · CTAS · TRI · GM** — measured flow rows, **no 4Phase anywhere** ⇒ no thesis may be built on them; filed as **coverage gaps, not rejections** (*"we have not written a thesis"* is not a rejection reason). |
| **Resolved-but-live** | **PSX** — filed **🔴RESOLVED at ALPHA on 08-02** while `ACTION_TICKETS.md` still carries it as a `CORE-STARTER (BUY)` dated **08-05**. ⚠⚠ **`core_pick` is HUMAN-LOCKED and was NOT modified.** **D19 firing for an 8th consecutive run**; the ticket's rationale still descends from **R8**, retracted 2026-07-22. ★ **And it gets worse today, not merely older: PSX prints 08-05 and S49-B just fired against the node the ticket is long.** Named, not fixed. |
| **Silently unindexable** | **28 of 300 universe tickers** return 0 regardless of coverage (M152's `_US_STOP`: A · AIG · ALL · C · CAT · CB · COST · **D** · F · FAST · **GS** · **ICE** · KR · LOW · **MA** · MET · MS · NOW · O · ON · PEG · PM · Q · SO · **T** · TT · **V** · **WELL**). ⚠ A "zero coverage" reading on any of these is **uninformative**, not evidence. |

---

## 6. RESEARCH triggers loaded as binding constraints — which group binds which stage

| Group | Fires when | IDs | Binds this run |
|---|---|---|---|
| **C** | you cite a number | C1 baseline · C2 both halves · C3 unknown column · C4 indistinguishable · C5 arbitrary choice | **MACRO · every stage.** ★ **C1 on special watch** (R41 was filed for a C1/C5 failure two runs ago). ★ **C2 binds ENRG hardest today** — the crack's *level* (82.5, still historically high) and its *rate* (−7.575/5d) point opposite ways and **both halves must be quoted**. |
| **S** | you make a statistical claim | S1 date-fold · S2 diagnose the null · S3 power first · S4 in-sample≠done · S5 short samples · S6 future labels | **Any stage citing a test.** ★ **S1 binds S49's verdict** — it is **one** threshold crossing, not a trend, and the run says so. |
| **D** | you read data | D1 second venue · D2 proxy sign · D3 signed vs unsigned · D4 regime contamination · D5 cross-provider · **D6 signal grade (OBV is C)** | **SWEEP · ALPHA · L2 indicators.** ★★ **D74/D31 bind SWEEP hardest today — the market is OPEN.** ★ **D6 binds every 🟢 count**: it is an OBV∧volume construct (7 replications, 2 markets) and may corroborate, never carry. |
| **W** | you write a conclusion | W1 cross-market · W2 inherited lead/lag · W3 real≠profitable · W4 name the customers · W5 sub-sector dispersion · W6 reader's-market spine | **DEEP · BET · ROTATION.** ★★ **W1 binds twice today**: the KR exposure rule is not a US input, **and R43 was measured on Korean refiners** — it is a hypothesis for MPC/PSX, not a fact about them. **W5 binds every sector verdict** (the label-is-the-wrong-unit shape is now measured **five** times). |
| **L** | lenses | L1 second derivative · L2 peak-margin trap · L3 branch information content | **DEEP · PREMORTEM.** ★★ **L1 is the run's central lens today** — S49-B *is* a second-derivative event on the desk's most-tracked series. ⚠ **L2 is unrunnable on 61% of names attempted (M233)** — no cheapness claim where `margin_history` is blank (**VLO · XOM · PLD · CSX · UNP · NSC**; truncated at RTX · TMO · T · GM). |

---

## 7. Stale flags and cleared suspensions

| Row | `asof` | Flag |
|---|---|---|
| Seed chain **M1–M19** | 2026-07 / 07-22 | ⚠ **M6 (MU fwd P/E 6.31×) is 13 days stale, superseded twice** (M206: 5.15–5.31×). Cite M206. |
| **M22** 3-2-1 crack 99.5th pctile | 07-21 | ⚠⚠ **DEAD as a level** (R30/D95: levels differ 5.80 points across bar granularity). **Changes only.** ★ **And the level has now fallen to 57.008 — quoting M22's "99.5th percentile" today would be wrong on both the staleness and the instrument axis.** |
| **`DTWEXBGS`** | **07-31 (was 07-24)** | ✅ **SUSPENSION CLEARED — printed after 11 calendar days and 4 pending runs.** ⇒ **converted to a dig instruction, not a silent trust**: MACRO reads the 07-28→07-31 path (**120.62 · 120.79 · 119.68 · 119.70**) as a *dollar* observation in its own right — a **−0.92% two-session drop** sits inside the window in which the KR crash and the Japan-Korea joint intervention (D142) both happened. |
| **000660 ADR flow suspension** (D1/R13) | ongoing | **STILL ON.** Its expiry is an observable (the ADR premium, **S17, settles 08-05**), not a date. The KR run re-checked the anti-signal at the primary on 08-04 — `module_disclosure 000660 --days 5` returns 2 filings, **neither an issuer disclosure raising the 2.5% ceiling.** **Not a US-desk read.** |
| **`CATALYST_WATCH.json`** | 08-04 | ⚠ **D18 has fired 15 times across both desks** (the KR run logged the 15th today). **Not trusted as the binary source**; MACRO re-pulls at **≥10 days** (D26). ⚠ **D141: the STRUCTURAL block reads an empty data file — a closed dig wearing a checkmark.** |
| **`core_pick` / `ACTION_TICKETS`** | 08-02 | ⚠ **D19, 8th run.** Human-locked, stale, and now pointing at the name S49-B just ran against. |

**Cleared suspensions converted to dig instructions: ONE — `DTWEXBGS`** (above). The one live
suspension (000660) is explicitly still on.

---

## 8. Dig list ranked for today — candidate DEEP assignments

| Rank | Dig | Why it is today's shape |
|---|---|---|
| **1** | **R43's read-across, and it is a W1 trap** — does the S-Oil finding (refining OP driven by **정제마진**, inventory gain only 21.4%) transmit to **MPC (prints tonight) / PSX (08-05) / VLO**? | **S49-B just said the commodity crack is releasing while R43 says the KR refiners' profit was crack-driven after all.** Those two readings pull in opposite directions on the same node **on the night MPC prints.** ⇒ **DEEP-ENRG's mandate.** ⚠ **The KR measurement is a hypothesis here, not evidence (W1).** |
| **2** | **D140's remedy — make it mechanical, not remembered.** | It **worked today** (the re-pull reproduced the revised +2.158 and the verdict is clean because of it). **Two brackets (S8, S49) have now been defeated by two different properties of one series.** The remedy is a stamp-and-re-pull convention, not a third threshold. Owner: PREMORTEM (registration) · MACRO (scoring). |
| **3** | **D126** *(defect)* — the `velocity` join oscillates 0/300 ↔ 50/300 between runs on the same data | **Quantified by the 08-03 run's controlled experiment (10 greens manufactured, 3 sector `wflow` signs flipped with no price input).** Today there IS new price data, so the experiment cannot be repeated cleanly — **SWEEP must instead report which side of the oscillation it landed on**, so the series stays interpretable. |
| **4** | **D1** — do LTA price floors hold margin? | **Now half-answered from both sides** — seller (M228: ~10 LTAs, ≤5y, deposits + volume commitments, *"to keep prices steady"*, **no price term disclosed**) and buyer (M310: OEM cost guidance). **C1 is measurable from both directions for the first time.** AMD/ANET print tonight (**S50**), which is the silicon-layer read. DEEP-IT. |
| **5** | **The IC ledger's cross-market sign disagreement on `vol_surge`** — see §9 item 6 | **The standing item says `vol_surge` is the only KR axis with a consistent negative sign across two horizons, and `sector_flow` still weights it positively.** The US ledger now carries **14 runs** and reads the **opposite sign**. **This is a W1 question with a measurement on both sides for the first time.** |
| **6** | **D9 · D10 · D11 · D17 · D19 · D20 · D22 · D104 · D141** *(open code/data defects, human-gated)* | Carried forward, **not silently re-discovered.** They will keep costing a stage per run until a human clears one. |

**New digs registered by this stage:** none. **ID counters verified at read time for the stages that
will register** (D137's three-grep requirement, run against all `handoff/*.md`):
**highest `M###` = 355 · highest `D###` = 148 · highest `R##` = 43 · highest `S##` = S54 (US) /
S51-KR (KR)** ⇒ this run takes **M356+ · D149+ · R44+ · S55+ (or `-US` suffixed)**.
⚠ **`S55` returns a single grep hit in `SCENARIOS.md` — it is prose inside the 08-03 collision note
(*"grep for S54/S55/S50-ANNEX returned 0"*), not a registration.** Checked rather than assumed.

---

## 9. What this stage hands forward

1. ★★★ **S49 FIRED-B (−7.575 vs a −5.0 line).** Its registered meaning hits **ENRG OW− and INDU OW−
   on the same tick.** ⚠ **Contingent on one open leg**: MACRO must confirm **no Hormuz reopening
   statement** exists in the fresh foreign pool (S49's invalidation, which is also S52 branch A).
2. ⚠⚠ **The market is OPEN — D74 is live.** SWEEP trims to ≤08-03 and says so; every price figure is
   stamped `asof 2026-08-03 settled`.
3. **S53 collapses to a name-level footnote by its own registration** now that S49-B fired first.
   It stays ARMED to 08-05; its result may not be re-counted as independent node evidence.
4. ✅ **`DTWEXBGS` suspension cleared** — 4-run pending state closed, converted to a MACRO read.
   **S44 leg 2 is recorded, NOT re-scored.**
5. ⚠ **S9's buffer halved to 8bp** (DFII10 2.41 → 2.47). **It is now the closest US kill line on the
   board** and settles 08-05.
6. ★★ **The IC ledger reads opposite signs on `vol_surge` across markets** — KR h=1 **−0.0488,
   t(NW) −2.93, n_eff 18, Bonferroni-significant**; US h=1 **+0.0267, t +1.36, n_eff 14,
   `구분 불가`**, and US h=5 also positive (+0.0416). ⇒ **the standing "kill `vol_surge`" item is a
   KR finding and does not transfer (W1).** Separately the **US `rs60` h=1 reads −0.0942, t(NW) −2.54,
   n_eff 14 — 유의(단독) but NOT Bonferroni** (threshold 2.8), with a consistent negative sign at two
   horizons. ⚠ **The measurement window is a −27% crash and a rebound; a crash-window IC does not
   generalise. Reported, not acted on (P4).**
7. **Tonight is dense: MPC · AMD · ANET all print 08-04.** **PREMORTEM must produce both-sides
   brackets** — a one-way tilt into a known binary is a protocol violation.
8. **Exposure: 복귀 with the 복귀→방어 transition at 2/3, 90% target vs 70.6% actual, −19.4pp band
   breach.** Size context only; **not a US sizing input (W1).**

**No position sizing, no buy/sell language appears anywhere in this carry (P4).**

---

## 10 · ⚠⚠ Retention budget — BREACHED and WORSENING, reported as a finding

`python -X utf8 scripts/handoff_compact.py --budget-only`, run at this stage:

```
RESEARCH.md         255.1 KB   budget  85 KB   OVER by 170   (was 244.4 → +10.7 in one day)
STANDING_VIEW_US.md 145.1 KB   budget  50 KB   OVER by  95
SCENARIOS_US.md     143.6 KB   budget  50 KB   OVER by  94
STANDING_VIEW_KR.md 121.9 KB   budget  50 KB   OVER by  72
STANDING_VIEW.md    109.1 KB   budget  45 KB   OVER by  64   (was 100.9 → +8.2)
SCENARIOS.md         54.8 KB   budget  20 KB   OVER by  35   (was  48.4 → +6.4)
--------------------------------------------------------------
US run reads        719.3 KB   budget 250 KB   OVER by 469 KB   (was 694.0 → +25.3 in ONE day)
KR run reads        625.2 KB   budget 250 KB   OVER by 375 KB   (was 580.9 → +44.3 in ONE day)

§2 fact rows: 289 (was 277) · avg 0.54 KB/row · rule is <= 0.35 KB/row
fattest: M340 1.21 KB · M152 1.04 KB · M184 0.92 KB
```

★ **The measurement the 08-03 run asked for is now available: the growth rate.** A US run's read cost
grew **+25.3 KB in a single day** and a KR run's **+44.3 KB**. At that rate the US read passes **1 MB
in ~11 runs.** The 07-25 rule was written when the file hit 286 KB.

★ **Stated positively, as the rule's own framing requires**: the instrument exists
(`handoff_compact.py`), it is **non-destructive by design** (facts *move* to `ARCHIVE_FACTS.md` and
stay greppable — the 07-25 pass lost **0 of 154**), and the precedent shows it works.
**What is missing is that nobody runs it. This is the highest-value mechanical item on the desk's
list that needs no new code.**

⚠ **Not acted on by this run**, for the same reason as yesterday: compaction is a bulk rewrite of the
shared spines while `industry_kr` may run concurrently, and this repo has measured **two same-day
concurrent-write incidents** (D76 ID collisions; M319's dig-counter collision). **A human should
schedule it between runs.** ★ **Second consecutive run naming it — recorded so the ask is visibly
repeated rather than restated as if new.**


---

# ★ POST-RUN NOTE — appended at writeback (append-only), 2026-08-05 ~00:5x KST

## Four rejection rows became DUE while this run was executing — handed forward explicitly

This stage recorded `reject_ledger.py due → recheck-date due 0` at its own clock (**asof 2026-08-04**),
and that was correct then. **The run crossed local midnight, and re-running the audit at writeback
(asof 2026-08-05) returns FOUR due rows:**

| Filed | Ticker | Class | `revives_if` |
|---|---|---|---|
| 2026-07-24 | **316140** 우리금융지주 | `K.본문반증` | foreign 20d net-buy sign flips **AND** the 07-29 governance package hits branch C (withdrawal) |
| 2026-07-24 | **139130** iM금융지주 | `K.본문반증` | foreign 20d sign flips **AND** institution net-buy holds even as news velocity normalises (≤2.0×) |
| 2026-07-31 | **CVX** Chevron | `E.상관가드` | **RS60 vs SPY > 0** AND refining-margin exposure re-confirmed |
| 2026-07-31 | **MU** Micron | `H.밸류소진` | **S30 median RS20 {STX, MU, WDC} vs SPY > 0 on 08-05** AND MU's OBV turning 매집 |

★ **Two of the four have evidence already sitting in THIS run's own output, and it is handed over
rather than left to be re-derived:**
- **CVX** — its revival condition is **RS60 > 0**, and this run measured **CVX RS60 = +1.8 on a
  days-21-to-60 segment of −11.0** ⇒ **technically true, and DEEP-ENRG's finding is that the number is
  a denominator artifact (repair of a hole, not a run).** **A mechanical `revived` call on this row
  would import exactly the artifact D154 was registered for. The next HANDOVER should resolve it
  on the SEGMENT, and say so.**
- **MU** — its revival condition names **S30's median on 08-05**. This run measured that median at
  **−9.55 on the settled 08-03 bar** (S30's FIRED-A having reversed ~10pp in one session, **D150**),
  and **filed a NEW rejection on MU at EVENT_ALPHA the same day** (`A.flow미도착`, recheck 08-18).
  ⚠ **Two live rejection rows on one name with different conditions is a state the ledger permits and
  nobody has ruled on — named here rather than resolved unilaterally.**

⚠ **This is a clock artifact, not a skipped audit** — the same family as **D155** (`action_bracket`
resolving its folder from `date.today()` mid-run). ⇒ **Both are evidence for one small remedy: a run
should stamp ONE run-date at start and every date-sensitive call should take it, rather than each
call reading the wall clock independently.** Registered as part of **D155**'s remedy note.
