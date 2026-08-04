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

$$B_{t+1} = B_t + \eta \, \Delta(B_t, E_t)$$

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

$$\mathcal{M} = (\mathcal{S}, \mathcal{A}, P, R, \gamma, \mu_0)$$

specifies the state space, action space, transition kernel, reward function, discount factor, and initial state distribution. The treatment organizes the mathematical treatment of experiential learning and continues to provide the canonical vocabulary for the field. The formal apparatus allows several standard extensions including the partially observable Markov decision process, the semi-Markov decision process, the constrained Markov decision process, and the multi-agent Markov game. Each extension has been substantially formalized and continues to organize modern research.

The agent's objective is formalized through the discounted return

$$G_t = \sum_{k=0}^\infty \gamma^k r_{t+k+1}$$

with $\gamma \in [0, 1)$ trading off immediate against delayed reward. The policy $\pi(a \mid s)$ induces a distribution over trajectories $\tau = (s_0, a_0, r_1, s_1, a_1, \ldots)$ specified by

$$p_\pi(\tau) = \mu_0(s_0) \prod_{t=0}^\infty \pi(a_t \mid s_t) \, P(s_{t+1} \mid s_t, a_t)$$

and the state-occupancy measure

$$d^\pi(s) = (1 - \gamma) \sum_{t=0}^\infty \gamma^t \, \Pr_\pi(s_t = s)$$

which appears in the policy-gradient theorem and the offline-reinforcement-learning distributional-shift literature.

The value function and Bellman recursion of [Bellman 1957][book_bellman_1957] provide the dynamic-programming foundation. The state-value function

$$V^\pi(s) = \mathbb{E}_\pi \left[ \sum_{t=0}^\infty \gamma^t r_{t+1} \mid s_0 = s \right]$$

and its Bellman recursion

$$V^\pi(s) = \sum_a \pi(a \mid s) \sum_{s'} P(s' \mid s, a) \left[ R(s, a, s') + \gamma V^\pi(s') \right]$$

provide the fixed-point characterization that continues to organize the algorithmic treatment. The action-value function

$$Q^\pi(s, a) = \mathbb{E}_\pi \left[ \sum_{t=0}^\infty \gamma^t r_{t+1} \mid s_0 = s, a_0 = a \right]$$

and the advantage function

$$A^\pi(s, a) = Q^\pi(s, a) - V^\pi(s)$$

provide the action-conditioned refinements that organize the policy-improvement and variance-reduction literatures. The optimal Bellman equation

$$V^*(s) = \max_a \sum_{s'} P(s' \mid s, a) \left[ R(s, a, s') + \gamma V^*(s') \right]$$

specifies the fixed-point characterization of the optimal value function. The corresponding optimal action-value function satisfies

$$Q^*(s, a) = \sum_{s'} P(s' \mid s, a) \left[ R(s, a, s') + \gamma \max_{a'} Q^*(s', a') \right]$$

This account has been markedly extended through subsequent work but continues to provide the mathematical foundation for the field.

Under partial observability the belief-state update

$$b_{t+1}(s') = \frac{O(o_{t+1} \mid s') \sum_s P(s' \mid s, a_t) \, b_t(s)}{\sum_{s''} O(o_{t+1} \mid s'') \sum_s P(s'' \mid s, a_t) \, b_t(s)}$$

provides the sufficient-statistic-of-history that permits the partially-observable Markov decision process to be recast as a fully-observable Markov decision process over belief states. The framework has been appreciably characterized and continues to provide the formal foundation for the partial-observability literature.

The temporal-difference error of [Sutton 1988][research_sutton_1988] provides the model-free foundation. The update

$$\delta_t = r_{t+1} + \gamma V(s_{t+1}) - V(s_t)$$

specifies the prediction-error signal that drives the temporal-difference learning update

$$V(s_t) \leftarrow V(s_t) + \alpha \delta_t$$

The account provides the model-free alternative to the model-based Bellman-recursion approach and continues to organize extensive modern research.

The Q-learning update of [Watkins 1989][research_watkins_1989] provides the control-side alternative. The update

$$Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha \left[ r_{t+1} + \gamma \max_a Q(s_{t+1}, a) - Q(s_t, a_t) \right]$$

specifies the off-policy update that provides the convergence guarantees under tabular conditions. The model continues to organize sizable modern research and provides the foundation for deep Q-network approaches.

The policy gradient theorem of [Williams 1992][research_williams_1992] and [Sutton McAllester Singh Mansour 2000][research_sutton_et_al_2000] provides the direct-policy-optimization foundation. The gradient

$$\nabla_\theta J(\theta) = \mathbb{E}_{\pi_\theta} \left[ \sum_t \nabla_\theta \log \pi_\theta(a_t \mid s_t) \, Q^{\pi_\theta}(s_t, a_t) \right]$$

provides the unbiased gradient estimator that continues to organize the direct-policy-optimization literature. This formulation has been greatly refined through variance-reduction techniques including baselines, advantage estimators, and trust-region methods.

The Rescorla-Wagner model of [Rescorla and Wagner 1972][research_rescorla_wagner_1972] provides the psychological correspondence. The associative-strength update

$$\Delta V_i = \alpha_i \beta \left( \lambda - \sum_j V_j \right)$$

specifies the prediction-error-driven learning rule that continues to organize the associative-learning literature. The formal correspondence to temporal-difference learning provides the bridge between psychology and machine learning that continues to organize appreciable modern research.

The regret decomposition of [Lai and Robbins 1985][research_lai_robbins_1985] provides the bandit-and-online-learning foundation. The regret bound

$$R_T \geq \sum_{a: \Delta_a > 0} \frac{\log T}{D_{KL}(P_a \| P_{a^*})} \, \Delta_a + o(\log T)$$

specifies the fundamental lower bound on cumulative regret that continues to organize the bandit and online-learning literature. The treatment has been considerably extended through subsequent work and continues to provide the formal foundation for the field.

These foundational formal objects constitute the settled public domain of the field. Any competent researcher is expected to command the formalisms, and the algorithmic and empirical developments of the subsequent articles rest on these foundations.

## The Established Algorithmic Toolkit

The established algorithmic toolkit of experiential learning consolidates the corpus of algorithms whose formal statement, empirical support, and reproducibility permit independent verification. This account provides the canonical algorithms that appear in modern textbooks and open-source implementations.

Bandits and online learning of [A251 Bandits and Online Learning][related_post_a251_bandits] contribute the upper-confidence-bound algorithm of [Auer Cesa-Bianchi Fischer 2002][research_auer_cesa_bianchi_fischer_2002] with its action-selection rule

$$a_t = \arg\max_a \left[ \hat{\mu}_a + \sqrt{\frac{2 \log t}{N_a(t)}} \right]$$

and its regret bound of order $O(\sqrt{T \log T})$, Thompson sampling of [Thompson 1933][research_thompson_1933] with the posterior-sampling rule

$$\theta_t \sim p(\theta \mid \mathcal{D}_{t-1}), \quad a_t = \arg\max_a \mathbb{E}[r \mid a, \theta_t]$$

and its Bayesian-optimal regret properties, the exponential-weights algorithm for the adversarial setting, and the extensions to contextual bandits including LinUCB and neural contextual bandits. The framework provides the pre-Markov-decision-process foundation for the field.

Reinforcement learning foundations of [A252 Reinforcement Learning Foundations][related_post_a252_rl_foundations] contribute the classical algorithms including value iteration and policy iteration of [Howard 1960][book_howard_1960], Monte Carlo methods, SARSA of [Rummery and Niranjan 1994][research_rummery_niranjan_1994], Q-learning of [Watkins 1989][research_watkins_1989], expected SARSA of [Van Seijen et al 2009][research_van_seijen_et_al_2009], and the eligibility-trace variants including TD($\lambda$) of [Sutton 1988][research_sutton_1988] and Watkins's Q($\lambda$) of [Watkins and Dayan 1992][research_watkins_dayan_1992]. The account provides the canonical algorithms whose convergence properties have been significantly characterized under tabular and linear function approximation conditions.

Deep reinforcement learning of [A253 Deep Reinforcement Learning][related_post_a253_deep_rl] contributes the canonical algorithms including deep Q-networks of [Mnih et al 2015][research_mnih_et_al_2015] with the target-network loss

$$\mathcal{L}(\theta) = \mathbb{E}_{(s, a, r, s') \sim \mathcal{D}} \left[ \left( r + \gamma \max_{a'} Q_{\theta^-}(s', a') - Q_\theta(s, a) \right)^2 \right]$$

the double DQN of [Van Hasselt Guez Silver 2016][research_van_hasselt_guez_silver_2016] and dueling DQN of [Wang et al 2016 Dueling][research_wang_et_al_2016_dueling] refinements, the policy-gradient methods including asynchronous advantage actor-critic of [Mnih et al 2016][research_mnih_et_al_2016], trust region policy optimization of [Schulman et al 2015][research_schulman_et_al_2015], and proximal policy optimization of [Schulman et al 2017][research_schulman_et_al_2017] with the clipped surrogate objective

$$\mathcal{L}^{\text{CLIP}}(\theta) = \mathbb{E}_t \left[ \min \left( \rho_t(\theta) \hat{A}_t, \, \text{clip}(\rho_t(\theta), 1 - \epsilon, 1 + \epsilon) \hat{A}_t \right) \right]$$

with $\rho_t(\theta) = \pi_\theta(a_t \mid s_t) / \pi_{\theta_{\text{old}}}(a_t \mid s_t)$, the deterministic-policy-gradient family including the [Silver et al 2014][research_silver_et_al_2014] deterministic policy gradient theorem, DDPG of [Lillicrap et al 2015][research_lillicrap_et_al_2015] and TD3 of [Fujimoto Hoof Meger 2018][research_fujimoto_hoof_meger_2018], the maximum-entropy family including soft actor-critic of [Haarnoja et al 2018][research_haarnoja_et_al_2018] with the entropy-regularized objective

$$J(\pi) = \sum_t \mathbb{E}_{(s_t, a_t) \sim \pi} \left[ r(s_t, a_t) + \alpha \mathcal{H}(\pi(\cdot \mid s_t)) \right]$$

the distributional reinforcement learning framework of [Bellemare Dabney Munos 2017][research_bellemare_dabney_munos_2017] that learns the distribution of the discounted return rather than only its expectation and induces the categorical DQN and quantile-regression DQN of [Dabney et al 2018][research_dabney_et_al_2018_qr_dqn] and the implicit quantile network of [Dabney et al 2018][research_dabney_et_al_2018_iqn], and the self-play framework including AlphaGo of [Silver et al 2016][research_silver_et_al_2016], AlphaZero of [Silver et al 2017][research_silver_et_al_2017] and its journal treatment in [Silver et al 2018][research_silver_et_al_2018], and MuZero of [Schrittwieser et al 2020][research_schrittwieser_et_al_2020] that extends the framework to unknown dynamics. The model provides the canonical algorithms that continue to organize modern deep reinforcement learning research.

Exploration, intrinsic motivation, and curiosity of [A254 Exploration Intrinsic Motivation and Curiosity][related_post_a254_exploration] contribute the count-based and pseudocount exploration frameworks including [Bellemare et al 2016][research_bellemare_et_al_2016] with the exploration-bonus reward

$$r^+_t = r_t + \frac{\beta}{\sqrt{\hat{N}(s_t)}}$$

the prediction-error curiosity of [Pathak et al 2017][research_pathak_et_al_2017] with the intrinsic reward

$$r^i_t = \eta \left\| \hat{\phi}(s_{t+1}) - \phi(s_{t+1}) \right\|_2^2$$

