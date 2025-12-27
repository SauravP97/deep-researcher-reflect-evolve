# How to conduct comprehensive and accurate situational awareness of space targets in the cislunar space, and support the effectiveness of short-term cislunar space tracking and monitoring tasks?

# Deep Research Report: Achieving Comprehensive Situational Awareness in Cislunar Space

## Executive Summary

The cislunar domain—the vast region of space between Earth's geosynchronous orbit and the Moon—is rapidly evolving from a quiet frontier into a strategic and commercially active environment. Driven by government initiatives like NASA's Artemis program and the Chinese Lunar Exploration Program, alongside a growing number of commercial ventures, the population of spacecraft, rocket bodies, and debris in this region is set to increase dramatically. This report analyzes the multifaceted challenge of conducting comprehensive and accurate Space Situational Awareness (SSA) in this unique domain to support the effectiveness of short-term tracking and monitoring tasks.

Achieving robust cislunar SSA requires a fundamental departure from the methods used for Low Earth Orbit (LEO) and Geosynchronous (GEO) regions. The primary challenges are the immense volume of space, the complex gravitational dynamics governed by the three-body problem, and the difficulty of detecting faint, distant objects. Current ground-based sensor networks are insufficient, providing only partial coverage with significant time gaps.

The solution lies in a multi-layered, system-of-systems approach. This includes deploying constellations of space-based sensors, leveraging a combination of advanced optical, radar, and passive RF technologies to overcome individual limitations. Computationally, this sensor network must be supported by specialized algorithms capable of initial orbit determination and trajectory prediction from sparse data in a multi-body environment, with collocation-based methods showing significant promise. Furthermore, addressing the critical data association problem for Too-Short Arcs (TSA) is essential for building a unified object catalog. Artificial intelligence and machine learning (AI/ML) will play a crucial role in optimizing sensor tasking, detecting anomalous behaviors, and assessing conjunctions.

Ultimately, technological advancements must be underpinned by a robust international policy framework for Cislunar Space Traffic Management (CSTM). While initiatives like the U.S. National Cislunar Science and Technology Strategy provide a roadmap, significant gaps in international consensus, data sharing agreements, and legal liability standards remain critical hurdles to ensuring the safe and sustainable use of cislunar space.

## Key Findings

### The Cislunar Challenge: A New Paradigm for SSA

