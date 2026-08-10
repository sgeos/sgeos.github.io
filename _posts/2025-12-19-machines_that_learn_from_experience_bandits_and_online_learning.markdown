---
layout: post
mathjax: true
comments: true
title:  "Machines That Learn From Experience: Bandits and Online Learning"
date:   2025-12-19 00:00:00 +0000
categories: artificial-intelligence machine-learning neuroscience
series: machines_that_learn_from_experience
series_title: Machines That Learn From Experience
series_index: 2
---

<!-- A251 -->
<script>console.log("A251");</script>

The multi-armed bandit problem is the theoretical foundation of experiential learning. A learner repeatedly selects one action from a finite set, receives a stochastic reward, and updates its beliefs to select subsequent actions well. The absence of dynamics, in the sense that actions do not change environment state, isolates the exploration-exploitation trade-off from the credit-assignment and state-representation problems that arise in the full Markov decision process treated in the next article. This article surveys bandits and their broader online-learning setting, walking the stochastic and adversarial bandit models, the upper confidence bound and Thompson sampling algorithm families, contextual and structured bandits, best-arm identification, non-stationary variants, and the connection to the broader online-learning literature on prediction with expert advice and online convex optimization. Article one of this series introduced the agent-environment loop in which bandits are the degenerate one-state case, subsequent articles treat the Markov decision process extension that reintroduces dynamics.

## The Bandit Problem

The classical stochastic multi-armed bandit problem specifies a set of $K$ arms indexed $a \in \{1, \ldots, K\}$, each associated with a reward distribution $\nu_a$ with mean $\mu_a$. At each round $t = 1, 2, \ldots, T$, the learner selects an arm $A_t$ and receives a reward $X_{t} \sim \nu_{A_t}$ drawn independently across rounds and arms. The learner's objective is to maximize the expected cumulative reward over the horizon $T$,

$$\mathbb{E}\left[\sum_{t=1}^T X_t\right]$$

or equivalently to minimize the regret, defined as the expected shortfall relative to always playing the optimal arm $a^* = \arg\max_a \mu_a$ with mean reward $\mu^* = \max_a \mu_a$,

$$R_T = T \mu^* - \mathbb{E}\left[\sum_{t=1}^T X_t\right] = \mathbb{E}\left[\sum_{t=1}^T (\mu^* - \mu_{A_t})\right]$$

Writing $\Delta_a = \mu^* - \mu_a$ for the suboptimality gap of arm $a$ and $N_a(T) = \sum_{t=1}^T \mathbb{1}\{A_t = a\}$ for the number of times arm $a$ has been played by round $T$, regret decomposes as

$$R_T = \sum_{a=1}^K \Delta_a \, \mathbb{E}[N_a(T)]$$

which makes explicit that regret accrues only from playing suboptimal arms.

A complementary objective is the simple regret at some fixed final round $T$, comparing the final recommendation to the optimal arm rather than accumulating regret over rounds,

$$r_T = \mu^* - \mu_{\hat{a}_T}$$

where $\hat{a}_T$ is the arm the learner recommends after $T$ rounds of interaction. Cumulative regret and simple regret can trade off against one another, since strategies that explore aggressively to identify the best arm may forego reward during exploration.

The Bernoulli bandit specializes the reward model to $X_t \in \{0, 1\}$ with $\nu_a = \text{Bernoulli}(\mu_a)$, useful both as a running example and as the canonical setting for early theoretical results. The Gaussian bandit specializes to $\nu_a = \mathcal{N}(\mu_a, \sigma^2)$ and provides the standard subgaussian analytical setting.

The problem is deceptively simple, and its analysis has driven the development of much of the modern theory of sequential decision-making under uncertainty. The learner faces a fundamental tension. To play the arm with the highest empirical mean maximizes short-term reward but risks missing a better arm whose empirical mean has been depressed by unlucky early samples. To play arms uniformly at random gathers information at the cost of forgoing reward from arms already known to be good. The bandit literature is the analysis of how to resolve this exploration-exploitation trade-off optimally.

## Historical Roots

The problem was posed in a decision-theoretic form by [Thompson 1933][research_thompson_1933] in the context of clinical trials, where the arms correspond to treatments and the rewards to patient outcomes. Thompson proposed the Bayesian strategy of sampling from a posterior distribution over arm parameters and playing the arm that appears best under the sample, an algorithm that would be revived and rigorously analyzed decades later.

[Robbins 1952][research_robbins_1952] formalized the sequential design of experiments problem in modern statistical language, initiating a research program that grew into the modern bandit literature. The [Robbins and Monro 1951][research_robbins_monro_1951] stochastic approximation paper of the previous year established the mathematical framework of iterative parameter updates from noisy samples that underlies both classical statistics and modern reinforcement learning. [Bellman 1956][research_bellman_1956] treated the bandit as a Markov decision process and gave a dynamic programming solution for the finite-horizon Bayesian case. [Gittins 1979][research_gittins_1979] index provided the optimal solution for the discounted infinite-horizon case, showing that the Bayesian problem decomposes into a per-arm index computation.

The frequentist theory reached its foundational result in [Lai and Robbins 1985][research_lai_robbins_1985], which established an asymptotic lower bound on regret for any consistent algorithm and constructed algorithms that achieve it. The bound provided the theoretical target that subsequent algorithm design has aimed to match.

[Auer Cesa-Bianchi and Fischer 2002][research_auer_cesa_bianchi_fischer_2002] introduced the UCB1 algorithm, providing a simple explicit rule that achieves $\mathcal{O}(\log T)$ regret in the stochastic setting with a small multiplicative constant. In the same year, [Auer Cesa-Bianchi Freund and Schapire 2002][research_auer_cesa_bianchi_freund_schapire_2002] developed the EXP3 algorithm for the adversarial bandit setting, providing $\mathcal{O}(\sqrt{KT \log K})$ regret without stochastic assumptions.

The 2010s produced substantial refinement. [Chapelle and Li 2011][research_chapelle_li_2011] empirical study demonstrated that Thompson sampling matched or exceeded UCB variants in practice, sparking renewed interest in the Bayesian family. [Bubeck 2012][book_bubeck_2012] monograph and [Bubeck and Cesa-Bianchi 2012][research_bubeck_cesa_bianchi_2012] survey provided comprehensive theoretical treatment of the field circa 2012, and [Lattimore and Szepesvari 2020][book_lattimore_szepesvari_2020] textbook consolidated the field into a modern reference standard.

## Stochastic Multi-Armed Bandits and Regret

Under standard assumptions, rewards are supported on a bounded interval such as $[0, 1]$ or are subgaussian with known constant. The empirical mean of arm $a$ after $n$ pulls,

$$\hat{\mu}_a(n) = \frac{1}{n} \sum_{i=1}^{n} X_{a, i}$$

