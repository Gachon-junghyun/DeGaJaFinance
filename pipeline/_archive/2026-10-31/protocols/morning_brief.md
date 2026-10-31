# PROTOCOL — morning_brief

> A protocol = an ordered composition of L1 blocks (references only). **Order is owned by this file**
> (L1 units are independent). Purpose: publish a **pre-open reader brief** at 08:30 KST from what the
> research desks already produced — no new research, no recommendation.
> Output root `llm_outputs/{YYYY-MM-DD}/morning_brief/`. Runtime: KR reader by default.

## ★ Whose morning is it — the rule that sets everything downstream

**The reader is in Korea, so the domestic pool is the spine and each foreign row earns its place by
having been printed for domestic readers.** Build it that way from the gather stage on; every later
stage inherits the frame it is handed.

**Why this needs saying out loud** (measured 2026-07-24): the overnight foreign pool held **810 market
events** against the prior domestic session's **357**, off **5,576 foreign articles vs 3,093 domestic**.
**The foreign pool is larger by construction, every single day** — a US session simply produces more
indexed English copy than a KR session produces Korean copy. So ranking candidates by event size
hands the editorial line to the wrong market **by default**, not by mistake. That run's first draft
did exactly that and the user corrected it: *"너무 외국 중심이야 한국 풀에서 놀아야 해."*

**And the correction cost nothing.** Rebuilt domestic-first: **8 of 15 published items were
domestic-origin**, and the remaining **7 were foreign-origin — every one of which a Korean outlet had
already printed (7/7)**. The separate foreign event pass contributed just **5 candidate rows of 810
(0.6%)**, and only two of those added anything the domestic pass had not already delivered.

★ **That is the finding worth carrying forward**: the overnight facts a KR reader needs — oil through
$100, the US close, an earnings surprise, a chip roadmap — **reach the domestic pool by 08:30 anyway**.
So the domestic-print test loses no information; it is the same test doing three jobs at once —
relevance to this reader, a date check in this reader's timezone, and the figures the English wires
drop (measured that morning: 두바이유 90달러선 and 원·엔 900원선 appeared **only** in Korean copy).

⇒ Carried as trigger **W6** in `handoff/RESEARCH.md`, and enforced in the gather, rank and render
EXIT CHECKs below.

## ★ The three skips this protocol now hard-gates (all measured 2026-07-25)

The rules below were **already written** when this run tripped over all three — the failure was
executing the clustered event passes and stopping, not a missing rule. So the fix is enforcement, not
prose: each is now a blocking EXIT CHECK line with this run as its anchor.

1. **The occurrence-dating WebSearch pass got skipped entirely** → a 07-24 (US Friday) event was
   dated to "주말 새벽", and an unverified *"다우 +360"* shipped. *(gather: dating pass must actually run.)*
2. **Overnight numbers were paraphrased from a cluster, not pulled** → "다우 +360" (wrong, Dow-only)
   hid Nasdaq −0.6% on an AI sell-off. *(gather settle-rule + render: all three indices, sourced.)*
3. **The day was over-cut to 12 items** because the run stopped at the default single-outlet view →
   HMM 8조, the 1,500억달러 조선동맹, and the Samsung 3Q memory-price boycott all sat in the deeper
   1-outlet tier, uncut only after `--singles-nb` was lowered. *(gather: mine the tier; rank: 15 is a
   target, defend every empty slot.)*

★ **The meta-lesson**: a well-specified prompt still fails if a stage runs the cheap path and calls
it done. These three EXIT CHECKs are phrased so "the rule was read" is not a pass — the pass is the
pull, the count, and the third index actually being on the page.

## What this desk is (and is NOT)
- **IS:** a *publication* desk, the same class as paper_desk — a **consumer** of finished output. It
  reads the previous run's industry desk files, the overnight foreign event pass, and today's
  calendar, then emits one file a person reads on a phone before the market opens.
- **IS NOT:** research. It derives no new number, forms no view, and names no trade. If a fact is not
  already established and publicly sourced, it does not appear.
- **The one hard constraint:** every line must be checkable by someone who has never seen this repo.
  Our filenames are where we wrote a fact down, not where it came from — the render stage's ban list
  and the public_source function exist to enforce exactly that.

## Composition (L1 order)

| # | L1 block | Output |
|---|---|---|
| 1 | [BRIEF_GATHER](../L1_stages/brief_gather.md) | `BRIEF_POOL.md` (candidate facts · origin · asof session · 08:30 availability) |
| 2 | [BRIEF_RANK](../L1_stages/brief_rank.md) | `BRIEF_RANK.md` (ordered ~15 + cut list with counts) |
| 3 | [BRIEF_RENDER](../L1_stages/brief_render.md) | `MORNING_BRIEF.md` ← **the published artifact** |

## Runtime notes
- **Timing.** 08:30 KST, KRX pre-open. The gather stage owns the availability rule; the short version
  is that today's KR price, flow and domestic news do not exist yet, and the overnight US session
  does. A brief that quotes a mid-session figure is wrong even when the figure is right.
- **Input date.** The desk run it reads is the **previous** one; the calendar and the overnight window
  are today's. These are different dates and both belong in the file's own header line.
- **Length.** ~15 items, more when the day is loaded — but the cut count is always written.
- **Nothing is scheduled to fire from here.** The brief is generated and a human posts it (P5).

**Start → BRIEF_GATHER, pass its EXIT CHECK, then rank, then render.** The render stage's ban-list
sweep is a grep, not a judgment call — run it before the file leaves the folder.
