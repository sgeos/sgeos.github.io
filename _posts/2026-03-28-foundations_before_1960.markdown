---
layout: post
mathjax: false
comments: true
title:  "Developments in Programming Language Theory, Foundations before 1960"
date:   2026-03-28 09:00:00 +0000
categories: programming-languages theory history
series: programming_language_theory
series_title: Developments in Programming Language Theory
series_index: 2
---
<!-- A207 -->
<script>console.log("A207");</script>

Programming language theory
inherits its vocabulary
from a small handful
of mathematical papers
written between nineteen thirty
and nineteen sixty.
The papers
belong to logic
and to computability theory,
not to computer science
in the modern sense,
because computer science
in the modern sense
did not yet exist.
They were written
to answer questions
about the foundations of mathematics.
They answered those questions
and,
as a side effect,
gave the discipline of programming
its central abstractions.

Every recurring thread
that
[the opener article to this series][related_post_pl_theory_arc]
named
has an origin
in this period.
Type systems trace to
Alonzo Church's simply typed lambda calculus
of the nineteen forties.
Semantics traces to
the reduction rules
Church wrote
for the untyped lambda calculus
of the nineteen thirties.
Effect systems trace to
Alan Turing's model
of state-carrying computation.
Recursive function theory
and the productivity discipline
trace to Stephen Kleene's work
on recursive functions.
Even the syntax of programming languages
traces to this period,
through John Backus's normal form
for describing ALGOL fifty-eight
and Peter Naur's extension
for ALGOL sixty.

This article
walks the pre-nineteen-sixty foundations
in the order
the papers appeared.
The order matters
because each later paper
depends on the earlier ones,
either directly
by extending them
or indirectly
by being a reaction
to their limits.

## Alonzo Church's Lambda Calculus

Alonzo Church
introduced the lambda calculus
in a nineteen thirty-two paper
in the Annals of Mathematics
titled
A Set of Postulates for the Foundation of Logic.
The paper's stated purpose
was
the construction of
a foundation for mathematical logic
free of the paradoxes
that had troubled Bertrand Russell's system.
Church's students
Stephen Kleene and John Barkley Rosser
soon proved
that the original system was inconsistent.
The subset that avoided the paradox
became
the lambda calculus
in the modern sense.

The system's central idea
is that a function
is a rule
written directly
rather than a mathematical object
extracted from a larger context.
The identity function
is written
`λx.x`.
The function that adds one to its argument
would be written
`λx.x+1`
if the calculus admitted a plus operator.
The pure calculus admits only
variables,
abstractions of the form
`λx.M`
where `M` is any term,
and applications of the form
`(M N)`
where `M` and `N` are any terms.
Everything else
is built up
from these three constructions.

Church published two further papers in nineteen thirty-six.
A Note on the Entscheidungsproblem
appeared in the Journal of Symbolic Logic
in March.
An Unsolvable Problem of Elementary Number Theory
appeared in the American Journal of Mathematics
in April.
The two papers together
proved that the decision problem
for first-order predicate calculus
is unsolvable,
which is
the negative answer
to Hilbert's Entscheidungsproblem.
The proof
depended on the lambda calculus
as its model of computation
and articulated
what came to be called
Church's thesis,
namely that
the effectively calculable functions
are exactly the lambda-definable functions.

The definitive presentation of the system
is Church's nineteen forty-one monograph
The Calculi of Lambda-Conversion,
published by Princeton University Press
as volume six
of the Annals of Mathematics Studies.
The monograph
consolidates
the reduction rules,
the confluence property,
and the equivalence
between lambda-definability
and general recursiveness.
It is the primary source
for every subsequent treatment
of the untyped lambda calculus.

Church also introduced
the simply typed lambda calculus
in a nineteen forty paper
titled
A Formulation of the Simple Theory of Types,
which appeared in the Journal of Symbolic Logic.
The simply typed calculus
adds
a type discipline
in which every variable
carries a type annotation
and every application
requires the operator's type
to match the operand's type.
The paper is the origin
of every subsequent type system
in the programming-languages literature.

