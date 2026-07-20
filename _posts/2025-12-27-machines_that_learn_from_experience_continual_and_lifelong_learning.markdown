---
layout: post
mathjax: true
comments: true
title:  "Machines That Learn From Experience: Continual and Lifelong Learning"
date:   2025-12-27 00:00:00 +0000
categories: artificial-intelligence machine-learning neuroscience
series: machines_that_learn_from_experience
series_title: Machines That Learn From Experience
series_index: 10
---

<!-- A259 -->
<script>console.log("A259");</script>

Continual and lifelong learning treats the problem of acquiring knowledge from a non-stationary stream of tasks or experiences without forgetting previously-learned material and without requiring simultaneous access to all training data. The setting departs from the standard machine learning assumption of independent identically distributed samples and instead confronts the algorithm with a sequence of distributional shifts across an open-ended horizon. The central obstacle is catastrophic forgetting, in which learning a new task overwrites the parameters that supported earlier tasks and produces sudden performance collapse on those tasks. The literature has developed several families of algorithmic responses including regularization-based methods that penalize parameter changes in directions important for prior tasks, replay-based methods that interleave old and new experiences during training, architecture-based methods that dedicate distinct parameters to distinct tasks, meta-learning approaches that optimize for continual learning capacity itself, and neuroscience-inspired complementary learning systems that separate fast task-specific learning from slow consolidation. This article surveys the science and theory of continual and lifelong learning as they stand in the mid 2020s. Coverage includes the classical connectionist observations of catastrophic forgetting, the modern regularization and replay families, architecture-based parameter isolation and modular compositional methods, class-incremental learning as a distinct sub-field, continual representation learning and self-supervised streams, continual reinforcement learning, task-free and online continual learning, continual foundation models and language models, federated and distributed continual learning, multi-modal continual learning, theoretical frameworks including neural tangent kernel analyses and loss-landscape geometry, benchmark and evaluation methodology, and the neuroscience correspondence to hippocampal-neocortical consolidation. Article nine treated meta-learning across a fixed task distribution. The present article treats how a learner extends across an open-ended task sequence with retention of prior capability.

## The Continual Learning Problem

Continual learning is specified by a sequence of tasks or data distributions

$$\mathcal{T}_1, \mathcal{T}_2, \ldots, \mathcal{T}_k, \ldots$$

that arrive over time and produce a stream of training data

$$\mathcal{D}_1, \mathcal{D}_2, \ldots, \mathcal{D}_k, \ldots$$

The learner has access to only the current task's data at any given time and must update a shared model $f_\theta$ so that the resulting parameters $\theta_k$ perform well on all tasks $\mathcal{T}_1, \ldots, \mathcal{T}_k$ observed so far. The formal objective aggregates performance across the task sequence,

$$\theta^* = \arg\min_\theta \sum_{i=1}^{k} L_{\mathcal{T}_i}(\theta)$$

but the training procedure has access only to the current task's loss $L_{\mathcal{T}_k}(\theta)$ at time $k$, subject to bounded memory and compute.

Three canonical continual learning scenarios have emerged in the empirical literature following [van de Ven and Tolias 2019][research_van_de_ven_tolias_2019]. Task-incremental learning provides the task identity at both training and test time, permitting task-specific output heads and simplifying the retention problem. Domain-incremental learning changes the input distribution across tasks while retaining a fixed output structure, requiring adaptation without explicit task labels. Class-incremental learning progressively expands the output space and is generally regarded as the hardest scenario, since the model must simultaneously accommodate new classes and preserve old class representations without confusion.

The task-agnostic setting removes task boundaries entirely. The learner encounters a stream of samples drawn from a slowly-varying distribution and must adapt continuously without external cues about when the distribution has changed. This setting is closest to the biological setting and closest to many practical deployment scenarios. Its algorithmic requirements differ substantially from those of task-incremental learning.

Continual learning contrasts with several related but distinct paradigms. Multi-task learning assumes simultaneous access to all tasks and jointly optimizes across them. Transfer learning treats the sequential transfer of a source-task model to a single target task without concern for retention of source-task performance. Meta-learning as treated in article nine optimizes for fast adaptation to a task drawn from a fixed distribution rather than accumulation across an open-ended sequence. Continual learning shares elements of all three paradigms while making distinct algorithmic and evaluation demands.

The primary evaluation metrics include average accuracy across all seen tasks, backward transfer measuring the effect of learning task $\mathcal{T}_k$ on prior tasks $\mathcal{T}_{i < k}$, forward transfer measuring the effect of prior tasks on the learning of new tasks, and forgetting measured as the difference between peak and final accuracy on each task. Let $a_{k,i}$ denote the test accuracy on task $\mathcal{T}_i$ after the learner has been trained through task $\mathcal{T}_k$. The [Lopez-Paz and Ranzato 2017][research_lopez_paz_ranzato_2017_gem] formal definitions specify

$$\bar{A}_k = \frac{1}{k} \sum_{i=1}^{k} a_{k,i}$$

for average accuracy after task $k$,

$$\text{BWT}_k = \frac{1}{k-1} \sum_{i=1}^{k-1} (a_{k, i} - a_{i, i})$$

for backward transfer, and

$$\text{FWT}_k = \frac{1}{k-1} \sum_{i=2}^{k} (a_{i-1, i} - \tilde{a}_i)$$

for forward transfer where $\tilde{a}_i$ is the accuracy of an untrained reference model on task $\mathcal{T}_i$. The forgetting measure of [Chaudhry Dokania Ajanthan Torr 2018][research_chaudhry_et_al_2018_riemannian_walk] captures the peak-to-final drop,

$$F_k = \frac{1}{k-1} \sum_{i=1}^{k-1} \left(\max_{t \in \{i, \ldots, k-1\}} a_{t, i} - a_{k, i}\right)$$

with $F_k = 0$ corresponding to no forgetting on any prior task. The [Diaz-Rodriguez Lomonaco Filliat Maltoni 2018][research_diaz_rodriguez_et_al_2018] extensions cover model size and memory usage as evaluation criteria alongside accuracy.

## Historical Development

The catastrophic forgetting phenomenon was first documented systematically in the connectionist literature. [McCloskey and Cohen 1989][research_mccloskey_cohen_1989] and [Ratcliff 1990][research_ratcliff_1990] independently demonstrated that neural networks trained sequentially on two related tasks lose most of their performance on the first task after learning the second, in stark contrast to the graceful interference patterns observed in human learning. The observation launched the continual learning research program. The stability-plasticity dilemma of [Grossberg 1987][research_grossberg_1987] provided the earlier theoretical framing of the tension between preserving prior knowledge and acquiring new knowledge, motivating the subsequent adaptive resonance theory framework and its neurophysiologically-motivated stability mechanisms. The [Sharkey and Sharkey 1995][research_sharkey_sharkey_1995] survey of catastrophic forgetting consolidated the connectionist literature at the transition point between early and modern treatments.

Pseudo-rehearsal of [Robins 1995][research_robins_1995] provided the earliest algorithmic response by regenerating synthetic exemplars from the prior task's distribution during training on the new task, foreshadowing the modern generative replay methods. The [French 1999][research_french_1999] survey consolidated the early literature and identified the fundamental tension between plasticity and stability that continues to organize the field.

The modern deep learning era of continual learning began with the empirical investigations of [Goodfellow Mirza Xiao Courville Bengio 2013][research_goodfellow_et_al_2013] which documented that dropout provides substantial protection against catastrophic forgetting in deep networks, and with the systematic evaluations of [Kemker McClure Abitino Hayes Kanan 2018][research_kemker_et_al_2018] which established standard benchmarks and quantified the severity of forgetting in modern architectures.

The regularization-based family began with Elastic Weight Consolidation (EWC) of [Kirkpatrick Pascanu Rabinowitz Veness Desjardins Rusu Milan Quan Ramalho Grabska-Barwinska et al 2017][research_kirkpatrick_et_al_2017_ewc], which introduced Fisher-information-based penalties on parameter changes and provided the first widely-adopted continual learning method. Synaptic Intelligence (SI) of [Zenke Poole Ganguli 2017][research_zenke_poole_ganguli_2017_si] and Memory-Aware Synapses (MAS) of [Aljundi Babiloni Elhoseiny Rohrbach Tuytelaars 2018][research_aljundi_et_al_2018_mas] provided complementary online-computable importance measures.

The replay-based family developed in parallel through Gradient Episodic Memory (GEM) of [Lopez-Paz and Ranzato 2017][research_lopez_paz_ranzato_2017_gem], Averaged GEM (A-GEM) of [Chaudhry Ranzato Rohrbach Elhoseiny 2019][research_chaudhry_et_al_2019_agem], and Deep Generative Replay of [Shin Lee Kim Kim 2017][research_shin_et_al_2017_dgr]. iCaRL of [Rebuffi Kolesnikov Sperl Lampert 2017][research_rebuffi_et_al_2017_icarl] introduced class-incremental exemplar management combined with representation learning.

Architecture-based methods emerged through Progressive Networks of [Rusu Rabinowitz Desjardins Soyer Kirkpatrick Kavukcuoglu Pascanu Hadsell 2016][research_rusu_et_al_2016_progressive_cl] and subsequent methods including PackNet of [Mallya and Lazebnik 2018][research_mallya_lazebnik_2018_packnet], HAT of [Serra Suris Miron Karatzoglou 2018][research_serra_et_al_2018_hat], and PathNet of [Fernando Banarse Blundell Zwols Ha Rusu Pritzel Wierstra 2017][research_fernando_et_al_2017_pathnet]. Dynamically Expandable Networks (DEN) of [Yoon Yang Hwang Lee 2018][research_yoon_et_al_2018_den] extended the framework with data-driven capacity allocation.

Continual reinforcement learning developed as a distinct sub-field through CLEAR of [Rolnick Ahuja Schwarz Lillicrap Wayne 2019][research_rolnick_et_al_2019_clear] which established off-policy replay as the strongest continual reinforcement learning baseline, followed by the Continual World benchmark of [Wołczyk Zajac Pascanu Miłos 2021][research_wolczyk_et_al_2021_continual_world] and the [Khetarpal Riemer Rish Precup 2022][research_khetarpal_et_al_2022_survey] framework for continual reinforcement learning as a general problem class.

The mid 2020s produced substantial diversification including task-free continual learning approaches, continual foundation models, and neural tangent kernel analyses of the continual learning dynamics. The [De Lange Aljundi Masana Parisot Jia Leonardis Slabaugh Tuytelaars 2022][research_de_lange_et_al_2022_survey] comprehensive survey and the earlier [Parisi Kemker Part Kanan Wermter 2019][research_parisi_et_al_2019_survey] treatment consolidated the field.

## Catastrophic Forgetting

Catastrophic forgetting is the tendency of a neural network trained sequentially to lose performance on previously-learned tasks when trained on a new task. Formally, if $\theta_k$ minimizes $L_{\mathcal{T}_k}$ from initialization $\theta_{k-1}$ through gradient descent, then in the absence of countermeasures

$$L_{\mathcal{T}_i}(\theta_k) \gg L_{\mathcal{T}_i}(\theta_{i}) \quad \text{for } i < k$$

with the gap widening as $k$ increases and as the tasks become more distinct in their representational demands.

The phenomenon is mechanistic. Gradient descent on the new task's loss modifies parameters that were previously tuned to minimize prior tasks' losses, and since the losses generally have distinct minimizers in parameter space, the modifications degrade prior-task performance. The severity depends on the overlap between the loss landscapes of the tasks. Tasks with shared features and minimizers experience mild forgetting, while tasks with orthogonal feature requirements experience severe forgetting. The gradient-alignment measure

$$\rho_{i, k}(\theta) = \frac{\nabla_\theta L_{\mathcal{T}_i}(\theta) \cdot \nabla_\theta L_{\mathcal{T}_k}(\theta)}{\|\nabla_\theta L_{\mathcal{T}_i}(\theta)\| \, \|\nabla_\theta L_{\mathcal{T}_k}(\theta)\|}$$

provides a quantitative measure of interference at parameter setting $\theta$, with $\rho_{i, k} < 0$ indicating conflicting task demands and $\rho_{i, k} > 0$ indicating aligned task demands. Empirical measurements of $\rho$ across the training trajectory expose the specific pattern by which task interference produces forgetting.

The phenomenon exhibits several characteristic patterns. Forgetting is typically most severe on the earliest tasks in a sequence, with more recent tasks retained better even under uniform learning treatment. Forgetting affects deeper layers less than shallow layers when the sequence is composed of tasks that share low-level features. Forgetting varies substantially with task ordering, with certain orderings producing systematically better retention than others under the same algorithm.

The severity depends on the ratio of task-specific to task-shared parameters and on the redundancy of the parameter space. Overparameterized networks with substantially more parameters than needed to fit each task exhibit less forgetting than tightly-fit networks, providing one route to mitigation via architecture. The [Ramasesh Dyer Raghu 2021][research_ramasesh_dyer_raghu_2021] analysis of anatomy of catastrophic forgetting documented that deep networks under gradient descent exhibit a specific pattern of representational drift that provides mechanistic explanation for the observed phenomenology.

