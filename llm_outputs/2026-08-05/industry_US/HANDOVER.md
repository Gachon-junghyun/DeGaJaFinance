# HANDOVER — industry_US · 2026-08-05 (Wed) · STAGE 1, runs before MACRO

## 0. Run clock — and it is the best clock this desk has had in four runs

**09:10 ET · 22:10 KST · 20 minutes BEFORE the US open.**

| | |
|---|---|
| Last settled US equity session | **2026-08-04 (Tue)** |
| Last settled session used by the prior (08-04) run | **2026-08-03 (Mon)** |
| New settled US price information since the last run | **ONE FULL SESSION, and it is the largest single-session macro move in the window** |
| US market state at stage start | **PRE-MARKET (closed).** Equity daily bars for 08-05 **do not exist yet** — verified: `yfinance` returns `NaN` for SPY/XOM/XLB/STX/MU/WDC on 2026-08-05 |
| Futures state | ⚠ **`CL=F` / `HO=F` / `RB=F` DO carry a live 08-05 bar** (75.98 · 3.7730 · 2.5992) — **unsettled, D74, recorded and not used for any verdict** |

★ **This inverts yesterday's constraint in the desk's favour.** The 08-04 run opened by declaring
D74 live because it ran 31 minutes *after* the open. **This run opens 20 minutes before it.** The
pre-commitment is therefore stronger, not weaker:

1. **Every equity price, RS and flow figure in this run is stamped `asof 2026-08-04 settled`.** No
   trimming is needed for equities because no 08-05 equity bar exists — this is stated as a
   *measurement*, not an assumption (the `NaN` row is the receipt).
2. ⚠ **The run WILL cross 09:30 ET.** Any pull made after that point re-enters D74. **SWEEP must
   re-check and trim, and must report which side of the open its cache was built on.**
3. **Commodity futures are already contaminated** and are the one series this desk's live brackets
   turn on. **The 08-05 futures bar is quoted only as 🟡live and carries no verdict.**

---

## 1. Inheritance read — what was opened, and one file could not be trusted as read

| File | Read | Note |
|---|---|---|
| `handoff/STANDING_VIEW.md` (SHARED SPINE) | ✅ **but see the incident below** | §1 regime · §5 retracted ledger R1–**R46** · §6 contradictions C1–C10 |
| `handoff/STANDING_VIEW_US.md` | ✅ | §2 US fact rows (M250→M393) · §3a per-name registry — **intact, authoritative** |
| `handoff/SCENARIOS.md` (SHARED SPINE) | ✅ in full | legend · scoring rules · master log · **master index, 73 brackets (49 US · 24 KR)** |
| `handoff/SCENARIOS_US.md` | ✅ | all 49 US rows status-scanned; **S30 · S31 · S36 · S49 · S52 · S53 · S55 · S57 · S58 · S59 · S60 read in full** |
| `handoff/SCENARIOS_KR.md` | ✅ **checked for past-dated rows this desk owes** | **ZERO.** The 08-05 `industry_kr` run scored its own board and named S17 as the **08-06** run's #1 job. No KR row is past-dated and unowned. |
| `handoff/RESEARCH.md` | ✅ Part A triggers · Part B lenses · Part C dig list (through **D165**) | loaded as **binding constraints**, §6 below |
| `module_report_tags show` | ✅ | reconciled in §5 |

### 🚨🚨 1a. DATA-INTEGRITY INCIDENT inherited — the shared spine was truncated to 0 bytes yesterday

**This is the first thing this stage is obliged to report, ahead of any market view.**

The **2026-08-05 `industry_kr` writeback opened `handoff/STANDING_VIEW.md` in `'w'` mode and raised
`UnicodeEncodeError` mid-serialisation.** Python had already truncated the file. **The shared spine
went to 0 bytes.** It was rebuilt from `handoff/.STANDING_VIEW.bak_0729us` (2026-07-29 23:18) plus
the asof chain. Consequences that **bind this run**:

| Part | State | How this run may use it |
|---|---|---|
| §§1–6, rows **R1–R26** | verbatim from the 07-29 snapshot | ✅ trustworthy, quotable |
| asof chain 07-29 → 08-04 | re-inserted verbatim from live run context | ✅ trustworthy |
| **Rows R27–R45** | **`[RECONSTRUCTED]`, not recovered** | ⚠⚠ **They still BIND — a retracted claim may not resurface — but their NUMBERS may not be quoted as the original measurement.** |
| **R45** | **content not recoverable at all** | 🚨 **A retraction whose content is unknown cannot be checked against.** This run states plainly that it **cannot certify** no claim of its own re-imports R45. |
| **R46** | written fresh 08-05 by the KR run | ✅ complete |
| §2/§3 of the spine | stale **pre-split** copies | ⇒ read the split files; the spine's §2/§3 are ignored |

