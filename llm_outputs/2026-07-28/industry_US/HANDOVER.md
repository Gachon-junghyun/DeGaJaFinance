# HANDOVER — industry_US · 2026-07-28 (Tue)

> Stage 1/10. Inherits the analytical carry before any new view is formed.
> Sources read in full: `handoff/STANDING_VIEW.md` (433 lines) · `handoff/SCENARIOS.md` (1,203 — every
> scenario block and every scoring-log block) · `handoff/RESEARCH.md` (Parts A/B in full, Part C dig
> list in full) · `handoff/README.md` · `module_report_tags show` · `scripts/reject_ledger.py due` ·
> `scripts/handoff_compact.py --budget-only` · `module_macro_us` · `module_KIS` (primary KR closes) ·
> `module_disclosure` (DART) · `llm_outputs/2026-07-28/CATALYST_WATCH.json`.
> **This stage transports analysis. Zero buy/sell language, zero sizing (P4).**

---

## 0 · Run clock — binding on every downstream stage

| | |
|---|---|
| Wall clock | **2026-07-28 22:1x KST = 09:1x ET, Tuesday** |
| US session state | **NOT OPEN** — the regular session opens 09:30 ET (22:30 KST). Pre-market only |
| Last settled US close | **Monday 2026-07-27** — ★ **genuinely new data**; the prior US run (07-27, 09:31 ET) could only read 07-24 |
| KR session state | **CLOSED and settled** — and it was a crash (see §0-b) |
| FRED `asof` | DGS2 **4.33 (07-24)** · DFII10 **2.43 (07-24)** · T10YIE **2.21 (07-27)** · HY OAS **2.79 (07-24)** · IG OAS 0.80 (07-24) · NFCI **−0.55 (07-17)** · **DTWEXBGS 120.71 (07-24) — it finally printed** · VIX 18.58 (07-24) |
| Prior US run | 2026-07-27 09:31 ET (read the 07-24 settled close) |
| Prior run of any desk | `industry_kr` 2026-07-28 ~08:2x KST (ended before both the KR close and the KR crash) |

### ★ What is genuinely new to this desk since the last US run

1. **One full settled US session (07-27).** Unlike the 07-27 run — which fired one minute into a live
   session and could add no price-derived delta — this run has a real new bar. **D74's settled-bar
   guard is satisfiable today**: the sweep must stamp `asof 2026-07-27` and every RS/OBV/`vol_surge`
   axis must come from that settled bar, never from the 07-28 pre-market.
2. **UPS printed pre-market this morning — the window's first binary (S20).** Scored in §2 below.
3. **`DTWEXBGS` printed for the first time in 11 calendar days**, which closed S12 at the KR desk's
   07-28 HANDOVER and retro-validated D46.
4. **A −10.8% KOSPI session settled while the KR desk was writing** (§0-b) — and its named driver is
   **CXMT**, i.e. the supply-side falsifier of *this* desk's own regime call (S34).

### 0-b · ★★ The KR settled close is materially worse than the number the KR run recorded, and this desk must not inherit the intraday figure

| Series | What the 2026-07-28 `industry_kr` run recorded (intraday ~10:1x) | **Settled close, primary** |
|---|---|---|
| KOSPI (종합) | −7.40% (M196) | **−10.84% → 6,023.66** `[KIS --futopt A05608 기초지수]` |
| KOSPI200 | −7.85% (M196 / S33-ANNEX) | **−11.55% → 945.69** `[same]` |
| `069500.KS` KODEX200 | −6.6% intraday (S33-ANNEX) | **−11.190% → 95,675** `[KIS --ohlcv, matches yfinance to the won]` |
| KOSPI200 near-month future | — | **−10.97%**, basis +0.85, 괴리율 **0.68% = orderly** |

⚠ **This is not a correction of the KR desk's judgment — it is the arithmetic consequence of a run that
ended before its own market closed.** But it has a hard downstream effect: **S33-ANNEX's beta-contamination
estimate was computed on a −7.85% benchmark and the real one was −11.55%, so the contamination it warned
about is ~47% larger than the ANNEX itself stated.** That is what makes S33 scoreable both ways in §2.
★ **The ETF did not dislocate**: 069500 −11.19% vs KOSPI200 −11.55% is ordinary tracking, so the frozen
observable's benchmark is clean. **No new D24-class provider dispute — KIS and yfinance agree exactly.**

---

## 1 · Inherited regime call — carried unchanged, not re-derived

