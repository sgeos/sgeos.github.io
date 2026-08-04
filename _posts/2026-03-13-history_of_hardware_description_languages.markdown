---
layout: post
mathjax: true
comments: true
title:  "A History of Hardware Description Languages"
date:   2026-03-13 09:00:00 +0000
categories: hdl hardware history
series: hdl_thread
series_title: Hardware Description Languages
series_index: 1
---
<!-- A200 -->
<script>console.log("A200");</script>

Hardware description languages
occupy
an unusual position
in the taxonomy of programming languages.
They are compiled
by tools called synthesisers
rather than by compilers,
their output
is not a program
but a circuit
described as
a netlist of gates
and wires,
and their execution semantics
are defined
in terms of
concurrent signal propagation
rather than
sequential instruction dispatch.
The languages
in this family
form
a coherent tradition
that runs
from
academic prototypes
in the nineteen seventies
through
commercial standardisation
in the nineteen eighties and nineteen nineties
to
a modern embedded-domain-specific-language revival
that began
in the twenty tens
and continues
into the present.

This article
walks
the history
in one pass
because
the total number
of languages
that
warrant serious historical treatment
is
modest,
on the order of
two dozen,
and the tradition
groups naturally
into
three overlapping eras
that share
architectural DNA
across their transitions.
The three eras
are
the academic prototypes
from
approximately nineteen seventy
to
nineteen eighty-four,
the commercial standardisation era
from
nineteen eighty-four
to
approximately two thousand ten,
and the
embedded-domain-specific-language revival
that continues
from
approximately two thousand ten
into
the present.

The article
is
descriptive rather than
prescriptive.
It records
what happened,
identifies
the design-complexity forcing function
that motivated
each successive wave,
and closes
with observations
about
where
the space
appears
to be
going.

## Prehistory and the Design-Complexity Forcing Function

The pre-hardware-description-language era
of digital design
worked
at the gate and netlist level.
A designer
drew
a schematic
that listed
gates,
flip-flops,
and wires,
and the schematic
was fabricated
directly
into
integrated circuits.
This approach
scaled
to
the small-scale-integration and medium-scale-integration
levels
of
the nineteen sixties and early nineteen seventies,
where
a full chip
might contain
a few thousand transistors
and
a manageable number of gates.

The forcing function
that motivated
the introduction of
hardware description languages
was
the transition
from
medium-scale integration
to
large-scale integration
and
very-large-scale integration
across
the nineteen seventies.
Transistor count per chip
grew
according to
Moore's Law,
which
Gordon Moore
formulated
in
nineteen sixty-five
and revised
in
nineteen seventy-five,
namely

$$
N(t) = N_0 \cdot 2^{t / T},
$$

where
$N(t)$
is the transistor count
per chip
at time $t$,
$N_0$
is the initial count,
and
$T$
is the doubling period,
approximately
eighteen to
twenty-four months.
As
transistor counts per chip
crossed
the ten thousand
and later
the hundred thousand
thresholds,
manual schematic capture
became
impractical.
A designer
could no longer
draw
every gate
by hand.
The abstraction layer
had to
move up
to
match
the growth
in chip complexity.

The design-complexity forcing function
repeats
at each subsequent wave
in the history.
Every major hardware description language
introduced
between
nineteen seventy
and
the present
appeared
in response to
an abstraction gap
that
prior languages
did not close.
The abstraction gap
in the seventies
was
gate-level to
register-transfer-level.
The gap
in the nineteen eighties
was
register-transfer-level to
behavioural.
The gap
in the two thousands
was
behavioural to
transaction-level and system-level.
The gap
in the twenty tens
was
system-level to
generator-and-parameterised design.
Each language
that
this article treats
sits
at
one of
these transitions.

## Academic Prototypes, Approximately Nineteen Seventy to Nineteen Eighty-Four

The academic era
produced
several hardware description languages
that
established
the vocabulary
and
the design patterns
that later commercial languages
would inherit.
None of the languages
in this era
achieved
widespread industrial adoption
in their original form,
but
they contributed
essential
architectural ideas
to
the languages
that
did achieve it.

