# BLINDSPOT_PREMORTEM — industry_US · 2026-09-07 (Mon, US Labor Day) · Stage 7 / L1·PREMORTEM ★US-only

> Four adversarial lenses argue **against this desk's own tilt** before the DEEP budget is committed.
> **P4: no sizing, no buy/sell language.**
> ⚠ **Execution constraint, declared** (standing, `RESEARCH.md`): the four lenses ran **IN-CONTEXT and
> serially**, not as a parallel adversarial agent fan-out. Each lens was run against the same fixed
> inputs (the draft tilt, the DEEP picks, `SECTOR_FLOW_US.json`, `CATALYST_WATCH.json`, `EVENT_ALPHA`)
> and each was required to return **named tickers + dated catalysts**. Stated so the method is not
> mistaken for the fan-out the stage describes.

## 0 · The binaries this stage must bracket

`CATALYST_WATCH.json` (`catalyst_calendar --days 10`) names **4**:

| binary | date | D− | already bracketed? |
|---|---|--:|---|
| **US Aug PPI** `[bls✓]` | 2026-09-10 | 3 | ✅ inside `S148` (09-14) and `S149` (09-11) windows |
| **US Aug CPI** `[bls~est]` | 2026-09-11 | 4 | ✅ `S125` · `S135` · `S142`(+ANNEX) · `S145` · `S149` · `P137` · `P138` · `P140` · **`P142`** (new today) |
| **FOMC + SEP/dot plot** `[fed✓]` | 2026-09-16 | 9 | 🚫 **outside every live window** — see §2c |
| **Iran "Strait of Hormuz open" statement** `[news👁]` | undated | — | ✅ `P126`/`P139`/`P140` all carry Hormuz-linked VOID or KPI legs |

🚨🚨 **And the calendar is incomplete. A fifth dated binary exists and the tool does not carry it.**

| **ECB rate decision** | **2026-09-10** | **3** | 🚫 **NOTHING on this desk brackets it** |
|---|---|--:|---|

Body-confirmed this run `[news — economictimes/Reuters, 09-07, read in full]`: the ECB *"is widely
expected to raise interest rates on Thursday"*; markets have *"fully priced in a 25-basis-point
increase, which would take the deposit rate to **2.5%**"*; euro-area inflation is **back above 3%**
on energy. ⇒ **`catalyst_calendar` carries no foreign central-bank dates at all**, which is the US
instance of the `D391`/`D510` structural-calendar gap. Registered as **`D562`**.
⇒ **This stage's mandatory bracket is `S152`** (§2a).

---

## LENS 1 — UNDER-COMPUTED LEGS

> *"Name the strongest bull case for a sector or sub-leg we did NOT deep-dive that has a catalyst
> ≤~5 trading days."*

ROTATION filled **2 of 4** DEEP slots for a **fourth** consecutive run (only two OW sectors exist and
padding is forbidden) and offered both empty slots here with named candidates. **This lens promotes
both — and for the first time in five runs the DEEP budget is filled.**

### 1a · **Utilities / the AI-power lane — PROMOTE-TO-DEEP**

