# SECTOR_ROTATION — industry_US · 2026-08-15 · Stage 6/11 (L1·ROTATION)

> Delta-only. MACRO owns the 11-sector matrix; `SECTOR_FLOW_US.json` owns the numbers. Both are on
> disk. **This file writes what changes and why.** `n_axes = 3` (velocity axis revoked) — stated once
> here and inherited by every number below. No sizing (P4).

## §0 · 🚨 The flip list, reproduced even where it changes nothing

**3 of 11 sectors flip sign when their single largest name is removed.** None may carry a promotion or
demotion on `wflow`:

| Sector | `wflow` | ex-top1 | top1 | `top1_w` | n |
|---|---|---|---|---|---|
| **Information Technology** | **+0.023** | **−0.082** | `NVDA` | 19.4% | 56 |
| **Industrials** | **−0.047** | **+0.006** | `CAT` | **8.7%** | 50 |
| **Materials** | **−0.169** | **+0.033** | `LIN` | 24.7% | 12 |

★ **Health Care EXITED the list** — `LLY` (19.4%) no longer flips the sign (`wflow −0.115`, ex-top1
−0.031) ⇒ **`wflow` is admissible for HLTH again this run**, for the first time since 08-13.
⚠ `Industrials` flips on a **top1 weight of only 8.7%**, which means its `wflow` is sitting on zero,
not that `CAT` is large. ⚠ Every `top1_w` is computed from a **31-day-stale** cap file (PREFLIGHT G5).

## §1 · Inherited — one line, verbatim from MACRO §G

`ENRG OW− · INDU OW− · IT N+ · HLTH N · FIN N− · MATR N− · DISC N− · COMM UW · STPL UW− · UTIL UW · RE UW`

## §2 · Deltas — **one carried, seven attempted and declined**

### §2a · CARRIED: **Energy OW− → OW**

| Sector | matrix said | flow evidence (Δ = one settled session, 08-13 → 08-14) | new verdict | who resolves |
|---|---|---|---|---|
| **Energy** | **OW−** | **`eqflow` +0.102 — the HIGHEST of all eleven sectors** · **`breadth` 0.12 — the HIGHEST of all eleven** (2🟢/1🔴 of 16) · `wflow` **+0.217**, the board's **only** positive, and **NOT a flipper** (ex-`XOM` **+0.205**, still positive at a 30.5% weight) · **Δ −0.042 vs −0.157 on 08-14 = the blocker narrowed 73%** | ★ **OW** | **DEEP-ENRG (continuous 1)** |

**Why this clears the bar that stopped it twice.** The 08-13 and 08-14 runs both declined this
promotion **on Δ** — *"the level is best-in-class and the change is nearly worst-in-class."* Two things
changed and one did not:
1. ✅ **The Δ blocker shrank by 73%** (−0.157 → **−0.042**) on a board whose deltas now span only
   −0.103 to +0.092.
2. ✅ **The promotion no longer needs `wflow` at all.** `eqflow` and `breadth` are **both the highest
   of eleven**, and neither is cap-weighted, so the 31-day-stale caps and the `XOM` concentration are
   irrelevant to the carrier. **This is the first run in which Energy leads the board on a
   non-cap-weighted axis.**
3. 🚨 **What did NOT change, stated rather than buried: Δ −0.042 is still the 2nd worst RANK of
   eleven** (only HLTH −0.103 is lower). The magnitude improved; the rank did not.

**Corroboration from three independent stages, none of them a macro re-argument:**
- **SWEEP**: `MPC` is Energy's **only admissible 🟢** after the `D261` velocity adjustment, and one of
  the board's two ✅clean-rise names (FINRA short z **−0.71**). `CVX`'s 🟢 is velocity-lit and was
  **excluded** from this verdict.
- **EVENT_ALPHA Card 3 (CONFIRMED-EARLY)**: a **named physical mechanism** — Ukraine struck Gazprom's
  200,000-bpd Salavat refinery (08-13) and a fuel terminal (08-14); **Russia's diesel exports crashed
  to a multiyear low** [`oilprice` 08-13]. Refiner RS60 vs `SPY` **+22 to +29** against integrateds
  **−4 to −7** — a **36-point spread inside one GICS sector**.
