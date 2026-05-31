---
layout: post
mathjax: false
comments: true
title:  "Three Audiences for an Operating System"
date:   2026-05-22 09:00:00 +0000
categories: operating-systems philosophy hci
---

<!-- A119 -->
<script>console.log("A119");</script>

An operating system
serves people.
The shipping
operating systems of 2026,
namely
[Microsoft Windows][ref_windows],
[macOS][ref_macos],
[the contemporary Linux distributions][ref_linux],
[Android][ref_android],
[iOS][ref_ios],
and their relatives,
serve two audiences well
and a third audience
poorly or not at all.
This article identifies
the three audiences,
sketches what each requires,
and observes
that the third audience,
namely the operator-as-end-user,
has not had
a contemporary operating system
designed for it.
The article does not propose
a solution.
Its purpose is
to name the category
that successor articles
in this series
attempt to fill.

The framing
that an operating system
has more than one audience
is not original.
[The Macintosh Human Interface Guidelines][ref_apple_hig],
[the Microsoft Windows User Experience Guidelines][ref_msft_uxg],
the
[Unix philosophy][ref_unix_philosophy],
[the GNOME Human Interface Guidelines][ref_gnome_hig],
and the
[KDE Human Interface Guidelines][ref_kde_hig]
each
target a population
and articulate
the design choices
that follow.
What is missing
is a contemporary
counterpart to these documents
for the third audience.
The Apollo flight team
had operator-facing computing
in the 1960s.
The contemporary cockpit
has glass instruments
designed under
[ARINC 661][ref_arinc_661].
The contemporary process plant
has supervisory control and data acquisition
displays
designed under
[ISA-101][ref_isa_101].
The contemporary
medical imaging console
has usability engineering
under
[IEC 62366][ref_iec_62366].
None of these
runs on a general-purpose operating system
that has been designed
for the operator audience.
They run on industrial systems
or on consumer or developer
operating systems
that the integrators
have bent into shape.

## The Three Audiences

The three audiences
are the consumer,
the developer,
and the operator.
The category names
are intentionally functional.
A single human being
can occupy
any of the three roles
at different times,
including within
a single working day.
The category
refers to the role
the user plays
when interacting with the system,
not to the human
who plays the role.

**The consumer
is the user
whose work
is primarily
read or watch
or send or buy.**
The consumer
opens a browser,
opens a mail client,
opens a streaming application,
opens a messenger,
opens a spreadsheet
to balance a checkbook,
or opens a photo viewer
to see a child's birthday.
The work is
serial,
loosely time-constrained,
and the artifacts
are mostly transient.
The interface
should
be familiar,
forgiving,
visually pleasant,
and consistent
with the rest
of the consumer's
software experience.

**The developer
is the user
whose work
is primarily
read source,
write source,
run programs,
inspect failures,
and version control.**
The developer
opens a text editor,
a terminal,
a version control client,
a debugger,
a profiler,
and a documentation viewer.
The work is
parallel,
interruption-tolerant,
and the artifacts
are
typed text
under
version control.
The interface
should
expose the system,
favour keyboard control,
admit composition
of small tools,
and reward
investment in customisation.

**The operator
is the user
whose work
is primarily
monitor, decide, command,
and document.**
The operator
sits at a console
that displays
the state
of an external system
under the operator's authority.
The console
shows trajectory tracks,
or vehicle health,
or patient vital signs,
or factory machine status,
or aircraft separation,
or transmission grid voltage.
The operator
reads the display,
applies a decision
under a written rule,
issues a command,
and records the action.
The work is
deadline-bound,
audit-bound,
and the artifacts
are typed records
of decisions
with verifiable provenance.
The interface
should
present typed information
under bounded latency,
distinguish trusted
from untrusted content,
expose composition
of typed parts,
and record
every operator action
in a form
the certification authority can review.

