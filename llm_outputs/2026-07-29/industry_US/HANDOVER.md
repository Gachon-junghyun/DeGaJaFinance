# HANDOVER — industry_US · 2026-07-29 (Wed)

> Stage 1/10 of `industry_us`. This stage **inherits**; it does not discover. Every claim below carries
> the tag it arrived with. Zero buy/sell language (P4).
> Sources read in full this stage: `handoff/STANDING_VIEW.md` (151.3 KB) · `handoff/SCENARIOS.md`
> (122.1 KB) · `handoff/RESEARCH.md` (150.1 KB) · `module_report_tags show` ·
> `reject_ledger.py due` **and** `score` · `CATALYST_WATCH.json` (2026-07-29).

---

## 0 · Run clock — binding on every downstream stage

| | |
|---|---|
| **Run start** | **2026-07-29 22:1x KST = 09:1x ET (Wed)** |
| **US session** | **NOT OPEN.** The 07-29 regular session opens at 09:30 ET, ~20 minutes after this stage. |
| **Newest settled US close** | **2026-07-28.** Every RS / flow / crack number this run computes must be stamped 07-28 or earlier. |
| **Newest settled KR close** | **2026-07-29** (KR session already closed — see §0-b; it was a −12% day). |
| **Nearest binary** | **FOMC decision 2026-07-29 14:00 ET — D-0, ≈5 hours after this stage.** Then META/MSFT/STX/V AMC tonight, then PCE 07-30 08:30 ET. |

★ **D74 is live today and this is the run it was written for.** `scripts/sector_flow.py` has no
settled-bar guard; the 07-28 US run tripped it at 09:38 ET and had to trim its cache. **This stage
hands SWEEP a hard instruction: the sweep must be run BEFORE 09:30 ET, or its cache trimmed to
≤2026-07-28 and re-run, and the `asof` field verified to read 2026-07-28.** A `asof: 2026-07-29`
stamp on any sweep artifact today is a contaminated bar, not a fresh one.

★ **Second binding clock rule, from this desk's own retracted ledger:** the 07-29 events listed in
`SCENARIOS.md` — **S2 · S9 · S11 · S13 · S16 · S17 · S18 · S19 · S23 · S24 · S30 · S35** — have
**not happened yet at this run's clock.** Filling any of them from a pre-open tape is exactly the
observable-fabrication `L3 scenario_score` forbids, and it is why the 07-29 KR run declined to score
them at 08:39 KST. **This run does not score them either.** They are named in §2 so they cannot be
dropped silently.

### 0-b · ★★ What is genuinely new since the last US run (2026-07-28) — and it lands on this desk's own regime call

Two items, both from the `--scope foreign` feed, both dated inside the last 24 hours:

1. **SK hynix printed a RECORD margin and MISSED, and the KR market took it as the miss.**
   The KR desk's own measurement this morning `[measured, M221, KR desk]`: **2Q operating profit
   ₩60.5426tn, +557.2% YoY, operating margin 76.3% = its own record — and ~₩4tn BELOW consensus.**
   The foreign feed carries the same event as a market event, not a beat:
   *"'Pray For Kospi': SK Hynix Earnings Miss, Sending Stock Reeling"* [zerohedge] ·
   *"SK Hynix shares sent sprawling once more as earnings miss steepens decline"* [marketwatch] ·
   *"Why SK Hynix's Record-Breaking Earnings Disappointed"* [yahoo_finance] ·
   *"Kospi crashes 12% after SK Hynix earnings"* [economictimes].
   ⚠ **Both halves are on the record (C2)** — record margin AND a consensus miss — and this stage
   carries both, not the convenient one.
   ★ **And the dispersion is the interesting part (W5), pre-flagged for MACRO/DEEP:**
   *"Why Micron Stock Is Rising After SK Hynix Fumbled Its Big Earnings Moment"* [yahoo_finance,
   2 items]. **One memory name fell on the print and another rose on the same print.** That is the
   exact shape C8/S30 exist to test, and MACRO must not compress it into "memory sold off".
   ⚠ **Grade: `[news]`, headline-level, bodies not yet drilled.** It is handed to MACRO as a
   **dig instruction**, not as an inherited fact.

