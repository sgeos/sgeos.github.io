---
layout: post
mathjax: true
comments: true
title: "Compiler Backend Bring-Up: Blocking Frequency as the Ordering Principle for Instruction-Set Coverage"
date: 2026-08-06 09:00:00 +0000
categories: engineering compilers verification
series: keleusma_native
series_title: Keleusma Native Code Generation
series_index: 1
---
<!-- A369 -->
<script>console.log("A369");</script>

**A compiler was 87 percent finished. It could not compile two thirds of the programs it was for.**

Both numbers are correct. The first counts individual instructions the compiler knew how to translate. The
second counts whole programs that would actually go through.
**The gap between them is what this article is about**, and the reason it exists is simple enough to state
in one sentence. **A program needs every instruction it uses, not most of them.** One missing instruction
out of a hundred stops the whole thing, exactly as one missing link stops a chain.

**That gap then destroyed a carefully reasoned plan.** One working session before the measurement was taken,
the author of this article had formally recommended what the next piece of work should be. The reasoning had
no invalid step in it. The measurement showed the recommendation to be worth nothing at all, because the
thing it would have unblocked **does not occur even once** in any program the compiler is meant to serve.
The instrument that established this took about twenty minutes to build and two seconds to run.

**The article reports that, and then reports four errors made while writing it**, all four of which ran in
the direction of a more striking result, and one of which was committed inside the paragraph warning against
the other three.

### What this is a case study of

The setting is compiler engineering, and a reader who has never written a compiler can follow the argument,
because the shape of the problem is not specific to compilers.

A **compiler backend** translates a program from an intermediate form into instructions a machine can run.
The intermediate form has a fixed vocabulary of operations, here 66 of them. Translating each one is
separate work. **Bringing up a backend therefore means choosing an order**, and the question of which
operation to implement next is the ordering problem this article treats.

**The ordering principle in common use ranks the remaining work by how hard each item is to build and by how tidily it fits the architecture.**
This article argues that principle is systematically wrong, and that the correct one ranks by
**measured frequency of blocking** over a representative body of real programs. The argument is empirical
rather than asserted. An instrument was built over the 58 compilable programs of the shipped corpus,
comprising 73,434 instruction instances across 496 compilation units, and the resulting distribution is
reported in full, including the negative results and confidence bounds on them.

**Anywhere a customer needs a conjunction of features rather than any one of them, the same trap is available**,
and the Pattern Extraction section at the end states it without reference to compilers. ### Seven
literatures touch this problem and none of them answers it

**That absence is worth stating plainly, because it is the gap the article fills.** Each of the following
traditions has something to say about coverage, and none supplies an ordering principle.

| Tradition | Range surveyed here |
|---|---|
| Code generation and instruction selection | [Sethi and Ullman 1970][research_sethi_ullman_1970] to [Ertl 1999][research_ertl_1999] |
| Verified and validated compilation | [Necula 1997][research_necula_1997] to [Lopes and colleagues 2021][research_lopes_2021] |
| Abstract interpretation | [Cousot and Cousot 1977][research_cousot_1977] to [Blanchet and colleagues 2003][research_blanchet_2003] |
| Worst-case resource analysis | [Liu and Layland 1973][research_liu_layland_1973] to [Wilhelm and colleagues 2008][research_wilhelm_2008] |
| Corpus-based empirical study | [Knuth 1971][research_knuth_1971] to [Ray and colleagues 2014][research_ray_2014] |
| Test adequacy and mutation | [DeMillo and colleagues 1978][research_demillo_1978] to [Inozemtseva and Holmes 2014][research_inozemtseva_holmes_2014] |
| Submodular optimisation and prioritisation | [Nemhauser, Wolsey and Fisher 1978][research_nemhauser_1978] to [Buchbinder and colleagues 2015][research_buchbinder_2015] |

**The reason none of them answers the question is the same in every case.** They all reason about
instructions, and the quantity that governs delivered capability is a property of **programs**.

## The Coverage Ordering Problem

The ordering problem for instruction-set coverage during backend bring-up is the question of which subset of
an instruction set a partial code generator should implement first, given a fixed implementation budget and
a target population of programs that the generator is intended to serve. The problem permits several
formalizations depending on the engineering tradition consulted.

The compiler-construction tradition treats the coverage property as an instruction-selection completeness
question, in which the generator must eventually cover the whole instruction set and the intermediate
ordering is a matter of developer convenience. The staged-delivery tradition, in the form [Boehm
1988][research_boehm_1988] gave it, treats the coverage property as an incremental-capability question, in
which each increment should deliver a demonstrable capability to some consumer. The verification tradition,
which is the governing tradition for the present case because the Keleusma value proposition is definitive
worst-case execution time and worst-case memory usage in the sense surveyed by [Wilhelm and colleagues
2008][research_wilhelm_2008] and by [Puschner and Burns 2000][research_puschner_burns_2000], treats the
coverage property as a soundness-preservation question, in the sense [Leroy 2009][research_leroy_2009]
establishes for a realistic compiler and [Pnueli and colleagues 1998][research_pnueli_1998] formulate as
translation validation, in which every implemented instruction must be shown to preserve the semantics
already proven on the bytecode artefact and every unimplemented instruction must be refused rather than
approximated.

The three traditions agree that the instruction set must eventually be covered in full and disagree about
the intermediate ordering. The present article adopts the verification tradition for correctness obligations
and argues that none of the three supplies an adequate ordering principle, because all three reason about
instructions in isolation while the quantity that governs delivered capability is a property of programs
rather than of instructions.

### Notation

**The formal machinery below is worth the four symbols it costs, because the central result is a comparison between two averages that look interchangeable and are not.**
A reader who prefers prose can take the following and skip to the results.
**One measure averages over instructions. The other averages over programs. The second is the one a user experiences, and it is far lower.**

Let $I$ denote the instruction set, with $|I| = 66$ in the present case. Let $S \subseteq I$ denote the
subset the generator currently lowers, with $|S| = 39$ at the time of measurement. Let

$$C = \{c_1, c_2, \ldots, c_M\}, \qquad M = 496$$

denote the corpus of compilation units, with each unit $c_m$ a finite sequence of instruction instances
drawn from $I$ and $|c_m|$ its length. Write the total instance count

$$N = \sum_{m=1}^{M} |c_m| = 73{,}434$$

and the per-unit lowered count

$$n^{\text{ok}}(c_m, S) = \bigl| \{ \iota \in c_m : \iota \in S \} \bigr|.$$

### Two coverage measures

The instruction-level coverage is the proportion of instruction instances the generator handles,

$$\rho^{\text{inst}}(S) = \frac{1}{N} \sum_{m=1}^{M} n^{\text{ok}}(c_m, S).$$

The unit-level coverage is the proportion of compilation units in which every instruction is handled.
Writing the lowerability indicator

$$\chi(c_m, S) = \prod_{\iota \in c_m} \mathbf{1}[\iota \in S] = \mathbf{1}\bigl[ n^{\text{ok}}(c_m, S) = |c_m| \bigr]$$

the unit-level coverage is

$$\rho^{\text{unit}}(S) = \frac{1}{M} \sum_{m=1}^{M} \chi(c_m, S).$$

**The product is the whole difficulty, and it is worth pausing on.** A sum forgives a missing term, since
ninety-nine present out of a hundred still averages to 0.99. **A product does not forgive anything**,
because a single zero anywhere sets the entire result to zero. The first measure is a sum over instructions
and the second is an average of products over programs, which is why they can differ so widely while both
being correct.

The product form of $\chi$ is the whole difficulty. The generator exploits structured control flow directly,
in the sense of the structured program theorem of [Bohm and Jacopini 1966][research_bohm_jacopini_1966], so
that basic blocks fall out of the instruction stream without the control-flow-graph reconstruction [Allen
1970][research_allen_1970] formalised, and the conjunction is therefore a property of the instruction
multiset rather than of any recovered graph. Lowerability is a conjunction over the unit, so a single
unimplemented instruction sets the indicator to zero regardless of how many instances were handled. The
refusal is not a defect. It is the required behaviour under the verification tradition, since a generator
that approximated an unimplemented instruction would emit native code whose semantics were never proven. The
stance is the one [Necula 1997][research_necula_1997] formalises as proof-carrying code, in which the
artefact carries its own evidence, extended to a certifying compiler by [Necula and Lee
1998][research_necula_lee_1998], and the bytecode-level analogue is the bytecode verification treated by
[Leroy 2003][research_leroy_2003] and specified for the Java virtual machine by the [Oracle Java Virtual
Machine Specification][ref_jvm_spec].

