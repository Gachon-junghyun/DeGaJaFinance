# L1 · REBALANCE_PLAN — turn breaches into a deterministic trim/add list (stage)

> Phase 5 of the wrap desk. The mandate says where the book should be, DECIDE has said which names may carry
> each sector — this stage produces the **numbers**: who is trimmed, who is added, by how much, to what weight.
> Calls L2. Output: `REBALANCE_PLAN.md` (+ `out/paper_book/WRAP_REBALANCE_{date}.json`).

## L2 called
- [mandate](../L2_modules/mandate.md) — `module_paper_book rebalance [--to target|band] [--fx r] [--json]`:
  legs (ticker · side · qty · price · KRW amount · weight before→after), unfilled gaps, post-plan concentration.
- [risk_model](../L2_modules/risk_model.md) — the caps the plan must respect are the *same* ones sizing uses
  (`MAX_POS_PCT` single-name, `MAX_THEME_PCT` correlated theme); the plan re-runs `concentration_check` on the
  **projected** book, so a rebalance can never fix a sector by breaking the correlation guard.

## What this stage does
- **Trims are deterministic**: inside an overweight sector the module sells the **weakest** name first —
  smallest distance-to-stop, ties broken by size. The desk does not get to protect a favourite by feel; if it
  wants a different name trimmed, it must say so as a DECIDE verdict and record why.
- **Adds go to held names first**, largest distance-to-stop first (add to what is working, not to what is
  bleeding), capped by the single-name ceiling.
- **`NEEDS_CANDIDATE` is the handoff, not a failure.** An underweight sector with no holding — or one where the
  held names cannot absorb the gap — returns the amount and stops. Fill it from the INTAKE ledger's 🟢LIVE names
  for that sector, sized by the SIZE stage's risk model; if the reports offer none, the honest outcome is to
  carry the underweight and say so. **Never invent a ticker to satisfy a weight.**
- **Mind the sleeve.** Cash is held per currency (KRW / USD) and the paper book has no FX-conversion primitive:
  a KRW-heavy cash pile cannot fund a US add. If a leg is cash-blocked, report the sleeve balance and treat the
  sleeve transfer as a human decision, not an assumed one.
- `--to target` restores fully (institutional default); `--to band` restores only to the band edge (cheaper,
  more residual drift). State which was used and why.
- ⚠ A plan is not an instruction. Nothing reaches the book until the SIMULATE stage is run with `--commit`
  by a human. No scheduler ever runs this stage.

## ✅ EXIT CHECK
- [ ] `REBALANCE_PLAN.md` written: every breached sector either has legs or an explicit `NEEDS_CANDIDATE` gap.
- [ ] Each leg shows qty · price · amount · weight before→after, and the rule that selected the name.
- [ ] Post-plan concentration re-checked (single-name + theme); any projected breach resolved or stated.
- [ ] Cash-blocked legs name the sleeve and its balance; `--to` mode stated.
