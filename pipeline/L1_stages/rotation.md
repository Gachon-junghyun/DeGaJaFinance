# L1 · ROTATION — sector rotation (stage)

> Phase 1. Transmission matrix × flow sweep → rank the 11 GICS sectors OW/UW and pick the
> **4 DEEP targets**. Calls L2. Output: `SECTOR_ROTATION.md` (+ a `DEEP_LOG {date}:` line).

## L2 called
- [indicators](../L2_modules/indicators.md) — news velocity recount (corroborant only — raw term
  counts are frequency noise; the flow sweep replaced them as primary intensity).
- [deepdive](../L2_modules/deepdive.md) — `module_industry_map` industry-map reference.

## What this stage does

### ★ Delta-only. Do not re-print the matrix.
MACRO already owns the 11-sector verdict; `SECTOR_FLOW.json` already owns the flow numbers. Both are
on disk for the whole run. **This stage writes only what changes and why.**

⚠ **Measured 2026-07-21**: of 9 comparable sectors, **8 came out identical to MACRO's transmission
matrix** — a 14KB file whose actual output was **2 verdict changes** (IT → UW, RE → Neutral). The
other 82% was restatement. Structure the file so that cannot happen:

1. **§1 Inherited — one line, verbatim from MACRO §4.** e.g.
   `MACRO holds: ENRG OW+ · FIN OW · HLTH OW · INDU N · COMM UW · STPL N · UTIL N · MATR UW`.
   No re-derivation, no per-sector prose for anything that is not changing.
2. **§2 Deltas only** — one row per sector where the money disagrees with the thesis:

   | sector | matrix said | flow evidence (wflow · eqflow · breadth · Δd/d · 🟢/🔴) | new verdict | who resolves |

   ★ **A delta must be carried by a flow number.** Re-arguing the macro thesis is **not** a delta —
   that is MACRO's job and doing it here duplicates the stage and degrades it (this stage has worse
   macro inputs than MACRO does). If the only reason to move a sector is a macro argument, **leave it
   and say so**. *Measured*: the 2026-07-21 RE change cited "3 runs of flow divergence **+ real-10Y
   easing**" — the second half was a macro re-argument and does not qualify.
3. **§3 DEEP picks + DEEP_LOG** — the real deliverable (rule below).

**Name every AGREE / DIVERGE explicitly** — but AGREE is the one-line §1, not eleven paragraphs:
  (a) matrix-OW but flow-absent = "right thesis, money not here yet" → rotate DOWN a notch,
      and make the divergence the #1 question the DEEP stage must resolve (early vs trap);
  (b) flow-led sector the matrix under-rated = promote (money moved before the thesis — treat as
      confirmation, note breadth: wflow≫eqflow = mega-cap-narrow, not broad strength);
  (c) new-🟢 ignition anywhere = early-cycle tell → consider watch-promote.
  ⚠ Remember the sweep is asof the previous close — a same-day catalyst is not in it yet.
- **4-DEEP selection rule (never by gut):**
  ① *Continuous-track 2* = today's top-2 OW. Anti-thrash continuity: a sector that held a
    continuous slot in the previous run AND is still top-4 OW today KEEPS the slot (state it).
  ② *Rotating 2* = next-highest OW not deep-dived in the last ~3 runs (read DEEP_LOG lines).
    If every OW was recently covered → fallback to next-highest OW regardless, and SAY
    "recency-starved"; a least-recently-covered tiebreak between adjacent OW ranks is allowed if stated.
  Never pad with Neutral/UW to reach 4 — fewer is fine if stated.
- Append `## DEEP_LOG {date}: continuous=[X,Y] rotating=[Z,W]` — next run's recency input.

## ✅ EXIT CHECK
- [ ] **§1 is ONE line** inheriting MACRO's matrix verbatim. No sector that is unchanged gets its own
      row, paragraph, or restated flow number.
- [ ] **Every §2 delta cites a flow number** (wflow/eqflow/breadth/Δ). Any change justified only by a
      macro argument is reverted to MACRO's verdict and the attempt logged as "macro re-argument, declined".
- [ ] Every matrix×flow divergence named with a resolution owner (DEEP).
- [ ] 4 DEEP targets picked by the rule (continuity + recency stated where applied); no padding.
- [ ] DEEP_LOG line appended for the next run.
- [ ] ⚠ If the delta count is 0, the correct output is a **short file saying "flow confirms the matrix
      on all 11"** plus the DEEP picks. That is a valid, informative run — not a reason to manufacture
      differences.