⇒ **Registered as inherited dig `D165` (human-gated).** ★ **Stated positively, as the rule requires:
the failure mode is one line of code** — the writeback must serialise to a temp file and rename, and
must encode with `errors='surrogatepass'`. **Until a human does that, every writeback in this repo,
including this run's own, is one emoji away from destroying the file it is updating.**
⚠⚠ **This run's own writeback (§10) will therefore write via `Edit`/append semantics, never a
whole-file `'w'` rewrite of a spine.** Pre-committed here, before the writeback happens.

### 1b. §5 retracted ledger read BEFORE forming today's view — the five that bind

- **R46** *(new, 2026-08-05, KR-filed, and it binds the US desk directly today)* — *"a confirmed
  Hormuz reopening normalises the KR lubricant base-oil spread"* is dead as a **category error**:
  **Hormuz is a transit route; the spread was created by a FACILITY** (QatarEnergy Pearl GTL at Ras
  Laffan, force majeure, normal operation guided **end-2027Q1**). **Opening a strait does not repair
  a broken plant.** ⇒ ⚠⚠ **The general form binds this run's central question**: today's tape is
  pricing a Hormuz reopening (§2a). **No stage may assume a strait reopening transmits to a
  product-specific spread without naming the physical object that sets that spread.** This is
  exactly the discrimination **S55** was registered to perform on distillate.
- **R43** — refining profit is **not** generically an inventory artifact (S-Oil printed 21.36%
  inventory contribution and named **정제마진**). ⇒ no stage may argue "the refining print is an
  inventory artifact" as a general property. ⚠ **W1: measured on Korean refiners.**
- **R41** — *"the largest / the most X on the board"* is withdrawn as a **method**. ⇒ **this run may
  not write a superlative about any flow score, short reading or spread without stating the
  population it scanned** (C1/C5).
- **R40** — the **"regulated seven" basket is contaminated** (D is a merger-arb security). ⇒ neither
  S35's nor S47's verdict may be cited about Utilities; both settle **08-07** on the regulated-**six**.
- **R39** — *"XOM is 0% refining"* is dead. ⇒ `CYCLE_EXPOSURE`'s Energy GAP magnitude is `unknown`
  (C3) and **may not be quoted as a level.** ⚠ **S31's own registration text still contains the
  retracted phrase** (*"the one with 0% refining exposure (M146)"*) — **the bracket is scored on its
  frozen observable regardless (a threshold is not re-opened), but its stated MEANING inherits R39
  and this is recorded, not smoothed** (§2c).

⚠ Cross-check performed: **no claim formed in this HANDOVER matches a live retracted entry**, with
the one honest exception that **R45's content is unrecoverable**, so the check is complete against
R1–R44 and R46 and **incomplete by construction against R45.** Stated, not waved.

---

## 2. ★★★ Scenarios — the board's whole Energy complex is being repriced by a news event, one day after the desk bracketed the price move as *"without a Hormuz statement"*

### 2a. The fact that governs the run — and it is the exact object S49-B's registered meaning excluded

`module_news_data search --scope foreign --days 2 Hormuz` → **225 foreign hits, 0 domestic.**
Representative, with source tags (all `[title-only]` unless a body length is shown — **D6 C-grade,
direction only**):

| Source | Headline | Body |
|---|---|---|
| `semafor` | **New deal expected to open the Strait of Hormuz** | 730자 |
| `aljazeera` | **Iran, Oman, US 'close' to Hormuz deal: What do they all want?** | 14,945자 |
| `guardian` | US and Iran signal hope for Hormuz deal but **terms unclear** | 6,842자 |
| `hellenicshipping` | **U.S. aims to announce Hormuz deal by Wednesday, Iran warns of delay** | 2,091자 |
| `fortune` | A deal … **could come as soon as today** — *with a truckload of caveats* | 11,637자 |
| `hellenicshipping` | ⚠ **Strait of Hormuz: Tanker lull PERSISTS despite Trump's peace pledge** | 2,587자 |
| `cnbc` | US Treasury yields fall as traders monitor possible Iran war deal | 1,974자 |

★★★ **The 08-04 settled tape already paid for it, before any deal exists:**

| Series | 08-03 | **08-04 settled** | move |
|---|---|---|---|
| `CL=F` WTI | 80.34 | **75.77** | **−5.69%** |
| `HO=F` heating oil | 3.8772 | **3.7705** | −2.75% |
| `RB=F` gasoline | 2.9667 | **2.8522** | −3.86% |
| `SPY` | 757.67 | **771.33** | **+1.80%** |

⇒ **Two sessions, crude −12.3% cumulative, on expectation alone.**

