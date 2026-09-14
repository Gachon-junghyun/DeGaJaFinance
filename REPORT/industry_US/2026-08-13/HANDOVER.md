# HANDOVER — industry_US · 2026-08-13 (Thu KST) · Stage 2/11 (L1·HANDOVER)

> Zero buy/sell language anywhere in this file (P4). This stage transports analysis, never a recommendation.

## 0. Run clock — and the one fact that reorders this whole run

**2026-08-13 22:10–23:00 KST = 2026-08-13 09:10–10:00 ET, Thursday.**

🚨🚨 **THE ≤48h BINARY DID NOT ARRIVE — IT ALREADY PRINTED, 40 MINUTES BEFORE THIS STAGE OPENED.**
**July PPI released 2026-08-13 08:30 ET.** `catalyst_calendar --days 14` lists it as **D-0 · binary
· [bls✓]**. Every prior run in this sequence met its binary *ahead* of the print and had to bracket
it; **this run meets its binary already settled in the data but NOT yet settled in the tape** — the
cash session opens at 09:30 ET, twenty minutes after this stage's clock.

⇒ **Three consequences, stated here so no downstream stage has to rediscover them:**
1. **PREMORTEM's mandatory both-sides bracket is NOT about PPI's content** — that is known. It is
   about **tonight's 08-13 session**, which is where six registered rows settle.
2. **`S71` — the CPI→PPI divergence bracket — is live and un-scoreable at this clock**, because its
   observable is `XLU` 1-session excess **on 08-13** minus the same on 08-12. Its *macro premise* is
   now readable and it is **not the clean case the row was written for** (§2c).
3. **Every "settle 2026-08-13" row (S63 · S64 · S67 · S68 · S69 · S71) settles TONIGHT, after this
   run ends.** They are named, not dropped, and **the next `industry_US` run inherits six settlements
   at once** — the largest scheduled batch on this board.

**Last settled US equity bar = 2026-08-12 (Wednesday).** ✅ **`D74` contamination = 0**, verified by
construction: the sweep's own price frame ends **2026-08-12** with a median last-bar volume of
**0.740×** the prior-20d average (a full session, not a stub), and `SPY` carries the same terminal
bar (PREFLIGHT G0 **PASS**).

**Second binary in the window**: **NVDA earnings 2026-08-26, D-13**, already inside `CATALYST_WATCH`
and already bracketed by **`S79`** (registered by 08-12 RUN-2, two independent legs). No action owed
this run beyond carrying it.

---

## 1. Inheritance read — what was opened, in full

| File | Read | Note |
|---|---|---|
| `handoff/STANDING_VIEW.md` (shared spine) | ✅ | §1 regime · §2 seed chain · §3a/§3b registry · §4 asymmetry · **§5 retracted ledger R1–R63 including every per-run append through the 08-13 KR block** · §6 open contradictions (C1 · C2 · C9 · C10) · asof chain |
| `handoff/STANDING_VIEW_US.md` | ✅ | §2 US fact rows · §3a per-name rows. mtime **2026-08-12 23:00** — the 08-12 RUN-2 writeback landed |
| `handoff/SCENARIOS.md` (shared spine) | ✅ | MASTER scoring log **and** MASTER INDEX through the 08-13 KR append — **93 brackets registered (67 US · 26 KR)** |
| `handoff/SCENARIOS_US.md` | ✅ | **every row due or near-due re-read at source (D213)** — S59 (:1731) · S61 (:1784) · S63 (:1868) · S64 (:1915) · S67 (:2054) · S68 (:2099) · S69 (:2143) · S71 (:2291) · S72 (:2332) · S73 (:2432) · S74 (:2482) · S75–S78 · S79 (:2677) |
| `handoff/SCENARIOS_KR.md` | ✅ **opened, as the spine rule requires** | Checked for a past-dated row this desk must score. **`S38` and `S48-KR` are `PENDING-DATA` on KRX short-balance T+2 and are KRX-observable ⇒ they belong to `industry_kr` (P5).** **`S56-KR` was scored FIRED-A by this morning's KR run.** Nothing here for this desk to settle |
| `handoff/RESEARCH.md` | ✅ | Part A triggers (C/S/D/W) · Part B lenses (L1–L3) · Part C dig list through **D241 (US, unsuffixed)** and **D245-KR** |
| `handoff/README.md` | ✅ | split rule · retention budget · toolkit table |
| `llm_outputs/2026-08-13/preflight/PREFLIGHT_US.md` | ✅ **ran first, this run** | 7 gates + the carried G0 · **PASS 3 / FAIL 5** — the best score this desk has posted. Rights carried into §5 |
| `module_report_tags show` (`DEGAJA_REPORT_DIR=llm_outputs`) | ✅ | Output normal. ⚠ **Its coverage stops at 2026-07-16** — the ledger has not ingested any run since (§4b) |

