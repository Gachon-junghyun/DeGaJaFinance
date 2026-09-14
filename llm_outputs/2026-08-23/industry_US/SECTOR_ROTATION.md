# SECTOR_ROTATION — industry_US · 2026-08-23 (Sun) · Stage 6 / L1·ROTATION

> Delta-only. MACRO §E owns the 11-sector verdict and `SECTOR_FLOW_US.json` owns the flow numbers;
> both are on disk. **This file writes what changes and why.**
> **Axis count this run: `n_axes` = 3 (`nonews`), `vel_axis` false, `vel_coverage` 0.0, `scored` 299.**
> ⇒ 🚫 **No delta below may cite theme freshness or news velocity**, and Δ vs the prior snapshot is
> read only against a snapshot of the same axis count (08-22 was also `nonews`/3).

## §0 · 🚨 The precondition that governs this entire stage

**`n_new_sessions_since_prior_run = 0`.** Today's sweep is **byte-identical** to the 08-22 file:
**0 of 299 `flow_score`s moved · 0 of 299 tags moved · 0 of 11 sector `wflow`s moved.** Terminal bar
**2026-08-21** on both runs.

⇒ **A verdict delta today would have to be produced by a number that did not change.** That is not a
delta; it is a re-reading, and the protocol calls a re-reading justified by argument rather than by a
flow number a **macro re-argument, declined**. **This stage therefore expects zero deltas and its job
is to show the attempts, not to manufacture a difference.**

## §1 · Inherited — one line, verbatim from MACRO §E

**MACRO holds: HLTH OW · ENRG OW · MATR OW− · DISC N+ · STPL N *(verdict blocked)* · FIN N ·
COMM N− · IT UW− · RE UW · INDU UW · UTIL UW.**

## §2 · Deltas — **ZERO**, from **eight attempts declined with numbers**

| # | Attempted move | Flow evidence for | Flow evidence against | Verdict |
|---|---|---|---|---|
| 1 | **ENRG OW → lower** | `delta` **−0.093**, second-most-negative of 11; **shortlist returns 0 names** | `eqflow` **+0.102 rank 2 of 11** · `exc5` **+4.162 rank 2** · `exc60` +9.635. **SWEEP §3 diagnosed the shortlist zero as a FILTER ARTIFACT**: `PSX` surge 1.11 / `MPC` 1.06 / `COP` 1.05 all fail 🟢 on the volume axis alone while OBV-accumulating with rs20 +13.8 / +13.0 / +8.5 | **DECLINED.** The absence is not evidence — SWEEP said so with numbers before this stage read it |
| 2 | **MATR OW− → N** | `Copper` COT **100th %ile** (max crowded long) · `NEM` fired `S89`-B on **exhaustion geometry** (`M779`: 246.4% of rs60 in the last 20 sessions) | `eqflow` **+0.046** positive · **breadth +0.080 = rank 1 of 11** · `exc5` +3.271 rank 3 | **DECLINED.** COT is Tuesday-close positioning with a 3–4 day lag ⇒ **context, not a trigger** (`D6`). No admissible flow number moved |
| 3 | **DISC N+ → N** | `exc60` **−4.938 = rank 10 of 11** · **breadth 0.000** of 28 names · 🟢0 : 🔴5 | `eqflow` **+0.103 = rank 2 of 11** · `exc20` **+4.244 = rank 1 of 11** | **DECLINED — two admissible axes contradict (`C5`).** ⇒ **This is exactly why DISC takes a DEEP slot (§3)**: the contradiction is the mandate |
| 4 | **IT UW− → UW** | EVENT_ALPHA Cards 1 & 3: the epicenter is repricing >15% on **cost**, and `AVGO` (held) lost Alphabet custom-silicon share to `MRVL` on 08-19 — rs60 spread **32.0pp** | **Every IT flow number is unchanged from 08-22.** `eqflow` −0.102, `exc5` −2.158, breadth +0.040, 🟢2:🔴15 — identical | **DECLINED as a macro/story re-argument.** A named news event is not a flow number. ⇒ **Routed to PREMORTEM as a 5th-slot candidate**, the 08-21 `INDU` precedent |
| 5 | **IT UW− → N− (contrarian)** | `Nasdaq-100` COT **4th %ile crowded-short**, wk Δ **+30,838** (covering) | Positioning, **5 days stale** (Tuesday 08-18 close), and `D6` bars a trigger read | **DECLINED** |
| 6 | **FIN N → lower** | `eqflow` **−0.034** (negative) · 🟢1 : **🔴9 of 47** · five of nine reds are insurers (`M805`) | `eqflow` ranks **6th of 11, not bottom** · `exc60` **+9.752 = rank 2 of 11** · the six large banks share one shape with **no exception** (`M805`) — a uniform sector is not a deteriorating one | **DECLINED** |
| 7 | **UTIL UW → lower** | `eqflow` **−0.621** worst of 11 · `exc20` **−11.230**, last by **5.7pp** · 🔴 **13 of 15** | — | **DECLINED: no notch below UW exists.** ⇒ **Routed to a DEEP slot instead** (§3) |
| 8 | **STPL → any direction** | `TGT` +0.950 🟢 vs `WMT` −0.333 🔴 = **17.1pp** intra-sector (`W5`); `WMT` FINRA 5v5 **+12.1▲**, the largest short-pressure build on the carried set | 🚫 **Blocked by rule** | **DECLINED BY RULE.** **This sector's sign is `WMT` at 28.9%** (`wflow` −0.013 → `wflow_ex_top1` **+0.116**). `R82` also stands |