## Combinatory Logic

Moses Schönfinkel
delivered a talk
in December nineteen twenty
in Göttingen
titled
Elemente der Logik.
The talk introduced
what became
combinatory logic
in its published form.
The paper
Über die Bausteine der mathematischen Logik
appeared in nineteen twenty-four
in Mathematische Annalen.
Schönfinkel's project
was
the elimination of bound variables
from mathematical logic.
He showed that
every logical expression
that uses variables
can be rewritten
as a composition
of two primitive constants,
which he named
S and K.

The K combinator
returns its first argument
and discards the second.
Its defining equation
is
`K x y = x`.
The S combinator
takes three arguments
and returns
the first applied to the third
applied to
the second applied to the third.
Its defining equation
is
`S x y z = (x z) (y z)`.
Every closed lambda expression
can be rewritten
as a combination of `S` and `K`,
so combinatory logic
and lambda calculus
compute
the same class of functions.
The equivalence
is the reason
combinatory logic
remains
a working alternative formulation
of the same computational content.

Haskell Curry
rediscovered
Schönfinkel's combinators
independently
while working as an instructor
at Princeton University
in late nineteen twenty-seven.
His nineteen thirty dissertation
Grundlagen der Kombinatorischen Logik,
published in the American Journal of Mathematics,
systematized the treatment
of combinatory logic
as an alternative foundation
to Russell's type theory.
Curry's subsequent work
extended combinatory logic
to a system
that could interpret
substantial fragments
of mathematical logic.
The definitive presentation
is
the monograph
Combinatory Logic
that Curry published
with Robert Feys
in nineteen fifty-eight.

The relationship
between combinatory logic
and lambda calculus
is
that the former
compiles the latter.
A term in the lambda calculus
can be translated
to a combinator expression
by the bracket abstraction
algorithm.
The resulting expression
uses no variables
and evaluates by reduction rules
that are structurally simpler
than the substitution rule
of the lambda calculus.
Combinatory logic
is thereby
an early example
of a target language
for a source-language compiler.

## Alan Turing's Machines

Alan Turing
introduced
what came to be called
Turing machines
in
On Computable Numbers, with an Application to the Entscheidungsproblem,
which appeared
in the Proceedings of the London Mathematical Society,
Series 2, Volume 42,
in the November thirtieth
and December twenty-third
issues
of nineteen thirty-six.
A two-page correction
appeared in the same journal,
Volume 43,
in nineteen thirty-eight.
Turing published his paper
independently of Church.
Turing added
an appendix
proving the equivalence
of his machines
with the lambda calculus,
and a fuller proof
appeared in his
nineteen thirty-seven paper
Computability and Lambda-Definability
in the Journal of Symbolic Logic.

Turing's model
is
a machine
with a finite state controller
and an infinite tape
that the controller reads from
and writes to
one cell at a time.
The controller
is defined by
a transition table
that maps
a pair of current state
and current tape symbol
to a triple of
new state,
new tape symbol,
and direction of tape motion.
The machine halts
when the transition table
has no entry
for the current pair.
A number
is computable
if a Turing machine exists
that,
starting from
a standard initial tape,
eventually halts
with the number
represented on its tape.

Turing's argument
in the paper
addressed
the same Entscheidungsproblem
that Church had addressed
in his own nineteen thirty-six papers.
Turing proved that
there is no general algorithm
that,
given a description
of a Turing machine
and an input tape,
decides
whether the machine halts.
The halting problem
is the founding negative result
of computability theory.

The Turing machine
matters
to programming language theory
for two reasons.
First,
it provides
a model of computation
that carries state
in a manifestly imperative form.
Every subsequent
imperative language
and every subsequent
operational semantics
draws on
this state-carrying picture,
directly or by analogy.
Second,
it provides
the definitional standard
for what an algorithm is.
A language
is Turing-complete
if it can simulate
an arbitrary Turing machine,
and the notion of Turing-completeness
is
the terminological anchor
for expressiveness comparisons
between languages.

## The Church-Turing Equivalence

