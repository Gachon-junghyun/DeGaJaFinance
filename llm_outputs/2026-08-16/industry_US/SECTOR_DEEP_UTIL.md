# SECTOR_DEEP_UTIL — industry_US · 2026-08-16 · **Rotating slot 2** (last covered 2026-08-12 = 4 runs)

> Full fresh map. Benchmark **`SPY`** named inline (C1). Settled **2026-08-14**. No sizing (P4).
> The mandate: this is simultaneously **the board's cleanest flow signal** and **its most contested
> mechanism** — and this run has to say which of those is load-bearing.

## §1 · The signal — the only zero on this board that is not a `vol_surge` artifact

**0 of 15 Utilities names pass `OBV 매집 ∧ RS20>0`.**

That matters because of what happens to every *other* zero on this board. `M144` replicated a **7th**
time this run: **110 names pass `OBV 매집 ∧ RS20>0`, 102 are not 🟢, and 100.0% of those are blocked by
`vol_surge` alone**. The whole tape is thin (median last-bar volume **0.649×** the 20-day norm, after
0.732×), so the gate closes board-wide (`D270`) and **"breadth 0.00" almost everywhere is a statement
about VOLUME, not demand.**
★ **Utilities' zero is different because the block happens one stage earlier — at OBV/RS, before
`vol_surge` is ever consulted.** ⇒ **This is the one sector where "the money is not there" survives the
correction and is a measurement.** `eqflow` **−0.433 = worst of eleven**; `wflow` −0.445; 0🟢 / 7🔴.

## §2 · ⚠⚠ The mechanism under the UW just changed for the SECOND time — and the price is already moving

