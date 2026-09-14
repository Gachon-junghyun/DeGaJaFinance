# HANDOVER — industry_US · 2026-09-07 (Mon, **US Labor Day — NYSE closed**) · Stage 2 / L1·HANDOVER

> Read before anything is decided. Inherits the **analytical carry**, not the coverage ledger.
> **Sources read this run.** Shared spines: `handoff/STANDING_VIEW.md` (§1 regime call, §2 chain head,
> §5 retracted ledger through the 2026-09-07 KR block `R136`–`R138`, §6 open contradictions `C21`–`C29`,
> the asof chain including the 09-06 US and 09-07 KR entries), `handoff/SCENARIOS.md` (master index,
> the un-split master scoring log, the dated settle queue, the 09-06 US and 09-07 KR blocks).
> This desk's halves: `handoff/STANDING_VIEW_US.md` (the 09-06 append in full — `M1352`–`M1380` and
> the §3a registry), `handoff/SCENARIOS_US.md` (**scanned mechanically end-to-end — 142 row headers
> parsed, every settle date resolved**, see §3). Method: `handoff/RESEARCH.md` Part C dig lists
> (09-05 US `D502`–`D519`; 09-07 KR `D545`–`D552`), `handoff/README.md`.
> **Other-market file opened**: the 2026-09-07 `industry_kr` blocks in both spines — required, because
> that run registered **`D551`** (*verdict-grep is not a verdict-confirmation tool*) **four hours before
> this run started**, and this run's own back-scan is built on it. See §3b.
> Mechanical ledger cross-queried: `module_report_tags show`.
> ⚠ **Read honestly**: the spines total **3.6 MB**. `STANDING_VIEW.md` §1–§6 were read as structure plus
> targeted extraction; the per-run append blocks were read in full for the two most recent runs (09-06 US,
> 09-07 KR) and by header index before that. `SCENARIOS_US.md` was parsed **mechanically in full** and
> read **in prose for every one of the nine rows named below**. Stated because "read the spine" and
> "grepped the spine" are different claims (`D528`).
> **P4 — this stage transports analysis. No sizing, no buy/sell language anywhere below.**

---

## 0 · The one-line state of this run

**Three consecutive runs with no new price session** (09-05 Sat · 09-06 Sun · 09-07 Labor Day). The
sweep's `asof` is **2026-09-04** for the third time and all 11 sectors are numerically identical to the
09-06 file. ⇒ **This run cannot produce a price-based finding, and it should not pretend to.** What it
*can* produce — and what this stage did — is the **ledger work that a live tape usually crowds out**:
an exhaustive back-scan under the method the KR desk registered this morning, which found **six more
past-dated rows with no verdict anywhere**, and **four of them were mechanically scoreable from
already-published data**. Four brackets that have been silently open for 25–40 days now have verdicts.

---

## 1 · Instrument health inherited FIRST (`preflight/PREFLIGHT.md`, written 22:09–22:17 KST)

**PREFLIGHT ran and exists.** Its verdicts govern every number below.

| gate | verdict | what it removes from this run |
|---|---|---|
| **G0** | ✅ **PASS — fourth consecutive clean run** (1/301 NaN on all 14 sessions, `EA` only; **partial-NaN 0**) | nothing, except any verdict on **`EA`** |
| **G1** | 🔴 sweep news axis **17.39%** (52/299) · ✅ direct path 6/6 · ★ mechanism replicated a **4th** time | 🚫 no theme-freshness / velocity / "it is quiet" **from the sweep**, *including* the 52 that scored — they are exactly the 52 largest caps. **Absolute for UTIL / MATR / RE: zero names measured each** |
| **G2** | 🟡 **scale continuous, NOVELTY ZERO for a 3rd run** — `asof` 2026-09-04 == both the 09-05 and 09-06 runs' `asof` | 🚫 **Δflow may not be worded as "today's move"**; it is the **09-03 → 09-04** change, now restated three times |
| **G3** | ✅ full 11-row list printed (1 flipper by the flag; **2 by issuer**) | 🚫 no `wflow` verdict on **Cons. Disc.** (AMZN 40.2%) or **Comm. Services** (Alphabet 76.6% under two tickers) |
| **G4** | 🔴 **12 / 11 / 10** units across 250/500/750d | 🚫 no single-number concentration claim; `--days` on the same line |
| **G5** | 🔴 universe **54 days** stale (cover ✅ 11/11, missing 0) | 🚫 no cap-weight / sector cap share / `top1_w%` / issuer share cited as current |
| **G6** | 🔴 accrual **0.56/day, 1.8×** slow | `kelly_size --ic` is "mechanical 1/4" if used at all |
| **G7** | 🟡 **49/51** `--help` clean; chart live 3/3 | 🚫 no `margin_history` output |

