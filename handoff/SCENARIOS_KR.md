# SCENARIOS_KR — pointer (KR half)

> **What this is.** Since 2026-10-31 the KR desk's pre-registered questions live in the `module_lens` ledger,
> not here. **When to read:** never in full — read [`SCENARIOS.md`](SCENARIOS.md) and run `module_lens due`.
> **Not here:** the bracket prose (205 KB) — byte-identical in [`_archive/2026-10-31/SCENARIOS_KR.md`](_archive/2026-10-31/SCENARIOS_KR.md).

- Register: `python -X utf8 -m module_lens ask … --market KR --desk industry_kr` (protocol: `pipeline/L2_modules/lens.md`).
- Score: `module_lens score` → `due` at HANDOVER; the ledger lists both markets — a past-due US row is yours too.
- Old ID → Q: `module_lens find S###` (legacy `S` IDs; `-KR` suffix dropped). ⚠ `P###` / `M-###` and colliding `S##-KR`
  rows were **not** migrated — the still-open ones are listed in `SCENARIOS.md` §"NOT in the ledger".
- Need the old narrative of a bracket: `grep -n "S###" handoff/_archive/2026-10-31/SCENARIOS_KR.md`.

## Change log
- 2026-10-31 — replaced by this pointer (orchestra branch K3).
