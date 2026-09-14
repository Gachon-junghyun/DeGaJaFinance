# SWEEP_READ — industry_US · 2026-09-01 (Tue) · Stage 4 / L1·SWEEP

> **The reading, not a second copy of the data.** Numbers live in
> `SECTOR_FLOW_US_REPAIRED.json` · `SECTOR_FLOW_US.json` · `US_LIVE_SHORTLIST.json` ·
> `../CYCLE_EXPOSURE.json`. No sector row and no shortlist row is reprinted here (2026-07-21 rule).
> IDs: **M1183–M1189 · D453–D455**.

## 0 · 🚨 Instrument health line — read before any number below

`SECTOR_FLOW_US.json §scoring` (**primary**): `n_axes` **3** · `vel_axis` **false** ·
`vel_coverage` **16.05%** (48/299) · `scored` **299** · `dropped_missing_axis` **0** · asof **08-31**.
`SECTOR_FLOW_US_REPAIRED.json §scoring`: `n_axes` **3** · `vel_coverage` **0.0%** (news deliberately
not queried — a 300-call burst on an already-rate-limited tunnel) · `scored` **299** ·
`dropped_missing_axis` **0** · asof **08-31**.

**The news axis is DEAD this run, and the cause is the PIPE, not silence.** Probed, not assumed:
`fts search --days 7 --count --scope foreign` returned **6/6 pre-sweep and 4/4 post-sweep**, every
count **above** yesterday's, and a direct `news_velocity` falsification probe returned **10/10 alive**
— including the two names the price ranking puts at the universe floor (`PCAR` 1.29, `JCI` 1.07) and
one at **3.07** (`AON`). ⇒ 🚫 **no theme-freshness, no news-velocity, and no "sector X is quiet"
claim may be sourced from this sweep.**

🔴 **The PRIMARY file's OBV axis is revoked** (PREFLIGHT G0b): 259 of 299 scored names have their two
most recent sessions zeroed out of the 20-session OBV window; measured label-flip rate **29%**.
**Every number in this reading comes from `SECTOR_FLOW_US_REPAIRED.json`** (5m-proxy patch of the
08-28 hole, 258 names patched, residual OBV error 0.009 mean / 0.026 max, **0/42 label flips**).
**Δ is a TWO-session quantity** (08-27 → 08-31) — the 08-28 snapshot holds 1 key and cannot be an operand.

**`top1_flips_sign` — the full list, handed to ROTATION (which may not promote/demote on these):**
- **repaired (citable): 1 of 11** — **Consumer Discretionary · `top1` `AMZN` · `top1_w` 40.2%**
  (−0.282 → **+0.081** ex-top1).
- **primary: 2 of 11** — the same row **plus Financials · `top1` `BRK-B` · `top1_w` 13.9%**
  (−0.040 → +0.004, a sign flip on a 0.004 margin).
- ⚠ **The two instruments disagree about Financials**, so its sign is unestablished by either
  (`C26`, registered in HANDOVER §1d). Treat **Financials as a third barred bucket** for `wflow`.
- ⚠ `D424` shape (a **non**-flipper that is still a one-name story, in the opposite direction) —
  **two cases**: **Energy** (+0.302 vs ex-`XOM` **+0.471**) and **Comm. Services** (`wflow` −0.547 vs
  `eqflow` **−0.033**, `GOOGL` 38.3%).

**Held-but-not-in-universe check: ✅ 0 missing.** All 11 US book names are in `us_top300.csv`
(300 rows). ⚠ The universe file is **48 days old** (mtime 2026-07-15) ⇒ cap-weight is not "current size".

**`CYCLE_EXPOSURE` GAP: ✅ none.** AI-compute epicenter **16.85%** (need ≥12.0) · Energy/refining
**10.28%** (need ≥8.0) · missile-defense 3.77% (no threshold). ⚠ Registry still carries **no
AI-power/grid row** (`D416`) and **no optical row** (`D250`, 17th run) ⇒ zero exposure to those is
**unstatable, not measured**. Nothing to hand ALPHA's action bracket.

---

## 1 · Universe headline — three numbers

**n 299 · wflow −0.156 · 6 🟢 / 84 🔴.** (Primary reads −0.126 / 13 🟢 / 78 🔴 — the repair moved the
board **more negative and narrower**, which is the direction the corrupted OBV was hiding.)

