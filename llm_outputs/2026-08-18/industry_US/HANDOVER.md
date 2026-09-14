# HANDOVER — industry_US · 2026-08-18 (Tue KST) · Stage 2/11 (L1·HANDOVER)

> Inheritance stage. Transports analysis, never a recommendation (P4). No sizing, no buy/sell language.
> Run clock **KST 22:10– = ET 09:10–, Tuesday, US cash pre-market** (bell 09:30 ET = 22:30 KST, mid-run).

---

## 0. Instrument health inherited BEFORE any number is trusted

`llm_outputs/2026-08-18/preflight/PREFLIGHT_US.md` **was run** (filename deviation logged there for the
9th run; `PREFLIGHT.md` in that folder belongs to this morning's `industry_kr` desk).

**PASS 2 / FAIL 6.** The rights this run inherits:

| Gate | Verdict | What this run may NOT claim |
|---|---|---|
| **G0** bar completeness | 🔴 **FAIL — new defect class** | **No 08-17 price, close or return, anywhere.** No "as of today/Monday". `module_chart --read` RSI / Bollinger / momentum / MA-position are NaN and may not be cited |
| **G1** news axis | 🔴 FAIL (6th run) | The sweep's `velocity` field · the 50 "survivors" as a set · any theme-freshness or "went quiet" claim from the sweep · `breadth` as a news-independent statistic. **"No news found" may not be written** |
| **G2** scale continuity | 🟢 PASS (literally) | No Δflow called "today's change" (5th replay of one interval) · no promotion on a `flow_score` gap ≤0.01 (measured revision noise) |
| **G3** sector sign | 🟢 PASS | No promote/demote of **IT · Industrials · Materials** on weighted `wflow` (3 of 11 flip on top1) |
| **G4** risk units | 🔴 FAIL (9th) | No concentration statement as a single number; the `--days` window goes on the same line as the conclusion |
| **G5** universe | 🔴 FAIL | No flow/RS/OBV/short judgement on **`EA`** ("not measurable", not "no signal"); every mcap weight is **34 days stale** |
| **G6** estimate accrual | 🔴 FAIL | No `--ic` size presented as evidence-based ("mechanical ¼" if it appears at all) |
| **G7** tool liveness | 🔴 FAIL (9th) | `module_chart` and `margin_history.py` citable only on their working command lines |

### 0a. The one structural fact that governs this whole run

**A US session settled for the first time in five runs — and this desk cannot read it.**
08-17 (Monday) was a full session: the tape printed, and the frame carries **300/301 volumes summing to
1.78 bn shares**. But **Close is NaN for 300 of 301 names**, so the sweep is anchored, again, to the
**2026-08-14 (Friday) close — the fifth consecutive run on the same terminal bar.**

This is *not* the same situation as the previous four replays. Those four had **no new information in
existence**. Today the information exists and the instrument cannot fetch it. Every downstream stage
must say **"unreadable"**, not **"unchanged"** — they are different claims and only the first is true.

⚠ **Binding on the 08-21 settlements.** `S95`–`S97` and `S84`–`S91`, `S93` all settle on a **5-session
excess window 08-14 → 08-21**. That window now contains **one session this desk cannot price today**.
Nothing needs re-registering — the settle date reads the close from a later pull — but no stage may
claim distance-to-branch progress today.

---

## 1. Inherited standing view (`STANDING_VIEW.md` + `STANDING_VIEW_US.md`)

**Regime call, carried unchanged:** *memory is a price-cycle industry in rate-of-change deceleration
while its level stays tight* `[inferred]`. The distinction that drives it — equity tracks the **second
derivative** of price, not the level — is why "shortage persists" and "stocks struggle" coexist.

Carried structural anchors, tags preserved:
- `M1`–`M9` the memory chain `[measured]`; `M18` MU gross margin **84.6% = 100th percentile of 17 years,
  +25.7pp above the prior-cycle peak** `[measured]` — the lens-L2 (peak-margin) instrument for the board.
- `M19` estimate-revision IC: folded **+0.32**, Q5−Q1 **+19.5pp**, **verdict "indistinguishable"**
  because Q5 is 72% IT / 39% semis and effective dates = 1. ⚠ Still `[inferred]` as a tradable edge;
  it may be carried, it may not be cited as evidence.
- `M25` the US 🟢 tag is a **volume-surge count, not a flow count** — with `velocity` dead, 🟢 requires
  OBV ∧ RS20>0 ∧ `vol_surge`≥1.2. ★ This binds hard today: the board shows **11 🟢 / 60 🔴 of 299**, and
  that ratio is a `vol_surge` statement, not a money-flow statement.
- `M704` / `D249` defense-vs-`XLI`, **upgraded** by `M719` (+4.32pp on 60 days with `LHX` removed).
- `R73` withdrew the term-premium **level** mechanism under the UW-duration complex (`XLU`/`XLRE`/`XLP`
  ± `XLV`): the measured shape is a **bull steepener**, which is a tailwind, not a drag. `S98` (08-20)
  is the row that settles whether that underweight is four legs of one bet.

### Retracted ledger read BEFORE forming today's view (§5)

Most recent US retractions `R76` · `R77` · `R78` (all 2026-08-17), plus this morning's KR
**`R77-REARGUED`**. Nothing in today's PREFLIGHT resurfaces a retracted claim. Two direct interactions:

1. **`R77-REARGUED` is confirmed by this run's own measurement, on the US side, and the KR desk's
   caveat is now closed.** The KR desk wrote that it *could not check whether the US 22:14 measurement
   shared the same counting defect*. It does not: today's US probe counted on `velocity is not None`
   from the start, and read **0/40**, then **0/41 over 92 seconds**, then **40/40** minutes later. The
   "tens-of-seconds block" pattern KR measured this morning (29 X → 13 O) reproduced here as a **single
   unbroken block of 41 failures**, on a different market, a different corpus and a different clock.
   ⇒ `R77`'s corrected diagnosis ("the failure attaches to the sweep as a usage pattern") stays
   **incomplete**, exactly as KR argued: today the failure attached to a **standalone, zero-load,
   two-second-interval probe**. Both patterns exist.
2. **`R78`'s lesson (a 🟢 built on the revoked axis) is pre-empted this run**: `tag` is again
   news-contaminated — `ORCL` and `MRVL` moved 🟡→🟢 on **byte-identical price data**. No stage may
   promote on a tag today.

### Open contradictions carried deliberately (§6) — not resolved by picking a side

- **`D261` / `M701`** — `breadth` and `tag` bypass the axis-drop guard while `flow_score` does not.
  Measured a third time today. Carried, not resolved.
- **`D279`** — a story that never left cannot burst, so `theme_age` and `burst` fail *together* on
  precisely the standing risks that matter. 🚫 Standing constraint: **no stage may read a low
  `theme_age` or an absent `burst` token as evidence that a risk has receded.**
- **`D280`** — nothing stamps `n_new_sessions_since_prior_run`. Today is the run where that gap bites
  hardest: the honest stamp would read **1 new session, 0 readable**.

---

## 2. Scenarios — every past-dated row scored or explicitly marked

**Condition-check executed on every ARMED row. Result: zero US rows past-dated.**

- `SCENARIOS_US.md` opened in full — nearest settlements **08-19** (`S75`–`S78`, `S80`) · **08-20**
  (`S82`, `S83`, `S98`) · **08-21** (`S84`–`S91`, `S93`, `S95`–`S97`) · 08-24 (`S74`) · 08-26/27
  (`S79`, `S81`) · 08-31 (`S92`, `S94`).
- `SCENARIOS_KR.md` opened (the other market's past-dated rows are this run's to score): nearest
  **`S52-KR` 08-19** · `S57-KR` · `S63-KR` 08-20. `S51-KR` was settled **FIRED-C** by the KR desk on
  08-17. ⇒ **nothing past-dated on either side.**
- **`EXPIRED` = 0 · silent skips = 0.**

★ **But the reason is no longer purely mechanical.** For four runs the null result was guaranteed —
zero sessions had settled. Today **one session settled** and the null result holds only because no
bracket was keyed to 08-17 or 08-18. That is luck, not construction, and it is written down as such.

🚨 **`S8` — UNSCOREABLE for the SIXTEENTH consecutive run.** Undated `[blank]` Hormuz binary; still on
`CATALYST_WATCH` as an undated 🔀binary. **A human must `VOID` it or re-register it with a date (P5).**
`S95` now brackets the 60-day MoU expiry that `S8` could not, so the desk's dependence on it is falling —
but the row itself is still an open process failure and is named here rather than dropped.

---

## 3. Both ledgers audited — symmetric, per `carryover.md` §3c

### 3a. Rejection ledger — `reject_ledger.py due`
`183 total · 97 resolved · legacy rows with no revives_if: **0** · due/past-due: **0**.`
⚠ Not read as "the ledger is healthy": the **legacy count is 0 and has stayed 0**, which is the
evidence the practice took hold. Nothing due is a null result, recorded as a check.
⚠ `D281` stands open — the enum still has no `M.OBV분배` cell, so the desk's most common measured
rejection ground continues to be mis-filed as `D.약한손`, corrupting per-class scoring.

### 3b. Missed ledger — `missed_ledger.py due`
`152 total · 57 resolved · legacy: 0 · **4 past-due**.` ⚠ `excess` sign is **inverted** here; the two
ledgers are never summed without aligning signs.

| Row | Condition | Measured on the settled 08-14 close | Resolution |
|---|---|---|---|
| **HPE** (08-04) | RS20 >0 **and** days-21-60 segment positive | RS20 **+23.7** · segment **+50.5** (RS60 +74.2 − RS20) — and the name **is in the book** (`pulse`, AI-compute-chain, 58.71) | ✅ `entered` |
| **316140** (08-04) | 🟢 flip **∨** 5d foreign leg recovering +100k | KIS investor-leg read has **no US equivalent** (P5) — but the name **is held** (`pulse`, KR-bank-holding, 33,750) | ✅ `entered`, condition itself left unjudged rather than guessed |
| **VLO** (08-04) | *no named windfall instrument appears* **and** RS60 > +15 | RS60 **+24.3** ✅. Windfall leg, hand-probed `--scope foreign` 14d at ~22:5x KST: **calls only, no US instrument** — `"Trump faces calls for windfall tax"` [yahoo_finance 08-07], `"calls for windfall taxes rise"` [upi 08-12]. ★ A **named** instrument does exist but it is **India's**, and it moved **twice in 12 days**: raised 08-03, **cut effective Saturday** [investing_en 08-14] | ⏳ **FIRED — deferred within-run** |
| **EQIX** (08-04) | delta positive a **second consecutive** settled session | `history.json`: 08-12 **0.328** → 08-13 **0.411** (+0.083) → 08-14 **0.444** (+0.033). Two consecutive positive deltas ✅ | ⏳ **FIRED — deferred within-run** |

★ **Why two rows are deferred rather than resolved, and it is a grammar gap, not a skip.**
`missed_ledger resolve` offers `{entered, reaffirmed, expired}`. For `VLO` and `EQIX` the condition
**fired** and neither name is held — `entered` is false, `reaffirmed` ("stays out on fresh evidence")
is the opposite of what was measured, and `expired` is false. The KR desk hit the identical wall on
`073240` this morning and logged it as a 문법 갭. **These two are resolved at the end of THIS run
against what BET actually does with them** — a within-run deferral, not a carry into a second HANDOVER.
⇒ new dig **`D283`**.

### 3c. Exposure state — `exposure_rule.py show`
Last row **2026-08-14, `settled`, verdict 정상**, invested **67.9%**. Cumulative (simple sum, **n=8**):
**total excess −14.31pp = cash contribution −6.33pp + selection contribution −7.98pp**.
🚨 **밴드이탈 −27.1pp** flagged on that row. ⚠ `n=8` — the sign is not yet askable (C4); the reported
goal is +1 per day until n≈20. ⚠ Not a cold start (live rows exist since 07-31), so the verdict is
usable as context — but **as context for BET/ALPHA sizing only**, never as a recommendation (P4).

---

## 4. Coverage vs belief — `module_report_tags show` cross-read

Reconciled, not merged:
- **Heavy coverage, standing thesis present:** ENRG · INDU · IT · HLTH · STPL · RE · DISC · FIN · MATR ·
  COMM — every sector in the 11 has at least one `SECTOR_DEEP_*` on the ledger. **No unowned coverage gap
  at sector level.**
- **`SECTOR_DEEP_UTIL.md` is on the US ledger with an EMPTY summary line** — the ledger indexes a file
  whose heading extraction returned nothing. Utilities is also the board's **most negative sector**
  (`wflow` −0.445, `eqflow` −0.433, 0 🟢 / 7 🔴 of 15) and one of the four legs `S98` settles on 08-20.
  ⇒ a belief the desk holds strongly with a report the ledger cannot read. Flagged as dig **`D284`**.
- **`SECTOR_DEEP_SEMI.md` is dated 2026-07-15 — 34 days stale**, while the AI-compute epicentre is
  **three of the book's thirteen names** (`NVDA`, `AVGO`, `ANET`) and one of them (`AVGO`, −5.9% on the
  08-14 tape) is the book's worst single-day mover. Stale-flagged below.