These three roles
are not exhaustive.
A computer scientist
running a long simulation
is a researcher,
which is partly developer
and partly operator.
A graphic designer
is a creative professional,
which is partly consumer
of media
and partly developer
of new artifacts.
A military analyst
is partly operator
of an intelligence platform
and partly developer
of new queries.
The boundaries are
soft.
What matters
is that the operator role
has structural requirements
that neither
the consumer role
nor the developer role
addresses,
and that those requirements
have not been served
by a shipping operating system
designed for the role.

## The Consumer Answer

The mass-market operating system
of 2026
is the consumer answer.
The file-and-application model,
the icon-and-menu interface,
the read-and-then-edit workflow,
and the application-store distribution channel
are all consumer optimisations.
The contemporary
[Windows User Experience Guidelines][ref_msft_uxg],
[the macOS Human Interface Guidelines][ref_apple_hig],
[the iOS Human Interface Guidelines][ref_apple_hig],
and the Android Material Design system
are sophisticated documents
that articulate the consumer answer
in considerable depth.
The mass-market consumer
has never had it so good.

The consumer answer
is correct
for the audience it serves.
Several billion people
use these systems daily.
The work the consumer does
matches the model the system offers.
A document
opened in a word processor
that closes the document
to switch to a spreadsheet
loses nothing
the consumer cares about.
A photograph
exported as a flat image
to send to a friend
loses metadata
the friend will not miss.
A browser session
that crashes
and reloads
loses the state the consumer
was willing to lose.
The lossy import-export model
is acceptable
because the consumer's tolerance
for loss
matches the model's lossy default.

What the consumer answer
does not serve
is the audience
whose tolerance for loss
is lower.

## The Developer Answer

The developer answer
is older than
the consumer answer.
The
[Unix philosophy][ref_unix_philosophy]
of small composable tools,
the text-as-universal-interface convention,
the programmer's editor tradition
from
[Emacs][ref_emacs] and
[Vim][ref_vim] through
[Visual Studio Code][ref_vscode],
the version-control culture
around
[Git][ref_git],
and the package-manager ecosystem
around
[Cargo][ref_cargo],
[npm][ref_npm], and
[pip][ref_pip],
are all developer answers.
A developer
at a workstation
in 2026
runs a Unix-derived operating system
or a Unix-derived environment
on top of Windows,
because the developer answer
is overwhelmingly Unix-shaped.

The developer answer
is correct
for the audience it serves.
A developer
who customises the editor,
configures the shell,
scripts the build,
and version-controls the result
is exercising
exactly the affordances
the system provides.
The lossy import-export model
is replaced
by the round-trip-clean
text formats that
the developer ecosystem
agrees on.
Every artifact
is text
or addressable bytes
in a content store.
Every change
is recorded
under cryptographic identity.

What the developer answer
does not serve
is the audience
whose work
is not the production
of new programs
but the operation
of existing systems
under written authority.

## The Operator

The operator audience
is what an operating system
should serve
when the user
is sitting at a console
that watches an external system
and the user's authority
to act
is written down.

The user's authority
is the load-bearing concept.
A consumer
who opens a document
has no formal authority
beyond ownership.
A developer
who runs a program
has authority
to commit the code
under the project's review rules.
An operator
has authority
defined by an external document,
namely a procedure,
a rule,
a policy,
a certification,
or a regulation.
The operator's action
is admissible
when it conforms
to the authority.
The operator's action
is inadmissible
when it violates the authority.
The system's job
is to make
the admissible action
easy
and the inadmissible action
either impossible
or audited.

The operator audience
appears whenever
the system being operated
has consequences
beyond the operator's
immediate work.
A flight controller
operates a launch vehicle.
A radiologist
operates an imaging device.
A power dispatcher
operates a transmission grid.
An air traffic controller
operates an airspace.
A nuclear reactor operator
operates a generating station.
A chemical plant operator
operates a refinery.
An intelligence analyst
operates a fusion platform
that synthesises classified information.
A regulatory affairs specialist
operates a submission system
that the regulator reviews.
A clinical researcher
operates an electronic data capture system
under a trial protocol.
A penetration tester
operates a controlled environment
under a written engagement scope.
A legal reviewer
operates a discovery platform
under a protective order.