**Instruction Set Processor Specifications (ISPS).**
ISPS
was
developed
at
Carnegie Mellon University
in the mid nineteen seventies
under
the DEC PDP-eleven and PDP-ten
architecture-description work
of
Mario Barbacci and colleagues.
The language
targeted
the description
of
processor instruction sets
and
their behaviour
at
the register-transfer level.
ISPS
influenced
the later
processor-description tradition
that
appears
in
GNU Superoptimizer,
in
the ARM Architecture Description Language,
and
in
the LLVM target-description files.
It did not
directly influence
the general-purpose hardware description language family
that this article
principally treats,
but it belongs
in the historical record
because
it established
the pattern
of
using
a formal language
to describe hardware behaviour.

**KARL.**
KARL,
the KAiserslautern Register-transfer Language,
was
developed
by Reiner Hartenstein
and his students
at
the Technical University of Kaiserslautern
across
the nineteen seventies and nineteen eighties.
KARL
was
one of the first
hardware description languages
to
receive
a full formal semantics
and
a working simulator.
Its influence
on
subsequent European hardware description work
was substantial,
though
it did not
achieve
American commercial adoption.

**ELLA.**
ELLA
was
developed at
the Royal Signals and Radar Establishment
in the United Kingdom
across
the nineteen seventies and nineteen eighties.
It was
used
for
British defence
hardware description
into the nineteen nineties
and had
a small but persistent user community
that
outlasted
its official maintenance.

**Silvar-Lisco HHDL,
CDL,
and
MetaHDL.**
Several
commercial and academic prototypes
appeared
in the same period
under
various acronyms.
Most did not
survive
into
the standardisation era.
The historical record
tends
to
subsume them
under
the broader category
of
pre-Verilog academic hardware description languages,
and
this article follows
that convention.

The academic era
established
several patterns
that
carried forward.
The register-transfer level
as
the natural abstraction
between
behavioural description
and
gate-level implementation
came from this era.
The distinction between
combinational and sequential blocks
came from this era.
The event-driven simulation semantics
that all subsequent hardware description languages
inherit
came
from this era.
The academic prototypes
did not
achieve
industrial adoption
because
none of them
offered
a
sufficiently attractive combination
of
language ergonomics,
simulator performance,
and
industrial tooling.
The commercial standardisation era
that followed
would
supply
all three.

## The Standardisation Era, Nineteen Eighty-Four to Approximately Two Thousand Ten

The standardisation era
begins
with
the parallel emergence
of
Verilog and VHDL
in
the mid nineteen eighties
and continues
through
their IEEE standardisation
in the mid nineteen nineties
into
the SystemVerilog and SystemC extensions
of
the two thousands.
The two dominant languages
of this era,
Verilog and VHDL,
have coexisted
for four decades
and
now
support
essentially the same
industrial design flows
with
different syntactic conventions.

**Verilog.**
Verilog
was
developed
between
late nineteen eighty-three
and
early nineteen eighty-four
by
Prabhu Goel,
Phil Moorby,
and
Chi-Lai Huang
at
Automated Integrated Design Systems,
the company
that
renamed itself
Gateway Design Automation
in
nineteen eighty-five.
Moorby wrote
the first Verilog simulator,
which came to market
in
early nineteen eighty-five,
and
the faster
Verilog-XL simulator
followed
in
nineteen eighty-seven.
Cadence Design Systems
acquired
Gateway
in
nineteen ninety
and
released
the Verilog language definition
to
Open Verilog International,
an industry consortium,
in
nineteen ninety-one.
The Institute of Electrical and Electronics Engineers
subsequently
standardised
the language
as
IEEE 1364
in
nineteen ninety-five.
The 1364 standard
was
revised
in
two thousand one and
two thousand five.

Verilog's design
prioritised
simulator throughput
and
implementation simplicity.
The syntax
resembles
the C programming language
at
the statement level,
with
concurrent `always` blocks
substituting
for
sequential function calls.
The language
succeeded
commercially
because
Gateway
had
a working simulator
in nineteen eighty-four
that
outperformed
academic simulators
by
substantial margins,
and
because
the language
was
straightforward enough
that
digital designers
who had been
working
at
the gate level
could learn it
in
a few weeks.

**VHDL.**
VHDL,
the VHSIC Hardware Description Language,
was
developed
under
the Very High Speed Integrated Circuits
program
of the United States Department of Defense.
The VHSIC program itself
began
in
nineteen eighty,
and
the VHDL-specific work
started
under
United States Air Force
contract F33615-83-C-1003
in
nineteen eighty-three.
The development team
comprised
Intermetrics
as
the prime contractor
and language experts,
Texas Instruments
as
the chip-design experts,
and
International Business Machines
as
the computer-system experts.
At the end of the program
in
March of nineteen eighty-six,
the Institute of Electrical and Electronics Engineers
took over
standardisation
through
the VHDL Analysis and Standardization Group,
and
IEEE 1076
was
released
in
nineteen eighty-seven.
The VHSIC program
had
a
substantially larger budget
than
Verilog's commercial origins,
and
VHDL's design
reflects
the defence-contracting
requirements
of
its sponsor.
The language
supports
strict type checking,
package-based
modularity,
and
formal
configuration management
that
Verilog
does not
match
without
substantial extensions.

