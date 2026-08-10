# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-10
**Task**: A325 equation-density review, the second of four passes. Committed, not pushed, not published.

**23 display equations to 42 across ten edits.** 3,695 to 3,788 lines, 14,380 to 14,862 words.
References held at 990 and measured before and after.

---

## What Was Missing

Twenty-three was **the lowest equation count in the series** against a median of 94, and the audit found
the same three categories the previous article did.

**Quoted values with no relation behind them.** The wing loading, the power loading and the weight
fractions all appeared as numbers with nothing shown.

**Relations used throughout and defined nowhere.** The dynamic pressure, the drag equation, range as
endurance times speed, and the full rate-of-climb expression, of which the draft displayed only the
ceiling.

**Whole sections arguing quantitatively with no equation at all.** The worst was **Area Per Dollar, which
is 969 words, is the article's central claim, and displayed nothing whatever.**

---

## The Two Additions That Matter

**The fleet form of the cost argument.** Writing it down shows why the figure of merit is a rate divided
by a price rather than a rate: fleet coverage is the budget multiplied by the area per dollar. Multiplying
up gives 7,200 aircraft covering 741,600 square nautical miles an hour against one Orion's 6,560, and
**the verifier asserts that the fleet route and the ratio route agree exactly rather than within a
tolerance.**

**The random-search law**, which the draft needed and never wrote. **Covering an area once finds 63.2
percent of what is in it**, and that exponential is the quantitative form of the argument the cost
section makes in dollars. It is why patrol aircraft are bought in numbers rather than singly.

Also added: the propeller advance ratio, helical tip speed and a **tip Mach number of 0.776**, which is
where a fixed-pitch propeller wants to be and explains the diameter and the engine speed; the disc
loading and induced velocity from the same momentum balance that gave the static thrust; Archimedes for
a displaced volume of 14.1 cubic feet; and the beam Froude number, the parameter the hump occurs at a
fixed value of.

---

## Verification

**39 to 62 independent checks, all passing, none importing the calculation**, with the helical tip speed
and the monotonicity of detection probability both tested as randomised properties. **All 58 verified
values were required to appear in the draft and all 58 do.**

`_verify.py` at the 21-warning baseline, check_any clean, reference integrity unchanged at 990 with zero
undefined and zero orphaned, and a 29-article isolated build with all 42 equations rendering.

---

## What the Next Pass Inherits

**23 of the 42 equations carry fewer than three citations within reach**, which is the reference base
having to follow the equations for the eighth article running. The newly promoted subjects with no
harvest behind them are **the random-search law and detection probability, propeller advance ratio and
tip speed, momentum-theory disc loading, and the beam Froude number**.

Reported as a target list rather than acted on, since the passes are separate.

---

## Awaiting Instruction

**A325 has completed two of four passes.** The expected next prompt is the primary-reference review.
