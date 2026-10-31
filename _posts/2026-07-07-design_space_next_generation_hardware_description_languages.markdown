---
layout: post
mathjax: false
comments: true
title:  "The Design Space for Next-Generation Hardware Description Languages"
date:   2026-07-07 09:00:00 +0000
categories: hdl hardware design
series: hdl_thread
series_title: Hardware Description Languages
series_index: 2
---
<!-- A201 -->
<script>console.log("A201");</script>

Article A200
walked
the historical trajectory
of hardware description languages
across five decades
and closed
on the observation
that
each successive wave
appeared
in response to
a specific abstraction gap
that
prior languages
left open
at
the new scale
of integration.
This article
treats
the design space
that
the next wave
occupies.
The question
is not
which specific language
will succeed
Verilog and VHDL
in
industrial mainstream flows,
because
the standardisation-era languages
have proven
remarkably durable.
The question
is
which design levers
remain
under-exploited
in
existing hardware description tradition,
and
what
a hardware description language
that
combined those levers
would look like.

This article
is a
design-space survey.
It identifies
pain points
in current industrial hardware description flows,
records
what
the recent
next-generation hardware description languages
have addressed,
and
examines
several
further design levers
drawn from
adjacent
programming-language traditions.
It closes
with
a section
on
self-hosted synthesis toolchains,
where
the open-source
Yosys and nextpnr projects
have
established
production-adjacent precedent,
and
a
brief closer
on
cross-domain description languages
that
compose
hardware description
with
mechanical, thermal, and system-level modelling.

## Pain Points in Current Hardware Description Flows

Four
persistent pain points
appear
in
industrial
Verilog and VHDL
design flows.
Each
represents
a
specific verification gap
that
the existing hardware description languages
close
inadequately
or
not at all.

**Pipeline timing verification.**
A designer
who
manually balances
a pipeline
must
count
clock cycles
across
each
sequential stage
and
ensure that
propagation delays
do not
violate
setup and hold times.
The industrial practice
uses
static timing analysis
tools
that
run
after
the synthesis stage.
This
places
the timing feedback
at
the wrong point
in
the design cycle,
because
a synthesis run
for
a substantial
field-programmable-gate-array
design
takes
tens of minutes
to several hours.
Timing violations
discovered
at
this point
require
substantial
source-level rework.

**Clock domain crossing.**
Modern
system-on-chip designs
contain
multiple
clock domains,
and
data
that
crosses
from one domain
to another
must pass through
synchroniser circuits
to
avoid
metastability.
Clock-domain-crossing bugs
manifest
as
setup and hold time violations
of flip-flops,
jitter due to
unpredictable delays,
and
functional issues
arising from
convergence and divergence
of crossover paths.
Standard Verilog and VHDL
do not
express
the domain
of
a signal
in
the type system,
so
crossing errors
are
verified
by
external
[static analysis tools][ref_cdc_verification]
rather than
by
the language itself.

**Area budget verification.**
An
industrial hardware designer
who
writes
a complex
Verilog module
does not
know
in advance
how many
look-up tables,
flip-flops,
and
block random-access-memory blocks
the synthesised
implementation
will require.
The synthesis tool
reports
the actual usage
after
a
long synthesis run,
and
designs
that
exceed
the target device's
available resources
require
source-level restructuring
and
another synthesis cycle.
The compile-then-discover pattern
is
particularly costly
for
educational and prototype work
where
compile-cycle time
dominates
the total
design effort.

**Deadlock and livelock verification.**
Complex
finite-state machines
in
Verilog and VHDL
can enter
unmapped states
or
loop
without
producing
output signal transitions,
particularly
when
concurrent processes
interact
through
shared handshaking protocols.
The verification
of
deadlock freedom
uses
external
formal-verification tools
built
on
model checking
or
symbolic execution.
The languages
themselves
do not
prevent
the class of bugs
that
these tools
diagnose.

## What the Embedded-Domain-Specific-Language Revival Addresses

Article A200
recorded
the embedded-domain-specific-language revival
that
began
in the early twenty tens.
The revival
languages,
notably
[Chisel][ref_chisel],
[SpinalHDL][ref_spinalhdl],
[Amaranth][ref_amaranth],
and
[Clash][ref_clash],
address
several
of
the pain points
identified above,
though
not
uniformly
and
not
completely.

