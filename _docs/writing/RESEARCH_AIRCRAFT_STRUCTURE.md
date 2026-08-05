# Research Aircraft Structure

> **Navigation**: [Writing](./README.md) | [Documentation Root](../README.md)

Section structure for the research-aircraft genre, a hybrid of the subsystem deep-dive and the analytical essay. Established by the X-Planes series at A297 through A368. See [Article Genres](./ARTICLE_GENRES.md) for genre identification.

## Why a Hybrid

Neither existing genre fits a research aircraft on its own.

A research aircraft exists to answer one question. The Bell X-1 exists to measure transonic drag rise, the North American X-15 to fly hypersonically and survive the heating, the Grumman X-29 to determine whether forward-swept-wing aeroelastic divergence can be controlled rather than avoided. That question behaves exactly like the architectural keystone of a [subsystem deep-dive](./SUBSYSTEM_DEEPDIVE_STRUCTURE.md), because the airframe, the propulsion, the structure, the control system, and the instrumentation were each dimensioned against it.

But an aircraft is also a programme with an origin, a political context, a flight-test record, and a consequence, and it frequently carries claims the historical record does not settle. Those belong to the [analytical essay](./ANALYTICAL_ESSAY_STRUCTURE.md), whose Epistemic State convention exists precisely for mixed certainty. The keystone template has no slot for them.

The hybrid takes the keystone as the technical spine and the essay as the historical frame. Neither is decorative. An article that dimensions systems without saying what the programme was for reads as a specification sheet, and one that narrates the programme without dimensioning anything reads as a magazine profile.

## Section Order

1. Opening prose with no heading. Name the aircraft, state the research question in one sentence, and cross-link the series opener and any companion articles.
2. `## The Research Question` section naming the keystone and explaining why it was the binding unknown at that moment rather than a general statement of interest.
3. `## Programme Origin` section covering who wanted the answer, who paid, and what institutional arrangement produced the aircraft.
4. `## Sizing From First Principles` section deriving the keystone relationship, defining each symbol in prose immediately before its equation, and giving a worked numerical example with a concrete result.
5. `## Dependent Systems` section with one subsection per system dimensioned against the keystone. Aerodynamics, propulsion, structure and materials, control, and instrumentation are the usual set. Order by dependency, not by convention.
6. `## The Flight Test Record` section stating what was actually flown, how many flights, what was measured, and what failed. Distinguish the flight envelope reached from the envelope designed for.
7. `## What the Data Changed` section identifying what the programme settled, what it fed into, and what it failed to influence. An aircraft whose data changed nothing is a finding, not an omission.
8. `## Where the Framing Breaks Down` section naming cases where treating this aircraft through its keystone misleads.
9. `## Epistemic State` section per the [analytical essay convention](./ANALYTICAL_ESSAY_STRUCTURE.md#the-epistemic-state-convention). Required without exception. Sort claims into historical fact, engineering analysis, and inference, and name any claim the record does not settle.
10. `## Out of Scope` section enumerating deferred topics.
11. `## Conclusion` section summarising what the aircraft answered.
12. `## References` section with the sorted, categorized reference index.

## The Three Article Classes

Depth is a function of the surviving record, not of the author's diligence. Three classes are recognised, and an article should state which it is rather than pad toward the largest.

| Class | Lines | Display equations | References | Sections |
|-------|-------|-------------------|------------|----------|
| Full aircraft | 1,300 to 1,600 | 60 to 80 | 250 to 380 | The full order above |
| Documentation-poor | 150 to 400 | 0 to 15 | 20 to 60 | Full order, short sections, explicit statement of what is unknown |
| Designation anomaly | 40 to 150 | 0 to 2 | 8 to 30 | Reduced order, see below |

The full-aircraft figures are the History of SpaceX medians and are descriptive rather than prescriptive. Do not pad an article to reach them. Do not strip one to stay under them.

### Designation Anomalies

Some designations were refused, reserved and never assigned, skipped, duplicated, or leapfrogged. For these the subject is the number rather than an aircraft, so there is no keystone to identify and no system to dimension. Use a reduced order.

1. Opening prose naming the designation and the anomaly.
2. What happened, with dates and the deciding authority where the record gives them.
3. Why, if the record says.
4. What the anomaly reveals about the designation system.
5. `## Epistemic State`.
6. `## References`.

An article stating that the X-52 designation was requested in 2006, was refused because of possible confusion with the B-52, and that the programme became the X-53 is complete at that length. Padding it with an Out of Scope section it does not need is worse than leaving it short.

### Required Regardless of Length

Front matter and debug markers per [Post Structure](./POST_STRUCTURE.md), the series metadata, opening prose, `## Epistemic State`, and `## References`. Below roughly 150 lines the Out of Scope and Conclusion sections may fold into a closing paragraph. The Epistemic State never folds, because on a short article it carries the statement of what the record does not settle, which is the article's main contribution.

## Handling a Thin Record

State the limit rather than writing around it. An article that says the public record contains no released specifications is more useful than one that infers specifications and does not say so.

Where sources disagree, name the disagreement and both sources rather than silently choosing. The X-23 designation is generally attributed to the Martin Marietta SV-5D PRIME while USAF nomenclature records reportedly show it was never assigned, and that conflict belongs in the article rather than behind it.

Where information postdates the article's editorial date, the survey is still written from current knowledge, and the Epistemic State says so.

## Related Sections

- [Article Genres](./ARTICLE_GENRES.md) for the genre framework
- [Subsystem Deep-Dive Structure](./SUBSYSTEM_DEEPDIVE_STRUCTURE.md) for the keystone pattern this borrows
- [Analytical Essay Structure](./ANALYTICAL_ESSAY_STRUCTURE.md) for the Epistemic State convention
- [MathJax Conventions](./MATHJAX_CONVENTIONS.md) for math density and numerical sanity checks
- [Style Guide](./STYLE_GUIDE.md) for prose rules
- [Publication Review](../process/PUBLICATION_REVIEW.md) for the review pass
