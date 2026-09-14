# DEEP ① · ENRG — 2026-07-24 (Fri) ★US-only · **CONTINUOUS TRACK · NARROWED TO THE REFINING NODE**

> Stage 7 / L1·DEEP. `--market us`, news `--scope foreign`. **Zero buy/sell, zero sizing.** Analytical only.
> **Benchmark for every relative figure in this file: SPY.** Named inline anyway (C1).
> **Run clock — the US regular session was OPEN at pull time (09:59–10:0x ET).** Every 2026-07-24 print
> below (futures and equity) is an **incomplete bar** and is labeled as such at each appearance.
> **Settled closes only** is now a binding rule on this file, not a preference (R17 / D48).
> **Carried by reference, NOT re-printed:** `llm_outputs/2026-07-23/industry_US/SECTOR_DEEP_ENRG.md`
> — the full value-chain map, the Bab el-Mandeb / Hormuz node, the services and midstream nodes, the
> tanker leg (§1c, still `indistinguishable`, the tonne-mile KPI is still unmeasurable here), and the
> chain-hop ledger (§5, zero promoted, now a **seventh** consecutive run — no re-sweep run today).
> This file writes **only the refining node and only what moved.**

---

## §0 · DELTA-FIRST VERDICT

**The mandate's own separator flipped sides overnight, and the reason is a data artifact, not a market event.**

1. ★★ **R17 is not a footnote — it removes the entire evidentiary basis of yesterday's deep-dive verdict.**
   Yesterday this file wrote that the crack "plunged −11.2%" and built §0(2), §1(b), §4 and KPI #1 on it.
   On settled closes the move was **−0.56%** (66.865 → 66.492) and the level sits at the **89th percentile
   of 90 days**. Everything yesterday inferred from the magnitude is withdrawn; only the *direction* of
   the product decomposition survives — and it survives **stronger**, on a settled weekly series (§3).
2. ★ **A SECOND claim from yesterday's file dies on the same settled data, and is proposed for retraction
   here.** Yesterday's KPI #1 said the week-to-date crack mean was **65.95**, *"the first negative weekly
   Δ in the entire series."* On settled closes the week 07-20→07-23 mean is **67.73 against 67.65 the prior
   week = +0.12% WoW — POSITIVE, not negative** — and the same settled window (2026-04-01→07-23) contains
   **five** prior negative weekly deltas, so "first in the entire series" was false on the window as well
   as on the sign. **Proposed as R17-b** (§7).
3. ★★ **Mandate (a) — the separator is answerable and I answer it: on every settled series available this
   run, this is MARGIN, not war premium.** Three independent legs, none of them the futures strip: a
   supermajor's own disclosed realized refining margin for the exact quarter in question, an EIA
   utilization/inventory print, and the weekly settled distillate crack. **§2(a).**
4. ★★ **Mandate (b) — the FINRA z-spread between MPC (−3.29) and XOM (+3.13) is substantially a
   BASELINE artifact and must not be read as positioning.** Measured this run at four different lookbacks:
   MPC's own 10/20/30/60-day baseline short-volume share is **53.9–57.1%**, chronically **~10–13pp above
   the tool's own stated 40–45% normal band**, so a single day at 36.4% produces a large negative z from
   an abnormal *denominator*. **PSX printed the identical 36.4% on the identical day and scored z −0.25**,
   because PSX's baseline is 39.0%. Same number, opposite tag. **§2(b).**
5. ★ **Mandate (c) — VLO's 07-30 print is pre-registered with a hard, checkable number**: consensus
   **EPS $10.127 on revenue $38.429B** requires VLO's gross margin to go from **6.30% (Q1'26, its own
   5-quarter maximum) to ~12.6%** — a doubling. **§2(c).**
6. ★★ **New measurement that undercuts the desk's own C4 counter at the root** (§8): over 535 sessions the
   3-2-1 crack and the refiners' SPY-residual returns are correlated **same-day only** (VLO +0.301,
   MPC +0.238, PSX +0.219); **every lead and lag from −4 to +4 days is inside ±0.07, i.e. indistinguishable
   from zero.** At r=0.30 the probability that crack and equity disagree in sign on a random day is
   **≈40%**, so a 3-session "detachment streak" occurs by chance **≈6.5%** of the time. **The C4 counter is
   measuring noise at the sample size it has been run at.**
7. ★ **W5 fires harder than on any prior run**: over 60 sessions the refining-minus-crude spread is
   **+27.27pp** while XLE's own move is **+4.60%** — the intra-sector spread is **5.93×** the sector's own
   move. **"Energy" is the wrong unit, and this run can put a ratio on it. §6.**

**One-line verdict**: *the refining margin is real and is being paid in cash by identifiable third parties;
what remains unresolved is not whether the margin exists but whether the second derivative has already
rolled over — and on the settled weekly series it has (§3).*

---

## §1 · What changed since 2026-07-23

| # | Change | Settled evidence | Where |
|---|---|---|---|
| 1 | **R17 filed** — the −11.2% crack collapse was an incomplete-bar artifact | 66.865 → **66.492 = −0.56%**, 89th pctile of 90d (90d range 41.14–69.45) | MACRO §D-P4 / §G |
| 2 | **The artifact is reproducible and is refused again today** | 07-24 pre-open computed 58.58 (mandate) → 58.21 at my 09:59 ET pull. Futures volume on the 07-24 bar is **19,456 (RB) vs 27,662 settled 07-23** — an unfinished session, refused | this file, §3 |
| 3 | **The product decomposition survives R17 and is confirmed on a weekly settled series** | diesel-minus-gasoline gap by weekly mean: **9.39 → 11.66 → 19.31 → 29.48 → 31.81** over five settled weeks | §3 |
| 4 | **A third-party REALIZED refining margin for Q2'26 landed on 07-23** | TotalEnergies Q2'26: European Refining Margin Marker **$12.4/bbl, +19% QoQ**, vs **$4.3/bbl in 1H2025**; adjusted net income **$6.0B, +12% QoQ and +68% YoY** | §2(a) |
| 5 | **R8 re-checked and HOLDS a third consecutive run** | Forward P/E pulled today: **MPC 10.71 < PSX 11.02 < VLO 12.27**. PSX is not the cheapest | §4 |
| 6 | **VLO's `margin_history` gap is confirmed, and partially routed around** | `scripts/margin_history.py VLO` → *"연간 데이터 없음"*. Quarterly XBRL/yfinance works and is used instead | §4 |
| 7 | **VLO's Item 1A risk-factor extraction FAILED** (`module_business_us VLO --json` returns `risk_factors: ""`, `risk_summary_bullets: []`, legacy-parser fallback on accession 0001628280-26-011499). **PSX's Item 1A extracted cleanly and is used as the anti-signal source instead** | §7 |
| 8 | **UPS remains the only unread W4 customer**, prints **2026-07-28** (S20) | §5 |

