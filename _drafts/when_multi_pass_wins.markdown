---
layout: post
mathjax: true
comments: true
title:  "When Multi-Pass Wins, Whole-Program Optimisation and Hindley-Milner Inference"
date:   2026-04-16 09:00:00 +0000
categories: compilers streaming series
---

<!-- A198 -->
<script>console.log("A198");</script>

The prior articles
of this series
have argued
for
the stream-processor discipline
without
suggesting
that
the discipline
is universally correct.
Article A197
compared
integrated and decomposed
architectures
within
the discipline
and noted
that
the choice
depended on
target context.
This article
closes the synthesis pair
by
identifying
the contexts
where
the stream-processor discipline itself
breaks down
and
where
the
multi-pass abstract-syntax-tree
tradition
is
the correct choice.

Four language features
push
past
the boundary
of
single-pass tractability.
The first is
whole-program optimisation,
which requires
information
that
crosses
compilation-unit boundaries.
The second is
Hindley-Milner type inference
in its unconstrained form,
where
the type of
a local variable
depends on
uses that
appear
later
in the function.
The third is
type-class or trait resolution,
where
selecting
a specific implementation
requires
searching
the whole program's
implementation space.
The fourth is
metaprogramming,
where
source-level transformations
require
reading and rewriting
source text
that has not yet
been produced.
Each feature
has
a productivity or expressiveness advantage
that
justifies
the multi-pass cost
in
its target context.

## Whole-Program Optimisation

Whole-program optimisation
combines
information
from
across
the entire program
to produce
target code
that
is
faster or smaller
than
per-function-optimised code.
The optimisations
in this class
include
inlining across
compilation units,
devirtualisation
of
polymorphic calls
based on
whole-program type analysis,
and
dead-code elimination
that identifies
functions
whose result
is never used
by any caller.

The information
required
for these optimisations
is not local.
Inlining
a function
into
its callers
requires knowing
which callers
the function has,
which is
whole-program information.
Devirtualising
a polymorphic call
requires knowing
all types
that
can appear
at that call site,
which is
whole-program information.
Dead-code elimination
requires knowing
all uses
of every function,
which is
whole-program information.

A stream-processor compiler
that emits target code
as it recognises source syntax
does not have
access to
this whole-program information
at the moment
of emission.
The compiler
sees
only
the current source position
and
what preceded it.
Any optimisation
that
depends on
information from
what follows
is
outside
the discipline's
reach.

Formally,
the optimisation cost
of
a whole-program pass
is

$$
C_{\text{WPO}}(P) = O(\lvert P \rvert \cdot \log \lvert P \rvert),
$$

for
well-designed
implementations
that use
efficient data structures
for
cross-function analysis.
The cost
is
not
$O(\lvert P \rvert^{2})$
in typical
production compilers
because
the whole-program analysis
uses
structured indexing
and
incremental
data-flow techniques.
The cost
is
still
super-linear
in the program size,
which
is the fundamental
departure from
the linear-cost
stream-processor bound.

The benefit
of whole-program optimisation
is
a
constant-factor speedup
in
the compiled code's
runtime performance.
The specific factor
depends on
the program
and
the optimisation techniques.
Production
optimising compilers
typically achieve

$$
\frac{T_{\text{unoptimised}}}{T_{\text{WPO}}} \in [2, 5]
$$

across
a range of
benchmark suites,
where
$T_{\text{unoptimised}}$
is
the runtime
of code
compiled without
whole-program optimisation
and
$T_{\text{WPO}}$
is
the runtime
of the same code
compiled with
whole-program optimisation
applied.
The range
brackets
typical benchmarks
rather than
worst-case
or best-case
scenarios.
For
programs
whose
runtime
dominates
compilation time
by
several orders of magnitude,
which is
the case for
long-running server workloads
and
scientific-computing programs,
the multi-pass cost
is a
one-time investment
that
pays back
across
the program's operational lifetime.

## Hindley-Milner Type Inference

Hindley-Milner type inference
in its
classical form
solves
a system of
type-equality constraints
across
the entire function body.
The type of
a local variable
is not
determined
by
its declaration
alone.
It depends on
how
the variable
is used
throughout
the function.

Consider
a function definition
of the form

$$
\lambda x. e
$$

where
$e$
is an expression
that
uses $x$
in some way.
The type of $x$
is determined by
$e$'s constraints on it.
If $e$
uses $x$
as an integer,
$x$
must be
of integer type.
If $e$
uses $x$
as
the head of
a list,
$x$
must be
of list type.
The determination
requires
inspecting
$e$
in its entirety,
which
requires
having parsed
the whole function body
before
resolving
$x$'s type.

A single-pass compiler
cannot perform
this inference
because
it does not have
$e$
available
at the time
$x$'s declaration
is parsed.
The classical resolution
requires
constructing
a constraint graph
that spans
the function body
and solving it
by unification
after
the whole body
has been parsed.

