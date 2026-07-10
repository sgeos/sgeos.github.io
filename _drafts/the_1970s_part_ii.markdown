---
layout: post
mathjax: false
comments: true
title:  "Developments in Programming Language Theory, The 1970s Part II"
date:   2026-03-31 09:00:00 +0000
categories: programming-languages theory history
---

<!-- A210 -->
<script>console.log("A210");</script>

The theoretical side of the nineteen seventies
took
the mathematical foundations
that
[the nineteen sixties][related_post_a208]
had established
and produced
a small number
of specific technical results
that the following four decades
would develop.
Hindley's principal type theorem
and its independent rediscovery
by Milner
gave the discipline
its first practical type inference algorithm.
Milner's Logic for Computable Functions
gave the discipline
its first interactive theorem prover
and,
as a side effect,
the first ML.
Per Martin-Löf's intuitionistic type theory
extended
the type-theoretic foundations
to
dependent types
and
supplied
a foundation
for constructive mathematics
that
subsequent proof assistants
would implement.
Dorothy Denning's lattice model
of information flow
supplied
the mathematical structure
that
production information-flow-control languages
of the twenty tens
and twenty twenties
would eventually adopt.
William Howard's manuscript
on the correspondence
between formulas and types
made explicit
a specific structural analogy
that would organize
type theory
for the rest of the century.
The ACM Symposium
on Principles of Programming Languages
founded
in October of the same decade
became
the primary venue
in which
all of this work
was published.

The [companion article][related_post_a209]
covers
the pragmatic side of the same decade.
The reader
should treat the two articles
as
a single treatment
in two parts.

## The Founding of the Symposium on Principles of Programming Languages

The first ACM Symposium
on Principles of Programming Languages
was held
in Boston,
Massachusetts,
in October
of nineteen seventy-three.
Patrick C. Fischer
and Jeffrey D. Ullman
edited the proceedings.
The symposium
was
a joint venture
of
the ACM Special Interest Group on Programming Languages
and
the ACM Special Interest Group on Algorithms
and Computation Theory.

The founding of a dedicated symposium
for theoretical work
on programming languages
was a substantive editorial statement.
It asserted
that
programming language theory
was
a distinct research discipline
with
its own methods
and
its own publication venues,
separate from
compiler construction,
which
already had
the SIGPLAN Symposium
on Compiler Construction
that became PLDI
in the nineteen eighties,
and separate from
software engineering,
which
would develop
its own venues
across the following decade.

The symposium's first several years
established
the format
that the venue
continues to use.
Papers
are rigorously refereed
against
a bar
that emphasizes
technical novelty
and
mathematical precision.
The symposium
did not
publish
tool papers
or
experience reports
in its first years,
and
the emphasis on
theoretical content
remains
its distinguishing characteristic
against
adjacent venues.

The founding
of the symposium
supplied
the discipline
with
a permanent record
of its work.
Every article in the remainder of this series
that names
a specific technical result
from
the nineteen seventies onward
either
was published
in the proceedings
of the symposium
or
was published
in a venue
that
the symposium
established
as a peer standard.

## Hindley's Principal Type Theorem

J. Roger Hindley
published
The Principal Type-Scheme
of an Object
in Combinatory Logic
in
the Transactions
of the American Mathematical Society,
volume one hundred forty-six,
pages twenty-nine
through sixty,
in nineteen sixty-nine.
The paper
proved
a specific result
about
combinatory logic
that would become
the foundation
of type inference
in
statically typed
functional programming languages.

The result
concerns
what happens
when
a term of combinatory logic
is asked
what type it has.
A term
may have
many types.
The identity combinator,
for example,
maps
any type
to itself,
so it has
the type
`Nat → Nat`,
the type
`Bool → Bool`,
the type
`(Nat → Nat) → (Nat → Nat)`,
and infinitely many others.
Hindley's theorem
established that
these types
are not
unrelated.
They are
all instances
of
a single most general type,
written
`∀α. α → α`,
which
the theorem
called
the principal type-scheme.
The principal type-scheme
is unique
up to renaming
of its bound variables.
Every other type
that a term admits
is
an instance of the principal type-scheme
obtained by
substituting concrete types
for
the bound variables.

The theorem
gave
an algorithm
for computing
the principal type-scheme
from
the term.
The algorithm
performs
unification
of type expressions
against
a set of constraints
derived from
the term's structure.
Robinson's nineteen sixty-five paper
A Machine-Oriented Logic
Based on the Resolution Principle
had supplied
the unification algorithm.
Hindley applied it
to the type-inference problem.

