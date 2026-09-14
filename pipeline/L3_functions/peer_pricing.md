# L3 · peer_pricing — what is the market actually pricing this name as?

> **Single-role unit.** Independent — no ordering; an L2/L1 calls it when needed. Does ONE thing:
> take one name and **two or more competing frames** (each frame = a set of pure-play peers), then
> measure which frame the tape moves with. It answers *"what does the market think it is buying?"* —
> which is a different question from *"what is the company?"* ([segment_pnl](segment_pnl.md)) and from
> *"what drives the earnings?"* ([driver_link](driver_link.md)).

## Method (deterministic)
1. Name the frames from the segment table — one frame per segment large enough to matter (≥10% of level).
2. For each frame pick **2+ liquid pure-plays** that are *not* the subject and not each other's parent.
3. Pull adjusted closes; report per peer: 20/60/120-day return **and** daily-return correlation with the
   subject over 20d and 60d.
4. The frame with the highest correlation **and** the closest return path is the frame the market is using.

## What it caught, both directions (measured 2026-08-21, PSX)

| frame | peers | 20d | corr(20d) |
|---|---|---:|---:|
| **refiner** | VLO / MPC / DINO | +14.0 / +17.0 / +6.8% | **+0.900 / +0.869 / +0.766** |
| midstream | OKE / TRGP / WES | +3.6 / +6.2 / +4.6% | +0.584 / +0.469 / +0.489 |
| *(subject)* | **PSX** | **+18.9%** | — |

**(a) It killed a false alpha.** The desk had observed that PSX rose **+18.8% over 20 days while its
roll-adjusted crack was flat (−1.0%)**, and read that gap as a PSX-specific re-rating. The peer row
shows VLO, MPC and DINO all did the same thing in the same window. **A move the whole peer set shares
is sector beta, not name alpha** — and it had already been written up as the latter.

**(b) It located a real, unpriced asset.** Midstream + Chemicals + Renewable Fuels are **~35% of PSX's
pre-tax income**, and NGL export was the **only accelerating theme** on the board (`theme-age` 🟡ACCEL,
4.29× — every refining term was ⚪ECHO). Correlation with the midstream frame is **+0.47~0.58**: the
market is not pricing that third of the company at all.

## ⚠ Two guards
- **A frame gap is a question, not an entry.** "The market does not price segment X" is compatible with
  *"and it never will"* and with *"the segment does not actually earn what its share suggests"*. The
  unit produces a dated observation point (*"does corr(subject, frame-B) rise?"*), never a buy.
- **Correlation is a frame test, not a causal one.** Two frames inside one sector share macro factors.
  Report the correlation **spread between frames**, not a single frame's absolute level.

## Output
`frame · peers · each peer's 20/60/120d return · corr(20d) · corr(60d) · Δ(20d−60d)` + one line naming
the dominant frame + one line naming any frame whose share of earnings exceeds its share of the tape.
No verdict (P4).