The UW was written under **`P56`: the long end is repricing TERM PREMIUM with `DGS2` pinned**, so
duration-proxy sectors get hit. **`P65` refutes half of that on the current window** (`[FRED]`, no new
data required — a re-measurement the prior run's window choice hid):

| | 08-06 | 08-13 |
|---|---|---|
| **30y − 10y** | 0.53 | **0.58** (+5bp, 5th consecutive widening) |
| `DGS30` | 5.22 | **5.21 — FELL** |
| `DGS10` | — | 4.63 (−6bp over 5 obs) |
| **`DGS2`** | **4.25** | **4.15 — FELL 10bp; it is NOT "unchanged"** |

⇒ **This is a BULL steepener at the long end**, not a term-premium level rise. Yields fell across the
curve; the 30y fell **less**. **A falling front end is a tailwind for regulated utilities**, which is
the opposite of the backdrop the UW was written under.

**And the price is already there** — 5-session excess vs **`SPY`**, settled closes:

| | exc5 | exc20 | exc60 |
|---|---|---|---|
| **`XLU`** | **+1.207** *(2nd best of eleven)* | −6.350 | −5.875 |
| `XLRE` | +0.246 | −4.777 | −2.780 |
| `XLP` | +0.741 | −3.390 | −5.807 |
| **EW of the three** | **+0.731** | **−4.839** | **−4.821** |

★★ **The three-legged "one duration bet" has turned POSITIVE on 5 days while remaining ≈−4.8pp on both
20 and 60.** That is exactly the shape `P65` predicts if the mechanism is dissolving.
🚨 **This is a THREE-SECTOR event, not a utilities one.** `S80` (settles **2026-08-19**) brackets the
UTIL/RE/STPL bundle. **Three of the desk's five UW/UW− verdicts may be one rate bet whose sign just
changed**, and `S80`'s scoring on 08-19 must be read that way (PREMORTEM §2d).

## §3 · So which is load-bearing — the flow zero or the price turn? The sector splits, and that decides it

**`W5`: "Utilities" is at least two businesses, and only one of them is the AI-power trade.**

| Name | Object | exc5 vs `SPY` | exc20 | Flow `asof 08-14` |
|---|---|---|---|---|
| **`VST`** | Merchant power / AI-power pure play | **+4.965** | **−9.149** | **🔴분산** · OBV **분산** · RS20 −9.1 |
| **`CEG`** | Nuclear merchant | **+4.274** | **+7.483** | 🟡 · OBV **중립** · RS20 **+7.5** |
| **`NEE`** | Regulated + renewables | +1.421 | **−7.386** | **🔴분산** · OBV **분산** · RS20 −7.4 |
| `GEV` *(INDU-classified)* | Turbines / grid equipment | **+6.966** | −3.935 | **🔴분산** · OBV 분산 |

⇒ **The 5-session bounce is concentrated in the MERCHANT/nuclear leg (`VST` +4.965, `CEG` +4.274,
`GEV` +6.966), not the regulated leg (`NEE` +1.421).** But a **bull steepener** should help the
**regulated** leg most (it is the rate-sensitive one) and do little for merchant power.
★ **So the 5-day turn is NOT the rate mechanism firing.** The rate story and the price move point at
**different legs**.

**What the merchant leg's bounce IS, per EVENT_ALPHA Card 5**: a **syndicated retail narrative** —
*"Why Data Centers Are Turning Energy Stocks Into AI Plays"* (`fool`→`yahoo_finance`→`nasdaq`,
**5 outlets 08-15/16**), *"3 Nuclear Energy Stocks Riding the AI Power Surge in August"* (08-16),
*"Could $5,000 in This Nuclear Stock Turn Into a Life-Changing Sum?"* (3 outlets 08-15).
⚠ **Not one operator announcement, PPA, filing or interconnection award is in the cluster.**
⇒ **Story loud, and the money on those exact names is 🔴 dispersing.** Per **RULE D6** the C-grade OBV
reading is stated only beside the A-grade price axis: `VST` OBV 분산 **with RS20 −9.1 vs `SPY`** ·
`NEE` OBV 분산 **with RS20 −7.4** · `GEV` OBV 분산 **with exc20 −3.935**. **Both axes agree on all
three names**, which is what makes a 5-day price bounce on top of them read as distribution rather than
as a turn.

## §4 · Value chain — 7 nodes, bottleneck marked

`Load growth (data-centre interconnect queue)` → `Generation (merchant: VST·CEG · regulated: NEE·SO·D)` →
**`🔴 GRID INTERCONNECTION QUEUE + TRANSFORMER/HV EQUIPMENT LEAD TIMES — the binding constraint`** →
`Transmission build (PWR — INDU-classified)` → `Turbines & grid equipment (GEV — INDU-classified)` →
`Rate-base recovery / regulatory lag (the regulated leg's real variable)` → `PPA pricing (the merchant leg's real variable)`
*(cross-sector inputs)* → `Copper · specialty steel (MATR)` · `Cost of capital (HY OAS — see RE)`.

- **Bottleneck justification**: demand is not the constraint — the interconnect queue and equipment
  lead times are. ⚠ **Two of the chain's most exposed nodes (`PWR`, `GEV`) are classified INDUSTRIALS**,
  so a Utilities-label verdict **structurally cannot see them**. That is `D9`'s sector face.
- ⚠ **The two legs have different bottlenecks**: regulated is bound by **regulatory lag + cost of
  capital**; merchant is bound by **PPA pricing**. **A single "Utilities" verdict prices neither.**

## §5 · The un-measured column, stated as `unknown` rather than filled (C3)

- **No `module_business_us` / filing pull was run on any Utilities name this run.** Rate-case status,
  interconnect-queue position and PPA terms are **`unknown`**, not "neutral".
- **`W4` is unmet across the sector**: the AI-power narrative names **zero** customers with a signed
  contract. The nearest thing in the corpus is a *Riot Platforms $9bn compute contract* (4 outlets,
  08-16), which is a **bitcoin-miner** counterparty and is not in `us_top300`.
- **No Utilities name reports inside the window** — the nearest prints are late October.
⇒ **This DEEP produces a verdict on the tape and the rate structure only, and says so.**

## §6 · Track KPIs and anti-signals

| Track KPI | Current (08-14) | Kill / anti-signal |
|---|---|---|
| **Accumulating count** | **0 of 15** | **any** UTIL name posts `OBV 매집 ∧ RS20>0` ⇒ the sector's cleanest signal is gone (this is Card 5's registered kill, re-check **08-28**) |
| **`XLU`/`XLRE`/`XLP` EW excess vs `SPY`** | exc5 **+0.731** · exc20 **−4.839** | exc20 turns positive ⇒ the three-legged UW is wrong as a bundle (`S80`, **08-19**) |
| **`DGS2`** | **4.15%** | `DGS2` **≥ 4.30%** ⇒ `P65` branch B, the term-premium mechanism reasserts and the UW's original justification returns |
| **30y − 10y** | **0.58** | narrows **< 0.50** ⇒ the steepener itself is over |
| Regulated vs merchant 20d excess spread vs `SPY` | `NEE` −7.386 vs `CEG` **+7.483** = **14.9pp** | converges ⇒ the `W5` split is not a real unit |
| Syndication count on the AI-power theme | **5 outlets, 08-16** | a **primary** operator announcement (PPA/interconnect award) ⇒ the story stops being retail advocacy |

**🚨 VOID**: a **heatwave or grid-emergency event** inside the window turns merchant power into a
weather trade and none of the above is attributable.

## §7 · Verdict handed forward

**Hold UW — and ROTATION was right to decline the notch DOWN, for the reason it gave second, not first.**
- ★ **The load-bearing fact is the split, not the zero.** The flow zero (0 of 15) is real and survives
  the `vol_surge` correction; the price turn (+1.207 exc5) is real too — **and they are about different
  legs.** A UW on "Utilities" as one object is now measurably imprecise: `CEG` is **+7.483** on 20 days
  vs `NEE` **−7.386**, a **14.9pp** spread inside the label.
- ⚠ **The UW's original mechanism is half-refuted** (`P65`), so it is now carried on **flow**, not on
  rates. **That is a weaker footing than it looked, and it is stated rather than papered over.**
- 🚨 **To ROTATION and to `S80` (08-19)**: read that bracket as a **three-sector** event. If the
  UTIL/RE/STPL EW turns positive on 20 days, **three verdicts fail together**, not one.
- ⚠ **To BET: nothing handed forward.** No admissible 🟢 exists in this sector by construction (0 of 15),
  and the 5-day bounce sits on names whose OBV is **분산**.