---

## 5. Stale flags and cleared suspensions

| Item | `asof` | Age | Consequence |
|---|---|---|---|
| `us_top300.csv` | 2026-07-15 | **34 days** | every sector mcap weight, and the `top1_w` column that drives G3, is 34 days old |
| `SECTOR_DEEP_SEMI.md` | 2026-07-15 | **34 days** | the epicentre's own map is older than the universe file |
| Estimate snapshots | 2026-08-14 | 4 days | G6; ETA 2.4× ideal |
| Price frame | **2026-08-14** | 1 settled session behind | G0 — unreadable, not unchanged |
| `S8` | undated | **16 runs** | human decision required |

**Cleared suspension → dig instruction:** none cleared this run.

---

## 6. RESEARCH.md rules loaded as binding constraints (not summarised)

| Group | Fires when | Binds, this run specifically |
|---|---|---|
| **C** (C1 baseline · C2 both halves · C3 unknown column · C4 "indistinguishable" · C5 arbitrary choice) | any number is cited | **MACRO · every stage.** C1 bites hardest today: with one unreadable session, every "unchanged" must be re-derived against a stated baseline, not inherited |
| **S** (S1 date-fold · S2 diagnose the null · S3 power first · S4 in-sample≠done · S5 short samples · S6 future labels) | any statistical claim | **S5** binds `n=8` exposure and **S2** binds the G1 null: a zero is diagnosed, never reported |
| **D** (D1 second venue · D2 proxy sign · D3 signed vs unsigned · D4 regime contamination · **D6 signal grade — OBV is C**) | data is read | **SWEEP · ALPHA · EVENT_ALPHA.** With `velocity` dead and `vol_surge` the 🟢 gate, **OBV (grade C) is carrying more of the verdict than its grade licenses** — say so wherever it does |
| **W** (W1 cross-market transfer · W2 inherited lead/lag · W3 real≠profitable · W4 name the customers · W5 sub-sector dispersion · W6 reader's-market spine) | a conclusion is written | **DEEP · BET · ROTATION.** W1 is live: the DEEP budget stays **N=4** precisely because the KR desk's cut to N=2 was KR-measured |
| **L** (L1 second derivative · L2 peak-margin trap · L3 branch information content) | lenses, not triggers | **DEEP · PREMORTEM.** L2 has a named target already (`M18`, MU at the 100th percentile); L3 governs whether today's brackets are worth registering |

---

## 7. Dig list ranked for today (candidate DEEP assignments)

| Rank | Dig | Why it is today's | Routes to |
|---|---|---|---|
| 1 | **`D283` (new)** | the missed ledger has no verb for "condition fired, desk holds nothing" — two live rows are stuck on it right now | scripts owner · resolved in-run at BET |
| 2 | **`D285` (new)** | **the three-quarters bar**: every completeness check the desk owns is volume-based and passed a bar with no closes. A non-null-close count belongs in the sweep's own preflight, not in a human's eye | scripts owner · PREFLIGHT |
| 3 | **`D284` (new)** | `SECTOR_DEEP_UTIL.md` indexes with an empty summary while Utilities is the board's most negative sector and a leg of `S98` (08-20) | DEEP-UTIL candidate |
| 4 | `D279` | freshness instruments fail together on standing risks — binds every stage that would call Hormuz "cooled" | standing constraint |
| 5 | `D274` | universe union covers what the book **owns**, not what its theses **point at** (`HII` still outside) | human · BET |
| 6 | `D275` | 3-vs-3 cohort splits are descriptions of 6 names — re-run DISC/RE splits as full partitions with the classification fixed first | DEEP-DISC / DEEP-RE |
| 7 | `D280` | nothing stamps new-session count; today the honest stamp is **1 settled, 0 readable** | scripts owner |

---

## 8. Self-refutations recorded, not edited away (§4c / D48)

Two, both from this stage:

1. **This run's first news reading was "the tunnel is up" and its next command refuted it.** The CLI
   probe `fts search Nvidia --days 7 --count` returned **3769** at ~22:1x, which read as a working
   pipe; the sweep had *already* recorded 16.7% coverage minutes earlier, and the library probe then
   read **0/40**. The two instruments disagreed for ~15 minutes before the block was measured
   directly. The sentence "the news API is alive" was true of one path and false of the other **at the
   same clock time**, and only a timed probe separated them.
2. **The mitigation was drafted as "drop the bad last bar" and the measurement narrowed it.** The first
   framing assumed a stub (KR's failure mode). The field-by-field count showed the bar is not a stub at
   all — **volume is real and full-session** — so the truncation is dropping a bar the market genuinely
   traded, and the frame's terminal date understates what happened by one session. That is a different
   and worse condition than a stub, and the rights table says so.

⚠ Zero self-refutations would itself be a finding (it usually means the controls were not adversarial).
Two is the honest count for a stage whose main instrument broke.

## ✅ EXIT CHECK
- [x] Shared spines + `STANDING_VIEW_US.md` + `SCENARIOS_US.md` + `SCENARIOS_KR.md` + `RESEARCH.md` read;
      `module_report_tags show` cross-queried (§4).
- [x] Retracted ledger read **before** today's view; `R76`/`R77`/`R78` + `R77-REARGUED` interactions stated.
- [x] Every past-dated scenario scored or marked — **zero past-dated, and the reason is stated as luck
      rather than construction**; `S8` named as a 16th-run process failure.
- [x] `reject_ledger.py due` run (0 due, legacy 0). `missed_ledger.py due` run (4 due → 2 resolved,
      2 explicitly named as within-run deferrals with the grammar gap logged as `D283`).
- [x] Exposure state read and carried (§3c) — not a cold start, band deviation −27.1pp carried.
- [x] Instrument health inherited first (§0); FAILED gates converted into explicit revocations.
- [x] Self-refutations written down (§8).
- [x] Stale rows flagged with `asof` (§5).
- [x] `[measured]`/`[inferred]` tags preserved; no `[inferred]` claim passed downstream as evidence.
- [x] RESEARCH groups C/S/D/W/L loaded as binding constraints with the stages they bind (§6).
- [x] No sizing, no buy/sell language anywhere in this document.
