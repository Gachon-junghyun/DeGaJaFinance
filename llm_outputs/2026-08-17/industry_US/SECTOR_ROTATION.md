# SECTOR_ROTATION — industry_US · 2026-08-17 · Stage 6/11 (L1·ROTATION)

> Delta-only. MACRO owns the 11-sector matrix (`MACRO_REPORT §G`); `SECTOR_FLOW_US.json` owns the flow
> numbers. Both are on disk. This file writes **only what changes, why, and the DEEP picks.**

## §0 · The axis count this run scored on, stated before any number is used

`SECTOR_FLOW_US.json §scoring.n_axes = **3**` · `vel_coverage = **0.1706**` (51/299) ·
`dropped_missing_axis = 0`.
⇒ **No delta below may cite theme freshness or news velocity**, and Δ is read only against the
**08-13** snapshot, which is the same 3-axis mode.

## §1 · Inherited — one line, verbatim from `MACRO_REPORT §G`

`ENRG OW · INDU OW− · IT N+ · HLTH N · FIN N− · MATR N− · DISC N− · COMM UW · STPL UW− · UTIL UW · RE UW`

## §2 · Deltas — **ZERO, and the zero is measured**

**No sector moves. No flow number capable of carrying a delta changed.**
Measured, not assumed: **299 of 299 names carry an identical `flow_score` to the 08-16 run**, 0 of 11
sector `wflow`/`eqflow` rows changed, and **0 sessions have settled since the prior run** (fourth
consecutive run priced off the 2026-08-14 close).

★ **Exactly two numbers on the entire board moved, and both are inadmissible.**

| Sector | What moved | Why it may not carry a verdict |
|---|---|---|
| **Financials** | `breadth` **0.04 → 0.06** | `MA`'s tag flipped 🟡→🟢 because its **news velocity** rose 1.17 → 1.29 across the 1.2 gate. **Price inputs identical to the digit.** `tag = flow_tag(price, velocity)` sits outside the axis-drop guard (`SWEEP_READ §3`) |
| **Communication Services** | `breadth` **0.08 → 0.00** | `NFLX`'s tag flipped 🟢→🟡 on velocity **1.23 → 1.17**, same mechanism, opposite direction |

⇒ **A `breadth` delta is not market information this week.** Both are `D261`/`D263-KR`, and `MA` is
additionally one of the four **inadmissible** greens (`vol_surge` 0.73 — it could never be green on the
axes the score is built from).

### §2b · 🚨 Flip list — reproduced in full even though it changes nothing

| Sector | wflow | ex-top1 | top1 | top1_w | n |
|---|---|---|---|---|---|
| Information Technology | **+0.023** | **−0.082** | `NVDA` | **19.4%** | 56 |
| Industrials | **−0.047** | **+0.006** | `CAT` | 8.7% | 50 |
| Materials | **−0.169** | **+0.033** | `LIN` | **24.7%** | 12 |

**3 of 11 — identical set, identical numbers to 08-15 and 08-16.** ⚠ That identity is **one observation
read three times**, not a structure confirmed (PREFLIGHT G2). **No verdict in this file rests on any
flipper's `wflow`.** Every `top1_w` is computed from a **33-day-old** cap file.

### §2c · Attempts declined, with numbers

