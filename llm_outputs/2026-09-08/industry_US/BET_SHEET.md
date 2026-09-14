# BET_SHEET — industry_US · 2026-09-08 (Tue) · Stage 9 / L1·BET

> **ONE file, per-sector sections** (downstream desks glob this exact filename — never split it).
> DEEP set this run: **`ENRG` · `HLTH` · `FIN` · `INDU`** (4 of 4 filled for the first time in five runs;
> `FIN` and `INDU` promoted by PREMORTEM Lens 1).
> **P4 — analytical only. No sizing, no buy/sell language anywhere in this file.**

## 🚨 0 · Two instrument facts that govern every number below

**① Prices in §A are the PARTIAL 2026-09-08 intraday bar.** `module_fundamentals_us` was called after
09:30 ET, so `price`, `market_cap` and every multiple derived from them use an **incomplete bar**
(`D577`, registered in MACRO §0-b). Where a settled figure matters, the **2026-09-04 close** is given
beside it. **All flow, `exc`, `rs` and `[FINRA]` figures in §C are settled 2026-09-04.**

**② `REPORT/COMPANY_SCOREBOARD.md` supplies NO confirmation for this sheet.** It is dated
**2026-08-21** (18 days = well past the 10-settled-session age test) and holds **five KR names, zero
US**. ⇒ every name below is derived, not confirmed, and this is stated rather than left implicit.
`module_report_tags ticker` was run per name: `MPC`/`PSX` return only today's KR PREFLIGHT (a
substring collision, not coverage), `VLO` → 2026-08-14 `SECTOR_DEEP_ENRG`, `SLB` → `SECTOR_DEEP_COMM`,
`MDT` → yesterday's `SECTOR_DEEP_HLTH`, **`LNG` → *"no report has covered it"***.

---

# §ENERGY — the DEEP sector, and the sheet's only section with a live thesis

## §A · Numbers (⚠ price/multiples on the 09-08 partial bar; estimate series are `[yfinance]` `eps_trend`)

| name | price | mcap $B | trail P/E | **fwd P/E** | P/S | P/B | fwd EPS | tgt median | vs price | % of 52w high |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| **MPC** *(held)* | 397.60 | 112 | 13.78 | **12.51** | 0.75 | 5.90 | 31.78 | 322 | **−19.0%** | **99.7%** |
| **PSX** *(held)* | 260.70 | 105 | 14.88 | **12.24** | 0.68 | 3.30 | 21.30 | 234 | **−10.2%** | **99.9%** |
| **VLO** | 381.64 | 110 | 15.91 | **12.23** | 0.83 | 4.40 | 31.21 | 325 | **−14.8%** | **99.8%** |
| **SLB** | 58.43 | 87 | 28.50 | **18.08** | 2.38 | 3.33 | 3.23 | 63 | **+7.8%** | 96.6% |
| **LNG** *(outside `us_top300`)* | 278.30 | 57 | 21.08 | **13.40** | 2.75 | 9.35 | 20.77 | **310** | **+11.4%** | 92.5% |

⚠ **Gross/operating margin: BLANK.** `module_fundamentals_us --json` returned no margin fields for any
of the five. **Stated as blank, not filled from elsewhere** (`C3`) — which means **lens `L2`'s
peak-margin test cannot be run on its own terms this run**, and the substitute below is stated as a
substitute.

## §A-2 · ★ The peak-margin / low-multiple trap, tested on the DENOMINATOR instead

Lens `L2` says a cyclical at its earnings peak prints its lowest forward multiple because the
denominator is peaking. With margins blank, the test runs on the **estimate series**, which is
arithmetic and admissible as a *description of where the denominator has been going*:

| name | `+1y` EPS 90d ago → now | Δ | `0y` EPS 90d ago → now | Δ | `+1y` revisions (30d) |
|---|---|--:|---|--:|---|
| **MPC** | 23.78 → **31.78** | **+33.6%** | 29.20 → **50.95** | ★ **+74.5%** | **14 up : 1 down** |
| **VLO** | 21.18 → **31.21** | ★ **+47.4%** | 29.33 → **43.83** | **+49.5%** | 15 up : 2 down |
| **PSX** | 17.07 → **21.30** | **+24.8%** | 17.88 → **25.67** | **+43.6%** | 14 up : 1 down |
| **LNG** | 19.27 → **20.77** | +7.8% | 17.70 → **22.80** | +28.8% | 2 up : 2 down · ⚠ `0q` **3.81 → 4.68 = +22.8% in SEVEN DAYS**, 3 up : 0 down |
| 🚨 **SLB** | 3.347 → **3.232** | 🔻 **−3.4%** | 2.607 → **2.498** | 🔻 **−4.2%** | 🔻 **5 up : 19 DOWN** |

