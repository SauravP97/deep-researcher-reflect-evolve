# As an agricultural engineering researcher focusing on 3D reconstruction and phenotypic analysis of crop grains, please develop a design report utilizing modern control theory, alongside other relevant theoretical methods and models, for the tasks of modeling, analysis, and design pertinent to my research area.

# **Deep Research Report: A Modern Control-Theoretic Framework for 3D Reconstruction and Phenotypic Analysis of Crop Grains**

## Executive Summary
This report presents a comprehensive design framework for an automated system for the 3D reconstruction and phenotypic analysis of crop grains, leveraging principles from modern control theory. The central challenge in high-throughput phenotyping is the need for rapid, accurate, and robust data acquisition. Traditional static image processing workflows often lack the adaptability and formal guarantees of performance required for dynamic, real-world agricultural settings.

To address this, the proposed design formulates the 3D reconstruction process as an active vision problem governed by a dynamic control system. This novel approach enables a robotic imaging platform to intelligently decide "where to look next" to build a complete 3D model efficiently. The core of this report details a dual-methodology strategy to de-risk the project and provide a robust pathway for development:

1.  **Approach A: Analytical Modeling from First Principles:** This method seeks to derive a classic "white-box" state-space model of the system dynamics based on the geometric relationship between camera motion and image features, defined by the image Jacobian matrix. This approach offers deep theoretical insight and the potential for formal guarantees of system properties like observability and controllability.

2.  **Approach B: Data-Driven Modeling via State Representation Learning (SRL):** This powerful alternative bypasses the need for an explicit analytical model by learning the system's state and transition dynamics directly from image-to-action data. This "black-box" approach is particularly advantageous for uncalibrated systems and can offer superior robustness in complex environments.

The report details the design of a unified controller architecture, applicable to both models, that integrates Next-Best-View (NBV) planning for information gain with a visual servoing control law for precise motion. Safety constraints, such as keeping the grain within the camera's field-of-view, are formally guaranteed using Control Barrier Functions (CBFs). Finally, a simulation-based validation strategy using MATLAB/Simulink is outlined to quantitatively compare the performance of both modeling approaches, providing a clear basis for selecting the optimal strategy for physical implementation.

## 1.0 Introduction: Problem Formulation as a Dynamic Control System

High-throughput crop grain phenotyping requires the automated extraction of quantitative traits such as volume, surface area, and shape descriptors from individual grains. The foundation of this analysis is the acquisition of a high-fidelity 3D model of each grain. This report reconceptualizes this acquisition process, traditionally viewed as a static computer vision task, as a dynamic control problem.

The central hypothesis is that by modeling the interaction between a robotic sensor (e.g., a camera on a manipulator) and the object of interest (the grain), we can design an active vision system that is more efficient, robust, and automated than conventional methods. This involves creating a closed-loop system where visual feedback is used in real-time to control the camera's motion, intelligently guiding it to viewpoints that optimally contribute to the 3D reconstruction. This control-theoretic framework provides the mathematical tools to analyze system properties, design high-performance controllers, and formally guarantee safe and effective operation [https://journals.sagepub.com/doi/10.1177/0278364908096706].

## 2.0 System Architecture and Components

The proposed system is composed of a data acquisition front-end and a data processing back-end. The design of these components is critical for the overall performance of the phenotyping pipeline.

### 2.1 Data Acquisition: 3D Imaging Modalities

The choice of sensor modality directly dictates the quality and speed of data acquisition. A comparative analysis of suitable technologies for small-scale objects like crop grains reveals a trade-off between speed, resolution, and cost.