⚠⚠ **This is the single most important thing this stage hands to MACRO, and it is a contradiction
with the desk's own 24-hour-old verdict.** S49-B fired on 08-03 and its **registered meaning**, quoted
verbatim at scoring, was: *"the bottleneck is releasing — **S8 branch A's economics arriving WITHOUT
a Hormuz statement.**"* **One session later the Hormuz statement is the tape's only driver.**

**What this does and does not do, stated precisely so no later stage over-reads it:**
- **It does NOT unfire S49.** A settled verdict on a frozen observable is not reopened (L3).
- **It DOES trigger S49's registered INVALIDATION path for anything built on top of it**: *"a Hormuz
  reopening statement ⇒ **S8** owns that as a narrative event, not this."* ⇒ **MACRO must adjudicate
  whether a "deal expected / aims to announce" cluster clears S52 branch A's bar, which requires a
  DATED Strait-reopening term in a PRIMARY text.** On this stage's read it **does not yet** — the
  strongest primary-adjacent item says terms are **unclear** and Iran **warns of delay**.
- **It IS precisely what S55 exists to separate.** S55's branch B — *"the distillate premium
  rebuilds ⇒ the collapse was the geopolitical premium deflating across the whole barrel; **ENRG OW−
  must NOT be cut on S49-B**"* — is now the live hypothesis, not the tail one.

★ **The counter-evidence is recorded in the same breath (C2, both halves):** `hellenicshipping`
reports the **tanker lull persists** — i.e. the physical transit data has not moved while the price
has. **Expectation and physical flow disagree, and that gap is the run's central open question.**

### 2b. S55's running value, computed but NOT scored (its window opens today)

S55's anchor is the **2026-08-04 settle** → endpoint **2026-08-11 settle**. **The window has not
elapsed; nothing is scored.** For orientation only, the 5-session (HO% − CL%) through the 08-04
settle reads **−4.76pp** (HO 4.1509→3.7705 = −9.16% · CL 79.26→75.77 = −4.40%). ⚠ **That is the
PRIOR window, not S55's. It is quoted as context and explicitly not as a partial verdict.**

### 2c. ★ The four brackets whose window closes on TODAY'S close — measured on the 08-04 settled bar and PRE-COMMITTED

⚠ **Method note, stated before the numbers.** All four say *"by 2026-08-05"*. **The 08-05 bar does not
exist at this clock.** These rows are therefore **not yet past-dated** and are **not** silent skips.
This stage does the strongest honest thing available: **it measures each on the last settled bar and
pre-commits the verdict**, so the 08-06 run scores against a number written *before* the final bar
rather than after it. **Any row whose final bar changes the branch will be scored on the final bar,
not on this pre-commitment.**

| ID | Frozen observable | **08-04 settled measurement** | Pre-committed verdict | Margin to the line |
|---|---|---|---|---|
| **S30** | median **RS20 vs SPY of {STX, MU, WDC}** crosses **> 0** by 08-05 (A) / stays **≤ 0** (B) | **STX −1.0 · MU −8.0 · WDC −0.1 ⇒ median −1.0** | **B (with us) — provisional** | 🚨 **1.0pp. Knife-edge.** |
| **S31** | **XOM RS20 vs SPY > +10** (A) / **≤ 0** (B) by 08-05 | **XOM RS20 +5.5 · RS60 −0.4** | 🚨 **NEITHER BRANCH — structural `AMBIGUOUS`** | A needs +4.5pp more; B needs −5.5pp |
| **S36** | XLB **5-day excess vs SPY > 0** AND green count still 0 (A) / **≤ 0** or green > 0 (B) | **XLB 52.34 → 52.00 = −0.65% · SPY 740.86 → 771.33 = +4.11% ⇒ excess −4.76pp** | **B (with us)** | **4.76pp inside B.** Effectively locked |
| **S53** | MPC (08-04) + PSX (08-05) guide: capture **stable/improving** (A) / **compression, hedging lag or turnaround drag** (B) / mixed (C) | **Not scoreable at this clock** — PSX prints today | **carried to 08-06** | — |

**★★ S30's compression is itself the finding, and it is bigger than the verdict.** At registration
(07-24 settled) the median was **−23.7**. Yesterday's run measured **−9.55** on the 08-03 bar. Today
it reads **−1.0**. ⇒ **the memory leg has closed 22.7pp of relative underperformance **vs SPY** in nine
sessions and sits 1.0pp from flipping the bracket.** The registered control pair says what that
would mean: **DELL RS20 +8.8 / RS60 +97.5 and HPE +17.4 / +71.0 are BOTH already positive** ⇒ per
S30's own text, *"if both turn it is an IT-beta event, not a memory event."* **The control pair has
already turned. If S30 flips on today's close, the registration pre-commits the reading to
IT-beta.** Recorded now so no later stage can claim a memory call it did not make.

