---
layout: post
mathjax: false
comments: true
title: "Cryptotelemeritocracy"
date: 2026-02-20 00:01:00 +0000
categories: management philosophy
---

<!-- A89 -->

The
[previous article on telemeritocracy][related_post_telemeritocracy]
proposed a governance model
in which authority is assigned to those
who have demonstrated the ability
to advance a defined organizational purpose.
Telemeritocracy synthesizes telocracy and meritocracy.
The telos constrains what counts as merit.
Merit constrains who holds authority.
The synthesis addresses weaknesses in each component
and provides a principled framework
for deciding who should make decisions and why.

That article identified mission drift
as one of several failure modes.
The telos itself can change gradually
without anyone noticing.
If the telos drifts,
then merit defined relative to that telos also drifts,
and the entire governance structure
silently realigns around a purpose
that no one explicitly chose.
Telemeritocracy offers no structural remedy for this problem.
It relies on periodic re-examination of purpose
without specifying who performs that re-examination
or how they are insulated
from the very drift they are meant to detect.

This article proposes cryptotelemeritocracy
as an extension of telemeritocracy
that addresses the mission drift vulnerability.
The prefix "crypto" refers to cryptographic anonymity.
A cryptotelemeritocracy is a telemeritocracy
augmented with an anonymous telos auditor
whose identity is concealed
through cryptographic mechanisms.
The auditor monitors organizational alignment
with the stated purpose
and may intervene when misalignment is detected.
Staff know that the auditor exists.
They do not know who the auditor is.

## Software Versions

