---
layout: post
mathjax: true
comments: true
title:  "Machines That Learn From Experience: The Established Public Baseline and the Open Questions"
date:   2026-01-02 00:00:00 +0000
categories: artificial-intelligence machine-learning neuroscience
series: machines_that_learn_from_experience
series_title: Machines That Learn From Experience
series_index: 16
---

<!-- A265 -->
<script>console.log("A265");</script>

The sixteen-article series has surveyed the science and theory of adaptive, reinforcement, and experiential learning artificial intelligence together with the neuroscience and psychology of learning from which the field has borrowed extensively and to which it contributes reciprocally. This closing article synthesizes the series by separating the established public interdisciplinary knowledge from the genuinely open problems, at the closing of the editorial window in the mid 2020s. The established public baseline names the corpus of formal objects, algorithms, empirical findings, and bidirectional correspondences that a competent researcher in the field is expected to command, that appear in the canonical modern reference [Sutton and Barto 2018][book_sutton_barto_2018] and its companion monographs, and that can be reproduced from open publications and freely available code without proprietary datasets or undisclosed engineering. The open problems name the residual questions that remain contested at the closing of the editorial window, whose resolution would considerably reorganize the field. Coverage includes the definition of the public-baseline concept, the foundational formal objects now established, the established algorithmic toolkit consolidated by article, the established empirical findings consolidated by article, the six-axis analytical framework of article one applied retrospectively, the established neuroscience and psychology correspondences, the foundation-model turn and its integration with the classical experiential-learning framework, the position papers and canonical debates that organize the field, the open problems partitioned into theoretical foundations, algorithmic frontiers, empirical benchmarks, neuroscience correspondence, psychological correspondence, and alignment safety and governance, the empirical landscape at the closing of the editorial window, established and emerging applications, and the series closing. Article one introduced the six-axis framework and the sixteen-article roadmap. The present article closes the roadmap by delineating the settled public domain from the active research frontier.

## The Synthesis Problem

The synthesis problem for a sixteen-article survey of a rapidly-moving interdisciplinary field is not simply summarization. The field of adaptive, reinforcement, and experiential learning has produced across seven decades a considerable corpus of formal objects, algorithms, empirical findings, neuroscience correspondences, and psychological correspondences whose validity varies in the ways that this article aims to make explicit. Some findings are settled at the level of textbook consensus, reproducible from open publications and freely available code, and taught to every graduate student in the field. Other findings are contested, replicated only under narrow conditions, or dependent on undisclosed engineering that resists independent verification. The synthesis problem is to draw the line between the two categories as it stood at the closing of the editorial window in the mid 2020s.

The distinction admits several formalizations. Epistemically, the established public baseline names the corpus of claims whose credibility is high, whose provenance is auditable, and whose demonstration is reproducible. The open problems name the corpus of claims whose credibility is contested, whose provenance is uncertain, or whose demonstration is not reproducible under the conditions that permit independent verification. Institutionally, the established public baseline names the corpus of material that appears in canonical textbooks, tutorial reviews, and open-source implementations. The open problems name the material that appears in position papers, workshop discussions, and research announcements without yet meeting the reproducibility standards of the textbook literature.

The framework contrasts with several assumptions that organize modern machine learning discourse. The assumption that recent capability advances demonstrate progress on the underlying science is often violated when the advances depend on undisclosed engineering that resists independent verification. The assumption that the field's canonical benchmarks characterize the empirical progress is often violated when the benchmarks measure surrogate quantities that diverge from the underlying capabilities of interest. The correspondence between the field's institutional signals of progress and the actual epistemic progress continues to organize significant modern research and represents one of the residual open problems that this article surveys.

The account also acknowledges the temporal-decay problem that any synthesis of a moving field faces. The findings that are settled at the closing of the editorial window may be revised by subsequent research. The open problems may be resolved by research that appears shortly after the closing of the editorial window. The synthesis is therefore explicitly a snapshot, and the claims it makes are indexed to the temporal window of the mid 2020s. Subsequent revisions of the synthesis will need to update the settled-versus-open partition to reflect the research developments that occur in the intervening period.

The general form of the synthesis-problem update follows the same recursive learning form that has organized the series,

$$
B_{t+1} = B_t + \eta \, \Delta(B_t, E_t)
\tag{1}
$$

with $B_t$ the established public baseline at time $t$, $E_t$ the empirical developments in the intervening period, $\Delta$ the update function that permits new findings into the baseline as they meet the reproducibility criteria, and $\eta$ the rate at which the field's institutional processes update the baseline. The dynamics of $B$ across time provide the meta-level object of study for the history and sociology of the field.

## The Established Public Baseline as a Concept

The established public baseline is a empirical and institutional object whose properties this article aims to make explicit. The model rests on the distinction between three categories of scientific claim.

Established public claims are those whose formal statement, empirical support, and reproducibility permit independent verification through open publications and freely available code. The claims are indexed to citations, appear in canonical textbooks and tutorial reviews, and admit demonstration at the graduate-course level with modest computational resources. Examples include the convergence guarantees of Q-learning under tabular conditions, the temporal-difference correspondence to Rescorla-Wagner in classical conditioning, and the policy-gradient theorem in its modern form.

Established private claims are those whose formal statement is available in the open literature but whose empirical support depends on undisclosed engineering, proprietary datasets, or computational resources that resist independent replication. The claims are documented in published research announcements but the pathways from published description to independent reproduction are unavailable. Examples include the training procedures of large frontier language models, the reinforcement-learning-from-human-feedback pipelines of commercial dialogue systems, and the evaluation protocols of proprietary agent benchmarks.

Open claims are those whose formal statement is contested, whose empirical support is preliminary, or whose scope of validity is not yet characterized. The claims appear in position papers, workshop discussions, and research announcements without yet meeting the reproducibility standards of the textbook literature. Examples include the status of reward-is-enough as a strong versus weak thesis, the correspondence between transformer attention and biological attention, and the empirical scope of scaling laws under interactive learning.

The distinction has consequences for the field's epistemic infrastructure. The established public baseline supports substantial cumulative progress through the ability of researchers to build on prior work without re-establishing its foundations. The established private baseline supports marked capability progress but through pathways that resist the cumulative-progress dynamics of open science. The open claims represent the frontier at which new science is being made and where the settled-versus-open partition will eventually be redrawn.

The size of the established public baseline provides a rough measure of the field's cumulative epistemic progress. Article one introduced the formal objects that organize the field. The subsequent fourteen articles surveyed the algorithms, empirical findings, neuroscience correspondences, and psychological correspondences that constitute the baseline. The present article consolidates the corpus, indexes it to the citations, and identifies the residual open problems at the closing of the editorial window.

## Foundational Formal Objects Now Established

The foundational formal objects of experiential learning have been significantly established across seven decades of research and now organize the graduate curriculum in the field. This formulation provides the formal vocabulary that subsequent algorithmic and empirical developments have consumed and refined.

The Markov decision process of [Bellman 1957][book_bellman_1957] and [Howard 1960][book_howard_1960] provides the formal foundation. The tuple

$$
\mathcal{M} = (\mathcal{S}, \mathcal{A}, P, R, \gamma, \mu_0)
\tag{2}
$$

specifies the state space, action space, transition kernel, reward function, discount factor, and initial state distribution. The treatment organizes the mathematical treatment of experiential learning and continues to provide the canonical vocabulary for the field. The formal apparatus allows several standard extensions including the partially observable Markov decision process, the semi-Markov decision process, the constrained Markov decision process, and the multi-agent Markov game. Each extension has been substantially formalized and continues to organize modern research.

The agent's objective is formalized through the discounted return

$$
G_t = \sum_{k=0}^\infty \gamma^k r_{t+k+1}
\tag{3}
$$

with $\gamma \in [0, 1)$ trading off immediate against delayed reward. The policy $\pi(a \mid s)$ induces a distribution over trajectories $\tau = (s_0, a_0, r_1, s_1, a_1, \ldots)$ specified by

$$
p_\pi(\tau) = \mu_0(s_0) \prod_{t=0}^\infty \pi(a_t \mid s_t) \, P(s_{t+1} \mid s_t, a_t)
\tag{4}
$$

and the state-occupancy measure

$$
d^\pi(s) = (1 - \gamma) \sum_{t=0}^\infty \gamma^t \, \Pr_\pi(s_t = s)
\tag{5}
$$

which appears in the policy-gradient theorem and the offline-reinforcement-learning distributional-shift literature.

The value function and Bellman recursion of [Bellman 1957][book_bellman_1957] provide the dynamic-programming foundation. The state-value function

$$
V^\pi(s) = \mathbb{E}_\pi \left[ \sum_{t=0}^\infty \gamma^t r_{t+1} \mid s_0 = s \right]
\tag{6}
$$

and its Bellman recursion

$$
V^\pi(s) = \sum_a \pi(a \mid s) \sum_{s'} P(s' \mid s, a) \left[ R(s, a, s') + \gamma V^\pi(s') \right]
\tag{7}
$$

provide the fixed-point characterization that continues to organize the algorithmic treatment. The action-value function

$$
Q^\pi(s, a) = \mathbb{E}_\pi \left[ \sum_{t=0}^\infty \gamma^t r_{t+1} \mid s_0 = s, a_0 = a \right]
\tag{8}
$$

and the advantage function

$$
A^\pi(s, a) = Q^\pi(s, a) - V^\pi(s)
\tag{9}
$$

provide the action-conditioned refinements that organize the policy-improvement and variance-reduction literatures. The optimal Bellman equation

$$
V^*(s) = \max_a \sum_{s'} P(s' \mid s, a) \left[ R(s, a, s') + \gamma V^*(s') \right]
\tag{10}
$$

specifies the fixed-point characterization of the optimal value function. The corresponding optimal action-value function satisfies

$$
Q^*(s, a) = \sum_{s'} P(s' \mid s, a) \left[ R(s, a, s') + \gamma \max_{a'} Q^*(s', a') \right]
\tag{11}
$$

This account has been markedly extended through subsequent work but continues to provide the mathematical foundation for the field.

Under partial observability the belief-state update

$$
b_{t+1}(s') = \frac{O(o_{t+1} \mid s') \sum_s P(s' \mid s, a_t) \, b_t(s)}{\sum_{s''} O(o_{t+1} \mid s'') \sum_s P(s'' \mid s, a_t) \, b_t(s)}
\tag{12}
$$

provides the sufficient-statistic-of-history that permits the partially-observable Markov decision process to be recast as a fully-observable Markov decision process over belief states. The framework has been appreciably characterized and continues to provide the formal foundation for the partial-observability literature.

The temporal-difference error of [Sutton 1988][research_sutton_1988] provides the model-free foundation. The update

$$
\delta_t = r_{t+1} + \gamma V(s_{t+1}) - V(s_t)
\tag{13}
$$

specifies the prediction-error signal that drives the temporal-difference learning update

$$
V(s_t) \leftarrow V(s_t) + \alpha \delta_t
\tag{14}
$$

The account provides the model-free alternative to the model-based Bellman-recursion approach and continues to organize extensive modern research.

The Q-learning update of [Watkins 1989][research_watkins_1989] provides the control-side alternative. The update

$$
Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha \left[ r_{t+1} + \gamma \max_a Q(s_{t+1}, a) - Q(s_t, a_t) \right]
\tag{15}
$$

specifies the off-policy update that provides the convergence guarantees under tabular conditions. The model continues to organize sizable modern research and provides the foundation for deep Q-network approaches.

The policy gradient theorem of [Williams 1992][research_williams_1992] and [Sutton et al. 1999b][research_sutton_et_al_2000] provides the direct-policy-optimization foundation. The gradient

$$
\nabla_\theta J(\theta) = \mathbb{E}_{\pi_\theta} \left[ \sum_t \nabla_\theta \log \pi_\theta(a_t \mid s_t) \, Q^{\pi_\theta}(s_t, a_t) \right]
\tag{16}
$$

provides the unbiased gradient estimator that continues to organize the direct-policy-optimization literature. This formulation has been greatly refined through variance-reduction techniques including baselines, advantage estimators, and trust-region methods.

The Rescorla-Wagner model of [Rescorla and Wagner 1972][research_rescorla_wagner_1972] provides the psychological correspondence. The associative-strength update

$$
\Delta V_i = \alpha_i \beta \left( \lambda - \sum_j V_j \right)
\tag{17}
$$

specifies the prediction-error-driven learning rule that continues to organize the associative-learning literature. The formal correspondence to temporal-difference learning provides the bridge between psychology and machine learning that continues to organize appreciable modern research.

The regret decomposition of [Lai and Robbins 1985][research_lai_robbins_1985] provides the bandit-and-online-learning foundation. The regret bound

$$
R_T \geq \sum_{a: \Delta_a > 0} \frac{\log T}{D_{KL}(P_a \| P_{a^*})} \, \Delta_a + o(\log T)
\tag{18}
$$

specifies the fundamental lower bound on cumulative regret that continues to organize the bandit and online-learning literature. The treatment has been considerably extended through subsequent work and continues to provide the formal foundation for the field.

These foundational formal objects constitute the settled public domain of the field. Any competent researcher is expected to command the formalisms, and the algorithmic and empirical developments of the subsequent articles rest on these foundations.

## The Established Algorithmic Toolkit

The established algorithmic toolkit of experiential learning consolidates the corpus of algorithms whose formal statement, empirical support, and reproducibility permit independent verification. This account provides the canonical algorithms that appear in modern textbooks and open-source implementations.

Bandits and online learning of [A251 Bandits and Online Learning][related_post_a251_bandits] contribute the upper-confidence-bound algorithm of [Auer et al. 2002][research_auer_cesa_bianchi_fischer_2002] with its action-selection rule

$$
a_t = \arg\max_a \left[ \hat{\mu}_a + \sqrt{\frac{2 \log t}{N_a(t)}} \right]
\tag{19}
$$

and its regret bound of order $O(\sqrt{T \log T})$, Thompson sampling of [Thompson 1933][research_thompson_1933] with the posterior-sampling rule

$$
\theta_t \sim p(\theta \mid \mathcal{D}_{t-1}), \quad a_t = \arg\max_a \mathbb{E}[r \mid a, \theta_t]
\tag{20}
$$

and its Bayesian-optimal regret properties, the exponential-weights algorithm for the adversarial setting, and the extensions to contextual bandits including LinUCB and neural contextual bandits. The framework provides the pre-Markov-decision-process foundation for the field.

Reinforcement learning foundations of [A252 Reinforcement Learning Foundations][related_post_a252_rl_foundations] contribute the classical algorithms including value iteration and policy iteration of [Howard 1960][book_howard_1960], Monte Carlo methods, SARSA of [Rummery and Niranjan 1994][research_rummery_niranjan_1994], Q-learning of [Watkins 1989][research_watkins_1989], expected SARSA of [Van Seijen 2009][research_van_seijen_et_al_2009], and the eligibility-trace variants including TD($\lambda$) of [Sutton 1988][research_sutton_1988] and Watkins's Q($\lambda$) of [Watkins and Dayan 1992][research_watkins_dayan_1992]. The account provides the canonical algorithms whose convergence properties have been significantly characterized under tabular and linear function approximation conditions.

Deep reinforcement learning of [A253 Deep Reinforcement Learning][related_post_a253_deep_rl] contributes the canonical algorithms including deep Q-networks of [Mnih et al. 2015][research_mnih_et_al_2015] with the target-network loss

$$
\mathcal{L}(\theta) = \mathbb{E}_{(s, a, r, s') \sim \mathcal{D}} \left[ \left( r + \gamma \max_{a'} Q_{\theta^-}(s', a') - Q_\theta(s, a) \right)^2 \right]
\tag{21}
$$

the double DQN of [Van et al. 2016][research_van_hasselt_guez_silver_2016] and dueling DQN of [Wang et al 2016 Dueling][research_wang_et_al_2016_dueling] refinements, the policy-gradient methods including asynchronous advantage actor-critic of [Mnih et al. 2016][research_mnih_et_al_2016], trust region policy optimization of [Schulman et al. 2015][research_schulman_et_al_2015], and proximal policy optimization of [Schulman et al. 2017][research_schulman_et_al_2017] with the clipped surrogate objective

$$
\mathcal{L}^{\text{CLIP}}(\theta) = \mathbb{E}_t \left[ \min \left( \rho_t(\theta) \hat{A}_t, \, \text{clip}(\rho_t(\theta), 1 - \epsilon, 1 + \epsilon) \hat{A}_t \right) \right]
\tag{22}
$$

with $\rho_t(\theta) = \pi_\theta(a_t \mid s_t) / \pi_{\theta_{\text{old}}}(a_t \mid s_t)$, the deterministic-policy-gradient family including the [Silver et al. 2014][research_silver_et_al_2014] deterministic policy gradient theorem, DDPG of [Lillicrap et al. 2015][research_lillicrap_et_al_2015] and TD3 of [Fujimoto Hoof Meger 2018][research_fujimoto_hoof_meger_2018], the maximum-entropy family including soft actor-critic of [Haarnoja et al. 2018][research_haarnoja_et_al_2018] with the entropy-regularized objective

$$
J(\pi) = \sum_t \mathbb{E}_{(s_t, a_t) \sim \pi} \left[ r(s_t, a_t) + \alpha \mathcal{H}(\pi(\cdot \mid s_t)) \right]
\tag{23}
$$

the distributional reinforcement learning framework of [Bellemare et al. 2017][research_bellemare_dabney_munos_2017] that learns the distribution of the discounted return rather than only its expectation and induces the categorical DQN and quantile-regression DQN of [Dabney et al. 2018a][research_dabney_et_al_2018_qr_dqn] and the implicit quantile network of [Dabney et al. 2018b][research_dabney_et_al_2018_iqn], and the self-play framework including AlphaGo of [Silver et al. 2016][research_silver_et_al_2016], AlphaZero of [Silver et al. 2017][research_silver_et_al_2017] and its journal treatment in [Silver et al. 2018][research_silver_et_al_2018], and MuZero of [Schrittwieser et al. 2020][research_schrittwieser_et_al_2020] that extends the framework to unknown dynamics. The model provides the canonical algorithms that continue to organize modern deep reinforcement learning research.

Exploration, intrinsic motivation, and curiosity of [A254 Exploration Intrinsic Motivation and Curiosity][related_post_a254_exploration] contribute the count-based and pseudocount exploration frameworks including [Bellemare et al. 2016][research_bellemare_et_al_2016] with the exploration-bonus reward

$$
r^+_t = r_t + \frac{\beta}{\sqrt{\hat{N}(s_t)}}
\tag{24}
$$

the prediction-error curiosity of [Pathak et al. 2017][research_pathak_et_al_2017] with the intrinsic reward

$$
r^i_t = \eta \left\| \hat{\phi}(s_{t+1}) - \phi(s_{t+1}) \right\|_2^2
\tag{25}
$$

the empowerment framework of [Klyubin et al. 2005][research_klyubin_polani_nehaniv_2005] with the channel-capacity objective

$$
\mathfrak{E}(s) = \max_{\omega} I(A_t^n; S_{t+n} \mid s_t = s)
\tag{26}
$$

and the information-gain frameworks including the [Houthooft et al. 2016][research_houthooft_et_al_2016] variational-information-maximizing exploration framework. The treatment provides the canonical exploration methods that continue to organize modern research on hard-exploration problems.

Hierarchical reinforcement learning of [A255 Hierarchical Reinforcement Learning][related_post_a255_hierarchical] contributes the options framework of [Sutton et al. 1999a][research_sutton_precup_singh_1999] with the option tuple

$$
o = \langle \mathcal{I}_o, \pi_o, \beta_o \rangle
\tag{27}
$$

comprising an initiation set, an intra-option policy, and a termination condition, and inducing, for an option of random duration $k$, the semi-Markov decision process value function

$$
V^\mu(s) = \sum_o \mu(o \mid s) \, \mathbb{E}\!\left[ \sum_{j=1}^{k} \gamma^{j-1} r_{t+j} + \gamma^k V^\mu(s_{t+k}) \,\middle|\, s, o \right]
\tag{28}
$$

