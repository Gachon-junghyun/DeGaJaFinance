# SECTOR_DEEP_MATR — Materials · 2026-08-10 (Mon) · settled 2026-08-07

> ROTATING track. Covered 08-08 (two runs ago) — recency filter deliberately broken because **S57
> settles 2026-08-12** and its carrier's driver was disclosed THIS MORNING. **Lead with the delta.**
> Zero buy/sell language, zero sizing (P4). Benchmark named on every relative number (C1). Both halves
> of every print (C2). Market is OPEN — price pulls filtered `<= 2026-08-07` or tagged `[live]`.

## §0 · THE DELTA — Newmont pays Barrick $1.95bn, and S57-ANNEX-2 registers it

**`S57` branch A**: XLB 5-session excess vs **SPY** > **+1.9**, any settled close through **2026-08-12**.
Reading today: **+1.307** — **0.593pp away.** Measured over the trailing 60 settled sessions
(desk figure, carried): mean **−0.316**, sd **2.284** ⇒ the gap is **0.26σ** — a hair outside the
desk's own "inevitable" (<0.25σ) class, and **XLB's own 08-14 option-implied move is ±2.1%** — roughly
**3.6× the size of the gap the bracket is measuring.**

**NEM alone is ~85% of that observable.** NEM's 5-session excess vs SPY is **+17.05pp — the MAXIMUM of
its own trailing 60 sessions, +3.32σ above that window's mean.** This is not a Materials reading; it is
one stock at a career-extreme print sitting inside a sector-ETF number.

### 0a. ★★★ The driver, from the issuer, this morning — and the WSJ headline gets the cash direction backwards

`[globenewswire press release + nasdaq body + wsj + mining, 2026-08-10]`:

- Newmont and Barrick **settled all outstanding Nevada Gold Mines joint-venture disputes.**
- **NEWMONT WILL PAY BARRICK $1.95 BILLION.**
- Newmont **formally consented to Barrick's proposed IPO of its North American gold assets.**
- Newmont's **Fiberline** and **Mike** developments, and Barrick's **Fourmile** development, go into
  the JV.

⚠⚠ **The WSJ headline — *"Barrick Mining Settles Newmont Nevada Dispute for $1.95 Billion"* — reads as
Barrick paying. The body says Newmont pays Barrick.** Verified against the primary release, not the
headline. **Cross-check (D5)**: the nasdaq body's Friday closes (NEM +7.16%, Barrick +5.58%) reproduce
this run's own yfinance settles to two decimals — **two independent sources agree.**

**Checked and not found**: `python -X utf8 -m module_disclosure_us NEM` (36 filings, trailing 90 days)
returns **zero** items in the M&A/JV category as of this run — the only Item-2.02/7.01 filings on file
predate the deal by weeks, and the 23 Form-4s are routine insider transactions through 08-07. **No 8-K
for the settlement has hit EDGAR yet.** This is a timing gap, not a contradiction (a same-day press
release routinely precedes the 8-K by 1–4 business days) — **flagged as a KPI: the 8-K's actual terms
should confirm the $1.95bn figure and the IPO-consent language when it files.**

### 0b. ★★★ The momentum shape says the print is not a trend, before the deal is even priced in

| | Value |
|---|---|
| NEM 60-day excess vs SPY | **−10.36pp** |
| NEM last-20-session excess vs SPY | **+16.14pp** |
| ⇒ 21–60-day base | **−26.50pp** |
| Revision breadth, current-FY | **1↑ / 9↓** |
| FY EPS estimate, 90d | **−8.8%** |
| FINRA short-vol z | **+1.30, BUILDING** |
| Ledger status | **🔴RESOLVED, filed; recheck 2026-08-13** |

Lens 3 (PREMORTEM §3) tags NEM **EXHAUSTED** on exactly this shape — a positive 60-day number entirely
manufactured in the last 20 sessions on a negative 21–60-day base, stacked against analysts cutting
numbers 9-to-1 while the tape rallies. **A $1.95bn cash outflow and an IPO consent for a competitor's
carve-out are not, on their face, reasons to raise those estimates.**

### 0c. ★★★ Independent recompute of the ex-NEM falsifier — method stated, and it brackets the SSGA-based prior

