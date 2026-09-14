# BLINDSPOT_PREMORTEM — industry_US · 2026-09-01 (Tue) · Stage 7 / L1·PREMORTEM ★US-only

> Four adversarial lenses argue **AGAINST our own tilt** before the deep budget is committed.
> Draft tilt under attack: `ENRG OW · HLTH OW · MATR OW · COMM OW− · FIN N (demoted today) · IT N ·
> STPL N · DISC UW · INDU UW− · RE UW · UTIL UW`; DEEP = continuous `[MATR, HLTH]` · rotating
> `[ENRG, COMM]`.

## §0 · Declared execution constraint (standing, 7th run)
⚠ **The four lenses ran IN-CONTEXT and serially, not as a parallel adversarial agent fan-out.**
This is a standing session constraint and it is declared, not hidden: **the adversarial construction
is preserved (each lens is run against the draft tilt with its own falsifying mandate), the
*diversity* of an independent fan-out is not.** Same declaration as the 08-21 → 08-31 runs.

## §0b · Instrument state
All flow numbers from `SECTOR_FLOW_US_REPAIRED.json` (3-axis `nonews`, 299 scored, **asof 08-31**) —
the primary file's OBV axis is revoked. **No lens cites news velocity or theme freshness from the
sweep** (`vel_coverage` 16.05%, axis dead, cause = the pipe).
⚠ **`module_flow --positioning` was run at ~10:2x ET with the NYSE OPEN** ⇒ its price axes are on a
**live partial bar** and are labelled as such; the settled values from the repaired sweep govern.

---

## Lens 1 · UNDER-COMPUTED LEGS — what has a catalyst ≤5 trading days and no DEEP slot

