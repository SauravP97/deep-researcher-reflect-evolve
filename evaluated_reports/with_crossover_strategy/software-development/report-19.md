# prometheus 的高流失率会造成什么影响，有什么系统的方案可以解决？各家云厂商有没有现有方案？

好的，作为首席研究编辑，我将根据提供的原始研究笔记，为您撰写一份全面、专业的深度研究报告。

---

### **Prometheus高流失率问题深度研究报告：影响、系统性解决方案与云厂商实践**

#### **执行摘要 (Executive Summary)**

Prometheus中的“高流失率”（High Churn Rate）指时间序列的频繁创建与销毁，是现代动态环境（如Kubernetes）中的常见挑战。此问题是导致“高基数”（High Cardinality）——即唯一时间序列总量过高——的核心驱动因素。高基数会严重影响Prometheus的性能、存储、可靠性和成本。

本报告深入分析了高基数带来的具体影响，包括内存消耗激增导致的OOM（内存溢出）风险、磁盘空间膨胀、查询性能下降，以及在云环境中急剧上升的运营成本。

针对此问题，报告系统性地梳理了从源头治理到架构优化的多层次解决方案。关键策略包括：通过`metric_relabel_configs`实施“允许列表（Allowlist）”策略以精确控制指标摄入；利用记录规则（Recording Rules）进行预聚合以优化查询。更进一步，报告深入探讨了两种核心架构选择的权衡：“流式预聚合”以牺牲数据原始粒度为代价换取极高的资源效率；而“批处理后聚合”（如记录规则）则保留了原始数据但无法解决存储成本问题。

最后，报告调研了主流开源扩展方案（如Thanos, VictoriaMetrics, Mimir）和主要云厂商（AWS, Google Cloud, Azure, 阿里云, 腾讯云）的托管服务。云厂商普遍提供具有明确配额和精细化控制机制的托管Prometheus服务，但在按用量付费的模式下，高基数问题会直接转化为高昂的成本，因此成本控制是其核心挑战。

---

#### **第一部分：定义、识别与影响分析**

##### **1.1 定义：从高流失率到高基数**

在Prometheus的上下文中，“高流失率”（High Churn Rate）特指时间序列被频繁地创建和销毁。当一个时间序列的标签（label）值发生变化时，旧的序列停止接收数据，系统会创建一个全新的序列来替代它。这是导致监控系统**高基数（High Cardinality）**问题的核心驱动因素。

常见成因包括：
*   **容器化环境**：Kubernetes中Pod的频繁创建、销毁或滚动更新，导致`pod_name`等标签值不断变化。
*   **高基数标签**：在指标中使用了动态且唯一的标签值，如`request_id`, `user_id`, `pod-template-hash`等。
*   **服务自动扩缩容**：实例的动态增减会生成新的时间序列。

##### **1.2 识别与量化**

识别高流失率的来源是解决问题的第一步。Prometheus自身提供了精确的元数据指标用于诊断：
*   **整体流失率评估**：通过查询`rate(prometheus_tsdb_head_series_created_total[5m])`可以估算实例整体的时间序列创建速率。
*   **精确定位来源**：使用`scrape_series_added`指标，可以定位到具体是哪个采集任务（job）或目标（target）贡献了最多的新序列。例如，`sum(sum_over_time(scrape_series_added[5m])) by (job)`可以找出5分钟内新增序列最多的任务。

##### **1.3 高基数的负面影响**

高流失率引发的高基数问题对整个监控系统构成严峻挑战，具体影响如下：

*   **性能影响**：每个时间序列都会在Prometheus的内存（Head Block）中保留元数据和索引。高基数导致内存消耗急剧增加，极易引发内存不足（OOM）错误，导致服务中断。同时，CPU在数据摄取、索引、查询和压缩（Compaction）过程中的负担也会加重，导致查询性能显著下降。
*   **存储影响**：大量短生命周期的序列会使TSDB磁盘空间迅速增长。这些不连续的数据也降低了数据块的压缩效率，导致存储膨胀。
*   **可靠性影响**：系统资源紧张可能导致数据采集延迟、数据点丢失，甚至告警失灵。
*   **成本影响**：在云环境中，更高的CPU、内存和磁盘使用量直接转化为更高的运营成本。对于采用按活跃时间序列或样本摄入量计费的托管服务，高基数问题会使成本被急剧放大。一份分析指出，在处理高基数负载时，云托管服务的成本可能是自建方案的7倍甚至54倍。

---

#### **第二部分：通用优化策略与核心架构权衡**

##### **2.1 通用缓解与优化策略**

在不改变核心架构的前提下，以下策略是解决高基数问题的最佳实践：

