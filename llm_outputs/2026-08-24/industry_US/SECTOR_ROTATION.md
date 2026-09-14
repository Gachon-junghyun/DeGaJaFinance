# SECTOR_ROTATION — industry_US · 2026-08-24 (Mon) · Stage 6 / L1·ROTATION

> **Delta-only.** MACRO §E owns the 11-sector verdict; `SECTOR_FLOW_US.json` owns the flow numbers.
> Both are on disk. This file writes **only what changes and why**.
> **Axis count this run: `n_axes = 3` (`vel_axis = false`, `vel_coverage = 0.0`, `scored = 299`).**
> 🚫 **No delta below may cite theme freshness or news velocity from the sweep**, and Δ-vs-prior is
> read only against a same-axis-count snapshot (08-22 and 08-23 are both `nonews`/3-axis — legal, and
> the Δ is **exactly zero**).

## §1 · Inherited — one line, verbatim from MACRO §E

`MACRO holds: ENRG OW · HLTH OW · MATR N+ · STPL N · COMM N · DISC N · FIN N · RE N− · INDU UW− · UTIL UW− · IT N`

## §2 · Deltas — **ZERO verdict changes**, and today the zero is arithmetic before it is a judgement

**`n_new_sessions_since_prior_run = 0`, second consecutive run.** All 299 `flow_score`s, all 299 tags
and all 11 sector `wflow` values are **identical to the 08-23 file and to the 08-22 file**. A delta
would have to come from a number that did not change.

★ **One genuinely new flow number exists this run, and it is the reason the zero had to be argued
rather than assumed**: `participation` = (`OBV 매집` ∧ `rs20 > 0`)/n, computed for the first time on the
US board (`M865`, SWEEP §2, the `D325`/`D332-KR` remedy). **Universe green_rate 2.01% vs participation
31.44% ⇒ +29.4pp**, and it re-ranks the board hard. **It was not used to move a verdict** — see COMM below.

**Nine promotion/demotion attempts, each declined with a number:**

| # | Attempt | Flow evidence | Verdict | Why declined |
|---|---|---|---|---|
| 1 | **COMM N → N+** | ★ `participation` **66.7% — rank 1 of 11** (8 of 12 names OBV 매집 ∧ rs20>0), against `green_rate` **0.0%** (joint last). `eqflow` +0.095, `wflow` +0.108 | **DECLINED — routed to a DEEP slot** | Three reasons, all numbers: **(a)** `participation` is on its **first US run** — a verdict may not move on an indicator's opening day; **(b)** the inputs are **byte-identical to the last two runs**, so the 66.7% was equally true on 08-22 and is **information about our instrument, not about the tape**; **(c)** 🚨 **`D297`, 5th run unfixed** — `GOOGL` **38.3%** + `GOOG` **38.3%** = the Alphabet complex is **76.6%** of a 12-name bucket while `top1_w` reports half, **and both classes are inside the 8 participating names.** The flipper guard is structurally blind here |
| 2 | **ENRG OW → higher** | `exc5` **+3.519 vs `SPY`** (rank 2 of 11) · `participation` 37.5% (rank 4) · `PSX` +0.728 / `MPC` +0.700 / `COP` +0.694, all OBV 매집 | **DECLINED** | `green_rate` **0.0%** and **`S74` settled `FIRED-C` today with its own anti-signal (a) partially fired** — a *third* Hormuz channel (bilateral exception-granting) exists that no bracket covers. **A two-sided object does not carry a promotion.** ⚠ The only same-day evidence pointing the other way is a **LIVE INTRADAY PRINT** (Brent −1.3%), which is inadmissible in this frame |
| 3 | **HLTH OW → higher** | **Rank 1 on three independent instruments**: `wflow` +0.196 · `eqflow` +0.229 · `exc5` **+3.889** · `participation` 59.4% (rank 2) · `MRK` +0.978 🟢 surge 1.56 | **DECLINED** | 🚨 **Zero narrative coverage** — EVENT_ALPHA Card 7 could produce **no direction body-read** because no HC thread exists in `brief`'s head, `thread`'s top-20, or the term table. MACRO §E logged the same hole. **Promoting a sector whose only evidence is price is promoting on price** |
| 4 | **INDU UW− → lower** | `exc5` **−1.736 = −1.29σ** (trailing-60 mean +0.437 / sd 1.681) · `participation` 16.0% (rank 10) | **DECLINED — no notch below UW− exists** | Routed to **`P93`** (settles 08-28), which is armed on exactly this question |
| 5 | **UTIL UW− → lower** | `participation` **0.0%** · `eqflow` −0.621 · `exc20` **−11.469** (worst on board) | **DECLINED — no notch below UW−** | ★ **The only sector where `green_rate` and `participation` agree (0.0 / 0.0).** Nothing to change; the grade already says it |
| 6 | **STPL N → any direction** | `eqflow` +0.048 · `participation` 31.6% · `TGT` +0.950 🟢 vs `WMT` −0.333 🔴 = **17.1pp intra-sector (`W5`)** | **DECLINED BY RULE — routed to a DEEP slot** | 🚨 **`top1_flips_sign = true`: the sector's sign is `WMT` at 28.9%** (`wflow` −0.013 → `ex_top1` **+0.116**), **3rd consecutive run.** Per the flipper rule a 🚨1名 bucket may carry neither promotion nor demotion |
| 7 | **MATR N+ → N** | `exc5` **mean +1.813 but median −0.315 — opposite signs** · `participation` 25.0% · `ECL` +0.606 🟢 | **DECLINED** | A mean/median sign disagreement is a **dispersion finding (`W5`)**, not a verdict. And `Copper` COT at the **100th percentile** is **6-day-stale positioning** — `D6` context, never a trigger |
| 8 | **IT N → UW** | `exc5` **−2.655 (worst on board)** but `exc20` **+1.992** — **the two windows disagree in sign** · `participation` 30.4% | **DECLINED — routed to PREMORTEM** | `C5`/`W5`: two admissible windows contradict. And **`NVDA` prints in two sessions (08-26, 🔀binary, `theme-age` 14.11×)** — a grade change at D-2 into a known binary is a timing bet, not a flow reading, and is precisely the one-way tilt PREMORTEM exists to bracket |
| 9 | **FIN N → lower** | `exc5` **mean +0.877, median −0.086** (same sign split as MATR) · `eqflow` **−0.034 = rank 6 of 11**, not bottom · `participation` 29.8% | **DECLINED** | Rank 6 is not a demotion case, and the mean/median split is dispersion |