### 1a. The D165 pre-commitment
`STANDING_VIEW.md` was truncated to 0 bytes on 2026-08-05 by a `'w'`-mode writeback. **Append-only
has held for every completed run since, and this run keeps it.** ⚠ Rows **R27–R45 remain
`[RECONSTRUCTED]`** — binding, but not quotable as original measurements.

### 1b. §5 retracted ledger read BEFORE today's view formed
Read in full first. **Four entries bind stages in this run directly:**

| Row | What it forbids today |
|---|---|
| **R3** | Cross-market transfer of a KR-measured signal. ★ **This binds `ic_ledger` (§3e): the IC scoreboard is KR-only and may NOT be read as a US axis verdict.** |
| **R47** | No stage may state *"the distillate bottleneck released"* as fact — **S55 scored C on 08-12 and the cause is still unseparated.** |
| **R51** | The ENRG wflow/eqflow gap is an **arithmetic identity**, not a signal. |
| **R56** | **`EA` is a delisted constituent still sitting in `us_top300.csv`** ⇒ any COMM aggregate breadth number is contaminated. ⚠ **This run measured a NEW consequence: `EA` returned a null 08-12 close** (PREFLIGHT G5) — the contamination has progressed from "wrong price" to "no price". **Day 29.** |

---

## 2. Scenarios — scored, and named-but-not-scoreable

### 2a. Scored this run — FOUR settlements

All four settle on the **2026-08-12** close, which is settled. Prices re-pulled in full at scoring
(**D140**), `yfinance`, `auto_adjust=False`, benchmark named inline (**C1**).

| ID | Registered | Event date | Branch fired | Observation (frozen text, honoured) |
|---|---|---|---|---|
| **S59** | 2026-08-05 (human-execution loop) | → 2026-08-12 | **FIRED-C** | `NDAQ − XLF` 10-session cumulative, **2026-07-29 → 2026-08-12**: NDAQ **+0.115%** vs XLF **+2.188%** = **−2.073pp**, inside the −5.17 / +4.43 band. ⇒ **the slope-dominant exchange name UNDERPERFORMED its sector over a window containing both NFP and CPI, but not by enough to falsify `M363`'s β +33.2.** ★ **Scoreable despite the FRED gap**: the 2s10s direction is a *qualifier* on branches A and B only, and the observable landed **between** them, so C fires on either 2s10s path. Recorded because the row's own text warned C would be frequent — **it was, for the reason given (conditionality), not for a new one.** |
| **S61** | 2026-08-05 (PREMORTEM Lens 2) | → 2026-08-12 | **FIRED-C** | EW{`STNG`,`FRO`} 5-session cumulative excess vs `SPY`. **Path**: 08-05 −9.863 · 08-06 −2.472 · 08-07 −4.184 · 08-10 **−4.711** · 08-11 −2.411 · **08-12 +3.174**. **Branch A (≥ +6.80 at ANY settled close) never reached** — max +3.174. **Branch B (≤ −4.19 at the 08-12 close) not met** — the 08-12 value is **positive**. ⇒ **no Red Sea war-risk premium appeared in tanker equities; `D168` stays named-but-inert.** 🚨 **CONSTRUCTION FINDING, registered as `D242` (§7)**: **branch B WAS satisfied at the 08-10 close (−4.711 ≤ −4.19) but B is written to settle only on the terminal bar while A settles on ANY bar.** The asymmetry is in the frozen text and is honoured; **no threshold was improvised.** |
| **S72** | 2026-08-08 (PREMORTEM Lens 2) | → 2026-08-12 | 🚨 **AMBIGUOUS — by its own pre-registered rule, not by a scorer's choice** | 1-session excess vs `SPY` on the 08-12 CPI close: **XLI −0.154 · XLF −0.043 · XLB −1.490 · XLU +0.231 · XLE −0.086.** **THREE of five legs read \|excess\| < 0.20pp** ⇒ the row's own clause fires verbatim: *"any leg reading \|excess\| < 0.20pp is recorded as `flat` and the row scores `AMBIGUOUS` rather than being forced into a sign."* ★★ **This is the desk pre-registering its own failure mode and the failure mode arriving.** The only two non-flat legs — **XLB −1.490 and XLU +0.231 — carry OPPOSITE signs**, so neither decomposition is supported even informally. ⇒ **Neither MACRO's three-tilt grouping nor Lens 2's four-tilt grouping gains support; the question is NOT answered and must not be reported as C.** |
| **S73 Leg 2** (equity) | 2026-08-10 (PREMORTEM Lens 2) | → 2026-08-12 close | **NEITHER equity branch fired** | **H-equity**: median 1-session excess vs SPY of {JPM +0.617, BAC +1.015, XLI −0.154} = **+0.617**, against a **≤ −1.50** line ⇒ not fired. **C-equity**: `XLU` **+0.231**, against **≥ +2.00** ⇒ not fired. ⇒ **the July CPI produced no tail equity reaction in either direction.** ★ **Leg 2 did exactly the job it was registered for** — it settled on the CPI session itself and **could not be blocked by the FRED lag that is once again blocking Leg 1.** ⚠ Its registration text pre-stated that Leg 2 is *"a directional CONFIRMATION, not a second discriminator"* — so **a null Leg 2 is not evidence that Leg 1 will be null.** |