Unlike the relatively predictable two-body mechanics that govern orbits in LEO and GEO, cislunar space is defined by the complex gravitational interactions of the Earth-Moon system, best modeled by the Circular Restricted Three-Body Problem (CR3BP). This dynamic environment introduces unique orbital classes, such as Near-Rectilinear Halo Orbits (NRHOs) and Distant Retrograde Orbits (DROs), which offer stability and accessibility for long-term missions like the Lunar Gateway [https://engineering.purdue.edu/people/kathleen.howell.1/Publications/Conferences/2017_IAA_ZimHowDav.pdf].

However, these multi-body dynamics make tracking and prediction significantly more difficult. Debris from fragmentation events can scatter unpredictably far beyond its original orbit [https://www.sciencedirect.com/science/article/abs/pii/S0273117724009189]. For high-fidelity predictions, models must often be expanded to a Restricted Four-Body Problem to account for the gravitational influence of the Sun and Jupiter. The primary challenges for cislunar SSA, therefore, shift from collision avoidance in a dense environment (LEO) to continuous detection and novel orbit determination across a vast and dynamically complex volume [https://www.sciencedirect.com/science/article/pii/S0094576524003308].

### A Growing and Diverse Cislunar Population

The cislunar domain is on the cusp of a population boom. A survey of planned missions from 2024 to 2033 reveals extensive activity from a wide range of actors. The United States leads with NASA's Artemis program, multiple Department of Defense projects (e.g., AFRL's Defense Deep Space Sentinel), and a vibrant commercial sector including Quantum Space (10 orbital platforms), Firefly Aerospace (8 landers), and Blue Origin (4 landers). International participation is also significant, with China planning six missions and numerous other nations like Russia, the European Space Agency, Japan, and India contributing orbiters, landers, and rovers [0].

This growth introduces a diverse population of objects requiring tracking, from crewed spacecraft and stations to rocket bodies, debris, and low-thrust vehicles. The latter pose a particular challenge due to their faint signatures and continuous, low-acceleration trajectories, making them difficult to detect and monitor consistently [https://hanspeterschaub.info/Papers/grads/MichaelKlonowski.pdf, https://www.space.com/space-exploration/launches-spacecraft/us-military-wants-to-track-potential-threats-coming-from-the-moon].

### Sensor Architectures: Overcoming Earth-Based Limitations

Existing ground-based sensor networks, such as the Space Surveillance Network (SSN), are fundamentally inadequate for comprehensive cislunar SSA. Their limitations include restricted fields of view, weather dependency, and insufficient power to detect faint objects at extreme distances. Performance analysis shows that current ground systems achieve only 56.4% observability of the cislunar region, with tracking gaps as long as 24 hours [https://amostech.com/TechnicalPapers/2022/Poster/Bloom.pdf].

A robust solution requires a multi-modal, layered sensor architecture, with a strong emphasis on space-based assets.
*   **Optical Telescopes:** Considered the "workhorse" for cislunar SSA, they are cost-effective for long distances and provide excellent angular data. However, they cannot measure range and are limited by lighting conditions. Space-based optical sensors can overcome these limitations [0, 3, 7].
*   **High-Power Radar:** While providing precise range and velocity data, radar effectiveness diminishes rapidly with distance due to the "tyranny of the fourth power law," making it prohibitively power-intensive for most cislunar applications [3, 8].
*   **Passive RF Sensing:** This technique is highly effective for characterizing active, transmitting satellites but is useless for tracking debris or non-cooperative, inactive objects [3, 6, 9].

To achieve continuous detection, particularly of faint objects, advanced processing initiatives like DARPA's "Track at Big Distances with Track-Before-Detect (TBD2)" program are developing new methods for processing optical signals from space-based platforms [https://sam.gov/opp/43a52cc42f5f420bb0c11452ace42d6f/view]. Furthermore, academic frameworks using concepts like the "facility location problem" are being explored to optimize the placement of sensor constellations in strategic locations, such as orbits around Lagrange points [https://www.researchgate.net/publication/383060120_Cislunar_Constellation_Design_for_Space_Situational_Awareness_with_Time-Expanded_Facility_Location_Problem].

### Advanced Algorithms and AI: The Computational Backbone

The sparse data expected from cislunar sensors necessitates a new generation of algorithms for orbit determination and catalog maintenance.
*   **Initial Orbit Determination (IOD):** Traditional methods like the Extended Kalman Filter (EKF) are often insufficient. Research indicates that **collocation-based IOD algorithms** are highly reliable, demonstrating superior accuracy and convergence for reconstructing multi-body orbits from sparse optical data over short arcs. Other advanced techniques include Differential Corrections algorithms and MCCLOD [Source: algorithms for cislunar initial orbit determination...].
*   **Data Correlation and Cataloging:** A major research gap is the data association problem, particularly for Too-Short Arc (TSA) observations where traditional IOD fails. Maintaining a unified catalog requires novel **tracklet association methods** that integrate admissible regions with nonlinear approaches to link disparate observations to a single object [https://arc.aiaa.org/doi/10.2514/1.G008069].
*   **AI and Machine Learning:** AI/ML offers powerful tools to automate and optimize cislunar SSA. Specific applications include:
    *   **Deep Reinforcement Learning (DRL)** for intelligent sensor tasking to maximize object discovery [https://amostech.com/TechnicalPapers/2022/Poster/Siew.pdf].
    *   **Convolutional Neural Networks (CNNs)** for detecting subtle satellite maneuvers [https://amostech.space/track/machine-learning-for-ssa-applications/].
    *   **Graph Neural Networks (GNNs)** for complex tasks like conjunction assessment and object characterization [https://amostech.space/track/machine-learning-for-ssa-applications/].

### Direct Applications for Short-Term Monitoring and Threat Assessment

Comprehensive cislunar SSA directly supports critical short-term tasks, including collision avoidance and rendezvous/proximity operations (RPO), which rely on precise state estimation using linearized CR3BP dynamic models [https://www.mdpi.com/2226-4310/10/8/674]. Beyond safety, SSA is crucial for threat assessment and characterizing the behavior of non-cooperative targets. Observable behaviors that can indicate intent include:
*   **High-Velocity Maneuvers:** Fuel-intensive maneuvers, like the 44 m/s burn by China's TJS-2 satellite, suggest advanced capability or urgent repositioning.
*   **Unusual Orbital Positioning:** Maneuvering to create shadows, as demonstrated by China's TJS-4, can indicate an attempt to blind an adversary's surveillance satellite.
*   **Rendezvous and Proximity Operations (RPO):** Close-approach operations, such as those conducted by Chinese and Russian satellites, could be for servicing, refueling, or inspection.
*   **Entry into Coplanar Orbits:** A satellite matching the orbital plane of another nation's asset, like Russia's Cosmos 2576 did with a U.S. satellite, is a notable event requiring characterization.
*   **Complex Flight Patterns:** Unconventional movements, such as the "corkscrew maneuvers" performed by Chinese satellites, can reveal advanced operational capabilities.
Furthermore, strategic placement of monitoring assets in DROs can enable rapid rendezvous with targets in NRHOs, supporting responsive monitoring or rescue missions [https://www.sciencedirect.com/science/article/abs/pii/S2468896724000557].

## Detailed Analysis

### Sensor and Algorithm Interdependencies

The effectiveness of a cislunar SSA architecture hinges on the synergy between its sensor hardware and its processing software. The vast distances and complex physics of the domain mean that no single sensor or algorithm can provide a complete solution. Optical systems, the primary detection method, generate angle-only data (azimuth/elevation) that is inherently ambiguous in range. This creates a critical need for either a) fusion with range-providing sensors like radar or passive RF, which are range-limited or target-dependent, or b) highly sophisticated IOD algorithms that can resolve an orbit from sparse, angle-only measurements.

The prominence of collocation-based IOD algorithms is a direct response to this challenge. Unlike traditional shooting methods or filters like the EKF, which can struggle to converge without a good initial guess, collocation methods reconstruct an entire trajectory segment that best fits the sparse observations. This makes them more robust to the long observational gaps and limited data inherent to cislunar tracking.

However, even with advanced IOD, the fundamental problem of linking tracklets—short arcs of observational data—remains. This "Too-Short Arc" (TSA) problem is a major bottleneck in catalog creation. A novel tracklet association method that combines geometric constraints (admissible regions) with nonlinear dynamics is a proposed solution, but this remains an active area of research and a critical gap in capability [https://arc.aiaa.org/doi/10.2514/1.G008069]. While the research logs identified Encke's method as a computational technique for trajectory propagation, specific details on its application to CR3BP and R4BP models using sparse data were not available in the provided sources.

### The Policy and International Collaboration Imperative

Technology alone is insufficient. The successful management of cislunar space requires a robust Cislunar Space Traffic Management (CSTM) framework. Currently, this framework is nascent and faces significant political hurdles. The research highlights a lack of international consensus on the urgency of the problem, an absence of legally binding data sharing agreements, and no agreed-upon standards for collision avoidance liability [https://www.unoosa.org/res/oosadoc/data/documents/2025/aac_105c_2_2025crp/aac_105c_2_2025crp_23_0_html/AC105_C2_2025_CRP23E.pdf]. Initiatives like "The Cologne Manual on Space Traffic Management" are important steps, but they are not binding regulations. Without shared data and established norms of behavior, distinguishing between routine operations, anomalous behavior, and outright threats becomes exponentially more difficult, increasing the risk of miscalculation and conflict.

## Conclusion & Outlook

Achieving comprehensive and accurate situational awareness in cislunar space is a grand challenge that requires a paradigm shift in technology, algorithms, and international policy. The path forward is not through a single breakthrough but through the integrated development of a system-of-systems.

The roadmap laid out by the U.S. National Cislunar Science and Technology Strategy provides a clear direction, prioritizing investment in R&D, international cooperation, and the extension of SSA capabilities beyond GEO [https://bidenwhitehouse.archives.gov/wp-content/uploads/2022/11/11-2022-NSTC-National-Cislunar-ST-Strategy.pdf]. Key investment priorities must focus on deploying space-based sensor constellations, maturing advanced IOD and data fusion algorithms to handle sparse data in multi-body regimes, and operationalizing AI/ML for autonomous sensor management and pattern-of-life analysis.

In the coming decade, as the cislunar population grows, the ability to track, monitor, and characterize objects will become a cornerstone of space safety, scientific discovery, and national security. Success will depend not only on deploying advanced hardware and software but also on fostering an international framework of transparency and data sharing to ensure that cislunar space remains a sustainable and accessible domain for all.

## References

A complete list of sources is available in the raw research logs. Key sources referenced in this report include materials from Ansys, ScienceDirect, MIT DSpace, NASA, Air Force Research Laboratory (AFRL), Purdue University, DARPA, AMOS Technical Papers, ResearchGate, and the United Nations Office for Outer Space Affairs (UNOOSA).

## Citations 
- https://dspace.mit.edu/bitstream/handle/1721.1/162417/rude-rudc6118-sm-tpp-2025-thesis.pdf.pdf?sequence=1&isAllowed=y
- https://www.sciencedirect.com/science/article/pii/S0094576524003308
- https://www.ansys.com/simulation-topics/what-is-space-situational-awareness
- https://hanspeterschaub.info/Papers/grads/MichaelKlonowski.pdf
- https://www.jhuapl.edu/Content/documents/CislunarSecurityNationalTechnicalVision.pdf
- https://www.afrl.af.mil/Portals/90/Documents/RV/A%20Primer%20on%20Cislunar%20Space_Dist%20A_PA2021-1271.pdf?ver=vs6e0sE4PuJ51QC-15DEfg%3D%3D
- https://www.airuniversity.af.edu/Portals/10/AEtherJournal/Journals/Special-Edition_Winter2023/Willis.pdf
- https://ntrs.nasa.gov/citations/20120009459
- https://www.airandspaceforces.com/article/cislunar-space/
- https://cdcl.umd.edu/papers/icssa20.pdf
- https://www.sciencedirect.com/science/article/abs/pii/S0094576521002526
- https://engineering.purdue.edu/people/kathleen.howell.1/Publications/Conferences/2017_IAA_ZimHowDav.pdf
- https://ntrs.nasa.gov/citations/20210007698
- https://www.sciencedirect.com/science/article/abs/pii/S2468896724000557
- https://openresearch.surrey.ac.uk/view/pdfCoverPage?instCode=44SUR_INST&filePid=13166040750002346&download=true
- https://space.stackexchange.com/questions/40560/two-body-problem-vs-three-body-problem-applications
- https://ross.aoe.vt.edu/books/Ross_3BodyProblem_Book_2022.pdf
- https://forum.nasaspaceflight.com/index.php?topic=24989.0
- https://www.sciencedirect.com/science/article/abs/pii/S0273117724009189
- https://www.gg.caltech.edu/~mwl/publications/papers/dynamicalThreeBody.pdf
- https://csps.aerospace.org/sites/default/files/2024-10/06d_Moonstruck_Bukley-Stover_20241022_0.pdf
- https://newspaceeconomy.ca/2024/09/28/cislunar-space-debris-increasing-concerns/
- https://www.hou.usra.edu/meetings/orbitaldebris2023/pdf/6105.pdf
- https://spacenews.com/university-researchers-flag-cislunar-space-debris-concerns/
- https://spacesecurity.wse.jhu.edu/2024/09/29/university-researchers-flag-cislunar-space-debris-concerns/
- https://www.space.com/space-exploration/launches-spacecraft/us-military-wants-to-track-potential-threats-coming-from-the-moon
- https://www.researchgate.net/publication/322399511_Challenges_and_Potential_in_Space_Domain_Awareness
- https://www.researchgate.net/publication/359014581_Expanding_the_Space_Surveillance_Network_with_Space-Based_Sensors_Using_Metaheuristic_Optimization_Techniques
- https://quizlet.com/study-guides/comparing-space-and-ground-based-sda-sensor-performance-14e3c31a-2940-4bc9-b4ce-7dcebcb7a224
- https://amostech.com/TechnicalPapers/2022/Poster/Bloom.pdf
- https://www.researchgate.net/publication/393975299_System_Design_and_Analysis_for_Cislunar_Space_Domain_Awareness_Through_Distributed_Sensors
- https://sam.gov/opp/43a52cc42f5f420bb0c11452ace42d6f/view
- https://www.highergov.com/contract-opportunity/track-at-big-distances-with-track-before-detect-t-darpa-ps-26-01-o-ae224/
- https://www.researchgate.net/publication/383060120_Cislunar_Constellation_Design_for_Space_Situational_Awareness_with_Time-Expanded_Facility_Location_Problem
- https://arxiv.org/html/2408.06238v1
- https://ui.adsabs.harvard.edu/abs/2023amos.conf...17H/abstract
- https://amostech.com/TechnicalPapers/2024/Cislunar_SDA/Ojeda-Romero.pdf
- https://www.researchgate.net/publication/394208975_Initial_Orbit_Determination_for_Cislunar_Objects_with_Unknown_Maneuvers_via_Collocation_and_Nonlinear_Programming
- https://link.springer.com/article/10.1007/s40295-025-00513-7
- https://www.researchgate.net/publication/394119537_Differential_Corrections_Algorithm_for_Initial_Orbit_Determination_in_the_Cislunar_Region_using_Angle-Only_Measurements
- https://ui.adsabs.harvard.edu/abs/2022AGUFMSA12A..05G/abstract
- https://www.researchgate.net/publication/372205114_Optimizing_Multi-spacecraft_Cislunar_Space_Domain_Awareness_Systems_via_Hidden-Genes_Genetic_Algorithm
- https://www.keaipublishing.com/en/journals/space-habitation/call-for-papers/ai-enabled-cislunar-space-situational-awareness/
- https://amostech.space/track/machine-learning-for-ssa-applications/
- https://amostech.com/TechnicalPapers/2022/Poster/Siew.pdf
- https://muse.jhu.edu/article/950954
- https://ar5iv.labs.arxiv.org/html/1910.03014
- https://doaj.org/article/4c048b4229f74e558d0c723a4e973227
- https://amostech.space/track/cislunar-ssa/
- https://www.researchgate.net/publication/372791517_Rendezvous_and_Proximity_Operations_in_Cislunar_Space_Using_Linearized_Dynamics_for_Estimation
- https://www.mdpi.com/2226-4310/10/8/674
- https://www.researchgate.net/publication/394384917_Spacecraft_Rendezvous_and_Precise_Landing_in_the_Cislunar_Region_with_a_LiDAR
- https://amostech.com/wp-content/uploads/2025/06/AMOS-2025-Program.pdf
- https://www.researchgate.net/publication/353300292_Multi-Fidelity_Orbit_Determination_with_Systematic_Errors
- https://docs.starrocks.io/docs/data_source/catalog/unified_catalog/
- https://www.researchgate.net/publication/228932337_Correlation_of_Optical_Observations_of_Objects_in_Earth_Orbit
- https://www.nasa.gov/wp-content/uploads/2021/05/cislunar_ssa_proposed_message_set-nov2021_rev2_without_emailspdf.pdf
- https://hal.science/hal-05067616v1/file/DTIS2025-009-Pre-proof-Accept%C3%A9e.pdf
- https://ilwr.jura.uni-koeln.de/sites/ilwr/user_upload/CM-STM_2025__Guidelines.pdf
- https://www.researchgate.net/publication/391481695_Weak_Signals_in_Cislunar_Space_Traffic_Management_How_can_policy_to_facilitate_CSTM_be_designed_to_adapt_to_unexpected_events_and_emerging_trends
- https://www.unoosa.org/res/oosadoc/data/documents/2025/aac_105c_22025crp/aac_105c_22025crp_23_0_html/AC105_C2_2025_CRP23E.pdf
- https://iser.org.in/conf/call.php?id=100268120
- https://arc.aiaa.org/doi/10.2514/1.G008069
- https://www.researchgate.net/publication/326567294_Improved_tracklet_association_for_space_objects_using_short-arc_optical_measurements
- https://discovery.researcher.life/topic/non-cooperative-target/15151680?page=1&topic_name=Non-cooperative%20Target
- https://csis-website-prod.s3.amazonaws.com/s3fs-public/2025-04/250425_Swope_Space_Threat.pdf?VersionId=orhySgjISemJLjhdQKKes2OVb35jwkU5
- https://bandi.mur.gov.it/doctorate.php/public/cercaFellowship?jf_comp_status_id=*&bb_type_code=%25&idarea=%25&azione=cerca&orderby=scadenza_desc
- https://dspace.mit.edu/bitstream/handle/1721.1/162417/rude-rudc6118-sm-tpp-2025-thesis.pdf.pdf?sequence=1&isAllowed=y
- https://spacenews.com/ostp-releases-cislunar-science-and-technology-plans/
- https://bidenwhitehouse.archives.gov/wp-content/uploads/2022/11/11-2022-NSTC-National-Cislunar-ST-Strategy.pdf
- https://bidenwhitehouse.archives.gov/wp-content/uploads/2024/12/Cislunar-Implementation-Plan-Final.pdf
- https://space.commerce.gov/white-house-releases-national-cislunar-st-strategy/
- https://www.researchgate.net/publication/363484263_Cislunar_Trajectory_Design_Methodologies_Incorporating_Quasi-Periodic_Structures_With_Applications
- https://www.sciencedirect.com/science/article/abs/pii/S0094576523003661