# HANDOVER — industry_US · 2026-08-23 (Sun) · Stage 2/11 · L1·HANDOVER

> Inheritance packet. **This stage transports analysis; it makes no market call, names no size and
> issues no buy/sell language (P4).** Run clock **KST 22:09–22:5x = ET 09:09–09:5x, SUNDAY — US cash
> CLOSED, and closed Saturday too.** Terminal settled bar throughout: **2026-08-21 (Friday close)** —
> **the same bar the previous run ended on.**
> Read: `handoff/STANDING_VIEW.md` (spine §1–§6 + retracted ledger through **`R95`**, incl. the
> `industry_kr` block appended this morning) · `STANDING_VIEW_US.md` (§2 fact table, §3a rows) ·
> `SCENARIOS.md` (spine scoring log through the 08-23 KR entry + MASTER INDEX) ·
> `SCENARIOS_US.md` (**S1–S114**, `P13`–`P89`, opened for the exhaustive past-date sweep) ·
> `SCENARIOS_KR.md` (**opened** — the other market's file is this run's to score if past-dated) ·
> `RESEARCH.md` (Part A triggers · Part B lenses · Part C dig list through **`D316`** / **`D321-KR`**).

---

## ★★★ The three things this packet exists to hand forward

1. ★★★ **This run has no new price information, and that is a measurement, not a caveat.** Its 299
   scores, 299 tags and 11 sector rows are **identical, element for element, to the 08-22 persisted
   file** — 0 differences. There was no Saturday session and no Sunday session.
   **`n_new_sessions_since_prior_run = 0`.** Every stage below must source its value from something
   other than the tape, and say which.
2. ★★★ **`R96` — the previous run's own correction is retracted, in its direction.** 08-22 concluded
   the partial-coverage tag layer was *"selection-biased **upward**"* and could not name the affected
   tickers (*"unrecoverable — run 1 was not persisted"*). **Today both runs were persisted.** The six
   flipped names are named, and **five of six move AWAY from neutral while one moves toward it — three
   up, three down.** The bias is **dispersion, not optimism**. §7.
3. ★★★ **The four persisted sweeps of 08-18 → 08-21 all carry `vel_coverage ≈ 16–17%`** — i.e. every
   one of them has a partial-coverage tag layer, built exactly the way today's run 1 was. **Only the
   08-22 and 08-23 files have a breadth reading this desk can vouch for.** Any back-reference to a
   green count in a report dated 08-18…08-21 inherits the defect and must be re-derived from the
   score column instead. §7.

---

## §0 · Instrument health inherited — what this run may NOT claim

`llm_outputs/2026-08-23/preflight/PREFLIGHT_US.md` **was run** (22:09–22:22 KST, this run's own stage
−1). **PASS 3 / FAIL 5** — the same verdict *pattern* as 08-22, which is the point: five of these are
structural and none is being repaired by the passage of days. The rights table binds every stage below
and is not re-litigated here.

**Revoked for this run:**
- ★ **Any sentence of the form "since our last run, X moved / turned / accelerated."** False by
  construction — there was no session. The only Δ that exists (08-20 → 08-21) **is the Δ the 08-22 run
  already consumed**, and re-labelling it as fresh would manufacture a second observation from one
  session.
- The sweep's **news-velocity axis** (`vel_coverage` exactly **0.0**) · any *"it went quiet"* sentence
  sourced from the sweep · the **Consumer Staples `wflow` sign** (`WMT` at **28.9%** owns it) · any
  concentration number without its `--days` · market-cap-weighted claims resting on universe weights
  (**39 days** stale) · any flow/RS/OBV/short call on **`EA`** (11th run unmeasurable) · `--ic`-derived
  sizes as evidence-backed · **KR-holding P&L, stops, or percent-of-total-assets** (the book prints
  `n/a` on both KR marks for a 4th run, so the 17,607,290 KRW denominator is computed without them) ·
  **any 2026-08-22 or 2026-08-23 price** (no weekend bar).
- ★ **New this run: no breadth number from a partial-coverage sweep, in EITHER direction** (§7).

**Granted:** settled prices and every price-derived statistic through the **2026-08-21** close ·
`flow_score`, RS, OBV, `vol_surge` · `eqflow` for all 11 sectors and `wflow` signs for the ten
non-flippers · **today's tag layer** (`velocity: null` on all 299 ⇒ provably velocity-free, citable as
*3-axis unanimity*, never as *news-confirmed*, and **never compared to a pre-08-22 run's breadth**) ·
FINRA short pressure · CFTC COT · FRED · primary filings · `module_chart --read` and
`margin_history <T>` (with the "`--help` dead, output probed" stamp) · **direct news calls made outside
a sweep window** — today **43/43 successful**, including a 40-name falsification probe that returned
**40/40 valid with 0 true silences**.

★ **The news mechanism, inherited from 08-22 and reproduced today rather than re-measured.** Budget
**≈100 remote calls (≈51 names)**, hard contiguous wall, **≈90 s cooldown**. Today's two sweeps on one
price frame returned **16.4%** then **0.0%** — the 08-22 drain reproduced to the decimal, with the
tunnel answering **3475** before and the hand probe **40/40** after. **Any stage needing news today
should spend ≤50 names at a time on the handful it actually cares about.** The cumulative falsification
ledger now stands at **360 hand-checks over nine runs, 0 false silences** — the most heavily-replicated
measurement this desk owns.

---

## §1 · Inherited regime call and standing view

**Regime (spine §1, `[inferred]`, unchanged):** *memory is a price-cycle industry in rate-of-change
deceleration while its level stays tight* — the equity tracks the **second derivative** of price, not
the level, which is why "shortage persists" and "stocks struggle" are both true.

