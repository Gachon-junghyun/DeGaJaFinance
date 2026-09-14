# DEEP · ENRG — 2026-07-23 (Thu) ★US-only · **CONTINUOUS TRACK · REFINING NODE, CRUDE/CRACK/TANKER SPLIT**

> Stage 7 / L1·DEEP. `--market us`, news `--scope foreign`. Zero buy/sell, zero sizing (P4).
> Run clock — the US regular session was **not yet open at pull time (~09:1x ET)**. All equity closes
> below through 2026-07-22 are settled session closes; every 2026-07-23 print (crude, product, and
> equity) is an **intraday, incomplete bar** and is labeled as such everywhere it appears.
> **Prior deeps carried by reference, not re-printed:** `llm_outputs/2026-07-22/industry_US/SECTOR_DEEP_ENRG.md`
> (value-chain map, Bab el-Mandeb node, services node, the PSX/MPC/VLO 10-K placements, the full player
> list) and `llm_outputs/2026-07-21/US_2/SECTOR_DEEP_10.md` (§4 chain map, §2 player list).
> Crack series below is a **self-computed rebuild** (`yfinance CL=F/RB=F/HO=F`, one continuous pull,
> `(2·RB·42 + HO·42 − 3·CL)/3`) reproduced independently this run — it matches the 07-22 file's own
> printed levels for every date it also carries (69.45 / 69.41 / 69.33 / 68.23 / 30.27 gasoline-distillate
> gap on 07-21 all reproduce exactly), so it is treated as validated, not merely "internally consistent."

---

## §0 · DELTA since 07-22 — the lead

**Four things changed, and one of them corrects the registry's own framing of the mandate.**

**(1) 07-22's close, now in hand, BREAKS the detachment pattern — it does not extend it.** The mandate
frames today as "the 4th observation" in a continuous run. It is not continuous: on 07-22, VLO/MPC/PSX
**fell** (−1.23% / −1.23% / −0.41%) while crude rose +2.26% and the crack fell −2.0%. That is the crack
and the equities moving **together**, the opposite of the 07-17/07-20/07-21 detachment shape. **§2 works
this out in full — it is the single most important correction in this file.**

**(2) The composite crack's −11.2% intraday move today is not a diesel story — it is a gasoline-crack
collapse, and the diesel/distillate binding constraint named 07-22 is still intact.** Decomposed by
product (own calc, below): the gasoline-only crack fell **58.14 → 56.59 → 46.71** (07-21→07-22→07-23,
**−19.7% in two sessions**) while the distillate-only crack fell only **88.41 → 87.42 → 85.24** (**−3.6%**
over the same window) — the gap between them **widened**, 30.27 → 30.83 → **38.53**. The anti-signal
registered 07-22 ("gap < $15 → constraint released") has moved the wrong direction to fire; what actually
broke is the crude/gasoline spread, not the middle-distillate bottleneck.

**(3) The customer check (W4/D23) is closed for four of five names.** DAL, UAL, FDX all read this run for
the first time (previously flagged as gaps, not filled); LUV printed same-day (07-23) and is read fresh;
UPS remains pending (07-28). **§4 below.**

**(4) VLO's estimate-revision pattern has gone flat on the current quarter and re-accelerated on next
quarter, refreshed this run** (`module_fundamentals_us`, fresh pull): current-Q consensus EPS increment
is now **+1.98 → +0.49 → +0.07 → 0.00** (90d→60d→30d→7d→now) — the flattening the 07-22 file's rate-of-
change lens predicted has now reached zero. Next-quarter is the opposite: **+1.30 → +0.48 → +2.52 →
+1.36**, still accelerating. XOM's current-Q estimate is **being cut on both windows** (0↑/2↓ over 7d,
0↑/4↓ over 30d) — XOM remains the control the 07-22 file named it.

---

## §1 · The three legs, answered separately — each has its own KPI and its own answer

### (a) Crude / integrated (XOM, CVX, EOG, COP, OXY) — KPI = crude price

| | 07-22 close | 07-23 intraday | 1d Δ |
|---|---|---|---|
| WTI (CL=F) | 86.83 | **91.37** (mandate) / 91.50 (own pull) | **+5.2% / +5.4%** |
| XOM | 154.45 | 156.83 | +1.54% |
| CVX | 192.98 | 196.71 | +1.93% |
| COP | 118.79 | 121.50 | +2.28% |
| OXY | 57.50 | 58.50 | +1.74% |
| EOG | 144.00 | 146.43 | +1.69% |

