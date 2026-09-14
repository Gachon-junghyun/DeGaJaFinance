# SECTOR_DEEP_HLTH — Health Care · industry_US · 2026-08-30 (Stage 8 / L1·DEEP)

> **CONTINUOUS TRACK.** Structural map (6-node value chain, sub-industry universe) unchanged from
> `llm_outputs/2026-08-29/industry_US/SECTOR_DEEP_HLTH.md` — **carried by reference, not reprinted.**
> This file leads with the delta. P4 — analytical only, no sizing, no buy/sell.
> ⚠ **Basis**: 08-28 daily Close was void; repaired via 5-min-bar proxy, **0.0225% mean / 0.038% max
> error vs KIS (n=9)**. Stated once, not re-litigated.

## §0 · Mandate, answered in one line

> *"`eqflow` +0.135 = rank 2, best breadth on the board. `XLV` `exc5` −2.46pp = worst of 11.
> Resolve. Also: `MRK` trades above mean target, fires `L2`."*

**Answer: a cap-weight artifact, not a breadth-vs-momentum paradox — measured, not asserted.**
Splitting the 32 names **upstream** (discovery/tools/device/pharma, 23 names, **80.9% of cap**) vs
**downstream** (distribution/payer/services/facilities, 9 names, **19.1% of cap**): cap-weighted
upstream flow **+0.129**, downstream **−0.439**. `eqflow` counts 23 accumulating names against 9 —
breadth reads strong. `wflow` (+0.021, `XLV`'s flow proxy) is dragged because **three of the four
largest names by cap — `LLY` ($980B, −0.288), `ABBV` ($382B, −0.327), `UNH` ($364B, −0.765) — are all
negative.** `XLV`'s bad 5-day tape is real, not one flipper's artifact: the mega-caps are genuinely
underperforming while the broad tape accumulates. Both numbers are true, each measuring a different
object. `S133` (constituents-vs-ETF, settles 09-14) is the correctly framed bracket — see §9.

## §1 · Delta since 08-29 (`asof` moved 08-27 → 08-28)

| | 08-29 file | today | delta |
|---|---|---|---|
| `eqflow` | +0.102 (highest of 11) | **+0.135, rank 2** | 🔴 up but **no longer #1** — check next run whether breadth is still the board's story |
| `top1_flips_sign` (`LLY`) | **TRUE** (`wflow` −0.027 vs ex-top1 +0.053, opposite signs) | **FALSE** (`wflow` +0.021 vs ex-top1 +0.095, **same sign**) | 🔴 **CHANGED, verified**: `LLY`'s drag weakened enough that the sector no longer needs `LLY` excluded to read positive — `M1071` |
| sector's sole 🟢가속 | `MRK` (flagged 🟢 in the mandate framing) | **`A` (Agilent)**, flow +0.906, `rs20` +8.1/`rs60` +9.9, OBV 매집 | 🆕 leadership rotated *within* the tools/instruments node, not out of it |
| `MRK` | +0.761, `rs60` +27.8 (in `S133` basket) | +0.678, `rs60` **27.3** (still in basket) | flow softened slightly, still 매집 |
| reds | none singled out | **`UNH` −0.765, `CVS` −0.828 — both Managed Care/Health Care Services, both the ONLY reds** | 🆕 clean downstream cluster, see §2 |
| distributors | `MCK` 분산 (binding-constraint node) | `MCK` still **분산** (−0.342), `COR`/`CAH` still 중립 | unchanged in direction, `MCK` now more negative |
| ABT (chain-hop candidate, 08-29) | `rs20` +1.7 vs `rs60` +26.8 (lag) | `rs20` **+3.4** vs `rs60` +27.2 | catch-up **in progress**, thesis still live |

## §2 · Flow — the real split is value-chain position, not GICS-industry count

By GICS sub-industry, equal-weight (n=32, all names — not just top-16 like 08-29's cut):

| industry | n | flow mean | `rs20` mean | `rs60` mean |
|---|---|---|---|---|
| Life Sciences Tools | 4 | **+0.530** | +7.0 | +16.4 |
| Biotechnology | 6 | +0.325 | +6.8 | +13.7 |
| Pharmaceuticals | 5 | +0.237 | +3.9 | +16.0 |
| HC Equipment | 8 | +0.141 | +1.9 | +8.3 |
| **HC Distributors** | 3 | **−0.214** | +0.2 | +18.9 |
| Managed Health Care | 3 | −0.104 | −1.1 | +5.6 |
| HC Facilities | 1 | −0.176 | +0.8 | +13.0 |
| **HC Services** | 2 | **−0.466** | **−8.4** | +0.5 |

★★ `M1072` `[measured]` **Every industry mean below zero sits on the payer/distribution/services
side of the chain; every one above zero sits on the discovery-to-device side.** Grouped: upstream
23 names, eqflow +0.277, `rs20` +4.5; downstream 9 names, eqflow **−0.229**, `rs20` **−2.1** — a
0.51 spread, **wider than the sector's own headline `eqflow` (+0.135)** ⇒ per rule 1, the sector
label is the coarser unit; value-chain position is the finer one that actually separates winners
from losers. This corrects 08-29's B5 read (narrow dispersion inside the top-16 only) — the full
32-name cut shows that read was an artifact of pre-filtering to `rs60` leaders, which excludes
`UNH`/`CVS` by construction.

🚨 Cap-weighted confirmation (`M1073` `[measured]`, ties to §0): downstream cap-weighted flow
**−0.439**, upstream **+0.129** — the downstream cluster is *worse* cap-weighted than equal-weighted,
because `UNH` ($364B) sits inside it at the sector's single worst score.

## §3 · Players — unchanged roster (see 08-29 §4 for full 6-node map); what moved

`A` (Agilent, Life Sciences Tools, $35.9B) is new to the sector's 🟢 slot — same node as `TMO`/`DHR`
(both still 매집, `rs60` +29.2/+19.3). The tools/instruments node, not any single name, is the
sector's most persistent accumulator across two runs. `MRK` ($281B, Pharma) is the carried standing
name and the subject of `L2` — see §7.

## §4 · IR anchor — two primary filings read, Item 1A/MD&A used for anti-signal

**`UNH` 10-K** (filed 2026-03-02, period 2025-12-31, EDGAR accession 0000731766-26-000062), MD&A
"Regulatory Trends and Uncertainties": *"Medicare Advantage rate notices for numerous years have
resulted in industry base rates well below the industry forward medical cost trend... the Advanced
Notice for 2027 is far below [trend]... substantial revisions to the risk adjustment model...have
resulted and will continue to result in reduced funding."* Also: *"commercial business is further
subject to CMS audits related to medical loss ratios (MLRs) and risk adjustment data."*
🚨 **Anti-signal, direct from the filing**: this is a company **describing its own regulated-rate
mechanism as a multi-year headwind**, not a floor — see §9.

**`CVS` 10-K** (business/MD&A extract): Aetna segment's "Medical Benefit Ratio" is explicitly a
**mandated ratio** — "health care costs divided by premium revenues" — used by CMS to cap the share
of premium a payer may retain. Segment text also documents CVS Caremark's PBM function (formulary
management, rebate negotiation via GPO) as the node between manufacturer and payer.

## §5 · Chain-hop — re-run, `"GLP-1" biotech "drug pricing"` (7d, foreign, ±300-char proximity)

| candidate | proximity/body | flow cross-check | verdict |
|---|---|---|---|
| `VRTX` | 6/6 | 매집, `rs60` +24.5 | 🚫 already in `S133` basket |
| `ABT` | 5/11 | 매집, `rs60` +27.2, **`rs20` +3.4** (up from +1.7 on 08-29) | ✅ **still the live candidate** — catching up, not yet caught |
| `COR` | 3/7 | 중립, `rs60` +20.1, `rs20` +0.4 | ⚠ Example body: *"McKesson Raises FY27 Guidance as Oncology and GLP-1 Growth Accelerate"* (24-Aug, but headlines `MCK`, not `COR` — a co-mention mismatch, not a `COR` signal). 🚫 **Rejected as a `COR` candidate**; recorded as a `MCK` fundamental data point instead — see §6 |
| `WMB` `KO` `SPGI` `CCEP` `WFC` `BLK` | 2–7 | — | 🚫 **Same six noise names as 08-29, recurring verbatim** (`WMB`'s example is again the unrelated *"Photronics...AI Boom"* piece). **The stability of this noise list across two runs is itself a finding — the tool's rejection criteria are working, not under-filtering** |

## §6 · Fundamentals meet flow — the distribution node is diverging, not deteriorating

`MCK` (McKesson) **raised FY27 guidance on 24-Aug citing oncology and GLP-1 volume growth** —
confirmed via `module_news_data fts` (nasdaq, 08-24). Yet `MCK`'s flow score is **−0.342** — the sector's most negative distributor — on **three axes, not
one** (RULE D6 satisfied by the orchestrator, not exempted): **OBV −0.136 분산 · `rs20` +1.4 vs `SPY`
(flat) · `vol_surge` 0.79 (below normal)**, against a **`rs60` of +18.9 vs `SPY`**. ⚠ **OBV is a C-grade
signal and may not carry a proposition alone** (r≈0.49 to real flow, no lead, t=1.00); the claim here
rests on the conjunction — a 60-day winner whose 20-day relative strength has gone flat on
below-normal volume while OBV distributes. 🚨 `M1074` `[measured]`: **guidance up, flow down** — this
is not a demand problem at node 5, it is a **de-rating**, consistent with the policy-risk framing in
§4/§9 (PBM transparency legislation, FTC settlement) rather than a volume miss. Sharpens 08-29's
binding-constraint call: distribution's constraint is priced risk, not weak throughput.

## §7 · `L2` peak-margin lens, applied to `MRK` — and a discrepancy flagged

Fresh pull (`module_fundamentals_us MRK --json`, live): **price $148.35, target_mean $148.73 ⇒
upside +0.26%**, essentially at-target — **does not reproduce the mandate's stated −4.4%**;
`[measured]`, flagged not silently reconciled, likely a snapshot-timing gap vs ROTATION's pull. Both
readings agree qualitatively: **`MRK` has little to no headroom to its own target — that's what
fires `L2`.** Forward PE 15.5x looks cheap next to trailing PE 118.7x (trailing EPS depressed by a
one-time item) — but **PEG is 10.26**: the "cheap" forward multiple is a low-growth-denominator
artifact, not a margin re-rating case. ⚠ **Revision trend disagrees by window** (rule 6): 0Q EPS
estimate down $2.307→$2.210 (90d→now); **+1Y EPS down** $9.567→$9.543 (60d→now) after **rising**
$9.534→$9.657 through 90d→30d — two non-overlapping windows, opposite signs. No margin percentile
available this run (`C3`, unknown, not assumed).

## §8 · Contract terms named (rule 7) — no mean-reversion claim made without them

- **Medicare Advantage**: CMS Final Notice 2026 ≈ trend; **Advance Notice 2027 "far below" trend**
  (`UNH` 10-K, §4). Structural, not cyclical — a rate-setting mechanism running below cost, the
  opposite of margin support.
- **MLR/MBR floors**: minimum medical-loss-ratio thresholds **cap** insurer margin retention by
  regulation (`CVS` Aetna MBR 87.4%, per-print). This is a ceiling, not a floor.
- **PBM**: CVS Caremark **settled an FTC antitrust matter in July 2026**; **PBM pricing transparency
  legislation is pending** (source: yahoo_finance/nasdaq/fool syndication, 29–30 Aug — see §10 for the
  dating caveat). Contract terms not fully disclosed in the public filings pulled this run — flagged
  `unknown` beyond what's quoted above, not assumed.
- **IRA price-negotiation list / LOE**: not pulled this run — `unknown` (`C3`).

## §9 · Frame-transfer test (rule 8) — regulated-return, applied to managed care, and it fails

The desk trusts **regulated-return** framing elsewhere (utilities: rate base × allowed ROE = a
*floor*). Tested here explicitly: **does not transfer.** Medicare Advantage rate-setting and MLR/MBR
floors are regulatory mechanisms, but they run in the **opposite direction** from a utility's
allowed-return floor — CMS rates have been **below** cost trend for "numerous years" per `UNH`'s own
filing, and MLR/MBR floors **cap** what an insurer keeps rather than guaranteeing what it earns.
**Checked, does not apply — pass.** This is the mechanical reason node 5/6 (distribution, managed
care) sit on the negative side of §2's split while the un-regulated upstream (discovery, tools,
device) sits positive: **regulation here is a margin ceiling with a cost-trend headwind, not a
margin floor.**

## §10 · Customers and disclosed spend (rule 9)

**Payers/PBM/CMS named.** Disclosed: `UNH`'s own MD&A on CMS rate trend (§4, dated period
2025-12-31, filed 2026-03-02); `CVS`/Aetna MBR 87.4% (dated print, company-disclosed). **Hospital
system spend**: `unknown` this run (`C3`) — no hospital capex series pulled. **Government (CMS)
spend**: the Advance/Final Notice cadence is the closest observable and is dated annually, not
inside this window.