- **CYCLE_EXPOSURE**: 🚨 **GAP on this exact node** — rank-2 cycle, epicenter **7.10% vs 8.0%
  required, margin −0.898pp.**

⚠ **The macro leg is deliberately NOT the carrier.** `P62` (distillate-led crack) and `XLE exc5
+7.271` are MACRO's, and re-arguing them here would be the 2026-07-21 defect. They are named as
context; **the verdict is carried by `eqflow`, `breadth` and the Δ improvement.**

### §2b · Attempted and DECLINED — seven, each with its number

| Sector | attempted | declined because |
|---|---|---|
| **INDU** OW− → **OW** | ★ **SWEEP found 25 of 50 Industrials names passing `OBV 매집 ∧ RS20>0`** — `LMT` (RS20 +15.2) · `AXON` (+15.7) · `EMR` (+12.5) · `RTX` (+10.8) · `NOC` (+7.9) · `ETN` (+8.4) · `GD` (+2.9) — **every one blocked on `vol_surge` alone.** Half a sector the board calls breadth-dead is accumulating | 🚫 **Declined on method, not on doubt.** The count is a **metric this run invented** (C5 — an arbitrary choice made after seeing the data), and the *registered* admissible axes all refuse: **G3 flipper (`CAT`) ⇒ `wflow` inadmissible**; `eqflow` **−0.007**; `breadth` **0.00**; Δ **−0.001**. ⇒ **Held at OW−, and the finding becomes the DEEP mandate rather than the verdict.** If the accumulation count is to move a sector, it must be registered as an axis first and measured for a sign — which is `D270`'s job, not this stage's |
| **IT** N+ → hold *(no change attempted upward)* | — | ⚠ **But the basis DECAYED and it is recorded here rather than left implicit.** The 08-14 promotion rested on `eqflow` sign-flip (−0.100 → +0.034) **and Δ +0.152 = 2nd best of 11**. Today `eqflow` **+0.044** (still positive, still above `wflow` +0.023) but **Δ is +0.007 — a 95% decay in one session**, and **EVENT_ALPHA Card 2 dates both admissible IT greens (`COHR` `LITE`) to their own 08-11/08-12 earnings prints**, i.e. the greens are **reaction volume, not accumulation**. **N+ is HELD on `eqflow` > `wflow` alone.** Its own falsifier `S85` (`RSPT − XLK`, settle 08-21) reads **+1.343 = branch C** |
| **HLTH** N → **N+** | ★ `LLY` **came off the flip list** ⇒ `wflow` admissible again; `eqflow` **+0.027 is positive**; Δ improved **−0.228 → −0.103**; and SWEEP found **15 of 32 accumulating** (the 0.00 breadth is a volume artifact) | 🚫 **Δ −0.103 is now the WORST of eleven** and it is the **4th consecutive negative** (+0.157 → −0.014 → −0.228 → −0.103). A promotion into the board's worst delta is the same error the ENRG promotion spent two runs avoiding. ⚠ Counter-evidence named: `XLV` exc60 **+7.803 vs `SPY`, 2nd best of 11**. **`S76` settles 08-19 · `S82` 08-20** |
| **DISC** N− → **UW** | `XLY` **exc5 −1.783 = worst of eleven**, `eqflow −0.123`, and **EVENT_ALPHA Card 5 supplies a dated body-read driver** (retail sales + consumer sentiment, 5 independent outlets, 08-14) | 🚫 **Δ is +0.038 — POSITIVE, and a deepening underweight needs a negative delta.** Declined **in the direction attempted**, exactly as COMM was on 08-14. ⚠ And the sector is not uniform (**W5**): `ABNB` is its only admissible 🟢 with **RS60 +34.5**, the best in the exposure set — a weak-goods/firm-services split the single label cannot express |
| **COMM** UW → any | Δ **+0.092 = the BEST of eleven** for a 2nd run; `eqflow −0.050` far better than `wflow −0.436` | 🚫 **Both directions blocked, and this run adds a composition warning**: `EA` has **dropped OUT of the scored set** (n 13 → **12**) after 8 runs of being scored while delisted (`R56`), **so this sector's numbers moved by composition, not by demand.** A verdict on a bucket that changed membership this run would be measuring the fix, not the market. ⚠ `XLC` exc60 **−8.311 = worst of eleven** blocks any promotion independently |
| **UTIL** UW → **UW−** | ★ SWEEP: **0 of 15 pass `OBV 매집 ∧ RS20>0` — the ONLY sector on the board where the absence is REAL and not a `vol_surge` artifact.** `wflow −0.445`, `eqflow −0.433` (worst of 11), 0🟢/7🔴 | 🚫 **Two numbers point the other way and both are dated to the same two sessions**: `XLU` **exc5 +1.207 = 2nd best of eleven**, and Δ **+0.045, positive**. ★ **Price turned while flow did not** — which is exactly what `P61` predicts if the driver is changing from term premium to policy-rate expectations. **A notch down into a mechanism that may be dissolving is not a measurement.** Handed to DEEP_LOG |
| **MATR** N− → any | ex-top1 `wflow` **+0.033** (positive); Δ +0.010 | 🚫 **Flipper (`LIN` 24.7%) ⇒ `wflow` inadmissible.** Permitted axes refuse: `eqflow` **−0.114**, breadth **0.00**, 0🟢/3🔴. ★ And the price side agrees independently — **`P59` scored HIT: ex-`NEM` EW exc5 −2.097 vs `SPY` with 1 of 11 positive**, while **copper spec sits at the 100th percentile long and `FCX` is the basket's worst name at −4.894.** `S77` settles 08-19 |
| **FIN** N− → any | `Δ +0.034`; `XLF` exc60 **+8.009 = best of eleven**; **`KKR` is the sector's only admissible 🟢** | 🚫 **`M40`'s inversion has NOT repaired**: `eqflow −0.126` still sits **below** `wflow −0.031`, i.e. the median financial is still worse than the cap-weighted sector (`R69` stands). ⚠ **The exc60 leg is a macro re-argument** (a steepener read) and is declined as a carrier on that ground — **and MACRO §A removes it anyway: `2s10s` is unchanged at +0.48 and the move was a 5bp parallel shift, not a steepening.** ★ **What IS confirmed on a second date: `M669`** — the breadth relocated to alternatives/asset-management, and `KKR` is exactly that node |
| **RE** UW → any · **STPL** UW− → deeper | — | 🚫 **RE**: `wflow −0.280` · `eqflow −0.244` · breadth 0.00 · Δ −0.029 · exc20 **−4.777, deteriorated from −4.366** — every axis still agrees. ⚠ **One new fact declines to fit**: SWEEP found **4 of 12 accumulating (`EQIX` `DLR` `CBRE` `IRM`)** — the data-centre node — inside the board's most uniformly negative sector. **That contradiction gets a DEEP slot rather than a verdict.** 🚫 **STPL**: declined **on notation** for the 2nd run — UW− is this board's floor and no step below it is defined; Δ **+0.081, positive**, so nothing pushes anyway |

