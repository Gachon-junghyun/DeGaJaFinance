# DEEP · ENRG — 2026-07-21 (Tue) ★US-only · **CONTINUOUS TRACK**

> Stage 6 / L1·DEEP. Runtime `--market us`, `--scope foreign` on every news call. Zero buy/sell
> calls, zero sizing (BET owns sizing).
> **Inputs reread from disk (not memory):** `MACRO_REPORT.md` (§1, §4 row 1, P3/P3′) ·
> `SWEEP_READ.md` (§1 row 2, §3 CYCLE EXPOSURE GAP) · `EVENT_ALPHA.md` (Card 1) ·
> `SECTOR_ROTATION.md` (§2g) · `BLINDSPOT_PREMORTEM.md` (Lens 3 re-tags, Lens 4 Energy hole, B1) ·
> `data/cycles/cycle_registry.json`.
> **PRIOR DEEP (continuous-track anchor): `llm_outputs/2026-07-19/industry_US/SECTOR_DEEP_ENRG.md`.**
> Per the continuous-track rule this file **leads with the delta** and carries unchanged structure
> **by reference** — the value-chain map, the PSX/CVI/MPC/VLO 10-K work, the tanker-hop kill — are
> not re-printed; §4 and §5 state exactly what is carried and what changed.
> **asof: 2026-07-20 close** (tape, flow, FINRA) for everything measured today; the crack-spread
> series below is self-computed (`yfinance CL=F/HO=F`) independently of any upstream file's pull.

---

## §0 DELTA since 2026-07-19 — lead

### ★★ D1 — The prior file's own falsifier fired: **detachment DAY 2, self-computed, not asserted**
The 07-19 file set an explicit trigger (KPI 3): *"2 consecutive sessions where the crack falls and
PBF/VLO still rise → Day 2 = the equity has decoupled from its KPI → treat as narrative-priced."*
It logged 07-17 as Day 1. **I recomputed the crack independently today** (`yfinance CL=F`/`HO=F`,
distillate crack = `HO=F×42 − CL=F`, one continuous pull so the series is internally consistent):

| Date | CL=F | HO=F | **Crack $/bbl** | Δcrack | VLO | PBF | MPC | PSX |
|---|---|---|---|---|---|---|---|---|
| 07-16 | 78.95 | 4.031 | **90.34 ← the top** | — | +2.60% | +3.71% | +2.23% | +2.63% |
| 07-17 | 82.49 | 4.065 | **88.22** | **−2.12** | **+3.13%** | **+2.97%** | +2.21% | +2.75% |
| 07-20 | 82.27 | 3.990 | **85.31** | **−2.91** | **+1.18%** | **+1.75%** | +0.87% | +0.94% |

**Two consecutive sessions, crack down both times, all four refiners up both times. Day 2 fired.**
⚠ **Data-vintage caution, stated rather than hidden:** my 07-17 crack level (88.22) does not match
the 07-19 file's own 07-17 print (83.57, from a different `CL=F` pull, 81.78 vs my 82.49). The
**absolute level is not reproducible to the cent across runs** — continuous-futures closes drift
with pull time. **The direction is robust across both independently-pulled series** (down 07-16→17,
down again 07-17→20), which is the only thing the trigger depends on.

### ★★ D2 — This is a DIFFERENT claim than the one MACRO/EVENT_ALPHA made, and the two were conflated
MACRO §1 and EVENT_ALPHA framed 07-20 as *"VLO rose +1.18% on the day crude fell −0.35% — the
decoupling test passed."* **True, but it answers a different question than D1.** On 07-20, product
fell MORE than crude (`HO=F` **−1.83%** vs `CL=F` **−0.27%**, both from my own pull) — **the crack
compressed, it did not hold.** VLO did not decouple from crude broadly; **it decoupled from its own
margin KPI**, which is the narrower and more dangerous claim, and it is the one the 07-19 file's own
falsifier was built to catch. **"Refiners are anti-fragile to a crude selloff" and "refiners are
rising while their own margin shrinks" are not the same sentence — this run separates them.**

