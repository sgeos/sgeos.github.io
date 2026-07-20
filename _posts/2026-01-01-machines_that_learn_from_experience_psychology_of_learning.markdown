---
layout: post
mathjax: true
comments: true
title:  "Machines That Learn From Experience: From Conditioning to Computation, the Psychology of Learning"
date:   2026-01-01 00:00:00 +0000
categories: artificial-intelligence machine-learning neuroscience
series: machines_that_learn_from_experience
series_title: Machines That Learn From Experience
series_index: 15
---

<!-- A264 -->
<script>console.log("A264");</script>

The psychology of learning treats the specific empirical and theoretical framework through which learning has been studied as a psychological phenomenon in its own right. The framework provides the specific bridge from the classical behaviorist tradition through the cognitive revolution to modern computational cognitive science, and provides the specific empirical constraints against which computational accounts of learning must be evaluated. Modern computational learning theory has been substantially shaped by the specific empirical findings of the psychology of learning literature, and modern psychology of learning has been substantially reshaped by the specific computational vocabulary that reinforcement learning, Bayesian cognitive science, and predictive processing provide. This article surveys the science and theory of the psychology of learning as it stands in the mid 2020s. Coverage includes the classical Pavlovian and instrumental conditioning traditions, the Rescorla-Wagner model as the specific formal foundation of predictive learning, behaviorism and its specific limits, the cognitive revolution and Tolman's cognitive maps, attention-based associative learning through Pearce-Hall and Mackintosh models, reinforcement learning as formalized psychology, motivation drives and reward systems, categorization and concept learning, analogical reasoning insight and problem solving, social learning and observational acquisition, skill acquisition and expertise, metacognition and learning-to-learn, individual differences in learning, memory systems from Atkinson-Shiffrin through the modern multi-system view, learning across the lifespan, Bayesian models of cognition, prospect theory and heuristics-and-biases, language acquisition as learning, predictive processing and free energy as psychological theory, the specific neuroscience correspondence, empirical benchmarks, reproducibility and methodological reform, and the specific applications to education, behavior therapy, and behavioral economics. Article fourteen treated the specific bidirectional exchange between neuroscience and machine learning. The present article treats the parallel exchange between the psychology of learning and modern computational learning theory.

## The Psychology of Learning Problem

The psychology of learning treats the specific question of how experience produces enduring changes in behavior, cognition, and neural representation. The framework provides the empirical foundation for both classical behaviorism and modern computational cognitive science, and identifies the specific empirical phenomena that any adequate theory of learning must reproduce.

The framework admits several distinct formalizations depending on the specific tradition and level of analysis. Behaviorist formalizations treat learning as the specific change in observable stimulus-response relationships. Cognitive formalizations treat learning as the specific change in internal mental representations. Neural formalizations treat learning as the specific change in synaptic weights and neural circuit properties. Computational formalizations treat learning as the specific update of algorithmic parameters through the specific interaction with the environment. The most general formal characterization treats learning as the systematic update of an internal state $\theta_t$ based on the interaction history,

$$\theta_{t+1} = \theta_t + \eta \, \Delta(\theta_t, o_t, a_t, r_t)$$

with $\eta$ a learning rate and $\Delta$ an update function that depends on the specific formalization adopted.

The specific empirical phenomena that any adequate theory of learning must reproduce include Pavlovian conditioning, instrumental conditioning, extinction, blocking, overshadowing, latent learning, categorization, skill acquisition, memory consolidation, language acquisition, and the specific developmental trajectories of learning across the lifespan. Modern computational theories of learning are systematically evaluated against these empirical phenomena, and the specific correspondences and failures organize substantial modern research.

The framework contrasts with several assumptions that organize modern machine learning. The independent-identically-distributed sampling assumption is often violated in the specific patterns of natural learning experience. The reward specification assumption of standard reinforcement learning is often difficult to reconcile with the specific patterns of biological reward learning. The specific supervised-learning framework requires labeled data that biological learners often do not have direct access to. The specific correspondence between computational learning frameworks and biological learning phenomena continues to organize substantial research.

The framework also raises specific methodological questions distinct from either pure psychology or pure computational learning. What is the specific level of description at which computational and psychological theories should be compared? What is the specific role of individual differences in psychological learning phenomena that computational theories must accommodate? What are the specific empirical benchmarks against which computational cognitive theories should be evaluated? These questions organize substantial modern computational cognitive science and continue to shape the specific bidirectional exchange between psychology and machine learning.

## Historical Development

The psychology of learning as a distinct research discipline emerged in the late nineteenth century through the specific combination of experimental physiology, comparative psychology, and philosophical reflection on the nature of mind. The [Ebbinghaus 1885][book_ebbinghaus_1885] Memory experiments introduced the specific quantitative approach to the study of learning through the systematic study of nonsense-syllable acquisition and forgetting. The framework provided the specific empirical foundation for the systematic study of memory and continues to shape modern memory research through the specific forgetting-curve and spacing-effect findings.

Classical conditioning of [Pavlov 1927][book_pavlov_1927] Conditioned Reflexes provided the systematic empirical framework for the specific study of associative learning through the systematic manipulation of stimulus contingencies. The framework identified the specific patterns of acquisition, extinction, and generalization that continue to organize the associative learning literature.

The Law of Effect of [Thorndike 1911][book_thorndike_1911] Animal Intelligence introduced the specific proposal that behaviors followed by satisfying consequences become more likely, providing the foundational modern statement of instrumental conditioning. The framework has been substantially refined through subsequent work but continues to provide the specific empirical foundation for the instrumental learning tradition.

Behaviorism as a distinct research program was systematically launched by the [Watson 1913][research_watson_1913] Psychology as the Behaviorist Views It manifesto, which argued that psychology should restrict itself to the specific study of observable behavior rather than the introspective study of consciousness. The framework substantially shaped subsequent American psychology through the specific commitment to behavioral measurement.

The [Skinner 1938][book_skinner_1938] Behavior of Organisms extended the behaviorist framework through the systematic study of operant conditioning and identified the specific reinforcement schedules that produce distinctive patterns of behavioral acquisition and maintenance. The framework has substantially shaped subsequent behavior analysis and continues to organize substantial applied psychology research. Purposive Behavior in Animals and Men of [Tolman 1932][book_tolman_1932] provided the systematic early alternative to strict behaviorism through the specific proposal that animal behavior is oriented toward specific goals and mediated by cognitive representations. Principles of Behavior of [Hull 1943][book_hull_1943] provided the alternative systematic neo-behaviorist framework through the specific hypothetico-deductive formulation of learning as a function of habit strength and drive. Stochastic Models for Learning of [Bush and Mosteller 1955][book_bush_mosteller_1955] introduced the specific formal probabilistic framework for learning that provided the systematic mathematical foundation for the subsequent computational learning theories, and Skinner's [Verbal Behavior 1957][book_skinner_1957] extended the operant framework to language behavior in the specific treatment that Chomsky subsequently critiqued.

Stimulus sampling theory of [Estes 1950][research_estes_1950] provided the specific formal alternative in which learning is characterized as the systematic sampling of stimulus elements associated with responses. The framework provided one of the earliest systematic mathematical treatments of learning and continues to shape the modern probabilistic treatment through the specific quantitative predictions it produces.

The cognitive revolution emerged in the 1950s through the specific combination of information-theoretic frameworks, empirical challenges to strict behaviorism, and the emergence of computer science as a source of specific computational vocabulary for mental processes. The [Miller 1956][research_miller_1956] Magical Number Seven paper introduced the specific information-processing framework for the study of short-term memory. The [Chomsky 1959][research_chomsky_1959] Review of Verbal Behavior provided the systematic linguistic critique of the specific behaviorist account of language acquisition. The [Bruner Goodnow Austin 1956][book_bruner_goodnow_austin_1956] Study of Thinking provided the specific cognitive-psychological alternative to behaviorism through the study of concept attainment.

The Rescorla-Wagner model of [Rescorla and Wagner 1972][research_rescorla_wagner_1972] introduced the specific formal model of classical conditioning that provided the modern quantitative framework for the study of associative learning. The framework has been substantially extended and refined through subsequent work but continues to provide the specific quantitative foundation for the field.

Modern computational cognitive science emerged in the 1980s and 1990s through the specific combination of connectionist modeling, Bayesian frameworks, and the increasing empirical grounding of computational theories. The [Anderson 1990][book_anderson_1990] Adaptive Character of Thought framework and the substantial subsequent work has substantially reshaped modern psychology through the specific commitment to computational-cognitive-model-fitting to empirical data.

The 2000s and 2010s produced the specific integration of reinforcement learning frameworks with the psychology of learning through the specific work of [Daw Niv Dayan 2005][research_daw_niv_dayan_2005] and the substantial subsequent literature. The framework provides the specific bridge between modern machine learning and the classical psychology of learning literature. The modern Bayesian cognitive science framework of [Tenenbaum Kemp Griffiths Goodman 2011][research_tenenbaum_et_al_2011] provided the complementary probabilistic framework that continues to organize substantial modern computational cognitive science.

## Classical Pavlovian Conditioning

Classical conditioning is the specific learning phenomenon in which an initially-neutral stimulus (the conditioned stimulus, CS) becomes associated with a stimulus that reliably elicits a response (the unconditioned stimulus, US), producing a conditioned response (CR) to the CS. The framework provides the foundational empirical paradigm for the study of associative learning.

The Pavlov 1927 systematic experimental framework identified the specific patterns of classical conditioning including acquisition, extinction, spontaneous recovery, generalization, and discrimination. Acquisition refers to the specific increase in the CR strength across CS-US pairings and is quantitatively described by the specific exponential-approach curve

$$V(n) = V_\infty (1 - e^{-\alpha n})$$

with $V(n)$ the associative strength after $n$ trials and $V_\infty$ the asymptotic strength. Extinction refers to the specific decrease in CR strength across CS-alone presentations and is often quantitatively described by the specific decay function $V(n) = V_0 \, e^{-\beta n}$. Spontaneous recovery refers to the specific partial return of the CR after a rest period following extinction. Generalization follows a specific similarity-based gradient

$$V(x) = V_{\text{CS}} \, s(x, x_{\text{CS}})$$

with $s$ a stimulus-similarity function. Discrimination refers to the specific differential responding to CS versus similar-but-distinct stimuli.

Blocking was systematically demonstrated by [Kamin 1968][research_kamin_1968] through the specific experimental paradigm in which prior conditioning to a CS blocks subsequent conditioning to a compound CS-plus-novel-cue stimulus. The framework provided the specific empirical demonstration that classical conditioning depends on the informativeness of the CS rather than on mere CS-US contiguity. The framework substantially motivated the subsequent development of the Rescorla-Wagner formal model.

Overshadowing is the specific phenomenon in which a more salient element of a compound CS acquires greater CR strength than a less salient element after equal CS-US pairings. The framework provides evidence for the specific competition among elements of a compound CS for associative strength during conditioning.

Contingency versus contiguity was systematically studied by [Rescorla 1968][research_rescorla_1968] through the specific truly-random-control experiments that demonstrated that CS-US pairings produce conditioning only when the CS provides information about the US, not merely when the CS and US co-occur. The contingency measure

$$\Delta P = P(\text{US} \mid \text{CS}) - P(\text{US} \mid \neg \text{CS})$$

quantifies the specific predictive relationship between the CS and the US, with $\Delta P > 0$ producing excitatory conditioning and $\Delta P < 0$ producing inhibitory conditioning. The framework has substantially shaped the modern understanding of associative learning as a form of predictive computation.

Second-order conditioning is the specific phenomenon in which a stimulus that has been established as a CS can serve as a US for conditioning of a second-order CS. The framework provides the specific mechanism through which classical conditioning can produce chains of associations that extend beyond the direct CS-US relationship, connecting classical conditioning to the specific higher-order cognitive phenomena.

