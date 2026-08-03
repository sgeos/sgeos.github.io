---
layout: post
mathjax: true
comments: true
title:  "The Stream Processor as Compiler and the Compiler as Stream Processor"
date:   2026-04-17 09:00:00 +0000
categories: compilers streaming series
series: streaming_compilers
series_title: Streaming Compilers
series_index: 12
---
<!-- A199 -->
<script>console.log("A199");</script>

The eleven preceding articles
of this series
argued
that
compilation
can be
organised
as
a stream-processor operation.
The historical trio
in
articles A189 through A191
identified
the three
foundational demonstrations
of the discipline
in
Niklaus Wirth's
languages,
Anders Hejlsberg's
Turbo Pascal,
and
Per Brinch Hansen's
pipeline architecture.
The theory pair
in
articles A192 and A193
developed
the mathematical foundation
in
block-structured control flow
and
coalgebraic productivity.
The techniques trio
in
articles A194 through A196
covered
the three
foundational engineering techniques
of
fixup tables,
declare-before-use,
and
scoped symbol tables.
The synthesis pair
in
articles A197 and A198
compared
the integrated
and decomposed shapes
and identified
where
the discipline breaks down.

This closing article
draws the analogy
in both directions.
A compiler
that reads its source in a stream
is a stream processor.
A stream processor
that compiles its own source
is a self-hosted stream processor.
The two claims
are duals of one another.
The article closes
with Keleusma's compilation pipeline
as the modern worked example,
where the compiler
is a stream processor
in both directions.

## The Compiler as Stream Processor

The first direction
of the analogy
takes
the compiler
as
its subject.
A compiler
$C$
maps
source programs
to
target programs

$$
C \colon \text{source} \to \text{target}.
$$

The stream-processor form
of the compiler
reads
the source
as
a stream
of tokens or bytes
and
produces
the target
as
a stream
of instructions
or bytecode
in
a forward sweep

$$
C_{\text{stream}} \colon A^{\omega} \to B^{\omega},
$$

where
$A$
is
the source alphabet
and
$B$
is
the target instruction alphabet.
Article A193
formalised
the productivity condition
that
$C_{\text{stream}}$
must satisfy.
A productive
stream-processor compiler
delivers
some finite prefix
of the target
after
consuming
some finite prefix
of the source,
with
the productivity function
$m$
specifying
how much output
each input prefix determines.

The compiler-as-stream-processor
framing
is
the perspective
that
articles A189 through A196
developed
in detail.
The Wirth line
demonstrated
the integrated form
of this framing.
Brinch Hansen
demonstrated
the decomposed form.
The theory pair
identified
the syntactic and semantic
conditions
under which
the framing
holds.
The techniques trio
identified
the engineering mechanisms
that
implement
the framing
in practice.

## The Stream Processor as Compiler

The second direction
of the analogy
takes
the stream processor
as its subject.
A stream processor
$P$
is
a program
that consumes
one or more input streams
and produces
one or more output streams
under
the productivity discipline.
The stream processor
does not
inherently
compile anything.
It processes
values.

The question
that
this direction
poses
is
what does it mean
for
a stream processor
to compile
its own source?

The answer
is
that
a stream processor
whose source
is
itself
a stream-processor program
in
the same language
can be
compiled
by
another stream processor
of the same shape.
When
the compiling stream processor
and
the compiled stream processor
are
the same program
running
on
the same virtual machine,
the arrangement
is
self-hosting.

The self-hosted
stream-processor compiler
$P_{\text{self}}$
satisfies

$$
P_{\text{self}}(\text{source}(P_{\text{self}})) = P_{\text{self}},
$$

where
$\text{source}(P_{\text{self}})$
denotes
the source form
of $P_{\text{self}}$
and
$P_{\text{self}}$
denotes
the compiled form.
This is
the fixed-point condition
that self-hosting
imposes.
A compiler
that compiles
itself
and produces
its own
compiled form
as the result
has reached
the fixed point.

The fixed-point condition
is
non-trivial
to achieve
in practice
because
the compiler's
source
must
express
a program
whose
compilation
produces
exactly
the compiler's
current
compiled form.
The bootstrap process
that reaches
this fixed point
is
documented
in
the Wirth Oberon
compiler literature
and
in
the LLVM,
Rust,
and Go
self-hosting histories.

## The Duality Made Precise

The two directions
of the analogy
are
duals in
a specific
technical sense.
A compiler
as
a stream processor
maps
source alphabets
to target alphabets
under
the productivity discipline