Church and Turing
worked independently.
Church's lambda calculus
and Turing's machine
were shown to be equivalent
in nineteen thirty-six
and nineteen thirty-seven.
The equivalence
established
that the class of computable functions
does not depend
on the model chosen.
Recursive functions,
lambda-definable functions,
and Turing-computable functions
are the same class.

The mathematical equivalence
between the three formulations
is a theorem.
The Church-Turing thesis
is a stronger claim,
that this shared class of functions
is exactly
the class of effectively calculable functions
in the informal sense.
In its strongest form,
which treats
the class as
the class of physically realizable computations,
the thesis
remains a conjecture
rather than a theorem.
The three original formulations
converge
on the same class of functions
by mathematical proof.
Whether that class is
the class of all possible computations
is a separate,
still-open,
question.

The equivalence
is
the reason
programming language theory
does not need
to choose
between the imperative
and the functional
picture
as the foundation
of the discipline.
Either picture
suffices.
The choice
is
a matter of engineering convenience,
of what a specific language
is designed to make easy.

## Recursive Function Theory

Kurt Gödel
introduced
the class of general recursive functions
in a nineteen thirty-four
Princeton lecture series
at the Institute for Advanced Study.
Stephen Kleene
and John Barkley Rosser
took notes,
which the Institute
mimeographed and distributed
under the title
On Undecidable Propositions
of Formal Mathematical Systems.
Gödel's construction
built on
Jacques Herbrand's earlier work
on definitions by equations.
Stephen Kleene
subsequently
extended and refined
the treatment
in his nineteen thirty-six paper
General Recursive Functions of Natural Numbers,
published
in Mathematische Annalen.
Kleene's nineteen fifty-two monograph
Introduction to Metamathematics
became
the standard graduate-level reference
for recursive function theory.

Recursive function theory
matters
to programming language theory
in three ways.
First,
it supplies
a third equivalent characterization
of the computable functions,
alongside Church's lambda calculus
and Turing's machines.
Second,
the primitive recursive functions,
which form
a proper subclass
of the general recursive functions,
are
the historical origin
of the totality analyses
that modern definitive-bound languages
enforce.
A function that is
primitive recursive
is
provably total.
Third,
the recursion theorems
that Kleene proved
are
the technical basis
for reasoning about
fixed points,
self-reference,
and the semantics
of recursive definitions
in later work.

## The Stored-Program Architecture

John von Neumann's
First Draft of a Report on the EDVAC,
completed on June thirtieth
nineteen forty-five,
consolidated
the design principle
that a machine's program
and its data
should share
the same memory
and be encoded
in the same form.
The report
drew on
work by
J. Presper Eckert
and John William Mauchly
at the Moore School
of the University of Pennsylvania,
where the ENIAC was being built
and the EDVAC
was being designed.
The First Draft
was
an internal report
rather than a formal publication,
and its attribution
has been contested
because Eckert and Mauchly's contributions
predate the report.
The report
nevertheless became
the disseminating document
for the stored-program architecture.

The stored-program architecture
matters
to programming language theory
because
it makes
the identification
of programs with data
concrete
at the machine level.
A compiler
that reads a source program
as input
and writes an executable program
as output
is
a program
that computes on programs.
The stored-program picture
provides
the operational substrate
that makes this identification
routine.
Church's lambda calculus
had already established
the identification
at the mathematical level.
The stored-program architecture
made it engineering fact.

## FORTRAN

John Backus
proposed
what became FORTRAN
in a November nineteen fifty-three
memorandum
to his manager
at International Business Machines.
The language definition
was completed
in late nineteen fifty-four.
The compiler
was programmed and tested
across nineteen fifty-five
and nineteen fifty-six.
The FORTRAN Automatic Coding System
for the International Business Machines seven oh four
shipped
to customers
in April nineteen fifty-seven.