concentrates around $\mu_a$ at the rate given by Hoeffding's inequality,

$$P\left(|\hat{\mu}_a(n) - \mu_a| \geq \epsilon\right) \leq 2 \exp(-2 n \epsilon^2)$$

for rewards in $[0, 1]$. For rewards with a subgaussian tail with parameter $\sigma$, the corresponding bound is

$$P\left(|\hat{\mu}_a(n) - \mu_a| \geq \epsilon\right) \leq 2 \exp\left(-\frac{n \epsilon^2}{2 \sigma^2}\right)$$

This concentration is the fundamental tool of the frequentist bandit analysis. It lets the learner construct confidence intervals around empirical means that shrink at rate $\mathcal{O}(1/\sqrt{n})$ and use those intervals to decide when the empirical ordering of arms is trustworthy.

Three notions of regret are worth distinguishing. The pseudo-regret

$$\bar{R}_T = T \mu^* - \sum_{t=1}^T \mu_{A_t}$$

compares against the true optimal mean and is what most stochastic bandit algorithms directly bound. The expected regret $R_T = \mathbb{E}[\bar{R}_T]$ takes expectation over the randomness of arm selection and reward realization. The Bayesian regret

$$R_T^{\text{Bayes}} = \mathbb{E}_{\theta \sim \pi}[R_T(\theta)]$$

further averages over a prior $\pi$ on the environment parameters $\theta$ and is the natural analysis object for Thompson sampling and Gittins-index algorithms.

Simple exploration strategies illustrate the regret landscape. Pure exploration plays each arm uniformly, incurring linear regret $R_T = \Theta(T)$. Pure exploitation plays the empirically best arm after some initial exploration but can lock onto a suboptimal arm and incur linear regret. The $\epsilon$-greedy strategy plays a random arm with probability $\epsilon_t$ decaying as $1/t$ and the empirically best arm otherwise, achieving

$$R_T^{\epsilon\text{-greedy}} = \mathcal{O}\!\left(\frac{K \log T}{\Delta_{\min}^2}\right)$$

under careful tuning of $\epsilon_t$, where $\Delta_{\min} = \min_{a : \Delta_a > 0} \Delta_a$. Explore-then-commit similarly explores for a fixed initial period and commits thereafter, achieving

$$R_T^{\text{ETC}} = \mathcal{O}\!\left(T^{2/3} (K \log K)^{1/3}\right)$$

when the exploration budget is set optimally in a distribution-independent sense, and $\mathcal{O}(\log T / \Delta_{\min}^2)$ when the gap $\Delta_{\min}$ is known.

## Regret Lower Bounds

The [Lai and Robbins 1985][research_lai_robbins_1985] lower bound establishes a fundamental information-theoretic limit for consistent algorithms on stochastic bandits. Recall that the Kullback-Leibler divergence between two probability measures $P$ and $Q$ absolutely continuous with respect to a common dominating measure is

$$\text{KL}(P \, \| \, Q) = \int p(x) \log \frac{p(x)}{q(x)} \, dx$$

and is zero if and only if $P = Q$ almost everywhere. Let $\text{KL}(\nu_a \, \| \, \nu^*)$ denote this divergence between the reward distributions of a suboptimal arm and the optimal arm. Any consistent algorithm on a parametric family of distributions satisfies asymptotically

$$\liminf_{T \to \infty} \frac{R_T}{\log T} \geq \sum_{a: \Delta_a > 0} \frac{\Delta_a}{\text{KL}(\nu_a \, \| \, \nu^*)}$$

The bound is tight in the sense that algorithms exist achieving this rate, and it establishes the $\log T$ scaling as unavoidable for any algorithm that adapts sensibly to unknown reward distributions.

For the worst-case adversarial bandit setting, [Auer Cesa-Bianchi Freund and Schapire 2002][research_auer_cesa_bianchi_freund_schapire_2002] and subsequent work established the minimax lower bound

$$R_T = \Omega(\sqrt{KT})$$

which is achieved up to logarithmic factors by the EXP3 family of algorithms. The difference in scaling between stochastic ($\log T$) and adversarial ($\sqrt{T}$) settings reflects the fact that the adversarial setting denies the learner access to concentration inequalities that would otherwise let it identify the optimal arm.

Instance-dependent and instance-independent bounds correspond to different measures of algorithm performance. Instance-dependent bounds like the Lai-Robbins bound scale with the arm gaps $\Delta_a$ and become tight for problems with well-separated arms. Instance-independent bounds like the minimax $\sqrt{T}$ bound scale uniformly across problem instances and reflect worst-case performance.

## Upper Confidence Bound Methods

The upper confidence bound family of algorithms implements the principle of optimism in the face of uncertainty. At each round, the algorithm plays the arm with the largest upper bound on a confidence interval around its empirical mean. The most widely known variant is UCB1 from [Auer Cesa-Bianchi and Fischer 2002][research_auer_cesa_bianchi_fischer_2002], which selects

$$A_t = \arg\max_a \left[ \hat{\mu}_a(N_a(t-1)) + \sqrt{\frac{2 \log t}{N_a(t-1)}} \right]$$

where the second term is a confidence radius derived from Hoeffding's inequality. UCB1 achieves the regret bound

$$R_T \leq \sum_{a: \Delta_a > 0} \frac{8 \log T}{\Delta_a} + \left(1 + \frac{\pi^2}{3}\right) \sum_{a=1}^K \Delta_a$$

which matches the Lai-Robbins lower bound up to constants.

Refinements of UCB1 tighten the confidence radius by using more sensitive concentration inequalities. UCB-V from [Audibert Munos Szepesvari 2009][research_audibert_munos_szepesvari_2009] incorporates the empirical variance, giving

$$A_t = \arg\max_a \left[ \hat{\mu}_a + \sqrt{\frac{2 \hat{V}_a \log t}{N_a}} + \frac{3 \log t}{N_a} \right]$$

which is tighter for arms with low variance. KL-UCB from [Cappé et al 2013][research_cappe_et_al_2013] uses the KL divergence-based confidence set,

$$A_t = \arg\max_a \max\left\{ q \in [0, 1] : N_a(t-1) \cdot \text{KL}(\hat{\mu}_a, q) \leq \log t + c \log \log t \right\}$$

and achieves the Lai-Robbins constant exactly.

For linear bandits with feature vectors $x_a \in \mathbb{R}^d$ and unknown parameter $\theta \in \mathbb{R}^d$, the LinUCB algorithm of [Li et al 2010][research_li_et_al_2010] and its predecessors constructs confidence ellipsoids on $\theta$ and plays

$$A_t = \arg\max_a \left[ \hat{\theta}_t^\top x_a + \beta_t \| x_a \|_{V_t^{-1}} \right]$$

where the ridge-regularized design matrix is