### 2b. Named, NOT scoreable at this clock — zero silent skips

| ID | Why not scoreable | Status |
|---|---|---|
| **S73 Leg 1** (macro) | 🚨 **`D212`, exactly as the row pre-declared.** FRED publishes `DGS2` · `DGS10` · `BAMLH0A0HYM2` through **2026-08-11 only**; the 08-12 CPI-day close is unpublished. **The row's own text: *"the first FRED close covering 08-12 may not print until 08-14–08-18. That is NOT grounds to re-date it."*** ⇒ **`PENDING-DATA`, band unchanged.** ★ **The lag is now measurably SHORTER than when the row was written**: H.15 is **1 session behind**, not the 3–4 the four-run block ran on. `T10YIE` already prints **08-12 (2.26, from 2.27 on 08-11 = −1bp)** |
| **S63 · S64 · S67 · S68 · S69 · S71** | **All six settle on the 2026-08-13 SETTLED CLOSE**, which is **20 minutes in the future** at this clock. Re-read at source this run to confirm none settles earlier | **ARMED · settle tonight.** ⚠ **The next run inherits six at once** |
| **S74** | Hormuz — → **2026-08-24** (or on first occurrence) | ARMED. ⚠ `D239` stands: its "conditions harden" branch is an **enumeration of two acts**, and the 08-11 *"Trump demands compensation from Iran"* event fit neither. **Band not moved** |
| **S75 · S76 · S77 · S78** | → **2026-08-19** | ARMED |
| **S79** | NVDA → settle **2026-08-27** | ARMED · **the name binary is now D-13 and inside the calendar window** |
| **S8** | 🚨🚨 **Undated `[blank]`. Un-scoreable for an ELEVENTH consecutive run by this desk** (the KR desk logged its own 11th this morning). A human must `VOID` it or re-register it with a date (P5) | **Named again, not dropped** |

**`EXPIRED` = 0 · silent skips = 0 · past-dated rows left unscored = 0.**

### 2c. ★ The PPI print, read as a macro premise — because `S71` cannot be scored on it yet

`S71` was written for *"a COOL CPI followed by a HOT PPI"*. **The print does not deliver that cleanly,
and saying so now prevents tonight's scorer from reading a reversal into a split print.**

| Series | July 2026 print | Prior |
|---|---|---|
| **CPI** (08-12) | **+0.1% MoM · 3.4% YoY**; **core +0.2% MoM · 2.5% YoY** — all in line with consensus | 3.5% YoY (June) |
| **PPI final demand** (08-13) | **UNCHANGED, 0.0% MoM** SA | −(down) in June |
| **PPI final demand GOODS** | **−0.7% MoM** | −1.4% (June) |
| **PPI final demand SERVICES** | **+0.2% MoM** | +0.5% (June) |
| **PPI core (ex food, energy, trade services)** | **+0.4% MoM** · **+4.7% 12-month** | +0.1% MoM (June) |

⇒ **The headline is cool and the core is hot in the same release.** Goods deflation (energy) is
holding the headline at zero while the **core accelerated 4× MoM (0.1 → 0.4)** against a **4.7%**
12-month rate. **This is neither S71's branch-A world nor a clean branch-B world — it is a split
print, and which half the tape trades is exactly what tonight's `XLU` bar answers.**

⚠⚠ **SOURCE TAG, and it is a downgrade, not a formality**: `[WebSearch — secondary aggregation,
2026-08-13]`. **The BLS primary release returned HTTP 403** to a direct fetch, and **PREFLIGHT G1
revoked the desk's own news path**, so these numbers rest on **two independent search aggregations
that agreed**. They are tagged **`[inferred-source]`** and **may not be cited as `[measured]` by any
downstream stage** until MACRO re-pulls them from FRED (`PPIFIS`) or a reachable primary.

---

## 3. Both ledgers audited — `due` run on each, every row resolved or named

### 3a. Rejection ledger — 149 rows · 70 resolved · **legacy (no `revives_if`) = 0** · 6 due

★ **The legacy count is ZERO for a second consecutive US run.** That was the ledger's founding defect
(24 of 25 rows entered with no revival condition) and it is closed. Reported because the L1 requires
evidence the practice is taking hold, not a quiet pass.