**Memory is a price-cycle industry in rate-of-change deceleration while its level stays tight.**
`[inferred]`, built on M1–M6 / M18. Carried verbatim; this run does not re-litigate it.

Governing distinction (lens **L1**): a commodity-cycle equity tracks the **second derivative of price**,
not the level — which is why *"shortage persists"* (M7) and *"the stocks struggle"* are both true (C3).

⚠ **The regime call acquired a registered supply-side falsifier yesterday and this desk has never
argued it.** **S34** (registered 2026-07-28 by `industry_kr`) brackets **CXMT's wafer capacity**, not
demand. Every prior falsifier of the regime call — S3, S4, S13, S16, S24, S30 — is a **demand or price**
observable. **A price cycle is ended by supply as much as by demand, and until yesterday the book had
zero branches on the supply side.** MACRO and EVENT_ALPHA inherit this as an open flank, not as a
resolved item. Corroborating carry: **M172** (CXMT IPO, ¥57.92bn explicitly for capacity, world #4 DRAM
at ~7.7% share, no HBM, DoD "Chinese Military Company"), **M195** (300k → 350k wpm by year-end; no EUV;
HBM 3–4 years behind), **M180** (`theme_age` CXMT **10.98× on n=187 — 2.0× the next-highest probe**,
the single cleanest separation the tool produced in four all-🟡 foreign runs), **D78** (the desk measured
itself missing a four-day 3→6→3→16-outlet build on this exact story).

---

## 2 · Scenarios scored this run

> Scored strictly against the **pre-registered observable and threshold** (L3 `scenario_score`).
> Zero thresholds were moved. Where the observable was ambiguous, that is recorded as a finding about
> the scenario's construction, not resolved by improvisation.

### S20 — UPS Q2 · event 2026-07-28 · **FIRED-B** (with a declared partial read)

**Frozen observable**: *"does the Q2 call quantify fuel expense YoY, and is FY guidance cut on fuel or
on volume?"* — categorical, deliberately (its only straddle expired pre-event at registration).

**Observed** `[company release via cnbc · nasdaq/RTTNews · wsj · yahoo_finance · marketwatch — 5 outlets]`:

| Line | Value |
|---|---|
| Adjusted EPS | **$1.76 vs $1.66 expected (LSEG)** |
| Revenue | **$22.834bn vs $21.81bn expected, +7.6% YoY** ($21.221bn) |
| GAAP net income | **$604m ($0.71/sh) vs $1.283bn ($1.51/sh) — down 53% YoY** |
| FY26 guidance | ★ **RAISED** — revenue **$91.2bn**, adjusted diluted EPS **~$7.22**; CEO Tomé: *"raising our full-year consolidated revenue, non-GAAP adjusted operating profit and non-GAAP adjusted diluted EPS guidance"* |
| Segment detail given | domestic revenue **+6%** (on revenue per piece), international **+12.5%**, supply-chain **+7.8%**, network-reconfiguration benefits **$1.2bn achieved / $3bn FY target** |
| **Fuel** | **Not mentioned in any of the five bodies** |

**Branch mapping, mechanically:**
- **Branch A** requires *fuel quantified up materially YoY* **AND** *a guidance cut attributed to fuel*.
  **Guidance was RAISED ⇒ A cannot fire**, regardless of the fuel leg.
- **Branch C** requires *a guidance cut on VOLUME*. **Guidance was RAISED ⇒ C cannot fire.**
- **Branch B** — *"fuel is a non-event in the call"* — is the only branch consistent with the observed
  release, and it is **positively supported**: five outlets itemised revenue-per-piece, international
  mix, supply-chain and network savings, and **none carried a fuel line**.

