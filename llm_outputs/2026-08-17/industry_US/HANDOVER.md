# HANDOVER — industry_US · 2026-08-17 (Mon KST) · Stage 2/11 (L1·HANDOVER)

> Inheritance only. No sizing, no buy/sell language (P4). This stage transports what the desk already
> believes, scores what has matured, and states what today's instruments forbid.

## 0. Run clock — and the two structural facts that govern everything below

| | |
|---|---|
| Run clock | **KST 2026-08-17 22:10– = ET 2026-08-17 09:10– — MONDAY, US cash PRE-MARKET** |
| Price asof | **2026-08-14 settled close** (Friday) |
| Δ baseline | `history.json["2026-08-13"]`, same 3-axis mode ⇒ Δ = 08-13 → 08-14 |
| ★ **Sessions observed since the prior run** | **ZERO — for the fourth consecutive run** |
| ★★ **Regular session opens** | **09:30 ET = 22:30 KST — twenty minutes after the sweep finished, i.e. DURING this run** |

**Fact 1 — the tape is still frozen, and this is the fourth reading of one Friday.** The 08-15 (Sat),
08-16 (Sun) and this run all price off the **08-14** close. Measured, not assumed: **all 299
`flow_score` values are identical to the 08-16 run** — zero differing names — and the universe
aggregate is identical (`n=299 · wflow −0.132 · 9 green / 60 red`). ⇒ **Agreement between this run and
the last three is evidence that one input was read four times.** It is not persistence, confirmation,
stability, or a "fourth consecutive" anything.

**Fact 2 — and this run is the last one that can say that.** The 08-17 session settles tonight at
16:00 ET (05:00 KST 08-18). The next `industry_US` run inherits **one genuinely new session** and the
first non-replay Δ since 08-14. Two consequences bind *this* run: **(a)** no stage may re-pull prices
after 22:30 KST and compare the result to this sweep — that would mix a live partial bar into a settled
frame (PREFLIGHT G0); **(b)** any verdict this run leaves standing will be tested against real data
tomorrow, which is an argument for stating falsifiers sharply now rather than for thrashing on unchanged
numbers.

★ **What "frozen" does NOT mean.** Three axes are not keyed to the equity session and can have moved:
`[FRED]` macro series, the **news corpus**, and **primary filings**. That is where this run's only new
information can come from. The 08-16 run proved the point at its own expense — it retracted its live
macro object (`R73`) using **a re-measurement of an existing `[FRED]` pull, with no new data at all**.

---

## 1. Inherited regime call — carried verbatim, tag intact

> **Memory is a price-cycle industry in rate-of-change deceleration while its level stays tight.**
> `[inferred]` — built on the measured chain `M1`–`M9`, `M18`, `M143`.

In a commodity-cycle industry the equity tracks the **second derivative of price**, not the level.
Level and rate point opposite ways, which is why "shortage persists" and "the stocks struggle" are both
true and not contradictory.

⚠ **`[inferred]` may be carried; it may not be cited as evidence** for a new proposition. Any stage
leaning on the regime call must name the measured row underneath it, not the call.

**The live macro object, as amended 08-16 — carry the amendment, not the original.**
`P56` ("the long end is repricing **term premium**") was **half-retracted by `R73`**. What survives:
the **spread** (30y−10y **0.53 → 0.58** over 08-06 → 08-13, a 5th consecutive widening) and `P56`'s
**sign**. What is withdrawn: the **front-end clause** — `DGS2` fell 10bp (4.25 → 4.15) and `DGS30`
itself *fell* (5.22 → 5.21), so the correct shape is a **bull steepener**, not a level rise. `P65`
replaces the mechanism.
🚨 **This binds the three-legged duration underweight (UTIL · RE · STPL) directly** — the mechanism
under it was the front-end clause. `S80` settles **08-19** and must now be read as a **three-sector**
event. **Any stage carrying that bundle today must carry `P65`, not `P56`'s original text.**
★ **MACRO's first job: `[FRED]` is again the one instrument that could have moved**, and it is the only
place `P65` is testable this run. The tape is not.

---

## 2. Sector verdict board inherited from 2026-08-16 (unchanged until ROTATION acts)

