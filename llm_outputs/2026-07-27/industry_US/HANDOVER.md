# HANDOVER — industry_US · 2026-07-27 (Mon)

> Stage 1/10. Inherits the analytical carry before any new view is formed.
> Sources read in full: `handoff/STANDING_VIEW.md` (336 lines) · `handoff/SCENARIOS.md` (1,003 — all
> scenario + scoring-log blocks) · `handoff/RESEARCH.md` (660 — Parts A/B in full, Part C dig list) ·
> `module_report_tags show` · `scripts/reject_ledger.py due` **and** `score` ·
> `module_macro_us --json` · `llm_outputs/2026-07-27/CATALYST_WATCH.json`.
> **This stage transports analysis. Zero buy/sell language, zero sizing (P4).**

---

## 0 · Run clock — binding on every downstream stage, and this run's single largest constraint

| | |
|---|---|
| Wall clock | **2026-07-27 22:31 KST = 09:31 ET, Monday** |
| US session state | **OPEN — 1 minute into the regular session.** Today's bar is 1/390th complete |
| Last settled US close | **Friday 2026-07-24** |
| Price/flow `asof` available | **2026-07-24 settled close — identical to what the 2026-07-25 US run already read** |
| FRED `asof` | daily curve **2026-07-23** (DGS10 4.71 · DGS2 4.37 · DFII10 2.43 · HY OAS 2.77 · IG 0.79 · VIX 18.70). `T10YIE` **07-24 = 2.26** · `RRPONTSYD` 07-24 · `SOFR` 07-24 · `NFCI` 07-17 = −0.552 · **`DTWEXBGS` STILL 07-17 = 120.5315** |
| Prior US run | **2026-07-25 09:09 ET (Sat)** — read the 07-24 settled close |
| Prior run of any desk | `industry_kr` 2026-07-27 ~08:2x KST (read the 07-24 KR close) |

### ★★ The constraint, stated plainly so no downstream stage pretends otherwise

**There has been NO US trading session between the prior US run and this one.** The 07-25 run fired on
a Saturday and read Friday 07-24; today is Monday and the 07-27 session is one minute old. Therefore:

- **Every price, RS20/RS60, OBV, `vol_surge`, flow-score and 🟢/🟡/🔴 tag this run can compute is the
  same 07-24 data the 07-25 run already computed.** Re-deriving them and presenting them as a new read
  would be a fabricated delta. SWEEP must stamp `asof 2026-07-24 (unchanged from the prior run)` and
  ROTATION may not report a "change" on any price-derived axis.
- **The 07-27 intraday bar is forbidden as an input.** This is exactly the R17 / R17-b / D48 failure
  class — an unsettled bar entering the carry as `[measured]` and surviving a whole run. At 09:31 ET
  there is no defensible caveat; the number simply does not exist yet.
- **The curve has not moved either** — FRED's daily block still ends 07-23, so P1's rate framing
  inherits unchanged and must not be re-argued as if new.

**What IS genuinely new to this desk this run**, and therefore what it can honestly add:

1. **News flow 2026-07-25 → 2026-07-27 pre-market** (weekend + Monday) — the only live axis.
2. **`T10YIE` 07-24 (2.26)**, `RRPONTSYD` and `SOFR` 07-24 — three series that advanced one day.
3. **Carry hygiene**: scoring, the reject-ledger audit, and the stale/suspension sweep.
4. **A pre-event bracket audit of the densest catalyst cluster the book has ever carried** —
   **07-28 UPS → 07-29 FOMC + the six-trigger cluster → 07-30 PCE + VLO/MA/EQIX/FTNT/STX → 07-31 XOM.**
   This run sits on the last full day before it. That is where its information content is, not in a
   flow re-read that cannot have changed.

⚠ **Live today, and it expires today**: MSFT / META / AMZN straddles all **expire 2026-07-27**, before
their own 07-29→07-31 events (M89, 4th consecutive run). Any implied-move number pulled for those three
after today's close covers a *different* window than the event and is inadmissible as an event threshold.

---

## 1 · Inherited regime call — carried unchanged, not re-derived

**Memory is a price-cycle industry in rate-of-change deceleration while its level stays tight.**
`[inferred]`, built on M1–M6 / M18. Carried verbatim; this run does not re-litigate it.