**Unchanged and deliberately not re-argued**: the value-chain map, the tanker leg, the chain-hop ledger,
the "no EIA module in this repo" gap, and the absence of a Singapore/Dubai margin cross-check — all
carried verbatim from the 07-23 file.

---

## §2 · The three mandate questions

### (a) Is the settled crack margin, or war premium? — **MARGIN, on three independent non-futures legs. S8's separator is answerable and I answer it.**

S8's registered separator is *"crude falls but cracks hold"* (branch B) versus *"crude falls AND the diesel
crack rolls over"* (branch A). That test needs a crude decline that has not happened, so S8 cannot be
scored on its own terms today. **What this run can do instead is attack the premium reading directly with
evidence that does not come from the futures strip at all** — because a war premium lives in the strip,
while a margin lives in someone's income statement and in physical operating rates.

**Leg 1 — a supermajor booked the margin as realized cash, for the exact quarter in question.**
TotalEnergies reported Q2 2026 on 2026-07-23: adjusted net income **$6.0B**, **+12% QoQ** and **+68% YoY**,
with the company's **European Refining Margin Marker at $12.4/bbl, +19% QoQ**, against **$4.3/bbl for
1H2025**. Equinor reported a **+93% YoY** Q2 profit surge the day before. `[measured, primary company
disclosure via news bodies, --scope foreign]`. **This is a realized, audited-basis quarterly refining
margin, not a strip.** A war premium in a futures curve does not appear as +19% QoQ on a European
refiner's own realized margin marker.

**Leg 2 — the physical operating rate is at the ceiling, which is the opposite of a premium signature.**
EIA week ended 2026-07-17: **US refinery utilization 96.2%, up from 94.7% the same week of 2025**;
**PADD2 and PADD4 at 100%**. US commercial crude stocks **6% below the 5-year average**; Cushing and the
SPR at multi-year and four-decade lows. US wholesale diesel futures **+26% month-to-date in July**
(FT-compiled). `[measured, EIA via news bodies]`. A war *premium* is a price paid for feared future
scarcity while physical throughput is normal; **a margin is what you earn when you are physically
sold out.** 96.2% with two PADDs at 100% is the second picture.

**Leg 3 — the settled weekly distillate crack is still rising while the composite has flattened.**
Weekly settled means (§3): the distillate-only crack **56.42 → 61.91 → 67.63 → 74.81 → 87.30 → 88.94**
over six weeks, and the diesel-minus-gasoline gap **10.78 → 9.39 → 11.66 → 19.31 → 29.48 → 31.81**.
The named binding constraint — Atlantic-basin middle-distillate conversion — is **tightening on settled
data across six weeks**, not on one intraday bar. Named supply-side causes in the same window: Russia's
diesel export ban, Asian throughput schedules upended by re-escalation.

**⚠ What this does NOT establish, stated plainly.** It does not establish that the margin *persists*. The
same news window contains the mechanism that ends it, and **PSX's own 10-K Item 1A names that mechanism
before any of us did** — its first-listed margin risk factors are *"production levels of refined products
by competitors"* and *"import and export capabilities."* Measured against that: **India is on track to
export 1.55 million bpd of light and middle distillates in July, versus 866,000 bpd in May — nearly
double sequentially, and the second-highest month in Kpler's series back to 2017** (`[measured]`, Kpler
via Reuters). **That is the competitor supply response the filing warns about, already in motion.**
So the honest state is: **the margin is real now (three legs), and the documented mechanism for ending it
is already running (one leg, quantified).** Those are compatible, and the question of *which wins* is a
rate-of-change question, which is §3.

**Verdict on (a): MARGIN — established on realized third-party P&L, physical utilization and the settled
weekly distillate series. The premium reading is not "rejected"; it is no longer needed to explain
anything on the tape (C4 language: the two are no longer `indistinguishable` on these three legs, because
the premium reading makes no prediction that any of them confirms).**

### (b) Why does MPC carry FINRA z −3.29 while XOM carries z +3.13? — **Mostly a baseline artifact. This is not a positioning signal and must not be carried as one.**

Re-measured this run at four baseline lengths (`scripts/us_flow.py`, FINRA Reg SHO daily short-volume
ratio, asof 2026-07-23):

| Ticker | short% (07-23) | base @10d | base @20d | base @30d | base @60d | z@10d | z@20d(default) | z@30d | z@60d | 5v5 trend |
|---|---|---|---|---|---|---|---|---|---|---|
| **MPC** | **36.4%** | 54.0% | (mandate: z −3.29) | **57.1%** | 53.9% | **−2.74** | **−3.29** | **−2.75** | **−1.71** | **+3.9 ▲** |
| **XOM** | **58.9%** | 41.8% | (mandate: z +3.13) | **41.1%** | 45.7% | **+2.42** | **+3.13** | **+2.54** | **+1.55** | **+8.4 ▲** |
| VLO | 45.2% | 43.8% | — | 44.5% | 46.3% | +0.21 | +0.38 | +0.11 | −0.16 | −2.2 ▼ |
| PSX | **36.4%** | 37.2% | — | 39.0% | 43.9% | −0.07 | −0.33 | −0.25 | −0.75 | +11.3 ▲ |

**Three findings, in order of how much they should change the desk's reading:**

**(i) ★★ The decisive one. MPC and PSX printed the IDENTICAL short-volume share on the identical day —
36.4% — and were tagged "strongest short-covering read on the board" and "normal range" respectively.**
The entire difference is the denominator: MPC's own baseline is **53.9–57.1%**, PSX's is **37.2–43.9%**.
A statistic that assigns opposite labels to identical readings is describing the baseline, not the day.
**The z is a statement about how unusual the stock's short-volume share normally is, not about whether
shorts covered.**

**(ii) MPC's baseline is chronically 10–13pp above the tool's own stated normal band (40–45%), at every
lookback from 10 to 60 days.** That is the substantive, non-artifactual fact hiding under the z: **MPC has
been persistently and heavily short-flow-intermediated for at least a quarter**, and one session at 36.4%
is a single day of relief inside that regime — which is why **MPC's own 5-vs-5 trend is still +3.9 ▲, i.e.
pointing UP**, in the same read that tags it "short-covering." The tag and the trend column disagree, and
the trend column covers 10 sessions while the z covers 1.

