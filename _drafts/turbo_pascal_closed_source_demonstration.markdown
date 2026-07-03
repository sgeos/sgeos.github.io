---
layout: post
mathjax: true
comments: true
title:  "Turbo Pascal, the Closed-Source Demonstration"
date:   2026-04-08 09:00:00 +0000
categories: compilers streaming series
---

<!-- A190 -->
<script>console.log("A190");</script>

Turbo Pascal
occupies an awkward position
in the historical record
of stream-based compilation.
The product
was commercially decisive.
Independent developers
who used Turbo Pascal
in nineteen eighty-four
report a productivity gain
of an order of magnitude
over the compilers
that preceded it
on the same hardware.
The productivity gain
was not incremental.
The claim
that the compile-link-run cycle
finished in seconds
rather than minutes
appears in
contemporary reviews,
in Hejlsberg's own recollections,
and in the folk memory
of that era of developers.
None of these sources
provide
the compiler source code.
The compiler
was proprietary
in nineteen eighty-three
and remains proprietary
today.

This article
treats Turbo Pascal
as evidence
for the stream-processor discipline
under a strict epistemic policy.
Claims about
the compiler's
external observable behaviour,
such as throughput,
memory footprint,
and shipped-binary size,
are treated as
reproducibly verifiable
from artefacts
that survive
in software archives.
Claims about
the compiler's
internal architecture
are treated as
secondary-source reports
that trace back
to Anders Hejlsberg's
oral history
at the [Computer History Museum][ref_hejlsberg]
and to a small number
of contemporary technical articles.
The distinction
matters because
external behaviour
can be reproduced today
by anyone who runs
the shipped binary
in an eight-oh-eight-eight emulator,
whereas
internal architecture
cannot be verified
independently.

## A Brief History

Anders Hejlsberg
developed the compiler
that became Turbo Pascal
at a small Danish company
named Poly Data.
The product
was originally called
Compas Pascal
and ran on
Zilog Z-eighty
processors under
the Control Program for Microcomputers.
Philippe Kahn,
Niels Jensen,
Ole Henriksen,
and Mogens Glad
founded Borland
in Scotts Valley, California
in nineteen eighty-three.
Borland acquired
the rights to Hejlsberg's compiler,
rebranded it Turbo Pascal,
and shipped
the first version
in November of nineteen eighty-three.
Hejlsberg
subsequently joined Borland
and became
the chief architect
of the Turbo Pascal product line.

Turbo Pascal one point zero
shipped for
three targets
in the first release.
The first target
was
Control Program for Microcomputers
running on the Zilog Z-eighty processor.
The second target
was
Control Program for Microcomputers eighty-six
running on the Intel eight-oh-eight-six.
The third target
was
Microsoft Disk Operating System
running on the Intel eight-oh-eight-eight
in the International Business Machines
Personal Computer.
The shipped list price
was
forty-nine United States dollars and ninety-five cents,
which undercut
the incumbent commercial compilers
by an order of magnitude.
The pricing decision
was decisive
for the product's rapid adoption.

Subsequent releases
extended the language
and the tooling
while retaining
the compile-link-run-in-memory
discipline
that defined the early versions.

- Turbo Pascal two point zero
  shipped in nineteen eighty-four
  with expanded numeric types
  and additional compile-time options.
- Turbo Pascal three point zero
  shipped in nineteen eighty-five
  with overlay support
  and eighty-eighty-seven floating-point-coprocessor support
  in a separate variant.
- Turbo Pascal four point zero
  shipped in nineteen eighty-seven.
  The four point zero release
  moved from
  the single-segment in-memory model
  to a units-based model
  with separate compilation
  along the lines
  of Modula-2's
  definition-implementation split.
  This transition
  marks the end
  of the strictly single-segment
  Turbo Pascal era
  and the beginning
  of the multi-module era.
- Turbo Pascal five point zero
  shipped in nineteen eighty-eight
  with an integrated debugger.
