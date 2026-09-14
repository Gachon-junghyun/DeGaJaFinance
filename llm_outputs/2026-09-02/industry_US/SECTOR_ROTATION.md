# SECTOR_ROTATION — industry_US · 2026-09-02 (Wed) · Stage 6 / L1·ROTATION

> **Delta-only.** MACRO §E owns the 11-sector matrix and `SECTOR_FLOW_US_REPAIRED.json` owns the flow
> numbers; both are on disk all run. This file writes **only what changes and why**, plus the DEEP picks.

## 🚨 Instrument state governing every delta below
`SECTOR_FLOW_US_REPAIRED.json §scoring`: **`n_axes` 3 · `vel_coverage` 0.0 · `scored` 298 ·
`dropped_missing_axis` 0 · `mode` nonews · asof 2026-09-01.** Primary file's `vel_coverage` **17.11%**.
⇒ **ZERO deltas below cite theme freshness or news velocity.** Δ is legal this run — the prior
same-mode snapshot is **2026-08-31** (`nonews`, n=299, 298 common) — so every Δ carries the label
**`repaired sweep, 08-31 → 09-01, ONE session`**, and per PREFLIGHT G2 it is used as a **direction,
not a magnitude** (the baseline is yesterday's holed-OBV primary).
🚫 Primary `SECTOR_FLOW_US.json` OBV/flow/Δ revoked (PREFLIGHT G0).

## §1 · Inherited — one line, verbatim from MACRO §E

`MACRO holds: ENRG OW · HLTH OW− · MATR N(contested) · IT N · STPL N · FIN N · RE UW · DISC UW ·
UTIL UW · INDU UW · COMM no-verdict(barred)`

⚠ **Stage-boundary irregularity, logged not hidden.** The inherited verdict entering today was
**`MATR OW`** (09-01 DEEP_LOG). **MACRO §E printed it as `N, contested`** — i.e. a verdict change was
made one stage early, in the stage that is supposed to set wind direction rather than issue verdicts.
It is **re-derived under ROTATION's discipline in §2 (delta 1)** rather than accepted or reverted on
authority. Registered as **`D476`**.

## §2 · Deltas — 3 changes of 11 attempts

**Flip list reproduced in full even where it changes nothing** (a silent flipper is how one company
becomes a sector call):

| file | `top1_flips_sign` buckets |
|---|---|
| **repaired (citable)** | **1 of 11** — Consumer Discretionary / `AMZN` **40.2%** (−0.286 → +0.033) |
| primary | **2 of 11** — adds Consumer Staples / `WMT` **28.9%** |
| ★ neither file sees | **Communication Services** — Alphabet **76.6%** under **two** tickers; prints `False`; ex-both-classes `wflow` **−0.506 → +0.257** (`D459`) |

★ **`C26` update — its Financials leg is RESOLVED and a new leg opens.** On 09-01 the two files
disagreed about **Financials** (primary flipped it on `BRK-B` by a 0.004 margin, repaired did not).
Today **both files agree Financials is a non-flipper**, and the disagreement has moved to
**Consumer Staples**. ⇒ the contradiction is not closed, but the name it attaches to changed, which is
itself evidence that the disagreement is **instrument noise at small margins**, not a property of any
one sector.

### Delta 1 — **`MATR` OW → N** (re-derived here; the change itself was made at MACRO)

| flow evidence (all non-cap-weighted, `repaired sweep, 08-31 → 09-01`) | |
|---|---|
| Δ | **−0.208 — the board's 2nd-worst** (only `INDU` −0.222 is lower) |
| `eqflow` | **−0.076, rank 4 of 11 but negative**, having been positive (+0.030) on 09-01 |
| breadth | 0.08 · **1 green of 12 · 4 reds** |
| flipper? | **No** — `LIN` 24.7%, `wflow` +0.061 → ex-top1 **+0.016** ⇒ the top-1 **holds it up** (a `D424` mirror case), so removing it does not rescue the bucket |

**Verdict: N. The delta stands.** Three admissible numbers, all non-cap-weighted, on a non-flipper.
⚠ **What is NOT used**: `NEM` turning 🟢 (it crossed a `vol_surge` gate it missed **by 0.01**
yesterday — `C5`), and `C24`'s copper spec at the **100th percentile** `[COT 08-25]`, which is
positioning context and, at 3–4 days' lag, cannot see 08-31 or 09-01. **`C24` reproduces a 4th time
and is carried, not resolved.**

### Delta 2 — **`FIN` N → UW**

| flow evidence | |
|---|---|
| `eqflow` | **−0.220, rank 7** — **worse than 09-01's −0.186** |
| Δ | **−0.220, the board's 3rd-worst** — against 09-01's −0.047 |
| breadth | **0.00** · **0 greens of 47 for a 3rd consecutive run** · **14 reds** |
| flipper? | **No, in both files today** — `BRK-B` 13.9%, `wflow` −0.260 → ex-top1 **−0.240** (removing the top name barely moves it) |

**Verdict: UW.** ⚠ **This is a second demotion in two runs** (`OW− → N` on 09-01), which is thrash
unless the numbers moved — **and they did, on both admissible axes** (`eqflow` −0.186 → −0.220;
Δ −0.047 → −0.220). The move is made on **new numbers, not on a restated argument**.
⚠ **What is NOT used**: `hy_oas` at the **0.4th percentile of 252** is the strongest thing available
in favour of this bucket, and it is a **macro re-argument** — declined as evidence here and left to
`P128` (settles 09-08) and `S134` (09-04), which bracket exactly this.

### Delta 3 — **`HLTH` OW− → OW**

| flow evidence | |
|---|---|
| `eqflow` | **+0.265, rank 2 of 11** — one of only **two** positive `eqflow` readings on the board |
| Δ | **+0.214, rank 3** |
| breadth / tags | 0.06 · **2 of the universe's 6 greens** (`A` +0.828, `MDT` +0.774) · 3 reds of 32 |
| flipper? | **No, and it has no top-1 dependence at all** — `LLY` 19.4%, `wflow` +0.279 → ex-top1 **+0.279**, identical to three decimals. **The `D424` gap that was open on this sector for four runs (+0.021 vs +0.095 on 08-30, +0.069 vs +0.115 on 09-01) has closed to zero** |

**Verdict: OW.** ⚠ **What is NOT used**: `XLV` exc5 **−1.53 vs `SPY`** (a return measure, MACRO's
object, not this stage's) and the two dated negatives in MACRO §B-2 (MFN pricing extended to 9
mid-sized drugmakers; the Novartis trial halt) — **both are macro re-arguments and are declined as
evidence for or against here.** They are handed to the DEEP mandate instead.

### Declines — 8 attempts, each with its number

| sector | attempted | declined because |
|---|---|---|
| **UTIL** | UW → N | 🚩 **The two admissible numbers disagree, and the disagreement is unusually wide**: Δ **+0.267 = the board's 2nd-best** against `eqflow` **−0.223, rank 8**, breadth **0.00**, 0 greens of 15. Precedent (`FIN`, 08-31): *state the disagreement, do not pick a side*. **4th consecutive decline on a 4th distinct reason** (method → newness → Δ-direction → **axis disagreement**). ⚠ EVENT_ALPHA Card 4's Texas "ghost demand" halt is a **macro re-argument** and was NOT used. **If Δ and `eqflow` agree next run, the move is made.** |
| **IT** | N → UW | Three numbers support it — `eqflow` **−0.252, rank 10 of 11**, breadth **0.02 (1 green of 55)**, **23 reds**, Δ −0.173, non-flipper (`NVDA` 19.5%, ex-top1 −0.154, sign held). 🚩 **Declined anyway, and the reason is a measured contradiction, not caution**: the desk has **two breadth measurements of the same sector over nearly the same window pointing opposite ways** — flow-breadth **1 of 55** against `S124`'s settled return-breadth **41 of 56** (`FIRED-A`, 08-31). `M1184`/`M1208` already explain the gap — it is **entirely `vol_surge`** — and `D395`/`D428` bar this desk from using the only IC measurement of that axis (`market=kr`, `W1`). **Demoting on the axis the desk cannot score would be picking a side of its own open contradiction.** ⇒ **routed to PREMORTEM for a 4th consecutive run**, with `S140` (09-08) bracketing exactly this. |
| **RE** | UW → UW− | Δ **+0.178, the board's 4th-best** — wrong direction for a demotion. `eqflow` −0.194 rank 6. **Numbers disagree; declined** |
| **DISC** | UW → UW− | 🚨**1名**: `AMZN` **40.2%**, and the bucket **flips sign** without it (−0.286 → **+0.033**). **Barred by rule.** ⚠ The FTC/22-state ad-auction suit (13 outlets) landed on that same 40.2% name — EVENT_ALPHA filed it explicitly as a **name-level** card so it could not be laundered into a sector call, and it is not used here |
| **STPL** | N → UW | 🚨 **the two instruments disagree about whether this bucket is a flipper** (primary: `WMT` 28.9% flips; repaired: does not) ⇒ PREFLIGHT G3 bars a `wflow` verdict, and `eqflow` −0.086 rank 5 with Δ **+0.060** point opposite ways. **Barred and disagreeing — declined twice over** |
| **COMM** | any | **Barred entirely.** `wflow` is one company held under two tickers (`D459`, 2nd reproduction, swing **0.763**); `eqflow` **−0.013** is flat and carries no verdict either way. **14th consecutive run this bucket is un-measurable by rule** |
| **INDU** | UW− → lower | **No notch below UW− exists.** The numbers deepened again — `eqflow` **−0.447 (worst)**, Δ **−0.222 (worst)**, **31 reds of 50 = the board's most**, breadth 0.00 — and are recorded rather than converted into a verdict |
| **ENRG** | OW → OW+ | **No notch above OW exists.** `eqflow` **+0.551**, Δ **+0.295**, breadth **0.12** — all board-best; recorded, not converted |

★ **The structural line of this board:** **`eqflow` is positive in exactly 2 of 11 sectors** (Energy
+0.551, Health Care +0.265) — down from 3 on 09-01 and 4 on 08-31 — while **6 of 11 carry a positive
Δ**. ⇒ **levels are narrowing and changes are broadening at the same time**, which is why five of
today's eight declines are "the two axes disagree" rather than "the number is small".

## §3 · DEEP picks + DEEP_LOG

**Recency read from DEEP FILES ON DISK** (not from `DEEP_LOG` prose), runs 08-24 → 09-01:
`ENRG` 0 · `HLTH` 0 · `MATR` 0 · `COMM` 0 · `IT` 0 · `INDU` 1 · `FIN` 2 · `STPL` 4 · `DISC` 4 ·
`RE` 5 · **`UTIL` 8 — the longest gap on the board for a 4th consecutive run.**

**Protocol DEEP budget: N = 4 (2 continuous + 2 rotating).**

| track | sector | rule applied |
|---|---|---|
| **continuous 1** | **`ENRG`** | today's **top OW by every admissible number** (`eqflow` +0.551, Δ +0.295, breadth 0.12 — all rank 1) |
| **continuous 2** | **`HLTH`** | **anti-thrash KEEP**: held a continuous slot on 09-01 **and** is still a top-N OW today (promoted to OW in §2 delta 3) |
| **rotating 1** | — | **UNFILLED** |
| **rotating 2** | — | **UNFILLED** |

🚫 **N = 2 of 4 filled, and the two empty slots are deliberate.** The rotating track takes the
*next-highest OW not deep-dived in ~3 runs*, and **after `ENRG` and `HLTH` there is no third OW sector
on the board** — `MATR` was demoted to N by delta 1 and everything else is N or below.
**Padding with Neutral/UW is forbidden by the selection rule, and fewer is fine if stated.** It is
stated here.
⚠ `MATR` and `COMM` — the two rotating slots of 09-01 — **lose their slots for opposite reasons**:
`MATR` because it is no longer OW, `COMM` because it is barred from carrying a verdict at all.

★ **The two unfilled slots are explicitly offered to PREMORTEM's promotion mechanism**, which is how
`IT` got its 5th slot on 09-01. The two candidates, with their reasons stated so PREMORTEM does not
have to re-derive them:
1. **`IT`** — declined in §2 on a **measured contradiction between two breadth measurements** (flow
   1/55 vs return 41/56) that this stage is barred from resolving. **4th consecutive routing.** It is
   also the book's largest concentration (`NVDA` 21.3% + `ANET` 14.6% = **35.9%** of real invested
   capital) and `AVGO` prints **tonight**.
