# PROTOCOL — paper_desk

> A protocol = an ordered composition of L1 blocks. **Order is owned by this file** — L1 units are
> independent and do not know their sequence. L1s are **referenced only** (content lives in each L1 file).
> Purpose: read the desk's own finished reports and **run a simulated book as a professional PM** —
> size by risk, simulate fills, mark-to-market, journal. **Paper only: no real order is ever sent.**
> Output root `llm_outputs/{YYYY-MM-DD}/paper_desk/`. Runtime `--market us|kr|all` (P3 auto-detects by ticker).

## What this desk is (and is NOT)
- **IS:** the *consumer* of the research desks. It reads `REPORT/` (industry_us/kr, company, real_alpha…)
  and today's `BET_SHEET.md §B` freshness tags + `ACTION_TICKETS.md` brackets, then decides ENTER/ADD/
  HOLD/TRIM/EXIT and books the result in a **simulated ledger** (`data/paper_book.db`).
- **IS NOT:** a live trader. Fills are simulated; `--commit` only writes the *paper* ledger. There is no
  `--execute`, no broker call, no scheduler auto-fire (P5 라이브 보호). Real orders stay human + `module_KIS`.
- **Division of labor (P4):** `module_paper_book` supplies the deterministic mechanics (intake, sizing,
  fills, marks, journal). **The judgment — which theses to back and with what conviction — is THIS protocol's
  DECIDE stage.** The module never decides; the desk never re-implements the module's math.

## File-output rules
- Run outputs → `llm_outputs/{date}/paper_desk/`: `INTAKE_LEDGER.md` · `BOOK_STATE.md` · `DECISIONS.md` ·
  `ORDERS.md` · `FILLS.md` · `PAPER_JOURNAL.md`. Previous dates are read-only (append-only corrections).
- The book itself is the single source of truth: `data/paper_book.db` (`PAPER_BOOK_DB_PATH` to relocate).
- No secrets in any output. Every derived number is module-computed (no eyeballed figures).

## Composition (L1 order)

| # | L1 block | Output |
|---|---|---|
| 1 | [INTAKE](../L1_stages/intake.md) | `INTAKE_LEDGER.md` (actionable theses: freshness · stop · theme · ★core) |
| 2 | [MARK](../L1_stages/mark.md) | `BOOK_STATE.md` (equity · cash · per-position P&L · stop-hits · theme exposure) |
| 3 | [DECIDE](../L1_stages/decide.md) | `DECISIONS.md` (per name: ENTER/ADD/HOLD/TRIM/EXIT + conviction) — **the judgment** |
| 4 | [SIZE](../L1_stages/size.md) | `ORDERS.md` (risk-based share counts + stops + concentration caps) |
| 5 | [SIMULATE](../L1_stages/simulate.md) | `FILLS.md` + updated `paper_book.db` (DRY-RUN unless `--commit`) |
| 6 | [REVIEW](../L1_stages/review.md) | `PAPER_JOURNAL.md` (decision journal + track record + portfolio review) |

## Runtime deltas
- **`--market`**: `us` (yfinance marks), `kr` (`module_KIS` marks + KIS balance cross-read), `all` (both sleeves).
- **Discipline carried from the research desks:** a 🔴RESOLVED tag ⇒ no ENTER + EXIT if held (so "it's cheap"
  can't resurface). A ⚡crowded-short / momentum-only stamp ⇒ hard-stop mandatory. The premortem's
  **"one risk unit"** correlation flag ⇒ the correlated basket is sized as ONE position, not several.
- **Epicenter ★core** candidates (cycle-GAP starters) are tape-INDEPENDENT: they may be entered regardless of
  the tape, at `--core` risk %, while the tape gates only the discretionary adds.

**Start → read [INTAKE](../L1_stages/intake.md) and execute.** Advance only after each L1's EXIT CHECK passes.
Finish with [handoff](../handoff.md) to fold the paper journal into the tag ledger.
