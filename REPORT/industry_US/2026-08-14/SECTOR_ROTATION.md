# SECTOR_ROTATION — industry_US · 2026-08-14 · Stage 6/11 (L1·ROTATION)

> **Delta-only.** MACRO owns the 11-sector verdict; `SECTOR_FLOW_US.json` owns the flow numbers.
> Both are on disk. This file writes **only what changes and why.** Analytical only, zero buy/sell (P4).

## §0 · The axis count this run scored on — read before any number below

`SECTOR_FLOW_US.json §scoring`: **`n_axes` 3 · `vel_coverage` 0.170 · `scored` 300 ·
`dropped_missing_axis` 0.** ⇒ **No delta below cites theme freshness or news velocity.** None does.

★ **Two constraints LIFTED, one ADDED — and the added one is new to this desk:**
1. ✅ **Δ is valid and one-session-clean.** Baseline `history.json["2026-08-12"]`, same mode
   (`nonews` / 3-axis), **300/300 names carry a Δ** (PREFLIGHT **G2 PASS**). "Δ vs the prior session"
   is literally true.
2. ✅ **The price bar is new and settled** — 2026-08-13, last-bar volume **0.732×** the 20d average,
   `SPY` carrying the same terminal date (PREFLIGHT **G0 PASS**).
3. 🚨 **NEW — the 🟢 TAG is contaminated and the `flow_score` is NOT** (`SWEEP_READ.md §2`).
   **5 of the 11 🟢 tags — `CSCO` `DELL` `CVX` `NVDA` `BAC` — cannot be produced by the 3-axis rule**
   (their `vol_surge` is 1.26 / **0.78 / 0.93 / 0.76 / 0.73** and `CSCO`'s RS20 is **−0.1**); each
   carries a velocity value, so only the **revoked** axis can be lighting them.
   ⇒ **Every green/red count below is the ADJUSTED count.** ★ Crucially, `flow_score` — and therefore
   **`wflow`, `eqflow` and `Δ` — are 3-axis and CLEAN**; only the tag is 4-axis. That is why every
   delta in §2 rests on `eqflow`/`Δ`, and none rests on a green count alone.

🚨 **Flip list, reproduced in full even where it changes nothing** (`top1_flips_sign`) — **3 of 11,
up from 2, and the new entrant is the board's largest sector**:

| Sector | wflow | ex-top1 | top1 | top1_w | n |
|---|---|---|---|---|---|
| **Information Technology** | **+0.016** | **−0.078** | `NVDA` Nvidia | 19.4% | 56 |
| **Health Care** | **−0.012** | **+0.002** | `LLY` Lilly (Eli) | 19.4% | 32 |
| **Materials** | **−0.179** | **+0.016** | `LIN` Linde | 24.7% | 12 |

**No verdict below rests on the `wflow` of any of the three.** Industrials came **OFF** the list
(`wflow −0.046`, `CAT` no longer flips it).
⚠ **The IT entry is the run's sharpest single fact**: the board's only non-Energy positive `wflow` is
**one name**, and **that name's own 🟢 is one of the five §0.3 disqualifies.**
⚠ `top1_w` weights come from a **30-day-old** market-cap file (PREFLIGHT G5).

## §1 · Inherited — one line, verbatim

**MACRO holds:** `INDU OW− · ENRG OW− · FIN N · IT N · HLTH N+ · DISC N− · MATR N− · COMM UW ·
UTIL UW · STPL UW− · RE UW`.

## §2 · Deltas — **THREE**, each carried by a non-cap-weighted flow number

| Sector | matrix said | flow evidence (Δ = 1 session, 08-12→08-13) | new verdict | who resolves |
|---|---|---|---|---|
| **Information Technology** | **N** | ★ **`eqflow` FLIPPED SIGN: −0.100 → +0.034** in one settled session · **Δ +0.152 = 2nd best on the board** · `eqflow` **>** `wflow` (+0.034 vs +0.016) ⇒ the median name beats the megacaps · adjusted **2🟢 / 10🔴 of 56** | ★ **N+** | **PREMORTEM** (not DEEP — see §3) |
| **Health Care** | **N+** | **Δ −0.228 = the WORST on the board**, and it is the **third consecutive deceleration** (+0.157 → −0.014 → **−0.228**) · **0🟢 / 3🔴 of 32** · breadth **0.00** | ★ **N** | **`S76` (08-19) · `S82` (08-20)** |
| **Financials** | **N** | ★ **`eqflow` −0.144 is now WORSE than `wflow` −0.066** — the breadth premium this desk has carried since 07-23 (M40: eqflow +0.320 > wflow +0.253) has **INVERTED** · `eqflow` deteriorated **−0.065 → −0.144** in one session · Δ −0.055 · adjusted **2🟢 / 9🔴 of 47** | ★ **N−** | **DEEP-FIN (rotating slot 2)** |

### 2a · Why the IT promotion is legal, and why it is only ONE notch

08-13 **declined** IT N→N+ with the numbers: *"`wflow` −0.136 **AND** `eqflow` −0.100 both negative on
a NON-flipper."* **Both halves of that blocker have changed in one settled session**: `eqflow` is now
**+0.034** and IT has **become** a flipper, which removes `wflow` from the argument entirely.
⇒ **The promotion rests on the one axis that is both admissible (not cap-weighted) and clean
(3-axis, unaffected by §0.3), plus the board's 2nd-largest Δ.**

⚠⚠ **And the counter-evidence, stated rather than buried — it is substantial:**
- **Adjusted greens are 2, not 5** (`COHR` `LITE`); `CSCO` `DELL` `NVDA` are disqualified.
  **2🟢 against 10🔴** is the count, and it points the other way from `eqflow`.
- **`wflow +0.016` is `NVDA` alone** — ex-top1 it is **−0.078** (§0 flip list).
- ⇒ **the notch is ONE step (N → N+), not two**, and it is explicitly **not** a call that IT's breadth
  is healthy. It is a call that the **median IT name stopped getting worse and turned**, which is what
  `eqflow` measures and what the count does not.
⚠ **S1**: the Δ is one session. ⚠ **Corroborating, independent of the sweep**: `XLK` is the **only
sector positive on all three price windows** vs `SPY` (exc5 **+1.723** · exc20 **+3.846 = best of 11**
· exc60 **+4.101**), and **Nasdaq-100 spec sits at the 0th percentile of a year** (crowded short).

### 2b · Why the HLTH demote is legal on a flipper bucket

HLTH **is** on the flip list (`LLY` 19.4%), so **`wflow −0.012` is inadmissible and is not used.**
The demote is carried by **Δ −0.228** and the **green count of zero** — neither is cap-weighted.
⚠ **The one contrary axis is named**: `eqflow` is **+0.019**, i.e. positive, and **`XLV` exc60 is
+10.239, the best of 11**. ⇒ **this is a demote of the CHANGE, not of the level.** A sector can be the
60-day leader and the worst decelerator at once, and today HLTH is both.
⚠ It is also **one notch (N+ → N), not two**, for exactly that reason. **`S82` (08-20) is the
registered instrument** for whether HLTH is idiosyncratic or the 4th leg of the duration complex.

### 2c · Why the FIN demote is a REVERSAL of a carried claim, not a drift

`M40` (2026-07-23) established Financials as *"the board's only breadth-led sector"* — `eqflow +0.320`
**above** `wflow +0.253`. **That ordering is now reversed**: `eqflow −0.144` sits **below**
`wflow −0.066`, i.e. **the median financial is worse than the cap-weighted sector.**
⇒ **any Financials thesis resting on breadth must be re-justified, not carried** — which is why this
sector takes a DEEP slot rather than only a notch.
⚠ **Counter-evidence, stated**: `XLF` exc60 is **+7.290, 2nd best of 11**, and `S51` **CONFIRMED** the
NIM mechanism while 2s10s steepened to **+0.48** with 30y−10y at **+0.56** (MACRO §A-1) — a long-end
steepener is a bank positive. **That is a macro argument and under this stage's rules it may not
carry or block a delta** (the 2026-07-21 measured failure). It is logged as the DEEP mandate instead.
⚠ **S1**: one session; **one notch.**

## §2d · Changes CONSIDERED and DECLINED — with the numbers, not with silence

| Sector | attempted | declined because |
|---|---|---|
| **ENRG** OW− → **OW** | the board's **only positive `wflow` (+0.259)**, `eqflow +0.099`, breadth 0.12, **not a flipper** ⇒ fully admissible | 🚫 **Δ is −0.157, the board's 2nd worst.** The level is best-in-class and the *change* is nearly worst-in-class — a promotion on a decaying delta is what the anti-thrash rule exists to stop. ⚠ Also `XLE` **exc60 −4.519** and **`S67` scored `FIRED-C` today at median RS20 +11.925, 1.635pp short of its own with-us branch** ⇒ **this desk's ENRG promotion is still neither confirmed nor falsified.** Held at OW− for a **2nd consecutive run on the same reasoning** |
| **COMM** UW → **UW−** | Δ **+0.185 = the BEST on the board**; `eqflow −0.107` far better than `wflow −0.523` | 🚫 **The Δ points the WRONG WAY for a demote** — a deepening UW needs a negative delta and this is the board's largest positive. **Declined in the direction attempted.** ⚠ **And a promotion is equally blocked**: `XLC` exc60 **−9.098 = worst of 11** and FINRA short z **+2.15 with a +12.4▲ trend = the steepest short surge of the eleven**. ⇒ **C3 — the axes disagree in sign, so there is no signal in either direction.** Handed to DEEP (rotating slot 1) |
| **MATR** N− → **N** | ex-top1 `wflow` **+0.016** (positive) | 🚫 **Flipper (`LIN` 24.7%) — `wflow` inadmissible.** The permitted axes all refuse: `eqflow` **−0.130**, breadth **0.00**, **0🟢/4🔴**, Δ **−0.073**. ⚠ And the price side agrees with the refusal: **ex-NEM EW exc5 −1.893 with 1 of 12 positive** (MACRO §C-2). **`S77` settles 08-19** |
| **UTIL** UW → **UW−** | Δ **−0.092**, 0🟢/9🔴, `wflow −0.491` = worst of 11 | 🚫 **Redundant on an unchanged floor**, and **one axis points the other way**: `XLU` **exc5 +0.309, positive**, while `S71` scored **`FIRED-C`** (the CPI→PPI reversal was **−0.472pp, inside band**). ⚠ Also **P56 changed UTIL's stated MECHANISM (policy rate → long-end term premium) without changing its sign** — a mechanism change is not a notch |
| **DISC** N− → **N** | FINRA short z **−1.61, the board's ONLY short-covering signal** (5v5 −9.3▼) | 🚫 **A positioning axis is not a demand axis (D6).** The demand axes refuse: `eqflow −0.174`, `wflow −0.416`, Δ −0.042, **1🟢/9🔴**. ⚠ **The 08-13 demote is not reversing** — it is flat. Logged to the missed ledger instead (EVENT_ALPHA §2) rather than acted on |
| **STPL** UW− → deeper | Δ **−0.221 = 2nd worst on the board** | 🚫 **Declined on notation, and the reason is stated rather than fudged**: UW− is already this board's floor for a non-DEEP sector and there is no defined step below it. The Δ is **logged in DEEP_LOG** so the next run sees it. ⚠ ★ **And `D249` binds here**: at 252 days **STPL — not FIN — is the measured third leg of the duration complex** (`S63`), so a STPL move would be a P56 move wearing a defensive label |
| **INDU** OW− → any | came **OFF** the flip list ⇒ `wflow −0.046` admissible again | 🚫 **No change carried**: `eqflow −0.026`, Δ −0.044, **0🟢/10🔴 of 50** — all mildly negative, none decisively. ⚠ **`D249` unresolved**: the desk's live bracket measures `XLI` while the actual position is **defense** (defense EW exc20 **+7.81** vs XLI **+0.89**). **Held at OW− and handed to DEEP-INDU** |
| **RE** UW → any | — | 🚫 **The most internally consistent verdict on the board**: `wflow −0.252` · `eqflow −0.224` · breadth **0.00** · Δ −0.079 · exc20 **−4.366** — every axis agrees. **No slot needed** |

**Attempted 8 · carried 3 · declined 5.**

## §3 · DEEP picks and DEEP_LOG — **N = 4** (protocol DEEP budget: 2 continuous + 2 rotating)

| Slot | Sector | Why, and the mandate |
|---|---|---|
| **Continuous 1** | **ENRG (OW−)** | **Anti-thrash APPLIED** — continuous on 08-12 and 08-13, still the board's top OW and its only positive `wflow`. **Mandate**: `S67` scored **C** — resolve *why the level is best-of-board while Δ is 2nd-worst*, and whether the expression is refiners or integrateds (`wflow` is 30.5% `XOM` while `MPC/PSX/VLO` lead RS20 by **+6.8pp** over it) |
| **Continuous 2** | **INDU (OW−)** | **Anti-thrash APPLIED** — continuous on 08-12 and 08-13, still top-N OW. **Mandate is `D249`, unchanged and unresolved for a 3rd run**: the bracket measures `XLI`, the position is **defense**. Resolve which object the OW− is actually on |
| **Rotating 1** | ★★ **COMM (UW)** | **Recency: last covered 2026-08-07 = 6 runs, the longest untouched gap on the board**, and *"the telecom node `T`/`VZ`/`CMCSA` un-owned"* has now been written in **six consecutive** DEEP_LOGs. **Mandate — a maximum-width contradiction**: Δ **+0.185 (best of 11)** against exc60 **−9.098 (worst of 11)** and FINRA z **+2.15 (steepest short surge of 11)**. 🚨 **And it must resolve `R56` FIRST**: `EA` is **delisted (go-private 08-04, Form 25-NSE)** and is **STILL scored in this 13-name bucket at `flow_score +0.617`, OBV 매집 +0.743, `vol_surge` 3.44 on a stale `last` of 209.70 and a NULL 08-13 close** — **7th consecutive run.** Ex-`EA` the bucket reads **`eqflow` −0.167 (worse) and Δ +0.205 (better)** ⇒ **both of this sector's headline numbers are partly a dead security** |
| **Rotating 2** | ★★ **FIN (N−)** | **Demoted today (§2c) and the demote reverses `M40`, a claim carried for 22 days** — a reversal of a standing claim must be resolvable, and this desk's own rules forbid resolving it with the macro argument that contradicts it. **Recency: last covered 2026-08-08 = 4 runs. Mandate**: does the **eqflow/wflow inversion** survive removing `BRK-B`, and does the **exc60 +7.290 / steepener** leg belong to a different sub-node (banks) than the one `eqflow` is measuring? **`S78` settles 08-19** |

⚠ **Rotating slots are a DECLARED recency-starved deviation for a 3rd consecutive run** — after the
deltas the board holds **two OW-side sectors (ENRG, INDU)** and both are continuous, so **no third OW
exists** to rotate into. Both rotating picks are therefore **UW/N− sectors chosen by recency +
contradiction width**, stated rather than smuggled.
⚠ **IT is NOT given a slot despite being the run's sharpest finding** — it was deep-dived **08-13,
one run ago**, and the recency rule excludes it. **Its contradiction is handed to PREMORTEM instead**,
which is the correct owner: *the board's only non-Energy positive `wflow` is one name, and that name's
🟢 is lit by a revoked axis.* **That is an instrument contradiction inside this run, not a sector question.**
⚠ **No padding**: 4 of 4 slots filled, none with a sector that had no mandate.

## DEEP_LOG 2026-08-14: continuous=[ENRG, INDU] rotating=[COMM, FIN] · N=4/4 · **THREE verdict deltas (IT N→N+ · HLTH N+→N · FIN N→N−), all carried by `eqflow`/Δ — never by a green count, because `SWEEP_READ §2` measured the 🟢 TAG to be 4-axis while `flow_score`/`wflow`/`eqflow`/Δ are 3-axis and clean: 5 of 11 greens (CSCO·DELL·CVX·NVDA·BAC) cannot be produced by OBV∧RS20>0∧vol_surge≥1.2 and are 2.6× over-represented from the 51-name 17%-coverage survivor sample** · **IT N→N+ is legal because BOTH halves of 08-13's stated blocker changed in one settled session (eqflow −0.100→+0.034, and IT BECAME a flipper so wflow leaves the argument), with the counter-evidence stated: adjusted 2🟢/10🔴 and wflow +0.016 = NVDA alone (ex-top1 −0.078)** · **HLTH N+→N demotes the CHANGE not the LEVEL — Δ −0.228 worst of 11 and 3rd consecutive deceleration (+0.157→−0.014→−0.228) with 0🟢/32, while eqflow +0.019 and XLV exc60 +10.239 (best of 11) both point the other way and are named** · **FIN N→N− REVERSES M40 (07-23, "the board's only breadth-led sector", eqflow +0.320 > wflow +0.253): the ordering has inverted to eqflow −0.144 BELOW wflow −0.066, i.e. the median financial is now worse than the cap-weighted sector** · **flip list 3 of 11 — Information Technology/NVDA/19.4% (NEW, and it is the board's largest sector) · Health Care/LLY/19.4% (NEW) · Materials/LIN/24.7%; Industrials came OFF — no verdict rests on any of their wflow** · **five attempts declined with numbers: ENRG OW−→OW (Δ −0.157 = 2nd worst on the board against the best level; S67 scored FIRED-C at median RS20 +11.925, 1.635pp short of its with-us branch ⇒ still un-adjudicated, 2nd run), COMM UW→UW− (the board's BEST Δ +0.185 points the wrong way for a demote, while exc60 −9.098 and FINRA z +2.15 block a promotion ⇒ C3 both directions), MATR N−→N (flipper LIN 24.7%; every permitted axis refuses — eqflow −0.130, breadth 0.00, Δ −0.073 — and ex-NEM EW exc5 −1.893 with 1 of 12 positive agrees from the price side), UTIL UW→UW− (redundant floor; XLU exc5 +0.309 positive and S71 scored FIRED-C at −0.472pp inside band; P56 changed UTIL's MECHANISM from policy-rate to long-end term premium without changing its sign, and a mechanism change is not a notch), DISC N−→N (the board's only FINRA short-covering signal z −1.61 is a POSITIONING axis, not a demand axis (D6); demand axes refuse at eqflow −0.174 and 1🟢/9🔴 — logged to the missed ledger instead))** · **STPL's Δ −0.221 (2nd worst) declined on NOTATION — UW− is this board's floor and no step below it is defined; logged here so the next run sees it, and ⚠ D249 says STPL not FIN is the 252-day third leg of the duration complex** · **anti-thrash APPLIED to both continuous slots (ENRG and INDU each continuous on 08-12 AND 08-13 and still top-N OW)** · **rotating slots are a DECLARED recency-starved deviation for a 3rd run — after the deltas only two OW-side sectors exist and both are continuous** · **IT deliberately NOT given a slot (covered 08-13 = 1 run) — its contradiction is handed to PREMORTEM as an INSTRUMENT question, not a sector one** · uncovered=[**IT(N+, PROMOTED TODAY, covered 08-13 = 1 run; ★the board's only non-ENRG positive wflow and it is one name — NVDA 19.4%, ex-top1 −0.078 — whose own 🟢 is disqualified; eqflow +0.034 > wflow +0.016; XLK positive on all three price windows (exc5 +1.723 / exc20 +3.846 best of 11 / exc60 +4.101) with Nasdaq-100 spec at the 0th percentile short; EVENT_ALPHA Card 2 finds Microsoft's Maia 300 at 300k units targeting September ⇒ the displacement is already in the 60-day tape at MRVL RS60 +26.2 vs NVDA −4.0; ★next run's first rotating pick on recency)**, **HLTH(N, DEMOTED TODAY, covered 08-13 = 1 run; Δ −0.228 worst of 11 and 3rd consecutive deceleration, 0🟢/32, breadth 0.00 — against XLV exc60 +10.239 best of 11 and eqflow +0.019; S76 settles 08-19 and S82 08-20, and S82 is already ABOVE its branch A at +3.091)**, **MATR(N−, covered 08-13 = 1 run; S57 FIRED-A twice with the tilt carried anyway, S77 is the replacement falsifier settling 08-19; the sector is NEM alone — NEM exc5 +7.096/exc20 +22.101 vs ex-NEM EW exc5 −1.893 with 1 of 12 positive; copper spec at the 100th percentile long while FCX is the basket's worst name at −5.170)**, **DISC(N−, covered 08-03 = 8 runs = the longest gap on the board; the only FINRA short-covering signal of the eleven (z −1.61, 5v5 −9.3▼) sitting on the worst demand axes — a positioning/demand disagreement nobody has deep-dived)**, **UTIL(UW, covered 08-12 = 2 runs; 0🟢/9🔴 and wflow −0.491 worst of 11, but exc5 +0.309 positive and the MECHANISM changed under it — P56 says long-end term premium, not policy rate, and no bracket tests the new mechanism; S80 settles 08-19)**, **STPL(UW−, covered 08-10 = 4 runs; Δ −0.221 = 2nd worst on the board and the notch was declined only on notation; D249 makes it the 252-day third duration leg)**, **RE(UW, covered 08-04 = 7 runs; every axis agrees — wflow −0.252, eqflow −0.224, breadth 0.00, Δ −0.079, exc20 −4.366 — which is exactly why it does not need a slot; ⚠ its one contrary axis is FINRA z −1.41 covering, a positioning axis not a demand axis (D6))**]

## ✅ EXIT CHECK

- [x] **§1 is ONE line**, inherited verbatim. No unchanged sector gets a row or a restated flow number.
- [x] **Every §2 delta cites a flow number** — IT on `eqflow` + Δ, HLTH on Δ + green count, FIN on
      `eqflow` ordering + Δ. **The FIN steepener/`exc60` argument is explicitly logged as a macro
      re-argument and declined as a carrier** (§2c).
- [x] 🚨 **No promotion or demotion rests on a `top1_flips_sign` bucket.** IT and HLTH are both
      flippers and both deltas are carried on non-cap-weighted axes with `wflow` named as excluded.
      **The full flip list is reproduced in §0 even where it changes nothing.**
- [x] **The axis count is stated** (`n_axes` 3), and — new this run — **the tag/score axis mismatch is
      stated and applied**: every green count in this file is the adjusted one.
- [x] **Every matrix×flow divergence has a resolution owner**: ENRG/INDU → DEEP (continuous),
      COMM/FIN → DEEP (rotating), IT → **PREMORTEM**, HLTH → `S76`/`S82`, MATR → `S77`, UTIL → `S80`.
- [x] **N=4 picked by the rule** — anti-thrash applied to both continuous slots, recency applied to
      both rotating slots, **recency-starvation declared**. **No padding.**
      **OW sectors without a slot: none exist** (both OW sectors hold continuous slots).
- [x] **DEEP_LOG line appended** with every uncovered sector, its last-covered date, and its dated
      catalyst.
- [ ] **Linter** — run below.

## §4 · Linter

```
python -X utf8 scripts/report_lint.py llm_outputs/2026-08-14/industry_US/SECTOR_ROTATION.md
✅ SECTOR_ROTATION.md · 총 0건.
```
**0 findings, no exemptions claimed.** ⚠ Form only (C1 · C2 · S6 · D6) — a clean lint is not a
correct rotation. This file's substantive weakness is that **all three deltas rest on a ONE-session
Δ (S1)**, which is why every one of them is a single notch.