**(iii) XOM's reading is the more genuinely extreme of the two in absolute terms — and it points the wrong
way to be positioning.** XOM's 58.9% sits against a baseline **inside** the normal band (41.1–45.7%), so
unlike MPC's the z is not baseline-inflated. But **XOM ROSE +1.58% on 2026-07-23, an excess of +2.81pp vs
SPY on a −1.23% SPY day**. A record share of consolidated volume marked short, on a day the stock
outperformed SPY by 2.81pp into the #1 news event of the day, is the signature of **market-maker delta
hedging against option and index demand** — which FINRA's own definition includes and the tool's help text
warns about (*"MM헤지 포함"*) — far more than of directional short-selling. `[inferred, mechanism not
directly measurable in this repo — no options-flow module]`.

**Verdict on (b): the z-spread between MPC and XOM does not measure what the board has been reading into
it. MPC's −3.29 is a baseline artifact (identical print to PSX, opposite tag) sitting on a real but
opposite-signed fact (chronically elevated short-flow, 5v5 still rising). XOM's +3.13 is real in
magnitude but arrived on a session XOM beat SPY by 2.81pp, which is inconsistent with directional
short-selling. Per the repo's own standing rule, FINRA short-pressure is context and never a trigger —
this run recommends demoting it from "the board's strongest short-covering read" to a baseline note.**
`indistinguishable` (C4) between hedging and positioning on XOM; **not** indistinguishable on MPC —
the PSX identical-print test settles that one.

### (c) VLO prints 2026-07-30 — the observable, pre-registered

**Confirmed date and consensus** (`yfinance calendar`, pulled 2026-07-24): **VLO 2026-07-30, consensus
EPS $10.127, consensus revenue $38.429B.** Peers: XOM 07-31, MPC 08-04, PSX 08-05. **VLO prints first,
and §6 shows it is also the cleanest crack instrument of the three — which is why this is the right
name to pre-register.**

**Why this print carries information no prior print could.** The crack's quarterly means (own calc,
settled): **2026Q1 32.06 → 2026Q2 50.96 → 2026Q3-to-date 64.71.** The 2026 crack spike began in
**March 2026** (monthly mean 25.45 → 46.10). **Q2 2026 is therefore the FIRST full reported quarter that
contains the spike, and it has not been reported by anyone in the US refining node yet.** This is also
why the annual gross-margin history in §4 cannot settle the peak-margin question: the peak is not in the
annual series because the quarter carrying it has not printed.

**The frozen observable — one hard number, checkable on the day.** Consensus EPS $10.127 × ~296.9M shares
≈ **net income $3.01B on revenue $38.429B = a 7.82% net margin, against 3.90% in Q1'26**. Rolling that
back through VLO's own Q1'26 tax and opex ratios gives an **implied Q2'26 gross margin of ~12.6%, against
6.30% in Q1'26 — which is itself the MAXIMUM of VLO's last five reported quarters** (6.30 / 6.23 / 5.47 /
4.09 / 1.64 for Q1'26 back to Q1'25). `[inferred — the ratio roll-forward assumes Q1'26 tax rate 73.3%
net/pretax and Q1'26 gross-to-operating ratio 1.178 both hold; the assumption is named, not hidden.]`

| Branch | Observable on 2026-07-30 | Meaning |
|---|---|---|
| **A** | Gross margin **≥ 12.0%** (or reported EPS ≥ $10.13) | The crack converted to P&L at the rate consensus underwrote. The margin reading in (a) is confirmed on a US refiner's own statements, and the peak-margin question moves from "is it real" to "when does it roll" |
| **B** | Gross margin **10.0–12.0%** (EPS ~$8.0–10.1) | Real margin expansion, incomplete capture. **The interesting branch** — it would say the NYMEX 3-2-1 overstates what a 15-refinery multinational system actually realizes, which is the single most useful thing this desk could learn about its own KPI |
| **C** | Gross margin **< 10.0%** (EPS < $8.0) | The crack is not converting. The KPI this desk has tracked since 07-17 is the wrong instrument for these equities, and §6's "VLO is the crack instrument" finding is falsified at its first test |

**⚠ The implied-move defect (M47) blocks the price bracket and is stated rather than worked around**:
VLO's only quoted straddle is **±2.3% expiring 2026-07-24 (D0) — it expires SIX DAYS BEFORE the print
and is unusable.** No price threshold is fabricated from it. **The only usable straddle in this node is
MPC ±11.2%, expiry 2026-08-21 (D28), against MPC's 08-04 print.** VLO's branch above is therefore
**categorical, on the company's own reported line, and I say so.**

**One pre-registered dated catalyst check, run and returning nothing** (`module_disclosure_us VLO`,
last 90 days, 30 filings): **3 8-Ks total — Item 2.02 earnings 04-30, Item 5.02 director change 05-08,
Item 7.01 Reg-FD 07-16.** No M&A, no contract, no capacity, no guidance-revision 8-K. **Nothing between
now and 07-30 is dated on VLO's own filing record.** Blank stays blank.

---

## §3 · Lens L1 — the crack's RATE of change, not its level

**The level is at the top of its range. The rate is at zero. Those are both true and only the second one
is new information.**

**Quarterly means of the settled 3-2-1 crack** (own calc, `yfinance CL=F/RB=F/HO=F` continuous,
`(2·RB·42 + HO·42 − 3·CL)/3`, settled closes only):

| Quarter | Crack mean $/bbl | QoQ % | QoQ $ | **2nd derivative (Δ of QoQ %)** | n sessions |
|---|---|---|---|---|---|
| 2025Q1 | 20.71 | +21.59% | +3.68 | +39.08 | 61 |
| 2025Q2 | 25.52 | +23.25% | +4.81 | +1.67 | 62 |
| 2025Q3 | 26.45 | +3.63% | +0.93 | **−19.62** | 65 |
| 2025Q4 | 25.30 | −4.34% | −1.15 | −7.97 | 64 |
| 2026Q1 | 32.06 | +26.74% | +6.77 | +31.08 | 61 |
| **2026Q2** | **50.96** | **+58.92%** | **+18.89** | **+32.18** | 62 |
| **2026Q3 to date** | **64.71** | **+26.98%** | **+13.75** | **★ −31.94** | **17 (partial)** |

⚠ **2026Q3 is 17 of ~64 sessions and is July-only, so the QoQ figure is a partial-quarter run-rate, not a
quarter.** It is printed because the mandate asked for the second derivative and refusing to print a
partial would hide the only observation that matters. **It is not a settled quarter and is labeled.**

