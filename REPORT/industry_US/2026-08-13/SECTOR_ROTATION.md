# SECTOR_ROTATION — industry_US · 2026-08-13 · Stage 6/11 (L1·ROTATION)

> **Delta-only.** MACRO owns the 11-sector verdict; `SECTOR_FLOW_US.json` owns the flow numbers.
> Both are on disk. This file writes **only what changes and why.** Analytical only, zero buy/sell (P4).

## §0 · The axis count this run scored on — read before any number below

`SECTOR_FLOW_US.json §scoring`: **`n_axes` 3 · `vel_coverage` 0.170 · `scored` 300 ·
`dropped_missing_axis` 0.** ⇒ **No delta below cites theme freshness or news velocity.** None does.

★ **Two constraints are LIFTED this run and they are why a delta is legitimate:**
1. **Δ is valid AND one-session-clean.** Baseline `history.json["2026-08-11"]`, same mode
   (`nonews`/3-axis), **300/300 names carry a Δ** (PREFLIGHT G2 **PASS**). Unlike 08-12's 2-session Δ
   and 08-13-KR's 4-calendar-day Δ, **"Δ vs the prior session" is literally true today.**
2. **The price bar is new and settled** — 2026-08-12, last-bar volume **0.740×** the 20d average,
   benchmark `SPY` carrying the same terminal date (PREFLIGHT G0 **PASS**). The S1 objection that
   forced zero deltas on 08-10 does not hold.

🚨 **Flip list, reproduced in full even where it changes nothing** (`top1_flips_sign`) — **2 of 11**:

| Sector | wflow | ex-top1 | top1 | top1_w | n |
|---|---|---|---|---|---|
| **Industrials** | **−0.002** | **+0.055** | `CAT` Caterpillar | 8.7% | 50 |
| **Materials** | **−0.106** | **+0.115** | `LIN` Linde | 24.7% | 12 |

**No verdict below rests on the `wflow` of either.**
✅ **Financials came OFF the flip list this run** (it was on it 08-12 at BRK-B 13.9%) ⇒ its `wflow`
is admissible again — and it reads **−0.011**, i.e. ≈zero.
⚠ `top1_w` weights come from a **29-day-old** market-cap file (PREFLIGHT G5).

## §1 · Inherited — one line, verbatim

**MACRO holds:** `INDU OW− · ENRG OW− · FIN N · IT N · HLTH N+ · DISC N · MATR N− · COMM UW ·
UTIL UW · STPL UW− · RE UW`.

## §2 · Deltas — **ONE**, and it is carried entirely by non-cap-weighted numbers

| Sector | matrix said | flow evidence (Δ = 1 session, 08-11→08-12) | new verdict | who resolves |
|---|---|---|---|---|
| **Consumer Discretionary** | **N** | **eqflow −0.063 (negative)** · **Δ −0.194 = the worst on the board** · **1🟢 vs 8🔴 of 28** · breadth **0.04** · **9 of 28 at the `OBV 매집 ∧ RS20>0` pre-condition (32%, 5th of 11)** · **not a flipper**, so `wflow −0.374` is admissible and agrees | ★ **N−** | **not deep-dived this run — see §3** |

### 2a · Why this delta is legal and the one that failed last run is not

08-12 declined a DISC change with *"cap and breadth disagree in sign (C3: no signal, not a neutral
verdict)"* — `wflow −0.180` against `eqflow +0.010`. **That disagreement has resolved, and it resolved
downward**: `eqflow` has gone **+0.010 → −0.063** in one settled session. ⇒ **the C3 objection that
blocked the notch is gone on its own terms**, and the demote now rests on **eqflow, Δ, and the
green/red count — all non-cap-weighted.**

⚠ **The AMZN concentration is stated rather than used**: `wflow −0.374` vs `eqflow −0.063` is a
**0.311 gap** owned by AMZN at ~40% of sector cap. **DISC is not on the flip list**, so `wflow` is
technically admissible — **but the notch is not carried by it.** Remove AMZN entirely and `eqflow`
still says the same thing.

⚠ **Corroborating and independent of the sweep**: `XLY` is **negative on all four price windows vs
SPY** — exc1 **−1.38** · exc5 −0.98 · exc20 −1.58 · exc60 −3.34 (MACRO §G). **On 08-12 it was the
second-worst sector on the day.**
⚠ **S1**: Δ is one session. **The notch is ONE step (N → N−), not two**, for exactly that reason.

## §2b · Changes CONSIDERED and DECLINED — with the numbers, not with silence

**Six attempts. All declined. Each says which axis refused it.**