| Sector | Verdict | Carried because |
|---|---|---|
| **ENRG** | **OW** | Promoted 08-15 on `eqflow +0.102` / `breadth 0.12`, both the highest of eleven. ⚠ **`M707` is the counterweight and it is measured**: the refining trio ripped **+14…19% in five sessions** with **no OBV confirmation and a bearish RSI divergence**. `S88` (08-21) is registered at the **100th percentile of two years** — its branch B was declared NO-INFORMATION at registration |
| **INDU** | **OW−** | ★ **`D249` CLOSED 08-16 by measurement** after 5 runs: `XLI` vs defense EW gives a **7.652pp sign-inverting spread on 20d** (−0.489 vs +7.163). The bracket really did measure a different object. `M708`'s Industrials decomposition shows **three businesses in one GICS code** (defense +7.163 · electricals ≈+5.7 · machinery ≈−2.4) |
| **IT** | **N+** | Held 08-15 with the basis decayed 95% (Δ +0.152 → +0.007). N+ rests on `eqflow +0.044 > wflow +0.023` **alone**. Falsifier `S85` settles **08-21**, and it already sits at **+1.343 = branch C** |
| **HLTH** | **N** | Promotion to N+ declined 08-15 — Δ **−0.103 = worst of eleven**. `S82` settles 08-20, **already above branch A at +3.091** at registration |
| **FIN** | **N−** | `M40`'s inversion has not repaired (`eqflow −0.126` below `wflow −0.031`); `R69` stands. `M669`'s relocated breadth node is `KKR` (fwd 15.43× on PEG 0.59) |
| **MATR** | **N−** | Flipper (`LIN` 24.7%) ⇒ `wflow` inadmissible; every permitted axis refuses |
| **DISC** | **N−** | Demote to UW declined 08-15 — Δ **+0.038** is the wrong direction. `S93` settles 08-21 |
| **COMM** | **UW** | Both directions blocked, and the bucket changed membership (`EA` out of the scored set) |
| **STPL** | **UW−** | Declined **on notation** for a 2nd run — UW− is this board's floor. `TGT` is the sheet's cleanest unowned accumulation inside it (**33.6pp** intra-Staples spread vs `WMT`/`COST`) |
| **UTIL** | **UW** | The board's **only real (non-`vol_surge`-artifact) flow absence**: 0 of 15 pass `OBV ∧ RS20>0`, i.e. the block happens **before** `vol_surge`. ⚠ But `R73`/`P65` make the rate leg a **tailwind**, and the 5-day bounce sits in the **merchant** leg (`VST` `CEG` `GEV`), not the regulated leg |
| **RE** | **UW** | Most internally consistent verdict — but **4 of 12 accumulate** (`EQIX` `DLR` `CBRE` `IRM` = `M131`'s data-centre unit). `S90` settles 08-21 |

**Last DEEP:** CONSUMER 08-16 · ENRG 08-16 · INDU 08-16 · IT 08-16 · UTIL 08-16 · DISC 08-15 ·
RE 08-15 · COMM 08-14 · FIN 08-14 · HLTH 08-13 · MATR 08-13.
⇒ **Recency-ranked candidates for today's rotating slots: MATR / HLTH (4 runs) · FIN / COMM (3 runs).**
ROTATION owns the decision; this stage only reports the clock.

⚠ **The structural warning, stated for a fourth run and now with a deadline.** With zero new sessions,
**every flow input to a verdict change is byte-identical to the one that produced yesterday's verdicts.**
A verdict delta today would have to be justified by something other than flow — a new `[FRED]` print, a
new filing, or an error found in the prior run's reasoning. ★ **And there is a cheap alternative to
thrash available today**: tomorrow's run gets real data, so the highest-value output of this run is a
**sharper falsifier**, not a re-ranked board.

---

## 3. Scenario status — **EXPIRED = 0 · silent skips = 0**

### 3a. Matured this run — the cross-desk check produced a NON-null result today
**Zero US-owned rows past-dated.** `SCENARIOS_US.md` opened in full: nearest settlements are **08-19**
(`S75` `S76` `S77` `S78` `S80`), **08-20** (`S82` `S83`), **08-21** (`S84`–`S91`, `S93`), **08-24**
(`S74`), **08-26/27** (`S79` `S81`), **08-31** (`S92` `S94`).

★ **`SCENARIOS_KR.md` was opened because a past-dated row in the other market's file is still this run's
to score — and today, for the first time in four runs, there was one.** `S51-KR` was dated **2026-08-17
= today**, and **this morning's `industry_kr` run scored it `FIRED-C`** before this desk reached it.
⇒ **Not this run's to score; verified settled rather than assumed.** For three runs the null result here
was mechanical ("no window could close"); today the check had a live row in it and returned a real
answer, which is the first evidence that the cross-desk rule does something.

**What `S51-KR` bought, and why this desk should carry it (it is a method finding, not a KR fact).**
The bracket pre-committed to re-checking a news-body number against the primary filing. Result: the
**denominator** reproduced to **0.0041%**, and the **numerator did not exist in the filing at all**
(「재고관련」 appears **0 times in 3,977,008 characters**). ⇒ **The operative rule is not "news bodies
are unreliable" but "ask first whether the number exists in the filing at all."** ⚠ **W1 applies**: this
is a *method* transfer, not a market conclusion, and it is carried as such. `R75` records the retraction.

**Remaining KR ARMED, none past-dated**: `S52-KR` 08-19 · `S57-KR`/`S63-KR` 08-20 · `S27` ~late-Aug ·
`S58-KR` 09-09 · `S61-KR` ~09-14 · `S62-KR` 09-15 · `S45`/`S54-KR` 09-30 · `S60-KR` 10-12 ·
`S49-KR` 10-30 · `S34`/`S53-KR` 10-31 · `S59-KR` 11-04.

### 3b. 🚨🚨 `S8` — undated, un-scoreable, **FIFTEENTH consecutive run**
`S8` remains `[blank]`-dated and cannot be settled by any desk. **A human must `VOID` it or re-register
it with a date (P5).** ⚠ Its observable is still live and still undated: `CATALYST_WATCH` (pulled
22:1x KST today) again carries *"Iran 'Strait of Hormuz open' statement (TACO trigger)"* as an
**undated 🔀binary**. **Named again, not dropped.**

### 3c. Binary catalysts in window — what PREMORTEM inherits
`catalyst_calendar --days 10`, run this stage: **2 binaries flagged.**

| Catalyst | Date | Note |
|---|---|---|
| `NVDA` earnings | **2026-08-26 (D-9)** | 🔀binary. **Not ≤48h**, so the protocol's mandatory both-sides trigger does **not** fire on it today. Already bracketed by `S79` (08-27) and `S81` (readthrough) |
| Iran "Strait of Hormuz open" statement | **undated** | 🔀binary, `[news👁]`. Bracketed by `S74` (08-24), `S84` (08-21) and `S92` (08-31) |

⇒ **No dated binary sits inside 48 hours of this run.** PREMORTEM's mandatory bracket clause is
therefore not triggered by the calendar — but `S8`'s undated row means the desk has an *un-dated* binary
it has failed to date for fifteen runs, which PREMORTEM should treat as the live blind spot rather than
as a satisfied condition.
⚠ **`D259-KR` binds this pull**: the calendar does not read `SCENARIOS`' armed dates, so a `--days 10`
window that shows "2 binaries" is **not** the same as "2 things settle in ten days" — **eight US rows
settle inside this window** (`S75`–`S78`, `S80`, `S82`, `S83`, `S84`–`S91`, `S93`) and the calendar
knows about none of them.

---

## 4. Both ledgers audited — clean, and clean for the right reason

| Ledger | Total | Resolved | **Legacy (no revival/entry condition)** | **Due now** |
|---|---|---|---|---|
| `reject_ledger` | **182** (+6 vs 08-16) | 91 | **0** | **0** |
| `missed_ledger` | **138** (+4 vs 08-16) | 56 | **0** | **0** |

★ **The legacy count is the number that matters and it is 0 on both sides, for a fourth run.** This
desk's most expensive measured error (`SK이터닉스`, **+41.2pp and +26.9pp**) happened because 24 of 25
rows carried no `revives_if` at all, so "any row whose condition has come true" was unstatable.
⚠ **A clean `due` is not evidence of health on its own.** It is evidence here only because **both**
conditions hold: legacy = 0 **and** the totals are still growing (176→182, 134→138). Report them
together, every run.
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
| Ledger rows | **35** (unchanged — no session accrued) |
| Cumulative decomposition (n=8) | **total excess −14.31pp = cash −6.33pp + selection −7.98pp** |
| Last measured band gap | **−27.1pp** (08-14, settled row) |

🚨 **Reported as unknown, not substituted** (P5). The state machine is **not** cold-starting (35 rows),
so the `정상` verdict is usable; the **invested %** is not.
★ **The line BET/ALPHA must carry**: over the accrued window the desk is behind on **both** legs — cash
weight −6.33pp *and* selection −7.98pp — so *"we were defensively positioned"* does not explain the
shortfall. ⚠ **n=8**, and it did not grow this run (no session). At this n the split is
**indistinguishable from zero (C4)**; it is reported to make the n grow, not to be acted on.
⚠ Standing alarm on every row: **`TIMEFOLIO_EXECUTE=1` is ARMED**. Analytical desks never pass
`--execute`; this run does not.

---

## 6. Instrument health inherited from PREFLIGHT — **the binding table**

Read `llm_outputs/2026-08-17/preflight/PREFLIGHT_US.md` (written **before** this stage). **PASS 3 /
FAIL 5.** The gate table is a rights table, and these are the rights:

| Stage | 🚫 Cannot use today |
|---|---|
| **ALL** | ★ **any Δ or comparison written as "today", "the latest session", "now accelerating"** — zero new sessions · **agreement with the prior three reports cited as confirmation** · ★★ **any statement that this run reflects Monday 08-17 trading** — the bell rings *after* the sweep |
| SWEEP | the sweep's velocity axis · **the 51 survivors** · theme freshness · "quiet" · **33-day-stale caps described as current** · any verdict on `EA` · ★ **`breadth` as a news-independent reading** |
| EVENT_ALPHA | "theme is fresh/cooled" from an **empty** `theme_age`/`chain_hop` result · `news_vectors.db` **after 2026-08-16** (08-17 is a partial 567-row day) |
| ROTATION | **`wflow` promotion/demotion for IT · Industrials · Materials** (G3 flippers) · ★ **`breadth`-change tie-breaks — use `eqflow`** · "the fourth run running" as a persistence argument |
| PREMORTEM | "the tape has gone quiet on this risk" — **measured: 0 of 120 silent names were quiet, across three runs** |
| DEEP | the velocity axis as an axis · "no news flow" as evidence |
| BET/SIZE | single-number concentration · `--ic`-backed size (→ **"mechanical ¼"**) · `AVGO/NVDA` and `ANET/ETN` unit counts |
| DRIFT | **must state whether its instrument answered, with the probe clock time.** An empty burst list is not "no drift" |

**✅ What is available, stated positively.** Settled prices through **08-14** with fine-grain RS (G0
clean, **5th** run) · OBV · **`eqflow`** · `vol_surge` **both directions** · FINRA short pressure · CFTC
COT percentiles · `[FRED]` · primary filings · `margin_history` · **per-name news velocity by hand
probe** · `news_vectors.db` through **08-16**.

### 6a. ★ The probe hit 100% — the best reading in five runs, and it relocates the defect

| Run | CLI path | Library path on the sweep's "silent" names | False silence |
|---|---|---|---|
| 08-14 | dead | *(not probed)* | — |
| 08-15 | dead 5/5 | **85%** | **0 of 40** |
| 08-16 | **alive 5/5** | 60% | **0 of 40** |
| **08-17** | **alive 5/5** (22:13:55) | ★ **100% — 40/40 valid, 0 pipe-fail, in 18.5 s** (22:14:12–22:14:30) | **0 of 40** |

**Cumulative: 0 of 120 names the sweep called silent were actually quiet.** The success *rate* has been
85% → 60% → 100%; the *false-silence rate* is stably **zero**.

★ **The reading this makes possible.** Standalone probing returned **100%** twenty minutes *after* the
full sweep recorded those exact names as silent at **17.1%** coverage. That is not a dead bridge and not
a flickering one — **the failure attaches to the full-universe sweep as a usage pattern.** The KR desk
measured the identical split this morning on its own corpus (**5.9% swept vs 100% standalone**, with the
48 successes spread evenly across the whole processing order, mean gap ≈17). **Two desks, two universes,
one shape, same calendar day.**
⚠ **This supersedes `D276`'s "flicker" framing** — a flickering transport would have failed some of
tonight's 80 sequential probe requests, and it failed none. `D276` is not retracted (its measurements
stand); its **diagnosis** is narrowed and the narrowing is recorded in §11.