| Attempt | Declined because |
|---|---|
| **ENRG OW → higher** | No notch above OW is defined. What is new today is **narrative, not flow** — a D-0 binary (the 60-day US–Iran MoU expired) and Hormuz traffic near zero. ★ **And the tape refuses it**: Brent **88.91 → 88.52** across 08-11→08-14 vs `SPY` +0.75%. Recorded as `P69`/`P70` and as the DEEP mandate, **not** as a verdict |
| **INDU OW− → OW** | Declined **on method for a 3rd run**. The 25-of-50 accumulation count remains a C5 invented metric; every registered axis refuses (flipper ⇒ `wflow` inadmissible · `eqflow −0.007` · `breadth 0.00` · Δ −0.001). ⚠ **Declining three times on identical data is one decision, not three** |
| **IT N+ → any** | Flipper ⇒ `wflow` inadmissible in both directions. N+ still rests on the **0.021** flow-point gap (`eqflow +0.044` vs `wflow +0.023`). `S85` settles **08-21** and reads **+1.343 = branch C** |
| **DISC N− → UW** | Δ **+0.038 positive** = wrong direction for a demote, for a 3rd run. ⚠ Today's `HD` 🔴분산 (OBV dispersing, RS20 −3.9) is a **name-level** flow number and does not move a 28-name aggregate; W5 independently blocks the label (`ABNB` 🟢 RS60 +34.5 vs `SPY` inside the same GICS code) |
| **STPL UW− → any** | UW− is the board's defined floor, so no demote exists. ★ **A promotion attempt is newly arguable and is declined on flow**: `TGT` is 🟢가속 with OBV accumulating and RS60 **+21.4%**, but the sector aggregate is unchanged (`eqflow −0.213`, 3 of 19 accumulating). **One name is a DEEP mandate, not a sector verdict** — and that is exactly what it becomes below |
| **UTIL UW → UW−** | Declined for a 2nd run. The flow case is the board's only real absence (0 of 15 pass at **OBV/RS**, before the `vol_surge` gate), but `P65`/`R73` leave the **mechanism half-refuted** — a bull steepener with `DGS2` falling 10bp is a tailwind for regulated utilities. **Notching down into a dissolving mechanism is not a measurement** |
| **FIN N− → any** | `M40`'s inversion is unrepaired (`eqflow −0.126` still below `wflow −0.031`); `R69` stands. Today's `breadth` uptick is instrument flicker (§2). `S78` settles **08-19** |
| **HLTH · MATR · COMM · RE** | All inherit the 08-16 declines **on byte-identical numbers**. Nothing new is argued; the settles do the work (`S76`/`S77`/`S78`/`S80` on 08-19, `S82` 08-20, `S90` 08-21) |

★ **The honest summary of this stage: with three of four macro instruments frozen and the fourth
inadmissible for deltas, zero is the correct output.** The protocol names this as a valid, informative
run. What the run added is in §3 — one rotating slot's mandate went from *empty* to *real*.

## §3 · DEEP picks and DEEP_LOG — **N = 4** (protocol budget: 2 continuous + 2 rotating)