The two measures satisfy $\rho^{\text{unit}}(S) \le \rho^{\text{inst}}(S)$ with equality only in the
degenerate cases where $S \supseteq \bigcup_m c_m$ or where every unit has unit length. Define the coverage
gap

$$\Gamma(S) = \rho^{\text{inst}}(S) - \rho^{\text{unit}}(S)$$

which measures the extent to which an instance-level progress report overstates delivered capability.

### Blocking sets and marginal gain

Define the blocking set of an instruction $\iota \notin S$ as the set of units that would become lowerable
if and only if $\iota$ were added,

$$B(\iota, S) = \bigl\{ c_m \in C : \chi(c_m, S) = 0 \ \wedge\ \chi(c_m, S \cup \{\iota\}) = 1 \bigr\}$$

with the marginal unit-level gain

$$g(\iota, S) = \frac{|B(\iota, S)|}{M} = \rho^{\text{unit}}(S \cup \{\iota\}) - \rho^{\text{unit}}(S).$$

Let $n(\iota)$ denote the instance count of $\iota$ across the corpus,

$$n(\iota) = \sum_{m=1}^{M} \bigl| \{ \iota' \in c_m : \iota' = \iota \} \bigr|.$$

The central structural claim is that $g$ is not monotone in $n$. Formally, there exist instructions
$\iota_a, \iota_b \notin S$ with

$$n(\iota_a) > n(\iota_b) \qquad \text{and} \qquad |B(\iota_a, S)| < |B(\iota_b, S)|$$

The results section exhibits such a pair at WORKSTREAM granularity, with a ratio exceeding three in the
instance count and exceeding three in the opposite direction in the blocking count. It does not exhibit one
at instruction granularity, and cannot, because the supermodularity established below empties almost every
instruction-level blocking set, so an instruction-level comparison would compare zeroes. The existence claim
above is therefore stated for completeness of the formalism and is witnessed only after aggregation.

The ordering problem is therefore the selection

$$\iota^{\star} = \arg\max_{\iota \in I \setminus S} \lambda(\iota, S), \qquad \lambda(\iota, S) = \frac{|B(\iota, S)|}{\kappa(\iota)}$$

with $\kappa(\iota)$ the implementation cost and $\lambda$ the leverage ratio. The ordering principle in
common use is the degenerate variant

$$\iota^{\star}_{\text{naive}} = \arg\min_{\iota \in I \setminus S} \kappa(\iota)$$

which minimises cost alone while leaving $|B|$ unmeasured and therefore implicitly assumed uniform across
instructions. The assumption is false in the case measured below.

### Supermodularity, and why greedy carries no guarantee here

The ordering principle advocated here is greedy, and it is worth asking whether greediness admits the usual
formal justification. It does not, and the reason is structurally important.

Write $R_m \subseteq I$ for the set of distinct instructions appearing in unit $c_m$, so that $\chi(c_m, S)
= \mathbf{1}[R_m \subseteq S]$ and

$$\rho^{\text{unit}}(S) = \frac{1}{M} \sum_{m=1}^{M} \mathbf{1}[R_m \subseteq S].$$

The objective is monotone non-decreasing,

$$S \subseteq S' \implies \rho^{\text{unit}}(S) \le \rho^{\text{unit}}(S')$$

since adding an instruction can only turn indicators from zero to one. The marginal gain of adding $\iota$
has the explicit form

$$g(\iota, S) = \frac{1}{M} \Bigl| \bigl\{ m : \iota \in R_m \ \wedge\ R_m \setminus \{\iota\} \subseteq S \bigr\} \Bigr|$$

and for $S \subseteq S'$ the qualifying set for $S$ is contained in the qualifying set for $S'$, since $R_m
\setminus \{\iota\} \subseteq S$ implies $R_m \setminus \{\iota\} \subseteq S'$. Therefore

