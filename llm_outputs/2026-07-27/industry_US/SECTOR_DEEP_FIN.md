# SECTOR_DEEP_FIN — Financials · 2026-07-27 (Stage 6 / L1·DEEP ②, continuous track run 5)

> **Run clock**: Mon 2026-07-27, ~09:4x ET. US session minutes old. All RS/OBV/flow numbers in this
> file come from `llm_outputs/2026-07-27/industry_US/SECTOR_FLOW_US.json` (**asof 2026-07-24,
> settled**) — `module_flow` was **not** called for RS (today's bar is a partial print; measured
> elsewhere at 8.6% of a session's volume). Fundamentals/revisions were called live where noted.
> **Benchmark: SPY on every relative number (C1).** OBV tags are **C-grade, corroborant only (D6)**.
> Continuous-track — the 47-name map and prior sub-node tables are carried by reference to
> [2026-07-25 SECTOR_DEEP_FIN](../../2026-07-25/industry_US/SECTOR_DEEP_FIN.md) and not reprinted.
> Analytical only — no sizing, no buy/sell language (P4).

---

## §0 · The three mandated verdicts, with numbers

### ① Is Financials' eqflow > wflow genuine breadth, or concentration? — **Mostly concentration, in two separate layers, one mechanical and one real-but-narrow.**

Current state (asof 07-24): **wflow +0.278, eqflow +0.342**, gap **+0.064**, 5 🟢 / 3 🔴 of 47, breadth 0.11.
I pulled all 47 Financials rows directly from the JSON (not the carried grouping) and rebuilt both
the cap weights and the flow means myself; the wflow figure I recompute from raw mcap × flow_score
reproduces the file's own wflow to the third decimal (0.2781 vs 0.278), so the underlying arithmetic
is verified before drawing conclusions.

**Layer 1 — mechanical, and it is most of the gap.** `BRK-B` (Multi-Sector Holdings) is the single
largest market cap in the entire Financials set — **$1,055.7B, 13.94% of the sector's total cap**,
larger than JPM ($871B). Its flow score is **+0.012**, effectively flat. Equal-weighted it would
carry a 2.1% vote; cap-weighted it carries 13.9%. Dropping it alone:

| | wflow | eqflow | gap |
|---|---|---|---|
| Full sector (n=47) | +0.278 | +0.342 | +0.064 |
| Ex-BRK-B (n=46) | **+0.321** | +0.349 | **+0.028** |

Removing one name cuts the eqflow-wflow gap by **56%** (0.064 → 0.028). Most of what looks like
"cap-weighted money is behind, equal-weighted breadth is ahead" is one enormous, flow-flat holding
company diluting the cap-weighted number — not funds rotating away from big Financials names in
general.

**Layer 2 — real, but narrow, not sector-wide.** After removing the BRK-B artifact, a genuine
residual concentration remains. Re-running the carried M40 partition (**banks n=9**: JPM BAC USB PNC
TFC WFC C HBAN FITB · **capital markets n=5**: SCHW HOOD GS MS IBKR · **payments+insurance n=16**: MA
PYPL V XYZ, AON AJG MRSH, MET PRU AFL, AIG, CB TRV HIG ALL PGR · **other n=17**: the remaining
asset-management, exchange, consumer-finance and BRK-B names) on today's file:

| group | n | eqflow mean | wflow mean | gross positive flow | 🟢 | 🔴 |
|---|---|---|---|---|---|---|
| banks | 9 | +0.183 | +0.296 | 2.394 | 1 | 1 |
| capital markets | 5 | **+0.009** | +0.019 | 0.650 | 0 | 1 |
| payments+insurance | 16 | **+0.529** | +0.554 | 8.465 | 4 | 0 |
| other | 17 | +0.348 | +0.155 | 6.581 | 0 | 1 |

Payments+insurance is **34.0% of names (16/47)** but **46.8% of gross positive flow (8.465/18.090)**,
at **1.55× the sector's own eqflow mean** (+0.529 vs +0.342). That ratio is down from the carried
M40 read of ~2× (+0.518 vs +0.253 on 07-22) — not because payments+insurance cooled (+0.518→+0.529,
essentially flat), but because the sector mean itself rose faster over the same stretch, largely
inside this same group. **Capital markets nets to flat (+0.009)**, confirming M40's "+0.005"
carried finding almost exactly two runs later. All **3 red tags** (AXP, C, MS) sit **outside**
payments+insurance; **4 of the 5 green tags** (MA, V, CB, TRV) sit **inside** it, the fifth being
JPM — itself the sector's biggest bank by cap.

**Alternative grouping, and what it does to the answer (C5 — required).** Re-cutting on the flow
file's own native 12-way GICS sub-industry field (the same field used for the exchange-node W5 cut
in the prior report) does **not** dissolve the concentration finding — it **sharpens** it:

| sub-industry (n) | eqflow mean | 🟢 | 🔴 |
|---|---|---|---|
| Property & Casualty Insurance (5) | +0.579 | 2 | 0 |
| Financial Exchanges & Data (7) | +0.556 | 0 | 0 |
| Life & Health Insurance (3) | +0.534 | 0 | 0 |
| Transaction & Payment Processing (4) | +0.529 | 2 | 0 |
| Insurance Brokers (3) | +0.470 | 0 | 0 |
| Multi-line Insurance (1, AIG) | +0.447 | 0 | 0 |
| Asset Management & Custody Banks (7) | +0.383 | 0 | 0 |
| Diversified Banks (7) | +0.194 | 1 | 1 |
| Regional Banks (2) | +0.147 | 0 | 0 |
| Multi-Sector Holdings (1, BRK-B) | +0.012 | 0 | 0 |
| Investment Banking & Brokerage (5) | +0.009 | 0 | 1 |
| Consumer Finance (2) | **−0.335** | 0 | 1 |

Under the finer cut, the top five sub-industries by flow (+0.579 to +0.470) are **insurance in three
flavors, payments, and exchanges** — 22 of 47 names, **zero red tags among them**. The bottom four
(Diversified Banks, Regional Banks, IB&Brokerage, Consumer Finance — 16 of 47) carry **all three red
tags** and materially lower means, down to outright negative for Consumer Finance. So the finer
grouping restates the same boundary the coarse one found (it is not a banks-vs-payments artifact of
how I drew the lines) — it just shows the exchange node (flagged separately in the 07-25 report as
RS60-negative) is *currently* inside the same high-20-day-flow cohort as insurance and payments,
which is a genuine addition the coarse grouping hid.

**Verdict stated in the form the evidence supports (C4):** the sector-level "eqflow > wflow, 5🟢/3🔴"
reading is **not indistinguishable from noise, and it is not sector-wide breadth either** — it
decomposes cleanly into (a) one mega-cap flow-flat name mechanically depressing wflow, plus (b) a
real, narrow cluster (insurance + payments + exchanges, ~29 of 47 names including asset managers)
carrying essentially all of the sector's positive flow and 100% of its green tags, against a
genuinely mixed-to-negative bank/broker/consumer-finance cohort (18 of 47) carrying all three red
tags. "Financials breadth" describes the first cluster, not the sector.

---

### ② Which sub-node's earnings still depend on the curve, and which has migrated away — updated with the live rate state

Carried mechanism (M138, unchanged): WFC's Q2 NII **missed** ($12.32B, +5% YoY) with FY26 guidance
**held flat at ~$50B**, CFO citing growth in **interest-bearing** deposit mix; JPM's Q2 NII guidance
was **raised to ~$105.5B** on **markets-related** balances. The split is: **deposit-spread NII**
(impaired by a flattener) vs **markets/financing-balance NII** (a different driver — balance growth
and volatility, not curve level).

**Where the curve sits right now, against S23's own threshold.** `[FRED]` DGS2 **4.37%**, DGS10
**4.71%** ⇒ **T10Y2Y = +0.34**. S23's flattener condition is DGS2 inside 4.15–4.45% (currently
**inside**, with room either side) **and** T10Y2Y ≤ +0.20 (currently **+0.14 away**, not yet met).
**S23 has not fired.** No newer print exists before Monday afternoon (Friday's FRED values publish
07-27 PM ET) — this is the same 07-23 snapshot as the prior run, correctly not re-estimated.

**The FOMC is the plausible trigger for exactly the missing 0.14pp.** CME FedWatch **hike**
probability for *this week's* meeting (07-29) rose **12% → 36%** in the week to 07-27; by the
Sept-16 meeting, 52.4% → 82.4%. A hawkish surprise or hawkish-hold repricing would be expected to
sell the front end faster than the long end (DGS2 up more than DGS10) — a textbook bear-flattener —
which is the mechanism that would close the remaining gap to T10Y2Y ≤ +0.20. **This is a forward
mechanical link, not a measured one: flagged `[inferred]`, no lag regression run (W2).**