| Slot | Sector | Mandate |
|---|---|---|
| **Continuous 1** | **ENRG (OW)** | Held the slot 08-15 and 08-16 and is still the top OW ⇒ **anti-thrash continuity, slot KEPT.** Mandate: ★ **resolve the discrimination the tape just handed us.** Card 1 measured Brent **−0.44%** and WTI **−0.96%** across 08-11→08-14 while Hormuz traffic collapsed and `XLE` beat `SPY` by only **+0.86pp**. The desk's own §3a thesis is *"refining-CAPACITY destruction, not a crude trade"* — **this is the first clean control that separates the two, and the DEEP must run it name by name** (refiner RS60 `PSX +27.5` · `VLO +31.5` vs integrated `XOM −2.2` · `CVX +0.4`). ② `M707`'s three refutations stand and must be re-tested, not restated (no OBV confirmation on the +19% 5-session move · bearish RSI divergence at the upper band · no issuer event until **11-03**). ③ `CYCLE_EXPOSURE` 🚨 **GAP −0.868pp** on this exact node on the day the MoU expired. ④ `S88` settles **08-21** from the **100th percentile of two years** |
| **Continuous 2** | **INDU (OW−)** | Held 08-15 and 08-16; still the only other OW-side sector ⇒ **slot KEPT.** Mandate: ★ **a dated issuer event landed on the basket's weakest leg today.** Card 3 — `LHX` CEO Christopher Kubasik stepped down, insider successor, **stock down**, 4 outlets, and its FINRA short-z was already **+1.86 🔴 building on 08-14**. `M704` had measured `LHX` as the **only** name negative on both 20d and 60d inside the defense EW that closed `D249`. **Re-run `M704`'s EW ex-`LHX`** and state whether the +7.163pp 20d verdict survives. ② `M708`'s three-businesses split (**10.6pp** spread) means a sector-level number here averages over an object already proven to be three. ③ `HII` remains **outside `us_top300`** (`D274`) — unmeasurable, say so rather than omitting it |
| **Rotating 1** | ★★ **STPL (UW−)** | **The board's longest gap — last covered 2026-08-10 = 7 runs** — and the 08-16 DEEP_LOG explicitly pre-committed: *"logged so the next run sees a 7-run gap and weighs it against a real mandate."* ★ **The mandate is real this run and was not on 08-16.** `TGT`: 🟢가속 · news **2.38×** (probe 22:41 KST) · OBV **매집** · RS20 +5.9 · **RS60 +21.4%**, against `WMT` exc60 −9.913 and `COST` exc60 −17.981 = a **33.6pp intra-sector spread**. ② **`TGT` reports ~08-20**, so the DEEP has three sessions to establish whether this is accumulation or pre-print positioning — the distinction `COHR`/`LITE` taught the desk on 08-16. ③ The sector is `S80`'s third duration leg (settles **08-19**) and `P65`/`R73` changed that mechanism underneath it |
| **Rotating 2** | **HLTH (N)** | **Last covered 2026-08-13 = 4 runs**, tied with MATR and winning the tiebreak on **two brackets settling inside three days with no fresh map**: `S76` (**08-19**, two independently scored legs) and `S82` (**08-20**, **already above its branch A at +3.091 at registration**). ★ A DEEP that lands **before** a settle is worth more than one that lands after. Mandate: ① Δ **−0.103 = the worst of eleven and a 4th consecutive negative** — against **15 of 32 accumulating**, so the `breadth 0.00` is a `vol_surge` artifact (`D270`) and the two must be reconciled, not averaged. ② `XLV` exc60 **+7.803 vs `SPY` = 2nd best of eleven** — price and flow disagree and the DEEP owns which is right. ③ `S82` asks whether HLTH is idiosyncratic med-tech or the **fourth** leg of the duration complex the desk is UW three times |

⚠ **Rotating slots are a DECLARED recency-starved deviation for a 6th run.** After the verdicts, only
two OW-side sectors exist and both hold continuous slots, so the rotating picks are drawn from the
non-OW board by recency + mandate. This is the protocol's stated fallback and it is named, not hidden.

⚠ **Lost the tiebreak, with reasons**: **MATR** (08-13 = 4 runs; flipper `LIN` 24.7%, `eqflow −0.114`,
6 of 12 accumulating so the absence is `unknown` (C3); scores via `S77` **08-19** without a DEEP) ·
**FIN** (08-14 = 3 runs; `KKR` is the sector's only admissible 🟢 and is ⚡crowded-short at z **+1.62**;
scores via `S78` **08-19**) · **COMM** (08-14 = 3 runs; the bucket's numbers move by **composition**
because `EA` left the scored set, so a DEEP would be mapping a changing object) · **IT** (08-16 = 1 run,
too recent — ★ but this run's single strongest cross-instrument signal is inside it: `optical` **1.74×**
+ `OPTOELECTRONICS` z **5.7** + a BUILDING Lightmatter thread + the board's **top two `flow_score`
names** `COHR` +0.99 / `LITE` +0.82, and `cycle_registry.json` **has no row for that cycle** (`D250`).
**Handed to PREMORTEM as an exposure-and-registry question**, not left unowned).

