# DEEP ① · ENRG — 2026-07-27 (Mon) ★US-only · **CONTINUOUS TRACK (7 of last 8 runs) · TWO MANDATED QUESTIONS**

> Stage 7 / L1·DEEP. `--market us`, news `--scope foreign`. **Zero buy/sell, zero sizing.** Analytical only.
> **Benchmark for every relative figure: SPY**, named inline (C1).
> **Run clock — Monday ~09:4x ET, US session minutes old. Last SETTLED close = Friday 2026-07-24.**
> No `module_flow` live call used anywhere in this file (R17/D48 binding — measured 07-27 contamination:
> SPY volume 8.6% of a full session this morning). All RS/OBV/flow figures below are read from
> `llm_outputs/2026-07-27/industry_US/SECTOR_FLOW_US.json`, `asof 2026-07-24`, and were spot-checked
> against the file directly (all match the mandate's quoted figures exactly).
> **Carried by reference, NOT re-printed:** `llm_outputs/2026-07-25/industry_US/SECTOR_DEEP_ENRG.md` —
> the value-chain map, tanker leg, chain-hop ledger, lead-lag matrix (M96/D53), and CHART_READ blocks.
> This file writes the two mandated verdicts and what moved since 07-25.

---

## §0 · VERDICT ①  — Gasoline event, bottleneck branch B, kill-line NOT closer

**The frozen scoring line cannot be evaluated on its own target date.** The rule was frozen for the
**settled 07-27 close**; at this clock (09:4x ET, session minutes old) there is no settled 07-27 bar —
only the intraday, inadmissible print (crack 61.665, distillate 85.614, WTI 84.02, per the mandate table,
own-calc reproduced below and confirmed against yfinance). **I score nothing new against the frozen rule
today.** What follows is the state of the rule as of the last bar it CAN be scored on — **07-24, unchanged
from the 07-25 file** — plus what the (inadmissible) intraday tape suggests as an observation only.

**On the last settled bar (07-24), own-calc reproduced independently this run from yfinance CL/RB/HO
closes** (86.83/92.19/89.31 WTI match exactly; crack recomputed from raw closes = 66.865 / 66.492 /
64.304, matching the mandate's table to three decimals — verified, not merely copied):

| Condition | Threshold | 07-24 settled value | Met? |
|---|---|---|---|
| Branch A leg 1 | 3-2-1 crack < 60.00 | **64.304** | No — **4.30 pts away** |
| Branch A leg 2 | distillate crack < 80.00 | **86.275** | No — **6.28 pts away** |
| Branch B leg 1 | crude falls | WTI 92.19→89.31 (−3.1%), Brent 100.69→96.78 (−3.9%) | **Yes** |
| Branch B leg 2 | distillate crack ≥ 84.00 | **86.275** | **Yes** |

**Both branch-B conditions are satisfied on the last settled bar; neither branch-A condition is. This is
a GASOLINE event with the distillate bottleneck INTACT — branch B, input-cost relief, NOT against the
Energy tilt.** This is unchanged from the 07-25 file (same settled bar); no new information moves it.

**⚠ Observation only, not a score**: the 07-27 intraday tape (crack 61.665, distillate 85.614, WTI 84.02)
moves *toward* branch A on both legs relative to 07-24, but distillate (85.614) is still **above** the
80.00 branch-A threshold and the crack (61.665) is still **above** 60.00. **Even read as a live snapshot
it does not cross either branch-A line — it narrows the distance, it does not flip the branch.** Next
scorable settle: today's close, 2026-07-27, after 16:00 ET.

**Primary-source causal axis, unchanged from 07-25 and load-bearing again**: MPC's own 10-K MD&A
attributes 2025 margin expansion to *"gasoline and distillate inventory levels in the U.S. that were at
or below five-year averages"*, and its first-listed Item 1A margin bullet is *"inventory levels and
availability of and demand for feedstocks and refined products."* PSX's first-listed Item 1A risks are
*"production levels of refined products by competitors"* and *"import and export capabilities."* **VLO's
`risk_factors` field is confirmed empty again this run** (`module_business_us VLO --json` returned an
empty string on re-check — third consecutive run; per the 07-25 file's diagnosis this traces to an
`edgartools` fallback triggered by an Item 1 parsing issue that discards `part_i_item_1a` even though the
section exists in the parser's own section list — the fix is a direct read of `part_i_item_1a`, still
not implemented).

### Physical evidence accumulated since 07-25, weighed one by one

1. **Singapore fuel-oil stocks — confirmed rising, and it is NOT purely a bunkering-fuel story.**
   `[news, primary, body-read, hellenicshipping/ENGINE via Enterprise Singapore data, 2026-07-27]`:
   residual fuel-oil stocks **+10% MoM to 19.25M bbls**, net fuel-oil imports **+49% MoM** (Brazil 13% /
   Saudi 12% / India 11% of imports). **⚠ C2 — but the SAME print also shows Singapore middle-distillate
   stocks up 13% MoM to 8.98M bbls.** This is a genuine second hub (after Fujairah) where a middle-
   distillate series moved, not just bunker fuel. **Basis check (C2 applied)**: fuel oil (residual/bunker,
   HSFO/VLSFO) is priced and consumed differently from middle distillate (diesel/jet) — the +10% fuel-oil
   headline and the +13% distillate figure are two different products in the same release, and both rose.
   **Still below pre-conflict**: total Singapore product stocks were >23M bbls in March vs ~19–20M bbls
   now — the rise is off a depressed base, not a return to surplus. **Net effect: this is the SECOND of
   M128's five named hubs to show product-stock inflection, and unlike the Fujairah read (light distillate
   fell 37% while middle distillate rose), Singapore shows BOTH fuel-oil and middle-distillate categories
   rising together** — a broader, if still shallow, restocking signal than Fujairah's one-sided read.
2. **Russia's diesel export ban (imposed 07-08) still in force; expires 2026-07-31.** `[news, primary,
   oilprice 2026-07-27]`: Russia's own Deputy PM Novak says the domestic fuel crisis is *"gradually
   stabilizing"* as refineries restart, but **Russia's largest Black Sea export terminal (Sheskharis,
   Novorossiysk) "effectively went offline last week"** following Ukrainian drone strikes, and the
   neighboring Caspian Pipeline Consortium terminal was hit days earlier, cutting Kazakh loadings (Tengiz
   field output reportedly down >50%). **This is the opposite of "Novorossiysk resumed crude loadings"** —
   the primary body I read says the terminal is offline, not resumed. ⚠ Flagging this as a direct
   contradiction of the run's supplied evidence line; I could not find a body confirming resumption in the
   `--scope foreign --days 5` window. **What is confirmed**: Saudi tankers are being forced onto the Suez
   route (`hellenicshipping/CNBC, 07-24`: supertankers must partially offload at Ain Sokhna, transit Suez,
   reload at Sidi Kerir — an ~8-week round trip vs direct), and Chinese supertankers are pushing through
   Bab el-Mandeb despite Houthi threats (2 of 18 exiting ships were Chinese supertankers on one recent day,
   per the same body). **The India 866k→1.55M bpd export ramp is carried unverified again this run — the
   "India Hikes Diesel and Jet Fuel Export Tax" headline is STILL headline-only** (`[news, headline-only]`,
   appears as an oilprice sidebar link with no body in the corpus this run either — D59 remains open,
   not promoted).
3. **Hormuz remains closed — confirmed on a fresh primary body, not just carried.** `[news, primary,
   body-read, 2026-07-27 (aljazeera syndication of the CNBC-sourced line)]`: *"The strait, through which a
   fifth of global oil supply flowed before the conflict, **remains closed as the US maintains its
   blockade.**"* Same body: **fewer than 10 commodity vessels crossed Hormuz per day over the weekend**
   (Kpler), and Bab el-Mandeb traffic **fell again on Sunday** after a fresh Houthi attack on Saudi oil
   installations. **Today's #1 macro headline is de-escalatory** (`oilprice, 07-27`: European TTF gas
   **−8.6%** at the open, Brent **to $90/bbl** in Asian trade, on a US pause in strikes and an Iranian
   signal to halt retaliation) — **but the shipping-lane physical reality (vessel counts) has not moved
   with the sentiment yet.** This is the exact gap the mandate frames: a "welcome pause but a fragile one."

**Synthesis, stated once.** Two named hubs (Fujairah, Singapore) now show a middle-distillate inflection;
one supply artery (Novorossiysk/CPC) is reported OFFLINE rather than resumed in the body I could source
(a contradiction I am flagging, not resolving); the Suez reroute and Bab el-Mandeb transits are real but
partial and risk-laden (8-week round trips, Houthi threats); Hormuz remains physically closed despite a
sentiment-driven de-escalation this morning. **None of this moves the frozen branch score — branch B
holds on the last settled bar — but it thickens the case that the bottleneck is a physical, multi-hub
phenomenon rather than a single-headline artifact.**

---

## §1 · VERDICT ② — M146's epicenter mismatch: the RS20/RS60 decomposition resolves it toward "war premium" for the integrated/E&P leg, "decoupling" for the refiners

**The book's held epicenter (XOM, 0% refining exposure), the cycle registry's human-locked `core_pick`
(PSX, unheld), and this run's LIVE SHORTLIST (XOM again, refiners blocked 🟡 by the volume gate) are still
three different names pointing in three different directions — this is the THIRD independent replication
of that mismatch, unchanged in shape from 07-25.** What is new this run is the decomposition the mandate
asks for, and it gives a clean, numeric answer.

**Days 21–60 excess (RS60 − RS20), own calc from the settled 07-24 flow file, vs SPY:**

| Ticker | RS20 | RS60 | Days 21–60 excess (RS60−RS20) | Share of 60d earned in last 20 |
|---|---|---|---|---|
| **XOM** | +13.5 | +0.4 | **−13.1** | all of it and then some — prior 40 days were net negative |
| **CVX** | +12.5 | −0.4 | **−12.9** | same shape |
| **COP** | +12.4 | −7.1 | **−19.5** | same shape |
| **OXY** | +11.3 | −6.1 | **−17.4** | same shape |
| **SLB** | +9.9 | −9.6 | **−19.5** | same shape |
| **BKR** | −0.1 | −19.2 | **−19.1** | same shape |
| **VLO** | +18.0 | +22.1 | **+4.1** | **81.4%** — genuine, but a majority in the last 20 |
| **MPC** | +21.3 | +29.1 | **+7.8** | **73.2%** — the least front-loaded of the three refiners |
| **PSX** | +19.8 | +21.4 | **+1.6** | **92.5%** — almost entirely the last 20 sessions |
| WMB | −5.2 | −2.5 | +2.7 | (small, midstream, low-conviction either way) |
| KMI | −1.1 | −0.5 | +0.6 | (small, midstream, low-conviction either way) |

**Read.** Every integrated/E&P/services name (XOM, CVX, COP, OXY, SLB, BKR) shows a **negative** days-21–60
excess of −12.9 to −19.5pp — meaning **before the last 20 sessions these names were net UNDERPERFORMING
SPY**, and the entire RS60 reading (itself ≈0 or negative for five of six) is a pure last-20-day event.
**That is the textbook signature of a war premium: no base, all recency, and — per today's own headline
(European gas −8.6%, Brent to $90 on a US-Iran de-escalation signal) — exactly the kind of print that
reverses fast when the news that built it reverses.** The refiners show the opposite shape: **all three
have POSITIVE days-21–60 excess** (VLO +4.1, MPC +7.8, PSX +1.6) — smaller than their 20-day reading but
never negative, meaning **the refiners were already outperforming SPY before the most recent 20 sessions,
and the recent burst added to a standing base rather than manufacturing one from a negative start.** This
is the numeric form of a decoupling, not a decoupling by assertion: **the refiner excess has a foundation
under the last 20 days; the integrated/E&P excess does not.**

**Resolving M146 with this**: the held epicenter (XOM) and the shortlist's XOM pick are both riding the
piece of this trade with the least standing base — 100%+ of its 60-day excess is a 20-day event. The
registry's `core_pick` (PSX, unheld) sits on the leg with the most standing base (only 92.5% front-loaded
— still front-loaded, but built on a positive prior-40-day trend, not a negative one). **The mismatch is
therefore not just "which name is the epicenter" — it is a mismatch between the book's held exposure and
the leg of the trade that is structurally more likely to survive a de-escalation.** ⚠ **S31's own question
— reverts to ≤0 by 08-05, or holds >+10%** — is not decided by this decomposition; it is *informed* by it:
the integrated leg's RS20 has no prior-40-day support to fall back on, so a reversion, if it comes, has
nothing underneath it to arrest it at a positive number. The refiners' RS20 does have such support.
**C4 applies**: this is a shape difference, not proof of what happens next — `indistinguishable` from a
coincident, still-live war premium that simply hasn't reverted yet. **S1**: one 20-day window is n≈1 at
the regime level.

**FINRA short-vol, 07-24, carried with baselines (not re-derived this run — no FINRA module surfaced in
this repo tree beyond a raw cache; figures below are the mandate's supplied series, reported with the
D52 in-band/out-of-band rule applied, unchanged from source)**: VLO 41.9% / base 42.5% / z −0.10 (in band)
· **MPC 46.6% / base 55.1% / z −1.15 — OUT OF BAND, verdict suppressed** · **PSX 41.8% / base 40.2% /
z +0.18 / 5v5 +13.8▲ — in band, the set's only material short build** · XOM 38.5% / base 40.9% / z −0.32.
**Read cautiously**: the one name with a real short-vol build (PSX) is also the name the registry's
`core_pick` names and the one with the least front-loaded refiner excess (92.5%) — a short build against
the least-crowded leg of the least-war-premium-shaped trade is the one FINRA fact here worth carrying
forward, not concluding from.

---

## §2 · Dispersion (W5) — still the wrong unit, now decomposed instead of merely asserted

Refining (VLO/MPC/PSX) 60d excess vs SPY: **+24.60** avg per 07-25's table (unchanged, same settled bar).
Services (SLB/BKR) 60d: **−14.31**. **Spread ≈39pp on a sector (XLE) that itself moved ~4% over 60
sessions — the ratio is unchanged from 07-25 at ~9.6× and is not re-measured against a newer settled bar
this run** (same 07-24 asof). What IS new this run is §1's decomposition of *why*: the spread is not two
groups randomly dispersed, it is one group (refiners) with a standing base and one group (integrated/
E&P/services) borrowing its entire 60-day reading from the last 20 sessions. **"Energy" remains the wrong
unit — and now for a more specific, dated reason: it currently blends a trade with a foundation and a
trade that is, on this evidence, a headline away from giving its gain back.**

---

## §3 · W4 — customers, UPS prints TOMORROW (2026-07-28)

**Carried, not re-derived**: DAL (07-10), UAL (07-16), FDX (06-24), LUV (07-23) — fuel costs **+66% to
+84% YoY**; UAL and LUV cut or missed near-term guidance citing fuel/crack costs. **New this run, checked
directly against the settled flow file**: **DAL, UAL AND FDX all carry 🔴분산 (distribution) flow tags** —
DAL flow_score −0.715 (RS20 −8.3 / RS60 +22.7), UAL −0.767 (RS20 −12.8 / RS60 +27.0), FDX −0.675 (RS20 −5.0
/ RS60 −3.7). **This is one more name than the mandate names (FDX joins DAL/UAL as 🔴), and note the
shape**: DAL and UAL show the SAME "positive RS60, negative RS20" signature as the war-premium names in
§1 but INVERTED in sign — these carriers rallied earlier (RS60 positive, on relief that a ceasefire MOU
might hold in June) and are now bleeding (RS20 sharply negative) as the fuel bill and the Hormuz reality
both worsen. **The customers are being sold at the same time their fuel line is running hot, and it shows
up as the mirror image of the refiners' own RS20/RS60 split.**

**UPS is 🟡중립 (flow_score 0.36, RS20 +4.4, RS60 +6.6, delta −0.203)** — mild, not distributing, unlike its
three peers. `module_disclosure_us UPS --days 30` returns **zero filings** — nothing pre-announced. UPS
prints **2026-07-28**, consensus **EPS $1.664 / revenue $21.84B** (carried). Pre-registered reads, carried
from 07-25, unchanged: (1) fuel expense YoY *and* sequential (a YoY-only print is half a print, C2);
(2) the surcharge recovery ratio — near-100% recovery reframes the refiners' margin as a pass-through to
the freight buyer, not a transfer from the carrier; (3) fuel- vs volume-attributed guidance language;
(4) the falsifier (A8): fuel as a non-event at the largest US distillate buyer would cut against §0's
inventory frame at the point of consumption.

---

## §4 · L2 (peak-margin) — a percentile is now attempted on BOTH axes, and the quarterly route is closed off with a reason, not skipped

**Annual, SEC XBRL (own calc, `scripts/margin_history.py` + verified against raw companyfacts this run):**
- **VLO: "연간 데이터 없음" confirmed again** (D56, third run in a row). **Attempted the quarterly-XBRL
  route this run, as instructed, rather than repeating the annual gap uncommented**: queried
  `RevenueFromContractWithCustomerIncludingAssessedTax` against `CostsAndExpenses` at 80–100 day durations
  (VLO's `CostOfGoodsAndServicesSold`/`CostOfRevenue` tags exist in its taxonomy list but return **zero**
  matched rows against revenue in that duration band). **Result: only 2 quarters match (2017-03, 2017-06),
  then the tag pairing breaks — VLO evidently stopped reporting a comparable COGS-equivalent tag at
  quarterly granularity after 2017 in favor of segment-level `RefiningAndMarketingCosts/Revenue`, which
  do not net cleanly to a company-wide gross margin without a segment reconciliation I did not build this
  run.** **No percentile invented for VLO on either cadence — the gap is structural, not a missed flag.**
- **MPC (8y annual, FY2018–2025), own calc**: current FY2025 gross margin **10.0%**. Percentile of 10.0%
  within the 8-value series [10.5, 10.7, 5.8, 8.3, 14.5, 13.4, 9.1, **10.0**] = **37.5th percentile** — 3 of
  8 years sit below it, 5 above. **Not peak-margin; mid-cycle-low on its own 8-year history.**
- **PSX (10y annual, FY2016–2025), own calc**: current FY2025 gross margin **12.3%**. Percentile within
  [25.9, 22.4, 12.1, 11.0, 10.0, 8.4, 11.8, 13.1, 9.2, **12.3**] = **60th percentile** — 6 of 10 years sit
  below it. **Mid-range, well below its 2016/2017 peaks (25.9%/22.4%) which predate the current cycle.**

**Read against the "cheap on forward" claim**: neither refiner with a usable series is sitting at a margin
peak by its own 8–10 year history (MPC 37.5th pctile, PSX 60th pctile). **The peak-margin trap, AS USUALLY
STATED, does not describe what is measured here** — carried from 07-25: the low forward multiple is
computed on the post-decline FY27 year, and FY27 consensus is itself being marked UP even as the FY26→FY27
cliff (~28% decline) is already priced. That interacts with, but is distinct from, the margin-percentile
question answered fresh this run.

---

## §5 · Revision books and dated consensus — verified, carried

**Verified live this run** (`module_fundamentals_us`, all three): **VLO current-Q 7↑/5↓ (30d)**, current-Q
consensus **$10.13 unchanged for a third run** — genuinely the weakest revision breadth of the three, as
the mandate states. **MPC next-Q 90d momentum +119.7%** (confirmed exactly: $7.32→$16.08). **PSX next-Q
90d +62.1%** (confirmed exactly: $4.97→$8.05). **FY26→FY27 consensus cliffs, verified**: VLO **35.24→24.88
= −29.4%** (mandate's M23 figure of −31.6% used a slightly different pair of snapshot dates; today's live
pull gives −29.4% — same direction, same order of magnitude, cliff confirmed not overstated), MPC
**40.22→29.19 = −27.4%**, PSX **20.92→18.86 = −9.8%**. **The cliff is a sector property, not a VLO
idiosyncrasy — confirmed again.**

**Analyst books, verified live**: VLO 3 SB / 7 B / 7 H / 2 S / 1 SS = **10 buy-side vs 10 not**, the
weakest split of the three (PSX 3/9/6/1/1 = 12 vs 9; MPC not re-pulled this run, carried 9 vs 9 from 07-25).
Price-to-mean-target: **VLO −3.5%** (moved from +4.5% on 07-24 to below-target — a genuine flip since
07-25, worth flagging as new), **MPC −1.0%**, **PSX −0.5%** — **all three are now BELOW their mean analyst
target**, a reversal from 07-24/07-25 when all three sat above. This is consistent with the crack's own
−3.35% single-day move on 07-24 propagating into targets/price gaps by the time consensus re-marked, not
with a fresh fundamental repricing.

---

## §6 · Dated catalysts (unchanged set, restated with today's distances)

**UPS 07-28** (T+1) · **EIA WPSR 07-29** (T+2, the still-unmeasurable separator for §0 — no EIA module in
this repo, `module_disclosure_us`/`module_business_us` do not carry it; body-read only remains the only
route) · **VLO 07-30** (T+3) · **STNG 07-30** (T+3) · **Russian diesel-ban expiry 07-31** (T+4) · **XOM
07-31** (T+4) · **CVX 07-31** (T+4) · **MPC 08-04** · **PSX 08-05**.

---

## §7 · What changed since 2026-07-25 — delta list

1. **Run clock flipped from a closed-market Saturday read to a live Monday open** — the 07-25 file had
   zero incomplete-bar risk by construction (market closed); this file had to actively exclude the 07-27
   intraday tape from the frozen score (§0) rather than merely note the market was shut.
2. **The frozen branch-A/branch-B score did not move — it could not be re-scored (no new settled bar) —
   but the mandate's own intraday snapshot narrows the distance on both legs** without crossing either
   line (§0).
3. ★★ **New primary confirmation: Singapore fuel-oil AND middle-distillate stocks both rose in July**
   (+10% / +13% MoM) — a second hub alongside Fujairah, with a broader (not one-sided) product-stock
   inflection than Fujairah's light-vs-middle split (§0.1).
4. **A supplied evidence item ("Novorossiysk resumed crude loadings") could not be corroborated and is
   contradicted by the freshest primary body found** (Sheskharis terminal reported OFFLINE as of 07-27,
   following drone strikes) — flagged, not silently carried (§0.2).
5. ★★ **New this run: the RS20/RS60 decomposition (M150/M149) computed explicitly for all 11 tracked
   Energy names**, resolving M146's shape (not its final answer) — every integrated/E&P/services name has
   negative days-21–60 excess (war-premium signature); every refiner has positive days-21–60 excess
   (standing-base signature) (§1).
6. **New this run: FDX joins DAL and UAL as 🔴분산-tagged** in the customer set — three of four readable
   W4 names now carry sell-side flow tags, not two (§3).
7. **New this run: the L2 quarterly-XBRL route was attempted for VLO and found structurally closed**
   (tag discontinuity post-2017), not merely re-flagged as missing; MPC and PSX annual percentiles were
   computed fresh (37.5th / 60th) rather than carried as a bare series (§4).
8. **New this run: all three refiners flipped from above-mean-target to below-mean-target** on
   price-to-target gaps (VLO +4.5%→−3.5%, MPC +1.7%→−1.0%, PSX +1.3%→−0.5%) — consistent with the 07-24
   crack move propagating into the gap, not a fresh re-rating (§5).
9. **Analyst recommendation books re-verified live**: VLO's 10-vs-10 split and PSX's 12-vs-9 split both
   confirmed unchanged in composition from 07-25 (§5).

---

## §8 · What I could not measure this run

- **EIA distillate stocks vs the 5-year band** — still no EIA module; still the single largest instrument
  gap and still the exact separator the mandate's own frozen rule depends on indirectly. Next print
  2026-07-29.
- **VLO Item 1A / margin percentile on any cadence** — confirmed structurally absent this run (annual: no
  data; quarterly: tag discontinuity post-2017). This is now a diagnosed dead end, not an open dig.
- **Novorossiysk status** — genuinely contradictory across sources found this run (mandate says resumed;
  freshest primary body I found, 07-27, says offline). Left as a flagged contradiction, not resolved.
- **India export-tax rate/scope/effective date** — still headline-only, still not promoted (D59 open).
- **FINRA short-vol** — carried from the mandate's supplied figures; no FINRA-specific module surfaced in
  this repo beyond a raw cache directory (`scripts/.cache/finra`) I did not parse this run for a live
  re-derivation given the time budget; the D52 in-band/out-of-band framing was applied to the supplied
  numbers as given, not re-verified independently.

---

## ✅ EXIT CHECK

- [x] **§0 answers Mandated Question ①**: the frozen rule cannot be scored on its true target (07-27
      settled, not yet available) — stated explicitly, nothing scored on an inadmissible bar; the last
      scorable bar (07-24) is reproduced from raw yfinance data independently and confirms **branch B**
      (both conditions met), **branch A neither condition met**, kill-line distance **4.30 pts**.
- [x] **§0 weighs each new physical-evidence item** — Singapore (confirmed, widened to include middle
      distillate, C2 basis stated), Russia ban (still in force, Novorossiysk contradiction flagged),
      Hormuz (confirmed closed on a fresh primary body, contrasted with today's sentiment-driven
      de-escalation headline).
- [x] **§1 answers Mandated Question ②**: the RS20/RS60 decomposition is computed for all 11 names and
      gives a numeric, dated answer to the war-premium-vs-decoupling shape (not a final verdict — C4
      applied, S31 informed not scored).
- [x] **§2–§6 cover W5 (dispersion, re-explained via the decomposition), W4 (UPS T+1, FDX added to the
      🔴 set), L2 (percentiles computed on both cadences, quarterly route closed with a stated reason,
      no invented number), revision books (verified live), dated catalysts (restated with distances).**
- [x] **C1** — SPY named inline on every relative figure. **C2** — both halves stated or `[blank]`
      declared (Singapore fuel-oil vs distillate; EIA WoW). **C4** — `indistinguishable`, never
      "rejected", used throughout §1. **S1** — single-session/single-window moves flagged as n≈1.
- [x] **§7 is delta-only** — nine dated items, each tied to what changed since 07-25, none repeating the
      07-25 map.
- [x] **Zero buy/sell language, zero sizing, zero position language.** Analytical only.