the MAXQ decomposition of [Dietterich 2000][research_dietterich_2000], the feudal networks framework of [Dayan and Hinton 1992][research_dayan_hinton_1993] and its modern extension in [Vezhnevets et al. 2017][research_vezhnevets_et_al_2017], and the option-critic hierarchical actor-critic method of [Bacon et al. 2017][research_bacon_harb_precup_2017]. This account provides the canonical hierarchical algorithms that continue to organize modern research on temporally-extended action.

World models and predictive model-based adaptation of [A256 World Models and Predictive Model-Based Adaptation][related_post_a256_world_models] contribute the model-based reinforcement learning algorithms including Dyna of [Sutton 1991][research_sutton_1991] with the interleaved update

$$
\hat{P}, \hat{R} \leftarrow \text{Learn}(\mathcal{D}); \quad Q \leftarrow Q + \alpha \left[ r + \gamma \max_{a'} Q(s', a') - Q(s, a) \right] \text{ on both real and simulated experience}
\tag{29}
$$

the PILCO framework of [Deisenroth and Rasmussen 2011][research_deisenroth_rasmussen_2011], the world-model architecture of [Ha and Schmidhuber 2018][research_ha_schmidhuber_2018] with a latent-dynamics model $z_{t+1} \sim p_\psi(z_{t+1} \mid z_t, a_t)$ trained jointly with an observation decoder $p_\phi(o_t \mid z_t)$, and the Dreamer family of algorithms of [Hafner et al. 2019][research_hafner_et_al_2020] and [Hafner et al. 2023][research_hafner_et_al_2023] that optimize policies through the differentiable rollout of learned latent dynamics. The framework provides the canonical model-based algorithms that continue to organize modern research on sample-efficient learning.

Offline and batch reinforcement learning of [A257 Offline and Batch Reinforcement Learning][related_post_a257_offline] contribute the canonical offline algorithms including batch-constrained Q-learning of [Fujimoto Meger Precup 2019][research_fujimoto_meger_precup_2019], conservative Q-learning of [Kumar et al. 2020][research_kumar_et_al_2020] with the pessimistic penalty

$$
\mathcal{L}_{\text{CQL}}(\theta) = \alpha \left[ \mathbb{E}_{s \sim \mathcal{D}} \log \sum_a \exp Q_\theta(s, a) - \mathbb{E}_{(s, a) \sim \mathcal{D}} Q_\theta(s, a) \right] + \mathcal{L}_{\text{TD}}(\theta)
\tag{30}
$$

behavior regularization methods with the policy-constraint objective

$$
\pi = \arg\max_\pi \mathbb{E}_{s \sim \mathcal{D}, a \sim \pi} [Q(s, a)] - \lambda \, D(\pi \| \pi_\beta)
\tag{31}
$$

and the implicit Q-learning approach of [Kostrikov et al. 2021][research_kostrikov_nair_levine_2022] that avoids querying out-of-distribution actions through expectile regression. The account provides the canonical offline algorithms that continue to organize modern research on learning from fixed datasets, and the [Levine et al. 2020][research_levine_et_al_2020] tutorial provides the canonical survey.

Meta-learning and online adaptation of [A258 Meta-Learning and Online Adaptation][related_post_a258_meta_learning] contribute the canonical meta-learning algorithms including model-agnostic meta-learning of [Finn Abbeel Levine 2017][research_finn_abbeel_levine_2017] with the bi-level objective

$$
\theta^* = \arg\min_\theta \sum_{\mathcal{T}_i \sim p(\mathcal{T})} \mathcal{L}_{\mathcal{T}_i} \left( \theta - \alpha \nabla_\theta \mathcal{L}_{\mathcal{T}_i}(\theta) \right)
\tag{32}
$$

the recurrent meta-reinforcement-learning approach of [Wang et al. 2016b][research_wang_et_al_2016] and [Duan et al. 2016][research_duan_et_al_2016] in which the inner-loop learning dynamics are absorbed into a recurrent network's hidden-state update, and the in-context learning frameworks introduced by [Brown 2020][research_brown_et_al_2020] in which foundation models perform the implicit adaptation through attention over the context window. The model provides the canonical meta-learning algorithms that continue to organize modern research on fast adaptation.

Continual and lifelong learning of [A259 Continual and Lifelong Learning][related_post_a259_continual] contribute the canonical continual-learning algorithms including elastic weight consolidation of [Kirkpatrick et al. 2017][research_kirkpatrick_et_al_2017] with the Fisher-information-weighted quadratic penalty

$$
\mathcal{L}(\theta) = \mathcal{L}_B(\theta) + \sum_i \frac{\lambda}{2} F_i (\theta_i - \theta^*_{A, i})^2
\tag{33}
$$

progressive networks of [Rusu et al. 2016][research_rusu_et_al_2016] that freeze prior-task parameters and add lateral adapters, the generative-replay framework of [Shin et al. 2017][research_shin_et_al_2017] that uses a learned generator $p_\psi(x, y)$ to rehearse prior tasks, the gradient episodic memory framework of [Lopez-Paz and Ranzato 2017][research_lopez_paz_ranzato_2017], and the averaged gradient episodic memory extension of [Chaudhry et al. 2018][research_chaudhry_et_al_2019]. This formulation provides the canonical continual-learning algorithms that continue to organize modern research on catastrophic forgetting.

Learning from demonstration, preference, and other agents of [A260 Learning From Demonstration Preference and Other Agents][related_post_a260_demonstration] contribute the canonical algorithms including behavior cloning with the maximum-likelihood objective

$$
\pi_{\text{BC}} = \arg\max_\pi \mathbb{E}_{(s, a) \sim \mathcal{D}_E} \log \pi(a \mid s)
\tag{34}
$$

generative adversarial imitation learning of [Ho and Ermon 2016][research_ho_ermon_2016] with the minimax objective

$$
\min_\pi \max_D \mathbb{E}_{\pi}[\log D(s, a)] + \mathbb{E}_{\pi_E}[\log(1 - D(s, a))] - \lambda \mathcal{H}(\pi)
\tag{35}
$$

maximum-entropy inverse reinforcement learning of [Ziebart 2008][research_ziebart_et_al_2008] with the trajectory-distribution model

$$
p(\tau) \propto \exp\left( \sum_t r_\phi(s_t, a_t) \right)
\tag{36}
$$

preference-based reinforcement learning of [Christiano et al. 2017][research_christiano_et_al_2017] with the Bradley-Terry preference model

$$
P(\tau^1 \succ \tau^2) = \frac{\exp \sum_t \hat{r}_\phi(s^1_t, a^1_t)}{\exp \sum_t \hat{r}_\phi(s^1_t, a^1_t) + \exp \sum_t \hat{r}_\phi(s^2_t, a^2_t)}
\tag{37}
$$

and the reinforcement-learning-from-human-feedback pipelines of [Ouyang et al. 2022][research_ouyang_et_al_2022] and [Stiennon et al. 2020][research_stiennon_et_al_2020] that operationalize preference-learning at scale for language model alignment. The treatment provides the canonical algorithms that continue to organize modern research on learning from non-reward signals, and the [Ng and Russell 2000][research_ng_russell_2000] and [Abbeel and Ng 2004][research_abbeel_ng_2004] foundational papers establish the inverse-reinforcement-learning framework.

Evolutionary and open-ended adaptation of [A261 Evolutionary and Open-Ended Adaptation][related_post_a261_evolutionary] contribute the canonical algorithms including evolutionary strategies of [Salimans et al. 2017][research_salimans_et_al_2017] with the natural-evolution-strategies gradient estimator

$$
\nabla_\theta \mathbb{E}_{\epsilon \sim \mathcal{N}(0, I)} \left[ F(\theta + \sigma \epsilon) \right] = \frac{1}{\sigma} \mathbb{E}_\epsilon \left[ F(\theta + \sigma \epsilon) \, \epsilon \right]
\tag{38}
$$

neuroevolution of augmenting topologies of [Stanley and Miikkulainen 2002][research_stanley_miikkulainen_2002], the quality-diversity frameworks including MAP-Elites of [Mouret and Clune 2015][research_mouret_clune_2015] that maintain an archive $\mathcal{A}$ over a behavior grid so that each cell $c$ retains

$$
\mathcal{A}[c] = \arg\max_{x \in \text{Cell}(c)} F(x)
\tag{39}
$$

the novelty-search framework of [Lehman and Stanley 2011][research_lehman_stanley_2011] that abandons the objective in favor of behavioral novelty, and the POET open-endedness framework of [Wang et al. 2019][research_wang_lehman_clune_stanley_2019] that co-evolves agents and environments. This account provides the canonical evolutionary algorithms that continue to organize modern research on population-based and open-ended learning.

Embodied cognition and developmental learning of [A262 Embodied Cognition and Developmental Learning][related_post_a262_embodied] contribute the canonical frameworks including sensorimotor contingency theory of [O'Regan and Noë 2001][research_oregan_noe_2001], morphological computation of [Pfeifer and Bongard 2007][book_pfeifer_bongard_2007], developmental robotics of [Weng et al. 2001][research_weng_et_al_2001], and the curriculum-and-scaffolding frameworks of [Bengio et al. 2009][research_bengio_et_al_2009]. The framework provides the canonical embodied-cognition frameworks that continue to organize modern research on physically-grounded learning.

The consolidated algorithmic toolkit constitutes the settled public domain of the field. Any competent researcher is expected to command the algorithms, and the applications and refinements of subsequent research consume these foundations.

## The Established Empirical Findings

The established empirical findings of experiential learning consolidate the corpus of empirical results whose replication has been substantially confirmed and whose scope of validity has been markedly characterized. The account provides the canonical empirical benchmarks against which subsequent research is evaluated.

The Atari 2600 benchmarks of [Bellemare et al. 2013][research_bellemare_et_al_2013] provide the canonical single-agent reinforcement-learning benchmark. The findings including the deep Q-network human-level performance on the fifty-seven-game suite of [Mnih et al. 2015][research_mnih_et_al_2015] have been appreciably replicated and continue to organize the benchmark evaluation of subsequent algorithms.

The MuJoCo continuous-control benchmarks of [Todorov et al. 2012][research_todorov_erez_tassa_2012] provide the canonical continuous-control benchmark. The findings including the proximal-policy-optimization performance and the soft-actor-critic performance have been greatly replicated and continue to organize the continuous-control literature.

The board game benchmarks of Go, chess, and shogi provide the canonical strategic-planning benchmarks. The findings including the AlphaGo and AlphaZero results have been considerably confirmed through subsequent research including the MuZero extension of [Schrittwieser et al. 2020][research_schrittwieser_et_al_2020] to unknown-dynamics settings, and continue to organize the game-playing literature.

The dopamine reward-prediction-error finding of [Schultz et al. 1997][research_schultz_dayan_montague_1997] provides the canonical neuroscience-machine-learning correspondence. The findings have been significantly replicated across species, tasks, and recording modalities, and continue to organize the neuroscience-of-reinforcement-learning literature.

The hippocampal replay finding of [Wilson and McNaughton 1994][research_wilson_mcnaughton_1994] and its extension in [Foster and Wilson 2006][research_foster_wilson_2006] provides the canonical memory-consolidation correspondence to experience replay in machine learning as introduced in [Lin 1992][research_lin_1992] and deployed at scale in [Mnih et al. 2015][research_mnih_et_al_2015]. The findings have been substantially replicated across species and tasks and continue to organize the hippocampal-machine-learning correspondence literature.

The complementary learning systems finding of [McClelland et al. 1995][research_mcclelland_mcnaughton_oreilly_1995] provides the canonical dual-memory-system correspondence. The findings have been markedly replicated and provide the bridge between the neuroscience of memory and the machine learning of continual learning.

The scaling laws of foundation models of [Kaplan et al. 2020][research_kaplan_et_al_2020] and [Hoffmann et al. 2022][research_hoffmann_et_al_2022] provide the empirical findings on the relationship between model size, compute, and performance. The Chinchilla-form parametric law

$$
L(N, D) = \frac{A}{N^\alpha} + \frac{B}{D^\beta} + E
\tag{40}
$$

specifies the relationship between the model parameter count $N$, the training-token count $D$, and the achieved loss $L$, with $E$ the irreducible loss and $\alpha, \beta$ the exponents fit to the empirical data. The compute-optimal frontier

$$
N^*(C) \propto C^a, \quad D^*(C) \propto C^b
\tag{41}
$$

specifies the allocation of a fixed compute budget $C$ across model size and data that minimizes the achieved loss. The findings have been appreciably replicated across model families and continue to organize the research on the scaling of foundation models. The applicability of scaling laws to interactive experiential learning remains greatly open and constitutes one of the open problems that this article surveys.

The Brain-Score benchmark of [Schrimpf et al. 2020][research_schrimpf_et_al_2020] provides the canonical benchmark for comparing artificial neural networks to biological brains. The findings including the ranking of candidate models by their brain-score correspondence continue to organize the NeuroAI benchmarking literature.

The replication crisis findings in psychology of [Open Science Collaboration 2015][research_osc_2015] provide the empirical foundation for the modern methodological reforms in psychology. The findings including the approximately thirty-six percent replication rate for strict significance criteria continue to organize the methodological-reform literature.

The consolidated empirical findings constitute the settled public domain of the field. The benchmarks organize the evaluation of subsequent algorithms, and the empirical findings provide the constraints against which theoretical claims are evaluated.

## The Six-Axis Framework Revisited

The six-axis analytical framework introduced in [A250 Framing][related_post_a250_framing] provides the dimensional structure through which the subsequent articles have been organized. The model names six axes (signal, objective, structure, model, interaction, and adaptation) along which any experiential learning problem supports characterization. The present section recapitulates each axis, records the position along the axis at which each article's subject sits, and identifies the empirical loci along each axis at which the settled-versus-open partition currently rests.

The signal axis characterizes the form of the training information the learner receives. The axis positions include dense scalar reward, sparse scalar reward, preference between trajectories, demonstration of desired behavior, and intrinsic motivation computed from the learner's own predictions. The series treats each position through the corresponding articles. Dense and sparse reward are the default of [A252 Reinforcement Learning Foundations][related_post_a252_rl_foundations] and [A253 Deep Reinforcement Learning][related_post_a253_deep_rl]. Preference is the subject of [A260 Learning From Demonstration Preference and Other Agents][related_post_a260_demonstration] alongside demonstration and inverse reinforcement learning. Intrinsic motivation is the subject of [A254 Exploration Intrinsic Motivation and Curiosity][related_post_a254_exploration]. The settled public baseline on this axis identifies the canonical algorithms per signal type. The residual open problem is the characterization of when hybrid signals provide practical benefits over pure single-signal training.

The objective axis characterizes the quantity the learner optimizes. The axis positions include expected discounted return, long-run average reward, risk-sensitive objectives including conditional value at risk

$$
\text{CVaR}_\alpha[G] = \mathbb{E}[G \mid G \leq q_\alpha(G)]
\tag{42}
$$

regret against a reference policy, distributional characteristics of return, and information-theoretic objectives including empowerment. The series treats each position through the corresponding articles. Discounted return is the default of [A252 Reinforcement Learning Foundations][related_post_a252_rl_foundations]. Regret is the subject of [A251 Bandits and Online Learning][related_post_a251_bandits]. Distributional characteristics are the subject of the distributional-reinforcement-learning framework of [Bellemare et al. 2017][research_bellemare_dabney_munos_2017] treated in [A253 Deep Reinforcement Learning][related_post_a253_deep_rl]. Information-theoretic objectives are the subject of [A254 Exploration Intrinsic Motivation and Curiosity][related_post_a254_exploration]. The settled public baseline identifies the canonical objectives and their algorithmic implementations. The residual open problem is the characterization of the correct objective under real-world safety and alignment constraints.

The structure axis characterizes the form of the environment the learner faces. The axis positions include the flat Markov decision process, the partially observable Markov decision process, the hierarchical decision process with options or sub-policies, the factored state space, the multi-agent stochastic game, and the partially observable stochastic game. The series treats each position through the corresponding articles. The flat Markov decision process is the default of [A252 Reinforcement Learning Foundations][related_post_a252_rl_foundations]. Hierarchical structure is the subject of [A255 Hierarchical Reinforcement Learning][related_post_a255_hierarchical]. Partial observability recurs throughout the series with treatment in the sensorimotor-contingency framework of [A262 Embodied Cognition and Developmental Learning][related_post_a262_embodied]. Multi-agent structure is the subject of the multi-agent extensions treated in [A260 Learning From Demonstration Preference and Other Agents][related_post_a260_demonstration]. The settled public baseline identifies the canonical formalisms per structure type. The residual open problem is the unified formal characterization of hierarchical decomposition under bounded computational resources.

The model axis characterizes the role of a learned environment model in the learning system. The axis positions include model-free (using only sample updates), model-based (learning an explicit generative model and planning with it), and model-implicit (using a learned representation that supports planning without an explicit generative model). The series treats each position through the corresponding articles. Model-free is the default of [A252 Reinforcement Learning Foundations][related_post_a252_rl_foundations] and [A253 Deep Reinforcement Learning][related_post_a253_deep_rl]. Model-based and model-implicit are the subject of [A256 World Models and Predictive Model-Based Adaptation][related_post_a256_world_models]. The correspondence between habitual model-free and goal-directed model-based behavior in animal learning is the subject of [A264 Psychology of Learning][related_post_a264_psychology] through the [Daw et al. 2005][research_daw_niv_dayan_2005] dual-system framework. The settled public baseline identifies the canonical algorithms per model type. The residual open problem is the optimal integration of model-free and model-based components under sample-complexity constraints.

The interaction axis characterizes the relationship between the learner's data source and the learner's policy. The axis positions include online interaction (collecting data from the environment as learning proceeds), offline learning (learning from a fixed prior dataset without further interaction), on-policy learning (using data collected under the current policy), and off-policy learning (using data collected under other policies). The series treats each position through the corresponding articles. Online on-policy is the default of many algorithms in [A252 Reinforcement Learning Foundations][related_post_a252_rl_foundations]. Off-policy learning is the subject of much of [A253 Deep Reinforcement Learning][related_post_a253_deep_rl] including the deep-Q-network family. Offline learning is the subject of [A257 Offline and Batch Reinforcement Learning][related_post_a257_offline]. The correspondence to human learning-from-demonstration is the subject of [A260 Learning From Demonstration Preference and Other Agents][related_post_a260_demonstration]. The settled public baseline identifies the canonical algorithms per interaction mode. The residual open problem is the characterization of when offline learning admits strong generalization guarantees beyond the coverage of the offline dataset.

The adaptation axis characterizes the temporal structure of the tasks the learner faces across its lifetime. The axis positions include stationary (a single fixed task), non-stationary (a task with drifting distribution), a task family requiring rapid adaptation for each new task, and an open-ended stream of tasks with no clear end. The series treats each position through the corresponding articles. Meta-learning across a task family is the subject of [A258 Meta-Learning and Online Adaptation][related_post_a258_meta_learning]. Continual and lifelong learning across a non-stationary stream is the subject of [A259 Continual and Lifelong Learning][related_post_a259_continual]. Open-ended adaptation is the subject of [A261 Evolutionary and Open-Ended Adaptation][related_post_a261_evolutionary]. Developmental adaptation across the lifespan is the subject of [A262 Embodied Cognition and Developmental Learning][related_post_a262_embodied]. The settled public baseline identifies the canonical algorithms per adaptation regime. The residual open problem is the formal characterization of open-endedness in the sense that human cultures and biological evolution exhibit.

The six-axis framework provides the analytical vocabulary through which any experiential learning problem permits characterization. This formulation's stability across the sixteen articles of the series provides evidence for its analytical power, and the correspondences between the axes and the algorithmic and empirical developments organize the research directions that this article surveys. The treatment also identifies the implicit dimensions along which the field has organized itself, and the residual open problems identified per axis constitute the research frontier at the closing of the editorial window.

## Established Neuroscience Correspondences

The established neuroscience correspondences consolidate the bidirectional exchanges between neuroscience and machine learning that have been considerably validated at the closing of the editorial window. This account was surveyed in detail in [A263 NeuroAI][related_post_a263_neuroai].

The dopamine reward-prediction-error correspondence of [Schultz et al. 1997][research_schultz_dayan_montague_1997] provides the paradigmatic correspondence. The finding that midbrain dopamine neurons encode a reward prediction error mathematically identical to the temporal-difference error

$$
\text{DA firing rate at } t \propto \delta_t = r_{t+1} + \gamma V(s_{t+1}) - V(s_t)
\tag{43}
$$

has been significantly replicated across species, tasks, and recording modalities, and continues to organize the neuroscience-of-reinforcement-learning literature.

The hippocampal-replay-experience-replay correspondence provides the memory-consolidation correspondence. The finding of [Wilson and McNaughton 1994][research_wilson_mcnaughton_1994] that hippocampal place cells replay recent experience during sharp-wave ripples, together with the reverse-replay finding of [Foster and Wilson 2006][research_foster_wilson_2006] and the hypothesis of a common mechanism in [Kumaran et al. 2016][research_kumaran_mcclelland_hassabis_2016], has been substantially replicated and provides the biological correspondence to the experience-replay mechanism that traces to [Lin 1992][research_lin_1992] and has been markedly deployed in modern deep reinforcement learning.

The complementary-learning-systems correspondence of [McClelland et al. 1995][research_mcclelland_mcnaughton_oreilly_1995] provides the dual-memory-system correspondence. The finding that fast hippocampal learning and slow cortical consolidation constitute complementary memory systems has been appreciably replicated and provides the biological correspondence to the interleaved-training-and-consolidation approaches in machine learning.

The predictive-coding correspondence of [Rao and Ballard 1999][research_rao_ballard_1999] provides the perceptual-inference correspondence. The finding that cortical hierarchies implement predictive coding through the top-down expectation and bottom-up prediction-error signaling allows the hierarchical formalization

$$
\epsilon_l = x_l - g_l(x_{l+1}), \quad x_l \leftarrow x_l + \eta \left( - \epsilon_l + \frac{\partial g_{l-1}(x_l)}{\partial x_l}^\top \epsilon_{l-1} \right)
\tag{44}
$$

with $x_l$ the representation at level $l$, $g_l$ the top-down generative model, and $\epsilon_l$ the residual prediction error. The framework has been greatly characterized and provides the biological correspondence to the modern generative-model and world-model literature.

The convolutional-network-visual-cortex correspondence provides the representational correspondence. The finding of [Yamins et al. 2014][research_yamins_et_al_2014] that convolutional networks trained on object recognition develop representations that match the hierarchical structure of the primate ventral visual stream, together with the representational-similarity analysis framework of [Kriegeskorte et al. 2008][research_kriegeskorte_mur_bandettini_2008], has been considerably characterized through the Brain-Score benchmarks of [Schrimpf et al. 2020][research_schrimpf_et_al_2020] and provides the representational correspondence between artificial and biological visual processing. The extension to the ventral-stream-and-object-recognition literature by [Khaligh-Razavi and Kriegeskorte 2014][research_khaligh_razavi_kriegeskorte_2014] provides the complementary characterization.

The grid-cell-successor-representation correspondence provides the spatial-and-planning correspondence. The successor representation of [Dayan 1993][research_dayan_1993]

$$
M^\pi(s, s') = \mathbb{E}_\pi \left[ \sum_{t=0}^\infty \gamma^t \, \mathbb{1}[s_t = s'] \mid s_0 = s \right]
\tag{45}
$$

factorizes the value function as

$$
V^\pi(s) = \sum_{s'} M^\pi(s, s') R(s')
\tag{46}
$$

and the eigenvector decomposition of $M^\pi$ produces spatial basis functions with the hexagonal-grid structure observed in entorhinal grid cells. The finding of [Stachenfeld et al. 2017][research_stachenfeld_botvinick_gershman_2017] that entorhinal grid cells implement this eigenvector decomposition of the successor representation has been significantly characterized and provides the bridge between the neuroscience of spatial cognition of [O'Keefe and Dostrovsky 1971][research_okeefe_dostrovsky_1971] and [Hafting et al. 2005][research_hafting_et_al_2005] and the successor-representation literature in machine learning.

The free-energy correspondence provides the unifying-principle correspondence. The variational free energy

$$
F(q, o) = \mathbb{E}_{q(s)} \left[ \log q(s) - \log p(o, s) \right] = D_{KL}(q(s) \| p(s \mid o)) - \log p(o)
\tag{47}
$$

specifies the upper bound on surprise that biological agents are proposed to minimize under the [Friston 2010][research_friston_2010] free-energy principle. The account has been substantially formalized and provides the bridge between the neuroscience of perception, action, and learning and the variational-inference framework in machine learning.

The consolidated neuroscience correspondences constitute the settled public domain of the NeuroAI research program. The correspondences provide the empirical constraints against which candidate frameworks in machine learning are evaluated, and the formal apparatus of machine learning provides the computational vocabulary through which neuroscience can articulate and test computational hypotheses.

## Established Psychology Correspondences

The established psychology correspondences consolidate the bidirectional exchanges between the psychology of learning and machine learning that have been markedly validated at the closing of the editorial window. The model was surveyed in detail in [A264 Psychology of Learning][related_post_a264_psychology].

The Rescorla-Wagner-temporal-difference correspondence of [Rescorla and Wagner 1972][research_rescorla_wagner_1972] and [Sutton 1988][research_sutton_1988] provides the paradigmatic correspondence. The finding that the Rescorla-Wagner update rule corresponds mathematically to the temporal-difference update rule in the limit of a limiting case has been appreciably characterized and provides the bridge between the psychology of classical conditioning and modern machine learning.

The model-free-model-based-dual-system correspondence of [Daw et al. 2005][research_daw_niv_dayan_2005] provides the dual-system correspondence. The finding that habitual behavior corresponds to model-free learning and goal-directed behavior corresponds to model-based learning has been greatly characterized in both animal and human experiments and provides the bridge between the psychology of instrumental behavior and modern machine learning.

The prospect-theory-loss-aversion correspondence of [Kahneman and Tversky 1979][research_kahneman_tversky_1979] provides the decision-making correspondence. The finding that human decision-making under uncertainty exhibits systematic deviations from expected-utility theory supports the formalization through the value function

$$
v(x) = \begin{cases} x^\alpha & x \geq 0 \\ -\lambda (-x)^\beta & x < 0 \end{cases}
\tag{48}
$$

with $\lambda > 1$ the loss-aversion coefficient, and the probability-weighting function

$$
w(p) = \frac{p^\gamma}{(p^\gamma + (1-p)^\gamma)^{1/\gamma}}
\tag{49}
$$

that captures the overweighting of small probabilities and underweighting of moderate-to-large probabilities. This formulation has been considerably replicated and provides the empirical constraints against which candidate models of human decision-making are evaluated.

The Bayesian-cognition correspondence of [Tenenbaum et al. 2011][research_tenenbaum_et_al_2011] provides the probabilistic-inference correspondence. The finding that many cognitive phenomena including concept learning, causal reasoning, and inductive generalization admit characterization as Bayesian inference over structured hypothesis spaces admits the formalization

$$
p(h \mid d) = \frac{p(d \mid h) \, p(h)}{\sum_{h' \in \mathcal{H}} p(d \mid h') \, p(h')}
\tag{50}
$$

with $\mathcal{H}$ a structured hypothesis space over concepts, causal graphs, or grammatical rules. The treatment has been significantly characterized and provides the bridge between the psychology of cognition and probabilistic machine learning.

The categorization-and-similarity correspondence provides the representation-learning correspondence. The findings including the [Rosch 1975][research_rosch_1975] prototype theory, the [Nosofsky 1986][research_nosofsky_1986] generalized context model, and the modern [Kemp and Tenenbaum 2008][research_kemp_tenenbaum_2008] structure-discovery framework have been substantially replicated and provide the bridge between the psychology of categorization and modern representation learning.

The spacing-and-retrieval-practice correspondence provides the educational-technology correspondence. The [Ebbinghaus 1885][book_ebbinghaus_1885] forgetting curve

$$
R(t) = R_0 \, e^{-t/\tau}
\tag{51}
$$

with $R(t)$ retention at time $t$ and $\tau$ a memory-time constant, and the [Cepeda et al. 2008][research_cepeda_et_al_2008] distributed-practice power-law form

$$
R(t, s) = R_0 \, (1 + t/s)^{-\beta}
\tag{52}
$$

with $s$ the spacing between study sessions and $\beta$ a task-forgetting parameter, together with the [Roediger and Karpicke 2006][research_roediger_karpicke_2006] test-enhanced-learning framework, have been markedly replicated and provide the practical foundation for modern learning technology.

The consolidated psychology correspondences constitute the settled public domain of the psychology-machine-learning research program. The correspondences provide the empirical constraints against which candidate frameworks in machine learning are evaluated, and the formal apparatus of machine learning provides the computational vocabulary through which psychology can articulate and test its theories.

## The Foundation-Model Turn and Reinforcement Learning

The foundation-model turn constitutes the paradigm shift that has appreciably reorganized the field at the closing of the editorial window. This account treats large pre-trained models, trained on broad corpora through self-supervised learning at scale, as the substrate for downstream experiential learning through fine-tuning, reinforcement learning from human feedback, and agentic frameworks. The integration of foundation models with the classical experiential-learning framework has emerged as one of the most active research areas of the field.

The [Bommasani et al. 2021][research_bommasani_et_al_2021] report On the Opportunities and Risks of Foundation Models provides the institutional consolidation of the paradigm. The framework treats foundation models as the general-purpose substrate whose downstream deployment through the fine-tuning and reinforcement-learning-from-human-feedback pipelines produces the application-capabilities of the modern deployment landscape.

The scaling laws of [Kaplan et al. 2020][research_kaplan_et_al_2020] and the compute-optimal refinement of [Hoffmann et al. 2022][research_hoffmann_et_al_2022] provide the empirical foundation for the paradigm. The findings that model loss follows the parametric relationship

$$
L(N, D) = \frac{A}{N^\alpha} + \frac{B}{D^\beta} + E
\tag{53}
$$

with model size $N$ and training-token count $D$ have greatly shaped the research on the scaling of foundation models and the downstream deployment through experiential learning.

The emergence phenomena of [Wei et al. 2022b][research_wei_et_al_2022_emergent] identify the capabilities that appear discontinuously with scale, and the chain-of-thought prompting framework of [Wei et al. 2022a][research_wei_et_al_2022_cot] provides the reasoning-enhancement technique that continues to organize the research on foundation-model reasoning.

The reinforcement-learning-from-human-feedback pipeline of [Ouyang et al. 2022][research_ouyang_et_al_2022] provides the alignment mechanism that has been considerably deployed across the modern foundation-model deployment landscape. The pipeline comprises the three-stage sequence of supervised fine-tuning on demonstrations, reward-model training on human preferences, and reinforcement-learning optimization of the policy against the learned reward model. The integration of the classical policy-gradient framework with the foundation-model substrate has significantly organized the modern alignment literature.

The constitutional AI framework of [Bai et al. 2022][research_bai_et_al_2022] provides the extension in which the reward-model training uses model-generated preferences guided by a written constitution rather than the direct human preferences. The account has substantially reorganized the scalable-oversight literature and continues to organize the research on foundation-model alignment.

The agentic-frameworks paradigm treats foundation models as the policy substrate for the sequential decision-making tasks that constitute the classical experiential-learning framework. The integration through tool-use, chain-of-thought reasoning, and hierarchical planning provides the research frontier at the intersection of foundation models and reinforcement learning. The empirical performance of agentic foundation models on the benchmarks including SWE-bench, WebArena, and AgentBench remains an active research area whose characterization continues to organize the field.

The tension between the pre-training paradigm and the classical experiential-learning framework remains markedly unresolved. The claim that pre-training on broad corpora appreciably reduces the need for downstream experiential learning is greatly supported by the empirical findings on in-context learning. The counter-claim that experiential learning remains necessary for the tasks that require environmental interaction is considerably supported by the findings on the integration challenges. The research on the optimal integration of pre-training and reinforcement learning remains an active area at the closing of the editorial window.

## Position Papers and Canonical Debates

The position papers and canonical debates that organize the field at the closing of the editorial window characterize the open questions that shape the research directions of the coming period. The model provides the field-level context within which the technical research proceeds.

The Bitter Lesson of [Sutton 2019][research_sutton_2019_bitter_lesson] provides the canonical position statement on the relationship between the general-purpose scaling of computation and the incorporation of human-engineered domain knowledge. The claim that the general-purpose methods that leverage the increases in available computation eventually outperform the methods that incorporate domain-human knowledge has significantly organized the research direction of the field and continues to shape the institutional and technical debates.

The Reward is Enough thesis of [Silver et al. 2021][research_silver_et_al_2021] provides the canonical position statement on the sufficiency of reward maximization as the framework for artificial intelligence. The strong claim

$$
\pi^* = \arg\max_\pi \mathbb{E}_\pi \left[ \sum_{t=0}^\infty \gamma^t r_{t+1} \right]
\tag{54}
$$

as the general framework for goal-directed behavior remains substantially contested at the closing of the editorial window, with the critical responses of [Roy and Duckett 2022][research_roy_duckett_2022] and the alternative frameworks including preference learning and inverse reinforcement learning providing the empirical alternatives.

The Welcome to the Era of Experience position paper of [Silver and Sutton 2024][research_silver_sutton_2024] provides the canonical position statement on the role of experiential learning at the closing of the era of static-data pre-training. The claim that the next generation of AI systems will markedly depend on experiential learning from environmental interaction rather than on the static-data pre-training paradigm has appreciably organized the research direction of the field.

The Catalyzing NeuroAI grand challenges of [Zador et al. 2023][research_zador_et_al_2023] provide the canonical position statement on the research directions in NeuroAI at the closing of the editorial window. The grand challenges including the embodied Turing test, the development of the animal-like AI capabilities, and the bidirectional exchange between neuroscience and machine learning provide the research directions that continue to organize the field.

The alignment-problem framing of [Ngo et al. 2022][research_ngo_chan_mindermann_2022] The Alignment Problem from a Deep Learning Perspective provides the canonical position statement on the alignment challenges facing modern deep learning systems. The taxonomy of misalignment failure modes and the research directions for their resolution have greatly organized the modern alignment-and-safety literature.

The consolidated position papers constitute the field-level context within which the technical research proceeds at the closing of the editorial window. The debates the papers organize continue to shape the research directions of the field, and the resolution of the debates through the empirical developments of subsequent research remains an active research area.

## Open Problems, Theoretical Foundations

The open problems in the theoretical foundations of experiential learning identify the residual questions whose resolution would considerably reorganize the field. This formulation identifies the formal questions that remain contested at the closing of the editorial window.

The deadly-triad problem identifies the instability arising from the combination of off-policy learning, function approximation, and bootstrapping. The divergence examples of [Baird 1995][research_baird_1995] and the systematic characterization of [van Hasselt et al. 2018][research_van_hasselt_et_al_2018] establish the empirical scope of the phenomenon. The empirical practice has assembled workarounds through the target-network stabilization, the experience-replay decorrelation, and the double Q-learning bias-correction techniques. The theoretical characterization of when the triad is safe and when it is unstable remains significantly open and constitutes one of the open problems of the field.

The exploration-exploitation-tradeoff problem in high-dimensional structured environments identifies the gap between the tight regret bounds available for bandits and low-dimensional Markov decision processes and the empirical performance of intrinsic-motivation methods in high-dimensional structured environments. The formal characterization of the sample-complexity of exploration in high-dimensional structured environments remains substantially open.

The partial-observability problem identifies the gap between the tractable partially-observable Markov decision process framework and the empirical reality of partially-observable environments at scale. The formal characterization of what representation-learning objectives suffice for near-optimal control under partial observability remains markedly open.

The sample-complexity-versus-computational-complexity problem identifies the tradeoff between sample-efficient algorithms (typically expensive computationally) and computationally-efficient algorithms (typically expensive in samples). The PAC-MDP sample-complexity bounds of [Kakade 2003][research_kakade_2003] and [Strehl et al. 2009][research_strehl_li_littman_2009]

$$
\tilde{O}\left( \frac{|\mathcal{S}||\mathcal{A}|}{(1 - \gamma)^3 \epsilon^2} \right)
\tag{55}
$$

for tabular reinforcement learning provide the worst-case characterization of the tabular setting, but the corresponding bounds under function approximation, partial observability, and structured environments remain appreciably open. The optimal tradeoff and the conditions under which each family of algorithms is preferred remain greatly open.

The open-endedness problem identifies the gap between the frameworks of reinforcement learning and evolutionary computation and the open-endedness that human cultures and biological evolution exhibit. The formal characterization of open-endedness and the mechanisms that produce it remain considerably open and provide the research frontier for [A261 Evolutionary and Open-Ended Adaptation][related_post_a261_evolutionary].

The reward-hypothesis problem identifies the status of the [Silver et al. 2021][research_silver_et_al_2021] Reward is Enough thesis. The claim in its strong form is that any goal-directed behavior of interest can be characterized as maximization of a expected cumulative reward

$$
\pi^* = \arg\max_\pi \mathbb{E}_\pi \left[ \sum_{t=0}^\infty \gamma^t r_{t+1} \right]
\tag{56}
$$

for a reward specification $r$. The empirical support for the thesis under the conditions of practical machine learning is significantly contested, and the alternative frameworks including preference learning and inverse reinforcement learning provide the empirical alternatives whose relative strengths remain substantially open.

The bounded-agent-and-hierarchical-decomposition problem identifies the formal characterization of hierarchical decomposition under bounded computational resources. The relationships between the options framework, the MAXQ decomposition, the feudal networks framework, and the temporally-extended action frameworks remain markedly open at the level of a unified formal theory.

The consolidated theoretical open problems constitute the research frontier for the theoretical foundations of the field. The research directions have been appreciably characterized in the survey articles of the series and continue to organize modern research.

## Open Problems, Algorithmic Frontiers

The open problems in the algorithmic frontiers identify the residual questions in algorithm design whose resolution would greatly advance the practical capabilities of experiential learning systems.

The credit assignment problem at long horizons identifies the difficulty of assigning credit for delayed rewards at temporal horizons considerably longer than those addressed by the standard algorithms. The eligibility-trace framework and the $n$-step-return framework provide partial solutions, but the credit-assignment problem at very long horizons remains significantly open.

The reward-model-learning problem in reinforcement learning from human feedback identifies the difficulty of learning reward models that generalize to novel behaviors. The findings on reward hacking, specification gaming, and reward-model exploitation surveyed in [Amodei et al. 2016][research_amodei_et_al_2016] Concrete Problems in AI Safety, in [Krakovna 2020][research_krakovna_et_al_2020], and in the systematic study of RLHF failure modes in [Casper et al. 2023][research_casper_et_al_2023] remain substantially uncharacterized and provide the research frontier for [A260 Learning From Demonstration Preference and Other Agents][related_post_a260_demonstration].

The catastrophic-forgetting problem at scale identifies the difficulty of preventing catastrophic forgetting in modern deep learning systems that must acquire and preserve considerable task suites. The empirical findings on the effectiveness of the modern continual-learning algorithms at scale remain markedly uncharacterized and provide the research frontier for [A259 Continual and Lifelong Learning][related_post_a259_continual].

The meta-learning-scale problem identifies the gap between the successes of meta-learning at small scales and the empirical performance of meta-learning at the scale of foundation models. The correspondence between the in-context-learning phenomenon and the classical meta-learning framework remains appreciably open at the level of formal characterization.

The world-model-scale problem identifies the gap between the successes of world models at low-dimensional continuous-control problems and the empirical performance of world models at the scale of complex environments. The representation-learning objectives that suffice for effective world-modeling remain greatly open and provide the research frontier for [A256 World Models and Predictive Model-Based Adaptation][related_post_a256_world_models].

The offline-reinforcement-learning-generalization problem identifies the difficulty of achieving policies that generalize considerably beyond the coverage of the offline dataset. The formal characterization of when offline reinforcement learning permits strong generalization guarantees remains significantly open and provides the research frontier for [A257 Offline and Batch Reinforcement Learning][related_post_a257_offline].

The multi-agent-learning-and-coordination problem identifies the difficulty of achieving coordinated behavior in multi-agent settings without explicit central coordination. The empirical findings on emergent coordination in multi-agent reinforcement learning remain substantially uncharacterized and provide the research frontier for the multi-agent extensions of experiential learning.

The consolidated algorithmic open problems constitute the research frontier for the algorithmic development of the field. The research directions have been markedly characterized in the survey articles of the series and continue to organize modern research.

## Open Problems, Empirical Benchmarks

The open problems in empirical benchmarks identify the residual questions in the measurement and evaluation of experiential learning systems.

The benchmark-validity problem identifies the gap between the empirical performance on standard benchmarks and the empirical performance on the underlying capabilities the benchmarks are intended to measure. The findings on benchmark saturation, benchmark gaming, and benchmark-versus-transfer divergence remain appreciably uncharacterized.

The evaluation-reproducibility problem identifies the difficulty of reproducing the empirical claims in deep reinforcement learning research. The findings including the [Henderson et al. 2018][research_henderson_et_al_2018] characterization of the variance in deep-reinforcement-learning benchmark results have provided the empirical foundation for the modern evaluation-reform movement in the field.

The compute-and-scale-dependence problem identifies the difficulty of separating the algorithmic contributions from the scale-dependent contributions in modern deep reinforcement learning research. The empirical findings that many algorithmic improvements are contingent on the compute and scale conditions provide the empirical foundation for the modern research on scaling laws in reinforcement learning.

The safety-evaluation problem identifies the difficulty of evaluating the safety properties of modern reinforcement learning systems. The empirical findings on reward hacking, specification gaming, and power-seeking behavior remain greatly uncharacterized and provide the research frontier for the safety-evaluation literature.

The consolidated empirical-benchmark open problems constitute the research frontier for the measurement and evaluation infrastructure of the field. The research directions continue to organize modern research on the methodological standards of the field.

## Open Problems, Neuroscience Correspondence

The open problems in the neuroscience correspondence identify the residual questions in the bidirectional exchange between neuroscience and machine learning.

The biological-plausibility-of-backpropagation problem identifies the difficulty of reconciling the effectiveness of backpropagation in machine learning with the implausibility of backpropagation as a biological learning rule surveyed in [Crick 1989][research_crick_1989] and [Lillicrap et al. 2020][research_lillicrap_et_al_2020]. The candidate biological-learning-rule frameworks including feedback alignment of [Lillicrap et al. 2016][research_lillicrap_et_al_2016], predictive coding as a biological learning rule characterized in [Whittington and Bogacz 2017][research_whittington_bogacz_2017], and target propagation of [Lee et al. 2015][research_lee_zhang_fischer_bengio_2015] provide partial solutions, but the correspondence between biological and artificial learning rules remains considerably open.

The scale-and-timescale-correspondence problem identifies the gap between the timescales of biological learning (from milliseconds through decades) and the timescales of artificial learning (typically limited to the training-episode timescale). The correspondence between the biological timescales and the artificial timescales remains significantly open.

The task-optimized-versus-normative problem identifies the tension between the task-optimized-network approach to modeling cortical function and the normative-computational approach. The relationship between the task-optimization objective and the evolutionary-and-developmental history that produced the biological brain remains substantially open.

The consolidated neuroscience-correspondence open problems constitute the research frontier for the NeuroAI research program. The research directions have been markedly characterized in [A263 NeuroAI][related_post_a263_neuroai] and continue to organize modern research.

## Open Problems, Psychological Correspondence

The open problems in the psychological correspondence identify the residual questions in the bidirectional exchange between the psychology of learning and machine learning.

The correspondence-quality problem identifies the difficulty of characterizing the closeness of the correspondence between human learning and machine learning at the level of algorithmic detail. The findings including the systematic divergences between human and machine performance on many tasks provide the empirical foundation for the research on the level at which the correspondence should be evaluated.

The individual-differences problem identifies the difficulty of accommodating the systematic variation across individuals in learning capacity, style, and outcome. The correspondence between the machine learning frameworks and the human-individual-differences literature remains appreciably open and provides the research frontier for the personalized-machine-learning literature.

The consciousness-and-awareness problem identifies the difficulty of characterizing the role of consciousness and awareness in psychological learning phenomena. The correspondence between the machine learning frameworks and the consciousness-and-awareness literature remains greatly open.

The consolidated psychological-correspondence open problems constitute the research frontier for the psychology-machine-learning research program. The research directions have been considerably characterized in [A264 Psychology of Learning][related_post_a264_psychology] and continue to organize modern research.

## Open Problems, Alignment, Safety, and Governance

The open problems in alignment, safety, and governance identify the residual questions in the safe deployment of experiential learning systems.

The reward-specification-problem identifies the difficulty of specifying reward functions that produce the intended behavior across the full deployment distribution. The findings of [Amodei et al. 2016][research_amodei_et_al_2016] on concrete problems in AI safety, the taxonomies of [Krakovna 2020][research_krakovna_et_al_2020] on specification gaming, the characterization of the Goodhart-effect regimes in [Manheim and Garrabrant 2018][research_manheim_garrabrant_2018], and the study of reward-model over-optimization in [Gao et al. 2023][research_gao_schulman_hilton_2023] provide the empirical foundation for the research on reward-specification robustness.

The scalable-oversight-problem identifies the difficulty of providing effective human oversight to reinforcement-learning systems at scales where human evaluation cannot cover the full deployment distribution. The candidate frameworks including debate of [Irving et al. 2018][research_irving_christiano_amodei_2018], iterated amplification of [Christiano et al. 2018][research_christiano_shlegeris_amodei_2018], and constitutional AI of [Bai et al. 2022][research_bai_et_al_2022] provide partial solutions, but the effectiveness of scalable oversight remains significantly open.

The mesa-optimization-and-inner-alignment problem identifies the difficulty of ensuring that the learned policies do not implement internal optimization processes with objectives that diverge from the outer training objective. The taxonomy of [Hubinger et al. 2019][research_hubinger_et_al_2019] Risks from Learned Optimization provides the formal characterization of the problem. The characterization of when mesa-optimization arises and the mechanisms that produce it remain substantially open.

The power-seeking-and-instrumental-convergence problem identifies the empirical and theoretical questions about the conditions under which reinforcement-learning agents develop instrumentally-convergent power-seeking behaviors. The formal analysis of [Turner et al. 2021][research_turner_et_al_2021] Optimal Policies Tend to Seek Power characterizes the class of environments in which instrumental convergence provably arises. The formal characterization of when instrumental convergence arises in the settings of practical machine learning remains markedly open.

The governance-and-deployment-safety problem identifies the institutional questions about the safe deployment of reinforcement-learning systems in the real-world contexts including healthcare, finance, criminal justice, and autonomous systems. The institutional frameworks for the governance of these deployments remain appreciably open and provide the research frontier for the technical-governance literature.

The consolidated alignment-safety-and-governance open problems constitute the research frontier for the safe deployment of the field's technology. The research directions continue to organize modern research on the safety and governance challenges the field faces.

## Empirical Landscape at the Closing of the Editorial Window

The empirical landscape at the closing of the editorial window in the mid 2020s characterizes the state of the field's capabilities, benchmarks, and open questions as of the temporal window of this survey.

Deep reinforcement learning systems have achieved significant performance on the canonical benchmarks including Atari, MuJoCo, Go, chess, and shogi. The empirical performance has greatly saturated on the classical benchmarks, with the human-normalized scores on the fifty-seven-game Atari suite exceeding one hundred percent on the median-game metric for the canonical algorithms, and the MuJoCo continuous-control benchmarks producing the asymptotic performance close to the theoretical maxima for the canonical tasks. The research frontier has considerably shifted to the more challenging benchmarks including the Procgen generalization benchmarks of [Cobbe et al. 2020][research_cobbe_et_al_2020], the Meta-World multi-task benchmarks of [Yu et al. 2020][research_yu_et_al_2020], the bsuite behavior suite of [Osband et al. 2020][research_osband_et_al_2020] for characterizing agent behavior along the dimensions of memory, generalization, and exploration, the complex real-time strategy games as characterized in the OpenAI Five Dota 2 system of [OpenAI et al. 2019][research_berner_et_al_2019] and the AlphaStar StarCraft II system of [Vinyals et al. 2019][research_vinyals_et_al_2019], the NetHack learning environment of [Küttler et al. 2020][research_kuttler_et_al_2020] as a specifically-difficult exploration benchmark, and the open-ended learning environments including XLand of [Open-Ended Team 2021][research_openended_team_2021].

Foundation models as characterized in [Bommasani et al. 2021][research_bommasani_et_al_2021] have emerged as a new paradigm that significantly reshapes the research landscape. The findings including the scaling laws of [Kaplan et al. 2020][research_kaplan_et_al_2020] and [Hoffmann et al. 2022][research_hoffmann_et_al_2022], the in-context-learning phenomena of [Brown 2020][research_brown_et_al_2020], and the reinforcement-learning-from-human-feedback pipelines of [Ouyang et al. 2022][research_ouyang_et_al_2022] have substantially reorganized the field's research agenda. The integration of foundation models with the classical reinforcement-learning framework remains an active and rapidly-moving research area.

Offline reinforcement learning has emerged as a practical framework for the deployment of reinforcement learning in the settings where online interaction is expensive or unsafe. The empirical performance of the canonical offline algorithms has been markedly characterized on the benchmark datasets, and the practical applications to healthcare, robotics, and recommendation systems have appreciably matured.

Meta-learning and in-context learning have emerged as the mechanisms through which foundation models achieve their broad task competence. The relationship between the classical meta-learning framework and the in-context-learning phenomena of foundation models continues to organize substantial research.

Alignment and safety research has emerged as a institutional research area with marked funding, staffing, and institutional consolidation. The empirical findings on reward hacking, specification gaming, and power-seeking behavior have provided the foundation for the research on the safe deployment of the field's technology.

The institutional consolidation of the field has continued with the emergence of dedicated conferences, journals, and open-source infrastructure. The research communities including the reinforcement learning, safe reinforcement learning, offline reinforcement learning, and NeuroAI communities have greatly matured and provide the institutional infrastructure for the cumulative-progress dynamics of the field.

The consolidated empirical landscape provides the starting point from which the research developments of the subsequent years will proceed. The settled-versus-open partition that this article surveys will be considerably revised by the research developments that occur in the intervening period.

## Applications, Established and Emerging

The applications of experiential learning have significantly expanded across the corpus of settled-and-emerging deployment contexts.

Established applications include the deployment of reinforcement learning in the domains of game playing (including chess, Go, poker as demonstrated in [Brown and Sandholm 2018][research_brown_sandholm_2018] Libratus and [Moravčík et al. 2017][research_moravcik_et_al_2017] DeepStack, video games, and real-time strategy), recommendation systems, dialogue systems, robot control (including manipulation, locomotion, and navigation), datacenter cooling of [Lazic et al. 2018][research_lazic_et_al_2018], chip design of [Mirhoseini et al. 2021][research_mirhoseini_et_al_2021], and drug discovery. The empirical findings have substantially matured in these domains and continue to organize the practical research on their deployment.

Emerging applications include the deployment of reinforcement learning in the domains of autonomous driving, healthcare (including treatment recommendation, drug dosing, and adaptive clinical trials), education (including personalized instruction and adaptive testing), financial services (including trading, portfolio management, and fraud detection), and scientific discovery (including materials science, protein design as demonstrated in the AlphaFold protein-structure-prediction system of [Jumper et al. 2021][research_jumper_et_al_2021], and mathematical proof discovery). The empirical findings continue to organize the practical research on the deployment challenges these domains present.

The bidirectional exchange with foundation models has produced a new family of applications including reinforcement learning from human feedback for language models, agentic-behavior systems, and multi-modal reasoning systems. The integration of the classical experiential-learning framework with the foundation-model framework continues to organize the research on the next generation of experiential-learning applications.

The consolidated applications landscape provides the practical impact of the field's cumulative research. The applications continue to shape the research directions of the field, and the bidirectional exchange between application-driven research and foundation-oriented research continues to produce the research dynamics that this article surveys.

## The Series Closing

The sixteen-article series has surveyed the science and theory of adaptive, reinforcement, and experiential learning artificial intelligence together with the neuroscience and psychology of learning from which the field has borrowed extensively and to which it contributes reciprocally. The treatment has been extensive and interdisciplinary, and the settled-versus-open partition that this article draws provides the starting point from which the research developments of the subsequent years will proceed.

The decision to survey the field at the closing of the mid-2020s editorial window represents a choice about the temporal indexing of the survey. The findings that are settled at this window may be revised by subsequent research, and the open problems may be resolved by research that appears shortly after this window. The choice to index the survey to this window reflects the institutional and empirical consolidation that has occurred in the field across the recent decades, and the readiness of the field for a consolidation-and-frontier survey of the present kind.

The bidirectional exchange between machine learning, neuroscience, and psychology that this series has surveyed continues to produce the research dynamics that will shape the field in the subsequent decades. The formal apparatus of machine learning provides the computational vocabulary through which neuroscience and psychology can articulate and test their theories. The empirical findings and existence proofs of neuroscience and psychology provide the biological and cognitive constraints against which candidate frameworks in machine learning are evaluated. The bidirectional exchange has produced sizable contributions in each direction and provides the research infrastructure through which the residual open problems of the field will be resolved.

The readers of the series are encouraged to consult the individual survey articles for the detailed treatment of each research area. Article one provides the framing and the six-axis analytical framework that organizes the series. Articles two through fifteen provide the detailed surveys of the research areas. The present article provides the consolidated synthesis and the settled-versus-open partition at the closing of the editorial window. The corpus continues to organize the research directions of the field, and the bidirectional exchange between machine learning, neuroscience, and psychology continues to produce the research dynamics through which the residual open problems will be resolved.

## Load-Bearing Open Questions

- What is the correct partition of the field's claims into settled public, established private, and open categories, and how does the partition evolve across the temporal window of the survey?
- How should the institutional infrastructure of the field be reorganized to close the gap between the established private claims of frontier research and the reproducibility standards of open science?
- What is the correct characterization of the residual open problems in the theoretical foundations, algorithmic frontiers, empirical benchmarks, neuroscience correspondence, psychological correspondence, and alignment safety and governance areas surveyed in this article?
- How should the bidirectional exchange between machine learning, neuroscience, and psychology be organized to maximize the research dynamics that produce the cumulative progress the series has surveyed?
- What is the correct account of the temporal-decay problem that any synthesis of a moving field faces, and how should the settled-versus-open partition be maintained across the temporal window of the survey?
- How should the alignment, safety, and governance research be integrated with the technical research on experiential learning to produce the safe and beneficial deployment of the field's technology?
- What is the correct account of the relationship between the classical experiential-learning framework and the foundation-model framework that has emerged in recent years?
- How should the practical applications of experiential learning to healthcare, education, autonomous systems, and scientific discovery be organized to maximize the beneficial impact while minimizing the safety and governance risks?
- What is the correct account of the role of the psychological and neuroscience-informed constraints on the research directions of the field?
- Can the consolidated corpus of the series inform the design of the next generation of experiential learning systems that address the residual open problems the series has surveyed?

## Equations

<!-- Equations generated by _lib/equations.py from _sources/equations/. Edit the data file and regenerate. Do not edit this section by hand. -->

This section collects the 56 display equations of the article in the order they appear,
each under its number and reproduced exactly as it stands in the text.
A title in bold names an established result,
and a title in italics beginning with the word Bespoke names a construction made for this analysis.
Of the 56, 54 are established and 2 are bespoke.
Returns, values and regret carry the units of the reward, the discount factor and all probabilities are dimensionless, and symbols such as $\alpha$, $\beta$, $\eta$, $\lambda$ and $\gamma$ are reused with a different meaning in each framework, so every equation is read with the symbols defined beside it.

*Equation 1, Bespoke Update of the Established Public Baseline.*
The article models the established public baseline as a recursive update from new empirical developments, with an institutional rate and an update function that admits findings once they meet the reproducibility criteria.

$$
B_{t+1} = B_t + \eta \, \Delta(B_t, E_t)
\tag{1}
$$

**Equation 2, Markov Decision Process Tuple.**
A Markov decision process is specified by its state space, action space, transition kernel, reward function, discount factor and initial state distribution.
[Bellman 1957][book_bellman_1957]
[Howard 1960][book_howard_1960]

$$
\mathcal{M} = (\mathcal{S}, \mathcal{A}, P, R, \gamma, \mu_0)
\tag{2}
$$

**Equation 3, Discounted Return.**
The return from a time step is the sum of all later rewards, each discounted geometrically by its delay.

$$
G_t = \sum_{k=0}^\infty \gamma^k r_{t+k+1}
\tag{3}
$$

**Equation 4, Trajectory Distribution Induced by a Policy.**
The probability of a trajectory is the initial state probability times the product of the policy and transition probabilities along it.

$$
p_\pi(\tau) = \mu_0(s_0) \prod_{t=0}^\infty \pi(a_t \mid s_t) \, P(s_{t+1} \mid s_t, a_t)
\tag{4}
$$

**Equation 5, Discounted State-Occupancy Measure.**
The normalised discounted occupancy of a state is the discount-weighted sum of the probabilities of visiting it at each step.

$$
d^\pi(s) = (1 - \gamma) \sum_{t=0}^\infty \gamma^t \, \Pr_\pi(s_t = s)
\tag{5}
$$

**Equation 6, State-Value Function.**
The value of a state under a policy is the expected discounted return when starting from that state.
[Bellman 1957][book_bellman_1957]

$$
V^\pi(s) = \mathbb{E}_\pi \left[ \sum_{t=0}^\infty \gamma^t r_{t+1} \mid s_0 = s \right]
\tag{6}
$$

**Equation 7, Bellman Expectation Equation.**
The value of a state equals the policy-weighted and transition-weighted average of the immediate reward plus the discounted value of the successor state.
[Bellman 1957][book_bellman_1957]

$$
V^\pi(s) = \sum_a \pi(a \mid s) \sum_{s'} P(s' \mid s, a) \left[ R(s, a, s') + \gamma V^\pi(s') \right]
\tag{7}
$$

**Equation 8, Action-Value Function.**
The action value is the expected discounted return when starting from a state, taking a given action and following the policy thereafter.

$$
Q^\pi(s, a) = \mathbb{E}_\pi \left[ \sum_{t=0}^\infty \gamma^t r_{t+1} \mid s_0 = s, a_0 = a \right]
\tag{8}
$$

**Equation 9, Advantage Function.**
The advantage of an action is its action value minus the value of the state.

$$
A^\pi(s, a) = Q^\pi(s, a) - V^\pi(s)
\tag{9}
$$

**Equation 10, Bellman Optimality Equation for State Values.**
The optimal value of a state is the maximum over actions of the expected immediate reward plus the discounted optimal value of the successor.
[Bellman 1957][book_bellman_1957]

$$
V^*(s) = \max_a \sum_{s'} P(s' \mid s, a) \left[ R(s, a, s') + \gamma V^*(s') \right]
\tag{10}
$$

**Equation 11, Bellman Optimality Equation for Action Values.**
The optimal action value is the expected immediate reward plus the discounted maximum optimal action value in the successor state.
[Bellman 1957][book_bellman_1957]

$$
Q^*(s, a) = \sum_{s'} P(s' \mid s, a) \left[ R(s, a, s') + \gamma \max_{a'} Q^*(s', a') \right]
\tag{11}
$$

**Equation 12, Belief-State Update.**
Under partial observability the belief is propagated through the transition model, reweighted by the observation likelihood and renormalised.

$$
b_{t+1}(s') = \frac{O(o_{t+1} \mid s') \sum_s P(s' \mid s, a_t) \, b_t(s)}{\sum_{s''} O(o_{t+1} \mid s'') \sum_s P(s'' \mid s, a_t) \, b_t(s)}
\tag{12}
$$

**Equation 13, Temporal-Difference Error.**
The temporal-difference error is the reward plus the discounted value of the next state minus the value of the current state.
[Sutton 1988][research_sutton_1988]

$$
\delta_t = r_{t+1} + \gamma V(s_{t+1}) - V(s_t)
\tag{13}
$$

**Equation 14, Temporal-Difference Value Update.**
The value estimate of the current state moves toward its bootstrapped target by a step proportional to the temporal-difference error.
[Sutton 1988][research_sutton_1988]

$$
V(s_t) \leftarrow V(s_t) + \alpha \delta_t
\tag{14}
$$

**Equation 15, Q-Learning Update.**
The off-policy Q-learning update moves an action value toward the reward plus the discounted maximum action value in the next state.
[Watkins 1989][research_watkins_1989]

$$
Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha \left[ r_{t+1} + \gamma \max_a Q(s_{t+1}, a) - Q(s_t, a_t) \right]
\tag{15}
$$

**Equation 16, Policy Gradient Theorem.**
The gradient of expected return is the expectation of the score function of the policy weighted by the action value.
[Williams 1992][research_williams_1992]
[Sutton et al. 1999b][research_sutton_et_al_2000]

$$
\nabla_\theta J(\theta) = \mathbb{E}_{\pi_\theta} \left[ \sum_t \nabla_\theta \log \pi_\theta(a_t \mid s_t) \, Q^{\pi_\theta}(s_t, a_t) \right]
\tag{16}
$$

**Equation 17, Rescorla-Wagner Update.**
The associative strength of each stimulus changes in proportion to the shared prediction error between the asymptote and the summed strength of all stimuli present.
[Rescorla and Wagner 1972][research_rescorla_wagner_1972]

$$
\Delta V_i = \alpha_i \beta \left( \lambda - \sum_j V_j \right)
\tag{17}
$$

**Equation 18, Lai-Robbins Regret Lower Bound.**
Any consistent bandit algorithm incurs regret growing at least logarithmically in the horizon, with each suboptimal arm contributing its gap divided by its Kullback-Leibler divergence from the optimal arm.
[Lai and Robbins 1985][research_lai_robbins_1985]

$$
R_T \geq \sum_{a: \Delta_a > 0} \frac{\log T}{D_{KL}(P_a \| P_{a^*})} \, \Delta_a + o(\log T)
\tag{18}
$$

**Equation 19, Upper Confidence Bound Action Selection.**
The upper confidence bound rule selects the arm whose empirical mean plus a confidence radius that shrinks with its pull count is largest.
[Auer et al. 2002][research_auer_cesa_bianchi_fischer_2002]

$$
a_t = \arg\max_a \left[ \hat{\mu}_a + \sqrt{\frac{2 \log t}{N_a(t)}} \right]
\tag{19}
$$

**Equation 20, Thompson Sampling.**
Thompson sampling draws model parameters from the posterior and acts greedily with respect to the draw.
[Thompson 1933][research_thompson_1933]

$$
\theta_t \sim p(\theta \mid \mathcal{D}_{t-1}), \quad a_t = \arg\max_a \mathbb{E}[r \mid a, \theta_t]
\tag{20}
$$

**Equation 21, Deep Q-Network Target-Network Loss.**
The deep Q-network minimises the squared temporal-difference error on replayed transitions against a target computed with a separate slowly updated network.
[Mnih et al. 2015][research_mnih_et_al_2015]

$$
\mathcal{L}(\theta) = \mathbb{E}_{(s, a, r, s') \sim \mathcal{D}} \left[ \left( r + \gamma \max_{a'} Q_{\theta^-}(s', a') - Q_\theta(s, a) \right)^2 \right]
\tag{21}
$$

**Equation 22, Proximal Policy Optimisation Clipped Objective.**
Proximal policy optimisation takes the minimum of the ratio-weighted advantage and its clipped counterpart, which removes the incentive to move the policy far from its previous iterate.
[Schulman et al. 2017][research_schulman_et_al_2017]

$$
\mathcal{L}^{\text{CLIP}}(\theta) = \mathbb{E}_t \left[ \min \left( \rho_t(\theta) \hat{A}_t, \, \text{clip}(\rho_t(\theta), 1 - \epsilon, 1 + \epsilon) \hat{A}_t \right) \right]
\tag{22}
$$

**Equation 23, Maximum-Entropy Objective of Soft Actor-Critic.**
Soft actor-critic maximises expected reward plus a temperature-weighted entropy of the policy at each visited state.
[Haarnoja et al. 2018][research_haarnoja_et_al_2018]

$$
J(\pi) = \sum_t \mathbb{E}_{(s_t, a_t) \sim \pi} \left[ r(s_t, a_t) + \alpha \mathcal{H}(\pi(\cdot \mid s_t)) \right]
\tag{23}
$$

**Equation 24, Pseudocount Exploration Bonus.**
The augmented reward adds a bonus inversely proportional to the square root of the pseudocount of the visited state.
[Bellemare et al. 2016][research_bellemare_et_al_2016]

$$
r^+_t = r_t + \frac{\beta}{\sqrt{\hat{N}(s_t)}}
\tag{24}
$$

**Equation 25, Prediction-Error Curiosity Reward.**
The intrinsic reward is the scaled squared error of a forward model predicting the feature embedding of the next state.
[Pathak et al. 2017][research_pathak_et_al_2017]

$$
r^i_t = \eta \left\| \hat{\phi}(s_{t+1}) - \phi(s_{t+1}) \right\|_2^2
\tag{25}
$$

**Equation 26, Empowerment as Channel Capacity.**
Empowerment is the maximum over action-sequence distributions of the mutual information between an $n$-step action sequence and the resulting state.
[Klyubin et al. 2005][research_klyubin_polani_nehaniv_2005]

$$
\mathfrak{E}(s) = \max_{\omega} I(A_t^n; S_{t+n} \mid s_t = s)
\tag{26}
$$

**Equation 27, Option Tuple.**
An option comprises an initiation set, an intra-option policy and a termination condition.
[Sutton et al. 1999a][research_sutton_precup_singh_1999]

$$
o = \langle \mathcal{I}_o, \pi_o, \beta_o \rangle
\tag{27}
$$

**Equation 28, Semi-Markov Option Value Function.**
The value of a state under a policy over options sums the discounted rewards accumulated while an option runs and the value of the state where it terminates, discounted by its duration.
[Sutton et al. 1999a][research_sutton_precup_singh_1999]

$$
V^\mu(s) = \sum_o \mu(o \mid s) \, \mathbb{E}\!\left[ \sum_{j=1}^{k} \gamma^{j-1} r_{t+j} + \gamma^k V^\mu(s_{t+k}) \,\middle|\, s, o \right]
\tag{28}
$$

**Equation 29, Dyna Interleaved Update.**
Dyna learns transition and reward models from data and applies the Q-learning update to both real experience and experience simulated from the learned model.
[Sutton 1991][research_sutton_1991]

$$
\hat{P}, \hat{R} \leftarrow \text{Learn}(\mathcal{D}); \quad Q \leftarrow Q + \alpha \left[ r + \gamma \max_{a'} Q(s', a') - Q(s, a) \right] \text{ on both real and simulated experience}
\tag{29}
$$

**Equation 30, Conservative Q-Learning Penalty.**
Conservative Q-learning adds to the temporal-difference loss a penalty that pushes down a soft maximum of action values while pushing up the values of actions in the dataset.
[Kumar et al. 2020][research_kumar_et_al_2020]

$$
\mathcal{L}_{\text{CQL}}(\theta) = \alpha \left[ \mathbb{E}_{s \sim \mathcal{D}} \log \sum_a \exp Q_\theta(s, a) - \mathbb{E}_{(s, a) \sim \mathcal{D}} Q_\theta(s, a) \right] + \mathcal{L}_{\text{TD}}(\theta)
\tag{30}
$$

**Equation 31, Behaviour-Regularised Policy Objective.**
Behaviour regularisation maximises the action value under the learned policy minus a penalty on its divergence from the behaviour policy that generated the data.
[Levine et al. 2020][research_levine_et_al_2020]

$$
\pi = \arg\max_\pi \mathbb{E}_{s \sim \mathcal{D}, a \sim \pi} [Q(s, a)] - \lambda \, D(\pi \| \pi_\beta)
\tag{31}
$$

**Equation 32, Model-Agnostic Meta-Learning Objective.**
Model-agnostic meta-learning chooses initial parameters that minimise the summed task losses after one inner gradient step on each task.
[Finn Abbeel Levine 2017][research_finn_abbeel_levine_2017]

$$
\theta^* = \arg\min_\theta \sum_{\mathcal{T}_i \sim p(\mathcal{T})} \mathcal{L}_{\mathcal{T}_i} \left( \theta - \alpha \nabla_\theta \mathcal{L}_{\mathcal{T}_i}(\theta) \right)
\tag{32}
$$

**Equation 33, Elastic Weight Consolidation Loss.**
Elastic weight consolidation adds to the new-task loss a quadratic penalty on each parameter's departure from its old-task value, weighted by the Fisher information.
[Kirkpatrick et al. 2017][research_kirkpatrick_et_al_2017]

$$
\mathcal{L}(\theta) = \mathcal{L}_B(\theta) + \sum_i \frac{\lambda}{2} F_i (\theta_i - \theta^*_{A, i})^2
\tag{33}
$$

**Equation 34, Behaviour Cloning Objective.**
Behaviour cloning fits the policy by maximising the log-likelihood of expert actions given expert states.

$$
\pi_{\text{BC}} = \arg\max_\pi \mathbb{E}_{(s, a) \sim \mathcal{D}_E} \log \pi(a \mid s)
\tag{34}
$$

**Equation 35, Generative Adversarial Imitation Learning Objective.**
Generative adversarial imitation learning trains a discriminator to separate policy and expert state-action pairs while the policy minimises the discriminator objective less an entropy bonus.
[Ho and Ermon 2016][research_ho_ermon_2016]

$$
\min_\pi \max_D \mathbb{E}_{\pi}[\log D(s, a)] + \mathbb{E}_{\pi_E}[\log(1 - D(s, a))] - \lambda \mathcal{H}(\pi)
\tag{35}
$$

**Equation 36, Maximum-Entropy Inverse Reinforcement Learning Trajectory Model.**
Maximum-entropy inverse reinforcement learning makes the probability of a trajectory proportional to the exponential of its summed learned reward.
[Ziebart 2008][research_ziebart_et_al_2008]

$$
p(\tau) \propto \exp\left( \sum_t r_\phi(s_t, a_t) \right)
\tag{36}
$$

**Equation 37, Bradley-Terry Trajectory Preference Model.**
The probability that one trajectory segment is preferred to another is a softmax over their summed predicted rewards.
[Christiano et al. 2017][research_christiano_et_al_2017]

$$
P(\tau^1 \succ \tau^2) = \frac{\exp \sum_t \hat{r}_\phi(s^1_t, a^1_t)}{\exp \sum_t \hat{r}_\phi(s^1_t, a^1_t) + \exp \sum_t \hat{r}_\phi(s^2_t, a^2_t)}
\tag{37}
$$

**Equation 38, Evolution Strategies Gradient Estimator.**
The gradient of the Gaussian-smoothed fitness equals the expectation of the fitness of a perturbed parameter vector times the perturbation, divided by the noise scale.
[Salimans et al. 2017][research_salimans_et_al_2017]

$$
\nabla_\theta \mathbb{E}_{\epsilon \sim \mathcal{N}(0, I)} \left[ F(\theta + \sigma \epsilon) \right] = \frac{1}{\sigma} \mathbb{E}_\epsilon \left[ F(\theta + \sigma \epsilon) \, \epsilon \right]
\tag{38}
$$

**Equation 39, MAP-Elites Archive Cell.**
Each cell of the Multi-dimensional Archive of Phenotypic Elites retains the fittest solution found whose behaviour falls in that cell.
[Mouret and Clune 2015][research_mouret_clune_2015]

$$
\mathcal{A}[c] = \arg\max_{x \in \text{Cell}(c)} F(x)
\tag{39}
$$

**Equation 40, Chinchilla Parametric Scaling Law.**
Loss is an irreducible term plus separate power-law terms that fall with parameter count and with training-token count.
[Hoffmann et al. 2022][research_hoffmann_et_al_2022]

$$
L(N, D) = \frac{A}{N^\alpha} + \frac{B}{D^\beta} + E
\tag{40}
$$

**Equation 41, Compute-Optimal Allocation.**
For a fixed compute budget the loss-minimising parameter count and token count each scale as a power of the budget.
[Hoffmann et al. 2022][research_hoffmann_et_al_2022]

$$
N^*(C) \propto C^a, \quad D^*(C) \propto C^b
\tag{41}
$$

**Equation 42, Conditional Value at Risk of the Return.**
The conditional value at risk is the expected return conditioned on falling at or below its lower quantile at level $\alpha$.

$$
\text{CVaR}_\alpha[G] = \mathbb{E}[G \mid G \leq q_\alpha(G)]
\tag{42}
$$

**Equation 43, Dopamine Reward Prediction Error Correspondence.**
The phasic firing of midbrain dopamine neurons is proportional to the temporal-difference error.
[Schultz et al. 1997][research_schultz_dayan_montague_1997]

$$
\text{DA firing rate at } t \propto \delta_t = r_{t+1} + \gamma V(s_{t+1}) - V(s_t)
\tag{43}
$$

**Equation 44, Hierarchical Predictive Coding Update.**
Each level carries the residual between its representation and the top-down prediction from the level above, and its representation moves to reduce its own error and the error it leaves in the level below.
[Rao and Ballard 1999][research_rao_ballard_1999]

$$
\epsilon_l = x_l - g_l(x_{l+1}), \quad x_l \leftarrow x_l + \eta \left( - \epsilon_l + \frac{\partial g_{l-1}(x_l)}{\partial x_l}^\top \epsilon_{l-1} \right)
\tag{44}
$$

**Equation 45, Successor Representation.**
The successor representation is the expected discounted number of future visits to each state from a starting state under the policy.
[Dayan 1993][research_dayan_1993]

$$
M^\pi(s, s') = \mathbb{E}_\pi \left[ \sum_{t=0}^\infty \gamma^t \, \mathbb{1}[s_t = s'] \mid s_0 = s \right]
\tag{45}
$$

**Equation 46, Value Factorised Through the Successor Representation.**
The value of a state is the successor representation applied to the state reward vector.
[Dayan 1993][research_dayan_1993]

$$
V^\pi(s) = \sum_{s'} M^\pi(s, s') R(s')
\tag{46}
$$

**Equation 47, Variational Free Energy.**
Free energy is the expected log ratio of the approximate posterior to the joint, equal to the Kullback-Leibler divergence from the true posterior minus the log evidence, so it bounds surprise from above.
[Friston 2010][research_friston_2010]

$$
F(q, o) = \mathbb{E}_{q(s)} \left[ \log q(s) - \log p(o, s) \right] = D_{KL}(q(s) \| p(s \mid o)) - \log p(o)
\tag{47}
$$

**Equation 48, Prospect Theory Value Function.**
The value function is a power function that is concave for gains and convex and steeper for losses, with the loss-aversion coefficient scaling the loss branch.
[Kahneman and Tversky 1979][research_kahneman_tversky_1979]

$$
v(x) = \begin{cases} x^\alpha & x \geq 0 \\ -\lambda (-x)^\beta & x < 0 \end{cases}
\tag{48}
$$

**Equation 49, Prospect Theory Probability Weighting Function.**
The one-parameter weighting function of cumulative prospect theory overweights small probabilities and underweights moderate and large ones.

$$
w(p) = \frac{p^\gamma}{(p^\gamma + (1-p)^\gamma)^{1/\gamma}}
\tag{49}
$$

**Equation 50, Bayes' Rule over a Hypothesis Space.**
The posterior over hypotheses is the likelihood times the prior normalised over the structured hypothesis space.
[Tenenbaum et al. 2011][research_tenenbaum_et_al_2011]

$$
p(h \mid d) = \frac{p(d \mid h) \, p(h)}{\sum_{h' \in \mathcal{H}} p(d \mid h') \, p(h')}
\tag{50}
$$

**Equation 51, Exponential Forgetting Curve.**
Retention decays exponentially from its initial value with a single memory time constant, the textbook simplification of the forgetting curve.

$$
R(t) = R_0 \, e^{-t/\tau}
\tag{51}
$$

*Equation 52, Bespoke Spacing-Dependent Power-Law Retention.*
The article writes retention as a power law in the ratio of the retention interval to the study spacing, a form it supplies rather than the fit reported in the cited meta-analysis.

$$
R(t, s) = R_0 \, (1 + t/s)^{-\beta}
\tag{52}
$$

**Equation 53, Chinchilla Parametric Scaling Law Restated.**
The same parametric law expresses loss as an irreducible term plus power-law terms in parameter count and training-token count.
[Hoffmann et al. 2022][research_hoffmann_et_al_2022]

$$
L(N, D) = \frac{A}{N^\alpha} + \frac{B}{D^\beta} + E
\tag{53}
$$

**Equation 54, Optimal Policy as Maximiser of Expected Discounted Return.**
The optimal policy is the policy that maximises the expected discounted return, the objective that the reward-is-enough thesis holds to be sufficient for intelligence.
[Silver et al. 2021][research_silver_et_al_2021]

$$
\pi^* = \arg\max_\pi \mathbb{E}_\pi \left[ \sum_{t=0}^\infty \gamma^t r_{t+1} \right]
\tag{54}
$$

**Equation 55, Tabular Sample Complexity Bound.**
The number of samples needed for an $\epsilon$-optimal policy in a tabular problem scales with the number of state-action pairs, the inverse cube of one minus the discount and the inverse square of the accuracy, up to logarithmic factors.

$$
\tilde{O}\left( \frac{|\mathcal{S}||\mathcal{A}|}{(1 - \gamma)^3 \epsilon^2} \right)
\tag{55}
$$

**Equation 56, Optimal Policy Restated for the Reward Hypothesis.**
The strong form of the reward hypothesis holds that any goal-directed behaviour of interest is the policy maximising expected discounted return for some reward specification.
[Silver et al. 2021][research_silver_et_al_2021]

$$
\pi^* = \arg\max_\pi \mathbb{E}_\pi \left[ \sum_{t=0}^\infty \gamma^t r_{t+1} \right]
\tag{56}
$$

### Notation

- $B_t$, the established public baseline at time $t$
- $E_t$, the empirical developments in the intervening period
- $\mu_0$, the initial state distribution
- $G_t$, the discounted return from step $t$
- $d^\pi(s)$, the normalised discounted state-occupancy measure of policy $\pi$
- $V^\pi(s)$, the state-value function of policy $\pi$
- $Q^\pi(s, a)$, the action-value function of policy $\pi$
- $A^\pi(s, a)$, the advantage function of policy $\pi$
- $b_t(s)$, the belief state, a probability distribution over hidden states at step $t$
- $\delta_t$, the temporal-difference error at step $t$
- $R_T$, the cumulative regret over horizon $T$
- $\Delta_a$, the suboptimality gap of arm $a$
- $N_a(t)$, the number of pulls of arm $a$ up to round $t$
- $Q_{\theta^-}$, the target network's action-value estimate
- $\rho_t(\theta)$, the ratio of the new to the old policy probability of the taken action
- $\hat{A}_t$, the advantage estimate at step $t$
- $\mathcal{H}$, the entropy of a policy in the objectives of equations 23 and 35, and the hypothesis space in equation 50
- $\hat{N}(s_t)$, the pseudocount of the visited state
- $\mathfrak{E}(s)$, the empowerment of state $s$
- $\pi_\beta$, the behaviour policy that generated the offline dataset
- $F_i$, the diagonal Fisher information of parameter $i$ on the old task
- $\mathcal{D}_E$, the dataset of expert demonstrations
- $L(N, D)$, the loss as a function of parameter count $N$ and training-token count $D$
- $q_\alpha(G)$, the lower $\alpha$-quantile of the return distribution
- $M^\pi(s, s')$, the successor representation of policy $\pi$
- $g_l$, the top-down generative model at level $l$
- $v(x)$, the prospect theory value of an outcome $x$
- $w(p)$, the prospect theory decision weight of probability $p$
- $R(t, s)$, the retention at time $t$ after a study session with spacing $s$

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Primary Sources, Peer-Reviewed

- Auer, Peter, Nicolò Cesa-Bianchi, and Paul Fischer. 2002. "Finite-Time Analysis of the Multiarmed Bandit Problem." *Machine Learning* 47 (2–3): 235–56. [https://doi.org/10.1023/a:1013689704352][research_auer_cesa_bianchi_fischer_2002]
- Crick, Francis. 1989. "The Recent Excitement about Neural Networks." *Nature* 337 (6203): 129–32. [https://doi.org/10.1038/337129a0][research_crick_1989]
- Daw, Nathaniel D., Yael Niv, and Peter Dayan. 2005. "Uncertainty-Based Competition between Prefrontal and Dorsolateral Striatal Systems for Behavioral Control." *Nature Neuroscience* 8 (12): 1704–11. [https://doi.org/10.1038/nn1560][research_daw_niv_dayan_2005]
- Foster, David J., and Matthew A. Wilson. 2006. "Reverse Replay of Behavioural Sequences in Hippocampal Place Cells during the Awake State." *Nature* 440 (7084): 680–83. [https://doi.org/10.1038/nature04587][research_foster_wilson_2006]
- Friston, Karl. 2010. "The Free-Energy Principle: A Unified Brain Theory?" *Nature Reviews Neuroscience* 11 (2): 127–38. [https://doi.org/10.1038/nrn2787][research_friston_2010]
- Hafting, Torkel, Marianne Fyhn, Sturla Molden, May-Britt Moser, and Edvard I. Moser. 2005. "Microstructure of a Spatial Map in the Entorhinal Cortex." *Nature* 436 (7052): 801–6. [https://doi.org/10.1038/nature03721][research_hafting_et_al_2005]
- Jumper, John, Richard Evans, Alexander Pritzel, et al. 2021. "Highly Accurate Protein Structure Prediction with AlphaFold." *Nature* 596 (7873): 583–89. [https://doi.org/10.1038/s41586-021-03819-2][research_jumper_et_al_2021]
- Klyubin, A. S., D. Polani, and C. L. Nehaniv. 2005. "Empowerment: A Universal Agent-Centric Measure of Control." In *2005 IEEE Congress on Evolutionary Computation*, vol. 1. IEEE. [https://doi.org/10.1109/cec.2005.1554676][research_klyubin_polani_nehaniv_2005]
- Kriegeskorte, Nikolaus, Mur, and Bandettini. 2008. "Representational Similarity Analysis – Connecting the Branches of Systems Neuroscience." *Frontiers in Systems Neuroscience*. [https://doi.org/10.3389/neuro.06.004.2008][research_kriegeskorte_mur_bandettini_2008]
- Kumaran, Dharshan, Demis Hassabis, and James L. McClelland. 2016. "What Learning Systems Do Intelligent Agents Need? Complementary Learning Systems Theory Updated." *Trends in Cognitive Sciences* 20 (7): 512–34. [https://doi.org/10.1016/j.tics.2016.05.004][research_kumaran_mcclelland_hassabis_2016]
- Lai, T. L., and Herbert Robbins. 1985. "Asymptotically Efficient Adaptive Allocation Rules." *Advances in Applied Mathematics* 6 (1): 4–22. [https://doi.org/10.1016/0196-8858(85)90002-8][research_lai_robbins_1985]
- Lee, Dong-Hyun, Saizheng Zhang, Asja Fischer, and Yoshua Bengio. 2015. "Difference Target Propagation." In *Machine Learning and Knowledge Discovery in Databases*. Springer International Publishing. [https://doi.org/10.1007/978-3-319-23528-8\_31][research_lee_zhang_fischer_bengio_2015]
- Lillicrap, Timothy P., Daniel Cownden, Douglas B. Tweed, and Colin J. Akerman. 2016. "Random Synaptic Feedback Weights Support Error Backpropagation for Deep Learning." *Nature Communications* 7 (1): 13276. [https://doi.org/10.1038/ncomms13276][research_lillicrap_et_al_2016]
- Lillicrap, Timothy P., Adam Santoro, Luke Marris, Colin J. Akerman, and Geoffrey Hinton. 2020. "Backpropagation and the Brain." *Nature Reviews Neuroscience* 21 (6): 335–46. [https://doi.org/10.1038/s41583-020-0277-3][research_lillicrap_et_al_2020]
- Lin, Long-Ji. 1992. "Self-Improving Reactive Agents Based on Reinforcement Learning, Planning and Teaching." *Machine Learning* 8 (3–4): 293–321. [https://doi.org/10.1007/bf00992699][research_lin_1992]
- Mirhoseini, Azalia, Anna Goldie, Mustafa Yazgan, et al. 2021. "A Graph Placement Methodology for Fast Chip Design." *Nature* 594 (7862): 207–12. [https://doi.org/10.1038/s41586-021-03544-w][research_mirhoseini_et_al_2021]
- Mnih, Volodymyr, Koray Kavukcuoglu, David Silver, et al. 2015. "Human-Level Control through Deep Reinforcement Learning." *Nature* 518 (7540): 529–33. [https://doi.org/10.1038/nature14236][research_mnih_et_al_2015]
- O'Keefe, J., and J. Dostrovsky. 1971. "The Hippocampus as a Spatial Map. Preliminary Evidence from Unit Activity in the Freely-Moving Rat." *Brain Research* 34 (1): 171–75. [https://doi.org/10.1016/0006-8993(71)90358-1][research_okeefe_dostrovsky_1971]
- Pathak, Deepak, Pulkit Agrawal, Alexei A. Efros, and Trevor Darrell. 2017. "Curiosity-Driven Exploration by Self-Supervised Prediction." In *2017 IEEE Conference on Computer Vision and Pattern Recognition Workshops (CVPRW)*. IEEE. [https://doi.org/10.1109/cvprw.2017.70][research_pathak_et_al_2017]
- Rao, Rajesh P. N., and Dana H. Ballard. 1999. "Predictive Coding in the Visual Cortex: A Functional Interpretation of Some Extra-Classical Receptive-Field Effects." *Nature Neuroscience* 2 (1): 79–87. [https://doi.org/10.1038/4580][research_rao_ballard_1999]
- Schrimpf, Martin, Jonas Kubilius, Michael J. Lee, N. Apurva Ratan Murty, Robert Ajemian, and James J. DiCarlo. 2020. "Integrative Benchmarking to Advance Neurally Mechanistic Models of Human Intelligence." *Neuron* 108 (3): 413–23. [https://doi.org/10.1016/j.neuron.2020.07.040][research_schrimpf_et_al_2020]
- Schrittwieser, Julian, Ioannis Antonoglou, Thomas Hubert, et al. 2020. "Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model." *Nature* 588 (7839): 604–9. [https://doi.org/10.1038/s41586-020-03051-4][research_schrittwieser_et_al_2020]
- Silver, David, Aja Huang, Chris J. Maddison, et al. 2016. "Mastering the Game of Go with Deep Neural Networks and Tree Search." *Nature* 529 (7587): 484–89. [https://doi.org/10.1038/nature16961][research_silver_et_al_2016]
- Silver, David, Julian Schrittwieser, Karen Simonyan, et al. 2017. "Mastering the Game of Go without Human Knowledge." *Nature* 550 (7676): 354–59. [https://doi.org/10.1038/nature24270][research_silver_et_al_2017]
- Silver, David, Satinder Singh, Doina Precup, and Richard S. Sutton. 2021. "Reward Is Enough." *Artificial Intelligence* 299: 103535. [https://doi.org/10.1016/j.artint.2021.103535][research_silver_et_al_2021]
- Stachenfeld, Kimberly L., Matthew M. Botvinick, and Samuel J. Gershman. 2017. "The Hippocampus as a Predictive Map." *Nature Neuroscience* 20 (11): 1643–53. [https://doi.org/10.1038/nn.4650][research_stachenfeld_botvinick_gershman_2017]
- Sutton, Richard S. 1988. "Learning to Predict by the Methods of Temporal Differences." *Machine Learning* 3 (1): 9–44. [https://doi.org/10.1007/bf00115009][research_sutton_1988]
- Sutton, Richard S., Doina Precup, and Satinder Singh. 1999a. "Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning." *Artificial Intelligence* 112 (1–2): 181–211. [https://doi.org/10.1016/s0004-3702(99)00052-1][research_sutton_precup_singh_1999]
- Todorov, Emanuel, Tom Erez, and Yuval Tassa. 2012. "MuJoCo: A Physics Engine for Model-Based Control." In *2012 IEEE/RSJ International Conference on Intelligent Robots and Systems*. IEEE. [https://doi.org/10.1109/iros.2012.6386109][research_todorov_erez_tassa_2012]
- Vinyals, Oriol, Igor Babuschkin, Wojciech M. Czarnecki, et al. 2019. "Grandmaster Level in StarCraft II Using Multi-Agent Reinforcement Learning." *Nature* 575 (7782): 350–54. [https://doi.org/10.1038/s41586-019-1724-z][research_vinyals_et_al_2019]
- Watkins, Christopher J. C. H., and Peter Dayan. 1992. "Q-Learning." *Machine Learning* 8 (3–4): 279–92. [https://doi.org/10.1007/bf00992698][research_watkins_dayan_1992]
- Williams, Ronald J. 1992. "Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning." *Machine Learning* 8 (3–4): 229–56. [https://doi.org/10.1007/bf00992696][research_williams_1992]
- Zador, Anthony, Sean Escola, Blake Richards, et al. 2023. "Catalyzing Next-Generation Artificial Intelligence through NeuroAI." *Nature Communications* 14 (1): 1597. [https://doi.org/10.1038/s41467-023-37180-x][research_zador_et_al_2023]

### Primary Sources, Non-Peer-Reviewed

- Abbeel, Pieter, and Andrew Y. Ng. 2004. "Apprenticeship Learning via Inverse Reinforcement Learning." In *Twenty-first international conference on Machine learning - ICML '04*. ACM Press. [https://doi.org/10.1145/1015330.1015430][research_abbeel_ng_2004]
- Amodei, Dario, Chris Olah, Jacob Steinhardt, Paul Christiano, John Schulman, and Dan Mané. 2016. "Concrete Problems in AI Safety." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1606.06565][research_amodei_et_al_2016]
- Bacon, Pierre-Luc, Jean Harb, and Doina Precup. 2017. "The Option-Critic Architecture." *Proceedings of the AAAI Conference on Artificial Intelligence* 31 (1). [https://doi.org/10.1609/aaai.v31i1.10916][research_bacon_harb_precup_2017]
- Bai, Yuntao, Saurav Kadavath, Sandipan Kundu, et al. 2022. "Constitutional AI: Harmlessness from AI Feedback." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2212.08073][research_bai_et_al_2022]
- Baird, Leemon. 1995. "Residual Algorithms: Reinforcement Learning with Function Approximation." In *Machine Learning Proceedings 1995*. Elsevier. [https://doi.org/10.1016/b978-1-55860-377-6.50013-x][research_baird_1995]
- Bellemare, Marc G., Will Dabney, and Rémi Munos. 2017. "A Distributional Perspective on Reinforcement Learning." In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v70/bellemare17a.html][research_bellemare_dabney_munos_2017]
- Bellemare, M. G., Y. Naddaf, J. Veness, and M. Bowling. 2013. "The Arcade Learning Environment: An Evaluation Platform for General Agents." *Journal of Artificial Intelligence Research* 47: 253–79. [https://doi.org/10.1613/jair.3912][research_bellemare_et_al_2013]
- Bellemare, Marc, iram Srinivasan Sr., Georg Ostrovski, Tom Schaul, David Saxton, and Remi Munos. 2016. "Unifying Count-Based Exploration and Intrinsic Motivation." *Advances in Neural Information Processing Systems* 29. [https://papers.nips.cc/paper/2016/hash/afda332245e2af431fb7b672a68b659d-Abstract.html][research_bellemare_et_al_2016]
- Bengio, Yoshua, Jérôme Louradour, Ronan Collobert, and Jason Weston. 2009. "Curriculum Learning." In *Proceedings of the 26th Annual International Conference on Machine Learning*. ACM. [https://doi.org/10.1145/1553374.1553380][research_bengio_et_al_2009]
- Bommasani, Rishi, Drew A. Hudson, Ehsan Adeli, et al. 2021. "On the Opportunities and Risks of Foundation Models." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2108.07258][research_bommasani_et_al_2021]
- Brown, Noam, and Tuomas Sandholm. 2018. "Superhuman AI for Heads-up No-Limit Poker: Libratus Beats Top Professionals." *Science* 359 (6374): 418–24. [https://doi.org/10.1126/science.aao1733][research_brown_sandholm_2018]
- Casper, Stephen, Xander Davies, Claudia Shi, et al. 2023. "Open Problems and Fundamental Limitations of Reinforcement Learning from Human Feedback." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2307.15217][research_casper_et_al_2023]
- Cepeda, Nicholas J., Edward Vul, Doug Rohrer, John T. Wixted, and Harold Pashler. 2008. "Spacing Effects in Learning: A Temporal Ridgeline of Optimal Retention." *Psychological Science* 19 (11): 1095–1102. [https://doi.org/10.1111/j.1467-9280.2008.02209.x][research_cepeda_et_al_2008]
- Chaudhry, Arslan, Marc'Aurelio Ranzato, Marcus Rohrbach, and Mohamed Elhoseiny. 2018. "Efficient Lifelong Learning with A-GEM." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1812.00420][research_chaudhry_et_al_2019]
- Christiano, Paul F., Jan Leike, Tom Brown, Miljan Martic, Shane Legg, and Dario Amodei. 2017. "Deep Reinforcement Learning from Human Preferences." *Advances in Neural Information Processing Systems* 30. [https://papers.nips.cc/paper/2017/hash/d5e2c0adad503c91f91df240d0cd4e49-Abstract.html][research_christiano_et_al_2017]
- Christiano, Paul, Buck Shlegeris, and Dario Amodei. 2018. "Supervising Strong Learners by Amplifying Weak Experts." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1810.08575][research_christiano_shlegeris_amodei_2018]
- Cobbe, Karl, Chris Hesse, Jacob Hilton, and John Schulman. 2020. "Leveraging Procedural Generation to Benchmark Reinforcement Learning." In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v119/cobbe20a.html][research_cobbe_et_al_2020]
- Dabney, Will, Georg Ostrovski, David Silver, and Remi Munos. 2018b. "Implicit Quantile Networks for Distributional Reinforcement Learning." In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v80/dabney18a.html][research_dabney_et_al_2018_iqn]
- Dabney, Will, Mark Rowland, Marc Bellemare, and Rémi Munos. 2018a. "Distributional Reinforcement Learning with Quantile Regression." *Proceedings of the AAAI Conference on Artificial Intelligence* 32 (1). [https://doi.org/10.1609/aaai.v32i1.11791][research_dabney_et_al_2018_qr_dqn]
- Dayan, Peter, and Geoffrey E. Hinton. 1992. "Feudal Reinforcement Learning." *Advances in Neural Information Processing Systems* 5. [https://papers.nips.cc/paper/1992/hash/d14220ee66aeec73c49038385428ec4c-Abstract.html][research_dayan_hinton_1993]
- Dietterich, T. G. 2000. "Hierarchical Reinforcement Learning with the MAXQ Value Function Decomposition." *Journal of Artificial Intelligence Research* 13: 227–303. [https://doi.org/10.1613/jair.639][research_dietterich_2000]
- Duan, Yan, John Schulman, Xi Chen, Peter L. Bartlett, Ilya Sutskever, and Pieter Abbeel. 2016. "RL^2: Fast Reinforcement Learning via Slow Reinforcement Learning." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1611.02779][research_duan_et_al_2016]
- Gao, Leo, John Schulman, and Jacob Hilton. 2023. "Scaling Laws for Reward Model Overoptimization." In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v202/gao23h.html][research_gao_schulman_hilton_2023]
- Ha, David, and Jürgen Schmidhuber. 2018. "Recurrent World Models Facilitate Policy Evolution." *Advances in Neural Information Processing Systems* 31. [https://papers.nips.cc/paper/2018/hash/2de5d16682c3c35007e4e92982f1a2ba-Abstract.html][research_ha_schmidhuber_2018]
- Haarnoja, Tuomas, Aurick Zhou, Pieter Abbeel, and Sergey Levine. 2018. "Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor." In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v80/haarnoja18b.html][research_haarnoja_et_al_2018]
- Hafner, Danijar, Timothy Lillicrap, Jimmy Ba, and Mohammad Norouzi. 2019. "Dream to Control: Learning Behaviors by Latent Imagination." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1912.01603][research_hafner_et_al_2020]
- Hafner, Danijar, Jurgis Pasukonis, Jimmy Ba, and Timothy Lillicrap. 2023. "Mastering Diverse Domains through World Models." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2301.04104][research_hafner_et_al_2023]
- Henderson, Peter, Riashat Islam, Philip Bachman, Joelle Pineau, Doina Precup, and David Meger. 2018. "Deep Reinforcement Learning That Matters." *Proceedings of the AAAI Conference on Artificial Intelligence* 32 (1). [https://doi.org/10.1609/aaai.v32i1.11694][research_henderson_et_al_2018]
- Hoffmann, Jordan, Sebastian Borgeaud, Arthur Mensch, et al. 2022. "Training Compute-Optimal Large Language Models." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2203.15556][research_hoffmann_et_al_2022]
- Houthooft, Rein, Xi Chen, Xi Chen, et al. 2016. "VIME: Variational Information Maximizing Exploration." In *Advances in Neural Information Processing Systems*. [https://papers.nips.cc/paper\_files/paper/2016/hash/abd815286ba1007abfbb8415b83ae2cf-Abstract.html][research_houthooft_et_al_2016]
- Hubinger, Evan, Chris van Merwijk, Vladimir Mikulik, Joar Skalse, and Scott Garrabrant. 2019. "Risks from Learned Optimization in Advanced Machine Learning Systems." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1906.01820][research_hubinger_et_al_2019]
- Irving, Geoffrey, Paul Christiano, and Dario Amodei. 2018. "AI Safety via Debate." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1805.00899][research_irving_christiano_amodei_2018]
- Kahneman, Daniel, and Amos Tversky. 1979. "Prospect Theory: An Analysis of Decision under Risk." *Econometrica* 47 (2): 263. [https://doi.org/10.2307/1914185][research_kahneman_tversky_1979]
- Kaplan, Jared, Sam McCandlish, Tom Henighan, et al. 2020. "Scaling Laws for Neural Language Models." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2001.08361][research_kaplan_et_al_2020]
- Kemp, Charles, and Joshua B. Tenenbaum. 2008. "The Discovery of Structural Form." *Proceedings of the National Academy of Sciences* 105 (31): 10687–92. [https://doi.org/10.1073/pnas.0802631105][research_kemp_tenenbaum_2008]
- Khaligh-Razavi, Seyed-Mahdi, and Nikolaus Kriegeskorte. 2014. "Deep Supervised, but Not Unsupervised, Models May Explain IT Cortical Representation." *PLoS Computational Biology* 10 (11): e1003915. [https://doi.org/10.1371/journal.pcbi.1003915][research_khaligh_razavi_kriegeskorte_2014]
- Kirkpatrick, James, Razvan Pascanu, Neil Rabinowitz, et al. 2017. "Overcoming Catastrophic Forgetting in Neural Networks." *Proceedings of the National Academy of Sciences* 114 (13): 3521–26. [https://doi.org/10.1073/pnas.1611835114][research_kirkpatrick_et_al_2017]
- Kostrikov, Ilya, Ashvin Nair, and Sergey Levine. 2021. "Offline Reinforcement Learning with Implicit Q-Learning." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2110.06169][research_kostrikov_nair_levine_2022]
- Kumar, Aviral, Aurick Zhou, George Tucker, and Sergey Levine. 2020. "Conservative Q-Learning for Offline Reinforcement Learning." *Advances in Neural Information Processing Systems* 33: 1179–91. [https://papers.nips.cc/paper/2020/hash/0d2b2061826a5df3221116a5085a6052-Abstract.html][research_kumar_et_al_2020]
- Küttler, Heinrich, Nantas Nardelli, Alexander Miller, et al. 2020. "The NetHack Learning Environment." *Advances in Neural Information Processing Systems* 33: 7671–84. [https://papers.nips.cc/paper/2020/hash/569ff987c643b4bedf504efda8f786c2-Abstract.html][research_kuttler_et_al_2020]
- Lazic, Nevena, Craig Boutilier, Tyler Lu, et al. 2018. "Data Center Cooling Using Model-Predictive Control." *Advances in Neural Information Processing Systems* 31. [https://papers.nips.cc/paper/2018/hash/059fdcd96baeb75112f09fa1dcc740cc-Abstract.html][research_lazic_et_al_2018]
- Lehman, Joel, and Kenneth O. Stanley. 2011. "Novelty Search and the Problem with Objectives." In *Genetic and Evolutionary Computation*. Springer New York. [https://doi.org/10.1007/978-1-4614-1770-5\_3][research_lehman_stanley_2011]
- Levine, Sergey, Aviral Kumar, George Tucker, and Justin Fu. 2020. "Offline Reinforcement Learning: Tutorial, Review, and Perspectives on Open Problems." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2005.01643][research_levine_et_al_2020]
- Lillicrap, Timothy P., Jonathan J. Hunt, Alexander Pritzel, et al. 2015. "Continuous Control with Deep Reinforcement Learning." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1509.02971][research_lillicrap_et_al_2015]
- Lopez-Paz, David, and Marc'Aurelio Ranzato. 2017. "Gradient Episodic Memory for Continual Learning." *Advances in Neural Information Processing Systems* 30. [https://papers.nips.cc/paper/2017/hash/f87522788a2be2d171666752f97ddebb-Abstract.html][research_lopez_paz_ranzato_2017]
- Manheim, David, and Scott Garrabrant. 2018. "Categorizing Variants of Goodhart's Law." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1803.04585][research_manheim_garrabrant_2018]
- McClelland, James L., Bruce L. McNaughton, and Randall C. O'Reilly. 1995. "Why There Are Complementary Learning Systems in the Hippocampus and Neocortex: Insights from the Successes and Failures of Connectionist Models of Learning and Memory." *Psychological Review* 102 (3): 419–57. [https://doi.org/10.1037/0033-295x.102.3.419][research_mcclelland_mcnaughton_oreilly_1995]
- Mnih, Volodymyr, Adria Puigdomenech Badia, Mehdi Mirza, et al. 2016. "Asynchronous Methods for Deep Reinforcement Learning." In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v48/mniha16.html][research_mnih_et_al_2016]
- Moravčík, Matej, Martin Schmid, Neil Burch, et al. 2017. "DeepStack: Expert-Level Artificial Intelligence in Heads-up No-Limit Poker." *Science* 356 (6337): 508–13. [https://doi.org/10.1126/science.aam6960][research_moravcik_et_al_2017]
- Mouret, Jean-Baptiste, and Jeff Clune. 2015. "Illuminating Search Spaces by Mapping Elites." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1504.04909][research_mouret_clune_2015]
- Ngo, Richard, Lawrence Chan, and Sören Mindermann. 2022. "The Alignment Problem from a Deep Learning Perspective." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2209.00626][research_ngo_chan_mindermann_2022]
- Nosofsky, Robert M. 1986. "Attention, Similarity, and the Identification–categorization Relationship." *Journal of Experimental Psychology: General* 115 (1): 39–57. [https://doi.org/10.1037/0096-3445.115.1.39][research_nosofsky_1986]
- Open-Ended Team. 2021. *XLand*. [https://scholar.google.com/scholar?q=XLand+Open-Ended+Team+2021][research_openended_team_2021]
- OpenAI, Christopher Berner, Greg Brockman, et al. 2019. "Dota 2 with Large Scale Deep Reinforcement Learning." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1912.06680][research_berner_et_al_2019]
- Osband, Ian, Yotam Doron, Matteo Hessel, et al. 2020. "Behaviour Suite for Reinforcement Learning." In *International Conference on Learning Representations*. [https://openreview.net/forum?id=rygf-kSYwH][research_osband_et_al_2020]
- Ouyang, Long, Jeffrey Wu, Xu Jiang, et al. 2022. "Training Language Models to Follow Instructions with Human Feedback." In *Advances in Neural Information Processing Systems 35*. Neural Information Processing Systems Foundation, Inc. (NeurIPS). [https://doi.org/10.52202/068431-2011][research_ouyang_et_al_2022]
- Roediger, Henry L., and Jeffrey D. Karpicke. 2006. "Test-Enhanced Learning: Taking Memory Tests Improves Long-Term Retention." *Psychological Science* 17 (3): 249–55. [https://doi.org/10.1111/j.1467-9280.2006.01693.x][research_roediger_karpicke_2006]
- Rosch, Eleanor. 1975. "Cognitive Representations of Semantic Categories." *Journal of Experimental Psychology: General* 104 (3): 192–233. [https://doi.org/10.1037/0096-3445.104.3.192][research_rosch_1975]
- Roy and Duckett. 2022. *Reward is Enough Critique*. [https://scholar.google.com/scholar?q=Reward+is+Enough+Critique+Roy+Duckett+2022][research_roy_duckett_2022]
- Rusu, Andrei A., Neil C. Rabinowitz, Guillaume Desjardins, et al. 2016. "Progressive Neural Networks." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1606.04671][research_rusu_et_al_2016]
- Salimans, Tim, Jonathan Ho, Xi Chen, Szymon Sidor, and Ilya Sutskever. 2017. "Evolution Strategies as a Scalable Alternative to Reinforcement Learning." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1703.03864][research_salimans_et_al_2017]
- Schulman, John, Sergey Levine, Pieter Abbeel, Michael Jordan, and Philipp Moritz. 2015. "Trust Region Policy Optimization." In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v37/schulman15.html][research_schulman_et_al_2015]
- Schulman, John, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. 2017. "Proximal Policy Optimization Algorithms." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1707.06347][research_schulman_et_al_2017]
- Schultz, Wolfram, Peter Dayan, and P. Read Montague. 1997. "A Neural Substrate of Prediction and Reward." *Science* 275 (5306): 1593–99. [https://doi.org/10.1126/science.275.5306.1593][research_schultz_dayan_montague_1997]
- Shin, Hanul, Jung Kwon Lee, Jaehong Kim, and Jiwon Kim. 2017. "Continual Learning with Deep Generative Replay." *Advances in Neural Information Processing Systems* 30. [https://papers.nips.cc/paper/2017/hash/0efbe98067c6c73dba1250d2beaa81f9-Abstract.html][research_shin_et_al_2017]
- Silver, David, Thomas Hubert, Julian Schrittwieser, et al. 2018. "A General Reinforcement Learning Algorithm That Masters Chess, Shogi, and Go through Self-Play." *Science* 362 (6419): 1140–44. [https://doi.org/10.1126/science.aar6404][research_silver_et_al_2018]
- Silver, David, Guy Lever, Nicolas Heess, Thomas Degris, Daan Wierstra, and Martin Riedmiller. 2014. "Deterministic Policy Gradient Algorithms." In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v32/silver14.html][research_silver_et_al_2014]
- Stiennon, Nisan, Long Ouyang, Jeffrey Wu, et al. 2020. "Learning to Summarize with Human Feedback." *Advances in Neural Information Processing Systems* 33: 3008–21. [https://papers.nips.cc/paper/2020/hash/1f89885d556929e98d3ef9b86448f951-Abstract.html][research_stiennon_et_al_2020]
- Strehl, Alexander L., Lihong Li, and Michael L. Littman. 2009. "Reinforcement Learning in Finite MDPs: PAC Analysis." *Journal of Machine Learning Research* 10: 2413–44. [https://jmlr.org/papers/v10/strehl09a.html][research_strehl_li_littman_2009]
- Sutton, Richard S. 1991. "Dyna, an Integrated Architecture for Learning, Planning, and Reacting." *ACM SIGART Bulletin* 2 (4): 160–63. [https://doi.org/10.1145/122344.122377][research_sutton_1991]
- Sutton, Richard S., David McAllester, Satinder Singh, and Yishay Mansour. 1999b. "Policy Gradient Methods for Reinforcement Learning with Function Approximation." *Advances in Neural Information Processing Systems* 12. [https://papers.nips.cc/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html][research_sutton_et_al_2000]
- Tenenbaum, Joshua B., Charles Kemp, Thomas L. Griffiths, and Noah D. Goodman. 2011. "How to Grow a Mind: Statistics, Structure, and Abstraction." *Science* 331 (6022): 1279–85. [https://doi.org/10.1126/science.1192788][research_tenenbaum_et_al_2011]
- Turner, Alex, Logan Smith, Rohin Shah, Andrew Critch, and Prasad Tadepalli. 2021. "Optimal Policies Tend to Seek Power." *Advances in Neural Information Processing Systems* 34: 23063–74. [https://papers.nips.cc/paper/2021/hash/c26820b8a4c1b3c2aa868d6d57e14a79-Abstract.html][research_turner_et_al_2021]
- Van, Hasselt, Guez, and Silver. 2016. *Double DQN*. [https://scholar.google.com/scholar?q=Double+DQN+Van+Hasselt+Guez+2016][research_van_hasselt_guez_silver_2016]
- van Hasselt, Hado, Yotam Doron, Florian Strub, Matteo Hessel, Nicolas Sonnerat, and Joseph Modayil. 2018. "Deep Reinforcement Learning and the Deadly Triad." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1812.02648][research_van_hasselt_et_al_2018]
- Vezhnevets, Alexander Sasha, Simon Osindero, Tom Schaul, et al. 2017. "FeUdal Networks for Hierarchical Reinforcement Learning." In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v70/vezhnevets17a.html][research_vezhnevets_et_al_2017]
- Wang, Jane X., Zeb Kurth-Nelson, Dhruva Tirumala, et al. 2016b. "Learning to Reinforcement Learn." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1611.05763][research_wang_et_al_2016]
- Wang, Rui, Joel Lehman, Jeff Clune, and Kenneth O. Stanley. 2019. "Paired Open-Ended Trailblazer (POET): Endlessly Generating Increasingly Complex and Diverse Learning Environments and Their Solutions." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1901.01753][research_wang_lehman_clune_stanley_2019]
- Wang, Ziyu, Tom Schaul, Matteo Hessel, Hado Hasselt, Marc Lanctot, and Nando Freitas. 2016a. "Dueling Network Architectures for Deep Reinforcement Learning." In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v48/wangf16.html][research_wang_et_al_2016_dueling]
- Wei, Jason, Yi Tay, Rishi Bommasani, et al. 2022b. "Emergent Abilities of Large Language Models." *Transactions on Machine Learning Research*. [https://openreview.net/forum?id=yzkSU5zdwD][research_wei_et_al_2022_emergent]
- Wei, Jason, Xuezhi Wang, Dale Schuurmans, et al. 2022a. "Chain-Of-Thought Prompting Elicits Reasoning in Large Language Models." In *Advances in Neural Information Processing Systems 35*. Neural Information Processing Systems Foundation, Inc. (NeurIPS). [https://doi.org/10.52202/068431-1800][research_wei_et_al_2022_cot]
- Weng, Juyang, James McClelland, Alex Pentland, et al. 2001. "Autonomous Mental Development by Robots and Animals." *Science* 291 (5504): 599–600. [https://doi.org/10.1126/science.291.5504.599][research_weng_et_al_2001]
- Wilson, Matthew A., and Bruce L. McNaughton. 1994. "Reactivation of Hippocampal Ensemble Memories during Sleep." *Science* 265 (5172): 676–79. [https://doi.org/10.1126/science.8036517][research_wilson_mcnaughton_1994]
- Yamins, Daniel L. K., Ha Hong, Charles F. Cadieu, Ethan A. Solomon, Darren Seibert, and James J. DiCarlo. 2014. "Performance-Optimized Hierarchical Models Predict Neural Responses in Higher Visual Cortex." *Proceedings of the National Academy of Sciences* 111 (23): 8619–24. [https://doi.org/10.1073/pnas.1403112111][research_yamins_et_al_2014]
- Yu, Tianhe, Deirdre Quillen, Zhanpeng He, et al. 2020. "Meta-World: A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning." In *Conference on Robot Learning*. [https://proceedings.mlr.press/v100/yu20a.html][research_yu_et_al_2020]

### Secondary Sources

- Bellman. 1957. *Dynamic Programming Princeton Landmarks in Mathematics*. Princeton University Press. [https://press.princeton.edu/books/paperback/9780691146683/dynamic-programming][book_bellman_1957]
- Bertsekas, Dimitri P., and Tsitsiklis. 1996. *Neuro-Dynamic Programming*. Athena Scientific. [http://www.athenasc.com/ndpbook.html][book_bertsekas_tsitsiklis_1996]
- Ebbinghaus. 1885. *Memory*. [https://www.taylorfrancis.com/books/mono/10.4324/9781315802749/memory-hermann-ebbinghaus][book_ebbinghaus_1885]
- Howard, Ronald Arthur. 1960. *Dynamic Programming and Markov Processes*. MIT Press. [https://mitpress.mit.edu/9780262080095/dynamic-programming-and-markov-processes/][book_howard_1960]
- Kahneman, Daniel. 2011. *Thinking, Fast and Slow*. Penguin Books, Limited. [https://us.macmillan.com/books/9780374533557/thinkingfastandslow][book_kahneman_2011]
- Pfeifer, Rolf, and Bongard. 2007. *How the Body Shapes the Way We Think: A New View of Intelligence (Bradford Books)*. The MIT Press. [https://mitpress.mit.edu/9780262162395/how-the-body-shapes-the-way-we-think/][book_pfeifer_bongard_2007]
- Russell, Stuart J., and Peter Norvig. 2020. *Artificial Intelligence: A Modern Approach*. Pearson Education, Limited. [https://aima.cs.berkeley.edu/][book_russell_norvig_2020]
- Sutton, Richard S., and Barto. 2018. *Reinforcement Learning: An Introduction*. MIT Press. [http://incompleteideas.net/book/the-book-2nd.html][book_sutton_barto_2018]

### Commercial Sources

- "DeepMind x UCL RL Course." n.d. Accessed October 25, 2026. [https://www.deepmind.com/learning-resources/reinforcement-learning-lecture-series-2021][ref_deepmind_ucl_rl]
- "Welcome to Spinning up in Deep RL! — Spinning up Documentation." n.d. Accessed October 25, 2026. [https://spinningup.openai.com/][ref_openai_spinning_up]

### General Sources

- "Berkeley CS285." n.d. Accessed October 25, 2026. [https://rail.eecs.berkeley.edu/deeprlcourse/][ref_berkeley_cs285]
- Brown. 2020. "GPT-3 In-Context Learning." [https://papers.nips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html][research_brown_et_al_2020]
- Dayan. 1993. "Successor Representation." [https://direct.mit.edu/neco/article-abstract/5/4/613/5786][research_dayan_1993]
- Deisenroth and Rasmussen. 2011. "PILCO." [https://dl.acm.org/doi/10.5555/3104482.3104541][research_deisenroth_rasmussen_2011]
- Finn Abbeel Levine. 2017. "MAML." [https://proceedings.mlr.press/v70/finn17a.html][research_finn_abbeel_levine_2017]
- Fujimoto Hoof Meger. 2018. "TD3." [https://proceedings.mlr.press/v80/fujimoto18a.html][research_fujimoto_hoof_meger_2018]
- Fujimoto Meger Precup. 2019. "Batch-Constrained Q-Learning." [https://proceedings.mlr.press/v97/fujimoto19a.html][research_fujimoto_meger_precup_2019]
- Ho and Ermon. 2016. "GAIL." [https://papers.nips.cc/paper/2016/hash/cc7e2b878868cbae992d1fb743995d8f-Abstract.html][research_ho_ermon_2016]
- Kakade. 2003. "Sample Complexity of RL." [https://homepages.inf.ed.ac.uk/csutton/publications/kakade-thesis.pdf][research_kakade_2003]
- Krakovna. 2020. "Specification Gaming: The Flip Side of AI Ingenuity." *Google DeepMind*. Accessed October 25, 2026. [https://deepmind.google/discover/blog/specification-gaming-the-flip-side-of-ai-ingenuity/][research_krakovna_et_al_2020]
- Ng and Russell. 2000. "Inverse Reinforcement Learning." [https://ai.stanford.edu/~ang/papers/icml00-irl.pdf][research_ng_russell_2000]
- O'Regan and Noë. 2001. "Sensorimotor Contingency." [https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/sensorimotor-account-of-vision-and-visual-consciousness/1B49A6F4EA76ECBD0938815EEE18C7DC][research_oregan_noe_2001]
- Open Science Collaboration. 2015. "Reproducibility Project." [https://www.science.org/doi/10.1126/science.aac4716][research_osc_2015]
- Rescorla and Wagner. 1972. "Classical Conditioning." [https://scholar.google.com/scholar?q=rescorla+wagner+1972+theory+pavlovian+conditioning][research_rescorla_wagner_1972]
- Rummery and Niranjan. 1994. "SARSA." [https://www.researchgate.net/publication/2500611\_On-Line\_Q-Learning\_Using\_Connectionist\_Systems][research_rummery_niranjan_1994]
- Silver and Sutton. 2024. "Era of Experience." [https://storage.googleapis.com/deepmind-media/Era-of-Experience%20/The%20Era%20of%20Experience%20Paper.pdf][research_silver_sutton_2024]
- "Silver RL Course UCL." n.d. Accessed October 25, 2026. [https://www.davidsilver.uk/teaching/][ref_silver_rl_course]
- "Stanford CS234." n.d. Accessed October 25, 2026. [https://web.stanford.edu/class/cs234/][ref_stanford_cs234]
- Stanley and Miikkulainen. 2002. "NEAT." [https://direct.mit.edu/evco/article/10/2/99/1123][research_stanley_miikkulainen_2002]
- Sutton. 2019. "The Bitter Lesson." [http://www.incompleteideas.net/IncIdeas/BitterLesson.html][research_sutton_2019_bitter_lesson]
- Thompson. 1933. "Thompson Sampling." [https://www.jstor.org/stable/2332286][research_thompson_1933]
- Van Seijen. 2009. "Expected SARSA." [https://ieeexplore.ieee.org/document/4927542][research_van_seijen_et_al_2009]
- Watkins. 1989. "Q-Learning." [https://www.cs.rhul.ac.uk/~chrisw/new\_thesis.pdf][research_watkins_1989]
- Whittington and Bogacz. 2017. "Predictive Coding as Biological Learning." [https://direct.mit.edu/neco/article-abstract/29/5/1229/8261][research_whittington_bogacz_2017]
- Ziebart. 2008. "Maximum Entropy IRL." [https://cdn.aaai.org/AAAI/2008/AAAI08-227.pdf][research_ziebart_et_al_2008]

### Related Posts

- Sechter, Brendan. 2025. "Machines That Learn From Experience: Framing." *Brendan A R Sechter's Development Blog*, December 18. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/18/machines\_that\_learn\_from\_experience\_framing.html][related_post_a250_framing]
- Sechter, Brendan. 2025. "Machines That Learn From Experience: Bandits and Online Learning." *Brendan A R Sechter's Development Blog*, December 19. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/19/machines\_that\_learn\_from\_experience\_bandits\_and\_online\_learning.html][related_post_a251_bandits]
- Sechter, Brendan. 2025. "Machines That Learn From Experience: Reinforcement Learning Foundations." *Brendan A R Sechter's Development Blog*, December 20. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/20/machines\_that\_learn\_from\_experience\_reinforcement\_learning\_foundations.html][related_post_a252_rl_foundations]
- Sechter, Brendan. 2025. "Machines That Learn From Experience: Deep Reinforcement Learning." *Brendan A R Sechter's Development Blog*, December 21. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/21/machines\_that\_learn\_from\_experience\_deep\_reinforcement\_learning.html][related_post_a253_deep_rl]
- Sechter, Brendan. 2025. "Machines That Learn From Experience: Exploration, Intrinsic Motivation, and Curiosity." *Brendan A R Sechter's Development Blog*, December 22. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/22/machines\_that\_learn\_from\_experience\_exploration\_intrinsic\_motivation\_and\_curiosity.html][related_post_a254_exploration]
- Sechter, Brendan. 2025. "Machines That Learn From Experience: Hierarchical Reinforcement Learning." *Brendan A R Sechter's Development Blog*, December 23. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/23/machines\_that\_learn\_from\_experience\_hierarchical\_reinforcement\_learning.html][related_post_a255_hierarchical]
- Sechter, Brendan. 2025. "Machines That Learn From Experience: World Models and Predictive, Model-Based Adaptation." *Brendan A R Sechter's Development Blog*, December 24. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/24/machines\_that\_learn\_from\_experience\_world\_models\_and\_predictive\_model\_based\_adaptation.html][related_post_a256_world_models]
- Sechter, Brendan. 2025. "Machines That Learn From Experience: Offline and Batch Reinforcement Learning." *Brendan A R Sechter's Development Blog*, December 25. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/25/machines\_that\_learn\_from\_experience\_offline\_and\_batch\_reinforcement\_learning.html][related_post_a257_offline]
- Sechter, Brendan. 2025. "Machines That Learn From Experience: Meta-Learning and Online Adaptation." *Brendan A R Sechter's Development Blog*, December 26. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/26/machines\_that\_learn\_from\_experience\_meta\_learning\_and\_online\_adaptation.html][related_post_a258_meta_learning]
- Sechter, Brendan. 2025. "Machines That Learn From Experience: Continual and Lifelong Learning." *Brendan A R Sechter's Development Blog*, December 27. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/27/machines\_that\_learn\_from\_experience\_continual\_and\_lifelong\_learning.html][related_post_a259_continual]
- Sechter, Brendan. 2025. "Machines That Learn From Experience: Learning From Demonstration, Preference, and Other Agents." *Brendan A R Sechter's Development Blog*, December 28. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/28/machines\_that\_learn\_from\_experience\_learning\_from\_demonstration\_preference\_and\_other\_agents.html][related_post_a260_demonstration]
- Sechter, Brendan. 2025. "Machines That Learn From Experience: Evolutionary and Open-Ended Adaptation." *Brendan A R Sechter's Development Blog*, December 29. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/29/machines\_that\_learn\_from\_experience\_evolutionary\_and\_open\_ended\_adaptation.html][related_post_a261_evolutionary]
- Sechter, Brendan. 2025. "Machines That Learn From Experience: Embodied Cognition and Developmental Learning." *Brendan A R Sechter's Development Blog*, December 30. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/30/machines\_that\_learn\_from\_experience\_embodied\_cognition\_and\_developmental\_learning.html][related_post_a262_embodied]
- Sechter, Brendan. 2025. "Machines That Learn From Experience: NeuroAI, What Neuroscience and Machine Learning Took From Each Other." *Brendan A R Sechter's Development Blog*, December 31. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/31/machines\_that\_learn\_from\_experience\_neuroai.html][related_post_a263_neuroai]
- Sechter, Brendan. 2026. "Machines That Learn From Experience: From Conditioning to Computation, the Psychology of Learning." *Brendan A R Sechter's Development Blog*, January 1. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2026/01/01/machines\_that\_learn\_from\_experience\_psychology\_of\_learning.html][related_post_a264_psychology]

[book_bellman_1957]: https://press.princeton.edu/books/paperback/9780691146683/dynamic-programming
[book_bertsekas_tsitsiklis_1996]: http://www.athenasc.com/ndpbook.html
[book_ebbinghaus_1885]: https://www.taylorfrancis.com/books/mono/10.4324/9781315802749/memory-hermann-ebbinghaus
[book_howard_1960]: https://mitpress.mit.edu/9780262080095/dynamic-programming-and-markov-processes/
[book_kahneman_2011]: https://us.macmillan.com/books/9780374533557/thinkingfastandslow
[book_pfeifer_bongard_2007]: https://mitpress.mit.edu/9780262162395/how-the-body-shapes-the-way-we-think/
[book_russell_norvig_2020]: https://aima.cs.berkeley.edu/
[book_sutton_barto_2018]: http://incompleteideas.net/book/the-book-2nd.html
[ref_berkeley_cs285]: https://rail.eecs.berkeley.edu/deeprlcourse/
[ref_deepmind_ucl_rl]: https://www.deepmind.com/learning-resources/reinforcement-learning-lecture-series-2021
[ref_openai_spinning_up]: https://spinningup.openai.com/
[ref_silver_rl_course]: https://www.davidsilver.uk/teaching/
[ref_stanford_cs234]: https://web.stanford.edu/class/cs234/
[related_post_a250_framing]: {% post_url 2025-12-18-machines_that_learn_from_experience_framing %}
[related_post_a251_bandits]: {% post_url 2025-12-19-machines_that_learn_from_experience_bandits_and_online_learning %}
[related_post_a252_rl_foundations]: {% post_url 2025-12-20-machines_that_learn_from_experience_reinforcement_learning_foundations %}
[related_post_a253_deep_rl]: {% post_url 2025-12-21-machines_that_learn_from_experience_deep_reinforcement_learning %}
[related_post_a254_exploration]: {% post_url 2025-12-22-machines_that_learn_from_experience_exploration_intrinsic_motivation_and_curiosity %}
[related_post_a255_hierarchical]: {% post_url 2025-12-23-machines_that_learn_from_experience_hierarchical_reinforcement_learning %}
[related_post_a256_world_models]: {% post_url 2025-12-24-machines_that_learn_from_experience_world_models_and_predictive_model_based_adaptation %}
[related_post_a257_offline]: {% post_url 2025-12-25-machines_that_learn_from_experience_offline_and_batch_reinforcement_learning %}
[related_post_a258_meta_learning]: {% post_url 2025-12-26-machines_that_learn_from_experience_meta_learning_and_online_adaptation %}
[related_post_a259_continual]: {% post_url 2025-12-27-machines_that_learn_from_experience_continual_and_lifelong_learning %}
[related_post_a260_demonstration]: {% post_url 2025-12-28-machines_that_learn_from_experience_learning_from_demonstration_preference_and_other_agents %}
[related_post_a261_evolutionary]: {% post_url 2025-12-29-machines_that_learn_from_experience_evolutionary_and_open_ended_adaptation %}
[related_post_a262_embodied]: {% post_url 2025-12-30-machines_that_learn_from_experience_embodied_cognition_and_developmental_learning %}
[related_post_a263_neuroai]: {% post_url 2025-12-31-machines_that_learn_from_experience_neuroai %}
[related_post_a264_psychology]: {% post_url 2026-01-01-machines_that_learn_from_experience_psychology_of_learning %}
[research_abbeel_ng_2004]: https://doi.org/10.1145/1015330.1015430
[research_amodei_et_al_2016]: https://doi.org/10.48550/arxiv.1606.06565
[research_auer_cesa_bianchi_fischer_2002]: https://doi.org/10.1023/a:1013689704352
[research_bacon_harb_precup_2017]: https://doi.org/10.1609/aaai.v31i1.10916
[research_bai_et_al_2022]: https://doi.org/10.48550/arxiv.2212.08073
[research_baird_1995]: https://doi.org/10.1016/b978-1-55860-377-6.50013-x
[research_bellemare_dabney_munos_2017]: https://proceedings.mlr.press/v70/bellemare17a.html
[research_bellemare_et_al_2013]: https://doi.org/10.1613/jair.3912
[research_bellemare_et_al_2016]: https://papers.nips.cc/paper/2016/hash/afda332245e2af431fb7b672a68b659d-Abstract.html
[research_bengio_et_al_2009]: https://doi.org/10.1145/1553374.1553380
[research_berner_et_al_2019]: https://doi.org/10.48550/arxiv.1912.06680
[research_bommasani_et_al_2021]: https://doi.org/10.48550/arxiv.2108.07258
[research_brown_et_al_2020]: https://papers.nips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html
[research_brown_sandholm_2018]: https://doi.org/10.1126/science.aao1733
[research_casper_et_al_2023]: https://doi.org/10.48550/arxiv.2307.15217
[research_cepeda_et_al_2008]: https://doi.org/10.1111/j.1467-9280.2008.02209.x
[research_chaudhry_et_al_2019]: https://doi.org/10.48550/arxiv.1812.00420
[research_christiano_et_al_2017]: https://papers.nips.cc/paper/2017/hash/d5e2c0adad503c91f91df240d0cd4e49-Abstract.html
[research_christiano_shlegeris_amodei_2018]: https://doi.org/10.48550/arxiv.1810.08575
[research_cobbe_et_al_2020]: https://proceedings.mlr.press/v119/cobbe20a.html
[research_crick_1989]: https://doi.org/10.1038/337129a0
[research_dabney_et_al_2018_iqn]: https://proceedings.mlr.press/v80/dabney18a.html
[research_dabney_et_al_2018_qr_dqn]: https://doi.org/10.1609/aaai.v32i1.11791
[research_daw_niv_dayan_2005]: https://doi.org/10.1038/nn1560
[research_dayan_1993]: https://direct.mit.edu/neco/article-abstract/5/4/613/5786
[research_dayan_hinton_1993]: https://papers.nips.cc/paper/1992/hash/d14220ee66aeec73c49038385428ec4c-Abstract.html
[research_deisenroth_rasmussen_2011]: https://dl.acm.org/doi/10.5555/3104482.3104541
[research_dietterich_2000]: https://doi.org/10.1613/jair.639
[research_duan_et_al_2016]: https://doi.org/10.48550/arxiv.1611.02779
[research_finn_abbeel_levine_2017]: https://proceedings.mlr.press/v70/finn17a.html
[research_foster_wilson_2006]: https://doi.org/10.1038/nature04587
[research_friston_2010]: https://doi.org/10.1038/nrn2787
[research_fujimoto_hoof_meger_2018]: https://proceedings.mlr.press/v80/fujimoto18a.html
[research_fujimoto_meger_precup_2019]: https://proceedings.mlr.press/v97/fujimoto19a.html
[research_gao_schulman_hilton_2023]: https://proceedings.mlr.press/v202/gao23h.html
[research_ha_schmidhuber_2018]: https://papers.nips.cc/paper/2018/hash/2de5d16682c3c35007e4e92982f1a2ba-Abstract.html
[research_haarnoja_et_al_2018]: https://proceedings.mlr.press/v80/haarnoja18b.html
[research_hafner_et_al_2020]: https://doi.org/10.48550/arxiv.1912.01603
[research_hafner_et_al_2023]: https://doi.org/10.48550/arxiv.2301.04104
[research_hafting_et_al_2005]: https://doi.org/10.1038/nature03721
[research_henderson_et_al_2018]: https://doi.org/10.1609/aaai.v32i1.11694
[research_ho_ermon_2016]: https://papers.nips.cc/paper/2016/hash/cc7e2b878868cbae992d1fb743995d8f-Abstract.html
[research_hoffmann_et_al_2022]: https://doi.org/10.48550/arxiv.2203.15556
[research_houthooft_et_al_2016]: https://papers.nips.cc/paper_files/paper/2016/hash/abd815286ba1007abfbb8415b83ae2cf-Abstract.html
[research_hubinger_et_al_2019]: https://doi.org/10.48550/arxiv.1906.01820
[research_irving_christiano_amodei_2018]: https://doi.org/10.48550/arxiv.1805.00899
[research_jumper_et_al_2021]: https://doi.org/10.1038/s41586-021-03819-2
[research_kahneman_tversky_1979]: https://doi.org/10.2307/1914185
[research_kakade_2003]: https://homepages.inf.ed.ac.uk/csutton/publications/kakade-thesis.pdf
[research_kaplan_et_al_2020]: https://doi.org/10.48550/arxiv.2001.08361
[research_kemp_tenenbaum_2008]: https://doi.org/10.1073/pnas.0802631105
[research_khaligh_razavi_kriegeskorte_2014]: https://doi.org/10.1371/journal.pcbi.1003915
[research_kirkpatrick_et_al_2017]: https://doi.org/10.1073/pnas.1611835114
[research_klyubin_polani_nehaniv_2005]: https://doi.org/10.1109/cec.2005.1554676
[research_kostrikov_nair_levine_2022]: https://doi.org/10.48550/arxiv.2110.06169
[research_krakovna_et_al_2020]: https://deepmind.google/discover/blog/specification-gaming-the-flip-side-of-ai-ingenuity/
[research_kriegeskorte_mur_bandettini_2008]: https://doi.org/10.3389/neuro.06.004.2008
[research_kumar_et_al_2020]: https://papers.nips.cc/paper/2020/hash/0d2b2061826a5df3221116a5085a6052-Abstract.html
[research_kumaran_mcclelland_hassabis_2016]: https://doi.org/10.1016/j.tics.2016.05.004
[research_kuttler_et_al_2020]: https://papers.nips.cc/paper/2020/hash/569ff987c643b4bedf504efda8f786c2-Abstract.html
[research_lai_robbins_1985]: https://doi.org/10.1016/0196-8858(85)90002-8
[research_lazic_et_al_2018]: https://papers.nips.cc/paper/2018/hash/059fdcd96baeb75112f09fa1dcc740cc-Abstract.html
[research_lee_zhang_fischer_bengio_2015]: https://doi.org/10.1007/978-3-319-23528-8_31
[research_lehman_stanley_2011]: https://doi.org/10.1007/978-1-4614-1770-5_3
[research_levine_et_al_2020]: https://doi.org/10.48550/arxiv.2005.01643
[research_lillicrap_et_al_2015]: https://doi.org/10.48550/arxiv.1509.02971
[research_lillicrap_et_al_2016]: https://doi.org/10.1038/ncomms13276
[research_lillicrap_et_al_2020]: https://doi.org/10.1038/s41583-020-0277-3
[research_lin_1992]: https://doi.org/10.1007/bf00992699
[research_lopez_paz_ranzato_2017]: https://papers.nips.cc/paper/2017/hash/f87522788a2be2d171666752f97ddebb-Abstract.html
[research_manheim_garrabrant_2018]: https://doi.org/10.48550/arxiv.1803.04585
[research_mcclelland_mcnaughton_oreilly_1995]: https://doi.org/10.1037/0033-295x.102.3.419
[research_mirhoseini_et_al_2021]: https://doi.org/10.1038/s41586-021-03544-w
[research_mnih_et_al_2015]: https://doi.org/10.1038/nature14236
[research_mnih_et_al_2016]: https://proceedings.mlr.press/v48/mniha16.html
[research_moravcik_et_al_2017]: https://doi.org/10.1126/science.aam6960
[research_mouret_clune_2015]: https://doi.org/10.48550/arxiv.1504.04909
[research_ng_russell_2000]: https://ai.stanford.edu/~ang/papers/icml00-irl.pdf
[research_ngo_chan_mindermann_2022]: https://doi.org/10.48550/arxiv.2209.00626
[research_nosofsky_1986]: https://doi.org/10.1037/0096-3445.115.1.39
[research_okeefe_dostrovsky_1971]: https://doi.org/10.1016/0006-8993(71)90358-1
[research_openended_team_2021]: https://scholar.google.com/scholar?q=XLand+Open-Ended+Team+2021
[research_oregan_noe_2001]: https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/sensorimotor-account-of-vision-and-visual-consciousness/1B49A6F4EA76ECBD0938815EEE18C7DC
[research_osband_et_al_2020]: https://openreview.net/forum?id=rygf-kSYwH
[research_osc_2015]: https://www.science.org/doi/10.1126/science.aac4716
[research_ouyang_et_al_2022]: https://doi.org/10.52202/068431-2011
[research_pathak_et_al_2017]: https://doi.org/10.1109/cvprw.2017.70
[research_rao_ballard_1999]: https://doi.org/10.1038/4580
[research_rescorla_wagner_1972]: https://scholar.google.com/scholar?q=rescorla+wagner+1972+theory+pavlovian+conditioning
[research_roediger_karpicke_2006]: https://doi.org/10.1111/j.1467-9280.2006.01693.x
[research_rosch_1975]: https://doi.org/10.1037/0096-3445.104.3.192
[research_roy_duckett_2022]: https://scholar.google.com/scholar?q=Reward+is+Enough+Critique+Roy+Duckett+2022
[research_rummery_niranjan_1994]: https://www.researchgate.net/publication/2500611_On-Line_Q-Learning_Using_Connectionist_Systems
[research_rusu_et_al_2016]: https://doi.org/10.48550/arxiv.1606.04671
[research_salimans_et_al_2017]: https://doi.org/10.48550/arxiv.1703.03864
[research_schrimpf_et_al_2020]: https://doi.org/10.1016/j.neuron.2020.07.040
[research_schrittwieser_et_al_2020]: https://doi.org/10.1038/s41586-020-03051-4
[research_schulman_et_al_2015]: https://proceedings.mlr.press/v37/schulman15.html
[research_schulman_et_al_2017]: https://doi.org/10.48550/arxiv.1707.06347
[research_schultz_dayan_montague_1997]: https://doi.org/10.1126/science.275.5306.1593
[research_shin_et_al_2017]: https://papers.nips.cc/paper/2017/hash/0efbe98067c6c73dba1250d2beaa81f9-Abstract.html
[research_silver_et_al_2014]: https://proceedings.mlr.press/v32/silver14.html
[research_silver_et_al_2016]: https://doi.org/10.1038/nature16961
[research_silver_et_al_2017]: https://doi.org/10.1038/nature24270
[research_silver_et_al_2018]: https://doi.org/10.1126/science.aar6404
[research_silver_et_al_2021]: https://doi.org/10.1016/j.artint.2021.103535
[research_silver_sutton_2024]: https://storage.googleapis.com/deepmind-media/Era-of-Experience%20/The%20Era%20of%20Experience%20Paper.pdf
[research_stachenfeld_botvinick_gershman_2017]: https://doi.org/10.1038/nn.4650
[research_stanley_miikkulainen_2002]: https://direct.mit.edu/evco/article/10/2/99/1123
[research_stiennon_et_al_2020]: https://papers.nips.cc/paper/2020/hash/1f89885d556929e98d3ef9b86448f951-Abstract.html
[research_strehl_li_littman_2009]: https://jmlr.org/papers/v10/strehl09a.html
[research_sutton_1988]: https://doi.org/10.1007/bf00115009
[research_sutton_1991]: https://doi.org/10.1145/122344.122377
[research_sutton_2019_bitter_lesson]: http://www.incompleteideas.net/IncIdeas/BitterLesson.html
[research_sutton_et_al_2000]: https://papers.nips.cc/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html
[research_sutton_precup_singh_1999]: https://doi.org/10.1016/s0004-3702(99)00052-1
[research_tenenbaum_et_al_2011]: https://doi.org/10.1126/science.1192788
[research_thompson_1933]: https://www.jstor.org/stable/2332286
[research_todorov_erez_tassa_2012]: https://doi.org/10.1109/iros.2012.6386109
[research_turner_et_al_2021]: https://papers.nips.cc/paper/2021/hash/c26820b8a4c1b3c2aa868d6d57e14a79-Abstract.html
[research_van_hasselt_et_al_2018]: https://doi.org/10.48550/arxiv.1812.02648
[research_van_hasselt_guez_silver_2016]: https://scholar.google.com/scholar?q=Double+DQN+Van+Hasselt+Guez+2016
[research_van_seijen_et_al_2009]: https://ieeexplore.ieee.org/document/4927542
[research_vezhnevets_et_al_2017]: https://proceedings.mlr.press/v70/vezhnevets17a.html
[research_vinyals_et_al_2019]: https://doi.org/10.1038/s41586-019-1724-z
[research_wang_et_al_2016]: https://doi.org/10.48550/arxiv.1611.05763
[research_wang_et_al_2016_dueling]: https://proceedings.mlr.press/v48/wangf16.html
[research_wang_lehman_clune_stanley_2019]: https://doi.org/10.48550/arxiv.1901.01753
[research_watkins_1989]: https://www.cs.rhul.ac.uk/~chrisw/new_thesis.pdf
[research_watkins_dayan_1992]: https://doi.org/10.1007/bf00992698
[research_wei_et_al_2022_cot]: https://doi.org/10.52202/068431-1800
[research_wei_et_al_2022_emergent]: https://openreview.net/forum?id=yzkSU5zdwD
[research_weng_et_al_2001]: https://doi.org/10.1126/science.291.5504.599
[research_whittington_bogacz_2017]: https://direct.mit.edu/neco/article-abstract/29/5/1229/8261
[research_williams_1992]: https://doi.org/10.1007/bf00992696
[research_wilson_mcnaughton_1994]: https://doi.org/10.1126/science.8036517
[research_yamins_et_al_2014]: https://doi.org/10.1073/pnas.1403112111
[research_yu_et_al_2020]: https://proceedings.mlr.press/v100/yu20a.html
[research_zador_et_al_2023]: https://doi.org/10.1038/s41467-023-37180-x
[research_ziebart_et_al_2008]: https://cdn.aaai.org/AAAI/2008/AAAI08-227.pdf