⇒ **The three refiners' "cheap" ~12.3× forward multiple is a denominator that rose 25–47% in 90 days**
— the exact `L2` shape, and it is why *"12× is cheap"* is not a valuation statement here.
⚠ **And the desk's own measurement bars using this as a signal**: `scripts/measure_ic.py` found the
revision axis is an **Information-Technology loading**, not a leading indicator (W1 +0.403 vs W2
−0.299, opposite signs, both above the power floor; ex-IT control +0.074 / −0.064). **Used
descriptively only; no proposition rests on it, and no sizing (`P4`).**

🚨 **The stale-target condition, stated because it is the opposite of what it looks like.** All three
refiners sit at **99.7–99.9% of their 52-week highs** with **analyst target medians BELOW spot**
(−19.0% / −10.2% / −14.8%). That is **not** a valuation verdict — it is targets that have not been
re-cut upward while estimates rose 25–47%. **Cited as an instrument lag, not as downside.**

★★ **`SLB` is the sheet's sharpest single contradiction and it is left standing.** It is the
LIVE_SHORTLIST's cleanest name — flow **+0.883 🟢**, OBV 매집, `rs20` **+14.2**, `[FINRA]` z **−1.21
with 5v5 −12.6▼ = short-covering**, news-velocity **1.94×** — **and its earnings estimates are being
cut on every horizon** (`+1y` 5 up : **19 down**; `0q` 5 up : **14 down**). Flow and the denominator
disagree. **Named, not averaged** — it goes to §E as an open question, not to a candidate line.

## §B · Thesis (freshness placeholder — ALPHA fills)

**The scarce asset is refining CAPACITY and, one link further out, GAS LIQUEFACTION — not the barrel.**
Body-read evidence, `--scope foreign`, 2026-09-07:
- **IEA: ~a fifth of Middle East refining capacity — 9.6 mb/d — knocked out by hostilities**;
  *"refinery margins are running at record highs across the world"*; **Russia banned diesel exports**
  after Ukrainian drone strikes; bunker-fuel shortfall **218,000 b/d this quarter** vs **6,000 b/d in
  2025**; *"record-low gasoline and diesel inventories"* [Reuters/Energy Aspects via oilprice].
- **QatarEnergy extended its LNG force majeure into November**; Asia spot LNG **$24.614/MMBtu = a
  5-month high**; TTF **€70 → €71.20/MWh = the highest in over 3.5 years, since January 2023**;
  Korea/India/Taiwan/Bangladesh tendering for Oct–Nov cargoes [oilprice, 2026-09-01].

**The arithmetic that confirms the mechanism** (DEEP-ENRG §1–2, settled 09-04):
distillate crack **level $99.21 = 95.6th percentile**, 20-session change **+$13.49 = 77.8th**,
60-session **+$37.51 = 91.3rd** — while the **gasoline crack's 5-session change is −$19.64 = the 0.0th
percentile of its own year.** ⇒ the diesel-prioritisation described in the wire is visible as a
**product-mix split in the futures**, not just as a quote.

## §C · Flow / positioning cross-read (settled **2026-09-04** unless marked)

| name | sweep flow | tag | OBV | `rs20` / `rs60` | `exc5` | `[FINRA]` z (5v5) | vol-normalised `z20` |
|---|--:|---|---|---|--:|---|--:|
| MPC | +0.694 | 🟡 | 매집 | **+30.8 / +41.5** | **+5.33** | +0.43 (+8.9▲) | ★ **+3.11** |
| VLO | +0.700 | 🟡 | 매집 | +24.7 / +37.5 | **+5.10** | +0.52 (+4.0▲) | ★ **+2.99** |
| PSX | +0.750 | 🟡 | 매집 | +25.5 / +34.2 | **+4.43** | −0.36 (+0.8▲) | ★ **+2.95** |
| SLB | +0.883 | 🟢 | 매집 | +14.2 / −2.6 | +0.20 | 🟢 **−1.21** (−12.6▼) | +1.25 |
| LNG | *(no sweep score — outside universe)* | 🟢 *(direct, **09-08 partial**)* | 매집 | — / **+11.2** | — | +0.02 (**+16.0▲**) | **+2.03** |
| WMB | +0.769 | 🟢 | 매집 | +5.7 / −3.6 | +0.46 | −1.16 (−11.6▼) | — |

