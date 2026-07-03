---
layout: post
mathjax: true
comments: true
title:  "Integrated Single-Pass versus Decomposed Pipeline"
date:   2026-04-15 09:00:00 +0000
categories: compilers streaming series
---

<!-- A197 -->
<script>console.log("A197");</script>

The prior-art trio
of articles A189 through A191
identified
two distinct architectures
that
belong to
the stream-processor
compilation discipline.
The integrated single-pass compiler
of
the Wirth line
and
Turbo Pascal
runs the entire pipeline
inside
a recursive-descent parser
that emits target code
inside its own procedures.
The decomposed pipeline compiler
of
Per Brinch Hansen's tradition
splits the pipeline
into
independent stages
that communicate through
bounded queues.
Both architectures
achieve
the same
theoretical properties
of
linear compilation cost
and
program-independent working memory.
Both have
been demonstrated
in
production compilers
by
different authors
in
different traditions.

This article
compares
the two architectures
head to head
on
workloads
that
either architecture
can accomplish.
It identifies
where
one architecture
carries
material advantages
over the other
and
where
the choice
is
essentially
a matter of
implementation preference.
The article
closes with
the Keleusma V0.3.0
self-hosting roadmap
as
a modern worked example
of
the decomposed pipeline
approach,
showing
how
Brinch Hansen's pattern
manifests
in
a coroutine-based
embedded scripting language
where
each pipeline stage
is
a `loop` function
that
communicates through
`yield` and `resume`
operations.

## The Two Shapes Recapped

The integrated single-pass compiler
has
one main procedure,
the recursive-descent parser.
Inside the parser,
the lexer
is
a method call
that
returns
the next token on demand.
The code generator
is
a set of
methods
called at
the syntactic point
where each construct
is recognised.
There is
no separate lexer process,
no separate parser stage,
no separate code-generation phase.
The three logical stages
are
inlined
into
a single call chain.

The decomposed pipeline compiler
has
multiple independent stages.
Each stage
runs
as
a separate process
in
concurrent implementations
or
as
a coroutine
in
sequential implementations.
Each stage
holds
only
its local working state.
The stages
communicate
through
bounded buffers
that
each stage
reads from
its upstream neighbour
and
writes to
its downstream neighbour.

The two shapes
sit at
opposite ends of
one axis
in
the two-axis design space
introduced in
article A188.
Both shapes
sit
at the same position
on
the other axis,
namely
abstract-syntax-tree-free
direct emission,
which
distinguishes them
from
the multi-pass
tradition
of
production
optimising compilers.

## Comparing on Matched Workloads

For a workload
where
either architecture
can produce
identical target bytecode,
the two shapes
have
comparable but not identical
resource profiles.

**Working memory.**
Both shapes
achieve
$O(1)$
per-declaration working set
in
the source program size,
and
both accumulate
a top-level environment
that
grows with
the top-level declaration count.
The integrated compiler
holds
the parse stack,
the symbol table,
and
the fixup buffer
in
one memory region.
The decomposed compiler
distributes
these
across
the pipeline stages
and adds
the inter-stage buffers.

For an integrated compiler,
the working memory
is
approximately

$$
M_{\text{integrated}}
\approx \lvert S \rvert + \lvert T \rvert + \lvert F \rvert,
$$

where
$S$
is the parse stack,
$T$
is the symbol table,
and
$F$
is the fixup buffer.

For a decomposed compiler
with $k$ stages
and inter-stage buffer sizes
$b_i$,
the working memory
is
approximately

$$
M_{\text{pipeline}}
\approx \sum_{i=1}^{k} m_i + \sum_{i=1}^{k-1} b_i,
$$

where
$m_i$
is
the working state of stage $i$.
The two sums
are typically
of the same
order of magnitude
because
the same total state
is
present in both architectures,
distributed differently.

**Compilation throughput.**
Both shapes
process
each source token
in
constant time
on average.
The compilation cost
is
linear
in
the program size
for both.
The constants
differ
by
a factor
that
depends on
the concrete implementation choices.

