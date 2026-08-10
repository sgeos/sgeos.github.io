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

## The Article Classes

Depth is a function of the surviving record, not of the author's diligence. Four classes are
recognised, and an article should state which it is.

**The classes are about SECTION ORDER, which is prescriptive. The numbers beside them are MEASURED
DESCRIPTIONS of what the series has produced, and they are not targets.**

| Class | Section order |
|-------|---------------|
| Series opener | Framing order, see below |
| Full aircraft | The full twelve-section order above, plus the three series sections |
| Documentation-poor | Full order, short sections, explicit statement of what is unknown |
| Designation anomaly | Reduced order, see below |

### What the Series Actually Produces

**Amended 2026-08-09 against measurements of all twenty-seven articles then drafted, A297 through
A323.** The previous version of this table carried bands drawn from the History of SpaceX medians that
no recent article matched, and it had drifted far enough from practice to be misleading.

| | Lines | Display equations | References |
|---|---|---|---|
| Minimum | 937 | 25 | 335 |
| Median | 1,488 | 94 | 404 |
| Maximum | 7,198 | 200 | 3,990 |

**The corpus contains two regimes and the transitions are sharp.**

| Group | Lines | Equations | References |
|---|---|---|---|
| A297 to A312 | 1,302 to 2,226 | 91 to 200 | 335 to 474 |
| A313 to A317 | 937 to 1,237 | 29 to 78 | 387 to 468 |
| A318 to A323 | 1,692 to 7,198 | 25 to 72 | 1,192 to 3,990 |

**The equation count fell at A313 and the reference count rose by an order of magnitude at A318.**
Neither is a change of standard. **The equation count follows the subject**, since the governing rule
displays whatever relations the prose relies on, and a multi-disciplinary vehicle such as the A305
Aerobee produces 200 while a single-question vehicle produces 30. **The reference count follows the
contemporary-survey directive**, which from A318 onward was satisfied by citing a topic as a body of
literature rather than by a few exemplars.

### The Governing Directive

**The human pilot directed on 2026-08-09 that the goal is for these articles to be as comprehensive as
possible and that doing more is not a problem.**

**Exceeding any figure above is therefore not a defect, requires no justification, and is not to be
trimmed toward.** A305 stands at 2,226 lines, 200 equations and 474 references and was explicitly left
as it is.

**Padding toward a figure is equally forbidden.** Comprehensiveness means earning the length, not
manufacturing it. **Report the counts, because the record is useful. Do not target them.**

### The Rules That Actually Produce the Numbers

**Equations.** **If the prose names a result, relies on a relation, or quotes a value that some
relation produced, show the relation.** A result cited by author and year but never displayed is the
defect the equation-density review exists to find. Every article in this series takes that review as a
standing expectation rather than an exception.

**References.** Prefer primary sources, meaning original research reports and papers contemporary with
the work. **Report the period COUNT as well as the primary FRACTION**, because adding a contemporary
survey lowers the fraction while leaving the count unchanged, and reporting only the fraction reads as
a regression when it is the directive working.

**Length.** Whatever the first two produce, plus the prose needed to carry the argument.

### The Series Opener

A series opener is not a per-aircraft article and does not use the twelve-section order. It carries
the analytical model, the shared sizing derivations, and the statement of what the series can and
cannot establish. **It is denser in equations than a per-aircraft article for a structural reason
rather than an editorial one**, and A297 measured 147 against a per-aircraft median of 94. Every
relation derived once in the opener is a relation the per-aircraft articles reference instead of
repeating, so density there buys brevity seventy-one times over. The opener should still show any
relation it names.

### Designation Anomalies

Some designations were refused, reserved and never assigned, skipped, duplicated, or leapfrogged. For these the subject is the number rather than an aircraft, so there is no keystone to identify and no system to dimension. Use a reduced order.

1. Opening prose naming the designation and the anomaly.
2. What happened, with dates and the deciding authority where the record gives them.
3. Why, if the record says.
4. What the anomaly reveals about the designation system.
5. `## Epistemic State`.
6. `## References`.

An article stating that the X-52 designation was requested in 2006, was refused because of possible confusion with the B-52, and that the programme became the X-53 is complete at that length. Padding it with an Out of Scope section it does not need is worse than leaving it short.

**The anomaly class has a boundary and A320 established it.** The X-23 is listed among the designation anomalies, but the SV-5D actually flew three times and returned a measurement, so it was written as a full-aircraft article with the anomaly given its own section. **The test is whether a vehicle existed and produced data, not whether the designation is disputed.** Where no vehicle was ever built, the reduced order is the honest choice however interesting the paperwork is.

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