**Sub-node split on today's data.** Diversified Banks (the deposit-funded, spread-dependent cohort:
JPM BAC USB PNC TFC WFC C) sit at eqflow **+0.194** — mixed, not accelerating, C outright red
(−0.744). Regional Banks (HBAN, FITB — the only two in this top-300-cap universe, both pure
deposit-spread books) sit at **+0.147**, the second-lowest sub-industry mean on the board.
Investment Banking & Brokerage (SCHW HOOD GS MS IBKR — the markets/financing-balance cohort) sits at
eqflow **+0.009**, essentially flat, with MS **red** — but its **RS60 vs SPY is uniformly strong and
positive across all five members** (IBKR +14.6, GS +10.7, MS +8.8, SCHW +8.4, HOOD +11.8), and GS's
estimate book (carried) is **current-quarter +17.7%/90d on 8↑:0↓ (30d)**, **current-year +19.5%/90d
on 9↑:0↓**. Read together: the markets-linked cohort already re-rated hard over 60 days on the
NII-migration story and the estimate book keeps confirming it fundamentally — but the **most recent**
20-day flow has gone flat-to-negative (GS, MS both red-adjacent), which is a distribution-after-the-
move signature, not a fresh re-acceleration. The curve-dependent cohort (Diversified + Regional Banks,
16 names) has neither the estimate momentum nor the flow to show it has been given anything new to
re-rate on. **Answer: earnings dependence on the curve is now concentrated in the deposit-funded
bank/regional cohort (16 names, weak flow, no estimate acceleration); the markets/financing-balance
cohort (IB&Brokerage, 5 names) has migrated away from curve-level dependence onto balance growth and
volatility, has already priced that migration in RS60, and its current 20-day flow is fading rather
than extending.**

**Credit-spread caveat, newly relevant.** HY OAS **2.77%** (07-23), **+9bp** — the first material
widening in six runs, still only 14bp off a 365-day low, while NFCI **−0.552** keeps easing (5th
week). That is a genuine, small divergence: broad financial conditions are still loosening while
high-yield credit shows its first wobble in weeks. It bears more directly on capital-markets revenue
(underwriting, trading) than on deposit-spread NII, and is not yet large enough to read as anything
beyond a watch item.

---

### ③ The exchange node's replacement observable — no new information exists yet, and that itself is the finding

**The registered replacement (K1, carried):** equal-weight excess return of the 7 exchange/data names
(NDAQ SPGI ICE CME MCO MSCI COIN) vs SPY, accumulated **2026-07-24 close → 2026-08-07 close**. At
registration it stood at **−3.00pp over the prior 5 sessions**, having peaked 07-17.

**Where it stands now: unchanged, because there is nothing to update it with.** This run's flow file
is the **same 07-24 settled asof** as the file the observable was registered against, and per the
run-clock constraint, today's partial session (~40 minutes old) cannot legitimately move a settled
excess-return statistic. **The observable's first possible update is after tonight's 07-27 close.**
Reporting a change here would require exactly the kind of premature RS read this file is built to
avoid (the SPY-8.6%-of-a-session problem named in the run clock). Correctly stated: **K1 = −3.00pp,
unchanged, next check after 07-27 close; hard confirm/falsify resolution remains 08-07.**

**What did move: nothing has printed yet, but two of the seven print this week.** SPGI reports
**07-28**, ICE reports **07-30** — both inside the K1 window and both still ahead of us. Neither has
disclosed anything since 07-24. CME, MCO, MSCI remain unable to print before 2026-10-20/21/22 (C3,
`[blank]`, not neutral). COIN is a standalone β≈3 crypto-volume object and should be read out of the
node per the carried A2 anti-signal.

**No revision to the §0-of-07-25 conclusion is warranted**: the registered rolling-RS60 test remains
structurally biased toward CONFIRM by 08-08 regardless of what happens next, and the only sub-node
member close to crossing on arithmetic (SPGI) is simultaneously the node's worst estimate book
(next-year EPS −8.1%/90d, carried) — that tension is unresolved until 07-28.

---

## §1 · M150 exhaustion geometry — decomposed for all five green names, not just TRV