⇒ **Verdict `FIRED-B`.**
⚠ **Declared limit, not buried**: the frozen text says *"the call"*, and the **8:30 ET call transcript is
not in the corpus at run clock** (the feed carries only the *"Q2 26 Earnings Conference Call At 8:30 AM
ET"* notice). B is therefore scored on the **release plus five independent outlet write-ups**, not on the
transcript. **This does not change the verdict** — the guidance clause alone eliminates A and C — but the
fuel-quantification leg is `[partially verified]` and is filed as a dig (**D85**) for the next run.

**Registered meaning of B, carried forward verbatim**: *"Against us. The distillate bottleneck is absent
from the P&L of the buyer most exposed to it ⇒ the crack is a price, not a cost anyone is paying."*
⇒ **W4 / dig D23 closes at 4 of 5, not 5 of 5.** DAL/UAL/FDX/LUV all quantified fuel at **+66% to +84%
YoY** and two cut guidance on it (M34); **the largest US distillate buyer did not, and raised guidance.**
The refining thesis's *"real dollars move through the crack"* leg is now **corroborated at four airlines
and refuted at the one ground-freight name**, which is a dispersion finding (**W5**), not a clean close.

★ **Second-order read the downstream stages must carry, stated here so it is not discovered late**:
**S20's branch C was the registered falsifier of the promoted rail node** (CSX/UNP/NSC), and it did not
fire — freight volume was *not* cut. **S20-ANNEX's own numeric observable is NOT settled by this** and
remains armed to **2026-08-04** (median RS20 vs SPY of {CSX, UNP, NSC} turning negative; last read
**+11.7**). ⚠ And the **pre-declared no-information band (±6.9%) cannot yet be evaluated** — the US
session is not open. **No stage may read today's UPS price reaction as confirming anything** until the
07-28 settled close exists.

### S28 — SK이터닉스 임시주총 · event 2026-07-28 09:00 KST · **FIRED-A**

Pre-declared by the 07-28 `industry_kr` run as **"next run's #1 scoring job"** (the event fired 35
minutes after that run's start clock). **This is that run.**

**Frozen observable**: whether **both** KKR-nominated directors are elected.

**Observed** `[PRIMARY — DART 임시주주총회결과, rcpNo 20260728800373, filed 2026-07-28]`:

| Agenda | Nominee | Attendance | For | Against |
|---|---|---|---|---|
| 1-1 사외이사 | **Masahiko Kato** (KKR Infrastructure Japan, Director since 2024.09) | 47.6% | **99.4%** | 0.6% |
| 1-2 사외이사 | **Abhishek Sharma** (KKR Climate/Infrastructure Singapore, Director since 2024.04) | 47.6% | **99.5%** | 0.5% |

**Both elected. ⇒ `FIRED-A`.** The filing itself restates the linkage: the election is a **거래종결
정지조건** (condition precedent) under the **2026-03-06 주식매매계약** with **Eclipse Holdco L.P.**

**Registered meaning, carried verbatim**: *"The condition precedent clears ⇒ S22 branch A (closing
07-31) becomes materially more likely. **This is not itself a closing.**"* ⚠ **S22 is not re-frozen and
is not pre-scored** — its observable remains *"does the SPA close on 2026-07-31 per DART"*, and its kill
remains **a second deferral, nothing else**. ★ **S28 did exactly what it was registered to do**: it
delivered a read on 07-28 that would otherwise have waited until 07-31, from a DART filing **no calendar
carried** (D18's 8th occurrence at registration).

### S33 — KR refiners on the first session that knows the crack held · event 2026-07-28 close · ★★ **the two pre-registered readings DISAGREE, and that disagreement is the verdict**

**Frozen observable**: median excess return of **096770** and **010950** vs **`069500.KS`**, 2026-07-28
settled close. Thresholds: **A ≥ +1.5pp · B ≤ −1.5pp · C between.**
**S33-ANNEX** (registered the same day, pre-close, on the S14-ANNEX precedent) pre-committed that **both
the raw reading and the beta-adjusted residual be recorded side by side, and that if they disagree, the
disagreement is the finding.**

**Measured** `[KIS Open API primary closes; yfinance agrees to the won — cross-provider check per D5]`:

| | 07-27 close | 07-28 close | Return |
|---|---|---|---|
| `069500.KS` (benchmark) | 107,730 | **95,675** | **−11.190%** |
| 010950 S-Oil | 136,400 | **129,500** | **−5.059%** |
| 096770 SK이노 | 116,700 | **112,700** | **−3.428%** |

**Betas re-measured by this run rather than inherited** (rule **C1** — R20's lesson: measure any baseline
you were handed). 60 sessions ending **2026-07-27**, vs `069500.KS`: **010950 −0.118 · 096770 +0.237**
against the ANNEX's −0.120 / +0.241 ⇒ **reproduced, ≤0.004 apart.**

| Reading | 010950 | 096770 | **Median** | Branch |
|---|---|---|---|---|
| **Raw excess (S33 exactly as frozen)** | +6.131pp | +7.762pp | **+6.947pp** | **A** (≥ +1.5) |
| **Beta-adjusted residual (S33-ANNEX)** | **−6.374pp** | −0.771pp | **−3.573pp** | **B** (≤ −1.5) |

⇒ **Verdict: `FIRED-A` on the frozen observable, and the beta-adjusted residual fires `B`. Both are
recorded; neither is discarded; the threshold was not moved.**

★ **What this actually measures.** On a −11.19% benchmark day, pure beta alone predicts an excess of
**+12.53pp (010950) and +8.49pp (096770), median +10.51pp**. The realised **+6.95pp is 3.57pp BELOW what
frozen mechanics predict.** So the honest statement is: **the refiners did not outperform on the crack
news — they underperformed their own beta while the tape fell around them.** The raw `A` is the artifact
S33-ANNEX predicted before the close, and it predicted it **at a smaller magnitude than reality
delivered** (ANNEX estimated the benchmark at −7.85%; it settled at −11.55%).

⚠ **What this does NOT do.** It does **not** close **C4** (margin vs war premium). The registered
information delta — *"the first KR session that opens with the crack's recovery public"* (M188) — was
**overwhelmed by a −10.8% index event whose named driver is CXMT, an unrelated axis.** Per **S1**, this
is **n = 1 on a contaminated date**. The correct carry is: *one vote for the war-premium reading on the
adjusted axis, no vote on the raw axis, and the test itself was swamped.*
★ **This is the first KR instance of the staged rule L3-bis** (*a bracket whose observable can settle on
frozen mechanics is not a test*) **and the second instance overall** — the first being **M135**, where the
exchanges' RS60 test reported CONFIRM on unchanged prices. **Two independent instances in four days is
the argument for promoting L3-bis and D82 out of the staging area.** Escalated to a human, not executed.

### Scenarios explicitly NOT scored, with the reason

| ID | Event date | Why not scored |
|---|---|---|
| **S32** | COT covering the **2026-07-28 Tuesday close** → window to 07-31 | ⚠ **The CFTC release covering today's close publishes Friday 07-31.** The observable does not exist yet. **Not EXPIRED, not pending — not yet published.** Scoring it off today's tape would be scoring a price reaction, which is exactly what the bracket's own registration text forbids |
| **S20-ANNEX** | → 2026-08-04 | Its frozen observable is a **median RS20 to 08-04**, not the print. Armed |
| **S22** | 2026-07-31 | Not due. S28's FIRED-A is a **leading read**, explicitly not a pre-score |
| S2 · S9 · S11 · S13 · S16 · S17 · S18 · S19 · S23 · S24 · S30 | 2026-07-29 (→ 08-05/08-12) | **Tomorrow.** The densest date on the book |
| S14 · S14-ANNEX · S14-num · S15 · S21 | 2026-07-30 (S14 scores 08-06) | Not due |
| S25 · S26 · S29 · S31 | 08-05 / 08-06 / 08-08 / 08-12 | Not due |
| S3 · S4 · S5 · S27 · S34 | 08-11 / ~08-late / ~09 / ~09-10 / 10-31 | Not due |
| S6 · S7 · S8 · S10 · S12 | — | **Already scored** (S8 and S12 both closed by the 07-28 KR run) |

**Zero past-dated scenarios are unscored. Zero `EXPIRED` rows this run.**

---

## 3 · Rejection-ledger audit — `due` run first, never `score` alone

```
scripts/reject_ledger.py due   →  전체 58건 · 해소됨 18 · 레거시(감사필요) 7 · 재확인일 도래/경과 0
```

**0 rows have a passed recheck date.** The audit obligation therefore falls entirely on the **7 legacy
rows** (entered before `--revives-if` was enforced).

**Resolved this run (1):**

| Date | Ticker | Class | Fresh measurement | Outcome |
|---|---|---|---|---|
| 2026-07-15 | **000660 SK하이닉스** | `B.모멘텀only` — *"OBV −34 분배 into strength"* | `module_KIS`: close **2,082,000 (07-15) → 1,550,000 (07-28) = −25.6% over 9 sessions**; 07-28 alone **−14.65%** with **foreign −182.6만주 — the largest single-session sell of the 10-session window** — absorbed by retail **+141.4만주**; institution **+38.9만** does not offset. ⚠ And **M199** records that this name raised **₩39.89tn of equity on 2026-07-15**, the rejection's own date, which no desk file recorded at the time | **`reaffirmed`** — the distribution read is re-established on **fresh** evidence, not carried on the stale one |

**Legacy count 7 → 6.** Run-over-run: **18 → 12 → 7 → 6.** It is not sitting flat.

**Still pending, named rather than dropped (6)** — each has now crossed at least one HANDOVER unexamined
and is flagged here so the gap is visible, per `carryover.md` §3b:

| Date | Ticker | Class | Why it was not audited this run |
|---|---|---|---|
| 2026-07-11 | 103590 일진전기 | `A.flow미도착` | KR small-cap; no US-desk data path and no US read-across |
| 2026-07-16 | 105560 KB금융 | `E.상관가드` | Structural (risk-unit duplication vs 하나) — a **portfolio-construction** rejection, so a flow re-pull cannot resolve it; needs the KR desk's unit map |
| 2026-07-20 | 000810 삼성화재 | `H.밸류소진` | Same |
| 2026-07-22 | 005380 현대차 | `K.본문반증` | `narrative`-class — the ledger's **most expensive class** (the +41.2pp/+26.9pp rows were both narrative). ★ **Priority-1 audit for the next KR HANDOVER** |
| 2026-07-22 | 373220 LG에너지솔루션 | `K.본문반증` | Same class, same priority |
| 2026-07-22 | 454910 두산로보틱스 | `L.vehicle없음` | Same |

⚠ **The honest summary**: this run audited the one legacy row it could measure from the US desk's own
tooling and named the other six. **Three of the six are `narrative`-class** — the exact class whose two
worst rows cost the ledger +41.2pp and +26.9pp — and **none of the three has been re-opened since it was
filed on 2026-07-22.** That is the single sharpest carry item in this section.

---

## 4 · Reconciliation — what we BELIEVE vs what we COVERED

`module_report_tags show` (updated 2026-07-28T09:47, **30 reports · 183 tickers · 11 sectors**).

**(a) Coverage without a standing thesis — candidate first-claims.** Carried from the 07-27 run and
**still unclosed**: **T** (LIVE-shortlist **#1 flow +0.96**, no thesis in any file) and **AAPL**
(**+20.4 RS20 / +19.2 RS60 vs SPY — the strongest two-window agreement in IT**, 1 report, no thesis).
⚠ **T's `0` is a tool artifact, not a gap** — it is one of the 28 tickers `module_report_tags` silently
refuses to index (M152 / D65). **AAPL's 1 is real.**

**(b) Belief without coverage — and the number moved the wrong way again.** **M183's D60 erasure
reproduced across the 07-27 → 07-28 boundary.** Measured now:

| Name | Carried in STANDING_VIEW §3a | Ledger count today | Note |
|---|---|---|---|
| **AMT** | Real Estate duration unit (M131) | **1** | was **8** on 07-25 (M152). Erased by `REPORT/` filename collision |
| **CCI · IRM** | duration / data-centre units | **1 each** | held only by the 07-25 `SECTOR_DEEP_RE.md` |
| **PCG** | Utilities' only 🟢 | **1** | held only by the 07-25 `SECTOR_DEEP_UTIL.md` — **a file no run since has rewritten** |
| **NDAQ · MCO · MSCI · URI · WAB · ODFL · EMR · HD** | exchanges node / rail read-across | **0** | M183's measured erasure, **unchanged** |
| **GS · MS · CB · ICE · MA · V · WELL · T** | active theses in §3a | **0 (unindexable)** | D65 — the guard is sensible, **the silence is the defect** |

⇒ **Binding instruction to DEEP and BET this run, from M183's restated rule**: *to preserve an at-risk
ticker, put it in a **TABLE ROW with its name**, not in a prose list.* The 07-27 run proved the prose-list
form does not register.

**(c) Resolved-but-live.** None newly detected; the `🔴RESOLVED` tags on AMAT/WDC/KLAC/EQIX/DLR/VST are
freshness tags inside live files, not verdict closures, and their §3a theses remain argued.

---

## 5 · Retracted ledger — read BEFORE forming today's view

All 24 rows (R1–R24, R17 renumbered) were read first. The ones that **bind a stage this run**:

| # | The claim that must not resurface | Binds |
|---|---|---|
| **R5** | *"EDA weakness leads semis by 12–18 months."* Lag-12 ≈ 0.02–0.05 vs same-month 0.63 — **coincident** | MACRO, any lead/lag claim (**W2**) |
| **R7 / R10** | *"RE is the purest duration expression"* / *"IT+RE+UTIL are ONE risk concentration"* — both measured down. Surviving weak form: **shared catalyst ≠ correlation** | ROTATION, PREMORTEM |
| **R8** | *"PSX is the cheapest large refiner on forward"* — **false on a like-for-like basis.** `core_pick` is **human-locked** and was not modified | BET, ALPHA |
| **R11** | *"The long-end move is bear-STEEPENING"* — 2s10s **flattened**. ⚠ **This removed one of the FIN OW's two legs**; the survivor is breadth, itself narrowed (M40 → M173: **56% one holdco**) | MACRO, DEEP FIN |
| **R12** | *"The C4 detachment counter is at 4 consecutive"* — recount: **3 confirmed / 1 broken / 1 unconfirmed** | EVENT_ALPHA |
| **R19** | *"the diesel-minus-gasoline gap narrowed for the FIRST time"* — it narrowed on **10 of 24** sessions | DEEP ENRG |
| **R20** | *"a positive KR RS60 is a top-8% event"* — the baseline is **size-dependent** | any cross-market RS transfer (**W1**) |
| **R23** | *"STX GM is +15.1pp over its own prior peak"* — quarterly-vs-annual mix; like-for-like **+3.8pp**. **L2 still CONFIRMED on STX**; only the magnitude is withdrawn | DEEP IT |
| **R24** | *"475150 is driven by something STRUCTURAL, not thematic"* — +55.58%/wk then **−29.42% in one session** with three renewables peers. ⚠ **Direction stands, driver retracted** — the same shape as R15/M52 | ★ **live today**: S28 FIRED-A is a **structural** read on a name whose **thematic** half was retracted 24 hours ago. **Both are true. Do not let S28's clean A relaunch the retracted driver line** |

⚠ **R24 × S28 is this run's sharpest carry hazard** and is written here rather than discovered later:
scoring S28 `FIRED-A` is **not** evidence that R24 was wrong. R24 retracted *"it is not a theme"*, not
*"the structure is not real"* (scope discipline, **C4**). The two coexist.

---

## 6 · Stale flags and cleared suspensions

| Item | `asof` | State |
|---|---|---|
| **`DTWEXBGS` suspension** | printed **120.71 (07-24)** after 11 days | ✅ **CLEARED** — S12 scored `FIRED-B` on the frozen observable by the KR run; **decision axis stays `AMBIGUOUS` (D35)**. **D46 retro-validated: a ~5-business-day lag is now measured** |
| **000660 flow suspension (D1 / S17)** | — | ⚠ **NOT cleared. Its window OPENS TOMORROW (07-29 → 08-05).** The premium prints daily from 07-29, so **the R13-vs-donga dispute settles in numbers, not words**. ★ **Converted into a dig instruction, not a silent trust: HANDOVER of the next run must pull the ADR premium on its first available print** |
| **M161** (연기금 #1 net buyer of 000660) | downgraded 07-28 | ⚠ **`[UNVERIFIED]` — may not be cited as evidence** (D62 unclosable: `module_KIS --investor` cannot separate 연기금) |
| **NFCI** | **07-17, 11 days old** | Quoted with its date wherever S26 is referenced. It is weekly with up to 7 days' lag; 11 days is **outside** that — flag, do not theorize |
| **`data/cycles/cycle_registry.json`** | **updated 2026-07-17 = 11 days stale, 3 rows** | ⚠ Four of the board's top-six RS60 names sit in **no row at any layer** (D60). The cycle-GAP guard can only see cycles someone wrote down |
| **`REPORT/industry_US/SECTOR_DEEP_UTIL.md` · `SECTOR_DEEP_RE.md` · `SECTOR_DEEP_SEMI.md`** | 07-25 or earlier | ⚠ **D33: re-scanned into the ledger as if current.** PCG/AMT/CCI/IRM's entire coverage rests on them |
| **STANDING_VIEW §3a re-check dates falling inside this window** | — | TRV/CB **08-06** · JPM **08-08** · HLTH block **08-06** · VTR **07-30** · tankers **08-06** · PYPL **08-06** · SLB **08-21** · VRT **08-12** · CRWD **09-02** · LHX/PWR **08-12** · BKR **08-14** — **none due today** |

---

## 7 · RESEARCH triggers loaded as BINDING CONSTRAINTS — which group binds which stage

> Loaded in **trigger form**, not summarised. The measured reason this section exists: **three of the
> 2026-07-22 session's six reversals broke rules that already existed** — written as prose, in a folder
> `pipeline/` referenced **zero** times.

| Group | Fires when | IDs | **Binds, this run specifically** |
|---|---|---|---|
| **C** | you cite a number | C1 baseline · C2 both halves · C3 unknown column · C4 "indistinguishable" · C5 arbitrary choice | **MACRO** (C1: every RS/excess names its benchmark inline; C2: both halves of any CPI/export/print) · **every stage.** ★ **C1 was exercised in §2** — the S33 betas were re-measured, not inherited |
| **S** | you make a statistical claim | S1 date-fold · S2 diagnose the null · S3 power first · S4 in-sample≠done · S5 short samples · S6 future labels | **PREMORTEM · DEEP.** ★ **S1 is live today**: the S33 reading is **n=1 on a contaminated date**, and the 07-28 KR crash makes every same-day KR cross-section one observation |
| **D** | you read data | D1 second venue · D2 proxy sign · D3 signed vs unsigned · D4 regime contamination · **D6 signal grade (A/B/C — OBV is C)** · D5 cross-provider | **SWEEP · ALPHA · L2 indicators.** ★ **D74 is the operative form today**: the sweep must run off the **07-27 settled** bar, and **no agent may be handed a live `module_flow` RS number once 09:30 ET passes** |
| **W** | you write a conclusion | W1 cross-market transfer · W2 inherited lead/lag · W3 real≠profitable · W4 name the customers · W5 sub-sector dispersion · W6 reader's-market spine | **DEEP · BET · ROTATION.** ★ **W4 is directly at stake**: S20 leaves D23 at **4 of 5** with the fifth customer *refuting* the other four ⇒ **W5 (dispersion) now governs the refining customer read, not W4** |
| **L** (lenses) | — | L1 second derivative · L2 peak-margin trap · L3 branch information content | **DEEP · PREMORTEM.** ⚠ **L2 carries a live blank**: VLO's margin percentile is structurally unobtainable (D56, 3rd run) and **L2 forbids calling anything cheap without one** |

**Staged, not yet promoted — and two now have a second independent instance each:**
- **C6-bis** (an A-grade signal must also be LIVE) · **L2-bis** (use the industry's own earnings metric) ·
  **S1-bis** (overlapping windows are one observation) ·
  **L3-bis** (a bracket that can settle on frozen mechanics is not a test) — ★ **now 2 measured instances:
  M135 (exchanges RS60 CONFIRMs on frozen prices) and S33/D82 (a relative-return bracket settling on
  frozen beta). Promotion is a human call; escalated here, not executed.**

---

## 8 · The dig list, ranked for THIS run

**Analytical digs — candidate DEEP assignments:**

| Rank | Dig | Why now |
|---|---|---|
| 1 | **D1 — do LTA price floors actually hold margin?** | The best counterargument on file against the regime call (**C1** contradiction), and **S34 sharpened it**: if a funded 4th entrant is the supply risk, whether LTAs floor price is the whole question. Unmeasured for six runs |
| 2 | **D78 — MACRO must name every BUILDING/REIGNITED thread that maps to no bucket** | The desk measured itself missing a four-day build on **CXMT**, the single largest supply-side event for its own regime call. **No EXIT CHECK enforces it. This run should enforce it at MACRO** |
| 3 | **D23 → now a W5 question** | S20 leaves it 4 of 5 with the 5th name *contradicting* the other four. **The dispersion is the finding**; a DEEP should ask why airlines pay the crack and ground freight does not |
| 4 | **D3 — hyperscaler capex → memory revenue lead-lag, tested the way W2 demands** | Four capex prints land 07-29→07-31. Testing the lag **after** them is a wasted window |
| 5 | **D51 — does a flow reading post-date a corporate event by 0–2 sessions?** | Unresolved, and the rail node's promotion still rests on a snapshot 0–1 sessions after CSX/UNP/NSC filed |

**Defects, not questions — these cost a stage per run until a human clears them:**

| Dig | Status this run |
|---|---|
| **D18** | ⚠ **9th CONSECUTIVE OCCURRENCE, verified by string search not by eye.** `CATALYST_WATCH.json` (`--days 14`, as-of 07-28) is **missing UPS — which printed today** — plus **MSFT · AMZN · XOM · EQIX · STX · SPGI · FTNT · ICE · GD**, and every 07-29/07-30 utility print (**WEC · ETR · EXC · SO · XEL · AEP**). It carries META/VLO/STNG/MA/AMD/ANET/MPC/PSX/CEG/LNG/VST. ⇒ **the defect is single-name earnings source coverage, not window length** |
| **D61** | ⚠ **5th CONSECUTIVE OCCURRENCE.** The STRUCTURAL block **still** regenerates the **R13-retracted** claim verbatim: *"SK하이닉스 ADR ↔ 원주 양방향 전환 개시 … 전환 개시로 차익거래가 열리면 프리미엄이 붕괴한다"*, dated **tomorrow**. A data edit to `data/catalysts/structural_schedule.json`, human approval required, **not made here** |
| **D17 / D64** | `drift_watch` remote-unrunnable — **6th run** if it reproduces at DRIFT. The substitute `fts` sweep can only test phrases already thought of |
| **D52** | `capex cut` is now **six measurements deep at ~0**. Retiring it is a **definition change to a carried contradiction (C6)** — human |
| **D65** | 28 tickers silently unindexable. **Fix is "report `unindexable`, not `0`"** — human |
| **D74 / D75** | No settled-bar guard; `velocity` null on 300/300. **Operative today**: this run fires pre-open, so 07-27 is clean — **but the guard is still absent** |
| **D56 / D54** | VLO's margin percentile and Item 1A are **structural blanks**, 3rd run each. **No percentile invented** |
| **D9 / D10** | Holdco concentration; news-body boilerplate (asiae **55.6%**). Found, documented, never fixed. **Carried, not re-discovered** |
| **NEW · D85** | ★ **An earnings-call transcript is not in the corpus at a pre-open US run clock**, so a scenario whose frozen observable names *"the call"* is only partially scoreable on the morning after. Measured on S20 today. **Minimum fix: register earnings observables against the RELEASE (8-K/press release) where possible, and mark the call leg as a separate, later-settling line** |

---

## 9 · ⚠ Reported finding — the handoff size budget is breached for a 4th consecutive run

```
scripts/handoff_compact.py --budget-only   (2026-07-28, at this run's start)
  RESEARCH.md        121.4 KB / 85   OVER by 36 KB
  SCENARIOS.md        99.6 KB / 60   OVER by 40 KB
  STANDING_VIEW.md   128.1 KB / 60   OVER by 68 KB
  TOTAL              358.4 KB  read in full at EVERY HANDOVER
  §2 fact rows: 126  ·  avg 0.48 KB/row  (rule: ≤ 0.35)
```

The compactor's plan remains **0 archivable rows / 0.0 KB** — its `--age-guard 2` protects the two most
recent run-blocks and the 07-25 consolidation already moved everything older. **Nothing was hand-deleted**
(the README is explicit that this desk's most expensive measured errors come from *losing* carry).

★ **The number that has not yet moved a human**: at **+30 KB/run**, the next four runs add another
**120 KB**. The standing recommendation is unchanged and is **option (b) — split the files by market**
(`STANDING_VIEW_KR.md` / `_US.md`): a US run currently reads ~40 KB of KR-only per-name theses and a KR
run reads the mirror image. **It loses zero bytes and needs no judgment call.** ⚠ **Reported, not
executed — this is a human decision.**

⚠ **Second, cheaper item, also mechanical**: **five per-run `Added by …` wrapper sections still sit in
`STANDING_VIEW.md`** against the file's own rule that a run appends rows to §2. **Folding them loses zero
facts.** This run leads by example — it appends §2 rows and overwrites §3a rows in place.

---

## 10 · What this stage hands to MACRO

1. **The regime call, carried unchanged** — plus the explicit note that its **only supply-side falsifier
   (S34) was registered 24 hours ago and has never been argued by this desk.**
2. **Run-clock constraints**: last settled US close **07-27** (new); **no live `module_flow` RS after
   09:30 ET** (D74); the KR settled close is **−10.84% / −11.55%**, not the −7.4% / −7.85% in the KR
   run's own carry.
3. **Three scenarios scored** — S20 `FIRED-B` (W4/D23 stalls at 4 of 5, and the 5th name refutes the
   other four), S28 `FIRED-A` (KKR condition precedent clears; **not** a closing), S33 `FIRED-A` raw /
   branch-B adjusted (**the disagreement is the finding — L3-bis instance #2**).
4. **31 scenarios still armed**, of which **eleven settle tomorrow (2026-07-29)**. That is the densest
   date the book has ever carried and PREMORTEM's both-sides obligation keys off it.
5. **The binding rule groups** (§7) and the **ranked dig list** (§8), with **D78 named as a MACRO
   obligation this run**.
6. **Two ledger facts**: legacy rejections **7 → 6**, and **three `narrative`-class rows untouched since
   2026-07-22** — the ledger's most expensive class.

**No position sizing, no buy/sell language, no recommendation appears anywhere above (P4).**