The paper
was
not
widely read
in
the programming languages community
at
the time
of its publication.
Its content
became influential
through
Robin Milner's independent rediscovery
of
the same result
almost a decade later.

## Robin Milner's Logic for Computable Functions

Robin Milner
had joined
the Stanford University
Artificial Intelligence Laboratory
in
the late nineteen sixties.
His nineteen seventy-two technical report,
Logic for Computable Functions,
Description of a Machine Implementation,
distributed as
Stanford Artificial Intelligence Laboratory Memo AIM-169,
introduced
the Logic for Computable Functions system,
which
came to be called
Edinburgh LCF
after
Milner moved to
the University of Edinburgh
in nineteen seventy-three
and continued
the work there.

The Logic for Computable Functions
was
a formal logic
that Dana Scott
had proposed
in
an unpublished nineteen sixty-nine note.
Scott's logic
extended
first-order predicate calculus
with
constructions
for
computable partial functions
over
recursively defined domains.
The logic
was
intended
as
a mathematical foundation
for
reasoning about
the meanings
of programs
in
the Scott-Strachey denotational-semantic style
that
[the companion article][related_post_a209]
develops.
Milner's LCF system
was
the first
mechanical implementation
of Scott's logic.

The system
allowed
a user
to
interactively
generate
formal proofs
about
recursively defined functions.
Proofs
were constructed
by
applying inference rules
of the logic
to
previously proved theorems.
The system
maintained
a data structure
representing
the current goal
and
the accumulated proof,
and
provided
commands
for extending the proof
by
one inference step
at a time.

The system's principal innovation
was
the tactic mechanism.
A tactic
was
a program
that
transformed
a goal
into
a list of subgoals
whose proofs
would together
suffice
to prove the original goal.
Tactics
could be
combined
using
tacticals,
which were
higher-order operations
on tactics
that
allowed
complex proof strategies
to be
constructed
from simple ones.
The tactic mechanism
required
a programming language
in which
tactics
could be written.
That language
was ML.

## The First ML

ML,
which stood for
Meta Language,
was
the language
in which
LCF tactics
were written.
Milner and his collaborators
at Edinburgh
designed the language
across
the mid nineteen seventies.
The formal type-system foundations
of the language
appeared
in
a nineteen seventy-eight paper
by Milner
titled
A Theory of Type Polymorphism in Programming
in
the Journal of Computer and System Sciences,
volume seventeen,
pages three hundred forty-eight
through three hundred seventy-four.
The paper
independently
rediscovered
the Hindley principal type theorem
and
supplied
a type-inference algorithm
that
came to be called
Algorithm W.
A complete description
of the language
appeared in
the nineteen seventy-nine book
Edinburgh LCF
by Michael Gordon,
Robin Milner,
and Christopher Wadsworth,
published by
Springer.

Algorithm W
takes
a term
without type annotations
and computes
its principal type-scheme.
The algorithm
proceeds
by
recursive descent
on
the term structure,
generating
type constraints
at each application
and each abstraction,
and solving
the constraints
by
unification
at the end.
The algorithm
succeeds
if the term is well-typed
and fails
if the term is not,
and its
output
is
the most general type
that
the term admits.

The Hindley-Milner type system,
which ML implements,
has
a specific technical property
that makes
type inference
practical.
The property
is
that
principal types exist
and can be computed
without
annotation.
A programmer
can write
`fn x => x`
in ML
and the compiler
determines that
the function
has type
`∀α. α → α`
without
any type declaration.
The property
distinguishes
Hindley-Milner
from
the more powerful System F,
in which
principal types
do not exist
in general
and
type inference
is undecidable.

The trade-off
that Hindley-Milner accepts
is
that
not every well-typed program
can be
expressed
in
its type system.
Programs
that require
higher-rank polymorphism
or
existential types
cannot
be inferred
by Algorithm W.
Modern successors,
including
Haskell,
provide
type-annotation escape hatches
that
extend
the inferable fragment
to
cover more expressive types
at the cost
of
requiring
annotations
for
the extended fragment.