2. **Oil re-escalated overnight.** *"Dow Jones Futures: Oil Jumps On Iran News"* [yahoo_finance,
   repeated across 4 same-day variants] · *"Stock Market Today: Dow Falls As Iran Hostilities Spark
   Up Again"* [yahoo_finance] · *"Asia 'scraping the bottom of the barrel' as Red Sea oil blockade
   worsens energy crisis"* [guardian 07-28].
   ⇒ **S8 branch A moved further away again**, and **S31's stated window contamination is live**.
   MACRO owns the settled numbers; this stage only records that the direction of the geopolitical
   axis inverted relative to the 07-27 "pause" headline that M184 already body-refuted.

---

## 1 · Inherited regime call — carried unchanged, NOT re-derived

> **Memory is a price-cycle industry in rate-of-change deceleration while its level stays tight.**
> `[inferred]`, built on the measured chain M1–M6 / M18.

The distinction that drives everything: a commodity-cycle equity tracks the **second derivative** of
price, not the level (lens **L1**). Level and rate point opposite ways, which is why *"shortage
persists"* and *"stocks struggle"* are both true (**C3**).

**What this stage does NOT do**: re-argue it. The 2026-07-22 measurement that six judgments were
reversed inside one session is the reason this stage exists. The regime call is inherited whole and
the only admissible way to change it is **S3 (4Q26 DRAM contract guidance, ~09/10)** or
**S34 (CXMT capacity, 10-31)** or **S37 (the branch in which CXMT is BULLISH for incumbents, → 09-30)**.

**Three inherited framing constraints handed forward verbatim:**

| # | Constraint | Where it binds |
|---|---|---|
| **§4 asymmetry** | *A hyperscaler capex **cut** changes the thesis. A capex **raise** only moves its timing.* Encode **before** the print, not after. | **MSFT/META tonight** — MACRO · PREMORTEM · S13/S16/S24 |
| **C1 (LTA price floors)** | They cap the upside *and* floor the downside. **Unmeasured.** Both readings stand. | DEEP-IT, any margin claim |
| **C8 (IT is one label over three legs)** | Spenders / suppliers / security want opposite verdicts. Resolving observable is **S13's cross-condition, dated today**. | ROTATION must not issue a blanket IT verdict |

---

## 2 · Scenario status — scored, unscoreable, and armed

### 2a · Past-dated rows: **ZERO unscored, ZERO silent skips**

Every row whose event date precedes today was settled by the two 07-28 runs and re-verified against
the scoring log this stage:

| ID | Event date | Verdict | Scored on |
|---|---|---|---|
| S1 | 07-22 AMC | **FIRED-A** | 07-23 HANDOVER (KR) |
| S6 | 07-23 AMC | **FIRED-A** | 07-24 HANDOVER (KR) |
| S7 | 07-23 | **FIRED-A** (both legs) | 07-23 US + 07-24 KR |
| S10 | 07-24 | **FIRED-B** | 07-24 HANDOVER (KR) |
| S12 | 07-23 | **FIRED-B** (observable) · **AMBIGUOUS** (decision axis, D35) | 07-28 HANDOVER (KR) |
| S8 | undated | **FIRED-B** | 07-28 HANDOVER (KR) |
| S20 | 07-28 | **FIRED-B** | 07-28 HANDOVER (US) |
| S28 | 07-28 09:00 KST | **FIRED-A** | 07-28 HANDOVER (US) |
| S33 | 07-28 close | **FIRED-A raw / branch-B beta-adjusted — the disagreement IS the verdict** | 07-28 HANDOVER (US) |

**`EXPIRED` count = 0. Silent-skip count = 0.**

### 2b · Rows whose date is TODAY and which are NOT scoreable at this clock — named, not dropped

