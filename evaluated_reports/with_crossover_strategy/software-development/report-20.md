# 研究下Anthropic最新发布的Streamable HTTP的工程中的具体实现方案

# Anthropic Streamable HTTP 工程实现深度解析：基于模型上下文协议（MCP）的标准化流式通信框架

## 报告摘要

本报告深入研究了 Anthropic 最新发布的 "Streamable HTTP" 的具体工程实现方案。研究表明，Streamable HTTP 并非一项独立的技术，而是**模型上下文协议（Model Context Protocol, MCP）** 的首个具体传输层实现。MCP 是一个由 Anthropic 主导开发的开放标准，旨在为大型语言模型（LLM）与外部工具、数据源和工作流的交互提供一个标准化的、基于 JSON-RPC 2.0 的远程过程调用（RPC）层。

Streamable HTTP 的核心工程实现巧妙地利用了标准的 HTTP `multipart/mixed` 响应类型，将一个完整的流式交互分解为结构化的、独立的数据块。这种设计不仅解决了传统流式技术（如 SSE）传输非结构化数据的局限性，还确保了对现有网络基础设施的广泛兼容性。此外，该协议通过在 schema 中引入 `'streamable'` 标志，创新性地实现了对大型输入的“按需引用加载”，极大地优化了处理大规模上下文时的效率和延迟。官方提供的客户端 SDK（如 TypeScript 和 Python）封装了对 `multipart/mixed` 流的解析逻辑，为开发者提供了与 MCP 服务器进行标准化交互的便捷途径。

## 核心研究发现

### 1. 协议定位：从 Streamable HTTP 到模型上下文协议（MCP）

最初的研究目标 "Streamable HTTP" 实际上是更宏大框架的一部分。所有研究资料均指向一个核心概念——**模型上下文协议（Model Context Protocol, MCP）**。

*   **MCP 是核心协议**: MCP 是一个开放、模型无关的协议，其设计灵感源于语言服务器协议（LSP），旨在成为“AI 领域的 USB-C”，为 LLM 与外部系统（工具、数据）的连接提供统一标准。
*   **Streamable HTTP 是传输实现**: Streamable HTTP 是 MCP 协议的一种具体服务器传输方案，专注于提供无状态（stateless）的 HTTP 支持。它利用 `multipart/mixed` 作为底层机制，将 MCP 定义的结构化数据在 HTTP 上进行流式传输。

### 2. 核心架构：基于 JSON-RPC 2.0 的标准化 RPC 层

MCP 本质上是一个面向能力的 RPC 层，其通信和数据结构由官方发布的 schema 严格定义。

