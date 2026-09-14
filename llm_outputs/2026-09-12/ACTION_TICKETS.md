# ACTION_BRACKET — 2026-09-12  (conditional DRY-RUN tickets · human pulls the trigger)

> Weaves CYCLE_EXPOSURE (gap→core) + CATALYST_WATCH (binary→both-sides) + risk model + live KIS.
> Book total ≈ 15,183,560원 · fx 1338 · per-trade risk 1.5% (core 0.8%) · stop 7.0% · maxpos 25.0%
> ⚠️ DRY-RUN — sizes are illustrative; execution is a separate human `module_kis --order ... --execute`. US = USD limit only.

**Nearest binary:** FOMC decision (SEP/dot plot) (D-4, axis=rates) — both-sides armed below.

### BRACKET::A_cool  ★asym-hedge — NVDA  (BUY)
- **condition:** IF FOMC decision (SEP/dot plot) (D-4) prints toward cool
- **size:** 5 sh @ ~$218.29 (≈$1,091.45 notional, risk $90.77 = 0.8% )
- **stop:** $203.01 (−7.0%) · exch NASD

### BRACKET::B_hot — XLE  (BUY)
- **condition:** IF FOMC decision (SEP/dot plot) (D-4) prints toward hot
- **size:** 37 sh @ ~$65.14 (≈$2,410.18 notional, risk $170.19 = 1.5% )
- **stop:** $60.58 (−7.0%) · exch AMEX

*Analytical/scheduling artifact — zero buy/sell advice. Tickets are pre-committed conditionals; no order is sent by this script.*

---

## ALPHA addendum — 2026-09-12 (Stage 10 / L1·ALPHA, 23:08 KST) · DRY-RUN, analytical only

**Quotes above are 09-11 settled closes** (run on a Saturday — no partial bar). ⚠ The script's `cool/hot`
branch map is an inflation-print template; for **FOMC 09-16 (a hike ~87% priced `[WebSearch]`)** read
A = **dovish surprise** (`P151`-B: `SHY` 1-session ≥ +0.134%) and B = **hawkish-beyond-consensus**
(`P151`-A: `SHY` ≤ −0.236%). ⚠ The script chose `NVDA` for the A-leg; DEEP-IT §9 reads `NVDA` as
**DISTRIBUTION** (rs20 flipped negative, OBV worsening) — the desk's own epicenter expression for the
rank-1 cycle is the **inference fork** (`QCOM`), so the A-leg name below is substituted analytically;
the script line is left standing for the record.

### Pre-committed conditional tickets (both-sides per binary; a human executes, never the desk)
| bracket | condition (frozen observable) | analytical expression | illustrative size (DRY-RUN) | stop / invalidation |
|---|---|---|---|---|
| **FOMC-A · dovish surprise** | `P151`-B: `SHY` 09-15→09-16 ≥ +0.134% (p95) **or** `P148`-B: `IEF−SHY` 09-15→09-17 ≥ +0.2856% | the against-us branch rips duration: `XLU` / `XLRE` starter (lens 2); held `MET` thesis dies, `NDAQ` becomes the winner | core-risk 0.8% line (≈ ₩121k risk) on `XLU` — **illustration** | dead if hike delivered ∧ `SHY` ≤ −0.073% by 09-17 close |
| **FOMC-B · hawkish beyond consensus** | `P151`-A: `SHY` ≤ −0.236% (p05) **or** `P148`-A: `IEF−SHY` ≤ −0.3469% | the desk's tilt confirmed: `XLE` (script line, 37 sh) or the refiner leg already held (`MPC`/`PSX`) — **no add is needed to express it; the ticket is "hold the tilt"** | 0 new shares (the book already holds the branch) | `hy_oas` ≥ 3.10 voids the rate attribution |
| **Hormuz-A · Muscat agreement signed (undated)** | ≥3-outlet confirmation **or** `S156`-A (crack 5-session ≤ −4.25 $/bbl by 09-18) **or** `CL=F` 1-session ≤ −4.98% ∧ crack ≤ p05 same day | against-us: refiners bleed — held `MPC`/`PSX` name rails **$374 / $247.5** (MA20); `DAL`/`UAL`/`JETS`/`XLI` are the rip side (lens 2, not held) | **exit-rail ticket** on held refiners, not an entry | `CL=F` reclaims 102.48 within two sessions of the headline |
| **Hormuz-B · scarcity extends** | `S156`-B (crack ≥ +8.70) ∧ `P149`-A (`XLE`−`CL` 5-session ≥ +4.69pp) | the equity leg catches up: **barrel leg** `DVN` / `EOG` (0% held) | core-risk 0.8% on `DVN` (~50.23; ≈ 24 sh ≈ $1,206 notional; stop 7% ≈ $46.71) — **illustration** | `P149`-B (gap ≤ −5.17) kills; `S156`-A voids the leg |
| **HLTH · `P150`** | A (EW HC ≤ −2.594pp vs `SPY` by 09-18) / B (≥ +2.422pp) | A: nothing to do (N stays; demotion on measurement) · B: survivors `REGN`/`VRTX`/`GILD` = the bounce side (lens 3) | no ticket — bracket only | `AMGN`/`BSX`/`SYK` excluded from any bounce read (broken, own news) |

### Cycle-GAP core-starter (PREMORTEM Lens 4 — tape-independent partial core; tape gates the remainder)
| gap | epicenter expression | illustrative core (0.8% risk, 7% stop, fx 1338) | tape gate for the remainder |
|---|---|---|---|
| **Inference-silicon / optics fork — 0% held** | **`QCOM`** (🟢, LAG; 8-K warrants @ $161.26) · alt `LITE` (optics, 매집 ∧ rs60 > 0) | `QCOM` ~181.97: ≈ **7 sh** (≈ $1,274 notional; risk ≈ $89; stop ≈ $169.2 — the lens-3 gap rail **$168.7** sits just below the 7% stop, stated) | 09-18 sweep LAG rail (≥3 of {`QCOM`,`AMD`,`MRVL`,`GLW`,`COHR`} rs20 > 0 ∧ OBV ≥ 중립); rs60 > 0 by 10-09 |
| **Barrel / E&P leg — 0% held** | **`DVN`** · `EOG` | see the Hormuz-B line (≈ 24 sh `DVN`) | `P149`-A |
| Ton-mile / tankers | `FRO` / `DHT` / `INSW` — **out of universe, unmeasurable** | none — named, not sized (`D563`) | universe rebuild (human) |

*All lines are DRY-RUN illustrations of the protocol's action bracket. Zero buy/sell advice; no order is
sent by any stage. A human re-prices and decides.*