$$
C_{\text{stream}} \colon A^{\omega}_{\text{source}} \to B^{\omega}_{\text{target}}.
$$

A stream processor
as
a compilable program
supplies
the source
that
compilation transforms
to
executable form

$$
P \colon \text{state} \to \text{state},
\qquad
\text{source}(P) \in A^{\omega}_{\text{source}}.
$$

When
the two
coincide,
namely when
$C = P$
and
the source alphabet
is
the alphabet
of
the compiler's own source language,
the arrangement
is
self-hosted.
The commutative diagram
that
this coincidence
implies
places
compilation
on
both sides of
the arrow
in
the coalgebraic setting
of article A193.

The mathematical content
of
the duality
is
that
compilation
respects
the productivity structure
in both directions.
The source-to-target
direction
is productive
by
the streaming discipline
of the compiler.
The compiler-source-to-compiler-behaviour
direction
is productive
by
the productivity guarantee
that
the source language
supplies
for any program
written in it,
including
the compiler itself.

## Self-Hosting as the Endpoint

Self-hosting
is
the demonstration
that
the discipline
scales
to
the compiler's own complexity.
A stream-processor language
that
cannot express
its own
compiler
in
the streaming discipline
fails to
demonstrate
that
the discipline
is
sufficient
for
programs
of
practical complexity.
A stream-processor language
that
can express
its own
compiler
in
the discipline
demonstrates
that
the discipline
is
sufficient
for
the most demanding
program
that
the language
must
support,
namely
its own toolchain.

One
demonstrated self-hosting arrangement
and one
in-progress target
appear
in the historical record
of the streaming discipline.
Wirth's Oberon
demonstrated
the integrated shape
under
the Wirth language line's
strict declare-before-use discipline
and closed
the self-hosting endpoint.
Keleusma's V0.3.0 roadmap
targets
the decomposed shape
under
a coroutine-based discipline
whose self-hosting endpoint
remains
in progress
at the time of writing.
Brinch Hansen's SuperPascal
provided
the language runtime
in which
the pipeline-of-processes shape
could be
expressed directly.
The SuperPascal compiler itself
was implemented
in standard sequential Pascal
rather than in SuperPascal,
per the published record.
The Brinch Hansen tradition
therefore
did not
close the self-hosting endpoint
even though
the language design
supported it.
The Rust compiler
demonstrated
the multi-pass
whole-program-optimising shape
under
a
fundamentally different set of
architectural choices,
which
places Rust
outside
the streaming discipline's boundary
per
the analysis
of article A198.

The self-hosting
demonstrations
inside
the streaming discipline
share
one specific structural property.
The compiler,
written
in its own source language,
is
a program
whose
runtime behaviour
respects
the discipline's
productivity condition.
The compiler
produces
target bytecode
incrementally
as
it consumes source.
The compiler
holds
bounded working memory
regardless of
the source
being compiled.
The compiler
completes
in
time
linear
in
the source size.

These properties
are
non-trivial
to preserve
when
the compiled program
happens to be
the compiler itself,
because
the compiler
is
a complex program
whose
memory footprint
and
computational complexity
must
fit
within
the discipline's
constraints.
The Wirth line's Oberon compiler,
approximately four thousand lines
in
Oberon source,
demonstrates
that
the constraint
is
achievable.
The Brinch Hansen SuperPascal language
provides
a runtime
in which
the decomposed shape
can be
expressed directly.
The SuperPascal compiler itself
was implemented
in standard sequential Pascal
rather than in SuperPascal.
The Brinch Hansen tradition
established the pipeline architecture
without closing
the self-hosting endpoint.

## Keleusma's Compilation Pipeline

Keleusma's compilation pipeline
provides
a modern
worked example
of
the discipline
at
substantial engineering ambition.
The pipeline
is
currently
implemented
in Rust
as
the production
compiler
and
is planned
to
be
self-hosted
in the V0.3.0
milestone
as
a Keleusma-in-Keleusma
compiler.
The
Keleusma-in-Rust
pipeline
provides
the demonstration
that
the discipline
scales
to
a
typed,
resource-bounded,
coroutine-based
scripting language
whose
target contexts
include
embedded audio,
game engines,
and
high-assurance
embedded control.