The related problem of loss of plasticity documented by [Dohare Sutton Mahmood 2021][research_dohare_sutton_mahmood_2021] establishes a complementary failure mode in which the network becomes increasingly resistant to learning new information as the sequence progresses, even without explicit forgetting mechanisms. Loss of plasticity affects the forward transfer term while catastrophic forgetting affects the backward transfer term, and modern continual learning must address both.

The trade-off between stability of prior knowledge and plasticity for new learning is the fundamental tension of continual learning. Extreme stability corresponds to freezing all parameters after the first task, producing no forgetting but no learning either. Extreme plasticity corresponds to unconstrained gradient descent, producing full learning of the current task and full forgetting of prior tasks. Practical algorithms occupy the intermediate regime through an objective of the form

$$L_{\text{CL}}(\theta) = L_{\text{plasticity}}(\theta) + \lambda \, R_{\text{stability}}(\theta, \theta_{1:k-1})$$

where the plasticity term encourages current-task performance and the stability term penalizes deviation from prior-task solutions, with $\lambda$ controlling the stability-plasticity balance. The choice of $R_{\text{stability}}$ specifies the algorithmic family.

## Regularization-Based Methods

Regularization-based methods add penalty terms to the training loss that discourage changes to parameters deemed important for prior tasks. The general form is

$$L_{\text{reg}}(\theta) = L_{\mathcal{T}_k}(\theta) + \sum_{i=1}^{k-1} \lambda_i \, R_i(\theta, \theta_i^*)$$

where $R_i$ measures the change of $\theta$ from the prior-task solution $\theta_i^*$ weighted by importance, and $\lambda_i$ controls the strength of the penalty.

Elastic Weight Consolidation of Kirkpatrick et al 2017 uses the Fisher information matrix diagonal as the parameter importance measure,

$$R_{\text{EWC}}(\theta, \theta_i^*) = \sum_j F_{i,j} (\theta_j - \theta_{i,j}^*)^2$$

where $F_{i,j}$ is the diagonal Fisher information for parameter $j$ evaluated at $\theta_i^*$,

$$F_{i,j} = \mathbb{E}_{(x, y) \sim \mathcal{D}_i}\!\left[\left(\frac{\partial \log p_\theta(y \mid x)}{\partial \theta_j}\right)^2\right]$$

The Fisher diagonal approximates the curvature of the log-likelihood at the prior task's optimum, providing a natural per-parameter importance signal. Parameters with high Fisher information are heavily penalized against change, while low-Fisher parameters are permitted to adapt freely.

Synaptic Intelligence of Zenke Poole Ganguli 2017 computes an online path-integral importance measure

$$\omega_{i,j} = \int_0^{T_i} g_{i,j}(t) \, \dot{\theta}_{j}(t) \, dt$$

where $g_{i,j}(t)$ is the gradient of the loss with respect to $\theta_j$ during task $i$ training and $\dot{\theta}_j$ is its update velocity. The mechanism attributes importance based on the total contribution of each parameter to loss reduction during training, and the online formulation avoids the need for separate importance-estimation passes.

Memory-Aware Synapses of Aljundi et al 2018 uses unsupervised importance estimation based on the gradient magnitude of the network output with respect to the parameters,

$$\Omega_{i,j} = \mathbb{E}_{x \sim \mathcal{D}_i}\!\left[\left|\frac{\partial \|f_\theta(x)\|^2}{\partial \theta_j}\right|\right]$$

providing a task-label-free importance measure applicable to unsupervised or self-supervised settings.

Learning without Forgetting (LwF) of [Li and Hoiem 2017][research_li_hoiem_2017_lwf] takes a distillation-based approach. Before training on task $\mathcal{T}_k$, the model computes predictions on the new task's data under the pre-update parameters, then trains the updated parameters to reproduce these predictions on the new task's inputs alongside the new task's labels,

$$L_{\text{LwF}}(\theta) = L_{\mathcal{T}_k}(\theta) + \lambda \, D_{\text{KL}}(f_{\theta_{k-1}}(x) \, \| \, f_\theta(x))$$

where the KL divergence is evaluated on inputs from $\mathcal{D}_k$. The mechanism preserves prior-task behavior indirectly through output-space regularization rather than parameter-space regularization.

Variational Continual Learning (VCL) of [Nguyen Li Bui Turner 2018][research_nguyen_et_al_2018_vcl] provides a Bayesian framework in which the prior for task $k$ is the posterior from task $k-1$,

$$p(\theta \mid \mathcal{D}_{1:k}) \propto p(\mathcal{D}_k \mid \theta) \, q_{k-1}(\theta)$$

with the posterior approximated by a variational distribution $q_k$. The framework provides a principled probabilistic account of continual learning and connects to Bayesian neural network posterior inference.

Online EWC of [Schwarz Czarnecki Luketina Grabska-Barwinska Teh Pascanu Hadsell 2018][research_schwarz_et_al_2018_online_ewc] combined the EWC framework with a running Fisher estimate that accumulates across tasks without maintaining per-task importance matrices, and their Progress and Compress framework separated fast task-specific learning from slow consolidation into a shared knowledge base. Online Structured Laplace Approximations of [Ritter Botev Barber 2018][research_ritter_botev_barber_2018] extended the Bayesian framework with a Kronecker-factored Laplace posterior that provides higher-quality curvature approximations than the diagonal Fisher of EWC, at manageable computational cost.

The recursion for Online EWC is

$$F_k^{\text{online}} = \gamma \, F_{k-1}^{\text{online}} + F_k$$

where $\gamma \in (0, 1]$ is a decay factor that emphasizes recent tasks, providing memory-efficient continual learning at long task sequences. The Riemannian Walk framework of [Chaudhry Dokania Ajanthan Torr 2018][research_chaudhry_et_al_2018_riemannian_walk] unified EWC with SI-style path integrals under a Riemannian-geometric account of parameter importance, defining the parameter importance through the path integral along the training trajectory,

$$\Omega_j^{\text{RW}} = \sum_i \int_{\theta_{i-1}}^{\theta_i^*} \frac{(\partial L / \partial \theta_j)^2}{2 (F_j + \epsilon)} \, d\theta_j$$

where $F_j$ is the Fisher information diagonal and $\epsilon$ is a small stabilizer.

Functional Regularization of Memorable Past of [Titsias Schwarz de G Matthews Pascanu Teh 2020][research_titsias_et_al_2020_frcl] extended the regularization framework to function space through inducing-point approximations, providing improved retention under Gaussian process priors and clarifying the specific connection between functional and parametric regularization. Uncertainty-based Continual Learning (UCL) of [Ahn Cha Lee Moon 2019][research_ahn_et_al_2019_ucl] introduced node-wise uncertainty estimates that provide a Bayesian alternative to the point-estimate Fisher approximations of EWC. Selfless Sequential Learning of [Aljundi Rohrbach Tuytelaars 2019][research_aljundi_rohrbach_tuytelaars_2019_ssl] introduced a sparsity-encouraging regularizer that reserves representational capacity for future tasks, addressing the loss-of-plasticity failure mode preemptively. Continual Learning with Adaptive Weights (CLAW) of [Adel Zhao Turner 2020][research_adel_zhao_turner_2020_claw] introduced per-parameter adaptation strength through Bayesian inference over the regularization strength itself.

The regularization family provides the conceptually simplest continual learning framework and produces reasonable performance on simple task sequences. Its principal limitation is that it does not address the plasticity side of the trade-off. Under long task sequences the accumulated regularization becomes so restrictive that new-task learning fails, producing a stability catastrophe rather than a forgetting catastrophe.

## Replay-Based Methods

Replay-based methods interleave samples from prior tasks with samples from the current task during training. The general framework maintains a memory buffer $\mathcal{M}$ of representative prior-task exemplars and trains on a mixture

$$L_{\text{replay}}(\theta) = L_{\mathcal{T}_k}(\theta) + \lambda \, L_{\mathcal{M}}(\theta)$$

where $L_{\mathcal{M}}$ is the loss on buffered exemplars from prior tasks.

Gradient Episodic Memory (GEM) of Lopez-Paz and Ranzato 2017 constrains the current-task gradient to not increase the loss on any prior task's memory,

$$g_k \cdot g_i \geq 0 \quad \text{for } i = 1, \ldots, k-1$$

where $g_i = \nabla_\theta L_{\mathcal{M}_i}(\theta)$ is the gradient on the memory for task $i$. When the constraint is violated, GEM projects the current-task gradient onto the constraint set through a quadratic program. The mechanism guarantees no forgetting on memory exemplars but at computational cost that scales with the number of prior tasks.

Averaged GEM (A-GEM) of Chaudhry et al 2019 approximates GEM by averaging over all prior-task memories rather than constraining each separately,

$$g \cdot \bar{g}_{\text{ref}} \geq 0, \quad \bar{g}_{\text{ref}} = \frac{1}{k-1} \sum_{i=1}^{k-1} g_i$$

providing substantial computational simplification at the cost of weaker retention guarantees. A-GEM has proved a strong baseline across benchmarks.

Deep Generative Replay of Shin et al 2017 uses a generative model trained on prior-task data to synthesize pseudo-exemplars for replay, avoiding the need to store real samples. The mechanism updates a coupled scholar network with generator plus classifier at each task, using the current scholar to generate replay samples for the next task's training. The framework is memory-efficient but requires the generative model to accurately capture the prior-task distributions. Brain-inspired replay of [van de Ven Siegelmann Tolias 2020][research_van_de_ven_siegelmann_tolias_2020_brain_inspired] extended the generative replay framework with internal-representation replay rather than pixel-space replay, providing substantially better retention on natural image benchmarks by aligning with the biological pattern of hippocampal-cortical replay. FearNet of [Kemker and Kanan 2018][research_kemker_kanan_2018_fearnet] applied a similar biologically-inspired dual-network architecture with fast learning of new experiences in one network and slow consolidation to a long-term network, providing an early modern instantiation of the complementary learning systems framework. Learning to Remember of [Ostapenko Puscas Klein Vincent Rodriguez Charlin Belilovsky 2019][research_ostapenko_et_al_2019] combined generative replay with dynamic capacity expansion, providing a hybrid framework that adapts capacity to task complexity.

Experience Replay for continual learning of [Chaudhry Rohrbach Elhoseiny Ajanthan Dokania Torr Ranzato 2019][research_chaudhry_et_al_2019_er] documented that even the simplest form of replay through random sampling from a fixed-size reservoir buffer often matches or exceeds the more sophisticated methods on standard benchmarks. The reservoir sampling procedure retains sample $i$ in a buffer of size $M$ with probability

$$p_i = \min\!\left(1, \frac{M}{i}\right)$$

producing an unbiased random sample from the observed stream at all times. The observation motivated the interest in reservoir-based approaches and challenged the conventional wisdom about the necessity of specialized continual learning machinery.

Dark Experience Replay (DER) of [Buzzega Boschini Porrello Abati Calderara 2020][research_buzzega_et_al_2020_der] combines experience replay with output-distillation, storing not only inputs and labels but also the pre-update network's logits $z$ and using them as soft targets during replay,

$$L_{\text{DER}}(\theta) = L_{\mathcal{T}_k}(\theta) + \alpha \, \mathbb{E}_{(x, z) \sim \mathcal{M}}\!\left[\|f_\theta(x) - z\|^2\right] + \beta \, \mathbb{E}_{(x, y) \sim \mathcal{M}}\!\left[L_{\text{CE}}(f_\theta(x), y)\right]$$

where $\mathcal{M}$ is the memory buffer, $L_{\text{CE}}$ is the cross-entropy loss, and $\alpha, \beta$ balance the distillation and hard-target terms. The mechanism combines the memory efficiency of small buffers with the retention benefits of distillation.

Meta Experience Replay (MER) of [Riemer Cases Ajemian Liu Rish Tu Tesauro 2019][research_riemer_et_al_2019_mer] applies meta-learning to the replay buffer sampling, using Reptile-style meta-gradients to optimize for gradient alignment between current-task and prior-task updates. The MER inner-outer optimization has the outer update

$$\theta \leftarrow \theta + \gamma \, (\text{SGD}_s(\theta) - \theta)$$

where $\text{SGD}_s$ denotes $s$ inner steps on a mixed batch of current-task and memory samples, meta-optimizing for prior-task gradient alignment.

iCaRL of Rebuffi et al 2017 combines exemplar replay with a nearest-mean-of-exemplars classifier and knowledge distillation, providing one of the strongest class-incremental learning methods. The mechanism selects representative exemplars via herding that greedily minimizes the distance between class prototype and buffered mean,

$$\mathcal{P}_c = \arg\min_{\{x_i\}_{i=1}^m} \left\|\mu_c - \frac{1}{m} \sum_{i=1}^{m} \varphi_\theta(x_i)\right\|$$

where $\mu_c = \mathbb{E}_{x \sim \mathcal{D}_c}[\varphi_\theta(x)]$ is the class-$c$ feature mean and $\varphi_\theta$ is the feature extractor. The classification decision for a query $x^*$ selects the class whose stored-exemplar mean is nearest in feature space.

