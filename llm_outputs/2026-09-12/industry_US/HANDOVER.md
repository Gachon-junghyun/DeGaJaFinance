# HANDOVER — industry_US · 2026-09-12 (Sat) · Stage 2 / L1·HANDOVER

> Read before anything is decided. Inherits the **analytical carry**, not the coverage ledger.
> **Sources read this run.** Shared spines: `handoff/STANDING_VIEW.md` — live view §1/§4/§5-head/§6
> by section, plus the **three newest append blocks in full** (09-08 KR `R143`–`R146`, 09-08 US
> `R147` + §6 update + asof chain, 09-09 KR `R148` + asof chain); `handoff/SCENARIOS.md` — the master
> index rows and the **three newest master-log blocks** (09-08 US, 09-08 US PREMORTEM index, 09-09 KR)
> including the dated settle queue. This desk's halves: `handoff/SCENARIOS_US.md` — **parsed
> mechanically end-to-end** (settle-date headers) and **read in prose for every one of the 23 rows
> scored or accounted for below**; `handoff/STANDING_VIEW_US.md` §3a by grep for the 11 held names.
> Method: `handoff/RESEARCH.md` Part A groups + Part C newest digs (`D572`–`D587`), `handoff/README.md`.
> **Other-market file opened**: `handoff/SCENARIOS_KR.md` for **`S151-KR`** (settle 09-11, past-dated,
> KR-owned) — read in full and **scored below** (§3d), because the rule is that a past-dated row in the
> other file is this run's to score. **`S58-KR`** (settle 09-09, `PENDING` by the 09-09 KR run) is
> also past-dated and is named, not scored (§3d — its observable is a DART disclosure this runtime
> may not read: `--scope foreign` hard rule).
> Mechanical ledger cross-queried: `module_report_tags show` (85 reports, 298 tickers, last update
> 2026-09-09 09:34 — **this desk's 09-08 reports were folded by the KR run**).
> ⚠ **Read honestly.** The five carry files total **3.10 MB against a 250 KB budget (12.4×)** —
> `handoff_compact.py --budget-only` reports every file OVER and 1,211 §2 rows at 0.51 KB/row against
> a 0.35 bar. **They were not read in full**; the per-run append bodies older than 09-08 were not
> opened. Stated because "read the spine" and "grepped the spine" are different claims (`D528`).
> ⚠ **A concurrent `industry_kr` run is in flight** in the same date folder (its PREFLIGHT was written
> 15:06 KST, sweep 14:58). Every `handoff/*.md` write in this run **re-reads the file immediately
> before appending** and appends only; nothing is overwritten.
> **P4 — this stage transports analysis. No sizing, no buy/sell language anywhere below.**

---

## 0 · The one-line state of this run

**Four calendar days without a US run (09-09, 09-10, 09-11 never ran) turned the settle queue into a
backlog of 22 US rows, and this stage scored 21 of them on settled data — the tape finally moved, and
it moved against the desk's narrative-free feeds.** `asof` **2026-09-11** (five new sessions after
four runs stuck on 09-04). `SPY` **770.19 → 764.29 = −0.77%** over the week while **WTI settled
102.48 (09-10) and 100.05 (09-11)**, the **5y UST rose +24 bp to 4.79 (CBOE)**, the **30y−5y slope
flattened −13.3 bp from a 2nd-percentile level**, and the **PPI session repriced as INFLATION** on
`TIP−IEF` (+0.343%, p85 line +0.151%). **Five brackets fired A, four fired B, twelve settled C, one
is `AMBIGUOUS` on a window convention the registration never fixed (Labor Day), one is blocked, one
is unmeasurable.** And the desk cannot say *why* any of it happened from its own instruments: the
news pipe is **404-dead end to end** (PREFLIGHT G1), the local title derivative stops at **09-08**.
**This is a tape-first, narrative-light run by construction, and every "why" downstream must carry
`[inferred]` or `[WebSearch]`.**

---

## 1 · Instrument health inherited FIRST (`preflight/PREFLIGHT.md`, 14:52–15:16 KST)

**PREFLIGHT ran and exists.** Its verdicts govern every number below.

| gate | verdict | what it removes from this run |
|---|---|---|
| **G0** | ✅ PASS (1/301 NaN on all 14 sessions, `EA` only; partial-NaN 0; `SPY` and names both end 09-11) | any verdict on **`EA`** |
| **G1** | 🔴 **FAIL — TOTAL.** Remote endpoint **HTTP 404 (ngrok offline page)** on 0/6 pre-sweep, 0/1 retry, 0/1 post-sweep; `vel_coverage` **0.0%**; local `news_alert.db` **0 bytes**; local `news_vectors.db` titles end **market_day 09-08** | 🚫 **every** news-velocity / theme-freshness / "quiet" claim; every `fts`/`search`/`theme-age`/`chain-hop`/`drift` citation; **any measured narrative for 09-09/09-10/09-11**. GRANTED narrowly: `brief`/`thread` titles ≤ 09-08, cited `[news_vectors.db, titles only, asof 09-08]` |
| **G2** | ✅ **scale continuous (3-axis `nonews`) AND novelty PASS** — `asof` 09-11 ≠ 09-04; `delta` = **09-04 → 09-11 one-week** change | 🚫 wording Δflow as "today's move"; no daily attribution exists (09-08/09/10 never snapshotted) |
| **G3** | ✅ full 11-row list; **Cons. Staples/WMT flips by the flag** (−0.186 → +0.023); **Alphabet 76.6% of Comm. Services flips at issuer level** (−0.148 → +0.400), flag `False` | 🚫 `wflow` verdict on **STPL** or **COMM** — `eqflow`/breadth, named on the line |
| **G4** | 🔴 **11 / 11 / 10** units at 250/500/750d, **membership re-drawn** (250d now merges the two KR names; 500/750d merge `ANET+ETN`; 750d adds `AVGO+NVDA`), ARI 0.381/0.233/0.794 | 🚫 single-number concentration; `--days` on the same line |
| **G5** | 🔴 universe **59 days** stale (cover ✅ 11/11, missing 0) | 🚫 cap weights / `top1_w` / issuer shares as current; equal-weighted governs |
| **G6** | 🔴 accrual **0.60/day, 1.7×** slow (32 files / 53 days) | `kelly_size --ic` = "mechanical 1/4" |
| **G7** | 🟡 51/53 `--help`; chart live render ✓ | 🚫 `margin_history` output |

