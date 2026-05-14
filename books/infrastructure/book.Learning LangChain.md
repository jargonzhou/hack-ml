# Learning LangChain: Building AI and LLM Applications with LangChain and LangGraph

action: [learning-langchain](../../codes/hack-llm//README.md#learning-langchain)

codes: Python, JavaScript.

brief concepts of agent framework, the abstractions among versions of LangChain change, just think LLM invocation as a step of application computations.

Still need to read the oss docs.

# 1. LLM Fundamentals with LangChain
## Getting Set Up with LangChain
## Using LLMs in LangChain

## Making LLM Prompts Reusable

## Getting Specific Formats out of LLMs
- JSON Output
- Other Machine-Readable Formats with Output Parsers

## Assembling the Many Pieces of an LLM Application
- Using the Runnable Interface
- Imperative Composition
- Declarative Composition

# 2. RAG Part I: Indexing Your Data
## The Goal: Picking Relevant Context for LLMs
## Embeddings: Converting Text to Numbers
- Embeddings Before LLMs
- LLM-Based Embeddings
- Semantic Embeddings Explained
## Converting Your Documents into Text
## Splitting Your Text into Chunks
## Generating Text Embeddings
## Storing Embeddings in a Vector Store
- Getting Set Up with PGVector
- Working with Vector Stores
## Tracking Changes to Your Documents
## Indexing Optimization
- MultiVectorRetriever
- RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval
- ColBERT: Optimizing Embeddings

# 3. RAG Part II: Chatting with Your Data
## Introducing Retrieval-Augmented Generation
- Retrieving Relevant Documents
- Generating LLM Predictions Using Relevant Documents

Figure 3-4. Effective strategies to optimize the accuracy of your RAG system
- 1. **query transformations**: rephrase, modify, and/or expand the question 
- 2. **routing**: route the query between datastores
- 3. **query construction**: natrual langauge to SQL/Cypher/metadata filters
- 4. **multimodal/semistructured index**: optimize docs for retrieval and/or build index to handle variable data types (images/tables)
- 5. **postprocessing**: consolidate, rank, and/or filter retrieved documents

## Query Transformation/查询转换
- Rewrite-Retrieve-Read/重写-检索-读
- Multi-Query Retrieval/多查询检索
- RAG-Fusion/RAG融合
- Hypothetical Document Embeddings(HyDE)/假设文档嵌入

## Query Routing/查询路由
- Logical Routing/逻辑路由
- Semantic Routing/语义路由

## Query Construction/查询构造
- Text-to-Metadata Filter/文本2元数据过滤
- Text-to-SQL/文本2SQL

# 4. Using LangGraph to Add Memory to Your Chatbot
## Building a Chatbot Memory System/记忆系统
## Introducing LangGraph
## Creating a StateGraph
## Adding Memory to StateGraph
## Modifying Chat History
- Trimming Messages/截断消息
- Filtering Messages/过滤消息
- Merging Consecutive Messages/合并连续消息

# 5. Cognitive Architectures/认知架构 with LangGraph

adoption among code and LLM
- decide output of step
- decide next steps to take
- decide what steps are available to take

Figure 5-1. Cognitive architectures for LLM applications
- 0. Code: doesn’t use LLMs at all
- 1. LLM call: with one LLM call only
- 2. Chain: with the use of multiple LLM calls in a predefined sequence
- 3. Router: use the LLM to define the sequence of steps to take
- 4. State machine
- 5. Autonomous

## Architecture #1: LLM Call
## Architecture #2: Chain
## Architecture #3: Router

# 6. Agent Architecture/智能体架构
## The Plan-Do Loop
## Building a LangGraph Agent
## Always Calling a Tool First
## Dealing with Many Tools

# 7. Agents II
## Reflection/反思

## Subgraphs/子图 in LangGraph
- Calling a Subgraph Directly/直接调用子图: 共享状态键
- Calling a Subgraph with a Function/使用函数调用子图: 不同的状态键

## Multi-Agent Architectures/多智能体架构

Figure 7-3. Multiple strategies for coordinating multiple agents
- Network/网络
- Supervisor Architecture, Supervisor as tools/监督者
- Hierarchical/层次
- Custom workflow/自定义工作流

# 8. Patterns to Make the Most of LLMs

Figure 8-1. The agency-reliability trade-off

## Structured Output
- Intermediate Output/中间输出
- Streaming LLM Output Token-by-Token/逐token的LLM流式输出
- Human-in-the-Loop Modalities/人机交互模式
- Multitasking LLMs/多任务LLM

# 9. Deployment: Launching Your AI Application into Production
## Prerequisites
- Install Dependencies
- Large Language Model
- Vector Store
- Backend API
- Create a LangSmith Account

## Understanding the LangGraph Platform API
- Data Models
  - Assistants: a configured instance of a `CompiledGraph`.
  - Threads: contains the accumulated state of a group of runs.
  - Runs: an invocation of an assistant.
  - Cron jobs: enable graphs to be run on a user-defined schedule.
- Features to support complex agent architecture
  - Streaming: 5 modes, values/messages/updates/events/debug
  - Humain-in-the-loop: 4 solutions, reject/enqueue/interrupt/rollback
  - Double texting
  - Stateless runs
  - Webhooks

## Deploying Your AI Application on LangGraph Platform
- Create a LangGraph API Config
- Test Your LangGraph App Locally
- Deploy from the LangSmith UI
- Launch LangGraph Studio

## Security

# 10. Testing: Evaluation, Monitoring, and Continuous Improvement
## Testing Techniques Across the LLM App Development Cycle

## The Design Stage: Self-Corrective RAG

## The Preproduction Stage
- Creating Datasets
- Defining Your Evaluation Criteria
- Regression Testing
- Evaluating an Agent’s End-to-End Performance

- Testing an agent’s final response
- Testing a single step of an agent
- Testing an agent’s trajectory

## Production
- Tracing
- Collect Feedback in Production
- Classification and Tagging
- Monitoring and Fixing Errors

# 11. Building with LLMs
- Interactive Chatbots/交互式聊天机器人
- Collaborative Editing with LLMs/基于LLM的协作编辑
- Ambient Computing/环境计算

# See Also
* Patrick Lewis et al., **Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks**, arXiv, April 12, 2021.
* Xinbei Ma et al., **Query Rewriting for Retrieval-Augmented Large Language Models**, arXiv, October 23, 2023. Research commissioned by Microsoft Research Asia.
* Luyu Gao et al., **Precise Zero-Shot Dense Retrieval Without Relevance Labels**, arXiv, December 20, 2022. - HyDE
* Theodore R. Sumers et al., **Cognitive Architectures for Language Agents**, arXiv, September 5, 2023, updated March 15, 2024.
* Stuart Russell and Peter Norvig. **Artificial Intelligence** (Pearson, 2020) 
* ReAct: Synergizing Reasoning and Acting in Language Models. - https://react-lm.github.io/
* Daniel Kahneman. **Thinking, Fast and Slow** (Farrar, Straus and Giroux, 2011)
* [LangGraph Platform is now Generally Available: Deploy & manage long-running, stateful Agents](https://www.langchain.com/blog/langgraph-platform-ga) - As of October 2025, LangGraph Platform has been re-named to "LangSmith Deployment".

tools
- LLM/chat model: OpenAI/Anthropic/Ollama
  - gpt-3.5-turbo
  - gpt-4, gpt-4o
- Embeddings: OpenAI/Cohere/Ollama
- Vector store: PGVector/Weaviate/OpenSearch, Supabase
- Python
  - Pydantic
- duckduckgo-search 

datasets
- the financial performance and risks in Tesla’s 2022 annual report


langchain supported vector stores
```markdown
LangChain 提供了一个统一的接口，支持 100 多种 向量存储方案，涵盖了从本地轻量级库到云端托管数据库的各种需求。 [1, 2, 3, 4, 5] 
以下是根据使用场景划分的常见支持列表：
## 1. 热门/主流集成 (Top Integrations) [6] 
这些是社区最常用且文档最丰富的选项： [7, 8] 

* [Chroma](https://docs.langchain.com/oss/python/integrations/vectorstores): 开源且易于使用的本地向量数据库，非常适合原型设计。
* [Pinecone](https://docs.langchain.com/oss/python/integrations/vectorstores/pgvector): 托管的云端服务，无需维护基础设施，扩展性极佳。
* FAISS (Facebook AI Similarity Search): 极其高效的本地库，适合处理大规模密集向量的相似性搜索。
* Weaviate: 开源向量数据库，支持元数据过滤和混合搜索。
* Qdrant: 提供生产级 API 的高性能向量搜索引擎。
* Milvus: 专为海量数据（十亿级）设计的企业级分布式向量数据库。 [2, 7, 9, 10, 11] 

## 2. 传统数据库的向量扩展
如果你已经在使用某些数据库，可以直接利用它们的向量插件： [12, 13] 

* PGVector (PostgreSQL): 如果你已有 Postgres 环境，这是添加向量功能最顺滑的选择。
* [MongoDB Atlas](https://docs.langchain.com/oss/python/integrations/vectorstores/singlestore): 支持在 MongoDB 中进行向量搜索集成。
* Elasticsearch: 强大的搜索引擎，现在也完整支持向量检索。
* Redis: 利用 Redis 的内存速度进行极速检索。 [9, 14, 15, 16, 17, 18] 

## 3. 轻量级与内存存储

* InMemoryVectorStore: 纯内存存储，适合临时的演示或小型任务，不具备持久化能力。
* HNSWLib: 轻量级的本地索引方案。 [2, 3, 8, 19, 20] 

## 如何选择？

* 本地开发/原型：首选 Chroma 或 FAISS。
* 快速上线/免运维：首选 Pinecone 或 Astra DB。
* 已有关系型数据：首选 PGVector (Postgres)。
* 海量规模 (十亿级)：首选 Milvus。 [7, 8, 13, 21, 22] 

由于 LangChain 使用统一的 VectorStore 接口，你可以通过更改几行初始化代码，在这些不同的后端之间进行无缝切换。 [23, 24] 
您目前处理的文档大约有多少量级？我可以根据您的规模推荐最匹配的存储方案。

[1] [https://docs.langchain.com](https://docs.langchain.com/oss/python/integrations/providers/overview)
[2] [https://medium.com](https://medium.com/@abhinavjyoti09/vector-stores-in-langchain-f2a639522f03)
[3] [https://www.geeksforgeeks.org](https://www.geeksforgeeks.org/artificial-intelligence/vector-stores-in-langchain/)
[4] [https://medium.com](https://medium.com/data-and-beyond/building-with-langchain-rag-application-971022c4c898)
[5] [https://skywork.ai](https://skywork.ai/skypage/en/bridging-worlds-langchain-mcp-server/1979009298000891904)
[6] [https://docs.langchain.com](https://docs.langchain.com/oss/python/integrations/vectorstores)
[7] [https://www.geeksforgeeks.org](https://www.geeksforgeeks.org/artificial-intelligence/vector-stores-in-langchain/)
[8] [https://medium.com](https://medium.com/@abhinavjyoti09/vector-stores-in-langchain-f2a639522f03)
[9] [https://dev.to](https://dev.to/aws-builders/day-6-demystifying-langchain-embeddings-and-vector-stores-a-chai-tapri-story-15d8)
[10] [https://www.pluralsight.com](https://www.pluralsight.com/resources/blog/ai-and-data/langchain-local-vector-database-tutorial)
[11] [https://www.pluralsight.com](https://www.pluralsight.com/resources/blog/ai-and-data/langchain-local-vector-database-tutorial)
[12] [https://docs.langchain.com](https://docs.langchain.com/oss/javascript/integrations/vectorstores)
[13] [https://encore.dev](https://encore.dev/articles/best-vector-databases)
[14] [https://docs.langchain.com](https://docs.langchain.com/oss/python/integrations/providers/overview)
[15] [https://docs.langchain.com](https://docs.langchain.com/oss/python/integrations/vectorstores/pgvectorstore)
[16] [https://docs.langchain.com](https://docs.langchain.com/oss/javascript/integrations/vectorstores/pgvector)
[17] [https://reference.langchain.com](https://reference.langchain.com/python/langchain-community/vector-stores)
[18] [https://medium.com](https://medium.com/@shankarwagh297/vector-stores-and-retrievers-in-langchain-powering-smarter-ai-retrieval-8b7e90b4f02e)
[19] [https://reference.langchain.com](https://reference.langchain.com/python/langchain-core/vectorstores)
[20] [https://reference.langchain.com](https://reference.langchain.com/python/langchain-core/vectorstores)
[21] [https://dev.to](https://dev.to/datastax/choosing-a-vector-store-for-langchain-4n48)
[22] [https://encore.dev](https://encore.dev/articles/best-vector-databases)
[23] [https://medium.com](https://medium.com/@shivendra6757patil/langchain-embeddings-and-vector-stores-4bb7049b0884)
[24] [https://medium.com](https://medium.com/@abhishekjainindore24/langchain-part-11-vector-stores-9b9971b0b1d8)
```