The Scala-based languages,
Chisel and SpinalHDL,
address
generator-based design
by
allowing
a
single parameterised description
to
produce
many
concrete circuit instances.
A designer
who
requires
a bank of
sixteen
functionally identical
memory controllers
can
write
one
parameterised module
in Chisel
and
instantiate it
sixteen times
at
elaboration time.
The standardisation-era languages
support
a
weaker form of
parameterisation
through
Verilog's `generate`
construct
and
VHDL's `generic` mechanism,
but
neither
matches
the full expressive power
of
Scala's type system
for
compile-time metaprogramming.

Amaranth
addresses
integration with
modern software-engineering workflows
by
embedding
hardware description
as
a Python library.
The Python ecosystem's
package management,
version control tooling,
and
continuous-integration infrastructure
apply
without
adaptation.
Amaranth
uses
[Yosys][ref_yosys]
as
its synthesis backend,
which
enables
open-source
end-to-end design flows
for
supported
field-programmable-gate-array
targets.

Clash
addresses
type-system expressiveness
by
embedding
hardware description
in Haskell.
Circuit descriptions
in Clash
inherit
Haskell's
type-inference and
higher-kinded types,
which
allow
the compiler
to
detect
a
substantial class
of
type errors
before
synthesis
proceeds.

None of
the embedded-DSL revival languages
address
pipeline timing verification
at
the source-language level.
None of them
express
clock-domain membership
in
the type system
in
a form
that
eliminates
the need
for
external
clock-domain-crossing analysis.
None of them
provide
a
statically-computed
area-budget bound
that
would allow
a designer
to
detect
resource overrun
without
running
the synthesis backend.
None of them
provide
static
deadlock and livelock verification.
The revival
narrowed
the abstraction gap
but
did not
close it.

## Further Design Levers

Several
design levers
that
adjacent
programming-language traditions
have developed
remain
under-exploited
in
existing hardware description languages.
This section
examines
four levers
and
notes
where
each
has been
demonstrated
in
research or
prototype systems.

**Static worst-case execution time analysis.**
The
worst-case execution time
of a program
is
the longest time
that
its execution
can take
under
any input.
Static
worst-case execution time analysis
computes
an upper bound
on
this time
from
source-language
control-flow analysis,
without
executing the program.
The technique
was
developed
principally
for
real-time software
and
is
[surveyed by Wilhelm and colleagues][research_wilhelm_wcet].
Applied
to
hardware description,
a
worst-case execution time
computed
in
clock cycles
per stage
gives
a
compile-time
timing bound
that
the designer
can
verify
before
the synthesis backend runs.
The
[Keleusma][ref_keleusma] language,
a
total functional stream processor
that
compiles to bytecode
for
embedded scripting
and
high-assurance embedded control contexts,
implements
static worst-case execution time analysis
at
module load
and
reports
the bound
in
its
verification pass.
The technique
is
not
inherently
tied to
software targets.
A hardware description language
that
adopted
the same
verification pass
would produce
a
per-module timing bound
that
static timing analysis
currently
reports
only
after synthesis.

