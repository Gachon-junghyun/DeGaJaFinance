# HANDOVER — industry_US · 2026-08-16 (Sun KST) · Stage 2/11 (L1·HANDOVER)

> Inheritance only. No sizing, no buy/sell language (P4). This stage transports what the desk already
> believes, scores what has matured, and states what today's instruments forbid.

## 0. Run clock — and the ONE structural fact that governs everything below

| | |
|---|---|
| Run clock | **KST 2026-08-16 20:05–… = ET 2026-08-16 07:05–… — SUNDAY, US cash closed** |
| Price asof | **2026-08-14 settled close** (Friday) |
| Δ baseline | `history.json["2026-08-13"]`, same 3-axis mode ⇒ Δ = 08-13 → 08-14 |
| ★ **Sessions observed since the prior run** | **ZERO** |

**The defining fact of this run, stated first because it changes how every later stage must write.**
The prior `industry_US` run executed on **Saturday 08-15** and priced off the **08-14** close. Today is
**Sunday**. The last settled US session is still **08-14**. Therefore:

- The sweep re-ran and produced **the same numbers** — 11-sector `wflow`/`eqflow`/`breadth` identical
  to three decimals, all three G3 flippers identical, `SPY` bars identical, last-bar volume ratio
  identical at **0.649**.
- Today's Δ (**08-13 → 08-14**) is **the same interval the 08-15 run reported**. The run wrote to the
  **same `history.json` key `2026-08-14`**; it created no new key.
- ⇒ **Agreement between this run and yesterday's is evidence that one input was read twice.** It is
  **not** persistence, confirmation, stability, or a "second consecutive" anything.

The KR desk reached the identical conclusion at 08:39 KST this morning, independently and for the same
calendar reason. **Two desks, one weekend, zero new price information.**

★ **What this does NOT mean.** The desk is not blind today. **Three axes are not keyed to the equity
session and CAN have moved**: `[FRED]` macro series (published on their own calendar), the **news
corpus** (the client store un-stalled overnight — §6), and **primary filings**. Those are where this
run's only genuinely new information can come from, and later stages should spend their effort there
rather than re-reading a frozen tape.

---

## 1. Inherited regime call — carried verbatim, tag intact

> **Memory is a price-cycle industry in rate-of-change deceleration while its level stays tight.**
> `[inferred]` — built on the measured chain `M1`–`M9`, `M18`, `M143`.

In a commodity-cycle industry the equity tracks the **second derivative of price**, not the level.
Level and rate point opposite ways, which is why "shortage persists" and "the stocks struggle" are both
true and not contradictory.

⚠ **`[inferred]` may be carried; it may not be cited as evidence for a new proposition.** Any stage
leaning on the regime call must name the measured row underneath it, not the call.