⚠ **The three refiners are 🟡 and that is an instrument state, not a flow verdict**: none carries a
`velocity` because all three sit outside universe rank 52, and `scoring.vel_axis` is **false**
(`D561` — measured twice now with the identical `CEG`/`PG` pair). Their **OBV is 매집 and their `rs60`
is the sector's strongest**; the tag simply cannot go green for them.
⚠ **`D6`**: OBV is **C-grade** and carries none of these lines alone; the load is on `rs20`/`rs60`
(**A-grade**) and the crack arithmetic.
⚠ **`[COT]` WTI spec 1-year percentile 70 (09-01 reference)** — context, never a trigger; COT
contrarian is in this desk's REJECTED table.

## §D · Competition / chain position

`crude supply → REFINING CAPACITY (binding) → distillate vs gasoline mix (binding) → logistics →
LIQUEFACTION & SHIPPING (binding, unmeasurable) → end market`

| node | names | eqflow | `exc5` median | binding? |
|---|---|--:|--:|---|
| **Refining & Marketing** | `MPC` `VLO` `PSX` | ★ **+0.715** | ★ **+5.10** | **YES** — 9.6 mb/d destroyed |
| Equipment & Services | `SLB` `BKR` | +0.596 | +0.92 | no — services do not rebuild a bombed coker in a quarter |
| E&P | `COP` `EOG` `DVN` `OXY` `FANG` | +0.578 | +1.39 | **no** — the barrel is the abundant leg (`CL=F` 91.48 *"struggles above $90"*) |
| Storage & Transport | `WMB` `OKE` `TRGP` `KMI` | +0.518 | +0.53 | no |
| Integrated | `CVX` `XOM` | +0.344 | +2.44 | no |
| ★ **Liquefaction & LNG shipping** | `LNG` `GLNG` `FLNG` | 🚫 **NOT IN THE UNIVERSE** | — | **YES** — and unmeasurable |

★ **Energy's dispersion / sector-move = 0.92× — the only sector on the board below 1.0** (`D566`: IT
4.6×, HLTH 5.72×, UTIL ≈23×, FIN **50.9×**). ⇒ **this is the one bucket where a sector-level statement
is admissible at all.**

## §E · Refutation + dated catalysts

| kills the thesis | observable | current |
|---|---|---|
| **A confirmed Strait-of-Hormuz reopening (≥3 outlets)** | 🚨 **the correlated hit** — it takes gas, refining premium, breakevens and the three duration UWs together (PREMORTEM §2a) | `catalyst_calendar` carries it as an **undated 🔀binary** |
| A restart of **≥3 mb/d** of Middle East refining capacity | IEA / operator confirmation | not observed |
| **Russia lifts its diesel export ban** | wire confirmation | not observed |
| QatarEnergy force majeure **expiring in November** without renewal | a **dated** kill | **November 2026** |
| `refinery` term Δ negative **two runs running** | term sweep, phrase convention | today **+12.50% = the board's top riser** |
| 🚨 **`SLB`'s estimate cuts continue** (`+1y` 19 down : 5 up) | `eps_trend` next run | **falling on every horizon** — the one name whose flow and denominator point opposite ways |

**Dated catalysts on this section:** `P126` **09-09** (barrel vs chain) · `P140` **09-11** (crack rate
vs level — settles on the **5-session** leg, which is the 45.6th percentile, i.e. genuinely mid-pack) ·
`P139` **09-14** (Venezuela leg — ⚠ its driver decelerated a **second** consecutive run: raw **−8.89%**
after −5.3%) · **`P145` 09-14** (the gas/LNG chain, registered by MACRO because no sweep instrument can
reach it).

---

# §HEALTH CARE — one name, and the section is short because the sector's answer was "no driver"

## §A/§C · `MDT` (Medtronic)

price **92.90** *(09-08 partial)* · mcap **$119B** · trail P/E 22.88 · **fwd P/E 14.52** · P/S 3.17 ·
P/B 2.40 · fwd EPS 6.40 · target median **106 = +14.1%** · **87.4% of its 52-week high**.
Flow **+0.928** 🟢 · OBV 매집 · vol-surge **1.47** · `rs20` **+8.4** / `rs60` **+11.2** · `exc5`
**+3.11** *(settled 09-04)*.