the empowerment framework of [Klyubin Polani Nehaniv 2005][research_klyubin_polani_nehaniv_2005] with the channel-capacity objective

$$\mathfrak{E}(s) = \max_{\omega} I(A_t^n; S_{t+n} \mid s_t = s)$$

and the information-gain frameworks including the [Houthooft et al 2016][research_houthooft_et_al_2016] variational-information-maximizing exploration framework. The treatment provides the canonical exploration methods that continue to organize modern research on hard-exploration problems.

Hierarchical reinforcement learning of [A255 Hierarchical Reinforcement Learning][related_post_a255_hierarchical] contributes the options framework of [Sutton Precup Singh 1999][research_sutton_precup_singh_1999] with the option tuple

$$o = \langle \mathcal{I}_o, \pi_o, \beta_o \rangle$$

comprising an initiation set, an intra-option policy, and a termination condition, and inducing the semi-Markov decision process value function

$$V^\mu(s) = \sum_o \mu(o \mid s) \left[ \sum_{k=1}^\infty \gamma^{k-1} \mathbb{E}[r_{t+k} \mid s, o] + \gamma^k \mathbb{E}[V^\mu(s_{t+k}) \mid s, o] \right]$$

the MAXQ decomposition of [Dietterich 2000][research_dietterich_2000], the feudal networks framework of [Dayan and Hinton 1993][research_dayan_hinton_1993] and its modern extension in [Vezhnevets et al 2017][research_vezhnevets_et_al_2017], and the option-critic hierarchical actor-critic method of [Bacon Harb Precup 2017][research_bacon_harb_precup_2017]. This account provides the canonical hierarchical algorithms that continue to organize modern research on temporally-extended action.

World models and predictive model-based adaptation of [A256 World Models and Predictive Model-Based Adaptation][related_post_a256_world_models] contribute the model-based reinforcement learning algorithms including Dyna of [Sutton 1991][research_sutton_1991] with the interleaved update

