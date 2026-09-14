# HANDOVER — industry_US · 2026-09-01 (Tue) · Stage 2 / L1·HANDOVER

> Runtime `--market us`. Inheritance step: read the carry BEFORE forming any view.
> Run clock **KST 22:09–22:5x = ET 09:09–09:5x, Tuesday, PRE-OPEN.** The 09-01 US session had not
> begun when this stage executed. Last completed US session **Mon 2026-08-31**.
> IDs issued by `module_evidence next-id` (M1161–M1182 · D445–D452 · R120–R123 reserved; highest
> existing **M1160** / **D444** / **R119**), not hand-grepped.

★ **The one thing that makes this run different from the last five: there is a settled session
behind it, and eleven pre-registered rows became readable at once.** The 08-30 and 08-31 runs each
scored **zero** rows for a structural reason (`M1127` / `D426` — this desk fires pre-open). Today
the 08-31 close exists, the ghost bar healed at the head of the series, and FRED caught up.
**Eleven rows settled: 3 fired a directional branch, 8 fired C, 0 silent skips.**

---

## 0 · Instrument health inherited — read BEFORE any number is trusted

`llm_outputs/2026-09-01/industry_US/preflight/PREFLIGHT.md` **was run**, this run, before this stage.
Verdicts: **G0 🟡(head healed / 08-28 holed) · G1 🔴 · G2 ⚠PASS-scale/Δ-undefined · G3 ✅ · G4 🔴 ·
G5 🔴 · G6 🔴 · G7 🟡.**

**Revoked today — binding on every later stage:**