**§A-2 — the denominator is DEAD FLAT**: `+1y` EPS **6.410 → 6.399** over 90 days (−0.2%), revisions
**1 up : 1 down** on every horizon. ⇒ `MDT` is a **pure flow-and-price name with zero estimate
momentum** — which is exactly consistent with DEEP-HLTH's verdict that the sector is a **residual, not
a thesis** (no driver found: `drug pricing` 🔴FADING 0.45× / 28 hits, `obesity drug` 19, against
`rate hike` 1,382 in the same window).

**§B/§D/§E, stated compactly because the section does not earn more:**
`MDT` is the sector's **only 🟢 and it sits inside the sector's ONLY negative-`eqflow` sub-node**
(Health Care Equipment: **−0.044 eqflow**, `exc5` median **−2.16**, with `SYK` −0.706 / `exc5` −8.44
and `IDXX` −0.692 both 🔴). ⇒ **it is the exception to its own sub-node and may not be read as sub-node
confirmation.** `[FINRA]` z **+1.43 (normal range)**. Refutation: HLTH `eqflow` losing its positive
sign, or any HLTH term clearing 500 articles/7d with `theme-age` ≥ 2× (⇒ a real driver arrived and the
residual framing is void). Dated catalyst: **`S133` 09-14**; the free cross-check is **`P148` branch B**
(09-17) — if a dovish steepening fires and HLTH does **not** deteriorate, the duration-residual
mechanism behind this whole section is wrong.

---

# §FINANCIALS — a DEEP sector that produces NO candidate, and that is the finding

**Dispersion / sector-move = 3.420 / 0.067 = 50.9× — by far the board's worst.** `FIN N` is
arithmetically correct and analytically empty: Exchanges/Data is the most **flow-positive** node and
**price-negative**; Diversified Banks is **flow-flat** and the most **price-positive**. Averaging them
produces `eqflow` −0.023 and means nothing.

**No name is carried to §A.** The sector's two decision-relevant facts are:
1. 🚨 **`SPGI`** — flow **+0.711** (sector #2), OBV 매집, surge 1.08, `exc5` **+0.03 = flat**, against
   `[FINRA]` short-vol **82.2% vs a 54.3% base = z +3.00 with 5v5 +17.9▲**, **the board's most extreme
   short-pressure reading this run.** Two weak instruments (C-grade OBV vs a short-volume proxy the US
   has no investor-type feed to check) pointing opposite ways. **Named, not averaged; filed to the
   opportunity-cost ledger rather than resolved.**
2. **P&C insurance is the one node a verdict could attach to** — `eqflow` **−0.323** with **5 of 5
   names 🔴 분산** (`ALL` −0.512 · `HIG` −0.514 · `TRV` −0.579 · `CB` −0.291 · `PGR` +0.282 the lone
   🟡). A node where every name agrees; **no candidate follows, because the agreement is negative.**

🚨 **And a coverage defect this sector exposed:** `us_top300.csv` holds **exactly two Regional Banks**
(`HBAN` +0.042, `FITB` −0.640, a 0.68 spread across the whole node). **Any "regional banks are X"
statement from this desk is a statement about two companies** — the same class as `D563`, registered
as **`D579`**.

**Dated catalysts:** `P128` **09-08** (🚫 blocked by `D427` for a 6th run — its `[FRED]` leg does not
carry 09-04) · `S142` **09-11** · **`P148` 09-17**, registered today precisely because it settles on
ETFs and `D427` cannot block it.

---

# §INDUSTRIALS — a DEEP sector that produces NO candidate, and one BOOK FLAG

**No name is carried to §A.** Aerospace & Defense is the sector's worst sub-node (`eqflow` **−0.622**,
`exc5` median **−3.90**, **0 greens of 10**, nine of ten 🔴 분산) and **`RTX` — held — is the single
worst flow score in the entire 50-name sector at −0.789**, `rs20` **−9.6**, `exc5` **−5.27**.

🚩 **BOOK FLAG on `RTX`, and it is now specified rather than repeated.** The defense capital cycle is
being repriced — but on **German and Japanese balance sheets**: *"Volkswagen finds defense role for
German factory"*, *"Japanese banks in a bind over defense investments and loans"* (10 articles / 5
outlets, 09-07), against `theme-age AfD` **8.73×, the fastest-accelerating term on the board**.
**`S150` (09-14) brackets `EW{RTX,LMT,NOC,GD,LHX}` — five US primes, none of which can express that.**
⇒ the position is not merely underperforming; **its catalyst is landing where its bracket cannot see.**