$$\hat{P}, \hat{R} \leftarrow \text{Learn}(\mathcal{D}); \quad Q \leftarrow Q + \alpha \left[ r + \gamma \max_{a'} Q(s', a') - Q(s, a) \right] \text{ on both real and simulated experience}$$

the PILCO framework of [Deisenroth and Rasmussen 2011][research_deisenroth_rasmussen_2011], the world-model architecture of [Ha and Schmidhuber 2018][research_ha_schmidhuber_2018] with a latent-dynamics model $z_{t+1} \sim p_\psi(z_{t+1} \mid z_t, a_t)$ trained jointly with an observation decoder $p_\phi(o_t \mid z_t)$, and the Dreamer family of algorithms of [Hafner et al 2020][research_hafner_et_al_2020] and [Hafner et al 2023][research_hafner_et_al_2023] that optimize policies through the differentiable rollout of learned latent dynamics. The framework provides the canonical model-based algorithms that continue to organize modern research on sample-efficient learning.

Offline and batch reinforcement learning of [A257 Offline and Batch Reinforcement Learning][related_post_a257_offline] contribute the canonical offline algorithms including batch-constrained Q-learning of [Fujimoto Meger Precup 2019][research_fujimoto_meger_precup_2019], conservative Q-learning of [Kumar et al 2020][research_kumar_et_al_2020] with the pessimistic penalty

$$\mathcal{L}_{\text{CQL}}(\theta) = \alpha \left[ \mathbb{E}_{s \sim \mathcal{D}} \log \sum_a \exp Q_\theta(s, a) - \mathbb{E}_{(s, a) \sim \mathcal{D}} Q_\theta(s, a) \right] + \mathcal{L}_{\text{TD}}(\theta)$$

behavior regularization methods with the policy-constraint objective

$$\pi = \arg\max_\pi \mathbb{E}_{s \sim \mathcal{D}, a \sim \pi} [Q(s, a)] - \lambda \, D(\pi \| \pi_\beta)$$

and the implicit Q-learning approach of [Kostrikov Nair Levine 2022][research_kostrikov_nair_levine_2022] that avoids querying out-of-distribution actions through expectile regression. The account provides the canonical offline algorithms that continue to organize modern research on learning from fixed datasets, and the [Levine et al 2020][research_levine_et_al_2020] tutorial provides the canonical survey.

Meta-learning and online adaptation of [A258 Meta-Learning and Online Adaptation][related_post_a258_meta_learning] contribute the canonical meta-learning algorithms including model-agnostic meta-learning of [Finn Abbeel Levine 2017][research_finn_abbeel_levine_2017] with the bi-level objective

$$\theta^* = \arg\min_\theta \sum_{\mathcal{T}_i \sim p(\mathcal{T})} \mathcal{L}_{\mathcal{T}_i} \left( \theta - \alpha \nabla_\theta \mathcal{L}_{\mathcal{T}_i}(\theta) \right)$$

the recurrent meta-reinforcement-learning approach of [Wang et al 2016][research_wang_et_al_2016] and [Duan et al 2016][research_duan_et_al_2016] in which the inner-loop learning dynamics are absorbed into a recurrent network's hidden-state update, and the in-context learning frameworks introduced by [Brown et al 2020][research_brown_et_al_2020] in which foundation models perform the implicit adaptation through attention over the context window. The model provides the canonical meta-learning algorithms that continue to organize modern research on fast adaptation.

Continual and lifelong learning of [A259 Continual and Lifelong Learning][related_post_a259_continual] contribute the canonical continual-learning algorithms including elastic weight consolidation of [Kirkpatrick et al 2017][research_kirkpatrick_et_al_2017] with the Fisher-information-weighted quadratic penalty

$$\mathcal{L}(\theta) = \mathcal{L}_B(\theta) + \sum_i \frac{\lambda}{2} F_i (\theta_i - \theta^*_{A, i})^2$$

progressive networks of [Rusu et al 2016][research_rusu_et_al_2016] that freeze prior-task parameters and add lateral adapters, the generative-replay framework of [Shin et al 2017][research_shin_et_al_2017] that uses a learned generator $p_\psi(x, y)$ to rehearse prior tasks, the gradient episodic memory framework of [Lopez-Paz and Ranzato 2017][research_lopez_paz_ranzato_2017], and the averaged gradient episodic memory extension of [Chaudhry et al 2019][research_chaudhry_et_al_2019]. This formulation provides the canonical continual-learning algorithms that continue to organize modern research on catastrophic forgetting.

Learning from demonstration, preference, and other agents of [A260 Learning From Demonstration Preference and Other Agents][related_post_a260_demonstration] contribute the canonical algorithms including behavior cloning with the maximum-likelihood objective

$$\pi_{\text{BC}} = \arg\max_\pi \mathbb{E}_{(s, a) \sim \mathcal{D}_E} \log \pi(a \mid s)$$

generative adversarial imitation learning of [Ho and Ermon 2016][research_ho_ermon_2016] with the minimax objective

$$\min_\pi \max_D \mathbb{E}_{\pi}[\log D(s, a)] + \mathbb{E}_{\pi_E}[\log(1 - D(s, a))] - \lambda \mathcal{H}(\pi)$$

maximum-entropy inverse reinforcement learning of [Ziebart et al 2008][research_ziebart_et_al_2008] with the trajectory-distribution model

$$p(\tau) \propto \exp\left( \sum_t r_\phi(s_t, a_t) \right)$$

preference-based reinforcement learning of [Christiano et al 2017][research_christiano_et_al_2017] with the Bradley-Terry preference model

$$P(\tau^1 \succ \tau^2) = \frac{\exp \sum_t \hat{r}_\phi(s^1_t, a^1_t)}{\exp \sum_t \hat{r}_\phi(s^1_t, a^1_t) + \exp \sum_t \hat{r}_\phi(s^2_t, a^2_t)}$$

and the reinforcement-learning-from-human-feedback pipelines of [Ouyang et al 2022][research_ouyang_et_al_2022] and [Stiennon et al 2020][research_stiennon_et_al_2020] that operationalize preference-learning at scale for language model alignment. The treatment provides the canonical algorithms that continue to organize modern research on learning from non-reward signals, and the [Ng and Russell 2000][research_ng_russell_2000] and [Abbeel and Ng 2004][research_abbeel_ng_2004] foundational papers establish the inverse-reinforcement-learning framework.

Evolutionary and open-ended adaptation of [A261 Evolutionary and Open-Ended Adaptation][related_post_a261_evolutionary] contribute the canonical algorithms including evolutionary strategies of [Salimans et al 2017][research_salimans_et_al_2017] with the natural-evolution-strategies gradient estimator

$$\nabla_\theta \mathbb{E}_{\epsilon \sim \mathcal{N}(0, I)} \left[ F(\theta + \sigma \epsilon) \right] = \frac{1}{\sigma} \mathbb{E}_\epsilon \left[ F(\theta + \sigma \epsilon) \, \epsilon \right]$$

neuroevolution of augmenting topologies of [Stanley and Miikkulainen 2002][research_stanley_miikkulainen_2002], the quality-diversity frameworks including MAP-Elites of [Mouret and Clune 2015][research_mouret_clune_2015] that maintain an archive $\mathcal{A}$ over a behavior grid so that each cell $c$ retains

$$\mathcal{A}[c] = \arg\max_{x \in \text{Cell}(c)} F(x)$$

the novelty-search framework of [Lehman and Stanley 2011][research_lehman_stanley_2011] that abandons the objective in favor of behavioral novelty, and the POET open-endedness framework of [Wang Lehman Clune Stanley 2019][research_wang_lehman_clune_stanley_2019] that co-evolves agents and environments. This account provides the canonical evolutionary algorithms that continue to organize modern research on population-based and open-ended learning.

Embodied cognition and developmental learning of [A262 Embodied Cognition and Developmental Learning][related_post_a262_embodied] contribute the canonical frameworks including sensorimotor contingency theory of [O'Regan and Noë 2001][research_oregan_noe_2001], morphological computation of [Pfeifer and Bongard 2007][book_pfeifer_bongard_2007], developmental robotics of [Weng et al 2001][research_weng_et_al_2001], and the curriculum-and-scaffolding frameworks of [Bengio et al 2009][research_bengio_et_al_2009]. The framework provides the canonical embodied-cognition frameworks that continue to organize modern research on physically-grounded learning.

The consolidated algorithmic toolkit constitutes the settled public domain of the field. Any competent researcher is expected to command the algorithms, and the applications and refinements of subsequent research consume these foundations.

## The Established Empirical Findings

The established empirical findings of experiential learning consolidate the corpus of empirical results whose replication has been substantially confirmed and whose scope of validity has been markedly characterized. The account provides the canonical empirical benchmarks against which subsequent research is evaluated.

The Atari 2600 benchmarks of [Bellemare et al 2013][research_bellemare_et_al_2013] provide the canonical single-agent reinforcement-learning benchmark. The findings including the deep Q-network human-level performance on the fifty-seven-game suite of [Mnih et al 2015][research_mnih_et_al_2015] have been appreciably replicated and continue to organize the benchmark evaluation of subsequent algorithms.

The MuJoCo continuous-control benchmarks of [Todorov Erez Tassa 2012][research_todorov_erez_tassa_2012] provide the canonical continuous-control benchmark. The findings including the proximal-policy-optimization performance and the soft-actor-critic performance have been greatly replicated and continue to organize the continuous-control literature.

The board game benchmarks of Go, chess, and shogi provide the canonical strategic-planning benchmarks. The findings including the AlphaGo and AlphaZero results have been considerably confirmed through subsequent research including the MuZero extension of [Schrittwieser et al 2020][research_schrittwieser_et_al_2020] to unknown-dynamics settings, and continue to organize the game-playing literature.

The dopamine reward-prediction-error finding of [Schultz Dayan Montague 1997][research_schultz_dayan_montague_1997] provides the canonical neuroscience-machine-learning correspondence. The findings have been significantly replicated across species, tasks, and recording modalities, and continue to organize the neuroscience-of-reinforcement-learning literature.

The hippocampal replay finding of [Wilson and McNaughton 1994][research_wilson_mcnaughton_1994] and its extension in [Foster and Wilson 2006][research_foster_wilson_2006] provides the canonical memory-consolidation correspondence to experience replay in machine learning as introduced in [Lin 1992][research_lin_1992] and deployed at scale in [Mnih et al 2015][research_mnih_et_al_2015]. The findings have been substantially replicated across species and tasks and continue to organize the hippocampal-machine-learning correspondence literature.

The complementary learning systems finding of [McClelland McNaughton O'Reilly 1995][research_mcclelland_mcnaughton_oreilly_1995] provides the canonical dual-memory-system correspondence. The findings have been markedly replicated and provide the bridge between the neuroscience of memory and the machine learning of continual learning.

The scaling laws of foundation models of [Kaplan et al 2020][research_kaplan_et_al_2020] and [Hoffmann et al 2022][research_hoffmann_et_al_2022] provide the empirical findings on the relationship between model size, compute, and performance. The Chinchilla-form parametric law

$$L(N, D) = \frac{A}{N^\alpha} + \frac{B}{D^\beta} + E$$

specifies the relationship between the model parameter count $N$, the training-token count $D$, and the achieved loss $L$, with $E$ the irreducible loss and $\alpha, \beta$ the exponents fit to the empirical data. The compute-optimal frontier

$$N^*(C) \propto C^a, \quad D^*(C) \propto C^b$$

specifies the allocation of a fixed compute budget $C$ across model size and data that minimizes the achieved loss. The findings have been appreciably replicated across model families and continue to organize the research on the scaling of foundation models. The applicability of scaling laws to interactive experiential learning remains greatly open and constitutes one of the open problems that this article surveys.

The Brain-Score benchmark of [Schrimpf et al 2020][research_schrimpf_et_al_2020] provides the canonical benchmark for comparing artificial neural networks to biological brains. The findings including the ranking of candidate models by their brain-score correspondence continue to organize the NeuroAI benchmarking literature.

The replication crisis findings in psychology of [Open Science Collaboration 2015][research_osc_2015] provide the empirical foundation for the modern methodological reforms in psychology. The findings including the approximately thirty-six percent replication rate for strict significance criteria continue to organize the methodological-reform literature.

The consolidated empirical findings constitute the settled public domain of the field. The benchmarks organize the evaluation of subsequent algorithms, and the empirical findings provide the constraints against which theoretical claims are evaluated.

## The Six-Axis Framework Revisited

The six-axis analytical framework introduced in [A250 Framing][related_post_a250_framing] provides the dimensional structure through which the subsequent articles have been organized. The model names six axes (signal, objective, structure, model, interaction, and adaptation) along which any experiential learning problem supports characterization. The present section recapitulates each axis, records the position along the axis at which each article's subject sits, and identifies the empirical loci along each axis at which the settled-versus-open partition currently rests.

The signal axis characterizes the form of the training information the learner receives. The axis positions include dense scalar reward, sparse scalar reward, preference between trajectories, demonstration of desired behavior, and intrinsic motivation computed from the learner's own predictions. The series treats each position through the corresponding articles. Dense and sparse reward are the default of [A252 Reinforcement Learning Foundations][related_post_a252_rl_foundations] and [A253 Deep Reinforcement Learning][related_post_a253_deep_rl]. Preference is the subject of [A260 Learning From Demonstration Preference and Other Agents][related_post_a260_demonstration] alongside demonstration and inverse reinforcement learning. Intrinsic motivation is the subject of [A254 Exploration Intrinsic Motivation and Curiosity][related_post_a254_exploration]. The settled public baseline on this axis identifies the canonical algorithms per signal type. The residual open problem is the characterization of when hybrid signals provide practical benefits over pure single-signal training.

The objective axis characterizes the quantity the learner optimizes. The axis positions include expected discounted return, long-run average reward, risk-sensitive objectives including conditional value at risk

$$\text{CVaR}_\alpha[G] = \mathbb{E}[G \mid G \leq q_\alpha(G)]$$

regret against a reference policy, distributional characteristics of return, and information-theoretic objectives including empowerment. The series treats each position through the corresponding articles. Discounted return is the default of [A252 Reinforcement Learning Foundations][related_post_a252_rl_foundations]. Regret is the subject of [A251 Bandits and Online Learning][related_post_a251_bandits]. Distributional characteristics are the subject of the distributional-reinforcement-learning framework of [Bellemare Dabney Munos 2017][research_bellemare_dabney_munos_2017] treated in [A253 Deep Reinforcement Learning][related_post_a253_deep_rl]. Information-theoretic objectives are the subject of [A254 Exploration Intrinsic Motivation and Curiosity][related_post_a254_exploration]. The settled public baseline identifies the canonical objectives and their algorithmic implementations. The residual open problem is the characterization of the correct objective under real-world safety and alignment constraints.

The structure axis characterizes the form of the environment the learner faces. The axis positions include the flat Markov decision process, the partially observable Markov decision process, the hierarchical decision process with options or sub-policies, the factored state space, the multi-agent stochastic game, and the partially observable stochastic game. The series treats each position through the corresponding articles. The flat Markov decision process is the default of [A252 Reinforcement Learning Foundations][related_post_a252_rl_foundations]. Hierarchical structure is the subject of [A255 Hierarchical Reinforcement Learning][related_post_a255_hierarchical]. Partial observability recurs throughout the series with treatment in the sensorimotor-contingency framework of [A262 Embodied Cognition and Developmental Learning][related_post_a262_embodied]. Multi-agent structure is the subject of the multi-agent extensions treated in [A260 Learning From Demonstration Preference and Other Agents][related_post_a260_demonstration]. The settled public baseline identifies the canonical formalisms per structure type. The residual open problem is the unified formal characterization of hierarchical decomposition under bounded computational resources.

The model axis characterizes the role of a learned environment model in the learning system. The axis positions include model-free (using only sample updates), model-based (learning an explicit generative model and planning with it), and model-implicit (using a learned representation that supports planning without an explicit generative model). The series treats each position through the corresponding articles. Model-free is the default of [A252 Reinforcement Learning Foundations][related_post_a252_rl_foundations] and [A253 Deep Reinforcement Learning][related_post_a253_deep_rl]. Model-based and model-implicit are the subject of [A256 World Models and Predictive Model-Based Adaptation][related_post_a256_world_models]. The correspondence between habitual model-free and goal-directed model-based behavior in animal learning is the subject of [A264 Psychology of Learning][related_post_a264_psychology] through the [Daw Niv Dayan 2005][research_daw_niv_dayan_2005] dual-system framework. The settled public baseline identifies the canonical algorithms per model type. The residual open problem is the optimal integration of model-free and model-based components under sample-complexity constraints.

The interaction axis characterizes the relationship between the learner's data source and the learner's policy. The axis positions include online interaction (collecting data from the environment as learning proceeds), offline learning (learning from a fixed prior dataset without further interaction), on-policy learning (using data collected under the current policy), and off-policy learning (using data collected under other policies). The series treats each position through the corresponding articles. Online on-policy is the default of many algorithms in [A252 Reinforcement Learning Foundations][related_post_a252_rl_foundations]. Off-policy learning is the subject of much of [A253 Deep Reinforcement Learning][related_post_a253_deep_rl] including the deep-Q-network family. Offline learning is the subject of [A257 Offline and Batch Reinforcement Learning][related_post_a257_offline]. The correspondence to human learning-from-demonstration is the subject of [A260 Learning From Demonstration Preference and Other Agents][related_post_a260_demonstration]. The settled public baseline identifies the canonical algorithms per interaction mode. The residual open problem is the characterization of when offline learning admits strong generalization guarantees beyond the coverage of the offline dataset.

The adaptation axis characterizes the temporal structure of the tasks the learner faces across its lifetime. The axis positions include stationary (a single fixed task), non-stationary (a task with drifting distribution), a task family requiring rapid adaptation for each new task, and an open-ended stream of tasks with no clear end. The series treats each position through the corresponding articles. Meta-learning across a task family is the subject of [A258 Meta-Learning and Online Adaptation][related_post_a258_meta_learning]. Continual and lifelong learning across a non-stationary stream is the subject of [A259 Continual and Lifelong Learning][related_post_a259_continual]. Open-ended adaptation is the subject of [A261 Evolutionary and Open-Ended Adaptation][related_post_a261_evolutionary]. Developmental adaptation across the lifespan is the subject of [A262 Embodied Cognition and Developmental Learning][related_post_a262_embodied]. The settled public baseline identifies the canonical algorithms per adaptation regime. The residual open problem is the formal characterization of open-endedness in the sense that human cultures and biological evolution exhibit.

The six-axis framework provides the analytical vocabulary through which any experiential learning problem permits characterization. This formulation's stability across the sixteen articles of the series provides evidence for its analytical power, and the correspondences between the axes and the algorithmic and empirical developments organize the research directions that this article surveys. The treatment also identifies the implicit dimensions along which the field has organized itself, and the residual open problems identified per axis constitute the research frontier at the closing of the editorial window.

## Established Neuroscience Correspondences

The established neuroscience correspondences consolidate the bidirectional exchanges between neuroscience and machine learning that have been considerably validated at the closing of the editorial window. This account was surveyed in detail in [A263 NeuroAI][related_post_a263_neuroai].

The dopamine reward-prediction-error correspondence of [Schultz Dayan Montague 1997][research_schultz_dayan_montague_1997] provides the paradigmatic correspondence. The finding that midbrain dopamine neurons encode a reward prediction error mathematically identical to the temporal-difference error

$$\text{DA firing rate at } t \propto \delta_t = r_{t+1} + \gamma V(s_{t+1}) - V(s_t)$$

has been significantly replicated across species, tasks, and recording modalities, and continues to organize the neuroscience-of-reinforcement-learning literature.

The hippocampal-replay-experience-replay correspondence provides the memory-consolidation correspondence. The finding of [Wilson and McNaughton 1994][research_wilson_mcnaughton_1994] that hippocampal place cells replay recent experience during sharp-wave ripples, together with the reverse-replay finding of [Foster and Wilson 2006][research_foster_wilson_2006] and the hypothesis of a common mechanism in [Kumaran McClelland Hassabis 2016][research_kumaran_mcclelland_hassabis_2016], has been substantially replicated and provides the biological correspondence to the experience-replay mechanism that traces to [Lin 1992][research_lin_1992] and has been markedly deployed in modern deep reinforcement learning.

The complementary-learning-systems correspondence of [McClelland McNaughton O'Reilly 1995][research_mcclelland_mcnaughton_oreilly_1995] provides the dual-memory-system correspondence. The finding that fast hippocampal learning and slow cortical consolidation constitute complementary memory systems has been appreciably replicated and provides the biological correspondence to the interleaved-training-and-consolidation approaches in machine learning.

The predictive-coding correspondence of [Rao and Ballard 1999][research_rao_ballard_1999] provides the perceptual-inference correspondence. The finding that cortical hierarchies implement predictive coding through the top-down expectation and bottom-up prediction-error signaling allows the hierarchical formalization

$$\epsilon_l = x_l - g_l(x_{l+1}), \quad x_l \leftarrow x_l + \eta \left( - \epsilon_l + \frac{\partial g_{l-1}(x_l)}{\partial x_l}^\top \epsilon_{l-1} \right)$$

with $x_l$ the representation at level $l$, $g_l$ the top-down generative model, and $\epsilon_l$ the residual prediction error. The framework has been greatly characterized and provides the biological correspondence to the modern generative-model and world-model literature.

The convolutional-network-visual-cortex correspondence provides the representational correspondence. The finding of [Yamins et al 2014][research_yamins_et_al_2014] that convolutional networks trained on object recognition develop representations that match the hierarchical structure of the primate ventral visual stream, together with the representational-similarity analysis framework of [Kriegeskorte Mur Bandettini 2008][research_kriegeskorte_mur_bandettini_2008], has been considerably characterized through the Brain-Score benchmarks of [Schrimpf et al 2020][research_schrimpf_et_al_2020] and provides the representational correspondence between artificial and biological visual processing. The extension to the ventral-stream-and-object-recognition literature by [Khaligh-Razavi and Kriegeskorte 2014][research_khaligh_razavi_kriegeskorte_2014] provides the complementary characterization.

The grid-cell-successor-representation correspondence provides the spatial-and-planning correspondence. The successor representation of [Dayan 1993][research_dayan_1993]

$$M^\pi(s, s') = \mathbb{E}_\pi \left[ \sum_{t=0}^\infty \gamma^t \, \mathbb{1}[s_t = s'] \mid s_0 = s \right]$$

factorizes the value function as

$$V^\pi(s) = \sum_{s'} M^\pi(s, s') R(s')$$

and the eigenvector decomposition of $M^\pi$ produces spatial basis functions with the hexagonal-grid structure observed in entorhinal grid cells. The finding of [Stachenfeld Botvinick Gershman 2017][research_stachenfeld_botvinick_gershman_2017] that entorhinal grid cells implement this eigenvector decomposition of the successor representation has been significantly characterized and provides the bridge between the neuroscience of spatial cognition of [O'Keefe and Dostrovsky 1971][research_okeefe_dostrovsky_1971] and [Hafting et al 2005][research_hafting_et_al_2005] and the successor-representation literature in machine learning.

The free-energy correspondence provides the unifying-principle correspondence. The variational free energy

$$F(q, o) = \mathbb{E}_{q(s)} \left[ \log q(s) - \log p(o, s) \right] = D_{KL}(q(s) \| p(s \mid o)) - \log p(o)$$

specifies the upper bound on surprise that biological agents are proposed to minimize under the [Friston 2010][research_friston_2010] free-energy principle. The account has been substantially formalized and provides the bridge between the neuroscience of perception, action, and learning and the variational-inference framework in machine learning.

The consolidated neuroscience correspondences constitute the settled public domain of the NeuroAI research program. The correspondences provide the empirical constraints against which candidate frameworks in machine learning are evaluated, and the formal apparatus of machine learning provides the computational vocabulary through which neuroscience can articulate and test computational hypotheses.

## Established Psychology Correspondences

The established psychology correspondences consolidate the bidirectional exchanges between the psychology of learning and machine learning that have been markedly validated at the closing of the editorial window. The model was surveyed in detail in [A264 Psychology of Learning][related_post_a264_psychology].

The Rescorla-Wagner-temporal-difference correspondence of [Rescorla and Wagner 1972][research_rescorla_wagner_1972] and [Sutton 1988][research_sutton_1988] provides the paradigmatic correspondence. The finding that the Rescorla-Wagner update rule corresponds mathematically to the temporal-difference update rule in the limit of a limiting case has been appreciably characterized and provides the bridge between the psychology of classical conditioning and modern machine learning.

The model-free-model-based-dual-system correspondence of [Daw Niv Dayan 2005][research_daw_niv_dayan_2005] provides the dual-system correspondence. The finding that habitual behavior corresponds to model-free learning and goal-directed behavior corresponds to model-based learning has been greatly characterized in both animal and human experiments and provides the bridge between the psychology of instrumental behavior and modern machine learning.

The prospect-theory-loss-aversion correspondence of [Kahneman and Tversky 1979][research_kahneman_tversky_1979] provides the decision-making correspondence. The finding that human decision-making under uncertainty exhibits systematic deviations from expected-utility theory supports the formalization through the value function

$$v(x) = \begin{cases} x^\alpha & x \geq 0 \\ -\lambda (-x)^\beta & x < 0 \end{cases}$$

with $\lambda > 1$ the loss-aversion coefficient, and the probability-weighting function

$$w(p) = \frac{p^\gamma}{(p^\gamma + (1-p)^\gamma)^{1/\gamma}}$$

that captures the overweighting of small probabilities and underweighting of moderate-to-large probabilities. This formulation has been considerably replicated and provides the empirical constraints against which candidate models of human decision-making are evaluated.

The Bayesian-cognition correspondence of [Tenenbaum Kemp Griffiths Goodman 2011][research_tenenbaum_et_al_2011] provides the probabilistic-inference correspondence. The finding that many cognitive phenomena including concept learning, causal reasoning, and inductive generalization admit characterization as Bayesian inference over structured hypothesis spaces admits the formalization

$$p(h \mid d) = \frac{p(d \mid h) \, p(h)}{\sum_{h' \in \mathcal{H}} p(d \mid h') \, p(h')}$$

with $\mathcal{H}$ a structured hypothesis space over concepts, causal graphs, or grammatical rules. The treatment has been significantly characterized and provides the bridge between the psychology of cognition and probabilistic machine learning.

The categorization-and-similarity correspondence provides the representation-learning correspondence. The findings including the [Rosch 1975][research_rosch_1975] prototype theory, the [Nosofsky 1986][research_nosofsky_1986] generalized context model, and the modern [Kemp and Tenenbaum 2008][research_kemp_tenenbaum_2008] structure-discovery framework have been substantially replicated and provide the bridge between the psychology of categorization and modern representation learning.

The spacing-and-retrieval-practice correspondence provides the educational-technology correspondence. The [Ebbinghaus 1885][book_ebbinghaus_1885] forgetting curve

$$R(t) = R_0 \, e^{-t/\tau}$$

with $R(t)$ retention at time $t$ and $\tau$ a memory-time constant, and the [Cepeda et al 2008][research_cepeda_et_al_2008] distributed-practice power-law form

$$R(t, s) = R_0 \, (1 + t/s)^{-\beta}$$

with $s$ the spacing between study sessions and $\beta$ a task-forgetting parameter, together with the [Roediger and Karpicke 2006][research_roediger_karpicke_2006] test-enhanced-learning framework, have been markedly replicated and provide the practical foundation for modern learning technology.

The consolidated psychology correspondences constitute the settled public domain of the psychology-machine-learning research program. The correspondences provide the empirical constraints against which candidate frameworks in machine learning are evaluated, and the formal apparatus of machine learning provides the computational vocabulary through which psychology can articulate and test its theories.

## The Foundation-Model Turn and Reinforcement Learning

The foundation-model turn constitutes the paradigm shift that has appreciably reorganized the field at the closing of the editorial window. This account treats large pre-trained models, trained on broad corpora through self-supervised learning at scale, as the substrate for downstream experiential learning through fine-tuning, reinforcement learning from human feedback, and agentic frameworks. The integration of foundation models with the classical experiential-learning framework has emerged as one of the most active research areas of the field.

The [Bommasani et al 2021][research_bommasani_et_al_2021] report On the Opportunities and Risks of Foundation Models provides the institutional consolidation of the paradigm. The framework treats foundation models as the general-purpose substrate whose downstream deployment through the fine-tuning and reinforcement-learning-from-human-feedback pipelines produces the application-capabilities of the modern deployment landscape.

The scaling laws of [Kaplan et al 2020][research_kaplan_et_al_2020] and the compute-optimal refinement of [Hoffmann et al 2022][research_hoffmann_et_al_2022] provide the empirical foundation for the paradigm. The findings that model capability follows the parametric relationship

$$L(N, D) = \frac{A}{N^\alpha} + \frac{B}{D^\beta} + E$$

with model size $N$ and training-token count $D$ have greatly shaped the research on the scaling of foundation models and the downstream deployment through experiential learning.

The emergence phenomena of [Wei et al 2022][research_wei_et_al_2022_emergent] identify the capabilities that appear discontinuously with scale, and the chain-of-thought prompting framework of [Wei et al 2022][research_wei_et_al_2022_cot] provides the reasoning-enhancement technique that continues to organize the research on foundation-model reasoning.

The reinforcement-learning-from-human-feedback pipeline of [Ouyang et al 2022][research_ouyang_et_al_2022] provides the alignment mechanism that has been considerably deployed across the modern foundation-model deployment landscape. The pipeline comprises the three-stage sequence of supervised fine-tuning on demonstrations, reward-model training on human preferences, and reinforcement-learning optimization of the policy against the learned reward model. The integration of the classical policy-gradient framework with the foundation-model substrate has significantly organized the modern alignment literature.

The constitutional AI framework of [Bai et al 2022][research_bai_et_al_2022] provides the extension in which the reward-model training uses model-generated preferences guided by a written constitution rather than the direct human preferences. The account has substantially reorganized the scalable-oversight literature and continues to organize the research on foundation-model alignment.

The agentic-frameworks paradigm treats foundation models as the policy substrate for the sequential decision-making tasks that constitute the classical experiential-learning framework. The integration through tool-use, chain-of-thought reasoning, and hierarchical planning provides the research frontier at the intersection of foundation models and reinforcement learning. The empirical performance of agentic foundation models on the benchmarks including SWE-bench, WebArena, and AgentBench remains an active research area whose characterization continues to organize the field.

The tension between the pre-training paradigm and the classical experiential-learning framework remains markedly unresolved. The claim that pre-training on broad corpora appreciably reduces the need for downstream experiential learning is greatly supported by the empirical findings on in-context learning. The counter-claim that experiential learning remains necessary for the tasks that require environmental interaction is considerably supported by the findings on the integration challenges. The research on the optimal integration of pre-training and reinforcement learning remains an active area at the closing of the editorial window.

## Position Papers and Canonical Debates

The position papers and canonical debates that organize the field at the closing of the editorial window characterize the open questions that shape the research directions of the coming period. The model provides the field-level context within which the technical research proceeds.

The Bitter Lesson of [Sutton 2019][research_sutton_2019_bitter_lesson] provides the canonical position statement on the relationship between the general-purpose scaling of computation and the incorporation of human-engineered domain knowledge. The claim that the general-purpose methods that leverage the increases in available computation eventually outperform the methods that incorporate domain-human knowledge has significantly organized the research direction of the field and continues to shape the institutional and technical debates.

The Reward is Enough thesis of [Silver Singh Precup Sutton 2021][research_silver_et_al_2021] provides the canonical position statement on the sufficiency of reward maximization as the framework for artificial intelligence. The strong claim

$$\pi^* = \arg\max_\pi \mathbb{E}_\pi \left[ \sum_{t=0}^\infty \gamma^t r_{t+1} \right]$$

as the general framework for goal-directed behavior remains substantially contested at the closing of the editorial window, with the critical responses of [Roy Duckett 2022][research_roy_duckett_2022] and the alternative frameworks including preference learning and inverse reinforcement learning providing the empirical alternatives.

The Welcome to the Era of Experience position paper of [Silver and Sutton 2024][research_silver_sutton_2024] provides the canonical position statement on the role of experiential learning at the closing of the era of static-data pre-training. The claim that the next generation of AI systems will markedly depend on experiential learning from environmental interaction rather than on the static-data pre-training paradigm has appreciably organized the research direction of the field.

The Catalyzing NeuroAI grand challenges of [Zador et al 2023][research_zador_et_al_2023] provide the canonical position statement on the research directions in NeuroAI at the closing of the editorial window. The grand challenges including the embodied Turing test, the development of the animal-like AI capabilities, and the bidirectional exchange between neuroscience and machine learning provide the research directions that continue to organize the field.

The alignment-problem framing of [Ngo Chan Mindermann 2022][research_ngo_chan_mindermann_2022] The Alignment Problem from a Deep Learning Perspective provides the canonical position statement on the alignment challenges facing modern deep learning systems. The taxonomy of misalignment failure modes and the research directions for their resolution have greatly organized the modern alignment-and-safety literature.

The consolidated position papers constitute the field-level context within which the technical research proceeds at the closing of the editorial window. The debates the papers organize continue to shape the research directions of the field, and the resolution of the debates through the empirical developments of subsequent research remains an active research area.

## Open Problems, Theoretical Foundations

The open problems in the theoretical foundations of experiential learning identify the residual questions whose resolution would considerably reorganize the field. This formulation identifies the formal questions that remain contested at the closing of the editorial window.

The deadly-triad problem identifies the instability arising from the combination of off-policy learning, function approximation, and bootstrapping. The divergence examples of [Baird 1995][research_baird_1995] and the systematic characterization of [Van Hasselt et al 2018][research_van_hasselt_et_al_2018] establish the empirical scope of the phenomenon. The empirical practice has assembled workarounds through the target-network stabilization, the experience-replay decorrelation, and the double Q-learning bias-correction techniques. The theoretical characterization of when the triad is safe and when it is unstable remains significantly open and constitutes one of the open problems of the field.

The exploration-exploitation-tradeoff problem in high-dimensional structured environments identifies the gap between the tight regret bounds available for bandits and low-dimensional Markov decision processes and the empirical performance of intrinsic-motivation methods in high-dimensional structured environments. The formal characterization of the sample-complexity of exploration in high-dimensional structured environments remains substantially open.

The partial-observability problem identifies the gap between the tractable partially-observable Markov decision process framework and the empirical reality of partially-observable environments at scale. The formal characterization of what representation-learning objectives suffice for near-optimal control under partial observability remains markedly open.

The sample-complexity-versus-computational-complexity problem identifies the tradeoff between sample-efficient algorithms (typically expensive computationally) and computationally-efficient algorithms (typically expensive in samples). The PAC-MDP sample-complexity bounds of [Kakade 2003][research_kakade_2003] and [Strehl Li Littman 2009][research_strehl_li_littman_2009]

$$\tilde{O}\left( \frac{|\mathcal{S}||\mathcal{A}|}{(1 - \gamma)^3 \epsilon^2} \right)$$

for tabular reinforcement learning provide the worst-case characterization of the tabular setting, but the corresponding bounds under function approximation, partial observability, and structured environments remain appreciably open. The optimal tradeoff and the conditions under which each family of algorithms is preferred remain greatly open.

The open-endedness problem identifies the gap between the frameworks of reinforcement learning and evolutionary computation and the open-endedness that human cultures and biological evolution exhibit. The formal characterization of open-endedness and the mechanisms that produce it remain considerably open and provide the research frontier for [A261 Evolutionary and Open-Ended Adaptation][related_post_a261_evolutionary].

The reward-hypothesis problem identifies the status of the [Silver Singh Precup Sutton 2021][research_silver_et_al_2021] Reward is Enough thesis. The claim in its strong form is that any goal-directed behavior of interest can be characterized as maximization of a expected cumulative reward

$$\pi^* = \arg\max_\pi \mathbb{E}_\pi \left[ \sum_{t=0}^\infty \gamma^t r_{t+1} \right]$$

for a reward specification $r$. The empirical support for the thesis under the conditions of practical machine learning is significantly contested, and the alternative frameworks including preference learning and inverse reinforcement learning provide the empirical alternatives whose relative strengths remain substantially open.

The bounded-agent-and-hierarchical-decomposition problem identifies the formal characterization of hierarchical decomposition under bounded computational resources. The relationships between the options framework, the MAXQ decomposition, the feudal networks framework, and the temporally-extended action frameworks remain markedly open at the level of a unified formal theory.

The consolidated theoretical open problems constitute the research frontier for the theoretical foundations of the field. The research directions have been appreciably characterized in the survey articles of the series and continue to organize modern research.

## Open Problems, Algorithmic Frontiers

The open problems in the algorithmic frontiers identify the residual questions in algorithm design whose resolution would greatly advance the practical capabilities of experiential learning systems.

The credit assignment problem at long horizons identifies the difficulty of assigning credit for delayed rewards at temporal horizons considerably longer than those addressed by the standard algorithms. The eligibility-trace framework and the $n$-step-return framework provide partial solutions, but the credit-assignment problem at very long horizons remains significantly open.

The reward-model-learning problem in reinforcement learning from human feedback identifies the difficulty of learning reward models that generalize to novel behaviors. The findings on reward hacking, specification gaming, and reward-model exploitation surveyed in [Amodei et al 2016][research_amodei_et_al_2016] Concrete Problems in AI Safety, in [Krakovna et al 2020][research_krakovna_et_al_2020], and in the systematic study of RLHF failure modes in [Casper et al 2023][research_casper_et_al_2023] remain substantially uncharacterized and provide the research frontier for [A260 Learning From Demonstration Preference and Other Agents][related_post_a260_demonstration].

The catastrophic-forgetting problem at scale identifies the difficulty of preventing catastrophic forgetting in modern deep learning systems that must acquire and preserve considerable task suites. The empirical findings on the effectiveness of the modern continual-learning algorithms at scale remain markedly uncharacterized and provide the research frontier for [A259 Continual and Lifelong Learning][related_post_a259_continual].

The meta-learning-scale problem identifies the gap between the successes of meta-learning at small scales and the empirical performance of meta-learning at the scale of foundation models. The correspondence between the in-context-learning phenomenon and the classical meta-learning framework remains appreciably open at the level of formal characterization.

The world-model-scale problem identifies the gap between the successes of world models at low-dimensional continuous-control problems and the empirical performance of world models at the scale of complex environments. The representation-learning objectives that suffice for effective world-modeling remain greatly open and provide the research frontier for [A256 World Models and Predictive Model-Based Adaptation][related_post_a256_world_models].

The offline-reinforcement-learning-generalization problem identifies the difficulty of achieving policies that generalize considerably beyond the coverage of the offline dataset. The formal characterization of when offline reinforcement learning permits strong generalization guarantees remains significantly open and provides the research frontier for [A257 Offline and Batch Reinforcement Learning][related_post_a257_offline].

The multi-agent-learning-and-coordination problem identifies the difficulty of achieving coordinated behavior in multi-agent settings without explicit central coordination. The empirical findings on emergent coordination in multi-agent reinforcement learning remain substantially uncharacterized and provide the research frontier for the multi-agent extensions of experiential learning.

The consolidated algorithmic open problems constitute the research frontier for the algorithmic development of the field. The research directions have been markedly characterized in the survey articles of the series and continue to organize modern research.

## Open Problems, Empirical Benchmarks

The open problems in empirical benchmarks identify the residual questions in the measurement and evaluation of experiential learning systems.

The benchmark-validity problem identifies the gap between the empirical performance on standard benchmarks and the empirical performance on the underlying capabilities the benchmarks are intended to measure. The findings on benchmark saturation, benchmark gaming, and benchmark-versus-transfer divergence remain appreciably uncharacterized.

The evaluation-reproducibility problem identifies the difficulty of reproducing the empirical claims in deep reinforcement learning research. The findings including the [Henderson et al 2018][research_henderson_et_al_2018] characterization of the variance in deep-reinforcement-learning benchmark results have provided the empirical foundation for the modern evaluation-reform movement in the field.

The compute-and-scale-dependence problem identifies the difficulty of separating the algorithmic contributions from the scale-dependent contributions in modern deep reinforcement learning research. The empirical findings that many algorithmic improvements are contingent on the compute and scale conditions provide the empirical foundation for the modern research on scaling laws in reinforcement learning.

The safety-evaluation problem identifies the difficulty of evaluating the safety properties of modern reinforcement learning systems. The empirical findings on reward hacking, specification gaming, and power-seeking behavior remain greatly uncharacterized and provide the research frontier for the safety-evaluation literature.

The consolidated empirical-benchmark open problems constitute the research frontier for the measurement and evaluation infrastructure of the field. The research directions continue to organize modern research on the methodological standards of the field.

## Open Problems, Neuroscience Correspondence

The open problems in the neuroscience correspondence identify the residual questions in the bidirectional exchange between neuroscience and machine learning.

The biological-plausibility-of-backpropagation problem identifies the difficulty of reconciling the effectiveness of backpropagation in machine learning with the implausibility of backpropagation as a biological learning rule surveyed in [Crick 1989][research_crick_1989] and [Lillicrap et al 2020][research_lillicrap_et_al_2020]. The candidate biological-learning-rule frameworks including feedback alignment of [Lillicrap et al 2016][research_lillicrap_et_al_2016], predictive coding as a biological learning rule characterized in [Whittington and Bogacz 2017][research_whittington_bogacz_2017], and target propagation of [Lee Zhang Fischer Bengio 2015][research_lee_zhang_fischer_bengio_2015] provide partial solutions, but the correspondence between biological and artificial learning rules remains considerably open.

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

The reward-specification-problem identifies the difficulty of specifying reward functions that produce the intended behavior across the full deployment distribution. The findings of [Amodei et al 2016][research_amodei_et_al_2016] on concrete problems in AI safety, the taxonomies of [Krakovna et al 2020][research_krakovna_et_al_2020] on specification gaming, the characterization of the Goodhart-effect regimes in [Manheim and Garrabrant 2018][research_manheim_garrabrant_2018], and the study of reward-model over-optimization in [Gao Schulman Hilton 2023][research_gao_schulman_hilton_2023] provide the empirical foundation for the research on reward-specification robustness.

The scalable-oversight-problem identifies the difficulty of providing effective human oversight to reinforcement-learning systems at scales where human evaluation cannot cover the full deployment distribution. The candidate frameworks including debate of [Irving Christiano Amodei 2018][research_irving_christiano_amodei_2018], iterated amplification of [Christiano Shlegeris Amodei 2018][research_christiano_shlegeris_amodei_2018], and constitutional AI of [Bai et al 2022][research_bai_et_al_2022] provide partial solutions, but the effectiveness of scalable oversight remains significantly open.

The mesa-optimization-and-inner-alignment problem identifies the difficulty of ensuring that the learned policies do not implement internal optimization processes with objectives that diverge from the outer training objective. The taxonomy of [Hubinger et al 2019][research_hubinger_et_al_2019] Risks from Learned Optimization provides the formal characterization of the problem. The characterization of when mesa-optimization arises and the mechanisms that produce it remain substantially open.

The power-seeking-and-instrumental-convergence problem identifies the empirical and theoretical questions about the conditions under which reinforcement-learning agents develop instrumentally-convergent power-seeking behaviors. The formal analysis of [Turner et al 2021][research_turner_et_al_2021] Optimal Policies Tend to Seek Power characterizes the class of environments in which instrumental convergence provably arises. The formal characterization of when instrumental convergence arises in the settings of practical machine learning remains markedly open.

The governance-and-deployment-safety problem identifies the institutional questions about the safe deployment of reinforcement-learning systems in the real-world contexts including healthcare, finance, criminal justice, and autonomous systems. The institutional frameworks for the governance of these deployments remain appreciably open and provide the research frontier for the technical-governance literature.

The consolidated alignment-safety-and-governance open problems constitute the research frontier for the safe deployment of the field's technology. The research directions continue to organize modern research on the safety and governance challenges the field faces.

## Empirical Landscape at the Closing of the Editorial Window

The empirical landscape at the closing of the editorial window in the mid 2020s characterizes the state of the field's capabilities, benchmarks, and open questions as of the temporal window of this survey.

Deep reinforcement learning systems have achieved significant performance on the canonical benchmarks including Atari, MuJoCo, Go, chess, and shogi. The empirical performance has greatly saturated on the classical benchmarks, with the human-normalized scores on the fifty-seven-game Atari suite exceeding one hundred percent on the median-game metric for the canonical algorithms, and the MuJoCo continuous-control benchmarks producing the asymptotic performance close to the theoretical maxima for the canonical tasks. The research frontier has considerably shifted to the more challenging benchmarks including the Procgen generalization benchmarks of [Cobbe et al 2020][research_cobbe_et_al_2020], the Meta-World multi-task benchmarks of [Yu et al 2020][research_yu_et_al_2020], the bsuite behavior suite of [Osband et al 2020][research_osband_et_al_2020] for characterizing agent behavior along the dimensions of memory, generalization, and exploration, the complex real-time strategy games as characterized in the OpenAI Five Dota 2 system of [Berner et al 2019][research_berner_et_al_2019] and the AlphaStar StarCraft II system of [Vinyals et al 2019][research_vinyals_et_al_2019], the NetHack learning environment of [Küttler et al 2020][research_kuttler_et_al_2020] as a specifically-difficult exploration benchmark, and the open-ended learning environments including XLand of [Team et al 2021][research_openended_team_2021].

Foundation models as characterized in [Bommasani et al 2021][research_bommasani_et_al_2021] have emerged as a new paradigm that significantly reshapes the research landscape. The findings including the scaling laws of [Kaplan et al 2020][research_kaplan_et_al_2020] and [Hoffmann et al 2022][research_hoffmann_et_al_2022], the in-context-learning phenomena of [Brown et al 2020][research_brown_et_al_2020], and the reinforcement-learning-from-human-feedback pipelines of [Ouyang et al 2022][research_ouyang_et_al_2022] have substantially reorganized the field's research agenda. The integration of foundation models with the classical reinforcement-learning framework remains an active and rapidly-moving research area.

Offline reinforcement learning has emerged as a practical framework for the deployment of reinforcement learning in the settings where online interaction is expensive or unsafe. The empirical performance of the canonical offline algorithms has been markedly characterized on the benchmark datasets, and the practical applications to healthcare, robotics, and recommendation systems have appreciably matured.

Meta-learning and in-context learning have emerged as the mechanisms through which foundation models achieve their broad task competence. The relationship between the classical meta-learning framework and the in-context-learning phenomena of foundation models continues to organize substantial research.

Alignment and safety research has emerged as a institutional research area with marked funding, staffing, and institutional consolidation. The empirical findings on reward hacking, specification gaming, and power-seeking behavior have provided the foundation for the research on the safe deployment of the field's technology.

The institutional consolidation of the field has continued with the emergence of dedicated conferences, journals, and open-source infrastructure. The research communities including the reinforcement learning, safe reinforcement learning, offline reinforcement learning, and NeuroAI communities have greatly matured and provide the institutional infrastructure for the cumulative-progress dynamics of the field.

The consolidated empirical landscape provides the starting point from which the research developments of the subsequent years will proceed. The settled-versus-open partition that this article surveys will be considerably revised by the research developments that occur in the intervening period.

## Applications, Established and Emerging

The applications of experiential learning have significantly expanded across the corpus of settled-and-emerging deployment contexts.

Established applications include the deployment of reinforcement learning in the domains of game playing (including chess, Go, poker as demonstrated in [Brown and Sandholm 2018][research_brown_sandholm_2018] Libratus and [Moravčík et al 2017][research_moravcik_et_al_2017] DeepStack, video games, and real-time strategy), recommendation systems, dialogue systems, robot control (including manipulation, locomotion, and navigation), datacenter cooling of [Lazic et al 2018][research_lazic_et_al_2018], chip design of [Mirhoseini et al 2021][research_mirhoseini_et_al_2021], and drug discovery. The empirical findings have substantially matured in these domains and continue to organize the practical research on their deployment.

Emerging applications include the deployment of reinforcement learning in the domains of autonomous driving, healthcare (including treatment recommendation, drug dosing, and adaptive clinical trials), education (including personalized instruction and adaptive testing), financial services (including trading, portfolio management, and fraud detection), and scientific discovery (including materials science, protein design as demonstrated in the AlphaFold protein-structure-prediction system of [Jumper et al 2021][research_jumper_et_al_2021], and mathematical proof discovery). The empirical findings continue to organize the practical research on the deployment challenges these domains present.

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

## References

### Books

- [Bellman 1957 Dynamic Programming][book_bellman_1957]
- [Bertsekas and Tsitsiklis 1996 Neuro-Dynamic Programming][book_bertsekas_tsitsiklis_1996]
- [Ebbinghaus 1885 Memory][book_ebbinghaus_1885]
- [Howard 1960 Dynamic Programming and Markov Processes][book_howard_1960]
- [Kahneman 2011 Thinking Fast and Slow][book_kahneman_2011]
- [Pfeifer and Bongard 2007 How the Body Shapes the Way We Think][book_pfeifer_bongard_2007]
- [Russell and Norvig 2020 Artificial Intelligence][book_russell_norvig_2020]
- [Sutton and Barto 2018 Reinforcement Learning][book_sutton_barto_2018]

### Reference

- [Berkeley CS285][ref_berkeley_cs285]
- [DeepMind x UCL RL Course][ref_deepmind_ucl_rl]
- [OpenAI Spinning Up][ref_openai_spinning_up]
- [Silver RL Course UCL][ref_silver_rl_course]
- [Stanford CS234][ref_stanford_cs234]

### Related Posts

- [A250 Machines That Learn From Experience Framing][related_post_a250_framing]
- [A251 Machines That Learn From Experience Bandits and Online Learning][related_post_a251_bandits]
- [A252 Machines That Learn From Experience Reinforcement Learning Foundations][related_post_a252_rl_foundations]
- [A253 Machines That Learn From Experience Deep Reinforcement Learning][related_post_a253_deep_rl]
- [A254 Machines That Learn From Experience Exploration Intrinsic Motivation and Curiosity][related_post_a254_exploration]
- [A255 Machines That Learn From Experience Hierarchical Reinforcement Learning][related_post_a255_hierarchical]
- [A256 Machines That Learn From Experience World Models and Predictive Model-Based Adaptation][related_post_a256_world_models]
- [A257 Machines That Learn From Experience Offline and Batch Reinforcement Learning][related_post_a257_offline]
- [A258 Machines That Learn From Experience Meta-Learning and Online Adaptation][related_post_a258_meta_learning]
- [A259 Machines That Learn From Experience Continual and Lifelong Learning][related_post_a259_continual]
- [A260 Machines That Learn From Experience Learning From Demonstration Preference and Other Agents][related_post_a260_demonstration]
- [A261 Machines That Learn From Experience Evolutionary and Open-Ended Adaptation][related_post_a261_evolutionary]
- [A262 Machines That Learn From Experience Embodied Cognition and Developmental Learning][related_post_a262_embodied]
- [A263 Machines That Learn From Experience NeuroAI][related_post_a263_neuroai]
- [A264 Machines That Learn From Experience Psychology of Learning][related_post_a264_psychology]

### Research

- [Abbeel and Ng 2004 Apprenticeship Learning][research_abbeel_ng_2004]
- [Amodei et al 2016 Concrete Problems in AI Safety][research_amodei_et_al_2016]
- [Auer Cesa-Bianchi Fischer 2002 UCB][research_auer_cesa_bianchi_fischer_2002]
- [Bacon Harb Precup 2017 Option-Critic][research_bacon_harb_precup_2017]
- [Bai et al 2022 Constitutional AI][research_bai_et_al_2022]
- [Baird 1995 Residual Algorithms][research_baird_1995]
- [Bellemare Dabney Munos 2017 Distributional RL][research_bellemare_dabney_munos_2017]
- [Bellemare et al 2013 Arcade Learning Environment][research_bellemare_et_al_2013]
- [Bellemare et al 2016 Pseudocount Exploration][research_bellemare_et_al_2016]
- [Bengio et al 2009 Curriculum Learning][research_bengio_et_al_2009]
- [Berner et al 2019 OpenAI Five Dota 2][research_berner_et_al_2019]
- [Bommasani et al 2021 Foundation Models][research_bommasani_et_al_2021]
- [Brown et al 2020 GPT-3 In-Context Learning][research_brown_et_al_2020]
- [Brown and Sandholm 2018 Libratus Poker][research_brown_sandholm_2018]
- [Casper et al 2023 Open Problems in RLHF][research_casper_et_al_2023]
- [Cepeda et al 2008 Distributed Practice][research_cepeda_et_al_2008]
- [Chaudhry et al 2019 Averaged Gradient Episodic Memory][research_chaudhry_et_al_2019]
- [Christiano et al 2017 Preference Learning][research_christiano_et_al_2017]
- [Christiano Shlegeris Amodei 2018 Iterated Amplification][research_christiano_shlegeris_amodei_2018]
- [Cobbe et al 2020 Procgen Benchmark][research_cobbe_et_al_2020]
- [Crick 1989 Recent Excitement About Neural Networks][research_crick_1989]
- [Dabney et al 2018 Implicit Quantile Networks][research_dabney_et_al_2018_iqn]
- [Dabney et al 2018 Quantile Regression DQN][research_dabney_et_al_2018_qr_dqn]
- [Daw Niv Dayan 2005 Uncertainty Competition][research_daw_niv_dayan_2005]
- [Dayan 1993 Successor Representation][research_dayan_1993]
- [Dayan and Hinton 1993 Feudal Reinforcement Learning][research_dayan_hinton_1993]
- [Deisenroth and Rasmussen 2011 PILCO][research_deisenroth_rasmussen_2011]
- [Dietterich 2000 MAXQ][research_dietterich_2000]
- [Duan et al 2016 RL Squared][research_duan_et_al_2016]
- [Finn Abbeel Levine 2017 MAML][research_finn_abbeel_levine_2017]
- [Foster and Wilson 2006 Reverse Replay][research_foster_wilson_2006]
- [Friston 2010 Free Energy Principle][research_friston_2010]
- [Fujimoto Hoof Meger 2018 TD3][research_fujimoto_hoof_meger_2018]
- [Fujimoto Meger Precup 2019 Batch-Constrained Q-Learning][research_fujimoto_meger_precup_2019]
- [Gao Schulman Hilton 2023 Reward Model Over-Optimization][research_gao_schulman_hilton_2023]
- [Ha and Schmidhuber 2018 World Models][research_ha_schmidhuber_2018]
- [Haarnoja et al 2018 Soft Actor-Critic][research_haarnoja_et_al_2018]
- [Hafner et al 2020 Dreamer][research_hafner_et_al_2020]
- [Hafner et al 2023 DreamerV3][research_hafner_et_al_2023]
- [Hafting et al 2005 Grid Cells][research_hafting_et_al_2005]
- [Henderson et al 2018 Deep RL That Matters][research_henderson_et_al_2018]
- [Ho and Ermon 2016 GAIL][research_ho_ermon_2016]
- [Hoffmann et al 2022 Chinchilla][research_hoffmann_et_al_2022]
- [Houthooft et al 2016 VIME][research_houthooft_et_al_2016]
- [Hubinger et al 2019 Risks From Learned Optimization][research_hubinger_et_al_2019]
- [Irving Christiano Amodei 2018 AI Safety via Debate][research_irving_christiano_amodei_2018]
- [Jumper et al 2021 AlphaFold][research_jumper_et_al_2021]
- [Kahneman and Tversky 1979 Prospect Theory][research_kahneman_tversky_1979]
- [Kakade 2003 Sample Complexity of RL][research_kakade_2003]
- [Kaplan et al 2020 Scaling Laws][research_kaplan_et_al_2020]
- [Kemp and Tenenbaum 2008 Structural Form][research_kemp_tenenbaum_2008]
- [Khaligh-Razavi and Kriegeskorte 2014 Deep Networks IT Models][research_khaligh_razavi_kriegeskorte_2014]
- [Kirkpatrick et al 2017 EWC][research_kirkpatrick_et_al_2017]
- [Klyubin Polani Nehaniv 2005 Empowerment][research_klyubin_polani_nehaniv_2005]
- [Kostrikov Nair Levine 2022 Implicit Q-Learning][research_kostrikov_nair_levine_2022]
- [Krakovna et al 2020 Specification Gaming][research_krakovna_et_al_2020]
- [Kriegeskorte Mur Bandettini 2008 Representational Similarity Analysis][research_kriegeskorte_mur_bandettini_2008]
- [Kumar et al 2020 Conservative Q-Learning][research_kumar_et_al_2020]
- [Kumaran McClelland Hassabis 2016 Complementary Learning Systems Update][research_kumaran_mcclelland_hassabis_2016]
- [Küttler et al 2020 NetHack Learning Environment][research_kuttler_et_al_2020]
- [Lai and Robbins 1985 Bandit Lower Bound][research_lai_robbins_1985]
- [Lazic et al 2018 Data Center Cooling][research_lazic_et_al_2018]
- [Lee Zhang Fischer Bengio 2015 Target Propagation][research_lee_zhang_fischer_bengio_2015]
- [Lehman and Stanley 2011 Novelty Search][research_lehman_stanley_2011]
- [Levine et al 2020 Offline RL Tutorial][research_levine_et_al_2020]
- [Lillicrap et al 2015 DDPG][research_lillicrap_et_al_2015]
- [Lillicrap et al 2016 Feedback Alignment][research_lillicrap_et_al_2016]
- [Lillicrap et al 2020 Backpropagation and the Brain][research_lillicrap_et_al_2020]
- [Lin 1992 Experience Replay][research_lin_1992]
- [Lopez-Paz and Ranzato 2017 Gradient Episodic Memory][research_lopez_paz_ranzato_2017]
- [Manheim and Garrabrant 2018 Goodhart's Law][research_manheim_garrabrant_2018]
- [McClelland McNaughton O'Reilly 1995 Complementary Learning Systems][research_mcclelland_mcnaughton_oreilly_1995]
- [Mirhoseini et al 2021 Chip Placement][research_mirhoseini_et_al_2021]
- [Mnih et al 2015 Deep Q-Network][research_mnih_et_al_2015]
- [Mnih et al 2016 A3C][research_mnih_et_al_2016]
- [Moravčík et al 2017 DeepStack Poker][research_moravcik_et_al_2017]
- [Mouret and Clune 2015 MAP-Elites][research_mouret_clune_2015]
- [Ng and Russell 2000 Inverse Reinforcement Learning][research_ng_russell_2000]
- [Ngo Chan Mindermann 2022 Alignment Problem][research_ngo_chan_mindermann_2022]
- [Nosofsky 1986 Generalized Context Model][research_nosofsky_1986]
- [O'Keefe and Dostrovsky 1971 Place Cells][research_okeefe_dostrovsky_1971]
- [Open Science Collaboration 2015 Reproducibility Project][research_osc_2015]
- [Open-Ended Team 2021 XLand][research_openended_team_2021]
- [Osband et al 2020 Behaviour Suite bsuite][research_osband_et_al_2020]
- [O'Regan and Noë 2001 Sensorimotor Contingency][research_oregan_noe_2001]
- [Ouyang et al 2022 InstructGPT][research_ouyang_et_al_2022]
- [Pathak et al 2017 Curiosity Driven Exploration][research_pathak_et_al_2017]
- [Rao and Ballard 1999 Predictive Coding][research_rao_ballard_1999]
- [Rescorla and Wagner 1972 Classical Conditioning][research_rescorla_wagner_1972]
- [Roediger and Karpicke 2006 Test-Enhanced Learning][research_roediger_karpicke_2006]
- [Rosch 1975 Prototype Theory][research_rosch_1975]
- [Roy and Duckett 2022 Reward is Enough Critique][research_roy_duckett_2022]
- [Rummery and Niranjan 1994 SARSA][research_rummery_niranjan_1994]
- [Rusu et al 2016 Progressive Networks][research_rusu_et_al_2016]
- [Salimans et al 2017 Evolutionary Strategies][research_salimans_et_al_2017]
- [Schrimpf et al 2020 Brain-Score][research_schrimpf_et_al_2020]
- [Schrittwieser et al 2020 MuZero][research_schrittwieser_et_al_2020]
- [Schulman et al 2015 TRPO][research_schulman_et_al_2015]
- [Schulman et al 2017 PPO][research_schulman_et_al_2017]
- [Schultz Dayan Montague 1997 Reward Prediction Error][research_schultz_dayan_montague_1997]
- [Shin et al 2017 Generative Replay][research_shin_et_al_2017]
- [Silver et al 2014 Deterministic Policy Gradient][research_silver_et_al_2014]
- [Silver et al 2016 AlphaGo][research_silver_et_al_2016]
- [Silver et al 2017 AlphaZero][research_silver_et_al_2017]
- [Silver et al 2018 AlphaZero Journal][research_silver_et_al_2018]
- [Silver Singh Precup Sutton 2021 Reward Is Enough][research_silver_et_al_2021]
- [Silver and Sutton 2024 Era of Experience][research_silver_sutton_2024]
- [Stachenfeld Botvinick Gershman 2017 Grid Cells Successor Representation][research_stachenfeld_botvinick_gershman_2017]
- [Stanley and Miikkulainen 2002 NEAT][research_stanley_miikkulainen_2002]
- [Stiennon et al 2020 Learning to Summarize with Human Feedback][research_stiennon_et_al_2020]
- [Strehl Li Littman 2009 PAC-MDP Analysis][research_strehl_li_littman_2009]
- [Sutton 1988 Temporal-Difference Learning][research_sutton_1988]
- [Sutton 1991 Dyna][research_sutton_1991]
- [Sutton 2019 The Bitter Lesson][research_sutton_2019_bitter_lesson]
- [Sutton McAllester Singh Mansour 2000 Policy Gradient Theorem][research_sutton_et_al_2000]
- [Sutton Precup Singh 1999 Options][research_sutton_precup_singh_1999]
- [Tenenbaum Kemp Griffiths Goodman 2011 How to Grow a Mind][research_tenenbaum_et_al_2011]
- [Thompson 1933 Thompson Sampling][research_thompson_1933]
- [Todorov Erez Tassa 2012 MuJoCo][research_todorov_erez_tassa_2012]
- [Turner et al 2021 Optimal Policies Seek Power][research_turner_et_al_2021]
- [Van Hasselt et al 2018 Deadly Triad Deep RL][research_van_hasselt_et_al_2018]
- [Van Hasselt Guez Silver 2016 Double DQN][research_van_hasselt_guez_silver_2016]
- [Van Seijen et al 2009 Expected SARSA][research_van_seijen_et_al_2009]
- [Vezhnevets et al 2017 FeUdal Networks][research_vezhnevets_et_al_2017]
- [Vinyals et al 2019 AlphaStar][research_vinyals_et_al_2019]
- [Wang et al 2016 Meta Reinforcement Learning][research_wang_et_al_2016]
- [Wang et al 2016 Dueling DQN][research_wang_et_al_2016_dueling]
- [Wang Lehman Clune Stanley 2019 POET][research_wang_lehman_clune_stanley_2019]
- [Watkins 1989 Q-Learning][research_watkins_1989]
- [Watkins and Dayan 1992 Q-Learning Convergence][research_watkins_dayan_1992]
- [Wei et al 2022 Chain-of-Thought Prompting][research_wei_et_al_2022_cot]
- [Wei et al 2022 Emergent Abilities][research_wei_et_al_2022_emergent]
- [Weng et al 2001 Developmental Robotics][research_weng_et_al_2001]
- [Whittington and Bogacz 2017 Predictive Coding as Biological Learning][research_whittington_bogacz_2017]
- [Williams 1992 REINFORCE][research_williams_1992]
- [Wilson and McNaughton 1994 Hippocampal Replay][research_wilson_mcnaughton_1994]
- [Yamins et al 2014 Ventral Stream Task Optimization][research_yamins_et_al_2014]
- [Yu et al 2020 Meta-World][research_yu_et_al_2020]
- [Zador et al 2023 Catalyzing NeuroAI][research_zador_et_al_2023]
- [Ziebart et al 2008 Maximum Entropy IRL][research_ziebart_et_al_2008]

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
[research_abbeel_ng_2004]: https://dl.acm.org/doi/10.1145/1015330.1015430
[research_amodei_et_al_2016]: https://arxiv.org/abs/1606.06565
[research_auer_cesa_bianchi_fischer_2002]: https://link.springer.com/article/10.1023/A:1013689704352
[research_bacon_harb_precup_2017]: https://ojs.aaai.org/index.php/AAAI/article/view/10916
[research_bai_et_al_2022]: https://arxiv.org/abs/2212.08073
[research_baird_1995]: https://www.sciencedirect.com/science/article/pii/B9781558603776500337
[research_bellemare_dabney_munos_2017]: https://proceedings.mlr.press/v70/bellemare17a.html
[research_bellemare_et_al_2013]: https://www.jair.org/index.php/jair/article/view/10819
[research_bellemare_et_al_2016]: https://papers.nips.cc/paper/2016/hash/afda332245e2af431fb7b672a68b659d-Abstract.html
[research_bengio_et_al_2009]: https://dl.acm.org/doi/10.1145/1553374.1553380
[research_berner_et_al_2019]: https://arxiv.org/abs/1912.06680
[research_bommasani_et_al_2021]: https://arxiv.org/abs/2108.07258
[research_brown_et_al_2020]: https://papers.nips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html
[research_brown_sandholm_2018]: https://www.science.org/doi/10.1126/science.aao1733
[research_casper_et_al_2023]: https://arxiv.org/abs/2307.15217
[research_cepeda_et_al_2008]: https://journals.sagepub.com/doi/10.1111/j.1467-9280.2008.02209.x
[research_chaudhry_et_al_2019]: https://arxiv.org/abs/1812.00420
[research_christiano_et_al_2017]: https://papers.nips.cc/paper/2017/hash/d5e2c0adad503c91f91df240d0cd4e49-Abstract.html
[research_christiano_shlegeris_amodei_2018]: https://arxiv.org/abs/1810.08575
[research_cobbe_et_al_2020]: https://proceedings.mlr.press/v119/cobbe20a.html
[research_crick_1989]: https://www.nature.com/articles/337129a0
[research_dabney_et_al_2018_iqn]: https://proceedings.mlr.press/v80/dabney18a.html
[research_dabney_et_al_2018_qr_dqn]: https://ojs.aaai.org/index.php/AAAI/article/view/11791
[research_daw_niv_dayan_2005]: https://www.nature.com/articles/nn1560
[research_dayan_1993]: https://direct.mit.edu/neco/article-abstract/5/4/613/5786
[research_dayan_hinton_1993]: https://papers.nips.cc/paper/1992/hash/d14220ee66aeec73c49038385428ec4c-Abstract.html
[research_deisenroth_rasmussen_2011]: https://dl.acm.org/doi/10.5555/3104482.3104541
[research_dietterich_2000]: https://www.jair.org/index.php/jair/article/view/10266
[research_duan_et_al_2016]: https://arxiv.org/abs/1611.02779
[research_finn_abbeel_levine_2017]: https://proceedings.mlr.press/v70/finn17a.html
[research_foster_wilson_2006]: https://www.nature.com/articles/nature04587
[research_friston_2010]: https://www.nature.com/articles/nrn2787
[research_fujimoto_hoof_meger_2018]: https://proceedings.mlr.press/v80/fujimoto18a.html
[research_fujimoto_meger_precup_2019]: https://proceedings.mlr.press/v97/fujimoto19a.html
[research_gao_schulman_hilton_2023]: https://proceedings.mlr.press/v202/gao23h.html
[research_ha_schmidhuber_2018]: https://papers.nips.cc/paper/2018/hash/2de5d16682c3c35007e4e92982f1a2ba-Abstract.html
[research_haarnoja_et_al_2018]: https://proceedings.mlr.press/v80/haarnoja18b.html
[research_hafner_et_al_2020]: https://arxiv.org/abs/1912.01603
[research_hafner_et_al_2023]: https://arxiv.org/abs/2301.04104
[research_hafting_et_al_2005]: https://www.nature.com/articles/nature03721
[research_henderson_et_al_2018]: https://ojs.aaai.org/index.php/AAAI/article/view/11694
[research_ho_ermon_2016]: https://papers.nips.cc/paper/2016/hash/cc7e2b878868cbae992d1fb743995d8f-Abstract.html
[research_hoffmann_et_al_2022]: https://arxiv.org/abs/2203.15556
[research_houthooft_et_al_2016]: https://papers.nips.cc/paper/2016/hash/abd815286ba1007abfbb8415b83ae2cf-Abstract.html
[research_hubinger_et_al_2019]: https://arxiv.org/abs/1906.01820
[research_irving_christiano_amodei_2018]: https://arxiv.org/abs/1805.00899
[research_jumper_et_al_2021]: https://www.nature.com/articles/s41586-021-03819-2
[research_kahneman_tversky_1979]: https://www.jstor.org/stable/1914185
[research_kakade_2003]: https://homepages.inf.ed.ac.uk/csutton/publications/kakade-thesis.pdf
[research_kaplan_et_al_2020]: https://arxiv.org/abs/2001.08361
[research_kemp_tenenbaum_2008]: https://www.pnas.org/doi/10.1073/pnas.0802631105
[research_khaligh_razavi_kriegeskorte_2014]: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003915
[research_kirkpatrick_et_al_2017]: https://www.pnas.org/doi/10.1073/pnas.1611835114
[research_klyubin_polani_nehaniv_2005]: https://ieeexplore.ieee.org/document/1554676
[research_kostrikov_nair_levine_2022]: https://arxiv.org/abs/2110.06169
[research_krakovna_et_al_2020]: https://deepmind.google/discover/blog/specification-gaming-the-flip-side-of-ai-ingenuity/
[research_kriegeskorte_mur_bandettini_2008]: https://www.frontiersin.org/articles/10.3389/neuro.06.004.2008/full
[research_kumar_et_al_2020]: https://papers.nips.cc/paper/2020/hash/0d2b2061826a5df3221116a5085a6052-Abstract.html
[research_kumaran_mcclelland_hassabis_2016]: https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(16)30043-2
[research_kuttler_et_al_2020]: https://papers.nips.cc/paper/2020/hash/569ff987c643b4bedf504efda8f786c2-Abstract.html
[research_lai_robbins_1985]: https://www.sciencedirect.com/science/article/pii/0196885885900028
[research_lazic_et_al_2018]: https://papers.nips.cc/paper/2018/hash/059fdcd96baeb75112f09fa1dcc740cc-Abstract.html
[research_lee_zhang_fischer_bengio_2015]: https://link.springer.com/chapter/10.1007/978-3-319-23528-8_31
[research_lehman_stanley_2011]: https://direct.mit.edu/evco/article-abstract/19/2/189/1365
[research_levine_et_al_2020]: https://arxiv.org/abs/2005.01643
[research_lillicrap_et_al_2015]: https://arxiv.org/abs/1509.02971
[research_lillicrap_et_al_2016]: https://www.nature.com/articles/ncomms13276
[research_lillicrap_et_al_2020]: https://www.nature.com/articles/s41583-020-0277-3
[research_lin_1992]: https://link.springer.com/article/10.1007/BF00992699
[research_lopez_paz_ranzato_2017]: https://papers.nips.cc/paper/2017/hash/f87522788a2be2d171666752f97ddebb-Abstract.html
[research_manheim_garrabrant_2018]: https://arxiv.org/abs/1803.04585
[research_mcclelland_mcnaughton_oreilly_1995]: https://psycnet.apa.org/doi/10.1037/0033-295X.102.3.419
[research_mirhoseini_et_al_2021]: https://www.nature.com/articles/s41586-021-03544-w
[research_mnih_et_al_2015]: https://www.nature.com/articles/nature14236
[research_mnih_et_al_2016]: https://proceedings.mlr.press/v48/mniha16.html
[research_moravcik_et_al_2017]: https://www.science.org/doi/10.1126/science.aam6960
[research_mouret_clune_2015]: https://arxiv.org/abs/1504.04909
[research_ng_russell_2000]: https://ai.stanford.edu/~ang/papers/icml00-irl.pdf
[research_ngo_chan_mindermann_2022]: https://arxiv.org/abs/2209.00626
[research_nosofsky_1986]: https://psycnet.apa.org/doi/10.1037/0096-3445.115.1.39
[research_okeefe_dostrovsky_1971]: https://www.sciencedirect.com/science/article/pii/0006899371903581
[research_openended_team_2021]: https://arxiv.org/abs/2107.12808
[research_oregan_noe_2001]: https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/sensorimotor-account-of-vision-and-visual-consciousness/1B49A6F4EA76ECBD0938815EEE18C7DC
[research_osband_et_al_2020]: https://openreview.net/forum?id=rygf-kSYwH
[research_osc_2015]: https://www.science.org/doi/10.1126/science.aac4716
[research_ouyang_et_al_2022]: https://papers.nips.cc/paper_files/paper/2022/hash/b1efde53be364a73914f58805a001731-Abstract-Conference.html
[research_pathak_et_al_2017]: https://proceedings.mlr.press/v70/pathak17a.html
[research_rao_ballard_1999]: https://www.nature.com/articles/nn0199_79
[research_rescorla_wagner_1972]: https://scholar.google.com/scholar?q=rescorla+wagner+1972+theory+pavlovian+conditioning
[research_roediger_karpicke_2006]: https://journals.sagepub.com/doi/10.1111/j.1467-9280.2006.01693.x
[research_rosch_1975]: https://psycnet.apa.org/doi/10.1037/0096-3445.104.3.192
[research_roy_duckett_2022]: https://arxiv.org/abs/2103.03356
[research_rummery_niranjan_1994]: https://www.researchgate.net/publication/2500611_On-Line_Q-Learning_Using_Connectionist_Systems
[research_rusu_et_al_2016]: https://arxiv.org/abs/1606.04671
[research_salimans_et_al_2017]: https://arxiv.org/abs/1703.03864
[research_schrimpf_et_al_2020]: https://www.cell.com/neuron/fulltext/S0896-6273(20)30605-X
[research_schrittwieser_et_al_2020]: https://www.nature.com/articles/s41586-020-03051-4
[research_schulman_et_al_2015]: https://proceedings.mlr.press/v37/schulman15.html
[research_schulman_et_al_2017]: https://arxiv.org/abs/1707.06347
[research_schultz_dayan_montague_1997]: https://www.science.org/doi/10.1126/science.275.5306.1593
[research_shin_et_al_2017]: https://papers.nips.cc/paper/2017/hash/0efbe98067c6c73dba1250d2beaa81f9-Abstract.html
[research_silver_et_al_2014]: https://proceedings.mlr.press/v32/silver14.html
[research_silver_et_al_2016]: https://www.nature.com/articles/nature16961
[research_silver_et_al_2017]: https://www.nature.com/articles/nature24270
[research_silver_et_al_2018]: https://www.science.org/doi/10.1126/science.aar6404
[research_silver_et_al_2021]: https://www.sciencedirect.com/science/article/pii/S0004370221000862
[research_silver_sutton_2024]: https://storage.googleapis.com/deepmind-media/Era-of-Experience%20/The%20Era%20of%20Experience%20Paper.pdf
[research_stachenfeld_botvinick_gershman_2017]: https://www.nature.com/articles/nn.4650
[research_stanley_miikkulainen_2002]: https://direct.mit.edu/evco/article/10/2/99/1123
[research_stiennon_et_al_2020]: https://papers.nips.cc/paper/2020/hash/1f89885d556929e98d3ef9b86448f951-Abstract.html
[research_strehl_li_littman_2009]: https://jmlr.org/papers/v10/strehl09a.html
[research_sutton_1988]: https://link.springer.com/article/10.1007/BF00115009
[research_sutton_1991]: https://dl.acm.org/doi/10.1145/122344.122377
[research_sutton_2019_bitter_lesson]: http://www.incompleteideas.net/IncIdeas/BitterLesson.html
[research_sutton_et_al_2000]: https://papers.nips.cc/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html
[research_sutton_precup_singh_1999]: https://www.sciencedirect.com/science/article/pii/S0004370299000521
[research_tenenbaum_et_al_2011]: https://www.science.org/doi/10.1126/science.1192788
[research_thompson_1933]: https://www.jstor.org/stable/2332286
[research_todorov_erez_tassa_2012]: https://ieeexplore.ieee.org/document/6386109
[research_turner_et_al_2021]: https://papers.nips.cc/paper/2021/hash/c26820b8a4c1b3c2aa868d6d57e14a79-Abstract.html
[research_van_hasselt_et_al_2018]: https://arxiv.org/abs/1812.02648
[research_van_hasselt_guez_silver_2016]: https://ojs.aaai.org/index.php/AAAI/article/view/10295
[research_van_seijen_et_al_2009]: https://ieeexplore.ieee.org/document/4927542
[research_vezhnevets_et_al_2017]: https://proceedings.mlr.press/v70/vezhnevets17a.html
[research_vinyals_et_al_2019]: https://www.nature.com/articles/s41586-019-1724-z
[research_wang_et_al_2016]: https://arxiv.org/abs/1611.05763
[research_wang_et_al_2016_dueling]: https://proceedings.mlr.press/v48/wangf16.html
[research_wang_lehman_clune_stanley_2019]: https://arxiv.org/abs/1901.01753
[research_watkins_1989]: https://www.cs.rhul.ac.uk/~chrisw/new_thesis.pdf
[research_watkins_dayan_1992]: https://link.springer.com/article/10.1007/BF00992698
[research_wei_et_al_2022_cot]: https://papers.nips.cc/paper_files/paper/2022/hash/9d5609613524ecf4f15af0f7b31abca4-Abstract-Conference.html
[research_wei_et_al_2022_emergent]: https://openreview.net/forum?id=yzkSU5zdwD
[research_weng_et_al_2001]: https://www.science.org/doi/10.1126/science.291.5504.599
[research_whittington_bogacz_2017]: https://direct.mit.edu/neco/article-abstract/29/5/1229/8261
[research_williams_1992]: https://link.springer.com/article/10.1007/BF00992696
[research_wilson_mcnaughton_1994]: https://www.science.org/doi/10.1126/science.8036517
[research_yamins_et_al_2014]: https://www.pnas.org/doi/10.1073/pnas.1403112111
[research_yu_et_al_2020]: https://proceedings.mlr.press/v100/yu20a.html
[research_zador_et_al_2023]: https://www.nature.com/articles/s41467-023-37180-x
[research_ziebart_et_al_2008]: https://cdn.aaai.org/AAAI/2008/AAAI08-227.pdf