**★★ S31 is a bracket with a HOLE, and that is a finding about its construction (L3), not about the
market.** Branch A needs **> +10**, branch B needs **≤ 0**, and **XOM has sat between them at +5.5
for the whole final week.** Per the L3 rule — *"`AMBIGUOUS` is a finding about the scenario"* — the
defect is recorded: **the two branches do not partition the observable's range, and the modal
outcome (the 0-to-+10 corridor) was assigned no meaning at registration.** ⚠ **And the branch labels
themselves inherit R39** (*"the one with 0% refining exposure"*). ⇒ **S31 must be re-registered by
PREMORTEM with an exhaustive partition, or retired.**

### 2d. Every other ARMED row — classified and checked

**Condition-settled, each compared against today's `[FRED]` pull (asof 08-03/08-04):**

| ID | Kill/branch line | Reading | Buffer |
|---|---|---|---|
| **S9** | real 10y (`DFII10`) **≥ 2.55** | **2.43 (08-03)**, down from 2.47 | ✅ **12bp — the buffer WIDENED**, reversing yesterday's "halved to 8bp" alarm |
| **S23 / S51** | derived 2s10s **≤ +0.20** | `DGS10` **4.70** − `DGS2` **4.25** = **+0.45** (08-03), from +0.47 | **25bp.** ⚠ It **flattened 2bp** — first move toward the line in the window |
| **S26** | HY OAS **≥ 3.10** | **2.78 (08-03)** | **32bp**, widened from 25bp |
| **S41** | IG OAS **≥ 0.90** | **0.78 (08-03)** | **12bp** |
| **S8** | Hormuz *"Strait open"* — **undated `[blank]`** | ⚠⚠ **4th consecutive run carried as un-scoreable — and today it is the most expensive carry on the board.** The desk has an unscoreable bracket on the exact event now driving every price it tracks. **It must be `VOID`ed or re-registered by a human. Named for the fourth time, not dropped.** |
| **S52** | dated Strait reopening **vs** named-infrastructure strike · window **08-06** | **Branch A NOT met on this stage's read** — "expected", "aims to announce", "terms unclear", "Iran warns of delay". **MACRO owns the primary-text adjudication and it is this run's most load-bearing check.** |
| **S57** | XLB 5-session excess **> +1.9** (A) / **< −2.4** (B) by 08-12 | running **−4.76pp** ⇒ **currently inside branch B's region**, 2.4pp past its line. Not scored (window → 08-12) |

**Date-settled, all future — dates recorded, no action:** S2 · S3 (~09/10) · S4 (~09 late) ·
S5 (**08-11**) · S13 (08-12) · S14/S14-num · S16 · S19 · S24 (08-12) · S25 (**08-08**) · S26 (08-12) ·
S35 + S35-ANNEX (**08-07**) · S37 (09-30) · S40 (09-30) · S41 (08-12) · S42 (08-12) · S46 (08-13) ·
S47 (**08-07**) · S48 (09-30) · **S49 (08-06)** · **S50 (08-06)** · S51 (**08-10**, NFP 08-07) ·
**S52 (08-06)** · S54 (08-10) · **S55 (08-11)** · **S56 (08-11, SPCX unlock 08-06)** · S57 (08-12) ·
**S58 (08-11)** · **S59 (08-12)** · **S60 (08-11)**.

**`EXPIRED` = 0 · silent skips = 0 · past-dated rows unscored = 0.**

### 2e. ⚠⚠ Three brackets were registered into the US file by a NON-PIPELINE actor, in Korean

**S58 (MET) · S59 (NDAQ) · S60 (XLE)** carry *"Registered 2026-08-05 by the human-execution loop"*
and are **written in Korean inside `SCENARIOS_US.md`**, which this protocol declares
**English-pure**. Three things are recorded and none is resolved unilaterally:

1. ✅ **They are legitimate and this stage inherits them as binding.** Each brackets a **real
   position change on 2026-08-04** (MET +7sh, NDAQ +7sh, XLE −10sh full exit), each has bands taken
   from its own measured distribution (D93), and **S58's registration text openly logs the buy as a
   protocol violation** — *"a one-way tilt into a known binary"* — and registers the bracket so the
   violation is at least **scoreable**. That is the ledger discipline working, not failing.
2. ⚠ **The language conflict is real and is a human call**, not this stage's. Recorded once.
3. ★★★ **S60 names a genuine instrument GAP and registers `D159` for it: this desk has NO ledger
   that scores a SALE.** `reject_ledger` scores what was not bought; `missed_ledger` scores what was
   not entered; **nothing scores what was sold.** ⇒ carried as this run's **dig rank 2**.