| Attempt | Why it was on the table | Why DECLINED |
|---|---|---|
| ★★ **IT N → N+** | **MACRO §G handed this stage a promotion argument**: `XLK` positive on **all four** price windows, **exc1 +1.24 = best sector on the CPI session**, FINRA **z −1.91 🟢 covering** | 🚨 **The flow axis refuses it and IT is NOT a flipper, so its `wflow` is admissible and NEGATIVE: −0.136, with `eqflow −0.100` also negative.** IT holds **the most 🟢 of any sector (6) AND the most 🔴 (19 of 56)** — **it is not one object.** ⚠⚠ And **EVENT_ALPHA Card 4 is direct counter-evidence**: five of six names in the memory sub-chain are distributing (`MU` OBV −0.161 · `AMAT` −0.108 · `LRCX` −0.179 · `KLAC` −0.139 · `WDC` −0.112), all with a positive RS60 and a negative RS20 — **M149's decaying-stock shape across a whole value chain.** ★ Third objection, from positioning: **Nasdaq-100 spec sits at the 0th percentile short** ⇒ a one-session tech bid into a record short is squeeze-shaped, not demand-shaped. **A promotion whose only support is price, against negative flow on both axes and a distributing sub-chain, is exactly the (a)-class divergence this stage is told to resolve DOWN, not up.** → **DEEP-IT owns it** |
| ★ **ENRG OW− → OW** | **Rank 1 on BOTH flow axes** (`wflow +0.416 · eqflow +0.242`), **Δ +0.056**, **no flipper** (XOM 30.5%, ex-top1 +0.316), **8 of 16 at the pre-condition**, `XLE` exc5 **+6.14** and exc20 **+5.68** both best of 11, and **EVENT_ALPHA Card 1 confirms it bottom-up** on a mechanism (refining-capacity destruction) that is independent of the sweep | ⛔ **Declined on TIMING, and the reason is registered rather than felt: `S67` — the falsifier for this desk's OWN 08-12 ENRG promotion — settles at TONIGHT'S CLOSE, in hours.** Moving the tilt again on the day its bracket settles **destroys the information the bracket was registered to buy** and would be the third ENRG verdict in three runs on a number that has already reversed sign once (`R51`). ⚠ Two further numbers argue for patience, not against the sector: **`XLE` exc60 is −1.83 (the 60-day has not turned)** and EVENT_ALPHA measured the headline refiners' money as **60 days old** (MPC RS60 +32.0 · VLO +27.2 · PSX +23.5). **The OW− stands; the promotion case is handed to the next run WITH S67's verdict in hand** |
| **STPL UW− → UW** | **Δ +0.120 is the LARGEST positive Δ on the entire board**, from the second-lowest tilt | ⛔ **Levels did not move and they are what the tilt is about**: `wflow −0.103 · eqflow −0.130 · breadth 0.00 · 3 of 19 at the pre-condition · XLP exc60 −3.99`. **A one-session Δ against unchanged negative levels is S1, not a turn.** Logged so the next run can see it was seen — **if the Δ persists a second session this becomes a real notch** |
| **UTIL UW → UW−** | Worst levels on every flow axis (`wflow −0.399 · eqflow −0.392 · 8🔴 of 15 · breadth 0.00`) **and 0 of 15 at the pre-condition — the only REAL absence on the board** (SWEEP §3) | ⛔ **Redundant, and contradicted on the change axis**: **Δ +0.077 is the 3rd-largest positive on the board.** Declined for the same reason as 08-12 — **a deepen on an unchanged floor is not information** — with one addition: **`S71` settles on `XLU`'s own 08-13 bar tonight**, so this sector's next verdict has a dated instrument arriving in hours |
| **MATR N− → N** | 🚨 **SWEEP §2 handed this stage a genuine contradiction**: **6 of 12 Materials names sit at `OBV 매집 ∧ RS20>0` — a 50% rate, 2nd-highest on the board** — and `eqflow −0.029` is far less negative than `wflow −0.106` | ⛔ **Two blocks.** (i) 🚨 **G3: `LIN` at 24.7% flips the sign** (wflow −0.106 → ex-top1 **+0.115**) ⇒ **no promotion may rest on this bucket's `wflow`.** (ii) The permitted axes refuse it anyway: **`eqflow` is still negative, `breadth` is 0.00, `Δ −0.037` is negative**, and **`XLB` exc5 collapsed +2.484 (08-11) → −0.465 (08-12)** while **`NEM`'s own exc5 is +12.642** ⇒ the sector's price is one name. ★ **The contradiction is REAL and is not resolved here — it is the #1 DEEP question** (§3) |
| **COMM UW → UW−** | `wflow −0.708` is the worst on the board; `XLC` exc60 **−9.51**, the worst long window of 11 | ⛔ 🚨 **`R56` binds and the contamination got WORSE this run, not merely older.** `EA` went private 2026-08-04/05, is **still in `us_top300.csv` on day 29**, and has now progressed to: a **null 08-12 close** (PREFLIGHT G5) → a **🟢가속 tag with OBV +0.74** → a **top-15 `US_LIVE_SHORTLIST` slot** → **one of only five `new_green` ignitions on the board.** ⇒ **any COMM breadth or ignition number contains a non-trading security.** ⚠ COMM is **not** on the flip list, so `wflow` is technically admissible — **it is declined on the delisted-constituent contamination instead**, which is the stronger objection. **6th consecutive run** |

