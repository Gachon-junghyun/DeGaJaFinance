# SECTOR_DEEP_INDU — Industrials · industry_US · 2026-08-10 (Mon) · delta-led, the breadth question settled by earnings calendar

> **Track: CONTINUOUS**, fifth consecutive DEEP (08-05/06/07/08/10). INDU remains the board's **only
> OW−**. Carried by reference, **not reprinted**: `llm_outputs/2026-08-08/industry_US/SECTOR_DEEP_INDU.md`
> (Kilby turbine chain at primary level, GEV/CAT "best-disclosed = worst-flowed" inversion, PWR>ETN≫AME>EMR
> data-centre-disclosure ranking, LMT/Saudi refutation, S64 crude-tick hypothesis). Flow/RS/short **asof
> 2026-08-07 settled** (`SECTOR_FLOW_US.json`, `US_LIVE_SHORTLIST.json`, `scripts/us_flow.py`); primary
> filings pulled live 2026-08-10 (`module_business_us`, `module_disclosure_us`, `module_fundamentals_us`),
> dated inline. Benchmark **SPY** named inline throughout (C1). **P4 — analysis only, zero buy/sell, zero
> sizing.**

---

## §0 · The delta, one line

**PREMORTEM Lens 3 (§3a) split ROTATION's own claim that INDU's breadth is corroborated by three names
(EMR, PH, AME) rather than one — only PH is broadly based; EMR (110% of its 60d excess earned in the
last 20 sessions) and AME (121%) sit on flat-to-negative 21–60d bases.** This stage went one level
under Lens 3's price decomposition and found the **mechanical cause, dated at the primary-filing
level**: **EMR, AME and CAT all filed Item 2.02 earnings 8-Ks on the SAME day, 2026-08-04** — three
days before this run's settled bar — while **PH's Item 2.02 filed 2026-08-06**, two days *later*, on
top of a base that was **already positive before its own print** (21–60d excess +7.80pp). ⇒ EMR/AME's
"breadth" is a shared-earnings-date price cluster with three trading days of settled history behind it;
PH's is not. **The breadth is one name, and now there is a calendar reason, not just a statistical one.**

---

## §1 · The inherited question, resolved — one live name, and here is why

### 1a · The earnings-date finding (new this run, primary-sourced)

`module_disclosure_us <TKR> --days 45`, filing dates verified against EDGAR accession numbers:

| Ticker | 8-K Item 2.02 filed | Accession | Days before this run's clock (08-10) |
|---|---|---|---|
| **EMR** | **2026-08-04** | 0000032604-26-000042 | 6 calendar / 4 trading days |
| **AME** | **2026-08-04** | 0001037868-26-000173 | 6 calendar / 4 trading days |
| **CAT** | **2026-08-04** | 0000018230-26-000040 | 6 calendar / 4 trading days |
| **PH** | **2026-08-06** | 0000076334-26-000082 | 4 calendar / 2 trading days |

**Same-day print for three of the four names this desk has been tracking.** A 20-session "share of
60-day excess" window measured on 08-07 (settled) necessarily loads almost all of EMR/AME/CAT's move
into the post-08-04 handful of sessions — that is what M149's **110%/121%** shares mechanically are.
PH's later print, on top of a base that was **positive before the print** (§1b), is a different shape
by construction, not by coincidence.

### 1b · The name-level table — flow + two independent OBV producers + revisions + short + filing-confirmed driver

`SECTOR_FLOW_US.json` (settled 08-07) cross-checked against `module_chart --read` (**D208 note**: this
run the two producers **agree** on all four names below — no sign flip, unlike MPC/PRU elsewhere on the
board today, see PREMORTEM §3e) and `module_fundamentals_us --json` (pulled 08-10):

