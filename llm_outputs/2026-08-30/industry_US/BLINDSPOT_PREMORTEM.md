# BLINDSPOT_PREMORTEM — industry_US · 2026-08-30 (Stage 7 / L1·PREMORTEM ★US-only)

> Four adversarial lenses fanned out **in parallel, one message**, each given the draft tilt, the 4
> DEEP picks, the repaired flow sweep and the dated catalysts, and each required to return **named
> tickers + dated catalysts**. Analytical only — no sizing, no buy/sell (P4).
> ⚠ **Agent output is not accepted at face value.** Every number a lens returned was re-checked
> against `SECTOR_FLOW_US_REPAIRED.json` before it appears below. **One lens diagnosis was refuted**
> (§0b) and the refutation turned into the run's largest finding.

## §0 · Two things the lenses found that outrank the brackets

### 0a ★★★ `M1098` — the desk is running **two different books** and has never reconciled them

I pulled the **real KIS account** to verify a Lens-4 claim. It does not match the paper book every
other stage in this run has used:

| | `module_paper_book status` (11 US names) | **real KIS account** (9 US names) |
|---|---|---|
| both | ANET · ETN · HPE · MPC · NVDA · PSX · RTX | same 7 |
| **paper only** | **AVGO · MET · NDAQ · NUE** | — |
| **real only** | — | **`CBRE` · `T`** |

⇒ 🚨 **`T` (AT&T) is 27 shares = $702 = 13.6% of the real account's invested capital, and it appears
in ZERO artifact this run** — no standing thesis, no flow tag pulled, no cycle row, no DEEP mandate.
**And ROTATION promoted Communication Services to OW and gave it a DEEP slot forty minutes ago
without knowing the desk already owns a position in that sector.** `T`'s numbers were available the
whole time: **flow +0.333 · OBV +0.393 매집 · rs20 +8.8 · rs60 +8.4 vs `SPY`**. ⚠ **CORRECTED: this section
originally called that "the second-strongest flow score in the twelve-name COMM bucket". It is not —
`T` ties `META` for 5th–6th of 12. `DIS` +0.539 · `WBD` +0.461 · `NFLX` +0.444 · `CMCSA` +0.422 all
rank above it.** The error was caught by the `SECTOR_DEEP_COMM` agent disagreeing with its own brief.
**The finding is unaffected** — what makes `T` matter is that it is a real 13.6%-of-invested position
with no thesis, not its rank — but the wrong number is corrected rather than left standing. `CBRE` ($151, Real Estate — a **UW** sector) is the same
class: **flow −0.127 · rs60 +17.7 vs `SPY`**, un-owned by any thesis.
⇒ **This is the 2026-08-10 "the desk cannot tag what it owns" invariant failing again — but in the
*real* book, where `PREFLIGHT G5` never looked.** G5 checked the universe against the **paper** book's
11 names and passed 11/11; `cycle_exposure.py` audited the **real** account's 9. **Two book objects,
one run, both reported as "the book", never reconciled.** Registered as **`D415`**.
✅ **Both names ARE in `us_top300`**, so this is not a universe gap — it is a *which book* gap.

### 0b ★★ `M1099` — `D5` (cross-provider) is now met at the **name** level, by a broker feed

