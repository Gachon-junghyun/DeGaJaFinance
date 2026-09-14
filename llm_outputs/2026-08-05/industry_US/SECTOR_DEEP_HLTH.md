# SECTOR_DEEP_HLTH — Health Care — industry_US — 2026-08-05 (Wed) · ★ PREMORTEM-PROMOTED 5th SLOT

> HLTH earned **no slot on the rotation rule** (`SECTOR_ROTATION §3`: "3rd-worst flow… it gets no
> slot and that is a real cost"). **Lens 1 of `BLINDSPOT_PREMORTEM` promoted it** to resolve C7's
> pre-registered, dated 08-06 observable — the promotion is the object under test, not a bull case.
> Flow/RS **asof 2026-08-04 settled** (`SWEEP_READ §0`: D74 trimmed, live 08-05 bar removed). Price
> series re-pulled independently, `auto_adjust=False`, trimmed ≤2026-08-04 — no leakage confirmed.

## 0 · Does the promotion survive its own test?

**Partially, and only on the letter of the rule.** C7's raw green-count observable reads **1** today,
**unambiguous under both competing definitions** (a genuine first — §2) — technically not a failure.
But its *substance* fully rotated: the name it survived on 07-30 (HCA) reversed hard and is no
longer green, replaced by a name **this desk rejected 24 hours earlier as momentum-only** (BMY).
And **the second registered anti-signal — "XLV's 5-day excess vs SPY turning negative while SPY
rises" — is CONFIRMED FIRING today** (§1). ⇒ The observable technically survives while the
anti-signal built to catch a false positive is simultaneously true — "trending toward its own
anti-signal," not resolution.

## 1 · Numbers verified independently

From `SECTOR_FLOW_US.json` (asof 2026-08-04), cross-checked against a fresh `yfinance` pull:

| Claim | JSON | Independent check | Match |
|---|---|---|---|
| BMY flow/OBV/RS20/RS60/surge | 0.956 🟢가속 · 매집 +0.527 · +10.5/+11.7 · 1.52 | RS20/RS60 exact | ✅ |
| HCA flow/RS20/RS60 | −0.572 · −8.4/−12.0 (tag now 🟡중립, obv 중립 not 분산) | exact | ✅ |
| TMO flow/RS20/RS60 | +0.515 · +6.2/+13.6 | exact | ✅ |
| XLV exc5/exc20 vs SPY | MACRO §B: −7.20/−4.58 | own pull: −7.198/−4.582 | ✅ |
| Sector aggregate | wflow −0.253, eqflow −0.112, 🟢1/🔴11 of 32, breadth 0.03, delta −0.201 | exact | ✅ |
| BMY FINRA short z | −2.50 (SWEEP §5) | `us_flow.py`: −2.50, 5v5 −7.8▼ (pressure leaving) | ✅ |

No discrepancy found; only 1 of 32 HLTH names is green. [context] HCA short z −0.14, 5v5 **+12.5▲
building** while price falls — a real reversal, not profit-taking.

## 2 · C7 reproduced — registered definition, applied to today's bar

07-30's registered observable: **"one 🟢 from OUTSIDE the top-6 by market cap,"** with two competing
definitions: **cap-rank top-6** (LLY·JNJ·ABBV·UNH·MRK·AMGN, $182.2bn cutoff) vs **the desk's named
block** {LLY, JNJ, ABBV, MRK, TMO, UNH}. Neither fixed by a human.

Today only **one** name is green: **BMY** ($110.3bn), outside the cap-rank top-6 **and** the named
block — first time since 07-23 the observable is unambiguous under both definitions, an
improvement on 07-30's 1-or-2-depending-on-definition mess.

⚠ **PRE-COMMITMENT, not the score.** The registered second observable is due **08-06**; this is one
day early (S1: n=1). Two things weaken it: (1) **HCA — 07-30's sole carrier — is no longer green**,
the evidentiary base fully turned over in six sessions; (2) **the second anti-signal fires
concurrently** (§7). A count of 1 resting entirely on a name rejected yesterday is not the same
fact as a count of 1 on an un-rejected name — recorded, not collapsed into "count=1."

## 3 · Does BMY's move have a real cause, or is it bare momentum?

**Mixed — real primary cause for most of it, unconfirmed talk for the marginal top.** Price: $58.72
(07-15) → $64.86 (07-30) → $65.89 (08-04): **+10.4% of the move happened before any M&A headline
existed.** `module_disclosure_us BMY --days 10` shows an **8-K, Item 2.02 (earnings), filed 07-30**
— real, primary, coincident with the window's largest daily jump (+2.8%). The **M&A/계약 category is
EMPTY** for BMY — no 8-K confirms the AstraZeneca talk. `module_news_data search BMY --scope
foreign` shows CNBC/SeekingAlpha both **citing the Financial Times** (AstraZeneca-Bristol Myers
"$400bn megadeal," 08-02) — a secondary rumor, not company disclosure. The move after the story
broke (+0.9% over two sessions) is small against the earnings-driven run. **Grade: earnings = B;
M&A talk = C (unconfirmed, ≤~1pp).** "Surged to 52-week highs" overstates it: $65.89 sits 3.2%
below the actual high, $68.10.

## 4 · Segment test (days 21–60 vs SPY, settled closes, auto_adjust=False)

| Ticker | RS20 | RS60 | segment 21-60 | tag |
|---|---|---|---|---|
| BMY | +10.5 | +11.7 | **+0.9** | run, razor-thin |
| TMO | +6.2 | +13.6 | **+6.7** | genuine run |
| HCA | −8.4 | −12.0 | **−3.6** | real decline, not a repair |
| LLY | −12.9 | +9.0 | **+24.5** | fading peak |
| ABBV | −7.4 | +14.8 | **+23.4** | fading peak |
| MRK | −3.8 | +8.5 | **+12.5** | fading peak |
| UNH | −8.0 | +4.8 | **+13.6** | fading peak |
| JNJ | −7.8 | +9.1 | **+17.9** | fading peak |
| PFE | +2.4 | −9.5 | **−11.3** | repair (TURN-OFF-A-HOLE) |

Confirms Lens 3's flag: BMY's segment is +0.9, run-side by the table's thinnest margin. The reject
ledger recorded this same segment at **−1.3** the date filed — a sign flip inside roughly one
session. **The instability, not the sign, is the finding**: one more red session flips BMY into
repair alongside HCA/PFE. The five pharma/managed-care names show the opposite shape — fading peak,
negative last-20 against a strong 40-day base — the sector's dominant pattern, not BMY's.

## 5 · Sub-sector dispersion (rule W5)

Eq-mean flow by industry group: **Pharma +0.079** (n=5) · Life Sciences Tools +0.070 (n=4) ·
Equipment +0.054 (n=8) · Services −0.210 (n=2) · Biotech −0.216 (n=6) · Distributors −0.359 (n=3) ·
Managed Care −0.445 (n=3) · Facilities (HCA alone) −0.572. Spread top-to-bottom ≈0.65 vs a sector
eqflow level of −0.112 — **~5.8× the level**, the same W5 conclusion 07-30 reached (then 140%).
⚠ **Pharma's "best" rank is a single-name artifact**: ex-BMY, (PFE+JNJ+MRK+LLY)/4 = **−0.140**,
negative like everything else. **Every bucket is negative except the one name carrying C7.**

## 6 · Valuation + estimate momentum (margin percentile, not multiple alone)

**BMY**: forward P/E **9.78**, PEG 2.51. `margin_history.py BMY` — contrary to 07-30's sector-wide
"L2 unrunnable" finding, its series is **live and complete (FY2007–FY2025)**: range 68.5%–78.6%,
median 72.7%; **FY2025 = 71.1%, ≈25th percentile of own history** — below-median, not distressed. A
sub-10 forward P/E against a below-median margin is moderate, not clean, cheapness. Estimate
momentum: current-year EPS +10.3% (90d), 12↑:6↓ (30d) positive; **next-year 6↑:10↓, net negative**.

**TMO**: forward P/E 20.82, PEG 1.87. `margin_history.py TMO` **confirms 07-30's finding**: series
**truncated at FY2017**, no current-year percentile — **no cheapness claim made (C3)**. Estimate
momentum: current-year 18↑:0↓ (30d, unanimous) — the sector's cleanest revision breadth.

## 7 · Track KPIs + anti-signals, dated

- **KPI (frozen from 07-30)**: count of 🟢 outside HLTH top-6 by cap, both definitions. **Today
  (PRE-COMMITMENT): cap-rank 1 (BMY) · named block 1 (BMY)** — unambiguous for the first time.
- **Anti-signal 1, quoted (07-30)**: *"that count returning to 0 on the 08-06 read ⇒ today was a
  one-session artifact and C7 goes back to unmeasured."* Not fired — scored read still pending.
- **Anti-signal 2, quoted (07-30)**: *"XLV's 5-day excess vs SPY turning negative while SPY rises ⇒
  the outperformance was defensive rotation, not sector demand."* **FIRING TODAY**: exc5 −7.20
  while SPY d5% +4.11%.
- **New dated observable**: BMY's segment sign at the next settle — +0.9 today vs −1.3 on the reject
  ledger same date. Negative on 08-06 ⇒ BMY joins HCA/PFE as a repair; C7's sole green loses its
  "genuine run" read too.
- **Ledger, not resolved (mandate)**: BMY's reject row (`2026-08-04`, class `B.모멘텀only`,
  `revives_if`: "segment turns positive and RS20 stays >0", recheck `2026-08-18`). Both conditions
  arguably already true today, two weeks early — tension reported, not adjudicated.

## ✅ Coverage

flow ✅ · C7 reproduced ✅ (PRE-COMMITMENT labeled) · cause check ✅ (8-K vs rumor, graded) ·
segment test ✅ (9 names) · dispersion ✅ (W5) · valuation ✅ (BMY margin percentile; TMO
truncation, no claim) · KPI + both anti-signals ✅ (dated, one firing) · no ledger row resolved.
