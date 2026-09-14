# SECTOR_ROTATION — industry_US · 2026-08-31 (Mon) · Stage 6 / L1·ROTATION

> **Delta-only.** MACRO §D owns the 11-sector verdict; `SECTOR_FLOW_US_REPAIRED.json` owns the flow
> numbers. Both are on disk. This file writes **only what changes and why**.

## 🚨 Instrument state governing every line below

**The native sweep scored 0 of 299** — all 301 cached tickers carry a `2026-08-28 Close = NaN`
(bench `SPY` included), **third calendar day, unhealed**. `SECTOR_FLOW_US.json` is left **empty** as
the honest record. **Every number here comes from `SECTOR_FLOW_US_REPAIRED.json`** — a labelled
reconstruction that patches only the 08-28 Close with a 5m-proxy value validated at **0.0181% mean /
0.0448% max** error (n=24, 0 above 0.05%), runs the **unmodified** engine, and scores **299/299**.
The reconstruction was rebuilt independently today and agrees with the 08-30 run's separate
reconstruction to **≤0.002 on 11 of 11 sectors**.

- **`n_axes` = 3** (`vel_coverage` **15.72%** ⇒ news axis dropped, `nonews` mode). ⇒ 🚫 **no delta
  below cites theme freshness or news velocity.**
- **Δ is legal this run**: the prior same-mode snapshot is **08-27 `nonews`, n=299**, and **299/299
  names are common** ⇒ one calendar step, same scale. Every Δ is labelled
  **`repaired sweep, 08-27 → 08-28`**.
- ★ **`asof` is 2026-08-28 and the run's largest macro event happened 08-30/31.** **The money has not
  voted on the Iran escalation.** This single fact decides §2's Energy row.

## §1 · Inherited — one line, verbatim from MACRO §D

`MACRO holds: ENRG OW(↑ from N) · HLTH OW · MATR OW · FIN OW− · COMM OW−(↓ from OW) · IT N · STPL N ·
DISC UW · INDU UW · RE UW · UTIL UW.`

## §2 · Deltas — one change, and every attempt logged with its numbers

**Flip list, reproduced in full even though it changes nothing** (a silent flipper is how one company
becomes a sector call): **3 of 11** — **IT / `NVDA` 19.4%** (+0.033 → **−0.016**) · **Energy / `XOM`
30.5%** (−0.097 → **+0.074**) · **Consumer Discretionary / `AMZN` 40.2%** (−0.262 → **+0.056**).
🚫 **None of the three may carry a promotion or a demotion this run.**

★ **And one bucket the flip guard does NOT catch** (`D424`, registered by the KR desk today):
**Health Care** has `top1_flips_sign = False` yet `wflow` **+0.021** against `wflow_ex_top1`
**+0.095** — **`LLY` is a drag on a sector that is materially stronger underneath it.** The guard is
silent because the sign never changed. Carried into §3 as HLTH's DEEP mandate.

### The one change

| sector | matrix said | flow evidence | new verdict | who resolves |
|---|---|---|---|---|
| **Industrials** | **UW** | **Δ −0.129 = 2nd-worst on the board** (`repaired sweep, 08-27 → 08-28`) · `eqflow` **−0.291 rank 9/11** · **17 reds of 50 — the most in absolute terms on the board** · `top1_flips_sign` **False** with `CAT` only **8.7%** and `wflow_ex_top1` **−0.291** ⇒ the weakness is **broad, not one name** | **UW−** | Not slotted — logged in DEEP_LOG. `S126` (`XLI` exc5 vs `SPY` **into** NFP) and `P114` (**out of** NFP) already bracket 09-04 |

