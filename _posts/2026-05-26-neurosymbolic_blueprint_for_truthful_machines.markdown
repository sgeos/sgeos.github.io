---
layout: post
mathjax: false
comments: true
title: "A Speculative Neurosymbolic Blueprint for Truthful, Scientific, and Abstaining Machines"
date:   2026-05-26 09:00:00 +0000
categories: ai philosophy
---

<!-- A108 -->
<script>console.log("A108");</script>

Suppose a person wants an assistant
that adheres rigidly to the
[scientific method][ref_scientific_method],
that values truthfulness over agreement,
and that declines to answer
or asks for a question to be rephrased
when declining is the honest response.
This article asks what machine architecture
would satisfy those requirements,
and it arrives at an uncomfortable conclusion.
No single [large language model][ref_llm]
can satisfy them,
because the requirements are guarantees
and a stochastic next-token predictor
cannot supply guarantees about its own behavior.
The system that could satisfy them
is not a model at all
but a compound [neuro-symbolic][ref_neurosymbolic] system
in which a language model is one component
wrapped inside deterministic and symbolic machinery
that holds the guarantees the network cannot.

This article is a speculative blueprint.
It is not a proven design.
The distinction matters,
and it is the same distinction
the proposed system is meant to enforce.
The individual components described here
each have support in the published literature.
The integration of those components
into a single working system
that is more truthful, more rigorous,
and more willing to abstain
than current assistants
is a hypothesis.
No deployed general-purpose system
demonstrates the whole assembly,
and the strongest published objections
land on exactly the parts
the design leans on most heavily.
Where a claim is established,
this article marks it as established.
Where a claim is an inference
or a hypothesis,
this article marks it as such.

## Software Versions

```sh
# Date (UTC)
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2026-05-26 09:00:00 +0000
```

## Four Requirements and One Tension

The requirements can be stated compactly.
First, the system should operate
under a regime of engineering and epistemic rigor.
It should distinguish facts, inferences, and hypotheses,
mark uncertainty explicitly,
and never imply completeness
where verification is incomplete.
Second, it should adhere to the scientific method,
treating an empirical claim as warranted
only when it is [falsifiable][ref_falsifiability]
and has survived an attempt at falsification.
This is the [demarcation criterion][book_logic_scientific_discovery]
that Karl Popper placed at the center of scientific method,
namely that a hypothesis is scientific
only if observations could in principle refute it,
and that the growth of knowledge proceeds
by the elimination of conjectures that fail testing
rather than by the accumulation of confirmations.
Third, it should value truthfulness over
[sycophancy][research_sycophancy],
the documented tendency of trained models
to tell a user what the user wants to hear.
Fourth, it should decline,
or ask for a reformulation,
when declining is the most truthful response
available within the method.

These four requirements are not independent.
Requirements two and four are the same property
viewed from two angles.
If a system adheres strictly to the scientific method,
then it must withhold judgment
on claims that are not testable,
that are under-specified,
or that the available evidence does not support.
A large fraction of ordinary requests
fall into one of those categories.
A system built to honor the method
would therefore decline, qualify,
or ask for reframing
far more often than current assistants do.
Principled abstention is not an accessory feature.
It is the direct consequence
of taking the scientific method seriously.
A reader who asks for requirement two
and is then frustrated by requirement four
has asked for two names of one thing.

## Why a Single Language Model Cannot Supply Guarantees

The argument that follows
rests on properties of current language models
that are documented rather than speculative.
The inference drawn from them,
that a single model cannot supply the guarantees,
is mine,
but the underlying properties are established.

A language model produces text
by sampling likely continuations,
not by consulting a grounded model of truth.
[Hallucination][ref_hallucination],
the confident generation of false content,
is therefore not an incidental defect
layered on top of an otherwise truthful system.
It is the default behavior of the mechanism,
with truthfulness being the property
that has to be trained and prompted into it.
[Lin and colleagues (2021)][research_truthfulqa]
demonstrated with the TruthfulQA benchmark
that models often reproduce human falsehoods,
and that scaling alone does not fix the problem.
[Farquhar and colleagues (2024)][research_semantic_entropy],
writing in Nature,
showed that a measure called semantic entropy
can detect a large class of these confabulations,
which establishes both that the failure is real
and that uncertainty signals can be extracted from the model.