$$V_t = \lambda I + \sum_{s=1}^{t-1} x_{A_s} x_{A_s}^\top$$

and the ridge-regularized least-squares estimate is

$$\hat{\theta}_t = V_t^{-1} \sum_{s=1}^{t-1} x_{A_s} X_s$$

Linear UCB achieves regret

$$R_T = \mathcal{O}\!\left(d \sqrt{T} \log T\right)$$

in the linear stochastic setting, replacing the arm count $K$ in the bound with the ambient dimension $d$. [Abbasi-Yadkori Pál and Szepesvári 2011][research_abbasi_yadkori_pal_szepesvari_2011] improved the analysis with self-normalized concentration inequalities, giving the tighter bound $R_T = \mathcal{O}(d \sqrt{T \log T})$ under standard regularity conditions. The minimax-optimal MOSS algorithm of [Audibert and Bubeck 2009][research_audibert_bubeck_2009] achieves the improved bound $R_T = \mathcal{O}(\sqrt{KT})$ in the finite-armed adversarial-adjacent setting.

## Thompson Sampling

Thompson sampling implements optimism in the face of uncertainty through Bayesian posterior sampling rather than confidence-bound construction. The algorithm maintains a posterior distribution over arm parameters and at each round samples from the posterior, then plays the arm that maximizes expected reward under the sample. For Bernoulli bandits with a Beta prior, the algorithm proceeds as follows.

Maintain for each arm $a$ counts of successes $\alpha_a$ and failures $\beta_a$, initialized at $\alpha_a = \beta_a = 1$ for a uniform prior. At each round $t$, sample $\tilde{\mu}_a \sim \text{Beta}(\alpha_a, \beta_a)$ for each arm and play $A_t = \arg\max_a \tilde{\mu}_a$. Upon receiving reward $X_t \in \{0, 1\}$, update $\alpha_{A_t} \leftarrow \alpha_{A_t} + X_t$ and $\beta_{A_t} \leftarrow \beta_{A_t} + (1 - X_t)$.

The Bayesian analysis of Thompson sampling due to [Russo and Van Roy 2014][research_russo_van_roy_2014] gives the Bayesian regret bound

$$R_T^{\text{Bayes}} \leq \sqrt{\frac{1}{2} T H(A^*)}$$

where $H(A^*)$ is the entropy of the prior over the optimal arm. The frequentist regret analysis of [Agrawal and Goyal 2012][research_agrawal_goyal_2012] shows Thompson sampling achieves $\mathcal{O}(\log T)$ instance-dependent regret with the Lai-Robbins constant asymptotically. [Kaufmann Korda and Munos 2012][research_kaufmann_korda_munos_2012] independently established non-asymptotic finite-time bounds for Thompson sampling on Bernoulli bandits that match the Lai-Robbins constant.

The empirical success of Thompson sampling documented by [Chapelle and Li 2011][research_chapelle_li_2011] extends to structured settings including linear, Gaussian process, and neural network bandits. For linear Thompson sampling, [Agrawal and Goyal 2013][research_agrawal_goyal_2013] established the frequentist regret bound

$$R_T = \tilde{\mathcal{O}}\!\left(d^{3/2} \sqrt{T}\right)$$

matching the LinUCB scaling in $T$ but with a worse polynomial dependence on dimension. The information-theoretic analysis of Thompson sampling has proved a productive framework for extending the algorithm and its analysis to reinforcement learning, where posterior sampling for reinforcement learning under the name PSRL provides a Bayesian analogue to optimistic reinforcement learning treated in article three.

## Adversarial Bandits and EXP3

The adversarial bandit setting drops the stochastic assumption. An adversary selects reward sequences without stochastic structure, potentially with knowledge of the learner's algorithm but not its randomization. The setting is the natural model for problems in which stochastic reward assumptions are implausible, such as online advertising against strategic advertisers or repeated games against sophisticated opponents.

The EXP3 algorithm of [Auer Cesa-Bianchi Freund and Schapire 2002][research_auer_cesa_bianchi_freund_schapire_2002] maintains exponentially-weighted probabilities over arms. Let $\eta$ be the learning rate and $\hat{X}_t(a)$ the importance-weighted reward estimate

$$\hat{X}_t(a) = \frac{X_t \, \mathbb{1}\{A_t = a\}}{p_t(a)}$$

where $p_t(a)$ is the algorithm's probability of playing arm $a$ at round $t$. Cumulative weights are updated as

$$w_t(a) = w_{t-1}(a) \exp(\eta \hat{X}_t(a))$$

and probabilities as

$$p_{t+1}(a) = (1 - \gamma) \frac{w_t(a)}{\sum_{a'} w_t(a')} + \frac{\gamma}{K}$$

where $\gamma$ is a mixing parameter that ensures exploration. With learning rate tuned to

$$\eta = \sqrt{\frac{2 \log K}{T K}}$$

EXP3 achieves regret bound

$$R_T \leq 2 \sqrt{T K \log K}$$

against any adversary. The matching lower bound

$$R_T = \Omega(\sqrt{T K})$$

holds for the adversarial setting, showing that EXP3 is nearly minimax-optimal up to logarithmic factors. The dependence on $T$ is $\sqrt{T}$ rather than $\log T$, reflecting the harder adversarial setting.

Refinements include EXP3.P, which provides high-probability guarantees rather than expected-regret bounds, and EXP3-IX, which uses implicit exploration through modified importance weights. The follow-the-perturbed-leader family gives an alternative algorithmic strategy for adversarial online learning that generalizes beyond the finite-armed setting.

The best-of-both-worlds family of algorithms achieves near-optimal regret in both stochastic and adversarial settings simultaneously, without prior knowledge of which regime the environment is in. [Bubeck and Slivkins 2012][research_bubeck_slivkins_2012] provided the first such algorithm with $\mathcal{O}(\log^3 T)$ regret in the stochastic setting and $\mathcal{O}(\sqrt{T \log T})$ regret in the adversarial setting. The [Zimmert and Seldin 2019][research_zimmert_seldin_2019] Tsallis-INF algorithm uses a Tsallis entropy regularizer

$$x_{t+1} = \arg\min_{p \in \Delta_K} \left[ \langle p, \hat{L}_t \rangle - \eta \sum_a \sqrt{p_a} \right]$$

and simultaneously achieves the optimal $\mathcal{O}(\sqrt{TK})$ adversarial regret and the $\mathcal{O}(\log T / \Delta)$ instance-dependent stochastic regret, closing a long-standing gap between the two settings.

## Contextual Bandits

Contextual bandits generalize the setting by providing the learner with side information at each round. At round $t$ the learner observes a context $x_t \in \mathcal{X}$, selects an arm $A_t \in \{1, \ldots, K\}$, and receives a reward whose distribution depends on both context and arm.