| | **PH** | EMR | AME | CAT (top1, context) |
|---|---|---|---|---|
| flow_score / tag | 0.883 🟢가속 | **0.911 🟢가속 (best in sector)** | 0.733 🟢가속 | −0.631 🔴분산 (sector-worst) |
| `sector_flow` OBV | 매집 +0.356 | 매집 +0.629 | 매집 +0.252 | 분산 −0.156 |
| `module_chart --read` OBV | **누적, 20d기울기 +80%, 다이버전스 없음** | 누적, +44%, 다이버전스 없음 | 누적, +110%, **다이버전스: 약세 (가격 고점↑·RSI 고점↓)** | 누적, +31% (PULLBACK-TO-SUPPORT, RSI 40.8) |
| rs20 / rs60 vs SPY | **9.3 / 17.1** | 11.5 / 10.5 | 6.0 / 5.0 | −14.0 / −12.4 |
| 60d excess vs SPY · share in last 20d · 21–60d base (PREMORTEM M149) | **+17.09 · 54% · +7.80** | +10.53 · 110% · −1.00 | +4.96 · 121% · −1.02 | n/a (not extended) |
| Revision breadth, current FY, 30d (`module_fundamentals_us`) | 3↑/5↓ (0y) but **current-Q & next-Q 1↑/0↓ clean, zero downgrades** | 2↑/3↓ (0y), current-Q 0↑/2↓ | 3↑/2↓ (0y) | 4↑/3↓ (0y), current-Q 2↑/2↓ |
| EPS-trend 90d drift (current-FY estimate) | +1.86% | +0.74% | +2.39% | **+10.68%** |
| FINRA short-vol z (`us_flow.py`, 08-07) | 0.01 △정상 | 0.67 △정상 | −0.20 △정상 | 0.74 △정상 |
| Filing-confirmed driver, dated | **8-K 08-06: FY2026 Q4 results. FY2025 10-K MD&A (filed 08-22-25) names "strength across commercial and defense markets" in the Aerospace Systems segment as the sales driver** | Automation Solutions / electrical, no data-centre language found in the captured 10-K excerpt (§3) | 8-K 08-04 results; FY2024 10-K names "data centers" once, among ~10 end-markets for UPS/electric-meter products | 8-K 08-04 results; FY 10-K/Q1 print already carries "power-gen sales +41% YoY driven primarily by data center applications" (08-08 file, not re-derived) |

⚠ **RS20/RS60 sit in the same paragraph as every OBV citation above (D6 compliance) — none of the OBV
readings in this table stand alone.**

**Reading:** short-vol pressure does not discriminate between the four (all `△정상범위`) — it is not
the axis that explains the flow gap. **What does**: PH is the only one of the four with (i) a positive
prior-window base **before** its print, (ii) unanimous near-term analyst upgrades with zero downgrades
in the two nearest quarters, and (iii) an independent second producer (`module_chart`) confirming no
divergence. **AME is the opposite case on the same second producer**: `module_chart` flags a bearish
divergence (price higher-high, RSI lower-high) that `sector_flow`'s single OBV number does not carry —
an independent, non-price-derived-in-the-same-way confirmation of PREMORTEM's "EXHAUSTED-leaning" tag.

### 1c · A second correction the calendar evidence adds: PH is not even the same story

`module_business_us PH --form 10-K` (filed 2025-08-22, FY ended 2025-06-30 — the most recent 10-K on
file; the 08-06 8-K is the newer FY2026 print, item-level only, full press-release body blocked by SEC
403 on direct fetch) states Parker-Hannifin serves **"aerospace & defense, in-plant & industrial
equipment, transportation, off-highway, energy, and HVAC & refrigeration"** with FY2025 growth
attributed to **"strength across commercial and defense markets"** in Aerospace Systems. **This is not
the data-centre/AI-power thesis** that carries GEV, CAT's power-gen segment, AME's UPS/electric-meter
line and (on the primary-filing text captured) not EMR either. ⇒ **INDU's board OW does not rest on one
story confirmed by three names — it rests on two unrelated stories, one of which (aerospace/diversified
industrial, carried by PH) currently has exactly one live name, and the other (data-centre-power,
carried by GEV/CAT/AME/EMR) is the compressed, earnings-date-clustered or outright inverted one** (GEV,
carried from 08-08: best primary-filing AI-power disclosure, worst flow on the board that run).
**TRI (flow 0.911, tied with EMR) is a third, unrelated driver again** — Thomson Reuters, GICS
"Research & Consulting Services," an information/legal-tech name with no aerospace or power-equipment
exposure — meaning the sector's own green cohort spans **at least three uncorrelated theses** (aerospace/
diversified industrial · data-centre power equipment · information services), before BA's separate
short-covering-driven bounce (§4) is even counted.

---

## §2 · Exposure — the fuel-cost channel, quantified from primary filings

PREMORTEM §2d: INDU is the DEEP set's most exposed pick, hit by both against-us branches of `S73`/`S74`,
**and they are correlated, not independent** — a Hormuz hardening (`S74` branch B) raises fuel costs,
which raises the odds of a hot 08-12 CPI print (`S73` branch H), which independently hits INDU through
the rate/NIM-adjacent channel. **Rule A6 applied**: naming INDU's own fuel-cost-exposed nodes and
reading their disclosed spend, rather than asserting the channel qualitatively.