**The superseding live macro object — `P56`, carried unchanged:** the long-end repricing is **term
premium**, not a real-rate *level* move (`M653`: 30y−10y +0.48 → +0.56 with `DGS2` **unchanged**;
`M654`: breakevens falling, HY OAS flat, NFCI loosening — none of the three usual channels confirms).
`P51` scored **HIT**; `P56` replaced its stated cause while keeping its sign. ⚠ `P56` carries a **named
competing explanation** since 08-14 (a geopolitical driver — *"Treasury yields rise as U.S. threatens
Iran with more economic sanctions"* [`cnbc` 08-14]). **Its `[inferred]` tag stands.**
★ **MACRO's first job today**: `[FRED]` is the one instrument that could have moved. **`P56` is testable
this run and the tape is not** — that asymmetry should decide where MACRO spends its budget.

---

## 2. Sector verdict board inherited from 2026-08-15 (unchanged until ROTATION acts)

| Sector | Verdict | Carried because |
|---|---|---|
| **ENRG** | **OW** | **Promoted 08-15** on `eqflow +0.102` and `breadth 0.12`, **both the highest of eleven and neither cap-weighted**; the two-run Δ blocker narrowed 73% (−0.157 → −0.042). Counter-evidence stated: Δ is still the **2nd-worst rank** of eleven |
| **INDU** | **OW−** | `D249` unresolved for a **5th** run — the bracket measures `XLI`, the position is **defense**. An OW attempt was declined **on method** (the 25-of-50 accumulation count is a C5 invented metric) |
| **IT** | **N+** | **Held 08-15 with the basis decayed 95%** (Δ +0.152 → +0.007). N+ now rests on `eqflow +0.044 > wflow +0.023` **alone**. Its falsifier `S85` settles 08-21 |
| **HLTH** | **N** | Promotion to N+ declined 08-15 — Δ **−0.103 = worst of eleven**, 4th consecutive negative |
| **FIN** | **N−** | `M40`'s inversion **has not repaired** (`eqflow −0.126` below `wflow −0.031`); `R69` stands |
| **MATR** | **N−** | Flipper (`LIN` 24.7%) ⇒ `wflow` inadmissible; every permitted axis refuses |
| **DISC** | **N−** | Demote to UW declined 08-15 — **Δ +0.038 is positive**, the wrong direction |
| **COMM** | **UW** | Both directions blocked, **and the bucket changed membership** (`EA` dropped out of the scored set) |
| **STPL** | **UW−** | Declined **on notation** for a 2nd run — UW− is this board's floor |
| **UTIL** | **UW** | The board's **only real (non-`vol_surge`-artifact) flow absence**: 0 of 15 accumulating — against `XLU` exc5 +1.207 |
| **RE** | **UW** | The most internally consistent verdict — **but 4 of 12 names accumulate** (`EQIX` `DLR` `CBRE` `IRM` = `M131`'s data-centre unit) |

**Last DEEP:** ENRG 08-15 · INDU 08-15 · DISC 08-15 · RE 08-15 · COMM 08-14 · FIN 08-14 · IT 08-13 ·
HLTH 08-13 · MATR 08-13 · UTIL 08-12 · **STPL 08-10**.
⇒ **Recency-ranked candidates for today's rotating slots: STPL (6 runs) · UTIL (4 runs) · IT / HLTH /
MATR (3 runs each).** ROTATION owns the decision; this stage only reports the clock.

⚠ **A structural warning for ROTATION, stated here so it is not discovered late.** With **zero new
sessions**, every flow input to a verdict change is byte-identical to the one that produced yesterday's
verdicts. **A verdict delta today would have to be justified by something other than flow** — a new
`[FRED]` print, a new filing, or an error found in yesterday's reasoning. Thrash on unchanged numbers
is the specific failure this note exists to prevent.

---

## 3. Scenario status — **EXPIRED = 0 · silent skips = 0**

### 3a. Matured this run
**None.** Condition-check executed on every ARMED row rather than skipped:
- `SCENARIOS_US.md` opened — nearest US-owned settlements are **08-19** (`S75` `S76` `S77` `S78` `S80`),
  **08-20** (`S82` `S83`), **08-21** (`S84` `S85` `S86` `S87`), **08-24** (`S74`), **08-26/27**
  (`S79` `S81`).
- `SCENARIOS_KR.md` opened (the other market's file — a past-dated KR row would still be this run's to
  score). Nearest is **`S51-KR` → 2026-08-17, tomorrow**; then `S52-KR` 08-19 · `S57-KR` 08-20 ·
  `S58-KR` 09-09 · `S61-KR` ~09-14 · `S45` / `S54-KR` 09-30 · `S60-KR` 10-12 · `S49-KR` 10-30 ·
  `S53-KR` 10-31 · `S59-KR` 11-04.
- **Zero rows past-dated for either desk.** ★ And the reason is mechanical, not lucky: **no observation
  window could close, because no session settled.** The KR desk logged the same null result this morning.

★ **`S82` is worth naming even though it does not settle today**: it was **already above its branch A at
+3.091** at registration, disclosed at registration rather than discovered later. Same shape as `S85`,
which sits at **+1.343 = branch C** and falsifies the IT N+ **on the axis the promotion used**.

### 3b. 🚨🚨 `S8` — undated, un-scoreable, **FOURTEENTH consecutive run**
`S8` remains `[blank]`-dated and cannot be settled by any desk. The KR run named it as its 13th this
morning; this makes **14**. **A human must `VOID` it or re-register it with a date (P5).**
⚠ And its observable moved over the weekend while the bracket stayed undated — the KR run logged
2026-08-15 *"이란, 美호르무즈 소유권 주장"* [asiae, 1 outlet] and 2026-08-14 *"'개방도 폐쇄도 아냐'…
호르무즈 항로 다층화 '뉴노멀'"* [yonhap, single-source tier], while `CATALYST_WATCH` still carries the
Hormuz statement as an **undated 🔀binary**. **Named again, not dropped.**

---

## 4. Both ledgers audited — clean, and clean for the right reason

| Ledger | Total | Resolved | **Legacy (no revival/entry condition)** | **Due now** |
|---|---|---|---|---|
| `reject_ledger` | **176** (+7 vs 08-15) | 90 | **0** | **0** |
| `missed_ledger` | **134** (+8 vs 08-15) | 51 | **0** | **0** |

★ **The legacy count is the number that matters and it is 0 on both sides, for a third run.** This
desk's most expensive measured error (`SK이터닉스`, **+41.2pp and +26.9pp**) happened because 24 of 25
rows carried no `revives_if` at all, so "any row whose condition has come true" was unstatable.
⚠ **A clean `due` is not evidence of health on its own.** It is evidence here only because **both**
conditions hold: legacy = 0 **and** the totals are still growing (169→176, 126→134). Report them together.
⚠ `missed_ledger`'s `excess` sign is **inverted** relative to `reject_ledger`; the two are never summed
without aligning signs. Its `score` block remains **outcome-selected** (the first 6 rows were harvested
from `leak_scan --top`) — quotable as accumulation, never as an edge.

---

## 5. Exposure state — carried as size context, not as a gate

`scripts/exposure_rule.py state` · benchmark `069500.KS` · asof **2026-08-14 settled**

| Item | Value |
|---|---|
| Rule state | **정상 / normal** (previous: normal) — no firing condition met |
| Target invested | **95%** |
| **Current invested** | 🚨 **UNKNOWN — the account query did not run**, so the band gap cannot be computed today |
| Ledger rows | **35** |
| Cumulative decomposition (n=8) | **total excess −14.21pp = cash −6.26pp + selection −7.95pp** |
| Last measured band gap | **−27.0pp** (08-14, live bar) |

🚨 **Reported as unknown, not substituted** (P5). The state machine is **not** cold-starting (35 rows),
so the `정상` verdict is usable; the **invested %** is not.
★ **The decomposition is the line BET/ALPHA must carry**: over the accrued window the desk is behind on
**both** legs — cash weight −6.26pp *and* selection −7.95pp — so *"we were defensively positioned"* does
not explain the shortfall. ⚠ **n=8**, and it did not grow this run (no session). At this n the split is
**indistinguishable from zero (C4)**; it is reported to make the n grow, not to be acted on.
⚠ Standing alarm on every row: **`TIMEFOLIO_EXECUTE=1` is ARMED**. Analytical desks never pass
`--execute`; this run does not.

---

## 6. Instrument health inherited from PREFLIGHT — **the binding table**

Read `llm_outputs/2026-08-16/preflight/PREFLIGHT_US.md` (written **before** this stage). **PASS 3 /
FAIL 5.** The gate table is a rights table, and these are the rights:

| Stage | 🚫 Cannot use today |
|---|---|
| **ALL** | ★ **any Δ or comparison written as "today", "the latest session", "now accelerating"** — zero new sessions · **agreement with yesterday's report cited as confirmation** |
| SWEEP | the sweep's velocity axis · **the 50 survivors** · theme freshness · "quiet" · **32-day-stale caps described as current** · any verdict on `EA` |
| EVENT_ALPHA | "theme is fresh/cooled" from an **empty** `theme_age`/`chain_hop` result · `news_vectors.db` **after 2026-08-15** |
| ROTATION | **`wflow` promotion/demotion for IT · Industrials · Materials** (G3 flippers) · "the third run running" as a persistence argument |
| PREMORTEM | "the tape has gone quiet on this risk" — **measured: 0 of 80 silent names were quiet, across two runs** |
| DEEP | the velocity axis as an axis · "no news flow" as evidence |
| BET/SIZE | single-number concentration · `--ic`-backed size (→ **"mechanical ¼"**) · `AVGO/NVDA` and `ANET/ETN` unit counts |
| DRIFT | **must state whether its instrument answered, with the probe clock time.** An empty burst list is not "no drift" |

**✅ What is available, stated positively.** Settled prices through **08-14** with fine-grain RS (G0
clean, **4th** run) · OBV · **eqflow / breadth** (unweighted, so the 32-day-stale caps barely touch them
— they carry more load today, not less) · `vol_surge` **both directions** · FINRA short pressure · CFTC
COT percentiles · `[FRED]` · primary filings · `margin_history` · **per-name news velocity by hand probe**.

★ **A right RESTORED today: `news_vectors.db` is usable again through 2026-08-15.** Yesterday's table
flagged its sync cursor **frozen at `2026-08-14T07:59:45`** with only **487** rows on 08-14, which put
the very session this desk prices off outside the local store (`D266`). Overnight it un-stalled: cursor
**`2026-08-16T09:01:55`**, **08-14 now holds 7,992 rows**, 08-15 holds 2,938. ⚠ **08-16 holds only 363
and is a partial day in progress — a low count there is not a quiet Sunday.**

⚠ **A right DOWNGRADED today, in the same breath.** The hand-probe warrant fell from **85% → 60%**
success (n=40, seeded draw from the 249 silent names). **The false-silence rate did not move: 0 of 40
again, 0 of 80 cumulative.** So the probe may still be cited — but now **the probe's clock time must be
on the same line as the counts**, because §6a shows a four-minute window can flip the answer.

### 6a. ★ The transport diagnosis inverted for the SECOND time in three runs — and the correct reading is neither "alive" nor "dead"

| Run | CLI path | Library path |
|---|---|---|
| 08-14 | dead | *(not probed)* — concluded *"both bridges are down"* |
| 08-15 | **dead 5/5** | **alive 85%** — refuted "both" |
| **08-16** | **ALIVE 5/5** (Nvidia 3,639 · Broadcom 359 · Eaton 49 · Nucor 17 · Raytheon 9) | **60%** |

The KR desk measured the same thing at finer resolution this morning: CLI alive at 08:41, **dead 51/51
across 08:44–08:50**, alive again at 08:54. ⇒ **The bridge flickers on a timescale of minutes.** Which
transport is up when you look is close to a coin flip, and **a full sweep firing ~600 sequential calls
converges toward zero on a flickering bridge by construction** — which is why coverage reads 16.7%
while a 40-name probe reads 60%.
🚫 **Consequence for every stage: no claim that any transport is dead.** Both prior diagnoses were true
at the minute measured and false four minutes either side. **Transport state may only be written with a
clock time attached.**

### 6b. `D265` acquired a shape this run — the survivor set is NESTED, not resampled

| | 08-14 | 08-15 | **08-16** |
|---|---|---|---|
| Velocity survivors | 51 | 51 | **50** |
| New entrants | — | **0** | **0** |
| Dropouts | — | **0** | **1 — `RTX`** |
| Shared values that moved | — | 48/51 | **48/50** |

**Three runs, zero new entrants, one dropout.** A rate-dependent random failure would resample the set
every run; this set only ever **shrinks**. It is not article volume (`C` returns **201** articles over
7 days and is a non-survivor) and it is not caching (48 of 50 values moved). ⇒ **`D265` upgrades from
"unexplained" to "unexplained, and monotone."** That is a stronger statement than yesterday's and it
makes the survivors **worse** than a random sample, not better. **Still not citable.**

★ **Carried instrument defect that binds every stage: `D261`.** `flow_score` is **3-axis** while
`flow_tag` is **4-axis**, and `§scoring` says nothing about it. On 08-15, **6 of 11 🟢 could not be
produced by `OBV ∧ RS20>0 ∧ vol_surge≥1.2`** and all six carried a velocity value ⇒ the admissible green
count was **5, not 11 = a 3.2× over-representation** of a 17%-coverage survivor sample. **SWEEP must
re-run that decomposition on today's greens before any stage counts a green.**

---

## 7. Method rules loaded as binding constraints (`handoff/RESEARCH.md`)

| Group | Fires when | IDs | Binds today |
|---|---|---|---|
| **C** | you cite a number | C1 baseline · C2 both halves · C3 unknown column · C4 "indistinguishable" · C5 arbitrary choice | **MACRO · every stage.** ★ **C1 binds hard**: every excess return names `SPY` inline. ★ **C5 binds unusually hard today** — with the tape frozen, the temptation is to invent a new metric that *does* move (`risk_units`' own instability sits entirely on an arbitrary 0.65 threshold: at 0.40–0.60 all three windows agree on 12 units) |
| **S** | you make a statistical claim | S1 date-fold · S2 diagnose the null · S3 power first · S4 in-sample≠done · S5 short samples · S6 future labels | **any stage citing a test.** ★ **S1 binds the headline fact**: yesterday's numbers and today's are **one date**, not two — anything counted twice is a date-fold violation. S5 binds `risk_units --days 250` (249 < 250 sessions) |
| **D** | you read data | D1 second venue · D2 proxy sign · D3 signed vs unsigned · D4 regime contamination · D5 cross-provider · **D6 signal grade (OBV is C)** | **SWEEP · ALPHA · DEEP.** ★ **D6 binds hard**: with the velocity axis revoked the score rests on OBV (**C-grade**) + RS + `vol_surge`, so **no DEEP verdict may rest on OBV alone** |
| **W** | you write a conclusion | W1 cross-market transfer · W2 inherited lead/lag · W3 real≠profitable · W4 name the customers · W5 sub-sector dispersion · W6 reader's-market spine | **DEEP · BET · ROTATION.** ★ **W1 binds §8's IC finding.** W5 binds every "sector" statement (`M666` Energy · `M667` Industrials · `M668` COMM · `M669` FIN are all one-label-two-businesses findings) |
| **L** | lenses (not triggers) | L1 second derivative · L2 peak-margin trap · L3 branch information content | **DEEP · PREMORTEM.** L2 currently fires on **`MU` alone** (`M670`: `MPC` sits at its **median** 10.0% vs 10.5%, not its peak) |

---

## 8. The signal scoreboard — and the transfer trap sitting on it

`scripts/ic_ledger.py score` — **21 tests · 421 ledger rows · KR universe**

| Axis | h | n | n_eff | mean IC | t(NW) | Verdict |
|---|---|---|---|---|---|---|
| **`vol_surge`** | **1** | 27 | **27.0** | **−0.0479** | **−3.30** | ★ **significant, clears Bonferroni (\|t\|>2.8)** |
| **`vol_surge`** | **5** | 22 | **4.4** | **−0.0438** | **−3.14** | ★ **significant, clears Bonferroni** |
| `obv_norm` | 5 | 22 | 4.4 | −0.0739 | −1.78 | indistinguishable |
| `rs60` | 5 | 21 | 4.2 | −0.1485 | −1.58 | indistinguishable |
| `flow_score` | 5 | 22 | 4.4 | −0.0853 | −1.37 | indistinguishable |
| *(14 of 21 cells)* | | | **< 4** | | | 🚨 **unquotable — overlapping windows** |

★ **The standing item, stronger again**: `vol_surge` is the **only** axis with a consistent sign across
two horizons and it clears Bonferroni on **both**, with a **NEGATIVE** sign — a high volume surge
predicted **lower** forward returns. **`sector_flow` still weights it positively**, and it is the axis
that decides the 🟢 gate. ⚠ Note the sample grew by exactly one run (n 26→27) while **this desk observed
zero sessions** — the ledger is KR-keyed and the KR desk ran this morning.

🚨 **The trap, stated before anyone reaches for it: this ledger is KR.** **`W1` forbids importing a
cross-market conclusion**, and this desk logs W1 violations as its most common failure. `D243` records
that **the US desk has no IC column at all**. ⇒ The correct statement today is: *"the US `vol_surge`
weighting is **unmeasured**, and the only market where it has been measured says the sign is backwards."*
**That is a dig, not a gate flip. No stage flips the gate today.**
★ This is exactly the reasoning the protocol itself uses to keep **DEEP N=4 for US** while KR cut to
N=2 — importing a conclusion across markets is the W1 violation this repo keeps logging.

---

## 9. Reconciliation — belief vs coverage (`module_report_tags show`)

Ledger: **68 reports · 273 names · 12 sectors**, refreshed **2026-08-16T09:56** (by the KR run).

⚠ **Reconciliation delta, carried for a second run and now measurably worse.** Most `industry_US`
entries in the ledger point at **flat** files (`industry_US/SWEEP_READ.md`), while several point at
**dated subfolders** (`industry_US/2026-08-13/…`, `industry_US/2026-08-14/…`). The two shapes coexist,
so the ledger's "most recent report" column is not a reliable recency signal for US names.
**This run copies its finalized reports to the flat path** per the protocol's resolved open decision.

**Beliefs with heavy coverage and no standing thesis** (candidate DEEP, unchanged): `EW` (22 reports),
`NEM` (17), `VLO` (16), `CL` (10), `MRVL` (9), `CVX` (9).
**Standing theses whose ledger coverage is thin**: the tanker block (`STNG`·`FRO`·`INSW`·`DHT`·`TNK`)
— still **outside `us_top300`**, so the desk cannot tag them at all; `HII` likewise (`M667` / EVENT_ALPHA
Card 1, 08-15).
⚠ **`M152` still binds this section**: **28 real tickers are silently unindexable** by the ledger's
`_US_STOP` guard (`A · AIG · ALL · C · CAT · CB · COST · D · F · FAST · GS · ICE · KR · LOW · MA · MET ·
MS · NOW · O · ON · PEG · PM · Q · SO · T · TT · V · WELL`). **A zero in the ledger for any of those 28
means "blocked", not "uncovered"** — do not build a coverage-gap argument on them.

---

## 10. Dig list, ranked for this run (`RESEARCH.md` Part C · highest existing ID **D270** un-suffixed, **D256-KR** suffixed)

| Rank | Dig | Why it is today's |
|---|---|---|
| **1** | **`D249`** — the INDU bracket measures `XLI` while the position is **defense** | **Unresolved for a 5th run.** INDU is a continuous OW− slot; the desk cannot keep holding a tilt whose falsifier measures a different object |
| **2** | **`D261`** — tag/score axis mismatch (3-axis score vs 4-axis tag) | **Binds every green count.** SWEEP must decompose today's greens before ROTATION counts one. Worsened 08-15 (3.2× over-representation, up from 2.6×) |
| **3** | **`D270`** — "breadth 0.00" this week is a statement about **VOLUME**, not demand | ★ **Directly answerable today with no new data.** The whole tape is thin (0.732 then 0.649 of the 20-day norm) so the `vol_surge` denominator carries a busier past and the gate closes board-wide at once. **`M144` replicated a 6th time at record size: 110 pass `OBV ∧ RS20>0`, 100 blocked, 100.0% of them on `vol_surge` alone** |
| **4** | **`D243`** — the US desk has **no IC column** | §8 shows exactly what its absence costs: the desk cannot say whether its own gate axis has a sign in its own market |
| **5** | **`D250`** — `cycle_registry.json` **29 days stale**, rank-3 floor `0.0` ⇒ check **OFF**; no entry for either live cycle (optical/interconnect, custom AI silicon) | PREMORTEM Lens 4 runs on a registry with no row for the two cycles owning the desk's best-scoring names |
| **6** | **`D264`** — a pool-normalised burst check can still return a **false all-clear** | **Binds DRIFT directly**, though the client store un-stalled today (§6) so the routing option improved |
| **7** | **`R56` / `EA`** — delisted 08-04, still in `us_top300` at day **32**, now dropped out of the scored set | **9th consecutive run.** The defect **changed shape** (it is now a composition change in COMM, not a phantom score) and should be re-stated, not re-copied |

**New digs from this stage → `D276` onward.**
🚨 **ID COLLISION CAUGHT AND CORRECTED AT RUN END — written down, not edited away (§4c).** This stage
first allocated **`D271`–`D273`** on a 3-grep that read *"highest existing D270 un-suffixed."* **A
re-grep at writeback time found `D271` · `D272` · `D273` · `D274` · `D275` ALL already registered** —
by the 08-15 `industry_US` run and the 08-16 `industry_kr` run, which this stage's first grep pattern
missed because it only matched table-cell form. **The three digs below are therefore `D276`–`D278`.**
⇒ This is the **`D76` collision class** reproducing on the dig namespace rather than the scenario
namespace, and it argues that **ID allocation should be a script, not a grep** — itself now a dig.

| ID | Dig | Owner |
|---|---|---|
| **D276** | ★★ **The news bridge FLICKERS on a minute timescale, and a sequential full sweep converges to ~0 on it by construction.** Measured across three runs and two desks: CLI dead 5/5 (08-15) then alive 5/5 (08-16); KR measured alive→dead 51/51→alive inside **13 minutes**. A ~600-call sequential sweep reads **16.7%** while an 80-call probe reads **60%**. **Positive-form remedy: give `news_velocity` a bounded retry with backoff and log per-call outcome, then re-measure coverage — the current number measures the transport's duty cycle, not the corpus** | **human** (transport) · **idle_probe** (characterise) |
| **D277** | ★★ **`D265` upgraded: the survivor set is MONOTONE-NESTING (51 → 51 → 50, zero entrants ever).** Combined with `D271`, a pure rate failure is excluded — a flickering transport resamples, it does not nest. **Positive-form remedy: log the ticker order and elapsed time per call inside `sector_flow`; if the survivors are the first-N in iteration order, the mechanism is a session/token that dies partway and the fix is per-call, not per-run** | **idle_probe** · **PREFLIGHT** (keep reporting the set-identity check) |
| **D278** | ★ **A weekend run pair produces two reports off ONE observation, and nothing in the pipeline marks the duplication.** `history.json` was overwritten at key `2026-08-14` by both the 08-15 and 08-16 runs; `SECTOR_FLOW_US.json`, `RISK_UNITS`, `margin_history` and `module_chart` all returned byte-identical output. Downstream key-indexed consumers (`ic_ledger`, `axis_inflection`, `reject_ledger`) cannot tell one observation from two. **Positive-form remedy: stamp `n_new_sessions_since_prior_run` into `§scoring` so a consumer can weight a replay as zero** | **PREFLIGHT** (report it) · **human** (whether the desk should run at all on a second non-session day) |

★ **`D266` is CLOSED this run** — the client store's sync cursor un-stalled on its own (frozen
`2026-08-14T07:59` / 487 rows → `2026-08-16T09:01` / 7,992 rows). Recorded as closed by observation, not
by repair; the underlying "a frozen sync looks like a live file" reporting gap is **not** fixed, so the
remedy half of `D266` is carried into `D276`'s owner queue.

---

## 11. §4c — verification that arrived after the assertion (D48 class)

**This stage's own count: 2.**

1. 🚨 **This stage nearly inherited the phrase "the CLI path is dead."** Yesterday's rights table
   measured it dead 5/5 and this stage was drafting that forward as today's constraint. **The PREFLIGHT
   probe run minutes earlier refuted it: 5/5 alive.** ⇒ **The inherited sentence was not wrong when
   written; it was wrong to carry.** Written here rather than edited into §6, per §4c. The correct
   generalisation is stronger than either version and is now `D271`: *neither "alive" nor "dead" is a
   property of that bridge.*
2. 🚨 **This stage drafted "the survivor set is identical three runs running" and its own diff refuted
   the word `identical`.** The 08-16 set is **50, not 51** — `RTX` dropped out. The corrected claim
   (**nested, monotone**) is *more* informative than the one it replaced, which is why the refutation
   was worth running rather than the assertion worth defending.

⚠ **Stated plainly**: two self-refutations in a stage that ran three independent probes is a
**reasonable** count, not a good one. Per §4c a *zero* usually means the controls were not adversarial.
The stages below should assume this stage under-tested itself rather than that it was clean —
**especially today, when the frozen tape removes the cheapest source of contradiction.**

---

## ✅ EXIT CHECK

- [x] **Shared spines read** — `STANDING_VIEW.md` (regime call §1, measured chain §2, §3a per-name
      registry, §4 asymmetry, §5 retracted ledger, §6 open contradictions) + `SCENARIOS.md` (MASTER
      scoring log **including the 08-16 KR entries**, MASTER INDEX) + this desk's `STANDING_VIEW_US.md`
      + `SCENARIOS_US.md` + `RESEARCH.md` (loaded as the C/S/D/W/L trigger groups in §7). **The other
      market's file WAS opened** — `SCENARIOS_KR.md` — and confirmed to hold **no past-dated row this
      run must score** (nearest `S51-KR` → 08-17).
      🚨 **Budget breach reported, not silently absorbed** (`handoff_compact --budget-only`): a US run
      reads **1,550.7 KB against a 250 KB budget = 1,301 KB over**; `STANDING_VIEW.md` 347.9 KB (budget
      45) · `SCENARIOS_US.md` 280.0 KB (budget 50) · `RESEARCH.md` 441.3 KB (budget 85). §2 fact rows =
      **778 at 0.51 KB/row against a 0.35 limit.** The cause is visible in the file's own headings —
      **per-run `## Added by the …` append blocks**, exactly what the 07-25 rule forbade. **This is a
      finding for a human (P5), and it is why this stage read the spines by section rather than
      end-to-end; that limitation is stated rather than hidden.**
- [x] **Retracted ledger read BEFORE forming any view.** `R69` (the `M40` Financials-breadth reversal)
      is the live one; `R56`/`EA` is carried as an **open defect, not a belief**. No claim above
      resurrects a retracted entry. ★ `R69`'s scope: it withdrew *"the board's only breadth-led sector"*
      as a property **of Financials**; it did **not** assert Financials has no breadth (`M669` relocated
      it to alternatives/asset-management, and `KKR` is that node).
- [x] **Every past-dated scenario scored or `EXPIRED` with a reason.** **Zero matured**; `EXPIRED = 0`;
      silent skips = 0. The null result is recorded as a **check performed**, with the mechanical reason
      (no session settled). `S8` named for the **14th** run.
- [x] **`reject_ledger.py due` run** — 0 due, **legacy 0**, 176 total / 90 resolved.
- [x] **`missed_ledger.py due` run** — 0 due, **legacy 0**, 134 total / 51 resolved. Sign inversion
      stated; the two are not summed.
- [x] **Exposure state read and carried** (§5) — verdict `정상`, target 95%, **invested % 🚨 unknown and
      NOT substituted**, cumulative **−14.21pp = cash −6.26 + selection −7.95 on n=8**. Not a cold start
      (35 rows). `밴드미설정` not triggered.
- [x] 🚨 **Instrument health inherited before any number was trusted** — `PREFLIGHT_US.md` read; the
      binding table is §6. It revokes **six** things (one of them new and board-wide: the word "today"
      on any price-derived change) and restores **one** (`news_vectors.db` through 08-15).
- [x] **Claims asserted and then refuted are written down, not edited away** — §11, two instances.
- [x] **Stale rows flagged with their `asof`** — `us_top300.csv` **32 days** · `cycle_registry.json`
      **29 days** (rank-3 floor 0.0 ⇒ check OFF) · `data/news_fts*.db` **0 bytes** (4 days) ·
      `handoff/` **1,301 KB over budget**. No suspension cleared this run, so none converted to a dig.
- [x] **`[measured]` / `[inferred]` tags preserved.** The regime call and `P56` travel as `[inferred]`
      and are not usable as evidence.
- [x] **RESEARCH triggers loaded as binding constraints**, grouped C/S/D/W + L (§7), with the stage each
      group binds named.
- [x] **No position sizing, no buy/sell language anywhere in this file** (P4).
- [ ] `handoff/*.md` writeback — **deferred to run end** (append-only for retractions), per the stage's
      own instruction.