Formally,
for a function body
containing
$n$ type variables
and
$m$ constraints,
the unification cost
is

$$
C_{\text{HM}}(f) = O(m \cdot \alpha(n, m)),
$$

where
$\alpha$
is
the inverse Ackermann function
that arises from
the union-find data structure
used
by
efficient
unification implementations.
The cost
is
near-linear
in
the constraint count
for
each function,
but
requires
the whole function body
to be
available
during
the analysis.

Three workarounds
allow
stream-processor compilers
to
support
languages
that resemble
Hindley-Milner
without paying
the full inference cost.

**Restrict inference to
per-declaration scope.**
A compiler
that
requires
explicit type annotations
on
procedure parameters
and return types
can
resolve
the type of
each local variable
against
the annotation
without
whole-function analysis.
This is
the approach
that Wirth's languages
take.
The programmer
supplies
the types
that
the compiler
would otherwise infer.

**Bound inference to
per-declaration scope
with local constraint graph.**
A compiler
that
allows
type inference
within
a single declaration
but
prohibits
inference
across
declarations
can
solve
the local
constraint graph
in
arena memory
whose size
is bounded by
the declaration's complexity.
This is
one of the approaches
that
the Keleusma V0.3.0
self-hosting plan
identifies
as compatible with
the stream-processor discipline.

**Introduce inference as a
separate non-streaming stage.**
A pipeline compiler
can insert
a
non-streaming
type-inference stage
between
the parser
and
the code generator.
The type-inference stage
consumes
each parsed declaration
in full,
runs
the unification algorithm
on
the local constraint graph,
and yields
a
typed declaration
that
subsequent stages
can consume
in streaming fashion.
This is
a
per-declaration
non-streaming stage
that
does not
break
the pipeline's
inter-stage
streaming discipline.

## Type-Class Resolution

Type-class or trait resolution
requires
selecting
a specific implementation
of
a polymorphic operation
based on
the types
that
appear
at
the call site.
The selection
involves
searching
the whole-program's
implementation space
for
an implementation
that
matches
the required type signature.

For a call site
of the form
`op(x)`
where
`op` is
a type-class method
and
`x`
has type
$T$,
the compiler
must find
an instance
of the type class
declared for
type $T$.
The instance
may be declared
anywhere in
the program,
in
any imported module,
or in
any transitively imported module.
The search
requires
whole-program information.

The Haskell
type-class dispatch
and
the Rust
trait-resolution mechanism
both
face
this constraint.
Rust
uses
a
resolution algorithm
that
maintains
an implementation index
across
the entire crate graph
and searches it
at each
polymorphic call site.
A simplified model
of the search cost
at a call site
is

$$
C_{\text{trait}}(\text{call site})
= O(\lvert \text{impls}(T) \rvert),
$$

where
$\lvert \text{impls}(T) \rvert$
is
the number of
implementations
declared
for type $T$.
The actual algorithm
is
substantially more complex
because
of
coherence checks,
orphan rules,
associated types,
higher-ranked trait bounds,
and
blanket implementations
that
require
additional processing
per call site.
For
programs
with
many implementations
per type
or
substantial trait-bound complexity,
the cost
can be
substantial.

A single-pass compiler
cannot support
type-class resolution
in
this form
because
the implementation index
requires
whole-program state.
The alternatives
include
requiring
explicit
dispatch
at each call site,
prohibiting
type classes,
or
restricting
implementations
to
per-declaration scope
where
they can be
resolved locally.
Each alternative
sacrifices
some of
the ergonomic advantages
that
type classes
provide.

## Metaprogramming and Macros

Source-level metaprogramming
in the tradition of
Lisp macros,
C-plus-plus templates,
and Rust
procedural macros
requires
the compiler
to
execute
source-level transformations
that
themselves
produce
new source
to be
compiled.
A macro invocation
in the source
expands
to
new source text
that
the compiler
must then
parse
and compile.

The expansion
can produce
arbitrary code.
The compiler
must
run
the parser
and
sometimes
the earlier compilation stages
on
the expanded output
before
resuming
the compilation
of
the original source.
The expansion
can itself
contain
macro invocations,
which
require
recursive expansion.

A single-pass compiler
that reads
each source token
once
cannot support
this pattern
without
substantial machinery.
The expansion output
must be
inserted
into
the input stream
at
the position of
the macro invocation.
The expanded content
must be
parsed
before
the macro's
containing construct
completes.
The recursion
requires
saving and restoring
the parser state
across
expansion boundaries.

The stream-processor discipline
therefore
prohibits
source-level macros
in general.
Restricted forms
of metaprogramming
that produce
their expansions
at
compile time
before
the streaming pipeline
starts
are compatible
with the discipline.
The Zig
compile-time evaluation model,
which
article A195
mentioned,
is
one such
restricted form.
The Rust
declarative macro system,
which uses
pattern matching
against
the invocation syntax,
is
another
restricted form,
though
Rust's overall
compilation model
is
already
multi-pass.