- Turbo Pascal five point five
  shipped in nineteen eighty-nine
  and introduced Object Pascal.
- Turbo Pascal seven point zero
  shipped in nineteen ninety-two
  and was
  the last Turbo-branded version.

The Turbo Pascal versions
that most cleanly demonstrate
the stream-processor discipline
are one point zero
through three point zero.
These versions
fit the entire product,
including the source editor,
the compiler,
the linker,
and the runtime library,
inside a single
sixty-four-kilobyte segment.
The integrated debugger
did not arrive
until Turbo Pascal five point zero
in nineteen eighty-eight,
which is one of the reasons
that version five
falls outside
the single-segment window.
Version four point zero
and later
relax the single-segment constraint
in exchange for
richer tooling
and separate compilation.
The rest of this article
concentrates on
versions one point zero
through three point zero
because they carry
the load-bearing evidence
for the stream-processor claim.

## What Can Be Verified from the Shipped Binary

Copies of the Turbo Pascal
one through three
distribution disks
survive in
software archives.
Borland released
Turbo Pascal one point zero,
three point zero two,
five point five,
and seven point zero one
as antique-freeware downloads
in twenty hundred,
and these downloads
remain accessible
through the community-maintained
Turbo Pascal preservation sites.
The shipped binaries
can be run today
in eight-oh-eight-eight emulators
and their behaviour observed.

Several claims
about Turbo Pascal
can be verified
from the shipped binary alone,
without any inspection
of source code
or dependence on
secondary reporting.

**Binary size.**
The Turbo Pascal three point zero
distribution
occupied approximately
thirty-nine kilobytes
in the main executable file
and roughly one hundred kilobytes total
including the runtime library
and the sample programs.
This can be observed
directly by listing
the distribution disk.
Modern compilers
are typically
several orders of magnitude larger.
For comparison,
the GNU Compiler Collection
front-end executable
alone exceeds
several tens of megabytes
in stripped binary form.
Expressed as a ratio,

$$
\frac{S_{\text{modern compiler}}}{S_{\text{TP 3.0 executable}}}
\sim \frac{5 \times 10^{7} \text{ bytes}}{3.9 \times 10^{4} \text{ bytes}}
\sim 10^{3},
$$

which is a three-order-of-magnitude size gap.
The gap
is a rough guide,
not a precise benchmark,
because
the two products
solve
substantially different problems
at substantially different levels of ambition.
The point
is that
the Turbo Pascal binary
belongs to
a size regime
that modern compilers
have long since departed.

**Memory footprint at run time.**
Running Turbo Pascal three
under a period-appropriate
Microsoft Disk Operating System configuration
occupies
under sixty-four kilobytes
of conventional memory
for the resident compiler,
editor,
and runtime.
This figure
can be observed
by inspecting the operating system's
memory-usage report
after Turbo Pascal
is loaded.

**Compile-link-run turnaround.**
The compile-link-run cycle,
measured wall-clock
in an emulator
configured for
a four-point-seven-seven megahertz
eight-oh-eight-eight,
completes in
under one second
for a program
of several hundred lines.
Larger programs
scale approximately linearly.
This is
a reproducible measurement
that anyone
can perform today.

**Absence of intermediate files.**
The default
build mode
in Turbo Pascal
one through three
produces no
intermediate files
on disk.
The compiler
reads the source,
produces an executable image
in memory,
and either runs it
or writes it
to disk
as a single
Microsoft Disk Operating System
executable file.
The absence
of intermediate files
is observable
by directory listing
before and after
a compilation.

These four
observations
are load-bearing
for the discipline claim.
They establish
that Turbo Pascal
produces
executable output
from source input
in one forward pass
without materialising
an intermediate representation
that persists
across pass boundaries.
The observations
do not require
any inspection
of the compiler's
internal state
during compilation.

## What Is Reported from Secondary Sources