Modern classical conditioning research increasingly treats the paradigm as a specific experimental system for studying general principles of predictive learning that apply across many species and many behavioral domains. The framework connects Pavlovian conditioning to modern reinforcement learning through the shared computational vocabulary of predictive-error learning. The [Wagner 1981][research_wagner_1981_sop] Sometimes Opponent Process (SOP) theory extended the Rescorla-Wagner framework with a specific opponent-process account of the temporal dynamics of associative learning, providing systematic quantitative predictions for many phenomena that pure Rescorla-Wagner cannot accommodate.

Context and ambiguity in extinction of [Bouton 1993][research_bouton_1993] provided the systematic modern treatment of the specific patterns of renewal, reinstatement, and spontaneous recovery observed after extinction. The framework identifies the specific role of context in the retrieval of extinguished versus original memories and continues to organize modern extinction research with substantial implications for behavior therapy. The [Gallistel and Gibbon 2000][research_gallistel_gibbon_2000] Time Rate and Conditioning framework provided the specific temporal-scaling alternative in which classical conditioning is governed by the temporal ratios between the CS and US rather than by the specific contiguity or contingency relationships that traditional theories emphasize.

## The Rescorla-Wagner Model and Predictive Learning

The Rescorla-Wagner model of Rescorla and Wagner 1972 provided the specific formal framework that quantitatively accounts for the specific empirical phenomena of classical conditioning. The framework has become the standard modern quantitative model of associative learning and continues to organize substantial contemporary research.

The Rescorla-Wagner update rule specifies the change in associative strength for each CS after a trial as

$$\Delta V_{\text{CS}} = \alpha_{\text{CS}} \, \beta_{\text{US}} \, (\lambda - \Sigma V)$$

with $V_{\text{CS}}$ the current associative strength of the specific CS, $\alpha_{\text{CS}}$ a CS-specific learning-rate parameter, $\beta_{\text{US}}$ a US-specific learning-rate parameter, $\lambda$ the maximum associative strength supported by the specific US, and $\Sigma V$ the sum of associative strengths of all CSs present on the trial. The specific error signal $(\lambda - \Sigma V)$ provides the driving force for learning and produces the specific patterns of blocking and other conditioning phenomena that pre-Rescorla-Wagner models could not accommodate.

Blocking follows directly from the Rescorla-Wagner update. If prior conditioning has established $V_A = \lambda$ for CS A, then adding a novel CS B during subsequent A+B trials produces $\Sigma V = V_A + V_B \approx \lambda$, yielding $(\lambda - \Sigma V) \approx 0$ and therefore no learning for CS B. The framework provides the specific quantitative account of the empirical blocking phenomenon that Kamin 1968 had documented.

The specific correspondence between the Rescorla-Wagner update and the temporal-difference learning rule of modern reinforcement learning is substantial. Both frameworks compute updates based on prediction errors that reflect the difference between actual and expected outcomes. The specific correspondence is captured by the observation that the Rescorla-Wagner rule is equivalent to trial-level temporal-difference learning with $\gamma = 0$,

$$V(s) \leftarrow V(s) + \alpha \, (r - V(s))$$

The specific correspondence has been extensively developed through subsequent work and provides the specific bridge between classical psychological learning theory and modern computational reinforcement learning.

Limitations of the Rescorla-Wagner framework include the specific failure to accommodate several empirical phenomena including latent inhibition, sensory preconditioning, and the specific effects of attention on associative learning. Subsequent models including the Pearce-Hall attention-based framework and the Mackintosh attention-based framework have been developed to address these specific limitations.

The specific bidirectional exchange in classical conditioning has been substantial. Psychology provides the specific empirical constraints that formal models must satisfy, and formal models provide the specific quantitative vocabulary through which psychological phenomena can be systematically characterized. The specific correspondence continues to organize substantial modern research on associative learning across species and behavioral domains.

## Instrumental Conditioning and the Law of Effect

Instrumental (or operant) conditioning is the specific learning phenomenon in which the future probability of a behavior depends on the consequences that follow the behavior. The framework provides the empirical paradigm for the specific study of learning driven by reward and punishment.

The Thorndike 1911 Law of Effect provided the specific foundational statement: behaviors followed by satisfying consequences become more likely to recur in similar circumstances, while behaviors followed by unsatisfying consequences become less likely to recur. The framework has been substantially refined through subsequent work but continues to provide the specific empirical foundation for the operant tradition.

The Skinner 1938 systematic experimental framework identified the specific reinforcement schedules and their distinctive effects on behavior. Continuous reinforcement produces rapid acquisition but rapid extinction. Fixed-ratio schedules produce high response rates with post-reinforcement pauses. Variable-ratio schedules produce high steady response rates that are particularly resistant to extinction. Fixed-interval schedules produce scallop-shaped response patterns. Variable-interval schedules produce steady moderate response rates. The specific patterns provide the systematic empirical foundation for the modern understanding of reinforcement effects on behavior.

Herrnstein's matching law of [Herrnstein 1961][research_herrnstein_1961] provided the systematic quantitative characterization of choice behavior under concurrent variable-interval schedules. The framework predicts that the proportion of responses on each of two alternatives matches the proportion of reinforcement obtained,

$$\frac{B_1}{B_1 + B_2} = \frac{R_1}{R_1 + R_2}$$

with $B_i$ the response rate and $R_i$ the reinforcement rate on alternative $i$. The framework has substantial empirical support across many species and has been substantially influential in behavioral economics.

Shaping is the specific technique through which complex behaviors are established through the successive reinforcement of progressively closer approximations to the target behavior. The framework provides the specific mechanism through which behaviors that would not occur spontaneously can be established through the systematic reinforcement of intermediate steps. The framework has substantial practical importance for animal training, applied behavior analysis, and instructional design.

Behavior chains are the specific patterns in which sequences of behaviors become linked through the establishment of specific stimuli as conditioned reinforcers for prior behaviors and as discriminative stimuli for subsequent behaviors. The framework provides the specific mechanism through which complex behavioral sequences can be established and maintained.

The specific distinction between operant and Pavlovian conditioning has been substantially blurred in modern accounts. Modern computational treatments including the specific reinforcement learning framework treat both as instances of general prediction-error-based learning, with the specific differences arising from the specific behavioral and computational demands rather than from fundamentally distinct mechanisms.

The specific distinction between actions and habits was systematically developed by [Dickinson 1985][research_dickinson_1985] through the specific empirical framework in which the sensitivity of behavior to outcome devaluation distinguishes goal-directed action from habitual response. The framework has substantial empirical support from operant learning studies and continues to organize modern research on the specific mechanisms underlying behavioral control. Goal-directed instrumental action of [Balleine and Dickinson 1998][research_balleine_dickinson_1998] extended the framework with the specific neuroanatomical account of the distinct neural substrates supporting goal-directed and habitual behavior.

Modern operant conditioning research increasingly connects to reinforcement learning through the shared computational vocabulary. The specific correspondence between the actor-critic architecture and the operant conditioning paradigm has been extensively developed and provides the modern computational instantiation of the classical operant framework.

## Motivation, Drives, and Reward Systems

Motivation provides the specific psychological framework through which the driving forces of behavior are systematically studied. The framework connects the specific psychology of reward and punishment to the modern reinforcement learning framework and to the specific affective neuroscience of the reward system.

Hull's drive-reduction theory of [Hull 1943][book_hull_1943] provided the specific foundational modern account in which behavior is driven by the reduction of physiological drives including hunger, thirst, and sexual arousal. The framework identifies the specific quantitative relationship

$$\text{response strength} = \text{habit strength} \times \text{drive} \times \text{incentive}$$

that combines learning history with current motivational state. The framework has been substantially refined but continues to provide the specific quantitative bridge between the psychology of motivation and modern reinforcement learning.

Intrinsic versus extrinsic motivation was systematically studied through the [Deci 1971][research_deci_1971] framework which documented that specific extrinsic rewards can undermine intrinsic motivation for tasks that are inherently interesting. The framework has substantial empirical support and provides the specific empirical grounding for the modern developmental-robotics treatments of intrinsic motivation covered in article thirteen.

Self-determination theory of [Ryan and Deci 2000][research_ryan_deci_2000_a264] provided the systematic modern framework for intrinsic motivation through the specific identification of autonomy, competence, and relatedness as the fundamental psychological needs that support intrinsically-motivated behavior. The framework has substantial empirical support across many domains including education, healthcare, and workplace psychology, and provides the specific bridge between the psychology of motivation and the modern intrinsic-motivation frameworks in computational learning.

The specific neuropsychology of reward has been extensively developed through the [Berridge and Robinson 1998][research_berridge_robinson_1998] Wanting versus Liking framework that distinguishes the specific neural systems supporting reward-related motivation (wanting, mediated by dopamine) from those supporting reward-related pleasure (liking, mediated by opioid and cannabinoid systems). The framework provides the specific empirical grounding for the observation that reward-prediction-error signals track wanting rather than liking, connecting modern computational reinforcement learning to the specific neuropsychology of hedonics.

The [Higgins 1997][research_higgins_1997] regulatory focus theory framework introduced the specific systematic distinction between promotion and prevention regulatory foci, providing the specific empirical framework for the study of motivational orientation effects on learning and behavior. The framework has substantial empirical support and continues to shape modern research on the specific role of motivational states in cognitive processing.

Modern computational treatments of motivation include the specific frameworks of intrinsic motivation in reinforcement learning treated in articles five and thirteen, the specific reward-learning treatments in articles two through four, and the specific dual-system frameworks treated earlier in this article. The framework provides the specific bridge between the classical psychology of motivation and modern computational learning theory.

## Behaviorism and Its Limits

Behaviorism as a research program dominated American psychology from the 1910s through the 1950s. The framework provided the specific methodological commitment to observable-behavior measurement that produced substantial empirical progress on learning and behavior, but also produced the specific theoretical constraints that motivated the subsequent cognitive revolution.

Watson 1913 launched behaviorism as an explicit research program through the specific argument that psychology should restrict itself to observable behavior rather than the introspective study of mental states. The framework substantially shaped subsequent American psychology through the specific commitment to behavioral measurement, systematic experimental control, and the rejection of unobservable mental constructs.

Radical behaviorism of Skinner extended the framework to include the specific position that even mental terminology should be reinterpreted as reference to observable behavior or dispositions to behavior. The framework produced substantial empirical progress on operant conditioning while raising specific theoretical concerns about the adequacy of purely-behavioral accounts of complex cognitive phenomena.

The specific limits of behaviorism became increasingly apparent through the 1950s. Latent learning experiments including [Tolman and Honzik 1930][research_tolman_honzik_1930] demonstrated that learning can occur without observable performance changes, undermining the specific behaviorist commitment to identifying learning with behavior change. Insight learning experiments of [Köhler 1925][book_kohler_1925] demonstrated that chimpanzees can solve novel problems through the specific reorganization of perceptual information rather than through gradual trial-and-error learning.

The Chomsky 1959 review of Skinner's Verbal Behavior provided the specific systematic critique of the behaviorist account of language acquisition. The framework argued that the specific structural properties of language could not be accommodated by behaviorist accounts of learning and required the specific postulation of innate linguistic structures. The review substantially shaped subsequent linguistics and cognitive science through the specific argument for nativist accounts of language.

Modern accounts of behaviorism recognize both its substantial empirical contributions and its specific theoretical limitations. The specific empirical findings on operant and classical conditioning continue to organize modern learning research. The specific theoretical limitations motivate the modern cognitive-computational alternative that combines the empirical rigor of behaviorism with the specific commitment to unobservable computational and representational constructs.

## The Cognitive Revolution and Tolman's Cognitive Maps

The cognitive revolution of the 1950s and 1960s introduced the specific commitment to unobservable mental representations and computational processes as legitimate objects of psychological study. The framework substantially reshaped psychology and provided the specific empirical and theoretical foundation for modern cognitive science.