GDumb of [Prabhu Torr Dokania 2020][research_prabhu_torr_dokania_2020_gdumb] provided a critical baseline that greedily fills a memory buffer with balanced class samples from the stream and trains from scratch on the buffer at test time. GDumb often matches or exceeds specialized continual learning methods on class-incremental benchmarks, exposing evaluation-protocol issues in the field and motivating stronger baseline comparisons.

CLEAR of Rolnick et al 2019 applied replay to continual reinforcement learning, combining behavior cloning on prior-task rollouts with V-trace off-policy correction to achieve substantially better retention than the model-free reinforcement learning baselines that lacked replay. The framework connected continual learning to the offline reinforcement learning methods of article eight.

Replay-based methods provide the strongest and most reliable continual learning across most benchmarks. Their principal cost is memory storage, which scales linearly with the number of tasks in the naive formulation and produces both privacy and scaling concerns in production settings.

## Architecture-Based Methods

Architecture-based methods allocate distinct parameters to distinct tasks, avoiding parameter interference by construction. The general framework partitions the parameter space or the computational graph so that different tasks operate on different subsets of parameters.

Progressive Networks of Rusu et al 2016 add a new column of parameters for each task while freezing prior columns. Task $k$'s output is computed by

$$h^{(k)}_l = \sigma\!\left(W^{(k)}_l h^{(k)}_{l-1} + \sum_{j<k} U^{(k, j)}_l h^{(j)}_{l-1}\right)$$

where $W^{(k)}_l$ are task-$k$ parameters at layer $l$ and $U^{(k, j)}_l$ are lateral connections from prior column $j$ to the current column. The frozen prior columns guarantee zero forgetting, and the lateral connections permit forward transfer from prior tasks. The parameter cost grows linearly with the number of tasks.

PackNet of Mallya and Lazebnik 2018 uses iterative pruning to identify a task-specific parameter subset within a fixed-capacity network. After training on task $k$, a subset of parameters is pruned and their masks are stored, freezing them for task $k$'s use, so that the effective task-$k$ parameters are

$$\theta^{(k)} = m^{(k)} \odot \theta$$

with $m^{(k)} \in \{0, 1\}^{|\theta|}$ the task-$k$ binary mask and $\odot$ the elementwise product. Subsequent tasks are trained on the remaining unmasked parameters. The mechanism supports many tasks within a single fixed-size network but requires careful mask management.

Hard Attention to the Task (HAT) of Serra et al 2018 uses learned per-task attention masks over the network activations, allowing each task to select the units it uses without directly modifying the shared parameters. The task-specific gates provide soft parameter isolation and are learned jointly with the standard task loss. The HAT layer computation applies a learned per-task soft mask

$$a_l^{(k)} = \sigma(s \cdot e_l^{(k)}), \quad h_l = a_l^{(k)} \odot \tilde{h}_l$$

where $e_l^{(k)}$ are task-specific gate embeddings at layer $l$, $s$ is an annealing temperature that pushes $a_l^{(k)}$ toward binary values over training, and $\tilde{h}_l$ is the pre-gated activation. The mask is used to bound parameter updates so that inputs previously important for prior tasks are preserved.

Piggyback of [Mallya Davis Lazebnik 2018][research_mallya_davis_lazebnik_2018_piggyback] and Supermasks in Superposition of [Wortsman Ramanujan Raghu Yamins Ilharco Ha Chen Cornebise Farhadi 2020][research_wortsman_et_al_2020_supsup] extended the mask-based framework with binary masks per task learned over a fixed random backbone, providing dramatic parameter efficiency for large task sequences. Superposition of Many Models into One of [Cheung Terekhov Chen Agrawal Olshausen 2019][research_cheung_et_al_2019_superposition] introduced a parameter-space rotation framework in which distinct task models are stored in superposition within a shared parameter block, retrieved through task-specific rotations. Continual Learning with Hypernetworks of [von Oswald Henning Sacramento Grewe 2020][research_von_oswald_et_al_2020_hnet] introduced task-conditional hypernetworks that generate task-specific network weights from a small task-embedding vector, providing an architecture-based framework with substantially lower memory overhead than progressive networks.

PathNet of Fernando et al 2017 uses evolutionary search over neural network pathways to identify task-specific sub-networks. The mechanism provides an architecture-search-based approach to continual learning that connects to neural architecture search. Expert Gate of [Aljundi Chakravarty Tuytelaars 2017][research_aljundi_chakravarty_tuytelaars_2017_expert_gate] introduced a gating architecture that routes each input to the appropriate task-specific expert through autoencoder-based task identification, enabling continual learning without shared parameter updates. Random Path Selection of [Rajasegaran Hayat Khan Khan Shao 2019][research_rajasegaran_et_al_2019_rps] combined path-based architecture selection with knowledge distillation, providing improved scalability over PathNet.

Dynamically Expandable Networks (DEN) of Yoon et al 2018 expand network capacity dynamically as new tasks arrive, adding neurons or layers when the current capacity is insufficient. The framework provides a data-driven trade-off between parameter efficiency and task-specific capacity.

Continual Learning with Neural Structural Rewiring (CN-DPM) of [Lee Ha Cha Song Kwon 2020][research_lee_et_al_2020_cndpm] introduced a Dirichlet-process mixture of experts that dynamically instantiates new experts as the input distribution shifts, providing a principled Bayesian nonparametric framework for architecture growth.

Architecture-based methods provide strong retention guarantees at the cost of parameter overhead. Their scalability to hundreds or thousands of tasks depends on the specific parameter-sharing structure. Mask-based methods scale better than column-addition methods for long sequences but require careful bookkeeping.

## Modular and Compositional Continual Learning

Modular continual learning approaches partition the network into functional units that can be selectively activated, combined, or added across the task sequence. The framework provides a middle ground between the parameter-isolation of architecture-based methods and the shared-parameter formulation of regularization and replay methods.

Modular Networks for Continual Learning of [Veniat Denoyer Ranzato 2021][research_veniat_denoyer_ranzato_2021_mntdp] introduced Modular Networks with Task Driven Prior (MNTDP), a framework in which each task assembles a sub-network from a shared library of modules. The mechanism supports positive transfer through shared modules and specialization through task-specific composition. The composition itself is learned per task, providing a principled framework for cross-task knowledge reuse.

Continual Compositional Task Learning of [Ostapenko Rodriguez Caccia Charlin 2021][research_ostapenko_et_al_2021_cctl] extended the modular framework with an explicit compositional generation of task-specific networks from a shared parameter pool, providing improved retention through structural reuse.

Mixture of Experts for Continual Learning has emerged as a distinct sub-field. The [Chen Lin Hong Cheng Wang Ma Xu Yin 2023][research_chen_et_al_2023_moe_cl] mixture-of-experts continual learning framework combined the compute-efficient scaling of MoE architectures with continual learning-specific expert allocation, providing an approach that scales substantially better than dense architectures at long task sequences. The [Fedus Zoph Shazeer 2022][research_fedus_zoph_shazeer_2022_switch] switch transformer framework provided the underlying compute-efficient MoE architecture that continual learning subsequently adapted.

Adapter-based continual learning uses parameter-efficient adapters as the modular unit. LoRA of [Hu Shen Wallis Allen-Zhu Li Wang Wang Chen 2022][research_hu_et_al_2022_lora] introduced low-rank adaptation as a general parameter-efficient fine-tuning framework, and continual learning implementations replace or add adapters per task rather than modifying the pretrained backbone. Continual Learning with Adapters of [Ermis Korman Sadin Berrada Zapella 2022][research_ermis_et_al_2022_adapters] provided the systematic treatment for transformer language models.

Compositional generalization studies of [Ostapenko et al 2021][research_ostapenko_et_al_2021_cg] provided evidence that continual learning success depends on the compositional structure of the learned representations. Systems that acquire compositional representations exhibit substantially better retention and forward transfer than systems whose representations are entangled.

Modular approaches provide a middle ground on the stability-plasticity trade-off. Task-specific modules provide isolation while shared modules and compositional structure provide forward transfer, and the framework scales naturally to open-ended task sequences through incremental module addition.

## Class-Incremental Learning

Class-incremental learning treats the specific setting in which the output space grows progressively across tasks and no task identity is provided at test time. The learner must accommodate new classes without confusing them with prior classes and without task-specific inference routing. The scenario is regarded as the hardest of the three canonical continual learning scenarios and admits a substantial dedicated literature.

The foundational modern method is iCaRL of Rebuffi et al 2017 treated in the replay section, which combines exemplar replay with nearest-mean-of-exemplars classification. Subsequent methods have addressed the specific pathologies of class-incremental learning including the recency bias of the softmax classifier and the feature-space drift across tasks.

End-to-End Incremental Learning (E2EIL) of [Castro Marín-Jiménez Guil Schmid Alahari 2018][research_castro_et_al_2018_e2eil] introduced end-to-end training with a balanced-fine-tuning stage that mitigates the class-imbalance bias caused by the small exemplar set. Learning without Memorizing (LwM) of [Dhar Singh Peng Wu Chellappa 2019][research_dhar_et_al_2019_lwm] extended the LwF framework with attention distillation, addressing the specific attention drift observed in class-incremental settings.

Bias Correction (BiC) of [Wu Chen Wang Ye Liu Guo Fu 2019][research_wu_et_al_2019_bic] identified the specific recency bias of the softmax over the enlarged class set and introduced a per-task calibration layer that removes the bias through a validation-set-based correction. Large-scale Incremental Learning (LUCIR) of [Hou Pan Loy Wang Lin 2019][research_hou_et_al_2019_lucir] introduced cosine normalization of the classifier and less-forget constraints, achieving strong performance on class-incremental ImageNet.

Pooled Outputs Distillation (PODNet) of [Douillard Cord Ollion Robert Valle 2020][research_douillard_et_al_2020_podnet] introduced spatial-plus-channel distillation over intermediate features, providing feature-space retention alongside output-space distillation. Der of [Yan Xie He 2021][research_yan_xie_he_2021_der] proposed dynamically-expanded feature representations that decouple the feature-space growth from the classifier growth.

The [Zhou et al 2023][research_zhou_et_al_2023_pycil] PyCIL benchmark library provides reference implementations of the major class-incremental methods with standardized hyperparameter configurations, and the associated [Masana et al 2023][research_masana_et_al_2023_cil_survey] class-incremental survey consolidated the empirical landscape.

The class-incremental setting has proved particularly challenging for regularization-based methods. Approaches that succeed on task-incremental benchmarks often fail dramatically in the class-incremental setting due to the absence of task-specific output heads. The dominant methods in the class-incremental setting are replay-based with substantial exemplar management, complemented by specialized calibration to address the recency bias.

Foundation-model-based class-incremental learning through DER of Yan Xie He 2021 and its extensions have substantially closed the gap between class-incremental performance and joint-training upper bounds when a strong pretrained backbone is available, motivating current research on class-incremental learning of large pretrained models.

## Continual Representation Learning and Self-Supervision

Continual representation learning treats the problem of learning transferable representations from a non-stationary data stream without task labels. The framework connects continual learning to self-supervised representation learning and to the broader unsupervised streaming literature.

Self-Supervised Continual Learning of [Fini Da Costa Alameda-Pineda Ricci Alahari Mairal 2022][research_fini_et_al_2022_sscl] extended contrastive learning frameworks including SimCLR and BYOL to the continual setting through a specific asymmetric momentum-encoder update that provides retention of prior representations. The framework documented that self-supervised losses exhibit substantially less catastrophic forgetting than supervised losses on the same task sequence.

Continual Barlow Twins of [Fini et al 2022][research_fini_et_al_2022_cbt] applied redundancy-reduction self-supervision to the continual setting, providing an alternative that avoids the negative-sample requirements of contrastive frameworks. Streaming Self-Training of [Purushwalkam Yan 2022][research_purushwalkam_yan_2022] introduced pseudo-labeling with slow-teacher targets for continual self-supervised learning on unlabeled video streams.

Representation Continuity of [Davari Asadi Mudur Aljundi Belilovsky 2022][research_davari_et_al_2022_rc] provided systematic empirical analysis of representation drift under continual learning, documenting that specific interventions preserve representational geometry substantially better than standard continual learning methods.

The [Purushwalkam Morgado Gupta 2022][research_purushwalkam_morgado_gupta_2022_ccl] Continual Contrastive Learning framework combined contrastive self-supervision with replay-based rehearsal, providing an approach that supports both label-agnostic representation learning and task-specific supervised heads. Time-Contrastive Learning of [Sermanet et al 2018][research_sermanet_et_al_2018_tcl] provided the earlier temporal-contrastive framework that continual learning subsequently adapted.

Continual representation learning exhibits several distinctive properties that differ from supervised continual learning. Self-supervised losses are typically substantially more forgiving than supervised losses on distributional shift, providing natural robustness. Representation drift can be monitored directly through feature-space metrics, providing internal diagnostics that supervised methods lack. The framework connects continual learning to the pretraining-and-adaptation paradigm of modern foundation models, and much recent work aims to unify continual representation learning with the fine-tuning of pretrained backbones.

## Federated and Distributed Continual Learning