---

## 3. Both ledgers audited — one row was due and it was RESOLVED this run

```
reject_ledger.py due  → 106 rows · 32 resolved · legacy (no revives_if) 0 · recheck-date due 1
missed_ledger.py due  →  56 rows ·  0 resolved · legacy (no enters_if)  0 · recheck-date due 0
```

**The one due row was resolved, not carried:**

| Filed | Ticker | Class | `revives_if` | Measured 08-04 settled | Call |
|---|---|---|---|---|---|
| 2026-07-31 | **MU** Micron | `H.밸류소진` | S30 median RS20{STX,MU,WDC} vs SPY **> 0 on 08-05** **AND** MU OBV → **매집** | median **−1.0** (fails) · MU OBV **분산** (fails) | **`reaffirmed`** — stays out, on **fresh** evidence |

⚠ **Both legs fail, but the first fails by 1.0pp.** The resolution note records that explicitly so a
narrow reaffirm cannot later be quoted as a wide one. ★ **This closes the row the 08-04 run's
post-run note handed forward as "explicitly carried because its condition names an 08-05 US close
that did not exist at that clock."** The other three it named (**316140 · 139130 · CVX**) were
resolved by the 08-05 KR run. ⇒ **zero rows have now crossed two HANDOVERs unexamined.**

- **Rejection ledger: legacy count 0 for a 9th consecutive run**; rows 98 → **106**.
- **Missed ledger: 56 rows (48 → 56), 0 legacy, 0 due.** ⚠⚠ **`resolved = 0 of 56` and it is worse
  in absolute terms for a second straight run.** First rechecks: **08-14 (KR 073240, 000150)**,
  **08-16 (US ADM, CTAS)**, **08-18**. **Named nine days early so it cannot be discovered late.**
- ⚠ **Signs are opposite and are NOT summed.** No combined figure appears in this run.
- ⚠ `missed_ledger score`'s first six rows remain `outcome_selected` (**D106**) — accumulation, never
  an edge. Not quoted.

---

## 4. Exposure state — ★ the transition the last run said would execute, EXECUTED

```
python -X utf8 scripts/exposure_rule.py state   → 2026-08-05, bench 069500.KS, [정착]
```

| Field | 08-04 | **08-05** |
|---|---|---|
| Rule state | 복귀 (⚠전이 보류 복귀→방어 **2/3**) | **방어 (직전 복귀)** — **the transition fired** |
| Bench close | 100,330 (+1.24%) | **104,300 (+3.96%)** · vs 20d high **−13.52%** · vs 20d low **+19.02%** · volume **0.738× [정착]** |
| Target invested | 90% | **55%** |
| Current invested (ledger row) | 70.6% | **71.1%** |
| **Band gap** | 🚨 −19.4pp | 🚨 **+16.1pp (밴드이탈, now OVER-invested)** |
| Ledger depth | 28 rows | **29 rows**; cumulative decomposition **n=4** |

**Cumulative: total excess −9.16pp = cash −4.03pp + selection −5.14pp (n=4).**
⚠ **n=4 is indistinguishable from zero (C4)** and is quoted only to keep the counter rising.

★★ **The 08-04 HANDOVER pre-committed: *"the 90% target is the state the rule is LEAVING, with one
session of life left. A stage that reads 복귀 ⇒ go wide is reading a number that is about to be
replaced."* It was replaced today, and the sign of the band breach INVERTED with it** — from 19.4pp
**under**-invested to 16.1pp **over**-invested, without the book changing size (70.6% → 71.1%).
**The rule moved, not the portfolio.** That is the cleanest illustration this desk has produced of
why an exposure verdict is size context and not a signal.

⚠⚠ **Four caveats, unchanged in force:**
1. **This is the KR book's exposure rule** (`069500.KS`, KR contest bands). **It is NOT a US sizing
   input and no US stage may size off it (W1).**
2. `state` returns **`투자비중미상`** (no account query) while `show` carries the **71.1%** row from
   the timefolio accrual task. **The `show` figure is the one quoted**, discrepancy stated.
3. 🚨 **`ARMED(TIMEFOLIO_EXECUTE=1)` is set in the environment — 3rd consecutive run.** This is a
   **read-only research run**: no orders, no `--execute`, no order-desk staging. Recorded because a
   standing armed flag is something a human should see.
4. **Not cold-starting** (29 rows) ⇒ the verdict is quotable. ⚠ The 08-05 row is tagged
   **`⚠미정착봉(장중·KIS실시간)`** — the KR session was live when it accrued.

---

## 5. Reconciliation — belief vs coverage (`module_report_tags show`)