**Attempted 9 · carried 1 · declined 8.**

## §3 · DEEP picks and DEEP_LOG — **N = 4** (protocol budget: 2 continuous + 2 rotating)

| Slot | Sector | Why, and the mandate |
|---|---|---|
| **Continuous 1** | ★ **ENRG (OW — promoted today)** | **Anti-thrash APPLIED** (continuous 08-13 · 08-14 · today) **and it is now the board's top OW.** **Mandate — three questions the promotion创造s**: ① the promotion is carried by `eqflow`/`breadth` while **Δ is still 2nd-worst by rank** — resolve whether the delta decay is `XOM` (Δ −0.153, 30.5% of cap) or the sector; ② **the `CYCLE_EXPOSURE` GAP is −0.898pp on the epicenter of the cycle this desk just promoted** — is the epicenter the refiners or the integrateds, given the **36-point RS60 spread**; ③ `PSX` and `VLO` carry the sector's #2 and #3 RS60 and are **🟡 on `vol_surge` 1.01/0.84 alone** (`D251`) — the two names leading the sector are filtered out of its own shortlist |
| **Continuous 2** | **INDU (OW−)** | **Anti-thrash APPLIED** (continuous 08-12 · 08-13 · 08-14). **Mandate is `D249`, now unresolved for a 4th run and with a THIRD object inside the same label**: ① the bracket measures `XLI`, the position is **defense**; ② SWEEP found **25 of 50 accumulating, all blocked on volume**, and the accumulating half is aero/defense + electricals (`M667`); ③ **NEW — EVENT_ALPHA Card 1**: the US Navy opened warship construction to foreign yards (08-14/08-15), and **`HII`, the pure-play US Navy shipbuilder, is NOT in `us_top300`** — the desk cannot measure the most exposed listed name. **Resolve which object the OW− is on, and whether the universe hole is material** |
| **Rotating 1** | ★★ **DISC (N−)** | **Recency: last covered 2026-08-03 = 9 runs, by far the longest gap on the board.** **Mandate — a contradiction that just acquired a driver**: `XLY` posted **exc5 −1.783, the worst of eleven**, in the same five sessions the consumer prints landed (Card 5, 5 independent outlets) — **yet Δ is +0.038, positive, which is what blocked the demote.** Resolve the split the label hides (**W5**): `AMZN` (40.2% of cap) is **OBV 분산** with `HD` at **−0.683 🔴**, while **`ABNB` is the sector's only admissible 🟢 at RS60 +34.5**. Goods vs services, on the flow axis |
| **Rotating 2** | ★★ **RE (UW)** | **Recency: last covered 2026-08-04 = 8 runs.** **Mandate — the one fact that does not fit the board's most consistent verdict**: every aggregate axis agrees (`wflow −0.280` · `eqflow −0.244` · breadth 0.00 · Δ −0.029 · exc20 −4.777 **and deteriorating**), **yet 4 of 12 names are accumulating — `EQIX` `DLR` `CBRE` `IRM`**, which is `M131`'s measured **data-centre unit**, not the tower/duration unit. ⚠ And `XLRE` is **the only duration leg that did NOT turn up on the 5-day window** (+0.246 vs `XLU` +1.207) while `P61` is removing the duration mechanism. **Resolve whether RE's UW is a duration call that has lost its driver, or a data-centre call the desk has never made** |