The governing distinction (RESEARCH lens **L1**): a commodity-cycle equity tracks the **second
derivative of price**, not the level. "Shortage persists" (M7 — new capacity mid-2027 / 2028) and
"stocks struggle" (M1 — contract QoQ **+90~95% → +58~63% → +13~18%**) are both true simultaneously.
**C3 binds every proposition built on either half: citing one alone quotes half the state.**

**The asymmetry governing every print in the 07-28→07-31 window** (STANDING_VIEW §4, verbatim):

> **A hyperscaler capex CUT changes the thesis. A capex RAISE only moves its timing.**

S1 already fired the raise branch (Alphabet $180–190B → **$195–205B**). None of that touches M1/M2/M18,
because the same buyers signed the price caps. **S13** remains the pre-registered bracket for the branch
the book does not otherwise contain — a capex *raise* priced as a *margin drag* — and **C6** records that
this branch was measurably **un-narrated** before it first fired.

---

## 2 · Retracted ledger — READ FIRST, before today's view forms

**22 rows live in STANDING_VIEW §5 (R1–R22, append-only; R17 is absent by numbering, R19 was renumbered
at run end).** The full ledger was read before any view formed. The rows that **bind this run's
downstream stages** are reproduced here so no stage can re-discover them as new:

| # | The claim that must not resurface | What killed it |
|---|---|---|
| **R7** | "Real Estate is the purest duration expression on the board" | The tape inverted it, then **M133** went further: the lowest-beta names **lead the downside** while hotels/office (HST +17.4, BXP +14.0) beat WELL ⇒ **an operating-recovery rotation mislabelled as duration** |
| **R8** | "PSX is the cheapest large refiner on forward" | FY26 consensus: **MPC 8.8× · VLO 9.4× · PSX 10.8×** — PSX is the most expensive of the three. ⚠ **`core_pick` is a human-locked field and still reads PSX**; the claim is retracted, the field is not this desk's to change |
| **R10** | "IT + RE + UTIL underweights are ONE risk concentration" | Four separate residual units. ⚠ **M148 later split the verdict**: **FALSE for the RE leg** (DLR–MSFT −0.061) and **TRUE for the UTIL leg** (VST–CEG +0.768, VST–NVDA +0.354) |
| **R11** | "The long-end move is bear-STEEPENING — term premium, not cut-pricing" | 2s10s **flattened** on a 2y at a 120-day high. **This removed one of the Financials OW's two legs**; the survivor is breadth alone, itself weaker than first written (M40) |
| **R12** | "The C4 detachment counter is at 4 consecutive observations" | Settled closes broke the streak on 07-22. Corrected to **3 confirmed / 1 broken / 1 unconfirmed** — and **D53** then measured the counter to be **under-powered by construction** (r≈0.30 ⇒ a 3-day sign disagreement occurs ~6.5% of the time by chance) |
| **R17 · R17-b** | "The crack fell −11.2% on 07-23" / "the first negative weekly Δ in the series" | Unsettled-bar artifacts. **R17-b survived R17's own correction** because nobody re-derived the downstream number ⇒ **D48**: when a figure is retracted, grep the run for every number derived from it *before the run ends* |
| **R19** | "the diesel−gasoline gap narrowed — the FIRST narrowing of the run-up" | It narrowed on **10 of 24 sessions**, including a larger one on 07-15. **The 07-24 narrowing survives as n=1; the word "first" and every inference resting on unprecedentedness are withdrawn** |
| **R20** ★ | "the KR RS baseline is the 828-name median, so positive RS60 is a top-8% event" | Size-unadjusted (KR-side, but the **method** binds here): a universe median is a small-cap median. **The US mirror is already measured and clean — M74/M145: RS20>0 on 51.7%, RS60>0 on 48.7% vs SPY ⇒ no baseline subtraction is required for US RS numbers** |
| **R22** ★ | "SK이노 · S-Oil · GS are ONE bet (residual ρ 0.77)" | GS is not a refiner. ⚠ **Scope discipline to copy**: the retraction did **not** re-measure ρ, so it retracts *"same bet"* without asserting *"different bets"* (**C4**). A label correction does not re-measure the statistic built on the old label |