### ★★ D3 — The registry's locked `core_pick: PSX` rationale reverses sign, verified independently (★ Q2 below)
`scripts/us_flow.py PSX VLO MPC XOM CVX` (07-20 session): **PSX FINRA short-vol z = +2.01
("극단" = extreme surge)**, base20 39.1%, actual short% 57.0%. The registry's `core_pick_why` cites
**z −1.43 ("shorts actively exiting"), human-locked 2026-07-17.** The sign has flipped. Full
treatment in §6 Q2 — flagged, not overridden.

### D4 — New independent chokepoint, now quantified: **Bab el-Mandeb, not Hormuz**
*"Houthis block Saudi Arabia from transiting Bab el-Mandeb Strait"* [UPI 07-20] ·
*"Fresh threat to global oil supply: Saudi Arabia's crude exports at risk"* [TOI]. Thread REIGNITED
4→8 outlets. **Mechanism-independent of a Hormuz ceasefire — a Hormuz deal does not reopen Bab
el-Mandeb — but not price-independent** (a broad crude selloff still knocks it, per MACRO's own
concession). Node placement: crude *logistics* (node 2), a second binary alongside Hormuz, not a
new node.

### D5 — The Russia mechanism is now quantified with a real number, not a strike count
07-19 tracked strike *frequency* (3 in 7 days). This run's fts turns up the **stock, sourced**:
*"at least 24 of Russia's 34 largest refineries"* damaged [nasdaq 07-20]; *"drone strikes have
disabled over **40% of Russia's refining capacity**"* [hellenicshipping 07-19]. **The mechanism did
not decelerate — no new single-strike headline in the last 4 days, but the cumulative damage stat
is now precise where it was a strike-count proxy before.**

### D6 — TACO trigger: still live, still undated-but-concrete, still rejected
10-day ceasefire proposal (07-20), rejected so far — *"US attacks Iran for tenth consecutive
night"* [aljazeera 07-21], no outlet has declared the diplomatic track dead as of the 07-21 pool
(14 articles, too thin to read). `ceasefire` 239→ hits/7d (MACRO), `Houthi` 144–151 hits/7d
(MACRO/PREMORTEM re-verify). Carried, not re-derived — the mechanics were already fully worked in
the 07-19 file and by PREMORTEM Bracket B1 this run.

### D7 — CYCLE_EXPOSURE gap: **unchanged, −8.00pp, now a 3rd/4th consecutive flag**
`data/cycles/cycle_registry.json` epicenter for "Energy / oil-refining (Hormuz + Russia crack)" is
still `["MPC","PSX","VLO","XOM","CVX","EOG","FRO","STNG","INSW","DHT"]` — **the 07-19 DEEP's
recommended correction (drop the four dead tankers, add DINO/PBF/DK/PARR/CVI, relabel XOM/CVX/EOG
as `counter_sign`) was not applied to the file.** Book holds 0.0% epicenter, only KMI/LNG adjacent.
Full treatment in §6 Q1.

### D8 — Small-cap refiners kept accelerating; CVI's short base inverted hard against PSX's
PBF RS20 **+65.8%→+71.8%**, DK **+49.1%→+56.5%**, PARR **+49.6%→+53.0%**, DINO **+34.1%→+40.8%**
(still the sole 🟢가속 tag). **CVI's short-vol z moved the OPPOSITE direction from PSX's**:
**+0.49 (07-17) → −2.20 (07-20, "급감" = sharp short-cover)** — the exact inverse of PSX's
+2.01. Two refiners, two opposite positioning signals, same week.

### M&A on the tape, logged not promoted
*"Magnolia Oil & Gas to Acquire WildFire Energy for $4.06 Billion"* [yahoo/nasdaq/SA 07-20] —
Eagle Ford E&P consolidation, **node 1 (crude supply), not the refining engine.** No exposure hop;
logged for completeness only.