⚠ **Rotating slots are a DECLARED recency-starved deviation for a 4th consecutive run.** After the
delta the board holds **two OW-side sectors (ENRG, INDU)** and both are continuous, so **no third OW
exists** to rotate into. Both rotating picks are **N−/UW sectors chosen by recency + contradiction
width**, stated rather than smuggled.
⚠ **Tiebreak stated: `UTIL` was the runner-up for Rotating 2** — it carries the board's only **real**
(non-artifact) flow absence, 0 of 15 accumulating, against `XLU` exc5 +1.207. **RE won on recency
(8 runs vs 3).** `UTIL`'s mandate is logged in DEEP_LOG so the next run's recency rule sees it.
⚠ **IT is NOT given a slot despite being this run's sharpest contradiction** — covered **08-13, 2 runs
ago**, inside the recency exclusion. **Its contradiction is handed to PREMORTEM**, which is the
correct owner: *the sector's N+ rests on `eqflow` alone after a 95% Δ decay, its two admissible greens
are dated to their own earnings prints, its `wflow` is one name whose green is disqualified, and its
leading node (optical) has NO entry in a 28-day-stale cycle registry.* **That is an instrument-and-
exposure question, not a sector question.**
⚠ **No padding**: 4 of 4 slots filled, every one with a written mandate.