1.  **指标源头治理**：最根本的方法是在应用代码或Exporter中避免使用高基数标签。
2.  **实施“允许列表”（Allowlist）策略**：通过Prometheus的`metric_relabel_configs`和`keep`动作，精确定义需要保留的指标列表。相比于性能和可控性较差的“拒绝列表”（Denylist）或`drop`策略，“允许列表”被认为是更优的最佳实践。可以借助`mimirtool`等工具自动化分析Grafana仪表盘和告警规则中正在使用的指标，以生成此列表。
3.  **使用记录规则（Recording Rules）预聚合**：对于无法在源头治理的高基数指标，可以创建记录规则，将其预聚合为新的、低基数的摘要时间序列。后续的仪表盘查询和告警应直接使用这些聚合后的新指标，以提升性能。

##### **2.2 核心架构权衡：流式预聚合 vs. 批处理后聚合**

当通用策略不足以解决问题时，需要进行架构层面的选择。核心权衡在于**资源效率 vs. 数据粒度**，体现在两种不同的聚合模型上：

1.  **批处理式后聚合（Batch Post-aggregation）**
    *   **代表技术**：Prometheus原生的记录规则（Recording Rules）。
    *   **工作原理**：在原始高基数数据被采集并**存入数据库之后**，周期性地执行查询，将结果存为新的低基数序列。
    *   **优势**：完整保留了原始的高基数数据，为未来的深度分析和即席查询（ad-hoc analysis）提供了可能性。
    *   **劣势**：**无法解决存储问题**。由于原始数据仍需被完整存储，因此由高基数带来的高昂存储成本和资源消耗问题依然存在。

2.  **流式预聚合（Streaming Pre-aggregation）**
    *   **代表技术**：M3DB的`m3aggregator`组件。
    *   **工作原理**：在指标数据流写入长期存储**之前**，在内存中对其进行实时聚合，去除高基数标签。
    *   **优势**：**从根本上解决了资源消耗问题**。只有聚合后的低基数数据被长期存储，显著降低了存储成本和查询负载。
    *   **劣势**：**丢失了原始数据粒度**。一旦聚合完成，原始的高基数数据通常会被丢弃，从而限制了对原始数据的任意维度查询能力。

**决策指南**：对于成本敏感型或查询模式固定的场景，流式预聚合是更优选择。对于数据完整性要求高、需要保留原始数据以进行探索性分析的场景，应采用批处理后聚合，并结合其他优化手段。

---

#### **第三部分：主流解决方案对比**

##### **3.1 开源扩展方案**

为解决Prometheus单点的性能和存储瓶颈，社区涌现了多个可水平扩展的远程存储方案：

| 方案 | 核心架构与特点 | 资源效率 | 适用场景 |
| :--- | :--- | :--- | :--- |
| **VictoriaMetrics** | 自研高性能TSDB，采用本地持久化存储。 | **非常高**。在同等负载下，其CPU、内存和磁盘消耗显著低于其他方案。 | 追求高性能、低资源消耗和高性价比的场景。 |
| **Grafana Mimir** | 源于Cortex，基于Prometheus TSDB，依赖对象存储。 | 中等。可扩展性极高（可达10亿序列），但内存消耗较大，成本昂贵。 | 需要极高可扩展性、可用性，且运维能力强的团队。 |
| **Thanos** | 模块化工具集，与Prometheus无缝集成，依赖对象存储。 | 中等。 | 对现有大量Prometheus实例进行联邦查询和长期存储的场景。 |
| **M3DB** | 专注于流式预聚合，解决高基数问题的专用方案。 | 高。通过`m3aggregator`在写入前聚合，有效控制资源。 | 对高基数问题有强烈需求，但运维复杂度相对较高。 |

##### **3.2 主流云厂商托管方案**

各大云厂商均提供“Prometheus as a Service”，内置了高基数管理能力，但其核心挑战在于成本控制。

| 云厂商 | 服务名称 | 核心机制与配额 |
| :--- | :--- | :--- |
| **Amazon (AWS)** | Amazon Managed Service for Prometheus (AMP) | - **高配额**：默认5000万活跃时间序列上限，可申请提升至10亿。<br>- **精细化控制**：支持基于标签（label-based）的摄入控制规则，主动管理高基数指标。 |
| **Google Cloud** | Managed Service for Prometheus | - **成本控制**：允许在数据收集器层面配置过滤规则，阻止高基数原始数据发送到云端。<br>- **诊断工具**：提供工具分析和识别导致高基数问题的具体指标。 |
| **Azure** | Azure Monitor managed service for Prometheus | - **明确的限制**：默认每分钟最多提取100万个数据点；side-car容器最多处理15万个唯一时间序列。<br>- **保护机制**：当单个抓取任务超限时，整个任务会被丢弃以保护系统。<br>- **扩展建议**：建议通过创建多个工作区来横向扩展。 |
| **阿里云** | 可观测监控Prometheus版 (ARMS) | - **按量计费**：基于写入的数据量和功能使用收费。<br>- **优化建议**：与腾讯云类似，主要通过优化采集配置来控制数据点数量，从而管理成本。设有数据采集、Agent等默认限制。 |
| **腾讯云** | Prometheus监控服务 (TMP/TPS) | - **按量计費**：收费标准基于上报的监控数据点数。<br>- **成本优化方案**：建议通过在`ServiceMonitor`等配置中添加过滤规则、只采集必要指标、区分付费与免费指标等方式，从源头减少数据上报量。 |

