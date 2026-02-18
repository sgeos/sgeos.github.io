---
layout: post
mathjax: false
comments: true
title: "The Cost of Failure Spectrum"
date: 2026-02-24 17:39:57 +0000
categories: management philosophy
---

<!-- A93 -->

In the author's experience,
there are two kinds of engineering.

The first kind values speed above correctness.
The minimum viable product is rough,
incomplete, and possibly broken,
but it is in front of users
generating feedback.
The feedback loop drives iteration.
Quality improves over time.
The initial release does not need
to be good.
It needs to exist.

The second kind values correctness above speed.
The minimum viable product
that ships with a critical defect
does not generate useful feedback.
It generates lawsuits, regulatory action,
or casualties.
There is no iteration loop
that recovers from killing a patient
or losing a client's retirement fund.
The initial release
needs to be correct.

The most succinct way to distinguish
these two modes
is to ask a single question.
Does a poor quality minimum viable product
have positive or negative value?
If the answer is positive,
the project operates
in the commercial engineering mode.
If the answer is negative,
the project operates
in the mission-critical engineering mode.
This article examines the distinction,
surveys the established frameworks
that formalize it,
and argues that the most common failure mode
is not the wrong engineering approach
but the wrong identification
of which mode applies.

## Software Versions

```sh
# Date (UTC)
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2026-02-18 17:39:57 +0000

# OS and Version
$ uname -vm
Darwin Kernel Version 23.6.0: Mon Jul 29 21:14:30 PDT 2024; root:xnu-10063.141.2~1/RELEASE_ARM64_T6000 arm64

$ sw_vers
ProductName:		macOS
ProductVersion:		14.6.1
BuildVersion:		23G93

# Hardware Information
$ system_profiler SPHardwareDataType | sed -n '8,10p'
      Chip: Apple M1 Max
      Total Number of Cores: 10 (8 performance and 2 efficiency)
      Memory: 32 GB
```

## The Dichotomy

### Commercial Software Engineering

The conventional academic term
for the speed-first engineering mode
is commercial software engineering.
Ian [Sommerville][book_sommerville]
draws the distinction explicitly
in his standard textbook *Software Engineering*
between commercial software
and [critical systems][ref_critical_system].
Commercial software
is software where the primary risk of failure
is lost revenue or user inconvenience
rather than physical harm
or catastrophic financial loss.

The practitioner term
for the methodology
that maximizes this mode
is [lean product development][book_lean_startup].
Eric Ries formalized the lean startup methodology
in his 2011 book *The Lean Startup*,
building on Steve Blank's
Customer Development methodology
and Kent Beck's
Extreme Programming.
The core mechanism
is the build-measure-learn feedback loop.
Build a minimum viable product.
Measure how users respond.
Learn from the response.
Iterate.
The poor quality MVP
has positive value
because it generates validated learning
that informs the next iteration.

The mindset is
"ship when possible, fix later."
Speed to market is the competitive advantage.
The first product to reach users
captures feedback and market position.
The product that waits for perfection
may arrive after the market has moved.

Examples of projects
that typically operate in this mode
include video streaming platforms,
video games,
social media applications,
e-commerce storefronts,
and content management systems.
In all of these cases,
a rough initial release
is preferable to no release.
Users tolerate imperfection
because the alternative
is the absence of the product entirely.

### Mission-Critical Engineering

Mission-critical engineering
is the mode where correctness
is valued above speed
because the cost of failure
is severe enough to threaten
the survival of the enterprise
or the safety of its users.

The term [critical system][ref_critical_system]
encompasses several categories.
A safety-critical system
is one where failure
may result in loss of life,
injury, or environmental damage.
A mission-critical system
is one where failure
may result in the failure
of some goal-directed activity.
A business-critical system
is one where failure
may result in very high financial losses.
A security-critical system
is one where failure
may result in unauthorized access
to information or resources.

The mindset is
"fix now, ship when ready."
Correctness is the survival requirement.
The product that ships
with a defect in its flight control software
does not get a second iteration.
The exchange that ships
with a defect in its order matching engine
does not get a second reputation.

Examples of projects
that operate in this mode
include aerospace flight control systems,
medical device firmware,
financial trading platforms,
nuclear reactor control software,
and autonomous vehicle perception systems.
In all of these cases,
a poor quality MVP
has negative value.
Shipping a defective product
is worse than shipping nothing.

## Why "Cost of Failure" Not "Speed vs Quality"

The dichotomy described above
might appear to be
a tradeoff between speed and quality.
It is not.

