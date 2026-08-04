---
layout: post
mathjax: false
comments: true
title: "BTRON, Hypermedia, and the Real-Time Desktop"
date: 2026-05-23 09:00:00 +0000
categories: operating-systems history philosophy
series: hypermedia_desktop
series_title: Hypermedia Desktop
series_index: 2
---
<!-- A113 -->
<script>console.log("A113");</script>

In 1984
Ken Sakamura proposed
a family of operating systems
that took two ideas seriously
at the same time.
The first idea was
that an interactive computer
deserves the same real-time discipline
as a flight control computer
or a factory controller.
The second idea was
that the user-visible primitive
on such a system
should not be the file
and the application,
but the typed document part
and the typed link.
The first idea matured into [ITRON][ref_itron],
which the [IEEE Milestone citation][research_ieee_milestone_tron]
of 2023 records as a cumulative deployment
in the billions of embedded devices,
presently invisible
in automobiles, appliances, and industrial controllers
worldwide.
The second idea matured into [BTRON][ref_btron],
shipped in a small number of products
in Japan,
and is presently
a footnote.

This is the asymmetry
this article is interested in.
The real-time half of the TRON Project
succeeded so completely
that it is now infrastructure.
The hypermedia desktop half
failed so completely
that no direct competitor exists
forty years later.
The asymmetry is not explained
by the engineering difficulty alone.
The combined demand
for real-time guarantees,
hypermedia composition,
and provenance-bearing documents
exists in well-funded form
in defense, aerospace,
intelligence, regulated medicine,
nuclear and chemical process operation,
and supervisory work
inside central banks and standards bodies.
None of these constituencies
has been served by a general-purpose product.
Several of them
have built private substitutes
that approximate parts of the design
at very high cost.

This article surveys the BTRON proposition,
why it failed,
and what other systems have occupied
the real-time and hypermedia niches
since.
It then examines
where the hypermedia model wins on merit,
where it is clearly the wrong fit,
who would be served by a real-time hypermedia desktop,
who is correctly served
by the mass-market application and file model,
whether a web browser
can substitute for an operating system in this role,
and what a successful entry strategy
would need to look like.
The treatment is analytical rather than prescriptive.
The objective is to leave the reader
with enough structural understanding
to recognize the design space
when it appears in a working environment,
not to argue for a product.

## The BTRON Proposition

BTRON, short for Business TRON,
was the desktop subproject
of the [TRON Project][ref_tron_project],
which Ken Sakamura founded
at the University of Tokyo in 1984.
The umbrella project also included
[ITRON][ref_itron] for embedded real-time control,
CTRON for telecommunications,
and MTRON for cross-system coordination.
The architecture was intended
as a coherent family
in which the same principles
applied at every scale,
from a microcontroller
running a single sensor loop
to a personal workstation
composing structured documents
to a network of cooperating computers
across an organization.

BTRON inherited from ITRON
the assumption that the operating system
underneath the user interface
is a hard real-time microkernel.
Window updates, input handling,
file system access,
and process scheduling
were intended to operate
with bounded latency
rather than best effort.
This was not a marketing position.
It was a design discipline.
The graphical interface
was treated as a deadline-sensitive subsystem
rather than as a layer
that could be slowed
by garbage collection
or virtual memory thrashing.

On top of this real-time substrate
sat the part of BTRON
that distinguished it
from contemporary desktops.
BTRON proposed
that the file and the application
are implementation details
that should not be exposed to the user.
The user-visible primitive
should be the typed document part.
A part has a stable identity,
a declared type, and a content body.
Parts can contain other parts.
The same mechanism
that embeds a figure in a report
also embeds a report in a workspace
and a workspace in a project.
There is no special case
for a top-level file.

Parts are connected
by typed links.
A link has a source,
a target, a type,
and metadata such as direction
and visibility.
The operating system
manages a link store
as a first-class service,
the same way a conventional system
manages a file system.
Links survive renames,
edits, and reorganizations,
because the link store
holds the canonical relationship
rather than relying
on a fragile string match.

Applications,
in this model,
are not owners of files.
They are handlers
for part types.
When a user opens a document
containing prose, a table, and a figure,
the system instantiates
the prose handler, the table handler,
and the figure handler in place.
Each handler edits
its own part type
inside the same document surface.
The user does not switch
between applications.
The user moves the cursor.

This composition principle
extended uniformly through BTRON.
The desktop itself
was a hypermedia surface
populated by links
into the object graph,
not by files in folders.
A Real Object held the canonical data.
A Virtual Object,
sometimes called a Pseudo Object
in the TRON Project literature,
held a reference into the Real Object graph
and allowed a single canonical part
to appear in many places
without being copied.
Edits to the canonical part
propagated to every appearance.

The realization of this proposition
in shipping products
was less ambitious
than the proposition itself,
but the products did exist.
Matsushita shipped the PanaCAL ET around 1989,
the first commercial BTRON product.
Personal Media Corporation
later developed the 1B, B-right, and V series,
culminating in [Cho Kanji][ref_cho_kanji],
which ran on commodity personal computer hardware
and is still nominally available.
The Cho Kanji line is interesting
not only as a desktop
but also as a deliberate exercise
in writing-system completeness.
It supports approximately 180,000
Chinese, Japanese, and Korean characters
through the [TRON character code][ref_tron_encoding]
and the associated GT Shotai font work,
a coverage figure that Unicode
required more than a decade to approach.
Unicode 1.0 in 1991 contained
20,902 unified CJK ideographs,
and Unicode reached comparable coverage
only with version 4.1 in 2005
and subsequent expansions.
BTRON-based Cho Kanji shipped in 1999
with its multi-plane character architecture
already in place.

The TRON Project's intellectual ambition,
in summary,
was to unify
the operating system,
the document model,
and the writing system
under a single coherent specification
with real-time guarantees
underneath all of it.
This is not a small program.
The fact that any part of it shipped
is a measure of how serious
the engineering investment was.

## Why BTRON Failed

The reasons are several,
and they reinforce one another.
Stating them precisely
matters for anyone contemplating
a successor.

The first reason was political.
In April 1989 the Office of the United States Trade Representative
listed the TRON Project
under Section [Super 301][ref_super_301]
as an unfair trade barrier,
on the grounds that
the Japanese Ministry of Education's plan
to deploy TRON-based personal computers
in schools
would foreclose foreign vendors
from a captive market.
The listing was withdrawn the following month
after a USTR inspection team
visited the TRON Association,
as documented in
the [USTR statement of 25 May 1989][research_ustr_1989].
By that point the practical damage was done.
The Ministry had already
conditioned support
on BTRON being made compatible with DOS
at the end of 1988,
and the school deployment was abandoned
under combined pressure
from the trade dispute
and domestic industry hesitancy.
The decision removed
the institutional anchor
that BTRON needed
to seed a software ecosystem.
Without the school program,
no general-purpose application market
could form around the platform.

The second reason was hardware.
The TRON architecture
included a specification
for a family of microprocessors
optimized for TRON operating systems.
The Gmicro series of chips
implemented this specification
and were used in some embedded TRON deployments,
but the chip line
never reached mass production
at the scale of contemporary microprocessors
from Intel, Motorola, or the various
reduced instruction set computing vendors.
BTRON survived this failure
by running on commodity personal computer hardware,
but the prestige association
between the operating system
and a national chip program
worked against the platform
once the chip program faltered.

The third reason was ecosystem.
The hypermedia model
that BTRON proposed
required a population of handlers
written by many vendors
who agreed on part types
and on the protocol
by which handlers composed.
Such agreement is expensive
and slow,
and no vendor population
of the necessary size and diversity
ever assembled around BTRON.
The platform was small,
Japan-centric,
and Japanese-language first.
Foreign vendors
had no business reason
to invest in handlers for BTRON,
and the domestic vendor pool
was insufficient
to populate the model fully.

The fourth reason was conceptual.
The hypermedia model
required users to learn
a richer mental model
than the file-and-application model
they already knew.
Users in the late 1980s
and early 1990s
were learning the file-and-application model
for the first time
and were not in the mood
for a second mental model
with greater conceptual depth.
The competing systems,
namely [Microsoft Windows][ref_windows],
[Macintosh System Software][ref_mac_os],
and the various Unix workstations,
offered familiar abstractions
and very large application catalogs.
BTRON offered a better model
that demanded relearning,
and the market chose familiarity.

The fifth reason was that
the global personal computer industry
was being structured
by a small number of vendors
who controlled
both hardware platforms
and software distribution.
A standards-led alternative
from outside that vendor pool,
even a technically excellent one,
faced obstacles
that had little to do
with its design merits.
The history of [OS/2][ref_os_2],
the [Plan 9][ref_plan_9] operating system,
[NeXTSTEP][ref_nextstep] before its absorption into Apple,
and the [BeOS][ref_beos] desktop
illustrates the same pattern.
Technically distinctive operating systems
that did not capture
the personal computer mass market
were consigned to niche status
regardless of merit.

The combined effect of these reasons
was that BTRON
became a permanent niche product
in Japan,
beloved by a small population
of writing-system enthusiasts
and a few research and government users,
and ignored everywhere else.
The TRON Project's other limb,
the embedded ITRON family,
followed a completely different trajectory.
ITRON and its successor T-Kernel
became the dominant real-time operating system
in Japanese consumer electronics,
spread to global vehicle electronics,
and are presently estimated
to ship in
several billion devices per year.
The same project
that failed as a desktop
succeeded as infrastructure.
This asymmetry
is the central historical fact
about the TRON Project,
and it deserves to be carried forward
into any successor design.

## A Brief History of Real-Time Operating Systems

To assess whether a real-time desktop
remains a defensible idea,
it helps to know
where real-time operating systems
have actually been deployed
in the four decades
since BTRON appeared.

The earliest commercial real-time operating systems
emerged across the 1980s
to control industrial processes,
military weapons systems,
and laboratory instruments.
[VRTX][ref_vrtx], released by Hunter and Ready in 1981
and widely cited
as the first commercial real-time operating system,
[pSOS][ref_psos], released by Software Components Group
in approximately 1982,
and [VxWorks][ref_vxworks], released by Wind River Systems in 1987,
were among the first
to package the discipline
into a reusable kernel.
VxWorks
became the dominant
hard real-time operating system
in aerospace and industrial control
and presently runs the avionics
of many commercial aircraft,
the control systems of
the Mars Pathfinder, Mars rovers,
and several deep-space probes,
and the network infrastructure
of major telecommunications equipment.
The well-known [Mars Pathfinder priority inversion incident][research_mars_pathfinder]
of 1997
was documented under VxWorks
in a Jet Propulsion Laboratory technical note
that remains a standard reference
on real-time scheduling pathologies.

[QNX][ref_qnx] originated in 1980
as a microkernel operating system
developed in the Ottawa area of Canada
by Quantum Software Systems,
founded by University of Waterloo students
Gordon Bell and Dan Dodge.
The architecture decoupled
the kernel from the device drivers,
file systems, and graphics subsystems,
each of which ran
as a user-space process
communicating through message passing.
QNX subsequently became the foundation
for [BlackBerry QNX Neutrino][ref_qnx_neutrino],
which is presently
the dominant real-time operating system
in automotive infotainment
and digital cockpit applications,
with more than 275 million vehicle deployments
as of late 2025
per the [BlackBerry QNX press release][research_qnx_275m].
QNX historically supported
a complete desktop environment
called [QNX Photon][ref_qnx_photon],
including a windowing system,
text editor, web browser,
and file manager,
all running on the hard real-time kernel.
A 1999 demonstration distributed QNX,
Photon, and a Voyager web browser
on a single 1.44 megabyte floppy disk.
The QNX Photon desktop
is presently retired as a product
and has been unsupported since 2014,
with Qt recommended as the successor
for graphical applications on QNX.
Photon remains the closest thing
to a successful real-time desktop
in the historical record
outside the TRON family.