| Class | Finding |
|---|---|
| **Belief without coverage** | **TSM and LNG** — held names **outside `us_top300`** (M252) ⇒ **no flow, RS or short axis exists for either.** TSM is a rank-1-cycle epicenter holding the grading instrument cannot see. **Unchanged for 7 runs**; needs a universe change (human). |
| **Coverage without belief** | **SPG · ADM · CTAS · TRI · GM** — measured flow rows, no 4Phase ⇒ no thesis may be built on them. Filed as **coverage gaps, not rejections**. |
| **Resolved-but-live** | **PSX** — filed 🔴RESOLVED at ALPHA on 08-02 while `ACTION_TICKETS.md` still carries `CORE-STARTER (BUY) PSX` dated **08-05**. ⚠⚠ `core_pick` is **HUMAN-LOCKED and was NOT modified**. **D19 firing for a 9th consecutive run**; rationale still descends from **R8**, retracted 2026-07-22. ★★ **And today is the ticket's own date, PSX prints today, and the crude complex just fell 12.3% in two sessions.** Named, not fixed. |
| **★ New this run** | **XLE was fully exited 08-04 and is bracketed by S60 — but XLE is itself outside `us_top300`**, which was reason (1) for selling it. ⇒ **the desk sold a position because it could not measure it, and the bracket that scores the sale runs on a series (XLE−SPY) it computes ad hoc.** Consistent, and worth a human's eye. |
| **Silently unindexable** | **28 of 300 universe tickers** return 0 regardless of coverage (M152 `_US_STOP`: A · AIG · ALL · C · CAT · CB · COST · **D** · F · FAST · **GS** · **ICE** · KR · LOW · **MA** · MET · MS · NOW · O · ON · PEG · PM · Q · SO · **T** · TT · **V** · **WELL**). ⚠⚠ **`MET` is on this list and the desk just bought it and bracketed it (S58)** — a "zero coverage" reading on MET is **uninformative**, not evidence, and S58's scoring must not treat silence as a signal. |

---

## 6. RESEARCH triggers loaded as binding constraints — which group binds which stage

| Group | Fires when | IDs | Binds this run |
|---|---|---|---|
| **C** | you cite a number | C1 baseline · C2 both halves · C3 unknown column · C4 indistinguishable · C5 arbitrary choice | **MACRO · every stage.** ★★ **C2 is the run's central rule**: the Hormuz cluster's *expectation* half (price −12.3%) and its *physical* half (tanker lull persists) point opposite ways and **both must be quoted every time either is.** ★ **C1 on watch** — R41 was filed for a C1/C5 failure. |
| **S** | you make a statistical claim | S1 date-fold · S2 null · S3 power · S4 in-sample≠done · S5 short samples · S6 future labels | **Any stage citing a test.** ★ **S1 binds §2c hardest** — four brackets settle on **one** final bar each. |
| **D** | you read data | D1 second venue · D2 proxy sign · D3 signed vs unsigned · D4 regime contamination · D5 cross-provider · **D6 signal grade** | **SWEEP · ALPHA.** ★★ **D74 binds SWEEP the moment the run crosses 09:30 ET.** ★★ **D6 binds every headline in §2a — 225 hits, and the ones that matter are `[title-only]`.** |
| **W** | you write a conclusion | W1 cross-market · W2 inherited lead/lag · W3 real≠profitable · W4 name the customers · W5 sub-sector dispersion · W6 reader's-market spine | **DEEP · BET · ROTATION.** ★★★ **W1 binds three times today**: the KR exposure rule is not a US input; **R43 was measured on Korean refiners**; and **`vol_surge` cleared Bonferroni on the KR ledger while the US ledger reads the OPPOSITE sign** (§9 item 4). **W5 binds every sector verdict** (label-is-the-wrong-unit, measured 5×). |
| **L** | lenses | L1 second derivative · L2 peak-margin trap · L3 branch information content | **DEEP · PREMORTEM.** ★★ **L3 binds S31 directly** — a bracket whose branches do not partition its observable produced `AMBIGUOUS` by construction. ⚠ **L2 unrunnable on 61% of names attempted (M233)** — no cheapness claim where `margin_history` is blank (VLO · XOM · PLD · CSX · UNP · NSC). |

---

## 7. Stale flags and cleared suspensions

