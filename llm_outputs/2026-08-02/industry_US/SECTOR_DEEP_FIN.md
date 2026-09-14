# SECTOR_DEEP_FIN — Financials — industry_US — 2026-08-02 (Sun) · CONTINUOUS-TRACK → **DELTA-LED**

> Continuous slot (6th consecutive run). Leads with the delta; unchanged structure by reference to
> `llm_outputs/2026-07-31/industry_US/SECTOR_DEEP_FIN.md`. Benchmark **SPY** inline on every relative
> number (C1). Flow **asof 2026-07-31 settled** (`SECTOR_FLOW_US.json`); curve read directly off
> **[FRED]** via `MACRO_REPORT.md §A`, not narrative (A6/W4). Analytical only — no sizing, no buy/sell
> (P4).

## 0 · ⛔ THE DELTA — the bank leg that carried the OW last run has ITSELF faded, and the curve stopped confirming the mechanism that greened it

The 07-31 file re-identified the OW's surviving carrier as **money-center bank NIM** (BAC/JPM
🟢가속, RS20 +5.8/+5.6 vs SPY) after R32 killed "breadth-led" as the sector's reason. **This run
re-measures both legs of that call on fresh data and both have weakened, on the same tickers, in the
same direction:**

- **BAC and JPM both faded from 🟢가속 to 🟡중립, and BOTH now carry a NEGATIVE delta** — BAC flow
  +0.467 (was accelerating; delta **−0.229**), JPM flow +0.404 (delta **−0.271**). RS20 vs SPY held up
  (BAC +5.2, JPM +4.9, essentially flat vs the prior read) but the *momentum* that earned the green tag
  is gone. **C (Citigroup) is now the sector's 2nd-worst name outright: 🔴분산 −0.647, delta +0.036
  (still red, marginally less bad).**
- **The specific curve configuration the 07-31 file cited as "the exact configuration that EXPANDS
  NIM" — front end FALLING while the long end rises — did NOT continue on the next settled print.**
  `[FRED, MACRO §A]`: **DGS2 4.22 (07-29) → 4.23 (07-30) = +1bp (rose)**; **DGS10 4.67 → 4.68 = +1bp**.
  The 07-29 print that drove the prior file's read (DGS2 −4bp, DGS10 +6bp) was a genuine front-falls
  configuration; **the 07-30 print is a parallel +1bp shift, which is NIM-neutral, not NIM-positive.**
  Derived 2s10s held at +0.45 only because both legs moved together — **the mechanism's specific
  transmission channel (deposit-cost relief) went quiet on the very next print.**
- **W3's own instruction — test which sub-node the migrated NII leg (markets/financing balances)
  actually reaches — was run this time, and it does not confirm.** `Investment Banking & Brokerage`
  (SCHW·MS·GS·IBKR·HOOD) is the **worst-performing sub-industry in the sector on flow**: mean flow
  **−0.236**, mcap-weighted **−0.160**, 2 of 5 names red (IBKR −0.478, HOOD −0.778). Only **SCHW**
  (+0.500) is positive; GS (−0.331) and MS (−0.092) — the two purest "markets NII" names — are both
  flow-negative this run. **The alternate channel M138 named is not where the money is going either.**

⇒ ★★ **Neither leg of the 07-31 "money-center bank NIM" call survives fresh measurement**: the names
decelerated, the curve's specific NIM-positive shape didn't repeat, and the migrated-NII alternate
node is the sector's worst sub-industry on flow. **§1 re-tests the two candidates the desk has floated
and lands on the insurance node — not because insurance got stronger, but because the bank leg's
support fell away underneath it.** This is the OW's **third distinct stated carrier in three runs**
(breadth → banks → insurance), which is itself flagged as an instability, not smoothed over.

## 1 · The two candidates, re-measured — (a) bank NIM does not confirm this run; (b) insurance re-measures wider, on a mechanism that fits today's specific curve shape better