The Keleusma pipeline
consists of
five stages
running
in sequence
as
a compile-time pipeline
followed by
a runtime pipeline
that
respects
the streaming discipline
during execution.
The five-stage decomposition
describes
the current Rust-hosted
production compiler.
Article A197 describes
the same pipeline
under
a three-stage
coroutine projection
in which
the middle three stages
are merged
into
a single Keleusma `loop` function.
The two descriptions
are
the same pipeline
at different levels of granularity.

**Stage one, tokenise.**
The source bytes
are consumed
by
the lexer,
which yields
tokens
one at a time.
The lexer
holds
a small character buffer
sufficient
to recognise
a single token
plus
a source-position tracker.
Its working memory
is
constant in
the source size.

**Stage two, parse.**
The token stream
is consumed
by
the parser,
which yields
declarations
one at a time.
The parser
holds
a bounded parse stack
whose depth
equals
the current syntactic nesting depth
of the source cursor,
plus
a fixup buffer
for
the currently parsed declaration.

**Stage three, typecheck.**
Each parsed declaration
is
consumed
by
the type checker,
which
runs
Hindley-Milner-style unification
over
the per-declaration constraint graph
and yields
a
typed declaration.
The constraint graph
is
held in
arena memory
whose size
is bounded by
the declaration's
complexity,
not by
the total program size.
This
is
the
per-declaration non-streaming stage
identified
in article A198
as
the escape hatch
that
allows
Hindley-Milner inference
inside
a streaming pipeline.

**Stage four, monomorphise.**
Each typed declaration
is
consumed
by
the monomorphiser,
which
generates
specialised versions
of
generic declarations
for
each concrete instantiation
that
the source
requests.
The monomorphiser
maintains
a
per-specialisation table
that
tracks
which
specialisations
have already been generated
across
the entire program.
The specialisation table
grows
with
the number of
distinct specialisations,
not with
the source size,
which
is
typically
a
small bound
in
practice.

**Stage five, hoist and emit chunks.**
Each monomorphised declaration
is
consumed
by
the closure-hoister
and
the chunk emitter.
Closure literals
are hoisted
to
top-level synthetic chunks.
Each chunk
emits
its bytecode
in
a final pass
that
patches
forward jumps
against
the block-local fixup table
that
article A194
formalised.
The output
is
a stream of
bytecode chunks
that
together
form
the compiled module.

The pipeline
respects
the streaming discipline
at
the compilation level.
Each stage
consumes
its input stream
and produces
its output stream
in
a productivity-preserving manner.
Formally,
the Keleusma compilation pipeline
is
the composition

$$
C_{\text{Keleusma}}
= \text{emit} \circ \text{monomorphise}
\circ \text{typecheck} \circ \text{parse} \circ \text{tokenise},
$$

which is
a stream processor
$C_{\text{Keleusma}} \colon A^{\omega}_{\text{source}} \to B^{\omega}_{\text{bytecode}}$
in
the sense of article A193.
The emit stage
performs
closure hoisting
before
chunk emission,
combining
what the Keleusma
implementation documents
as
two separate operations
into
a single logical stage
for
the purposes of
this composition.
The composition
inherits
per-stage productivity
by
the compositional productivity result
of the theory pair,
namely
that
a pipeline
of productive stages
is
itself
productive
with
composed productivity function
$m = m_5 \circ m_4 \circ m_3 \circ m_2 \circ m_1$
across
the five stages.

The pipeline's
total working memory
respects
the compositional bound
of
article A196,

$$
M_{\text{Keleusma}}
= \sum_{i=1}^{5} M_i + \sum_{i=1}^{4} b_i,
$$

where
$M_i$
is
the working memory
of stage $i$
and
$b_i$
is
the capacity of
the inter-stage buffer
between stages $i$
and $i + 1$.
Each per-stage term
$M_i$
that
corresponds to
a per-declaration working set
is bounded
a priori
by
Keleusma's
worst-case memory usage analysis,
which
is
program-independent
by construction.
The per-declaration portion
of
$M_{\text{Keleusma}}$
is therefore
$O(1)$
in
the source program size,
matching
the discipline's
overall bound.
The accumulating top-level environment
that
tracks
signatures of
declarations already parsed
grows
with
the top-level declaration count
and is bounded per module
under Keleusma's
separate-compilation model.

A separate
structural verification stage
runs
after emission
and validates
the completed module
against
the block-structured
verification rules
that
article A192 developed.
The verifier
is
formally
a distinct
stream processor
that operates
on
the emitted module
rather than
a stage
of
the compilation pipeline itself.