### §2-a · Flipper list reproduced in full — **1 of 11**, unchanged for a third run

| Sector | top1 | `top1_w` | `wflow` | `wflow_ex_top1` | flips? |
|---|---|---:|---:|---:|---|
| **Consumer Staples** | **`WMT`** | **28.9%** | **−0.013** | **+0.116** | 🚨 **YES** |
| *(the other ten)* | — | — | — | — | `top1_flips_sign = false` |

⚠ **Compounding hazard, now shown to be structural rather than coincidental** (PREFLIGHT §1):
`WMT` is *also* one of the six tag-contaminated names, and it is contaminated **because** it is a
mega-cap and flips the sign **because** it is a mega-cap. **The two defects share a cause.**
🚨 **`D297` is a second, invisible flipper case**: the Alphabet complex at **76.6%** of COMM is never
tested by `top1_flips_sign`, which sees only 38.3%. **5th run unfixed.**

### §2-b · Replication hygiene — what is NOT a new observation today

★ **`M144`/`D270` is a RE-PRINT, not a 13th independent replication.** 94 names pass
`OBV 매집 ∧ rs20 > 0`; **6 are 🟢; 88 are blocked and 100% of them on `vol_surge` alone.** These are the
identical numbers the 08-22 and 08-23 runs printed, because the frame is identical. **The independent
observation count stays at TWELVE.** Inflating it would be today's cheapest available error, exactly
as the 08-23 run wrote.
★ **`R81`/`D290` again had nothing to replicate** (299/299 velocities `null`) ⇒ admissible green count
**6** = printed green count 6; all 6 `US_LIVE_SHORTLIST` rows admissible. **The rule is not retired —
it re-binds on the next partial-coverage run**, and PREFLIGHT §1 now shows that run's contaminated set
is the **top-49 by market cap**, not a random sixth.

### §2-c · One measurement that changes how a 🟢 must be quoted downstream

HANDOVER §6 scored the US IC ledger for the first time (405 rows / 33 run-dates):
**`vol_surge` h=1 `IC +0.0398`, `t(NW) +3.40`, 67% positive — Bonferroni pass, POSITIVE**, against KR's
`−0.0454 / −3.86`. 🚫 **The KR argument for distrusting the 🟢 gate does not transfer (`W1`).**
But **`rs60` h=5 is `IC −0.1310`, `t(NW) −5.46`, 7% positive — Bonferroni pass, NEGATIVE**, with h=1
the same sign, **and all six greens sit on high rs20** (14.2 · 26.5 · 12.8 · 17.3 · 11.4 · 1.2).
⇒ **Horizon decides. Every 🟢 citation downstream carries its horizon on the same line.**
⚠ Regime label required: the ledger window is **2026-07-13 → 2026-08-20**, which contains the
mid-August drawdown; `rs60`'s −5.46 is the shape a drawdown produces. `n_eff 5.4` clears the bar only
just, and the h=10 cells are **unquotable** (`n_eff 2.1`).
🚫 **No verdict moved on this.** It is a citation constraint, not a delta.

