---
layout: post
mathjax: true
comments: true
title:  "Compilation as a Streaming Discipline"
date:   2026-04-06 09:00:00 +0000
categories: compilers streaming series
series: streaming_compilers
series_title: Streaming Compilers
series_index: 1
---
<!-- A188 -->
<script>console.log("A188");</script>

A compiler
that reads its source once,
holds nothing in memory
that grows with the size of the input,
and emits its output as it goes
is a stream processor.
A compiler
that constructs a whole-program abstract syntax tree,
solves constraints
that span the entire program,
and rewrites the tree
across many passes
is not.
The distinction is not a matter of taste.
The two disciplines
produce compilers
whose working memory,
compilation throughput,
and error-recovery behaviour
differ by orders of magnitude.
They also produce compilers
whose amenability to formal verification,
to embedded deployment,
and to independent auditing
differ qualitatively.

The stream-processor discipline
is the older of the two.
It reaches from Niklaus Wirth's PL/0 pedagogy
of nineteen seventy-six,
through the original Pascal compiler,
Modula-2,
Turbo Pascal,
Oberon,
Per Brinch Hansen's SuperPascal,
and forward into
the WebAssembly single-pass validator
and the recent embedded-scripting family.
The multi-pass abstract-syntax-tree discipline
that dominates present-day
production compilers,
GNU Compiler Collection,
Clang,
and the Rust compiler,
optimises for a different objective.
Whole-program optimisation
demands a whole-program representation.
Modern hardware
tolerates the memory cost
that comes with it.

The trade-off is real,
but it is not a value judgement.
Neither discipline
is universally correct.
This series
treats the stream-processor discipline
on its own terms,
identifies the design levers
that make single-pass compilers work,
records the closed-source
and open-source demonstrations
that shaped the tradition,
and closes with a synthesis
that names the modern realisations
in the WebAssembly ecosystem
and in the coroutine-based
embedded-scripting family.

## The Streaming Discipline