Tolman's cognitive maps of [Tolman 1948][research_tolman_1948_cognitive_maps] introduced the specific proposal that rats learn cognitive maps of their environments rather than specific stimulus-response associations. The framework identified the specific empirical phenomena including latent learning, place learning, and shortcuts that support the specific cognitive-map account and challenge the specific stimulus-response account of classical behaviorism. The framework has been substantially extended through the modern hippocampal cognitive map literature treated in article fourteen.

The Miller 1956 Magical Number Seven paper introduced the specific information-theoretic framework for short-term memory. The framework proposed that short-term memory capacity is approximately seven plus-or-minus two chunks,

$$C_{\text{STM}} \approx 7 \pm 2 \text{ chunks}$$

providing the specific quantitative characterization that continues to organize memory research. The framework has been substantially refined through subsequent work but continues to provide the specific empirical foundation for capacity-limited cognitive processing.

Bruner Goodnow Austin 1956 A Study of Thinking provided the specific empirical framework for the study of concept attainment. The framework identified the specific strategies through which subjects acquire novel categorizations from labeled examples and provided the empirical foundation for subsequent categorization research.

The [Newell and Simon 1972][book_newell_simon_1972] Human Problem Solving provided the systematic modern treatment of the specific cognitive processes underlying problem solving. The framework introduced the specific problem-space framework in which problem solving is characterized as search through a space of intermediate cognitive states, providing the specific bridge between cognitive psychology and artificial intelligence research.

The specific correspondence between the cognitive revolution and modern computational cognitive science has been substantial. The specific commitment to unobservable computational processes as legitimate objects of study underlies the modern computational cognitive science research program, and the specific empirical phenomena identified during the cognitive revolution continue to provide benchmarks against which modern computational theories are evaluated.

## Attention-Based Associative Learning

Attention-based models of associative learning were developed in the 1970s and 1980s to address the specific limitations of the Rescorla-Wagner model on phenomena including latent inhibition and the differential learning rates observed with different CSs.

The Mackintosh attention model of [Mackintosh 1975][research_mackintosh_1975] proposed that the CS-specific learning rate $\alpha_{\text{CS}}$ increases when the CS is a good predictor of the US and decreases when the CS is a poor predictor. The framework provides the specific mechanism through which prior experience with a CS affects subsequent learning about the same CS. The formal update takes the form

$$\Delta \alpha_A > 0 \text{ iff } |\lambda - V_A| < |\lambda - V_X|$$

with $\alpha_A$ the learning rate for CS A and $V_X$ the summed associative strength of all other CSs present on the trial. The specific update reflects the observation that a CS receives more attention when it predicts the US better than the alternative CSs present.

The Pearce-Hall attention model of [Pearce and Hall 1980][research_pearce_hall_1980] provided the alternative proposal that the CS-specific learning rate is modulated by the unpredictability of the US on the previous trial. The Pearce-Hall attention update takes the form

$$\alpha_{\text{CS}}^{(n)} = \gamma \, |\lambda^{(n-1)} - \Sigma V^{(n-1)}| + (1 - \gamma) \, \alpha_{\text{CS}}^{(n-1)}$$

with $\alpha_{\text{CS}}^{(n)}$ the attention to the CS on trial $n$, $\gamma$ a smoothing parameter, and the absolute-value term reflecting the unsigned prediction error on the prior trial. The framework predicts that surprise-generating CSs receive more attention and hence faster learning, providing the specific mechanism for latent inhibition and other phenomena.

The two attention-based models make specific opposing predictions in several experimental paradigms. The Mackintosh model predicts that predictive CSs receive more attention, while the Pearce-Hall model predicts that surprising CSs receive more attention. Substantial empirical work has documented that both mechanisms operate under different experimental conditions, motivating the modern hybrid attention frameworks that combine both mechanisms.

Modern computational treatments of attention in associative learning connect to the specific frameworks of Bayesian attention allocation, uncertainty-based exploration, and specific reinforcement learning treatments of attention. The framework connects the classical psychological attention literature to modern computational treatments through the shared computational vocabulary.

The specific correspondence between attention-based associative learning and modern reinforcement learning treatments of exploration under uncertainty has been substantially developed. The specific frameworks provide complementary accounts of the specific mechanisms through which learning rates should be adjusted based on the specific properties of the learning environment.

## Reinforcement Learning as Formalized Psychology

Modern reinforcement learning provides the specific formal framework through which the classical psychology of learning has been increasingly reinterpreted. The framework provides the specific computational vocabulary that unifies substantial portions of the classical learning literature under a single formal treatment.

The [Sutton and Barto 1990][research_sutton_barto_1990] Time-Derivative Models of Pavlovian Reinforcement framework introduced the specific proposal that classical conditioning implements a temporal-difference learning algorithm. The framework provides the specific unification of Pavlovian conditioning with the modern reinforcement learning framework and has been substantially developed through subsequent work.

The [Daw Niv Dayan 2005][research_daw_niv_dayan_2005_a264] Uncertainty-Based Competition framework introduced the specific proposal that the brain implements both model-based and model-free reinforcement learning systems that compete for behavioral control based on the specific uncertainty properties of the current situation. The framework combines the two value estimates through an uncertainty-weighted average

$$V(s, a) = w_{\text{MB}}(s, a) \, V_{\text{MB}}(s, a) + (1 - w_{\text{MB}}(s, a)) \, V_{\text{MF}}(s, a)$$

with $w_{\text{MB}}(s, a) \propto 1/\sigma^2_{\text{MB}}(s, a)$ the model-based weight scaled by the inverse variance of the model-based estimate. The framework provides the specific computational account of the classical psychological distinction between habitual and goal-directed behavior and continues to organize substantial modern research.

The specific correspondence between habit versus goal-directed behavior and model-free versus model-based reinforcement learning has been extensively documented through experimental paradigms including the [Adams 1982][research_adams_1982] outcome-devaluation task. Behaviors that are insensitive to outcome devaluation are treated as habitual (model-free), while behaviors that are sensitive to outcome devaluation are treated as goal-directed (model-based). The framework provides the specific empirical operationalization of the theoretical distinction.

Dopaminergic reward-prediction-error signals treated in article fourteen provide the specific neurobiological instantiation of the temporal-difference learning framework, connecting the psychological learning theory to the specific neurobiological mechanisms. The specific bidirectional exchange has substantially advanced both fields through the shared computational vocabulary.

The [Doll Simon Daw 2012][research_doll_simon_daw_2012] Ubiquity of Model-Based Reinforcement Learning framework consolidated the modern understanding of model-based versus model-free reinforcement learning in psychological research and identified the specific research directions that continue to organize the field.

The specific extensions of reinforcement learning to psychological phenomena beyond direct reward learning include the successor-representation framework treated in article fourteen, the specific application of hierarchical reinforcement learning to human behavior, and the specific application of meta-reinforcement learning to cognitive flexibility and rapid task adaptation.

The [Gläscher Daw Dayan O'Doherty 2010][research_glascher_et_al_2010] States Rewards and the Basis of Habitual and Goal-Directed Control framework provided the systematic empirical fMRI dissociation of the neural substrates of the model-based and model-free reinforcement learning systems, providing the specific empirical validation of the Daw et al 2005 dual-system proposal. The [Balleine Daw O'Doherty 2008][research_balleine_daw_odoherty_2008] Multiple Forms of Value Learning framework consolidated the modern understanding of the specific value-learning mechanisms in the human brain and identified the specific behavioral and neural signatures of the multiple learning systems.

The cost of control framework of [Kool Cushman Gershman 2018][research_kool_cushman_gershman_2018] extended the framework with the specific proposal that model-based control is subjectively costly and therefore avoided when the specific reward advantages do not exceed the cost. The framework provides the specific rational account of the empirical patterns of habit versus goal-directed control observed across many experimental paradigms.

## Categorization and Concept Learning

Categorization and concept learning treat the specific psychological processes through which entities are grouped into meaningful categories. The framework provides the empirical and theoretical foundation for the specific study of conceptual knowledge and its acquisition.

The classical view of concepts as necessary-and-sufficient feature lists was substantially challenged by the [Rosch 1975][research_rosch_1975] prototype theory framework. The framework proposed that categories are organized around prototypical examples rather than necessary-and-sufficient conditions, and that category membership is a graded rather than binary matter. The prototype-based classification computes similarity to a category prototype

$$P(C_k \mid x^*) \propto s(x^*, p_k) \, p(C_k)$$

with $p_k$ the category prototype and $s$ a similarity function. The framework has substantial empirical support from categorization experiments and continues to organize substantial modern categorization research.

Exemplar models of categorization including the [Nosofsky 1986][research_nosofsky_1986] Generalized Context Model provided the specific formal alternative in which category judgments are computed by comparing the target item to specific stored exemplars of each category. The framework produces quantitative fits to empirical categorization data that often exceed those of prototype models.

The Nosofsky Generalized Context Model computes the specific classification decision as

$$P(C_k \mid x^*) = \frac{\sum_{i \in C_k} \eta(x^*, x_i)}{\sum_{j} \eta(x^*, x_j)}$$

with $\eta(x^*, x_i) = \exp(-c \, d(x^*, x_i))$ the exemplar-similarity function and $d(x^*, x_i)$ a weighted-Minkowski distance metric. The framework provides quantitative fits to empirical categorization data and has been substantially influential in subsequent categorization research.

Rule-based models of categorization propose that categorization is performed through the specific application of learned or hypothesized rules rather than through similarity-based comparison. The specific correspondence between rule-based and similarity-based categorization has been extensively studied, and modern accounts increasingly recognize that both mechanisms operate in different circumstances.

Bayesian models of concept learning of [Tenenbaum 1999][research_tenenbaum_1999] and the substantial subsequent literature provided the specific probabilistic framework in which concept acquisition is characterized as Bayesian inference over a hypothesis space of candidate concepts. The Bayesian generalization update computes

$$p(h \mid X) \propto p(X \mid h) \, p(h) = \left[\prod_{x \in X} \mathbb{1}[x \in h] / |h|\right] \, p(h)$$

with the specific size principle likelihood favoring smaller hypotheses consistent with the observed examples. The framework provides the systematic formal treatment of concept learning as rational inference and has been substantially influential in modern computational cognitive science.

Kruschke's ALCOVE model of [Kruschke 1992][research_kruschke_1992_alcove] introduced the specific attention-modulated exemplar model of categorization that combines the specific advantages of exemplar-based classification with the specific attention-based learning mechanism of the Mackintosh framework. The ALCOVE activation of exemplar node $i$ takes the form

$$a_i^{\text{exemplar}} = \exp\!\left(-c \, \left[\sum_j \alpha_j \, |x_j^* - x_{i,j}|^r\right]^{q/r}\right)$$

with $\alpha_j$ the learned attention weight for dimension $j$ and $c, q, r$ model hyperparameters. The framework has been substantially influential in modern categorization research.

The rational analysis of categorization of [Anderson 1991][research_anderson_1991] introduced the specific Bayesian nonparametric framework in which category structure is inferred from observed examples through Dirichlet process priors over category-count distributions. The framework provides the specific rational account of category learning that continues to shape modern Bayesian categorization research. The [Ashby Alfonso-Reese Turken Waldron 1998][research_ashby_et_al_1998_covis] COVIS framework provided the specific neurally-motivated dual-system model of category learning that identifies distinct rule-based and information-integration category-learning systems. SUSTAIN of [Love Medin Gureckis 2004][research_love_medin_gureckis_2004] introduced the specific network model of category learning that dynamically recruits new category clusters as needed, providing the specific alternative to fixed-prototype and fixed-exemplar frameworks.