| leg | catalyst | strongest bull case AGAINST our tilt | verdict |
|---|---|---|---|
| ★★★ **Information Technology / semis** | **`AVGO` earnings D-1 (2026-09-02)** ⚠ `D420` unresolved — the issuer calendar says **09-03**, `catalyst_calendar` says **09-02** | **A settled bracket fired against the desk here this run.** `S124` **FIRED-A at 41 of 56** names with positive 5-session excess vs `SPY`, from a registration state of **13 of 56 = the 5.6th percentile of two years** — and 41 is **above** the trailing-252 **p85 (39)**. Tape agrees: `XLK` `exc5` **+3.11pp** and `exc20` **+3.51pp vs `SPY`**, the 2nd-best on the board on both. ★ **And the bar that killed the last three IT promotions is gone** — IT is **no longer a `top1_flips_sign` bucket** (`NVDA` 19.4%, +0.048 → +0.001, sign held). ROTATION still declined it, correctly, because `eqflow` **−0.014** is negative and the pro-case is a *return* measurement — **but that is exactly the shape of a leg the deterministic desk cannot promote and a pre-mortem must interrogate** | ★ **PROMOTE-TO-DEEP — 5th slot** |
| **Industrials** | **August NFP D-3 (2026-09-04)** | `XLI` `exc20` **−5.62pp vs `SPY`** is the board's 2nd-worst and `INDU` is `UW−`; the against-us branch is a hot payroll that reads as cycle strength rather than as rate pressure. ⚠ **Already bracketed both ways** — `S126` (five sessions **into** the print) and `P114` (five sessions **out of** it). A DEEP would not add an observation | **WITHIN-RUN-WATCH** — logged, not dropped |
| **Financials** | **`S134` settles 2026-09-04** | Demoted `OW− → N` **today**, and the tape still disagrees with the flow (`XLF` `exc2` **+0.23pp vs `SPY`**, the board's 3rd-best 2-session). If `S134` fires **A** (`exc5 ≥ +2.00pp`) the demotion was wrong within four days | **WITHIN-RUN-WATCH** — the bracket already exists and settles inside the window |
| **Utilities** | none dated ≤5d | ★ The against-us case is now **named**: if the AI-power leg is real, `UTIL` is the bucket that owns it — and `UTIL` has the **longest recency gap on the board (7 runs)** and is structurally unreachable by ROTATION's selection rule. ⚠ But **EVENT_ALPHA Card 5 supplies a dated falsifier** (Texas halted data-center power; "ghost demand") **and the tape agrees with the falsifier**: every measurable AI-power name is 🟡 or 🔴, **none is 🟢** | **WITHIN-RUN-WATCH** with a dated re-check **2026-09-08** (`P123`) |

**Nothing was silently dropped.** One promotion, three logged watches.

---

## Lens 2 · REGIME-FLIP / BOTH-SIDES — every binary in `CATALYST_WATCH`, with the against-us branch

### 2a. `AVGO` earnings, D-1 — ★ the existing bracket has gone NO-INFORMATION and is not re-banded

**`M1197` [measured].** `module_flow AVGO --positioning` reads **예상변동 ±9.6% (expiry 2026-09-02,
D1)**. **`S132`'s frozen threshold is ±9.00pp**, derived at registration from a **±8.11%** straddle.
⇒ **`S132` now sits INSIDE the implied move and is pre-declared NO-INFORMATION.**
🚫 **The threshold is NOT moved** (`D242`). This is the `S103` → `S115` precedent: write a **new row
outside** the priced move rather than re-band the old one.

Positioning at the same read (⚠ **live partial bar**): options **P/C 1.73** (put-heavy = fear),
**IV skew −3.3**, short interest **1.2% of float, covering, DTC 3.0**, news velocity **1.33× accelerating**.
Settled flow (repaired, 08-31): `AVGO` **−0.616 🔴분산**, OBV **−0.133**, `rs20` **−6.8**,
`rs60` **−12.9 vs `SPY`**. **`AVGO` is held.**

**The against-us branch, named:** a **beat** rips the semi complex while the desk holds `IT` at `N`
and **declined to promote it today**. What rips: `AVGO`(held) · `MRVL`(`rs60` −34.4, `rs20` **+8.0** —
already turning) · `AMAT`(−0.889, the board's worst) · `NXPI`(−31.6) · `ARM`(−39.8) · `ON`(−45.1) —
i.e. **the deepest-discounted half of IT**, none of which the book owns.
**Which of our OWs gets hit:** none directly; **the cost is opportunity, not drawdown**, which is why
it is a pre-mortem item rather than a risk item.
**Trigger** `AVGO` 1-session excess ≥ +11.00pp vs `SPY`. **Invalidation** a miss with `rs60` making a
new low.

⇒ **REGISTER `S138`** (below), threshold **outside** the ±9.6% priced move.

### 2b. August NFP, D-3 — the correlated-UW pattern, and it just PAID

⚠ **Field note applied.** `UTIL` + `RE` + `STPL` are three underweights that are **one bet**
("long duration"), and this is no longer a hypothesis: **`S112` FIRED-B today** — `EW{XLU, XLRE, XLP}`
3-session excess **−2.331pp vs `SPY`** against a −1.757 threshold. **The pattern is real and it paid.**
⇒ **the desk's three UW labels are one position**, which is a concentration fact for BET, and
**`S135` (settles 09-11) already asks exactly this question** — no second row is registered for it.

**The against-us branch:** a **cold** payroll collapses September hike odds and the same three rip
**together**, giving back the −2.331pp in one session. `S112` has scored and is no longer armed ⇒
**the correlated-UW exposure is currently unbracketed across the NFP window.**
⇒ **REGISTER `S139`** (below), re-arming the identical observable across 09-04.

### 2c. Iran / Strait of Hormuz, undated — the replacement bracket, CHECKED not assumed

`S92` **scored `FIRED-A` today** and is no longer armed. HANDOVER §8 flagged that the oil axis would
lose its bracket. **Checked:** `P122` was registered at MACRO this run — both-sided
(**A** `CL=F` ≥ 88.00 **and** WTI spec ≥ 65th %ile at `[COT 09-08]` · **B** `CL=F` ≤ 80.00 · C between),
`D93`-banded off a 30-day realised range of 81.25–87.83, with a **roll anti-signal whose base rate is
explicitly raised** because `R116` was retracted on a roll artifact one run ago. `P107` · `P112` ·
`P117` remain armed on the same axis. ⇒ **the axis is covered; no new row.**
⚠ **The against-us branch is stated**: `CL=F` ≤ 80.00 would take **Energy** — the desk's most-confirmed
OW, rank 1 on both flow axes with both of the universe's only two `new_green` ignitions — down
first and hardest. The named bear leg is the **Venezuela** cluster (15 outlets, `theme-age` **2.74×
ACCELERATING**).

### 2d. Binaries deliberately NOT bracketed, with the reason (information-content rule)
- **MSCI 08-31** — scored today (`S131`, `C`), out of the window.
- **`AAPL` succession / the 09-0x product event** — a 21-outlet BUILDING thread, but **neither branch
  changes a sector verdict**: `AAPL` is not held and IT's verdict turns on breadth, not one name.
  Filed as a dig in EVENT_ALPHA, not bracketed.
- **California wildfire legislation** — a dated single-state regulatory event that **explains** part
  of `XLU` −2.20% but does not carry the `UTIL UW` thesis. A bracket would measure the news.

---

## Lens 3 · MOMENTUM-CONTINUATION — "already ran" is not a verdict. Re-tag every runner.

Ranked on `rs60 vs SPY` (repaired sweep, settled 08-31). ⚠ **`D48`/B3**: a date-clustered move is
**n≈1**, not n=N — the Energy names below moved on one session and are counted as one observation.

| name | `rs60` / `rs20` vs `SPY` | OBV · surge | re-tag | flip condition |
|---|---|---|---|---|
| **`DASH`** | **+43.5** / +14.3 | **OBV +0.603 — the highest in the top-15** · 0.84 | ★ **EXTENDED-BUT-LIVE** | OBV → 분산. ⚠ **It sits inside our `DISC` UW**, and the UW is barred from deepening because `AMZN` owns the sign. **The single clearest "already ran ≠ avoid" case on the board** |
| **`MPC`** (held) | **+38.5** / +20.4 | OBV **+0.427** (2nd-highest board-wide) · 1.08 | **EXTENDED-BUT-LIVE** | OBV → 분산, or `CL=F` ≤ 80.00 (`P122`-B). ⚠ short-volume **z +2.90 🔴** — shorts pressing **into** the rally |
| **`VLO`** · **`PSX`**(held) | +37.3 / +15.5 · **+32.6** / +18.4 | OBV +0.224 · +0.183, 매집 both | **EXTENDED-BUT-LIVE** | same |
| **`ABNB`** | **+35.7** / +20.4 | OBV +0.227 · **1.10** | **EXTENDED-BUT-LIVE** | ⚠ also inside `DISC` UW; missed the 🟢 tag by 0.10 of surge |
| **`CRM`** | +35.1 / **+37.3** | OBV +0.326 · **1.90 — highest on the board** | **EXTENDED-BUT-LIVE, top-risk flagged** | ⚠ `rs20 ≈ rs60` ⇒ **the entire 60-day move is the last 20 days.** OBV and surge both support it now; a surge fall below 1.0 with OBV flat is the exhaustion tell |
| **`PLTR`** | +30.2 / **+47.1** | OBV +0.220 · 0.68 | ⚠ **EXHAUSTION GEOMETRY** | **`rs20` (+47.1) EXCEEDS `rs60` (+30.2)** ⇒ days 21–60 were **negative**; the whole run is one 20-day leg, on a **surge of 0.68**. This is the `M149`/`M779` shape the desk has logged before |
| **`PANW`** | +35.5 / +8.8 | **OBV −0.101** · 0.95 | **EXHAUSTED** | OBV already negative under a top-5 `rs60`. Re-tag to LIVE only if OBV turns 매집 |
| **`CMG`** | +33.6 / **+0.3** | OBV −0.060 · 0.66, flow **−0.301** | **EXHAUSTED** | the 60-day rank is a fossil; the 20-day is dead flat and flow is negative |
| **`APP`** | **−45.5** / −24.4 | OBV −0.288, **−0.806 🔴** | **not a runner — the board's worst** | listed so the lens is not read as bull-only |

★ **`M1198` [measured] — the two cleanest EXTENDED-BUT-LIVE names in the entire universe
(`DASH` +43.5 and `ABNB` +35.7, both OBV-accumulating) sit inside a sector the desk holds at `UW`**,
and ROTATION is **barred** from deepening that UW because `AMZN` owns 40.2% of its cap weight. ⇒ the
label and the money point opposite ways inside one bucket, for a **third consecutive run**
(08-30 and 08-31 logged the same pair). **Handed to BET as a name-level question, not a sector one.**

---

## Lens 4 · CYCLE-EXPOSURE — registry vs coverage vs the REAL book

`cycle_exposure.py` (real KIS book, total ≈$11,012 · invested $5,171):

| cycle | rank | epicenter % | need ≥ | any-layer % | held | GAP |
|---|---:|---:|---:|---:|---|---|
| AI-compute / semiconductors | 1 | **16.85%** | 12.0% | 20.44% | `NVDA`, `ANET` | ✅ |
| Energy / oil-refining | 2 | **10.28%** | 8.0% | 10.28% | `MPC`, `PSX` | ✅ |
| Missile-defense / rearmament | 3 | 3.77% | — | 3.77% | `RTX` | ⚪ no threshold set |

**✅ No top-rank cycle GAP** — third consecutive run.

🚨 **But two cycles cannot be measured at all, and the gap is now costing live questions:**
- **AI-power / grid** — `D416`, still no ranked registry row ⇒ **"the book has 0% AI-power exposure"
  is UNSTATABLE, not measured as zero.** ★ This run it stopped being academic: `P123` (registered at
  MACRO) and EVENT_ALPHA Card 5 (Texas halt / "ghost demand") are a **live both-sided question about a
  cycle the registry cannot see**, and the tape says **every measurable power name is 🟡 or 🔴 — none
  is 🟢** (`ETN` −0.339 Δ −0.687 · `VRT` −0.215 Δ −0.687 · `NEE` −0.254 · `CEG` −0.396 ·
  `VST` −0.767🔴 · `PWR` −0.597🔴 · `FIX` −0.783🔴 · `DUK` −0.672🔴 · `SO` −0.597🔴).
  ⚠ **`ETN` is held** and its thesis rides this layer.
- **Optical / interconnect** — `D250`, **17th run** with no registry row. ★ **Now bracketed directly
  by `S137`** (settles 09-09), which does not need the registry — but EVENT_ALPHA Card 6 measured
  that `S137`'s two legs have **separated** (`LITE` OBV **+0.284 매집**, `rs20` +16.1 vs `COHR`
  `rs60` **−35.5**, **Δ −0.805 = the worst in the 299-name universe**). An equal-weight basket of a
  diverging pair averages two different stories; **the row is not re-banded, the divergence is
  disclosed** (`D458`).

**Cleanest epicenter expressions, named** (P4 — analytical, no sizing, no recommendation):
- AI-compute epicenter: `NVDA`, `ANET` — **both held**; `NVDA` OBV **−0.098** with `vol_surge` **1.39**
  (the crowded-layer shape).
- Energy epicenter: `MPC`, `PSX` — **both held**; and **`SLB` + `WMB`, the universe's ONLY two
  `new_green` ignitions, are NOT held.**
- Memory (EVENT_ALPHA Card 1): `MU`, `SNDK` — **neither held**; `WDC` explicitly excluded (−0.861 🔴).

---

## §5 · Brackets registered this stage — both-sided, thresholds frozen, implied move stated

> ⚠ **ID 3-grep at WRITE time** across `handoff/*.md` · `llm_outputs/**` · `REPORT/**` via
> `module_evidence next-id S` — highest existing **`S137`**; **`S138`–`S140`** issued. IDs allocated
> against **every** existing row in **both** `SCENARIOS*.md` files (`D76` collision class).

### `S138` — ★★★ `AVGO`: a threshold that is actually outside the priced move
| field | value |
|---|---|
| **Event** | `AVGO` FQ3 earnings, **2026-09-02** per `catalyst_calendar` ⚠ **`D420` unresolved** — the issuer calendar says **09-03**. **The row settles on the observable, not the date**: the first settled close after the print |
| **Frozen observable** | **`AVGO` 1-session excess vs `SPY`**, settled closes, first settled session after the print, each vs its own prior close |
| **Implied move at registration** | **±9.6%** — `module_flow AVGO --positioning`, expiry **2026-09-02 (D1)**. ⚠ Read with its `D±n`: the straddle covers the path to expiry, not the event alone |
| **A (the discount was wrong)** | excess **≥ +11.00pp** — **outside** the ±9.6% priced move ⇒ `rs60` **−12.9 vs `SPY`** was a discount, not a franchise loss, and the deepest-discounted half of IT (`MRVL` `rs60` −34.4 with `rs20` **+8.0** already turning, `AMAT`, `NXPI`, `ARM`, `ON`) re-rates with it — **none of which the book owns** |
| **B (the discount was right)** | excess **≤ −11.00pp** ⇒ the franchise loss is real and **the AI-compute epicenter is narrower than the book's three names assume** |
| **C** | between — **disclosed favourite, and disclosed as LARGE**: the band spans 22pp against a 9.6% priced move. **Stated rather than tightened** |
| **Information grade (B4)** | **HIGH on both.** A falsifies ROTATION's `IT N` hold *and* `S116`'s B-leaning read that `MRVL` took the socket; B falsifies the epicenter's breadth. ⚠ **C is likely** and that is the honest cost of putting the threshold outside the priced move |
| **Relationship to `S132`/`S127`** (`D343`) | 🚫 **`S132` is NOT re-banded and NOT voided** — it settles on its own ±9.00pp and is **pre-declared no-information** because that now sits inside the ±9.6% straddle (`M1197`). `S127` (09-08) observes a different window. **This row exists solely because it is the only one of the three with a threshold outside the priced move** — the `S103` → `S115` precedent |
| **Anti-signal (VOID)** | a **guidance withdrawal, M&A announcement, or export-control action** at `AVGO` inside the window — none of which would be the print. ⚠ Base rate: low but **not** remote given the export-control tape |
| **Positioning disclosed at registration** | options **P/C 1.73**, IV skew **−3.3**, short **1.2% float covering, DTC 3.0**, news velocity **1.33× accelerating** ⚠ **live partial bar**; settled flow (08-31) `−0.616 🔴분산`, OBV −0.133 |
| **Owner** | `industry_US` · **settles first settled close after the print (2026-09-03 or 09-04)** |

### `S139` — ★★ Re-arming the correlated-underweight bracket across the NFP
| field | value |
|---|---|
| **Why it exists** | `S112` **FIRED-B today** on exactly this basket (−2.331pp vs a −1.757 threshold) ⇒ **the correlated-UW pattern is measured, not hypothetical**, and it has now **scored and disarmed**, leaving three of the desk's underweights unbracketed across a dated macro binary |
| **Frozen observable** | **`EW{XLU, XLRE, XLP}` 3-session excess vs `SPY`**, settled closes, **2026-09-01 close → 2026-09-04 close** (August NFP prints that morning) |
| **A (AGAINST US)** | **≥ +1.653pp** (trailing-252 **p85**) — the three underweights rip **together** on a cold payroll; the correlated-UW position gives back its `S112` gain in one window |
| **B (with us)** | **≤ −1.757pp** (trailing-252 **p15**) — a hot payroll extends the duration repricing and the same basket pays twice |
| **C** | between — the disclosed favourite |
| **`D93` before freezing** | **Identical distribution to `S112`**, reused deliberately rather than re-derived: trailing 252 mean −0.156 · sd 1.754 · p05 −2.893 · **p15 −1.757** · p50 −0.168 · **p85 +1.653** · p95 +2.719 ⇒ **A ≈15% · B ≈15% · C ≈70%** |
| **State at registration** | the same basket **just delivered −2.331pp**, i.e. it starts **below p05** ⇒ ⚠ **B is the low-information branch here (mean reversion alone could produce a C), and A is the informative one** — the reverse of `S112`'s balanced start, and it is disclosed |
| **Implied move** | ⚠ **No straddle prices an equal-weight three-ETF basket.** Stated as unavailable rather than invented (`D2`) |
| **Anti-signal (VOID)** | a **BLS delay or methodology restatement** of the August payroll release |
| **Relationship to `S135`** (`D343`) | `S135` (09-11) asks whether these three are **one verdict or three**; this row asks how the **one bet** behaves across a dated binary. Different objects; the correlation is named here in advance |
| **Owner** | `industry_US` · **settles 2026-09-04** |

### `S140` — ★★★ Does IT's repaired breadth HOLD, or was 41-of-56 one week?
| field | value |
|---|---|
| **Why it exists** | `S124` **FIRED-A at 41 of 56** today, above the trailing-252 **p85 (39)**, from a registration state of **13 of 56 (5.6th percentile)**. ROTATION declined to promote `IT` because the pro-case is a **return** measurement and `eqflow` is **−0.014**. ★ **The desk therefore holds a verdict that its own settled bracket just argued against, and nothing re-tests it** |
| **Frozen observable** | **COUNT of `us_top300` Information Technology names (n=56) with a positive 5-session excess vs `SPY`**, settled closes, at the **2026-09-08** close — the identical construction `S124` used |
| **A (the repair is structural)** | **≥ 39** (trailing-252 p85) — breadth holds at an extreme through the `AVGO` print ⇒ `IT N` is wrong and ROTATION's `eqflow`-based decline was measuring participation while the money was measuring price |
| **B (it was one week)** | **≤ 20** (trailing-252 p15) ⇒ the 41 was a post-print bounce and the sweep's `eqflow` −0.014 / 3🟢-vs-9🔴 was the better instrument |
| **C** | 21–38 — **disclosed favourite** |
| **`D93` before freezing** | trailing 252 of the same count: mean **29.5** · sd **9.0** · p05 **13** · **p15 20** · p50 **30** · **p85 39** · p95 **43** ⇒ **A ≈15% · B ≈15% · C ≈70%** |
| **State at registration** | **41 of 56 = above p85.** ⚠ Starting at an extreme means **mean reversion alone produces C**, and that is disclosed |
| **Implied move** | ★ the observable is a **cross-sectional COUNT, which no straddle prices** ⇒ the threshold is outside the implied move **by construction**, stated rather than claimed as a virtue |
| **Information content (B4)** | **Both branches change a conclusion**: A kills `IT N`, B vindicates the flow instrument over the return instrument and settles the `M1184` contradiction that ROTATION could only name. ⚠ Deliberately **not** a fifth reading of the `AVGO` print — `S138`/`S132`/`S127` own that; this row owns the **sector-breadth consequence** |
| **Anti-signal (VOID)** | a **GICS reclassification moving ≥3 names into/out of Information Technology**, or a market-wide trading halt, inside 09-02 → 09-08 |
| **Owner** | `industry_US` · **settles 2026-09-08** |

---

## §6 · DEEP set updated

**Final DEEP set — N = 5** (4 by ROTATION's rule + 1 PREMORTEM promotion):
**continuous `[MATR, HLTH]` · rotating `[ENRG, COMM]` · PREMORTEM-promoted `[IT]`.**

**`IT`'s promoted mandate is NARROW and disjoint from ROTATION's four**, so it does not duplicate:
> *`S124` fired A at 41 of 56 while `eqflow` reads −0.014 with 3🟢 against 9🔴. **Price and
> participation disagree inside one sector.** Which of the two is describing the money — and does the
> answer survive the `AVGO` print?* Resolve on the **name level** (the 41 vs the 9 reds), not on the
> bucket, and state whether the desk's `IT N` should have been `OW`.

---

## ✅ EXIT CHECK
- [x] 4 lenses run against the draft tilt, each returning **named tickers + dated catalysts**.
      ⚠ **In-context and serial, not a parallel agent fan-out — declared (§0), 7th run.**
- [x] **Every bracket names its observable + frozen threshold + date, both branches, and an
      anti-signal.** Three registered (`S138` · `S139` · `S140`); **no one-way bracket.**
      ✅ **Registered into `handoff/SCENARIOS_US.md` THIS STAGE** (append-only, backup
      `SCENARIOS_US.md.bak_0901us`), together with MACRO's `P121`–`P124`. The `SCENARIOS.md` master-index
      line is appended at the run-end handoff step.
- [x] **Every magnitude threshold stated against the implied move.** `S138` **±11.00pp vs a measured
      ±9.6% (D1)** — outside. `S139` and `S140` have **no straddle by construction** (a basket and a
      cross-sectional count) and say so rather than inventing one (`D2`). ★ **And an existing row was
      pre-declared no-information rather than re-banded**: `S132`'s ±9.00pp now sits **inside** the
      ±9.6% priced move (`M1197`), threshold **not moved** (`D242`).
- [x] **Each branch graded by information content**; three binaries were **dropped with reasons**
      (MSCI — already scored; `AAPL` succession — neither branch moves a verdict; California wildfire
      legislation — explains a move but does not carry the thesis).
- [x] `BLINDSPOT_PREMORTEM.md` written — legs · brackets · re-tags · cycle GAP.
- [x] Every catalyst-bearing leg **promoted (`IT`) or logged (`INDU`, `FIN`, `UTIL`)**; brackets
      handed to ALPHA's action bracket; the cycle findings handed to BET.
- [x] **DEEP set updated and stated**: N=5, `[MATR, HLTH]` + `[ENRG, COMM]` + PREMORTEM-promoted `[IT]`.
- [x] ⚠ **Correlated-UW pattern checked** (field note) — and it is **confirmed by a settled bracket**
      (`S112` FIRED-B). The three UW labels are **one bet**; `S135` owns the structural question and
      `S139` re-arms the exposure across the NFP.

---
> Next: `python pipeline/run_protocol.py industry_us --next` → **DEEP** (Stage 8), N=5.
