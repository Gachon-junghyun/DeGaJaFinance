# L3 · portfolio_beta — regression beta of each holding, and of the book

> One deterministic job: turn daily returns into a beta per position and a weighted book beta.
> Called by L2·mandate. No judgment — it reports a number and a band verdict, nothing else.

## Call
```bash
python -X utf8 -m module_paper_book drift --period 1y            # betas are part of the drift view
python -X utf8 -m module_paper_book drift --json --period 6mo    # machine-readable
```

## What it computes
- **Per position**: `beta = cov(r_i, r_bench) / var(r_bench)` on **daily** returns over `--period`
  (default 1y). Benchmark is the position's own market: **KR → `^KS11`, US → `SPY`**
  (`module_paper_book._allocate.BENCH` is the single source of that mapping).
- **Book beta** = Σ (weight_i × beta_i), where weight is the position's KRW-translated value over
  **total equity including cash**. Cash therefore has beta 0 and damps the book beta on purpose —
  a 40%-cash book is genuinely less exposed than its stock picks suggest. `invested_beta`
  (positions only) is reported alongside so the two are never confused.
- **Band verdict** vs the mandate's `target_beta ± beta_band` (`mandate --target-beta/--beta-band`):
  HIGH / LOW / inside.

## Honesty rules (P4)
- Fewer than 60 overlapping observations, or a symbol yfinance does not return ⇒ **beta is blank**,
  the ticker is listed under `missing_beta`. A blank is never printed as 0.0 and never estimated.
- KR and US betas are measured against **different** benchmarks; blending them into one book number
  is a cross-market approximation useful for *managing against the mandate band*, not a CAPM
  estimate. Say so whenever the number is quoted.
- Beta is backward-looking by construction. A name whose thesis just changed (spin-off, new
  contract, regime break) carries a beta describing the company it *used to be*.