| Row | Registered condition | Fresh measurement (sweep asof **2026-08-12** unless noted) | Resolved |
|---|---|---|---|
| **MRK** (rej. 07-23, B.momentum-only) | CY revision breadth ≥2↑:0↓ over 30d **OR** CY estimate stops falling 2 consecutive weekly pulls | `module_fundamentals_us`: CY 30d breadth **1↑ / 2↓** ✗; CY consensus **2.74 now vs 2.76 seven days ago** ⇒ latest weekly delta is still **negative** ✗ | **`reaffirmed`** ⚠ **Counter disclosed on the same line**: its *price* axes have turned — OBV **+0.302 accumulating**, RS20 **+5.2**, RS60 **+14.8**, flow +0.389. **It stays out on the registered condition, not on weak flow** |
| **QCOM** (07-30, K.body-refutation) | RS20 vs SPY > 0 **AND** the Apple-content leg replaced by a named design win | RS20 **−10.7** ✗ (RS60 −23.6, OBV −0.112 distributing, flow **−0.856 🔴**) | **`reaffirmed`** — the AND is broken by the price leg, so the row resolves **on measurement**, not on the news leg G1 killed |
| **PANW** (07-31, H.valuation-spent) | OBV → accumulating **AND** RS20 vs SPY > 0 | OBV **−0.055 = NEUTRAL** ✗ · RS20 **+7.0 ✓** (RS60 +54.9) | **`reaffirmed`** — a **one-leg miss**, narrowly. Flagged for an earlier recheck if OBV crosses |
| **SNDK** (07-31, A.flow-never-arrived) | OBV → accumulating **AND** RS20 > 0 | OBV **−0.176 distributing** ✗ · RS20 **−19.1** ✗ · flow −0.700 🔴 | **`reaffirmed`** — the widest failure of the six |
| **NEM** (08-08, A.flow-never-arrived) | 30d FY revision breadth net-positive **OR** XLB exc5 vs SPY clears +1.9 **with NEM under one third** | ★ **Leg (b) FIRED inside the window and was independently verified when S57 was scored**: XLB exc5 **+2.227 (08-10)** and **+2.484 (08-11)** vs a +1.9 line, with **ex-NEM cap-weighted +1.203, equal +0.908, 8 of 12 names positive, NEM only 11.6% of sector cap** (< ⅓) | ★ **`revived`** ⚠⚠ **Disclosed against the revival, on the same line**: on the recheck DATE itself (08-12) **XLB exc5 has fallen back to −0.465 while NEM's own exc5 is +12.642** ⇒ **the broadening that satisfied the condition has REVERSED and Materials is now NEM alone.** Revived because the condition **demonstrably occurred**; the reversal is recorded, not used to un-see it. **Same anchor-vs-window class as `D233`, now on a ledger `revives_if` rather than a bracket** |
| **DHT** (07-31, A.flow-never-arrived) | RS60 vs SPY > 0 **AND** Hormuz / tanker-rate **body-confirm** | RS60 **+1.61 ✓** (RS20 +1.60). **Leg 2 CANNOT BE EVALUATED — PREFLIGHT G1 FAIL, the news search layer is dead in both bridges** | 🚨 **STILL PENDING — named, not silently carried.** ⚠ **This is its FIRST carry, not its second**, so it is not yet a process failure — **but it becomes one at the next HANDOVER if G1 is still down.** Partial context that does *not* substitute for the body-confirm: the tanker complex is **internally split** — FRO RS60 **+3.43**, INSW **+4.71**, but **STNG −11.78** |

### 3b. Missed-entry ledger — 107 rows · 38 resolved · **legacy = 0** · 2 due
⚠ **Sign is INVERTED here** (`excess > 0` means missing it cost us). The two ledgers' `excess`
columns are **not** summed anywhere in this run.

| Row | Entry condition | Measurement | Status |
|---|---|---|---|
| **INSW** (07-31, U.never-surfaced) | body-proximity Hormuz/tanker-rate confirm **AND** RS60 vs SPY holds > 0 | RS60 **+4.71 ✓**; body-confirm **unevaluable (G1)** | 🚨 **PENDING — named.** First carry |
| **FRO** (07-31, U.never-surfaced) | body-confirm **AND** RS60 vs SPY > 0 | RS60 **+3.43 ✓**; body-confirm **unevaluable (G1)** | 🚨 **PENDING — named.** First carry |

★ **Both ledgers' pending rows fail on the SAME leg — a news body-confirm — and all three names sit
in the SAME theme (tankers).** That is not three independent gaps; it is **one instrument outage
projected onto three rows**, and it is the clearest measured cost of PREFLIGHT G1 this run.
⚠ Note the coincidence with **S61 FIRED-C** on the same basket: the *price* half of the tanker
question answered "no premium", while the *narrative* half is unreadable. **The two halves are not
substitutes** — S61 scoring C does not resolve DHT/INSW/FRO, because their conditions are conjunctions.

### 3c. Rejection-ledger `score` (context, not a gate)
Run alongside `due` as the L2 requires. Benchmarked against the **equal-weight ≥$1B universe**, never
the index. Read as *which reason classes are earning their keep*, and **not** as a surface for a
revived name — that is `due`'s job and `due` did it above.

### 3d. Exposure state — **read, and it is the KR contest book, not this desk's**

```
python -X utf8 scripts/exposure_rule.py state    → rule-state 정상 (prior 방어), bench 069500.KS
python -X utf8 scripts/exposure_rule.py show --tail 10
```