2. **`UTIL`** — declined in §2 on an axis disagreement, carries the board's **2nd-best Δ and 2nd-best
   exc1** against its rank-8 `eqflow`, has an **8-run recency gap**, and is the sector EVENT_ALPHA
   Card 4 supplies a **named, dated falsifier** for. **UW sectors cannot take a DEEP slot by rule, so
   PREMORTEM is the only path to it** — 4th consecutive run in which the board's most contested
   sector is structurally unreachable by the selection rule.

## DEEP_LOG 2026-09-02: continuous=[ENRG, HLTH] rotating=[] · **N=2/4 filled — the 2 rotating slots are UNFILLED because only 2 OW sectors exist on the board and padding with N/UW is forbidden; both empty slots are offered to PREMORTEM promotion with named candidates (IT, UTIL) and reasons** · **OW sectors WITHOUT a slot: none — both OW sectors got one** · **verdict deltas 3 of 11 attempts: `MATR OW→N` (re-derived here after being made one stage early at MACRO — `D476`; carried by Δ −0.208 = 2nd-worst, `eqflow` −0.076 turned negative from +0.030, 1🟢/4🔴 of 12, non-flipper where the top-1 HOLDS IT UP: `LIN` 24.7%, +0.061 → ex-top1 +0.016), `FIN N→UW` (2nd demotion in 2 runs but on NEW numbers on both axes — `eqflow` −0.186 → −0.220, Δ −0.047 → −0.220, 0 greens of 47 for a 3rd run, 14 reds, non-flipper in BOTH files today), `HLTH OW−→OW` (`eqflow` +0.265 rank 2 = one of only two positive readings on the board, Δ +0.214 rank 3, 2 of the universe's 6 greens, and ★ the `D424` gap on this sector CLOSED TO ZERO: `wflow` +0.279 vs ex-`LLY` +0.279, from +0.069/+0.115 on 09-01)** · **8 declines each with its number: `UTIL UW→N` (Δ +0.267 = 2nd-best vs `eqflow` −0.223 rank 8 and 0🟢/15 — the two admissible axes DISAGREE; 4th consecutive decline on a 4th DISTINCT reason: method → newness → Δ-direction → axis disagreement; the Texas ghost-demand halt is a macro re-argument and was NOT used), `IT N→UW` (three numbers support it — `eqflow` −0.252 rank 10/11, breadth 0.02 = 1🟢 of 55, 23🔴, Δ −0.173, non-flipper — but DECLINED on a measured contradiction: flow-breadth 1/55 against `S124`'s settled RETURN-breadth 41/56, a gap `M1184`/`M1208` already attribute entirely to `vol_surge`, the one axis `D395`/`D428` bar this desk from scoring (`W1`); routed to PREMORTEM 4th consecutive run, `S140` settles 09-08), `RE UW→UW−` (Δ +0.178 = 4th-best, wrong direction), `DISC UW→UW−` (🚨1名 `AMZN` 40.2%, flips −0.286 → +0.033), `STPL N→UW` (the two files DISAGREE on whether `WMT` 28.9% flips it ⇒ G3 bar, AND `eqflow` −0.086 vs Δ +0.060 disagree — declined twice over), `COMM` any (barred, `D459` 2nd reproduction with the swing GROWN to 0.763 from 0.691; `eqflow` −0.013 flat; 14th run un-measurable by rule), `INDU UW−→lower` (no notch; numbers deepened to `eqflow` −0.447 worst, Δ −0.222 worst, 31 reds of 50 = board's most), `ENRG OW→OW+` (no notch; all three numbers board-best)** · **flip list: repaired 1 of 11 (DISC/`AMZN` 40.2%), primary 2 of 11 (adds STPL/`WMT` 28.9%) — ★ `C26`'s FINANCIALS leg is RESOLVED (both files now agree FIN is a non-flipper) and a new STAPLES leg opened, which is evidence the disagreement is instrument noise at small margins rather than a sector property** · 🚨 **instrument state: 08-28 is now a FROZEN hole (259 of 301 NaN at T+5, identical set to T+4, zero backfill in 24h) ⇒ the primary file's OBV axis is revoked and every number above is `SECTOR_FLOW_US_REPAIRED.json` (258 names patched from the 5m endpoint; residual OBV-axis error 0.0087 mean / 0.0272 max, **1 of 42 label flips — NOT zero, corrected from yesterday's claim**; **RULE D6 exempt — this is an instrument-error measurement OF the OBV axis, not a market proposition resting ON it, and no verdict above is carried by an OBV number alone**); the head of the series held for a 2nd run (09-01 NaN 2 of 301: `EA`, `APH`) and the sweep scored 298/298** · **`n_axes` 3, `vel_coverage` 0.0 (repaired) / 17.11% (primary) ⇒ ZERO deltas cite velocity or freshness; Δ IS legal (prior same-mode snapshot 08-31 `nonews`) and every Δ is labelled `repaired sweep, 08-31 → 09-01, ONE session` and used as DIRECTION ONLY because the baseline is yesterday's holed primary (PREFLIGHT G2)** · ★★ **the structural line: `eqflow` is positive in exactly 2 of 11 sectors (ENRG +0.551, HLTH +0.265), down from 3 and 4 in the two prior runs, while 6 of 11 carry a positive Δ — levels narrowing and changes broadening at once, which is why 5 of 8 declines are "the two axes disagree" rather than "the number is small"** · **uncovered=[IT(N, 09-01 = 0 runs, routed to PREMORTEM 4th consecutive run, the book's largest concentration at 35.9% of real invested capital, `AVGO` prints TONIGHT, `S140` settles 09-08), MATR(N — DEMOTED TODAY, 09-01 = 0 runs, `C24` copper 100th %ile carried unresolved a 4th time), COMM(no-verdict, 09-01 = 0 runs, un-measurable by rule 14th run), INDU(UW−, 08-31 = 1 run, 31 reds of 50 = board's most, bracketed 09-04 by `S126`+`P114`), FIN(UW — DEMOTED TODAY, 08-30 = 2 runs, `S134` 09-04 and `P128` 09-08 both bracket it), STPL(N, 08-27 = 4 runs, flipper status disputed between the two files), DISC(UW, 08-27 = 4 runs, 🚨1名 `AMZN` 40.2%, carries the FTC suit as a NAME-level card), RE(UW, 08-26 = 5 runs, Δ +0.178 = 4th-best, wrong direction for its verdict), UTIL(UW, 08-23 = **8 runs — the longest recency gap on the board for a 4th consecutive run**, board's 2nd-best Δ +0.267 and 2nd-best exc1 +1.47 against a rank-8 `eqflow`, NOT slotted because UW sectors do not take DEEP slots; ★ offered to PREMORTEM as one of the two unfilled slots because EVENT_ALPHA Card 4 gives it a named dated falsifier and the structural unreachability is now costing a live question for a 2nd run)]**