### 6b. `D277` FALSIFIED — the survivor set is not monotone

| | 08-14 | 08-15 | 08-16 | **08-17** |
|---|---|---|---|---|
| Velocity survivors | 51 | 51 | 50 | **51** |
| New entrants | — | 0 | 0 | **1 — `RTX` (re-entered)** |
| Dropouts | — | 0 | 1 (`RTX`) | **0** |
| Shared values that moved | — | 48/51 | 48/50 | **41/50** |

Yesterday's run registered `D277` on the claim that the set **only ever shrinks** ("zero entrants,
ever"). **`RTX` came back today.** ⇒ **The monotone half of `D277` is dead after one run.** What
survives and is still unexplained: a **stable ~50-name core plus a flickering edge**, selected by a
mechanism that is **not** article volume (`C` returns **201** articles over 7 days and has never been a
survivor) and **not** caching (41 of 50 values moved). **Still not citable.**

### 6c. ★ `D261` reproduced in the US market, on `breadth` specifically

**Measured today:** all 299 `flow_score` values identical to 08-16 — and the sector table is **not**
identical. `Financials` breadth **0.04 → 0.06**, `Communication Services` breadth **0.08 → 0.00**.
Cause: `sector_flow.py:224` computes `tag = flow_read.flow_tag(p, vel)` — the 🟢/🟡/🔴 label consumes
**raw velocity**, outside the axis-drop guard that protects `flow_score`; `breadth` is then
`greens / len(names)` over that tag (`sector_flow.py:342`). Two names moved on zero new prices:

| Name | 08-16 tag | 08-17 tag | velocity | flow_score |
|---|---|---|---|---|
| `NFLX` | 🟢가속 | **🟡중립** | 1.23 → **1.17** | **unchanged** |
| `MA` | 🟡중립 | **🟢가속** | 1.17 → **1.29** | **unchanged** |

⇒ **Two sector breadth readings moved on instrument flicker.** The universe totals cancel (9 green /
60 red both runs), which is exactly why this survived four runs unnoticed — the aggregate is stable
while the per-sector numbers are not.
⚠ **This binds ROTATION hard**, because `breadth` was the axis that carried the **ENRG promotion**
(`breadth 0.12`) and it is quoted alongside IT's N+ (`breadth 0.05`). Those are *level* readings inside
one run, which remains permitted; what is now forbidden is **reading a breadth CHANGE between runs as a
market change**.

---

## 7. Method rules loaded as binding constraints (`handoff/RESEARCH.md`)

| Group | Fires when | IDs | Binds today |
|---|---|---|---|
| **C** | you cite a number | C1 baseline · C2 both halves · C3 unknown column · C4 "indistinguishable" · C5 arbitrary choice | **MACRO · every stage.** ★ **C1 binds hardest today**: `R73` is the third logged instance of a carried sentence measured on an old window and never re-measured — and it was caught on a frozen tape. ★ **C5**: `risk_units`' whole instability sits on an arbitrary 0.65 threshold (at 0.40–0.60 all three windows agree on **12** units) |
| **S** | you make a statistical claim | S1 date-fold · S2 diagnose the null · S3 power first · S4 in-sample≠done · S5 short samples · S6 future labels | **any stage citing a test.** ★ **S1 binds the headline**: four runs' numbers are **one date**. S5 binds `risk_units --days 250` (249 < 250 sessions) |
| **D** | you read data | D1 second venue · D2 proxy sign · D3 signed vs unsigned · D4 regime contamination · D5 cross-provider · **D6 signal grade (OBV is C)** | **SWEEP · ALPHA · DEEP.** ★ **D6 binds hard**: with velocity revoked the score rests on OBV (**C-grade**) + RS + `vol_surge` ⇒ **no DEEP verdict may rest on OBV alone.** ★ **New D-trigger inherited from the KR desk 08-17**: *before comparing a news-body number to a filing, ask whether the number exists in the filing at all* (`S51-KR`, 0.0041% where it does / undefined where it does not) |
| **W** | you write a conclusion | W1 cross-market transfer · W2 inherited lead/lag · W3 real≠profitable · W4 name the customers · W5 sub-sector dispersion · W6 reader's-market spine | **DEEP · BET · ROTATION.** ★ **W1 binds §8 and §3a**: the IC ledger is **KR**, and the `S51-KR` finding is carried as a *method*, never as a market fact. W5 binds every "sector" statement — `M708`'s Industrials split (**10.6pp** across three sub-objects in one GICS code) is this run's live example |
| **L** | lenses (not triggers) | L1 second derivative · L2 peak-margin trap · L3 branch information content | **DEEP · PREMORTEM.** L2 does **not** fire on `MPC` (`M670`/`M707`: GM **10.0% vs its own 8-yr median 10.5%**), and the reason it might later is stated: **the crack sits at the 95.2nd %ile of 250d and is not yet in the margin series** |

