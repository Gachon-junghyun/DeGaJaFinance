# L1 · ROTATION — sector rotation (stage)

> Phase 1. Transmission matrix × flow sweep → rank the 11 GICS sectors OW/UW and pick the
> **N DEEP targets** (**N is set by the protocol** — us:4, kr:2). Calls L2.
> Output: `SECTOR_ROTATION.md` (+ a `DEEP_LOG {date}:` line).

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

   🚨 **AND the flow number must survive removing the sector's largest name** (added 2026-08-10).
   `wflow` is **market-cap weighted**, so in a concentrated bucket it is one company wearing a sector
   label. **Measured on the KR board: 10 of 26 sectors (38%) FLIP SIGN when their top-1 name is
   removed** — 전기·가스 −0.046 → **+0.468** (한국전력 = **79.9%** of a 10-name bucket) ·
   보험 −0.049 → +0.384 (삼성생명 53.4%) · 통신 +0.198 → **−0.180** (SKT 48.2%) ·
   금융 −0.046 → +0.236 (SK스퀘어 26.5% **of 75 names**) · 유통 −0.046 → +0.154 (삼성물산 52.7%).
   `SECTOR_FLOW.json` now carries `top1` · `top1_w` · `wflow_ex_top1` · `top1_flips_sign` per sector,
   and the text render marks flippers **🚨1名**.
   ⇒ **A 🚨1名 bucket may not carry a promotion or a demotion.** Either cite `eqflow`/breadth
   instead (they are not cap-weighted) or state that the sector's number is one name and leave the
   verdict where MACRO put it.
   ★ **Concentration is not the same as a flip, and the field distinguishes them**: 삼성전자 is
   **45.6%** of 전기·전자 but the sector stays negative without it (−0.433 → −0.547) ⇒ **not** a
   flipper. Do not reject a bucket for being top-heavy; reject it for being *sign-dependent* on one name.
   ⚠ This is dig **D9**'s sector face (the holdco/subsidiary mix-up is its book face) — KRX also
   classifies holdcos as *financials*, which is how `SK스퀘어` came to own the 금융 bucket's sign.
3. **§3 DEEP picks + DEEP_LOG** — the real deliverable (rule below).

**Name every AGREE / DIVERGE explicitly** — but AGREE is the one-line §1, not eleven paragraphs:
  (a) matrix-OW but flow-absent = "right thesis, money not here yet" → rotate DOWN a notch,
      and make the divergence the #1 question the DEEP stage must resolve (early vs trap);
  (b) flow-led sector the matrix under-rated = promote (money moved before the thesis — treat as
      confirmation, note breadth: wflow≫eqflow = mega-cap-narrow, not broad strength);
  (c) new-🟢 ignition anywhere = early-cycle tell → consider watch-promote.
  ⚠ Remember the sweep is asof the previous close — a same-day catalyst is not in it yet.
- **N-DEEP selection rule (never by gut).** ★ **N is owned by the protocol, not by this stage** —
  `industry_us` sets **N=4** (2 continuous + 2 rotating), `industry_kr` sets **N=2** (1 + 1).
  Read your protocol's "DEEP budget" line before selecting; if it is absent, default to N=4.
  ① *Continuous-track ⌈N/2⌉* = today's top OW ranks. Anti-thrash continuity: a sector that held a
    continuous slot in the previous run AND is still top-N OW today KEEPS the slot (state it).
  ② *Rotating ⌊N/2⌋* = next-highest OW not deep-dived in the last ~3 runs (read DEEP_LOG lines).
    If every OW was recently covered → fallback to next-highest OW regardless, and SAY
    "recency-starved"; a least-recently-covered tiebreak between adjacent OW ranks is allowed if stated.
  Never pad with Neutral/UW to reach N — fewer is fine if stated.
  ⚠ **When N is small the un-covered OW sectors do not vanish — they get logged.** Append the OW
  sectors that did NOT get a DEEP slot to the DEEP_LOG line so the next run's recency rule can see
  them, and so "we never looked" is distinguishable from "we looked and passed" (the same asymmetry
  `missed_ledger` exists to close).
- Append `## DEEP_LOG {date}: continuous=[X,Y] rotating=[Z,W]` — next run's recency input.

## ✅ EXIT CHECK
- [ ] **§1 is ONE line** inheriting MACRO's matrix verbatim. No sector that is unchanged gets its own
      row, paragraph, or restated flow number.
- [ ] **Every §2 delta cites a flow number** (wflow/eqflow/breadth/Δ). Any change justified only by a
      macro argument is reverted to MACRO's verdict and the attempt logged as "macro re-argument, declined".
- [ ] 🚨 **No promotion or demotion rests on a `top1_flips_sign` bucket.** Every delta on a 🚨1名
      sector either switches to a non-cap-weighted number (eqflow/breadth) or is declined with
      *"this sector's sign is `<name>` at `<top1_w>`%"* written out. The flip list is reproduced in §2
      even when it changes nothing — a silent flipper is how one company becomes a sector call.
- [ ] **The axis count this run scored on is stated** (`SECTOR_FLOW.json §scoring.n_axes`). If the
      news axis was dropped (coverage < 80%), **no delta may cite theme freshness or news velocity**,
      and Δ vs the prior snapshot is only read against a snapshot of the same axis count.
- [ ] Every matrix×flow divergence named with a resolution owner (DEEP).
- [ ] N DEEP targets picked by the rule at the protocol's DEEP budget (continuity + recency stated
      where applied); no padding. **OW sectors left without a slot are named in DEEP_LOG**, not dropped silently.
- [ ] **Linter run on this stage's own output** — `python -X utf8 scripts/report_lint.py <written file>`. Every finding is fixed or the paragraph carries its rule ID with a stated reason for exemption. ⚠ It checks form only (C1 benchmark · C2 both halves · S6 future label · D6 OBV-alone); a clean run is not a correct report.
- [ ] DEEP_LOG line appended for the next run.
- [ ] ⚠ If the delta count is 0, the correct output is a **short file saying "flow confirms the matrix
      on all 11"** plus the DEEP picks. That is a valid, informative run — not a reason to manufacture
      differences.