**Weekly means — the same finding at a resolution where every point is a complete week of settled closes:**

| Week ending | Crack | Gasoline crack | Distillate crack | **Gap (dist − gas)** | WoW % | **Accel (Δ WoW %)** | n |
|---|---|---|---|---|---|---|---|
| 2026-06-19 | 49.23 | 45.64 | 56.42 | 10.78 | +4.68% | +0.25 | 4 |
| 2026-06-26 | 55.65 | 52.52 | 61.91 | 9.39 | +13.03% | +8.35 | 5 |
| 2026-07-03 | 59.86 | 55.97 | 67.63 | 11.66 | +7.56% | −5.47 | 4 |
| 2026-07-10 | 61.94 | 55.50 | 74.81 | 19.31 | +3.48% | −4.08 | 5 |
| 2026-07-17 | 67.65 | 57.82 | 87.30 | 29.48 | +9.21% | +5.73 | 5 |
| **2026-07-20→23** | **67.73** | **57.12** | **88.94** | **31.81** | **+0.12%** | **★ −9.09** | **4, all settled** |

**Read, in one paragraph.** The crack's *level* is the highest weekly mean in the series (67.73) and the
07-23 settled close (66.492) is at the **89th percentile of 90 days**. Its *rate of change* is
**+0.12% week-over-week — arithmetically flat**, down from +9.21%, and the quarterly second derivative has
gone **−31.94** on the partial Q3. **This is the classic peak-shape: the level makes the headline and the
second derivative makes the decision.** ★ **But note the composite is hiding the same two-legged move R17
said survives**: over the same six weeks the **gasoline crack went 45.64 → 57.12 (+25.2%) and stalled
(57.82 → 57.12, −1.2% in the last week), while the distillate crack went 56.42 → 88.94 (+57.6%) and is
still rising (+1.9% in the last week)**. **The composite's flat +0.12% is a stalling gasoline leg netting
against a still-rising distillate leg — it is not a margin that stopped.**

**⚠ Today's 07-24 bar, refused and shown so the refusal is auditable.** At 09:59 ET the 07-24 bar computes
**crack 58.21 (−12.4% vs the 07-23 settle)** on WTI 89.83, RB 3.2365, HO 4.0985. **RB=F is −7.43% on that
unfinished bar**, consistent with an RBOB August-contract roll. **Session volume on the 07-24 bar is
RB 19,456 vs 27,662 on the settled 07-23 bar** — an unfinished session. **This number appears nowhere in
any conclusion in this file.** Separately logged as a data-integrity note: **yfinance reports identical
volume for 07-22 and 07-23 on all three legs (CL 358,021 / HO 25,967 / RB 27,662) while the closes
differ** — the volume column for 07-23 is not trustworthy; the close column is (it reproduces MACRO §D-P4
to 3 decimals independently).

---

## §4 · Lens L2 — peak-margin / low-multiple, with the revision second derivative beside it

**The multiple, pulled today** (`module_fundamentals_us`, 2026-07-24 intraday):

| | Fwd P/E | Fwd EPS | Price (07-24 intraday) | Mean target | Price vs target | CY EPS rev 90d | Next-Q rev 90d |
|---|---|---|---|---|---|---|---|
| **MPC** | **10.71** | $29.19 | 313.12 | $298.12 | **+5.0% ABOVE target** | +65.8% | **+104.2%** |
| **PSX** | **11.02** | $18.86 | 208.47 | $203.89 | **+2.2% ABOVE target** | +42.0% | +62.2% |
| **VLO** | **12.27** | $24.88 | 305.64 | $287.28 | **+6.4% ABOVE target** | +33.4% | +78.8% |
| XOM (control) | 14.64 | $10.73 | 157.21 | $167.14 | **−5.9% BELOW target (upside)** | +8.6% | +6.1% |

★ **R8 HOLDS for a third consecutive run: MPC 10.71 < PSX 11.02 < VLO 12.27. PSX is not the cheapest
large refiner on forward, and the human-locked `core_pick` rationale that says it is remains wrong.**
★ **All three refiners trade ABOVE mean consensus target while XOM trades below it** — the low multiple
and the exhausted target are the same fact seen twice.

**The revision second derivative — the number that decides whether the low multiple is cheap or is a
peak denominator** (consensus EPS increments between windows, 90d→60d→30d→7d→now):

| | Current-Q increments | Next-Q increments | Breadth, current-Q (7d / 30d) |
|---|---|---|---|
| **VLO** | +1.98 → +0.49 → **+0.07 → 0.00** | +1.30 → +0.52 → +2.52 → **+1.36** | ★ **6↑ / 5↓ · 7↑ / 5↓** |
| **MPC** | +2.77 → +0.68 → +1.67 → **+0.38** | +1.48 → +0.82 → +3.44 → **+1.67** | **2↑ / 0↓ · 5↑ / 2↓** |
| **PSX** | +0.98 → +0.27 → +0.83 → **+0.13** | +0.89 → +0.45 → +1.00 → **+0.68** | **2↑ / 0↓ · 6↑ / 2↓** |
| **XOM** | +0.19 → +0.16 → **−0.04 → −0.02** | +0.17 → +0.25 → **−0.23 → −0.01** | **0↑ / 2↓ · 0↑ / 4↓** |

★★ **The single most decision-relevant line in this table is VLO's breadth: 6↑ / 5↓ over 7 days and
7↑ / 5↓ over 30 days — VLO is the ONLY refiner of the three with analysts CUTTING its current quarter,
and it is the one that prints in six days.** MPC and PSX are 2↑/0↓ unanimous. VLO's current-quarter
increment has been **exactly 0.00 for two consecutive runs** while its next quarter still rises. Read
together: **consensus has stopped marking the quarter VLO is about to report and is still marking up the
quarter after it** — and 5 of 11 analysts are moving the near number *down*. ⚠ **XOM, the control, is now
being cut on BOTH quarters and on both windows** — 0↑/2↓ and 0↑/4↓ — which is what makes it the control:
XOM captures crude, not crack, and its book says so.

**The peak-margin check on reported history — and an honest statement that it does not settle the question.**

`scripts/margin_history.py` (SEC XBRL annual gross margin):