| Row | `asof` | Flag |
|---|---|---|
| Seed chain **M1–M19** | 2026-07 / 07-22 | ⚠ **M6 (MU fwd P/E 6.31×) is 14 days stale, superseded twice.** Cite M206. |
| **M22** 3-2-1 crack "99.5th pctile" | 07-21 | ⚠⚠ **DEAD as a level** (R30/D95). **Changes only.** |
| **`DTWEXBGS`** | 07-31 | ✅ suspension cleared 08-04; today reads **119.70 (3m +1.1%)**, mid-range ⇒ **S57's premise confirmed: the Materials dollar leg is dormant by construction.** |
| **`DFII10`** | 08-03 | ✅ **printed 2.43, buffer widened 8bp → 12bp** — yesterday's "closest kill line" alarm partially retracted by the next print. **This is what an honest kill line looks like: it moves both ways.** |
| **COT file** | 07-31 release | 🚨 **Byte-identical stale snapshot; next publication 2026-08-07.** ⇒ **no copper/NDX/WTI positioning percentile may be leaned on this run** (D104/D140 class). Binds SWEEP and PREMORTEM. |
| **`CATALYST_WATCH.json`** | 08-05 | ⚠ **D18 has fired 15+ times across both desks.** Not trusted as the binary source; MACRO re-pulls at ≥10 days (D26). ⚠ **D141: the STRUCTURAL block reads an empty data file.** |
| **`core_pick` / `ACTION_TICKETS`** | 08-02 | ⚠ **D19, 9th run.** Human-locked, stale, **and its date is today.** |
| **000660 ADR flow suspension** | ongoing | **STILL ON.** KR-owned; S17 is the 08-06 KR run's #1 job. **Not a US-desk read.** |

**Cleared suspensions converted to dig instructions: ONE — `DFII10`'s reversal** (above): MACRO reads
the 2.47 → 2.43 print as a *real-rate* observation in its own right, on the same session crude fell
5.7% and SPY rose 1.8%. **Falling real rates + falling crude + rising equities is a coherent
disinflationary-relief signature, and it is the first time in this window the three agree.**

---

## 8. Dig list ranked for today — candidate DEEP assignments

| Rank | Dig | Why it is today's shape |
|---|---|---|
| **1** | ★★★ **Is the Energy repricing EXPECTATION or PHYSICAL?** Price says −12.3% in two sessions; `hellenicshipping` says the **tanker lull persists**. **S55 is the registered instrument and its window opened today.** | **This is the run's central question and it has a bracket, a frozen observable and a live contradiction.** ⇒ **DEEP-ENRG's mandate.** ⚠ **R46's category lesson binds**: name the physical object, do not let "strait" stand in for "spread". |
| **2** | ★★★ **`D159` — the desk has no ledger that scores a SALE.** S60 is a hand-built proxy for one sale. | **A desk that scores rejections and misses but not exits is asymmetric in the one direction that touches realised P&L.** Needs a human; **the instrument that already exists (`reject_ledger`) is 80% of the shape.** |
| **3** | ★★ **S31's branch hole, and S8's 4th unscoreable carry.** | Two Energy brackets are structurally unable to produce information: **S31 has an unassigned modal corridor; S8 has no threshold at all.** **PREMORTEM owns re-registration** — and **S8's object is exactly what is happening today.** |
| **4** | ★★ **The IC ledger's cross-market sign split on `vol_surge`, which today became asymmetric in EVIDENCE, not just in sign.** | **KR cleared Bonferroni today** (h=1 IC −0.0488, t(NW) −2.93, n_eff 18, 필요n reached) and registered **D161**; **US reads +0.0267, t +1.36, n_eff 14, `구분 불가`.** ⇒ **W1: the KR kill does not transfer.** ★ **But the KR interim RULE does transfer as method — no stage cites a green tag without decomposing which axis lit it.** Binds SWEEP/ROTATION. |
| **5** | ★★ **US `rs60` h=1: IC −0.0942, t(NW) −2.54, n_eff 14 — 유의(단독), NOT Bonferroni (|t|>2.8), with a consistent negative sign at two horizons.** | **The desk's own 60-day relative-strength ranking has a negative sign on the US board and it is one step from significance.** ⚠ **Window is a crash + rebound; a crash-window IC does not generalise. Reported, not acted on (P4).** |
| **6** | **D9 · D10 · D11 · D17 · D19 · D20 · D22 · D104 · D141 · D151 · D152 · D155 · D159 · D161 · D165** *(open defects, human-gated)* | Carried forward, not silently re-discovered. **D165 (the truncation) and D155 (the wall-clock date bug) are the two that destroy or falsify data rather than merely cost a stage.** |

**New digs registered by this stage:** none. **ID counters verified at read time** (D137's grep
requirement, run against all `handoff/*.md`): **highest `M###` = M393 · `D###` = D165 · `R##` = R46 ·
`S##` = S60 (US) / S52-KR (KR)** ⇒ this run takes **M394+ · D166+ · R47+ · S61+**.

---

## 9. What this stage hands forward