A stream processor
reads its input in a single forward pass
and produces its output incrementally.
The classical model
was formalised by Rutten
as the coalgebraic view of stream computation
[Rutten's universal-coalgebra treatment][research_rutten_universal_coalgebra]
and elaborated in the [coinductive stream calculus][research_rutten_stream_calculus].
The applied form
appears in synchronous reactive languages,
signal-processing pipelines,
and any program
whose working set
is bounded by
the size of a sliding window
rather than the size of the input.

A stream-processor compiler
applies the same discipline
to source-code processing.
The lexer
reads bytes
and yields tokens.
The parser
reads tokens
and yields declarations,
one at a time.
The code generator
reads declarations
and yields bytecode
or machine code,
one chunk at a time.
Each stage
holds a bounded amount of state.
No stage
holds the entire program.
The compiler's working memory
is a function of
the largest single declaration,
not the total program size.

The formal guarantee
that a stream-processor compiler
does not stall
is [productivity in the coinductive sense][research_abel_pientka_copatterns].
For a stream processor
of the shape $f\colon A^{\omega} \to B^{\omega}$,
productivity requires
a monotone non-decreasing function
$m\colon \mathbb{N} \to \mathbb{N}$
such that

$$
\forall n \in \mathbb{N}, \quad
f(a)[0 \ldots m(n)]
\text{ is determined by }
a[0 \ldots n].
$$

Every finite prefix of input
produces some finite prefix of output.
The output stream
does not depend on
the compiler having seen
the end of the input stream.
This property
is the same one
that makes an audio-processing loop
useful
and a divergent computation
useless.
Endrullis and colleagues
showed that productivity
is [decidable for suitably restricted stream definitions][research_endrullis_productivity].
Block-structured control flow,
declare-before-use ordering,
and forward-declaration discipline
put a compiler
inside the decidable subclass.

The consequence
for working memory
is the property
that separates the disciplines.
A multi-pass compiler
that materialises
a whole-program abstract syntax tree
requires working memory
linear in the program size,
written as

$$
M_{\text{multi-pass}}(P) = \Theta(\lvert P \rvert),
$$

where $\lvert P \rvert$
is the source-file byte length
of program $P$.
A stream-processor compiler
holds no whole-program representation.
Its working memory
is bounded by
the largest single declaration
plus the total inter-stage buffer size,
written as

$$
M_{\text{stream}}(P)
= O\bigl(D(P) + B\bigr),
$$

where $D(P)$
is the maximum size
of any single declaration in $P$
and $B$
is the sum
of the fixed-size
inter-stage buffers.
When $D(P)$ is bounded independently of $\lvert P \rvert$,
which holds for
any program
whose individual declarations
respect a size limit,
the stream-processor compiler's per-declaration working set
is $O(1)$
in the program size.
The accumulating top-level environment,
which
records
signatures of
declarations already parsed,
grows
with the top-level declaration count
rather than
with the total source size,
and is bounded per module
under separate compilation.
The distinction
between
the bounded per-declaration working set
and
the accumulating top-level environment
is developed
in articles A195 and A196.

## Two Design Axes

The stream-processor tradition
divides along two orthogonal axes.
The first axis
runs from integrated single-pass
to decomposed pipeline.
The second axis
runs from AST-materialised
to AST-free direct emission.

An integrated single-pass compiler
runs the entire pipeline
inside one recursive-descent parser.
The lexer
is a method on the parser
that returns the next token on demand.
The code generator
is a set of methods
called at the point in parsing
where each syntactic construct is recognised.
There is no token stream
that persists between stages,
because the parser
consumes each token
as soon as the lexer produces it.
There is no abstract syntax tree,
because the parser
never builds one.
Turbo Pascal,
the Oberon compiler,
and the various Modula-2 compilers
followed this shape.

A decomposed pipeline compiler
splits the stages
into independent processes
that communicate through bounded queues.
Per Brinch Hansen
advocated this shape
in his book
[Brinch Hansen on Pascal Compilers][book_brinch_hansen_pascal_compilers].
The lexer,
parser,
semantic analyser,
and code generator
run as concurrent processes,
each holding local state,
each yielding to the next
through a fixed-size buffer.
The compiler's total working memory
is the sum
of the per-stage local state
plus the inter-stage buffer sizes.
Neither term
grows with the program size.
Brinch Hansen's SuperPascal
extended the pipeline architecture
into
a language
designed for
concurrent stream processing,
demonstrating
the pipeline-of-processes shape
in
a language whose runtime
was designed
to support it directly.
The SuperPascal compiler itself
was implemented
in standard sequential Pascal
rather than in SuperPascal,
per the published record.

The second axis,
AST-materialised versus AST-free,
is nearly orthogonal to the first.
A pipeline compiler
can materialise an AST
between the parser stage
and the code generator stage,
paying the memory cost
that the streaming discipline
would otherwise avoid.
An integrated single-pass compiler
can build an AST fragment
for a single declaration
and free it
as soon as the declaration is emitted.
The empirical pattern
in the Wirth tradition
is integrated-and-AST-free.
The empirical pattern
in the modern production tradition
is multi-pass-and-AST-materialised.
The pipeline-and-AST-free quadrant,
where Brinch Hansen worked,
remains the least populated.

## The Turbo Pascal Question

Turbo Pascal
occupies a peculiar position
in the history of this discipline.
The productivity gains
were commercially decisive.
The compiler's throughput
of ten thousand to thirty thousand
lines per second
on a four-point-seven-seven megahertz
Intel eight-oh-eight-eight processor
in nineteen eighty-four
changed the shape
of the [interactive development cycle that Hejlsberg himself later recounted][ref_hejlsberg].
Working from the reported upper-end throughput,
the cycle budget per source line
was

$$
\frac{4.77 \times 10^{6} \text{ cycles/second}}
     {3.0 \times 10^{4} \text{ lines/second}}
\approx 159 \text{ cycles/line}.
$$

The compile-link-run cycle
fit inside sixty-four kilobytes
of random-access memory
as a Borland design constraint.
For the Zilog Z-eighty version
that shipped for Control Program for Microcomputers,
sixty-four kilobytes
was the machine's total user address space
because the Z-eighty's address bus
was sixteen bits wide.
For the Intel eight-oh-eight-eight version
that shipped for Microsoft Disk Operating System,
the design constraint
was not the address bus,
which was twenty bits wide
and reached one megabyte,
but the choice
to keep the editor,
compiler,
and runtime
together in a single
sixty-four-kilobyte segment.
The order-of-magnitude conclusion
is what carries the argument.
A compiler
that materialises
a whole-program abstract syntax tree
on an eight-oh-eight-eight processor
of that period
would need
substantially more time
than one hundred and fifty-nine cycles per line,
because the tree-node writes alone
consume most of the budget
before any parsing decisions occur.
This inference
is not proven here
in strict cycle-accounting terms.
The claim rests on
the sixty-four-kilobyte segment budget,
which caps the AST size
independently of throughput,
and on the observation
that the memory-write cost per node
is a substantial fraction
of the reported cycles per line.
The stream-processor discipline
under these hardware constraints
was not
a stylistic choice.
It was
the architecture
that fit the hardware.

The compiler's internal architecture
was never released as open source.
Anders Hejlsberg wrote it in
Intel eight-oh-eight-six assembly language.
Present-day study
of the internal design
must proceed
from the surviving oral-history record
and from
reverse-engineering of the shipped binary.
This series
gives Turbo Pascal
a dedicated article
that surveys what is known,
what is inferred,
and what remains
formally unknown.
The uncertainty
does not undermine
the architectural point.
Turbo Pascal
was commercially successful
because it was fast,
and it was fast
because it applied
the stream-processor discipline
consistently.
The internal detail
matters
for historical accuracy,
but not
for the conceptual argument.

## Why It Matters Now

Three developments
have brought
the stream-processor compilation discipline
back into active use.

The first
is the rise of WebAssembly
as a portable execution target.
The WebAssembly design
mandates block-structured control flow
precisely so that
a single-pass validator
can accept or reject
each function
in one forward sweep
without constructing a [control-flow graph][research_haas_webassembly].
The design received
the Programming Language Design and Implementation
distinguished-paper award
of twenty seventeen
for this insight.

The second
is the emergence
of embedded scripting languages
that target
resource-bounded environments.
Real-time audio engines,
game scripting,
and high-assurance
embedded control
cannot afford
a compiler
whose working memory
depends on the program size.
Contemporary work
in this area,
including Rhai,
Lua bindings,
and the Rex project,
grapples with the same trade-off
that Wirth and Brinch Hansen
resolved decades earlier.

The third
is the growing interest
in formal verification
of compilers.
The [CompCert project][research_leroy_compcert]
demonstrated
that formally verified compilation
is possible for a multi-pass compiler,
but the verification burden
is substantial.
A single-pass compiler
with a small
and well-structured
verification obligation
is inherently
easier to audit.
The Wirth tradition
produced compilers
whose small size,
in some cases
fewer than four thousand lines,
positions them
as candidates
for full formal treatment
that a modern
million-line compiler
cannot approach.

## Series Roadmap

The twelve articles
of this series
walk the stream-processor
compilation discipline
in three groups.

The prior-art trio,
articles A189 through A191,
covers the three
foundational demonstrations.
Article A189
treats Niklaus Wirth's single-pass line
from PL/0 in nineteen seventy-six
through Oberon in nineteen eighty-seven.
Article A190
treats Turbo Pascal
as the closed-source commercial demonstration,
with explicit epistemic care
throughout.
Article A191
treats Per Brinch Hansen's
pipeline-of-processes architecture
and the SuperPascal self-hosting result.

The theory pair,
articles A192 and A193,
develops the mathematical structure
that makes the stream-processor discipline
work.
Article A192
covers block-structured control flow
and the single-pass validation strategy
that WebAssembly
canonised.
Article A193
covers coalgebraic productivity,
the property
that formalises the streaming guarantee
in the coinductive setting.

The techniques trio,
articles A194 through A196,
covers the three
low-level engineering techniques
that make single-pass compilation possible.
Article A194
covers fixup tables
and the forward-jump problem.
Article A195
covers declare-before-use ordering
and forward declarations
for mutual recursion.
Article A196
covers symbol tables,
scope popping,
and the bookkeeping
that keeps
the compiler's working memory
bounded.

The synthesis pair,
articles A197 and A198,
compares the design shapes
against one another
and identifies
when the trade-off breaks down.
Article A197
compares integrated single-pass
against decomposed pipeline
in matched-workload terms.
Article A198
identifies
where multi-pass compilation wins,
covering whole-program optimisation,
Hindley-Milner type inference
in its unconstrained form,
and the language features
that push
past the stream-processor boundary.

The closer,
article A199,
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
The closer
uses a modern embedded-scripting
compiler pipeline
as the worked example.

## Terminology

This series
adopts specific meanings
for several terms
that appear
in the compilation literature
with less precision.

A **pass**
is a traversal
of the input.
A single-pass compiler
reads the input once
from start to finish.
A multi-pass compiler
reads the input
or an intermediate representation
more than once.
The distinction
counts traversals of the source or of an equivalent representation,
not stages in a pipeline.

A **stage**
is a component of the compiler
that performs
a distinct transformation.
A lexer,
a parser,
and a code generator
are three stages.
A compiler
can have many stages
and still be single-pass,
if each stage
reads its input in one forward sweep.
The stages
can execute concurrently
in a pipeline,
or sequentially
without materialising
the intermediate representation.

A **stream**
in this series
is a sequence
that is produced incrementally
and consumed incrementally.
The stream
does not have to be infinite.
A source file
of finite length
is a finite stream.
The property
that matters
is that
the consumer
does not need to see
the end of the stream
before starting to produce output.

A **stream processor**
is a program
that consumes streams
and produces streams
under the productivity discipline.
A stream-processor compiler
is a compiler
that fits this description.

A **decomposed pipeline**
is a compiler
whose stages
communicate through
inter-stage buffers.
An **integrated single-pass compiler**
is a compiler
whose stages
are inlined
into a single function-call chain,
typically the recursive-descent parser
at the outer layer.

These definitions
carry through
the rest of the series
without further comment.

## Conclusion

Compilation as a streaming discipline
is an old idea
with a new mandate.
The productivity gains
that made Turbo Pascal
commercially decisive
in nineteen eighty-four
apply again
to embedded scripting,
to WebAssembly,
and to any environment
where working memory
is bounded.
The formal foundation
in coalgebraic productivity
gives the analogy
mathematical content.
The next eleven articles
walk the tradition
one topic at a time,
starting with
Niklaus Wirth's
single-pass line
in article A189.

## References

### Book

- [Brinch Hansen on Pascal Compilers][book_brinch_hansen_pascal_compilers], Per Brinch Hansen, Prentice-Hall, 1985

[book_brinch_hansen_pascal_compilers]: https://en.wikipedia.org/wiki/Per_Brinch_Hansen

### Reference

- [Anders Hejlsberg biographical entry, which cites the Computer History Museum oral history][ref_hejlsberg]
- [Turbo Pascal history and technical details][ref_turbo_pascal]
- [WebAssembly single-pass validator specification][ref_webassembly]

[ref_hejlsberg]: https://en.wikipedia.org/wiki/Anders_Hejlsberg
[ref_turbo_pascal]: https://en.wikipedia.org/wiki/Turbo_Pascal
[ref_webassembly]: https://en.wikipedia.org/wiki/WebAssembly

### Research

- [Abel and Pientka, Wellfounded Recursion with Copatterns, ICFP 2013][research_abel_pientka_copatterns]
- [Endrullis and colleagues, Productivity of Stream Definitions, Theoretical Computer Science 411, 2010][research_endrullis_productivity]
- [Haas and colleagues, Bringing the Web up to Speed with WebAssembly, PLDI 2017][research_haas_webassembly]
- [Leroy, Formal Verification of a Realistic Compiler, Communications of the ACM 52 no. 7, 2009][research_leroy_compcert]
- [Rutten, A Coinductive Calculus of Streams, Mathematical Structures in Computer Science 15, 2005][research_rutten_stream_calculus]
- [Rutten, Universal Coalgebra a Theory of Systems, Theoretical Computer Science 249, 2000][research_rutten_universal_coalgebra]

[research_abel_pientka_copatterns]: https://dl.acm.org/doi/10.1145/2500365.2500591
[research_endrullis_productivity]: https://doi.org/10.1016/j.tcs.2009.10.014
[research_haas_webassembly]: https://dl.acm.org/doi/10.1145/3062341.3062363
[research_leroy_compcert]: https://doi.org/10.1145/1538788.1538814
[research_rutten_stream_calculus]: https://doi.org/10.1017/S0960129504004517
[research_rutten_universal_coalgebra]: https://doi.org/10.1016/S0304-3975(00)00056-6