**Verdict: CONFIRMS cleanly, no separation puzzle on this leg.** Crude equities moved with crude, in
the same direction and roughly proportionate magnitude (equities ~+1.5–2.3% against a ~+5% crude move,
i.e. sub-1.0 beta on the day, unsurprising for large-cap integrateds with downstream/chemicals exposure
diluting the upstream beta). **WTI COT is 10%ile of 1yr (Tuesday close), NatGas 6%ile** — cited as cushion
context only, per D6: it is not offered as a reason for anything, and the next print (Fri 07-24) is
S8's own registered cross-check, not this file's.

### (b) Refining margin (VLO, MPC, PSX) — KPI = the 3-2-1 crack

| Date | Crack321 | 1d Δ | WTI | 1d Δ | VLO | MPC | PSX |
|---|---|---|---|---|---|---|---|
| 07-16 | 69.45 | +1.98% | 78.95 | −0.82% | +2.60% | +2.23% | +2.63% |
| 07-17 | 69.41 | −0.06% | 82.49 | +4.48% | +3.13% | +2.21% | +2.75% |
| 07-20 | 69.33 | −0.12% | 83.23 | +0.90% | +1.18% | +0.87% | +0.94% |
| 07-21 | 68.23 | −1.59% | 84.91 | +2.02% | +0.48% | +1.41% | +1.66% |
| 07-22 | 66.86 | **−2.01%** | 86.83 | +2.26% | **−1.23%** | **−1.23%** | **−0.41%** |
| 07-23 (intraday) | **59.36** | **−11.2%** | 91.37 | **+5.2%** | +1.05%\* | +0.76%\* | +1.04%\* |

\*07-23 equity moves are same-session-incomplete, computed against 07-22 settled close on live quotes at
pull time — directionally usable, not a closing return.

**Verdict: the leg is real but its own margin engine is now moving in the OPPOSITE direction from crude
on 4 of the last 5 sessions, and the one session that moved WITH the crack (07-22, equities down) is the
one the mandate's framing skipped.** Crack321 is at the **98.0th percentile of 3 years** (own calc,
down from 99.9th on 07-17 and 99.6th on 07-21 — still historically rich, but the level has now given back
roughly 14.6% of its move from the 07-16 peak in five sessions, three-quarters of that in the
last, unconfirmed session alone). **L2 (peak-margin trap) restated with fresh numbers**: VLO's forward
multiple (9.4x FY26 cons., carried from 07-22, M23) sits on a margin whose own current-quarter
revision rate has gone to **zero this week** while its next-quarter revision rate is still
accelerating (+1.36 in the last 7 days) — consensus is still chasing the print for one quarter out, not
yet marking down the quarter that is closing. That is the honest, dated state of the trap, not a verdict.

### (c) Tankers / shipping (FRO, STNG, INSW, DHT, TNK) — KPI = tonne-miles

| Name | 07-22 close | 07-23 intraday | 1d own | RS20 vs SPY | RS60 vs SPY |
|---|---|---|---|---|---|
| FRO | 37.96 | 38.77 | +2.13% | −6.5 | +3.3 |
| STNG | 78.46 | 79.32 | +1.09% | −0.7 | −5.0 |
| INSW | 88.91 | 90.47 | +1.76% | +1.7 | +8.2 |
| DHT | 18.13 | 18.47 | +1.88% | −5.9 | −3.0 |
| TNK | 74.78 | 75.78 | +1.34% | −2.2 | −6.5 |

**Verdict: INDISTINGUISHABLE — cannot be resolved with tools available this run.** Every name in the
basket is up on today's intraday tape (+1.1% to +2.1%, consistent with the crude/war-headline pop), but
the A-grade RS20/RS60 signal (per D6, RS carries; OBV/vol_surge here is C-grade and additionally flagged
D31-contaminated by the incomplete bar) is **negative-to-mixed on the 20/60-day window for 4 of 5 names**
— the basket has been a laggard over the past month despite an acute blockade/attack headline sequence.
One up-session after a named-ship attack does not overturn a 20/60-day laggard reading; it is also not
proof the laggard reading is right going forward. **The KPI itself — tonne-miles, or a freight-rate/
Baltic-type index — is not measured by any tool in this repo** (see §8, "what I could not measure").
This leg cannot be answered past "the news is loud, the flow says laggard, the actual KPI is absent."