These users
share a structural pattern.
The work is
deadline-bound, audit-bound,
authority-bound,
and consequential
beyond the user's
immediate session.
The artifacts
are typed records
of decisions.
The interface
must present
typed information
under
bounded latency.
The certification authority
must be able to review
the trail.
The system itself
must distinguish
trusted from untrusted content
and prevent
silent contamination.

## A Short History of Operator-Facing Computing

Operator-facing computing
predates the consumer
and the developer audiences.
The earliest interactive computer systems
were operator consoles.
[Ivan Sutherland's Sketchpad][ref_sketchpad]
at MIT Lincoln Laboratory in 1963
was an operator station
for an engineering design task.
[Doug Engelbart's NLS][ref_nls],
demonstrated in 1968,
was a knowledge-worker console
in which the operator
composed
typed parts
with typed links
under explicit authority.
The Apollo
[Mission Operations Control Room][ref_mocr],
operating from 1965 onward,
was the
largest operator-facing installation
of its era.
The contemporary
[glass cockpit][ref_glass_cockpit]
inherits the
Apollo console tradition.

The personal computer revolution
of the late 1970s and 1980s
moved interactive computing
toward
the consumer audience.
[The Xerox Alto][ref_alto],
[the Apple Macintosh][ref_macintosh],
[Microsoft Windows][ref_windows],
and their successors
optimised
for personal productivity,
not for operator-facing work.
[BTRON][ref_btron],
the Business TRON
subproject of Sakamura's
TRON Project,
attempted
to serve operator-facing computing
in a personal-computer form factor
but did not achieve
the mass-market adoption
its sibling
[ITRON][ref_itron]
achieved in embedded systems.
The hypermedia tradition
of
[HyperCard][ref_hypercard],
[OpenDoc][ref_opendoc],
and
[GNOME Bonobo][ref_bonobo]
attempted
typed-part composition
in consumer form
but did not survive
the consumer-market shift
to the World Wide Web.

The operator-facing computing tradition
survived
in industrial form.
[Supervisory Control and Data Acquisition][ref_scada]
systems
in process industries,
the
[Programmable Logic Controllers][ref_plc]
that drive
factory floors,
the
[ARINC 661][ref_arinc_661]
cockpit displays in aviation,
the
[ISA-101][ref_isa_101]
process control human-machine interfaces,
the
[NUREG-0700][ref_nureg_0700]
nuclear control room
displays,
the
[IEC 62366][ref_iec_62366]
medical device usability framework,
and the
[ISO 9241][ref_iso_9241]
ergonomics of human-system interaction
family
all describe
operator-facing computing
without calling it that.
Each describes the requirements
for a specific operator industry
without proposing
a general-purpose operating system
to satisfy them.
The
[Abnormal Situation Management Consortium][ref_asm_consortium]
guidelines
for high-performance human-machine interfaces
in process industries
are the closest contemporary
attempt at a cross-industry
operator-facing design statement.

The contrast
with the consumer
and developer traditions
is structural.
The consumer tradition
ships a general-purpose operating system
that defines a coherent design language
for the audience.
The developer tradition
ships
several general-purpose operating systems
that define
coherent design languages
for the developer audience.
The operator tradition
ships
industry-specific systems
that do not compose
across industries
and do not benefit
from a shared operating system layer.

## Why the Consumer Answer Fails the Operator

The mass-market operating system
fails the operator
in several structural ways.

**The application owns the file.**
The operator's authority
attaches to
a typed part inside a document,
not to a file.
The mass-market model
hides the part
inside the application
that opened the file.
A flight rule
that the operator must apply
is buried
inside a portable document file
or inside a vendor-specific
document management system.
The operator cannot
address the rule directly
through the operating system
the way the operator can
address a process
or a file
or a network connection
on a Unix system.

**The interface is optimised
for casual use.**
The consumer operating system
hides system state
behind progressive disclosure
intended to reduce
the cognitive cost
for the casual user.
The operator
needs
the opposite.
The operator wants
maximum information density
under the operator's
existing mental model.
The
[Abnormal Situation Management Consortium][ref_asm_consortium]
high-performance HMI guidelines
make exactly this point
for industrial control rooms.

**Latency is best-effort.**
The mass-market operating system
admits arbitrary user code,
admits dynamic memory allocation
without bound,
and admits garbage collection
without deadline.
The operator console
needs bounded latency
on the surfaces that drive
operator decisions.
The mass-market answer
cannot provide it
without
a real-time patch
that the operator's
employer must integrate
and certify.

**Provenance is bolted on.**
The mass-market operating system
provides no platform-level
audit trail.
The operator's organisation
adds an enterprise document management system
or a session recorder
or a screen capture system
to satisfy
the certification authority.
Each addition
is bespoke,
expensive, and partial.

**The trust model is binary.**
The mass-market operating system
distinguishes
the user from
the system administrator.
The operator needs
finer-grained
trust labels
on information,
not on user accounts.
An untrusted telemetry source
must not contaminate
a trusted display surface,
regardless of
which user account
is logged in.

The operator can run
the mass-market operating system
and discharge
the operator's responsibilities
through external scaffolding.
The cost of the scaffolding
is borne
by every operator-facing program
that ships,
because there is no shared
operating system layer
that addresses the requirements.

## Why the Developer Answer Also Fails

The developer answer
is closer to the operator's needs
than the consumer answer.
The Unix philosophy
of typed text streams,
the version control discipline,
the package manager
that addresses code
by content hash,
and the keyboard-driven
composition of small tools
all map onto
the operator's
typed-information-with-provenance
requirement
better than the
icon-and-menu
consumer answer maps.

The developer answer
nonetheless fails
the operator
for several reasons.

**The developer audience
authors programs.**
The operator audience
operates them.
The text editor,
the version control system,
the package manager,
and the build tools
are oriented toward
the production
of new artifacts.
The operator
consumes
typed information
about an external system
and produces
typed records of decisions.
The developer's tools
do not match
this shape.

**The developer's trust model
is about source provenance.**
A Git commit
is signed by an author
and reviewed by a committer.
The operator's trust model
is about
information provenance
at the granularity
of a single
typed part
of a document
at a single moment
in operational time.
The developer's tools
do not address
information at that granularity.

**The developer's latency model
is best-effort.**
A compiler
that takes ten seconds longer
than expected
inconveniences the developer
but does not violate
a deadline.
An operator surface
that misses a deadline
violates the operator's
written procedure
and may invalidate
the operator's action.

**The developer's display
is dense, textual,
and tuned to the developer's
mental model
of source code.**
The operator's display
is dense, typed, and tuned
to the operator's
mental model
of the external system.
The two density requirements
are similar
but the underlying
mental models differ.
A developer environment
shows lexically structured text
in fixed-width fonts.
An operator environment
shows
trajectory plots,
trend charts,
schematic diagrams,
and alarm lists,
all simultaneously
and all live.

The developer answer
is closer than the consumer answer
but still does not target
the operator audience.

## The Operator Population Today

The operator population
in 2026
is large,
well funded,
and underserved
by general-purpose computing.

Aerospace operations,
including launch control,
mission operations,
and air traffic management,
employ tens of thousands
of operators
in the United States alone.
The
[Federal Aviation Administration][ref_faa]
operates
[en route automation systems][ref_eram]
at twenty-one
air traffic control centres.
[Eurocontrol][ref_eurocontrol]
operates the European equivalent.
The
[National Aeronautics and Space Administration][ref_nasa]
operates
crewed mission control
at the Johnson Space Center
and uncrewed mission control
at the Jet Propulsion Laboratory.
Commercial launch operators
including SpaceX, Blue Origin,
and Rocket Lab
operate their own control rooms.

Medical operations,
including imaging,
intraoperative monitoring,
intensive care,
and surgical robotics,
employ hundreds of thousands
of operators
in clinical settings worldwide.
The applicable usability standard
is
[IEC 62366][ref_iec_62366].
The software lifecycle standard
is
[IEC 62304][ref_iec_62304].
The U.S. regulatory authority
is the
[Food and Drug Administration][ref_fda].

Industrial operations,
including process plants,
power generation,
transmission grid management,
and manufacturing control,
employ
millions of operators globally.
The applicable HMI standard
is
[ISA-101][ref_isa_101].
The functional safety standard
is
[IEC 61508][ref_iec_61508].
The nuclear domain
adds
[NUREG-0700][ref_nureg_0700].

Defense and intelligence operations,
including intelligence analysis,
command and control,
and ground station operations,
employ
unknown numbers of operators
under classification.
The relevant
public-facing infrastructure tradition
includes the
[Joint Worldwide Intelligence
Communications System][ref_jwics]
and the related platforms
operated by
the
[Defense Information Systems Agency][ref_disa]
and its peer organisations.

Legal and regulatory operations,
including electronic discovery,
litigation review,
mergers and acquisitions due diligence,
and regulatory submission management,
employ hundreds of thousands
of operators
worldwide.
The platforms
they use
include
[Relativity][ref_relativity],
[iManage Work][ref_imanage],
and bespoke
in-house systems
at large law firms
and accounting firms.

Financial market operations,
including trading floors,
treasury management,
and clearing-house operations,
employ
hundreds of thousands
of operators
under regulatory frameworks
including the
[Markets in Financial Instruments Directive][ref_mifid],
[the Dodd-Frank Act][ref_dodd_frank],
and the
[Sarbanes-Oxley Act][ref_sox].

The combined population
is in the millions.
The combined budget
is in the tens of billions
of US dollars annually.
The combined regulatory weight
is global.
This population
does not have
a general-purpose operating system
designed for the work it does.

## A Scorecard of Audience Requirements

The structural differences
among the three audiences
can be presented
as a scorecard
of requirements
under which each audience
operates.

| Property | Consumer | Developer | Operator |
|---|---|---|---|
| Primary verb | Read, watch, communicate, buy | Read, write, run, debug, version | Monitor, decide, command, document |
| Authority model | Ownership | Project review rules | Written external authority |
| Artifact lifetime | Transient | Source-controlled history | Audited for decades |
| Latency tolerance | Best-effort acceptable | Best-effort acceptable | Bounded required |
| Trust model | Per-user account | Per-source-commit signature | Per-information-part label |
| Composition unit | Application owning file | Pipe-connected text tools | Typed handler on typed part |
| Provenance | Optional metadata | Per-commit signed history | Intrinsic at every operation |
| Display density | Low, progressive disclosure | High, lexical | High, typed-information-mental-model |
| Failure cost | Annoyance | Rework | Money, safety, liability |
| Certification posture | None | Internal review | External regulator |

The columns are not strict.
A given individual
may move
across the table
in a single day.
The columns
characterise the role,
not the human.

What the scorecard shows
is that the operator column
has no general-purpose
operating system
designed for it.
The consumer column
has many.
The developer column
has many.
The operator column
has industry-specific
systems
that do not share
a layer.

## The Gap That Remains

The unfilled cell
of the audience table
is the third column,
the operator.
The gap is not a failure
of the consumer or developer audiences.
The consumer answer
is correct
for the consumer.
The developer answer
is correct
for the developer.
The gap is the absence
of an operator-facing
general-purpose operating system
that would
do for the operator
what the mass-market consumer system
does for the consumer
and the Unix-derived developer system
does for the developer.

The gap is not new.
Operator-facing computing
has been
under-served
since the personal computer
revolution
moved the centre of gravity
toward the consumer.
The
[BTRON][ref_btron]
project of the 1980s
attempted to address it.
The
[OpenDoc][ref_opendoc]
project of the 1990s
attempted to address it
from a different direction.
[Lotus Notes][ref_hcl_notes]
addressed parts of it
for the enterprise document use case.
[Palantir Gotham and Foundry][ref_palantir_foundry]
address parts of it
for intelligence and enterprise data fusion.
Each effort
covered a fraction
of the operator requirements
and none
proposed a general-purpose
operator-facing operating system.

The gap is also not
a problem of engineering capability.
The components needed
to build an operator-facing operating system
exist.
[Capability-secure microkernels][ref_sel4]
exist.
[Component-based operating system frameworks][ref_genode]
exist.
[Local-first collaboration libraries][ref_automerge]
exist.
[Content-addressed storage][ref_content_addressable_storage]
exists.
[Browser-class rendering engines][ref_servo]
exist.
[Verified bytecode component models][ref_wasm_component_model]
exist.
A team of competent engineers
with a decadal horizon
could compose these
into a credible
operator-facing operating system.

The gap is a problem
of incentive,
of audience identification,
of vertical-versus-general strategy,
and of the conceptual move
required to recognise
the operator as a first-class audience.
The consumer and developer markets
attracted
the platform investment
of the 1980s
through 2010s.
The operator market
did not.
The operator market
was small
in each individual industry,
even though
the cross-industry total
was substantial.
The cross-industry total
remained invisible
because no platform
existed to address it.

## Out of Scope

This article restricts itself
to naming the category.
Three substantive topics
are deliberately deferred
to follow-up articles
in this series.

The first deferred topic
is the design of a successor
operator-facing operating system.
The shape of such a system,
namely the substrate,
the document model,
the user-interface conventions,
the trust model,
and the audit infrastructure,
is the subject of
[the next article in this series][related_post_btron_hypermedia],
which proposes
a hypermedia desktop
on a real-time substrate
in the BTRON lineage.

The second deferred topic
is the choice of language
in which such a system
would be built.
The selection criteria
are the subject of
[a further article][related_post_keleusma_substrate]
which assesses Keleusma
as a language-level substrate.

The third deferred topic
is the worked example
of a specific operator vertical.
The illustrative vertical
is the subject of
[a third article][related_post_apollo_vertical]
which uses human spaceflight ground systems
in the Apollo lineage
as a worked example
with explicit extrapolation
to contemporary requirements.

The trilogy
that follows this article
addresses the substantive
"what would it look like" question.
This article
addresses only
the prior question
of who the system serves
and why
the operator audience
has gone unserved.

## Conclusion

An operating system serves people.
The shipping operating systems of 2026
serve the consumer audience
and the developer audience
well.
The operator audience
is the third population
whose work
neither answer fits.
The operator
sits at a console
under written authority,
monitors an external system,
applies a decision under a rule,
commands the system,
and records the action.
The latency budget,
the trust model,
the audit posture,
and the composition idiom
that the operator's work requires
have no
shipping general-purpose
operating system
to address them.

The category is real.
The population is millions.
The combined budget
is in tens of billions
of dollars annually.
The regulatory weight
is global.
The engineering components
to build an operator-facing
operating system
all exist.
What has not existed
is the conceptual move
to name the audience
and a credible platform program
to serve it.

The articles
that follow this one
attempt that move.
They do not assume
the operator category
is settled.
They argue for it
on structural grounds,
propose a substrate,
and walk through
a worked example.
This article's purpose
is to mark the question
those articles
take up.

## References

- [Reference, Abnormal Situation Management Consortium][ref_asm_consortium]
- [Reference, Android Operating System][ref_android]
- [Reference, Apple Human Interface Guidelines][ref_apple_hig]
- [Reference, Apple Macintosh][ref_macintosh]
- [Reference, ARINC 661 Cockpit Display System Standard][ref_arinc_661]
- [Reference, Automerge Conflict-Free Replicated Data Type Library][ref_automerge]
- [Reference, BTRON][ref_btron]
- [Reference, Cargo Rust Package Manager][ref_cargo]
- [Reference, Content-addressable Storage][ref_content_addressable_storage]
- [Reference, Defense Information Systems Agency][ref_disa]
- [Reference, Dodd-Frank Wall Street Reform and Consumer Protection Act][ref_dodd_frank]
- [Reference, Emacs Text Editor][ref_emacs]
- [Reference, En Route Automation Modernization][ref_eram]
- [Reference, Eurocontrol][ref_eurocontrol]
- [Reference, Federal Aviation Administration][ref_faa]
- [Reference, Food and Drug Administration][ref_fda]
- [Reference, Genode Operating System Framework][ref_genode]
- [Reference, Git Version Control System][ref_git]
- [Reference, Glass Cockpit][ref_glass_cockpit]
- [Reference, GNOME Bonobo][ref_bonobo]
- [Reference, GNOME Human Interface Guidelines][ref_gnome_hig]
- [Reference, HCL Notes][ref_hcl_notes]
- [Reference, HyperCard][ref_hypercard]
- [Reference, IEC 61508 Functional Safety Standard][ref_iec_61508]
- [Reference, IEC 62304 Medical Device Software Lifecycle Processes][ref_iec_62304]
- [Reference, IEC 62366 Usability Engineering for Medical Devices][ref_iec_62366]
- [Reference, iManage Work][ref_imanage]
- [Reference, iOS Operating System][ref_ios]
- [Reference, ISA-101 Human Machine Interfaces for Process Automation Systems][ref_isa_101]
- [Reference, ISO 9241 Ergonomics of Human-System Interaction][ref_iso_9241]
- [Reference, ITRON][ref_itron]
- [Reference, Joint Worldwide Intelligence Communications System][ref_jwics]
- [Reference, KDE Human Interface Guidelines][ref_kde_hig]
- [Reference, Linux Operating System Family][ref_linux]
- [Reference, Markets in Financial Instruments Directive][ref_mifid]
- [Reference, Microsoft Windows][ref_windows]
- [Reference, macOS Operating System][ref_macos]
- [Reference, Microsoft Windows User Experience Guidelines][ref_msft_uxg]
- [Reference, Mission Operations Control Room][ref_mocr]
- [Reference, National Aeronautics and Space Administration][ref_nasa]
- [Reference, NLS oN-Line System][ref_nls]
- [Reference, npm Node Package Manager][ref_npm]
- [Reference, NUREG-0700 Human-System Interface Design Review Guidelines][ref_nureg_0700]
- [Reference, OpenDoc][ref_opendoc]
- [Reference, Palantir Foundry][ref_palantir_foundry]
- [Reference, Pip Python Package Installer][ref_pip]
- [Reference, Programmable Logic Controller][ref_plc]
- [Reference, Relativity Electronic Discovery Platform][ref_relativity]
- [Reference, Sarbanes-Oxley Act][ref_sox]
- [Reference, Servo Browser Engine][ref_servo]
- [Reference, seL4 Microkernel][ref_sel4]
- [Reference, Sketchpad][ref_sketchpad]
- [Reference, Supervisory Control and Data Acquisition][ref_scada]
- [Reference, Unix Philosophy][ref_unix_philosophy]
- [Reference, Vim Text Editor][ref_vim]
- [Reference, Visual Studio Code][ref_vscode]
- [Reference, WebAssembly Component Model][ref_wasm_component_model]
- [Reference, Xerox Alto][ref_alto]
- [Related Post, BTRON Hypermedia and the Real-Time Desktop][related_post_btron_hypermedia]
- [Related Post, Human Spaceflight Ground Systems as an Illustrative Vertical for a Hypermedia Desktop][related_post_apollo_vertical]
- [Related Post, Keleusma as a Substrate for a Real-Time Hypermedia Desktop][related_post_keleusma_substrate]

[ref_alto]: https://en.wikipedia.org/wiki/Xerox_Alto
[ref_android]: https://en.wikipedia.org/wiki/Android_(operating_system)
[ref_apple_hig]: https://developer.apple.com/design/human-interface-guidelines/
[ref_arinc_661]: https://en.wikipedia.org/wiki/ARINC_661
[ref_asm_consortium]: https://www.asmconsortium.net/
[ref_automerge]: https://automerge.org/
[ref_bonobo]: https://en.wikipedia.org/wiki/Bonobo_(component_model)
[ref_btron]: https://en.wikipedia.org/wiki/BTRON
[ref_cargo]: https://doc.rust-lang.org/cargo/
[ref_content_addressable_storage]: https://en.wikipedia.org/wiki/Content-addressable_storage
[ref_disa]: https://en.wikipedia.org/wiki/Defense_Information_Systems_Agency
[ref_dodd_frank]: https://en.wikipedia.org/wiki/Dodd%E2%80%93Frank_Wall_Street_Reform_and_Consumer_Protection_Act
[ref_emacs]: https://www.gnu.org/software/emacs/
[ref_eram]: https://en.wikipedia.org/wiki/En_Route_Automation_Modernization
[ref_eurocontrol]: https://www.eurocontrol.int/
[ref_faa]: https://www.faa.gov/
[ref_fda]: https://www.fda.gov/
[ref_genode]: https://genode.org/
[ref_git]: https://git-scm.com/
[ref_glass_cockpit]: https://en.wikipedia.org/wiki/Glass_cockpit
[ref_gnome_hig]: https://developer.gnome.org/hig/
[ref_hcl_notes]: https://en.wikipedia.org/wiki/HCL_Notes
[ref_hypercard]: https://en.wikipedia.org/wiki/HyperCard
[ref_iec_61508]: https://en.wikipedia.org/wiki/IEC_61508
[ref_iec_62304]: https://en.wikipedia.org/wiki/IEC_62304
[ref_iec_62366]: https://en.wikipedia.org/wiki/IEC_62366
[ref_imanage]: https://imanage.com/product/imanage-work/
[ref_ios]: https://en.wikipedia.org/wiki/IOS
[ref_isa_101]: https://www.isa.org/standards-and-publications/isa-standards/isa-101-standards
[ref_iso_9241]: https://en.wikipedia.org/wiki/ISO_9241
[ref_itron]: https://en.wikipedia.org/wiki/ITRON_project
[ref_jwics]: https://en.wikipedia.org/wiki/Joint_Worldwide_Intelligence_Communications_System
[ref_kde_hig]: https://develop.kde.org/hig/
[ref_linux]: https://en.wikipedia.org/wiki/Linux
[ref_macintosh]: https://en.wikipedia.org/wiki/Macintosh
[ref_macos]: https://en.wikipedia.org/wiki/MacOS
[ref_mifid]: https://en.wikipedia.org/wiki/Markets_in_Financial_Instruments_Directive_2014
[ref_mocr]: https://en.wikipedia.org/wiki/Christopher_C._Kraft_Jr._Mission_Control_Center
[ref_msft_uxg]: https://learn.microsoft.com/en-us/windows/apps/design/
[ref_nasa]: https://www.nasa.gov/
[ref_nls]: https://en.wikipedia.org/wiki/NLS_(computer_system)
[ref_npm]: https://www.npmjs.com/
[ref_nureg_0700]: https://www.nrc.gov/reading-rm/doc-collections/nuregs/staff/sr0700/
[ref_opendoc]: https://en.wikipedia.org/wiki/OpenDoc
[ref_palantir_foundry]: https://www.palantir.com/platforms/foundry/
[ref_pip]: https://pip.pypa.io/
[ref_plc]: https://en.wikipedia.org/wiki/Programmable_logic_controller
[ref_relativity]: https://www.relativity.com/data-solutions/ediscovery/
[ref_scada]: https://en.wikipedia.org/wiki/SCADA
[ref_sel4]: https://sel4.systems/
[ref_servo]: https://servo.org/
[ref_sketchpad]: https://en.wikipedia.org/wiki/Sketchpad
[ref_sox]: https://en.wikipedia.org/wiki/Sarbanes%E2%80%93Oxley_Act
[ref_unix_philosophy]: https://en.wikipedia.org/wiki/Unix_philosophy
[ref_vim]: https://www.vim.org/
[ref_vscode]: https://code.visualstudio.com/
[ref_wasm_component_model]: https://component-model.bytecodealliance.org/
[ref_windows]: https://en.wikipedia.org/wiki/Microsoft_Windows
[related_post_apollo_vertical]: {% post_url 2026-05-25-human_spaceflight_ground_systems_as_illustrative_vertical %}
[related_post_btron_hypermedia]: {% post_url 2026-05-23-btron_hypermedia_and_real_time_desktop %}
[related_post_keleusma_substrate]: {% post_url 2026-05-24-keleusma_as_substrate_for_real_time_hypermedia_desktop %}