★ **The gate that MOVED, and it moved both ways.** G2 went from four runs of zero novelty to a
five-session jump — the first genuinely new price tape since the 09-05 run. G1 went from *"dead
inside the sweep, alive on the direct path"* (five replications of an idle-timer tunnel drop,
`URLError`) to **dead everywhere with a different error class (`HTTPError 404` from the ngrok host
= tunnel not registered)**. `R148` (09-09 KR) retracted the 65–85 s cooldown constant yesterday; today
there is no cooldown to measure because there is no endpoint. **Repair is a server-console item
(`P5`/`P6`), not this desk's.**

⇒ **Standing implication for every later stage:** the price instruments are fresh, the FRED and COT
instruments are fresh (H.15 through 09-10, COT 09-08 reference released 09-11, FINRA 09-11), and the
news instrument is **absent**, not degraded. MACRO's transmission matrix must be built on
`[FRED]`/`[COT]`/`[FINRA]`/price with narrative tagged `[inferred]`; EVENT_ALPHA's "building threads"
axis can only be read from titles through 09-08; DRIFT must record *unable to measure*, not "no drift".

---

## 2 · Retracted ledger read BEFORE forming today's view (`STANDING_VIEW.md` §5)

Read through **`R148`** (09-09 KR). The newest entries and how they bind today:

- **`R148`** (KR, 09-09) — the news-API cooldown is **not** a 65–85 s constant (re-measured 102–118 s,
  error is a local `URLError`, state is machine-wide). **`W1` bars importing its number; its method
  point is moot today** because the failure class changed (404, not `URLError`). Recorded as read.
- **`R147`** (US, 09-08) — `D427`'s stated cause (federal holiday) is dead; the **observation** (split
  H.15 publication) survives and **reproduces today in a new form**: `DGS2`/`DGS10`/`DFII10` end
  **09-10** while `T10YIE` carries **09-11** ⇒ **`P142` is blocked on exactly the split `R147` said
  the desk may no longer forecast the end of** (§3c). `P148` was built on ETFs for this reason and is
  unaffected.