Claims about
the compiler's
internal architecture,
its data structures,
and its algorithmic choices
depend on
secondary sources.
The two
most substantial
secondary sources
are Hejlsberg's oral history
recorded at the
[Computer History Museum][ref_hejlsberg]
and a small collection
of contemporary technical articles
in *Byte* magazine,
*Dr. Dobb's Journal*,
and the Borland
technical notes archive.
These sources
are consistent
with one another
but derive
from the same
authorial voice
and cannot be
independently corroborated
against the source code.

The reported
architectural claims,
each of which
carries a
secondary-source flag,
are as follows.

**No abstract syntax tree.**
The compiler
does not construct
an abstract syntax tree.
Each syntactic construct
recognised by the parser
emits its target machine code
at the point of recognition.
This is
the integrated single-pass
architecture
described in article A189
for the Wirth line.
Turbo Pascal
followed the same architecture
independently.
The compiler
holds no
whole-program representation
of the source
at any point
during compilation.

**Assembly-language implementation.**
The compiler
was written
in eight-oh-eight-six assembly language,
by Hejlsberg,
for the Intel target variants.
The Zilog Z-eighty variant
was written
in Z-eighty assembly language.
The assembly-language implementation
choice
enabled
the small binary size
and the direct control
over memory layout
that the single-segment constraint required.
A higher-level implementation language
would have imposed
runtime overhead
that the design budget
did not admit.

**Recursive-descent parser
with direct emission.**
The parser
is a hand-written
recursive-descent parser
in the Wirth idiom.
Each grammar production
corresponds to
a parser procedure.
Code emission
happens inside
the parser procedures
at the syntactic point
where the emitted instruction
is determined.
Forward jumps
are resolved
through a small
fixup buffer
that is
patched
when the target address
becomes known.

**Symbol table
in a single segment.**
The symbol table
lives in
the same
sixty-four-kilobyte segment
as the compiler code
and the emitted output buffer.
The symbol table
is scoped
and popped
on scope exit.
The compiler
does not carry
identifiers
outside their scope
into subsequent compilation.
The single-segment budget
places
a hard cap
on
the accumulating top-level environment
that
tracks
signatures of
declarations already parsed.
Because
the top-level environment
grows monotonically
with
the top-level declaration count,
the segment cap
translates
directly into
a program-size limit.
This is
one of
the honest reasons
that
early Turbo Pascal programs
were structured
into
short units
with
few
top-level declarations
per unit
even before
the version-four-point-zero
multi-module release
made
separate compilation
explicit.

These claims
are internally consistent
with the observable
external behaviour.
They also
match
the Wirth-line
architectural pattern
described in article A189.
The claims
are not
independently verifiable
against the source code
because the source code
is not public.
A determined reverse engineer
with access to
an eight-oh-eight-eight
disassembler
could verify or refute
the internal-architecture claims
from the shipped binary,
but no
publicly documented
reverse-engineering project
has been carried out
to the standard
that would establish
the claims
as verified.
The internal-architecture claims
therefore
should be treated
as
consistent with the evidence
but not
formally verified.

## The Throughput Argument

The most frequently cited
Turbo Pascal number
is the throughput
on a four-point-seven-seven megahertz
Intel eight-oh-eight-eight processor.
Hejlsberg's own reports
give figures
between
ten thousand
and thirty thousand
lines per second.
Contemporary reviews
in *Byte* magazine
report similar numbers.
The specific number
depends on
the program characteristics
and on
whether
the reported figure
is a peak
or an average.

Working from the reported figures,
the cycle budget
per source line
was between

$$
\frac{4.77 \times 10^{6} \text{ cycles/second}}
     {1.0 \times 10^{4} \text{ lines/second}}
= 477 \text{ cycles/line}
$$

at the low end
and

$$
\frac{4.77 \times 10^{6} \text{ cycles/second}}
     {3.0 \times 10^{4} \text{ lines/second}}
\approx 159 \text{ cycles/line}
$$

at the high end.
The order-of-magnitude
result
holds across the range.

