# SECTOR_ROTATION — industry_US · 2026-08-12 · Stage 6/11 (L1·ROTATION)

> Delta-only. MACRO owns the 11-sector verdict; `SECTOR_FLOW_US.json` owns the flow numbers. Both are
> on disk. This file writes **only what changes and why.** Analytical only, zero buy/sell (P4).

## §0 · The axis count this run scored on — read before any number below

`SECTOR_FLOW_US.json §scoring`: **`n_axes` 3 · `vel_coverage` 0.1133 · `scored` 300 ·
`dropped_missing_axis` 0.**

**The news axis is dead again** (11.3% coverage), so per the EXIT CHECK **no delta below cites theme
freshness or news velocity.** None does.

★ **But two constraints that bound the last three runs are LIFTED, and that is why this run can move:**
1. **Δ is valid.** The matched baseline is **2026-08-07** — same mode (`nonews`/3-axis), **299 tickers,
   100% ticker overlap, 299/300 names carrying a Δ** (PREFLIGHT G2 **PASS**). `D232`'s 5-ticker
   18-day-old baseline does **not** apply. **Every Δ below is a 2-SESSION change (08-07 → 08-11), never
   "today."**
2. **Levels are comparable to 08-10 for the first time**, because **both runs are 3-axis `nonews`** —
   unlike the 08-08→08-10 sequence where the mode changed under an identical price bar. **And the price
   bar itself is new: two settled sessions (08-10, 08-11).** ⇒ the S1 objection that made zero-delta the
   correct output on 08-10 **does not hold today**.

🚨 **Flip list, reproduced in full even where it changes nothing** (`top1_flips_sign`) — **3 of 11**:

| Sector | wflow | ex-top1 | top1 | top1_w | n |
|---|---|---|---|---|---|
| **Financials** | +0.004 | **−0.060** | BRK-B | 13.9% | 47 |
| **Industrials** | −0.015 | **+0.059** | CAT | 8.7% | 50 |
| **Materials** | −0.069 | **+0.168** | LIN | 24.7% | 12 |

**No verdict below rests on the `wflow` of any of these three.**

## §1 · Inherited — one line, verbatim

**MACRO holds:** `INDU OW− · ENRG N+ · FIN N+ · IT N · HLTH N · DISC N · MATR N− · COMM UW · UTIL UW ·
STPL UW− · RE UW`.

## §2 · Deltas — **THREE**, each carried by a non-cap-weighted flow number

★ **The single cleanest number on the board, and it decides two of the three**: of the eleven sectors,
**only TWO carry a positive 2-session Δ — Energy +0.074 and Health Care +0.157** — and they are exactly
the two MACRO §G argued for promotion from the price side. The other nine run −0.003 (STPL) to −0.212 (COMM).

| Sector | matrix said | flow evidence (Δ = 2 sessions, 08-07→08-11) | new verdict | who resolves |
|---|---|---|---|---|
| **Energy** | **N+** | **rank-1 on BOTH axes: wflow +0.360 · eqflow +0.163** · **Δ +0.074** · **7 of 16 at the OBV∧RS20 pre-condition** · breadth 0.06 · **no flipper** (XOM 30.5%, ex-top1 **+0.257**, sign holds) | ★ **OW−** | **DEEP-ENRG (continuous)** |
| **Health Care** | **N** | **rank-2 on BOTH axes: wflow +0.230 · eqflow +0.217** — the **tightest cap-vs-equal agreement of 11** (gap 0.013) · **Δ +0.157 = largest on the board** · **18 of 32 at the pre-condition, 3rd-highest count** · no flipper (LLY 19.4%, ex-top1 +0.169) | ★ **N+** | **DEEP-HLTH (rotating)** |
| **Financials** | **N+** | 🚨 **flipper (BRK-B) ⇒ wflow +0.004 is INADMISSIBLE.** On the non-cap-weighted axes: **eqflow −0.043 (negative)** · **Δ −0.078** · breadth 0.09, **but 2 of its 4 greens (JPM surge 0.56 · BRK-B 0.92) are VELOCITY-LIT** (SWEEP §2a) on an 11.3%-coverage axis | **N** | **DEEP-FIN — NOT this run (see §3)** |

