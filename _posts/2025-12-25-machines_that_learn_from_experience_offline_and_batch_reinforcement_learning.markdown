---
layout: post
mathjax: true
comments: true
title:  "Machines That Learn From Experience: Offline and Batch Reinforcement Learning"
date:   2025-12-25 00:00:00 +0000
categories: artificial-intelligence machine-learning neuroscience
series: machines_that_learn_from_experience
series_title: Machines That Learn From Experience
series_index: 8
---

<!-- A257 -->
<script>console.log("A257");</script>

Offline reinforcement learning treats the problem of learning a policy from a fixed dataset of previously-collected experience without any further environment interaction. The setting is central to reinforcement learning's applied deployment because many domains including healthcare, education, industrial control, autonomous driving, and recommendation systems admit either large historical logs or limited online experimentation budgets, and effective offline algorithms permit meaningful policy improvement from such data. The theoretical and algorithmic challenges are considerable. Distributional shift between the data-generating behavior policy and the target policy invalidates the naive application of off-policy methods, and standard Q-learning-with-bootstrapping under function approximation produces value overestimation that compounds catastrophically when propagated through Bellman updates. The offline reinforcement learning literature has developed a distinctive set of algorithmic responses including importance sampling with variance control, behavior regularization, conservative Q-learning, uncertainty-aware methods, sequence-modeling reformulations, diffusion-based policies, and model-based approaches that share the aim of controlling exploitation of the model beyond its data coverage. This article surveys the science and theory of offline reinforcement learning as it stands in the mid 2020s, covering the foundational importance-sampling machinery of Precup Sutton and Singh, the modern policy-constraint and conservative-value families, the sequence-modeling reformulations that recast offline reinforcement learning as autoregressive prediction, the pessimism-based sample complexity theory, and the empirical landscape of D4RL and RL Unplugged benchmarks. Articles two through seven treated online reinforcement learning across model-free and model-based frameworks, this article treats the offline counterpart.

## The Offline Reinforcement Learning Problem

The offline reinforcement learning problem is specified by a fixed dataset

$$
\mathcal{D} = \{(s_i, a_i, r_i, s'_i)\}_{i=1}^N
\tag{1}
$$

collected under some behavior policy $\mu$ or mixture of policies. The learner does not interact with the environment during training and must produce a policy that performs well when subsequently deployed. The behavior policy $\mu$ is generally unknown, though its samples are observed through the action selections in $\mathcal{D}$.

The offline setting differs fundamentally from the online setting in that the state-action distribution induced by any candidate policy $\pi$ may differ considerably from the state-action distribution in $\mathcal{D}$. Let $d^\pi(s, a)$ denote the discounted state-action occupancy under policy $\pi$,

$$
d^\pi(s, a) = (1 - \gamma) \sum_{t=0}^{\infty} \gamma^t \Pr(s_t = s, a_t = a \mid s_0 \sim \mu_0, \pi)
\tag{2}
$$

and let $d^\mu$ denote the corresponding occupancy under the behavior policy. The distributional shift between $\pi$ and the offline data is captured by the ratio

$$
w(s, a) = \frac{d^\pi(s, a)}{d^\mu(s, a)}
\tag{3}
$$

which becomes unbounded or infinite when $\pi$ visits states or takes actions not covered by $\mu$. When $\pi$ visits states or takes actions poorly covered by $\mathcal{D}$, the learned value estimates or reward predictions at those states are unreliable, and policies that exploit such unreliable estimates typically fail catastrophically at deployment.

Batch reinforcement learning of [Lange et al. 2012][research_lange_gabel_riedmiller_2012] provided the earlier framing of the offline problem, treating it as a supervised-learning-style pipeline in which policy learning proceeds through repeated batch updates on the fixed dataset. Contemporary offline reinforcement learning inherits this framing but has developed significantly richer algorithmic responses to the distributional shift problem than the early batch methods provided.

The offline reinforcement learning problem is well-motivated by practical applications. Healthcare records, industrial control logs, autonomous driving demonstrations, recommendation system click logs, and educational tutoring transcripts all provide large fixed datasets from which improved policies could in principle be learned. The gap between the theoretical potential and the practical realization has driven much of the field's recent development.

## Historical Development

Offline reinforcement learning as a distinct field emerged in the late 2010s from the confluence of several precursor threads. Batch reinforcement learning of Lange Gabel and Riedmiller 2012 provided the earlier framing. Off-policy evaluation of [Precup et al. 2000][research_precup_sutton_singh_2000_offline] provided the importance-sampling machinery for estimating policy values from behavior-policy data. Fitted Q iteration of [Ernst et al. 2005][research_ernst_geurts_wehenkel_2005_offline] provided the algorithmic template for batch value iteration with function approximation. The earlier Neural Fitted Q Iteration of [Riedmiller 2005][research_riedmiller_2005_nfq] adapted the framework to neural function approximation and provided the direct precursor to modern deep offline reinforcement learning. Stable function approximation for dynamic programming of [Gordon 1995][research_gordon_1995] and residual algorithms of [Baird 1995][research_baird_1995] provided the theoretical foundations for the value-function stability problems that would later manifest as the deadly triad in offline settings. The [Antos et al. 2007][research_antos_szepesvari_munos_2008] finite-sample analysis of fitted policy iteration provided one of the first rigorous sample complexity treatments of batch reinforcement learning under function approximation.

The deeper roots trace to the foundational reinforcement learning theory of [Watkins 1989][research_watkins_1989_thesis] doctoral thesis introducing Q-learning as a stochastic approximation to Bellman optimality, [Sutton 1988][research_sutton_1988_td] temporal difference learning that established the incremental value-updating framework used across all subsequent methods, and the [Bertsekas and Tsitsiklis 1996][book_bertsekas_tsitsiklis_1996] Neuro-Dynamic Programming monograph that consolidated the theoretical treatment of reinforcement learning with function approximation. These earlier works framed the questions of stability and convergence that offline reinforcement learning subsequently inherited under the more severe distributional shift regime.

The QT-Opt system of [Kalashnikov 2018][research_kalashnikov_et_al_2018] demonstrated that large-scale offline reinforcement learning could produce competitive robotic grasping policies from logged demonstrations combined with limited online experience, providing empirical validation that offline reinforcement learning at scale could work in practice.

The distributional-shift problem was crystallized in [Fujimoto et al. 2019][research_fujimoto_meger_precup_2019] Batch-Constrained deep Q-learning (BCQ), which documented the value-overestimation catastrophe of standard Q-learning under offline data and proposed a policy-constraint response. [Kumar Fu Tucker Levine 2019][research_kumar_et_al_2019_bear] Bootstrapping Error Accumulation Reduction (BEAR) developed a complementary policy-constraint framework using maximum mean discrepancy.

The [Levine et al. 2020][research_levine_et_al_2020] tutorial and survey consolidated the field, positioning distributional shift as the central problem and surveying the emerging algorithmic responses. [Kumar Zhou Tucker Levine 2020][research_kumar_zhou_tucker_levine_2020] Conservative Q-Learning (CQL) provided a distinctive value-based response that has become the most widely-used baseline. [Fujimoto and Gu 2021][research_fujimoto_gu_2021] TD3+BC provided a minimalist policy-constraint alternative that achieves competitive performance with substantially simpler implementation.

The 2020s produced a diversification of algorithmic approaches including uncertainty-aware methods, sequence-modeling reformulations through Decision Transformer treated in article four, diffusion-based policies, and model-based methods treated in article seven. The theoretical understanding of offline reinforcement learning through the pessimism framework matured markedly through work including [Xie et al. 2021][research_xie_et_al_2021], [Rashidinejad et al. 2021][research_rashidinejad_et_al_2021], and [Jin et al. 2021][research_jin_yang_wang_2021].

## The Distributional Shift Problem

The distributional shift problem is the central difficulty of offline reinforcement learning. Standard Q-learning under function approximation produces value overestimation when applied to off-policy data because the max operator in the Bellman target,

$$
y = r + \gamma \max_{a'} Q(s', a')
\tag{4}
$$

extrapolates the Q-function to actions that may be poorly represented in the dataset. If $\hat{Q}$ has estimation noise with variance $\sigma^2$ at each action, the expected max is systematically biased upward by

$$
\mathbb{E}[\max_a \hat{Q}(s, a)] - \max_a Q^*(s, a) \geq c(|\mathcal{A}|) \sigma
\tag{5}
$$

where $c(\lvert \mathcal{A} \rvert)$ grows with the action space size, capturing the Jensen-gap for the max operator over noisy estimates. When $Q$ overestimates value at such actions, the Bellman update propagates the overestimation to predecessor states, and the compounding error catastrophically destroys value estimates over many training iterations.

The problem is fundamental to Q-learning-with-function-approximation combined with off-policy data, and does not arise for on-policy methods or for exact-Q-learning in tabular settings. It manifests through two mechanisms. First, the max operator selects actions with the highest predicted Q-value, and these are systematically the actions where the function approximator has extrapolated most incorrectly. Second, the Bellman update propagates these overestimated targets through the value function via bootstrapping, amplifying the error. The maximization bias was documented for tabular Q-learning by [Thrun and Schwartz 1993][research_thrun_schwartz_1993] and formally addressed by [van Hasselt 2010][research_van_hasselt_2010] Double Q-learning, both of which anticipated the more severe offline manifestation. The [Kumar et al. 2021a][research_kumar_et_al_2021_dr3] DR3 analysis provided the mechanistic account of implicit under-regularization in offline Q-learning through examination of feature co-adaptation and rank collapse.

The [Fujimoto et al. 2019][research_fujimoto_meger_precup_2019] BCQ paper diagnosed the problem experimentally by showing that flat DQN and DDPG applied to offline datasets produce policies with dramatically inflated Q-values that predict much better performance than the policies actually achieve. The gap between predicted and achieved performance grows without bound during training under standard Q-learning. Complementary analyses by [Fu et al. 2019][research_fu_et_al_2019_divergence] documented divergence in deep Q-learning on off-policy data and identified the interaction between neural function approximation and target-network staleness as a driver of the observed instability.

Formally, the deadly-triad analysis of article three (off-policy learning + function approximation + bootstrapping) directly implies the risk of divergence in the offline setting. Online algorithms escape this risk in practice through mechanisms including exploration that keeps the data distribution reasonably aligned with the current policy, target networks that stabilize bootstrapping, and gradient corrections. Offline algorithms cannot rely on exploration to correct their distribution and must resort to explicit regularization to control extrapolation.

Behavior-cloned baselines that simply imitate the behavior policy avoid distributional shift by construction but forfeit policy improvement. The tension between imitation (safe but limited) and improvement (potentially beneficial but risky) organizes the algorithmic landscape of offline reinforcement learning.

## Behavior Cloning and Weighted Imitation Baselines

Behavior cloning (BC) provides the simplest baseline for offline reinforcement learning by treating the problem as supervised learning of the behavior policy,

$$
L_{\text{BC}}(\pi_\theta) = -\mathbb{E}_{(s, a) \sim \mathcal{D}}\!\left[\log \pi_\theta(a \mid s)\right]
\tag{6}
$$

which produces a policy that approximates $\mu$ without any policy improvement. The [Pomerleau 1988][research_pomerleau_1988_alvinn] ALVINN autonomous driving system provided one of the earliest demonstrations of behavior cloning at deployment scale, training a neural network to steer from expert demonstrations. The [Bain and Sammut 1995][research_bain_sammut_1995] and subsequent behavior cloning literature established the account in imitation learning, and its application to offline reinforcement learning provides a lower bound on the performance any real offline algorithm should exceed.

The DAgger framework of [Ross Gordon Bagnell 2011][research_ross_gordon_bagnell_2011] addressed a critical failure mode of pure behavior cloning. The compounding error under sequential deployment produces state distributions divergent from the training data. DAgger requires online queries to the expert and does not apply to the fully offline setting, but its analysis of covariate shift underlies much of the offline literature. Generative Adversarial Imitation Learning of [Ho and Ermon 2016][research_ho_ermon_2016_gail] provided an alternative that matches occupancy distributions rather than actions, extending the imitation learning framework to a maximum-entropy inverse reinforcement learning formulation. Behavioral Cloning from Observation of [Torabi et al. 2018][research_torabi_warnell_stone_2018] extended the model to the setting where only state observations are available without action labels, addressing a common condition in medical and industrial data. Dexterous manipulation from demonstrations of [Rajeswaran et al. 2017][research_rajeswaran_et_al_2018_dapg] combined behavior cloning with policy gradient improvement (DAPG) and provided one of the earliest sim-to-real demonstrations of this formulation on high-dimensional manipulation tasks.

Advantage-weighted regression of [Peng et al. 2019][research_peng_kumar_zhang_levine_2019] combines behavior cloning with implicit policy improvement through exponentiated-advantage weighting,

$$
L_{\text{AWR}}(\pi_\theta) = -\mathbb{E}_{(s, a) \sim \mathcal{D}}\!\left[\exp(A(s, a) / \beta) \log \pi_\theta(a \mid s)\right]
\tag{7}
$$

analogously to AWAC treated later. The mechanism produces policies that lie in the neighborhood of the behavior policy but weighted toward higher-advantage actions, providing modest policy improvement without value-function machinery.

Critic Regularized Regression (CRR) of [Wang 2020][research_wang_et_al_2020_crr] extends the treatment with a value-function-based advantage estimator, providing improved performance across the D4RL benchmark. RL via Supervised Learning (RvS) of [Emmons Eysenbach Kostrikov Levine 2021][research_emmons_et_al_2021] documented the surprising performance of pure conditional imitation combined with return-to-go conditioning, connecting to the Decision Transformer framework treated later.

The behavior-cloning-plus-conditioning family provides a practical alternative to value-based offline RL for tasks where the behavior policy is already reasonable and the required improvement is modest. When the required improvement is significant or the behavior policy is poor, value-based methods with explicit distributional shift handling become necessary.

## Off-Policy Evaluation via Importance Sampling

Off-policy evaluation (OPE) is the sub-problem of estimating the value of a target policy $\pi$ from data collected under a behavior policy $\mu$. It provides both a diagnostic tool for offline reinforcement learning and an application in its own right where practitioners want to estimate the value of candidate policies without deploying them.

The importance-sampling estimator of [Precup et al. 2000][research_precup_sutton_singh_2000_offline] applies importance-sampling ratios to trajectories, with the [Precup et al. 2001][research_precup_sutton_dasgupta_2001] extension covering off-policy temporal difference learning with function approximation,

$$
\hat{V}^\pi_{\text{IS}} = \frac{1}{N} \sum_{i=1}^N \rho_{0:T_i-1}^{(i)} G^{(i)}
\tag{8}
$$

where $G^{(i)}$ is the return of trajectory $i$ and $\rho_{0:T-1}$ is the trajectory-level importance-sampling ratio

$$
\rho_{0:T-1} = \prod_{t=0}^{T-1} \frac{\pi(a_t \mid s_t)}{\mu(a_t \mid s_t)}
\tag{9}
$$

The estimator is unbiased under mild conditions but has variance that grows exponentially with trajectory length in the worst case, making it impractical for long-horizon problems.

Per-decision importance sampling reduces variance by exploiting the trajectory structure,

$$
\hat{V}^\pi_{\text{PDIS}} = \frac{1}{N} \sum_{i=1}^N \sum_{t=0}^{T_i-1} \gamma^t \rho_{0:t}^{(i)} r_{t+1}^{(i)}
\tag{10}
$$

using only the prefix importance-sampling ratio up to each reward.

Weighted importance sampling normalizes by the sum of importance-sampling ratios,

$$
\hat{V}^\pi_{\text{WIS}} = \frac{\sum_i \rho_{0:T_i-1}^{(i)} G^{(i)}}{\sum_i \rho_{0:T_i-1}^{(i)}}
\tag{11}
$$

trading bias for reduced variance. The weighted estimator is consistent under standard conditions and is generally preferred in practice.

Doubly robust estimators of [Jiang and Li 2016][research_jiang_li_2016_offline] and [Thomas and Brunskill 2016][research_thomas_brunskill_2016] combine importance sampling with a learned Q-function baseline. More Robust Doubly Robust of [Farajtabar Chow Ghavamzadeh 2018][research_farajtabar_chow_ghavamzadeh_2018] provided the extended variant with reduced variance in high-dimensional settings. The optimal off-policy evaluation framework of [Xie et al. 2019][research_xie_ma_wang_2019_optimal] established minimax-optimal marginalized importance sampling with matching upper and lower sample-complexity bounds. The Bootstrapping Off-Policy Evaluation of [Hanna et al. 2016][research_hanna_stone_niekum_2017] introduced bootstrap confidence intervals for off-policy evaluation, providing distributional uncertainty rather than point estimates.

The doubly robust framework is defined by

$$
\hat{V}^\pi_{\text{DR}} = \frac{1}{N} \sum_{i=1}^N \sum_{t=0}^{T_i-1} \gamma^t \left[\rho_{0:t}^{(i)} \left(r_{t+1}^{(i)} - \hat{Q}(s_t^{(i)}, a_t^{(i)})\right) + \rho_{0:t-1}^{(i)} \hat{V}(s_t^{(i)})\right]
\tag{12}
$$

which is unbiased if either the importance-sampling weights or the value baseline is correct, providing robustness to specification errors.

Marginalized importance sampling methods including DualDICE of [Nachum et al. 2019][research_nachum_et_al_2019_dualdice] and its extensions bypass the trajectory-level variance explosion by estimating the marginal state-action distribution ratio rather than the trajectory-level ratio. The [Liu et al. 2018][research_liu_li_tang_zhou_2018] Breaking the Curse of Horizon framework provided the initial theoretical treatment of marginal importance sampling and established the polynomial-horizon guarantee. Retrace of [Munos et al. 2016][research_munos_et_al_2016_retrace] introduced truncated importance ratios that provide safe and efficient off-policy multi-step return estimation. Minimax weight learning of [Uehara et al. 2020][research_uehara_huang_jiang_2020] provided a unified framework for marginal importance sampling with function approximation, and the [Kallus and Uehara 2020][research_kallus_uehara_2020] framework provided efficient double reinforcement learning bounds for off-policy evaluation. The DualDICE objective solves the min-max problem

$$
\min_v \max_\zeta \, \mathbb{E}_{(s, a) \sim d^\mu}\!\left[f(\zeta(s, a)) - \zeta(s, a) \cdot \mathcal{T}^\pi v(s, a)\right] + (1 - \gamma) \mathbb{E}_{s_0 \sim \mu_0, a_0 \sim \pi}\!\left[v(s_0, a_0)\right]
\tag{13}
$$

where $\mathcal{T}^\pi$ is the Bellman expectation operator under $\pi$ and $f$ is a convex function whose conjugate produces the correct estimator. The estimator achieves polynomial rather than exponential variance in the horizon, providing a foundation for practical long-horizon off-policy evaluation.

Fitted Q evaluation of [Le Voloshin Yue 2019][research_le_voloshin_yue_2019] iteratively fits a Q-function to observed data through the Bellman backup

$$
\hat{Q}_{k+1}(s, a) = \mathbb{E}_{(s', r) \sim \mathcal{D}}\!\left[r + \gamma \mathbb{E}_{a' \sim \pi}[\hat{Q}_k(s', a')]\right]
\tag{14}
$$

using only the actions actually taken in the dataset for the Bellman target, avoiding the max-operator extrapolation of Q-learning. The resulting value estimate is unbiased under standard concentrability conditions.

## Behavior-Regularized Methods

Behavior regularization approaches constrain the learned policy to remain close to the data-generating behavior policy, limiting distributional shift by construction. The general framework adds a divergence penalty to the standard policy objective,

$$
J_{\text{BR}}(\pi) = \mathbb{E}\!\left[Q(s, a)\right] - \alpha \, D(\pi(\cdot \mid s) \, \| \, \mu(\cdot \mid s))
\tag{15}
$$

where $D$ is a divergence measure and $\alpha$ controls the strength of the constraint.

BEAR of [Kumar Fu Tucker Levine 2019][research_kumar_et_al_2019_bear] uses the maximum mean discrepancy (MMD) between the learned policy and an estimated behavior policy,

$$
\text{MMD}^2(\pi, \mu) = \mathbb{E}_{a \sim \pi, a' \sim \pi}[k(a, a')] - 2 \mathbb{E}_{a \sim \pi, a' \sim \mu}[k(a, a')] + \mathbb{E}_{a \sim \mu, a' \sim \mu}[k(a, a')]
\tag{16}
$$