For the integrated compiler,
each token
travels
through
a single procedure call chain
whose
constant per-token overhead
is
low.
For the decomposed compiler,
each token
crosses
inter-stage buffer boundaries,
which
adds
a small
per-token buffering cost.
The specific ratio

$$
\frac{T_{\text{pipeline}}}{T_{\text{integrated}}}
= 1 + \frac{k - 1}{L},
$$

where
$L$
is the average number of instructions per token processed within a stage
and
$k$
is the number of stages,
approaches
one
for
larger $L$
and
grows
with
smaller $L$.
For a typical Wirth-style compiler
with
$L$
on the order of
tens to hundreds of instructions per token,
the pipeline overhead
is
under ten percent
compared to
the integrated form.

**End-to-end latency.**
The two shapes
differ
substantially
in
end-to-end latency.
The integrated compiler
produces
target output
immediately
as
each syntactic construct
is recognised,
with
sub-token latency.
The decomposed compiler
must
transit
each item
through
the buffer chain,
which
takes
at least
$k - 1$
buffer-transit times
per item,
as
article A191 formalised.
The comparative latency
between the two shapes
is therefore

$$
\Delta L
= L_{\text{pipeline}} - L_{\text{integrated}}
\approx (k - 1) \cdot \tau_{\text{buffer}},
$$

where
$\tau_{\text{buffer}}$
is
the average
inter-stage buffer-transit time
per item.
For a $k$ around
four or five
and
$\tau_{\text{buffer}}$
on the order of
microseconds
under
typical
in-process
coroutine
implementations,
the latency gap
is
on the order of
tens of microseconds
per item.

For compilation of
programs
whose bytecode output
must be
delivered
incrementally
during compilation,
the integrated shape
has
a
qualitative advantage.
For compilation of
programs
whose bytecode output
is
written to a file
and consumed later,
the latency difference
is
irrelevant.

## Testability

The decomposed shape
has
a
substantial advantage
in
testability.
Each stage
can be
tested
in isolation
by
driving it
with
a synthesised input stream
and
inspecting
the output stream.
A test harness
that
exercises
the parser stage
does not need to
run
the lexer stage,
because
the parser
receives
its input
from
a buffer
that the test
can populate directly.

For a compiler
with
$k$ stages,
the testability decomposition gives

$$
\text{Test surfaces}
= k \text{ per-stage surfaces}
+ 1 \text{ full-pipeline surface}.
$$

The integrated compiler
has
only
the full-pipeline surface
because
its stages
are
inlined.
A test
that
exercises
the parser
must
run
the lexer
because
the two
are called
in the same procedure.
A test
that
exercises
the code generator
must
run
all upstream stages.

The per-stage testability
of
the decomposed shape
supports
several testing techniques
that
the integrated shape
cannot use directly.

**Property-based testing per stage.**
Random-input generation
for
the parser
can proceed
by
generating
token streams
directly
rather than
generating
source strings
that
must round-trip through
the lexer.
The generated inputs
exercise
the parser's decision boundaries
without
any lexer-imposed
distributional constraints.

**Snapshot testing per stage.**
Golden-file tests
that
capture
the output
of
each stage
against
a known input
can catch
regressions
in
individual stages
independently
of
the other stages.
A regression
in
the parser stage
manifests
as
a snapshot mismatch
at
the parser output,
which
localises
the failure
to
the parser
before
any downstream stage
runs.

**Differential testing between stages.**
When
two different implementations
of
the same stage
exist,
they
can be
compared
by
driving both
with
the same input stream
and
comparing
their output streams.
The comparison
requires
the stage boundaries
to be
observable,
which
the decomposed shape
provides
by construction
and
the integrated shape
does not.

## Verification Burden

For
a compiler
that
must undergo
formal verification
or
extensive independent review,
the choice of
architectural shape
affects
the verification burden.

The decomposed shape
supports
compositional verification.
Each stage
can be
verified independently.
The composition
of
correctly verified stages
gives
a correctly verified compiler
under
appropriate
composition rules.
The total verification cost
is
therefore