| Item | Value |
|---|---|
| Rule state | **정상 / normal** (prior: 방어) — bench **069500.KS** close 107,270 · **+3.893% on the day** · −5.26% from the 20d high · **+22.41% from the 20d low** · volume 0.864× |
| Target invested | **95%** · current **55.6%** · **band gap −39.4pp** 🚨 |
| Cumulative decomposition, **n = 7** | total excess **−12.84pp** = **cash contribution −5.49pp** + **selection contribution −7.35pp** |
| Alerts | 🚨🚨 `ARMED (TIMEFOLIO_EXECUTE=1)` · ⚠ **unsettled bar (intraday KIS live)** on today's row |

⚠⚠ **Three disclosures this desk must carry rather than quote:**
1. **This ledger's benchmark is `069500.KS` (KODEX 200) and its book is the KR contest book.** It is
   **not** a US exposure state. **R3 / W1 forbid transferring it into a US conclusion** — it is
   carried here as *size context that exists*, and BET/ALPHA may cite the **band gap** as a fact about
   the book, never as a US allocation signal.
2. **n = 7.** The file prints its own warning: the sign is not askable until n ≈ 20 (**C4**).
3. **Today's row is an UNSETTLED intraday bar.** The cumulative number moves when it settles.

★ **Not a cold start** (34 rows accrued), so the 2026-07-31 cold-start failure mode does not apply.
✅ **This L2 did NOT run `log`** — accrual belongs to the 09:10/15:00 timefolio tasks.

### 3e. Signal scoreboard (`ic_ledger score`) — **and the transfer rule that binds it**

387 ledger rows · **21 simultaneous tests** ⇒ read against **Bonferroni |t| > 2.8**, not 2.

| Axis | h | n | n_eff | mean IC | t(NW) | verdict |
|---|---|---|---|---|---|---|
| **`vol_surge`** | 1 | 25 | **25.0** | **−0.0482** | **−3.08** | ★ **significant, clears Bonferroni** |
| `vol_surge` | 5 | 20 | 4.0 | −0.0385 | −2.60 | significant on the solo bar only |
| `flow_score` | 1 | 25 | 25.0 | −0.0431 | −1.01 | indistinguishable |
| `obv_norm` | 1 | 25 | 25.0 | −0.0240 | −0.79 | indistinguishable |
| `rs20` | 1 | 24 | 24.0 | −0.0484 | −0.89 | indistinguishable |
| **14 of 21 cells** | — | — | **< 4** | — | — | 🚨 **unquotable (overlapping forward windows)** |

★ **The standing item, reported every run as required**: **`vol_surge` is the only axis with a
consistent sign across two horizons and it is NEGATIVE** (h=1 −3.08 · h=5 −2.60), agreeing
independently with **M224** — **while `sector_flow`'s 🟢 tag still weights it positively.** The gate
is **not** flipped (P4, and it has not been re-measured on US data).

⚠⚠ **THE BINDING CONSTRAINT, and it is stronger than it looks: this scoreboard is `# IC LEDGER — KR`.**
Every cell is measured on the **KR** ranking. **R3 is the retracted-ledger row that exists precisely
for this** — a KR-measured signal applied to a US index, where the source document itself recorded US
replication failure. ⇒ **No US stage in this run may cite these t-statistics as a verdict on a US
axis.** What *is* citable: **the US desk has no IC scoreboard of its own**, and that is a gap, not a
result. Registered as **`D243`** (§7).

---

## 4. Reconciliation, staleness, and the ledger that stopped moving

### 4a. Stale rows and cleared suspensions

| Item | asof | Flag |
|---|---|---|
| `us_top300.csv` | 2026-07-15 | 🔴 **29 days** (limit ≤8). **All `wflow` weights and every `top1_w` in the flip list are 29-day-old caps** |
| `us_all_v2_candidate.csv` | 2026-08-10 | Exists, **unpromoted**. Promotion is a human decision (P5) — **carried, not acted on** |
| **`EA` in `us_top300.csv`** | went private 2026-08-04/05 | 🔴 **Day 29.** **R56.** ⚠ **New this run: it now returns a NULL 08-12 close**, so the contamination is no longer a wrong number — it is a hole |
| FRED H.15 / OAS block | through **2026-08-11** | 🟡 **1 session behind** — materially better than the 3–4 that blocked four runs. **Still blocks `S73` Leg 1** |
| `T10YIE` | through **2026-08-12** | 🟢 current — **2.26, −1bp on the CPI session** |

**Cleared suspensions → dig instructions**: none cleared this run.

### 4b. 🚨 Mechanical ledger vs the analytical carry — they have DRIFTED APART

`module_report_tags show` runs clean and its **newest entry is `2026-07-16`**. Meanwhile
`handoff/` has absorbed **~25 completed desk runs** since. ⇒ **the two objects the L1 says must be
cross-read are no longer describing the same period**: *what we believe* is current to today, *what
we covered* stopped four weeks ago.

