# SECTOR_ROTATION — industry_US · 2026-08-25 (Tue) · Stage 6 / L1·ROTATION

> **Delta-only.** MACRO §E owns the 11-sector verdict; `SECTOR_FLOW_US.json` owns the flow numbers.
> Both are on disk. Nothing unchanged is restated here.

**Axis count this run: `n_axes = 3` · `vel_coverage 0.1706` (51/299) ⇒ the news axis is DEAD.**
🚫 **No delta below cites theme freshness or news velocity.** Δ against the prior snapshot is
axis-legal (3 vs 3) but ⚠ **spans a settled-08-21 → stub-08-25 terminal-bar change (`D355`)**, so
**every delta below is argued on an ABSOLUTE flow level and its rank, never on a Δ.**

---

## §1 · Inherited from MACRO §E — one line, verbatim

`MACRO holds: ENRG OW · HLTH OW · STPL N+ · MATR N+ · COMM N · DISC N · FIN N · RE N− · UTIL UW− · INDU UW− · IT UW`

---

## §2 · Deltas — 2 changes from 10 attempts, every decline carried by a number

### 🚨 Flip list first, reproduced even though it changed the constraint (rule: a silent flipper is how one company becomes a sector call)

**`top1_flips_sign = TRUE` on 1 of 11: `Health Care` — top1 `LLY`, `top1_w` 19.4%.**
The other **ten print `false`**, including **Consumer Staples**, which was the flipper on 08-22, 08-23
and 08-24 and **has LEFT the set this run** (`wflow −0.224`, sign held without `WMT`).
⚠ **`D297`, 6th run unfixed**: the test is per-ticker, so `GOOGL` (38.3%) + `GOOG` (38.3%) = **76.6%
of COMM** while `top1_w` reports half and the flag prints `false`. **COMM is treated as a flipper
bucket regardless of the flag.**

### Changes (2)

| sector | matrix said | flow evidence (`SECTOR_FLOW_US.json §sector_rotation`, asof 08-25) | new verdict | who resolves |
|---|---|---|---|---|
| **Consumer Staples** | **N+** | `eqflow` **−0.217, rank 8 of 11** · `wflow` −0.224 · **1 🟢 / 3 🔴 of 19** · breadth 0.05 · **not a flipper this run** (sign holds ex-`WMT`) | **N** | **DEEP not available — logged to DEEP_LOG with mandate** |
| **Materials** | **N+** | `eqflow` **−0.165, rank 6 of 11** · `wflow` −0.103 · **0 🟢 / 3 🔴 of 12** · **breadth 0.00** | **N** | **DEEP slot R1 (this run)** |

**Why these two and not the others.** Both are matrix-**positive** sectors whose money is **absent on
an absolute, non-cap-weighted number** — rule (a), *"right thesis, money not here yet"* → down a notch.
Neither is a `top1_flips_sign` bucket, so the demotion does not rest on one name.
★ **The Staples case is the sharper one and it is stated as a contradiction, not resolved**: STPL is
simultaneously **the board's BEST 5-session price sector** (equal-weight `exc5` **+5.048** vs `SPY`,
median +5.243, **17 of 19 names positive**) and **8th of 11 on `eqflow`**. **Price says broad strength;
money says absence.** The notch down follows the flow rule; **the price fact is carried into DEEP_LOG
as the mandate, not buried.**

### Declines — 8 attempts, each refused with a number

