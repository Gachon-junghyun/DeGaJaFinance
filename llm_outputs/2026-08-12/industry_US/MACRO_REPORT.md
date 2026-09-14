# MACRO_REPORT — industry_US · 2026-08-12 (KST) · Stage 3/11 (L1·MACRO)

> Analytical output only. No buy/sell recommendation anywhere (P4).
> Clock: **2026-08-12 11:40 KST = 2026-08-11 22:40 ET.** US cash market **closed**; last settled equity
> bar **2026-08-11**. **Two fresh sessions (08-10, 08-11) since the last completed run.**
> 🚨 **July CPI prints 2026-08-12 08:30 ET — ~10 hours from this clock. It is the ≤48h binary and
> PREMORTEM must bracket it both ways.**

## ⚠⚠ THE DEFINING ASYMMETRY OF THIS RUN, STATED FIRST

**This run has TWO fresh PRICE bars and ZERO fresh NEWS bars.** That is the exact inverse of the
08-08/08-09/08-10 triple, which had fresh news and one frozen price bar. Stated here so no stage below
mistakes the shape:

- **Price/rates/credit/positioning: genuinely new.** FRED published through **08-10** (`D212` resolved
  after four blocked runs), CFTC COT published for the **08-11** Tuesday close, FINRA Reg SHO for
  **08-11**, and two equity sessions settled.
- **News: an empty denominator, measured not assumed.** `thread --days 7 --scope foreign` returns
  **08-06 816 · 08-07 719 · 08-08 283 · 08-09 285 · 08-10 720 · 08-11 0 · 08-12 0**, and
  `brief --body 2 --scope foreign` returns **0 articles → 0 events → 0 market events** for today.
- ⇒ **Every news-derived proposition in this report is inherited, not refreshed.** No "quiet" claim is
  made **in either direction** — see §D for why the zero is the instrument's and not the market's.

---

## §A · The rate/credit axis — `[FRED]`, this run's own pull

`module_macro_us --json`, pulled 2026-08-12 11:0x KST. ⚠ Monthly series (CPI, M2) lag ~1 month and are
labelled as such — **the July CPI that prints tonight is NOT in this table.**

| Series | `[FRED]` id | Latest | `asof` | Prior run's read (08-10) |
|---|---|---|---|---|
| 2y | `DGS2` | **4.25** | **2026-08-10** | 4.25 @ 08-06 |
| 10y | `DGS10` | **4.72** | **2026-08-10** | 4.69 @ 08-06 |
| **derived 2s10s** | — | **+0.47** | 2026-08-10 | +0.44 @ 08-06 |
| real 10y | `DFII10` | **2.43** | 2026-08-10 | 2.43 @ 08-06 |
| **10y breakeven** | `T10YIE` | **2.27** | **2026-08-11** | 2.25 @ 08-07 |
| HY OAS | `BAMLH0A0HYM2` | **2.70** | 2026-08-10 | 2.71 @ 08-06 |
| IG OAS | `BAMLC0A0CM` | **0.78** | 2026-08-10 | 0.78 @ 08-06 |
| NFCI (weekly) | `NFCI` | −0.529 | 2026-07-31 | unchanged |
| VIX | `VIXCLS` | 15.46 | 2026-08-10 | 14.90 @ 08-07 |
| SOFR · RRP | `SOFR`·`RRPONTSYD` | 3.63 · 1.25 | 08-10 · **08-11** | 3.62 · 1.45 @ 08-07 |
| Broad dollar | `DTWEXBGS` | **119.0649** | **2026-08-07** | 119.7034 @ 07-31 (**6 days stale then**) |
| CPI · core CPI (monthly) | `CPIAUCSL`·`CPILFESL` | 332.568 · 336.065 | **2026-06** — one month old | unchanged |
| Unemployment | `UNRATE` | 4.1 | 2026-07 | unchanged |

### A-1 · ★★★ `D212` is RESOLVED, and it resolved into three scored brackets

The yield/credit block that stopped at 08-06 for four consecutive runs now prints **08-10**. That
single publication settled **S51, S66 and S70** in this run's HANDOVER (§2b there). ⚠ **A one-day skew
persists** (`T10YIE` and `RRPONTSYD` carry 08-11 while the constant-maturity block carries 08-10) — the
per-series clock is real, it is just no longer blocking.

### A-2 · ★★★ The payroll shock produced the OPPOSITE of a growth scare, on all three axes

The registered question — *"was 08-07 dovish relief or credit fear?"* — is answered, and **the answer is
neither.** Both halves quoted (C2), like-for-like, anchored on the pre-print **08-05** close:

| Axis | 08-05 (pre-NFP) | 08-07 | **08-10** | Move |
|---|---|---|---|---|
| `DGS2` | 4.18 | 4.19 | **4.25** | **+7bp** — the front end **SOLD** after a −23k payroll |
| `DGS10` | 4.63 | 4.65 | **4.72** | +9bp |
| derived 2s10s | +0.45 | +0.46 | **+0.47** | **+2bp — the bear steepener persisted** |
| `DFII10` (real) | 2.41 | 2.40 | **2.43** | +2bp |
| `T10YIE` (breakeven) | — | 2.25 | **2.29** (08-11: 2.27) | **+4bp** |
| HY OAS | 2.75 | 2.70 | **2.70** | **−5bp — credit TIGHTENED through the shock** |
| IG OAS | 0.78 | 0.78 | 0.78 | flat |