| Revoked | Which stages it binds |
|---|---|
| **OBV / accumulation-distribution / flow score from the PRIMARY `SECTOR_FLOW_US.json`** — 259 of 299 names have their two most recent sessions zeroed out of the OBV window; **measured label-flip rate 29%** | SWEEP · ROTATION · DEEP · BET |
| **Any Δflow from the primary file** (null on 299/299) · **any Δ called a one-day move** — the only valid baseline is **08-27**, two sessions back | SWEEP · ROTATION |
| **`wflow` promotion/demotion of Consumer Discretionary** (`AMZN` owns the sign at 40.2%) · **any `wflow` claim about Financials** (primary and repaired disagree on its sign) · **"Comm. Services is worst" from `wflow` alone** (`eqflow` +0.054) | ROTATION §2 |
| **News velocity / theme freshness / "sector X is quiet"** *sourced from the sweep* (16.05% coverage; **10/10** direct re-probes alive, incl. the universe's bottom two) | SWEEP · ROTATION · EVENT_ALPHA · DEEP |
| **08-28 closes from the daily endpoint for the 259 unbackfilled names** · **any 08-28 volume or volume-magnitude claim from either instrument** | every stage |
| **Concentration as a single number** (G4) · **cap-weighted "current size"** (G5, universe **48 d** stale) · `kelly_size --ic` as evidenced (G6) | SIZE · BET · ALPHA |
| **Anything about the 09-01 tape** — the market had not opened | every stage |

**Granted today, with a mandatory label on the same line as the number:**
- ★ **the 08-31 session, PLAINLY and with no proxy label** — 1/301 NaN (EA only). `module_paper_book
  status` and `pulse` are current again (`status` prints `ANET` **195.69** = the real 08-31 close).
  **Yesterday's staleness revocation is LIFTED.**
- **`SECTOR_FLOW_US_REPAIRED.json`** (299 scored, 3-axis `nonews`, asof **08-31**, 258 names patched at
  08-28) — label `repaired sweep, 5m-proxy`;
- **Δflow vs the 08-27 snapshot** (299/299 common names, same `nonews` mode) — label
  `repaired sweep, 08-27 → 08-31, two sessions`;
- **`module_chart`** — live **3/3** today (0/3 yesterday). **US chart-shape citation is RESTORED**;
- **direct** news queries (≤11 consecutive, ~90 s pause if refused).

★ **`M1161` [measured] — the ghost bar healed at the head and froze at 08-28.** 08-31 Close NaN
**1 of 301** (the 1 is `EA`, which the 5m endpoint also refuses); 08-28 remains **259 of 301** at T+4.
The 08-30/08-31 runs' framing ("a rolling T-1 hole") is superseded: **it is a fixed hole at one date.**
Two tools recovered on their own as a direct consequence — the sweep scored **299/299**
(`dropped_missing_axis=0`, after two consecutive `scored=0` runs) and `module_chart` renders 3/3.

★ **`M1162` [measured] — the fixed hole is NOT cosmetic, and its size is now measured rather than
asserted.** On the 42 names the vendor did backfill, blanking their 08-28 bar — i.e. simulating what
the other 259 suffer — shifts `obv_norm` by **0.0652 mean / 0.4040 max**, flips the
accumulation/distribution **label on 12 of 42 (29%)** and the **sign on 7 of 42 (17%)**. Mechanism is
exact: `np.sign(close.diff())` is NaN at 08-28 **and** 08-31 when the prior close is missing, so
`.fillna(0)` assigns **direction zero to the two most recent sessions** of a 20-session window.
⇒ this is why the primary file's OBV axis is revoked above.

★ **`M1163` [measured] — yesterday's 5m proxy is confirmed against the settle, and one of its stated
warrants was too generous.** Seven names in yesterday's published 08-28 proxy tape were backfilled
overnight: **7/7 within 0.04pp** (`NVDA` proxy −4.58% vs official **−4.57%**; `SPY` −0.22% vs
**−0.23%**; `HPE` −3.90% vs **−3.86%**; `AVGO` −0.77% / −0.74%; `QQQ` −0.65% / −0.65%; `XLE` +0.59% /
+0.63%; `XLF` +0.36% / +0.38%). **Yesterday's 08-28 statements stand.**
⚠ But re-validated on 42 official closes the proxy's max error is **0.0937%** with **4 names over
0.05%**, against yesterday's stated **0.0448% max / 0 over**. ⇒ **`R120`** below.

★ **`M1164` [measured] — the proxy's VOLUME leg was never validated and it is biased −18%.**
5m volume sums run **−18.15% mean · −14.52% median · −4.74% … −54.58%** against the official bar (they
miss off-exchange and closing-auction prints). Measured **through to the axis it feeds**: the repair's
residual `obv_norm` error is **0.0090 mean / 0.0262 max with 0/42 label flips** — **~7× smaller than
the error it removes.** ⇒ the repair is kept, and the volume caveat rides on the label.

---

## 1 · Inherited standing view

### 1a. Regime call — carried unchanged, `[inferred]`, still barred from citation as evidence
Carried with its `[inferred]` tag intact and explicitly barred. **`P111` (settles 09-14) remains the
registered test.** This stage does not move the call and does not cite it.

### 1b. Sector verdicts carried in from 2026-08-31
`ENRG OW` · `HLTH OW` · `MATR OW` · `FIN OW−` · `COMM OW−` · `IT N` · `STPL N` · `DISC UW` ·
`INDU UW` · `RE UW` · `UTIL UW`. DEEP that run: continuous `[MATR, HLTH]`, rotating R1 `[ENRG]`,
**R2 deliberately unfilled ⇒ N = 3/4**. These are inherited, not re-derived here — ROTATION owns them.

⚠ **Two of the eleven cannot be re-argued on `wflow` today** (PREFLIGHT G3): **Consumer Discretionary**
(`AMZN` 40.2%, −0.282 → **+0.081**) and **Financials** (the primary file calls it a flipper on a 0.004
margin; the repaired file does not — **the instruments disagree, so its sign is unestablished**).
⚠ **`D424` re-checked against today's board** — a `top1_flips_sign=False` bucket can still be a
one-name story in the *opposite* direction. **Two now show that shape**: **Energy** `wflow +0.302` vs
`ex-XOM` **+0.471** (XOM dragging a broader positive) and **Comm. Services** `wflow −0.547` vs
`eqflow` **+0.054** (GOOGL's 38.3% owns the whole negative). Health Care, last run's `D424` case, has
**narrowed**: +0.069 vs ex-LLY +0.115.

### 1c. Retracted ledger (§5) — read BEFORE forming today's view
Read through the tail (`R110`–`R119`). The entries that bind this run:

| id | what may not resurface |
|---|---|
| **`R110`** | "The foreign news ingest has been dark." The server was current; the client mirror was stale. ⇒ any "the news went quiet" claim must state **which side was queried**. ✅ complied: today's 6/6 pre-sweep counts are all **above** yesterday's |
| **`R111`** | "`MU` has no take-or-pay." Killed by the FY26Q3 10-Q ⇒ the take-or-pay frame **does** transfer to memory |
| **`R113`** | Do not assume a KRX-side event is unpriced because the speech post-dated the close |
| **`R114`** | Reconstruct observation times from **mtime / the actual command sequence**, not memory (`D400-KR`). ✅ complied: PREFLIGHT's timeline is the real command order, and the two long jobs (sweep, repair) name their own log files |
| **`R115`** ★ | **"`fast_info.previousClose` is a third recovery path for the 08-28 ghost."** Killed by widening n from 1 to 24: mean abs err **0.394%**, max **3.208%**, **17 of 24 above the 0.05% bar**. ⇒ **directly binding today** — this run did **not** reach for `previousClose`; the recovery used the 5m endpoint, and its error was re-measured on 42 names rather than inherited |
| **`R116`** | "Brent fell despite the escalation." It was a **front-month roll** in `BZ=F` (Brent−WTI 5.91 → 2.61 in one session). ⇒ **binding on `S92` today**: the Hormuz reading is taken on **`CL=F`**, as the row itself freezes, and no Brent sentence is written |
| **`R117`** | An asof misalignment does not damage a fixed axis — **it swaps which axis is damaged** with the shape of the missingness. ⇒ binding: today the missingness moved from the head to a fixed interior date, and PREFLIGHT re-measured **OBV** (not `rs20`) as the damaged axis rather than carrying yesterday's answer |
| **`R118`** | An anti-signal can fire into a state that **neither branch covers**. Threshold not moved; the row is discarded, not re-banded |
| **`R119`** | Do not call a multiple "expensive because the denominator is at a peak" without the margin series |

⚠ **`R89` + `P83` still bar any refining-margin-vs-barrel separation claim** — relevant because
`MPC` **+2.69%** and `PSX` **+2.82%** are again the book's two best 08-31 names (official closes).

### 1d. Open contradictions carried, NOT resolved
- **`C21`** — RSI convention, untouched. ⚠ The related defect (`us_setup_screener` dropping the void
  bar) is **now moot at the head** but still applies to any window spanning 08-28.
- **`C22`** — the two ledgers name different hands. **No new sample: both `due` runs returned 0 rows.**
- **`C23`** — **two books, and every stage reads whichever one its tool opens.** ★ **Reproduced again
  with fresh numbers** (§4).
- **`C24`** — Materials' flow axis vs its positioning axis. ⚠ **Today it half-inverts**: Materials
  falls from rank 1 to **rank 2** on the repaired file (`wflow +0.148`, `eqflow +0.030`, **0 greens /
  2 reds of 12**) while **Energy takes rank 1** (`+0.302`, `eqflow +0.299`, `breadth 0.190` — the only
  sector on the board with breadth above zero). Carried; **not** resolved by picking a side.
- **`C25`** — the desk's two instruments read OBV's sign oppositely on one name (KR-registered).
  ★ **The US analogue is now tested and it is worse than a name-level disagreement**: `M1162` shows the
  *same* instrument gives two different OBV signs depending on whether one interior bar is present.
- **`C26`** ★ **new, US, registered here** — **the primary and repaired sweeps disagree about which
  sectors are one-name buckets** (primary: Cons. Disc. + Financials; repaired: Cons. Disc. only), and
  they disagree about the board's **rank 1** (primary Materials +0.269; repaired Energy +0.302).
  Both files were produced by the same engine on the same day from the same cache. **Carried, not
  resolved** — the repaired file is the citable one, but the fact that a 20-session axis reorders the
  board on one missing interior bar is a finding about the axis, not about the sectors.

---

## 2 · Scenario scoring — eleven rows settled, every past-dated row named

★ **`M1165` [measured] — the backlog cleared in one run.** The 08-30 and 08-31 runs each scored zero
because this desk fires **pre-open** (`M1127`); seven rows sat "due today" and none could be read.
Today all seven are readable, plus four more that were blocked on `[FRED]`.
**Composition: 11 scored (3 directional, 8 `C`) · 0 `EXPIRED` · 1 unscoreable (`S8`) · 0 silent skips.**
(`D430` complied with: the composition is stated, not just the count.)

### 2a. Rows that fired a DIRECTIONAL branch

**★★★ `S124` — `FIRED-A`. The desk's own IT underweight is measured wrong.**
- Frozen observable: COUNT of `us_top300` Information Technology names (n=56) with a **positive
  5-session excess vs `SPY`**, settled closes, at the **2026-08-31** close.
- **Measured: 41 of 56 positive** (window 08-24 → 08-31; `SPY` +0.469%; **0 names missing**).
  A ≥ 30 ⇒ **A fires**, and 41 sits **above the trailing-252 p85 (39)**, not merely above the median.
- State at registration was **13 of 56 = the 5.6th percentile of two years.** ⇒ the breadth repair is
  the largest single move in this row's own two-year distribution.
- ⚠ **`D93` was executed before freezing and A was the disclosed favourite (~50%)** — so this is a
  favourite landing, not a surprise. **What it costs the desk is not reduced by that**: branch A is
  written as *"the UW is wrong"*, and `IT` has been carried at `N` (not UW) since 08-31, so the row
  scores against a verdict the desk had already partly walked back. **Recorded as a partial hit
  against a partly-withdrawn call, not as a clean one.**
- ⚠ Anti-signal checked: no GICS reclassification of ≥3 names and no market-wide halt inside
  08-25 → 08-31. **MSCI's 08-31 review was pre-declared NOT a voider.** Row is valid.
- ✅ **Not `EXPIRED`, not re-banded** (`D242`).

**★★★ `S112` — `FIRED-B`. The correlated-underweight tilt was right through Jackson Hole.**
- Frozen observable: `EW{XLU, XLRE, XLP}` **3-session excess vs `SPY`**, settled closes,
  **08-26 close → 08-31 close**.
- **Measured: `XLU` −2.942% · `XLRE` −2.173% · `XLP` −1.495% ⇒ EW −2.204%; `SPY` +0.127%
  ⇒ excess −2.331pp.** B ≤ −1.757pp (252-obs p15) ⇒ **B fires**, and it clears the threshold by
  0.57pp.
- State at registration was **−0.225 = the 49th percentile, dead centre** — the most balanced starting
  state the desk had registered in weeks, which makes this the more informative of today's two
  directional hits.
- ⇒ **`UTIL UW` · `RE UW` · `STPL N` survive their own registered test.** ⚠ The row's own honesty
  clause stands: July PCE fell inside the window and is **not** separated out.

**★★ `P86` — `FIRED-B`, and its own KPI points the other way.**
- Frozen: **A** = core PCE MoM ≤ +0.20% **AND** `DGS2` ≤ 4.10 at the first close covering 08-28.
  **B** = core PCE MoM ≥ +0.35% **OR** `DGS2` ≥ 4.32.
- **Measured: `DGS2` 08-28 = 4.34 ≥ 4.32 ⇒ B fires on the OR-leg.** (The PCE leg went A's way —
  +0.2% MoM, `M977` — but A is a conjunction and its rate leg failed at 4.34.)
- ★ **`M1166` [measured] — B fired while B's registered KPI disagrees.** The row's KPI says *"branch B
  should carry `breakeven_10y` above 2.42."* It reads **2.31**, and it did not move (2.33 → 2.31 across
  the same window). The 08-28 session was a **+14bp move in `DGS2`, +6bp in `DGS10`, +8bp in `DFII10`,
  with breakevens FLAT** ⇒ **the wedge closed upward on the REAL-rate/policy-path leg, not on
  inflation compensation.** The branch label ("YoY wins") is therefore **half-earned**: the level test
  fired, the mechanism it named did not. **Recorded as fired-with-a-dissenting-KPI, not laundered.**

### 2b. Rows that fired `C` — each with the number, not a shrug

| id | observable | measured | branches | verdict |
|---|---|---|---|---|
| **`S92`** | Mandatory Hormuz bracket, 3 branches | see below | — | ★ **`FIRED-A`** — see 2c |
| **`S94`** | `EW{COHR, LITE}` 5-session excess vs `SPY` at 08-31 **AND** `vol_surge ≥ 1.0` on both **AND** registry still carries no optical entry | excess **+5.05pp** (COHR +0.85% · LITE +10.19% ⇒ EW +5.52%; SPY +0.47%) — **A's price leg clears +3pp by 2pp** — but `vol_surge` **COHR 0.83 · LITE 0.76**, i.e. **below 1.0 on BOTH** | A > +3pp ∧ vol_surge ≥1.0 both / B < −3pp | **`FIRED-C`** ⚠ **and this is the informative kind of C**: the conjunct that failed is exactly the one written in to guard against print-reaction volume decay, and it failed in the direction that says the move is **not** volume-confirmed. **A is NOT awarded on the price leg alone** (`D242`) |
| **`S103`** | `NVDA` 5-session excess vs `SPY`, 08-25 close → first settled close on/after 08-29 ⇒ **08-31** | `NVDA` 213.05 → 220.78 = **+3.628%**; `SPY` +0.149% ⇒ **excess +3.479pp** | A ≥ +5.0 / B ≤ −5.0 | **`FIRED-C`**. ⚠ Carried caveat honoured: the 08-23 run pre-declared these hand-set ±5.0pp bands **NO-INFORMATION** because they sit inside the implied move (`NVDA` ±6.11%). **A C from a no-information band is not evidence.** Pre-settle read on 08-29 was +1.663pp; final +3.479pp — the pre-settle understated it, the 4th straight time a pre-settle read has been wrong in direction or size |
| **`S104`** | `T10YIE` change in bp, 08-27 `[FRED]` close → first `[FRED]` close covering 08-31 | 2.33 → **2.31 = −2.0 bp** | A ≥ +3.0 / B ≤ −3.0 | **`FIRED-C`** — **1.0bp short of B**. ⚠ Stated, not rounded into B. Direction agrees with the desk's real-yield frame; magnitude does not reach the pre-registered bar |
| **`S111`** | `ig_oas` level at the first close covering 08-28 | **0.79** (08-27 0.79 → 08-28 0.79, unmoved) | A ≥ 0.85 / B ≤ 0.77 | **`FIRED-C`** — the disclosed ~78% favourite. ⇒ **`P67`'s instrument question is unresolved**: IG did not widen to confirm, and did not tighten to exonerate |
| **`S120`** | `DGS30` **and** `T10YIE` at the first observation where BOTH carry 08-28 | **`DGS30` 5.22 · `T10YIE` 2.31** — ✅ the joint date finally arrived (both carry 08-28) | A: `DGS30` ≥5.31 ∧ `T10YIE` ≤2.38 / B: `DGS30` ≤5.10 ∧ `T10YIE` 2.28–2.40 | **`FIRED-C`** — 5.22 is inside the realised 8-obs range 5.17–5.27. ★ **The observation-lag clause written INTO the row did its job**: the row waited three runs and settled cleanly instead of being improvised, which is what `S102` could not do |
| **`S131`** | `RSP` − `SPY` 1-session excess, 08-28 → 08-31 (the mandatory ≤48h MSCI bracket) | `RSP` 220.69 → 219.39 = **−0.589%**; `SPY` 769.35 → 767.05 = **−0.299%** ⇒ **excess −0.290pp** | A ≥ +1.30 / B ≤ −1.30 | **`FIRED-C`** ⚠ **`RSP`'s 08-28 close is in the hole** — 220.69 is the value frozen at registration; the 5m proxy independently gives **220.66** (0.014% apart), so the verdict is the same on either. Labelled |
| **`P97`** | broad dollar **and** `DGS10` at the first observation where BOTH carry the same date ≥ 08-28 | joint date **08-28**: dollar **118.7479** · `DGS10` **4.73** | A: ≤117.44 ∧ ≥4.75 / B: ≥118.60 ∧ ≤4.65 | **`FIRED-C`** ★ **and it is readable for the first time.** The dollar leg **alone** clears B (118.75 ≥ 118.60) but `DGS10` 4.73 misses B's ≤4.65 by 8bp ⇒ **the conjunction saves the row from a false B.** ⚠ Recorded because the single-leg reading is the trap: a run reading only the dollar would have scored B |

### 2c. `S92` — the Hormuz bracket, scored branch by branch
- **Branch B** (`CL=F` settled close **< 78.00** on any session through 08-31 with no dated US action):
  **does not fire.** `CL=F` closes 08-13 → 08-31: 81.25 · 82.40 · 84.50 · 84.94 · 85.83 · 87.83 ·
  87.06 · 85.01 · 82.36 · 82.23 · 83.53 · 83.40 · **85.76**. **Minimum 82.23 — never within 4.2 of B.**
- **Branch C, the row's own designated falsifier** (a **US-brokered halt to Ukrainian strikes on
  Russian energy infrastructure**): **does not fire.** The strikes continued through the window —
  Yaroslavl [bloomberg, 08-28], Volga region [bloomberg, 08-26], Samara [bloomberg, 08-22],
  Krasnodar [aljazeera, 08-25], plus [oilprice, 08-28] *"Ukraine Drones Spark Fire at Russian Refinery
  as Fuel Crisis Worsens."* ⇒ **`P66`'s Russia supply-destruction leg SURVIVES**, as the row
  pre-registered it would under any non-C outcome.
