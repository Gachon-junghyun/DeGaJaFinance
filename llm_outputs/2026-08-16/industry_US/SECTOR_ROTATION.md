# SECTOR_ROTATION — industry_US · 2026-08-16 · Stage 6/11 (L1·ROTATION)

> **Delta-only.** MACRO owns the 11-sector matrix; `SECTOR_FLOW_US.json` owns the numbers. Both are on
> disk. This file writes **only what changes and why**. Benchmark **`SPY`** named inline (C1).

## §1 · Inherited — one line, verbatim

`ENRG OW · INDU OW− · IT N+ · HLTH N · FIN N− · MATR N− · DISC N− · COMM UW · STPL UW− · UTIL UW · RE UW`

## §2 · Deltas — **ZERO this run, and that is the measured verdict, not an omission**

### 2a · Why no delta is possible on a flow number today

The stage's own rule: *"A delta must be carried by a flow number… If the only reason to move a sector
is a macro argument, leave it and say so."* Measured this run:

| Test | Result |
|---|---|
| Names with an identical `last` price vs the prior run | **299 / 299** |
| Names whose `flow_score` changed | **0 / 299** |
| Sector `wflow` / `eqflow` / `breadth` rows that changed | **0 / 11** (identical to 3dp) |
| Sessions settled since the prior `industry_US` run | **0** |

⇒ **Every flow input that could carry a delta is byte-identical to the one that produced yesterday's
verdicts.** Moving a sector today would be **thrash on unchanged numbers** — the exact failure
`HANDOVER §2` warned this stage about before it opened.

### 2b · The one thing that DID change is not admissible as a delta

The 🟢 count moved **11 → 9** (`NVDA` and `MRVL` dropped out) with **zero price change**. The cause is
exact: `NVDA` velocity **1.20 → 1.16**, `MRVL` **1.20 → 1.10**, both crossing the 1.2 gate, while OBV,
RS20, `vol_surge` and `flow_score` are identical to the digit for both.
🚫 **Inadmissible, twice over**: (i) PREFLIGHT G1 revokes citation of the velocity axis
(coverage **16.7%**, survivor set monotone-nesting); (ii) both names have `vol_surge` **0.73 / 0.48**,
so **neither could ever have been green on the 3-axis path** — they were velocity-only greens.
⇒ **`NVDA`, the G3 flipper that owns IT's entire `wflow` sign, lost its 🟢 to a 4-basis-point move in an
article-count ratio on a day no market was open.** That is an instrument event. **No verdict moves on it.**

### 2c · Attempts considered and declined, each with its number