The stochastic contextual bandit assumes rewards follow some function of context and arm plus noise,

$$X_t = f(x_t, A_t) + \eta_t$$

with $\eta_t$ zero-mean. The learner's task is to learn a policy $\pi : \mathcal{X} \to \{1, \ldots, K\}$ that maximizes expected reward.

For linear contextual bandits, the reward function has the form $f(x, a) = \theta_a^\top x$ for arm-parameters $\theta_a$, or $f(x, a) = \theta^\top \phi(x, a)$ for a shared parameter with joint context-action features. LinUCB and Thompson sampling extend directly, and the regret analyses generalize with the number of arms replaced by an effective dimension parameter.

For general contextual bandits without linear structure, the epoch-greedy family of algorithms of [Langford and Zhang 2007][research_langford_zhang_2007], the exp4 algorithm of [Auer Cesa-Bianchi Freund Schapire 2002][research_auer_cesa_bianchi_freund_schapire_2002], and the exp4.P variant of [Beygelzimer Langford Li Reyzin Schapire 2011][research_beygelzimer_et_al_2011] provide reduction-based algorithms with regret bounds

$$R_T = \mathcal{O}\left(\sqrt{T K \log |\Pi|}\right)$$

where $\lvert \Pi \rvert$ is the cardinality of a fixed policy class. For infinite policy classes indexed by a bounded-VC-dimension hypothesis space, the bound generalizes with $\log \lvert \Pi \rvert$ replaced by the appropriate complexity measure.

Contextual bandits provide the algorithmic foundation for personalized recommendation, targeted content selection, and other applied problems that this series does not treat directly. The theoretical apparatus that supports the applied deployments is treated here.

## Structured and Linear Bandits

Structured bandits exploit known relationships among arm rewards to reduce sample complexity. The linear bandit setting assumes rewards are linear in a feature vector $\phi(a) \in \mathbb{R}^d$ associated with each arm,

$$\mu_a = \theta^\top \phi(a)$$

for unknown parameter $\theta$. The dimension $d$ replaces the number of arms $K$ in regret bounds, which is advantageous when $K \gg d$ or when $K$ is infinite.

Kernel bandits generalize the linear structure to reproducing kernel Hilbert spaces, giving nonparametric algorithms with regret bounds in terms of an information gain quantity of the kernel. The GP-UCB algorithm of [Srinivas et al 2010][research_srinivas_et_al_2010] provides an early treatment, achieving regret

$$R_T = \mathcal{O}\!\left(\sqrt{T \gamma_T \log T}\right)$$

where the maximum information gain over $T$ observations is

$$\gamma_T = \max_{|S| \leq T} \frac{1}{2} \log \det(I + \sigma^{-2} K_S)$$

with $K_S$ the kernel Gram matrix on the sample set $S$. The information gain $\gamma_T$ replaces the ambient dimension in the linear case and characterizes the sample complexity of the kernel bandit problem.

Combinatorial bandits treat problems where the arm set has combinatorial structure, such as ranking, matching, or path selection, and the learner receives feedback on the selected combination rather than individual components. The [Cesa-Bianchi and Lugosi 2012][research_cesa_bianchi_lugosi_2012] treatment of combinatorial prediction and its bandit specialization achieves regret bounds

$$R_T = \mathcal{O}(m \sqrt{T \log |\mathcal{A}|})$$

where $m$ is the size of each combinatorial action and $\lvert \mathcal{A} \rvert$ is the combinatorial action set size, exploiting the combinatorial structure to avoid regret bounds that scale linearly with the exponentially large arm set.

Continuum-armed or Lipschitz bandits allow an uncountable action set with rewards Lipschitz-continuous in the action. The [Kleinberg Slivkins and Upfal 2008][research_kleinberg_slivkins_upfal_2008] zooming algorithm achieves regret

$$R_T = \tilde{\mathcal{O}}(T^{(d+1)/(d+2)})$$

where $d$ is the zooming dimension of the problem, an information-theoretic quantity capturing the effective difficulty. The regret scaling $T^{(d+1)/(d+2)}$ interpolates between $\sqrt{T}$ (small $d$) and $T$ (dense reward landscape).

The specialized literature includes interval bandits, extreme-value bandits, adversarial bandits with structure, and bandits with corruption. Each variant modifies the standard setup along one dimension and admits a specialized analysis.

## Bandits with Non-Standard Feedback

The classical bandit assumes the learner observes a scalar reward from the chosen arm. Real-world sequential decision problems frequently violate this assumption in structured ways, and the bandit literature has developed specialized algorithms and analyses for the corresponding variants.

Dueling bandits [Yue Broder Kleinberg and Joachims 2012][research_yue_et_al_2012] replace scalar reward feedback with pairwise preference comparisons. At each round the learner selects two arms $A_t^{(1)}, A_t^{(2)}$ and observes a binary preference $X_t \sim \text{Bernoulli}(p_{A_t^{(1)}, A_t^{(2)}})$ where $p_{a, b}$ is the probability that $a$ is preferred to $b$. The regret is measured against the Condorcet winner or Copeland winner of the preference tournament. Regret bounds of $\mathcal{O}(K^2 \log T)$ or better are achievable under standard conditions such as strong stochastic transitivity. Dueling bandits connect to preference-based reinforcement learning treated in article eleven and to the reinforcement learning from human feedback methods used in language model post-training.

Delayed feedback bandits observe rewards only after a delay that may depend on the arm played, the environment, or the round. The [Joulani Gyorgy and Szepesvari 2013][research_joulani_gyorgy_szepesvari_2013] queuing-based framework reduces the delayed-feedback problem to a black-box reduction over undelayed algorithms, achieving regret

$$R_T = \mathcal{O}(R_T^{\text{undelayed}} + \bar{D} \sqrt{T})$$

where $\bar{D}$ is the expected delay. The framework covers stochastic, adversarial, and contextual settings uniformly.

Graph-structured feedback [Alon Cesa-Bianchi Gentile Mansour 2013][research_alon_et_al_2013] allows the learner to observe rewards for a subset of arms determined by a feedback graph $G$. Full-information feedback corresponds to the complete graph and bandit feedback to the empty graph (self-loops only). Regret bounds interpolate between these extremes through spectral properties of $G$, giving

$$R_T = \mathcal{O}(\sqrt{\alpha(G) T \log K})$$

where $\alpha(G)$ is the independence number of the feedback graph. Applications include social-network content recommendation, where selecting one item may reveal preferences for related items.

Bandits with corruption or robust bandits [Lykouris Mirrokni Leme 2018][research_lykouris_mirrokni_leme_2018] allow an adversary to corrupt reward observations subject to a corruption budget $C$. Robust variants of UCB and Thompson sampling achieve regret bounds that gracefully degrade with $C$, of the form $\mathcal{O}(K \log T / \Delta + K C)$ for the stochastic setting with bounded corruption.

