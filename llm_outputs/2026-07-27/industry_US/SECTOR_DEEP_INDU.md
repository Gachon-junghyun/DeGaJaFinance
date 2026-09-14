# SECTOR_DEEP_INDU — Industrials, sector-level map — 2026-07-27 (Mon)

> **Rotated back inside the recency window because the registered falsifier fires in under 24 hours.**
> UPS prints **2026-07-28** = **S20 + S20-ANNEX** — simultaneously (i) the desk's pre-registered
> falsifier of the rail node promoted 2026-07-24 and (ii) dig **D23**'s fifth and last unread refiner
> customer (**W4**). The 2026-07-24 file (`llm_outputs/2026-07-24/industry_US/SECTOR_DEEP_INDU.md`)
> narrowly mapped the rail/freight node only; **this file is the fresh sector-level map** it deferred.
>
> ⚠ **Run clock: 2026-07-27 ~09:4x ET.** The US session is minutes old. **Last settled close = Friday
> 2026-07-24.** Per binding instruction, **no `module_flow <TKR>` calls were made for RS/OBV/flow
> numbers** (today's partial bar measured elsewhere at 8.6% of a session's volume on SPY) — **every
> RS/OBV/flow figure below is read from `SECTOR_FLOW_US.json`, `asof 2026-07-24`, settled.** Filings,
> fundamentals and news were pulled live 2026-07-27. Analytical only — **zero buy/sell, zero sizing.**

---

## §0 · THE THREE VERDICTS, FIRST

### ① Is Industrials one sector or three? — **THREE, and the split is measured stable, not a snapshot artifact.**

| Node | n | mean flow | 🟢/🔴 | mcap share |
|---|---|---|---|---|
| Defense primes (LMT·RTX·NOC·GD·LHX) | 5 | **+0.667** | 3/0 | 11.3% |
| Rails/freight (UNP·CSX·NSC·ODFL·UPS·FDX) | 6 | **+0.368** | 2/1 | 9.9% |
| Capital goods + everything else | 39 | **−0.193** | **0/16** | **78.8%** |

Re-derived independently from the 50 raw Industrials rows in `SECTOR_FLOW_US.json` — every count above
matches the mandate's own table exactly (mcap $5,220.2B total). **Spread = 0.860**, against the
sector's own mean flow of **−0.040** — the internal split is **21× larger than the sector's own
average move.** ★ **W5 test applied explicitly: the sub-node spread (0.860) dwarfs the sector's own
move (−0.040), so the sector label is the wrong unit of analysis.**