**Union Pacific (UNP), FY2025 10-K, filed 2026-02-06** — Fuel expense **$2,390 million of $14,664
million total operating expenses = 16.3% of opex**, down 3% YoY on a **6% decrease in locomotive diesel
price** ($2.64/gal → $2.49/gal). The filing's own mechanism for a fuel spike: **"our fuel surcharge
programs trail increases or decreases in fuel prices by approximately two months"** — fuel surcharge
revenue was **$2.3bn in 2025 vs $2.6bn in 2024**. ⇒ **a Hormuz-driven fuel spike hits UNP's cost line
immediately; the offsetting surcharge revenue arrives roughly two months later** — a timing mismatch
that is negative on any window shorter than the lag, consistent with **M437** (carried, not re-derived:
"the rails' fuel-surcharge lever is NET NEGATIVE on a full-year basis"), now with the mechanism dated.

**Delta Air Lines (DAL), FY2025 10-K** — **"Fuel expense represented approximately 17% of our total
operating expense during 2025"** ($9,819 million), and, verbatim: **"Fuel prices have historically been
volatile due to many factors, including geopolitical events."** Unlike the rails, **airlines carry no
surcharge pass-through mechanism** in the filing language — DAL's own Monroe refinery covers
**"approximately 75% of our consumption"** as the filing's stated natural hedge, leaving ~25% of
consumption fully exposed to spot jet fuel.

⇒ **Two INDU nodes, two different exposure shapes, both quantified and both primary-sourced**: rails
carry ~16% opex fuel cost with a ~2-month revenue-recovery lag (short-term margin risk, full-year
neutral-to-negative per M437); this airline carries ~17% opex fuel cost with no surcharge and a
75%-covering refinery hedge. **Both mechanisms fire on the same correlated tail PREMORTEM flagged**: a
Hormuz-hardening event that also raises CPI odds hits INDU's transports directly (fuel cost) and the
sector's cap-weighted names indirectly (the rate/regime channel), through one shared cause, not two.
**DAL's flow this run**: 0.106 🟡중립 (rs20 +2.1, rs60 +24.4) — **RS named in the same paragraph as no
OBV claim here (no D6 trigger)**; **UNP is not on today's shortlist or greens** (flow not separately
re-pulled this run; carried at the filing level only, price axis not re-derived).

---

## §3 · The registry gap — a proposal, not an edit

PREMORTEM §4c (reproduced, not re-derived): **CAT, EMR and AME appear in no row of
`data/cycles/cycle_registry.json` at any layer**, while **GEV is already present** in the rank-1
AI-compute cycle's `adjacent` layer. This stage checked what evidence, if any, would support adding the
other three, using the same primary-filing method as the GEV/CAT ranking carried from 08-07/08-08:

| Candidate | Layer proposed | Evidence found this run | Confidence |
|---|---|---|---|
| **CAT** | `adjacent`, AI-compute rank-1 (same tier as GEV) | Carried from 08-08: Q1 power-gen sales **"+41% YoY driven primarily by data center applications"** — a quantified, dated, segment-level disclosure, same class as GEV's RPO language | **High** — same evidentiary bar GEV already cleared |
| **AME** | `fuel` (adjacent-of-adjacent), not `adjacent` | FY2024 10-K names **"data centers" once**, as one of ~10 end-markets listed for the Electromechanical Group's UPS/electric-meter/smart-grid products — real but thin, generic, non-headline | **Low-moderate** — disclosed but not segment-quantified |
| **EMR** | Not supported on evidence gathered | **Zero** "data center" or "hyperscal-" mentions in the captured Item-1 Business + Item-7 MD&A text (≈61K characters, `--no-xbrl` excerpt; `--full` not pulled this run, so a discrete Automation Solutions segment disclosure outside this excerpt cannot be ruled out) | **Unresolved** — human should re-run `module_business_us EMR --full` before deciding, not this stage's job (P5) |

**What a correct CAT row would contain**, concretely: `epicenter: [...existing...]` unchanged;
`adjacent: [..., "CAT"]` appended alongside GEV/ETN/VRT/PWR; the same `core_pick_why`-style one-line
citation this registry already uses for its human-locked picks, e.g. *"CAT power-gen segment sales
+41% YoY, 'driven primarily by data center applications' (Q1 print, Reuters/Motley Fool 08-03/04) —
same disclosure class as GEV's RPO language, both currently among the board's worst-flowed names
(§1, §0), i.e. an adjacent-layer add on demand evidence, not on price."** **Not written to the file —
`data/cycles/cycle_registry.json` is human-curated (md-ledger discipline stated in the file's own
`_note`), and this is a proposal for that human pass.**

---