⚠ **The per-name table below is NOT a fresh measurement.** Every figure in it is the **08-21 settled
close**, which is the same close the 08-22 packet measured, and this run's sweep reproduced them with
**zero differences**. It is reproduced here as *inheritance*, explicitly stamped, because a HANDOVER
that silently re-prints yesterday's numbers under today's date is manufacturing evidence.
⚠ Per `C11`'s replacement constraint (§8 of the 08-22 packet), every OBV figure names its instrument:
all are the **sweep's `obv_norm` — a 20-session change of a cumulative signed-volume series ÷ 20-day
mean volume (a LEVEL)**, not `module_chart`'s 10-session slope of a rolling-20 (a RATE).

| Node | Carried state | Tag | 08-21 settle (unchanged since the 08-22 packet) |
|---|---|---|---|
| **`MPC` · `PSX` · `VLO`** | Refining-**capacity** destruction; the constraint is `L2` peak margin, not the barrel | `[measured]` price · `[filing]` structure | 🟡 ×3. flow **+0.700 / +0.728 / +0.506**, rs60 **+44.0 / +37.0 / +43.1**, all three OBV 매집. `S88` settled **C**; **`P70` MISSED on its control leg** (`BZ=F` 5-session **+6.631%** vs a ≤ +2.0% bar) ⇒ `R89`'s retraction of the *separation* claim is confirmed at settle. **The refiner CONTRACT question (`module_disclosure_us MPC` → 10-Q MD&A + Item 1A) is unopened for a 4th run** and `P70`'s miss makes it the binding gap, not a note |
| **`RTX`** | The defense group's **beta**, not its leader; the book's diversifier | `[measured]` | 🟡. flow **−0.122**, rs20 **−5.0**, rs60 **+16.8**, OBV **중립 +0.023**; **delta −0.304**, still the book's largest single-session deterioration — ⚠ **and it is now a THREE-day-old delta, not a fresh one.** `M778` measured `ETN`–`RTX` at **−0.006**, so the diversification claim survives. **Customer unmeasured, 206 days (`W4`)** |
| **`LHX`** | Succession priced as a **discontinuity** (`S97` FIRED-A) | `[measured]` | 🟡. flow −0.113, rs20 −14.8, rs60 −15.7, OBV 중립, surge 1.21. **`M803` settled the obligation**: `M704` ex-`LHX` is **−4.162 vs −4.775** ⇒ the discontinuity explains **13%** of defense weakness; the other **87% is every other prime** |
| **`NUE`** | Post-earnings re-rate; FINRA **z −2.33 (covering)** | `[measured]` | 🟡. flow **+0.319**, rs20 −5.2, rs60 −3.2, OBV 매집 **+0.148**, surge **1.41** — clears the surge leg, **fails rs20**, so not 🟢. ⚠ `S114` (registered 08-22, settles **09-03**) is the steel/tariff bracket pointed at this held name |
| **`T`** | 🚨 An orphan — **9.74%** of the real book's invested, no cycle label, no card | `[measured]` | 🟡. flow +0.089, rs20 +1.2, rs60 −0.4, OBV 매집 +0.296, surge **0.47**. `S107` → **09-03**. Still **unindexable** by `module_report_tags` (`M152`) |
| **`WMT` · `TGT`** | The Staples carriers, and they disagree | `[measured]` | `TGT` flow **+0.950 🟢** vs `WMT` **−0.333 🔴** — **17.1pp intra-sector on one window (`W5`)**. **`WMT` is today's G3 flipper for a 2nd run** (sector −0.013 on `wflow`, **+0.116 ex-Walmart**). 🚨 **New today: `WMT` is ALSO one of the six tag-contaminated names** (§7) — it is simultaneously the name that owns the sector's *sign* and the name whose *tag* moved with the news bucket. `S93` VOIDed |
| **`GOOGL`** | Half the COMM underweight is already wrong | `[measured]` | 🟡. flow +0.245, rs20 +4.2, rs60 −13.4, OBV 매집 +0.135. Not a flipper (COMM +0.108 → ex-top1 **+0.022**, same sign). **`D297` still unfixed**: `GOOG` is a second **38.3%** row, so the Alphabet complex is **76.6%** of the sector while `top1_w` reports half |
| **`KKR` · `LITE` · `ORCL`** | Cross-sector orphans, carried because their sectors hold no DEEP slot | `[measured]` | 🟡 ×3. `KKR` +0.458 · `LITE` **+0.639** · `ORCL` +0.444 with rs60 **−25.3** |
| **`XOM`** | 🔴 RESOLVED — the crack-attribution **control**, and a control is not a bet | `[measured]` | Negative: flow **−0.183**, OBV **분산 −0.101**, delta −0.200. Ledger `A.flow미도착` → **09-16** |
| **`NEM` / `FCX` / the `Copper` COT** | 🔴 RESOLVED — survives as a risk, not a thesis | `[measured]` | `S89` FIRED-**B** (exc5 **+13.104**, anti-signal `GC=F` **+5.563%** inside the ±8% void band ⇒ the row scored). ⚠ **`M779`: 246.4% of `NEM`'s rs60 sits in the last 20 sessions** ⇒ **B fired on exhaustion geometry** (`D306` class). **B is a price fact, not evidence of a base** |
| **The optical/interconnect cycle** | 🚨 `cycle_registry.json` has **no row** for it ⇒ exposure is **unmeasurable, not zero** | `[measured]` | `S86` and `S96` both settled **B**. `LITE` **+0.639** OBV 매집 · `COHR` **+0.158** OBV 중립 · `CIEN` **−0.380 🔴** rs60 **−34.0**. `D250`/`M731` unfixed. ⚠ `APH` was closed `entered` on 08-22 **on the file naming the node, not on `APH` being mapped into it** — the caveat travels with the closure |

**The 11 book names, 08-21 settle — reproduced, not re-measured (0 differences vs the 08-22 file):**