### What is CARRIED UNCHANGED BY REFERENCE (not re-derived, not re-printed)
1. **The value-chain node map and bottleneck = conversion capacity, not crude, not demand** —
   07-17/07-19 §4. Re-affirmed below with D5's updated damage stat; not re-derived from scratch.
2. **PSX / CVI / MPC / VLO 10-K primary-source work** — five PSX segments + the LA refinery idling
   (the only non-war bottleneck source in the file), CVI's three segments + Wynnewood RDU reversion +
   70% Icahn control, MPC's Item 1A risk factor — 07-17/07-19 §3. Unchanged; today's
   `module_disclosure_us` re-check (below) confirms no new order/contract 8-K superseding it.
3. **The tanker one-hop is dead** — killed twice independently (07-17 price pull, EVENT_ALPHA Card 2
   STORY-ONLY). Not revisited.
4. **The "war hedge" retail-marketing tell** — *"Five Oil and Gas Stocks Ready for a Hormuz Spike"*
   [CNBC/yahoo, 07-15/07-16/07-17] recurs again this run (§5 chain-hop, below) — carried as evidence
   of the same late-cycle marketing signature, not re-argued.

---

## §1 Flow — measured today, by node

`module_flow --bench SPY` + `scripts/us_flow.py` (FINRA Reg SHO, 07-20 session).

### Upstream / integrated (counter-sign to the crack)
| Ticker | OBV | RS20 | RS60 | vol surge | short z / 5v5 |
|---|---|---|---|---|---|
| XOM | 매집 | +8.3% | −5.1% | 0.83× | −0.77 / +2.2▲ |
| CVX | 중립 | +9.9% | −2.5% | 0.73× | +0.46 / +3.1▲ |
| OXY | 중립 | +7.1% | −7.6% | 0.80× | — |
| COP | 중립 | +8.0% | −10.0% | 0.82× | — |
| EOG | 중립 | +9.2% | +1.7% | 0.82× | — |

### Refining — majors (the run's epicenter, most crowded)
| Ticker | OBV | RS20 | RS60 | vol surge | short z / 5v5 | **Δz vs 07-17** |
|---|---|---|---|---|---|---|
| **VLO** | 매집 | **+33.2%** | +29.3% | 1.06× | +0.31 / −5.7▼ | −0.63→+0.31 |
| **MPC** | 매집 | +30.4% | +37.6% | 0.86× ⚠ | −0.94 / +2.4▲ | +0.18→−0.94 |
| **PSX** | 매집 | +26.3% | +25.6% | 0.96× | **+2.01 "극단" / −8.7▼** | **−0.98→+2.01 ★★** |

### Refining — independents (the actual price action; invisible to `us_top300` tooling)
| Ticker | OBV | RS20 | RS60 | vol surge | short z / 5v5 | Note |
|---|---|---|---|---|---|---|
| **DINO** | 매집 | **+40.8%** | +47.7% | **1.29×** | +1.26 / +8.2▲ | ★ sole 🟢가속 tag |
| **PBF** | 매집 | **+71.8% ← largest** | +53.5% | 1.11× | −0.54 / −4.3▼ | |
| **DK** | 매집 | +56.5% | +59.6% | 1.08× | −0.87 / −4.2▼ | |
| **PARR** | 매집 | +53.0% | +14.8% | 0.91× | +0.44 / +1.1▲ | |
| **CVI** | 중립 | +27.1% | +6.4% | 0.91× | **−2.20 "급감" / −5.0▼** | ★ short base inverted vs PSX |

### Services (cross-cutting, not part of the thesis)
| Ticker | OBV | RS20 | RS60 | vol surge |
|---|---|---|---|---|
| SLB | 🔴분산 | −2.9% | −19.0% | 0.66× |
| HAL | 분산 | +1.1% | −14.6% | 0.82× |

### Node 5 — the crack's counterparty
| Ticker | OBV | RS20 | RS60 | vol surge |
|---|---|---|---|---|
| DAL | 매집 | +1.1% | +19.2% | 0.80× |
| UAL | 중립 | −0.1% | +23.8% | 0.99× |
| LUV | 중립 | +1.4% | +18.5% | 0.78× |