| | FY window | Peak | Trough | Median | **FY2025** | Where FY2025 sits |
|---|---|---|---|---|---|---|
| **MPC** | FY2018–25 | **14.5% (FY2022)** | 5.8% (FY2020) | 10.5% | **10.0%** | below median, 4.5pp below peak |
| **PSX** | FY2016–25 | **25.9% (FY2016)** | 8.4% | 12.1% | **12.3%** | at median, 13.6pp below peak |
| **VLO** | — | — | — | — | — | ★ **TOOL GAP: `연간 데이터 없음`** |

⚠⚠ **Stated as loudly as the mandate requires: this table does NOT settle the peak-margin question, for
two independent reasons.** (1) **Annual gross margin for a refiner is structurally diluted by crude
passthrough in the revenue denominator** — a rising crude price mechanically compresses the ratio while
the per-barrel margin is unchanged, and crude rose from a 2025Q4 mean of $59.14 to a 2026Q2 mean of
$92.70. (2) **The 2026 crack spike cannot appear in any FY2025 series at all.** What the table honestly
shows is only this: **the annual series is not at a peak** — which is a statement about 2025, not about
the quarter that prints on 07-30.

**Routing around the VLO tool gap with quarterly data — the closest this run can get:**

| Quarter | VLO gross margin | VLO operating margin | MPC gross margin | PSX gross margin | Crack mean |
|---|---|---|---|---|---|
| 2025Q1 | 1.64% | 0.76% | 4.33% | 6.50% | 20.71 |
| 2025Q2 | 4.09% | 3.34% | 8.83% | 10.29% | 25.52 |
| 2025Q3 | 5.47% | 4.69% | 7.95% | 10.05% | 26.45 |
| 2025Q4 | 6.23% | 5.19% | 8.86% | 12.18% | 25.30 |
| **2026Q1** | **6.30%** | **5.35%** | **6.23%** | **8.50%** | **32.06** |
| **2026Q2 (prints 07-30 / 08-04 / 08-05)** | — | — | — | — | **50.96** |

★ **This is a better answer than the annual table and it contains a genuine surprise: on the quarter with
the highest crack of the five (32.06), MPC's gross margin FELL to its 5-quarter low of 6.23% and PSX's
fell to 8.50% — only VLO's rose.** Whatever drives MPC's and PSX's gross margin, it was not the crack in
Q1'26. §6 measures that directly.

**The arithmetic bracket for what consensus is underwriting — assumption named.** Fitting each company's
last five reported quarterly gross profits against the same quarters' mean settled crack (OLS, n=5):

| | Fit | **r** | **p (two-tailed, df=3)** | Model-implied GP 2026Q2 | Actual GP 2026Q1 | Implied QoQ |
|---|---|---|---|---|---|---|
| **VLO** | GP = −1.908 + 0.1303·crack | **+0.836** | **≈0.078** | **$4.73B** | $2.04B | +132% |
| MPC | GP = +1.085 + 0.0516·crack | +0.307 | ≈0.62 | $3.71B | $2.13B | +74% |
| PSX | GP = +1.903 + 0.0483·crack | +0.238 | ≈0.70 | $4.37B | $2.77B | +58% |

⚠ **n=5, df=3. None of these is significant at the 5% bar — VLO's is marginal (p≈0.078) and MPC's and
PSX's are `indistinguishable` from zero (C4 language, deliberately: not "rejected," not "no
relationship" — the sample cannot tell).** With that caveat carried: **VLO's own crack sensitivity
extrapolates to $4.73B of Q2'26 gross profit and the consensus EPS implies ~$4.83B — a 2% gap.**
**So consensus for 07-30 is, to within 2%, the straight-line extrapolation of VLO's own five-quarter
crack sensitivity. It is not a fantasy number, and calling it one would be wrong.** Where the
extrapolation does become heroic is **Q3'26: the same fit implies $6.53B of gross profit at the
July-to-date crack of 64.71 — and that quarter, not Q2, is what the 12.27× forward multiple capitalizes.**

**L2 verdict, stated as a state and not a call: the low multiple sits on a denominator whose input (the
crack) is at the 89th percentile of 90 days with a WoW rate of +0.12%, and on a consensus that has
stopped rising for the printing quarter at exactly the name that prints first (VLO, 0.00 increment,
6↑/5↓). That is the peak-margin signature in its early, not its late, form. It is not resolved and
2026-07-30 is the first date that can resolve it.**

---

## §5 · The customers, named with dated prints (W4 / D23)

**Four of five closed on the 07-23 run and carried unchanged; the fifth is dated and imminent.** No
customer figure in this section is re-derived — see the 07-23 file §3 for the full quotes.

| Customer | Print date | Fuel cost | Sequential/guide action |
|---|---|---|---|
| **DAL** | 2026-07-10 | +$1,913M YoY | FY26 EPS $6.50–7.50 maintained; ~60% of the incremental fuel cost passed to fares |
| **UAL** | 2026-07-16 | +$2,335M YoY (**+84%**) | **Q3 guide $2.50–3.50 vs $3.60 consensus — a sequential guide-down**; ~$6B FY26 fuel headwind; cites *"jet fuel crack spreads soaring"* |
| **FDX** | 2026-06-24 | $864M → $1.43B (**+66%** YoY) | Beat and guided FY27 $16.90–18.10; **sequentially absorbed**, no demand impact cited |
| **LUV** | 2026-07-23 | +67% YoY to $2.22B | **Q3 guide $0.50–0.75 vs $0.82 consensus, FY26 cut to $3.25–4.25** — a sequential cut on fuel |
| **UPS** | ★ **2026-07-28 — the only one still unread** | — | — |

**What this adds this run, beyond the carry.** Two of four printed customers cut near-term guidance
citing fuel specifically. Together with §2(a)'s three legs this closes the *"the crack is a paper
number"* objection completely: **the margin is disclosed as a dollar expense on four customer income
statements and as a dollar revenue on TotalEnergies'.** ⚠ **It still does not separate margin from war
premium by itself** — a war premium also shows up as a real cost to a fuel buyer. §2(a) does the
separating; §5 only removes the "paper" objection.

**UPS 2026-07-28 (S20) is the frozen observable and its implied move is unusable** (±1.3–1.7%, expiry
2026-07-24, D0 — M47). The observable is therefore categorical and pre-registered by PREMORTEM: **does
the Q2 call quantify fuel expense YoY with a sequential comparison, and is any guidance cut attributed
to fuel or to volume?** Fuel a non-event at the largest US distillate buyer would contradict §2(a)
Leg 3 directly.

---

## §6 · W5 — sub-node dispersion. **The sector label is the wrong unit, and this run puts a ratio on it.**

**Measured this run** (own calc, settled closes to 2026-07-23; refining = equal-weight VLO/MPC/PSX,
crude = equal-weight XOM/CVX/COP; benchmark **SPY** named inline):