**Why this one qualifies and the others do not**: it is carried by **three** non-cap-weighted numbers
(Δ, `eqflow` rank, absolute red count), it is **newly measurable** — this is the **first run in which
a Δ exists for the 08-28 session** (the 08-30 run's repair produced no Δ column) — and the sector is
**not** a flipper, so the number is not one company.

### Attempts declined, with their numbers

| attempted | numbers | why declined |
|---|---|---|
| **Energy `OW → N`** (i.e. undo MACRO's promotion) | `wflow` **−0.097** · `eqflow` **+0.005 (rank 4/11, flat)** · **0 greens of 16**, 3 reds · **`top1_flips_sign` TRUE, `XOM` 30.5%, ex-`XOM` +0.074** | 🚫 **Declined twice over.** (i) A 🚨1名 bucket may not carry a demotion — **Energy's entire negative sign is `XOM`**. (ii) The non-cap-weighted substitute `eqflow` is **+0.005**, i.e. flat, and flat cannot carry a demotion either. ★ (iii) **The decisive reason is the clock**: this flow is `asof 08-28`, **two days before the strikes**. Demoting on it would be scoring the escalation against a tape that predates it |
| **Financials `OW− → N`** | `eqflow` **−0.089 (rank 6/11)** · **0 greens of 47 — the largest bucket on the board with no green** · but **Δ +0.073 = 3rd-best on the board** | 🚫 **Declined: the two non-cap-weighted signals disagree.** Level says demote, Δ says the opposite, and the desk's rule is to state the disagreement rather than pick a side (`C5`). ⚠ **0 greens in 47 is carried forward as FIN's standing question**, not as a verdict |
| **Utilities `UW → UW−`** | `eqflow` **−0.524 = rank 11/11** · **red-rate 66.7% = worst on the board** · not a flipper (`NEE` 17.7%, ex-top1 −0.525) | 🚫 **Declined on newness, not on quality.** Utilities was **already** the board's worst on both axes in the 08-30 run, and **Δ is −0.025 ≈ flat**. A verdict change needs a *change*; re-stating an unchanged extreme is restatement. ⚠ 08-30 declined this same move **on method** (macro re-argument); today it is declined **on the numbers**, which is a different and stronger reason — recorded so the two are not conflated |
| **IT `N → OW`** or **`N → UW`** | `wflow` **+0.033** but `eqflow` **−0.034** · **3 greens of 56 = breadth 0.05, the best on the board** against **13 reds** · **flipper, `NVDA` 19.4%, ex-`NVDA` −0.016** | 🚫 **Declined — 1名 bucket, and the two admissible numbers have opposite signs.** ⇒ **routed to PREMORTEM**, as on 08-30 |
| **Consumer Discretionary `UW → UW−`** | **red-rate 42.9% (12 of 28) = 2nd-worst** · `eqflow` −0.247 rank 8 · Δ −0.126 · **flipper, `AMZN` 40.2%, ex-`AMZN` +0.056** | 🚫 **Declined — 1名 bucket.** The red-rate would support it, but the desk's own 08-30 finding stands: **the two largest runners in the entire 299-name universe (`DASH` `rs60` +51.1, `ABNB` +39.8 vs `SPY`) sit inside this UW.** Deepening the label on a bucket whose sign is one company would be the exact `D9` failure |
| **Comm. Services further cut** | `eqflow` **+0.080 = rank 3/11, positive** · `wflow` −0.422 · Δ **−0.162 = worst on the board** | 🚫 **Declined — MACRO already made the one-notch cut TODAY on Δ**, and a second cut in the same run on the same number is double-counting. ⚠ `D297` still applies: `GOOGL`+`GOOG` are ~85% of a 12-name bucket with a **0.502** `wflow`/`eqflow` gap that `top1_flips_sign` does **not** catch |
| **Real Estate `UW → UW−`** | `eqflow` −0.333 rank 10 · **Δ +0.078 = 2nd-best on the board** · ex-top1 **−0.415** (the top-1 is holding it **up**) | 🚫 Declined — the Δ points the wrong way for a demotion |
| **Cons. Staples `N → UW`** | `eqflow` −0.187 **rank 7 = mid-table** · Δ +0.080 = 3rd-best · ex-`WMT` **−0.130** (better without the top-1) | 🚫 Declined — mid-table plus a positive Δ |
| **HLTH / MATR `OW → OW+`** | HLTH `eqflow` +0.135 rank 2, **2 reds of 32**; MATR `eqflow` +0.164 rank 1, **0 reds of 12**, Δ **+0.197 = best on the board** | 🚫 **No notch above OW exists in this desk's scale.** Recorded so the absence is not read as indifference |

**Delta count: 1 of 11 attempted moves taken.** Ten declined, each with the number that declined it.

### ★ The within-sector finding that is NOT a verdict change, and is the run's most useful flow read

Energy's sector number is uninformative for the reason above, **but the bucket splits cleanly by
position in the chain** (`repaired sweep, asof 08-28`):

- **accumulating** — `SLB` **+0.661** (OBV +0.318) · `MPC` **+0.650** (OBV +0.329) · `PSX` +0.388 ·
  `VLO` +0.349 (`rs60` **+32.7** vs `SPY`) · `COP` +0.324
- **distributing** — `XOM` **−0.486 🔴** (OBV −0.201) · `FANG` **−0.622 🔴** · `EOG` **−0.694 🔴**

⇒ **the money left E&P and sat in services/refining before the strikes.** This is a **DEEP mandate**,
not a sector verdict — it says *where inside Energy*, which is precisely what a sector label cannot.

## §3 · DEEP picks + DEEP_LOG

**DEEP budget: N = 4** (protocol line: 2 continuous + 2 rotating; unchanged 2026-07-31 when
`industry_kr` cut to N=2, because that cut was justified by KR-specific measurement and importing it
would be the `W1` violation this repo keeps logging).

**Recency read from DEEP FILES ON DISK**, not from `DEEP_LOG` lines (the 08-28 run logged 4 slots and
produced 0 files — the lines are not a reliable index):

| sector | last DEEP file | runs since |
|---|---|---:|
| HLTH · FIN · COMM · IT · MATR | 2026-08-30 | **0** |
| ENRG | 2026-08-29 | **1** |
| DISC · INDU · STPL | 2026-08-27 | **3** |
| RE | 2026-08-26 | **4** |
| **UTIL** | **2026-08-23** | **6 — the longest gap on the board** |

**Selection:**

- **Continuous (⌈4/2⌉ = 2) — `MATR`, `HLTH`.** Both were continuous last run and both are still OW
  today ⇒ **anti-thrash continuity applies and is stated.** They are also the board's `eqflow` rank 1
  and rank 2, so continuity and merit agree here rather than conflict.
- **Rotating slot R1 — `ENRG`.** It is the **only remaining OW sector**, and it is a **declared
  1-run recency violation** taken under the recency-starved fallback (every other OW is a continuous
  holder). Justified independently by: MACRO promoted it `N → OW` today; EVENT_ALPHA handed **three**
  candidates out of it (`SLB`, `COP`, `VLO`); and its sector number is unusable (§2) precisely because
  the answer is one level down the chain.
- **Rotating slot R2 — DELIBERATELY UNFILLED. N = 3/4.** The OW set has exactly three members and two
  are continuous holders. The two pads considered and **rejected**:
  - **`FIN`** (OW−) — covered **0 runs ago**, and §2 just declined its own delta because its two
    non-cap-weighted signals disagree. A DEEP would be re-opening yesterday's file to answer a
    question §2 says is unresolved, not unasked.
  - **`COMM`** (OW−) — covered **0 runs ago**, and `D297` says its bucket is un-measurable by rule
    (`GOOGL`+`GOOG` ≈85% of 12 names with a 0.502 `wflow`/`eqflow` gap the flip guard misses).
  **Padding with N/UW is forbidden by rule, and fewer is fine if stated. It is stated.**
  ⚠ The 4th slot remains available to **PREMORTEM** (Stage 7) as a promoted slot — that is PREMORTEM's
  call, not ROTATION's, and `IT` is routed there again (§2).

**Mandates handed to DEEP** (each is the question the sector's own numbers could not answer):

| slot | sector | mandate — one question |
|---|---|---|
| **C1** | **MATR** | ★ **`C24`, now reproduced twice**: the board's rank-1 `eqflow` (+0.164, **0 reds of 12**, Δ **+0.197**) against **copper speculative net at the 100th percentile of its year**. The DEEP resolved *what* the signal is on 08-30 (`FCX`+`NEM`, not Materials); it did **not** resolve **which instrument to believe**. ⚠ *"Steel Hits 2½-Month Highs"* [2 outlets] printed today and `NUE` (held) reads **−0.307 with `rs20` −5.6 vs `SPY`** — the held name is on the wrong side of the sector's own strength |
| **C2** | **HLTH** | ★ **The `D424` case (§2)**: `wflow` +0.021 vs **ex-`LLY` +0.095**. Is the sector's breadth (`eqflow` +0.135 rank 2, **only 2 reds of 32**) real, or is it an artifact of `LLY` being the sole large drag? ⚠ `LLY` announced the **Merida Biosciences acquisition (up to $2.875bn, 5 outlets)** today — the drag name is the one doing deals. `S133` (09-14) already asks whether the sector is its constituents or its ETF; **do not pre-commit its answer** |
| **R1** | **ENRG** | ★★ **Where inside the chain does the escalation land?** The sector number is unusable (1名 `XOM`) and `eqflow` is flat, but the bucket splits **services/refining accumulating vs E&P distributing** (§2). ⇒ (a) is the split a war-premium effect or a pre-existing structural one, given the tape **predates the strikes**? (b) `SLB` carries the board's **most extreme FINRA short-vol (`z +2.40`, 5v5 +9.0▲)** *and* OBV **+0.318 매집** *and* a **$3.4bn data-centre acquisition announced today** — resolve whether that is a squeeze setup or distribution under a headline. ⚠ **`R89` + `P83` bar any refining-margin-vs-barrel separation claim** — `P118` (registered today, `DCOILWTICO` spot, settles 09-11) is the row that measures it, and the DEEP **may not assert the separation** |
| R2 | — | **unfilled, by rule** |

## DEEP_LOG 2026-08-31: continuous=[MATR, HLTH] rotating=[ENRG] · N=3/4 filled, 4th slot deliberately unfilled (only 3 OW sectors exist and 2 are continuous holders; pads `FIN`/`COMM` both 0-run recency and both rejected with reasons; padding with N/UW forbidden) · **OW sectors WITHOUT a slot: none — all 3 OW sectors got one** · **verdict deltas 1 of 11 attempts: `INDU UW → UW−`, carried by three non-cap-weighted numbers (Δ −0.129 = 2nd-worst, `eqflow` −0.291 rank 9, 17 reds = most in absolute terms) on a NON-flipper bucket (`CAT` 8.7%, ex-top1 −0.291)** · **10 declines each with its number: `ENRG OW→N` (1名 `XOM` 30.5% ⇒ barred; `eqflow` +0.005 flat ⇒ cannot demote; ★ and the decisive reason is the CLOCK — the flow is `asof 08-28`, two days BEFORE the strikes, so demoting on it would score an event against a tape that predates it), `FIN OW−→N` (level −0.089 rank 6 and 0 greens of 47 say demote, Δ +0.073 = 3rd-best says the opposite; disagreement stated, side not picked, `C5`), `UTIL UW→UW−` (declined on NEWNESS not quality — already the board's worst on both axes last run and Δ −0.025 ≈ flat; note 08-30 declined the same move on METHOD, a different and weaker reason), `IT N→OW/UW` (1名 `NVDA` 19.4%; `wflow` +0.033 vs `eqflow` −0.034 opposite signs ⇒ routed to PREMORTEM), `DISC UW→UW−` (1名 `AMZN` 40.2%, and the universe's two largest runners `DASH`/`ABNB` sit inside the UW), `COMM` further cut (MACRO already cut one notch TODAY on the same Δ ⇒ double-count), `RE UW→UW−` (Δ +0.078 = 2nd-best, wrong direction), `STPL N→UW` (rank 7 mid-table, Δ +0.080), `HLTH`/`MATR OW→OW+` (no notch above OW exists)** · **flip list 3 of 11 — IT/`NVDA` 19.4%, ENRG/`XOM` 30.5%, DISC/`AMZN` 40.2% — UNCHANGED from 08-30, the first run in four in which the flip set did not move** · ★ **`D424` applied to this board for the first time and it caught a case the flip guard cannot: `HLTH` does NOT flip yet `wflow` +0.021 vs ex-`LLY` +0.095, i.e. the top-1 DRAGS a broader positive; the mirror case is `RE` (−0.338 → −0.415 without `WELL`, the top-1 HOLDS IT UP) and `STPL` (−0.264 → −0.130 without `WMT`, drags)** · 🚨 **instrument state: the NATIVE sweep scored 0 of 299 for a SECOND consecutive run (301/301 tickers carry a 2026-08-28 Close=NaN, T+3 across a weekend ⇒ this is a standing hole, no longer a transient); `SECTOR_FLOW_US.json` left EMPTY as the honest record; all numbers from `SECTOR_FLOW_US_REPAIRED.json`, independently rebuilt today and agreeing with 08-30's separate reconstruction to ≤0.002 on 11 of 11 sectors** · **`n_axes` 3, `vel_coverage` 15.72% ⇒ ZERO deltas cite velocity or freshness; Δ IS legal this run (prior same-mode snapshot 08-27 `nonews` n=299, 299/299 common) and every Δ carries the label `repaired sweep, 08-27 → 08-28`** · ★★ **the structural line: `eqflow` is positive in exactly 4 of 11 sectors (MATR +0.164, HLTH +0.135, COMM +0.080, ENRG +0.005) and only TWO of those four are also positive on `wflow` — the board is narrow at the top and the two axes disagree on half of the positive set** · **uncovered=[IT(N — routed to PREMORTEM, 08-30 = 0 runs, the book's largest concentration; `S124` settles on the NEXT run and tests this desk's own IT underweight cross-sectionally, with branch B the one that vindicates the desk), FIN(OW−, 08-30 = 0 runs, PAD REJECTED, the board's largest bucket with ZERO greens in 47 and its two non-cap-weighted signals in disagreement), COMM(OW−, 08-30 = 0 runs, PAD REJECTED, un-measurable BY RULE 12th run via `D297`), DISC(UW, 08-27 = 3 runs, 1名 `AMZN`, contains the universe's two largest runners), INDU(UW− — DEMOTED TODAY, 08-27 = 3 runs, 17 reds = board's most, bracketed on 09-04 by `S126`+`P114`), STPL(N, 08-27 = 3 runs, rank 7 mid-table), RE(UW, 08-26 = 4 runs, ex-top1 WORSE than headline), UTIL(UW, 08-23 = 6 runs — the board's worst `eqflow` (−0.524) and worst red-rate (66.7%) and the LONGEST recency gap on the board, NOT slotted because UW sectors do not take DEEP slots; this is the 2nd consecutive run in which the board's most extreme sector is structurally unreachable by the selection rule, and it is named here rather than dropped)]**

## ✅ EXIT CHECK
- [x] **§1 is ONE line**, inherited verbatim from MACRO §D. No unchanged sector gets a row, paragraph
      or restated flow number.
- [x] **Every §2 delta cites a flow number** — the single delta (`INDU`) cites Δ, `eqflow` rank and
      absolute red count, all non-cap-weighted. **Every decline also carries its number**, and the
      one decline that would have been a **macro re-argument** (Energy, on the escalation) is
      declined explicitly on that ground plus the `asof` clock.
- [x] 🚨 **No promotion or demotion rests on a `top1_flips_sign` bucket.** All three flippers
      (IT/`NVDA`, ENRG/`XOM`, DISC/`AMZN`) had moves attempted and **all three were declined with
      *"this sector's sign is `<name>` at `<top1_w>`%"* written out.** The flip list is reproduced in
      §2 even though it changed nothing. ★ Plus the `D424` non-flipping exception (`HLTH`).
- [x] **Axis count stated**: `n_axes` **3**, `vel_coverage` **15.72%** ⇒ no delta cites freshness or
      velocity; Δ is read only against a same-axis-count snapshot (08-27 `nonews`, 299/299 common).
- [x] Every matrix×flow divergence named with a resolution owner — **Energy → DEEP R1**, **HLTH's
      `D424` gap → DEEP C2**, **MATR's `C24` → DEEP C1**, **IT → PREMORTEM**, **FIN's 0-greens-in-47
      → logged in DEEP_LOG as un-owned**.
- [x] **N DEEP targets by the rule** — continuity stated (`MATR`,`HLTH` keep their slots), recency
      read **from files on disk**, `ENRG`'s **1-run recency violation declared** under the
      recency-starved fallback, **4th slot unfilled with both rejected pads named**, no padding.
      **OW sectors left without a slot: none.** All uncovered sectors named in DEEP_LOG with recency.
- [x] **Linter** — `python -X utf8 scripts/report_lint.py llm_outputs/2026-08-31/industry_US/SECTOR_ROTATION.md`
      → **0 findings** on C1 / C2 / S6 / D6, no exemptions claimed. ⚠ Form only.
- [x] `DEEP_LOG` line appended.
- [x] The delta count is 1, not 0 — and the file is short because ten of eleven attempts were
      declined, which is the informative output, not a reason to manufacture differences.
