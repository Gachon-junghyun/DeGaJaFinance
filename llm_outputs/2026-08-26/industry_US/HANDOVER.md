# HANDOVER — industry_US · 2026-08-26 (Stage 0)

> Inheritance step. Reads `handoff/` (the analytical carry) + the mechanical tag ledger, scores every
> matured scenario, audits **both** ledgers, and loads the RESEARCH rules as binding constraints.
> **No sizing, no buy/sell language anywhere in this file (P4).**
> Run clock: **2026-08-26 22:1x KST = 09:1x ET, Wednesday US PRE-MARKET.**
> **Terminal settled US bar = 2026-08-25 (Tuesday).** `n_new_sessions_since_prior_run = 1`.

---

## 0. Instrument health inherited — read BEFORE any number is trusted

`llm_outputs/2026-08-26/industry_US/preflight/PREFLIGHT.md` **was run** (Phase −1, before this stage).
**3 PASS / 4 FAIL / 0 UNKNOWN.**

**What this run may NOT claim (carried verbatim into every downstream stage):**

| # | Removed right | Gate |
|---|---|---|
| 1 | **No news-velocity or theme-freshness citation anywhere**, and **no "quiet"/"no news" verdict** on any name or sector. `BET_SHEET §B` freshness tags must read `UNMEASURED (G1 FAIL)` | G1 (`vel_coverage` 17.06% vs 80% bar) |
| 2 | **No bare concentration number** — every unit count carries its `--days` on the same line | G4 (250d→11 · 500d→10 · 750d→10, groupings differ) |
| 3 | **`wflow` is not a current weighting** (42-day-old caps). On `wflow`/`eqflow` disagreement, **`eqflow` is the citable one**; `wflow` only with the 42-day tag | G5 |
| 4 | **Health Care may not be promoted/demoted on the weighted-flow bucket** — substitute `eqflow`/`breadth`, say so inline | G3 (flipper = HLTH/`LLY`) |
| 5 | **No IC-backed sizing language** — any fraction is "mechanical 1/4, IC not yet estimable" | G6 (0.50/day = 2.0× slow) |
| 6 | **SWEEP must re-read `§scoring.n_axes` before any Δflow subtraction** | G2, conditional and now live |

★ **PREFLIGHT executed `D358-KR` the same morning it was registered** — it now carries a
`vs-yesterday` DIFF column. Two sentences that were true on 08-25 and are **false today** were
available to be copied forward and were caught by the column:
- *"the news axis has been fully dead for four runs"* → `vel_coverage` **0.0% → 17.06%**;
- *"Consumer Staples' sign belongs to `WMT`"* → **STPL is no longer the flipper; Health Care is.**
⇒ **The STPL restriction is LIFTED this run and an equivalent HLTH restriction is ATTACHED.**
This is the **second consecutive run** in which the flipper changed identity. It is a per-run
measurement and must never be carried from memory.

---

## 1. Inherited standing view

### 1a · Regime call (§1) — **CARRIED UNCHANGED, tag preserved**
> **"Memory is a price-cycle industry in rate-of-change deceleration while its level stays tight."**
> `[inferred]` — built on the measured chain `M1`–`M6`/`M18`.

**Carried, not re-derived, and not upgraded.** One new settled session is `n=1` (`S5`) and does not
test a regime call. The memory complex's own next print is **`MU` 2026-09-24**. ⚠ The tag stays
`[inferred]` — it may be carried but **may not be cited as evidence** for a new proposition.