```sh
# Date (UTC)
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2026-02-15 00:40:00 +0000

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

## The Problem of Mission Drift

Organizations systematically deviate
from their founding purpose over time.
This observation is not speculation.
It is one of the most replicated findings
in organizational theory.

Robert K. Merton identified goal displacement
as a bureaucratic dysfunction
in which formal rules and procedures,
originally designed as means to achieve organizational ends,
become ends in themselves.
Merton attributed this to trained incapacity
resulting from overconformity.
Officials who follow rules too rigidly
lose the ability to deal efficiently
with changing circumstances.
The phenomenon represents a means-ends reversal.
Instrumental processes assume an importance
that exceeds their concrete technical value.

Robert Michels articulated a more pessimistic version
of this observation
in his 1911 book *Political Parties*.
Michels proposed the iron law of oligarchy.
All complex organizations,
regardless of how democratic they are at founding,
inevitably develop into oligarchies.
The mechanism is goal displacement at the leadership level.
Leaders who are now entrenched
with an organization to run,
staff to pay,
and a reputation to maintain
begin prioritizing the institution itself
over its founding ideals.
They put the survival of the organization,
which provides them with their livelihood,
above all other considerations.
Michels argued that this tendency arises
from the tactical and technical necessities of organization.
Competent leadership, centralized authority,
and the division of tasks
within a professional bureaucracy
create structural incentives
for leaders to preserve their positions.

Philip Selznick documented a related dynamic
in his 1949 study *TVA and the Grass Roots*.
The Tennessee Valley Authority
was established as a New Deal institution
to address regional economic stagnation and inequality.
Selznick showed that the TVA
adopted a strategy of cooptation and accommodation
with powerful local agricultural elites
at the expense of vulnerable populations.
The institution compromised its founding purpose
not through internal drift
but through adaptation to external power structures.
Selznick coined the term informal cooptation
to describe this pattern
and contributed process theories
for how major projects fail
through goal displacement and values depletion.

These three accounts describe
the same fundamental dynamic
from different angles.
Merton explains how means replace ends.
Michels explains how leaders replace missions.
Selznick explains how environments replace intentions.
All three apply to telemeritocratic organizations.

A telemeritocracy is particularly vulnerable to mission drift
because its authority structure
is defined relative to the telos.
If the telos drifts,
the distribution of authority drifts with it.
The people who hold decision-making power
under a drifting telos
are precisely those whose demonstrated ability
aligns with the new, unofficial purpose.
They have no structural incentive to detect the drift
because the drift validates their authority.
This creates a positive feedback loop.
Drift selects for leaders
who are adapted to the drifted state,
and those leaders have no reason
to restore the original purpose.

The question is not whether organizations drift.
They do.
The question is whether a governance structure
can include a mechanism
for detecting and flagging drift
before the feedback loop
makes correction politically impossible.

## Precedents for Anonymous Oversight

The idea of an institutional role
dedicated to challenging alignment
is not new.
Organizations have repeatedly created positions
whose function is to question
whether the institution
is doing what it is supposed to do.
Several of these precedents
involve anonymity or structural independence
as essential features.

### Athenian Ostracism

Ostracism was a political mechanism
in Athenian democracy
in which citizens could vote annually
to banish any individual for ten years.
The term derives from *ostraka*,
the pottery shards used as voting tokens.
Each year the Assembly asked
whether to hold an ostracism.
If approved,
citizens scratched a name on a pottery shard.
The shards were piled face down
to preserve anonymity.
The person whose pile contained the most ostraka
was banished,
provided a quorum of at least 6,000 total votes was met.
The banished person retained property,
revenues, citizenship, and status.

Ostracism represents one of the earliest known mechanisms
for anonymous collective evaluation of leaders.
It was designed to prevent
the concentration of excessive power.
The use of broken pottery as ballots
made the system accessible to all citizens
regardless of wealth.

### Roman Tribunes of the Plebs

The tribunes of the plebs
were annually elected magistrates
established in 494 BCE
following the first secession of the plebs
to the Sacred Mount.
They were the most important check
on the power of the Roman Senate and magistrates.
Their sacrosanctity was guaranteed
by a sacred oath sworn by the plebs,
meaning any assault on a tribune's person
was punishable by death.

Tribunes possessed the *ius intercessionis*,
the power of veto,
to intercede on behalf of the plebeians
and obstruct actions of the magistrates.
Because they were not technically magistrates themselves,
they relied on their sacrosanctity
rather than formal authority
to exercise this power.
Their *auxilium* power
allowed personal intervention
in defense of a citizen's rights.

The tribunes derived authority
not from the existing hierarchy
but from a compact with the people
they were meant to protect.
The role was designed specifically
to counter the power of the governing class
from a position outside that class's power structure.

### The Devil's Advocate

The Promotor Fidei,
popularly known as the Devil's Advocate,
was a canon lawyer appointed by the Catholic Church
to argue against the canonization
of a candidate for sainthood.
The role was formally established
as an office by Pope Sixtus V in 1587.
The Devil's Advocate cross-examined witnesses,
questioned evidence,
looked for holes in the case,
and argued that attributed miracles were fraudulent.
The role opposed the Advocatus Dei,
who argued in favor.

The Devil's Advocate represents
an institutionalized role of structured dissent.
Its fate is instructive.
Pope John Paul II significantly reduced
the office's powers in 1983,
greatly accelerating the canonization process.
This demonstrates a recurring pattern.
Oversight roles that constrain institutional leaders
tend to be weakened or eliminated
when those leaders have sufficient authority to do so.

### Venetian Bocche di Leone

The Council of Ten
was established in Venice in 1310
as a body to bypass ordinary courts
for political crimes.
The Council introduced the *bocche di leone*,
marble reliefs carved into the image
of a lion's face
with a slot for inserting paper documents
containing complaints.
Boxes were placed in each *sestiere*
and in church walls.
Each box dealt with a specific category of complaint.

The bocche di leone
contained a significant structural restriction.
Denunciations generally were not anonymous.
Notes had to be signed
and include the signatures of several witnesses
to the complainant's good character.
Anonymous denunciations were accepted
only against public officials
who were misusing their power,
not against private individuals.

This distinction is important.
Anonymity was reserved specifically
for oversight of governmental authority.
The principle maps directly
to the concept of an anonymous telos auditor.
Anonymity is not general.
It is granted for a specific function.

### Grand Jury Secrecy

Grand jury secrecy
has endured as a fundamental principle
in American criminal procedure
for over four centuries.
The rationale encompasses five justifications.
It prevents the escape of those
whose indictment might be contemplated.
It ensures freedom of deliberation.
It prevents tampering with witnesses.
It encourages untrammeled disclosures
by persons with relevant information.
It protects the innocent accused
from unwarranted publicity.

Grand jury secrecy demonstrates
how anonymity and confidentiality
can serve institutional integrity
by insulating deliberative processes
from external pressure and manipulation.

### Inspector Generals and Ombudsmen

The Inspector General Act of 1978
established independent inspectors general
across the United States federal government.
Inspectors general are appointed
to conduct independent audits and investigations.
They report to both the agency head
and to Congress,
a dual-reporting structure
designed to insulate them
from the authority they oversee.
The Sarbanes-Oxley Act of 2002
extended similar principles
to publicly traded companies
by requiring audit committees
to establish procedures for confidential,
anonymous submission of concerns
by employees regarding accounting or auditing matters.

The pattern across these precedents is consistent.
Organizations have repeatedly found it necessary
to create roles whose function
is to challenge institutional alignment.
Many of these roles
incorporate anonymity or structural independence
as essential features,
not incidental ones.

## The Anonymous Telos Auditor

A cryptotelemeritocracy
is a telemeritocratic organization
augmented with an anonymous telos auditor.
The auditor is a member of the organization,
drawn from the employee pool,
who monitors organizational alignment
with the stated telos
and may intervene when misalignment is detected.

The auditor's identity is concealed
through cryptographic mechanisms.
All staff know that the auditor exists.
No staff member knows
who the auditor is.
The auditor operates from within the organization,
performing their regular duties
alongside their oversight function.
They observe the organization's decisions,
priorities, and trajectory
from the perspective
of an ordinary participant.

The anonymity serves three functions.

First, it eliminates halo effects.
If the auditor's identity were known,
their status, reputation, and social relationships
would influence how their interventions
are received.
Anonymity ensures that interventions
are evaluated on their substance
rather than on the authority of the speaker.

Second, it protects the auditor from retaliation.
An identified auditor who flags
inconvenient misalignment
faces pressure from those
whose authority depends on the current trajectory.
This is the same dynamic
that led to the weakening of the Devil's Advocate
and the erosion of inspector general independence.
Anonymity removes the primary mechanism
by which incumbents neutralize oversight.

Third, it reduces the political cost of monitoring.
Michael Jensen and William Meckling
established in their 1976 paper
"Theory of the Firm"
that monitoring has costs.
Agency costs are the sum
of monitoring costs incurred by the principal,
bonding costs incurred by the agent,
and residual loss.
The optimal level of monitoring
occurs where the marginal benefit
of additional monitoring
equals its marginal cost.
An anonymous auditor
potentially reduces monitoring costs
by eliminating the political overhead
associated with visible oversight.
There are no status negotiations,
no performance review anxieties,
and no career consequences
for the act of monitoring itself.

The auditor does not hold executive authority.
The auditor's power is the power to flag,
to compel review,
and to demand that the organization
explicitly reaffirm or revise its telos.
The auditor cannot dictate solutions.
The auditor can force the question.
This limitation is deliberate.
The auditor is a mechanism for detection,
not for correction.
Correction remains the responsibility
of the telemeritocratic governance structure itself.

## Auditor Mechanics

### Selection

The auditor is drawn
from a pool of eligible candidates
who are employed by the organization.
Eligibility criteria may vary
but should reflect demonstrated understanding
of the organizational telos
and sufficient tenure
to observe patterns over time.
The selection mechanism
must prevent the candidate pool
from being manipulated
by those whose authority
the auditor is meant to check.

### Appointment

The appointment may be temporary or pseudo-lifetime.
A temporary appointment
creates regular rotation,
reducing the risk that any single auditor
develops a distorted understanding of the telos.
A pseudo-lifetime appointment
provides continuity and insulates the auditor
from the pressure of reappointment politics.
Both approaches have precedent.
Grand juries serve fixed terms.
Inspectors general serve indefinitely.

The auditor may step down voluntarily.
Involuntary removal
requires action by the candidate pool,
not by organizational leadership.
This mirrors the sacrosanctity of the Roman tribune.
The auditor's protection comes
from the constituency they serve,
not from the hierarchy they oversee.

### Powers

The auditor's powers are limited
to those necessary for mission alignment oversight.
The auditor may observe organizational decisions
and their relationship to the stated telos.
The auditor may issue an intervention
when misalignment is detected.
An intervention compels the organization
to explicitly address the identified misalignment.
The organization must either correct the trajectory
or publicly reaffirm that the current trajectory
is consistent with the telos.
The auditor cannot unilaterally alter decisions,
remove personnel, or redirect resources.

### Communication Protocol

Interventions are channeled
through a protocol that preserves anonymity.
The intervention document
is cryptographically signed
in a manner that proves
the signer holds a valid auditor credential
without revealing which credential holder signed it.
This is the technical function
that gives cryptotelemeritocracy its name.

### Incentives

The auditor receives no material gain
beyond their regular compensation.
No special salary, bonus, or advancement
is attached to the auditor role.
This design choice
preserves impartiality
by eliminating financial incentives
for both overintervention and underintervention.

### Recall

The candidate pool
may replace an auditor
who fails to maintain alignment oversight.
Because the auditor's identity
is concealed from organizational leadership,
the recall mechanism operates
within the candidate pool itself.
This creates a two-level accountability structure.
The auditor is accountable to the candidate pool.
The candidate pool is accountable
to the organizational telos.

## Cryptographic Foundations

The "crypto" in cryptotelemeritocracy
refers to the cryptographic mechanisms
that enable the auditor's anonymity.
This is not anonymity by policy or convention.
It is anonymity enforced by mathematics.

### Anonymous Credentials

David Chaum proposed anonymous credential systems
in his 1985 paper
"Security without Identification."
In an anonymous credential system,
a credential holder can prove
that they possess certain attributes
without revealing their identity
or any information beyond the attributes shown.
A user never transmits the credential itself.
Instead, the user demonstrates
that the credential satisfies certain properties.

Applied to the telos auditor,
anonymous credentials allow the auditor
to prove that they hold a valid auditor appointment
without revealing which member of the candidate pool
they are.
The organization can verify
that an intervention comes from a legitimate auditor
without learning who issued it.

### Zero-Knowledge Proofs

A Zero-Knowledge Proof (ZKP)
is a protocol in which a prover
can convince a verifier
that a given statement is true
without conveying any information
beyond the truth of that statement.
In the context of a cryptotelemeritocracy,
zero-knowledge proofs enable the auditor
to demonstrate the validity
of their intervention authority
without exposing any identifying information.

The Minimal Anti-Collusion Infrastructure, or MACI,
demonstrates the practical feasibility
of this approach.
MACI is a private voting protocol
that uses Ethereum smart contracts,
encryption, and zero-knowledge proofs
to enable on-chain voting
where individual votes are private
but final results are public and verifiable.
No voter can reveal how they voted,
yet results are verifiable
with cryptographic proofs.

### Ring Signatures

Ring signatures enable a member of a group
to sign a message anonymously
by hiding the signer's identity
within a ring of multiple public keys.
Unlike group signatures,
ring signatures do not require fixed group membership.
Users select their own ring when signing.
Linkable ring signatures
maintain the property
that two signatures from the same signer
are publicly identifiable,
which prevents double-signing
while preserving anonymity.

For the telos auditor,
ring signatures offer a mechanism
by which the auditor can sign interventions
within the ring of all candidate pool members.
Any observer can verify
that the signature came from a candidate pool member
but cannot determine which one.

### The Venetian Principle

The cryptographic anonymity
in a cryptotelemeritocracy
follows what might be called the Venetian principle.
Anonymity is not general.
It is granted for a specific function.
The Venetian *bocche di leone*
accepted anonymous denunciations
only against officials misusing their power.
Similarly, the auditor's cryptographic anonymity
applies only to their oversight function.
The auditor is not anonymous
in their regular role as an employee.
Their anonymity is scoped
to the specific act of telos alignment oversight.

This scoping is important.
General anonymity in an organization
would undermine accountability.
Targeted anonymity
for a specific oversight function
preserves accountability for all other activities
while protecting the oversight function
from political interference.

## Risks and Failure Modes

Cryptotelemeritocracy has failure modes
that deserve explicit attention.

**Incompetent auditor.**
Anonymity protects mediocrity
as well as merit.
An auditor who misunderstands the telos
may issue interventions
that are incorrect, counterproductive,
or distracting.
Because the auditor is anonymous,
their competence cannot be directly evaluated
by organizational leadership.
The candidate pool bears responsibility
for selecting competent auditors,
but the pool's own competence is not guaranteed.

**Telos misinterpretation.**
The auditor's understanding of the telos
may differ from the organization's intended meaning.
If the telos is ambiguous,
the auditor may enforce
an interpretation that the organization
did not intend.
This risk increases
when the telos is stated in broad terms.
An auditor enforcing alignment with "innovation"
may have a very different understanding
of that word
than the organizational leadership.

**Staff resistance.**
Anonymous interventions
may be perceived as illegitimate,
paranoid, or authoritarian.
If staff do not understand the purpose
of the auditor role,
they may view interventions
as interference from an unaccountable authority.
The success of the model
depends on staff understanding
and accepting the governance structure
before they encounter an intervention.

**Authority exceeding mandate.**
The auditor's powers are designed
to be limited to flagging and compelling review.
In practice, an anonymous role
with the power to compel organizational attention
may acquire informal authority
beyond its formal mandate.
If interventions are perceived
as commands rather than questions,
the auditor becomes
an anonymous autocrat.

**Candidate pool capture.**
If the candidate pool is small,
the auditor's identity
may be inferrable through elimination.
If the pool is captured
by a faction within the organization,
the auditor becomes
an instrument of that faction
rather than a guardian of the telos.
The pool must be large enough
for genuine anonymity
and diverse enough
to resist factional capture.

**Surveillance atmosphere.**
The knowledge that an anonymous auditor exists
may create a culture of suspicion.
If staff believe they are being watched
by an unidentifiable colleague,
they may become risk-averse,
performative, or distrustful.
The intended effect is alignment.
The unintended effect
may be organizational anxiety.

**Erosion over time.**
Like the Devil's Advocate,
the auditor role may be weakened
by leadership that finds oversight inconvenient.
Cryptographic anonymity
makes the auditor harder to identify and dismiss
than a named officeholder,
but it does not make the role invulnerable.
If leadership eliminates the candidate pool,
changes the selection criteria,
or ignores interventions without consequence,
the role becomes ceremonial.

## When Not to Use Cryptotelemeritocracy

Cryptotelemeritocracy is not appropriate
in every organizational context.

When the telos is contested or undefined,
there is nothing for the auditor to audit.
The model requires a telos
that is clearly stated and broadly accepted.
If the organization has not yet agreed
on its purpose,
it needs to resolve that question
before adding an oversight mechanism.

When the organization is too small,
anonymity is not credible.
If the candidate pool consists of three people,
any intervention
effectively narrows the auditor's identity
to one of three candidates.
The model requires sufficient organizational size
for the anonymity to be genuine.

When the candidate pool
lacks the competence to evaluate telos alignment,
the auditor role
becomes a source of noise rather than signal.
The model assumes that the organization
contains members who understand the telos
well enough to detect drift.
If that assumption is false,
the mechanism fails.

When transparent oversight mechanisms are sufficient,
cryptographic anonymity adds complexity
without proportional benefit.
An organization with a strong culture
of open dissent and transparent governance
may not need anonymous oversight.
The model is designed for contexts
where visible oversight
is structurally compromised
by the very dynamics it is meant to check.

When the overhead of cryptographic infrastructure
exceeds the benefit,
the model is impractical.
Implementing anonymous credentials,
zero-knowledge proofs,
or ring signatures
requires technical expertise
and ongoing maintenance.
For a small engineering team
with a clear and stable purpose,
the governance costs
may exceed the governance benefits.

## Summary

Cryptotelemeritocracy extends telemeritocracy
with a structural mechanism
for detecting mission drift.
The extension is an anonymous telos auditor,
a member of the organization
whose identity is concealed
through cryptographic mechanisms,
who monitors alignment
with the organization's stated purpose
and may intervene when misalignment is detected.

The problem it addresses is well established.
Merton, Michels, and Selznick
all documented the tendency
of organizations to deviate
from their founding purpose.
Telemeritocracy, which defines authority
relative to the telos,
is particularly vulnerable to this dynamic
because a drifting telos
silently redefines merit
and selects for leaders
who are adapted to the drifted state.

The solution it proposes has precedent.
Athenian ostracism, Roman tribunes,
the Devil's Advocate,
Venetian denunciation boxes,
grand jury secrecy,
and modern inspector general systems
all demonstrate that organizations
have repeatedly created roles
whose function is to challenge institutional alignment.
Many of these roles incorporate anonymity
or structural independence as essential features.

The cryptographic component
distinguishes this model from its historical precedents.
Anonymous credentials, zero-knowledge proofs,
and ring signatures
provide mathematically enforced anonymity
that does not depend on policy, convention,
or the goodwill of those being overseen.
Practical systems like the Minimal Anti-Collusion Infrastructure
and Snapshot's shielded voting
demonstrate that this technology is deployable.

The model is not without risks.
Incompetent auditors, telos misinterpretation,
staff resistance, authority creep,
candidate pool capture,
surveillance atmospheres,
and erosion over time
are all failure modes
that require explicit attention.
The model is inappropriate
for small organizations,
those with contested purposes,
those lacking competent candidate pools,
and those where transparent oversight
already functions well.

For organizations that operate
under telemeritocratic governance,
that face genuine risks of mission drift,
and that have sufficient size and technical capacity,
cryptotelemeritocracy offers
a principled structural mechanism
for preserving alignment
between organizational authority
and organizational purpose.

## Future Reading

The organizational theory
underlying the mission drift problem
begins with Robert Michels's *Political Parties*
and its iron law of oligarchy,
continues through Philip Selznick's
*TVA and the Grass Roots*
and its analysis of institutional cooptation,
and extends into the modern mission drift literature
on social enterprises and microfinance.
Michael Jensen and William Meckling's
"Theory of the Firm"
provides the economic framework
for analyzing monitoring costs
and agency relationships.

The cryptographic foundations
draw from David Chaum's work on anonymous credentials
and the subsequent development
of zero-knowledge proofs
and ring signatures.
The Minimal Anti-Collusion Infrastructure
provides a practical reference implementation
of cryptographic privacy in governance contexts.

The companion articles on
[telemeritocracy][related_post_telemeritocracy]
and mission command
provide the governance framework
that cryptotelemeritocracy extends.
The historical precedents discussed in this article
are covered in greater depth
in the referenced works
on Roman tribunes, Athenian ostracism,
and the Venetian Council of Ten.

## References

- [Book, Political Parties][book_political_parties]
- [Book, TVA and the Grass Roots][book_tva]
- [Reference, Devil's Advocate][ref_devils_advocate]
- [Reference, Inspector General Act of 1978][ref_ig_act]
- [Reference, MACI][ref_maci]
- [Reference, Ostracism][ref_ostracism]
- [Reference, Sarbanes-Oxley Whistleblower Provisions][ref_sox]
- [Reference, Tribune of the Plebs][ref_tribune]
- [Reference, Venetian Council of Ten][ref_council_ten]
- [Related Post, Telemeritocracy][related_post_telemeritocracy]
- [Research, Anonymous Credentials][research_chaum]
- [Research, Goal Displacement in Bureaucracies][research_merton]
- [Research, Mission Drift in Social Enterprises][research_mission_drift]
- [Research, Ring Signatures and Group Signatures][research_ring_signatures]
- [Research, Theory of the Firm][research_jensen_meckling]

[book_political_parties]: https://en.wikipedia.org/wiki/Political_Parties_(book)
[book_tva]: https://en.wikipedia.org/wiki/Philip_Selznick
[ref_devils_advocate]: https://www.britannica.com/topic/devils-advocate
[ref_ig_act]: https://www.ignet.gov/content/ig-act
[ref_maci]: https://maci.pse.dev/
[ref_ostracism]: https://en.wikipedia.org/wiki/Ostracism
[ref_sox]: https://www.whistleblowers.gov/statutes/sox_amended
[ref_tribune]: https://en.wikipedia.org/wiki/Tribune_of_the_plebs
[ref_council_ten]: https://en.wikipedia.org/wiki/Council_of_Ten
[related_post_telemeritocracy]: {% post_url 2026-02-19-telemeritocracy %}
[research_chaum]: https://chaum.com/security-without-identification/
[research_merton]: https://www.ebsco.com/research-starters/social-sciences-and-humanities/mertons-dysfunctions-bureaucracies
[research_mission_drift]: https://www.researchgate.net/publication/265969563_Understanding_and_combating_mission_drift_in_social_enterprises
[research_ring_signatures]: https://www.mdpi.com/2410-387X/6/1/3
[research_jensen_meckling]: https://www.sciencedirect.com/science/article/pii/0304405X7690026X