The cycle budget
translates directly
into a memory-write budget
per source line.
A sixteen-bit memory-write instruction
on the eight-oh-eight-eight,
including the effective-address computation
and the additional bus cycles
that the eight-bit external bus imposes,
costs on the order of
fifteen to twenty cycles
for typical addressing modes.
The number of memory writes
that fit in
one line's compilation budget
at the high-throughput end
is therefore

$$
W_{\text{per line}}
\le \frac{C_{\text{per line}}}{C_{\text{per write}}}
\approx \frac{159 \text{ cycles}}{17 \text{ cycles/write}}
\approx 9 \text{ writes/line}.
$$

Constructing an abstract-syntax-tree node
for a typical expression
requires several memory writes
for the node itself
plus additional writes
for parent, child, and sibling pointers.
Under a nine-write-per-line budget,
even a single AST node per line
saturates the write budget
before any semantic-analysis work occurs.
At the low-throughput end
the budget rises
to on the order of thirty writes per line,
which admits
some tree construction
but still forecloses
whole-program tree materialisation.
A compiler
that finishes a source line
in fewer than
five hundred cycles
on an eight-oh-eight-eight
therefore
cannot afford
per-line operations
that require
substantial dynamic-memory allocation,
tree-node construction,
or multi-pass traversal.
The observed throughput
therefore constrains
the architecture
even without
any inspection
of the compiler's
internal design.

The address-space cap
provides
a second architectural constraint.
The compiler segment
is sixty-four kilobytes,
or

$$
S_{\text{segment}} = 2^{16} \text{ bytes} = 65536 \text{ bytes}.
$$

A typical
abstract-syntax-tree node
for an expression
consumes
between eight
and thirty-two bytes,
depending on
implementation choices.
Denote by
$S_{\text{code}}$
the compiler code size,
$S_{\text{output}}$
the emitted-output buffer,
$S_{\text{symtab}}$
the symbol-table budget,
and
$S_{\text{node}}$
the average AST-node size.
The maximum
number of AST nodes
that fit in
the shared segment
is bounded by

$$
N_{\text{AST}}
\le \frac{S_{\text{segment}} - S_{\text{code}} - S_{\text{output}} - S_{\text{symtab}}}
        {S_{\text{node}}}.
$$

Substituting
order-of-magnitude estimates
for a Turbo Pascal
one-through-three-vintage build,

$$
N_{\text{AST}}
\le \frac{65536 - 25000 - 8000 - 4000}{16}
\approx 1800 \text{ nodes}.
$$

The specific numerator terms
are estimates
consistent with
the observed binary size
and with
the reported
runtime memory footprint.
Even under
generous relaxations
of these estimates,
the node cap
remains
below several thousand.
This is
insufficient for
the abstract syntax tree
of a program
of even
a few hundred lines,
which would require
tens of thousands
of nodes
under conventional
tree representations.
The address-space cap
therefore rules out
whole-program-abstract-syntax-tree
compilation
for the shared-segment
Turbo Pascal versions
on architectural grounds
independent of
throughput.

The two constraints,
throughput
and address space,
converge on
the same conclusion.
The compiler
must be
an integrated single-pass compiler
in the Wirth idiom,
because no other architecture
can meet
both constraints
simultaneously.
The observable evidence
therefore corroborates
the secondary-source
architectural claims
by architectural necessity
even absent
the source code.

## The Hejlsberg Line

Hejlsberg's subsequent work
carried forward
several themes
from the Turbo Pascal era
into commercial products
that shaped
software development
in the nineteen nineties and beyond.

**Delphi.**
After Turbo Pascal
matured
into an
object-oriented language
in version five point five,
Hejlsberg led
the Delphi project at Borland,
which paired
Object Pascal
with a visual
graphical user interface builder.
Delphi
inherited
the compilation-speed emphasis
of Turbo Pascal.
Delphi programs
compiled
substantially faster
than equivalent
Visual C-plus-plus programs
on the same hardware
throughout the nineteen nineties.