```
PSX  +0.728 rs20 +13.8 rs60 +37.0 OBV accum   surge 1.11   MPC  +0.700 rs20 +13.0 rs60 +44.0 OBV accum   surge 1.06
HPE  +0.489 rs20  +8.5 rs60 +41.6 OBV accum   surge 0.68   ANET +0.417 rs20  +4.8 rs60 +20.2 OBV accum   surge 0.82
NUE  +0.319 rs20  −5.2 rs60  −3.2 OBV accum   surge 1.41   ETN  +0.210 rs20  +0.1 rs60  +1.1 OBV accum   surge 0.77
NDAQ −0.025 rs20  +3.0 rs60  +6.5 OBV neutral surge 0.67   RTX  −0.122 rs20  −5.0 rs60 +16.8 OBV neutral surge 1.07
MET  −0.164 rs20  −4.1 rs60 +11.4 OBV neutral surge 0.87   NVDA −0.181 rs20  +0.2 rs60  −1.0 OBV neutral surge 0.75
AVGO −0.221 rs20  −7.2 rs60 −14.7 OBV neutral surge 1.00
```

★ **All 11 are 🟡 for a third consecutive run.** ⚠ And the instrument caveat is now stronger than it was
on 08-22: with `vel_coverage = 0.0` the tag layer has **one fewer axis available to push any name off
neutral**, so *"the book is all-neutral"* is **a statement about the instrument, not about the book.**

### Retracted ledger read BEFORE forming today's view (spine §5, through `R95`)

Eight entries bind this run; the two newest arrived this morning from the sibling desk.

- **`R78` · `R81`** — *a 🟢 tag is not evidence while `vel_axis=false`*. **Stands, and today it again has
  nothing to bite on** (all 299 velocities null ⇒ every tag is price-only). It re-binds the moment a run
  gets partial coverage — which is what today's discarded run 1 was.
- **`R82`** — the Consumer Staples UW− → UW promotion is withdrawn. **Live today**: Staples is the G3
  flipper and the flipper works *against* the sector. **No stage may promote or demote it on `wflow`.**
- **`R80`/`R84`** — the "survivor set is deterministic / burnt in the first 51 tickers" shape. The 08-22
  run re-opened this with a direct burst experiment and landed on the budget side. **Nothing today
  re-argues it; today's evidence is consistent with it and is not offered as a re-test.**
- **`R87`/`D298`** — any carried claim containing a **COUNT** or a **STATE** needs re-computation each
  run. **Applied to this entire packet**: the per-name table above is stamped as *inherited*, and the
  ledger/exposure counts in §3–§4 were re-run rather than carried.
- **`R89`** — the refiners' *separation* claim: killed, and confirmed at settle by `P70`'s MISS.
- **`R90`** — `P65`'s bull-steepener framing: `DGS2` **4.19**, `30y−10y` **0.54**. **Unchanged and
  unchangeable today** — FRED's daily series still end 2026-08-20 (§2b).
- **`R93`** — *"Warsh's Jackson Hole debut is TODAY, 2026-08-21"* is wrong by six days, and the
  second-order retraction (that `catalyst_calendar` did **not** miss a D-0 binary) is the one that
  matters. ★ **Independently re-verified today from bodies, not headlines** (§8).
- **`R94` · `R95`** *(KR-registered this morning; read because §5 is un-split)* — both kill a **20-day
  cumulative investor-flow sign** by splitting the same window into halves and getting the opposite
  answer. ⚠ **The transferable half is a method warning, not a KR fact**: *a cumulative-window sign is
  not a direction*. **`W1` forbids importing the KR measurement**; what carries is the question — **does
  this desk cite any 20-day cumulative as a direction?** It does not currently hold an equivalent US
  instrument (there is no US investor-type feed), so the answer is *no by absence*, and that is recorded
  rather than claimed as discipline.

**Nothing in this packet re-argues a retracted claim.** ⚠ One thing in this packet **retracts a claim of
its own predecessor** — §7, `R96` — filed with the measurement that killed it.

---

## §2 · Scenarios — exhaustive past-date sweep: **0 to score**, and the sweep is shown

### (a) The exhaustive table — "nothing was due" and "nobody checked" must not look alike

The sibling desk made this point in its own log this morning and it is adopted here. **Every
US-owned bracket with a settle date, checked against 2026-08-23:**

| Settle | Rows | Status |
|---|---|---|
| ≤ 2026-08-21 | `S84`–`S101`, `P65`–`P75`, and all earlier | **ALL SCORED** — nine by the KR desk on 08-22, five by the US desk on 08-22 (`S88` C · `S89` B · `S90` A · `S91` VOID · `S93` VOID), four P-rows settled |
| **2026-08-22** | **none** | — |
| **2026-08-23 (today)** | **none** | — |
| 2026-08-24 | `S74` | armed, **tomorrow** |
| 2026-08-25 | `P79` · `S108` (⚠ premise void, settles as registered per `D242`) | armed |
| 2026-08-26 | `S79` · `S101` · `S103` · `P77` · `P78` · `P80` (+ `NVDA` print) | armed |
| 2026-08-27 | `S81` · `P83` (+ Jackson Hole opens) | armed |
| 2026-08-28 | `P67` · `P81` · `S111` · `P85`–`P89` (+ July PCE, `FRO`) | armed |
| 2026-08-31 | `S92` · `S94` · `S104` · `S112` (+ MSCI review) | armed |
| 2026-09-01 → 09-30 | `S113` · `S109` · `S105`–`S107` · `S110` · `P84` · `S114` · `S48` | armed |

⇒ **The earliest US settle is 2026-08-24, one day away. Zero rows were due today, and this table is the
evidence that the question was asked.** `EXPIRED` **0** · silent skips **0**.
**KR-owned rows** (`SCENARIOS_KR.md`, opened): earliest settle **2026-09-04** (`S67-KR`) — none past-dated.

### (b) `S102` — not-yet-arrived, **4th consecutive US run**, and the diagnosis is now 5×-replicated

