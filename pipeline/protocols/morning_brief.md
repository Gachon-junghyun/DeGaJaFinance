# PROTOCOL — morning_brief

> A protocol = an ordered composition of L1 blocks (references only). **Order is owned by this file**
> (L1 units are independent). Purpose: publish a **pre-open reader brief** at 08:30 KST from what the
> research desks already produced — no new research, no recommendation.
> Output root `llm_outputs/{YYYY-MM-DD}/morning_brief/`. Runtime: KR reader by default.

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