*   **通信基础**: 协议建立在轻量级的 JSON-RPC 2.0 之上，用于处理所有客户端与服务器之间的请求、响应和通知 [https://github.com/modelcontextprotocol/specification]。
*   **能力抽象**: 服务器通过三个核心概念向 AI 暴露其能力，并使用 JSON Schema 进行描述，以便客户端在调用前进行验证：
    *   **资源 (Resources)**: 提供结构化的上下文信息和数据。
    *   **工具 (Tools)**: 暴露可供 AI 执行的功能或动作。
    *   **提示 (Prompts)**: 提供预构建的指令模板，引导模型完成复杂任务。
*   **协议的“事实之源”**: 官方 GitHub 仓库中的 `schema.ts` 和 `schema.json` 文件是协议所有消息、类型和结构的唯一事实来源（single source of truth）[https://github.com/modelcontextprotocol/specification/blob/main/schema/2025-03-26/schema.ts]。

### 3. 传输层实现：`multipart/mixed` 的精巧运用

Streamable HTTP 的工程亮点在于其对标准 HTTP `multipart/mixed` 响应类型的创造性使用，从而实现了结构化的流式传输。

*   **响应头**: 服务器返回的 `Content-Type` 为 `multipart/mixed; boundary="..."`，通过边界字符串分隔不同的消息部分。
*   **结构化响应体**:
    1.  **第一部分 (元数据)**: `Content-Type` 为 `application/json`，对应 MCP 规范中的 `StreamStartEvent`，包含流类型和消息元数据。
    2.  **中间部分 (数据块)**: 任意数量的数据块，`Content-Type` 为 `application/json;type=chunk`，对应 `StreamMessageEvent`，通常包含文本增量等内容块（Content Blocks）。
    3.  **结束部分 (结尾)**: 对应 `StreamEndEvent`，标志流的结束，并提供停止原因（`stop_reason`）和用量统计（`usage`）。

### 4. 创新机制：通过 URL 引用处理大型流式输入

MCP 协议设计了一个高效机制来处理大型输入上下文，避免了在每次请求中上传庞大的数据。

*   **`'streamable'` 标志位**: 在 MCP 的 `ContentBlock` 对象定义中，包含一个布尔类型的 `'streamable'` 标志。
*   **按需引用加载**: 当客户端需要包含大型内容（如代码库、大型文档）时，可将该内容块的 `'streamable'` 标志设为 `true`，并在 `url` 字段中提供一个可访问该内容的 URL。
*   **模型按需拉取**: 请求载荷中不包含实际数据。模型在处理时，会根据需要从该 URL 流式传输数据，从而显著减少请求体积和网络延迟。

### 5. 生态系统与 SDK：官方客户端与服务器实现

Anthropic 与社区共同维护着 MCP 的官方 SDK，为开发者提供了协议的完整实现。

*   **多语言 SDK**: 官方提供了包括 TypeScript、Python、Java、Go 在内的多种语言 SDK [https://github.com/modelcontextprotocol]。
*   **客户端实现**: TypeScript SDK 中的 `@modelcontextprotocol/client` 包包含了客户端实现，其核心逻辑位于 `packages/client/src/client/streamableHttp.ts` 文件中，负责处理 `multipart/mixed` 响应流的解析 [https://github.com/modelcontextprotocol/typescript-sdk]。
*   **示例代码**: SDK 仓库中提供了丰富的客户端和服务器端示例（如 `simpleStreamableHttp.ts`），展示了如何构建和交互 MCP 服务。

## 深度技术分析

### 1. MCP 流生命周期与 `multipart/mixed` 结构映射

MCP 定义了清晰的流生命周期事件，这些事件与 Streamable HTTP 中 `multipart/mixed` 的各个部分精确对应，实现了结构化数据的流式传输。

| MCP 事件               | `multipart/mixed` 相应部分                                | 描述                                                         |
| ---------------------- | ----------------------------------------------------------- | ------------------------------------------------------------ |
| **`StreamStartEvent`** | **第一部分** (Part 1)<br>`Content-Type: application/json`   | 标志着流的开始。包含整个消息的元数据，如 `message_id`、`model`、`role` 等。 |
| **`StreamMessageEvent`** | **中间部分** (Part 2...N)<br>`Content-Type: application/json;type=chunk` | 包含流式传输的数据块增量（delta）。最常见的类型是 `content_delta`，用于传输文本块（`TextBlock`）的增量内容。 |
| **`StreamEndEvent`**   | **最后部分** (Final Part)                                   | 标志着流的正常结束。包含最终的 `stop_reason` 和 `usage`（用量统计）信息。 |

### 2. 客户端 SDK 实现分析

官方 TypeScript SDK 中的 `streamableHttp.ts` 文件是理解客户端如何处理 Streamable HTTP 响应的关键。尽管完整的源代码解析细节在研究资料中有限，但其核心职责清晰：

*   **连接建立**: 客户端通过 `StreamableHTTPClientTransport` 类与远程 MCP 服务器建立 HTTP 连接。
*   **流式解析**: 该模块内聚了对 `multipart/mixed` 响应体的解析逻辑。它会监听 HTTP 响应流，并根据 `boundary` 字符串来切分数据。
*   **事件分发**: 每当一个完整的部分（part）被接收并解析后，SDK 会将其内容（通常是 JSON 对象）转换为对应的 MCP 事件（如 `StreamStartEvent`），并分发给上层应用逻辑进行处理。
*   **会话管理**: SDK 还负责管理会札，包括通过 OAuth 凭证进行安全认证，以及在并发连接中隔离会话数据（尽管资料指出早期版本在此处存在已知问题）。

### 3. 服务器端架构考量

构建一个 MCP 服务器需要在定义的 JSON-RPC 2.0 框架内管理会话上下文和执行工具调用。

*   **会话初始化**: 会话始于客户端发送的 `InitializeRequest`。服务器需在此阶段响应其自身能力（`ServerCapabilities`），与客户端进行能力协商，确保双方协议版本和功能兼容。
*   **上下文管理**: MCP 是一个有状态协议。服务器需要维护会话上下文，响应客户端对“资源”的读取请求（如 `resources/list`, `resources/read`），为模型的决策提供依据。
*   **工具执行**: 服务器通过 `tools/list` 方法向客户端暴露其可用的工具列表。当接收到 `tools/call` 请求时，服务器执行相应的业务逻辑，并将结果作为 `tool_result` 内容块返回。由于工具由 JSON Schema 定义，输入验证可以在客户端和服务端两侧进行。
*   **异步与进度通知**: 对于长时间运行的任务，客户端可以在请求中包含一个 `progress_token`。服务器则可以通过发送 `notifications/progress` 消息，异步地向客户端报告任务进度。

### 4. 协议设计哲学与竞品对比

MCP 的设计哲学在于建立一个通用的、持久化的工具连接标准，这与业界其他方案形成了鲜明对比。

| 方案                            | **Anthropic (MCP)**                                        | **OpenAI (Assistants API)**                                 | **Google (A2A Protocol)**                                         |
| ------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------------- |
| **核心理念**                    | **持久化会话**：建立一个标准化的、双向、持久的连接（“AI领域的USB-C”）。 | **按次调用（Per-call）**：轻量级、无状态的单次函数调用模式。        | **多智能体协作**：为企业级、大规模的多智能体生态系统设计的协作协议。 |
| **技术架构**                    | **协议驱动**：基于 JSON-RPC 2.0，传输层无关（transport-agnostic）。 | **API 驱动**：通常利用 OpenAPI (OAS) 规范来描述 HTTP 服务。 | **消息格式驱动**：定义了用于消息、线程、函数调用和事件的共享格式。 |
| **状态管理**                    | **有状态 (Stateful)**：强调会话和能力协商。                 | **无状态 (Stateless)**：每次调用都是独立的。                  | **有状态 (Stateful)**：专为复杂的协作工作流设计。                 |
| **开放性**                      | **开放协议**：由 Anthropic 主导，但规范和 SDK 完全开源。     | **专有 API**：由 OpenAI 定义和控制。                          | **开放协议**：由 Google 和超过50个生态系统合作伙伴共同支持。      |

## 结论与展望

Anthropic 的 Streamable HTTP 并非简单的流式 API，而是其推动模型交互标准化的战略核心——模型上下文协议（MCP）——的工程落地。通过将结构化的 JSON-RPC 消息封装在标准的 `multipart/mixed` HTTP 响应中，该方案在实现高级流式功能（如结构化数据、双向通信）的同时，保持了对现有网络生态的兼容性。

其最大的创新在于将交互的关注点从临时的、非结构化的“字节流”提升到了持久的、协议驱动的“会话层”。`'streamable'` 标志的设计也为解决 LLM 面临的大上下文处理挑战提供了一个优雅且高效的工程范例。

展望未来，MCP 的成功将取决于其生态系统的发展和业界的采纳程度。如果其他模型提供商和工具开发者广泛采用此协议，MCP 有望成为连接 AI 与外部世界的标准化桥梁，极大地降低集成复杂性，并催生出更强大、更可靠的代理式 AI 应用。

## 参考文献

*   Model Context Protocol - Official Specification Repository: [https://github.com/modelcontextprotocol/specification](https://github.com/modelcontextprotocol/specification)
*   Model Context Protocol - TypeScript SDK Repository: [https://github.com/modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk)
*   Model Context Protocol - Python SDK Repository: [https://github.com/modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk)
*   MCP Schema (Version 2025-03-26): [https://github.com/modelcontextprotocol/specification/blob/main/schema/2025-03-26/schema.ts](https://github.com/modelcontextprotocol/specification/blob/main/schema/2025-03-26/schema.ts)
*   Developer Community Discussion on MCP: [https://github.com/orgs/community/discussions/174921](https://github.com/orgs/community/discussions/174921)

## Citations 
- https://developer.emporix.io/changelog/2025/2025-12-04-ai
- https://pypi.org/project/anthropic/0.3.9/
- https://modelcontextprotocol.io/development/roadmap
- https://www.speakeasy.com/docs/gram/api-clients/using-anthropic-api-with-gram-mcp-servers
- https://platform.claude.com/docs/en/release-notes/overview
- https://modelcontextprotocol.io/
- https://modelcontextprotocol.io/specification/2025-11-25
- https://modelcontextprotocol.info/docs/
- https://zuplo.com/docs/mcp-server/introduction
- https://www.ietf.org/archive/id/draft-zeng-mcp-troubleshooting-00.html
- https://medium.com/@shubh7/model-context-protocol-mcp-by-anthropic-1b77ddcc2fbc
- https://www.jsonrpc.org/specification
- https://modelcontextprotocol.io/specification/2025-11-25/server/tools
- https://modelcontextprotocol.info/specification/draft/server/tools/
- https://modelcontextprotocol.io/specification/2025-11-25
- https://github.com/modelcontextprotocol/specification/blob/main/schema/2025-03-26/schema.ts
- https://www.blackhillsinfosec.com/model-context-protocol/
- https://github.com/modelcontextprotocol/modelcontextprotocol
- https://modelcontextprotocol.io/docs/learn/architecture
- https://betterstack.com/community/guides/ai/mcp-explained/
- https://blog.logrocket.com/understanding-anthropic-model-context-protocol-mcp/
- https://modelcontextprotocol.io/docs/learn/architecture
- https://www.anthropic.com/news/model-context-protocol
- https://mlops.community/model-context-protocol/
- https://gpt-trainer.com/blog/anthropic+model+context+protocol+mcp
- https://modelcontextprotocol.io/specification/2025-06-18/schema
- https://modelcontextprotocol.io/specification/draft/schema
- https://github.com/modelcontextprotocol/specification/blob/main/schema/2025-03-26/schema.ts
- https://github.com/modelcontextprotocol/specification/blob/main/schema/2024-11-05/schema.json
- https://www.deep-kondah.com/intromodel-context-protocol-mcp/
- https://github.com/modelcontextprotocol/specification/blob/main/schema/2025-03-26/schema.ts
- https://modelcontextprotocol.io/specification/draft/schema
- https://modelcontextprotocol.info/specification/draft/basic/utilities/progress/
- https://modelcontextprotocol.io/docs/learn/architecture
- https://zbrain.ai/model-context-protocol/
- https://github.com/e0ipso/jsonrpc_mcp
- https://github.com/modelcontextprotocol/specification/blob/main/schema/2025-03-26/schema.ts
- https://github.com/modelcontextprotocol/specification/blob/main/schema/2024-11-05/schema.json
- https://github.com/modelcontextprotocol/modelcontextprotocol
- https://www.anthropic.com/news/model-context-protocol
- https://github.com/cyanheads/model-context-protocol-resources/blob/main/guides/mcp-client-development-guide.md
- https://modelcontextprotocol.io/docs/learn/architecture
- https://github.com/madhukarkumar/anthropic-mcp-servers
- https://github.com/modelcontextprotocol/servers
- https://www.reddit.com/r/programming/comments/1k3e0ax/model_context_protocol_exhaustively_explained/
- https://github.com/modelcontextprotocol/specification/blob/main/schema/2025-03-26/schema.ts
- https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/capabilities.md
- https://github.com/modelcontextprotocol/typescript-sdk
- https://modelcontextprotocol.io/specification/draft/basic
- https://github.com/modelcontextprotocol/modelcontextprotocol
- https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/schema/2025-03-26/schema.json
- https://deepwiki.com/modelcontextprotocol/python-sdk/5.3-context-and-progress-reporting
- https://github.com/modelcontextprotocol/typescript-sdk
- https://uuithub.com/modelcontextprotocol/rust-sdk
- https://uithub.com/modelcontextprotocol/modelcontextprotocol/tree/main/docs/specification/2025-03-26
- https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/schema/2025-03-26/schema.ts
- https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/schema/2025-03-26/schema.json
- https://github.com/salman1993/specification/blob/main/schema/schema.json
- https://github.com/modelcontextprotocol/specification/blob/main/schema/draft/schema.ts
- https://github.com/modelcontextprotocol
- https://github.com/modelcontextprotocol/specification/blob/main/schema/2025-03-26/schema.ts
- https://github.com/modelcontextprotocol/specification/blob/main/schema/2024-11-05/schema.json
- https://modelcontextprotocol.io/specification/draft/schema
- https://github.com/cyanheads/model-context-protocol-resources/blob/main/guides/mcp-server-development-guide.md
- https://modelcontextprotocol.io/specification/2025-06-18/schema
- https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/refs/heads/main/README.md
- https://github.com/modelcontextprotocol/specification/blob/main/schema/2025-03-26/schema.ts
- https://github.com/modelcontextprotocol/specification/blob/main/CONTRIBUTING.md
- https://github.com/modelcontextprotocol/modelcontextprotocol
- https://modelcontextprotocol.io/specification/2025-06-18/server/resources
- https://deepwiki.com/modelcontextprotocol/modelcontextprotocol/2.2-schema-system-and-message-types
- https://github.com/dandavison/modelcontextprotocol-modelcontextprotocol/blob/main/schema/2025-03-26/schema.ts
- https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/schema/2025-03-26/schema.ts
- https://deepwiki.com/modelcontextprotocol/modelcontextprotocol/7.3-schema-development-workflow
- https://deepwiki.com/modelcontextprotocol/modelcontextprotocol/6.3-schema-development-workflow
- https://github.com/ihill7/MCP-docs-modelcontextprotocol/blob/main/schema/2025-11-25/schema.ts
- https://modelcontextprotocol.io/specification/2025-06-18/schema
- https://modelcontextprotocol.io/specification/2025-03-26/basic
- https://github.com/modelcontextprotocol/modelcontextprotocol
- https://deepwiki.com/modelcontextprotocol/modelcontextprotocol/2.2-schema-system-and-message-types
- https://modelcontextprotocol.io/docs/sdk
- https://github.com/modelcontextprotocol
- https://github.com/modelcontextprotocol/typescript-sdk
- https://medium.com/@balazskocsis/building-model-context-protocol-servers-typescript-or-python-a1a235f789d7
- https://github.com/modelcontextprotocol/python-sdk
- https://github.com/modelcontextprotocol/typescript-sdk/blob/main/src/examples/client/simpleStreamableHttp.ts
- https://github.com/modelcontextprotocol/typescript-sdk/blob/main/CLAUDE.md
- https://github.com/modelcontextprotocol/typescript-sdk
- https://github.com/modelcontextprotocol/typescript-sdk/issues/742
- https://github.com/modelcontextprotocol/typescript-sdk/blob/main/examples/client/README.md
- https://github.com/modelcontextprotocol/typescript-sdk/blob/main/src/examples/client/simpleStreamableHttp.ts
- https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/server.md
- https://github.com/modelcontextprotocol/typescript-sdk/blob/main/examples/client/README.md
- https://www.reddit.com/r/modelcontextprotocol/comments/1k2cuxd/mcp_typescript_sdk_110x_releassed_with_streamable/
- https://www.npmjs.com/package/@modelcontextprotocol/sdk?ref=blog.promptlayer.com
- https://dzone.com/articles/model-context-protocol-mcp-guide-architecture-uses-implementation
- https://modelcontextprotocol.io/docs/learn/server-concepts
- https://modelcontextprotocol.io/specification/2025-06-18/architecture
- https://cloud.google.com/discover/what-is-model-context-protocol
- https://guptadeepak.com/mcp-for-technical-professionals-a-comprehensive-guide-to-understanding-and-implementing-the-model-context-protocol/
- https://rajeevbarnwal.medium.com/model-context-protocol-mcp-vs-function-calling-vs-openapi-tools-when-to-use-each-547f3d59c5da
- https://www.linkedin.com/pulse/openai-function-calling-vs-anthropic-model-context-protocol-liu-pdj3e
- https://www.ikangai.com/model-context-protocol-comparison-mcp-vs-function-calling-plugins-apis/
- https://www.reddit.com/r/ClaudeAI/comments/1h0w1z6/model_context_protocol_vs_function_calling_whats/
- https://www.marktechpost.com/2025/10/08/model-context-protocol-mcp-vs-function-calling-vs-openapi-tools-when-to-use-each/
- https://github.com/orgs/community/discussions/174921
- https://github.com/modelcontextprotocol
- https://github.com/niradler/code-feedback
- https://github.com/cyanheads/model-context-protocol-resources/blob/main/guides/mcp-server-development-guide.md
- https://github.com/asinghcsu/model-context-protocol-survey
- https://github.com/modelcontextprotocol/typescript-sdk/blob/main/CLAUDE.md
- https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/client.md
- https://github.com/hideya/langchain-mcp-tools-ts/issues/33
- https://github.com/modelcontextprotocol/typescript-sdk/blob/main/examples/client/README.md
- https://github.com/modelcontextprotocol/typescript-sdk/blob/main/examples/server/README.md
- https://github.com/Http-Multipart-Data-Parser/Http-Multipart-Data-Parser/issues/106
- https://github.com/mjackson/multipart-parser
- https://github.com/modelcontextprotocol/typescript-sdk/blob/main/src/examples/server/simpleStatelessStreamableHttp.ts