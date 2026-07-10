---
layout: post
mathjax: false
comments: true
title:  "Developments in Programming Language Theory, A Historical Arc"
date:   2026-03-27 09:00:00 +0000
categories: programming-languages theory history
---

<!-- A206 -->
<script>console.log("A206");</script>

Programming language theory
is the intellectual project
of asking what a program means
before asking what a program does.
The project began
before the first practical compiler
and continues today
in academic conferences,
industrial toolchains,
and the small handful
of production languages
whose central design goal
is a verified property
rather than a runtime behavior.
The arc from foundations
to present-day production practice
runs about seventy years
if the count begins
with Alonzo Church's lambda calculus
of the nineteen thirties,
about fifty years
if the count begins
with the first ACM Symposium
on Principles of Programming Languages
in October nineteen seventy-three
in Boston,
Massachusetts,
and about thirty years
if the count begins
with the maturation of type theory
into an engineering discipline
in the mid nineteen nineties.
Any of the three starting points
tells a coherent story.
The story ends at the present moment.

This article opens
a ten-article back-dated series
that traces the arc
from foundations
to the current state of the practice.
The purpose of the series
is instrumental.
The historical treatment
is a scaffold
for the periodic current-event surveys
that follow the arc.
A reader who arrives
at a modern development
without the background
of Hindley-Milner unification,
Reynolds's parametricity,
or Denning's information-flow lattice
cannot judge
whether the development
is a substantive advance
or a rediscovery.
The arc supplies the background.
The current-event surveys
apply it.

The series
is not the first
back-dated historical treatment
in this corpus.
[A History of Hardware Description Languages][related_post_hdl_history]
covers the parallel arc
for the languages
that describe circuits
rather than programs,
and
[the stream-based compilers series][related_post_compilers_streaming]
covers a specific compiler-architecture tradition
across twelve articles.
The present series
is the third
sustained historical treatment,
and it consumes
the article numbers A206 through A215
across the ten consecutive days
2026-03-27 through 2026-04-05,
concluding
one day before
the stream-based compilers series
begins
at A188 on 2026-04-06.
The two blocks
form
a contiguous historical spine
running from the current article
through to
the end of April.

## Why a Chronological Treatment

The choice
of a chronological treatment
over a theme-based lineage treatment
is deliberate,
and it is worth defending.
A theme-based treatment
picks one intellectual thread,
for example the development
of type systems
from Curry through Hindley,
Milner,
Reynolds,
and Pierce
to current dependent-type practice,
and follows the thread
across every decade in which it is active.
The theme-based treatment
honors the internal logic
of each thread
but conceals
the interactions
between threads.

The chronological treatment
does the opposite.
It picks a decade
and asks
what every active thread was doing
in that decade.
The trade-off is real.
A chronological article
must break each thread
at the decade boundary
and reintroduce it
in the following article.
The gain
is the coherent picture
of a specific research moment,
which is what the reader
needs
if the destination
of the series
is a synthesis
of present-day work.

The historical eras
that this series treats
receive different levels of coverage
because
the density of substantive developments
was not the same across decades.
The nineteen seventies
receive two articles
because
the decade
delivered
Hindley-Milner inference,
denotational semantics
in the form Christopher Strachey and Dana Scott gave it,
Robin Milner's Logic for Computable Functions
and the first ML,
the earliest work
on dependent types
in Per Martin-Löf's type theory,
and the founding
of the ACM Symposium
on Principles of Programming Languages.
The nineteen eighties
receive one article
even though
Prolog matures,
the Haskell precursors form,
category theory
becomes a working tool
of language semantics,
effect systems formalize
in Gifford and Lucassen's work,
and object-oriented programming
matures
through Smalltalk
with the founding of OOPSLA
in nineteen eighty-six,
because
each of those developments
extends
rather than opens
a research direction.

## The Instrumental Destination

Every article in this series
ends
by naming
what the developments of the era
enable
in later work.
The purpose is not
antiquarian.
The purpose is to arm the reader
to read
a current-day paper
or product announcement
and immediately
place the work
against
its intellectual predecessors.

