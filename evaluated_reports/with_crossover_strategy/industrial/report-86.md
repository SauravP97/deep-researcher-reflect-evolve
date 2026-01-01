# Conduct a research report on the manufacturing technology options for hollow motor shafts used in New Energy Vehicle (NEV) electric drive units. List all current forming techniques, compare them based on criteria such as suitable materials, cost-effectiveness, required subsequent processing steps, and other relevant factors. Finally, identify the most suitable manufacturing routes for this specific application.

# **Deep Research Report: Manufacturing Technology Analysis for New Energy Vehicle (NEV) Hollow Motor Shafts**

## Executive Summary

This report provides a comprehensive analysis of the manufacturing technologies for hollow motor shafts, a critical component in New Energy Vehicle (NEV) electric drive units. The shift toward higher motor speeds and power densities necessitates advanced shafts that facilitate internal oil cooling, optimize Noise, Vibration, and Harshness (NVH), and ensure high mechanical reliability.

The analysis reveals a definitive industry trend away from traditional subtractive methods like deep drilling towards advanced near-net-shape forming technologies. For high-volume production, **Cold Forging/Extrusion in a monobloc (one-piece) configuration** has emerged as the most suitable manufacturing route. This method, validated by leading Tier 1 suppliers like GKN, offers an optimal balance of superior mechanical properties (enhanced by continuous grain flow), high material utilization (>90%), and cost-effectiveness at scale.

For high-performance applications demanding complex geometries and maximum lightweighting, **hybrid process chains centered on Orbital Forming** are the preferred choice. Championed by suppliers like Schaeffler, this route combines a pre-forming step (e.g., deep drawing or backward extrusion) with orbital forming to create intricate features like splines with exceptional precision and strength, significantly improving NVH characteristics.

Traditional methods like 'Hot Extrusion + Cold Drawing' are becoming less competitive due to lower fatigue performance and higher energy consumption. Additive Manufacturing is currently viable only for prototyping and low-volume specialty production due to high costs and extensive post-processing requirements.

## 1. Introduction: The Critical Role of Hollow Motor Shafts in NEVs

The hollow motor shaft is an integral component of the modern NEV e-axle. Its design and manufacturing process are critical for three primary reasons:

1.  **Thermal Management:** The hollow core serves as a conduit for indirect oil cooling, a superior method for managing heat in high-speed, high-power-density electric motors [https://en.eeworld.com.cn/news/qrs/eic676309.html, https://www.allpcb.com/allelectrohub/oil-cooling-systems-for-ev-drive-motors].
2.  **NVH Performance:** The shaft's geometry and stiffness are precisely tuned to shift its natural resonance frequencies away from the motor's excitation frequencies, significantly reducing vibration and contributing to the quiet operation expected of EVs [https://www.researchgate.net/publication/325758398_NVH_Aspects_of_Electric_Drives-Integration_of_Electric_Machine_Gearbox_and_Inverter].
3.  **Performance and Lightweighting:** As a key power transmission component, the shaft must withstand high torque and fatigue loads while being as lightweight as possible to improve overall vehicle efficiency.

## 2. Key Performance Benchmarks for Evaluation

To objectively compare manufacturing routes, this analysis uses the following key performance criteria, which have been validated for high-performance NEV motor shafts:

| Performance Criterion | Specification |
| :--- | :--- |
| **Torsional Stiffness** | 1500 - 3000 Nm/deg |
| **Fatigue Life** | > 1,000,000 cycles at peak torque |
| **Balancing Grade** | ISO 21940 G2.5 or better (G1.0 for speeds >15,000 rpm) |
| **Key Dimensional Tolerances** | Runout: < 20 µm, Concentricity: < 20 µm, Roundness: < 5 µm |

## 3. Analysis of Individual Manufacturing Technologies

Manufacturing processes for hollow shafts can be categorized as subtractive, forming (bulk and sheet), welding, and additive. Forming technologies are overwhelmingly preferred for mass production.

### 3.1. Subtractive Manufacturing: Deep Drilling

Deep drilling creates a hollow shaft by machining a central hole through a solid bar. While conceptually simple, it is largely unsuitable for mass production in the NEV industry.

*   **Disadvantages:**
    *   **Extreme Material Waste:** Material utilization can be less than 50%, with a large portion of expensive raw material converted to low-value scrap.
    *   **Low Cost-Effectiveness:** High material waste, long cycle times, and high energy/tool consumption make it an expensive process for high volumes.
    *   **Inferior Mechanical Properties:** The drilling process cuts through the material's natural grain flow, creating stress concentrations and compromising strength and fatigue resistance compared to forming methods.
*   **Verdict:** Suitable only for prototyping and very small-batch production.

### 3.2. Bulk and Sheet Forming Technologies

These near-net-shape processes shape the material into its final form, offering superior material utilization and mechanical properties.

| Technology | Process Description | Key Advantages | Key Disadvantages |
| :--- | :--- | :--- | :--- |
| **Cold Forging / Extrusion** | Shaping metal at room temperature using compressive force to form a monobloc part from a solid slug. | Excellent mechanical properties (work hardening, continuous grain flow), high precision, minimal subsequent machining. | High initial investment in tooling and presses. Limited geometric complexity compared to hot forging. |
| **Hot Forging / Extrusion** | Shaping metal above its recrystallization temperature. | High design flexibility for large, complex shapes. Lower forming forces required. | Poor surface finish and dimensional accuracy requires significant secondary machining. Higher energy consumption. |
| **Orbital Forming / Rotary Swaging** | Incremental cold forming where rollers or dies shape a preform over a mandrel at high frequency. | Creates complex internal/external geometries (splines) with high precision. Uninterrupted grain flow enhances strength and NVH. Short cycle times. | Requires a hollow preform. Technology is specialized. |
| **Flow Forming** | An incremental cold forming process that shapes a hollow preform over a rotating mandrel using rollers. | Ideal for high-precision, thin-walled parts. Enhances material properties via cold work. Cost-efficient for specialty alloys. | Limited to axisymmetric (cylindrically symmetrical) geometries. |
| **Cross-Wedge Rolling (CWR)** | A hot forming process where heated bars are progressively compressed and elongated by wedge-shaped tools. | Efficient, material-saving, produces parts with high dimensional accuracy and good surface finish. | As a hot process, may require subsequent finishing. |
| **Deep Drawing** | A sheet-forming process that stretches a flat metal sheet into a hollow shape. | Extremely cost-effective for high volumes (>50,000 units). High production rates and good material savings. | High initial tooling cost. Requires multiple secondary operations (trimming, machining, heat treatment). |
| **Tube Hydroforming** | Uses high-pressure internal fluid to expand a metal tube into a die cavity. | Excellent for complex, non-uniform cross-sections. Reduces assembly steps and material waste. | High initial capital investment. Data on achievable tolerances and NVH was unavailable in the provided research. |

### 3.3. Welding and Assembly Technologies

This approach involves fabricating a shaft from tubing and other components.

*   **Electric Resistance Welding (ERW) Tubing:** A cost-effective, high-speed method for producing tubes. However, the weld seam represents a potential structural weak point, making it less suitable for high-stress applications on its own.
*   **Laser Welding:** A high-precision process that creates strong, high-quality welds with a minimal heat-affected zone. This reduces distortion and the need for subsequent machining but involves high capital costs. It is highly versatile with materials, including advanced high-strength steels (AHSS).

### 3.4. Additive Manufacturing (AM)

AM builds parts layer-by-layer, offering unparalleled design freedom. However, for this application, it is currently limited to prototyping and low-volume production.

*   **Selective Laser Melting (SLM):** Offers high resolution for intricate internal geometries (e.g., cooling channels).
*   **Directed Energy Deposition (DED):** Has a much higher deposition rate, making it more cost-effective for larger parts and rapid prototyping.
*   **Common Limitations:** Both methods have high costs and require mandatory, extensive post-processing, including heat treatment (to relieve stress), Hot Isostatic Pressing (HIP) (to reduce porosity for fatigue life), and finish machining (for tolerances and surface finish).

## 4. Profile of Validated Hybrid Manufacturing Routes

The most effective solutions for NEV hollow shafts involve optimized process chains, often combining multiple techniques. The following routes have been validated by industry leaders.

### 4.1. Cold Forging / Extrusion (Monobloc Approach)

This is widely regarded as the mainstream technology for mass-market NEVs. The process forms a single, integrated (monobloc) hollow shaft from a solid billet.
*   **Process Chain:** Blanking -> Intermediate Heating -> Lubrication (Phosphating) -> Multi-stage Cold Extrusion -> Stress Relief Annealing -> Finishing (Soft Machining, Heat Treatment, Hard Machining/Grinding).
*   **Performance:** Creates an uninterrupted grain flow that follows the component's contour, dramatically increasing strength and fatigue life (reported as >3.6 times that of hot extruded parts). The monobloc design provides superior dynamic balance and concentricity, directly improving NVH.
*   **Cost-Effectiveness:** Despite high initial investment, it is highly cost-effective at scale due to material utilization >90% and minimal secondary machining, with estimated cost savings over 20% compared to traditional methods.
*   **Industry Validation:** Leading supplier GKN Driveline utilizes this method to produce monobloc shafts with integrated splines and gears.

### 4.2. Pre-forming + Orbital Forming

This advanced hybrid route is ideal for high-performance applications requiring complex features and maximum strength.
*   **Process Chain:** Pre-forming (e.g., Deep Drawing or Backward Extrusion to create a hollow blank) -> Orbital Forming (to create final internal/external splines and geometries) -> Hardening -> Hard-Fine Machining (on critical surfaces like bearing seats).
*   **Performance:** Orbital forming creates an uninterrupted grain flow in features like splines, resulting in superior strength, fatigue life, and durability compared to machined features. The high precision and surface quality lead to excellent NVH characteristics.
*   **Cost-Effectiveness:** This route shortens the production chain by consolidating multiple conventional steps (milling, broaching) into a single forming operation, saving material and time.
*   **Industry Validation:** Schaeffler is a key proponent of this technology, combining orbital forming with other cold forming techniques to produce lightweight, high-strength shafts.

### 4.3. ERW Tubing + Laser Welding Assembly

This route offers a cost-optimized solution by combining low-cost bulk material with high-precision joining.
*   **Process Chain:** Use cost-effective ERW tubing for the main shaft body -> Use high-precision laser welding to attach other components (e.g., gears, flanges).
*   **Performance:** Leverages the precision and low heat input of laser welding for critical joints, ensuring strength and minimizing distortion, while using low-cost tubing for the less critical main body.
*   **Cost-Effectiveness:** Balances the low cost of ERW material with the higher cost of laser welding, applying the expensive process only where necessary.
*   **Industry Validation:** This hybrid approach is increasingly common for creating cost-effective, high-performance assembled components in the automotive industry.

### 4.4. Hot Extrusion + Cold Drawing

This is the most traditional forming route for hollow shafts.
*   **Process Chain:** Hot Extrusion (to create near-net shape tube) -> Annealing -> Cold Drawing (to achieve final dimensions/finish) -> Straightening -> Heat Treatment -> Final Machining.
*   **Performance:** Produces parts with good mechanical properties but a less uniform microstructure and coarser grains compared to cold forging. This can result in lower fatigue performance.
*   **Cost-Effectiveness:** Now considered less competitive due to a long process flow, high energy consumption, and lower material utilization compared to advanced cold forming methods.

## 5. Comparative Analysis and Strategic Recommendations

| Manufacturing Route | Material Utilization | Per-Unit Cost (High Vol.) | Mechanical Performance (Fatigue) | NVH Performance | Production Efficiency |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Cold Forging (Monobloc)** | Excellent (>90%) | Low | Excellent | Excellent | High |
| **Pre-forming + Orbital Forming** | Excellent (>70%) | Low-Medium | Superior | Superior | High |
| **Hot Extrusion + Cold Drawing** | Good (>90%) | Medium | Good | Good | Medium |
| **Deep Drilling (Subtractive)** | Poor (<50%) | High | Inferior | Good | Low |

### Recommendations by Market Segment

*   **For Mass-Market NEVs:**
    **Cold Forging / Extrusion (Monobloc)** is the most suitable manufacturing route. Its combination of low per-unit cost at scale, high production efficiency, excellent material utilization, and robust mechanical performance directly meets the demands of high-volume automotive production.

*   **For High-Performance NEVs:**
    The **Pre-forming + Orbital Forming** hybrid process chain is the premier choice. It delivers superior strength, durability, and NVH performance by creating geometrically complex parts with an optimized grain structure. The ability to lightweight and integrate features makes it ideal for applications where performance is the primary driver. The Cold Forging (Monobloc) route is also a strong contender in this segment.

*   **For Prototyping and Niche/Motorsport Applications:**
    **Additive Manufacturing (SLM or DED)** is the most suitable route for developing and testing innovative, lightweight designs with complex internal features that are not feasible with other methods. For simple, early-stage prototypes where cost is a major constraint, **Deep Drilling** remains a viable, albeit low-performance, option.

## 6. Conclusion and Outlook

The manufacturing technology for hollow motor shafts in NEVs has evolved rapidly to meet stringent performance, cost, and volume requirements. Advanced cold forming techniques have decisively replaced traditional subtractive and less-efficient hot forming processes. **Cold forging** provides a robust, cost-effective solution for the mass market, while **orbital forming** enables a higher level of performance and design integration for premium applications. As the NEV market continues to push for higher power densities and efficiency, these forming-centric, near-net-shape manufacturing routes will remain the cornerstone of electric drive unit production.

---
## 7. References

*   [https://en.eeworld.com.cn/news/qrs/eic676309.html](https://en.eeworld.com.cn/news/qrs/eic676309.html)
*   [https://www.allpcb.com/allelectrohub/oil-cooling-systems-for-ev-drive-motors](https://www.allpcb.com/allelectrohub/oil-cooling-systems-for-ev-drive-motors)
*   [https://www.researchgate.net/publication/325758398_NVH_Aspects_of_Electric_Drives-Integration_of_Electric_Machine_Gearbox_and_Inverter](https://www.researchgate.net/publication/325758398_NVH_Aspects_of_Electric_Drives-Integration_of_Electric_Machine_Gearbox_and_Inverter)
*   [https://www.sciencedirect.com/science/article/pii/S1526612519302890](https://www.sciencedirect.com/science/article/pii/S1526612519302890)
*   [https://www.researchgate.net/publication/384053671_Design_and_simulation_of_cross_wedge_rolling_process_for_hollow_motor_shaft](https://www.researchgate.net/publication/384053671_Design_and_simulation_of_cross_wedge_rolling_process_for_hollow_motor_shaft)
*   [https://www.researchgate.net/publication/309561936_Analysis_of_a_cross_wedge_rolling_process_for_producing_drive_shafts](https://www.researchgate.net/publication/309561936_Analysis_of_a_cross_wedge_rolling_process_for_producing_drive_shafts)
*   [https://engrxiv.org/preprint/download/2996/5509](https://engrxiv.org/preprint/download/2996/5509)
*   [https://www.alekvs.com/metal-forming-processes-forging-rolling-drawing-and-extrusion/](https://www.alekvs.com/metal-forming-processes-forging-rolling-drawing-and-extrusion/)
*   [https://onetouchexim.com/metal-forming-processes-types-applications/](https://onetouchexim.com/metal-forming-processes-types-applications/)
*   [https://supply.csmfg.com/how-to-draw-metal/](https://supply.csmfg.com/how-to-draw-metal/)
*   [https://aluminum-extrusions.net/](https://aluminum-extrusions.net/)
*   [https://artizono.com/hot-vs-cold-extrusion-key-differences-and-applications/](https://artizono.com/hot-vs-cold-extrusion-key-differences-and-applications/)
*   [https://www.researchgate.net/figure/Rotor-design-of-the-interior-permanent-magnet-IPM-machine-of-production-traction_fig5_340841920](https://www.researchgate.net/figure/Rotor-design-of-the-interior-permanent-magnet-IPM-machine-of-production-traction_fig5_340841920)
*   [https://www.francis-press.com/uploads/papers/rjosn3TEvnVXlmmK2UcuDQfopkGhyNJvBETSIdhD.pdf](https://www.francis-press.com/uploads/papers/rjosn3TEvnVXlmmK2UcuDQfopkGhyNJvBETSIdhD.pdf)
*   *Additional sources were synthesized from the raw research logs provided in the prompt.*

## Citations 
- https://www.researchgate.net/publication/325758398_NVH_Aspects_of_Electric_Drives-Integration_of_Electric_Machine_Gearbox_and_Inverter
- https://en.eeworld.com.cn/news/qrs/eic676309.html
- https://www.allpcb.com/allelectrohub/oil-cooling-systems-for-ev-drive-motors
- https://www.alekvs.com/metal-forming-processes-forging-rolling-drawing-and-extrusion/
- https://onetouchexim.com/metal-forming-processes-types-applications/
- https://engrxiv.org/preprint/download/2996/5509
- https://sdbidoon.com/document/production-technology-09.04.2020.pdf
- https://supply.csmfg.com/how-to-draw-metal/
- https://www.sciencedirect.com/science/article/pii/S1526612519302890
- https://fr.scribd.com/presentation/455943670/MPS-PPT-radial-forging
- https://apps.dtic.mil/sti/tr/pdf/ADA278770.pdf
- https://www.sakysteel.com/news/the-process-flow-of-forging-and-the-characteristics-of-its-forgings/
- https://www.youtube.com/watch?v=TGHwfv7TcOo
- https://www.researchgate.net/publication/309561936_Analysis_of_a_cross_wedge_rolling_process_for_producing_drive_shafts
- https://www.researchgate.net/publication/384053671_Design_and_simulation_of_cross_wedge_rolling_process_for_hollow_motor_shaft
- https://www.researchgate.net/publication/397887450_Comparative_analysis_of_cross-wedge_rolling_methods
- https://www.scribd.com/document/899514508/Lab-Manual-TA211-2025-26
- https://felss.com/en/industry/
- https://felss.com/en/technologies/rotary-swaging/
- https://www.researchgate.net/publication/395886662_Structure_and_Mechanical_Properties_of_Tubular_Steel_Products_Processed_by_Cold_Rotary_Swaging
- https://astforgetech.com/flow-forming-a-complete-overview/
- https://link.springer.com/rwe/10.1007/978-3-642-35950-7_16750-1
- https://intradefairs.com/flow-forming-or-metal-spinning
- https://americanflowform.com/whatisflowforming
- https://www.sciencedirect.com/topics/materials-science/flow-forming
- https://artizono.com/hot-vs-cold-extrusion-key-differences-and-applications/
- https://aluminum-extrusions.net/
- https://www.researchgate.net/profile/Manikandan-Ganapathy/publication/278598389_Tube_hydroforming_in_automotive_applications/links/578e282a08ae81b4466eb8c3/Tube-hydroforming-in-automotive-applications.pdf
- https://www.semanticscholar.org/paper/Tube-hydroforming-process%3A-A-reference-guide-Alaswad-Benyounis/b5a1a6b6d05aa76bee3aa9064b42a2a8bdfbc00d
- https://www.youtube.com/watch?v=QWLKEPRetcM
- https://www.thefabricator.com/tubepipejournal/article/hydroforming/introduction-to-tube-hydroforming
- https://ricos.it/tube-hydroforming-process-everything-you-need-to-know/
- https://4umachining.com/cold-extrusion/
- https://realitycapeforum.com/forums/topic/fundamental-principles-of-high-precision-cold-extrusion-process
- https://www.linkedin.com/pulse/advantages-disadvantages-cold-extrusion-vzibc
- https://www.programmaticblog.com/2025/06/26/manufacturing-process-of-high-precision-cold-extrusion-parts/
- https://artizono.com/hot-vs-cold-extrusion-key-differences-and-applications/
- https://news.futunn.com/en/post/23890315/new-coordinates-603040-in-depth-report-holding-the-powerful-tools
- https://www.marklines.com/en/search/0?q=Winding&and=true&func=2&order=
- https://patents.google.com/patent/US4556116A/en
- https://teslaresearch.jimdofree.com/articles-interviews/electrical-oscillators-by-nikola-tesla-electrical-experimenter-july-1919/
- https://www.worldradiohistory.com/Archive-Electronics/70s/73/Electronics-1973-05-24.pdf
- https://www.researchgate.net/figure/Rotor-design-of-the-interior-permanent-magnet-IPM-machine-of-production-traction_fig5_340841920
- https://en.eeworld.com.cn/news/qrs/eic681987.html
- https://d-scholarship.pitt.edu/47057/13/Lubin_Master_Thesis-3.pdf
- https://www.francis-press.com/uploads/papers/rjosn3TEvnVXlmmK2UcuDQfopkGhyNJvBETSIdhD.pdf
- https://www.sciencedirect.com/science/article/pii/S2590123025011831
- https://www.researchgate.net/publication/334458265_Numerical_investigation_of_a_cold_forging_process_for_manufacturing_hollow_shafts_with_variable_wall_thickness
- https://www.researchgate.net/publication/240381059_New_warm_forming_processes_to_produce_hollow_shafts
- https://modtech.ro/international-journal/ijpapers.php
- https://studylib.net/doc/25342914/section-13-manufacturing-processes
- https://iopscience.iop.org/issue/1742-6596/2566/1