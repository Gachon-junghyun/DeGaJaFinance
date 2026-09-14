# ACTION_BRACKET — 2026-08-17  (conditional DRY-RUN tickets · human pulls the trigger)

> Weaves CYCLE_EXPOSURE (gap→core) + CATALYST_WATCH (binary→both-sides) + risk model + live KIS.
> Book total ≈ 16,051,249원 · fx 1415 · per-trade risk 1.5% (core 0.8%) · stop 7.0% · maxpos 25.0%
> ⚠️ DRY-RUN — sizes are illustrative; execution is a separate human `module_kis --order ... --execute`. US = USD limit only.

**Nearest binary:** NVDA earnings (D-9, axis=earnings) — both-sides armed below.

### CORE-STARTER (tape-independent) — PSX  (BUY)
- **condition:** establish NOW regardless of tape — closes Energy / oil-refining (Hormuz + Russia crack) epicenter GAP (7.13% < 8.0%)
- **size:** 5 sh @ ~$238.4399 (≈$1,192.2 notional, risk $90.76 = 0.8% )
- **stop:** $221.75 (−7.0%) · exch NYSE
- **why core:** cheapest large refiner on forward (11.2, PEG 1.17) + the only Energy name with shorts actively exiting (FINRA short-vol z -1.43, 5v5 -16.6▼) = clean structural entry, not an extended one (cf. MPC RSI 85.7). Crack-spread leverage, not crude beta. Human-locked 2026-07-17; evidence: llm_outputs/2026-07-17/industry_US/SECTOR_DEEP_ENRG.md

*Analytical/scheduling artifact — zero buy/sell advice. Tickets are pre-committed conditionals; no order is sent by this script.*
---

# ADDENDUM — L1·ALPHA, industry_US 2026-08-17 (Stage 10/11)

> The block above is the **script's** deterministic output. This addendum is the desk's reading of it.
> **Analytical only — zero buy/sell advice, no order sent, no `--execute` anywhere in this run (P4/P5).**

## 1 · 🚨 The script's binary line is INCOMPLETE, and that is the first thing to say

The generated header reads **"Nearest binary: NVDA earnings (D-9)"**. It is wrong by nine days, because
it reads `CATALYST_WATCH.json`, and **`CATALYST_WATCH` missed today's D-0 binary**:

**The 60-day US–Iran ceasefire / Memorandum of Understanding EXPIRED 2026-08-17** — 5 independent
outlets (`MACRO_REPORT §D-1`), with Strait-of-Hormuz tanker traffic reported at or near **zero**.

⇒ **Every "both-sides armed" claim in the block above is armed against the wrong event.** The correct
both-sides bracket for today's binary is **`S95`** (registered by PREMORTEM: `BZ=F` at the 08-21
settle — **A ≥ 93.00 · B ≤ 86.50 · C 86.50–93.00 declared NO-INFORMATION and the favourite**).
This is `D259-KR` reproduced on the US desk: **the calendar does not read `SCENARIOS`' armed dates**,
and eight US rows settle inside the same ten-day window it summarised as "2 binaries".

## 2 · 🚨 The CORE-STARTER ticket's rationale is STALE and must not be read as this run's evidence

The ticket cites *"MPC RSI 85.7"* and *"FINRA short-vol z −1.43"* and stamps
**"Human-locked 2026-07-17; evidence: llm_outputs/2026-07-17/…"** — a **31-day-old** evidence file.
**Today's measurements differ:**

| Claim in the ticket | Today's measurement (settled 2026-08-14) |
|---|---|
| `PSX` FINRA short-vol z **−1.43**, 5v5 −16.6▼ | **not re-measured for `PSX` this run** — `us_flow` was run for `MPC` (z −0.71) and eight other names, **not `PSX`**. ⇒ the ticket's short leg is `unknown` (C3) |
| *"clean structural entry, not an extended one (cf. MPC RSI 85.7)"* | `PSX` rs60 is now **+22.3** vs `SPY` and rs5 **+14.17** — **the entry is no longer un-extended.** Lens 3 measures the 5-day move at **+3.15z** |
| *"cheapest large refiner on forward (11.2, PEG 1.17)"* | fwd P/E **11.32**, **PEG 1.35** today. `MPC` is now marginally cheaper on forward (**11.24**) | 
| Price `~$238.44` | live intraday 22:5x KST; **settled 08-14 close was $233.61** |

⇒ **The ticket is a pre-committed conditional whose stated reason has decayed.** It is left in place
(the script owns that file section and a human locked it), and **this addendum is the correction of
record** rather than an edit to it.