VHDL's syntax
resembles
Ada
at
the statement level,
which
is
unsurprising
given that
Ada
was
the DoD
programming language
of the same era.
The language
achieved
industrial adoption
through
DoD contracting requirements
that
mandated
VHDL descriptions
for
defence electronics,
and
through
European standardisation efforts
that
preferred VHDL
over
Verilog
for
similar reasons
of
formal rigour.

The Verilog-and-VHDL split
divided
the industrial hardware design community
along
geographic and application lines.
North American commercial designers
predominantly used Verilog.
European designers,
defence contractors,
and
formal-verification
proponents
predominantly used VHDL.
The split
persisted
for
two decades
and
is only
now
receding
as
SystemVerilog
increasingly
absorbs
both traditions.

**SystemVerilog.**
SystemVerilog
extended Verilog
with
verification and design features
that
industrial users
had accumulated
by
the late nineteen nineties.
Accellera,
the industry consortium
that
manages
hardware design standards,
released
the initial SystemVerilog specification
in
two thousand two,
and
IEEE
standardised the language
as
IEEE 1800
in
two thousand five.
SystemVerilog
added
strong data types,
object-oriented classes
for
verification,
assertion syntax,
and
interface constructs
that
factored
common Verilog boilerplate
into
reusable modules.

SystemVerilog Assertions,
often abbreviated as SVA,
provided
a formal property specification syntax
for
temporal assertions
that
industrial designers
could embed
in
their Verilog code.
The Universal Verification Methodology,
UVM,
built
on
SystemVerilog's
object-oriented features
to
provide
a
standard verification testbench framework.
Both
SVA and UVM
are
now
industry standard
for
verification-heavy design flows.

**SystemC.**
SystemC
originated
at Synopsys
in nineteen ninety-nine
as
a
C-plus-plus class library
for
hardware modelling
at
the transaction level.
The Open SystemC Initiative,
OSCI,
formed
in
two thousand
as
an independent consortium
to
develop and promote
the language,
and released
version 2.0
in
two thousand two.
IEEE
standardised SystemC
as
IEEE 1666
in
two thousand five.
Accellera
and OSCI
subsequently merged
in
December of two thousand eleven
as
Accellera Systems Initiative.
SystemC
targeted
system-level design
and
software-hardware co-design,
where
the same
description
could serve
both
as
a simulation model
for
early software development
and
as
a synthesisable specification
for
subsequent hardware implementation.

SystemC's C-plus-plus foundation
gave it
access to
the extensive
software-engineering ecosystem
that
Verilog and VHDL
could not
match.
The language
achieved
industrial adoption
in
system-on-chip design flows
where
transaction-level modelling
was
essential,
particularly
in
mobile-processor and
consumer-electronics
design.

**Bluespec.**
Bluespec SystemVerilog,
often abbreviated as BSV,
originated
in
research
by
Arvind Mithal
and
James Hoe
at
the Massachusetts Institute of Technology
in the late nineteen nineties.
Lennart Augustsson
wrote
the initial implementation,
called BH,
as
a Haskell variant.
Bluespec Incorporated
was
co-founded
in June of two thousand three
by
Arvind Mithal
and
Joe Stoy
of Oxford University
to
commercialise the language.
The language
combined
Verilog syntax
with
a
guarded-atomic-action semantics
that
allowed
the compiler
to
schedule
rule execution
into
efficient hardware
without
manual pipelining.
Bluespec
targeted
high-frequency design
and
formal verification,
and
it achieved
industrial adoption
in
niche applications
where
the correctness-by-construction
argument
justified
the tooling investment.

The standardisation era
established
Verilog and VHDL
as
the two industrial-standard hardware description languages,
extended them
with
SystemVerilog and SystemC
for
verification and system-level modelling,
and
demonstrated
with
Bluespec
that
higher-level semantics
could be
introduced
into
the same syntactic family
without
breaking
the industrial tooling.