★ **And the sector's only positive-`exc5` cluster is a chain whose bottleneck has no ticker.** `VRT`
**+9.01**, `FIX` **+5.92**, `PWR` **+3.49**, `GEV` **+3.18**, `ETN` **+1.89**, `EME` **+1.78** — every
one a data-centre electrical/MEP name, **and the flow axis is negative on all six**, with `[FINRA]`
short pressure **building** on `VRT` (+1.03), `FIX` (+1.10) and `PWR` (+1.33). The binding constraint
is an **interconnect permit**, and **two jurisdictions have now halted approvals** (Texas; **Thailand,
2026-09-04, all builds**). **No candidate follows, because a permit has no ticker.**

---

# §LIVE_SHORTLIST — cross-sector names outside the DEEP sectors

Eleven names cleared `mcap ≥ $10B ∧ 🟢가속`. Three are already in §ENERGY (`SLB`, `WMB`, `CVX`); one
is §HEALTH CARE (`MDT`). The remaining seven, with the one number that decides each:

| name | sector (verdict) | the deciding number | disposition |
|---|---|---|---|
| **DELL** | IT (`N`) | ★ **`0y` EPS 18.35 → 25.88 = +41% in 90 days**, `+1q` **4.05 → 6.87 in SEVEN DAYS**, 0 downgrades; fwd P/E **18.10**; flow **+1.000 = the board's top score**; `exc5` — ; `[FINRA]` −0.46. ⚠ **P/B prints −234.12 = negative book equity**, a buyback artifact, **stated as unusable, not as a valuation** (`C3`) | ★ **CARRIED to §B as the sheet's only non-Energy live thesis candidate** — see below |
| **DE** | INDU (`UW−`) | flow +0.911 🟢, `exc5` **+9.92 = the sector's best** — **but `0q` revisions are 2 up : 14 DOWN (30d)** and `+1y` EPS is **falling** (22.83 → 22.67) at a **30.2× forward P/E** | **SET ASIDE** — price and denominator disagree at a 30× multiple. `reject_ledger` |
| **HOOD** | FIN (`N`) | `rs20` **+31.3**, `exc5` **+17.01 = the board's largest**; `[FINRA]` −0.64 clean. **But vol-normalised `z20` is only +1.19** on a 5.81% own-sigma ⇒ **not extended, and not confirmed either** | **SET ASIDE** — no sector verdict to hang it on (`FIN` dispersion 50.9×). `reject_ledger` |
| **CTVA** | MATR (`N−`) | ★ **vol-normalised `z20` +2.21 on the board's second-smallest sigma (1.45%)** — a 2σ move that the raw ranking hides; flow +0.861 🟢 | **SET ASIDE, and flagged as the run's quietest extreme** — `P102` settles the two-name MATR question **09-09** and moving first would pre-empt it (`D343`). `missed_ledger` |
| **RSG** | INDU (`UW−`) | flow +0.631 🟢 but `[FINRA]` z **+2.61 = ⚡crowded-short**, `exc5` **+0.16 ≈ flat** | **SET ASIDE** — squeeze fuel is turn-conditional and there is no turn. `reject_ledger` |
| **TSLA** | DISC (`UW`) | flow +0.828 🟢 with velocity 1.52× — inside the board's **worst `exc20`** bucket after INDU (`eqflow` −0.280, 21 of 28 negative on `exc5`) | **SET ASIDE** — sector verdict and name disagree, and the sector cut is the admissible one. `reject_ledger` |
| **PG** | STPL (`UW`) | 🚨 flow **+0.231** with vol-surge **0.89 — below the gate** — green **only because rank 34 grants it a velocity on an axis `scoring.vel_axis` declares FALSE** (`D561`, 2nd reproduction) | **SET ASIDE as an instrument artifact, not a name** |

## §DELL — the sheet's second live thesis, carried on its denominator