⚠ **The meta-pattern, and it is the one this run is most exposed to.** Of the last ten retractions,
**R14 · R15 · R16 · R18 · R19 · R20 · R21 · R22 were all written by a run's own earlier stages and
killed by its own later ones** — five KR instances plus the US pair. The verifying stages (DEEP,
PREMORTEM, DRIFT) run *after* the asserting stages (MACRO, SWEEP, ROTATION), so an assertion gets ~4
stages of life before anything checks it. **The 07-27 KR run executed the counter for the first time**
(R20 was propagated to all five carrying files before the run ended) rather than merely logging it.
**This run inherits that standard, not the older one.**

---

## 3 · Scenario status — every past-dated row settled or explicitly named

**Read: 29 registered scenarios (S1–S29) plus S14-ANNEX, S14-num and S20-ANNEX.**

### 3a · Past-dated rows — the complete list

| ID | Event date | Status carried in | Verdict this HANDOVER |
|---|---|---|---|
| S1 | 2026-07-22 | scored 07-23 | **FIRED-A** — settled, no action |
| S6 | 2026-07-23 | scored 07-24 | **FIRED-A** — settled |
| S7 (backlog + band) | 2026-07-23 | scored 07-23 / 07-24 | **FIRED-A, branch complete** — settled |
| S10 | 2026-07-24 | scored 07-24 | **FIRED-B** (12.5%) — settled |
| **S12** | **2026-07-23** | **PENDING, 4 prior checks** | ⚠ **STILL PENDING — 5th check. See below.** |

**Every other ARMED row is future-dated or undated.** Verified row by row: S2 (07-29) · S3 (~09/10) ·
S4 (~09) · S5 (~08-11) · **S8 (undated `[blank]` — cannot expire)** · S9 (07-29 + running) · S11 (07-29) ·
S13 (07-29) · S14 + ANNEX + num (07-30) · S15 (07-30) · S16 (07-29) · S17 (07-29→08-05) · S18 (07-29) ·
S19 (07-29) · S20 + ANNEX (**07-28, tomorrow**) · S21 (07-30) · S22 (07-31) · S23 (07-29) · S24 (07-29→31) ·
S25 (→08-08) · S26 (→08-12) · S27 (~08 late) · S28 (**07-28 09:00 KST**) · S29 (08-06).
**Zero silent skips.**

### 3b · ⚠ S12 — 5th consecutive carry, and it is named as a process failure, not waved through

`DTWEXBGS` pulled fresh this run: **120.5315, asof 2026-07-17 — byte-identical for the 5th consecutive
check** (07-24 US · 07-25 KR · 07-25 US · 07-27 KR · **07-27 US**), now **10 calendar days unprinted**.
120-day range unchanged **[117.4396, 121.412]**.

- **The decision axis is already `AMBIGUOUS`** (D35): the branches were *hawkish surprise* (A) and
  *hold-with-**dovish**-tilt* (B); what happened — **hold with a hawkish tilt** — is in neither.
- **The FX axis cannot settle inside its own window by construction** (D46): a **3-session**
  invalidation window was written on a series with a **~5-business-day publication lag**.
- **The frozen deadline is 2026-07-28 — tomorrow.** Per the frozen instruction: if it has still not
  printed then, score **`AMBIGUOUS`** with the reason and **substitute no proxy**.
- ⚠ **The 07-27 KR run pre-declared that "a 5th carry IS a scoring failure and must be logged as one."
  This is the 5th carry, and it is logged here as one.** It is a failure of the *bracket's construction*
  (D46), not of anyone's attention — but the desk does not get to call a construction failure a neutral.
- **This run does NOT score it early.** The deadline is frozen at 07-28 and a print tomorrow could
  still carry a post-event value; moving the verdict forward by a day to tidy the ledger would be the
  same class of act as moving a threshold. **Whichever desk runs on or after 2026-07-28 must score it.
  A 6th carry is not available.**

### 3c · Brackets that settle inside the next four sessions — the pre-event state, inherited not re-derived

**Tomorrow (07-28): S20 + S20-ANNEX — UPS Q2, the window's first binary.** It is two tests at once:
it closes **W4 / dig D23** (the refiners' 5th and last unread customer, after DAL/UAL/FDX/LUV printed
fuel costs **+66% to +84% YoY**), and it is the pre-registered **falsifier of the rail node**
(frozen observable: median RS20 vs SPY of {CSX, UNP, NSC} turning negative by 08-04). ★ It carries
**the only genuinely event-priced straddle on the board** (±6.9%, 1.81× √5·σ20) on a **complacent**
option book (P/C 0.35, skew +11.1). ⚠ **UNP is double-hit on branch B** — ~8 of its 12 revenue growth
points are fuel surcharge (M91), so a volume cut plus a rolling crack is one shock counted twice.

