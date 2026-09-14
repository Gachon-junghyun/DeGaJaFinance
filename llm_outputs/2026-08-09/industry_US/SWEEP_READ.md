# SWEEP_READ — industry_US · 2026-08-09 (Sun) · Stage 3/10 (L1·SWEEP)

> The reading only. **Numbers live in `SECTOR_FLOW_US.json` · `US_LIVE_SHORTLIST.json` ·
> `CYCLE_EXPOSURE.json` and are cited, not reprinted.** Zero buy/sell, zero sizing.

## 1. Universe headline — three numbers

**n = 300 · wflow +0.033 · 22🟢 / 77🔴** (`SECTOR_FLOW_US.json §universe`, **asof 2026-08-07**).

⚠ **The sweep's `asof` is the same settled bar the 08-08 run swept.** Which makes the next section
possible, and it is this stage's main output.

---

## 2. ★★★ A control experiment fell out of the re-run: **same bar, different flow**

The 08-08 run reported **wflow +0.057 · 23🟢**. Today's re-run of the identical settled bar reports
**+0.033 · 22🟢** — a **−42% move in the headline and a lost green.** Diffed name-by-name against
`2026-08-08/SECTOR_FLOW_US.json`:

| Axis | names differing (of 300) |
|---|---|
| `last` (price) | **0** |
| `obv_norm` | **0** |
| `rs20` | **0** |
| `rs60` | **0** |
| `vol_surge` | **0** |
| **`velocity`** | **50** (non-null count 50 → **51**) |
| ⇒ **`flow_score`** | **37** |

⇒ **every price axis is byte-identical and only the news axis moved**, because the **2026-08-08 news
day completed after the 08-08 run executed at 09:10 ET**. **The headline flow of this desk's primary
sweep fell 42% on zero price information.**

★★★ **And the largest single move is `RTX`: `velocity` **None → 0.42**, `flow_score` **+0.639 →
+0.229 (−64%)**.** **RTX did nothing. The news pool merely learned it exists.**
⇒ **this is `D225-KR`'s mechanism reproducing on the US board**: a **null** velocity drops the 4th
axis and the name is scored on three (a free positive), while a **low** velocity enters as a penalty.
⚠ **W1 discipline**: what transfers here is a **code property of a shared module**, not a KR market
result — and it is verified on US data, not imported.
⚠ **And RTX is the same name `D217` records being cut 4 → 3 shares because the rank-3 GAP check
cannot fire.** Two instrument defects, one week, one name.

**The lost green is `MSFT`** — `vol_surge` **0.99**, `velocity` **1.15**. It cleared the gate
yesterday on a velocity that the completed news day revised **below 1.2**. **A tag flipped on a
completed denominator, not on a market event.**

---

## 3. Cross-checks against the MACRO matrix — one confirms, two contradict

**✅ CONFIRMS · Utilities.** Sector wflow **−0.395** and eqflow **−0.381**, **both the worst of 11 by
a wide margin**, 0🟢/11🔴 — and **ZERO of its 15 names even reach the `OBV-매집 ∧ RS20>0`
pre-condition.** The UW is the one verdict on the board that flow, breadth and the tape agree on
(MACRO §G: XLU exc5 −5.18 / exc20 −6.39, worst 20-day).

**🚨 CONTRADICTS · Materials — and it removes one of `S57-ANNEX`'s six legs.**
The 08-08 run listed *"the sector's 0🟢 of 12 with breadth 0.000"* as an independent leg supporting
Materials UW−. **Measured today: 5 of 12 Materials names DO pass `OBV-매집 ∧ RS20>0` and every one is
blocked by `vol_surge` alone** — NUE 0.95 · NEM 0.93 · STLD 0.90 · SHW 0.83 · ECL 0.83.
⇒ **the 0🟢 is a gate artifact, not evidence of absent accumulation** (the M238 class, replicated).
**S57 is not re-frozen and its thresholds are untouched — but ROTATION must not cite the green count
as a MATR leg**, and **S57's branch A still fires at any settled close through 08-12 from 0.59pp away.**

**🚨 CONTRADICTS · Consumer Discretionary.** wflow **+0.056** and eqflow **+0.057** — the only sector
whose two flow measures agree to within 0.001, i.e. **no mega-cap concentration at all** — with
**10 of 28 names passing the pre-condition and all 10 blocked by `vol_surge`**, one of them
(**DASH, 1.19**) **one hundredth of a point below the gate.** The sector carries **N** and reads as
`0🟢/8🔴` only because of the gate. ⇒ **the "no signal either direction" reading is right for the
wrong reason: there is a signal and the instrument cannot issue it.**

**The 🟢-gate mechanism replicates an 8th time across two markets**: **101 names pass
`OBV-매집 ∧ RS20>0`; 22 are 🟢; 79 are blocked and 79 of 79 fail on `vol_surge` alone**, with the
**highest `vol_surge` among all 79 = 1.19 against a 1.20 gate.**

**D161 executed on all 22 greens** (no 🟢 cited without decomposing which axis lit it):
**15 volume-lit** (`vol_surge` ≥ 1.2) vs **7 velocity-lit** (`vol_surge` 0.65–0.96, all on the stable
~50-name whitelist — **R59/D205**). ★ **Both Energy greens (XOM 0.88 · CVX 0.96) and three of four
Financials greens (JPM 0.65 · BAC 0.73 · BRK-B 0.85) are news tags on BELOW-average volume** — so
**the two sectors the sweep ranks #1 and #3 on wflow have no volume behind their greens**, exactly as
on 08-08. **JPM's 0.65 is again the lowest `vol_surge` of any green on the board.**

---

## 4. Shortlist — the absences, each diagnosed