The 08-29 run recorded `D5` as unmet (Stooq 404'd) and said name-level 08-28 prices were
"one-provider, three-surface". The KIS pull above carries **Korea Investment & Securities' own
overseas quotes** — a real broker feed, entirely independent of `yfinance`:

| | NVDA | ANET | ETN | HPE | MPC | PSX | RTX | T | CBRE |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **KIS (broker)** | 217.55 | 195.38 | 402.78 | 52.31 | 368.83 | 244.01 | 211.71 | 26.01 | 150.82 |
| **5m proxy (yfinance)** | 217.54 | 195.31 | 402.67 | 52.29 | 368.88 | 244.03 | 211.72 | 26.00 | 150.87 |
| diff | −0.005% | −0.036% | −0.027% | −0.038% | +0.012% | +0.008% | +0.005% | −0.038% | +0.033% |

**Mean abs 0.0225% · max 0.038% · n=9 · zero names above 0.04%.**
⇒ **The 2026-08-28 session is now corroborated at the single-name level across two independent
providers**, on top of the index-level FRED check in `MACRO_REPORT §A-0`. **`D5` is met.**

⚠ **And the lens diagnosis that led me here was WRONG, which is recorded rather than quietly fixed.**
Lens 4 reported that `AVGO` is in the rank-1 epicenter list but absent from `epi_names`, and
diagnosed *"a ticker-match miss in the classifier, same family as the historic `.KS`-suffix bug."*
**It is not a bug.** `cycle_exposure.py` reads the **real KIS account**, and **`AVGO` is simply not
held there** — it is a paper-book position. The lens's *observation* was correct and valuable; its
*mechanism* was invented. **`M1100`.**

---

## §1 · LENS 1 — UNDER-COMPUTED LEGS

Every number below re-verified against the JSON. Verdicts are mine, not the lens's.

| rank | leg (not deep-dived) | the bull case | named tickers (flow · OBV · rs20 · rs60 vs `SPY`) | dated catalyst | verdict |
|---|---|---|---|---|---|
| **1** | **IT — enterprise/application software** | **3 of the universe's only 4 🟢 names sit in this one sub-industry**, invisible in IT's cap-weighted view because semis dominate it and `wflow` is barred (flipper, `NVDA` 19.4%) | `CRM` **+1.000 · +0.305 매집 · +36.3 · +32.4** (`vol_surge` **1.64**, the only volume-confirmed green) · `NOW` +0.572 · +0.393 매집 · +27.1 · +20.7 · `PLTR` +0.506 · +0.263 매집 · **+48.4** · +29.0 · `SHOP` +0.456 · +0.437 매집 · +27.6 · +33.4 · `INTU` +0.850 · +0.165 매집 · +10.3 · +13.0 | **08-31 MSCI review (D-1)**; `AVGO` 09-02 for sector read-through | ★ **PROMOTE-TO-DEEP** (see §5) |
| **2** | **ENRG — refining + oilfield services** | ENRG's `eqflow` (+0.005) understates it: four names carry OBV accumulation with the board's best 60-day legs | `SLB` +0.661 · +0.318 매집 · +12.6 · **−1.2** · `MPC` (held) +0.650 · +0.329 매집 · +13.6 · **+36.0** · `PSX` (held) +0.388 · +0.082 매집 · +12.3 · **+30.1** · `VLO` +0.349 · +0.090 매집 · +9.6 · **+32.7** | Hormuz state (undated) | **WITHIN-RUN-WATCH** — ⚠ **not promoted**, because `R89`+`P83` bar the margin-vs-barrel attribution this leg's bull case depends on. `SLB` already logged to `missed_ledger` in EVENT_ALPHA |
| 3 | **INDU — asset-light business services inside a UW sector** | INDU's `eqflow` −0.291 is dragged by machinery/transport; a payroll/waste/information cluster is accumulating **inside the same red sector** | `RSG` +0.449 · +0.204 매집 · +2.5 · +6.7 · `ADP` +0.393 · +0.287 매집 · +4.9 · **+24.2** · `TRI` +0.343 · **+0.403 매집** · +5.3 · +25.4 · `PAYX` +0.321 · +0.389 매집 · +5.7 · +27.0 | **Aug NFP 09-04 (D-5)** — `ADP`/`PAYX` are priced on the same variable | **WITHIN-RUN-WATCH** |
| 4 | **DISC — travel/experiences inside a UW sector** | the sector was just demoted to UW on `eqflow` −0.247, yet it holds the **two biggest runners in the entire 299-name universe** | `DASH` +0.594 · **+0.679 매집** · +17.6 · **+51.1** · `ABNB` +0.689 · +0.275 매집 · **+22.0** · **+39.8** · `BKNG` +0.266 · +0.133 매집 · +3.6 · +22.8 | none direct; NFP 09-04 read-through | **WITHIN-RUN-WATCH** — ⚠ **and this is a challenge to a verdict this run made 30 minutes ago**; see §3 |

**Falsifiers, one per leg**: (1) IT-software — `CRM` `vol_surge` falling below 1.0 while `rs20` stays
high (the volume confirmation is the only thing separating this from the drift). (2) ENRG — `VLO`'s
`obv_state` flipping back to 분산, which would make the whole cluster's `rs60` a stale July echo.
(3) INDU — a hot ADP/NFP hitting payroll-processor multiples on rate sensitivity even as the labour
data reads "good". (4) DISC — no direct catalyst exists, so it is momentum-only by construction.

---

## §2 · LENS 2 — REGIME-FLIP / BOTH-SIDES · brackets registered

★ **Every magnitude threshold below is stated against the implied move I measured directly** (ATM
straddle mid, spot = 08-28 5m-proxy close). This closes **`D295`**, unmet for 5 runs:

| underlying | expiry | implied | 20d realised (5-session) | note |
|---|---|---:|---:|---|
| **`AVGO`** | 08-31 (pre-print) | **±1.73%** | — | OI 198c/124p |
| **`AVGO`** | **09-04 (spans the 09-02 print)** | **±8.09%** | **6.21%** | **OI 645c/354p** — implied is **1.30×** realised |
| `AVGO` | 09-11 / 09-18 | ±8.99% / ±9.97% | — | — |
| **`HPE`** | **09-04 (spans the 09-03 print)** | **±11.23%** | **7.21%** | **OI 232c / 507p (P/C 2.19)** — implied **1.56×** realised |
| `NVDA` | 09-04 / 09-11 / 09-18 | ±3.67% / ±4.96% / ±6.16% | — | 🚨 **09-11 put OI 4,602 vs call OI 379 = P/C 12.1×** |
| `XLK` | 09-04 / 09-11 | ±2.52% / ±3.94% | 3.84% | — |
| `XLF` | 09-04 / 09-11 | ±1.36% / ±2.17% | 1.41% | — |
| **`XLU`** | 09-04 / **09-11** / 09-18 | ±4.14% / **±2.88%** / ±4.21% | 1.89% | 🚨 **09-11 put OI 3,594 vs call OI 22** · **09-18 put OI 11,313 vs call 5,341** |

★ **`M1101`** `[measured]` **The heaviest one-sided option positioning on this board sits at the
2026-09-11 expiry — the August CPI date — in `XLU` (put/call OI 163×) and `NVDA` (12.1×), which are
exactly the two legs the desk has NO bracket on.** The desk logged "PPI/CPI, zero rows" as a gap for
two runs; the options market has been building a position there the whole time.

### Registered brackets — ★ **one registered, three withdrawn, because the ledger already owned them**

🚨 **I drafted four brackets and then read `handoff/SCENARIOS_US.md` before writing any of them, and
three were already registered by the 08-29 run.** They are withdrawn rather than issued, because a
second row on one event is the `D343` double-count this desk keeps logging:

| drafted | fate | the row that already owns it |
|---|---|---|
| MSCI 08-31 (the mandatory ≤48h bracket) | ❌ **WITHDRAWN** | **`S131`** (registered 08-29, ARMED, settles **2026-08-31**): `RSP` − `SPY` 1-session excess, **A ≥ +1.30pp / B ≤ −1.30pp**, both outside `RSP`'s own ±1.06% implied. ⇒ **the ≤48h obligation is already satisfied** and my tighter ±0.60pp draft would have re-frozen a live threshold, which `D242` forbids. ⚠ **My independent band derivation is recorded anyway** (±0.41σ of `SPY`'s 20-day daily sigma) **because it lands tighter than the armed row's**, i.e. the live row is the more conservative of the two |
| `AVGO` 09-02 print | ❌ **WITHDRAWN** | **`S132`** (08-29, ARMED, settles **09-03**): 1-session excess vs `SPY`, **±9.00pp**, set outside the then-measured ±8.11% implied — **and `S127` is armed on the same print** (settles 09-08). **Two rows already; a third is excessive.** ★ **My independent re-measurement of the implied move today gives ±8.09% (09-04 expiry, K=367.5, straddle 29.83, OI 645c/354p) against the 08-29 run's ±8.11% — agreement to 2 bp on a different day's chain**, which is a useful corroboration of `S132`'s threshold and is why it is left alone |
| `HPE` 09-03 print | ❌ **WITHDRAWN** | **No row owns it — and it was deliberately deferred**: the 08-29 run declined it in writing because *"it is inside the `IT` DEEP mandate and bracketing a name the same run is about to deep-dive pre-commits the DEEP's conclusion."* **`IT` is again a DEEP this run (promoted, §5), so the identical reasoning applies and the deferral is renewed, not re-decided.** ⚠ Recorded with today's number so the DEEP inherits it: implied **±11.23%** (09-04 expiry, K=52.00, straddle 5.87, **P/C OI 2.19×**) against a **7.21%** 5-session realised sigma |
| duration-basket dispersion | ✅ **REGISTERED as `S135`** | nothing live owns it — the nearest prior settled **2026-08-13** |

