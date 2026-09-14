# HANDOVER — industry_US · 2026-08-15 (Sat KST) · Stage 2/11 (L1·HANDOVER)

> Inheritance only. No sizing, no buy/sell language (P4). This stage transports what the desk already
> believes, scores what has matured, and states what today's instruments forbid.

## 0. Run clock, and the three structural facts that define this run

| | |
|---|---|
| Run clock | **KST 2026-08-15 22:10–… = ET 2026-08-15 09:10–… — SATURDAY, US cash closed** |
| Price asof | **2026-08-14 settled close** (Friday). No live bar can intrude — `D74` is **structurally impossible** today, the first run this year that can say that rather than measure it |
| Δ baseline | `history.json["2026-08-13"]`, same 3-axis mode ⇒ **Δ = exactly one settled session (08-13 → 08-14)** |

**Three facts shape everything below.**
1. **This is a weekend run.** Two of the desk's recurring instrument failures (intruding live bars,
   intraday stubs) cannot occur. The tape is fully settled and the desk should spend the run on
   *reading* rather than on *pinning*.
2. **The news instrument's diagnosis inverted today** (PREFLIGHT G1). Yesterday the desk concluded
   "both bridges are down." Today's n=40 re-probe of the *silent* names returned **34 valid · 6
   pipe-fail · ZERO genuinely quiet**. The sweep's 83% silence is **100% instrument, 0% world**, and
   the library path is alive at probe rate. **A right was restored, with conditions** (§6).
3. **Nothing matures today.** Every ARMED US bracket settles **08-19 or later**; `EXPIRED = 0`;
   both ledgers' `due` lists are **empty with legacy count 0**. This is the first run in weeks with
   no scoring obligation — which makes it the run with the least excuse for a thin DEEP.

---

## 1. Inherited regime call — carried verbatim, tag intact

> **Memory is a price-cycle industry in rate-of-change deceleration while its level stays tight.**
> `[inferred]` — built on the measured chain `M1`–`M9`, `M18`, `M143`.

The distinction that drives everything: in a commodity-cycle industry the equity tracks the **second
derivative of price**, not the level. Level and rate point opposite ways, which is why "shortage
persists" and "the stocks struggle" are both true and not contradictory.

⚠ **`[inferred]` may be carried; it may not be cited as evidence for a new proposition.** Any stage
that leans on the regime call must name the measured row underneath it, not the call.

**The superseding mechanism carried from 08-14 — `P56`, and it is the live macro object:**
the long-end repricing is **term premium**, not a real-rate *level* move (`M653`: 30y−10y +0.48 →
+0.56 with `DGS2` **unchanged**; `M654`: breakevens **falling**, HY OAS flat, NFCI loosening — none of
the three usual channels confirms). `P51`'s call was scored **HIT** and `P56` replaced its stated
cause while keeping its sign. ⚠ `P56` carries a **named competing explanation** since 08-14: a
geopolitical driver (*"Treasury yields rise as U.S. threatens Iran with more economic sanctions"*
[`cnbc` 08-14]). **Its `[inferred]` tag stands.**

---

## 2. Sector verdict board inherited from 2026-08-14 (unchanged until ROTATION acts)

| Sector | Verdict | Carried because |
|---|---|---|
| **ENRG** | **OW−** | Board's only positive `wflow`; **promotion to OW declined twice** on Δ −0.157 (2nd worst) |
| **INDU** | **OW−** | `D249` unresolved for a 3rd run — the bracket measures `XLI`, the position is **defense** |
| **IT** | **N+** | **Promoted 08-14** on `eqflow` sign-flip −0.100 → +0.034 and Δ +0.152; counter-evidence stated (adjusted 2🟢/10🔴, `wflow` = `NVDA` alone) |
| **HLTH** | **N** | **Demoted 08-14** on Δ −0.228 (worst of 11, 3rd consecutive deceleration) — the *change*, not the level |
| **FIN** | **N−** | **Demoted 08-14**; the demote **reverses `M40`** (`R69`) after 22 days |
| **MATR** | **N−** | Flipper (`LIN`); every permitted axis refuses |
| **DISC** | **N−** | Covered 08-03 = **8 runs, the longest gap on the board** |
| **COMM** | **UW** | Δ +0.185 (best of 11) vs exc60 −9.098 (worst of 11) ⇒ C3, both directions blocked |
| **STPL** | **UW−** | Δ −0.221 (2nd worst) — the notch was declined **on notation only** |
| **UTIL** | **UW** | Mechanism changed under it (`P56`) without changing the sign |
| **RE** | **UW** | The board's most internally consistent verdict — every axis agrees |