### 2a · Why Health Care's headline breadth of 0.0 is not a contradiction

`SECTOR_FLOW_US.json` shows HLTH **breadth 0.00 (0 🟢 of 32)**, which reads as a flat refutation of a
promotion. **It is a filter artifact and SWEEP §4 measured it**: **18 of 32 HLTH names pass
`OBV 매집 ∧ RS20 > 0`** — the 3rd-highest count on the board — **and every one is blocked by
`vol_surge` < 1.2 alone** (94 of 94 blocked names board-wide fail on that single axis; **M144's sixth
replication across two markets and six dates**). ⇒ **the breadth column is the wrong instrument for
HLTH today; wflow/eqflow are the right ones, and they rank it 2nd of 11 with the board's largest Δ.**
Corroborating and **independent of the sweep**: `XLV` exc5 **+3.75**, exc20 **+3.65**, **exc60 +11.59 —
the board's best 60-day**, vs `SPY` (benchmark named inline).

⚠ **HLTH is promoted ONE notch (N → N+), not two.** The 08-08 and 08-10 runs both declined this sector
on its own 07-30 anti-signal, whose magnitude has weakened **−6.78 → −3.05 → −1.59** across three
firings; `DEEP_LOG 2026-08-10` instructed that **a fourth firing at a smaller magnitude should
re-examine the ANTI-SIGNAL, not the sector.** That re-examination is a DEEP question, not a ROTATION
one — so the notch is single and **DEEP-HLTH owns the rest.**

### 2b · Financials — the demote, and the argument against it stated in full

The demote is carried **only** by non-cap-weighted numbers, as the flipper rule requires: **eqflow
−0.043** and **Δ −0.078**. Its apparent breadth (0.09, rank 2) **decomposes to a news count** — the
exact mechanism **S65** was registered to bracket on 2026-08-06, reproduced today with velocity coverage
at **11.3%**: JPM 🟢 at `vol_surge` **0.56** and BRK-B 🟢 at **0.92**, both lit by `velocity` values
(1.27 / 1.51) drawn from a 34-name subsample.

⚠⚠ **The counter-argument, stated rather than buried**: **S51 FIRED-A this run** — the bear steepener
persisted at 2s10s **+0.47**, so FIN's NIM mechanism is intact — and **S65 FIRED-C**, i.e. the breadth
neither converted nor collapsed. **That is a MACRO argument, and the protocol forbids this stage from
carrying a verdict on one** ("a change justified only by a macro argument is reverted"; the symmetric
reading is that a *hold* justified only by a macro argument is MACRO's call, not this stage's).
**This stage moves on the flow it is allowed to read and hands the mechanism question to MACRO/PREMORTEM.**
This is FIN's **third consecutive demote on a consistent axis** (OW → OW− 08-07 → N+ 08-08 → **N** today),
not a thrash.

### 2c · 🚨 Attempts DECLINED, with their numbers