| ID | Event | Why not scoreable now | Who scores it |
|---|---|---|---|
| **S2** | the 07-29 cluster | MSFT/META print AMC tonight; FOMC is 5h away | next US HANDOVER (07-30+) |
| **S9 · S19 · S23** | FOMC real-rate / hike / bear-flattener | **Decision at 14:00 ET, ~5h after this stage.** All three carry DGS2/DFII10/T10Y2Y windows running to **08-05** | 07-30 onward; windows close 08-05 |
| **S13 · S16 · S24** | MSFT/META capex; META vs {MSFT,AMZN,AAPL}; the UTIL leg | Prints are AMC tonight; all three observables run **10 sessions, to ≈08-12** | 08-12 |
| **S30 · S35** | supplier RS20 median; regulated-utility RS20 median | Windows open today, close **08-05 / 08-07** | 08-05 / 08-07 |
| **S17** | SK hynix ADR premium | **Its window OPENS today (07-29 → 08-05).** First observation is available from today's KR close — see §6 | KR desk (owner); US desk carries the read-through |
| **S11 · S18** | KR governance package · KT sanction | ★ **Both are KR-domestic regulatory events that occurred during the KR session today.** This desk's `--scope foreign` hard rule was applied: `fts search "KT" fine --days 2 --scope foreign` returns **1 irrelevant hit**; `Korea governance --days 3 --scope foreign` returns **108 hits, none of them the FSC package or the KT sanction**. ⇒ **Not scoreable on this desk's admissible feed.** **Explicitly assigned to the `industry_kr` run of 2026-07-30 and named here so it cannot be carried silently a second time.** |
| **S32** | NDX net-spec positioning | **The CFTC release covering the 07-28 Tuesday close publishes 2026-07-31.** Not EXPIRED, not pending — **not yet published** | 07-31 |

⚠ **S11/S18 are the one place this run has to hand work to another desk.** That is recorded as a
handoff, not as a pass — it is the same class as an `EXPIRED` row if the 07-30 KR run also skips it.

### 2c · Armed rows with dates ahead, ranked by how close they are

**S15** (PCE, 07-30) · **S14 / S14-ANNEX / S14-num** (MA, 07-30, scored 08-06) · **S21** (STNG, 07-30)
· **S22** (SK이터닉스 SPA, 07-31 — branch B, a *second* deferral, is the kill) · **S31** (XOM, → 08-05,
⚠ XOM prints 07-31 *inside* its own window, declared at registration) · **S36** (XLB vs SPY, → 08-05)
· **S26** (the credit escape hatch, → 08-12) · **S25** (RE, → 08-08) · **S29** (셀트리온, 08-06)
· **S38** (006360 short balance, → 08-12) · **S39** (pharma shelter, event-conditional → 10-31)
· **S27** (9th 최고가격, ~08 late) · **S5** (KR exports, ~08-11) · **S37** (MU fwd P/E, → 09-30)
· **S3 / S4** (~09/10) · **S34** (CXMT capacity, 10-31).

---

## 3 · Rejection-ledger audit — `due` run FIRST, and `score` separately

```
reject_ledger.py due  →  전체 63건 · 해소됨 20건 · 레거시(부활조건 없음) 5건 · 재확인일 도래/경과 0건
```

**Rows with a passed recheck date: ZERO.** Nothing is being carried past its own appointment.

**Legacy (no `revives_if` was ever set) — 5 rows, all KR:**
`103590 일진전기` · `105560 KB금융` · `000810 삼성화재` · `373220 LG에너지솔루션` · `454910 두산로보틱스`.

★ **One legacy row audited this run with a fresh pull, per the standing rule that the count must not
sit flat:**

- **373220 LG에너지솔루션** (filed 2026-07-22, `K.본문반증`, *"단독 1건, 체인 전체 분산"*) →
  **`resolve --outcome reaffirmed`.** Fresh `module_flow 373220.KS --bench ^KS11`:
  **🔴분산 · OBV 분산 · RS20 +16.2 / RS60 −21.1 vs `^KS11` · `vol_surge` 0.61 ·
  KIS 20d 외 +8.7만 / 기 −18.3만 / 개 +18.5만 (retail absorbing) · short balance 1.55% float
  `building(+0.08)`.** ⇒ the original **narrative** basis is now corroborated on the **B-grade**
  investor actuals and the A-grade RS60, so it stays out **on fresh evidence, not on a stale one**.
  **Legacy count 5 → 4** after this resolution.