### §2-a · The flip list, reproduced in full even though it changes nothing — **1 of 11**

| Sector | `top1` | `top1_w` | `wflow` | `wflow_ex_top1` | flips? |
|---|---|---:|---:|---:|---|
| **Consumer Staples** | **`WMT`** | **28.9%** | **−0.013** | **+0.116** | 🚨 **YES** |
| Health Care · Consumer Discretionary · Communication Services · Energy · Materials · Financials · Information Technology · Industrials · Real Estate · Utilities | LLY 19.4% · AMZN 40.2% · GOOGL 38.3% · XOM 30.5% · LIN 24.7% · BRK-B 13.9% · NVDA 19.4% · CAT 8.7% · WELL 16.9% · NEE 17.7% | — | — | — | **no ×10** |

Unchanged from 08-22 (`WMT` was the flipper then too). **A silent flipper is how one company becomes a
sector call, so the list is printed even at zero change.**

🚨 **`D297` reproduces unfixed for a fourth run.** `GOOG` is a **second 38.3% row** in Communication
Services, so the Alphabet complex is **76.6%** of the sector while `top1_w` reports 38.3%. **The
flipper guard is structurally blind in exactly one bucket**, and it cost nothing today only because
COMM did not move.

### §2-b · Standing replications — and one of them is **not** an independent observation today

- **`M144`/`D270`, "13th replication" — stated with its caveat.** 94 names pass `OBV 매집 ∧ rs20 > 0
  vs SPY`; **6 are 🟢; 88 are blocked and 100% of them on `vol_surge` alone.** 22 names clear
  `vol_surge ≥ 1.2` and **16 of those are 🟡/🔴**. Universe median `vol_surge` **0.82**.
  ⚠⚠ **These are the same 94/6/88 the 08-22 run measured, because it is the same frame.** ⇒ **This is
  a re-print, not a thirteenth independent replication**, and calling it the latter would inflate the
  evidence count by one. **The series stands at twelve independent observations.**
  ★ And the standing cross-reference holds: the axis doing 100% of the blocking is `vol_surge`, which
  the desk's `ic_ledger` measures at **t(NW) −3.86 (h=1, `n_eff` 34.0)** and **−3.38 (h=5)**, both past
  Bonferroni — **in a `market=kr` ledger**, so **`W1` bars this desk from acting on it** (`D310`, open).
- **`R81`/`D290` had nothing to replicate, for a second consecutive run.** All 299 velocities are
  `null` ⇒ **0 of 6 greens are velocity-derived**, admissible green count **6 = printed green count 6**,
  and all 6 `US_LIVE_SHORTLIST` rows are admissible. **The rule is not retired** — it re-binds on the
  next partial-coverage run, and `R96` (filed today) makes it stricter: partial coverage biases the tag
  layer **outward in both directions**, so the repair is to re-derive breadth from the score column
  rather than to discount greens.
- **New-🟢 ignitions: 2 — `MSI` and `ECL`.** ⚠ Both are day-over-day flags on an **unchanged frame**,
  i.e. they are the *same* two ignitions the 08-22 run saw. **No sector is promoted on them** (`MSI`
  in IT, `ECL` in Materials — neither moves a verdict).
- ⚠ **Two of the six greens are one factor**: `COIN` (Financials) and `MSTR` (Information Technology)
  are both bitcoin beta. **A third of the entire green set is one risk unit wearing two GICS labels** —
  the same shape the 08-21 run flagged, and **neither sector is promoted on it.**

## §3 · DEEP picks and DEEP_LOG — **N = 4** (protocol budget: 2 continuous + 2 rotating)

