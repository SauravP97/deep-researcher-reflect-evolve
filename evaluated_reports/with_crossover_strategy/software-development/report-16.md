# 收集整理目前非接触式感知领域做的最好的算法策略，并为我评估他们的输入信号与准确率

好的，这是根据您提供的研究笔记编写的深度研究报告。

---

### **非接触式感知技术SOTA算法策略综合评估报告**

**报告日期:** 2024年5月24日
**报告ID:** AI-RE-2024-05-24-01
**撰写方:** 自主AI研究服务 - 首席研究编辑

### **执行摘要**

本报告旨在全面评估当前非接触式感知领域的顶尖（State-of-the-Art, SOTA）算法策略、其核心输入信号及性能指标。研究发现，非接触式感知技术主要依赖Wi-Fi/射频、毫米波雷达、计算机视觉等物理信号，并普遍采用深度学习模型作为核心算法框架。

- **基于Wi-Fi的感知技术**已相当成熟，主流方法利用信道状态信息（CSI）作为输入。在人体活动和手势识别任务中，**WiADG、EfficientFi**等算法在ARIL、Widar3.0等公开数据集上可实现**超过95%**的准确率。新兴的生成式模型（如**RF-Diffusion**）代表了新的研究方向，但其直接性能对比数据尚不明确。

- **基于毫米波雷达的感知技术**在手势识别领域表现尤为突出，利用点云、距离-多普勒图（RDM）等作为输入，**GRNet、ST-GCN**等算法在自建数据集上的准确率甚至**超过99%**。然而，在睡眠监测、驾驶员监控等其他场景，尽管技术路径明确，但具体的量化性能指标仍然缺乏。

- **基于视觉的远程生命体征测量（rPPG）**技术重点在于提升算法在复杂光照和运动条件下的鲁棒性。其性能评估更侧重于信噪比（SNR）、相关系数等指标，而非单一的准确率。

- **多模态融合**是提升系统鲁棒性和准确率的关键策略。报告分析了一个毫米波雷达与摄像头融合的占用检测系统案例，其准确率达到了**93.8%**，验证了该路径的有效性。

- **未来趋势**显示，该领域正朝着**智能反射面（IRS）**以优化感知环境、**边缘计算**以实现高效部署，以及**生成式AI**以创造高质量训练数据的方向发展。

**核心挑战：** 贯穿整个领域的一个关键挑战是**缺乏统一、大规模的公共基准数据集**，这使得跨研究的算法性能直接对比变得困难。SenseFi框架和EHUNAM等数据集的出现，正试图缓解这一问题。

### **1. 非接触式感知技术概述与分类**

非接触式感知，或称无设备感知（Device-free Sensing），是指在不需用户佩戴或携带任何设备的情况下，通过分析环境中物理信号的变化来感知目标状态、活动或生理特征的技术。根据所依赖的物理信号，主流技术路径可分为以下几类：

*   **基于Wi-Fi/射频（RF）的感知**：利用Wi-Fi、蜂窝网络等无线射频信号的传播特性变化进行感知。
*   **基于毫米波雷达（mmWave Radar）的感知**：利用毫米波频段电磁波的高分辨率和穿透性进行精细感知。
*   **基于计算机视觉（Video/Thermal）的感知**：通过摄像头捕捉可见光或热成像视频进行分析。
*   **基于声学（Acoustic）的感知**：利用声波（如超声波）的反射和多普勒效应进行感知。

本报告将重点分析前三种技术路径的SOTA算法。

### **2. 基于Wi-Fi/射频信号的感知技术分析**

#### **2.1 核心输入信号：信道状态信息（CSI）**
当前基于Wi-Fi的感知技术已从早期的接收信号强度指示（RSSI）转向信息更丰富的**信道状态信息（CSI）**。CSI能精细刻画信号在多条传播路径上的振幅和相位信息，对由人体活动引起的细微环境变化更为敏感，因此成为当前SOTA算法的主流输入信号。

#### **2.2 SOTA算法性能评估**
多种基于深度学习的算法在Wi-Fi感知任务中取得了优异表现。以下是对几款代表性算法的性能评估：

| 算法/策略 | 核心架构 | 任务 | 性能指标（准确率） | 评估基准/数据集 |
| :--- | :--- | :--- | :--- | :--- |
| **WiADG** | Attention-based BLSTM + GRU，结合对抗性领域自适应 | 手势识别 | **98.7%** / **94.7%** | ARIL (公开) |
| | | | **97.5%** | 自建数据集 |
| **EfficientFi** | 轻量级CNN，结合强化学习进行子载波选择 | 人体活动识别 | **97.4%** | ARIL (公开) |
| | | 手势识别 | **96.2%** (平均) | Widar3.0 (公开) |
| **Attention-Based BLSTM** | 双向长短期记忆网络 + 注意力机制 | 人体活动识别 | **97.41%** / **97.52%** | WiAR / WiDAR |
| **DeepSeg** | 深度学习分割框架 | 活动信号分割 | >**95%** (分割准确率) | 多个公开数据集 |