$$
V_{\text{pipeline}}
= \sum_{i=1}^{k} V_i^{\text{stage}}
+ V^{\text{composition}},
$$

where
$V_i^{\text{stage}}$
is
the cost of
verifying stage $i$
in isolation
and
$V^{\text{composition}}$
is
the cost of
composing
the individual results
into
an end-to-end guarantee.

The integrated shape
requires
whole-compiler verification.
The verification argument
must
track
the state of
the parser stack,
the symbol table,
the fixup buffer,
and
the output emission
throughout
a single monolithic argument.
The total verification cost
is

$$
V_{\text{integrated}}
= V^{\text{monolithic}},
$$

which
generally
exceeds
the sum of
per-stage costs
by
a factor
that
depends on
the strength of
the required guarantees.
The CompCert project
and
Watt's WebAssembly mechanisation,
mentioned in
articles A188 and A192,
both address
verification of
compiler artefacts,
and
both benefit
from
architectural decomposition
where possible.

## Concurrent Execution Options

The decomposed shape
admits
concurrent execution
of
the pipeline stages
on
multiprocessor hardware.
The integrated shape
does not
admit
concurrent execution
of its logical stages
because
they are
inlined
into
a single call chain.

For the decomposed shape,
under
the pipeline-parallelism model
of
article A191,
the speedup
of concurrent execution
against
sequential execution
of the same pipeline
is

$$
\text{speedup}
= \frac{\sum_{i=1}^{k} T_i^{-1}}{\max_{i} T_i^{-1}},
$$

which
approaches $k$
for
a $k$-stage pipeline
balanced
across
the stages
and
degrades
to one
when
a single slow stage
dominates.
In practice,
compilation stages
are not
perfectly balanced,
and
the achieved speedup
is
typically
in
the two-to-four range
for
a four-to-five-stage compiler.
The absolute throughput gain
is
modest
compared to
the throughput of
a well-tuned integrated compiler,
but
becomes
significant
for
very large
source files
or
for
batch compilation
of
many source files.

The integrated shape
can exploit
concurrent execution
only
at
a higher granularity,
such as
compiling
multiple source files
in parallel.
The intra-file
compilation
remains
serial.

## The Coroutine Middle Ground

Between
the integrated shape
and
the decomposed shape
with
concurrent execution
lies
a
coroutine-based decomposition
that
preserves
the decomposed architecture
without
requiring
concurrent execution.

Each pipeline stage
is
a coroutine
whose
`yield` operation
plays the role of
a bounded-buffer send
and whose
`resume` operation
plays the role of
a bounded-buffer receive.
The stages
run
sequentially
on
a single processor,
with
one stage
active at a time.
When
the active stage
yields,
control transfers
to the next stage,
which resumes
where it
left off.

The coroutine implementation
preserves
several properties
of
the decomposed shape.
Per-stage testability
holds
because
each coroutine
can be
driven
independently
by
supplying
its input stream
directly.
Compositional resource bounds
hold
because
each coroutine's
working memory
is
bounded independently
and
the inter-stage buffers
have
fixed capacity.
Sequential single-processor execution
is
predictable
in
timing
and
memory usage,
which matters for
embedded and
real-time contexts.

The coroutine implementation
sacrifices
one property
of
the fully concurrent
decomposed shape,
namely
pipeline parallelism
on
multiprocessor hardware.
For single-processor
embedded targets
where
concurrent execution
is
unavailable
or
undesirable,
the sacrifice
is
irrelevant.
For multi-processor
production compilation contexts
where
throughput
is
critical,
the coroutine implementation
leaves
performance
on the table.

## Keleusma V0.3.0 as a Modern Worked Example

The Keleusma language
is
a total functional stream processor
that compiles
to bytecode
for
embedded scripting,
real-time audio and game engines,
and
high-assurance
embedded control contexts.
The language's
V0.3.0 self-hosting roadmap,
which the Keleusma project
has published
as a strategy document,
adopts
the decomposed-pipeline
compiler architecture
with
the coroutine implementation
just described.
The recommendation
is
documented
as
a design in progress
rather than
a shipped result.
Keleusma's Rust-hosted compiler
is
the current production form,
and
the self-hosted Keleusma-in-Keleusma
compiler
is
the V0.3.0 endpoint.