### Continuous ⌈N/2⌉ = 2 — **ENRG and HLTH KEEP their slots**
Both are today's top-2 OW in MACRO §E and both held a continuous slot in the previous run ⇒ the
anti-thrash continuity rule applies and is stated rather than assumed.
- **HLTH** — rank 1 on **both** axes (`exc5` +5.700, `eqflow` +0.229) and rank 1 at 60 days (+15.327).
  ⚠ **18 names blocked by `vol_surge` alone — the largest blocked set of any sector** (SWEEP §2).
  **Mandate: is the sector's leadership broad, or is it 18 names the gate cannot see plus `LLY`?**
- **ENRG** — `eqflow` +0.102 rank 2, `exc5` +4.162 rank 2, **and `delta` −0.093, second-worst of 11**.
  **Mandate, and it is the one carried unopened for four runs: the refiner CONTRACT question.**
  `module_disclosure_us MPC` → 10-Q MD&A + Item 1A. `P70` MISSED on its control leg (`BZ=F` 5-session
  **+6.631%** against a ≤+2.0% bar), which makes margin-sustainability the binding gap rather than a
  note. ★ **A closed market is the right session for a filings read** — nothing competes for attention
  and filings do not move on weekends.

### Rotating ⌊N/2⌋ = 2 — **DECLARED recency-starved deviation, 10th consecutive run**
MACRO's OW set is **{HLTH, ENRG, MATR−}**. HLTH and ENRG took the continuous slots; **MATR was covered
2026-08-21, i.e. 2 runs ago, inside the ~3-run recency bar.** ⇒ **No eligible OW remains.** Per the
rule, R1/R2 are filled from non-OW **by evidence density with recency as the tiebreak**, and the
deviation is declared rather than hidden.

- **R1 = Consumer Discretionary (N+)** — **last covered 2026-08-15 = ~8 runs, the worst recency on the
  board**, and it carries the run's largest *un-tested* contradiction: **`exc20` +4.244 (rank 1 of 11)
  against `exc60` −4.938 (rank 10)**, with **breadth 0.000 across 28 names** and 🟢0 : 🔴5.
  ⚠ **And it has no live bracket** — `S91` was VOIDed on 08-22, so the row that was testing this
  sector is gone. **Mandate: a 20-day leader with zero breadth and a 60-day deficit — is this a
  reversal with a base, or five names?** (§2 attempt 3 was declined into this slot.)
- **R2 = Utilities (UW)** — last covered 2026-08-20 = 3 runs, and the evidence density is the highest
  of any uncovered sector because a **quantified** demand number arrived this week against the board's
  worst tape: **Morgan Stanley's named 38-gigawatt AI data-centre power gap** (`yahoo_finance` + `fool`,
  08-20) versus `eqflow` **−0.621**, `exc20` **−11.230** (last by 5.7pp), **🔴 13 of 15**.
  ★ **And `M802` is unresolved for a second run**: `NVDA` is guaranteeing up to **$105bn** of OpenAI's
  Ohio leases while **five of eight measurable power names print 🔴분산** (`TT` −0.812 · `GEV` −0.741 ·
  `VST` −0.689 · `CEG` −0.625 · `NEE` −0.600 — each also `flow_score` ≤ −0.600 **and** rs20 ≤ −4.2, so
  the verdict does not rest on OBV, `RULE D6`).
  **Mandate: is there any equity transmission from AI power capex at all, or is the desk carrying a
  capex story with no listed expression?** (§2 attempt 7 was declined into this slot.)

### Routed to PREMORTEM rather than to a slot
🚨 **Information Technology.** It has the highest evidence density on the board — the 08-26 `NVDA`
print at **D-3**, the >15% memory-cost pass-through (`P90`), the `AVGO`/`MRVL`/Alphabet event on a
**held** name with a **32.0pp** rs60 spread, `SECTOR_DEEP_SEMI.md` at **39 days**, and 4 of 11 book
names inside it. **But it was covered yesterday (2026-08-22, PREMORTEM-promoted 5th slot), and taking
a rotating slot one day later is intra-run thrash.** ⇒ **Handed to PREMORTEM as a 5th-slot candidate**,
exactly as `INDU` was on 08-21. **Not dropped, and the routing is the record.**

### Un-covered OW and near-OW sectors, named with last-covered date and mandate
- **MATR (OW−, 08-21, 2 runs)** — recency-blocked from a rotating slot. Copper COT **100th %ile**;
  `NEM` fired `S89`-B on exhaustion geometry (`M779` 246.4%); breadth **+0.080 = rank 1 of 11**.