**分析：**
- **WiADG** 专注于解决跨环境、跨设备的“领域漂移”问题，鲁棒性是其核心优势。
- **EfficientFi** 则通过模型压缩和特征选择，在保证高精度的前提下，显著降低了计算开销，适用于大规模或资源受限的部署场景。
- **Attention-Based BLSTM** 作为一种强大的序列数据处理模型，是许多复杂算法的基础构件。
- **DeepSeg** 专注于预处理环节，其高精度的信号分割能力是保障后续分类模型性能的关键。

#### **2.3 新兴生成式模型：RF-Diffusion**
近期在顶级会议MobiCom 2024上出现的**RF-Diffusion**算法标志着一个重要的技术转向。它是一个基于时频扩散的射频信号生成模型，从传统的判别式模型（即分类）转向生成式模型。其核心优势在于能够生成多样化、高质量的时间序列射频数据，可用于数据增强、系统仿真等。尽管相关研究已将其与三种主流生成模型进行对比，但**目前公开的资料中并未提供具体的量化性能对比结果**。

#### **2.4 评估基准与挑战**
为解决评估标准不统一的问题，研究界正积极构建标准化框架和数据集。**SenseFi**是一个基于PyTorch的开源Wi-Fi感知深度学习库，旨在为不同模型提供一个公平的性能比较平台。同时，**EHUNAM**等综合性公共CSI数据集的发布，为算法的训练和验证提供了宝贵资源。

### **3. 基于毫米波雷达的感知技术分析**

毫米波雷达因其高分辨率、保护隐私和抗环境干扰能力强的优点，在非接触式感知领域得到了广泛应用。

#### **3.1 核心输入信号**
毫米波雷达感知算法的输入数据形式多样，主要包括：
*   **点云（Point Clouds）**：提供目标在三维空间中的稀疏反射点，描述其形状和轨迹。
*   **距离-多普勒图（Range-Doppler Maps, RDM）**：以序列形式捕捉目标的距离和速度信息。
*   **距离-角度图（Range-Angle Maps, RAM）**：提供目标的距离和空间角度信息。
*   **多维张量/热力图**：融合距离、多普勒、角度、时间等多维度信息的数据立方体。

#### **3.2 SOTA算法性能评估（手势识别）**
在手势识别这一细分领域，毫米波雷达技术取得了极高的准确率。

| 算法模型 | 输入信号 | 性能指标（准确率） | 数据集（手势类别数） |
| :--- | :--- | :--- | :--- |
| **GRNet** | 4D TSTD 特征 | **99.64%** | 10种动态手势 |
| **ST-GCN** | 点云 | **99.2%** | 11种手势 |
| **DAR (3D-CNN+ConvLSTM)** | RDM 序列 | **99.2%** | 6种手势 |
| **CNN + LSTM** | 距离-多普勒-时间数据 | **98.8%** | 6种手势 |
| **3D-CNN (多种变体)** | RDM, RDT, 4D张量等 | **96.5% - 98.7%** | 7-15种手势 |

**分析：** 3D-CNN及其混合架构是处理毫米波雷达数据最主流且有效的模型。同时，专门处理点云数据的图卷积网络（GCN/ST-GCN）也展现出顶尖性能。然而，**必须指出，上述极高的准确率大多是在研究者自建的数据集上取得的**，这限制了算法间的直接可比性。

#### **3.3 其他应用场景（睡眠与驾驶员监控）**
毫米波雷达也被用于睡眠监测（如姿势转换、生命体征监测）和驾驶员监控。主流方法同样采用深度学习模型（如CNN）进行分析。尽管存在公开的睡眠姿势数据集，但研究资料**并未提供这些应用场景下SOTA算法具体的准确率或性能评估数据**，相关研究更多地集中在系统框架的搭建和可行性验证上。

### **4. 基于视觉信号的感知技术分析：远程生命体征测量（rPPG）**

rPPG技术通过标准摄像头分析人脸视频中由心跳引起的皮肤颜色细微变化，以非接触方式测量心率等生命体征。