## §3 · DEEP picks and DEEP_LOG — **N = 4** (protocol budget: 2 continuous + 2 rotating)

**Continuous ⌈4/2⌉ = 2 — `ENRG` and `HLTH` KEEP their slots.** Both held a continuous slot in the
previous run and both remain today's only OW ranks ⇒ **anti-thrash continuity applies, stated.**

**Rotating ⌊4/2⌋ = 2 — a DECLARED recency-starved deviation for an ELEVENTH run.** MACRO holds only
**two** OW sectors and both took continuous slots. The next-highest grade is `MATR` (N+), **covered
2026-08-21 — inside the ~3-run bar.** ⇒ R1/R2 are filled from non-OW by **evidence density with
recency as the stated tiebreak**:

| Slot | Sector | Last covered | Mandate the DEEP must answer |
|---|---|---|---|
| **C1** | **ENRG** (OW) | 08-23 (continuous) | **`S74` settled `FIRED-C` and its anti-signal (a) partially fired.** Does the ENRG OW survive a Strait that hardened (fatal strike, seizure, strictest-ever sanctions) *and* partially reopened (Iraqi permits, on neither named condition) in the same 72 hours? And is the refining leg's `rs60 +37/+44/+43` a capacity thesis or a war premium? ⚠ **MPC FY2025 10-K Item 1A is unopened for a 2nd run** — `M831`/`M833`'s contradiction (+106.7% YoY R&M margin on *lower* utilisation, attributed by the issuer to conflict-driven supply disruption) cannot be resolved without it |
| **C2** | **HLTH** (OW) | 08-23 (continuous) | 🚨 **Rank 1 on `wflow`, `eqflow` and `exc5`, rank 2 on `participation` — and ZERO narrative coverage.** Attempt 3 was declined on exactly this. Is the leadership a mechanism or a one-week rotation artifact? **The DEEP must produce the direction body-read EVENT_ALPHA could not**, and register an HC term in the living table |
| **R1** | **COMM** (N) | **2026-08-19 ≈ 5 runs** | ★ **The board's largest matrix×flow contradiction, and it is brand new**: `participation` **66.7% (rank 1)** against `green_rate` **0.0%** (joint last). Resolve: is the 66.7% real breadth or an artifact of a sector whose eight participating names all accumulate on **sub-0.83 `vol_surge`**? ⚠ **`D297` must be handled explicitly** — the Alphabet complex is **76.6%**, so the answer must be computed **ex-`GOOGL`-and-`GOOG`**. Also: **the `T` orphan is 9.74% of the real book's invested for a 7th run, with no cycle label and no card** |
| **R2** | **STPL** (N) | **2026-08-17 ≈ 7 runs — worst recency on the board** | Flipper-blocked at the sector level (attempt 6), so the DEEP is the only place it can be examined. **`TGT` +0.950 🟢 (surge 1.51, rs60 +26.9) vs `WMT` −0.333 🔴 (surge 1.68, rs60 −14.6) = 17.1pp on one window (`W5`)** — two consumer-staples retailers, opposite tags, **and both clear the `vol_surge` gate**, so this is not a filter artifact. ★ **New object from EVENT_ALPHA Card 1: Canada's retaliation list names *dairy* and *agricultural goods*, effective 2026-09-08** |

**Not padded.** No Neutral/UW sector was added to reach N; R1/R2 are declared deviations, not filler.

