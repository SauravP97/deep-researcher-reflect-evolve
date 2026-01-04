# 调研国内金融机构之间的投资借贷关系与系统性风险的联系？对不同层次或类型的借贷关系和风险建模

好的，作为首席研究编辑，我将根据您提供的原始研究主题、最终执行计划以及详细的原始研究笔记，编写一份全面、专业的深度研究报告。

---

### **深度研究报告：中国金融机构投资借贷关系与系统性风险建模分析**

**报告日期：** 2024年10月27日
**报告ID：** AI-DSR-241027-CNFIN-RISK
**研究服务：** 自主AI研究服务

---

#### **执行摘要 (Executive Summary)**

本报告旨在深入分析中国国内金融机构间的投资借贷关系与系统性风险的内在联系，并探讨其风险建模框架。研究发现，中国的系统性风险评估与管理已形成一套以**宏观情景压力测试**为核心的官方框架，该框架由中国人民银行通过其年度《中国金融稳定报告》权威发布。

风险主要通过**信用风险**渠道传导，尤其是在房地产、地方政府债务和中小微企业等领域。虽然银行同业间的直接传染风险被评估为相对可控，但由证券、保险等非银机构引发的**跨行业风险传染**被识别为系统性风险的关键放大器。

本研究的核心发现是确认了一个可用于模型校准的官方量化基准：根据《中国金融稳定报告（2023）》，在**2024年GDP增速降至1.9%的重度冲击情景（输入）下，19家国内系统重要性银行（D-SIBs）的总体资本充足率将在2025年末精确下降至12.66%（输出）**。这一基准为任何旨在模拟中国金融系统脆弱性的实证模型提供了核心验证标准。

监管体系通过**D-SIBs附加监管要求**（如差异化资本要求、恢复与处置计划）和**金融稳定保障基金**等制度安排，构建了多层次的风险缓释防线，以维护金融体系的整体稳定。

---

#### **核心发现 (Key Findings)**

1.  **官方评估框架：以宏观情景压力测试为核心**
    中国官方对系统性风险的评估并未依赖于对单一金融工具或机构的微观建模，而是采取了自上而下的宏观审慎视角。其核心工具是**宏观情景压力测试**，主要应用于国内系统重要性银行（D-SIBs），通过模拟宏观经济（如GDP增速）在轻、中、重度冲击下的表现，来评估核心金融机构的资本充足率变化和损失吸收能力。

2.  **关联网络结构：四大渠道与核心参与者**
    国内金融机构间的投资借贷关系构成了复杂的关联网络，主要通过以下四大渠道形成：
    *   **银行间市场与债券市场**：作为核心枢纽，承载了机构间的资金融通、债券交易和流动性管理功能。
    *   **资产管理业务**：特别是资产证券化，作为跨机构的连接纽带，加强了银行、券商、信托等机构间的资产与风险联系。
    *   **股权投资**：形成了金融机构间，特别是大型金融集团内部更深层次的协同与关联。
    *   网络的核心参与者是**19家国内系统重要性银行（D-SIBs）**，它们因其规模、关联度和复杂性，成为系统性风险管理和监管的焦点。其他参与者包括国有大行、股份制银行、城商行/农商行以及券商、保险、基金等非银金融机构。

3.  **风险传导机制：信用风险主导与跨行业传染放大**
    系统性风险在中国金融体系内主要通过三大机制传导：
    *   **直接传染**：单一机构的资产负债表收缩可能引发连锁反应。
    *   **跨部门违约风险**：风险从实体部门（尤其是房地产和地方政府债务）向金融体系传递。房地产相关贷款被视为当前最大的“灰犀牛”。
    *   **资产共通性**：多家机构持有相似资产，在市场冲击下可能同时遭受损失。
    压力测试结果明确指出，**信用风险**是影响银行资本水平的最主要因素，而市场风险影响有限。尤其值得关注的是，虽然银行同业间的直接传染风险被证明是可控的，但**来自证券业和保险业的风险向银行业的传染会显著放大系统性风险**。

4.  **监管与缓释体系：D-SIBs框架与金融稳定保障基金**
    为应对系统性风险，监管机构已建立起一套多层次的宏观审慎管理框架：
    *   **D-SIBs附加监管**：对认定的D-SIBs提出差异化的附加资本和杠杆率要求，并强制要求制定“恢复与处置计划”（即“生前遗嘱”），以增强其自救能力和有序处置能力，切断风险传播链。
    *   **金融稳定保障基金**：作为处置金融风险的最后一道防线，其资金使用顺位在机构自救、市场化资金和存款保险等行业保障基金之后，为极端情况下的系统稳定提供最终保障。

---

#### **深度分析 (Detailed Analysis)**