**Totality and productivity as
type-system properties.**
The distinction between
functions
that
must
terminate
and
functions
that
must
produce output continuously
originates in
[Turner's total functional programming manifesto][research_turner_total]
and
was
formalised
through
[Rutten's universal-coalgebra treatment][research_rutten_universal_coalgebra]
and
his
subsequent stream-calculus work,
which
together
supply
the mathematical foundation
for
productivity
as
the coinductive dual
of termination.
Article A193
in the compilers series
developed
this framework
in detail.
A hardware description language
that
enforced
totality
on
combinational blocks
and
productivity
on
sequential blocks
at
the type-system level
would
statically
rule out
the deadlock
and livelock
patterns
that
external verification tools
currently diagnose.
Keleusma
categorises
functions
into
three classes,
namely
the atomic total `fn` category,
the non-atomic total `yield` category,
and
the productive divergent `loop` category,
which
maps
directly
onto
the combinational,
sequential,
and streaming
distinctions
in
hardware description.
The
[Kami framework][research_kami]
at MIT
demonstrates
a
Coq-based
hardware description language
whose type system
carries
formally verified
correctness properties
into
the compiled circuit.
The Koika language,
also from MIT,
provides
a
formally verified compiler
from
a Bluespec-inspired
rule-based
hardware description
into
gates,
with
machine-checked proofs
that
the semantics
compose
with
[one-rule-at-a-time execution][research_koika].
Both
Kami and Koika
demonstrate
that
formal-methods integration
at
the type-system level
is
feasible
for
hardware description
and
not
limited to
software targets.

**Coroutine primitives for
clock-domain crossing.**
Clock-domain crossing
is
usually described
in
Verilog and VHDL
through
handshaking protocols
that
the designer
implements
manually.
The pattern
lends itself
to
higher-level
description
under
coroutine
semantics,
where
a
data producer
in one clock domain
and
a
data consumer
in another clock domain
exchange
typed values
through
a
bounded buffer
whose
capacity
is
statically known.
Keleusma
uses
a
strict coroutine model
with
typed
`yield` and `resume` primitives
for
host-driven stream processing
in
its
software runtime.
Applied
to
hardware description,
the same
primitives
would express
clock-domain-crossing protocols
in
a form
that
the type system
verifies
directly,
without
requiring
external
clock-domain-crossing analysis.
The
[pragmatic formal verification methodology][research_cdc_verification]
that
industry practice
currently uses
would
correspondingly
become
redundant
for
languages
that
enforced
this discipline.

**Static memory footprint analysis.**
The
area-budget verification gap
identified above
maps
naturally
onto
static
memory-footprint analysis
in
the software context.
Keleusma
implements
static worst-case memory usage analysis
that
reports
the required
arena capacity
in bytes
at
module load,
without
executing the program.
The analog
in hardware description
would report
the required
look-up table count,
flip-flop count,
and
block random-access-memory blocks
before
the synthesis backend runs.
The information
is
in principle
computable
from
the source description
because
the synthesis tool
computes
essentially the same information
during its
elaboration phase.
Making
the computation
part of
the type-checking pass
rather than
part of
the synthesis backend
would
shorten
the compile-cycle time
for
area-budget verification
by
orders of magnitude.

**Composition.**
The four levers
above
compose.
A hardware description language
that
adopted
all four
would
statically verify
timing bounds,
combinational totality,
sequential productivity,
clock-domain-crossing protocols,
and
area budgets
at
the type-checking pass,
before
the synthesis backend runs.
The design
would
resemble
a
Rust-and-Bluespec
cross-breed,
retaining
the type-system expressiveness
of
functional programming
languages
while
compiling to
deterministic
hardware descriptions.
No existing
hardware description language
implements
all four levers
in
their strongest form.
Keleusma
implements
software-target
analogs
of three
of the four,
and
its
design-in-progress status
means
that
whether
its analysis passes
can be
adapted
to
a
hardware-target
implementation
remains
an open question.

## Self-Hosted Synthesis Toolchains

The industrial
hardware synthesis flow
depends on
substantial
proprietary tooling.
[AMD Vivado][ref_vivado],
[Intel Quartus][ref_quartus],
and
[Synopsys Synplify][ref_synplify]
occupy
the industrial mainstream
for
their respective
target device families.
The proprietary tools
represent
a
substantial dependency
for
any
long-term
autonomous system
that
must
generate
its own
hardware designs
without
external
software support.

Open-source alternatives
have
matured
over
the past decade
to
production-adjacent
capability
for
some device families.
The relevant projects
are
Yosys
for
register-transfer-level synthesis,
[nextpnr][ref_nextpnr]
for
place-and-route,
and
[F4PGA][ref_f4pga],
formerly known as
SymbiFlow,
which
coordinates
the tools
into
a unified
vendor-neutral flow.
The current F4PGA flow
supports
selected Lattice
and Xilinx 7-Series device families,
with
ongoing work
on
additional targets.
For
supported device families,
the open-source flow
delivers
end-to-end synthesis
from
Verilog or Amaranth source
to
device bitstream
without
proprietary dependencies.

A
self-hosted synthesis toolchain
would
extend
this precedent
by
running
the toolchain itself
on
the hardware
that
the toolchain
synthesises.
The concept
is
analogous to
a
self-hosted
software compiler
that
compiles
its own source.
Current
Yosys and nextpnr
run on
general-purpose
central-processing units
rather than
on
the field-programmable-gate-array fabric
that
they target,
so
the current state
is
open-source
but
not
self-hosted
in
the strict
compiler-tradition sense.

Two research directions
approach
the strict self-hosting endpoint.
The first
implements
a
compact synthesis toolchain
in
a hardware description language
itself,
such that
the toolchain
can be
synthesised
onto
the field-programmable-gate-array
alongside
the target design.
The second
implements
a
hardware description language
whose
compilation output
is
directly executable
by
a
programmable interconnect
without
a
separate synthesis stage.
Neither direction
has
produced
a
production-adjacent artefact
at
the time of writing,
though
the underlying technology
is
mature enough
that
prototype work
is
within reach
for
academic and
open-source
research groups.

The applicability
of
a
self-hosted synthesis toolchain
is
narrow
in
mainstream industrial contexts,
where
the compile-cycle time saved
does not
justify
the tooling complexity added.
The applicability
is
substantial
in
long-term
autonomous system
contexts
where
external
software support
cannot be
assumed,
and
in
educational contexts
where
the tooling stack
is
itself
the object of study.
The
[von Neumann
self-replicating machine][ref_von_neumann_probe]
concept,
occasionally discussed
in
the interstellar-mission
speculative literature,
depends on
self-hosted
synthesis capability
among
several other
essential
autonomous-manufacturing capabilities.
This article
does not
develop
the interstellar case
in detail
because
the practical applications
for
self-hosted synthesis
are
substantially
closer
to
present-day engineering.

## Cross-Domain Description Languages

The final
design lever
that
this article
examines
sits
outside
the traditional
hardware description language
scope.
A
complete
electronic system
description
must
model
not only
the digital logic
but also
the analog behaviour,
the thermal characteristics,
the mechanical packaging,
and
the system-level
requirements
that
the design
must satisfy.
Cross-domain
description languages
attempt
to
represent
some or all
of
these concerns
in
a unified
source form.

**SysML v2.**
The
[Systems Modeling Language
version 2][ref_sysml_v2],
approved
in
beta form
by
the Object Management Group
in
July of
two thousand twenty-three,
introduces
a
textual notation
for
system architecture description
alongside
the graphical notation
that
version one supported.
The textual syntax
enables
version-control workflows,
code review,
and
programmatic generation
of
system models
that
graphical-only
tools
did not
support.
SysML v2
represents
system components,
their attributes,
and
the connections
between them.
A hardware description language
that
integrated
with SysML v2
would
place
its digital logic modules
in
a
larger system context
that
included
mechanical, thermal, and requirements
constraints.

**Modelica.**
The
[Modelica language][ref_modelica],
developed
by
the Modelica Association,
provides
an
object-oriented
declarative language
for
multi-domain physical modelling.
Modelica descriptions
represent
mechanical, electrical, thermal, hydraulic, and control
subcomponents
in
a unified form
that
supports
differential-equation-based
simulation.
The
[OpenModelica][ref_openmodelica]
open-source implementation
provides
industrial-adjacent
tooling
for
Modelica-based
system simulation.
Combined
with
a hardware description language,
Modelica
would provide
the analog and thermal
context
that
the digital design
operates within.

**Constructive geometry languages.**
A
complete
electronic system
description
must also
represent
physical geometry
for
manufacturing.
[OpenSCAD][ref_openscad]
and
[CadQuery][ref_cadquery]
provide
textual representations
of
three-dimensional geometry
that
support
programmatic generation
of
computer-aided-design output.
A hardware description language
that
integrated
with
these tools
would
generate
mechanical enclosures
and
circuit-board layouts
alongside
the digital logic.

The composition
of
these three
description languages
with
a
next-generation
hardware description language
remains
an
open research question.
No existing
system-level tool
integrates
digital hardware description,
multi-domain physical modelling,
and
constructive geometry
into
a single
type-checked source form.
The technology
to
build
such an integration
is
available
in
principle,
but
the standardisation
across
domain boundaries
that
would enable
industrial adoption
does not yet exist.

## Conclusion

The design space
for
next-generation
hardware description languages
contains
several
under-exploited levers
drawn from
adjacent
programming-language traditions.
Static
worst-case execution time analysis,
type-system encoding
of
totality and productivity,
coroutine primitives
for
clock-domain crossing,
and
static
area budget analysis
each
address
a
persistent pain point
in
current industrial flows.
None of them
is
speculative.
Each
has been
demonstrated
in
software targets
by
existing languages,
including
Keleusma
as
a design-in-progress
example
that
implements
software-target analogs
of
three
of the four.

Self-hosted synthesis toolchains
represent
a
narrower
but
increasingly reachable
research direction,
enabled
by
the maturation
of
Yosys and nextpnr
into
production-adjacent
open-source flows.
Cross-domain description languages
that
compose
hardware description
with
system-level requirements,
multi-domain physical simulation,
and
constructive geometry
remain
an open research question
whose
standardisation status
lags behind
the individual
component languages.

The article A200
observed
that
each historical wave
of hardware description languages
appeared
in response to
a specific abstraction gap.
The gap
that
the next wave
appears
positioned
to close
combines
type-system integration
with
formal verification
at
the source-language level,
and
open-source
end-to-end
synthesis
flows
whose
production-adjacent capability
now
approaches
the industrial mainstream
for
some device families.
Whether
a
single language
will
combine
these design levers
into
a
consolidated
next-generation
hardware description language,
or
whether
the design space
will
remain
populated
by
multiple
partial-solution
languages,
is
a question
that
the current decade
will
answer.

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Primary Sources, Peer-Reviewed

- Bourgeat, Thomas, Clément Pit-Claudel, Adam Chlipala, and Arvind. 2020. "The Essence of Bluespec: A Core Language for Rule-Based Hardware Design." In *Proceedings of the 41st ACM SIGPLAN Conference on Programming Language Design and Implementation*. ACM. [https://doi.org/10.1145/3385412.3385965][research_koika]
- Choi, Joonwon, Muralidaran Vijayaraghavan, Benjamin Sherman, Adam Chlipala, and Arvind. 2017. "Kami: A Platform for High-Level Parametric Hardware Specification and Its Modular Verification." *Proceedings of the ACM on Programming Languages* 1 (ICFP): 1–30. [https://doi.org/10.1145/3110268][research_kami]
- Rutten, J. J. M. M. 2000. "Universal Coalgebra: A Theory of Systems." *Theoretical Computer Science* 249 (1): 3–80. [https://doi.org/10.1016/s0304-3975(00)00056-6][research_rutten_universal_coalgebra]
- Wilhelm, Reinhard, Jakob Engblom, Andreas Ermedahl, et al. 2008. "The Worst-Case Execution-Time Problem—Overview of Methods and Survey of Tools." *ACM Transactions on Embedded Computing Systems* 7 (3): 1–53. [https://doi.org/10.1145/1347375.1347389][research_wilhelm_wcet]

### Primary Sources, Non-Peer-Reviewed

- "Amaranth hardware description library." n.d. amaranth-lang.org. Accessed October 25, 2026. [https://amaranth-lang.org/][ref_amaranth]
- Kumar, Aman, Muhammad Ul Haque Khan, and Bijitendra Mittra. 2024. "Pragmatic Formal Verification Methodology for Clock Domain Crossing (CDC)." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2406.06533][ref_cdc_verification]
- "Pragmatic Formal Verification Methodology for Clock Domain Crossing." 2024. Preprint, . [https://arxiv.org/abs/2406.06533][research_cdc_verification]
- "Sgeos/keleusma: Total Function Stream Processor for Deterministic Control Loops." n.d. GitHub. Accessed October 25, 2026. [https://github.com/sgeos/keleusma][ref_keleusma]
- "Systems Modeling Language version two." n.d. github.com. Accessed October 25, 2026. [https://github.com/Systems-Modeling/SysML-v2-Release][ref_sysml_v2]
- Turner, David A. 2004. "Total Functional Programming." Preprint, TUGraz OPEN Library (Graz University of Technology). [https://doi.org/10.3217/jucs-010-07-0751][research_turner_total]
- "YosysHQ/nextpnr: Nextpnr Portable FPGA Place and Route Tool." n.d. GitHub. Accessed October 25, 2026. [https://github.com/YosysHQ/nextpnr][ref_nextpnr]

### Commercial Sources

- "AMD Vivado™ Design Suite." n.d. AMD. Accessed October 25, 2026. [https://www.amd.com/en/products/software/adaptive-socs-and-fpgas/vivado.html][ref_vivado]

### General Sources

- "CadQuery programmatic computer-aided-design library." n.d. Accessed October 25, 2026. [https://cadquery.readthedocs.io/][ref_cadquery]
- "Clash Haskell-based hardware description." n.d. Accessed October 25, 2026. [https://clash-lang.org/][ref_clash]
- "F4PGA open-source field-programmable-gate-array toolchain." n.d. Accessed October 25, 2026. [https://f4pga.readthedocs.io/][ref_f4pga]
- "Modelica multi-domain modelling language." n.d. Accessed October 25, 2026. [https://modelica.org/][ref_modelica]
- "OpenModelica open-source Modelica implementation." n.d. Accessed October 25, 2026. [https://openmodelica.org/][ref_openmodelica]
- "OpenSCAD programmatic solid computer-aided-design language." n.d. Accessed October 25, 2026. [https://openscad.org/][ref_openscad]
- "Quartus® Prime Design Software \| Altera® FPGA." n.d. Accessed October 25, 2026. [https://www.intel.com/content/www/us/en/products/details/fpga/development-tools/quartus-prime.html][ref_quartus]
- "SpinalHDL hardware description language." n.d. Accessed October 25, 2026. [https://spinalhdl.github.io/SpinalDoc-RTD/][ref_spinalhdl]
- "Synplify \| Logic Synthesis for FPGA Design." n.d. Accessed October 25, 2026. [https://www.synopsys.com/implementation-and-signoff/fpga-based-design/synplify-pro.html][ref_synplify]
- "Yosys Open SYnthesis Suite:: About." n.d. Accessed October 25, 2026. [https://yosyshq.net/yosys/][ref_yosys]

### Tertiary Sources

- "Chisel (Programming Language)." 2025. Wikipedia. Last modified December 22, at 10:02 (UTC). [https://en.wikipedia.org/w/index.php?title=Chisel\_(programming\_language)&oldid=1328884818][ref_chisel]
- "Self-Replicating Spacecraft." 2026. Wikipedia. Last modified June 5, at 05:34 (UTC). [https://en.wikipedia.org/w/index.php?title=Self-replicating\_spacecraft&oldid=1357876287][ref_von_neumann_probe]

[ref_amaranth]: https://amaranth-lang.org/
[ref_cadquery]: https://cadquery.readthedocs.io/
[ref_cdc_verification]: https://doi.org/10.48550/arxiv.2406.06533
[ref_chisel]: https://en.wikipedia.org/w/index.php?title=Chisel_(programming_language)&oldid=1328884818
[ref_clash]: https://clash-lang.org/
[ref_f4pga]: https://f4pga.readthedocs.io/
[ref_keleusma]: https://github.com/sgeos/keleusma
[ref_modelica]: https://modelica.org/
[ref_nextpnr]: https://github.com/YosysHQ/nextpnr
[ref_openmodelica]: https://openmodelica.org/
[ref_openscad]: https://openscad.org/
[ref_quartus]: https://www.intel.com/content/www/us/en/products/details/fpga/development-tools/quartus-prime.html
[ref_spinalhdl]: https://spinalhdl.github.io/SpinalDoc-RTD/
[ref_synplify]: https://www.synopsys.com/implementation-and-signoff/fpga-based-design/synplify-pro.html
[ref_sysml_v2]: https://github.com/Systems-Modeling/SysML-v2-Release
[ref_vivado]: https://www.amd.com/en/products/software/adaptive-socs-and-fpgas/vivado.html
[ref_von_neumann_probe]: https://en.wikipedia.org/w/index.php?title=Self-replicating_spacecraft&oldid=1357876287
[ref_yosys]: https://yosyshq.net/yosys/
[research_cdc_verification]: https://arxiv.org/abs/2406.06533
[research_kami]: https://doi.org/10.1145/3110268
[research_koika]: https://doi.org/10.1145/3385412.3385965
[research_rutten_universal_coalgebra]: https://doi.org/10.1016/s0304-3975(00)00056-6
[research_turner_total]: https://doi.org/10.3217/jucs-010-07-0751
[research_wilhelm_wcet]: https://doi.org/10.1145/1347375.1347389
