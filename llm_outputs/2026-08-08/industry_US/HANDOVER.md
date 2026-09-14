# HANDOVER — industry_US · 2026-08-08 (Sat) · Stage 1/10 (L1·HANDOVER)

> Zero buy/sell language anywhere in this file (P4). This stage transports analysis, never a recommendation.

## 0. Run clock — and the structural fact that defines this run

**2026-08-08 09:10 ET (Sat) · 22:10 KST.** **The US market is CLOSED and has been since Friday's
16:00 ET settle.**

★★★ **This is the first `industry_US` run in four with a fully settled price panel and therefore
`D74` contamination = 0.** The 08-04 run self-reported *"its honest weakness is its CLOCK: it ran
10:0x–11:2x ET with the US market OPEN"*; the 08-06 and 08-07 runs carried the same defect. Today
every price object in this file is a **settled 2026-08-07 daily close**, verified by pulling the
index tail (`last bar: 2026-08-07`) rather than assumed.

⇒ **Two consequences that bind every downstream stage:**
1. **Promotions and demotions are allowed in both directions this run.** The three prior runs had to
   treat contamination sign as a composition rule because the bias only ran one way. There is no
   bias to correct for today.
2. **The 2026-08-07 close is the bar every bracket dated 08-07 freezes on** — so this run owns
   scoring jobs the 08-07 run could only pre-commit to.

⚠ **What being closed costs, stated up front**: there is **no new US session** since the last run, so
every *price* observable moves by exactly one bar and no more. **The new information in this run is
(a) the settle itself, (b) FRED's 08-06 close, which the 08-07 run did not have, and (c) the CFTC COT
release that published 15:30 ET Friday** — after the 08-07 run's own stages had finished.

---

## 1. Inheritance read — what was opened, in full

