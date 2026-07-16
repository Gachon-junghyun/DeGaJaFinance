# L3 · competitors — competitors & value-chain neighbors

> **Single-role unit.** Independent — no ordering; an L2 calls it when needed. Does ONE thing.

- **Role**: extract a company's competitors/value-chain neighbors and fix its relative position
  (bottleneck node? beneficiary node?).
- **Input**: ticker · sector thesis terms · (optional) peer codes.
- **CLI**:
  ```bash
  python -X utf8 -m module_industry_map "<sector thesis terms>"                # chain nodes 5–8
  python -X utf8 -m module_valuation <ticker> --peers <peer1>,<peer2>          # relative multiples
  python -X utf8 -m module_business <ticker>                                   # business reality check (US = module_business_us --json)
  ```
- **Output**: competitor list + bottleneck-node position + peer-relative multiples
  (a de-rated lane vs peers = open alpha, if the business check supports it).