The compiled bytecode
respects
the streaming discipline
at
the execution level.
The bytecode
is
consumed
by
the Keleusma virtual machine
that
executes
one instruction
at a time,
yields
output values
through
the coroutine `yield` operation,
and resumes
through
the coroutine `resume` operation.
The runtime pipeline
is
itself
a stream processor
whose behaviour
respects
the productivity condition.

The self-hosting endpoint
that
Keleusma's V0.3.0 roadmap
targets
is
the coincidence
of
these two roles.
The Keleusma-in-Keleusma
compiler
is
a stream processor
in
Keleusma source
that
compiles
Keleusma source
to
Keleusma bytecode.
The self-hosted compiler
demonstrates
the discipline
at
its
fixed-point
completion.

## Historical Precedents Recapped

The Keleusma pipeline
sits
within
a
lineage
of
self-hosted
stream-processor compilers
that
this series has traced.

**Wirth's Oberon (nineteen eighty-seven language, nineteen ninety-two book).**
The Oberon compiler,
written in
Oberon,
approximately four thousand lines
of
Oberon source,
demonstrated
the integrated shape
of
the streaming discipline.
The compiler
compiles itself
in one pass
under
the strict declare-before-use rule.

**Turbo Pascal one through three (nineteen eighty-three to nineteen eighty-five).**
Turbo Pascal
was
not
self-hosted,
because
its compiler
was
written in
eight-oh-eight-six assembly language,
not
in Pascal.
Turbo Pascal
was
however
a
commercial demonstration
of
the streaming discipline
at
mass-market scale,
which article A190
treated
under
the epistemic-policy
constraint
of
the closed-source status.

**Brinch Hansen's SuperPascal (nineteen ninety-four).**
SuperPascal
provided
a language runtime
in which
the decomposed pipeline shape
could be expressed
directly
through
`parallel` blocks,
`forall` loops,
and typed channels,
as article A191
detailed.
The SuperPascal compiler itself
was
implemented in
standard sequential Pascal
rather than in
SuperPascal,
per the published record.
Brinch Hansen's line
established
the pipeline architecture
without closing
the self-hosting endpoint.

**WebAssembly (twenty seventeen).**
WebAssembly
codified
the block-structured discipline
at
the bytecode level
for
portable execution.
The WebAssembly compilers
that emit
this bytecode
are typically
multi-pass
at
the source-language level,
but
the bytecode itself
respects
the streaming validation discipline
that
article A192 developed
and Watt mechanised.

**Keleusma (in progress).**
Keleusma
adopts
the streaming discipline
throughout
its language design
and
targets
self-hosting
in
its V0.3.0 milestone.
The
Keleusma-in-Rust
production compiler
implements
the pipeline described above.
The
Keleusma-in-Keleusma
self-hosted compiler
is
the design endpoint.

These five precedents
demonstrate
that
the streaming discipline
has been
achieved
across
four decades
by
different authors
in
different traditions
targeting
different application domains.
The discipline
is
not
a
niche academic exercise.
It
has been
demonstrated
repeatedly
in
production compilers
under
production constraints.

## The Series Argument in Summary

The series
argued
four theses.

**Thesis one: the streaming discipline is a real phenomenon.**
The stream-processor
compilation discipline
is not
a rhetorical framing.
It has
a formal mathematical foundation
in
Rutten's coalgebraic productivity
and
a concrete syntactic characterisation
in
block-structured control flow.
Programs
compiled
under
the discipline
inherit
provable
productivity guarantees
that
programs
compiled
under
the multi-pass tradition
do not
directly
support.

**Thesis two: the streaming discipline is achievable at production scale.**
Wirth's Oberon,
Turbo Pascal,
Brinch Hansen's SuperPascal,
WebAssembly's bytecode validator,
and
Keleusma's compilation pipeline
all
demonstrate
the discipline
at
production scale
under
production constraints.
The discipline
does not
require
academic
toys.

**Thesis three: the streaming discipline has an applicability boundary.**
The discipline
is
the correct choice
for
embedded scripting,
real-time control,
safety-critical systems,
interactive development,
and
educational contexts.
It
is
not
the correct choice
for
whole-program-optimised
native code,
polymorphism-heavy
functional languages,
or
metaprogramming-heavy
domain-specific languages.
The choice
between
the streaming discipline
and
the multi-pass tradition
depends on
target context,
and
neither
is
universally correct.