★ **This is not a "belief without coverage / coverage without belief" reconciliation** — that
comparison is **unavailable**, because the mechanical side has no rows to compare against. **Naming
the unavailability is the finding.** Registered as **`D244`** (§7). It also means the run-end handoff
step (`pipeline/handoff.md`) has more work than a normal append.

### 4c. ID hygiene — checked at READ time, and the audit is once again crying wolf

`handoff_id_audit`: **max M612 · 153 colliding M ids · D237–D241 reported as "declared 2×".**

⚠⚠ **The D-side collisions are FALSE POSITIVES and this run opened the file BEFORE saying so** — the
correction 08-12 RUN-2 had to make in place. `RESEARCH.md:1948` declares **`D231-KR ~ D237-KR`**
(suffixed) and `:2045` declares **`D237–D241`** (unsuffixed); `:2080` declares **`D239-KR ~ D245-KR`**.
**Two correctly-formed namespaces.** The tool parses `##` headers by numerals and drops the suffix —
**`D240`**, already registered. ✅ **The M-side 153 are real** (same-namespace).

**ID ranges this run takes**, checked by grep across all nine handoff files at read time:
**`M613+`** (max 612) · **`D242+`** (US unsuffixed max **D241**; the KR run explicitly reserved
D242+ for this desk in `RESEARCH.md:2075`) · **`S80+`** (max S79) · **`R64+`** (max R63).

---

## 5. 🚨 Instrument health inherited — what this run may NOT claim

From `llm_outputs/2026-08-13/preflight/PREFLIGHT_US.md` — **PASS 3 / FAIL 5**, the best this desk has
scored (08-10: 1/6 · 08-12: 2/5).

| Gate | Verdict | Binding consequence for this run |
|---|---|---|
| **G0** bars/dates | 🟢 PASS | ✅ **RS may be compared at fine grain** and **`vol_surge` read in both directions** — both were revoked on the last two runs. `asof 2026-08-12` needs no caveat |
| **G1** news axis | 🔴 FAIL (17.0%) | 🚫 **No velocity, no theme freshness, no "it went quiet", no `theme_age`/`chain_hop`/`drift_watch` citation.** **DRIFT must report its instrument was dead, not report "no drift."** The 51 surviving names are a **survivor sample** and are not usable either |
| **G2** scale continuity | 🟢 PASS | ✅ **Δ is valid and spans exactly ONE settled session (08-11 → 08-12)** — the cleanest Δ in a week. 300/300 names carry it |
| **G3** sector sign owner | 🟢 PASS | 🚫 **Industrials and Materials may not be promoted or demoted on `wflow`** (flippers `CAT` 8.7% · `LIN` 24.7%). Both sectors' `eqflow` points **opposite** to their `wflow` |
| **G4** risk units | 🔴 FAIL | 🚫 No single-number concentration guard; the `--days` window goes on the same line as any concentration claim; **no verdict on whether `AVGO`+`NVDA` are one unit** (250d says two, 500/750d say one) |
| **G5** universe | 🔴 FAIL (age) | 🚫 `wflow` is **not** "current-cap weighted" — 29-day-old caps. 🚫 No flow/RS/OBV verdict on **`EA`**. ✅ **11/11 US holdings are inside the universe AND scored** — zero "held but unmeasurable" names |
| **G6** estimate accrual | 🔴 FAIL (2.6×) | 🚫 No `kelly_size --ic` figure reported as evidence-backed. Any size is labelled **"mechanical ¼"** |
| **G7** tools | 🔴 FAIL (2/41) | `margin_history.py` and `module_chart` fail `--help` for a **4th run**; both pass functional probes ⇒ **citable only via those probe command lines** |

★ **The intermittency finding, which is new and matters more than the FAIL itself.** The remote news
bridge was **ALIVE at 08:40 KST today** (the KR desk logged 5/5 successes on the same tunnel),
**ALIVE at 22:45 KST on 08-12** (RUN-2 explicitly restored G1 and used it), and **DEAD at 22:14 KST
today** (5/5 `URLError`). ⇒ **This is not a persistent outage — it is an availability pattern, and
the desk has never characterised it.** Meanwhile the client-side store proves the corpus is fine:
**51,718 articles for 08-06→08-13, including 476 `Nvidia` title hits.** Registered as **`D245`** (§7).

---

## 6. RESEARCH triggers loaded as binding constraints — which group binds which stage

Loaded as constraints, not as a summary (the L1's own measured failure: three of six reversals broke
rules that already existed in prose nobody read).