## Bandit Convex Optimization

Bandit convex optimization extends the online convex optimization framework of the online learning section to the setting in which the learner observes only the function value at the played point, rather than the gradient. The learner selects $x_t \in \mathcal{K}$ for $\mathcal{K}$ a convex subset of $\mathbb{R}^d$, receives $f_t(x_t)$ for convex $f_t$, and does not observe $\nabla f_t$.

The [Flaxman Kalai and McMahan 2005][research_flaxman_kalai_mcmahan_2005] one-point gradient estimator constructs a stochastic gradient from a perturbation. For a smoothing parameter $\delta$ and a random unit vector $u$, the estimator

$$\hat{g}_t = \frac{d}{\delta} f_t(x_t + \delta u) u$$

is an unbiased estimator of the gradient of a smoothed version of $f_t$. Feeding this estimator to online gradient descent yields regret

$$R_T = \mathcal{O}(T^{3/4})$$

for general convex losses. The bound was subsequently improved to $\mathcal{O}(\sqrt{T})$ under stronger smoothness assumptions by [Bubeck Cesa-Bianchi and Kakade 2012][research_bubeck_cesa_bianchi_kakade_2012] and to matching lower bounds by [Bubeck Eldan and Lee 2017][research_bubeck_eldan_lee_2017] for smooth strongly convex losses.

Bandit convex optimization connects to derivative-free optimization, evolution strategies treated in article twelve, and zeroth-order optimization more broadly. The theoretical framework provides regret bounds that are dimension-independent up to logarithmic factors under strong smoothness assumptions, making it applicable to high-dimensional optimization problems where gradient information is unavailable.

## Best-Arm Identification and Pure Exploration

The pure exploration setting replaces the regret minimization objective with an arm-identification objective. The learner interacts with the bandit for some budget or until a stopping condition and outputs a guess for the optimal arm. Regret over the interaction is not the performance criterion, the probability of misidentification is.

The fixed-budget setting fixes the number of arm pulls in advance and analyzes the probability of incorrect identification. The fixed-confidence setting fixes the probability of incorrect identification and analyzes the expected number of pulls. Both settings have well-developed theory including instance-dependent lower bounds and matching algorithms.

The successive elimination algorithm of [Even-Dar Mannor and Mansour 2006][research_even_dar_mannor_mansour_2006] iteratively rules out arms whose empirical means fall too far below the current best. At each round it eliminates any arm $a$ satisfying

$$\hat{\mu}_{\max}(t) - \hat{\mu}_a(t) > 2 \sqrt{\frac{\log(4 K t^2 / \delta)}{N_a(t)}}$$

with confidence parameter $\delta$, ensuring correct identification with probability $1 - \delta$. The track-and-stop algorithm of [Garivier and Kaufmann 2016][research_garivier_kaufmann_2016] achieves the instance-optimal sample complexity for fixed-confidence identification asymptotically, matching the lower bound

$$\mathbb{E}[\tau_\delta] \geq T^*(\mu) \log(1/\delta)$$

where $T^*(\mu)$ is a complex information-theoretic quantity involving a maxmin over allocation vectors and the KL divergences among reward distributions.

Pure exploration extends beyond best-arm identification to top-$k$ identification, threshold bandits, and Pareto-front identification in multi-objective settings. The connection to bayesian optimization and to active learning is direct.

## Non-Stationary and Restless Bandits

Real-world reward distributions frequently drift, jump, or evolve in ways that violate the stationary assumption of the classical bandit. Non-stationary bandit theory develops algorithms that maintain low regret against non-stationary environments.

The abrupt-change setting assumes that arm rewards change at discrete change-points that partition the horizon into stationary segments. The sliding-window UCB algorithm of [Garivier and Moulines 2011][research_garivier_moulines_2011] uses only the most recent $\tau$ samples to construct confidence bounds,

$$A_t = \arg\max_a \left[ \hat{\mu}_a^{\tau}(t) + \sqrt{\frac{\xi \log \min(t, \tau)}{N_a^{\tau}(t)}} \right]$$

where $\hat{\mu}_a^{\tau}(t)$ is the empirical mean over the sliding window and $N_a^{\tau}(t)$ the count of pulls within it. Sliding-window variants achieve regret bounds of $\mathcal{O}(\sqrt{S T \log T})$ where $S$ is the number of change-points.

The smoothly-varying setting assumes that arm rewards evolve continuously, possibly with a bounded rate of change. Discounted UCB variants apply a discount factor $\gamma \in (0, 1)$ to older samples,

$$\hat{\mu}_a^{\gamma}(t) = \frac{\sum_{s=1}^{t} \gamma^{t-s} \mathbb{1}\{A_s = a\} X_s}{\sum_{s=1}^{t} \gamma^{t-s} \mathbb{1}\{A_s = a\}}$$

and give bounds involving the drift rate.

Restless bandits allow arm rewards to evolve according to Markov chains whose transitions depend on whether the arm is played. The problem is generally PSPACE-hard, but the [Whittle 1988][research_whittle_1988] index provides a widely-used heuristic that computes an arm-index

$$W_a(x) = \inf\{ \lambda : \text{it is optimal to activate arm } a \text{ in state } x \text{ under passive-arm subsidy } \lambda \}$$

with theoretical guarantees under indexability conditions.

Contextual non-stationary bandits combine the context and non-stationarity settings and require algorithms sensitive to both spatial and temporal structure.

## Online Learning Beyond Bandits

The bandit setting is a special case of the broader online learning framework. Prediction with expert advice generalizes the multi-armed bandit to problems in which the learner observes advice from a finite set of experts, selects a distribution over experts, incurs a loss based on the outcome, and observes losses for all experts rather than only the selected one. Foundational treatments include [Vovk 1990][research_vovk_1990] aggregating strategy analysis, [Littlestone and Warmuth 1994][research_littlestone_warmuth_1994] weighted majority algorithm, and [Cesa-Bianchi et al 1997][research_cesa_bianchi_et_al_1997] treatment of prediction with expert advice as a fundamental online-learning primitive.

The Hedge algorithm of [Freund and Schapire 1997][research_freund_schapire_1997] provides multiplicative weight updates

$$w_{t+1}(a) = w_t(a) \exp(-\eta L_t(a))$$

where $L_t(a)$ is the observed loss of expert $a$ at round $t$, and plays experts with probability proportional to weights. Hedge achieves regret bound

$$R_T \leq \sqrt{2 T \log N}$$

against the best expert in hindsight, where $N$ is the number of experts. The bandit setting corresponds to observing only the loss of the selected expert, which yields the harder EXP3 problem.

