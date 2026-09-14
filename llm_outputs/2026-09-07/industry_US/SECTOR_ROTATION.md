# SECTOR_ROTATION — industry_US · 2026-09-07 (Mon, US Labor Day) · Stage 6 / L1·ROTATION

> **Delta-only.** MACRO owns the 11-sector wind (`MACRO_REPORT §E`); `SECTOR_FLOW_US.json` owns the
> flow numbers. Both are on disk. This file writes **only what changes and why** — and for a
> **second consecutive run** the answer is that nothing may change, for a structural reason.

## 🚨 Instrument state governing every delta below

`§scoring`: **`n_axes` 3 · `mode` nonews · `vel_coverage` 17.39% (52/299) · `scored` 299 ·
`dropped_missing_axis` 0** · `asof` **2026-09-04**.

- **Coverage 17.39% ≪ 80% ⇒ the news axis is dropped.** 🚫 **No delta below cites theme freshness or
  news velocity.** Cause **probed, not assumed**: 6/6 alive pre-sweep with counts *moving*
  (NVIDIA 3,841→3,761), 0/4 immediately post-sweep, alive again after ~2 min probe-free idleness
  (`D502`, 4th replication; recovery-clock failure is new and is `D553`).
- **Δ is legal on scale**: prior same-mode snapshot 09-03, same 3-axis `nonews` scale. ⚠ **Every Δ
  below is the `09-03 → 09-04` change** — the same change the 09-05 run spent and the 09-06 run
  re-read. **Third statement of one number.**
- Cap weights are **54 days stale** (G5) ⇒ **`eqflow` is the citable cut on every line.**
- 🚨 **The 🟢 tag is not a clean instrument, and this run measured the cut-point.** `flow_tag` uses
  `velocity` — an axis `scoring.vel_axis` declares **false** — and `velocity` exists only for
  **universe ranks 1–52**. Measured: **`PG` (rank 34, flow +0.231, `vol_surge` 0.89) is 🟢** while
  **`CEG` (rank 124, flow +0.644, surge 0.96) and `VST` (rank 220, flow +0.619, surge 1.02) are 🟡**;
  all 7 greens *without* a velocity carry surge **1.21–1.47**. ⇒ **two different gates by cap rank**
  (`D561`, sharpening `D537`). **Any delta resting on a green count or on breadth is affected**, and
  §2 says where.

---

## §1 · Inherited — one line

**Standing verdicts, carried from the 2026-09-05 `industry_US` ROTATION (the last run to issue any):**
`ENRG OW+ · HLTH OW · MATR N · IT N · FIN N · STPL UW · UTIL UW · RE UW · DISC UW · INDU UW− · COMM no-verdict issued`.

**Today's MACRO §E wind, verbatim:**
`ENRG OW · HLTH N+ · IT N · FIN N · UTIL N− · MATR N− · STPL UW · RE UW− · INDU UW− · DISC UW · COMM no verdict issued`.

🚨 **`D476` reproduces for a FOURTH consecutive run, and once again the offender is this desk's own
MACRO stage.** Five of today's §E labels differ from the standing set (`ENRG` OW vs OW+ · `HLTH` N+
vs OW · `UTIL` N− vs UW · `MATR` N− vs N · `RE` UW− vs UW). **§E is a WIND, not a verdict. None of
the five is inherited as a change**; each is either re-derived below against a flow number or
**reverted to the standing verdict**. The fix stays mechanical and stays unbuilt: **MACRO §E should
carry the standing verdict in a column beside its wind** (`P5` — a template change, not a judgement).

---

## §2 · Deltas — **0 changes of 11 attempts**, and the reason is the calendar

★★★ **The governing fact, now on its third consecutive occurrence.** `asof` is **2026-09-04** — the
same settled session the 09-05 **and** 09-06 runs read — and all 11 sectors reproduce **identically**
on all nine fields (PREFLIGHT `G2`, verified again this run on an independent price-frame
recomputation in `MACRO §E`).

**A delta must be carried by a flow number** (this stage's own rule). **Every flow number available
today was spent by the 09-05 run**, which used them to issue three deltas (`ENRG OW→OW+`,
`FIN UW→N`, `STPL N→UW`). Therefore, and for the same three reasons the 09-06 run gave:
re-issuing is double-counting · issuing differently is a claim the 09-05 run misread the same
numbers · issuing on today's genuinely new evidence (the ECB hike, the UST-selling mechanism, the
IEA 9.6 mb/d refining outage, the LNG force majeure) is a **macro re-argument this stage is
forbidden to make** — and MACRO has already handled it by registering `P142`, `P143` and `P144`.