**Thesis four: self-hosting is the discipline's demonstrative endpoint.**
A stream-processor language
that
can
express
its own
compiler
in
the streaming discipline
demonstrates
the discipline's
sufficiency
for
programs
of
practical complexity.
The self-hosting
demonstrations
that
this series
identified,
namely Oberon
and
Keleusma's V0.3.0 target,
each
close
the discipline's
completeness argument
for
their respective language line.

## Where Next

The series
ends
here
but
the discipline
does not.
Several open questions
remain
for
subsequent investigation.

**Formal verification of stream-processor compilers.**
Watt's WebAssembly mechanisation
and
Leroy's CompCert
both
demonstrated
that
formal verification
of
compiler artefacts
is
feasible
under
current tools.
A stream-processor compiler
whose
architectural discipline
composes
well
with
compositional verification
techniques
is
a natural candidate
for
this treatment.
The Keleusma V0.3.0 roadmap
identifies
this
as
a future direction
without
committing
to
a specific
verification framework.

**Auditability of the discipline.**
A stream-processor compiler
whose
architectural discipline
composes
across stage boundaries
admits
independent per-stage checking
more readily
than
a
multi-pass
optimising compiler
whose
whole-program state
must be
inspected
as a unit.
Small,
single-sweep verifiers
of the kind
that
article A192 developed
are
easier to
audit
than
their
multi-pass counterparts.
The precise mapping
between
architectural properties
and
external review criteria
depends on
the target context
and
remains
future work.

**Extension to non-textual source formats.**
The streaming discipline
generalises
naturally
to
source formats
other than
text,
including
binary
intermediate representations,
graph-based
program representations,
and
domain-specific
data structures.
A stream-processor compiler
whose
source alphabet
is
not
byte-oriented text
retains
the discipline's
compositional properties
if
the source stream
respects
the productivity condition.

**Combined stream-and-batch pipelines.**
Many practical
compilation workflows
combine
streaming
per-file compilation
with
batch
whole-program
post-processing.
The synthesis
of
the two disciplines
into
a
single
architecturally coherent
compilation model
is
an
open engineering question
that
articles
in
the multi-pass tradition
have
not
directly addressed.

## Conclusion

Compilation
is
a stream-processor operation
when
the source language,
the target format,
and
the compiler architecture
respect
the productivity discipline
that
Rutten's coalgebraic framework
formalises.
The historical record
demonstrates
that
the discipline
is
achievable
in
production compilers
under
production constraints,
from
Wirth's Oberon language
in
nineteen eighty-seven
through
Keleusma's
in-progress
self-hosting
in
the present.
The discipline
has
applicability
that
target contexts
either
match
or
do not,
and
the choice
between
the discipline
and
the multi-pass tradition
depends on
the target context
rather than
on
any universal ranking
of
the two.
The self-hosted
stream-processor compiler
is
the fixed-point endpoint
at which
the compiler
and
its compiled programs
are
both stream processors
of
the same language,
demonstrating
the discipline's
sufficiency
for
its own
implementation.
This closes
the series.

## References

### Book

- [*Compiler Construction*][book_wirth_compiler_construction], Niklaus Wirth, Addison-Wesley, 1996
- [*Project Oberon, The Design of an Operating System and Compiler*][book_wirth_project_oberon], Niklaus Wirth and Jürg Gutknecht, revised edition 2013
- [*Brinch Hansen on Pascal Compilers*][book_brinch_hansen_pascal_compilers], Per Brinch Hansen, Prentice-Hall, 1985, ISBN 0-13-083098-4

[book_wirth_compiler_construction]: https://en.wikipedia.org/wiki/Compiler_Construction_(Wirth_book)
[book_wirth_project_oberon]: https://people.inf.ethz.ch/wirth/ProjectOberon/
[book_brinch_hansen_pascal_compilers]: https://en.wikipedia.org/wiki/Per_Brinch_Hansen

### Reference

- [Keleusma total functional stream processor][ref_keleusma]
- [Self-hosting compilers][ref_self_hosting]
- [Bootstrap compilers][ref_bootstrap]

[ref_keleusma]: https://github.com/sgeos/keleusma
[ref_self_hosting]: https://en.wikipedia.org/wiki/Self-hosting_(compilers)
[ref_bootstrap]: https://en.wikipedia.org/wiki/Bootstrapping_(compilers)

### Related Post

