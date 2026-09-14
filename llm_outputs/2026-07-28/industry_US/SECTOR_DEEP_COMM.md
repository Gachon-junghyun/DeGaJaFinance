# SECTOR_DEEP_COMM — industry_US — 2026-07-28 (Tue) · **ROTATING → full fresh map**

> ★ **The first DEEP file this desk has ever written on Communication Services.** Verified against the
> visible history (`llm_outputs/2026-07-21 → 07-27/industry_US/`): **zero prior `SECTOR_DEEP_COMM.md`.**
> Picked by `SECTOR_ROTATION.md` §4 as a **stated deviation** from "next-highest OW" (COMM is N).
> Flow `asof 2026-07-27 settled`. Benchmark **SPY** inline (C1). Analytical only (P4).
> ⚠ **Written in-run, not by a subagent** — see `BLINDSPOT_PREMORTEM.md` §0.

---

## 1 · Why this sector, in flow numbers

`SECTOR_FLOW_US.json`: **n 13 · wflow +0.109 · eqflow +0.079 · gap only 0.030 ⇒ NOT mega-cap-narrow ·
breadth 0.15 (3rd best of eleven) · 🟢 2 / 🔴 3 · Δd/d +0.173 = the LARGEST positive delta on the board.**

★ And the single fact that made it a pick: **T's flow score is +0.921 — the highest of all 300 names**,
on **`vol_surge` 1.74 with `velocity` None**, i.e. **a volume path, not one of the 14 velocity-path
greens** (SWEEP §4). **T is also one of the two names STANDING_VIEW §3a names as an unowned coverage
gap** — *"the shortlist's #1 flow, no thesis in any desk file"* — and its ledger zero is a **D65 tool
artifact** (T is one of 28 tickers `module_report_tags` silently refuses to index), **not an absence.**

⚠ **Sector caveat, stated up front**: **13 names, of which GOOG and GOOGL are the same company filed
twice** ⇒ the effective n is **12**, and **GOOG+GOOGL are $8,975bn of a sector whose next-largest name
is $326bn.** **Any mcap-weighted COMM number is an Alphabet number** (the C5 arbitrary-choice rule made
explicit). This file therefore reads the sector **equal-weight and by node**, and says so.

---

## 2 · ★★★ The finding: the board's #1 flow score is a post-earnings drift, not a discovered trend

**`module_disclosure_us T --days 30`, primary:**

| Date | Filing | Content |
|---|---|---|
| **2026-07-22** | **8-K Item 2.02 + 10-Q** | **Q2 results** |
| 2026-07-02 | **8 × Form 4** | insider transactions |
| **2026-07-27** | ★ **FWP** | **a free writing prospectus — a debt offering marketed the day BEFORE the flow snapshot** |

**The print, body-read** `[news, 4 outlets]`: *"AT&T tops Q2 profit expectations **despite revenue
miss**, **accelerates share repurchases**"* [seekingalpha 07-22]; GAAP earnings **$4.591bn** [nasdaq];
*"AT&T Stock Rises After Earnings. **So Much for SpaceX Fears.**"* [yahoo_finance].

⇒ ★★ **The flow snapshot is 2026-07-27 and the print was 2026-07-22 — three sessions earlier. T's
#1-of-300 flow score is substantially a post-earnings, buyback-accelerated drift.**
**This is D51's exact pattern** — *"no stage checks whether a flow reading post-dates a corporate event
by 0–2 sessions"* — reproduced at **three** sessions, on the strongest single flow reading on the
board. **It is named here rather than re-used as independent confirmation**, which is precisely what
the 07-27 rail DEEP had to do with CSX/UNP/NSC.

### And the fundamentals invert the usual trap

| | T |
|---|---|
| Price / mcap | **$25.16 / $172bn** · beta **0.42** · dividend **4.55%** |
| Multiple | trailing P/E **8.30** · **forward P/E 9.80** |
| ⚠ Direction of the denominator | ★★ **trailing EPS $3.03 → forward EPS $2.57. The forward multiple is HIGHER than the trailing one because the denominator is FALLING** |
| Estimate momentum, 90d | current quarter **−1.1%** · **next quarter −3.9%** · this year +0.9% · next year +0.5% |
| Revision breadth, 30d | this year **1↑ : 2↓** · next year **1↑ : 2↓** |
| Consensus | mean target **$28.71 = +14.1%**; 4 Strong Buy / 12 Buy / 9 Hold / 1 Sell |
| **Margin percentile (lens L2)** | ⛔ **UNOBTAINABLE.** `margin_history.py T` returns a series that **stops at FY2014** — 8 years, FY2007–2014, max 60.6%, median 58.7%. **The last 11 years are missing.** |