FORTRAN
was
not the first
high-level programming language.
Grace Hopper's A-0 system
of nineteen fifty-one,
Alick Glennie's Autocode
of nineteen fifty-two
for the Manchester Mark One,
and other early systems
predated it.
FORTRAN was
the first
high-level language
whose compiler
produced code
that ran
comparably to
hand-written assembly.
Backus's team
implemented
an aggressive optimizing compiler
whose output
was
within a small constant factor
of what a human programmer
could write directly.
The comparable-performance property
was
what made
high-level programming
economically viable.

FORTRAN
matters
to programming language theory
for a specific reason.
It established
the principle
that a language
can be more abstract than
the machine it runs on
without
paying an unacceptable performance cost.
Every subsequent optimizing compiler
is
downstream
of the FORTRAN demonstration.
The FORTRAN team
also introduced
several ideas
that later became standard,
including
loop-invariant code motion,
common-subexpression elimination,
strength reduction
on index expressions,
and register allocation
by ad hoc heuristics
that later work
would supersede
with graph-coloring approximations.

## LISP

John McCarthy
began developing LISP
at the Massachusetts Institute of Technology
in late nineteen fifty-eight.
The language
grew out of
his effort
to define
a computable analogue
of the recursive functions
that operate on
symbolic expressions
rather than on numbers.
The seminal paper
Recursive Functions of Symbolic Expressions
and Their Computation by Machine, Part One
appeared
in Communications of the ACM,
Volume 3,
Number 4,
in April nineteen sixty.
Part Two
was never published.

LISP's central data structure
is
the cons pair,
a two-field record
whose fields
hold either atoms
or other cons pairs.
The language
uses
the same notation
for programs
and for data,
so a program
is a list
that can be manipulated
by other programs.
The identification
of program with data
is Church's identification
made syntactically direct.
The property
is the basis
for LISP macros
and for
the metacircular evaluator,
which is
the definition
of the LISP evaluator
in LISP itself.

The nineteen sixty paper
introduced
automatic memory management
through garbage collection.
Steve Russell,
McCarthy's student,
had implemented
the first working LISP interpreter
in nineteen fifty-nine
by hand-translating
McCarthy's eval function
into assembly code
for the International Business Machines seven oh four.
The interpreter
demonstrated
that the metacircular evaluator
was executable
in practice
rather than only
notational.

LISP
matters
to programming language theory
in several ways.
The garbage-collection technique
became
the standard memory-management strategy
for functional languages,
for many object-oriented languages,
and for
most modern scripting languages.
The identification of program with data
became
the foundation
of macro systems
in the Scheme,
Common Lisp,
and Racket
traditions.
The metacircular evaluator
became
the pedagogical template
for understanding
how an interpreter works,
which
Harold Abelson and Gerald Sussman
would later make canonical
in
Structure and Interpretation of Computer Programs.

## ALGOL 58 and Backus-Naur Form

A joint committee
of the American Association for Computing Machinery
and the German Society for Applied Mathematics and Mechanics,
the Gesellschaft für Angewandte Mathematik und Mechanik,
met at the Federal Institute of Technology
in Zurich
from May twenty-seventh to June second
of nineteen fifty-eight.
The German-side delegation
was
Friedrich Bauer,
Hermann Bottenbruch,
Heinz Rutishauser,
and Klaus Samelson.
The American-side delegation
was
John Backus,
Charles Katz,
Alan Perlis,
and Joseph Wegstein.
The committee
produced
the preliminary report
on
the International Algebraic Language,
which was subsequently
renamed ALGOL,
which stood for
Algorithmic Language.
The preliminary specification
was published
in December nineteen fifty-eight
and became known
as ALGOL fifty-eight.

ALGOL fifty-eight
introduced
several features
that became standard
in subsequent languages,
including
block structure,
lexical scope,
and
call-by-name parameter passing.
The language
was intended
as a publication language
for algorithms
rather than as an implementation language,
and its specification
therefore emphasized
readability
and precision
over ease of compilation.

