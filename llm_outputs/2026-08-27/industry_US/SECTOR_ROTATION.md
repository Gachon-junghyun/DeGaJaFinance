# SECTOR_ROTATION — industry_US · 2026-08-27 (Stage 6 / L1·ROTATION)

> **Delta-only.** MACRO owns the 11-sector verdict; `SECTOR_FLOW_US.json` owns the flow numbers. Both
> are on disk. This file writes **only what changes and why**, plus the DEEP picks.
> **Axis count this run scored on: `n_axes` = 3** (`§scoring`, `vel_coverage` **16.7%**, `dropped_missing_axis` 0).
> 🚫 **The news axis is dead ⇒ no delta below cites theme freshness or news velocity**, and Δ is read
> only against snapshots of the **same 3-axis** scale (08-20 → 08-27, unbroken).
> ⚠ The sweep is asof **2026-08-27, a pre-market stub bar** (median volume **4.65%** of the prior
> session, 2 of 300 names above 50%). **`vol_surge` and the 🟢/🔴 tag are not used to carry a verdict.**

---

## §1 · Inherited — one line, verbatim

`MACRO holds: ENRG OW · HLTH OW · MATR N · COMM N · DISC N · FIN N · STPL N− · RE N− · INDU UW− · UTIL UW− · IT UW`

✅ **§0 reconciliation check passed this run** — MACRO §0 restated the standing line and it matches the
08-26 ROTATION's output exactly. **No undeclared re-promotion to correct.** (`D358-KR` fired at this
point on 08-26 with `MATR N+` and again this morning on the KR side with `IT N`; **it did not fire
here**, which is the check working rather than the check being unnecessary.)

---

## §2 · Deltas

### 🚨 The flipper list, reproduced in full — even though it changes one verdict and blocks nothing else

`§sector_rotation[].top1_flips_sign`, **2 of 11**:

| sector | top1 | top1_w | wflow | wflow_ex_top1 | may this run promote/demote it on `wflow`? |
|---|---|---|---|---|---|
| **Health Care** | `LLY` | **19.4%** | −0.033 | **+0.038** | **NO** — substitute `eqflow` **+0.086** / breadth **0.06** |
| **Energy** | `XOM` | **30.5%** | −0.091 | **+0.140** | **NO** — substitute `eqflow` **+0.042** / breadth **0.00** |

Nine sectors carry `top1_flips_sign: false`.

🚨 **The set changed between this run's own PREFLIGHT and its own SWEEP — 2nd consecutive run, 4th
consecutive change of identity.** PREFLIGHT (reading the 08-26 baseline) attached restrictions to
**DISC / MATR / ENRG**; the SWEEP measures **HLTH / ENRG**. ⇒ **the DISC and MATR restrictions are
LIFTED and a HLTH restriction is ATTACHED**, in-stage. **This matters to a verdict below**: the one
delta this run issues is on **DISC**, which was barred four hours ago and is not barred now — and that
is stated at the point of use, not buried here.

### The one delta

| sector | matrix said | flow evidence (`eqflow` · red-rate · breadth · Δd/d · 🟢/🔴) | new verdict | who resolves |
|---|---|---|---|---|---|
| **Consumer Discretionary** | **N** | `eqflow` **−0.339 = rank 9 of 11** · **red-rate 39.3% (11 of 28) = 2nd worst on the board**, behind only Utilities (53.3%) · **breadth 0.00** · **`delta` −0.188 = the board's largest negative day-over-day move**, 2.1× the next-largest (`IT` −0.087) · **0 🟢 / 11 🔴** | **N−** | **PREMORTEM** (no DEEP slot — see §3) |

**Why this one is admissible and today's other nine attempts are not:**
- **All four numbers are non-cap-weighted** (`eqflow`, red-rate, breadth, equal-weight Δ). **No `wflow`
  is used**, and DISC is **not** a flipper on this snapshot (`top1_flips_sign: false`, `AMZN`).
- **It is not a macro re-argument.** The macro case for DISC is unchanged from MACRO §E; what changed
  is the money, on four independent flow readings.