**§A** price **517.75** *(09-08 partial)* · mcap **$335B** · trail P/E 30.13 · **fwd P/E 18.10** ·
P/S 2.21 · **P/B −234.12 (unusable — negative book equity)** · fwd EPS 28.61 · target median **564 =
+8.9%** · 96.8% of its 52-week high.
**§A-2** `0y` EPS **18.35 → 25.88 = +41.0% in 90 days**; `+1q` **4.05 → 6.87 = +69.7% in seven days**;
revisions `0y` **8 up : 0 down (30d)**, `+1y` 2 up : 0 down. ⇒ a **post-print step-change**, not a drift.
**§C** flow **+1.000 = the highest score in the 299-name universe**, OBV 매집, **vol-surge 2.48 = the
highest on the board**, `rs20` **+15.9**, velocity **2.22×** (one of only four shortlist names with a
measured velocity at all), `[FINRA]` z **−0.46 = clean** *(settled 09-04)*.
**§B/§D** the AI-server assembly leg of the compute chain — the layer between the silicon (`NVDA`,
`AVGO`, both held) and the data-centre power problem §INDUSTRIALS just showed has no ticker.
**§E — refutation** ⚠ **its sector is `IT N`, and `D566` measures IT's dispersion/move at 4.6× ⇒ there
is no sector-level fact to attach it to**; the name must stand on its own denominator. ⚠ **And the
desk's own `measure_ic` result says the estimate-revision axis is an INFORMATION-TECHNOLOGY loading**
— i.e. exactly where the confound lives — so **`DELL`'s revision series may not be used as independent
evidence** (`RESEARCH.md`, binding). It is here as a **description**, and the section says so.
**Dated catalyst**: `S140` settles **on tonight's close**; `S148` **09-14** (`ORCL`+`ADBE` prints 09-10).

---

## ✅ EXIT CHECK — BET

- [x] **ONE file, per-sector sections**, filename unchanged.
- [x] Candidate set = DEEP-sector thesis leaders **∪** `US_LIVE_SHORTLIST.json` names (the cross-sector
      drag-in has its own section), **not** the three names already known.
- [x] **§A numbers table with blanks stated as blanks** — gross/operating margin is **blank for all
      five Energy names** and is written as blank, with the consequence (lens `L2` cannot run on its
      own terms) stated rather than papered over.
- [x] **XBRL ↔ yfinance cross-check**: `module_fundamentals_us` pulls both; the one field that
      disagrees with reality (`DELL` P/B −234.12) is **marked unusable**, not printed as a multiple.
- [x] §B thesis + freshness placeholder (ALPHA fills) · §C flow/positioning with **asof on every
      figure** and the settled-vs-partial split stated · §D chain position · §E refutation + dated catalyst.
- [x] **Cycle GAP / epicenter-starter**: `cycle_exposure` reports **no GAP** — and PREMORTEM Lens 4's
      limit is carried: the ✅ covers **three registry cycles**, and **two of the week's loudest
      (gas/LNG, AI-power permitting) have no row at all**. **No epicenter-starter module is emitted on
      a ✅ this desk cannot verify.**
- [x] **Sizing language: none.** `P4`.
- [x] **Every name set aside is written to a ledger with its class, `--revives-if` and `--recheck-date`**
      — see the ledger block appended below.
- [x] **`module_math_check` run on this file** — result appended below.

---

## Ledger writes made by this stage

**`reject_ledger`** — every row carries a reason class, a `--revives-if` and a `--recheck-date`
(script-enforced; `add` refuses without both):

| ticker | class | revives if | recheck |
|---|---|---|---|
| **DE** | `I.테제반증` | the `+1y` EPS series turns up two consecutive runs **AND** `0q` revisions stop being net-down | **2026-09-29** |
| **HOOD** | `G.섹터중립` | FIN dispersion/sector-move falls below 5× **OR** a FIN sub-node verdict is issued that `HOOD` sits inside | **2026-09-22** |
| **RSG** | `D.약한손` | `[FINRA]` z falls below +1.0 while flow stays above +0.5 **AND** `exc5` turns positive | **2026-09-22** |
| **TSLA** | `G.섹터중립` | DISC `eqflow` turns positive **OR** DISC `exc5` breadth exceeds 14 of 28 | **2026-09-22** |

**`missed_ledger`** — names that cleared a gate and never reached a candidate line (⚠ sign inverted vs
the rejection ledger: `excess > 0` means missing it cost us):

| ticker | class | enters if | recheck |
|---|---|---|---|
| **CTVA** | `S.테마회피` | `P102` settles and its verdict does not rest on `CTVA`, **AND** `CTVA` `z20` stays above +1.5 | **2026-09-10** |
| **SPGI** | `Q.확신부족` | the two instruments agree in sign — `[FINRA]` z below +1.0 while flow stays above +0.5, **OR** flow turns negative | **2026-09-22** |
| **GLNG** · **FLNG** *(filed by EVENT_ALPHA, listed here for completeness)* | `N.유니버스부재` | the name appears in `us_top300.csv` **AND** its sweep tag is green with OBV accumulating (**RULE D6 exempt** — this is a ledger revival *condition*, i.e. the gate a future run must clear, not a proposition this run rests on) | **2026-09-22** |