**`S135` — the one new row.**

| Field | Value |
|---|---|
| **Why it exists** | The stage's field note tells this lens to hunt the **correlated-UW pattern**, and the desk currently books `UTIL`, `RE` and `STPL` as three separate verdicts. The last row that tested this family settled **2026-08-13** and nothing has replaced it. ★ **And there is a fresh prior AGAINST the one-bet reading**: on 08-28 the three duration legs printed **1.11pp apart** (`XLK` −1.33 · `XLU` −0.87 · `XLRE` −0.22 vs `SPY`), which is why the row is worth running rather than assumed |
| **Frozen observable** | **max pairwise spread among `XLU`, `XLRE`, `XLP` 5-session excess returns vs `SPY`**, settled closes, **2026-09-04 → 2026-09-11**, `yfinance`, `auto_adjust=False`. Benchmark **`SPY`, named inline on all three legs (`C1`)** |
| **Branch A (they are ONE bet)** | max pairwise spread **≤ 1.50pp** ⇒ the desk's three UW verdicts are one position booked as three, and `G4`'s unresolved grouping question gets its first market answer |
| **Branch B (they decouple)** | max pairwise spread **≥ 4.00pp** ⇒ each UW needs its own cause, and `EVENT_ALPHA` Card 4's capex explanation for `XLU` becomes separable from the rate explanation |
| **Branch C** | between — disclosed favourite |
| **Band derivation (`C5`, stated)** | 5-session realised sigma, measured on the repaired series: `XLU` **1.89%** · `XLRE` **1.59%** · `XLP` **2.04%**. **4.00pp ≈ 2σ of the widest leg; 1.50pp is below 1σ of any leg** ⇒ both bands sit outside the noise, in opposite directions, and neither is a round number chosen for looks |
| **Implied-move check, stated not smuggled** | `XLU` **±2.88%** (09-11 expiry, K=42.50, **put OI 3,594 vs call OI 22**). ⚠ **No `XLRE` or `XLP` straddle was pulled and none is fabricated (`C3`)** — a 4.00pp *dispersion* among three ETFs cannot be produced by any single implied move, so the implied is reported as context, not as the band's source |
| **State at registration** | `XLU` `exc5` **−0.62pp** · `XLRE` **−1.85pp** · `XLP` **−1.14pp** vs `SPY` ⇒ current max pairwise spread **1.23pp**, i.e. **already inside branch A's line**, which is disclosed so A cannot later be read as a discovery |
| **Anti-signal (VOID)** | a **utility-specific regulatory or single-issuer event** (rate-case decision, major outage, or an announced merger) at ≥2 `XLU` constituents inside the window ⇒ `XLU` moves for a non-duration reason. ⚠ **Base rate checked and NOT remote** — `XLU` is the board's worst sector (10 reds of 15) and distressed sectors are where corporate actions cluster |
| **Information grade (`B4`)** | **HIGH on A.** A says three of the desk's eleven verdicts are one decision — a claim about its own book structure, which is the class `G4` has failed to settle for 11 runs. **B is the modal-adjacent outcome and confirms only that the current bookkeeping is not wrong**, which is worth less. **Stated at registration** |
| **Non-redundancy (`D343`)** | 09-04 carries `S126` and `S134`; 09-11 carries `P108`/`P116`. **`S135` observes a spread among three UW sectors, not a level on any one of them**, and its window sits **between** the two dates rather than on either |
| **Owner** | `industry_US` |