**C-sharp and dot-NET.**
Hejlsberg
left Borland
for Microsoft
in nineteen ninety-six
and became
the chief architect
of the C-sharp language,
which shipped
as part of
the dot-NET platform
in twenty hundred two.
The dot-NET runtime itself
was the work
of a broader team
that included Hejlsberg
among many others.
C-sharp
retains
the strong-static-typing tradition
of Pascal and Modula-2
but adopts
a syntax
influenced by
C and Java.
The early C-sharp compiler,
written in C-plus-plus,
prioritised
compilation speed
in a way that
echoed the Turbo Pascal emphasis
even though
the subsequent
Roslyn rewrite
adopted
a much richer
multi-pass architecture
in support of
language-service scenarios.

**TypeScript.**
Hejlsberg
became
the lead architect
of TypeScript
in the twenty tens.
The TypeScript compiler
is a
much more complex
multi-pass system
than Turbo Pascal,
reflecting
the demands of
bidirectional and contextual
type inference
over
a structural type system,
which
TypeScript's
type system requires.
Even so,
TypeScript
retains
the compilation-speed emphasis
that defined
Hejlsberg's earlier work.
The TypeScript language server
maintains
incremental compilation state
that permits
sub-second turnaround
on edit-time typechecking
for programs
of hundreds of thousands of lines.

The through-line
across Hejlsberg's career
is not the specific
compilation architecture,
which necessarily evolved
as the language complexity
required.
The through-line
is the treatment of
compilation speed
as a first-class
product requirement,
not as
an incidental engineering concern.
This treatment
originated
in the sixty-four-kilobyte segment
of Turbo Pascal one point zero
and persists
in the incremental typechecker
of TypeScript
four decades later.

## Where Turbo Pascal Sits in the Discipline

The two-axis
design space
introduced in article A188
places
Turbo Pascal
in the same quadrant
as the Wirth line,
namely
integrated single-pass
and abstract-syntax-tree-free.
The compiler
runs the entire pipeline
inside
a hand-written
recursive-descent parser.
No token stream
persists
between the lexer
and the parser,
because the lexer
is a method
on the parser
that returns
the next token
on demand.
No abstract syntax tree
persists,
because each parsed construct
emits its output
immediately.

Turbo Pascal
differs from
the Oberon compiler
in its target
and its authorship model.
Oberon targets
a research operating system
under continuous ETH stewardship
with open source
and detailed academic documentation.
Turbo Pascal targets
personal computing
under commercial closed-source stewardship
with sparse
architectural documentation.
The two products
converged
on the same architecture
because the design constraints
were the same.

Turbo Pascal
also differs from
the Oberon compiler
in the choice of
implementation language.
Oberon's compiler
is written
in Oberon,
which is a
self-hosted arrangement
that permits
academic verification
of every architectural claim
against the published source.
Turbo Pascal's compiler
is written in
assembly language,
which forecloses
academic verification
in the same sense.
The choice of
implementation language
is a downstream consequence
of the size budget.
An assembly-language implementation
fits inside
a sixty-four-kilobyte segment.
A high-level-language implementation
of the same functionality
would not.

## Legacy

The commercial impact
of Turbo Pascal
is well documented.
The product
sold
more than one million copies
by nineteen eighty-seven,
which was
an unprecedented number
for a development tool.
Turbo Pascal
established
the personal-computer
software-development market
as a mass market
rather than
a specialist market.
The product
made professional-grade
compilation
available to
anyone
with a personal computer
and forty-nine dollars.

The architectural legacy
is subtler
and requires
explicit attention
to survive.
The Wirth-line
academic tradition
preserved
the single-pass discipline
through publication
and pedagogy.
The Turbo Pascal
commercial tradition
preserved
the single-pass discipline
through
market success,
but the market success
faded
as the personal-computing platform
matured
and as
production compilers
migrated
to the multi-pass
optimising architecture
of GNU Compiler Collection
and Clang.
The Turbo Pascal
architecture
survives in
academic memory
and in
the folk memory
of developers
who used the product,
but not
in
a public technical record
comparable to
the *Project Oberon*
source listing.

