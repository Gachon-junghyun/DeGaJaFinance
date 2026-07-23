# L2 · schedule — timing (orchestration)

> Called by L1s. "When does it fire" — catalyst dates, narrative age, kill-switch bursts.

## Calls
- Catalyst calendar — `python -X utf8 scripts/catalyst_calendar.py --days 5`
  (🔀binary macro prints + earnings clusters; ✓=official-source confirmed vs ~=pattern-estimate —
  verify the ~ ones). ⚠ saves `CATALYST_WATCH.json` under the day-folder ROOT.
  **Any binary ≤48h ⇒ the pre-mortem MUST bracket it both ways** (one-way tilt into a known binary
  = protocol violation).
  ⚠ **Do not stop at `--days 5` when `SCENARIOS.md` already names a date beyond it.** Measured
  2026-07-23 (dig D26): 2026-07-29 had been carried as "the single most loaded date on the calendar"
  (S2) for at least a week of runs, but the 5-day default never reaches it — a **10-day** re-pull on
  that same date surfaced a fifth 07-29 event (a financial-holdco governance reform) that had never
  been registered anywhere, sitting on the desk's own continuously-OW sector. **A 5-day pull that
  never cross-checks its own window against `SCENARIOS.md`'s already-armed dates is not a complete
  schedule read.** Run `--days 10` (or further, to the furthest ARMED date inside ~2 weeks) whenever
  any `ARMED` row's date sits beyond the default window, not only when something feels incomplete.
- Theme age — `python -X utf8 -m module_news_data theme-age "<theme>" --scope foreign`
  (🟢FRESH ≤14d+accel / 🟡ACCELERATING / ⚪ECHO / 🔴FADING — deterministic novelty BEFORE spending WebSearch).
- Kill-switch burst — `python -X utf8 scripts/drift_watch.py --report <MACRO_REPORT path>`
  (post-run regime-flip early warning; 🚨 → body-read, then append-only ADDENDUM).
- If no calendar is wired for a future event: write the catalyst as `[blank]` — never guess a date.

## Output
Imminent catalysts + FRESH/ECHO priority + any post-run burst.
**The calling L1 uses it for timing and for both-sides discipline.**