**(a) The bear steepener → bank NIM.** Curve real (2s10s +0.45, held two settled prints — MACRO P13),
but §0 above shows the **specific front-falls transmission broke on the latest print**, BAC/JPM
decelerated, and the markets/financing alternate node (GS/MS/IBKR) is sector-worst on flow. ⚠
**MACRO's own A-1 this run reframes the move as concentrated at the VERY LONG END**: DGS10 +7bp is
**~100% breakeven** (DFII10 flat at 2.41 three prints), while **DGS30 +12bp and 30y−10y widened to
+0.53 (from +0.48)**. A 30y-led steepening is a **term-premium/duration** event, not a classic
2s10s deposit-funded-NIM event — **the mechanism the OW was built on (P13, framed as NIM) is not the
mechanism the curve is actually showing this run.**

**(b) The insurance node, re-measured from this run's JSON** (Life & Health + Property & Casualty +
Multi-line Insurance, 9 names: MET·PRU·AFL·TRV·ALL·HIG·CB·PGR·AIG):

| | eq-mean flow | vs sector eqflow (+0.1226) | mcap % of sector |
|---|---|---|---|
| **9-name node (incl. AIG)** | **+0.297** | **2.43×** | 7.8% |
| **8-name node (ex-AIG, which is red)** | **+0.355** | **2.89×** | 7.3% |

★ **The prior run cited this node at eq-mean +0.603 = 1.48× the sector.** Today's absolute level is
roughly **half that**, but the **relative premium is WIDER (2.4–2.9× vs 1.48×)** — because the
sector's own eqflow compressed more than the insurance node did. **Both numbers are true and both are
reported**: the node's edge over the sector widened even as its own flow fell.

**RS bases underneath it are the deepest in the entire 47-name sector**, and all four large names carry
매집 (accumulating) OBV: **TRV RS20 +9.1 / RS60 +21.0 · PRU +7.8 / +18.5 · ALL +5.2 / +17.6 ·
MET +6.4 / +17.1** (MET is the sector's #1 flow score, +0.800, and one of only two 🟢 in the whole
47-name universe today — the other is ICE, §2).

⇒ **Mechanistic fit, not just money flow**: the insurance node's driver is **long-duration
reinvestment yield on float** — a direct beneficiary of a 30y-led steepening — which is a **closer
match to today's specifically long-end curve shape** than deposit-funded bank NIM, whose classic
front-end transmission just went quiet (§0). This is **the same distinction the 07-31 file drew**
("reinvestment yield, NOT NIM") — it is reaffirmed here, not reversed, and it is now the better-fitting
of the two candidates **because the curve's own shape moved toward it, not because insurance itself
re-accelerated.**

**Verdict on Q1**: **(b) survives measurement; (a) does not, this run.** The OW's reason is **insurance
/ long-duration reinvestment yield**, carried with the caveat that it is a **7–8%-of-mcap corner of the
sector** — it can explain **eqflow (breadth)**, never **wflow (mega-cap)**, and R32's ban on citing the
aggregate eqflow−wflow gap as "the reason" is unaffected by this node-level finding (SWEEP re-tested
that gap today: all-47 +0.0370, ex-BRK-B +0.0095 — still fragile, still not usable as the sector-wide
argument).

### W4 — MET (primary sources)

`module_fundamentals_us --json MET`: **fwd P/E 8.75× vs trailing 18.6×** — the gap is a GAAP-vs-adjusted-EPS
artifact typical of variable-annuity insurers (derivative/hedge accounting swings GAAP EPS), **not a
clean cheapness read on its own.** ⚠ **`scripts/margin_history.py MET` → "연간 데이터 없음" (no annual
data) — L2 is UNRUNNABLE per the binding rule. No cheapness claim is made on MET.** Estimate momentum:
**+1y EPS 3 up : 0 down (last 30d)** — clean, if thin (n=3); **0y EPS 4 up : 1 down** — also net
positive. `module_disclosure_us MET`: **37 filings/90d, zero M&A or debt-issuance 8-Ks**; the two
market-moving items are routine (Item 2.02 05-06 results, Item 7.01 06-29 Reg FD). **Next earnings
2026-08-06** — same week as TRV's existing recheck date carried from the prior file.

## 2 · The exchanges node — the split reproduces with signs reversed, ICE's `new_green` is earnings-week-coincident, and a replacement observable is proposed for M135's broken RS60 test

Settled 07-31, full 7-name **Financial Exchanges & Data** industry:

| Ticker | Flow | Tag | RS20 | RS60 | Delta | Read |
|---|---|---|---|---|---|---|
| **ICE** | **+0.789** | 🟢 `new_green` | **+14.4** | **−5.0** | +0.145 | venue |
| NDAQ | +0.606 | 🟡 | +11.0 | +2.6 | −0.050 | venue |
| CME | +0.500 | 🟡 | +12.9 | −9.8 | +0.033 | venue |
| COIN | −0.401 | 🟡 | −11.9 | −29.3 | −0.929 | crypto venue, own category |
| SPGI | −0.446 | 🔴분산 | −6.7 | −0.5 | −0.825 | ratings/index |
| MCO | −0.506 | 🔴분산 | −2.8 | +2.0 | −0.580 | ratings/index |
| MSCI | −0.603 | 🔴분산 | −5.4 | −4.7 | −0.816 | ratings/index |

**M137's revenue-engine split (venue vs ratings/index) reproduces cleanly, with the sign INVERTED vs
July** (when SPGI/MCO were the only two positive on both windows): **venue (ICE·NDAQ·CME) eq-mean flow
+0.632 vs ratings/index (SPGI·MCO·MSCI) eq-mean flow −0.518 — a +1.15 spread.** ⚠ **On RS20 the venue
group leads by +18.8pp (12.8 vs −6.1), but on RS60 the two groups are close and both negative (venue
−4.1, ratings/index −2.6)** — **the divergence is entirely a last-20-day event, not a base-level one.**