| Sector | Attempted | Declined because |
|---|---|---|
| **INDU** OW− → **OW** | SWEEP: **25 of 50 accumulate (`OBV 매집 ∧ RS20>0`) — the board's HIGHEST count, above IT's 22 of 56** — while the sector produced **zero** shortlist names, **100% blocked by `vol_surge` alone**. EVENT_ALPHA Card 6 adds a dated narrative (NATO shootdowns over **Latvia 08-14** and **Romania 08-16**) | 🚫 **Declined on method for a 2nd consecutive run, and the reason is unchanged**: the accumulation count is a **metric this desk invented after seeing the data (C5)**, and every registered axis refuses — **G3 flipper (`CAT`) ⇒ `wflow` inadmissible**; `eqflow` **−0.007**; `breadth` **0.00**; Δ **−0.001**. ⚠ **And the numbers are the same numbers as yesterday** — declining twice on identical data is one decision, not two. ⇒ **Held at OW−; the finding is the DEEP mandate** |
| **UTIL** UW → **UW−** | ★ SWEEP §4: **0 of 15 pass `OBV 매집 ∧ RS20>0` — the ONLY zero on this board that survives the `vol_surge` correction**, i.e. the only sector where "the money is not there" is a measurement rather than a volume artifact. `eqflow −0.433` (worst of eleven). EVENT_ALPHA Card 5: the AI-power narrative is syndicating hard (**5 outlets 08-16**) onto names the tape is **dispersing** (`NEE` 🔴 · `VST` 🔴 · `GEV` 🔴) | 🚫 **Declined — and the reason CHANGED this run, which is why it is written out.** Yesterday it was declined on `XLU` exc5 **+1.207** (2nd best of eleven) and Δ **+0.045**. Today **`P65` adds a second, independent reason**: the long-end move is a **BULL steepener** (30y−10y 0.53→0.58 **while `DGS30` FELL and `DGS2` fell 10bp**), not a term-premium level rise. **A falling front end is a friendlier rate backdrop for regulated utilities than the mechanism this UW was written under.** ⇒ **A notch down into a mechanism that is dissolving is not a measurement.** Held at UW, and the mandate goes to DEEP |
| **RE** UW → any | 4 of 12 accumulate (`EQIX` `DLR` `CBRE` `IRM` = `M131`'s measured data-centre unit); EVENT_ALPHA Card 4 supplies a candidate driver (**$70bn of AI shadow-credit backstops**, `bloomberg` 08-15) | 🚫 **Declined in both directions.** Every aggregate axis still agrees with the UW (`wflow −0.280` · `eqflow −0.244` · breadth 0.00 · exc20 −4.777 vs **`SPY`**), and the promotion case is a **credit** argument whose own instrument is flat (`HY OAS` **2.71% = 10.3rd percentile, unchanged 5 sessions**). ⇒ **A macro re-argument does not qualify as a delta** (the stage's own rule, and the 2026-07-21 precedent it cites) |
| **DISC** N− → **UW** | EVENT_ALPHA Card 7 hardens the driver: *"US retail sales post first decline in nine months"* (08-14) + **`WMT`·`HD`·`TGT` all report this week**; `HD` **🔴분산**, `COST` **🔴분산**, `AMZN` OBV **분산** | 🚫 **Δ is +0.038 — POSITIVE.** A deepening underweight needs a negative delta, and the number has not moved. ⚠ **W5 blocks it independently**: `ABNB` (**🟢가속**, RS60 **+34.5** vs `SPY`, 3-axis producible, FINRA clean-rise z −0.94) and `HD` (🔴분산) sit in **one GICS label**. The label cannot express the goods/services split, so a label-level verdict would be measuring the wrong object |
| **IT** N+ → any | `eqflow +0.044 > wflow +0.023` still holds | 🚫 **G3 flipper (`NVDA`, 19.4%) ⇒ `wflow` inadmissible in either direction.** ⚠ **And its basis is now decayed AND instrument-dependent**: the 08-14 promotion rested on an `eqflow` sign-flip **and** Δ +0.152; Δ is now **+0.007** (95% decay, unchanged since yesterday), so N+ rests on `eqflow > wflow` **alone** — a gap of **0.021 flow points**. Its own falsifier `S85` settles **08-21** and reads **+1.343 = branch C**. **Held, and handed to DEEP** |
| **ENRG** OW → any higher | Card 1: **five dated Russian refining strikes in six days**, Russia at a multiyear-low diesel export, SPR near a cavern-damage threshold | 🚫 **No notch above OW is defined on this board.** ⚠ And the promotion's own counter-evidence stands unchanged: **Δ is still the 2nd-worst rank of eleven**. ✅ What is new is **narrative, not flow** — correctly recorded as a DEEP mandate and as `P66`, not as a verdict |
| **HLTH · FIN · MATR · COMM · STPL** | — | 🚫 All five inherit yesterday's declines on **identical numbers**. HLTH: Δ **−0.103**, worst of eleven, 4th consecutive negative. FIN: `eqflow −0.126` still **below** `wflow −0.031` ⇒ `R69` stands; ★ **and `P65` removes the steepener rescue — a BULL steepener with the front end falling is not the NII geometry `M138` describes.** MATR: flipper (`LIN`); `eqflow −0.114`. COMM: both directions blocked **and the bucket changed membership** (`EA` left the scored set). STPL: declined **on notation** for a 3rd run — UW− is this board's floor |