## DEEP_LOG 2026-08-17: continuous=[ENRG, INDU] rotating=[STPL, HLTH] · N=4/4 · **ZERO verdict deltas — measured: 299/299 identical `flow_score`, 0/11 sector rows changed, 0 sessions settled since the prior run (4th consecutive replay of the 2026-08-14 close)** · **★the ONLY two flow numbers that moved on the entire board are `Financials` breadth 0.04→0.06 and `Communication Services` breadth 0.08→0.00, and BOTH are instrument flicker — `MA` velocity 1.17→1.29 and `NFLX` 1.23→1.17 crossing the 1.2 tag gate with price inputs identical to the digit (`D261` / `D263-KR`, now demonstrated all the way through to the candidate list: the live shortlist swapped `NFLX` out for `MA`, and `MA` is one of the four INADMISSIBLE greens at `vol_surge` 0.73)** · **flip list 3 of 11 — Information Technology/`NVDA`/19.4% · Industrials/`CAT`/8.7% · Materials/`LIN`/24.7%; identical set and numbers to 08-15 and 08-16 = ONE observation read three times; no verdict rests on any flipper's `wflow`; every `top1_w` from a 33-day-old cap file** · **`D261` decomposition on today's greens: 5 of 9 are 3-axis producible (`COHR`·`KKR`·`ABNB`·`LITE`·`MPC`), 4 are not (`CVX` surge 0.95 · `CSCO` RS20 −4.7 · `BAC` surge 0.73 · `MA` surge 0.73) and all four carry a velocity value ⇒ admissible green count is 5 not 9 = 1.8× over-representation of a 17.1%-coverage survivor sample (08-16 2.2× · 08-15 3.2× · 08-13 2.6×, FOURTH replication and the ratio is falling only because the green count fell)** · **`M144`/`D270` replicated an EIGHTH time at a NEW RECORD: 125 names pass `OBV 매집 ∧ RS20>0`, exactly 5 also clear `vol_surge ≥ 1.2`, so 120 are blocked and 100.0% of them on `vol_surge` alone (prior record 110/100) ⇒ "breadth 0.00" this week is a statement about VOLUME, not demand; median last-bar volume 0.649× after 0.732×** · **eight attempts declined with numbers (ENRG→higher: no notch defined AND the new evidence is narrative not flow — the tape refuses it, Brent −0.44% and WTI −0.96% across 08-11→08-14 while Hormuz traffic collapsed; INDU→OW: declined ON METHOD for a 3rd run on identical data = one decision not three; IT→any: flipper both ways, N+ rests on a 0.021 gap, `S85` reads branch C; DISC→UW: Δ +0.038 positive is the wrong direction and `HD`'s 🔴분산 is name-level not aggregate; STPL→any: floor already, and `TGT`'s 🟢 is one name = a DEEP mandate not a verdict; UTIL→UW−: the MECHANISM is half-refuted by `P65`/`R73`, a bull steepener with `DGS2` −10bp is a tailwind for the regulated leg; FIN→any: `M40` inversion unrepaired, `R69` stands, today's breadth tick is flicker; HLTH/MATR/COMM/RE inherit 08-16's declines on byte-identical numbers)** · **★the structural headline: THREE of four macro instruments returned data identical to the prior run — equity tape (08-14), `[FRED]` (**all 14 series, zero new observations AND zero revisions, on a live pull with no module cache**), COT (Tue 08-11) — and the fourth, the news corpus, moved **+3,843 articles** and carried a **D-0 binary the calendar missed**: the 60-day US–Iran MoU EXPIRED 2026-08-17 with Hormuz traffic near zero (5 outlets). `CATALYST_WATCH` returned only `NVDA` 08-26 and an UNDATED Hormuz row ⇒ `D259-KR` reproduced on this desk** · **★and every term instrument was blind to it: `theme_age` returned ⚪ECHO on 13 of 13 probes including `ceasefire` at 0.81× and `tanker` at 0.68×, and `burst` — which uses NO fixed vocabulary — surfaced ZERO Iran/Hormuz/oil tokens (its top-z words were `LG` 9.5 · `HBM` 7.2 · `OPTOELECTRONICS` 5.7). Mechanism: burst reads `field=title` against a 30-day baseline in which the term never left ⇒ a continuing story cannot burst (`D279`)** · **`CYCLE_EXPOSURE` 🚨 GAP on rank-2 Energy epicenter **7.13% vs an 8.0% floor = −0.868pp**, flagged on the very day the MoU expired — handed to ALPHA; rank-1 AI-compute clears at 16.57% vs 12.0%; rank-3 missile-defense has NO floor ⇒ ⚪n/a; **and the registry still has no row for optical/interconnect**, the cycle owning the board's top two `flow_score` names (`D250`)** · **`STPL` promoted to a rotating slot after being DECLINED on 08-16 for an empty mandate — the 08-16 DEEP_LOG pre-committed to re-weighing it and the mandate is now real (`TGT` 🟢가속, news 2.38×, OBV 매집, RS60 +21.4% vs `WMT` −9.913 / `COST` −17.981 = a 33.6pp intra-sector spread, reporting ~08-20)** · **rotating slots are a DECLARED recency-starved deviation for a 6th run** · uncovered=[**IT(N+, 08-16 = 1 run, too recent for a slot; ★the run's strongest cross-instrument convergence sits here — `optical` 1.74× (highest of 13 terms), `OPTOELECTRONICS` burst z 5.7, a BUILDING Lightmatter thread *"AI hits copper wall"*, and the board's top two flow scores `COHR` +0.99 / `LITE` +0.82, both 3-axis admissible; chain-hop surfaced `APH` at headline-0/proximity-3 with OBV 매집 and short-z −2.14 but RS60 already +32.4%; `cycle_registry` has NO row for the cycle ⇒ handed to PREMORTEM)**, **MATR(N−, 08-13 = 4 runs; flipper `LIN` 24.7%, eqflow −0.114, 6 of 12 accumulating ⇒ absence is `unknown` (C3); copper spec 100th %ile long; S77 08-19)**, **FIN(N−, 08-14 = 3 runs; `R69` stands, eqflow −0.126 below wflow −0.031; `KKR` the only admissible 🟢, ⚡crowded-short z +1.62; today's breadth tick is flicker; S78 08-19)**, **COMM(UW, 08-14 = 3 runs; the bucket's numbers move by COMPOSITION — `EA` delisted 08-04, still in the universe file at day 33, null last bar for a 5th run (`R56`); `XLC` exc60 −8.311 worst of eleven)**, **DISC(N−, 08-15 = 2 runs; Δ +0.038 blocks the demote; ★new bear-side evidence today is name-level — `HD` 🔴분산 with OBV 분배, RS20 −3.9 and news 1.67× = attention up while money leaves, filed to `reject_ledger`; `HD` reports imminently and its CEO took medical leave 08-16)**, **RE(UW, 08-15 = 2 runs; 4 of 12 accumulate = `M131`'s data-centre unit; `P67`'s credit driver is flat at HY OAS 2.71% for a 6th session; S90 08-21)**, **CONSUMER(premortem-promoted 5th slot 08-16 = 1 run)**]

