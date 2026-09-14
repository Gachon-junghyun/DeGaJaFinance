# SECTOR_DEEP_FIN — Financials, the OW's reason just changed · 2026-07-23 (Stage 6 / L1·DEEP)

> **CONTINUOUS track, 9th pass.** Deep-dived 07-22 (`llm_outputs/2026-07-22/industry_US/SECTOR_DEEP_FIN.md`),
> 07-21 (×2), 07-19, 07-17, 07-15. Baselines carried **BY REFERENCE, not reprinted**: the 6-node value-chain
> map and the JPM/TRV/NDAQ 10-K anchors live in `llm_outputs/2026-07-21/US_2/SECTOR_DEEP_40.md` §2/§4; the
> PYPL M&A resolution and the SCHW pre-print bracket live in `llm_outputs/2026-07-21/industry_US/SECTOR_DEEP_FIN.md`
> §1/§3/§4; the super-regional-steepener / life-insurer / IB-de-rate node map is [07-22 FIN] §1/§5, not
> re-derived here. Flow asof **2026-07-22 close** (`SECTOR_FLOW_US.json`, this run's copy); FINRA short-vol z
> asof 2026-07-22; fundamentals pulled live 2026-07-23 pre-open (US cash session not yet open at run time,
> 09:1x ET — everything flow/short-vol below is the 07-22 close, not today's tape).
> **Every rs20/rs60 below is vs SPY.** OBV / 🟢🟡🔴 are C-grade, corroborant only, never load-bearing alone.
> Zero buy/sell, zero sizing.

---

## §0 · THE DELTA — the OW's reason changed underneath it, twice

1. **The steepener leg that funded [07-22 FIN] §1's super-regional read is now gone.** 2s10s **flattened
   +0.39 → +0.37 (−2bp)** between 07-21 and 07-21→07-22 because the **2y made a 120-day high at 4.26%**
   while the 10y rose only **+3bp to 4.63%** [FRED, asof 07-21]. That is bear-**flattening** (front end
   repricing hawkish faster than the back end) — the mechanical opposite of what the regional-bank leg
   (USB/PNC/FITB/HBAN, [07-22 FIN] §1) needs. The mechanism [07-22 FIN] called "intact" one day ago has
   reversed sign.
2. **eqflow fell (+0.357 → +0.320) while wflow rose (+0.212 → +0.253) — the eqflow-over-wflow gap that
   defines "breadth" narrowed from +0.145 to +0.067, even as green count improved (5→7) and red fell
   (5→3, breadth 0.11→0.15).** Financials is getting *more* cap-weight-confirmed and *less* purely
   equal-weight-driven at the same time — the opposite of a classic "narrow leadership masquerading as
   breadth" pattern, which would show the gap widening. This cuts against the PREMORTEM's concentration
   worry on its own terms, before §1 below even decomposes the names.
3. **The named binding constraint on the insurance leg (P&C/reinsurance pricing softening, [07-22 FIN] §5)
   is unchanged and uncontested today** — no new print. **NFCI lengthened its loosening streak to a 5th
   straight week (−0.552, asof 07-21)** from the 3rd-week reading [07-22 FIN] cited, the single incremental
   fact in the credit column (§5 below).

**Net: the OW's original engine (steepening) inverted; its replacement engine (breadth) is real but
narrower than the headline number, and its two dated brackets (S9, S14) both sharpened this run (§4, §7).**

---

## §1 · Breadth or concentration? — quantified, grouping stated (C5)

**Grouping choice (C5):** GICS sub-industry, rolled into three buckets to match this file's mandate —
**banks** = Diversified Banks + Regional Banks (JPM, BAC, WFC, C, USB, TFC, PNC, HBAN, FITB, n=9, carrying
forward [07-22 FIN]'s own "Banks (9)" leg for continuity); **capital markets** = Investment Banking &
Brokerage (SCHW, MS, HOOD, GS, IBKR, n=5); **payments+insurance** = Transaction & Payment Processing
(PYPL, MA, V, XYZ) + all Insurance sub-industries — P&C, Life & Health, Multi-line, Brokers (n=16, 20
combined). **Alternative choice, stated:** folding Insurance Brokers (AJG/AON/MRSH, fee-only, no float) out
of "insurance" and into a fourth "fee-based" bucket would pull ~3pp of flow out of payments+insurance and
into a smaller, higher-mean bucket — it would sharpen the concentration story, not soften it, so keeping
brokers inside insurance is the conservative choice here. The residual **"other"** = Financial Exchanges &
Data, Asset Mgmt/Custody, Consumer Finance, Multi-Sector Holdings (n=17).

| Bucket | n | mean flow (eqw) | cap-wtd flow | share of Σ positive flow | 🟢 | 🔴 |
|---|---|---|---|---|---|---|
| **Payments+Insurance** | 16 | **+0.470** | **+0.518** | **45.4%** | 4 (TRV, CB, MA, V) | 0 |
| **Banks (9)** | 9 | +0.359 | +0.337 | 22.9% | 2 (USB, JPM) | 1 (C) |
| **Other** (exch/data, asset mgmt, cons. fin., BRK-B) | 17 | +0.250 | +0.060 | 28.1% | 1 (STT) | 1 (BRK-B) |
| **Capital markets** | 5 | +0.005 | +0.060 | 3.5% | 0 | 1 (IBKR) |
| **Sector (check)** | 47 | +0.320 | +0.253 | 100% (Σ pos = 16.997) | 7 | 3 |

**Answer: it is real breadth with a genuine concentration inside it, and the two are different claims.**
Payments+insurance is 34% of the sector's names (16/47) but generates **45%** of gross positive flow and,
cap-weighted, a flow score (+0.518) **more than double** the sector mean (+0.253) — that is concentration
by any definition. But **banks are a second, independent leg that clears the sector average on both
counts** (+0.359 eqw, +0.337 cap-wtd vs sector +0.320/+0.253) — this is not a one-leg sector. What is
genuinely flat, not breadth: **capital markets nets to essentially zero (+0.005 eqw)** — SCHW's bid is
being cancelled name-for-name by GS/MS/IBKR/HOOD's de-rate (§2) — and **"other" is cap-weight-flat
(+0.060)** despite a positive equal-weight mean, meaning its flow is a long tail of small names (STT is the
one large-cap exception) rather than a broad AUM/exchange bid. **Of the 7 🟢 tags, 4 sit in
payments+insurance, 2 in banks, 1 in "other" (STT), 0 in capital markets** — the green count itself is
concentration-consistent even before the flow-score math.

**M25 caveat, stated because it changes the picture:** PYPL (+0.772 flow, rs20 **+31.2 vs SPY**) and MCO
(+0.733) and NDAQ (+0.672) — the 2nd/3rd/6th-highest raw flow scores in the sector — are all 🟡, not 🟢,
purely because `vol_surge` sits at **1.19 / 1.12 / 1.01**, under the 1.2 cutoff. PYPL in particular misses
the 🟢 tag by 0.01 on vol_surge alone while carrying the single highest rs20 in the entire sector. Reading
"7 green" as "the whole positive story" undercounts payments+insurance's true breadth by at least one name
that clears every other bar.

---

## §2 · The three sub-nodes — flow, revisions, verdict

| Node | n | mean flow | rs20 vs SPY | rs60 vs SPY | Verdict |
|---|---|---|---|---|---|
| **Banks** | 9 | +0.359 | +1.7 | +6.8 | Genuine, but its funding mechanism (2s10s) just flattened (§0.1) — see per-name split below |
| **Capital markets** | 5 | +0.005 | −0.9 | +14.1 | Net-zero: an activity-peak de-rate (GS/MS/IBKR/HOOD) offsetting one clean long (SCHW) |
| **Payments+Insurance** | 16 | +0.470 | +6.9 | +6.2 | The concentration leg — priced ahead of estimates in 3 of its biggest names (§1, §7) |

- **Banks.** The steepener-leg split from [07-22 FIN] holds structurally but its fuel just reversed: USB
  (+0.690, rs20 **+5.5**/rs60 **+11.3** vs SPY), PNC (+3.9/+10.2), FITB (+3.6/+11.4), HBAN (+3.1/+6.7) are
  still the best-bid names in the bucket, but they are pricing a curve that **flattened** 07-21→07-22
  (§0.1), not one that is steepening further. JPM (+0.503, +2.3/+8.3) is the sector's only 🟢 money-center;
  BAC (+0.499, +4.5/+13.7) and WFC (+0.214, +0.8/+4.1) trail on both axes. **C is the outlier (§3).**
  FINRA short-vol on JPM: **z +1.89, 🔴 극단, 5v5 +8.0▲** [us_flow.py, asof 07-22] — texture only per D6
  (short-vol sign can invert on market-maker hedging), not a directional call against JPM's clean A-grade
  rs20/rs60 print.
- **Capital markets.** SCHW is the one name in the bucket with **both** axes positive vs SPY (rs20 +6.3,
  rs60 +9.2) and revisions intact — it does not belong in the "activity peak" grouping [07-22 FIN] built
  for GS/MS/IBKR. GS (0y EPS **+18.8% in 30 days on 9↑:0↓** [07-22 FIN] §4, unchanged today) sits at
  flow **−0.057**, rs20 **−1.5**/rs60 **+13.8 vs SPY** — the de-rate is intact. MS (flow +0.024, rs20 −5.2/
  rs60 +11.5) and **IBKR** (flow −0.500 🔴, rs20 −3.2/rs60 +17.3, short-vol **z +2.22, 🔴 극단, 5v5 +1.4▲**
  [us_flow.py]) and **HOOD** (flow −0.022, rs20 −0.7/rs60 +18.7) all now share the identical
  positive-rs60/negative-rs20-vs-SPY shape — the "post-record-quarter mean reversion" cohort is 4 names
  wide, not 3.
- **Payments+Insurance.** TRV (+0.933 🟢, rs20 +15.5/rs60 +18.2 vs SPY) leads on a combined-ratio story,
  not a rate story ([07-22 FIN] §1/§5, unchanged). CB (+0.685 🟢, rs20 +1.5/rs60 +0.6) is priced on a
  **flat** estimate book ([07-22 FIN] §4: 0y EPS +0.1% over 30d). MA (+0.622 🟢, rs20 +7.1/rs60 +0.8) and
  V (+0.603 🟢, rs20 +5.7/rs60 +9.5) anchor payments — their revision divergence is sharpened in §7. PYPL
  (+0.772, discussed §1) remains the M&A special situation per [07-21 FIN] §4, not re-derived.

---

## §3 · Is C really the only broken bank? — confirmed, with one qualifier

**Yes, inside the 9-name bank bucket.** C is the **only** one of the nine with **both** rs20 (**−10.7**)
and rs60 (**−1.4**) negative vs SPY; every other name (USB, JPM, BAC, TFC, PNC, HBAN, FITB, WFC) is
positive on both, or — TFC alone — positive rs20 (+2.3) with only a mild rs60 dip (−2.7). GS, MS, IBKR and
now HOOD (§2) share a **different** shape entirely — positive rs60, negative rs20 — which is the
post-record-quarter mean-reversion signature the STANDING_VIEW says not to conflate with C's outright
double-negative. **Grouping C with GS/MS/IBKR as "the money-centers are being sold" mixes two mechanisms
and this run confirms it again**, unchanged from [07-22 FIN] §1.

**Qualifier, sector-wide:** C is not the sector's only double-negative name — APO (**rs20 −10.7/rs60
−8.9**), PGR (−7.1/−2.9), MSCI (−3.7/−8.4) and BRK-B (−2.6/−0.4) also fail both axes vs SPY, and APO's
rs60 magnitude (−8.9) is actually *worse* than C's (−1.4). None of those four is a bank, so the STANDING
VIEW's claim survives exactly as scoped ("only genuinely broken *bank*"), but "only broken name in
Financials" would be false — worth stating precisely rather than letting "only" drift beyond its scope.
C's own short-vol print, for texture: **z +0.87, 🟡 정상범위, 5v5 +1.9▲** [us_flow.py, asof 07-22] — a mild
short-interest build, not (per D6) a directional confirmation of the price weakness already visible on
rs20/rs60. One counter-narrative on file: *"Bull of the Day: Citigroup (C)"* [nasdaq/yahoo_finance, 07-20]
argued C is "the cheapest [large bank] despite a remarkable rally" — dated **before** the −10.7 rs20 print
below and not confirmed by anything measured since; recorded as sell-side texture, not evidence.

---

## §4 · Rate sensitivity — both sides of S9, named

**Where we sit:** real 10y **2.37%**, a 120-day high, with breakeven **2.28%** [FRED, asof 07-21] — above
S9-A's dovish trigger (real 10y **<2.20%** with breakeven rising) and below the **>2.55%** hawkish
anti-signal, but the last move (§0.1) is a step *toward* the hawkish side, not the dovish one.

**Loses on S9-A (real 10y <2.20%, breakeven rising — the dovish/stagflation branch):**
- **MET, PRU, AFL** (life insurers, spread book) — the direct hit, [07-22 FIN] §2 already established this
  and it is unchanged: rs60 vs SPY **+17.1/+20.1/+1.7**, but flow already decelerating (MET −0.029, AFL
  −0.058 30-day deltas per [07-22 FIN]).
- **TRV, CB** — second-order via float reinvestment; combined ratio (an underwriting variable, §2) still
  dominates the P&L, so this leg is a slower bleed than the life names.
- **STT** — not named as a loser in [07-22 FIN] §2 ("front-end geared, indifferent to the 10y"), but a
  stagflation-cut scenario that drags the real 10y under 2.20% would very likely drag Fed funds (currently
  **3.63%**) down with it eventually, and STT's own coverage frames its NII as **"Macro Conditions ...
  Drive Healthy Operating Leverage"** [seekingalpha, 07-16] — i.e., levered to the *level* being high, not
  merely to the curve. This is an extension of [07-22 FIN]'s frame, not yet tested by data — flagged
  `[unverified]`.

**Loses on the hawkish/higher-for-longer branch, as it is actually being expressed today — not a mirror
image:** the textbook "hawkish is good for banks via a steeper curve" does not hold on today's tape,
because today's hawkish move is a **bear-flattening** (2y +to 4.26% 120-day high, 2s10s narrowing to +0.37,
§0.1). If that pattern persists, it is the **super-regional bank leg (USB, PNC, FITB, HBAN)** — the
cleanest expression of the original steepener thesis — that loses, not the life insurers or STT. **STT and
the life insurers (MET/PRU/AFL) are the names that gain from "higher-for-longer" as a level story**, while
the regionals need the *slope*, not just the *level*, to keep working. These are not the same trade and
today's data has them moving in opposite directions inside one sector.

**Payments (MA/V/PYPL/XYZ) and capital markets (GS/MS/SCHW/IBKR/HOOD) have no clean S9 mechanism** —
consistent with [07-22 FIN] §2's finding that S9-A "hits zero of the five FIN greens cleanly." Volume/deal-
activity variables dominate both, not the real yield.

---

## §5 · Credit reality vs credit narrative

**Reality, unchanged and incrementally stronger:** HY OAS **2.69%** (flat, 6bp off the 365-day low of
2.63, 120-day max 3.46), IG OAS **0.78%** [FRED, asof 07-21]. **NFCI −0.552, now loosening a 5th straight
week** [FRED, asof 07-21/07-17] — up from the 3rd-week reading [07-22 FIN] §3 cited two days ago; the
loosening trend lengthened, it did not reverse. The bank-side credit-cost print wave from [07-22 FIN] §3
(KEY, TFC $395M below NCOs, MTB $120M/23bp, WFC 10bp, USB 0.53%, ALLY −18bp, UCB 9bp, exceptions FSUN/
BayFirst sub-$10B) is carried by reference and has no contradicting print today. **Both honest limits from
[07-22 FIN] still bind: these are Apr–Jun (M27) books and cannot speak to July, and COF's *level* (3.4%
total NCO) remains high even as its direction is benign.**