### 1b · What the last two runs established that governs today
| Source | Carried fact | Tag |
|---|---|---|
| 08-25 US | The 08-24 session produced `EW{Staples+HealthCare} − EW{IT}` 5-session = **+9.336 = 97.6th percentile of two years** vs a two-year mean −1.064 (`M914`) | `[measured]` |
| 08-25 US · DEEP | That IT move is a **HARDWARE de-rate, not "one trade"**: software `exc5 +3.32`/`exc20 +7.98` at 57.9% participation vs semis −7.06 / semicap −9.90 / hardware −10.89 (**14.21pp gap**); epicenter is analog/embedded/auto (`ON −40.8`, `QCOM −37.1`, `NXPI −31.5`), **`NVDA` FLAT at `rs60 −0.8`** | `[measured]` |
| 08-25 US · DRIFT | 🚨 **The `IT UW` is a CONSENSUS position as of 08-24/25** — five outlets published the same rotation headline the same day, one naming `IT`+`INDU` together. Recorded on the **against-us** side | `[measured]` |
| 08-25 US | `M879` replicated a **4th** time: ENRG refining `exc20 +12.48` at 100% participation vs E&P `exc5 +3.23` (+6.69 on twenty), midstream 0.0% | `[measured]` |
| 08-25 US | The refiner kill is one settled session from firing **and the kill is WEAK** — two consecutive negative 5-session crack rates occur on **35.5% of the trailing 252 days** (`D352`/`M916`) | `[measured]` |
| 08-26 KR (this morning) | `C17` opened: **a single value chain is split across 3+ sector labels**, so sector-level instruments structurally cannot see it (`D361-KR`). Measured twice independently in KR | `[measured]` |
| 08-26 KR | `M921`: the BOK-hold consensus went **11:10 → ~80% hold in one session**. ⇒ information asymmetry inverted — *a hold teaches almost nothing* | `[measured]` |

### 1c · Retracted ledger (§5) — **READ BEFORE forming today's view**
Highest allocated at read time: **`R102`** (2026-08-26 `industry_kr`), **`D361-KR`**, **`M926`**,
**`C17`**. Two retractions bind this run directly:

- **`R101` (08-25 US)** — *"`server prices` reads 🟡ACCELERATING 6.79×"* withdrawn as **UNREADABLE**,
  because `D340`'s own measured band (~60–2,000 articles) makes a base of 34–38 a count, not a ratio.
  🚫 **No theme-age ratio may be quoted this run on a base below ~60**, and with G1 FAILED no
  theme-freshness citation is admissible at all — the two constraints stack.
- **`R102` (08-26 KR)** — *"IRS short-end strength = the hike is pre-priced"* died because **the same
  outlet read the same move the opposite way one day later**. 🚫 **A single-outlet directional label
  on a rates move is not evidence.** The *fact* of a move survives; the *direction attached to it*
  does not. This binds MACRO today: any front-end reading must carry ≥2 independent outlets or be
  written as an unlabelled move.

⚠ **ID allocation for this run must 3-grep at WRITE time** across `handoff/*.md` · `llm_outputs/**` ·
`REPORT/**` before taking any new `R`/`D`/`M`/`S`/`P`/`C` id. `D76`'s collision class has now fired
and been **prevented** twice in two days (`R99`/`R100` on 08-25; `C16`→`C17` on 08-26).

### 1d · Open contradictions (§6) — carried, NOT resolved
- **`C15` · the `vol_surge` gate** — **carried, human-gated, and the split is now sharper than ever.**
  Today's ledgers, both re-run: **KR `vol_surge` h=1 `t(NW) −3.64`, n_eff 37.0 — Bonferroni-passing
  NEGATIVE**; **US `vol_surge` h=1 `t(NW) +3.40`, n_eff 33.0 — Bonferroni-passing POSITIVE.**
  ⇒ **Two markets, same axis, opposite signs, both clearing the multiple-comparison bar.** This is
  precisely the `W1` cross-market-transfer prohibition made visible: **neither result may be imported
  into the other market's desk.** The US desk keeps the positive sign; the KR desk keeps the negative.
  ⚠ KR's h=5 leg **lost** its Bonferroni clearance today (−3.35 → −2.33) — the 08-25 sentence *"both
  horizons pass"* is **not true** and is not inherited.
  🚨 **`S101` settles this question from the US side at tonight's close** (see §2b).
- **`C16` (08-25 US)** — the two admissible instrument families disagree about who is winning and
  neither is graded high enough to overrule the other (`eqflow` ranking vs 5-session price excess
  agree only at the bottom and invert at the top). **Carried unchanged.**
- **`C17` (08-26 KR, NEW)** — value chains split across ≥3 sector labels; sector instruments cannot
  see the chain. ⚠ **Explicitly NOT the flipper problem.** **US-side relevance is untested** and is
  filed as this run's dig 1 (§6).
