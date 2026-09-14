# SWEEP_READ — industry_US — 2026-07-28 (Tue)

> Stage 3/10. **The reading, not a second copy of the data.** Sector rows and per-name rows live in
> `SECTOR_FLOW_US.json` and `US_LIVE_SHORTLIST.json` and are cited, never reprinted.
> Benchmark **SPY** inline (C1). Analytical only (P4).

## 1 · Universe headline

**n = 300 · wflow +0.121 · 🟢 24 / 🔴 65 · `asof 2026-07-27` (settled).**

## ⚠ 0 · D74 FIRED — the first sweep of this run was contaminated, and it is logged rather than hidden

The stage's first `sector_flow --market us` call executed at **09:38 ET, eight minutes into the live
2026-07-28 session**, and silently stamped `asof: 2026-07-28`. **Measured contamination on the bar it
used**: SPY **9.2%** of the prior session's volume · NVDA 8.9% · DLR 5.0% · WAB 4.6% · CSX 3.7% ·
VLO **3.0%**. Prices confirm it read the partial bar, not the settle (MU `last` 822.87 against a 07-27
close of **900.20**; MA 562.02 against 551.71).

**Remediation performed, and stated so it is auditable:**
1. `llm_outputs/sector_flow/prices_2026-07-28.pkl` → backed up as `.contaminated.bak`, then **trimmed
   to bars ≤ 2026-07-27** and the sweep re-run. Result: `asof 2026-07-27`, wflow +0.121, 🟢24/🔴65.
2. The contaminated **`history.json` snapshot keyed `2026-07-28` was removed** (backed up first) so
   that `new_green` does not diff today against a partial bar.

⚠ **A second, separate finding surfaced while doing (2): `history.json` has NO snapshot for 07-25 or
07-27 — its last settled key is `2026-07-24`.** So **today's `new_green` is a 3-session delta, not a
day-over-day ignition**, and must not be read as "ignited overnight". This is D79's US analogue and it
is filed as **D89**.

⇒ **D74 is now measured on TWO US runs (07-27, 07-28) and remains unfixed.** The minimum fix stated on
07-27 — *drop the final bar when its volume is <~60% of the trailing-20 median, or expose `--asof`* —
would have prevented both. **The script still has no `--asof` flag** (verified from `--help`).

## 2 · Cross-checks against the MACRO matrix — where money and matrix agree, and where they don't

**CONFIRMS the matrix (4):**

| Matrix line | The money |
|---|---|
| **Energy OW−** | **#1 sector on wflow (+0.435) with the board's best breadth (0.19)** and eqflow +0.281 ⇒ not a single-name artifact. The tilt is the best-funded on the board |
| **Info Tech N, "split unconfirmed" (P3/P10)** | ★★ **The widest wflow−eqflow gap on the board: +0.169 vs −0.132 = 0.301** with **20 reds of 56, the worst red count anywhere.** The label is mega-cap-narrow *by measurement*, on an axis independent of the RS panel MACRO used |
| **Utilities N− (S24)** | **0 greens of 15, wflow −0.381, eqflow −0.380, delta −0.226.** ★ **PCG — carried in STANDING_VIEW §3a as "Utilities' only 🟢" — is 🟡 today** (flow +0.376, RS20 −0.1). S24's basket median RS20 reproduces at **−5.65** |
| **Financials OW−, "breadth-led"** | **eqflow +0.339 > wflow +0.304** — the signature holds, gap **+0.035**. ⚠ But M173 measured this gap at **+0.064 → +0.028 once BRK-B is removed**; at +0.035 raw it is **narrower than the run in which the desk first called it breadth-led** |

**CONTRADICTS the matrix (3) — stated with which side the money is on:**

1. ★★★ **Materials.** The matrix carries **UW** and MACRO §E-9 recorded that its own deferred price
   test **ran and went against it** (XLB beat SPY on both the 1-day and 5-day windows). **The flow says
   the opposite of the price: wflow −0.328, eqflow −0.237, 0 greens of 12, breadth 0.0 — the second-worst
   sector on the board.** ⇒ **Price and flow disagree on the one tilt that owes a re-argument.**
   **The money is on the UW; the tape is not.** ROTATION owns this.
2. ★★ **Health Care.** The matrix carries **N** with C7 open. The flow just collapsed: **1 green of 32
   (was 6, then 5), delta −0.228 = the largest negative delta on the board**, eqflow +0.009 ≈ zero.
   ⚠ **And the single surviving green is a diagnosis, not a signal** — **JNJ is 🟢 on `velocity` 2.57
   with `vol_surge` 0.96**, and MACRO §C-4 identifies the news that produced it: **the $5.5bn talc
   settlement, 10 articles / 10 outlets.** ⇒ **C7's "money without narrative" has inverted into
   "narrative without money", and the resolving observable (one 🟢 from outside the top-6 by cap) is
   now measured at ZERO of 32 rather than zero of 26.** The money left; the matrix has not moved.
