---
layout: post
mathjax: false
comments: true
title: "Telemeritocracy"
date: 2026-02-19 00:01:00 +0000
categories: management philosophy
---

<!-- A87 -->

The
[previous article]({% post_url 2026-02-18-mission-command-management-style %})
examined mission command
as a structural doctrine
for distributing decision-making authority
in organizations operating under uncertainty.
Mission command addresses the question of
how to delegate execution authority
while maintaining alignment with the leader's intent.
It does not address a prior question.
Who should hold authority in the first place,
and on what basis should that authority be assigned?

This article proposes a governance model
called telemeritocracy.
The term is a portmanteau of telocracy and meritocracy.
A telocracy is an organization governed by its purpose.
A meritocracy is an organization
governed by demonstrated ability.
Telemeritocracy combines these two principles.
Authority is assigned to those
who have demonstrated the ability
to advance the organization's purpose.

The model is not new in practice.
Scientific laboratories, engineering teams,
and open source communities
have long operated on something resembling this principle.
What is new is the explicit synthesis
and the argument that this synthesis
deserves its own name
because it differs in important ways
from either telocracy or meritocracy alone.

## Software Versions

```sh
# Date (UTC)
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2026-02-14 23:42:34 +0000

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

## Telocracy

A telocracy is a system of governance
organized around a substantive purpose.
The term derives from the Greek *telos*,
meaning end, purpose, or goal,
combined with *-cracy*, meaning rule.
A teleocratic organization exists to achieve something specific.
Its structure, roles, and rules
are instruments in service of that end.

The philosopher Michael Oakeshott
developed the most influential treatment
of this concept in *On Human Conduct* in 1975.
Oakeshott distinguishes two ideal types
of human association.

An enterprise association, which Oakeshott calls *universitas*,
is teleocratic.
Its members are united by shared substantive purposes.
They function as role-players
in a coordinated endeavor
where individual aspirations remain secondary
to the enterprise's defining end.
A business, a research laboratory, a military unit,
and a political campaign
are all enterprise associations.
A person enters and exits such an association voluntarily.

A civil association, which Oakeshott calls *societas*,
is nomocratic.
Its members share procedural agreements
and rules of conduct
rather than common goals.
The laws of a civil association
set out a structure for human interaction
but do not advance or inhibit
the particular causes of individuals or groups.
A constitutional republic
is the paradigmatic example of civil association.

Friedrich Hayek developed a parallel distinction
in *Law, Legislation and Liberty* in 1973.
Hayek describes a state as teleocratic
"if the same hierarchy of ends is binding on all its members"
and nomocratic
"if its general welfare consists solely
in the preservation of an abstract and end-independent order."

Both Oakeshott and Hayek warn
that teleocratic governance becomes dangerous
when applied to the state.
If a government defines a substantive purpose
and organizes all of society to achieve it,
citizens who do not share that purpose
have no meaningful exit.
Constitutional stability erodes
when substantive outcomes take priority over procedural rules.

This warning is important
but it applies specifically to coercive institutions.
Oakeshott explicitly notes
that enterprise association is the natural and appropriate model
for voluntary organizations.
A business, a research team, or an engineering department
is properly teleocratic.
Members join voluntarily to pursue a shared purpose.
The organization's structure should serve that purpose.
The danger arises only when teleocratic governance
is imposed on people who cannot leave.

## Meritocracy

The word meritocracy was coined
by the British sociologist Michael Young
in his 1958 satirical novel
*The Rise of the Meritocracy*.
The book describes a dystopian future United Kingdom
in which merit, defined as intelligence plus effort,
has become the central organizing principle of society.
The narrative ends in 2034
with a popular revolt against the meritocratic elite.

Young intended the term as a warning.
He represented meritocracy satirically
as the cold scientization of ability,
the bureaucratization of talent,
and the creation of a new ruling class
that could justify its privilege
through the claim of deserving it.
In June 2001, six months before his death,
Young published an essay in The Guardian
titled "Down with Meritocracy,"
protesting that Tony Blair's Labour Party
had adopted his satirical coinage as a term of praise.

Despite Young's intent,
the term was widely adopted as a positive ideal.
Meritocracy in organizational contexts
means that authority, advancement, and influence
are assigned based on demonstrated ability
and measurable contribution
rather than seniority, social class, or political connection.

The technology industry and open source communities
have been prominent sites
of meritocratic ideology.
The Apache Software Foundation
formally describes its governance model as meritocratic.
Contributors earn decision-making rights
through sustained, high-quality contributions.
The progression from user to contributor
to committer to Project Management Committee member
is determined by demonstrated merit
as assessed by existing members.

Meritocracy has well-documented failure modes.

The first failure mode is measurement.
Merit is ill-defined,
and its measurement reflects the biases
of those who define it.
When organizations claim to evaluate people on merit,
they often evaluate people
on a narrow set of visible outputs
that may not capture the full range
of valuable contributions.

The second failure mode is privilege replication.
The ability to contribute
often depends on access to resources
that are unequally distributed.
Free time to contribute to open source projects,
for example, is itself a mark of privilege.
A meritocratic system that does not account for this
may reproduce existing inequalities
while claiming to transcend them.

The third failure mode is self-serving bias.
The people who define merit
are typically those who have already succeeded
under the existing definition.
The ruling class becomes the gatekeeper
of an ill-defined concept
that conveniently validates its own position.

These critiques are serious
but they apply primarily
to meritocracy as a complete governance philosophy.
When meritocracy is used as one component
of a more carefully specified system,
and when the definition of merit
is explicitly tied to a defined purpose,
several of these failure modes can be mitigated.

## Telemeritocracy

Telemeritocracy synthesizes telocracy and meritocracy
into a single governance principle.
The organization defines its purpose.
Authority is assigned to those
who have demonstrated the ability
to advance that purpose.

The synthesis addresses weaknesses in each component.

Pure telocracy defines the purpose
but does not specify
how to assign decision-making authority.
A teleocratic organization knows what it is trying to achieve
but has no principled basis
for deciding who should make which decisions.
It risks concentrating authority
in whoever claims to speak for the purpose,
regardless of competence.

Pure meritocracy defines a basis for assigning authority
but does not anchor that basis to a purpose.
A meritocratic organization rewards demonstrated ability
but "demonstrated ability at what?" is left underspecified.
Without a telos to constrain the definition of merit,
the system drifts toward rewarding
whatever the current power structure values,
which may or may not align
with what the organization needs.

Telemeritocracy constrains both.
The telos defines what the organization is trying to achieve.
Merit is defined relative to that telos.
The people who hold decision-making authority
are those who have demonstrated the ability
to advance the organization's stated purpose.
When the purpose changes,
the distribution of authority should change with it,
because the relevant expertise may differ.

This is not a novel practice.
It is a novel name
for a compound governance principle
that already operates in many technical organizations.
What the name provides is a vocabulary
for discussing, evaluating, and deliberately designing
governance structures
that combine purpose alignment with competence-based authority.

## Precedents

Several organizational models
exhibit telemeritocratic characteristics
even when they do not use the term.

### Apache Software Foundation

The Apache Software Foundation
governs over 350 open source projects
using a formally meritocratic model.
Contributors earn decision-making rights
through sustained, high-quality contributions
to a project's stated mission.
The progression from user to committer
to Project Management Committee member
is governed by lazy consensus.
A few positive votes with no negative vote
is sufficient to proceed.
A negative vote requires an explanation
and an alternative proposal.

The model is explicitly teleocratic.
Each project has a defined charter.
Merit is assessed relative to that charter.
A contributor who writes excellent code
for a different project's goals
does not thereby earn authority
over the current project.
Purpose and merit are coupled.

### The IETF

The Internet Engineering Task Force
operates on the principle
articulated by Dave Clark of MIT in 1992.
"We reject kings, presidents, and voting.
We believe in rough consensus and running code."

RFC 7282
defines rough consensus
as being achieved
"when all issues are addressed,
but not necessarily accommodated."
The critical distinction is examining
unresolved technical objections
rather than tallying supporters.
Running code serves as a merit signal.
A proposal backed by a working implementation
carries more weight
than a proposal backed only by argument.
The IETF's purpose is to produce
practical, interoperable internet standards.
Authority flows to those
who advance that purpose
through technical contribution.

### Academic Shared Governance

University departments operate
under a model of shared governance
defined by the American Association of University Professors
as "the joint responsibility of faculty,
administrations, and governing boards
to govern colleges and universities."
Faculty have primary responsibility over curriculum
because their training and knowledge
make them "distinctly qualified to exercise
decision-making authority in their areas of expertise."

This is telemeritocratic in structure.
The purpose is education and scholarship.
Authority over academic matters
is assigned to those with demonstrated expertise
in the relevant domain.
Administrative authority over budgets and operations
is assigned separately.

### Valve Corporation

Valve Corporation published
its *Handbook for New Employees* in 2012,
describing a company without formal management.
All desks have wheels.
Employees form ad hoc teams
by physically moving to projects they find compelling.

Valve is an instructive failure case.
Former employees have described
a "pseudo-flat structure"
with an informal, unacknowledged layer of management.
Without formal authority structures,
power consolidated around personal relationships
and social capital rather than demonstrated merit.
Employees compared the environment
to *Lord of the Flies*.
The flat structure was blamed
for lack of diversity
and perverse incentives around performance reviews.

Jo Freeman anticipated this outcome in 1972.
Her essay "The Tyranny of Structurelessness" argues
that truly structureless groups are impossible.
"Any group of people of whatever nature
that comes together for any length of time
for any purpose
will inevitably structure itself in some fashion."
When organizations reject formal structures,
they do not eliminate hierarchy.
They hide it behind informal arrangements
that become harder to challenge.

The lesson for telemeritocracy is that
the governance structure must be explicit.
If authority is to be assigned based on merit
relative to a defined purpose,
the mechanisms for assessing merit,
assigning authority,
and resolving disputes
must be formalized and transparent.
An informal telemeritocracy
degenerates into an informal oligarchy.

### Mission Command

The
[previous article]({% post_url 2026-02-18-mission-command-management-style %})
on mission command
describes a military doctrine
that is structurally telemeritocratic.
The commander sets the intent,
which defines the organizational purpose.
Authority to execute is delegated
to subordinate leaders
based on their competence and proximity to the problem.
The six principles of mission command
as codified in Army Doctrine Publication 6-0
include building cohesive teams through mutual trust,
creating shared understanding,
providing clear commander's intent,
exercising disciplined initiative,
using mission orders,
and accepting prudent risk.

Mission command is telemeritocratic
because authority flows
to those who can best advance the mission
and because the mission itself
is explicitly defined and communicated.

## Why Telemeritocracy Fits Engineering Teams

Engineering and scientific organizations
are natural candidates for telemeritocratic governance
because their operating conditions
align with the model's prerequisites.

The first prerequisite is a definable purpose.
Engineering organizations typically have clear missions.
Build a product.
Solve a research problem.
Maintain a system.
Ship a standard.
The telos is usually concrete enough
to serve as an anchor for defining merit.

The second prerequisite is distributed expertise.
In engineering organizations
the people closest to the problem
typically have more relevant information
than their managers.
Telemeritocracy acknowledges this asymmetry
and builds authority structures around it.
The person who best understands
the database replication topology
should hold decision-making authority
over database replication changes,
regardless of where they sit
in the organizational hierarchy.

The third prerequisite
is that contribution quality is assessable.
Code can be reviewed.
Designs can be evaluated.
Systems can be tested.
Research results can be replicated.
While the assessment of merit is never perfect,
engineering disciplines
provide more objective signals of contribution quality
than most organizational contexts.

The fourth prerequisite is voluntary membership.
Engineers join companies and teams voluntarily.
They can leave if the purpose changes
or if they disagree with the governance structure.
This satisfies Oakeshott's condition
for legitimate teleocratic governance.
The organization may properly be organized
around a shared purpose
because its members chose to be there.

The benefits follow from these prerequisites.
Decision-making scales
because authority is distributed
to those with the most relevant expertise.
Innovation improves
because the people closest to novel problems
have the authority to explore solutions.
Purpose alignment is maintained
because the definition of merit
is anchored to the organizational telos.
Accountability is clearer
because authority comes with
explicit expectations of contribution.

## Risks and Failure Modes

Telemeritocracy has failure modes
that deserve explicit attention.

**Goodhart's Law.**
"When a measure becomes a target,
it ceases to be a good measure."
Any metric used to assess merit
will be gamed once it becomes the basis for advancement.
Lines of code, number of commits,
number of papers published,
and patent counts
are all metrics that have been optimized
at the expense of the underlying purpose they were meant to serve.
A telemeritocratic organization must continuously revisit
whether its merit signals
still correlate with purpose advancement.

**The Peter Principle.**
Laurence Peter observed in 1969
that in a hierarchy,
employees are promoted based on success in previous jobs
until they reach a level at which they are no longer competent.
Telemeritocracy is not immune.
A brilliant individual contributor
who is elevated to an architectural role
may lack the communication and coordination skills
that the new role requires.
Merit in one domain
does not automatically transfer to another.

**Mission drift.**
The telos itself can change gradually
without anyone noticing.
Social enterprises and purpose-driven organizations
face the risk of slowly deviating from their stated purpose
as external pressures shift incentives.
A telemeritocratic organization
must periodically re-examine its purpose
and verify that its authority structures
still align with that purpose.

**Authoritarianism risk.**
Bryan Cheang argued in the
*Journal of Institutional Economics* in 2024
that mission-directed governance
"could require the use of authoritarian
and disciplinary mechanisms
to sustain mission focus in an environment of uncertainty."
When purpose alignment becomes mandatory
rather than voluntary,
teleocratic governance slides toward coercion.
This risk is mitigated in voluntary organizations
where members can exit,
but it remains a concern
in organizations where exit costs are high.

**Informal hierarchy.**
As the Valve case illustrates,
removing formal hierarchy
does not eliminate hierarchy.
It makes hierarchy informal, opaque,
and harder to challenge.
A telemeritocratic organization
must formalize its authority structures
even though formalization
introduces bureaucratic overhead.
The alternative is worse.

**Narrow definitions of merit.**
If the organization defines merit too narrowly,
it will systematically undervalue
contributions that fall outside the definition.
Community building, mentorship, documentation,
and operational maintenance
are all forms of merit
that are often invisible
in systems that reward only technical novelty.

## When Not to Use Telemeritocracy

Telemeritocracy is not appropriate
in every organizational context.

In organizations where the purpose is contested
or where members did not voluntarily agree to the purpose,
teleocratic governance is illegitimate.
A government cannot properly be telemeritocratic
because citizens did not choose its purpose
and cannot easily exit.

In organizations where expertise is concentrated
at the top of the hierarchy
rather than distributed throughout the organization,
a more traditional hierarchical model
may be more efficient.
Telemeritocracy is designed for organizations
where the people closest to the problem
have better information than the people giving orders.
When that condition does not hold,
the model loses its advantage.

In regulated environments
where compliance with specific procedures
is legally required,
distributing authority based on expertise
may conflict with regulatory requirements
for defined chains of accountability.
A nuclear power plant
requires a clear command hierarchy
regardless of how expertise is distributed.

In organizations without the maturity
to support transparent merit assessment,
attempting telemeritocracy
will produce the informal oligarchies
that Freeman warned about.
The prerequisites of trust,
transparent evaluation,
and genuine commitment to purpose
must be in place before the model can function.

## Summary

Telemeritocracy is a governance model
that assigns decision-making authority
based on demonstrated ability
to advance a defined organizational purpose.
It combines two established concepts.
Telocracy provides the purpose.
Meritocracy provides the basis for assigning authority.
The synthesis constrains both.
Purpose prevents meritocracy
from rewarding ability disconnected from organizational needs.
Merit prevents telocracy
from concentrating authority
in whoever claims to speak for the purpose.

The model has precedents
in open source governance,
academic shared governance,
internet standards bodies,
and military mission command.
It is well suited to engineering and scientific organizations
where the purpose is definable,
expertise is distributed,
contribution quality is assessable,
and membership is voluntary.

Telemeritocracy is not a universal solution.
It fails when merit measurement is corrupted,
when purpose drifts unexamined,
when authority structures remain informal,
or when the organization lacks the maturity
to support transparent evaluation.
It is inappropriate for coercive institutions,
regulated environments requiring strict chains of accountability,
and organizations where expertise is centralized
rather than distributed.

For engineering and scientific teams
that operate under uncertainty,
value distributed expertise,
and align around a shared purpose,
telemeritocracy provides a principled framework
for deciding who should hold authority and why.

## Future Reading

Michael Oakeshott's *On Human Conduct*
provides the foundational distinction
between teleocratic and nomocratic governance.
Michael Young's *The Rise of the Meritocracy*
is the original satirical treatment
of meritocracy as a social system.
Jo Freeman's "The Tyranny of Structurelessness"
is essential reading on the dangers of informal hierarchy
in organizations that reject formal authority structures.
The Apache Software Foundation's governance documentation
provides a working example
of formalized meritocratic governance for open source projects.
RFC 7282 describes the IETF's consensus model
in detail.
The companion article on
[mission command]({% post_url 2026-02-18-mission-command-management-style %})
examines a military doctrine
that is structurally telemeritocratic.

## References

- [Book, On Human Conduct][book_on_human_conduct]
- [Book, The Rise of the Meritocracy][book_rise_meritocracy]
- [Reference, Apache Software Foundation Governance][ref_apache]
- [Reference, RFC 7282 On Consensus and Humming][ref_rfc_7282]
- [Reference, Valve Employee Handbook][ref_valve]
- [Related Post, Mission Command Management Style][related_post_mission_command]
- [Research, Hayek on Nomocracy and Teleocracy][research_cheung_hayek]
- [Research, Levels without Bosses at Valve][research_moller_valve]
- [Research, Mission-Directed Governance Risks Authoritarianism][research_cheang]
- [Research, The Dangers of Teleocratic Politics][research_weiner]
- [Research, The Tyranny of Structurelessness][research_freeman]

[book_on_human_conduct]: https://global.oup.com/academic/product/on-human-conduct-9780198277583
[book_rise_meritocracy]: https://en.wikipedia.org/wiki/The_Rise_of_the_Meritocracy
[ref_apache]: https://www.apache.org/foundation/how-it-works/
[ref_rfc_7282]: https://datatracker.ietf.org/doc/rfc7282/
[ref_valve]: https://archive.org/details/ValveEmployeeHandbook
[related_post_mission_command]: {% post_url 2026-02-18-mission-command-management-style %}
[research_cheang]: https://www.cambridge.org/core/journals/journal-of-institutional-economics/article/why-missiondirected-governance-risks-authoritarianism-lessons-from-east-asia/E0254D7CFB996C52FC24FDFE768DD925
[research_cheung_hayek]: https://cosmosandtaxis.org/wp-content/uploads/2014/11/ct_1_2_cheung.pdf
[research_freeman]: https://www.jofreeman.com/joreen/tyranny.htm
[research_moller_valve]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3884844
[research_weiner]: https://theconstitutionalist.org/2020/12/10/the-dangers-of-teleocratic-politics/