| Attempt | Declined because |
|---|---|
| **MATR N− → N** (its UW leg lost its falsifier) | 🚨 **Materials is a flipper — LIN, 24.7% of a 12-name bucket — so `wflow` may not carry a move in either direction.** Switching to the permitted axes **does not support the promotion**: **`eqflow` DECAYED +0.040 (08-10) → +0.018**, **breadth 0.00**, **Δ −0.030**. ⇒ **the price leg fired and the money leg did not follow.** ★ **This is a genuine, maximum-width matrix×flow contradiction**: **S57 FIRED-A** (XLB exc5 +2.484), **P44's own anti-signal fired** (ex-NEM cap-weighted **+1.203**, equal-weighted +0.908, **8 of 12 names positive**), and the sweep's `wflow_ex_top1` **+0.168** agrees with both — **three price/composition constructions against one decaying flow axis.** **Declined here and handed to PREMORTEM**, which owns S57's consequence for a live tilt |
| **UTIL UW → UW−** (deepen) | Redundant, and the sector already sits at the floor of what this desk's scale expresses. Its numbers are the board's worst on **every** flow axis (wflow −0.475 · eqflow −0.482 · 13🔴 of 15 · **0 of 15 at the OBV∧RS20 pre-condition — the only REAL absence on the board**, SWEEP §4) but **Δ −0.081 is mid-pack** and one session (`XLU` exc1 **+1.48, best of 11**) points the other way. **A deepen on an unchanged floor is not information** |
| **IT N → N−** | ⚠ Its contradiction is **wider** than last run, not narrower: **eqflow −0.218 is WORSE than wflow −0.151** (the average IT name lags the cap-weighted index), **23🔴 of 56**, Δ −0.142 — against **breadth 0.11, the HIGHEST of 11**. **Breadth-as-count and breadth-as-eqflow disagree in IT and only in IT.** EVENT_ALPHA Card 6 grades the AI thread **STORY-ONLY** on the same evidence. **A contradiction at maximum width is a DEEP question, not a delta** (the 08-10 decline, repeated for the same reason and now with a live narrative cross-check) |
| **COMM UW → UW−** | **R56 binds**: `EA` went private 2026-08-04/05 and **is still in `us_top300.csv`**, so any COMM breadth number is contaminated. The aggregate's `wflow −0.474` vs `eqflow −0.016` is a **0.458** gap owned by GOOGL at 38.2% of sector cap. ⚠ **COMM is NOT on the flip list**, so wflow is technically admissible — **it is declined on the delisted-constituent contamination instead**, which is the stronger objection |
| **DISC N → N+** | wflow −0.180 vs **eqflow +0.010** — cap and breadth disagree in **sign**, with AMZN at 40.2% of cap (ex-top1 **−0.294**). **C3: no signal, not a neutral verdict.** Δ −0.147. Its 4-run window disagreement closed 08-08 at ≈zero both ways and nothing has re-opened it |

## §3 · DEEP picks and DEEP_LOG — **N = 4** (protocol DEEP budget: 2 continuous + 2 rotating)

| Slot | Sector | Why, by the rule |
|---|---|---|
| **Continuous 1** | **ENRG (OW−)** | Today's **rank-1 OW on both flow axes**, promoted this run. **Anti-thrash N/A** — it did not hold a continuous slot on 08-10 (it was deliberately un-dived there with its question handed to PREMORTEM+BET). Last covered **2026-08-08**. Its two brackets settled this run in opposite ways — **S60 FIRED-A** (the XLE sale was wrong) and **S55 C** (the physical-vs-premium split is still unresolved) — and **EVENT_ALPHA Cards 1+2 confirm from the bottom up.** **The unresolved question is now dated: S67 settles 08-13** |
| **Continuous 2** | **INDU (OW−)** | ★ **Anti-thrash APPLIED and stated**: INDU held a continuous slot on **2026-08-10** and is **still a top-N OW today**, so it KEEPS the slot by the rule. ⚠ It is now the **weakest** overweight on the board — exc5 **−0.28** while three sectors beat it on every window, eqflow +0.048, Δ −0.055, and it is a **flipper (CAT)** so its wflow is inadmissible. **DEEP-INDU's first question is whether the OW− survives its own numbers** |
| **Rotating 1** | **HLTH (N+)** | ★★ **A written pre-commitment HONOURED on its first ask.** `DEEP_LOG 2026-08-10` wrote *"HLTH — ★next run's first rotating pick."* **Last covered 2026-08-06 = 4 runs.** Promoted today on rank-2 both axes + the board's largest Δ. **Its DEEP mandate is explicit: re-examine the 07-30 ANTI-SIGNAL (weakening −6.78 → −3.05 → −1.59 across three firings), not the sector** |
| **Rotating 2** | **UTIL (UW)** | ⚠ **Declared deviation, stated rather than hidden: the rotating rule asks for the "next-highest OW not covered in ~3 runs" and NO third OW EXISTS** (the board holds exactly two, both taken as continuous). **Recency-starved fallback.** UTIL is the **longest-uncovered sector with a live signal — last covered 2026-08-05 = 5 runs** — and it carries this run's one genuinely NEW measurement: **0 of 15 names at the `OBV 매집 ∧ RS20>0` pre-condition, the only absence on the board that is REAL rather than a `vol_surge` filter artifact.** Against that, `XLU` was the **best sector on the 08-11 session (+1.48 exc1)** and the **worst on 20 days (−7.00)**. **DEEP-UTIL resolves which one is the tape** |