[Forsgren, Humble, and Kim][book_accelerate]
demonstrated in their 2018 book *Accelerate*,
based on the
[DORA State of DevOps][research_dora] research
spanning over 23,000 survey respondents
across more than 2,000 organizations,
that elite engineering teams
achieve both speed and stability simultaneously.
High-performing teams
deploy more frequently,
have lower change failure rates,
and recover from failures faster
than low-performing teams.
The supposed tradeoff between speed and stability
is empirically false
among the best performers.

The real variable
is not speed versus quality.
It is the cost of failure.
When the cost of failure is low,
rapid deployment is rational
because failures are cheap to detect
and cheap to correct.
When the cost of failure is high,
rigorous pre-deployment verification is rational
because failures are expensive to detect
and expensive, or impossible, to correct.

The DORA research
demonstrates that elite teams
can deploy quickly
while maintaining low failure rates.
This does not mean
that a medical device company
should adopt the deployment cadence
of a social media startup.
It means that the limiting factor
is not organizational capability
but the consequence of getting it wrong.
A social media startup
that deploys a broken feature
rolls it back.
A medical device company
that deploys a broken feature
faces a product recall,
regulatory investigation,
and potential wrongful death litigation.
The engineering practices differ
not because the teams differ in skill
but because the stakes differ in magnitude.

## Established Frameworks

Several established frameworks
formalize the concept
of engineering mode
based on failure consequence.

### Critical Systems Taxonomy

Sommerville's textbook classification
identifies four types
of [critical systems][ref_critical_system].
Safety-critical systems
are those where failure
may result in loss of life or injury.
Mission-critical systems
are those where failure
may result in the failure
of some goal-directed activity.
Business-critical systems
are those where failure
may result in very high financial losses.
Security-critical systems
are those where failure
may result in unauthorized access
to information or resources.
These categories are not mutually exclusive.
A financial trading platform
may be simultaneously business-critical
and security-critical.

### Safety Integrity Levels

[IEC 61508][ref_iec_61508]
defines four
[Safety Integrity Levels][ref_safety_integrity_level]
(SIL 1 through SIL 4)
for electrical, electronic,
and programmable electronic systems.
SIL 1 is the lowest integrity level
and SIL 4 is the highest.
Each level specifies
quantitative targets
for the probability of dangerous failure.
The standard applies to general industrial systems
and serves as the parent standard
for domain-specific derivatives.

[DO-178C][ref_do_178c]
defines five Design Assurance Levels
(DAL A through DAL E)
for airborne software.
Level A corresponds to catastrophic failure conditions
and Level E corresponds
to no safety effect.
The standard specifies
the software development processes,
verification activities,
and documentation requirements
appropriate to each level.

[ISO 26262][ref_iso_26262]
defines four
Automotive Safety Integrity Levels
(ASIL A through ASIL D)
plus a Quality Management (QM) level
for automotive systems.
ASIL D applies to systems
where failure is life-threatening,
such as braking and steering.
QM applies to systems
with no safety requirement,
such as infotainment.
The standard permits
ASIL decomposition,
allowing a system rated ASIL D
to be decomposed into components
with different ASIL ratings.
This decomposition mechanism
formalizes the hybrid pattern
discussed below.

### Bimodal IT

Gartner introduced the concept
of [Bimodal IT][ref_bimodal_it]
around 2014.
Mode 1 is traditional, sequential,
and emphasizes safety and accuracy.
Mode 2 is exploratory, nonlinear,
and emphasizes agility and speed.
The framework was widely discussed
and widely criticized.
The primary criticism
is that framing the two modes
as separate organizational functions
creates a false dichotomy
and leads to a two-speed organization
where Mode 1 teams
accumulate technical debt
and Mode 2 teams
lack operational discipline.
The DORA research
provides empirical evidence
against the Bimodal framing
by demonstrating that elite teams
achieve both modes simultaneously.

Despite its limitations,
the Bimodal IT concept
is useful as a diagnostic tool.
Organizations that recognize
the distinction between the two modes
can make deliberate decisions
about which mode applies
to each project or component.
The failure is not in recognizing the distinction
but in treating it
as an organizational structure
rather than a project-level decision.

### Pace Layering

Stewart Brand proposed
[pace layering][research_pace_layering]
as a model
for understanding how complex systems
change at different rates.
Fast layers innovate.
Slow layers stabilize.
The fast layers are free to experiment
because the slow layers
absorb the consequences of failure.
The slow layers are free to remain stable
because the fast layers
handle adaptation to changing conditions.