| Group | Fires when | Binds, this run specifically |
|---|---|---|
| **C** — C1 baseline · C2 both halves · C3 unknown column · C4 "indistinguishable" · C5 arbitrary choice | you cite a number | **MACRO** (every excess return names its benchmark inline) · ★ **C2 binds §2c hardest: the PPI headline and the PPI core point OPPOSITE ways and neither may be quoted alone** · **C4** binds S72's AMBIGUOUS — "not answered" ≠ "C" |
| **S** — S1 date-fold · S2 diagnose the null · S3 power first · S4 in-sample≠done · S5 short samples · S6 future labels | any statistical claim | **SWEEP / ROTATION**: Δ is **one** session — S1 forbids "the trend turned." **S5** binds §3e (14 of 21 IC cells unquotable) and G4 (249-bar window). **S2** binds G1: diagnose the null before reporting it |
| **D** — D1 second venue · D2 proxy sign · D3 signed vs unsigned · D4 regime contamination · **D6 signal grade (OBV is C)** | you read data | **SWEEP · ALPHA**: OBV is **grade C** and carries no verdict alone — ⚠ with the news axis dead, OBV's *load* rises while its *grade* does not. **D6's S56 scope limit stands**: share-counted positioning ≠ percentile positioning |
| **W** — W1 cross-market transfer · W2 inherited lead/lag · W3 real≠profitable · W4 name the customers · W5 sub-sector dispersion · W6 reader's-market spine | you write a conclusion | ★★ **W1 is the load-bearing rule of this run** — it binds §3d (KR exposure ledger) and §3e (KR IC ledger) and it is why the DEEP budget stays **N=4** while `industry_kr` cut to N=2. **W5** binds ENRG (refiners ≠ integrateds) and MATR (**NEM ≠ the other 11**) |
| **L** — L1 second derivative · L2 peak-margin trap · L3 branch information content | lenses, not triggers | **DEEP · PREMORTEM.** **L3** owns tonight's mandatory bracket; **L1** owns the PPI read (0.1 → **0.4** MoM core is a second-derivative statement) |

---

## 7. Dig list — ranked for today, plus the four this run registers

### New this run (`D242`–`D245`, unsuffixed US namespace, reserved for this desk by the KR run)

| # | Dig | How it was found | Human needed? |
|---|---|---|---|
| **D242** | ★★ **A bracket whose branch A settles on ANY bar while branch B settles only on the TERMINAL bar is not symmetric, and `S61` just paid for it.** S61's path touched **−4.711 on 08-10**, past branch B's **−4.19** line, and scored **C** because B is written to the 08-12 close alone. **The row is honoured as frozen — no threshold was improvised** — but the asymmetry was invisible until a path crossed one line and not the other. **Positive-form remedy: registration should state each branch's settlement mode (`ANY` vs `TERMINAL`) explicitly and, when they differ, say why.** Same family as `D233` (anchor-vs-window) | HANDOVER §2a scoring S61 | **human (settle the convention once, board-wide) · PREMORTEM (state the mode at registration)** |
| **D243** | ★★★ **The US desk ranks 300 names every run and has NO IC scoreboard for its own rankings.** `ic_ledger score` prints **`# IC LEDGER — KR`**; all 387 rows and all 21 tests are KR. **R3 forbids reading them as a US verdict**, so the US desk's flow/OBV/RS axes are **completely unscored** — and the one axis with a Bonferroni-clearing sign (`vol_surge`, negative) is exactly the axis `sector_flow` weights positive **in both markets**. ⇒ **the desk cannot say whether its US ranking has a sign, in either direction.** **Positive-form remedy: run `axis_inflection` + `ic_ledger log` on the US sweep so a US column starts accruing** — the same "learn from an N-name ranking, not from 11 positions' P&L" argument that justified the KR ledger | HANDOVER §3e, applying R3/W1 | **human (wire it) · HANDOVER (report the absence every run until it exists)** |
| **D244** | ★★ **The mechanical tag ledger and the analytical carry have drifted 4 weeks apart, and the reconciliation the L1 mandates is therefore UNAVAILABLE, not clean.** `module_report_tags show` runs without error and its newest row is **2026-07-16**; `handoff/` is current to today. The L1 asks for three cross-reads (belief-without-coverage, coverage-without-belief, resolved-but-live) and **none can be computed.** ⚠ **The danger is that a clean-exiting tool reads as a clean reconciliation** — the exact class `preflight` exists for. **Positive-form remedy: either point `DEGAJA_REPORT_DIR` at the live output root and re-ingest, or have `show` print its newest-row date so staleness is visible in the output** | HANDOVER §4b | **human (choose the ingest mode — this is the open PROMPT_MAP §6 decision) · every HANDOVER: quote the ledger's newest date** |
| **D245** | ★★★ **The news bridge is INTERMITTENT, not down, and nobody has characterised the pattern.** Measured across 26 hours on one tunnel: **ALIVE 08-12 22:45 KST** (RUN-2 restored G1 and used it) → **ALIVE 08-13 08:40 KST** (KR desk, 5/5) → **DEAD 08-13 22:14 KST** (5/5 `URLError`). The client store holds **51,718 articles for 08-06→08-13 incl. 476 `Nvidia` title hits**, so the corpus is healthy throughout. ⇒ **every G1 FAIL to date has been logged as an outage, and at least some of them are a availability window the desk could schedule around.** **Positive-form remedy: log a timestamped reachability probe on every desk run (3 lines) so the pattern becomes measurable; and give the local FTS index a rebuild owner — `news_fts.db` has been 0 bytes since 08-12 and `news_fts_kr.db` since 07-30** | PREFLIGHT G1 + cross-reading the KR desk's 08:32 run | **human (server console — FTS writes are server-only, P6) · idle_probe (characterise the window)** |