---

## §2 · C4 counter — is today observation 4 or 5? **Neither. The honest count is: 3 confirmed, 1 broken, 1 unconfirmed.**

`handoff/STANDING_VIEW.md` §6 C4 registers the counter at **3** (07-17, 07-20, 07-21 — crack down, crude
up, all three refiners up every session) and states the rule: at 5 consecutive, the equity is priced off
something other than its KPI. The mandate's own framing implicitly treats 07-22 and today as
observations #4 and #5 in that same streak. **Measured against the actual 07-22 close, that framing does
not hold:**

| Date | Crack | Crude | VLO/MPC/PSX | Pattern match? |
|---|---|---|---|---|
| 07-17 | ↓ | ↑ | ↑ / ↑ / ↑ | **Obs #1 — detachment** |
| 07-20 | ↓ | ↑ | ↑ / ↑ / ↑ | **Obs #2 — detachment** |
| 07-21 | ↓ | ↑ | ↑ / ↑ / ↑ | **Obs #3 — detachment** |
| **07-22** | ↓ | ↑ | **↓ / ↓ / ↓** | **BREAKS the pattern — refiners tracked the falling crack DOWN, the opposite of detachment** |
| 07-23 (intraday) | ↓↓ (−11.2%) | ↑ (+5.2%) | ↑ / ↑ / ↑ | Pattern-consistent **if it holds to close** — currently an incomplete bar, not a session close |

**On 07-22, the equities did the thing the margin thesis predicts they should do when the margin falls —
they fell with it.** That is evidence *for* the margin-not-premium reading on that specific day, not a
4th detachment observation. The mandate's "4th observation" framing appears to have been written from
the crude/crack levels alone without checking whether the equities actually detached that day; they did
not. **Today's tape, if it holds through the 16:00 ET close, would be a legitimate 4th detachment
observation** (crack down hard, crude up, refiners up) — but per the binding rule on incomplete bars,
an intraday print with the session still open cannot be counted as a closed observation. **Correction
recommended for the registry: the counter should read "3 confirmed, 1 broken (07-22), 1 pending
confirmation (07-23 close)" rather than advancing to 4 or 5 on the current framing.** Per C4 itself, this
is exactly the "indistinguishable, not rejected" case the rule was written for — the sample is not just
small, it is now internally inconsistent, and that inconsistency is the finding.

---

## §3 · Mandate 2 — the customers (W4/D23), closed for four of five

**All four airlines/logistics names that have printed inside the war window were pulled and read this
run** (fuel-cost figures below are from primary earnings releases/calls, quoted like-for-like YoY per C2):

| Customer | Print date | Fuel-cost line (YoY, Q2 unless noted) | Guide action | Read |
|---|---|---|---|---|
| **DAL** | 07-10 | Fuel cost **+$1,913M** YoY; op. income **−$501M** YoY (adj.) | Maintained FY26 EPS $6.50–7.50; passing ~60% of extra fuel cost to fares | Absorbing, not cutting guide |
| **UAL** | 07-16 | Fuel cost **+$2,335M** YoY (**+84%** to $2.3B); all-in fuel ~**$3.69/gal** guided Q3 | **Q3 EPS guide $2.50–3.50 vs. $3.60 cons. — a guide-down/miss vs. Street**; FY26 low end raised to $9 (from $7), high end held at $11; **~$6B** total 2026 fuel-cost headwind vs. original budget | Explicitly cites "jet fuel crack spreads soaring" as the driver |
| **FDX** | 06-24 (FY26 Q4, period ended 05-31) | Fuel cost **$864M → $1.43B, +66%** YoY | Beat EPS ($6.31 adj. vs. $5.96 cons.) and revenue; FY27 guide $16.90–18.10 issued | Absorbed; management said no demand impact from fuel |
| **LUV** | 07-23 (today, same-day) | Fuel bill **+67%** YoY to **$2.22B** | **Q3 EPS guide $0.50–0.75 vs. $0.82 cons. — a miss**; **FY26 guide cut to $3.25–4.25** (cons. $3.23), down from a higher prior range (exact prior figure not retrieved this pull — source truncated) | Second airline this window to cut guide on fuel |
| **UPS** | **07-28 — pending** | — | — | Not yet printed |