Observable: *"`[FRED]`, the first close covering 2026-08-21"* · `DGS2` ≥ 4.30 (A) / `DGS2` ≤ 4.08 ∧
`30y−10y` ≥ 0.59 (B), frozen.
**Today's pull is the fifth independent one** (two by the KR desk on 08-22, one by the US desk on 08-22,
one by the KR desk this morning, this one now): **FRED's `DGS2`/`DGS10`/`DGS30` still end 2026-08-20** —
`DGS2` **4.19**, `DGS30` 5.23, `DGS10` 4.69 ⇒ `30y−10y` **0.54**.
🚫 **The 08-20 values are NOT substituted.** Changing an observable after the fact converts a prediction
into a narrative.
★ **What this row produces today is not a verdict but a sample.** `D309` (*a bracket on a FRED daily
series settles on a publication, not on a market close — and FRED does not publish on weekends*) is now
**five identical observations across three desks and three calendar days**. It has stopped being an
inference. **The 08-22 hand-off to the 08-24 run stands unchanged**, and today — a Sunday — could not
have changed it.

### (c) 🚨 `S8` — undated and unscoreable for the **22nd** consecutive run

Still on `CATALYST_WATCH` as its undated 🔀binary (*"Iran 'Strait of Hormuz open' statement"*, axis=oil;
confirmed present in today's `catalyst_calendar --days 10` output). **A human must `VOID` it or
re-register it with a date (P5).** `S74` (settles **tomorrow**) and `S92`/`S95` bracket what `S8` cannot.
This run **does not fix it and only increments the count** — the record that it was not passed over
silently is the whole purpose of this line.

**Score this run: 0 scored (exhaustively verified, table above) · 0 `EXPIRED` · 0 silent skips ·
1 not-yet-arrived with a 5×-replicated structural reason and a named successor run (`S102` → 08-24) ·
1 undated and named for the 22nd time (`S8`).**

---

## §3 · Both ledgers — audited symmetrically

`reject_ledger.py due` **and** `missed_ledger.py due` were both run (not `score` alone).

| Ledger | Rows | Resolved | Past due | Legacy (no revival condition) |
|---|---:|---:|---:|---:|
| Rejections | **225** | 133 | **0** | **0** |
| Misses | **206** | 110 | **0** | **0** |

★ **Both ledgers are completely clean — 0 due and 0 legacy on each, for the second consecutive run.**
The legacy count has now held at **0 for 12 runs**, which is a trend rather than a quiet pass.

**The four rows that were due on 08-22 all closed, and the two pre-commitments both held:**
- **`APH`** (08-07, `U.발굴부재`) — closed **`entered`** on 08-22. The 08-21 packet had pre-committed in
  writing that it *"must not cross a second HANDOVER unresolved"*. **It did not.** ⚠ The closure note
  carries its own honest caveat forward: OR-leg 1 was met on `SECTOR_DEEP_IT.md` **naming** the
  interconnect node, while the node itself was populated by `LITE`/`COHR`/`CIEN` and **`APH` was not
  mapped into it**. That caveat travels; it was not laundered at closure.
- **`009830` 한화솔루션** — handed back to `industry_kr` on 08-22 and **resolved by that desk this
  morning** as `reaffirmed`, with both entry legs measured and failing. **A row handed across desks came
  back closed within one run.**
- `VLO` **entered** · `CBRE` **reaffirmed** — both on 08-22 measurements.

⚠ **Sign hygiene (`3c`)**: the two ledgers' `excess` columns are **inverted** relative to each other and
are **not summed** anywhere in this packet.
⚠ **`score` is accumulation, not an edge** — the miss ledger's first six rows are outcome-selected and
the script says so itself.
★ Carried and still binding (`T25`): any structural rejection this run makes must re-print the rejection
ledger's loss-asymmetry number beside it.

---

## §4 · Exposure state — carried as size context for BET/ALPHA (read-only; this stage never logs)

`exposure_rule.py state` + `show --tail 10`, both run.

| Quantity | Reading |
|---|---|
| Rule state | **정상 (normal)**, prior state normal — *"no firing condition"* |
| Bench (069500.KS) 08-21 settled | 109,980 · **+1.654%** · −0.07% from the 20d high · +25.5% from the 20d low · volume **1.481×** |
| Target invested | **95%** |
| Current invested | 🚨 **BLANK in `state`** — no account query supplied, so `state`'s own gap is unavailable |
| Ledger's last row (08-21, **live** bar) | invested **85.1%**, band gap **−9.9pp** |
| Band-gap trajectory | −39.4 → −27.1 → −14.0 → −13.9 → **−9.9pp** — closing, five consecutive readings |
| Cumulative decomposition | total **−16.64pp** = cash **−6.46pp** + **selection −10.19pp**, **n = 11** |

🚨 **The one thing that changed here is that nothing changed, and that is itself the finding.** The
ledger holds **38 rows** and its last is still **2026-08-21**. The script's own stated goal is printed
beside the number — *"the aim of this repo is to raise this n by 1 every day; at n≈20 you may finally
ask about the sign (`C4`)"* — and **n has been stuck at 11 for three calendar days** because weekends
accrue nothing. **The instrument that is supposed to answer "does this desk have selection skill" gains
zero information on 2 of every 7 days**, so the honest ETA to n≈20 is **~12 calendar days, not 9.**

⚠ **`C4` binds in both directions at n=11**: **no stage may claim the desk's selection has a negative
edge.** What may be said is narrower and true: *the "our lead is cash, not skill" story is no longer
supported by its own ledger*, because the sign flipped on both components since 07-31.

⚠ **Two standing flags carried, not acted on** (P4 — this is a research run):
- 🚨🚨 **`ARMED (TIMEFOLIO_EXECUTE=1)`** on every ledger row. **Named, not touched.** No stage in this
  protocol may pass `--execute`.
- 🚨 **`투자비중미상` on `state`** ⇒ the 4-state verdict is quoted with its gap missing and **no number is
  substituted** (P5). The band gap above comes from the *ledger's* 08-21 row and is labelled **live-bar**.
- ⚠ Carried and still true: `exposure_rule`'s `state` and `target` can diverge (the minimum-maintenance
  gate), so a completed plan is **not** citable as evidence. Human fix.