**Last DEEP:** ENRG 08-14 · INDU 08-14 · COMM 08-14 · FIN 08-14 · IT 08-13 · HLTH 08-13 · MATR 08-13 ·
UTIL 08-12 · STPL 08-10 · RE 08-04 · **DISC 08-03**.
⇒ **Recency-ranked candidates for today's rotating slots: DISC (8 runs) · RE (7 runs) · STPL (4 runs).**
ROTATION owns the decision; this stage only reports the clock.

---

## 3. Scenario status — **EXPIRED = 0 · silent skips = 0**

### 3a. Matured this run
**None.** Every US-owned bracket carries an event date of **08-19 or later**. Verified by scanning
`SCENARIOS_US.md` for in-window dates: the only 08-1x dates present are **registration** dates
(08-10 · 08-11 · 08-12 · 08-13 · 08-14) and the **08-19** settlement cluster.

### 3b. ARMED, with dates — the forward clock

| Settles | IDs | What they test |
|---|---|---|
| **2026-08-17** | `S51-KR` · KR `S38` follow-ups | KR-owned; the KR desk scored `S38` and `S48-KR` **early** on 08-15 (observable printed 08-12) |
| **2026-08-19** | **`S75` `S76` `S77` `S78` `S80`** | HLTH · MATR · FIN · UTIL falsifiers |
| **2026-08-20** | **`S82` `S83`** | `S82` is **already above its branch A at +3.091** |
| **2026-08-21** | **`S84` `S85` `S86` `S87`** | ★ `S84` is the **mandatory Hormuz both-sides bracket**; `S85` falsifies the **same run's IT N→N+ promotion on the axis the promotion used** |
| **2026-08-24** | `S74` | |
| **2026-08-26/27** | `S79` · `S81` (+ NVDA print) | |

★ **`S85` deserves naming today.** It was registered as the falsifier for the IT promotion, and its
state at registration was **+1.980, already above p85 of its own justifying estimator** — disclosed at
registration rather than discovered later. **IT's N+ is therefore held at the 85th–95th percentile of
the very statistic that justified it.** Any stage tempted to add to IT today should read that line first.

### 3c. 🚨🚨 `S8` — undated, un-scoreable, **THIRTEENTH consecutive run**
`S8` remains `[blank]`-dated and cannot be settled by any desk. The KR run named it this morning as
its 12th; this makes **13**. **A human must `VOID` it or re-register it with a date (P5).**
**Named again, not dropped.**

---

## 4. Both ledgers audited — and both are clean for the right reason

| Ledger | Total | Resolved | **Legacy (no revival/entry condition)** | **Due now** |
|---|---|---|---|---|
| `reject_ledger` | **169** | 88 | **0** | **0** |
| `missed_ledger` | **126** | 49 | **0** | **0** |

★ **The legacy count is the number that matters and it is 0 on both sides.** This desk's most
expensive measured error (`SK이터닉스`, **+41.2pp and +26.9pp**) happened because 24 of 25 rows had no
`revives_if` at all, so "any row whose condition has come true" was unstatable. That hole is now
**closed on both ledgers, and held closed for a second run** (`D258`'s three tanker rows were the last
of them, re-filed 08-14).
⚠ **A clean `due` is not evidence of health on its own** — it is evidence here only because the legacy
count is 0 and the totals are still growing (169/126). **Both conditions must be reported together.**
⚠ `missed_ledger`'s `excess` sign is **inverted** relative to `reject_ledger`; the two are never summed
without aligning signs. And its `score` block is still **outcome-selected** (the first 6 rows were
harvested from `leak_scan --top`) — quotable as accumulation, never as an edge.