## The Embedded-Domain-Specific-Language Revival, Approximately Two Thousand Ten to the Present

The embedded-domain-specific-language revival
began
in the early twenty tens
in response to
several forcing functions
that
the standardisation-era languages
did not
adequately address.
The first
was
generator-based design,
where
a single parameterised description
should produce
many concrete circuit instances
depending on
compile-time parameters.
The second
was
tighter integration with
software design tools
and
version-control workflows.
The third
was
the desire
for
more expressive type systems
and
better error messages
than
Verilog and VHDL
could easily provide.

The revival
embeds
hardware description
as
a
domain-specific language
inside
a general-purpose host language,
which
gives
the hardware designer
access to
the host language's
type system,
build system,
package ecosystem,
and
development tools.
The trade-off
is that
the designer
must learn
the host language
and
its idioms
in addition to
the hardware-description embedding,
which
imposes
a
non-trivial learning cost.

**Chisel.**
Chisel,
the Constructing Hardware in a Scala Embedded Language,
was
developed
by
Krste Asanović's group
at
the Parallel Computing Laboratory
of
the University of California Berkeley
beginning
in
two thousand twelve.
The core Chisel team
included
Asanović
along with
graduate students
Yunsup Lee
and
Andrew Waterman,
who
also
originated
the RISC-V instruction set architecture
in
the same lab.
Chisel
embeds
hardware description
as
a Scala library.
The Rocket Chip
generator,
which produces
RISC-V processor implementations,
is written in Chisel,
which
gave
the language
substantial
credibility
in
academic and industrial RISC-V
design flows.

**SpinalHDL.**
SpinalHDL
was
developed
by
Charles Papon
beginning
in
two thousand fifteen.
Like Chisel,
SpinalHDL
embeds
hardware description
as
a Scala library.
SpinalHDL
diverged from Chisel
by
emphasising
strong static typing
and
by
providing
a
richer standard library
of
pre-designed
hardware components.
The two Scala-based languages
now
coexist
as
complementary alternatives
in the same
overall
generator-based design space.

**Amaranth.**
Amaranth,
originally called nMigen,
was
developed
by
Catherine "whitequark"
and other contributors
beginning
in December of two thousand eighteen,
with
the rename to Amaranth
announced in December of two thousand twenty-one.
Amaranth
embeds
hardware description
as
a Python library
and
uses Yosys
as
its synthesis backend.
It succeeded Migen,
Sébastien Bourdeauducq's
earlier
Python-based hardware description library
from
two thousand seven.
Amaranth
targets
the field-programmable-gate-array design space
that
open-source tooling
principally addresses,
and
it has become
the default choice
for
hobbyist and open-source
FPGA projects
in
the twenty twenties.

**MyHDL.**
MyHDL
was
developed
by
Jan Decaluwe
beginning
in
two thousand three.
MyHDL predates
the broader embedded-DSL revival
and
uses Python
for
hardware description
before
Migen and Amaranth
made
that approach
widespread.
MyHDL
converts
its Python descriptions
to
Verilog or VHDL
for
synthesis,
which
allows
the language
to
inter-operate
with
industrial toolchains
without
requiring
the toolchains
to
support Python natively.

**Clash.**
Clash
was
developed
by
Christian Baaij
at
Utrecht University
and later
Delft University of Technology
across
the twenty tens.
Clash
embeds
hardware description
in
Haskell.
The language
uses Haskell's type system
and
functional-programming idioms
to describe
combinational and sequential circuits,
and
compiles
its Haskell descriptions
to
VHDL, Verilog, or SystemVerilog
for
industrial synthesis flows.

**Chisel-adjacent and Chisel-successor languages.**
Several languages
in the twenty tens
extended
or
succeeded
Chisel's design pattern.
FIRRTL,
the Flexible Intermediate Representation for RTL,
provides
a
common target
that
several front-end languages
compile to
before
subsequent
synthesis-tool
consumption.
Diplomacy,
a
Chisel library,
provides
compositional interconnect design
that
supports
system-on-chip integration
at
the source-language level.
These are
not
independent
hardware description languages
in the historical sense
but
component technologies
in
the broader Chisel design ecosystem.

The embedded-DSL revival
has changed
the shape
of
hardware description
in
academic and open-source contexts
but
has not
displaced
Verilog and VHDL
in
industrial mainstream flows.
The two traditions
now
coexist,
with
industrial designers
using
SystemVerilog
for
production design work
and
open-source projects
using
Amaranth or Chisel
for
academic and hobbyist work.