*   **核心输入信号**：标准摄像头（如手机、网络摄像头）拍摄的面部视频。
*   **SOTA算法与评估**：当前SOTA算法以深度学习模型为主，如**DeepPhys、PhysNet**等时空卷积网络。研究重点已从单纯追求高精度转向提升模型在**复杂光照变化和头部运动**等干扰下的**鲁棒性**。
*   **性能指标**：rPPG的性能评估不常用分类准确率，而是采用信号处理领域的指标，如**信噪比（SNR）、皮尔逊相关系数（Pearson Correlation）、平均绝对误差（MAE）和均方根误差（RMSE）**。研究指出，部分模型（如PhysNet）可能存在与真实信号的“相位偏移”问题。然而，**本次研究未能从资料中获取这些顶尖算法在公开数据集（如UBFC-rPPG）上的具体量化性能数值**。

### **5. 多模态融合感知策略**

融合多种传感器的信息是克服单传感器局限性、提升系统整体性能的有效途径。

一项结合**毫米波雷达和摄像头**的室内占用检测与跟踪系统研究提供了具体案例。该系统利用毫米波雷达精确的测距测角能力和摄像头高分辨率的识别能力，通过特征级或决策级的融合策略，显著提升了感知的可靠性。在商业环境的测试中，该融合系统实现了**93.8%的总体检测准确率**，中位位置误差为1.7米，证明了多模态融合带来的性能增益。

### **6. 关键研究趋势与未来展望**

*   **智能反射面（IRS）**：通过可编程的超表面智能调控无线信号的传播路径，IRS技术有望从根本上优化感知环境，为Wi-Fi/RF感知带来性能上的飞跃。
*   **边缘计算与端侧AI**：将复杂的感知算法部署到靠近传感器的边缘设备（如Nvidia Jetson Nano）上，可以降低延迟、保护隐私。然而，边缘设备有限的计算能力是当前面临的主要挑战。
*   **从判别式到生成式AI**：以RF-Diffusion为代表的生成式模型的兴起，预示着AI在非接触式感知中的应用正从简单的“识别”走向更复杂的“理解与生成”，这对于解决数据稀缺问题具有重要意义。

### **结论**

非接触式感知技术在过去几年取得了显著进展，深度学习算法的广泛应用使其在多个场景下达到了极高的性能水平。基于Wi-Fi和毫米波雷达的技术路径已相对成熟，尤其在活动识别和手势识别等任务中准确率超过95%。然而，整个领域仍面临着标准化基准缺失的严峻挑战，这使得算法的横向比较与评估充满困难。

未来的发展将聚焦于提升系统在真实复杂环境中的鲁棒性、通用性和部署效率。多模态融合、智能反射面（IRS）和边缘计算将是实现这些目标的关键技术路径，而生成式AI的引入则为该领域开辟了新的想象空间。

---
**资料来源:** 报告内容完全基于项目提供的原始研究日志（Search Queries & Answers）进行综合分析与撰写。