Luis Damas,
Milner's doctoral student
at Edinburgh,
supplied
the formal soundness proof
of Algorithm W
in
a nineteen eighty-two joint paper with Milner
at
the Symposium on Principles of Programming Languages
and
in
his nineteen eighty-five doctoral dissertation.
The Damas-Milner soundness proof
established that
Algorithm W
computes
the principal type-scheme
correctly
and
that
principal types
have
the expected substitution property.
The algorithm
is now
called
Hindley-Damas-Milner
or
Damas-Milner
in the formal-methods literature
to acknowledge
Damas's contribution.

## Per Martin-Löf's Intuitionistic Type Theory

Per Martin-Löf
delivered
a lecture series
in
nineteen seventy-one
that
introduced
a type theory
intended
as
a foundation
for
constructive mathematics.
The original nineteen seventy-one formulation
was
impredicative,
meaning
that it included
a type of all types
that could
quantify over
itself.
Jean-Yves Girard
proved
that
the impredicative formulation
was
inconsistent
using
a variant
of
the Burali-Forti paradox.
Martin-Löf
revised
the theory
in
nineteen seventy-two
to
a predicative formulation
that
avoided
self-reference
by
introducing
a hierarchy
of universes,
each of which
contained
types
of
lower universes.

The predicative formulation
was
presented
at
the nineteen seventy-three Logic Colloquium
and
published
in nineteen seventy-five
in
the Logic Colloquium '73 proceedings
under the title
An Intuitionistic Theory of Types,
Predicative Part.
The theory
included
dependent types,
which
are
types
that depend
on
values.
The dependent function type,
written
`Π (x : A). B(x)`,
is
the type of functions
that
take
a value `x` of type `A`
and return
a value
of type `B(x)`,
where `B(x)`
is
a type
that depends
on `x`.
The dependent pair type,
written
`Σ (x : A). B(x)`,
is
the type of pairs
whose first component
is
a value `x` of type `A`
and whose second component
is
a value
of type `B(x)`.

Dependent types
were
a substantial extension
of
the simply typed lambda calculus
that
[the foundations article][related_post_a207]
described.
The simply typed lambda calculus
distinguishes
values
from
types
and treats them
as
separate levels.
Martin-Löf's type theory
collapses the distinction.
A type
is
a value
that lives
in
a universe.
A value
that a function takes
can be
a type.
The collapse
allowed
mathematical propositions
to be
expressed
as
types,
and
proofs of propositions
to be
expressed
as
values of the corresponding types.

Martin-Löf published
the definitive presentation
of the theory
in
his nineteen eighty-four book
Intuitionistic Type Theory,
based on
notes
by Giovanni Sambin
from
a lecture series
in Padua.
The book
became
the standard reference
for
the theory
and
the basis
for
the Agda,
Coq,
and Lean
proof assistants
of
subsequent decades.

## The Curry-Howard Correspondence Formalized

Haskell Curry
had noted
in
his nineteen fifty-eight book
Combinatory Logic
that
there was
a structural analogy
between
the types
of
combinators
and
the propositions
of
intuitionistic propositional logic.
The type of the K combinator,
namely
`A → B → A`,
was
the same
as
the axiom
`A ⊃ (B ⊃ A)`
of
intuitionistic propositional logic.
Curry's observation
was
suggestive
but
not
formally developed.

William Howard
formalized
Curry's observation
into
a full correspondence
in
a manuscript
titled
The Formulae-as-Types Notion of Construction,
written
in nineteen sixty-nine
and
circulated
as a xeroxed copy
among
type theorists
for the next decade.
The manuscript
was
not
published
until
nineteen eighty,
when
it appeared
in
the Festschrift volume
To H. B. Curry,
Essays on Combinatory Logic,
Lambda Calculus and Formalism,
edited by
Jonathan Seldin
and J. Roger Hindley.

Howard's correspondence
established
a specific systematic connection.
Propositions
of intuitionistic propositional logic
correspond
to types
of the simply typed lambda calculus.
Proofs
of propositions
correspond
to terms
of the corresponding types.
Proof normalization
corresponds
to
beta reduction
of the corresponding term.
The correspondence
extends
to intuitionistic predicate logic
and
Martin-Löf's dependent type theory
in
a natural way,
so that
universal quantification
`∀x. P(x)`
corresponds
to
the dependent function type
`Π (x : A). B(x)`
and
existential quantification
`∃x. P(x)`
corresponds
to
the dependent pair type
`Σ (x : A). B(x)`.