The concrete example
that motivates the series
is
information-flow control.
Denning's original nineteen seventy-six lattice paper
formalized
the mathematical structure
of information-flow constraints
in a way that lay dormant
for close to two decades.
Andrew Myers's work on JFlow at Cornell
in the late nineteen nineties,
alongside Heintze and Riecke's SLam calculus
of nineteen ninety-eight,
revived the mathematical program
in a practical form.
Sabelfeld and Myers's two thousand three survey
and Pottier and Simonet's Flow Caml
consolidated the state of the practice.
The twenty twenties
have seen
information-flow labels
appear
in production language design.
[Keleusma's information-flow-labels chapter][kel_ifc]
describes
one such adoption,
and
[an earlier article of this blog][related_post_ifc_deep_dive]
develops
the practical use of the pattern.

A reader
who arrives at Keleusma's labels
without the arc
sees a language feature.
A reader
who arrives
with the arc
sees
a nineteen seventy-six theorem
that took fifty years
to reach a production language,
and they understand
why
the intervening decades were needed.
The same story
holds
for refinement types,
for coroutine-based concurrency,
for dependent-type surface syntax,
and for the totality
and productivity
disciplines
that a modern definitive-bound language
enforces.

## The Divisions Ahead

The remaining nine articles
divide the arc
as follows.

- A207, 2026-03-28, foundations before nineteen sixty.
  Church's lambda calculus of nineteen thirty-two through nineteen forty-one,
  Curry's combinatory logic,
  Turing's nineteen thirty-six construction,
  ALGOL fifty-eight and ALGOL sixty,
  the founding papers
  that gave the field its language.
- A208, 2026-03-29, the nineteen sixties.
  Structured programming
  as a discipline,
  the first practical type systems,
  the maturation of LISP,
  ALGOL sixty-eight,
  Peter Landin's next seven hundred programming languages,
  and the earliest work
  on formal semantics.
- A209, 2026-03-30, the nineteen seventies, part one.
  Structured programming
  as a settled position,
  denotational semantics
  in the Strachey and Scott formulation,
  Dijkstra's discipline of programming,
  Pascal
  and C,
  the pragmatic side of the decade.
- A210, 2026-03-31, the nineteen seventies, part two.
  Hindley-Milner inference,
  Robin Milner's Logic for Computable Functions,
  the first ML,
  Per Martin-Löf's type theory,
  Denning's information-flow lattice,
  and the founding
  of the ACM Symposium
  on Principles of Programming Languages
  in nineteen seventy-three.
- A211, 2026-04-01, the nineteen eighties.
  Prolog matures,
  the Haskell precursors form,
  category theory
  becomes a working tool
  of language semantics,
  Standard ML solidifies as a research program,
  effect systems formalize
  in Gifford and Lucassen's work,
  and object-oriented programming
  matures
  through Smalltalk
  with the founding of OOPSLA
  in nineteen eighty-six.
- A212, 2026-04-02, the nineteen nineties.
  Haskell ships,
  effect systems mature,
  refinement types formalize
  in the Freeman-Pfenning work,
  proof assistants
  become practical,
  the International Conference on Functional Programming
  founds
  in nineteen ninety-six,
  and the second HOPL conference
  in nineteen ninety-three
  in Cambridge, Massachusetts
  produces its proceedings.
- A213, 2026-04-03, the two thousands.
  Liquid Haskell
  as the first production-oriented refinement type system,
  Coq and Agda uptake,
  the third HOPL conference
  in two thousand seven
  in San Diego,
  the ascendancy of dynamic languages,
  gradual typing
  as an intellectual project,
  and Pierce's Types and Programming Languages
  as the discipline's consolidation textbook
  in two thousand two.
- A214, 2026-04-04, the twenty tens.
  Rust's ownership discipline,
  the production adoption
  of information-flow control,
  session types
  entering industrial use,
  dependent types
  reaching industrial use
  through F-star
  and Idris,
  and the maturation
  of effect handlers.
- A215, 2026-04-05, the twenty twenties to the present.
  The fourth HOPL conference,
  originally scheduled for June twenty twenty
  and finally held
  in two thousand twenty-one,
  formal-verification pipelines
  reaching production,
  worst-case-execution-time
  as a first-class language property,
  the recent uptake
  of refinement types
  and information-flow labels
  in embedded scripting,
  and the developments
  the current-event surveys will pick up
  from.

## Recurring Threads

Every era article
in this series
carries
a set of recurring threads
that the reader can trace
across decade boundaries.
The threads are not
independent
research programs.
They interact,
and part of the value
of a chronological treatment
is showing the interactions.

The principal threads
are the following.

- Type systems.
  From Church's simply typed lambda calculus
  through Hindley-Milner
  and System F
  to dependent types
  and refinement types.
- Semantics.
  From operational reduction rules
  through Strachey and Scott's denotational program
  through Plotkin's structural operational semantics
  to modern coalgebraic and game-semantic treatments.
- Effect systems.
  From Gifford and Lucassen's original nineteen eighty-eight formulation
  through the FX language
  to modern monadic and effect-handler treatments.
- Information-flow control.
  From Bell-LaPadula and Biba in the security literature
  through Denning's nineteen seventy-six lattice
  to Jif,
  Flow Caml,
  and current production labels.
- Refinement types.
  From LCF conditioning
  through Freeman-Pfenning's nineteen ninety-one formulation
  through Liquid Haskell
  to production adoption
  in F-star
  and adjacent languages.
- Dependent types.
  From Per Martin-Löf's type theory
  through Nuprl,
  Coq,
  and Agda
  to F-star
  and Idris.
- Coroutines and productivity.
  From Conway's nineteen sixty-three formulation
  through the coalgebraic treatment
  of productivity in stream-processing languages
  to modern async and generator idioms.
- Totality analysis.
  From primitive recursive functions
  through the totality disciplines
  of proof assistants
  to definitive-bound production languages.

A reader who follows one thread
across the arc
sees
a specific intellectual project
develop.
A reader who reads
the arc chronologically
sees
which threads
were active together
at each moment.

## Ground Rules for Attribution

The series
follows
the epistemic conventions
established
in the compilers series
and the hardware description language history.
Facts,
inferences,
and hypotheses
are distinguished
explicitly.
Uncertainty markers
are stated
rather than elided.
Primary sources
are cited
where they exist.
Standard secondary references
are cited
for consolidated treatments.

The consolidated references
for this arc
are the four
History of Programming Languages
conferences,
each of which
produced
substantial proceedings.
The first,
in nineteen seventy-eight
in Los Angeles,
was chaired by Jean E. Sammet
as both general and program chair
with Richard L. Wexelblat as proceedings chair.
The second,
in nineteen ninety-three
in Cambridge, Massachusetts,
was chaired by John A. N. Lee
with Jean E. Sammet
as program chair.
The third,
in two thousand seven
in San Diego,
consolidated
another wave of developments.
The fourth,
originally scheduled for June twenty twenty
and held
in two thousand twenty-one
after the pandemic delay,
brings the record
close to the present.
The four HOPL proceedings
are the authoritative primary-source-oriented
survey documents
of the field.

Three canonical textbooks
appear
throughout the series
as consolidation-of-record references.
Benjamin C. Pierce's
Types and Programming Languages,
published
by the MIT Press
in two thousand two,
is the graduate-level type-systems reference.
Glynn Winskel's
The Formal Semantics of Programming Languages,
published
by the MIT Press
in nineteen ninety-three,
is the operational semantics reference.
John C. Reynolds's
Theories of Programming Languages,
published
by Cambridge University Press
in nineteen ninety-eight,
is the broad theoretical-basis reference
that covers imperative and functional programming
in a single treatment.
Each of the three
is cited
where the era article's development
depends on the treatment
the textbook consolidates.

The current-day publication venues
that supply the material
for the later current-event surveys
are the ACM SIGPLAN conferences.
The Symposium on Principles of Programming Languages
founded in nineteen seventy-three
publishes theory-forward work.
The International Conference on Functional Programming
founded in nineteen ninety-six
publishes functional-language work.
The Programming Language Design and Implementation conference
began in nineteen seventy-nine
as the SIGPLAN Symposium on Compiler Construction
and adopted its current name
in nineteen eighty-eight.
Object-Oriented Programming Systems Languages and Applications
founded in nineteen eighty-six
publishes object-oriented and adjacent work.
The four together
are the primary current-venue signal
that the surveys
at the end of the arc
will consume.

## How This Series Connects to the Corpus

The programming-language-theory arc
is not a standalone piece.
It sits next to
three other sustained treatments
in this corpus.

The stream-based compilers series
at
[A188 through A199][related_post_compilers_streaming]
covers
a specific compiler-architecture tradition
from Wirth's PL/0 pedagogy
of nineteen seventy-six
to the present-day
WebAssembly single-pass validator
and coroutine-based embedded-scripting family.
The current series
supplies
the intellectual context
that makes
the compiler-architecture tradition
readable.
Wirth's PL/0
is not a random choice
of a pedagogical language.
It sits in a specific place
in the type-systems
and structured-programming
threads.

The hardware description language history
at
[A200][related_post_hdl_history]
and its companion articles
at A201 through A204
cover
the parallel language tradition
for circuits.
The current series
supplies
the intellectual context
for why
the embedded-domain-specific-language revival
in the twenty tens
happened
and why it happened
in the languages it happened in.

The Keleusma articles
at
[A107][related_post_keleusma_011],
[A110][related_post_keleusma_020],
and
[A205][related_post_keleusma_022]
walk the reader
through
one specific production language
that pulls
several threads
of programming-language theory
into a single small implementation.
The current series
supplies
the intellectual context
for why
those threads
are the right threads
to pull in.

The three prior treatments
are pre-existing background
that the current series
was constructed to make legible.
A reader
who reads
the current series
first
will find
the prior treatments
better contextualized.
A reader
who reads
the current series
last
will find that it consolidates
what the prior treatments
were doing
without saying.

## What This Series Is Not

The series
is deliberately
a survey
rather than a monograph.
The genuine standard
for a monograph
on the history of programming language theory
is set
by the four HOPL proceedings
and by the graduate-level textbooks
named earlier.
This series
does not attempt
that level of depth.

The series
is also
not a substitute
for the current-event surveys
it introduces.
The historical arc
establishes the context.
The current-event surveys
consume the context
and apply it
to specific developments
as they emerge.
A reader
who wants
the current state of the practice
should read
the current-event surveys.
A reader
who wants
the historical context
that makes the current-event surveys
readable
should read
the historical arc.

The series
is also
not a Turing-award citation.
The Turing award
has been given
to individuals
whose work
shaped programming language theory,
and their names
appear
throughout the arc.
But the citations
are situated
within their intellectual moment
rather than presented
as biographical retrospectives.
A reader
who wants
biographical retrospectives
should consult
the ACM Turing Award citations directly.

## Conclusion

Programming language theory
is a coherent intellectual project
with a fifty-year to seventy-year arc,
depending on where the count begins.
The arc
runs
from Alonzo Church's lambda calculus
through the founding
of the ACM Symposium on Principles of Programming Languages
in nineteen seventy-three
in Boston,
through the maturation of type theory
into an engineering discipline,
to the current state of the practice
in which
several fifty-year-old theorems
appear
as production language features.
This series
traces that arc
in ten articles
across ten consecutive days
in a back-dated block
that ends flush
against the stream-based compilers series.
The purpose is instrumental.
The historical treatment
supplies the context
that later current-event surveys
consume.

The next article,
A207,
covers the foundations
before nineteen sixty.

## References

- [ACM SIGPLAN][ref_sigplan]
- [History of Programming Languages Conference (HOPL)][ref_hopl]
- [International Conference on Functional Programming (ICFP)][ref_icfp]
- [Object-Oriented Programming Systems Languages and Applications (OOPSLA)][ref_oopsla]
- [Pierce, Benjamin C., Types and Programming Languages, MIT Press, 2002][book_pierce_tpl]
- [Programming Language Design and Implementation (PLDI)][ref_pldi]
- [Reynolds, John C., Theories of Programming Languages, Cambridge University Press, 1998][book_reynolds_tpl]
- [Symposium on Principles of Programming Languages (POPL)][ref_popl]
- [Winskel, Glynn, The Formal Semantics of Programming Languages, MIT Press, 1993][book_winskel_semantics]
- [Related Post, A History of Hardware Description Languages][related_post_hdl_history]
- [Related Post, The Stream Processor as Compiler and the Compiler as Stream Processor][related_post_compilers_streaming]
- [Related Post, Getting Started with Keleusma 0.1.1][related_post_keleusma_011]
- [Related Post, Getting Started with Keleusma 0.2.0][related_post_keleusma_020]
- [Related Post, Getting Started with Keleusma 0.2.2][related_post_keleusma_022]
- [Related Post, Information-Flow Control, A Deep Dive with Keleusma][related_post_ifc_deep_dive]
- [Reference, Keleusma Guide, Information-Flow Labels][kel_ifc]

[book_pierce_tpl]: https://mitpress.mit.edu/9780262162098/types-and-programming-languages/
[book_reynolds_tpl]: https://www.cambridge.org/core/books/theories-of-programming-languages/19530A88F3471B2A7D9891770B21DAF9
[book_winskel_semantics]: https://mitpress.mit.edu/9780262731034/the-formal-semantics-of-programming-languages/
[kel_ifc]: https://github.com/sgeos/keleusma/blob/v0.2.1/docs/guide/24_information_flow_labels.md
[ref_hopl]: https://en.wikipedia.org/wiki/History_of_Programming_Languages_(conference)
[ref_icfp]: https://en.wikipedia.org/wiki/International_Conference_on_Functional_Programming
[ref_oopsla]: https://en.wikipedia.org/wiki/OOPSLA
[ref_pldi]: https://en.wikipedia.org/wiki/Programming_Language_Design_and_Implementation
[ref_popl]: https://en.wikipedia.org/wiki/Symposium_on_Principles_of_Programming_Languages
[ref_sigplan]: https://en.wikipedia.org/wiki/SIGPLAN
[related_post_compilers_streaming]: {% post_url 2026-04-17-stream_processor_as_compiler_and_compiler_as_stream_processor %}
[related_post_hdl_history]: {% post_url 2026-03-13-history_of_hardware_description_languages %}
[related_post_ifc_deep_dive]: {% post_url 2026-05-29-information_flow_control_deep_dive_with_keleusma %}
[related_post_keleusma_011]: {% post_url 2026-03-14-keleusma_getting_started %}
[related_post_keleusma_020]: {% post_url 2026-05-28-keleusma_0_2_0_getting_started %}
[related_post_keleusma_022]: {% post_url 2026-07-10-keleusma_0_2_2_getting_started %}
