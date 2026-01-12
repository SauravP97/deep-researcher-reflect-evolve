# 软件行业未来趋势和被AI替代的可能性

好的，作为首席研究编辑，我将根据提供的原始研究主题、最终执行计划以及所有原始研究笔记，为您撰写一份全面、专业的深度研究报告。

---

# **软件行业未来趋势深度报告：AI驱动下的角色演变与风险应对**

## **摘要 (Executive Summary)**

本报告深度剖析了软件行业的未来趋势，并系统性评估了人工智能（AI）对从业者角色的潜在影响。研究的核心结论是：**软件行业当前及未来的主要矛盾是大规模、结构性的高端人才短缺，而非人才过剩。** 基于此前提，AI辅助软件工程（AASE）并非旨在“替代”开发者，而是作为应对人才缺口、提升行业整体生产力的关键工具。

然而，AASE工具的普及也暴露出了一系列有数据支撑的严峻风险。实证研究显示，AI编程助手可能导致任务完成时间增加19%的“效率陷阱”，其生成的代码中存在60-70%的最高级别安全漏洞，以及高达92%的不充分异常处理率。同时，“氛围编程”（vibe coding）现象正在催生开发者核心技能退化的风险。

因此，软件行业的未来范式并非简单的“人机替代”，而是深度复杂的“人机协作”。开发者的角色将从代码的“执行者”演变为更高层次的“监督者”、“架构师”和“系统设计师”。成功驾驭这一转变的关键在于：

1.  **采纳新的工作模式**：推广以“技术负责人监督AI初级工程师”为核心的协作流程。
2.  **建立严格的治理模型**：实施“混合代码审查”（AI自动化初审+人类专家复审）以系统性地规避AI带来的质量与安全风险。
3.  **重塑技能价值**：系统性思维、复杂问题分解能力、批判性思维及对AI产出的高效审查能力，将成为未来软件工程师的核心价值。

本报告旨在为个人开发者和企业提供清晰的战略蓝图，以应对挑战，抓住AI时代的结构性机遇。

## **核心发现 (Key Findings)**