## §4 · Dispersion inside the sector — the sub-node spread exceeds the sector's own move

MACRO §C: **XLI exc60 vs SPY = +1.46**, the sector's own single number. **Within INDU today**
(`SECTOR_FLOW_US.json`, n=50, RS60 vs SPY): the range runs from **AXON +40.3** to **GEV/CAT −12.4**, a
**52.7pp spread** — 36× the sector's own 60-day excess. On flow_score, the spread is **EMR/TRI +0.911
to GEV −0.850 = 1.761**, against a sector eqflow of **+0.098**. ⇒ **XLI's own excess-vs-SPY print is
not a usable description of what is happening inside Industrials this run — it averages out a name
(AXON) running 40 points ahead of SPY over 60 days against two names (GEV, CAT) running 12 points
behind it, and the OW verdict itself rests on one name's base (§1) inside that spread.** **The sector
label is the wrong unit here**, consistent with the same finding SWEEP §2a made about Materials being
one name (LIN/NEM) wearing an 11-sector aggregate.

---

## §5 · Value-chain map — 5–8 nodes, binding constraint named at each layer that has one

Carrying the Kilby/turbine-OEM chain from 08-08 by reference (not reprinted: node ranking
PWR>ETN≫AME>EMR, the Chevron-exec "reserved a year and a half ago" quote, the 10-year LTSA horizon).
**Adding one layer this run** — the MEP/installation contractor, surfaced by chain-hop (§6):