---

#### **第四部分：结论与展望**

Prometheus的高流失率及其导致的高基数问题，是对现代监控系统稳定性和成本效益的直接挑战。解决此问题不存在“银弹”，而是一套需要结合业务场景进行权衡的系统性方法论。

*   **对于中小规模用户**：应优先从**源头治理**和**配置优化**入手，如避免使用高基数标签，并严格实施基于“允许列表”的指标过滤策略。
*   **对于大规模或高动态环境的用户**：必须考虑采用**架构级解决方案**。选择在于：
    *   **数据完整性优先**：采用如VictoriaMetrics或Thanos等远程存储方案，结合记录规则进行优化。
    *   **成本与资源效率优先**：采用支持流式预聚合的方案（如M3DB），以牺牲部分数据粒度换取极致的资源效率。
*   **对于希望降低运维复杂度的用户**：云厂商的托管服务是理想选择，但必须精通其提供的成本控制工具和配额管理机制，否则将面临高昂的费用。

未来，随着云原生技术的进一步普及，监控系统处理高基数的能力将成为衡量其成熟度的关键指标。解决方案将继续在**数据粒度、查询性能、存储成本和运维复杂度**这几个维度之间寻求更优的平衡点。

---

#### **参考文献**

*   https://cloud.tencent.com/developer/article/2183178
*   https://flashcat.cloud/blog/prometheus-performance-and-cardinality-in-practice/
*   https://blog.csdn.net/qq_43684922/article/details/126814815
*   https://blog.csdn.net/qq_43684922/article/details/126814335
*   https://m3db.io/docs/how_to/use_as_tsdb/
*   https://m3db.io/docs/architecture/m3aggregator/
*   https://chronosphere.io/learn/aggregating-millions-of-prometheus-timeseries-with-m3/
*   https://groups.google.com/g/m3db/c/Mn-W42-JnSE
*   https://m3db.io/docs/overview/