The language description
posed
a specific problem
for the committee.
Existing programming languages
were described
in natural language prose
with representative examples,
which
left ambiguities
that different implementers
resolved differently.
John Backus
proposed
a formal notation
for describing
the syntax
of the language.
His nineteen fifty-nine paper
The Syntax and Semantics of the Proposed
International Algebraic Language
of the Zurich ACM-GAMM Conference,
delivered
at the International Conference
on Information Processing in Paris,
introduced
what he called
the metalinguistic formulae.
Peter Naur
revised the notation
for the ALGOL sixty report
and it became known
as Backus normal form.
Donald Knuth
argued in a
nineteen sixty-four letter
to Communications of the ACM
that Backus normal form
was not
a normal form
in any technical sense.
Knuth proposed
the rename
to Backus-Naur form
to credit Naur
and preserve
the abbreviation,
and the rename prevailed.

A Backus-Naur form production
has
the shape
`<nonterminal> ::= <alternative-1> | <alternative-2> | ...`,
where each alternative
is a sequence of nonterminals
and terminal symbols.
The notation
is
a context-free grammar
in a specific syntactic dress.
It is
the origin
of every subsequent
formal syntax specification
in programming language theory.
Every parser generator,
every language reference manual
that carries a grammar section,
and every proof-assistant formalization
of a language syntax
descends from
the metalinguistic formulae
that Backus introduced
in nineteen fifty-nine.

## ALGOL 60

The joint committee
reconvened
in Paris
from January eleventh to sixteenth
of nineteen sixty.
The thirteen-member committee
included
John Backus,
Friedrich Bauer,
and several delegates
from the ALGOL fifty-eight process.
Peter Naur
served as
editor and rapporteur.
The Report on the Algorithmic Language ALGOL 60
was published
in May nineteen sixty
in Communications of the ACM
and simultaneously
in the German journal
Numerische Mathematik.
A revised report
was published
in Communications of the ACM
in January nineteen sixty-three.

ALGOL sixty
consolidated
the innovations
of ALGOL fifty-eight
into a complete language definition
that included
recursion,
lexically scoped local variables,
dynamic array allocation,
and
a formal syntax
in Backus-Naur form.
The language
was
never widely used
as an industrial implementation language,
but it became
the reference notation
for algorithm publication
in the ACM literature
for two decades.
Every ACM algorithm publication
until the mid nineteen eighties
appeared
in an ALGOL sixty subset.

ALGOL sixty
matters
to programming language theory
because it consolidated
the discipline's technical vocabulary.
The terms
block structure,
lexical scope,
call-by-value,
call-by-name,
type declaration,
formal parameter,
and actual parameter
appear
in the ALGOL sixty report
in the sense
they carry today.
Every subsequent programming language
either extends
the ALGOL sixty vocabulary
or explicitly rejects it.
The report
is
the vocabulary reference
for the next fifty years
of language design.

## What This Era Enables

The pre-nineteen-sixty foundations
supply
the mathematical and terminological infrastructure
that the nineteen sixties
will use
to consolidate
programming language theory
as a research discipline.
Specifically,
the era supplies
three things
that
the next article in this series
will pick up.

First,
two independent
mathematical models of computation,
the lambda calculus
and the Turing machine,
that
were proved equivalent
in nineteen thirty-six
and nineteen thirty-seven.
The equivalence
underwrites
the discipline's ability
to move
between imperative
and functional
formulations
without loss of expressive power.

Second,
a small but growing
set of practical high-level languages,
FORTRAN,
LISP,
and ALGOL fifty-eight,
that
demonstrated
the feasibility
of programming above
the machine-code level.
The demonstrations
made the discipline
economically defensible.
Before them,
high-level programming
was an academic curiosity.
After them,
it was
an industrial necessity.

Third,
a formal notation
for describing language syntax,
namely
Backus-Naur form,
which
made it possible
to state precisely
what a language is
rather than to convey it
by example.
The notation
is
the essential enabler
of every subsequent
formal-semantics program,
which
the next article will begin to develop.

## Conclusion

Programming language theory
before nineteen sixty
was
not yet
programming language theory.
It was
mathematical logic,
computability theory,
and
early computer engineering,
each pursuing
its own questions.
The questions
converged
on a small set of shared objects,
namely
computable functions,
formal syntax,
and stored-program machines,
that
would
become
the material
of the discipline
in the next decade.