| File | Read | Note |
|---|---|---|
| `handoff/STANDING_VIEW.md` (shared spine) | ✅ | §1 regime · §2 seed chain · §4 asymmetry · **§5 retracted ledger** · §6 open contradictions · full asof chain to the 2026-08-08 KR entry |
| `handoff/STANDING_VIEW_US.md` | ✅ | §2 US fact rows through **M466–M486** (08-07) · §3a per-name registry incl. the 08-07 overwrites |
| `handoff/SCENARIOS.md` (shared spine) | ✅ | MASTER scoring log **and** MASTER INDEX (**80 brackets — 54 US-owned · 26 KR-owned**) |
| `handoff/SCENARIOS_US.md` | ✅ | every ARMED row's branch text re-read at source, **not from the prior HANDOVER's summary** |
| `handoff/SCENARIOS_KR.md` | ✅ **opened, as the spine rule requires** | checked for any past-dated row this desk must score — **none** (the 08-08 KR run closed its queue; next KR settle is 08-11/S22). **S56-KR registered by that run 08-08** |
| `handoff/RESEARCH.md` | ✅ | Part A triggers (C/S/D/W) · Part B lenses (L1–L3) · **Part C dig list through D202–D210 (US) and D202-KR–D214-KR + D211 (KR)** |
| `module_report_tags show` | ✅ | `DEGAJA_REPORT_DIR=llm_outputs`, **exit 0** (the KR run's `exit 255` did **not** reproduce under this invocation — recorded as a null result, not a fix) |

### 1a. The data-integrity incident still binds this run's writeback

`STANDING_VIEW.md` was truncated to 0 bytes on 2026-08-05 by a `'w'`-mode writeback that raised
mid-serialisation. **D165's pre-commitment — append only, never a whole-file rewrite of a spine —
has now held for six consecutive runs (five US + the 08-08 KR run) and this run keeps it a seventh.**
⚠ Rows **R27–R45 remain `[RECONSTRUCTED]`**: their CLAIM and KILLER are right, their measured detail
is lost. They bind (a retracted claim may not resurface) but **their numbers may not be quoted as
original measurements.**

### 1b. §5 retracted ledger read BEFORE today's view formed — the six that bind

| # | What may not resurface | Binds which stage today |
|---|---|---|
| **R56** | **"COMM's flow is breadth-led"** — half its carrier (**EA**) is a **delisted** security, price frozen 209.70 on two zero-volume bars after a $55bn go-private. **COMM = UW.** | **SWEEP · ROTATION** — any COMM breadth claim must be re-derived **ex-EA**, and the universe defect (**D207**) is still open today |
| **R57** | **"FIN eqflow is the 2nd-lowest of 16"** — it was the **4th**. The conclusion (bottom-quartile, never negative, OW− stands) survived; the rank did not | **every stage** — a rank quoted off a truncated series is a **C1** violation |
| **R58** | **"VST reports AMC"** — it reported **pre-market** 08-07. Two PREMORTEM lenses made that error from opposite directions | **PREMORTEM** — and see §2a: the settle now shows what actually happened |
| **R59** | **"`velocity` is populated on mcap-ranks 1–51"** — it is a **stable ~50-name whitelist**; the `names` array sorts by `flow_score`, not mcap. The 🟢-gate defect is **structural and permanent** | **SWEEP · ALPHA** — the D161 interim rule (no stage cites a 🟢 tag without decomposing which axis lit it) is **not optional** |
| **R60** (KR-registered, 08-08) | **"the polysilicon 232 tariff applies origin-blind"** — origin **determines** the rate (Korea capped at 15% combined, same treatment as EU/JP/TW/CH/LI) | **W1** — this is a KR row; it is carried as a *method* lesson (a category error: item-scope vs origin), **not** imported as a US fact |
| **R46** | M-19″'s kill condition named **Hormuz (a strait)** while the mechanism runs on **Pearl GTL (a facility)** — a **category error**, not a magnitude error | **PREMORTEM · MACRO** — every bracket registered today must name the object the mechanism actually runs on |

★ **The class these six share is worth stating once**: **four of the six are object-identification
errors** (wrong security, wrong estimator, wrong print time, wrong gate mechanism), not wrong
directional calls. **This desk's dominant failure mode is naming the wrong object, not reading the
right object wrongly** — and §2c below adds a fifth instance from yesterday's own file.

---

## 2. ★★★ Scenarios — the run's #1 job executed: **S62 FIRED-B**

### 2a. S62 — scored on the settled 2026-08-07 close

**Frozen observable**: (median RS20 vs SPY of {EMR, ETN, AME, PWR}) − (XLU RS20 vs SPY), settled
closes, benchmark SPY inline. **Branch A ≤ −5.91 · B ≥ +7.42 · C between.**

✅ **Estimator verified before scoring (C1).** The convention was re-derived from scratch and
reproduced the 08-07 HANDOVER's independently-computed **08-06** figures on **every leg**:

| Leg | this run's 08-06 recompute | 08-07 HANDOVER printed | gap |
|---|---|---|---|
| EMR | +11.626 | +11.63 | 0.004 |
| ETN | +8.196 | +8.20 | 0.004 |
| AME | +5.651 | +5.65 | 0.001 |
| PWR | −2.291 | −2.29 | 0.001 |
| median | +6.924 | +6.925 | 0.001 |
| XLU | −6.119 | −6.12 | 0.001 |
| **spread** | **+13.043** | **+13.045** | **0.002** |

**The settle (2026-08-07):**

| Leg | RS20 vs SPY |
|---|---|
| EMR | **+11.529** |
| ETN | **+7.740** |
| AME | **+5.986** |
| PWR | **−0.406** |
| **median** | **+6.863** |
| XLU | **−6.389** |
| **SPREAD** | **+13.252** |

> **`S62 · 2026-08-07 · FIRED-B · observed: +13.252 · threshold was: B ≥ +7.42`**
> **What it does to the standing view: it does NOT support "INDU OW− and UTIL UW are one bet".**
> The two labels' spread stayed near its 85th-percentile tail for the whole window, i.e. the tilts
> are **separable on this observable**, and the correlated-tilt objection PREMORTEM raised is not
> confirmed by its own registered test.

⚠⚠ **And the fire is worth almost nothing, by the bracket's own registration — this is `D206` confirmed
on the settle.** Branch A sat **19.16pp away** on the final bar. The pre-commitment was written on
08-06 (*"B, and the condition under which that is wrong is XLU gaining ≈5.6pp on the INDU median in
one session"*), and **the actual session moved the spread +0.21pp.** ⇒ **a partition that was valid at
registration became degenerate before its settle.** The staged rule from D206 — *re-check branch
reachability at every HANDOVER and record when a branch becomes unreachable so its settle is not read
as earned* — is **executed for the whole board in §2c below, for the first time.**

★★ **The named contamination mechanism did NOT fire, and now we can say so with the settle rather
than a forecast.** The 08-07 run flagged that **VST prints from inside XLU** and a large beat would
compress the spread toward A without moving the leg the spread is long. Measured on the settle:

- **VST −0.56% on 08-07** · **XLU +0.53%** · **SPY +0.61%** ⇒ **XLU lost 0.08pp to SPY on the day.**
- ⇒ VST's print was a non-event for the spread. **The spread widened +0.209pp, in the direction the
  bracket was already tracking.**
- ★ **This also settles R58's practical stake**: the AMC/BMO error was real and the primary source
  refuted it correctly — **and it turned out not to matter for S62's verdict.** Both halves are
  recorded. **Being right about the mechanism and wrong about the consequence is still being right
  about the mechanism** (`R58` is not weakened), but the desk should not claim the correction
  *changed* an outcome. It did not.

### 2b. Every other ARMED US row — re-measured at source on the settled bar

⚠ **Every branch line below was re-read from `SCENARIOS_US.md` itself, not inherited from the 08-07
HANDOVER's summary table.** §2c explains why that mattered this run.

**Price/level-settled rows, on the 2026-08-07 settle:**

| ID | Frozen observable | Reading (08-07 settled) | vs 08-06 | Branch region | Settles |
|---|---|---|---|---|---|
| **S57** | XLB 5-session excess vs SPY | ★★★ **+1.307** | **−2.596 → +1.307 = a +3.90pp swing in ONE session** | ⚠ **left branch B, now 0.593pp BELOW branch A (+1.9)** — and **A fires at ANY settled close through 08-12** | 08-12 |
| **S61** | EW {STNG, FRO} 5-session excess vs SPY | ★★★ **−4.184** (STNG −5.797 · FRO −2.571) | −2.472 → −4.184 | ⚠⚠ **0.006pp from branch B's line (≤ −4.19)** — B settles only at the 08-12 close | 08-12 |
| **S55** | (HO=F %chg − CL=F %chg) from the **08-04 anchor** | **+0.318pp** (HO +3.498% · CL +3.181%) | — | **C**, deep in it: A needs −3.32pp more, B needs +6.18pp more | 08-11 |
| **S60** | XLE 5-session excess vs SPY | **−6.954** | — | ⚠ **already 1.90pp past branch B's line (≤ −5.05)** | 08-11 |
| **S65** | median RS20 vs SPY {JPM, BAC, WFC, BRK-B} | **+3.352** (JPM +3.83 · BAC +3.44 · WFC −2.32 · BRK-B +3.26) | +3.805 → +3.352 | **C** (A ≤ +0.34 · B ≥ +6.81) | 08-11 |
| **S67** | median RS20 vs SPY {MPC, VLO, PSX} | **+3.852** (MPC +2.67 · VLO +3.85 · PSX +5.83) | — | tracking; all three legs positive | 08-13 |
| **S68** | leg (i) median RS20 {DIS, EA} — **VOID by construction** (S68-ANNEX) · leg (ii) DIS revision breadth | **DIS RS20 +7.290**; leg (ii) not pulled at this stage | — | leg (i) unscoreable, leg (ii) stands | 08-13 |
| **S69** | MET RS20 vs SPY, quoted with FY revision breadth | **MET RS20 +4.252** | — | tracking | 08-13 |
| **S58** | MET cumulative excess vs SPY, first **3** settled sessions after the 08-05 AMC print | **+1.118pp at 2 of 3 sessions** (08-06, 08-07) | — | **C** (A ≥ +2.45 · B ≤ −2.70). **3rd session = 08-10** | 08-11 |
| **S59** | NDAQ − XLF 10-session cumulative **AND** 2s10s rising | **+0.424pp**; **2s10s fell 08-05→08-06 (+0.45 → +0.44)** ⇒ **the conditioning leg is currently NOT satisfied** | — | **C by the condition, not by the level** — exactly what the registration predicted would be frequent | 08-12 |
| **S30** | scored **FIRED-B** 08-05 | context only, not reopened | — | — | closed |

**Condition-settled rows, against this run's `[FRED]` pull (`asof` 2026-08-06 for the yield/credit
block — one day fresher than the 08-07 run had):**

| ID | Kill / branch line | Reading (08-06) | Buffer | Δ vs the 08-05 read |
|---|---|---|---|---|
| **S9** | real 10y (`DFII10`) **≥ 2.55** | **2.43** | **12bp** | ⚠ narrowed **14 → 12bp** — third consecutive narrowing |
| **S23 / S51** | derived 2s10s **≤ +0.20** | `DGS10` **4.69** − `DGS2` **4.25** = **+0.44** | **24bp** | ⚠ narrowed **25 → 24bp** — the widening the 08-07 run recorded did not continue |
| **S26** | HY OAS **≥ 3.10** | **2.71** | **39bp** | ★ **WIDENED 35 → 39bp — credit TIGHTENED into the print** |
| **S41** | IG OAS **≥ 0.90** | **0.78** | **12bp** | unchanged (4th consecutive unchanged read) |
| **S8** | Hormuz *"Strait open"* — **undated `[blank]`** | 🚨🚨 **SEVENTH consecutive run carried as un-scoreable.** Must be `VOID`ed or re-registered **by a human (P5)**. Named again, not dropped | — | — |

★★★ **S66 is correctly NOT scoreable, and the reason is now a measurable defect rather than a wait.**
S66's observable is **ΔDGS2 + ΔHY OAS from the 08-05 anchor, at the first `[FRED]` close covering the
08-07 NFP print.** `DGS2`, `DGS10`, `DFII10`, `BAMLH0A0HYM2` all stop at **08-06** ⇒ the print is
still uncovered and **S66 stays ARMED, expect 08-10** exactly as registered.

⚠⚠ **But one FRED series in the same pull DOES carry an 08-07 value — and it is arithmetically
derived from two that do not.** `T10YIE` (10y breakeven) prints **2026-08-07 = 2.25** (from 2.26),
while `DGS10` and `DFII10` — whose difference *is* `T10YIE` — both stop at 08-06. **⇒ FRED already
holds the 08-07 nominal and real 10y; this feed's per-series publication lag hides them.**
⇒ **new dig `D212`.** What it costs while open: **the desk's single most consequential open branch
(*was 08-07 dovish relief or credit fear?*) is blocked on a lag that a sibling series demonstrates is
not a data-availability limit.** ⚠ **What the breakeven alone can and cannot say (C3/C4)**: 10y
breakeven **fell 1bp on the NFP session**. That is a *mild* disinflation tick and it **does not
decompose into nominal vs real**, so it **may not be used to settle S66 or to call the direction.**
Recorded as an observation, not an answer.

**Date-settled, all future — dates recorded, no action:** S2 · S3 (~09/10) · S4 (~09 late) ·
**S5 (08-11)** · S13 (08-12) · S14 / S14-num · S16 · S19 · S24 (08-12) · **S25 (08-08 — already
FIRED and pre-declared ZERO-INFORMATION on 08-02, `D122`; today is its nominal date and there is
nothing to score)** · S26 (08-12) · S37 (09-30) · S40 (09-30) · S41 (08-12) · S42 (08-12) ·
S46 (08-13) · S48 (09-30) · **S51 (08-10)** · **S54 (08-10)** · **S56 (08-11)** · S57 (08-12) ·
**S63 (08-13, CPI 08-12)** · **S64 (08-13)** · **S66 (expect 08-10)**.

**`EXPIRED` = 0 · silent skips = 0 · past-dated rows unscored = 0.**

### 2c. ★★ D206's staged rule executed for the first time — branch REACHABILITY across the board

The staged rule from the 08-07 run: *re-check every armed bracket's branch reachability against the
current level at each HANDOVER, and record when a branch becomes unreachable so its settle is not read
as earned.* Executed:

| ID | Nearest branch | Distance | Reachable in the remaining window? |
|---|---|---|---|
| **S62** | A | **19.16pp** | ❌ **NO — settled today as one-way confirmation.** `D206` confirmed on the settle |
| **S57** | **A** | **0.59pp** | ✅ **YES, and A fires at ANY close through 08-12** — the most live row on the board |
| **S61** | **B** | **0.006pp** | ✅ **YES** (B settles at the 08-12 close only) |
| **S60** | **B** | **already past by 1.90pp** | ✅ needs only to hold to 08-11 |
| **S58** | A | 1.33pp, **one session left** | △ possible but tight |
| **S65** | A 3.01pp / B 3.46pp | ~symmetric | ✅ genuinely two-sided |
| **S55** | A 3.32pp / B 6.18pp | asymmetric | △ A reachable, B unlikely |
| **S59** | — | blocked by its **2s10s conditioning leg**, not by level | ⚠ a *conditional* C, which the registration disclosed |
| **S68** | leg (i) | **VOID by construction** | ❌ leg (ii) only |

★ **The finding this produces is not about any one row**: **of nine live US brackets, one settled
degenerate, one is void on half its construction, and one is blocked by a conditioning leg — so a
third of the board could not have paid information this week regardless of what the market did.**
That is a **registration-quality** statistic, and it is the first time this desk has been able to
state one.

### 2d. 🚨 A correction to yesterday's own HANDOVER — the S61 row was read on the wrong estimator

The 08-07 HANDOVER's §2c table reported **S61** as *"STNG −2.07 · FRO +5.96 · ★★ FRO has FLIPPED
POSITIVE (−4.55 → +5.96) and STNG improved sharply (−7.51 → −2.07)"*.

**Those are RS20 values. S61's frozen observable is a 5-session cumulative excess.** On the bracket's
own axis, the same 08-06 bar reads **STNG −2.50 · FRO −2.45 · EW −2.472** — **FRO was negative, not
positive.**

| 08-06 bar | 5-session excess (**the bracket's axis**) | RS20 (**what was quoted**) |
|---|---|---|
| STNG | **−2.50** | −2.07 |
| FRO | **−2.45** | **+5.96** |

⇒ **the row's reported direction was inverted by an estimator substitution.** ⚠ **And it was not
cosmetic**: on the correct axis the row has since moved to **−4.184, six thousandths of a point from
branch B**, which the RS20 reading would never have surfaced. **This is `C1`'s failure mode — quote
the estimator the bracket froze, not a sibling that shares its inputs** — and it is the **fifth
object-identification error** in the class §1b names. ⇒ **new dig `D213`**, and this run's operating
rule: **every branch line is re-read from `SCENARIOS_US.md` at source each HANDOVER** (done above).

⚠ **Scope (C4)**: this corrects **one row's reading in one file**. It does **not** retract S61, whose
registration text and bands are untouched, and it does **not** imply the 08-07 run's other rows were
mis-estimated — S62's were verified to 0.002pp in §2a.

---

## 3. Both ledgers audited — `due` empty, legacy zero for a **12th** consecutive run

```
reject_ledger.py due  → 127 rows · 44 resolved · legacy (no revives_if) 0 · recheck-date due 0
missed_ledger.py due  →  81 rows · 34 resolved · legacy (no enters_if)  0 · recheck-date due 0
```

⚠⚠ **A clean `due` is not proof of a healthy ledger — the unit says so and this run obeys it.**
Growth since 08-07: rejections **120 → 127 (+7)**, resolutions **42 → 44 (+2)**; missed **73 → 81
(+8)**, resolutions **32 → 34 (+2)**. **The legacy count is the only real evidence the practice is
taking hold, and it is 0 for a 12th run.**

⚠ **The two ledgers' `excess` columns are NOT summed anywhere in this run** — their signs are
inverted relative to each other (`reject`: `excess > 0` = the rejection cost us; `missed`:
`excess > 0` = missing it cost us).

⚠ **`missed_ledger score`'s seeded block remains outcome-selected** (its first 6 rows came from
`leak_scan --top`). **Class means from that stratum are accumulation, never an edge estimate**, and
none is quoted here.

---

## 4. Exposure state — `방어`, and it is **KR-only** (W1)

```
exposure_rule.py state → 2026-08-07 (settled) · bench 069500.KS 98,090 · −0.819% on the day
                         20d-high −18.67% · 20d-low +11.93% · volume 0.604× [settled]
                         상태 방어 (prior 방어) · target invested 55% · current % 🚨 unknown
```

- **Verdict `방어`** on all four legs, unchanged from the 08-07 read. **Target invested 55%.**
- 🚨 **Current invested % is UNKNOWN** — the account query is not run (`투자비중미상`). Per **P5** no
  number is substituted for the band gap.
- **Ledger `show` returns 31 rows, so this is NOT a cold start** and the verdict may be quoted as
  reliable (contrast the 2026-07-31 cold-start incident where `방어`/−1.9pp became `복귀`/−37.2pp
  after backfill).
- **Cumulative decomposition, n = 4**: total excess **−5.68pp** = cash **−2.03pp** + selection
  **−3.65pp**. ⚠ **n = 4 with overlapping regime; indistinguishable from zero (C4).** The series has
  now moved **−9.16 → −2.13 → −5.68 → −5.68** across four runs.
- ⚠ **The 2026-08-07 ledger row is stamped `live`, not `settled`** — it was accrued intraday at
  55.5% invested. **The decomposition therefore rests on an unsettled bar (D74 inside the ledger
  itself)**, which is a different object from this run's own settled price panel. Flagged, not fixed
  (the 09:10/15:00 timefolio tasks own accrual; a research run must not write a second row).
- ⚠⚠ **W1 binds hard here: this is a KOSPI-benchmarked KRW book. It is NOT a US sizing input.**
  It is carried because BET/ALPHA must know a candidate list has a size context at all — not because
  55% means anything on the US board.
- ⚠ **`🚨🚨ARMED(TIMEFOLIO_EXECUTE=1)` is set for a 6th consecutive run.** **This run touches nothing
  executable and issues no order of any kind.**

---

## 5. ★★ The signal scoreboard — the US board's own axis is **0.03 from Bonferroni**

`axis_inflection.py` → `ic_ledger.py log` → `log --market us` → `score --market us`.
✅ **`--market us` was passed this run** (the `D203` defect that starved the US ledger for four runs).
**15 new US rows accrued; n went 18 → 19.**

| Market | Axis | h | n | n_eff | mean IC | t(NW) | positive | 필요n | verdict |
|---|---|---|---|---|---|---|---|---|---|
| **US** | **`rs60`** | 1 | **19** | 19.0 | **−0.0817** | **−2.77** | **21%** | **10 (reached)** | **유의(단독)** — **0.03 short of Bonferroni \|t\|>2.8** |
| **US** | `vol_surge` | 1 | 19 | 19.0 | **+0.0306** | +1.80 | 58% | 25 | 구분 불가 — **and the sign is OPPOSITE KR's** |
| **KR** | `vol_surge` | 1 | 21 | 21.0 | −0.0340 | **−2.06** | 33% | 21 | 유의(단독), **5th consecutive retreat** |

★★★ **`rs60`'s trajectory is the run's most important instrument observation.** Across four accruals:
**t −2.54 (n=14) → −2.67 (n=18) → −2.77 (n=19)** — **the |t| has risen monotonically with n while the
mean IC held near −0.08.** After the `mention_z` episode (필요n 44 at n=7 → 757 at n=14) a signal that
strengthens through two n-jumps is the opposite shape.

- ★ **And it agrees across all three horizons**: h=1 **−0.0817** · h=5 **−0.1647** · h=10 **−0.2937**,
  **all negative, 21% / 0% / 0% positive.** ⚠ **The h=5 and h=10 cells are `n_eff` 2.8 and 1.0 and are
  NOT quoted as evidence** — only their **sign agreement** is, which is the D105 check.
- **What this would mean if it clears**: **60-day relative strength INVERTS forward returns on the US
  board.** That is a direct challenge to how EVENT_ALPHA, ROTATION and BET currently read RS60 as a
  strength axis. ⛔ **It has not cleared, and nothing is changed on it this run (P4).**
- ⛔ **The `sector_flow` gate change stays un-made, and the reason is now sharper**: the module weights
  `vol_surge` **positively**; **KR measures it negative (t −2.06) and the US measures it POSITIVE
  (t +1.80).** ⇒ **W1 — neither market's reading may be imported into the other, and a live shared
  module is not flipped on two results that disagree in sign.**
- ✅ **The D161 interim rule stands and BINDS SWEEP · ROTATION · ALPHA**: *no stage cites a 🟢 tag
  without decomposing which axis lit it.* **R59/D205 is why** — the `velocity` gate is a **name
  whitelist**, so a sector whose names sit outside it can never produce a velocity-lit green on any run.
- ⚠ **`n_eff < 4` cells (7 of 15 US, 14 of 21 KR) are quoted nowhere in this run** except for the
  sign-agreement check above.
- ⚠ **Regime label, as the unit requires**: the window is a **crash-plus-rebound-plus-payroll-shock**
  stretch. **A crash-window IC does not generalise.**

---

## 6. Reconciliation — belief vs coverage (`module_report_tags show`)

`DEGAJA_REPORT_DIR=llm_outputs`, **exit 0**, **241 `industry_US` report rows** indexed.

| Class | Finding |
|---|---|
| **Belief without coverage** | **XOM** — carried in `SCENARIOS_US.md` S31 throughout as *"the only Energy name the book holds"*, while `cycle_exposure` reads the held Energy epicenter as **MPC, PSX**. **The bracket has been describing a position that does not exist** (found 08-06, still open). ⇒ **PREMORTEM must re-register S31 with an exhaustive partition or retire it.** XOM's settled RS20 today is **+7.77** and RS60 **−3.15**, i.e. still inside the unassigned corridor that made S31 `AMBIGUOUS` twice |
| **Coverage without belief** | **VST** — carried in the flow tags and named in R58, sits inside XLU (one of S62's two legs), **printed pre-market 08-07**, and its settled **RS20 is −13.93 / RS60 −9.03** — the weakest of any name touched in this file. **No standing thesis owns it.** Candidate DEEP or a rejection-ledger row |
| **Resolved-but-live** | **EA** — 🔴 by every mechanical test (delisted, zero volume, frozen price) and **still in `us_top300.csv`**. `D207` is unfixed at this stage (see §7) |
| **Ledger mode used** | `DEGAJA_REPORT_DIR=llm_outputs` for the **query**; finalized reports are **copied into `REPORT/industry_US/`** at run end per the task file's resolution of the PROMPT_MAP §6 open decision. **Stated, as the protocol requires.** |

---

## 7. Stale flags and cleared suspensions

| Item | State | Converted to |
|---|---|---|
| 🚨🚨 **`data/us_universe/us_top300.csv`** | **24 days stale** (built 2026-07-15) and **contains a delisted constituent (EA)**. The `sector_flow.py` staleness guard **fires but tests the wrong property** (stale mcaps, not constituent liveness) | ⚠ **SWEEP must read the sweep's stderr in full this run** — the 08-07 run redirected it to a log and read only the tail, which is how EA passed. **Recorded as a binding instruction to stage 2, not a hope** |
| ✅ **CFTC COT** | **The 6-read stale streak is BROKEN** — the release published **15:30 ET Friday 2026-08-07**, after the 08-07 run's stages had finished | **A cleared suspension is a dig instruction, not a silent trust**: SWEEP/MACRO must pull it and **verify the file is not byte-identical to the 07-31 snapshot** before quoting any percentile. Copper's 96th percentile has been unquotable for six reads |
| **`DTWEXBGS` (dollar)** | last print **2026-07-31 = 119.7034**, **5 publication days ago** — mid-range against S57's dormant `[117.44, 121.41]` leg | Carried. **The MATR dollar leg remains dormant by construction** — which is exactly why S57's price leg (now 0.59pp from branch A) is the live falsifier |
| **FRED yield/credit block** | `asof` **2026-08-06** — **does not cover the 08-07 NFP print** | **S66 stays ARMED, expect 08-10.** ⇒ **`D212`** (T10YIE prints 08-07 while its own two inputs stop at 08-06) |
| **`drift_watch.py`** | unrunnable remotely for a **3rd** consecutive run (deployment lag: `DB_READ_CMDS` holds `drift`, the server allow-list does not) | **DRIFT (stage 10) runs by substitution and must say so** |
| **R27–R45** `[RECONSTRUCTED]` | binding but un-quotable as measurements | carried |

---

## 8. RESEARCH triggers loaded as binding constraints — which group binds which stage

| Group | Fires when | IDs | Binds today |
|---|---|---|---|
| **C** | you cite a number | C1 baseline · C2 both halves · C3 unknown column · C4 "indistinguishable" · C5 arbitrary choice | **MACRO · every stage.** ★ **C1 is the run's sharpest live constraint** — it produced §2a's estimator verification **and** §2d's correction of yesterday's row |
| **S** | you make a statistical claim | S1 date-fold · S2 diagnose the null · S3 power first · S4 in-sample≠done · S5 short samples · S6 future labels | **any stage citing a test.** **S1 binds §5's n=19 and §4's n=4** |
| **D** | you read data | D1 second venue · D2 proxy sign · D3 signed vs unsigned · D4 regime contamination · D5 cross-provider · **D6 signal grade (OBV is C)** | **SWEEP · ALPHA · L2 indicators · L2 money_trail.** ★ **D6 + D208 together**: `module_flow` and `module_chart` both print an axis called "OBV" from **different statistics** and disagreed in **sign** on MPC — **citing one against the other is the error** |
| **W** | you write a conclusion | W1 cross-market transfer · W2 inherited lead/lag · W3 real≠profitable · W4 name the customers · W5 sub-sector dispersion · W6 reader's-market spine | **DEEP · BET · ROTATION.** ★ **W1 binds three separate objects today**: the exposure state (KR book), R60 (a KR retraction), and the `vol_surge` sign disagreement |
| **L** (lenses) | — | L1 second derivative · L2 peak-margin trap · L3 branch information content | **DEEP · PREMORTEM.** ★ **L3 is elevated this run** — §2c is an L3 audit of the whole board, and **PREMORTEM must apply reachability BEFORE freezing any new bracket** |

⚠ **Loaded as constraints, not as a summary.** Three of the 2026-07-22 session's six reversals broke
rules that already existed in prose nobody carried into working constraints. **§2a, §2c and §2d are
this run's evidence that they were carried.**

---

## 9. Dig list ranked for today — candidate DEEP assignments

| Rank | Dig | Why it is today's | Owner stage |
|---|---|---|---|
| 1 | **D207** — universe staleness + no liveness assertion | **The one defect that already produced a wrong sector delta (R56).** Cheapest three checks, any one of which catches EA: last settled volume ≠ 0 · `Open≠High≠Low≠Close` not degenerate over two bars · no Form 25/25-NSE in 30 days | **SWEEP** (read stderr in full; assert liveness on any 🟢 before it reaches ROTATION) |
| 2 | **S57 at 0.59pp from branch A** | The most reachable branch on the board, on a sector the desk holds **UW−** with **no other live falsifier**, while its dollar leg is dormant | **ROTATION · PREMORTEM** |
| 3 | **D205 / R59** — the `velocity` name whitelist | **Structural and permanent**: a sector outside the ~50-name list can never produce a velocity-lit green. Every 🟢 must be decomposed | **SWEEP · ALPHA** |
| 4 | **XOM ∉ book, S31 describes a phantom position** | Two consecutive `AMBIGUOUS` verdicts on a bracket about a holding that does not exist | **PREMORTEM** (re-register exhaustively or retire) |
| 5 | **VST — coverage without belief**, RS20 −13.93 after a pre-market print inside XLU | An un-owned name that moved one of this run's own scored brackets | **DEEP-UTIL or a rejection-ledger row** |
| 6 | **D212** (new) — T10YIE prints ahead of its own inputs | Blocks the desk's most consequential open branch on a lag that is demonstrably not a data limit | human-gated |
| 7 | **D213** (new) — bracket rows read on sibling estimators | §2d; the fix is procedural and already executed this run | procedural |
| 8 | **D208** — two "OBV" vocabularies, sign-disagreeing | Cost the 08-07 run a false alarm, caught only by recomputation | **DEEP briefs** must name which module produced an OBV verdict |
| 9 | **D202** — a bracket's header still reads `ARMED` after the shared log scores it | Cost three of four handed rows on 08-07. **S62's header must be stamped `FIRED-B` at writeback this run** | writeback |
| 10 | **D9 · D10 · D11 · D15 · D17 · D18 · D19 (12th run) · D20 · D22 · D26 · D37 · D50 · D74 · D104 · D122 · D137 · D141 · D149 · D151 · D152 · D155 · D157 · D159 · D161 · D165 · D183 · D184–D192 · D203 · D204 · D206 · D209 · D210 · D211** | **carried forward, human-gated, NOT re-discovered** | — |

---

## 10. What this stage hands forward

1. ★★★ **`S62` FIRED-B at +13.252 on the settled 08-07 close, estimator verified to 0.002pp against
   yesterday's independent computation.** **It does NOT support "INDU OW− and UTIL UW are one bet"** —
   and **it is a degenerate settle**: branch A was **19.16pp** away. **D206 is confirmed on a settle
   rather than predicted.**
2. ★★★ **`S57` swung +3.90pp in one session and now sits 0.59pp below branch A**, which fires at **any**
   close through 08-12. **Materials UW− has exactly one live falsifier and it is nearly at its line.**
   ⇒ **ROTATION owns this; a MATR call made without it is a call made against a known live falsifier.**
3. ★★★ **`S61` sits 0.006pp from branch B — and yesterday's HANDOVER read that row on the wrong
   estimator** (RS20 in place of a 5-session excess), which inverted the reported sign on FRO.
   ⇒ **`D213`**, and every branch line in this file was re-read at source.
4. ★★ **The US `rs60` axis reached `t(NW) −2.77` at n=19 — 0.03 from Bonferroni, with sign agreement
   across all three horizons and a monotone rise in |t| through two n-jumps.** **Nothing is changed on
   it (P4)**, but if it clears, it challenges how ROTATION and BET read RS60 today.
   **`vol_surge` stays sign-opposite across the two markets; the gate change stays un-made (W1).**
5. ★★ **The CFTC COT stale streak is broken** — Friday's 15:30 ET release landed after the last run's
   stages. **SWEEP/MACRO must verify the file is not byte-identical to 07-31 before quoting a
   percentile.** Copper's 96th has been unquotable for six reads.
6. ⚠⚠ **`us_top300.csv` is 24 days stale and still lists a delisted security.** **SWEEP must read the
   sweep's stderr IN FULL** — reading only its tail is precisely how EA became 🟢가속 `new_green`.
7. ⚠ **`S66` is correctly un-scoreable (FRED stops 08-06)**, so **the run's most consequential branch —
   dovish relief vs credit fear — is still `unknown` (C3)**. The only 08-07 FRED observable is the 10y
   breakeven at **2.25 (−1bp)**, which cannot decompose nominal vs real and **is not used to call it.**
   ⇒ **`D212`.**
8. ✅ **Both ledgers `due` empty with zero legacy rows for a 12th run**, reported **with** the unit's own
   warning that a clean `due` is throughput, not quality.
9. **Exposure `방어` / target 55%, current % unknown (P5, no number substituted); n=4 decomposition
   −5.68pp = cash −2.03 + selection −3.65, indistinguishable from zero (C4). KR-only — NOT a US
   sizing input (W1).** `ARMED(TIMEFOLIO_EXECUTE=1)` set for a 6th run; **this run touches nothing
   executable.**
10. ✅ **Zero D74 contamination for the first time in four US runs.** **Both-direction sector changes
    are permitted this run** — the composition rule the last three runs needed does not apply.

**`EXPIRED` = 0 · silent skips = 0 · past-dated rows unscored = 0.**
**No position sizing and no buy/sell language appears anywhere in this carry (P4).**

---

## 11. ID counters reserved by this stage (D137 — checked at read time against all `handoff/*.md`)

```
scripts/handoff_id_audit.py  →  max M500 · max D211 · max S69 (US) / S56-KR (KR) · max R60
grep S70 / S71 / D212        →  0 hits in all nine handoff files
```

⇒ **this run takes `M501–` · `D212–` · `R61–` · `S70–`.**
**HANDOVER assigns `D212` and `D213`.** ⚠ **The shared-counter proposal for a human now stands for a
FIFTEENTH run**, and the **dig counter now carries the same collision the scenario counter had**
(`D202–D210` US vs `D202-KR–D214-KR` KR, distinguished only by suffix — registered as **D211** by the
08-08 KR run).

---

## ✅ EXIT CHECK

- [x] Both shared spines read in full · `STANDING_VIEW_US.md` + `SCENARIOS_US.md` read · **`SCENARIOS_KR.md` opened** and confirmed to hold no past-dated row for this desk · `RESEARCH.md` read · **`module_report_tags show` cross-queried (exit 0)**
- [x] **Retracted ledger read BEFORE today's view formed** (§1b) — six entries named with the stage each binds
- [x] **Every past-dated scenario scored** — **S62 FIRED-B**. `EXPIRED` = 0, silent skips = 0
- [x] **`reject_ledger.py due` run** — 0 due, **legacy 0**, count reported (127 rows / 44 resolved)
- [x] **`missed_ledger.py due` run** — 0 due, **legacy 0** (81 / 34); **signs never summed**; the outcome-selected stratum warning carried
- [x] **Exposure state read and carried** — `방어` / 55% / current % **unknown, no number substituted (P5)**; **not** a cold start (31 ledger rows); n=4 decomposition carried with its C4 caveat
- [x] Stale rows flagged with their `asof`; **the cleared COT suspension converted into a dig instruction**
- [x] `[measured]` / `[inferred]` tags preserved; **no `[inferred]` claim passed downstream as evidence**
- [x] **RESEARCH triggers loaded as binding constraints, grouped C/S/D/W + L**, with the stage each binds
- [x] `HANDOVER.md` written; `handoff/*.md` writeback owned by run end, **append-only** (D165)
- [x] **No position sizing, no buy/sell language (P4)**