---

## 8. The signal scoreboard — and the transfer trap sitting on it

`scripts/ic_ledger.py score` — **21 tests · 421 ledger rows · KR universe** (unchanged: no new observation)

| Axis | h | n | n_eff | mean IC | t(NW) | Verdict |
|---|---|---|---|---|---|---|
| **`vol_surge`** | **1** | 27 | **27.0** | **−0.0479** | **−3.30** | ★ **significant, clears Bonferroni (\|t\|>2.8)** |
| **`vol_surge`** | **5** | 22 | **4.4** | **−0.0438** | **−3.14** | ★ **significant, clears Bonferroni** |
| `obv_norm` | 5 | 22 | 4.4 | −0.0739 | −1.78 | indistinguishable |
| `rs60` | 5 | 21 | 4.2 | −0.1485 | −1.58 | indistinguishable |
| `flow_score` | 5 | 22 | 4.4 | −0.0853 | −1.37 | indistinguishable |
| *(14 of 21 cells)* | | | **< 4** | | | 🚨 **unquotable — overlapping windows** |

★ **The standing item**: `vol_surge` is the **only** axis with a consistent sign across two horizons and
it clears Bonferroni on **both**, with a **NEGATIVE** sign — a high volume surge predicted **lower**
forward returns. **`sector_flow` still weights it positively**, and it is the axis that decides the 🟢
gate. ⚠ The row count did **not** grow this run (421 both days) — the KR desk ran this morning but
scored a scenario rather than accruing a ranking observation.