| Horizon | Refining | Crude | **Spread** | XLE own move | XLE vs **SPY** | **\|spread\| ÷ \|XLE own move\|** |
|---|---|---|---|---|---|---|
| 1d (07-23) | −1.68% | +1.17% | **−2.85pp** | +0.30% | +1.54pp | **9.38×** |
| 5d | +2.19% | +6.59% | −4.40pp | +4.14% | +5.81pp | 1.06× |
| 20d | +25.11% | +13.47% | +11.64pp | +10.85% | +10.17pp | 1.07× |
| **60d** | **+30.56%** | **+3.29%** | **+27.27pp** | **+4.60%** | **+1.38pp** | **★ 5.93×** |

**Per name, 60 sessions, excess vs SPY** (reproduces `SECTOR_FLOW_US.json §names` independently to within
0.1pp, which is why it is trusted): **MPC +34.22 · VLO +24.91 · PSX +22.91 · XOM +2.65 · CVX +2.00 ·
COP −4.43 · XLE +1.38.**

★ **The W5 condition fires on both the daily and the 60-day horizon: the spread between the crude node and
the refining node is 9.38× and 5.93× the sector's own move.** On 60 sessions XLE carries **+4.60%** while
the two nodes inside it differ by **27.27pp**. **A label that moves 4.6% while its constituents diverge by
27pp is not describing a position; it is averaging two.** ⇒ **"Energy" must not be used as the unit of
analysis for this node, and MACRO §E's OW — written on the crude leg from a single session — sits on the
leg with +2.65pp of 60-day excess vs SPY while the leg it excludes carries +22.9 to +34.2pp.**
SWEEP §2b and EVENT_ALPHA Card 3 reached this independently; this file adds the **ratio**, which is the
form W5 actually asks for.

**★ And the dispersion goes one level deeper than crude-vs-refining — the three refiners are not one
node either, on the fundamental axis.** From §4's regressions: **VLO's gross profit tracks the crack at
r = +0.836; MPC's at +0.307 and PSX's at +0.238** (n=5 each, `indistinguishable` from zero for MPC/PSX).
The reason is in the filings, which this run read: **VLO is 15 refineries plus Renewable Diesel and
Ethanol — three segments, all fuels** (10-K filed 2026-02-25, ~3.2M bpd throughput); **MPC is Refining &
Marketing + Midstream + Renewable Diesel** (~3.0M bpd, carried); **PSX is FIVE segments — Midstream,
Chemicals (a 50% CPChem JV), Refining (10 refineries US+Europe), Marketing & Specialties, and Renewable
Fuels** (10-K filed 2026-02-20, total assets $73.7B). **PSX and MPC have large non-refining earnings
streams that mechanically dilute crack beta; VLO does not.** This is the structural reason §4's quarterly
table shows MPC's and PSX's gross margin *falling* in Q1'26 while VLO's rose.

⚠⚠ **The countervailing measurement, and it is the strongest single number against treating these as
three positions.** PREMORTEM §3b measured the **VLO–MPC SPY-residual correlation at +0.864** over 251
sessions, and **XOM–XLE at +0.912**. **On price, the three refiners are one risk unit with three
tickers; on fundamentals, they are three different businesses with crack betas of 0.84 / 0.31 / 0.24.**
Both are measured and both are true. **The reconciliation: the price correlation says they will move
together on the crack headline; the fundamental dispersion says they will separate on their own print
dates (07-30, 08-04, 08-05).** That is a testable claim and §7 registers it.

**And the same PREMORTEM measurement extends the W5 problem outside the sector**: **XLE–^TNX residual
correlation +0.326 while XLU/XLRE/XLP–^TNX are −0.194 to −0.302.** The Energy OW and the three N− bond-
proxy tilts sit on **opposite signs of the same yield axis** — one bet doubled, not four independent
views. Carried, not re-derived.

---

## §7 · Track KPIs and anti-signals, as dated observables

**KPIs — every one on settled closes only (binding after R17 / D48).**