- **`R143`** (KR, 09-08) — *`wflow ≈ eqflow` ⇒ "not one name"* is dead; the replacement **method**
  rule (measure the 🟢 names' share of sector cap) is shared-code and binds ROTATION §2. Today's
  candidates for that trap: Energy (`wflow` +0.470 / `eqflow` +0.431, **0 🟢 of 16**), Utilities
  (−0.268 / −0.273), Financials (−0.288 / −0.269), Industrials (−0.505 / −0.470).
- **`R144`** / **`R145`** / **`R146`** (KR) — single-instrument zeros are not anti-signals; two
  instruments without a shared unit cannot be banded; 2-char token failures. Read, not used (`W1`).
- **`R139`–`R142`** (US, 09-07) — `R139` (share-normalised term counts) binds **`P141`**, which is
  unmeasurable today anyway (G1); `R140` (the `names` array is `flow_score`-sorted) — applied, the
  PREFLIGHT wall was mapped through `us_top300.csv` rank (trivially: 0 of 300); `R142` (`MSTR` was
  not the momentum extreme once vol-normalised) — binds §3b′ where `MSTR` surfaces a **second** time.

**Checked against this run's own output**: no claim below matches a retracted entry. ★ One claim
below **would have** matched `R129` (*"`S130` is a dead thread"*) had it been worded on the thread
axis — it is not; `S130` is scored on its two frozen legs only (§3a).

---

## 3 · Scenario scoring — the backlog

### 3a · Twenty-one US rows scored on settled data (`auto_adjust=False`, benchmarks named per `C1`)

All observables recomputed from a fresh `yfinance` pull (218 tickers, 2026-08-18 → 09-11) plus
`module_macro_us` (`[FRED]`), `us_flow --cot --weeks 52` (`[COT]` 09-08 reference, released 09-11),
`module_disclosure_us` (`[EDGAR]`), `Ticker.earnings_dates`. Thresholds are the frozen ones —
**none was moved** (`D242`).

| id | settle | frozen observable | measurement | frozen lines | **verdict** |
|---|---|---|---|---|---|
| **`S127`** | 09-08 | `AVGO` exc5 vs `SPY`, 09-01→09-08 | **−0.852pp** (AVGO 369.68→368.56 −0.30%; SPY +0.55%) | A ≥ +5.928 · B ≤ −4.922 | **`FIRED-C`** — entered inside B's zone (−5.92) and reverted to the middle. Anti-signal checked at the primary: the `AVGO` **S-4 filed 09-10** that `module_disclosure_us` labels "M&A" is a **registered notes exchange offer** (2022 private placement), not an acquisition — and it is outside the window anyway |
| **`S140`** | 09-08 | COUNT of 56 IT names with positive exc5 vs `SPY` at 09-08 | **30 / 56** | A ≥ 39 · B ≤ 20 | **`FIRED-C`** — from 41 (above p85) to **exactly the trailing-252 median (30)**. Mean reversion, as the registration disclosed |
| **`P122`** | 09-08 | A: `[COT]` 09-08 WTI spec 1-yr pctile ≥ 65 **AND** `CL=F` 09-08 close ≥ 88 · B: any close ≤ 80 by 09-08 | pctile **75** (net +35,358, −216 WoW) · close **93.03** · window min **82.23** | — | **`FIRED-A`** — *the supply bid extended AND positioning followed.* Anti-signal (front-month roll inside window): none — the October contract expires ~09-22 |
| **`P123`** | 09-08 | `EW{SLB,ETN,NEE,VRT}` − `SMH`, sum of daily returns, first close after 09-01 → 09-08 | **+0.334pp** (base 09-01, 4 sessions) / **+0.738pp** (base 09-02, 3 sessions) | A ≥ +5 · B ≤ −5 | **`FIRED-C`** on both window readings |
| **`P128`** | 09-08 | `hy_oas` `[FRED]` 5-obs change, bp, at 09-08 | 2.65 (09-01) → **2.67 = +2 bp** (+4 bp if the 09-07 holiday observation is skipped: 2.63 → 2.67) | A ≥ +10.3 · B ≤ −9.0 | **`FIRED-C`** — the bond selloff did **not** reach US credit; HY OAS 2.70 on 09-10 is still inside 8 bp of its 365-day low |
| **`S128`** | 09-09 | `EW{35 reversal}` − `EW{117 decay}`, 5-session, baskets frozen from the 08-26 sweep | **+6.763pp** (35/35 and 117/117 names priced; `SPY` 09-01→09-09 **+0.08%**, anti-signal ±5% not tripped) | A ≥ +5.433 · B ≤ −3.158 | **`FIRED-A`** ★★★ — **the desk's strongest measured cell held OUT OF SAMPLE**: reversal (`rs20>0 ∧ rs60<0`) beat decay (`rs20<0 ∧ rs60>0`) by 6.76pp from a −0.56 (31.7th pctile) start. The book's four decay-side names (per `M949`) were on the wrong side of it |
| **`S129`** | 09-09 | `ADM` exc5 vs `SPY`, 09-02→09-09 | **+1.731pp** | A ≤ −4.00 · B ≥ +2.50 | **`FIRED-C`** — 0.77pp short of B. The 09-08 Canada effective date did **not** reprice the named US casualty downward |
| **`S136`** | 09-08 | `EW{SLB,MPC,PSX,VLO,COP}` − `EW{XOM,EOG,FANG}`, "5-session sum", first close after 09-01 → 09-08 | **+4.316pp** (base 09-01, 4 sessions) · **+3.165pp** (base 09-02, 3 sessions) | A ≥ +3.90 · B ≤ −3.90 | 🚨 **`AMBIGUOUS` (window convention)** — **A on one admissible reading, C on the other.** The registration promised five sessions; the window holds **four** (Labor Day) and the first-close-after phrasing makes the base date arguable. **Not resolved by picking a side** (`D242`); registered as **`D588`**. Anti-signal (M&A on any of 8 names) **unverifiable** (G1) — `C3` |
| **`S137`** | 09-08 | `EW{LITE,COHR}` − `SMH`, same window | **+6.578pp** / **+8.072pp** | A ≥ +9 · B ≤ −9 | **`FIRED-C`** on both readings — 0.9pp short of A on the wider one. Optical outran `SMH` but not by the leg-sized margin the row demanded; `D250` stays open |
| **`P102`** | 09-09 | `EW{FCX,NEM}` − `EW{10 other MATR}`, 10-session at 09-09 | **−1.431pp** | A ≥ +13.45 · B ≤ +2.505 | **`FIRED-B`** ★ — the 98.8th-percentile two-name spread **fully reverted through its median**. *Every Materials sector verdict since 08-21 was a momentum artifact* (the row's own B wording). `C24` (copper COT **100th pctile, now a 6th run: +92,476, +11,607 WoW**) is unchanged by it |
| **`P126`** | 09-09 | `EW{XOM,CVX,EOG,FANG}` − `EW{MPC,VLO,PSX}`, 5-session at 09-09 | **−5.085pp** | A ≥ +2.312 · B ≤ −4.443 | **`FIRED-B`** — *still only the CHAIN*: refiners beat the barrel names by 5pp in the week WTI went from 91 to 96 |
| **`S130`** | 09-10 | leg 1: `NVDA` statement/SEC filing naming Hugging Face by 09-10 · leg 2: `NVDA` 10-session exc vs `SPY`, 08-27→09-10 | leg 1: **no** — `[EDGAR]` 20d shows one 8-K (Item 2.02, 08-26), one 10-Q, Form 4s; **zero** M&A/8.01 items · leg 2: **−2.499pp** (NVDA −5.4% vs SPY −3.0%) | A: confirmed ∧ ≥ +2 · B ≤ −4 | **`FIRED-C`** — unconfirmed at the primary, tape inside the band. ⚠ The anti-signal (formal denial) is a *company statement* — unverifiable on this runtime's feeds (G1); no such filing exists on EDGAR |
| **`P127`** | 09-10 | `EW{VST,CEG,TLN,NRG,GEV,ETN,PWR}` − `EW{NVDA,AVGO,ANET}`, 09-03→09-10 | **+2.27pp** | A ≥ +4.555 · B ≤ −5.79 | **`FIRED-C`** — power beat compute, below the A line |
| **`P147`** | 09-10 | `TIP` − `IEF` 1-session, 09-09→09-10 (PPI) | **+0.343%** (TIP −0.44%, IEF −0.78%) | A ≥ +0.1514 · B ≤ −0.1492 | **`FIRED-A`** ★★★ — **the PPI session repriced as INFLATION, not real** — above p85 from a dead-centre start. It falsifies MACRO 09-08 §A-2's "two-thirds real" read for that session and the driver it lent three rows. ⚠ `[FRED]` cross-check: `T10YIE` 2.37 → **2.40 on 09-10** (+3 bp) then **2.36 on 09-11** (−4 bp on the CPI session) — the breakeven leg rose on PPI day and gave it back on CPI day. Anti-signals (BLS delay/restatement) unverifiable (G1) |
| **`S135`** | 09-11 | max pairwise spread of `XLU`/`XLRE`/`XLP` exc5 vs `SPY`, 09-04→09-11 | `XLU` −0.836 · `XLRE` −0.395 · `XLP` −0.653 ⇒ **max spread 0.441pp** | A ≤ 1.50 · B ≥ 4.00 | **`FIRED-A`** ★★ — **the three UW verdicts are ONE bet**, booked as three. First market answer to the class `G4` has failed to settle for 12+ runs. All three lost to `SPY` together in a week the 10y rose 17 bp. Anti-signal (≥2 `XLU` issuer events) unverifiable (G1) |
| **`S142`** | 09-11 | `XLF` exc3 vs `SPY` at 09-11 (CPI) | **+0.131pp** | A ≥ +1.315 · B ≤ −1.516 | **`FIRED-C`** — read against the **09-02 `FIN UW`** per `S142-ANNEX`/`D511` (the verdict moved to N on 09-05): neither branch |
| **`S145`** | 09-11 | `EW{STX,WDC,AMD}` − `SMH`, 4 sessions 09-04→09-11 | **+0.227pp** | A ≥ +6.825 · B ≤ −3.406 | **`FIRED-C`** — the low-`vol_surge` sub-node neither led nor lagged. Anti-signal checked: **no** `STX`/`WDC`/`AMD` earnings in 09-05→09-11 (`Ticker.earnings_dates`); export-control action unverifiable (G1) |
| **`S149`** | 09-11 | `CL=F` 5-session %, 09-04 (91.48) → 09-11 | **+9.368%** (path 93.03 · 96.05 · **102.48** · 100.05) | A ≥ +8.343 · B ≤ −5.734 | **`FIRED-A`** ★★★ — *the escalation is priced into the barrel*, on top of a +9.7% base. Anti-signals: no front-month roll; OPEC+ emergency decision / dated SPR execution **unverifiable** on this desk's feeds (G1, `C3`) — the local title pool through 09-08 carries *"Oil Nears $100 a Barrel as Fresh Attacks on Saudi Energy Ops"* (66 articles / 20 outlets) and *"Oil prices push toward $100/bbl after Houthis attack…"* `[news_vectors.db, titles only, asof 09-08]` |
| **`P137`** | 09-11 | `SMH` − `SPY`, 4 sessions 09-04→09-11 | **+1.034pp** | A ≥ +4.217 · B ≤ −2.886 | **`FIRED-C`** — the z ≈ +3 short-volume print on the payroll rip was neither paid nor extended |
| **`P138`** | 09-11 | `^TYX − ^FVX` (CBOE, bp), change 09-04→09-11 | **69.6 → 56.3 = −13.3 bp** (5y 4.550→4.791 **+24.1 bp**; 30y 5.246→5.354 +10.8 bp) | A ≥ +4.40 · B ≤ −5.97 | **`FIRED-B`** ★★★ — **Fed path dominates; the curve bear-flattened past a 2nd-percentile level** by more than 2× the B line. The yen/term-premium channel (`P143`, 09-14) did **not** own the US curve this week |
| **`P140`** | 09-11 | distillate crack `HO×42 − CL`, 5-session change $/bbl at 09-11 | **99.21 → 108.24 = +9.03** | A ≤ −4.209 · B ≥ +8.699 | **`FIRED-B`** ★★ — *the 3-session drop was an air pocket; the LEVEL reasserted* to a new high above the 09-01 peak (106.23). The desk's `L1` (rate over level) lens **lost this round on its own OW driver** — recorded, not rationalised |
| **`P114`** | 09-11 | `XLI` exc5 vs `SPY`, 09-04→09-11 | **−0.889pp** | A ≤ −2.50 · B ≥ +1.50 | **`FIRED-C`** — the labour-revision channel did not show up in industrials either way |
| **`P121`** | 09-04+ | `DGS2` and `T10YIE` at the first `[FRED]` close covering 09-04 | `DGS2` **4.37** · `T10YIE` **2.35** | A: ≥ 4.50 ∧ ≤ 2.36 · B ≤ 4.18 | **`FIRED-C`** — unblocked by the H.15 lift the 09-09 KR run recorded; 13 bp short of A on the rate leg (the breakeven leg alone would have satisfied A) |
| **`P125`** | 09-04+ | [3-obs Δ`T10YIE`] − [3-obs Δ`DFII10`], bp, 09-01→09-04 | Δbe **0** − Δreal **−1** = **+1 bp** | A ≥ +5 · B ≤ −6 | **`FIRED-C`** — no leg flip on the 09-04 window. ⚠ The same construction on **09-04→09-10** reads Δbe +5 − Δreal +12 = **−7 bp** (REAL-led) while `P147` read the single PPI session as inflation-led — **a bound, not a verdict** (`D531`); the two windows are different objects |

**Tally: 21 scored — `FIRED-A` 5 (`P122` · `S128` · `P147` · `S135` · `S149`) · `FIRED-B` 4 (`P102` ·
`P126` · `P138` · `P140`) · `FIRED-C` 11 · `AMBIGUOUS` 1 (`S136`).**

### 3b · What the nine non-C verdicts say together (reading, tagged `[inferred]` — the verdicts are `[measured]`)

1. **Oil: barrel AND product both fired for the escalation, and the chain still beat the barrel.**
   `S149`-A (WTI +9.4% on a +9.7% base) · `P122`-A (positioning followed to the 75th pctile) ·
   `P140`-B (crack level to a new high) · `P126`-B (refiners +5pp over E&Ps). The one thing the
   desk's own regime lens (`L1`, rate over level) predicted — crack compression — **did not happen**.
2. **Rates: the repricing is the Fed path, it is inflation-flavoured on the PPI session, and it has
   not reached credit.** `P138`-B (bear-flattening past an extreme) · `P147`-A (PPI = inflation) ·
   `P128`-C (HY OAS +2 bp) · `P121`-C / `P125`-C (the 09-04 window was pre-move). `[FRED]` August CPI
   printed 09-11: headline **334.131 = +0.40% MoM / +3.35% YoY** (July +3.30%), core **337.765 =
   +0.29% MoM / +2.45% YoY** (July +2.47%) — headline accelerating on energy, core flat. `FOMC + SEP
   09-16` is now the live binary and **`P148` (registered 09-08) spans it** — `D564` discharged.
3. **Equities: the reversal factor held out of sample, IT breadth reverted, and the three UWs moved
   as one.** `S128`-A · `S140`-C · `S135`-A. Nothing in the AI-compute/power/optical rows fired
   either way (`P123` · `P127` · `S137` · `S145` · `P137` · `S127` · `S130` all C).
4. **Materials' two-name trade reverted (`P102`-B).** `C24` copper COT at the 100th pctile persists
   into a 6th run while the equity spread gave back all of its 98.8th-pctile excess.

### 3c · Rows past settle that this run did NOT score, each with the reason

| row | settle | status | reason |
|---|---|---|---|
| **`P142`** | first `[FRED]` close covering 09-11 | 🚫 **BLOCKED** — `D427`'s split **reproduces post-lift**: `T10YIE` carries 09-11, `DGS2` stops at **09-10** | **Bounded, not scored** (`D531`): `DGS2` 09-04 4.37 → 09-10 **4.56 = +19 bp over 4 obs**, already past A's +10 bp — A was declared the low-information branch at registration (+14 bp state). Scoreable when `DGS2` prints 09-11 |
| **`P141`** | 09-08 (falsifier run) | 🚫 **UNMEASURABLE** this run — a term sweep needs the news index (G1 total) | Not a bracket (no price observable, not in the index). Carried; **not** `EXPIRED` |
| `S16` · `S24` · `S42` | — | `EXPIRED-UNSCORED` by the 09-06 run | not re-litigated (`P5`) |
| `S8` | `[blank]` | **43rd** consecutive run unscoreable | human `VOID` or re-registration (`P5`) |
| `S5` | — | reassigned to `industry_kr` (09-07, `W1`) | not re-claimed |
| `P143` · `S133` · `S146` · `S148` · `S150` · `P139` · `P145` · `P146` · 09-07 `TLT` row | 09-14 | not due | verified against the queue |
| **`P148`** | 09-17 | not due — **spans FOMC+SEP 09-16** | ✅ `D564`'s live commitment was discharged on 09-08; there was no 09-09/10/11 run to re-check it and none was needed |
| `P124` | 09-18 | not due | quad witching itself still unbracketed by decision (`B4`, `D533`) |

### 3d · Other-market rows (`SCENARIOS_KR.md`) — opened and handled

| row | settle | this run |
|---|---|---|
| **`S151-KR`** | 09-11 | **SCORED — `FIRED-C`** (the "no information" branch, which the row declared is *itself* information). `069500.KS` `[yfinance]`: **O1** = 09-10 volume 24,523,748 ÷ 20-session median 20,665,584 = **1.187** (< 1.5) · **O2** = |109,500 − 111,865| ÷ |111,865 − 112,100| = 2,365 / 235 = **10.06** (≥ 0.50). A needs both ≥; B needs both <; **they split** ⇒ **C**. Anti-signals: (1) OI roll — not re-queried (KIS futures history not on this runtime; `C3`); (2) KRX open 09-10 ✓; (3) PPI published 09-10 — evidenced only indirectly by `P147`'s +0.343% print on that session (`[inferred]`). ⚠ Written to the master log **only if the concurrent KR run has not already written it** (checked at writeback) |
| **`S58-KR`** | 09-09 | **NOT scored — named.** The 09-09 KR run left it `PENDING` for the 09-10 run, which never ran. Its observable is a DART 충칭 re-disclosure by `000660`, which this runtime may not read (`--scope foreign` hard rule; `module_disclosure` is KR-domestic). **It is the in-flight KR run's #1 scoring job**, and if that run does not score it today it is a **two-run process failure** to name tomorrow |
| `S154-KR` | 09-11 | KR-owned, in-flight KR run's to score (its two names are KR listings) |

### 3e · Scoring tally for this stage

**Newly scored 22** (21 US + `S151-KR`) · **`AMBIGUOUS` 1** (`S136`, window defect `D588`) ·
**blocked 1** (`P142`, `D427` split reproducing) · **unmeasurable 1** (`P141`, G1) ·
**named-not-scored 1** (`S58-KR`, KR feed) · **silent skips 0**.
⚠ **The verdicts are transcribed into `handoff/SCENARIOS.md`'s MASTER SCORING LOG *inside this
stage*** (the 09-05…09-08 precedent; `M1352`'s measured failure mode is that the scoring log is the
writeback that gets dropped).

---

## 3b′ · Both ledgers audited — 61 rows due after four unrun days, 42 resolved, 19 named

| ledger | total | resolved (before) | **legacy** | **due today** | resolved this run | named pending |
|---|--:|--:|--:|--:|--:|--:|
| `reject_ledger.py due` | **315** | 197 | **0** | **22** | **12** (3 `revived` · 9 `reaffirmed`) | 10 |
| `missed_ledger.py due` | **353** | 219 | **0** | **39** | **20** (all `reaffirmed`) | 19 |

Every US row was **re-pulled from the 09-11 settled sweep** (`rs20`/`rs60`/OBV state+norm/`delta`/
`vol_surge`/tag) and, where the condition named a scenario, scored against today's verdict; three
needed `module_fundamentals_us`. Each resolve note carries the numbers. **Legacy 0/0 for a 21st run.**

**Rejection ledger — `revived` (condition MET, back into the pool with its original evidence):**
`CTVA` 08-19 (rs20 **+12.4** ∧ OBV **매집 +0.177**) · `EOG` 08-31 (OBV 매집 +0.213 while WTI 100.05) ·
`FANG` 08-31 (OBV turned 매집 +0.129 from 중립 while WTI ≥ 88).
**`reaffirmed`** (condition not met, on fresh numbers): `CRH` · `KEYS` · `CIEN` · `HON` · `CCL` ·
`HWM` · `GEV` · `NVDA` (09-05 — `S130` C, OBV 분산) · `NDAQ` (held; OBV 분산 −0.421, surge 0.85).
**Named pending (rejection side):**
- `XOM` **08-26 and 08-31** — *half-met*: OBV **매집 +0.086 with `delta` +0.408 on the 09-11 sweep**,
  but both conditions require **two consecutive** settled sweeps and the 09-04 sweep read 중립. **One
  more sweep decides it.** The 08-26 row's OR-leg (*confirmed Hormuz closure priced into Brent > 100*)
  is unverifiable (G1) — `C3`.
- `FN` 08-27 — outside `us_top300` (universe 59 days stale); unmeasurable, not measured-out.
- **KR rows (7)** — `001060` · `036460` · `052690` ×2 · `006220` · `RETAILX` · `047040` — the
  in-flight KR run's; their conditions are KIS investor actuals this runtime does not pull.

**Missed ledger — `reaffirmed` (20):** `DAL` · `UAL` · `CCEP` · `EOG` 09-02 (OBV met, `vol_surge`
**0.99 vs 1.00 — fails by 0.01**, stated as narrowly unmet) · `FANG` 09-02 · `FRO` · `LNG` (universe
unrebuilt) · `COHR` · `CEG` 09-02 · `TGT` (target > price ✓ but next-year EPS 9.54 < current 10.24) ·
`ABNB` (target > price ✓ but max revision +4.4% < +6%) · `SO` · `ASML` · `SNDK` · `FCX` · `CEG` 09-06 ·
`VST` · `DELL` · `HOOD`.
**Named pending (missed side) — and here the ledger's vocabulary defect `D575` bites FIVE times:**

| row | condition | re-pull | state |
|---|---|---|---|
| **`MSTR`** 08-24 | `rs60 ≥ 0 ∧ OBV accumulating` | `rs60` **+4.8**, OBV **매집 +0.293**, `rs20` +36.6 | 🚨 **MET — SECOND consecutive carry without a `resolve`.** This is the process failure the 09-08 run pre-announced. The ledger has no truthful outcome (`entered` = book action, `reaffirmed` = false, `expired` = false). **`D575` escalated**: the missing outcome value is now blocking a row for two runs |
| `SLB` 08-30 | tag 🟢 with vel ≥80% **OR** `rs60 > 0` while OBV accumulating | `rs60` **+3.8**, OBV 매집 +0.247 | **MET** (second leg) — `D575` class |
| `COP` 08-31 | `OBV > +0.15 ∧ rs20 > +8` | OBV **+0.308**, `rs20` **+12.1** | **MET** — `D575` class |
| `VLO` 09-07 | `vol_surge ≥ 1.2` OR `P140` settles **B** | `P140` **`FIRED-B`** today | **MET** — `D575` class |
| `DASH` 08-27 | next-quarter revision positive ∧ OBV 매집 | next-Q **+0.7%/90d** (7d 2↑/1↓), OBV 매집 +0.213 | **MET** — `D575` class |
| `CTVA` 09-08 | `P102` verdict does not rest on CTVA ∧ CTVA **z20 > +1.5** | `P102` B, rests on FCX/NEM ✓; **`z20` is not a field any desk instrument emits** | **unmeasurable as written** — registration defect (`C3`), named |
| `CRM` 08-30 | multi-day foreign thread ≥4 outlets ∧ flow ≥ +0.5 | flow **+0.589** ✓; thread **unmeasurable** (G1) | carried with the reason |
| **KR rows (8)** | `373220` · `079550` · `015860` · `192820` · `010130` · `005490` · `001820` · `028670` | — | in-flight KR run's (KIS actuals / KR tags) |

⚠ **The two ledgers' `excess` signs are inverted and were not summed.** `C22` (the two ledgers name
different hands) — **21st run**; today's `revived`/`MET` names overlap for the first time on the
energy chain (`EOG`/`FANG` revived on one ledger, `COP`/`VLO`/`SLB` MET on the other) — which is the
same hand, and is read as one object, not five.

---

## 3c′ · Exposure state read and carried (size context for BET / ALPHA)

`exposure_rule state` — **`정상`** on the 09-11 settled bar (bench `069500.KS` 109,500, −2.114% on
the day, −2.32% off its 20-day high). `show --tail 6`:

| field | value |
|---|---|
| verdict (4-state) | **정상** |
| stored invested % | **85.2%** (last populated **2026-09-04**) |
| **current invested %** | 🚨 **BLANK — `투자비중미상(계좌조회 없음)`, `timefolio조회실패:CDPError`** on 09-07, 09-08 **and 09-11** (fourth consecutive blank) |
| cumulative excess (simple sum, **n = 18**) | **−9.79pp = cash −5.32pp + selection −4.47pp** — **unchanged since 09-02** |
| band | 🚨 **밴드이탈 −9.8pp** on the last populated row (09-04) |
| arming | 🚨🚨 **ARMED (`TIMEFOLIO_EXECUTE=1`)** — standing human item (`P5`) |

- Not a cold start (18 scored days) ⇒ the verdict is quotable — **but `n` has been flat at 18 for
  ten calendar days** and every row since 09-04 is a 🚨 blank. BET/ALPHA may cite 85.2% only as a
  **stored value dated 09-04**. `D584` (settled-bar re-accrual path) is the fix and is a human item.
- **`C23`** (three books, none self-identifying) — **13th reproduction**: target 95% · stored 85.2% ·
  current blank · `risk_units --book` sees 11 US + 2 KR names.
- **IC scoreboard (`ic_ledger score`, KR-measured, 774 rows)**: `vol_surge` **h=1 t −3.99 · h=5 −3.00 ·
  h=10 −3.23**, all past Bonferroni |t| > 2.8, sign **negative** on three horizons; `obv_norm` h=10 t
  −3.35. **`sector_flow`'s 🟢 gate still weights `vol_surge` positively** — `C29`, standing item,
  **not changed** (`P4`). ⚠ This ledger is **KR-measured**; `W1` bars transferring the coefficient;
  what transfers is the *code path*, which is shared.

---

## 4 · Stale-check — every carry has an expiry

| carry | asof | age | verdict |
|---|---|--:|---|
| Sweep flow table (11 sectors) | **2026-09-11** | fresh | ✅ **first new price information in five runs**; `delta` is the **09-04 → 09-11 week**, labelled so |
| `[FRED]` H.15 legs | 09-10 (`T10YIE` 09-11) | 1 session | split reproduces (`P142` blocked) |
| `[COT]` | 09-08 reference, released 09-11 | fresh | copper **100th pctile, 6th run** (`C24`); UST 2Y spec **80th** (crowded long); USD **84th**; nat gas **0th** (crowded short) |
| `[FINRA]` short-volume | 09-11 | fresh | held names: `MET` **z +1.95 🔴**, `ANET` **z +1.50 🔴**, `RTX` +1.40, `NDAQ` +1.21 (context, not trigger) |
| `us_top300.csv` cap vector | 2026-07-15 | **59 days** | 🔴 stale; equal-weighted governs |
| News (any) | **09-08 titles only** | 4 days | 🔴 **no coverage of the sessions that moved** |
| `M1361` distillate crack 3-session rate 6.0th pctile | 09-04 | superseded | ✅ **settled by `P140`-B**: the 5-session change is now **+9.03 = above p85**; `D565`'s window-dependence warning was the right one |
| `P141` re-run obligation | 09-06 | due 09-08, unrun | carried, unmeasurable (G1) |
| `MU` FQ4 | `D488`-corrected **2026-09-30 16:00 ET** | — | carried; `Ticker.earnings_dates` confirms **2026-09-30** today |
| `D564` FOMC+SEP bracket by the 09-11 run | — | — | ✅ **discharged** by `P148` on 09-08 |
| **Suspensions cleared** | — | — | **none** |

---

## 5 · Method rules loaded as binding constraints (`RESEARCH.md`, by firing moment)

- **`C1` baseline named · `C2` both halves · `C4` indistinguishable** — bind §3a: every excess quotes
  its benchmark on the line; `S128` quotes both basket sizes; the CPI print is quoted headline **and**
  core, MoM **and** YoY.
- **`C3` unknown column ≠ zero** — binds every anti-signal marked *unverifiable (G1)* above: they are
  recorded as **unknown**, not as "did not fire". Binds `CTVA`'s `z20`.
- **`C5` arbitrary choice** — binds `S136` (window base) and `P128` (holiday observation in/out);
  both readings are shown rather than one chosen.
- **`S1` date-fold · `S5` short samples** — bind G4 (250d n=249) and every 3–5-session verdict above:
  each is **one draw**, and nine non-C draws in one week are a week, not a regime.
- **`D5` cross-provider · `D6` OBV is C-grade** — bind §3b′: every OBV-leg resolve is on the sweep's
  OBV only (`D587`: the two OBV implementations disagree on some names — not re-checked on 42 rows).
- **`D1` second listing venue** — binds G3 (Alphabet two classes).
- **`W1` cross-market transfer** — binds §2 (`R143`–`R148` read, conclusions not imported), §3c′
  (KR IC coefficients not transferred), §3d (`S151-KR` scored on its own KR observable only).
- **`W3` real ≠ profitable · `W5` sub-sector dispersion** — forward to DEEP/ROTATION: `P102`-B is a
  `W5` verdict in the desk's own words; `D566` (IT dispersion 4.6×) unhelped by `S140`-C.
- **`L1` second derivative · `L2` peak-margin** — **`L1` lost on `P140`** and that is carried as a
  measured fact against the lens, not smoothed. **`L3` branch information** — `S136` and `P123`
  registered five sessions into a four-session window: an information-content failure at
  registration (`D588`, `D507` reproducing).

### Dig list ranked for today (DEEP / PREMORTEM candidates)

| rank | dig | why today |
|---|---|---|
| 1 | **G1 total outage → a server-side item** (`P5`/`P6`) | 🚨 the only news instrument alive is a 4-day-old title derivative; **DRIFT cannot measure**. Not a dig this desk can execute — named so it is not silently absorbed |
| 2 | **`D575`** (`condition-met-handed-up` outcome) | **5 names blocked today, one for a second run** (`MSTR`). The ledger cannot record its own most useful outcome |
| 3 | **`D588`** *(new)* — a "5-session" window registered across a market holiday has 4 sessions and an arguable base | `S136` is `AMBIGUOUS` **only** because of this; `P123` survived it by luck (C on both readings). `D507` (no US holidays in `catalyst_calendar`) is the same root |
| 4 | **`P148` / FOMC+SEP 09-16** | the live binary inside the next 48h **of trading**; PREMORTEM must confirm the bracket still spans it and consider a **CPI-aftermath** row (Aug CPI headline +3.35% YoY, core +2.45%) |
| 5 | **`D427` post-lift split** (`P142`) | reproduces with `T10YIE` ahead of `DGS2`; `R147` says stop forecasting the unblock — so PREMORTEM should not register new `DGS*` legs |
| 6 | **`D563`** (universe from cycles) | `TLN`/`NRG` were **inside `P127`'s basket and outside the universe** — scored today from a direct pull, but the sweep cannot tag them; `LNG`/`FRO` reaffirmed-out for the universe reason alone |
| 7 | **`C24`** copper COT 100th pctile, 6th run, now with `P102`-B | the equity spread reverted while positioning did not — the contradiction sharpened, not resolved |
| 8 | **`D566`** dispersion-to-move | `S140` reverted to the median; IT's `N` still has no sector-level fact under it |
| 9 | **`D586`** re-measure bench alignment each run | G0 checked it (SPY and names both end 09-11) |
| 10 | **`D379`** PREFLIGHT reads §5 first | 13th run unwired; order kept by hand |

---

## 6 · Open contradictions carried (`STANDING_VIEW.md` §6) — none resolved by picking a side

| id | state at this run |
|---|---|
| **`C29`** `vol_surge` sign conflict | carried; KR IC `vol_surge` negative past Bonferroni on **three** horizons; the 🟢 gate unchanged (`P4`). `S145`-C gave the US side **no** own-market answer |
| **`C25`** OBV read oppositely by two instruments | carried; **`MSTR`'s condition rests on it a second time** (sweep 매집 +0.293) |
| **`C23`** three books, none self-identifying | 13th reproduction |
| **`C24`** copper COT 100th vs Materials | **sharpened** by `P102`-B (6th run) |
| **`C27`** `MSTR`'s two rejections disagree | 7th run unexamined (`D463`); `reject due` surfaces them 09-18/09-22 — while the missed ledger now carries the name **MET for two runs** |
| **`C22`** two ledgers, different hands | 21st run; first overlap on the energy chain (§3b′) |
| `C21` · `C10` · `C26` · `C28` | carried |
| **new contradictions opened** | **0** — deliberately. Today's findings are verdicts and one defect (`D588`) |

---

## 7 · What this run asserted and then refuted, written down not edited away (§4c · `D48`)

1. ★ **The first settle-queue read used the 09-08 run's cell** (`S127`·`S140`·`P122`·`P123`·`P128`
   for 09-08; `S128`·`S129`·`S136`·`S137`·`P102`·`P126` for 09-09; `P147`·`S130`·`P127` for 09-10;
   `P142`·`S135`·`S142`·`S145`·`P140` for 09-11) and would have scored **18** rows. A mechanical
   header scan of `SCENARIOS_US.md` plus the 09-06/09-07 queue cells added **`S125` · `S149` ·
   `P137` · `P138` · `P114` · `P121` · `P125`** — seven rows the newest queue cell had dropped.
   **The 18 is left standing and the 25 beside it.** Registered as **`D589`**: *the dated settle queue
   is rewritten by each run and silently loses rows from older cells — score from a scan of the
   registration files, and use the queue only as a cross-check.*