**P44's registered falsifier**: XLB's ex-NEM excess turning positive on a settled close. 08-08's DEEP
computed this from **SSGA's dated XLB holdings file (25 names)**, getting **+0.194**. This run did not
re-fetch that file (not reachable in the time available); instead a **second, independent method** was
run to cross-check the direction, and the method is stated rather than implied:

**Method**: mcap-weighted proxy basket restricted to the **12 names in this run's own Materials
universe** (`SECTOR_FLOW_US.json`), yfinance settled closes (`auto_adjust=False`), 07-31 close →
08-07 close (5 sessions), benchmarked to **SPY**.

| Quantity | Result |
|---|---|
| SPY 5-session % | +3.511% |
| XLB 5-session %, actual | +4.819% → **excess +1.307** (reproduces the desk's own number exactly — data pipeline cross-validated) |
| NEM 5-session excess, self-computed | **+17.052** (reproduces the desk's +17.05 to three decimals) |
| 12-name mcap-weighted proxy basket, ALL | **excess +2.966** |
| 12-name mcap-weighted proxy basket, **EX-NEM** (reweighted to 100%) | **excess +1.123** |

**The proxy's full-basket number (+2.966) does not match XLB's actual (+1.307)** — the true ETF holds
~25 names and this proxy holds 12, so the ~13+ smaller-cap names absent from this universe are pulling
the real fund down by roughly 1.66pp of weighted return, which is consistent in direction with why the
SSGA-based ex-NEM figure (+0.194) sits below this proxy's ex-NEM figure (+1.123): **this proxy most
likely overstates the true ex-NEM reading**, because it is missing exactly the drag names the 08-08
recompute captured.

⇒ **Even on the more generous of the two independent measurements, ex-NEM sits at +1.123 — still
0.777pp short of the +1.9 fire line, and the more rigorous prior measurement (+0.194) is 1.706pp
short.** Both bracket the same conclusion from different methods: **the ex-NEM basket does not clear
its own falsifier, and it is not close.**

**Verdict: S57-ANNEX is not re-frozen. It is extended — this run's registration is `S57-ANNEX-2`
(BLINDSPOT_PREMORTEM §7) — with a named, dated, primary-sourced driver that a headline-only read would
have gotten backwards.**

---

## §1 · The value chain, node by node — binding constraints, sub-node dispersion stated

12 names, **0 green of 12** (breadth), settled 08-07. No news-velocity axis this run (sweep dead,
`vel_coverage 0.0`) — where velocity is cited below it is `module_flow`'s **live** read, named as such
and never substituted for the settled sweep number (D208 discipline).

| # | Node | Names (cap) | Binding constraint | Sub-node dispersion (settled, vs SPY) |
|---|---|---|---|---|
| 1 | **Precious-metals mining** | NEM ($110.8B) | **A dated JV/M&A cash event, not a gold-price or materials-cycle mechanism** (§0). Estimate credibility separately cut 9-to-1 | 🟡 +0.476, OBV 매집 +0.087, RS20 **+16.1**, RS60 **−10.4** |
| 2 | **Industrial gases** | **LIN ($236.8B, 24.7% of sector cap)**, APD ($62.4B), ECL ($75.7B) | LIN and APD are diversified across healthcare/chemicals/manufacturing/metals-mining/food/electronics (10-K, `module_business_us`) — **breadth means no single sector catalyst reaches them**, and neither is participating in whatever lifted the rest of the group | LIN 🔴 **−0.683**, OBV 분산 −0.297, RS20 **−9.9**, RS60 −7.5 · APD 🟡 +0.114, RS20 −1.1 · ECL 🟡 +0.301, OBV 매집 +0.168, RS20 +1.5 — **the pair (LIN, APD) diverges from ECL inside one "gases" label** |
| 3 | **Copper / industrial metals** | FCX ($98.7B) | **Positioning, not physical supply**: CFTC COT spec long 100th %ile of the trailing year, still BUILDING (+9,842 wk), while FCX's own equity OBV is 중립 — the futures market is more committed than the equity tape | 🟡 +0.130, OBV 중립 −0.071, RS20 **+10.7**, RS60 +0.7 |
| 4 | **Coatings** | SHW ($79.1B) | Best settled flow score in the sector — no binding constraint identified against it this run | 🟡 +0.572, OBV 매집 +0.196, RS20 +8.3, RS60 +13.9 |
| 5 | **Aggregates / construction materials** | CRH ($74.3B), VMC ($39.3B), MLM ($36.6B) | A data-centre / non-residential construction demand story with **no flow confirmation**: VMC and MLM are the two worst flow scores in the entire 12-name universe | CRH 🟡 −0.173, RS20 −6.5 · VMC 🔴 **−0.599**, OBV 분산 −0.149, RS20 −6.0 · MLM 🔴 **−0.668**, OBV 분산 −0.187, RS20 −7.5 |
| 6 | **Steel** | NUE ($55.5B), STLD ($36.0B) | A **detection-gate** constraint on the desk's own instrument, not a fundamental one (§2.1) — `vol_surge` sits just under the 1.2 gate on both names | NUE 🟡 +0.639, OBV 매집 +0.611, RS20 **+17.5**, RS60 **+13.9** · STLD 🟡 +0.611, OBV 매집 +0.396, RS20 +12.5, RS60 +8.0 — **the two strongest OBV prints in the sector, both trapped 🟡 by one axis** |
| 7 | **Ag chemicals** | CTVA ($52.6B) | Segment pricing pressure (Crop Protection −2% y/y, LatAm/APAC) plus a planned Q4 2026 Vylor spin-off overhang | 🟡 −0.235, OBV 중립 −0.062, RS20 **−12.8**, RS60 −11.7 — **the worst RS20 in the sector after excluding LIN/VMC/MLM's 🔴 reads** |

**D208 check, done and clean for this sector**: `module_flow` (live, run today) and the sweep JSON
(settled 08-07) were compared name-by-name for NEM, FCX and LIN — **all three agree in OBV state**
(매집/매집, 중립/중립, 분산/분산). **No sign flip inside Materials this run.** The two `D208` sign-flip
instances this run are outside the sector — **MPC and PRU** (PREMORTEM §3e) — named for the record,
not imported here.

---

## §2 · Assignments

### 2.1 · Steel — carried forward, mechanically unchanged

**`vol_surge`: NUE 0.95, STLD 0.90 — identical to 08-08.** Neither has crossed the 1.2 gate; the
🟡-not-🟢 read remains a detection-gate artifact, not new information (see §1, node 6, and 08-08's
DEEP for the backlog/tariff evidence, not repeated here since nothing has moved).

### 2.2 · ★★ L2 peak-margin / low-multiple table — re-verified this run, `scripts/margin_history.py`

**Re-run against SEC XBRL for all seven names.** Every FY2025 gross-margin figure and every percentile
**reproduced exactly** — the annual data has not moved since 08-08, so the percentile column is
unchanged; **forward P/E is refreshed to today's live price** (`module_fundamentals_us --no-xbrl`,
`[live]`), and **EV/EBITDA is carried forward from 08-08 (not re-measured this run — no fast source for
it was available in the time budget; flagged rather than silently reused)**.

| Ticker | Fwd P/E `[live 08-10]` | EV/EBITDA `[carried, 08-08]` | FY2025 gross margin | Percentile in own history | Read |
|---|---|---|---|---|---|
| **NEM** | 10.84 | 6.79 | `[unavailable]` | `[unavailable]` | `margin_history.py` still returns "no annual data" — **NEM's XBRL gross-margin tag does not resolve.** Tooling gap, not skipped |
| **FCX** | 17.04 | 12.39 | 26.1% | **46.7%** (n=15) | Mid-range margin, elevated-for-FCX multiple — not a trap, not statistically cheap |
| **NUE** | 14.62 | 11.93 | 11.9% | **52.6%** (n=19) | Median margin; the +57% backlog build is a forward bet the multiple has started to price |
| **STLD** | 14.10 | 15.48 | 13.2% | **42.1%** (n=19) | Below-median margin, richest EV/EBITDA of the group |
| **DOW** | 16.18 | 9.56 | 6.3% | **12.5%** (n=8) — **literal minimum of its own 8-year window** | **Not cheap** at 16.2× forward on the lowest gross margin Dow has printed as a public company — pricing a recovery that has not appeared |
| **LYB** | 9.47 | 8.70 | 8.5% | **6.7%** (n=15) — **literal 15-year minimum** | The multiple **is** cheap (9.5×) against a genuine trough — the countercyclical setup, a different object from DOW's more expensive version of the same trough |
| **CF** | 10.85 | 5.58 | 38.5% | **78.9%** (n=19) — **near-peak** | ★★★ **The textbook L2 trap, unchanged**: a cheap-looking multiple on a margin in its own top quintile. Forward P/E moved 10.42 → 10.85 since 08-08 (price recovering off the 08-05 miss) while the margin percentile that makes it a trap has not moved at all |

⇒ **Nothing in this table flipped in two sessions.** The two trough names (DOW, LYB) and the one peak
name (CF) are exactly where they were 08-08 — the delta this run is confirmation, not new information,
and that is itself informative: **the margin cycle moves on quarters, the price moves daily; conflating
the two is the trap this table exists to catch.**

### 2.3 · ★★★ The dollar leg (P44/P45) — the only non-NEM mechanism, and it is genuinely contested

If S57 branch A fires on a real sector leg rather than on NEM alone, the desk's own analysis (P44
direction B) names **the dollar** as the one candidate mechanism — precious/industrial metals pricing
in a weaker USD, independent of the NEM-specific JV cash event.