## 3 · The GAP the ticket exists to close — restated with the counter-argument attached

`CYCLE_EXPOSURE`: **rank-2 Energy / oil-refining epicenter 7.13% vs an 8.0% floor = −0.868pp**, flagged
on the day the binary expired. The stage rule is that a crowded tape gates ADD **timing**, never the
core's existence — and the core here is **0.87pp under a floor**, not zero.

⚠⚠ **Three measured objections travel on the same line (PREMORTEM Lens 4a, BET §F):**
1. `MPC` **+3.10z**, `PSX` **+3.15z**, `VLO` **+2.96z** are **date-clustered in the same five sessions
   on the same driver** ⇒ **n≈1, not n=3.**
2. **The barrel refuses the story**: Brent **−0.44%** and WTI **−0.96%** across 08-11 → 08-14 while
   Hormuz traffic collapsed; `XLE` beat `SPY` by only **+0.86pp**.
3. **All three refiners trade ABOVE consensus target median** (`MPC` +12.4% · `PSX` +8.1% · `VLO` +7.4%).
⇒ **Reported as a GAP. No action, no size, no recommendation.**

## 4 · 🚨 The GAP check cannot see this run's best-scoring cycle

`cycle_registry.json` has **no row for optical/interconnect**. The desk's **#1 and #2 `flow_score`
names board-wide** (`COHR` +0.99, `LITE` +0.82) sit in that cycle, so exposure to it is
**unmeasurable, not zero** — and no ticket can ever be generated for it. Rank-3 missile-defense has the
mirror defect: **no floor set ⇒ ⚪n/a ⇒ it cannot fail.** `D250`; `S94` settles 08-31. **Registry
maintenance is a human item (P5).**

## 5 · Freshness tags issued this run — and the one that could not be issued

Full tags live in `BET_SHEET §B`. Summary: **8 names tagged 🟡PARTIAL, 0 🟢LIVE, 0 🔴RESOLVED.**

★ **`F1` closed a second time, and this run locates the failing leg.** The pipe answered **19 of 19**
`theme_age` probes (22:30–23:05 KST), so the zero is not the instrument. The gate needs
**age ≤14d AND accel ≥2×**:
- **Acceleration cleared twice** — `travel booking` **2.2×** (`ABNB`) and `retail earnings` **30.0×**
  (`TGT`, ⚠ base 61 articles ⇒ fragile ratio).
- **Age failed on all 19** — seventeen read the tool's own cap **">=90"**, the two accelerating ones
  ≥90 and **82**.
⇒ **For any theme older than 90 days, 🟢FRESH is structurally unreachable regardless of acceleration**,
and a US desk trading multi-quarter industrial cycles will not see a ≤14-day theme. The 08-16 run
closed `F1` as a *gate* property; this run names **which half of the gate**.
🚫 **Consequence: no name may be marked 🔴RESOLVED on a freshness reading**, because the instrument
cannot issue the contrasting tag. Zero 🔴 rows were written to `reject_ledger` from this stage.

## 6 · 🟡PARTIAL residuals are dated appointments — handed to carryover

| Name | Residual | Re-check |
|---|---|---|
| `MPC` `PSX` `VLO` | does the barrel ever pay? (`S95` · `P70` · `S88` all settle together) | **2026-08-21** |
| `COHR` | reclaim **332.48** with `vol_surge` ≥1.0 (`S96`) | **2026-08-21** |
| `LITE` | rs60 turns positive, so the move is a trend not a print reaction (`S96`) | **2026-08-21** |
| `KKR` | explain the **±10.8%** implied move with no scheduled print (`S78`) | **2026-08-19** |
| `ABNB` | Lens-3 flip: rs20 negative while rs60 positive (`S93`) | **2026-08-21** |
| `TGT` | its own print, against a **±6.7%** implied move = **4.5× its 1.48% daily sigma**, put-heavy | **~2026-08-20** |

⚠ **Every residual above has a date and a registered row.** An armed condition nobody returns to is an
idea the desk already paid for and never collected (the 475150 precedent, **+41.2pp / +26.9pp**).

## 7 · Tags that were never issued — written to the missed ledger, not left silent

`APH` (`Q.확신부족`) · `NOC` (`M.숏리스트탈락`) · `CIEN` (`M.숏리스트탈락`) — all three cleared at
least one axis, none reached a tag, all three carry an `enters-if` and a **2026-08-25** re-check.
`HD` is the run's only rejection (`D.약한손`, revives-if OBV accumulating **and** rs20 > 0, **08-25**).

*Analytical artifact. No order was sent, no `--execute` flag was used, and this desk issues no buy or
sell recommendation (P4).*