| attempted | evidence for | why declined |
|---|---|---|
| **HLTH OW → N** | `eqflow` collapsed **+0.229 → +0.004**; **5 🔴 of 32**; `LLY` `delta −0.383` | 🚫 **DECLINED BY RULE — Health Care is this run's flipper** (`LLY`, 19.4%). Substituting the non-cap-weighted numbers: **`eqflow +0.004` is still rank 2 of 11** and price breadth is **29 of 32 positive** (`exc5` +4.295, `exc20` +3.318 vs `SPY`). ⇒ **verdict stays where MACRO put it.** Written out per the rule: *this sector's flow sign is `LLY` at 19.4%* |
| **ENRG OW → OW+** | Only **positive `eqflow` on the board (+0.227)** and the **only sector with ZERO 🔴** (1 🟢 / 0 🔴 of 16) | Declined — **two-sided.** The commodity leg is breaking on a **LIVE 08-25 print** (Brent −4.65%, 3-2-1 crack −8.21, `P96`), and a live futures bar is **not** a flow number. Promoting into an un-settled adverse print is the `D273` shape. **Routed to DEEP (continuous slot C1)** |
| **IT UW → N−** | `eqflow` **−0.090 ranks 4 of 11** — the flow is *not* bottom-of-board, and `exc20` is **+0.189 ≈ flat** | Declined — this would be a **promotion on the two axes this desk's own IC ledger ranks NEGATIVE** (`rs60` h=5 `IC −0.1310`, `t(NW) −5.46`, Bonferroni-passing) plus C-grade OBV (`D6`), against **43 of 56 names negative on price with mean ≈ median**. ⚠ And **2 of IT's 3 🟢 are velocity-derived and withdrawn** (SWEEP §3) ⇒ its admissible green count is **1** (`MSTR`). **Routed to DEEP slot R2** |
| **COMM N → N+** | `eqflow` **−0.086 ranks 3 of 11**; price `exc5` +3.478 with 11 of 13 positive | 🚫 **DECLINED BY RULE, `D297`** — the Alphabet complex is **76.6% of a 12-name bucket** across two ticker rows, so neither `wflow` nor `eqflow` is a sector number here. **Recorded as un-measurable, not as neutral** |
| **DISC N → N−** | **0 🟢 / 8 🔴 of 28**, **breadth 0.00**, `eqflow` −0.159 rank 5 | Declined — **both admissible axes contradict (`C5`)**: price is `exc5` **+3.091**, median +2.431, **24 of 28 positive**. A demotion on flow while price breadth is 86% positive is picking a side of an open contradiction. **Logged uncovered** |
| **FIN N → N−** | **2 🟢 / 10 🔴 of 47**, `eqflow` −0.194 rank 7 | Declined — same `C5` shape: price `exc5` **+2.662**, median +2.413, and MACRO recorded that FIN's **mean/median sign disagreement CLOSED** this run. ⚠ 17 of 47 negative is the third-worst breadth on the board and is logged, not acted on |
| **RE N− → UW** | `eqflow` **−0.410, rank 10 of 11**, 0 🟢 / 3 🔴, breadth 0.00 | Declined — **`C5` again, and this one is measured**: MACRO's price cut has RE's **median `exc5` +2.782 at 2.1× its mean (+1.319)**, i.e. the sector is *better* than its aggregate. ⚠ And the duration-UW's measured rate beta is **−0.0072 pp/bp ≈ zero**, so a rate argument would be a **macro re-argument** and is barred here. **Logged uncovered** |
| **UTIL UW− / INDU UW− → lower** | UTIL `eqflow` **−0.616**, **10 🔴 of 15**; INDU **−0.313**, **18 🔴 of 50, 0 🟢** | Declined — **no notch below `UW−` exists.** Both are the run's cleanest flow×price agreements (UTIL price `exc5` −1.011 / 13 of 15 negative; INDU −1.881 / 30 of 50 negative) and need no change |

⇒ **2 deltas from 10 attempts. Eight declines, every one carried by a number rather than by a
judgement, and two of them declined BY RULE on flipper/share-class grounds.**

---

## §3 · DEEP picks and DEEP_LOG — **N = 4** (protocol budget: 2 continuous + 2 rotating)

### Continuous track (⌈N/2⌉ = 2) — anti-thrash continuity applied and stated