**07-29 — six triggers on one day**, of which four are US: FOMC (**S19** hike branch · **S23**
bear-flattener-hold branch · **S9** dovish branch), MSFT/META capex (**S13** · **S16** · **S24**),
V (S14 family), STX. **07-30**: June PCE (**S15**), VLO, MA (**S14-num**), EQIX (**S25**'s second
settling point), FTNT, STNG (**S21** — delivers **S8 branch A** without needing a Hormuz statement).
**07-31**: XOM, and the KR-side S22.

⚠ **Pre-registered n≈1 warnings that bind any reading of that week**: (i) FOMC 07-29 and PCE 07-30
**share one driver (oil), one day apart — they are not two observations** (S19); (ii) S24's four
Utilities names are **one residual unit**, not four (VST–CEG +0.768).

⚠ **Date-provider dispute declared and NOT resolved (D5)**: this desk carries MSFT/META 07-29 and
AMZN 07-30; `yfinance` returns MSFT 07-30 · META 07-30 · AMZN 07-31 · V 07-29 · STX 07-29 · EQIX 07-30 ·
XOM 07-31 · PSX 08-05. **Every bracket above is written on an observable with a window, so a one-day
calendar error cannot void any of them** — that was the point of writing them that way.

---

## 4 · Rejection-ledger audit — `due` run, not substituted with `score`

`python -X utf8 scripts/reject_ledger.py due` — **54 rows · 12 resolved · recheck-date due: 0 ·
legacy (no `revives_if` ever set): 12.**

- **Zero rows are due today.** The four US rejections filed 2026-07-25 all carry live dates:
  **SLB 08-21 · VRT 08-12 · CRWD 09-02 · PYPL 08-06** — none reached.
- **Legacy count trend: 21 → 19 → 18 → 12.** This is the health metric the L3 unit asks for, and it is
  **falling, not flat.** The 07-27 KR run closed six in one pass.
- **All 12 remaining legacy rows are KR names** (일진전기 · SK하이닉스 · 신한지주 · 두산에너빌리티 ·
  KB금융 · S-Oil · 한미반도체 · 삼성화재 · 롯데렌탈 · 현대차 · LG에너지솔루션 · 두산로보틱스).
  **This US desk does not own them and does not audit them from here** — three of them (000660, 010950,
  105560) carry live theses in STANDING_VIEW §3b whose owner is `industry_kr`. **Named here rather than
  dropped**, so the carry is visible: the US desk contributes **zero** legacy rows to this backlog.
- `score` (context, never a gate): **37 scored · 26 noise (70%) · loss-sum +103.2pp vs gain-sum −93.0pp.**
  The tail is still on the loss side — **rejection is not a symmetric act.** By type: `narrative`
  **+11.8pp (n=7)** · `measured` **−2.1pp (n=24)** · `structural` **−3.4pp (n=6)**. ⚠ Class n runs 1–7;
  **these are accumulating observations, not a validated edge (P4).** Do not promote any class average
  into a rule this run.

---

## 5 · Stale-check and cleared suspensions — every one converted into a dig instruction

| Carry | `asof` | State |
|---|---|---|
| **`DTWEXBGS`** | 07-17 | **10 days stale.** Blocks S12. No proxy permitted |
| **FRED daily curve** | 07-23 | 4 calendar days; expected (07-24 publishes this afternoon ET). **Not** a defect — do not log it as one |
| **CFTC COT (M125)** | 07-21 Tue close | Stale by construction — next release covers 07-28. **The 79-percentile-point NDX-short / SPX-long spread is carried unchanged into the print week and cannot be refreshed before it** |
| **FINRA short-vol** | 07-24 | Current. ⚠ **D52 binds**: the z is a statement about how unusual a name's *own* short-volume share is, not about covering. Report the baseline beside every z |
| **Cycle registry** (`data/cycles/`) | 07-17 | **10 days stale, 3 rows.** M146: the ✅ clears by **1.1 basis points** on mark-to-market drift with the held set unchanged across five runs ⇒ treat |margin| < 0.5pp as **UNRESOLVED, not PASS** (D61) |
| **`REPORT/industry_US/`** | mixed | `SECTOR_DEEP_SEMI.md` and `SECTOR_DEEP_UTIL.md` are **2026-07-15, undated, and re-scanned as if current** (D33, 3rd occurrence) |
| **000660 flow suspension** | live | **EXTENDED, not cleared** (R13). Its expiry is now an *observable* (S17: the ADR premium), not the 07-29 date. ⚠ **D61: `catalyst_calendar` is still regenerating the retracted 07-29 conversion claim — 3rd run** |
| **K8 — R7's replacement observable** | **opens today** | *"the next fresh non-overlapping 20-session block, ≈07-27 → 08-21."* ★ **This is a dig instruction that starts on this run's date**: R7's carried 18–24pp is **5.7×–7.7× the independent base rate** (M130 — rank 26 of 26, +1.98σ), so the next clean block is the only honest test of it. **DEEP RE must not re-cite the old block as if it were fresh evidence.** |