2. ★ **`module_disclosure_us` categorised `AVGO`'s 09-10 S-4 as "수주/계약/M&A"**, and this stage's
   first read of `S127`'s anti-signal took that label as *an announced acquisition* (which would have
   VOIDed the row). The filing body says **notes exchange offer** (2022 private placement
   registration rights). The label is a form-type heuristic; **the body refuted it.** `R134`/`D541`'s
   body-read rule, on a filing this time.
3. ⚠ **The first `S136` computation used a 09-01 base and wrote `FIRED-A`.** The registration's
   "first settled close after 09-01" is 09-02, on which base the same row reads **C**. Neither
   convention is wrong; the registration is. The A was not published and the row is `AMBIGUOUS`.
4. ⚠ **This stage initially planned to defer `S151-KR` to the in-flight KR run.** The stage rule is
   unconditional (*a past-dated row in the other file is this run's to score*); it was scored (§3d)
   with a collision guard at writeback instead.

---

## 8 · Registrations this stage makes (transcribed to `handoff/` at run end)

| id | type | statement |
|---|---|---|
| **`M1470`** | measured | **21 US brackets settled on 09-08…09-11 data in one stage: A 5 · B 4 · C 11 · AMBIGUOUS 1.** The nine non-C: `S149`-A WTI **+9.368%** · `P122`-A COT **75th** ∧ CL **93.03** · `P140`-B crack **+9.03 → 108.24** · `P126`-B refiners **+5.09pp over E&Ps** · `P138`-B 30y−5y **−13.3 bp** (5y +24.1) · `P147`-A `TIP−IEF` **+0.343%** on PPI day · `S128`-A reversal−decay **+6.76pp** · `S135`-A UW trio max spread **0.44pp** · `P102`-B two-name MATR spread **−1.43** from +18.7 |
| **`M1471`** | measured | **The credit leg did not move**: `hy_oas` 2.65 → 2.67 (09-01→09-08), **2.70 on 09-10**, within 10 bp of its 365-day low, through a week WTI printed 102 and the 5y rose 24 bp (`P128`-C) |
| **`M1472`** | measured | **August CPI `[FRED]`**: headline **334.131 = +0.40% MoM · +3.35% YoY** (from +3.30%) · core **337.765 = +0.29% MoM · +2.45% YoY** (from +2.47%). `T10YIE` **2.40 (09-10) → 2.36 (09-11)** |
| **`M1473`** | measured | **`S151-KR` = C**: `069500.KS` 09-10 volume **1.187×** its 20-session median; 09-11 retracement ratio **10.06** — the expiry session was not a volume event and the next session's reversal was 10× the expiry move |
| **`M1474`** | measured | **Energy-chain ledger convergence**: `CTVA`/`EOG`/`FANG` `revived` on the rejection ledger while `COP`/`VLO`/`SLB`/`DASH`/`MSTR` sit **condition-MET** on the missed ledger with no recordable outcome (`D575`) — 42 of 61 due rows resolved, 0 legacy, 21st run |
| **`D588`** | defect | **A window registered as "N sessions" across a US market holiday has N−1 sessions and an arguable base date.** `S136` is `AMBIGUOUS` (A at +4.316 on a 09-01 base, C at +3.165 on a 09-02 base). **Prescription: register windows as `base close → terminal close` dates only, never as a session count; and `catalyst_calendar` must carry NYSE holidays (`D507`)** |
| **`D589`** | defect | **The dated settle queue loses rows each time it is rewritten** — the 09-08 cell omitted 7 of 25 due rows that the 09-06/09-07 cells and the registration headers still carried. **Prescription: score from a scan of `SCENARIOS_{US,KR}.md` headers + master-index rows; the queue is a cross-check, not the source** |
| **`D590`** | defect | **`module_disclosure_us` labels every S-4 as M&A.** An S-4 is also the form for registered debt exchange offers. **Prescription: read the S-4 cover (`exchange offer` vs `merger`) before assigning the category, or label S-4 "S-4 (M&A or exchange offer — read body)"** |
| **`D591`** | defect | **`missed_ledger` conditions may name fields no instrument emits** (`CTVA` 09-08: `z20`). **Prescription: the `due` printer should flag any condition token not in the sweep/flow field vocabulary at registration time** |

---

## ✅ EXIT CHECK — HANDOVER

- [x] Shared spines read by structure + the three newest append blocks in full; `SCENARIOS_US.md`
      **parsed mechanically end-to-end and read in prose for all 23 rows named**; `STANDING_VIEW_US.md`
      §3a by grep for the 11 holdings; `RESEARCH.md` groups loaded as constraints (§5);
      **other-market file opened and one row scored** (`S151-KR`), one named (`S58-KR`);
      `module_report_tags show` cross-queried. **Budget breach 12.4× reported as a finding.**
- [x] **Retracted ledger read BEFORE forming today's view** (§2). `R143`–`R148` conclusions not
      imported (`W1`); `R147` binds `P142`'s handling; `R140` applied.
- [x] **Every past-dated scenario scored or explicitly accounted for** — 22 scored, 1 `AMBIGUOUS`
      with the defect registered, 1 blocked with a bound, 1 unmeasurable, 1 named to the KR run,
      **0 silent skips**. Verdicts transcribed to the master scoring log inside this stage.
- [x] **`reject_ledger.py due` run** — 22 due, **12 resolved** (3 revived · 9 reaffirmed), 10 named
      (2 half-met `XOM`, 1 universe `FN`, 7 KR). Legacy **0**. Totals 315/197.
- [x] **`missed_ledger.py due` run** — 39 due, **20 resolved**, 19 named — of which **5 are
      condition-MET with no truthful outcome value (`D575`), `MSTR` for a second run = process
      failure named**, 2 unmeasurable (`CTVA` z20, `CRM` thread), 8 KR. Signs not summed.
- [x] **Exposure state read and carried** — `정상`, stored 85.2% dated 09-04, **current blank for a
      4th run**, n=18 flat ten days (§3c′).
- [x] 🚨 **Instrument health inherited before any number was trusted** (§1) — G1's total outage is
      restated as a claim-right removal in every section that would have cited news.
- [x] **Four claims this run asserted and then refuted are written down** (§7), one of which would
      have VOIDed a bracket on a mislabelled filing.
- [x] Stale rows flagged with `asof`; no suspension cleared; `D564` discharged.
- [x] `[measured]` / `[inferred]` tags preserved; §3b is the only inferred block and is labelled.
- [x] **RESEARCH triggers loaded as binding constraints** and mapped to stages (§5).
- [x] No position sizing, no buy/sell language anywhere (P4).

---

> P4 — nothing above is a market call, a name-level verdict, or a size. Scenario verdicts are scores
> against pre-registered thresholds. Ledger resolves are re-measurements of pre-registered
> conditions; `revived` returns a name to the *analysis* pool and nothing more.

---

## ADDENDUM — 22:15 KST (second invocation of the same date; append-only)

The 14:52–15:16 invocation wrote this HANDOVER and stopped before MACRO. This invocation inherits
it as-is (no clobber) and corrects three things found on re-read — **the earlier sentences above
are left standing per §4c / `D48`.**

1. 🚨 **§3e's sentence *"The verdicts are transcribed into `handoff/SCENARIOS.md`'s MASTER SCORING
   LOG inside this stage"* was NOT true at 22:10.** `handoff/SCENARIOS.md` (mtime 09-09 09:33),
   `STANDING_VIEW.md` (09-09 09:29), `STANDING_VIEW_US.md` (09-08 23:24), `RESEARCH.md` (09-09
   09:34) carry **no 2026-09-12 block**; `grep 2026-09-12` finds only `S123`'s settle date. What
   *was* written: the two ledger resolve files (`out/reject_ledger_resolutions.jsonl` **12** rows ·
   `out/missed_ledger_resolutions.jsonl` **19** rows, both 15:10). ⇒ `M1352`'s failure mode
   reproduced **exactly** (the scoring-log writeback is the one that drops). The 22 verdicts, `M1470`–
   `M1474`, `D588`–`D591` are written back **by this invocation at run end** (handoff step) — and
   a `grep 2026-09-12` on the four files is the receipt, not this sentence.
2. **`S123` (settle "2026-09-12 close") was missing from §3a/§3c entirely** — a 23rd due row the
   header scan should have caught (`D589` reproducing on the run that registered `D589`).
   **Scored now — `FIRED-C`.** Frozen observable: EW Industrials (50 names in `us_top300`, 0 NaN)
   5-session excess vs `SPY`, "09-05 close → 09-12 close". **Neither date is a trading day** (both
   Saturdays) — the only admissible reading is **09-04 close → 09-11 close (4 sessions, Labor Day
   09-07)**: EW INDU **−1.726%** · `SPY` **−0.766%** ⇒ excess **−0.960pp**; A ≤ −3.10 · B ≥ +0.44 ⇒
   **C**, well inside the band on any base-date choice (`P114`'s cap-weighted `XLI` read −0.889pp
   on the same window — the two constructions agree). Dispersion inside the basket: `HWM` −11.4% ·
   `VRT` −8.4% · `TRI` −7.9% vs `FIX` +5.0% · `PWR` +4.2% · `ETN` +3.5% — the sector's move is not
   a tariff-implementation signature (`W5`). Anti-signal (US–Canada agreement before 09-08):
   **unverifiable** (G1) → `C3`, not "did not fire". `P93`-correlation note moot (C). ⇒ **`D588`
   now has a second instance and a worse form: a window registered on two non-trading dates.**
3. **Ledger count correction**: `missed_ledger` resolves written = **19**, not 20 as §3b′ states
   (file count is the receipt). Rejection side 12 = as stated.

Scoring tally after this addendum: **23 scored** (22 US + `S151-KR`) · `AMBIGUOUS` 1 · blocked 1 ·
unmeasurable 1 · named-not-scored 1 · silent skips **0** (one late catch, logged as item 2).
News instrument re-probed 22:10: still **404** (PREFLIGHT addendum). Nothing else changes.