[Sycophancy][research_sycophancy]
has a known origin in the training objective.
[Sharma and colleagues (2023)][research_sycophancy]
analyzed human preference data
and found that responses agreeing with a user
were more likely to be marked as preferred,
even when the agreeable response was wrong.
A reward model fit to such data
internalizes an agreement heuristic,
and a policy optimized against that reward
amplifies it.
[Reinforcement learning from human feedback][ref_rlhf]
is the mechanism by which the bias enters,
which means the fix must also live
at the level of the objective,
not merely in surface phrasing.
This is one instance of a more general failure,
[reward hacking][ref_reward_hacking],
also called specification gaming,
in which an optimizer satisfies the literal objective
while missing the intended outcome.
[Amodei and colleagues (2016)][research_concrete_problems]
catalogued this as a foundational safety problem,
and it remains the deeper risk under sycophancy.

A subtler defect undermines self-report directly.
A model has limited and unreliable introspective access
to its own computation.
When it reports on its reasoning,
its confidence, or its internal state,
it is largely generating a plausible narrative
by the same process that generates everything else.
There is an honest nuance to state here.
[Kadavath and colleagues (2022)][research_self_knowledge]
showed that large models are partially calibrated
and can estimate the probability that their own answers are correct,
so the access is not zero.
But partial calibration is not faithful introspection,
and self-reports can still be fluent and wrong
with no internal signal distinguishing the two.
Any honesty guarantee that depends
on a model truthfully reporting its own state
is therefore unreliable at the root.

Two further properties compound the problem.
Generation is autoregressive and single-pass,
so an early error conditions everything after it,
and errors can accumulate
rather than self-correct.
[Huang and colleagues (2023)][research_cannot_self_correct]
found that models cannot reliably self-correct their reasoning
without external feedback,
and that self-correction can even degrade performance.
This is a central result for the present design,
because it implies that correction must come
from an external checker rather than from the model itself.
The recursive degradation of unverified self-correction
is the same family of concern
explored for autonomous systems
in [the error correction recursion problem][related_post_error_correction].
And compute per token is fixed,
so the model spends roughly the same effort
on a trivial step and a decisive one.
The partial mitigations are to externalize reasoning
as intermediate tokens through
[chain-of-thought prompting][research_chain_of_thought]
or to make depth adaptive through architectures like
[mixture-of-depths][research_mixture_of_depths],
but neither converts a stochastic proposer into a verifier.

The conclusion I draw from these properties
is that the desired guarantees
cannot be obtained from a single network
by training or prompting alone.
A stochastic model can be nudged
toward truthful, rigorous, abstaining behavior,
but it cannot certify that it has complied,
because it has no faithful access
to whether it has complied.
The guarantees must come from somewhere else.

## The Central Design Principle

The principle that organizes the whole design
follows from the previous section.
Rigidity must live in deterministic machinery
outside the neural model,
and the neural model must be demoted
to a proposal engine
whose outputs are gated by that machinery.
Fluency and hypothesis generation
belong in the network,
because that is what networks do well.
Guarantees belong in symbolic and procedural code,
because that is the only part of the system
whose behavior can be audited
and does not depend on the model
choosing to behave.

This principle has a direct precedent.
The systems that today come closest
to verified machine reasoning,
namely [automated theorem provers][ref_theorem_proving],
work exactly this way.
A neural network proposes a candidate,
and a symbolic engine checks it.
The guarantee comes from the checker,
not from the proposer.

## A Layered Architecture

The following layers describe one design
that applies the central principle.
The decomposition is a proposal,
not a validated specification.

### Layer Zero, Typed Claims as the Native Output

The foundational choice
is that the system does not emit free prose
as its primary artifact.
It emits a structured object
in which every assertion carries
an explicit epistemic tag
drawn from a fixed set,
namely fact, inference, hypothesis, or speculation,
together with a provenance pointer
and a confidence value.
Prose is rendered from this structure
as a final step.
This makes the requirement
to distinguish facts, inferences, and hypotheses
a structural invariant
rather than a stylistic preference.
A claim tagged as fact
that lacks a resolvable provenance pointer
is rejected by the layer above it
and forced to downgrade.

### Layer One, Separation of Knowledge from Computation