⚠ **`PG` is deliberately in NEITHER ledger.** It was set aside as an **instrument artifact** — green
solely because universe rank 34 grants it a `velocity` on an axis `scoring.vel_axis` declares **false**
(`D561`, second reproduction today with the identical `CEG`/`PG` pair). Filing an instrument defect as
a stock rejection would put a tool bug into a stock scoreboard and corrupt the reason-class statistics.
**Recorded here in prose instead**, which is the honest place for it.

## `module_math_check` — result

`python -X utf8 -m module_math_check llm_outputs/2026-09-08/industry_US/BET_SHEET.md`
⇒ **ALL MATH CHECKS PASSED** (0 findings). ⚠ It verifies arithmetic, not judgement.


---

# §B · ALPHA FRESHNESS TAGS — filled by Stage 10 / L1·ALPHA (2026-09-08)

> 🚨 **The gate's own instrument was probed before any verdict was issued** (`G1`, and this stage's
> standing warning that a dead pipe and a quiet theme return identical values). Falsification probe on
> the **direct** path, after an idle gap: `NVIDIA` **3,926** and `삼성전자` **1,450` — both loud, both
> moving vs earlier in this same run (3,892 / 1,442). **The pipe answered, so the zero below is
> arithmetic and not the instrument.** PREFLIGHT `G1` FAILs the **sweep** axis (17.39%) and explicitly
> **GRANTS** direct `module_news_data` calls made outside a sweep burst — which is what every
> `theme-age` reading here is.

## The tags

| bet | theme (`theme-age`, foreign) | tag | evidence label + date | residual / why not higher | **re-check** |
|---|---|:--:|---|---|---|
| **ENRG refining** — `MPC` *(held)* · `PSX` *(held)* · `VLO` | `refining margin` **⚪ECHO 0.71×** (age 82, base 326) · `diesel` ⚪ECHO **1.06×** (base 2,073) | 🟡 **PARTIAL** | `[body-read 2026-09-07]` IEA **9.6 mb/d** of Middle East refining capacity destroyed · *"refinery margins at record highs"* · **Russia diesel export ban** · bunker shortfall **218 kb/d vs 6 kb/d in 2025** · `[futures 2026-09-04]` distillate crack **level 95.6th pctile**, 20d change **77.8th**, 60d **91.3rd**, gasoline crack 5d **0.0th** | ★ **The two axes disagree by construction**: the *narrative* axis is decelerating for a **6th consecutive run** (0.71×) while the *physical* axis printed new dated evidence today. `D559` says the age leg measures the age of the **word**, not of the event — so ECHO here is a statement about vocabulary, not about supply. **Not upgraded to 🟢 anyway**, because the desk does not get to overrule its own gate with an argument | **2026-09-11** (`P140` settles on the **5-session** crack leg = the 45.6th pctile) |
| **ENRG gas/LNG** — `LNG` · `GLNG` · `FLNG` *(all outside `us_top300`)* | `LNG` ⚪ECHO **1.18×** · `force majeure` ⚪ECHO **1.18×** (age 76, base 159) · `Hormuz` ⚪ECHO **0.78×** on a **10,568** base | 🟡 **PARTIAL** | `[body-read 2026-09-01]` **QatarEnergy force majeure extended into November** · Asia spot LNG **$24.614/MMBtu = 5-month high** · TTF **€71.20/MWh = highest since Jan-2023** · `[FINRA 09-04]` `GLNG` z **−1.65**, `FLNG` z **−1.85** = short-covering | 🚨 **The residual is an INSTRUMENT residual, not a market one**: none of the three has a sweep score, a shortlist line or `chain-hop` reachability, because the universe does not contain them (`D563`). **`P145` is the only object that will settle it.** ⚠ `LNG`'s own short interest is **BUILDING** (2.1% float, DTC 2.6) against a P/C of **0.06 = complacent** | **2026-09-14** (`P145`) |
| **`SLB`** | `refining margin` ⚪ECHO 0.71× | 🟡 **PARTIAL** · ★ **MOMENTUM-ONLY, HARD-STOP REQUIRED** | flow **+0.883 🟢**, `rs20` **+14.2**, news-velocity **1.94×**, `[FINRA 09-04]` z **−1.21 / 5v5 −12.6▼ = short-covering**, short 4.3% float **covering** | 🚨 **RS and volume are green while the DENOMINATOR is being cut on every horizon** — `+1y` **5 up : 19 down**, `0q` **5 up : 14 down**, `+1y` EPS −3.4% in 90 days. ⚠ **This is NOT the `D6` C-grade case** — the disagreement is with the **estimate series**, not with OBV, so it does not auto-downgrade; it is stamped **momentum-only** and carries a hard-stop requirement instead. Option book **P/C 0.45 = complacent** | **2026-09-22** |
| **`MDT`** | no sector driver found — `drug pricing` 🔴**FADING 0.45×** (28 hits/7d), `obesity drug` 19, `Medicare` 160, `FDA approval` 94, against `rate hike` **1,382** in the same window | 🟡 **PARTIAL** | flow **+0.928 🟢**, surge **1.47**, `rs20` +8.4 / `rs60` +11.2, `exc5` **+3.11**, `[FINRA]` z +1.43 normal, short 1.1% float covering | **The denominator is DEAD FLAT** (`+1y` EPS 6.410 → 6.399 over 90 days, 1 up : 1 down) and the name is the **exception inside its own sector's only negative sub-node**. DEEP-HLTH's verdict — *breadth without a driver* — is the residual | **2026-09-14** (`S133`; free cross-check **`P148`-B** 09-17) |
| **`DELL`** | `AI server` ⚪ECHO **1.56×** (base 1,350) — the **highest acceleration of any bet theme this run** | 🟡 **PARTIAL** | flow **+1.000 = the highest of 299**, vol-surge **2.48 = board's highest**, velocity **2.22×**, `rs20` +15.9, `[FINRA]` z −0.46 clean · `0y` EPS **+41.0% in 90 days**, `+1q` **+69.7% in seven days**, 8 up : 0 down | ⚠ **The single piece of evidence that would upgrade it is the one the desk's own control says is confounded**: `measure_ic` found the revision axis is an **Information-Technology loading** (ex-IT control +0.074 / −0.064), and `DELL` is IT. ⚠ Its sector has **no attachable fact** (`D566`, IT dispersion/move 4.6×). ⚠ Short interest **BUILDING** 4.6% float, P/C **2.3 = hedged/fearful** | **2026-09-14** (`S148`; `S140` settles **tonight**) |

## 🚨 `F1` — 🟢LIVE fired **ZERO** times again, and this run can say something sharper than "no fresh theme exists"

**Zero 🟢LIVE**, for the same structural reason `D559` identified: **every** bet theme measured today is
**⚪ECHO**, and every one fails on the **age** leg (`refining margin` 82 · `force majeure` 76 · `diesel`
and `AI server` ≥90), not on acceleration. The gate requires **≤14 days AND ≥2× acceleration**, and a
theme old enough to have a 90-day base is old enough to fail the age leg by construction.

★ **But the board is NOT short of acceleration — the acceleration is in themes with no bettable name.**
Measured this run: **`AfD` 🟡ACCELERATING 8.73×** (age 78) · **`bond selloff` 🟡ACCELERATING 4.18×** ·
**`Fed hike` 🟡ACCELERATING 2.09×**. All three clear the acceleration leg decisively; **none has a US
ticker this desk can express** (`AfD` → `P146`'s `EWG`; `bond selloff`/`Fed hike` → `P142`/`P148`/the
09-07 `TLT` row — all **index or ETF** objects, not names). ⇒ **The correct statement is not
*"nothing is fresh"* but *"what is accelerating has no name on this sheet"***, which is a different
finding and points at the universe rather than at the market.

## Carry-forward — tagged names follow the NAME, not the sector's turn in the rotation

The next run inherits **all five tags above regardless of which sectors hold DEEP slots**:
`MPC` · `PSX` · `VLO` · `SLB` · `LNG` · `MDT` · `DELL`. Measured reason this rule exists: a name that
carried an ALPHA tag and lost its sector's slot went **+12.3% over five sessions, unowned**.

**🔴RESOLVED this run: none.** No tag was dropped, so no `reject_ledger` row is written *by this
stage*; the four names set aside at BET (`DE` · `HOOD` · `RSG` · `TSLA`) already carry rows with
`--revives-if` and `--recheck-date`, and `CTVA` · `SPGI` carry `missed_ledger` rows.