**Not padded.** Two sectors with live claims were left out and both are named, not dropped: **MATR**
(covered 08-10 — "we looked and passed" applies, and its consequence belongs to PREMORTEM) and **FIN**
(demoted today, covered 08-08; its mechanism question is bracketed by S51/S65 rather than open).

## DEEP_LOG 2026-08-12: continuous=[ENRG, INDU] rotating=[HLTH, UTIL] · N=4/4 · **THREE verdict deltas — the first non-zero delta run since 08-08 — and the reason is instrumental, not interpretive: two fresh settled sessions (08-10, 08-11) plus a RESTORED Δ baseline (PREFLIGHT G2 PASS, same-mode 299-name 08-07 snapshot, 99.7% coverage), so the S1 objection that correctly forced zero deltas on 08-10 no longer holds** · **ENRG N+→OW− (rank-1 both axes, wflow +0.360/eqflow +0.163, Δ +0.074, no flipper, EVENT_ALPHA Cards 1+2 confirm bottom-up)** · **HLTH N→N+ (rank-2 both axes with the tightest cap-vs-equal gap of 11 at 0.013, Δ +0.157 = board's largest; its breadth 0.00 is a `vol_surge` FILTER ARTIFACT — 18 of 32 pass OBV∧RS20 and 94/94 board-wide blocked names fail on that axis alone = M144's 6th replication)** · **FIN N+→N, third consecutive demote on a consistent axis, carried ONLY by eqflow −0.043 and Δ −0.078 because BRK-B makes it a flipper; its breadth again decomposes to a news count (JPM surge 0.56, BRK-B 0.92, both velocity-lit on an 11.3%-coverage axis = S65's mechanism reproducing)** · **five attempts declined with numbers: MATR N−→N (flipper LIN 24.7%; the permitted axes REFUSE the promotion — eqflow decayed +0.040→+0.018, breadth 0.00, Δ −0.030 — while S57 FIRED-A and P44's anti-signal fired at ex-NEM +1.203 ⇒ a maximum-width price-vs-flow contradiction handed to PREMORTEM), UTIL UW→UW− (redundant on an unchanged floor), IT N→N− (contradiction WIDER: eqflow −0.218 worse than wflow −0.151 vs breadth 0.11 highest of 11 — a DEEP question), COMM UW→UW− (R56 — EA delisted and still in the universe file, 5th run), DISC N→N+ (cap and breadth disagree in sign, C3))** · **flip list 3 of 11 — Financials/BRK-B/13.9% · Industrials/CAT/8.7% · Materials/LIN/24.7% — no verdict rests on any of their wflow** · **anti-thrash APPLIED to INDU (continuous on 08-10, still top-N OW); NOT applicable to ENRG** · **rotating slot 2 is a DECLARED recency-starved deviation — no third OW exists on an 11-sector board holding exactly two** · uncovered=[**MATR(N−, covered 08-10 = 1 run; ★S57 FIRED-A on 08-10/08-11 (+2.227/+2.484 vs a +1.9 line) and P44's registered anti-signal FIRED (ex-NEM cap-weighted +1.203, equal +0.908, 8 of 12 names positive, NEM only 11.6% of sector cap) ⇒ the UW's stated legs are refuted on price while eqflow decayed — **PREMORTEM owns the consequence for a live tilt**, and this is ★next run's first rotating pick if the flow axis turns)**, **FIN(N, demoted today, covered 08-08 = 2 runs; S51 FIRED-A keeps the NIM mechanism, S65 FIRED-C at median RS20 +2.871 with ex-BRK-B +3.084 ⇒ the BRK-B contamination pre-commitment is DISCHARGED at a 0.21pp gap; PRU remains the only FINRA clean-rise in its shortlist quartet)**, **IT(N, covered 08-10; 23🔴 of 56, eqflow −0.218 vs breadth 0.11 = the board's only breadth-count/breadth-eqflow sign disagreement; EVENT_ALPHA Card 6 grades the AI thread STORY-ONLY on the same bar; the CXMT/Apple supply axis (P43) is carried UNREFRESHED because the news feed returned 0 articles for 08-11 and 08-12)**, STPL(UW−, covered 08-10 — first deep-dive in recorded history; Δ −0.003 = flattest of 11, i.e. the demote has stopped deepening; ADM/CTAS missed-ledger recheck 08-16), COMM(UW, covered 08-07 = 4 runs; **the telecom node T/VZ/CMCSA un-owned for a 4th run**; R56 blocks the aggregate while EA sits in `us_top300.csv` at day 28), DISC(N, covered 08-03 = **the longest gap on the board, 6 runs** — but C3 no-signal in both directions, so the gap is not an information gap), RE(UW, covered 08-04 = 5 runs; the most internally consistent verdict on the board — wflow −0.222, eqflow −0.182, breadth 0.00, Δ −0.190 (2nd worst), exc5 −2.31 (worst of 11) — every axis agrees, which is why it does not need a slot)]