[Green Hills Software's INTEGRITY][ref_integrity]
is a separation-kernel real-time operating system
certified to the highest assurance levels
required by aerospace and defense.
It is used in fighter aircraft,
commercial cockpit displays,
and high-assurance military communication systems.
INTEGRITY's design isolates partitions
both in space and in time,
which makes it suitable
for hosting safety-critical
and security-critical workloads
on the same hardware.

[FreeRTOS][ref_freertos]
emerged as an open-source kernel
for microcontroller-class hardware
and is among the most widely deployed
real-time kernels in absolute numbers,
because a large fraction of
internet-of-things products
that require a kernel
choose FreeRTOS.
Stewardship transferred from Real Time Engineers Ltd
to Amazon Web Services in November 2017,
as announced in the
[Amazon FreeRTOS launch blog post][research_amazon_freertos].
The MIT License was preserved
and the original maintainer Richard Barry
joined Amazon Web Services.

[Zephyr][ref_zephyr],
hosted by the Linux Foundation,
is a younger open-source real-time operating system
targeting the same microcontroller niche
with a more modern build system
and a permissive license.
It has been adopted
by several vendors in industrial,
medical, and consumer device categories.

[RTEMS][ref_rtems]
is a long-running open-source real-time kernel
maintained primarily
by aerospace and defense contractors
and used in numerous space missions,
including instruments
on Mars probes
and small satellites.

[NuttX][ref_nuttx]
is an open-source real-time kernel
that emphasizes POSIX compatibility
and is used in drone autopilots,
notably the PX4 flight stack,
and in several wearable devices.

The Toyota-originated and broader Japanese-industry projects
that descend from ITRON,
notably [μITRON][ref_uitron] and [T-Kernel][ref_t_kernel],
remain widely deployed in vehicle subsystems,
industrial robotics,
and consumer electronics
under both proprietary
and open-source licenses
managed by the [TRON Forum][ref_tron_forum].

Several research and adjacent systems
deserve mention.
[seL4][ref_sel4] is a formally verified microkernel
whose correctness proof
relative to its specification,
[published by Klein and colleagues at SOSP 2009][research_sel4_sosp],
remains the most extensive functional-correctness proof
of a general-purpose operating system kernel to date.
It is used in defense applications
and in several research desktop frameworks.
[Genode][ref_genode]
is a component-based operating system framework
that runs on top of seL4,
NOVA, Fiasco.OC, and similar microkernels,
and ships a desktop distribution
called Sculpt OS
intended for security-conscious end users.
The Genode framework's real-time properties
are inherited from its base kernel
and from the user's configuration choices.

[Redox OS][ref_redox]
is an open-source microkernel operating system
written in Rust,
with a working Orbital desktop environment
and a memory-safe systems language at every layer.
The project remains in alpha
and is not production-ready
as of 2026.
It is not advertised
as a real-time operating system,
but its microkernel architecture
is amenable to real-time discipline
and the project has produced
significantly more progress
toward a usable Rust-native desktop
than was widely expected.

The general pattern that emerges
from forty years of real-time operating systems
is that the technology
has matured very thoroughly
in domains where the operator
is a machine,
namely aerospace, automotive,
industrial control,
and embedded devices.
The technology has matured
much less thoroughly
in domains where the operator
is a human at a desk.
QNX Photon was the most serious attempt
to bridge this gap
in the era after BTRON,
and it did not become
a sustained product.
The category presently exists
mostly in two forms,
namely the operator-facing
heads-up displays
in aircraft and vehicles,
and the operator workstations
in industrial control rooms,
both of which are integrated
by specialist vendors
rather than purchased
as general-purpose desktops.

## A Brief History of Hypermedia Systems

The hypermedia model
that BTRON instantiated
has a much longer intellectual history
than the operating system
that bore it.
The history is worth recounting
because the recurring failures
illuminate the structural difficulty
of the model
as much as its conceptual elegance.

[Vannevar Bush's][book_as_we_may_think]
1945 Atlantic Monthly essay
"As We May Think"
described the Memex,
a hypothetical desktop device
that stored microfilmed books
and allowed the user
to create associative trails
linking documents and annotations.
The Memex was never built,
but the essay
introduced the idea
that the relationships among documents
are first-class objects
deserving infrastructure support.

[Ivan Sutherland's Sketchpad][ref_sketchpad],
completed at the Massachusetts Institute of Technology
Lincoln Laboratory in 1963
and documented in
[Sutherland's doctoral thesis][research_sketchpad],
introduced direct manipulation
of typed graphical objects
through a light pen on the TX-2 computer.
Sketchpad's master and instance subpictures
prefigured object-oriented programming.
Its constraint-satisfaction engine
prefigured contemporary
parametric computer-aided design.
The reason to mention Sketchpad here
is that direct manipulation of typed parts
is the user-interface idiom
that hypermedia composition requires.
Sketchpad is the earliest demonstration
that the idiom is viable.

[Doug Engelbart][ref_nls]
demonstrated NLS,
short for oN-Line System,
in San Francisco on 9 December 1968
at the Fall Joint Computer Conference,
in a presentation
that is now remembered
as the Mother of All Demos.
NLS implemented hypertext
with internal and external links,
collaborative editing
across a network,
mouse-driven graphical interaction,
and structured documents
with addressable parts,
as documented in
[Engelbart and English's contemporaneous AFIPS paper][research_engelbart_1968].
Most of the features
of modern personal computing
existed simultaneously
on a single research system
five years
before the personal computer industry
had begun.
NLS was developed at the Stanford Research Institute
through funding from
the Advanced Research Projects Agency,
the National Aeronautics and Space Administration,
and the United States Air Force,
and was the most complete
working hypermedia system
of the 1960s.

[Alan Kay's Dynabook][ref_dynabook] vision,
originated in 1968 at the University of Utah
and developed at Xerox PARC from 1970 onward,
articulated the personal computer
as a portable, networked device
on which the user authors
rich interactive media
as fluently as the user reads it.
[Kay and Goldberg's 1977 paper
"Personal Dynamic Media"][research_personal_dynamic_media]
in IEEE Computer
remains the canonical statement
of the vision.
The Xerox Alto was initially called
the interim Dynabook,
and the Dynabook concept
directly motivated
the Smalltalk environment
discussed below.
The Dynabook vision matters here
because it framed the personal computer
as an authoring instrument
rather than as a consumption device.
The hypermedia thesis
inherits the authoring premise.

[Ted Nelson's][book_literary_machines]
Project Xanadu
began in 1960
and has continued in various forms
to the present.
Nelson coined the terms hypertext and hypermedia
and proposed a design
in which documents
were never copied
but always referenced,
with transclusion
as the fundamental composition operation
and micropayments
as the economic substrate
for content reuse.
Xanadu has produced
several partial implementations,
most recently
the OpenXanadu prototype in 2014,
but has never shipped
as a complete system.
Nelson's writings,
particularly "Literary Machines"
and "Computer Lib / Dream Machines",
remain
the most thorough articulation
of the maximal hypermedia thesis
in print.

The Xerox Palo Alto Research Center
produced several systems
in the 1970s and 1980s
that incorporated hypermedia ideas
to varying degrees.
[Smalltalk][ref_smalltalk]
implemented a uniform object model
with first-class messages
and was an experimental personal computing environment
that anticipated
much of the structure
of later desktop operating systems.
[NoteCards][ref_notecards],
developed at Xerox PARC starting in 1984
by Randall Trigg, Frank Halasz, and Thomas Moran,
was an explicit hypermedia authoring system
modeled on index cards
connected by typed links.
Halasz's 1988 retrospective
"[Reflections on NoteCards][research_halasz_1988]"
in Communications of the ACM
identified seven open problems
that subsequent hypermedia systems
have continued to grapple with.
The Cedar environment
provided a typed file system
with rich object semantics
that influenced subsequent
research operating systems.

[Apple's HyperCard][ref_hypercard],
released in August 1987
and bundled free with new Macintosh computers,
was the most commercially successful
hypermedia authoring system
of its era.
HyperCard organized content
into stacks of cards
connected by buttons
that invoked scripts
in the HyperTalk language.
HyperCard reached millions of users
through Macintosh bundling,
seeded a generation of authors
with hypermedia intuitions,
and was discontinued by Apple in March 2004
without a successor.

[Microsoft's Object Linking and Embedding][ref_ole],
which became OLE 2
through the 1992 to 1993 release window
and shipped in production form
with Word 6.0 and Excel 5.0,
allowed Word documents
to contain editable spreadsheets,
spreadsheets to contain editable drawings,
and so on across the Microsoft Office product line.
OLE was a partial realization
of the hypermedia thesis
within a single vendor's product family.
The underlying [Component Object Model][ref_com]
generalized the protocol
beyond the document use case
and became the substrate
for ActiveX, DCOM, and DirectX.
Microsoft's broader [Cairo project][ref_cairo],
intended to produce
an object-oriented file system
and a fully compound-document desktop,
was canceled
without shipping
as a complete product
during the 1990s.

[OpenDoc][ref_opendoc],
developed jointly by
Apple, IBM, WordPerfect, Novell, SunSoft, and other vendors
under the Component Integration Laboratories consortium
established in 1993,
attempted a cross-vendor compound document architecture
in the mid-1990s.
The OpenDoc framework
shipped on System 7.5 in 1994.
The first OpenDoc product,
Apple's CyberDog Internet client,
shipped in May 1996.
OpenDoc was discontinued
in March 1997
following Steve Jobs's return
to Apple,
without ever achieving
meaningful application adoption.

[David Gelernter and Eric Freeman's
Lifestreams][ref_lifestreams],
developed at Yale University
in the mid-1990s
and presented at
[the Computer-Human Interaction conference
in 1996][research_lifestreams_chi96],
proposed an alternative to the desktop metaphor
in which every document is a typed event
on a single time-ordered stream
that extends from the user's past
into the user's future.
The system supported retrospective queries
that searched backward through the stream
and prospective queries
that fired alerts on future events
such as reminders and calendar items.
The model is documented further in
[Freeman and Gelernter's 1996
Special Interest Group on Management of Data
record paper][research_lifestreams_sigmod]
and in
[Gelernter's 1991 book Mirror Worlds][book_mirror_worlds]
from Oxford University Press.
Mirror Worlds Technologies,
later Scopeware,
commercialized the design
until it ceased operations in 2004.
Lifestreams is the canonical precedent
for the contemporary stream-based
information architectures
that drive social media feeds,
activity streams,
and timeline-based knowledge tools.
For a real-time hypermedia operating system,
Lifestreams contributes
the temporal dimension
that the article's earlier discussion
of typed parts and typed links
left implicit.
A part has not only a type and a link graph
but also a time of origin
and a time of last modification,
and the platform's query language
must address all three dimensions.

[GNOME Bonobo][ref_bonobo]
and [KDE KParts][ref_kparts]
were the GNOME and KDE projects' attempts
at compound-document component frameworks
in the early 2000s.
Bonobo was deprecated by GNOME
in the late 2000s.
KParts continues to exist in KDE
but is used primarily
within a small number of applications
rather than as a general composition framework.

[Lotus Notes][ref_lotus_notes],
released in December 1989
and presently maintained as HCL Notes
following the 2018 transfer from IBM,
was the most commercially successful
hypermedia-adjacent platform
in enterprise software.
Notes combined a structured document database,
typed forms,
typed links between documents,
replication across nodes,
and a programming model
suitable for line-of-business applications.
Notes reached
on the order of 42 million active seats
by 1998
and approximately 140 million cumulative licenses
through 2008,
and is presently
in slow decline,
displaced by web-based collaboration tools
rather than
by a successor compound-document platform.

[Microsoft SharePoint][ref_sharepoint]
inherited some of the Notes thesis
and dominated the enterprise collaboration market
during the 2000s and 2010s,
with structural awareness of documents,
typed metadata, lists, web parts,
and content management workflows.
SharePoint is more conservative than Notes
in its hypermedia aspirations.
It treats files and lists
as the primary primitives,
with typed links secondary
rather than woven through.

[Tim Berners-Lee's World Wide Web][ref_www],
proposed at CERN in March 1989
through the document
"[Information Management, A Proposal][research_berners_lee_1989]"
and implemented in 1990,
absorbed the public mindshare
that compound document architectures
had been competing for
inside the operating system.
The Web was a weaker hypermedia design
than NLS, Xanadu, BTRON, or OpenDoc,
in that links were unidirectional and untyped,
parts were not first-class,
and transclusion was absent.
But the Web was free,
universal, and easy to author,
and it absorbed the use cases
that compound document architectures
had failed to claim.
The browser became
the substrate on which
the next generation
of hypermedia ideas
would be tried.

The contemporary descendants of the hypermedia tradition
fall into several clusters.
[Roam Research][ref_roam],
[Logseq][ref_logseq],
and [Obsidian][ref_obsidian]
are personal knowledge tools
that support block-level addressing
and bidirectional links.
Obsidian and Logseq are local-first.
[Notion][ref_notion] and [Coda][ref_coda]
are cloud-based structured document tools
with typed blocks
and embedded databases.
[Jupyter][ref_jupyter]
and [Observable][ref_observable]
are computational notebook environments
that blend prose, code, and live output
within a single document.
[Solid][ref_solid],
a project from Tim Berners-Lee's group at MIT,
is an architecture for personal data pods
with typed linked data
that attempts to restore
some of the hypermedia properties
that the Web's evolution discarded.
[Beaker Browser][ref_beaker]
was an experimental hypermedia browser
built on peer-to-peer protocols,
discontinued after its last stable release
in December 2020,
but with influential design notes.
[Ink and Switch's local-first research][research_local_first],
articulated in
[Kleppmann and colleagues' Onward 2019 essay][research_kleppmann_local_first],
has produced libraries such as [Automerge][ref_automerge]
that make local-first hypermedia
technically tractable.
[Yjs][ref_yjs]
is a comparable library
based on different theoretical foundations.

These contemporary tools
draw cultural energy
from a loose research and practice community
known as the Tools for Thought movement.
The term originates with
[Howard Rheingold's 1985 book of the same title][book_tools_for_thought],
which surveyed the early history
of mind-expanding technology
from Bush, Engelbart, and Kay.
The contemporary movement
takes its defining statement from
[Andy Matuschak and Michael Nielsen's 2019 essay
"How can we develop transformative tools for thought?"][research_matuschak_nielsen_ttft],
which argued that the genre is presently underbuilt
and proposed mnemonic medium
as one direction of investment.
[Matuschak's personal site][ref_andy_matuschak]
and [his Evergreen Notes practice][ref_evergreen_notes]
have influenced the design
of Roam, Logseq, and Obsidian.
[Maggie Appleton's writings][ref_maggie_appleton],
particularly
[her brief history of the Digital Garden][ref_appleton_garden_history],
provide the cultural-studies framing
that names the movement.
[Bret Victor's manifesto Magic Ink][ref_magic_ink]
on the worrydream.com archive
is the most-cited foundational essay
in this lineage,
arguing that information software design
is graphic design
rather than engineering.
The community organizes through
the [Future of Coding podcast and forum][ref_future_of_coding]
and through small online communities
such as [Hyperlink Academy][ref_hyperlink_academy].
The Tools for Thought movement
matters for the BTRON successor question
because it is the most active contemporary
constituency for hypermedia ideas
outside the regulated-industry market.
A successful platform
that draws on the movement's design intuitions
inherits a developer and user community
that the regulated industries do not provide.

The pattern across this history
is unmistakable.
The hypermedia model
keeps recurring
because the demand
is real.
Compound document architectures
keep being canceled or marginalized
because the engineering, ecosystem, and product economics
are punishing.
The Web absorbed
a large fraction of the use cases
by being weaker
but universal.
The unresolved question
is whether the remaining use cases,
namely those requiring
real-time guarantees,
strong provenance,
or composition outside the browser,
can sustain a successor.

## Other Radical Unifications

Hypermedia is not the only proposal
to unify the desktop, the document, and the program
under a single coherent abstraction.
Several research operating systems
have advanced rival unifications,
each addressing a piece
of the same underlying problem
that BTRON aimed at.
A successor design
that ignores these systems
forfeits useful lessons.

[Plan 9 from Bell Labs][ref_plan_9],
designed by Rob Pike, Ken Thompson,
Dave Presotto, Phil Winterbottom,
and Dennis Ritchie
from the late 1980s onward,
chose the unification
"everything is a file"
extended through two structural commitments.
The first commitment is
the [9P protocol][ref_9p_protocol],
a single message-oriented file system protocol
that exposes devices, network connections,
processes, and windows
as files served by user-space servers.
The second commitment is
the per-process namespace.
Each process composes its environment
by binding remote or local resources
into chosen mount points,
so the address space of names
is a local composition
rather than a global registry.
Plan 9 was relicensed under the MIT License in 2021,
and the official archive is now maintained by
the [Plan 9 Foundation][ref_plan_9_foundation].
The 9front fork remains under active monthly development.
The structural lesson for hypermedia
is that namespace composition
is the operating system analogue
of part composition.
Plan 9 performs composition on typed file servers,
where a hypermedia operating system
would perform the same operation
on typed document fragments.

[Inferno][ref_inferno],
created at Lucent Bell Labs in 1995
and presently maintained by
Vita Nuova Holdings,
is the distributed-systems descendant of Plan 9.
Inferno applications are written in Limbo
and compiled to bytecode for the Dis virtual machine,
which the original team designed
to provide platform independence
under the same 9P-derived Styx protocol.
Inferno was relicensed under the MIT License in 2021.
The structural lesson for hypermedia
is that uniform protocol plus portable bytecode
permits the same composition principle
to extend across heterogeneous hardware
without losing the typed-resource discipline.

[Self][ref_self],
designed by David Ungar and Randall Smith
at Xerox PARC and Stanford from 1986,
chose the unification
of direct manipulation of live typed objects.
Self pioneered prototype-based object orientation
and the adaptive just-in-time compilation techniques
that later influenced Java's HotSpot virtual machine.
The Morphic user interface framework,
introduced in Self by Smith and John Maloney
and documented in
[Maloney's foundational paper][research_morphic],
treats every graphical element
as a morph that the user may inspect,
edit, embed, and connect at run time.
Morphic is the canonical precedent
for direct manipulation of typed parts.
The user interface is not a render target
separate from objects.
It is literally the live structural graph
of objects,
manipulable through embedding, halos, and inspection.
A hypermedia composition system
that treats parts as typed editable values
occupies the same design slot as Morphic,
with persistence in a document-oriented store
in place of the live image.

[Oberon][ref_oberon],
designed by Niklaus Wirth and Jürg Gutknecht
at ETH Zurich
with initial release in 1987
and documented comprehensively in
[Project Oberon][ref_project_oberon],
chose the unification
of executable command text.
Any text fragment of the form Module.Command
may be activated by a middle click
to execute it.
This combines the convenience of a graphical interface
with the linguistic strength of a command line,
in the project's own description.
The structural lesson for hypermedia
is that document, command, and program
can be the same artifact viewed at different layers.
The hypermedia object model
extends this property
by replacing the Module.Command convention
with a typed reference to a part
that exposes named operations.
The unification claim is identical.

[JX][ref_jx]
was developed at the University of Erlangen-Nuremberg
by Michael Golm, Meik Felser, Christian Wawersich,
and Jürgen Kleinöder,
and presented at the
[2002 USENIX Annual Technical Conference][research_jx_usenix].
Both the microkernel and applications are written in Java.
Protection rests solely on
the type safety of Java bytecode
rather than on memory management unit address space separation,
which permits system calls and inter-process communication
without an address space switch.
JX is the strongest precedent
for language-level rather than hardware-level isolation
of handler code.
In a hypermedia operating system
where third-party handlers manipulate typed parts
inside the same document process,
the latency of crossing hardware protection domains
dominates the manipulation cost.
JX demonstrates that verified bytecode
plus capability-style component domains
can substitute for memory management unit isolation.
The hypermedia analogue
is sandboxed handlers implemented through
verified WebAssembly modules
or a similarly typed intermediate language,
where the part registry plays the role
of the JX domain boundary
and the type system enforces noninterference.

Taken together,
these five systems
illustrate that the BTRON proposition
is not the only credible unification of the desktop.
Plan 9 unified through namespace composition.
Self unified through live object manipulation.
Oberon unified through executable text.
JX unified through type-safe isolation.
Each chose one axis of the problem
and pushed it to its conclusion.
BTRON chose the hypermedia axis.
A modern successor
can draw on
the namespace discipline of Plan 9,
the direct manipulation surface of Self,
the executable-text idea of Oberon,
and the bytecode-isolation model of JX,
without abandoning
the typed-part-and-typed-link core
that distinguishes hypermedia
from these other unifications.

## The Hypermedia Object Model in Detail

The reason hypermedia is not just
"better files"
deserves to be stated precisely.
The model rests on six structural commitments
that the file and application model
does not make.

The first commitment is
that the document is a tree of typed parts.
A part is a unit of content
with a declared type
and a stable identity.
A part may contain other parts.
A document is not a blob
but a structure.
The user-facing implication is
that a report containing prose, tables,
and figures is not three files stitched together
but one document with three kinds of parts.

The second commitment is
that parts are addressable.
Every part has a stable identifier
that survives renames and moves.
The user-facing implication is
that one can refer
to a paragraph
of a document
without quoting it,
without copying it,
and without depending
on the document's current position
in the file system.

The third commitment is
that links are first-class objects.
A link has a source, a target,
a type, a direction, and metadata.
The operating system
stores links in a link store
the way it stores files in a file system.
The user-facing implication is
that the relationships among documents
are queryable, traversable,
and durable.

The fourth commitment is
that applications register
as handlers for part types,
not as owners of files.
When a document is opened,
the system instantiates
the handler for each part type
inside the document surface.
The user-facing implication is
that a spreadsheet table
embedded in a report
is edited by the spreadsheet handler
inside the report,
not in a separate application window.

The fifth commitment is
that composition is uniform and recursive.
The mechanism that embeds a figure in a report
is the same mechanism
that embeds a report in a workspace
and a workspace in a project.
There is no special case
for top-level files.
The user-facing implication is
that the desktop, the document,
and the workspace
are points on a single spectrum,
not different kinds of things.

The sixth commitment is
that provenance is intrinsic.
Because parts have identities
and links are typed,
the system can record
where each part came from,
when it changed,
and what it depends on.
The user-facing implication is
that questions such as
which results depend on which inputs,
which paragraphs cite which sources,
and what changed between two revisions
have system-level answers
rather than ad hoc ones.

These six commitments
are mutually reinforcing.
A system that adopts only some of them
collapses into one of the partial implementations
that the historical record contains.
A system that adopts all of them
inherits both the conceptual power
and the engineering and ecosystem burden
that have repeatedly sunk
prior attempts.

## Where the Hypermedia Model Wins on Merit

The model is genuinely better than
the file and application model
in a definable class of work.

It is better
when the artifact is a composition
of parts from many sources.
Research papers, regulatory submissions,
clinical case records, legal briefs,
engineering requirements documents,
and audited financial reports
are intrinsically multi-source.
The file model
either forces these into a single application's native format
or scatters them across many files
held together by convention.
The hypermedia model
holds the composition explicitly.

It is better
when the artifact must remain interpretable
across years or decades.
Long-lived artifacts
accumulate revisions, contributors,
and supporting evidence.
The file model
loses these relationships
through filename collisions, directory restructuring,
and application migrations.
The hypermedia model
preserves them
as typed links in the link store.

It is better
when downstream decisions
depend on provenance.
A clinical trial submission
that cannot trace each assertion
to a source dataset
fails regulatory review.
An engineering safety case
that cannot trace each requirement
to its test evidence
fails certification.
A financial audit
that cannot trace each figure
to its underlying transaction
fails the audit.
The hypermedia model
provides provenance as a system service.
The file model
provides it as a labor-intensive convention.

It is better
when the artifact must be transformed structurally.
A typed document
can be rendered to print,
to screen, to a screen reader,
to braille,
and to machine-readable downstream consumers
from a single source.
A flat document
requires bespoke conversion
for each rendering.

It is better
when many contributors edit different parts concurrently.
A typed document
allows fine-grained editing
without locking the whole file.
The unit of contention shrinks
from the file to the part.

It is better
when content is partially live.
A part can be a running computation
rather than an inert byte string.
A scientific notebook
that includes a live simulation,
an engineering document
that includes a live model query,
or an operations playbook
that includes a live system status
becomes structurally feasible
in a way that the file model does not allow.

## Where the Hypermedia Model Is Clearly the Wrong Fit

The model is poorly suited
to large categories of real work.
Stating these honestly
is more useful
than overselling the model.

It is wrong for bulk binary data.
A photo library,
a video archive,
a scientific dataset,
or a game asset bundle
is best treated
as an opaque blob
with external metadata.
Structuring the bytes
as typed parts
adds cost without benefit.

It is wrong for streaming and ephemeral content.
Chat messages, telemetry feeds,
and log streams
are sequences, not documents.
A log or queue model
fits them better
than a hypermedia model.

It is wrong for performance-critical interactive software.
Games, video editors,
digital audio workstations,
and computer-aided design tools
need direct control
over data layout and rendering.
A general handler-composition framework
imposes overhead and indirection
that these tools cannot absorb.

It is wrong for privacy-sensitive single-purpose tools.
Password managers,
authentication agents,
and secure messengers
benefit from minimal surface area
and minimal composability,
not from rich integration
with arbitrary handlers.

It is wrong for throwaway content.
A scratch note,
a quick calculation,
a one-off image,
or a temporary draft
does not benefit
from typed links and provenance.
The model's overhead
is wasted on content
that will be discarded
within an hour.

It is wrong under adversarial composition
unless the platform pays
the cost of formal isolation.
Every additional handler in a document
is a potential confused deputy.
A platform that composes content
from many sources
without strong information-flow control
is structurally vulnerable
to cross-handler exfiltration
and supply-chain compromise.
The browser's origin model
is a hard-won response
to exactly this failure mode,
and any hypermedia platform
must offer equivalent guarantees
or accept that it is unsuitable
for adversarial environments.

## Real-Time Plus Hypermedia, the Special Case

The combination
of a real-time substrate
and a hypermedia desktop
is BTRON's defining commitment.
The combination belongs squarely
in the [mission-critical engineering][related_post_fast_moving_mission_critical] mode
in which correctness, traceability, and bounded behavior
are valued above iteration speed.
It is justified
only when both problems
are present in the same artifact.
A hypermedia system
without real-time guarantees
is a knowledge management tool.
A real-time system
without hypermedia composition
is an embedded controller.
The intersection
is narrower than either set.

The intersection is occupied
by operator-facing systems
where bounded latency, structural composition,
and provenance
matter simultaneously.
Mission control consoles
compose telemetry feeds,
flight plans,
historical analyses,
and operator annotations
into a single surface
with deadline constraints
on the most critical displays.
Air traffic management workstations
compose flight tracks,
weather, airspace structure,
and controller instructions
with strict timing
on conflict alert paths.
Cockpit electronic flight bags
and avionics maintenance consoles
compose charts, manuals,
telemetry, and procedures
with guarantees
on the surfaces
that pilots interact with
during phases of high workload.
Medical imaging
and surgical robotics consoles
compose live imagery,
prior studies,
treatment plans,
and intra-operative annotations
with bounded latency.
Industrial control rooms
for power generation,
refining, and process industries
compose trends, alarms,
schematics, and procedures
with hard timing on alarm paths.
Defense and intelligence workstations
handle multi-source, multi-classification material
with provenance requirements
and operator latency budgets.

In each of these settings,
the present-day solution
is a custom-integrated stack
in which a vendor or system integrator
assembles a real-time operating system,
a graphics toolkit,
and a vertical application
to approximate
the operator's requirements.
The integration is expensive,
fragile,
and rarely transfers
between programs.
A hypermedia real-time desktop
would replace this custom integration
with a platform
on which the operator-facing surface
is a composition of typed parts
with provenance,
running on a real-time substrate
with bounded latency
on the surfaces that need it.

The adversarial pressure
on these settings
sharpens the case
rather than weakening it.
An adversary attacks
the integrity of the composition
and the boundary
between trusted and untrusted material.
A platform that pays
the engineering cost
of typed parts, typed links,
and per-part isolation
buys exactly the properties
that the adversary attacks.
The discipline required to operate such a platform
maps closely
to the [mission command][related_post_mission_command] tradition,
in which authority to act
is delegated to the trained operator at the edge
under explicit intent
rather than centralized
through every step of a workflow.
Whether this is achievable
in a generic platform
is an open engineering question.
The component frameworks
that have shipped to date,
including OpenDoc and Bonobo,
have not solved it adequately.
A serious attempt
would need to draw on
the seL4 verification work,
the QNX message-passing model,
the Genode capability architecture,
and the information-flow control literature
that has matured
in academic security research.

## Performance and Latency Engineering for Composed Documents

Real-time discipline
and hypermedia composition
pull in opposite directions.
Bounded latency is easier
when the workload is predictable.
Arbitrary composition of handlers
from many vendors
is the opposite of predictable.
A platform that takes both seriously
must adopt
a small number of structural commitments
that have no analogue
in mass-market desktop architectures.

The first commitment is
bounded handler execution time.
Each handler that participates
in a deadline-sensitive surface
must declare its worst-case execution time
for each operation it performs,
and the platform must enforce that bound.
The mechanism is well understood
in safety-critical software.
What is novel is applying it
at the part-handler boundary
inside a user-facing document.

The second commitment is
deadline propagation across handler boundaries.
When the operating system
schedules the rendering of a document,
the deadline must propagate
to every handler that participates
in that document's current frame.
This is conceptually similar
to the priority inheritance
that the Mars Pathfinder VxWorks incident
made famous as a failure mode
when omitted.
The same logic applies
to a typed part
whose handler must complete
within the document's deadline budget.

The third commitment is
preallocated resources for safety-critical surfaces.
Memory, file descriptors,
display surfaces, and link-store handles
must be allocated when the surface is opened
and held for the surface's lifetime.
Dynamic allocation
inside the inner loop of a safety-critical display
is the canonical source of unbounded latency
and must be excluded by design.
This constraint
restricts the set of handlers
that may appear on such a surface
to those that have been audited
for static resource use.

The fourth commitment is
spatial and temporal isolation of misbehaving parts.
A handler that exceeds its budget
must not be allowed
to starve other handlers
on the same surface
or to compromise their state.
This is the contribution of separation kernels
such as [Green Hills INTEGRITY][ref_integrity]
and microkernels such as [seL4][ref_sel4],
extended down to the part-handler level.
The [Genode Operating System Framework][ref_genode]
provides a contemporary user-space realization
of this principle
through capability-typed components,
and the [WebAssembly Component Model][ref_wasm_component_model]
provides a portable realization
through verified bytecode components.

The fifth commitment is
admission control at the surface boundary.
A real-time hypermedia surface
must reject the embedding of a handler
whose declared budgets
would prevent the surface
from meeting its overall deadline.
The user perceives this
as the surface refusing to render
a particular embedded part,
not as the surface degrading silently
once the deadline has been missed.
This is analogous to
the receive-only mode
that ARINC 653 partitioned systems
enter when a partition exceeds its budget.

The combined effect of these commitments
is a stratified architecture.
The most safety-critical surfaces
admit only a small set of audited handlers
operating on preallocated resources
with declared budgets.
Less critical surfaces admit
a larger set of handlers
with weaker guarantees.
Ordinary documents
admit any handler
with no guarantees beyond
the underlying browser's sandbox.
The platform exposes
the stratification to the user
through visible markings
on the surface boundary,
so that the user knows
which guarantees apply
to which part of the screen.
This is the discipline
that distinguishes a real-time hypermedia desktop
from a general-purpose desktop
that merely happens to include
a few real-time components.

## Who Is Served by the Mass-Market Application and File Model

The mass-market application and file model
is correctly chosen
for users whose work
has the inverse properties.

It is correct for users
who produce primarily transient documents.
An office worker
who writes meeting notes,
edits a spreadsheet,
and sends an email
is not authoring a multi-source compound document
with audit and provenance requirements.
The file and application model
matches the work.

It is correct for users
who consume more than they produce.
A worker who reviews reports
that someone else assembled
does not benefit
from authoring infrastructure.

It is correct for users
of throwaway scratch space.
A student doing homework,
a researcher running a quick analysis,
or a developer prototyping an idea
does not benefit
from typed links
or provenance tracking
on artifacts
that will be replaced or discarded
within a working session.

It is correct for performance-bound creative work.
A video editor,
a digital audio producer,
or a three-dimensional modeler
needs direct control
over the data model
and benefits from
specialized application architectures
rather than general composition.

It is correct for entertainment
and consumer media consumption.
A music player,
a streaming video application,
or a game
does not present documents.
It presents experiences.
The file and application model
maps to the user-visible primitive of choice,
namely the title or the session.

It is correct for the long tail
of light personal productivity.
The market settled
on the file and application model
because the model is adequate
for most users most of the time,
and the cost of teaching everyone
a richer model
exceeded the benefit.
This is not a failure of the alternatives.
It is a reasonable equilibrium
given the actual distribution
of user needs.

## Who Would Benefit from a Hypermedia Real-Time Desktop

The benefit accrues
to a comparatively small population
whose work has three properties
at the same time.

The first property is
that the artifact is a structured composition
of parts from many sources.
The second property is
that the artifact has a long lifetime
under audit pressure.
The third property is
that consequential decisions
downstream of the artifact
depend on the integrity
of its provenance chain.

If even one of these properties
is absent,
the case weakens substantially.
If all three are present,
the case is strong
and the existing tooling
is widely acknowledged
as inadequate.

User populations that meet all three include
research scientists
producing reproducible computational artifacts,
engineering analysts
producing requirements
and verification evidence
in safety-critical industries,
clinical staff
authoring case records
under retention obligations
that exceed twenty years,
clinical trial researchers
authoring regulatory submissions
under traceability requirements,
regulators and auditors
verifying the provenance
of clinical and financial submissions,
legal practitioners
working in litigation, mergers and acquisitions,
and regulatory matters,
intelligence analysts
synthesizing reports
from multiple sources
under classification and tradecraft constraints,
investigative journalists
working under similar source-protection constraints,
systems engineers
in aerospace, defense, and safety-critical industries
who maintain requirements traceability
under standards
such as [DO-178C][ref_do_178c],
[ARP4754A][ref_arp4754a] and its 2023 successor ARP4754B,
[ISO 26262][ref_iso_26262],
and [IEC 62304][ref_iec_62304],
and policy authors
inside large institutions
whose work is intrinsically transclusive.

User populations that do not benefit enough
to justify the platform cost
include
general office workers
who produce transient documents,
consumer users
who consume more than they produce,
creative professionals
in video, audio, and game production
whose tools are performance-critical
and already domain-specific,
and developers writing software,
whose source control and language-server tooling
already provides
most of the structural benefits
at lower cost.

The market gap
between the populations
that would benefit
and the products that exist
is real.
The partial substitutes that occupy the gap,
notably IBM DOORS, Siemens Polarion,
PTC Windchill, Dassault ENOVIA,
Veeva Vault,
Palantir Gotham and Foundry,
Relativity, iManage,
and a long tail
of bespoke internal systems,
are each multi-hundred-million
or multi-billion-dollar product lines
that occupy a slice of the design space
and force users
to integrate across them.
The fact that these incumbents exist
at this scale
is the strongest evidence
that the demand is present
and well-funded.

## The Artificial Intelligence Synergy

The hypermedia thesis acquires new force
in the era of large language models.
Four contemporary developments
are converging on requirements
that the file-and-application model
does not satisfy
and that the hypermedia model
satisfies by construction.

The first development is
[retrieval-augmented generation][research_rag_lewis],
introduced by Lewis and colleagues at NeurIPS 2020
and now the dominant pattern
for grounding large language model outputs
in source material.
A retrieval-augmented system
selects fragments from a corpus
and conditions the model's output
on those fragments.
The system's correctness
depends on the fragments
having stable identities,
on the relationships
between fragments
being inspectable,
and on the user
being able to trace each output
to its sources.
These are precisely
the properties
that the hypermedia model provides
and that the file-and-application model
withholds.
In a file world,
retrieval-augmented systems
recreate the link store
inside their own vector database,
which is then siloed from
every other tool the user employs.
In a hypermedia world,
the link store
is shared infrastructure.

The second development is
the [Model Context Protocol][ref_mcp],
[announced by Anthropic in November 2024][research_mcp_announcement]
as an open standard
for connecting large language models
to external data sources and tools.
Model Context Protocol
generalizes the practice
that retrieval-augmented systems
implement ad hoc.
A Model Context Protocol server
exposes typed resources and typed tools
to a language model client.
The pattern is
the operating system call interface
of the agentic era.
A hypermedia operating system
that exposes its parts
through a Model Context Protocol server
makes those parts
addressable
by any large language model client
that speaks the protocol,
without bespoke integration.

The third development is
structured output from language models.
The major model providers,
namely [OpenAI Structured Outputs][ref_openai_structured],
[Anthropic Tool Use][ref_anthropic_tool_use],
and [Google Gemini function calling][ref_gemini_function],
each constrain the model's output
to conform to a developer-provided schema.
The pattern is
a forcing function for typed parts.
A language model that emits
schema-conforming output
is producing exactly the kind of content
that a hypermedia handler can consume in place
without parsing-and-conversion errors.
The mismatch between language model output
and downstream consumer expectations,
which is presently
a significant operational burden
on agentic systems,
disappears when both ends
share a typed part vocabulary.

The fourth development is
content provenance.
The [Coalition for Content Provenance and Authenticity][ref_c2pa]
maintains a specification
for cryptographically signed manifests
that travel with media assets
through capture, edit, and publication.
[Content Credentials][ref_content_credentials]
is the consumer-facing brand for this work,
backed by Adobe, Microsoft, OpenAI,
Google, Meta, the BBC, and others.
The specification answers
the question
of where a particular image, audio file,
or generated artifact came from
and what was done to it.
This is the provenance feature
that the hypermedia model
makes intrinsic at the document level,
extended to media at the asset level.
The [National Institute of Standards and Technology
generative artificial intelligence profile][research_nist_ai_rmf]
of the AI Risk Management Framework,
published in July 2024,
recommends provenance metadata and watermarking
as standard controls
for generative artificial intelligence outputs,
and the [European Union Artificial Intelligence Act
Article 50][ref_eu_ai_act_50]
mandates machine-readable marking
of synthetic content
under Regulation 2024/1689.
Provenance for artificial intelligence content
is moving from optional best practice
to regulatory requirement.

The convergence of these four developments
points at an opportunity.
A hypermedia substrate
that exposes its parts via
the Model Context Protocol,
ingests language-model-produced structured output
as typed parts directly,
embeds Content Credentials
on derived media assets,
and records the agent's prompts and decisions
as first-class provenance entries
solves several problems
the present tooling solves only partially.
The academic community
has begun to articulate this thesis.
The [PROV-AGENT model][research_prov_agent]
extends the World Wide Web Consortium PROV ontology
to capture the prompt, response,
and decision chain
of large language model agents
inside workflow provenance.
The [HyperAgents workshop at ECAI 2025][research_hyperagents]
explicitly frames the union of
Web of Things, distributed knowledge graphs,
and generative artificial intelligence
as a homogeneous hypermedia fabric
on which autonomous agents
browse, query, observe, and act.
The hypermedia-and-agents framing
is becoming the standard research vocabulary
for this problem.

Several contemporary tools
already approximate parts of this design.
[Jupyter AI][ref_jupyter_ai],
the official JupyterLab extension
for integrating large language model agents
into computational notebooks,
treats agent contributions
as cells in the notebook
that are subject to the same versioning
and provenance as human contributions.
[Ink and Switch's Jacquard project][ref_ink_switch_jacquard],
built on the
[Patchwork collaborative environment][ref_ink_switch_patchwork],
treats agent edits as branches
that can be merged in whole or in part,
with each agent action
attributed in the document history.
The general academic survey
of agent frameworks
is [Wang and colleagues' 2023 review][research_wang_agents],
updated through 2025,
and a more recent comparative analysis
of agent frameworks is provided in
[Derouiche and colleagues' 2025 survey][research_derouiche_agentic].

The implication for a successor to BTRON
is concrete.
The case for a hypermedia operating system
is stronger in 2026
than at any point
since the original BTRON proposition,
because the demand
for provenance, typed composition,
and agent-friendly addressability
is no longer
a niche knowledge-worker requirement.
It is becoming
a regulatory requirement
for any system
that produces or consumes
artificial-intelligence-generated content.
The hypermedia model
is one of the few designs
that addresses this demand
at the operating system layer
rather than as application-level scaffolding.

## The Web Browser as Hypermedia Substrate

A reasonable question is
whether the modern web browser
suffices as the hypermedia substrate
for the work that BTRON envisioned.
The answer is
that the browser provides
a substantial fraction of the model
and lacks the rest
in ways that block
the BTRON-style use case.

The browser provides
a structured document format with typed elements,
namely Hypertext Markup Language and the Document Object Model.
It provides embedded media,
including images, audio, video,
and procedural graphics
through Canvas and WebGL.
It provides a scripting and component model
through JavaScript,
Custom Elements,
and Shadow Document Object Model.
It provides universal hyperlinks
with stable syntax.
It provides a security model
with origin isolation.
And it provides universal deployment,
since the runtime is present
on nearly every device.

The browser does not provide
several of the properties
that the BTRON model required.
It does not provide
stable identity for sub-document parts
across revisions.
Uniform Resource Locator fragments are fragile
and depend on author discipline.
It does not provide
first-class typed links
beyond the plain anchor.
There is no link metadata,
no link direction,
and no system-managed link store.
It does not provide
canonical sub-documents by reference
rather than by copy.
Transclusion has been proposed
repeatedly under names
such as the Web Annotations Working Group's work,
but no standard has reached
universal browser support.
It does not provide
local persistence and editing as the default.
The browser is a viewer
with editing bolted on,
not an editor with viewing as a consequence.
It does not provide
in-place composition across origins.
Cross-origin iframes are sandboxes,
not collaborating handlers.
It does not provide
operating system-level resource scheduling
or real-time guarantees.
It does not provide
provenance and version tracking
as a platform service
rather than as an application concern.

The browser is therefore
the right substrate
for distribution and security boundaries
and the wrong substrate
for authorship and provenance.
Treating the browser
as a complete hypermedia operating system
collapses the distinction.
Treating the browser
as a deployment medium
on which a hypermedia application platform
must be constructed
is more honest.

## A Super-Browser as a Modern Realization

The most defensible modern architecture
for the BTRON idea
is a super-browser
that adopts the browser's universality and security model
and adds the missing primitives.
A minimal feature list
for such a system would include
the following.

Content-addressed parts,
in which every part has an identity
derived from its content
or from a stable identifier,
rather than from its position
in a Uniform Resource Locator.

Typed links as first-class storage,
in which a link store
managed by the platform
records source, target, type,
direction, and metadata,
and links survive
renames and edits.

Transclusion by reference,
in which a document can include
a live view of a part of another document
with the original remaining canonical
and updates visible to the dependent document.

Local-first persistence,
in which documents live on the user's device
and synchronize to the cloud,
rather than the reverse,
and in which conflict-free replicated data types
or operational transforms
handle merge.

Handler registration by part type,
in which editors register
as handlers for content types
and the platform composes them in place.
Sandboxing follows
the browser's origin model
extended to part types.

Provenance as a platform service,
in which the platform records,
for each part,
where it came from,
when it changed,
and what it depends on.
Users and tools query this
through a uniform interface.

Structural transformation,
in which typed parts
can be rendered to print, screen,
screen reader, and machine consumer
from a single source.

Optional real-time scheduling,
in which live parts
such as simulations and instruments
receive bounded-latency scheduling
from the platform.
This is where a real-time operating system substrate
would matter,
though a useful super-browser
can ship without it
in non-safety-critical settings.

Existing partial precedents
are worth studying as inputs.
Roam Research, Logseq, and Obsidian
provide block-level addressing
and bidirectional links
in personal knowledge tools.
Notion and Coda
provide typed blocks
and embedded databases.
Jupyter and Observable
provide live computational documents.
Solid provides personal data pods
with typed linked data.
Beaker Browser provided
peer-to-peer hypermedia.
Automerge and Yjs
provide local-first conflict-free replicated data type libraries.
[ActivityPub][ref_activitypub] and the IndieWeb
provide typed cross-site links
at a coarse granularity.

None of these partial precedents
is by itself
a successor to BTRON,
but a system that integrated
their best features
into a single super-browser
with a deliberate hypermedia commitment
would be a credible
modern realization
of the BTRON thesis,
restricted to the non-real-time portion.

A real-time hypermedia desktop,
as distinct from a super-browser,
would still need
a real-time operating system substrate
underneath
because the browser
is not engineered
for bounded latency guarantees.
For the user populations
that need bounded latency,
the path forward
is likely
a domain-specific platform
built directly on a real-time microkernel,
not a browser extension.

## Why the Gap Persists, a Corrected Diagnosis

A market gap that has persisted
for forty years
despite repeated well-funded attempts
is usually not explained
by engineering difficulty alone.
The fuller picture
has four components.

The first component is
that the engineering is genuinely difficult.
Compound document frameworks
must coordinate
memory, focus, undo,
crash recovery,
and security
across handler boundaries.
Most prior attempts
underestimated the depth
of the handler-protocol,
isolation, and provenance problems.
This component is necessary
but not sufficient
to explain the failures.

The second component is
that the go-to-market problem
is harder than the engineering problem.
Buyers in this segment
do not buy operating systems.
They buy outcomes,
namely traceability,
certification credit,
audit defensibility,
and reduced rework.
Products that name the outcome
succeed.
Products that name the technology
fail.
A successful entrant
must look like a vertical application
to its buyers,
even if its substrate
is a hypermedia operating system
underneath.

The third component is
that the partial substitutes
have entrenched.
DOORS, Polarion, Windchill,
ENOVIA, Vault, Gotham,
Relativity, and iManage
are not loved,
but they are deployed
at enormous scale.
Replacing them requires
data migration,
training,
recertification,
and political will
inside the buying organization.
The incumbents have absorbed
enough of the hypermedia thesis,
namely typed objects,
linked traceability,
and provenance,
to be defensible
against a clean replacement.
A new entrant
must beat them
on the dimensions they cover
and on the dimensions they miss,
simultaneously.

The fourth component is
that open standards in this space
have failed repeatedly.
Hypermedia depends on
shared part types
and link types.
Standardization in this space
is governed by the same dynamics
that produced
the long, painful history
of document format standards.
A viable entrant
must either own enough of the stack
to bypass standardization
or accept a slower path
through a consortium
with a sponsoring institution
willing to compel adoption.

A founder or program manager
who reads the situation
as "the engineering is the bottleneck"
will under-invest
in the other three components
and will produce
another technically excellent system
that fails to find a buyer.
A founder who reads the situation
as "the demand is real
and the engineering is one of four hard problems"
has a chance.

## How the Incumbents Compare

The previous sections named the partial substitutes
that occupy the regulated-industry market.
A side-by-side comparison
clarifies what each incumbent
has and lacks
relative to the BTRON hypermedia ideal.
The dimensions are typed parts,
typed links,
in-place handler composition,
provenance and audit,
and local-first persistence.
The check marks indicate
that the property is present
in a meaningful form,
not that it matches
the BTRON ideal exactly.

| Product | Typed parts | Typed links | In-place composition | Provenance and audit | Local-first option |
|---|---|---|---|---|---|
| [IBM DOORS Next][ref_doors] | Yes | Yes, OSLC | Limited | Yes, baselines and e-signatures | Yes, on-premises Jazz |
| [Siemens Polarion][ref_polarion] | Yes | Yes, configurable roles | Partial, LiveDocs | Yes, baselines and signatures | Yes, on-premises |
| [PTC Windchill][ref_windchill] | Yes, rich object model | Yes, BOM and association rules | Partial, Creo View | Yes, iterations and revisions | Yes, on-premises |
| [Dassault ENOVIA][ref_enovia] | Yes, schema-driven | Yes, with effectivity | Partial, Compass apps | Yes, maturity and baselines | Yes, on-premises |
| [Veeva Vault][ref_veeva_vault] | Yes, Vault Object Framework | Partial, document relations | Limited | Very strong, GxP audit trail | No, cloud-only |
| [Palantir Gotham][ref_palantir_gotham] | Yes, Ontology | Yes, typed and classified | Yes, Dossiers and Graph | Very strong, data tethering | Hybrid, Apollo deployments |
| [Palantir Foundry][ref_palantir_foundry] | Yes, Ontology | Yes, with cross-ontology lineage | Yes, Workshop and Slate | Very strong, end-to-end lineage | Hybrid, Apollo deployments |
| [Relativity][ref_relativity] | Yes, e-discovery types | Partial, families and clusters | Partial, configurable layouts | Very strong, evidentiary chain | Yes, on-premises Server |
| [iManage Work][ref_imanage] | Shallow, document-centric | Minimal | Partial, Microsoft 365 co-author | Yes, version and access audit | Yes, on-premises legacy |

Several patterns emerge.
The strongest typed-part and typed-link models
appear in
Palantir Foundry and Gotham,
followed by Dassault 3DEXPERIENCE
and the engineering-lifecycle tools.
The strongest in-place handler story
appears again in the Palantir products,
where Workshop, Slate, Quiver, Code Workbook,
Dossier, and Graph
all operate over the same Ontology objects.
The strongest provenance and audit story
appears in
Veeva Vault and Relativity,
both of which are designed
to meet evidentiary or regulatory standards.
Local-first persistence
is becoming the exception
rather than the rule.
Cloud-only operation
is the default for Veeva
and the strong default for the Palantir products
and for the cloud editions
of the engineering-lifecycle tools.

The universal shortfall
relative to the BTRON ideal
is consistent across all nine products.
None offers
operating-system-level typed parts.
None offers
operating-system-level typed links
that survive outside the vendor's platform.
None offers
user-composable in-place handler chains
spanning arbitrary applications.
Each is a closed federation
around its own ontology or document class.
The closest approximations
are the Palantir products,
which provide a rich shared ontology
behind a closed set of Palantir-built apps,
and ENOVIA's Compass,
which composes Dassault-built apps
over a shared schema.
A successor platform
that exposed similar typed parts and typed links
as operating system services
would inherit the demand
that these incumbents have validated
without inheriting their lock-in.

## Coexistence with the File and Application World

A hypermedia operating system
that demanded
the abandonment of every existing application
and every existing document
would fail
for the same reason
that BTRON failed
in the 1990s.
A credible successor must coexist
with the file-and-application world,
not replace it overnight.

The coexistence problem
has four parts.

The first part is
file system bridges.
The hypermedia link store
must be able to address
ordinary files in conventional file systems
through stable identifiers
that survive moves and renames.
The mechanism resembles
the inode-and-bookmark approach
that desktop file managers
have used for decades,
extended with content-addressing
as a fallback when the path-based identity breaks.
[Content-addressable storage][ref_content_addressable_storage]
provides the necessary primitive.

The second part is
import handlers for legacy formats.
Every meaningful office format,
namely Microsoft Word and Office Open XML,
OpenDocument, PDF, plain text,
Markdown, comma-separated values,
and the major image, audio, and video formats,
needs an import handler
that lifts the file
into a typed-part representation
on demand.
The lift is a one-way operation
on first encounter
and a synchronization operation
on subsequent edits.
The user perceives
the legacy file
as a sub-part of the hypermedia document
that can be edited in place
through the handler.
Round-trip preservation
to the legacy format
is the harder half of this problem
and is the reason
that prior compound-document frameworks
struggled with vendor cooperation.

The third part is
export and sharing across the boundary.
A user authoring a hypermedia document
that includes typed parts and typed links
needs to send a representation
to a colleague who lives in the file world.
The representation is necessarily lossy.
The exported file
loses the typed links
and the part identities
that the hypermedia substrate maintained.
The platform must communicate this loss
honestly,
typically by offering a portable representation
that retains the visible structure
but not the live behavior.
Web archive formats and PDF
are the existing precedents
for such lossy export.

The fourth part is
gradual adoption.
The platform must run usefully
on the user's first day
with only legacy files in view
and accumulate hypermedia properties
as the user produces new content
or invests in importing legacy material.
The platform must not punish
the user who never imports
by withholding basic file access.
This implies that
the hypermedia layer
sits above the file system,
not in place of it,
and that the file system remains
a first-class citizen
of the platform.
The user upgrades particular documents
to hypermedia at the point
that the upgrade pays for itself.

The historical precedent
for this kind of coexistence
is the spreadsheet.
VisiCalc and its successors
introduced a typed structured document
to a market dominated by
ledger books and typewriters.
Spreadsheets did not require
the abandonment of paper.
They became indispensable
for the work
that benefited from them
and remained absent
where the work did not.
The same pattern
is likely
for a hypermedia operating system
that coexists honestly with the file world.

## Viable Entry Strategies

If the diagnosis is correct,
the viable entry strategies
are constrained.

The vertical-first, platform-second strategy
picks one regulated vertical,
for example aerospace requirements engineering,
clinical trial documentation,
intelligence analysis,
or pharmaceutical regulatory submission,
and builds a product
that wins on outcomes
in that vertical.
The substrate is architected
as a hypermedia platform from day one,
but it is sold
as a vertical application.
Expansion to adjacent verticals
follows
once the substrate
has paid for itself.

The internal-program strategy
places the build
inside an organization
that already has
the demand,
the budget,
and the patience.
Defense primes,
national laboratories,
top-three pharmaceutical companies,
major regulators,
and large multilateral organizations
are plausible hosts.
The platform never becomes a product,
but the organization captures
the value
through reduced rework,
faster certification,
and lower audit exposure.
Internal programs ossify over time,
which means
the program must be funded
on a decadal horizon
with explicit refresh cycles.

The acquisition-path strategy
builds the hypermedia substrate
as a thin layer
that augments an incumbent,
namely DOORS, Polarion,
Vault, Gotham, or iManage,
with the explicit intent
of being acquired.
The substrate then becomes part of the incumbent
and reaches scale
through the incumbent's installed base.
This strategy
trades equity for distribution
and is feasible
only if the substrate
is genuinely complementary
to the incumbent's strengths.

The sponsored-standards strategy
anchors the platform
to a single large sponsor,
namely a regulator
or a multilateral body,
that can compel adoption
among the entities it oversees.
This is the only path
that has ever produced
wide adoption
of a shared document model,
and it has succeeded rarely.
Examples include
the [Health Level Seven][ref_hl7] family of standards
in healthcare,
the [Standard for the Exchange of Product Model Data][ref_step]
in manufacturing,
and the [Extensible Business Reporting Language][ref_xbrl]
in financial reporting.
None of these is a hypermedia operating system,
but each provides
a working precedent
for standards-led adoption
of a structured document model
in a regulated industry.

The path that has not worked,
on the historical evidence,
is the general-purpose-platform strategy,
in which a vendor
builds a hypermedia operating system
and waits for the right users
to discover it.
Every prior attempt at this path
has failed
for reasons that are not
solely about engineering difficulty.

## A Concrete Architectural Sketch

The discussion so far has been abstract.
A short architectural sketch
grounds the proposal
in components that exist today
and can be assembled
by a competent team
without invention from first principles.
The sketch is illustrative
rather than prescriptive.
A serious program
would substitute components
based on local constraints,
namely licensing, certification,
team experience, and ecosystem ties.

**Layer one, the verified microkernel.**
The trusted core
is the [seL4 microkernel][ref_sel4],
chosen for its formal verification
relative to its specification.
For programs
that prefer a more permissive license
or a more practical engineering ecosystem
than seL4 imposes,
the [Genode Operating System Framework][ref_genode]
on a non-verified base kernel
such as NOVA or its own hardware-supporting kernel
is an acceptable substitute
that preserves the capability discipline.

**Layer two, the component runtime.**
Above the microkernel,
the platform exposes
a capability-typed component runtime.
Two candidates exist.
Native components
written in a memory-safe language
such as Rust
communicate via
[Cap'n Proto][ref_capn_proto] capability-RPC.
Portable components
that the platform admits
across hardware architectures
ship as
[WebAssembly Component Model][ref_wasm_component_model]
modules under WebAssembly System Interface 0.2 or later.
The two component types coexist
through a shared capability protocol.

**Layer three, content-addressed storage.**
The link store and the part store
rest on content-addressed storage.
The mature options
are [InterPlanetary File System][ref_ipfs],
which is widely deployed
but has acknowledged performance and trust limitations,
and the newer [Iroh][ref_iroh],
which uses BLAKE3 hashing
and QUIC transport
and is better suited
to embedded and mobile clients.
For append-only signed feeds,
[Hypercore Protocol][ref_hypercore]
remains the canonical choice.

**Layer four, the conflict-free replicated data type substrate.**
Local-first persistence
with multi-device synchronization
rests on conflict-free replicated data types.
The mature options
are [Automerge][ref_automerge],
released as Automerge 3.0 in July 2025
with substantial memory improvements,
[Yjs][ref_yjs],
which dominates collaborative-editor integration,
and the newer [Loro][ref_loro],
which uses the Fugue algorithm
to reduce interleaving anomalies.
The earlier [Hypermerge][ref_hypermerge] project
is archived,
and its successor is Automerge-repo.

**Layer five, the link store and part registry.**
The link store
is a typed graph database
managed by the platform
as a system service.
Each link records source, target,
type, direction, and metadata.
The part registry
records each part's identity,
type, and current handler binding.
Both are addressed by capability
so that confined components
cannot enumerate the user's parts
without explicit grant.
This layer is novel
in the sense that
no existing open-source project
implements it as a standard service.
A serious program would build it.

**Layer six, the rendering substrate.**
Display surfaces composed
of typed handlers
require a graphics stack
that can host arbitrary handler-drawn content.
The candidates are
[Skia][ref_skia],
the Google two-dimensional graphics library
that powers Chrome, ChromeOS, Android, and Flutter,
and [Cairo][ref_cairo_graphics],
which offers superior PDF and PostScript output
where vector fidelity matters.
Text shaping
for non-trivial international content
requires [HarfBuzz][ref_harfbuzz],
and font rasterization
requires [FreeType][ref_freetype].
For embeddable browser-class rendering
where Web Platform compatibility is needed,
[Servo][ref_servo] is the only memory-safe option,
with [Chromium Embedded Framework][ref_cef]
and [WebKit][ref_webkit]
as the proven non-memory-safe alternatives.

**Layer seven, the editor frameworks.**
Structured editing
of prose, tables, code, and mixed content
rests on the editor frameworks
that the contemporary Web ecosystem has produced.
[ProseMirror][ref_prosemirror]
is the principled foundation
for schema-driven rich-text editing.
[TipTap][ref_tiptap]
provides higher-level user-interface components
above ProseMirror.
[Lexical][ref_lexical]
is Meta's alternative
with a tree-of-nodes data model.
[CodeMirror 6][ref_codemirror]
is the natural complement
for code regions inside documents.
For projectional editing
of non-textual notations,
including mathematics, diagrams, and forms,
[JetBrains Meta Programming System][ref_mps]
remains the canonical citation.

**Layer eight, the file-world bridge.**
The platform exposes
ordinary files in conventional file systems
through a translation layer
that lifts each file
into a typed part on first access
and maintains synchronization
for the file's lifetime.
The bridge integrates with
the local operating system's file events
through [Capsicum][ref_capsicum] capabilities
on FreeBSD-derived hosts
or analogous mechanisms elsewhere.
The user perceives the file
as a part of the hypermedia document,
with explicit indication
of the lossy-roundtrip warning
when the file is exported
back to the legacy format.

**Layer nine, the agent and provenance interface.**
The hypermedia platform exposes
its parts and links
to language-model agents
through the [Model Context Protocol][ref_mcp].
Agent contributions are admitted
as typed parts
with provenance records
attached to the link store.
Media assets carry
[Content Credentials][ref_content_credentials]
manifests in conformance with
the [Coalition for Content Provenance and Authenticity][ref_c2pa]
specification.
The platform's provenance model
follows the [PROV-AGENT][research_prov_agent] convention
of treating agent prompts, responses,
and decisions
as first-class entries
in the part history.

**Layer ten, the user-facing shell.**
The shell is the surface
on which the user composes documents,
navigates the link graph,
and invokes handlers.
The shell may borrow design cues
from Self's Morphic framework
for direct manipulation,
from Oberon's executable text
for command-as-document unification,
and from contemporary block editors
such as Notion and Logseq
for familiarity.
The shell is the part of the system
that varies most by audience.
A clinical workstation,
a legal review console,
an intelligence analyst surface,
and a research notebook
share the underlying layers
but present distinct shells.

The point of this sketch
is not that every program
must use these exact components.
The point is that
each layer of a hypermedia operating system
has at least one
production-quality open-source candidate
in 2026.
The integration task
is large but bounded.
The novel engineering
concentrates in layer five,
the link store and part registry,
which no existing project
implements as a standard service,
and in the cross-layer plumbing
that gives the platform
its character.
A team of competent engineers
with a decadal horizon
can ship a credible
vertical-first hypermedia operating system
on this stack
without inventing
new languages, kernels, or graphics systems.

## A Day in the Workflow, an Aerospace Requirements Example

The abstract argument benefits
from a concrete user journey.
The example below
follows a single safety analyst
through one working day
on a hypothetical real-time hypermedia desktop
deployed inside an aerospace prime contractor
that develops avionics
under [DO-178C][ref_do_178c]
and [ARP4754A][ref_arp4754a].
The example is illustrative
rather than prescriptive.
Many of the operations described
would compose differently
in a clinical, legal, or intelligence setting.

**Morning, configuration check.**
The analyst signs in at a workstation
that runs the hypermedia desktop
over a verified microkernel.
The login surface is itself a typed part
that confirms the user's identity,
the user's clearance level,
and the active project context.
On signing in, the desktop opens
the analyst's current workspace,
a hypermedia document
containing the day's open items
as typed parts linked
to the underlying engineering artifacts.

**Mid-morning, requirements analysis.**
The analyst opens a system requirement
for a flight control function.
The requirement is a typed part
in the platform's link store.
The part displays its text
in a prose handler
and exposes typed links
to its parent system specification,
its derived software requirements,
its safety analyses,
its verification evidence,
and its certification status.
The analyst clicks
a link to a safety analysis
to inspect the assumptions
underlying the requirement.
The safety analysis
opens in place
as a nested part
inside the workspace,
not in a separate application.
The link store records
the access for audit.

**Late morning, evidence assembly.**
The safety analysis cites
three test results
and one analytical proof.
Each citation is a typed link
to a typed part.
The analyst inspects the test results,
which open as nested parts
containing the test scripts,
the recorded outputs,
and the cryptographic signatures
of the test execution environment.
The analytical proof
opens as a Lean or Coq script
in a code editor handler,
with the proof state
visible alongside the prose.
The analyst confirms
that each piece of evidence
is current with respect to
the requirement's last modification timestamp.
The link store
flags one piece of evidence
as stale,
because the underlying test
was rerun yesterday
with a different result.

**Midday, agent-assisted summary.**
The analyst asks a configured agent
to summarize the open issues
across all requirements
in the safety case.
The agent operates through
the [Model Context Protocol][ref_mcp]
and accesses
only the parts the analyst's grant permits.
The agent's summary is itself a typed part,
appended to the workspace
with a provenance record
that names the agent,
the prompt,
the model version,
and the parts the agent inspected.
The agent's contribution
is visibly distinguished
from human-authored content
in the user interface.

**Afternoon, defect investigation.**
A failed test result
references a commit
in the source repository.
The analyst opens the commit
through a typed link
into a code repository handler.
The code repository
exposes its files
as typed parts
through a file-world bridge.
The analyst inspects the diff,
notices that a constant
in the control law
was changed from a measured value
to a placeholder,
and opens the issue.
The issue is filed
as a new typed part
linked to the requirement,
the test result,
and the offending commit.
A real-time alert
propagates through the link store
to subscribed reviewers.

**Late afternoon, certification artifact production.**
The analyst's team lead
requests a certification artifact package
for an upcoming Stage of Involvement review.
The lead's request
is itself a typed part,
addressed to the workspace.
The desktop assembles
a typed-part bundle
containing the requirements,
the evidence,
the analyses,
the agent contributions,
and the provenance records,
and renders the bundle
to a portable representation
suitable for transmission
to the certification authority.
The lossy export
is explicit.
The portable representation
preserves the structure and content
but loses the live links
and the typed part identities.
The link store
records the export
and tracks the consumer
who received it.

**Close of day, audit reconciliation.**
The analyst's workstation
synchronizes the workspace
to the program's authoritative link store
on the secured network.
The synchronization is
a conflict-free replicated data type merge,
not a file overwrite.
Concurrent edits
by other team members
during the day
appear as typed-part updates
with provenance attached.
A final audit-log entry
records the user's session,
the parts accessed,
the agents consulted,
and the artifacts produced.
The log is itself a typed part
in the link store,
accessible to the program's auditor
through a separate grant.

The day described above
is presently impossible
on any shipping platform.
Each step requires
a feature
that the file-and-application model
or any of the named incumbent products
withholds at the operating system level.
The aerospace prime that operates the workflow
today
accomplishes the same outcomes
through a confederation
of perhaps a dozen
specialist tools,
many manual handoffs,
and a substantial labor cost
on the analyst's part
to maintain the linkages by hand.
The case for a hypermedia operating system
in this setting
is the elimination
of that confederation
in favor of a single platform
on which the linkages are intrinsic.
Whether the elimination
is worth the engineering investment
is a question
the analysis sections of this article
have addressed at the market level.
The user journey
illustrates
what the engineering investment is for.

## Epistemic State of the Argument

The article makes three classes of claims,
and the reader is owed
a clear statement
of which is which.

The first class is historical fact.
The dates, named individuals,
named systems, and named events
are factual claims
that should hold against
independent verification.
The article's research passes
verified these against
primary and secondary sources
where available
and softened wording
where the record was unclear.
Notable softened claims include
the ITRON cumulative deployment figure,
the Lotus Notes peak seat count,
the HyperCard user count,
and the seL4 verification superlative.
Notable corrected claims include
the first-generation real-time operating systems date range,
the QNX founding location,
the OpenDoc shipping chronology,
and the Super 301 listing chronology.
Where a claim could not be verified,
the article either omits it
or marks it as inference.

The second class is structural analysis.
The six commitments of the hypermedia object model,
the five engineering commitments
for real-time hypermedia composition,
the four parts of the coexistence problem,
the ten-layer architectural sketch,
and the categorical mismatches
between the model and certain workloads
are structural claims.
These are conclusions
drawn from the engineering literature
and from the design choices
of the systems surveyed.
They are not provable
in the sense that
a mathematical theorem is provable,
but they are testable
in the sense that
a competing analysis
can dispute particular commitments
and propose alternatives.
The reader is invited to disagree
with the structural analysis
on engineering grounds.

The third class is market inference.
The four-component diagnosis
of why the gap persists,
the four entry strategies,
the analysis of who would benefit
and who would not,
the assertion that
the demand is real and well-funded,
and the recommendation
that vertical-first or internal-program
are the only paths
with historical precedent
are inferences from the historical record
and from the present configuration of the industry.
These claims are
the most opinionated portion of the article.
The reader is invited to disagree
with the market inference
on strategic grounds.
A founder, an analyst,
or a program manager
with direct experience
in the named industries
will have evidence
that this article cannot incorporate.

A useful test for the reader is
whether disagreement with the article
is on factual, structural, or strategic grounds.
Factual disagreement should be checkable
against the references.
Structural disagreement
is an engineering argument
that the article welcomes.
Strategic disagreement
is a market argument
that the article anticipates
but cannot resolve
without empirical entry into the market.

## Conclusion

BTRON was a sensible design
that lost to history
for reasons
which had only partly
to do with engineering merit.
The real-time half of the TRON Project
became infrastructure.
The hypermedia desktop half
became a footnote.
The structural demand
that BTRON aimed at,
namely operator-facing systems
in which bounded latency,
structural composition,
and provenance
must coexist,
has not gone away.
It is presently served
by a thicket of partial substitutes
that approximate parts of the design
at very high cost
and that do not interoperate cleanly.

The mass market
is correctly served
by the file and application model,
and a successor to BTRON
should not attempt
to dispossess that market.
The successor should aim instead
at the smaller population
whose work requires
structured composition,
strong provenance,
long-lived artifacts,
and bounded latency,
and for whom
the present tooling
is widely acknowledged
as inadequate.
The most defensible architecture
combines a hypermedia substrate
inspired by BTRON's commitments
with a real-time microkernel
inspired by the four decades
of progress
in operating system research
that has accumulated
since BTRON appeared.

A super-browser
that restores
what HTML and the cloud
discarded in transition
is a more reachable target
than a from-scratch real-time desktop,
and is appropriate
for the non-real-time portion
of the user population.
For the real-time portion,
a domain-specific platform
built on a real-time microkernel
remains necessary.
The two approaches
should be understood
as serving different populations,
not as alternatives.

A successful entry into this space
will not look like
"a better operating system."
It will look like
a vertical product
in a regulated industry
that happens to be built
on a deliberate hypermedia substrate
underneath.
The substrate is the platform.
The vertical is the wedge.
This is the pattern
that has succeeded
in adjacent enterprise markets
and the pattern
that prior attempts
in this market
have not followed.

Whether anyone will build it
remains an open question.
The demand is present.
The funding is present.
The technical components,
namely real-time microkernels,
conflict-free replicated data types,
verified isolation,
and modern graphics stacks,
have all matured
in ways
that were not available
to Sakamura in 1984.
What has not yet appeared
is the founder, program, or institution
willing to take on
the multi-decade commitment
that the design demands.
That a forty-year gap exists
is itself evidence
that the commitment is hard
and that the rewards
have so far been
insufficient to elicit it.

## Out of Scope

This article has stayed
at the architectural and market level.
Several topics
that a complete treatment would address
have been left out by intent
and are flagged here
so that the reader knows
what is missing.

The detailed security model
is out of scope.
The article identifies
that a hypermedia platform
under adversarial conditions
requires per-part isolation,
information-flow control,
and verified handler bytecode,
and names the relevant precedents
in seL4, Genode, and Capsicum.
A complete treatment
would specify the trust model
in formal terms,
identify the confused-deputy risks
of typed handler composition,
and discuss cross-domain solutions
for multi-classification material.

The data-model engineering
of the link store
is out of scope.
The article calls for
a typed link store
with content-addressed parts
and conflict-free replicated data type backing,
and names the candidate libraries.
A complete treatment
would specify the link type schema,
the part identity discipline,
the merge semantics
for concurrent edits
to typed parts,
and the cache-and-replication strategy
for cross-device synchronization.

The mobile and extended-reality question
is out of scope.
The article treats the desktop
as the canonical surface.
Whether the hypermedia model
applies usefully
to mobile devices,
to augmented-reality and virtual-reality systems,
or to operator-facing surfaces
that are neither desktops nor mobiles
is a substantive question
that this article does not address.

The economic model
is out of scope.
Xanadu proposed micropayments.
The Web settled on advertising.
Notes was sold by seat.
SharePoint was bundled with operating systems.
The Palantir products are sold by deployment.
A hypermedia operating system
will require an economic model
that funds platform development,
handler authorship,
and link-store hosting.
This article does not propose one.

The migration tooling design
is out of scope.
The article identifies
the coexistence requirement
and names the four parts
of the coexistence problem.
A complete treatment
would specify the import handler interface,
the round-trip preservation discipline
for each major legacy format,
and the user experience
of lossy export.

The verification methodology
is out of scope.
The article notes
that seL4 is formally verified
and that handler isolation
benefits from verified bytecode.
A complete treatment
would specify
which platform components
require formal verification,
which require certified compilation,
and which may rely on
testing and runtime monitoring.

The internationalization layer
beyond text shaping and rendering
is out of scope.
The article addresses
the TRON character work
as a historical curiosity
that anticipated Unicode coverage,
and names HarfBuzz and FreeType
as the rendering substrate.
A complete treatment
would address
bidirectional and complex-script editing,
input method integration
with handler composition,
locale-aware part metadata,
and accessibility services
including screen reader access
to typed parts.

These omissions
are deliberate
and reflect the article's intent
to map the design space
and the market diagnosis,
not to specify a product.
Each omitted topic
is a candidate
for a follow-up article
in this series.

## Reader's Next Steps

A reader who finds the analysis persuasive
and wants to engage further
has several entry points.

The [TRON Forum][ref_tron_forum]
maintains the specifications
for the systems that survived
from the original 1984 TRON proposition.
For practitioners
interested in the embedded
real-time operating system descendants
or in the hypermedia line through Cho Kanji,
the Forum is the canonical entry point.

The [seL4 community][ref_sel4]
and the [Genode Operating System Framework community][ref_genode]
are the most active venues
for capability-secure microkernel work
suitable for a hypermedia substrate.
Both publish regular release notes,
host community workshops,
and accept contributions
under their respective licenses.

The local-first software community
centered on
[Ink and Switch][research_local_first]
and on
[Automerge][ref_automerge],
[Yjs][ref_yjs], and [Loro][ref_loro]
is the most active venue
for conflict-free replicated data type
and hypermedia data engineering.
Anyone considering a serious build
should engage with this community
before committing to a synchronization architecture.

The [Solid Project][ref_solid]
hosted by the World Wide Web Consortium
is the most direct
contemporary continuation
of the original hypermedia thesis
in a standards-track form.
For practitioners interested in
typed linked data
and personal data pods,
the Solid working group
is the canonical venue.

The [HyperAgents Workshop][research_hyperagents]
co-located with the European Conference on Artificial Intelligence
and coordinated with the World Wide Web Consortium
Web Agents Community Group
is the most active academic venue
for the hypermedia-and-agents thesis.

The [Tools for Thought community][research_matuschak_nielsen_ttft]
organized through
the [Future of Coding podcast and forum][ref_future_of_coding],
[Andy Matuschak's writings][ref_andy_matuschak],
[Maggie Appleton's writings][ref_maggie_appleton],
and the [Hyperlink Academy][ref_hyperlink_academy]
provides the contemporary cultural framing
for hypermedia ideas
outside the regulated-industry market.
Anyone building a hypermedia tool
intended for knowledge workers
should engage with this community
to calibrate the design.

The [HyperCard Wikipedia entry][ref_hypercard]
and the
[Plan 9 Foundation archive][ref_plan_9_foundation]
remain the most accessible introductions
to two of the historical systems
discussed at length above.
Newcomers to the hypermedia tradition
benefit from reading these
before tackling the academic literature.

For the academic foundations,
[Bush's "As We May Think"][book_as_we_may_think],
[Engelbart and English's 1968 AFIPS paper][research_engelbart_1968],
[Nelson's Literary Machines][book_literary_machines],
[Sutherland's Sketchpad thesis][research_sketchpad],
[Kay and Goldberg's Personal Dynamic Media][research_personal_dynamic_media],
[Halasz's Reflections on NoteCards][research_halasz_1988],
and
[Freeman and Gelernter's Lifestreams CHI 1996 paper][research_lifestreams_chi96]
form a core reading list
of approximately seven canonical sources
that the rest of the field
returns to repeatedly.

## Glossary

The article uses several terms
with precise meanings
that the reader may find useful
to have in one place.

**Capability-based security.**
A model of access control
in which a subject possesses
an unforgeable token, called a capability,
that confers an authority
on an object.
The model is contrasted with
access-control-list discipline,
in which the object holds a list
of subjects and their permissions.
[Capsicum][ref_capsicum]
and [Cap'n Proto][ref_capn_proto]
are contemporary realizations
of the capability discipline.

**Compound document.**
A document composed of typed parts
edited in place by part-specific handlers.
Historical examples include
[OLE 2][ref_ole],
[OpenDoc][ref_opendoc],
[Bonobo][ref_bonobo], and
[KParts][ref_kparts].
The hypermedia object model
generalizes the compound document
by treating the part-and-link graph
as the primary structure
rather than as a feature
of one application.

**Conflict-free replicated data type.**
A data structure
that admits concurrent edits
on multiple replicas
and converges to a consistent state
without coordination.
The current production-grade libraries
are [Automerge][ref_automerge],
[Yjs][ref_yjs],
and [Loro][ref_loro].
Conflict-free replicated data types
are the mechanism that makes
local-first persistence
of typed parts technically tractable.

**Content-addressable storage.**
A storage scheme
in which each stored object
is named by a cryptographic hash
of its contents.
The name is stable
under any path or location change.
Git, [the InterPlanetary File System][ref_ipfs],
and [Iroh][ref_iroh]
are examples.

**Handler.**
The software component
that interprets, renders, and edits
a typed part.
In the hypermedia object model,
handlers compose
inside the document surface
rather than owning files.

**Hypermedia object model.**
The model articulated
in [the BTRON Proposition][ref_btron]
under which the user-visible primitive
is a typed part connected to other typed parts
by typed links,
rather than a file owned by an application.
The article's section
"The Hypermedia Object Model in Detail"
gives the six structural commitments.

**Link store.**
A system-managed graph database
that records the typed links
between typed parts.
The link store
is the operating system analogue
of a file system,
extended to relationships
rather than to single files.

**Microkernel.**
An operating system kernel
that retains only
the minimum necessary functionality,
typically scheduling,
inter-process communication,
and memory management,
and pushes file systems,
drivers, and networking
to user-space processes.
[QNX Neutrino][ref_qnx_neutrino],
[seL4][ref_sel4], and
[Redox OS][ref_redox]
are contemporary microkernel operating systems.

**Provenance.**
A record of where data came from,
who or what produced it,
and how it was transformed.
For artificial intelligence content,
provenance is the subject of
[the Coalition for Content Provenance
and Authenticity][ref_c2pa] specification
and the [PROV-AGENT][research_prov_agent] model
extending W3C PROV.

**Real-time operating system.**
An operating system
that guarantees responses
to events within bounded latency.
Examples include
[VxWorks][ref_vxworks],
[QNX Neutrino][ref_qnx_neutrino],
[INTEGRITY][ref_integrity],
[FreeRTOS][ref_freertos],
and
[ITRON][ref_itron]
and its descendants.

**Separation kernel.**
A microkernel-class operating system
that isolates partitions
both in space and in time,
typically to host
safety-critical and security-critical
workloads on the same hardware.
[INTEGRITY][ref_integrity]
is the canonical commercial example.

**Transclusion.**
The inclusion in one document
of a typed part
from another document
by reference rather than by copy.
The original part remains canonical
and updates propagate
to the dependent document.
The term originates with
[Ted Nelson][book_literary_machines]
in the Xanadu literature.

**Typed link.**
A link between typed parts
that carries
a source, a target, a type,
a direction, and metadata.
Typed links are first-class platform objects
in a hypermedia operating system,
distinct from the
unidirectional untyped anchor links
of the World Wide Web.

**Typed part.**
A unit of content
with a declared type
and a stable identity,
which may contain other parts
and which is edited
by a handler registered
for that type.

## References

- [Book, As We May Think][book_as_we_may_think]
- [Book, Literary Machines][book_literary_machines]
- [Book, Mirror Worlds][book_mirror_worlds]
- [Book, Tools for Thought, Rheingold 1985][book_tools_for_thought]
- [Reference, 9P Protocol][ref_9p_protocol]
- [Reference, ActivityPub][ref_activitypub]
- [Reference, Andy Matuschak Personal Site][ref_andy_matuschak]
- [Reference, Anthropic Tool Use][ref_anthropic_tool_use]
- [Reference, Appleton, A Brief History of the Digital Garden][ref_appleton_garden_history]
- [Reference, ARP4754A Guidelines for Development of Civil Aircraft and Systems][ref_arp4754a]
- [Reference, Automerge][ref_automerge]
- [Reference, Beaker Browser][ref_beaker]
- [Reference, BeOS][ref_beos]
- [Reference, BTRON][ref_btron]
- [Reference, Cairo Graphics 2D Library][ref_cairo_graphics]
- [Reference, Cairo Operating System Project][ref_cairo]
- [Reference, Cap'n Proto][ref_capn_proto]
- [Reference, Capsicum][ref_capsicum]
- [Reference, Cho Kanji][ref_cho_kanji]
- [Reference, Chromium Embedded Framework][ref_cef]
- [Reference, Coalition for Content Provenance and Authenticity][ref_c2pa]
- [Reference, Coda][ref_coda]
- [Reference, CodeMirror][ref_codemirror]
- [Reference, Component Object Model][ref_com]
- [Reference, Content Credentials][ref_content_credentials]
- [Reference, Content-addressable Storage][ref_content_addressable_storage]
- [Reference, Dassault ENOVIA][ref_enovia]
- [Reference, DO-178C][ref_do_178c]
- [Reference, Dynabook][ref_dynabook]
- [Reference, European Union Artificial Intelligence Act Article 50][ref_eu_ai_act_50]
- [Reference, Evergreen Notes][ref_evergreen_notes]
- [Reference, Extensible Business Reporting Language][ref_xbrl]
- [Reference, FreeRTOS][ref_freertos]
- [Reference, FreeType][ref_freetype]
- [Reference, Future of Coding][ref_future_of_coding]
- [Reference, Genode Operating System Framework][ref_genode]
- [Reference, GNOME Bonobo][ref_bonobo]
- [Reference, Google Gemini Function Calling][ref_gemini_function]
- [Reference, Green Hills INTEGRITY][ref_integrity]
- [Reference, HarfBuzz][ref_harfbuzz]
- [Reference, HCL Notes][ref_lotus_notes]
- [Reference, Health Level Seven][ref_hl7]
- [Reference, HyperCard][ref_hypercard]
- [Reference, Hypercore Protocol][ref_hypercore]
- [Reference, Hyperlink Academy][ref_hyperlink_academy]
- [Reference, Hypermerge Archived Project][ref_hypermerge]
- [Reference, IBM DOORS Next][ref_doors]
- [Reference, IEC 62304][ref_iec_62304]
- [Reference, iManage Work][ref_imanage]
- [Reference, Inferno Operating System][ref_inferno]
- [Reference, Ink and Switch Jacquard][ref_ink_switch_jacquard]
- [Reference, Ink and Switch Patchwork][ref_ink_switch_patchwork]
- [Reference, InterPlanetary File System][ref_ipfs]
- [Reference, Iroh Peer to Peer Networking][ref_iroh]
- [Reference, ISO 26262][ref_iso_26262]
- [Reference, ITRON][ref_itron]
- [Reference, JetBrains Meta Programming System][ref_mps]
- [Reference, Jupyter][ref_jupyter]
- [Reference, Jupyter AI][ref_jupyter_ai]
- [Reference, JX Operating System][ref_jx]
- [Reference, KDE KParts][ref_kparts]
- [Reference, Lexical Editor Framework][ref_lexical]
- [Reference, Lifestreams Project at Yale][ref_lifestreams]
- [Reference, Logseq][ref_logseq]
- [Reference, Loro CRDT Library][ref_loro]
- [Reference, Macintosh System Software][ref_mac_os]
- [Reference, Maggie Appleton Personal Site][ref_maggie_appleton]
- [Reference, Magic Ink, Bret Victor 2006][ref_magic_ink]
- [Reference, Microsoft SharePoint][ref_sharepoint]
- [Reference, Microsoft Windows][ref_windows]
- [Reference, Model Context Protocol][ref_mcp]
- [Reference, NeXTSTEP][ref_nextstep]
- [Reference, NoteCards][ref_notecards]
- [Reference, Notion][ref_notion]
- [Reference, NuttX][ref_nuttx]
- [Reference, Oberon Operating System][ref_oberon]
- [Reference, Object Linking and Embedding][ref_ole]
- [Reference, Observable][ref_observable]
- [Reference, Obsidian][ref_obsidian]
- [Reference, oN-Line System][ref_nls]
- [Reference, OpenAI Structured Outputs][ref_openai_structured]
- [Reference, OpenDoc][ref_opendoc]
- [Reference, OS/2][ref_os_2]
- [Reference, Palantir Foundry][ref_palantir_foundry]
- [Reference, Palantir Gotham][ref_palantir_gotham]
- [Reference, Plan 9 Foundation][ref_plan_9_foundation]
- [Reference, Plan 9 from Bell Labs][ref_plan_9]
- [Reference, Project Oberon][ref_project_oberon]
- [Reference, ProseMirror][ref_prosemirror]
- [Reference, pSOS][ref_psos]
- [Reference, PTC Windchill][ref_windchill]
- [Reference, QNX][ref_qnx]
- [Reference, QNX Neutrino][ref_qnx_neutrino]
- [Reference, QNX Photon microGUI][ref_qnx_photon]
- [Reference, Redox OS][ref_redox]
- [Reference, Relativity][ref_relativity]
- [Reference, Roam Research][ref_roam]
- [Reference, RTEMS][ref_rtems]
- [Reference, Self Programming Language][ref_self]
- [Reference, seL4][ref_sel4]
- [Reference, Servo Browser Engine][ref_servo]
- [Reference, Siemens Polarion][ref_polarion]
- [Reference, Sketchpad][ref_sketchpad]
- [Reference, Skia Graphics Library][ref_skia]
- [Reference, Smalltalk][ref_smalltalk]
- [Reference, Solid Project][ref_solid]
- [Reference, Standard for the Exchange of Product Model Data][ref_step]
- [Reference, Super 301][ref_super_301]
- [Reference, T-Kernel][ref_t_kernel]
- [Reference, TipTap Editor][ref_tiptap]
- [Reference, TRON Character Encoding][ref_tron_encoding]
- [Reference, TRON Forum][ref_tron_forum]
- [Reference, TRON Project][ref_tron_project]
- [Reference, Veeva Vault][ref_veeva_vault]
- [Reference, VRTX][ref_vrtx]
- [Reference, VxWorks][ref_vxworks]
- [Reference, WebAssembly Component Model][ref_wasm_component_model]
- [Reference, WebKit][ref_webkit]
- [Reference, World Wide Web][ref_www]
- [Reference, Yjs][ref_yjs]
- [Reference, Zephyr Project][ref_zephyr]
- [Reference, μITRON][ref_uitron]
- [Related Post, Fast-Moving Versus Mission-Critical Engineering][related_post_fast_moving_mission_critical]
- [Related Post, Mission Command Management Style][related_post_mission_command]
- [Research, Announcing Amazon FreeRTOS, AWS News Blog][research_amazon_freertos]
- [Research, Announcing the Model Context Protocol, Anthropic 2024][research_mcp_announcement]
- [Research, BlackBerry QNX 275 Million Vehicles Press Release][research_qnx_275m]
- [Research, Derouiche and colleagues, Agentic AI Frameworks, arXiv 2025][research_derouiche_agentic]
- [Research, Engelbart and English, A Research Center for Augmenting Human Intellect, AFIPS 1968][research_engelbart_1968]
- [Research, Halasz, Reflections on NoteCards, Communications of the ACM 1988][research_halasz_1988]
- [Research, HyperAgents Workshop at ECAI 2025][research_hyperagents]
- [Research, IEEE Milestone, TRON Real-time Operating System Family, 1984][research_ieee_milestone_tron]
- [Research, Information Management a Proposal, Berners-Lee at CERN 1989][research_berners_lee_1989]
- [Research, JX Operating System, USENIX 2002][research_jx_usenix]
- [Research, Klein and colleagues, seL4 Formal Verification of an OS Kernel, SOSP 2009][research_sel4_sosp]
- [Research, Kleppmann and colleagues, Local-First Software, Onward 2019][research_kleppmann_local_first]
- [Research, Lewis and colleagues, Retrieval-Augmented Generation, NeurIPS 2020][research_rag_lewis]
- [Research, Lifestreams, an Alternative to the Desktop Metaphor, CHI 1996][research_lifestreams_chi96]
- [Research, Lifestreams, a Storage Model for Personal Data, SIGMOD 1996][research_lifestreams_sigmod]
- [Research, Local-First Software, Ink and Switch][research_local_first]
- [Research, Maloney, The Self User Interface Framework][research_morphic]
- [Research, Mars Pathfinder Priority Inversion Engineering Note][research_mars_pathfinder]
- [Research, Matuschak and Nielsen, How can we develop transformative tools for thought?][research_matuschak_nielsen_ttft]
- [Research, NIST AI Risk Management Framework Generative AI Profile, 2024][research_nist_ai_rmf]
- [Research, Personal Dynamic Media, Kay and Goldberg 1977][research_personal_dynamic_media]
- [Research, PROV-AGENT Unified Provenance for AI Agent Interactions, IEEE eScience 2025][research_prov_agent]
- [Research, Sketchpad Thesis, Sutherland 1963][research_sketchpad]
- [Research, USTR Super 301 Statement of 25 May 1989][research_ustr_1989]
- [Research, Wang and colleagues, A Survey on Large Language Model based Autonomous Agents, 2023][research_wang_agents]

[book_as_we_may_think]: https://www.theatlantic.com/magazine/archive/1945/07/as-we-may-think/303881/
[book_literary_machines]: https://en.wikipedia.org/wiki/Literary_Machines
[book_mirror_worlds]: https://global.oup.com/academic/product/mirror-worlds-9780195079067
[book_tools_for_thought]: https://rheingold.com/texts/tft/
[ref_9p_protocol]: https://en.wikipedia.org/wiki/9P_(protocol)
[ref_activitypub]: https://en.wikipedia.org/wiki/ActivityPub
[ref_andy_matuschak]: https://andymatuschak.org/
[ref_anthropic_tool_use]: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview
[ref_appleton_garden_history]: https://maggieappleton.com/garden-history
[ref_arp4754a]: https://en.wikipedia.org/wiki/ARP4754
[ref_automerge]: https://automerge.org/
[ref_beaker]: https://en.wikipedia.org/wiki/Beaker_(web_browser)
[ref_beos]: https://en.wikipedia.org/wiki/BeOS
[ref_bonobo]: https://en.wikipedia.org/wiki/Bonobo_(component_model)
[ref_btron]: https://en.wikipedia.org/wiki/BTRON
[ref_c2pa]: https://c2pa.org/
[ref_cairo]: https://en.wikipedia.org/wiki/Cairo_(operating_system)
[ref_cairo_graphics]: https://www.cairographics.org/
[ref_capn_proto]: https://capnproto.org/
[ref_capsicum]: https://papers.freebsd.org/2010/rwatson-capsicum/
[ref_cef]: https://github.com/chromiumembedded/cef
[ref_cho_kanji]: https://www.chokanji.com/en/
[ref_coda]: https://en.wikipedia.org/wiki/Coda_(document_editor)
[ref_codemirror]: https://codemirror.net/
[ref_com]: https://en.wikipedia.org/wiki/Component_Object_Model
[ref_content_addressable_storage]: https://en.wikipedia.org/wiki/Content-addressable_storage
[ref_content_credentials]: https://contentcredentials.org/
[ref_do_178c]: https://en.wikipedia.org/wiki/DO-178C
[ref_doors]: https://www.ibm.com/products/requirements-management-doors-next
[ref_dynabook]: https://en.wikipedia.org/wiki/Dynabook
[ref_enovia]: https://www.3ds.com/products/enovia
[ref_eu_ai_act_50]: https://artificialintelligenceact.eu/article/50/
[ref_evergreen_notes]: https://notes.andymatuschak.org/Evergreen_notes
[ref_freertos]: https://www.freertos.org/
[ref_freetype]: https://freetype.org/
[ref_future_of_coding]: https://futureofcoding.org/
[ref_gemini_function]: https://ai.google.dev/gemini-api/docs/function-calling
[ref_genode]: https://genode.org/
[ref_harfbuzz]: https://harfbuzz.github.io/
[ref_hl7]: https://en.wikipedia.org/wiki/Health_Level_7
[ref_hypercard]: https://en.wikipedia.org/wiki/HyperCard
[ref_hypercore]: https://github.com/holepunchto/hypercore
[ref_hyperlink_academy]: https://hyperlink.academy/
[ref_hypermerge]: https://github.com/automerge/hypermerge
[ref_iec_62304]: https://en.wikipedia.org/wiki/IEC_62304
[ref_imanage]: https://imanage.com/product/imanage-work/
[ref_inferno]: https://en.wikipedia.org/wiki/Inferno_(operating_system)
[ref_ink_switch_jacquard]: https://www.inkandswitch.com/jacquard/notebook/01/
[ref_ink_switch_patchwork]: https://www.inkandswitch.com/patchwork/
[ref_integrity]: https://en.wikipedia.org/wiki/Integrity_(operating_system)
[ref_ipfs]: https://ipfs.tech/
[ref_iroh]: https://www.iroh.computer/
[ref_iso_26262]: https://en.wikipedia.org/wiki/ISO_26262
[ref_itron]: https://en.wikipedia.org/wiki/ITRON_project
[ref_jupyter]: https://jupyter.org/
[ref_jupyter_ai]: https://github.com/jupyterlab/jupyter-ai
[ref_jx]: https://en.wikipedia.org/wiki/JX_(operating_system)
[ref_kparts]: https://en.wikipedia.org/wiki/KParts
[ref_lexical]: https://lexical.dev/
[ref_lifestreams]: https://www.cs.yale.edu/homes/freeman/lifestreams.html
[ref_logseq]: https://logseq.com/
[ref_loro]: https://github.com/loro-dev/loro
[ref_lotus_notes]: https://en.wikipedia.org/wiki/HCL_Notes
[ref_mac_os]: https://en.wikipedia.org/wiki/Classic_Mac_OS
[ref_maggie_appleton]: https://maggieappleton.com/
[ref_magic_ink]: https://worrydream.com/MagicInk/
[ref_mcp]: https://modelcontextprotocol.io/
[ref_mps]: https://www.jetbrains.com/mps/
[ref_nextstep]: https://en.wikipedia.org/wiki/NeXTSTEP
[ref_nls]: https://en.wikipedia.org/wiki/NLS_(computer_system)
[ref_notecards]: https://en.wikipedia.org/wiki/NoteCards
[ref_notion]: https://www.notion.com/
[ref_nuttx]: https://nuttx.apache.org/
[ref_oberon]: https://en.wikipedia.org/wiki/Oberon_(operating_system)
[ref_observable]: https://observablehq.com/
[ref_obsidian]: https://obsidian.md/
[ref_ole]: https://en.wikipedia.org/wiki/Object_Linking_and_Embedding
[ref_openai_structured]: https://platform.openai.com/docs/guides/structured-outputs
[ref_opendoc]: https://en.wikipedia.org/wiki/OpenDoc
[ref_os_2]: https://en.wikipedia.org/wiki/OS/2
[ref_palantir_foundry]: https://www.palantir.com/platforms/foundry/
[ref_palantir_gotham]: https://www.palantir.com/platforms/gotham/
[ref_plan_9]: https://en.wikipedia.org/wiki/Plan_9_from_Bell_Labs
[ref_plan_9_foundation]: https://en.wikipedia.org/wiki/Plan_9_Foundation
[ref_polarion]: https://www.siemens.com/en-us/products/polarion/
[ref_project_oberon]: https://www.projectoberon.net/
[ref_prosemirror]: https://prosemirror.net/
[ref_psos]: https://en.wikipedia.org/wiki/PSOS_(real-time_operating_system)
[ref_qnx]: https://en.wikipedia.org/wiki/QNX
[ref_qnx_neutrino]: https://qnx.software/
[ref_qnx_photon]: https://en.wikipedia.org/wiki/QNX_Photon
[ref_redox]: https://www.redox-os.org/
[ref_relativity]: https://www.relativity.com/data-solutions/ediscovery/
[ref_roam]: https://roamresearch.com/
[ref_rtems]: https://www.rtems.org/
[ref_sel4]: https://sel4.systems/
[ref_self]: https://selflanguage.org/
[ref_servo]: https://servo.org/
[ref_sharepoint]: https://en.wikipedia.org/wiki/SharePoint
[ref_sketchpad]: https://en.wikipedia.org/wiki/Sketchpad
[ref_skia]: https://skia.org/
[ref_smalltalk]: https://en.wikipedia.org/wiki/Smalltalk
[ref_solid]: https://solidproject.org/
[ref_step]: https://en.wikipedia.org/wiki/ISO_10303
[ref_super_301]: https://en.wikipedia.org/wiki/Section_301_of_the_Trade_Act_of_1974
[ref_t_kernel]: https://en.wikipedia.org/wiki/T-Kernel
[ref_tiptap]: https://tiptap.dev/
[ref_tron_encoding]: https://en.wikipedia.org/wiki/TRON_(encoding)
[ref_tron_forum]: https://www.tron.org/
[ref_tron_project]: https://en.wikipedia.org/wiki/TRON_project
[ref_uitron]: https://en.wikipedia.org/wiki/ITRON_project
[ref_veeva_vault]: https://www.veeva.com/products/vault-platform/
[ref_vrtx]: https://en.wikipedia.org/wiki/Versatile_Real-Time_Executive
[ref_vxworks]: https://en.wikipedia.org/wiki/VxWorks
[ref_wasm_component_model]: https://component-model.bytecodealliance.org/
[ref_webkit]: https://webkit.org/
[ref_windchill]: https://www.ptc.com/en/products/windchill
[ref_windows]: https://en.wikipedia.org/wiki/Microsoft_Windows
[ref_www]: https://en.wikipedia.org/wiki/World_Wide_Web
[ref_xbrl]: https://en.wikipedia.org/wiki/XBRL
[ref_yjs]: https://yjs.dev/
[ref_zephyr]: https://www.zephyrproject.org/
[related_post_fast_moving_mission_critical]: {% post_url 2026-02-24-fast_moving_versus_mission_critical_engineering %}
[related_post_mission_command]: {% post_url 2026-02-17-mission_command_management_style %}
[research_amazon_freertos]: https://aws.amazon.com/blogs/aws/announcing-amazon-freertos/
[research_berners_lee_1989]: https://www.w3.org/History/1989/proposal.html
[research_derouiche_agentic]: https://arxiv.org/abs/2508.10146
[research_engelbart_1968]: https://dl.acm.org/doi/10.1145/1476589.1476645
[research_halasz_1988]: https://dl.acm.org/doi/10.1145/48511.48514
[research_hyperagents]: https://ecai2025.hyperagents.org/
[research_ieee_milestone_tron]: https://ethw.org/Milestones:TRON_Real-time_Operating_System_Family,_1984
[research_jx_usenix]: https://www.usenix.org/legacy/publications/library/proceedings/usenix02/full_papers/golm/golm.pdf
[research_kleppmann_local_first]: https://www.inkandswitch.com/essay/local-first/
[research_lifestreams_chi96]: https://www.cs.yale.edu/homes/freeman/ericchi96.html
[research_lifestreams_sigmod]: https://dl.acm.org/doi/10.1145/381854.381893
[research_local_first]: https://www.inkandswitch.com/local-first/
[research_mars_pathfinder]: https://www.cs.unc.edu/~anderson/teach/comp790/papers/mars_pathfinder_short_version.html
[research_matuschak_nielsen_ttft]: https://numinous.productions/ttft/
[research_mcp_announcement]: https://www.anthropic.com/news/model-context-protocol
[research_morphic]: https://ftp.squeak.org/docs/Self-4.0-UI-Framework.pdf
[research_nist_ai_rmf]: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
[research_personal_dynamic_media]: https://www.newmediareader.com/book_samples/nmr-26-kay.pdf
[research_prov_agent]: https://arxiv.org/abs/2508.02866
[research_qnx_275m]: https://www.automotiveworld.com/news-releases/blackberry-qnx-embedded-technology-powers-255-million-vehicles-on-the-road-today/
[research_rag_lewis]: https://arxiv.org/abs/2005.11401
[research_sel4_sosp]: https://dl.acm.org/doi/10.1145/1629575.1629596
[research_sketchpad]: https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-574.pdf
[research_ustr_1989]: https://worldjpn.net/documents/texts/JPUS/19890525.S1E.html
[research_wang_agents]: https://arxiv.org/abs/2308.11432