## ✅ EXIT CHECK

- [x] **§1 is one line**, inherited verbatim from `MACRO_REPORT §G`. No unchanged sector gets a row.
- [x] **Every §2 delta cites a flow number** — and the count is **zero**, with the zero measured
      (299/299 identical `flow_score`). The two numbers that did move are named **and disqualified**.
- [x] 🚨 **No promotion or demotion rests on a `top1_flips_sign` bucket.** The flip list is reproduced
      in full (§2b) even though it changes nothing.
- [x] **Axis count stated** (§0, `n_axes = 3`, coverage 17.06%). No delta cites theme freshness or news
      velocity; Δ is read only against the same-mode 08-13 snapshot.
- [x] **Every matrix×flow divergence has a resolution owner** — ENRG's narrative-vs-tape split and
      INDU's issuer event go to DEEP; IT's optical convergence and the registry gap go to PREMORTEM;
      the `CYCLE_EXPOSURE` GAP goes to ALPHA.
- [x] **N = 4 picked by the rule** — 2 continuous by anti-thrash continuity, 2 rotating by recency +
      mandate, **no padding**. The recency-starved deviation is declared (6th run).
- [x] **OW sectors left without a slot**: none exist — both OW-side sectors hold continuous slots.
      All seven uncovered non-OW sectors are named in DEEP_LOG with last-covered date and mandate.
- [x] Linter run on this file.
- [x] DEEP_LOG line appended for the next run.