**Decomposition (real quoted with breakeven, as the rule requires):** the 10y's +9bp is **+2bp real ·
+4bp inflation-expectations** on the 08-10 pair (4.72 = 2.43 + 2.29). ⇒ **the post-payroll move is
inflation-expectation-led, not real-rate-led** — the first run in five where the split is not ~100% real.
That is a materially different regime read from the one carried since 2026-07-25 (M123: *"~100% of the
move is real"*).

⇒ **A weak payroll print was read by the bond market as a reason to price FEWER cuts, and by the credit
market as no reason to widen at all.** Any framing of 08-07 as a growth scare is refuted on this desk's
own primary series.

---

## §B · Positioning — **the COT file is FRESH for the first time in three runs**

`us_flow --cot`, published for the **2026-08-11** Tuesday close. The 08-08/08-09/08-10 runs all quoted the
**08-04** snapshot, which **pre-dated NFP**; this one contains it.

| Instrument | Net spec | Wk Δ | 1y %ile | Read |
|---|---|---|---|---|
| **Copper** | +77,123 | +9,842▲ | **100%** | 🟢 crowded-long — **96th → 100th, and it kept building** |
| USD Index | +22,499 | +5,302▲ | **81%** | 🟢 crowded-long, **still adding** |
| S&P 500 (E-mini) | −27,258 | −10,062▼ | 80% | 🟢 |
| UST 2Y | −1,004,228 | +120,346▲ | 65% | 🟡 — **shorts covered into the front-end selloff** |
| Gold · Silver | +197,634 · +22,280 | +15,564▲ · +63▲ | 29% · 29% | 🟡 — ⚠ **the metal that ripped is NOT the crowded one** |
| Russell 2000 | −8,899 | −7,520▼ | 26% | 🟡 |
| **WTI Crude** | +23,033 | +3,275▲ | **18%** | 🔴 crowded-short — **into a +10.6% five-session rally** |
| **UST 10Y** | −979,243 | −103,124▼ | **3%** | 🔴 — shorts **added 103k** into a rising yield |
| **Nat Gas** | −197,546 | −6,747▼ | **1%** | 🔴 |
| **Nasdaq-100** | −35,006 | −25,091▼ | **0%** | 🔴 crowded-short |

⚠ **Context, not a trigger** — the US has no investor-type feed and this is a Tuesday-close file with a
3–4 day publication lag. Two lines are load-bearing below: **copper at the 100th percentile** (§C-2's
Materials question) and **WTI at the 18th percentile short into a violent crude rally** (§C-1).

**FINRA Reg SHO, 2026-08-11** — `XLB z +2.02 🔴 (5v5 +14.8▲)` · `MET +1.55 🔴 (+24.8▲)` · PSX +0.85 ·
JPM +0.85 · VLO +0.68 · MPC +0.66 · NEM +0.47 · NDAQ +0.46 · **XOM −0.41 (the only clean-rise)**.
⚠ **XLB is being shorted hard into the outperformance §C-2 measures** — recorded as the contrary axis.

---

## §C · The tape — settled 2026-08-11, **two genuinely new bars** (bench `SPY` named inline, C1)

`SPY` itself: **1d −0.32% · 5d −0.10% · 20d +2.49%.**

| Sector ETF | exc1 | exc5 | exc20 | exc60 |
|---|---|---|---|---|
| **XLE** Energy | **+1.57** | **+4.22** | **+4.50** | +1.93 |
| **XLV** Health Care | +0.06 | **+3.75** | +3.65 | **+11.59** |
| **XLB** Materials | +0.43 | **+2.48** | +2.64 | +0.05 |
| XLY Cons Disc | −0.04 | +0.90 | +0.39 | −2.51 |
| XLF Financials | +0.30 | −0.04 | +0.39 | **+9.70** |
| XLI Industrials | +0.92 | −0.28 | +0.42 | +3.42 |
| XLK Info Tech | +0.20 | −0.33 | −1.15 | +0.68 |
| XLC Comm Svcs | −0.18 | −0.59 | −2.65 | **−7.98** |
| XLP Staples | +0.01 | −0.70 | −0.97 | −3.33 |
| **XLU** Utilities | **+1.48** | −0.99 | **−7.00** | −5.82 |
| XLRE Real Estate | −0.40 | **−2.31** | −3.39 | −2.61 |

Cross-asset: **GLD exc5 +7.26 · SLV exc5 +8.85** (both **negative** on exc60: −9.14 / −25.45) ·
UUP exc5 +0.03 (5d **−0.07%**) · TLT exc5 −0.66 · HYG exc5 +0.05 · FXY −0.79 · FXE +0.24.

### C-1 · ★★★ Energy inverted violently in two sessions, and it is a WHOLE-BARREL move

**XLE went from exc5 −6.95 (worst of eleven, 08-07) to +4.22 (best of eleven, 08-11) in two sessions.**
The underlying, on settled futures closes:

| | 08-04 | 08-07 | **08-11** | 5-session |
|---|---|---|---|---|
| `CL=F` | 75.77 | 78.18 | **83.81** | **+10.611%** |
| `HO=F` | 3.7705 | 3.9024 | **4.2919** | **+13.828%** |
| **HO% − CL%** | — | — | — | **+3.217pp** |

⇒ **both legs rallied**, which is the signature S55 was written to detect and it scored **branch C**
(§HANDOVER 2b): the release/premium question **stays unseparated**. ★ **What is new and settled**: the
crude leg moved **+10.6% while speculative positioning sat at the 18th percentile short and ADDED**.
A crowded short into a supply-narrative rally is the cleanest squeeze geometry on the board — **and it
is context, not a trigger (D6).**

### C-2 · ★★★ Materials: a pre-registered anti-signal FIRED and refuted the inherited reading

**P44 (08-10) claimed direction A at ~60%**: *"S57's branch A fires and means nothing about Materials —
85% of the observable is NEM, whose driver is a $1.95bn JV settlement."* **Its registered anti-signal (a)
was: "if XLB's ex-NEM excess turns positive on a settled close, A is wrong and there is a sector leg."**

Measured this run on the 12 `us_top300` Materials names (5-session excess vs SPY, settled 08-11):

| | Value |
|---|---|
| XLB (the ETF) | **+2.484** |
| 12-name **cap-weighted** | **+3.381** |
| 12-name cap-weighted **EX-NEM** | ★ **+1.203** |
| 12-name **equal-weighted** | +2.502 |
| 12-name equal-weighted **EX-NEM** | ★ **+0.908** |
| Names positive | **8 of 12** (NEM +20.03 · APD +5.05 · CRH +2.58 · FCX +2.43 · LIN +1.32 · VMC +1.04 · SHW +0.89 · ECL +0.63; negative: MLM −0.29 · STLD −0.43 · NUE −0.66 · CTVA −2.57) |
| NEM's cap weight in the 12 | **11.6%** — it carries ~52% of the cap-weighted excess, **not 85%** |

⇒ **P44's anti-signal (a) fired: the ex-NEM leg is positive on a settled close.** **Direction A is
refuted by its own registered condition, and P44 is scored MISS in §F.** ★ **Triangulation, three
independent constructions agreeing**: (i) the ETF (+2.484), (ii) the ex-NEM constituent basket (+1.203
cap / +0.908 equal), (iii) **the sweep's own `wflow_ex_top1` for Materials, +0.168 against a headline
wflow of −0.069** — the only construction that says Materials is negative is the one **owned by a single
name (LIN, 24.7% of sector cap, a G3 flipper)**.
⚠ **What does NOT follow** (C4): this does not say the sector leg is a *dollar* leg. GLD +7.26 / SLV
+8.85 against UUP ~flat says the live driver is **precious metals**, and gold's own COT sits at the
**29th** percentile while **copper** sits at the **100th** — i.e. **the metal that moved is not the
crowded one.** The leg is real; its named cause is not established.

### C-3 · The two-window contradictions worth naming

- **XLU: best sector on the day (+1.48 exc1) and worst on 20 days (−7.00).** The sweep says the same
  thing from the other side — **Utilities wflow −0.475 / eqflow −0.482, 13 reds of 15, breadth 0.0, the
  board's worst.** A one-session bid inside the worst medium-term tape is a bounce until a second bar.
- **XLF: exc60 +9.70 (2nd best) against exc5 −0.04 and exc20 +0.39.** M149's decaying-stock shape, on the
  sector this desk carries at N+/OW.
- **XLC: negative on all four windows (−0.18 / −0.59 / −2.65 / −7.98)** — the only sector that is, for a
  second consecutive measurement. ⚠ **R56 binds: any breadth claim must be re-derived ex-EA, which is
  still in `us_top300.csv`.**
- **XLV: exc60 +11.59, the board's best, with exc5 +3.75 now agreeing.** The only sector where the long
  and short windows point the same way and both are strong.

---

## §D · News — **an empty denominator, and the zero is the instrument's**

🚨 **This stage could not run its event pass, its trajectory pass, its 7-bucket sweep or its blind-spot
pass, and it does not substitute anything for them.**

| Probe (all `--scope foreign`) | Result |
|---|---|
| `fts search <5 queries> --days 7 --count` | **`URLError` — remote `/exec` unreachable**, twice, ~40 min apart |
| local fallback index `data/news_fts.db` | **0 bytes** |
| `brief --body 2` | **0 articles → 0 events → 0 market events** |
| `thread --days 7` | 08-06 **816** · 08-07 **719** · 08-08 283 · 08-09 285 · 08-10 **720** · **08-11 0** · **08-12 0** |
| client store `news_vectors.db` | 388,245 articles; **last article 2026-08-10 21:45 UTC**; sync cursor **2026-08-11T08:00** |
| sweep `vel_coverage` | **11.3%** (34/300) ⇒ velocity axis excluded, all 300 names scored on 3 axes |

**The falsification the gate requires, and its limit stated honestly (C3):** the pool through **08-10**
is full — **50,234 foreign articles for 08-04→08-11**, including 361 `Nvidia`, 167 `tariff`, 60
`Broadcom`. So the low coverage is **not** evidence of a quiet market. **But whether collection itself
continued after 2026-08-11 08:00 KST is `unknown`**: the client's store stops there and the server is
unreachable, so this desk cannot distinguish *"the server kept collecting and the client did not sync"*
from *"collection stopped."* ⇒ **`D235` registered.**

⇒ **Rights this stage exercises: none on the news axis.** No proposition below cites a theme tag, a
thread curve, a velocity, an outlet count from 08-11 or 08-12, or a "quiet" claim in either direction.
**Every inherited news-grade claim (P41 · P43) is carried at its 08-10 grade and explicitly not refreshed.**

---

## §E · Propositions — falsifiable, both branches, mandatory anti-signal

> ID counters (D137, checked at read time): `handoff_id_audit` reports **max M559**, because the 08-10
> run's promised **M560–M572 never landed** (HANDOVER §5). This run's writeback **rescues M560–M572 at
> their original numbers** and **this stage therefore takes `M573–M580`.** It registers **`D235`** and
> **no bracket** — **PREMORTEM owns registration** and must apply the `D216` σ-distance test.

### P46 — ★★★ The payroll shock resolved AGAINST the growth-scare reading on all three axes, and that is now scored, not argued

- **Claim** `[measured, FRED]`: from the 08-05 pre-print close to the 08-10 close, **`DGS2` +7bp,
  2s10s +2bp to +0.47, HY OAS −5bp to 2.70, IG flat.** The three brackets that owned this question all
  settled the same way this run — **S51 FIRED-A** (bear steepener persists), **S66 FIRED-B** (neither
  leg of the growth-scare conjunction moved), **S70 FIRED-A** (credit relief).
- **Direction A (the repricing is hawkish and holds, ~55%)**: a −23k payroll that sells the front end is
  a market pricing **fewer cuts**, consistent with the 07-29 hold-with-three-hike-dissents. **FIN's NIM
  mechanism keeps its carrier; UTIL/RE stay wrong-footed by the absence of a duration bid** (XLU exc20
  −7.00, XLRE −3.39).
- **Direction B (it is a pre-CPI positioning artifact and unwinds tonight, ~45%)**: the whole move sits in
  the two sessions before a binary print, `T10YIE` did **+4bp of the +9bp** (an inflation-expectation
  move, not a growth one), and **UST 10Y spec is at the 3rd percentile short having ADDED 103k** — a
  cover on a cool CPI reverses the curve reading without any macro news.
- **Track KPI**: `DGS2` and HY OAS at the first `[FRED]` close covering **08-12** (S73's macro leg);
  2s10s vs the **+0.20** S23 flattener line (**27bp** of buffer).
- ⚠ **Mandatory anti-signal, both sides**: **(a)** HY OAS ≥ **2.96** on any settled close kills A (it is
  S70's own branch-B line, 26bp away); **(b)** `DGS2` ≤ **4.10** with 2s10s widening kills A the other
  way — a bull steepener is the leg S51 refuses to score and S66's A′ owns. **(c)** kills B: if the
  front end holds ≥4.25 through the CPI settle, the repricing was not positioning.
- **Catalyst**: **2026-08-12 CPI `[bls✓ 🔀binary]`**, macro leg settling at the first FRED close covering it.

### P47 — ★★★ Energy's inversion is a whole-barrel move into a crowded short, and the product-specific reading remains unavailable

- **Claim** `[measured, settled futures + ETF + COT]`: `CL=F` **+10.611%** and `HO=F` **+13.828%** over
  five settled sessions; XLE **exc5 −6.95 → +4.22**; **S55 scored C at +3.217pp** (branch B needed +6.5);
  **S60 FIRED-A at +4.218** — the 08-04 XLE sale was wrong on its own observable. WTI spec positioning:
  **18th percentile short, +3,275 added.**
- ★ **Why this is a proposition and not a datapoint**: the desk has spent four runs trying to separate
  *physical release* from *war premium* (S49 → R47 → S55). **The five-session move says the separation is
  not available**: a difference-of-two-legs cannot discriminate when **both legs rise double digits**.
- **Direction A (war premium rebuilding, ~55%)**: the Hormuz condition set named on 08-08/08-09 (P41,
  inherited, **not refreshed** — §D) binds; crude carries the whole barrel; **ENRG's N+ has a live macro
  carrier again** and the refiners ride it as beta, not as margin.
- **Direction B (physical/inventory tightening, ~45%)**: distillate outran crude by **+3.2pp**, which is
  the *direction* of a product-specific bid even though it did not reach S55's threshold; **S67's refiner
  median RS20 is +8.392 with all three legs positive and rising** (MPC +8.39 · VLO +4.97 · PSX +8.88).
- **Track KPI**: **S67 settles 08-13**; the dist−gas spread on settled closes; `CL=F` vs the 18th-percentile
  short in the **08-14** COT release.
- ⚠ **Mandatory anti-signal, both sides**: **(a)** a settled `HO% − CL%` ≤ **−3.0** (S55 branch A's line)
  kills A — the release would be product-specific after all; **(b)** crude giving back >5% while the
  refiner median RS20 holds positive kills A the other way and confirms B; **(c)** kills B: refiner RS20
  collapsing with crude on one session ⇒ they are crude beta, not margin.
- ⚠ **R47 binds and is NOT un-withdrawn here**: no stage may argue *"the distillate bottleneck released"*
  as established fact. **S55 scored C — the question is open, not answered.**
- **Catalyst**: **S67 08-13** · Hormuz **undated `[blank]`, not guessed** (`S74` owns it → 08-24).

### P48 — ★★★ Materials has a real sector leg, and this desk's own anti-signal is what proved it

- **Claim** `[measured, settled prices]`: **XLB exc5 +2.484 · ex-NEM cap-weighted +1.203 · ex-NEM
  equal-weighted +0.908 · 8 of 12 names positive · NEM only 11.6% of sector cap.** **S57 FIRED-A**, and
  **P44's registered anti-signal (a) fired with it** ⇒ **MATR UW− has lost both of its stated legs and the
  "it's just one name" defence is measured false.**
- ★ **The sweep's own decomposition agrees from the other side**: Materials headline `wflow` **−0.069**
  but **`wflow_ex_top1` +0.168** — the negative sign is **owned by LIN** (24.7% of sector cap, `🔴분산`,
  exc5 +1.32), and **PREFLIGHT G3 forbids promoting or demoting Materials on `wflow` for exactly this
  reason.** Three constructions (ETF · ex-NEM basket · ex-top1 flow) point one way; only the LIN-owned
  cap-weighted flow points the other.
- **Direction A (a metals-complex leg, ~55%)**: **GLD exc5 +7.26 · SLV +8.85** while **UUP is flat
  (5d −0.07%)** ⇒ the driver is precious metals, **not** the dollar. ⚠ And gold's spec long is only at the
  **29th** percentile — an uncrowded move has room.
- **Direction B (a dollar/industrial-metals leg, ~45%)**: `DTWEXBGS` **119.5977 (08-04) → 119.0649
  (08-07) = −0.45%**, **copper spec at the 100th percentile**, FCX exc5 **+2.43** and CRH/VMC/APD
  positive ⇒ breadth beyond the miners.
- **Track KPI**: **XLB ex-NEM exc5** (the estimator this run built, **+1.203**); `DTWEXBGS` on its next
  print; the **08-14** copper COT.
- ⚠ **Mandatory anti-signal, both sides**: **(a)** if XLB's ex-NEM exc5 turns **negative** on a settled
  close, the sector leg was NEM after all and P48 is wrong; **(b)** if gold/silver give back while XLB
  holds, A is wrong and B owns it; **(c)** **`XLB`'s FINRA z is +2.02 with 5v5 +14.8▲ — the largest short
  build on this run's pull sits on the instrument this proposition is measured on.** If that short is
  right, both directions are early.
- **Catalyst**: **S57 already fired** (no further settlement) · **2026-08-12 CPI** · copper COT 08-14.

### P49 — ★★ The desk is blind on the news axis for two days, and the correct output is to say so, not to infer quiet

- **Claim** `[measured]`: the foreign feed returns **0 articles for 08-11 and 08-12** against a 5-day
  weekday mean of ~750/day; the remote query API is unreachable; the local FTS index is **0 bytes**; the
  client store's cursor stops at **2026-08-11 08:00 KST**.
- **Direction A (a client-side sync/tunnel failure, ~65%)**: the store holds 388k articles and the last
  one is timestamped inside a normal collection cadence ⇒ the *server* likely kept collecting and only the
  client's link died. **Nothing about the market is implied.**
- **Direction B (collection itself stopped, ~35%)**: `_rss_feeds`' own documented failure mode is that
  feeds die **silently with HTTP 200 and entries=0** (measured 2026-07-18 across 11 feeds), so a genuine
  collection halt would look exactly like this from here.
- **Track KPI**: the first non-zero day count from `thread --days 7`; whether `data/news_fts.db` gains bytes.
- ⚠ **Mandatory anti-signal, both sides**: **(a)** if the API returns and the missing days back-fill, B is
  wrong; **(b)** if the API returns and 08-11/08-12 are still empty **server-side**, A is wrong and this is
  a collection outage — a P6 server-console item for a human.
- ⚠ **This proposition exists so that no downstream stage converts an instrument outage into a market
  reading.** It is the R59/G1 lesson written as a dated claim. **`D235`.**
- **Catalyst**: `[blank]` — **not guessed.**

### P50 — ★★★ July CPI tonight: the branch map, written BEFORE the print

- **Claim** `[structural]`: **CPI 2026-08-12 08:30 ET `[bls✓ 🔀binary]`**, then **PPI 08-13 `[bls✓]`**.
  **S73** owns the print with two independently-scored legs; **S71** owns the CPI→PPI divergence;
  **S72** settles on the CPI-day close. **The regime context that makes this two-sided**: the FOMC held
  3.50–3.75% on 07-29 **with three hike dissents**, the front end has just sold 7bp on a **negative**
  payroll, and breakeven carried +4bp of the 10y's +9bp.
- **Direction HOT (~45%)**: `DGS2` extends above 4.25, hike-odds rebuild, the dollar recovers.
  **Rips against: UTIL · RE · MATR** (the duration and metals legs, i.e. **P48's direction A**).
  **Rips for: FIN** (P46-A's NIM carrier).
- **Direction COOL (~45%)**: front-end rally, duration bid, **UTIL/RE relief and the metals leg extends**;
  **FIN loses the mechanism S51 just re-confirmed**.
- **Direction IN-LINE (~10%)**: **S72's sign-pattern test becomes the informative object**, because a
  no-information print is exactly when four GICS labels moving together would reveal one exposure.
- ⚠ **Mandatory anti-signal, both sides**: **(a)** a CPI delay ⇒ **S72 VOID** (its own registered
  condition); **(b)** an intraday halt truncating the 08-12 session ⇒ **S72 VOID**; **(c)** if BOTH the
  front end sells **and** utilities rally, neither direction above describes the tape and the
  proposition is wrong as constructed.
- 🚨 **PREMORTEM's mandate, restated**: this is the ≤48h binary. **A one-way tilt into it is a protocol
  violation.** S73 exists; PREMORTEM must verify its branch distances in σ (D216) and add coverage for
  any tilt it does not reach.
- **Catalyst**: **2026-08-12 08:30 ET**, then **2026-08-13 PPI**.

---

## §F · Self-backtest — **2 scored, 1 MISS on a fired anti-signal, 2 unscoreable**

| Proposition | Registered condition | Settled outcome | Score |
|---|---|---|---|
| **P41** (08-10) — Hormuz two-sided; direction B (~60%): *"S61's tanker leg and the whole ENRG complex stay bid"* | Track KPI (ii) thread curve · (iii) **S61's EW{STNG,FRO} 5-session excess, −4.184** | ★ **The ENRG half is confirmed hard** (XLE exc5 −6.95 → **+4.22**, crude +10.6%). ★ **The tanker half is refuted**: S61's EW ran **−4.184 → −4.711 → −2.411** and **never approached branch A (+6.80)** ⇒ **no war-risk premium appeared in the tankers even as crude ripped.** ⚠ KPI (ii) unreadable (§D) | **HALF** — one named leg confirmed, one named leg refuted |
| **P42** (08-10) — direction B (~55%): the compression was a gasoline event and supply is re-tightening | Track KPI = **S55's HO%−CL% at the 08-11 settle** (B ≥ +6.5 · A ≤ −3.0), settled at +0.318 | **S55 settled +3.217 — moved 2.9pp toward B and did not reach it.** Registered anti-signal **(a)** *"spread back toward/below zero ⇒ B is wrong"* **did NOT fire**; anti-signal **(b)** *"distillate falls while gasoline holds"* **did NOT fire** (distillate +13.8%) | **HALF** — direction confirmed, threshold not met |
| **P43** (08-10) — CXMT is an uncovered supply-side axis | Track KPI = an Apple/CXMT **filing**, MU revision breadth, whether it reaches HBM | **No news bar exists (§D); no filing checked** | **UNSCOREABLE** — carried unrefreshed at `[news]` grade |
| **P44** (08-10) — direction A (~60%): S57-A fires and means nothing about Materials (85% NEM) | ⚠ **anti-signal (a): "if XLB's ex-NEM excess turns positive on a settled close, A is wrong"** | ★★★ **THE ANTI-SIGNAL FIRED.** ex-NEM cap-weighted **+1.203**, equal-weighted **+0.908**, **8 of 12 names positive**, NEM only **11.6%** of sector cap (§C-2) | ★ **MISS** — killed by its own registered condition, one run later |
| **P45** (08-10) — direction A (~55%): a crowded dollar long unwinding ⇒ weakness extends | Track KPI = UUP · `DTWEXBGS` on print · CPI | **UUP 5d −0.07% = flat** (exc5 +0.03), **`DTWEXBGS` printed 119.0649 @08-07, −0.45% from 08-04**, and the **COT long ADDED again to the 81st percentile.** Anti-signal (a) was *"UUP rises while the long keeps building"* — **UUP did not rise, it went flat** ⇒ the anti-signal did not fire, but neither did the claim | **UNSCOREABLE — `indistinguishable` (C4)**, ±0.07% is inside a daily noise band. **Not counted as a hit** |

**Running hit-rate, appended.** This run's line: **2 HALF · 1 MISS · 2 unscoreable.**
★★★ **The MISS is the most valuable row on this page and it is recorded as a MISS, not softened.** P44
was written yesterday by this desk, carried a ~60% direction, **named the exact measurement that would
kill it**, and that measurement killed it on the next settled bar. **A desk that only scores its hits has
no track record** — and the inverse rule applies here: a desk whose anti-signals never fire is not writing
real anti-signals. ⚠ **This is also a D48 instance in the healthy direction**: verification arrived after
the assertion, and the assertion is being retracted rather than edited.

---

## §G · ★ Sector transmission matrix — all 11 GICS. **This is ROTATION's input.**

**Inherited verdicts** (last completed run, `2026-08-10/SECTOR_ROTATION.md`, verified on disk):
`INDU OW− · ENRG N+ · FIN N+ · IT N · HLTH N · DISC N · MATR N− · COMM UW · UTIL UW · STPL UW− · RE UW`.

⚠ **Flow numbers are 3-axis** (`vel_coverage` 11.3% ⇒ velocity excluded, all 300 names scored alike) —
**stated on the same line as the conclusion, as G1 requires.** Δ is a **2-session** change (08-07 → 08-11).
🚨 **G3 flippers — Financials (BRK-B) · Industrials (CAT) · Materials (LIN) — may NOT be promoted or
demoted on `wflow`.**

| # | Sector | Wind (this stage) | Driving prop | Numbers (settled 08-11 · bench SPY · flow 3-axis) |
|---|---|---|---|---|
| 1 | **Energy** | ★ **N+ → argues for promotion; its macro carrier is BACK** | **P47** | exc1 **+1.57** · exc5 **+4.22 (best of 11)** · exc20 **+4.50 (best)** · exc60 +1.93. Sweep **rank-1 on both axes: wflow +0.360 · eqflow +0.163**, Δ **+0.074 (only positive-Δ sector but one)**, no flipper. **S60 FIRED-A · S55 C · crude +10.6% into an 18th-pctile short** |
| 2 | **Health Care** | ★ **N → argues for promotion, and it is the cleanest on the board** | — | exc5 **+3.75** · exc20 +3.65 · **exc60 +11.59 (best)** — **the only sector where all four windows agree and the long window is strongest.** Sweep **wflow +0.230 · eqflow +0.217 (rank 2)**, Δ **+0.157 (largest on the board)**. ⚠ **breadth 0.0 (0🟢/2🔴 of 32)** — C7's old shape: the level is strong and the participation is not measured as broad |
| 3 | **Materials** | ★★ **N− → its UW leg is REFUTED; ROTATION must re-argue, not carry** | **P48** | exc5 **+2.48** · exc20 +2.64. **S57 FIRED-A** and **P44's anti-signal fired**: ex-NEM **+1.203**, 8/12 positive. `wflow −0.069` is **LIN-owned** (ex-top1 **+0.168**) ⇒ **🚨 G3 forbids a wflow-based call here.** ⚠ Contrary axis: **XLB FINRA z +2.02, 5v5 +14.8▲** |
| 4 | **Industrials** | **OW− held — and it is now the weakest overweight case on the board** | — | exc1 +0.92 · exc5 **−0.28** · exc20 +0.42 · exc60 +3.42. Sweep **wflow −0.015 · eqflow +0.048 · breadth 0.08**, Δ −0.055. 🚨 **G3 flipper (CAT, ex-top1 +0.059)** ⇒ no wflow-based call. **Three sectors now out-rank it on every window** |
| 5 | **Financials** | **N+ held; its mechanism survived and its breadth did not convert** | **P46** | exc60 **+9.70 (2nd best)** against exc5 −0.04 · exc20 +0.39 — **M149's decaying-stock shape.** **S51 FIRED-A** (2s10s +0.47, 27bp of buffer) · **S65 FIRED-C** (median RS20 +2.871; ex-BRK-B +3.084, gap 0.21pp). Sweep wflow +0.004 · eqflow −0.043 · **breadth 0.09**. 🚨 **G3 flipper (BRK-B, ex-top1 −0.060)** |
| 6 | **Information Technology** | **N held** | — | exc5 −0.33 · exc20 **−1.15** · exc60 +0.68 — ≈flat on every window. Sweep **wflow −0.151 · eqflow −0.218**, **23 reds of 56**, Δ −0.142, **breadth 0.11 (highest of 11)**. ⚠ **P43's CXMT axis is carried UNREFRESHED (§D)** |
| 7 | **Consumer Discretionary** | **N held** | — | exc1 −0.04 · exc5 +0.90 · exc20 +0.39 · exc60 −2.51. Sweep wflow −0.180 (AMZN 40.2% of cap, ex-top1 **−0.294**) · eqflow **+0.010** ⇒ **cap and breadth disagree in sign.** **C3: no signal, not a neutral verdict** |
| 8 | **Consumer Staples** | **UW− held** | — | exc5 −0.70 · exc20 −0.97 · exc60 −3.33. Sweep wflow −0.223 · eqflow −0.205 · breadth 0.0 · **Δ −0.003 (the flattest on the board)**. **Deep-dived 08-10 for the first time in recorded history** |
| 9 | **Communication Services** | **UW held — the only sector negative on all four windows** | — | −0.18 / −0.59 / −2.65 / **−7.98**. Sweep **wflow −0.474** vs **eqflow −0.016** — a **0.458** gap owned by GOOGL (38.2%). ⚠ **R56: EA is still in `us_top300.csv`; any breadth claim must be re-derived ex-EA** |
| 10 | **Utilities** | **UW held — and the sweep is more negative than the tape** | — | exc1 **+1.48 (best on the day)** vs exc20 **−7.00 (worst)**. Sweep **wflow −0.475 · eqflow −0.482 · 13 reds of 15 · breadth 0.0 — the worst on every flow measure.** A one-session bid is not a turn |
| 11 | **Real Estate** | **UW held** | — | exc5 **−2.31 (worst of 11)** · exc20 −3.39 · exc60 −2.61. Sweep wflow −0.222 · eqflow −0.182 · breadth 0.0 · **Δ −0.190 (2nd worst)**. Consistent across price and flow |

**Universe headline**: n=300 · **wflow −0.148** · **🟢 17 · 🟡 202 · 🔴 81**.

⚠⚠ **What this stage does and does not claim.** Unlike the 08-08→08-10 runs, **the price inputs above are
genuinely new**, so a delta is legitimate and three sectors carry a real argument for change:
**ENRG (promotion), HLTH (promotion), MATR (its UW leg refuted).** ★ **But this stage does not change a
verdict — ROTATION owns the decision (stage ownership), and G3 removes `wflow` as an admissible basis for
three of the eleven.** The arguments are handed over with their instrument caveats attached.

---

## §H · Catalysts injected at run start

`catalyst_calendar.py --days 5` → `llm_outputs/2026-08-12/CATALYST_WATCH.json`.
**⚠ 3 BINARY catalysts in window — both-sides brackets REQUIRED for each.**

| When | Event | Axis | Type | Owning bracket |
|---|---|---|---|---|
| 🚨 **D-0 · 2026-08-12 08:30 ET** | **July CPI** | inflation | 🔀binary `[bls✓]` | **S73** (2 legs) · **S72** (CPI-day sign pattern) · **P50** |
| **D-1 · 2026-08-13** | **July PPI** | inflation | 🔀binary `[bls✓]` | **S71** (CPI→PPI divergence) |
| **undated** | Iran *"Strait of Hormuz open"* statement | oil | 🔀binary `[news👁]` | **S74** (→08-24) · 🚨 **S8 still `[blank]`, un-scoreable for a TENTH run — human, P5** |

**[EARNINGS]** none in window. **[STRUCTURAL]** none — `data/catalysts/structural_schedule.json` is
human-maintained and empty. ⚠ **Recorded as "not populated", not as "no structural catalysts exist."**

---

## §I · New facts registered by this stage (`M573–M580`) and one new dig

| ID | Fact |
|---|---|
| **M573** | **`D212` resolved**: the FRED yield/credit block published through **2026-08-10** after four blocked runs, settling S51/S66/S70. A one-day per-series skew persists (`T10YIE`/`RRPONTSYD` at 08-11) |
| **M574** | **The post-NFP move is inflation-expectation-led, not real-rate-led**: 10y +9bp = **real +2bp · breakeven +4bp** (08-10: 4.72 = 2.43 + 2.29), against M123's carried *"~100% real"* |
| **M575** | **Credit tightened through the payroll shock**: HY OAS **2.75 → 2.71 → 2.70** (08-05→08-10), IG flat at 0.78. The growth-scare conjunction (S66-A) never fired |
| **M576** | **XLE inverted from worst to best in two sessions** (exc5 **−6.95 → +4.22**) on `CL=F` **+10.611%** and `HO=F` **+13.828%** — both legs, i.e. whole-barrel |
| **M577** | ★ **Materials has a sector leg ex-NEM**: 12-name cap-weighted exc5 **+3.381**, **ex-NEM +1.203**, equal-weighted ex-NEM **+0.908**, **8 of 12 positive**, NEM **11.6%** of sector cap. **P44's anti-signal (a) fired** |
| **M578** | **Three constructions agree on Materials and the dissenting one is single-name-owned**: ETF +2.484 · ex-NEM basket +1.203 · sweep `wflow_ex_top1` **+0.168** vs headline `wflow` **−0.069** (LIN, 24.7% of cap) |
| **M579** | **The metal that ripped is not the crowded one**: GLD exc5 **+7.26** / SLV **+8.85** with gold spec at the **29th** percentile, while **copper sits at the 100th** and UUP is flat (5d −0.07%) |
| **M580** | **Crude rallied 10.6% in five settled sessions with speculative positioning at the 18th percentile short and ADDING (+3,275)** — the cleanest squeeze geometry on this run's board. **Context, not a trigger (D6)** |

| ID | Dig |
|---|---|
| **`D235`** | **The desk cannot distinguish a client sync failure from a collection outage.** `brief`/`thread` read the client-owned `news_vectors.db` and report **0 articles for 08-11/08-12**; the remote API is unreachable and the local FTS index is 0 bytes ⇒ *"the server kept collecting and the client did not sync"* and *"collection stopped"* are **observationally identical from here**. The feeds' own documented failure mode (HTTP 200 + entries=0, 11 feeds, 2026-07-18) makes the second live. **Positive-form remedy for a human: the client should surface its sync cursor age beside every news count**, so a zero is labelled `stale-client` or `empty-server` rather than just zero |

---

## ✅ EXIT CHECK

- [x] **Catalysts injected** (`catalyst_calendar --days 5` → `CATALYST_WATCH.json`); **3 binaries recorded, CPI at D-0**; indicators read (**FRED primaries + fresh COT + fresh FINRA**); **daily anchor read** (`2026-08-10/industry_US/MACRO_REPORT.md` propositions P41–P45 + matrix, and `module_report_tags show`)
- [x] **Events attempted via `brief --body 2 --scope foreign` and `thread --days 7`** — ⚠ **denominator is 0 for 08-11 and 08-12**, quoted with the 5-day comparison (~750/day). **§D states the gap rather than substituting for it**; the three recovery sections are **not** claimed to have been read, because there was nothing to read
- [x] **The zero is NOT converted into a coverage or a quiet claim in either direction.** The falsification probe (50,234 articles 08-04→08-11 in the client store) is quoted, **and its limit is stated (C3): whether collection continued is `unknown` ⇒ `D235`**
- [x] **7-bucket sweep and blind-spot pass NOT run and NOT faked** — the query path is dead in both routes (PREFLIGHT G1). No bucket count is quoted, so no mis-passed-CLI zero can enter a proposition
- [x] **Both halves of every headline print cited on like-for-like windows** — the NFP row carries **−23k payroll AND unemployment 4.1% down from 4.2%** (inherited, S66's registration text); the rate move carries **level AND decomposition**; Materials carries **cap-weighted AND equal-weighted, with and without NEM**
- [x] **Every relative-performance number names its benchmark inline** (`SPY` throughout; the sweep's own excess is labelled 3-axis); **no statistical result carried across markets** (W1)
- [x] **Credit axis read and cited** — `hy_oas` **2.70** and `nfci` **−0.529**; the "no growth scare" claim rests on HY OAS, not on narrative
- [x] **`real_10y` quoted with `breakeven_10y`** — 2.43 with 2.29/2.27, and the split is the point of M574
- [x] **Transmission matrix produced — all 11 sectors, one line each**, with the G3 flipper prohibition and the 3-axis caveat on the same lines as the conclusions
- [x] **Self-backtest appended — 2 HALF · 1 MISS · 2 unscoreable**, with **P44 scored MISS on its own fired anti-signal** and P45 refused as `indistinguishable` rather than counted
- [x] `MACRO_REPORT.md` written with primary numbers explicit; **M573–M580** and **`D235`** registered; **no new bracket registered (PREMORTEM owns registration)**; **no blind-spot terms folded back** — none could be measured this run, stated rather than skipped
- [x] **`report_lint.py` run on this stage's own output — `총 0건` (rules C1 · C2 · S6 · D6).** ⚠ It
      checks **form only**; a clean run is not a correct report, and the substantive check on this page
      is §F's MISS, which no linter can see

---

# §J · DRIFT ADDENDUM — appended post-run (Stage 11/11) · **APPEND-ONLY, nothing above is rewritten**

> The protocol names this a *"§5 ADDENDUM"*; this report's sections run §A–§I, so it is appended as
> **§J**. **The section-number deviation is logged rather than silently renumbered** — the original
> call stays visible next to its correction, which is the whole point of append-only (D165).

## J-1 · The detector is dead, and so is its usual substitute — **6th consecutive run**

```
drift_watch.py --report .../MACRO_REPORT.md
  → drift 질의 실패 (rc=2): 'drift' 는 원격 실행 불가(조회 전용)
```
`drift` has never been on the remote news API's allow-list (**D17, 6th run**). ⚠⚠ **New this run: the
substitute is dead too.** Prior runs fell back to `fts`/`burst` sweeps; today **`burst --days 2 --scope
foreign` returns `TimeoutError`** and `fts` returns `URLError`, while the local index is **0 bytes**.

⇒ 🚨 **This run has NO kill-switch detector of any kind.** **The correct output is to say so, not to
issue an all-clear** — a silent detector and a quiet tape return the identical value, which is `D235`
registered in §I. **No "no burst fired" line is written**, because this desk cannot know that today.

**What WAS re-pulled, and it moved nothing** — the second `[FRED]` pull pre-committed by this stage:
`DGS2` **4.25** · `DGS10` **4.72** · `DFII10` **2.43** · `hy_oas` **2.70** · `ig_oas` **0.78** · `VIXCLS`
**15.46** (all `asof` **2026-08-10**, unchanged from §A) · `T10YIE` **2.27** (08-11) · `DTWEXBGS`
**119.0649** (08-07). ⇒ **no macro observable changed between the report's baseline and this addendum**,
and **S73's macro leg is still unpublished** — its first covering close remains **≈08-13/08-14**.

## J-2 · ★★ A real finding, and it came from the schedule rather than the tape

The L2 rule says **do not stop at `--days 5` when an `ARMED` row names a date beyond it** (dig `D26`).
This run's rows settle **08-19** (S75 · S76 · S77 · S78) and **08-24** (S74), so a **`--days 14`**
re-pull was run. It surfaced a **FOURTH binary the 5-day window could not see**:

| When | Event | Type | Why it matters here |
|---|---|---|---|
| **D-14 · 2026-08-26** | **NVDA earnings** | 🔀binary | ★ **NVDA is a held epicenter name of the #1 cycle**, it is one of the **six velocity-lit 🟢** (SWEEP §2a), its **days21-60 is −10.9**, and it is the **cool-side ticket in `ACTION_TICKETS.md`.** **No bracket owns this print.** |

⇒ **`D26` reproduces exactly as written**: a five-day schedule read is not a complete schedule read.
**Handed to the next run's PREMORTEM as a registration item** — MACRO does not register brackets
(stage ownership), and 08-26 is outside every currently ARMED window.

## J-3 · What this addendum does and does not change

**Changes nothing above.** No proposition is edited, no matrix cell moves, no verdict is revised.
**Adds two carry items**: (i) the **NVDA 08-26 binary is un-bracketed**, and (ii) **this run ended with
zero kill-switch coverage** — so any overnight regime move (the 2026-07-13 proof case: a desk finished
at 15:59 and the Hormuz read flipped intraday) **would not have been caught.** ⚠ **That is a stated
exposure, not a reassurance.**

⚠ **And the imminent one, restated so it is the last thing on this page: July CPI prints 2026-08-12
08:30 ET.** The equity leg of **S73** settles at tonight's close and **S72** settles on the same bar.
**This report's three tilt changes (ENRG↑ · HLTH↑ · FIN↓) were made one session before that print**,
and PREMORTEM §2a records that a single print can wrong-foot all three at once because they may be
**one rate/duration exposure wearing three GICS labels** — the open **S72** contradiction, carried and
deliberately not resolved.

## §I-CORRECTION — appended at writeback (the D48 rule applied to this stage's own output)

⚠⚠ **§I above assigned this stage's facts `M573–M580`, and that was WRONG. It is left visible and
corrected here rather than rewritten.**

At §I write time, `handoff_id_audit` reported **max M559**, so M560+ read as free. The rescue then
opened the two orphaned files and found the numbers were **claimed, not free**:
- `llm_outputs/2026-08-09/industry_US/MACRO_REPORT.md` — **M544–M552**, which the 08-10 run
  pre-committed to re-register at **M560–M568** because the KR runs had taken M544–M559.
- `llm_outputs/2026-08-10/industry_US/MACRO_REPORT.md §I` — **M569–M579**, its own, never written back.

⇒ **M573–M579 collide with the 08-10 run's rescued block.** Renumbering a *rescued* finding creates two
ids for one fact (the `D211` complaint), so **the rescues keep their numbers and THIS stage's facts move
down**: **M573→M580 · M574→M581 · M575→M582 · M576→M583 · M577→M584 · M578→M585 · M579→M586 · M580→M587.**
**The writeback registers them at M580–M587.** The §I table above keeps its original numbers so the
error stays visible; **the handoff spine is authoritative.**

---
---

# ═══ RUN-2 ADDENDUM · MACRO — 2026-08-12 22:30–22:50 KST · **APPEND-ONLY** ═══

> Nothing above is rewritten — not §A–§I, not the §J DRIFT addendum, not the §I-CORRECTION.
> Analytical output only. No buy/sell recommendation anywhere (P4).
> **Clock: 2026-08-12 22:30 KST = 09:30 ET.** July CPI fired at **08:30 ET**; the cash session opens
> **at this clock**. Last settled equity bar remains **2026-08-11**.

## §R2-A · The inversion of RUN-1's defining asymmetry

RUN-1 opened by stating its shape: **"TWO fresh PRICE bars and ZERO fresh NEWS bars."** RUN-2 is the
mirror image, and it should be read that way:

| Axis | RUN-1 (11:40 KST) | **RUN-2 (22:30 KST)** |
|---|---|---|
| Price | 2 fresh settled bars (08-10, 08-11) | **ZERO new bars.** 08-12 does not exist on any interval |
| News | **0 events, 0 articles** — the query path was dead | ★ **2,237 articles → 337 events → 337 market events** for 08-12 alone; **08-11 recovered 0 → 774** |
| Macro release | CPI pending, ~10h out | ★ **CPI PRINTED** — but **not yet in `[FRED]`** |

⇒ **RUN-2's entire informational gain is on the news and event axis, plus one macro release that its
own primary instrument cannot yet see.** Every price statement below is inherited from the 08-11
settle. **No 08-12 price appears in this addendum.**

---

## §R2-B · July CPI — the print, and what grade it carries

| Field | Value | Grade |
|---|---|---|
| Headline | **+0.1% m/m** · **3.4% y/y** (from 3.5%) | `[WebSearch]` ×2 outlets |
| Core | **+0.2% m/m** · **2.5% y/y** | `[WebSearch]` |
| vs consensus | **in line** | `[WebSearch]` |
| Driver | rise **primarily energy**; **gasoline −2.9% m/m**; June **−0.4% m/m** | `[WebSearch]` |
| Release | **08:30 ET, on schedule — no delay** | `[WebSearch]` + `[bls✓]` via `catalyst_calendar` |
| `[FRED]` CPI | **332.568 @ 2026-06-01** — **July is NOT in FRED** | `[FRED]` |

🚩 **These figures are `[WebSearch]`-grade and may not be laundered into `[FRED]` or `[measured]`.**
★ **Cross-check actually run** (the A1 / corroboration rule): the external source says June was
**−0.4% m/m**; FRED's own June/May index levels give **332.568 / 333.979 = −0.42%.** ⇒ the external
source **reproduces the desk's primary series on the prior month.** That is the strongest available
validation short of the July release itself.

⚠⚠ **One external number was REJECTED.** A search result stated *"the 10-year rose 4bp to 4.31%, near
multi-year highs ~4.36%."* **`[FRED]` `DGS10` = 4.72 @ 08-10**, `DGS2` = 4.25. A **41bp** gap is not
rounding — that snippet describes a different tape. **Discarded. No external yield enters this run.**

### §R2-B1 · The FRED block, re-pulled this run

| Series | Latest | `asof` | vs RUN-1's read |
|---|---|---|---|
| `DGS2` | 4.25 | 08-10 | unchanged |
| `DGS10` | 4.72 | 08-10 | unchanged |
| derived 2s10s | **+0.47** | 08-10 | unchanged |
| `DFII10` real 10y | 2.43 | 08-10 | unchanged |
| `T10YIE` breakeven | **2.27** | 08-11 | unchanged |
| `BAMLH0A0HYM2` HY OAS | 2.70 | 08-10 | unchanged |
| `BAMLC0A0CM` IG OAS | 0.78 | 08-10 | unchanged |
| **`NFCI`** | **−0.549** | **2026-08-07** | ★ **NEW weekly print** (RUN-1 had −0.529 @ 07-31) |
| `RRP` | **1.25** | 08-11 | ★ from 0.975 @ 08-10 |
| `SOFR` | 3.64 | 08-11 | 3.63 @ 08-10 |
| `DFF` fed funds | 3.63 | 08-10 | unchanged |

★ **NFCI is the one genuinely new macro measurement RUN-2 owns, and it carries a revision trap.**
FRED now prints **07-31 = −0.546**, but RUN-1 quoted **−0.529** for that same date. **NFCI revises.**
⇒ **the 07-31→08-07 change must be computed inside one pull (−0.546 → −0.549 = −0.003, a third
consecutive easing) and never as "−0.549 minus RUN-1's −0.529."** Differencing across two runs' quotes
would manufacture a **−20bp** loosening that did not happen. Recorded as a method rule, not a footnote.

⇒ **Financial conditions eased into the print.** Combined with **HY OAS 2.70 / IG OAS 0.78** — both at
the tight end of their carried range — **there is no credit-stress signature in the pre-print data.**

---

## §R2-C · ★★★ The proposition this run exists to state: an in-line CPI measured the wrong month

**The print is backward-looking in a way that matters more than usual this cycle.**

1. **July's benign headline is energy-led *downward*: gasoline −2.9% m/m.**
2. **The oil supply picture inverted after the July window closed, and the event pass measures it:**
   - **Largest event of 08-12: *"Oil rises as doubts over US-Iran deal heighten supply concerns"*
     — 28 articles / 14 outlets**, the day's top cluster by outlet count.
   - Its sub-events: *"Hormuz closure squeezes global economy as oil demand destruction…"* [4/3] ·
     ★ ***"IEA: Global Oil Deficit To Hit 1.8 Million Bpd This Quarter"*** [3/3] ·
     *"IEA Says Oil Markets Are Facing a Wider Shortfall"* [2/2].
   - **BUILDING thread, 08-11→08-12: Libya — *"Fire rages after drone strikes Libya's largest oil
     refinery"* → *"Drone strikes power station near Libya's largest oil refinery"*** [4→4 outlets].
   - **BUILDING thread: *"Europe gas extends gains as EU storage at historical August low"*** [3 outlets].
   - **08-12 head: *"Ukraine Strikes Grain Terminals at Russia's Key Black Sea Port"*** [13/9].
3. ⇒ **The disinflation in this print is a measurement of the last month before the supply shock
   compounds — not evidence that the shock is absorbed.**

**Stated as a falsifiable proposition, not a forecast:**
> **P-R2-1.** *The July CPI's benign headline is a July-window artifact. If the energy channel is what
> it appears to be, the **August** print (2026-09) shows the energy contribution turning positive and
> the headline y/y **stops falling**.*
> **Falsifier**: August headline y/y prints **≤ 3.3%** with a **non-positive energy contribution** ⇒
> the supply-shock transmission is not reaching the index and this proposition is wrong.
> ⚠ **`[inferred]` — it rests on `[WebSearch]` CPI components and `[news]`-grade supply events.
> It may NOT be cited downstream as evidence for a tilt.** It is registered so it can be scored.

**The counter-evidence, stated rather than omitted (the desk's own W-rule):**
- Rate expectations moved the *other* way. **BUILDING thread 08-10→08-12, 4→2→5 outlets:**
  *"Cleveland Fed's Hammack: it will take more than one inte…"* → *"…says multiple rate hikes needed"*
  → ★ ***"The Odds of a September Rate Hike Have Plunged, but the…"*** [7 articles / 5 outlets, 08-12].
  Traders **tilted to HOLD from a ~50-50 hold-vs-hike split the day before** `[WebSearch]`.
- ⇒ **The market read the print as removing hike urgency; this section argues the input is stale.**
  **Both are recorded. The disagreement is the finding, and it is exactly what S73 was written to
  settle — on the bar that has not printed yet.**

---

## §R2-D · The event pass RUN-1 could not run (news axis restored)

`brief --date 2026-08-12 --scope foreign --body 2` — **2,237 articles → 337 events → 337 market / 0
non-market.** ⚠ Denominator stated because a "quiet" claim is only legal with one.
`thread --days 7 --scope foreign` — **08-06 816 · 08-07 720 · 08-08 283 · 08-09 289 · 08-10 783 ·
08-11 774 · 08-12 337**; **481 multi-day threads, 122 live, 212 new one-day events today.**

⚠ **The recovery was NOT free and the mechanism is recorded:** `thread` first returned **08-11 0 ·
08-12 0** *after* the search path was already alive. The two live on different instruments —
`fts`/`search` hit the server pool; `brief`/`thread`/`cluster` read the **client-owned
`news_vectors.db`**, whose cursor was stuck at **2026-08-11T08:00**. An `embed sync` pulled **14,637
articles (14,610 embedded, 27 dropped for missing publish time)**, moving the cursor to
**2026-08-12T21:34 KST** — **four minutes past the CPI release.** ⇒ ★ **"the news axis" is not one
instrument, and RUN-1's G1 FAIL masked a second, independent staleness underneath it.**

**Threads bearing on this desk's registered structure:**

| Thread (outlet curve) | Bears on |
|---|---|
| ★★ **NVDA's $500bn financing plan** — *"20 times what the te…"* [11/6] + *"Why Wall Street and Nvidia Are Building an Exotic Money Pi…"* + ***"Nvidia's show of financial force soothes credit markets"*** | **S41** (the AI-issuer credit channel S26's invalidation clause excluded) and **S40** (a capex GUIDE is not a capex MEASUREMENT). **The AI capex is being financed through a credit pipe, and the pipe is now the story** |
| **CoreWeave earnings beat, operating-margin upside** — BUILDING 3→3→5 across 08-06→08-12 | **S13 · S40** — an AI-capex *demand* datapoint arriving as a print, not a guide |
| **AI-infrastructure bottleneck moving into the electrical layer** — *"Jabil: The AI Infrastructure Bottleneck Is Moving Into I…"* → *"Better AI Infrastructure Stock: Vertiv vs. Eaton"* [2→4] | **UTIL / INDU** transmission — the power-equipment layer |
| **Optical / interconnect** — *"Market's Momentum Darlings Resurface as Optical Stocks Tak…"* | **S48**, the optical/interconnect bracket, registered → 09-30 |
| **Black Sea / Ukraine strikes on Russian port + refinery infrastructure** [13/9] | **S61** (tanker war-risk premium) and its ANNEX — the volume-destruction mechanism |
| **Hormuz / Iran, 28 articles / 14 outlets** + *"Factions in Iran openly fight over war's direction"* [8/6] | **S8** (undated, 11th run) · **S74** (reopening conditions) · **S52** |
| **Gold firms below a 10-week high into CPI** [4 outlets] · **JPY toward 160** [2→2→2] · **USD subdued** [23/6] | the dollar/real-rate leg |

⚠ **Curve shapes are not importance and outlet counts are not direction (P4)** — these are named as
objects to read, not as verdicts.

---

## §R2-E · Positioning — re-pulled, and it is the SAME file (no new information)

`us_flow --cot` returns the **2026-08-11 Tuesday close**, identical to RUN-1's read:
**Copper 100th %ile 🟢** (+9,842▲) · **USD Index 81st 🟢** (+5,302▲) · S&P500 80th 🟢 · UST 2Y 65th 🟡 ·
Gold 29th 🟡 · Silver 29th 🟡 · Russell 26th 🟡 · **WTI 18th 🔴** (+3,275▲) · **UST 10Y 3rd 🔴**
(−103,124▼) · **Nat Gas 1st 🔴** · **Nasdaq-100 0th 🔴** (−25,091▼).

★ **Stated because a re-pull that returns the same file is a finding, not a formality**: the desk has
**no post-CPI positioning data and will not have any until the next Friday release covering the 08-18
Tuesday close.** ⚠ **Context, not a trigger** — the US has no investor-type feed (protocol).
⚠ **UST 10Y at the 3rd percentile with shorts still adding, into a print that cut hike odds**, is the
single most asymmetric line on this table — recorded as an observation, **not** as a contrarian signal
(`D6`, and its scope limit from S56 applies to *share-counted*, not percentile, positioning).

---

## §R2-F · Catalyst injection (run-start requirement) — **4 binaries in the 14-day window**

`catalyst_calendar --days 14` → `CATALYST_WATCH.json`:

| When | Event | Type | Bracket status |
|---|---|---|---|
| **D-0 · 2026-08-12** | **July CPI** | 🔀binary `[bls✓]` | ✅ **S73** (2 legs) + **S72**. **FIRED; observables settle tonight** |
| **D-1 · 2026-08-13** | **July PPI** | 🔀binary `[bls✓]` | ✅ **S71** (the CPI→PPI divergence bracket) |
| **undated** | Iran *"Strait of Hormuz open"* | 🔀binary `[news👁]` | ⚠ **S8** — undated `[blank]`, **11th consecutive un-scoreable run**; **S74** now carries the named conditions |
| **D-14 · 2026-08-26** | **NVDA earnings** | 🔀binary | 🚨 **UN-BRACKETED.** RUN-1's DRIFT flagged it; it is now **inside** the calendar window |

🚨 **PREMORTEM inherits one mandatory item**: **NVDA 08-26 has no both-sides bracket**, NVDA is a held
epicenter name, and **G4 (FAIL) means the desk cannot say whether that print strikes one risk unit or
two** — `{AVGO,NVDA,TSM}` merges at 500d/750d and splits at 250d. **Registering the bracket is
PREMORTEM's job; MACRO does not register brackets (stage ownership).**

---

## §R2-G · What this addendum changes above

**Nothing above is edited.** No proposition is revised, no transmission cell moves, no verdict changes.
**It adds four carry items:**
1. **The CPI print as a `[WebSearch]`-grade dated fact**, cross-checked against FRED's June level, with
   one external yield figure explicitly rejected.
2. **`P-R2-1`** — the stale-window proposition, tagged `[inferred]`, **not citable as tilt evidence**,
   registered so it can be scored on the September release.
3. **The NFCI revision rule** — never difference this series across two runs' quotes.
4. **The two-instrument news finding** — `fts` recovered while `news_vectors.db` stayed 1.5 days stale;
   a single "news axis" verdict can hide a second staleness underneath it.

⚠ **And the standing limitation, restated last because it governs everything above**: **the binary
fired and no settled instrument covers it.** FRED has no July CPI, yfinance has no 08-12 bar, COT has
no post-print file. **S72 and S73 settle tonight, not now.**

---

# ═══ RUN-2 · §K DRIFT ADDENDUM — 2026-08-13 00:00 KST · **APPEND-ONLY** ═══

> RUN-1's DRIFT is §J above and is **not** rewritten. This is RUN-2's, appended beneath it.
> Baseline for this pass: RUN-2's own stage outputs, 22:10–23:55 KST.
> ⚠ The stage's own rule applies to itself: **the original call stays visible next to its correction.**

## §K-1 · 🚨 The tool failed. Twice. Logged, not worked around silently.

```
scripts/drift_watch.py --report llm_outputs/2026-08-12/industry_US/MACRO_REPORT.md
  → drift 질의 실패 (rc=2): 'drift' 는 원격 실행 불가(조회 전용)
     허용: [blindspot, burst, chain-hop, coverage, export, fts, search, theme-age]
```

**Retried once (the unattended-run rule), then retried a third time with `DEGAJA_NEWS_API` cleared to
force the documented local fallback — same refusal.** The shim routes through the API client
regardless of the env var, so **the local-fallback path did not engage.**

★ **Diagnosis, and it is a wiring defect with a known single source**: `drift` is **absent from
`module_news_data/__main__.DB_READ_CMDS`**, which `Server/news_api.py` imports as the **single source**
of the remote allowlist (CLAUDE.md P6). Every other subcommand this run used — `fts`, `search`,
`chain-hop`, `theme-age` — is on that list and worked. ⇒ **`drift_watch.py` is unrunnable from a
client whenever the news API is in use**, which is the normal configuration.
⚠ **This is the second consecutive run in which the DRIFT stage could not use its own tool** — RUN-1's
G1 revoked it for a different reason (dead query path). **The stage has now failed on two independent
causes in one day.** Repair is a human-approved item (rule 1); **naming it is this stage's job.**

## §K-2 · Substitute drift check, executed with allowed commands only

Kill-switch / anti-signal terms, `fts search --days 1 --count --scope foreign`:

| Term | Hits (1d) |
|---|---|
| **"Hormuz reopen"** | **33** 🚨 |
| "Strait of Hormuz open" | 1 |
| "circuit breaker" | 3 |
| "ceasefire Iran" | **0** |
| "credit spread widen" | **0** |
| "emergency Fed" | **0** |

⇒ **No credit-stress or emergency-policy burst.** ⇒ **`circuit breaker` at 3 is background**, and it
matters specifically because **S72 and S79 both carry a market-wide-halt VOID condition** — nothing
suggests one. **One term spiked, and it was read rather than counted.**

## §K-3 · ★★★ The Hormuz burst read: hopes are FADING, and the direction is the opposite of a kill

All 33 were body-read by title and source. **The cluster is unanimous in direction:**

- *"WTI Oil hits fresh highs at **$83.50** as Hormuz reopening hopes vanish"* `[fxstreet 08-11 body]`
- *"WTI jumps over **6%** as Strait of Hormuz reopening remains uncertain"* `[fxstreet 08-10 body]`
- *"Oil rises **3%** as Iran tempers hopes of Hormuz reopening"* `[cna 08-10 body]`
- *"Oil prices rise as attacks dent hopes for Strait of Hormuz reopening"* `[aljazeera 08-12 body]`
- ★ *"**IEA slashes 2026 supply forecast** as Hormuz reopening remains elusive"* `[investing_en 08-12]`
  `[google_en/Reuters 08-12]`
- *"U.S. Stocks Fall as Hopes for Strait of Hormuz Reopening Are Dashed Again"* `[wsj 08-10, title]`
- *"The Hormuz Shock Is Far From Over"* `[oilprice 08-10 body]`
- Counter-current, recorded: *"Qatar says Oman-Iran talks reach advanced stage"* `[fxstreet 08-11 body]`

⇒ **No reopening. The anti-signal (a) of S74 — "a reopening with no statement on either named
condition" — did NOT occur.** **S8 remains undated and un-scoreable for an 11th run** (human-gated, P5).

### ★★ S74 — a NEAR-MISS on branch B, and the construction question is the finding

**Dated, attributable, and corroborated in ≥2 outlet BODIES** — the grade S74 requires:
- *"**Trump demands compensation from Iran** as talks on Strait of Hormuz continue"* `[aljazeera 08-11 body]`
- *"Indian Rupee opens lower as **Trump demands war compensation**"* `[fxstreet 08-11 body]`

**S74's branch B reads: *"a formal US refusal of the two named conditions, OR a strike on a transiting
VLCC."*** The two named conditions are **(a) an end to the US naval blockade** and **(b) compensation
for war damages — demanded BY Iran FROM the US.**

⚠⚠ **This is NOT scored as a fire, and the discipline is deliberate.** A **US counter-demand for
compensation from Iran** is not, as written, *"a formal US refusal"* — it is an adjacent act that
**inverts the direction of condition (b)** rather than refusing it. **Improvising a threshold to make
this scoreable is exactly what HANDOVER §2 forbids.** ⇒ **S74 stays ARMED to 2026-08-24.**

★ **What IS recorded is a finding about the row's construction** (the S54 `D233` class): **S74's
branch B enumerates a refusal and a VLCC strike, and did not anticipate the most likely real-world
form — a symmetric counter-demand that hardens the conditions without formally refusing them.**
**A human should decide whether "conditions harden" needs a broader observable.** Registered as a dig;
**the band is not moved and the row is not re-frozen.**

## §K-4 · What the drift pass changes in RUN-2's own conclusions

**Nothing above is rewritten. Two carry items:**

1. ⚠⚠ **The tension this run must not smooth over.** RUN-2's ALPHA recorded that RUN-1's
   **`BRACKET::A_cool` (NVDA) antecedent matched** on an in-line CPI. **The same 24 hours produced WTI
   at fresh highs, an IEA supply-forecast cut, and a hardening Hormuz posture.** ⇒ **the "cool print"
   and the "hardening oil supply" readings are both live, and MACRO §R2-C's proposition `P-R2-1`
   (that the benign July headline measured a stale window) is the one this drift pass supports.**
   **The two are left standing side by side — S73 settles them tonight, not this addendum.**
2. **The correlated-tail flag is now closer, not further.** S73 registered that **S74-B raises the
   probability of S73 branch H** via energy pass-through, and that a joint fire is **one** regime flip,
   not two confirmations. **Tonight's tape moved toward S74-B without firing it.** ⚠ **Stated as an
   exposure, not a forecast.**

## §K-5 · Kill-switch coverage after this run

⚠ **RUN-1's §J-3 recorded that it ended with *zero* kill-switch coverage.** RUN-2 ends with
**partial** coverage: the term sweep above ran, but **`drift_watch` itself is unrunnable (§K-1)**, so
there is **no automated post-run watch** on the 08-12 US session — which **settles S72, S73-Leg2 and
S63 while no desk process is watching.** **That is a stated exposure, not a reassurance.**

---

## §R2-CORRECTION — appended at writeback (D48 applied to RUN-2's own output)

⚠⚠ **Two claims RUN-2 wrote are WRONG. They are left visible above and corrected here, not rewritten.**

### Correction 1 — the "same-day cross-desk dig collision" does not exist

**§R2-10 above states**: *"`D233`–`D236` is NEW and is a same-day cross-desk collision… **Both desks
allocated from one counter on the same date**,"* and the same claim was written into the
`SCENARIOS.md` MASTER INDEX addendum.

**That is false, and it was falsified by opening the file instead of trusting the tool.** The actual
rows in `handoff/RESEARCH.md`:
- the KR block registers **`D231-KR` · `D232-KR` · `D233-KR` · `D234-KR` · `D235-KR` · `D236-KR` ·
  `D237-KR`** — **every row is market-suffixed**;
- the US block registers **`D233` · `D234` · `D235` · `D236`** — unsuffixed.

⇒ **The two desks did NOT share a counter. `D233-KR` and `D233` are distinct ids and both are
correctly formed.** What actually happened is that **`handoff_id_audit` parses the `##` range header
(*"D231-KR ~ D237-KR"*) by its numerals and drops the `-KR` suffix**, so it reports a collision between
two correctly-suffixed namespaces.

★ **The defect is real but it belongs to the AUDIT TOOL, not to the desks** — and it is the more
useful finding, because a false-positive collision report is what caused this run to assert one.
⚠ **This is RUN-2 reproducing the desk's own dominant failure mode — naming the wrong object — inside
the very stage that catalogues it.** Registered as **`D240`**.

⚠ **The `M###` half of §R2-10 stands and is NOT retracted**: 153 colliding `M` ids, max **M587**, with
**M561–M572** the 08-10-rescue-vs-today overlap that RUN-1's own `§I-CORRECTION` documents, and the
**M22–M256** bulk the known 2026-07-29 split duplication. **Those are same-namespace collisions.**

### Correction 2 — the DRIFT tool failure is **not** two runs old, it is **six**

**§K-1 of the DRIFT addendum states**: *"This is the second consecutive run in which the DRIFT stage
could not use its own tool."*

**Understated, and the correct number was already in this repo.** `handoff/RESEARCH.md` carries
**`D17`** in its re-confirmed list with the annotation ***"6th run — `drift` still unrunnable."***

⇒ **RUN-2 did not discover this defect; it re-confirmed a dig that is now on its SEVENTH run.**
**The root cause named in §K-1 stands** (`drift` is absent from `module_news_data/__main__.DB_READ_CMDS`,
the single source `Server/news_api.py` imports), and **the substitute term sweep in §K-2 stands** —
what is corrected is the novelty claim and the count.

★ **Both corrections have the same shape and it is worth stating once**: RUN-2 twice treated a tool's
output as the object of study without opening the underlying file or the standing dig list.
**The instrument-check protocol exists for exactly this, and this stage failed its own rule 2**
(*"do not use the fact that a number was returned as a PASS"*).