Federated continual learning combines the challenges of continual learning with those of federated learning, in which multiple clients maintain local data and coordinate model updates without sharing raw data. The framework is essential for practical deployments where privacy and bandwidth constraints preclude the centralized data assumption of standard continual learning.

The FedWeIT framework of [Yoon Jeong Kim Nang Hwang 2021][research_yoon_et_al_2021_fedweit] introduced weighted inter-client transfer and continual learning under federated aggregation, providing a first systematic framework. Each client maintains a task-specific parameter set and a shared federated parameter set, with weighted transfer across clients that balances personalization with cross-client generalization.

GLFC of [Dong Wang Jiao Xu Deng Bai 2022][research_dong_et_al_2022_glfc] extended the framework to global-local federated class-incremental learning, addressing the specific challenges of class distribution shift across both clients and time. The framework introduces class-aware gradient compensation to handle the class-imbalance problem in federated class-incremental learning.

Continual Federated Learning under Concept Drift of [Casado Lema Traoré Nakayama Sanguineti Coquelin Cortes 2022][research_casado_et_al_2022] provided a systematic framework for federated continual learning under gradual distribution drift without discrete task boundaries, providing an important practical extension of the federated continual learning framework.

The federated continual learning setting exposes distinctive algorithmic considerations. Client heterogeneity means that different clients experience different distributional shifts, complicating the global aggregation. Communication constraints limit the frequency and volume of parameter exchange, restricting the algorithmic families available. Privacy constraints preclude the exemplar-sharing that dominates class-incremental learning, motivating generative-replay and regularization-based alternatives. Modern federated continual learning frameworks address each of these constraints through specialized algorithmic choices.

## Multi-Modal Continual Learning

Multi-modal continual learning extends the framework to learners that acquire capabilities across sequences that include multiple input or output modalities. The setting connects continual learning to the broader multi-modal learning literature and to the foundation model treatments of article eight.

Continual Learning of a Vision-Language Model of [Ding et al 2022][research_ding_et_al_2022_vlm_cl] documented the specific forgetting patterns that arise when a vision-language model is fine-tuned on a sequence of vision-language tasks, and proposed replay-based mitigation strategies that maintain the modality alignment.

Cross-Modal Continual Learning of [Yan Chen Ji Yin Chen 2022][research_yan_et_al_2022_cross_modal] introduced cross-modal alignment losses that preserve prior-modality behavior when learning new modalities. The framework connects continual learning to the modality-alignment literature that underlies modern multi-modal foundation models.

Continual Adaptation of Vision Transformers of [Ermis Korman Sadin Berrada Zapella 2022][research_ermis_et_al_2022_vit] documented specific interventions in the transformer architecture that enable continual adaptation without catastrophic forgetting of pretrained image classification capabilities.

The multi-modal continual learning setting inherits the algorithmic frameworks of the general continual learning literature but faces distinct challenges. Modality-specific forgetting can occur independently across modalities, complicating the retention analysis. Cross-modal transfer is often the primary benefit of the multi-modal setting, requiring algorithms that specifically preserve cross-modal alignment. The specific architectural choices of vision-language and audio-language models produce distinctive interference patterns that require modality-aware algorithmic responses.

## Meta-Learning and Continual Learning

Meta-learning approaches to continual learning optimize the learner itself for continual-learning capacity, rather than adopting a hand-designed continual-learning algorithm. The framework treats catastrophic forgetting as a phenomenon to be mitigated through better initialization, better representations, or better update rules acquired through meta-training on continual-learning tasks.

Online Aware Meta-Learning (OML) of [Javed and White 2019][research_javed_white_2019_oml] meta-learns a representation such that a linear classifier over the representation supports fast continual learning without catastrophic forgetting. The meta-training procedure alternates between the inner loop of sequential task training on the linear head and the outer loop of representation-parameter updates that account for the retention of prior-task performance. Formally, the OML meta-objective optimizes representation parameters $\phi$ so that

$$\phi^* = \arg\min_\phi \mathbb{E}_{\tau \sim p(\tau)}\!\left[\sum_{t=1}^{T} L\!\left(\text{SGD}_t\!\left(W_0; \varphi_\phi(\mathcal{D}_{\tau, 1:t})\right)\right)\right]$$

where $\text{SGD}_t$ denotes $t$ gradient steps on the sequence-so-far and $W_0$ is the linear-head initialization, forcing the representation to support catastrophic-forgetting-resistant sequential learning at the head.

A Neuromodulated Meta-Learning Algorithm (ANML) of [Beaulieu Frati Miconi Lehman Stanley Clune Cheney 2020][research_beaulieu_et_al_2020_anml] extended the framework with a neuromodulatory gating network that modulates plasticity per parameter based on the current task,

$$h_l = g_\phi(x) \odot f_\theta(x)$$

where $g_\phi$ is the neuromodulatory network that produces per-unit gates from the input $x$ and $f_\theta$ is the standard forward pass. The gating provides input-dependent plasticity control that meta-optimizes for continual retention. The framework achieved substantial improvements on long continual learning sequences.

MER of Riemer et al 2019 as noted in the replay section can be viewed as a meta-learning approach in which the meta-objective is retention on the current buffer distribution.

La-MAML of [Gupta Yadav Paull 2020][research_gupta_yadav_paull_2020_lamaml] applied MAML-style gradient-based meta-learning to per-parameter learning rates for continual learning, producing adaptive plasticity that responds to task-specific demands.

Meta-Learning Representations for Continual Learning of [Javed and White 2019][research_javed_white_2019_oml] and the [Caccia Rodriguez Ostapenko Normandin Lin et al 2020][research_caccia_et_al_2020_osaka] OSAKA benchmark treated in article nine provided systematic evaluation frameworks that reveal the specific trade-offs between meta-learning and standard continual learning methods.

The relationship between continual learning and meta-learning is bidirectional. Meta-learning provides a framework for optimizing continual learning algorithms, and continual learning provides a stress test for meta-learners that must operate across open-ended sequences rather than fixed task distributions.

## Continual Reinforcement Learning

Continual reinforcement learning treats the problem of a reinforcement learning agent that must learn from a sequence of tasks or environments without forgetting prior policy skills. The framework combines the challenges of continual learning with the additional complications of reinforcement learning including non-stationary state distributions and the exploration-exploitation trade-off.

CLEAR of Rolnick et al 2019 provided the foundational modern method. The framework uses off-policy actor-critic learning with a replay buffer that accumulates trajectories from all prior tasks. During training on task $k$, the agent samples a mixture of current-task and prior-task trajectories, applying behavior cloning to prior-task samples and full policy-gradient updates to current-task samples. V-trace off-policy corrections handle the distributional mismatch between the replayed trajectories and the current policy. The CLEAR objective is a weighted sum

$$L_{\text{CLEAR}}(\theta, \psi) = L_{\text{V-trace}}(\theta, \psi) + \lambda_{\text{BC}} \, \mathbb{E}_{\tau \sim \mathcal{M}}\!\left[\sum_t \|\pi_\theta(\cdot \mid s_t) - \mu(\cdot \mid s_t)\|^2\right] + \lambda_{\text{KL}} \, \mathbb{E}_{\tau \sim \mathcal{M}}\!\left[\sum_t D_{\text{KL}}(\pi_\theta \, \| \, \mu)\right]$$

where $\mu$ denotes the behavior policy of the buffered trajectory, $\mathcal{M}$ is the replay buffer accumulating across tasks, and $\lambda_{\text{BC}}$ and $\lambda_{\text{KL}}$ weight the behavior-cloning and KL terms respectively. The V-trace corrected value targets take the form

$$v_t = V(s_t) + \sum_{k=t}^{t+n-1} \gamma^{k-t} \prod_{j=t}^{k-1} c_j \, \delta_k V$$

with $c_j = \min(\bar{c}, \pi_\theta(a_j \mid s_j) / \mu(a_j \mid s_j))$ the truncated importance-sampling ratio and $\delta_k V = \rho_k (r_k + \gamma V(s_{k+1}) - V(s_k))$ the temporal-difference residual.

Continual Learning in Deep Reinforcement Learning of [Kirkpatrick et al 2017][research_kirkpatrick_et_al_2017_ewc] applied the EWC framework to Atari game sequences, providing early evidence that regularization-based methods transfer from supervised to reinforcement learning settings. However subsequent work by [Kaplanis Shanahan Clopath 2018][research_kaplanis_shanahan_clopath_2018] and by [Isele and Cosgun 2018][research_isele_cosgun_2018] documented that replay-based methods generally outperform regularization-based methods in the reinforcement learning setting, mirroring the observation in supervised continual learning.

Continual World of Wołczyk et al 2021 provides the standard benchmark for continual reinforcement learning through a sequence of 20 manipulation tasks in Meta-World. The benchmark supports systematic comparison across regularization-based, replay-based, and architecture-based methods, and the associated evaluation protocols have become the field standard.

Policy Consolidation of Kaplanis Shanahan Clopath 2018 combines EWC-style parameter regularization with a hierarchy of policy networks at different timescales, providing a biologically-motivated continual reinforcement learning architecture. The mechanism aligns with the complementary learning systems account of biological memory consolidation. Progress and Compress of [Schwarz Czarnecki Luketina Grabska-Barwinska Teh Pascanu Hadsell 2018][research_schwarz_et_al_2018_p_and_c] extended the framework with dedicated progress and knowledge-base networks that separate fast task-specific learning from slow consolidation, providing an early modern instantiation of the complementary learning systems architecture at reinforcement-learning scale. DisCoRL of [Traoré Caselles-Dupré Lesort Sun Cai Díaz-Rodríguez Filliat 2019][research_traore_et_al_2019_discorl] introduced continual learning of reinforcement learning policies through end-to-end policy distillation across a task sequence, avoiding the value-function machinery of CLEAR-style methods.

Same State Different Task of [Kessler Parker-Holder Ball Bhattacharjee Roberts 2022][research_kessler_et_al_2022_ssdt] documented that the continual reinforcement learning problem exhibits qualitatively different failure modes when task changes affect the reward function versus the transition dynamics, motivating task-type-specific algorithmic choices.

Fine-tuning of Reinforcement Learning Models of [Wołczyk Kurcyusz Zajac Bortkiewicz Pascanu Miłos 2022][research_wolczyk_et_al_2022_finetuning] documented that offline fine-tuning of pretrained reinforcement learning models exhibits catastrophic forgetting patterns similar to the supervised continual learning setting, unifying the offline and continual reinforcement learning frameworks.

The [Khetarpal Riemer Rish Precup 2022][research_khetarpal_et_al_2022_survey] survey provided a systematic taxonomy of continual reinforcement learning frameworks and identified the specific challenges that distinguish it from supervised continual learning, including the non-stationarity of state distributions, the credit-assignment complications under changing dynamics, and the interaction between exploration and forgetting.

Continual World Model learning of [Kessler Cobbe Fischer Riedmiller Vinyals 2023][research_kessler_et_al_2023_continual_world_models] combines the world-model framework of article seven with continual learning through selective replay of trajectories that produce novel dynamics predictions.

## Task-Free and Online Continual Learning

Task-free continual learning removes the assumption that task boundaries are known during training. The learner encounters a stream of samples from a slowly-shifting distribution and must accommodate the shift without explicit cues about when the distribution has changed.

The [Aljundi Kelchtermans Tuytelaars 2019][research_aljundi_et_al_2019_task_free] task-free continual learning framework introduced online loss surface plateau detection as a trigger for consolidation, providing the first systematic task-free framework. Continual Prototype Evolution of [De Lange and Tuytelaars 2021][research_de_lange_tuytelaars_2021_cope] extended the framework with prototype-based classification that supports smooth transitions across the input stream.

Online Continual Learning through [Aljundi Belilovsky Tuytelaars Charlin Caccia Lin Ranzato 2019][research_aljundi_et_al_2019_online_cl] provided the framework for single-pass learning from an unbounded data stream with strict memory and compute constraints. The setting is closest to many practical deployment scenarios and admits distinctive algorithmic considerations.

Maximally Interfered Retrieval of [Aljundi Caccia Belilovsky Caccia Lin Charlin Tuytelaars 2019][research_aljundi_et_al_2019_mir] introduced a memory-buffer sampling strategy that selects prior-task examples that are most affected by the current update. The MIR selection criterion chooses samples that maximize the anticipated loss increase under the current gradient step,

