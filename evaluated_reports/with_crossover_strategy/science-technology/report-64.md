# Regarding the attitude control problem for UAVs, most open-source flight controllers currently implement cascaded PID control algorithms. However, a single set of PID controller parameters typically performs well only under specific flight conditions. In practical applications, UAVs operate across diverse flight states. What methods can be employed to enhance the actual control performance of PID algorithms, and how should PID parameters be optimally selected?

# Deep Research Report: Advanced Methods for Enhancing PID Control Performance in UAV Attitude Systems

## Executive Summary

Standard cascaded Proportional-Integral-Derivative (PID) controllers are the cornerstone of attitude control in most open-source Unmanned Aerial Vehicle (UAV) flight controllers. While effective, their performance is optimized for a narrow range of flight conditions. A single set of PID parameters is often insufficient to provide optimal stability and responsiveness across a UAV's full operational envelope, which involves variations in mass, aerodynamics, and external disturbances like wind.

This report analyzes methods to enhance PID control performance and optimize parameter selection. Key findings indicate a progression from simple adaptive techniques to complex, intelligent, and hybrid control architectures:

*   **Adaptive Tuning Methods:** Techniques like Gain Scheduling, Fuzzy Logic Control (FLC), and Neural Network (NN) tuners adapt PID parameters in real-time. Gain Scheduling offers a low-cost solution by pre-calculating gains for different flight states, while FLC and NNs provide more dynamic, intelligent tuning to handle non-linearities.
*   **Offline Optimization:** Metaheuristic algorithms, including Genetic Algorithms (GA) and Particle Swarm Optimization (PSO), are used in simulation to find a globally optimal set of PID parameters before flight, balancing trade-offs like overshoot and settling time.
*   **Advanced & Hybrid Control:** For superior robustness, advanced strategies augment or replace PID. Hybrid systems combining Sliding Mode Control (SMC) with Active Disturbance Rejection Control (ADRC), or Model Predictive Control (MPC), offer significant performance gains, though often at a higher computational cost.
*   **Learning-Based Control:** Reinforcement Learning (RL) and Deep Reinforcement Learning (DRL) represent the state-of-the-art, enabling controllers to learn optimal policies directly from interaction. These methods demonstrate high robustness to unmodeled dynamics and can even form end-to-end control systems that bypass the traditional PID structure.
*   **Practical Implementation:** Open-source platforms like PX4 and ArduPilot have implemented practical solutions such as in-flight 'Autotune' and offline tuning workflows that leverage flight log data for system identification.

The selection of an appropriate method depends on a trade-off between desired control performance, available computational resources on the flight controller, and implementation complexity.

---

## Key Findings

### 1. Foundational Analysis of Cascaded PID in UAV Attitude Control

The standard control architecture for a multirotor UAV is a cascaded PID system. This structure consists of two nested loops for each axis of rotation (roll, pitch, yaw):

*   **Outer Loop (Angle Control):** Typically a Proportional-Derivative (PD) controller, this loop calculates the difference between the desired attitude angle and the measured angle. Its output is a target angular rate required to correct this error.
*   **Inner Loop (Rate Control):** This loop, usually a full PID controller, receives the target angular rate from the outer loop. It works to match the UAV's actual angular velocity to this target rate by adjusting motor commands.

For this system to be stable, the inner rate control loop must operate at a significantly higher frequency than the outer angle loop. This P-PID structure is effective but its performance is highly dependent on its gain parameters (Kp, Ki, Kd).