Modern computational treatments of categorization increasingly connect to the specific representation-learning frameworks of modern deep learning. The [Kemp and Tenenbaum 2008][research_kemp_tenenbaum_2008] Discovery of Structural Form framework extended the Bayesian framework to the specific learning of the structural form (chain, tree, ring, grid) that best organizes a domain of categories, providing the systematic bridge between the classical categorization literature and modern computational structure learning. The framework continues to organize substantial research on the specific computational mechanisms underlying category learning.

## Analogical Reasoning, Insight, and Problem Solving

Analogical reasoning, insight, and problem solving treat the specific cognitive processes through which novel solutions to problems are discovered through the systematic use of prior knowledge. The framework provides the specific empirical and theoretical bridge from the classical Gestalt tradition through modern computational cognitive science.

Insight learning of [Köhler 1925][book_kohler_1925] documented the specific problem-solving behavior of chimpanzees through the specific experiments in which apes solved novel problems through the sudden reorganization of the perceptual field rather than through gradual trial-and-error learning. The framework provided the specific empirical challenge to strict behaviorist accounts and established the specific empirical foundation for the modern insight-learning literature.

The systematic modern treatment of insight problem-solving of [Wallas 1926][book_wallas_1926] introduced the specific four-stage account including preparation, incubation, illumination, and verification that continues to organize the specific psychological research on creative problem solving. The framework has been substantially refined through subsequent work but continues to provide the foundational vocabulary.

The [Duncker 1945][book_duncker_1945] Problem Solving framework introduced the specific empirical demonstrations of functional fixedness, the specific psychological phenomenon in which prior use of an object for one function inhibits the perception of alternative uses. The framework has been extensively studied and continues to organize modern research on the specific creative-cognition phenomena.

Analogical reasoning has been systematically studied through the [Gentner 1983][research_gentner_1983] structure-mapping framework in which analogies are characterized as specific structural correspondences between source and target domains. The framework identifies the specific relational-similarity computations that support analogical inference and continues to organize modern research on the specific cognitive mechanisms of analogy.

The formal structure-mapping framework specifies the mapping between source $S$ and target $T$ as

$$m^* = \arg\max_m \, \text{StructuralConsistency}(m) + \text{Systematicity}(m)$$

with the specific preference for mappings that preserve relational structure over surface similarity and for mappings that connect to higher-order relations. The framework provides quantitative fits to human analogical-reasoning behavior across many domains.

The Structure-Mapping Engine of [Falkenhainer Forbus Gentner 1989][research_falkenhainer_forbus_gentner_1989] provided the specific computational implementation of structure-mapping theory that has been extensively applied in cognitive-science research. The framework has been substantially extended through subsequent work and continues to provide the specific computational foundation for the analogical-reasoning literature.

Problem solving as search of [Newell and Simon 1972][book_newell_simon_1972] treated in the Cognitive Revolution section provided the systematic modern framework for problem solving as heuristic search through problem spaces. The framework has been substantially extended through subsequent work on the specific patterns of problem-solving behavior and provides the specific bridge to modern AI research on problem solving.

Modern computational treatments of insight and analogical reasoning include the specific frameworks of program synthesis, structure discovery, and modern foundation models that exhibit specific analogical-reasoning capabilities. The framework provides the specific bridge between the classical insight-and-analogy literature and modern computational cognitive science.

## Social Learning and Observational Acquisition

Social learning treats the specific class of learning phenomena in which behavioral acquisition occurs through observation of others rather than through direct experience with rewards and punishments. The framework connects the psychology of learning to social psychology and to the multi-agent learning treatments of article eleven.

Bandura's social learning theory treated in article eleven provided the systematic modern framework for observational learning. The framework identifies the specific attentional, retention, reproduction, and motivational processes that support the acquisition of behaviors through observation of models.

The specific empirical demonstration of observational learning through the [Bandura Ross Ross 1961][research_bandura_ross_ross_1961] Bobo Doll experiments documented that children spontaneously acquire aggressive behaviors through observation of adult models, providing the specific empirical foundation for the observational-learning framework.

Vicarious reinforcement is the specific phenomenon in which observed reinforcement of a model affects the observer's likelihood of performing similar behavior. The specific update integrates observed and direct reinforcement through

$$\Delta P(a) = \eta_{\text{direct}} \, r_{\text{self}}(a) + \eta_{\text{vicarious}} \, r_{\text{model}}(a)$$

with $\eta_{\text{vicarious}} < \eta_{\text{direct}}$ typically observed empirically. The framework extends the operant framework beyond direct reinforcement of the observer's own behavior to encompass the specific effects of observing others' outcomes.

Modeling and imitation have been extensively studied both empirically and computationally. The specific developmental progression from reflexive imitation through selective imitation to culturally-shaped imitation treated in article twelve provides the specific developmental foundation for the modern computational treatments.

Social learning strategies of [Laland 2004][research_laland_2004] identified the specific rules through which individuals selectively copy behaviors from specific others. The framework identifies specific strategies including copy-successful-individuals, copy-the-majority, and copy-when-uncertain, and provides the specific empirical framework for the study of strategic social learning. The copy-successful strategy takes the specific form

$$P(\text{adopt } a) \propto \exp(\beta \, \bar{r}(a))$$

with $\bar{r}(a)$ the observed average reward of individuals performing behavior $a$ and $\beta$ a temperature parameter that controls the specific concentration of copying on the most-successful behaviors.

Modern computational treatments of social learning include the specific frameworks for learning from demonstration, learning from preference, and multi-agent reinforcement learning treated in article eleven. The framework provides the specific bridge between the classical social learning literature and modern machine learning practice.

## Skill Acquisition and Expertise

Skill acquisition and expertise treat the specific psychological processes through which highly-skilled performance is acquired through extensive practice. The framework provides the empirical and theoretical foundation for the study of long-term learning and cognitive development.

The [Fitts and Posner 1967][book_fitts_posner_1967] Human Performance framework introduced the specific three-stage model of skill acquisition including cognitive, associative, and autonomous stages. The framework has been substantially influential in subsequent skill-acquisition research and continues to provide the systematic developmental framework.

Chunking as a mechanism for expertise was systematically documented by [Chase and Simon 1973][research_chase_simon_1973] through the specific comparative study of chess-position memory in masters versus novices. The framework demonstrated that expert memory advantages depend on the specific ability to encode meaningful chunks rather than on generic memory superiority. The framework has been substantially extended to many other expertise domains.

The power law of practice of [Newell and Rosenbloom 1981][research_newell_rosenbloom_1981] provided the specific quantitative characterization of skill improvement across practice as

$$T(n) = T_0 + A \, n^{-\beta}$$

with $T(n)$ the time to complete the task on the $n$-th trial, $T_0$ the asymptotic time, and $\beta$ a positive exponent typically around 0.5. The framework has substantial empirical support across many skill domains and provides the specific quantitative benchmark against which computational models of skill acquisition are evaluated.

Fitts's law of [Fitts 1954][research_fitts_1954] provided the systematic quantitative characterization of the specific speed-accuracy tradeoff in motor movement,

$$T = a + b \, \log_2\!\left(\frac{2 D}{W}\right)$$

with $T$ the movement time, $D$ the movement distance, $W$ the target width, and $a, b$ device- and task-specific constants. The framework has substantial empirical support and has been extensively applied in human-computer interaction design.

Deliberate practice of [Ericsson Krampe Tesch-Römer 1993][research_ericsson_krampe_tesch_romer_1993] introduced the specific proposal that expert-level performance is acquired through extensive deliberate practice rather than through generic experience. The framework identifies the specific characteristics of deliberate practice including focused effort, feedback, and progressive difficulty adjustment. The framework has substantially shaped both practical training methodology and theoretical accounts of expertise.

Automaticity is the specific end-state of skill acquisition in which performance becomes fast, effortless, and resistant to interference. The [Shiffrin and Schneider 1977][research_shiffrin_schneider_1977] automaticity framework provided the systematic empirical characterization of the specific developmental progression from controlled to automatic processing. The framework has been substantially extended to modern cognitive control and executive function research.

Modern computational treatments of skill acquisition include the specific frameworks of hierarchical reinforcement learning, options learning, and skill-primitive discovery treated in article six. The framework provides the specific bridge between the classical expertise literature and modern reinforcement learning practice.

The specific role of deliberate practice in artificial systems remains an active research area. Modern deep learning systems achieve substantial capability through the specific training regimes that mirror aspects of human deliberate practice, and the specific correspondence between artificial and human skill acquisition continues to organize substantial research.

## Metacognition and Learning-to-Learn

Metacognition treats the specific psychological processes through which learners monitor and regulate their own cognitive activities. The framework provides the specific empirical and theoretical bridge between the classical learning literature and modern research on self-regulated learning, and provides the specific psychological foundation for the meta-learning treatments of article nine.

The [Flavell 1979][research_flavell_1979] Metacognition and Cognitive Monitoring framework introduced the systematic modern treatment of metacognitive knowledge, metacognitive experiences, and metacognitive strategies. The framework identifies the specific cognitive components that support the monitoring and control of the specific learning process and continues to organize modern metacognition research.

The [Nelson and Narens 1990][research_nelson_narens_1990] Metamemory framework provided the specific theoretical framework for metacognition through the specific proposal that metacognitive processes involve two distinct levels of representation, with the specific monitoring and control processes connecting the two levels. The framework has substantial empirical support and provides the specific formal foundation for the modern metacognition research.

Metamemory judgments including feeling-of-knowing, judgments-of-learning, and confidence judgments have been extensively studied and provide the specific empirical operationalization of metacognitive processes. The specific accuracy of these judgments provides the specific measure of metacognitive competence and has been shown to correlate with academic achievement across many domains.

Learning sets of [Harlow 1949][research_harlow_1949] provided the specific empirical framework for learning-to-learn through the systematic study of discrimination-reversal learning. The framework documented that primates progressively improve their learning speed across successive discrimination problems, providing the specific empirical foundation for the modern meta-learning literature.

Modern computational treatments of metacognition include the specific frameworks for meta-reinforcement learning treated in article nine, the specific frameworks for uncertainty estimation in modern deep learning, and the specific frameworks for foundation-model confidence calibration. The framework provides the specific bridge between the classical metacognition literature and modern computational cognitive science.

## Individual Differences in Learning

Individual differences in learning treat the specific systematic variation across individuals in learning capacity, style, and outcome. The framework provides the specific empirical and theoretical foundation for the study of the specific factors that shape individual learning trajectories.

Intelligence as a specific factor supporting learning has been extensively studied through the specific psychometric tradition that traces to [Spearman 1904][research_spearman_1904] Two Factor Theory. The framework identified the specific $g$ factor of general intelligence that correlates positively with performance across many cognitive tasks and provides the specific quantitative characterization of individual differences in cognitive ability. The framework continues to organize substantial modern research on intelligence and its correlates.

The [Cattell 1963][research_cattell_1963] Fluid and Crystallized Intelligence framework provided the specific distinction between fluid intelligence (the ability to reason and solve novel problems) and crystallized intelligence (accumulated knowledge and vocabulary). The framework has substantial empirical support and provides the specific psychological foundation for the modern research on cognitive aging and the specific patterns of intellectual change across the lifespan.

Working memory capacity as a specific individual difference has been extensively studied through the [Engle 2002][research_engle_2002] individual differences framework. The framework documents the specific correlation between working memory capacity and performance across many cognitive tasks, providing the specific quantitative characterization of the individual differences that shape learning outcomes.

Aptitude-treatment interactions of [Cronbach and Snow 1977][book_cronbach_snow_1977] provided the systematic modern framework for the specific study of the interaction between individual differences and instructional treatments. The framework proposes that instructional methods differ in their effectiveness across individuals with different aptitude profiles, providing the specific empirical foundation for personalized instruction.

Modern computational treatments of individual differences include the specific frameworks for personalized learning technology, the specific frameworks for adaptive testing, and the specific frameworks for individualized reinforcement learning treatments in behavioral interventions. The framework provides the specific bridge between the classical individual-differences literature and modern computational learning practice.

## Memory Systems and Learning