**Suspensions that have NOT cleared and must not be quietly trusted**: 000660 foreign flow (above);
`drift_watch` remote execution (**D17/D64 — 4 consecutive runs**, and the KR substitute is now measured
broken too, D68); `module_news_data burst` (D55, timed out twice on the last US run).

---

## 6 · RESEARCH rules loaded as binding constraints — grouped by firing moment

Loaded from `handoff/RESEARCH.md` Part A (21 triggers) + Part B (3 lenses). **Binding, not summarized.**

| Group | Fires when | IDs | Binds these stages this run |
|---|---|---|---|
| **C** | you cite a number | C1 baseline named in-sentence · C2 both halves of a print · C3 keep an unknown column · C4 say *indistinguishable*, not *rejected* · C5 expose the arbitrary choice | **MACRO · every stage.** C1 is live at maximum force: **SPY must be named in the same sentence as every RS number**, and M74/M145 mean **no baseline subtraction is applied to US RS** (that is the KR-only correction R20 re-scoped) |
| **S** | you make a statistical claim | S1 fold by date · S2 diagnose the null · S3 power first · S4 in-sample ≠ done · S5 short samples invent structure · S6 tag future-using labels | **PREMORTEM · DEEP · any stage citing a t or a counter.** ★ **S1 binds hardest this run**: with no new session, any cross-sectional agreement is **n≈1 on the 07-24 date**, not n=300 |
| **D** | you read data | D1 second listing venue · D2 proxy sign · D3 signed vs unsigned · D4 regime contamination · D5 cross-provider · **D6 signal grade (A/B/C — OBV is C)** | **SWEEP · ALPHA · DEEP.** ⚠ **The US has no B-grade investor-type feed at all** — KR's KIS foreign/institution actuals have no US equivalent. The substitute (FINRA short-pressure + COT percentile) is **positioning context, not a trigger**, and D52 says report its baseline. ⇒ **a US flow proposition that rests on OBV alone rests on a C-grade signal with no B-grade check available** |
| **W** | you write a conclusion | W1 market of measurement · W2 inherited lead/lag tested or tagged · W3 real ≠ profitable · W4 name the customers · W5 state sub-sector dispersion · W6 reader's-market spine | **DEEP · BET · ROTATION.** **W4 settles tomorrow on UPS** (D23's 5th customer). **W5 binds IT, Financials and Real Estate simultaneously** — all three are carried as single labels over legs that want opposite verdicts (C8, M136, M131) |
| **L** | lenses, not triggers | L1 second derivative · L2 peak-margin trap · L3 branch information content | **DEEP · PREMORTEM.** ⚠ **L1 is measured NOT to work on the crack series** (M129: P(4-week decline │ two negative accelerations) = **37.0%** against a **43.1%** unconditional base ⇒ the conditioning *subtracts* information). **L2 applies to MU and STX; it does NOT apply to WDC (+1.5pp over its own peak) and SNDK is UNMEASURABLE (no cycle in a 3-year post-spin series)** |

**Two `[inferred]` claims are carried and may NOT be cited as evidence downstream**: the regime call
itself, and *"NVDA/AVGO are a separate boat from memory."* Both keep their tags.

---

## 7 · Reconciliation — what we believe vs what the ledger says we covered

`module_report_tags show`: **30 reports · 178 tickers · 12 sectors**, updated 2026-07-27T09:46.

