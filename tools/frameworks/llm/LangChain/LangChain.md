# LangChain
* https://www.langchain.com/
* https://en.wikipedia.org/wiki/LangChain

> LangChain is a software framework that helps facilitate the integration of large language models (LLMs) into applications. As a **language model integration framework/语言模型集成框架**, LangChain's use-cases largely overlap with those of language models in general, including document analysis and summarization, chatbots, and code analysis.

# Core Components
- Agents
- Models
- Messages
- Tools
- Short-term memory
- Streaming
- Structured output


```shell
pip install langchain
pip install langchain-ollama
pip install langchain-community
pip install langchain-postgres

pip install langchain-mcp-adapters
pip install langchain-tests
pip install langchain-text-splitters
```

- show me concept graph of LangChain, including Deep Agents, LangGraph, LangSmith, especially in Python stack.
```markdown
这是一个基于 Python 技术栈的 LangChain 生态系统概念图谱。它展示了核心组件、数据流向以及它们如何协同构建、调试和部署高级大语言模型（LLM）应用。 [1, 2, 3, 4] 

                       [ 开发者 / 用户 ]
                               │
                        (编写 Python 代码)
                               │
                               v
┌──────────────────────────────────────────────────────────────────┐
│                    LANGSMITH (监控与评估)                        │
│  - 追踪 Trace  - 评估 Evaluation  - 提示词管理 Hub  - 调试 Debug │
└──────────────────────^───────────────^───────────────────────────┘
                       │               │
            (遥测数据 / Telemetry)     (遥测数据 / Telemetry)
                       │               │
┌──────────────────────┴──────┐ ┌──────┴────────────────────────────┐
│     LANGCHAIN CORE & EXP    │ │          LANGGRAPH                │
│                             │ │  (循环/图结构智能体 & 多智能体)   │
│  ┌───────────────────────┐  │ │                                   │
│  │   LangChain Expression│  │ │   ┌──────────────────────┐        │
│  │   Language (LCEL)     │  │ │   │   State (全局状态)   │        │
│  └───────────┬───────────┘  │ │   └──────────┬───────────┘        │
│              │              │ │              │                    │
│              v              │ │              v                    │
│  ┌───────────────────────┐  │ │   ┌──────────────────────┐        │
│  │  Chains (线性流水线)  │  │ │   │    Nodes (节点/函数) │        │
│  └───────────┬───────────┘  │ │   └──────────┬───────────┘        │
│              │              │ │              │                    │
│              v              │ │              v                    │
│  ┌───────────────────────┐  │ │   ┌──────────────────────┐        │
│  │  Agents (传统单智能体)│  │ │   │  Edges (边/条件路由) │        │
│  └───────────────────────┘  │ │   └──────────────────────┘        │
└──────────────┬──────────────┘ └──────────────┬────────────────────┘
               │                               │
               └───────────────┬───────────────┘
                               │
                               v
┌──────────────────────────────────────────────────────────────────────┐
│               DEEP AGENTS & ADVANCED PATTERNS                        │
│  (基于 LangGraph 实现的复杂架构，如 LangGraph Engineer / ReAct)      │
│  - 反思循环 (Reflection)              - 规划与执行 (Plan-and-Solve)  │
│  - 人机交互回退 (Human-in-the-loop)    - 记忆系统 (Long/Short Memory)│
└──────────────────────────────┬───────────────────────────────────────┘
                               │
            (调用底层组件 / Utilizes Infrastructure)
                               │
                               v
┌──────────────────────────────────────────────────────────────┐
│                  基础组件层 (Infrastructure)                 │
│  - LLMs / ChatModels (OpenAI, Anthropic, Ollama, etc.)       │
│  - Vector Stores (Chroma, Pinecone)                          │
│  - Tools / Toolkits (Google Search, Python REPL)             │
│  - Document Loaders & Text Splitters (RAG 数据准备)          │
└──────────────────────────────────────────────────────────────┘

# 核心组件解析
## 1. LangChain (核心与基础) [5, 6] 

* LCEL (LangChain 表达语言): 使用 | 管道符声明式链接组件。
* Chains: 固定的线性工作流。输入直接流向输出。
* 传统 Agents: 依赖 LLM 决定下一步。但在处理复杂循环、条件分支和多智能体协同协作时能力有限。 [7, 8, 9, 10] 

## 2. LangGraph (状态管理与循环)

* State: 包含图运行当前状态的 Python 对象。每个节点都可以修改它。
* Nodes: 具体的 Python 函数。执行工具调用、调用 LLM 或处理数据。
* Edges: 控制流向。条件边 (Conditional Edges) 允许 LLM 动态决定下一个执行节点。
* 适用场景: 构建具有复杂反思循环 (Reflection) 和多智能体架构 (Multi-agent) 的深层智能体（Deep Agents）。 [11, 12, 13, 14, 15] 

## 3. Deep Agents (深层智能体模式)

* 高阶认知能力: 不再是简单的“提示词->回答”模式。
* 设计模式: 包含 Plan-and-Solve (规划与执行)、RAG-Reviewer (检索-评审循环)。
* 核心特性: 支持 Human-in-the-loop (人工介入)。在敏感节点挂起状态，等待人工审批后再继续。 [16, 17, 18] 

## 4. LangSmith (全生命周期平台)

* Trace (追踪): 自动记录 Python 代码中每一步的输入输出、耗时和 Token 消耗。
* Evaluation (评估): 使用生产数据或黄金数据集自动评估 Agent 的准确率。
* Prompt Hub: 在云端集中管理、版本化和测试提示词。 [19, 20, 21] 

------------------------------
如果想深入了解具体实现，请告诉我：

* 您是否需要某个特定模式（例如 ReAct 架构 或 多智能体协作）的 Python 代码示例？
* 您目前的业务场景更偏向于 RAG（知识库检索） 还是 自动化工具执行（Agent）？ [22, 23] 


[1] [https://www.digitalocean.com](https://www.digitalocean.com/community/conceptual-articles/langchain-framework-explained)
[2] [https://www.upgrad.com](https://www.upgrad.com/blog/what-is-langchain/)
[3] [https://pub.towardsai.net](https://pub.towardsai.net/langchain-vs-langgraph-pipelines-vs-processes-in-agentic-systems-0436e52dc2c0)
[4] [https://medium.com](https://medium.com/@warunkarabrar/understanding-langchain-langgraph-rag-building-the-next-generation-of-ai-systems-962143e3eed0)
[5] [https://www.linkedin.com](https://www.linkedin.com/pulse/haystack-vs-langchainlanggraph-which-framework-should-alon-avramson-1yb0e)
[6] [https://www.cnblogs.com](https://www.cnblogs.com/edeny/p/18654857)
[7] [https://levelup.gitconnected.com](https://levelup.gitconnected.com/building-llm-apps-langchain-basics-16bcd78be433)
[8] [https://k21academy.com](https://k21academy.com/ai-ml/langchain-expression-language/)
[9] [https://medium.com](https://medium.com/@abhishekmayya/what-is-langchain-a-friendly-introduction-for-beginners-e0ed2db6f57e)
[10] [https://medium.com](https://medium.com/@poojakhape08/from-prompts-to-ai-systems-a-deep-dive-into-langchain-architecture-caa22da8516e)
[11] [https://www.analyticsvidhya.com](https://www.analyticsvidhya.com/blog/2025/05/chatbot-using-agentic-rag/)
[12] [https://dranolia.medium.com](https://dranolia.medium.com/building-advanced-llm-applications-a-technical-deep-dive-into-langchain-langgraph-and-rag-with-bd925c2cbf50)
[13] [https://medium.com](https://medium.com/@Shrishml/a-primer-on-ai-agents-with-langgraph-understand-all-about-it-0534345190dc)
[14] [https://medium.com](https://medium.com/aimonks/building-production-grade-rag-systems-with-langgraph-from-knowledge-bases-to-intelligent-retrieval-72da0d090414)
[15] [https://www.zenml.io](https://www.zenml.io/blog/llamaindex-vs-langchain)
[16] [https://www.langchain.com](https://www.langchain.com/langchain)
[17] [https://www.instagram.com](https://www.instagram.com/p/DYH1lxjFDj9/)
[18] [https://www.flowhunt.io](https://www.flowhunt.io/blog/human-in-the-loop-middleware-python-safe-ai-agents/)
[19] [https://walseisarel.medium.com](https://walseisarel.medium.com/top-10-open-source-rag-evaluation-frameworks-you-must-try-15c40d0ba2c0)
[20] [https://link.springer.com](https://link.springer.com/chapter/10.1007/979-8-8688-0882-1_9)
[21] [https://www.langchain.com](https://www.langchain.com/blog/aws-marketplace-july-2025-announce)
[22] [https://link.springer.com](https://link.springer.com/chapter/10.1007/979-8-8688-0569-1_7)
[23] [https://www.mdpi.com](https://www.mdpi.com/2673-7426/5/4/70)
```