★ **The honest arithmetic of this stage: 4 brackets drafted, 1 registered, 3 withdrawn on ledger
inspection.** That ratio is the point — the 08-29 run's rows were doing their job, and the check that
found this was reading `SCENARIOS_US.md` **before** writing, not after.

⚠ **Lens 2's proposed `XLU` 09-11 bracket was considered and DECLINED**: `XLU`'s 09-11 implied is
**±2.88%** while its 5-session realised sigma is **1.89%**, so any threshold outside implied would sit
at >1.5 sigma — reachable — **but `S135` already tests `XLU` on the same window through a spread that
carries more information** (it tests whether `XLU` is a separate bet at all). One observable, one row.

---

## §3 · LENS 3 — MOMENTUM RE-TAGS · and a challenge to this run's own verdict

Top runners by `rs60` vs `SPY`, re-tagged. **10 of 12 pass the continuation test; the tag is not a
rubber stamp** — two fail:

| ticker | sector | rs60 | rs20 | OBV | `vol_surge` | TAG | flip condition (dated, machine-checkable) |
|---|---|---:|---:|---|---:|---|---|
| `DASH` | DISC | **+51.1** | +17.6 | 매집 | 0.87 | **EXTENDED-BUT-LIVE** | `rs20` < 0 on 2 consecutive settled closes by **09-18**, OR `obv_state` → 분산 |
| `ABNB` | DISC | +39.8 | +22.0 | 매집 | 1.04 | **EXTENDED-BUT-LIVE** | same test, **09-18** |
| `MPC` (held) | ENRG | +36.0 | +13.6 | 매집 | 0.97 | **EXTENDED-BUT-LIVE** | `rs20` < 0 ×2 closes OR `obv` → 분산 by the **09-10** PPI print |
| `SHOP` | IT | +33.4 | **+27.6** | 매집 | 0.62 | **EXTENDED-BUT-LIVE, accelerating** (`rs20` pace > `rs60` pace) | `obv` → 분산 by **09-18** |
| `VLO` | ENRG | +32.7 | +9.6 | 매집 | 0.69 | EXTENDED-BUT-LIVE, **decel flag** (`rs20` is 29% of `rs60`) | `rs20` < 0 OR `obv` → 분산 by **09-18** |
| `CRM` | IT | +32.4 | **+36.3** | 매집 | **1.64** | **EXTENDED-BUT-LIVE**, the set's only volume-confirmed name | `vol_surge` < 1.00 while `rs20` stays > +20 by **09-18** |
| `PANW` | IT | +30.6 | +9.0 | **분산** | 0.86 | 🔴 **EXHAUSTED (early)** — OBV already distributing while `rs60` is still elevated | re-flips only if `obv_state` → 매집/중립 **AND** `rs20` > +15 by **09-02** |
| `CMG` | DISC | +30.3 | **−0.8** | 중립 | 0.69 | 🔴 **EXHAUSTED** — `rs20` already negative | `rs20` > +10 on 2 closes **AND** `obv` → 매집 by **09-18** |
| `PSX` (held) | ENRG | +30.1 | +12.3 | 매집 | 0.79 | **EXTENDED-BUT-LIVE** | `rs20` < 0 OR `obv` → 분산 by **09-18** |
| `AJG` | FIN | +30.1 | +4.3 | 매집 | 0.88 | EXTENDED-BUT-LIVE, **fading** (30.1 → 4.3) | `rs20` < 0 by **09-18** |
| `TMO` | HLTH | +29.2 | +5.3 | 매집 | 0.73 | EXTENDED-BUT-LIVE, fading | `rs20` < 0 by **09-18** |
| `PLTR` | IT | +29.0 | **+48.4** | 매집 | 0.71 | **EXTENDED-BUT-LIVE, re-accelerating hardest of the 12** | `obv` → 분산 by **09-18** |