⚠ **One hold whose BASIS changed, recorded because a hold on new evidence is not the same object as a
hold on inertia**: **INDU OW−.** MACRO called it *"the weakest overweight on the board"* on price
(exc5 −0.60). **EVENT_ALPHA Card 5 supplies a non-cap-weighted counterweight this stage may use**:
`GD` OBV **+0.414** · `LMT` +0.377 · `NOC` +0.347 · `RTX` +0.303 · `LHX` +0.204 — **five defense names
all accumulating, none tagged 🟢 because all five are blocked by `vol_surge < 1.2` alone.** With
`eqflow +0.049` (**one of only three positive eqflows on the board**) and **22 of 50 at the
pre-condition — the highest COUNT of any sector** — **the OW− is held on breadth, not on price.**
🚨 `wflow` remains inadmissible here (**flipper `CAT`**), and no number above is cap-weighted.

## §3 · DEEP picks — **N = 4** (protocol DEEP budget: 2 continuous + 2 rotating, unchanged 2026-07-31)

| Slot | Sector | Why |
|---|---|---|
| **Continuous 1** | **ENRG (OW−)** | ★ **Anti-thrash APPLIED and stated**: ENRG held a continuous slot on **2026-08-12** and is **still a top-N OW today** (rank 1 on both flow axes) ⇒ it **KEEPS** the slot by the rule. **DEEP-ENRG's first question is the one this stage declined: does the promotion case survive `S67`'s settle tonight, and is the driver refining-capacity destruction (EVENT_ALPHA Card 1) or war premium (`S55` still C, `R47` still binding)?** |
| **Continuous 2** | **INDU (OW−)** | ★ **Anti-thrash APPLIED**: continuous on 08-12, still a top-N OW ⇒ **KEEPS** the slot. **DEEP-INDU's first question is whether the OW− is a defense call wearing an Industrials label** — five defense names accumulating with `eqflow +0.049` while `XLI` exc5 is −0.60 and `CAT` makes the sector a flipper |
| **Rotating 1** | ★★ **MATR (N−)** | **Pre-committed by the previous run**: `DEEP_LOG 2026-08-12` wrote *"★next run's first rotating pick if the flow axis turns."* **The flow axis did not turn — it produced a contradiction instead**, and that is sharper: **50% of the sector at the accumulation pre-condition against a price that is one name (NEM exc5 +12.642 vs XLB exc5 −0.465).** **S57 has already FIRED-A twice and the N− was carried anyway**; `S77` is its replacement falsifier, settling 08-19. **DEEP-MATR must resolve which window is right, not pick one** |
| **Rotating 2** | ★★ **IT (N)** | **Three stages of this run disagree about it and none can settle it**: MACRO argues promotion from price, SWEEP refuses on both flow axes and finds IT is simultaneously the board's biggest accumulator (6🟢) and biggest distributor (19🔴), EVENT_ALPHA finds the memory sub-chain distributing across five of six names. **Last covered 2026-08-10 (2 runs).** ⚠ **`P43`'s CXMT/Apple supply axis has now been carried UNREFRESHED for four runs — DEEP-IT must actually pull the filing**, since the news axis is available (MACRO §0) and the last three runs' excuse is gone |

⚠⚠ **Rotating slot selection is a DECLARED recency-starved deviation, for the second consecutive
run.** The rule asks for *"the next-highest OW not deep-dived in the last ~3 runs."* **The board holds
exactly two OW sectors (ENRG, INDU) and both are on the continuous track**, and the single N+ (HLTH)
was covered **yesterday**. ⇒ **there is no third OW to rotate to.** Both rotating slots are therefore
taken from **N/N− sectors chosen by open-question sharpness**, and that choice is stated rather than
presented as the rule's output.

**No padding.** Four slots, four real questions.