## DEEP_LOG 2026-08-15: continuous=[ENRG, INDU] rotating=[DISC, RE] · N=4/4 · **ONE verdict delta — ENRG OW−→OW, carried by `eqflow +0.102` and `breadth 0.12`, BOTH the highest of eleven and NEITHER cap-weighted, with the two-run Δ blocker narrowing 73% (−0.157 → −0.042); the counter-evidence is stated — Δ is still the 2nd-worst RANK of eleven** · **the promotion deliberately does NOT use `wflow` even though ENRG is not a flipper and `wflow +0.217` is the board's only positive, because `eqflow`/`breadth` are immune to the 31-day-stale caps** · **corroborated by three independent stages and NO macro re-argument: SWEEP (`MPC` = the only admissible 🟢 in the sector after the D261 velocity adjustment, FINRA z −0.71 clean-rise), EVENT_ALPHA Card 3 CONFIRMED-EARLY (named physical mechanism — Salavat 200kbpd refinery struck 08-13, fuel terminal 08-14, Russia diesel exports at a multiyear low; refiner RS60 +22~+29 vs integrateds −4~−7 = a 36-point spread inside one GICS sector), and CYCLE_EXPOSURE 🚨 GAP −0.898pp on that same node** · **flip list 3 of 11 — Information Technology/`NVDA`/19.4% · Industrials/`CAT`/**8.7%** · Materials/`LIN`/24.7%; ★Health Care EXITED (LLY no longer flips, `wflow` admissible again for the first time since 08-13); no verdict rests on any flipper's `wflow`** · **eight attempts declined with numbers: INDU OW−→OW (declined ON METHOD — the 25-of-50 accumulation count is a metric this run invented after seeing the data (C5), and every registered axis refuses: flipper ⇒ wflow inadmissible, eqflow −0.007, breadth 0.00, Δ −0.001 ⇒ the finding becomes the DEEP mandate, not the verdict), HLTH N→N+ (Δ −0.103 = now the WORST of eleven and a 4th consecutive negative, against eqflow +0.027 and XLV exc60 +7.803 = 2nd best, both named), DISC N−→UW (Δ +0.038 POSITIVE = wrong direction for a demote; declined in the direction attempted, and W5 flagged — ABNB RS60 +34.5 vs AMZN OBV 분산 and HD 🔴), COMM UW→any (both directions blocked AND the bucket changed membership — `EA` finally dropped out of the scored set, n 13→12, so its numbers moved by composition not demand: R56 changed shape rather than being fixed), UTIL UW→UW− (the board's ONLY real non-artifact flow absence, 0 of 15 accumulating — but XLU exc5 +1.207 = 2nd best of eleven and Δ +0.045 positive, price turning while flow does not, exactly what P61 predicts if the mechanism is dissolving), MATR N−→any (flipper LIN 24.7%; eqflow −0.114, breadth 0.00; P59 scored HIT — ex-NEM EW exc5 −2.097 with 1 of 11 positive while copper spec is 100th %ile long and FCX is the worst name at −4.894), FIN N−→any (M40's inversion has NOT repaired — eqflow −0.126 still below wflow −0.031, R69 stands; the exc60 +8.009 leg is a macro re-argument AND MACRO §A removes it anyway — 2s10s unchanged at +0.48, a 5bp PARALLEL shift not a steepening; ★M669 confirmed on a 2nd date — KKR, the alternatives/asset-management node, is the sector's only admissible 🟢), STPL UW−→deeper (declined on notation for a 2nd run, Δ +0.081 positive))** · **★the run's instrument headline binds every count here: `D261` REPLICATED AND WORSE — 6 of 11 🟢 (NFLX·NVDA·CVX·MRVL·CSCO·BAC) cannot be produced by OBV∧RS20>0∧vol_surge≥1.2 and all six carry a velocity value, so the admissible green count is 5 not 11 = a 3.2× over-representation of a 17.1%-coverage survivor sample (08-13 was 2.6×); CSCO is 🟢 on RS20 −4.7, negative, for the second run running** · **★and `M144` replicated a SIXTH time at record size — 110 names pass OBV 매집 ∧ RS20>0, 100 are blocked, and 100.0% of them by `vol_surge` alone; this run explains WHY for the first time: the whole tape is thin (median last-bar volume 0.732× then 0.649× the 20-day average) so the ratio's denominator carries a busier past and the gate closes board-wide at once ⇒ "breadth 0.00" this week is a statement about VOLUME, not demand (`D270`)** · **rotating slots are a DECLARED recency-starved deviation for a 4th run — after the delta only two OW-side sectors exist and both are continuous** · **IT deliberately NOT given a slot (covered 08-13 = 2 runs) — handed to PREMORTEM as an instrument-and-exposure question** · **UTIL was Rotating 2's runner-up, lost on recency (3 runs vs RE's 8), mandate logged here** · uncovered=[**IT(N+, HELD but the basis decayed 95% — Δ +0.152→+0.007, N+ now rests on `eqflow +0.044 > wflow +0.023` alone; ★both admissible greens COHR/LITE are dated by EVENT_ALPHA Card 2 to their OWN 08-11/08-12 earnings prints ⇒ reaction volume, not accumulation; RSPT beats XLK on all three windows (+1.343/+3.213/+5.927 vs SPY) so the breadth leg is real; NDX spec at the 0th percentile short; 🚨cycle_registry has NO ENTRY for optical/interconnect (28 days stale, D250) — the desk's registry does not contain the cycle owning its two best-scoring names; S85 settles 08-21 and reads +1.343 = branch C; covered 08-13, first rotating pick next run on recency)**, **HLTH(N, covered 08-13 = 2 runs; Δ −0.103 worst of 11 and 4th consecutive negative, but 15 of 32 accumulating so the 0.00 breadth is an artifact; S76 08-19, S82 08-20)**, **MATR(N−, covered 08-13 = 2 runs; P59 HIT twice; S77 08-19)**, **UTIL(UW, covered 08-12 = 3 runs; ★the board's ONLY real flow absence — 0 of 15 accumulating — against XLU exc5 +1.207 and a MECHANISM that P61 may be removing; S80 08-19; runner-up for Rotating 2)**, **STPL(UW−, covered 08-10 = 5 runs; Δ +0.081; D249 makes it the 252-day third duration leg)**, **COMM(UW, covered 08-14 = 1 run; Δ +0.092 best of 11 for a 2nd run but the bucket lost EA this run so composition changed; XLC exc60 −8.311 worst of 11)**, **FIN(N−, covered 08-14 = 1 run; R69 stands, M669's relocated breadth node KKR is the only admissible 🟢; S78 08-19)**]

