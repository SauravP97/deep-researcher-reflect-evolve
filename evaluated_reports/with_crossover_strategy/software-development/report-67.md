# Summarize recent research progress in reinforcement learning focused on enabling agents to explore efficiently and proactively under conditions of sparse rewards and constraints, respectively. Additionally, analyze and discuss the potential implications and insights this research provides for trajectory planning problems.

# Deep Research Report: Advances in Reinforcement Learning for Efficient and Constrained Exploration with Implications for Trajectory Planning

### **Executive Summary**

This report summarizes recent research progress in reinforcement learning (RL) focused on two critical challenges: enabling agents to explore efficiently in environments with sparse rewards, and ensuring agents act proactively and safely under operational constraints. For sparse reward problems, where feedback is rare, research has converged on methods that generate dense, internal rewards (intrinsic motivation) or reframe the learning problem (goal-conditioning and skill discovery). For constrained problems, research has formalized the challenge using Constrained Markov Decision Processes (CMDPs) and developed specialized algorithms like Constrained Policy Optimization (CPO) and Lagrangian-based methods to balance reward maximization with safety adherence.

These advancements have profound implications for trajectory planning. Efficient exploration techniques provide mechanisms to discover novel and optimal paths in complex environments without dense, hand-engineered guidance. Curiosity can drive a planner to explore unknown areas, Hindsight Experience Replay (HER) allows learning from failed paths, and skill-discovery methods create high-level primitives for hierarchical planning. Concurrently, safe RL provides the formalisms and algorithms to generate trajectories that are guaranteed to respect physical, environmental, or operational constraints, such as collision avoidance, kinematic limits, and no-fly zones. Key remaining challenges include guaranteeing safety during the exploration process itself, improving sample efficiency, and bridging the gap between simulation and real-world deployment.

### **1. Foundational Concepts**

#### **1.1 Reinforcement Learning and the Exploration-Exploitation Dilemma**

Reinforcement Learning (RL) is a paradigm where an agent learns to make decisions by performing actions in an environment to maximize a cumulative reward signal. A central challenge in RL is the **exploration-exploitation dilemma**: the agent must balance exploiting actions that have yielded high rewards in the past with exploring new, untried actions to discover potentially better strategies ["https://qspace.library.queensu.ca/bitstreams/aaae7d13-1a97-4010-b279-3f037c8fb741/download", "https://intuitionlabs.ai/articles/reinforcement-learning-explained"]. This dilemma is managed through strategies like optimistic initialization of action-values and structured decay of exploration rates over time ["https://medium.com/data-scientists-diary/solving-the-exploration-exploitation-dilemma-in-reinforcement-learning-07b4c21e3d40"].

#### **1.2 The Challenge of Sparse Rewards and Constraints**

The exploration problem is significantly exacerbated under two common conditions:

*   **Sparse Rewards:** In many complex tasks, rewards are only given after a long and specific sequence of actions (e.g., solving a puzzle in Montezuma's Revenge). In such cases, random exploration is highly ineffective, as the probability of stumbling upon a reward signal is vanishingly small ["https://qspace.library.queensu.ca/bitstreams/aaae7d13-1a97-4010-b279-3f037c8fb741/download"].
*   **Constraints:** In real-world applications, agents must operate within safety, budget, or physical limits. An autonomous vehicle must avoid collisions, and a robot must respect its torque limits. Exploring actions that violate these constraints can be costly or catastrophic.

#### **1.3 Trajectory Planning**

Trajectory planning is the process of computing an ordered sequence of states or control inputs for a system to move from a starting point to a destination while satisfying certain objectives and constraints. Traditional formulations often rely on explicit models of the environment and dynamics. RL offers a model-free alternative where an agent can learn to generate trajectories through trial and error, making it well-suited for complex, dynamic environments.

### **2. Efficient Exploration in Sparse Reward Environments**

To overcome the challenge of sparse rewards, researchers have developed techniques that guide exploration more intelligently than random chance. These methods can be broadly categorized into intrinsic motivation, goal-conditioning, and diversity-driven approaches.

#### **2.1 Intrinsic Motivation: Generating Dense Internal Rewards**

Intrinsic Motivation (IM) methods augment the sparse external reward with a dense, internally generated reward signal that encourages exploration [https://arxiv.org/html/2507.19725v1].

*   **Curiosity-Driven Methods:** These methods reward the agent for visiting novel or surprising states. The **Intrinsic Curiosity Module (ICM)** rewards the agent for actions that lead to states it cannot accurately predict, effectively encouraging it to learn the environment's dynamics [https://medium.com/biased-algorithms/curiosity-driven-exploration-in-reinforcement-learning-dd3f7d263fce]. While ICM has been shown to be stable and learn effective exploratory behaviors quickly, its final performance can sometimes resemble that of an agent with no intrinsic motivation [https://tams.informatik.uni-hamburg.de/lehre/2018ws/seminar/ir/doc/slides/AntonWiehe-Exploration_RL.pdf, https://arxiv.org/html/2507.19725v1]. **Random Network Distillation (RND)** is a related technique that also rewards novelty [https://tams.informatik.uni-hamburg.de/lehre/2018ws/seminar/ir/doc/slides/AntonWiehe-Exploration_RL.pdf].
*   **Count-Based Methods:** These methods incentivize visiting less-frequented states. However, simple state counting can lead to suboptimal behaviors, such as an agent repeatedly visiting the boundaries of an environment late in training [https://arxiv.org/html/2507.19725v1].
*   **Information-Theoretic Methods:** These approaches motivate the agent to take actions that maximize the information it gains about the environment. **Variational Information Maximizing Exploration (VIME)** is a key method in this category [https://tams.informatik.uni-hamburg.de/lehre/2018ws/seminar/ir/doc/slides/AntonWiehe-Exploration_RL.pdf].

#### **2.2 Goal-Oriented and Diversity-Driven Exploration**

This paradigm shifts focus from rewarding novelty to achieving diverse goals or learning a repertoire of skills.

*   **Goal-Conditioned RL:**
    *   **Hindsight Experience Replay (HER):** A powerful technique that learns from failures. After an unsuccessful episode, HER retroactively treats the achieved state as the intended goal. By storing this "successful" (but modified) trajectory in the replay buffer, the agent learns valuable skills from every attempt, drastically improving sample efficiency in sparse-reward settings [https://openai.com/index/hindsight-experience-replay/, https://arxiv.org/abs/1707.01495]. This creates an "implicit curriculum" where achievable goals naturally become more complex as the agent's capabilities grow [https://arxiv.org/pdf/1707.01495].
    *   **DISCOVER Algorithm:** The Directed Sparse-Reward Goal-Conditioned Very Long-Horizon RL (DISCOVER) method automatically creates a curriculum by selecting a sequence of exploratory goals that lie in the direction of the final target. It balances goal achievability, novelty, and relevance to solve long-horizon problems that were previously considered intractable ["https://arxiv.org/html/2505.19850v1", https://arxiv.org/abs/2505.19850].
*   **Diversity-Driven & Skill-Discovery Methods:**
    *   **Diversity is All You Need (DIAYN):** This method learns a diverse set of useful skills in an unsupervised manner, without any external reward function. It uses an information-theoretic objective to maximize the mutual information between latent "skill" variables and the states visited by the agent. This incentivizes the agent to learn a repertoire of distinct and recognizable behaviors, which inherently promotes broad exploration [https://arxiv.org/abs/1802.06070, https://www.researchgate.net/publication/323257379_Diversity_is_All_You_Need_Learning_Skills_without_a_Reward_Function].
    *   **Reward Impact Driven Exploration (RIDE):** RIDE is an intrinsic reward mechanism that encourages an agent to take actions that cause significant changes in its learned state representation. By rewarding "impactful" actions, it promotes more effective exploration, especially in procedurally-generated environments.
*   **Implicit Exploration via Entropy Regularization:** Algorithms like **Soft Actor-Critic (SAC)** operate within the maximum entropy RL framework. By augmenting the reward with the policy's entropy, SAC encourages the agent to act as randomly as possible while still achieving the objective. This stochasticity serves as a natural and continuous form of exploration, preventing premature convergence to a suboptimal policy and leading to more stable training.

### **3. Proactive and Safe Exploration Under Constraints**

When agents must operate within safety limits, the exploration problem requires a more structured approach, formalized as Safe RL.

#### **3.1 Formalisms and Core Challenges**

The standard framework for this problem is the **Constrained Markov Decision Process (CMDP)**, which extends the standard MDP by including one or more cost functions and constraints on their expected cumulative values. Environments like **Safety Gym** have been developed to standardize research by providing separate reward (task) and cost (safety) signals.

Research in this area has identified several core challenges:
*   **Guaranteed Safety During Exploration:** The primary difficulty is optimizing a policy while ensuring, with high probability, that no safety constraints are violated during the learning process itself.
*   **Transfer Learning:** A major challenge involves adapting a trained agent to a new environment where either the task objectives or the safety requirements have changed.

#### **3.2 Dominant Algorithm Families**

Two main families of algorithms have emerged to solve CMDPs online:

*   **Constrained Policy Optimization (CPO):** CPO is a trust-region policy search algorithm that provides theoretical guarantees for near-constraint satisfaction at each policy update. It maximizes reward improvement while ensuring that the expected cost of the new policy does not exceed a predefined limit [https://arxiv.org/abs/1705.10528]. A number of variants exist, including SCPO (which introduces a safety critic), PCPO, and FOCOPS [https://www.ijcai.org/proceedings/2024/0913.pdf, https://openreview.net/revisions?id=3uNRbYM3qJ].
*   **Lagrangian Methods:** This approach converts the constrained optimization problem into an unconstrained one by incorporating the constraints into the objective function using Lagrange multipliers. Algorithms like PPO-Lagrangian are widely used. Experimental comparisons suggest a trade-off: CPO offers stricter step-wise safety guarantees, while Lagrangian methods may achieve higher performance or better sample efficiency in some benchmarks [https://papers.neurips.cc/paper_files/paper/2022/file/9a8eb202c060b7d81f5889631cbcd47e-Paper-Conference.pdf].

### **4. Implications and Applications for Trajectory Planning**

The research in efficient and safe exploration directly translates into powerful new tools for trajectory planning in complex, real-world domains.

#### **4.1 Efficient Exploration for Discovering Novel Trajectories**

*   **Discovering Paths with Curiosity:** Intrinsic motivation acts as a guide for discovering novel paths. For example, the "Action-Critic-Curiosity" (A-C-C) framework uses curiosity to promote exploration of unknown areas in robotic trajectory planning, accelerating learning efficiency by over 40% in some studies and helping the agent avoid local optima [https://www.shcas.net/en/article/doi/10.3969/j.issn.1000-386x.2025.03.039].
*   **Goal-Agnostic Planning with HER:** Hindsight Experience Replay enables a planner to learn useful sub-trajectories even from failed attempts. A robot that fails to reach a specific destination still learns the trajectory to wherever it ended up, making the learning process far more sample-efficient [https://dl.acm.org/doi/10.1145/3638529.3654045].
*   **Hierarchical Planning with Skill Discovery:** Skills learned by algorithms like DIAYN can serve as high-level primitives or "options" for a hierarchical planner. Instead of planning a long sequence of low-level motor commands, a planner can compose a shorter sequence of learned skills (e.g., "open door," "grasp object") to generate complex trajectories more efficiently and scalably [https://sites.google.com/view/diayn/].
*   **Curriculum-Based Pathfinding:** The DISCOVER algorithm provides a direct blueprint for decomposing a long-horizon trajectory problem into a series of shorter, achievable steps, guiding the agent toward a distant goal ["https://arxiv.org/html/2505.19850v1"].

#### **4.2 Constrained RL for Safe and Feasible Trajectories**

Safe RL provides the formalisms and enforcement mechanisms to generate trajectories that are guaranteed to be feasible and safe. This is critical for applications in autonomous driving, robotics, and aerial navigation.

*   **State-of-the-Art Enforcement Techniques:**
    *   **Predictive Safety Filters (PSF):** A motion planner can use a PSF to manage constraints like road boundaries and adapt a vehicle's path based on environmental factors like friction.
    *   **Control Barrier Functions (CBF):** CBFs can be used to filter an agent's proposed actions, guaranteeing that only safe actions are executed to navigate around obstacles.
    *   **Controllable Imitative Reinforcement Learning (CIRL):** This approach has proven effective in training driving agents to achieve high success rates in high-fidelity simulators using only vision inputs.
*   **Domain Applications:** These techniques are being applied to enforce specific constraints across various domains:
    *   **Autonomous Driving:** Collision avoidance, adherence to traffic laws, staying within road boundaries.
    *   **Robotics:** Respecting kinematic constraints, joint limits, and actuator torque limits.
    *   **Aerial Navigation:** Adhering to no-fly zones and staying within energy or fuel budgets.

### **5. Synthesis, Open Problems, and Future Directions**

The intersection of efficient and safe exploration presents a frontier for RL research with the potential to unlock widespread deployment of autonomous systems. However, significant challenges remain.

*   **Inherent Tensions:** There is a fundamental trade-off between maximizing exploration to find an optimal policy and satisfying strict safety constraints, which inherently limit the agent's actions. The core open problem is developing algorithms that can provably guarantee safety *during* the exploration and learning process.
*   **Key Challenges:**
    *   **Sample Complexity:** Training deep RL agents, especially for safe exploration, often requires vast amounts of data, which is impractical in the real world [https://www.researchgate.net/publication/395402495_A_Comprehensive_Review_of_Reinforcement_Learning_for_Autonomous_Driving_in_the_CARLA_Simulator].
    *   **Sim-to-Real Gap:** While training in simulation is common, policies often fail to transfer effectively to the real world due to unmodeled dynamics or sensor noise. Bridging this gap for safety-critical systems is a major hurdle [https://neurips.cc/virtual/2024/poster/95701].
    *   **Scalability:** Scaling these methods to high-dimensional state and action spaces while maintaining performance and safety guarantees remains an ongoing challenge.
*   **Future Research Directions:**
    *   **Provably Safe RL:** Developing algorithms with mathematical guarantees of safety throughout the entire learning phase.
    *   **Hierarchical RL (HRL):** Decomposing long-horizon tasks into a hierarchy of sub-goals to make exploration more tractable and structured.
    *   **Offline RL and Imitation Learning:** Leveraging existing datasets to pre-train policies, reducing the need for risky online exploration.
*   **Pioneering Labs and Researchers:** This interdisciplinary field is being advanced by leading academic and industrial labs, including **UC Berkeley (BAIR)**, **Stanford**, **CMU**, **MIT**, **Google DeepMind**, and **OpenAI**. Key researchers include **Pieter Abbeel**, **Sergey Levine**, **Anca Dragan**, **J. Andrew Bagnell**, **Andreas Krause**, and **Jan Peters**, among many others who are shaping the future of safe and intelligent autonomous systems.

### **6. Conclusion & Outlook**

Recent research has equipped reinforcement learning agents with powerful new capabilities for navigating complex environments. Intrinsic motivation, goal-conditioning, and skill discovery have made significant strides in solving the hard exploration problem posed by sparse rewards. Simultaneously, the formalisms and algorithms of safe RL, centered on CMDPs, are providing the tools needed to deploy agents that can act reliably within critical operational constraints.

For trajectory planning, these advancements represent a paradigm shift. They move the field away from reliance on perfect models and hand-crafted reward functions toward systems that can learn to discover novel, efficient, and provably safe trajectories through interaction. As research continues to address the challenges of sample efficiency, sim-to-real transfer, and guaranteed safety during learning, these RL techniques are poised to become a cornerstone of next-generation autonomous robotics, vehicles, and logistics systems.

### **7. References**

*   [https://qspace.library.queensu.ca/bitstreams/aaae7d13-1a97-4010-b279-3f037c8fb741/download](https://qspace.library.queensu.ca/bitstreams/aaae7d13-1a97-4010-b279-3f037c8fb741/download)
*   [https://opendilab.github.io/DI-engine/02_algo/exploration_rl.html](https://opendilab.github.io/DI-engine/02_algo/exploration_rl.html)
*   [https://intuitionlabs.ai/articles/reinforcement-learning-explained](https://intuitionlabs.ai/articles/reinforcement-learning-explained)
*   [https://medium.com/data-scientists-diary/solving-the-exploration-exploitation-dilemma-in-reinforcement-learning-07b4c21e3d40](https://medium.com/data-scientists-diary/solving-the-exploration-exploitation-dilemma-in-reinforcement-learning-07b4c21e3d40)
*   [https://arxiv.org/html/2505.19850v1](https://arxiv.org/html/2505.19850v1)
*   [https://arxiv.org/html/2507.19725v1](https://arxiv.org/html/2507.19725v1)
*   [https://ui.adsabs.harvard.edu/abs/2025arXiv250818420Q/abstract](https://ui.adsabs.harvard.edu/abs/2025arXiv250818420Q/abstract)
*   [https://tams.informatik.uni-hamburg.de/lehre/2018ws/seminar/ir/doc/slides/AntonWiehe-Exploration_RL.pdf](https://tams.informatik.uni-hamburg.de/lehre/2018ws/seminar/ir/doc/slides/AntonWiehe-Exploration_RL.pdf)
*   [https://www.semanticscholar.org/paper/An-Evaluation-Study-of-Intrinsic-Motivation-applied-Andres-Villar-Rodriguez/1dc27caf3c3615028e5a4de536edf6eaf1073b0c](https://www.semanticscholar.org/paper/An-Evaluation-Study-of-Intrinsic-Motivation-applied-Andres-Villar-Rodriguez/1dc27caf3c3615028e5a4de536edf6eaf1073b0c)
*   [https://www.researchgate.net/publication/228631709_Intrinsic_motivation_for_reinforcement_learning_systems](https://www.researchgate.net/publication/228631709_Intrinsic_motivation_for_reinforcement_learning_systems)
*   [https://arxiv.org/pdf/2506.05980](https://arxiv.org/pdf/2506.05980)
*   [http://papers.neurips.cc/paper/8249-diversity-driven-exploration-strategy-for-deep-reinforcement-learning.pdf](http://papers.neurips.cc/paper/8249-diversity-driven-exploration-strategy-for-deep-reinforcement-learning.pdf)
*   [https://arxiv.org/html/2501.11533v1](https://arxiv.org/html/2501.11533v1)
*   [https://openai.com/index/hindsight-experience-replay/](https://openai.com/index/hindsight-experience-replay/)
*   [https://arxiv.org/abs/1707.01495](https://arxiv.org/abs/1707.01495)
*   [https://liner.com/review/hindsight-experience-replay](https://liner.com/review/hindsight-experience-replay)
*   [https://arxiv.org/pdf/1707.01495](https://arxiv.org/pdf/1707.01495)
*   [https://www.semanticscholar.org/paper/Soft-Hindsight-Experience-Replay-He-Zhuang/6253a0f146a36663e908509e14648f8e2a5ab581](https://www.semanticscholar.org/paper/Soft-Hindsight-Experience-Replay-He-Zhuang/6253a0f146a36663e908509e14648f8e2a5ab581)
*   [https://arxiv.org/abs/1802.06070](https://arxiv.org/abs/1802.06070)
*   [https://towardsai.net/p/l/diayn-diversity-is-all-you-need](https://towardsai.net/p/l/diayn-diversity-is-all-you-need)
*   [https://sites.google.com/view/diayn/](https://sites.google.com/view/diayn/)
*   [https://www.researchgate.net/publication/323257379_Diversity_is_All_You_Need_Learning_Skills_without_a_Reward_Function](https://www.researchgate.net/publication/323257379_Diversity_is_All_You_Need_Learning_Skills_without_a_Reward_Function)
*   [https://www.slideshare.net/slideshow/diversity-is-all-you-needdiayn-learning-skills-without-a-reward-function/117168978](https://www.slideshare.net/slideshow/diversity-is-all-you-needdiayn-learning-skills-without-a-reward-function/117168978)
*   [https://www.semanticscholar.org/paper/A-Survey-of-Safe-Reinforcement-Learning-and-MDPs%3A-A-Kushwaha-Ravish/79fa2130c55992691a0e7eb08e1d30c5b51ddef6](https://www.semanticscholar.org/paper/A-Survey-of-Safe-Reinforcement-Learning-and-MDPs%3A-A-Kushwaha-Ravish/79fa2130c55992691a0e7eb08e1d30c5b51ddef6)
*   [https://www.researchgate.net/publication/395481976_Safe_Reinforcement_Learning_with_Constraints_A_Survey](https://www.researchgate.net/publication/395481976_Safe_Reinforcement_Learning_with_Constraints_A_Survey)
*   [https://mosi.uni-saarland.de/assets/theses/ma_philipp_sauer.pdf](https://mosi.uni-saarland.de/assets/theses/ma_philipp_sauer.pdf)
*   [https://www.ijcai.org/proceedings/2024/0913.pdf](https://www.ijcai.org/proceedings/2024/0913.pdf)
*   [https://openreview.net/revisions?id=3uNRbYM3qJ](https://openreview.net/revisions?id=3uNRbYM3qJ)
*   [https://www.shcas.net/en/article/doi/10.3969/j.issn.1000-386x.2025.03.039](https://www.shcas.net/en/article/doi/10.3969/j.issn.1000-386x.2025.03.039)
*   [https://dl.acm.org/doi/10.1145/3638529.3654045](https://dl.acm.org/doi/10.1145/3638529.3654045)
*   [https://medium.com/biased-algorithms/curiosity-driven-exploration-in-reinforcement-learning-dd3f7d263fce](https://medium.com/biased-algorithms/curiosity-driven-exploration-in-reinforcement-learning-dd3f7d263fce)
*   [https://openurl.ebsco.com/contentitem/doi:10.3390/computers14100434?sid=ebsco:plink:crawler&id=ebsco:doi:10.3390/computers14100434](https://openurl.ebsco.com/contentitem/doi:10.3390/computers14100434?sid=ebsco:plink:crawler&id=ebsco:doi:10.3390/computers14100434)
*   [https://www.researchgate.net/publication/395402495_A_Comprehensive_Review_of_Reinforcement_Learning_for_Autonomous_Driving_in_the_CARLA_Simulator](https://www.researchgate.net/publication/395402495_A_Comprehensive_Review_of_Reinforcement_Learning_for_Autonomous_Driving_in_the_CARLA_Simulator)
*   [https://neurips.cc/virtual/2024/poster/95701](https://neurips.cc/virtual/2024/poster/95701)
*   [https://kclpure.kcl.ac.uk/ws/files/300373453/A_Review_of_Safe_Reinforcement_Learning_Methods_Theories_and_Applications_2_.pdf](https://kclpure.kcl.ac.uk/ws/files/300373453/A_Review_of_Safe_Reinforcement_Learning_Methods_Theories_and_Applications_2_.pdf)
*   [https://www.ijcai.org/proceedings/2025/0970.pdf](https://www.ijcai.org/proceedings/2025/0970.pdf)
*   [https://publications.tno.nl/publication/34644580/jYQDO8Ih/garg-2025-safe.pdf](https://publications.tno.nl/publication/34644580/jYQDO8Ih/garg-2025-safe.pdf)
*   [https://arxiv.org/abs/1705.10528](https://arxiv.org/abs/1705.10528)
*   [https://www.ambujtewari.com/stats701-winter2021/student%20presentation%20slides/Jang-Moug.pdf](https://www.ambujtewari.com/stats701-winter2021/student%20presentation%20slides/Jang-Moug.pdf)
*   [https://papers.neurips.cc/paper_files/paper/2022/file/9a8eb202c060b7d81f5889631cbcd47e-Paper-Conference.pdf](https://papers.neurips.cc/paper_files/paper/2022/file/9a8eb202c060b7d81f5889631cbcd47e-Paper-Conference.pdf)
*   [https://www.researchgate.net/publication/392134422_DISCOVER_Automated_Curricula_for_Sparse-Reward_Reinforcement_Learning](https://www.researchgate.net/publication/392134422_DISCOVER_Automated_Curricula_for_Sparse-Reward_Reinforcement_Learning)
*   [https://arxiv.org/abs/2505.19850](https://arxiv.org/abs/2505.19850)
*   [https://arxiv.org/html/2505.19850v2](https://arxiv.org/html/2505.19850v2)
*   [https://www.research-collection.ethz.ch/entities/publication/d877b41e-5bb0-45a2-8b78-d8e306a10745](https://www.research-collection.ethz.ch/entities/publication/d877b41e-5bb0-45a2-8b78-d8e306a10745)

## Citations 
- https://qspace.library.queensu.ca/bitstreams/aaae7d13-1a97-4010-b279-3f037c8fb741/download
- https://arxiv.org/html/2505.19850v1
- https://opendilab.github.io/DI-engine/02_algo/exploration_rl.html
- https://medium.com/data-scientists-diary/solving-the-exploration-exploitation-dilemma-in-reinforcement-learning-07b4c21e3d40
- https://intuitionlabs.ai/articles/reinforcement-learning-explained
- https://cdn.openai.com/safexp-short.pdf
- https://arxiv.org/abs/2402.02025
- https://research.tudelft.nl/files/124176896/Yang2022_Article_Safety_constrainedReinforcemen.pdf
- https://openreview.net/forum?id=dQLsvKNwZC&noteId=dkkof1UcOa
- https://proceedings.mlr.press/v202/wang23as/wang23as.pdf
- https://www.researchgate.net/publication/228631709_Intrinsic_motivation_for_reinforcement_learning_systems
- https://www.semanticscholar.org/paper/An-Evaluation-Study-of-Intrinsic-Motivation-applied-Andres-Villar-Rodriguez/1dc27caf3c3615028e5a4de536edf6eaf1073b0c
- https://tams.informatik.uni-hamburg.de/lehre/2018ws/seminar/ir/doc/slides/AntonWiehe-Exploration_RL.pdf
- https://ui.adsabs.harvard.edu/abs/2025arXiv250818420Q/abstract
- https://arxiv.org/html/2507.19725v1
- http://papers.neurips.cc/paper/8249-diversity-driven-exploration-strategy-for-deep-reinforcement-learning.pdf
- https://arxiv.org/html/2501.11533v1
- https://arxiv.org/pdf/2506.05980?
- https://www.semanticscholar.org/paper/Soft-Hindsight-Experience-Replay-He-Zhuang/6253a0f146a36663e908509e14648f8e2a5ab581
- https://openai.com/index/hindsight-experience-replay/
- https://liner.com/review/hindsight-experience-replay
- https://arxiv.org/abs/1707.01495
- https://arxiv.org/pdf/1707.01495
- https://di-engine-docs.readthedocs.io/en/latest/12_policies/sac.html
- https://www.geeksforgeeks.org/deep-learning/soft-actor-critic-reinforcement-learning-algorithm/
- http://bair.berkeley.edu/blog/2018/12/14/sac/
- https://arxiv.org/abs/1801.01290
- https://medium.com/@kdk199604/sac-a-soft-touch-to-efficient-reinforcement-learnings-c89acb1cb6b8
- https://www.researchgate.net/publication/323257379_Diversity_is_All_You_Need_Learning_Skills_without_a_Reward_Function
- https://www.slideshare.net/slideshow/diversity-is-all-you-needdiayn-learning-skills-without-a-reward-function/117168978
- https://towardsai.net/p/l/diayn-diversity-is-all-you-need
- https://sites.google.com/view/diayn/
- https://arxiv.org/abs/1802.06070
- https://www.researchgate.net/publication/395481976_Safe_Reinforcement_Learning_with_Constraints_A_Survey
- https://www.semanticscholar.org/paper/A-Survey-of-Safe-Reinforcement-Learning-and-MDPs%3A-A-Kushwaha-Ravish/79fa2130c55992691a0e7eb08e1d30c5b51ddef6
- https://www.ijcai.org/proceedings/2024/0913.pdf
- https://mosi.uni-saarland.de/assets/theses/ma_philipp_sauer.pdf
- https://openreview.net/revisions?id=3uNRbYM3qJ
- https://www.shcas.net/en/article/doi/10.3969/j.issn.1000-386x.2025.03.039
- https://openurl.ebsco.com/contentitem/doi:10.3390/computers14100434?sid=ebsco:plink:crawler&id=ebsco:doi:10.3390/computers14100434
- https://medium.com/biased-algorithms/curiosity-driven-exploration-in-reinforcement-learning-dd3f7d263fce
- https://dl.acm.org/doi/10.1145/3638529.3654045
- https://www.researchgate.net/publication/383777197_Constraints_Driven_Safe_Reinforcement_Learning_for_Autonomous_Driving_Decision-Making
- https://www.semanticscholar.org/paper/0999032fd68b8fe3fd8cc44d690aee4c5c8fed51
- https://www.ijmerr.com/2025/IJMERR-V14N3-347.pdf
- https://arxiv.org/abs/2011.04702
- https://arxiv.org/pdf/2506.22894
- https://www.researchgate.net/publication/395402495_A_Comprehensive_Review_of_Reinforcement_Learning_for_Autonomous_Driving_in_the_CARLA_Simulator
- https://neurips.cc/virtual/2024/poster/95701
- https://kclpure.kcl.ac.uk/ws/files/300373453/A_Review_of_Safe_Reinforcement_Learning_Methods_Theories_and_Applications_2_.pdf
- https://publications.tno.nl/publication/34644580/jYQDO8Ih/garg-2025-safe.pdf
- https://www.ijcai.org/proceedings/2025/0970.pdf
- https://www.researchgate.net/figure/DF-and-rewarding-impact-driven-exploration-RIDE-overview-In-IDF-the-features-are_fig3_360333045
- https://liner.com/review/ride-rewarding-impactdriven-exploration-for-procedurallygenerated-environments
- https://ai.meta.com/research/publications/ride-rewarding-impact-driven-exploration-for-procedurally-generated-environments/
- https://www.emergentmind.com/papers/2002.12292
- https://www.semanticscholar.org/paper/RIDE%3A-Rewarding-Impact-Driven-Exploration-for-Raileanu-Rockt%C3%A4schel/bebe8ffb0c357ac0c7eea2556f817b03ee22b570
- https://www.ambujtewari.com/stats701-winter2021/student%20presentation%20slides/Jang-Moug.pdf
- https://arxiv.org/abs/1705.10528
- https://arxiv.org/pdf/2510.17564?
- https://papers.neurips.cc/paper_files/paper/2022/file/9a8eb202c060b7d81f5889631cbcd47e-Paper-Conference.pdf
- https://openreview.net/forum?id=FdtdjQpAwJ
- https://www.researchgate.net/publication/392134422_DISCOVER_Automated_Curricula_for_Sparse-Reward_Reinforcement_Learning
- https://arxiv.org/abs/2505.19850
- https://arxiv.org/html/2505.19850v2
- https://www.research-collection.ethz.ch/entities/publication/d877b41e-5bb0-45a2-8b78-d8e306a10745
- https://www.themoonlight.io/en/review/discover-automated-curricula-for-sparse-reward-reinforcement-learning