1.  **核心矛盾是结构性人才短缺，而非人才过剩**：
    与普遍的“AI替代焦虑”相反，研究数据显示行业面临严峻的人才缺口。仅中国市场，2023年的数字人才缺口就高达2500万至3000万 [https://bimsa.net/doc/publication/15684.pdf]。人工智能、云计算、物联网等关键领域的人才供需比严重失衡，表明AI工具的出现是弥补劳动力缺口的关键解决方案，而非威胁。

2.  **AI辅助软件工程（AASE）的双刃剑效应已量化显现**：
    尽管AASE工具（如GitHub Copilot）市场渗透率极高，但其负面影响不容忽视：
    *   **效率陷阱**：独立研究指出，使用AI编程助手可能导致任务完成时间增加19%，开发者容易陷入主观感觉效率提升而客观生产率下降的“效率幻觉” [https://post.smzdm.com/p/apwq3d89, https://post.smzdm.com/p/an56le3v]。
    *   **严重安全与质量缺陷**：Sonar报告显示，AI生成的代码中60%-70%的安全漏洞为最高严重等级（BLOCKER），检出率比人工代码高2.3倍。同时，存在92%的不充分异常处理和远超阈值1763倍的认知复杂度等系统性工程质量问题 [https://cloud.tencent.com/developer/article/2555208]。
    *   **开发者技能退化风险**：过度依赖导致“氛围编程”（vibe coding）现象蔓延，开发者陷入“提问-获取答案”的浅层循环，削弱了其深度思考、调试和问题分解等核心能力，催生“伪开发者” [https://post.smzdm.com/p/an56le3v]。

3.  **行业未来是“人机协作”，而非“人机替代”**：
    AI的角色定位是一个知识渊博但缺乏项目背景的“资深初级工程师”，而人类开发者则升级为“技术负责人”。在这种模式下，开发者的核心工作从编写每一行代码，转变为将复杂问题分解为AI可执行的任务、监督AI的产出质量、并专注于系统架构、安全保障和业务创新等更高价值的活动。

4.  **软件行业自身技术趋势与AASE深度融合**：
    AASE正作为催化剂，加速软件行业其他核心技术趋势的演进。它与云原生（Cloud-Native）结合催生AIOps；赋能低代码/无代码（LC/NC）平台处理更复杂的逻辑，实现开发普惠化；并深度集成于DevSecOps流水线，通过自动化安全审计缓解专业人才不足的压力。

---

## **深度分析 (Detailed Analysis)**

### **第一章：软件行业宏观背景：增长、趋势与人才缺口**

**市场持续高速增长**
全球软件市场正经历强劲增长。预计规模将从2026年的9263.4亿美元增长至2034年的22122.1亿美元，复合年增长率（CAGR）高达11.5% [https://www.fortunebusinessinsights.com/zh/software-market-111481]。中国市场同样表现出色，工业软件、数据仓库等细分领域均保持高速增长 [https://blog.csdn.net/Wnq10072/article/details/148176819]。

**核心技术与商业模式演进**
行业的核心驱动力是数字化转型以及云计算、大数据和AI等技术的融合 [https://pdfs.cir.cn/ITTongXun/68/%E8%BD%AF%E4%BB%B6%E8%A1%8C%E4%B8%9A%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A_1A11368.pdf]。开发模式正从DevOps向更安全的DevSecOps及更关注开发者体验的平台工程（Platform Engineering）演进。商业模式上，基于云的SaaS订阅制和按量付费的消费制已成为主流。

**结构性人才短缺是根本前提**
行业增长的最大制约因素是熟练专业人才的短缺 [https://www.fortunebusinessinsights.com/zh/software-market-111481]。量化数据显示：
*   **中国总体缺口**：2023年达2500万-3000万人 [https://bimsa.net/doc/publication/15684.pdf]。
*   **细分领域缺口**：
    *   **人工智能**：2023年人才供需比低至0.39，即每5个岗位争夺2名人才 [https://jsfz.luas.edu.cn/_upload/article/files/47/64/9f950da64fc18ac1439b41b5f09b/21a6d282-8861-44b2-9eca-ea5c994cb8e1.pdf]。
    *   **云计算**：预计到2024年，人才缺口将扩大至446万人 [https://e.huawei.com/marketingcloud/pep/asset/20000001/Material/880481f0c28b4a6c99f383723d533ce5/M1T1A669N798852809802465317/%E4%B8%AD%E5%9B%BDICT%E4%BA%BA%E6%89%8D%E7%94%9F%E6%80%81%E7%99%BD%E7%9A%AE%E4%B9%A6.pdf]。
    *   **物联网**：预计到2024年，缺口将达到336万人 [https://e.huawei.com/marketingcloud/pep/asset/20000001/Material/880481f0c28b4a6c99f383723d533ce5/M1T1A669N798852809802465317/%E4%B8%AD%E5%9B%BDICT%E4%BA%BA%E6%89%8D%E7%94%9F%E6%80%81%E7%99%BD%E7%9A%AE%E4%B9%A6.pdf]。

这一核心前提确立了AASE工具的根本价值定位：**赋能现有开发者，弥补人才鸿沟**。

### **第二章：AI辅助软件工程（AASE）的机遇与严峻挑战**

AASE指利用AI技术增强软件开发全生命周期，其核心技术为基于Transformer架构的大语言模型（LLM）。

**机遇：主流工具普及与应用场景分化**
AASE工具已广泛普及，以GitHub Copilot为首，其月活跃用户超过1500万 [developer.volcengine.com/articles/7386867728508715017]。市场呈现多元化格局，包括主流付费工具（Copilot、Tabnine、Amazon CodeWhisperer），强有力的免费竞争者（Codeium），以及重要的区域性替代品（豆包 MarsCode）。

同时，工具的应用场景出现分化：
*   **通用生产力增强**：GitHub Copilot等工具专注于日常开发，提供代码补全、函数生成、代码解释等功能，旨在提升开发效率。
*   **复杂问题解决**：Google的AlphaCode 2（基于Gemini模型）则专注于解决复杂的竞争性编程问题，其能力在Codeforces等平台得到验证，表现优于85%的人类参赛者 [https://blog.csdn.net/qq_22866291/article/details/145525936]。这代表了AI在程序综合（Program Synthesis）领域的尖端水平。

**挑战：量化的风险深度剖析**
尽管潜力巨大，但AASE的广泛应用带来了必须正视的、有数据支撑的风险：
1.  **效率陷阱**：研究表明，修改AI生成的代码所需的时间有时超过从头编写，导致任务完成时间反而增加19%。开发者主观感觉效率提升，但客观生产率下降，形成“效率幻觉” [https://post.smzdm.com/p/apwq3d89]。
2.  **代码质量与安全风险**：Sonar的报告揭示了AI代码的严重缺陷 [https://cloud.tencent.com/developer/article/2555208]：
    *   **高危漏洞**：60-70%的漏洞为BLOCKER级别，最常见的包括注入类漏洞和硬编码凭证。
    *   **工程纪律薄弱**：92%的代码未能妥善处理`NullPointerException`等常见异常，严重缺乏工程鲁棒性。
    *   **认知复杂度**：GPT-4o生成的代码平均认知复杂度超过推荐阈值的1763倍，为长期维护埋下隐患。
3.  **开发者技能退化**：过度依赖AI工具进行“氛围编程”（vibe coding）——即通过模糊的自然语言提示生成代码，而开发者不完全理解其底层逻辑——正在削弱开发者的核心工程能力，如调试、算法思维和系统性问题分解能力 [https://post.smzdm.com/p/an56le3v]。

### **第三章：未来范式：角色演变与治理模型**

面对AASE的挑战，行业必须转向更成熟的人机协作范式，重塑开发者角色并建立相应的治理模型。

**开发者角色的重塑：从执行者到监督者**
AI不会替代所有开发者，但会重塑其工作内容。低层次的编码任务自动化程度会越来越高，而人类的价值将向高阶抽象能力迁移：
*   **初级工程师**：传统的编码成长路径受挑战，需更快转向系统理解和调试等综合能力。
*   **测试与运维（QA/SRE）工程师**：AI将极大增强自动化测试、缺陷检测和AIOps能力，其角色将转向设计更智能的测试策略和运维系统。
*   **系统架构师/技术负责人**：角色价值空前提升。他们从日常编码中解放出来，专注于系统设计、技术选型、复杂问题分解，并承担监督和审查AI产出质量的核心职责。

“**技术负责人监督AI初级工程师**”将成为未来团队的核心协作模式。人类专家负责定义需求、设计架构，AI负责生成初始代码，人类再进行审查、调试和集成。

**关键应对策略：混合代码审查与新技能培养**
为系统性地应对AASE风险，必须建立新的治理和发展策略：
1.  **混合代码审查 (Hybrid Code Review)**：这是应对AI代码质量和安全风险的首要最佳实践。流程应为“AI自动化初审+人类专家复审”。AI工具（如Snyk Code, Amazon Q）负责大规模、快速地扫描常见漏洞、代码异味和反模式，而人类专家则专注于审查复杂的业务逻辑、架构合理性和AI难以判断的边缘情况。
2.  **新技能价值凸显**：AI时代，价值最高的技能不再是编码速度，而是：
    *   **系统性思维与问题分解**：将复杂业务需求拆解为AI可理解和执行的清晰模块。
    *   **批判性思维**：对AI的建议和生成内容进行严格的审视、验证和质疑。
    *   **高效审查能力**：快速识别AI生成代码中的缺陷、漏洞和长期风险。
3.  **教育体系改革**：计算机教育需从单纯的编码技能训练，转向系统设计、工程思维和批判性思维的培养，防止产生只会用自然语言描述问题但无法从根本上解决问题的“伪开发者”。

### **第四章：技术融合的协同效应**

AASE并非孤立发展，它正与软件行业的其他主流趋势深度融合，产生协同效应：
*   **AASE + 低代码/无代码 (LC/NC)**：生成式AI为LC/NC平台注入了革命性动力，用户可通过自然语言生成应用，使平台能处理更复杂的逻辑，真正实现“开发民主化”，并缓解开发者短缺的压力。
*   **AASE + DevSecOps**：AI工具被集成到CI/CD流水线中，自动化执行静态/动态安全测试（SAST/DAST）和威胁建模，实现“安全左移”，构建智能化的安全防线。
*   **AASE + 云原生**：AI反向赋能云原生运维，AIOps能够实现复杂云环境的智能调度、故障诊断和资源优化，提升系统稳定性和效率。
*   **Web3与区块链**：作为去中心化应用的底层技术，Web3是行业一个潜在的远期发展方向。但目前仍面临监管、成本、用户采纳和商业模式不明确等多重落地挑战，其发展成熟度远低于上述趋势。

## **结论与展望 (Conclusion & Outlook)**

软件行业的未来并非由“AI替代人类”的零和博弈所定义，而是由“AI辅助人类应对人才短缺”这一核心议题所驱动。AI正成为一把锋利的双刃剑，既是前所未有的生产力放大器，也带来了可量化的质量、安全和技能退化风险。

**未来发展蓝图**
*   **短期 (1-3年)**：AASE工具作为生产力增强器全面普及，成为开发者标准配置。“混合代码审查”和新的团队协作模式开始落地，以规避初期风险。
*   **中期 (3-10年)**：AI在测试、运维、前端开发等特定领域实现高度自主化，显著缓解人才瓶颈。AI Agent成为软件应用的核心组件，行业焦点转向多智能体协同和长程推理认知。
*   **长期 (10年以上)**：通用人工智能（AGI）或将颠覆软件创造的范式，“智能体即应用”（Agent as Application）可能成为主流，软件开发成本趋近于零，引发商业模式的根本性变革。

**战略建议**
*   **对个人开发者**：
    1.  **拥抱而非抗拒**：熟练掌握至少一种主流AASE工具，将其内化为工作流的一部分。
    2.  **转变角色定位**：主动从“编码者”向“技术负责人”转型，训练自己分解问题、定义任务和审查结果的能力。
    3.  **投资高阶技能**：持续学习系统设计、架构、网络安全和复杂调试，这些是AI短期内无法替代的核心价值。

*   **对企业**：
    1.  **建立治理体系**：立即推行“混合代码审查”流程，将AI生成的代码纳入最严格的质量与安全管控之下。
    2.  **重构团队与流程**：试点“技术负责人监督AI”模式，优化开发流程，提升精英人才的杠杆效应。
    3.  **投资人才培养**：调整内部培训体系，鼓励员工具备批判性思维和AI协作能力，构建能够驾驭AI而非被其削弱的韧性人才战略。

最终，能否在AI时代保持竞争力的关键，在于我们能否超越对“代码生成”的浅层迷恋，转而建立起一套成熟、审慎且高效的人机协作与治理体系。

---

## **参考资料 (References/Sources)**

*   <https://www.fortunebusinessinsights.com/zh/software-market-111481>
*   <https://blog.csdn.net/Wnq10072/article/details/148176819>
*   <https://pdfs.cir.cn/ITTongXun/68/%E8%BD%AF%E4%BB%B6%E8%A1%8C%E4%B8%9A%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A_1A11368.pdf>
*   <https://bimsa.net/doc/publication/15684.pdf>
*   <https://jsfz.luas.edu.cn/_upload/article/files/47/64/9f950da64fc18ac1439b41b5f09b/21a6d282-8861-44b2-9eca-ea5c994cb8e1.pdf>
*   <https://e.huawei.com/marketingcloud/pep/asset/20000001/Material/880481f0c28b4a6c99f383723d533ce5/M1T1A669N798852809802465317/%E4%B8%AD%E5%9B%BDICT%E4%BA%BA%E6%89%8D%E7%94%9F%E6%80%81%E7%99%BD%E7%9A%AE%E4%B9%A6.pdf>
*   <https://developer.volcengine.com/articles/7386867728508715017>
*   <https://blog.csdn.net/qq_22866291/article/details/145525936>
*   <https://post.smzdm.com/p/apwq3d89>
*   <https://post.smzdm.com/p/an56le3v>
*   <https://cloud.tencent.com/developer/article/2555208>
*   所有其他在研究日志中引用的URL。

## Citations 
- https://pdfs.cir.cn/ITTongXun/68/%E8%BD%AF%E4%BB%B6%E8%A1%8C%E4%B8%9A%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A_1A11368.pdf
- https://www.fortunebusinessinsights.com/zh/software-market-111481
- https://www.infoq.cn/minibook/j5EAaLjyiMN48OmOjGaT
- https://blog.csdn.net/Wnq10072/article/details/148176819
- https://pdf.dfcfw.com/pdf/H3_AP202212071580887280_1.pdf
- https://www.shaqiu.cn/article/pJgjLm6NV4BO
- https://cloud.tencent.com/developer/article/2346749
- https://04665u.npoall.com/news/itemid-25430.html
- https://aise.phodal.com/ai4se.html
- https://aise.phodal.com/design-aise.html
- https://www.cisco.com/c/dam/global/zh_cn/about/csr/net_acad/pdf/greater_china_whitepaper_chinese.pdf
- https://economicgraph.linkedin.com/content/dam/me/economicgraph/en-us/download/china-digital-economy-talent-report.pdf
- https://www.tsinghua.edu.cn/__local/4/E6/DA/A12EB75B9D564353167D4F107C5_D711D7DB_79EC7D.pdf
- https://bimsa.net/doc/publication/15684.pdf
- https://e.huawei.com/marketingcloud/pep/asset/20000001/Material/880481f0c28b4a6c99f383723d533ce5/M1T1A669N798852809802465317/%E4%B8%AD%E5%9B%BDICT%E4%BA%BA%E6%89%8D%E7%94%9F%E6%80%81%E7%99%BD%E7%9A%AE%E4%B9%A6.pdf
- https://jsfz.luas.edu.cn/_upload/article/files/47/64/9f950da64fc18ac1439b41b5f09b/21a6d282-8861-44b2-9eca-ea5c994cb8e1.pdf
- https://www.fangzhenxiu.com/post/14173821/?uri=9cqwx99Uken%20%E4%BD%9C%E8%80%85%EF%BC%9A%E4%BB%BF%E7%9C%9F%E7%A7%80%20https%3A%2Fwww.bilibili.com%2Fread%2Fhttps%3A%2Fwww.fangzhenxiu.com%2Fcourse%2F9107400
- https://www.opensourceway.community/tags/%E5%BC%80%E6%BA%90%E4%B9%8B%E9%81%93/
- https://zhuanlan.zhihu.com/p/458046979
- https://zhuanlan.zhihu.com/p/630213524
- https://www.51cto.com/article/771744.html
- https://blog.csdn.net/weixin_48576413/article/details/145883475
- https://blog.csdn.net/fq1986614/article/details/149139622
- https://www.reddit.com/r/programming/comments/1620w1d/10_ai_coding_assistant_tools_compared_github/?tl=zh-hans
- https://www.cnblogs.com/wangxi01/p/18896858
- https://www.reddit.com/r/programming/comments/x41v4z/github_copilot_vs_tabnine_choose_the_best_ai/?tl=zh-hans
- https://blog.csdn.net/2301_82242750/article/details/145762826
- https://blog.csdn.net/Frankabcdefgh/article/details/147630669
- https://blog.csdn.net/qq_38998213/article/details/149328322
- https://blog.csdn.net/2503_92604243/article/details/149674287
- https://juejin.cn/post/7229976104009236536
- https://zhuanlan.zhihu.com/p/676257615
- http://9f339.jxycyx.com/article/2026-01-05_4868e.html
- https://www.cncso.com/google-gemini-ai-mega-model-surpasses-chatgpt-on-all-fronts.html
- https://www.wenxiaobai.com/api/expends/detail?article=8e7ddade-350a-4676-994c-f52426d2d1ab
- https://www.reddit.com/r/programming/comments/x41v4z/github_copilot_vs_tabnine_choose_the_best_ai/?tl=zh-hans
- https://blog.csdn.net/Frankabcdefgh/article/details/147630669
- https://zhuanlan.zhihu.com/p/630213524
- https://www.ruanyifeng.com/blog/2024/07/copilot-vs-marscode.html
- https://blog.csdn.net/weixin_30205153/article/details/147184495
- https://www.scribd.com/document/750770862/%E5%9F%BA%E4%BA%8E%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E7%9A%84%E7%A8%8B%E5%BA%8F%E5%90%88%E6%88%90%E7%A0%94%E7%A9%B6%E8%BF%9B%E5%B1%95-%E8%8B%9F%E5%80%A9%E6%96%87
- https://developer.volcengine.com/articles/7386867728508715017
- https://aicoding.csdn.net/69631a736554f1331aa12ec7.html
- https://medium.com/@kaushikvikas/ai-powered-development-a-comparative-study-of-amazon-codewhisperer-github-copilot-and-tabnine-df21c0649f76
- https://post.smzdm.com/p/apwq3d89
- https://www.reddit.com/r/programming/comments/1620w1d/10_ai_coding_assistant_tools_compared_github/?tl=zh-hans
- http://gotc2023.oschina.net/
- https://pdf.dfcfw.com/pdf/H3_AP202209061578069134_1.pdf
- https://developer.aliyun.com/article/1246873
- https://blog.csdn.net/GanKuRenSheng/article/details/148292828
- https://www.gminsights.com/zh/industry-analysis/low-code-development-platform-market
- https://my.idc.com/getdoc.jsp?containerId=prCHC52441824
- https://pdf.dfcfw.com/pdf/H3_AP202212061580867579_1.pdf
- https://blog.csdn.net/2501_91226441/article/details/146938006
- https://www.primeton.com/blog/49485.html
- https://blog.csdn.net/2301_79342058/article/details/147806899
- https://www.iplaysoft.com/marscode.html
- https://zhuanlan.zhihu.com/p/663898339
- https://www.ruanyifeng.com/blog/2024/07/copilot-vs-marscode.html
- https://www.scribd.com/document/908520005/%E5%A4%A7%E6%A8%A1%E5%9E%8B%E8%BE%85%E5%8A%A9%E7%BC%96%E7%A8%8B%E6%89%8B%E5%86%8C
- https://www.reddit.com/r/dotnet/comments/1bpdrpq/codeium_or_github_copilot_which_one/?tl=zh-hans
- https://post.smzdm.com/p/apwq3d89
- https://baoyu.io/?page=15
- https://post.smzdm.com/p/an56le3v
- https://blog.csdn.net/jsntghf/article/details/150463183
- https://cloud.tencent.com/developer/article/2555208
- https://limboy.me/docs/research-the-rise-of-ai-coding-agents-and-its-profound-impact
- https://github.com/ChanceYu/front-end-rss/blob/master/details/%E5%89%8D%E7%AB%AF%E6%97%A9%E8%AF%BB%E8%AF%BE.md
- https://www-file.huawei.com/-/media/corp2020/pdf/publications/cloud-plus/cloud_plus_19_cn.pdf
- https://aise.phodal.com/aise-code-review.html
- https://docs.aws.amazon.com/zh_cn/amazonq/latest/qdeveloper-ug/code-reviews.html
- https://zhuanlan.zhihu.com/p/1976689424361351046?share_code=IwvahfLGBw9O&utm_psn=1979500321140151782
- https://www.reddit.com/r/ExperiencedDevs/comments/1grd2d9/whats_your_experience_with_aibased_code_review/?tl=zh-hans
- https://juejin.cn/post/7415914059106418751
- https://www.reddit.com/r/ClaudeAI/comments/1jhtrn0/vibe_coding_is_actually_great/?tl=zh-hans
- https://aicoding.csdn.net/69192ebc0e4c466a32e85489.html
- https://blog.csdn.net/asce1885/article/details/155151150
- https://blog.csdn.net/u013134676/article/details/156040287
- https://news.qq.com/rain/a/20241125A00N2H00
- https://www.aigcopen.com/content/corporate_news/31802.html
- https://zhuanlan.zhihu.com/p/1936132427832599304
- https://zhuanlan.zhihu.com/p/665444701
- https://ojs.vitu-pub.com/index.php/jyfzycxx/article/viewFile/149663/148683
- https://www.sciscanpub.com/index/index/show_article/id/8444.html
- https://blog.csdn.net/yuntongliangda/article/details/149115067
- https://www.ccf.org.cn/CCF_BC/activities/BLS/2023-11-15/798154.shtml
- https://zhuanlan.zhihu.com/p/1941063239015335719
- https://blog.csdn.net/weixin_44821345/article/details/153154119
- https://www.phodal.com/blog/ai4se-trends-2025/
- https://www.cnblogs.com/txw1958/p/18791536
- https://cloud.tencent.com/developer/article/2574609
- https://blog.csdn.net/qq_22866291/article/details/145525936
- https://cloud.tencent.com/developer/article/1510754
- https://zhuanlan.zhihu.com/p/1936876151021741674
- https://30295522.s21i.faiusr.com/61/ABUIABA9GAAg1rvixgYo_KK7zgc.pdf
- https://www-file.huawei.com/admin/asset/v1/pro/view/39056d5bf2c5412f93d58026c146308c.pdf
- https://www.bagevent.com/event/8988232/p/555582
- https://www.crypto-dam.com/wp-content/uploads/2025/06/Web3%E5%8D%80%E5%A1%8A%E9%8F%88%E8%B3%BD%E9%81%93%E8%A1%8C%E6%A5%AD%E5%A0%B1%E5%91%8A.pdf
- https://www.scribd.com/document/916072412/20250731-%E5%85%A8%E7%90%83Web3-0%E6%8A%80%E6%9C%AF%E4%BA%A7%E4%B8%9A%E7%94%9F%E6%80%81%E5%8F%91%E5%B1%95%E6%8A%A5%E5%91%8A-2024%E5%B9%B4
- https://www.beijing.gov.cn/ywdt/gzdt/202305/P020230529616313576667.pdf
- https://www.gfnds.com/uploads/20250818/735bfbac582b224666297c35c70cfc74.pdf
- https://www.fisco.com.cn/upload/files/20241224/1735026089203663.pdf
- https://assets.fenwick.com/legacy/FenwickDocuments/Blockchain-Compliance-Whitepaper-3-0.pdf
- https://www.china-cic.cn/upload/202012/05/4e4d16d7e620490db221f2cb0446f2a7.pdf
- https://www.zhonglun.com/upload/report/05.pdf
- https://assets.kpmg.com/content/dam/kpmg/cn/pdf/zh/2020/10/china-regulatory-sandbox-innovation-and-practice-report.pdf
- https://www.sciengine.com/parse/pdf/1002-0306/21C4D31F86204ADDA30B0528D1B7F11F.pdf