## Citations 
- https://www.computer.org/csdl/journal/tm/2025/09/10964381/25UAatWZcOs
- https://www.sciencedirect.com/science/article/pii/S1389128625008734?dgcid=rss_sd_all
- https://www.techscience.com/cmc/v86n1/64495/html
- https://dl.acm.org/doi/10.1145/3714394.3754369
- https://www.researchgate.net/publication/397588254_Development_and_validation_of_a_multi-modal_contactless_sensing_system_for_surgical_risk_analysis_in_a_real-world_environment
- https://koara.lib.keio.ac.jp/xoonips/modules/xoonips/download.php/KO50002002-20256506-0003.pdf?file_id=191778
- https://www.tandfonline.com/doi/full/10.1080/10095020.2019.1612600
- https://www.scilit.com/publications/031b2caa79048fb153c5a9b505279816
- https://www.sciencedirect.com/science/article/pii/S2666389923000405
- https://github.com/NTUMARS/Awesome-WiFi-CSI-Sensing
- https://www.researchgate.net/publication/399197156_Wireless-Based_Human_Vital_Signs_Monitoring_Technology_and_Its_Applications
- https://www.nature.com/articles/s41597-025-06238-4
- https://colab.ws/articles/10.1109%2Ftmc.2025.3556674
- https://patents.google.com/patent/US10139916B2/en
- https://www.preprints.org/manuscript/202506.0794
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11985057/
- https://www.researchgate.net/publication/349747261_CNN-based_Driver_Monitoring_Using_Millimeter_Wave_Radar_Sensor
- https://pubmed.ncbi.nlm.nih.gov/40213044/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12181896/
- https://ieeexplore.ieee.org/document/10753140/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12227916/
- https://www.researchgate.net/publication/392867649_A_comprehensive_review_of_heart_rate_measurement_using_remote_photoplethysmography_and_deep_learning
- https://www.sciencedirect.com/science/article/abs/pii/S1746809423010418
- https://www.webpronews.com/mui-board-integrates-mmwave-radar-for-private-sleep-tracking-and-gestures/
- https://www.winmarketresearch.com/home/goods/detail/id/4183860.html
- https://ieeexplore.ieee.org/document/9753424/
- https://dl.acm.org/doi/10.1145/2942358.2942381
- https://www.researchandmarkets.com/reports/6055245/medical-millimeter-wave-radar-market-global?srsltid=AfmBOooPqqQ59zLsnwvbzEg54V1n8U2V2ytsAyKoHr3YfSKc_lefstAL
- https://www.researchgate.net/publication/354017154_Reduction_of_Motion_Artifacts_From_Remote_Photoplethysmography_Using_Adaptive_Noise_Cancellation_and_Modified_HSI_Model
- https://arxiv.org/pdf/2504.01774
- https://www.scitepress.org/PublicationsDetail.aspx?ID=6mh4QWP76X0=&t=1
- https://pubmed.ncbi.nlm.nih.gov/37943637/
- https://www.researchgate.net/publication/373130052_Deep_learning-based_image_enhancement_for_robust_remote_photoplethysmography_in_various_illumination_scenarios
- https://dl.acm.org/doi/10.1145/3749511
- https://escholarship.org/content/qt1s80d5r1/qt1s80d5r1.pdf
- https://dl.acm.org/doi/abs/10.1109/COMST.2024.3398004
- https://www.researchgate.net/publication/398897327_On_the_Relationship_Between_the_Properties_of_Non-Stationary_Radio_Channels_and_the_System_Functions_of_mmWave_LFMCW_Radars_in_Indoor_Environments
- https://www.mdpi.com/1424-8220/23/21/8901
- https://www.mdpi.com/2071-1050/14/9/5114
- https://www.researchgate.net/publication/383643448_A_mmWave_Sensor_and_Camera_Fusion_System_for_Indoor_Occupancy_Detection_and_Tracking
- https://www.researchgate.net/publication/364503356_mmWave_radar_tracking_and_sensor_fusion_with_camera
- https://www.ideals.illinois.edu/items/131962
- https://www.mdpi.com/1424-8220/22/7/2542
- https://www.nature.com/articles/s41597-025-06238-4
- https://sensys.acm.org/2026/cfp.html
- https://www.semanticscholar.org/paper/Research-Progress-in-Millimeter-Wave-Radar-Based-A-Wang-Luo/2964244ee085a6b57768baff9eb3dbcd3551d65b
- https://www.researchgate.net/publication/360036235_Research_Progress_in_Millimeter_Wave_Radar-Based_non-contact_Sleep_Monitoring_-_A_Review
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12197076/
- https://www.researchgate.net/publication/377995959_Intelligent_Reflecting_Surface_Aided_Wireless_Sensing_Applications_and_Design_Issues
- https://www.researchgate.net/publication/368474160_Intelligent_Reflecting_Surface_Aided_Wireless_Sensing_Applications_and_Design_Issues
- https://ieeexplore.ieee.org/iel8/9739/5451756/10812728.pdf
- https://public-pages-files-2025.frontiersin.org/journals/signal-processing/articles/10.3389/frsip.2023.1197240/pdf
- https://pmc.ncbi.nlm.nih.gov/articles/PMC9572609/
- https://dl.acm.org/doi/10.1145/3718958.3750474
- https://ui.adsabs.harvard.edu/abs/2019nsf....2000480W/abstract
- https://cse.msu.edu/~caozc/papers/tosn25-zhang.pdf
- https://www.winlab.rutgers.edu/~yychen/daisylab/journal.html
- https://arxiv.org/html/2409.16209v2
- https://cswu.me/
- https://www.scribd.com/document/744419496/2403-04333
- https://www.researchgate.net/publication/386454535_A_Survey_of_Wireless_Sensing_Security_from_a_Role-Based_View_Victim_Weapon_and_Shield
- https://isac.committees.comsoc.org/wp-content/uploads/sites/147/2023/05/ISAC-Focus_Issue6_0520.pdf
- https://www.researchgate.net/publication/394618606_Low-Cost_Wi-Fi_Sensing_Challenges_Advances_and_a_Framework_for_Edge_Deployment
- https://www.cs.cmu.edu/~jingaox/assets/pdf/papers/mobicom24_rfdiffusion.pdf
- https://arxiv.org/abs/2404.09140