`US_LIVE_SHORTLIST.json`: **15 names**, filter `mcap ≥ $10B ∧ 🟢가속`.
Composition by sector: **Industrials 4 · Health Care 4 · IT 3 · Comm Services 2 · Energy 1 · Financials 1.**

| Absent sector | Names passing the pre-condition | Diagnosis |
|---|---|---|
| **Utilities** | **0 of 15** | ✅ **EVIDENCE** — nothing is accumulating; the only clean absence on the board |
| **Consumer Discretionary** | **10 of 28**, all blocked by `vol_surge` (DASH 1.19) | 🚨 **FILTER ARTIFACT** |
| **Materials** | **5 of 12**, all blocked by `vol_surge` | 🚨 **FILTER ARTIFACT** — and it is an `S57-ANNEX` leg (§3) |
| **Real Estate** | **2 of 12** (DLR 0.70 · CBRE 0.74) | **mostly evidence** — a thin pre-condition pass, and both are deep below the gate |
| **Consumer Staples** | **2 of 19** (MDLZ 0.87 · HSY 0.67) | **mostly evidence** — consistent with the 08-08 UW− demote (worst eqflow **−0.173** and worst delta **−0.164** of 11) |

**Short-pressure verdicts read** (`us_flow` FINRA z): **13 of 15 △normal · 1 ✅clean-rise (XOM, z −0.59)
· 1 ⚡crowded-short (WAT, z +2.27 — squeeze fuel, turn-conditional, NOT a buy).**
⚠ **US has no investor-type feed**; this is a short-pressure proxy and is context, not a trigger.

---

## 5. 🚨 Universe integrity — the `D207` assertion executed on the full board

`volume = 0` on either of the last two settled bars **OR** `O=H=L=C` on both, over all 300 names in
the sweep's own price cache (`prices_2026-08-09.pkl`, last bar **2026-08-07**):

> **1 FAIL · 0 false positives · 0 names with insufficient data.**
> **`EA` — zero volume on BOTH bars AND degenerate OHLC on both — and it is tagged `🟢가속` with the
> board's highest `vol_surge` (3.66) and highest `obv_norm` (0.749), price frozen at 209.70.**
> **It is ALSO on the LIVE SHORTLIST, where the FINRA proxy returned a real short-z of +0.79 for a
> security that did not trade.**

**The check works, costs one pass over a cache the sweep already builds, and is wired into nothing.**
`D215` explains why nothing is fixed: `build_top300.py`, the rebuilder the sweep's own stderr
recommends, **does not exist in this repository**. **stderr was read IN FULL this run** (`[warn]
유니버스 us_top300.csv 25일 경과…` + download/progress lines only — no liveness warning exists to miss).

★ **A correction to `D215`'s own wording, measured.** D215 says *"a SECOND delisted name surfaced
independently, **X** (US Steel)"*, which reads as a second universe constituent. **`X` is NOT in
`us_top300.csv`** — the CSV holds exactly 300 tickers and its set is a **perfect 1:1 match** with the
sweep's 300 names (0 missing, 0 extra). ⚠ **Scope (C4)**: this does not say `X` is not delisted, nor
that no other desk file lists it. It says **the universe's constituent-liveness defect is EA and EA
alone**, so D215's *"second delisted name in the universe"* framing overstates by one. **D215's
core — that no rebuilder exists — is untouched.**

---

## 6. Cycle exposure — no GAP, and one phantom confirmed a 4th run

`CYCLE_EXPOSURE.json`: **AI-compute rank 1, epicenter 19.74% vs a 12.0% floor ✅** (held AVGO, NVDA,
ANET) · **Energy rank 2, 10.23% vs 8.0% ✅** (held **MPC, PSX**) · **Missile-defense rank 3, 6.15%,
⚪ 기준 미설정.** Book ≈ **$10,888 total, $6,361 invested**.

- ✅ **No top-rank GAP** — a genuine improvement on the 08-05/08-06 window, when M209 read **both**
  ranked cycles in GAP and M146 measured AI-compute clearing by **1.1 basis points**. Today's margin
  is **7.7pp**.
- 🚨 **`XOM` is again absent from the held Energy epicenter (MPC, PSX)** ⇒ **`S31`, which describes
  XOM as *"the only Energy name the book holds"*, has now described a position that does not exist
  for FOUR consecutive runs.** Handed to **PREMORTEM**: re-register exhaustively or retire.
- ⚪ **The rank-3 line is still un-fireable by construction** — `cycle_exposure.py:87`'s
  `cyc["rank"] <= 2` clause excludes rank 3 **categorically**, so setting the floor cannot fix it
  (**D217**, human-gated, code change).

---

## ✅ EXIT CHECK

- [x] `sector_flow --market us --json` → `SECTOR_FLOW_US.json` (asof 2026-08-07); sector ranking read; **`new_green` = 0 across all 11 sectors**
- [x] `US_LIVE_SHORTLIST.json` written; short-pressure verdicts read (1 ✅ · 1 ⚡ · 13 △)
- [x] `CYCLE_EXPOSURE` read — **no 🚨GAP**; the rank-3 ⚪ and the XOM phantom handed to PREMORTEM/ALPHA
- [x] **No table here exists in the JSONs** — sector rows and per-name rows are cited by artifact; what is printed is the cross-run diff, the gate decomposition, the absence diagnosis and the liveness assertion, **none of which the JSON can express**
- [x] **Cross-checks stated**: 1 confirming (UTIL), **2 contradicting (MATR — an S57-ANNEX leg; DISC)**; **every absence diagnosed as evidence vs filter artifact**
- [x] **Sweep stderr read IN FULL** (the HANDOVER instruction), not tailed