### 7a · Beliefs with no ledger coverage — corrected for the silent-blocking defect

⚠ **M152 / D65 first, because it invalidated the last run's version of this list.**
`module_report_tags/_extract.py`'s `_US_STOP` guard silently blocks **28 real universe tickers**:
`A · AIG · ALL · C · CAT · CB · COST · D · F · FAST · GS · ICE · KR · LOW · MA · MET · MS · NOW · O ·
ON · PEG · PM · Q · SO · T · TT · V · WELL`. **A blocked ticker reports `0`, not `unindexable`** —
which is why the 07-25 HANDOVER's "zero coverage" list mixed two different things.

- **`unindexable`, NOT gaps** — these carry live theses and real coverage the ledger cannot see:
  **GS** (§3a de-rate thesis, 4th run; 5 mentions in `SECTOR_DEEP_FIN.md`) · **MS · CB · WELL · ICE ·
  MA · V**. **Do not re-dig them and do not report them as uncovered.**
- **Genuine gaps closed by the 07-25 run**: AMT 0→8 · VTR 2→4 · SPGI 0→3.
- **Still genuinely thin**: **KNX**, and the **tanker complex (STNG · FRO · INSW · DHT · TNK)** — which
  is a different problem: they sit **outside `us_top300` entirely**, so this desk cannot tag them at
  all even though **S21 settles on STNG on 07-30**. That is an instrument gap, not a coverage lapse.

### 7b · Coverage with no standing thesis — unowned, and it is the same node three runs running

Heavy ledger coverage, no row in STANDING_VIEW §3a: **MSFT (10 reports) · AMZN (9) · META (8) ·
GOOGL (4) · AAPL (1).** The hyperscalers are the **buyers** whose disclosed spend the entire memory
chain rests on (**W4**), they are half of **S13 · S16 · S24**, and the desk holds **no per-name thesis
on any of them** — only the sector-level §4 asymmetry. ⚠ **This is the exact shape that surfaced 009150
as a KR DEEP candidate.** Named as a reconciliation delta for ROTATION to answer; **this stage adds no
names and takes no view (P4).**

### 7c · ⚠ D60 — naming the tickers this run's own file-copy will erase from the ledger

`REPORT/` is **one slot per filename**, so when this run copies its finalized reports in, the prior
file's coverage is **deleted from the ledger**. Measured across the 07-25 → 07-27 KR boundary: 009150
went **6→3**, 신한 **5→1**, KB **4→1**. The 07-27 KR run measured the free mitigation: **naming the
at-risk tickers in prose preserved them (ledger 168 → 178, M170).** Applying it here.

**US tickers whose ONLY ledger coverage sits in a file this run may overwrite:**

- `industry_US/SECTOR_DEEP_FIN.md` — **NDAQ · MCO · CME · MSCI · COIN · WFC · IBKR · SCHW · HOOD**
  (seven of these are the exchanges node whose registered test **M135 measured to be BROKEN**)
- `industry_US/SECTOR_DEEP_INDU.md` — **URI · WAB · ODFL · EMR · LMT · HD · RTX**
- `industry_US/SECTOR_DEEP_ENRG.md` — **SLB · CVX · BKR**
- `industry_US/EVENT_ALPHA.md` — **PWR · GEV** (both are S24 rip-names)
- `industry_US/HANDOVER.md` — **PYPL** · `industry_US/MACRO_REPORT.md` — **AAPL**
- Held by the two stale 2026-07-15 files, at risk only if those sectors are DEEP-picked:
  `SECTOR_DEEP_SEMI.md` — **ASML · ARM**; `SECTOR_DEEP_UTIL.md` — **AEP · ETR · SRE · EXC · DUK ·
  WEC · ED · XEL**

**The underlying reports are not lost** — `llm_outputs/{date}/` is date-partitioned; only the ledger's
view is. The structural fix (date-partition `REPORT/{desk}/`) is a **human decision** and is not taken here.

---

## 8 · Open contradictions carried forward — not resolved by picking a side