⚠ **Do not read a clean `due` as a healthy ledger** (the rule's own warning). The legacy count has run
**12 → 7 → 6 → 5 → 4** across five runs — it is shrinking, which is the only evidence that this
practice is taking hold.

### 3b · `score` — ★ a new measurement, and it moved

```
40 scoreable rows · 평균초과 −1.7pp · 손해 8 · 이득 10 · 노이즈 22 (55%)
손해합 +65.8pp   vs   이득합 −131.2pp
유형별: narrative −1.0pp · measured −1.6pp · structural −3.1pp
```

Against the carried **M211** (07-28, 38 rows: **손해합 +55.5 vs 이득합 −71.0**, noise 66%), the
**benefit side nearly doubled (−71.0 → −131.2pp) on two added rows**, and the noise share fell
**66% → 55%**. Direction is unchanged from M211 (rejecting has been net-beneficial on this sample);
the magnitude is not.
⚠ **This is one crash session's mark-to-market, not an edge.** The 07-28 KOSPI −11.19% session and
today's −12% session sit inside almost every row's measurement window, so the "benefit" is
substantially **beta, not selection** — the same contamination S33-ANNEX/D82 named. **Reported as an
accumulating observation (C4), not promoted to a rule.**

---

## 4 · Reconciliation — what we BELIEVE vs what we COVERED

`module_report_tags show`: **32 reports · 182 tickers · 11 sectors**, updated 2026-07-29T09:37 (i.e.
it already contains today's KR run's files).

**(a) Belief with no coverage — demote or dig.**
- **AAPL** — carried in §3a with *"+17.3 / +20.8 vs SPY, the strongest two-window agreement in IT"*
  and **no thesis anywhere**. Ranked first-claim #2 by the 07-28 run. Still uncovered.
- **BX** — Financials' **#1 flow score (+0.767)**, appears in **no carried thesis**, no 4Phase.
  Ranked first-claim **#1** by the 07-28 run. **Still uncovered.**
- **Tankers (STNG·FRO·INSW·DHT·TNK)** — a carried `[measured]` belief on names **outside
  `us_top300`**, so this desk structurally cannot tag them. **S21 settles part of it 07-30.**

**(b) Coverage with no belief — candidate DEEP.**
- **COMM's long tail** (TTWO · TMUS · DIS · EA · CMCSA) picked up their **first-ever** coverage in the
  07-28 `SECTOR_DEEP_COMM.md` and carry **no standing thesis**. That is expected one run after a
  sector's first deep-dive; flagged so it is either converted or dropped, not left dangling.

**(c) Resolved-but-live — re-justify or retract.**
- **GOOGL · AMZN · NSC · FTNT · CME · NDAQ · PLD · 066570** all read `RESOLVED 🔴` in the ledger while
  carrying live §3a/§3b rows. **FTNT is the sharp one**: it was re-tagged **EXHAUSTED** on 07-28
  (RS20 −0.7 vs SPY with OBV 분산 against RS60 +73.1) **and it prints tomorrow, 07-30.** Its live
  thesis and its ledger verdict disagree, and the print is the resolver.

**(d) ⚠ The reconciliation itself is partly blind, and this is measured, not suspected.**
**M152/D65: 28 of the 300 universe tickers are silently unindexable** by
`module_report_tags/_extract.py`'s `_US_STOP` guard — **A · AIG · ALL · C · CAT · CB · COST · D · F ·
FAST · GS · ICE · KR · LOW · MA · MET · MS · NOW · O · ON · PEG · PM · Q · SO · T · TT · V · WELL.**
Verified again on today's ledger: **T, MA, V, GS, CB, WELL, ICE, SO, D all read 0 or are absent**,
while `SECTOR_DEEP_COMM.md` discusses **T** at length and `SECTOR_DEEP_FIN.md` discusses **GS**.
⇒ **Any "zero coverage" statement about those 28 names is uninterpretable.** The lists in (a) and (b)
above were built **after excluding** the 28. **The guard is sensible; the silence is the defect.**

---

## 5 · Retracted ledger — read BEFORE forming today's view

**26 retractions on file (R1–R26; R17-b, C-A/B/C also logged).** The rows this run is most likely to
re-derive, with what killed them:

| # | Must not resurface | Killed by |
|---|---|---|
| **R1 / D1** | *"SK hynix foreign selling is bearish"* | ADR venue migration. **The suspension is EXTENDED (R13), not lifted — and the calendar still says otherwise today (D61, §6).** |
| **R5 / W2** | *"EDA leads semis by 12–18 months"* | lag-12 ≈ 0.05 vs same-month 0.63 — **coincident** |
| **R7** | *"Real Estate is the purest duration expression"* | the tape inverted it; superseded again by **M133** (an operating-recovery rotation) |
| **R11** | *"the long-end move is bear-STEEPENING"* | 2s10s **flattened**. **The FIN OW lost one of its two legs here** — and **S23 is 0.14pp from firing** |
| **R15** | *"FIN OW — flow led the earnings: HIT"* | all seven KR FIN names lost the explosion day; driver was brokerage, not NIM |
| **R23** | *"STX GM is +15.1pp over its own prior peak"* | quarterly-vs-annual mix; like-for-like **+3.8pp**. **STX prints tonight** |
| **R25** | *"`capex cut` has returned ~0 six times"* | **a QUERY-FORM artifact.** Quoted → 0/0; two-argv AND → **66/273** on the same corpus. ★ **Binding on every stage today: a 0 from a quoted multi-word probe is NOT evidence of absence.** C6's conclusion survives on other evidence |
| **R26** | *"SKT's −13.09pp residual is a stale-beta re-rating"* | the beta series shows no drift across four windows |

★ **The pattern that produced 6 of the last 8 retractions (D48): a run's own later stage kills its own
earlier stage's claim.** It has now fired **10+ times across both markets**, and twice it was a
*subagent* correcting the mandate it was handed. **Instruction to every downstream stage: when this
run hands you a number, re-measure it rather than inherit it.**

---

## 6 · Stale flags and cleared suspensions

| Item | State | Action this run |
|---|---|---|
| **M6 · MU forward P/E 6.31x** `asof 07-22` | **Superseded by M206 (5.15–5.31x on 07-28, entirely on price).** ★ **S37's own registration text says the 6.31x is re-pulled at scoring** | DEEP-IT re-pulls; no stage may quote 6.31x as current |
| **M16 · credit `asof 07-20`** | Superseded — **M223: HY OAS 2.81%, a 4th consecutive widening, +18bp off the 365-day low**; **NFCI −0.552 is 12 days stale** | MACRO pulls fresh (EXIT CHECK enforces the credit axis) |
| **M125 · COT `asof 07-21 Tue close`** | **8 days old and structurally unrefreshable until 07-31** | S32 owns it; may be cited only with its asof |
| **000660 flow suspension** | **EXTENDED, not lifted.** R13 killed the "resolves 07-29" belief on named KSD testimony | **S17's window OPENS TODAY** — the premium becomes a daily-printing observable. This is a **dig instruction**, not a lifting |
| **⚠ D61 — 7th consecutive run** | `CATALYST_WATCH.json` **regenerates the R13-retracted claim verbatim, dated TODAY**: *"2026-07-29 SK하이닉스 ADR ↔ 원주 양방향 전환 개시 … 전환 개시로 차익거래가 열리면 프리미엄이 붕괴한다."* **On the very date it names, it reads like fact.** | **Named here BEFORE any stage uses the calendar. No stage may carry it.** The fix is a data edit to `data/catalysts/structural_schedule.json` and needs a human |
| **⚠ D18 — partial, on the US side** | Today's `CATALYST_WATCH` **does** carry FOMC · PCE · META · VLO · STNG · MA · the SPA. It carries **NO** row for **MSFT · STX · V · GD · AMZN · EQIX · XOM**, nor for the **seven regulated utilities S35 brackets** (WEC/ETR 07-29; EXC/SO/XEL/AEP 07-30; D 07-31) | Consistent with the 07-29 KR restatement: **the defect is single-name earnings source coverage, not window length.** The desk's own bracket book is more complete than the calendar seeding it |
| **`asof` on §2 rows M1–M19** | seed-dated, ≥7 days | May be cited **with** the asof; **M1 is the regime call's spine and is due a refresh at S3** |

---

## 7 · RESEARCH triggers loaded as BINDING CONSTRAINTS — which group binds which stage

Loaded from `handoff/RESEARCH.md` in **trigger form**, not as a summary. The rule this file exists for:
three of the 07-22 reversals broke rules that already existed but were written as prose in a folder
`pipeline/` referenced zero times.

| Group | Fires when | IDs | **Binds, this run** |
|---|---|---|---|
| **C** | you cite a number | C1 baseline·C2 both halves·C3 unknown column·C4 "indistinguishable"·C5 arbitrary choice | **EVERY stage.** ★ **C2 is on point today**: SK hynix printed a record margin AND a miss; MACRO quotes both |
| **S** | you make a statistical claim | S1 date-fold·S2 diagnose the null·S3 power first·S4 in-sample≠done·S5 short samples·S6 future labels | MACRO · SWEEP · DEEP. ★ **S1 is on point**: a one-session crash is **n≈1**, not n=22 |
| **D** | you read data | D1 second venue·D2 proxy sign·D3 signed/unsigned·D4 regime contamination·D5 cross-provider·**D6 signal grade (OBV = C)** | **SWEEP · ALPHA · every DEEP.** ★ **D5 is on point**: US has no investor-type feed, so the substitute is short-pressure + COT *positioning* = context, never a trigger |
| **W** | you write a conclusion | W1 cross-market transfer·W2 inherited lead/lag·W3 real≠profitable·W4 name the customers·W5 sub-sector dispersion·W6 reader's-market spine | **ROTATION · DEEP · BET.** ★ **W1 is on point**: a KR crash session is **not** a US observable (the 07-28 run already dropped a bracket for exactly this). ★ **W5 is on point**: MU rising while SKHY falls on one print |
| **L** (lenses) | — | L1 second derivative · L2 peak-margin trap · L3 branch information content | **DEEP · PREMORTEM.** ⚠ **L2 has two structural blanks: VLO (D56, 4 runs) and every KR ticker (D70).** A blank is `unknown` (C3) — **it may not be converted into "cheap"** |

★ **Two staged rules promoted to binding for this run** (two independent instances in four days is the
argument the 07-28 run made for promoting them; a human has not ruled, so they bind here and are
escalated again, not executed as a code change):
- **L3-bis** — *a bracket whose observable can settle on frozen prices is not a test.* Before freezing
  any rolling-window threshold, compute what it reports **if nothing happens**. (M135, S33.)
- **D82** — *before freezing a relative-return observable, check the legs' betas and state what the
  bracket reports on a large benchmark move.* (S33-ANNEX; **S39 applied it at registration**.)
- **D95 rider** — any residual claim must carry its noise band **and** state that the band is hand-set.

---

## 8 · The dig list, ranked FOR THIS RUN

| # | Dig | Why it is ranked here today | Owner stage |
|---|---|---|---|
| **1** | **The SKHY-miss / MU-rise dispersion (§0-b)** | It is a live, dated, two-sided test of **C8 / S30** on the desk's own regime call, and it arrived overnight. **W5 forbids compressing it.** | MACRO → DEEP-IT |
| **2** | **BX** — Financials' #1 flow, zero thesis | An unowned coverage gap of exactly the shape that surfaced 009150 and T. **Ranked #1 first-claim by the 07-28 run and still open.** No thesis may be built until a 4Phase exists | DEEP-FIN |
| **3** | **AAPL** — strongest two-window RS agreement in IT, no thesis, and it is one of the 28 unindexable tickers | Two independent reasons it stays invisible | DEEP-IT |
| **4** | **D74 settled-bar guard** | **Live today** — the sweep must be run pre-open or trimmed. Universe-wide contamination risk | SWEEP (§0) |
| **5** | **D78 — no stage owns "a BUILDING thread with no matching term bucket"** | This is how the desk missed CXMT's IPO week for four days. **MACRO must list every BUILDING/REIGNITED thread that maps to no bucket, and open a bucket or say why not** | MACRO EXIT CHECK |
| **6** | **D23 / W4 — refiner customers** | Closed at **4 of 5 with the 5th (UPS) REFUTING the other four** (S20 FIRED-B). **That is a dispersion finding, not a closure** — it needs a named cause, not a re-count | DEEP-ENRG |
| **7** | **D51 — no stage checks whether a flow reading post-dates a corporate event by 0–2 sessions** | Unresolved for 3 runs; **directly live tonight** (STX/META/MSFT print, and tomorrow's sweep reads the day after) | SWEEP · DEEP |
| **8** | **D9 · D10** ★ | **Open code defects the lab found, documented, and never fixed** (holdco concentration; news-body boilerplate ~55.6% at asiae). **Carried forward rather than re-discovered.** Human approval required | human |
| **9** | **D15 — PLAY23 has never produced a result** | The only experiment testing this repo's founding hypothesis. Its own README predicts "indistinguishable" at 27–31 rebalance points — **which is still worth knowing** | human |
| **10** | **D16 — estimate snapshot, day 8/~40** | Unrecoverable retroactively; every unstored day is gone | automated, verify it ran |

---

## 9 · ⚠ Reported finding — the handoff size budget, 8th consecutive breach

Measured at this run's start with `handoff_compact.py --budget-only`:

```
RESEARCH.md      150.1 KB  / 85   OVER by 65
SCENARIOS.md     122.1 KB  / 60   OVER by 62
STANDING_VIEW.md 151.3 KB  / 60   OVER by 91
TOTAL            432.7 KB  read in full at every HANDOVER
§2 fact rows: 153 · avg 0.48 KB/row (rule: ≤0.35)
```

**+40.2 KB since the 07-28 US run's own start-of-run measurement (392.5 KB)**, i.e. the ~30 KB/run
projection is now running **above** trend. **A desk reporting the same breach for an eighth time while
adding to it is reporting, not managing.** The two judgment-free fixes remain unmade and both need a
human: **(i)** fold the surviving per-run wrapper blocks into §2 (zero facts lost — the 07-25
compaction moved 154 facts and lost **0**); **(ii) split the files by market.** ★ **Measured cost of
not doing (ii), from this run**: this US HANDOVER read **~45 KB of KR-only per-name theses** (§3b, 22
rows) and the entire KR scoring log in order to produce a US report. **(ii) remains the
highest-leverage open item on the list.**

**This run's write-back discipline, pre-declared:** rows are **appended to §2**; §3a rows for names
this run touches are **OVERWRITTEN IN PLACE**; **no new per-run block is opened**; §5 is append-only
and byte-preserved.

---

## 10 · What this stage hands to MACRO

1. **The clock (§0)** — settled data ends **2026-07-28**; the sweep must not stamp 07-29.
2. **The regime call, inherited whole** — with the §4 asymmetry pre-encoded **before** tonight's prints.
3. **Two overnight items (§0-b)** as *dig instructions*, `[news]`-grade, bodies undrilled:
   the **SKHY record-miss with MU rising against it**, and the **oil re-escalation**.
4. **Twelve rows dated today that are NOT scoreable at this clock (§2b)** — and the explicit
   assignment of **S11/S18 to the KR desk's 07-30 run**.
5. **A clean `due` ledger, one legacy row closed (5 → 4), and a moved `score` (§3)** — carried as an
   accumulating observation, not as an edge.
6. **The 28-ticker indexing blindness (§4d)** — any "no coverage" claim about T/MA/V/GS/CB/WELL/ICE/
   SO/D is uninterpretable.
7. **D61's retracted-claim regeneration (§6)**, named before the calendar is used.
8. **The trigger groups as binding constraints (§7)**, plus L3-bis / D82 / D95 promoted for this run.

---

## ✅ EXIT CHECK

- [x] `STANDING_VIEW.md` · `SCENARIOS.md` · `RESEARCH.md` all read **in full**; `module_report_tags show`
      cross-queried and reconciled in §4 (with its own measured blind spot declared).
- [x] **Retracted ledger read BEFORE forming today's view** (§5) — no claim in this file matches a
      retracted entry; R13/R25/R26 are named as live traps for downstream stages.
- [x] **Every past-dated scenario scored** (§2a) — `EXPIRED` = 0, silent skips = 0. Rows dated **today**
      are named as not-yet-scoreable with the reason (§2b), and **S11/S18 are handed to a named desk
      and date** rather than dropped.
- [x] **`reject_ledger.py due` run this HANDOVER, first, not substituted with `score`** (§3).
      Rows surfaced with a passed date: **0**. Legacy count reported (**5**) and **reduced to 4** by one
      audited resolution on fresh evidence.
- [x] Stale rows flagged with their `asof`; the one suspension whose window opens today (**S17**) is
      converted into a dig instruction, **not** into a lifting of the R13/D1 suspension (§6).
- [x] `[measured]` / `[inferred]` tags preserved on every carried claim; **§0-b is tagged `[news]` and
      is explicitly not passed downstream as evidence.**
- [x] RESEARCH triggers loaded as binding constraints, grouped **C/S/D/W + L**, with the stage each
      group binds stated (§7) — not summarized.
- [x] `HANDOVER.md` written to `llm_outputs/2026-07-29/industry_US/`. `handoff/*.md` write-back happens
      at run end, per the stage contract (discipline pre-declared in §9).
- [x] **No position sizing, no buy/sell language anywhere.**