## Compile-Time Reflection

Compile-time reflection
allows
programs
to
inspect
the structure of
their own
types,
functions,
and modules
during compilation
and generate
code
based on
the inspection results.
Serialisation libraries,
object-relational mappers,
and
schema-driven
code generators
frequently rely on
compile-time reflection.

The reflection API
requires
the compiler
to
maintain
enough
type-and-structure information
to
answer
the reflection queries.
The information
must be
available
at
the reflection call site.
For a reflection query
that inspects
a type
declared
later in
the source,
a single-pass compiler
cannot answer
without
looking ahead.

Most modern languages
that support
compile-time reflection
also support
some form of
multi-pass compilation.
The reflection API
sits
naturally
in
the multi-pass
architecture
because
the whole-program
type table
is already
available
by the time
reflection queries
are evaluated.
Single-pass compilers
that
attempt
to support
reflection
must either
restrict
the reflection scope
to
already-parsed material
or
add
a whole-program
type-collection pass
before
the streaming compilation begins.

## Where the Boundary Lies

The four features
above
share
a common structural property.
Each requires
information
that
is not
available
from
the current source position
alone.
The information
lies
either
in
the source
that
has not yet
been parsed
or
in
imported modules
whose
structure
must be
known
to
the current compilation.

Formally,
a compilation task
is
inside
the stream-processor discipline
if
the target output
at
position $i$
depends only on
the source
in
positions
$0$
through $i$,
that is,

$$
\text{output}(i) = f(\text{source}[0 \ldots i]).
$$

A compilation task
is
outside
the discipline
if
the output
at position $i$
depends on
source
that appears later
or
on
whole-program information,
that is,

$$
\text{output}(i) = f(\text{source}[0 \ldots \infty]).
$$

The boundary
between
the two cases
is
sharp
in
theory
but
gradient
in
practice.
Many languages
adopt
hybrid approaches
that
combine
a stream-processor
front end
with
a multi-pass
optimisation backend,
paying
the multi-pass cost
only for
the features
that require it.
The hybrid form
gives
the output
access to
both
the streaming source prefix
and
a
whole-program
interface index
that
declares
identifier signatures
and
type declarations
before
compilation begins,

$$
\text{output}(i) = f(\text{source}[0 \ldots i], \text{interface}[0 \ldots \infty]).
$$

The interface index
carries
whole-program declarations
without
whole-program bodies,
which
allows
name resolution
to proceed
in a
single forward pass
against
a
pre-computed
declaration table.
The C-plus-plus compilation model,
with
its
translation-unit-local
compilation
followed by
link-time whole-program optimisation,
is
one instance
of this hybrid.
The Rust compilation model,
with
its
crate-local
compilation
followed by
whole-program
monomorphisation
and
optimisation,
is
another.

## Escape Hatches within the Discipline

Some features
that
appear to
require
multi-pass compilation
admit
restricted forms
that
fit
the stream-processor discipline.
The restrictions
sacrifice
some of
the feature's
expressiveness
in exchange for
compilation-cost linearity.

**Explicit type annotations
in place of
Hindley-Milner inference.**
Wirth's languages,
Go's function signatures,
Rust's function signatures
at
the item level,
and
WebAssembly's function types
all
require
explicit annotations
that
substitute
programmer effort
for
inference cost.

**Restricted macros
that expand
before compilation begins.**
Preprocessor-style
macro expansion,
where
the expander
runs
before
the compiler
sees
the source,
is compatible with
streaming compilation
of
the post-expansion source.
The overall compilation
is
multi-pass
only
if
the expander pass
is counted.

**Whole-program information
supplied
by
separate declaration files.**
Modula-2's
definition-implementation split,
C-plus-plus's
header files,
and
Rust's
module interface files
allow
whole-program information
to be
delivered
to
the compiler
through
a
pre-compiled index
rather than
through
source scanning.
The index
is
compact
and
can be
loaded
at
compilation start,
allowing
the actual compilation
to proceed
in
a single forward pass.

**Per-function
non-streaming stages
inside
a streaming pipeline.**
The pipeline compiler
can insert
non-streaming stages
between
the parser
and
the code generator
that
operate on
one declaration at a time
without
requiring
whole-program state.
These stages
break
the strict
streaming discipline
at
the per-declaration level
but preserve it
at
the whole-program level.

## When to Accept Multi-Pass Costs

The multi-pass discipline
is
the correct choice
when
one or more of
the following conditions
hold.

**The target program
runs
for
years
of accumulated
processor time.**
Long-running
server workloads,
scientific-computing programs,
and
production
embedded systems
benefit
substantially
from
whole-program optimisation.
The multi-pass compilation cost
is
amortised
across
many runs.