**1. 核心建模基准：官方压力测试的量化输入与输出**

本研究最重要的发现是，基于《中国金融稳定报告（2023）》的数据，我们得以确认一个精确的、可用于模型校准的宏观输入-输出关系。这为所有后续的实证建模提供了权威基准。

*   **输入（重度冲击情景）**：
    *   **核心宏观变量**：假设2024年国内生产总值（GDP）同比增长速度放缓至**1.90%**。
    *   **其他变量**：同时假设短期市场利率上升，信用利差扩大，并设置了更严格的流动性测试参数。

*   **输出（D-SIBs资本充足率变化）**：
    *   **初始状态**：19家国内系统重要性银行（D-SIBs）在2022年末的整体资本充足率为**16.29%**。
    *   **最终结果**：在上述重度冲击情景下，至2025年末，其整体资本充足率预计将精确下降至**12.66%**。

这一结果表明，尽管资本水平显著下降了3.63个百分点，但整体仍高于监管最低要求，显示出核心银行体系具备较强的风险抵御能力。任何旨在评估中国系统性风险的实证模型，其首要任务应是能够**精确复现**这一输入-输出关系。

**2. 风险传导路径的量化拆解**

官方压力测试不仅给出了总体结果，还对不同风险渠道的影响进行了量化拆解，揭示了风险传导的主次关系。

*   **信用风险传导**：这是资本损耗的主要来源。宏观经济下行通过企业和个人违约率上升，转化为银行不良贷款率攀升，最终侵蚀银行资本。在特定领域敏感性测试中，其冲击效果显著：
    *   **中小微企业贷款**：若中小微企业及个人经营性贷款不良率上升600%，参试银行整体资本充足率将骤降4.48个百分点至10.59%。
    *   **地方政府融资平台**：若融资平台不良率上升至15%，整体资本充足率将下降0.69个百分点。
    *   **房地产贷款**：尽管报告认为风险总体可控，但国有大行2023年对公房地产不良贷款率普遍在5%以上，远高于平均水平，显示该领域仍是信用风险的关键集聚点。（注：研究资料未提供重度压力情景下房地产贷款不良率的具体变化参数）。

*   **市场风险传导**：影响极为有限。利率和信用利差变动导致的债券估值下降，使D-SIBs整体资本充足率累计下降0.16个百分点；而利率上升带来的利息净收入增加，又使其上升0.07个百分点。两者对冲后，**利率相关市场风险的净影响仅为-0.09个百分点**。汇率变化影响更小。

*   **机构间传染风险**：测试结果呈现出显著的结构性差异。
    *   **银行同业间传染**：风险较低。在对60家银行的测试中，**任意单家银行违约均不会引起交易对手的接续违约**。
    *   **跨行业传染（非银→银行）**：风险显著放大。当**证券公司或保险公司**作为初始违约方时，银行间的风险传染性会**显著增强**，最高传染轮数增加至2轮。这表明银行通过资金融通、资产管理等业务与非银机构形成的借贷关系，是系统性风险的关键传导渠道。

---

#### **结论与展望 (Conclusion & Outlook)**

本报告系统性地梳理了中国金融机构间的投资借贷关系与系统性风险的联系。研究表明，中国的系统性风险评估与管理已经从定性描述转向了以**宏观情景压力测试**为核心的量化分析框架。

**核心结论**在于，系统性风险的主要驱动力是源于实体经济的**信用风险**，而**跨行业传染**（特别是从证券和保险业到银行业）是风险在金融体系内放大的关键环节。相比之下，传统的银行同业间直接传染风险已得到较好控制。

**未来展望**方面，本报告确认的**“1.9% GDP增长 → 12.66% D-SIBs资本充足率”**这一官方量化基准，为学术界和业界构建更精确的实证模型提供了坚实的校准目标。未来的研究应集中于构建能够复现此结果的简化模型，并利用该模型进一步评估关键监管政策（如D-SIBs附加资本要求、恢复与处置计划、金融稳定保障基金）在不同压力情景下的风险缓释效果，从而为宏观审慎政策的持续优化提供前瞻性的量化支持。

---

#### **参考文献与数据来源 (References/Sources)**