The correspondence
is
the foundation
of
the modern
proof-assistant program.
A proof assistant
that
implements
Martin-Löf-style dependent type theory,
including
Agda,
Coq,
Lean,
and F-star,
uses
the correspondence
to
allow
a user
to
construct
a proof of a proposition
by
writing
a term
of the corresponding type.
The type checker
verifies
that
the term
has
the claimed type,
which
by the correspondence
is
the claim
that
the term
proves
the proposition.
Type checking
and
proof checking
are
the same operation.

## Denning's Information-Flow Lattice

Dorothy Denning
published
A Lattice Model
of Secure Information Flow
in
Communications of the ACM
volume nineteen,
pages two hundred thirty-six
through two hundred forty-three,
in May
of nineteen seventy-six.
The paper
formalized
the mathematical structure
of information-flow constraints
in a way
that
would
lay dormant
for
close to two decades
before
production programming languages
adopted it.

The paper's central object
is
a lattice
`(L, ≤, ⊕, ⊗)`,
where
`L` is a set of security classes,
`≤` is a partial order on the security classes,
`⊕` is the least upper bound operation,
and
`⊗` is the greatest lower bound operation.
A program
respects
the lattice
if information
flowing from
a value
of security class `x`
to
a value
of security class `y`
requires
`x ≤ y`,
namely
that
the source class
is
at or below
the destination class
in the partial order.
The condition
prohibits
information
from flowing
upward
in the lattice
to
a class
that
does not
already
contain
that information.

The paper
gave
a specific example lattice
for
a two-level security system
with classes
public and private,
in which
public information
can flow
to private
but
private information
cannot flow
to public.
The general lattice
handles
more complex classification schemes
that
distinguish
between
different secrecy categories
and
different integrity levels,
each of which
forms
its own dimension
in the lattice.

The paper
also
gave
a static analysis
that
verifies
whether
a program
respects
the lattice.
The analysis
traces
the information flow
through
assignments,
conditionals,
and loops,
and
computes
for each value
in the program
a security class
that
represents
the maximum classification
of information
that
could have flowed
into
that value.
The analysis
rejects
a program
that
requires
an information flow
that
the lattice
prohibits.

The paper
was
substantially
ahead of
the state
of practical programming languages
at
the time
of its publication.
Production programming languages
of
the nineteen seventies
and nineteen eighties
did not
carry
information-flow types.
The paper's mathematical apparatus
would
begin
to see
practical use
in
the late nineteen nineties
when
Andrew Myers
built
JFlow
at the Massachusetts Institute of Technology
as
his doctoral work
and,
subsequently,
Jif
at Cornell,
both
on the Denning foundation,
and
would
reach production adoption
in
the twenty twenties
in
languages
such as
Keleusma
that
carry
information-flow labels
in
the surface type system.
The article after next in this series,
A212,
develops
the nineteen nineties adoption.
The article on the twenty twenties,
A215,
develops
the production adoption.

## What This Era Enables

The theoretical side of the nineteen seventies
supplied
five things
that
the following decades
consumed.

First,
type inference
as
a practical technique,
through
the Hindley-Milner algorithm.
Every statically typed
functional language
after ML
either
uses
Hindley-Milner
directly
or
extends it
with
annotation escape hatches
for
more expressive types.

Second,
the tactic mechanism
for
interactive theorem proving,
through
LCF.
Every subsequent
interactive theorem prover,
including
HOL,
Isabelle,
Coq,
Agda,
Lean,
and F-star,
uses
tactic-based proof construction
in
the LCF tradition.

Third,
dependent types
as
a foundation
for
proof assistants,
through
Martin-Löf's theory.
Every modern proof assistant
that supports
mathematical propositions
as
types
implements
some fragment
of
Martin-Löf's theory.

Fourth,
the Curry-Howard correspondence
as
the organizing principle
of
the proof-assistant program.
The identification
of
proofs with programs
allowed
the type-checker
to serve
as
the proof-checker,
which
made
the following decades
of
mechanized mathematics
practical.

Fifth,
the information-flow lattice
as
the mathematical foundation
for
security-typed programming languages.
The Denning apparatus
lay dormant
for
close to two decades
before
practical uptake
began.

The next article,
A211,
covers
the nineteen eighties.

## Conclusion

The theoretical side of the nineteen seventies
established
five research programs
that
the following decades
would develop.
Type inference
became
Hindley-Milner
and
its extensions.
Interactive theorem proving
became
the LCF tradition
of tactics.
Dependent types
became
Martin-Löf's theory
and
its implementations.
The correspondence
between formulas and types
became
the organizing principle
of
proof assistants.
The information-flow lattice
became
the foundation
that
production information-flow languages
would eventually adopt.