1. ★★★ **A Hormuz deal is the tape's only driver and the desk bracketed the price move 24 hours ago
   as happening "WITHOUT a Hormuz statement."** S49-B is **not** unfired, but **everything built on
   its meaning is now contingent on S52's primary-text adjudication, which MACRO owns.** On this
   stage's read branch A is **not** met ("expected", "aims to", "terms unclear", "warns of delay").
2. ★★ **C2 is the run's governing rule**: expectation (−12.3% crude) vs physical (tanker lull
   persists) must be quoted together, every time.
3. **Four brackets close on today's close and all four are pre-committed in §2c** — S30 **B at a
   1.0pp margin** (🚨 knife-edge, control pair already turned ⇒ an IT-beta reading if it flips),
   S31 **structurally AMBIGUOUS** (branch hole), S36 **B by 4.76pp** (locked), S53 **carried**.
4. ★★ **`vol_surge` cleared Bonferroni on the KR ledger and the US ledger reads the opposite sign.**
   **W1: do not transfer the kill. DO transfer the method rule — decompose every green tag.**
5. 🚨 **The shared spine was truncated to 0 bytes yesterday and rebuilt; R27–R45 are reconstructed
   and R45 is unrecoverable.** This run's writeback **must not** use whole-file `'w'` rewrite.
6. ⚠ **The COT file is a stale byte-identical snapshot until 08-07** — no positioning percentile may
   be leaned on.
7. **Exposure flipped 복귀 → 방어; target 90% → 55%; band breach INVERTED to +16.1pp over-invested
   without the book changing size.** Size context only; **not a US sizing input (W1).**
8. **Tonight/today is dense: PSX prints (S53) · SPCX unlock 08-06 (S56) · S49 · S50 · S52 all settle
   08-06 · NFP 08-07.** **PREMORTEM must produce both-sides brackets** — a one-way tilt into a known
   binary is a protocol violation, **and S58 exists because that violation already happened once.**

**No position sizing, no buy/sell language appears anywhere in this carry (P4).**

---

## 10 · ⚠⚠ Retention budget — BREACHED, and the growth rate ACCELERATED

`python -X utf8 scripts/handoff_compact.py --budget-only`, run at this stage:

```
RESEARCH.md         279.0 KB   budget  85 KB   OVER by 194   (was 255.1 → +23.9 in one day)
STANDING_VIEW.md    181.8 KB   budget  45 KB   OVER by 137   (was 109.1 → +72.7 ⚠ post-truncation rebuild)
SCENARIOS_US.md     170.7 KB   budget  50 KB   OVER by 121   (was 143.6 → +27.1)
STANDING_VIEW_US.md 159.7 KB   budget  50 KB   OVER by 110   (was 145.1 → +14.6)
STANDING_VIEW_KR.md 141.9 KB   budget  50 KB   OVER by  92
SCENARIOS_KR.md      78.6 KB   budget  50 KB   OVER by  29
SCENARIOS.md         74.6 KB   budget  20 KB   OVER by  55   (was  54.8 → +19.8)
--------------------------------------------------------------
US run reads        877.4 KB   budget 250 KB   OVER by 627 KB   (was 719.3 → +158.1 in ONE day)
KR run reads        767.5 KB   budget 250 KB   OVER by 518 KB   (was 625.2 → +142.3 in ONE day)

§2 fact rows: 461 (was 289) · avg 0.55 KB/row · rule is <= 0.35 KB/row
fattest: M340 1.21 KB · M386 1.10 KB · M152 1.04 KB
```

★★ **The growth rate the 08-03 run asked for is now measured twice, and it went up six-fold.**
A US run's read cost grew **+25.3 KB** on 08-04 and **+158.1 KB** on 08-05. **Fact rows went 289 →
461 (+172) in a single day.** At yesterday's rate the US read passed 1 MB in ~11 runs; **at today's
rate it passes 1 MB in ONE run.**

⚠ **Part of today's +72.7 KB on the spine is the truncation rebuild, not new content** — stated so
the acceleration is not over-read. **The other ~85 KB is genuine.**

★ **Stated positively, as the rule's framing requires**: the instrument exists
(`handoff_compact.py`), it is **non-destructive by design** (facts *move* to `ARCHIVE_FACTS.md` and
stay greppable — the 07-25 pass lost **0 of 154**), and the precedent shows it works.
**What is missing is that nobody runs it.**

⚠⚠ **And today the ask changes character.** For two runs this was an efficiency item. **After the
08-05 truncation it is a SAFETY item**: the larger these files get, the longer every writeback holds
a `'w'` handle open, and the more a single encoding fault destroys. **A human should schedule
compaction between runs — and fix the writeback's temp-file-and-rename before the next one.**
★ **Third consecutive run naming compaction; first run naming it as a safety issue rather than a
size one.**