**Read:** RS20 momentum decelerated across the board today (VLO +28.8→+33.2 last run, day-over-day
gain smaller than the 07-17→07-19 gain) while short-vol z **diverged violently within the group** —
PSX +2.01 (shorts piling in relative to its own base), CVI −2.20 (shorts fleeing). ⚠ **Volume surge
is still <1.1× everywhere in the majors** (VLO 1.06×, MPC 0.86×, PSX 0.96×) — the RS gains are
**not** being confirmed by fresh incremental volume; the independents (DINO 1.29×, PBF 1.11×, DK
1.08×) are the only names with real volume behind the move. DAL's RS20 decelerated sharply (+14.3%
RS60 last run → +1.1% RS20 now, though RS60 is still +19.2%) — the counterparty side cooled too.

---

## §2 Players — large-cap universe UNION thematic small-caps
Bar: named ≥2× in the sector news window **AND** a real ticker **AND** mcap ≥ ~$2B. mcap/fwd PE
carried from the 07-19 read (not re-pulled today — these move slowly relative to flow/short data,
which ARE re-pulled today and marked as such).

| Ticker | Name | Node | mcap (07-19 read) | Today's delta |
|---|---|---|---|---|
| **VLO** | Valero | Refining major | $91.9B | RS20 28.8→**33.2%**; vol still <1.1× |
| **MPC** | Marathon Petroleum | Refining + MPLX midstream | $91.3B | RS20 27.5→**30.4%**; z flipped +0.18→**−0.94** |
| **PSX** | Phillips 66 | 5 segments; registry `core_pick` | $82.9B | ★★ z −0.98→**+2.01** — Q2 |
| **DINO** | HF Sinclair | Refining + lubricants | $16.0B | RS20 34.1→**40.8%**; still sole 🟢가속 |
| **PBF** | PBF Energy | Pure-play refiner | $7.4B | RS20 65.8→**71.8%**, the run's largest mover |
| **DK** | Delek US | Small independent refiner | $3.9B | RS20 49.1→**56.5%** |
| **PARR** | Par Pacific | Hawaii/Rockies refiner | $3.8B | RS20 49.6→**53.0%** |
| **CVI** | CVR Energy | Refining + N-fertilizer | $3.5B | ★ z +0.49→**−2.20**, inverse of PSX |
| XOM / CVX | Integrateds | Crude monetizers, counter-sign | $610.8B / $373.2B | RS20 +4.4→**8.3%** / +5.2→**9.9%** |
| **DAL** | Delta Air Lines | Node-5 counterparty | $55.4B | RS20 decelerated to +1.1% (was RS60 +14.3%) |
| **MGY** | Magnolia Oil & Gas | ★ new — E&P/node-1, M&A acquirer | not verified today | Named 5× (M&A, 07-20); logged, not chain-hopped — Eagle Ford, not refining |
| KMI / LNG | Midstream / LNG export | Zero crack participation | — | Held book position; unchanged |

⚠ **Tool-floor finding, carried for the fourth consecutive run:** `chain-hop`'s universe is
`us_top300`; PBF/DK/PARR/CVI/MGY are structurally invisible to it. The bounded union above remains
the only mechanism in this pipeline that sees them.

---

## §3 IR anchor — primary sources (re-check, not re-derivation)

**PSX / CVI / MPC / VLO 10-K work is carried by reference from 07-17/07-19 §3** — the 5-segment PSX
breakdown, the LA refinery idling, CVI's Wynnewood RDU reversion and 70% Icahn control, VLO's "no
midstream buffer" structure, MPC's Item 1A language naming competitor closures as a margin driver.
Not re-pulled; nothing in today's filings contradicts it.