---

## 5. Exposure state — carried as size context, not as a gate

`scripts/exposure_rule.py state` · benchmark `069500.KS` · asof **2026-08-14 settled**

| Item | Value |
|---|---|
| Rule state | **정상 / normal** (previous: normal) — no firing condition met |
| Target invested | **95%** |
| **Current invested** | 🚨 **UNKNOWN — the account query did not run**, so the band gap cannot be computed today |
| Ledger rows | **35** (10 shown) |
| Cumulative decomposition (n=8) | **total excess −14.21pp = cash −6.26pp + selection −7.95pp** |
| Last measured band gap | **−27.0pp** (08-14, live bar) |

🚨 **Reported as unknown, not substituted** (P5). The state machine is **not** cold-starting (35 rows),
so the `정상` verdict itself is usable; the **invested %** is not.
★ **The decomposition is the line BET/ALPHA must carry**: over the accrued window the desk is behind on
**both** legs — cash weight −6.26pp *and* selection −7.95pp — so "we were defensively positioned" does
not explain the shortfall. ⚠ **n=8.** At this n the split is not distinguishable from zero (C4); it is
reported to make the n grow, not to be acted on.
⚠ Standing alarm on every row: **`TIMEFOLIO_EXECUTE=1` is ARMED**. Analytical desks never pass
`--execute`; this run does not.

---

## 6. Instrument health inherited from PREFLIGHT — **the binding table**

Read `llm_outputs/2026-08-15/preflight/PREFLIGHT_US.md` (written **before** this stage). **PASS 3 /
FAIL 5.** The gate table is a rights table, and these are the rights:

| Stage | 🚫 Cannot use today |
|---|---|
| SWEEP | the sweep's velocity axis · **the 51 survivors** · theme freshness · "quiet" · stale (31-day) caps described as current · any verdict on `EA` |
| EVENT_ALPHA | "theme is fresh/cooled" from `theme_age`/`chain_hop` · **`news_vectors.db` content after 2026-08-13** |
| ROTATION | **`wflow` promotion/demotion for IT · Industrials · Materials** (G3 flippers) |
| PREMORTEM | "the tape has gone quiet on this risk" — **measured: 0 of 40 silent names were quiet** |
| DEEP | the velocity axis as an axis · "no news flow" as evidence |
| BET/SIZE | single-number concentration · `--ic`-backed size (→ **"mechanical ¼"**) · `AVGO/NVDA` and `ANET/ETN` unit counts |
| DRIFT | **must report that its instrument was dead** — an empty burst list today is not "no drift" |

**✅ What is available, stated positively.** Settled prices through **08-14** with fine-grain RS (G0
clean, 3rd run) · OBV · **eqflow / breadth** (unweighted, so the 31-day-stale caps barely touch them —
they carry more load today, not less) · `vol_surge` **both directions** · FINRA short pressure · CFTC
COT percentiles · `[FRED]` · primary filings · `margin_history`.

★ **One right RESTORED today, and it changes what EVENT_ALPHA and DEEP can do.** Per-name news
velocity **may** be cited when the stage runs `flow_read.news_velocity` for that specific name and
writes the returned **7d/30d counts on the same line as the claim**. Warrant: **85% success at probe
rate, 0% false silence, n=40.** Two limits travel with it: it is an **article-count ratio, not
content**; and a name that fails the probe is **unmeasured, not quiet**.

⚠ **One thing PREFLIGHT could NOT explain, carried openly:** the 51 velocity survivors are the **same
51 tickers as 08-14** (set identity exact) with **48 of 51 values changed**. Random rate-failure does
not reproduce an identical survivor set two days running, and it is not article volume (`NDAQ` returns
3,895 articles and is a non-survivor) nor caching. **The selection mechanism is unmeasured.** This is
registered below as a dig rather than papered over.