**C1** LTA price floors (unmeasured — the best counterargument on file against the margin-peak call) ·
**C3** level vs rate · **C4** refining: margin or war premium (⚠ its counter is measured **under-powered**,
D53) · **C5** security/observability momentum vs valuation (**this repo has never measured a valuation
factor**; PLAY23 has never produced a result — D15) · **C6** the un-narrated branch (⚠ **D52 asks to
retire `capex cut` as the probe term** — it returned ~0 for a 4th time while `AI spending` ran d1=259;
**that is a definition change to a carried contradiction and is flagged for a human, not made here**) ·
**C7** Health Care belief-vs-money (resolving observable: **one 🟢 from outside the top-6 by cap** —
zero of 26 today; horizon 08-06) · **C8** IT as one label over three legs (resolving observable: S13's
07-29 cross-condition).

**C2 is CLOSED and stays closed** (009150, KR-owned) — reopening it as a fresh idea is exactly what
§5's append-only design exists to prevent.

---

## 9 · Dig list carried into this run — the ones that bind US stages

**Tooling defects that will fire again this run if unhandled**: **D17/D64** `drift_watch` remote-unrunnable
(4 runs — DRIFT must state that a clean `fts` sweep means *"none of the known phrases fired"*, never
*"nothing happened"*) · **D18** single-name earnings missing from `CATALYST_WATCH` (5+ runs) · **D51**
a flow reading that post-dates an 8-K by 0–2 sessions is the event counted twice · **D52** the FINRA z
needs its baseline reported · **D54** `module_business_us` returns an **empty Item 1A** instead of raising
(measured on VLO, MA, V) · **D55/D63** `theme_age` n-floor and poisoned tokens (`rail` ≈40% "payment
rails"; `exchanges` 4.57× on 9,809 hits) · **D56** `margin_history.py VLO` broken **and** annual gross
margin is structurally the wrong instrument for a refiner · **D57** yfinance duplicated futures volume
across 07-22/07-23 — **the exact column that distinguishes a settled bar from an unfinished one** ·
**D61** the cycle-GAP threshold needs re-specifying (|margin| < 0.5pp ⇒ UNRESOLVED) · **D62** `RISK_UNITS.json`
and `cycle_exposure` disagree about whether TSM is in the book — **unsettled, so the 12.01% epicenter
figure is not to be trusted until it is**.

**Analytical digs owed**: **D1** (do LTA price floors actually hold margin — the C1 opener) ·
**D3** (hyperscaler capex → memory revenue lead-lag, tested the way **W2** demands) ·
**D57-old/D22** (build the Japan lead/lag table **or retire P7** — flat for three runs) ·
**D59** (confirm the India diesel/jet export-tax headline — it cuts directly against **M93**, and was
used as a lead, never as evidence).

---

## ✅ EXIT CHECK

- [x] `STANDING_VIEW.md`, `SCENARIOS.md`, `RESEARCH.md` all read in full; `module_report_tags show`
      cross-queried and reconciled in §7 (both directions, plus the unindexable correction).
- [x] **Retracted ledger read BEFORE today's view formed** (§2) — 22 rows, with the 9 that bind
      downstream stages reproduced verbatim in-file.
- [x] **Every past-dated scenario settled or explicitly named** (§3a): S1/S6/S7/S10 already scored;
      **S12 is the only pending row, named as a 5th-carry process failure with a frozen 07-28 deadline
      and no proxy substitution.** Zero silent skips.
- [x] **`reject_ledger.py due` run this HANDOVER** (§4) — 0 due, legacy 12, **trend 21→19→18→12
      reported**; `score` run alongside, cited as accumulation not as a gate.
- [x] Stale rows flagged with `asof` (§5); **K8 — the one suspension that clears today — converted
      into an explicit dig instruction for DEEP RE.**
- [x] `[measured]` / `[inferred]` tags preserved; the two `[inferred]` carries named and barred from
      use as evidence (§6).
- [x] **RESEARCH triggers loaded as binding constraints, grouped C/S/D/W + L**, with the stage each
      group binds stated (§6).
- [x] `HANDOVER.md` written. `handoff/*.md` to be updated at run end (append-only for retractions).
- [x] **No position sizing, no buy/sell language anywhere** (P4).
- [x] **English-pure** except where a KR proper noun is the ledger's own primary key.

---

> ⚠ **The single instruction this stage hands downstream**: *there is no new US price data this run.*
> Any stage that reports a flow "change", a "new" 🟢, or a moved RS number is reporting an artifact.
> The honest surface area is **news since 07-25, the three FRED series that advanced, and the
> pre-event audit of the 07-28→07-31 cluster.**
