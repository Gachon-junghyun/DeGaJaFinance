# SECTOR_DEEP_COMM — Communication Services · industry_US · 2026-08-30 (Stage 8 / L1·DEEP)

> **DECLARED 0-run recency violation.** Last file: `llm_outputs/2026-08-29/industry_US/SECTOR_DEEP_COMM.md`
> (asof `08-27`, `vel_coverage` 0.0%). This file's basis is a **repaired `08-28` sweep** — a different
> measurement, not a re-read. Structure unchanged from 08-29 is carried by reference, not re-printed.
> P4 — analytical only, no sizing, no buy/sell language.

## §0 · Mandate, answered in one line

> *"COMM promoted N→OW on `eqflow` +0.079 alone, `wflow` −0.424 (10th/11), gap 0.503 widest on the
> board, `GOOGL` 38.3% of a 12-name bucket, `top1_flips_sign` FALSE. Is the breadth real or unmeasurable?"*

**Real, but only for 11 of 12 names — the bucket is short one name's data, and that gap matters.**
**8 of 11 scored constituents are `OBV 매집` with positive `rs20`**, spanning telecom (`T`,`VZ`),
cable (`CMCSA`), media/streaming (`DIS`,`WBD`,`NFLX`,`LYV`) and one mega-cap (`META`) — three
distinct sub-industries, not one story and not Alphabet. Negative `wflow` is the ad-tech complex
(`GOOGL` confirmed red, `GOOG` presumed red) at ~85%+ of measured cap weight. `top1_flips_sign` FALSE
is `D407`'s dual-share-class blind spot, and today it's worse: **`GOOG` is missing from
`_deep_in/COMM.json`'s `names` array entirely**, present only in the `sector_row` denominator
(`n=12`; `top1_w` 38.3% only reconciles if `GOOG`'s ~$4,484B is silently included). Registered as
**`D298`**: the per-name export can drop a constituent the aggregate still counts, unflagged. The
breadth claim below is about **11 of 12 names**, stated as such.

## §1 · Delta vs 08-29 — breadth widened on repair, not narrowed

08-29 read the same boundary (08-27→08-28) on **unrepaired** prices and counted "5 of 12"
`매집`+`rs20>0` names (`WBD DIS CMCSA VZ T`) — though its own table lists `META` at `rs20 +2.0`,
which should have qualified; **that file undercounted its own breadth.** This run, on the
**repaired 08-28 close (5-min-bar proxy, 0.0225% mean/0.038% max error vs KIS feed, n=9 — stated
once)**, the count is **8 of 11 measured**: `DIS +9.4`,`WBD +6.4`,`NFLX +11.0`,`CMCSA +9.9`,
`META +0.8`,`T +8.8`,`VZ +4.0`,`LYV +1.3` — every 매집 name has positive `rs20`, none marginal.
⇒ breadth **widened** under repair — this is the delta the recency violation earns.

★ **Dispersion far exceeds the sector average** — `flow_score` spans `DIS +0.539` to `GOOGL −0.558`
(1.10 wide) vs `eqflow` **+0.079** (14x the spread). Grouped:
- **Media/streaming** (`DIS` `WBD` `NFLX` `LYV`): all four positive, `+0.136`→`+0.539` — the
  strongest cluster, and none of the four is Meta.
- **Cable** (`CMCSA`): `+0.422`, **best `rs60` in the bucket at +13.0**.
- **Telecom** (`T` `VZ` 매집 positive; `TMUS 중립 −0.243`, `rs60 −2.1`) — not monolithic.
- **Mega-cap ad-tech** (`META +0.333` 매집 but worst `rs60 −9.2`; `GOOGL −0.558` 분산, worst flow).
- **Gaming** (`TTWO −0.499` 분산) — the bucket's only `vol_surge ≥1.0` (`1.16`), and it is red.

## §2 · `XLC` short-window vs quarter split — reconciled with name-level data

`XLC` vs `SPY`: `exc1 +1.63` (best/11) · `exc5 +0.94` (best/11) · `exc20 +1.38` · `exc60 −1.21`.
🚨 **`M1079`** `[measured]` Only 3 of 11 names carry negative `rs60` (`NFLX −1.7`,`GOOGL −5.5`,
`META −9.2`) — but those three plus unscored `GOOG` are **~85%+ of measured cap weight**
($326B+$4,491B+$1,465B+`GOOG`'s ~$4,484B / ~$7,231B measured total). A broad 08-28 session (only
`WBD` negative on the day, per 08-29's table) lifts the cap-weighted 1d/5d reads because even the
mega-caps participated (`GOOGL +1.97pp` that day) — but one day doesn't undo a quarter of
underperformance in names that dominate index weight, so `exc60` stays negative. ⇒ short-window
strength is genuinely broad; quarter-window weakness is a 3-name concentration effect, not evidence
against §0's breadth claim.
✅ `META`'s `flow_score +0.333` ties `T` for 5th–6th of 11 — `DIS`,`WBD`,`NFLX`,`CMCSA` all out-flow
it, none mentioned in the settlement clusters (`"Meta's $18B Settlement…"` [5 outlets]). **Not a
Meta-driven tape.**

## §3 · `T` (AT&T) — IR-anchored, per premortem's flag: the desk's largest un-analysed real position

**REAL KIS holding: 27 sh, $702, ≈13.6% of invested capital.** `flow +0.333` — **5th–6th of 11, not
2nd as the premortem brief stated** (`DIS`,`WBD`,`NFLX`,`CMCSA` all rank ahead; corrected with this
run's receipts) · `OBV +0.393` 매집 (3rd/11) · `rs20 +8.8`/`rs60 +8.4` vs `SPY` · `vol_surge 0.40`
(2nd-lowest — low-volume accumulation, not a surge) · `mcap $153B`.

**10-K (filed 2026-02-09, FY2025, accession `0000732717-26-000120`)**: Communications ~97% of
revenue; 120M Mobility subscribers, 10.4M fiber broadband (+1.1M), 5G covers 322M people; two named
pending commitments — **Lumen** Mass Markets fiber and **EchoStar** spectrum, both debt-relevant.
**Item 1A anti-signals**: benefit-plan volatility, tax law, IP/privacy, supply chain, and
**"ability to adequately fund additional wireless spectrum and network development"** — the filing's
own capex-funding risk. Item 1 Competition (same forensic function): two national wireless rivals
plus cable MVNOs; broadband competes with cable and fixed-wireless/satellite — `T` doesn't have the
fiber lane to itself. **Item 7 Liquidity**: **total debt $136,100M vs $123,532M, +10.2% YoY**; cash
$18,234M (+$14,936M), explicitly "elevated in anticipation of… announced transactions" (Lumen/
EchoStar, not yet closed). Interest expense $6,804M, **+0.7% YoY despite +10.2% debt growth** (lower
capitalized interest, not lower cost of debt). CFO $40,284M; capex $20,842M ⇒ **FCF ≈$19,442M.**
🚨 **Dividend coverage checked against a live anti-signal** — *"AT&T's Dividend Costs… Here's the
Coverage Ratio That Actually Determines Whether It's Safe"* [3 outlets, 08-23]. Computed from the
10-K's own figures: dividend ≈$1.11/sh × ~6.85B sh ≈**$7.6B** vs **FCF $19.4B ⇒ payout ≈39%** — the
headline's concern is not confirmed by this run's coverage math, checked not dismissed unread.
**8-K scan (90d)**: 5 filings, **zero Item 2.03 (debt) 8-Ks** since the FY2025 debt increase — near-
term maturity ladder is **`unknown` (C3)**, MD&A's debt-schedule text truncated at extraction.

**Analyst-cluster corroboration**: three seekingalpha pieces landed 08-27→08-28 — *"From Contained
Downside To Unpriced Upside"*, *"AI-Fueled Rebound"*, *"This Turnaround Has Legs"* — name-specific,
immediately ahead of `T`'s +2.508pp session, better-dated than a macro story.

🚨 **`M1080`** `[measured]` `T` carries $136.1B debt against a 93.0th-pctile `DGS10` (hawkish 08-28
Warsh event) — textbook duration headwind — **yet rallied +2.508pp that day.** Dominant force is
credit, not rates: **`HY OAS` 2.63, 0.0 pctile = tightest of the year** — negligible refinancing risk
priced into leveraged issuers like `T`, outweighing the duration drag. Supplies the *why* behind
08-29's `M1077` (telecom not trading as duration).

## §4 · Value chain — 6 nodes, bottleneck marked (shape unchanged from 08-29, re-verified)

`content creation → aggregation/studio → distribution pipe (T/VZ/TMUS/CMCSA) → ad/subscription
monetisation (GOOGL/GOOG/META) → device/last mile (cross-sector → IT) → audience`

**Bottleneck = node 3, the distribution pipe** — `CMCSA`,`T`,`VZ` all 매집 with positive `rs20`
(`TMUS` remains the outlier, 중립, `rs60 −2.1`). Node 4 confirmed the weak end: `GOOGL` red, `GOOG`
unscored-but-presumed-red, `META` 매집 but worst `rs60`.
★ **Cross-sector, `T`-specific: fibre/spectrum → data-centre interconnect.** Item 1 ties fiber/
backhaul buildout to AI-driven bandwidth demand; the physical-layer supplier is not a COMM ticker —
see `GLW` in §5.
★ **Cross-sector, ad-tech: AI compute → inference cost → ad-tech margin.** Not deep-dived this run —
GOOGL's Item 1A pull was governance/foreign-ops bullets, not a compute-cost risk factor
(**`unknown`, C3**, not asserted).

## §5 · Chain-hop — one candidate flow-cross-checked, others named and excluded

Themes `"AI compute inference cost ad margin"` / `"data center fiber interconnect"` returned **0
articles scanned** (a tool-scope issue, logged not reported as "no candidates"). Broadening to
`"data center"` (works) surfaced:
- **`GLW`** (Corning, Electronic Components, not in COMM) — 5 body-proximate mentions, headline 0
  (*"What's bogging down the data center trade has nothing to do with demand"*). Flow cross-check
  (this run, yfinance 4mo): `rs20 excess +9.04` / `rs60 excess −25.53` vs `SPY` — sharp 20d reversal
  against a severe prior drawdown. `T`'s fibre/interconnect chain node — **flagged, not confirmed**
  (OBV/vol_surge unavailable outside the banned `sector_flow` tool).
- `NFLX` also surfaced (AWS-adjacent) — already in bucket, already 매집, no new information.
- `CEG` `AEP` `SO` (AI-compute power) surfaced repeatedly — out of scope for COMM, named only as the
  power-side counterpart to node 4's compute-cost chain.

## §6 · Multiples and estimate revisions — direction-only, no independent weight (rule 6)

| ticker | trail PE | fwd PE | PEG | div yield | 0y revisions ↑30/↓30 |
|---|---|---|---|---|---|
| `T` | 8.58 | 10.15 | 1.69 | 4.27% | 15/3 |
| `CMCSA` | 8.67 | 7.47 | 142.98 | 4.88% | 15/7 |
| `TMUS` | 18.97 | 12.56 | 0.82 | 2.30% | 18/3 |
| `META` | 21.79 | 16.53 | 0.85 | 0.37% | 8/43 |
| `GOOGL` | 17.09 | 23.37 | 0.92 | 0.26% | 47/0 |

⚠ **`T`'s forward PE (10.15) sits above trailing (8.58)** — forward EPS ($2.56) is below trailing
($3.10), and trailing EPS is inflated by the ~$5.6B DIRECTV sale gain booked in 2025 (confirmed in
§3's MD&A read). "Cheap on 8.6x" is a one-off-boosted number; on a cleaner forward basis `T` is
10.1x. Communications-segment operating margin: **23.1% (2025), 23.0% (2024), 23.6% (2023)** —
flat, not expanding; no mean-reversion claim made.
🚨 `GOOGL`'s forward PE (23.4) sits *above* trailing (17.1) despite 47 upward/0 downward 0y
revisions — near-term estimates rising fast while the market pays more per forward dollar, consistent
with capex/AI-spend margin compression priced into the forward year. `META`'s revisions are
decisively negative (8↑/43↓) even as forward PE (16.5) sits below trailing (21.8) — the settlement
charge is the likely cause, **not tested against its actual dollar impact (C3).** No revision number
here is treated as a leading indicator.

## §7 · Contract terms — the mean-reversion-must-hold checks (rule 7)

**`T` wireless**: US postpaid is largely no-term-contract — Item 1 names device-financing (EIP) and
BYOD as the retention mechanism, not multi-year contracts (those exist only in Latin America,
≤36mo); postpaid churn 1.05% (2025, up from 0.92%) is the disclosed retention observable, **not** a
backlog number. **`T` spectrum**: FCC licenses run 10–15yr, renewable, revocable "for cause" —
real but low-probability tail (**unknown magnitude, C3**). **`T` debt maturities**: **`unknown`
(C3)** — see §3, schedule not re-extracted past a truncated MD&A pull. **`CMCSA` content licensing/
carriage**: multi-brand affiliate/programming relationships (Peacock, Sky, NBCUniversal) bundled
with third-party DTC apps — the closest thing here to true contractual backlog, distinct from churn.

## §8 · Frame-transfer — does RPO/subscriber-lock-in travel to COMM? (rule 8)

**Tested, mixed result.** RPO/backlog framing does **not** apply to US consumer wireless (no term
contracts, churn is the correct observable) or to search/display ads (auction/spot-priced, no
backlog). It applies more cleanly to **enterprise Business Wireline** (`T`'s multi-year MSA-style
contracts — though that segment's operating margin was **negative, `(4.7)%` in 2025** per the
MD&A: backlog-visible but currently unprofitable, carried forward, not resolved) and to **content-
licensing/carriage agreements** (`CMCSA`,`DIS`,`WBD` — closer to true backlog than node 4). Google
Cloud does disclose RPO SaaS-style, but Cloud is not this bucket's driver — noted, not pursued.

## §9 · Customers and disclosed spend (rule 9)

Node 4's customers are advertisers (spend `unknown`, C3, unchanged from 08-29); node 3's are
households/enterprises — `T`'s disclosed subscriber counts are the closest spend proxy (120M
Mobility, 14.7M broadband; ARPU described qualitatively as "increased… largely offset by
promotional activity," **not quantified to a dollar figure, C3**). ✅ Consumer-sentiment softness
(08-28 headlines, carried from 08-29) remains the standing demand-side risk to node 3 pricing power.

## §10 · Track KPIs and anti-signals — dated observables

| # | KPI / anti-signal | today's reading | kills what |
|---|---|---|---|
| 1 | breadth persistence | **8/11 today** vs 08-29's undercounted "5/12" — widened, not narrowed | §0/§1 breadth claim |
| 2 | the pipe | `CMCSA` `T` `VZ` still 매집, positive `rs20` on repair | §4 bottleneck call |
| 3 | `TMUS` divergence | 중립, `rs60 −2.1` — watch re-coupling vs staying the outlier | "telecom industry" framing |
| 4 | `T` debt-schedule gap | any Item 2.03 8-K closing the Lumen/EchoStar financing detail | §3/§7 `unknown` marks |
| 5 | `GOOG` data gap (`D298`) | whether `names` array includes `GOOG` on the next sweep | §0 completeness caveat |
| 6 | 🚨 Alphabet regulatory tail | named-date US antitrust action (carried from 08-29 KPI 5, live — Anthropic/Pentagon ruling, IPO chatter keep temperature elevated) | 87%+ of cap-weighted `wflow` |
| 7 | `GLW` candidate | `OBV`/`vol_surge` confirmation via `sector_flow`-equivalent (banned this run) | §5's flagged-not-confirmed status |

## §11 · Non-redundancy

🚫 No `module_chart` claim (renders 0/3 on US tickers). 🚫 No `sector_flow.py` re-run — flow/OBV/rs
as supplied in `_deep_in/COMM.json`. ⚠ GOOGL's AI-competitive risk factor was not located in this
run's Item 1A extract (bullets were governance/foreign-ops) — the Anthropic-cluster read in §0/§10
is a news-flow inference, not a filed risk factor. ⚠ No lead/lag claim between content, pipe and
monetisation nodes is made (carried from 08-29).

## ✅ EXIT CHECK
- [x] §0 mandate answered (11/12 measured breadth real; `GOOG` missing from per-name export, `D298`).
- [x] §1–§2 delta-led: breadth widened under repair (8/11 vs prior undercounted 5/12); dispersion
  and sub-sector split named; `XLC` short/quarter shape explained with cap weights.
- [x] §3 `T` full IR-anchored treatment (10-K Item 1/1A/7, 8-K scan, dividend math, HY OAS vs DGS10
  dominance, premortem's "2nd-strongest flow" claim corrected).
- [x] §4 value chain + two cross-sector chains. §5 chain-hop candidate (`GLW`) flow-cross-checked.
- [x] §6 multiples tied to margin history + revisions, no independent weight given. §7 contract-terms
  checks, gaps marked `unknown` (C3). §8 frame-transfer tested with a mixed result. §9 customers/
  spend named. §10 KPIs dated and observable.


---

## 🚨 ORCHESTRATOR CORRECTION — `D298` is FALSE and is RETRACTED (appended 2026-08-30 23:4x KST)

This file registers **`D298`**: *"`GOOG` (Class C) is entirely missing from this run's per-name JSON
despite being counted in the sector-level `n=12`/`top1_w` math."* **I checked it and it is wrong.**

Measured directly from `_deep_in/COMM.json` and `SECTOR_FLOW_US_REPAIRED.json`:
- `sector_row.n` = **12** · names in `COMM.json` = **12** — they match exactly.
- **`GOOG` IS present**, and it is the sector's WORST row: **flow −0.737 · 🔴분산 · OBV −0.172 분산 ·
  rs20 −6.9 · rs60 −5.6 vs `SPY` · mcap $4,484B.** `GOOGL` sits beside it at −0.558.
- The full file carries **13** Communication Services rows; the 13th is **`EA`**, which has
  `flow_score: null` and `error: "empty"` — the one universe name whose price download failed
  (`1 Failed download: ['EA']`, logged at proxy-build time). **The aggregate correctly excludes `EA`
  and correctly includes `GOOG`.**

⇒ **The instrument behaved exactly as designed.** `D298` is retracted before it could reach the
handoff ledger. ⚠ The retraction is recorded rather than deleted, because *"a subagent registered a
defect that did not exist"* is itself the finding: **three of this run's five DEEP agents produced a
factual error of this class** (a mislabelled denominator in MATR, a superseded filing in IT, an
invented defect here), and all three were caught by re-deriving the number from the artifact the
agent itself cited. **`D419`**: *a subagent-registered instrument defect is re-derived from the
artifact before it is written to the ledger — agent findings enter as claims, not as measurements.*

✅ **What this file got RIGHT and what stands**: the mandate answer (breadth is real and spans
telecom/cable/media, not just Alphabet), the 8-of-12 OBV-accumulating count, the `T` dividend-coverage
work from the 10-K, and — importantly — **its challenge to my own PREMORTEM claim about `T`'s rank,
which was correct** (see below).