**ROLL-OVER list** (`rs60` > +15 vs `SPY` with `rs20` < 0) — **20 names, 8 of them Financials, and two
of them are the book's own**: `RTX` (rs60 **+20.7**, rs20 −4.6, OBV 중립) and `MET` (rs60 +17.2,
rs20 −2.6, OBV 중립). ⚠ **`MET` sits in the paper book only** (§0a), so half the flag lands on a
position the real account does not hold — **which is itself the §0a finding biting inside this stage.**

**TURN list** (`rs60` < 0 with `rs20` > +15 — beaten down, now turning): **`MSTR`** (−1.4 / **+33.5**,
매집, `vol_surge` 1.39) · **`LITE`** (−6.6 / **+22.3**, 매집) · **`SNDK`** (−20.9 / **+19.3**, 매집).
🚨 **None is held, none has a standing thesis, and all three sit in IT — a Neutral sector, so no
sector-level trigger sends anyone to look.** **This is the desk's structural blind spot named
precisely: it has no process that starts at a name whose 60-day leg is negative.**

★ **`M1102` — Lens 3 challenges a verdict this run made 30 minutes earlier, and the challenge is
correct on its numbers.** ROTATION demoted **Consumer Discretionary N → UW** on `eqflow` −0.247 and a
42.9% red-rate. **The two largest runners in the entire 299-name universe are both in that sector**
(`DASH` rs60 +51.1, `ABNB` +39.8 vs `SPY`), both still OBV-accumulating, both still positive on
`rs20`. **The demotion is not reversed** — `eqflow` and red-rate are the sector-level instruments the
rule requires and they are unambiguous, and `CMG` (the third DISC runner) is genuinely rolling over,
so this is dispersion, not a hidden bull sector. **But the UW label is now recorded as masking the
board's two best names**, and that is written down rather than resolved by moving the verdict.