Applied to software systems,
pace layering suggests
that the user interface layer
should change rapidly
and tolerate high rates of failure
because the cost of a UI defect is low.
The data layer and infrastructure layer
should change slowly
and tolerate low rates of failure
because the cost of a data corruption
or infrastructure outage is high.
This is the theoretical foundation
for the hybrid pattern
discussed in the next section.

## The Hybrid Pattern

Most projects
are not purely commercial
or purely mission-critical.
They contain components
that operate in different modes.

A financial technology platform
has a mission-critical transaction engine
where a rounding error
in currency conversion
can produce regulatory violations
and financial losses.
The same platform has a commercial
user interface
where a layout defect
is a minor inconvenience
that can be fixed in the next deployment.

A video game
has a commercial gameplay loop
where a balance issue
is an annoyance
that the community will vocally report
and the developer will patch.
The same video game
has a mission-critical anti-cheat system
where a false positive
bans a paying customer
and a false negative
destroys the competitive integrity
that sustains the player base.

An advertising technology platform
has a mission-critical bidding engine
where a pricing defect
can cause the platform
to overbid by millions of dollars
in minutes.
The same platform has a commercial
reporting dashboard
where a data visualization error
is a nuisance
that the account manager
can explain to the client.

The boundary identification problem
is itself an engineering decision.
Knowing where the mission-critical core ends
and the commercial shell begins
requires domain expertise
and deliberate analysis.
The boundary is not always obvious.
A login system
for a consumer social network
is commercial in isolation.
The same login system
for a healthcare portal
that provides access
to protected health information
is security-critical.
Context determines criticality,
not the component itself.

ISO 26262's ASIL decomposition
provides a formal mechanism
for this pattern
within automotive systems.
A system rated ASIL D
can be decomposed into components
with different ASIL ratings.
The braking actuator software
is rated ASIL D.
The seat heater controller
is rated QM.
Both are part of the same vehicle,
but they are engineered
under radically different processes.

Brand's pace layering
provides the theoretical justification.
Fast layers innovate,
slow layers stabilize.
The mission-critical core
is the slow layer.
The commercial shell
is the fast layer.
The architecture
should reflect this distinction
so that rapid iteration
in the commercial shell
cannot propagate failures
into the mission-critical core.

## Mindset Mismatch

The most common failure mode
in the cost of failure spectrum
is not the wrong engineering approach.
It is the wrong identification
of which mode applies.

A commercial mindset
applied to a mission-critical project
produces software
that ships quickly
and fails catastrophically.
The [Therac-25][ref_therac_25] radiation therapy machine
killed patients in the 1980s
in part because software development practices
appropriate for commercial software
were applied to a safety-critical system.
The Boeing 737 MAX MCAS system
contributed to two fatal crashes
in part because software integration testing
did not reflect
the safety-critical nature
of the flight control augmentation.

A mission-critical mindset
applied to a commercial project
produces software
that is rigorously verified,
thoroughly documented,
and irrelevant by the time it ships.
The competitive window has closed.
The users have adopted a competitor's product
that shipped with defects
but shipped first.
The development team
has spent six months
on a comprehensive test suite
for a feature
that the market did not want.

The same engineer
can operate effectively in both modes.
The adaptation is not a matter of skill
but a matter of calibration.
A pilot who flies both
single-engine recreational aircraft
and commercial airliners
does not become a worse pilot
when switching between them.
The pilot adjusts the checklist,
the preflight inspection rigor,
and the decision-making thresholds
to match the aircraft
and the passengers.

The critical skill
is correct identification
of which mode applies.
If the project has a mission-critical core
with a commercial shell,
defining that boundary is essential.
Engineers working on the core
must understand
that the defect tolerance is zero.
Engineers working on the shell
must understand
that the deployment cadence
is measured in days, not months.
And the architecture
must ensure that the boundary
is enforced by design,
not by convention.

## Conclusion

The cost of failure spectrum
describes a continuum
along which every engineering project
can be placed.
At one end,
failure is cheap and informative.
A poor quality MVP
generates user feedback
that funds the next iteration.
At the other end,
failure is expensive and destructive.
A poor quality MVP
generates casualties, lawsuits,
or catastrophic financial loss.

The conventional terminology
for these two modes
is commercial software engineering
and mission-critical engineering.
The established frameworks
from Sommerville's critical systems taxonomy
through IEC 61508, DO-178C, and ISO 26262
formalize the engineering practices
appropriate to each point on the spectrum.
Brand's pace layering
and ISO 26262's ASIL decomposition
provide theoretical and practical foundations
for the hybrid pattern
where a mission-critical core
operates under rigorous processes
while a commercial shell
iterates rapidly around it.