The absence
of a
comparable technical record
is what makes
Turbo Pascal
the closed-source demonstration.
The evidence
that the discipline works
at commercial scale
is real.
The evidence
of exactly how the discipline
was realised
in one specific commercially successful product
is
formally unavailable.
Present-day compiler engineers
who want to
learn
the stream-processor discipline
have
Wirth's [*Project Oberon*][book_wirth_project_oberon]
and [*Compiler Construction*][book_wirth_compiler_construction]
as their primary references.
They do not have
the Turbo Pascal source code.
This series
takes the position
that the Wirth references
are sufficient
for teaching purposes
and that
the Turbo Pascal evidence
matters
for its
historical demonstration
that the discipline
scales
commercially.

## Conclusion

Turbo Pascal
is
the commercial demonstration
that the stream-processor
compilation discipline
scaled
past
the academic setting
to
mass-market personal computing.
The compiler's
external behaviour,
observable today
in eight-oh-eight-eight emulators
running preserved binaries,
supports
the architectural claim
by two independent arguments,
the throughput constraint
and the address-space constraint,
both of which
rule out
whole-program-abstract-syntax-tree
compilation
on architectural grounds
without reference to
the source code.
The internal architecture
that
secondary sources report
is consistent with
this external evidence
but is not
independently verifiable.
The Hejlsberg-authored line
of subsequent products,
including Delphi,
C-sharp,
and TypeScript,
carries forward
the compilation-speed emphasis
even where
the specific architecture
necessarily evolved.
Article A191
treats
Per Brinch Hansen's
pipeline-of-processes compilers
as the third of the three
foundational demonstrations
in this series.

## References

### Book

- [*Compiler Construction*][book_wirth_compiler_construction], Niklaus Wirth, Addison-Wesley, 1996
- [*Project Oberon, The Design of an Operating System and Compiler*][book_wirth_project_oberon], Niklaus Wirth and Jürg Gutknecht, revised edition 2013

[book_wirth_compiler_construction]: https://en.wikipedia.org/wiki/Compiler_Construction_(Wirth_book)
[book_wirth_project_oberon]: https://people.inf.ethz.ch/wirth/ProjectOberon/

### Reference

- [Anders Hejlsberg biographical entry, which cites the Computer History Museum oral history][ref_hejlsberg]
- [Borland software company entry][ref_borland]
- [C-sharp programming language][ref_csharp]
- [Delphi integrated development environment][ref_delphi]
- [Intel eight-oh-eight-eight processor entry][ref_8088]
- [Object Pascal language entry][ref_object_pascal]
- [Turbo Pascal history and technical details][ref_turbo_pascal]
- [TypeScript programming language][ref_typescript]

[ref_hejlsberg]: https://en.wikipedia.org/wiki/Anders_Hejlsberg
[ref_borland]: https://en.wikipedia.org/wiki/Borland
[ref_csharp]: https://en.wikipedia.org/wiki/C_Sharp_(programming_language)
[ref_delphi]: https://en.wikipedia.org/wiki/Delphi_(software)
[ref_8088]: https://en.wikipedia.org/wiki/Intel_8088
[ref_object_pascal]: https://en.wikipedia.org/wiki/Object_Pascal
[ref_turbo_pascal]: https://en.wikipedia.org/wiki/Turbo_Pascal
[ref_typescript]: https://en.wikipedia.org/wiki/TypeScript

### Related Post

- [Compilation as a Streaming Discipline][related_post_streaming_discipline], article A188 in this series
- [Wirth's Single-Pass Line, PL/0 through Oberon][related_post_wirth], article A189 in this series

[related_post_streaming_discipline]: {% post_url 2026-04-06-compilation_as_streaming_discipline %}
[related_post_wirth]: {% post_url 2026-04-07-wirth_single_pass_line %}