**C1 `ENRG` · C2 `HLTH`.** Both held continuous slots in the previous run **and** are still the only
two OW ranks today ⇒ **the continuity rule keeps the slots**; this is stated rather than re-derived.

- **`ENRG` mandate**: the sector has the board's **only positive `eqflow` (+0.227)** and **zero 🔴**,
  while its commodity leg broke **−4.65% (Brent) / −8.21 (crack)** on a LIVE bar. **Resolve: is the
  refining `exc20 +12.85` a capacity story that survives a falling crude AND a falling crack, or does
  `P96` branch A retire it?** Sub-question the desk owns and has not answered: **`MPC` and `PSX` are
  the book's two best flow scores (+0.578 / +0.556, both OBV 매집, `rs60` +43.3 / +35.5) and BOTH are
  blocked from 🟢 by `vol_surge` alone** (0.84 / 0.80) — **and `D355` makes that blocker ~18% tighter
  on a pre-market run than on a settled one.**
- **`HLTH` mandate**: **the flipper question.** `eqflow` collapsed +0.229 → +0.004 while price breadth
  is **29 of 32 positive**. **Resolve: is the flow collapse `LLY`-specific (19.4% of the sector,
  `delta −0.383`), in which case the OW is broad-based — or is it the sector?** Second mandate:
  **`MRK` is the sector's only 🟢, survives the velocity withdrawal (surge 1.53), carries a clean FINRA
  short read (z −0.72) — and carries revisions of 1↑/5↓ with RSI 86.7.** Both readings stand; DEEP must
  say which one the KPI table should track.

### Rotating track (⌊N/2⌋ = 2) — ⚠ **DECLARED recency-starved deviation, 12th consecutive run**

Only **two OW ranks exist** and both took continuous slots. Per the documented fallback, R1/R2 are
filled from non-OW by **evidence density with recency as tiebreak**, and the deviation is declared.

- **R1 `MATR`** — **last covered 2026-08-21 = 4 runs, the board's worst recency**, and the only
  matrix-positive sector **outside** the ~3-run bar. This is the one rotating pick that needs no
  evidence-density override: the recency rule selects it.
  **Mandate**: this run **demoted it N+ → N on `eqflow −0.165` / 0🟢 3🔴 / breadth 0.00** while price
  reads `exc5` **+2.621** with 10 of 12 positive. **Resolve the contradiction.** Carried constraints:
  **Copper COT at the 100th percentile** (3rd run, `D6` context-not-trigger), **`S122` armed to 09-30**
  on Shell's $8bn US chemicals sale, and 🚨 **`LYB`/`DOW` are outside `us_top300`** (`D341`) so the
  named counterparties are untaggable.
- **R2 `IT`** — **recency 1 run (08-24), the worst among the candidates, and taken anyway on evidence
  density. The cost is stated below, not hidden.** The 08-24 IT slot was a **PREMORTEM-promoted 5th
  slot on a narrow, disjoint mandate**, not a full sector map; `SECTOR_DEEP_SEMI.md` is **41 days old**.
  **Evidence density, all measured this run**: the run's **only matrix verdict change** (N → UW);
  **43 of 56 names negative on `exc5` with mean −4.761 ≈ median −6.279** (broad, not mega-cap);
  **`exc20 +0.189` = twenty sessions erased in five**; **`P79` settles TONIGHT at −10.852, inside
  branch B**; **`NVDA` prints tomorrow (D-1)**; **`AI capex` narrative ⚪0.62× on a readable 1,176 base
  = decelerating**; **4 of the 11 US book names sit here** (`ANET` `AVGO` `HPE` `NVDA`).
  **Mandate**: **is the de-rate a factor event or an epicenter event?** MACRO's own split says the
  sector is two businesses **19.17pp apart** (`M876`); DEEP must test whether today's 43/56 breadth
  crosses that line or respects it. ⚠ **DEEP must NOT re-litigate the `NVDA` print** — `S79`, `S103`,
  `P90` and `S118` already own it and a fifth reading would be `D343`.