The article on
[mission command][related_post_mission_command]
examined how to delegate execution authority
while maintaining alignment with intent.
The article on
[telemeritocracy][related_post_telemeritocracy]
examined how to assign authority
based on demonstrated ability
to advance a defined purpose.
This article addresses a prior question
for both frameworks.
Before delegating authority
or assigning it based on merit,
the organization must determine
whether the project demands
the speed of commercial engineering
or the rigor of mission-critical engineering.
The answer to that question
determines the engineering culture,
the deployment practices,
the testing standards,
and the acceptable failure rate
for every component in the system.

## Future Reading

Ries's *[The Lean Startup][book_lean_startup]*
formalizes the build-measure-learn loop
and the concept of validated learning
through minimum viable products.
It is the foundational text
for the commercial engineering mode.

Perrow's *[Normal Accidents][book_normal_accidents]*
argues that catastrophic accidents
are inevitable in systems
that are both interactively complex
and tightly coupled.
It provides the theoretical foundation
for understanding
why mission-critical engineering
demands fundamentally different practices
rather than merely "more careful" versions
of commercial practices.

Forsgren, Humble, and Kim's
*[Accelerate][book_accelerate]*
presents the DORA research
demonstrating that elite teams
achieve both speed and stability.
It provides empirical evidence
against the false dichotomy
between speed and quality.

Brand's
"[Pace Layering][research_pace_layering]"
proposes the model
of fast and slow layers
that underpins the hybrid pattern.
It applies well beyond software
to any system
where different components
change at different rates.

Leveson's
*[Engineering a Safer World][book_leveson]*
develops the STAMP model
for systems-theoretic accident analysis.
It provides tools
for identifying the boundary
between mission-critical
and commercial components
in complex systems.

## References

- [Book, Accelerate][book_accelerate]
- [Book, Engineering a Safer World][book_leveson]
- [Book, Normal Accidents][book_normal_accidents]
- [Book, Software Engineering][book_sommerville]
- [Book, The Lean Startup][book_lean_startup]
- [Reference, Bimodal IT][ref_bimodal_it]
- [Reference, Critical System][ref_critical_system]
- [Reference, Cynefin Framework][ref_cynefin]
- [Reference, DO-178C][ref_do_178c]
- [Reference, IEC 61508][ref_iec_61508]
- [Reference, ISO 26262][ref_iso_26262]
- [Reference, Safety Integrity Level][ref_safety_integrity_level]
- [Reference, Therac-25][ref_therac_25]
- [Related Post, Mission Command Management Style][related_post_mission_command]
- [Related Post, Telemeritocracy][related_post_telemeritocracy]
- [Research, DORA State of DevOps][research_dora]
- [Research, Pace Layering][research_pace_layering]

[book_accelerate]: https://en.wikipedia.org/wiki/Accelerate_(book)
[book_leveson]: https://direct.mit.edu/books/oa-monograph/2908/Engineering-a-Safer-WorldSystems-Thinking-Applied
[book_normal_accidents]: https://press.princeton.edu/books/paperback/9780691004129/normal-accidents
[book_sommerville]: https://en.wikipedia.org/wiki/Ian_Sommerville_(software_engineer)
[book_lean_startup]: https://en.wikipedia.org/wiki/The_Lean_Startup
[ref_bimodal_it]: https://www.gartner.com/en/information-technology/glossary/bimodal
[ref_critical_system]: https://en.wikipedia.org/wiki/Critical_system
[ref_cynefin]: https://en.wikipedia.org/wiki/Cynefin_framework
[ref_do_178c]: https://en.wikipedia.org/wiki/DO-178C
[ref_iec_61508]: https://en.wikipedia.org/wiki/IEC_61508
[ref_iso_26262]: https://en.wikipedia.org/wiki/ISO_26262
[ref_safety_integrity_level]: https://en.wikipedia.org/wiki/Safety_integrity_level
[ref_therac_25]: https://en.wikipedia.org/wiki/Therac-25
[related_post_mission_command]: {% post_url 2026-02-18-mission_command_management_style %}
[related_post_telemeritocracy]: {% post_url 2026-02-19-telemeritocracy %}
[research_dora]: https://dora.dev/research/
[research_pace_layering]: https://jods.mitpress.mit.edu/pub/issue3-brand