| Instrument | Reading | asof |
|---|---|---|
| UUP | **−0.35%/5d, −1.13%/20d** | settled 08-07 |
| FXY | +1.01%/5d, **+2.64%/20d** | settled 08-07 |
| FXE | +0.18%/5d, **+1.31%/20d** | settled 08-07 |
| CFTC COT, USD Index | **81st percentile, ADDED +5,302** | ⚠ **Tuesday 08-04 snapshot — pre-dates the 08-07 payroll print** |
| CFTC COT, Copper | **100th percentile of the trailing year, ADDED +9,842** | Tuesday 08-04 snapshot |
| `DTWEXBGS` (broad trade-weighted USD, the desk's own series) | 🚨 **last printed 2026-07-31 — six publication days stale** | — |

UUP, FXY and FXE **agree in sign** on dollar weakness (D5) — a real, if modest, directional read. But
the COT positioning behind it is **already crowded (81st percentile) and still building**, on a
snapshot that **predates the one print (NFP) that would tell you whether that crowd is right.**

⚠⚠ **Object discipline (D1/D2), stated explicitly because the two are easy to conflate**: **UUP is a
DXY-basket proxy; `DTWEXBGS` is the BROAD trade-weighted index.** They measure related but different
baskets. **No UUP value is substituted for a `DTWEXBGS` value anywhere in this file**, and `DTWEXBGS`'s
six-day staleness means the broad measure simply has no fresh read to offer — UUP is carrying the
entire dollar-leg argument by default, not by choice.

**Mandatory anti-signal, both directions** (inherited from P44/P45, restated for Materials):
(a) if UUP rises while the COT long keeps building, the crowded-long-unwind story is wrong and the
dollar leg does not support a sector read; (b) if the dollar falls **and** copper's 100th-percentile
long unwinds together, this is **one** positioning event (USD and copper positioning moving as a single
trade), not two independent legs — P44 and P45 collapse into a single claim if that happens.

### 2.4 · ★★ `top1_flips_sign` — Materials may not be called on its cap-weighted aggregate

`SECTOR_FLOW_US.json §sector_rotation`: **Materials is the only sector of 11** where removing the
largest name flips the sign of the sector's flow number.

| Metric | Value |
|---|---|
| `wflow` (cap-weighted, all 12 names) | **−0.038** |
| `wflow` ex-top1 (LIN removed, reweighted) | **+0.173** |
| Top1 | **LIN**, 24.7% of sector cap |
| `eqflow` (equal-weighted, all 12 names) | **+0.040** |
| Breadth | **0🟢 / 12** |
| n | 12 |

**The non-cap-weighted read disagrees with itself in sign**: `eqflow` is positive (+0.040) while
breadth is flat-zero-green. Neither substitutes cleanly for the barred cap-weighted number, and this
file does not pick one to make a cleaner story. ⇒ **ROTATION is barred from promoting or demoting
Materials on `wflow` today** (ROTATION §2b), and this DEEP file's own §0–§2 verdicts are built entirely
from name-level and primary-source evidence for exactly that reason — **the sector aggregate cannot be
trusted regardless of which way it points.**

---

## §3 · Chain-hop candidates — body-proximate only, carried and re-checked

`module_news_data chain-hop` was non-responsive to the two named cross-sector chains on 08-08 (returned
an unrelated theme both times, >150s each) and was **not re-run this run** — no new tool defect was
introduced by skipping a call already logged as non-responsive; re-attempting it would not have produced
body-proximate evidence either way. Falling back again to the flow-JSON cross-check:

- **AI → power → transformers → copper (FCX).** FCX settled 🟡중립 (flow score +0.130, RS20 +10.7,
  RS60 +0.7), unchanged from 08-08 (byte-identical bar, §2.4's Materials-has-zero-top-50-names
  structural note applies) — **the composite 🟡중립 tag itself, not the OBV component alone (D6), is
  what contradicts a "money is flowing into copper" read: a flat-to-neutral composite sitting against
  a 100th-percentile, still-building futures long is the mismatch**, OBV is one of the four axes behind
  that tag and is named here only as an ingredient, not as the evidence. No flip since 08-08.
- **Texas data-centre build → cement/aggregates (VMC, MLM).** Both still 🔴 (VMC −0.599, MLM −0.668) —
  **the two worst flow scores in the 12-name universe**, unchanged from 08-08. No flow confirmation of
  this chain has appeared in two runs.

**No Materials chain-hop candidate reached BET-eligibility this run** — same conclusion as 08-08, and
for a structural reason: Materials, Real Estate and Utilities are the three sectors with **zero names
in the mcap top-50**, so their sweep-level readings cannot move on this bar regardless of how many times
the run repeats (`SECTOR_ROTATION.md §2d`). **Everything of value in this file came from primary
sources and name-level work, not from re-reading the sweep.**

---

## §4 · Track-KPIs and anti-signals — dated observables

| # | Observable | Reads today | Falsifies / confirms |
|---|---|---|---|
| 1 | **S57 branch A**: XLB 5-session excess vs SPY > +1.9, ANY settled close through **08-12** | **+1.307** (0.593pp away, 0.26σ of its own 60-session sigma) | If it fires, read it through §0c's ex-NEM bracket [+0.194, +1.123] BEFORE treating it as a Materials call |
| 2 | **XLB ex-NEM, on a settled close** (P44's registered falsifier) | Bracketed **+0.194 (SSGA-based, 08-08) to +1.123 (12-name proxy, this run, likely an overstatement)** | Either measurement turning positive and holding = the first evidence of a real sector leg |
| 3 | **Newmont's 8-K for the Nevada JV settlement, on EDGAR** | 🚫 **not yet filed** (checked `module_disclosure_us`, 36 filings, none in the M&A category) | The 8-K's actual terms should confirm the $1.95bn figure and the IPO-consent language — track for confirmation, not contradiction |
| 4 | **NEM 30d revision breadth turning net-positive**, or gold giving back the print | **1↑/9↓ current-FY, EPS −8.8%/90d**; short-vol z **+1.30 and BUILDING** | Either failing while price holds = the exhaustion case (Lens 3) materialising |
| 5 | **Copper COT next Tuesday close (08-11, published 08-14)** | **100th %ile, +9,842 wk, still building** | A pullback from the yearly max = the first sign the crowded-long leg is capping, not confirming |
| 6 | **USD COT next print**, and whether it pre- or post-dates NFP | **81st %ile, +5,302, Tuesday-08-04 snapshot — pre-NFP** | A build that survives the NFP-inclusive print supports P44 direction B; a reversal kills it |
| 7 | **`DTWEXBGS` on next print** | 🚨 stale since **2026-07-31** | UUP is carrying the entire dollar-leg argument alone until this prints — no UUP value substitutes for it (D1/D2) |
| 8 | **NUE / STLD `vol_surge` crossing 1.2** | 0.95 / 0.90 — unchanged since 08-08 | A mechanical flip to 🟢 on an unchanged fundamental picture = a detection-lag event, not new information |
| 9 | **VMC / MLM flow score** | −0.599 / −0.668, both 🔴, unchanged since 08-08 | A flip to 🟡/🟢 alongside continued Texas data-centre headlines = the first flow confirmation of the aggregates leg |
| 10 | **XLB / NEM 08-14 option-implied moves (D4)** | **XLB ±2.1%**, **NEM ±5.0%** | Any branch-A fire, or any NEM move, inside these bands is LOW-INFORMATION until a subsequent session extends beyond them |
| 11 | **NEM short interest** | **2.2% of float, BUILDING**, DTC 2.3 | A further build alongside the 9-to-1 revision cut = the market pricing the exhaustion case even as the tape holds |

**No position sizing and no buy/sell language appears anywhere in this file (P4).**