**⇒ Verdict delta count: 0.** ★ **Stated positively**: on a board where nothing was observed, the
correct output is nothing moved — and the value this stage added is the **five declines whose reasons
are now on record with numbers**, one of which (`UTIL`) changed its reason.

---

## §3 · DEEP picks and DEEP_LOG — **N = 4** (protocol budget: 2 continuous + 2 rotating)

**Recency clock** — last DEEP by sector: ENRG 08-15 · INDU 08-15 · DISC 08-15 · RE 08-15 · COMM 08-14 ·
FIN 08-14 · **IT 08-13 · HLTH 08-13 · MATR 08-13** · **UTIL 08-12** · **STPL 08-10**.

| Slot | Sector | Why, and the mandate |
|---|---|---|
| **Continuous 1** | ★ **ENRG (OW — the board's top OW)** | **Anti-thrash APPLIED** (continuous 08-13 · 08-14 · 08-15 · today). **Mandate — the one thing that moved this run is on this sector, and it is narrative:** ① **`P66` / Card 1**: five dated strikes on Russian refining in six days (08-10 · 08-11 · **08-13 Salavat 200kbpd** · 08-14 terminal · 08-14 Russia admits petrol shortages), Russian diesel exports at a **multiyear low**, Russia **importing Indian fuel** — resolve whether the desk's own crack series corroborates a *physical* supply-destruction mechanism or merely a price move. ② **Score the OTHER branch with equal weight**: *"Kyiv stops strikes on Russian port after request from JD Vance"* [`semafor` 08-12] — **a named US actor is braking the exact mechanism**. ③ **`D251` again**: `PSX` and `VLO` carry the sector's #2 and #3 RS60 vs `SPY` (+22.3 / +24.3) and are 🟡 on **`vol_surge` 1.01 / 0.84 alone** — the two names leading the sector are filtered out of its own shortlist for a 2nd run. ④ **The `CYCLE_EXPOSURE` GAP is −0.898pp on this exact node** — identical to yesterday, so resolve whether the epicenter is refiners or integrateds given the **36-point RS60 spread** |
| **Continuous 2** | **INDU (OW−)** | **Anti-thrash APPLIED** (continuous 08-12 · 08-13 · 08-14 · 08-15). **Mandate is `D249`, unresolved for a 5th run, and it now has THREE objects inside one label**: ① the bracket measures **`XLI`**, the position is **defense**; ② SWEEP: **25 of 50 accumulating — the board's highest — 100% blocked on volume**, and the accumulating half is aero/defense + electricals (`M667`); ③ **Card 6**: NATO shot down drones over **Latvia (08-14, 10 outlets)** and **Romania (08-16)**, yet the closest chain fit (`LHX`, C4ISR/EW) has the **weakest tape of the five** (RS20 −1.0) while `LMT` (+15.2) and `RTX` (+10.8, held) lead. **Resolve which object the OW− is on, and whether `HII`'s absence from `us_top300` is material.** ★ **This is the 5th run of the same question — either close it or say in writing why it cannot be closed** |
| **Rotating 1** | ★★ **IT (N+)** | **Pre-committed by the 08-15 DEEP_LOG** (*"covered 08-13; first rotating pick next run on recency"*) — honoured. **Mandate — the sector where the instrument and the story collided this run**: ① **its N+ now rests on a 0.021 flow-point gap** (`eqflow +0.044` vs `wflow +0.023`) after a **95% Δ decay**; ② ★ **Card 2 — Microsoft's Maia 300 (300,000-unit target, unveil "as early as September") and *"Microsoft Rethinks Its Nvidia Reliance"*** — a **substitution** story aimed at the sector's largest name, with `MRVL` named as beneficiary. **Sourcing is `[news]`-only** (*"The Information, Report Says"*) — **find or fail to find a primary**; ③ **`NVDA` and `MRVL` both lost their 🟢 this run on velocity alone with zero price change** — establish that no fundamental read may rest on that; ④ **the only two admissible 🟢 in the sector are `COHR` and `LITE`** (optical/interconnect), the layer **neither** side of the substitution touches — and **`cycle_registry.json` has NO ENTRY for optical/interconnect OR custom AI silicon and is 29 days stale (`D250`)**; ⑤ `S85` settles **08-21** at branch C |
| **Rotating 2** | ★★ **UTIL (UW)** | **Recency: last covered 08-12 = 4 runs, and it was Rotating 2's runner-up last run** (lost to RE on recency). **Mandate — this is the board's cleanest signal and its most contested mechanism at the same time**: ① ★ **0 of 15 accumulating — the ONLY zero on the board that survives the `vol_surge` correction.** Establish whether that is a genuine capital-flight read or a sector-composition property; ② ★★ **`P65` changes the mechanism under the UW for a SECOND time**: the long-end move is a **bull steepener** (30y−10y **0.53 → 0.58** while `DGS30` **fell** and `DGS2` fell **10bp**), so the term-premium story the UW was written under is half-refuted — **a falling front end is a tailwind for regulated utilities**; ③ **Card 5**: the AI-power narrative is syndicating at **5 outlets** onto `NEE`/`VST`/`GEV`, **all three 🔴분산** — resolve whether the UW is a *rates* call, a *crowding* call, or a *merchant-vs-regulated* call, because those have different kills; ④ `XLU` exc5 **+1.207 vs `SPY` = 2nd best of eleven** — **price turned while flow did not**, and `S80` settles **08-19** |

### Declared deviations, stated rather than hidden

1. 🚨 **`STPL` is the longest-uncovered sector on the board (08-10 = 6 runs) and was NOT given a slot.**
   Declined with a reason: its mandate is empty — Δ **+0.081 (positive)**, UW− is this board's defined
   floor, **3 of 19 accumulating (the board's lowest share, which agrees with the verdict)**, and no
   dated catalyst. **A DEEP slot spent on a sector with nothing to resolve is a slot wasted**, and the
   recency rule exists to prevent blind spots, not to force coverage. **Logged so the next run's recency
   rule sees a 7-run gap and weighs it against a real mandate.**
2. **Rotating slots are a recency-starved deviation for a 5th consecutive run.** After the verdicts,
   only **two OW-side sectors exist (ENRG, INDU)** and **both are continuous**, so there is no third OW
   to rotate into. Both rotating picks are N+/UW sectors chosen by **recency + contradiction**, and that
   is stated rather than presented as the rule working.
3. **`HLTH` and `MATR` (both 08-13 = 3 runs) lost the rotating tiebreak to `IT`** — `IT` on the 08-15
   pre-commitment, `UTIL` on a 4-run gap plus a mechanism that changed under it this run. Their pending
   falsifiers (`S76`/`S82` for HLTH, `S77` for MATR) settle **08-19/08-20** and will score without a DEEP.

---

## DEEP_LOG 2026-08-16: continuous=[ENRG, INDU] rotating=[IT, UTIL] · N=4/4 · **ZERO verdict deltas — and the zero is measured, not assumed: 299/299 names carry an identical `last` price, 0/299 changed `flow_score`, 0/11 sector rows changed to 3dp, and 0 sessions settled since the prior run, so no flow number capable of carrying a delta moved** · **the ONE thing that changed is inadmissible: the 🟢 count fell 11→9 because `NVDA` velocity 1.20→1.16 and `MRVL` 1.20→1.10 crossed the 1.2 gate with every price input identical to the digit — and both carry `vol_surge` 0.73/0.48 so neither could EVER be green on the 3-axis path ⇒ `NVDA`, the G3 flipper owning IT's entire `wflow` sign, lost its 🟢 to a 4bp move in an article-count ratio on a day no market was open (`D261` demonstrated, not argued)** · **flip list 3 of 11 — Information Technology/`NVDA`/19.4% · Industrials/`CAT`/8.7% · Materials/`LIN`/24.7%, identical set and identical numbers to 08-15 which is ONE observation read twice, not a structure confirmed; no verdict rests on any flipper's `wflow`** · **`D261` decomposition on today's greens: 5 of 9 are 3-axis producible (`COHR`·`KKR`·`ABNB`·`LITE`·`MPC`), 4 are not (`NFLX`·`CVX`·`CSCO`·`BAC`) and all four carry velocity ⇒ admissible green count is 5 not 9, a 2.66× over-representation of a 16.7%-coverage survivor sample (08-15 3.19× · 08-13 2.6×, third replication); `CSCO` is 🟢 on RS20 −4.7 for a third run** · **`M144` replicated a SEVENTH time: 110 pass `OBV 매집 ∧ RS20>0`, 102 are not 🟢, 100.0% of them blocked by `vol_surge` alone — and `D270`'s explanation survives re-measurement (median last-bar volume 0.649× after 0.732×, so the ratio's denominator carries a busier past and the gate closes board-wide at once ⇒ "breadth 0.00" this week is a statement about VOLUME, not demand)** · **seven attempts declined with numbers: INDU OW−→OW (declined ON METHOD for a 2nd run — the 25-of-50 accumulation count is a C5 invented metric and every registered axis refuses: flipper ⇒ wflow inadmissible, eqflow −0.007, breadth 0.00, Δ −0.001; ⚠ declining twice on IDENTICAL data is one decision not two), UTIL UW→UW− (★the reason CHANGED — yesterday it was `XLU` exc5 +1.207 and Δ +0.045; today `P65` adds that the long-end move is a BULL steepener with `DGS2` falling 10bp, so the term-premium mechanism the UW was written under is half-refuted and a notch down into a dissolving mechanism is not a measurement), RE UW→any (declined both ways — every aggregate axis agrees with the UW and the promotion case is a CREDIT argument whose own instrument is flat at HY OAS 2.71% = 10.3rd percentile unchanged 5 sessions ⇒ a macro re-argument does not qualify as a delta), DISC N−→UW (Δ +0.038 POSITIVE = wrong direction, and W5 blocks it independently — `ABNB` 🟢가속 RS60 +34.5 vs SPY and `HD` 🔴분산 are in ONE GICS label), IT N+→any (flipper ⇒ wflow inadmissible both ways; N+ now rests on a 0.021 flow-point gap after a 95% Δ decay; `S85` 08-21 reads +1.343 = branch C), ENRG OW→higher (no notch above OW is defined; what is new is NARRATIVE not flow — five dated Russian refinery strikes in six days ⇒ recorded as `P66` and a DEEP mandate, not a verdict), HLTH/FIN/MATR/COMM/STPL (all inherit yesterday's declines on identical numbers; ★`P65` additionally removes FIN's steepener rescue — a bull steepener with the front end FALLING is not the NII geometry `M138` describes)** · **★the run's structural headline binds this whole file: THREE of the desk's four macro instruments returned data identical to the prior run (equity tape 08-14, `[FRED]` 08-13, COT Tue 08-11) and only the news corpus moved (+1,855 articles) ⇒ this stage's correct output is zero deltas and five documented declines, and the value added is that one decline's REASON changed** · **`CYCLE_EXPOSURE` 🚨 GAP on rank-2 Energy epicenter 7.1% vs 8.0% floor = −0.898pp, identical to 08-15 to three decimals (the book did not trade and prices did not move) — handed to ALPHA; rank-1 AI-compute clears at 16.54% vs a 12.0% floor; rank-3 missile-defense has NO floor set ⇒ ⚪n/a, which is `D250`: the registry is 29 days stale and has no entry for EITHER cycle this desk actually found (optical/interconnect, custom AI silicon)** · **`STPL` deliberately NOT given a slot despite being the longest-uncovered sector (08-10 = 6 runs) — declined because its mandate is empty (Δ +0.081 positive, UW− is the defined floor, 3 of 19 accumulating agrees with the verdict, no dated catalyst); logged so the next run sees a 7-run gap and weighs it against a real mandate** · **rotating slots are a DECLARED recency-starved deviation for a 5th run — after the verdicts only two OW-side sectors exist and both are continuous** · **`IT` given Rotating 1 on the 08-15 DEEP_LOG's own pre-commitment; `HLTH`/`MATR` (both 08-13 = 3 runs) lost the tiebreak and will score via `S76`/`S82`/`S77` on 08-19/08-20 without a DEEP** · uncovered=[**HLTH(N, 08-13 = 3 runs; Δ −0.103 worst of eleven and 4th consecutive negative, but 15 of 32 accumulating so the 0.00 breadth is a `vol_surge` artifact; `XLV` exc60 +7.803 vs SPY = 2nd best of eleven; S76 08-19, S82 08-20 already at +3.091 above its branch A)**, **MATR(N−, 08-13 = 3 runs; flipper `LIN` 24.7%, eqflow −0.114, 6 of 12 accumulating so the absence is `unknown` (C3) not evidence; copper spec 100th %ile long; S77 08-19)**, **FIN(N−, 08-14 = 2 runs; `R69` stands, eqflow −0.126 still below wflow −0.031; `KKR` is the only admissible 🟢 and is `M669`'s relocated alternatives/asset-management breadth node; ★`P65` removes the steepener rescue; S78 08-19)**, **COMM(UW, 08-14 = 2 runs; Δ +0.092 best of eleven but the bucket lost `EA` from the scored set so its numbers moved by composition; `XLC` exc60 −8.311 worst of eleven; `NFLX` is the run's only `new_green` and it is velocity-produced ⇒ not an ignition)**, **DISC(N−, 08-15 = 1 run; Δ +0.038 positive blocks the demote; W5 split `ABNB` +34.5 vs `HD` 🔴; `WMT`/`HD`/`TGT` all report this week and `CATALYST_WATCH` carried ZERO of them)**, **RE(UW, 08-15 = 1 run; every aggregate axis agrees yet 4 of 12 accumulate = `M131`'s data-centre unit; Card 4's $70bn shadow-credit story is the candidate driver and `P67` settles 08-28)**, **STPL(UW−, 08-10 = 6 runs, the board's longest gap, deliberately declined — see above)**]

---

## ✅ EXIT CHECK

- [x] **§1 is one line, verbatim** — no per-sector prose for anything not changing.
- [x] **§2 is deltas only, and the delta count is 0** — with the four-row measurement that shows why no
      flow number capable of carrying a delta exists today (§2a).
- [x] **Every attempted move is declined with a number**, not with prose (§2c) — seven attempts, and the
      one whose *reason changed* (`UTIL`) is called out as changed rather than restated.
- [x] 🚨 **No verdict rests on a `top1_flips_sign` bucket's `wflow`** — IT, Industrials and Materials are
      all blocked in both directions and the block is stated each time.
- [x] **No delta rests on a macro re-argument** — the RE promotion case was declined **specifically**
      on that ground, citing the stage's own 2026-07-21 precedent.
- [x] **N-DEEP selection by rule, not by gut** — 2 continuous (anti-thrash, both stated), 2 rotating
      (one honouring the prior run's written pre-commitment, one on a 4-run recency gap + a mechanism
      that changed). **Not padded to N with an empty mandate**: `STPL` was declined *despite* being the
      least-recently-covered, with the reason written out.
- [x] **DEEP_LOG appended** with all four slots, every uncovered sector, its last-covered date, its
      pending falsifier and its settle date.
- [x] **No sizing, no buy/sell language** (P4).