**Stability check (M36's caution, applied directly): exclude the single largest contributor on each
side.** Drop LMT (primes' top flow, +0.856) and VRT (capital-goods' most negative, −0.911):

| | full node | excl. largest mover | decay |
|---|---|---|---|
| Primes mean flow | +0.667 | **+0.620** (ex-LMT) | −7% |
| Capital-goods mean flow | −0.193 | **−0.174** (ex-VRT) | −10% |
| **Spread** | **0.860** | **0.795** | **−7.6%** |

The ranking holds and the spread stays **above M26's original 0.705** even with the single biggest
mover on each side removed. A median-based cut is if anything wider: primes median **+0.744**,
capital-goods median **−0.301**, spread **1.045**. **Verdict: the split is real and durable across two
different aggregation methods, not an artifact of one earnings pop (LMT) or one air-pocket (VRT).**
This corrects the M36 lineage carried in `handoff/STANDING_VIEW.md` (0.705 → 0.285 trough → 0.860 on
07-24, now re-confirmed one session later on 07-27's read of the same settled close) — **the spread did
not decay, the desk was comparing the wrong two nodes for one session.**

**All five of the sector's greens are primes or rails. Zero of 39 capital-goods names is green; 16 of
17 sector reds sit in that bucket, on 78.8% of the sector's cap.** One exception worth naming: **CTAS**
(Diversified Support Services, technically inside the "everything else" bucket) carries the sector's
**best RS20 (+21.1 vs SPY)** but stays 🟡, not 🟢 — its `vol_surge` is only 1.02 and delta is negative
(−0.055), so it fails the desk's own 3-axis green test (M25) even though its relative-strength axis is
clean. Flagged so the "0 green in capital goods" finding is not read as "nothing there is working."

### ② Does the rail node survive a VOLUME-driven UPS cut? — **The annex holds one day later; the crack is the mechanism, and the option market is priced for calm on the desk's own falsifier.**

**S20-ANNEX (frozen 2026-07-25, not re-frozen here):** observable = median RS20 vs SPY of {CSX, UNP,
NSC}; threshold = that median turns negative by 2026-08-04. Branch A (fuel quantified materially
higher YoY) closes W4/D23 5-of-5. Branch B (guidance cut on **volume**, not fuel) = INDU N is false
comfort.

Measured today (asof 07-24, one session later than the annex's registration): **CSX RS20 +11.6, UNP
+14.2, NSC +11.7 vs SPY → median +11.7**, comfortably above zero and unchanged in sign from the
annex's registration state. **The annex's threshold is not close to tripping**, but it does not settle
until 2026-08-04 and UPS prints first.

**Options priced for calm on the falsifier itself** — pulled fresh today, compared against the
S20-ANNEX's own 07-25 pull:

| | 07-25 (annex registration) | 07-27 (today) |
|---|---|---|
| Implied move | ±6.9%, expiry 07-31 (D6) | **±6.8%, expiry 07-31 (D4)** |
| P/C | 0.35 | **0.34** |
| Skew | +11.1 | **+1.6** |
| Short % float | 3.1%, covering | **3.3%, covering** |
| Days-to-cover | 4.3 | **5.1** |

The straddle itself is essentially unchanged (still the board's only genuinely event-priced instrument
on this name, ~1.8× realized 20-day σ) — but **skew compressed from +11.1 to +1.6 in two sessions**,
i.e. downside-put demand relative to calls eased sharply into the print, and short interest ticked up
marginally while days-to-cover rose (more short shares, thinner daily volume to cover them against).
**Read together: the option market is calmer about a large move than it was two days ago, on the
desk's own registered falsifier of the rail thesis** — consistent with, not falsifying, the mandate's
framing that "the option market is priced for calm."

**M91 restated and re-grounded on today's numbers, not carried unchanged:** the fuel-surcharge
decomposition from the 07-22/23 Q2 prints is a filed fact, not a flow read, so it does not move day to
day — but the RS state that sits on top of it has: **UNP RS20 fell 16.4 → 14.2, RS60 rose 10.0 → 11.0**
(comparing the 07-24-close file's numbers to today's identical-source read one calendar day later);
**CSX RS20 fell 11.6 from a differently-computed 14.0** in the two files (methodology note: the prior
file's table used a 07-23 close, this file's uses 07-24 — one session's difference explains the
divergence, not a reversal). The shape is consistent with a post-earnings pop that is fading on the
20-day window while continuing to build on the 60-day window — the base effect of the print rolling
into the trailing average, not fresh accumulation.

**★★ M91 stands, restated: ~8 of UNP's 12 Q2 revenue-growth points were fuel surcharge** (ex-surcharge
freight revenue +4%); **CSX intermodal +26% revenue on +9% volume, RPU +16% "driven by fuel
surcharge"** (company's own words); Q1'26 YoY was ~flat at all three rails. **UNP is double-hit under
Branch B**: a volume cut and a rolling crack are one shock counted twice through the rail leg, not two
independent risks.

**Positioning is unreadable on the two names that matter most, and this file does not quote the
suppressed verdicts** — re-run live today via `scripts/us_flow.py UPS UNP CSX NSC`, matching
`MACRO_REPORT.md`'s own D52/D73-gated table exactly:

| Ticker | short% | base20 | z | 5v5 | Readable? |
|---|---|---|---|---|---|
| **UPS** | 52.0% | **57.7%** | −1.12 | flat | ❌ baseline 12.7pp above the tool's 40–45% normal band — **verdict suppressed (D52)** |
| **UNP** | 31.8% | **52.2%** | −2.41 | −11.8▼ | ❌ baseline out of band — the "short-covering" string is **suppressed, not reported** |
| CSX | 37.7% | 35.9% | +0.18 | −10.2▼ | ✅ in band — neutral, pressure easing on trend |
| NSC | 48.0% | 42.6% | +0.78 | −1.8▼ | ✅ in band — neutral |

**D73's point applies with a date attached: the two names whose Q2 prints and Q2 fuel exposure matter
most tomorrow (UPS, UNP) are exactly the two whose "who is trading" axis this desk cannot read.**
Report the baseline; do not act on the tag.

### ③ Defense: is the money ahead of the narrative, and does W4 hold? — **Closed 3 of 5 from primary sources; GD partial (pre-print); LHX open.**

| Name | W4 status | Primary evidence |
|---|---|---|
| **LMT** | ★ **Closed.** Q2 printed 07-23: revenue $20.1B (+11%), EPS $7.94, **$65B new Q2 orders incl. a $35B multi-year THAAD/MDA agreement**, **record backlog $230.4B (from $166.5B a year ago, +38.4%)**. Guidance raised to revenue $79.75–81.75B, EPS $29.95–30.65 [yahoo_finance, seekingalpha, both 07-23/07-27] | 10-Q + 8-K Item 2.02, 07-23 |
| **RTX** | ★ **Closed.** Q2: revenue $24.7B (+16% organic, 5th consecutive beat), EPS $1.89, **backlog record $289B ($170B commercial aerospace + $119B defense), +22% YoY**. Guidance raised: EPS $7.10–7.25, revenue $95–96B [yahoo_finance 07-23] | 8-K Item 2.02, 07-23 |
| **NOC** | ★ **Closed this run, from the primary exhibit.** Q2 8-K (Item 2.02, filed 07-21) + Exhibit 99: sales **+5% YoY to $10.9B**, EPS **$7.68** (vs $8.15 PY, which included a $1.04/sh divestiture benefit), **net awards $20.0B → book-to-bill ≈1.83×**, **backlog record $104.7B**. Guidance raised: sales $43.75–44.25B (+$250M), MTM-adj EPS $28.60–29.10 (+$1.20). ★ Its own 10-K's **#1 risk-summary bullet, verbatim**: *"We depend heavily on a single customer, the U.S. government, for a substantial portion of our business."* — the exact customer-concentration disclosure AXON's 10-K was found to lack (R9) | 8-K Exhibit 99 (`noc-06302026xearningsrelea.htm`) + 10-K risk_summary_bullets, pulled live 07-27 |
| **GD** | ⚠ **Partial — Q2 has not printed.** `next_earnings_date` = **2026-07-29**, one day after UPS. Freshest primary read is **Q1 2026** (8-K Exhibit 99.1, filed 04-29): revenue $13.5B (+10.3%), EPS $4.10 (+12%), **orders $26.6B, book-to-bill 2:1 companywide (2.2:1 defense, 1.2:1 Aerospace)**, **backlog $130.8B / total estimated contract value $188.4B**. 10-K: **68% of 2025 consolidated revenue from the U.S. government** (DoW $29.8B + non-DoW $5.0B + FMS $1.0B = $35.8B), and the business text names dated multi-year backlog on Virginia-class subs (through 2034), DDG-51 destroyers (through 2032) and T-AO-205 oilers (through 2030). `risk_factors` free text returned **empty** (D54) | 8-K Exhibit 99.1 (Q1) + 10-K business text, pulled live 07-27 |
| **LHX** | ❌ **Unmet — no fresh read available.** Next earnings **2026-07-30** (in-window, but not yet). No W4 anchor pulled this run beyond the standing dispersion number. Fwd P/E 22.4, PEG 1.7, price $305.89 vs mean target $375.11 (**+22.6% upside**), 2 SB / 13 B / 5 H, no sells — a buy-heavy book on the primes' worst RS60 name | `module_fundamentals_us`, pulled live 07-27 |

**W5 dispersion inside "defense," on today's settled flow:** RS60 vs SPY runs **GD +19.5 · RTX +17.3 ·
LMT +9.9 · NOC −10.0 · LHX −11.4** — a **30.9pp spread** — with the two `new_green` names (RTX, NOC)
sitting at *opposite* ends of it. LHX's weak RS60 sits next to the *most* bullish analyst upside of the
five (+22.6% to target) and a print three sessions out — an unresolved setup, not a verdict.

**R9 discipline applied, not waived:** the desk's registered lesson from AXON is *"no customer >10% of
net sales, municipal/state base, 'backlog' absent from the 10-K."* On the two names actually checked
this run, defense is the **opposite** case on all three counts: NOC names a single >10%-of-revenue
customer explicitly (its own #1 risk bullet), GD quantifies 68% USG revenue directly, and "backlog" is
not merely present but the headline metric of both earnings releases (NOC's release literally opens
with backlog; GD's 10-K devotes pages to dated backlog schedules). **W4 closes cleanly where checked.**
It is left **open, not assumed**, for LHX — the one name whose RS is actually negative.

**Single-outlet news, confirmed as such:** the only defense item in the 7-day news window remains
*"L3Harris signs seven-year deals to expand Patriot, THAAD manufacturing"* [seekingalpha, 07-27,
single-outlet]. `chain-hop "defense" "backlog"` (07-27) returns **zero clean candidates** — see §7.
★ Corroborating physical context found live this run, from a different search
(`fts "Patriot" AND "THAAD"`): a Guardian piece [07-24] states US/allied **Patriot and THAAD interceptor
stockpiles have been "run down by about half" after a 38-day bombing campaign** — a genuine physical
depletion/replenishment driver behind the backlog numbers, independent of the L3Harris item and not
itself flow-confirmed (no ticker in the article).

---

## §1 · Value chain, left → right — three legs, two named cross-sector chains

```
[1] DEFENSE — U.S. + allied government budgets                    ★ LEG A
    DoW / intelligence community · NATO 5%-of-GDP commitments · FY27 $1.5T proposed budget
    Interceptor stockpile depletion named directly (Guardian 07-24: Patriot/THAAD "run down by half")
      ▼
[2] PRIME CONTRACTORS — order intake                               ★★ ALL THREE CHECKED CONFIRM
    LMT backlog $230.4B (+38%) · RTX backlog $289B (+22%) · NOC backlog $104.7B (record, b:b 1.83×)
    GD backlog $130.8B / $188.4B total contract value (Q1, Q2 pending 07-29)
      ▼
[3] SUBCONTRACTORS / COMPONENT SUPPLIERS — L3Harris (Patriot/THAAD propulsion, single-outlet item)
    — the physical bottleneck on replenishment speed, not named quantitatively in this window
      ▼
─────────────────────────────────────────────────────────────────────────────
[4] SHIPPER DEMAND — the freight pie                               ⚠ LEG B, SHRINKING
    Cass Freight Index June: shipments −4.1% YoY / −3.1% MoM (carried from 07-24 file, unchanged)
      ▼
[5] ★★ LINE-HAUL RAIL NETWORK — CSX/UNP/NSC                        ★★ BINDING CONSTRAINT = terminal
    RS20 median +11.7 vs SPY (§0②) · dwell/trip-plan compliance (07-24 file, unchanged this run)     dwell
      ▼
[6] FUEL INPUT — ★★ CROSS-SECTOR CHAIN → Energy (DEEP ①)
    Diesel/jet fuel: simultaneously a rail revenue pass-through (surcharge, M91) and an airline cost
    line. Settled 3-2-1 crack 64.30 (kill line 60), unsettled 07-27 61.67 — nearest-to-kill on the
    board [EVENT_ALPHA, MACRO_REPORT §D-4 this run]
      ▼
[7] AIRLINE / PARCEL CUSTOMERS OF THE CRACK — ★★ NAMED CHAIN, §6 below
    DAL fuel expense +67% YoY, UAL +84% YoY (both primary, verified this run) — both 🔴 in Industrials
    UPS = the crack's last unread customer, prints 07-28 (§0②)
─────────────────────────────────────────────────────────────────────────────
[8] CAPITAL GOODS DEMAND — private capex, paid on a completely different clock
    0 of 39 names green, 16 of 17 sector reds live here (78.8% of sector mcap) — §0①
      ▼
[9] ★ CROSS-SECTOR CHAIN → AI/power buildout
    GEV (Heavy Electrical Equip, flow −0.151) · PWR (Construction & Eng, −0.872) · VRT (Electrical
    Components, −0.911) — the transformer/data-center-power leg of the AI capex chain, ALL THREE RED
    in this sector's own data, tracked cross-sector at S24 (median RS20 vs {VST,CEG,GEV,VRT})
```

**Three separate clocks, not one sector**: the defense leg is paid on an appropriated multi-year budget
line and its own backlog metric; the rail leg is paid by shipper share-shift against a *shrinking* pie,
levered through a shared fuel-surcharge tick to Energy; capital goods is paid by private capex that
has not turned, on 78.8% of the sector's market cap. **Averaging these into one "Industrials" verdict
prices none of the three.**

---

## §2 · Full node table — all 50 names, flow asof 2026-07-24 settled close, benchmark SPY

| Ticker | Industry | mcap($B) | flow | tag | OBV | RS20 | RS60 | vol_surge | Δ | new_green |
|---|---|---|---|---|---|---|---|---|---|---|
| UNP | Rail Transportation | 152.5 | **+0.867** | 🟢 | 매집 | +14.2 | +11.0 | 1.36 | 0.000 | — |
| LMT | Aerospace & Defense | 117.8 | **+0.856** | 🟢 | 매집 | +14.7 | +9.9 | 1.34 | +0.039 | — |
| CSX | Rail Transportation | 84.8 | **+0.856** | 🟢 | 매집 | +11.6 | +13.9 | 1.34 | −0.022 | — |
| RTX | Aerospace & Defense | 249.9 | **+0.792** | 🟢 | 매집 | +13.4 | +17.3 | 1.10 | +0.103 | **Y** |
| NSC | Rail Transportation | 67.4 | +0.767 | 🟡 | 매집 | +11.7 | +6.9 | 1.18 | 0.000 | — |
| WAB | Constr. Machinery *(rail equip.)* | 46.5 | +0.754 | 🟡 | 중립 | +6.5 | +11.1 | 1.74 | −0.004 | — |
| NOC | Aerospace & Defense | 74.1 | **+0.744** | 🟢 | 매집 | +8.0 | −10.0 | 1.23 | +0.209 | **Y** |
| CTAS | Diversified Support Services | 68.4 | +0.678 | 🟡 | 매집 | **+21.1** | +14.4 | 1.02 | −0.055 | — |
| GD | Aerospace & Defense | 94.7 | +0.661 | 🟡 | 매집 | +11.6 | +19.5 | 0.99 | +0.017 | — |
| ITW | Industrial Machinery | 76.0 | +0.544 | 🟡 | 매집 | +4.0 | +1.6 | 1.08 | −0.052 | — |
| AXON | Aerospace & Defense *(GICS-mislabelled — not a chain member, see R9)* | 34.1 | +0.450 | 🟡 | 매집 | +12.3 | +19.8 | 0.61 | +0.031 | — |
| URI | Trading Cos & Distributors | 67.5 | +0.444 | 🟡 | 매집 | −0.4 | +14.8 | 1.41 | −0.244 | — |
| ADP | HR & Employment Services | 87.3 | +0.403 | 🟡 | 중립 | +15.0 | +21.7 | 0.84 | +0.135 | — |
| WM | Environmental & Facilities | 86.2 | +0.365 | 🟡 | 매집 | +6.4 | +1.2 | 0.70 | +0.159 | — |
| EMR | Electrical Components | 84.4 | +0.365 | 🟡 | 매집 | +1.2 | +3.1 | 1.00 | +0.018 | — |
| **UPS** | **Air Freight & Logistics** | **89.1** | **+0.360** | 🟡 | 매집 | **+4.4** | **+6.6** | **0.91** | **−0.203** | — |
| PCAR | Constr. Machinery | 62.6 | +0.334 | 🟡 | 중립 | +8.0 | +6.7 | 1.29 | +0.040 | — |
| PAYX | HR & Employment Services | 35.2 | +0.311 | 🟡 | 중립 | +16.8 | +21.0 | 0.90 | −0.100 | — |
| LHX | Aerospace & Defense | 54.9 | +0.283 | 🟡 | 중립 | +3.4 | **−11.4** | 1.12 | −0.051 | — |
| TRI | Research & Consulting | 34.3 | +0.257 | 🟡 | 중립 | +10.7 | −3.5 | 0.84 | +0.058 | — |
| GE | Aerospace & Defense *(mislabelled — see 07-22 file's GE catch)* | 373.7 | +0.240 | 🟡 | 매집 | −5.4 | +18.5 | 0.78 | −0.049 | — |
| HON | Industrial Conglomerates | 145.1 | +0.200 | 🟡 | 매집 | −0.4 | +5.1 | 0.79 | −0.131 | — |
| MMM | Industrial Conglomerates | 83.8 | +0.092 | 🟡 | 분산 | +2.1 | +14.4 | 1.44 | +0.107 | — |
| ODFL | Cargo Ground Transportation | 46.0 | +0.033 | 🟡 | 중립 | +5.2 | +1.2 | 0.74 | +0.045 | — |
| FAST | Trading Cos & Distributors | 52.7 | −0.008 | 🟡 | 중립 | −0.4 | +1.4 | 0.91 | −0.077 | — |
| GEV | Heavy Electrical Equipment | 298.2 | **−0.151** | 🔴 | 분산 | −7.1 | −10.6 | 1.17 | −0.274 | — |
| AME | Electrical Components | 54.4 | −0.211 | 🟡 | 분산 | −0.2 | +1.9 | 0.95 | −0.092 | — |
| ETN | Electrical Components | 163.8 | −0.235 | 🟡 | 중립 | −4.4 | −6.0 | 0.73 | −0.467 | — |
| RSG | Environmental & Facilities | 63.1 | −0.298 | 🟡 | 분산 | +1.0 | +0.4 | 0.73 | −0.016 | — |
| HWM | Aerospace & Defense | 111.1 | −0.301 | 🟡 | 분산 | +5.3 | +16.5 | 0.66 | +0.089 | — |
| PH | Industrial Machinery | 120.2 | −0.320 | 🟡 | 중립 | −0.9 | −1.2 | 0.78 | −0.042 | — |
| GWW | Industrial Machinery | 64.5 | −0.330 | 🟡 | 분산 | −0.1 | +15.3 | 0.86 | −0.140 | — |
| CAT | Constr. Machinery | 454.1 | **−0.338** | 🔴 | 분산 | **−16.6** | +4.8 | 0.79 | +0.168 | — |
| DE | Agricultural & Farm Machinery | 159.1 | −0.373 | 🟡 | 분산 | −1.0 | +7.6 | 0.85 | −0.103 | — |
| JCI | Building Products | 88.4 | −0.378 | 🟡 | 중립 | −2.1 | −2.6 | 0.59 | −0.116 | — |
| BA | Aerospace & Defense | 175.6 | −0.540 | 🔴 | 분산 | −4.6 | −13.0 | 0.97 | +0.042 | — |
| ROK | Electrical Components | 52.7 | −0.586 | 🔴 | 분산 | −4.2 | +11.3 | 0.86 | −0.178 | — |
| FIX | Construction & Engineering | 69.2 | −0.622 | 🔴 | 분산 | −14.7 | −3.0 | 1.08 | −0.330 | — |
| CARR | Building Products | 59.6 | −0.650 | 🔴 | 분산 | −10.0 | +7.3 | 1.03 | −0.018 | — |
| **FDX** | **Air Freight & Logistics** | **77.8** | **−0.675** | 🔴 | 분산 | −5.0 | −3.7 | 0.76 | −0.385 | — |
| UBER | Passenger Ground Transp. | 145.8 | −0.706 | 🔴 | 분산 | −9.4 | −14.9 | 0.93 | −0.007 | — |
| **DAL** | **Passenger Airlines** | **55.3** | **−0.715** | 🔴 | 분산 | −8.3 | **+22.7** | 0.77 | −0.109 | — |
| FER | Construction & Engineering | 49.5 | −0.716 | 🔴 | 분산 | −10.5 | −10.7 | 0.81 | −0.206 | — |
| TDG | Aerospace & Defense | 74.3 | −0.719 | 🔴 | 분산 | −7.8 | +3.3 | 0.89 | +0.003 | — |
| CMI | Constr. Machinery | 98.9 | −0.722 | 🔴 | 분산 | −9.3 | −0.4 | 0.72 | −0.336 | — |
| TT | Building Products | 106.9 | −0.735 | 🔴 | 분산 | −5.1 | −3.8 | 0.66 | −0.243 | — |
| **UAL** | **Passenger Airlines** | **38.4** | **−0.767** | 🔴 | 분산 | −12.8 | **+27.0** | 0.82 | −0.028 | — |
| EME | Construction & Engineering | 37.3 | −0.778 | 🔴 | 분산 | −14.3 | −17.6 | 0.80 | −0.311 | — |
| PWR | Construction & Engineering | 105.4 | **−0.872** | 🔴 | 분산 | −13.5 | −4.6 | 0.63 | −0.069 | — |
| VRT | Electrical Components | 127.9 | **−0.911** | 🔴 | 분산 | −11.4 | −8.6 | 0.56 | −0.253 | — |

**Note on AXON and GE:** both carry Aerospace & Defense as their GICS industry tag but are **not**
counted in the "5 primes" node — AXON is municipal/state public-safety equipment (R9's own
finding, carried so it cannot silently re-enter as a defense name) and GE is aerospace-engine /
non-defense industrial (the 07-22 file's catch). The primes node used throughout this file is the
named five: LMT, RTX, NOC, GD, LHX.

**Dispersion, sector-wide (50 names):** flow range **+0.867 (UNP) → −0.911 (VRT) = 1.778 points**;
RS20 range **CTAS +21.1 → CAT −16.6 = 37.7pp** (population σ 9.39); RS60 range **UAL +27.0 → EME
−17.6 = 44.6pp** (population σ 10.91). ★ **UAL and DAL sit at the top of the sector's own RS60 ranking
(+27.0, +22.7) while carrying the two most negative flow deltas among freight names (−0.028, −0.109)
and OBV 분산 (distribution)** — a "was up, now being sold" shape, not a "just started" one. Their
60-day strength is a residual of an earlier move (broad airline recovery / summer-travel pricing); the
fuel-cost hit (§6) is showing up in the flow axis now, on top of it.

---

## §3 · W4 continued — DAL/UAL cross-sector chain, verified from primary Q2 releases

★ **Both DAL and UAL sit in the sector's red 39-name bucket, and both are Energy's downstream fuel
customers — a cross-sector chain worth naming explicitly, not a coincidence.**

| | DAL Q2 (reported 07-10) | UAL Q2 (reported 07-15) |
|---|---|---|
| Fuel expense YoY | **+67%** GAAP ($4,109M vs $2,458M); **+77%** adjusted ($4,410M vs $2,497M) | **+84%** adjusted ($2.3B increase) |
| Fuel price/gallon YoY | $3.66 vs $2.21 (**+66%**); adjusted $3.93 vs $2.25 (**+75%**) | $4.19 vs $2.34 (**+79.4%**) |
| Result | Operating income **down** YoY despite revenue +13%; guidance affirmed | Pre-tax margin 5.8% (adjusted 4.8%); **"nearly $6 billion increase in anticipated fuel costs"** for FY26; guidance still raised on strength elsewhere |

Both primary releases were pulled live this run and both independently corroborate the mandate's
"+66–84% YoY" fuel-bill claim — the range is if anything conservative (UAL's adjusted figure hits 84%
almost exactly at the top of it; DAL's GAAP figure of 67% sits just inside it).

**This closes 4 of 5 names in dig D23** (the refiners' downstream-customer read-through), per
`handoff/STANDING_VIEW.md` M34: **DAL (07-10), UAL (07-15/16), FDX (06-24), LUV (07-23)** all confirmed
at fuel costs +66–84% YoY; **UPS is the fifth and last**, printing 07-28 (§0②). Three of those four
names (DAL, UAL, FDX) sit inside this sector's own 39-name red bucket — **the same crack that lifts the
rail node's revenue line (M91) is simultaneously the cost line that keeps DAL, UAL and FDX red.** One
commodity, two Industrials sub-nodes, opposite signs — a structural reason the sector label cannot
carry one verdict, independent of §0①'s flow-based argument.

---

## §4 · L2 — UPS's multiple, with a margin percentile actually attached (not left blank this time)

The 07-24 file flagged margin history as an unfilled gap for the rail names because `margin_history.py`
had not been run. Run live this run for **UPS**, whose gross-margin tags don't exist in SEC XBRL
(services company; the script returns "no annual data" for exactly that reason — a genuine tool
limitation, not an error). **Substituted with operating margin, computed directly from SEC XBRL
`OperatingIncomeLoss` / revenue, FY2007–FY2025 (19 annual points):**

| | value |
|---|---|
| FY2025 operating margin | **8.9%** |
| 19-year range | 1.2% (FY2007) → 13.2% (FY2015) |
| FY2025 percentile of own 19-year history | **~21st** (4 of 19 years lower) |
| **Most recent quarter (Q1 2026, ended 03-31)** | **6.0%** — **~11th percentile** (only FY2007 and FY2012 lower) |

**This is a materially different pattern from the desk's recurring peak-denominator trap (MU at M14,
refiners at M43): UPS's 14.25× forward multiple sits next to a margin near a 19-year trough, not a
19-year peak.** A multiple without a margin percentile is not a valuation (L2) — with one attached,
**UPS reads as a genuine cyclical-trough value case, not a "priced for perfection, about to mean-revert
down" case.** That does not make it a buy (P4 — zero sizing here); it does mean the standing framing
*"the only cheap name is the only one the money is not in"* should be read as **cheap-and-depressed**,
not cheap-and-euphoric, which changes what a Branch-B outcome (§0②) would actually falsify: a fuel-led
guide-down would be consistent with a business still working through a margin trough, while a
volume-led cut would suggest the trough has further to go.

**Cross-check against the five other node names' multiples** (unchanged from the 07-24 file's pull,
not re-verified live this run since none of them print before 07-29): CSX 23.3× fwd / PEG 2.24, UNP
21.9× / 3.54, NSC 25.0× / 4.83, WAB 24.3× / 1.37, all with clean 5↑:0↓ or 9↑:1↓ revision books and
three of six trading **above** their own mean analyst target. **The cheapness and the flow are still
mutually exclusive in this node** — UPS remains the one name that is both cheap and where the money is
not, only now with a primary-sourced reason (margin trough) rather than an assumed one.

---

## §5 · Chain-hop — defense theme, flow-cross-checked, zero pass

`module_news_data chain-hop "defense" "backlog" --scope foreign` (07-27, 1500 articles scanned,
±300-char proximity, OR mode):

**Headline-named (already crowded):** GOOG/GOOGL, NVDA, MSFT, ORCL, LMT, TSLA, BA, RTX, NOC, GE, and
eight others — none new.

**Candidates surfaced (title 0× + proximity ≥2):** MRK, PWR, SPGI, CVX, DLR, D, COP, ADBE, OXY, CRWD,
SLB. **All are listicle or macro co-mentions, not body-proximate defense-chain members** — e.g. PWR's
proximity example is *"Is AGX Stock Worth Buying After Its 92% YTD Surge?"* (a different ticker
entirely, AGX/Argan, mis-attributed by the tool's proximity window), and SPGI's is *"Why GE Vernova
Stock Surged 80%"* (an index-provider co-mention, not a supply relationship). **Cross-checked against
`SECTOR_FLOW_US.json`: PWR is 🔴 (−0.872) and already logged in this file as a capital-goods red name**
— its appearance here is noise, not a genuine chain-hop find. **Zero PASS.**

Consistent with the 07-24 file's finding for the rail chain: the genuinely body-proximate suppliers of
the defense chain (propulsion/energetics subcontractors — the same node the 2026-07-22 file mapped)
remain outside this chain-hop's headline-driven candidate generation. **Recorded as a coverage
limitation, not worked around.**

---

## §6 · Track KPIs and anti-signals — dated observables

### KPIs

- **2026-07-28 — UPS Q2 = S20 + S20-ANNEX** (§0②, unmoved from registration). Categorical: fuel
  quantified + guidance cut on fuel = Branch A (closes W4/D23 5-of-5); fuel non-event = Branch B
  (against the crack thesis); guidance cut on **volume** = Branch C, **against the promoted rail node**,
  read-through to CSX/UNP/NSC/URI. Numeric annex: median RS20 vs SPY of {CSX, UNP, NSC} turning
  negative by 2026-08-04 is the frozen falsifier. **No-information zone: any UPS move inside ±6.9%.**
- **2026-07-29 — GD Q2.** Closes the one open primary-source gap in the defense W4 table (§0③).
  Watch book-to-bill (Q1 was 2.2:1 defense) and backlog delta from $130.8B.
- **2026-07-30 — LHX Q2.** The one defense name with negative RS60 (−11.4) and no fresh W4 read;
  watch whether backlog/book-to-bill closes the gap the way NOC's did this run.
- **Rolling — settled 3-2-1 crack vs the 60 kill line.** Settled 64.30, unsettled 07-27 print 61.67
  [EVENT_ALPHA/MACRO_REPORT this run] — nearest-to-kill tilt on the entire board, and the mechanism
  underneath both M91 (rail revenue) and the DAL/UAL/FDX cost line (§3). A close below 60 would
  remove the fuel surcharge from the rails' revenue growth **and** the cost pressure from the airlines'
  red tags on the same tick.
- **Rolling — CTAS's flow-tag gap.** Best RS20 in the sector (+21.1 vs SPY) held to 🟡 by vol_surge
  1.02 and negative delta; watch whether a volume confirmation would flip it green under the desk's
  own 3-axis rule (M25), which would add a fourth name to the sector's green list outside primes/rails.

### Anti-signals

- **Positioning is unreadable on UPS and UNP, the two names that matter most into 07-28** (§0②, D52/D73)
  — both FINRA baselines sit 7–13pp outside the tool's stated 40–45% normal band. This is a coverage
  gap, not a bullish or bearish signal, and should not be read as either.
- **LHX is the one defense name with negative 60-day relative strength vs SPY (RS60 −11.4) and no
  fresh backlog read** —
  it is the node's open question, not a confirmed member of the "money ahead of the narrative" case.
- **GD's Q2 has not printed**; treating GD's flow/RS state as confirmed by the same evidence as
  LMT/RTX/NOC would be reading a not-yet-observed quarter into an already-decided verdict.
- **UAL and DAL's strong RS60 (+27.0, +22.7) is inherited strength, not current accumulation** — both
  carry 🔴분산 (distribution) tags and negative deltas; the fuel-cost shock (§3) is showing up in the
  flow axis now, layered on top of an earlier, unrelated move.
- **Skew on the UPS straddle compressed from +11.1 to +1.6 in two sessions** while short interest and
  days-to-cover both rose slightly — a genuine, dated change in how the option market is positioned
  into the print, not noise; worth re-checking after 07-28 settles.
- **Cass Freight Index still shrinking** (June: −4.1% YoY / −3.1% MoM, carried unchanged from the
  07-24 file — no fresher print exists this run) — the rail node's underlying demand pie continues to
  contract even as share-shift and fuel surcharge lift its revenue line.

---

## §7 · Corrections and notes filed this run

| # | Claim | Status |
|---|---|---|
| **C-D** | The 07-24 file's M36 correction (spread 0.705→0.285→0.805, re-measured on 07-23 close) | **Re-confirmed independently on the 07-24 close, one calendar day later, using the identical re-aggregation method: spread = 0.860.** Additionally stress-tested for the first time by excluding the single largest mover on each side (LMT, VRT): spread holds at **0.795**, still above M26's original 0.705. **The split is durable across two sessions and two aggregation choices**, not a one-session artifact |
| **C-E** | NOC and GD's W4 status, carried as "no such read in any desk file" | **NOC closed this run** from its own 8-K Exhibit 99 and 10-K risk_summary_bullets (record backlog $104.7B, single-customer risk bullet verbatim). **GD partially closed** — Q1 primary data pulled (backlog $130.8B, book-to-bill 2.2:1 defense, 68% USG revenue), Q2 genuinely unprinted (next earnings 07-29), left **explicitly marked partial**, not backfilled with an assumption |
| **C-F** | UPS margin history, left blank in the 07-24 file ("the multi-year percentile is the gap this file could not fill") | **Partially filled.** Gross margin is genuinely unavailable (no COGS XBRL tag for this services company — a tool limitation, confirmed by re-running `margin_history.py` live). Operating margin substituted from raw XBRL: **FY2025 8.9% ≈ 21st percentile of a 19-year history; Q1 2026 6.0% ≈ 11th percentile** — the cheap multiple sits next to a margin trough, not a peak, which is the opposite pattern from the desk's recurring "peak-denominator" trap |

**New dig proposed:** ★ **`margin_history.py` cannot score services/logistics companies** (UPS, and by
extension likely FDX, ODFL, the airlines) because they do not file under
`CostOfGoodsAndServicesSold`/`CostOfRevenue`/`CostOfGoodsSold` tags. An operating-margin variant (as
computed manually here from `OperatingIncomeLoss`) would close this gap for the entire freight/logistics
node and any other services-sector name the L2 lens is applied to.

---

## ✅ EXIT CHECK

- [x] **Mandated Q①** answered and stress-tested: three nodes, not two or one; spread survives removing
      the single largest mover on each side; W5's own-move-vs-spread test applied explicitly
      (0.860 vs sector mean −0.040).
- [x] **Mandated Q②** answered: S20-ANNEX's frozen observable re-measured (median RS20 +11.7, unmoved
      in sign), options re-pulled fresh and compared to the annex's own 07-25 baseline (skew
      compression flagged as a real, dated change), FINRA positioning reported with baselines and
      suppressed verdicts **not** quoted (D52/D73), M91 restated and re-grounded rather than carried
      unchanged.
- [x] **Mandated Q③** answered: LMT/RTX/NOC W4 closed from primary 8-K exhibits and 10-K text pulled
      live this run (not carried from S7 unverified); GD explicitly marked partial with dated reason
      (Q2 prints 07-29); LHX explicitly marked unmet; W5 dispersion (30.9pp RS60) stated.
- [x] **Chain map, 9 nodes**, binding constraint named (rail terminal dwell, carried from 07-24 file
      since unchanged this run), **two cross-sector chains marked explicitly**: fuel surcharge → Energy
      (§6 in the chain, evidenced in §3/§0②) and AI/power/transformers/copper → GEV/PWR/VRT (all red).
- [x] **Chain-hop**: defense theme run, flow-cross-checked, **zero pass**, false candidates named and
      explained (PWR ticker/proximity noise, SPGI index co-mention).
- [x] **C1** — every relative figure names SPY inline. **C4** — LHX/GD called "unmet"/"partial," never
      "rejected." **S1** — no single-day co-movement is read as more than n≈1. **D6** — OBV states
      (매집/분산) are paired with the A-grade RS/flow axis throughout, never cited alone.
- [x] Blanks left blank where genuinely unfilled: LHX's fresh W4 read, GD's Q2 print, the tariff/STB
      items from the 07-24 file (not repeated here, out of this run's scope).
- [x] Zero buy/sell, zero sizing throughout.

---

*Sources: `SECTOR_FLOW_US.json` asof 2026-07-24 close (re-aggregated by node, independently reproduced
in this file) · `module_fundamentals_us` UPS/NOC/GD/LHX/LMT/RTX (live pull 2026-07-27) ·
`module_disclosure_us` NOC/GD/DAL/UAL (90-day EDGAR, live 2026-07-27) · NOC 8-K Exhibit 99
(`noc-06302026xearningsrelea.htm`, filed 07-21) and GD 8-K Exhibit 99.1 (`gd-20260405exhibit991.htm`,
filed 04-29), fetched directly from EDGAR · `module_business_us` NOC/GD --json (10-K risk_summary_bullets
and business_customer text) · raw SEC XBRL `companyfacts` pull for UPS (`OperatingIncomeLoss` /
revenue, 19 annual + 6 quarterly points, live calc) · `scripts/us_flow.py UPS UNP CSX NSC` (FINRA
short-volume, 2026-07-24, D52/D73 band rule applied) · `module_news_data chain-hop "defense" "backlog"`
and `fts search` on "jet fuel"+"Delta", "Patriot"+"THAAD", "Lockheed"+"backlog", "RTX"+"backlog" (all
--scope foreign, live 2026-07-27) · DAL 8-K Exhibit (`deltaairlinesannouncesjune.htm`) and UAL 8-K
Exhibit (`ual_erx06302026xex991.htm`), fetched directly from EDGAR · `handoff/SCENARIOS.md` S20 /
S20-ANNEX (verbatim) · `handoff/STANDING_VIEW.md` M26/M34/M36/M91/R9 · this run's
`llm_outputs/2026-07-27/industry_US/` MACRO_REPORT (§ FINRA table, D52/D73, row 4 of the tilt table)
and EVENT_ALPHA (crack levels) · prior `llm_outputs/2026-07-24/industry_US/SECTOR_DEEP_INDU.md`
(rail/freight node — referenced for the chain map's unchanged elements, not repeated wholesale). No
guessed numbers; blanks left blank. Zero buy/sell, zero sizing.*
