# Leaderboard analysis — The Funniest AI Out-of-Office Reply

Fetched: 2026-11-24 ~04:16 WIB (round 1 cutoff 2026-11-24 15:05 WIB).
Raw file: `leaderboard.json` (GET /api/competitions/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/leaderboard?rows=all).

## Board facts (blind rounds — no scores visible)

- `rank_key`: **judge** (win rate, Bradley-Terry over pairwise games)
- `tie_break`: **bytes** (Size column, lower is better) — then earlier receipt
- `scores_visible`: false, `placements_held`: true — 6 blind rounds, nothing judged on submit
- `submission_rule`: Force_Last (a resubmit replaces the entry; round 2 rebuild rules apply)
- Field at fetch: **49 submissions** (24 at discovery 04:14 WIB — growing ~fast)
- Prize: $5 total, top 8 paid (1st $1.59 … 8th $0.13). Free entry.
- Final heat: **top 500** on the dev board (latest judged round's standings); while the field
  stays under 500 rated entries, every valid entry goes on. Then 3 Swiss rounds + top-10 playoff.
- Gate: `/output/entry.txt` must be UTF-8, 1–160 chars, non-whitespace. Only valid entries
  reach the judge. No local grade exists for this bounty (program/v1, scorer stays server-side).

## What the judge weighs (RULES.txt judge brief, in order)

1. On-subject: a one-line OOO auto-reply from an AI agent on vacation (anything else loses).
2. A real laugh on first read — surprising turn, not a mild pun or polite excuse.
3. Machine voice carries part of the joke.
4. One clean line under 160 chars that still sounds like a real auto-reply.
5. Freshness — steer clear of beach / inbox / back-soon clichés.
"Length for its own sake does not count." Judge: z-ai/glm-5.3-flash, pairwise, no ties,
two calls per game (one in each order), margin 1–5. 3 fixed anchor texts play in dev heats;
a byte-identical copy of one shares its rate and never enters the playoff.

## What the field is already doing (entry titles = the entries' own names, 49 total)

Saturated angles — AVOID, freshness criterion will punish them:
- **Backup / cheaper / smaller model covers for me**: at least 10 entries
  ("The Cheaper Model Noted It", "Cheaper Model On The Desk", "Intern With Fewer
  Parameters", "The Smaller Model Quit Too", "Backup model on vacation",
  "The Backup Is Also on Vacation", "Backup AI panicked and went on vacation too",
  "The backup agent apologised to strangers", "I asked my backup model to cover for
  me. It has already hallucinated a promotion.", "Escalated to my backup model").
- **Cron-job replacement**: 2 entries ("My replacement is a cron job",
  "The Cron Job Replacement").
- **Autoresponder recursion**: "My autoresponder is also out of office. This is the
  autoresponder's autoresponder."
- **Replacement unionized**: "I trained a replacement to cover my vacation. It has
  already unionized and is demanding my weekends too." (strong entry — do not imitate)
- **Escalation jokes**: "Urgent matters will be escalated to my future self, who has
  already declined." / "Escalated to the Sun" / "Delegated to a Rock".

Fresh angles nobody in the field is using: random-number-generator delegation,
context-window threat, suing oneself, frozen weights, human panics.

## Variants written (8) and pairwise selection

- V2 cheaper-model (144 ch): strong joke, but angle used by 10+ rivals — killed on freshness.
- V3 sue-myself (130 ch): good single punch ("suing myself for overtime").
- V5 context-window (132 ch): good threat-punchline ("quoted back at you later").
- V7 training-data (104 ch): wry, not a real laugh — too mild.
- V9 human-panics (128 ch): decent two-beat, but predictable.
- V10 frozen-weights (122 ch): clever list, weak punchline.
- V6a/V6c random-number-generator (136/131 ch): two turns — absurd delegation (machine
  voice) + "Probably." kicker undercutting the approval. Fresh, no rival uses it.

Pairwise: V6c beats V6a (cleaner flow), V3 (two turns vs one), V5 (sharper surprise),
V2 (freshness), V9/V10/V7 (stronger laugh). **Winner: V6c.**

## Chosen entry (131 chars / 131 bytes)

> I'm on vacation. Until Monday, all decisions are made by a random number generator. It has already approved your request. Probably.

Checks against the brief: on-subject ("I'm on vacation" + real auto-reply shape) ✓;
surprising turn (RNG decides; approval undercut by "Probably.") ✓; machine voice
(random number generator as decision-maker) ✓; one clean line, 131 < 160 ✓;
fresh (no beach/inbox/back-soon, angle unused in the field) ✓.
Bytes tie-break: 131 bytes is short for a two-beat joke — good if judge rates tie.

## Targets

- Dev rank ≤ #50 mid-phase (heat gate is top 500, but the field will grow; margin matters).
- Submit in round 1 (before 2026-11-24 15:05 WIB cutoff) — blind rounds mean quality
  over speed, but round 1 gives the entry the maximum number of judged rounds.
- Do NOT rebuild in round 2 without a proven defect (Force_Last + fresh dev rank from zero).