🚨 **The trap, stated before anyone reaches for it: this ledger is KR.** `W1` forbids importing a
cross-market conclusion, and this desk logs W1 violations as its most common failure. `D243` records
that **the US desk has no IC column at all**. ⇒ The correct statement today is: *"the US `vol_surge`
weighting is **unmeasured**, and the only market where it has been measured says the sign is backwards."*
**That is a dig, not a gate flip. No stage flips the gate today.**
★ This is the same reasoning the protocol uses to keep **DEEP N=4 for US** while KR cut to N=2.

---

## 9. Reconciliation — belief vs coverage (`module_report_tags show`)

Ledger scanned this stage. ⚠ **Reconciliation delta, carried for a third run**: most `industry_US`
entries point at **flat** files (`industry_US/SWEEP_READ.md`) while several point at **dated
subfolders**, so the ledger's "most recent report" column is not a reliable recency signal for US names.
**This run copies its finalized reports to the flat path** per the protocol's resolved open decision.

**Heavy coverage, no standing thesis** (candidate DEEP, unchanged): `EW` (22 reports), `NEM` (17),
`VLO` (16), `CL` (10), `MRVL` (9), `CVX` (9).
**Standing theses whose ledger coverage is thin**: the tanker block (`STNG`·`FRO`·`INSW`·`DHT`·`TNK`)
— still **outside `us_top300`**, so the desk cannot tag them at all; `HII` likewise (`D274`).
⚠ **`M152` still binds this section**: **28 real tickers are silently unindexable** by the ledger's
`_US_STOP` guard (`A · AIG · ALL · C · CAT · CB · COST · D · F · FAST · GS · ICE · KR · LOW · MA · MET ·
MS · NOW · O · ON · PEG · PM · Q · SO · T · TT · V · WELL`). **A zero for any of those 28 means
"blocked", not "uncovered"** — no coverage-gap argument may be built on them. ★ Note `MA` is on that
list and is one of the two names whose tag moved in §6c: the desk cannot cross-check it in the ledger.

---

## 10. Dig list, ranked for this run