### Carried digs re-confirmed rather than re-discovered
**`D212`** (⚠ still binding on `S73` Leg 1 — **but measurably smaller: 1 session, not 3–4**) ·
**`D17`** (⚠ **EIGHTH run — `drift` still absent from `DB_READ_CMDS`**; DRIFT will hit it again at
stage 11) · **`D233`** (anchor-vs-window convention — **a human call, now with a second instance in
§3a's NEM revival**) · **`D239`** (S74's two-act enumeration, band unmoved) · **`D240`** (the audit's
false cross-namespace collisions — **applied correctly this run, file opened first**) · **`D241`**
(velocity `0.00×` vs no-match — **untestable today; the whole axis is down**) · **`D237`**
(shock-conditional risk units — its dated test is `S79` Leg 2) · **`D211`** (dig-counter collision —
**human pending, 7th run**) · **`D6`** (OBV grade C).

### Ranked for THIS run's DEEP slots — the top open questions
1. **MATR** — `S57` FIRED-A twice and the N− was carried anyway; `S77` is its replacement falsifier.
   **New today: XLB exc5 collapsed +2.484 (08-11) → −0.465 (08-12) while NEM alone ran +12.642.**
   The sector is now one name. **Flagged by ROTATION 08-12 as "next run's first rotating pick."**
2. **FIN** — demoted N+ → N on `eqflow` while **S51 CONFIRMED** its NIM mechanism; `S78` brackets the
   disagreement. **CPI produced no bank move (JPM +0.62 · BAC +1.02, both inside noise).**
3. **IT** — the board's only breadth-count vs breadth-eqflow **sign disagreement**; the CXMT/Apple
   supply axis (**P43**) has been carried **UNREFRESHED for three runs** because the news feed is down.
4. **COMM** — the telecom node (T/VZ/CMCSA) **un-owned for a 5th run**, and `R56`/`EA` now blocks the
   aggregate with a **null price**, not just a stale one.
5. **ENRG / INDU** — the two continuous slots; **S67 (ENRG) and S64 (INDU) both settle tonight.**

---

## 8. Claims this run asserted and then refuted (§4c · D48)

**Two, both left visible rather than edited away:**

1. **Asserted** (this stage, drafting §2b): *"the six 08-13 rows may be scoreable because the PPI
   print has already landed."* **Refuted by the observable's own text** — S63/S64/S67/S68/S69/S71
   settle on the **08-13 SETTLED CLOSE**, and this run's clock is **09:10 ET, twenty minutes before
   the open.** A print landing is not a session closing. ⇒ **all six correctly named as not-scoreable.**
2. **Asserted** (this stage, reading `catalyst_calendar`): *"the ≤48h binary is ahead of us."*
   **Refuted by arithmetic in the same minute** — 08:30 ET is **40 minutes BEHIND** a 09:10 ET clock.
   The run's framing changed as a result (§0), which is why the correction is worth its line.

⚠ **A third, adjacent, worth naming**: this stage began to treat **S61 FIRED-C** as resolving the
tanker question and therefore as grounds to close DHT/INSW/FRO. **It does not** — those rows'
conditions are **conjunctions with a news leg**, and a price answer cannot discharge a conjunction.
Caught before the `resolve` calls were made; **the three rows are carried as PENDING (§3a/§3b).**

★ **Zero self-refutations would itself be a finding** (it usually means the controls were not
adversarial). Three, with two of them about this stage's own clock, is the honest count.

---

## 9. What this stage hands to MACRO

- **Inherited tilts, verbatim from `SECTOR_ROTATION.md 2026-08-12 §1 + its three deltas**:
  **`INDU OW− · ENRG OW− · FIN N · IT N · HLTH N+ · DISC N · MATR N− · COMM UW · UTIL UW · STPL UW− ·
  RE UW`**
- **Regime call inherited unchanged** `[inferred]`: *memory is a price-cycle industry in
  rate-of-change deceleration while its level stays tight* — carried, **not cited as evidence**.
- **§4 asymmetry, unchanged**: a hyperscaler capex **cut** changes the thesis; a **raise** only moves
  its timing. **Encode before each print** — and **NVDA prints 08-26 (D-13)**.
- **The macro premise of the day**: a **cool CPI (08-12)** followed by a **split PPI (08-13)** —
  headline **0.0%**, goods **−0.7%**, **core +0.4% MoM / +4.7% 12m**. Tagged **`[inferred-source]`**
  until MACRO re-pulls it (§2c).
- **Four scored rows** (S59 C · S61 C · S72 AMBIGUOUS · S73 Leg 2 null) and **thirteen still armed**,
  six of them settling tonight.
- **The rights table** (§5): speak with settled prices, RS at fine grain, OBV, breadth, positioning,
  FRED and primary documents. **Do not speak with the news axis, theme age, or a single
  concentration number.**