Online convex optimization further generalizes to problems in which the learner selects a point in a convex set at each round and receives a convex loss function. The online gradient descent algorithm of [Zinkevich 2003][research_zinkevich_2003] projects a gradient step back onto the feasible set,

$$x_{t+1} = \Pi_{\mathcal{K}}\!\left[x_t - \eta \nabla f_t(x_t)\right]$$

and achieves regret bound

$$R_T \leq \frac{D^2}{2 \eta} + \frac{\eta G^2 T}{2}$$

where $D$ is the diameter of the feasible set $\mathcal{K}$ and $G$ is a bound on the gradient norm. With $\eta = D/(G\sqrt{T})$ the bound becomes $R_T \leq D G \sqrt{T}$. Follow-the-regularized-leader generalizes the framework, selecting

$$x_{t+1} = \arg\min_{x \in \mathcal{K}} \left[ \sum_{s=1}^{t} f_s(x) + \frac{1}{\eta} R(x) \right]$$

for a strongly convex regularizer $R$. The follow-the-perturbed-leader algorithm of [Kalai and Vempala 2005][research_kalai_vempala_2005] provides an efficient alternative using random perturbation of the cumulative loss, especially useful for structured decision sets. Mirror descent extends the Euclidean projection to Bregman divergences, unifying multiplicative weights, exponentiated gradient, and other algorithms as instances of a common framework. The [Hazan 2016][book_hazan_2016] textbook provides a comprehensive treatment.

Non-stationary online learning extends the framework to the setting in which the comparator changes over time. Dynamic regret bounds compete against a sequence of comparators rather than a single best expert, and the tracking-the-best-expert framework of [Herbster and Warmuth 1998][research_herbster_warmuth_1998] provides the foundational analysis.

Adaptive online learning algorithms achieve regret bounds that adapt to problem-dependent quantities such as gradient variance, function smoothness, or distributional structure. The framework connects to stochastic optimization, statistical learning theory, and the analysis of stochastic gradient descent that underlies deep learning practice.

## Neuroscience and Psychology Connections

The bandit framework has deep connections to the psychology and neuroscience of decision-making under uncertainty, connections that this series treats more thoroughly in articles fourteen and fifteen but which merit summary here.

Foraging theory in behavioral ecology treats animals as bandit-like decision-makers choosing among patches with unknown reward distributions. The marginal value theorem of [Charnov 1976][research_charnov_1976] gives the optimal patch-departure rule for a foraging animal balancing the reward from the current patch against the expected reward from switching, and its structure parallels the exploration-exploitation trade-off in bandits.

Human bandit experiments have documented systematic departures from optimal bandit strategies. [Daw et al 2006][research_daw_et_al_2006] compared human choice behavior on a four-armed bandit task to model predictions from softmax exploration, epsilon-greedy exploration, and Bayesian exploration policies, finding evidence for softmax-like directed exploration matched by activation in frontopolar cortex and intraparietal sulcus. [Cohen McClure and Yu 2007][research_cohen_mcclure_yu_2007] framed the exploration-exploitation trade-off in terms of neuromodulator function, hypothesizing distinct roles for noradrenaline and dopamine in random and directed exploration.

Prefrontal cortex has been identified as a substrate for representing expected value and uncertainty in bandit-like tasks. [Behrens Woolrich Walton and Rushworth 2007][research_behrens_et_al_2007] identified anterior cingulate cortex as tracking volatility of reward contingencies, providing a neural substrate for adaptive learning rates that respond to environmental non-stationarity. The Bayesian bandit interpretation of these findings suggests that human decision-makers maintain approximate posterior distributions over arm parameters and update them in response to observed rewards.

The correspondence between animal and human bandit-task performance and algorithmic classes is imperfect. Systematic biases including probability matching, myopic exploration, and reward-magnitude insensitivity all appear in the empirical literature. Article fifteen treats the psychology of learning as a distinct topic and revisits the imperfect algorithmic mapping.

## Empirical Landscape and Benchmarks

The bandit framework acquired its practical character through deployment in applied settings and through standardized empirical benchmarks. As with article one, this survey treats the empirical landscape briefly rather than the applications directly, given the series science-and-theory focus.

Recommendation systems have been a major application setting. The [Li et al 2010][research_li_et_al_2010] LinUCB deployment for news recommendation on Yahoo Front Page provided a canonical empirical validation of contextual bandit theory, showing improved click-through rates against non-contextual baselines. Subsequent recommendation-system deployments have used contextual and combinatorial bandit algorithms at scale across content platforms.

Clinical trial design, the original motivation of [Thompson 1933][research_thompson_1933], has seen renewed adoption of adaptive-allocation methods with bandit theoretical foundations. Response-adaptive randomization allocates patients preferentially to treatments with promising interim results, treating patient allocation as a bandit problem while maintaining the statistical validity of the resulting trial.

Online advertising and online auction settings use bandit and adversarial-bandit theory extensively. The exchange between advertiser and platform is repeated over time under distributional and adversarial reward dynamics, and both LinUCB and Thompson sampling have deployment experience at scale.

A/B testing platforms use adaptive-allocation bandit methods to reduce sample sizes for detecting treatment effects. The pure-exploration and best-arm-identification literatures treated above provide the theoretical foundations for adaptive experimentation frameworks such as Bayesian A/B testing and multi-armed bandit optimization.

Standardized benchmark suites for bandit algorithms include the Contextual Bandit Bakeoff of [Bietti Agarwal and Langford 2021][research_bietti_agarwal_langford_2021], which provides evaluation datasets and standardized protocols for comparing contextual bandit algorithms across hundreds of tasks derived from classification datasets [Vowpal Wabbit][ref_vowpal_wabbit] provides open-source reference implementations of contextual bandit algorithms with production deployment experience.

Non-benchmark empirical practice includes reproducibility guidelines analogous to those for reinforcement learning treated in article one. Bandit algorithm performance is often sensitive to hyperparameter tuning, prior specification for Thompson sampling, and confidence-radius calibration for UCB variants, and reported results should include seed variance and hyperparameter sensitivity analyses.

## The Bridge to Reinforcement Learning

Bandits sit at the boundary of the reinforcement learning field. From above, the multi-armed bandit is the degenerate case of a Markov decision process with a single state and infinite horizon under any discount factor. From below, the contextual bandit is the degenerate case of an MDP whose contexts are one-shot states with no dynamics. Article three treats the general Markov decision process theory that reintroduces state dynamics and long-horizon credit assignment.

Two conceptual translations connect the theories. First, exploration bonuses in reinforcement learning generalize the UCB confidence radius from arms to state-action pairs. Second, posterior sampling for reinforcement learning generalizes Thompson sampling from arms to environments. These generalizations preserve the theoretical structure of the bandit analyses at the cost of substantially more complex proofs and looser bounds.