## ✅ EXIT CHECK
- [x] **§1 is ONE line**, inheriting MACRO §E verbatim; no unchanged sector gets a row or a restated
      number. The one irregularity (a verdict changed at MACRO) is named and re-derived, not accepted.
- [x] **Every §2 delta cites a flow number** — Δ, `eqflow`, breadth, green/red counts, `wflow_ex_top1`.
      **Three macro re-arguments were attempted and declined in writing**: `hy_oas` for `FIN`, the
      Texas halt for `UTIL`, the MFN/Novartis prints for `HLTH`.
- [x] 🚨 **No promotion or demotion rests on a `top1_flips_sign` bucket.** `DISC` barred (`AMZN`
      40.2%), `STPL` barred (the two files disagree), `COMM` barred (`D459`). **The flip list is
      reproduced for both files even though it changes nothing**, and the `C26` update is recorded.
- [x] **The axis count is stated** (`n_axes` 3, `vel_coverage` 0.0 / 17.11%). **No delta cites theme
      freshness or news velocity.** Δ is read only against a same-mode (`nonews`) snapshot, is
      labelled with its window, and is used as direction only.
- [x] Every matrix×flow divergence has a named resolution owner: `IT` → PREMORTEM + `S140`;
      `UTIL` → PREMORTEM + `S135`; `FIN` → `S134`/`P128`; `MATR`/`C24` → carried; `ENRG` barrel-vs-chain
      → `P126`/`S136`.
- [x] **N DEEP targets picked by the rule** — continuity applied (`HLTH` KEEP) and stated; **no
      padding**; the two unfilled slots are explained and offered to PREMORTEM with named candidates.
      **Every uncovered sector is named in DEEP_LOG with its recency.**
- [x] **Linter run on this stage's own output** — `python -X utf8 scripts/report_lint.py llm_outputs/2026-09-02/industry_US/SECTOR_ROTATION.md` ⇒ first pass **1 finding** (`D6`, OBV cited alone in the DEEP_LOG instrument line); **fixed by carrying the rule ID and the exemption reason in that line** (it measures the OBV axis's own error, it does not rest a verdict on OBV). Re-run ⇒ **0 findings**. ⚠ Form only; a clean run is not a correct report.
- [x] `DEEP_LOG` line appended for the next run.