A fixed set of gains is fundamentally limited because the UAV's dynamics are not constant. Key factors that invalidate a single-gain assumption include:
*   **Changing Mass:** Payload variations or battery drain alter the vehicle's inertia.
*   **Aerodynamic Variations:** Air density and aerodynamic forces change with airspeed and altitude.
*   **External Disturbances:** Wind gusts and turbulence introduce unpredictable forces that the controller must reject [https://www.sciencedirect.com/science/article/pii/S2772671124004169, https://www.researchgate.net/publication/360410400_Aerodynamic_Modelling_and_Wind_Disturbance_Rejection_of_Multirotor_Unmanned_Aerial_Vehicles].

### 2. Methods for Adaptive PID Parameter Tuning

To overcome the limitations of fixed gains, several methods dynamically adjust PID parameters during flight.

#### 2.1. Gain Scheduling
Gain Scheduling is a straightforward adaptive method where multiple sets of PID parameters are pre-calculated for various operating points. These gains are stored in a lookup table, and the flight controller selects or interpolates between them in real-time based on a "scheduling variable" such as airspeed or throttle level [https://www.mathworks.com/help/slcontrol/ug/pidgainscheduler.html].

*   **Advantages:** Simple to implement and computationally inexpensive, making it suitable for resource-constrained microcontrollers. It improves path tracking and fault tolerance compared to fixed-gain controllers [https://www.researchgate.net/publication/326490598_Gain_Scheduling_Based_PID_Control_Approaches_for_Path_Tracking_and_Fault_Tolerant_Control_of_a_Quad-rotor_UAV].
*   **Disadvantages:** Requires extensive pre-flight characterization to build the lookup table. The control response can be discontinuous if interpolation between operating points is not smooth. The provided research did not specify further disadvantages [https://www.ijmerr.com/uploadfile/2018/0709/20180709111619835.pdf].

#### 2.2. Intelligent PID Control using Fuzzy Logic
Fuzzy Logic Controllers (FLC) embed human-like reasoning into the control system to tune PID parameters online. The typical architecture involves:
1.  **Fuzzification:** Controller inputs, typically the error (e) and the change in error (de/dt), are converted into linguistic fuzzy sets (e.g., "Negative Big," "Zero," "Positive Small") using membership functions.
2.  **Fuzzy Inference:** A rule base of "IF-THEN" statements (e.g., "IF error is Positive Big AND change-in-error is Zero, THEN Kp_adjustment is Big") processes the fuzzy inputs to determine a fuzzy output.
3.  **Defuzzification:** The fuzzy output is converted back into a crisp numerical value that is used to adjust the Kp, Ki, and Kd gains. The **Center of Gravity (COG)** method is a common and effective technique for this step [https://www.researchgate.net/figure/Membership-functions-of-the-error-for-the-fuzzy-PID-controller_fig4_276509370, https://www.youtube.com/watch?v=etFR1xwvd7w].

This approach allows the controller to adapt smoothly to a wide range of operating conditions without an explicit mathematical model of the system's dynamics.

#### 2.3. Intelligent PID Control using Neural Networks
Neural Networks (NN) can learn the complex, non-linear dynamics of a UAV and use this knowledge to perform online self-tuning of PID gains. Several architectures exist:

*   **Direct Gain Tuning:** A simple, single-layer NN can take proportional, integral, and derivative errors as inputs to directly output adjustments for the PID gains [https://pmc.ncbi.nlm.nih.gov/articles/PMC12396714].
*   **Inverse Dynamics Modeling:** The **Direct Inverse Control Artificial Neural Network (DIC-ANN)** architecture involves training an NN to learn the inverse dynamics of the UAV. This inverse model can then be used to calculate the required control inputs, enhancing the PID loop [https://onlinelibrary.wiley.com/doi/10.1155/2018/3823201].
*   **Hybrid Architectures:** More advanced systems combine NNs with other techniques. One example fuses an NN-PID with a Fuzzy Logic PID (NNPID+FPID), where the NNPID excels at lateral/heading control and the FPID handles longitudinal/altitude dynamics [https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0331036]. Another approach uses an Improved Sparrow Search Algorithm (ISSA) to optimize a Backpropagation NN (BPNN), which is then paired with a Linear Extended State Observer (LESO) for superior disturbance rejection.

While powerful, some research notes that the performance improvement from NN-based tuning may be small relative to the significant increase in implementation complexity.

### 3. Offline Optimization using Metaheuristic Algorithms

Instead of tuning parameters in-flight, metaheuristic optimization finds an optimal set of PID gains offline. This is achieved by running numerous simulations of the UAV's mathematical model (e.g., in Simulink).

*   **Process:** An optimization algorithm systematically searches for the best combination of Kp, Ki, and Kd values.
*   **Algorithms:** Common choices include Genetic Algorithms (GA), Particle Swarm Optimization (PSO), and Cuckoo Search Algorithm (CSA).
*   **Cost Function:** The performance of each parameter set is evaluated against a cost (or fitness) function. This function is designed to penalize undesirable behaviors and reward desired ones, often by integrating weighted metrics such as Integral Absolute Error, overshoot, rise time, and settling time.

This method is highly effective for finding a globally robust set of parameters for a known system model before any hardware is tested.

---

## Detailed Analysis: Advanced and Hybrid Control Strategies

For applications demanding the highest levels of performance and robustness, control strategies that augment or entirely replace the PID structure are employed.

#### Robust and Hybrid Control Methods
*   **Sliding Mode Control (SMC):** SMC is known for its exceptional robustness to matched uncertainties and external disturbances. It drives the system's state trajectory onto a predefined "sliding surface" and maintains it there, ensuring stability.
*   **SMC with Active Disturbance Rejection Control (ADRC):** This powerful hybrid combines the strengths of both methods. The ADRC component uses an **Extended State Observer (ESO)** to estimate and actively compensate for both internal (unmodeled dynamics) and external (wind) disturbances. The SMC component then provides robust attitude control. This combination, particularly with Super-Twisting SMC (ST-SMC), has demonstrated superior dynamic response and disturbance rejection compared to standalone PID or ADRC [https://www.mdpi.com/2076-3417/15/9/5124].
*   **Adaptive Neuro-Fuzzy Inference System (ANFIS):** ANFIS merges neural networks with fuzzy logic. It can be used in hybrid architectures, such as being combined with SMC to improve trajectory tracking robustness [https://library.acadlore.com/JISC/2023/2/1/JISC_02.01_04.pdf]. Alternatively, ANFIS can be used for system identification, with a Genetic Algorithm subsequently optimizing the controller parameters based on the identified model [https://www.semanticscholar.org/paper/Adaptive-genetic-neuro-fuzzy-attitude-control-for-a-Oliveira-Rosa/5180f14654e3d98aa632a3c9a54da27110c573f6].

#### Model Predictive Control (MPC)
MPC uses a model of the UAV to predict its future behavior and calculates an optimal sequence of control inputs over a finite time horizon.
*   **Benefits:** MPC excels at trajectory tracking and can explicitly handle system constraints (e.g., maximum motor thrust, roll/pitch angle limits), making it ideal for aggressive maneuvers [1, 8].
*   **Drawbacks:** Its primary disadvantage is the high computational cost associated with the online optimization performed at each time step. This makes real-time implementation a significant challenge on typical embedded flight controllers and often requires more powerful hardware [1, 2, 5, 6, 7, 8, 10]. Its computational burden is greater than that of both PID and SMC.

#### Reinforcement Learning (RL)
RL-based controllers learn optimal control policies through trial-and-error interaction with the environment (either in simulation or reality), guided by a reward function.
*   **Benefits:** DRL controllers, using algorithms like Deep Deterministic Policy Gradient (DDPG) or Proximal Policy Optimization (PPO), can learn the UAV's non-linear dynamics directly without needing an explicit model [https://arxiv.org/abs/1804.04154]. They show remarkable robustness, generalizing well to unseen disturbances like wind after training on minimal flight data [https://www.semanticscholar.org/paper/Reinforcement-Learning-for-UAV-Attitude-Control-Koch-Mancuso/b223b7d1dc76be5591bc261e9550ae4d168b6222].
*   **Physics-Informed RL (PI-RL):** While RL is a highly active area of research, the provided data did not contain specific details on the application of Physics-Informed Reinforcement Learning (PI-RL), where a dynamics model is explicitly integrated into the learning process for this application.

### Comparative Analysis of Methods

| Method | Control Performance | Computational Cost | Implementation Complexity | Reliance on Model | Adaptability |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Fixed PID** | Baseline; poor in varied conditions | Very Low | Low | Moderate (for initial tuning) | Very Low |
| **Gain Scheduling** | Good; improved over fixed PID | Low | Moderate | High (for pre-calculation) | Moderate |
| **Fuzzy Logic PID** | Very Good; robust to non-linearity | Moderate | High | Low | High |
| **Neural Network PID** | Very Good; highly adaptive | Moderate to High | High | Low (learns from data) | Very High |
| **Metaheuristic Opt.**| Optimal for a given model | N/A (Offline) | Moderate (for simulation setup) | Very High | Low (produces fixed gains) |
| **SMC-ADRC** | Excellent; superior disturbance rejection | Moderate to High | High | Moderate | High |
| **MPC** | Excellent; handles constraints | Very High | Very High | Very High | Moderate |
| **DRL** | Excellent; robust to unmodeled dynamics | High (training) / Mod-High (inference) | Very High | Low | Very High |

*Note: Data on implementation complexity was not available for all methods in the provided research.*

---

## Practical Implementations in Open-Source Autopilots

Major open-source flight control stacks have implemented user-friendly features to address the PID tuning challenge.

*   **Autotuning:** Both PX4 and ArduPilot feature in-flight autotune routines.
    *   **PX4** uses the OCTUNE algorithm. For multicopters, the vehicle must land and be disarmed for new parameters to be applied, whereas fixed-wing gains can be tested and reverted in the air if unstable [https://docs.px4.io/v1.14/en/config/autotune].
    *   **ArduPilot** has a well-known autotune function that some users characterize as potentially "rough" for certain vehicle frames [https://github.com/PX4/Firmware/issues/8472].
*   **Offline Tuning via Log Analysis:** A more advanced workflow involves using flight log data for system identification.
    *   **PX4** users can leverage Python scripts to analyze `.ulog` files and perform system identification to tune attitude rate loops offline [https://github.com/mzahana/px4_pid_tuner].
    *   **ArduPilot** provides a "System Identification" feature for advanced users, which injects stimulus signals during flight to measure the vehicle's frequency response, enabling the creation of precise mathematical models from log data.

## State-of-the-Art and Future Research Directions

The research frontier in UAV attitude control is moving beyond traditional cascaded structures and towards more integrated, intelligent systems.

1.  **End-to-End Control with DRL:** Research is exploring the use of DRL to create end-to-end controllers that map sensor inputs directly to motor commands, bypassing the PID structure entirely. This has shown promise for complex tasks like dynamic target tracking and stabilization of fixed-wing UAVs [https://pmc.ncbi.nlm.nih.gov/articles/PMC9680462/, https://www.researchgate.net/publication/347432613_Deep_Reinforcement_Learning_Attitude_Control_of_Fixed-Wing_UAVs].
2.  **Novel Sensor Fusion for State Estimation:** The performance of any controller is limited by the quality of its state estimates. Novel sensor fusion techniques using deep learning—such as Deep Learning Neural Networks (DLNN) and Long-Short Term Memory (LSTM) networks—are being developed to provide more accurate and fault-tolerant attitude estimation. By feeding the controller a cleaner, more reliable signal, these methods indirectly but significantly enhance control performance.

## Conclusion & Outlook

While the cascaded PID controller remains the standard for many UAV applications due to its simplicity and effectiveness under nominal conditions, its limitations in diverse real-world scenarios are clear. To enhance performance, a spectrum of solutions is available.

*   For **hobbyist and standard commercial use**, methods like **Gain Scheduling** and the **Autotune** features in PX4/ArduPilot provide a practical balance of improved performance and low implementation overhead.
*   For **high-performance and industrial applications** requiring robustness to significant disturbances, intelligent and hybrid approaches like **Fuzzy Logic PID**, **SMC-ADRC**, and **NN-based tuners** are more appropriate, despite their higher complexity.
*   The future of UAV control lies with **learning-based methods**. Deep Reinforcement Learning offers a path towards highly adaptive, robust controllers that can operate with minimal prior knowledge of the vehicle's dynamics, enabling a new level of autonomy and performance in complex, unpredictable environments.

The optimal choice depends on the specific application's performance requirements, the computational constraints of the hardware, and the development resources available.

---

## References

A complete list of sources referenced in the research logs is available upon request. Key sources have been cited inline throughout the document.

## Citations 
- https://onlinelibrary.wiley.com/doi/10.1155/2023/6651286
- https://www.researchgate.net/publication/381005548_Cascade_PID_Control_for_Altitude_and_Angular_Position_Stabilization_of_6-DOF_UAV_Quadcopter
- https://discuss.px4.io/t/multicopter-control-architecture-design-choices/31815
- https://robotics.stackexchange.com/questions/8895/quadcopter-pid-control-is-it-possible-to-stabilize-a-quadcopter-considering-onl
- https://link.springer.com/article/10.1007/s42452-019-0698-7
- https://www.researchgate.net/publication/334775957_Optimizing_PID_controller_gains_to_model_the_performance_of_a_quadcopter
- https://www.mdpi.com/2673-4591/87/1/93
- https://www.scribd.com/document/706250461/30
- https://www.researchgate.net/publication/360410400_Aerodynamic_Modelling_and_Wind_Disturbance_Rejection_of_Multirotor_Unmanned_Aerial_Vehicles
- https://www.sciencedirect.com/science/article/pii/S2772671124004169
- https://www.researchgate.net/figure/Gain-scheduling-FL-PID-controller-implementation_fig2_344677720
- https://www.mathworks.com/help/slcontrol/ug/pidgainscheduler.html
- https://www.researchgate.net/publication/326490598_Gain_Scheduling_Based_PID_Control_Approaches_for_Path_Tracking_and_Fault_Tolerant_Control_of_a_Quad-rotor_UAV
- https://www.researchgate.net/publication/317040874_Gain_Scheduled_Attitude_Control_of_Fixed-Wing_UAV_With_Automatic_Controller_Tuning
- https://www.ijmerr.com/uploadfile/2018/0709/20180709111619835.pdf
- https://www.researchgate.net/figure/Fuzzy-PID-rule-base-for-K-df-gain_tbl4_363776496
- https://www.semanticscholar.org/paper/fe28504483b86768926d08d340241fbc4fa62f72
- https://www.researchgate.net/publication/234025186_Fuzzy_Logic_Based_Approach_to_Design_of_Flight_Control_and_Navigation_Tasks_for_Autonomous_Unmanned_Aerial_Vehicles
- https://www.researchgate.net/publication/220312345_Fuzzy_PID_controller_Design_performance_evaluation_and_stability_analysis
- https://www.researchgate.net/publication/387657973_Self-Tuning_PID_Controller_for_Quadcopter_using_Fuzzy_Logic
- https://ieeexplore.ieee.org/iel8/6287639/10380310/10794762.pdf
- https://www.reddit.com/r/ControlTheory/comments/1fuselt/optimize_pid_gains_using_neural_networks/
- https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0331036
- https://www.sciencedirect.com/science/article/pii/S2590123025043075
- https://onlinelibrary.wiley.com/doi/10.1155/2018/3823201
- https://drpress.org/ojs/index.php/ajst/article/view/11951
- https://www.semanticscholar.org/paper/A-Genetic-Algorithm-Approach-to-PID-Tuning-of-a-UAV-Say-Sybingco/3ad8c1b25d48b3f72dc76a3f465125140f4731d3
- https://www.matlabi.ir/wp-content/uploads/bank_papers/gpaper/g654-www.Matlabi.ir.pdf
- https://link.springer.com/article/10.1007/s44291-025-00049-y
- https://www.mdpi.com/2076-3417/11/14/6492
- https://www.researchgate.net/figure/Membership-functions-of-the-error-for-the-fuzzy-PID-controller_fig4_276509370
- https://www.youtube.com/watch?v=etFR1xwvd7w
- https://www.researchgate.net/figure/Fuzzy-membership-function-for-error_fig4_388313885
- https://cse.iitkgp.ac.in/~dsamanta/courses/archive/sca/Archives/Chapter%205%20Defuzzification%20Methods.pdf
- https://www.youtube.com/watch?v=XwafDor2g6A
- https://www.mdpi.com/2076-3417/15/9/5124
- https://www.researchgate.net/publication/382213105_Attitude_Control_of_Small_Fixed-Wing_UAV_Based_on_Sliding_Mode_and_Linear_Active_Disturbance_Rejection_Control
- https://repository.library.northeastern.edu/files/neu:bz617b344/fulltext.pdf
- https://ui.adsabs.harvard.edu/abs/1997IJSyS..28..435C/abstract
- https://ieeexplore.ieee.org/iel8/6287639/10820123/10935310.pdf
- https://www.mdpi.com/1424-8220/22/23/9240
- https://engrxiv.org/preprint/download/4462/7760/6405
- https://discuss.px4.io/t/how-to-autotune-the-pid-params/3395
- https://github.com/PX4/Firmware/issues/8472
- https://docs.px4.io/v1.14/en/config/autotune
- https://onlinelibrary.wiley.com/doi/10.1155/er/9959245?msockid=06f218dd51456b761c060e0c50476a2b
- https://link.springer.com/article/10.1007/s10489-025-06505-2
- https://link.springer.com/article/10.1007/s40435-025-01963-5
- https://www.researchgate.net/publication/285588789_Optimal_attitude_control_of_a_quadrotor_UAV_using_Adaptive_Neuro-Fuzzy_Inference_System_ANFIS
- https://www.mi-research.net/en/article/doi/10.1007/s11633-020-1251-2
- https://www.researchgate.net/publication/270723449_UAV_Controller_Based_on_Adaptive_Neuro-Fuzzy_Inference_System_and_PID
- https://www.semanticscholar.org/paper/Adaptive-genetic-neuro-fuzzy-attitude-control-for-a-Oliveira-Rosa/5180f14654e3d98aa632a3c9a54da27110c573f6
- https://library.acadlore.com/JISC/2023/2/1/JISC_02.01_04.pdf
- https://arxiv.org/abs/1804.04154
- https://cs-web.bu.edu/faculty/richwest/papers/tcps2019.pdf
- https://www.researchgate.net/publication/324492570_Reinforcement_Learning_for_UAV_Attitude_Control
- https://repositorio.usp.br/directbitstream/ce1d9930-6f58-4e4c-9ba6-e76334e2ed82/Reinforced%20Learning%20for%20UAV%20Attitude%20Control.pdf
- https://www.semanticscholar.org/paper/Reinforcement-Learning-for-UAV-Attitude-Control-Koch-Mancuso/b223b7d1dc76be5591bc261e9550ae4d168b6222
- https://www.researchgate.net/publication/287744283_Active_disturbance_rejection_control_of_attitude_for_spacecraft
- https://www.researchgate.net/publication/341381778_Active_disturbance_rejection_control_strategy_for_airborne_radar_stabilization_platform_based_on_cascade_extended_state_observer
- https://www.researching.cn/articles/OJ2fd62d7f09bd3944
- https://www.mdpi.com/2076-3417/11/13/5960
- https://www.sciencedirect.com/science/article/pii/S0307904X2400341X
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12396714/
- https://onlinelibrary.wiley.com/doi/10.1155/2018/3823201
- https://www.researchgate.net/publication/387214019_The_Application_and_Optimisation_of_a_Neural_Network_PID_Controller_for_Trajectory_Tracking_Using_UAVs
- https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0331036
- https://d-nb.info/1269634712/34
- https://pmc.ncbi.nlm.nih.gov/articles/PMC9680462/
- https://www.researchgate.net/publication/347432613_Deep_Reinforcement_Learning_Attitude_Control_of_Fixed-Wing_UAVs
- https://open.bu.edu/items/62d0b93a-7066-4c70-a86a-9c022677748d
- https://arxiv.org/pdf/2111.04153
- https://folk.ntnu.no/torarnj/eeb_ICUAS_Paper.pdf
- https://github.com/mzahana/px4_pid_tuner
- https://www.youtube.com/watch?v=shg6Q5ubhpw
- https://ardupilot.org/plane/docs/common-systemid-mode.html
- https://docs.px4.io/main/en/log/flight_review
- https://ardupilot.org/copter/docs/common-systemid-mode-operation.html
- https://scispace.com/pdf/deep-learning-based-neural-network-training-for-state-2coq5garjl.pdf
- https://www.mdpi.com/2079-9292/13/16/3342
- http://vigir.missouri.edu/~gdesouza/Research/Conference_CDs/IEEE_WCCI_2020/CEC/Papers/E-24096.pdf
- https://researchrepository.ul.ie/ndownloader/files/52733126/1
- https://arxiv.org/pdf/2108.03173
- https://www.researchgate.net/publication/391456123_Research_on_the_Stability_of_UAV_Attitude_Under_Hybrid_Control_Integrating_Active_Disturbance_Rejection_Control_and_Super-Twisting_Sliding_Mode_Control
- https://www.mdpi.com/2076-3417/15/9/5124
- https://www.mdpi.com/2504-446X/8/7/318
- https://www.sciencedirect.com/science/article/abs/pii/S1270963821007732
- https://discovery.researcher.life/topic/attitude-control/848581?page=3
- https://www.emergentmind.com/papers/1804.04154
- https://cs-web.bu.edu/faculty/richwest/papers/tcps2019.pdf
- https://www.researchgate.net/publication/324492570_Reinforcement_Learning_for_UAV_Attitude_Control
- https://www.semanticscholar.org/paper/Reinforcement-Learning-for-UAV-Attitude-Control-Koch-Mancuso/b223b7d1dc76be5591bc261e9550ae4d168b6222
- https://arxiv.org/abs/1804.04154