- [Compilation as a Streaming Discipline][related_post_streaming_discipline], article A188 in this series
- [Wirth's Single-Pass Line, PL/0 through Oberon][related_post_wirth], article A189 in this series
- [Turbo Pascal, the Closed-Source Demonstration][related_post_turbo_pascal], article A190 in this series
- [Brinch Hansen's Pipeline-of-Processes Compilers][related_post_brinch_hansen], article A191 in this series
- [Block-Structured Control Flow and Single-Pass Validation][related_post_block_structured], article A192 in this series
- [Coalgebraic Productivity and the Stream-Processor Analogy][related_post_coalgebraic], article A193 in this series
- [Fixup Tables and the Forward-Jump Problem][related_post_fixup_tables], article A194 in this series
- [Declare-Before-Use and Forward Declarations][related_post_declare_before_use], article A195 in this series
- [Symbol Tables, Scope Popping, and Bounded Working Memory][related_post_symbol_tables], article A196 in this series
- [Integrated Single-Pass versus Decomposed Pipeline][related_post_integrated_pipeline], article A197 in this series
- [When Multi-Pass Wins, Whole-Program Optimisation and Hindley-Milner Inference][related_post_multi_pass], article A198 in this series

[related_post_streaming_discipline]: {% post_url 2026-04-06-compilation_as_streaming_discipline %}
[related_post_wirth]: {% post_url 2026-04-07-wirth_single_pass_line %}
[related_post_turbo_pascal]: {% post_url 2026-04-08-turbo_pascal_closed_source_demonstration %}
[related_post_brinch_hansen]: {% post_url 2026-04-09-brinch_hansen_pipeline_of_processes %}
[related_post_block_structured]: {% post_url 2026-04-10-block_structured_single_pass_validation %}
[related_post_coalgebraic]: {% post_url 2026-04-11-coalgebraic_productivity_stream_processor_analogy %}
[related_post_fixup_tables]: {% post_url 2026-04-12-fixup_tables_forward_jump_problem %}
[related_post_declare_before_use]: {% post_url 2026-04-13-declare_before_use_forward_declarations %}
[related_post_symbol_tables]: {% post_url 2026-04-14-symbol_tables_scope_popping_bounded_memory %}
[related_post_integrated_pipeline]: {% post_url 2026-04-15-integrated_single_pass_versus_decomposed_pipeline %}
[related_post_multi_pass]: {% post_url 2026-04-16-when_multi_pass_wins %}

### Research

- [Haas and colleagues, Bringing the Web up to Speed with WebAssembly, PLDI 2017][research_haas_webassembly]
- [Leroy, Formal Verification of a Realistic Compiler, Communications of the ACM 52 no. 7, 2009][research_leroy_compcert]
- [Rutten, Universal Coalgebra a Theory of Systems, Theoretical Computer Science 249, 2000][research_rutten_universal_coalgebra]
- [Watt, Mechanising and Verifying the WebAssembly Specification, CPP 2018][research_watt_wasm]

[research_haas_webassembly]: https://dl.acm.org/doi/10.1145/3062341.3062363
[research_leroy_compcert]: https://doi.org/10.1145/1538788.1538814
[research_rutten_universal_coalgebra]: https://doi.org/10.1016/S0304-3975(00)00056-6
[research_watt_wasm]: https://dl.acm.org/doi/10.1145/3167082

## Erratum

An earlier revision of this article
made
two claims
that were
subsequently corrected.

**The SuperPascal self-hosting claim.**
The article previously described
Brinch Hansen's SuperPascal
as
one of
three self-hosting demonstrations
alongside Oberon and Keleusma's V0.3.0 target.
The SuperPascal compiler and interpreter
were
in fact
implemented in
standard sequential Pascal,
specifically the ISO Level 1 dialect,
rather than in SuperPascal.
Brinch Hansen's line
established
the pipeline architecture
and the language design
in which
a self-hosted stream-processor compiler
could naturally be written
but did not
close
the self-hosting endpoint.
The corrected series lists
one demonstrated self-hosting arrangement,
namely Oberon,
and one in-progress target,
namely Keleusma's V0.3.0 roadmap.
Article A191
carries
the corresponding correction
in
the Brinch Hansen historical treatment.

**The working-memory bound.**
The article previously stated
that the compilation pipeline's
total working memory
was
$O(1)$ in the source program size.
This was
overstated.
The per-declaration working set
is
$O(1)$ in the program size
by the streaming discipline,
but
the accumulating top-level environment
that
tracks signatures of
declarations already parsed
grows with
the top-level declaration count
and
is bounded per module
under separate compilation.
Article A196
carries
the corresponding correction
in
the symbol table treatment.