Using the file's own rs20/rs60 (already SPY-relative, C1) as the last-20 / full-60 split:

| ticker | rs20 vs SPY | rs60 vs SPY | rs20/rs60 (last-20 share of 60d) | read |
|---|---|---|---|---|
| **TRV** | +21.0 | +21.1 | **99.5%** | reproduces carried M150 (98.6%) — a steady late-window run, not a reversal |
| **JPM** | +4.8 | +9.6 | 50.0% | roughly linear — half the 60-day excess predates the last 20 sessions |
| **V** | +7.0 | +11.2 | 62.5% | moderately back-loaded, not extreme |
| **CB** | +8.1 | +5.1 | **158.8%** | last 20 days *exceed* the full 60-day excess — the first ~40 days were net negative vs SPY |
| **MA** | +9.7 | +2.5 | **388.0%** | same pattern, more extreme — almost the entire 60-day excess is a last-20-day event |

Two of five (CB, MA) are not "steady acceleration into exhaustion" like TRV — they are **V-shaped
reversals**, where the last 20 sessions erase an SPY-relative deficit rather than extend a lead.
**CB's is dated and explained**: CB reported Q2 on **2026-07-22** (`module_fundamentals_us`, live
pull), with current-year EPS revised **26.98 → 27.56 (+2.1%/90d)** and current-quarter **6.27 → 6.31
(+0.7%)** — an n≈1 earnings print, the same S1 shape as TRV's 07-17 jump, just one sub-node over.
**MA's is not.** MA does not report until **2026-07-30** — its 20-day, 388%-of-60-day surge has **no
earnings catalyst behind it yet**, and its own estimate book is flat-to-slightly-down (current-quarter
**4.85→4.78, −1.6%/90d**; current-year **+0.3%**, essentially flat; live pull, `module_fundamentals_us`
07-27). A near-4x concentration of trailing excess into 20 days with a flat book and an unreported
print ahead of it is the least-supported of the five green tags and the one most exposed to K5
(07-30) disappointing.

---

## §2 · Delta since 2026-07-25

1. **New this run**: the eqflow>wflow question is decomposed into a mechanical layer (BRK-B, 13.94%
   of sector cap at flow +0.012, explains 56% of the gap) and a real-but-narrow layer
   (payments+insurance, 1.55× sector mean, carries 4 of 5 green tags) — the 07-25 file did not carry
   this question; it is answered fresh here from the raw 47-name pull.
2. **CB confirmed as an n≈1 earnings print** (07-22, live pull) — the sector's third green name shown
   to be single-print-driven, alongside TRV (07-17, carried). MA's 20-day surge, by contrast, has
   **no supporting print** and is the weakest of the five green tags on this measure.
3. **T10Y2Y distance to S23's threshold now quantified**: +0.34 vs the ≤+0.20 trigger, a **0.14pp
   gap**, with the FOMC's own repricing (hike odds for 07-29 up 12%→36% in a week) offered as the
   plausible — but unmeasured — mechanism that could close it. This was qualitative in 07-25; it is
   numeric here.
4. **K1 (exchange-node replacement observable) has not moved** — still −3.00pp, because no settled
   close has occurred since registration. This is reported as a non-update, not silently dropped.
5. HY OAS's +9bp widening (07-23) is carried forward as a live watch item against the NII-migration
   read in §0②; NFCI still loosening in the same window is flagged as the divergence worth tracking.

---

## §3 · Track KPIs and anti-signals — dated observables