⇒ **L2 forbids calling T cheap without a margin percentile, one cannot be built, and this file does not
call it cheap.** ★ **The honest statement is the inverse of the peak-margin trap and also of M175's UPS
case**: **T's 9.80× sits on a shrinking forward EPS with negative near-term revision breadth.** A low
multiple on a **falling** denominator is not cheapness either — it is a de-rating in progress that the
tape has not yet expressed, while **the flow says the opposite.**
★ **New dig instance (D91)**: `margin_history.py` is documented as failing on **KR** tickers (D70);
**here it truncates silently on a US mega-cap at FY2014 and reports the truncated series as if
complete.** A silent truncation reads as "this is the history."

---

## 3 · Node map — 5 nodes, built BY HAND, with the sector's own flow

⚠ **`chain-hop` is unusable this run** (D58 silent zeros on 3-token queries; D10 boilerplate dominating
single-token queries). **This map is hand-built from `SECTOR_FLOW_US.json`; no un-named-beneficiary
coverage is claimed.**

| Node | Names | flow · RS20 / RS60 vs SPY | Tag |
|---|---|---|---|
| **① Telecom carriers** | **T** +0.921 · **+6.1 / −9.0**, `vol_surge` **1.74** | ★ the sector's #1 | **🟢 volume path** |
| | **VZ** −0.315 · +0.3 / −2.3, OBV **분산** · **TMUS** +0.062 · −4.4 / **−14.4** | | 🟡 / 🟡 |
| **② Digital advertising** | **GOOGL** +0.086 · **−4.6 / −10.5** (`velocity` 2.45) · **GOOG** +0.022 · −3.8 / −9.8, OBV **분산** · **META** +0.539 · **+6.5 / −15.1** (`vol_surge` **0.65**) | | 🟡 · **🔴** · **🟢 velocity** |
| **③ Streaming / studios** | **NFLX** −0.062 · **−6.0 / −27.4** (`velocity` **3.18** — the sector's loudest news on the sector's worst RS60) · **DIS** −0.428 · −3.6 / −8.5 · **WBD** −0.522 · **−6.8 / −10.4** | | 🟡 · **🔴** · **🔴** |
| **④ Interactive entertainment** | **EA** +0.415 · +0.5 / −0.7, `vol_surge` **1.11**, OBV 매집 · **TTWO** −0.040 · +0.9 / **+9.4** | | 🟡 · 🟡 |
| **⑤ Cable / live events** | **CMCSA** +0.258 · −3.0 / **−18.7** · **LYV** +0.097 · −1.4 / **+13.3** | | 🟡 · 🟡 |

**The binding constraint in this sector is not supply — it is ATTENTION SHARE and its capex.** Two
nodes are spending against each other: **② is funding AI inference** (GOOGL's Q2 capex **+100.1% YoY**
with **FCF −$5.86bn and $49.6bn of equity raised**, M132/M134) while **① is funding fibre and spectrum
and returning cash** (T accelerating buybacks and marketing debt on 07-27). ⇒ **The two nodes have
opposite cash-flow signs inside one GICS label.**

---

## 4 · Dispersion (W5) — and here the sector's own move is not small, which is unusual

**RS20 vs SPY spans +6.5 (META) to −6.8 (WBD) = 13.3pp** — **the tightest RS20 range of the four DEEP
sectors** (Energy 32.1pp, IT 58.7pp, Financials 26.2pp). **RS60 spans +13.3 (LYV) to −27.4 (NFLX) =
40.7pp.** Against **XLC +1.28% on the day / −2.83% over five sessions.**

⇒ ★ **On the 20-day window this label is comparatively coherent — the exception among the four DEEP
sectors.** **On the 60-day window it is not**, and the split is **carriers/streaming (deeply negative)
versus live events and interactive entertainment (positive)** — **not** the advertising-vs-everything
split the sector's mcap weight would suggest.
⚠ **Eleven of thirteen names carry a NEGATIVE RS60.** The two exceptions are **LYV +13.3 and
TTWO +9.4**, together **$84bn = under 1% of sector cap.** **The positive 60-day performance of
"Comm Services" as a label does not exist inside its own constituents.**

---

## 5 · Customers and counterparties (W4)