---

## §4 · LENS 4 — CYCLE EXPOSURE

**Deterministic check verified and AGREED on all three rows** (`CYCLE_EXPOSURE.md`): AI-compute
epicenter **16.93% ≥ 12.0%** (`NVDA`, `ANET`) · Energy/refining **9.97% ≥ 8.0%** (`MPC`, `PSX`) ·
missile-defense 3.83% (`RTX`, **threshold unset — the guard is disarmed, not passing**). **No GAP.**

**Cycles with NO registry row — what is unmeasurable, not zero:**

| missing cycle | what it hides | cleanest expressions (flow · OBV · rs20 · rs60 vs `SPY`) |
|---|---|---|
| **Optical / photonics** — 🚨 **`D250`, 15th run** | a cycle with no row **cannot produce a GAP flag by construction** | **`LITE` +0.550 · +0.287 매집 · +22.3 · −6.6** · `COHR` +0.324 · +0.121 매집 · +3.2 · **−35.2** |
| **Memory as its own bucket** | `MU` sits inside AI-compute's epicenter list; **`SNDK` and `WDC` are in no list at all** | `MU` +0.346 · +0.126 매집 · +10.3 · −15.6 · `SNDK` +0.358 · +0.100 매집 · **+19.3** · −20.9 · `WDC` **−0.839 🔴분산** · −18.6 · −24.6 |
| **Semiconductor equipment** | a sub-entry of AI-compute, never separately testable | `AMAT` −0.839 🔴 · `KLAC` −0.647 · `LRCX` −0.022 (OBV 매집, rs60 −14.2) |
| **AI-power / grid** | listed only as *adjacent* to AI-compute ⇒ **it can never independently pass or fail a core-exposure test** | `ETN` (held) −0.061 · +0.202 매집 · `VRT` +0.153 · `GEV` −0.640 · `PWR` −0.622 🔴 · `NEE` −0.658 🔴 · `VST` −0.750 🔴 |

★ **`M1103` — and a registry defect the lenses did not reach**: the rank-1 epicenter list names **14
tickers, and `TSM` and `SMCI` are NOT in `us_top300`.** ⇒ **two of the desk's own rank-1 epicenter
names cannot be flow-tagged by any instrument this desk runs.** This is the identical class as the
2026-08-10 `TSM`/`LNG` finding, reappearing on the **registry** axis rather than the book axis.

★ **The sharpest single finding — exposure that is ONE LAYER OFF the epicenter.** The book's
AI-interconnect exposure runs entirely through **`ANET`** (switch hardware, `rs20` **+5.3** vs `SPY`).
The optical modules that go **inside** those switches are **`LITE`**, whose `rs20` is **+22.3** — the
strongest 20-day relative-strength number of any name in this pre-mortem — and which has **no registry
row, no thesis, and no holding**. ⇒ **if the live layer of the interconnect story is optical rather
than switching, the book's credited "epicenter" is itself one layer removed, and the deterministic GAP
check is structurally incapable of seeing it.**

**Is the 🔴 AI-power tape being used to justify a structural zero?** — **No, and the numbers say so.**
The book holds `ETN` (adjacent tier, **3.65%** of total) — one of the two least-bad names in the
complex, still **OBV +0.202 매집** — while adding to none of the four that are actively distributing.
**That is the tape gating ADD timing on the weak names while a small adjacent core is held through the
chop, which is the correct use of the rule.** ⚠ The unresolved item is architectural: **AI-power has
no epicenter tier at all**, so "0% core in AI-power" is not a statement this desk's instruments can
even make. Registered as **`D416`**.

---

## §5 · Injection — what changes

### DEEP set updated: a 5th slot is PROMOTED

**Final DEEP set (5): continuous=[`MATR`, `HLTH`] · rotating=[`FIN`, `COMM`] · ★ PREMORTEM-PROMOTED=[`IT`]**

