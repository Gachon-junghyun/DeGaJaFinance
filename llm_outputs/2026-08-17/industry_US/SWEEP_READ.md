# SWEEP_READ — industry_US · 2026-08-17 · Stage 4/11 (L1·SWEEP)

> The reading, not a second copy of the data. Numbers live in `SECTOR_FLOW_US.json` ·
> `US_LIVE_SHORTLIST.json` · `CYCLE_EXPOSURE.json` and are **cited, not reprinted**.

## 0 · 🚨 Instrument health line, read before any number

`SECTOR_FLOW_US.json §scoring` → `{"vel_axis": false, "vel_coverage": 0.1706, "n_axes": 3,
"scored": 299, "dropped_missing_axis": 0}`

**Coverage 17.06% (51/299) ⇒ the news axis is DEAD this run, for the 5th consecutive run.**
**Cause: the pipe, not the world — probed, not assumed.** A seeded n=40 re-probe of the 248 names the
sweep recorded as `velocity: None`, run at **22:14:12–22:14:30 KST** through the same library call the
sweep makes, returned **40/40 valid · 0 pipe failures · 0 genuinely quiet**, in 18.5 seconds.
Cumulative across three runs: **0 of 120** "silent" names were actually quiet.
⇒ Every score below is a **3-axis score**, and the failure attaches to the full-universe sweep as a
usage pattern, not to the transport (the same split the KR desk measured this morning: 5.9% swept vs
100% standalone).

## 1 · Universe headline — three numbers

**n = 299 · wflow −0.132 · 9 🟢 / 60 🔴.**
⚠ **Identical to the 08-16 run, and all 299 `flow_score` values are identical name-by-name.** Fourth
reading of the 2026-08-14 close. This is not persistence; it is one file read four times (PREFLIGHT G2).

## 2 · ★ The green count does not survive its own decomposition — `D261`, run as ROTATION's precondition

| | Count |
|---|---|
| Tagged 🟢가속 | **9** |
| Producible by the 3-axis path (`OBV+ ∧ RS20>0 ∧ vol_surge ≥ 1.2`) | **5** — `COHR` `KKR` `ABNB` `LITE` `MPC` |
| **Inadmissible** — green only because a 4th axis the score does not use answered | **4** — `CVX` (surge 0.95) · `CSCO` (RS20 **−4.7**) · `BAC` (surge 0.73) · `MA` (surge 0.73) |

⇒ **Admissible green count is 5, not 9 — a 1.8× over-representation** (08-16: 2.2× · 08-15: 3.2×).
🚫 **ROTATION may not count a green without this split.** All four inadmissible names carry a velocity
value; none could ever be green on the axes the score is actually built from.

## 3 · ★★ The one composition change in the whole sweep is 100% instrument

The shortlist moved from `[COHR KKR ABNB LITE MPC **NFLX** CVX CSCO BAC]` to
`[COHR KKR ABNB LITE MPC CVX CSCO BAC **MA**]`.
Cause, measured: with **zero price change**, `NFLX`'s velocity fell 1.23 → 1.17 and `MA`'s rose
1.17 → 1.29 across the 1.2 tag gate. `tag = flow_tag(price, velocity)` sits **outside** the axis-drop
guard that protects `flow_score` (`sector_flow.py:224` / `:342`).
⇒ **Candidate generation is non-deterministic under a 17%-coverage news bridge**, and **`MA` — the name
that entered — is one of the four inadmissible greens in §2.** This is `D263-KR` reproduced on the US
desk, now demonstrated all the way through to the candidate list rather than only at the tag layer.
🚫 **No stage may treat `MA`'s appearance or `NFLX`'s disappearance as information.**

## 4 · ★ `D270` replicated a 7th time, at a new record — "breadth 0.00" is a VOLUME statement

**125 names pass `OBV accumulating ∧ RS20 > 0`. Exactly 5 of them also clear `vol_surge ≥ 1.2`.**
⇒ **120 blocked, 100.0% of them on `vol_surge` alone** — the largest count this desk has recorded
(prior record 110 pass / 100 blocked). The whole tape is thin (median last-bar volume 0.649× the
20-day norm, after 0.732× on 08-13), so the surge denominator carries a busier past and the gate
closes board-wide at once.
⇒ **A sector reading `breadth 0.00` this week is telling you about volume, not about demand.** The one
exception is **Utilities**, where the block happens at OBV/RS — *before* `vol_surge` — and therefore
survives this correction.

## 5 · Cross-checks against the MACRO matrix — where money agrees and where it does not