---

## 2 · Cross-checks against the MACRO transmission matrix

### ✅ CONFIRMS — Energy `OW`, on four independent legs
Rank 1 on **both** axes; **`eqflow` +0.387 > `wflow` +0.302 ⇒ breadth-led, not mega-cap-narrow**;
**0 reds of 16**, the only sector on the board with `breadth` above zero; **Δ +0.353, the best on the
board by 2×**; and ★ **the only two `new_green` ignitions in the entire 299-name universe are `SLB`
and `WMB` — both Energy.** `M1183` [measured]. The MACRO matrix put Energy first on tape
(`exc20` +7.56pp vs `SPY`); the flow instrument agrees through a different quantity.

### 🚨 CONTRADICTS — Information Technology, and this is the run's sharpest disagreement
`M1184` [measured]. **Two instruments, opposite breadth verdicts, same sector, same settle date:**
- **`S124` (scored today)**: **41 of 56** IT names have a **positive 5-session excess vs `SPY`** —
  above the trailing-252 **p85 of 39**.
- **This sweep**: IT `eqflow` **−0.014**, **3 greens against 9 reds**, and the sector's two worst
  names on the whole board are IT (`AMAT` −0.889, `WDC` −0.861).

**The diagnosis, not a shrug**: `flow_score` is `OBV + RS20 + vol_surge`; `S124` is pure 5-session
excess return. A name can beat `SPY` for a week **on falling volume** and still score 🔴.
⇒ **IT is up on price and down on participation.** **ROTATION must state which quantity its IT
verdict is about** — and per HANDOVER §5 the desk's own IC scoreboard says the *participation* axis
(`vol_surge`) has a **negative** measured sign (t(NW) **−3.51**, Bonferroni-passing) — on a **KR**
ledger, so `W1` bars using that to break the tie here. **The tie is named, not broken.**

### 🚨 CONTRADICTS — Materials `OW`
`M1185` [measured]. **0 greens / 2 reds of 12**, `eqflow` **+0.030** (flat, rank 5), and the entire
`wflow` +0.148 is `LIN`'s 24.7% (ex-`LIN` **+0.115**, *below* the headline). It **fell from rank 1 to
rank 2** on the repaired file. ⚠ `C24` reproduces a third time: this sits against **copper spec
positioning at the 100th percentile of its year** `[COT 08-25]`. **An OW with no ignition and a
crowded underlying.**

### 🚨 CONTRADICTS — Financials `OW−`
`M1186` [measured]. **0 greens of 47 — the largest bucket on the board with none — against 13 reds**,
both axes ≈ **−0.19**, Δ **−0.047**. This is the **second consecutive run** with zero greens in
Financials. ⚠ And it is now also a **barred bucket** on `wflow` (§0), so ROTATION's substitutes are
`eqflow` (−0.186), the red count, and the tape (`XLF` `exc2` **+0.23pp vs `SPY`**, `exc5` −1.34).
**Flow and tape still point opposite ways** — which is exactly what `S134` (settles 09-04) brackets.

### ✅ CONFIRMS — the three underweights
Industrials **23 reds of 50 (worst absolute on the board)**, `eqflow` −0.365, **Δ −0.225 (2nd-worst)**.
Utilities **10 reds of 15 = 66.7%, the worst rate**, `eqflow` −0.454 rank 11/11.
Consumer Discretionary **12 reds of 28**, Δ −0.146. All three agree with MACRO §E's 20-session tape
(`XLI` −5.62 · `XLU` −6.04 · `XLY` −2.61 vs `SPY`).

### ⚠ NEITHER — Communication Services `OW−`
`wflow` **−0.547** against `eqflow` **−0.033**: a **0.514 gap, the widest on the board.** `GOOGL` at
38.3% owns the entire negative without technically flipping. `D297` already rules this bucket
un-measurable (n=12). **No confirmation and no contradiction is claimed** — the instrument cannot
produce one.

---

## 3 · Shortlist composition — the absences, diagnosed. **They are a filter artifact this run.**