*   中国人民银行，《中国金融稳定报告》系列，特别是2023年版。
*   《系统重要性银行评估办法》及《系统重要性银行附加监管规定（试行）》。
*   商业银行年度报告及Wind等金融数据库公开披露的数据。
*   相关监管机构公开文件及新闻稿。
    *   [https://www.nfra.gov.cn/chinese/docfile/2025/24172aeaeb86406ca096b7b6e54af21d.docx](https://www.nfra.gov.cn/chinese/docfile/2025/24172aeaeb86406ca096b7b6e54af21d.docx)
    *   [https://www.pbc.gov.cn/chubanwu/114566/114579/4356052/4356380/2021100915525242238.pdf](https://www.pbc.gov.cn/chubanwu/114566/114579/4356052/4356380/2021100915525242238.pdf)
    *   [https://reportify-1252068037.cos.ap-beijing.myqcloud.com/media/production/s_f3358c68_f3358c68419796e97100ab9437233589.pdf](https://reportify-1252068037.cos.ap-beijing.myqcloud.com/media/production/s_f3358c68_f3358c68419796e97100ab9437233589.pdf)
    *   [https://jrj.sh.gov.cn/SCDT197/20240813/9a49d9d5ee6b4bf49857bae8e9f88b1e.html](https://jrj.sh.gov.cn/SCDT197/20240813/9a49d9d5ee6b4bf49857bae8e9f88b1e.html)
    *   [https://www.hankunlaw.com/upload/newsAndInsights/65a712e236a427c5fbdc103cc6ba20dd.pdf](https://www.hankunlaw.com/upload/newsAndInsights/65a712e236a427c5fbdc103cc6ba20dd.pdf)

## Citations 
- https://chinaifs.org.cn/upload/1/editor/1730241589839.pdf
- https://www.pbc.gov.cn/eportal/fileDir/image_public/UserFiles/goujisi/upload/File/%E5%9B%BD%E9%99%85%E6%B8%85%E7%AE%97%E9%93%B6%E8%A1%8C%E7%AC%AC82%E6%9C%9F%E5%B9%B4%E6%8A%A5%EF%BC%88%E4%B8%AD%E6%96%87%EF%BC%89.pdf
- https://www.econ.sdu.edu.cn/__local/2/B2/29/8E21DC87D341C8B679F95C2336F_A261B3FF_219D0F4.pdf?e=.pdf
- https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/2025122616592613805/2025123019161895262.pdf
- https://finance.sina.cn/bank/yhgd/2023-01-18/detail-imyaqvkp5613461.d.html?vt=4&cid=79649&node_id=79649
- https://file.iyanbao.com/pdf/92047-3213af1a-e355-4b2e-9542-a4d974b1bf49.pdf
- https://r.img.cctvpic.com/photoAlbum/page/20231222/2023122218161782885.pdf?spm=C73544894212.P59511941341.0.0&file=2023122218161782885.pdf
- https://www.cjcci.org/cj_pdf/2024bs/china/2024_All_CN.pdf
- https://www.shmet.com/news/newsDetail-2-881844.html
- https://www.imf.org/-/media/files/publications/cr/2017/chinese/cr17359c.pdf
- https://www.investor.org.cn/xxzx/tjzl/tjnrgmjytx/bk/kj/202302/P020230228412257379005.pdf
- https://www2.ccb.com/chn/company/gsjgsy/cpfw/tzyx/zczqh/index.shtml
- https://www.pbc.gov.cn/chubanwu/114566/114579/3842271/3842506/2019061117392776646.pdf
- https://www.group.citic/html/2025/News_1226/3116.html
- https://www.fitchbohua.cn/sites/default/files/2021-10/%E9%A6%96%E6%89%B9%E7%B3%BB%E7%BB%9F%E9%87%8D%E8%A6%81%E6%80%A7%E9%93%B6%E8%A1%8C%E7%AC%A6%E5%90%88%E9%99%84%E5%8A%A0%E8%B5%84%E6%9C%AC%E8%A6%81%E6%B1%82%E9%AB%98%E7%BB%84%E5%88%AB%E9%93%B6%E8%A1%8C%E8%B5%84%E6%9C%AC%E6%B0%B4%E5%B9%B3%E6%99%AE%E9%81%8D%E5%85%85%E8%B6%B3.pdf
- https://v.icbc.com.cn/userfiles/Resources/ICBC/haiwai/Asia/download/EN/2021/annual_report_2021en.pdf
- https://www.nfra.gov.cn/chinese/docfile/2025/24172aeaeb86406ca096b7b6e54af21d.docx
- https://www.pbc.gov.cn/chubanwu/114566/114579/4356052/4356380/2021100915525242238.pdf
- https://www.imf.org/-/media/files/publications/cr/2017/chinese/cr17358c.pdf
- https://finance.sina.com.cn/jjxw/2025-12-26/doc-inhecwfc2489841.shtml
- https://m.thepaper.cn/newsDetail_forward_32259167?from=sohu
- https://m.sohu.com/a/969750648_260616?scm=10001.325_13-325_13.0.0-0-0-0-0.5_1334
- https://www.pbc.gov.cn/jinrongwendingju/146766/146772/5a4efceedf4a4995a1441f0aca3ee3ab/2020122208471890109.pdf
- https://www.aof.org.hk/uploads/conference_detail/1564/0_-.pdf
- http://www.zgglkx.com/CN/10.16381/j.cnki.issn1003-207x.2015.10.004
- http://www.jryj.org.cn/CN/abstract/abstract937.shtml
- https://www.pbcsf.tsinghua.edu.cn/__local/8/CD/56/7325CD27538D62902F804C601ED_8B513D9F_F7911.pdf?e=.pdf
- http://www.nifd.cn/Uploads/Paper/c7e0acc6-2b7d-4463-b871-8eb7285a0cee.pdf
- https://finance.sina.cn/bank/yhgd/2021-04-14/detail-ikmxzfmk6724002.d.html
- https://www.sohu.com/a/420332619_530597
- https://view.inews.qq.com/a/20210414A03MCU00
- https://assets.kpmg.com/content/dam/kpmg/cn/pdf/zh/2024/06/china-banking-industry-survey-report-2024.pdf
- https://www.renrendoc.com/paper/463577794.html
- https://www.hkma.gov.hk/media/chi/publications-and-research/quarterly-bulletin/qb201209/C_Half-yearly.pdf
- https://reportify-1252068037.cos.ap-beijing.myqcloud.com/media/production/s_f3358c68_f3358c68419796e97100ab9437233589.pdf
- https://www.liuyanecon.com/wp-content/uploads/%E9%93%B6%E8%A1%8C%E7%B3%BB%E7%BB%9F%E6%80%A7%E9%A3%8E%E9%99%A9%E7%9A%84%E5%AE%9E%E4%BD%93%E7%BB%8F%E6%B5%8E%E8%B5%B7%E6%BA%90%E4%B8%8E%E9%98%B2%E8%8C%83%E5%8C%96%E8%A7%A3%E6%9C%BA%E5%88%B6202507.pdf
- https://thesis.lib.nycu.edu.tw/bitstreams/f0190d72-77c4-4ed0-bf22-17d633cdd7fd/download
- https://pdf.dfcfw.com/pdf/H3_AP201902281300873960_1.pdf?1551361152000.pdf
- https://www.toutiao.com/article/7589070974059708938/
- http://qxuk.com/cjzx/2665.html
- https://r.img.cctvpic.com/photoAlbum/page/20231222/2023122218161782885.pdf?spm=C73544894212.P59511941341.0.0&file=2023122218161782885.pdf
- https://reportify-1252068037.cos.ap-beijing.myqcloud.com/media/production/s_f3358c68_f3358c68419796e97100ab9437233589.pdf
- https://r.img.cctvpic.com/photoAlbum/page/20231222/2023122218161782885.pdf?spm=C73544894212.P59511941341.0.0&file=2023122218161782885.pdf
- https://file.iyanbao.com/pdf/92047-3213af1a-e355-4b2e-9542-a4d974b1bf49.pdf
- https://finance.sina.cn/bond/zsyw/2023-12-29/detail-imzzsiyz5847935.d.html?vt=4&cid=76633&node_id=76633
- https://r.img.cctvpic.com/photoAlbum/page/20231222/2023122218161782885.pdf?spm=C73544894212.P59511941341.0.0&file=2023122218161782885.pdf
- https://j.eastday.com/m/1703242540035093
- https://www.shmet.com/news/newsDetail-2-881844.html
- https://pdf.dfcfw.com/pdf/H3_AP202104061481451661_1.pdf?1617708577000.pdf
- https://pdf.dfcfw.com/pdf/H3_AP202110211524105037_1.pdf
- https://finance.sina.cn/zl/2021-12-24/zl-ikyakumx6124825.d.html?from=wap
- https://www.moomoo.com/hans/news/post/27903293
- https://m.10100.com/article/40814550
- https://www.econ.sdu.edu.cn/__local/C/B6/AF/5001B750FE24BB0C1ABD41A4665_5CC41E93_21F876E.pdf?e=.pdf
- https://jrj.sh.gov.cn/SCDT197/20240813/9a49d9d5ee6b4bf49857bae8e9f88b1e.html
- https://wallstreetcn.com/articles/3762149
- https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/2025122616592613805/2025123019161895262.pdf
- https://www.hankunlaw.com/upload/newsAndInsights/65a712e236a427c5fbdc103cc6ba20dd.pdf
- https://finance.sina.cn/bond/zsyw/2023-12-29/detail-imzzsiyz5847935.d.html?vt=4&cid=76633&node_id=76633
- https://file.iyanbao.com/pdf/92047-3213af1a-e355-4b2e-9542-a4d974b1bf49.pdf
- https://r.img.cctvpic.com/photoAlbum/page/20231222/2023122218161782885.pdf?spm=C73544894212.P59511941341.0.0&file=2023122218161782885.pdf