None of these
were
production techniques
in
the nineteen seventies.
All of them
were
established results
by the end of the decade,
and
each of them
would
develop
into
a working discipline
over
the following forty years.

The next article,
A211,
covers
the nineteen eighties.

## References

- [Damas, Luis and Milner, Robin, Principal Type-Schemes for Functional Programs, POPL, 1982][paper_damas_milner]
- [Gordon, Michael J., Milner, Robin, and Wadsworth, Christopher P., Edinburgh LCF, A Mechanised Logic of Computation, Springer LNCS 78, 1979][book_edinburgh_lcf]
- [Damas, Luis, Type Assignment in Programming Languages, PhD Thesis, University of Edinburgh, 1985][thesis_damas]
- [Denning, Dorothy E., A Lattice Model of Secure Information Flow, CACM 19, 1976][paper_denning_lattice]
- [Hindley, J. Roger, The Principal Type-Scheme of an Object in Combinatory Logic, Transactions of the American Mathematical Society 146, 1969][paper_hindley]
- [Howard, William A., The Formulae-as-Types Notion of Construction, in To H. B. Curry, Essays on Combinatory Logic, Lambda Calculus and Formalism, Academic Press, 1980][paper_howard]
- [Martin-Löf, Per, An Intuitionistic Theory of Types, Predicative Part, in Logic Colloquium '73, North-Holland, 1975][paper_martinlof_1975]
- [Martin-Löf, Per, Intuitionistic Type Theory, Bibliopolis, 1984][book_martinlof_1984]
- [Milner, Robin, Logic for Computable Functions, Description of a Machine Implementation, Stanford AI Memo AIM-169, 1972][paper_milner_lcf]
- [Milner, Robin, A Theory of Type Polymorphism in Programming, Journal of Computer and System Sciences 17, 1978][paper_milner_polymorphism]
- [Robinson, J. A., A Machine-Oriented Logic Based on the Resolution Principle, Journal of the ACM 12, 1965][paper_robinson_resolution]
- [Scott, Dana S., A Type-Theoretical Alternative to ISWIM, CUCH, OWHY, unpublished note, 1969][paper_scott_lcf_note]
- [Symposium on Principles of Programming Languages, first held Boston, October 1973][ref_popl]
- [Related Post, Programming Language Theory as a Historical Arc][related_post_a206]
- [Related Post, Foundations before 1960][related_post_a207]
- [Related Post, The 1960s][related_post_a208]
- [Related Post, The 1970s Part I][related_post_a209]

[book_martinlof_1984]: https://en.wikipedia.org/wiki/Intuitionistic_type_theory
[paper_denning_lattice]: https://dl.acm.org/doi/10.1145/360051.360056
[paper_hindley]: https://en.wikipedia.org/wiki/Hindley%E2%80%93Milner_type_system
[paper_howard]: https://en.wikipedia.org/wiki/Curry%E2%80%93Howard_correspondence
[paper_martinlof_1975]: https://en.wikipedia.org/wiki/Intuitionistic_type_theory
[paper_milner_lcf]: https://en.wikipedia.org/wiki/Logic_for_Computable_Functions
[paper_milner_polymorphism]: https://en.wikipedia.org/wiki/Hindley%E2%80%93Milner_type_system
[paper_robinson_resolution]: https://en.wikipedia.org/wiki/Robinson%27s_resolution
[paper_scott_lcf_note]: https://en.wikipedia.org/wiki/Logic_for_Computable_Functions
[ref_popl]: https://en.wikipedia.org/wiki/Symposium_on_Principles_of_Programming_Languages
[paper_damas_milner]: https://dl.acm.org/doi/10.1145/582153.582176
[book_edinburgh_lcf]: https://link.springer.com/book/10.1007/3-540-09724-4
[thesis_damas]: https://en.wikipedia.org/wiki/Hindley%E2%80%93Milner_type_system
[related_post_a206]: {% post_url 2026-03-27-programming_language_theory_as_a_historical_arc %}
[related_post_a207]: {% post_url 2026-03-28-foundations_before_1960 %}
[related_post_a208]: {% post_url 2026-03-29-the_1960s %}
[related_post_a209]: {% post_url 2026-03-30-the_1970s_part_i %}