| Check | Money says | MACRO matrix says | Verdict |
|---|---|---|---|
| **Energy** | Only sector with positive `wflow` (**+0.217**) *and* positive `eqflow` (**+0.102**) — the sole both-ways-positive bucket of eleven. `MPC` is one of two ✅clean-rise names (short z **−0.71**) | **OW**, driver replaced today with `P69`/`P70` (a D-0 binary the barrel refuses to pay) | ✅ **CONFIRMS** — and note the money arrived **before** today's binary, not because of it |
| **IT** | `eqflow +0.044 > wflow +0.023` — the sector's non-negativity is one name (`NVDA`, 19.4%). **Its two live shortlist names are `COHR` and `LITE`, both optical/interconnect** | **N+**, with §D-4 naming optical as the live sub-node (`optical` 1.74× · `OPTOELECTRONICS` z 5.7 · a BUILDING Lightmatter thread) | ✅ **CONFIRMS, and sharpens** — flow and news independently pick the *same sub-node*, and it is a node the book has **zero** exposure to (`S86`) |
| **Financials** | `eqflow −0.126` **below** `wflow −0.031` — the inversion `M40`/`R69` flagged is **unrepaired**. Yet 2 of 9 shortlist names are financials (`KKR` ⚡crowded-short z +1.62, `BAC`) | **N−** | ⚠ **CONTRADICTS at the name level, not the sector level.** The money is in two names inside a sector whose breadth is worse than its mega-caps. `BAC` is inadmissible (§2); `KKR` is not |
| **Utilities** | Worst `wflow` of eleven (−0.445) **and** worst `eqflow` (−0.433) — the only bucket where both agree at the bottom | **UW**, but with `P65`/`R73` making the rate leg a *tailwind* | ⚠ **CONTRADICTS the driver, confirms the verdict.** The money and the mechanism disagree; the money is unambiguous and the mechanism is inferred |
| **Consumer Discretionary** | `wflow −0.378` (10th) but `eqflow −0.123` — a **25.5pp** wflow/eqflow gap, the widest on the board, driven by `AMZN` at 40.2% weight. `ABNB` is a ✅clean-rise green inside it | **N−**, with new bear-side news (Goldman consumer-slowdown warning, Home Depot transactions down 5 straight) | ⚠ **CONTRADICTS**: the sector's headline weakness is one mega-cap; underneath it the breadth is far less bad and one name is accumulating cleanly |

## 6 · Shortlist absences — diagnosed, not cited

**Nine names from four sectors.** The absences, and what each actually is:

- **Utilities (0), Real Estate (0), Materials (0), Staples (0), Health Care (0)** — ⚠ **filter
  artifact for four of the five.** §4 shows the 🟢 gate is closing board-wide on `vol_surge` alone;
  a sector cannot produce a 🟢 name in a week when 120 of 125 accumulating names are blocked on volume.
  **Only Utilities' zero is evidence**: 0 of 15 fail at **OBV/RS**, before the surge gate.
- **Industrials (0)** — ⚠ **the most important absence, and it is a measurement gap, not a flow
  reading.** `M708` measured a **10.6pp** spread across three businesses inside the one GICS code
  (defense ≈ +7.2 · electricals ≈ +5.7 · machinery ≈ −2.4 on 20d vs `SPY`), and the defense leg is the
  book's actual position. A sector-level zero here is averaging over an object the desk has already
  proven is three objects. **And `HII` — the name today's news lead (`KUBASIK`, 0% burst baseline)
  sits next to — is outside `us_top300` entirely** (`D274`).
- **Communication Services (0)** — bucket membership changed (`EA` delisted 08-04, still in the
  universe file at day **33**, null last bar for a 5th run; `R56`).

## 7 · Held-but-not-in-universe check — clean, 6th consecutive run

**11 of 11 US holdings are inside `us_top300` AND scored** (verified against `§names`, not just the
CSV): `ANET AVGO ETN HPE MET MPC NDAQ NUE NVDA PSX RTX`. The `LNG`/`TSM` hole stays closed (neither is
held). **Zero "held but unmeasurable" names.**
⚠ But `us_top300.csv` is **33 days old** ⇒ every cap weight, including the 19.4% that decides IT's
sign, is stale. `us_all_v2_candidate.csv` exists and is unpromoted (human decision, P5).

## 8 · 🚨 CYCLE_EXPOSURE GAP — handed to ALPHA

`CYCLE_EXPOSURE.json`, book ≈ $11,601 total / $6,037 invested:

- **Rank 2 · Energy / oil-refining (Hormuz + Russia crack): epicenter 7.13% vs floor 8.0% ⇒ 🚨 GAP,
  margin −0.868pp.** Held epicenter: `MPC`, `PSX`. No adjacent/fuel layer.
  ★ **The timing is the point**: the gap is flagged on the day the 60-day US–Iran MoU expired
  (`MACRO_REPORT §D-1`). ⚠ Per the stage's own rule, **a 🔴 tape gates ADD timing and never justifies
  zero core** — and here the core is not zero, it is 0.87pp under a floor.
- Rank 1 · AI-compute: **16.57% vs 12.0% floor ✅** (`AVGO` `NVDA` `ANET`; any-layer 20.46%).
- Rank 3 · Missile-defense: 5.78%, **⚪ no floor set** — `D250`'s rank-3 floor of 0.0 is still live, so
  this row cannot fail by construction.
- 🚨 **And the registry still has NO ROW for optical / interconnect**, which is the node §5 shows flow
  and news independently selecting today, and which carries the desk's top two `flow_score` names.
  **A GAP check cannot flag exposure to a cycle it does not contain.** `D250`, reproduced with force.