**The source language
has
type-class
or
trait
polymorphism.**
Modern
functional languages
and
Rust
rely on
these features
for
ergonomic abstractions.
A stream-processor compiler
cannot support them
without
substantial restrictions
that
the language design
did not
anticipate.

**The source language
supports
metaprogramming
as
a
first-class feature.**
Lisp,
Rust,
Zig,
and
Julia
all
use
metaprogramming
extensively.
A stream-processor compiler
that supports
these languages
would
have to
prohibit
or
substantially restrict
this feature.

**The compilation target
supports
whole-program-optimised
executables.**
Native code
for
performance-critical
workloads
benefits from
link-time optimisation.
JIT-compiled bytecode
for
dynamic languages
benefits from
runtime profiling
and
adaptive recompilation.
Both patterns
depend on
whole-program information
that
the stream-processor discipline
does not provide.

## The Streaming Discipline's Domain

The four
push-past conditions
above
identify
the boundary
of
the stream-processor discipline.
Inside the boundary
lie
target contexts
where
the discipline's
compositional properties
are decisive.

- Embedded scripting
  with
  bounded memory
  and
  predictable timing.
- Real-time control
  where
  compilation-cost variability
  is
  an operational concern.
- Safety-critical systems
  where
  small,
  auditable compilers
  reduce
  the verification burden.
- Interactive development
  where
  compilation-cycle latency
  dominates
  developer productivity.
- Educational contexts
  where
  the compiler
  is
  the object of study
  and
  must fit
  in
  a curriculum's time budget.

For target contexts
outside
the boundary,
including
whole-program-optimised
native code,
polymorphism-heavy
functional languages,
and
metaprogramming-heavy
domain-specific languages,
the multi-pass discipline
is
the correct choice.
The synthesis
of
this series
is
that
neither discipline
is universally correct.
The design decision
for
any specific compiler
is
to
identify
which side of
the boundary
the target context
falls on
and
to choose
the corresponding
architecture.

## Conclusion

The stream-processor discipline
does not fit
every target context.
Whole-program optimisation,
Hindley-Milner type inference,
type-class resolution,
and
metaprogramming
each
push past
the boundary
of
single-pass tractability
by
requiring
information
that is not
available
from
the current source position alone.
For target contexts
where
these features
are
essential
or where
the runtime performance benefit
of
whole-program analysis
justifies
the compilation-cost investment,
the multi-pass discipline
is
the correct choice.
For target contexts
where
compositional properties,
bounded memory,
and
compilation-cycle latency
matter more than
these features,
the stream-processor discipline
holds.
Article A199
closes
the series
with
the synthesis
that
compilation itself
is
a stream-processor operation
and that
a self-hosted stream-processor compiler
demonstrates
the discipline
at its
strongest,
using
Keleusma's V0.3.0
compilation pipeline
as
the modern
worked example.

## References

### Reference

- [Whole-program optimisation and link-time optimisation][ref_lto]
- [Hindley-Milner type inference][ref_hm]
- [Rust trait resolution][ref_rust_traits]
- [Lisp macros][ref_lisp_macros]
- [C-plus-plus templates][ref_cpp_templates]

[ref_lto]: https://en.wikipedia.org/wiki/Interprocedural_optimization
[ref_hm]: https://en.wikipedia.org/wiki/Hindley%E2%80%93Milner_type_system
[ref_rust_traits]: https://en.wikipedia.org/wiki/Rust_(programming_language)
[ref_lisp_macros]: https://en.wikipedia.org/wiki/Macro_(computer_science)
[ref_cpp_templates]: https://en.wikipedia.org/wiki/Template_(C%2B%2B)

### Related Post

- [Compilation as a Streaming Discipline][related_post_streaming_discipline], article A188 in this series
- [Wirth's Single-Pass Line, PL/0 through Oberon][related_post_wirth], article A189 in this series
- [Declare-Before-Use and Forward Declarations][related_post_declare_before_use], article A195 in this series
- [Integrated Single-Pass versus Decomposed Pipeline][related_post_integrated_pipeline], article A197 in this series

[related_post_streaming_discipline]: {% post_url 2026-04-06-compilation_as_streaming_discipline %}
[related_post_wirth]: {% post_url 2026-04-07-wirth_single_pass_line %}
[related_post_declare_before_use]: {% post_url 2026-04-13-declare_before_use_forward_declarations %}
[related_post_integrated_pipeline]: {% post_url 2026-04-15-integrated_single_pass_versus_decomposed_pipeline %}

### Research

- [Leroy, Formal Verification of a Realistic Compiler, Communications of the ACM 52 no. 7, 2009][research_leroy_compcert]

[research_leroy_compcert]: https://doi.org/10.1145/1538788.1538814