*   **Laser Triangulation:** This technique is identified as the optimal solution for high-speed, dynamic scanning environments, such as grains moving on a conveyor line. Its primary advantage is speed, making it ideal for high-throughput applications [https://www.automate.org/vision/tech-papers/structured-light-vs-laser-triangulation-for-3d-scanning-and-inspection].
*   **Structured Light:** These systems provide higher accuracy and resolution compared to other methods, making them well-suited for capturing fine surface details like crease depth or defects. This modality is recommended when the highest fidelity models are required, potentially at the cost of acquisition speed [https://www.ml6.eu/en/blog/optical-3d-acquisition-methods-a-comprehensive-guide-part-2].
*   **Multi-View Stereo (Photogrammetry):** A versatile and cost-effective method that offers a good balance of performance. It provides higher accuracy than Time-of-Flight sensors and is suitable for applications where real-time depth information is a priority [https://www.researchgate.net/publication/391519768_Advancements_and_Challenges_in_3D_Scanning_A_Comprehensive_Review_of_Engineering_Applications, https://www.ml6.eu/en/blog/optical-3d-acquisition-methods-a-comprehensive-guide-part-2].

### 2.2 System Output: Phenotypic State Variables

The ultimate goal of the system is to extract a set of morphometric and textural phenotypes from the reconstructed 3D models. These phenotypes serve as the system's measurable outputs. The process involves generating a 3D point cloud using a method like Structure-from-Motion (SfM), segmenting individual grains using algorithms such as the watershed method, and then computing critical phenotypes. These include, but are not limited to:
*   Length, width, and thickness
*   Volume
*   Surface area
*   Sphericity

Algorithms for calculating these traits from 3D point cloud or mesh data are well-established [https://www.researchgate.net/publication/354674020_Cereal_Grain_3D_Point_Cloud_Analysis_Method_For_Shape_Extraction_And_FilledUnfilled_Grain_Identification_Based_On_Structured_Light_Imaging, https://pubmed.ncbi.nlm.nih.gov/35210561/]. The accuracy of the final 3D model can be validated by measuring the Hausdorff distance between the raw point cloud data and the generated mesh [https://www.mdpi.com/2077-0472/14/3/391].

## 3.0 System Dynamics Modeling: A Dual-Methodology Approach

The core of the control-theoretic design is the creation of a mathematical model that describes the system's dynamics—how control inputs (camera velocity) affect the system's state (image features). A dual-methodology approach is proposed to develop and compare two distinct models.

### 3.1 Approach A: Analytical Modeling from First Principles

This approach aims to derive an explicit, "white-box" state-space model of the form `ẋ = f(x, u)`, where `x` is the state vector and `u` is the control input. This model is based on the principles of Image-Based Visual Servoing (IBVS).

The foundational kinematic relationship in IBVS is `ṡ = J(s, z)v_c`, where `ṡ` is the velocity of image features, `v_c` is the camera's velocity, and `J` is the image Jacobian (or interaction matrix) that maps camera motion to image feature motion [https://robotacademy.net.au/lesson/the-image-jacobian/]. The image Jacobian's analytical form depends on the feature's 3D spatial information (particularly depth, `z`), which is often unknown, posing a significant implementation challenge [https://arxiv.org/pdf/2210.10549].

**Finding:** While the research confirms the fundamental equation `ṡ = Jv_c` and describes methods for deriving the analytical Jacobian (e.g., using Green formulas [http://www.diag.uniroma1.it/deluca/rob2_en/17_VisualServoing.pdf]), a complete derivation of the nonlinear state-space dynamics `ẋ = f(x, u)` was not found in the provided source materials. The primary focus of existing literature is on the estimation of the Jacobian matrix itself.

### 3.2 Approach B: Data-Driven Modeling via State Representation Learning (SRL)

As a powerful alternative, SRL bypasses the challenges of analytical modeling. This "black-box" approach learns a model directly from data. The process involves two key components:
1.  **State Representation:** A model (e.g., a neural network) learns to build a compact state representation of the robot's configuration directly from camera images.
2.  **Transition Dynamics:** The system learns the transition dynamics from collected execution traces (sequences of images and actions), effectively modeling how an action transitions the system from one state to the next [https://www.merl.com/publications/docs/TR2025-094.pdf, https://www.mdpi.com/2075-1702/13/3/231].

This learned model can then be used to compute the control velocities needed to reach a desired goal state (also defined by an image). A major advantage of SRL is its ability to function effectively even with uncalibrated cameras, making it highly robust for practical applications [https://www.merl.com/publications/docs/TR2025-094.pdf].

## 4.0 System Analysis: Observability and Controllability

A key advantage of the analytical model (Approach A) is that it enables rigorous theoretical analysis of the system's fundamental properties.

*   **Observability:** Determines if the internal state of the system can be fully inferred from its outputs (the image features). In visual servoing, this can be interpreted as the ability to "observe" the unmeasurable state of feature depth (`Z`) from the image data [https://www.researchgate.net/publication/220121980_Feature_Depth_Observation_for_Image-based_Visual_Servoing_Theory_and_Experiments].
*   **Controllability:** Determines if the system can be driven from any initial state to any desired final state.

For nonlinear systems like visual servoing, this analysis is performed using tools from differential geometry. An observability matrix is constructed using **Lie derivatives**, and its rank determines the system's observability [https://www.mdpi.com/2227-7390/8/11/1876, https://www.researchgate.net/publication/338805605_Nonlinear_Observability_Analysis]. This analysis is a critical preliminary step in the design of state estimators like the Extended Kalman Filter and helps inform optimal sensor placement [https://math.stackexchange.com/questions/4459003/observability-of-non-linear-system-using-lie-derivative].

## 5.0 Controller Design Framework

A unified, multi-objective controller architecture is proposed, which can be implemented using either the analytical or the learned dynamics model.

### 5.1 Core Control Law: Visual Servoing

The fundamental control objective is to minimize the error `e(t) = s(t) - s*` in the image plane, where `s(t)` are the current image features and `s*` are the desired features. The controller computes the required camera velocity `v_c` based on the error dynamics and the (estimated or learned) image Jacobian to drive `e(t)` to zero [https://dellaert.github.io/21S-8803MM/Readings/L7%20Visual%20Servo%20Control.pdf].

### 5.2 Viewpoint Planning: Next-Best-View (NBV)

To ensure the 3D reconstruction is built efficiently, an NBV planner works in conjunction with the visual servoing controller. The NBV module's goal is to select the next viewpoint that maximizes information gain about the object's geometry. Two primary methods for this were identified:
*   **Probabilistic Volumetric Methods:** These methods use a volumetric map (e.g., voxels) and select the view that is predicted to resolve the most uncertainty, often quantified by entropy reduction [https://rpg.ifi.uzh.ch/docs/ICRA16_Isler.pdf, https://www.researchgate.net/publication/303719117_An_Information_Gain_Formulation_for_Active_Volumetric_3D_Reconstruction].
*   **Predictive Shape Completion Methods:** These advanced methods use a learned model (e.g., trained on a large shape dataset) to predict the object's complete geometry from a few initial views. The NBV planner then directs the camera to areas of high discrepancy between the current model and the predicted shape, leading to more intelligent exploration.

### 5.3 Safety Guarantees: Control Barrier Functions (CBFs)

To ensure robust operation, safety constraints must be formally enforced. A critical constraint is keeping the grain within the camera's limited field-of-view (FOV) to prevent tracking loss. **Control Barrier Functions (CBFs)** are an effective method for enforcing such safety constraints. The CBF is formulated as part of a real-time **Quadratic Program (QP)** that modifies the nominal control input (from the visual servoing law) in a minimal way to guarantee the system remains within a predefined safe set [https://mit-realm.github.io/nerf-cbf/, https://repository.lboro.ac.uk/articles/journal_contribution/CBF-based_hierarchical_quadratic_programs_with_guaranteed_feasibility_for_safety-critical_systems/30830948].

## 6.0 Implementation and Refinement

Practical implementation requires addressing model uncertainties and measurement noise for both modeling approaches.

### 6.1 Model Parameter Estimation (Approach A)

Since the analytical image Jacobian depends on unknown parameters (like feature depth), it must be estimated. Classical system identification techniques can be used for this purpose. Specifically, **Recursive Least Squares (RLS)** is a well-established method for estimating the Jacobian matrix from input-output data (previous robot motions and resulting sensor signals) ["https://www.academia.edu/28777782/Image_based_visual_servoing_Estimated_image_Jacobian_by_using_fundamental_matrix_VS_analytic_Jacobian"]. This allows for online adaptation of the model.

### 6.2 Real-Time State Estimation (Both Approaches)

Vision sensor measurements are inherently noisy. To obtain the best possible estimate of the system's state in real-time, filtering techniques are essential.
*   **Kalman Filters:** Are a powerful tool for 3D object tracking and can effectively handle challenges like minor occlusions [https://www.researchgate.net/publication/246598201_Kalman_Filter_for_vision_tracking, https://medium.com/@boukamchahamdi/how-to-create-a-kalman-filter-for-3d-object-tracking-c-6977fe5e1e91].
*   **Particle Filters:** Offer a robust alternative that can handle more complex, non-Gaussian dynamics and provide flexibility for different system models [https://pmc.ncbi.nlm.nih.gov/articles/PMC3663080/].

## 7.0 Simulation and Validation Strategy

A comparative simulation provides the primary means to validate and directly compare the two modeling and control methodologies before physical implementation. **MATLAB/Simulink** is identified as a suitable environment for this task.

The research indicates the availability of comprehensive resources, including a complete simulation model for a conveyor and robotic sorting system that can be adapted for this application [https://wiredwhite.com/matlab-simulink-conveyor-robotic-sorting-simulation/]. The simulation can be built using specialized toolboxes:
*   **Computer Vision Toolbox™:** For developing the automated visual inspection algorithms, including deep learning models (e.g., YOLOX) for feature detection.
*   **Machine Vision Toolbox (MVTB):** For implementing the vision-based control (visual servoing) loops.
*   **Simulink 3D Animation:** For visualizing the 3D motion and interaction of the robotic manipulator with the grain, providing crucial insights into dynamic performance.

The simulation will perform a direct comparison of the closed-loop systems resulting from Approach A (analytical) and Approach B (data-driven) based on key performance indicators: reconstruction accuracy, throughput (time to build a complete model), robustness to measurement noise, and computational load.

## 8.0 Conclusion and Outlook

This report has detailed a novel design framework for 3D crop grain phenotyping, grounded in the principles of modern control theory. The proposed dual-methodology approach, comparing an analytical first-principles model with a data-driven learned model, provides a comprehensive and de-risked strategy for development.

The primary trade-off between the two approaches is clear:
*   **Approach A (Analytical)** offers deep theoretical insight and the potential for formal proofs of system properties, but faces significant challenges in deriving and parameterizing an accurate model for real-world conditions.
*   **Approach B (Data-Driven)** provides a highly practical and potentially more robust alternative that can adapt to uncalibrated systems, at the cost of requiring large amounts of training data and offering less theoretical transparency.

The outlined simulation strategy will provide the quantitative evidence needed to evaluate these trade-offs and determine the superior modeling paradigm for this specific application. By framing the problem of 3D reconstruction within a control-theoretic context, this research direction promises to deliver more autonomous, efficient, and robust systems for next-generation agricultural phenotyping. Future work will focus on the development of hybrid models that combine the strengths of both approaches and the eventual implementation on a physical robotic platform.

## 9.0 References

A complete list of sources referenced in this report can be found in the aggregated research logs. The URLs have been provided inline throughout the document for direct access to the source material.

## Citations 
- https://cvpr.thecvf.com/virtual/2025/events/workshop
- https://www.mdpi.com/2227-9717/11/11/3171
- https://www.sciencedirect.com/science/article/abs/pii/S0926580512001690
- https://proceedings.neurips.cc/paper_files/paper/2024/file/0e5cce15e1bfc6b3d7b71f24cc5da821-Paper-Conference.pdf
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11014007/
- https://ai.meta.com/blog/sam-3d/
- https://arxiv.org/html/2505.10578v1
- https://www.researchgate.net/publication/391519768_Advancements_and_Challenges_in_3D_Scanning_A_Comprehensive_Review_of_Engineering_Applications
- https://www.automate.org/vision/tech-papers/structured-light-vs-laser-triangulation-for-3d-scanning-and-inspection
- https://www.ml6.eu/en/blog/optical-3d-acquisition-methods-a-comprehensive-guide-part-2
- https://www.researchgate.net/publication/354674020_Cereal_Grain_3D_Point_Cloud_Analysis_Method_For_Shape_Extraction_And_FilledUnfilled_Grain_Identification_Based_On_Structured_Light_Imaging
- https://pubmed.ncbi.nlm.nih.gov/35210561/
- https://ui.adsabs.harvard.edu/abs/2025EGUGA..2715463L/abstract
- https://esurf.copernicus.org/articles/10/1211/2022/
- https://www.mdpi.com/2077-0472/14/3/391
- https://pmc.ncbi.nlm.nih.gov/articles/PMC7973267/
- https://journals.sagepub.com/doi/10.1177/0278364911410755
- https://rovislab.com/papers/Gigi_RAAD_2011.pdf
- https://hal.science/hal-05397812v1/file/2025_ral_misimi.pdf
- https://www.researchgate.net/publication/220122397_Active_Vision_in_Robotic_Systems_A_Survey_of_Recent_Developments
- https://ras.papercept.net/conferences/conferences/ICRA25/program/ICRA25_ContentListWeb_1.html
- https://iclr.cc/virtual/2025/calendar
- https://css.paperplaza.net/conferences/conferences/ACC25/program/ACC25_ContentListWeb_3.html
- https://ras.papercept.net/conferences/conferences/ICRA25/program/ICRA25_ContentListWeb_2.html
- https://www.mdpi.com/2076-3417/12/12/6167
- https://www.sciencedirect.com/science/article/pii/S0947358025001414
- https://journals.sagepub.com/doi/10.1177/09596518211028379
- https://pmc.ncbi.nlm.nih.gov/articles/PMC3859066/
- https://journals.sagepub.com/doi/10.1177/0278364908096706
- https://commons.erau.edu/cgi/viewcontent.cgi?article=1017&context=edt
- https://www.researchgate.net/publication/220121980_Feature_Depth_Observation_for_Image-based_Visual_Servoing_Theory_and_Experiments
- https://open.clemson.edu/context/all_theses/article/4446/viewcontent/Allen_clemson_0050M_16045.pdf
- http://www.diag.uniroma1.it/deluca/rob2_en/17_VisualServoing.pdf
- https://www.mdpi.com/2227-7390/8/11/1876
- https://www.roebenack.de/observability
- https://www.researchgate.net/publication/338805605_Nonlinear_Observability_Analysis
- https://math.stackexchange.com/questions/4459003/observability-of-non-linear-system-using-lie-derivative
- https://www.researchgate.net/publication/318039789_An_efficient_method_to_compute_Lie_derivatives_and_the_observability_matrix_for_nonlinear_systems
- https://mit-realm.github.io/nerf-cbf/
- https://ras.papercept.net/conferences/conferences/IROS25/program/IROS25_ContentListWeb_1.html
- https://www.mdpi.com/2218-6581/14/12/190
- https://discovery.ucl.ac.uk/10209946/1/ICARM25_0172_FI.pdf
- https://ieeexplore.ieee.org/iel8/3516/4785241/11173962.pdf
- https://medium.com/@boukamchahamdi/how-to-create-a-kalman-filter-for-3d-object-tracking-c-6977fe5e1e91
- https://arxiv.org/abs/2506.01086
- https://www.researchgate.net/publication/246598201_Kalman_Filter_for_vision_tracking
- https://www.researchgate.net/publication/269723326_A_real-time_visual_object_tracking_system_based_on_Kalman_filter_and_MB-LBP_feature_matching
- https://pmc.ncbi.nlm.nih.gov/articles/PMC3663080/
- https://sir.upc.edu/projects/ris_tutorials/advanced/tutorialT4/tutorialT4.html
- https://wiredwhite.com/matlab-simulink-conveyor-robotic-sorting-simulation/
- https://www.mathworks.com/discovery/visual-inspection.html
- https://www.mathworks.com/help/simulink/slref/shape-tracing-manipulator-with-simulink-3d-animation.html
- https://www.mathworks.com/academia/students/tutorials-videos.html
- https://www.researchgate.net/publication/251919514_Image_Base_Visual_Servoing_Estimation_of_the_image_Jacobian_by_using_lines_in_a_stereo_vision_system
- https://www.sciencedirect.com/science/article/pii/S1000936124001961
- https://www.researchgate.net/publication/221472673_Image_Based_Visual_Servoing_A_New_Method_for_the_Estimation_of_the_Image_Jacobian_in_Dynamic_Environments
- https://www.sciencedirect.com/science/article/abs/pii/S0736584510000645
- https://www.sciencedirect.com/science/article/abs/pii/S0952197625017804
- https://github.com/kkkls/EVSSM
- https://www.merl.com/publications/docs/TR2025-094.pdf
- https://www.researchgate.net/publication/392941690_A_Survey_of_State_Representation_Learning_for_Deep_Reinforcement_Learning
- https://arxiv.org/abs/2506.17518
- https://www.merl.com/publications/docs/TR2025-094.pdf
- https://www.mdpi.com/2075-1702/13/3/231
- https://arxiv.org/html/2506.17518v1
- https://www.academia.edu/28777782/Image_based_visual_servoing_Estimated_image_Jacobian_by_using_fundamental_matrix_VS_analytic_Jacobian
- https://www.researchgate.net/publication/251919514_Image_Base_Visual_Servoing_Estimation_of_the_image_Jacobian_by_using_lines_in_a_stereo_vision_system
- https://www.researchgate.net/publication/224156371_Robust_Jacobian_Estimation_for_Uncalibrated_Visual_Servoing
- https://www.researchgate.net/publication/50991888_Image_Based_Visual_Servoing_Estimated_Image_Jacobian_by_Using_Fundamental_Matrix_VS_Analytic_Jacobian
- https://www.wseas.us/e-library/conferences/2008/uk/ISPRA/ispra-06.pdf
- https://hal.science/hal-05397812v1/file/2025_ral_misimi.pdf
- https://pure.au.dk/portal/en/publications/active-3d-vision-for-robotic-manufacturing-enhancement-2/
- https://www.researchgate.net/publication/398474354_Visual_Servoing-Based_Active_Vision_for_3D_Object_Reconstruction
- https://ptacts.uspto.gov/ptacts/public-informations/petitions/1556121/download-documents?artifactId=Phj3iN3WLQmtcvzGL-641aTlmr-_eu56erYw6XPWzf_VQxmhZWvnQxo
- https://www.researchgate.net/publication/221472673_Image_Based_Visual_Servoing_A_New_Method_for_the_Estimation_of_the_Image_Jacobian_in_Dynamic_Environments
- https://ui.adsabs.harvard.edu/abs/2017IRAL....2..912T/abstract
- https://robotacademy.net.au/lesson/the-image-jacobian/
- https://www.youtube.com/watch?v=XDE6oxEJn3c
- https://inria.hal.science/inria-00436722v1/document
- https://ecai2025.org/accepted-papers/
- https://css.paperplaza.net/conferences/conferences/ACC25/program/ACC25_ContentListWeb_3.html
- https://www.mdpi.com/1424-8220/25/18/5748
- https://openreview.net/pdf/47e4f7aed1fadec7617b0314d78968366b8e661d.pdf
- https://dl.acm.org/doi/10.1109/ICRA.2016.7487527
- https://www.researchgate.net/publication/303719117_An_Information_Gain_Formulation_for_Active_Volumetric_3D_Reconstruction
- https://www.mdpi.com/2072-4292/11/20/2440
- https://rpg.ifi.uzh.ch/docs/ICRA16_Isler.pdf
- https://hal.science/hal-03086499/file/HaMoMoMaMo_IROS20.pdf
- https://ieeexplore.ieee.org/ielaam/7083369/7875382/7835670-aam.pdf
- https://dl.acm.org/doi/10.5555/1732643.1732707
- https://openaccess.thecvf.com/content/CVPR2024/papers/Chen_GenNBV_Generalizable_Next-Best-View_Policy_for_Active_3D_Reconstruction_CVPR_2024_paper.pdf
- https://www.researchgate.net/publication/220887545_Next-Best-View_Planning_for_3D_Object_Reconstruction_under_Positioning_Error
- https://par.nsf.gov/servlets/purl/10489772
- https://mediatum.ub.tum.de/doc/1344440/18465862505.pdf
- https://open.clemson.edu/context/all_theses/article/4446/viewcontent/Allen_clemson_0050M_16045.pdf
- https://www.tandfonline.com/doi/full/10.1080/15599610802303579
- https://dellaert.github.io/21S-8803MM/Readings/L7%20Visual%20Servo%20Control.pdf
- https://www.sciencedirect.com/science/article/abs/pii/S0045790619319159
- https://www.merl.com/publications/docs/TR2025-094.pdf
- https://dellaert.github.io/21S-8803MM/Readings/L7%20Visual%20Servo%20Control.pdf
- https://peerj.com/articles/cs-2559/
- https://pure-oai.bham.ac.uk/ws/files/150739566/09596518211028379.pdf
- https://journals.sagepub.com/doi/10.1177/17298814211016674
- https://arxiv.org/abs/2502.08129
- https://www.researchgate.net/publication/372131019_Enforcing_safety_for_vision-based_controllers_via_Control_Barrier_Functions_and_Neural_Radiance_Fields
- https://ui.adsabs.harvard.edu/abs/2016arXiv160906408A/abstract
- https://www.sciencedirect.com/science/article/pii/S0921889024001970
- https://repository.lboro.ac.uk/articles/journal_contribution/CBF-based_hierarchical_quadratic_programs_with_guaranteed_feasibility_for_safety-critical_systems/30830948
- https://mediatum.ub.tum.de/doc/1344440/18465862505.pdf
- https://www.researchgate.net/publication/221472673_Image_Based_Visual_Servoing_A_New_Method_for_the_Estimation_of_the_Image_Jacobian_in_Dynamic_Environments
- https://open.clemson.edu/context/all_theses/article/4446/viewcontent/Allen_clemson_0050M_16045.pdf
- https://discoveryjournals.org/engineering/current_issue/2023/v20/n54/e36ije1672.pdf
- https://robotacademy.net.au/lesson/image-based-visual-servoing/
- https://www.researchgate.net/publication/221472673_Image_Based_Visual_Servoing_A_New_Method_for_the_Estimation_of_the_Image_Jacobian_in_Dynamic_Environments
- https://arxiv.org/pdf/2211.11178
- https://automaticaddison.com/how-to-derive-the-state-space-model-for-a-mobile-robot/
- https://www.sciencedirect.com/science/article/abs/pii/S0736584510000645
- https://limbs.lcsr.jhu.edu/wp-content/uploads/2013/05/Cowangeometric2005.pdf
- http://culturetechlab.culture.upatras.gr/sites/default/files/downloads/rcim_10.pdf
- https://inria.hal.science/hal-00920414v1/document
- http://vigir.missouri.edu/~gdesouza/Research/Conference_CDs/IEEE_ICRA_2010/data/papers/1516.pdf
- https://upcommons.upc.edu/bitstreams/92045008-a559-4768-bc3a-af61db602443/download
- https://faculty.cc.gatech.edu/~seth/ResPages/pdfs/HutHagCor96.pdf
- http://www.diag.uniroma1.it/deluca/rob2_en/17_VisualServoing.pdf
- https://visp-doc.inria.fr/manual/visp-2.6.1-tutorial-visual-servoing.pdf
- https://inria.hal.science/hal-01010470/PDF/Visual_Servoing.pdf
- https://www.academia.edu/28777782/Image_based_visual_servoing_Estimated_image_Jacobian_by_using_fundamental_matrix_VS_analytic_Jacobian
- http://www.diag.uniroma1.it/deluca/rob2_en/17_VisualServoing.pdf
- http://culturetechlab.culture.upatras.gr/sites/default/files/downloads/rcim_10.pdf
- https://arxiv.org/html/2405.18830v1
- https://arxiv.org/pdf/2210.10549
- https://siyuxu.com/cv-arxiv-daily/