★ **Carried instrument defect that binds every stage: `D261`.** `flow_score` is **3-axis** while
`flow_tag` is **4-axis**, and `§scoring` says nothing about it. On 08-13, **5 of 11 🟢 could only be
lit by the revoked velocity axis** — a **2.6× over-representation** of a 17%-coverage survivor sample —
and one of the five was `NVDA`, **which is also the G3 flipper owning IT's sign**. **SWEEP must
re-run that decomposition on today's greens before any stage counts a green.**

---

## 7. Method rules loaded as binding constraints (`handoff/RESEARCH.md`)

| Group | Fires when | IDs | Binds today |
|---|---|---|---|
| **C** | you cite a number | C1 baseline · C2 both halves · C3 unknown column · C4 "indistinguishable" · C5 arbitrary choice | **MACRO · every stage.** ★ C1 binds hard today: every excess return names `SPY` inline |
| **S** | you make a statistical claim | S1 date-fold · S2 diagnose the null · S3 power first · S4 in-sample≠done · S5 short samples · S6 future labels | **any stage citing a test.** S5 binds `risk_units --days 250` (249 < 250 sessions) |
| **D** | you read data | D1 second venue · D2 proxy sign · D3 signed vs unsigned · D4 regime contamination · D5 cross-provider · **D6 signal grade (OBV is C)** | **SWEEP · ALPHA · DEEP.** ★ **D6 binds unusually hard today**: with the velocity axis revoked, the score rests on OBV (**C-grade**) + RS + `vol_surge`, so no DEEP verdict may rest on OBV alone |
| **W** | you write a conclusion | W1 cross-market transfer · W2 inherited lead/lag · W3 real≠profitable · W4 name the customers · W5 sub-sector dispersion · W6 reader's-market spine | **DEEP · BET · ROTATION.** ★ **W1 binds the IC finding in §8** and W5 binds every "sector" statement (`M666` Energy · `M667` Industrials · `M668` COMM · `M669` FIN are all one-label-two-businesses findings) |
| **L** | lenses (not triggers) | L1 second derivative · L2 peak-margin trap · L3 branch information content | **DEEP · PREMORTEM.** L2 currently fires on **`MU` alone** (`M670`: `MPC` is at its **median** 10.0% vs 10.5%, not its peak) |

---

## 8. The signal scoreboard — and the transfer trap sitting on it

`scripts/ic_ledger.py score` — **21 tests · 404 ledger rows · KR universe**

| Axis | h | n | n_eff | mean IC | t(NW) | Verdict |
|---|---|---|---|---|---|---|
| **`vol_surge`** | **1** | 26 | **26.0** | **−0.0481** | **−3.20** | ★ **significant, clears Bonferroni (\|t\|>2.8)** |
| **`vol_surge`** | **5** | 21 | **4.2** | **−0.0405** | **−2.90** | ★ **significant, clears Bonferroni** |
| `obv_norm` | 5 | 21 | 4.2 | −0.0738 | −1.70 | indistinguishable |
| `rs60` | 5 | 20 | 4.0 | −0.1428 | −1.46 | indistinguishable |
| `flow_score` | 5 | 21 | 4.2 | −0.0814 | −1.25 | indistinguishable |
| *(14 of 21 cells)* | | | **< 4** | | | 🚨 **unquotable — overlapping windows** |

★ **The standing item, now stronger than when it was written.** `vol_surge` is the **only** axis with a
consistent sign across two horizons **and it now clears Bonferroni on BOTH** — with a **NEGATIVE** sign,
meaning a high volume surge predicted **lower** forward returns. **`sector_flow` still weights it
positively**, and it is the axis that decides the 🟢 gate. Six sectors' green counts are therefore lit
by a statistic whose measured sign is backwards.