**Narrative, and where it diverges from the spread market:** feed 07-23 carries a **"Euro-zone banks
tighten credit standards"** thread that is **fading and narrative-only — it cites no spread number**
[per assignment brief]. This is the mirror image of the credit-cost print wave above: real bank data (US)
shows costs falling; a media thread (Europe) asserts tightening with nothing behind it. Meanwhile
**UniCredit raised its own profit targets** [9 art/6 outlets, 07-23] — a genuine European data point running
*against* the tightening narrative in the same news cycle. **P2's kill line is untouched: HY OAS >3.10% on
a close (now 2.69%).** The credit TERM remains the fastest-moving bucket in the news feed at 1.24x the pool
average — velocity of coverage, not velocity of spreads, and the two have now diverged for at least two
runs.

---

## §6 · Track KPIs and anti-signals — dated observables

| Observable | State (dated) | Falsifier / confirmer |
|---|---|---|
| **2s10s direction (NEW, replaces the steepener KPI)** | Flattened **+0.39 → +0.37** (−2bp), 2y at a **120-day high** (4.26%), 10y +3bp (4.63%) [FRED, asof 07-21] | **Confirmer:** 2s10s prints a new 20-day low by **07-29** (FOMC) → regional-bank leg (§2/§4) loses its stated mechanism outright. **Falsifier:** 2s10s re-widens above +0.39 before FOMC |
| **eqflow/wflow gap (NEW)** | Narrowed +0.145 → +0.067 while breadth improved (green 5→7, red 5→3) | **Confirmer:** gap continues to compress toward 0 with green count held ≥7 = genuine broadening. **Falsifier:** gap re-widens while green count falls = concentration reasserting |
| **GS dislocation** | 0y EPS +18.8%/30d, 9↑:0↓ **against** flow −0.057, rs20 −1.5 vs SPY [07-22 FIN] §4, unchanged | **Falsifier:** rs20 crosses 0 vs SPY while revisions hold. **Confirmer:** revisions roll net-down by **07-31** |
| **P&C pricing cycle** | Softening, unchanged since [07-22 FIN] §5 (Arch 07-17, WRB call 07-20, WRB reins. loss ratio 57.7% vs 53.1% est) | **Confirmer:** a second carrier calls pricing competitive by **07-31**. **Falsifier:** CB/TRV Q3 guide underlying CR flat-or-better |
| **Credit costs (P2)** | Provisions/NCOs down across KEY/TFC/MTB/WFC/USB/ALLY/UCB; NFCI now loosening **5 straight weeks** | **Kill:** HY OAS **>3.10%** on a close (now 2.69%) |
| **IBKR/GS/MS/HOOD cohort (widened this run)** | All four now share positive rs60 / negative rs20 vs SPY; IBKR short-vol z **+2.22 🔴 극단** | **Falsifier for the cohort read:** any one of the four crosses rs20 positive vs SPY while the others don't — cohort breaks apart |
| **JPM short-vol build** | z **+1.89 🔴 극단**, 5v5 +8.0▲ against a clean A-grade rs20/rs60 print — texture only (D6) | Watch for a reversal below z +1.0 within 3 sessions (spent-signal test, same as [07-22 FIN]'s GS/STT precedent) |
| Dated catalysts | **V earnings 2026-07-29 (same day as FOMC)**; **MA earnings 2026-07-30**; FOMC 07-28~29, Warsh chairing, no SEP | §7 |

---

## §7 · Sharpened observable for bracket S14 (MA earnings, 07-30)

[07-22 FIN] registered S14 as "MA earnings 2026-07-30" without a specific test. Two facts sharpen it:

1. **V reports 07-29 — the FOMC day itself — and MA reports 07-30, the day after.** The payments leg of
   the concentration bucket (§1) faces its own earnings **inside the same 48 hours as the rate decision**
   that §4 shows is currently moving against, not for, the sector's other rate-sensitive leg.
2. **V and MA diverge on estimate momentum going in, despite an identical 🟢 flow tag.** V's current-quarter
   consensus is **+1.7% over 90 days** (3.18 → 3.23) with FY26 **+2.2%**, while carrying the sector's most
   crowded short (**FINRA short-vol z +2.13**, per the US_LIVE_SHORTLIST). MA's current-quarter consensus
   is **−1.7% over 90 days** (4.85 → 4.77, revision breadth 0↑:1↓ over both 7 and 30 days) while FY26 is
   only **+0.4%** and its short-vol is unremarkable (**z −0.03**) — price (rs20 +7.1 vs SPY) is running
   **ahead of**, not with, its own near-term estimate revision.

**The sharpened observable:** V walks into 07-29 with rising estimates *and* a crowded short — a beat
squeezes a name already priced for one; a miss vindicates the short against improving fundamentals, an
unusual combination worth flagging on its own. MA walks into 07-30 with falling near-term estimates and a
flow-driven (not revision-driven) price — the cleaner test of whether payments+insurance's 45% share of
positive flow (§1) is being paid for growth that has already been trimmed 1.7% in 90 days. **If MA reports
a beat-and-raise that reverses its own 90-day cut, the concentration leg gets independent fundamental
support. If it merely meets and the cut stands, the flow bid in payments was priced ahead of the
denominator — the same pattern §1's M25 note already flags for PYPL/MCO/NDAQ on volume, now on
estimates.**

---

## §8 · Dispersion (W5)

**Financials rs20 spread vs SPY = 42.6pp this run** (PYPL +31.2 to C −10.7) against a **median name move
of +3.6 vs SPY** — roughly **12× the sector's own central move**, wider than [07-22 FIN]'s 7.3× reading
because the tails on both ends moved further apart (PYPL up, C down) while the middle held still. rs60
spread vs SPY is **27.6pp** (IBKR +17.3 to COIN −21.5). Bucket-level cap-weighted flow spans **+0.518
(payments+insurance) to +0.060 (capital markets / other, tied)** — a narrower bucket-level range than
[07-22 FIN]'s sub-leg spread, because this run's grouping (§1, C5) folds five of [07-22 FIN]'s six sub-legs
into three buckets; the name-level dispersion did not narrow, only the aggregation did. **"Financials" is
still the wrong unit for a single number** — the sector mean (+0.320 eqflow) sits inside the payments+
insurance range on one end and describes capital markets (+0.005) not at all.

---

## §9 · What I could not measure

- **Whether the 2s10s flattening (§0.1) is a one-day print or the start of a trend** — one data point
  (07-21→07-22), not a series; flagged `[unverified]` and tracked in §6.
- **Whether STT's NII is more level-geared or slope-geared** — §4's extension beyond [07-22 FIN]'s own
  framing is inference from the company's own language ("macro conditions"), not a decomposed NII bridge;
  `[unverified]`.
- **July (post-Q2) credit costs** — M27/P2 (§5) is Apr–Jun by construction; no Q3 print exists yet for any
  name in the bank bucket.
- **A cap-weighted flow number for the "other" bucket's internal split** (exchanges/data vs asset mgmt vs
  consumer finance) — the 17-name residual was left aggregated because the mandate's three named buckets
  did not require it; a future run should decompose it if "other" ever becomes flow-relevant.
- **Same-day (07-23) price action** — the US cash session was not open at run time; every number above is
  the 07-22 close, restated per file header.

---

**EXIT CHECK:** ✅ Delta led (3 numbered, each with a measured number vs [07-22 FIN]); value chain, player
table and five of six sub-legs carried by reference · ✅ concentration question quantified with the grouping
choice and its alternative stated (C5) · ✅ three sub-nodes each carry flow + rs20/rs60 + a verdict · ✅ C's
"only broken bank" status confirmed inside banks, qualified sector-wide · ✅ S9 answered on both branches,
with the hawkish side shown to hurt regionals via flattening rather than help them · ✅ credit reality vs
narrative separated with a dated example (Euro tightening thread vs UniCredit) · ✅ every rs number carries
**vs SPY**; OBV/short-vol mentions carry an A-grade RS figure alongside (D6) · ✅ S14 sharpened with the
V/MA estimate-momentum divergence and the FOMC-week earnings clustering · ✅ dispersion restated (W5) with
the mechanism for why bucket-level spread narrowed while name-level spread widened · ✅ zero buy/sell, zero
sizing. **→ proceed.**
