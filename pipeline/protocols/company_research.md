# PROTOCOL — company_research (컴패니 리서치 · 단일 종목 "이걸 베팅할까")

> A protocol = an ordered composition of L1 blocks. **Order is owned by this file.** L1s are referenced only.
> Purpose: dissect **ONE name** — what it sells, what actually moves those earnings, what frame the tape
> is using, what is already priced — and end in a **single trading verdict** written into a scored ledger.
> Market-parameterized (`--market us|kr`, KR 6-digit auto-detect); no mirrored per-market file (P3).
> Output root `llm_outputs/{YYYY-MM-DD}/company_{ticker}/`.

## What this desk is (and is NOT)
- **IS**: the "do we bet" axis — one name, trader's lens, ending in `ENTER·ADD·HOLD·TRIM·EXIT·PASS`
  with a written stop, a dated catalyst, and one ledger row that a later run grades.
- **IS NOT**: the forensic "is it REAL?" desk — that is [`real_alpha_kr`](real_alpha_kr.md), a different
  axis (4-tier, 참고-only, binding:false). The two may disagree; both are kept.
- **IS NOT**: an order path. It hands a size request to SIZE and stops. Staging intent cards onto the KIS
  stack belongs to [`미러링`](미러링.md); running a book belongs to [`paper_desk`](paper_desk.md).
- **Prerequisite**: [`preflight`](preflight.md) is stage −1 for every desk. A failed gate removes a
  citation right for this run — a dead news axis means no theme-freshness claim here either.

## Composition (L1 order)

| # | L1 block | Output |
|---|---|---|
| 0 | [PULSE](../L1_stages/pulse.md) ☆optional-lead | same-day tape sanity if the name is moving hard today |
| 1 | [HANDOVER](../L1_stages/handover.md) | carry + **both ledgers** + book position — the inputs G8 needs |
| 2 | [FORENSIC_PACK](../L1_stages/forensic_pack.md) | `DATAPACK.md` — every number frozen before reasoning |
| 3 | [SELF_SCORE](../L1_stages/self_score.md) | prior observation points graded 적중/기각/미도래 (skip if first research) |
| 4 | [DRIVER_TEST](../L1_stages/driver_test.md) ★new | `DRIVER_TEST.md` — segments → drivers (roll-guarded) → the frame the tape uses |
| 5 | [MONEY_FORENSIC](../L1_stages/money_forensic.md) | is the profit cash · insider/treasury · 말vs행동 괴리표 |
| 6 | [SET_DIFF](../L1_stages/set_diff.md) | ①already-priced vs ②measured → `alpha_delta` / `risk_unseen` |
| 7 | [FALSIFY](../L1_stages/falsify.md) | strongest bear case first → reject/uphold with A/B evidence |
| 8 | [BET_VERDICT](../L1_stages/bet_verdict.md) ★new | `COMPANY_VERDICT.md` + **exactly one** ledger row + observation points |
| 9 | [SIZE](../L1_stages/size.md) ☆optional | share count from the risk model — never a gut number |

## What is REUSED vs NEW vs REMOVED
> Prose names stages in plain text on purpose — **only the composition table's links set the run order.**

- **Reused as-is**: pulse · handover · forensic_pack · self_score · money_forensic · set_diff · falsify ·
  size (L1); carryover · deepdive · money_trail · news · indicators (L2); scenario_score · reject_ledger ·
  missed_ledger · exposure_state · accruals_check · set_difference · filing_diff · competitors (L3).
- **New (5)**: L1 **DRIVER_TEST** · L1 **BET_VERDICT** · L3 **segment_pnl** · L3 **driver_link** ·
  L3 **peer_pricing**. All five come from one measured run (2026-08-21, PSX); each closes a mechanical
  error that run made.
- **Removed on purpose (3)** — see Removals below.

## ★ Why the new stage sits at position 4 (measured 2026-08-21, PSX)
A full pass over this desk's modules was run on Phillips 66 before this protocol existed. Four errors
appeared, none of them from missing data — all four from **starting at the label**:

| # | Error | Caught by |
|---|---|---|
| 1 | Modeled a **5-segment** company off one spread. Refining is **61.6%** of pre-tax income; the other ~38% is driven by **regulatory credits**, **mark-to-market** and **NGL volumes** — none of which move with a crack | L3 segment_pnl |
| 2 | Read a **−$9.48/bbl one-day (4.6σ)** driver move as a margin collapse. Leg decomposition `CL +0.94% · HO −2.32% · RB −7.93%` = a **RBOB Sep→Oct summer/winter spec roll**. Roll-adjusted, the same window is **−1.0% at the 92.8th percentile**, not −12.5% | L3 driver_link |
| 3 | Wrote a **+18.8%/20d** move as a name-specific re-rating. VLO/MPC/DINO did the same in the same window (corr **+0.90/+0.87/+0.77**) — it was **sector beta** | L3 peer_pricing |
| 4 | Quoted revenue **+53% YoY** as growth. The release's Basis of Presentation: WRB (Borger·Wood River) went **50% equity-method → 100% consolidated on 2025-10-01** | L3 segment_pnl scope line |

⇒ The stage sits **before** money/valuation/falsify because each of those inherits the denominator it
produces. Run it after the pack and before anything reasons.

## Removals (덜어냄 — and why)
1. **The 11-branch chart matrix + M1–M4 conflict rules** (`PROMPT_MAP §5`, legacy company Phase 4).
   Replaced by `module_chart --read` + L2 indicators' **A/B/C/REJECTED grade table**, which does M1
   (weighting) and M3 (uncorrelated confluence) *with measurements* and grades OBV — a whole branch of the
   old matrix — as corroborant-only with **no leading power** once real flow is known. Eleven branches
   printed at equal visual weight is the failure that grade table exists to prevent.
2. **The order/execution tail** (`trading_engine`·`alert_bot`, legacy strategy Phase 3). Neither is in this
   repo, and the intent-card path already has an owner (`미러링`). A protocol naming a module this repo does
   not have does not fail loudly — it just stops happening (PROMPT_MAP §7).
3. **The separate "Phase 3 valuation/catalyst" phase.** Valuation lives in the pack (deepdive) and its
   *direction* in L2 indicators §2 (estimate momentum); the catalyst calendar is already a pack axis.
   Kept as its own phase it re-printed upstream tables — the P1 duplication README §Core properties forbids.

## Fixes this protocol required (applied, not deferred)
- **`build_protocol.py` collected L3s from L2 text only**, so every L3 an L1 calls **directly** was dropped
  from the compiled executable. Measured: `real_alpha_kr` named `filing_diff · contract_alpha ·
  set_difference` in its stages and shipped a compiled file containing **none** of the three (L3 8 → 11
  after the fix). This protocol leans on L1→L3 calls, so the compiler was fixed first.
- **KR business-report path** — `module_business --include-dart` reaches the pre-fix
  `module_business/_dart_fetch.py`, which scrapes `dsaf001/main.do` (the DART **frameset shell**) and can
  return navigation text as 본문. The single source is `module_disclosure --business-report`
  (viewer.do coordinate parsing, fixed 2026-07-20). L2 deepdive now says so.

## Runtime deltas (`--market us|kr`)
| axis | US | KR |
|---|---|---|
| segment P&L | earnings **8-K exhibit 99.1** (the 10-K is annual + qualitative) | DART 사업보고서 부문별 정보 |
| business text | `module_business_us --full --json` | `module_disclosure --business-report` ⚠ **not** `module_business --include-dart` |
| investor flow | ❌ none — FINRA short-vol z + options are the substitutes | ✅ **KIS per-investor daily actuals** (B-grade, overrides OBV) |
| implied move | ✅ `module_flow --positioning` (ATM straddle) | ❌ no equivalent — thresholds stay hand-set, and the file says so |
| insider | Form 4 (**with price**) + Form 144 | DART equity/treasury (**direction+qty only, price 미확보**) |
| ledger scoring | 🚨 **US rows score as 채점불가** — see BET_VERDICT's defect note | ✅ scored |
| ticker format | plain (`PSX`) | 6-digit KIS/DART · `.KS/.KQ` chart/flow · 한글명 news |

**Start → read PULSE if the tape is moving, else HANDOVER, and execute.** Advance only after each EXIT
CHECK passes. Finish at BET_VERDICT with one ledger row written; SIZE only if the verdict was ENTER/ADD.
Run stage-by-stage with `run_protocol.py company_research` (context-loss guard).