**`IT` is promoted** (Lens 1 rank 1, and ROTATION explicitly routed it here rather than to a slot).
Mandate, stated so DEEP cannot drift: **the sector's only three accelerating names are all software
(`CRM`, `INTU`, `MSTR`) while `SMH`'s `exc60` is −15.31pp vs `SPY` and `AVGO` — a book position —
prints in 3 sessions with a ±8.09% implied move.** The question is whether IT is one sector or two.
⚠ **`ENRG` was the other PROMOTE candidate and is DECLINED with its reason**: its bull case rests on
separating refining margin from the barrel, and `R89`+`P83` say the desk has no surviving instrument
that does. **Logged as within-run watch, not dropped.**

### Handed to ALPHA (action brackets)
- **`S135`** — registered this run (duration-basket dispersion, settles **2026-09-11**).
- **Already armed and inherited, not re-issued**: **`S131`** (MSCI **08-31**, the ≤48h obligation) ·
  **`S132`** + **`S127`** (`AVGO` 09-02) · **`S126`** + **`P114`** (NFP 09-04) · **`P116`** (CPI 09-11
  credit leg) · **`P107`/`P112`/`P117`** (Hormuz).
- **Declared non-brackets, with reasons** (so an absence stays legible):
  **Aug PPI 09-10** — dropped on information grade (`B4`): it is a nowcast update to the CPI print one
  day later, and neither branch would change a verdict `P116` does not already carry. **3rd run
  unbracketed — now BY DECISION, not by omission.**
  **Hormuz (undated)** — already spanned three ways; a fourth is `D343`.
  **`HPE` 09-03** — deferred to the `IT` DEEP by the 08-29 precedent, renewed today with its numbers.

### Handed to BET (epicenter starters, analytical only — no sizing here)
- **Optical, the unmeasurable cycle**: `LITE` · `COHR` — with `D250` attached (15th run).
- **Memory producers vs equipment split**: `MU` · `SNDK` accumulating against `WDC`/`AMAT` distributing
  — ⚠ but `MU`/`SNDK`/`WDC` are `P111`'s registered observable, so they are **withheld from BET to
  keep that test out-of-sample** (`S4`).
- 🚨 **`T` and `CBRE` — held in the real account, owned by no thesis** (§0a). **This is a
  reconciliation item, not a candidate.**

### Handed back to HANDOVER (writeback)
`D415` (two books, never reconciled) · `D416` (AI-power has no epicenter tier) · `M1098`–`M1103`.

---

## ✅ EXIT CHECK
- [x] **4 lenses fanned out in parallel, one message**; each returned named tickers + dated catalysts. **Every number re-verified against the JSON before use**, and **one lens diagnosis was refuted and recorded** (§0b).
- [x] **Every registered bracket names its observable + frozen threshold + date and carries BOTH branches** — **`S135`**, the one row registered. ⚠ **Three drafted brackets were WITHDRAWN on ledger inspection** (MSCI → `S131`; `AVGO` → `S132`+`S127`; `HPE` → deferred to the IT DEEP by the 08-29 precedent) and **two events are declared non-brackets with stated reasons** (PPI 09-10 on information grade; Hormuz as already triple-spanned). **None is a silent omission, and the ≤48h obligation is satisfied by the armed `S131`, not by a new row.** Registration into `handoff/SCENARIOS_US.md` + the `SCENARIOS.md` MASTER INDEX is done in the writeback step.
- [x] **Every magnitude threshold is stated against the implied move** — `AVGO` ±9.50% vs implied **±8.09%** · `HPE` ±12.50% vs **±11.23%** · `S135`'s 1.50/4.00pp vs the legs' 1.59–2.04% 5-session realised sigma. **A move inside the implied is pre-declared NO-INFORMATION**, not narrated as a trigger. ★ **`D295` closed after 5 runs** — the straddle chain spanning the 09-02 print was read directly.
- [x] **Each branch graded by information content**; the one binary where neither branch would change a conclusion (**PPI 09-10**) is **dropped with that reason stated**, and the bracket spent on `S135` instead.
- [x] `BLINDSPOT_PREMORTEM.md` written — legs · brackets · re-tags · cycle GAP.
- [x] **Every catalyst-bearing leg promoted or logged**: IT **promoted to a 5th DEEP**; ENRG **declined with its reason**; INDU-services and DISC-travel logged as within-run watch.
- [x] **DEEP set updated and stated**: continuous=[MATR, HLTH] · rotating=[FIN, COMM] · promoted=[IT] — **5 slots**.