- **② advertising's customers are every other sector's marketing budget** — the sector has no
  concentrated named buyer. **W4 cannot be closed here in the way it can for a supply chain**, and this
  file says so rather than manufacturing a customer list.
- **① carriers' counterparties are handset and equipment vendors and the capital markets.**
  ★ **T marketed debt on 2026-07-27 (FWP)** — with **HY OAS at 2.79% and +11bp off its 365-day low
  over three prints**, a 4.55%-yield issuer's funding cost is the live variable, and it is **S26's
  observable**, not a COMM-specific one.
- ⚠ **The competitive threat named in T's own tape is not another carrier**: *"So Much for SpaceX
  Fears"* [yahoo_finance 07-22], and the blindspot pass returned **SpaceX at 115 token-0 mentions** in
  a 400-row random sample. ★ **SpaceX is unlisted, so this desk has no instrument for the single named
  competitive risk to its top-flow name.** Recorded as a structural gap.

---

## 6 · The divergence ROTATION handed here — verdict

**Question**: COMM carries the board's largest positive delta (+0.173) and its #1 single-name flow, on
a sector never deep-dived. Is the delta real?

**Verdict: the delta is real but its cause is dated and mechanical, not thematic.**
- **T's flow (the sector's #1) is a 3-session post-earnings drift** on a beat-and-buyback print (§2).
- **META's 🟢 is a velocity path** (`vol_surge` 0.65) **into its own print tomorrow**, with its
  **next-quarter revision breadth 10↑ : 22↓ over 30 days** — the near book is being cut.
- **Eleven of thirteen names carry negative RS60** (§4).
⇒ **COMM's promote from N− to N is carried by the flow numbers as ROTATION required, and this file
narrows what the promote means: it is a two-name event with a dated cause, not sector breadth.**
**Nothing here supports going further than N.**

---

## 7 · Track KPIs and anti-signals — stated as observables

| KPI | Now | Test |
|---|---|---|
| **META's capex guide** | pending | ★ **S16 settles 2026-07-29** — does COMM N− reflect a sector or a misapplied single name? **Implied ±8.1% (expiry 07-31, D3) — event-priced for the first time (M89 superseded on 2 of 3 spenders)** |
| **T's forward EPS** | **$2.57 and falling** (next quarter **−3.9%/90d**, breadth 1↑:2↓) | **If forward EPS stops falling, the 9.80× becomes arguable; while it falls, it is not** |
| **T's flow persistence** | **+0.921**, `vol_surge` 1.74 | ★ **Does it survive the print's third week?** The D51 test: a flow reading that post-dates an event by 0–2 sessions is the event. **Re-check 2026-08-06** |
| **GOOGL / GOOG divergence** | GOOGL 🟡 (+0.086) vs **GOOG 🔴 (+0.022, OBV 분산)** | ⚠ **Two share classes of one company carry different tags.** That is an **instrument artifact**, and any COMM breadth count that treats them as two names is double-counting **$4.5tn** |
| **NFLX** | `velocity` **3.18** = the sector's loudest news, on **RS60 −27.4** = the sector's worst | **Story without money — the clean STORY-ONLY case in this sector** |

**Anti-signals**: **a META capex CUT 07-29** (S13 branch C — it breaks the volume and price legs of the
whole AI complex together, per STANDING_VIEW §4) · **T's forward EPS revision breadth turning to
0↑:3↓** · **HY OAS ≥3.10% on a close** (T is a levered, high-yield-adjacent issuer that marketed debt
last week ⇒ **S26 reaches this sector through the balance sheet, not through advertising**).

**Dated catalysts**: **META 2026-07-29 (S16)** ⚠ **provider dispute declared: `yfinance` says 07-30
(D5)** · **T re-check 2026-08-06** · **no other COMM print is inside the 10-day window**, and
`CATALYST_WATCH` carries **only META** for this sector.

---

## 8 · What this file hands forward

1. **T is now covered.** The §3a coverage gap is closed on the analysis side; ⚠ **the ledger will still
   read 0 because T is one of the 28 tickers `module_report_tags` cannot index (D65)** — so **T is
   named in a TABLE ROW with its full name above (M183's restated rule), not in a prose list.**
2. **COMM N stands** — the promote is carried, and its meaning is narrowed to two dated names.
3. **A new dig (D91)**: `margin_history.py` silently truncates a US mega-cap's series at FY2014 and
   presents it as complete.
4. **A structural instrument gap**: the named competitive risk to the sector's top-flow name
   (**SpaceX**) is unlisted and untaggable by this desk.