🚨 **And here is the trap, stated before anyone reaches for it: this ledger is KR.**
**`W1` forbids importing a cross-market conclusion**, and this desk logs W1 violations as its most
common failure. `D243` records that **the US desk has no IC column at all** — so the correct statement
today is *"the US `vol_surge` weighting is **unmeasured**, and the only market where it has been
measured says the sign is backwards."* **That is a dig, not a gate flip.** No stage flips the gate today.

---

## 9. Dig list, ranked for this run (`RESEARCH.md` Part C · highest existing ID **D264**)

| Rank | Dig | Why it is today's |
|---|---|---|
| **1** | **`D249`** — the INDU bracket measures `XLI` while the position is **defense** | **Unresolved for a 4th run.** INDU is a continuous OW− slot; the desk cannot keep holding a tilt whose falsifier measures a different object (defense EW exc20 **+7.81** vs `XLI` **+0.89**) |
| **2** | **`D261`** — tag/score axis mismatch | **Binds every green count in this run.** SWEEP must decompose today's greens before ROTATION counts one |
| **3** | **`D243`** — the US desk has **no IC column** | §8 shows exactly what its absence costs: the desk cannot say whether its own gate axis has a sign |
| **4** | **`R56` / `EA`** — delisted 08-04, **still in `us_top300` at day 31**, still scored 08-13 | **8th consecutive run.** Today it finally dropped out of the scored set (299/300) — so the defect changed shape and should be re-stated, not re-copied |
| **5** | **`D250`** — `cycle_registry.json` **28 days stale**, rank-3 floor `0.0` ⇒ check **OFF**; no entry for either cycle the desk found (optical/interconnect, custom AI silicon) | PREMORTEM Lens 4 runs on a registry that has no row for the two live cycles |
| **6** | **`D254`** — the `🟢LIVE` gate is an **off switch**, not a filter (age ≤14d on a 90-day corpus) | Carried; the KR desk independently reproduced it (`D250-KR`, 19 consecutive zeros) |
| **7** | **`D264`** — a pool-normalised burst check can still return a **false all-clear** | **Binds DRIFT directly today**, and the client store is thin again (§10) |

**New digs from this stage → `D265` onward** (3-grep performed at write time: highest existing is
**D264** un-suffixed, **D256-KR** suffixed):

| ID | Dig | Owner |
|---|---|---|
| **D265** | ★★ **The velocity survivor set is IDENTICAL across two runs while its values change — the selection mechanism is unmeasured.** 51/51 same tickers on 08-14 and 08-15, 48 of 51 values different; not volume (`NDAQ` 3,895 articles, non-survivor), not caching. A random rate-failure cannot produce this. **Positive-form remedy: log the per-call outcome inside `sector_flow` (ticker, elapsed, note) so the survivor set can be explained rather than inferred** | **idle_probe** (characterise) · **PREFLIGHT** (report the set-identity check) |
| **D266** | ★★ **The client news store's sync cursor froze while its mtime kept moving.** `news_vectors.db` cursor is stuck at `2026-08-14T07:59:45` — byte-identical to 08-14 — with 08-14 holding only **487 rows** against 8,000–9,000 on normal days, yet the file's mtime advanced to 08-15 10:56. ⇒ **the entire Friday 08-14 US session is unwitnessed locally** while the remote corpus is demonstrably fresh (`NVDA` 7d = 1,407). **Positive-form remedy: `--status` prints the cursor age and the last day's row count next to the file mtime, so a frozen sync cannot look like a live file** | **human** (sync) · **DRIFT** (route through the live index per `D264`) |

---

## 10. §4c — verification that arrived after the assertion (D48 class)

**This stage's own count: 1.**

🚨 **HANDOVER §6 nearly inherited a refuted diagnosis.** The 08-14 rights table concluded *"both
bridges are down"* and this stage was drafting that forward as today's constraint. **The PREFLIGHT
re-probe run minutes earlier refuted it**: the CLI path is dead 5/5, but the **library** path — the one
`sector_flow` itself calls — answered **34 of 40** on names the sweep had recorded as silent, **0 of
which were genuinely quiet**. ⇒ **The inherited sentence was not wrong about the CLI; it was wrong
about "both."** Written here rather than edited into §6, per §4c. The practical consequence is a
**restored** right, not a lost one — which is why it had to be caught: inheriting the pessimistic
version would have silently cost this run its only remaining news axis.