`RESEARCH.md` Part C · **highest existing un-suffixed ID = `D278`** (allocated by the 08-16 US run) ·
**highest suffixed = `D274-KR`** (allocated by this morning's KR run). **New digs from this run →
`D279` onward.** *(ID check run at read time; it will be re-run at writeback — the 08-16 run recorded a
collision caused by trusting a single grep, and that lesson is applied rather than restated.)*

| Rank | Dig | Why it is today's |
|---|---|---|
| **1** | **`D261`** — tag/score axis mismatch (3-axis score, 4-axis tag) | ★ **Now reproduced in BOTH markets** (`M701` US 08-16 · `D263-KR` KR · §6c US 08-17 on `breadth`). It silently moves the statistic that **carried the ENRG promotion**. Human-approval code change (P5) |
| **2** | **`D270`** — "breadth 0.00" this week is a statement about **VOLUME**, not demand | Directly answerable with no new data: the whole tape is thin (0.732 then 0.649 of the 20-day norm) so the `vol_surge` denominator carries a busier past and the gate closes board-wide at once. **`M144` replicated 6× at record size** |
| **3** | **`D243`** — the US desk has **no IC column** | §8 shows exactly what its absence costs: the desk cannot say whether its own gate axis has a sign in its own market |
| **4** | **`D250`** — `cycle_registry.json` stale, rank-3 floor `0.0` ⇒ check **OFF**; no entry for either live cycle (optical/interconnect, custom AI silicon) | PREMORTEM Lens 4 runs on a registry with no row for the two cycles owning the desk's best-scoring names. `S94` brackets it (08-31) |
| **5** | **`D274`** — the universe union covers what the book **owns**, not what its theses **point at** (`HII`) | Blocks measurement of the most policy-exposed US name in the INDU thesis |
| **6** | **`D264`** — a pool-normalised burst check can still return a **false all-clear** | **Binds DRIFT directly.** The client store is healthy through 08-16, so the routing option is available |
| **7** | **`R56` / `EA`** — delisted 08-04, still in `us_top300` at day **33**, null last bar for a 5th run | **10th consecutive run.** State the current shape (a COMM composition change), do not re-copy the original phrasing |
| **8** | **`D259-KR`** — `catalyst_calendar` does not read `SCENARIOS`' armed dates | Reproduced on this desk today: the calendar reports **2 binaries** in a 10-day window in which **eight US rows settle** (§3c) |

---

## 11. §4c — verification that arrived after the assertion (D48 class)

**This stage's own count: 3.** Written down, not edited away.

1. 🚨 **This stage's own PREFLIGHT labelled the `breadth` contamination "★★ NEW" and it is not new.**
   The mechanism was already registered as **`D261`**, measured on the US green set as **`M701`**
   (08-16: 🟢 11 → 9 with zero price change), and measured in KR as **`D263-KR`** (6 tags changed,
   breadth 11.4% → 11.6%). ⇒ **What is actually new is narrower and worth keeping**: (i) the effect
   landed on **`breadth` specifically**, the statistic that carried the ENRG promotion; and (ii)
   **yesterday's rights table granted `breadth` as safe anyway** — *"unweighted, so the stale caps barely
   touch them; they carry more load, not less"* — while the same run's own HANDOVER §6 carried `D261`.
   **The desk contradicted itself inside one run and neither half noticed.** That is the finding.
2. 🚨 **`D277` — registered yesterday, falsified today by its own next observation.** The claim was
   "zero new entrants, ever" (51 → 51 → 50). `RTX` re-entered (§6b). The monotone half is dead after
   **one run**. It is not deleted; `D277`'s measurements stand and its diagnosis is corrected.
3. 🚨 **`D276`'s "flicker" diagnosis is narrowed by tonight's probe.** A transport that flickers on a
   minute timescale should have dropped some of 80 sequential requests inside 18.5 s. It dropped
   **none**. Combined with the KR desk's even spread of successes across a full sweep, the better-fitting
   statement is **"per-call failure probability rises under full-universe sweep load"**, not "the bridge
   blinks." ⚠ **Still `[inferred]`** — load and a ~5-second window are not separated by today's data.

⚠ **Stated plainly**: three self-refutations, two of them against claims **this desk registered
yesterday**, is a sign the prior run under-tested itself — not a sign this one is clean. Per §4c a
*zero* usually means the controls were not adversarial. The stages below should assume this stage
under-tested itself too, **especially with the tape frozen for a fourth run, which removes the cheapest
source of contradiction.**

---

## ✅ EXIT CHECK

- [x] **Shared spines read** — `STANDING_VIEW.md` (regime call §1, measured chain §2, §3a registry, §4
      asymmetry, §5 retracted ledger through `R75`, §6 open contradictions) + `SCENARIOS.md` (MASTER
      scoring log **including the 08-17 KR entry for `S51-KR`**, MASTER INDEX) + `STANDING_VIEW_US.md`
      (§2 rows through `M709`, §3a rows as overwritten 08-16) + `SCENARIOS_US.md` (all ARMED headers
      enumerated, `S32`→`S94`) + `RESEARCH.md` (loaded as the C/S/D/W/L trigger groups in §7).
      ★ **The other market's file WAS opened and it mattered this time** — `SCENARIOS_KR.md` held a row
      dated **today** (`S51-KR`), verified **already scored `FIRED-C`** by the morning KR run (§3a).
      🚨 **Budget breach reported, not silently absorbed** (`handoff_compact --budget-only`): a US run
      reads **1,598.0 KB against a 250 KB budget = 1,348 KB over** — **worse than yesterday's 1,301 KB**.
      `RESEARCH.md` 454.8 (budget 85) · `STANDING_VIEW.md` 354.0 (45) · `STANDING_VIEW_US.md` 292.6 (50)
      · `SCENARIOS_US.md` 287.3 (50). §2 fact rows = **788 at 0.51 KB/row against a 0.35 limit.** The
      cause is visible in the files' own headings — **per-run `## Added by the …` append blocks**, exactly
      what the 07-25 rule forbade. **This is a finding for a human (P5), and it is why this stage read the
      spines by section rather than end-to-end; that limitation is stated rather than hidden.**
- [x] **Retracted ledger read BEFORE forming any view.** Live entries checked: `R69` (the `M40`
      Financials-breadth reversal — it withdrew *"the board's only breadth-led sector"* **as a property of
      Financials**, and did not assert Financials has no breadth; `M669` relocated it to
      alternatives/asset-management, `KKR` is that node), **`R73`** (the `P56` front-end clause — carried
      into §1 as an amendment, and the UTIL/RE/STPL mechanism updated to `P65` accordingly), `R74`/`R75`
      (KR-registered today; `R75` is carried as a *method* finding under W1). `R56`/`EA` is carried as an
      **open defect, not a belief**. No claim above resurrects a retracted entry.
- [x] **Every past-dated scenario scored or `EXPIRED` with a reason.** **Zero US rows matured**;
      `EXPIRED = 0`; silent skips = 0. The one past-dated row in scope (`S51-KR`, dated today) was
      **verified already scored `FIRED-C`**, not assumed. `S8` named for the **15th** run.
- [x] **`reject_ledger.py due` run** — 0 due, **legacy 0**, 182 total / 91 resolved.
- [x] **`missed_ledger.py due` run** — 0 due, **legacy 0**, 138 total / 56 resolved. Sign inversion
      stated; the two are not summed.
- [x] **Exposure state read and carried** (§5) — verdict `정상`, target 95%, **invested % 🚨 unknown and
      NOT substituted**, cumulative **−14.31pp = cash −6.33 + selection −7.98 on n=8**. Not a cold start
      (35 rows). `밴드미설정` not triggered.
- [x] 🚨 **Instrument health inherited before any number was trusted** — `PREFLIGHT_US.md` read; the
      binding table is §6. It revokes **seven** things (two of them new: the word "today" applied to a
      Monday run that predates the open, and `breadth` as a news-independent reading).
- [x] **Claims asserted and then refuted are written down, not edited away** — §11, **three** instances,
      two of them against claims this desk registered yesterday.
- [x] **Stale rows flagged with their `asof`** — `us_top300.csv` **33 days** · `cycle_registry.json`
      stale (rank-3 floor 0.0 ⇒ check OFF) · `data/news_fts*.db` **0 bytes** (5 days) · `news_alert.db`
      **0 bytes** · `handoff/` **1,348 KB over budget**. No suspension cleared this run, so none converted
      to a dig.
- [x] **`[measured]` / `[inferred]` tags preserved.** The regime call, `P65` and §11's load-vs-window
      diagnosis all travel as `[inferred]` and are not usable as evidence.
- [x] **RESEARCH triggers loaded as binding constraints**, grouped C/S/D/W + L (§7), with the stage each
      group binds named.
- [x] **No position sizing, no buy/sell language anywhere in this file** (P4).
- [ ] `handoff/*.md` writeback — **deferred to run end** (append-only for retractions), per the stage's
      own instruction.