## DEEP_LOG 2026-08-24: continuous=[ENRG, HLTH] rotating=[COMM, STPL] · N=4/4 · **ZERO verdict deltas, and for the second run running the zero is STRUCTURAL rather than a judgement — `n_new_sessions_since_prior_run = 0` and the persisted sweep is element-identical to BOTH 08-23 and 08-22 (0/299 scores, 0/299 tags, 0/11 sector `wflow`s), so three consecutive runs stand on the 2026-08-21 close. NINE attempts declined with numbers (COMM→N+ declined despite `participation` 66.7% rank 1 — new-indicator first run ∧ inputs byte-identical to two prior runs ∧ `D297` puts the Alphabet complex at 76.6% of a 12-name bucket with both classes inside the participating 8 — routed to a DEEP slot · ENRG→higher declined: `green_rate` 0.0% and `S74` `FIRED-C` with anti-signal (a) partially fired ⇒ two-sided · HLTH→higher declined: rank 1 on three instruments with ZERO narrative coverage, promoting on price · INDU→lower and UTIL→lower declined: no notch below UW− exists · STPL→any declined BY RULE, `WMT` 28.9% flips the sign, 3rd run · MATR→N declined: `exc5` mean +1.813 vs median −0.315 = dispersion `W5`, and Copper COT 100th %ile is 6-day-stale `D6` context · IT→UW declined: `exc5` −2.655 vs `exc20` +1.992 disagree in sign AND `NVDA` prints in 2 sessions — routed to PREMORTEM · FIN→lower declined: `eqflow` −0.034 ranks 6 of 11)** · **flip list 1 of 11 — Consumer Staples/`WMT`/28.9% (`wflow` −0.013 → `ex_top1` +0.116), unchanged 3rd run; the other TEN print `top1_flips_sign = false`** · 🚨 **`D297` reproduces unfixed for a 5th run and today it is load-bearing: the Alphabet complex is 76.6% of COMM while `top1_w` reports 38.3%, and COMM is this run's R1 DEEP pick precisely on a breadth number that both Alphabet rows sit inside** · **★★ the run's structural headline is a MEASUREMENT ON THE DESK'S OWN INSTRUMENTS, not on the tape: (1) `participation` computed on the US board for the first time reads 31.44% against `green_rate` 2.01% = +29.4pp, LARGER than the KR desk's +26.4pp, and it inverts COMM from joint-last to rank 1 (`M865`); (2) the sweep's news bucket is positionally identified as universe ranks 0–48 — contiguous, 49/49 identical to yesterday, 16.4% of names but 69.0% of market cap — so the tag contamination is deterministic and MEGA-CAP-SELECTIVE, retracting two runs of "arbitrary bucket" language (`M856`); (3) the US `ic_ledger` was scored for the first time (405 rows / 33 run-dates) and INVERTS the KR verdict on the 🟢 gate's gatekeeper axis — `vol_surge` h=1 `t(NW) +3.40` POSITIVE in the US vs `−3.86` in KR, both Bonferroni-passing, retracting the 08-23 claim that the US desk had no equivalent measurement (`R98`, `M854`)** · **★ `M144`/`D270` is a RE-PRINT not a 13th replication (94 pass `OBV 매집 ∧ rs20>0`, 6 🟢, 88 blocked, 100% on `vol_surge` alone — identical to 08-22/08-23 because the frame is identical); the independent-observation count stays at TWELVE** · **`R81`/`D290` had nothing to replicate for a 3rd run (299/299 null ⇒ admissible greens 6 = printed 6)** · **rotating slots are a DECLARED recency-starved deviation for an ELEVENTH run: only 2 OW exist and both took continuous slots, MATR (the only N+) was covered 08-21 inside the ~3-run bar ⇒ R1/R2 filled from non-OW by evidence density with recency as tiebreak — COMM on the board's largest matrix×flow contradiction (participation rank 1 vs green_rate joint-last) plus ~5-run recency plus the `T` orphan at 9.74% of real invested for a 7th run, STPL on the board's WORST recency (08-17 ≈ 7 runs) plus a 17.1pp `TGT`/`WMT` split where BOTH names clear the `vol_surge` gate (so it is not a filter artifact) plus Canada's 09-08 retaliation list naming dairy and agricultural goods** · **🚨 `D341` filed at EVENT_ALPHA: the desk cannot tag what its own discovery layer surfaces — `AA`/`X`/`WY` (the Canada-tariff epicentre, this run's #1 object), `LYB`/`DOW` (the named counterparties in Shell's $8bn US chemicals sale) and `BABA` (the $10.2bn HK placement issuer) are ALL outside `us_top300`, so THREE of eight EVENT_ALPHA cards carry no flow-tagged principal** · **🚨 `D342` filed: both trade-war brackets (`P92`, `P93`) settle 2026-08-28, ELEVEN DAYS BEFORE Canada's retaliation takes effect 2026-09-08 — they can measure the announcement and never the implementation, and no row on this board is keyed to 09-08** · **uncovered=[MATR(N+, 08-21, recency-blocked at 3 runs; `exc5` mean +1.813 vs median −0.315 sign split, Copper COT 100th %ile, and NEW — Shell's $8bn US chemicals sale with `XOM` bidding, surfaced only by the blind-spot pass at `CHEMICALS` z 13.2, with `LYB`/`DOW` untaggable), IT(N, 08-23, ROUTED TO PREMORTEM — `NVDA` D-2 🔀binary at `theme-age` 14.11×, `P90`, `S115`/`S117`, `exc5` −2.655 vs `exc20` +1.992 sign split, 4 of 11 book names, `SECTOR_DEEP_SEMI` at 40 days), INDU(UW−, 08-22, `P93` armed at −1.29σ and `D342`'s 09-08 gap — the board's only live transmission test), FIN(N, 08-22, `exc5` mean/median sign split, `NDAQ`/`MET` held), DISC(N, 08-23, `AMZN` 40.2% with `ex_top1` +0.254 vs `wflow` +0.122, `participation` 39.3% rank 3), RE(N−, 08-22, `participation` 16.7%, measured rate beta −0.0072 ⇒ the UW rests on flow not on rates), UTIL(UW−, 08-23, `participation` 0.0% — the only sector where both breadth instruments agree, `exc20` −11.469 worst on board)]**