**`module_disclosure_us` re-run today (VLO, PSX) — result: still no order/contract/M&A 8-K in
either name in 90 days.** One new item since 07-17: **VLO filed an Item 7.01 (Reg FD) 8-K on
2026-07-16**, referencing a **February 25, 2026 board action** — generic disclosure housekeeping,
not a new catalyst; the filing itself gives no operative detail beyond the reference date. VLO also
carries one Item 5.02 (management change, 2026-05-08) inside the 90-day window, unremarked. **No
filing-level catalyst exists for the epicenter names in window; the only dated catalysts remain
earnings** (VLO/PBF/CVI 07-30 · MPC 08-04 · PSX/PARR/DK 08-05 — carried from 07-19 D7, unchanged).

---

## §4 Value-chain node map — carried by reference, node 2 updated

*(Full 6-node map is 07-19 §4; not re-printed. The only structural change is node 2, which now
carries two independent chokepoint binaries instead of one.)*

```
[1 CRUDE SUPPLY]     [2 ★ CRUDE LOGISTICS —    [3 ★★ CONVERSION       [4 PRODUCT LOGISTICS]  [5 END-USE /              [6 CO-PRODUCT
 not scarce           TWO chokepoints now]     CAPACITY —              export levies,          COUNTERPARTY              SPILLOVERS]
 XOM CVX EOG COP       Hormuz (undated,        the BOTTLENECK,         mostly unlisted         pays the crack
 OXY + MGY/WildFire    10-day ceasefire        unchanged                                        DAL UAL LUV (jet)        CVI→UAN/ammonia
 (new E&P M&A)         proposal, rejected)     VLO MPC PSX DINO                                  FDX UPS (diesel)         PSX→50% CPChem
 ⚠ COUNTER-SIGN        + Bab el-Mandeb          PBF DK PARR CVI                                  ⚠ COUNTER-SIGN            → petchem
 to the crack          (Houthi, NEW, 07-20,    24 of 34 largest                                  to the crack
                        independent of          Russian refineries
                        Hormuz mechanism,        damaged / 40% of
                        NOT of price)            capacity disabled
        [ SERVICES layer, cross-cutting: SLB 분산 RS60 −19.0% · HAL 분산 −14.6% — worst node, not part of the thesis ]
```

**Bottleneck re-affirmed, not re-derived:** conversion capacity (node 3) is still the binding
constraint — crude is not scarce (XOM/CVX/COP/EOG all only mid-single-digit RS20, none accelerating),
demand is paying rather than constraining (DAL/UAL/LUV still RS60 +18–24%, absorbing the cost), and
the mechanism damage is now precisely sourced (D5: 24/34 refineries, 40% of Russian capacity).
**Node 2's new second chokepoint (Bab el-Mandeb) feeds crude that never reaches node 3 at all — a
different failure mode than node 3's own capacity loss, but the same directional pressure on the
crack.** Cross-sector chains (node 3→5 airlines/freight; CVI→ag inputs; PSX→CPChem petchem) carried
unchanged from 07-19.

---

## §5 Chain-hop candidates — again ZERO promoted, fourth consecutive run

`module_news_data chain-hop "refining margin" "crack spread" "diesel" --days 14 --scope foreign`
(173 articles scanned):

- HEADLINE-NAMED (excluded by rule): GOOGL, GOOG, META, XOM, TSLA, AMZN, CVX, MSFT, COP, ORCL, UPS,
  FDX, MPC, F, MMM, PSX — the mega-cap contamination the run has flagged before, still present.
- **★ CHAIN-HOP candidates (title 0× + ≥2 body co-mentions): MS (Morgan Stanley, 4 prox / 10 body),
  VLO (2 prox / 2 body).**

| Candidate | Why proposed | Flow cross-check | **Verdict** |
|---|---|---|---|
| **MS** | Body-proximate to a diesel-inventory story (*"Europe Faces Diesel Crunch as Inventories Head Toward Multi-Year Lows"*) | **🔴분산, RS20 −4.9%, vol 1.37×** — distributing on a volume surge, the worst possible combination | ❌ **REJECTED on flow.** Also a relevance rejection: MS is quoted as a *strategist*, not a chain participant — an analyst-commentary proximity artifact, the same failure class as 07-17's "Newmarket = horse race" find |
| **VLO** | Body-proximate | Already an epicenter name, already headline-named elsewhere in the pool | ❌ **Not a candidate by construction** — a name already at the center of the thesis cannot be a "hop." The example article (*"Five Oil and Gas Stocks Ready for a Hormuz Spike"*) is the same retail-marketing headline pattern flagged 07-15/07-16/07-17 (carried §0 item 4) — its recurrence is itself evidence for the late-cycle-instrument read, not a new lead |