The bandit setting also provides the cleanest analytical laboratory for questions that recur in reinforcement learning. Exploration-exploitation trade-offs, regret decomposition, sample complexity, and adaptivity to problem structure all admit sharper answers in the bandit setting than in the full MDP setting. The subsequent articles exploit these connections where they yield insight into the harder problems.

Sample complexity in bandits versus regret is a subtle distinction. Regret bounds count cumulative reward foregone during learning, while sample complexity counts environment interactions to achieve a stated performance level. The two are related through the fundamental information-theoretic content of the problem but differ in what they measure. Article three treats sample-complexity results for tabular and function-approximation reinforcement learning.

## Load-Bearing Open Questions

- What is the optimal instance-dependent regret bound for structured bandits beyond the linear and kernel cases? The Lai-Robbins lower bound extends to structured settings, but tight instance-dependent upper bounds for general structured bandits remain incomplete.
- How closely do the frequentist and Bayesian regret analyses of Thompson sampling correspond for general reward families beyond the Bernoulli, Gaussian, and other conjugate cases?
- What is the tightest regret bound for adversarial contextual bandits with infinite policy classes? Instance-independent bounds via VC-dimension or Rademacher complexity apply, but instance-dependent adaptivity is less developed.
- How should non-stationarity be characterized when its structure is unknown to the learner? Change-point detection, sliding windows, and discounting each capture aspects of the problem, but a unified adaptive framework remains open.
- What is the correct sample-complexity theory for pure exploration in structured bandits, and how does it compare to the corresponding theory for cumulative-regret minimization?
- To what extent does the bandit exploration-exploitation trade-off translate to human decision-making under uncertainty? The empirical psychology of choice under uncertainty documents systematic departures from optimal bandit strategies that article fifteen surveys.

## References

### Books

- [Bubeck 2012][book_bubeck_2012]
- [Cesa-Bianchi and Lugosi 2006][book_cesa_bianchi_lugosi_2006]
- [Gittins Glazebrook Weber 2011][book_gittins_glazebrook_weber_2011]
- [Hazan 2016][book_hazan_2016]
- [Lattimore and Szepesvari 2020][book_lattimore_szepesvari_2020]
- [Slivkins 2019][book_slivkins_2019]

### Reference

- [Bandit Algorithms Book][ref_lattimore_book_site]
- [Berkeley CS294 Bandit Convex Optimization][ref_berkeley_cs294_bco]
- [Introduction to Online Learning Lecture Notes][ref_hazan_notes]
- [MSR Bandits Tutorial][ref_msr_bandits]
- [Vowpal Wabbit][ref_vowpal_wabbit]

### Related Posts

- [A250 Machines That Learn From Experience Framing][related_post_a250_framing]

### Research

- [Abbasi-Yadkori Pál and Szepesvári 2011][research_abbasi_yadkori_pal_szepesvari_2011]
- [Agrawal and Goyal 2012][research_agrawal_goyal_2012]
- [Agrawal and Goyal 2013][research_agrawal_goyal_2013]
- [Alon Cesa-Bianchi Gentile Mansour 2013][research_alon_et_al_2013]
- [Audibert and Bubeck 2009][research_audibert_bubeck_2009]
- [Audibert Munos Szepesvari 2009][research_audibert_munos_szepesvari_2009]
- [Auer Cesa-Bianchi and Fischer 2002][research_auer_cesa_bianchi_fischer_2002]
- [Auer Cesa-Bianchi Freund and Schapire 2002][research_auer_cesa_bianchi_freund_schapire_2002]
- [Behrens Woolrich Walton and Rushworth 2007][research_behrens_et_al_2007]
- [Bellman 1956][research_bellman_1956]
- [Beygelzimer Langford Li Reyzin Schapire 2011][research_beygelzimer_et_al_2011]
- [Bietti Agarwal and Langford 2021][research_bietti_agarwal_langford_2021]
- [Bubeck and Cesa-Bianchi 2012][research_bubeck_cesa_bianchi_2012]
- [Bubeck and Slivkins 2012][research_bubeck_slivkins_2012]
- [Bubeck Cesa-Bianchi and Kakade 2012][research_bubeck_cesa_bianchi_kakade_2012]
- [Bubeck Eldan and Lee 2017][research_bubeck_eldan_lee_2017]
- [Cappé et al 2013][research_cappe_et_al_2013]
- [Cesa-Bianchi and Lugosi 2012][research_cesa_bianchi_lugosi_2012]
- [Cesa-Bianchi et al 1997][research_cesa_bianchi_et_al_1997]
- [Chapelle and Li 2011][research_chapelle_li_2011]
- [Charnov 1976][research_charnov_1976]
- [Cohen McClure and Yu 2007][research_cohen_mcclure_yu_2007]
- [Daw et al 2006][research_daw_et_al_2006]
- [Even-Dar Mannor and Mansour 2006][research_even_dar_mannor_mansour_2006]
- [Flaxman Kalai and McMahan 2005][research_flaxman_kalai_mcmahan_2005]
- [Freund and Schapire 1997][research_freund_schapire_1997]
- [Garivier and Kaufmann 2016][research_garivier_kaufmann_2016]
- [Garivier and Moulines 2011][research_garivier_moulines_2011]
- [Gittins 1979][research_gittins_1979]
- [Herbster and Warmuth 1998][research_herbster_warmuth_1998]
- [Joulani Gyorgy and Szepesvari 2013][research_joulani_gyorgy_szepesvari_2013]
- [Kalai and Vempala 2005][research_kalai_vempala_2005]
- [Kaufmann Korda and Munos 2012][research_kaufmann_korda_munos_2012]
- [Kleinberg Slivkins and Upfal 2008][research_kleinberg_slivkins_upfal_2008]
- [Lai and Robbins 1985][research_lai_robbins_1985]
- [Langford and Zhang 2007][research_langford_zhang_2007]
- [Li et al 2010][research_li_et_al_2010]
- [Littlestone and Warmuth 1994][research_littlestone_warmuth_1994]
- [Lykouris Mirrokni Leme 2018][research_lykouris_mirrokni_leme_2018]
- [Robbins 1952][research_robbins_1952]
- [Robbins and Monro 1951][research_robbins_monro_1951]
- [Russo and Van Roy 2014][research_russo_van_roy_2014]
- [Srinivas et al 2010][research_srinivas_et_al_2010]
- [Thompson 1933][research_thompson_1933]
- [Vovk 1990][research_vovk_1990]
- [Whittle 1988][research_whittle_1988]
- [Yue Broder Kleinberg and Joachims 2012][research_yue_et_al_2012]
- [Zimmert and Seldin 2019][research_zimmert_seldin_2019]
- [Zinkevich 2003][research_zinkevich_2003]