## DEEP_LOG 2026-08-13: continuous=[ENRG, INDU] rotating=[MATR, IT] · N=4/4 · **ONE verdict delta (DISC N→N−), carried by eqflow −0.063 + Δ −0.194 (worst on board) + 1🟢/8🔴, with the AMZN 0.311 cap-gap stated but NOT used — and it is legal precisely because 08-12's C3 blocker resolved on its own terms (eqflow +0.010 → −0.063 in one settled session)** · **Δ is ONE settled session (08-11→08-12) against a same-mode 3-axis baseline, 300/300 names — the cleanest Δ this desk has had in a week (PREFLIGHT G0+G2 both PASS)** · **SIX attempts declined with numbers: IT N→N+ (MACRO's own promotion argument REFUSED — wflow −0.136 AND eqflow −0.100 both negative on a NON-flipper, 6🟢 vs 19🔴 = biggest accumulator and biggest distributor simultaneously, EVENT_ALPHA Card 4's memory chain distributing 5-of-6, Nasdaq-100 spec at the 0th percentile short), ENRG OW−→OW (declined on TIMING — S67, the falsifier for this desk's own 08-12 promotion, settles tonight; also exc60 −1.83 and headline refiner money 60 days old at RS60 +32/+27/+23), STPL UW−→UW (largest positive Δ on the board at +0.120 but levels unchanged and negative — S1), UTIL UW→UW− (redundant on an unchanged floor; Δ +0.077 points the other way; S71 settles on XLU tonight), MATR N−→N (G3 flipper LIN 24.7% blocks wflow; eqflow/breadth/Δ all refuse anyway — but the 6-of-12 pre-condition contradiction is REAL and becomes rotating pick 1), COMM UW→UW− (R56 — EA delisted, still in us_top300 at day 29, and now carrying a 🟢 tag, OBV +0.74, a top-15 shortlist slot and a new_green flag; 6th run))** · **flip list 2 of 11 — Industrials/CAT/8.7% · Materials/LIN/24.7% — no verdict rests on either wflow; Financials came OFF the list** · **INDU's HOLD was re-based from price to breadth (5 defense names accumulating at OBV +0.414/+0.377/+0.347/+0.303/+0.204, all hidden by the vol_surge<1.2 filter; eqflow +0.049; 22/50 at the pre-condition = highest count of 11)** · **anti-thrash APPLIED to both continuous slots (ENRG and INDU each continuous on 08-12 and still top-N OW)** · **rotating slots are a DECLARED recency-starved deviation for a 2nd run — no third OW exists on a board holding exactly two** · uncovered=[**HLTH(N+, covered 08-12 = 1 run; rank 2 on both flow axes with the tightest cap-vs-equal gap of 11 at 0.011 and XLV exc60 +11.58 = board's best, BUT Δ has gone +0.157→−0.014 ⇒ deceleration flag; 19/32 at the pre-condition = highest RATE on the board while breadth reads 0.00 = M144's 7th replication; S76's two legs settle 08-19)**, **FIN(N, covered 08-08 = 3 runs; came OFF the flip list so wflow −0.011 is admissible again and reads ≈zero; eqflow −0.065 negative with 11🔴 of 47, BUT EVENT_ALPHA Card 2 finds JPM OBV +0.394 / BAC +0.332 new_green / PRU +0.283 all accumulating and 2s10s steepened a 3rd consecutive print to +0.48 ⇒ S51's NIM mechanism is extending while the sector's breadth is not; S78 settles 08-19)**, **COMM(UW, covered 08-07 = 5 runs; ★the telecom node T/VZ/CMCSA un-owned for a 5th run; R56 blocks the aggregate and the contamination has now reached the shortlist)**, **DISC(N−, DEMOTED TODAY, covered 08-03 = 7 runs — the longest gap on the board, and unlike 08-12 the gap is now an information gap because the C3 no-signal reading has resolved into a signal)**, STPL(UW−, covered 08-10; Δ +0.120 = largest positive on the board on unchanged levels — first thing to check next run), UTIL(UW, covered 08-12; 0/15 at the pre-condition = the board's only REAL absence, second run running; S71 settles tonight), RE(UW, covered 08-04 = 6 runs; wflow −0.172/eqflow −0.151/breadth 0.00 all agree, XLRE exc5 −1.92 — the most internally consistent verdict on the board, which is why it does not need a slot; ⚠ its one contrary axis is FINRA z −1.94 covering, a positioning axis not a demand axis (D6))]

---

**Linter**: `python -X utf8 scripts/report_lint.py llm_outputs/2026-08-13/industry_US/SECTOR_ROTATION.md`
→ **`✅ SECTOR_ROTATION.md` · 총 0건** (C1 · C2 · S6 · D6). ⚠ Form only — it cannot see whether the
DISC notch is *right*, only that its benchmark is named. The place this stage would break first is
**§2a's claim that the C3 blocker "resolved on its own terms"**: that rests on a **one-session**
eqflow sign change (+0.010 → −0.063), and if the next session reverses it, the notch was S1 noise.