**Honest result: zero promoted chain-hop candidates, fourth consecutive run.** The adjacency for this
cycle continues to read as genuinely empty at `us_top300` scale — a finding (the crack is a spread,
not a supply chain), not a search failure.

---

## §6 ★★ ANSWERS TO THE TWO MANDATED QUESTIONS

### ★ Q1 — The −8.00pp epicenter hole: cleanest expressions, kept separate from timing

**The gap, restated from `cycle_exposure.py` (unchanged from prior runs):** rank-2 cycle, epicenter
exposure **0.0%**, required **8.0%**, margin **−8.00pp**. Book holds only KMI/LNG (adjacent/fuel —
beta to the consequence, none to the engine). Three consecutive DEEP runs have called refining the
desk's #1-conviction lane; the registry's own recommended fix from 07-19 (drop FRO/STNG/INSW/DHT,
add the independents, relabel XOM/CVX/EOG `counter_sign`) was never applied to the file.

**Cleanest epicenter expressions, by what was measured TODAY, ranked by cleanliness of signal:**

1. **XOM** — un-crowded layer, not headline-named anywhere in this run's chain-hop or card work.
   OBV 매집, RS20 +8.3%, vol 0.83×, short z **−0.77** (no crowding at all). Benefits from a
   Saudi-export-substitution mechanism during a Bab el-Mandeb disruption, independent of Hormuz.
   Two independent stages (EVENT_ALPHA Card 1, PREMORTEM Lens 4) converged on this name
   independently of each other and of this file.
2. **DINO** — the only name in the whole complex still carrying an active-ignition (🟢가속) tag,
   with real volume behind it (1.29×, vs <1.1× in all three majors). The cleanest *momentum* signal,
   distinct from XOM's cleanest *crowding* signal.
3. **VLO** — strongest RS (+33.2%) and the name most directly tied to the mechanism narrative, but
   also the most run and the most retail-marketed (§5); vol 1.06× is not confirming fresh buying.
4. **MPC** — RS20 +30.4%, short base covering (z −0.94), but the most technically extended of the
   majors (RSI 86.4 per PREMORTEM Lens 3) on the thinnest volume (0.86×).
5. **PSX** — the registry's locked pick; excluded from this ranking's "clean" tier because its own
   short-positioning signal reversed sign today (Q2, below). Its non-crack-segment argument (4 of 5
   segments) is unaffected by that reversal and is not disqualified — the flag is narrower than that.

**Timing — kept strictly separate from the name question, per the brief:** the add/no-add decision
is gated by the **live 10-day Iran ceasefire proposal** (undated resolution, rejected so far, but a
concrete document for the first time) **and, independently, by D1's detachment-day-2 finding**
(crack down two consecutive sessions while every refiner rose both times — a specific, dated,
narrative-priced signal that argues for waiting on a KPI re-test rather than chasing the extended
tape). Both gates argue the same direction — caution on entry timing — without changing which name
is cleanest. **No size is recommended here or anywhere in this file.**

### ★★ Q2 — The registry's `core_pick: PSX`: the locked rationale is stale, verified independently

**The registry text** (`data/cycles/cycle_registry.json`, human-locked 2026-07-17):
> *"cheapest large refiner on forward (11.2, PEG 1.17) + **the only Energy name with shorts actively
> exiting (FINRA short-vol z −1.43, 5v5 −16.6▼)** = clean structural entry, not an extended one."*