3. ★★ **Energy's internal direction is inverted relative to the desk's own thesis.** The sector is #1
   on flow, but its **three greens are SLB, XOM and CVX** — and **XOM/CVX are green on a velocity path**
   (`vol_surge` 0.82 / 0.78, `velocity` 3.02 / 2.14) **with NEGATIVE RS60 (−3.8 / −5.0)**, i.e. exactly
   the "base-less integrated leg" M177 named. **The three refiners are not green at all** (see §3).
   ⇒ **The tag points at the leg MACRO says has no base and away from the leg it says has one.**

## 3 · Shortlist composition — the absences, each diagnosed

`US_LIVE_SHORTLIST.json` (mcap ≥$10B ∧ 🟢 ∧ top-15 by flow) returned 15 names. **The composition is
the finding: 4 of the top 5 are rail/freight Industrials (WAB, CSX, UNP, NSC) and the #1 is T.**

| Absence | Diagnosis | Verdict |
|---|---|---|
| ★★★ **No refiner (VLO · MPC · PSX)** | All three are **OBV 매집 with RS20 +16.2 / +21.6 / +19.7 and RS60 +17.5 / +25.3 / +15.9** — two of three axes pass — and all three are blocked by **`vol_surge` 0.84 / 0.98 / 0.96 < 1.2** with `velocity` **None** | **FILTER ARTIFACT, not evidence.** This is the 2026-07-21 measured case reproduced exactly. **ROTATION may not read "no refiner in the shortlist" as flow leaving the refining leg** |
| ★★ **No memory or equipment name** | MU 🔴 (−0.318) · AMAT 🔴 (−0.400) · LRCX 🔴 (−0.312) · KLAC 🔴 (−0.321) · SNDK 🔴 (−0.179) — **OBV 분산 on all five**, RS20 −18.9 to −40.2 | **EVIDENCE.** Three independent axes agree (RS, OBV, tag). ⚠ **STX is the near-miss and it matters: 🟡 with OBV 매집 and `vol_surge` 1.17 — it fails the gate by 0.03 on the day before its print** |
| ★★ **Utilities 0 of 15 · Materials 0 of 12 · Staples 0 of 19** | breadth **0.00** at all three; wflow −0.381 / −0.328 / −0.142 | **EVIDENCE** for Utilities and Staples. ⚠ **Materials contradicts its own price (§2-1)** |
| ★ **Real Estate: only PLD** | **EQIX −0.629 · AMT −0.618 · CCI −0.551, all 🔴분산**; DLR 🟡 with **RS20 0.0** | **EVIDENCE, and it re-confirms P5**: DLR's 20-day excess has fully retraced, and the reds are the tower/data-centre names again — **not** a duration signature |
| ★ **Security/observability absent** (PANW · CRWD · FTNT · DDOG) | RS60 **+70.9 / +55.4 / +73.1 / +84.1** against RS20 **+2.9 / +1.4 / −0.7 / +3.7**, `vol_surge` 0.61–0.75 | **BOTH.** The RS60 is real and the RS20 is gone — this is C6-bis's decaying-stock shape on the desk's only A-grade-verified node, and **FTNT is now OBV 분산** |
| ★ **HPE absent, DELL present** | **HPE `vol_surge` 0.46 — the lowest measured on the probe — and `velocity` None ⇒ 🟡.** DELL is 🟢 **only via velocity 2.35 with `vol_surge` 0.58** | **BOTH ARE ARTIFACTS.** Neither tag carries information; **the DELL/HPE case rests on RS (A-grade) alone**, which is where §3a already puts it. ⚠ **No stage may call DELL "volume-confirmed"** |
| ★ **TRV absent** | flow **+0.750 — higher than 9 of the 24 greens** — RS20 +17.9 / RS60 +25.3, blocked by `vol_surge` **1.15** | **FILTER ARTIFACT.** Financials' green count of 5 **understates** the sector |

## 4 · ★★★ The 🟢-gate mechanism replicates a SIXTH time — and this run measures the half that reverses M25

| Measurement | Value |
|---|---|
| Names passing `OBV 매집 ∧ RS20 > 0` but **not** 🟢 | **70** |
| …of which blocked by **`vol_surge` < 1.2 alone** | **70 / 70 = 100%** |
| `velocity` non-null | **50 / 300** |

★★ **And the other half, which the US desk has never measured before: 14 of the 24 greens carry
`vol_surge` < 1.2 and clear on `velocity` alone** — XOM 0.82 · JNJ 0.96 · BAC 0.95 · JPM 0.83 ·
NVDA 0.81 · AAPL 0.78 · CVX 0.78 · PLTR 0.75 · MSFT 0.69 · MA 0.68 · META 0.65 · V 0.62 ·
AVGO 0.61 · DELL 0.58 — every one with `velocity` ≥ 1.43.