- ★ **It resolves a contradiction rather than creating one.** DISC has been logged for **five
  consecutive runs** as the board's widest `C5` gap — flow said soft, price said firm. **This run
  measured that the gap CLOSED** (`M989`): MACRO's own settled 08-26 price frame now reads DISC at
  `exc1` **−0.866 = worst of 11** and `med5` **−1.227 = worst of 11**. **Both instruments now agree**,
  and a notch is what agreement across two instruments buys.
- ⚠ **The `delta` is on a stub bar and is therefore used only as a cross-sectional rank** ("largest
  negative of 11"), never as a magnitude. The other three numbers are level/count readings that a
  low-volume bar does not distort in the cross-section.

### Attempts DECLINED, with the numbers that declined them (9)

> Logged rather than dropped, so that *"we looked and passed"* stays distinguishable from *"we never
> looked"* — the same asymmetry the missed ledger exists to close.

| # | attempt | why declined |
|---|---|---|
| 1 | **`HLTH` OW → N+** | **Declined; nothing supports a notch down.** `eqflow` **+0.086 = rank 1 of 11**, **the only sector on the board with positive breadth (0.06)**, red-rate **9.4% = best of 11**, `delta` **+0.099 = 2nd-largest positive**. ⚠ **🚨1名 bucket — `LLY` at 19.4%; `wflow −0.033` is unusable by rule** and the permitted substitutes all argue the other way. **Held at OW** |
| 2 | **`ENRG` OW → N+** (rule (a): matrix-OW, flow-absent) | **Declined.** The flow is not absent: `eqflow` **+0.042 = rank 2 of 11**, red-rate **12.5% = 2nd best**. ⚠ **🚨1名 bucket — `XOM` at 30.5%**, so `wflow −0.091` may not carry a demotion **by rule**; the substitute says rank 2. ⚠ Counter-evidence stated: **breadth 0.00, 0 🟢**. **Held at OW**; the commodity leg is bracketed by **`P103` (09-02)** and the equity leg by `S119` (settles tonight) |
| 3 | **`MATR` N → N+** | **Declined, and the reason is a reading correction.** `MATR` is **the board's only zero-red sector (0 of 12)** and `delta` **+0.071**, which reads as strength — but it is **0 🟢 AND 0 🔴 on a 4.65%-volume bar**, i.e. **nothing happened**, not something good. `eqflow` **−0.042** is still negative. ⚠ **And the anti-thrash case is explicit**: the 08-25 ROTATION demoted `MATR` N+ → N and the 08-26 MACRO was caught silently re-promoting it. **Re-promoting it today on a no-participation reading would be that same error with a stage's letterhead on it.** Held at `N`; `P102` (09-09) owns the two-name spread |
| 4 | **`IT` UW → upgrade** | **Declined as a price re-argument.** MACRO's settled frame has IT `exc20` **+6.708 = best of 11**, which is a real number — **but it is a price number, and this stage requires a flow number.** The flow says the opposite: `eqflow` **rank 5**, `delta` **−0.087 = 2nd-worst on the board**, **9 🔴 of 56**. 🚫 **Not resolved by preference** — this is **`C16`**, and it is routed to **`P105`** (registered this run, settles 09-09), which puts the 20-day excess itself in a both-sided bracket |
| 5 | **`STPL` N− → restore N** | **Declined as too thin to reverse a one-day-old verdict.** The 08-26 demotion was carried by `eqflow` rank 9 + breadth 0.00 + **red-rate 42.1% = 2nd worst**. Today: rank **8**, breadth **still 0.00**, red-rate **36.8% = 3rd worst** (Utilities 53.3% and DISC 39.3% are now worse). **A 5.3pp red-rate improvement and one rank on a stub bar is not a reversal**; it is noise inside the same reading. **Handed to DEEP instead** (§3) |
| 6 | **`RE` N− → UW** | **Declined; the flow readings disagree with each other.** `eqflow` **−0.389 rank 10** and breadth 0.00 argue down, but red-rate is **25.0% = 6th of 11 (middle)** and `delta` is **+0.049 (positive)**. MACRO's price frame also refuses it (`exc5` +0.230, `exc60` +3.927). ⚠ **And the 08-26 DEEP already measured that RE's binding constraint is NOT rates**, so a demotion on the duration story would re-argue a question this desk has already answered against itself. Held at `N−` |
| 7 | **`FIN` N → N+** | **Declined as a price re-argument, and flagged as the board's largest un-owned positive.** Price: `exc5` **+2.105 = 2nd of 11**, `exc60` **+12.469 = 2nd of 11**, red-rate **14.9% = 3rd best**. Flow: `eqflow` **−0.144 = rank 6, dead middle**, `delta` −0.024. **A mid-rank flow number does not carry a promotion.** Held at `N`. ★ Named for the next run's recency rule: FIN was covered 08-26 (1 run) so it cannot take a rotating slot today |
| 8 | **`UTIL` UW− → change** | **Declined; every instrument agrees.** `eqflow` **−0.552 = rank 11**, red-rate **53.3% = worst of 11**, breadth 0.00, `delta` +0.002 ≈ flat; MACRO price `exc20` **−7.735**. **Nothing disagrees, so there is nothing for a delta to resolve.** Held |
| 9 | **`COMM` N → change** | **Declined BY RULE for a 9th consecutive run** (`D297`): `GOOGL`+`GOOG` ≈ **76.6% of a 12-name bucket** while `top1_flips_sign` prints **false** — the flag does not fire but the concentration is real, so no `wflow` claim is admissible either way. `eqflow` **−0.037 rank 3** with **0 🟢 / 2 🔴** is a two-name reading wearing a sector label. **Held at `N`, un-measurable rather than confirmed** |

**`INDU` was not attempted** — `eqflow` **−0.244 rank 7**, **15 🔴 = the most on the board**, 0 🟢, and
MACRO's price frame gives it the **worst 5-day breadth (26 of 50 negative)**. The standing `UW−` and
the flow agree; there is no delta to write. **It gets a DEEP slot instead** (§3).

**Delta count: 1 of 10 attempts.**

---

## §3 · DEEP picks — N = 4 (protocol budget: 2 continuous + 2 rotating)

### Continuous track (⌈N/2⌉ = 2) — **`ENRG`, `HLTH`**
Both held a continuous slot in the previous run **and are still the only two OW sectors today**
⇒ **anti-thrash continuity keeps the slots**, stated. This is the **8th consecutive run** for `ENRG`
and the **8th** for `HLTH`.

### Rotating track (⌊N/2⌋ = 2) — **`INDU`, `STPL`** · 🚨 declared recency-starved deviation, **14th run**

**The deviation, stated plainly**: the rule wants *"next-highest OW not deep-dived in ~3 runs."*
**Only two OW sectors exist and both took continuous slots.** ⇒ fallback to non-OW, ranked by
**information content** with **least-recently-covered as the tiebreak**, as the rule permits when stated.

**Recency, read from `DEEP_LOG` lines 08-16 → 08-26:**
`INDU` **5 runs** · `DISC` 4 · `UTIL` 4 · `COMM` 3 · `STPL` 3 · `MATR` 2 · `IT` 2 · `RE` 1 · `FIN` 1.

| pick | why it wins the slot |
|---|---|
| **`INDU`** (5 runs — **the board's worst recency**) | ★ **The 08-26 run declined INDU explicitly, and its stated reason has expired.** That reason was *"three instruments already agree there, and a slot where nothing disagrees buys the least information."* **Today two things disagree.** (i) **The horizons split**: `exc1` **+0.803 = 3rd best of 11** and `exc60` **+4.490 = 4th best**, against `eqflow` rank 7, **15 reds** and the **worst 5-day breadth on the board**. (ii) **A dated, live, and unbracketed catalyst now sits on it** — the **09-08 Canadian retaliatory tariffs**, whose headline thread is FADING off a 29-outlet peak while the *durability* thread (*"US and Canada Are Bracing for Prolonged Trade Dispute"*, 14 outlets) is climbing (EVENT_ALPHA Card 7). 🚨 **`D342`, 3rd run: the 09-08 date is bracketed only by `S123`, which settles 09-12 — four days late.** **Mandate**: is INDU's positive 1- and 60-day excess a different node from the 15 reds, and does the 09-08 date land on that node? |
| **`STPL`** (3 runs) | ★ **The slot buys the measurement that §2's attempt #5 could not make.** STPL carries a **one-run-old `N−` verdict** and its two instruments now disagree: flow says `eqflow` rank 8 / **36.8% red-rate** / breadth 0.00 with **0 🟢**, while MACRO's settled price frame says `exc5` **+0.939** with **only 4 of 19 negative**. **A fresh demotion whose price half refuses it is exactly what a DEEP slot is for.** **Second mandate**: `ADM` is the named US casualty of Canada's dairy/agricultural retaliation list (`ADM` **flow −0.643 🔴분산, OBV −0.154 분산**) and **has no bracket anywhere** — `D342`'s unbracketed half, **3rd run**. |

### Not picked, and why — so the next run's recency rule can see them
- **`DISC` (4 runs)** — **just demoted by this stage (§2), and it is the one sector where the two
  instruments newly AGREE** (`M989`). Agreement is the cheapest information on the board. **Lost the
  4-run tie to `INDU` explicitly**, and its verdict question is handed to **PREMORTEM** instead.
- **`UTIL` (4 runs)** — every instrument agrees (rank 11, worst red-rate, worst-but-one `exc20`).
  **Lowest information content on the board.**
- **`COMM` (3 runs)** — **un-measurable by rule for a 9th run** (`D297`). A slot cannot produce a
  measurement here; spending one would manufacture the appearance of coverage.
- **`IT` (2 runs)** — recency-blocked, **and it is deliberately routed elsewhere**: `C16` is the
  board's live contradiction and it is now owned by **`P105` (09-09)** and by PREMORTEM, not by a DEEP
  slot that would re-derive it two runs after the last one.
- **`MATR` (2 runs)** — recency-blocked; `P102` (09-09) owns its two-name spread.
- **`RE`, `FIN` (1 run each)** — recency-blocked.

**No 5th slot promoted at this stage.** PREMORTEM may promote one.

---

## §4 · Divergences named, with a resolution owner

| divergence | owner |
|---|---|
| **`C16`** — IT `eqflow` rank 5 / `delta` 2nd-worst **vs** `exc20` best of 11 | **`P105`** (settles 09-09) + PREMORTEM. 🚫 Not resolved here |
| **`STPL`** — flow `N−` evidence **vs** price `exc5 +0.939` with 4 of 19 negative | **DEEP (rotating slot)** |
| **`INDU`** — `exc1`/`exc60` top-4 **vs** `eqflow` rank 7 with the most reds and worst breadth | **DEEP (rotating slot)** |
| **`ENRG`** — `eqflow` rank 2 **vs** breadth 0.00 / 0 🟢; and `exc1` best of 11 **vs** `exc5` worst of 11 | **DEEP (continuous)** + **`P103`** (09-02, commodity leg) + `S119` (tonight, equity leg) |
| **`MATR`** — zero reds **vs** negative `eqflow` on a no-participation bar | **`P102`** (09-09) |
| **`RE`** — `eqflow` rank 10 **vs** positive `delta` and positive `exc60` | Left open; the 08-26 DEEP already ruled the binding constraint is not rates |
| **optical/interconnect** — `MRVL`/`LITE`/`COHR` all print RS20-positive / RS60-negative / OBV-매집, and **no cycle registry row exists** (`D250`, 13th run) | **ALPHA** (registry defect), and `S128` (09-09) is the accidental test |

---

## §5 · What this stage did NOT use
- 🚫 **`module_industry_map` was not run.** Its corpus is Korean and English seeds return 0 hits **by
  design** (a measured property of the tool, not a failure) — running it on a US-pure runtime would
  produce an empty result that reads like an absence of industry linkage. **Stated rather than run.**
  The US chain-linkage tool is `chain_hop`, and **no chain-hop pass was run this run either** — carried
  forward as a gap (the 08-26 run logged the same).
- 🚫 **News-velocity recount (the L2 `indicators` corroborant) was not run and could not be cited if it
  had been** — G1 FAIL removes the citation right for the whole run.

---

## DEEP_LOG 2026-08-27: continuous=[ENRG, HLTH] rotating=[INDU, STPL] · N=4/4 · **ONE verdict delta (DISC N→N−) from TEN attempts**, carried by four non-cap-weighted numbers (`eqflow` −0.339 rank 9 · red-rate 39.3% 2nd-worst · breadth 0.00 · `delta` −0.188 = board's largest negative, used as a rank not a magnitude) and admissible **only because the G3 flipper set moved off DISC between this run's own PREFLIGHT and its own SWEEP** · ★ **the delta CLOSES a 5-run contradiction rather than opening one (`M989`): DISC's flow-vs-price gap, logged as the board's widest `C5` gap since 08-22, is gone — MACRO's settled 08-26 frame now reads `exc1` −0.866 = worst of 11 and `med5` −1.227 = worst of 11, so both instruments agree for the first time** · **flip list 2 of 11 (HLTH/`LLY`/19.4% · ENRG/`XOM`/30.5%) and the set changed for a 4th consecutive run and for a 2nd consecutive run MID-RUN — PREFLIGHT attached DISC+MATR+ENRG at 22:1x KST and SWEEP measured HLTH+ENRG at 22:4x; the DISC restriction that lifted is the reason today's only delta exists at all** · ✅ **`D358-KR` did NOT fire here — MACRO §0 restated the standing line and it matched the 08-26 output exactly, the first clean inheritance in three runs across the two desks** · 🚨 **`D355` 3rd consecutive run: the sweep bar is a pre-market stub, median volume 4.65% of the prior session with 2 of 300 names above 50% (08-26: 2.48%, 0 of 299) ⇒ 5 🟢 / 67 🔴, all breadth figures and all `delta` magnitudes were DECLINED as levels and used only as cross-sectional ranks** · 🚨 **`M987`: the news-axis cap (`R103`) reproduced a 4th time INSIDE this run's own sweep — 50 velocity-covered names = `us_top300` ranks 1–50, contiguous, zero gaps; `vel_coverage` 16.7%, `n_axes` 3 for an 8th consecutive snapshot** · **rotating slots are a DECLARED recency-starved deviation for a 14th run: only 2 OW exist and both took continuous slots (ENRG 8th run, HLTH 8th), so R1/R2 were filled from non-OW by information content with least-recently-covered as the stated tiebreak** · ★ **`INDU` WINS the slot it lost on 08-26, and the reason is that the 08-26 run's own stated reason expired: it was declined then because "three instruments agree and a slot where nothing disagrees buys the least information", and today two things disagree — `exc1` +0.803 (3rd of 11) and `exc60` +4.490 (4th of 11) against `eqflow` rank 7, 15 reds (most on the board) and the worst 5-day breadth (26 of 50 negative) — plus a dated live catalyst (09-08 Canadian retaliation) that `D342` records as bracketed only by `S123`, which settles 09-12, four days LATE** · **`STPL` takes R2 to measure what §2's declined attempt #5 could not: a ONE-RUN-OLD `N−` whose price half refuses it (`exc5` +0.939 with only 4 of 19 negative against `eqflow` rank 8 / 36.8% red-rate / breadth 0.00 / 0 🟢), plus `ADM` — the named US casualty of Canada's dairy-and-agricultural retaliation list, flow −0.643 🔴분산 with OBV −0.154 분산 — carrying NO bracket anywhere, `D342`'s unbracketed half for a 3rd run** · **`DISC` LOST the 4-run tie EXPLICITLY** because this stage just made its two instruments agree and agreement is the cheapest information available; its verdict question went to PREMORTEM · **`COMM` skipped BY RULE for a 9th run (`D297`, `GOOGL`+`GOOG` ≈ 76.6% of 12 names)** · **`IT` deliberately routed to `P105` (09-09) + PREMORTEM rather than to a slot, 2-run recency** · **NO 5th slot promoted at this stage** · **uncovered=[DISC(N− — DEMOTED TODAY, 08-23 = 4 runs, tie-loser NAMED not dropped), UTIL(UW−, 08-23 = 4 runs, every instrument agrees — rank 11, red-rate 53.3% worst of 11, `exc20` −7.735 — lowest information on the board), COMM(N, 08-24 = 3 runs, un-measurable BY RULE 9th run), MATR(N, 08-25 = 2 runs, recency-blocked; zero-red reading declined as no-participation on a 4.65% bar, `P102` owns the two-name spread), IT(UW, 08-25 = 2 runs, `C16` carrier routed to `P105`), RE(N−, 08-26 = 1 run), FIN(N, 08-26 = 1 run — and it is the board's largest un-owned positive: `exc5` +2.105 and `exc60` +12.469, both 2nd of 11, with a 14.9% red-rate 3rd-best, against an `eqflow` rank 6 that will not carry a promotion)]**
