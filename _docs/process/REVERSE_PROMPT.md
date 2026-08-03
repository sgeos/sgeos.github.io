# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-04
**Task**: Pathological word-usage pass across all twelve History of SpaceX articles. **"specific" reduced from 16,230 occurrences to 44.**

---

## What the Measurement Showed

I compared per-thousand-word rates across the series against a 40-post baseline from the rest of the corpus, which separates a genuine tic from ordinary topic vocabulary.

You were right that `specific` was the problem, and it was worse than the earlier sample suggested. **87.17 per thousand words against a baseline of 1.73 — a factor of 44.** 16,230 occurrences, of which 12,260 were the bare filler `the specific`.

Per-article density before the pass ran from 0.0 in A292 and 0.1 in A291, the two written after the problem was identified, up to **88.4 in A286**.

Three other words cleared the bar for a genuine tic. Everything else that looked elevated turned out to be topic vocabulary — spacex, falcon, launch, capital, venture and so on — and I left those alone.

---

## What Changed

| Word | Before | After | Baseline |
|---|---|---|---|
| specific | 87.17 /1k | **0.20 /1k** | 1.73 |
| compact | 3.62 | 1.85 | 0.02 |
| admits | 4.74 | 2.69 | 0.28 |
| supplies | 1.73 | 0.53 | 0.05 |

**`specific`**: 16,230 to 44 occurrences. Below natural baseline now.

**The equation-introduction formula.** `admits the compact form` and `admits the compact statement` accounted for **429 of 488** equation introductions. Varied across nine alternatives, no single phrase now over 59 instances. Applied only to line-final occurrences preceding a display equation, so sentence-medial uses stayed intact.

**`supplies`** rotated through provides, offers, gives, yields, contributes.

**`configuration`** I deliberately left as domain vocabulary, since 774 of its sentences contain a single occurrence and the series is genuinely about configurations. But 37 sentences used it three or more times, which is just repetitive. I varied the within-sentence repeats only; that count is now 2.

---

## What I Protected

**Technical terms.** `specific impulse`, `specific heat`, `specific thrust`, `specific power`, `specific strength` — stashed before any rule ran so nothing could touch them. All 16 genuine instances survive.

**Contrastive uses.** Kept where the contrast attaches to the same noun phrase, as in "specific X rather than general Y". My first attempt used a proximity window, which was too loose and protected whole regions merely because "rather than" appeared somewhere nearby; I tightened it to require the construction itself.

**Everything structural.** Math blocks, headings, reference bullets, link definitions. Equation counts are identical in all twelve.

---

## Verification

All twelve articles: zero missing, unused, or duplicate anchors; zero duplicate bullets; zero duplicate URLs; balanced LaTeX with matched `\left`/`\right`; **unchanged equation counts**; zero style violations.

Grammar after removal: zero a-before-vowel errors, zero an-before-consonant errors, zero doubled words, zero `the the`. Two flagged "doubled words" were false positives on my part — `lock-in in shaping` and `Falcon Heavy Heavy-Lift Vehicle` are both correct English.

---

## Two Implementation Notes Worth Keeping

**1. My math-skipping logic was silently wrong at first.** It toggled state on lines *beginning* with `$$`, so a block closing with `\end{array}$$` never toggled back and every line after it was skipped. That is why an early run looked like it had plateaued. Rewritten to track delimiters by cumulative count.

**2. The technical-term guard ran too late.** Placed after the determiner rules, it was already defeated — `the specific impulse` had become `the impulse` before the guard saw it, losing 12 of 17 terms. Moved to run before everything else.

Both were caught by verification rather than by reading, which is an argument for checking counts on things you did not intend to change.

---

## Items Requiring Your Attention

1. **The prose reads noticeably better.** The A290 opening paragraph, which previously carried 31 instances of `the specific` in a single line, now reads normally. Worth a spot-read before you publish.
2. **Nothing outstanding blocks publication.** The batch A288 through A292 is ready.
3. **Seven published articles carry uncommitted edits** from this pass and the consistency pass. Publishing will push content changes to live posts either way.

---

## Suggested Next Steps

- Spot-read a couple of the rewritten passages to confirm the register is what you want.
- Stage and publish A288 through A292, with a build verification in a Gemfile-free scratch copy first.
- Consider resolving the 269 Open Library search URLs to specific work identifiers. Citation quality, not link rot.
- Codify the durable handoff process.
