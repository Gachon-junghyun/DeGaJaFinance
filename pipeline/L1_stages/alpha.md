# L1 · ALPHA — alpha-freshness gate (stage)

> Phase 4. Separates "interesting" from "bettable NOW". The whole pipeline runs on lagging data
> (news up to 60d, EOD primaries) — by thesis time the catalyst may have fired. Calls L2.
> Output: `BET_SHEET §B` tags (🟢LIVE / 🟡PARTIAL / 🔴RESOLVED) + (US) `ACTION_TICKETS.md`.

## L2 called
- [schedule](../L2_modules/schedule.md) — `theme_age` deterministic novelty FIRST (token-0):
  🟢FRESH (≤14d + accel ≥2×, the golden zone) / 🟡ACCELERATING / ⚪ECHO (loud but consumed) /
  🔴FADING. ECHO/FADING theses need *stronger* live evidence to survive.
- [indicators](../L2_modules/indicators.md) — `module_flow --positioning` quantitative first.
  ⚠ **`--positioning` (implied move) is US-only.** For KR the positioning read is
  `module_KIS --futboard`/`--futopt` — index-futures **basis + OI (context, not a threshold)**. KR
  scenario thresholds therefore stay hand-set until the **options-IV v1.1** lands (the true KR implied
  move); do not fabricate a KR threshold from futures basis. Stamp KR positioning as context only.
- [news](../L2_modules/news.md) — targeted live WebSearch per bet: catalyst already fired?
  move already made? thesis already street consensus?

## What this stage does
- Tag each bet 🟢LIVE / 🟡PARTIAL (state the residual) / 🔴RESOLVED → **🔴 is DROPPED from the
  bettable list + logged with why** (so "it's cheap" can't resurface next run).
  **Log it as a ledger row, not as prose** — L3 [reject_ledger](../L3_functions/reject_ledger.md),
  with its reason class and its **`--revives-if`** condition. The condition is what lets a 🔴 come back
  on evidence rather than on someone remembering it: measured, 475150's kill condition (short
  `covering→building`) reversed three runs later while the ban stayed on.
  ★ **And the tags that never got issued.** A name carried into ALPHA that receives **no tag at all**
  — because the sheet ran out of room, or its sector lost its DEEP slot — is not a 🔴; it is a
  *missed* entry, and it leaves no record unless you write one to L3
  [missed_ledger](../L3_functions/missed_ledger.md) with an `--enters-if`. Measured why this matters:
  🟢LIVE fired **0 times in 8 consecutive runs** (F1) because it required a FRESH theme age the board
  structurally could not produce — a gate that never fires looks identical to a universe with
  nothing in it, and neither leaves a row.

  🚨🚨 **AND THAT ZERO MAY NOT BE THE MARKET — CHECK THE PIPE BEFORE READING IT AS ARITHMETIC**
  (added 2026-08-10; the KR count is now **18 consecutive runs**). This whole stage stands on
  `theme_age`, which stands on the news index, and **the news index was measured failing silently**:
  · The search rides a remote tunnel (`DEGAJA_NEWS_API`) with **no local fallback on the client**
    (`data/news_fts.db` does not exist there — the server owns it, P6), and it **intermittently
    drops**: success → 5/5 failure → success, inside one hour.
  · A dead pipe and a quiet theme return the **identical** value. Nothing distinguishes them.
  · Separately, the KR universe sweep queried the **foreign/English** pool for Korean company names
    for months (`kr=` never passed) — 삼성바이오로직스 base **5 articles**, LG에너지솔루션 **2**.
  ⇒ **Before writing "F1 is arithmetic — no FRESH theme exists", run the falsification probe:**
  `python -X utf8 -m module_news_data fts search 삼성전자 --days 7 --count` (KR) — a known-loud name
  must come back loud. If it does not, **the zero is the instrument** and this stage must say so
  instead of issuing another F1 line. This is gate **G1** of [preflight](../protocols/preflight.md);
  when G1 FAILs, ALPHA may not issue a freshness verdict at all.
  ★ **Eighteen identical observations are not eighteen observations if one wire is loose.** The
  desk has been recording the count faithfully and never once asked whether the counter worked —
  the same shape as the estimate-snapshot daemon that reported *"35 days to go"* while dying (D16).
- **A 🟡PARTIAL is a dated appointment, not a shelf.** Whenever you state a residual ("enters on the
  breakout", "revisit after the 2Q NIM print"), give it an explicit **re-check date** and hand it to
  [carryover](../L2_modules/carryover.md) so the next run re-reads it. An armed condition nobody
  returns to is an idea the desk already paid for and never collected — 475150 was 🟡 with
  "돌파 後" and broke out unattended.
- **A tagged name stays tracked even when its sector rotates out of DEEP.** ALPHA tags follow the
  *name*, not the sector's turn in the rotation; carry them in the next run's inheritance packet.
  Measured: 006360 GS건설 carried an ALPHA tag with **+64.40%** consensus upside and real-hands flow
  on 07-20, then INDU rested and nothing tracked it — **+12.3% over the next five sessions, unowned.**
- **Momentum-only flag**: RS/volume green but the accumulation axis disagrees = tape trade → stamp
  "hard-stop required". ⚠ **Grade the disagreement before acting on it** (carry rule D6): the
  accumulation read is **A-grade** when it comes from KR KIS foreign/institution actuals,
  **B-grade** as a conditional confirmation, and **C-grade when it is only OBV** (r≈0.49 vs real
  flow, **no leading power, t=1.00**). A C-grade disagreement **downgrades to 🟡 and is reported as
  a disagreement** — it does not by itself convert a bet into a tape trade.
- Positioning gate: KR — weak-hands actuals demote even a 🟢 flow; US — ⚡crowded-short is
  turn-conditional squeeze fuel, never a standalone buy (stamp hard-stop).
- (US) `action_bracket` → `ACTION_TICKETS.md`: pre-committed conditional tickets — the pre-mortem's
  both-sides brackets per binary + any cycle-GAP tape-independent core-starter, with DRY-RUN share
  counts. Analysis→ticket conversion; a human executes separately, never the desk.

## ✅ EXIT CHECK
- [ ] Every §B tag filled with evidence label + date; 🔴 dropped AND logged **as a ledger row with a
      reason class, a `--revives-if` condition, AND a `--recheck-date`** (`reject_ledger.py add` —
      the script does not accept the call without both; do not write a rejection you cannot attach
      an expiry to).
- [ ] Every 🟡PARTIAL carries an explicit **re-check date**, and every ALPHA-tagged name is listed for
      carry-forward **independently of whether its sector holds a DEEP slot next run**.
- [ ] Momentum-only and positioning flags stamped where they apply.
- [ ] (US) ACTION_TICKETS.md written (both-sides brackets + core-starter if GAP).