- **`C14` · `C10` · `C1` · `C2`-successor** — carried unchanged.
- **`D293-KR`** — 13th reproduction (KR-owned instrument defect; noted, not this desk's).

---

## 2. Scenarios — settlement

### 2a · Scored this run by this desk: **0.** And the exhaustive settle table is the evidence the question was asked.

**The two rows dated 08-25 were already scored this morning by the sibling `industry_kr` desk**,
which the 08-25 US run had explicitly handed them to:

| ID | Settle | Verdict (KR desk, 08-26) | Observed | Threshold |
|---|---|---|---|---|
| **`P79`** | 08-25 close | **`FIRED-C`** | `EW{COHR,LITE,HPE,AVGO,ANET}` trailing-5 excess vs `SPY` **−2.977pp** | A ≥ +8.02 · B ≤ −7.72 |
| **`S108`** | 08-25 close | **`FIRED-C` by the letter**, VOID question **handed to this desk** | `EW{XLU,XLRE,XLP}` 3-session excess vs `SPY` **−0.108pp** (`XLP` +0.972 · `XLRE` +0.187 · `XLU` −1.485) | A ≥ +1.68 · B ≤ −1.76 |

★ **`P79`'s trajectory is the information, not its branch**: −12.425 (registration 08-20) → −7.178 →
−5.609 → **−10.852 (08-24)** → **−2.977 (08-25)**, i.e. **+7.9pp in one roll**, because the trailing
window dropped 08-17 and took on 08-25. ⇒ **the "second consecutive sub-p05 week" state the 08-25 desk
recorded was erased by a single session.** 🚫 Not readable as *"the rebound came"* — roll-off and new
session are mixed and the decomposition was declared out of scope by the scoring desk.

### 2b · 🚨 OWNER RULING — `S108` VOID question (this desk owns the row; the ruling was deferred to it)

**The question**, as the KR desk framed it: `S108` froze its window around *"Warsh's Jackson Hole
**D-0, 2026-08-21**"*, and **`R93` (08-22 US) established the speech is 2026-08-27~29.**
⇒ **the event the bracket was built to measure never occurred inside the bracket's window.**

**RULING: NO VOID. `S108` STANDS as `FIRED-C`. It is simultaneously re-labelled
`LOW-INFORMATION-BY-CONSTRUCTION` and may not be cited as evidence about the Jackson Hole equity
reaction.** Four grounds, in order of weight:

1. **The letter of the anti-signal clause.** `S108`'s VOID list is exhaustive and specific: *a
   CPI/PPI/PCE print · an intermeeting FOMC action · a Treasury refunding/buyback-schedule change*
   inside 08-20→08-25. **None fired.** A premise failure is **not** an item on that list.
2. **The rule against widening a frozen clause after the fact** — the identical ground on which this
   desk ruled `S102` `FIRED-C`/no-void on 08-25. Ruling the other way here would make the two rulings
   inconsistent within 24 hours on the same principle.
3. **`D242`**: a row is not re-banded, re-dated or re-scoped after registration; it settles as
   registered.
4. ⚠ **But the honest consequence must be written down, not buried in the verdict word.** With no
   event inside the window, `S108` measured **three sessions of noise**, and `C` was already its
   disclosed ~70% favourite. **A `C` on a null window confirms nothing.** The row's *surviving*
   contribution is the dispersion observation, which does survive: **the three legs span 2.46pp and
   one is negative**, so the row's own premise — *"the three underweights rip together"* — **was not
   observed even in the branch that fired.** That much is a real measurement on a real window.

**No successor row is needed** — Jackson Hole is already double-bracketed with the corrected dates:
**`S120`** (Warsh's first speech as Chair, settle **08-28**) and **`S112`** (the mandatory Jackson Hole
bracket, settle **08-31**). Registering a third would be `D343`'s date-stacking error.
⇒ **New dig registered: see §6 dig 2 (`D362` candidate).**

### 2c · Not yet arrived — named so they cannot be skipped silently
🚨 **This run executes at 09:1x ET, PRE-MARKET.** Every row below settles at **tonight's
2026-08-26 close** and is therefore **unscoreable now, not skipped.** **The 2026-08-27 run must take
all of them.**

| ID | Settles | Pre-settle reading available to this run (08-25 close, ONE SESSION EARLY — **not a score**) |
|---|---|---|
| **`S101`** | 08-26 close | **spread = +1.616pp** · A ≥ +4.45 · B ≤ −3.88 ⇒ **inside C, leaning A.** Excluded basket EW `+0.440` (`DASH +8.13` · `TMO +6.84` · `SHOP +5.18` · `ABNB +4.16` vs `CRWD −12.73` · `PANW −8.95`); admitted basket EW **−1.176** (`MA +4.56` vs `WMT −8.32` · `RTX −6.54`). ⚠ Both baskets are ±13pp-wide internally — the EW spread hides that |
| **`S103`** | window 08-25→08-29 (`NVDA` print inside) | ⚠ **LOW-RESOLUTION by its own registration** (hand-set ±5.0pp bands; `D295`'s re-derivation obligation was met on 08-25 with the ±6.1% straddle, which brackets the ±5.0 bands ⇒ **`S103` is inside the implied move and is pre-declared low-information**, per `D242` it is NOT re-banded) |
| **`P77` `P78` `P80` `P90`** | 08-26 close | Not computed here — these are MACRO-stage pre-commitments and the MACRO stage re-reads them from the run dir, not from this file |
| **`S79`** | 08-27 | The `NVDA` binary itself |
| **`S115` `S117` `S119`** | 08-27 | `NVDA` print · memory-IV-vs-`NVDA`-beta · Bessent sanctions presser |
| **`S116` `S118` `S120` `S111`** | 08-28 | `MRVL` print · printer-vs-memory · Warsh speech · `P67`'s credit observable |
| **`S104` `S112` `S124`** | 08-31 | July PCE · Jackson Hole · IT breadth repair |

⚠ **`S101`'s pre-settle reading is disclosed now rather than discovered at scoring** — the same
practice that caught the 08-25 desk's `P79` window error. It is **explicitly not a verdict**: the
window is 4 of 5 sessions and `P79` has just demonstrated that one session can move a trailing-5
spread by 7.9pp.

### 2d · 🚨 `S8` — undated and unscoreable for the **27th** consecutive run
Unchanged and unfixable by this desk: **a human must `VOID` it or re-register it with a date (P5).**
Its cost stays on the record — `S74`, the row written *because* `S8` was unscoreable, settled
`FIRED-C` on 08-24 and retired, while `S8` still holds the same object with no date.

**Run totals: 0 SCORED by this desk · 1 OWNER RULING issued (`S108`, no-void) · 0 `EXPIRED` ·
0 silent skips · 1 unscoreable-by-construction (`S8`, 27th run).**

---

## 3. Both ledgers audited — and the clean result was verified independently, not taken on trust

The L2 warns explicitly: *"do not treat a clean `due` run as proof the ledger is healthy."*
So both tools were run **and** their claims were re-derived from the raw `jsonl` by hand.

| Ledger | Tool output | Independent re-derivation | Agree? |
|---|---|---|---|
| **Rejections** | 238 total · 140 resolved · **0 due** · **0 legacy needing audit** | 238 rows; **117** with `recheck_date ≤ 2026-08-26`, of which **0 unresolved**; **24** rows carry neither `revives_if` nor `recheck_date`, of which **0 unresolved** | ✅ **yes** — the "legacy 0" means *0 legacy rows still needing audit*, out of a historical legacy stock of **24**, all of which have been resolved |
| **Misses** | 241 total · 136 resolved · **0 due** · **0 legacy** | 241 rows; **136** with `recheck_date ≤ today`, of which **0 unresolved**; **0** rows lacking both `enters_if` and `recheck_date` | ✅ **yes** |

⇒ **Legacy-needing-audit = 0 for a 15th consecutive run.** That, not the empty `due` list, is the
evidence the practice took hold. **The legacy *stock* is 24 on the rejection side and 0 on the miss
side** — stated because a shrinking-to-zero count is the only real evidence, and this one is now flat
at zero by resolution rather than by absence.

⚠ **Sign discipline (`carryover §3c`)**: the two ledgers' `excess` columns have **inverted signs** and
are **not summed** anywhere in this run.

### 3a · Class scores — accumulation, not edge (P4 · C4)
- **Rejections**, n=126 scored, mean excess **+2.3pp** · 손해 40 / 이득 27 / **노이즈 59 (47%)**.
  By type: narrative **+4.1pp** (n=16) · measured **+2.3pp** (n=103) · structural **−2.0pp** (n=7).
- **Misses**, n=125 scored, mean **+0.6pp** · 놓쳐손해 29 / 안사서이득 36 / **노이즈 60 (48%)**.
  🚨 **Read the strata, never the pooled mean**: `outcome_selected` n=6 **+14.2pp** (harvested from
  names that had already risen — structurally positive, **unusable for estimation**);
  **`prospective` n=95 `−0.7pp`, the ONLY unbiased stratum**; `random` n=24 +2.1pp.
  ⇒ **The desk's own unbiased selection record is indistinguishable from zero.** Carried as context.
- ⚠ **~47–48% of both ledgers is noise by the tools' own classification.** No class mean is quoted
  downstream as an edge.

---

## 4. Exposure state — inherited as size context, not as a gate

```
exposure_rule state : 정상 (규칙상태, 직전 정상) · bench 069500.KS 107,710 (+0.857%)
                      target 95%  ·  current % ─  ·  gap ─
                      🚨 투자비중미상 — the account query failed; `state` could not read NAV
exposure_rule show  : 41 rows, last = 2026-08-26 (live bar) · 투자 85.5% · 밴드이탈 −9.5pp
cumulative (n=14)   : 총초과 −12.63pp = 현금기여 −6.08pp + 선택기여 −6.56pp
```

- **Band gap −9.5pp** (target 95% vs accrued 85.5%) — the **narrowest of the last eight rows**
  (−39.4 → −27.1 → −14.0 → −13.9 → −9.9 → −9.7 → −9.7 → **−9.5**).
- ⚠ **The 85.5% is STATED from the accrued ledger row, not substituted for a live account read.**
  `state` returned `투자비중미상`; per the L2's rule that is reported as 🚨 and **no number is
  invented** (P5). The ledger row is a different object (it is what was accrued at 09:10/15:00 by the
  timefolio tasks) and is labelled as such.
- ⚠ **`n=14` is not a sign.** The −12.63pp decomposition splits almost evenly between cash weight
  (−6.08) and selection (−6.56); with n=14 neither half is distinguishable from zero (`C4`).
- ⚠ Every row carries **`⚠미정착봉(장중·KIS실시간)`** — the accrual is taken on unsettled intraday
  bars. This is the same class of defect as `D355` on the sweep side.
- 🚫 **This desk logs nothing** — `log` is owned by the 09:10/15:00 timefolio tasks (`carryover §3d`).

---

## 5. Signal scoreboard (`ic_ledger --market us`) — 405 rows / 33 run-dates / 15 tests

**Quotable cells only (`n_eff ≥ 4`), Bonferroni threshold `|t| > 2.8` for 15 simultaneous tests:**

| Axis | h | n | `n_eff` | mean IC | `t(NW)` | positive | verdict |
|---|---|---|---|---|---|---|---|
| **`rs60`** | **5** | 27 | **5.4** | **−0.1310** | **−5.46** | **7%** | ★ **significant, clears Bonferroni — NEGATIVE** |
| **`vol_surge`** | **1** | 33 | **33.0** | **+0.0398** | **+3.40** | 67% | ★ **significant, clears Bonferroni — POSITIVE** |
| `rs60` | 1 | 33 | 33.0 | −0.0635 | −2.77 | 21% | significant on its own bar only |
| `obv_norm` `flow_score` `rs20` (h=1, h=5) | | | 5.4–33.0 | −0.02 to −0.05 | −1.6 to −0.9 | | **indistinguishable** |

★★ **The load-bearing new reading: `rs60` at h=5 is the strongest cell on the US board and its sign is
NEGATIVE — ranking the universe by 60-day relative strength has been *inversely* predictive of the
next five sessions across 27 run-dates, positive in only 7% of them.** ⇒ **A momentum-following
selection rule is measured, on this desk's own ledger, to have had the wrong sign over this window.**
⚠ **`S6`/regime label required**: the ledger window covers a tape in which the market's biggest
winners have been sold (the 08-24 rotation is inside it). **A reversal IC measured in a
reversal regime does not generalize** — this is carried as a live constraint on ROTATION/BET, not as
a proven law.

⚠ **Six cells are unquotable at `n_eff < 4`** (all h=10, plus `rs60` h=10 at `n_eff 2.1`), including
the largest raw |t| in the table. They are excluded, not reported.
⚠ **`vol_surge` h=5 is `+0.44` — indistinguishable.** So the US positive sign lives at **h=1 only**;
the two-horizon agreement `D105` asks for is **absent** on the very axis `C15` is stuck on.
🚫 **`kelly_size --ic` is not an evidence-backed size this run** (G6 FAIL) — any fraction downstream
is labelled **"mechanical 1/4 — IC not yet estimable"**.

---

## 6. Stale-check + dig list ranked for today

### 6a · Stale flags
| Object | `asof` | Age | Flag |
|---|---|---|---|
| **`STANDING_VIEW §3a` per-name US registry** | **2026-07-25** | **32 days** | 🚨 **The narrative registry has not been touched in a month**, and ~12 of its inline recheck dates have passed (`TRV` 08-06 · `JPM` 08-08 · HLTH block 08-06 · tankers 08-06 · `PYPL` 08-06 · `VRT` 08-12 · `SLB` 08-21 · `AMAT/LRCX/KLAC` crossings 08-20 · `VTR` 07-30 · `HUM` 07-31 · `MRK` 08-04 · exchanges node 08-07). ⚠ **Verified before asserting**: the *recheck function* has since migrated to the mechanical ledgers, which are clean (§3) and do carry `PYPL`/`SLB`/`VRT`/`CRWD`/`GS`/`DLR`/`UPS`. ⇒ **This is a DOCUMENTATION gap, not an unexamined-name gap** — but the registry is the object HANDOVER is supposed to inherit, and it is a month stale |
| **`module_report_tags` ledger index** | **2026-07-21T18:58** | **36 days** | 🚨 252 reports / 350 names / 15 sectors indexed, newest entry `2026-07-21`. **Five weeks of `industry_US` and `industry_kr` output are absent from the mechanical coverage ledger.** ⇒ the "belief vs coverage" reconciliation this stage is supposed to perform **cannot be performed against current data**. Refreshed at run end (§8) |
| **`data/us_universe/us_top300.csv`** | 2026-07-15 | 42 days | G5 FAIL; weights and membership both stale |
| **`000660` flow read** | suspended | — | Suspension is **an observable (`S17`), not a date** (`R13`). Nothing cleared; carried. KR-owned |
| **`estimates` accrual** | 2026-08-26 | current | G6 FAIL on *rate*, but the last **8** accruals are daily. The deficit is July/early-August holes, permanently unrecoverable |

**No suspension cleared this run**, so no suspension converts into a dig.

### 6b · Dig list ranked for today (candidate DEEP/PREMORTEM assignments)

1. 🆕 **Is `C17` a US problem too?** The KR desk measured, twice independently, that a value chain
   splits across ≥3 sector labels so that no sector aggregate can see it. **The US desk has never
   tested this**, and it has an obvious US candidate on file: `D250`/`M731`, **11 runs old** —
   *no optical/interconnect row exists in `cycle_registry.json`* while `COHR` and `LITE` were the
   board's worst 5-session names and the largest contributors to `P79`. **Optical/interconnect is
   exactly a chain that is not a bucket.** ⇒ **Highest-value dig this run.**
2. 🆕 **`D362` candidate — a bracket anchored on an event date must verify that date from a primary
   source at registration.** `S108` is the **second** row in four days to be litigated at settle over
   what its clause meant (`S102` was the first, and produced `D356`). `S108`'s defect is different and
   worse: not an ambiguous clause but **a window that did not contain its event**, discovered by a
   *later* run (`R93`). **Positive-form remedy: PREMORTEM prints the event date and the source it was
   taken from beside every frozen window, and the `D93` baseline table gains an `event_in_window`
   boolean.** Cost ≈ one line per registration.
3. **`D355` — the sweep will run on an unsettled pre-market bar again today**, and it depresses
   `vol_surge`, **the only US axis with a Bonferroni-passing positive sign** (§5). Measured 08-25:
   `vol_surge` median 0.820 → 0.670 (−18.3%), `≥1.2` count 22 → 12 (−45%). ⇒ **SWEEP must re-measure
   the pre-market volume fraction today and state it**, and must not read a `vol_surge` drop as
   information.
4. **`D352` — print the unconditional base rate beside the refiner kill.** The registered kill
   (two consecutive negative 5-session crack rates) fires on **35.5%** of days unconditionally. It is
   one settled session from firing. **MACRO must carry the 35.5% on the same line as the kill.**
5. **`D294` — 7th reproduction**: `action_bracket.py` names a binary and then reports there are none.
   `ACTION_TICKETS.md` will be hand-built for a **4th** run. **Analytical-only mandate: dry-run share
   counts are deliberately omitted.**
6. **`D341`** — `OKLO` `AA` `X` `WY` `LYB` `DOW` `FRO` `SMCI` `NRG` sit outside `us_top300`;
   **`S109` remains armed on `FRO`, a name this desk cannot flow-tag at all.** Carried.
7. **`D343` — 08-28 now carries nine rows** and 08-27 carries six. Any registration this run must
   name its non-redundancy and should avoid both dates.
8. **`D339`/`D340`/`D345`/`D346`/`D297`/`D327`/`D329`** — carried, counts to be incremented at their
   own stages, no new numbers here.

---

## 7. RESEARCH triggers loaded as BINDING constraints (not summarized) — and which stage each binds

> `handoff/RESEARCH.md` is the single source. Loaded as constraints, per the stage's own warning that
> three of one session's six reversals broke rules that already existed in prose nobody carried.

| Group | Fires when | IDs | **Binds, this run** |
|---|---|---|---|
| **C** | you cite a number | `C1` baseline · `C2` both halves · `C3` unknown column · `C4` "indistinguishable" · `C5` arbitrary choice | **MACRO + every stage.** ★ `C1` is live: the 08-25 desk mis-read `P79`'s own window and caught itself — **re-measure every inherited number including baselines.** `C4` binds §3a (n=14 exposure, n=126/125 ledgers, prospective stratum −0.7pp) and §5 (six unquotable cells). `C5` binds G4's threshold (0.65 sits on a slope, not a plateau) |
| **S** | you make a statistical claim | `S1` date-fold · `S2` diagnose the null · `S3` power first · `S4` in-sample≠done · `S5` short samples · `S6` future labels | **Any stage citing a test.** ★ `S5` binds the regime call (1 new session ≠ a regime test) and `risk_units` (249-day window flagged by the tool itself). `S6` binds §5 — **the `rs60` reversal IC must carry its regime label** |
| **D** | you read data | `D1` second venue · `D2` proxy sign · `D3` signed vs unsigned · `D4` regime contamination · **`D6` signal grade (OBV is C-grade)** · `D5` cross-provider | **SWEEP · ALPHA · L2 indicators.** ★ `D6` is load-bearing today: **with G1 dead, the surviving sweep axes are OBV (C-grade) + `rs20`/`rs60`** — that is `C16`'s whole substance. `D4` binds §5's regime caveat |
| **W** | you write a conclusion | `W1` cross-market transfer · `W2` inherited lead/lag · `W3` real≠profitable · `W4` name the customers · `W5` sub-sector dispersion · `W6` reader's-market spine | **DEEP · BET · ROTATION.** ★★ **`W1` is the single most binding rule this run** — `C15` now shows the *same axis with opposite Bonferroni-passing signs in the two markets*. Nothing measured in KR this morning transfers. ★ `W5` binds every sector verdict: the 08-25 DEEP already proved IT's headline was a **hardware** de-rate, not a sector one |
| **L** | lenses, not triggers | `L1` second derivative · `L2` peak-margin trap · `L3` branch information content | **DEEP · PREMORTEM.** `L1` underwrites the regime call itself; `L2` is the `MPC` instance the 08-25 run flagged; `L3` gates every new bracket |

**Standing method pre-commitments carried into this run:**
- **`D165`** — handoff writeback is **append-only**; nothing above a new block is read into memory and rewritten.
- **`D357`** — the 2026-08-05 truncation mechanism is **still live** and the protection is accidental.
  ⇒ **This run stages all writeback text in the scratchpad first and appends with `>>`, never `'w'`.**
- **`D93`** — every registered threshold carries a baseline computed **before** freezing.
- **`B4`** — a bracket declares at registration which branch is low-information.
- **`D76`** — 3-grep every new ID at **write** time, not draft time.

---

## 8. What this run asserted and then refuted (§4c · `D48`) — written down, not edited away

Two so far, both in this stage:

1. 🚨 **This stage drafted the §6a stale-flag as *"~12 dated rechecks in `§3a` have passed unexamined."*
   The next command refuted the strong half.** Reading `out/reject_ledger.jsonl` and
   `out/missed_ledger.jsonl` directly showed `PYPL` `SLB` `VRT` `CRWD` `GS` `DLR` `UPS` `MA` `NEM`
   `CVX` `FCX` `GEV` all carry live ledger rows with forward recheck dates. **The correct sentence is
   "a documentation gap, not an unexamined-name gap."** The draft is left in place above with the
   correction appended, per `D48`.
2. ⚠ **This stage drafted the rejection ledger's legacy count as `0` from the tool's own line.**
   The independent re-derivation found **24 legacy rows exist**; the tool's `0` means *0 legacy rows
   still needing audit*. Both numbers are now stated (§3). **The tool was right; the draft sentence
   was imprecise in a way that would have read as "there are no legacy rows".**

⚠ **Zero self-refutations would itself have been worth a line** — it usually means the controls were
not adversarial. Two is a low but non-zero count for a stage this mechanical.

---

## 9. Carry emitted for downstream stages

- **Regime call**: carried unchanged, `[inferred]`, not citable as evidence.
- **Citation rights**: the six-row table in §0 governs every subsequent stage.
- **`W1` is the run's hardest constraint** — nothing from this morning's KR run transfers.
- **`eqflow` is the citable weighting** wherever it disagrees with `wflow` (G5).
- **Health Care is rank-restricted** to `eqflow`/`breadth` (G3); **Consumer Staples is NOT** (lifted).
- **Size context**: exposure `정상`, target 95% vs accrued 85.5%, gap **−9.5pp**; cumulative n=14
  −12.63pp = cash −6.08 + selection −6.56; **account read FAILED, number stated not substituted.**
- **Concentration**: **10 units @750d · 10 units @500d · 11 units @250d** — never as one number (G4).
- **Sizing language**: "mechanical 1/4 — IC not yet estimable (G6 FAIL)".
- **Tonight's settles** (§2c) are handed forward to the 2026-08-27 run **by name**, with `S101`'s
  pre-settle reading disclosed at **+1.616pp**.
- Handoff writeback (`handoff/*.md`) + the tag-ledger refresh happen at **run end**, per protocol.

## ✅ EXIT CHECK
- [x] Shared spines read (`STANDING_VIEW.md` §1–§6 + the 08-25 US and 08-26 KR appends;
      `SCENARIOS.md` master scoring log + master index) **and** this desk's halves
      (`STANDING_VIEW_US.md` §3a, `SCENARIOS_US.md` full ARMED roster) **and** `RESEARCH.md`
      (Parts A/B rule groups + Part C, latest appends `D352`–`D361-KR`).
      ⚠ **The other market's file was opened** — `SCENARIOS.md`'s 08-26 KR scoring block holds the two
      past-dated rows this run had to account for, and one of them (`S108`) is US-owned.
- [x] Mechanical ledger cross-queried (`module_report_tags show`) — **and found 36 days stale**, which
      is reported as a finding rather than used as if current.
- [x] Retracted ledger read **before** forming today's view; `R101` and `R102` bind stated constraints.
- [x] **Every past-dated scenario accounted for.** 0 scored by this desk (both were scored this morning
      by the sibling desk); **1 OWNER RULING issued on `S108`**; **0 `EXPIRED`; 0 silent skips**;
      `S8` unscoreable for a 27th run and named.
- [x] `reject_ledger.py due` run — 0 due, 0 legacy needing audit (of a legacy stock of 24, all resolved);
      **independently re-derived from the raw jsonl rather than trusted.**
- [x] `missed_ledger.py due` run — 0 due, 0 legacy; independently re-derived. **Signs not summed.**
- [x] Exposure state read and carried, with the 🚨 `투자비중미상` failure stated and **no number substituted**.
- [x] Instrument health inherited from `PREFLIGHT.md`; every FAIL converted into a removed citation right.
- [x] Two self-refutations written down, not edited away (§8).
- [x] Stale rows flagged with their `asof`; no suspension cleared this run.
- [x] `[measured]`/`[inferred]` tags preserved; the `[inferred]` regime call is explicitly barred from
      being used as evidence.
- [x] RESEARCH triggers loaded as binding constraints, grouped C/S/D/W/L, with the stage each binds.
- [x] **No position sizing, no buy/sell language anywhere in this file (P4).**

---
> Next: `python pipeline/run_protocol.py industry_us --next` → **MACRO**.