Memory systems provide the specific psychological framework for the different kinds of long-term change that result from learning experiences. The framework provides the empirical and theoretical foundation for understanding what is learned and how it is stored.

The Atkinson-Shiffrin multi-store model of [Atkinson and Shiffrin 1968][research_atkinson_shiffrin_1968] introduced the specific three-stage framework including sensory memory, short-term memory, and long-term memory. The framework has been substantially refined but continues to provide the foundational architecture for memory research. Ebbinghaus's forgetting curve of [Ebbinghaus 1885][book_ebbinghaus_1885] provided the systematic quantitative characterization of memory retention over time,

$$R(t) = R_0 \, e^{-t/\tau}$$

with $R(t)$ the retention at time $t$ after learning, $R_0$ the initial retention, and $\tau$ a memory-specific time constant. The framework has been substantially refined through subsequent work but the specific exponential-decay form continues to provide the foundational characterization of retention dynamics.

Working memory of [Baddeley and Hitch 1974][research_baddeley_hitch_1974] extended the framework with the specific working-memory architecture including the phonological loop, visuospatial sketchpad, and central executive components. Short-term memory decay follows the specific characterization

$$P(\text{recall} \mid \text{delay} = t) = P_0 \, e^{-t/\tau_{\text{STM}}}$$

with $\tau_{\text{STM}} \approx 20 \text{ s}$ in the absence of active rehearsal, matching the specific empirical decay observed in Brown-Peterson-task studies. The framework has been extensively studied and continues to organize modern working memory research.

The specific distinction between episodic and semantic memory of [Tulving 1972][research_tulving_1972] provided the systematic empirical foundation for the modern multi-system view of long-term memory. Episodic memory refers to the specific memory for personally-experienced events with contextual detail, and semantic memory refers to the specific memory for general facts and knowledge without contextual detail. The framework has substantial empirical support from neuropsychological studies of memory-impaired patients.

The specific distinction between declarative and non-declarative memory of [Cohen and Squire 1980][research_cohen_squire_1980] provided the complementary categorization that groups episodic and semantic memory as declarative while grouping procedural, priming, and conditioning phenomena as non-declarative. The framework has substantial empirical support and continues to organize modern memory research.

The [Squire 2004][research_squire_2004] Memory Systems framework consolidated the modern multi-system view of memory and identified the specific neural substrates of each memory system. The framework provides the systematic modern treatment that unifies psychological and neuroscientific perspectives on memory.

Levels of processing of [Craik and Lockhart 1972][research_craik_lockhart_1972] introduced the specific alternative framework in which memory encoding depth (shallow perceptual through deep semantic) determines subsequent retention, providing the systematic quantitative alternative to the strict multi-store framework. Encoding specificity of [Tulving and Thomson 1973][research_tulving_thomson_1973] documented the specific dependence of retrieval on the match between encoding and retrieval contexts, providing the foundational modern account of the specific context-dependence of memory that continues to organize research on retrieval. Memory consolidation of [McGaugh 2000][research_mcgaugh_2000] consolidated the modern understanding of the specific molecular and systems-level mechanisms of memory consolidation, providing the systematic bridge between cellular neuroscience and the specific psychological memory phenomena.

Modern computational treatments of memory include the specific frameworks of complementary learning systems treated in articles ten and fourteen, the specific memory-augmented neural networks treated in article fourteen, and the specific memory-consolidation frameworks in machine learning. The framework provides the specific bridge between the classical memory-systems literature and modern computational cognitive science.

The specific correspondence between machine learning memory systems and biological memory systems has been substantially developed through recent research. The specific frameworks including neural Turing machines, differentiable neural computers, and modern retrieval-augmented generation provide the specific computational instantiations of memory systems that connect to the biological framework.

## Learning Across the Lifespan

Learning across the lifespan treats the specific developmental trajectories of learning capacity from infancy through senescence. The framework provides the specific empirical and theoretical bridge between the classical developmental tradition and modern research on cognitive aging.

Early learning in infancy has been extensively studied through the specific methodological frameworks of habituation, preferential looking, and violation-of-expectation paradigms. The [Meltzoff and Moore 1977][research_meltzoff_moore_1977] neonatal imitation findings documented the specific early emergence of imitative learning, and the [Baillargeon 1987][research_baillargeon_1987] object permanence findings documented the specific early emergence of physical-world knowledge. The framework provides the specific empirical foundation for the modern developmental cognitive science literature, and connects directly to the developmental treatments of article thirteen.

Piaget's stage theory of [Piaget 1952][book_piaget_1952] Origins of Intelligence in Children provided the systematic developmental framework in which cognitive development proceeds through the specific sequence of sensorimotor, preoperational, concrete-operational, and formal-operational stages. The framework has been substantially refined and challenged through subsequent work but continues to provide the foundational vocabulary for developmental cognitive science.

The [Vygotsky 1978][book_vygotsky_1978] Mind in Society framework introduced the specific social-constructivist alternative to Piaget in which cognitive development is mediated by social interaction with more knowledgeable others through the zone of proximal development. The framework provides the specific psychological foundation for scaffolding-based approaches to education and for social-learning treatments in machine learning.

Lifespan developmental psychology of [Baltes 1987][research_baltes_1987] introduced the specific systematic framework for cognitive development across the entire lifespan through the specific propositions that development involves gains and losses at all ages, is multidirectional and multidimensional, and is shaped by historical and cultural context. The framework has substantial empirical support and provides the specific psychological foundation for the modern lifespan-development literature.

Cognitive aging has been systematically studied through the specific frameworks of [Craik and Salthouse 2008][book_craik_salthouse_2008] Handbook of Aging and Cognition. The framework documents the specific patterns of age-related cognitive change including declines in processing speed, working memory, and episodic memory alongside the specific preservation of crystallized intelligence and semantic memory. The specific processing-speed theory of [Salthouse 1996][research_salthouse_1996] proposes that age-related cognitive decline is substantially mediated by reductions in processing speed, and continues to organize substantial modern cognitive-aging research.

Neuroplasticity across the lifespan has been substantially developed through modern research showing that neuroplasticity persists into old age but with the specific quantitative reductions that shape learning capacity. The framework provides the specific bridge between the classical cognitive-aging literature and the modern neuroscience-of-aging research.

Modern computational treatments of lifespan learning include the specific frameworks for continual learning treated in article ten, the specific frameworks for developmental machine learning treated in article thirteen, and the specific frameworks for age-appropriate personalization in learning technology. The framework provides the specific bridge between the classical lifespan-development literature and modern computational cognitive science.

## Bayesian Models of Cognition

Bayesian models of cognition provide the specific probabilistic framework through which cognitive processes have been increasingly formalized. The framework provides the specific alternative to both the classical symbolic and the classical connectionist frameworks for cognitive modeling.

The Tenenbaum Kemp Griffiths Goodman 2011 How to Grow a Mind framework provided the systematic modern statement of the Bayesian cognitive science research program. The framework proposes that cognition is fundamentally Bayesian inference over structured hypothesis spaces, and provides the specific computational vocabulary for the specific treatment of concept learning, causal reasoning, and other cognitive processes.

The general Bayesian framework computes the posterior over hypotheses through Bayes' rule,

$$p(h \mid d) = \frac{p(d \mid h) \, p(h)}{p(d)}$$

with $h$ a candidate hypothesis, $d$ observed data, $p(h)$ the prior, $p(d \mid h)$ the likelihood, and $p(h \mid d)$ the posterior. The framework provides the systematic formal treatment of many cognitive phenomena.

The [Griffiths Chater Kemp Perfors Tenenbaum 2010][research_griffiths_et_al_2010] Probabilistic Models of Cognition tutorial consolidated the modern Bayesian cognitive science literature and provided the specific methodological framework for the systematic application of Bayesian modeling to psychological phenomena.

Concept learning as Bayesian inference of Tenenbaum 1999 provided the specific paradigmatic application. The framework treats concept acquisition as inference over a hypothesis space of candidate concepts given observed examples, and produces quantitative fits to human categorization data across many concept domains.

Causal reasoning as Bayesian inference of [Gopnik Glymour Sobel Schulz Kushnir Danks 2004][research_gopnik_et_al_2004] extended the framework to the specific study of causal learning in children and adults. The framework treats causal learning as inference over causal-graph structures given observed evidence,

$$p(G \mid D) \propto p(D \mid G) \, p(G) = \prod_i p(x_i \mid \text{Pa}_G(x_i)) \, p(G)$$

with $G$ a candidate causal graph and $\text{Pa}_G(x_i)$ the parents of variable $x_i$ under graph $G$. The framework provides quantitative fits to human causal-reasoning behavior across many domains.

The specific correspondence between Bayesian cognitive science and modern machine learning has been substantially developed. The specific frameworks including Bayesian deep learning, probabilistic programming, and variational inference provide the specific computational infrastructure through which Bayesian cognitive models can be scaled to complex domains.

The specific limitations of Bayesian cognitive modeling include the specific computational tractability concerns for inference over rich hypothesis spaces and the specific empirical questions about whether biological cognition actually implements approximate Bayesian inference. The [Sanborn and Chater 2016][research_sanborn_chater_2016] Bayesian Brains without Probabilities framework provided the systematic discussion of the specific alternatives to strict Bayesian inference that produce Bayesian-like behavior.

## Prospect Theory, Heuristics, and Judgment Under Uncertainty

The specific tradition of judgment and decision making treats the specific psychological processes through which humans make choices under uncertainty. The framework has substantially reshaped modern economics through the specific behavioral-economics research program and continues to organize substantial cognitive science research.

Prospect theory of [Kahneman and Tversky 1979][research_kahneman_tversky_1979] introduced the specific formal alternative to expected utility theory that accommodates the specific empirical patterns of human decision-making under risk. The framework proposes that decisions are made based on the specific value function that is concave for gains and convex for losses (loss aversion) and the specific probability weighting function that overweights small probabilities and underweights moderate-to-large probabilities.

The prospect theory value function takes the form

$$v(x) = \begin{cases} x^\alpha & x \geq 0 \\ -\lambda \, (-x)^\beta & x < 0 \end{cases}$$

with $\alpha, \beta \approx 0.88$ and $\lambda \approx 2.25$ producing the specific patterns of risk-seeking for losses, risk-aversion for gains, and asymmetric weighting of losses versus gains that characterize human decision-making. The framework provides quantitative fits to human decision-making across many domains.

The prospect theory probability weighting function

$$w(p) = \frac{p^\gamma}{(p^\gamma + (1-p)^\gamma)^{1/\gamma}}$$

with $\gamma \approx 0.61$ for gains and $\gamma \approx 0.69$ for losses produces the specific pattern in which small probabilities are overweighted and moderate-to-large probabilities are underweighted. The composite decision value under prospect theory takes the form

$$V = \sum_i w(p_i) \, v(x_i)$$

with the specific decision computed as the expected weighted value under the prospect theory value and weighting functions.

Heuristics and biases of [Tversky and Kahneman 1974][research_tversky_kahneman_1974] introduced the specific empirical framework for the systematic study of the shortcuts that humans use in judgment under uncertainty. The framework identified specific heuristics including representativeness, availability, and anchoring-and-adjustment that produce specific systematic biases in human judgment.

Dual-process theory of [Kahneman 2011][book_kahneman_2011] Thinking Fast and Slow consolidated the modern research on the specific two systems of cognitive processing including the fast, automatic System 1 and the slow, deliberative System 2. The framework has substantially shaped modern cognitive psychology and behavioral economics through the specific systematic account of the interaction between the two systems.

Fast and frugal heuristics of [Gigerenzer and Todd 1999][book_gigerenzer_todd_1999] provided the alternative ecological-rationality framework in which heuristics are treated as adaptive solutions to specific environmental structures rather than as systematic biases. The framework has substantially shaped subsequent research on the specific ecological validity of heuristic reasoning.