The proposed Keleusma
self-hosted compiler
consists of
three coordinated stages
at
the coroutine-projection level.
Each stage
is
a Keleusma `loop` function
in
source form.

- The **lexer** stage
  consumes
  source bytes
  and
  yields tokens.
- The **parser** stage
  consumes tokens
  and
  yields
  parsed declarations
  one at a time.
- The **compiler** stage
  consumes
  parsed declarations
  and
  yields
  bytecode chunks.

The three-stage decomposition
is
the simplified
self-hosted coroutine projection
that
maps
one Keleusma `loop` function
to
one pipeline stage.
The current
Rust-hosted production compiler
uses
a finer-grained
five-stage decomposition
of
tokenise,
parse,
typecheck,
monomorphise,
and
emit-with-hoist,
as
article A199 details
in the closer.
The two decompositions
describe
the same pipeline
at different levels of granularity.
The coroutine projection
merges
the middle three
Rust stages
into
the compiler `loop` function
because
the coroutine model
does not
require
independent stage boundaries
between
typecheck,
monomorphise,
and
emit.

The three stages
map
one-to-one
with
Brinch Hansen's
pipeline-of-processes model.
The Keleusma
`yield` operation
transmits
a value
from
the yielding stage
to
its downstream consumer.
The
`resume` operation,
which
Keleusma structures
as
the host's call
to the coroutine,
delivers
the next input
to
the resuming stage.
The inter-stage buffer
is
implicitly
of capacity one
because
Keleusma's coroutine model
delivers
one value per yield-resume cycle.

Each stage's
working memory
is bounded
by
Keleusma's
worst-case memory usage analysis,
which
Keleusma calls
WCMU
and
which
compiles into
a
compile-time guarantee
on
each stage's
memory footprint.
The guarantee
per stage
is
independent of
the source program
being compiled,
matching
the bounded-working-memory bound
of the trio.

The choice
of
the coroutine implementation
over
the fully concurrent
decomposed shape
reflects
Keleusma's
target contexts.
The language
runs
on
no-standard-library plus
allocation-supporting
embedded hosts
where
single-processor execution
is
the norm.
Pipeline parallelism
is
not
a
target design property.
The coroutine implementation
preserves
the testability,
compositional-resource,
and
Brinch-Hansen-lineage
architectural benefits
without
paying
the concurrency cost.

Keleusma
also documents
the integrated single-pass
alternative
for
completeness
and notes
that
the alternative
sits
on the shelf
if
implementation
surfaces
a
material reason
to prefer it.
The design decision
is
that
neither shape
is
obviously better
for
Keleusma's target contexts,
so
the decomposed shape
is
chosen
for
its
compositional
verification properties
and
its
per-stage testability.

## Decision Criteria

The decision
between
the integrated shape
and
the decomposed shape
depends on
several considerations
that
do not
always point
the same way.

**Verification requirements.**
For
compilers
that
must undergo
formal verification
under
a safety standard,
the decomposed shape
supports
compositional verification
and
reduces
the total verification burden.
For
compilers
without
such requirements,
the choice
is
less
constrained.

**Concurrent execution availability.**
For
compilers
that
run on
multiprocessor hardware
and
target
programs
whose compilation
benefits from
concurrent processing,
the decomposed shape
admits
pipeline parallelism.
For
compilers
that
run on
single-processor hardware
or
whose targets
are small enough
that
parallelism
does not help,
the choice
is
between
the integrated shape
and
the coroutine-based
decomposed shape.

**Testing methodology.**
For
compilers
whose
testing strategy
relies on
per-stage golden files,
property-based tests
of
intermediate representations,
or
differential comparison
against
a reference implementation,
the decomposed shape
supports
these techniques
directly.
For
compilers
whose
testing strategy
uses
only
end-to-end integration tests
against
the shipped bytecode,
the decomposition
adds
overhead
without proportionate benefit.