- **IT (UW−, 08-22, 1 run)** — routed to PREMORTEM above.
- **FIN (N, 08-22, 1 run)** — `M805`'s three-businesses split measured; 🔴9 of 47, five insurers.
- **INDU (UW, 08-22, 1 run)** — `M803` discharged (`M704` ex-`LHX` −4.162 vs −4.775 ⇒ 13% / 87%).
  ⚠ New this run: the **50% US–Canada tariff took effect 08-22**, *after* the flow frame, and the four
  most-exposed names (`X`, `WY`, `CNI`, `CP`) are **outside the universe**.
- **STPL (N, 08-17, ~6 runs)** — **flipper-blocked**; `WMT` 28.9% owns the sign; `WMT`'s weakness has a
  named dated cause (*"Walmart shares tumble as sales growth slows"*, peak **19 outlets** 08-19→08-22).
- **COMM (N−, 08-19, ~4 runs)** — `T` orphan at **9.74%** of the real book's invested for a **6th** run;
  `D297` unfixed so the flipper guard cannot see the 76.6% Alphabet complex.
- **RE (UW, 08-21, 2 runs)** — `S90` FIRED-A against this desk's own prior promotion; the sub-node split
  (`DLR`/`EQIX`/`IRM` vs `AMT`/`PLD`/`WELL`) is measured but not deep-dived. `DLR` carries the board's
  **most negative one-session delta, −1.083**.

## DEEP_LOG 2026-08-23: continuous=[ENRG, HLTH] rotating=[DISC, UTIL] · N=4/4 · **ZERO verdict deltas — and today the zero is STRUCTURAL, not a judgement: `n_new_sessions_since_prior_run = 0` and the sweep is byte-identical to 08-22 (0/299 scores, 0/299 tags, 0/11 sector `wflow`s moved), so any delta would have had to come from a number that did not change. EIGHT attempts declined with numbers (ENRG→lower declined because SWEEP diagnosed the shortlist-zero as a `vol_surge` FILTER ARTIFACT — `PSX` 1.11 / `MPC` 1.06 / `COP` 1.05 all OBV-accumulating with rs20 +13.8/+13.0/+8.5 · MATR→N declined: Copper COT 100th %ile is 5-day-stale positioning, `D6` context-not-trigger, while breadth +0.080 is rank 1 · DISC→N declined: `eqflow` +0.103 rank 2 and `exc20` +4.244 rank 1 contradict `exc60` −4.938 rank 10 and breadth 0.000, `C5` — routed to a DEEP slot · IT→UW declined as a macro/story re-argument: every IT flow number is unchanged and a named news event is not a flow number — routed to PREMORTEM · IT→N− contrarian declined: `Nasdaq-100` 4th-%ile short is 5-day-stale positioning · FIN→lower declined: `eqflow` −0.034 ranks 6th of 11 not bottom and `exc60` +9.752 is rank 2 · UTIL→lower declined: no notch below UW — routed to a DEEP slot · STPL→any declined BY RULE: the sector's sign is `WMT` at 28.9%, `wflow` −0.013 → `ex_top1` +0.116)** · **flip list 1 of 11 — Consumer Staples/`WMT`/28.9%, unchanged from 08-22; the other TEN print `top1_flips_sign = false`** · 🚨 **`D297` reproduces unfixed for a 4th run (`GOOG` a second 38.3% row ⇒ Alphabet complex 76.6% of COMM while `top1_w` reports 38.3%)** · **★ `M144`/`D270` is a RE-PRINT, not a 13th independent replication — 94 pass `OBV 매집 ∧ rs20>0`, 6 are 🟢, 88 blocked, 100% on `vol_surge` alone, 22 clear surge≥1.2 of which 16 are 🟡/🔴, median surge 0.82 — all identical to 08-22 because the frame is identical; the independent-observation count stays at TWELVE and inflating it would have been the cheapest available error today** · **`R81`/`D290` had nothing to replicate for a 2nd run (299/299 velocities null ⇒ admissible green count 6 = printed 6, all 6 shortlist rows admissible); `R96` filed today makes the rule stricter — partial coverage biases the tag layer OUTWARD in both directions (`MRVL`/`MA`/`CVX` 🟢→🟡, `MS`/`JPM` 🔴→🟡, `WMT` 🟡→🔴 across two persisted runs of one frame), so the repair is to re-derive breadth from the score column, NOT to discount greens** · **★★ the run's structural headline is a NEWS fact on a day with no tape: `NVDA` notified customers of >15% server price increases and the reporting names MEMORY COSTS as the cause (`yahoo_finance` 08-22, 8 outlets, latest 08-23), three days before the 08-26 print, alongside Samsung's up-to-15% foundry increase (08-19) — two ~15% increases at two chain layers in four days, registered both ways as `P90`** · **★★ and the second is a HELD-NAME event the desk had no thesis line for: Alphabet dual-sourced custom silicon to `MRVL` on 08-19 and is taking `MRVL` warrants, with `AVGO` (held) at rs60 −14.7 vs `MRVL` +17.3 = a 32.0pp spread already realised, `AVGO` FINRA z −2.53 covering INTO the decline (the `M804` shape, 3rd instance this run after `RTX` z −2.15 into delta −0.304) — and `MRVL` is simultaneously one of the six `R96` tag-contaminated names, its 🟢 in the partial-coverage run coming from THIS story's velocity while its score column says the same thing cleanly** · 🚨 **a TOOL DEFECT found inside EVENT_ALPHA that manufactures zeros: `module_news_data fts search` wraps the whole user string in quotes, so a bare boolean (`Micron AND CXMT`) becomes a phrase search and returns 0 while `"Micron" AND "CXMT"` returns 27 and `Micron` alone returns 562 — it fired FOUR times in one stage and would have produced four fabricated silences, one on a held name** · **rotating slots are a DECLARED recency-starved deviation for a 10th run: MACRO's only third OW (MATR) was covered 08-21, inside the ~3-run bar, so R1/R2 were filled from non-OW by evidence density with recency as tiebreak — DISC on the board's worst recency (~8 runs) plus an untested `exc20` rank-1 vs `exc60` rank-10 contradiction with breadth 0.000 and no live bracket since `S91` VOIDed, UTIL on the highest evidence density (Morgan Stanley's named 38-GW gap, 08-20, against `eqflow` −0.621 / 🔴13 of 15 / `M802`'s $105bn guarantee unresolved for a 2nd run)** · **uncovered=[MATR(OW−, 08-21, recency-blocked, Copper 100th %ile + `NEM` exhaustion geometry `M779` 246.4% + breadth rank 1), IT(UW−, 08-22, ROUTED TO PREMORTEM as 5th-slot candidate — `NVDA` D-3, `P90`, the `AVGO`/`MRVL` held-name event, `SECTOR_DEEP_SEMI` at 39 days, 4 of 11 book names), FIN(N, 08-22, `M805` three-businesses split, 🔴9 of 47 with 5 insurers), INDU(UW, 08-22, `M803` discharged 13%/87%; NEW: the 50% US–Canada tariff took effect 08-22 AFTER the flow frame and `X`/`WY`/`CNI`/`CP` are outside the universe), STPL(N, 08-17 = ~6 runs, flipper-blocked, `WMT` weakness has a named cause at peak 19 outlets), COMM(N−, 08-19 = ~4 runs, `T` orphan 9.74% of real invested for a 6th run, `D297` unfixed), RE(UW, 08-21, `S90` FIRED-A against the desk's own promotion, sub-node split measured not deep-dived, `DLR` carries the board's most negative delta −1.083)]**