**M135's registered RS60 test on this node is confirmed broken here too**: ICE RS60 is **−5.0**, which
a naive "CONFIRM if RS60 > prior" test would misread depending on the stale comparison point it was
built against (the file's own field note: it "reports CONFIRM on unchanged prices"). Applying the
desk's own M149/M150 days-21-to-60 method (used elsewhere this run by the PREMORTEM lens) to ICE:
**days 21–60 = RS60 − RS20 = −5.0 − 14.4 = −19.4 ⇒ NO-BASE by the same test PREMORTEM used on
TRI/ETN.** ICE's entire outperformance is a 20-day event stacked on top of a 60-day base that is
*negative* — consistent with the mandate's flag.

**★ Proposed replacement observable** (per §2 mandate, "why it is better"): drop the single-name RS60
test and track **(ICE + NDAQ + CME) eq-weight flow_score MINUS (SPGI + MCO + MSCI) eq-weight
flow_score**, currently **+1.150**. This is better because (i) it is computed on the same `flow_score`
field the desk already treats as A-grade, not a stale-price RS60 join; (ii) it is a **spread**, so it
does not require picking a single ticker's base to trust; (iii) it directly encodes M137's own
venue-vs-content thesis rather than a generic momentum test. **KPI**: the spread, **dated to 08-07**
(EVENT_ALPHA Card 7's existing window on this node) — kill if it inverts back through 0 before then.

**W4 — ICE (primary sources).** `module_fundamentals_us --json ICE`: fwd P/E 17.4× vs trailing 21.5×
(ordinary growth-adjusted relationship — no artifact). ⚠ **`scripts/margin_history.py ICE` also
returns no annual data — the same instrument limitation reproduces outside insurance/banks; no
cheapness claim is made on ICE either.** Estimate revisions are **thin and mixed** (+1y: 1 up : 1 down
in 30d) — **not a revision-driven re-rate.** `module_disclosure_us ICE`: **32 filings/90d, ZERO
M&A-category 8-Ks** — the MarketAxess deal does not appear in ICE's own EDGAR M&A disclosure bucket in
this pull (it may be wrapped inside the 07-30 Item 7.01 Reg FD filing, which is dated the *same day* as
ICE's own earnings). **ICE's `new_green` is therefore earnings-week-coincident (07-30 earnings, 07-30
Reg FD 8-K, `new_green` same window) — the same D51 caution the desk already applies to FTNT elsewhere
this run** ("an earnings-week `new_green` is not yet evidence of a structural re-rate"). **Next
earnings not until 2026-10-29** — no near-term print re-tests it.

## 3 · Sub-sector dispersion (W5) — the spread between industries is 7× the sector's own move

12 industries inside the 47-name Financials sector, sorted by eq-mean flow (mcap %, median RS20/RS60
vs SPY):

| Industry | n | mcap% | mean flow | median RS20 | median RS60 | 🟢/🔴 |
|---|---|---|---|---|---|---|
| **Life & Health Insurance** | 3 | 2.0 | **+0.618** | +6.4 | +17.1 | 1🟢/0🔴 |
| Asset Mgmt & Custody Banks | 7 | 8.8 | +0.430 | +7.6 | +0.9 | 0/0 |
| Transaction & Payment Processing | 4 | 15.0 | +0.238 | +4.3 | +11.4 | 0/0 |
| Property & Casualty Insurance | 5 | 5.3 | +0.196 | +2.6 | +5.5 | 0/0 |
| Diversified Banks | 7 | 26.5 | +0.132 | +1.4 | +9.5 | 0/1 |
| Financial Exchanges & Data | 7 | 6.6 | −0.009 | −2.8 | −4.7 | 1/3 |
| Insurance Brokers | 3 | 2.7 | −0.052 | +0.6 | +11.4 | 0/0 |
| Regional Banks | 2 | 1.1 | −0.059 | −3.2 | +4.8 | 0/0 |
| Consumer Finance | 2 | 4.7 | −0.085 | −1.6 | +5.1 | 0/0 |
| Multi-Sector Holdings (BRK-B) | 1 | 13.9 | −0.116 | +0.4 | +6.7 | 0/0 |
| Multi-line Insurance (AIG) | 1 | 0.5 | −0.160 | −1.3 | −3.1 | 0/0 |
| **Investment Banking & Brokerage** | 5 | 12.9 | **−0.236** | −1.9 | +8.0 | 0/2 |

**Spread: +0.618 to −0.236 = 0.854 between the best and worst sub-node — roughly 7× the sector's own
eqflow (+0.1226) and 2.8× the entire wflow-eqflow gap R32 already ruled unusable.** ⇒ **the sector
label is the wrong unit, plainly.** The sector-level delta (−0.300) and the sector-level "OW−" verdict
describe an average of a node running +0.62 (insurance) and a node running −0.24 (brokerage/markets),
with the largest single name (BRK-B, 13.9% of mcap) sitting in neither and dragging wflow down on its
own (−0.116). **Any single "Financials is OW because X" sentence is describing at most one of twelve
sub-nodes.**

## 4 · Live brackets — what each needs, checked against today's data

- **S23** (2s10s ≤ +0.20 by 08-05): **currently +0.45, receding-then-flat (§0)** — 25bp away with 2
  sessions left in-window; needs a sharp reversal to fire. If it fires, it falsifies P13 outright and
  removes the OW's original stated mechanism (already weakened per §0/§1).
- **S26** (HY ≥ 3.10%, →08-12): **2.84%, 26bp away** — the FOMC spike fully retraced twice; no
  Financials-specific credit stress visible in this sector's own flow (no bank/insurer carries a
  distressed OBV read).
- **S41** (IG ≥ 0.90%, →08-12): **0.80%, 10bp away** — the closer of the two credit lines. Per M147's
  shared beta, this sector (JPM β 0.932) is first-hit if it fires; watch GS/MS/IBKR (already the
  sector's weakest flow node, §0) as the earliest tell.
- **S51** (NFP 08-07, bear flattener risk): a hot print reprices cuts out, front end sells harder than
  the long end ⇒ **bear FLATTENER** ⇒ compresses 2s10s toward S23's line **and** removes even the
  residual front-end relief §0 measured going quiet — the print that would hurt this sector's
  strongest remaining candidate (insurance, which needs the long end to keep leading, not the front end
  to catch up).
- **S14** (MA/V/PYPL cross-border + RS20, scores 08-06): current inputs — **PYPL RS20 +25.5** (clears
  by a wide margin), **MA +5.9**, **V +0.8** (flat, the weak leg). ⚠ This file does not have S14's
  frozen threshold text on disk to quote verbatim; reported as the raw RS20 dispersion so the 08-06
  check has a same-run baseline. **V is the name that would need to move for a "payments broadly
  strong" read; PYPL alone already carries the group.**

## 5 · PREMORTEM re-tags addressed

- **NDAQ EXHAUSTED** (rs60 +2.6, days 21-60 **−8.4**): confirmed on this run's JSON (rs20 +11.0, rs60
  +2.6 ⇒ 21-60 window = +2.6−11.0 = −8.4). NDAQ sits in the "venue" half of §2's split (flow +0.606,
  still positive) but **its apparent base is a 20-day event too**, same shape as ICE. Flip condition
  per PREMORTEM: rs60 < 0 by 08-07 — **same date as this file's proposed venue-minus-ratings KPI
  (§2)**, so both checks land together.
- **ICE NO-BASE** (rs60 −5.0): reproduced independently in §2 via the same days-21-to-60 method
  (**−19.4**), and tied to the earnings-week-coincidence finding from W4 — **two independent checks
  (momentum-shape and disclosure-timing) point the same direction: ICE's green is fresh and unbased,
  not yet a structural re-rate.** Flip condition: rs60 > 0 on a settled close, or the venue-minus-ratings
  spread (§2) holding through 08-07 without decaying.

## 6 · Verdict

**The OW's stated mechanism has round-tripped for a third time in three runs.** This run's fresh
measurement finds: **(i) the money-center bank NIM leg the 07-31 file greened has itself faded — BAC/JPM
both slipped to 🟡 with negative deltas, and the front-end curve relief that justified the "NIM
expansion" framing did not repeat on the next settled print; (ii) the markets/financing alternate
channel W3 named is the sector's worst-flow sub-industry; (iii) the insurance node re-measures at a
WIDER relative premium to the sector (2.4–2.9× vs the previously cited 1.48×) even as its absolute
level roughly halved, carries the deepest RS60 bases in the 47-name sector, and its long-duration
reinvestment mechanism is the better fit for a curve move MACRO's own A-1 now measures as concentrated
at the 30y, not the front end.** **The OW survives on insurance, not banks, this run** — the same
"direction stands, carrier retracted" shape as R32, now one node deeper. ⚠ **The instability itself is
the finding worth carrying forward**: three different stated reasons in three runs (breadth → banks →
insurance) is not a sign of a robust thesis, and the next run should treat any single-carrier claim as
provisional until it survives two consecutive reads. **Separately, the exchanges node (§2) is not a
sector-wide reading — it is a venue-vs-ratings split, real but 20-day-only on ICE, with a replacement
observable proposed to retire the broken RS60 test.** **Kill lines**: 2s10s ≤ +0.20 (S23, 08-05), IG ≥
0.90% (S41, 08-12, 10bp away), or the venue-minus-ratings spread (§2) inverting before 08-07.

## ✅ Coverage

flow ✅ (47/47 names pulled live from `SECTOR_FLOW_US.json`, 12 sub-industries grouped) · players/IR ✅
(insurance node re-measured 9-name and 8-name ex-AIG; exchanges node 7-name venue/ratings/crypto split)
· curve **checked against [FRED] via MACRO §A, not narrative** ✅ (A6/W4; front-end reversal on 07-30
identified directly from the printed table) · value chain ✅ (`curve shape → deposit cost / reinvestment
yield → which node captures it`) · W4 primary sources ✅ (MET: fundamentals + disclosure + margin_history;
ICE: fundamentals + disclosure + margin_history) · B2/L2 cheap-check: **NOT MADE on MET or ICE —
`margin_history.py` returned no annual data for both; the binding rule's L2-unrunnable clause is
invoked explicitly rather than skipped silently** · dispersion ✅ (W5: 0.854 spread across 12
industries = ~7× the sector's own eqflow, §3) · live brackets ✅ (S14/S23/S26/S41/S51, §4) ·
PREMORTEM re-tags ✅ (NDAQ EXHAUSTED confirmed, ICE NO-BASE reproduced independently, §5) · lead/lag ✅
(no inherited lead/lag claim used without re-dating). **Failed lookups**: `module_business_us --full
--json MET` timed out at 120s and was not retried (fundamentals + disclosure covered the same W4
requirement without it); S14's frozen threshold text not located on disk, reported as raw RS20 inputs
instead of a scored check.