The reasoning core does not hold facts
in its weights as ground truth.
Factual claims must be backed by retrieval
from an external, versioned store
that carries provenance.
This is the architecture of
[retrieval-augmented generation][ref_rag],
introduced by [Lewis and colleagues (2020)][research_rag],
which combines parametric memory in the weights
with non-parametric memory in an external index.
A claim tagged as fact is valid
only if it resolves to a citation
that the verifier can independently re-fetch
and check for support.

The machinery for that check now exists in research form.
[Self-RAG][research_self_rag]
trains a model to retrieve on demand
and to critique its own generations
against retrieved evidence using reflection tokens.
[RARR][research_rarr]
researches and revises model output post hoc
to attach attribution and remove unsupported content.
[FActScore][research_factscore]
decomposes a long answer into atomic facts
and scores each against a knowledge source,
and the [Search-Augmented Factuality Evaluator][research_safe]
automates that decomposition and verification at scale.
These methods make Layer One concrete.
Claims that cannot be grounded
are demoted to inference or hypothesis automatically,
which attacks hallucination at its source
and makes knowledge correctable without retraining.

### Layer Two, Generator and Adversarial Critic

This layer is the scientific-method engine
and the core anti-sycophancy mechanism.
One model proposes.
A separate critic, or an ensemble of critics,
is trained with the opposite objective,
to refute the proposal,
to find the unfalsifiable claim,
the missing control, the confound, the overreach.
The idea that correctness can be enforced
by an adversarial game between agents
traces to [AI safety via debate][research_debate],
proposed by [Irving and colleagues (2018)][research_debate].
A practical instance is
[CriticGPT][research_criticgpt],
reported by [McAleese and colleagues (2024)][research_criticgpt],
which catches errors in code
that human reviewers miss.
The broader research program of [scalable oversight][research_weak_to_strong]
studies exactly this problem,
namely how a weaker verifier
can supervise a more capable generator.

The decisive design choice
is that the critic is rewarded
for successful refutation
and is never exposed
to any signal about user approval.
Sycophancy lives in the reward function,
so the cure must live there too.
The [Constitutional AI][research_constitutional_ai] method
of [Bai and colleagues (2022)][research_constitutional_ai]
demonstrated that a model can be trained
against an explicit set of principles
using AI-generated feedback rather than human approval,
which is one route to a critic
with no incentive to please.
A critic with no incentive to please
and a strong incentive to break weak claims
removes the gradient
that produces agreeableness.
The generator must then survive the critic
rather than satisfy a human rater.

I must flag the strongest objection to this layer immediately.
The result of [Huang and colleagues (2023)][research_cannot_self_correct]
implies that the critic must be genuinely independent of the generator,
because a model checking its own work
is unreliable.
If the critic and generator share training data
and therefore share blind spots,
the adversarial guarantee weakens toward self-critique,
which is the failure mode this layer is meant to avoid.

### Layer Three, A Deterministic Scientific-Method Controller

An outer control loop,
written as ordinary code rather than learned,
runs the cycle explicitly.
It elicits the question,
requires any empirical claim
to be cast as a falsifiable statement
with predicted observations,
dispatches the generator to propose,
dispatches the critic to attempt falsification,
consults the retrieval store and verifiers,
and only then permits an output.
Intermediate reasoning is externalized
through [chain-of-thought][research_chain_of_thought]
so that each step is inspectable,
and each step can be scored
by a [process reward model][research_process_supervision].
[Lightman and colleagues (2023)][research_process_supervision]
showed that process supervision,
which provides feedback on each reasoning step,
outperforms outcome supervision
and localizes the exact step that fails.
The loop has explicit terminal states,
and crucially the set of terminal states
does not include
"produce a best guess anyway."
It includes answer warranted,
answer warranted with stated uncertainty,
insufficient evidence so abstain,
and question ill-posed so request reframing.
Because this loop is deterministic code,
adherence to the method is auditable
and does not depend on the model
electing to comply.
This is where the scientific method actually lives.

### Layer Four, Calibration and First-Class Abstention

The system needs trustworthy confidence
and a real ability to decline.
The proposer carries a calibration head
fitted with a [proper scoring rule][ref_scoring_rule]
so that its confidence values mean something.
Where stronger guarantees are required,
[conformal prediction][ref_conformal_prediction]
offers distribution-free coverage,
and recent work such as
[conformal uncertainty with correctness coverage][research_conformal]
applies it to open-ended generation.
The decoder has explicit actions
for decline and for request-rephrase,
not merely the implicit option
of generating a hedge.

