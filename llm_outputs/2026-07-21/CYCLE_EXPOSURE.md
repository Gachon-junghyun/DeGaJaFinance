# CYCLE_EXPOSURE — 2026-07-21 (industry_US, SWEEP stage byproduct)

> Dominant-cycle registry (`data/cycles/cycle_registry.json`, updated 2026-07-14) vs the REAL book.
> ⚠ **GAP check could not run this sandbox** — `cycle_exposure.py` requires the live KIS account
> (broker API) to read the book; no `.env`/creds here and the KIS token endpoint reset the connection.
> So this file reports the **registry side only** + the reconciliation it forces on the SWEEP flow tape.
> No 🚨 GAP figure is fabricated (P4): the book-vs-registry % simply is not measurable in this run.

## Dominant secular cycles (registry)

| Rank | Cycle | Core | min-epicenter | Epicenter (head) |
|---|---|---|---|---|
| **1** | AI-compute / semiconductors | **NVDA** | **12.0%** | NVDA, AVGO, AMD, MU, TSM, ASML, AMAT, LRCX, KLAC, MRVL, ANET, SMH |
| **2** | Energy / oil-refining (Hormuz + Russia crack) | — | 0% | MPC, PSX, VLO, XOM, CVX, EOG + tankers FRO, STNG, INSW, DHT |
| **3** | Missile-defense / rearmament | — | 0% | RTX, LMT, NOC, GD, LHX |

## Reconciliation with the SWEEP flow tape (the important output)

- **Rank-1 (AI-compute) vs tape:** Info Tech is the **worst-flow bleeder** this week (wflow −0.215,
  eqflow −0.375, **33 red names**), yet COT has Nasdaq-100 at **4%ile crowded-short** (under-owned).
  **The registry guard fires here:** the 2026-07-14 postmortem's named failure was *zero exposure to
  the #1 cycle's epicenter*. Rule: **a 🔴 tape gates ADD *timing*, it never justifies zero core in a
  top cycle.** → Keep a semis core (NVDA/SMH), do NOT chase, let flow + TSLA/AVGO guidance gate adds.
- **Rank-2 (Energy) vs tape:** Energy has the **biggest ignition delta (+0.457)** and +0.147 wflow,
  and COT is crowded-short (WTI 10%ile). Registry rank-2 + tape ignition + positioning all align → the
  cleanest OW. Note tanker sleeve (FRO/STNG/INSW) is the Hormuz-binary epicenter.
- **Rank-3 (Defense) vs tape:** sits inside Industrials (worst-flow-adjacent, wflow −0.22), but **RTX +
  LMT report 7/23 (binary ≤48h from mid-window)** → this is the pre-mortem swing that could promote
  Industrials from N- to a DEEP pick. Handed to PREMORTEM.

## Handoff
- No live-book 🚨 GAP number to hand ALPHA's action bracket (book unavailable). The **actionable guard**
  handed forward instead: *do not zero-core the #1 (AI-compute) cycle despite red tech flow* — ALPHA
  should express this as a "core-hold, gate-adds-on-flow" ticket, not an ADD-now ticket.
