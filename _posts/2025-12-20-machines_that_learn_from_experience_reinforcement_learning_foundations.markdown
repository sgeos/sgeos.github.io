---
layout: post
mathjax: true
comments: true
title:  "Machines That Learn From Experience: Reinforcement Learning Foundations"
date:   2025-12-20 00:00:00 +0000
categories: artificial-intelligence machine-learning neuroscience
series: machines_that_learn_from_experience
series_title: Machines That Learn From Experience
series_index: 3
---

<!-- A252 -->
<script>console.log("A252");</script>

Reinforcement learning is the study of computational agents that learn to select actions in a stochastic environment so as to maximize a long-term cumulative reward. The Markov decision process provides the standard formal object, dynamic programming provides the exact planning apparatus when the transition and reward model are known, and the family of sample-based methods including Monte Carlo, temporal-difference learning, Q-learning, SARSA, policy gradients, and actor-critic provide the algorithmic apparatus when the model is unknown. This article treats the classical foundations of reinforcement learning systematically, following the layout of the [Sutton and Barto 2018][book_sutton_barto_2018] canonical reference and the mathematical treatment of [Puterman 1994][book_puterman_1994], [Bertsekas and Tsitsiklis 1996][book_bertsekas_tsitsiklis_1996], and [Bertsekas 2019][book_bertsekas_2019]. Article one of this series introduced the agent-environment loop and previewed the machinery, article two treated the pre-Markov bandit and online-learning special case, this article provides the systematic treatment of the Markov decision process theory that reinforcement learning proper builds on. Article four treats the deep-learning-based extension.

## The Markov Decision Process

A Markov decision process is a tuple

$$\mathcal{M} = (\mathcal{S}, \mathcal{A}, P, R, \gamma, \mu_0)$$

where $\mathcal{S}$ is a state space, $\mathcal{A}$ is an action space (possibly state-dependent), $P : \mathcal{S} \times \mathcal{A} \to \Delta(\mathcal{S})$ is a transition kernel with

$$P(s' \mid s, a) = \Pr(s_{t+1} = s' \mid s_t = s, a_t = a)$$

$R : \mathcal{S} \times \mathcal{A} \times \mathcal{S} \to \Delta(\mathbb{R})$ is a reward distribution, $\gamma \in [0, 1)$ is a discount factor, and $\mu_0 \in \Delta(\mathcal{S})$ is an initial state distribution. The Markov property requires

$$P(s_{t+1} \mid s_t, a_t, s_{t-1}, a_{t-1}, \ldots, s_0, a_0) = P(s_{t+1} \mid s_t, a_t)$$

so the transition depends only on the most recent state and action.

A policy $\pi : \mathcal{S} \to \Delta(\mathcal{A})$ specifies action selection. Deterministic policies are the special case where $\pi(a \mid s)$ concentrates on a single action for each state. The policy and MDP together induce a distribution over trajectories

$$p_{\pi}(\tau) = \mu_0(s_0) \prod_{t=0}^{\infty} \pi(a_t \mid s_t) P(s_{t+1} \mid s_t, a_t)$$

The discounted return from time $t$ is

$$G_t = \sum_{k=0}^{\infty} \gamma^k r_{t+k+1}$$

with $r_{t+1}$ the reward received after action $a_t$ from state $s_t$. The agent's objective is to maximize the expected return under the initial state distribution,

$$J(\pi) = \mathbb{E}_{\pi} \left[ G_0 \right] = \mathbb{E}_{s \sim \mu_0}[V^{\pi}(s)]$$

where $V^{\pi}(s)$ is the state value function defined below.

Finite MDPs have $|\mathcal{S}|, |\mathcal{A}| < \infty$. Countable and uncountable state and action spaces are treated in the extensions section. Episodic tasks introduce a terminal absorbing state and may use $\gamma = 1$. Continuing tasks have $\gamma < 1$ or use the average-reward formulation treated later.

An MDP is called unichain if under every stationary policy the induced Markov chain has a single recurrent class plus a possibly-empty set of transient states, and multichain otherwise. The distinction matters for the average-reward setting where multichain MDPs require a more careful treatment.

## Historical Development

The MDP formalism traces to [Bellman 1957][book_bellman_1957] work on dynamic programming and to [Howard 1960][book_howard_1960] explicit treatment of Markov decision processes with policies. The mathematics of optimal control theory in parallel developed similar objects for continuous-state continuous-action systems.

The transition from planning under a known model to learning from experience without a model came in stages. [Samuel 1959][research_samuel_1959] checkers program used what would be called temporal-difference learning long before that concept was named. [Michie and Chambers 1968][research_michie_chambers_1968] BOXES system learned pole-balancing control by trial and error. [Klopf 1972][research_klopf_1972] hedonistic-neuron hypothesis connected the reinforcement idea to single-neuron computation.

[Sutton 1988][research_sutton_1988] gave the first systematic treatment of temporal-difference learning as a machine-learning algorithm and proved its convergence for the tabular case, using ideas from stochastic approximation traced to [Robbins and Monro 1951][research_robbins_monro_1951]. The earlier [Sutton 1984][book_sutton_1984_thesis] doctoral thesis introduced the credit-assignment framework that the 1988 paper crystallized. [Watkins 1989][research_watkins_1989] and [Watkins and Dayan 1992][research_watkins_dayan_1992] introduced Q-learning as an off-policy control algorithm and proved its convergence in the tabular case. [Jaakkola Jordan and Singh 1994][research_jaakkola_jordan_singh_1994] provided a unified convergence analysis for tabular TD and Q-learning under the stochastic approximation framework, and [Tsitsiklis 1994][research_tsitsiklis_1994] extended the analysis to asynchronous Q-learning. [Barto Sutton and Anderson 1983][research_barto_sutton_anderson_1983] actor-critic architecture provided the algorithmic template for policy-based methods.

The policy gradient theorem was proved in its modern form by [Sutton McAllester Singh and Mansour 2000][research_sutton_mcallester_singh_mansour_2000], synthesizing earlier work by [Williams 1992][research_williams_1992] REINFORCE, [Baxter and Bartlett 2001][research_baxter_bartlett_2001] GPOMDP, and others. The synthesis established policy-based methods as a coherent family with a shared analytical apparatus.

The 1990s and 2000s produced the systematic mathematical foundations. [Bertsekas and Tsitsiklis 1996][book_bertsekas_tsitsiklis_1996] provided the neuro-dynamic programming perspective on approximate value-based methods. [Puterman 1994][book_puterman_1994] provided the definitive treatment of finite MDPs. [Szepesvari 2010][book_szepesvari_2010] and [Sutton and Barto 2018][book_sutton_barto_2018] became the modern reference textbooks. The deep-learning wave of the 2010s treated in article four extends but does not supersede this classical foundation.

## Value Functions, Policies, and Bellman Equations

The state value function under a policy $\pi$ is the expected return from state $s$ under $\pi$,

$$V^{\pi}(s) = \mathbb{E}_{\pi} \left[ G_t \mid s_t = s \right]$$

The action value function or Q function under $\pi$ is the expected return from state $s$ taking action $a$ and thereafter following $\pi$,

$$Q^{\pi}(s, a) = \mathbb{E}_{\pi} \left[ G_t \mid s_t = s, a_t = a \right]$$

The two are related by