## §11 · Instrument note — the "dark ingest" premise did not hold, measured

🚨 `M1075` `[measured]` **The brief states the foreign news ingest has been dark since 08-28. A live
`module_news_data fts`/`search` query this run returned dated 08-29 and 08-30 body-bearing foreign
articles** (e.g. *"Wall Street Isn't Giving Up on CVS Health"* — yahoo_finance/nasdaq/fool, dated
Sat 29-Aug and Sun 30-Aug, 4341–6543 char bodies) — **contradicting the stated cutoff.** Used the
content anyway because it is dated, sourced, and internally consistent (matches `CVS`'s FTC/PBM
facts independently corroborated in the 10-K extract, §4) — but **flagging the contradiction rather
than silently trusting either claim**: either the ingest resumed and the brief's premise is stale, or
these three articles' dates are mislabeled. Not resolved this run.

## §12 · `S133` running state — checked, not re-frozen, explicitly NOT a score

Registered 08-29 at `asof` 08-28: window 08-28 → 09-14. **No new settled session exists yet** (asof
is still the 08-28 repaired bar; the next trading close has not settled in this data pull) ⇒ **no
running-state delta to report — state unchanged from registration.** `EW{REGN,AMGN,TMO,BDX,MRK,VRTX}`
membership unchanged; all six still `OBV 매집`, `rs20` still positive on every member per the current
sweep (`REGN` +1.1/+26.3, `AMGN` +9.3/+25.8, `TMO` +5.3/+29.2, `BDX` +11.5/+28.2, `MRK` +10.9/+27.3,
`VRTX` +10.6/+24.5).

