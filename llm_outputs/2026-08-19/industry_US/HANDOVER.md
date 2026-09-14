# HANDOVER — industry_US · 2026-08-19 (Wed KST) · Stage 2/11 (L1·HANDOVER)

> Inheritance stage. Transports analysis, never a recommendation (P4). No sizing, no buy/sell language.
> Run clock **KST 21:51– = ET 08:51–, Wednesday, US cash pre-market** (bell 09:30 ET = 22:30 KST, mid-run).

---

## 0. Instrument health inherited BEFORE any number is trusted

`llm_outputs/2026-08-19/preflight/PREFLIGHT_US.md` **was run** (filename deviation logged there for the
10th run; `PREFLIGHT.md` in that folder belongs to this morning's `industry_kr` desk).

**PASS 3 / FAIL 5 — the best instrument state this desk has recorded.** The rights this run inherits:

| Gate | Verdict | What this run may NOT claim |
|---|---|---|
| **G0** bar completeness | 🟢 **PASS** *(first ever)* | No 08-19 price of any kind (the session opens mid-run). No re-pull after 22:30 KST treated as comparable |
| **G1** news axis | 🔴 FAIL (7th run) | The sweep's `velocity` field · the 51 "survivors" as a set · any theme-freshness or "went quiet" claim from the sweep · `breadth` as a news-independent statistic. **"No news found" may not be written.** Hand probes must carry a clock time |
| **G2** scale continuity | 🟢 PASS | ★ **No Δ may be called "today's change" — every Δ this run is 08-14 → 08-18, TWO sessions.** No promotion on a `flow_score` gap ≤0.01 |
| **G3** sector sign | 🟢 PASS | No promote/demote of **Financials · Industrials · Materials** on weighted `wflow` (3 of 11 flip on top1) |
| **G4** risk units | 🔴 FAIL (10th) | No concentration statement as a single number; the `--days` window goes on the same line as the conclusion |
| **G5** universe | 🔴 FAIL | No flow/RS/OBV/short judgement on **`EA`** ("not measurable", not "no signal"); every mcap weight is **35 days stale** |
| **G6** estimate accrual | 🔴 FAIL | No `--ic` size presented as evidence-based ("mechanical ¼" if it appears at all) |
| **G7** tool liveness | 🔴 FAIL (10th) | `module_chart` and `margin_history.py` citable only on their working command lines — but **today the full `--read` panel is citable**, unlike 08-18 |

### 0a. The structural fact that governs this whole run

**The freeze is over. The terminal bar moved 08-14 → 08-18, two settled sessions in one step, after
five runs of zero.**

For five consecutive runs this desk opened on the same Friday close and could not move a single
scoreboard row. Yesterday it recorded that a session had settled and the instrument could not read it
(the 08-17 "three-quarters bar": OHL+V present, Close NaN on 300 of 301 names). **Today that bar comes
back complete from the provider, and 08-18 settled on top of it.** Nothing was repaired on this side.

Three consequences bind every stage below:

1. **`n_new_sessions_since_prior_run = 2`.** Every `delta` in `SECTOR_FLOW_US.json` is **08-18 minus
   08-14**. A stage that writes "moved today" is wrong by a factor of two. (`D280` says nothing stamps
   this automatically; it is stamped here by hand.)
2. **The board actually moved**: **298 of 299 `flow_score` values changed**, median |Δ| **0.127**,
   **44 tag changes**, and the G3 flipper set changed for the first time in five runs. The five
   readings of 08-15→08-18 were **one observation**; today is the second.
3. **Nothing may be dated 08-19.** The US session opens at 22:30 KST, after this stage.

---

## 1. Inherited standing view (`STANDING_VIEW.md` spine + `STANDING_VIEW_US.md`)

**Regime call, carried unchanged:** *memory is a price-cycle industry in rate-of-change deceleration
while its level stays tight* `[inferred]`. Lens L1 (equity tracks the **second derivative** of price,
not the level) is why "shortage persists" and "stocks struggle" coexist.

Carried structural anchors, tags preserved:
- `M1`–`M9` the memory chain `[measured]`; `M18` MU gross margin **84.6% = 100th percentile of 17
  years, +25.7pp above the prior-cycle peak** `[measured]` — the lens-L2 (peak-margin) instrument.
- `M19` estimate-revision IC: folded **+0.32**, Q5−Q1 **+19.5pp**, verdict **"indistinguishable"**
  because Q5 is 72% IT / 39% semis and effective dates = 1. Still `[inferred]` as a tradable edge —
  carried, **not citable as evidence**.
- `M25` the US 🟢 tag is a **volume-surge count, not a flow count**. Binding today: the board shows
  **8 🟢 / 63 🔴 of 299**, and that ratio is a `vol_surge` statement.
- `M704` / `D249` defense-vs-`XLI`, upgraded by `M719` (+4.32pp on 60 days with `LHX` removed).
- `R73` withdrew the term-premium **level** mechanism under the UW-duration complex; the measured shape
  is a **bull steepener**, a tailwind rather than a drag. `S80` (tonight) and `S98` (08-20) are the rows
  that settle whether that underweight is three or four legs of one bet.

### Retracted ledger (§5) read BEFORE forming today's view

Most recent rows: `R73`–`R78` (US, 08-16/17), `R77-REARGUED` (KR, 08-18), **`R79-REARGUED` (KR, this
morning 08-19)**. Nothing in today's PREFLIGHT resurfaces a retracted claim. Two live interactions:

1. 🚨 **`R79-REARGUED` was registered nine hours ago and this run's own measurement narrows it — the
   same day, on the same bridge.** The KR desk closed at 08:29 KST by confirming a **~50-call /
   ~2-minute quota** with three probes (idle 42/42 · burst `[('1',50),('0',90)]` · recovery +77.2 s)
   and drew a corollary: *"deterministic — the same first 51 names survive every run,"* with survivor
   indices `[0…50]` and the warning that the survivor set is a **market-cap selection bias**.
   **The US sweep at 21:52 returned the same count and a different shape:** survivors **51**, but
   **44 separate runs, longest 3, forty singletons, spanning indices 16–295.**
   ⇒ The **quota** half survives (this desk's own recovery probe reproduced lockout→recovery:
   15 consecutive failures ≈36 s, then 32 unbroken successes). The **determinism corollary does not** —
   survivors are an arbitrary sample here, not a mcap prefix. **Registered below as `R80` (scope
   narrowing, not reversal), and the KR-specific rights-line about mcap bias is NOT imported (W1).**
2. **`R78`'s lesson is pre-empted again**: `tag = flow_tag(price, velocity)` still bypasses the
   axis-drop guard, so no stage may promote on a tag today (`D261`/`M701`, 4th measurement).

### Open contradictions carried deliberately (§6) — not resolved by picking a side

- **`C1` LTA price floors** — cap the upside and floor the downside. Unmeasured. Carried.
- **`C10`** renewables/oil linkage — both readings survive their own tests. Unmeasured. Carried.
- **`D261` / `M701`** — `breadth` and `tag` bypass the axis-drop guard while `flow_score` does not.
  Carried, not resolved.
- **`D279`** — a story that never left cannot burst, so `theme_age` and `burst` fail *together* on
  precisely the standing risks that matter. 🚫 Standing constraint: **no stage may read a low
  `theme_age` or an absent `burst` token as evidence that a risk has receded.**
- **`D280`** — nothing stamps `n_new_sessions_since_prior_run`. Today the honest stamp is **2 new
  sessions, 2 readable** — the first run in six where those two numbers agree.

---

## 2. Scenarios — condition-check executed on every ARMED row

### 2a. US: zero rows past-dated — and this time the reason is a clock, not a frozen tape

`SCENARIOS_US.md` opened in full. Nearest settlements: **08-19 tonight** (`S75`–`S78`, `S80`) ·
**08-20** (`S82`, `S83`, `S98`) · **08-21** (`S84`–`S91`, `S93`, `S95`–`S97`) · 08-24 (`S74`) ·
08-26/27 (`S79`, `S81`) · 08-31 (`S92`, `S94`).

★ **The five rows dated 08-19 settle on tonight's 08-19 US close — which occurs at 05:00 KST on 08-20,
after this run ends.** This is not luck and not a frozen tape; it is **structural**: this desk runs
pre-market every day, so a row dated D is always scored by the **D+1** run. Written down explicitly so
that the 08-20 run treats them as **past-due on arrival**, not as fresh.

**`EXPIRED` = 0 · silent skips = 0.**

### 2b. ★ Pre-settle distance-to-branch — the first such reading in six runs

Not scores. **Readings at the 2026-08-18 settled close, one session short of the settle**, recorded so
the 08-20 run inherits a trajectory rather than a surprise. Every threshold below was frozen at
registration and is quoted unchanged.

| Row | Frozen observable | Reading @ 08-18 | Branch A | Branch B | Where it sits |
|---|---|---|---|---|---|
| **S75** ENRG promotion | `XLE` 5-session excess vs `SPY` | **+4.917** | ≤ −3.60 | ≥ +3.94 | **above B** — the promotion is running validated on its own axis |
| **S76** leg 1 HLTH | `XLV` exc5 vs `SPY` | **+1.427** | ≤ −2.67 | ≥ +2.62 | mid-band |
| **S76** leg 2 HLTH | count of HLTH names with `OBV 매집 ∧ RS20>0` | **17 of 32** | ≤ 10 | ≥ 22 | mid-band (anchor was 18) |
| **S77** MATR | EW 5-session excess of the 11 **non-NEM** Materials names | **−3.231** | ≥ +2.03 | ≤ −2.04 | **below B** — the UW− is heading to its **first NEM-free confirmation** |
| **S78** FIN | median RS20 vs `SPY` of {JPM, BAC, WFC, BRK-B} | **+1.256** | ≥ +4.68 | ≤ −5.65 | mid-band |
| **S80** duration | EW{`XLU`,`XLRE`,`XLP`} cum. excess from the 08-13 close | **+0.801** *(3 of 4 sessions)* | ≥ +1.85 | *(see row)* | below A, one session left |

Also readable early, for rows settling later:

| Row | Reading @ 08-18 | Note |
|---|---|---|
| **S98** (08-20) — is the UW **four** legs of one bet? | `XLU` **+1.30** · `XLRE` **+1.65** · `XLP` **+1.45** · `XLV` **+1.43` | ★ **all four the same sign and inside a 0.35pp spread** — pointing hard at branch **A (all four agree)**, which by its own registration text **would retire a four-sector tilt**. Consistent with `R73`'s bull-steepener correction |
| **S96** (08-21) optical | `EW{COHR,LITE}` exc5 **+0.247** | far from both ±5.0 bands |
| **S97** (08-21) `LHX` | exc5 **−1.862** | between A (≤ −4.0) and B (≥ 0) |

⚠ **Three disclosures on the table above.** (i) These are **pre-settle**, one session short, and a
5-session excess against a 2–4pp sigma can cross a band in one session. (ii) `S76` leg 2 carries the
construction ambiguity its own text created — *"the next full sweep"* versus *"the 08-19 settle"*;
today's sweep is the **last full sweep before the settle**, and the number is recorded as that, not as
a verdict (protocol §2: record the ambiguity, do not improvise a threshold). (iii) `S77`'s per-name
detail is **10 of 11 negative** (`CTVA` +2.62 the only positive), so the reading is broad rather than
one name — which is precisely the property `S77` was built to test.

★ **Supporting measurement for `S76`, and it is the row's actual point:** of the **17** HLTH names
passing `OBV 매집 ∧ RS20>0`, **zero** clear `vol_surge ≥ 1.2`. **The entire Health Care breadth reading
of 0.00 is the volume gate alone — M144's 7th replication.**

### 2c. KR: one past-dated row, and it was already scored by the sibling desk — verified, not assumed

`SCENARIOS_KR.md` opened. **`S52-KR` was dated 2026-08-19 and the KRX session closed at 15:30 KST**, so
it was past-dated at this run's clock and is this desk's to score under the cross-market rule.
**It was already handled this morning**: `llm_outputs/2026-08-19/industry_KR/HANDOVER.md §3-A` settles
it **`미결 (undecided)` · partial settlement · re-registration required** — O1 195,500 inside the band,
O2 unscoreable, all five anti-signals unfired, window 9 of 11 sessions — with **`S64-KR` reserved** as
the replacement. **Checked in the sibling's output, not assumed from the date.** Remaining KR rows,
none past-dated: `S57-KR` 08-20 (its own desk has already recorded a trajectory of `EXPIRED-미도래`) ·
`S63-KR` 08-20 · `S27` ~late-Aug · `S58-KR` 09-09 · `S61-KR` ~09-14 · `S62-KR` 09-15 · `S45` & `S54-KR`
09-30 · `S60-KR` 10-12 · `S49-KR` 10-30 · `S34` & `S53-KR` 10-31 · `S59-KR` 11-04.

### 2d. 🚨 `S8` — UNSCOREABLE for the SEVENTEENTH consecutive run

Undated `[blank]` Hormuz binary, still on `CATALYST_WATCH` as an undated 🔀binary. **A human must
`VOID` it or re-register it with a date (P5).** `S95` now brackets the 60-day MoU expiry that `S8`
could not, so the desk's dependence is falling — the row itself remains an open process failure and is
named here rather than dropped.

---

## 3. Both ledgers audited — symmetric, per `carryover.md` §3c

### 3a. Rejection ledger — `reject_ledger.py due`
`184 total · 101 resolved · legacy rows with no revives_if: **0** · due/past-due: **3**.`

| Row | Revival condition | Status this run |
|---|---|---|
| **EMR** (08-05, H.밸류소진) | *first upward next-quarter revision* **AND** *segment 21-60 vs SPY ≥ 0* | 🚨 **leg 2 FIRED (+2.48)**, leg 1 **structurally unmeasurable** |
| **AME** (08-05, H.밸류소진) | same | 🚨 **leg 2 FIRED (+5.79)**, leg 1 **structurally unmeasurable** |
| **VLO** (08-12, H.밸류소진) | *≥2 of 3 refiners back below consensus mean target* **AND** *refining-margins theme accel ≥ 1.5×* | ⏳ **not resolvable today** — the theme-acceleration leg needs the news axis, revoked by G1 |

🚨 **`EMR` and `AME` cannot be resolved by any evidence, ever, as written — and this is measured, not
suspected.** Their leg 1 requires an estimate revision, and the estimate universe
(`data/estimates/eps_2026-08-19.json`, `rows`) holds **120 names of which neither is one** — verified
directly today (`EMR` False · `AME` False · `NVDA` True). The condition is a conjunction with one leg
that has no instrument, so the row is **permanently blocked**, not pending.
★ **This reproduces `D279-KR` — registered by the KR desk on 08-19 for KR names — on US names with US
data, measured here rather than imported (W1).** Named as a construction defect and carried to the dig
list; a `resolve` call would be a fabrication, so none was made.
**All three rows are named here rather than silently carried a second time.**

### 3b. Missed ledger — `missed_ledger.py due`
`154 total · 65 resolved · legacy rows with no entry condition: **0** · due/past-due: **7**.`

`VLO` (08-04, Q.확신부족) · `EQIX` (08-04, M.숏리스트탈락) · `028050` (08-05) · `069620` (08-05) ·
`008930` ×2 (08-07, 08-12) · `ABT` (08-12, R.타이밍대기).

- **`VLO`'s entry condition has fired on the price leg**: *"no named windfall instrument appears and
  VLO holds RS60 > +15"* — measured **RS60 +41.87** at the 08-18 close, 2.8× the bar.
- **`ABT`'s condition is a three-way conjunction keyed to `S76` settling** *(registered as "S76 settles
  08-19 as promotion-held AND vol_surge ≥ 1.2 AND positive upside to consensus mean")*. `S76` settles
  tonight, and `ABT` is one of the 17 HLTH accumulation names with **`vol_surge` below 1.2** ⇒ leg 2
  is currently false. Not resolvable until the 08-20 run.
- The three KR rows belong to the sibling desk's morning run and were handled there (`008930`'s second
  leg is now structurally dead — `S52-KR` finished **undecided**, so it cannot support the row either).
- ⚠ `D278-KR` stands: `missed_ledger` has no `condition_fired` outcome value, so a fired-but-not-traded
  condition has **no truthful resolution** on a desk that does not trade. `VLO` is exactly that case,
  for the **second** consecutive run. Named, not laundered.
- ⚠ **Sign discipline**: the two ledgers' `excess` signs are **inverted** and were not summed.

### 3c. Exposure state (`exposure_rule.py show`) — carried as size context only

Latest row **2026-08-19 · `live` · state `정상` · invested **81.0%** · day excess −6.72 (cash −2.42,
selection +4.30 decomposition) · 🚨 **band deviation −14.0pp**.
Cumulative, **n = 9**: total excess **−10.01pp = cash −5.05pp + selection −4.96pp**.

⚠ Three flags carried verbatim: (i) the row is `live`/**unsettled** (intraday KIS), (ii) **`n=9` — C4
forbids asking the sign of the decomposition yet**, (iii) 🚨 the state reads `정상` while the band
deviation reads **−14.0pp**, i.e. **state and target disagree**; the desk has logged this divergence
class before and **a correction is a human call (P5)** — no number is substituted here.

---

## 4. Stale-check

| Carry | asof | Status |
|---|---|---|
| `us_top300.csv` market caps | 2026-07-15 | 🔴 **35 days** — every sector weight in ROTATION inherits this |
| Sweep terminal bar | **2026-08-18** | 🟢 current (2 sessions gained) |
| Estimate snapshots | **2026-08-19** | 🟡 saved today; accrual rate still 2.6× slow |
| `M19` IC verdict | 2026-08-06 | carried `[inferred]`, not citable as evidence |
| `EA` measurability | — | 🔴 unmeasurable for 7 consecutive runs; "not measurable", never "no signal" |
| Prior US desk outputs | **2026-08-17** | ⚠ the 08-18 run stalled after SWEEP — `MACRO_REPORT.md` · `BET_SHEET.md` etc. in the ledger are **08-17**, two days old |

⚠ **Not retroactively cleaned**: the 08-15→08-18 stretch of "identical" readings stays in the record as
what it was — one observation replayed, now explicitly labelled.

---

## 5. Method rules loaded as binding constraints (`RESEARCH.md`)

Loaded, not summarised. The ones that bind hardest today:

- **C1 baseline in the same sentence** — `R73` was found by re-measuring a carried window; the same
  failure mode is live wherever this run quotes a two-session Δ.
- **C4 scope** — `n=9` on exposure, `n=1` on today's G1 session, `n=2` on the flipper table.
- **C5 arbitrary choice** — the risk-unit count moves 12→4 across the threshold sweep; it is a choice.
- **W1 cross-market transfer** — 🚨 **the live one.** `R79-REARGUED`'s mcap-bias corollary is a KR
  measurement and is **not** imported; the US shape was measured here and differs.
- **D6 signal grade** — OBV is grade C; `S76` leg 2 and `S77` both lean on it and say so.
- **S1 date-fold · S3 power first** — no band verdict from a 3-of-4-session window (`S80`).
- **L1 second derivative · L2 peak-margin** — the regime call and `M18` respectively.

---

## 6. Dig list ranked for today

| # | Dig | Why it ranks here |
|---|---|---|
| 1 | **`R80` (below) — the survivor-shape divergence** | Two desks, one bridge, one day, two different shapes and the same count of 51. The count is quota-shaped; the membership is not. Registered this run |
| 2 | **`D287` (new) — a revival condition whose instrument does not cover the name** | `EMR`/`AME` are permanently blocked. `D279-KR` predicted this class; today it is measured on US names |
| 3 | **`D282` — DRIFT watches the corpus when it should watch its own thresholds** | Binds the last stage of this run |
| 4 | **`D280` — `n_new_sessions_since_prior_run` is unstamped** | Today it would have read **2**, after five runs of 0. The one day the stamp mattered most |
| 5 | **`D10` — news-body boilerplate** | Open code defect, needs human approval **and a server console** (FTS writes are server-only, P6). Carried, not re-discovered |
| 6 | **`D9` — holdco risk mismatch: block or warn?** | Half-closed; the remaining half is a human call |

---

## 7. To be written back to `handoff/*.md` at run end

- **`R80`** — scope narrowing of `R79-REARGUED`: the **~50-call quota** survives (reproduced here by an
  independent recovery probe), the **determinism corollary does not**. Evidence: US sweep survivors
  **51**, run structure **44 runs / longest 3 / 40 singletons / indices 16–295**, against KR's single
  run of `[0…50]` the same day. `[measured, n=1 session per market]`.
- **`D287`** — pre-check that a revival/entry condition's instrument actually covers the name before
  registering it. Measured: `EMR`/`AME` blocked forever; `data/estimates` covers 120 of the universe.
- **`M726`** (proposed) — Health Care: **17 of 32** names on `OBV 매집 ∧ RS20>0`, **0 of 17** clearing
  `vol_surge ≥ 1.2`. The breadth-0.00 reading is the volume gate alone, 7th replication.
- **`M727`** (proposed) — the non-NEM Materials EW 5-session excess is **−3.231 with 10 of 11 negative**
  at the 08-18 close, i.e. broad and NEM-free, one session before `S77` settles.
- **Stamp**: `n_new_sessions_since_prior_run = 2` for the 08-19 US run.

## ✅ EXIT CHECK
- [x] Shared spines (`STANDING_VIEW.md` §5/§6, `SCENARIOS.md` master log) + `STANDING_VIEW_US.md` +
      `SCENARIOS_US.md` + `RESEARCH.md` read; **`SCENARIOS_KR.md` opened because it held a past-dated
      row (`S52-KR`)**; `module_report_tags show` cross-queried (US outputs stand at 08-17).
- [x] Retracted ledger read **before** forming today's view; `R79-REARGUED` interaction argued with a
      **new** measurement that names the old one.
- [x] Every past-dated scenario scored or explicitly marked — **US: zero past-dated (structural clock
      reason recorded). KR: `S52-KR` past-dated and verified already scored by the sibling desk.**
      `EXPIRED` = 0 · silent skips = 0.
- [x] `reject_ledger.py due` run — **3 rows, all named**, two of them shown **permanently blocked** by
      measurement rather than silently carried. Legacy count **0**.
- [x] `missed_ledger.py due` run — **7 rows, all named**; signs not summed across ledgers.
- [x] Exposure state read and carried with its three flags (unsettled · n=9 · state↔band divergence).
- [x] 🚨 Instrument health inherited before any number was trusted (§0), and each FAIL's revoked right
      is carried into the stages that must obey it.