| # | Node | Representative names | Binding constraint (if identified) |
|---|---|---|---|
| 1 | Hyperscaler capex commitment (demand signal) | not INDU — MSFT/CVX Kilby JV, carried | — (demand-side, out of sector) |
| 2 | Gas-turbine / heavy-genset OEM | **GEV, CAT** | **Turbine manufacturing lead time**, carried 08-08: equipment for Kilby "reserved very early — a year and a half ago"; GEV's own installed base ~7,000 units with ~10-year average remaining LTSA life. **Not demand-constrained — the desk's carried finding stands.** |
| 3 | Electrical distribution / power-quality equipment | EMR, AME, ETN, PWR | Carried 08-08: no fresh filing pull this run (§1c notes EMR's disclosure gap specifically) |
| 4 | **Data-centre mechanical/electrical (MEP) install** | **FIX (new this run)** | **Skilled-trades labor, by the filing's own revenue mix**: 63.2% of FIX's FY2025 revenue is "installation services in newly constructed facilities" — a field-labor-bound activity, a different constraint class from node 2's factory lead time |
| 5 | Rail / air transport (fuel-cost-exposed logistics) | **UNP, DAL** (§2) | Fuel-surcharge recovery lag (rails, ~2mo) / uncovered spot exposure (~25% of airline consumption) — the correlated-tail node named in §2, not previously mapped here |
| 6 | Aerospace & defense (PH's actual driver) | **PH**, RTX, LMT | Carried 08-07: LMT backlog $193.6bn+9.9%, FMS booked; not re-derived this run |
| 7 | Diversified industrial recovery (PH's other leg) | PH | Not separately isolated from node 6 in the filing text pulled |
| 8 | Information/legal-tech (TRI's driver, unrelated to 2–7) | TRI | Not chain-mapped — outside the AI-power/aerospace value chains entirely; flagged in §1c as evidence the sector's breadth is not one chain |

---

## §6 · Chain-hop candidates — body-proximate only, flow cross-checked

`module_news_data chain-hop "data center" power grid --days 7 --scope foreign` (1,500 articles scanned).
**Headline-named and disqualified as candidates (already crowded)**: GEV (11 headline/16 body), CAT
(22/24) — both already the sector's tracked names.

**Body-proximate, non-headline candidates, verified against primary filings before being called
candidates (not on the co-mention alone)**:

- **FIX (Comfort Systems USA)** — 4 proximity hits, e.g. *"Buy 5 Top-Ranked Growth Stocks for August to
  Tap Market Rally."* **Verified**: FIX's own FY2025 10-K MD&A states **"the increase in demand has been
  especially strong in the technology sector, particularly for data centers,"** with total revenue
  **$9,101,641K (+29.5% vs $7,027,476K in 2024)**, Mechanical segment 73.3% of revenue. **This clears the
  body-proximity bar with a primary-filing confirmation.** ⇒ **Flow cross-check**: flow_score **−0.690
  🔴분산**, `module_chart`-independent OBV not pulled this run but sector_flow's own OBV **분산 −0.194**,
  paired here with **rs20 −5.9 / rs60 −20.7 (D6 compliant)**. **A third instance of this run's carried
  "best-disclosed = worst-flowed" pattern** (after GEV, and CAT's post-beat fade), now at the
  installation layer rather than the OEM layer.
- **MMM** — 12 proximity hits (Elon Musk grid-power commentary, listicle-adjacent). **Verified, weaker**:
  MMM's 10-K lists **"Solutions for data centers"** as one line among ~15 diversified product categories
  in the Electronics & Energy segment — real, but not segment-quantified the way FIX's or CAT's language
  is. Flow_score **0.506 🟡중립**, OBV 매집 +0.284 (paired with rs20 +13.7/rs60 +23.0, D6 compliant) — **no
  inversion here**; disclosure and flow are roughly aligned, which is the less interesting case and is
  recorded as such rather than promoted.

⚠ **Tool gap carried from 08-08, unchanged**: Texas Pacific Land (TPL) and Engine No. 1, named directly
in the Kilby primary source, still do not surface in chain-hop's entity matching (`[C3, unmeasured]`).

---

## §7 · Track-KPIs and anti-signals — dated observables

1. **The mechanical decay test on EMR/AME/CAT's "compressed" share (§1a)**: the 08-04 print exits the
   20-session lookback window around **2026-09-02**. If, at that date, their 21–60d base has turned
   positive on a fresh pull, the compression read was purely a lookback-window artifact and this run's
   distinction from PH weakens. If the base is still flat-to-negative once the print-day sessions roll
   out of the 20d window, the "sold-the-print, not accumulated" read (already carried for CAT from
   08-08) strengthens for EMR/AME too.
2. **PH's revision-breadth follow-through**: current-Q and next-Q are 1↑/0↓ clean today. **A downgrade
   appearing in either window within 30 days** would be the first crack in the "genuinely live" read.
3. **AME's `module_chart`-flagged bearish divergence**: re-pull `module_chart AME --read` at the next
   settle; **a divergence that resolves via RSI catching up (not price falling) would be the
   anti-signal that reopens AME**, distinct from a price-led resolution.
4. **FIX (§6, new)**: rs20 −5.9/rs60 −20.7 against a filing-confirmed, growing data-centre revenue line
   — **a print above 0 on rs20 with OBV turning to 매집 (sector_flow) or 누적 (module_chart) closes this
   run's inversion; a continued slide despite Q3 results (FIX's next 8-K, date not yet filed) would
   argue the market is pricing something the filing doesn't disclose (labor cost, margin compression on
   fixed-price MEP contracts) — flagged, not measured, this run.**
5. **UNP/DAL fuel-surcharge and CASM prints** (§2) at their next 10-Q — the first post-08-10 read on
   whether the correlated Hormuz/CPI tail (PREMORTEM §2d) actually moved INDU's transport-node costs.
6. **Carried unchanged from 08-08** (§8 below): GEV's next 8-K (Wind-segment loss narrowing/widening,
   next earnings 2026-10-28), CAT rs20 crossing back above 0 (re-check 2026-08-14), GEV's "125 GW under
   contract by year end" marker, PWR's rs20 (flat at −0.4 on 08-08's pull, not re-derived this run).

---

## §8 · Carried unchanged, by reference (not re-derived this run)

- Kilby turbine chain at primary level: Chevron exec quote, GEV/CAT allocation timing, immateriality to
  GEV's backlog (08-08 file §1b).
- PWR>ETN≫AME>EMR primary-filing data-centre-disclosure ranking (08-07 file §2); **§1c above narrows
  this further — EMR's captured text shows zero data-centre mentions, consistent with its last-place
  rank in that ordering.**
- LMT/Saudi defence-substitution refutation (08-07 file §3): backlog $193.6bn +9.9%, FMS booked, 60-day
  DSCA search empty.
- **S64** (do N+ Energy and OW− Industrials take the same crude tick in opposite directions?) settles
  **08-13**; first live test (08-07) went against the hypothesis (crude +1.15%, both XLE and XLI fell vs
  SPY). **M437 stands**: do not re-argue crude weakness as an Industrials tailwind — **§2 above is the
  same finding, now with the fuel-surcharge mechanism dated at the filing level.**
- Sector line, unrelated to today's breadth question: n=50 · wflow **+0.041** / eqflow **+0.098**
  (breadth-led) · 5🟢/9🔴 (today's greens: EMR, TRI, PH, AME, BA — **not** the 3-name set ROTATION/
  PREMORTEM's shortlist table cites; BA and TRI are also green today and are addressed in §1c/§4, not
  omitted).

**No position sizing and no buy/sell language appears anywhere in this file (P4).**