$$S \subseteq S' \subseteq I, \quad \iota \notin S' \implies g(\iota, S) \ \le\ g(\iota, S')$$

which is **increasing** marginal returns. The objective is supermodular, not submodular. An initial draft of
this article asserted the opposite and invoked the [Nemhauser, Wolsey and Fisher
1978][research_nemhauser_1978] result to claim that greedy selection attains $\bigl(1 - \tfrac{1}{e}\bigr)
\approx 0.632$ of the optimum under a cardinality constraint. That claim is false. The classical guarantee
requires diminishing returns, whose tightness [Nemhauser and Wolsey 1978][research_nemhauser_wolsey_1978b]
establish, whose dependence on curvature [Conforti and Cornuejols 1984][research_conforti_cornuejols_1984]
characterise, whose geometric character [Lovasz 1983][research_lovasz_1983] develops, whose budgeted variant
[Khuller and colleagues 1999][research_khuller_1999] treat, and whose unconstrained non-monotone case
[Buchbinder and colleagues 2015][research_buchbinder_2015] settle at one half. Maximisation of a monotone
supermodular function admits no constant-factor approximation in general, the containment being of the
set-cover family whose completeness [Karp 1972][research_karp_1972] established and whose logarithmic
inapproximability threshold [Feige 1998][research_feige_1998] proved. The greedy ordering advocated here is
therefore an empirically justified heuristic with no approximation guarantee attached, and the article says
so rather than borrowing authority from a theorem that does not apply.

The correction is not merely a repair, because the increasing-returns structure explains an empirical fact
the erroneous version could not. Under increasing returns the singleton blocking sets are typically empty,

$$\bigl| B(\iota, S) \bigr| = 0 \quad \text{for most } \iota \notin S, \qquad \text{while} \qquad \bigl| B(W, S) \bigr| \gg 0$$

because a unit requiring several unimplemented instructions is unblocked by none of them individually and by
all of them jointly. This is precisely why instruction-level attribution is uninformative in this setting
and why the analysis must aggregate to workstreams. The conjunction that makes $\chi$ a product, the
conjunction that makes the objective supermodular, and the conjunction that empties the singleton blocking
sets are one observation viewed three ways.

### Workstream aggregation

Instructions that share a design prerequisite are implemented together, so the practically available choices
are workstreams rather than individual instructions. Let $W \subseteq I \setminus S$ denote a workstream.
The workstream blocking set and counterfactual gain are

$$B(W, S) = \bigl\{ c_m : \chi(c_m, S) = 0 \ \wedge\ \chi(c_m, S \cup W) = 1 \bigr\}, \qquad \Delta\rho^{\text{unit}}(W) = \frac{|B(W, S)|}{M}.$$

Workstream-level counterfactuals are better identified than instruction-level ones, because the
co-occurrence that defeats instruction-level attribution is largely within workstreams rather than across
them. An instruction reading a data-segment slot co-occurs with an instruction writing one far more often
than either co-occurs with a coroutine suspension.

## The Code Generation Literature, and Where Ordering Is Absent From It

The instruction-selection literature is mature and supplies no ordering principle, which is worth
establishing rather than asserting, because the absence is the gap this article addresses.

The tradition begins with optimality results for restricted shapes. [Sethi and Ullman
1970][research_sethi_ullman_1970] gave optimal code generation for arithmetic expressions under a
register-count constraint, and the result is optimal with respect to a fixed and fully implemented
instruction set. [Glanville and Graham 1978][research_glanville_graham_1978] introduced table-driven
selection by parsing the intermediate representation against a machine grammar, and [Fraser, Hanson and
Proebsting 1992][research_fraser_1992] reduced the approach to a practical generator generator. [Ertl
1999][research_ertl_1999] extended optimality from trees to directed acyclic graphs. At the extreme,
[Massalin 1987][research_massalin_1987] searched the instruction space exhaustively for the shortest program
computing a function. Every one of these results presupposes that the target instruction set is available in
its entirety. None addresses the partial-implementation regime, because none has a reason to.

The supporting analyses are likewise complete-set analyses. [Allen 1970][research_allen_1970] established
control-flow analysis, [Kildall 1973][research_kildall_1973] the unified dataflow framework, [Ferrante and
colleagues 1987][research_ferrante_1987] the program dependence graph, [Wegman and Zadeck
1991][research_wegman_zadeck_1991] conditional constant propagation, and [Chaitin
1982][research_chaitin_1982] register allocation by graph colouring. Static single assignment form,
introduced by [Cytron and colleagues 1991][research_cytron_1991], given a functional reading by [Appel
1998][research_appel_1998], and reduced to a simple construction by [Braun and colleagues
2013][research_braun_2013], is the representation the present generator relies on, since it models the
operand stack as memory slots and delegates their promotion to registers to that machinery. The generator
targets the intermediate representation of [Lattner and Adve 2004][research_lattner_adve_2004] specified in
the [LLVM Language Reference][ref_llvm_langref].

The observation to draw is that this literature optimises within a covered instruction set and is silent on
how to reach one. A backend author consulting it finds a great deal about how to lower an instruction well
and nothing about which instruction to lower next. The silence is not an oversight, because in the settings
these works address the instruction set is a fixed input rather than a schedule. It becomes an oversight
only when the set is being covered incrementally, which is the universal condition of a backend under
construction and a condition the literature treats as a transient state not worth theorising.

## Verified and Validated Compilation as the Governing Constraint

The refusal discipline that makes $\chi$ a conjunction is inherited from the verified-compilation
literature, and the strength of the inheritance determines how much of the ordering problem is forced rather
than chosen.

Two families of technique exist. The first proves the compiler correct once and for all, of which [Leroy
2009][research_leroy_2009] is the canonical instance for a realistic C compiler and [Kumar and colleagues
2014][research_kumar_2014] the analogous result for a functional language with a verified implementation
down to machine code. The second validates each compilation run rather than the compiler, an approach
[Pnueli and colleagues 1998][research_pnueli_1998] introduced as translation validation, [Sewell and
colleagues 2013][research_sewell_2013] applied to a verified operating-system kernel, and [Kang and
colleagues 2018][research_kang_2018] carried into the LLVM setting as credible compilation. [Zhao and
colleagues 2012][research_zhao_2012] formalised the LLVM intermediate representation itself so that
transformations over it may be verified, and [Lopes and colleagues 2021][research_lopes_2021] built bounded
translation validation for LLVM into a practical tool.

Where full verification is unavailable, differential and randomised testing carries the load. [Yang and
colleagues 2011][research_yang_2011] found hundreds of defects in production C compilers by random program
generation, [Le and colleagues 2014][research_le_2014] introduced equivalence modulo inputs as a general
oracle for compiler testing, and [Chen and colleagues 2016][research_chen_2016] applied coverage-directed
differential testing across virtual machine implementations. The present generator sits in this second
family. Its oracle is differential execution of the same bytecode on the reference virtual machine and on
the lowered native code, which is the equivalence-modulo-inputs pattern with the input space supplied by
hand rather than generated.

The consequence for the ordering problem is that partial implementation is not merely permitted but required
to be explicit. A generator in this tradition cannot silently approximate. Every unimplemented instruction
is a refusal, every refusal propagates to the whole compilation unit through the conjunction, and the
ordering problem therefore acquires its characteristic structure directly from the verification stance
rather than from any property of the instruction set. A generator willing to emit unverified approximations
would face a smooth ordering problem with diminishing returns and would be able to invoke the classical
greedy guarantee. The verification stance is what makes the objective supermodular and the guarantee
unavailable, which is a cost of that stance worth stating plainly alongside its benefits.

## Static Analysis, Undecidability, and the Conservative Stance

The generator consumes shape information produced by an abstract interpretation in the sense of [Cousot and
Cousot 1977][research_cousot_1977], which is also the framework within which [Blanchet and colleagues
2003][research_blanchet_2003] built a static analyser for large safety-critical avionics software and within
which [Regehr and colleagues 2005][research_regehr_2005] eliminated stack overflow in embedded software by
bounding stack depth statically. The last of these is the closest published analogue to the native
memory-bound problem the present workstream faces.

The conservative stance the language adopts, under which programs whose bounds cannot be proven are rejected
rather than admitted, is forced by classical undecidability. [Rice 1953][research_rice_1953] established
that every non-trivial semantic property of programs is undecidable, and [Landi 1992][research_landi_1992]
sharpened the consequence for static analysis specifically. A verifier that admits only what it can prove
will therefore reject some programs that are in fact well behaved, and the size of that gap is a design
parameter rather than a defect.

This bears on the ordering problem in a way not immediately obvious. The corpus measured below consists of
programs the front end accepts, which is a population already shaped by the conservative stance.
Instructions associated with constructs the verifier rejects cannot appear in the corpus at any frequency,
so their measured blocking contribution is zero for a reason unrelated to demand. The measurement therefore
estimates blocking frequency conditional on admissibility, and an instruction whose frequency would be high
in an unconstrained population may measure at zero here. No such case is known to arise in the present data,
but the conditioning is a real limitation of the method rather than a hypothetical one.

## Worst-Case Resource Analysis and the Native Transfer Problem

The reason the whole programme exists is the resource-bound guarantee, and the literature on that guarantee
is what determines whether native lowering can preserve it.

Hard real-time scheduling, in the form [Liu and Layland 1973][research_liu_layland_1973] established,
presupposes a worst-case execution time for each task. Obtaining that number is the subject of a substantial
literature surveyed by [Wilhelm and colleagues 2008][research_wilhelm_2008] and earlier by [Puschner and
Burns 2000][research_puschner_burns_2000]. The dominant bounding technique is implicit path enumeration,
introduced by [Li and Malik 1995][research_li_malik_1995], which expresses the worst-case path as an integer
linear program over basic-block execution counts. The precision of any such bound on real hardware depends
on microarchitectural modelling, for which [Ferdinand and Wilhelm 1999][research_ferdinand_wilhelm_1999]
gave cache behaviour prediction and [Reineke and colleagues 2007][research_reineke_2007] characterised the
predictability of cache replacement policies themselves.

The memory-bound side draws on the region and arena literature. [Tofte and Talpin
1997][research_tofte_talpin_1997] introduced region-based memory management with static inference of region
lifetimes, [Grossman and colleagues 2002][research_grossman_2002] carried regions into a safe systems
language, [Hanson 1990][research_hanson_1990] gave the practical arena discipline of allocation by object
lifetime, and [Berger and colleagues 2002][research_berger_2002] examined empirically when custom allocation
actually pays. Keleusma's arena model is of this family, and the native transfer question is whether a bound
proven over the arena survives lowering to code whose stack frames are chosen by a register allocator in the
tradition of [Chaitin 1982][research_chaitin_1982].

A companion measurement, recorded in the project's decision register rather than in a separate article,
establishes that the per-function frame size is recoverable from the emitted object file, that it folds to a
compile-time constant, and that it varies by a factor of roughly thirty depending on whether the middle-end
promotion pass of [Cytron and colleagues 1991][research_cytron_1991] has run. That measurement is what makes
the [Regehr and colleagues 2005][research_regehr_2005] approach applicable here, since it supplies the
per-function weights their longest-path analysis consumes. The ordering relevance is that none of this work
is unblocked by the instruction classes the naive ordering favoured.

## Corpus-Based Empirical Study of Programs

The method employed here belongs to a tradition with a clear origin. [Knuth 1971][research_knuth_1971]
collected and statically analysed a corpus of FORTRAN programs for the explicit reason that the profession's
beliefs about which language constructs mattered were untested, and found the distribution of constructs to
be sharply different from the folklore. The paper is the direct methodological ancestor of the instrument
described below, and its central move, which is to measure the population rather than reason about the
language, is the move this article recommends generalising.

The tradition has continued. [Basili and Weiss 1984][research_basili_weiss_1984] formalised the collection
of valid software engineering data and the failure modes of informal collection. [Richards and colleagues
2010][research_richards_2010] measured the dynamic behaviour of deployed JavaScript programs and found
systematic divergence between what the language permits, what the literature assumed programs did, and what
programs actually did. [Allamanis and Sutton 2013][research_allamanis_sutton_2013] and [Dyer and colleagues
2013][research_dyer_2013] built infrastructure for corpus mining at repository scale, and [Ray and
colleagues 2014][research_ray_2014] applied such infrastructure to language-level questions about code
quality.

Two lessons from this tradition bear directly on the present measurement. The first is that the gap between
permitted and actual is routinely large, which is exactly the gap the zero result below occupies, since the
four instructions in question are fully supported by the language and used by no program in the corpus. The
second is that corpus composition dominates conclusions, a point [Ray and colleagues
2014][research_ray_2014] and its subsequent reanalyses illustrate at length, and which the
threats-to-validity section below treats as the principal limitation of this work rather than as a
formality.

## Coverage Adequacy, Mutation, and What a Passing Suite Permits

The instrument reports a coverage figure, and the software-testing literature has spent decades establishing
what coverage figures do and do not mean. The parallel is close enough to be worth drawing explicitly.

[Zhu, Hall and May 1997][research_zhu_1997] surveyed test coverage and adequacy criteria and the
relationships among them. The decisive empirical result is [Inozemtseva and Holmes
2014][research_inozemtseva_holmes_2014], which found that coverage is not strongly correlated with
test-suite effectiveness once suite size is controlled, and therefore that a coverage percentage is a poor
proxy for the property anyone actually wants. The structural analogy to the present case is exact.
Instruction-level coverage $\rho^{\text{inst}}$ is the attractive, easily computed, and largely
uninformative measure. Unit-level coverage $\rho^{\text{unit}}$ is the one that tracks delivered capability,
and the two differ here by $\Gamma = 0.534$.

The correctness discipline used throughout the development this article reports is mutation testing,
introduced by [DeMillo, Lipton and Sayward 1978][research_demillo_1978] and surveyed by [Jia and Harman
2011][research_jia_harman_2011]. Every structural assertion in the generator's test suite carries a
must-fire case, meaning a deliberate defect injected into the lowering that the assertion is required to
detect, and a must-not-fire case, meaning a known-clean input on which it is required to stay silent. The
empirical justification for treating mutants as a proxy for real defects is given by [Andrews and colleagues
2005][research_andrews_2005] and strengthened by [Just and colleagues 2014][research_just_2014], which found
mutant detection to be correlated with real-fault detection to a degree that supports the practice.

The practice earned its place during this work rather than being adopted on authority. Of twenty-two
mutations run across the increments this article reports, five failed to fire on first execution, and those
five were of four distinct kinds.

One was a **null mutation**, in which the mutated code is semantically identical to the original, so no test
could distinguish it and none should. Changing an arithmetic shift to a logical one before a truncation that
discards the differing bits is of this kind. A null mutation is not evidence of a coverage gap and treating
it as one leads to writing a test that can never fail.

One was a **real coverage gap** in a target-specific case, where the hardware happened to define the
behaviour that the undefined-behaviour rule permitted the compiler to exploit, so no behavioural test on
that target could observe the defect. The response is a structural assertion over the emitted code.

Two were **vacuous tests**, in which the test data carried a symmetry that concealed the asymmetry under
test. In one, two branches of a differential case returned identical values. In the other, the callee of a
cross-function call performed a commutative operation, so exchanging its arguments changed nothing. The
response is redesigned input.

One was **genuinely unobservable**, a value no program in the language can read. The response is an explicit
statement that the property is untested and untestable, which is the only honest option.

The four demand different responses and were nearly conflated. Only the mutation runs distinguished them,
and the vacuous-test kind recurred three times across the work despite being actively watched for, which is
the strongest available evidence that the failure is structural rather than attributable to inattention.

## Submodular Optimisation, Coverage, and Prioritisation

The formal home of the ordering problem is the maximisation of a set function under a budget, and the
relevant results have been stated above in the course of establishing which of them apply. The complementary
literature is on prioritisation as an engineering practice rather than as an optimisation problem.

[Karlsson and Ryan 1997][research_karlsson_ryan_1997] introduced a cost-value approach to prioritising
requirements, in which candidate requirements are scored on value and on cost and ordered by the ratio,
which is structurally the leverage ratio $\lambda$ defined above. Their contribution for present purposes is
the observation that practitioners reliably estimate cost and reliably fail to estimate value, so that a
ratio-based method degenerates in practice to a cost-based one unless value is measured rather than
elicited. That is precisely the failure this article documents in the compiler setting.

The regression-testing literature supplies the closest analogue with an empirical base. [Elbaum and
colleagues 2002][research_elbaum_2002] studied test-case prioritisation across a family of empirical studies
and found that orderings informed by measured fault-detection history substantially outperform orderings
informed by structural properties of the tests. The transferable finding is that a measured signal about
outcomes beats a structural signal about artefacts, and that the margin is large enough to justify the
measurement cost.

## The Identification Problem for Blocking Attribution

The identification problem is the question of separating the blocking contribution of an individual
instruction from the contributions of the instructions that co-occur with it. A unit blocked by four
distinct unimplemented instructions is unblocked by none of them individually, so naive per-instruction
attribution overstates every contribution. The overstatement obeys

$$\sum_{\iota \in I \setminus S} |B(\iota, S)| \ \le\ \Bigl| \bigcup_{\iota \in I \setminus S} B(\iota, S) \Bigr| \ \le\ M \cdot \bigl(1 - \rho^{\text{unit}}(S)\bigr)$$

where the first inequality is an equality only when the blocking sets are pairwise disjoint, which is to say
only when no unit is blocked by two distinct instructions. In the corpus below the blocking sets are very
far from disjoint, and the singleton blocking sets are in fact mostly empty, for the supermodularity reason
established above.

The principled resolution of the attribution problem is the value of [Shapley 1953][research_shapley_1953],
which distributes the total unblocking across contributors by averaging each contributor's marginal gain
over all orders in which the contributors might be added. Writing $\mathcal{W}$ for the set of workstreams,
the Shapley attribution of workstream $W$ is

$$\phi(W) = \sum_{T \subseteq \mathcal{W} \setminus \{W\}} \frac{|T|!\,\bigl(|\mathcal{W}| - |T| - 1\bigr)!}{|\mathcal{W}|!} \Bigl[ \rho^{\text{unit}}\bigl(S \cup \textstyle\bigcup T \cup W\bigr) - \rho^{\text{unit}}\bigl(S \cup \textstyle\bigcup T\bigr) \Bigr]$$

which satisfies the efficiency property

$$\sum_{W \in \mathcal{W}} \phi(W) = \rho^{\text{unit}}\bigl(S \cup \textstyle\bigcup \mathcal{W}\bigr) - \rho^{\text{unit}}(S) = 1 - \rho^{\text{unit}}(S)$$

so the attributions sum exactly to the total unblocking with no double counting, which is precisely the
property the naive per-instruction count lacks. With $|\mathcal{W}| = 6$ the exact computation requires
$2^{6} = 64$ evaluations of $\rho^{\text{unit}}$, each a linear pass over the corpus, so the exact Shapley
attribution is computationally trivial here and its omission is a matter of scope rather than tractability.

The article therefore reports two statistics with different properties rather than attempting a single
attribution. The first is the instance count $n(\iota)$, an upper bound on effort saved that carries no
unblocking claim whatsoever. The second is the first-blocker distribution, which assigns each blocked unit
to exactly one workstream and therefore partitions the blocked population without double counting,

$$\sum_{W} f(W) = M \cdot \bigl(1 - \rho^{\text{unit}}(S)\bigr), \qquad f(W) = \bigl| \{ c_m : \text{first blocking instance of } c_m \in W \} \bigr|.$$

The first-blocker assignment is order-dependent within a unit. Writing $\pi$ for the instruction-stream
order and $f_\pi(W)$ for the resulting partition, the article reports $f_\pi$ for the natural $\pi$ and does
not compute

$$\bar f(W) = \mathbb{E}_{\pi \sim \mathcal{U}}\bigl[ f_\pi(W) \bigr]$$

over the uniform distribution on orders, nor the full blocking lattice over subsets of $I \setminus S$. This
is stated rather than left as an implicit claim to completeness. The first-blocker partition should be read
as a cheap surrogate for $\phi$, agreeing with it in ordering when one workstream dominates and unreliable
when several are comparable.

## Method

The instrument compiles every Keleusma source file in four corpus directories through the reference front
end, walks the resulting instruction streams, classifies each instance as lowered or blocking, attributes
blocking instances to a workstream by a total function over the instruction set, and classifies each
compilation unit by the lowerability indicator $\chi$.

Three properties bound the strength of the conclusions.

The instrument measures the reference compiler's output rather than source text, following the precedent
[Knuth 1971][research_knuth_1971] set in measuring what programs actually contain rather than what their
authors assume, and the data-collection discipline [Basili and Weiss 1984][research_basili_weiss_1984]
formalise. This is the correct choice, because the generator consumes bytecode rather than source, and
because the relationship between surface syntax and emitted instructions is not obvious in this language. A
prior increment established that the four instructions named for ordinary arithmetic do not carry integer
operands at all, and that all integer arithmetic is emitted as a checked form followed by a discard of two
of its three results. Any instrument reasoning over source text would have miscounted that entirely.

The instrument excludes files the front end rejects. Five of the sixty-three files were rejected, all of
them real-time operating system scripts referring to host functions registered by the embedding application
rather than declared in the script. The exclusion is environmental rather than linguistic, and including
those files would add instances to the native application binary interface class, reinforcing the reported
conclusion rather than qualifying it.

The instrument carries a guard assertion

$$\bigl(\text{files compiled} > 10\bigr) \ \wedge\ \bigl(N > 1000\bigr)$$

and fails loudly otherwise. The assertion exists because a path error in corpus discovery would silently
yield a small clean sample, and every proportion reported below would then be noise presented as a
measurement. The characteristic failure mode of a measurement instrument is a plausible number rather than
an obvious error, a point [Mytkowicz and colleagues 2009][research_mytkowicz_2009] make forcefully for
performance measurement, where bias from incidental factors such as link order and environment size was
found sufficient to reverse published conclusions.

## Results

The corpus comprises sixty-three files, of which fifty-eight compiled, yielding $M = 496$ compilation units
and $N = 73{,}434$ instruction instances. The implemented subset was $|S| = 39$ of $|I| = 66$.

**This is the headline result and everything else in the article is either support for it or a consequence of it.**

The two coverage measures diverge sharply.

$$\rho^{\text{inst}}(S) = \frac{64{,}116}{73{,}434} = 0.8731, \qquad \rho^{\text{unit}}(S) = \frac{168}{496} = 0.3387$$

$$\Gamma(S) = 0.8731 - 0.3387 = 0.5344$$

The generator handles the large majority of instruction instances and the minority of compilation units. A
programme reporting eighty-seven percent coverage would be reporting a number no consumer of the generator
can use, because no consumer executes an instruction instance in isolation.

### The measurement repeated at a larger implemented subset, and a third level

The figures above were taken at $|S| = 39$. The subset has since reached $|S| = 46$, and repeating the
measurement is instructive both because the numbers move and because it exposed a level of the conjunction
the original analysis missed.

$$\rho^{\text{inst}}(S') = \frac{71{,}948}{73{,}434} = 0.9798, \qquad \rho^{\text{unit}}(S') = \frac{432}{496} = 0.8710, \qquad \Gamma(S') = 0.1088$$

The gap between the two measures has closed from $0.534$ to $0.109$, which is the expected behaviour, since
as $S$ approaches the union of the corpus's requirement sets, both measures approach one and the gap between
them must vanish.

**But a compilation unit is not what a consumer deploys.** A consumer deploys a MODULE, and a module lowers
only if every one of its compilation units does. That is the same conjunction applied once more, and it had
been left out of the analysis entirely. Writing $\mathcal{P}$ for the corpus of programs and $u(P)$ for the
compilation units of program $P$,

$$\rho^{\text{prog}}(S) = \frac{1}{|\mathcal{P}|} \sum_{P \in \mathcal{P}} \prod_{c \in u(P)} \chi(c, S)$$

and measured at $|S'| = 46$,

$$\rho^{\text{prog}}(S') = \frac{12}{58} = 0.2069.$$

So the three measures at the same implemented subset are $0.980$, $0.871$ and $0.207$. The collapse from the
middle figure to the outer one is a factor of

$$\frac{\rho^{\text{unit}}(S')}{\rho^{\text{prog}}(S')} = \frac{0.8710}{0.2069} = 4.21$$

and the article as first drafted quoted the middle one. That is the same category of error the article was
written to describe, committed one level up, in the section reporting the error. The general form is that a
conjunction exists at every level of aggregation the consumer's requirement spans, and an analysis must find
the OUTERMOST one rather than the first one that looks like a unit of work.

### Ground truth, and why the original instrument could not supply it

The figures above at $|S| = 39$ came from a classification function that mirrored the lowering by hand. That
mirror is a second implementation of the acceptance predicate, and it drifted, because the implemented set
moved three times, each move requiring an edit to a list the lowering itself never reads.

The $|S'| = 46$ figures for $\rho^{\text{prog}}$ come instead from calling the real entry point on every
corpus program and counting successes, which cannot drift by construction. Where the two disagree the second
is authoritative. **An instrument that mirrors the system under measurement measures the mirror**, and the
defence is to call the system.

The blocking instances and first-blocker partition distribute as follows.

| Workstream $W$ | $\sum_{\iota \in W} n(\iota)$ | $f_\pi(W)$ |
|---|---|---|
| Data segment | 7832 | 267 |
| Native application binary interface | 1057 | 9 |
| Composites | 331 | 28 |
| Sub-coroutines | 98 | 24 |
| Typed arithmetic | 0 | 0 |
| Floating point and fixed point | 0 | 0 |

At $|S'| = 46$, with the data segment implemented, the same table reads as follows.

| Workstream $W$ | $\sum_{\iota \in W} n(\iota)$ | $f_\pi(W)$ |
|---|---|---|
| Native application binary interface | 1057 | 11 |
| Composites | 331 | 28 |
| Sub-coroutines | 98 | 25 |
| Typed arithmetic | 0 | 0 |

The data segment has left the table entirely, which is what implementing the leading blocker is supposed to
look like. The native interface remains the instance-count leader and the blocked-unit laggard, so the
non-monotonicity the article exhibits is not an artefact of one measurement.

The data-segment workstream accounts for

$$\frac{267}{496 - 168} = \frac{267}{328} = 0.814$$

of blocked units. The five most frequent individual blocking instructions are the data-segment slot write at
$n = 3385$, the slot read at $n = 2109$, the indexed read at $n = 1456$, the verified native call at $n =
1057$, and the indexed write at $n = 882$.

The native application binary interface class instantiates the non-monotonicity claim at the workstream
level. Writing $W_a$ for the native-call workstream and $W_b$ for the composite workstream, and extending
$n$ additively to workstreams,

$$n(W_a) = 1057 > 331 = n(W_b), \qquad f_\pi(W_a) = 9 < 28 = f_\pi(W_b)$$

so ranking by instance count places the native interface second and ranking by blocked units places it
fourth. The instruction-level claim stated earlier is the same phenomenon one level down. It is exhibited
here at workstream granularity because, for the supermodularity reason given above, the instruction-level
blocking sets are mostly empty and the instruction-level comparison would be a comparison of zeroes. Its
instances concentrate in a small number of large units already blocked for other reasons.

The sub-coroutine class deserves separate comment because its blocking count of twenty-four understates its
architectural weight. Coroutines in the sense [Conway 1963][research_conway_1963] introduced, and in the
modern treatment of [Moura and Ierusalimschy 2009][research_moura_ierusalimschy_2009], are the load-bearing
primitive for the streaming execution model the language targets, so the workstream sits on the critical
path for reasons the blocking count does not express. The ordering principle advocated here is a claim about
marginal capability and not a claim about architectural sequencing, and where a low-blocking workstream is a
prerequisite for a high-blocking one the dependency order dominates. No such dependency is known to hold
between coroutines and the data segment in the present case, and the data-segment lowering does not appear
to require suspension support. That is an engineering judgement about the two designs rather than a measured
result, and it is the one load-bearing step in this article's recommendation that rests on judgement rather
than on the instrument.

### The independence null and the clustering coefficient

The unit-level collapse invites an obvious explanation, that unimplemented instructions are simply spread
thinly across many units. That explanation is testable. Under an independence null in which each instruction
instance in a unit is lowered with probability $p = \rho^{\text{inst}}(S)$ independently, the expected
unit-level coverage is

$$\rho^{\text{unit}}_{0} = \frac{1}{M} \sum_{m=1}^{M} p^{|c_m|}$$

and the clustering coefficient is the ratio of observed to null,

$$\Phi = \frac{\rho^{\text{unit}}(S)}{\rho^{\text{unit}}_{0}}.$$

Evaluating with the measured length distribution gives

$$\rho^{\text{unit}}_{0} = 6.152 \times 10^{-2}, \qquad \Phi = \frac{0.3387}{0.06152} = 5.51$$

so the blocking instructions are clustered, and by a factor of roughly five and a half rather than by an
overwhelming margin. Repeating the calculation at $|S'| = 46$ gives $\rho^{\text{unit}}_{0} = 3.275 \times
10^{-1}$ and $\Phi = 2.66$, a weaker clustering, which is again the expected direction, since as fewer
instructions block, those that remain have less opportunity to concentrate. Unimplemented instructions
concentrate in units that use them repeatedly, which is the expected consequence of a data-segment-heavy
workload, and the concentration is real but moderate.

### A methodological near-miss worth reporting

The null above must be evaluated per unit and not at the mean unit length. Since $x \mapsto p^{x}$ is convex
for $0 < p < 1$, the inequality of [Jensen 1906][research_jensen_1906] gives

$$\frac{1}{M} \sum_{m=1}^{M} p^{|c_m|} \ \ge\ p^{\,\bar{L}}, \qquad \bar{L} = \frac{1}{M}\sum_{m=1}^{M} |c_m| = 148.05$$

and the two quantities differ enormously here because the length distribution is heavily right-skewed, with
mean $148.05$ against median $69$. Numerically,

$$p^{\,\bar{L}} = 0.8731^{148.05} = 1.884 \times 10^{-9} \qquad \text{against} \qquad \frac{1}{M}\sum_m p^{|c_m|} = 6.152 \times 10^{-2}$$

a discrepancy of more than seven orders of magnitude. Had the null been evaluated at the mean length, the
clustering coefficient would have been reported as

$$\Phi_{\text{wrong}} = \frac{0.3387}{1.884 \times 10^{-9}} = 1.80 \times 10^{8}$$

instead of $5.51$, and the article would have claimed an overwhelming clustering effect where the true
effect is moderate. The error would have been in the direction of a more striking finding, which is the
direction in which errors are least likely to be questioned.

### Confidence bounds on the zero counts

Two instruction classes occur zero times as blockers. A zero count is not an assertion of impossibility, and
the appropriate summary is an upper confidence bound rather than a point estimate. For zero events observed
in $n$ independent trials, the rule of three stated by [Hanley and Lippman-Hand 1983][research_hanley_1983]
and examined by [Jovanovic and Levy 1997][research_jovanovic_levy_1997], a normal-approximation shortcut on
the exact interval of [Clopper and Pearson 1934][research_clopper_pearson_1934], gives the approximate
ninety-five percent upper bound

$$\hat{p}_{\text{upper}} \approx \frac{3}{n}$$

which follows from solving $(1 - p)^n = 0.05$ and using $\log(0.05) \approx -3$. Applied to the two units of
account,

$$\hat{p}^{\text{inst}}_{\text{upper}} = \frac{3}{73{,}434} = 4.09 \times 10^{-5}, \qquad \hat{p}^{\text{unit}}_{\text{upper}} = \frac{3}{496} = 6.05 \times 10^{-3}$$

so the true per-instance rate of typed arithmetic in this population is below roughly four in one hundred
thousand, and the per-unit rate is below roughly six in one thousand, each at the stated confidence. The
independence assumption underlying the rule of three is violated here, since instruction instances within a
unit are strongly dependent, and the per-unit bound is consequently the more defensible of the two. For a
boundary proportion of this kind the interval of [Wilson 1927][research_wilson_1927], or the adjusted
interval [Agresti and Coull 1998][research_agresti_coull_1998] recommend in preference to the exact method,
would be the more careful summary, and the rule of three is reported here because it is the form in which
such a result is conventionally communicated rather than because it is the tightest available.

## The Zero Result, and the Recommendation It Falsified

The second zero is the finding of consequence, because the working session immediately preceding the
measurement closed with a formal recommendation that the next research spike address exactly that class. The
reasoning was as follows. The four instructions are reachable only for byte, fixed-point and floating-point
operands. The byte representation had just been settled by a measurement contributed from a parallel
development line. The remaining obstacle was that the instruction does not record which of the three types
its operands carry, and the lowerings differ, since a byte addition must mask its result to eight bits while
a fixed-point addition must not. Recovering operand types would therefore unblock the class. The
recommendation observed further that the same type information is required by the composite workstream for
field offsets, and concluded that operand type recovery was the highest-leverage remaining work by a clear
margin.

Every step of that reasoning is correct. The conclusion is worthless. Writing $W_{\text{typed}}$ for the
class,

$$n(W_{\text{typed}}) = 0 \implies B(W_{\text{typed}}, S) = \varnothing \implies \Delta\rho^{\text{unit}}(W_{\text{typed}}) = 0$$

and the composite workstream it was partly justified by satisfies $f_\pi(W_{\text{composite}}) = 28$ against
the data segment's $267$, a ratio of

$$\frac{f_\pi(W_{\text{data}})}{f_\pi(W_{\text{composite}})} = \frac{267}{28} = 9.54.$$

The failure is not a reasoning error, and the distinction matters because the corrective differs. The
argument contained no invalid step. It reasoned carefully about the structure of a problem while never
asking how often the problem occurs. A dependency analysis answers what must be true before an instruction
can be implemented. It does not answer whether anyone needs the instruction, and the two questions are
independent. The recommendation was a well-constructed answer to a question nobody had asked. [Meehl
1967][research_meehl_1967] observed the general form of this hazard in comparing theory-testing practice
across disciplines, namely that a methodology can be internally rigorous and systematically uninformative
about the question of interest.

### A refinement the same work later forced, which sharpens the lesson

The account above is correct and incomplete, and the missing part changes what a reader should take away.

Operand type recovery was dismissed on the strength of a zero. Some increments later, the composite
workstream turned out to require exactly that capability, for an unrelated reason, namely that
`Op::NewComposite` carries the composite kind, the field count and the total byte size, and NOT the
per-field widths, while packing is tight and in declaration order. Writing a composite body therefore needs
each field's width and no instruction records it. That is 18 compilation units, against the zero the
original assessment measured.

So the measurement was right and the inference from it was too broad. It established that type recovery was
worthless FOR THE INSTRUCTION CLASS PROPOSED, and the conclusion drawn was that type recovery was worthless.
A capability is not made valueless by the emptiness of one demand for it, and a frequency measurement that
redirects work away from a capability has said something about that demand rather than about the capability.

The sharpened statement is therefore in two parts rather than one. Measure demand before ordering by
structure, because a dependency argument cannot see frequency. And scope the negative result to what was
measured, because a zero counts occurrences of one thing and licenses no conclusion about anything else. The
first part saved the work described here. The second part was learned by getting it wrong in the same
programme, a few increments later, and having to correct a document that had recorded the over-broad version
as a finding.

The corpus check that falsified it cost approximately twenty minutes to build and two seconds to run. The
cost of the work it redirected cannot be stated with comparable confidence, because that work was never
performed. **The numerator below is measured and the denominator is an estimate of a counterfactual**, so
the ratio should be read as an order of magnitude and not as a quantity. Writing $\kappa_{\text{measure}}$
for the measured cost and $\kappa_{\text{spike}}$ for the estimated cost of the redirected spike,

$$\frac{\kappa_{\text{measure}}}{\kappa_{\text{spike}}} \sim 10^{-2}$$

so the measurement plausibly cost one or two orders of magnitude less than the work it redirected, and the
redirected work would have delivered $\Delta\rho^{\text{unit}} = 0$ exactly. Only the last of those three
statements is a measurement. An earlier draft gave this ratio as $0.019$ against a sixteen-hour denominator,
presenting an invented figure to two significant figures inside a formal expression, which lent it a
precision it had not earned.

## Measurement Error and the Direction of Bias

This article reports **four** errors made in the course of producing it, and their common direction is the
most transferable observation available.
**Three are described below and the fourth is described inside the description of the third**, which is not
an accident and is the point of the section.

The first is the convexity shortcut described above, which would have inflated a clustering coefficient by
seven orders of magnitude. The second is a false modularity theorem, in which the coverage objective was
asserted to be submodular so that a classical approximation guarantee could be invoked, when the objective
is supermodular and no such guarantee exists. The third occurred while assembling this article's references.
Of ninety-one candidate digital object identifiers supplied from memory, four resolved to entirely different
works and one did not resolve at all, an error rate of five and a half percent. One resolved to a paper on
record allocation for drum storage in place of a paper on optimal code generation for expression trees, and
one to a paper on a lambda calculus of objects in place of a paper on lightweight bytecode verification.
Each of the four would have returned a successful response to a reachability check, so only comparison of
the resolved title against the claimed title detected them.

**A draft of this article reported this rate as near ten percent over forty-two candidates.** That figure is
the first three verification batches taken alone, which is the worse subsample, and the later batches were
run after the sentence was written and never folded into it. The effect was to report a more alarming number
than the data supported, in the section of the article devoted to the tendency to report more alarming
numbers than the data support. The error is left visible here rather than silently repaired, because a
corrected figure with no record of the correction would conceal the most instructive part of the episode.

All four errors ran toward a more striking or better-founded-looking result. The clustering error would have
produced a dramatic finding, the modularity error would have supplied a theoretical guarantee for the
article's central recommendation, the citation errors would have furnished authority, and the misstated
defect rate would have made the cautionary point more forcefully. None ran in the direction of weakening a
claim, and the fourth was committed while writing the paragraph warning against the first three.

This direction is documented at scale in the empirical-methods literature. [Rosenthal
1979][research_rosenthal_1979] described the suppression of null results and estimated the number of
unpublished null studies required to overturn a published effect. [Simmons, Nelson and Simonsohn
2011][research_simmons_2011] demonstrated that undisclosed flexibility in data collection and analysis
suffices to produce statistically significant evidence for false propositions without any conscious
dishonesty. [Ioannidis 2005][research_ioannidis_2005] derived the consequences for base rates of published
findings, and [Munafo and colleagues 2017][research_munafo_2017] set out the corresponding reform programme.
The mechanism in each case is not fraud but asymmetric scrutiny, in which a result the author expects and
welcomes receives less checking than one that surprises or disappoints.

The engineering translation is direct. An error that weakens a claim tends to be noticed because it is
unwelcome. An error that strengthens one is congenial and passes unexamined, and a formal apparatus is an
efficient way to manufacture such errors because its conclusions carry borrowed authority. Three defences
were used here and are recommended generally. Evaluate aggregates over the observed distribution rather than
at its mean whenever the aggregating function is not affine. Test a formal claim by brute-force enumeration
over instances small enough to check exhaustively before relying on it. Verify every citation against the
resolved record rather than against memory, since the failure mode is a plausible reference rather than a
broken link.

## Threats to Validity

The corpus is drawn from one project's own examples, standard library and self-hosted compiler stages, and
is therefore not a sample of the programs the generator will eventually serve. Writing
$\mathcal{D}_{\text{corpus}}$ for the empirical distribution over units and $\mathcal{D}_{\text{target}}$
for the eventual target population, every quantity reported above estimates

$$\mathbb{E}_{c \sim \mathcal{D}_{\text{corpus}}}\bigl[ \cdot \bigr] \qquad \text{rather than} \qquad \mathbb{E}_{c \sim \mathcal{D}_{\text{target}}}\bigl[ \cdot \bigr]$$

and no importance weighting is applied because the target distribution is not yet observable. The corpus
over-represents the self-hosted compiler, a text-processing workload with heavy data-segment use, and
under-represents the signal-processing and embedded-control workloads the roadmap names as target
applications. A defensible reading is that the data segment leads for the near-term consumer and that the
ranking should be re-measured when the target population changes. The sensitivity of conclusions to corpus
composition is the standard caution of this literature, and [Blackburn and colleagues
2006][research_blackburn_2006] made the point concrete in constructing a benchmark suite specifically
because prior suites had shaped conclusions unrepresentatively, while [Blackburn and colleagues
2016][research_blackburn_2016] set out the corresponding evaluation discipline.

The first-blocker attribution is order-dependent, as formalised above, and the full blocking lattice is not
computed. For the leading result this is unlikely to matter, since

$$\frac{f_\pi(W_{\text{data}})}{\max_{W \ne W_{\text{data}}} f_\pi(W)} = \frac{267}{28} = 9.54$$

and an order-dependence artefact would have to be extreme to invert a margin approaching ten to one. For the
ordering of the second, third and fourth workstreams, at $28$, $24$ and $9$, the artefact could plausibly
reorder them, and no claim about that ordering should be read as established. Since the exact Shapley
attribution requires only sixty-four corpus passes, the honest characterisation is that the surrogate was
used for scope reasons and that the secondary ordering could be settled cheaply whenever it matters.

The zero results are subject to the corpus caveat and are bounded above rather than asserted absent, as
quantified in the confidence-bound section. The correct inference is not that the typed arithmetic class
will never matter but that it does not matter now, which is the question an ordering principle asks.

The measurement is static rather than dynamic. It counts instruction instances in compiled units and not
executions, so it estimates the difficulty of lowering a program and not the time a program spends in any
instruction. For the ordering question this is the correct unit, since a refusal is a static property, but
the resulting figures must not be read as execution profiles. [Georges and colleagues
2007][research_georges_2007] set out why execution-time claims require a different and considerably more
careful methodology than the one applied here, and no such claim is made.

Finally, the measurement was performed by the same party that made the recommendation it falsifies, using an
instrument that party wrote. The guard assertion described in the method section addresses the most likely
failure mode of that arrangement, which is a silently empty sample, but it does not address the possibility
of a classification function whose workstream boundaries were drawn, unconsciously, to produce a tidy
result. The classification is a total function over sixty-six instructions and is available for inspection,
which is offered as mitigation rather than as a claim that the concern is closed.

## Pattern Extraction

The abstract mechanic generalises beyond compiler backends to any incremental capability programme in which
a consumer requires a conjunction of features rather than any one of them.

The mechanic has three parts. First, when a consumer requires every element of a set to be present,
delivered capability is governed by the product form $\chi = \prod_i \mathbf{1}[\,\cdot\,]$ and not by the
sum form $\rho^{\text{inst}} = \frac{1}{N}\sum_i \mathbf{1}[\,\cdot\,]$, so per-element progress measures
overstate delivered capability by the gap $\Gamma$, which grows with the dispersion of the missing elements.
Second, the natural ordering heuristics available to an implementer, which are implementation cost $\kappa$,
architectural elegance, and dependency depth, are all properties of elements considered in isolation, and
none carries information about $|B(\iota, S)|$. Third, the corrective is a frequency measurement over a
representative population of consumers, and the measurement satisfies

$$\kappa_{\text{measure}} \ll \kappa_{\text{work}}$$

characteristically by one to two orders of magnitude, because the cost of counting occurrences is nearly
independent of the cost of the work being ordered.

The observation is old. [Knuth 1971][research_knuth_1971] measured a corpus of FORTRAN programs precisely
because the profession's assumptions about which constructs mattered were untested, and [Amdahl
1967][research_amdahl_1967] had already given the arithmetic showing that effort spent outside the dominant
term is bounded above by a small number regardless of how well it is spent, a bound [Gustafson
1988][research_gustafson_1988] later reframed without dissolving. The present article adds only that the
same asymmetry applies to feature ordering under a conjunctive consumer, that the dominant term is not
visible from the structure of the work, and that the conjunction makes the objective supermodular so that no
approximation guarantee is available to substitute for the measurement.

The mechanic carries a self-application. An implementer reasoning carefully about dependency structure
produces recommendations that feel well-founded, because they are well-founded with respect to the question
of what is required. The recommendation acquires unearned authority from the rigour of the dependency
argument, and the missing question is not visible from inside that argument. The defence is procedural
rather than intellectual. Before accepting an ordering derived from structure, measure the frequency, and
treat the structural argument as establishing feasibility rather than priority.

A second self-application concerns the analysis itself, and this article contains four instances of it,
comprising a convexity shortcut, a false modularity theorem, a defect rate in citations supplied from
memory, and a misstatement of that rate over the worse subsample. All ran toward a more striking or
better-supported result, which is the direction least likely to attract scrutiny, and none was caught by
reading. Each was caught by an execution, respectively a numerical evaluation whose answer was implausible,
a brute-force enumeration over small instances, a query against an authoritative record, and a recount over
the full sample rather than the remembered one. That the fourth was committed inside the passage cautioning
against the first three is the clearest evidence available that awareness of a bias does not confer immunity
to it. The general defence is to test the apparatus on cases small enough to enumerate before trusting it on
the case of interest.

The general statement is that dependency analysis and demand measurement answer different questions, that
the first is more intellectually satisfying and more readily available to an implementer, and that ordering
decisions made on the first alone are unreliable in a direction the analysis itself cannot reveal.

## Epistemic State

**Measured, and reproducible from the instrument.** The corpus comprises 63 files of which 58 compiled,
yielding 496 compilation units and 73,434 instruction instances. The implemented subset was 39 of 66
instructions. Instruction-level coverage was 0.8731 and unit-level coverage 0.3387, for a gap of 0.5344. The
leading workstream blocked 267 units against 28 for the next, a ratio of 9.54. The instruction class the
falsified recommendation would have unblocked occurs zero times. Of 91 candidate digital object identifiers
supplied from memory, four resolved to different works and one did not resolve, an error rate of 5.5
percent.

**Derived, and checkable from the definitions.** That unit-level coverage cannot exceed instruction-level
coverage follows from the product form. That the objective is supermodular rather than submodular, so that
the classical greedy approximation guarantee does not apply, is established by counterexample. The
clustering coefficient of 5.51 and the confidence bounds on the zero counts follow from the stated method.

**Assumed, and marked as such.** The first-blocker attribution is order-dependent and the full blocking
lattice was not computed, so **the ordering of the second, third and fourth workstreams is not established**
and no claim about it should be read as such. The cost ratio between the measurement and the work it
redirected is an order of magnitude rather than a quantity, because its numerator is measured and its
denominator is an estimate of work never performed.

**Corrected during writing, and left visible.** An independence null was first evaluated at the mean
compilation-unit length rather than per unit, which would have inflated a clustering coefficient by seven
orders of magnitude. A modularity theorem was asserted that the objective does not admit. A citation defect
rate was first reported as near ten percent over the worse subsample rather than 5.5 percent over the full
one. **The conclusion that operand type recovery was worthless was itself too broad**, since the capability
was later required by a different workstream for an unrelated reason, at 18 compilation units. The zero was
correct and the inference from it was not.

**What the article does not establish.** Whether the corpus resembles the population the generator will
eventually serve, since it is drawn from one project's own examples and over-represents a text-processing
workload. Whether the classification of instructions into workstreams was drawn neutrally, since the party
that made the falsified recommendation also wrote the instrument that falsified it.
**The article offers the classification for inspection as mitigation and does not claim the concern is closed.**

**The strongest claim the evidence supports** is that on this corpus, at this implemented subset, a
frequency measurement redirected work away from an item that would have delivered exactly zero.
**The weakest link is corpus representativeness**, and a reader who doubts it should read the ordering as
established for the present consumer rather than for the eventual one.

## Out of Scope

The design of the code generator itself, and the lowering strategy for any particular instruction. The
worst-case execution time and memory analysis that motivates the project, which is a separate subject.
Register allocation, instruction scheduling and peephole optimisation, none of which the ordering question
touches. Dynamic profiling, since the measurement here is static by design and the two answer different
questions. The exact Shapley attribution over the blocking lattice, which is affordable at 64 corpus passes
and was not performed. Any claim about execution time, which would require a different and considerably more
careful methodology. The Keleusma language itself and its implementation history.

## Conclusion

**Eighty-seven percent of the instructions and thirty-four percent of the programs are the same compiler on the same day.**
The first number is what a progress report contains and the second is what a user experiences, and the
distance between them is created entirely by the fact that a program needs every instruction it uses.

**The practical rule is short.** When a consumer requires a conjunction of features, per-feature progress
overstates delivered capability, and the amount of the overstatement is not visible from inside the work.
**Dependency analysis tells you what is required before something can be built. It tells you nothing about whether anyone needs it**,
and those two questions are independent in a way that is easy to miss because the first is more satisfying
to answer.

**The measurement that settles it is usually trivial next to the work it redirects.** Twenty minutes of
instrument against a research spike, in this case, and the spike would have delivered nothing.

**The last part is the least comfortable and the most useful.** Four errors were made in producing this
article and every one of them pointed toward a more striking result. None was found by rereading. Each was
found by running something, whether a numerical evaluation whose answer was implausible, an enumeration over
small cases, a query against an authoritative record, or a recount over the full sample rather than the
remembered one. **The fourth was committed while writing the warning about the first three**, which is the
clearest evidence available that knowing about a bias does not protect anyone from it.

## References

### Reference

[ref_jvm_spec]: https://docs.oracle.com/javase/specs/jvms/se21/html/index.html
[ref_llvm_langref]: https://llvm.org/docs/LangRef.html

### Research

[research_agresti_coull_1998]: https://doi.org/10.1080/00031305.1998.10480550
[research_allamanis_sutton_2013]: https://doi.org/10.1109/MSR.2013.6624029
[research_allen_1970]: https://doi.org/10.1145/800028.808479
[research_amdahl_1967]: https://doi.org/10.1145/1465482.1465560
[research_andrews_2005]: https://doi.org/10.1109/ICSE.2005.1553583
[research_appel_1998]: https://doi.org/10.1145/278283.278285
[research_basili_weiss_1984]: https://doi.org/10.1109/TSE.1984.5010301
[research_berger_2002]: https://doi.org/10.1145/582419.582421
[research_blackburn_2006]: https://doi.org/10.1145/1167473.1167488
[research_blackburn_2016]: https://doi.org/10.1145/2983574
[research_blanchet_2003]: https://doi.org/10.1145/781131.781153
[research_boehm_1988]: https://doi.org/10.1109/2.59
[research_bohm_jacopini_1966]: https://doi.org/10.1145/355592.365646
[research_braun_2013]: https://doi.org/10.1007/978-3-642-37051-9_6
[research_buchbinder_2015]: https://doi.org/10.1137/130929205
[research_chaitin_1982]: https://doi.org/10.1145/872726.806984
[research_chen_2016]: https://doi.org/10.1145/2908080.2908095
[research_clopper_pearson_1934]: https://doi.org/10.1093/biomet/26.4.404
[research_conforti_cornuejols_1984]: https://doi.org/10.1016/0166-218X(84)90003-9
[research_conway_1963]: https://doi.org/10.1145/366663.366704
[research_cousot_1977]: https://doi.org/10.1145/512950.512973
[research_cytron_1991]: https://doi.org/10.1145/115372.115320
[research_demillo_1978]: https://doi.org/10.1109/C-M.1978.218136
[research_dyer_2013]: https://doi.org/10.1109/ICSE.2013.6606588
[research_elbaum_2002]: https://doi.org/10.1109/32.988497
[research_ertl_1999]: https://doi.org/10.1145/292540.292562
[research_feige_1998]: https://doi.org/10.1145/285055.285059
[research_ferdinand_wilhelm_1999]: https://doi.org/10.1023/A:1008186323068
[research_ferrante_1987]: https://doi.org/10.1145/24039.24041
[research_fraser_1992]: https://doi.org/10.1145/151640.151642
[research_georges_2007]: https://doi.org/10.1145/1297027.1297033
[research_glanville_graham_1978]: https://doi.org/10.1145/512760.512785
[research_grossman_2002]: https://doi.org/10.1145/512529.512563
[research_gustafson_1988]: https://doi.org/10.1145/42411.42415
[research_hanley_1983]: https://doi.org/10.1001/jama.1983.03330370053031
[research_hanson_1990]: https://doi.org/10.1002/spe.4380200104
[research_inozemtseva_holmes_2014]: https://doi.org/10.1145/2568225.2568271
[research_ioannidis_2005]: https://doi.org/10.1371/journal.pmed.0020124
[research_jensen_1906]: https://doi.org/10.1007/BF02418571
[research_jia_harman_2011]: https://doi.org/10.1109/TSE.2010.62
[research_jovanovic_levy_1997]: https://doi.org/10.1080/00031305.1997.10473947
[research_just_2014]: https://doi.org/10.1145/2635868.2635929
[research_kang_2018]: https://doi.org/10.1145/3192366.3192377
[research_karlsson_ryan_1997]: https://doi.org/10.1109/52.605933
[research_karp_1972]: https://doi.org/10.1007/978-1-4684-2001-2_9
[research_khuller_1999]: https://doi.org/10.1016/S0020-0190(99)00031-9
[research_kildall_1973]: https://doi.org/10.1145/512927.512945
[research_knuth_1971]: https://doi.org/10.1002/spe.4380010203
[research_kumar_2014]: https://doi.org/10.1145/2535838.2535841
[research_landi_1992]: https://doi.org/10.1145/161494.161501
[research_lattner_adve_2004]: https://doi.org/10.1109/CGO.2004.1281665
[research_le_2014]: https://doi.org/10.1145/2594291.2594334
[research_leroy_2003]: https://doi.org/10.1023/A:1025055424017
[research_leroy_2009]: https://doi.org/10.1145/1538788.1538814
[research_li_malik_1995]: https://doi.org/10.1145/217474.217570
[research_liu_layland_1973]: https://doi.org/10.1145/321738.321743
[research_lopes_2021]: https://doi.org/10.1145/3453483.3454030
[research_lovasz_1983]: https://doi.org/10.1007/978-3-642-68874-4_10
[research_massalin_1987]: https://doi.org/10.1145/36206.36194
[research_meehl_1967]: https://doi.org/10.1086/288135
[research_moura_ierusalimschy_2009]: https://doi.org/10.1145/1462166.1462167
[research_munafo_2017]: https://doi.org/10.1038/s41562-016-0021
[research_mytkowicz_2009]: https://doi.org/10.1145/1508284.1508275
[research_necula_1997]: https://doi.org/10.1145/263699.263712
[research_necula_lee_1998]: https://doi.org/10.1145/277650.277752
[research_nemhauser_1978]: https://doi.org/10.1007/BF01588971
[research_nemhauser_wolsey_1978b]: https://doi.org/10.1287/moor.3.3.177
[research_pnueli_1998]: https://doi.org/10.1007/BFb0054170
[research_puschner_burns_2000]: https://doi.org/10.1023/A:1008119029962
[research_ray_2014]: https://doi.org/10.1145/2635868.2635922
[research_regehr_2005]: https://doi.org/10.1145/1113830.1113833
[research_reineke_2007]: https://doi.org/10.1007/s11241-007-9032-3
[research_rice_1953]: https://doi.org/10.1090/S0002-9947-1953-0053041-6
[research_richards_2010]: https://doi.org/10.1145/1806596.1806598
[research_rosenthal_1979]: https://doi.org/10.1037/0033-2909.86.3.638
[research_sethi_ullman_1970]: https://doi.org/10.1145/321607.321620
[research_sewell_2013]: https://doi.org/10.1145/2491956.2462183
[research_shapley_1953]: https://doi.org/10.1515/9781400881970-018
[research_simmons_2011]: https://doi.org/10.1177/0956797611417632
[research_tofte_talpin_1997]: https://doi.org/10.1006/inco.1996.2613
[research_wegman_zadeck_1991]: https://doi.org/10.1145/103135.103136
[research_wilhelm_2008]: https://doi.org/10.1145/1347375.1347389
[research_wilson_1927]: https://doi.org/10.1080/01621459.1927.10502953
[research_yang_2011]: https://doi.org/10.1145/1993498.1993532
[research_zhao_2012]: https://doi.org/10.1145/2103656.2103709
[research_zhu_1997]: https://doi.org/10.1145/267580.267590