★ **The two gates that MOVED, and both against this run.**
1. **G1's recovery clock failed for the first time in three runs** — 0/5 through t+100s under 20s
   polling, where 09-05 and 09-06 both recovered at t+60s. It was alive again after ~2 min of
   *probe-free* idleness. ⇒ **hypothesis, explicitly not a measurement**: failed probes reset the idle
   timer, so polling for recovery prevents it. Registered below as `D553`.
2. **G1's wall moved 50 → 52** (universe rank), confirming `M1354`'s volume-threshold reading a third
   time — and PREFLIGHT recorded a **method correction** that matters for every future run: the
   `names` array is sorted by **`flow_score`**, not universe rank, so computing the wall on array index
   makes it look random. This is the same class of error as `D551` (reading the wrong index and
   believing the output). Carried as `D554`.

⇒ **Standing implication, inherited into every later stage**: the price tape is three runs stale.
**Whatever is genuinely new today must come from the non-price instruments.** And because Labor Day
also suppresses US macro releases and US corporate filings, even those are thin — which is the reason
this stage spent its budget on the ledger rather than the tape.

---

## 2 · Retracted ledger read BEFORE forming today's view (`STANDING_VIEW.md` §5)

Read through the 2026-09-07 KR block. The three newest entries are KR-owned (`R136` term-length
prescription · `R137` "four insurers = one risk unit ⇒ insurance sector = one unit" · `R138` the
insurance-vs-bank two-verdict split) and **`W1` bars this desk from importing any of them**. They are
recorded as read, not used.

**Checked against this run's own output**: no claim below matches a retracted entry. The one that
came closest is `R134` (the `fts search --full` habit) — this run did make direct news calls and did
**not** body-read them, which is the *same habit* the KR desk closed one instance of this morning.
**Stated rather than hidden** (§4c / `D48`).

---

## 3 · Scenario scoring — the back-scan, and what it found

### 3a · The queue says zero. The queue is not the instrument.

The dated settle queue's next cell is **2026-09-08**; there is no 09-07 cell (Labor Day). Both the
09-06 US run and the 09-07 KR run verified this independently. **This run did not stop there.**

### 3b · The method, and why it changed this morning

The 09-07 `industry_kr` run registered **`D551`** hours before this run: *verdict-grep is not a tool
for confirming a verdict* — summary rows that list many ids alongside a verdict token, and negations
(`"NOT EXPIRED"`, `"PENDING"`), both read as positive verdicts. Its own back-scan produced **23/23
false ✅** twice before a third method worked: **only a table row whose FIRST cell is that id counts.**

**This run ran both methods on the US file, deliberately, to see whether `D551` is a KR-file property
or a property of the technique.** It is the technique:

| method | past-dated `ARMED` headers | reported as having a verdict | **missed** |
|---|--:|--:|--:|
| ±200-char proximity grep (the 09-06 method) | 87 | 84 | **6** (3 false ✅ from `S46-KR`/`S49`/`S41`-adjacent prose) |
| **first-cell table row only (`D551`'s method)** | 87 | 81 | **0 known** |

⇒ **`D551` reproduces on an independent file, an independent desk and an independent operator, within
one day of registration.** Filed as **`M1411`**. The 09-06 run's own count of "five past-dated rows it
could not see" was itself an undercount produced by the weaker method — **stated plainly rather than
edited away** (`D48` applies to this desk's predecessor run, and this run is its successor).

### 3c · What the strict scan found — **six** more US rows past settle with no verdict anywhere

| row | settle | days past | class | what this run did |
|---|---|--:|---|---|
| **`S19`** — FOMC 07-29, the **hike** branch | 2026-07-29 (numeric legs → **08-05**) | 33 | `D531` interim-tracking-line | ★ **SCORED — `FIRED-M`** |
| **`S9`** — the DOVISH real-rate branch | 2026-07-29 *"and running"* | 40 | **no terminal date registered** | ★ **SCORED — `FIRED-B`** + construction finding |
| **`S41`** — the AI-issuer credit channel | 2026-08-12 | 26 | `D531` | ★ **SCORED — `FIRED-B`** |
| **`S46`** — `AAPL`, the ledger-revival bracket | 2026-08-13 | 25 | partial verdict 08-02, never closed | ★ **SCORED — `FIRED-A` (against us)** |
| **`S14`** — Mastercard Q2, the FIN-breadth test | 2026-08-06 (invalidation date) | 32 | `D531` | 🟡 **HALF-SCORED** — B ruled out mechanically; A's fundamental leg unreachable |
| **`S5`** — KR semiconductor exports 1–10 Aug | ~2026-08-11 | 27 | `W1` — KR customs series on a US-pure desk | **`EXPIRED-UNSCORED`, reassigned to `industry_kr`** |

### 3d · The four verdicts, with the measurement (`D242`: thresholds are as registered, unchanged)

**`S19` — `FIRED-M`.** Observable: (i) the target-range decision, (ii) `DGS2` close by **2026-08-05**.
- Invalidation checked **first**: HY OAS > 3.10% on a close ⇒ window max **2.87%** (07-29 … 08-05).
  **Not invalidated.**
- Branch **H** (raised, OR held with `DGS2` **> 4.45%** by 08-05): the decision leg was already on
  record as *held with three dissents for a hike*; `DGS2` window **4.22 · 4.23 · 4.28 · 4.25 · 4.20 ·
  4.18**, **max 4.28** ⇒ **H did not fire.**
- Branch **D** (held dovish AND `DGS2` **< 4.15%** by 08-05): **min 4.18** ⇒ **D did not fire** on its
  numeric leg, so the language leg never binds.
- Branch **M** (held, `DGS2` stays **4.15–4.45%**): **every close in the window is inside the band.**
  ⇒ **M: "no conclusion changes."**
- ★ The row's own pre-registered `n≈1` warning (FOMC 07-29 and June PCE 07-30 share one driver, oil,
  one day apart) is carried with the verdict, not dropped.

**`S9` — `FIRED-B`, and a construction finding filed alongside it.** Observable: `DFII10` with
`T10YIE` quoted alongside. Branches: A `< 2.20` with breakeven rising · B `2.20–2.55` · C `> 2.55`.
- **27 settled observations from 2026-07-29 to 2026-09-03: min 2.32 · max 2.47. Zero below 2.20, zero
  above 2.55.** ⇒ **B on every observation the row could ever have been scored against** — *"term-premium
  blip; the tilt survives on flow."*
- 🚨 **The row registered no terminal date** (header *"2026-07-29 (FOMC) and running"*). It is a
  condition-settled row whose condition never fired, which is why **no run could ever find it "due"** —
  a class the queue and the back-scan **both** structurally miss. Registered as **`D555`**.
- ⚠ This verdict is **not** a licence to re-argue the duration bet: it says the real-yield wedge did
  not invert, which is the *low-information* branch of the three and was disclosed as such.

**`S41` — `FIRED-B`.** Observable: IG OAS (`BAMLC0A0CM`) on a close, HY OAS quoted alongside.
- Branch **A** (IG OAS **≥ 0.90%** on a close by 2026-08-12): the 11 closes in the window are
  **0.81 · 0.80 · 0.79 · 0.78 · 0.78 · 0.78 · 0.78 · 0.78 · 0.78 · 0.79 · 0.79** ⇒ **max 0.81, never
  reached.** Branch **B** (IG < 0.90 **and** HY < 3.10 through 08-12): HY window max **2.87** ⇒ **both
  legs held.** Invalidation (a single-issuer default) did not occur.
- ★★ **This is the informative one.** The row was registered *because* the tape carried single-name AI
  CDS widening (Oracle ~200bp, NVIDIA ~78bp *"risen sharply"*, Meta ~93bp vs an IG index ~53bp) that
  the desk's index-level credit axis structurally could not see. **The verdict says the single-name
  widening did NOT transmit to the index in the following two weeks.** ⇒ `S26-A` held and the desk's
  index axis was the correct resolution — **on this window**. The registration's own counter-evidence
  (CDS trades are thin, single-digit daily trades, `[news]`-grade single-wire) is carried forward
  intact and means this is **not** evidence that CDS is a useless channel, only that it did not
  transmit inside 14 sessions. `D97` (no CDS feed) stays open.

**`S46` — `FIRED-A`, and A is the against-us branch.** Observable: (i) `AAPL` FQ4 gross-margin guide
direction (categorical), (ii) `AAPL` RS20 vs `SPY` **minus** `QCOM` RS20 vs `SPY`, settled closes,
through **2026-08-13**. State at registration **+32.6pp**.
- Leg (i) was already on record from the 08-02 partial: **gross margin flat or down ⇒ A's leg 1 MET**
  (and B's *"guided up"* leg therefore permanently false).
- Leg (ii), computed from settled closes this run: **07-31 +16.34 · 08-04 +10.68 · 08-07 +10.63 ·
  08-11 +5.50 · 08-13 −4.99pp.** A needs **< +15pp** by 08-13 — crossed on **2026-08-04** and never
  recovered; window min **−4.99** on the settle date itself.
- ⇒ **Both legs of A met. `FIRED-A`: the ledger revival was flow-chasing into a binary, and the
  zero-base reading was right.** The row's own stated information content — *"branch A falsifies a
  decision this run made three stages earlier"* — is realised.
- ⚠ The separately-registered reaction test (implied ±3.3%, `D28` fix) is **not** folded into the
  branch and is not used to soften the verdict.
- ⚠ **This verdict lands on a decision class, not on a name.** It says a `resolve --outcome revived`
  taken on a **flow pull hours before an unbracketed binary** was wrong once, measured. `n=1`.

**`S14` — half-scored, and the half is the discriminating one.** Observable: MA cross-border volume
growth **AND** {`MA`,`V`,`PYPL`} RS20 vs `SPY` over the 5 sessions after the 07-30 print; branch B's
RS condition measured to **2026-08-06**.
- RS20 vs `SPY` on all five sessions plus the invalidation date: `MA` **+5.95 → +7.84** · `V` **+0.80
  → +4.15** · `PYPL` **+25.52 → +29.66**. **All three positive on every session.**
- ⇒ **Branch B is definitively ruled out** (it requires the RS20 flip, which never happened).
  **Branch A's price leg is MET**; its fundamental leg (cross-border volume "holds") could **not** be
  retrieved 39 days later on this desk's admissible feed — `fts search "Mastercard cross-border"
  --days 60 --scope foreign` returns **0**, and the one 07-30 print article that exists
  (*"Mastercard in Charts: Purchase transactions and GDV post solid Q2 gains"*, seekingalpha) speaks
  to purchase transactions and GDV, **not** to the frozen observable.
- ⇒ **Recorded as `A-partial` with the settled half published and the missing half named.** Widening
  "cross-border volume" to "GDV" to make it scoreable is exactly the improvisation `D242` forbids.

### 3e · What this run did NOT score, and why

- **`S5`** — a Korean customs series. Scoring it here is a `W1` cross-market transfer. **Reassigned to
  `industry_kr` by name** so it cannot be carried silently a third time.
- **`S16` · `S24` · `S42`** — already marked `EXPIRED-UNSCORED` by the 09-06 run with reasons. **Not
  re-litigated.** They remain human items (`P5`).
- **`P121` · `P114` · `P125`** — 🚨 **`D427`'s 8th reproduction, and the calendar floor the 09-06 run
  predicted was confirmed.** A fresh `module_macro_us --days 400 --json` this run:

| carries **2026-09-04** | stops at **2026-09-03** | stops earlier |
|---|---|---|
| `T10YIE` **2.35** · `RRPONTSYD` 0.675 | `DGS2` **4.34** · `DGS10` 4.77 · `DGS5` 4.52 · `DGS30` 5.25 · `DFII10` **2.42** · `hy_oas` **2.65** · `ig_oas` 0.79→0.81 · `VIXCLS` 14.32 · `SOFR` 3.66 | `WALCL` 09-02 · `DTWEXBGS` **08-28** · `NFCI` 08-28 |

  **Identical split to 09-06, byte for byte on the named values.** Because H.15 does not publish on a
  federal holiday, this is **the 5th consecutive blocked run and the block was correctly predicted in
  advance** — filed as `M1412`: *the desk's instrument pre-commitment was right, which is rare enough
  to count.* ★ `P125`'s joint-date construction continues to protect it from a verdict it would get
  wrong.
- **`S8`** — **41st consecutive run unscoreable**, date field still `[blank]`. Human `VOID` or
  re-registration (`P5`). The 41st writing of this line is the finding.

### 3f · Scoring tally for this stage

**Newly scored 4** (`S19` M · `S9` B · `S41` B · `S46` A) · **half-scored 1** (`S14`) ·
**`EXPIRED-UNSCORED` 1 with a named owner** (`S5` → KR) · **blocked-and-named 3** (`P121`/`P114`/`P125`) ·
**silent skips 0.**

⚠ **All four verdicts are transcribed into `handoff/SCENARIOS.md`'s MASTER SCORING LOG *inside this
stage*, not deferred to run end** — following the 09-05/09-06 precedent, and because `M1352`'s measured
failure mode is precisely that the scoring log is the writeback target that gets dropped.

---

## 3b′ · Both ledgers audited (`reject_ledger` **and** `missed_ledger`)

| ledger | total | resolved | **legacy (no revive/enter condition)** | **due today** |
|---|--:|--:|--:|--:|
| `reject_ledger.py due` | **303** | 185 | **0** | **0** |
| `missed_ledger.py due` | **337** | 207 | **0** | **0** |

- **Legacy 0/0 for a 19th consecutive run.** Per the stage's own warning, a clean `due` is **not**
  proof of health — but the legacy counter is the real evidence, and it has been at zero since the
  class was closed. ✅
- ⚠ Totals moved **303 → 303** rejections and **334 → 337** misses since the 09-06 US run; the three
  new misses were filed by the 09-07 KR run, not by this desk. **`C22`** (the two ledgers name different
  hands) carried, 19th run.
- ⚠ **The two ledgers' `excess` signs are inverted and were not summed.**
- 🚨 **`C27` / `D463` — `MSTR`'s two opposite rejections are unexamined for a 5th consecutive run.**
  `due` surfaces them **09-18 / 09-22**, so the ledger is behaving correctly; the defect is that the
  desk keeps waiting for the tool to force the question. Named, not dropped.

---

## 3c′ · Exposure state read and carried (size context for BET / ALPHA)

`exposure_rule show` — **`live` / `정상`**, latest row **2026-09-07**:

| field | value |
|---|---|
| verdict (4-state) | **정상** (normal) |
| stored invested % | **85.2%** (last populated 2026-09-04) |
| **current invested %** | 🚨 **BLANK — `투자비중미상(계좌조회 없음)`, `timefolio조회실패:CDPError`** |
| cumulative excess (simple sum, n=**18**) | **−9.79pp = cash −5.32pp + selection −4.47pp** |
| band | 🚨 **밴드이탈 −9.8pp** on the last populated row |
| arming | 🚨🚨 **ARMED (`TIMEFOLIO_EXECUTE=1`)** — standing human item (`P5`) |

- **Not a cold start** (18 scored days), so the verdict is quotable — **but the current-invested-% field
  is empty for a second consecutive run** (`M1358`, `D483-KR`). ⇒ **BET/ALPHA may cite the 85.2% only
  as a *stored* value with its 09-04 date attached, never as "current".**
- ⚠ **`n` has been flat at 18 for six calendar days.** The stated purpose of this ledger is to raise `n`
  by one per day; it is not doing so, and the reason is the same account-query failure. Carried.
- **`C23`** (three books, none self-identifying) — **10th reproduction**, four legs disagreeing:
  `exposure_rule` target 95% · `show` stored 85.2% · `state` current **blank** · `cycle_exposure` reads
  the real KIS book at ~52% cash.

---

## 4 · Stale-check — every carry has an expiry

| carry | asof | age at this run | verdict |
|---|---|--:|---|
| Sweep flow table (all 11 sectors) | **2026-09-04** | **3 runs, 0 new sessions** | 🚫 **not stale — but not new either.** May be cited only with the 09-03→09-04 label |
| `us_top300.csv` cap vector | 2026-07-15 | **54 days** | 🔴 **stale.** Equal-weighted readings govern where the two disagree |
| `M1360` — the carried *"WTI printed $96"* | corrected 09-06 | — | ✅ **already retracted by the 09-06 run**; settled `CL=F` gives 09-04 close **$91.48**, window high **$93.14**, 5-session **+9.69%**. **This run does not resurrect the $96** |
| `M1361` — distillate crack 3-session **−$7.02/bbl = 6.0th pctile** while its **level is 95.6th** | 2026-09-04 | 3 sessions, no new data | carried **unchanged**; it cannot have moved |
| `M1364`/`M1365` — 17/17 carried terms fell on raw counts; **zero 🟢FRESH for a 13th measurement** | 2026-09-06 | 1 day | ⚠ carried **with its denominator warning**: the raw fall was a weekend-window artifact; share-normalised it is ±5% flat |
| `MU` FQ4 date | `D488`-corrected to **2026-09-30 16:00 ET** | — | carried; **three sources gave three dates**, the `Ticker.earnings_dates` one governs |
| `S4` (`MU` FQ4) · `S3` (~09/10) | — | — | **not due** |
| **Suspensions cleared** | — | — | **none cleared this run** — no window expired on a closed session |

---

## 5 · Method rules loaded as binding constraints (`RESEARCH.md`, by firing moment)

Loaded, not summarised. The ones that actually bind **this** run, with why:

- **`C1` baseline · `C2` both halves · `C4` "indistinguishable"** — bind §3d. Every verdict above
  quotes the window's full observation set, not the endpoint alone, and the invalidation clause was
  checked **before** the branch in all four.
- **`C5` arbitrary choice** — binds G4: the concentration count is 12/11/10 depending on `--days`, and
  the 0.65 threshold is itself load-bearing (12 for every threshold 0.40–0.65, then 10/7/7/5).
- **`S1` date-fold · `S5` short samples** — bind G4's 250d window (249 < 250, ARI 0.3874 against a
  flattering +0.8511 fit = the fit-vs-stability inversion).
- **`D5` cross-provider · `D6` signal grade (OBV is C)** — bind `C25`: the sweep and `module_chart`
  disagree on OBV sign at a **measured rate** now (`M1373`: 6 agree / 1 partial / 1 outright on eight
  names). No OBV claim below C grade.
- **`W1` cross-market transfer** — **binds hard today, twice**: (i) the three new KR retractions
  `R136`–`R138` are read and not used; (ii) `S5` is reassigned rather than scored here.
- **`W3` real ≠ profitable** — flagged forward to DEEP for the defense node (`M1370`/`M1377`: a
  7.1st-percentile 5-session extreme with **zero** narrative carriage cuts both ways).
- **`L3` branch information content** — binds PREMORTEM: `S150` was registered with **B already below
  its own line**, disclosed; `S149`'s informative branch is the against-us one.

### Dig list ranked for today (the DEEP/PREMORTEM candidates)

| rank | dig | why today |
|---|---|---|
| 1 | **`D551` → `M1411`** *(verdict-grep is not verdict confirmation)* | ✅ **worked on today's run** — it is what found the six rows. Carry the method, not the conclusion |
| 2 | **`D531`/`D555`** *(interim tracking lines, and now condition-settled rows with no terminal date)* | 4 of the 6 rows found today are `D531`; `S9` opens the **new** sub-class |
| 3 | **`D427`** *(H.15 split publication)* | **8th reproduction**, 5th consecutive block of `P121`/`P114`/`P125` |
| 4 | **`D507`** *(no US market holidays in `catalyst_calendar`)* | **today is the holiday.** Every N-session window written off `--days` is mis-dated unless 09-07 is excluded by hand |
| 5 | **`D513`/`D517`** *(AI-power lane has no registry row and no price series)* | assigned forward to PREMORTEM/DEEP; unchanged |
| 6 | **`D459`** *(collapse dual-class issuers before `top1_w`)* | **12th reproduction** — Alphabet 76.6%, COMM un-rankable for a 16th run |
| 7 | **`D472`** *(scored rows whose header still reads `ARMED`)* | residual **47 → will rise by 4** when today's verdicts are written; the counter is published so it can be tracked |
| 8 | **`D379`** *(PREFLIGHT should read §5 first)* | **11th run unwired**; order kept by hand again |

---

## 6 · Open contradictions carried (`STANDING_VIEW.md` §6) — none resolved by picking a side

| id | state at this run |
|---|---|
| **`C29`** an axis with opposite signs on two instruments (`vol_surge`) | 🚨 **carried, now with 7 legs across both desks.** The sweep's 🟢 gate still uses `vol_surge` with a **positive** weight while `ic_ledger` measures h=1 **negative**. **Not changed** (`P4`) — but every 🟢 tag this run reads is read with that known sign conflict attached |
| **`C25`** two instruments read OBV's sign oppositely | carried; US disagreement rate now measured (`M1373`). KR added a held-name instance today |
| **`C23`** three books, none self-identifying | **10th reproduction** (see §3c′) |
| **`C24`** copper spec at the 100th percentile vs a Materials bucket | **10th run.** `P102` settles **09-09**. ⚠ MATR has **zero** news-measured names today, so no "the story is absent" reading is available |
| **`C27`** `MSTR`'s two rejections disagree | **5th run unexamined** (`D463`) |
| **`C22`** the two ledgers name different hands | 19th run, legacy **0/0** |
| **`C21` · `C10` · `C26` · `C28`** | carried; `C26` closed-by-disappearance for a 4th run (no repaired sweep file needed) |
| **new contradictions opened this run** | **0.** Today's five findings are **defects**, not contradictions, and are filed as `D553`–`D556`. Opening a `C` is the easy side and this run deliberately did not |

---

## 7 · What this run asserted and then refuted, written down not edited away (§4c · `D48`)

1. ★★ **This operator's first pass at the news wall concluded *"the positional wall is GONE today —
   velocities are scattered across the whole universe with gaps everywhere."*** The **next command
   refuted it**: the `names` array is sorted by **`flow_score`**, not universe rank; re-mapped through
   `us_top300.csv`'s `rank` column the wall is **exactly contiguous, ranks 1–52, zero gaps**. ⇒ the
   sentence is left standing here and the refutation is appended beside it. Filed as **`D554`**.
2. ★ **The first back-scan of `SCENARIOS_US.md` reported 84 of 87 past-dated rows as verdicted.** The
   strict first-cell method reported **81**, i.e. the first pass produced **3 false ✅** from prose
   containing `S46-KR`, `S49` and `S41`-adjacent text. **The first number is not deleted.**
3. ⚠ **This run made direct news calls and did not body-read them** — the same habit `R134`/`D541`
   named this morning. Recorded as an instance, not excused.

---

## 8 · Registrations this stage makes (transcribed to `handoff/` at run end)

| id | type | statement |
|---|---|---|
| **`M1411`** | measured | `D551` (verdict-grep false ✅) **reproduces on an independent file, desk and operator within 24h**: proximity-grep 84/87 verdicted vs first-cell-table 81/87 on `SCENARIOS_US.md` ⇒ **6 rows, not 3, were past-dated with no verdict** |
| **`M1412`** | measured | `D427`'s **8th** reproduction, and its 09-06 **pre-commitment held** — the Labor Day floor was predicted in advance and the split published exactly as forecast (`T10YIE`/`RRP` at 09-04; `DGS2`/`DGS10`/`DGS5`/`DGS30`/`DFII10`/`hy_oas`/`ig_oas`/`VIX`/`SOFR` at 09-03) |
| **`M1413`** | measured | Four brackets open 25–40 days were **scoreable from already-published data all along**: `S19` M · `S9` B · `S41` B · `S46` A. **The obstacle was never data availability; it was that nothing looked** |
| **`D553`** | defect | *The news tunnel's recovery clock cannot be measured by polling it — a failed probe plausibly resets the idle timer.* Measured: 0/5 through t+100s at 20s spacing, alive after ~2 min of probe-free idleness, where the two prior runs recovered at t+60s under the same polling. **Hypothesis, needs a single-probe-at-t+180s test in `idle_probe`** |
| **`D554`** | defect | *`SECTOR_FLOW_US.json`'s `names` array is sorted by `flow_score`, not universe rank — any positional analysis computed on array index is meaningless and looks random rather than erroring* |
| **`D555`** | defect | *A scenario registered with no terminal date (`"and running"`) is invisible to both the settle queue and every date-based back-scan; it can only be found by a full parse that treats a missing end-date as a defect.* Origin: `S9`, undetected for **40 days** |
| **`D556`** | defect | *A bracket with one price leg and one fundamental leg degrades asymmetrically: the price leg stays scoreable indefinitely, the fundamental leg expires with the news window. Register the fundamental leg's retrieval path at registration time.* Origin: `S14`, whose RS leg scored cleanly at 32 days while its cross-border-volume leg returned **0 hits** |

---

## ✅ EXIT CHECK — HANDOVER

- [x] Shared spines read in full-by-structure + targeted extraction; **`SCENARIOS_US.md` parsed
      mechanically end-to-end (142 headers)**; this desk's `STANDING_VIEW_US.md` 09-06 append read in
      full; `RESEARCH.md` Parts A/B/C loaded as binding constraints (§5); **other-market file opened**
      (the 09-07 KR blocks, required for `D551`); `module_report_tags show` cross-queried.
- [x] **Retracted ledger read BEFORE forming today's view** (§2). No claim below matches a retracted
      entry; the closest habit-match is named against this run itself.
- [x] **Every past-dated scenario scored or explicitly marked with a reason** — 4 scored, 1 half-scored
      with the missing leg named, 1 `EXPIRED-UNSCORED` reassigned by name, 3 blocked-and-named,
      **0 silent skips** (§3f).
- [x] **`reject_ledger.py due` run** — 0 due, legacy **0**, reported with totals.
- [x] **`missed_ledger.py due` run** — 0 due, legacy **0**; signs **not** summed with the rejection ledger.
- [x] **Exposure state read and carried** with its 4-state verdict, the **blank** current-% flagged 🚨,
      and the cumulative cash/selection split at n=18 (§3c′).
- [x] 🚨 **Instrument health inherited before any number was trusted** (§1); every FAIL's revoked
      claim-right is restated here, not merely referenced.
- [x] **Two claims this run asserted and then refuted are written down, not edited away** (§7).

---

> P4 — nothing above is a market call, a name-level verdict, or a size. Scenario verdicts are
> *scores against pre-registered thresholds*, which is the opposite of a new view.