---

## §5 · Reconciliation — belief vs mechanical coverage

`module_report_tags show` cross-queried.

- **Coverage without belief:** `industry_US/SECTOR_DEEP_SEMI.md` is dated **2026-07-15** — **39 days**,
  the oldest US DEEP file on the board by a wide margin (next-oldest is `SECTOR_DEEP_CONSUMER` at 7
  days), and it covers **the AI-compute epicenter, where 4 of the 11 book names live** (`ANET`, `AVGO`,
  `NVDA`, `HPE` adjacent). ⚠ **And `NVDA` reports in three days.** ⇒ **Top-ranked DEEP candidate on the
  reconciliation axis**, carried to ROTATION with the print date attached.
- **Belief without coverage:** `T` (9.74% of the real book's invested) still has **no DEEP file, no
  cycle label and no card** — 🚨 and per `M152` it is one of **two book names (`MET`, `T`) that
  `module_report_tags ticker` cannot index at all**, so this instrument **cannot** reconcile them by
  construction. **Unindexable ≠ uncovered**, and the distinction is preserved rather than collapsed.
- ✅ **The 08-22 packet's stale-index note is CLOSED.** It recorded that `industry_US/PREFLIGHT_US.md`
  in `REPORT/` still read 2026-08-20 and instructed its successor not to repeat the omission. **Today
  the ledger reads `PREFLIGHT — 2026-08-22`** ⇒ the 08-22 copy-to-`REPORT/` step ran. **This run must
  do the same at run end** and the check is recorded here so it can be verified rather than assumed.

---

## §6 · The signal scoreboard — the pre-registered threshold is still crossed, and `W1` still blocks it

`axis_inflection.py` → `ic_ledger.py log` → `ic_ledger.py score`, all three run. **0 new rows accrued**
(**729 rows, `market=kr`**) — nothing newly resolved since the last run, which is expected on a weekend.

| Axis | h | n | `n_eff` | mean IC | **t(NW)** | positive | verdict |
|---|---|---|---|---|---|---|---|
| **`vol_surge`** | **1** | 34 | **34.0** | **−0.0454** | **−3.86** | 24% | ★ **significant, passes Bonferroni (\|t\|>2.8)** |
| **`vol_surge`** | **5** | 27 | **5.4** | **−0.0555** | **−3.38** | 18% | ★ **significant, passes Bonferroni** |
| `obv_norm` | 5 | 27 | 5.4 | −0.0704 | −2.08 | 22% | significant on a standalone bar only |

🚫 **This run may not act on it.** The ledger is **`market=kr`**. Importing a KR-measured axis IC into
the US sweep is **exactly the `W1` violation this repo keeps logging** — the same reasoning the protocol
used on 2026-07-31 to refuse importing KR's DEEP-budget cut into the US desk. **The threshold cleared in
KR; the US desk has no equivalent measurement and therefore no verdict.**

⇒ **`D310` stays open and its cost is now countable: this is the second consecutive run in which a
desk-written kill-condition is met in the market that cannot act and unmeasured in the market that can.**

★ **What IS legitimately carried, with the `W1` caveat on its face.** `vol_surge ≥ 1.2` is one of the
three axes in the 🟢 gate, and with velocity null it is the axis that blocks almost everything — on the
08-21 frame **`CBRE` failed its ledger leg on that axis alone** and **`NUE` fails 🟢 despite surge 1.41**.
If the KR-measured negative IC generalises, the gate is selecting **against** forward returns. **That is
a hypothesis to test on US data, not a finding to apply** — and every stage citing a 🟢 today carries the
sentence *"selected partly on `vol_surge`, an axis measured negative in the KR ledger."*

---

## §7 · 🚨 `R96` — the retraction this run files against its own predecessor

**The claim.** The 2026-08-22 `industry_US` run wrote, in its PREFLIGHT §3, its HANDOVER §0 and its
asof-chain entry (`M795`): *"zero coverage is uniform and therefore safe, while partial coverage is
**selection-biased upward** … three names were promoted to 🟢 for no reason but having landed inside an
arbitrary 51-name bucket. **The three names are unrecoverable — run 1 was not persisted as JSON. Logged
as a gap, not guessed at.**"*

**What killed it — the same experiment, run today with both outputs persisted.** Two sweeps, four
minutes apart, one identical price frame (`asof` 2026-08-21 both times):

| | Run 1 (`vel_coverage` **16.4%**) | Run 2 (`vel_coverage` **0.0%**) | Same? |
|---|---|---|---|
| `flow_score`, all 299 names | — | — | ✅ **0 differences** |
| `wflow` / `eqflow` / `delta`, all 11 sectors | — | — | ✅ **0 differences** |
| Universe 🟢 / 🔴 | **9 / 72** | **6 / 71** | 🚨 no |
| **Tags** | — | — | 🚨 **6 names differ** |

| Ticker | Sector | Run 1 (partial) | Run 2 (zero) | Direction |
|---|---|---|---|---|
| `MRVL` | Information Technology | 🟢가속 | 🟡중립 | away from neutral |
| `MA` | Financials | 🟢가속 | 🟡중립 | away from neutral |
| `CVX` | Energy | 🟢가속 | 🟡중립 | away from neutral |
| `MS` | Financials | 🔴분산 | 🟡중립 | away from neutral |
| `JPM` | Financials | 🔴분산 | 🟡중립 | away from neutral |
| `WMT` | Consumer Staples | 🟡중립 | 🔴분산 | **toward** neutral |

**⇒ Three consequences, and the second is the one worth carrying.**

1. **The direction was wrong.** Three names went up and three went down; five of six moved **away** from
   neutral. Run 1 carried **one extra 🔴 as well as three extra 🟢** (72 vs 71). The aggregate 🟢 9→6
   that the 08-22 run read as an upward bias was **one half of a symmetric effect.**
2. ★★★ **The correction the 08-22 run proposed would have been wrong on two specific names.** Its
   remedy was, in effect, *discount the greens*. Applied to today's run 1 that leaves `JPM` and `MS`
   **marked 🔴 for exactly the same arbitrary reason** the greens were marked 🟢. **An upward bias is
   correctable by a one-directional discount; a dispersion bias is not correctable at all** — which is
   why the rule must be *no breadth number from a partial-coverage sweep, in either direction*, rather
   than a haircut.
3. **What survives, and it matters:** the **uniform-vs-selective half of `M795` is untouched and is now
   better evidenced.** Zero coverage is missing-completely-at-random across all 299 names; partial
   coverage is missing conditional on bucket membership. **Today's persisted file is again run 2**, and
   `_sweep_run1.json` is kept beside it so the next run inherits the comparison instead of re-deriving it.

★ **The ledger consequence nobody had counted.** The persisted sweeps of **08-18 (16.72%) · 08-19
(17.06%) · 08-20 (16.39%) · 08-21 (16.72%)** all have partial-coverage tag layers. **Four of the last six
persisted files carry the defect**; only 08-22 and 08-23 are clean. Their `flow_score` and sector `wflow`
columns remain sound (the score layer never sees `vel`), so **the remedy is to re-derive breadth from the
score column, not to quote the stored counts.**

⚠ **Why this is filed as a retraction and not a refinement.** The 08-22 wording named a **direction** and
justified a **one-sided correction**. That is a claim, it was carried into a rights table, and it is
false. Filing it as "we sharpened it" would hide that a rule this desk wrote would have mis-tagged two
large-cap banks.

---

## §8 · `R93` re-verified from bodies, and `D18` reproduced on the same command

**Why re-verify at all.** `R93` killed a date, and `D311`'s registered remedy is explicit: *when a news
item is promoted to a dated catalyst, require an explicit DATE STRING from a body, not a headline.*
A retraction that is never independently re-confirmed is just a second assertion.

**Measured today, `--scope foreign`, direct calls outside any sweep window:**

| Query (FTS, body-indexed, BM25) | Window | Hits |
|---|---|---|
| `"Jackson Hole"` | 3 days | **96** |
| `"Jackson Hole" AND "August 27"` | 4 days | **22** |
| `"Jackson Hole" AND "August 29"` | 4 days | **20** |
| `"Jackson Hole" AND "next week"` | 4 days | **62** |

Body-carrying sources in the top matches include `economictimes` *"Wall Street Week Ahead: Nvidia
earnings, Jackson Hole to test pillars of stock rally"* (08-22) and a `seekingalpha` *"Wall Street Week
Ahead"* dated **Sun, 23 Aug** — i.e. the corpus has **today's** articles.
⇒ **`R93` holds: the symposium is 2026-08-27 → 08-29, and it is still being written about in the future
tense on 08-23.**

🚨 **And `D18` reproduces on the same command that exposed it.** `catalyst_calendar.py --days 10`, run
today, prints **5 binaries — `NVDA` 08-26 (D-3) · July PCE 08-28 (D-5) · `FRO` 08-28 · `AVGO` 09-02 ·
`S8` undated — and ZERO rows for Jackson Hole 08-27→08-29.** The single largest scheduled macro event in
the window is invisible to the desk's own calendar for a **third** consecutive run, while a named market
view ranks it first (`bloomberg` 08-21: *"Allspring's Miletti Sees Jackson Hole as **Bigger Risk Than
Nvidia**"*).
⇒ **`S112`, registered 08-22, already brackets it on its true dates (settles 08-31).** The gap is in the
**calendar tool**, not in the scenario coverage, and those are different defects with different owners.

⚠ **Catalyst-injection check required by the protocol header:** *any binary ≤48h ⇒ PREMORTEM must
produce a both-sides bracket.* **Today there is none** — the nearest binary is `NVDA` at **D-3**.
**This is the last run before that stops being true**, and the 08-24 run inherits `NVDA` at D-2.

---

## §9 · Stale flags, digs registered, and the dig list ranked for today

### Suspensions and obligations whose date has passed ⇒ dig instructions
- **`S102`** — structurally unreachable by a weekend desk; **handed to the 08-24 run for the second
  time**, with the diagnosis now 5×-replicated (§2b).
- 🚨 **`D295` / `S103`'s `NVDA` bands** — hand-set for a **fourth** run, with the print **three days
  out**. Diagnosed on 08-22 as the tool defect `D315` (`--positioning NVDA` returns the 08-24 expiry for
  an 08-26 event). **This is the last run in which a re-derivation can precede the print, and it is
  ALPHA's obligation today, not a note.**
- 🚨 **The refiner CONTRACT question** (`module_disclosure_us MPC` → 10-Q MD&A + Item 1A) — unopened for
  a **fourth** run. `P70`'s MISS makes the margin-sustainability leg the binding gap. ★ **A closed market
  is the ideal session for a filings read** — there is no tape to compete for attention and the filings
  do not move on weekends. **DEEP-ENRG's obligation today.**
- **`SECTOR_DEEP_SEMI.md`** at **39 days**, covering where 4 of 11 book names live, with `NVDA` reporting
  08-26 (§5).
- **`M704` ex-`LHX`** — ✅ **discharged** on 08-22 (`M803`: −4.162 vs −4.775). Removed from the list.
- **`APH`** — ✅ **discharged** on 08-22 (`entered`, with its caveat). Removed from the list.

### Digs registered by this run
> ⚠ **ID 3-grep at WRITE time** across `handoff/*.md`, `llm_outputs/`, `REPORT/`: `D322` `D323`
> returned **0 hits** in both the suffixed and unsuffixed series. Highest existing: **`D316`** (US) /
> **`D321-KR`** (KR).
> 🚨 **And the first attempt collided — recorded rather than silently renumbered (`D48`).** This run
> first drafted these as `D318`/`D319`; the post-write grep found **`D318-KR`** and **`D319-KR`**
> already in `handoff/RESEARCH.md`, registered by the `industry_kr` run **this morning (08:3x KST,
> ~14 hours earlier)** as part of a `D317-KR`–`D321-KR` block. **The sibling desk's own note says it
> grepped `D317`–`D321` unsuffixed and found 0 hits at its write time — which was true then and is
> exactly the `D76` collision class the ID rule exists to prevent: two desks reserving the same
> integer on the same day, one with a suffix and one without.** Numbers were moved beyond **both**
> series. ⚠ **The real defect is that the reservation is not atomic**, and neither desk can see the
> other's pending write — carried as an observation below, not registered as a dig this run.

| ID | Dig | Evidence (measured this run) |
|---|---|---|
| **`D322`** | 🚨 **A partial-coverage tag layer is biased OUTWARD, not upward — so no one-directional correction can repair it, and four persisted files carry the defect uncorrected.** | Two sweeps on one price frame, both persisted: **6 tags differ, 3 up and 3 down, 5 of 6 away from neutral** (`MRVL`/`MA`/`CVX` 🟢→🟡, `MS`/`JPM` 🔴→🟡, `WMT` 🟡→🔴), while **all 299 `flow_score`s and all 11 sector `wflow`s are identical**. The 08-22 remedy (*discount the greens*) would have left `JPM` and `MS` mis-tagged 🔴. **Persisted `vel_coverage`: 08-18 16.72% · 08-19 17.06% · 08-20 16.39% · 08-21 16.72% · 08-22 0.0% · 08-23 0.0%.** **Positive-form remedy: derive `breadth`/`green`/`red` from the score column, which never sees `vel`** — or pass the run-level axis set into `flow_tag` so the tag layer and the score layer share one axis count |
| **`D323`** | 🚨 **The instrument that is meant to answer "does this desk have selection skill" gains zero information on 2 of every 7 days, and its own ETA line does not say so.** | `exposure_rule.py show` prints *"the aim is to raise n by 1 every day; at n≈20 you may ask about the sign"* — but **n has been 11 for three calendar days** (ledger 38 rows, last **2026-08-21**) because the accrual is keyed to sessions while the sentence is written in calendar days. **Same failure shape as `D16`** (the snapshot daemon counted files as days and reported *"35 more days"* against a true 108). **Positive-form remedy: state the ETA in CALENDAR days using the trading-day ratio** — n=11 → n≈20 is **~12 calendar days, not 9** |

### Method observations (rule candidates — not promoted to triggers)
- ★ **A retraction that is never independently re-confirmed is a second assertion.** `R93` was
  re-verified today from **body** co-mentions (22 hits on "August 27", 20 on "August 29") rather than
  re-quoted. **`D311`'s remedy is cheap to run and should be run on every retraction that killed a date.**
- ★ **"Nothing was due" and "nobody checked" look identical in an output.** The sibling desk's exhaustive
  settle table (adopted in §2a) is the only device that separates them. **A run scoring zero scenarios
  should be required to print the table.**
- ★ **A weekend run is not a degraded weekday run — it is a different instrument** (carried from 08-22
  and reinforced today). It cannot score FRED rows (`D309`, five replications), it gains no exposure-
  ledger observation (`D319`), and its sweep is a byte-identical repeat. **What it can do uniquely: read
  filings with no tape competing, and run controlled instrument experiments with the price frame frozen**
  — which is how `C11` was resolved on 08-22 and how `R96` was measured today. **Both of this desk's last
  two genuine instrument findings came from closed sessions.**
- ★ **A one-directional correction to a two-directional bias is worse than no correction**, because it
  converts a symmetric error into an asymmetric one (§7, consequence 2).

### The dig list ranked for today (candidate DEEP assignments)
1. **The refiner CONTRACT question** (`module_disclosure_us MPC`) — 4th run unopened, `P70` MISS makes it
   binding, **and a closed market is the right session for it.**
2. **`D295` / `S103`'s `NVDA` bands** — 4th run, print in **three days**, last run with slack. ALPHA.
3. **`SECTOR_DEEP_SEMI` at 39 days** with 4 of 11 book names inside it and `NVDA` reporting 08-26 — a
   reconciliation-driven DEEP candidate for ROTATION.
4. **Jackson Hole's absence from `catalyst_calendar`** — `S112` covers the event; the **tool** does not.
5. **`D297`** — `GOOG`/`GOOGL` double-counting makes the Alphabet complex **76.6%** of COMM while
   `top1_w` reports 38.3%. Unfixed and it silently understates a flipper risk.

---

## §10 · What this run asserted and then refuted — written down, not edited away (`§4c`, `D48`)

**One, and it is the reason `R96` exists rather than a quiet edit.**

This run's own PREFLIGHT drafted its §1 heading as *"the contamination is selection-biased upward,
confirmed with names"* — i.e. it set out to **confirm** the inherited conclusion and to supply the names
the 08-22 run could not. **The names refuted the conclusion they were collected to support.** Three
tickers moved up and three moved down; the inherited direction did not survive its own confirmation.
**The heading was rewritten to "bidirectional", the inherited wording was quoted in full beside the
correction rather than replaced, and `R96` was filed against a claim this desk made yesterday.**

★ **The useful part is the mechanism, not the modesty**: the check was designed to *supply evidence for*
an existing belief, and it worked as a falsification test only because the raw output was persisted
instead of summarised. **The 08-22 run's single procedural mistake — not persisting run 1 — is what
made its conclusion unfalsifiable for a day.**

⚠ **Zero self-refutations would not have been a good sign.** Per the standing note, a run that reports
none usually means its controls were not adversarial.

---

## §11 · RESEARCH triggers loaded as binding constraints — which group binds which stage

| Group | Fires when | IDs | Binds, this run specifically |
|---|---|---|---|
| **C** | you cite a number | C1 baseline · C2 both halves · C3 unknown column · C4 "indistinguishable" · C5 arbitrary choice | **MACRO + every stage.** ⚠ **`C4` is live in §4** — n=11 forbids a selection-edge claim **in either direction**, and §4 now records *why* n is not growing. ⚠ **`C5` is live in G4** — the risk-unit `dist 0.65` threshold does all the work; at 0.40–0.60 **all three windows agree on 12 units**, and only the selected 0.65 splits them |
| **S** | you make a statistical claim | S1 date-fold · S2 diagnose the null · S3 power first · S4 in-sample≠done · S5 short samples · S6 future labels | **§6 above.** `n_eff` and Bonferroni applied; `vol_surge` is the only axis quoted and it is quoted **as a KR result**. ⚠ **`S5` fires on G4** — the tool's own warning that ARI moves opposite to fit |
| **D** | you read data | D1 second venue · D2 proxy sign · D3 signed vs unsigned · D4 regime contamination · D5 cross-provider · D6 signal grade (OBV is C) | **SWEEP · ALPHA · DEEP.** ⚠ **`D6` binds §1** — `C11`'s resolution on 08-22 did **not** promote OBV; every citation still names instrument and quantity. ⚠ **`D5` carried from `D307`** — a settled-price citation used to score a bracket records its pull timestamp |
| **W** | you write a conclusion | W1 cross-market transfer · W2 inherited lead/lag · W3 real≠profitable · W4 name the customers · W5 sub-sector dispersion · W6 reader's-market spine | **DEEP · BET · ROTATION.** 🚨 **`W1` is the binding constraint of §6** and it fires a **second** time in §1 on `R94`/`R95` — the KR half-window measurement is carried as a *question*, never as a US fact. **`W5`**: `WMT`/`TGT` at **17.1pp** intra-sector. **`W4`: `RTX`'s customer unmeasured for 206 days** |
| **L** | lenses, not triggers | L1 second derivative · L2 peak-margin trap · L3 branch information content | **DEEP · PREMORTEM.** ★ **`L2` is the live one** — the refiner CONTRACT dig exists precisely to test whether peak margin is structural. **`L3` binds PREMORTEM**: do not register another row whose only informative branch needs a 15pp reversal from a 100th-percentile state (`S88`'s C bought little) |

---

## ✅ EXIT CHECK

- [x] Spine `STANDING_VIEW.md` (through **`R95`**, incl. this morning's KR block) + `SCENARIOS.md`
      (through the 08-23 KR log) **in full**, plus `STANDING_VIEW_US.md`, `SCENARIOS_US.md`,
      `RESEARCH.md` read. **`SCENARIOS_KR.md` opened** — verified it holds **no** past-dated row
      (earliest KR settle **09-04**).
- [x] **Retracted ledger read BEFORE forming today's view.** Eight binding entries listed, including the
      two (`R94`/`R95`) appended by the sibling desk hours before this run, **with an explicit statement
      of which half transfers under `W1` and which does not.**
- [x] **Every past-dated scenario scored or explicitly dispositioned** — **0 due, verified by an
      exhaustive settle table (§2a) rather than asserted**; `S102` not-yet-arrived with a 5×-replicated
      structural reason and a named successor run; `S8` named for the **22nd** time.
      **`EXPIRED` 0 · silent skips 0.**
- [x] **`reject_ledger.py due` run** — **0 due, 0 legacy** (2nd consecutive clean run; legacy 0 for 12).
- [x] **`missed_ledger.py due` run** — **0 due, 0 legacy**; all four 08-22 rows verified closed, and
      **both** written pre-commitments (`APH`, `009830`) confirmed honoured. Sign inversion respected;
      the two ledgers are never summed.
- [x] **Exposure state read and carried** (§4) — **정상**, target **95%**, current **blank in `state`**,
      ledger band gap **−9.9pp (live bar)**, cumulative **−16.64pp = cash −6.46 + selection −10.19,
      n=11**. Not a cold start (38 rows). `투자비중미상` reported 🚨 with **no number substituted**.
      **★ And the reason n is frozen is measured and registered as `D323`.**
- [x] 🚨 **Instrument health inherited before any number was trusted** (§0) — `PREFLIGHT_US.md` run,
      **PASS 3 / FAIL 5**, rights table binding, with the **zero-new-sessions** constraint propagated as
      the first revocation.
- [x] **Self-refutation written down, not edited away** (§10) — one, and it produced `R96`.
- [x] **Stale rows flagged with dates; every cleared obligation converted into a dig or discharged**
      (§9) — two discharged (`M704` ex-`LHX`, `APH`), four carried with run-counts, two new digs filed.
- [x] `[measured]` / `[inferred]` tags preserved. The regime call is carried **`[inferred]`** and is not
      cited as evidence anywhere in this packet. **The entire per-name table is stamped as INHERITED,
      not re-measured**, because reproducing an identical frame under a new date would be manufacturing.
- [x] **RESEARCH triggers loaded as binding constraints, grouped C/S/D/W/L**, with the stage each binds
      **and the specific rule that fired this run** named (§11) — not summarized.
- [x] `HANDOVER.md` written. `handoff/*.md` to be updated **at run end** (append-only for `R96` and
      `D322`–`D323`), per the protocol.
- [x] **No position sizing, no buy/sell language anywhere in this packet** (P4).