The next article,
A208,
covers
the nineteen sixties.

## References

- [Backus, John, The Syntax and Semantics of the Proposed International Algebraic Language of the Zurich ACM-GAMM Conference, ICIP Paris, 1959][paper_backus_syntax]
- [Church, Alonzo, A Set of Postulates for the Foundation of Logic, Annals of Mathematics 33, 1932][paper_church_postulates]
- [Church, Alonzo, An Unsolvable Problem of Elementary Number Theory, American Journal of Mathematics 58, 1936][paper_church_unsolvable]
- [Church, Alonzo, A Formulation of the Simple Theory of Types, Journal of Symbolic Logic 5, 1940][paper_church_simple_types]
- [Church, Alonzo, The Calculi of Lambda-Conversion, Princeton University Press, 1941][book_church_calculi]
- [Curry, Haskell B., Grundlagen der Kombinatorischen Logik, American Journal of Mathematics 52, 1930][paper_curry_grundlagen]
- [Curry, Haskell B. and Feys, Robert, Combinatory Logic, North-Holland, 1958][book_curry_feys]
- [Kleene, Stephen C., General Recursive Functions of Natural Numbers, Mathematische Annalen 112, 1936][paper_kleene_recursive]
- [Kleene, Stephen C., Introduction to Metamathematics, North-Holland, 1952][book_kleene_intro]
- [McCarthy, John, Recursive Functions of Symbolic Expressions and Their Computation by Machine, Part I, CACM 3, 1960][paper_mccarthy_lisp]
- [Naur, Peter (editor), Report on the Algorithmic Language ALGOL 60, CACM 3, 1960][paper_naur_algol60]
- [Perlis, Alan and Samelson, Klaus (editors), Preliminary Report on ALGOL 58, CACM 1, 1958][paper_algol58_preliminary]
- [Schönfinkel, Moses, Über die Bausteine der mathematischen Logik, Mathematische Annalen 92, 1924][paper_schonfinkel]
- [Turing, Alan, On Computable Numbers, with an Application to the Entscheidungsproblem, Proceedings of the London Mathematical Society 42, 1936][paper_turing_computable]
- [von Neumann, John, First Draft of a Report on the EDVAC, Moore School, University of Pennsylvania, 1945][paper_vonneumann_edvac]
- [Related Post, Programming Language Theory as a Historical Arc][related_post_pl_theory_arc]

[book_church_calculi]: https://press.princeton.edu/books/paperback/9780691083940/the-calculi-of-lambda-conversion-am-6-volume-6
[book_curry_feys]: https://en.wikipedia.org/wiki/Combinatory_logic
[book_kleene_intro]: https://en.wikipedia.org/wiki/Stephen_Cole_Kleene
[paper_algol58_preliminary]: https://en.wikipedia.org/wiki/ALGOL_58
[paper_backus_syntax]: https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form
[paper_church_postulates]: https://www.jstor.org/stable/1968337
[paper_church_simple_types]: https://en.wikipedia.org/wiki/Simply_typed_lambda_calculus
[paper_church_unsolvable]: https://www.jstor.org/stable/2371045
[paper_curry_grundlagen]: https://en.wikipedia.org/wiki/Combinatory_logic
[paper_kleene_recursive]: https://en.wikipedia.org/wiki/General_recursive_function
[paper_mccarthy_lisp]: https://dl.acm.org/doi/10.1145/367177.367199
[paper_naur_algol60]: https://en.wikipedia.org/wiki/ALGOL_60
[paper_schonfinkel]: https://en.wikipedia.org/wiki/Combinatory_logic
[paper_turing_computable]: https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/plms/s2-42.1.230
[paper_vonneumann_edvac]: https://en.wikipedia.org/wiki/First_Draft_of_a_Report_on_the_EDVAC
[related_post_pl_theory_arc]: {% post_url 2026-03-27-programming_language_theory_as_a_historical_arc %}