$$x^* = \arg\max_{x \in \mathcal{M}} \left[L(f_{\theta'}(x), y) - L(f_\theta(x), y)\right]$$

where $\theta' = \theta - \eta \nabla_\theta L(\theta; x_{\text{cur}}, y_{\text{cur}})$ is the anticipated post-update parameters after applying the current-task gradient. Retrieving and replaying the maximally-interfered samples provides efficient retention with modest memory usage.

Continual Learning under Domain Drift of [Doan Nguyen Pham Kanoulas Papapetrou 2023][research_doan_et_al_2023] provided a systematic framework for handling gradual distribution shift without discrete task boundaries. The framework combines online detection with adaptive consolidation.

Online Coreset Selection of [Yoon Madaan Yang Hwang 2022][research_yoon_et_al_2022_online_coreset] introduced principled data-selection methods for online continual learning that maintain a diverse and representative buffer under strict memory limits.

The [Mai Li Jeong Nguyen Chen Sanner 2022][research_mai_et_al_2022_online_survey] survey of online continual learning consolidated the practical algorithmic frameworks and identified the specific evaluation protocols that differ from the task-boundary-aware setting.

The task-agnostic setting has proved substantially more difficult than the task-aware setting on all standard benchmarks. The absence of task boundaries deprives methods of critical algorithmic hooks including per-task heads, per-task importance measures, and per-task consolidation triggers. Progress in the task-agnostic setting requires methods that are robust to gradual distribution shift and that discover task-like structure automatically.

## Continual Foundation Models and Language Models

Continual learning of foundation models presents distinctive challenges beyond those of task-specific continual learning. Foundation models have hundreds of millions to hundreds of billions of parameters, are pretrained on massive datasets, and are typically deployed with a mixture of prompted usage and fine-tuning across many downstream tasks. Retaining the broad pretrained capabilities while adapting to specific downstream tasks requires continual learning algorithms that scale to the foundation model regime.

Towards Continual Knowledge Learning of Language Models by [Jang Ye Yang Seonwoo Hwang Kim et al 2022][research_jang_et_al_2022_ckl] documented that continual pretraining of language models on updated corpora exhibits catastrophic forgetting of the original knowledge, and proposed regularization and replay strategies specific to the language model setting.

Continual Learning of a BERT Model of [Ke Liu Ma Wang 2021][research_ke_et_al_2021_bert_cl] provided one of the early treatments of continual fine-tuning for transformer language models, documenting the specific forgetting patterns and effective mitigation strategies.

Ostapenko Rodríguez Caccia Charlin Belilovsky 2022 [research_ostapenko_et_al_2022] applied continual pretraining to a language model corpus stream and documented that a specific pattern of learning-rate rewarming enables continual pretraining without catastrophic forgetting, providing evidence for the tractability of the task at scale.

Cossu Tuytelaars Carta Passaro Lomonaco Bacciu 2022 [research_cossu_et_al_2022] provided a systematic empirical study of continual pretraining strategies for language models across multiple corpora, identifying the trade-offs between rehearsal buffer size, learning rate schedule, and forgetting.

Simple and Scalable Strategies of [Ibrahim et al 2024][research_ibrahim_et_al_2024] documented that carefully-designed learning-rate schedules combined with modest replay buffers achieve strong continual pretraining performance at foundation model scale, providing a practical recipe for the deployment of continually-updated foundation models.

Parameter-Efficient Continual Learning through [Wang Wang Ebrahimi Sun Chen Ren Su Perot Dy Pfister 2022][research_wang_et_al_2022_dualprompt] DualPrompt combined the parameter-efficient LoRA-style adaptation with continual learning, providing a framework in which the pretrained foundation model backbone is frozen and only small task-specific adapters are trained continually. Formally, DualPrompt augments the frozen backbone $f_{\theta_0}$ with a general prompt $p_g$ that is shared across all tasks and a task-expert prompt $p_e^{(k)}$ per task,

$$\hat{y} = f_{\theta_0}\!\left([\, p_g \, ; \, p_e^{(k)} \, ; \, x \,]\right)$$

with only the prompts updated during continual learning. The general prompt captures task-shared structure while the expert prompts capture task-specific structure. Learning to Prompt (L2P) of [Wang Zhang Ebrahimi Sun Zhang Lee Ren Su Perot Dy Pfister 2022][research_wang_et_al_2022_l2p] provided the precursor prompt-pool framework in which relevant prompts are dynamically selected from a shared pool per input. CODA-Prompt of [Smith Karlinsky Chan Cascante-Bonilla Klinger 2023][research_smith_et_al_2023_coda] introduced decomposed attention-based prompt composition that provides continual composition of learned prompts without task boundaries. Lifelong Language Pretraining of [Chen Wang 2023][research_chen_wang_2023] documented systematic protocols for continual pretraining across domain-shift streams that avoid degradation of both pretrained and continually-learned capabilities.

Continual Instruction Tuning of large language models has emerged as an active area combining reinforcement learning from human feedback with continual updates as new task requirements or safety constraints are identified. The framework connects continual learning to the offline reinforcement learning treatments of article eight.

The continual foundation model setting inherits the algorithmic frameworks of the general continual learning literature but faces distinct scaling challenges. Full replay of pretraining data is often infeasible due to size, and full regularization on pretrained parameters is often too restrictive due to the specific structure of pretrained representations. Progress in this setting depends on developing algorithms adapted to the specific structure of foundation model pretraining and fine-tuning.

## Theoretical Frameworks

The theoretical understanding of continual learning has matured substantially in recent years. Several distinct frameworks provide complementary accounts of the phenomenology.

The neural tangent kernel (NTK) framework of [Bennani Doan Sugiyama 2020][research_bennani_doan_sugiyama_2020] and [Doan Bennani Mazoure Rabusseau Alquier 2021][research_doan_et_al_2021_ntk] analyzes continual learning in the infinite-width limit where the network's behavior is approximated by a fixed kernel

$$K(x, x') = \mathbb{E}_\theta\!\left[\nabla_\theta f_\theta(x)^\top \nabla_\theta f_\theta(x')\right]$$

The framework provides closed-form expressions for the forgetting rate under sequential training and identifies the dependence of forgetting on task similarity through the kernel Gram matrix. The task-similarity coefficient

$$\rho_{ij} = \frac{\text{Tr}(K_i^\top K_j)}{\|K_i\|_F \, \|K_j\|_F}$$

with $K_i$ the NTK block on task $i$ inputs predicts the mutual forgetting between tasks $i$ and $j$ under sequential training.

The task-similarity account of forgetting predicts that similar tasks produce more mutual interference than dissimilar tasks in a specific regime, and less interference in another regime, providing a testable prediction about the task-ordering effect. The empirical work of [Ramasesh Dyer Raghu 2021][research_ramasesh_dyer_raghu_2021] confirmed the non-monotonic dependence of forgetting on task similarity.

The loss-landscape geometry account of [Mirzadeh Farajtabar Pascanu Ghasemzadeh 2020][research_mirzadeh_et_al_2020] documented that continual learning is affected substantially by the specific curvature of the loss surface at the transition between tasks. The Hessian eigenvalue spectrum

$$\lambda_{\max}(H_i(\theta_i^*)) = \max_{\|v\| = 1} v^\top \nabla_\theta^2 L_{\mathcal{T}_i}(\theta_i^*) \, v$$

correlates with the observed forgetting when subsequently training on task $\mathcal{T}_{i+1}$. Flat minima with small $\lambda_{\max}$ produce less catastrophic forgetting than sharp minima with large $\lambda_{\max}$, motivating specific optimization strategies that seek flat regions.

Understanding the Role of Training Regimes in Continual Learning of [Mirzadeh Farajtabar Görür Pascanu Ghasemzadeh 2020][research_mirzadeh_et_al_2020_understanding] provided experimental evidence that training regimes affecting minimum flatness (learning rate, batch size, epoch count) affect continual learning performance in a specific and predictable pattern.

Compositional Generalization and Continual Learning of [Ostapenko Puscas Klein Vincent Rodriguez Charlin Belilovsky 2021][research_ostapenko_et_al_2021_cg] connected continual learning to the compositional generalization literature, arguing that appropriate compositional representations enable continual learning through structural reuse rather than through explicit retention mechanisms.

Sample complexity analyses of [Lin Lu Lu Wang 2023][research_lin_et_al_2023_theory] established formal bounds on the memory and compute requirements for continual learning under specified retention guarantees, providing the theoretical foundation for evaluating the fundamental trade-offs between memory, compute, and retention. The [Nguyen Achille Lam Busbridge Yin Kim Turner 2020][research_nguyen_et_al_2020_theory] theoretical account of continual learning provided sample complexity bounds through a Bayesian lens that connect continual learning to the broader online-learning literature. Cascade synaptic models of [Fusi Drew Abbott 2005][research_fusi_drew_abbott_2005] provided a foundational neuroscience-motivated theoretical framework in which synaptic states evolve through a cascade of transitions of varying stability, resolving the plasticity-stability dilemma at the single-synapse level and predicting power-law memory decay observed in behavioral data.

Continual Learning as a Sequential Function Approximation of [Farquhar and Gal 2018][research_farquhar_gal_2018] connected continual learning to the theoretical framework of streaming function approximation, providing a distinct theoretical basis that clarifies the specific limits of task-agnostic continual learning under the streaming assumption.

The relationship between continual learning and the broader theory of neural network optimization remains an active research area. The specific connection between the implicit regularization of gradient descent and the retention of prior tasks is not yet fully characterized.

## Empirical Landscape and Benchmarks

The continual learning empirical landscape has consolidated around several standard benchmarks. Split MNIST partitions the MNIST digits into a sequence of binary or five-way classification tasks. Permuted MNIST applies distinct pixel-permutations to MNIST inputs across tasks. Split CIFAR-10 and Split CIFAR-100 provide the natural extensions to more complex image classification. Split Tiny ImageNet extends to a larger label space.

CORe50 of [Lomonaco and Maltoni 2017][research_lomonaco_maltoni_2017_core50] provides a continuous object recognition benchmark with 50 objects presented under varying poses and backgrounds, offering a stream that is closer to natural visual experience than the disjoint task setups of the MNIST and CIFAR variants. Stream-51 of [Roady Hayes Vaidya Kanan 2020][research_roady_et_al_2020_stream51] extended the framework with an explicitly-streaming natural-image benchmark that removes the batched-task assumption of prior continual learning benchmarks. CLEAR benchmark of [Lin Xie Fu Liu 2021][research_lin_et_al_2021_clear_benchmark] provided a naturally-temporally-ordered visual classification benchmark drawn from photos with real-world time metadata, capturing genuinely gradual distribution shift.

Continual World of Wołczyk et al 2021 provides the standard reinforcement learning benchmark through 20 sequential Meta-World manipulation tasks. The benchmark supports evaluation of forward transfer, backward transfer, and average performance under fixed training-compute budgets.

CORA of [Powers Xing Kolve Mottaghi Gupta 2022][research_powers_et_al_2022_cora] provides a continual reinforcement learning benchmark specifically designed to evaluate embodied navigation tasks with realistic distribution shift.

Progressive Continual Learning of [Antoniou Storkey 2021][research_antoniou_storkey_2021] introduced few-shot continual learning benchmarks that combine the few-shot and continual settings, exposing methods that succeed at one to distinct challenges of the combined setting.

CLoM benchmarks for continual learning of language models have emerged including LAMOL of [Sun Ho Lee 2020][research_sun_ho_lee_2020_lamol] and subsequent extensions that provide task-sequential language modeling with retention evaluation.

The evaluation methodology for continual learning has itself been substantially refined. The [Farquhar and Gal 2018][research_farquhar_gal_2018_evaluation] critique of standard continual learning evaluation identified several confounds in the benchmark protocols and proposed more rigorous evaluation frameworks. Subsequent work has adopted variants including balanced-sampling from prior tasks, task-order randomization across seeds, and explicit reporting of computational budgets.

The GDumb baseline of Prabhu Torr Dokania 2020 exposed the sensitivity of continual learning conclusions to evaluation protocol choice. When evaluated with sufficient compute for training from scratch on the memory buffer, GDumb often matches or exceeds specialized continual learning methods on class-incremental benchmarks. The result motivated the field to adopt stronger baselines and to specify compute-normalized comparisons.

Empirical patterns across the benchmark landscape show several consistent findings. Replay-based methods provide the strongest and most reliable performance across most settings. Regularization-based methods perform reasonably on short task sequences but degrade on long sequences. Architecture-based methods provide strong retention at parameter cost. The task-agnostic setting produces substantially lower performance than the task-aware setting across all method families. Class-incremental learning remains the most challenging standard scenario with substantial performance gaps between the current best methods and full multi-task learning baselines.

## Evaluation Methodology and Reproducibility

The evaluation methodology of continual learning has received substantial attention as the field has matured. Standard evaluation involves a specific task sequence, memory budget, compute budget, and evaluation frequency, and the choice of each affects the resulting method rankings. The [Van de Ven and Tolias 2019][research_van_de_ven_tolias_2019] taxonomy of continual learning scenarios provided the foundational categorization of task-incremental, domain-incremental, and class-incremental settings that has become the field standard.

Compute-normalized evaluation is a specific concern raised by the GDumb baseline of Prabhu Torr Dokania 2020. Methods that appear to outperform simpler baselines at fixed compute budget often lose the advantage when the simpler baseline is given comparable compute. The [De Lange et al 2022][research_de_lange_et_al_2022_survey] survey documented systematic compute-normalized comparisons across the major method families.

The Avalanche framework of [Lomonaco Pellegrini Cossu Carta Graffieti Hayes De Lange Masana Pomponi et al 2021][research_lomonaco_et_al_2021_avalanche] provides an open-source continual learning library that consolidates the major benchmarks and reference implementations. The library has become the field standard for reproducible experimentation and has enabled systematic comparison across methods with consistent evaluation protocols.

Reproducibility of continual learning results has been a persistent challenge given the sensitivity of the field to task ordering, hyperparameter choice, and evaluation protocol. The [Delange et al 2021][research_delange_et_al_2021] reproducibility study documented substantial variation across independent implementations of standard methods and proposed reporting guidelines that have been increasingly adopted.

Metrics beyond accuracy are increasingly emphasized. Memory usage, compute usage, wall-clock training time, and privacy compliance are all critical for practical deployment and are reported inconsistently in the continual learning literature. The [Roady Hayes Vaidya Kanan 2020][research_roady_et_al_2020_stream51] streaming evaluation protocol emphasized the importance of realistic evaluation conditions that reflect actual deployment scenarios.

The stability-plasticity trade-off itself is not fully captured by any single metric. Methods that achieve strong average accuracy at the cost of low forward transfer or high memory usage may be inferior to alternative methods in practice. Multi-dimensional evaluation frameworks including radar plots and Pareto-frontier analysis have been proposed to communicate the trade-offs more completely.

The distinct evaluation demands of continual reinforcement learning have motivated specialized protocols. Continual World provides normalized-reward evaluation with fixed compute budgets, and the [Powers et al 2022][research_powers_et_al_2022_cora] CORA benchmark introduced explicit forward-transfer, backward-transfer, and stability metrics for continual reinforcement learning that mirror the supervised continual learning definitions.

## Applications

Personalized on-device learning represents one of the most-developed application areas of continual learning. Mobile phones, wearables, and edge devices maintain personalized models that adapt to individual users through continual learning on the device. The setting requires memory-efficient continual learning algorithms that operate under strict compute and battery constraints while preserving pretrained baseline capabilities.

Robotic skill acquisition uses continual learning to accumulate skills across a sequence of manipulation tasks without forgetting prior skills. The framework connects to the continual reinforcement learning treatments above and to the hierarchical reinforcement learning of article six. The [Lesort Lomonaco Stoian Maltoni Filliat Diaz-Rodriguez 2020][research_lesort_et_al_2020] continual learning for robotics survey consolidated the specific practical requirements of the robotic setting and identified the algorithmic gaps between benchmark performance and physical deployment.

Autonomous driving systems use continual learning to adapt to new road conditions, weather, and traffic patterns without forgetting the base driving policy. The setting is safety-critical and requires strong retention guarantees that current continual learning methods do not fully provide.

Recommender systems and content-ranking pipelines use continual learning to adapt to shifting user preferences and content distributions. The setting benefits from the large-scale replay-based methods that dominate modern practice.

Language model updating for evolving knowledge represents an emerging application. Foundation language models trained on a pretraining corpus become progressively outdated as world knowledge changes, and continual learning provides frameworks for incorporating updated information without retraining from scratch.

Medical diagnosis models updated on new patient data or new imaging protocols use continual learning to preserve prior clinical accuracy while incorporating new information. The setting is safety-critical and typically requires rigorous evaluation of both retention and adaptation.

Anomaly detection in industrial monitoring uses continual learning to adapt to shifting operating conditions while maintaining the ability to recognize prior anomaly patterns. The framework connects continual learning to the broader change-detection literature in signal processing.

## Neuroscience Connections

The Complementary Learning Systems (CLS) theory of [McClelland McNaughton O'Reilly 1995][research_mcclelland_mcnaughton_oreilly_1995] proposed that mammalian memory arises from the interaction of two distinct learning systems. The hippocampus provides fast episodic learning of individual experiences, while the neocortex provides slow gradual learning of the statistical regularities across experiences through hippocampal replay during rest and sleep. The two-system architecture resolves the stability-plasticity dilemma by dedicating distinct neural substrates to the two demands.

The framework provides the biological grounding for the replay-based continual learning methods of the machine learning literature. Hippocampal replay of prior-task experiences during rest and sleep provides the biological analogue of experience-buffer replay in continual learning algorithms, and the slow consolidation to cortex provides the biological analogue of the slow-parameter update mechanism used in many continual learning frameworks.

The revised CLS account of [Kumaran Hassabis McClelland 2016][research_kumaran_hassabis_mcclelland_2016] extended the framework with the observation that rapid learning of new information consistent with prior structure occurs directly in cortex, while radical departures from prior structure require the hippocampal system. The revision aligns closely with the observation in machine continual learning that within-distribution updates are less prone to forgetting than out-of-distribution updates.

Systems consolidation of memory as reviewed by [Frankland and Bontempi 2005][research_frankland_bontempi_2005] and by [Squire Genzel Wixted Morris 2015][research_squire_et_al_2015] documented the gradual transfer of memory from hippocampal to neocortical dependence over hours to years. The temporal profile of consolidation places specific constraints on the biological analogues of continual learning algorithms and provides testable predictions about the effect of interventions during specific consolidation windows.

Sleep-dependent memory consolidation of [Rasch and Born 2013][research_rasch_born_2013] and the specific role of NREM sleep in declarative memory consolidation of [Diekelmann Born 2010][research_diekelmann_born_2010] provided the mechanistic account of the offline consolidation phase. Sleep replay of prior experiences occurs preferentially during specific sleep stages, and behavioral evidence supports the causal role of these replays in retention.

Sleep-dependent motor learning of [Yang Pan Gan Ferretti Gan 2014][research_yang_et_al_2014] documented the specific role of REM sleep in motor skill retention and provided evidence for structural synaptic changes during sleep that support long-term retention. Branch-specific dendritic memory of [Cichon and Gan 2015][research_cichon_gan_2015] documented that motor learning selectively strengthens a subset of dendritic branches while sparing others, providing a specific biological mechanism for parameter-isolation continual learning that parallels the machine-learning architecture-based methods. The [Karlsson and Frank 2009][research_karlsson_frank_2009] documentation of awake replay in the hippocampus extended the replay account beyond sleep-based consolidation, showing that hippocampal replay during quiet wakefulness also supports memory-guided behavior.

The Poo et al 2016 [research_poo_et_al_2016] review of memory formation consolidated the cellular and systems-level mechanisms and identified the specific neuromodulatory signals that coordinate consolidation across the sleep-wake cycle.

The relationship between machine and biological continual learning is bidirectional. Biological mechanisms provide inspiration for algorithmic approaches, and machine learning methods provide computational tests of hypotheses about biological memory function. The [Hadsell Rao Rusu Pascanu 2020][research_hadsell_et_al_2020] review of embracing change provided a systematic account of the biological-machine correspondence in continual learning.

Article fourteen returns to the NeuroAI bridge and treats the continual learning correspondence in greater detail alongside the broader mapping between machine learning and neuroscience.

## Load-Bearing Open Questions

- What is the correct algorithmic framework for continual learning that scales to open-ended task sequences without accumulating memory or compute cost linearly with the sequence length?
- How can continual learning methods handle the plasticity side of the stability-plasticity trade-off? Current methods often address forgetting but produce loss of plasticity that limits new-task learning.
- What is the correct evaluation protocol for continual learning? Compute-normalized versus memory-normalized versus wall-clock evaluations produce substantially different method rankings.
- How should continual learning be integrated with foundation model pretraining and fine-tuning at scale?
- Can continual reinforcement learning methods be reliably scaled to long sequences of substantially-distinct tasks?
- What is the correct treatment of task-agnostic continual learning without external cues about distribution shift?
- How closely do the algorithmic continual learning methods correspond to the biological complementary learning systems architecture, and where do the correspondences fail?
- Can continual learning be combined with meta-learning to produce systems that improve their continual learning capacity over the task sequence itself?
- What is the correct theoretical framework for the stability-plasticity trade-off, and can it be characterized as a fundamental information-theoretic limit rather than as an algorithmic engineering challenge?

## References

### Books

- [Sutton and Barto 2018][book_sutton_barto_2018]

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

### Research

- [Adel Zhao Turner 2020 CLAW][research_adel_zhao_turner_2020_claw]
- [Ahn Cha Lee Moon 2019 UCL][research_ahn_et_al_2019_ucl]
- [Aljundi Babiloni Elhoseiny Rohrbach Tuytelaars 2018 MAS][research_aljundi_et_al_2018_mas]
- [Aljundi Belilovsky Tuytelaars Charlin Caccia Lin Ranzato 2019 Online CL][research_aljundi_et_al_2019_online_cl]
- [Aljundi Caccia Belilovsky Caccia Lin Charlin Tuytelaars 2019 MIR][research_aljundi_et_al_2019_mir]
- [Aljundi Chakravarty Tuytelaars 2017 Expert Gate][research_aljundi_chakravarty_tuytelaars_2017_expert_gate]
- [Aljundi Kelchtermans Tuytelaars 2019 Task Free][research_aljundi_et_al_2019_task_free]
- [Aljundi Rohrbach Tuytelaars 2019 Selfless][research_aljundi_rohrbach_tuytelaars_2019_ssl]
- [Antoniou Storkey 2021][research_antoniou_storkey_2021]
- [Beaulieu et al 2020 ANML][research_beaulieu_et_al_2020_anml]
- [Bennani Doan Sugiyama 2020][research_bennani_doan_sugiyama_2020]
- [Casado et al 2022 Concept Drift][research_casado_et_al_2022]
- [Castro Marín-Jiménez Guil Schmid Alahari 2018 E2EIL][research_castro_et_al_2018_e2eil]
- [Chen et al 2023 MoE CL][research_chen_et_al_2023_moe_cl]
- [Buzzega Boschini Porrello Abati Calderara 2020 DER][research_buzzega_et_al_2020_der]
- [Caccia et al 2020 OSAKA][research_caccia_et_al_2020_osaka]
- [Chaudhry Dokania Ajanthan Torr 2018 Riemannian Walk][research_chaudhry_et_al_2018_riemannian_walk]
- [Chaudhry Ranzato Rohrbach Elhoseiny 2019 A-GEM][research_chaudhry_et_al_2019_agem]
- [Chaudhry Rohrbach Elhoseiny Ajanthan Dokania Torr Ranzato 2019 ER][research_chaudhry_et_al_2019_er]
- [Chen Wang 2023 Lifelong Language Pretraining][research_chen_wang_2023]
- [Cheung Terekhov Chen Agrawal Olshausen 2019 Superposition][research_cheung_et_al_2019_superposition]
- [Cichon and Gan 2015 Dendritic Memory][research_cichon_gan_2015]
- [Cossu et al 2022 Continual Pretraining][research_cossu_et_al_2022]
- [Davari et al 2022 Representation Continuity][research_davari_et_al_2022_rc]
- [De Lange and Tuytelaars 2021 CoPE][research_de_lange_tuytelaars_2021_cope]
- [De Lange Aljundi Masana Parisot Jia Leonardis Slabaugh Tuytelaars 2022 Survey][research_de_lange_et_al_2022_survey]
- [Delange et al 2021 Reproducibility][research_delange_et_al_2021]
- [Dhar Singh Peng Wu Chellappa 2019 LwM][research_dhar_et_al_2019_lwm]
- [Diaz-Rodriguez Lomonaco Filliat Maltoni 2018][research_diaz_rodriguez_et_al_2018]
- [Ding et al 2022 VLM CL][research_ding_et_al_2022_vlm_cl]
- [Diekelmann and Born 2010][research_diekelmann_born_2010]
- [Doan Bennani Mazoure Rabusseau Alquier 2021 NTK][research_doan_et_al_2021_ntk]
- [Doan et al 2023 Domain Drift][research_doan_et_al_2023]
- [Dohare Sutton Mahmood 2021 Plasticity Loss][research_dohare_sutton_mahmood_2021]
- [Dong et al 2022 GLFC][research_dong_et_al_2022_glfc]
- [Douillard Cord Ollion Robert Valle 2020 PODNet][research_douillard_et_al_2020_podnet]
- [Ermis et al 2022 Adapters][research_ermis_et_al_2022_adapters]
- [Ermis et al 2022 ViT CL][research_ermis_et_al_2022_vit]
- [Farquhar and Gal 2018 Evaluation][research_farquhar_gal_2018_evaluation]
- [Farquhar and Gal 2018 Sequential][research_farquhar_gal_2018]
- [Fedus Zoph Shazeer 2022 Switch Transformer][research_fedus_zoph_shazeer_2022_switch]
- [Fernando et al 2017 PathNet][research_fernando_et_al_2017_pathnet]
- [Fini et al 2022 Continual Barlow Twins][research_fini_et_al_2022_cbt]
- [Fini et al 2022 SSCL][research_fini_et_al_2022_sscl]
- [Frankland and Bontempi 2005][research_frankland_bontempi_2005]
- [French 1999 Survey][research_french_1999]
- [Fusi Drew Abbott 2005 Cascade Synapses][research_fusi_drew_abbott_2005]
- [Goodfellow Mirza Xiao Courville Bengio 2013][research_goodfellow_et_al_2013]
- [Grossberg 1987 Stability-Plasticity][research_grossberg_1987]
- [Gupta Yadav Paull 2020 La-MAML][research_gupta_yadav_paull_2020_lamaml]
- [Hadsell Rao Rusu Pascanu 2020 Embracing Change][research_hadsell_et_al_2020]
- [Hou Pan Loy Wang Lin 2019 LUCIR][research_hou_et_al_2019_lucir]
- [Hu et al 2022 LoRA][research_hu_et_al_2022_lora]
- [Ibrahim et al 2024 Simple Scalable Strategies][research_ibrahim_et_al_2024]
- [Isele and Cosgun 2018 Selective Replay][research_isele_cosgun_2018]
- [Jang et al 2022 CKL][research_jang_et_al_2022_ckl]
- [Javed and White 2019 OML][research_javed_white_2019_oml]
- [Kaplanis Shanahan Clopath 2018 Policy Consolidation][research_kaplanis_shanahan_clopath_2018]
- [Karlsson and Frank 2009 Awake Replay][research_karlsson_frank_2009]
- [Ke Liu Ma Wang 2021 BERT CL][research_ke_et_al_2021_bert_cl]
- [Kemker and Kanan 2018 FearNet][research_kemker_kanan_2018_fearnet]
- [Kemker McClure Abitino Hayes Kanan 2018][research_kemker_et_al_2018]
- [Kessler et al 2022 Same State Different Task][research_kessler_et_al_2022_ssdt]
- [Kessler et al 2023 Continual World Models][research_kessler_et_al_2023_continual_world_models]
- [Khetarpal Riemer Rish Precup 2022 Survey][research_khetarpal_et_al_2022_survey]
- [Kirkpatrick et al 2017 EWC][research_kirkpatrick_et_al_2017_ewc]
- [Kumaran Hassabis McClelland 2016 CLS Revised][research_kumaran_hassabis_mcclelland_2016]
- [Lee et al 2020 CN-DPM][research_lee_et_al_2020_cndpm]
- [Lesort et al 2020 CL for Robotics][research_lesort_et_al_2020]
- [Li and Hoiem 2017 LwF][research_li_hoiem_2017_lwf]
- [Lin et al 2021 CLEAR Benchmark][research_lin_et_al_2021_clear_benchmark]
- [Lin et al 2023 Theory][research_lin_et_al_2023_theory]
- [Lomonaco and Maltoni 2017 CORe50][research_lomonaco_maltoni_2017_core50]
- [Lomonaco et al 2021 Avalanche][research_lomonaco_et_al_2021_avalanche]
- [Lopez-Paz and Ranzato 2017 GEM][research_lopez_paz_ranzato_2017_gem]
- [Mai Li Jeong Nguyen Chen Sanner 2022 Survey][research_mai_et_al_2022_online_survey]
- [Masana et al 2023 CIL Survey][research_masana_et_al_2023_cil_survey]
- [Mallya and Lazebnik 2018 PackNet][research_mallya_lazebnik_2018_packnet]
- [Mallya Davis Lazebnik 2018 Piggyback][research_mallya_davis_lazebnik_2018_piggyback]
- [McClelland McNaughton O'Reilly 1995 CLS][research_mcclelland_mcnaughton_oreilly_1995]
- [McCloskey and Cohen 1989][research_mccloskey_cohen_1989]
- [Mirzadeh Farajtabar Görür Pascanu Ghasemzadeh 2020 Understanding][research_mirzadeh_et_al_2020_understanding]
- [Mirzadeh Farajtabar Pascanu Ghasemzadeh 2020 Loss Landscape][research_mirzadeh_et_al_2020]
- [Nguyen Achille Lam Busbridge Yin Kim Turner 2020 Theory][research_nguyen_et_al_2020_theory]
- [Nguyen Li Bui Turner 2018 VCL][research_nguyen_et_al_2018_vcl]
- [Ostapenko et al 2019 Learning to Remember][research_ostapenko_et_al_2019]
- [Ostapenko et al 2021 CCTL][research_ostapenko_et_al_2021_cctl]
- [Ostapenko et al 2021 CG][research_ostapenko_et_al_2021_cg]
- [Ostapenko et al 2022 Continual Pretraining][research_ostapenko_et_al_2022]
- [Parisi Kemker Part Kanan Wermter 2019 Survey][research_parisi_et_al_2019_survey]
- [Poo et al 2016 Memory Formation][research_poo_et_al_2016]
- [Powers Xing Kolve Mottaghi Gupta 2022 CORA][research_powers_et_al_2022_cora]
- [Prabhu Torr Dokania 2020 GDumb][research_prabhu_torr_dokania_2020_gdumb]
- [Purushwalkam Morgado Gupta 2022 CCL][research_purushwalkam_morgado_gupta_2022_ccl]
- [Purushwalkam Yan 2022 Streaming Self-Training][research_purushwalkam_yan_2022]
- [Rajasegaran et al 2019 Random Path Selection][research_rajasegaran_et_al_2019_rps]
- [Ramasesh Dyer Raghu 2021 Anatomy][research_ramasesh_dyer_raghu_2021]
- [Rasch and Born 2013][research_rasch_born_2013]
- [Ratcliff 1990][research_ratcliff_1990]
- [Rebuffi Kolesnikov Sperl Lampert 2017 iCaRL][research_rebuffi_et_al_2017_icarl]
- [Riemer Cases Ajemian Liu Rish Tu Tesauro 2019 MER][research_riemer_et_al_2019_mer]
- [Ritter Botev Barber 2018 Online Laplace][research_ritter_botev_barber_2018]
- [Roady Hayes Vaidya Kanan 2020 Stream-51][research_roady_et_al_2020_stream51]
- [Robins 1995 Pseudo-Rehearsal][research_robins_1995]
- [Rolnick Ahuja Schwarz Lillicrap Wayne 2019 CLEAR][research_rolnick_et_al_2019_clear]
- [Rusu et al 2016 Progressive Networks][research_rusu_et_al_2016_progressive_cl]
- [Schwarz et al 2018 Online EWC][research_schwarz_et_al_2018_online_ewc]
- [Schwarz et al 2018 Progress and Compress][research_schwarz_et_al_2018_p_and_c]
- [Sermanet et al 2018 Time-Contrastive][research_sermanet_et_al_2018_tcl]
- [Serra Suris Miron Karatzoglou 2018 HAT][research_serra_et_al_2018_hat]
- [Sharkey and Sharkey 1995][research_sharkey_sharkey_1995]
- [Shin Lee Kim Kim 2017 DGR][research_shin_et_al_2017_dgr]
- [Smith Karlinsky Chan Cascante-Bonilla Klinger 2023 CODA-Prompt][research_smith_et_al_2023_coda]
- [Squire Genzel Wixted Morris 2015][research_squire_et_al_2015]
- [Sun Ho Lee 2020 LAMOL][research_sun_ho_lee_2020_lamol]
- [Titsias et al 2020 FRCL][research_titsias_et_al_2020_frcl]
- [Traoré et al 2019 DisCoRL][research_traore_et_al_2019_discorl]
- [van de Ven and Tolias 2019 Three Scenarios][research_van_de_ven_tolias_2019]
- [van de Ven Siegelmann Tolias 2020 Brain-Inspired Replay][research_van_de_ven_siegelmann_tolias_2020_brain_inspired]
- [Veniat Denoyer Ranzato 2021 MNTDP][research_veniat_denoyer_ranzato_2021_mntdp]
- [von Oswald et al 2020 Hypernetworks CL][research_von_oswald_et_al_2020_hnet]
- [Wang et al 2022 DualPrompt][research_wang_et_al_2022_dualprompt]
- [Wang et al 2022 L2P][research_wang_et_al_2022_l2p]
- [Wołczyk Kurcyusz Zajac Bortkiewicz Pascanu Miłos 2022 Finetuning][research_wolczyk_et_al_2022_finetuning]
- [Wołczyk Zajac Pascanu Miłos 2021 Continual World][research_wolczyk_et_al_2021_continual_world]
- [Wortsman et al 2020 Supermasks][research_wortsman_et_al_2020_supsup]
- [Wu Chen Wang Ye Liu Guo Fu 2019 BiC][research_wu_et_al_2019_bic]
- [Yan Chen Ji Yin Chen 2022 Cross-Modal][research_yan_et_al_2022_cross_modal]
- [Yan Xie He 2021 DER-CIL][research_yan_xie_he_2021_der]
- [Yang Pan Gan Ferretti Gan 2014 Sleep Motor Learning][research_yang_et_al_2014]
- [Yoon Madaan Yang Hwang 2022 Online Coreset][research_yoon_et_al_2022_online_coreset]
- [Yoon Yang Hwang Lee 2018 DEN][research_yoon_et_al_2018_den]
- [Yoon et al 2021 FedWeIT][research_yoon_et_al_2021_fedweit]
- [Zenke Poole Ganguli 2017 SI][research_zenke_poole_ganguli_2017_si]
- [Zhou et al 2023 PyCIL][research_zhou_et_al_2023_pycil]

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
[research_adel_zhao_turner_2020_claw]: https://openreview.net/forum?id=Hklso24Kwr
[research_ahn_et_al_2019_ucl]: https://papers.nips.cc/paper/2019/hash/2c3ddf4bf13852db711dd1901fb517fa-Abstract.html
[research_aljundi_chakravarty_tuytelaars_2017_expert_gate]: https://openaccess.thecvf.com/content_cvpr_2017/html/Aljundi_Expert_Gate_Lifelong_CVPR_2017_paper.html
[research_aljundi_et_al_2018_mas]: https://openaccess.thecvf.com/content_ECCV_2018/html/Rahaf_Aljundi_Memory_Aware_Synapses_ECCV_2018_paper.html
[research_aljundi_et_al_2019_mir]: https://papers.nips.cc/paper/2019/hash/15825aee15eb335cc13f9b559f166ee8-Abstract.html
[research_aljundi_et_al_2019_online_cl]: https://arxiv.org/abs/1902.10486
[research_aljundi_et_al_2019_task_free]: https://openaccess.thecvf.com/content_CVPR_2019/html/Aljundi_Task-Free_Continual_Learning_CVPR_2019_paper.html
[research_aljundi_rohrbach_tuytelaars_2019_ssl]: https://openreview.net/forum?id=Bkxbrn0cYX
[research_antoniou_storkey_2021]: https://arxiv.org/abs/2003.11498
[research_beaulieu_et_al_2020_anml]: https://arxiv.org/abs/2002.09571
[research_bennani_doan_sugiyama_2020]: https://arxiv.org/abs/2010.09543
[research_buzzega_et_al_2020_der]: https://papers.nips.cc/paper/2020/hash/b704ea2c39778f07c617f6b7ce480e9e-Abstract.html
[research_casado_et_al_2022]: https://arxiv.org/abs/2201.11976
[research_castro_et_al_2018_e2eil]: https://openaccess.thecvf.com/content_ECCV_2018/html/Francisco_M._Castro_End-to-End_Incremental_Learning_ECCV_2018_paper.html
[research_chen_et_al_2023_moe_cl]: https://arxiv.org/abs/2211.01452
[research_caccia_et_al_2020_osaka]: https://papers.nips.cc/paper/2020/hash/c0a271bc0ecb776a094786474322cb82-Abstract.html
[research_chaudhry_et_al_2018_riemannian_walk]: https://openaccess.thecvf.com/content_ECCV_2018/html/Arslan_Chaudhry__Riemannian_ECCV_2018_paper.html
[research_chaudhry_et_al_2019_agem]: https://openreview.net/forum?id=Hkf2_sC5FX
[research_chaudhry_et_al_2019_er]: https://arxiv.org/abs/1902.10486
[research_chen_wang_2023]: https://arxiv.org/abs/2205.12393
[research_cheung_et_al_2019_superposition]: https://papers.nips.cc/paper/2019/hash/4c7a167bb329bd92580a99ce422d6fa6-Abstract.html
[research_cichon_gan_2015]: https://www.nature.com/articles/nature14251
[research_cossu_et_al_2022]: https://arxiv.org/abs/2205.09357
[research_davari_et_al_2022_rc]: https://openaccess.thecvf.com/content/CVPR2022/html/Davari_Probing_Representation_Forgetting_in_Supervised_and_Unsupervised_Continual_Learning_CVPR_2022_paper.html
[research_de_lange_et_al_2022_survey]: https://ieeexplore.ieee.org/document/9349197
[research_de_lange_tuytelaars_2021_cope]: https://openaccess.thecvf.com/content/ICCV2021/html/De_Lange_Continual_Prototype_Evolution_Learning_Online_From_Non-Stationary_Data_Streams_ICCV_2021_paper.html
[research_delange_et_al_2021]: https://arxiv.org/abs/2101.10423
[research_dhar_et_al_2019_lwm]: https://openaccess.thecvf.com/content_CVPR_2019/html/Dhar_Learning_Without_Memorizing_CVPR_2019_paper.html
[research_diaz_rodriguez_et_al_2018]: https://www.sciencedirect.com/science/article/pii/S1566253518300538
[research_diekelmann_born_2010]: https://www.nature.com/articles/nrn2762
[research_ding_et_al_2022_vlm_cl]: https://arxiv.org/abs/2208.11267
[research_doan_et_al_2021_ntk]: https://proceedings.mlr.press/v130/doan21a.html
[research_doan_et_al_2023]: https://arxiv.org/abs/2306.13091
[research_dohare_sutton_mahmood_2021]: https://arxiv.org/abs/2108.06325
[research_dong_et_al_2022_glfc]: https://openaccess.thecvf.com/content/CVPR2022/html/Dong_Federated_Class-Incremental_Learning_CVPR_2022_paper.html
[research_douillard_et_al_2020_podnet]: https://openaccess.thecvf.com/content/ECCV2020/papers/Douillard_PODNet_Pooled_Outputs_Distillation_for_Small-Tasks_Incremental_Learning_ECCV_2020_paper.pdf
[research_ermis_et_al_2022_adapters]: https://arxiv.org/abs/2203.06667
[research_ermis_et_al_2022_vit]: https://arxiv.org/abs/2201.04924
[research_farquhar_gal_2018]: https://arxiv.org/abs/1805.09733
[research_farquhar_gal_2018_evaluation]: https://arxiv.org/abs/1805.09733
[research_fedus_zoph_shazeer_2022_switch]: https://jmlr.org/papers/v23/21-0998.html
[research_fernando_et_al_2017_pathnet]: https://arxiv.org/abs/1701.08734
[research_fini_et_al_2022_cbt]: https://arxiv.org/abs/2205.11319
[research_fini_et_al_2022_sscl]: https://openaccess.thecvf.com/content/CVPR2022/html/Fini_Self-Supervised_Models_Are_Continual_Learners_CVPR_2022_paper.html
[research_frankland_bontempi_2005]: https://www.nature.com/articles/nrn1607
[research_french_1999]: https://www.sciencedirect.com/science/article/abs/pii/S1364661399013418
[research_fusi_drew_abbott_2005]: https://www.cell.com/neuron/fulltext/S0896-6273(05)00062-6
[research_goodfellow_et_al_2013]: https://arxiv.org/abs/1312.6211
[research_grossberg_1987]: https://www.tandfonline.com/doi/abs/10.1207/s15516709cog1101_2
[research_gupta_yadav_paull_2020_lamaml]: https://papers.nips.cc/paper/2020/hash/85b9a5ac91cd629bd3afe396ec07270a-Abstract.html
[research_hadsell_et_al_2020]: https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(20)30219-9
[research_hou_et_al_2019_lucir]: https://openaccess.thecvf.com/content_CVPR_2019/html/Hou_Learning_a_Unified_Classifier_Incrementally_via_Rebalancing_CVPR_2019_paper.html
[research_hu_et_al_2022_lora]: https://openreview.net/forum?id=nZeVKeeFYf9
[research_ibrahim_et_al_2024]: https://arxiv.org/abs/2403.08763
[research_isele_cosgun_2018]: https://ojs.aaai.org/index.php/AAAI/article/view/11595
[research_jang_et_al_2022_ckl]: https://openreview.net/forum?id=vfsRB5MImo9
[research_javed_white_2019_oml]: https://papers.nips.cc/paper/2019/hash/f4dd765c12f2ef67f98f3558c282a9cd-Abstract.html
[research_kaplanis_shanahan_clopath_2018]: https://proceedings.mlr.press/v80/kaplanis18a.html
[research_karlsson_frank_2009]: https://www.nature.com/articles/nn.2344
[research_ke_et_al_2021_bert_cl]: https://papers.nips.cc/paper/2021/hash/bcd0049c35799cdf57d06eaf2eb3cff6-Abstract.html
[research_kemker_et_al_2018]: https://ojs.aaai.org/index.php/AAAI/article/view/11651
[research_kemker_kanan_2018_fearnet]: https://openreview.net/forum?id=SJ1Xmf-Rb
[research_kessler_et_al_2022_ssdt]: https://arxiv.org/abs/2106.02940
[research_kessler_et_al_2023_continual_world_models]: https://arxiv.org/abs/2303.06253
[research_khetarpal_et_al_2022_survey]: https://www.jair.org/index.php/jair/article/view/13673
[research_kirkpatrick_et_al_2017_ewc]: https://www.pnas.org/doi/10.1073/pnas.1611835114
[research_kumaran_hassabis_mcclelland_2016]: https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(16)30043-2
[research_lee_et_al_2020_cndpm]: https://openreview.net/forum?id=SJxSOJStPr
[research_lesort_et_al_2020]: https://www.sciencedirect.com/science/article/pii/S1566253519307377
[research_li_hoiem_2017_lwf]: https://ieeexplore.ieee.org/document/8107520
[research_lin_et_al_2021_clear_benchmark]: https://arxiv.org/abs/2201.06289
[research_lin_et_al_2023_theory]: https://arxiv.org/abs/2302.03970
[research_lomonaco_et_al_2021_avalanche]: https://openaccess.thecvf.com/content/CVPR2021W/CLVision/html/Lomonaco_Avalanche_An_End-to-End_Library_for_Continual_Learning_CVPRW_2021_paper.html
[research_lomonaco_maltoni_2017_core50]: https://proceedings.mlr.press/v78/lomonaco17a.html
[research_lopez_paz_ranzato_2017_gem]: https://papers.nips.cc/paper/2017/hash/f87522788a2be2d171666752f97ddebb-Abstract.html
[research_mai_et_al_2022_online_survey]: https://www.sciencedirect.com/science/article/pii/S0925231221014995
[research_masana_et_al_2023_cil_survey]: https://ieeexplore.ieee.org/document/9915459
[research_mallya_davis_lazebnik_2018_piggyback]: https://openaccess.thecvf.com/content_ECCV_2018/html/Arun_Mallya_Piggyback_Adapting_a_ECCV_2018_paper.html
[research_mallya_lazebnik_2018_packnet]: https://openaccess.thecvf.com/content_cvpr_2018/html/Mallya_PackNet_Adding_Multiple_CVPR_2018_paper.html
[research_mcclelland_mcnaughton_oreilly_1995]: https://psycnet.apa.org/doi/10.1037/0033-295X.102.3.419
[research_mccloskey_cohen_1989]: https://www.sciencedirect.com/science/article/pii/S0079742108605368
[research_mirzadeh_et_al_2020]: https://papers.nips.cc/paper/2020/hash/518a38cc9a0173d0b2dc088166981cf8-Abstract.html
[research_mirzadeh_et_al_2020_understanding]: https://papers.nips.cc/paper/2020/hash/518a38cc9a0173d0b2dc088166981cf8-Abstract.html
[research_nguyen_et_al_2018_vcl]: https://openreview.net/forum?id=BkQqq0gRb
[research_nguyen_et_al_2020_theory]: https://arxiv.org/abs/1908.01091
[research_ostapenko_et_al_2019]: https://openaccess.thecvf.com/content_CVPR_2019/html/Ostapenko_Learning_to_Remember_A_Synaptic_Plasticity_Driven_Framework_for_Continual_CVPR_2019_paper.html
[research_ostapenko_et_al_2021_cctl]: https://openreview.net/forum?id=RxDdvSfM8yD
[research_ostapenko_et_al_2021_cg]: https://openreview.net/forum?id=RxDdvSfM8yD
[research_ostapenko_et_al_2022]: https://arxiv.org/abs/2205.12393
[research_parisi_et_al_2019_survey]: https://www.sciencedirect.com/science/article/pii/S0893608019300231
[research_poo_et_al_2016]: https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-016-0261-6
[research_powers_et_al_2022_cora]: https://arxiv.org/abs/2110.10067
[research_prabhu_torr_dokania_2020_gdumb]: https://openaccess.thecvf.com/content/ECCV2020/papers/Prabhu_GDumb_A_Simple_Approach_that_Questions_Our_Progress_in_Continual_ECCV_2020_paper.pdf
[research_purushwalkam_morgado_gupta_2022_ccl]: https://openaccess.thecvf.com/content/CVPR2022/html/Purushwalkam_The_Challenges_of_Continuous_Self-Supervised_Learning_CVPR_2022_paper.html
[research_purushwalkam_yan_2022]: https://arxiv.org/abs/2203.12710
[research_rajasegaran_et_al_2019_rps]: https://papers.nips.cc/paper/2019/hash/83da7c539e1ab4e759623c38d8737e9e-Abstract.html
[research_ramasesh_dyer_raghu_2021]: https://openreview.net/forum?id=LhY8QdUGSuw
[research_rasch_born_2013]: https://journals.physiology.org/doi/full/10.1152/physrev.00032.2012
[research_ratcliff_1990]: https://psycnet.apa.org/doi/10.1037/0033-295X.97.2.285
[research_rebuffi_et_al_2017_icarl]: https://openaccess.thecvf.com/content_cvpr_2017/html/Rebuffi_iCaRL_Incremental_Classifier_CVPR_2017_paper.html
[research_riemer_et_al_2019_mer]: https://openreview.net/forum?id=B1gTShAct7
[research_ritter_botev_barber_2018]: https://papers.nips.cc/paper/2018/hash/f31b20466ae89669f9741e047487eb37-Abstract.html
[research_roady_et_al_2020_stream51]: https://openaccess.thecvf.com/content_CVPRW_2020/html/w15/Roady_Stream-51_Streaming_Classification_and_Novelty_Detection_From_Videos_CVPRW_2020_paper.html
[research_robins_1995]: https://www.tandfonline.com/doi/abs/10.1080/09540099550039318
[research_rolnick_et_al_2019_clear]: https://papers.nips.cc/paper/2019/hash/fa7cdfad1a5aaf8370ebeda47a1ff1c3-Abstract.html
[research_rusu_et_al_2016_progressive_cl]: https://arxiv.org/abs/1606.04671
[research_schwarz_et_al_2018_online_ewc]: https://proceedings.mlr.press/v80/schwarz18a.html
[research_schwarz_et_al_2018_p_and_c]: https://proceedings.mlr.press/v80/schwarz18a.html
[research_sermanet_et_al_2018_tcl]: https://arxiv.org/abs/1704.06888
[research_serra_et_al_2018_hat]: https://proceedings.mlr.press/v80/serra18a.html
[research_sharkey_sharkey_1995]: https://link.springer.com/article/10.1007/BF00120687
[research_shin_et_al_2017_dgr]: https://papers.nips.cc/paper/2017/hash/0efbe98067c6c73dba1250d2beaa81f9-Abstract.html
[research_smith_et_al_2023_coda]: https://openaccess.thecvf.com/content/CVPR2023/html/Smith_CODA-Prompt_COntinual_Decomposed_Attention-Based_Prompting_for_Rehearsal-Free_Continual_Learning_CVPR_2023_paper.html
[research_squire_et_al_2015]: https://cshperspectives.cshlp.org/content/7/8/a021766.long
[research_sun_ho_lee_2020_lamol]: https://openreview.net/forum?id=Skgxcn4YDS
[research_titsias_et_al_2020_frcl]: https://openreview.net/forum?id=SkxCzeHFDB
[research_traore_et_al_2019_discorl]: https://arxiv.org/abs/1907.05855
[research_van_de_ven_siegelmann_tolias_2020_brain_inspired]: https://www.nature.com/articles/s41467-020-17866-2
[research_van_de_ven_tolias_2019]: https://arxiv.org/abs/1904.07734
[research_veniat_denoyer_ranzato_2021_mntdp]: https://openreview.net/forum?id=EKV158tSfwv
[research_von_oswald_et_al_2020_hnet]: https://openreview.net/forum?id=SJgwNerKvB
[research_wang_et_al_2022_dualprompt]: https://arxiv.org/abs/2204.04799
[research_wang_et_al_2022_l2p]: https://openaccess.thecvf.com/content/CVPR2022/html/Wang_Learning_To_Prompt_for_Continual_Learning_CVPR_2022_paper.html
[research_wolczyk_et_al_2021_continual_world]: https://papers.nips.cc/paper/2021/hash/e6c58bcdca67f0d0f00a2c1f8b21e34c-Abstract.html
[research_wolczyk_et_al_2022_finetuning]: https://arxiv.org/abs/2210.10469
[research_wortsman_et_al_2020_supsup]: https://papers.nips.cc/paper/2020/hash/ad1f8bb9b51f023cdc80cf94bb615aa9-Abstract.html
[research_wu_et_al_2019_bic]: https://openaccess.thecvf.com/content_CVPR_2019/html/Wu_Large_Scale_Incremental_Learning_CVPR_2019_paper.html
[research_yan_et_al_2022_cross_modal]: https://arxiv.org/abs/2208.11267
[research_yan_xie_he_2021_der]: https://openaccess.thecvf.com/content/CVPR2021/html/Yan_DER_Dynamically_Expandable_Representation_for_Class_Incremental_Learning_CVPR_2021_paper.html
[research_yang_et_al_2014]: https://www.science.org/doi/10.1126/science.1249098
[research_yoon_et_al_2018_den]: https://openreview.net/forum?id=Sk7KsfW0-
[research_yoon_et_al_2021_fedweit]: https://proceedings.mlr.press/v139/yoon21b.html
[research_yoon_et_al_2022_online_coreset]: https://openreview.net/forum?id=f9D-5WNG4Nv
[research_zenke_poole_ganguli_2017_si]: https://proceedings.mlr.press/v70/zenke17a.html
[research_zhou_et_al_2023_pycil]: https://arxiv.org/abs/2112.12533