⇒ **M25 is superseded on its central clause.** M25 states: *"`vel` is **None on all 300 US rows**, so
🟢 requires OBV ∧ RS20>0 ∧ vol_surge≥1.2 (3-axis unanimity)."* **Measured today: `velocity` is non-null
on 50 of 300, and 58% of the greens clear on it.** The US gate is a **3-of-4 vote exactly like KR's
(M165)**, not a 3-axis unanimity — which means **58% of today's US greens mean "the news is loud", not
"the volume confirms"**, and that is the KR finding replicating in the second market.
⚠ **D75's stronger claim (*"`velocity` null on 300/300"*) does NOT reproduce** — it is 250/300 null,
matching M144. D75's *mechanism* (the axis is unwired on one call path) survives; its magnitude does not.

**Immediate consequence for this run**: **META, MSFT, NVDA, AVGO and DELL are all 🟢 on velocity with
`vol_surge` 0.58–0.81, on the eve of their prints.** A stage reading those five greens as accumulation
would be reading pre-earnings press coverage.

## 5 · Cycle-exposure GAP — **both** ranked cycles now flag, and one flipped on drift alone

`CYCLE_EXPOSURE.json` (live read-only KIS account call). Book ≈ **$11,527**, invested **$4,398**
⇒ roughly **62% cash**.

| Cycle | rank | epicenter % | need | margin | held epicenter | flag |
|---|---|---|---|---|---|---|
| AI-compute / semiconductors | 1 | **8.23%** | 12.0% | **−3.769pp** | AVGO, NVDA, TSM | 🚨 GAP |
| Energy / oil-refining | 2 | **7.67%** | 8.0% | **−0.327pp** | **PSX, XOM** | 🚨 **GAP (was ✅)** |
| Missile-defense | 3 | 7.65% | — | — | RTX | ⚪ no threshold set |

★★★ **M181's pre-registered warning is vindicated by a measurement, one session later.** It wrote:
*"Energy's +0.027pp is inside [D61's proposed 0.5pp band] ⇒ that ✅ is UNRESOLVED, not a pass."*
**It flipped to 🚨 the next session, a −0.354pp move, with the held names unchanged in kind.**
⇒ **D61's proposal — report `margin_pp` as a first-class field and treat |margin| < 0.5pp as
UNRESOLVED rather than PASS — is now supported by a live flip, not only by back-reading.** Escalated;
a threshold change needs a human.

★★ **Two book-composition changes are visible in this artifact and are reported as observations, not
conclusions** (M182 established `cycle_exposure` as authoritative on holdings):
- **Energy's held epicenter went `XOM` → `PSX, XOM`.** **PSX is the registry's human-locked `core_pick`
  that M146/M181 flagged as *unheld* across five consecutive runs.** It now reads as held.
- **`any-layer %` collapsed on both cycles** (AI-compute 26.39% → 14.84%; Energy 21.73% → 14.28%) and
  the adjacent list went **(VST, KMI, LNG) → (LNG)**.
⚠ **n = 1 session (S1).** These are read from one account call and are recorded so the next run can
confirm or refute them; **no stage may build a thesis on a one-session book delta.**

⚠ **D60 reproduces unchanged**: the artifact's footer cites `data_build/cycles/cycle_registry.json`,
**a path that does not exist** (verified — the registry is at `data/cycles/cycle_registry.json`), and
that registry is **`updated: 2026-07-17` = 11 days stale with 3 rows.** The GAP guard can only see
cycles someone wrote down, and **four of the board's strongest RS60 names (DELL +103.7, DDOG +84.1,
FTNT +73.1, PANW +70.9) sit in no row at any layer.**

## 6 · Handed to ROTATION

1. **Energy is the best-funded tilt on the board (#1 wflow, best breadth) — and its tag points at the
   wrong leg inside it.** The refiner absence is a filter artifact; the integrated greens are velocity paths.
2. **Info Tech's mega-cap-narrow signature is now measured on flow as well as on RS** — 0.301 wflow−eqflow
   gap, 20 reds of 56, and **zero memory/equipment greens**, with STX missing by 0.03 the day before it prints.
3. **Health Care contradicts the matrix**: 6 → 5 → **1 green of 32**, the board's largest negative delta,
   and the one green is a **litigation-settlement velocity artifact**.
4. **Materials contradicts itself**: the flow is the second-worst on the board while the price beat SPY on
   both windows — and this is the tilt whose deferred re-argument is due.
5. **Both ranked cycles flag 🚨 GAP**, one of them having flipped from ✅ on 0.354pp of drift.
6. ⚠ **Two instrument caveats that bind every number above**: `new_green` is a **3-session** delta
   (D89), and **58% of the greens are velocity paths, not volume confirmations** (§4).