`US_LIVE_SHORTLIST.json`: **6 names** from `mcap ≥ $10B · tag 🟢가속 · flow desc top15`, drawn from
**three** sectors (IT 3 · Energy 2 · Health Care 1). **Eight of eleven sectors produced nothing.**

★ **`M1187` [measured] — the absence is NOT evidence, and the whole difference is 0.2 of `vol_surge`.**
Counting the underlying axes directly on the repaired file:

| condition | count |
|---|---:|
| OBV **매집** ∧ `rs20 > 0` (accumulating **and** beating `SPY` over 20 sessions) | **88** |
| … ∧ `vol_surge ≥ 1.0` | **15** |
| … ∧ `vol_surge ≥ 1.2` (**= today's 🟢 set**) | **6** |

The **9-name band excluded by the last 0.2** is: **`NEM` 1.19 · `KMI` 1.11 · `ABNB` 1.10 ·
`COIN` 1.09 · `MPC` 1.08 · `TGT` 1.07 · `ADSK` 1.07 · `FCX` 1.06 · `RSG` 1.05** — spanning
**Materials (2) · Energy (2) · Cons. Disc. · Financials · Staples · IT · Industrials**, i.e. **five of
the eight "empty" sectors have an accumulating, outperforming name that missed the tag on surge alone.**
★ **`NEM` misses by 0.01.** (`C5` — an arbitrary threshold doing load-bearing work.)

★ **`M1188` [measured] — and with the news axis dead the 🟢 gate silently became STRICTER, not looser.**
`flow_tag` requires **`green ≥ 3` of four axes AND conviction**; with `vel = None` the news green can
never fire, so the ceiling is 3 ⇒ **a name now needs all three price axes positive, unanimously.**
⚠ This is the **opposite direction** to the 2026-08-09 defect, which inflated every score by +0.305
when the axis dropped. ⇒ **the 6-green count is a floor produced by a dead pipe, not a level**, and
any downstream sentence of the form "only six names are accelerating" is measuring the tunnel.
⇒ **`D453`**.

★ **`M1189` [measured] — the 2026-07-21 refiner artifact reproduces exactly.** `MPC` (`flow +0.711`,
OBV **+0.427 매집**, `rs20` **+20.4**, `rs60` **+38.5` vs `SPY`) ranks **9th of 299** and is excluded;
`PSX` (+0.617, `rs60` +32.6) ranks **18th** and is excluded. **Energy's shortlist of 2 understates the
sector**, and the two names understated are the two the book actually holds.
⇒ **`D454`**: *a shortlist absence is diagnosed against the underlying axis counts before it is cited
as evidence* — the 2026-07-21 rule said exactly this and this run is the first to execute the check
and find the absence **fails** it.

★ **`D455`** — *the 🟢 filter is keyed on `vol_surge`, which is the one axis this desk's own IC ledger
gives a significant NEGATIVE sign (t(NW) −3.51, `n_eff` 41, Bonferroni-passing).* The shortlist is
therefore selecting on the axis the scoreboard says is inverted. 🚫 **Not acted on** — the ledger is
`market=kr` and `W1` bars the transfer (`D428`). **Registered so the next run does not re-discover it.**

**Genuine absences (green = 0 in the underlying data, no near-band name):** Real Estate (5 reds of 12)
and Communication Services (3 reds of 12). Those two are evidence.

---

## 4 · What ROTATION inherits from this stage
1. **Energy is the only sector confirmed by tape, flow, breadth and ignition simultaneously.**
2. **IT's two instruments disagree about breadth** (41/56 positive excess vs `eqflow` −0.014,
   3🟢/9🔴). The verdict must name its quantity.
3. **Barred from `wflow` promotion/demotion: Consumer Discretionary (flipper), Financials
   (instruments disagree), Communication Services (`D297`, un-measurable).**
4. **Materials is an OW with zero ignition and a 100th-percentile crowded underlying.**
5. **The shortlist's emptiness is a `vol_surge` threshold artifact, not a market fact** — do not read
   "8 of 11 sectors have nothing" as breadth evidence.

---
> Output: `SECTOR_FLOW_US.json` (primary, OBV revoked) · `SECTOR_FLOW_US_REPAIRED.json` (citable) ·
> `US_LIVE_SHORTLIST.json` · `../CYCLE_EXPOSURE.md/.json` · this file.