Cumulative prospect theory of [Tversky and Kahneman 1992][research_tversky_kahneman_1992] extended the original prospect theory framework with the specific cumulative probability weighting that accommodates decisions involving multiple outcomes and eliminates the specific violations of stochastic dominance that the original framework produced. The framework has become the specific standard descriptive theory of decision-making under risk. Bounded rationality of [Simon 1955][research_simon_1955] provided the foundational modern statement of the specific limits of rational decision-making imposed by cognitive constraints, providing the theoretical foundation for the subsequent heuristics-and-biases and behavioral-economics traditions. The [Thaler and Sunstein 2008][book_thaler_sunstein_2008] Nudge framework consolidated the specific applied implications of behavioral economics for policy design through the specific choice-architecture framework.

Modern computational treatments of judgment under uncertainty include the specific frameworks of resource-rational analysis, bounded-rationality models, and specific reinforcement learning treatments of value-based decision-making. The framework provides the specific bridge between the classical heuristics-and-biases literature and modern computational cognitive science.

## Language Acquisition as Learning

Language acquisition provides the specific empirical and theoretical laboratory in which claims about the specific structure of learning are systematically tested. The framework connects the psychology of learning to linguistics and to the language-development treatments of articles twelve and thirteen.

The Chomsky 1959 review of Skinner's Verbal Behavior treated earlier provided the specific systematic critique of the behaviorist account of language acquisition. The framework substantially shaped subsequent linguistics and psychology through the specific argument for innate linguistic structures.

The Universal Grammar framework of [Chomsky 1965][book_chomsky_1965] provided the systematic modern treatment of the specific innate cognitive structures that support language acquisition. The framework has substantially shaped modern linguistics and cognitive science but remains actively contested by usage-based alternatives.

Usage-based language acquisition of Tomasello treated in article thirteen provided the systematic alternative to the Universal Grammar framework through the specific proposal that grammatical structure emerges from the specific patterns of language usage rather than from innate universal grammar. The framework has substantially shaped subsequent developmental linguistics and provides the specific bridge to computational language-acquisition models.

Statistical learning in infants treated in article thirteen provided the specific empirical foundation for the modern view that infants deploy powerful statistical learning mechanisms from the earliest ages. The framework provides the specific empirical grounding for the specific bootstrapping mechanisms through which language acquisition proceeds.

Bayesian models of language acquisition of [Xu and Tenenbaum 2007][research_xu_tenenbaum_2007_a264] and the substantial subsequent literature provided the specific computational framework in which language acquisition is characterized as Bayesian inference over linguistic structures. The specific cross-situational word-learning framework updates the mapping posterior after each labeling instance,

$$p(m \mid W, R) \propto \prod_{(w, r) \in (W, R)} p(w \mid m, r) \, p(m)$$

with $m$ the word-referent mapping, $W$ the observed words, and $R$ the observed referents. The framework provides quantitative fits to empirical child data across many language-acquisition phenomena.

Modern large language models treated in articles four and fourteen provide the specific computational demonstration that substantial linguistic competence can be acquired from massive text exposure through the specific mechanisms of gradient-based learning on next-word-prediction objectives. The framework has substantially reshaped debates about the specific role of innate versus experience-driven mechanisms in language acquisition.

Early language acquisition was systematically reviewed by [Kuhl 2004][research_kuhl_2004] through the specific empirical framework identifying the specific perceptual-narrowing patterns and social-interaction requirements that support language learning. Rule learning by 7-month-old infants of [Marcus Vijayan Rao Vishton 1999][research_marcus_et_al_1999] documented the specific abstract-rule-learning capabilities of infants that go beyond specific statistical learning, providing evidence for the specific structural-representation capacity that computational models must accommodate.

## Predictive Processing and Free Energy in Psychology

Predictive processing and the free energy principle provide the specific modern unified framework through which perception, action, and learning are treated as manifestations of a single specific computational principle. The framework has substantially reshaped modern cognitive science and continues to organize substantial research.

The framework, treated more extensively in articles thirteen and fourteen, proposes that cognitive processes correspond to the specific minimization of prediction error at multiple hierarchical levels. The specific variational-inference formulation minimizes the free energy

$$F = D_{\text{KL}}(q(s) \, \| \, p(s \mid o)) - \log p(o)$$

with $q(s)$ the approximate posterior over hidden states and $p(o)$ the evidence. The specific psychological implications include the systematic account of perception as active inference, emotion as interoceptive inference, and cognitive development as the specific progressive refinement of the generative model.

Interoceptive predictive processing of [Seth 2013][research_seth_2013] extended the framework to the specific account of emotion and subjective experience through the specific proposal that emotions arise from the interoceptive predictive processing of bodily states,

$$\text{emotion}(t) = f_{\text{cat}}\!\left(\text{PE}_{\text{interoceptive}}(t), \, \text{context}(t)\right)$$

with $\text{PE}_{\text{interoceptive}}$ the interoceptive prediction error and $f_{\text{cat}}$ the categorical inference process that produces the specific emotional category from the interoceptive state and context. The framework has substantially influenced modern affective science and provides the specific bridge between predictive processing and emotion research.

Active inference treatments of goal-directed behavior treated in article fourteen provide the specific unified account of the psychological distinction between habitual and goal-directed behavior through the specific mechanism of expected-free-energy minimization. The framework provides the specific computational alternative to the model-free/model-based reinforcement learning distinction.

The specific empirical support for predictive processing accounts of psychological phenomena has been extensively developed through neuroimaging, behavioral, and clinical studies. The specific framework provides testable predictions about the specific patterns of neural activity, behavioral responses, and clinical symptoms that continue to organize substantial modern research.

The specific limitations of predictive processing as a psychological framework include the specific concerns about its explanatory completeness, the specific empirical challenges to particular predictions, and the specific philosophical questions about the relationship between the computational framework and phenomenal experience. The [Clark 2013][research_clark_2013] Whatever Next framework provided the systematic modern statement of the predictive processing research program in psychology and identified the specific research directions that continue to organize the field. Modern debates continue to shape the specific evolution of the framework.

## Neuroscience Connections

The neuroscience of learning has been extensively documented across many decades of research. The framework provides the specific biological grounding for the psychological learning phenomena and provides the specific empirical constraints against which psychological theories must be evaluated.

Long-term potentiation (LTP) of [Bliss and Lømo 1973][research_bliss_lomo_1973] provided the foundational empirical framework for the specific cellular mechanism of learning through the specific demonstration that repeated stimulation of hippocampal synapses produces long-lasting increases in synaptic strength. The specific spike-timing-dependent plasticity (STDP) rule of [Bi and Poo 1998][research_bi_poo_1998] provided the modern quantitative characterization,

$$\Delta w_{ij} = \begin{cases} A^+ \, e^{-\Delta t / \tau^+} & \Delta t > 0 \\ -A^- \, e^{\Delta t / \tau^-} & \Delta t \leq 0 \end{cases}$$

with $\Delta t = t_{\text{post}} - t_{\text{pre}}$ the time difference between post- and pre-synaptic spikes. The framework has substantially shaped subsequent cellular neuroscience of learning and provides the specific bridge between the Hebbian learning framework and biological plasticity.

Long-term depression (LTD) provided the complementary decrement in synaptic strength that occurs under specific patterns of neural activity, providing the bidirectional plasticity mechanism required for adaptive learning across many timescales.

Amnesia patients including the celebrated case of patient HM (Henry Molaison) provided the specific empirical foundation for the multi-system view of memory. The specific pattern of preserved procedural memory alongside severely impaired declarative memory in HM provided the definitive empirical evidence for the specific distinction between memory systems. The [Scoville and Milner 1957][research_scoville_milner_1957] foundational report and the [Corkin 2002][research_corkin_2002] subsequent decades-long study provide the systematic empirical foundation.

Dopamine reward-prediction-error signals treated in article fourteen provide the specific neurobiological instantiation of the Rescorla-Wagner and temporal-difference learning frameworks. The specific correspondence has been extensively documented and continues to organize substantial modern research on the reward system.

Modern neuroscience of learning increasingly integrates cellular, systems-level, and behavioral perspectives through the specific computational-cognitive-neuroscience research program. The framework provides the specific bridge between the psychology of learning literature and the neuroscience treatments of article fourteen.

Article sixteen returns to the specific research directions and open questions that will organize the next decade of learning research.

## Applications

Educational applications of the psychology of learning have been substantially developed across many decades. The specific findings on spaced practice, retrieval practice, interleaving, and elaborative encoding provide the specific evidence-based practices that improve learning outcomes. The [Roediger and Karpicke 2006][research_roediger_karpicke_2006] Test-Enhanced Learning framework provided the systematic modern treatment of retrieval practice effects on long-term retention. The [Cepeda Pashler Vul Wixted Rohrer 2008][research_cepeda_et_al_2008] Distributed Practice framework provided the systematic meta-analytic quantitative characterization of the specific spacing effects that continue to shape modern educational practice. The specific spaced-practice benefit follows the specific power law characterization

$$R(t, s) = R_0 \cdot (1 + t/s)^{-\beta}$$

with $R(t, s)$ the retention at time $t$ following a study session with spacing $s$ from prior study, and $\beta$ a task-specific forgetting parameter. The framework predicts the specific optimal spacing intervals that maximize long-term retention and has been extensively deployed in modern learning-technology systems.

Behavior therapy applications include the specific frameworks of applied behavior analysis, cognitive-behavioral therapy, and exposure therapy that deploy the specific empirical findings from the classical learning literature to address behavioral and psychological problems. The specific foundational modern cognitive therapy framework of [Beck 1970][research_beck_1970] applied the specific insights from cognitive psychology to depression treatment, providing the specific practical bridge from research to clinical application. The framework has substantial practical impact across clinical psychology, psychiatry, and education.

Behavioral economics applications include the specific frameworks derived from prospect theory, heuristics and biases, and dual-process theory that address the specific patterns of human decision-making in economic contexts. The framework has substantially influenced modern policy design through the specific nudge interventions and choice-architecture frameworks.

Skill training applications deploy the specific deliberate-practice framework to design effective training regimens across domains including music, sports, medicine, and technical skills. The framework has substantial practical impact on professional training and continuing education.

Behavioral interventions for public health including specific applications to smoking cessation, weight management, and adherence to medical treatment deploy the specific classical and operant learning frameworks alongside the specific modern behavior-change theories. The framework has substantial practical impact across public health practice.

Modern personalized learning technology increasingly deploys the specific findings from the psychology of learning combined with machine learning frameworks for adaptive difficulty selection, personalized feedback, and individualized instruction. The framework provides the specific bridge between the classical educational research and modern educational technology.

## Reproducibility and Methodological Reform

Reproducibility and methodological reform in the psychology of learning treat the specific empirical crisis of the 2010s and the systematic response that reshaped the specific methodological standards of the field. The framework has substantially influenced the specific ways that psychological findings are now produced, reported, and evaluated.

The [Open Science Collaboration 2015][research_osc_2015] Estimating the Reproducibility of Psychological Science project provided the specific systematic empirical assessment of reproducibility across one hundred experimental and correlational studies published in top psychology journals. The framework documented the specific rate at which original findings replicated (approximately thirty six percent for the strict-significance criterion) and provided the specific empirical foundation for the modern methodological reform movement.

The [Simmons Nelson Simonsohn 2011][research_simmons_nelson_simonsohn_2011] False-Positive Psychology framework provided the systematic modern treatment of the specific researcher-degrees-of-freedom problem in which flexibility in data analysis inflates false-positive rates. The framework has substantially influenced the specific movement toward preregistration and specific statistical-transparency standards.

Preregistration and registered reports have emerged as the specific methodological responses to reproducibility concerns. The framework requires researchers to specify hypotheses, methods, and analyses prior to data collection, and provides the specific structural safeguard against the specific hypothesizing-after-results-known problem. The framework has been substantially adopted across psychology and cognitive science.