## §13 · Track KPIs and anti-signals — updated

| # | KPI / anti-signal | today's read | kills what |
|---|---|---|---|
| 1 | `S133` | unchanged from registration (§12) | the `OW` promotion |
| 2 | breadth persistence | 23/32 (72%) upstream names positive-flow, unchanged in shape from 08-29's 11/16 | §0/§2's split |
| 3 | distribution node | `MCK` 분산 deepened (−0.342 vs prior), **guidance/flow divergence confirmed** (§6) | thesis that node 5 is a demand problem — it isn't |
| 4 | `L2`, `MRK` | applied; live upside ≈ flat (+0.26%), mandate's −4.4% not reproduced this run — flagged, not silently reconciled | any `MRK` cheapness claim |
| 5 | payer cluster | `UNH`/`CVS` both 🔴, both regulated-ceiling names (§9) — watch for a 3rd Managed Care/Services name joining red | §2's clean split holding |
| 6 | VOID | FDA/trial readout named-date at ≥2 of `S133`'s six, inside window | `S133` scoreability — none observed yet this run |

## ✅ EXIT CHECK
- [x] Mandate answered §0, cap-weight-vs-equal-weight mechanism measured, not asserted.
- [x] Delta-led (§1); unchanged structural map referenced, not reprinted.
- [x] Dispersion tested full-universe (§2) — **exceeds sector move ⇒ sector label flagged as coarse unit**, value-chain position is the right one (upstream/downstream split).
- [x] 2 primary filings read (`UNH`, `CVS`), Item 1A/MD&A anti-signal used (§4).
- [x] Chain-hop re-run, body-proximate, cross-checked, noise stability itself flagged (§5).
- [x] Cheap-multiple claim carries margin/PEG context + non-overlapping-window revision disagreement (§7).
- [x] Contract terms named for any mean-reversion-adjacent claim, or marked `unknown`/`C3` (§8).
- [x] Frame-transfer question asked and answered: regulated-return does not transfer to managed care (§9).
- [x] Customers named, spend dated where available, `unknown` stated where not (§10).
- [x] `L2` applied explicitly to `MRK`, including a flagged non-reproduction of the mandate's figure (§7).
- [x] `S133` checked, not re-frozen, explicitly labelled not-a-score (§12).
- [x] Instrument-note discipline continued: this run's own contradiction (dark-ingest premise vs live query) written down (§11), not suppressed.