## ✅ EXIT CHECK

- [x] **§1 is ONE line**, inheriting MACRO §E verbatim. No unchanged sector gets a row or a paragraph.
- [x] **Every §2 attempt cites a flow number**, and the two justified only by argument (IT→UW on a news
      event; MATR→N on stale positioning) are **declined and logged as such**, not enacted.
- [x] 🚨 **No promotion or demotion rests on a `top1_flips_sign` bucket.** Consumer Staples is declined
      **by rule** with *"this sector's sign is `WMT` at 28.9%"* written out. **The full flip list is
      reproduced (§2-a) even though it changes nothing.**
- [x] **Axis count stated** — `n_axes` 3 (`nonews`), `vel_coverage` 0.0. **No delta cites theme
      freshness or news velocity**, and the Δ-vs-prior comparison is against a same-axis-count snapshot.
- [x] **Every matrix×flow divergence has a named resolution owner** — DISC → DEEP R1, UTIL → DEEP R2,
      IT → PREMORTEM, ENRG's shortlist-zero → resolved in SWEEP before this stage.
- [x] **N=4 picked by the rule**, continuity stated for ENRG/HLTH and the **recency-starved deviation
      declared** for the rotating pair. **No padding.** All un-covered sectors named with last-covered
      date and mandate.
- [x] **The zero-delta output is the correct output** and is labelled **structural** — with the reason
      (`n_new_sessions = 0`) rather than presented as a judgement.
- [x] **Linter run on this stage's own output** — `report_lint.py SECTOR_ROTATION.md` → **0 findings** (C1, C2, S6, D6). ⚠ Form only; a clean lint does not check that the eight declines were the right eight.