## ✅ EXIT CHECK
- [x] **§1 is ONE line**, inherited verbatim from MACRO §G. No unchanged sector gets a row or a
      restated flow number.
- [x] **Every §2 delta cites a flow number** — the single carried delta (ENRG) is carried by
      **`eqflow +0.102` and `breadth 0.12`**, both the highest of eleven and both non-cap-weighted,
      plus the Δ improvement. **The macro leg (`P62`, `XLE exc5`) is named as context and explicitly
      declined as the carrier.**
- [x] 🚨 **No promotion or demotion rests on a `top1_flips_sign` bucket.** The full flip list is
      reproduced in §0 even though Health Care's exit is the only change; **INDU and MATR attempts
      were declined with `wflow` named as inadmissible**, and the ENRG promotion — on a
      **non**-flipper — still avoids `wflow` by choice, with the reason given.
- [x] **The axis count is stated** (`n_axes = 3`), and **no delta cites theme freshness or news
      velocity.** Every green count in this file is the **`D261`-adjusted** one (5, not 11).
- [x] **AGREE/DIVERGE named explicitly** — 1 carried, **8 declined with their numbers**, and each
      declined attempt records the *direction attempted* so a future run can see what was tried.
- [x] **DEEP_LOG appended** with all four slots, every uncovered sector, its last-covered date and its
      dated brackets — including the **runner-up tiebreak** and the reason IT was excluded.
- [x] **No padding** — 4 of 4 slots, each with a written mandate; **INDU's promotion was declined on
      method while its finding was promoted to the mandate**, which is the honest split.