**No padding.** Neutral/UW sectors were not used to reach N; `MATR` and `IT` were selected by the
stated fallback, not to fill a quota.

---

## DEEP_LOG 2026-08-25: continuous=[ENRG, HLTH] rotating=[MATR, IT] · N=4/4 · **TWO verdict deltas (STPL N+→N · MATR N+→N) from TEN attempts, and for the first time in four runs the deltas are NOT structural-zero — the tape advanced one settled session (terminal bar 2026-08-24, the first new close since 08-21) and the deltas are argued on absolute `eqflow` levels and ranks, never on Δ, because `D355` makes this run's snapshot a stub-bar snapshot** · **flip list 1 of 11 — Health Care/`LLY`/19.4% (`eqflow` +0.229 → +0.004, `top1_flips_sign` TRUE); ★ Consumer Staples/`WMT` LEFT the set after THREE consecutive runs as the flipper, which is what made today's STPL demotion admissible at all** · 🚨 **`D297` reproduces unfixed for a 6th run and COMM is again treated as a flipper bucket regardless of its `false` flag (Alphabet complex 76.6% of a 12-name bucket across two ticker rows)** · 🚨🚨 **`D355` filed at SWEEP — the sweep ran on an UNSETTLED pre-market bar (median volume 3.18% of the prior session, 0 of 300 names above 50%) and it depressed universe `vol_surge` median 0.820 → 0.670 (−18.3%) with the ≥1.2 count falling 22 → 12 (−45%); `vol_surge` h=1 is the ONLY US IC cell with a Bonferroni-passing POSITIVE sign (`t(NW) +3.40`), and this desk runs pre-market every day, so the depression is systematic and `n_axes` continuity (G2) cannot detect it** · **`R81`/`D290` RE-BINDS after three runs with nothing to replicate: `vel_coverage` returned to 17.1% ⇒ **4 of 8 greens are velocity-derived (`MRVL` 0.74 · `ORCL` 0.47 · `CVX` 0.73 · `MA` 0.68, all `vol_surge` < 1.0) and ALL FOUR are also this run's ENTIRE `new_green` list** ⇒ admissible green count **4**, and **100% of the day-over-day "ignitions" are artifacts of which 51 names the news pipe had budget to query** · **`M856` reproduced exactly and one rank wider: the news bucket is universe ranks 0–50, CONTIGUOUS (`rk == range(0,51)`), 51 of 299 names, and the overlap with 08-24's bucket is ZERO because that run measured none** · **★★ the run's structural headline is on the TAPE for the first time in four runs: an AI-compute de-rate paid for by defensives, `EW{STPL+HLTH} − EW{IT}` 5-session = **+9.336 = the 97.6th percentile of two years** against a two-year mean of −1.064, with IT 43/56 negative and STPL 17/19 positive — and `theme-age "AI capex"` reads ⚪**0.62×** on a readable 1,176 base, i.e. the de-rate is arriving while its own narrative DECELERATES** · **★ `P79` sits at −10.852 INSIDE branch B one session before settle, having travelled −12.425 → −7.178 → −5.609 → −10.852; `S108` sits at +0.484 with its three legs 3.75pp apart and `XLU` negative, so its own premise ("the three underweights rip together") is weakening before its settle** · **★ EVENT_ALPHA Card 2's finding is an ABSENCE: `chain-hop "Rubin"` scanned 230 articles and returned ZERO chain-hop candidates — every `us_top300` name the story touches is already headline-named, so the un-named beneficiary layer this tool exists to find does not exist here; reported rather than replaced by a plausible neighbour** · **★ EVENT_ALPHA Card 1's finding is a LINK: `chain-hop "Treasury buyback"` ties the bond-buyback thread to the Bitcoin thread through one liquidity mechanism ("How a Treasury buyback tweak helped bitcoin surge 25%"), surfacing `BLK` (title 0 / body 12, OBV 매집, `rs60 +10.6`) as the run's only CONFIRMED-EARLY un-named name** · **rotating slots are a DECLARED recency-starved deviation for a 12th run: only 2 OW exist and both took continuous slots; R1 `MATR` is selected cleanly by the recency rule (08-21 = 4 runs, the board's worst), R2 `IT` is an evidence-density override at 1-run recency and the cost is that RE and FIN go uncovered for a 4th run running** · **uncovered=[RE(N−, 08-22 = 4 runs, `eqflow` −0.410 rank 10 with 0🟢/3🔴 AGAINST a price median `exc5` +2.782 = 2.1× its mean — `C5` unresolved, and the measured rate beta −0.0072 means the UW rests on flow not on rates), FIN(N, 08-22 = 4 runs, `eqflow` −0.194 rank 7 with 2🟢/10🔴 and 17 of 47 negative, AGAINST price +2.662 whose mean/median sign split CLOSED this run — `NDAQ`/`MET` held), DISC(N, 08-23, **0🟢/8🔴 of 28 with breadth 0.00 against 24 of 28 positive on price** — the board's widest single `C5` contradiction and it has had no live bracket since `S91` VOIDed), STPL(N — **demoted today**, 08-24, and the demotion's own contradiction is the mandate: BEST price sector on the board (+5.048, 17/19 positive) at rank 8 of 11 on `eqflow`; Canada's 09-08 retaliation list names **dairy and agricultural goods** and `ADM` is that leg's name with NO bracket — `D342`'s unbracketed half), COMM(N, 08-24, un-measurable by rule — `D297` 6th run, `T` orphan at 9.74% of real invested for an 8th run), INDU(UW−, 08-22 = 4 runs, `P93` settles 08-28 ELEVEN DAYS before the 09-08 effective date (`D342`), `AA`/`X`/`WY` untaggable (`D341`), 18🔴 of 50), UTIL(UW−, 08-23, `eqflow` −0.616 worst on board for a 4th run and `exc20` −8.401 — but EVENT_ALPHA Card 4 flags the board's TWO LARGEST positive deltas (`GEV` +0.440, `CEG` +0.300) sitting inside it, against `OKLO` −5.70% and `OKLO`/`NRG` both outside the universe)]**