---

## ✅ EXIT CHECK

- [x] **§1 is ONE line**, MACRO's matrix verbatim. No unchanged sector gets a row or a restated flow number
- [x] **Every §2 delta cites a flow number** — ENRG (wflow+eqflow+Δ+pre-condition count), HLTH (wflow+eqflow+Δ+pre-condition count), FIN (eqflow+Δ). **No delta rests on a macro argument**; where one existed (FIN's NIM mechanism via S51-A) it is **named as a counter-argument and explicitly handed back to MACRO/PREMORTEM**
- [x] 🚨 **No promotion or demotion rests on a `top1_flips_sign` bucket.** The flip list (3 of 11) is reproduced in §0 in full. **FIN moves on `eqflow` with the inadmissibility of its `wflow` written out; MATR's move is DECLINED and the decline is written out with its permitted-axis numbers**
- [x] **The axis count is stated** (`n_axes` 3 · `vel_coverage` 0.1133) and **no delta cites theme freshness or velocity.** ★ **Δ is read against a same-axis-count snapshot (08-07, 299 names, 99.7% coverage) and is labelled "2 sessions" everywhere**
- [x] **Every matrix×flow divergence named with a resolution owner** — HLTH's breadth artifact → DEEP-HLTH · MATR's price-vs-flow contradiction → **PREMORTEM** · IT's breadth-count-vs-eqflow contradiction → DEEP (logged uncovered) · UTIL's 1-day-vs-20-day split → DEEP-UTIL
- [x] **N=4 DEEP targets picked by the rule** — continuity **applied to INDU and stated**, **not applicable to ENRG and stated**; the rotating-2 fallback is a **declared recency-starved deviation** because no third OW exists. **No padding**
- [x] **OW sectors left without a slot are named in DEEP_LOG** with last-covered dates and dated catalysts — including the two live claims (MATR, FIN) that were deliberately passed over
- [x] **Linter run on this stage's own output** — see below
- [x] **DEEP_LOG line appended** for the next run

---
---

# ═══ RUN-2 ADDENDUM · ROTATION — 2026-08-12 23:05 KST · **APPEND-ONLY** ═══

> Delta-only, as the stage requires. Nothing above is rewritten. **No DEEP pick is changed.**

## §R2-1 · Verdict deltas this run: **ZERO**, and the reason is structural

**RUN-1 holds:** `INDU OW− · ENRG OW− · FIN N · IT N · HLTH N+ · DISC N · MATR N− · COMM UW ·
UTIL UW · STPL UW− · RE UW` (after its three deltas: ENRG N+→OW−, HLTH N→N+, FIN N+→N).

**RUN-2 changes none of them.** This is a decision with a stated basis, not an omission:

1. **No new settled price bar exists.** Every flow axis a tilt may move on is unchanged from the
   08-11 close. A verdict move on unchanged data is a re-description, not a delta.
2. **The one axis that DID change (news) may not be used to move a sector.** RUN-2's velocity reads
   are **4-axis direct calls on individual names**; the sector aggregates on disk are **3-axis**.
   **G2 forbids differencing them**, so no sector-level Δ can be constructed from the recovery.
3. **G3 still binds Financials · Industrials · Materials** — no promotion or demotion on `wflow`,
   unchanged from RUN-1.

⇒ **The correct rotation output for a post-print, pre-open run is zero deltas.** Recorded explicitly
because a run that produces no verdict change should say so rather than manufacture one.

## §R2-2 · What the restored news axis changes about RUN-1's §0 caveat

RUN-1's §0 states: *"The news axis is dead again (11.3% coverage), so no delta below cites theme
freshness."* **That caveat is correct as written and stays.** RUN-2 narrows it rather than lifting it:

- ✅ **Theme-freshness statements are now legal when the warrant is a RUN-2 direct call.**
- ⛔ **They remain illegal for anything sourced from `SECTOR_FLOW_US.json`** — that file was scored
  with the axis dropped and does not become news-informed retroactively.

## §R2-3 · Intra-sector refinements — **none of which move a verdict**

| Sector | RUN-1 verdict | What RUN-2 measured (4-axis direct, 08-11 bar) | Effect on the verdict |
|---|---|---|---|
| **ENRG** | **OW−** | The strength is **refining**, not the sector: **PSX 🟢 (vel 2.07×) · MPC 🟢 (1.27×) · VLO 🟡** all OBV-accumulating with RS60 **+21.9 / +26.6 / +23.7**, while **XOM 0.82× and CVX 0.85× run velocity BELOW 1** and **KMI 🔴 (0.40×) · LNG 🔴** distribute | **NONE.** It **sharpens** the OW− rather than moving it — and it explains **breadth 0.06** on 16 names. ⚠ **DEEP-ENRG owns this**, not ROTATION |
| **IT** | **N** (N− declined as "a contradiction at maximum width") | The width is now **decomposed**: **ANET 🟢 vel 2.59× · RS60 +40.7%** and **COHR/LITE 🟢 inflecting**, against **MU 🔴 · AMD 🔴 · GEV 🔴 · CIEN 🔴** | **NONE — and the decline is now better founded.** The sector's internal dispersion is **real and named** (interconnect leading, memory lagging), which is precisely why an aggregate verdict is the wrong instrument |
| **UTIL** | **UW** (deepen to UW− declined) | **VST reads 🔴 on the 3-axis sweep and 🟡 on the 4-axis direct call**; **NRG runs vel 3.16× — the highest of any name measured — against OBV distribution**; CEG 🟡 1.57×, TLN 🟡 1.29× | **NONE.** ⚠ Stated carefully: **the two tags are different instruments, not a change** (G2). What is citable is that **UTIL's floor is carried by names whose narrative is loud and whose money is leaving** — the STORY-ONLY signature |
| **MATR** | **N−** (N declined; S57 FIRED-A handed to PREMORTEM) | No new data. **Copper still 100th %ile** on the same 08-11 COT file | **NONE.** Unchanged and still PREMORTEM's |

★ **The one line worth carrying**: **on 4 axes, no Energy name in the measured sample is 🟢 except the
refiners, and no Utilities name is 🟢 at all.** The sector labels at the top of the board and the names
underneath them are describing different objects — the same fact **breadth ≤0.06 in 7 of 11 sectors**
reports from the aggregate side.

## §R2-4 · DEEP picks — **unchanged, not re-run**

`DEEP_LOG 2026-08-12` stands as RUN-1 wrote it: **ENRG · HLTH · INDU · MATR** (+ **UTIL** as the
pre-mortem-promoted 5th). **RUN-2 does not re-pick.** Re-selecting DEEP targets on identical flow data
would consume the rotation budget twice for one day's information and would orphan the five
`SECTOR_DEEP_*.md` files already on disk.