for a kernel $k$, and constrains the policy to satisfy $\text{MMD}(\pi, \mu) \leq \epsilon$.

BRAC of [Wu et al. 2019][research_wu_tucker_nachum_2019] systematically evaluated KL, MMD, and Wasserstein divergences for policy regularization, providing a unified empirical framework that documented the practical performance of alternative divergence choices. Way Off-Policy of [Jaques et al. 2019][research_jaques_et_al_2019] applied KL-constrained policy learning to offline reinforcement learning from human-human dialogue transcripts, providing a direct precursor to the RLHF-style methods that would become standard for language model post-training. Advantage-Weighted Behavior Models (ABM) of [Siegel et al. 2020][research_siegel_et_al_2020_abm] combined behavior modeling with advantage weighting under a KL constraint, achieving strong performance on the DeepMind Control Suite offline benchmarks.

TD3+BC of [Fujimoto and Gu 2021][research_fujimoto_gu_2021] provided a minimalist approach that adds a behavior cloning term to the TD3 policy objective,

$$
J_{\text{TD3+BC}}(\pi) = \mathbb{E}\!\left[Q(s, \pi(s))\right] - \lambda \mathbb{E}_{(s, a) \sim \mathcal{D}}\!\left[\|\pi(s) - a\|^2\right]
\tag{17}
$$

with adaptive weighting $\lambda$ based on the Q-value scale. The simplicity of the approach combined with competitive empirical performance has made TD3+BC a widely-used baseline.

Advantage-Weighted Actor Critic (AWAC) of [Nair et al. 2020][research_nair_et_al_2020_awac] takes a weighted-behavior-cloning approach in which the policy is trained to imitate the advantage-weighted behavior distribution,

$$
\pi^*(a \mid s) \propto \mu(a \mid s) \exp(A(s, a) / \beta)
\tag{18}
$$

using an implicit constraint on the KL divergence from the behavior policy. The AWAC gradient minimizes the KL-constrained cross-entropy,

$$
\nabla_\theta L_{\text{AWAC}}(\theta) = -\mathbb{E}_{(s, a) \sim \mathcal{D}}\!\left[\exp\!\left(A^{\pi_k}(s, a) / \beta\right) \nabla_\theta \log \pi_\theta(a \mid s)\right]
\tag{19}
$$

which reweights the standard behavior-cloning gradient by the exponentiated advantage of each dataset action. AWAC has proved particularly effective for offline-to-online fine-tuning discussed later.

Implicit Q-Learning (IQL) of [Kostrikov Nair Levine 2022][research_kostrikov_nair_levine_2022] avoids the Q-value overestimation problem by fitting the value function via expectile regression,

$$
L_{\text{IQL}}(V) = \mathbb{E}_{(s, a) \sim \mathcal{D}}\!\left[L_2^\tau(Q_{\text{target}}(s, a) - V(s))\right]
\tag{20}
$$

with expectile loss $L_2^\tau(u) = \lvert \tau - \mathbb{1}\{u < 0\} \rvert u^2$ for expectile $\tau \in (0, 1)$. The Q-function is updated with respect to the fitted value baseline,

$$
L_{\text{IQL}}(Q) = \mathbb{E}_{(s, a, r, s') \sim \mathcal{D}}\!\left[(r + \gamma V(s') - Q(s, a))^2\right]
\tag{21}
$$

and the policy is extracted via advantage-weighted regression analogous to AWAC. The mechanism approximates the max over actions in the dataset without requiring explicit policy evaluation on out-of-distribution actions.

## Conservative Q-Learning

Conservative Q-Learning (CQL) of [Kumar Zhou Tucker Levine 2020][research_kumar_zhou_tucker_levine_2020] provides a distinctive value-based response to the distributional shift problem. Rather than constraining the policy to remain near the behavior policy, CQL modifies the Q-learning objective to systematically underestimate value on out-of-distribution actions.

The CQL objective augments the standard Bellman error with a penalty term,

$$
L_{\text{CQL}}(Q) = \alpha \, \mathbb{E}_{s \sim \mathcal{D}}\!\left[\log \sum_a \exp(Q(s, a)) - \mathbb{E}_{a \sim \mu}[Q(s, a)]\right] + L_{\text{Bellman}}(Q)
\tag{22}
$$

where the first term is a per-state Q-value overhang penalty that becomes large when the learned Q-function assigns high value to actions not represented in the dataset. Under the CQL objective, actions in the dataset receive their Bellman-consistent value estimates while actions outside the dataset receive systematically lower value estimates, preventing policy exploitation of out-of-distribution Q-value overestimates.

The theoretical analysis of CQL shows that the learned Q-function provides a lower bound on the true Q-function of any policy sufficiently close to the dataset support. Formally, for the exact CQL solution $\hat{Q}$ under the tabular setting, the expected value under any policy $\pi$ satisfies

$$
\mathbb{E}_{a \sim \pi}\!\left[\hat{Q}(s, a)\right] \leq \mathbb{E}_{a \sim \pi}\!\left[Q^\pi(s, a)\right]
\tag{23}
$$

with the bound tight when $\pi = \mu$ and increasingly loose as $\pi$ diverges from $\mu$. This pessimistic value estimation aligns with the pessimism-based sample complexity theory discussed later.

CQL has become the most widely-used offline reinforcement learning baseline. Its combination of theoretical guarantees, empirical competitiveness across benchmarks, and reasonable implementation complexity has made it the standard against which new methods are compared. Fisher-BRC of [Kostrikov et al. 2021][research_kostrikov_et_al_2021] provided a related conservative framework using Fisher divergence between the learned Q-function and behavior-consistent Q-values, achieving competitive performance with a distinct theoretical basis. Pessimistic Bootstrapping for uncertainty-aware offline reinforcement learning (PBRL) of [Bai et al. 2022][research_bai_et_al_2022_pbrl] combined bootstrapped Q-ensembles with pseudo out-of-distribution regularization, providing an alternative that explicitly models epistemic uncertainty. Support-constrained offline reinforcement learning of [Wu et al. 2022][research_wu_sun_sen_zhu_zhang_2022] formalized the connection between conservative Q-learning and support-set constraints, providing a unified analytical framework. Anti-Exploration by Random Network Distillation (ReBRAC) of [Tarasov et al. 2023b][research_nikulin_et_al_2023_rebrac] provided a systematic simplification of TD3+BC that achieves state-of-the-art performance across D4RL benchmarks with minimal architectural changes, and Robust Offline Reinforcement Learning (RORL) of [Yang et al. 2022][research_yang_et_al_2022_rorl] added smoothing regularization to combat perturbation sensitivity in the learned policy.

Extensions of CQL to model-based settings including COMBO of Yu Kumar Rafailov Rajeswaran Levine Finn 2021 treated in article seven combine conservative value estimation with model-based data augmentation.

## Uncertainty-Aware Offline Reinforcement Learning

Uncertainty-aware approaches use explicit uncertainty estimates in the Q-function to reduce reliance on unreliable value estimates at out-of-distribution states and actions. The general framework combines an ensemble of Q-networks with a penalty for high inter-ensemble disagreement. This account traces to Bootstrapped DQN of [Osband et al. 2016][research_osband_et_al_2016_bootstrapped_dqn] which introduced ensemble-based epistemic uncertainty for exploration, and to Deep Ensembles of [Lakshminarayanan et al. 2017][research_lakshminarayanan_pritzel_blundell_2017] which established ensemble uncertainty as a standard tool for out-of-distribution detection in supervised deep learning.

SAC-N of [An et al. 2021][research_an_et_al_2021] scales the SAC algorithm to use a large ensemble of $N$ Q-networks (typically $N = 10$ to $100$) and uses the min across the ensemble as the Q-value target,

$$
Q_{\text{target}}(s, a) = \min_{k=1, \ldots, N} Q_k(s, a)
\tag{24}
$$

The mechanism produces an implicit pessimism that scales with ensemble disagreement, providing state-of-the-art performance on D4RL benchmarks without explicit policy constraints or behavior regularization.

EDAC of An Moon Kim Song 2021 provides a diversity-encouraging regularization that pushes ensemble members apart in gradient space,