**Verification run today, independently of the registry text or any upstream file's claim:**
`python -X utf8 scripts/us_flow.py PSX VLO MPC XOM CVX` (07-20 session, FINRA Reg SHO):

```
PSX   57.0%   base20 39.1%   z  +2.01   5v5 -8.7▼   2026-07-20   🔴 공매도급증(자기베이스대비 극단)
VLO   44.7%   base20 42.8%   z  +0.31   5v5 -5.7▼   2026-07-20   🟡 정상범위
MPC   51.3%   base20 56.7%   z  -0.94   5v5 +2.4▲   2026-07-20   🟡 정상범위
```

**Confirmed: PSX's short-vol z is +2.01 ("극단" — extreme surge), the full opposite sign from the
locked rationale's −1.43.** PSX is now the ONLY one of the five checked here tagged 🔴 (extreme),
where the locked rationale specifically named it the ONLY one with shorts exiting. **The premise the
core_pick rationale is built on — "the only Energy name with shorts actively exiting" — has
reversed, not just decayed.** PREMORTEM's Lens 3 chart re-tag independently reaches the same place
from a different instrument (`module_chart`): PSX flagged **EXTENDED-BUT-LIVE ⚠ outlier**, flip
condition *"OBV→분배 while z stays >+2.0"* — i.e., PSX is now the name in the complex closest to its
own kill condition, not the cleanest entry.

**What this does and does not mean, stated precisely:**
- **The forward-multiple leg of the rationale (11.2×, cheapest large refiner) is untouched** — that
  is a valuation fact, not a positioning read, and nothing measured today moves it.
- **The non-crack-segment argument (4 of 5 segments non-crack, carried from 07-19 §6) is also
  untouched** — it is a business-mix fact, independent of short interest.
- **The specific, stated, load-bearing premise of the written rationale — clean short positioning —
  has flipped sign.** A rationale that says "X because of clean positioning" is no longer accurately
  described once the positioning is the opposite of clean.
- ★ **This is filed as a finding, not a change.** `core_pick` is a **human-locked field**
  (`_note` in the registry: *"Human-locked 2026-07-17"*). This file has no authority to alter it and
  does not attempt to. **The registry entry should be re-verified by a human before being treated as
  current** — that is the full extent of what this section recommends.

---

## §7 Track KPIs + anti-signals — dated observables

| # | Observable | Reading now (asof 07-20 close, self-computed where noted) | Falsifier / trigger | Date |
|---|---|---|---|---|
| 1 | ★★ **Detachment day-2 test (KPI 3 from 07-19)** | **FIRED.** Crack down 2 consecutive sessions (90.34→88.22→85.31, self-computed), all four refiners up both sessions | Day 3 (next session crack down again + refiners still up) = the pattern is now systematic, not a one-off | rolling |
| 2 | **Distillate crack level ($/bbl, self-computed series)** | **85.31**, off the 90.34 top (07-16) | Sustained recovery above 88 breaks the 2-day-down streak; sustained fall toward the ~$32 2y median (07-19 read, not re-verified today) is the slow-motion kill | daily |
| 3 | ★ **PSX short-vol z** | **+2.01 "극단"** (was −1.43 on 07-17) | Reversion back below 0 = the registry rationale is repaired; staying >+2.0 while OBV turns 분산 = PREMORTEM's own PSX kill condition | daily |
| 4 | **CVI short-vol z** | **−2.20**, opposite direction from PSX | Convergence of the two back toward each other would remove the divergence as a signal | daily |
| 5 | **Russian refining capacity destroyed** | **24 of 34 largest refineries; 40% of capacity disabled** [nasdaq/hellenicshipping, 07-19/20] | A confirmed repair/restart of named capacity = mechanism decelerating | rolling |
| 6 | **Russian diesel export ban expiry** | in force | Not renewed on **2026-07-31** (D+10 from today) = hard dated kill | 07-31 |
| 7 | **Bab el-Mandeb / Houthi embargo** | REIGNITED 4→8 outlets, 07-20; still live on the thin 07-21 pool | Actual tanker interdiction (not just declared) = escalation; talks resume = the second chokepoint closes | rolling |
| 8 | **Iran 10-day ceasefire proposal** | Rejected so far; 10th consecutive night of US strikes [aljazeera 07-21] | Iran formally accepts/signs = the TACO trigger fires; 2 sessions of CL=F −3%+ with refiner RS20 turning negative same-day = the escalation-crash branch | undated, live |
| 9 | **Volume confirmation (majors)** | VLO 1.06× · MPC 0.86× · PSX 0.96× — **still no incremental-buying surge >1.1×** | A close on >1.3× volume, either direction, breaks the "extended on thin volume" read | daily |
| 10 | **Independents' volume (contrast)** | DINO 1.29× · PBF 1.11× · DK 1.08× — real volume, unlike the majors | Convergence toward the majors' <1.0× pattern = the independents' move is also thinning out | daily |
| 11 | **Earnings calendar** | VLO/PBF/CVI 07-30 (1 day pre-export-ban-expiry) · MPC 08-04 · PSX/PARR/DK 08-05 (post-expiry) · **KMI still date-unresolved** (07-22 per CATALYST_WATCH, flagged unverified since 07-17 DRIFT) | Q3 crack guidance on the calls | dated |
| 12 | **Counterparty (node 5)** | DAL RS20 decelerated to +1.1% (RS60 still +19.2%); UAL/LUV flat-to-down on RS20 | Airlines rolling over on RS60 too = demand destruction is finally showing, a worse regime for everyone | daily |