| | |
|---|---|
| **Bull case against our own UW** | Its disqualifier has been *breadth 0.00* for six runs. **This run measured that zero and it is a filter artifact with a known cut-point**: `CEG` (flow **+0.644**, OBV **+0.188 매집**, `rs20` **+11.2**) and `VST` (**+0.619**, OBV +0.207, **Δ +0.491 = the board's largest**) are excluded from 🟢 by `vol_surge` **0.96 / 1.02** against a ~1.2 gate — *while* `PG` at flow **+0.231** and surge **0.89** is 🟢 because universe rank 34 grants it a velocity, an axis `scoring.vel_axis` declares **false** (`D561`). **The bucket's breadth number was produced by the gate, not by the tape.** |
| **Named tickers** | `CEG` · `VST` · `GEV` (flow −0.186, OBV +0.022 중립, `rs20` −4.5 — the lane's weak leg) · book-held **`ETN`** (flow **−0.662 🔴분산**, `rs20` −8.0) |
| **Dated catalysts ≤5 sessions** | **`P123` settles 2026-09-08** (AI marginal dollar: compute vs power) · **`P127` settles 2026-09-10**, window 09-03→09-10, basket `EW{VST,CEG,TLN,NRG,GEV,ETN,PWR}` − `EW{NVDA,AVGO,ANET}` · **`S146` settles 2026-09-14** (is the AI-power lane one object, or is the book holding its worst name?) |
| ⚠ **What DEEP must resolve** | `P127`'s basket contains **`TLN` and `NRG`, neither of which is in `us_top300`** — so a live row settles on names this desk cannot flow-tag. That is `D563`'s second instance and it is a *scoring* exposure, not just a measurement one |
| **Verdict** | ★ **PROMOTE-TO-DEEP (slot 3).** The reason is new this run (a measured cut-point), which is what distinguishes this from the six prior declines |

### 1b · **Information Technology — PROMOTE-TO-DEEP**

| | |
|---|---|
| **Bull case against our own N** | Routed here for a **7th** consecutive run and never resolved. This run gives it a **new** shape rather than a repeat: `exc5` **mean −0.27 but median +0.27 with 30 of 56 positive**, and `exc20` **mean −0.99 vs median −1.82** — the two cuts invert *within the sector across two windows*. **A split this wide cannot be represented by any sector-level verdict** (`W5`), which is why six declines have not converged |
| **Named tickers** | `NVDA` (−0.032, OBV −0.084) · `AVGO` (**−0.356**, OBV **−0.454 분산**, `rs20` **−15.9** — the book's weakest holding) · `ANET` (+0.047, **Δ +0.404**) · `HPE` (+0.379, surge **2.18**, **Δ −0.421**) · `DELL` (**+1.000**, the board's top flow) · `MU`/`SNDK`/`WDC` memory leg · `ORCL`/`ADBE` (both print **09-10 16:00 ET**) |
| **Dated catalysts ≤5 sessions** | **`S127` settles 2026-09-08** (`AVGO`) · **`S140` settles 2026-09-08** (does IT's repaired breadth hold?) · **`ORCL` + `ADBE` print 09-10** · **`S148` settles 09-14** (does `P101`'s SW-vs-HW inversion survive its own two biggest prints?) |
| 🚨 **The instrument fact DEEP must carry** | `catalyst_calendar`'s EARNINGS block prints **"(none in window / yfinance unavailable)"** while `ORCL` and `ADBE` both report inside the window. **An unavailability rendered as an absence** (`D540`, US instance ⇒ `D560`) |
| **Verdict** | ★ **PROMOTE-TO-DEEP (slot 4).** Seven routings without a resolution is itself the finding; the sub-node split is the question |

### 1c · Legs examined and NOT promoted — logged, not dropped

| leg | why not | disposition |
|---|---|---|
| **Materials** | `eqflow` −0.107, `exc20` median **−2.99** vs mean −0.85, **3/12** positive — the numbers support a demotion. But **`P102` settles 2026-09-09** on exactly the "is MATR two names?" question | **WITHIN-RUN-WATCH.** Promoting would pre-empt a live row (`D343`, 3rd run) |
| **Real Estate** | Board's most internally consistent bucket (**1/12** positive on `exc5`, negative on every cut) and the **longest DEEP gap on the board (7 runs, 4th consecutive time)**. But its breadth 0.00 **is evidence** — its best names miss the gate on the **non-news** axes too | **WITHIN-RUN-WATCH.** A UW sector with no live catalyst ≤5 sessions and no instrument defect to re-examine |
| **Defense / missile-defense** | Deep-dived **09-06**; the node sits at a **7.1st-percentile** 5-session extreme with **zero** narrative carriage and `S150` settles **09-14** | **WITHIN-RUN-WATCH**, already bracketed |
| **US LNG export chain** | ★ **The strongest bull case on the board and it cannot be deep-dived**: QatarEnergy force majeure **into November**, Asia spot LNG **$25.9/mmBtu = highest since 2022**, European gas at a 2023 high — and **`LNG`·`CQP`·`NFE`·`GLNG`·`FLNG`·`VG`, every gas E&P and every tanker are absent from `us_top300.csv`** | 🚨 **CANNOT PROMOTE — no measurable name exists.** Handed to ALPHA as an instrument action (universe rebuild, **P5**) and filed to the missed ledger under `N.유니버스부재` with a 09-14 recheck |

**Final DEEP set: `ENRG` · `HLTH` · `UTIL`(AI-power lane) · `IT` — 4 of 4, filled for the first time in five runs.**

---

## LENS 2 — REGIME-FLIP / BOTH-SIDES

> *"For each known binary, what is the AGAINST-US branch? What rips, which of our OWs gets hit?"*

### 2a · ★★★ `S152` — the ECB decision, 2026-09-10 (the mandatory bracket)

**The against-us branch, stated first.** This desk's tilt is a **US-domestic** rate story: `P121`'s
policy-path frame, `P142`'s Fed-hike repricing, three underweights (`RE` · `STPL` · `UTIL`) argued on
US duration. **The against-us branch is that the long-end move is EXTERNAL** — an ECB hike plus
Japan's UST selling (`EVENT_ALPHA` Card 2) plus $40tn/$1.25tn issuance (Card 6) — in which case
**the US front end can fall while the US long end keeps rising**, and every one of those three UW
verdicts is right for a reason the desk has not written down, which means its **kill conditions are
pointed at the wrong variable.**

| field | value |
|---|---|
| **Frozen observable** | **`TLT` 3-session % change**, settled closes, `auto_adjust=False`, window **2026-09-09 close → 2026-09-14 close** (the 3 settled sessions 09-10, 09-11, 09-14). ⚠ The start is **09-09** deliberately, so the ECB decision and the CPI print are **inside** the window and not in the base |
| **Branch A (AGAINST US — the long end RALLIES through the ECB hike)** | **≥ +0.913%** (trailing-252 **p85**) — a hiked-and-done ECB plus a soft CPI pulls global duration back; the `RE`/`STPL`/`UTIL` underweights lose their driver **together**, and `P142` branch B is the consistent partner |
| **Branch B (WITH US — the external supply story wins)** | **≤ −1.124%** (trailing-252 **p15**) — hawkish guidance transmits to the US long end while Japan keeps funding intervention by selling USTs; the three underweights are vindicated **on an external cause** |
| **Branch C** | between = the disclosed favourite |
| **`D93` executed BEFORE freezing** | trailing 252 of `TLT` 3-session % change: p05 **−1.651** · **p15 −1.124** · p50 **−0.081** · **p85 +0.913** · p95 +1.468 ⇒ A ≈15% · B ≈15% · C ≈70% |
| **State at registration** | **+0.415% = the 67.1st percentile** (09-04 settled, close 82.21) — ★ **inside C and genuinely mid-pack.** ⇒ **both branches carry information**, which is *not* true of `P142` (registration already above A) or `P143` (already above p95). **This is the only balanced bracket the desk registered today and that is stated as its main virtue** |
| **Implied move, and why it does NOT set the threshold** | `module_flow TLT --positioning`: **예상변동 ±0.7%, expiry 2026-09-09, D2.** 🚫 **The straddle expires 09-09 — BEFORE the window opens.** Borrowing a proxy straddle that expires early is the scope error `M1305` made and `M1326` corrected, so the thresholds come from `D93` on the observable itself and the straddle is recorded as **not covering the event** rather than quietly used |
| **Branch information grading (`B4`, before the event)** | **A is the falsifier and B is the confirmer.** B leaves every standing verdict where it is; **A breaks three of them at once**. ⇒ **A is the informative branch**, disclosed at registration |
| **Anti-signal (VOID)** | an **unscheduled ECB action or emergency statement**, a **BLS delay/restatement of the August CPI**, or **`hy_oas` ≥ 3.10% on a close** inside the window (then it is a credit event and the rate attribution is void) |
| **Non-redundancy (`D343`)** | `P142` is the **US front end** (`DGS2`, rate of change) · `P143` is the **yen** (`FXY`) · `P128` is **US credit** (`hy_oas`) · `P124` is the **dollar** (`DTWEXBGS`) · `S135` is the **equity** UW basket. **No row measures the US LONG end**, which is the tenor the external-supply story hits first (`DGS30` 96.0th pctile, `DGS10` 98.8th) |
| **Owner** | `industry_US` |

### 2b · Binaries examined and deliberately NOT bracketed (`B4`), each with its reason

| binary | why no new bracket |
|---|---|
| **`ORCL` + `ADBE` prints, 09-10** | 🚫 **No-information by measurement, 2nd consecutive run.** `module_flow --positioning` this run: `ORCL` **예상변동 ±11.8%** (expiry 09-11, D4), `ADBE` **±8.1%** (09-11, D4) — against an observable whose `D93` p85/p15 vs `SMH` are **+3.15 / −3.66**. **A threshold inside the implied move is pre-declared no-information**, which is exactly what `S132`/`S138` measured (`D503`). ⚠ And `S148` already owns the pair's real question, settling 09-14 with both prints inside its window |
| **US Aug PPI, 09-10 (standalone)** | Already inside `S148` and `S149` windows. A standalone row would be a second observation of one event |
| **US Aug CPI, 09-11 (standalone)** | Bracketed from **nine** directions already (§0). A tenth adds width, not information (`D503`) |
| **FOMC + SEP, 09-16** | 🚫 **Deferred for a SECOND consecutive run — and this time with a dated commitment instead of an open deferral.** Reason unchanged and still valid: every branch line would come from a `D93` computed on a **frozen tape** (`asof` 2026-09-04, third run) and the 09-11 COT does not exist yet. ⚠ **But deferring twice starts to look like avoidance, so the commitment is written down: the row must be registered by the 2026-09-11 run at the latest**, because after the CPI prints the pre-print information is in the base and the bracket loses the thing it exists to capture. Filed as **`D564`** so the next run inherits the deadline rather than the excuse |
| **KOSPI200 quadruple witching, 09-10** | 🚫 **Out of scope for `--market us`** (`W1`). `D533` stays open and needs a human or a KR protocol change (**P5**), for a second run |
| **S&P rebalance, 09-18** | Structural, not directional; `P124` already settles that date |

### 2c · The correlated-underweight pattern — checked, and it is now **four** legs, not three

The stage's own field note warns about *"two UW sectors that are one bet in disguise."* Measured today:

| bucket | verdict | `eqflow` | `exc5` breadth | the shared driver |
|---|---|--:|--:|---|
| Real Estate | UW | −0.124 | **1/12** | US long-end rates |
| Consumer Staples | UW | −0.098 | 7/19 | US long-end rates (bond-proxy) |
| Utilities | UW | **+0.050** | 7/15 | US long-end rates — **and its flow disagrees with its verdict** |
| **Financials** | **N** | −0.023 | 26/47 | 🚨 **the same rates axis, in the opposite direction** |

⇒ **`D512` reproduces, and this run adds the fourth leg by naming the sign**: `RE`/`STPL`/`UTIL` are
short duration and `FIN` is long it. **`S152` branch A hits all four at once** — three lose their
driver and the fourth loses its NIM story — which is precisely why A is graded the informative branch.
⚠ **`S135` (settles 09-11) equal-weights `UTIL`+`RE`+`STPL` as one bet**, and `M1372` already records
that it averages **one measured bucket with one mis-measured one** (Utilities' breadth is an artifact,
Real Estate's is evidence). **Construction note carried on a live row; thresholds unchanged** (`D242`).

---

## LENS 3 — MOMENTUM-CONTINUATION ("already ran" ≠ avoid)

> Re-tag each runner **EXTENDED-BUT-LIVE** vs **EXHAUSTED**, with the flip condition.
> ★ **Normalized by each name's own 20-day volatility first** (`B3`) — a raw % move is not a z.

| name | 20d move | daily σ(20d) | **z = move / (σ·√20)** | chart read (`module_chart --read`) | sweep OBV | re-tag |
|---|--:|--:|--:|---|---|---|
| **`MPC`** (held) | +30.4% | 2.08% | ★★ **+3.27 — the board's true outlier** | **CONFIRMED-TURN** · OBV **누적 +52%** · **no divergence** · RSI 76.0 · bullish stack 4/4 MA · coiling 18.9% | +0.621 매집 | ★ **EXTENDED-BUT-LIVE** |
| **`PSX`** (held) | +25.1% | 1.82% | ★★ **+3.08** | **CONFIRMED-TURN** · OBV 누적 +58% · 🚨 **BEARISH DIVERGENCE** (price HH, RSI LH) · RSI 68.6 | +0.434 매집 | ⚠ **EXTENDED-BUT-LIVE, WITH A DIVERGENCE ITS TWIN DOES NOT HAVE** |
| **`MSTR`** | **+42.8%** | **6.27%** | 🚨 **+1.53 — the LOWEST z of the three biggest raw runners** | NEUTRAL/CHOP · OBV **중립 +2%** · Bollinger **expanding 60.9%** · RSI 71.2 | +0.326 매집 | **EXHAUSTED** (unchanged from 09-06) |
| **`HOOD`** | +30.9% | 5.40% | +1.28 | CONFIRMED-TURN · OBV 누적 +80% · bearish divergence · band **expanding 35.7%** | +0.211 매집 | **EXTENDED-BUT-LIVE**, low conviction |
| **`SLB`** | +13.8% | 2.40% | +1.29 | CONFIRMED-TURN · OBV **누적 +87%** · **no divergence** · only 3/4 MA | +0.439 매집 | **EXTENDED-BUT-LIVE** |
| **`CVX`** | +11.8% | **1.34%** | **+1.97** | — | +0.371 매집 | **EXTENDED-BUT-LIVE** ⚠ its 🟢 tag is a `D561` artifact and is not citable |
| **`COP`** | +14.2% | 1.70% | +1.86 | — | +0.222 매집 | **EXTENDED-BUT-LIVE** |
| **`DELL`** | +15.5% | 4.96% | **+0.70 — the least exceptional on the board** | CONFIRMED-TURN · OBV **누적 +128%** · bearish divergence · RSI **59.0** | +0.252 매집 | **EXTENDED-BUT-LIVE**, and the flow rank-1 overstates it |
| **`NEM`** | +13.4% | 2.94% | +1.02 | NEUTRAL/CHOP · OBV **분배 −58%** · bearish divergence | +0.144 **매집** | 🚨 **`C25` OUTRIGHT DISAGREEMENT reproduced** — no re-tag issued |

★★ **The lens's finding, and it inverts a carried framing.** The 09-06 run recorded `MSTR` as
*"the board's largest 20-day momentum (+46.7%)"* and treated it as the extreme case.
**Volatility-normalized it is the least extreme of the three: +1.53 z against `MPC`'s +3.27 and
`PSX`'s +3.08.** The genuine outliers are the two **held refiners**, and `MPC` is the only name on
the board that is **>3 z with no divergence and OBV accumulating on both instruments**.
⇒ *"already ran"* was being applied to the wrong names.

**Flip conditions (registered, not narrative).** **RULE D6 exempt** — these are *flip conditions on an already-issued composite tag*, not propositions resting on OBV; each requires OBV **plus** a second axis (a divergence, a band state, or a settle) before it fires:
- `MPC` **EXTENDED-BUT-LIVE → EXHAUSTED** if a bearish RSI divergence appears **or** OBV 20d slope
  turns negative. Tracked by `P140`, settles **09-11**.
- `PSX` → **EXHAUSTED** if its existing divergence is confirmed by an OBV slope turn (it has the
  divergence already; only the second leg is missing).
- `MSTR` **EXHAUSTED → LIVE** if OBV 20d slope exceeds +20% **and** the Bollinger expansion contracts.
- `NEM` — **no tag issued until the two instruments agree** (`C25`). Not "neutral"; **unresolved.**

---

## LENS 4 — CYCLE-EXPOSURE (registry vs coverage vs the REAL book)

`cycle_exposure --json` against the real KIS book (read-only):

| cycle | rank | epicenter % | need ≥ | held epicenter | GAP |
|---|--:|--:|--:|---|---|
| AI-compute / semiconductors | 1 | **17.51%** | 12.0% | `NVDA` · `ANET` | ✅ |
| Energy / oil-refining | 2 | **10.49%** | 8.0% | `MPC` · `PSX` | ✅ |
| Missile-defense / rearmament | 3 | 3.65% | 🚨 **no bar set** | `RTX` | ⚪ **n/a by construction** |

**✅ No top-rank GAP.** The book holds a core in every rank ≤2 cycle's epicenter.

🚨 **Three findings the GAP flag cannot produce:**

1. **The rank-3 cycle has no bar, so the check is silent on it** — `M1374`, reproduced — **at the
   exact moment its node prints a 7.1st-percentile 5-session extreme with zero narrative carriage**
   and the book holds **its worst name** (`RTX` flow −0.789, OBV −0.294 분산, `rs20` −9.6).
   `S150` settles **09-14**. **A silent check is not a pass.**
2. ★★ **A cycle the registry does not contain cannot be flagged, and this run found one with a
   dated, body-confirmed catalyst**: the Hormuz LNG chain (force majeure into November, Asia spot at
   a 2022 high). **Epicenter exposure: 0%. Measurable epicenter names: 0.** ⇒ **`D563`** — *the
   universe is built from index membership ∪ current holdings, so a cycle the desk does not already
   own is a cycle it cannot measure; the exposure gap and the measurement gap are the same gap.*
   The rule that *"a 🔴 tape gates ADD timing, it never justifies zero core"* **cannot even be
   applied here, because there is no tape to read.**
3. **The epicenter-vs-one-layer-off audit finds one layer mislabelled.** `risk_units --book` merges
   **`ANET`+`ETN` into ONE unit at 500d and 750d**, spanning two book theme labels
   (`AI-compute-EPICENTER` + `AI-power/electrical`). ⇒ **`cycle_exposure` counts AI-compute at 17.51%
   using `NVDA`+`ANET`, while the 500d/750d measurement says `ANET` is partly the power lane.**
   ⚠ Concentration must carry its `--days`: **12 units at 250d / 11 at 500d / 10 at 750d.**

**Cleanest epicenter expressions, named as the lens requires** (measurement subjects, not
recommendations): AI-compute — `NVDA`, `AVGO`, `ANET`, `DELL`; Energy/refining — `MPC`, `PSX`,
`VLO` (**the un-held leg of a three-name node whose other two are held**); AI-power — `CEG`, `VST`,
`GEV`, `ETN`; **Hormuz LNG — none available.**

---

## 5 · Synthesis — what this stage injects downstream

| output | destination |
|---|---|
| **DEEP set updated: `ENRG` · `HLTH` · **`UTIL`/AI-power** · **`IT`** — 4 of 4** (two promotions) | **DEEP (stage 8)** |
| **`S152`** — ECB 09-10 both-sides bracket, `TLT` 3-session, A ≥ +0.913% / B ≤ −1.124%, settle **09-14** | `SCENARIOS_US.md` + `SCENARIOS.md` master index + **ALPHA's action bracket** |
| **`D562`** `catalyst_calendar` carries no foreign central-bank dates · **`D563`** un-owned cycles are unmeasurable · **`D564`** the FOMC bracket has a 09-11 deadline | `RESEARCH.md` Part C |
| **Momentum re-tags** with volatility-normalized z and explicit flip conditions; `NEM` left **unresolved** rather than tagged | **BET** |
| **Cycle GAP: none by the flag; three findings the flag cannot produce** | **BET** (epicenter starter) + **ALPHA** |
| **Correlated-underweight pattern now measured at FOUR legs with signs** (`RE`/`STPL`/`UTIL` short duration, `FIN` long it) | **BET** · construction note on `S135` |

★ **Did all four lenses agree with the draft?** **No — and two of them moved it.** Lens 1 promoted
two sectors the deterministic stages could not slot, and Lens 3 **inverted** the carried momentum
ranking. Lens 2 found a binary the desk's own calendar does not contain. Lens 4 found a cycle the
desk cannot measure. **The default expectation held.**

---

## ✅ EXIT CHECK — PREMORTEM

- [x] **4 lenses run**, each returning named tickers + dated catalysts. ⚠ **Execution mode declared**: in-context and serial, not a parallel agent fan-out.
- [x] **Every bracket names its observable + frozen threshold + date and has BOTH branches** — `S152` is the only registration and it is two-sided. **Zero one-way brackets.**
- [x] **Every magnitude threshold stated against the implied move** — `TLT` **±0.7% expiring 09-09, before the window opens** ⇒ declared **not covering**, thresholds taken from `D93`; `ORCL` **±11.8%** and `ADBE` **±8.1%** ⇒ both **pre-declared no-information** and not bracketed.
- [x] **Each branch graded by information content before the event** — `S152` A is the falsifier (breaks three verdicts), B the confirmer; and the balanced 67.1st-percentile registration state is stated as the reason both branches carry information, in contrast to `P142`/`P143`.
- [x] **Binaries where no branch would change the conclusion were dropped with the reason stated** — `ORCL`/`ADBE`, standalone PPI, standalone CPI, S&P rebalance.
- [x] `BLINDSPOT_PREMORTEM.md` written — legs · brackets · re-tags · cycle GAP.
- [x] **Every catalyst-bearing leg promoted or logged** — 2 promoted, 4 logged as WITHIN-RUN-WATCH with reasons, 1 (LNG chain) declared un-promotable with the instrument cause and filed to the missed ledger.
- [x] **DEEP set updated and stated: `ENRG` · `HLTH` · `UTIL` · `IT` = 4 of 4.**
- [x] **`S152` registered in `handoff/SCENARIOS_US.md` and indexed in the `SCENARIOS.md` spine** (written inside this stage, per the 09-05/09-06 precedent).

---

> P4 — analytical only. No sizing, no buy/sell language. Tickers are measurement subjects.