## The Verification Language Track

Alongside
the main hardware description language lineage,
a
parallel track
of
verification-specific languages
developed
across
the standardisation era.
Verification languages
describe
properties
that
a design
must satisfy,
rather than
describing
the design itself.

**Property Specification Language, PSL.**
PSL
was
developed
by
Accellera
and
standardised
as
IEEE 1850
in
two thousand five.
The language
derives from
IBM's Sugar
property specification language
of
the late nineteen nineties
and
provides
a
compact temporal-logic syntax
that
formal verification tools
can consume
for
model checking
and
theorem proving.

**SystemVerilog Assertions, SVA.**
SVA
provides
a
temporal-assertion syntax
inside
SystemVerilog
that
allows
designers
to
embed
formal properties
directly
in
their design source.
SVA
has largely
displaced
PSL
in
industrial adoption
because
SystemVerilog
was
already
the dominant design language
when
both
were standardised.

**Universal Verification Methodology, UVM.**
UVM
provides
a
verification testbench methodology
built
on
SystemVerilog's
object-oriented features.
It is
not
a language
in
the strict sense,
but
a
reusable class library
that
Accellera
standardised
in
two thousand ten
and
IEEE
adopted
as
IEEE 1800.2
in
two thousand seventeen.
UVM
has become
the industrial standard
for
verification-heavy design flows.

## The High-Level Synthesis Track

A
separate track
of
higher-level synthesis
attempted
to
raise
the abstraction level
above
the register-transfer level
that
Verilog and VHDL
principally target.
High-level synthesis
tools
consume
a
sequential specification
and
generate
a
pipelined hardware implementation
that
implements
the same functionality.

**Behavioral Verilog and Behavioral VHDL.**
Both Verilog and VHDL
support
a
behavioural subset
that
higher-level synthesis tools
can consume.
Synopsys and Cadence
provided
behavioural synthesis
tools
across
the nineteen nineties and two thousands,
though
adoption
remained
limited
because
the resulting circuits
were
often
inefficient
compared to
hand-designed
register-transfer-level
implementations.

**SystemC HLS.**
SystemC
was
developed
in part
as
a target
for
high-level synthesis.
The Vivado HLS
tool
from Xilinx
and
the Catapult HLS
tool
from Siemens
both
consume
SystemC or
C-plus-plus source
and
generate
synthesisable
register-transfer-level output.
Industrial adoption
of
these tools
grew
across
the twenty tens
but
did not
match
the adoption
of
register-transfer-level design
in
Verilog and VHDL.

**Modern high-level synthesis alternatives.**
Recent
high-level synthesis efforts
have
targeted
domain-specific accelerator design,
where
the design space
is
narrow enough
that
the tool
can produce
efficient hardware
without
manual tuning.
Cornell's
Dahlia
and
similar
academic projects
demonstrate
the approach
for
deep-learning accelerator design
and
scientific-computing workloads.

## What Made Each Wave Necessary

The design-complexity forcing function
that
this article opened with
returns
as
the organising explanation
for
the historical sequence.
Each wave
of
hardware description languages
appeared
in response to
a
abstraction gap
that
prior languages
did not
close.

The academic prototypes
appeared
because
gate-level netlists
did not
scale
past
the medium-scale-integration boundary.
The standardisation era
appeared
because
the academic prototypes
did not
have
sufficient tooling
and
industrial commitment
to
support
production design flows.
The embedded-DSL revival
appeared
because
Verilog and VHDL
did not
have
adequate
generator-based
design support
or
integration with
modern software-engineering workflows.

The pattern
repeats
because
Moore's Law
continued to
raise
the transistor count per chip
across
each decade
of
this history,
and
each wave
addressed
the abstraction gap
that
the prior wave
had left open
at
the new scale.
The pattern
appears
to be
continuing
into
the current decade,
with
domain-specific accelerator design
now
occupying
the abstraction gap
that
general-purpose hardware description
does not
efficiently close.

## Where the Space Is Going

Several developments
in
the twenty twenties
appear
to be
shaping
the next wave
of
hardware description.

**Formal-methods integration.**
The formal verification community
has
increasingly
adopted
hardware description languages
as
their target,
with
Coq-based
and
Isabelle-based
hardware specification work
producing
verified implementations
of
processor cores
and
accelerator designs.
The Kami framework
and
its successors
represent
this line
of work.