**Anti-signals, ranked by proximity:**
1. ★★ **Detachment day-2, now fired, not hypothetical.** The closest and most concrete anti-signal
   in the file — it is a dated, two-session-old fact, not a forward trigger.
2. **PSX's short-vol reversal specifically** — the name the registry has locked as its highest-
   conviction pick is now the name closest to a positioning-driven reversal, per two independent
   instruments (FINRA z, `module_chart`).
3. **07-31 export-ban expiry**, with three names printing earnings the day before it — unchanged
   dated risk, now D+10.
4. **Zero volume confirmation in the majors** (all <1.1×) against real volume in the independents —
   the extension in VLO/MPC/PSX specifically, not the complex as a whole, is thin.
5. **The retail "war hedge" marketing headline recurring for the fourth time** (§5) — a late-cycle
   narrative tell, not new but persistent.
6. **Carried:** the 07-31 Russia diesel export ban and the Houthi embargo both remain live, undated-
   or-dated two-sided risks with no resolution yet.

---

**EXIT CHECK:** ✅ **Delta led** (§0, 8 numbered items), unchanged structure carried **by reference**
(4 items) rather than re-printed · ✅ **Flow re-measured today by node** (`module_flow`, `us_flow.py`
FINRA), majors + independents + services + counterparty, with the volume-confirmation gap named
explicitly · ✅ **§2 Players = bounded union**, MGY logged as a new node-1 entrant without being
force-fit into the refining chain · ✅ **§3 IR anchor re-checked** (`module_disclosure_us` on VLO/PSX
— no order/contract 8-K; VLO's 07-16 Reg FD 8-K logged as non-operative) · ✅ **§4 node map carried,
node 2 updated** with the Bab el-Mandeb second chokepoint, correctly distinguished from node 3's
conversion-capacity bottleneck · ✅ **§5 chain-hop — zero candidates again**, MS rejected on both flow
and relevance grounds, VLO rejected as a non-candidate by construction · ✅ **§6 Q1 answered** — five
ranked expressions with reasoning, name kept strictly separate from the two independent timing gates
(ceasefire binary + detachment-day-2) · ✅ **§6 Q2 answered** — PSX's z verified independently
(**+2.01**, opposite sign from the locked −1.43), the reversal stated plainly, the human lock
respected (flagged, not overridden) · ✅ **§7 12 dated observables + 6 ranked anti-signals**, the
detachment-day-2 fire promoted to anti-signal #1 · ✅ **Zero buy/sell calls, zero sizing.**