# Deep Agents
* https://docs.langchain.com/oss/python/deepagents/overview

Deep agents are the easiest way to **start building agents and applications powered by LLMs**—with built-in capabilities for task planning, file systems for context management, subagent-spawning, and long-term memory. You can use deep agents for any task, including complex, multi-step tasks.

# LangGraph
* https://docs.langchain.com/oss/python/langgraph/overview

LangGraph is a low-level **orchestration framework and runtime/编排框架和运行时** for building, managing, and deploying long-running, stateful agents.


```shell
$ pip install -U langgraph
# LangGraph CLI
$ pip install langgraph-cli
```

more:
* [langgraph.json](https://docs.langchain.com/langsmith/cli#configuration-file)

# Integrations
* https://reference.langchain.com/python/integrations/overview

LangChain packages to connect with popular LLM providers, vector stores, tools, and other services.

[All LangChain Python integration providers](https://docs.langchain.com/oss/python/integrations/providers/all_providers)

# LangSmith
* https://docs.langchain.com/langsmith/home

LangSmith is a platform that helps AI teams use live production data for continuous testing and improvement. LangSmith provides:
- **Observability**: See exactly how your agent thinks and acts with detailed tracing and aggregate trend metrics.
- **Evaluation**: Test and score agent behavior on production data or offline datasets to continuously improve performance.
- **Prompt Engineering**: Iterate on prompts with version control, prompt optimization, and collaboration features.
- **Deployment**: Ship your agent in one click, using scalable infrastructure built for long-running tasks.

# MCP Adapter

Use Model Context Protocol (MCP) tools within LangChain and LangGraph applications.

# See Also
* [Awesome LangChain](https://github.com/kyrolabs/awesome-langchain): Awesome list of tools and projects with the awesome LangChain framework.
* [Microsoft - LangChain for Beginners - A Course](https://github.com/microsoft/langchain-for-beginners): A course teaching everything you need to know to start building AI Agents with LangChain.
