# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-11
**Task**: A332, the Lockheed Martin X-35, drafted as
`_drafts/x_planes_lockheed_martin_x35.markdown`, editorial date 2025-11-10, series index 36 of 72.
**Committed, not pushed.** **Not published.**

**18,396 lines, 30 display equations, 5,814 reference definitions, 98,627 words**, with all 5,678
master records cited and none left over. All thirty-six articles remain in `_drafts/`.

---

## The Question the Handoff Set, and the Answer

The handoff asked whether the single sortie that flew a short takeoff, a supersonic dash and a
vertical landing was **evidence or theatre**. It is answerable, and the answer came from the
chronology rather than from the physics.

**Every element of Mission X had already been flown before 20 July 2001.** The first in-flight
conversion to hovering mode happened on **9 July**, on a sortie that also refuelled in the air and
reached **Mach 1.08**. The short takeoff, the wingborne to jet-borne transition and the vertical
landing were all flown on **16 July**, and the programme manager listed them as done, in those terms,
four days before the famous flight.

**Mission X reached Mach 1.05, so it was not even the aircraft's fastest flight.** It contained no
manoeuvre the aircraft had not already performed. **What it contained was the assembly.**

**The arithmetic then says none of the three events was individually demanding.**

- **The short takeoff did not have to be short.** Total vertical thrust is 41,900 pounds force
  against a weight of 34,000, a margin of **1.232**, and the aircraft had already taken off
  vertically eighteen times.
- **The supersonic leg was thermally free.** At Mach 1.05 and twenty-five thousand feet the
  stagnation temperature is **291.2 kelvin**, which is **3.1 kelvin above a standard sea-level day**.
  Thrust to drag at that condition is 2.389.
- **The vertical landing was the easiest of the three**, because it came last and therefore at the
  lowest weight of the day. The ordering alone is worth a factor of **1.115** in margin.

**The expensive event is not one of the three. It is the conversion, which is not in the name of the
trick.** The article says so and then argues against itself in a later section, because a
demonstration also exists to show that separately verified capabilities compose, and that function is
real.

---

## The Result I Did Not Expect

**Not one record in 7,567 harvested carries "X-35" in its title.** Three harvests asked for it
directly, with queries reading "X-35 flight test results", "X-35B STOVL flight demonstration" and
"X-35C carrier variant flight test". The answer was zero every time.

**This is the control case for the pattern A330 and A331 established, and it fails it in an
unexpected direction.** Those two articles found their vehicle's cluster empty after cancellation and
concluded that a cancelled programme stops generating literature under its own name. **The X-35 was
not cancelled. It won.** And its designation has a smaller documentary trace than either of the
cancelled vehicles, because it never had one. Forty records name the Joint Strike Fighter and twelve
name the F-35. **Nothing names the aeroplane.**

**The article states the narrower inference rather than the exciting one.** These were contractor
demonstrators flown for a source selection, which is not the arrangement that produces published
reports, while the X-33 and X-34 were agency programmes with reporting obligations. **So the trace
measures the institution rather than the aircraft**, and the three cases together belong in the
closing article.

---

## The Best Piece of Physics in the Article

**A clutch engaging a stationary inertia to a constant-speed source destroys exactly half the energy
drawn, and the fraction does not depend on how gently it is done.** The impulse fixes the total work
at $I \omega_s^2$ and the inertia keeps half of it. A slow engagement destroys exactly as much as a
violent one.

I verified it by integrating the equations of motion under a constant torque, a linearly rising
torque and an exponentially decaying torque. **The dissipated fraction came back as 0.5 in all
three.**

**The magnitude then comes from a bound that assumes nothing.** At most the rated shaft power flows
for at most the quoted nine-second engagement, so at most 97.3 megajoules can be destroyed, which
would raise twenty kilograms of carbon by about 6,853 kelvin. **The bound is absurd and the absurdity
is the finding.** The real dissipation is between 1.9 and 3.7 percent of rated power spread over
those nine seconds, so **the nine seconds is the time the heat requires, not the time the energy
requires.**

**And counter-rotation turns out to be structural rather than decorative.** Inverting for the fan
speed at which a single-rotation fan's reaction torque would consume the entire roll-post couple
gives thresholds between 2,976 and 4,761 revolutions per minute across the plausible roll-post
positions, and an independent estimate of the fan's speed from its pressure ratio lands at 3,645.
**Across the whole bracket a single-rotation fan would have consumed three quarters to all of the
aircraft's roll authority merely to stand still.**

---