[book_bubeck_2012]: https://www.nowpublishers.com/article/Details/MAL-024
[book_cesa_bianchi_lugosi_2006]: https://www.cambridge.org/core/books/prediction-learning-and-games/A0552F0DA7B92B2AA4EDB4C6A56F5306
[book_gittins_glazebrook_weber_2011]: https://onlinelibrary.wiley.com/doi/book/10.1002/9780470980033
[book_hazan_2016]: https://sites.google.com/view/intro-oco/
[book_lattimore_szepesvari_2020]: https://tor-lattimore.com/downloads/book/book.pdf
[book_slivkins_2019]: https://www.nowpublishers.com/article/Details/MAL-068
[ref_berkeley_cs294_bco]: https://people.eecs.berkeley.edu/~jordan/bandits.html
[ref_hazan_notes]: https://sites.google.com/view/intro-oco/lecture-notes
[ref_lattimore_book_site]: https://tor-lattimore.com/downloads/book/book.pdf
[ref_msr_bandits]: https://www.microsoft.com/en-us/research/publication/introduction-multi-armed-bandits/
[ref_vowpal_wabbit]: https://vowpalwabbit.org/
[related_post_a250_framing]: {% post_url 2025-12-18-machines_that_learn_from_experience_framing %}
[research_abbasi_yadkori_pal_szepesvari_2011]: https://papers.nips.cc/paper/2011/hash/e1d5be1c7f2f456670de3d53c7b54f4a-Abstract.html
[research_agrawal_goyal_2012]: https://proceedings.mlr.press/v23/agrawal12.html
[research_agrawal_goyal_2013]: https://proceedings.mlr.press/v28/agrawal13.html
[research_alon_et_al_2013]: https://papers.nips.cc/paper/2013/hash/f2201f5191c4e92cc5af043eebfd0946-Abstract.html
[research_audibert_bubeck_2009]: https://proceedings.mlr.press/v5/audibert09a.html
[research_audibert_munos_szepesvari_2009]: https://www.sciencedirect.com/science/article/pii/S030439750900027X
[research_auer_cesa_bianchi_fischer_2002]: https://link.springer.com/article/10.1023/A:1013689704352
[research_auer_cesa_bianchi_freund_schapire_2002]: https://epubs.siam.org/doi/10.1137/S0097539701398375
[research_behrens_et_al_2007]: https://www.nature.com/articles/nn1954
[research_bellman_1956]: https://www.jstor.org/stable/25049379
[research_beygelzimer_et_al_2011]: https://proceedings.mlr.press/v15/beygelzimer11a.html
[research_bietti_agarwal_langford_2021]: https://www.jmlr.org/papers/v22/18-863.html
[research_bubeck_cesa_bianchi_2012]: https://www.nowpublishers.com/article/Details/MAL-024
[research_bubeck_cesa_bianchi_kakade_2012]: https://proceedings.mlr.press/v23/bubeck12b.html
[research_bubeck_eldan_lee_2017]: https://arxiv.org/abs/1507.06580
[research_bubeck_slivkins_2012]: https://proceedings.mlr.press/v23/bubeck12a.html
[research_cappe_et_al_2013]: https://projecteuclid.org/journals/annals-of-statistics/volume-41/issue-3/Kullback-Leibler-upper-confidence-bounds-for-optimal-sequential-allocation/10.1214/13-AOS1119.full
[research_cesa_bianchi_et_al_1997]: https://dl.acm.org/doi/10.1145/258128.258179
[research_cesa_bianchi_lugosi_2012]: https://www.sciencedirect.com/science/article/pii/S0022000012000876
[research_chapelle_li_2011]: https://papers.nips.cc/paper/2011/hash/e53a0a2978c28872a4505bdb51db06dc-Abstract.html
[research_charnov_1976]: https://www.sciencedirect.com/science/article/pii/0040580976900409
[research_cohen_mcclure_yu_2007]: https://royalsocietypublishing.org/doi/10.1098/rstb.2007.2098
[research_daw_et_al_2006]: https://www.nature.com/articles/nature04766
[research_even_dar_mannor_mansour_2006]: https://www.jmlr.org/papers/v7/evendar06a.html
[research_flaxman_kalai_mcmahan_2005]: https://dl.acm.org/doi/10.5555/1070432.1070486
[research_freund_schapire_1997]: https://www.sciencedirect.com/science/article/pii/S002200009791504X
[research_garivier_kaufmann_2016]: https://proceedings.mlr.press/v49/garivier16a.html
[research_garivier_moulines_2011]: https://link.springer.com/chapter/10.1007/978-3-642-24412-4_16
[research_gittins_1979]: https://www.jstor.org/stable/2985029
[research_herbster_warmuth_1998]: https://link.springer.com/article/10.1023/A:1007424614876
[research_joulani_gyorgy_szepesvari_2013]: https://proceedings.mlr.press/v28/joulani13.html
[research_kalai_vempala_2005]: https://www.sciencedirect.com/science/article/pii/S0022000004001394
[research_kaufmann_korda_munos_2012]: https://link.springer.com/chapter/10.1007/978-3-642-34106-9_18
[research_kleinberg_slivkins_upfal_2008]: https://dl.acm.org/doi/10.1145/1374376.1374475
[research_lai_robbins_1985]: https://www.sciencedirect.com/science/article/pii/0196885885900028
[research_langford_zhang_2007]: https://papers.nips.cc/paper/2007/hash/4b04a686b0ad13dce35fa99fa4161c65-Abstract.html
[research_li_et_al_2010]: https://dl.acm.org/doi/10.1145/1772690.1772758
[research_littlestone_warmuth_1994]: https://www.sciencedirect.com/science/article/pii/S0890540184710091
[research_lykouris_mirrokni_leme_2018]: https://dl.acm.org/doi/10.1145/3188745.3188918
[research_robbins_1952]: https://www.jstor.org/stable/2321000
[research_robbins_monro_1951]: https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-22/issue-3/A-Stochastic-Approximation-Method/10.1214/aoms/1177729586.full
[research_russo_van_roy_2014]: https://proceedings.mlr.press/v28/russo14.html
[research_srinivas_et_al_2010]: https://arxiv.org/abs/0912.3995
[research_thompson_1933]: https://www.jstor.org/stable/2332286
[research_vovk_1990]: https://dl.acm.org/doi/10.5555/92571.92672
[research_whittle_1988]: https://www.cambridge.org/core/journals/journal-of-applied-probability/article/abs/restless-bandits-activity-allocation-in-a-changing-world/1893AA495D3ADC46A08017E4E38C89E0
[research_yue_et_al_2012]: https://www.sciencedirect.com/science/article/pii/S0022000012000281
[research_zimmert_seldin_2019]: https://proceedings.mlr.press/v89/zimmert19a.html
[research_zinkevich_2003]: https://www.cs.cmu.edu/~maz/publications/techconvex.pdf