**Read-through, stated once and precisely (this closes the cheapest open omission on the dig list):**
all four printed names show fuel cost as a **dollar-quantified, disclosed, rising expense line** (+66%
to +84% YoY across the four), and **two of four (UAL, LUV) explicitly cut or missed near-term guidance
citing fuel/jet-fuel-crack costs specifically**, while two (DAL, FDX) absorbed the hit and maintained or
beat. This is an independent, customer-side confirmation that **the crack level itself — whatever its
cause — is transmitting into real fuel-buyer P&Ls in dollar terms.** It does not resolve the C4
margin-vs-premium question (that is a refiner-supply-side question; the customer side only proves the
crack is real cash flowing somewhere), but it does directly confirm the refining-margin story is not a
paper number: someone downstream is visibly paying for it, on the record, this quarter.

---

## §4 · Value chain — carried by reference; only what changed

Full chain map, Bab el-Mandeb/Hormuz node, services node, midstream, integrated node, and the VLO
Benicia idle / St. Charles FCC disclosure: **unchanged, see the two prior files cited in the header.**
**One update, product-level, feeds directly from §0(2):** the binding constraint named 07-22 — middle-
distillate conversion capacity in the Atlantic basin — is **still intact and, if anything, strengthening
relative to gasoline**: the distillate crack alone fell only 3.6% over two sessions while the gasoline
crack fell 19.7%. **The composite 3-2-1's plunge is a gasoline/crude-spread story, not evidence the
diesel bottleneck released.** Nothing else in the chain map changed this run (no new 10-K/8-K items
found for VLO/MPC/PSX in a same-day disclosure check).

---

## §5 · Chain-hop candidates — **ZERO promoted, sixth consecutive run**

`chain-hop refinery crack --days 14 --scope foreign` (631 articles) and `chain-hop tanker Hormuz Bab
Mandeb --days 14 --scope foreign` (1,500 articles), each candidate flow-cross-checked before it may
reach BET (co-mention alone is not a candidate, per rule):

| Candidate | Proximity / body | Flow check | Verdict |
|---|---|---|---|
| **STX** (Seagate) | 4/17, near *"Weekly Vessel Valuations Report"* | 🟡중립, RS20 −7.9 / RS60 **+51.6** vs SPY | **FAIL — no mechanism.** HDD/storage company; the "vessel" co-mention is lexical, not thematic. Large RS60 is real but unrelated to shipping. |
| **CME** | 27/64, *"Gold falls as Middle East tensions lift Oil prices"* | Carried 07-22 fail (🔴분산, RS60 −22.5) | **FAIL** — a macro-derivatives-volume story, no refining/tanker exposure |
| **KKR** | 3/4 | Carried 07-22 fail | **FAIL** |
| **AMP** | 3/3, *"Bonds unsettled as oil and gas climb"* | Carried 07-22 fail — macro co-mention, no chain position | **FAIL on mechanism** |
| **V, MSFT, ABT, JNJ, BAC, WMT, STT, SNDK, BA, USB, WMB, HUM** | 2–12 body hits each | Not individually flow-checked — every headline example returned is an unrelated AI-earnings/tech-rotation/bank story (Zelle lawsuit, TSMC pricing, Blackstone quarterly, submarine-production summit) co-occurring in the same news cycle as the oil headline, not a chain mechanism | **FAIL — lexical false positives, dismissed on inspection without individual flow pulls** |
| **WMB, VLO, PSX** | 2 each | Already-named nodes (WMB midstream, VLO/PSX refiners) | Not hops — the named node reappearing |
| **META** | 8/217 (*"Africa's Richest Man Proposes To Build 700,000 Bpd Oil Refinery In Kenya"*) | — | **FAIL — lexical false positive** (unrelated Kenya refinery story, no US-listed mechanism) |

No genuine hop survives. This is the sixth consecutive run at zero.

---

## §6 · Track KPIs + anti-signals — dated observables

1. **3-2-1 crack (own calc).** 59.36 intraday 07-23 (98.0%ile/3y), from 68.23 (07-21, 99.6%ile) via 66.86
   (07-22, 99.2%ile). **Anti-signal**: two consecutive *weekly means* below 60.00. Current week-to-date
   mean (07-20/21/22/23, 4 of 5 sessions) is **65.95**, down from last full week's 67.65 — **the first
   negative weekly Δ in the entire series** (prior deltas were +1.99/+2.20/+6.42/+4.21/+2.08/+5.71, all
   positive). One negative reading is not the anti-signal (which needs two consecutive); it is the first
   time the rate has gone negative at all. Next full week closes 07-24.