| # | KPI | Current settled reading | Next reading |
|---|---|---|---|
| 1 | **3-2-1 crack, level** | **66.492** (2026-07-23), **89th pctile of 90d**, 90d range 41.14–69.45 | next settle 2026-07-24 ~14:30 ET |
| 2 | ★ **3-2-1 crack, WEEKLY RATE** (the L1 metric) | **+0.12% WoW** (67.73 vs 67.65), accel **−9.09pp** | week ending 2026-07-31 |
| 3 | ★ **Gasoline and distillate cracks read SEPARATELY** (the 07-23 file's own correction, adopted) | gasoline **57.12** (−1.2% WoW, stalling) · distillate **88.94** (+1.9% WoW, still rising) · gap **31.81** | weekly |
| 4 | **VLO current-Q consensus increment and breadth** | **0.00 for a second consecutive run; 6↑/5↓ (7d), 7↑/5↓ (30d)** — the only refiner being cut | daily; resolves 2026-07-30 |
| 5 | **XOM as the control** | Cut on **both** quarters and **both** windows (0↑/2↓ 7d, 0↑/4↓ 30d) while price is +2.65pp vs SPY over 60d | XOM prints 2026-07-31 |
| 6 | **US refinery utilization** (EIA weekly) | **96.2%** wk to 07-17 (vs 94.7% yr-ago); PADD2/PADD4 **100%** | ⚠ no EIA module in this repo — read via news bodies only |
| 7 | **India refined-product exports** (the competitor supply response) | **1.55M bpd est. July vs 866k bpd May**, 2nd-highest in Kpler's series since 2017 | monthly, via `--scope foreign` |
| 8 | **FINRA short-vol z** — ★ **DEMOTED this run** to a baseline note, not a positioning read (§2b) | MPC 36.4% on a 53.9–57.1% baseline; PSX **identical 36.4%** on a 39.0% baseline | daily; context, never a trigger |

**Anti-signals — dated, and each one stated so it can fire against this file.**

| # | Anti-signal | Threshold | State today | Distance |
|---|---|---|---|---|
| **A1** | S8 / MACRO P4's registered kill | **settled crack < 60.00 with WTI > $90** | crack 66.49, WTI 92.19 | **$6.49 away — armed** |
| **A2** | Two consecutive **weekly means** below 60.00 (carried from 07-23, corrected to settled basis) | — | 67.65, 67.73 | not near |
| **A3** | ★ **The distillate bottleneck releases** — gap (dist − gas) narrows below **$15** | gap **31.81** and widening 5 weeks | far, and moving away |
| **A4** | ★ **New this run, from PSX's own Item 1A**: *"production levels of refined products by competitors"* + *"import and export capabilities."* **Fire if a second month of Indian/Asian export ramp coincides with a falling weekly distillate crack** | India already +79% sequentially (866k → 1.55M bpd) but the distillate crack is still rising — **the two halves disagree, so it has NOT fired** | monitor monthly |
| **A5** | S21 (STNG 2026-07-30, ±10.0% D28 — the node's other usable straddle): TCE flat-or-down with Q3 booked days below Q2 ⇒ S8 branch A arrives with no Hormuz statement | not yet printed | 2026-07-30 |
| **A6** | ★ **This file's own falsifier**: VLO reports gross margin **< 10.0%** on 2026-07-30 | — | 2026-07-30 |
| **A7** | ★ **The §6 dispersion claim's falsifier**: if VLO / MPC / PSX print within ~1pp of each other on gross margin across 07-30 / 08-04 / 08-05, the "three different businesses" reading in §6 is wrong and the +0.864 residual correlation is the whole story | — | 2026-08-05 |

**Dated calendar for this node**: **UPS 07-28** (S20) · **VLO 07-30** (consensus EPS $10.127, rev $38.429B)
· **STNG 07-30** (S21) · **XOM 07-31** (consensus EPS $3.664) · **MPC 08-04** (consensus EPS $13.871,
±11.2% straddle usable) · **PSX 08-05** (consensus EPS $7.492).

**★ Proposed retraction, filed by this stage for `handoff/STANDING_VIEW.md` §5:**

| # | Claim | Killed by | Date |
|---|---|---|---|
| **R17-b** | **"The week-to-date 3-2-1 crack mean is 65.95, down from 67.65 — the first negative weekly Δ in the entire series"** — the 07-23 `SECTOR_DEEP_ENRG` §6 KPI #1, a downstream consequence of the same incomplete bar R17 retracted | **On settled closes the week 07-20→07-23 mean is 67.73 vs 67.65, i.e. +0.12% — POSITIVE.** And on the settled 2026-04-01→07-23 window there are **five** prior negative weekly deltas (−1.63, −0.92, −4.87, −7.94, −9.18), so *"first in the entire series"* fails on the window as well as the sign. ★ This is **D48's mechanism reproducing one level downstream**: R17 corrected the daily number, and a second, separately-computed weekly claim built on the same bad bar survived the correction because it was never re-derived | 2026-07-24 |

---

## §8 · The lead/lag claim — **measured this run, not asserted**

The desk's C4 "detachment counter" presumes a lead/lag structure between the crack and the refiner
equities (crack moves, equities should follow or track). **That presumption has never been measured.
It is measured here.** Method: log daily returns, SPY-residual for each equity (OLS on SPY, benchmark
named inline), cross-correlated against the settled 3-2-1 crack's log return at lags −4 to +4 sessions,
**n = 535 trading days, 2024-06-04 → 2026-07-23.**

```
corr( crack_t , SPY-residual_{t+k} )        k > 0 means the crack LEADS the equity
  k        VLO      MPC      PSX      XOM
 -4     -0.007   -0.007   -0.013   +0.008
 -3     +0.020   +0.010   +0.017   +0.063
 -2     +0.006   +0.019   +0.001   -0.031
 -1     -0.009   -0.005   +0.021   +0.051
 +0     +0.301   +0.238   +0.219   +0.078      <- the ONLY non-trivial cell
 +1     +0.001   +0.006   -0.018   +0.028
 +2     -0.005   -0.010   +0.021   +0.008
 +3     +0.001   +0.009   +0.043   +0.047
 +4     -0.047   -0.009   -0.022   -0.035
```

**Three results.**

**(1) There is no lead and no lag. The relationship is entirely same-day.** Every cell outside k=0 is
inside ±0.07 and is **`indistinguishable` from zero (C4)**. ⇒ **No trading, timing or sequencing claim
of the form "the crack moved, the equities have not caught up yet" is supported by this data.** Any such
claim elsewhere in the desk's carry should be tagged `[unverified]` until it is measured on something
other than this pair.

**(2) ★★ The same-day correlation is only ~0.30, and that is what invalidates the C4 counter as
constructed.** For a bivariate-normal pair with r = 0.301, the probability that the two disagree in sign
on a random day is `0.5 − arcsin(r)/π ≈ 40.3%`. **A run of three consecutive sign-disagreement days
therefore occurs by chance about 0.403³ ≈ 6.5% of the time in any given three-day window** — and there
are ~250 such windows a year. For MPC (r = 0.238) it is ≈7.6%. **The C4 counter's threshold ("at 5
consecutive observations the equity is priced off something other than its KPI") is counting an event
that a 0.30 correlation generates routinely.** The counter is not wrong-headed; it is **under-powered at
the sample size it has been run at**, and the correct statement is **`indistinguishable` — not
"rejected."** ⇒ **Recommended to the registry: the C4 counter needs either a much longer streak
threshold or a magnitude condition (e.g. cumulative divergence in pp), not a 5-day count.**

**(3) ★ The rolling window says the link is STRENGTHENING, which is the opposite of detachment.**
60-session rolling same-day correlation to the crack: **VLO 0.404 now vs 0.235 twenty sessions ago
(0.445 sixty sessions ago) · MPC 0.340 vs 0.252 · PSX 0.341 vs 0.350.** Two of three are materially
higher than they were a month ago. **The equities are tracking their KPI more closely now, not less.**

**(4) XOM's same-day correlation to the crack is +0.078 — `indistinguishable` from zero.** ⇒ **XOM is
confirmed as the control: it carries no measurable crack exposure at all**, which is exactly why the
crude-vs-refining split in §6 is a split between two different KPIs and not two flavors of one.

### CHART_READ — embedded VERBATIM per the standing rule (`module_chart <T> --read`, pulled 2026-07-24 ~10:00 ET)

⚠⚠ **These blocks are computed on a series whose LAST BAR IS TODAY'S INCOMPLETE 07-24 BAR** (US session
open at pull time). Every level, RSI, OBV slope and trigger below is therefore contaminated by an
unsettled bar and is presented as-is, unsummarised, exactly as the rule requires — **not as a settled
reading.** The clearest tell: VLO's printed trigger `close>309.82` sits **above** VLO's own last settled
close of 305.26 (2026-07-23) and above its 07-24 intraday 305.64.

```
VLO
OBV: 누적(매수압력↑) (20d기울기 +102%)
다이버전스: 없음
MA정렬: 강세스택(5>20>60>120) · 가격 3/4 MA 위
볼린저: 확장 26.8% · 중단
RSI: 70.4 · 모멘텀20d +17.5%
턴-판정: CONFIRMED-TURN (확인된 반전)
트리거(점화): close>309.82 + OBV→누적 / 스탑(스윙저점): 259.37
```

```
MPC
OBV: 누적(매수압력↑) (20d기울기 +38%)
다이버전스: 없음
MA정렬: 강세스택(5>20>60>120) · 가격 3/4 MA 위
볼린저: 확장 31.8% · 중단
RSI: 79.8 · 모멘텀20d +22.8%
턴-판정: CONFIRMED-TURN (확인된 반전)
트리거(점화): close>315.05 + OBV→누적 / 스탑(스윙저점): 254.06
```

```
PSX
OBV: 누적(매수압력↑) (20d기울기 +35%)
다이버전스: 없음
MA정렬: 강세스택(5>20>60>120) · 가격 3/4 MA 위
볼린저: 확장 31.1% · 중단
RSI: 78.0 · 모멘텀20d +21.2%
턴-판정: CONFIRMED-TURN (확인된 반전)
트리거(점화): close>209.50 + OBV→누적 / 스탑(스윙저점): 169.05
```

```
XOM
OBV: 누적(매수압력↑) (20d기울기 +122%)
다이버전스: 없음
MA정렬: 혼조 · 가격 4/4 MA 위
볼린저: 확장 19.8% · 상단밴드
RSI: 84.1 · 모멘텀20d +15.0%
턴-판정: CONFIRMED-TURN (확인된 반전)
트리거(점화): close>—(전 MA 위) + OBV→누적 / 스탑(스윙저점): 136.06
```

**Reading these under D6 — the OBV tag is C-grade and may not carry a conclusion on its own, so the
A-grade momentum axis is quoted beside it in the same breath.** All four names print OBV
accumulation (누적); the A-grade 60-session excess return vs **SPY** for the same four is **MPC +34.22 ·
VLO +24.91 · PSX +22.91 · XOM +2.65**, and the 20-session figures vs **SPY** are **MPC +26.0 · VLO +25.2 ·
PSX +22.1 · XOM +13.9** (`SECTOR_FLOW_US.json`, asof 07-23). **The A-grade axis agrees with the C-grade
OBV tag for all four**, so the accumulation reading is admissible here — but note the OBV *slope* ranks
XOM first (+122%) while the A-grade axis ranks it last (+2.65pp vs SPY), so **the two axes rank the same
four names in nearly opposite order.** Per D6 the A-grade order governs. ⚠ RSI 70–84 across all four on
an incomplete bar is not read as a signal in either direction. ⚠ All three refiners are tagged 🟡중립
rather than 🟢가속 **solely** because `vol_surge` is 0.87–1.00 — the filter artifact SWEEP §3 diagnosed,
not evidence.

---

## §9 · What I could not measure this run

- **VLO's Item 1A risk factors.** `module_business_us VLO --json` returns `risk_factors: ""` and
  `risk_summary_bullets: []` — the `edgartools` TenK parser fell back to the legacy path on accession
  `0001628280-26-011499` and produced an empty section. **PSX's extracted cleanly and was substituted.**
  ⇒ **Dig: the same fallback will silently blank Item 1A for other tickers; the tool should raise rather
  than return an empty string.**
- **VLO annual gross-margin history.** `scripts/margin_history.py VLO` → *"연간 데이터 없음"* while MPC
  and PSX return 8- and 10-year series. Routed around with 5 quarters of yfinance/XBRL data (§4).
- **EIA weekly inventory and utilization as a first-party series.** No EIA module in this repo; §2(a)
  Leg 2 and KPI #6 are read out of news bodies, which is a weaker source than the others in this file
  and is labeled as such.
- **Options flow / market-maker hedging.** §2(b)(iii)'s mechanism for XOM's z is `[inferred]`; nothing in
  this repo separates hedging short-volume from directional short-volume.
- **Tonne-miles or a tanker freight index.** Unchanged from 07-23 — the tanker leg remains
  `indistinguishable` and is carried, not re-argued.
- **A non-US-Gulf refining margin benchmark computed by this desk.** TotalEnergies' own European marker
  (§2a Leg 1) is the first non-USGC margin number this file has ever carried, but it is a company
  disclosure read from a news body, not a series this repo can compute or update.
- **Whether the 07-24 crack move is a genuine decline or an RBOB contract roll.** The bar is unsettled;
  no roll-adjusted continuous contract is available in this toolset. **Resolves at the 07-24 settle.**

---

## ✅ EXIT CHECK

- [x] **Delta-first**: §0 leads with the delta; the value-chain map, tanker leg and chain-hop ledger are
      carried by reference to `llm_outputs/2026-07-23/industry_US/SECTOR_DEEP_ENRG.md` and **not reprinted**.
- [x] **R17 carried and extended** — and a **second, downstream retraction (R17-b) filed** for the weekly
      KPI that R17 did not reach.
- [x] **All three mandate questions answered**: (a) margin, on three non-futures legs · (b) baseline
      artifact, with the PSX identical-print test · (c) VLO 07-30 pre-registered with a hard number and
      three branches. **None left open without saying so.**
- [x] **§3 is a rate-of-change section, not a level section** — quarterly QoQ + second derivative, and a
      weekly series where every point is settled.
- [x] **§4 puts the estimate-revision second derivative beside the multiple**, and states explicitly that
      the annual margin table **does not** settle the peak question, with both reasons.
- [x] **§5 names every customer with a dated print**; UPS 07-28 is the one open item.
- [x] **§6 states the sector label is the wrong unit and puts a ratio on it** (5.93× / 9.38×).
- [x] **§7 gives KPIs and anti-signals as dated observables**, including two that can falsify this file
      (A6, A7).
- [x] **§8's lead/lag claim is MEASURED** (n=535, lags −4..+4) and the C4 counter is re-graded
      `indistinguishable`, never "rejected."
- [x] **Every relative figure names SPY inline** (C1). **`indistinguishable`, never "rejected"** (C4).
- [x] **CHART_READ blocks embedded verbatim**, with the incomplete-bar contamination stated (D31).
- [x] **Blanks left blank** — VLO Item 1A, VLO annual margin, EIA first-party, options flow, tonne-miles,
      the 07-24 roll question. **No number guessed.**
- [x] **Zero buy/sell language, zero sizing, zero position language.** Analytical only.