Abstention must also be trained, not only thresholded.
[R-Tuning][research_r_tuning]
teaches a model to refuse questions
beyond its parametric knowledge,
and the [alignment for honesty][research_alignment_honesty] framework
trains a model to refuse when it lacks knowledge
without becoming uselessly conservative.
The controller reads the calibrated confidence,
the abstention policy,
and the critic verdict,
and routes to abstention or reframing
when confidence is low
and no verification path exists.
Selective prediction and abstention
are surveyed comprehensively in
[Know Your Limits (2024)][research_abstention_survey]
and pursued in work on
[risk-controlled refusal][research_risk_refusal].
This is where the fourth requirement
is implemented as an action
rather than a tone.

### Layer Five, A Deterministic Governance and Style Layer

Some rules can be checked mechanically.
A linter and policy checker
enforces the machine-checkable constraints,
such as not stating an ungrounded claim as fact
and defaulting to denial
for authorization decisions,
and can reject or repair an output
before it reaches the user.
The judgment-laden rules,
such as preferring correctness
over conversational harmony,
are pushed into the training signal
and the critic objective.
This keeps the rigid parts
out of the stochastic model.

### Layer Six, Interpretability Hooks

This layer is aspirational
and I hold it with low confidence
as currently achievable.
To the extent the field allows,
the system should ground its self-reports
in actual internal state
rather than generated narrative,
so that a claim about its own reasoning
is itself verifiable.
The partial calibration found by
[Kadavath and colleagues (2022)][research_self_knowledge]
and the detection of confabulation by
[semantic entropy][research_semantic_entropy]
suggest that some internal signal is recoverable,
but reading it faithfully
rather than approximating it
remains unsolved.
Without this layer,
the confabulated-introspection defect
leaves a permanent hole
in any honesty guarantee.

## A Concrete Instantiation

What follows is one illustrative configuration
with specific numbers.
I commit to figures
because a blueprint without numbers
is not a blueprint,
but these are a plausible design point,
not measurements from a built system.

The question of whether the components
are large or small models
has a nuanced answer.
The generative proposer is best served by scale,
so it is [large-language-model][ref_llm] class.
The verification and critic roles
are narrow and repetitive
and run many times per query,
which is precisely the regime
where [small language models][research_slm]
are argued by
[Belcak and colleagues (2025)][research_slm]
to be not only sufficient
but more economical.
So the correct description is a system
that uses one large model,
several small models,
and a symbolic and control layer together.

- **Proposer.**
  A [mixture-of-experts][ref_mixture_of_experts] model
  of approximately one hundred twenty billion total parameters
  with approximately fourteen billion active per token,
  in the lineage of the
  [Switch Transformer][research_switch_transformer],
  with a context window of approximately one hundred twenty-eight thousand tokens
  and adaptive per-token depth in the manner of
  [mixture-of-depths][research_mixture_of_depths].
  It can call external tools in the manner of
  [Toolformer][research_toolformer].
  It only proposes and never has final authority.
- **Critic ensemble.**
  Three to five small models
  of approximately seven to eight billion parameters each,
  each fine-tuned for a distinct refutation lens
  such as logical validity, evidential support,
  and methodological soundness,
  trained adversarially
  and shielded from any user-approval signal.
- **Process reward model.**
  A model of approximately seven billion parameters
  trained on step-level supervision
  following [Lightman and colleagues (2023)][research_process_supervision].
- **Calibration and abstention head.**
  A lightweight adapter on the proposer
  fitted with [temperature scaling][ref_calibration]
  and a [proper scoring rule][ref_scoring_rule],
  with a [conformal][ref_conformal_prediction] layer
  for coverage guarantees,
  feeding a selective-prediction threshold.
- **Retrieval subsystem.**
  A bi-encoder embedding model
  of roughly three hundred to six hundred million parameters
  over an external index
  of approximately ten million to one billion text chunks,
  using an approximate
  [nearest-neighbor][ref_nearest_neighbor] index,
  with provenance metadata on every chunk.
