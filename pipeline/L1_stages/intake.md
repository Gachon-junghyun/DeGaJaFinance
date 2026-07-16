# L1 · INTAKE — read the desk's reports (stage)

> Phase 0. Turn the research desks' finished reports into an **actionable thesis ledger** before touching the
> book. No judgment yet — surface every candidate with its report-stamped freshness. Calls L2.
> Output: `INTAKE_LEDGER.md`.

## L2 called
- [report_read](../L2_modules/report_read.md) — `module_paper_book intake` reads `REPORT/` (handoff ledger source)
  + today's `BET_SHEET.md §B` / `ACTION_TICKETS.md`, reusing `module_report_tags` for ticker-universe validation.

## What this stage does
- Extract each actionable name with: **freshness** (🟢LIVE / 🟡PARTIAL / 🔴RESOLVED) · **hard-stop** (if the
  report stamped one) · **theme/section** (the correlation-unit tag) · **★core** flag (epicenter/cycle-GAP starter).
- **Reconcile duplicates across reports**: a name tagged both LIVE (one desk) and RESOLVED (another) is surfaced
  with BOTH sources — DECIDE resolves it, INTAKE never silently drops. The strongest freshness per source is kept.
- Separate the three buckets explicitly: 🟢LIVE (enterable) · 🟡PARTIAL (residual stated) · 🔴RESOLVED (exit/no-enter,
  logged so it can't resurface). List the ★core set (tape-independent).
- ⚠ INTAKE is a *reader*, not a screener — it does not add names the reports never raised. New ideas come from the
  research desks (industry_us/kr etc.), not from here.

## ✅ EXIT CHECK
- [ ] `INTAKE_LEDGER.md` written; every report name captured with freshness + stop + theme + ★core.
- [ ] The three freshness buckets listed; 🔴RESOLVED names logged as no-enter/exit.
- [ ] Cross-report freshness conflicts surfaced (not dropped) for DECIDE to resolve.