⚠ **Stated plainly: one self-refutation in a stage that ran two independent probes is a low count.**
Per §4c a *zero* usually means the controls were not adversarial; one is not much better. The stages
below should assume this stage under-tested itself rather than that it was clean.

---

## ✅ EXIT CHECK

- [x] **Shared spines read in full** — `STANDING_VIEW.md` (regime call §1, measured chain §2, §5
      retracted ledger through `R69`, asof chain) + `SCENARIOS.md` (MASTER scoring log incl. the
      **08-15 KR entries**, MASTER INDEX = **101 brackets, 75 US / 26 KR**) + this desk's
      `STANDING_VIEW_US.md` (§2 `M653`–`M672`, §3a per-name rows) + `SCENARIOS_US.md` +
      `RESEARCH.md`. **The other market's file WAS opened** — `SCENARIOS_KR.md` / the KR half of the
      scoring log — and confirmed to hold **no past-dated row this run must score** (`S38` and
      `S48-KR` were settled by the KR run this morning, two days early).
- [x] **Mechanical ledger cross-queried** — `module_report_tags show`. ⚠ **Reconciliation delta
      found**: the ledger's `industry_US` entries are dated **2026-08-12** for most files while the
      `industry_KR` entries are current to **08-15**, i.e. the **08-13 and 08-14 US runs wrote into
      dated subfolders** (`REPORT/industry_US/2026-08-13/`, `/2026-08-14/`) rather than refreshing the
      flat files the ledger indexes. **Named here; this run copies to the flat path per the protocol's
      resolved open decision.**
- [x] **Retracted ledger read BEFORE forming any view.** `R69` (the `M40` Financials-breadth reversal)
      is the live one; **`R56`/`EA` is carried as an open defect, not a belief**. No claim below
      resurrects a retracted entry. ★ Note `R69` withdrew *"the board's only breadth-led sector"* as a
      property **of Financials** — it did not assert Financials has no breadth (`M669` relocated it to
      alternatives/asset-management). Any stage re-arguing FIN must respect that scope.
- [x] **Every past-dated scenario scored or `EXPIRED` with a reason.** **Zero matured today**;
      `EXPIRED = 0`; silent skips = 0. `S8` named for the **13th** run.
- [x] **`reject_ledger.py due` run** — 0 due, **legacy 0**, 169 total / 88 resolved.
- [x] **`missed_ledger.py due` run** — 0 due, **legacy 0**, 126 total / 49 resolved. Sign inversion
      stated; the two are not summed.
- [x] **Exposure state read and carried** (§5) — verdict `정상`, target 95%, **invested % 🚨 unknown
      and NOT substituted**, cumulative **−14.21pp = cash −6.26 + selection −7.95 on n=8**. Not a cold
      start (35 rows).
- [x] 🚨 **Instrument health inherited before any number was trusted** — `PREFLIGHT_US.md` read; the
      binding table is §6 and it revokes five things and restores one.
- [x] **A claim asserted and then refuted is written down, not edited away** — §10, one instance.
- [x] **Stale rows flagged with their `asof`** — `us_top300.csv` **31 days** · `cycle_registry.json`
      **28 days** (rank-3 floor 0.0 ⇒ check OFF) · `news_vectors.db` cursor **frozen at 08-14 07:59**.
      No suspension cleared this run, so no suspension converted to a dig.
- [x] **`[measured]`/`[inferred]` tags preserved.** The regime call and `P56` travel as `[inferred]`
      and are not usable as evidence.
- [x] **RESEARCH triggers loaded as binding constraints, grouped C/S/D/W + L** (§7), with the stage
      each group binds named.
- [x] **No sizing, no buy/sell language anywhere in this file** (P4).
- [ ] `handoff/*.md` writeback — **deferred to run end** (append-only), per the stage's own instruction.
