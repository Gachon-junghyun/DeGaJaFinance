# ACTION_BRACKET — 2026-07-22  (conditional DRY-RUN tickets · human pulls the trigger)

> Weaves CYCLE_EXPOSURE (gap→core) + CATALYST_WATCH (binary→both-sides) + risk model + live KIS.
> Book total ≈ 11,305,406원 · fx 1476 · per-trade risk 1.5% (core 0.8%) · stop 7.0% · maxpos 25.0%
> ⚠️ DRY-RUN — sizes are illustrative; execution is a separate human `module_kis --order ... --execute`. US = USD limit only.

**Nearest binary:** TSLA earnings (D-0, axis=earnings) — both-sides armed below.

### CORE-STARTER (tape-independent) — PSX  (BUY)
- **condition:** establish NOW regardless of tape — closes Energy / oil-refining (Hormuz + Russia crack) epicenter GAP (0.0% < 8.0%)
- **size:** 4 sh @ ~$214.7937 (≈$859.17 notional, risk $61.29 = 0.8% )
- **stop:** $199.76 (−7.0%) · exch NYSE
- **why core:** cheapest large refiner on forward (11.2, PEG 1.17) + the only Energy name with shorts actively exiting (FINRA short-vol z -1.43, 5v5 -16.6▼) = clean structural entry, not an extended one (cf. MPC RSI 85.7). Crack-spread leverage, not crude beta. Human-locked 2026-07-17; evidence: llm_outputs/2026-07-17/industry_US/SECTOR_DEEP_ENRG.md

*Analytical/scheduling artifact — zero buy/sell advice. Tickets are pre-committed conditionals; no order is sent by this script.*

---
---

# ★ ALPHA FRESHNESS GATE — appended 2026-07-22 (Stage 9/10 · L1·ALPHA), append-only

> Everything above this line is `action_bracket.py`'s deterministic output, **unedited**. Everything
> below is the ALPHA stage's freshness gate over it. Written **06:5x ET, US session not open**.
> All RS figures **vs SPY**. Zero buy/sell advice; nothing here instructs an order.

## 🚨 GATE 1 — the PSX ticket's "why core" line is **stale on BOTH of its load-bearing premises**

The generated line reads: *"**cheapest large refiner on forward (11.2, PEG 1.17)** + the only Energy name
with **shorts actively exiting (FINRA short-vol z −1.43, 5v5 −16.6▼)**."* Both clauses were measured
independently today and neither holds:

**(1) The short-flow clause is a frozen string, and it has now been wrong in two different directions on
two consecutive runs.** Registry says **z −1.43**. Measured **2026-07-20: z +2.01 🔴** (flagged by
yesterday's GATE 1). Measured **2026-07-21: z +0.01 — neutral.** The spike has fully normalized. So the
correct statement today is neither "shorts actively exiting" nor "short spike": it is **"nothing to see
on this axis."** The number in the ticket is not a live read and should not be treated as one.
⚠ C-grade axis regardless (D6) — it may corroborate, it may not carry the ticket.

**(2) The "cheapest large refiner" clause fails on a like-for-like basis.** On one consistent basis —
FY26 consensus EPS, pulled today — the three in-universe refiners are **MPC 8.8x · VLO 9.4x · PSX 10.8x**.
**PSX is the most expensive of the three**, not the cheapest. The ticket's "11.2 forward" is on an
unstated basis (a vendor forward-EPS field, not FY26 consensus), and comparing across bases is how this
kind of claim survives unchallenged. **The basis must be stated in the registry field or the claim is
not checkable.**

★ **But a better-founded case for the same name survives, and it is not the one the ticket makes.**
On FY26 → FY27 consensus EPS the three carry very different cliffs: **VLO −31.6% · MPC −25.8% ·
PSX −7.2%.** With the 3-2-1 crack at the **99.5th percentile of 3 years**, **PSX is by far the least
peak-dependent of the three.** That is a structural argument that survives a truce; "cheapest on forward"
is not. **Offered as an observation, not substituted into the ticket** —
⚠ `core_pick` is a **HUMAN-LOCKED registry field** (`_note`: "Human-locked 2026-07-17"). **This stage has
no authority to change it and does not. The ticket is flagged, not rewritten.** A human must re-verify.

## 🚨 GATE 2 — the script announced a both-sides bracket and emitted none. **Second consecutive run.**

Line 7 reads *"**Nearest binary:** TSLA earnings (D-0) — both-sides armed below"* and **nothing is armed
below it.** The identical defect was logged on 2026-07-21. Two further problems compound it:

- **`CATALYST_WATCH.json` missed the largest binary on the board entirely.** Today's calendar lists
  TSLA and KMI (07-22) and RTX and LMT (07-23). **GOOGL — which prints tonight, carries a ±7.1% implied
  move, and is the single event the whole run is organised around — is absent.** This is the desk's own
  previously-logged failure class (*"catalyst_calendar missed the largest binary two runs running"*),
  now recurring on the US side. **Logged, not patched around.**
- **The run's own PREMORTEM explicitly DECLINED to bracket TSLA**, with the reason stated: neither branch
  changes a conclusion, because the Cons Disc UW rests on **eqflow −0.103, 0 green / 8 red of 28** — a
  breadth verdict one name can neither repair nor confirm. So the script's "nearest binary" is **not this
  run's binary**, and arming it would have been the wrong bracket.

**The run's actual brackets are registered where a script cannot see them** — `handoff/SCENARIOS.md`
**S1 (GOOGL capex), S6 (INTC 07-23), S7 (RTX+LMT 07-23, one binary), S8 (Hormuz, undated), S9 (the dovish
real-rate branch)** — all registered **before** their events, thresholds frozen, each with both branches.
⚠ **Frozen magnitude thresholds carry a measurement defect that is recorded, not absorbed**: GOOGL's
±7.1% and INTC's ±4.4% straddles are tagged **expiry D0** — the contract expires *before* the print it is
meant to price. **They are floors, not fair estimates.** The thresholds are **not widened** for this.

## 🚨 GATE 3 — the GAP the ticket exists to close is now **4 for 4**, and both of these are true at once

Epicenter exposure to rank-2 Energy/oil-refining printed **0.00%** on **07-17, 07-19, 07-21 and 07-22**,
against an 8.0% requirement. Today the cycle also holds a DEEP slot. Stated plainly, both halves:
- **A 🔴/crowded tape gates ADD timing; it never justifies 0% core in a rank-2 multi-year cycle.**
- **A 🚨 GAP is a coverage statement about the book, not a signal** — and this run's oil variable
  **reversed twice in two sessions** ($89 → $82 → >$92), with **S8 branch B explicitly stating that crude
  falling while cracks hold is NOT against the thesis.**
**This stage records both and resolves them into no action.** The decision is a human's.
⚠ Coverage finding attached: the in-universe epicenter is **exhaustively VLO · MPC · PSX**; the
independent-refiner tier (PBF, DINO, CVI, DK, PARR) and the whole tanker/Hormuz-transit leg (FRO, STNG,
INSW, DHT) are **not in `us_top300`** and cannot be seen by any stage of this run.

## Momentum-only flags — **hard-stop required** where stamped

| Name | Read | Flag |
|---|---|---|
| **T (AT&T)** | 🟢 tag built on a **1.53 volume surge** with **RS20 +0.2 / RS60 −22.0** | **MOMENTUM-ONLY, and not even that** — the A-grade axis disagrees outright. **Dropped in BET §E.** The board's clearest single instance of defect **D11** |
| **EA** | 🟢 on surge 1.41 with RS20 +2.5 / RS60 −2.4 | **Dropped.** Volume-surge artifact |
| **UNH** | The **only 🟢** of the managed-care trio while carrying **1/5th of HUM's RS60 (+82.5)** | **C-grade tag outranking the A-grade axis.** Kept, flagged, **hard-stop required** |
| **AXON** | Price outran SPY **+24.6pp** while FY26 EPS was **cut 1.24%**; **no backlog line in the 10-K**; **−42.3% from its 52-week high** | **MULTIPLE-ONLY. Dropped from the defense bucket and logged** so it cannot return as "the most accelerating defense name" |
| **PYPL** | Board-best flow **+1.000**, RS20 +31.4 — on **0y EPS +0.06%** and revisions **0↑ : 3↓ all within 7 days** | **M&A situation, not a thesis. 🔴 RESOLVED → dropped and logged** |

⚠ **Grading note (D6), applied throughout**: on the US path `has_conviction` can only be satisfied by
OBV (news velocity is `None` on all 300 rows), so **every US 🟢 on this board is OBV-gated**. A C-grade
disagreement **downgrades to 🟡 and is reported as a disagreement** — it does not by itself convert a bet
into a tape trade. The names where RS agrees on both horizons (PYPL-ex, CTAS, TRV, ABT, CB, USB, UNH,
STT) survive that downgrade as genuine; T, EA and TRI do not.

## Positioning gates — crowded-short is **turn-conditional squeeze fuel, never a standalone reason**

| Name | FINRA short-vol z (07-21) | Gate |
|---|---|---|
| **CB** | **+1.61 🔴** (5v5 +14.8▲) — the sector's new crowded short | ⚡ squeeze fuel only, **hard-stop stamp**. Test: z back below +1.0 by **07-24** = spent, the same 3-session test GS just passed |
| **MPC** | **+1.69 🔴** (base20 56.3% → 66.1%) — the only spike in the refining complex | ⚡ same treatment; it is also the most extreme name on **every** valuation and revision axis in §A |
| **NOC** | **+2.27 🔴 building**, with RS60 **−18.4** | ⚡ and its vendor consensus is **stale** against its own 07-21 guidance raise — not usable as evidence this run |
| **TRV** | **−2.00** extreme covering | Clean on this axis — but see BET §B: **+9.7% above** consensus target, **+1y EPS below 0y**, GS **Sell/$350** on 07-20 |
| **GS · STT** | +1.59 → **−0.11** · +1.50 → **−0.13** | **Both 07-21 anti-signals are SPENT, not confirmed.** Recorded as falsified and **not carried forward** |

## Freshness roll-up (the tags written into `BET_SHEET.md §B` this stage)

| Bet | Tag | Evidence label + date |
|---|---|---|
| Energy / refining (VLO·MPC·PSX) | 🟡 **PARTIAL** | `theme-age "refining margin"` **🟡ACCELERATING, 54d, 8.57×, n=30** (2026-07-22). Residual: crack at 99.5th 3y pct; detachment counter **3** |
| Financials — GS dislocation | 🟢 **LIVE** | 0y EPS **+18.8%/30d, 9↑:0↓** vs flow −0.450 (2026-07-22) |
| Financials — STT · USB | 🟢 **LIVE** | STT 4↑:0↓ all periods, 12.02x fwd; USB = the super-regional steepener (2026-07-22) |
| Financials — P&C (TRV·CB) | 🟡 **PARTIAL** | `theme-age "reinsurance pricing"` **🟢FRESH, 5d — but n=1**, so carried on Arch 07-17 + WRB call 07-20, not on the tag |
| Financials — PYPL | 🔴 **RESOLVED → DROPPED** | M&A, not fundamentals; 0↑:3↓ in 7 days; +6.5% above target (2026-07-22) |
| Industrials — GD | 🟢 **LIVE** | Only clean 3↑/0↓ book, z −1.53 covering, positive on both RS horizons; prints **07-29** |
| Industrials — RTX · LMT | 🟡 **PARTIAL** | Frozen behind **S7**, observable = backlog at both, **2026-07-23** |
| Industrials — AXON | 🔴 **RESOLVED → DROPPED** | Estimates cut while price ran; no backlog line; customer is not a DoD budget line (2026-07-22) |
| Security / observability — FTNT | 🟢 **LIVE** | 39↑:0↓ both periods; **catalyst 2026-07-30, inside the window**. ⚠ **+31.8% above** consensus target |
| Security / observability — DDOG | 🟢 **LIVE** | 0y EPS **+12.5%/90d**, PEG **1.61**, at target; catalyst 08-06 |
| Security / observability — CRWD · PANW | 🟡 **PARTIAL** | CRWD fwd 122.4x / PEG 6.6 / slowest estimates, catalyst 09-02. PANW +1y 3↑:7↓ **plus a suspected vendor period artifact** |
| Cross-sector — CTAS · ABT | 🟡 **PARTIAL** | RS agrees on both horizons; no catalyst in window `[blank]` |
| Cross-sector — TRI | 🟡 **PARTIAL** | RS20 +18.0 but **RS60 −5.0** — mixed, carried not promoted |
| Cross-sector — T · EA | 🔴 **DROPPED** | Volume-surge tags with disagreeing RS (2026-07-22) |

⚠ Theme-age verdicts built on **n ≤ 2** (`"agentic AI risk"` n=2, `"munitions replenishment"` n=1,
`"reinsurance pricing"` n=1, `"diesel crack spread"` n=0) are recorded as **indistinguishable**, not as
fades or as freshness. **A 🔴FADING on one article is a term artifact, not a measurement** — and
`⚫SILENT n=0` means the desk used a phrase the feed does not, exactly the failure class the quoted-bucket
trap belongs to.

## ✅ EXIT CHECK
- [x] Every §B tag filled with an evidence label and a date; **three 🔴 dropped AND logged with why**
      (PYPL, AXON, T/EA) so they cannot resurface next run as fresh ideas.
- [x] Momentum-only flags stamped (T, EA, UNH, AXON, PYPL) with hard-stop where kept.
- [x] Positioning gates stamped (CB, MPC, NOC crowded-short = turn-conditional only; GS/STT anti-signals
      recorded as **spent, not confirmed**).
- [x] `ACTION_TICKETS.md` written by the script and gated here; the script's two defects (unarmed
      announced bracket; a "why core" line stale on both premises) are **flagged, not silently accepted**,
      and the human-locked registry field is **not** modified by this stage.

*Analytical artifact. Zero buy/sell advice, zero sizing recommendation. Nothing in this file sends an
order; the DRY-RUN ticket above is the script's, and a human executes separately if at all.*