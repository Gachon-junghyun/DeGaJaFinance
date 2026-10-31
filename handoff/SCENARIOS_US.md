# SCENARIOS_US — pointer (US half)

> **What this is.** Since 2026-10-31 the US desk's pre-registered questions live in the `module_lens` ledger,
> not here. **When to read:** never in full — read [`SCENARIOS.md`](SCENARIOS.md) and run `module_lens due`.
> **Not here:** the bracket prose (565 KB) — byte-identical in [`_archive/2026-10-31/SCENARIOS_US.md`](_archive/2026-10-31/SCENARIOS_US.md).

- Register: `python -X utf8 -m module_lens ask … --market US --desk industry_US` (protocol: `pipeline/L2_modules/lens.md`).
- Score: `module_lens score` → `due` at HANDOVER; the ledger lists both markets — a past-due KR row is yours too.
- Old ID → Q: `module_lens find S###` (legacy `S` IDs; `-KR` suffix dropped). ⚠ `P###` / `M-###` and colliding `S##-KR`
  rows were **not** migrated — the still-open ones are listed in `SCENARIOS.md` §"NOT in the ledger".
- Need the old narrative of a bracket: `grep -n "S###" handoff/_archive/2026-10-31/SCENARIOS_US.md`.

## Change log
- 2026-10-31 — replaced by this pointer (orchestra branch K3).