---

## ✅ EXIT CHECK
- [x] **§1 is ONE line**, inheriting MACRO §E verbatim. No unchanged sector has a row or a paragraph.
- [x] **Every §2 delta cites an absolute flow number and its rank** (`eqflow` −0.217 rank 8 · −0.165
      rank 6, with 🟢/🔴 and breadth). **No delta is argued from a macro thesis**; the two attempts that
      would have required one (RE on rates, IT on the print) are declined and logged as such.
- [x] 🚨 **No promotion or demotion rests on a `top1_flips_sign` bucket.** HLTH's attempted demotion is
      declined BY RULE with *"this sector's flow sign is `LLY` at 19.4%"* written out; COMM is declined
      by `D297` on the same principle despite a `false` flag. **The full flip list is reproduced**
      (1 of 11 TRUE, 10 false) including the fact that it **changed** from the last three runs.
- [x] **Axis count stated** (`n_axes = 3`, `vel_coverage` 0.1706). **No delta cites theme freshness or
      news velocity**, and Δ is not used as an argument anywhere because of `D355`'s bar-regime change.
- [x] Every matrix×flow divergence named with a resolution owner: ENRG→C1, HLTH→C2, MATR→R1, IT→R2;
      RE/FIN/DISC/STPL/COMM/INDU/UTIL → **named in DEEP_LOG with last-covered date and mandate**.
- [x] **N = 4/4 by the rule** — continuity stated for both continuous slots, recency-starved deviation
      declared for both rotating slots, the R2 evidence-density override and **its cost** stated.
      **No padding with Neutral/UW to reach N.**
- [x] `DEEP_LOG` line appended for the next run's recency rule.