| # | Observable | Date | Confirms | Falsifies |
|---|---|---|---|---|
| K1 ★ | Equal-weight excess of the 7 exchange names vs SPY, 07-24→08-07 | 2026-08-07 (next update: after 07-27 close) | > 0 ⇒ new money | ≤ 0 ⇒ roll-off only, de-rate intact |
| K2 | SPGI Q2 print, the node's only ≈RS60-crossing name with a −8.1% next-year book | **2026-07-28** | Guide raise + breadth turns ↑ | Another cut ⇒ de-rating on fundamentals |
| K3 | ICE Q2 print, 0↑:2↓ (30d) current-quarter book vs +24.8% target gap | **2026-07-30** | Book turns up | Cut again ⇒ target gap was stale |
| K4 | T10Y2Y vs S23's ≤+0.20 threshold — currently **+0.34, 0.14pp away** | 07-29 FOMC → 08-05 | Closes to ≤+0.20 without breaching DGS2 4.15–4.45 ⇒ spread-NII leg impaired | Stays >+0.20 or DGS2 exits band ⇒ S23 does not fire |
| K5 | V (07-29) and MA (07-30) prints — MA's flat book + unsupported 388%-of-60d rs20 concentration | 07-29 / 07-30 | Both beat + guide up ⇒ payments breadth earnings-backed | MA guides down/flat ⇒ its green tag was pre-print positioning, not fundamentals |
| K6 | CB's 07-22 print already in price (2.1% CY EPS raise) — next check is guidance durability, not the print itself | ongoing | Estimates keep drifting up post-print | Estimates roll over ⇒ 07-22 pop was a one-day re-rate, not a trend change |
| A1 | Anti-signal — BRK-B (13.94% of sector cap, flow +0.012) treated as a "Financials name" in any cap-weighted sector statistic | ongoing | — | Any sector wflow move driven by BRK-B alone is a BRK-B statistic, not a Financials one |
| A2 | Anti-signal — COIN counted inside the exchange node | ongoing | — | Carried from 07-25; unchanged |
| A3 | Anti-signal — MA's green tag read as confirming payments-sector breadth before 07-30 | 07-30 | — | MA's current flow is unsupported by its own estimate book; do not extrapolate until the print |

---

## §4 · Sub-node map (binding constraint named)

- **Payments+insurance (16 names, incl. exchanges 7 under the finer cut = ~23):** binding constraint
  is **earnings-print concentration** — 2 of its 5 green tags (CB, TRV) are single-day, already-
  reported re-rates; a 3rd (MA) has an unsupported pre-print run. W4: payments are paid per-swipe by
  merchants/issuers (MA/V/PYPL/XYZ); P&C/life insurers are paid premiums by policyholders and are
  currently repricing risk (CB, TRV); this is not one customer base, it is three, correlated only
  through the flow-file's positive tag.
- **Banks/brokers/consumer-finance (18 names):** binding constraint is **curve dependence vs curve
  migration**, per §0②. Diversified/Regional Banks (16) are customer-deposit funded and exposed to
  T10Y2Y; IB&Brokerage (5, one double-counted with capital markets group) is exposed to trading
  volumes/AUM and has already priced its migration away from the curve.
- **Exchanges & Data (7):** binding constraint remains the **broken registered confirm test** (07-25
  finding, unrevised) — the only live update is that its replacement observable (K1) has not yet had
  a chance to move.
- **BRK-B (1):** binding constraint is that it is **not comparable to any peer in this sector** —
  an insurance/equity-portfolio conglomerate whose flow score is structurally muted by its own size
  and diversification, and whose cap weight (13.94%) is large enough to distort sector-level
  cap-weighted statistics on its own.

---

## ✅ EXIT CHECK

- [x] **§0 answers all three mandated questions first, with numbers**, using the raw 47-name pull
      (not the carried grouping) for ① and quantifying the S23 curve gap (+0.34 vs ≤+0.20) for ②.
- [x] **Continuous-track, delta-led** — §2 lists exactly what is new; the 47-name map and prior
      sub-node/counterparty detail are carried by reference, not reprinted.
- [x] **C1** SPY named at every relative number · **C4** the sector breadth question is answered
      as a decomposition (mechanical + real-but-narrow), not "confirmed"/"rejected" · **C5** both the
      coarse (banks/capmkt/pay+ins/other) and the alternative (native 12-way GICS) groupings shown,
      with the alternative's effect stated explicitly (sharpens, does not dissolve, the finding).
- [x] **D6** — OBV tags treated as corroborant only throughout; the exchange-node and NII-migration
      verdicts rest on RS/estimate-book data (A-grade), not flow tags.
- [x] **S1** — CB (07-22) and MA (unreported, 07-30) both checked against single-print risk; MA
      flagged as the weaker case because it has **no** print behind its run.
- [x] **W2** — the FOMC→T10Y2Y mechanism explicitly marked `[inferred]`, no lag regression run, not
      cited as settled evidence.
- [x] **W4** — customer/counterparty named for the payments+insurance and bank/broker clusters.
- [x] **D52** — no z-score/base-rate statistic was computed in this file requiring a FINRA base20
      comparison; none suppressed or misapplied.
- [x] **R11 (retracted steepener) not cited anywhere.** No sizing, no buy/sell language (P4).