Effect-size reporting and meta-analytic thinking have become the specific standards for empirical psychology research through the systematic movement to report effect sizes with confidence intervals rather than only null-hypothesis significance tests. The [Cumming 2014][research_cumming_2014] New Statistics framework provided the specific systematic modern treatment of effect-size-based inference and has substantially influenced modern statistical practice.

Sample-size determination through the specific power analysis has become the standard preliminary step for empirical psychology research. The specific finding that the classical psychology literature was substantially underpowered (with median statistical power around fifty percent) provided the specific empirical foundation for the modern movement toward larger sample sizes and multi-site collaborations.

The specific correspondence between reproducibility concerns in psychology and reproducibility concerns in machine learning has been substantially developed in recent years. The specific frameworks for reproducible machine learning research including detailed reporting standards, code and data sharing requirements, and systematic benchmark comparisons provide the specific bridge between the two fields.

Modern computational treatments of reproducibility include the specific frameworks for automated meta-analysis, the specific frameworks for reproducibility assessment through machine learning, and the specific frameworks for personalized inference through Bayesian hierarchical modeling. The framework provides the specific bridge between the classical psychology-of-science tradition and modern computational meta-science.

## Load-Bearing Open Questions

- What is the correct integration of the specific empirical findings from the psychology of learning with the specific computational frameworks of modern machine learning?
- How closely do the specific patterns of human learning correspond to the specific patterns produced by modern reinforcement learning, and where do they systematically diverge?
- What is the correct account of the specific individual differences in learning capacity and style that computational models must accommodate?
- How should the specific developmental progression of learning capabilities across the lifespan be integrated into computational learning theories?
- What is the correct treatment of the specific role of consciousness and awareness in psychological learning phenomena?
- Can the specific insights from the psychology of learning inform the specific design of more effective and more human-like artificial learning systems?
- How should the specific practical applications of the psychology of learning to education, therapy, and behavioral intervention be scaled through modern technology while preserving their specific empirical grounding?
- What is the correct account of the relationship between the specific cellular mechanisms of learning documented in neuroscience and the specific behavioral phenomena documented in psychology?
- How should the specific findings from prospect theory and behavioral economics be integrated with the specific normative frameworks of expected utility theory and Bayesian decision theory?
- Can modern foundation models be productively evaluated as models of human learning across the specific empirical phenomena documented in the psychology of learning literature?

## References

### Books

- [Anderson 1990 Adaptive Character][book_anderson_1990]
- [Bruner Goodnow Austin 1956 Study of Thinking][book_bruner_goodnow_austin_1956]
- [Bush and Mosteller 1955 Stochastic Models][book_bush_mosteller_1955]
- [Chomsky 1965 Aspects of the Theory of Syntax][book_chomsky_1965]
- [Craik and Salthouse 2008 Handbook of Aging and Cognition][book_craik_salthouse_2008]
- [Cronbach and Snow 1977 Aptitudes and Instructional Methods][book_cronbach_snow_1977]
- [Duncker 1945 On Problem Solving][book_duncker_1945]
- [Ebbinghaus 1885 Memory][book_ebbinghaus_1885]
- [Fitts and Posner 1967 Human Performance][book_fitts_posner_1967]
- [Gigerenzer and Todd 1999 Simple Heuristics][book_gigerenzer_todd_1999]
- [Hull 1943 Principles of Behavior][book_hull_1943]
- [Kahneman 2011 Thinking Fast and Slow][book_kahneman_2011]
- [Köhler 1925 Mentality of Apes][book_kohler_1925]
- [Newell and Simon 1972 Human Problem Solving][book_newell_simon_1972]
- [Pavlov 1927 Conditioned Reflexes][book_pavlov_1927]
- [Piaget 1952 Origins of Intelligence in Children][book_piaget_1952]
- [Skinner 1938 Behavior of Organisms][book_skinner_1938]
- [Skinner 1957 Verbal Behavior][book_skinner_1957]
- [Sutton and Barto 2018][book_sutton_barto_2018]
- [Thaler and Sunstein 2008 Nudge][book_thaler_sunstein_2008]
- [Thorndike 1911 Animal Intelligence][book_thorndike_1911]
- [Tolman 1932 Purposive Behavior][book_tolman_1932]
- [Vygotsky 1978 Mind in Society][book_vygotsky_1978]
- [Wallas 1926 Art of Thought][book_wallas_1926]

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

### Research