**Implementation preference.**
For
compilers
written
by
a single author
who prefers
one shape
over the other,
the choice
is
a
matter of preference
provided
the underlying
theoretical properties
hold
for both.
The Wirth tradition
and
the Brinch Hansen tradition
both produced
working compilers
under
different
architectural choices,
and
neither tradition's
choice
was
uniquely correct.

## Conclusion

The integrated single-pass compiler
and
the decomposed pipeline compiler
both belong to
the stream-processor
compilation discipline
and
both achieve
the same
$O(1)$-in-program-size
per-declaration working set,
the same
top-level environment growth
proportional to
top-level declaration count,
and
the same
linear-in-program-size
compilation cost.
The integrated shape
has
a
lower per-token overhead
and
lower end-to-end latency.
The decomposed shape
has
per-stage testability,
compositional verification,
and
optional pipeline parallelism.
The coroutine-based
implementation
of
the decomposed shape,
demonstrated in
the Keleusma V0.3.0
self-hosting roadmap,
sits
between
the two extremes
by preserving
the compositional properties
without
requiring
concurrent execution.
For
target contexts
where
formal verification,
per-stage testability,
or
lineage
alignment with
Brinch Hansen's tradition
matters,
the decomposed shape
is
the preferred choice.
For
target contexts
where
raw throughput
or
minimal overhead
matters,
the integrated shape
is
the preferred choice.
Neither shape
is universally correct.
Article A198
closes
the synthesis pair
with
an analysis of
where
the stream-processor discipline
itself
breaks down,
covering
whole-program optimisation,
Hindley-Milner type inference,
and
the language features
that
push
past
the boundary
of
single-pass tractability.

## References

### Book

- [*Brinch Hansen on Pascal Compilers*][book_brinch_hansen_pascal_compilers], Per Brinch Hansen, Prentice-Hall, 1985, ISBN 0-13-083098-4
- [*Project Oberon, The Design of an Operating System and Compiler*][book_wirth_project_oberon], Niklaus Wirth and Jürg Gutknecht, revised edition 2013

[book_brinch_hansen_pascal_compilers]: https://en.wikipedia.org/wiki/Per_Brinch_Hansen
[book_wirth_project_oberon]: https://people.inf.ethz.ch/wirth/ProjectOberon/

### Reference

- [Keleusma total functional stream processor][ref_keleusma]
- [Coroutines in programming languages][ref_coroutines]

[ref_keleusma]: https://github.com/sgeos/keleusma
[ref_coroutines]: https://en.wikipedia.org/wiki/Coroutine

### Related Post

- [Compilation as a Streaming Discipline][related_post_streaming_discipline], article A188 in this series
- [Wirth's Single-Pass Line, PL/0 through Oberon][related_post_wirth], article A189 in this series
- [Turbo Pascal, the Closed-Source Demonstration][related_post_turbo_pascal], article A190 in this series
- [Brinch Hansen's Pipeline-of-Processes Compilers][related_post_brinch_hansen], article A191 in this series
- [Block-Structured Control Flow and Single-Pass Validation][related_post_block_structured], article A192 in this series

[related_post_streaming_discipline]: {% post_url 2026-04-06-compilation_as_streaming_discipline %}
[related_post_wirth]: {% post_url 2026-04-07-wirth_single_pass_line %}
[related_post_turbo_pascal]: {% post_url 2026-04-08-turbo_pascal_closed_source_demonstration %}
[related_post_brinch_hansen]: {% post_url 2026-04-09-brinch_hansen_pipeline_of_processes %}
[related_post_block_structured]: {% post_url 2026-04-10-block_structured_single_pass_validation %}

### Research

- [Brinch Hansen, SuperPascal, a Publication Language for Parallel Scientific Computing, Concurrency Practice and Experience 6, 1994][research_brinch_hansen_superpascal]

[research_brinch_hansen_superpascal]: https://doi.org/10.1002/cpe.4330060509