- **Branch A** (a **dated US action on the Strait** — declaration / escort regime / interdiction —
  reported by **≥2 independent foreign outlets** by 08-31, **AND** `CL=F` settled close **> 82.40`):
  **fires on both legs.**
  - Price leg: `CL=F` 08-31 **85.76 > 82.40** ✅.
  - Action leg, **two independent categories, each ≥2 outlets** (all `--scope foreign`):
    **(i) declaration** — *"Trump says Strait of Hormuz is 'an American territory'"* [upi, 08-22];
    *"Trump Labels Map Of Strait Of Hormuz 'New U.S. Territory' After Passing 60-Day Deadline"*
    [forbes, 08-18]. **(ii) interdiction / clearance operation** — *"US President Trump: US Navy has
    cleared Strait of Hormuz mines"* [fxstreet, 08-25]; *"Trump: Mines fully removed from Strait of
    Hormuz"* [axios, 08-25]; corroborated adversarially by *"US Allies Cast Doubt on Trump's Claim
    Hormuz Has Been Demined"* [bloomberg, 08-26] and *"Hormuz transits fall to 16 ships as US Navy
    fires on Iran-bound container ship"* [hellenicshipping, 08-13].
- ⇒ **`S92` = `FIRED-A`.** ★ **And the row's own B4 grading is carried with the verdict: A is
  CONFIRM-ONLY.** It confirms the war-premium leg and says nothing the desk did not already hold.
  **The falsifier (C) is the branch that would have carried information, and it did not fire.**
  ⚠ **`M1167` [measured] — the state moved AGAINST A's own premise inside the window's last session**:
  *"Iran Says Supertanker Hit by Mines in Strait of Hormuz"* [oilprice, 08-31] and *"IRGC says ship
  struck 2 sea mines after U.S. declared Hormuz cleared"* [upi, 08-31] — i.e. the demining
  **declaration** that helps satisfy A was **publicly falsified on the settle date itself**, while
  `CL=F` rose 83.40 → **85.76 → 88.13 (09-01, unsettled)**. **The row is scored A as written
  (`D242`); the contradiction is recorded beside it, not used to re-band.** ⇒ **`D445`.**

### 2d. Rows still ARMED, disclosed not scored
| id | requirement | today's read | status |
|---|---|---|---|
| **`P67`** | `hy_oas` ≥ 2.85% | 08-28 = **2.60**, and it has **tightened seven observations running** (2.73 → 2.60) ⇒ **25bp further from its trigger than at registration** | **ARMED**, disclosed. ⚠ With `S111` at C, the desk now has **two credit instruments that both refuse to confirm** the AI-capex-to-debt claim |
| **`P111`** | the regime call's registered test | settles **09-14** | ARMED |
| **`S126`** `P114` | `XLI` exc5 vs `SPY` into / out of the 09-04 NFP | not due | ARMED |
| **`S132`** | `AVGO` 1-session excess, settles **09-03** | not due. ⚠ **`D420` still open** — issuer calendar says 09-03, `catalyst_calendar` says **09-02** | ARMED |
| **`S133`** (09-14) · **`S134`** (09-04) · **`S135`** (09-11) · **`S136`** (09-09) · **`S137`** (09-09) | — | not due | ARMED |
| **`S3`** (~09/10) · **`S4`** (~09 late) · `S109` · `S127`–`S130` · `P81` `P85` `P87`–`P89` `P115`–`P117` | — | not due | ARMED |

### 2e. Named again rather than dropped
- **`S8`** — ⛔ **unscoreable for a 34th consecutive run**; date field still `[blank]`. A human must
  `VOID` it or re-register it with a date (P5). **Named, not dropped.**
- **KR-owned rows** — earliest `S67-KR` is **09-04**; zero due.

---

## 3 · Both ledgers audited — symmetric, per `carryover.md` §3c

| ledger | rows | resolved | **legacy (no revival/entry condition)** | **due today** |
|---|---:|---:|---:|---:|
| `reject_ledger.py due` | **273** | 155 | **0** | **0** |
| `missed_ledger.py due` | **285** | 164 | **0** | **0** |

**`M1168` [measured] — legacy 0 on both sides for a 13th consecutive run**, and both ledgers **grew**
(259 → 273 rejections, 277 → 285 misses) while legacy stayed at zero — i.e. the new rows are being
filed **with** conditions, which is the property that matters, not the zero itself.
⚠ Signs are **inverted** between the two ledgers and are **not summed**.
⚠ `missed_ledger score`'s first 6 rows remain a seeded, outcome-selected block — quoted as
*accumulation*, never as an edge.

---

## 4 · Exposure state carried as size context — `C23` reproduced a third time

**Not cold-starting**: `exposure_rule.py show` returns **45 rows**, most recent **2026-09-01**.

| | value |
|---|---|
| rule state | **정상 (normal)** — no firing condition; bench `069500.KS` 107,885, +0.251% |
| target invested | **95%** |
| **actual invested (09-01 row)** | **85.2%** ⇒ **band gap −9.8pp**, the **13th consecutive session outside the band** |
| cumulative decomposition (n=17) | **total excess −12.51pp = cash −5.88pp + selection −6.63pp** |
| alarm | 🚨🚨 `ARMED (TIMEFOLIO_EXECUTE=1)` |

⚠ `exposure_rule.py state` again printed **"투자비중 미상"** (no account query) while `show` carries the
number — the verdict line and the ledger line disagree about whether the weight is known. Reported as
read; **not substituted** (P5). Second consecutive run.

### ★ `C23` / `D415` — the two books, with today's numbers

**`M1169` [measured].** The three instruments this stage ran name **three different books**:

| instrument | book it read | invested | names |
|---|---|---|---|
| `module_paper_book status` | **paper** | total ₩17,684,377 | **13** (11 US + `028050`, `316140`) |
| `cycle_exposure.py` | **real KIS** | **$5,171 of ≈$11,012 total** | **5 US** tagged (`NVDA`·`ANET`·`MPC`·`PSX`, +`RTX`) |
| `exposure_rule.py show` | **KR contest / timefolio** | **85.2%** | — |

⇒ **the real US account is 53.0% cash** ($5,841 of $11,012 un-invested) at the same moment the exposure
instrument reports **85.2% invested against a 95% target**. Both numbers are true; **neither output
says which book it is about.** ⚠ Which book is authoritative for research is a **human call (P5)**.
★ **For BET/ALPHA**: any sizing sentence this run writes must **name its book on the same line.**

**`M1170` [measured] — no top-rank cycle GAP on the real book, third consecutive run.**
AI-compute epicenter **16.85%** (need ≥12.0, margin +4.85pp) · Energy/refining **10.28%** (need ≥8.0,
margin +2.28pp) · Missile-defense **3.77%** (no threshold set). ⚠ Per `D416`/`D250` the registry still
carries **no AI-power/grid ranked row** and **no optical row** ⇒ "0% exposure" is **unstatable** for
those, not measured as zero. ★ **`S137` (settles 09-09) now brackets the optical question directly
without waiting for the registry** — `D250`'s 17th run, but the first with an instrument.

---

## 5 · Signal scoreboard — `vol_surge` holds its kill-threshold clearance, and `W1` still bars acting

`axis_inflection.py` ran (16 axis files); `ic_ledger.py log` accrued **20 new rows** (**총 1034행 ·
market=kr** — still KR-only, `D395`/`D428` unchanged); `ic_ledger.py score` read (21 tests).

| axis | h | n | n_eff | mean IC | t(NW) | positive | verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| **`vol_surge`** | **1** | **41** | **41.0** | **−0.0417** | **−3.51** | 27% | ★ **significant, passes Bonferroni (\|t\| > 2.8)** — 2nd consecutive run |
| `vol_surge` | 5 | 37 | 7.4 | −0.0390 | −2.41 | 32% | standalone only |
| `obv_norm` | 5 | 37 | 7.4 | −0.0590 | −2.27 | 27% | standalone only |
| `flow_score` | 1 | 41 | 41.0 | −0.0389 | −1.44 | 44% | indistinguishable |
| `rs20` | 1 | 40 | 40.0 | −0.0422 | −1.27 | 42% | indistinguishable |

**`M1171` [measured] — the result strengthened, not decayed**: `t(NW)` **−3.32 → −3.51** with `n_eff`
40 → 41, sign still **negative**, agreeing with **M224**, **while `sector_flow` continues to weight
`vol_surge` positively in its 🟢 tag rule.**
🚫 **And this run may still not act on it.** The ledger is **`market=kr`**; flipping a **US** gate on a
**KR** measurement is the `W1` violation this repo keeps logging (the same reasoning that held the US
DEEP budget at N=4 when `industry_kr` cut to N=2). **`D428` stands unmet**: the US desk has no
`ic_ledger` of its own, so the pre-commitment is unreachable in the market that owns the decision.
★ **It is now materially binding, not academic** — `S94` fired `C` today **precisely on a `vol_surge`
conjunct**, and the desk's own scoreboard says that axis's sign is negative.
⚠ **9 of 21 cells remain unquotable** (`n_eff < 4`); `필요n` is not quoted for any cell with `n < 10`.
⚠ Regime label: a hawkish real-rate repricing stretch (08-28 `DGS2` +14bp), not a crash window.

---

## 6 · Stale-check

| carry | age at this run | action |
|---|---|---|
| Sector verdicts (08-31) | **1 run**, and **one new settled US session** since | fresh enough to inherit; ROTATION re-derives on the repaired sweep — and it must, because **rank 1 changed** (§1d `C24`) |
| Regime call `[inferred]` | tested by `P111` (09-14) | carried, not cited |
| `us_top300.csv` | **48 days** (mtime 2026-07-15) | 🚫 cap-weight may not be called "current size" (G5). `us_all_v2_candidate.csv` (08-10) sits beside it, **human-approval item, not switched** |
| **`DTWEXBGS`** | ✅ **now 08-28 — caught up from 08-21** | **`D333` CLOSED for this run after 13 reproductions**; `P97` became readable and scored. ⚠ Closed *as a lag observation*, not as a fix — the series can fall behind again |
| **H.15 dailies** | ✅ **now 08-28 — caught up from 08-27** | **`S120` unblocked and scored.** ⚠ `T10YIE` again runs **one date ahead** (08-31) of its own constituents (08-28) — `D427`'s split is **reproduced, not repaired** |
| `NFCI` | 08-21 (11 days) | weekly series; not blocking |
| `cycle_registry.json` | no ranked AI-power row (`D416`), no optical row (`D250`, **17th run**) | "0% exposure" unstatable for both; `S137` now brackets optical directly |
| **Suspensions whose clearing date has passed** | **none found** | — |
| Contaminated stretch: **the 2026-08-28 daily bar** | registered 08-29 | ⚠ **not retro-cleaned.** Prior runs' figures keep their notes. **Today's addition: 42 of 301 names were backfilled, and that partial repair does NOT clean the window** — it makes it *inhomogeneous*, which is worse for cross-sectional work than uniform absence (`M1162`) |

---

## 7 · Dig list ranked for today

**New this run:**

| id | dig (positive form) | measured origin |
|---|---|---|
| **`D445`** | ★★ *When a scenario's branch fires while a dated public fact inside the same window contradicts the branch's own premise, the run scores the branch as written AND records the contradiction on the same line.* | `M1167`: `S92`-A is satisfied partly by the US demining **declaration** of 08-25, and *"IRGC says ship struck 2 sea mines after U.S. declared Hormuz cleared"* [upi, 08-31] falsifies that declaration **on the settle date** |
| **`D446`** | ★★★ *An axis computed over a rolling window states how many bars in that window are actually present, per name.* | `M1162`: the OBV axis silently zeroed **the two most recent sessions** for 259 of 301 names and every one still printed a number, with a **29% label-flip rate** |
| **`D447`** | ★★ *A recovery proxy is validated on EVERY input it feeds, not only on the one that is easiest to check.* | `M1164`: the 5m proxy's **close** leg was validated on 08-31 and its **volume** leg was not — and the volume leg is biased **−18.15%**, feeding an OBV axis |
| **`D448`** | ★ *A partial vendor backfill is logged as an INHOMOGENEITY, not as an improvement.* | 42 of 301 names now carry an official 08-28 bar and 259 do not ⇒ cross-sectional axes mix two data generations. Uniform absence is more citable than partial presence |
| **`D449`** | ★★ *A proposition whose branch text lives only in a run report is re-stated in `SCENARIOS*.md` when it is carried, so scoring does not depend on locating a five-run-old MACRO file.* | Scoring `P86` and `P97` required opening `llm_outputs/2026-08-22/` and `2026-08-25/MACRO_REPORT.md`; the spine carried **only the thresholds**, not the branch semantics. A threshold without its meaning can be scored but not interpreted |
| **`D450`** | ★ *A row whose branch is a CONJUNCTION records, at scoring, which legs passed — a conjunctive C is not the same object as a both-legs-missed C.* | `P97`: the dollar leg **cleared B alone** (118.75 ≥ 118.60) and only `DGS10` (4.73 vs ≤4.65) held it at C. `S94`: the price leg cleared A by 2pp and the `vol_surge` conjunct failed on both names |
| **`D451`** | ★ *A "no-information band" declared at registration is re-stated at scoring, so a later reader cannot mistake the C for evidence.* | `S103` scored C from bands the 08-23 run had already declared inside the implied move; without the restatement, "+3.479pp, C" reads like a measurement |
| **`R120`** | **retraction** — *"the 5m-proxy close error is ≤0.0448% with 0 names over 0.05%"* (2026-08-31 PREFLIGHT, n=24, validated against the **prior** session) | **Re-measured today against 42 OFFICIAL 08-28 closes: mean 0.0203%, max 0.0937%, 4 names over 0.05%.** ⇒ the proxy is still good and its **conclusions stand** (`M1163`, 7/7 within 0.04pp); **the stated bound was tighter than the instrument earns.** Retracted by the run that inherited it |

**Carried, unmet, with run counts:** `D250` optical registry row — **17th run** (but now bracketed by
`S137`) · `D333` `DTWEXBGS` lag — ✅ **closed this run after 13 reproductions** · `D379` PREFLIGHT
reads §5 first — **6th run unwired** · `D394` standing-view writeback — both halves to verify at run
end · `D395`/`D428` US `ic_ledger` — **now materially binding** (§5) · `D411`/`D412` news-axis
instrumentation — **unaddressed; today's 10/10 direct probe is a 4th reproduction** · `D415` two
books — **reproduced with fresh numbers (§4), still human-owned** · `D416` AI-power ranked row ·
`D420` `AVGO` 09-02 vs 09-03 — **still open, and `S132` is armed on the disputed date** · `D421`
`action_bracket` window · `D422` `drift_watch` anchor · `D424` — **checked, and it now has TWO US
cases (§1b)** · `D426` pre-open settle rule — ✅ **its prescription worked**: the seven rows it
identified all scored today · `D427` FRED split-publication — **reproduced** (`T10YIE` 08-31 vs
constituents 08-28) · `D429` two-run ghost → standing hole — ✅ **the call was right; the hole froze
at 08-28** · `D430` composition of a zero — ✅ complied (§2a) · `S8` — **34th run unscoreable**.

**Ranked as candidate DEEP mandates for this run** (ROTATION owns the final picks):
1. ★★★ **Information Technology** — `S124` just fired **A** at **41/56** from a registration state of
   **13/56**. The desk's IT call is the one a settled bracket has moved against, and `IT` is currently
   `N`. **This is the highest-information mandate on the board today.**
2. ★★ **Energy** — it took **rank 1** on the repaired sweep (`+0.302`, `eqflow +0.299`, the **only**
   sector with breadth > 0) with `ex-XOM` **+0.471**, i.e. the strength is *broader* than the headline.
   `S92` fired A (confirm-only) and `S136` (chain-position vs barrel) settles 09-09. Continuous-track
   carry from 08-31.
3. ★★ **Materials** — `C24` inverts: it fell from rank 1 to rank 2 (`+0.148`) with **0 greens / 2 reds
   of 12** and `ex-LIN` **+0.115** (below the headline). The contradiction, not the ranking, is the
   mandate.
4. ★ **Health Care** — the `D424` shape has **narrowed** (+0.069 vs ex-LLY +0.115, from +0.021 vs
   +0.095). Continuous-track carry; `S133` settles 09-14.
5. ⚠ **Communication Services** — `wflow −0.547` against `eqflow **+0.054**` is the widest cap-vs-equal
   split on the board. `D297` says the bucket is un-measurable by rule (n=12, GOOGL 38.3%), so this is
   flagged as a **measurement mandate**, not a verdict mandate.

---

## 8 · ≤48h binary catalysts injected at run start (protocol requirement)

`catalyst_calendar.py --days 5` → **3 binaries in window**:

| when | event | bracket status |
|---|---|---|
| **D-1 · 2026-09-02** | **`AVGO` earnings** | ✅ **owned twice** — `S132` (±9.00pp, settles 09-03) and `S127` (09-08). ⚠ **`D420` unresolved**: issuer calendar **09-03**, `catalyst_calendar` **09-02** |
| **D-3 · 2026-09-04** | **August NFP** | ✅ spanned twice — `S126` (five sessions **into**) and `P114` (five sessions **out of**). `S134` also settles that date |
| undated | Iran "Strait of Hormuz open" (TACO trigger) | ⚠ **`S92` has just SCORED and is no longer armed.** Remaining coverage: `P107`·`P112`·`P117`. ★ **And the state moved inside the last session** (`M1167`) — a mined supertanker on 08-31, `CL=F` **85.76 → 88.13** into an unsettled 09-01 |
| — | **MSCI 08-31** | ✅ **scored today** (`S131`, C) — out of the window |

⇒ **PREMORTEM (Stage 7) inherits a specific obligation.** `AVGO` at **D-1** is the nearest binary and
it **is** bracketed — so the mandatory ≤48h requirement is satisfied by an armed row and issuing a
second would re-freeze a live threshold (`D242`). ★ **But the Hormuz axis has just lost its bracket to
a score**, and `M1167` says the underlying state moved against the branch that fired **on the settle
date**. **If ROTATION carries `ENRG OW` forward, PREMORTEM must re-bracket the oil axis** — a one-way
tilt into an undated binary with no live row would be exactly the violation this protocol names.

---

## ✅ EXIT CHECK
- [x] Shared spines read (`STANDING_VIEW.md`, `SCENARIOS.md`) plus this desk's `STANDING_VIEW_US.md`,
      `SCENARIOS_US.md`, `RESEARCH.md`. **`SCENARIOS_KR.md` checked** for past-dated rows (earliest
      `S67-KR` = 09-04, none due). Mechanical ledger cross-queried (`module_report_tags show`).
- [x] **Retracted ledger read before forming today's view** (§1c) — through `R119`. **Two entries bound
      real decisions this run**: `R115` kept the recovery off `fast_info.previousClose`, and `R116`
      kept the `S92` reading on `CL=F` rather than `BZ=F`.
- [x] **Every past-dated scenario scored or explicitly named.** **11 scored** (`S92` A · `S112` B ·
      `P86` B · `S94` C · `S103` C · `S104` C · `S111` C · `S120` C · `S124` A · `S131` C · `P97` C) ·
      **0 `EXPIRED`** · 1 unscoreable (`S8`, 34th) · **0 silent skips.** No threshold moved (`D242`).
- [x] `reject_ledger.py due` run — **0 due, 0 legacy** (273 rows). `missed_ledger.py due` run — **0 due,
      0 legacy** (285 rows). Signs not summed. Legacy count reported: **0 for a 13th run**, on ledgers
      that both grew.
- [x] Exposure state read and carried (§4), **not cold start** (45 rows), band gap **−9.8pp**, and the
      book contradiction it exposes is named rather than averaged.
- [x] **Instrument health inherited before any number was trusted** (§0) — every revoked citation is
      written here as a binding constraint, and the three **restored** ones (08-31 tape, `status`,
      `module_chart`) are named as restored rather than silently reused.
- [x] **Claims asserted and then refuted are written down, not edited away** (§4c, `D48`): `R120`
      retracts a bound this desk published **yesterday**, and `M1166` records that `P86`'s branch fired
      while `P86`'s own KPI dissents. Neither earlier sentence was rewritten.
- [x] Stale rows flagged with their `asof`; **two suspensions cleared** (`DTWEXBGS`, H.15) and both were
      converted into scored rows rather than silent trust.
- [x] `[measured]` / `[inferred]` tags preserved. The regime call stays `[inferred]` and is not cited.
- [x] **RESEARCH triggers loaded as binding constraints**, grouped: **C1** (name the benchmark — `SPY`
      inline on every excess), **C4/C5** (`S104` −2.0bp is *not* rounded into B; G4's threshold
      sensitivity), **D5** (cross-provider — the 5m/daily cross-check IS the D5 instance today),
      **D6** (OBV is C-grade — and `M1162` shows why), **S1/S5** (`n_eff`, 249 < 250 short sample),
      **W1** (the `vol_surge` result is **not** transferred to US), **L3** (branch information content —
      `S92`-A is graded confirm-only, `S103`'s C graded no-information).
- [x] No position sizing, no buy/sell language anywhere in the carry (P4).

---
> Next: `python pipeline/run_protocol.py industry_us --next` → **MACRO** (Stage 3).
> ⚠ MACRO inherits: `[FRED]` H.15 **caught up to 08-28** and the 08-28 session is a **+14bp `DGS2` /
> +8bp `DFII10` real-rate repricing with breakevens FLAT at 2.31**; the primary sweep's OBV axis is
> revoked; `SECTOR_FLOW_US_REPAIRED.json` (asof **08-31**) is the citable flow object; the Energy axis
> lost its bracket to a score and PREMORTEM has been told so.