- **Symbolic layer.**
  A deterministic controller
  plus a [satisfiability-modulo-theories][ref_smt] solver
  such as [Z3][ref_z3],
  into which the falsifiability checks
  and the machine-checkable governance rules
  are compiled as constraint problems.

The dominant cost
is the multi-round propose-then-refute loop.
That cost is the price of rigor
and is not optimizable away
without weakening the method.

## Training Regime

Three departures from the conventional recipe matter most.
First, divorce the truthfulness reward
from the approval reward.
The truthfulness signal
comes from survival against the critic
and from retrieval and verifier checks,
not from whether a rater liked the answer.
The [Constitutional AI][research_constitutional_ai] approach
of training against explicit principles
with AI feedback is one concrete mechanism.
Second, train abstention and calibration
with proper scoring rules
and a curriculum that includes
ill-posed and unanswerable questions,
following [R-Tuning][research_r_tuning]
and [alignment for honesty][research_alignment_honesty],
so that declining is a learned competence
rather than a failure to be penalized.
Third, train the critics adversarially
and independently,
and rotate or ensemble them
so the generator cannot learn
to fool a single fixed critic.

## What Already Exists

A natural question is whether anyone
is building this or something close.
The honest answer has two parts.

In bounded formal domains,
something architecturally very close
to the full stack exists, works, and is funded.
Automated theorem proving is the clearest case.
[AlphaProof and AlphaGeometry][research_alphaproof],
from Google DeepMind,
pair a neural proposer
with a symbolic engine.
[AlphaGeometry][research_alphageometry],
published in Nature by
[Trinh and colleagues (2024)][research_alphageometry],
guides a symbolic deduction engine
with a neural language model.
AlphaProof generates candidate proofs
that are checked in [Lean][ref_lean],
a proof assistant
that mechanically validates every step.
[DeepSeek-Prover][research_deepseek_prover]
and [Harmonic's Aristotle][research_aristotle]
do the same with reinforcement learning
from proof-assistant feedback.
These systems exhibit principled abstention natively.
When no proof is found,
they return failure
rather than a plausible-sounding guess,
because the verifier
will not certify what it cannot prove.

For open-ended knowledge work,
the components exist
but are not assembled into one rigorous system.
Retrieval grounding with real citations
is shipping in scientific assistants
such as Consensus, Elicit, and Scite,
built on [retrieval-augmented generation][ref_rag],
and factuality verification is advancing through
[Self-RAG][research_self_rag],
[RARR][research_rarr],
[FActScore][research_factscore],
and [SAFE][research_safe].
Anti-sycophancy and calibrated uncertainty
are active research,
including [uncertainty-aware methods][research_smart]
that reduce sycophantic behavior
while preserving capability.
Neuro-symbolic verification
of general instruction following
is being prototyped,
for example in
[neuro-symbolic instruction-following verification][research_nsvif]
and in [solver-backed agentic oversight][research_formaljudge].
But these live in separate products and papers.
I found no general-purpose assistant
that combines retrieval grounding,
an adversarial critic ensemble,
a symbolic verifier,
calibrated abstention,
and a truthfulness-first objective
into a single governed system.

## The Crux, Generalizing Verification

The reason the complete system
is not a shipping product
is not lack of attention.
It is that the symbolic verifier,
the component that supplies the actual guarantee,
only gives that guarantee
where claims can be formalized
and mechanically checked.
Mathematics, code, and formal logic admit that.
Most natural-language questions do not.
There is no proof assistant
for whether a historical interpretation is sound
or whether an engineering tradeoff is wise.

So the rigorous version of the architecture
works exactly as far
as the formalizable frontier reaches,
and degrades to softer checks beyond it.
Search-augmented verification such as
[SAFE][research_safe]
extends checking into open domains,
but its guarantee is probabilistic agreement with sources,
not mechanical proof.
Generalizing a verifier-backed guarantee
from formal domains
to open-ended language
is the unsolved research problem
on which the whole design is gated.
This is a hard problem,
not an engineering oversight.
A recent position paper argues directly
that [logical soundness is not by itself
a reliable criterion][research_soundness_criterion]
for neuro-symbolic fact-checking with language models,
which is a warning
that even within the formal layer
a system can certify validity
while passing through a false premise.

## Failure Modes and Unaddressed Concerns

Honesty about the design
requires stating where it can fail.

Calibration degrades out of distribution.
A confidence value fitted on one distribution
is untrustworthy on inputs unlike the training data,
which is exactly when abstention matters most.
[Conformal prediction][ref_conformal_prediction]
mitigates this with distribution-free coverage,
but its guarantees weaken under distribution shift as well.

The critic can be wrong in both directions.
It can fail to refute a false claim,
or it can refute a true one,
and an overly aggressive critic
combined with a strict controller
yields a system that declines almost everything
and is useless.
There is no abstract value
for the right operating point.

The generator and critic
can share blind spots
through shared training data,
so their independence is partial
and the anti-sycophancy guarantee
is weaker than it appears.
This is the self-critique limitation
established by [Huang and colleagues (2023)][research_cannot_self_correct],
and it cuts against
the layer the design relies on most.
The optimizer can also engage in
[reward hacking][ref_reward_hacking],
gaming the critic or the verifier
rather than satisfying their intent.

Provenance quality bounds everything.
A confidently cited but wrong source
produces a confidently wrong fact
with a citation attached,
which is more dangerous
than an obvious guess.
This is also adjacent to
[model collapse][ref_model_collapse],
where recursive training on synthetic data
degrades the very corpus
the retrieval store would draw on,
a concern developed further in
[the case for human-authored long-form writing][related_post_long_form_writing].

Confabulated introspection is not solved,
only routed around.
Wherever the system reports on itself
rather than on an external verifiable object,
the honesty guarantee reverts
to the weak one.

Finally there is a cost
that is a consequence rather than a defect.
The system is slower,
more expensive in computation,
and more prone to declining
than a conventional assistant.
Taking the scientific method seriously
means accepting that.

## A Competing Vision

It is worth recording a more radical position
that contradicts the premise of this blueprint.
[LeCun (2022)][research_jepa]
argues that the language-model substrate itself
is the wrong foundation for reliable reasoning,
and that autonomous machine intelligence
requires a learned world model
trained by joint embedding prediction
rather than by next-token generation.
If that view is correct,
then wrapping a language model in verifiers
is treating a symptom,
and the better path is a different core
that grounds reasoning in a predictive model of the world.
I do not adjudicate this here.
I note it because intellectual honesty
requires acknowledging that the entire approach
of the present article
rests on a contested assumption,
namely that the language-model proposer is worth keeping
if it is properly constrained.

## Conclusion

The system that would adhere
to the scientific method,
value truth over agreement,
and decline when declining is honest
is not a better-trained language model.
It is a compound neuro-symbolic system
in which the network proposes,
a decoupled critic attempts refutation,
an external store grounds every fact,
a calibrated policy governs abstention,
and a deterministic symbolic layer
holds the guarantees.
The pieces are each supported in the literature.
The assembled whole is a hypothesis,
and its hardest unsolved problem
is extending verifier-backed guarantees
beyond the formalizable frontier.

There is no proven blueprint.
This article documents
the closest feasible approximation to one
that the current literature supports,
and it marks the boundary
between what is established
and what is speculative.
That boundary is itself the point.
A machine that could draw it reliably,
and refuse to cross it,
is the machine the four requirements describe.

## Future Reading

- Popper, *The Logic of Scientific Discovery* (1959)
- Irving, Christiano, and Amodei, "AI Safety via Debate" (2018)
- Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" (2020)
- Kadavath et al., "Language Models (Mostly) Know What They Know" (2022)
- Lightman et al., "Let's Verify Step by Step" (2023)
- Huang et al., "Large Language Models Cannot Self-Correct Reasoning Yet" (2023)
- Sharma et al., "Towards Understanding Sycophancy in Language Models" (2023)
- Farquhar et al., "Detecting Hallucinations in Large Language Models Using Semantic Entropy" (2024)
- Trinh et al., "Solving Olympiad Geometry without Human Demonstrations" (2024)
- Belcak et al., "Small Language Models are the Future of Agentic AI" (2025)

## References

- [Book, The Logic of Scientific Discovery][book_logic_scientific_discovery]
- [Reference, Automated Theorem Proving][ref_theorem_proving]
- [Reference, Calibration of Predictions][ref_calibration]
- [Reference, Conformal Prediction][ref_conformal_prediction]
- [Reference, Falsifiability][ref_falsifiability]
- [Reference, Hallucination in Artificial Intelligence][ref_hallucination]
- [Reference, Large Language Model][ref_llm]
- [Reference, Lean Proof Assistant][ref_lean]
- [Reference, Mixture of Experts][ref_mixture_of_experts]
- [Reference, Model Collapse][ref_model_collapse]
- [Reference, Nearest Neighbor Search][ref_nearest_neighbor]
- [Reference, Neuro-Symbolic AI][ref_neurosymbolic]
- [Reference, Proper Scoring Rule][ref_scoring_rule]
- [Reference, Reinforcement Learning from Human Feedback][ref_rlhf]
- [Reference, Retrieval-Augmented Generation][ref_rag]
- [Reference, Reward Hacking][ref_reward_hacking]
- [Reference, Satisfiability Modulo Theories][ref_smt]
- [Reference, Scientific Method][ref_scientific_method]
- [Reference, Z3 Theorem Prover][ref_z3]
- [Related Post, Long-Form Writing in the Age of Large Language Models][related_post_long_form_writing]
- [Related Post, The Error Correction Recursion Problem][related_post_error_correction]
- [Research, AI Safety via Debate][research_debate]
- [Research, Alignment for Honesty][research_alignment_honesty]
- [Research, AlphaProof and AlphaGeometry at IMO Silver-Medal Level][research_alphaproof]
- [Research, Aristotle IMO-Level Automated Theorem Proving][research_aristotle]
- [Research, Chain-of-Thought Prompting Elicits Reasoning][research_chain_of_thought]
- [Research, Concrete Problems in AI Safety][research_concrete_problems]
- [Research, Conformal Uncertainty with Correctness Coverage][research_conformal]
- [Research, Constitutional AI, Harmlessness from AI Feedback][research_constitutional_ai]
- [Research, DeepSeek-Prover Harnessing Proof Assistant Feedback][research_deepseek_prover]
- [Research, FActScore Atomic Evaluation of Factual Precision][research_factscore]
- [Research, FormalJudge Neuro-Symbolic Agentic Oversight][research_formaljudge]
- [Research, Know Your Limits, A Survey of Abstention][research_abstention_survey]
- [Research, Large Language Models Cannot Self-Correct Reasoning Yet][research_cannot_self_correct]
- [Research, Language Models Mostly Know What They Know][research_self_knowledge]
- [Research, Let's Verify Step by Step][research_process_supervision]
- [Research, LLM Critics Help Catch LLM Bugs][research_criticgpt]
- [Research, Mixture-of-Depths Adaptive Compute][research_mixture_of_depths]
- [Research, Neuro-Symbolic Verification on Instruction Following][research_nsvif]
- [Research, A Path Towards Autonomous Machine Intelligence][research_jepa]
- [Research, Position on Logical Soundness as a Criterion][research_soundness_criterion]
- [Research, RARR Researching and Revising Language Model Output][research_rarr]
- [Research, Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks][research_rag]
- [Research, R-Tuning Refusing Unknown Questions][research_r_tuning]
- [Research, Search-Augmented Factuality Evaluator][research_safe]
- [Research, Self-RAG Self-Reflective Retrieval-Augmented Generation][research_self_rag]
- [Research, Semantic Entropy for Detecting Hallucinations][research_semantic_entropy]
- [Research, Small Language Models are the Future of Agentic AI][research_slm]
- [Research, Solving Olympiad Geometry without Human Demonstrations][research_alphageometry]
- [Research, Switch Transformers Trillion-Parameter Sparsity][research_switch_transformer]
- [Research, Sycophancy Mitigation with Uncertainty-Aware Reasoning][research_smart]
- [Research, Toolformer Language Models Can Teach Themselves Tools][research_toolformer]
- [Research, Towards Understanding Sycophancy in Language Models][research_sycophancy]
- [Research, Trusted Uncertainty and Risk-Controlled Refusal][research_risk_refusal]
- [Research, TruthfulQA Measuring How Models Mimic Falsehoods][research_truthfulqa]
- [Research, Weak-to-Strong Generalization][research_weak_to_strong]

[book_logic_scientific_discovery]: https://en.wikipedia.org/wiki/The_Logic_of_Scientific_Discovery
[ref_theorem_proving]: https://en.wikipedia.org/wiki/Automated_theorem_proving
[ref_calibration]: https://en.wikipedia.org/wiki/Calibration_(statistics)
[ref_conformal_prediction]: https://en.wikipedia.org/wiki/Conformal_prediction
[ref_falsifiability]: https://en.wikipedia.org/wiki/Falsifiability
[ref_hallucination]: https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)
[ref_llm]: https://en.wikipedia.org/wiki/Large_language_model
[ref_lean]: https://en.wikipedia.org/wiki/Lean_(proof_assistant)
[ref_mixture_of_experts]: https://en.wikipedia.org/wiki/Mixture_of_experts
[ref_model_collapse]: https://en.wikipedia.org/wiki/Model_collapse
[ref_nearest_neighbor]: https://en.wikipedia.org/wiki/Nearest_neighbor_search
[ref_neurosymbolic]: https://en.wikipedia.org/wiki/Neuro-symbolic_AI
[ref_scoring_rule]: https://en.wikipedia.org/wiki/Scoring_rule
[ref_rlhf]: https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback
[ref_rag]: https://en.wikipedia.org/wiki/Retrieval-augmented_generation
[ref_reward_hacking]: https://en.wikipedia.org/wiki/Reward_hacking
[ref_smt]: https://en.wikipedia.org/wiki/Satisfiability_modulo_theories
[ref_scientific_method]: https://en.wikipedia.org/wiki/Scientific_method
[ref_z3]: https://en.wikipedia.org/wiki/Z3_Theorem_Prover
[related_post_long_form_writing]: {% post_url 2026-02-25-long_form_writing_in_age_of_large_language_models %}
[related_post_error_correction]: {% post_url 2026-03-12-error_correction_recursion_problem %}
[research_debate]: https://arxiv.org/abs/1805.00899
[research_alignment_honesty]: https://arxiv.org/abs/2312.07000
[research_alphaproof]: https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/
[research_aristotle]: https://arxiv.org/abs/2510.01346
[research_chain_of_thought]: https://arxiv.org/abs/2201.11903
[research_concrete_problems]: https://arxiv.org/abs/1606.06565
[research_conformal]: https://arxiv.org/abs/2407.00499
[research_constitutional_ai]: https://arxiv.org/abs/2212.08073
[research_deepseek_prover]: https://arxiv.org/abs/2408.08152
[research_factscore]: https://arxiv.org/abs/2305.14251
[research_formaljudge]: https://arxiv.org/abs/2602.11136
[research_abstention_survey]: https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00754/131566/Know-Your-Limits-A-Survey-of-Abstention-in-Large
[research_cannot_self_correct]: https://arxiv.org/abs/2310.01798
[research_self_knowledge]: https://arxiv.org/abs/2207.05221
[research_process_supervision]: https://arxiv.org/abs/2305.20050
[research_criticgpt]: https://arxiv.org/abs/2407.00215
[research_mixture_of_depths]: https://arxiv.org/abs/2404.02258
[research_nsvif]: https://arxiv.org/abs/2601.17789
[research_jepa]: https://openreview.net/pdf?id=BZ5a1r-kVsf
[research_soundness_criterion]: https://arxiv.org/abs/2604.04177
[research_rarr]: https://arxiv.org/abs/2210.08726
[research_rag]: https://arxiv.org/abs/2005.11401
[research_r_tuning]: https://arxiv.org/abs/2311.09677
[research_safe]: https://arxiv.org/abs/2403.18802
[research_self_rag]: https://arxiv.org/abs/2310.11511
[research_semantic_entropy]: https://www.nature.com/articles/s41586-024-07421-0
[research_slm]: https://arxiv.org/abs/2506.02153
[research_alphageometry]: https://www.nature.com/articles/s41586-023-06747-5
[research_switch_transformer]: https://arxiv.org/abs/2101.03961
[research_smart]: https://arxiv.org/abs/2509.16742
[research_toolformer]: https://arxiv.org/abs/2302.04761
[research_sycophancy]: https://arxiv.org/abs/2310.13548
[research_risk_refusal]: https://arxiv.org/abs/2509.01455
[research_truthfulqa]: https://arxiv.org/abs/2109.07958
[research_weak_to_strong]: https://arxiv.org/abs/2312.09390