2. **Gasoline-crack vs distillate-crack gap.** Widened 30.27 → 30.83 → **38.53** (07-21→07-22→07-23
   intraday) — moving away from, not toward, the $15 anti-signal threshold. **Correction to how this KPI
   should be read**: a narrowing gap would mean the diesel constraint released; a widening gap driven by
   gasoline collapsing, as measured here, means the opposite leg is compressing. This KPI needs to be
   read as two separate series (gasoline crack, distillate crack) going forward, not one gap number.
3. **Detachment counter (C4).** Corrected this run to **3 confirmed / 1 broken (07-22) / 1 pending
   (07-23 close)** — see §2. Next reading: 07-23 16:00 ET close.
4. **WTI COT %ile.** 10%ile (Tue close), NatGas 6%ile — next print **Fri 2026-07-24** (S8's frozen
   cross-check, cushion context only per D6, never a standalone reason).
5. **Estimate second derivative, refreshed this run** (`module_fundamentals_us`, fresh pull). VLO
   current-Q increment 90d→now: **+1.98 → +0.49 → +0.07 → 0.00** — flattened to zero this week. VLO
   next-Q increment: **+1.30 → +0.48 → +2.52 → +1.36** — still accelerating. XOM current-Q: **0↑/2↓ (7d),
   0↑/4↓ (30d)** — unanimous cuts, XOM remains the control per §0(4).
6. **Prints**: VLO 07-30 · XOM 07-31 · MPC 08-04 · PSX 08-05 (unchanged, carried).
7. **XOM as the control.** +1.54% today, cumulative +7.45% (07-16→07-23 intraday) on crude beta alone,
   while its own current-quarter estimates are being cut on both the 7-day and 30-day windows. If XOM's
   revisions turn up while the crack keeps falling, the whole board's move was crude, not margin.
8. **Customer fuel-cost line (new this run, W4).** DAL/UAL/FDX all closed this run (§3); **UPS 07-28**
   is the one customer print still outstanding and is now the single cleanest remaining observable on
   this axis.

---

## §7 · Dispersion (W5)

Using this run's own supplied `SECTOR_FLOW_US.json` (asof 07-22 close) subset: **RS60 vs SPY spans
MPC +36.2 to SLB −19.8, a 56.0pp range**, with COP −7.1, XOM −1.0, CVX −0.5, WMB −2.3, KMI −2.3, OXY −4.0
scattered in between. **The three-name refining node (VLO/MPC/PSX) and the crude/integrated names (XOM/
CVX/COP/OXY) sit on opposite sides of this range while carrying the same "Energy" sector label** — the
node driving the RS spread and the node absorbing crude-price beta directly are not the same trade, and
the sector aggregate (wflow +0.283, eqflow +0.118, breadth 0.06 asof 07-22) is a blend of two structurally
different KPIs (crack vs. crude price) plus a third (tonne-miles) that is not observable in this universe
at all. **"Energy" remains the wrong unit of analysis** — the three legs answered separately in §1 is
the level at which this sector actually resolves.

---

## §8 · What I could not measure

- **Tonne-miles / a tanker freight-rate index (e.g., Baltic Dirty Tanker Index or WS rate).** No module
  in this repo prices tanker freight directly; the tanker leg (§1c) is answered on RS/price proxy only,
  and is stated as indistinguishable rather than resolved because of this gap.
- **EIA weekly distillate/crude inventory prints for 07-22 and 07-29.** Not pulled this run (no EIA
  module wired into this toolset); the 07-22 file's KPI #3 is carried unchanged rather than refreshed.
- **LUV's prior FY26 EPS guide figure** (the number the $3.25–4.25 cut is measured against) — the source
  article body truncated at retrieval; only the new range and consensus ($3.23) were captured.
- **HD현대 / independent-refiner tier (PBF, DINO, CVI, DK, PARR) / MPLX/ET/LNG** — confirmed absent from
  `us_top300`, carried by reference from 07-22; not re-verified this run.
- **A Singapore/Dubai (or equivalent non-US-Gulf) refining margin cross-check** — this file, like the
  KR desk's own SECTOR_DEEP_ENRG, has only ever measured the US Gulf Coast NYMEX proxy; no tool here
  prices any other refining complex.