- [Adams 1982 Outcome Devaluation][research_adams_1982]
- [Anderson 1991 Rational Categorization][research_anderson_1991]
- [Ashby et al 1998 COVIS][research_ashby_et_al_1998_covis]
- [Atkinson and Shiffrin 1968 Multi-Store][research_atkinson_shiffrin_1968]
- [Baddeley and Hitch 1974 Working Memory][research_baddeley_hitch_1974]
- [Baillargeon 1987 Object Permanence][research_baillargeon_1987]
- [Balleine Daw O'Doherty 2008 Multiple Values][research_balleine_daw_odoherty_2008]
- [Balleine and Dickinson 1998 Goal-Directed][research_balleine_dickinson_1998]
- [Baltes 1987 Lifespan Development][research_baltes_1987]
- [Bandura Ross Ross 1961 Bobo Doll][research_bandura_ross_ross_1961]
- [Beck 1970 Cognitive Therapy][research_beck_1970]
- [Berridge and Robinson 1998 Wanting and Liking][research_berridge_robinson_1998]
- [Bi and Poo 1998 STDP][research_bi_poo_1998]
- [Bliss and Lømo 1973 LTP][research_bliss_lomo_1973]
- [Bouton 1993 Extinction Context][research_bouton_1993]
- [Cattell 1963 Fluid and Crystallized Intelligence][research_cattell_1963]
- [Cepeda et al 2008 Distributed Practice][research_cepeda_et_al_2008]
- [Chase and Simon 1973 Chess Expertise][research_chase_simon_1973]
- [Chomsky 1959 Review Verbal Behavior][research_chomsky_1959]
- [Clark 2013 Whatever Next][research_clark_2013]
- [Cohen and Squire 1980 Procedural Declarative][research_cohen_squire_1980]
- [Corkin 2002 HM][research_corkin_2002]
- [Craik and Lockhart 1972 Levels of Processing][research_craik_lockhart_1972]
- [Cumming 2014 New Statistics][research_cumming_2014]
- [Daw Niv Dayan 2005 Uncertainty Competition][research_daw_niv_dayan_2005_a264]
- [Deci 1971 Intrinsic Motivation][research_deci_1971]
- [Dickinson 1985 Actions Habits][research_dickinson_1985]
- [Doll Simon Daw 2012 Ubiquity Model-Based][research_doll_simon_daw_2012]
- [Engle 2002 Working Memory Capacity][research_engle_2002]
- [Ericsson Krampe Tesch-Römer 1993 Deliberate Practice][research_ericsson_krampe_tesch_romer_1993]
- [Estes 1950 Stimulus Sampling][research_estes_1950]
- [Falkenhainer Forbus Gentner 1989 Structure-Mapping Engine][research_falkenhainer_forbus_gentner_1989]
- [Fitts 1954 Speed-Accuracy][research_fitts_1954]
- [Flavell 1979 Metacognition][research_flavell_1979]
- [Gallistel and Gibbon 2000 Time Rate][research_gallistel_gibbon_2000]
- [Gentner 1983 Structure-Mapping][research_gentner_1983]
- [Gläscher et al 2010 States Rewards][research_glascher_et_al_2010]
- [Gopnik et al 2004 Causal Reasoning][research_gopnik_et_al_2004]
- [Griffiths et al 2010 Probabilistic Models][research_griffiths_et_al_2010]
- [Harlow 1949 Learning Sets][research_harlow_1949]
- [Herrnstein 1961 Matching Law][research_herrnstein_1961]
- [Higgins 1997 Regulatory Focus][research_higgins_1997]
- [Kahneman and Tversky 1979 Prospect Theory][research_kahneman_tversky_1979]
- [Kamin 1968 Blocking][research_kamin_1968]
- [Kemp and Tenenbaum 2008 Structural Form][research_kemp_tenenbaum_2008]
- [Kool Cushman Gershman 2018 Cost of Control][research_kool_cushman_gershman_2018]
- [Kruschke 1992 ALCOVE][research_kruschke_1992_alcove]
- [Kuhl 2004 Early Language][research_kuhl_2004]
- [Laland 2004 Social Learning Strategies][research_laland_2004]
- [Love Medin Gureckis 2004 SUSTAIN][research_love_medin_gureckis_2004]
- [Mackintosh 1975 Attention Theory][research_mackintosh_1975]
- [Marcus et al 1999 Infant Rule Learning][research_marcus_et_al_1999]
- [McGaugh 2000 Consolidation][research_mcgaugh_2000]
- [Meltzoff and Moore 1977 Neonatal Imitation][research_meltzoff_moore_1977]
- [Miller 1956 Magical Number Seven][research_miller_1956]
- [Nelson and Narens 1990 Metamemory][research_nelson_narens_1990]
- [Newell and Rosenbloom 1981 Power Law][research_newell_rosenbloom_1981]
- [Nosofsky 1986 Generalized Context][research_nosofsky_1986]
- [Open Science Collaboration 2015 Reproducibility Project][research_osc_2015]
- [Pearce and Hall 1980 Attention Model][research_pearce_hall_1980]
- [Rescorla 1968 Contingency][research_rescorla_1968]
- [Rescorla and Wagner 1972][research_rescorla_wagner_1972]
- [Roediger and Karpicke 2006 Test-Enhanced][research_roediger_karpicke_2006]
- [Rosch 1975 Prototype][research_rosch_1975]
- [Ryan and Deci 2000 Self-Determination Theory][research_ryan_deci_2000]
- [Salthouse 1996 Processing Speed Theory][research_salthouse_1996]
- [Sanborn and Chater 2016 Bayesian Brains][research_sanborn_chater_2016]
- [Scoville and Milner 1957 HM][research_scoville_milner_1957]
- [Seth 2013 Interoceptive Predictive][research_seth_2013]
- [Shiffrin and Schneider 1977 Automaticity][research_shiffrin_schneider_1977]
- [Simmons Nelson Simonsohn 2011 False-Positive Psychology][research_simmons_nelson_simonsohn_2011]
- [Simon 1955 Bounded Rationality][research_simon_1955]
- [Spearman 1904 Two-Factor Theory][research_spearman_1904]
- [Squire 2004 Memory Systems][research_squire_2004]
- [Sutton and Barto 1990 TD Pavlovian][research_sutton_barto_1990]
- [Tenenbaum 1999 Concept Learning][research_tenenbaum_1999]
- [Tenenbaum Kemp Griffiths Goodman 2011 How to Grow a Mind][research_tenenbaum_et_al_2011]
- [Tolman 1948 Cognitive Maps][research_tolman_1948_cognitive_maps]
- [Tolman and Honzik 1930 Latent Learning][research_tolman_honzik_1930]
- [Tulving 1972 Episodic Semantic][research_tulving_1972]
- [Tulving and Thomson 1973 Encoding Specificity][research_tulving_thomson_1973]
- [Tversky and Kahneman 1974 Heuristics][research_tversky_kahneman_1974]
- [Tversky and Kahneman 1992 Cumulative Prospect][research_tversky_kahneman_1992]
- [Wagner 1981 SOP][research_wagner_1981_sop]
- [Watson 1913 Behaviorist Manifesto][research_watson_1913]
- [Xu and Tenenbaum 2007 A264][research_xu_tenenbaum_2007_a264]

[book_anderson_1990]: https://www.taylorfrancis.com/books/mono/10.4324/9780203771730/adaptive-character-thought-john-anderson
[book_bruner_goodnow_austin_1956]: https://www.taylorfrancis.com/books/mono/10.4324/9781315082707/study-thinking-jerome-bruner-jacqueline-goodnow-george-austin
[book_bush_mosteller_1955]: https://scholar.google.com/scholar?q=bush+mosteller+1955+stochastic+models+for+learning
[book_chomsky_1965]: https://mitpress.mit.edu/9780262530071/aspects-of-the-theory-of-syntax/
[book_craik_salthouse_2008]: https://www.taylorfrancis.com/books/edit/10.4324/9780203837665/handbook-aging-cognition-fergus-craik-timothy-salthouse
[book_cronbach_snow_1977]: https://scholar.google.com/scholar?q=cronbach+snow+1977+aptitudes+instructional+methods
[book_duncker_1945]: https://psycnet.apa.org/doi/10.1037/h0093599
[book_ebbinghaus_1885]: https://www.taylorfrancis.com/books/mono/10.4324/9781315802749/memory-hermann-ebbinghaus
[book_fitts_posner_1967]: https://scholar.google.com/scholar?q=fitts+posner+1967+human+performance
[book_gigerenzer_todd_1999]: https://global.oup.com/academic/product/simple-heuristics-that-make-us-smart-9780195143812
[book_hull_1943]: https://scholar.google.com/scholar?q=hull+1943+principles+of+behavior
[book_kahneman_2011]: https://us.macmillan.com/books/9780374533557/thinkingfastandslow
[book_kohler_1925]: https://www.taylorfrancis.com/books/mono/10.4324/9781315010311/mentality-apes-wolfgang-kohler
[book_newell_simon_1972]: https://scholar.google.com/scholar?q=newell+simon+1972+human+problem+solving
[book_pavlov_1927]: https://www.taylorfrancis.com/books/mono/10.4324/9780203010457/conditioned-reflexes-ivan-pavlov
[book_piaget_1952]: https://psycnet.apa.org/doi/10.1037/11494-000
[book_skinner_1938]: https://scholar.google.com/scholar?q=skinner+1938+behavior+of+organisms
[book_skinner_1957]: https://scholar.google.com/scholar?q=skinner+1957+verbal+behavior
[book_sutton_barto_2018]: http://incompleteideas.net/book/the-book-2nd.html
[book_thaler_sunstein_2008]: https://yalebooks.yale.edu/book/9780300262285/nudge/
[book_thorndike_1911]: https://scholar.google.com/scholar?q=thorndike+1911+animal+intelligence
[book_tolman_1932]: https://scholar.google.com/scholar?q=tolman+1932+purposive+behavior+animals+men
[book_vygotsky_1978]: https://www.hup.harvard.edu/books/9780674576292
[book_wallas_1926]: https://scholar.google.com/scholar?q=wallas+1926+art+of+thought
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
[research_adams_1982]: https://www.tandfonline.com/doi/abs/10.1080/14640748208400878
[research_anderson_1991]: https://psycnet.apa.org/doi/10.1037/0033-295X.98.3.409
[research_ashby_et_al_1998_covis]: https://psycnet.apa.org/doi/10.1037/0033-295X.105.3.442
[research_atkinson_shiffrin_1968]: https://www.sciencedirect.com/science/article/pii/S0079742108604223
[research_baddeley_hitch_1974]: https://www.sciencedirect.com/science/article/abs/pii/S0079742108604521
[research_baillargeon_1987]: https://psycnet.apa.org/doi/10.1037/0012-1649.23.5.655
[research_balleine_daw_odoherty_2008]: https://www.nature.com/articles/nrn2357
[research_balleine_dickinson_1998]: https://www.sciencedirect.com/science/article/pii/S0028390898000330
[research_baltes_1987]: https://psycnet.apa.org/doi/10.1037/0012-1649.23.5.611
[research_bandura_ross_ross_1961]: https://psycnet.apa.org/doi/10.1037/h0045925
[research_beck_1970]: https://www.sciencedirect.com/science/article/pii/S0005789470800304
[research_berridge_robinson_1998]: https://www.sciencedirect.com/science/article/abs/pii/S0165017398000198
[research_bi_poo_1998]: https://www.jneurosci.org/content/18/24/10464
[research_bliss_lomo_1973]: https://physoc.onlinelibrary.wiley.com/doi/10.1113/jphysiol.1973.sp010273
[research_bouton_1993]: https://psycnet.apa.org/doi/10.1037/0033-2909.114.1.80
[research_cattell_1963]: https://psycnet.apa.org/doi/10.1037/h0046743
[research_cepeda_et_al_2008]: https://journals.sagepub.com/doi/10.1111/j.1467-9280.2008.02209.x
[research_chase_simon_1973]: https://www.sciencedirect.com/science/article/pii/0010028573900042
[research_chomsky_1959]: https://www.jstor.org/stable/411334
[research_clark_2013]: https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/whatever-next-predictive-brains-situated-agents-and-the-future-of-cognitive-science/33542C736E17E3D1D44E8D03BE5F4CD9
[research_cohen_squire_1980]: https://www.science.org/doi/10.1126/science.7414331
[research_corkin_2002]: https://www.nature.com/articles/nrn726
[research_craik_lockhart_1972]: https://www.sciencedirect.com/science/article/pii/S002253717280001X
[research_cumming_2014]: https://journals.sagepub.com/doi/10.1177/0956797613504966
[research_daw_niv_dayan_2005]: https://www.nature.com/articles/nn1560
[research_daw_niv_dayan_2005_a264]: https://www.nature.com/articles/nn1560
[research_deci_1971]: https://psycnet.apa.org/doi/10.1037/h0030644
[research_dickinson_1985]: https://royalsocietypublishing.org/doi/10.1098/rstb.1985.0010
[research_doll_simon_daw_2012]: https://www.sciencedirect.com/science/article/pii/S0959438812001304
[research_engle_2002]: https://journals.sagepub.com/doi/10.1111/1467-8721.00160
[research_ericsson_krampe_tesch_romer_1993]: https://psycnet.apa.org/doi/10.1037/0033-295X.100.3.363
[research_estes_1950]: https://psycnet.apa.org/doi/10.1037/h0060563
[research_falkenhainer_forbus_gentner_1989]: https://www.sciencedirect.com/science/article/abs/pii/0004370289900774
[research_fitts_1954]: https://psycnet.apa.org/doi/10.1037/h0055392
[research_flavell_1979]: https://psycnet.apa.org/doi/10.1037/0003-066X.34.10.906
[research_gallistel_gibbon_2000]: https://psycnet.apa.org/doi/10.1037/0033-295X.107.2.289
[research_gentner_1983]: https://onlinelibrary.wiley.com/doi/10.1207/s15516709cog0702_3
[research_glascher_et_al_2010]: https://www.cell.com/neuron/fulltext/S0896-6273(10)00287-4
[research_gopnik_et_al_2004]: https://psycnet.apa.org/doi/10.1037/0033-295X.111.1.3
[research_harlow_1949]: https://psycnet.apa.org/doi/10.1037/h0062474
[research_herrnstein_1961]: https://onlinelibrary.wiley.com/doi/10.1901/jeab.1961.4-267
[research_higgins_1997]: https://psycnet.apa.org/doi/10.1037/0003-066X.52.12.1280
[research_griffiths_et_al_2010]: https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(10)00113-X
[research_kahneman_tversky_1979]: https://www.jstor.org/stable/1914185
[research_kamin_1968]: https://scholar.google.com/scholar?q=kamin+1968+predictability+surprise+attention+conditioning
[research_kemp_tenenbaum_2008]: https://www.pnas.org/doi/10.1073/pnas.0802631105
[research_kool_cushman_gershman_2018]: https://link.springer.com/chapter/10.1007/978-3-319-98561-1_7
[research_kruschke_1992_alcove]: https://psycnet.apa.org/doi/10.1037/0033-295X.99.1.22
[research_kuhl_2004]: https://www.nature.com/articles/nrn1533
[research_laland_2004]: https://link.springer.com/article/10.3758/BF03196002
[research_love_medin_gureckis_2004]: https://psycnet.apa.org/doi/10.1037/0033-295X.111.2.309
[research_mackintosh_1975]: https://psycnet.apa.org/doi/10.1037/h0076778
[research_marcus_et_al_1999]: https://www.science.org/doi/10.1126/science.283.5398.77
[research_mcgaugh_2000]: https://www.science.org/doi/10.1126/science.287.5451.248
[research_meltzoff_moore_1977]: https://www.science.org/doi/10.1126/science.198.4312.75
[research_miller_1956]: https://psycnet.apa.org/doi/10.1037/h0043158
[research_nelson_narens_1990]: https://www.sciencedirect.com/science/article/pii/S0079742108604468
[research_newell_rosenbloom_1981]: https://scholar.google.com/scholar?q=newell+rosenbloom+1981+mechanisms+of+skill+acquisition
[research_nosofsky_1986]: https://psycnet.apa.org/doi/10.1037/0096-3445.115.1.39
[research_osc_2015]: https://www.science.org/doi/10.1126/science.aac4716
[research_pearce_hall_1980]: https://psycnet.apa.org/doi/10.1037/0033-295X.87.6.532
[research_rescorla_1968]: https://psycnet.apa.org/doi/10.1037/h0025984
[research_rescorla_wagner_1972]: https://scholar.google.com/scholar?q=rescorla+wagner+1972+theory+pavlovian+conditioning
[research_roediger_karpicke_2006]: https://journals.sagepub.com/doi/10.1111/j.1467-9280.2006.01693.x
[research_rosch_1975]: https://psycnet.apa.org/doi/10.1037/0096-3445.104.3.192
[research_ryan_deci_2000]: https://psycnet.apa.org/doi/10.1037/0003-066X.55.1.68
[research_ryan_deci_2000_a264]: https://psycnet.apa.org/doi/10.1037/0003-066X.55.1.68
[research_salthouse_1996]: https://psycnet.apa.org/doi/10.1037/0033-295X.103.3.403
[research_sanborn_chater_2016]: https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(16)30126-7
[research_scoville_milner_1957]: https://jnnp.bmj.com/content/20/1/11
[research_seth_2013]: https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(13)00219-3
[research_shiffrin_schneider_1977]: https://psycnet.apa.org/doi/10.1037/0033-295X.84.2.127
[research_simmons_nelson_simonsohn_2011]: https://journals.sagepub.com/doi/10.1177/0956797611417632
[research_simon_1955]: https://www.jstor.org/stable/1884852
[research_spearman_1904]: https://www.jstor.org/stable/1412107
[research_squire_2004]: https://www.sciencedirect.com/science/article/pii/S0301008204000188
[research_sutton_barto_1990]: https://scholar.google.com/scholar?q=sutton+barto+1990+time+derivative+models+pavlovian
[research_tenenbaum_1999]: https://papers.nips.cc/paper/1999/hash/f515efb8a3d9c9f5faf1a6cd3c7cf95c-Abstract.html
[research_tenenbaum_et_al_2011]: https://www.science.org/doi/10.1126/science.1192788
[research_tolman_1948_cognitive_maps]: https://psycnet.apa.org/doi/10.1037/h0061626
[research_tolman_honzik_1930]: https://scholar.google.com/scholar?q=tolman+honzik+1930+introduction+removal+reward+maze
[research_tulving_1972]: https://scholar.google.com/scholar?q=tulving+1972+episodic+semantic+memory
[research_tulving_thomson_1973]: https://psycnet.apa.org/doi/10.1037/h0020071
[research_tversky_kahneman_1974]: https://www.science.org/doi/10.1126/science.185.4157.1124
[research_tversky_kahneman_1992]: https://link.springer.com/article/10.1007/BF00122574
[research_wagner_1981_sop]: https://scholar.google.com/scholar?q=wagner+1981+sop+model+behavior
[research_watson_1913]: https://psycnet.apa.org/doi/10.1037/h0074428
[research_xu_tenenbaum_2007_a264]: https://psycnet.apa.org/doi/10.1037/0033-295X.114.2.245