## Two Shared-Library Defects, Both Found by Surveying Characters

**The first manufactured a defect that did not exist.** `refs.clean` collapsed every dash to a space,
so a harvested title reading "jet-jet/film impingement", written with an en dash, became "jet jet",
and the corpus doubled-word check reported a defect against a title that never carried one. **A dash
between two word characters is a compound joiner and now becomes a hyphen**, while a parenthetical
dash still becomes a space.

**The second hid a defect that did exist, and it is the worse of the two.** The corpus contraction
check matches an ASCII apostrophe. A harvested title reading "What's New" written with a right single
quotation mark **sailed straight past a check that exists to catch exactly that word.** `refs.clean`
now normalises typographic punctuation to ASCII before any other rule runs, and also strips the soft
hyphen and stray combining marks. **Diacritics are untouched, because an author's name is not
punctuation.**

Both have regression tests. **`test_lib` is 51 to 53**, and a pre-existing syntax warning in that
file was fixed at the same time, so the suite now runs clean.

---

## Three Errors of Mine, All Caught by the Steps That Exist for Them

**Reading the rendered prose found a factual error.** I wrote that no earlier vertical-landing
aircraft had combined that capability with supersonic flight. **The Yak-141 flew supersonically in
1987 and completed full transitions from 1990.** The claim was wrong and is now corrected, and the
correction improved the article, because the Yak-141 also used a **three-bearing swivel nozzle** and
Lockheed and Yakovlev had a commercial agreement in the early 1990s. **The article now says that the
shaft-driven lift fan is the genuinely new idea and the nozzle behind it has a longer history**,
while declining to settle how much descends from that arrangement.

**Reading also found a rendering defect.** Every cluster marker in my source carried a leading list
dash, and the assembler emits list dashes of its own, so ninety markers rendered as `- - [text]`,
which is a nested list with an empty parent item.

**Checking a citation rather than trusting its status code found a mis-citation.** I had linked
"figure of merit" to a Wikipedia page that returns 200 and **contains no aeronautical content
whatever**. The link is removed rather than repointed, because the article defines the quantity with
an equation on the next line.

---

## The Promotion Rule, Thirteenth Article Running

Auditing the twenty-four subjects the equations name against the pool **before** writing found
**eleven thin and five at literally zero**, including the standard atmosphere, the stagnation
temperature relation, the takeoff ground roll and thrust lapse.

**Seven stay thin after three harvests aimed at them, and the article says which of the three kinds
each one is.** Two are settled knowledge that stopped generating papers, being the ground roll and
the standard atmosphere, which live in every performance textbook and in no journal article. Four are
wrong headings over subjects the pool does hold. One has moved, the modern half of kinetic heating
having gone to hypersonics and left the transonic case behind. **None is padded.**

---

## Verification

- `python3 _verify.py` **0 errors, 21 warnings**, the established baseline.
- `python3 tmp/errata/check_any.py` **0 failures, 0 warnings**.
- `python3 _lib/test_lib.py` **53 of 53**.
- `python3 tmp/a332/verify.py` **53 of 53**, by an independent verifier that does not import the
  calculation. The actuator disc is solved by bisecting the streamtube mass balance, the atmosphere
  by integrating the hydrostatic equation, the stagnation temperature through the energy equation,
  the clutch identity by integration under three torque profiles, the ground roll by time-stepping,
  and three relations as randomised properties over twenty thousand inputs each.
- **Isolated build clean**, 36 series drafts plus the full corpus staged, exit 0, and the rendered
  page carries **zero unexpanded markers, zero nested empty lists, zero blockquotes, zero stray
  delimiters and all fifteen sections in genre order.**
- **All 20 hand-curated reference URLs return 200**, and two were then read rather than trusted,
  which is how the mis-citation was found.
- **60 of 60 sampled DOIs verify against the Crossref registry**, with three honestly declining the
  author check for want of a foldable author.

---

## What I Did Not Do

**I did not push.** The draft pass commits only. **I did not publish, and publication has never been
authorised.** The `post_url` interlock is now **thirty-six deep**.

**The equation count is 30, which is low against the series median of 94, and I am reporting it
rather than padding it.** The subject has one physical chain rather than several, and the
equation-density review is the pass that exists to decide whether more are warranted.

---

## Next

**A332 pass two**, the equation-density review, on your prompt. The obvious candidates are the
transonic drag rise the article asserts rather than derives, the thrust lapse it takes as a power
law, the ground roll it time-steps without displaying, and the fan stage loading that currently
appears only as a sentence.