**11 attempts, 11 declines, each with its number:**

| # | attempted | flow evidence | why declined |
|---|---|---|---|
| 1 | `ENRG OW+ → OW` (demote) | `eqflow` **+0.562 rank 1** · breadth **0.19 rank 1** · **15/16 positive on `exc5`** · Δ +0.054 · non-flipper (`XOM` 30.5% **holds it down**: +0.440 → ex-top1 +0.621) | The only new argument is that the sector's two **narrative** instruments decelerate (`Strait of Hormuz` 0.88×, `refining margin` 0.68×). **That is a news-axis argument and the news axis is barred** (`vel_coverage` 17.39%). Every flow number is rank-1. **Declined.** |
| 2 | `HLTH OW → OW+` (promote) | `eqflow` **+0.190 rank 2** · `exc20` **+3.63 mean / +3.74 median** (median ≥ mean = broad) · Δ **−0.043**, negative and unchanged | The Δ points the wrong way and has not moved. **Declined for absence of change.** |
| 3 | `IT N → UW` (demote) | `eqflow` −0.195 · Δ −0.010 · `exc5` mean **−0.27** but median **+0.27** with **30/56 positive** · `exc20` −0.99/−1.82 | **7th consecutive decline, 7th distinct reason: the two price cuts contradict each other within the same window.** A mean-vs-median inversion with breadth at 54% is a **split** bucket, and `W5` bars a sector-wide verdict across a split. Routed to PREMORTEM for a **7th** run. `S140` settles 09-08, `S148` 09-14 |
| 4 | `FIN N → OW−` (promote) | `eqflow` **−0.023** flat and unchanged · Δ −0.004 · `exc20` **+1.92/+1.04** with 26/47 positive on `exc5` | The available promoting argument is `hy_oas` at the **2.0th percentile** — a **MACRO number**. **Macro re-argument, declined** (2nd consecutive run declining on the same temptation). `P128` settles 09-08 |
| 5 | `UTIL UW → N` (promote) | `eqflow` **+0.050** (positive) vs Δ **−0.037** (negative) · breadth 0.00 🚫 **inadmissible** (`D537`/`D561`: `CEG` surge 0.96 and `VST` surge 1.02 are blocked by the gate alone, and this run shows the gate is not applied to the top 52) | **7th decline, and now on ONE surviving reason instead of two**: the breadth-0.00 reason is dead, so what remains is `eqflow` and Δ **disagreeing in sign**. **Declined**, and the case for a DEEP slot is stronger than the case for a notch |
| 6 | `MATR N → N−` (demote) | `eqflow` −0.107 · Δ −0.037 · `exc5` mean −1.13 vs median **−2.44** · `exc20` −0.85/**−2.99** · **3/12 positive** — the numbers **do** support it | **Declined on `D343` for a 3rd consecutive run: `P102` settles 2026-09-09** and asks precisely whether Materials is two names. Moving two days early makes a live row unscoreable-as-designed. `C24` carried an **8th** run (copper COT 100th %ile, 7th consecutive — ⚠ on **09-01** data) |
| 7 | `RE UW → UW−` (deepen) | Negative on **every** cut and window · **1/12 positive on `exc5`** — the board's most internally consistent bucket · Δ **−0.020**, the 4th-smallest on the board | Consistent but **not newly worse**. Deepening a notch on unchanged numbers is padding. ⚠ Its breadth 0.00 **is** evidence (unlike UTIL's) — RE's best names do not clear the gate on the **non-news** axes either. **Declined** |
| 8 | `STPL UW → UW−` (deepen) | `eqflow` −0.098 · Δ −0.018 · `exc5` mean −1.39 vs median **−2.29** · 7/19 positive | 🚨 **Declined partly on instrument grounds, and the ground is now measured rather than suspected**: **`PG` is 🟢 at flow +0.231 with `vol_surge` 0.89 solely because rank 34 gives it a velocity** (`D561`). A bucket whose green count is set by a dead axis may not carry a delta in either direction. **2nd consecutive run declined for this reason** |
| 9 | `DISC UW → UW−` (deepen) | 🚨1名 **`AMZN` 40.2%**, `top1_flips_sign` **True** (−0.255 → **+0.068**) ⇒ `wflow` **barred**. Admissible cut `eqflow` **−0.280 agrees with the barred sign**; 21/28 negative on `exc5`; `exc20` **−4.11/−5.27** | The admissible number supports the direction, but **Δ moved 0.000**. **Declined for absence of change**, not absence of support |
| 10 | `COMM` any verdict | 🚫 **barred, 17th consecutive run.** `D459` **13th reproduction**: Alphabet is **76.6%** of the bucket across `GOOGL`+`GOOG`, invisible to the per-ticker flag which prints **False**; ex-issuer `wflow` −0.389 → **+0.272**, swing **0.661**. `eqflow` **−0.035 = flat**; `exc5` **2/13** positive against `exc20` median **+3.70** | **A sector this desk cannot aggregate is a sector this desk does not rank.** ⚠ And the two price windows contradict each other, so even `eqflow` would not carry a verdict |
| 11 | `INDU UW− → N` (promote) | The board's **largest Δ +0.082** · but `exc20` **−5.04 mean / −5.90 median = worst on the board** · 17/50 positive on `exc5` | **The Δ is the 09-03→09-04 change for the third time** — a stale number cannot be an ignition. 🚨 And new evidence argues the **other** way: the defense node is at a **7.1st-percentile 5-session extreme** with **zero narrative carriage**, and the **book-held `RTX` is its worst name** (flow −0.789, OBV −0.294 분산, rs20 −9.6). `S150` settles 09-14. **Declined** |

**Macro re-arguments attempted and declined: 3** — `FIN` promotion on `hy_oas`, `ENRG` demotion on
the decelerating news instruments, `INDU` promotion on the stale Δ. **Logged, not dropped.**

### Flip list, reproduced in full even though it changes nothing

| by the built-in flag | by ISSUER (share classes merged) |
|---|---|
| **1 of 11 — Consumer Discretionary / `AMZN` / 40.2%**, `wflow` −0.255 → ex-top1 **+0.068** | **2 of 11** — adds **Comm. Services / Alphabet (`GOOGL`+`GOOG`) / 76.6%**, `wflow` −0.389 → ex-issuer **+0.272**, swing **0.661**, which the per-ticker flag **cannot see** (13th run) |

⚠ `XOM` at **30.5%** of Energy is top-heavy but **not** a flipper — the sector is *more* positive
without it (+0.440 → +0.621) — and is therefore **not** a bar. Concentration ≠ sign-dependence.

---

## §3 · DEEP picks + DEEP_LOG

**Protocol DEEP budget: N = 4** (2 continuous + 2 rotating). Recency read from **DEEP files on disk**,
not from prose.

| sector | standing verdict | last DEEP | runs since | slot |
|---|---|---|--:|---|
| **Energy** | **OW+** | 2026-09-06 | 0 | ★ **CONTINUOUS #1** — held the slot last run **and** is still top OW (`eqflow` rank 1, breadth rank 1). Anti-thrash continuity applies and is stated |
| **Health Care** | **OW** | 2026-09-06 | 0 | ★ **CONTINUOUS #2** — same rule; the board's only other OW and its only other positive `eqflow` |
| Information Technology | N | 2026-09-05 | 1 | ✖ not OW |
| Utilities | UW | 2026-09-05 | 1 | ✖ not OW |
| (Defense sub-node) | — | 2026-09-06 | 0 | ✖ PREMORTEM-promoted, not a GICS sector |
| Materials | N | 2026-09-01 | 3 | ✖ not OW |
| Communication Services | no verdict | 2026-09-01 | 3 | ✖ un-rankable |
| Industrials | UW− | 2026-08-31 | 4 | ✖ not OW |
| Financials | N | 2026-08-30 | 5 | ✖ not OW |
| Consumer Staples | UW | 2026-08-27 | 6 | ✖ not OW |
| Consumer Discretionary | UW | 2026-08-27 | 6 | ✖ not OW |
| Real Estate | UW | 2026-08-26 | **7 — the longest gap on the board, 4th consecutive run** | ✖ UW sectors do not take DEEP slots |

**DEEP picks = 2 of 4: `ENRG` · `HLTH`.**
🚨 **The 2 rotating slots are UNFILLED for a FOURTH consecutive run** — the board carries only two OW
sectors and **padding with N/UW is forbidden**. Both empty slots are **offered to PREMORTEM** with
named candidates and reasons:

- **`IT`** — routed for a **7th** consecutive run; the book's largest concentration; its `exc5`
  mean and median now **contradict each other** with breadth at 54%, which is a split no sector-level
  verdict can express (`W5`). `S140` settles **09-08**, `S148` **09-14**.
- **`UTIL` / the AI-power lane** — its breadth-0.00 disqualifier is now **measured as a filter
  artifact with a known cut-point** (`D561`), which is a stronger case than either prior run had;
  the lane spans three GICS labels (`D416`); the book holds `ETN` (flow −0.662 🔴). `P123` 09-08 ·
  `P127` 09-10 · `S146` 09-14.

★★ **`M1371` reaches n = 4, and that matters to the protocol itself.** `pipeline/protocols/industry_us.md`
holds N=4 and states that any cut *"needs **its own** measurement first"*. **This run supplies the
fourth consecutive measurement**: on 09-02, 09-05, 09-06 and 09-07 the US board carried exactly two
OW sectors and the budget was structurally unfillable. **This stage does not change N (P5 — the
protocol's DEEP-budget line is human-owned); it records that the measurement the protocol asked for
now exists, with n = 4.**

## DEEP_LOG 2026-09-07: continuous=[ENRG, HLTH] rotating=[] · **N=2/4 filled for a FOURTH consecutive run — board has only 2 OW sectors, padding forbidden; both empty slots offered to PREMORTEM with named candidates (IT, UTIL/AI-power lane) and reasons (`M1371`, n=4 — the protocol's own precondition for revisiting N is now met, P5)** · **verdict deltas 0 of 11 attempts, structural not judgemental: `asof` 2026-09-04 for a THIRD run, all 11 sectors identical on all nine fields, and every flow number was spent by the 09-05 run** · **11 declines each with its number: `ENRG OW+→OW` (all flow ranks 1; the only demoting argument is the decelerating news axis, which is barred at 17.39% coverage), `HLTH OW→OW+` (Δ −0.043 wrong-signed and unchanged), `IT N→UW` (7th decline, 7th distinct reason — `exc5` mean −0.27 vs median +0.27 with 30/56 positive = a SPLIT bucket, `W5` bars a sector-wide verdict), `FIN N→OW−` (hy_oas 2.0th %ile is a macro re-argument, declined 2nd consecutive run; eqflow −0.023 flat), `UTIL UW→N` (7th decline, now on ONE reason: breadth-0.00 is dead as a reason under `D561`, leaving eqflow +0.050 vs Δ −0.037 sign-disagreement), `MATR N→N−` (numbers DO support it — eqflow −0.107, exc20 median −2.99 vs mean −0.85, 3/12 positive — declined on `D343` 3rd run because **P102 settles 09-09**; C24 8th run), `RE UW→UW−` (1/12 positive = board's most consistent, but Δ −0.020 is 4th-smallest ⇒ not newly worse; its breadth 0.00 IS evidence, unlike UTIL's), `STPL UW→UW−` (🚨 declined on instrument grounds now MEASURED: **PG is 🟢 at flow +0.231 / surge 0.89 solely because rank 34 grants it a velocity**, while CEG at flow +0.644 / surge 0.96 is 🟡 — two gates by cap rank, `D561`), `DISC UW→UW−` (🚨1名 AMZN 40.2% flips −0.255→+0.068; admissible eqflow −0.280 AGREES and 21/28 negative on exc5 — declined for **absence of change**, Δ 0.000), `COMM` any (**barred, 17th run**; D459 13th reproduction, Alphabet 76.6% across two tickers invisible to the per-ticker flag, swing 0.661, eqflow −0.035 flat, and exc5 2/13 contradicts exc20 median +3.70), `INDU UW−→N` (board's best Δ +0.082 is the **09-03→09-04 change for the third time**; exc20 −5.04/−5.90 worst on the board; 🚨 the defense node sits at a 7.1st-percentile extreme with ZERO narrative carriage and the book-held RTX is its worst name)** · **macro re-arguments attempted and declined: 3 (FIN on hy_oas, ENRG on the news deceleration, INDU on the stale Δ)** · **flip list: by the flag 1 of 11 (DISC/AMZN/40.2%); by ISSUER 2 of 11 (adds COMM/Alphabet/76.6% across two share classes, swing 0.661 — 13th run); XOM at 30.5% of ENRG is top-heavy but NOT a flipper and is not a bar** · 🚨 **instrument state: n_axes 3 (`nonews`), vel_coverage **17.39%** ⇒ ZERO deltas cite velocity or freshness; cause PROBED (6/6 pre-sweep with counts MOVING, 0/4 post, and — new — **0/5 through t+100s** under 20s polling before recovering after ~2min of probe-free idleness, `D553`); the wall sits at universe ranks **1–52** (49→50→52 across three runs) and is only visible in universe-rank order, NOT in the JSON's flow_score-sorted array (`D554`); Δ is legal on scale but is the same 09-03→09-04 change for a third statement; cap weights **54 days stale** so eqflow is the citable cut on every line; ★★ NEW AND MEASURED — **the 🟢 tag applies two different gates by cap rank**: all 7 greens without a velocity carry vol_surge 1.21–1.47, while PG (rank 34, surge 0.89) and CVX (rank 35, surge 0.99) are green on velocity alone, an axis `scoring.vel_axis` declares FALSE and which exists only for ranks 1–52 (`D561`, sharpening `D537` from an artifact on one name to a structural rule with a cut-point)** · ★★ **the structural line: this is the SECOND consecutive run whose correct delta count is zero for calendar reasons, and the third run reading session 2026-09-04. The run's new information is entirely non-price — MACRO §B/§D (ECB hike 09-10 undated in the desk's calendar; Japan funding yen intervention by SELLING USTs; `bond selloff` theme-age 5.93× on base 247) and EVENT_ALPHA (IEA 9.6 mb/d of Middle East refining capacity destroyed; QatarEnergy force majeure into November; the ENTIRE US LNG export chain absent from the universe)** · **uncovered=[IT(N, last DEEP 09-05 = 1 run, routed to PREMORTEM 7th consecutive run, book's largest concentration, exc5 mean/median now CONTRADICT, S140 09-08 · S148 09-14), UTIL(UW, last DEEP 09-05 = 1 run, offered to PREMORTEM with the strongest case yet because `D561` gives its breadth-0.00 artifact a measured cut-point, AI-power lane spans 3 GICS labels `D416`, BOOK FLAG on held ETN flow −0.662 🔴, P123 09-08 · P127 09-10 · S146 09-14), MATR(N, last DEEP 09-01 = 3 runs, P102 settles 09-09, C24 8th run, copper COT 100th %ile 7th run on 09-01 data), COMM(no-verdict, last DEEP 09-01 = 3 runs, un-rankable by rule 17th run), INDU(UW−, last DEEP 08-31 = 4 runs, board's worst exc20 AND board's best but STALE Δ, 🚨 defense node at a 7.1st-percentile extreme with zero narrative and the book holding its worst name, S150 09-14), FIN(N, last DEEP 08-30 = 5 runs, P128 09-08 · S142 09-11), STPL(UW, last DEEP 08-27 = 6 runs, 🚨 its green count is set by a dead axis — `D561`), DISC(UW, last DEEP 08-27 = 6 runs, 🚨1名 AMZN 40.2%, 21/28 negative on exc5), RE(UW, last DEEP 08-26 = **7 runs, the longest recency gap on the board for a 4th consecutive run**, 1/12 positive on exc5, breadth 0.00 confirmed as EVIDENCE not artifact; NOT slotted because UW sectors do not take DEEP slots)]** · **NEW THIS RUN, handed to PREMORTEM as a MANDATORY bracket: the ECB rate decision on 2026-09-10, fully priced at 25bp to a 2.5% deposit rate, body-confirmed, and ABSENT from `catalyst_calendar --days 10` (`D562`)**

---

## ✅ EXIT CHECK — ROTATION

- [x] **§1 is ONE line** inheriting the standing verdicts, plus one line quoting MACRO §E verbatim. No unchanged sector gets a paragraph.
- [x] **Every §2 row cites a flow number**, and the **3 macro re-arguments attempted were declined and logged** rather than used.
- [x] 🚨 **No promotion or demotion rests on a `top1_flips_sign` bucket** — `DISC` was attempted on the **admissible** `eqflow` (−0.280) and declined for absence of change; `COMM` was barred outright. **The flip list is reproduced in full**, including the issuer-level case the flag cannot see.
- [x] **The axis count is stated** (`n_axes` 3, `nonews`, `vel_coverage` 17.39%). **Zero deltas cite theme freshness or velocity**, and Δ is read only against a same-axis-count snapshot (09-03).
- [x] **Every divergence has a named resolution owner** — `IT` and `UTIL` to PREMORTEM; `MATR` to `P102` (09-09); `FIN` to `P128` (09-08); `INDU`/defense to `S150` (09-14); `ENRG`'s narrative-vs-flow split to `P140` (09-11) and `P136`/`P139` (09-14).
- [x] **DEEP picks by the rule** — continuity stated for both continuous slots, recency table printed from files on disk, **no padding**, and the unfilled slots offered to PREMORTEM with named candidates. **Every uncovered sector is named in DEEP_LOG with its recency.**
- [x] **Linter run on this stage's own output** — see below.
- [x] **DEEP_LOG line appended** for the next run.
- [x] **Delta count is 0 and the file is short and says why** — which the stage's own rule declares a valid, informative run.

---

> P4 — no sizing, no buy/sell language.