$$
L_{\text{EDAC}} = L_{\text{SAC-N}} + \eta \, \mathbb{E}\!\left[\sum_{k \neq k'} \frac{|\nabla_a Q_k^\top \nabla_a Q_{k'}|}{\|\nabla_a Q_k\| \|\nabla_a Q_{k'}\|}\right]
\tag{25}
$$

encouraging the ensemble members to disagree more strongly on out-of-distribution actions, amplifying the pessimism effect.

SAC-RND of [Ghasemipour Gu Nachum 2022][research_ghasemipour_gu_nachum_2022] uses random network distillation as an uncertainty proxy in place of Q-ensemble disagreement, providing a computationally cheaper alternative to large Q-ensembles with competitive performance. The lower-confidence-bound (LCB) formulation of pessimistic offline learning generalizes both approaches through

$$
Q_{\text{LCB}}(s, a) = \hat{Q}(s, a) - \beta \, \hat{\sigma}(s, a)
\tag{26}
$$

where $\hat{\sigma}(s, a)$ is an epistemic uncertainty estimate and $\beta$ scales the pessimism. Policy improvement against $Q_{\text{LCB}}$ produces provably-safe offline learning under standard concentrability conditions.

Random Ensemble Mixture of [Agarwal et al. 2020][research_agarwal_schuurmans_norouzi_2020] combined offline data with distributional RL, producing robust performance on Atari from purely offline logs. UWAC of [Wu et al. 2021][research_wu_et_al_2021_uwac] provided uncertainty-weighted actor-critic that adjusts the Bellman update magnitude based on epistemic uncertainty, providing an alternative pessimism mechanism to the min-over-ensemble approach. Randomized Ensembled Double Q-Learning (REDQ) of [Chen Wang Zhou Ross 2021][research_chen_wang_zhou_ross_2021_redq] documented that ensemble reduction with in-target minimization matches state-of-the-art without the large ensembles of SAC-N, providing computational efficiency at competitive performance.

Uncertainty-aware methods have proved competitive with and sometimes exceeding conservative Q-learning on standard benchmarks. Their computational cost from large Q-ensembles is substantial, but the algorithmic simplicity of the min-over-ensemble approach is attractive.

## Sequence Modeling and Transformer Approaches

Sequence modeling reformulations recast offline reinforcement learning as autoregressive prediction of trajectory tokens rather than as value learning or policy optimization. Article four's treatment of Decision Transformer, Trajectory Transformer, and Gato introduced the account. This section revisits the offline-analytical properties.

Decision Transformer of [Chen et al. 2021][research_chen_et_al_2021_dt] treated in article four predicts actions conditioned on states, previous actions, and target returns-to-go,

$$
\pi_\theta(a_t \mid s_{t-K:t}, a_{t-K:t-1}, \hat{R}_{t-K:t})
\tag{27}
$$

trained by the standard supervised cross-entropy loss on the offline dataset,

$$
L_{\text{DT}}(\theta) = -\mathbb{E}_{\tau \sim \mathcal{D}}\!\left[\sum_t \log \pi_\theta(a_t \mid s_{t-K:t}, a_{t-K:t-1}, \hat{R}_{t-K:t})\right]
\tag{28}
$$

The return-to-go conditioning provides an inference-time knob for policy specification. At test time the agent conditions on a chosen target return, producing actions consistent with achieving that return.

The sequence modeling approach avoids the distributional shift problem entirely by never fitting a value function or Bellman target. It also avoids the policy constraint machinery of the behavior regularization family. The trade-off is that the approach cannot in principle exceed the returns present in the training distribution, since it learns to imitate rather than to improve. Empirical results have mixed evidence on whether Decision Transformer actually achieves policy improvement or merely sophisticated imitation. The critical analysis of [Brandfonbrener et al. 2022][research_brandfonbrener_et_al_2022] documented that return-conditioned supervised learning provably fails to improve beyond the behavior policy in stochastic environments, providing the theoretical grounding for the empirical limitation.

Trajectory Transformer of [Janner et al. 2021][research_janner_li_levine_2021_tt] tokenizes state, action, and reward and uses beam search over the model to plan action sequences that maximize predicted return, providing a more explicit optimization step that can in principle exceed training-distribution returns.

Multi-Game Decision Transformer of [Lee 2022][research_lee_et_al_2022_mgdt] extended the model to a multi-task setting, and Gato of [Reed et al. 2022][research_reed_et_al_2022_gato_offline] to general-purpose multi-modal agents. Elastic Decision Transformer of [Wu Wang Reed Lee 2023][research_wu_wang_reed_lee_2023_edt] introduced adaptive context-length selection at inference time, enabling trajectory stitching that produces policies exceeding the best training trajectories in favorable regimes. Online Decision Transformer of [Zheng Zhang Grover 2022][research_zheng_zhang_grover_2022_odt] extended this formulation to the offline-to-online setting through a stochastic-policy formulation of return conditioning. Generalized Decision Transformer of [Furuta et al. 2022][research_furuta_matsuo_gu_2022_gdt] unified the family under the hindsight information matching framework, providing a principled account of the choice of return-to-go conditioning. Q-Transformer of [Chebotar et al. 2023][research_chebotar_et_al_2023_q_transformer] combined discrete action tokenization with autoregressive Q-value prediction to scale Q-learning to transformer-based architectures on real-robot manipulation tasks.

The relationship between sequence modeling and traditional value-based offline reinforcement learning remains an active research area. Empirical comparisons on D4RL benchmarks show comparable performance between the two families for tasks with marked data, with the sequence modeling family often outperforming on tasks with narrow data distributions where policy constraints are difficult to specify correctly.

## Diffusion-Based Offline Reinforcement Learning

Diffusion models have provided a distinctive class of offline reinforcement learning algorithms in the 2020s. The core observation is that the policy distribution $\pi(a \mid s)$ can be parameterized as a diffusion model conditional on state, providing extensive representation capacity for the multi-modal action distributions that arise in offline datasets collected from mixture policies. The underlying score-based generative modeling framework of [Sohl-Dickstein et al. 2015][research_sohl_dickstein_et_al_2015] and its practical realization in DDPM of [Ho Jain Abbeel 2020][research_ho_jain_abbeel_2020_ddpm] provided the generative modeling machinery that offline reinforcement learning subsequently adopted.

Diffuser of [Janner et al. 2022][research_janner_du_song_2022] provided the first systematic treatment, using diffusion over trajectory sequences rather than over per-state actions. The forward diffusion process progressively noises the trajectory $\tau$,

$$
q(\tau^{(k)} \mid \tau^{(k-1)}) = \mathcal{N}(\tau^{(k)} ; \sqrt{1 - \beta_k} \, \tau^{(k-1)}, \beta_k I)
\tag{29}
$$

and the reverse denoising process is learned by a neural network,

$$
p_\theta(\tau^{(k-1)} \mid \tau^{(k)}) = \mathcal{N}(\tau^{(k-1)} ; \mu_\theta(\tau^{(k)}, k), \Sigma_\theta(\tau^{(k)}, k))
\tag{30}
$$

The method treats planning as conditional generation, sampling trajectories from a diffusion model conditioned on start state and target reward through classifier-free or classifier guidance,

$$
\tilde{\mu}_\theta(\tau^{(k)}, k) = \mu_\theta(\tau^{(k)}, k) + \Sigma_\theta \, \nabla_{\tau^{(k)}} J(\tau^{(k)})
\tag{31}
$$

where $J$ is a reward-based guidance signal.

Diffusion Q-Learning of [Wang et al. 2022][research_wang_hunt_zhou_2022] uses a diffusion policy in a standard actor-critic setup, providing a drop-in replacement for the Gaussian policies of TD3 and SAC. The mechanism supports appreciably more expressive policies than Gaussian actors and has proved effective on multi-modal offline datasets.

Implicit Diffusion Q-Learning (IDQL) of [Hansen-Estruch et al. 2023][research_hansen_estruch_et_al_2023] combines diffusion policies with implicit Q-learning to avoid Q-value overestimation problems, producing state-of-the-art performance on D4RL benchmarks.

Consistency policies of [Chen et al. 2023][research_chen_xu_vella_zhou_2023] and related work extend the treatment with consistency-model policy parameterizations that permit faster action sampling than iterative diffusion, addressing a practical bottleneck of diffusion-based methods.

Decision Diffuser of [Ajay et al. 2023][research_ajay_et_al_2023_decision_diffuser] combines the trajectory-level diffusion approach with return conditioning analogous to Decision Transformer, providing a diffusion-based analog to the sequence modeling family. Diffusion Policy of [Chi et al. 2023][research_chi_et_al_2023_diffusion_policy] extended the framework to real-robot manipulation with sizable improvements over prior baselines on 12 different manipulation tasks. Efficient Diffusion Policies for offline reinforcement learning of [Kang et al. 2023][research_kang_yang_wang_2023_efficient_diffusion] addressed the inference-cost problem through single-step diffusion approximations that retain most of the policy expressiveness. Imitating Human Behaviour with Diffusion Models of [Pearce et al. 2023][research_pearce_et_al_2023] documented diffusion policy performance on human video game demonstrations, providing evidence for the account's applicability beyond robotic control. Contrastive Energy Prediction of [Lu et al. 2023][research_lu_et_al_2023_cep] introduced an energy-based-model perspective on diffusion policies that unifies score-based generation with policy improvement through classifier guidance.

The diffusion-based approaches trade computational cost at inference for policy expressiveness through iterative denoising steps. The empirical results suggest that the trade-off is favorable for tasks with sufficiently complex action distributions.

## Model-Based Offline Reinforcement Learning

Article seven treated model-based offline reinforcement learning at length. The core framework combines a learned dynamics model with policy optimization on model-generated rollouts, subject to conservative penalties that discount rollouts in regions where the model is uncertain.

MOPO of [Yu et al. 2020][research_yu_et_al_2020_mopo] and MOReL of [Kidambi et al. 2020][research_kidambi_et_al_2020_morel] provided the foundational methods with uncertainty-penalty rewards that penalize policy visits to high-uncertainty model regions. The MOPO penalty modifies the reward on model-based rollouts as

$$
\tilde{r}(s, a) = \hat{r}(s, a) - \lambda \, u(s, a)
\tag{32}
$$

where $u(s, a)$ is an epistemic uncertainty estimate from the model ensemble and $\lambda$ controls the trade-off between model exploitation and conservatism. COMBO of [Yu et al. 2021][research_yu_et_al_2021_combo] extended the model by combining model-based rollouts with the CQL conservative value objective, achieving state-of-the-art performance on many benchmarks.

RAMBO of [Rigter Lacerda Hawes 2022][research_rigter_lacerda_hawes_2022_rambo] introduced adversarial model training, in which the model is trained to be adversarially conservative against the policy, providing a more principled treatment of the policy-model interaction than uncertainty-penalty methods. MBOP of [Argenson and Dulac-Arnold 2020][research_argenson_dulac_arnold_2021_mbop] provided a model-based planning approach with behavior priors that avoids the value function machinery entirely. BREMEN of [Matsushima et al. 2021][research_matsushima_et_al_2021_bremen] proposed behavior-regularized model ensembles that combine trust-region policy optimization with imagination-based rollouts under a behavior policy constraint. LOMPO of [Rafailov et al. 2021][research_rafailov_et_al_2021_lompo] extended model-based offline reinforcement learning to visual observation spaces through latent-space uncertainty penalties, demonstrating this formulation's applicability to high-dimensional image inputs. MOBILE of [Sun et al. 2023][research_sun_et_al_2023_mobile] introduced a model-Bellman-inconsistency penalty that regularizes the learned model against value-inconsistent transitions, providing an alternative to reward-shaping approaches. Revisiting Design Choices of [Lu et al. 2021][research_lu_et_al_2022_design] provided a systematic empirical analysis of MOPO-family algorithms that identified reward normalization and rollout length as the dominant hyperparameters governing performance.

Model-based methods complement the model-free approaches surveyed above by leveraging the learned model to generate additional training data through simulated rollouts. The trade-off between the benefits of expanded data and the risks of model bias remains an active research area.

## Offline-to-Online Fine-Tuning

Offline-to-online fine-tuning treats the offline stage as pretraining and subsequently deploys the policy for limited online adaptation. The model combines the sample-efficiency benefits of offline learning with the ability to further improve during deployment.

The primary challenge is the policy-mismatch problem. The offline-trained policy may perform poorly at the start of online adaptation due to distributional shift, and standard online reinforcement learning updates may catastrophically forget the offline knowledge before the online data can produce improvement.

AWAC of Nair et al 2020 was designed with offline-to-online fine-tuning in mind. The advantage-weighted behavior cloning objective naturally supports both offline pretraining and online improvement, transitioning smoothly between the two regimes as the online data accumulates.

Cal-QL of [Nakamoto et al. 2023][research_nakamoto_et_al_2023] provides an alternative approach that calibrates the offline-trained conservative Q-function to match the true value scale, permitting effective online fine-tuning without the policy collapse that plain CQL exhibits during online adaptation. The Cal-QL objective adds a calibration term to CQL that lower-bounds the Q-function by the Monte Carlo return of the behavior policy,

$$
L_{\text{Cal-QL}}(Q) = L_{\text{CQL}}(Q) + \eta \, \mathbb{E}_{(s, a) \sim \mathcal{D}}\!\left[\left(\max(Q(s, a), V^\mu(s)) - Q(s, a)\right)^2\right]
\tag{33}
$$

preventing the Q-function from underestimating value on states well-covered by the dataset.

Balanced Replay of [Lee Seo Lee Abbeel Shin 2022][research_lee_et_al_2022_balanced_replay] combines offline and online data in a replay buffer with adaptive weighting, permitting continued influence of offline data during online fine-tuning without full replacement. RLPD of [Ball Smith Kostrikov Levine 2023][research_ball_et_al_2023_rlpd] documented that direct off-policy training on symmetric mixtures of offline and online data, combined with large ensembles and standard SAC updates, achieves strong performance without dedicated offline-to-online algorithmic machinery. Policy Expansion of [Zhang et al. 2023][research_zhang_et_al_2023_policy_expansion] combined offline-pretrained policy priors with online policy expansion, avoiding catastrophic forgetting through explicit policy composition. Jump-Start Reinforcement Learning of [Uchendu et al. 2023][research_uchendu_et_al_2023_jumpstart] proposed a rollout-mixture framework in which the offline-pretrained policy provides initial trajectory prefixes for online reinforcement learning, effectively transferring initial-state distribution rather than the full policy. Efficient online reinforcement learning fine-tuning approaches of [Zheng 2023][research_zheng_et_al_2023_finetune] documented systematic protocols for stability during the offline-to-online transition.

The offline-to-online setting connects offline reinforcement learning to the meta-learning and continual learning frameworks treated in articles nine and ten.

## Sample Complexity and the Pessimism Framework

The theoretical understanding of offline reinforcement learning matured greatly in the 2020s through the pessimism framework. The core observation is that offline algorithms cannot outperform online algorithms in the worst case because they lack the ability to explore beyond the offline data distribution, but they can achieve optimal performance relative to any policy whose induced state-action distribution is well-covered by the offline data.

The pessimism principle formalizes this observation. An offline algorithm should compute a policy that maximizes a pessimistic estimate of value, where the pessimism reflects uncertainty about the value at states and actions poorly covered by the data.

Xie Cheng Jiang Mineiro and Agarwal 2021, [Rashidinejad et al. 2021][research_rashidinejad_et_al_2021], [Jin et al. 2021][research_jin_yang_wang_2021], and [Uehara and Sun 2022][research_uehara_sun_2022] established sample complexity bounds for pessimistic offline reinforcement learning of the form

$$
V^* - V^{\hat{\pi}} \leq \tilde{\mathcal{O}}\!\left(\sqrt{\frac{C^* H^3}{N}}\right)
\tag{34}
$$

where $C^\*$ is a concentrability coefficient measuring the coverage of the optimal policy's state-action distribution by the offline data distribution and $N$ is the dataset size. The bound depends on $C^\*$ rather than the state-action space size, providing meaningful guarantees for problems with large state spaces provided the coverage is favorable.

The concentrability coefficient can be characterized as

$$
C^* = \max_{s, a} \frac{d^{\pi^*}(s, a)}{d^\mu(s, a)}
\tag{35}
$$

where $d^{\pi^\*}$ is the state-action distribution of the optimal policy and $d^\mu$ is that of the behavior policy. When $C^\*$ is bounded, the offline dataset provides sufficient coverage to identify a near-optimal policy without further exploration.

Weaker single-policy concentrability replaces the maximum over states and actions with an average,

$$
\bar{C}^* = \mathbb{E}_{(s, a) \sim d^{\pi^*}}\!\left[\frac{d^{\pi^*}(s, a)}{d^\mu(s, a)}\right]
\tag{36}
$$

and yields tighter bounds in favorable regimes. All-policy concentrability

$$
C_{\text{all}} = \sup_\pi \max_{s, a} \frac{d^\pi(s, a)}{d^\mu(s, a)}
\tag{37}
$$

is required by algorithms without pessimism, and its typical unboundedness is the fundamental reason such algorithms fail in offline settings.

Bilinear MDP and low-rank MDP settings admit sharper analyses that avoid the direct dependence on concentrability. Function approximation settings including linear MDPs and neural function approximation have been analyzed under several assumptions on the model class. The [Wang et al. 2020][research_wang_foster_kakade_2021] treatment of statistical limits established negative results for offline reinforcement learning with function approximation, documenting that realizability alone is insufficient for polynomial sample complexity without additional coverage assumptions. The [Zhan et al. 2022][research_zhan_ren_yin_zhu_2022] framework provided a matching upper bound under realizability and single-policy concentrability, establishing tight sample complexity for offline reinforcement learning with function approximation. The [Chen and Jiang 2019][research_chen_jiang_2019] information-theoretic considerations paper provided the foundational lower-bound framework that motivated the pessimism approach.

Adversarially-trained pessimism of [Cheng Xie Jiang Agarwal 2022][research_cheng_et_al_2022_atac] introduced Adversarially Trained Actor Critic (ATAC), providing a game-theoretic pessimism framework with matching upper and lower bounds under single-policy concentrability. The [Yin and Wang 2021][research_yin_wang_2021] policy learning framework provided the minimax-optimal sample complexity for offline policy learning in tabular settings, and the [Nguyen-Tang et al. 2021][research_nguyen_tang_et_al_2022] neural function approximation analysis extended the theory to overparameterized neural networks under favorable geometry assumptions.

The [Buckman et al. 2020][research_buckman_gelada_bellemare_2020] importance of pessimism paper provided an experimental complement to the theoretical developments, documenting that offline algorithms without explicit pessimism systematically overestimate value and underperform pessimistic alternatives.

## Empirical Landscape

The D4RL benchmark of [Fu et al. 2020][research_fu_et_al_2020_d4rl] is the canonical benchmark for offline reinforcement learning, providing standardized datasets across MuJoCo continuous control (locomotion tasks with different data-collection policies), AntMaze navigation, kitchen manipulation, Adroit dexterous manipulation, and CARLA autonomous driving. The datasets are labeled by their collection policy quality (random, medium, expert, medium-replay, etc.), enabling systematic evaluation of algorithms across data quality regimes.

The RL Unplugged benchmark of [Gulcehre et al. 2020][research_gulcehre_et_al_2020] provides Atari, DMLab, and Real World RL Suite offline datasets, complementing D4RL with visual observations and larger-scale evaluation.

Empirical performance across these benchmarks shows several consistent patterns. Conservative Q-learning and its extensions provide competitive performance across most tasks. Uncertainty-aware ensemble methods including SAC-N and EDAC achieve state-of-the-art on continuous control benchmarks at appreciable compute cost. Sequence modeling methods perform well on tasks with considerable data and reasonable data quality but struggle on tasks requiring policy improvement beyond the training distribution. Diffusion-based methods provide the most expressive policies but at inference-time cost.

No single method dominates across all benchmarks. Method selection depends on data quality, action space structure, and the requirements of the deployment setting.

Hyperparameter selection in offline reinforcement learning presents distinctive challenges. Without online interaction, standard cross-validation approaches do not directly apply. Off-policy evaluation provides a partial solution but with its own accuracy limitations. The [Kumar et al. 2021b][research_kumar_singh_tucker_levine_2021] workflow for offline reinforcement learning paper documented systematic approaches to hyperparameter selection through offline metrics and reduced training-time evaluation. The [Paine et al. 2020][research_paine_et_al_2020] hyperparameter selection framework provided empirical evidence that offline policy selection through off-policy evaluation is often accurate enough for practical model selection when the OPE method is chosen appropriately.

The CORL benchmark library of [Tarasov et al. 2023a][research_tarasov_et_al_2022] provides reference implementations of major offline reinforcement learning algorithms with standardized hyperparameter configurations, addressing the reproducibility challenges documented across the field. The [Prudencio et al. 2022][research_prudencio_maximo_colombini_2023] survey provides a comprehensive taxonomy of offline reinforcement learning methods that complements the [Levine et al. 2020][research_levine_et_al_2020] tutorial with coverage of the 2020-2023 algorithmic developments.

## Data Composition, Quality, and Coverage

The empirical behavior of offline reinforcement learning depends considerably on the composition of the offline dataset. Datasets vary along dimensions including the quality of the behavior policy (random, medium, expert), the diversity of behaviors represented (single-policy vs mixture), the size of the dataset, and the reward-signal density.

Expert-quality datasets support strong behavior cloning baselines but provide limited signal for policy improvement, since the behavior policy already achieves high return. Medium-quality datasets provide significant opportunity for policy improvement but require reliable extrapolation to actions not represented in the data. Random-quality datasets provide broad coverage but rarely contain trajectories that reach the reward region, making value learning difficult.

Mixture datasets combining trajectories from multiple behavior policies provide richer coverage than single-policy datasets. The [Kumar et al. 2022][research_kumar_hong_levine_tucker_2022] work on mixture data documented that mixture datasets often produce significantly better offline learning outcomes than single-policy datasets of comparable size, providing motivation for deliberate data-collection strategies that combine behaviors. COG of [Singh et al. 2020][research_singh_et_al_2020_cog] documented that combining task-with task-agnostic offline data enables policies that generalize substantially beyond narrow single-task datasets. Learning from Unlabeled Data of [Yu et al. 2022][research_yu_et_al_2022_uds] extended the framework to unlabeled action data through pseudo-labeling, expanding the class of usable offline data sources.

Coverage matters for offline reinforcement learning more than dataset size per se. A large dataset with narrow coverage produces the same distributional shift problems as a small one, while a small but well-distributed dataset can support meaningful policy improvement. The concentrability-based sample complexity analyses discussed above formalize this observation.

Data augmentation strategies including hindsight relabeling, state-action perturbation, and generative augmentation provide mechanisms to expand effective dataset coverage without additional data collection. The offline setting benefits markedly from these techniques given the fixed-data constraint. Model-based methods treated in article seven provide an extreme instantiation of the strategy, in which the learned model generates synthetic data far beyond the coverage of the original dataset.

The quality of the reward signal in the offline dataset also matters. Sparse-reward datasets are particularly difficult because value estimates near the reward-region require substantial extrapolation from the limited trajectories that reach it. Dense-reward datasets support easier learning but may reflect proxy objectives rather than the true goal.

## Offline Preference-Based Reinforcement Learning

Preference-based offline reinforcement learning combines offline data with human preference comparisons rather than scalar reward labels, extending the offline framework to domains where reward specification is difficult or unavailable. The treatment connects offline reinforcement learning to the RLHF apparatus of article four and to the preference-based reinforcement learning of article eleven. Deep Reinforcement Learning from Human Preferences of [Christiano et al. 2017][research_christiano_et_al_2017_rlhf] provided the foundational modern framework, and InstructGPT of [Ouyang et al. 2022][research_ouyang_et_al_2022_instructgpt] scaled the model to language model instruction following.

The general setting provides a dataset of trajectory pairs $(\tau_i, \tau'\_i)$ with human preferences $y_i \in \{0, 1\}$ indicating whether $\tau_i$ or $\tau'\_i$ was preferred. A reward model is learned by minimizing the Bradley-Terry log-likelihood

$$
L_{\text{reward}}(\phi) = -\mathbb{E}_{(\tau, \tau', y)}\!\left[y \log \sigma(\hat{R}_\phi(\tau) - \hat{R}_\phi(\tau')) + (1 - y) \log \sigma(\hat{R}_\phi(\tau') - \hat{R}_\phi(\tau))\right]
\tag{38}
$$

where $\hat{R}\_\phi(\tau) = \sum_t \hat{r}\_\phi(s_t, a_t)$ is the trajectory-level reward under the learned reward model. The learned reward is then used to label the offline dataset and enable standard offline reinforcement learning.

Preference Transformer (PT) of [Kim et al. 2023][research_kim_et_al_2023_pt] extended this formulation with a transformer-based reward model that captures long-range dependencies in preference judgments. The mechanism provides marked improvements on tasks where preference structure varies across trajectories.

Direct Preference Optimization (DPO) of [Rafailov et al. 2023][research_rafailov_et_al_2023_dpo] treated in article four provides a preference-based offline reinforcement learning framework that skips the explicit reward model, directly optimizing the policy against preference data with a KL constraint against a reference policy. DPO has become widely adopted for language model post-training and provides evidence that preference-based offline methods can scale to foundation model settings.

Contrastive preference learning of [Hejna et al. 2023][research_hejna_et_al_2023] provides an alternative preference-based offline framework that unifies preference learning with contrastive representation learning. The approach connects offline reinforcement learning to the broader self-supervised representation learning literature. The B-Pref benchmark of [Lee et al. 2021][research_lee_smith_abbeel_2021_bpref] provided standardized evaluation of preference-based reinforcement learning methods and enabled systematic comparison of preference-learning algorithms. The [Wirth et al. 2017][research_wirth_et_al_2017] survey of preference-based reinforcement learning consolidated the preference-elicitation and preference-learning literature and identified the representational requirements that offline preference-based methods subsequently addressed. Learning reward functions from preferences over trajectories of [Sadigh et al. 2017][research_sadigh_et_al_2017] provided the direct precursor to modern deep preference learning through active preference queries under a linear reward model. PEBBLE of [Lee Smith Krishnan Abbeel 2021][research_lee_smith_krishnan_abbeel_2021_pebble] extended the treatment to unsupervised pretraining plus preference-based fine-tuning, providing a semi-supervised alternative that reduces the number of required preference labels.

## Offline Constrained Reinforcement Learning and Safety

Offline constrained reinforcement learning augments the standard offline setting with constraints that the learned policy must satisfy at deployment. The model is essential for practical deployments where safety, fairness, or other constraints must be respected.

The constrained offline problem seeks a policy that maximizes expected return subject to constraint satisfaction,

$$
\max_\pi J(\pi) \quad \text{subject to} \quad J_{c_i}(\pi) \leq d_i \text{ for } i = 1, \ldots, K
\tag{39}
$$

where $J_{c_i}(\pi)$ is the expected value of constraint $i$ under policy $\pi$ and $d_i$ is the allowed threshold. Both $J$ and the $J_{c_i}$ must be estimated from the offline data, subject to the same distributional shift challenges as unconstrained offline reinforcement learning.

Constrained Offline Q-Learning (COptiDICE) of [Lee Jeon Kim Kim 2022][research_lee_et_al_2022_coptidice] extends the DualDICE framework to the constrained setting, providing a Lagrangian-based algorithm with theoretical guarantees under standard concentrability conditions. Batch Policy Learning under Constraints of [Le et al. 2019][research_le_voloshin_yue_2019_constraints] provided the foundational treatment of constrained offline reinforcement learning with explicit sample complexity bounds under linear function approximation. The DSRL benchmark of [Liu et al. 2023][research_liu_ding_liu_2023_dsrl] provided standardized evaluation for safe offline reinforcement learning across a diverse suite of constrained control tasks.

The [Xu et al. 2021][research_xu_zhan_zhu_2022] Constraints Penalized Q-learning framework combines conservative Q-learning with a constraint penalty, providing a practical algorithm that scales to high-dimensional continuous control. Constrained Policy Optimization of [Achiam Held Tamar Abbeel 2017][research_achiam_et_al_2017_cpo] provided the trust-region-based online precursor whose theoretical framework of monotonic constraint satisfaction has been adapted to the offline setting. Risk-constrained reinforcement learning of [Chow et al. 2018][research_chow_et_al_2017] introduced conditional-value-at-risk constraints and provided the algorithmic framework for risk-sensitive offline policy learning.

Safety-critical applications including healthcare, autonomous driving, and industrial control frequently mandate offline constrained learning. The offline setting is often the only feasible learning framework in these domains because online exploration would produce unacceptable risk.

The connection between offline constrained reinforcement learning and the broader safe reinforcement learning literature is direct. Offline algorithms provide one of the few frameworks in which safety constraints can be reliably enforced during learning, since the deployment policy is verified against constraints before online deployment.

## Foundation Models and Offline Reinforcement Learning

The rise of large-scale foundation models has produced new frameworks for offline reinforcement learning that leverage web-scale pretraining. This formulation treats offline reinforcement learning as an application of transfer learning from a general-purpose foundation model to a control task.

RT-1 of [Brohan et al. 2022][research_brohan_et_al_2022_rt1] and RT-2 of [Brohan et al. 2023][research_brohan_et_al_2023_rt2] provide foundation-model-scale robotic control policies trained on large offline datasets combined with web-scale vision-language pretraining. The treatment produces policies with appreciably improved generalization to novel objects and instructions compared to task-offline training.

RoboCat of [Bousmalis et al. 2023][research_bousmalis_et_al_2023] applies the foundation model framework specifically to robotic manipulation, producing a self-improving loop in which the pretrained model is fine-tuned on task-data and its improved policy generates additional training data for further pretraining. BC-Z of [Jang et al. 2022][research_jang_et_al_2022_bcz] introduced zero-shot task generalization from language-conditioned demonstrations, providing the direct precursor to RT-2's vision-language-action integration.

The Open X-Embodiment collaboration of [Embodiment Collaboration et al. 2023][research_padalkar_et_al_2024] provides a large-scale multi-institution offline dataset of robotic demonstrations spanning many robot embodiments, addressing a bottleneck in foundation model scaling for embodied AI. The Octo generalist policy of [Octo et al. 2024][research_octo_model_team_2024] and OpenVLA of [Kim et al. 2024][research_kim_et_al_2024_openvla] extended this formulation with open-source foundation models for robot manipulation that reach parity with proprietary counterparts.

PaLM-E of [Driess et al. 2023][research_driess_et_al_2023_palme] extended the treatment to embodied multimodal language models that jointly reason over vision, language, and robot actions. The 562-billion-parameter model demonstrated extensive positive transfer between web-scale vision-language pretraining and robotic control, providing evidence that foundation-model scale produces qualitatively different capabilities than task-offline training.

The relationship between foundation model pretraining and offline reinforcement learning is bidirectional. Foundation models provide strong pretrained policies and representations that offline algorithms can build on. Offline reinforcement learning provides the framework for improving foundation model policies on tasks where pretraining alone is insufficient. The interplay is expected to become increasingly central as foundation models scale further.

## Diagnostics and Practical Deployment

The practical deployment of offline reinforcement learning presents distinctive challenges beyond the algorithmic development. Model selection, hyperparameter tuning, and reliability estimation must be performed without online interaction, and standard techniques from online reinforcement learning do not directly apply.

Offline model selection through off-policy evaluation provides one approach. The [Precup et al. 2000][research_precup_sutton_singh_2000_offline] importance sampling and doubly robust estimators discussed above provide the basis for offline value estimation, but their accuracy limitations under distributional shift limit their utility as model selection criteria.

The [Kumar et al. 2021b][research_kumar_singh_tucker_levine_2021] workflow proposal identified several practical heuristics including monitoring Q-value divergence during training, checking for policy collapse, and using held-out data for selection. The [Fu 2021][research_fu_et_al_2021] Benchmarks for Deep Off-Policy Evaluation (DOPE) provided systematic evaluation of off-policy evaluation methods across a range of tasks, documenting the accuracy challenges.

Diagnostic tools including trajectory visualization, state coverage analysis, and behavior policy characterization provide qualitative complements to quantitative evaluation. In practice, offline reinforcement learning deployments typically combine algorithmic evaluation with domain-safety checks and controlled online rollouts.

The gap between benchmark evaluation and real-world deployment remains sizable. Benchmark performance provides a useful proxy but does not fully capture the challenges of deployment in domains where data quality, coverage, and reward specification all vary.

## Applications

Healthcare treatment optimization has been a target application for offline reinforcement learning since the field's early days. Reinforcement learning approaches to sepsis treatment, ICU management, and chronic disease management have been developed using retrospective medical records. The AI Clinician of [Komorowski et al. 2018][research_komorowski_et_al_2018] provided one of the earliest high-profile applications, using offline reinforcement learning on ICU records to recommend fluid and vasopressor doses for sepsis patients. The challenges of the healthcare setting include distributional shift as patient populations and treatment protocols change over time, reward specification where mortality is measurable but quality-of-life is contested, and the ethical requirement for cautious extrapolation from historical data.

Recommender systems and content ranking use offline reinforcement learning to optimize long-term engagement metrics from historical click-and-dwell logs. Top-K Off-Policy correction for YouTube of [Chen et al. 2019][research_chen_et_al_2019_youtube] documented deployment-scale offline reinforcement learning for content recommendation, providing empirical evidence that offline methods can produce meaningful policy improvement over standard supervised recommendation baselines. The setting is friendly to offline learning because logged data is abundant and cheap, but the distributional shift problem is severe due to feedback loops between recommendation and user behavior.

Autonomous driving and robotics use offline reinforcement learning to leverage large logged datasets from vehicle fleets or demonstration collections. The QT-Opt system of Kalashnikov et al 2018 provided an early large-scale deployment for robotic grasping. Subsequent work has extended to broader manipulation tasks and to autonomous driving policy learning. The [Nair et al. 2022][research_nair_et_al_2022_rrl] robotic reinforcement learning at scale framework documented systematic protocols for offline reinforcement learning on large-scale robotic manipulation datasets, providing evidence that carefully-tuned offline methods can match online counterparts at greatly reduced data-collection cost.

Industrial control including HVAC optimization, network routing, and manufacturing process control use offline reinforcement learning to leverage large historical control logs. The offline setting is often mandated by safety constraints that preclude online exploration in production systems.

Language model post-training treated in article four uses offline reinforcement learning through the RLHF and DPO frameworks. The setting is offline in the sense that the pretrained model and preference dataset are fixed, though the algorithms differ considerably from the general-purpose offline reinforcement learning methods treated here.

## Neuroscience Connections

Offline learning in biological brains has been extensively studied through the hippocampal replay literature treated in articles three and seven. Hippocampal place cells replay sequences of past experience during quiet wakefulness and sleep, and this replay has been linked to memory consolidation and behavioral improvement without additional environmental interaction. The foundational [Wilson and McNaughton 1994][research_wilson_mcnaughton_1994] observations of coordinated hippocampal reactivation during sleep provided the earliest neurophysiological evidence for offline experience replay in the mammalian brain. The reverse-replay observations of [Foster and Wilson 2006][research_foster_wilson_2006] documented that hippocampal place cell sequences reactivate in reverse temporal order during rest, providing the mechanistic basis for reward propagation across the recent trajectory. The [O'Neill et al. 2010][research_oneill_et_al_2010] review consolidated the hippocampal replay literature and established replay as the leading biological candidate for memory consolidation. Preplay observations by [Pfeiffer and Foster 2013][research_pfeiffer_foster_2013] documented forward replay of trajectories to future goal locations, providing evidence that hippocampal replay serves prospective planning as well as retrospective consolidation.

The connection to computational offline reinforcement learning is direct. Hippocampal replay provides a biological analogue to experience replay in offline reinforcement learning algorithms, and the sleep-based consolidation of memories provides a biological analogue to offline policy improvement from stored experience.

Recent work including [Mattar and Daw 2018][research_mattar_daw_2018] has proposed that hippocampal replay implements prioritized replay analogous to the prioritized sweeping methods of article seven, with replayed transitions selected based on their expected utility for value estimation. The [Ólafsdóttir et al. 2018][research_olafsdottir_bush_barry_2018] treatment of nonlocal hippocampal replay documented that replayed sequences frequently traverse trajectories the animal never physically experienced, providing a biological analogue to model-based generation from a learned world model.

The distinction between habitual and goal-directed behavior treated in articles three and fifteen also connects to offline reinforcement learning. Habitual behavior corresponds to policies that have been consolidated through repeated offline replay and no longer require online planning, while goal-directed behavior corresponds to online model-based reasoning. The interplay between the two systems provides a biological analogue to the offline-to-online fine-tuning setting.

Article fourteen returns to the NeuroAI bridge and treats the relationship between machine learning offline reinforcement learning and biological offline learning systematically.

## Load-Bearing Open Questions

- What is the correct algorithmic approach to offline reinforcement learning without careful hyperparameter tuning? Current methods are sensitive to hyperparameters in ways that limit practical deployment.
- How can offline algorithms be reliably combined with online fine-tuning without catastrophic forgetting of the offline knowledge or excessive online sample requirements?
- What is the correct off-policy evaluation methodology for offline hyperparameter selection when online evaluation is unavailable?
- How should offline reinforcement learning handle non-stationary environments where the offline data was collected under conditions that no longer hold at deployment time?
- What is the correct theoretical framework for offline reinforcement learning with function approximation? Sample complexity results assume favorable conditions on the model class that may not hold in practice.
- How closely do the offline learning mechanisms of hippocampal replay correspond to offline reinforcement learning algorithms?
- What is the correct approach to combining multiple heterogeneous offline datasets from different collection policies, quality levels, and time periods?
- How should offline reinforcement learning be integrated with the sequence modeling, diffusion, and foundation model paradigms that have emerged in the 2020s?

## Equations

<!-- Equations generated by _lib/equations.py from _sources/equations/. Edit the data file and regenerate. Do not edit this section by hand. -->

This section collects the 39 display equations of the article in the order they appear,
each under its number and reproduced exactly as it stands in the text.
A title in bold names an established result,
and a title in italics beginning with the word Bespoke names a construction made for this analysis.
Of the 39, 37 are established and 2 are bespoke.
Occupancy measures, importance ratios and concentrability coefficients are dimensionless, values and returns carry the units of the reward signal, and $N$ counts transitions in some equations and trajectories in others, so a sample complexity bound must be read with the unit of $N$ that its source uses.

**Equation 1, Offline Dataset.**
Offline reinforcement learning receives a fixed set of transitions collected beforehand by a behaviour policy.
[Levine et al. 2020][research_levine_et_al_2020]

$$
\mathcal{D} = \{(s_i, a_i, r_i, s'_i)\}_{i=1}^N
\tag{1}
$$

**Equation 2, Discounted State-Action Occupancy.**
The normalised discounted occupancy gives how often a policy visits each state-action pair, weighted by the discount.

$$
d^\pi(s, a) = (1 - \gamma) \sum_{t=0}^{\infty} \gamma^t \Pr(s_t = s, a_t = a \mid s_0 \sim \mu_0, \pi)
\tag{2}
$$

**Equation 3, Occupancy Ratio.**
The ratio of the target policy's occupancy to the behaviour occupancy measures distributional shift and is unbounded where the data do not cover the target policy.

$$
w(s, a) = \frac{d^\pi(s, a)}{d^\mu(s, a)}
\tag{3}
$$

**Equation 4, Q-Learning Target.**
The bootstrapped target maximises over next actions, including actions the dataset may never contain.

$$
y = r + \gamma \max_{a'} Q(s', a')
\tag{4}
$$

*Equation 5, Bespoke Lower Bound on Maximisation Bias.*
The article states that the expected maximum of noisy action values exceeds the true maximum by at least a multiple of the noise scale that grows with the action count, which holds only under its assumption of zero-mean noise of equal variance at every action.

$$
\mathbb{E}[\max_a \hat{Q}(s, a)] - \max_a Q^*(s, a) \geq c(|\mathcal{A}|) \sigma
\tag{5}
$$

**Equation 6, Behaviour Cloning Loss.**
Behaviour cloning maximises the log likelihood of the dataset actions under the learned policy.

$$
L_{\text{BC}}(\pi_\theta) = -\mathbb{E}_{(s, a) \sim \mathcal{D}}\!\left[\log \pi_\theta(a \mid s)\right]
\tag{6}
$$

**Equation 7, Advantage-Weighted Regression Loss.**
Advantage-weighted regression weights each behaviour cloning term by the exponential of the action's advantage over a temperature.
[Peng et al. 2019][research_peng_kumar_zhang_levine_2019]

$$
L_{\text{AWR}}(\pi_\theta) = -\mathbb{E}_{(s, a) \sim \mathcal{D}}\!\left[\exp(A(s, a) / \beta) \log \pi_\theta(a \mid s)\right]
\tag{7}
$$

**Equation 8, Trajectory Importance Sampling Estimator.**
The estimator averages each trajectory's return weighted by its full importance ratio.
[Precup et al. 2000][research_precup_sutton_singh_2000_offline]

$$
\hat{V}^\pi_{\text{IS}} = \frac{1}{N} \sum_{i=1}^N \rho_{0:T_i-1}^{(i)} G^{(i)}
\tag{8}
$$

**Equation 9, Trajectory Importance Sampling Ratio.**
The ratio of target to behaviour policy probabilities is multiplied over the actions of a trajectory of length $T$.
[Precup et al. 2000][research_precup_sutton_singh_2000_offline]

$$
\rho_{0:T-1} = \prod_{t=0}^{T-1} \frac{\pi(a_t \mid s_t)}{\mu(a_t \mid s_t)}
\tag{9}
$$

**Equation 10, Per-Decision Importance Sampling Estimator.**
Each reward is weighted only by the importance ratio of the actions up to and including the one that produced it.
[Precup et al. 2000][research_precup_sutton_singh_2000_offline]

$$
\hat{V}^\pi_{\text{PDIS}} = \frac{1}{N} \sum_{i=1}^N \sum_{t=0}^{T_i-1} \gamma^t \rho_{0:t}^{(i)} r_{t+1}^{(i)}
\tag{10}
$$

**Equation 11, Weighted Importance Sampling Estimator.**
Weighted importance sampling normalises the reweighted returns by the sum of the ratios, which introduces bias but usually reduces variance.

$$
\hat{V}^\pi_{\text{WIS}} = \frac{\sum_i \rho_{0:T_i-1}^{(i)} G^{(i)}}{\sum_i \rho_{0:T_i-1}^{(i)}}
\tag{11}
$$

**Equation 12, Doubly Robust Off-Policy Estimator.**
The doubly robust estimator combines importance-weighted rewards with a learned value baseline so that it remains unbiased if either the ratios or the baseline is correct.
[Jiang and Li 2016][research_jiang_li_2016_offline]
[Thomas and Brunskill 2016][research_thomas_brunskill_2016]

$$
\hat{V}^\pi_{\text{DR}} = \frac{1}{N} \sum_{i=1}^N \sum_{t=0}^{T_i-1} \gamma^t \left[\rho_{0:t}^{(i)} \left(r_{t+1}^{(i)} - \hat{Q}(s_t^{(i)}, a_t^{(i)})\right) + \rho_{0:t-1}^{(i)} \hat{V}(s_t^{(i)})\right]
\tag{12}
$$

**Equation 13, DualDICE Saddle-Point Objective.**
Distribution correction estimation, abbreviated DICE, recovers the occupancy ratio as the solution of a saddle-point problem that uses only the dataset and samples from the initial distribution.
[Nachum et al. 2019][research_nachum_et_al_2019_dualdice]

$$
\min_v \max_\zeta \, \mathbb{E}_{(s, a) \sim d^\mu}\!\left[f(\zeta(s, a)) - \zeta(s, a) \cdot \mathcal{T}^\pi v(s, a)\right] + (1 - \gamma) \mathbb{E}_{s_0 \sim \mu_0, a_0 \sim \pi}\!\left[v(s_0, a_0)\right]
\tag{13}
$$

**Equation 14, Fitted Q Evaluation Backup.**
Each iteration regresses the action value onto the reward plus the discounted expected value of the previous estimate under the target policy at the next state.
[Le Voloshin Yue 2019][research_le_voloshin_yue_2019]

$$
\hat{Q}_{k+1}(s, a) = \mathbb{E}_{(s', r) \sim \mathcal{D}}\!\left[r + \gamma \mathbb{E}_{a' \sim \pi}[\hat{Q}_k(s', a')]\right]
\tag{14}
$$

**Equation 15, Behaviour-Regularised Policy Objective.**
The policy maximises its expected action value less a multiple of its divergence from the behaviour policy.
[Wu et al. 2019][research_wu_tucker_nachum_2019]

$$
J_{\text{BR}}(\pi) = \mathbb{E}\!\left[Q(s, a)\right] - \alpha \, D(\pi(\cdot \mid s) \, \| \, \mu(\cdot \mid s))
\tag{15}
$$

**Equation 16, Squared Maximum Mean Discrepancy.**
The squared maximum mean discrepancy between two action distributions is written with kernel expectations within and across the two distributions.
[Kumar Fu Tucker Levine 2019][research_kumar_et_al_2019_bear]

$$
\text{MMD}^2(\pi, \mu) = \mathbb{E}_{a \sim \pi, a' \sim \pi}[k(a, a')] - 2 \mathbb{E}_{a \sim \pi, a' \sim \mu}[k(a, a')] + \mathbb{E}_{a \sim \mu, a' \sim \mu}[k(a, a')]
\tag{16}
$$

**Equation 17, TD3 Plus Behaviour Cloning Objective.**
The deterministic actor maximises its action value less a weighted squared distance from the dataset action.
[Fujimoto and Gu 2021][research_fujimoto_gu_2021]

$$
J_{\text{TD3+BC}}(\pi) = \mathbb{E}\!\left[Q(s, \pi(s))\right] - \lambda \mathbb{E}_{(s, a) \sim \mathcal{D}}\!\left[\|\pi(s) - a\|^2\right]
\tag{17}
$$

**Equation 18, Advantage-Weighted Optimal Policy.**
The solution of the divergence-constrained improvement problem is the behaviour policy reweighted by the exponentiated advantage.
[Nair et al. 2020][research_nair_et_al_2020_awac]

$$
\pi^*(a \mid s) \propto \mu(a \mid s) \exp(A(s, a) / \beta)
\tag{18}
$$

**Equation 19, Advantage-Weighted Actor-Critic Gradient.**
The policy gradient is the behaviour cloning gradient with each dataset action weighted by its exponentiated advantage.
[Nair et al. 2020][research_nair_et_al_2020_awac]

$$
\nabla_\theta L_{\text{AWAC}}(\theta) = -\mathbb{E}_{(s, a) \sim \mathcal{D}}\!\left[\exp\!\left(A^{\pi_k}(s, a) / \beta\right) \nabla_\theta \log \pi_\theta(a \mid s)\right]
\tag{19}
$$

**Equation 20, Implicit Q-Learning Value Loss.**
Implicit Q-learning fits the state value by expectile regression on target action values, approximating a maximum over dataset actions.
[Kostrikov Nair Levine 2022][research_kostrikov_nair_levine_2022]

$$
L_{\text{IQL}}(V) = \mathbb{E}_{(s, a) \sim \mathcal{D}}\!\left[L_2^\tau(Q_{\text{target}}(s, a) - V(s))\right]
\tag{20}
$$

**Equation 21, Implicit Q-Learning Action-Value Loss.**
The action value regresses onto the reward plus the discounted fitted state value, so no out-of-distribution action is queried.
[Kostrikov Nair Levine 2022][research_kostrikov_nair_levine_2022]

$$
L_{\text{IQL}}(Q) = \mathbb{E}_{(s, a, r, s') \sim \mathcal{D}}\!\left[(r + \gamma V(s') - Q(s, a))^2\right]
\tag{21}
$$

**Equation 22, Conservative Q-Learning Objective.**
Conservative Q-learning adds to the Bellman error a penalty equal to the soft maximum of the action values less their mean over dataset actions.
[Kumar Zhou Tucker Levine 2020][research_kumar_zhou_tucker_levine_2020]

$$
L_{\text{CQL}}(Q) = \alpha \, \mathbb{E}_{s \sim \mathcal{D}}\!\left[\log \sum_a \exp(Q(s, a)) - \mathbb{E}_{a \sim \mu}[Q(s, a)]\right] + L_{\text{Bellman}}(Q)
\tag{22}
$$

**Equation 23, Conservative Value Lower Bound.**
In the tabular setting the policy-averaged conservative action value does not exceed the corresponding true value.
[Kumar Zhou Tucker Levine 2020][research_kumar_zhou_tucker_levine_2020]

$$
\mathbb{E}_{a \sim \pi}\!\left[\hat{Q}(s, a)\right] \leq \mathbb{E}_{a \sim \pi}\!\left[Q^\pi(s, a)\right]
\tag{23}
$$

**Equation 24, Ensemble Minimum Target.**
The target takes the minimum over an ensemble of $N$ action-value networks, which yields pessimism that grows with their disagreement.
[An et al. 2021][research_an_et_al_2021]

$$
Q_{\text{target}}(s, a) = \min_{k=1, \ldots, N} Q_k(s, a)
\tag{24}
$$

**Equation 25, Ensemble Gradient Diversity Penalty.**
The ensemble-diversified actor-critic adds a penalty on the pairwise cosine similarity of the members' action gradients.
[An et al. 2021][research_an_et_al_2021]

$$
L_{\text{EDAC}} = L_{\text{SAC-N}} + \eta \, \mathbb{E}\!\left[\sum_{k \neq k'} \frac{|\nabla_a Q_k^\top \nabla_a Q_{k'}|}{\|\nabla_a Q_k\| \|\nabla_a Q_{k'}\|}\right]
\tag{25}
$$

**Equation 26, Lower Confidence Bound Action Value.**
The pessimistic action value subtracts a multiple of the epistemic uncertainty from the estimate.
[Rashidinejad et al. 2021][research_rashidinejad_et_al_2021]

$$
Q_{\text{LCB}}(s, a) = \hat{Q}(s, a) - \beta \, \hat{\sigma}(s, a)
\tag{26}
$$

**Equation 27, Return-Conditioned Policy.**
Decision Transformer conditions each action on a recent window of states, actions and returns-to-go.
[Chen et al. 2021][research_chen_et_al_2021_dt]

$$
\pi_\theta(a_t \mid s_{t-K:t}, a_{t-K:t-1}, \hat{R}_{t-K:t})
\tag{27}
$$

**Equation 28, Decision Transformer Loss.**
The model is trained by maximising the log likelihood of dataset actions under that conditioning.
[Chen et al. 2021][research_chen_et_al_2021_dt]

$$
L_{\text{DT}}(\theta) = -\mathbb{E}_{\tau \sim \mathcal{D}}\!\left[\sum_t \log \pi_\theta(a_t \mid s_{t-K:t}, a_{t-K:t-1}, \hat{R}_{t-K:t})\right]
\tag{28}
$$

**Equation 29, Forward Diffusion Step.**
Each forward step shrinks the trajectory by $\sqrt{1 - \beta_k}$ and adds Gaussian noise of variance $\beta_k$.
[Ho Jain Abbeel 2020][research_ho_jain_abbeel_2020_ddpm]

$$
q(\tau^{(k)} \mid \tau^{(k-1)}) = \mathcal{N}(\tau^{(k)} ; \sqrt{1 - \beta_k} \, \tau^{(k-1)}, \beta_k I)
\tag{29}
$$

**Equation 30, Learned Reverse Diffusion Step.**
A network predicts the mean and covariance of the Gaussian that removes one step of noise.
[Janner et al. 2022][research_janner_du_song_2022]

$$
p_\theta(\tau^{(k-1)} \mid \tau^{(k)}) = \mathcal{N}(\tau^{(k-1)} ; \mu_\theta(\tau^{(k)}, k), \Sigma_\theta(\tau^{(k)}, k))
\tag{30}
$$

**Equation 31, Guided Reverse Mean.**
Guidance shifts the reverse mean along the gradient of a return signal scaled by the reverse covariance.
[Janner et al. 2022][research_janner_du_song_2022]

$$
\tilde{\mu}_\theta(\tau^{(k)}, k) = \mu_\theta(\tau^{(k)}, k) + \Sigma_\theta \, \nabla_{\tau^{(k)}} J(\tau^{(k)})
\tag{31}
$$

**Equation 32, Uncertainty-Penalised Reward.**
Model-based offline policy optimisation subtracts from the model reward a multiple of the ensemble uncertainty.
[Yu et al. 2020][research_yu_et_al_2020_mopo]

$$
\tilde{r}(s, a) = \hat{r}(s, a) - \lambda \, u(s, a)
\tag{32}
$$

*Equation 33, Bespoke Calibration Penalty for Conservative Q-Learning.*
The article renders the calibration of Cal-QL as a squared penalty on any shortfall of the action value below the behaviour value, a form of its own rather than the cited method's substitution inside the conservative penalty.
[Nakamoto et al. 2023][research_nakamoto_et_al_2023]

$$
L_{\text{Cal-QL}}(Q) = L_{\text{CQL}}(Q) + \eta \, \mathbb{E}_{(s, a) \sim \mathcal{D}}\!\left[\left(\max(Q(s, a), V^\mu(s)) - Q(s, a)\right)^2\right]
\tag{33}
$$

**Equation 34, Suboptimality Bound of Pessimistic Offline Learning.**
Pessimistic offline algorithms return a policy whose suboptimality shrinks as the square root of the concentrability coefficient over the dataset size, with a polynomial dependence on the horizon.
[Rashidinejad et al. 2021][research_rashidinejad_et_al_2021]
[Jin et al. 2021][research_jin_yang_wang_2021]

$$
V^* - V^{\hat{\pi}} \leq \tilde{\mathcal{O}}\!\left(\sqrt{\frac{C^* H^3}{N}}\right)
\tag{34}
$$

**Equation 35, Single-Policy Concentrability Coefficient.**
The coefficient is the largest ratio of the optimal policy's occupancy to the behaviour occupancy.
[Rashidinejad et al. 2021][research_rashidinejad_et_al_2021]

$$
C^* = \max_{s, a} \frac{d^{\pi^*}(s, a)}{d^\mu(s, a)}
\tag{35}
$$

**Equation 36, Averaged Concentrability Coefficient.**
Averaging the occupancy ratio under the optimal policy's occupancy gives a weaker coverage measure than its maximum.

$$
\bar{C}^* = \mathbb{E}_{(s, a) \sim d^{\pi^*}}\!\left[\frac{d^{\pi^*}(s, a)}{d^\mu(s, a)}\right]
\tag{36}
$$

**Equation 37, All-Policy Concentrability Coefficient.**
All-policy concentrability takes the largest occupancy ratio over every policy, which the data must bound for algorithms without pessimism.

$$
C_{\text{all}} = \sup_\pi \max_{s, a} \frac{d^\pi(s, a)}{d^\mu(s, a)}
\tag{37}
$$

**Equation 38, Bradley-Terry Trajectory Preference Loss.**
The reward model minimises the cross-entropy of observed trajectory preferences under a logistic model of summed predicted rewards.
[Christiano et al. 2017][research_christiano_et_al_2017_rlhf]

$$
L_{\text{reward}}(\phi) = -\mathbb{E}_{(\tau, \tau', y)}\!\left[y \log \sigma(\hat{R}_\phi(\tau) - \hat{R}_\phi(\tau')) + (1 - y) \log \sigma(\hat{R}_\phi(\tau') - \hat{R}_\phi(\tau))\right]
\tag{38}
$$

**Equation 39, Constrained Policy Optimisation Problem.**
The policy maximises expected return subject to each expected constraint cost staying below its threshold.
[Le et al. 2019][research_le_voloshin_yue_2019_constraints]

$$
\max_\pi J(\pi) \quad \text{subject to} \quad J_{c_i}(\pi) \leq d_i \text{ for } i = 1, \ldots, K
\tag{39}
$$

### Notation

- $\mathcal{D}$, the fixed offline dataset
- $d^\pi(s, a)$, the normalised discounted state-action occupancy of policy $\pi$
- $d^\mu(s, a)$, the occupancy of the behaviour policy
- $w(s, a)$, the occupancy ratio
- $\rho_{0:T-1}$, the trajectory importance sampling ratio
- $\beta$, the advantage temperature in equations 7, 18 and 19, the pessimism scale in equation 26 and, as $\beta_k$, the diffusion noise schedule
- $\alpha$, the strength of behaviour regularisation or of the conservative penalty
- $k(a, a')$, the kernel of the maximum mean discrepancy
- $L_2^\tau$, the expectile loss at level $\tau$
- $\hat{\sigma}(s, a)$, the epistemic uncertainty estimate
- $\tau^{(k)}$, the trajectory after $k$ diffusion steps
- $u(s, a)$, the ensemble uncertainty estimate
- $C^*$, the single-policy concentrability coefficient
- $H$, the episode horizon
- $J_{c_i}(\pi)$, the expected cost of constraint $i$, with $d_i$ its threshold

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Primary Sources, Peer-Reviewed

- Antos, András, Csaba Szepesvári, and Rémi Munos. 2007. "Learning near-Optimal Policies with Bellman-Residual Minimization Based Fitted Policy Iteration and a Single Sample Path." *Machine Learning* 71 (1): 89–129. [https://doi.org/10.1007/s10994-007-5038-2][research_antos_szepesvari_munos_2008]
- Foster, David J., and Matthew A. Wilson. 2006. "Reverse Replay of Behavioural Sequences in Hippocampal Place Cells during the Awake State." *Nature* 440 (7084): 680–83. [https://doi.org/10.1038/nature04587][research_foster_wilson_2006]
- Komorowski, Matthieu, Leo A. Celi, Omar Badawi, Anthony C. Gordon, and A. Aldo Faisal. 2018. "The Artificial Intelligence Clinician Learns Optimal Treatment Strategies for Sepsis in Intensive Care." *Nature Medicine* 24 (11): 1716–20. [https://doi.org/10.1038/s41591-018-0213-5][research_komorowski_et_al_2018]
- Mattar, Marcelo G., and Nathaniel D. Daw. 2018. "Prioritized Memory Access Explains Planning and Hippocampal Replay." *Nature Neuroscience* 21 (11): 1609–17. [https://doi.org/10.1038/s41593-018-0232-z][research_mattar_daw_2018]
- Pfeiffer, Brad E., and David J. Foster. 2013. "Hippocampal Place-Cell Sequences Depict Future Paths to Remembered Goals." *Nature* 497 (7447): 74–79. [https://doi.org/10.1038/nature12112][research_pfeiffer_foster_2013]
- Riedmiller, Martin. 2005. "Neural Fitted Q Iteration – First Experiences with a Data Efficient Neural Reinforcement Learning Method." In *Machine Learning: ECML 2005*. Springer Berlin Heidelberg. [https://doi.org/10.1007/11564096\_32][research_riedmiller_2005_nfq]
- Sutton, Richard S. 1988. "Learning to Predict by the Methods of Temporal Differences." *Machine Learning* 3 (1): 9–44. [https://doi.org/10.1007/bf00115009][research_sutton_1988_td]

### Primary Sources, Non-Peer-Reviewed

- Agarwal, Rishabh, Dale Schuurmans, and Mohammad Norouzi. 2020. "An Optimistic Perspective on Offline Reinforcement Learning." In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v119/agarwal20c.html][research_agarwal_schuurmans_norouzi_2020]
- An, Gaon, Seungyong Moon, Jang-Hyun Kim, and Hyun Oh Song. 2021. "Uncertainty-Based Offline Reinforcement Learning with Diversified Q-Ensemble." *Advances in Neural Information Processing Systems* 34: 7436–47. [https://papers.nips.cc/paper/2021/hash/3d3d286a8d153a4a58156d0e02d8570c-Abstract.html][research_an_et_al_2021]
- Argenson, Arthur, and Gabriel Dulac-Arnold. 2020. "Model-Based Offline Planning." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2008.05556][research_argenson_dulac_arnold_2021_mbop]
- Bousmalis, Konstantinos, Giulia Vezzani, Dushyant Rao, et al. 2023. "RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2306.11706][research_bousmalis_et_al_2023]
- Brandfonbrener, David, Alberto Bietti, Jacob Buckman, Romain Laroche, and Joan Bruna. 2022. "When Does Return-Conditioned Supervised Learning Work for Offline Reinforcement Learning?" In *Advances in Neural Information Processing Systems*. [https://papers.nips.cc/paper\_files/paper/2022/hash/0a2f65c9d2313b71005e600bd23393fe-Abstract-Conference.html][research_brandfonbrener_et_al_2022]
- Brohan, Anthony, Noah Brown, Justice Carbajal, et al. 2023. "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2307.15818][research_brohan_et_al_2023_rt2]
- Brohan, Anthony, Noah Brown, Justice Carbajal, et al. 2022. "RT-1: Robotics Transformer for Real-World Control at Scale." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2212.06817][research_brohan_et_al_2022_rt1]
- Buckman, Jacob, Carles Gelada, and Marc G. Bellemare. 2020. "The Importance of Pessimism in Fixed-Dataset Policy Optimization." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2009.06799][research_buckman_gelada_bellemare_2020]
- Chebotar, Yevgen, Quan Vuong, Alex Irpan, et al. 2023. "Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2309.10150][research_chebotar_et_al_2023_q_transformer]
- Chen, Minmin, Alex Beutel, Paul Covington, Sagar Jain, Francois Belletti, and Ed H. Chi. 2019. "Top-K off-Policy Correction for a REINFORCE Recommender System." In *Proceedings of the Twelfth ACM International Conference on Web Search and Data Mining*. ACM. [https://doi.org/10.1145/3289600.3290999][research_chen_et_al_2019_youtube]
- Chen, Jinglin, and Nan Jiang. 2019. "Information-Theoretic Considerations in Batch Reinforcement Learning." In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v97/chen19e.html][research_chen_jiang_2019]
- Chen, Lili, Kevin Lu, Aravind Rajeswaran, et al. 2021. "Decision Transformer: Reinforcement Learning via Sequence Modeling." *Advances in Neural Information Processing Systems* 34: 15084–97. [https://papers.nips.cc/paper/2021/hash/7f489f642a0ddb10272b5c31057f0663-Abstract.html][research_chen_et_al_2021_dt]
- Chen, Xu, Vella, and Zhou. 2023. *\[Title not identified\]*. [https://scholar.google.com/scholar?q=Chen+Xu+Vella+2023][research_chen_xu_vella_zhou_2023]
- Chi, Cheng, Zhenjia Xu, Siyuan Feng, et al. 2023. "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2303.04137][research_chi_et_al_2023_diffusion_policy]
- Chow, Yinlam, Mohammad Ghavamzadeh, Lucas Janson, and Marco Pavone. 2018. "Risk-Constrained Reinforcement Learning with Percentile Risk Criteria." *Journal of Machine Learning Research* 18: 1–51. [https://jmlr.org/papers/v18/15-636.html][research_chow_et_al_2017]
- Christiano, Paul F., Jan Leike, Tom Brown, Miljan Martic, Shane Legg, and Dario Amodei. 2017. "Deep Reinforcement Learning from Human Preferences." *Advances in Neural Information Processing Systems* 30. [https://papers.nips.cc/paper/2017/hash/d5e2c0adad503c91f91df240d0cd4e49-Abstract.html][research_christiano_et_al_2017_rlhf]
- Driess, Danny, Fei Xia, Mehdi S. M. Sajjadi, et al. 2023. "PaLM-E: An Embodied Multimodal Language Model." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2303.03378][research_driess_et_al_2023_palme]
- Embodiment Collaboration, Abby O'Neill, Abdul Rehman, et al. 2023. "Open X-Embodiment: Robotic Learning Datasets and RT-X Models." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2310.08864][research_padalkar_et_al_2024]
- Ernst, Damien, Pierre Geurts, and Louis Wehenkel. 2005. "Tree-Based Batch Mode Reinforcement Learning." *Journal of Machine Learning Research* 6: 503–56. [https://www.jmlr.org/papers/v6/ernst05a.html][research_ernst_geurts_wehenkel_2005_offline]
- Fu, Justin, Aviral Kumar, Ofir Nachum, George Tucker, and Sergey Levine. 2020. "D4RL: Datasets for Deep Data-Driven Reinforcement Learning." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2004.07219][research_fu_et_al_2020_d4rl]
- Fu, Kumar, Soh, and Levine. 2019. *Divergence*. [https://scholar.google.com/scholar?q=Divergence+Fu+2019][research_fu_et_al_2019_divergence]
- Fujimoto, Scott, and Shixiang Gu. 2021. "A Minimalist Approach to Offline Reinforcement Learning." In *Advances in Neural Information Processing Systems*. [https://papers.nips.cc/paper\_files/paper/2021/hash/a8166da05c5a094f7dc03724b41886e5-Abstract.html][research_fujimoto_gu_2021]
- Furuta, Hiroki, Yutaka Matsuo, and Shixiang Shane Gu. 2022. "Generalized Decision Transformer for Offline Hindsight Information Matching." In *International Conference on Learning Representations*. [https://openreview.net/forum?id=CAjxVodl\_v][research_furuta_matsuo_gu_2022_gdt]
- Gulcehre, Caglar, Ziyu Wang, Alexander Novikov, et al. 2020. "RL Unplugged: A Suite of Benchmarks for Offline Reinforcement Learning." *Advances in Neural Information Processing Systems* 33: 7248–59. [https://papers.nips.cc/paper/2020/hash/51200d29d1fc15f5a71c1dab4bb54f7c-Abstract.html][research_gulcehre_et_al_2020]
- Hanna, Josiah P., Peter Stone, and Scott Niekum. 2016. "Bootstrapping with Models: Confidence Intervals for off-Policy Evaluation." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1606.06126][research_hanna_stone_niekum_2017]
- Hansen-Estruch, Philippe, Ilya Kostrikov, Michael Janner, Jakub Grudzien Kuba, and Sergey Levine. 2023. "IDQL: Implicit Q-Learning as an Actor-Critic Method with Diffusion Policies." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2304.10573][research_hansen_estruch_et_al_2023]
- Hejna, Joey, Rafael Rafailov, Harshit Sikchi, et al. 2023. "Contrastive Preference Learning: Learning from Human Feedback without RL." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2310.13639][research_hejna_et_al_2023]
- Jang, Eric, Alex Irpan, Mohi Khansari, et al. 2022. "BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning." In *Conference on Robot Learning*. [https://proceedings.mlr.press/v164/jang22a.html][research_jang_et_al_2022_bcz]
- Janner, Michael, Qiyang Li, and Sergey Levine. 2021. "Offline Reinforcement Learning as One Big Sequence Modeling Problem." In *Advances in Neural Information Processing Systems*. [https://papers.nips.cc/paper\_files/paper/2021/hash/099fe6b0b444c23836c4a5d07346082b-Abstract.html][research_janner_li_levine_2021_tt]
- Jaques, Natasha, Asma Ghandeharioun, Judy Hanwen Shen, et al. 2019. "Way off-Policy Batch Deep Reinforcement Learning of Implicit Human Preferences in Dialog." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1907.00456][research_jaques_et_al_2019]
- Jiang, Nan, and Lihong Li. 2016. "Doubly Robust off-Policy Value Evaluation for Reinforcement Learning." In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v48/jiang16.html][research_jiang_li_2016_offline]
- Jin, Ying, Zhuoran Yang, and Zhaoran Wang. 2021. "Is Pessimism Provably Efficient for Offline RL?" In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v139/jin21e.html][research_jin_yang_wang_2021]
- Kallus, Nathan, and Masatoshi Uehara. 2020. "Double Reinforcement Learning for Efficient off-Policy Evaluation in Markov Decision Processes." *Journal of Machine Learning Research* 21: 1–63. [https://jmlr.org/papers/v21/19-827.html][research_kallus_uehara_2020]
- Kang, Bingyi, Xiao Ma, Chao Du, Tianyu Pang, and Shuicheng Yan. 2023. "Efficient Diffusion Policies for Offline Reinforcement Learning." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2305.20081][research_kang_yang_wang_2023_efficient_diffusion]
- Kidambi, Rahul, Aravind Rajeswaran, Praneeth Netrapalli, and Thorsten Joachims. 2020. "MOReL: Model-Based Offline Reinforcement Learning." In *Advances in Neural Information Processing Systems*. [https://papers.nips.cc/paper\_files/paper/2020/hash/f7efa4f864ae9b88d43527f4b14f750f-Abstract.html][research_kidambi_et_al_2020_morel]
- Kim, Changyeon, Jongjin Park, Jinwoo Shin, Honglak Lee, Pieter Abbeel, and Kimin Lee. 2023. "Preference Transformer: Modeling Human Preferences Using Transformers for RL." In *The Eleventh International Conference on Learning Representations*. [https://openreview.net/forum?id=Peot1SFDX0][research_kim_et_al_2023_pt]
- Kim, Moo Jin, Karl Pertsch, Siddharth Karamcheti, et al. 2024. "OpenVLA: An Open-Source Vision-Language-Action Model." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2406.09246][research_kim_et_al_2024_openvla]
- Kostrikov, Ilya, Rob Fergus, Jonathan Tompson, and Ofir Nachum. 2021. "Offline Reinforcement Learning with Fisher Divergence Critic Regularization." In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v139/kostrikov21a.html][research_kostrikov_et_al_2021]
- Kumar, Aviral, Rishabh Agarwal, Tengyu Ma, Aaron Courville, George Tucker, and Sergey Levine. 2021a. "DR3: Value-Based Deep Reinforcement Learning Requires Explicit Regularization." In *International Conference on Learning Representations*. [https://openreview.net/forum?id=POvMvLi91f][research_kumar_et_al_2021_dr3]
- Kumar, Aviral, Anikait Singh, Stephen Tian, Chelsea Finn, and Sergey Levine. 2021b. "A Workflow for Offline Model-Free Robotic Reinforcement Learning." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2109.10813][research_kumar_singh_tucker_levine_2021]
- Lakshminarayanan, Balaji, Alexander Pritzel, and Charles Blundell. 2017. "Simple and Scalable Predictive Uncertainty Estimation Using Deep Ensembles." *Advances in Neural Information Processing Systems* 30. [https://papers.nips.cc/paper/2017/hash/9ef2ed4b7fd2c810847ffa5fa85bce38-Abstract.html][research_lakshminarayanan_pritzel_blundell_2017]
- Lange, Sascha, Thomas Gabel, and Martin Riedmiller. 2012. "Batch Reinforcement Learning." In *Adaptation, Learning, and Optimization*. Springer Berlin Heidelberg. [https://doi.org/10.1007/978-3-642-27645-3\_2][research_lange_gabel_riedmiller_2012]
- Le, Hoang, Cameron Voloshin, and Yisong Yue. 2019. "Batch Policy Learning under Constraints." In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v97/le19a.html][research_le_voloshin_yue_2019_constraints]
- Lee, Kimin, Laura Smith, Anca Dragan, and Pieter Abbeel. 2021. "B-Pref: Benchmarking Preference-Based Reinforcement Learning." In *Thirty-fifth Conference on Neural Information Processing Systems Datasets and Benchmarks Track (Round 1)*. [https://openreview.net/forum?id=ps95-mkHF\_][research_lee_smith_abbeel_2021_bpref]
- Levine, Sergey, Aviral Kumar, George Tucker, and Justin Fu. 2020. "Offline Reinforcement Learning: Tutorial, Review, and Perspectives on Open Problems." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2005.01643][research_levine_et_al_2020]
- Liu, Zuxin, Zijian Guo, Haohong Lin, et al. 2023. "Datasets and Benchmarks for Offline Safe Reinforcement Learning." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2306.09303][research_liu_ding_liu_2023_dsrl]
- Liu, Qiang, Lihong Li, Ziyang Tang, and Dengyong Zhou. 2018. "Breaking the Curse of Horizon: Infinite-Horizon off-Policy Estimation." *Advances in Neural Information Processing Systems* 31. [https://papers.nips.cc/paper/2018/hash/dda04f9d634145a9c68d5dfe53b21272-Abstract.html][research_liu_li_tang_zhou_2018]
- Lu, Cong, Philip J. Ball, Jack Parker-Holder, Michael A. Osborne, and Stephen J. Roberts. 2021. "Revisiting Design Choices in Offline Model-Based Reinforcement Learning." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2110.04135][research_lu_et_al_2022_design]
- Lu, Cheng, Huayu Chen, Jianfei Chen, Hang Su, Chongxuan Li, and Jun Zhu. 2023. "Contrastive Energy Prediction for Exact Energy-Guided Diffusion Sampling in Offline Reinforcement Learning." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2304.12824][research_lu_et_al_2023_cep]
- Munos, Remi, Tom Stepleton, Anna Harutyunyan, and Marc Bellemare. 2016. "Safe and Efficient off-Policy Reinforcement Learning." *Advances in Neural Information Processing Systems* 29. [https://papers.nips.cc/paper/2016/hash/c3992e9a68c5ae12bd18488bc579b30d-Abstract.html][research_munos_et_al_2016_retrace]
- Nachum, Ofir, Yinlam Chow, Bo Dai, and Lihong Li. 2019. "DualDICE: Behavior-Agnostic Estimation of Discounted Stationary Distribution Corrections." *Advances in Neural Information Processing Systems* 32. [https://papers.nips.cc/paper/2019/hash/cf9a242b70f45317ffd281241fa66502-Abstract.html][research_nachum_et_al_2019_dualdice]
- Nair, Ashvin, Abhishek Gupta, Murtaza Dalal, and Sergey Levine. 2020. "AWAC: Accelerating Online Reinforcement Learning with Offline Datasets." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2006.09359][research_nair_et_al_2020_awac]
- Nair, Rajeswaran, Kumar, Finn, and Gupta. 2022. *Robotic RL at Scale*. [https://scholar.google.com/scholar?q=Robotic+RL+at+Scale+Nair+2022][research_nair_et_al_2022_rrl]
- Nakamoto, Mitsuhiko, Simon Zhai, Anikait Singh, et al. 2023. "Cal-QL: Calibrated Offline RL Pre-Training for Efficient Online Fine-Tuning." In *Advances in Neural Information Processing Systems*. [https://papers.nips.cc/paper\_files/paper/2023/hash/c44a04289beaf0a7d968a94066a1d696-Abstract-Conference.html][research_nakamoto_et_al_2023]
- Nguyen-Tang, Thanh, Sunil Gupta, A. Tuan Nguyen, and Svetha Venkatesh. 2021. "Offline Neural Contextual Bandits: Pessimism, Optimization and Generalization." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2111.13807][research_nguyen_tang_et_al_2022]
- Octo, Model, and Team. 2024. *\[Title not identified\]*. [https://scholar.google.com/scholar?q=Octo+Model+Team+2024][research_octo_model_team_2024]
- Osband, Ian, Charles Blundell, Alexander Pritzel, and Benjamin Van Roy. 2016. "Deep Exploration via Bootstrapped DQN." *Advances in Neural Information Processing Systems* 29. [https://papers.nips.cc/paper/2016/hash/8d8818c8e140c64c743113f563cf750f-Abstract.html][research_osband_et_al_2016_bootstrapped_dqn]
- Ouyang, Long, Jeffrey Wu, Xu Jiang, et al. 2022. "Training Language Models to Follow Instructions with Human Feedback." In *Advances in Neural Information Processing Systems 35*. Neural Information Processing Systems Foundation, Inc. (NeurIPS). [https://doi.org/10.52202/068431-2011][research_ouyang_et_al_2022_instructgpt]
- Paine, Tom Le, Cosmin Paduraru, Andrea Michi, et al. 2020. "Hyperparameter Selection for Offline Reinforcement Learning." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2007.09055][research_paine_et_al_2020]
- Peng, Xue Bin, Aviral Kumar, Grace Zhang, and Sergey Levine. 2019. "Advantage-Weighted Regression: Simple and Scalable off-Policy Reinforcement Learning." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1910.00177][research_peng_kumar_zhang_levine_2019]
- Pomerleau, Dean A. 1988. "ALVINN: An Autonomous Land Vehicle in a Neural Network." *Advances in Neural Information Processing Systems* 1. [https://papers.nips.cc/paper/1988/hash/812b4ba287f5ee0bc9d43bbf5bbe87fb-Abstract.html][research_pomerleau_1988_alvinn]
- Prudencio, Rafael Figueiredo, Marcos R. O. A. Maximo, and Esther Luna Colombini. 2022. "A Survey on Offline Reinforcement Learning: Taxonomy, Review, and Open Problems." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2203.01387][research_prudencio_maximo_colombini_2023]
- Rafailov, Rafael, Archit Sharma, Eric Mitchell, Christopher D. Manning, Stefano Ermon, and Chelsea Finn. 2023. "Direct Preference Optimization: Your Language Model Is Secretly a Reward Model." In *Advances in Neural Information Processing Systems 36*. Neural Information Processing Systems Foundation, Inc. (NeurIPS). [https://doi.org/10.52202/075280-2338][research_rafailov_et_al_2023_dpo]
- Rajeswaran, Aravind, Vikash Kumar, Abhishek Gupta, et al. 2017. "Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1709.10087][research_rajeswaran_et_al_2018_dapg]
- Reed, Scott, Konrad Zolna, Emilio Parisotto, et al. 2022. "A Generalist Agent." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2205.06175][research_reed_et_al_2022_gato_offline]
- Sadigh, Dragan, Sastry, and Seshia. 2017. *\[Title not identified\]*. [https://scholar.google.com/scholar?q=Sadigh+Dragan+Sastry+2017][research_sadigh_et_al_2017]
- Singh, Avi, Albert Yu, Jonathan Yang, Jesse Zhang, Aviral Kumar, and Sergey Levine. 2020. "COG: Connecting New Skills to past Experience with Offline Reinforcement Learning." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2010.14500][research_singh_et_al_2020_cog]
- Sohl-Dickstein, Jascha, Eric Weiss, Niru Maheswaranathan, and Surya Ganguli. 2015. "Deep Unsupervised Learning Using Nonequilibrium Thermodynamics." In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v37/sohl-dickstein15.html][research_sohl_dickstein_et_al_2015]
- Sun, Zheng, Ma, and Wu. 2023. *MOBILE*. [https://scholar.google.com/scholar?q=MOBILE+Sun+2023][research_sun_et_al_2023_mobile]
- Tarasov, Denis, Vladislav Kurenkov, Alexander Nikulin, and Sergey Kolesnikov. 2023b. "Revisiting the Minimalist Approach to Offline Reinforcement Learning." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2305.09836][research_nikulin_et_al_2023_rebrac]
- Tarasov, Denis, Alexander Nikulin, Dmitry Akimov, Vladislav Kurenkov, and Sergey Kolesnikov. 2023a. "CORL: Research-Oriented Deep Offline Reinforcement Learning Library." In *Advances in Neural Information Processing Systems 36*. Neural Information Processing Systems Foundation, Inc. (NeurIPS). [https://doi.org/10.52202/075280-1351][research_tarasov_et_al_2022]
- Torabi, Faraz, Garrett Warnell, and Peter Stone. 2018. "Behavioral Cloning from Observation." In *Proceedings of the Twenty-Seventh International Joint Conference on Artificial Intelligence*. International Joint Conferences on Artificial Intelligence Organization. [https://doi.org/10.24963/ijcai.2018/687][research_torabi_warnell_stone_2018]
- Uchendu, Ikechukwu, Ted Xiao, Yao Lu, et al. 2023. "Jump-Start Reinforcement Learning." In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v202/uchendu23a.html][research_uchendu_et_al_2023_jumpstart]
- Uehara, Masatoshi, Jiawei Huang, and Nan Jiang. 2020. "Minimax Weight and Q-Function Learning for off-Policy Evaluation." In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v119/uehara20a.html][research_uehara_huang_jiang_2020]
- Uehara, Masatoshi, and Wen Sun. 2022. "Pessimistic Model-Based Offline Reinforcement Learning under Partial Coverage." In *International Conference on Learning Representations*. [https://openreview.net/forum?id=tyrJsbKAe6][research_uehara_sun_2022]
- van Hasselt. 2010. *\[Title not identified\]*. [https://scholar.google.com/scholar?q=van+Hasselt+2010][research_van_hasselt_2010]
- Wang, Ruosong, Dean P. Foster, and Sham M. Kakade. 2020. "What Are the Statistical Limits of Offline RL with Linear Function Approximation?" Preprint, arXiv. [https://doi.org/10.48550/arxiv.2010.11895][research_wang_foster_kakade_2021]
- Wilson, Matthew A., and Bruce L. McNaughton. 1994. "Reactivation of Hippocampal Ensemble Memories during Sleep." *Science* 265 (5172): 676–79. [https://doi.org/10.1126/science.8036517][research_wilson_mcnaughton_1994]
- Wirth, Christian, Riad Akrour, Gerhard Neumann, and Johannes Fürnkranz. 2017. "A Survey of Preference-Based Reinforcement Learning Methods." *Journal of Machine Learning Research* 18: 1–46. [https://jmlr.org/papers/v18/16-634.html][research_wirth_et_al_2017]
- Wu, Yifan, George Tucker, and Ofir Nachum. 2019. "Behavior Regularized Offline Reinforcement Learning." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1911.11361][research_wu_tucker_nachum_2019]
- Wu, Jialong, Haixu Wu, Zihan Qiu, Jianmin Wang, and Mingsheng Long. 2022. "Supported Policy Optimization for Offline Reinforcement Learning." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2202.06239][research_wu_sun_sen_zhu_zhang_2022]
- Xie, Tengyang, Ching-An Cheng, Nan Jiang, Paul Mineiro, and Alekh Agarwal. 2021. "Bellman-Consistent Pessimism for Offline Reinforcement Learning." In *Advances in Neural Information Processing Systems*. [https://papers.nips.cc/paper\_files/paper/2021/hash/34f98c7c5d7063181da890ea8d25265a-Abstract.html][research_xie_et_al_2021]
- Xie, Tengyang, Yifei Ma, and Yu-Xiang Wang. 2019. "Towards Optimal off-Policy Evaluation for Reinforcement Learning with Marginalized Importance Sampling." *Advances in Neural Information Processing Systems* 32. [https://papers.nips.cc/paper/2019/hash/4ffb0d2ba92f664c2281970110a2e071-Abstract.html][research_xie_ma_wang_2019_optimal]
- Xu, Haoran, Xianyuan Zhan, and Xiangyu Zhu. 2021. "Constraints Penalized Q-Learning for Safe Offline Reinforcement Learning." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2107.09003][research_xu_zhan_zhu_2022]
- Yang, Rui, Chenjia Bai, Xiaoteng Ma, Zhaoran Wang, Chongjie Zhang, and Lei Han. 2022. "RORL: Robust Offline Reinforcement Learning via Conservative Smoothing." In *Advances in Neural Information Processing Systems*. [https://papers.nips.cc/paper\_files/paper/2022/hash/96bbdd0ed2a9e7cd2fb7caf2fae15f3d-Abstract-Conference.html][research_yang_et_al_2022_rorl]
- Yu, Tianhe, Aviral Kumar, Rafael Rafailov, Aravind Rajeswaran, Sergey Levine, and Chelsea Finn. 2021. "COMBO: Conservative Offline Model-Based Policy Optimization." *Advances in Neural Information Processing Systems* 34: 28954–67. [https://papers.nips.cc/paper/2021/hash/f29a179746902e331572c483c45e5086-Abstract.html][research_yu_et_al_2021_combo]
- Yu, Tianhe, Garrett Thomas, Lantao Yu, et al. 2020. "MOPO: Model-Based Offline Policy Optimization." *Advances in Neural Information Processing Systems* 33: 14129–42. [https://papers.nips.cc/paper/2020/hash/a322852ce0df73e204b7e67cbbef0d0a-Abstract.html][research_yu_et_al_2020_mopo]
- Zhang, Haichao, We Xu, and Haonan Yu. 2023. "Policy Expansion for Bridging Offline-to-Online Reinforcement Learning." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2302.00935][research_zhang_et_al_2023_policy_expansion]
- Zheng. 2023. *Online Finetune*. [https://scholar.google.com/scholar?q=Online+Finetune+Zheng+2023][research_zheng_et_al_2023_finetune]

### Secondary Sources

- Bertsekas and Tsitsiklis. 1996. *Textbook: Neuro-Dynamic Programming*. [http://athenasc.com/ndpbook.html][book_bertsekas_tsitsiklis_1996]
- Sutton, Richard S., and Barto. 2018. *Reinforcement Learning: An Introduction*. MIT Press. [http://incompleteideas.net/book/the-book-2nd.html][book_sutton_barto_2018]

### Commercial Sources

- "DeepMind x UCL RL Course." n.d. Accessed October 25, 2026. [https://www.deepmind.com/learning-resources/reinforcement-learning-lecture-series-2021][ref_deepmind_ucl_rl]
- "Welcome to Spinning up in Deep RL! — Spinning up Documentation." n.d. Accessed October 25, 2026. [https://spinningup.openai.com/][ref_openai_spinning_up]

### General Sources

- Achiam Held Tamar Abbeel. 2017. "CPO." [https://proceedings.mlr.press/v70/achiam17a.html][research_achiam_et_al_2017_cpo]
- Ajay, Du, Gupta, et al. 2023. "\[Title not identified\]." Accessed October 25, 2026. [https://openreview.net/forum?id=Cw5uJx8XLU][research_ajay_et_al_2023_decision_diffuser]
- Bai, Wang, Xu, et al. 2022. "PBRL." [https://openreview.net/forum?id=Y4cs1Z3HnqL][research_bai_et_al_2022_pbrl]
- Bain and Sammut. 1995. "\[Title not identified\]." Accessed October 25, 2026. [https://scholar.google.com/scholar?q=bain+sammut+1995+behavioural+cloning][research_bain_sammut_1995]
- Baird. 1995. "\[Title not identified\]." Accessed October 25, 2026. [https://www.sciencedirect.com/science/article/pii/B9781558603776500285][research_baird_1995]
- Ball Smith Kostrikov Levine. 2023. "RLPD." [https://proceedings.mlr.press/v202/ball23a.html][research_ball_et_al_2023_rlpd]
- "Berkeley CS285." n.d. Accessed October 25, 2026. [https://rail.eecs.berkeley.edu/deeprlcourse/][ref_berkeley_cs285]
- Chen Wang Zhou Ross. 2021. "REDQ." [https://openreview.net/forum?id=AY8zfZm0tDd][research_chen_wang_zhou_ross_2021_redq]
- Cheng Xie Jiang Agarwal. 2022. "ATAC." [https://proceedings.mlr.press/v162/cheng22b.html][research_cheng_et_al_2022_atac]
- Emmons Eysenbach Kostrikov Levine. 2021. "RvS." [https://openreview.net/forum?id=S874XAIpkR-][research_emmons_et_al_2021]
- Farajtabar Chow Ghavamzadeh. 2018. "MRDR." [https://proceedings.mlr.press/v80/farajtabar18a.html][research_farajtabar_chow_ghavamzadeh_2018]
- Fu. 2021. "DOPE." [https://openreview.net/forum?id=kWSeGEeHvF8][research_fu_et_al_2021]
- Fujimoto, Meger, and Precup. 2019. "BCQ." [https://proceedings.mlr.press/v97/fujimoto19a.html][research_fujimoto_meger_precup_2019]
- Ghasemipour Gu Nachum. 2022. "SAC-RND." [https://proceedings.mlr.press/v162/ghasemipour22a.html][research_ghasemipour_gu_nachum_2022]
- Gordon. 1995. "\[Title not identified\]." Accessed October 25, 2026. [https://www.sciencedirect.com/science/article/pii/B9781558603776500325][research_gordon_1995]
- Ho and Ermon. 2016. "GAIL." [https://papers.nips.cc/paper/2016/hash/cc7e2b878868cbae992d1fb743995d8f-Abstract.html][research_ho_ermon_2016_gail]
- Ho Jain Abbeel. 2020. "DDPM." [https://papers.nips.cc/paper/2020/hash/4c5bcfec8584af0d967f1ab10179ca4b-Abstract.html][research_ho_jain_abbeel_2020_ddpm]
- Janner, Du, and Song. 2022. "Diffuser." [https://proceedings.mlr.press/v162/janner22a.html][research_janner_du_song_2022]
- Kalashnikov. 2018. "QT-Opt." [https://proceedings.mlr.press/v87/kalashnikov18a.html][research_kalashnikov_et_al_2018]
- Kostrikov Nair Levine. 2022. "IQL." [https://openreview.net/forum?id=68n2s9ZJWF8][research_kostrikov_nair_levine_2022]
- Kumar, Hong, Levine, and Tucker. 2022. "\[Title not identified\]." Accessed October 25, 2026. [https://openreview.net/forum?id=WwbSsEO5tKI][research_kumar_hong_levine_tucker_2022]
- Kumar Fu Tucker Levine. 2019. "BEAR." [https://papers.nips.cc/paper/2019/hash/c2073ffa77b5357a498057413bb09d3a-Abstract.html][research_kumar_et_al_2019_bear]
- Kumar Zhou Tucker Levine. 2020. "CQL." [https://papers.nips.cc/paper/2020/hash/0d2b2061826a5df3221116a5085a6052-Abstract.html][research_kumar_zhou_tucker_levine_2020]
- Le Voloshin Yue. 2019. "FQE." [https://proceedings.mlr.press/v97/le19a.html][research_le_voloshin_yue_2019]
- Lee. 2022. "Multi-Game DT." [https://papers.nips.cc/paper/2022/hash/b2c1c92e2c9c31e5b21e4ada58cfd7de-Abstract-Conference.html][research_lee_et_al_2022_mgdt]
- Lee Jeon Kim Kim. 2022. "COptiDICE." [https://openreview.net/forum?id=RfL3XwZaMoI][research_lee_et_al_2022_coptidice]
- Lee Seo Lee Abbeel Shin. 2022. "Balanced Replay." [https://openreview.net/forum?id=Xd4-6HQY\_C\_][research_lee_et_al_2022_balanced_replay]
- Lee Smith Krishnan Abbeel. 2021. "PEBBLE." [https://proceedings.mlr.press/v139/lee21e.html][research_lee_smith_krishnan_abbeel_2021_pebble]
- Matsushima, Furuta, Matsuo, Nachum, and Gu. 2021. "BREMEN." [https://openreview.net/forum?id=3hGNqpI4WS][research_matsushima_et_al_2021_bremen]
- O'Neill, Pleydell-Bouverie, Dupret, and Csicsvari. 2010. "\[Title not identified\]." Accessed October 25, 2026. [https://www.cell.com/trends/neurosciences/fulltext/S0166-2236(10)00003-3][research_oneill_et_al_2010]
- Ólafsdóttir, Bush, and Barry. 2018. "\[Title not identified\]." Accessed October 25, 2026. [https://www.cell.com/current-biology/fulltext/S0960-9822(17)31517-5][research_olafsdottir_bush_barry_2018]
- Pearce, Rashid, Kanervisto, et al. 2023. "Human Diffusion." [https://openreview.net/forum?id=Pv1GPQzRrC8][research_pearce_et_al_2023]
- Precup, Sutton, and Dasgupta. 2001. "\[Title not identified\]." Accessed October 25, 2026. [https://scholar.google.com/scholar?q=precup+sutton+dasgupta+2001+off-policy+temporal+difference][research_precup_sutton_dasgupta_2001]
- Precup, Sutton, and Singh. 2000. "\[Title not identified\]." Accessed October 25, 2026. [https://proceedings.mlr.press/v98/precup00a.html][research_precup_sutton_singh_2000_offline]
- Rafailov, Yu, Rajeswaran, and Finn. 2021. "LOMPO." [https://openreview.net/forum?id=fEXW1DEeD-h][research_rafailov_et_al_2021_lompo]
- Rashidinejad, Zhu, Jiao, and Russell. 2021. "\[Title not identified\]." Accessed October 25, 2026. [https://papers.nips.cc/paper/2021/hash/6ea9ab1baa0efb9e19094440c317e21b-Abstract.html][research_rashidinejad_et_al_2021]
- Rigter Lacerda Hawes. 2022. "RAMBO." [https://papers.nips.cc/paper/2022/hash/6d4e9c5db4f01e26c0dbf65d5b62e9c9-Abstract-Conference.html][research_rigter_lacerda_hawes_2022_rambo]
- Ross Gordon Bagnell. 2011. "DAgger." [https://proceedings.mlr.press/v15/ross11a.html][research_ross_gordon_bagnell_2011]
- Siegel, Springenberg, Berkenkamp, et al. 2020. "ABM." [https://openreview.net/forum?id=rke7geHtwH][research_siegel_et_al_2020_abm]
- "Silver RL Course UCL." n.d. Accessed October 25, 2026. [https://www.davidsilver.uk/teaching/][ref_silver_rl_course]
- "Stanford CS234." n.d. Accessed October 25, 2026. [https://web.stanford.edu/class/cs234/][ref_stanford_cs234]
- Thomas and Brunskill. 2016. "DR-OPE." [https://proceedings.mlr.press/v48/thomasa16.html][research_thomas_brunskill_2016]
- Thrun and Schwartz. 1993. "Issues in Using Function Approximation for Reinforcement Learning." Robotics Institute Carnegie Mellon University. Accessed October 25, 2026. [https://www.ri.cmu.edu/publications/issues-in-using-function-approximation-for-reinforcement-learning/][research_thrun_schwartz_1993]
- Wang. 2020. "CRR." [https://papers.nips.cc/paper/2020/hash/588cb956d6bbe67078f29f8de420a13d-Abstract.html][research_wang_et_al_2020_crr]
- Wang, Hunt, and Zhou. 2022. "Diffusion-QL." [https://openreview.net/forum?id=AHvFDPi-FA][research_wang_hunt_zhou_2022]
- Watkins. 1989. "Q-Learning." [https://www.cs.rhul.ac.uk/~chrisw/new\_thesis.pdf][research_watkins_1989_thesis]
- Wu, Zhai, Kolter, Levine, and Ba. 2021. "UWAC." [https://proceedings.mlr.press/v139/wu21i.html][research_wu_et_al_2021_uwac]
- Wu Wang Reed Lee. 2023. "Elastic DT." [https://proceedings.mlr.press/v202/wu23p.html][research_wu_wang_reed_lee_2023_edt]
- Yin and Wang. 2021. "\[Title not identified\]." Accessed October 25, 2026. [https://proceedings.mlr.press/v139/yin21b.html][research_yin_wang_2021]
- Yu, Kumar, Chebotar, Hausman, Finn, and Levine. 2022. "UDS." [https://openreview.net/forum?id=5R6qHYqhHIS][research_yu_et_al_2022_uds]
- Zhan, Ren, Yin, and Zhu. 2022. "\[Title not identified\]." Accessed October 25, 2026. [https://openreview.net/forum?id=Cw5uJx8XLU][research_zhan_ren_yin_zhu_2022]
- Zheng Zhang Grover. 2022. "ODT." [https://proceedings.mlr.press/v162/zheng22c.html][research_zheng_zhang_grover_2022_odt]

### Related Posts

- Sechter, Brendan. 2025. "Machines That Learn From Experience: Framing." *Brendan A R Sechter's Development Blog*, December 18. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/18/machines\_that\_learn\_from\_experience\_framing.html][related_post_a250_framing]
- Sechter, Brendan. 2025. "Machines That Learn From Experience: Bandits and Online Learning." *Brendan A R Sechter's Development Blog*, December 19. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/19/machines\_that\_learn\_from\_experience\_bandits\_and\_online\_learning.html][related_post_a251_bandits]
- Sechter, Brendan. 2025. "Machines That Learn From Experience: Reinforcement Learning Foundations." *Brendan A R Sechter's Development Blog*, December 20. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/20/machines\_that\_learn\_from\_experience\_reinforcement\_learning\_foundations.html][related_post_a252_rl_foundations]
- Sechter, Brendan. 2025. "Machines That Learn From Experience: Deep Reinforcement Learning." *Brendan A R Sechter's Development Blog*, December 21. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/21/machines\_that\_learn\_from\_experience\_deep\_reinforcement\_learning.html][related_post_a253_deep_rl]
- Sechter, Brendan. 2025. "Machines That Learn From Experience: Exploration, Intrinsic Motivation, and Curiosity." *Brendan A R Sechter's Development Blog*, December 22. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/22/machines\_that\_learn\_from\_experience\_exploration\_intrinsic\_motivation\_and\_curiosity.html][related_post_a254_exploration]
- Sechter, Brendan. 2025. "Machines That Learn From Experience: Hierarchical Reinforcement Learning." *Brendan A R Sechter's Development Blog*, December 23. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/23/machines\_that\_learn\_from\_experience\_hierarchical\_reinforcement\_learning.html][related_post_a255_hierarchical]
- Sechter, Brendan. 2025. "Machines That Learn From Experience: World Models and Predictive, Model-Based Adaptation." *Brendan A R Sechter's Development Blog*, December 24. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/24/machines\_that\_learn\_from\_experience\_world\_models\_and\_predictive\_model\_based\_adaptation.html][related_post_a256_world_models]

[book_bertsekas_tsitsiklis_1996]: http://athenasc.com/ndpbook.html
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
[research_achiam_et_al_2017_cpo]: https://proceedings.mlr.press/v70/achiam17a.html
[research_agarwal_schuurmans_norouzi_2020]: https://proceedings.mlr.press/v119/agarwal20c.html
[research_ajay_et_al_2023_decision_diffuser]: https://openreview.net/forum?id=Cw5uJx8XLU
[research_an_et_al_2021]: https://papers.nips.cc/paper/2021/hash/3d3d286a8d153a4a58156d0e02d8570c-Abstract.html
[research_antos_szepesvari_munos_2008]: https://doi.org/10.1007/s10994-007-5038-2
[research_argenson_dulac_arnold_2021_mbop]: https://doi.org/10.48550/arxiv.2008.05556
[research_bai_et_al_2022_pbrl]: https://openreview.net/forum?id=Y4cs1Z3HnqL
[research_bain_sammut_1995]: https://scholar.google.com/scholar?q=bain+sammut+1995+behavioural+cloning
[research_baird_1995]: https://www.sciencedirect.com/science/article/pii/B9781558603776500285
[research_ball_et_al_2023_rlpd]: https://proceedings.mlr.press/v202/ball23a.html
[research_bousmalis_et_al_2023]: https://doi.org/10.48550/arxiv.2306.11706
[research_brandfonbrener_et_al_2022]: https://papers.nips.cc/paper_files/paper/2022/hash/0a2f65c9d2313b71005e600bd23393fe-Abstract-Conference.html
[research_brohan_et_al_2022_rt1]: https://doi.org/10.48550/arxiv.2212.06817
[research_brohan_et_al_2023_rt2]: https://doi.org/10.48550/arxiv.2307.15818
[research_buckman_gelada_bellemare_2020]: https://doi.org/10.48550/arxiv.2009.06799
[research_chebotar_et_al_2023_q_transformer]: https://doi.org/10.48550/arxiv.2309.10150
[research_chen_et_al_2019_youtube]: https://doi.org/10.1145/3289600.3290999
[research_chen_et_al_2021_dt]: https://papers.nips.cc/paper/2021/hash/7f489f642a0ddb10272b5c31057f0663-Abstract.html
[research_chen_jiang_2019]: https://proceedings.mlr.press/v97/chen19e.html
[research_chen_wang_zhou_ross_2021_redq]: https://openreview.net/forum?id=AY8zfZm0tDd
[research_chen_xu_vella_zhou_2023]: https://scholar.google.com/scholar?q=Chen+Xu+Vella+2023
[research_cheng_et_al_2022_atac]: https://proceedings.mlr.press/v162/cheng22b.html
[research_chi_et_al_2023_diffusion_policy]: https://doi.org/10.48550/arxiv.2303.04137
[research_chow_et_al_2017]: https://jmlr.org/papers/v18/15-636.html
[research_christiano_et_al_2017_rlhf]: https://papers.nips.cc/paper/2017/hash/d5e2c0adad503c91f91df240d0cd4e49-Abstract.html
[research_driess_et_al_2023_palme]: https://doi.org/10.48550/arxiv.2303.03378
[research_emmons_et_al_2021]: https://openreview.net/forum?id=S874XAIpkR-
[research_ernst_geurts_wehenkel_2005_offline]: https://www.jmlr.org/papers/v6/ernst05a.html
[research_farajtabar_chow_ghavamzadeh_2018]: https://proceedings.mlr.press/v80/farajtabar18a.html
[research_foster_wilson_2006]: https://doi.org/10.1038/nature04587
[research_fu_et_al_2019_divergence]: https://scholar.google.com/scholar?q=Divergence+Fu+2019
[research_fu_et_al_2020_d4rl]: https://doi.org/10.48550/arxiv.2004.07219
[research_fu_et_al_2021]: https://openreview.net/forum?id=kWSeGEeHvF8
[research_fujimoto_gu_2021]: https://papers.nips.cc/paper_files/paper/2021/hash/a8166da05c5a094f7dc03724b41886e5-Abstract.html
[research_fujimoto_meger_precup_2019]: https://proceedings.mlr.press/v97/fujimoto19a.html
[research_furuta_matsuo_gu_2022_gdt]: https://openreview.net/forum?id=CAjxVodl_v
[research_ghasemipour_gu_nachum_2022]: https://proceedings.mlr.press/v162/ghasemipour22a.html
[research_gordon_1995]: https://www.sciencedirect.com/science/article/pii/B9781558603776500325
[research_gulcehre_et_al_2020]: https://papers.nips.cc/paper/2020/hash/51200d29d1fc15f5a71c1dab4bb54f7c-Abstract.html
[research_hanna_stone_niekum_2017]: https://doi.org/10.48550/arxiv.1606.06126
[research_hansen_estruch_et_al_2023]: https://doi.org/10.48550/arxiv.2304.10573
[research_hejna_et_al_2023]: https://doi.org/10.48550/arxiv.2310.13639
[research_ho_ermon_2016_gail]: https://papers.nips.cc/paper/2016/hash/cc7e2b878868cbae992d1fb743995d8f-Abstract.html
[research_ho_jain_abbeel_2020_ddpm]: https://papers.nips.cc/paper/2020/hash/4c5bcfec8584af0d967f1ab10179ca4b-Abstract.html
[research_jang_et_al_2022_bcz]: https://proceedings.mlr.press/v164/jang22a.html
[research_janner_du_song_2022]: https://proceedings.mlr.press/v162/janner22a.html
[research_janner_li_levine_2021_tt]: https://papers.nips.cc/paper_files/paper/2021/hash/099fe6b0b444c23836c4a5d07346082b-Abstract.html
[research_jaques_et_al_2019]: https://doi.org/10.48550/arxiv.1907.00456
[research_jiang_li_2016_offline]: https://proceedings.mlr.press/v48/jiang16.html
[research_jin_yang_wang_2021]: https://proceedings.mlr.press/v139/jin21e.html
[research_kalashnikov_et_al_2018]: https://proceedings.mlr.press/v87/kalashnikov18a.html
[research_kallus_uehara_2020]: https://jmlr.org/papers/v21/19-827.html
[research_kang_yang_wang_2023_efficient_diffusion]: https://doi.org/10.48550/arxiv.2305.20081
[research_kidambi_et_al_2020_morel]: https://papers.nips.cc/paper_files/paper/2020/hash/f7efa4f864ae9b88d43527f4b14f750f-Abstract.html
[research_kim_et_al_2023_pt]: https://openreview.net/forum?id=Peot1SFDX0
[research_kim_et_al_2024_openvla]: https://doi.org/10.48550/arxiv.2406.09246
[research_komorowski_et_al_2018]: https://doi.org/10.1038/s41591-018-0213-5
[research_kostrikov_et_al_2021]: https://proceedings.mlr.press/v139/kostrikov21a.html
[research_kostrikov_nair_levine_2022]: https://openreview.net/forum?id=68n2s9ZJWF8
[research_kumar_et_al_2019_bear]: https://papers.nips.cc/paper/2019/hash/c2073ffa77b5357a498057413bb09d3a-Abstract.html
[research_kumar_et_al_2021_dr3]: https://openreview.net/forum?id=POvMvLi91f
[research_kumar_hong_levine_tucker_2022]: https://openreview.net/forum?id=WwbSsEO5tKI
[research_kumar_singh_tucker_levine_2021]: https://doi.org/10.48550/arxiv.2109.10813
[research_kumar_zhou_tucker_levine_2020]: https://papers.nips.cc/paper/2020/hash/0d2b2061826a5df3221116a5085a6052-Abstract.html
[research_lakshminarayanan_pritzel_blundell_2017]: https://papers.nips.cc/paper/2017/hash/9ef2ed4b7fd2c810847ffa5fa85bce38-Abstract.html
[research_lange_gabel_riedmiller_2012]: https://doi.org/10.1007/978-3-642-27645-3_2
[research_le_voloshin_yue_2019]: https://proceedings.mlr.press/v97/le19a.html
[research_le_voloshin_yue_2019_constraints]: https://proceedings.mlr.press/v97/le19a.html
[research_lee_et_al_2022_balanced_replay]: https://openreview.net/forum?id=Xd4-6HQY_C_
[research_lee_et_al_2022_coptidice]: https://openreview.net/forum?id=RfL3XwZaMoI
[research_lee_et_al_2022_mgdt]: https://papers.nips.cc/paper/2022/hash/b2c1c92e2c9c31e5b21e4ada58cfd7de-Abstract-Conference.html
[research_lee_smith_abbeel_2021_bpref]: https://openreview.net/forum?id=ps95-mkHF_
[research_lee_smith_krishnan_abbeel_2021_pebble]: https://proceedings.mlr.press/v139/lee21e.html
[research_levine_et_al_2020]: https://doi.org/10.48550/arxiv.2005.01643
[research_liu_ding_liu_2023_dsrl]: https://doi.org/10.48550/arxiv.2306.09303
[research_liu_li_tang_zhou_2018]: https://papers.nips.cc/paper/2018/hash/dda04f9d634145a9c68d5dfe53b21272-Abstract.html
[research_lu_et_al_2022_design]: https://doi.org/10.48550/arxiv.2110.04135
[research_lu_et_al_2023_cep]: https://doi.org/10.48550/arxiv.2304.12824
[research_matsushima_et_al_2021_bremen]: https://openreview.net/forum?id=3hGNqpI4WS
[research_mattar_daw_2018]: https://doi.org/10.1038/s41593-018-0232-z
[research_munos_et_al_2016_retrace]: https://papers.nips.cc/paper/2016/hash/c3992e9a68c5ae12bd18488bc579b30d-Abstract.html
[research_nachum_et_al_2019_dualdice]: https://papers.nips.cc/paper/2019/hash/cf9a242b70f45317ffd281241fa66502-Abstract.html
[research_nair_et_al_2020_awac]: https://doi.org/10.48550/arxiv.2006.09359
[research_nair_et_al_2022_rrl]: https://scholar.google.com/scholar?q=Robotic+RL+at+Scale+Nair+2022
[research_nakamoto_et_al_2023]: https://papers.nips.cc/paper_files/paper/2023/hash/c44a04289beaf0a7d968a94066a1d696-Abstract-Conference.html
[research_nguyen_tang_et_al_2022]: https://doi.org/10.48550/arxiv.2111.13807
[research_nikulin_et_al_2023_rebrac]: https://doi.org/10.48550/arxiv.2305.09836
[research_octo_model_team_2024]: https://scholar.google.com/scholar?q=Octo+Model+Team+2024
[research_olafsdottir_bush_barry_2018]: https://www.cell.com/current-biology/fulltext/S0960-9822(17)31517-5
[research_oneill_et_al_2010]: https://www.cell.com/trends/neurosciences/fulltext/S0166-2236(10)00003-3
[research_osband_et_al_2016_bootstrapped_dqn]: https://papers.nips.cc/paper/2016/hash/8d8818c8e140c64c743113f563cf750f-Abstract.html
[research_ouyang_et_al_2022_instructgpt]: https://doi.org/10.52202/068431-2011
[research_padalkar_et_al_2024]: https://doi.org/10.48550/arxiv.2310.08864
[research_paine_et_al_2020]: https://doi.org/10.48550/arxiv.2007.09055
[research_pearce_et_al_2023]: https://openreview.net/forum?id=Pv1GPQzRrC8
[research_peng_kumar_zhang_levine_2019]: https://doi.org/10.48550/arxiv.1910.00177
[research_pfeiffer_foster_2013]: https://doi.org/10.1038/nature12112
[research_pomerleau_1988_alvinn]: https://papers.nips.cc/paper/1988/hash/812b4ba287f5ee0bc9d43bbf5bbe87fb-Abstract.html
[research_precup_sutton_dasgupta_2001]: https://scholar.google.com/scholar?q=precup+sutton+dasgupta+2001+off-policy+temporal+difference
[research_precup_sutton_singh_2000_offline]: https://proceedings.mlr.press/v98/precup00a.html
[research_prudencio_maximo_colombini_2023]: https://doi.org/10.48550/arxiv.2203.01387
[research_rafailov_et_al_2021_lompo]: https://openreview.net/forum?id=fEXW1DEeD-h
[research_rafailov_et_al_2023_dpo]: https://doi.org/10.52202/075280-2338
[research_rajeswaran_et_al_2018_dapg]: https://doi.org/10.48550/arxiv.1709.10087
[research_rashidinejad_et_al_2021]: https://papers.nips.cc/paper/2021/hash/6ea9ab1baa0efb9e19094440c317e21b-Abstract.html
[research_reed_et_al_2022_gato_offline]: https://doi.org/10.48550/arxiv.2205.06175
[research_riedmiller_2005_nfq]: https://doi.org/10.1007/11564096_32
[research_rigter_lacerda_hawes_2022_rambo]: https://papers.nips.cc/paper/2022/hash/6d4e9c5db4f01e26c0dbf65d5b62e9c9-Abstract-Conference.html
[research_ross_gordon_bagnell_2011]: https://proceedings.mlr.press/v15/ross11a.html
[research_sadigh_et_al_2017]: https://scholar.google.com/scholar?q=Sadigh+Dragan+Sastry+2017
[research_siegel_et_al_2020_abm]: https://openreview.net/forum?id=rke7geHtwH
[research_singh_et_al_2020_cog]: https://doi.org/10.48550/arxiv.2010.14500
[research_sohl_dickstein_et_al_2015]: https://proceedings.mlr.press/v37/sohl-dickstein15.html
[research_sun_et_al_2023_mobile]: https://scholar.google.com/scholar?q=MOBILE+Sun+2023
[research_sutton_1988_td]: https://doi.org/10.1007/bf00115009
[research_tarasov_et_al_2022]: https://doi.org/10.52202/075280-1351
[research_thomas_brunskill_2016]: https://proceedings.mlr.press/v48/thomasa16.html
[research_thrun_schwartz_1993]: https://www.ri.cmu.edu/publications/issues-in-using-function-approximation-for-reinforcement-learning/
[research_torabi_warnell_stone_2018]: https://doi.org/10.24963/ijcai.2018/687
[research_uchendu_et_al_2023_jumpstart]: https://proceedings.mlr.press/v202/uchendu23a.html
[research_uehara_huang_jiang_2020]: https://proceedings.mlr.press/v119/uehara20a.html
[research_uehara_sun_2022]: https://openreview.net/forum?id=tyrJsbKAe6
[research_van_hasselt_2010]: https://scholar.google.com/scholar?q=van+Hasselt+2010
[research_wang_et_al_2020_crr]: https://papers.nips.cc/paper/2020/hash/588cb956d6bbe67078f29f8de420a13d-Abstract.html
[research_wang_foster_kakade_2021]: https://doi.org/10.48550/arxiv.2010.11895
[research_wang_hunt_zhou_2022]: https://openreview.net/forum?id=AHvFDPi-FA
[research_watkins_1989_thesis]: https://www.cs.rhul.ac.uk/~chrisw/new_thesis.pdf
[research_wilson_mcnaughton_1994]: https://doi.org/10.1126/science.8036517
[research_wirth_et_al_2017]: https://jmlr.org/papers/v18/16-634.html
[research_wu_et_al_2021_uwac]: https://proceedings.mlr.press/v139/wu21i.html
[research_wu_sun_sen_zhu_zhang_2022]: https://doi.org/10.48550/arxiv.2202.06239
[research_wu_tucker_nachum_2019]: https://doi.org/10.48550/arxiv.1911.11361
[research_wu_wang_reed_lee_2023_edt]: https://proceedings.mlr.press/v202/wu23p.html
[research_xie_et_al_2021]: https://papers.nips.cc/paper_files/paper/2021/hash/34f98c7c5d7063181da890ea8d25265a-Abstract.html
[research_xie_ma_wang_2019_optimal]: https://papers.nips.cc/paper/2019/hash/4ffb0d2ba92f664c2281970110a2e071-Abstract.html
[research_xu_zhan_zhu_2022]: https://doi.org/10.48550/arxiv.2107.09003
[research_yang_et_al_2022_rorl]: https://papers.nips.cc/paper_files/paper/2022/hash/96bbdd0ed2a9e7cd2fb7caf2fae15f3d-Abstract-Conference.html
[research_yin_wang_2021]: https://proceedings.mlr.press/v139/yin21b.html
[research_yu_et_al_2020_mopo]: https://papers.nips.cc/paper/2020/hash/a322852ce0df73e204b7e67cbbef0d0a-Abstract.html
[research_yu_et_al_2021_combo]: https://papers.nips.cc/paper/2021/hash/f29a179746902e331572c483c45e5086-Abstract.html
[research_yu_et_al_2022_uds]: https://openreview.net/forum?id=5R6qHYqhHIS
[research_zhan_ren_yin_zhu_2022]: https://openreview.net/forum?id=Cw5uJx8XLU
[research_zhang_et_al_2023_policy_expansion]: https://doi.org/10.48550/arxiv.2302.00935
[research_zheng_et_al_2023_finetune]: https://scholar.google.com/scholar?q=Online+Finetune+Zheng+2023
[research_zheng_zhang_grover_2022_odt]: https://proceedings.mlr.press/v162/zheng22c.html
