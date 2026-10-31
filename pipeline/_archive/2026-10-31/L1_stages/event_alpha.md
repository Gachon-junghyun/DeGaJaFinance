# L1 · EVENT_ALPHA — building stories × following money → forward cards (stage)

> Big stage. The **bottom-up** complement to MACRO's top-down transmission matrix: MACRO asks
> "which sectors SHOULD benefit from my propositions"; this stage asks "which stories ARE
> building this week, and is money already following them". Runs after SWEEP, before ROTATION
> (its candidates are a rotation cross-check). Runtime: `--market us|kr`.
> Output: `EVENT_ALPHA.md` under `llm_outputs/{date}/industry_{US|KR}/`.

## L2 called
- [narrative_money](../L2_modules/narrative_money.md) — the whole cross: thread selection →
  direction body-read → exposure map (one hop past headlines) → flow tags → 2×2 cell.
  ⚠ Scope is market-locked there (KR=domestic, US=foreign, `all` banned) — the measured 787:0
  KR-feed bias is exactly the failure this rule exists to prevent.

## What this stage does
- **Select ≤8 threads** from the alive market set: precursor-form first (curve starting ≤2 outlets
  and climbing — the measured shape: the BOK rate-hike saga gave 5 days of runway from a 2-outlet
  tail item), then remaining BUILDING/REIGNITED by peak. Log what was NOT selected (count — no
  silent truncation).
- Run each through the narrative_money cross. Kill any thread whose direction body-read
  contradicts its headline before it reaches a card.
- **Write FORWARD cards — the deliverable.** One per surviving thread, each a dated, falsifiable
  "this industry/company's future" statement:
  - **Thread**: title · tag · curve · window denominator (e.g. `BUILDING 2→2→5 · 사건 2,480/스레드 352`)
  - **Direction**: one sentence from the body-read, with the quoted evidence line
  - **Exposure**: 2–5 names, each `ticker · chain position · flow tag(asof) · crowding note`
    (headline-layer names marked as such — they are the crowded layer by construction)
  - **Future (both branches, mandatory)**: IF the thread keeps building AND flow stays 🟢 →
    {scenario + track KPI + horizon date}; ELSE → {kill condition that falsifies the card}
  - **Cell + hand-off**: CONFIRMED-EARLY → BET-stage candidate · STORY-ONLY → watchlist with a
    dated re-check · LATE-MONEY → valuation gate note · DEAD → drop
  - ⚠ **DEAD is a MONEY verdict, not a story verdict.** The 2×2's bottom-right cell is
    FADING/ENDED **×🔴 dispersing** — *both* axes. A thread that went quiet while the flow is still
    🟢 accumulating is not DEAD; it is a name whose thesis needs rewriting, so re-file it (new thesis
    line + dated re-check) rather than dropping it. Every drop is written to the ledger with its
    **`--revives-if`** condition — L3 [reject_ledger](../L3_functions/reject_ledger.md).
  - ⚠ **A thread you read and did not turn into a card is not a drop — it is a miss.** Threads that
    cleared the money axis but never became cards go to L3
    [missed_ledger](../L3_functions/missed_ledger.md) (`M.숏리스트탈락` or `Q.확신부족`) with an
    `--enters-if`. Otherwise the funnel's widest stage is the one with no scoreboard.
- **Book cross-check**: any ENDED thread that an open book position's thesis rides on → flag to
  the book desk (paper_desk / 미러링) in the card file's final section. Attention rotated;
  the position must re-justify on something that is still alive.
- Hand candidates forward: ROTATION reads the cards as sector-level cross-evidence; BET §B reads
  CONFIRMED-EARLY names as fresh candidates (BET owns sizing — this stage never sizes).

## ✅ EXIT CHECK
- [ ] Scope was market-correct (KR=domestic / US=foreign) — a card citing cross-market feed is void.
- [ ] Selection logged: N alive threads → ≤8 selected, non-selected counted (no silent cap).
- [ ] Every card: direction body-read done (headline-only cards are a failed stage — the biggest
      measured thread was a LOSS the headline never said).
- [ ] Every exposure name carries a flow tag with asof date; STORY-ONLY names did not leak into
      the candidate hand-off.
- [ ] Every card has both branches + a kill condition + a dated horizon (P4: falsifiable or absent).
- [ ] `EVENT_ALPHA.md` written; CONFIRMED-EARLY handed to ROTATION/BET; ENDED-thread book flags
      emitted; handoff ledger updated ([handoff](../handoff.md)).