## Citations 
- https://blog.csdn.net/qq_43684922/article/details/131095243
- https://chenlujjj.github.io/monitor/prometheus-term-note/
- https://valyala.medium.com/prometheus-storage-technical-terms-for-humans-4ab4de6c3d48
- https://training.promlabs.com/training/monitoring-and-debugging-prometheus/web-status-pages/tsdb-status-information/
- https://zhuanlan.zhihu.com/p/615997777
- https://blog.csdn.net/qq_43684922/article/details/126814335
- https://www.cnblogs.com/east4ming/p/17011688.html
- https://cloud.tencent.com/developer/article/2183178
- https://flashcat.cloud/blog/prometheus-performance-and-cardinality-in-practice/
- https://blog.csdn.net/qq_43684922/article/details/126814815
- https://blog.csdn.net/sinat_32582203/article/details/127278422
- https://www.cnblogs.com/love-DanDan/p/18404463
- https://cloud.tencent.com/developer/article/2376532
- https://zhuanlan.zhihu.com/p/135899052
- https://icloudnative.io/posts/comparing-thanos-to-victoriametrics-cluster/
- https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-managed-service-prometheus-50M-default-activeserieslimit/
- https://docs.aws.amazon.com/prometheus/latest/userguide/AMP_quotas.html
- https://victoriametrics.com/blog/managed-prometheus-pricing/
- https://aws.amazon.com/prometheus/pricing/
- https://aws.amazon.com/blogs/mt/optimizing-metrics-ingestion-with-amazon-managed-service-for-prometheus/
- https://cloud.google.com/managed-prometheus
- https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/cost-controls
- https://medium.com/@platform.engineers/optimizing-prometheus-storage-handling-high-cardinality-metrics-at-scale-31140c92a7e4
- https://last9.io/blog/how-to-manage-high-cardinality-metrics-in-prometheus/
- https://docs.cloud.google.com/stackdriver/docs/managed-prometheus
- https://learn.microsoft.com/en-us/azure/azure-monitor/metrics/azure-monitor-workspace-scaling-best-practice
- https://learn.microsoft.com/en-us/azure/azure-monitor/metrics/prometheus-metrics-details
- https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/service-limits
- https://last9.io/blog/how-to-manage-high-cardinality-metrics-in-prometheus/
- https://stackoverflow.com/questions/46373442/how-dangerous-are-high-cardinality-labels-in-prometheus
- https://www.alibabacloud.com/help/zh/arms/prometheus-monitoring/use-prometheus-to-monitor-tencent-cloud-services
- https://www.aliyun.com/product/developerservices/prometheus
- https://buy.cloud.tencent.com/price/prometheus
- https://zhuanlan.zhihu.com/p/9832335139
- https://www.tencentcloud.com/zh/product/tmp
- https://grafana.com/docs/grafana-cloud/cost-management-and-billing/analyze-costs/reduce-costs/metrics-costs/client-side-filtering/
- https://heyoncall.com/guides/the-art-of-metric-relabeling-in-prometheus
- https://www.nsghospital.com/how-to/prometheus-relabel_configs-vs-metric_relabel_configs
- https://chejinying.com/tech/posts/prometheus/metric_relabel/
- https://www.robustperception.io/relabel_configs-vs-metric_relabel_configs/
- https://blog.csdn.net/qq_34556414/article/details/125574036
- https://cloud.tencent.com/developer/article/2136284
- https://help.aliyun.com/zh/arms/prometheus-monitoring/product-overview/billing-description/
- https://help.aliyun.com/zh/arms/prometheus-monitoring/product-overview/service-limits
- https://help.aliyun.com/zh/prometheus/product-overview/billing-overview
- https://www.alibabacloud.com/help/zh/arms/product-overview/product-billing-new-version
- https://main.qcloudimg.com/raw/document/product/pdf/457_71895_cn.pdf
- https://buy.cloud.tencent.com/price/prometheus
- http://static-aliyun-doc.oss-cn-hangzhou.aliyuncs.com/download%2Fpdf%2F122122%2FPrometheus%25E7%259B%2591%25E6%258E%25A7%25E5%2585%25AC%25E5%2585%25B1%25E4%25BA%2591%25E5%2590%2588%25E9%259B%2586_cn_zh-CN.pdf
- https://m3db.io/docs/how_to/use_as_tsdb/
- https://groups.google.com/g/m3db/c/Mn-W42-JnSE
- https://m3db.io/docs/architecture/m3aggregator/
- https://m3db.io/docs/overview/
- https://chronosphere.io/learn/aggregating-millions-of-prometheus-timeseries-with-m3/
- https://m3db.io/docs/
- https://m3db.io/docs/integrations/prometheus/
- https://m3db.io/
- https://m3db.io/docs/architecture/m3db/
- https://m3db.io/docs/overview/components/
- https://prometheus.io/docs/practices/rules/
- https://signoz.io/guides/what-is-a-prometheus-rule/
- https://last9.io/blog/prometheus-recording-rules/
- https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/
- https://training.promlabs.com/training/recording-rules/recording-rules-overview/evaluation-cycle/
- https://github.com/m3db/m3/blob/master/site/content/architecture/m3aggregator/overview.md
- https://m3db.io/docs/architecture/m3aggregator/
- https://risingwave.com/glossary/consistency-state-management/
- https://mboehm7.github.io/teaching/ws2122_dbs/12_StreamProcessing.pdf
- https://mboehm7.github.io/teaching/ws2122_dia/12_StreamProcessing.pdf
- https://www.youtube.com/watch?v=kYz6me_C_fA
- https://chronosphere.io/learn/aggregating-millions-of-prometheus-timeseries-with-m3/
- https://static.sched.com/hosted_files/promconna21/51/PromConNA_Streaming_Recording_Rules_Prometheus_Thanos_Cortex.pdf
- https://promconna21.sched.com/event/mGKp/streaming-recording-rules-for-prometheus-thanos-and-cortex-using-the-m3-coordinator-gibbs-cullen-rob-skillington-chronosphere
- https://chronosphere.io/learn/stream-vs-batch-leveraging-m3-and-thanos-for-real-time-aggregation/
- https://zhuanlan.zhihu.com/p/461204793
- https://chronosphere.io/learn/aggregating-millions-of-prometheus-timeseries-with-m3/
- https://www.linkedin.com/posts/apurvachaudhary_streaming-aggregation-vs-recording-rules-activity-7067790987439325185-3kVR
- https://www.youtube.com/watch?v=kYz6me_C_fA
- https://www.alibabacloud.com/help/zh/arms/prometheus-monitoring/product-overview/benefits
- https://www.alibabacloud.com/help/zh/arms/prometheus-monitoring/untitled-document-1753770404448
- https://developer.aliyun.com/article/1518807
- https://www.alibabacloud.com/help/zh/arms/prometheus-monitoring/data-storage
- https://www.alibabacloud.com/help/zh/arms/prometheus-monitoring/operation-guide/