**Machine-learning-driven design.**
Large language models
have begun
to
generate
Verilog and VHDL
from
natural-language specifications.
The quality
of
generated designs
remains
mixed
as of
the early twenty twenties,
but
the trajectory
suggests
that
hardware description
may become
a compilation target
for
higher-level intent specifications
rather than
a
directly-authored
source language.

**Open-source
industrial tooling.**
Yosys,
the open-source synthesis toolchain,
has
matured
sufficiently
to
support
production design flows
for
some
field-programmable-gate-array applications.
The combination
of
Yosys
with
Amaranth or Chisel
provides
a
fully open-source
hardware design toolchain
that
has attracted
academic and hobbyist adoption
and
is beginning
to
find
industrial applications
in
niche domains.

**Domain-specific hardware description.**
Recent
academic work
has produced
domain-specific hardware description languages
for
deep-learning accelerator design,
digital signal processing,
and
scientific computing.
These languages
narrow
the design space
enough
to
enable
substantially higher-level
description
than
Verilog and VHDL
can
efficiently support,
at
the cost of
generality.

## Conclusion

Hardware description languages
have followed
a
recognisable trajectory
across
five decades.
Academic prototypes
in
the seventies
established
the register-transfer-level abstraction
and
the event-driven simulation model.
Verilog and VHDL
in
the eighties
supplied
the industrial tooling
that
the academic prototypes
could not
match.
SystemVerilog and SystemC
in
the two thousands
extended
the standardisation-era languages
with
verification and system-level modelling.
The embedded-DSL revival
of
the twenty tens
introduced
generator-based design
and
integration with
modern software-engineering workflows
through
Chisel,
Amaranth,
SpinalHDL,
Clash,
and
related languages.
Verification-specific languages
developed
alongside
the main lineage
across
the standardisation era.
High-level synthesis efforts
attempted
to
raise
the abstraction level
above
the register-transfer level
with
mixed
industrial success.

The forcing function
throughout
this history
has been
the growth
in
transistor count per chip
that
Moore's Law
sustained
across
five decades.
Each successive wave
of
hardware description languages
appeared
in response to
the abstraction gap
that
the prior wave
left open
at
the new scale
of
integration.
The pattern
appears
to be
continuing
into
the current decade,
with
domain-specific accelerator design,
formal-methods integration,
and
machine-learning-driven
design synthesis
shaping
the next wave.

The full historical record
of
hardware description languages
is
richer
than
this article
can compactly cover,
and
readers
who need
detail
on
languages
should consult
the primary sources
that
the reference list
below identifies.

## References

### Reference

- [Verilog language history and standardisation][ref_verilog]
- [VHDL language history and standardisation][ref_vhdl]
- [SystemVerilog language and IEEE 1800][ref_systemverilog]
- [SystemC transaction-level modelling][ref_systemc]
- [Bluespec SystemVerilog and guarded atomic actions][ref_bluespec]
- [Chisel hardware construction language][ref_chisel]
- [SpinalHDL language documentation][ref_spinalhdl]
- [Amaranth hardware description library][ref_amaranth]
- [MyHDL Python-based hardware description][ref_myhdl]
- [Clash Haskell-based hardware description][ref_clash]
- [Property Specification Language and IEEE 1850][ref_psl]
- [Universal Verification Methodology][ref_uvm]
- [High-level synthesis overview][ref_hls]
- [Yosys open-source synthesis toolchain][ref_yosys]

[ref_amaranth]: https://amaranth-lang.org/
[ref_bluespec]: https://en.wikipedia.org/wiki/Bluespec
[ref_chisel]: https://en.wikipedia.org/wiki/Chisel_(programming_language)
[ref_clash]: https://clash-lang.org/
[ref_hls]: https://en.wikipedia.org/wiki/High-level_synthesis
[ref_myhdl]: https://www.myhdl.org/
[ref_psl]: https://en.wikipedia.org/wiki/Property_Specification_Language
[ref_spinalhdl]: https://spinalhdl.github.io/SpinalDoc-RTD/
[ref_systemc]: https://en.wikipedia.org/wiki/SystemC
[ref_systemverilog]: https://en.wikipedia.org/wiki/SystemVerilog
[ref_uvm]: https://en.wikipedia.org/wiki/Universal_Verification_Methodology
[ref_verilog]: https://en.wikipedia.org/wiki/Verilog
[ref_vhdl]: https://en.wikipedia.org/wiki/VHDL
[ref_yosys]: https://yosyshq.net/yosys/