$$V^{\pi}(s) = \sum_a \pi(a \mid s) Q^{\pi}(s, a), \quad Q^{\pi}(s, a) = \mathbb{E}\!\left[r + \gamma V^{\pi}(s') \mid s, a\right]$$

The advantage function

$$A^{\pi}(s, a) = Q^{\pi}(s, a) - V^{\pi}(s)$$

captures the improvement of action $a$ over the policy-average action at state $s$ and is central to policy-gradient variance reduction.

The Bellman expectation equation for the state value function is

$$V^{\pi}(s) = \sum_a \pi(a \mid s) \sum_{s', r} P(s', r \mid s, a) \left[ r + \gamma V^{\pi}(s') \right]$$

This is a linear system in $V^{\pi}$ over $|\mathcal{S}|$ unknowns and has a unique solution when $\gamma < 1$. In matrix form for finite MDPs, letting $\mathbf{V}^{\pi} \in \mathbb{R}^{|\mathcal{S}|}$ be the value vector, $\mathbf{R}^{\pi}$ the expected immediate reward vector under $\pi$, and $\mathbf{P}^{\pi}$ the $|\mathcal{S}| \times |\mathcal{S}|$ policy-induced transition matrix, the equation is

$$\mathbf{V}^{\pi} = \mathbf{R}^{\pi} + \gamma \mathbf{P}^{\pi} \mathbf{V}^{\pi}$$

which has the closed-form solution

$$\mathbf{V}^{\pi} = (\mathbf{I} - \gamma \mathbf{P}^{\pi})^{-1} \mathbf{R}^{\pi}$$

for $\gamma < 1$ where the inverse exists because $\gamma \mathbf{P}^{\pi}$ has spectral radius at most $\gamma$. The corresponding equation for $Q^{\pi}$ is

$$Q^{\pi}(s, a) = \sum_{s', r} P(s', r \mid s, a) \left[ r + \gamma \sum_{a'} \pi(a' \mid s') Q^{\pi}(s', a') \right]$$

The Bellman optimality equations characterize the optimal value functions $V^*$ and $Q^*$,

$$V^*(s) = \max_a \sum_{s', r} P(s', r \mid s, a) \left[ r + \gamma V^*(s') \right]$$

$$Q^*(s, a) = \sum_{s', r} P(s', r \mid s, a) \left[ r + \gamma \max_{a'} Q^*(s', a') \right]$$

An optimal policy $\pi^*$ is any policy achieving $V^{\pi^*} = V^*$ at every state, equivalently any policy that at each state selects an action in $\arg\max_a Q^*(s, a)$. Existence of optimal deterministic policies is guaranteed for finite MDPs under standard conditions.

## Optimality, Contraction, and Fixed Points

The Bellman expectation and optimality operators acting on value functions provide the theoretical foundation for the classical algorithms. Define the Bellman expectation operator under $\pi$,

$$(T^{\pi} V)(s) = \sum_a \pi(a \mid s) \sum_{s', r} P(s', r \mid s, a) \left[ r + \gamma V(s') \right]$$

and the Bellman optimality operator,

$$(T^* V)(s) = \max_a \sum_{s', r} P(s', r \mid s, a) \left[ r + \gamma V(s') \right]$$

Both operators are $\gamma$-contractions on $\mathbb{R}^{|\mathcal{S}|}$ under the supremum norm,

$$\| T^{\pi} V - T^{\pi} V' \|_{\infty} \leq \gamma \| V - V' \|_{\infty}, \quad \| T^* V - T^* V' \|_{\infty} \leq \gamma \| V - V' \|_{\infty}$$

By the Banach fixed-point theorem, each operator has a unique fixed point that value iteration converges to at a geometric rate governed by $\gamma$. The fixed point of $T^{\pi}$ is $V^{\pi}$ and the fixed point of $T^*$ is $V^*$. The corresponding contraction property for the $Q$-value operators is analogous.

The greedy policy with respect to a value function $V$ is the deterministic policy

$$\pi_V(s) = \arg\max_a \sum_{s', r} P(s', r \mid s, a) \left[ r + \gamma V(s') \right]$$

The policy improvement theorem states that if $\pi$ and $\pi'$ are two policies such that $Q^{\pi}(s, \pi'(s)) \geq V^{\pi}(s)$ for all $s$, then $V^{\pi'}(s) \geq V^{\pi}(s)$ for all $s$. In particular, the policy greedy with respect to $V^{\pi}$ is at least as good as $\pi$, providing the foundation for policy iteration.

## Dynamic Programming Methods

When the MDP model $(P, R)$ is known, dynamic programming provides exact algorithms for computing $V^{\pi}$ and $V^*$.

Value iteration applies the Bellman optimality operator directly,

$$V_{k+1}(s) = (T^* V_k)(s)$$

converging to $V^*$ from any initial $V_0$ at a rate

$$\| V_k - V^* \|_{\infty} \leq \gamma^k \| V_0 - V^* \|_{\infty}$$

by the contraction property. Value iteration produces an $\epsilon$-optimal value function in $\mathcal{O}(\log(1/\epsilon)/(1-\gamma))$ iterations.

Policy iteration alternates policy evaluation, which solves the linear system $V^{\pi_k} = T^{\pi_k} V^{\pi_k}$ exactly for the current policy, and policy improvement, which sets

$$\pi_{k+1}(s) = \arg\max_a \sum_{s', r} P(s', r \mid s, a) \left[ r + \gamma V^{\pi_k}(s') \right]$$

Policy iteration converges to $\pi^*$ in a finite number of iterations for finite MDPs, since each iteration strictly improves the policy or terminates. In practice policy iteration converges in a small number of iterations independent of state-space size for well-posed problems.

Modified policy iteration interpolates between value and policy iteration by performing a limited number of Bellman expectation operator applications before each policy improvement step, trading exactness of policy evaluation for reduced per-iteration cost. Asynchronous dynamic programming permits the Bellman operator to be applied to states in arbitrary order and possibly with stale value estimates, provided every state is visited infinitely often. Gauss-Seidel value iteration uses the most recent updated values within each sweep, typically converging faster in practice than the synchronous Jacobi-style update.

Linear programming provides an alternative exact solution method for finite MDPs. The optimal value function is the unique feasible solution of

$$\min_{V} \sum_s \mu_0(s) V(s) \quad \text{subject to} \quad V(s) \geq \sum_{s', r} P(s', r \mid s, a) [r + \gamma V(s')] \; \forall s, a$$

The dual formulation solves for occupation measures directly and connects to convex-optimization approaches to reinforcement learning treated in subsequent articles.

## Monte Carlo Methods

Monte Carlo methods estimate value functions from sample episodes rather than from a known model. For episodic tasks, the first-visit Monte Carlo estimator of $V^{\pi}(s)$ averages returns following the first visit to state $s$ in each episode,

$$\hat{V}^{\pi}_{\text{FV}}(s) = \frac{1}{|\text{Ep}(s)|} \sum_{i \in \text{Ep}(s)} G^{(i)}_{t^{(i)}_s}$$

where $\text{Ep}(s)$ is the set of episodes containing state $s$ and $t^{(i)}_s$ is the time of first visit. The every-visit variant

$$\hat{V}^{\pi}_{\text{EV}}(s) = \frac{1}{N(s)} \sum_{i} \sum_{t : s_t^{(i)} = s} G^{(i)}_{t}$$

averages over all visits with $N(s)$ the total visit count and shares the same limit but with different finite-sample bias and variance. The first-visit estimator is unbiased for i.i.d. episodes, the every-visit estimator introduces bias from within-episode correlation between successive visits but often has lower variance.

Monte Carlo prediction converges to $V^{\pi}$ almost surely under mild conditions on the episode distribution and policy. Monte Carlo control alternates policy evaluation via Monte Carlo estimation with policy improvement via greedy or $\epsilon$-greedy action selection, subject to the exploration issue that greedy improvement over Monte Carlo estimates can leave some state-action pairs unvisited.

The standard resolutions are the assumption of exploring starts, in which each episode begins from a state-action pair drawn uniformly, or the use of $\epsilon$-soft policies that assign at least $\epsilon/|\mathcal{A}|$ probability to every action, ensuring infinite visitation of all state-action pairs.

Off-policy Monte Carlo control learns about a target policy $\pi$ from data generated under a behavior policy $\mu$ via importance sampling. The per-episode importance sampling ratio for an episode of length $T$ is

$$\rho_{0:T} = \prod_{t=0}^{T} \frac{\pi(a_t \mid s_t)}{\mu(a_t \mid s_t)}$$

and the ordinary importance-sampling estimator of $V^{\pi}(s)$ is

$$\hat{V}^{\pi}_{\text{OIS}}(s) = \frac{\sum_i \rho^{(i)} G^{(i)}}{|\text{Ep}(s)|}$$

which is unbiased but often has infinite or unbounded variance. The weighted importance-sampling estimator

$$\hat{V}^{\pi}_{\text{WIS}}(s) = \frac{\sum_i \rho^{(i)} G^{(i)}}{\sum_i \rho^{(i)}}$$

is biased but often has substantially lower variance and is consistent under standard conditions. Per-decision importance sampling reduces variance further by using per-transition ratios only over the relevant portion of the trajectory,

$$\hat{V}^{\pi}_{\text{PD}}(s_t) = \mathbb{E}_\mu\!\left[\sum_{k=t}^{T} \gamma^{k-t} \rho_{t:k-1} r_{k+1}\right]$$

with $\rho_{t:k-1} = \prod_{j=t}^{k-1} \pi(a_j \mid s_j) / \mu(a_j \mid s_j)$.

## Temporal-Difference Learning

Temporal-difference learning combines the sample-based character of Monte Carlo methods with the bootstrapping character of dynamic programming. The one-step TD update, called TD(0), applies the update

$$V(s_t) \leftarrow V(s_t) + \alpha \left[ r_{t+1} + \gamma V(s_{t+1}) - V(s_t) \right]$$

after each transition. The TD error

$$\delta_t = r_{t+1} + \gamma V(s_{t+1}) - V(s_t)$$

is the fundamental quantity driving both prediction and control algorithms in the value-based family.

TD(0) is guaranteed to converge to $V^{\pi}$ under linear function approximation and mild step-size conditions, with the tabular case as a special case of this result. The Robbins-Monro conditions require

$$\sum_{t=0}^{\infty} \alpha_t = \infty, \quad \sum_{t=0}^{\infty} \alpha_t^2 < \infty$$

for step-size sequences $\alpha_t$ that decay appropriately.

TD versus Monte Carlo trades off bias and variance. Monte Carlo estimates are unbiased but high variance, TD estimates are biased by the current $V$ but low variance. In practice TD converges faster on many problems, and the analysis of which regime is preferable for which class of problems is an active research area.

The $n$-step TD return

$$G_t^{(n)} = r_{t+1} + \gamma r_{t+2} + \cdots + \gamma^{n-1} r_{t+n} + \gamma^n V(s_{t+n})$$

interpolates between one-step TD ($n=1$) and Monte Carlo ($n$ equal to episode length). The $n$-step update replaces $V(s_{t+1})$ in TD(0) with $G_t^{(n)}$.

## Q-Learning and SARSA

Q-learning is the canonical off-policy TD control algorithm. The one-step Q-learning update after transition $(s_t, a_t, r_{t+1}, s_{t+1})$ is

$$Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha \left[ r_{t+1} + \gamma \max_{a'} Q(s_{t+1}, a') - Q(s_t, a_t) \right]$$

The target uses the maximum $Q$ over next actions rather than the action actually selected, making the update off-policy. Q-learning learns about the greedy policy regardless of which policy generated the data. [Watkins and Dayan 1992][research_watkins_dayan_1992] proved that Q-learning converges to $Q^*$ almost surely under standard conditions on the step-size and the visitation of state-action pairs.

SARSA is the on-policy analogue, using the actually-selected next action in the target,

$$Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha \left[ r_{t+1} + \gamma Q(s_{t+1}, a_{t+1}) - Q(s_t, a_t) \right]$$

named for the tuple $(s_t, a_t, r_{t+1}, s_{t+1}, a_{t+1})$ appearing in the update. SARSA was introduced by [Rummery and Niranjan 1994][research_rummery_niranjan_1994] and converges to the $Q$ function of the greedy-in-the-limit policy under standard exploration conditions.

Expected SARSA replaces the sample $Q(s_{t+1}, a_{t+1})$ with its expectation under the current policy,

$$Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha \left[ r_{t+1} + \gamma \sum_{a'} \pi(a' \mid s_{t+1}) Q(s_{t+1}, a') - Q(s_t, a_t) \right]$$

reducing variance at the cost of slightly greater computation per update.

Double Q-learning [van Hasselt 2010][research_van_hasselt_2010] addresses the overestimation bias in Q-learning by maintaining two independent estimators $Q_A$ and $Q_B$ and using each to select the maximizing action for the target of the other. On each update, with probability one-half the update is

$$Q_A(s_t, a_t) \leftarrow Q_A(s_t, a_t) + \alpha \left[r_{t+1} + \gamma Q_B(s_{t+1}, \arg\max_{a'} Q_A(s_{t+1}, a')) - Q_A(s_t, a_t)\right]$$

and with probability one-half the roles of $Q_A$ and $Q_B$ are swapped. The mechanism removes the systematic upward bias in max-based estimators over noisy samples,

$$\mathbb{E}[\max_a Q(s, a)] \geq \max_a \mathbb{E}[Q(s, a)]$$

with equality only when the estimates are exact.

Q-learning and SARSA both extend to $n$-step and eligibility-trace variants. The relationship between on-policy and off-policy variants illuminates the deeper divide between the two families of control algorithms.

## Exploration Strategies in Markov Decision Processes

Value-based and policy-gradient methods both require an exploration strategy to ensure that all state-action pairs are visited sufficiently often. Article five treats intrinsic motivation and structured exploration at length, the classical exploration strategies for tabular and linear-function-approximation settings are surveyed here.

The $\epsilon$-greedy strategy selects a uniform random action with probability $\epsilon$ and the greedy action otherwise,

$$\pi(a \mid s) = \begin{cases} 1 - \epsilon + \epsilon / |\mathcal{A}| & \text{if } a = \arg\max_{a'} Q(s, a') \\ \epsilon / |\mathcal{A}| & \text{otherwise} \end{cases}$$

Under decaying schedules $\epsilon_t \to 0$ with $\sum \epsilon_t = \infty$, $\epsilon$-greedy Q-learning converges to $Q^*$ in the tabular case and provides a widely-used baseline for control experiments.

Boltzmann exploration, also called softmax exploration, weights actions by the exponential of their $Q$-values with temperature parameter $\tau$,

$$\pi(a \mid s) = \frac{\exp(Q(s, a) / \tau)}{\sum_{a'} \exp(Q(s, a') / \tau)}$$

The temperature $\tau$ interpolates between uniform ($\tau \to \infty$) and greedy ($\tau \to 0$) exploration. Softmax provides smoother action selection than $\epsilon$-greedy and is preferred when $Q$-value differences carry meaningful information beyond just the ordering.

Optimistic initialization sets $Q(s, a) = Q_{\max}$ for all state-action pairs at the start of training, inducing exploration through the natural tendency of TD updates to drive the value estimates downward toward the true values. The strategy is simple, requires no exploration parameter, and provides theoretical guarantees in the tabular finite-horizon setting.

Entropy regularization augments the policy gradient objective with a policy entropy term,

$$J_{\text{ent}}(\theta) = J(\theta) + \beta \mathbb{E}_{s \sim d^{\pi_\theta}}\!\left[H(\pi_\theta(\cdot \mid s))\right]$$

where $H(\pi(\cdot \mid s)) = -\sum_a \pi(a \mid s) \log \pi(a \mid s)$ is the Shannon entropy. The entropy bonus prevents premature convergence to deterministic suboptimal policies and provides a smoothed maximum-entropy formulation that underlies soft actor-critic and related maximum-entropy methods treated in article four.

Count-based exploration bonuses reward visitation of infrequently-observed state-action pairs, adding to the reward

$$r^{\text{expl}}(s, a) = \beta / \sqrt{N(s, a)}$$

for visit count $N(s, a)$. The bonus is the value-based analogue of the UCB confidence radius from article two and provides asymptotically optimal exploration under suitable conditions. Article five extends these ideas to structured environments where naive count-based exploration fails.

## Eligibility Traces and TD Lambda

Eligibility traces provide an efficient mechanism for propagating credit backward through time. The forward view of TD($\lambda$) defines the $\lambda$-return

$$G_t^{\lambda} = (1 - \lambda) \sum_{n=1}^{\infty} \lambda^{n-1} G_t^{(n)}$$

which is a geometrically-weighted average of the $n$-step returns for $\lambda \in [0, 1]$. For $\lambda = 0$ this recovers TD(0), for $\lambda = 1$ it recovers Monte Carlo.

The backward view maintains an eligibility trace $e_t(s)$ for each state,

$$e_t(s) = \gamma \lambda e_{t-1}(s) + \mathbb{1}\{s_t = s\}$$

and updates all state values in proportion to their eligibility on each TD error,

$$V(s) \leftarrow V(s) + \alpha \delta_t e_t(s) \quad \forall s$$

The forward and backward views are equivalent in expectation and produce identical updates over episodes. The backward view is computationally efficient because it operates online with $\mathcal{O}(|\mathcal{S}|)$ storage rather than requiring the full trajectory to be observed before updates begin.

Watkins's Q($\lambda$) and [Peng and Williams 1996][research_peng_williams_1996] Q($\lambda$) provide off-policy variants of TD($\lambda$) for the action-value case, differing in how they handle exploratory actions that break the eligibility trace. [Precup Sutton and Singh 2000][research_precup_sutton_singh_2000] developed the off-policy eligibility-trace framework using importance-sampling corrections, providing the theoretical basis for later off-policy multistep methods.

## Policy Gradient Methods

Policy gradient methods parameterize the policy directly as $\pi_\theta$ and optimize the expected return $J(\theta)$ by gradient ascent on $\theta$. The policy gradient theorem [Sutton McAllester Singh and Mansour 2000][research_sutton_mcallester_singh_mansour_2000] gives

$$\nabla_\theta J(\theta) = \mathbb{E}_{s \sim d^{\pi_\theta}, a \sim \pi_\theta}\!\left[ \nabla_\theta \log \pi_\theta(a \mid s) \, Q^{\pi_\theta}(s, a) \right]$$

where $d^{\pi_\theta}(s) = \sum_{t=0}^{\infty} \gamma^t p^{\pi_\theta}(s_t = s)$ is the discounted state distribution under $\pi_\theta$. The gradient does not require differentiation through the transition kernel, only through the policy, which permits treatment of unknown or non-differentiable environments.

The REINFORCE algorithm of [Williams 1992][research_williams_1992] implements policy gradient with a Monte Carlo return estimate,

$$\theta_{t+1} = \theta_t + \alpha \sum_{k=t}^{T} \nabla_\theta \log \pi_\theta(a_k \mid s_k) G_k$$

Variance reduction subtracts a state-dependent baseline $b(s_t)$ from the return,

$$\theta_{t+1} = \theta_t + \alpha \sum_{k=t}^{T} \nabla_\theta \log \pi_\theta(a_k \mid s_k) \left[G_k - b(s_k)\right]$$

which does not change the expectation. Using $b(s) = V^{\pi_\theta}(s)$ yields the advantage form

$$\nabla_\theta J(\theta) = \mathbb{E}_{\pi_\theta}\!\left[ \nabla_\theta \log \pi_\theta(a \mid s) A^{\pi_\theta}(s, a) \right]$$

The natural policy gradient of [Kakade 2001][research_kakade_2001] preconditions the gradient by the inverse Fisher information matrix

$$F(\theta) = \mathbb{E}_{s, a}\!\left[ \nabla_\theta \log \pi_\theta(a \mid s) \nabla_\theta \log \pi_\theta(a \mid s)^\top \right]$$

yielding the update $\theta \leftarrow \theta + \alpha F(\theta)^{-1} \nabla_\theta J(\theta)$. Natural gradient corrects for the parameterization-dependence of the plain gradient and provides invariance to policy reparameterization. [Peters and Schaal 2008][research_peters_schaal_2008] developed the natural-actor-critic algorithm for robotics applications, and [Bhatnagar Sutton Ghavamzadeh and Lee 2009][research_bhatnagar_et_al_2009] provided convergence-guaranteed natural actor-critic algorithms with function approximation. Trust-region and proximal policy optimization treated in article four build on the natural-gradient framework.

Simulation-based optimization of Markov reward processes by [Marbach and Tsitsiklis 2001][research_marbach_tsitsiklis_2001] provided a parallel formulation and convergence analysis for policy-gradient methods in the average-reward setting. [Kakade and Langford 2002][research_kakade_langford_2002] conservative policy iteration established monotone improvement guarantees for approximate policy iteration under update schemes, connecting policy-gradient theory to approximate dynamic programming.

## Actor-Critic Architectures

Actor-critic algorithms combine a parameterized policy (the actor) with a parameterized value function (the critic). The critic estimates $V^{\pi_\theta}$ or $Q^{\pi_\theta}$ by TD learning, and the actor uses the critic to reduce variance in policy gradient updates.

The advantage actor-critic update uses

$$\theta \leftarrow \theta + \alpha_\theta \nabla_\theta \log \pi_\theta(a_t \mid s_t) \left[r_{t+1} + \gamma V_w(s_{t+1}) - V_w(s_t)\right]$$

where the bracketed quantity is a one-step advantage estimate. The critic parameters $w$ are updated by TD(0) on the value function,

$$w \leftarrow w + \alpha_w \left[r_{t+1} + \gamma V_w(s_{t+1}) - V_w(s_t)\right] \nabla_w V_w(s_t)$$

The two updates operate on different timescales, with $\alpha_w \gg \alpha_\theta$ ensuring the critic tracks the current policy sufficiently well. [Konda and Tsitsiklis 2000][research_konda_tsitsiklis_2000] proved convergence for linear function-approximation actor-critic under standard timescale-separation and step-size conditions.

Deterministic policy gradient of [Silver Lever Heess Degris Wierstra Riedmiller 2014][research_silver_et_al_2014] treats continuous action spaces with a deterministic policy $\pi_\theta : \mathcal{S} \to \mathcal{A}$. The deterministic policy gradient theorem gives

$$\nabla_\theta J(\theta) = \mathbb{E}_{s \sim d^{\pi_\theta}}\!\left[ \nabla_\theta \pi_\theta(s) \nabla_a Q^{\pi_\theta}(s, a) \big|_{a = \pi_\theta(s)} \right]$$

avoiding the score-function trick required for stochastic policies. The deterministic policy gradient underlies the DDPG algorithm treated in article four.

Generalized advantage estimation of [Schulman Moritz Levine Jordan Abbeel 2016][research_schulman_moritz_levine_jordan_abbeel_2016] interpolates between one-step and Monte Carlo advantage estimates using a $\lambda$ parameter analogous to TD($\lambda$). The GAE advantage is

$$\hat{A}^{\text{GAE}(\gamma, \lambda)}_t = \sum_{l=0}^{\infty} (\gamma \lambda)^l \delta_{t+l}$$

where $\delta_t = r_{t+1} + \gamma V(s_{t+1}) - V(s_t)$ is the one-step TD residual. Setting $\lambda = 0$ recovers the one-step advantage and $\lambda = 1$ recovers Monte Carlo, with intermediate values trading bias for variance in the advantage estimate used in policy-gradient updates.

## Linear Function Approximation

Function approximation is required when the state space is large or continuous. Linear function approximation represents value as

$$V_w(s) = \phi(s)^\top w = \sum_i \phi_i(s) w_i$$

for feature vector $\phi(s) \in \mathbb{R}^d$ and weight vector $w \in \mathbb{R}^d$. The corresponding TD(0) update becomes

$$w \leftarrow w + \alpha \delta_t \phi(s_t)$$

where $\delta_t$ is the TD error computed with $V_w$. This is stochastic gradient descent on a modified least-squares objective, not on true mean-squared value error, and the resulting fixed point is the solution of a projected Bellman equation

$$w = \Pi_{\phi} T^{\pi} V_w$$

where $\Pi_\phi$ is the projection onto the space spanned by the features under the on-policy state distribution.

The linear TD fixed point exists and is unique for on-policy learning under standard conditions on the feature representation. [Tsitsiklis and Van Roy 1997][research_tsitsiklis_van_roy_1997] established convergence of TD(0) with linear function approximation for the on-policy prediction problem. [Gordon 1995][research_gordon_1995] treatment of stable function approximation and averagers provided an early foundational analysis. [Boyan and Moore 1995][research_boyan_moore_1995] highlighted the practical difficulty of generalization in value-based reinforcement learning, and [Sutton 1996][research_sutton_1996] sparse coarse coding approach demonstrated that carefully designed feature representations enable reliable learning on standard benchmarks. [Baird 1999][research_baird_1999] residual algorithms proposed an alternative update rule that combines TD and gradient descent on Bellman error to trade off convergence guarantees against solution quality.

Least-squares TD (LSTD) of [Bradtke and Barto 1996][research_bradtke_barto_1996] solves the projected Bellman equation directly,

$$w = A^{-1} b$$

where $A = \Phi^\top D_\pi (\Phi - \gamma P^{\pi} \Phi)$ and $b = \Phi^\top D_\pi R^{\pi}$, with $\Phi$ the feature matrix and $D_\pi$ the on-policy state-visitation diagonal matrix. LSTD converges in $\mathcal{O}(d^2)$ storage and $\mathcal{O}(d^3)$ computation per solve, making it efficient for moderate $d$.

Least-squares policy iteration [Lagoudakis and Parr 2003][research_lagoudakis_parr_2003] alternates LSTD-based policy evaluation with greedy policy improvement, providing a sample-efficient batch algorithm for control.

Nonlinear function approximation with neural networks is the subject of article four. The classical treatment developed here provides both the theoretical framework and the practical mechanisms that deep reinforcement learning generalizes.

## Batch Reinforcement Learning and Fitted Methods

Fitted methods approach reinforcement learning as a sequence of supervised learning problems, applying regression or classification learners to Bellman targets computed from a batch of experience. The framework separates the data-collection phase from the learning phase, permitting the use of any function-approximation method as a black-box regression subroutine.

Fitted value iteration of [Gordon 1995][research_gordon_1995] and [Munos and Szepesvari 2008][research_munos_szepesvari_2008] iteratively fits a value function to targets computed by applying the Bellman optimality operator to samples,

$$V_{k+1} = \arg\min_{V \in \mathcal{F}} \sum_{i=1}^n \left(V(s_i) - (T^* V_k)(s_i)\right)^2$$

for a function class $\mathcal{F}$. Fitted Q iteration of [Ernst Geurts and Wehenkel 2005][research_ernst_geurts_wehenkel_2005] extends the approach to the action-value case,

$$Q_{k+1} = \arg\min_{Q \in \mathcal{F}} \sum_{i=1}^n \left(Q(s_i, a_i) - (r_i + \gamma \max_{a'} Q_k(s_i', a'))\right)^2$$

using ensemble tree learners as the function class. Neural fitted Q iteration of [Riedmiller 2005][research_riedmiller_2005] used neural networks as the function class and provided a direct precursor to deep Q-networks. The fitted approach cleanly separates the two challenges of reinforcement learning (defining targets and fitting them) at the cost of substantially higher per-iteration computation than online TD updates.

Batch reinforcement learning treats the setting in which all data is collected up front and no further environment interaction is permitted. Distributional shift between the data-generating policy and the target policy is the fundamental obstacle, treated systematically in article eight on offline reinforcement learning. The [Lange Gabel Riedmiller 2012][research_lange_gabel_riedmiller_2012] framework provided an early systematic treatment of batch reinforcement learning as a distinct problem.

## The Deadly Triad and Divergence

Off-policy learning, function approximation, and bootstrapping together constitute the deadly triad identified by [Sutton and Barto 2018][book_sutton_barto_2018]. When all three are combined, TD-based value learning can diverge even under linear function approximation. [Baird 1995][research_baird_1995] counterexample provides the canonical demonstration through a small MDP with linear features and off-policy data on which linear TD(0) diverges to infinity.

The mathematical cause is that the projected Bellman operator $\Pi_\phi T^{\pi}$ is not necessarily a contraction under off-policy sampling, even though $T^{\pi}$ itself is a $\gamma$-contraction. [Tsitsiklis and Van Roy 1997][research_tsitsiklis_van_roy_1997] proved the formal characterization of when off-policy TD converges and when it diverges.

Gradient-TD methods of [Sutton Maei Precup Bhatnagar Silver Szepesvari Wiewiora 2009][research_sutton_maei_precup_2009] modify the TD update to descend on a true objective function that guarantees convergence in the off-policy linear setting. The mean-squared projected Bellman error

$$\text{MSPBE}(w) = \| \Pi_\phi (T^{\pi} V_w - V_w) \|_{D_\mu}^2$$

serves as the objective function, and the TDC update rule is

$$w \leftarrow w + \alpha \left[\delta_t \phi_t - \gamma \phi_{t+1} (\phi_t^\top h_t)\right], \quad h \leftarrow h + \beta \left[\delta_t - \phi_t^\top h_t\right] \phi_t$$

where $h$ is an auxiliary weight vector that estimates the linear part of the correction. GTD, TDC, and GTD2 provide alternative gradient corrections, differing in their asymptotic bias and finite-sample behavior.

Emphatic TD of [Sutton Mahmood White 2016][research_sutton_mahmood_white_2016] weights TD updates by an emphasis quantity

$$M_t = \lambda I_t + (1 - \lambda) F_t$$

where $I_t$ is an interest function and $F_t = \gamma \rho_{t-1} F_{t-1} + I_t$ is a followon trace. Deep reinforcement learning generally accepts the deadly triad and manages its instability through empirical mechanisms such as target networks and experience replay rather than through the classical gradient-TD analytical framework.

## Convergence Theory

The convergence theory of reinforcement learning algorithms rests on the general framework of stochastic approximation. The Robbins-Monro conditions on step sizes are necessary and sufficient for many algorithms under standard regularity, and the analysis proceeds by identifying the algorithm's expected update as a contraction and appealing to ODE-based analysis or martingale arguments.

The ODE method of [Kushner and Clark 1978][book_kushner_clark_1978] associates the stochastic iteration

$$w_{t+1} = w_t + \alpha_t h(w_t, \xi_{t+1})$$

with the deterministic differential equation

$$\dot{w}(t) = \bar{h}(w(t)) = \mathbb{E}[h(w, \xi)]$$

so that under standard conditions the iterates track the ODE trajectory. When the ODE has a globally asymptotically stable equilibrium $w^*$, the stochastic iterates converge to $w^*$ almost surely.

For the tabular case, convergence of TD(0), Q-learning, SARSA, and eligibility-trace variants is established under mild conditions on step sizes and infinite visitation of all state-action pairs. The convergence rates are typically $\mathcal{O}(1/\sqrt{t})$ in the stochastic setting and $\mathcal{O}(\gamma^k)$ in the exact deterministic setting.

For the on-policy linear function approximation case, TD(0), TD($\lambda$), and gradient-based policy methods converge under standard conditions. For the off-policy case, convergence generally requires gradient-TD or emphatic-TD corrections.

For nonlinear function approximation, convergence guarantees are substantially weaker. Even the on-policy case can exhibit non-convergence under nonlinear function approximation combined with bootstrapping. Empirical practice manages these hazards through architectural choices and training-procedure interventions treated in article four.

Finite-sample analyses under the Wasserstein-metric framework of [Munos et al 2016][research_munos_stepleton_harutyunyan_bellemare_2016] provide non-asymptotic bounds for various TD variants and connect to the modern theoretical understanding of function-approximation reinforcement learning.

## Sample Complexity and PAC-MDP

The sample complexity of reinforcement learning is the number of environment interactions required to obtain a near-optimal policy with high probability. The PAC-MDP framework of [Kakade 2003][book_kakade_thesis_2003] defines an algorithm to be probably approximately correct if its sample complexity, defined as the number of steps in which the policy is not $\epsilon$-optimal, is bounded with high probability by a polynomial in the problem parameters.

The E3 algorithm of [Kearns and Singh 2002][research_kearns_singh_2002] and the R-MAX algorithm of [Brafman and Tennenholtz 2002][research_brafman_tennenholtz_2002] achieve PAC-MDP guarantees for finite MDPs with sample complexity polynomial in $|\mathcal{S}|$, $|\mathcal{A}|$, and $1/(1-\gamma)$. The R-MAX sample complexity bound has the form

$$\tilde{\mathcal{O}}\!\left(\frac{|\mathcal{S}|^2 |\mathcal{A}|}{\epsilon^3 (1-\gamma)^6} \log(1/\delta)\right)$$

for producing an $\epsilon$-optimal policy with probability at least $1 - \delta$. Both algorithms use the principle of optimism in the face of uncertainty. Unknown states are treated as maximally rewarding, encouraging exploration to reduce their uncertainty.

Regret-based analysis of finite MDPs began with the UCRL2 algorithm of [Jaksch Ortner and Auer 2010][research_jaksch_ortner_auer_2010] and its successors, building on [Auer and Ortner 2007][research_auer_ortner_2007] earlier logarithmic regret bounds. UCRL2 maintains confidence sets over transition and reward parameters and follows optimistic policies with respect to those sets. The regret bound

$$R_T = \tilde{\mathcal{O}}(D \sqrt{|\mathcal{S}| |\mathcal{A}| T})$$

involves the diameter $D$ of the MDP, the state and action-space sizes, and the horizon $T$. The minimax lower bound of [Azar Osband and Munos 2017][research_azar_osband_munos_2017] establishes $\Omega(\sqrt{H |\mathcal{S}| |\mathcal{A}| T})$ for finite-horizon MDPs, and their UCBVI algorithm matches this bound. Posterior sampling for reinforcement learning of [Osband and Van Roy 2013][research_osband_van_roy_2013] extends Thompson sampling from bandits to MDPs and achieves Bayesian regret bounds of similar order under the Bayesian setting.

Model-based interval estimation with exploration bonuses of [Strehl Li and Littman 2009][research_strehl_li_littman_2009] provided a unified analysis of several PAC-MDP algorithms under a common framework. Sample complexity results for continuous-state MDPs and for MDPs with function approximation require substantial additional apparatus. Recent work has established polynomial sample complexity for finite-horizon linear MDPs and for MDPs with low-rank transition structure, connecting reinforcement learning theory to the low-rank matrix estimation literature.

Reward shaping can substantially reduce sample complexity when auxiliary reward information is available. Potential-based reward shaping of [Ng Harada and Russell 1999][research_ng_harada_russell_1999] modifies the reward function to

$$r'(s, a, s') = r(s, a, s') + \gamma \Phi(s') - \Phi(s)$$

for an arbitrary potential function $\Phi : \mathcal{S} \to \mathbb{R}$. The transformation preserves the optimal policy exactly while shaping the effective sparsity of the reward signal, addressing the well-known difficulty of learning under sparse rewards. The theoretical framework and its extensions have proved influential for practical applications where reward-signal engineering meaningfully reduces sample complexity. Hindsight experience replay of [Andrychowicz et al 2017][research_andrychowicz_et_al_2017] extends the reward-shaping idea by relabeling failed goal-reaching episodes with the actually-achieved outcomes, treating each trajectory as an off-policy demonstration for the corresponding hindsight goal.

## Off-Policy Learning

Off-policy learning enables value estimation and policy improvement from data generated under a policy different from the target policy. The importance-sampling ratio between target policy $\pi$ and behavior policy $\mu$ over a length-$T$ trajectory is

$$\rho_{0:T-1} = \prod_{t=0}^{T-1} \frac{\pi(a_t \mid s_t)}{\mu(a_t \mid s_t)}$$

Per-decision importance sampling improves variance by using ratios only over the relevant portion of the trajectory. Weighted importance sampling normalizes by the sum of ratios rather than the count.

The variance of importance sampling estimators grows exponentially with the trajectory length in the worst case,

$$\text{Var}[\rho_{0:T-1} G] = \mathcal{O}\!\left(\left(\frac{\pi_{\max}}{\mu_{\min}}\right)^{2T}\right)$$

which is the fundamental sample-complexity obstacle to off-policy learning at long horizons. Doubly robust estimators of [Jiang and Li 2016][research_jiang_li_2016] combine importance sampling with model-based value estimates to control variance,

$$\hat{V}^{\pi}_{\text{DR}}(s) = \hat{V}^{\pi}_{\text{model}}(s) + \mathbb{E}_\mu\!\left[\rho\!\left(G - \hat{V}^{\pi}_{\text{model}}(s)\right)\right]$$

where $\hat{V}^{\pi}_{\text{model}}$ is a model-based value estimate and the importance-sampling term serves as a correction that is unbiased whenever either the model or the importance-sampling estimate is correct.

Off-policy learning is central to sample-efficient reinforcement learning because it permits reuse of past experience and enables learning from human demonstrations, expert data, or exploratory data collected under different policies. Article eight treats offline reinforcement learning as its principal topic.

## Model-Based Reinforcement Learning Foundations

Model-based methods learn or maintain an internal model of the environment and use it for planning. When the environment model $(P, R)$ is known, dynamic programming solves the MDP exactly. When it is unknown, the natural strategy is to fit a model from samples and plan with the fitted model. Article seven treats model-based reinforcement learning at length, the foundational algorithms are surveyed here.

The most direct model-based approach is certainty equivalence. Fit the maximum-likelihood transition and reward parameters from data,

$$\hat{P}(s' \mid s, a) = \frac{N(s, a, s')}{N(s, a)}, \quad \hat{R}(s, a) = \frac{\sum_i r_i \mathbb{1}\{s_i = s, a_i = a\}}{N(s, a)}$$

and solve for $\hat{\pi}^*$ using value or policy iteration on $\hat{P}$ and $\hat{R}$. The strategy is optimal in the limit of infinite data and provides finite-sample guarantees under suitable conditions.

The Dyna architecture of [Sutton 1990][research_sutton_1990] interleaves real environment interaction with simulated interaction from the learned model. After each real transition $(s, a, r, s')$, the algorithm updates $Q$ from the real transition, updates the model $\hat{P}, \hat{R}$ from the transition, and performs $n$ simulated Q-updates by sampling states from the model. The mechanism reuses each real transition multiple times through the model and dramatically improves sample efficiency in tabular problems.

Prioritized sweeping of [Moore and Atkeson 1993][research_moore_atkeson_1993] extends Dyna by prioritizing simulated updates for states whose predecessors have recently seen large TD errors, focusing computation on the parts of the state space where the value estimate is changing most rapidly. Real-time dynamic programming of [Barto Bradtke and Singh 1995][research_barto_bradtke_singh_1995] combines asynchronous value iteration with actual environment traversal, updating only the values along visited trajectories.

Model-based methods offer sample-complexity advantages over model-free methods when the model is expressible in a compact form, at the cost of computational overhead for model fitting and planning. The trade-off between model-based and model-free approaches has been an enduring research topic that article seven treats systematically.

## Distributional Reinforcement Learning

Distributional reinforcement learning replaces the expected return $V^{\pi}$ with the return distribution $Z^{\pi}$,

$$Z^{\pi}(s, a) \stackrel{D}{=} R(s, a, s') + \gamma Z^{\pi}(s', a')$$

as a random variable rather than its scalar mean. The distributional Bellman operator applied to a return-distribution estimate produces a target distribution that the estimator regresses against.

The C51 algorithm of [Bellemare Dabney and Munos 2017][research_bellemare_dabney_munos_2017] represents the return distribution as a categorical distribution over a fixed set of atoms and minimizes the KL divergence between predicted and target distributions. Quantile regression DQN of [Dabney Rowland Bellemare Munos 2018][research_dabney_rowland_bellemare_munos_2018] represents the distribution by its quantiles and uses quantile regression loss, providing a more flexible representation. Implicit quantile networks extend the approach to arbitrary quantile levels.

Beyond the immediate algorithmic gains, distributional methods provide the natural setting for risk-sensitive reinforcement learning objectives such as CVaR discussed in article one. The distributional framework also connects to categorical distributional approaches in probabilistic modeling and to quantile-based statistical learning theory.

## Continuing Tasks and Average Reward

For continuing tasks in which episode boundaries are absent or artificial, the average-reward formulation replaces the discounted objective by

$$J_{\text{avg}}(\pi) = \lim_{T \to \infty} \frac{1}{T} \mathbb{E}_{\pi}\!\left[\sum_{t=0}^{T-1} r_{t+1}\right]$$

Under ergodicity of the induced Markov chain, this limit exists and equals $\sum_s d^{\pi}(s) \sum_a \pi(a \mid s) r(s, a)$ where $d^{\pi}$ is the stationary distribution.

The differential value function

$$\tilde{V}^{\pi}(s) = \mathbb{E}_{\pi}\!\left[\sum_{t=0}^{\infty} (r_{t+1} - J_{\text{avg}}(\pi)) \mid s_0 = s\right]$$

replaces the discounted value function, and the differential Bellman equation

$$\tilde{V}^{\pi}(s) = \sum_a \pi(a \mid s) \sum_{s', r} P(s', r \mid s, a) \left[r - J_{\text{avg}}(\pi) + \tilde{V}^{\pi}(s')\right]$$

provides the recursive structure. Differential Q-learning and differential SARSA extend the tabular algorithms.

Average-reward methods are theoretically preferable for continuing tasks where discounting is inappropriate but are practically less common because discounting provides a straightforward smoothing that improves finite-sample behavior. [Schwartz 1993][research_schwartz_1993] introduced R-learning as the average-reward analogue of Q-learning, and [Mahadevan 1996][research_mahadevan_1996] provided the first systematic survey of average-reward reinforcement learning. The [Puterman 1994][book_puterman_1994] textbook provides the definitive treatment of average-reward MDPs including multichain cases that require additional apparatus.

## Neuroscience and Psychology Connections

The reinforcement learning apparatus has striking parallels in neuroscience. [Schultz Dayan and Montague 1997][research_schultz_dayan_montague_1997] identified midbrain dopamine neurons as encoding a temporal-difference reward prediction error

$$\delta_t = r_{t+1} + \gamma V(s_{t+1}) - V(s_t)$$

with quantitative correspondence between dopamine spike responses and TD error predictions across a range of behavioral tasks. This finding launched the modern field of computational neuroscience of reward learning and provided the empirical foundation for treating temporal-difference learning as a candidate algorithmic account of animal learning. [O'Doherty Dayan Schultz Deichmann Friston and Frackowiak 2004][research_odoherty_et_al_2004] demonstrated the analogous TD-like signals in human ventral striatum using functional magnetic resonance imaging, and [Bayer and Glimcher 2005][research_bayer_glimcher_2005] provided quantitative single-neuron recordings in primates that established the fine-grained correspondence between dopamine firing and the TD prediction error. The [Niv 2009][research_niv_2009] review synthesized the reinforcement-learning-in-the-brain literature at the state of the art of the late 2000s.

The actor-critic architecture aligns with the anatomy of the basal ganglia. Striatal medium spiny neurons participate in circuits that separately implement policy (actor) and value (critic) functions, with dopamine as the training signal that updates both. Article fourteen treats the NeuroAI bridge in detail.

Model-free versus model-based control corresponds to the psychological distinction between habitual and goal-directed behavior [Daw Niv and Dayan 2005][research_daw_niv_dayan_2005]. Habits operate through cached values updated by temporal-difference-like learning, goal-directed behavior operates through a learned model and forward planning. Article fifteen treats the model-free versus model-based distinction and its correspondence to habitual versus goal-directed behavior in humans.

The Rescorla-Wagner model of classical conditioning corresponds exactly to a single-state TD learning rule, providing a formal bridge between animal learning theory and modern reinforcement learning that has been productive in both directions.

The successor representation of [Dayan 1993][research_dayan_1993] provides a distinctive value-function factorization that has since informed both machine learning and neuroscience. The successor representation is the matrix

$$M^{\pi}(s, s') = \mathbb{E}_{\pi}\!\left[\sum_{t=0}^{\infty} \gamma^t \mathbb{1}\{s_t = s'\} \mid s_0 = s\right]$$

giving the expected discounted future visitation of state $s'$ starting from state $s$ under policy $\pi$. The value function factors as $V^{\pi}(s) = \sum_{s'} M^{\pi}(s, s') R(s')$, decomposing value into the state-visitation structure and the reward structure. The factorization is efficient when reward changes but transitions do not, since only $R$ needs to be relearned. Neural evidence for successor-representation-like structure in the hippocampus [Stachenfeld Botvinick Gershman 2017][research_stachenfeld_botvinick_gershman_2017] has made the successor representation a load-bearing bridge concept between reinforcement learning and neuroscience.

## Empirical Landscape

The reinforcement learning empirical landscape rests on a set of canonical benchmark problems that provide standardized settings for algorithm development and comparison.

Grid-world tasks are the simplest environment class. The learner navigates a two-dimensional grid to a goal state, receiving reward at the goal and possibly a step cost elsewhere. Grid worlds provide clean settings for demonstrating value iteration, policy iteration, TD learning, and Q-learning. Variants include cliff walking, wind grid worlds, and stochastic grid worlds.

The Mountain Car problem of [Moore 1990][book_moore_1990] treats an under-powered car in a one-dimensional valley that must reach a hilltop by building momentum through backward-forward motion. The state space is two-dimensional (position and velocity) and continuous, making it a canonical setting for value-based methods with linear function approximation.

The Cart-Pole balancing problem of [Michie and Chambers 1968][research_michie_chambers_1968] and [Barto Sutton and Anderson 1983][research_barto_sutton_anderson_1983] treats a pole balanced on a cart, with actions to push the cart left or right and reward for maintaining balance. Cart-Pole provides the canonical setting for actor-critic and policy-gradient methods with linear function approximation.

The Acrobot problem treats a two-link pendulum with actuation at the middle joint, requiring energy accumulation to swing the tip to a target height. The problem features continuous states, discrete actions, and delayed sparse rewards.

The Tetris benchmark provides a large discrete state space (approximately $10^{60}$ board configurations) that has served as a challenge problem for value-based methods with hand-engineered features throughout the 1990s and 2000s.

Contemporary benchmarks including the Arcade Learning Environment of [Bellemare Naddaf Veness and Bowling 2013][research_bellemare_naddaf_veness_bowling_2013] and the MuJoCo physics simulator of [Todorov Erez and Tassa 2012][research_todorov_erez_tassa_2012] treated in article four extend the classical benchmark set to higher-dimensional pixel-based and continuous control settings, testing algorithmic scalability and generalization.

Reproducibility concerns in reinforcement learning have received increasing attention. [Henderson et al 2018][research_henderson_et_al_2018] documented that reinforcement learning results are frequently more variable across random seeds, hyperparameters, and implementation details than reported summary statistics suggest. Best-practice guidelines now include reporting seed variance, hyperparameter sensitivity, code and configuration availability, and evaluation across multiple task instances. Open-source implementations including CleanRL, Stable Baselines, and RLlib provide reference algorithm implementations with documented reproducibility characteristics that support empirical comparison.

## The Bridge to Deep Reinforcement Learning

The classical reinforcement learning apparatus described in this article provides the foundation on which deep reinforcement learning treated in article four builds. The transition from tabular and linear function approximation to nonlinear function approximation via neural networks introduces both new capabilities and new instabilities.

The core algorithmic templates persist. Deep Q-networks are Q-learning with neural function approximation. Trust-region policy optimization and proximal policy optimization are policy gradient methods with variance-reduced gradient estimates. Advantage actor-critic and soft actor-critic are actor-critic methods with neural function approximation. The convergence theory does not carry over automatically, but the algorithmic intuitions do.

Two developments enable the transition to deep neural function approximation. Experience replay of [Lin 1992][research_lin_1992] decouples the temporal correlation of successive updates, permitting stochastic-gradient-descent-based optimization to converge in practice. Target networks introduced by [Mnih et al 2015][research_mnih_et_al_2015] stabilize the bootstrapping target by holding a slower-updated copy of the value function. The target network update rule is either a hard periodic copy

$$\theta^{-} \leftarrow \theta \quad \text{every } C \text{ steps}$$

or a soft Polyak-averaged update

$$\theta^{-} \leftarrow \tau \theta + (1 - \tau) \theta^{-}$$

for small $\tau$. Both mechanisms accept the deadly triad and manage its instability rather than avoiding it.

Article four develops the deep reinforcement learning wave that these mechanisms enabled, treating deep Q-networks, deep policy gradients, and the AlphaGo and AlphaZero self-play systems in detail.

## Load-Bearing Open Questions

- What is the tight sample-complexity dependence on the discount factor $\gamma$ in the classical PAC-MDP setting? Current bounds involve factors of $(1-\gamma)^{-c}$ for various $c$, and the tightest $c$ remains under active analysis.
- Under what conditions on the MDP or on the function-approximation family do off-policy TD methods converge without gradient-TD corrections? Empirical practice frequently uses plain off-policy TD in the deadly-triad regime, and the theoretical characterization of when it works remains incomplete.
- What is the correct theoretical framing of the deep reinforcement learning success? Neural function approximation combined with off-policy learning and bootstrapping should be theoretically fragile, yet the empirical practice of deep RL produces working systems on many benchmarks. The gap between theory and practice remains substantial.
- How should sample complexity be characterized for continuous-state continuous-action MDPs beyond the linear and low-rank cases? Deep function approximation admits practical algorithms whose sample complexity is not tightly characterized by current theory.
- What is the correct treatment of long-horizon credit assignment under function approximation? Eligibility traces provide a partial answer, but the interaction between long horizons, function approximation, and bootstrapping remains a source of both theoretical and empirical difficulty.
- How closely does the actor-critic apparatus correspond to the anatomy and physiology of the mammalian basal ganglia, and what algorithmic variants are supported or refuted by the neural evidence? Article fourteen returns to this question.

## References

### Books

- [Bellman 1957][book_bellman_1957]
- [Bertsekas 2019][book_bertsekas_2019]
- [Bertsekas and Tsitsiklis 1996][book_bertsekas_tsitsiklis_1996]
- [Howard 1960][book_howard_1960]
- [Kakade 2003 Thesis][book_kakade_thesis_2003]
- [Kushner and Clark 1978][book_kushner_clark_1978]
- [Moore 1990][book_moore_1990]
- [Puterman 1994][book_puterman_1994]
- [Sutton 1984 Thesis][book_sutton_1984_thesis]
- [Sutton and Barto 2018][book_sutton_barto_2018]
- [Szepesvari 2010][book_szepesvari_2010]

### Reference

- [Berkeley CS285][ref_berkeley_cs285]
- [DeepMind x UCL RL Course][ref_deepmind_ucl_rl]
- [OpenAI Spinning Up][ref_openai_spinning_up]
- [Silver RL Course UCL][ref_silver_rl_course]
- [Stanford CS234][ref_stanford_cs234]
- [Sutton and Barto Second Edition PDF][ref_sutton_barto_pdf]

### Related Posts

- [A250 Machines That Learn From Experience Framing][related_post_a250_framing]
- [A251 Machines That Learn From Experience Bandits and Online Learning][related_post_a251_bandits]

### Research

- [Andrychowicz et al 2017][research_andrychowicz_et_al_2017]
- [Auer and Ortner 2007][research_auer_ortner_2007]
- [Azar Osband and Munos 2017][research_azar_osband_munos_2017]
- [Baird 1995][research_baird_1995]
- [Baird 1999][research_baird_1999]
- [Barto Bradtke and Singh 1995][research_barto_bradtke_singh_1995]
- [Barto Sutton Anderson 1983][research_barto_sutton_anderson_1983]
- [Baxter and Bartlett 2001][research_baxter_bartlett_2001]
- [Bayer and Glimcher 2005][research_bayer_glimcher_2005]
- [Bellemare Dabney and Munos 2017][research_bellemare_dabney_munos_2017]
- [Bellemare Naddaf Veness Bowling 2013][research_bellemare_naddaf_veness_bowling_2013]
- [Bhatnagar Sutton Ghavamzadeh Lee 2009][research_bhatnagar_et_al_2009]
- [Boyan and Moore 1995][research_boyan_moore_1995]
- [Bradtke and Barto 1996][research_bradtke_barto_1996]
- [Brafman and Tennenholtz 2002][research_brafman_tennenholtz_2002]
- [Dabney Rowland Bellemare Munos 2018][research_dabney_rowland_bellemare_munos_2018]
- [Daw Niv and Dayan 2005][research_daw_niv_dayan_2005]
- [Dayan 1993][research_dayan_1993]
- [Ernst Geurts and Wehenkel 2005][research_ernst_geurts_wehenkel_2005]
- [Gordon 1995][research_gordon_1995]
- [Henderson et al 2018][research_henderson_et_al_2018]
- [Jaakkola Jordan and Singh 1994][research_jaakkola_jordan_singh_1994]
- [Jaksch Ortner and Auer 2010][research_jaksch_ortner_auer_2010]
- [Jiang and Li 2016][research_jiang_li_2016]
- [Kakade 2001][research_kakade_2001]
- [Kakade and Langford 2002][research_kakade_langford_2002]
- [Kearns and Singh 2002][research_kearns_singh_2002]
- [Klopf 1972][research_klopf_1972]
- [Konda and Tsitsiklis 2000][research_konda_tsitsiklis_2000]
- [Lagoudakis and Parr 2003][research_lagoudakis_parr_2003]
- [Lange Gabel Riedmiller 2012][research_lange_gabel_riedmiller_2012]
- [Lin 1992][research_lin_1992]
- [Mahadevan 1996][research_mahadevan_1996]
- [Marbach and Tsitsiklis 2001][research_marbach_tsitsiklis_2001]
- [Michie and Chambers 1968][research_michie_chambers_1968]
- [Mnih et al 2015][research_mnih_et_al_2015]
- [Moore and Atkeson 1993][research_moore_atkeson_1993]
- [Munos and Szepesvari 2008][research_munos_szepesvari_2008]
- [Munos Stepleton Harutyunyan Bellemare 2016][research_munos_stepleton_harutyunyan_bellemare_2016]
- [Ng Harada and Russell 1999][research_ng_harada_russell_1999]
- [Niv 2009][research_niv_2009]
- [O'Doherty et al 2004][research_odoherty_et_al_2004]
- [Osband and Van Roy 2013][research_osband_van_roy_2013]
- [Peng and Williams 1996][research_peng_williams_1996]
- [Peters and Schaal 2008][research_peters_schaal_2008]
- [Precup Sutton and Singh 2000][research_precup_sutton_singh_2000]
- [Riedmiller 2005][research_riedmiller_2005]
- [Robbins and Monro 1951][research_robbins_monro_1951]
- [Rummery and Niranjan 1994][research_rummery_niranjan_1994]
- [Samuel 1959][research_samuel_1959]
- [Schulman Moritz Levine Jordan Abbeel 2016][research_schulman_moritz_levine_jordan_abbeel_2016]
- [Schultz Dayan Montague 1997][research_schultz_dayan_montague_1997]
- [Schwartz 1993][research_schwartz_1993]
- [Silver et al 2014][research_silver_et_al_2014]
- [Stachenfeld Botvinick Gershman 2017][research_stachenfeld_botvinick_gershman_2017]
- [Strehl Li and Littman 2009][research_strehl_li_littman_2009]
- [Sutton 1988][research_sutton_1988]
- [Sutton 1990][research_sutton_1990]
- [Sutton 1996][research_sutton_1996]
- [Sutton Maei Precup 2009][research_sutton_maei_precup_2009]
- [Sutton Mahmood White 2016][research_sutton_mahmood_white_2016]
- [Sutton McAllester Singh Mansour 2000][research_sutton_mcallester_singh_mansour_2000]
- [Todorov Erez and Tassa 2012][research_todorov_erez_tassa_2012]
- [Tsitsiklis 1994][research_tsitsiklis_1994]
- [Tsitsiklis and Van Roy 1997][research_tsitsiklis_van_roy_1997]
- [van Hasselt 2010][research_van_hasselt_2010]
- [Watkins 1989][research_watkins_1989]
- [Watkins and Dayan 1992][research_watkins_dayan_1992]
- [Williams 1992][research_williams_1992]

[book_bellman_1957]: https://press.princeton.edu/books/paperback/9780691146683/dynamic-programming
[book_bertsekas_2019]: http://www.athenasc.com/rlbook.html
[book_bertsekas_tsitsiklis_1996]: http://www.athenasc.com/ndpbook.html
[book_howard_1960]: https://mitpress.mit.edu/9780262080095/dynamic-programming-and-markov-processes/
[book_kakade_thesis_2003]: https://homes.cs.washington.edu/~sham/papers/thesis/sham_thesis.pdf
[book_kushner_clark_1978]: https://link.springer.com/book/10.1007/978-1-4684-9352-8
[book_moore_1990]: https://www.cs.cmu.edu/~awm/moorethesis.pdf
[book_puterman_1994]: https://onlinelibrary.wiley.com/doi/book/10.1002/9780470316887
[book_sutton_1984_thesis]: http://incompleteideas.net/papers/sutton-84.pdf
[book_sutton_barto_2018]: http://incompleteideas.net/book/the-book-2nd.html
[book_szepesvari_2010]: https://sites.ualberta.ca/~szepesva/rlbook.html
[ref_berkeley_cs285]: https://rail.eecs.berkeley.edu/deeprlcourse/
[ref_deepmind_ucl_rl]: https://www.deepmind.com/learning-resources/reinforcement-learning-lecture-series-2021
[ref_openai_spinning_up]: https://spinningup.openai.com/
[ref_silver_rl_course]: https://www.davidsilver.uk/teaching/
[ref_stanford_cs234]: https://web.stanford.edu/class/cs234/
[ref_sutton_barto_pdf]: http://incompleteideas.net/book/RLbook2020.pdf
[related_post_a250_framing]: {% post_url 2025-12-18-machines_that_learn_from_experience_framing %}
[related_post_a251_bandits]: {% post_url 2025-12-19-machines_that_learn_from_experience_bandits_and_online_learning %}
[research_andrychowicz_et_al_2017]: https://papers.nips.cc/paper/2017/hash/453fadbd8a1a3af50a9df4df899537b5-Abstract.html
[research_auer_ortner_2007]: https://papers.nips.cc/paper/2006/hash/c1b70d965ca504aa751ddb62ad69c63f-Abstract.html
[research_azar_osband_munos_2017]: https://proceedings.mlr.press/v70/azar17a.html
[research_baird_1995]: https://www.sciencedirect.com/science/article/pii/B9781558603776500452
[research_baird_1999]: https://www.leemon.com/papers/1999b.pdf
[research_barto_bradtke_singh_1995]: https://www.sciencedirect.com/science/article/pii/000437029400011O
[research_barto_sutton_anderson_1983]: https://ieeexplore.ieee.org/document/6313077
[research_baxter_bartlett_2001]: https://www.jair.org/index.php/jair/article/view/10269
[research_bayer_glimcher_2005]: https://www.cell.com/neuron/fulltext/S0896-6273(05)00365-4
[research_bellemare_dabney_munos_2017]: https://proceedings.mlr.press/v70/bellemare17a.html
[research_bellemare_naddaf_veness_bowling_2013]: https://www.jair.org/index.php/jair/article/view/10819
[research_bhatnagar_et_al_2009]: https://www.sciencedirect.com/science/article/pii/S0005109809002628
[research_boyan_moore_1995]: https://papers.nips.cc/paper/1994/hash/b6928e9c1cf1a5b8b0e0f1b9a3f6f8f4-Abstract.html
[research_bradtke_barto_1996]: https://link.springer.com/article/10.1007/BF00114723
[research_brafman_tennenholtz_2002]: https://www.jmlr.org/papers/v3/brafman02a.html
[research_dabney_rowland_bellemare_munos_2018]: https://ojs.aaai.org/index.php/AAAI/article/view/11791
[research_daw_niv_dayan_2005]: https://www.nature.com/articles/nn1560
[research_dayan_1993]: https://direct.mit.edu/neco/article/5/4/613/5679
[research_ernst_geurts_wehenkel_2005]: https://www.jmlr.org/papers/v6/ernst05a.html
[research_gordon_1995]: https://www.sciencedirect.com/science/article/pii/B9781558603776500268
[research_henderson_et_al_2018]: https://ojs.aaai.org/index.php/AAAI/article/view/11694
[research_jaakkola_jordan_singh_1994]: https://link.springer.com/article/10.1162/neco.1994.6.6.1185
[research_jaksch_ortner_auer_2010]: https://www.jmlr.org/papers/v11/jaksch10a.html
[research_jiang_li_2016]: https://proceedings.mlr.press/v48/jiang16.html
[research_kakade_2001]: https://papers.nips.cc/paper/2001/hash/4b86abe48d358ecf194c56c69108433e-Abstract.html
[research_kakade_langford_2002]: https://homes.cs.washington.edu/~sham/papers/rl/aoarl.pdf
[research_kearns_singh_2002]: https://link.springer.com/article/10.1023/A:1017984413808
[research_klopf_1972]: https://apps.dtic.mil/sti/citations/AD0742259
[research_konda_tsitsiklis_2000]: https://papers.nips.cc/paper/1999/hash/6449f44a102fde848669bdd9eb6b76fa-Abstract.html
[research_lagoudakis_parr_2003]: https://www.jmlr.org/papers/v4/lagoudakis03a.html
[research_lange_gabel_riedmiller_2012]: https://link.springer.com/chapter/10.1007/978-3-642-27645-3_2
[research_lin_1992]: https://link.springer.com/article/10.1007/BF00992699
[research_mahadevan_1996]: https://link.springer.com/article/10.1023/A:1018064306595
[research_marbach_tsitsiklis_2001]: https://ieeexplore.ieee.org/document/911375
[research_michie_chambers_1968]: https://scholar.google.com/scholar?q=Michie+Chambers+BOXES+1968
[research_mnih_et_al_2015]: https://www.nature.com/articles/nature14236
[research_moore_atkeson_1993]: https://link.springer.com/article/10.1007/BF00993104
[research_munos_stepleton_harutyunyan_bellemare_2016]: https://papers.nips.cc/paper/2016/hash/c3992e9a68c5ae12bd18488bc579b30d-Abstract.html
[research_munos_szepesvari_2008]: https://www.jmlr.org/papers/v9/munos08a.html
[research_ng_harada_russell_1999]: https://www.aaai.org/Papers/ICML/1999/ICML99-041.pdf
[research_niv_2009]: https://www.sciencedirect.com/science/article/pii/S0022249608001004
[research_odoherty_et_al_2004]: https://www.science.org/doi/10.1126/science.1094285
[research_osband_van_roy_2013]: https://papers.nips.cc/paper/2013/hash/6a5889bb0190d0211a991f47bb19a777-Abstract.html
[research_peng_williams_1996]: https://link.springer.com/article/10.1023/A:1018076709321
[research_peters_schaal_2008]: https://www.sciencedirect.com/science/article/pii/S0925231208000532
[research_precup_sutton_singh_2000]: https://proceedings.mlr.press/v98/precup00a.html
[research_riedmiller_2005]: https://link.springer.com/chapter/10.1007/11564096_32
[research_robbins_monro_1951]: https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-22/issue-3/A-Stochastic-Approximation-Method/10.1214/aoms/1177729586.full
[research_rummery_niranjan_1994]: https://www.cambridge.org/engineering/reports/on-line-q-learning-using-connectionist-systems
[research_samuel_1959]: https://ieeexplore.ieee.org/document/5392560
[research_schulman_moritz_levine_jordan_abbeel_2016]: https://arxiv.org/abs/1506.02438
[research_schultz_dayan_montague_1997]: https://www.science.org/doi/10.1126/science.275.5306.1593
[research_schwartz_1993]: https://www.sciencedirect.com/science/article/pii/B9781558603073500454
[research_silver_et_al_2014]: https://proceedings.mlr.press/v32/silver14.html
[research_stachenfeld_botvinick_gershman_2017]: https://www.nature.com/articles/nn.4650
[research_strehl_li_littman_2009]: https://www.jmlr.org/papers/v10/strehl09a.html
[research_sutton_1988]: https://link.springer.com/article/10.1007/BF00115009
[research_sutton_1990]: https://dl.acm.org/doi/10.5555/3091622.3091638
[research_sutton_1996]: https://papers.nips.cc/paper/1995/hash/f9a40a4780f5e1306c46f1c8daecee3b-Abstract.html
[research_sutton_maei_precup_2009]: https://icml.cc/Conferences/2009/papers/546.pdf
[research_sutton_mahmood_white_2016]: https://www.jmlr.org/papers/v17/14-488.html
[research_sutton_mcallester_singh_mansour_2000]: https://papers.nips.cc/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html
[research_todorov_erez_tassa_2012]: https://ieeexplore.ieee.org/document/6386109
[research_tsitsiklis_1994]: https://link.springer.com/article/10.1007/BF00993306
[research_tsitsiklis_van_roy_1997]: https://ieeexplore.ieee.org/document/580874
[research_van_hasselt_2010]: https://papers.nips.cc/paper/2010/hash/091d584fced301b442654dd8c23b3fc9-Abstract.html
[research_watkins_1989]: https://www.cs.rhul.ac.uk/~chrisw/new_thesis.pdf
[research_watkins_dayan_1992]: https://link.springer.com/article/10.1007/BF00992698
[research_williams_1992]: https://link.springer.com/article/10.1007/BF00992696
