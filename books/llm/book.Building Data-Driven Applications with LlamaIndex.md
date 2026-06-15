# Building Data-Driven Applications with LlamaIndex: A practical guide to retrieval-augmented generation (RAG) to enhance LLM applications

version in book: 0.10. 2026-05 0.14.22.

action: [hack-llamaindex](../../codes/hack-llamaindex/README.md)

- Part 1:Introduction to  Generative AI and LlamaIndex: 1-2
- Part 2: Starting Your First LlamaIndex Project: 3-5
- Part 3: Retrieving and Working with Indexed Data: 6-8
- Part 4: Customization, Prompt Engineering, and Final Words: 9-11

# 1: Understanding Large Language Models
- Introducing GenAI and LLMs
  - What is GenAI?
  - What is an LLM?
- Understanding the role of LLMs in modern technology
- Exploring challenges with LLMs
- Augmenting LLMs with RAG

# 2: LlamaIndex: The Hidden Jewel - An Introduction to the LlamaIndex Ecosystem
- Technical requirements
- Optimizing language models – the symbiosis/共生 of fine-tuning, RAG, and LlamaIndex
  - Is RAG the only possible solution?
  - What LlamaIndex does
    - Build a search engine for your document collection
    - Create a company chatbot with customized knowledge
    - Generate summaries of large reports or papers
    - Develop a smart assistant for complex workflows
- Discovering the advantages of progressively disclosing complexity
  - An important aspect to consider
- Introducing PITS(personalized intelligent tutoring system)/个性化智能辅导系统 – our LlamaIndex hands-on project
  - Here’s how it will work
- Preparing our coding environment
  - Installing Python
  - Installing Git
  - Installing LlamaIndex
  - Signing up for an OpenAI API key
  - Discovering Streamlit – the perfect tool for rapid building and deployment!
  - Installing Streamlit
  - Finishing up
  - One final check
- Familiarizing ourselves with the structure of the LlamaIndex code repository

Figure 2.3 – An overview of the PITS workflow
- user onboarding
- upload and index existing user material/上传和索引现有的用户资料
- gauge user knowledge level/评估用户知识水平
- build custom learing material/构建定制学习资料
- user learning journey/用户学习旅程
  - trainer agent
  - slides, narration, quizzes/幻灯片, 旁白, 测验
  - present concepts, provide exampels, answer questions, track progress, track conversation

# 3: Kickstarting Your Journey with LlamaIndex
- Technical requirements
- Uncovering the essential building blocks of LlamaIndex – documents, nodes, and indexes
  - Documents `from llama_index.core import Document`
    - `from llama_index.readers.wikipedia import WikipediaReader`
  - Nodes `from llama_index.core.schema import TextNode`
  - Manually creating the Node objects
  - Automatically extracting Nodes from Documents using splitters
    - `from llama_index.core.node_parser import TokenTextSplitter`
  - Nodes don’t like to be alone – they crave relationships
    - `from llama_index.core.schema import NodeRelationship`
  - Why are relationships important?
  - Indexes
    - `SummaryIndex`
    - `DocumentSummaryIndex`
    - `VectorStoreIndex`
    - `TreeIndex`
    - `KeywordTableIndex`
    - `KnowledgeGraphIndex`
    - `ComposableGraph`
  - Are we there yet? - retrievers/检索器, response synthesizers/响应合成器
  - How does this actually work under the hood?
    - `QueryEngine`: retrievers, response synthesizers
    - node postprocessor
  - A quick recap of the key concepts
- Building our first interactive, augmented LLM application
  - Using the logging features of LlamaIndex to understand the logic and debug our applications
  - Customizing the LLM used by LlamaIndex
  - Easy as 1-2-3
  - The temperature parameter
  - Understanding how Settings can be used for customization
    - `from llama_index.core.settings import Settings`
- Starting our PITS project – hands-on exercise
  - Let’s have a look at the source code

Figure 3.5 – The complete RAG workflow with LlamaIndex
- 1. Loading data as Documents
- 2. Parsing Documents into coherent Nodes
- 3. Building an optimized index from Nodes
- 4. Running queries over the index to retrieve relevant Nodes
- 5. Synthesizing the final response

# 4: Ingesting Data into Our RAG Workflow/数据摄入
- Technical requirements
- Ingesting data via LlamaHub
- An overview of LlamaHub
- Using the LlamaHub data loaders to ingest content
  - Ingesting data from a web page `llama-index-readers-web`
  - Ingesting data from a database `llama-index-readers-database`
  - Bulk-ingesting data from sources with multiple file formats
    - `SimpleDirectoryReader`
    - LlamaParse
- Parsing the documents into nodes
  - Understanding the simple text splitters `from llama_index.core.node_parser import ...`
    - `SentenceSplitter`
    - `TokenTextSplitter`
    - `CodeSplitter`: `tree_sitter`, `tree_sitter_languages`
  - Using more advanced node parsers `NodeParser`
    - `SentenceWindowNodeParser`
    - `LangchainNodeParser`: `langchain`
    - `SimpleFileNodeParser`
    - `HTMLNodeParser`, `MarkdownNodeParser`, `JSONNodeParser`
  - Using relational parsers
    - `HierarchicalNodeParser`
    - `UnstructuredElementNodeParser`
  - Confused about node parsers and text splitters?
  - Understanding `chunk_size` and `chunk_overlap`
  - Including relationships with `include_prev_next_rel`
  - Practical ways of using these node creation models
    - `parser.get_nodes_from_documents([doc])`
    - `Settings.text_splitter = text_splitter`
    - Defining the parsers as a transformation step in an ingestion pipeline
- Working with metadata to improve the context
  - `SummaryExtractor`
  - `QuestionsAnsweredExtractor`
  - `TitleExtractor`
  - `EntityExtractor`: NLTK
  - `KeywordExtractor`
  - `PydanticProgramExtractor`
  - `MarvinMetadataExtractor`: Marvin AI engineering framework
  - Defining your custom extractor: `BaseExtractor`
  - Is having all that metadata always a good thing?
- Estimating the potential cost of using metadata extractors
  - Follow these simple best practices to minimize your costs
  - Estimate your maximal costs before running the actual extractors
- Preserving privacy with metadata extractors, and not only
  - Scrubbing personal data and other sensitive information
    - PII: Personally Identifiable Information
    - `from llama_index.core.postprocessor import NERPIINodePostprocessor`
- Using the ingestion pipeline to increase efficiency
  - `IngestionPipeline`
- Handling documents that contain a mix of text and tabular data
- Hands-on – ingesting study materials into our PITS

Figure 4.4 – An ingestion pipeline at work

# 5: Indexing with LlamaIndex
- Technical requirements
- Indexing data – a bird’s-eye view
  - Common features of all Index types `BaseIndex`
- Understanding the `VectorStoreIndex`
  - A simple usage example for the VectorStoreIndex
  - Understanding embeddings
  - Understanding similarity search
    - cosine similarity
    - dot product
    - euclidean distance
  - OK, but how does LlamaIndex generate these embeddings?
    - OpenAI text-embedding-ada-002
    - Hugging Face BAAI/bge-small-en-v1.5
  - How do I decide which embedding model I should use?
- Persisting and reusing Indexes
  - Understanding the `StorageContext`
    - docstore, index_store, vector_store, graph_store
  - The difference between vector stores and vector databases
- Exploring other index types in LlamaIndex
  - The `SummaryIndex`
  - The `DocumentSummaryIndex`
  - The `KeywordTableIndex`
  - The `TreeIndex`
  - The `KnowledgeGraphIndex`
- Building Indexes on top of other Indexes with `ComposableGraph`
  - How to use the ComposableGraph
  - A more detailed description of this concept
- Estimating the potential cost of building and querying Indexes
- Indexing our PITS study materials – hands-on

# 6: Querying Our Data, Part 1 – Context Retrieval/上下文检索
- Technical requirements
- Learning about query mechanics – an overview
- Understanding the basic retrievers/基本检索器
  - The `VectorStoreIndex` retrievers: `VectorIndexRetriever`, `VectorIndexAutoRetriever`
  - The `SummaryIndex` retrievers: `SummaryIndexRetriever`, `SummaryIndexEmbeddingRetriever`, `SummaryIndexLLMRetriever`
  - The `DocumentSummaryIndex` retrievers: `DocumentSummaryIndexLLMRetriever`, `DocumentSummaryIndexEmbeddingRetriever`
  - The `TreeIndex` retrievers: `TreeSelectLeafRetriever`, `TreeSelectLeafEmbeddingRetriever`, `TreeAllLeafRetriever`, `TreeRootRetriever`
  - The `KeywordTableIndex` retrievers: `KeywordTableGPTRetriever`, `KeywordTableSimpleRetriever`, `KeywordTableRAKERetriever`
  - The `KnowledgeGraphIndex` retrievers: `KGTableRetriever`, `KnowledgeGraphRAGRetriever`
  - Common characteristics shared by all retrievers
    - `QueryBundle`
    - `callback_manager`
    - `BaseRetriever`
  - Efficient use of retrieval mechanisms – asynchronous operation/异步操作
- Building more advanced retrieval mechanisms/高级检索机制
  - The naive retrieval method/朴素检索方法
  - Implementing metadata filters/元数据过滤器
  - Using selectors/选择器 for more advanced decision logic
    - `LLMSingleSelector`, `LLMMultiSelector`, `EmbeddingSingleSelector`, `PydanticSingleSelector`, `PydanticMultiSelector`
  - Understanding tools
    - `RetrieverTool`
  - Transforming and rewriting queries/转换和重写查询
    - `QueryTransform`
      - `IdentityQueryTransform`
      - `HyDEQueryTransform`: Hypothetical Document Embeddings (HyDE) transforms the query into a hypothetical document generated by an LLM
      - `DecomposeQueryTransform`
      - `ImageOutputQueryTransform`
      - `StepDecomposeQueryTransform`
  - Creating more specific sub-queries/子查询
    - `from llama_index.core.question_gen import LLMQuestionGenerator`
    - `SubQuestionQueryEngine`
- Understanding the concepts of dense and sparse retrieval/稠密和稀疏检索
  - Dense retrieval: embedding vectors
  - Sparse retrieval: the Term Frequency – Inverse Document Frequency (TF-IDF) method
  - Implementing sparse retrieval in LlamaIndex
    - `BM25Retriever`
  - Discovering other advanced retrieval methods
    - [Advanced Retrieval Strategies](https://developers.llamaindex.ai/python/framework/optimizing/advanced_retrieval/advanced_retrieval/): Small-to-Big retrieval, recursive retrieval, retrieval from embedded tables, multi-modal retrieval, auto-merging retrieval, ...

# 7: Querying Our Data, Part 2 – Postprocessing/后置处理 and Response Synthesis/响应合成
- Technical requirements
- Re-ranking, transforming, and filtering nodes using postprocessors/使用后置处理器重排序/转换/过滤文档节点
  - Exploring how postprocessors filter, transform, and re-rank nodes
  - `SimilarityPostprocessor`
  - `KeywordNodePostprocessor`: spaCy
  - `PrevNextNodePostprocessor`
  - `LongContextReorder`
  - `PIINodePostprocessor` and `NERPIINodePostprocessor`
  - `MetadataReplacementPostprocessor`
  - `SentenceEmbeddingOptimizer`
  - Time-based postprocessors
    - `FixedRecencyPostprocessor`
    - `EmbeddingRecencyPostprocessor`
    - `TimeWeightedPostprocessor`
  - Re-ranking postprocessors
    - `LLMRerank`
    - `CohereRerank`: Cohere’s neural models https://cohere.com/rerank
    - `SentenceTransformerRerank`: sentence transformer models
    - `RankGPTRerank`: Sun et al. (2023), **Is ChatGPT Good at Search? Investigating Large Language Models as Re-Ranking Agents** https://arxiv.org/abs/2304.09542v2
    - `LongLLMLinguaPostprocessor`: Jiang et al. (2023), **LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models** (https://arxiv.org/abs/2310.05736v2)
  - Final thoughts about node postprocessors: `BaseNodePostprocessor`
- Understanding response synthesizers/响应合成器
  - `from llama_index.core import get_response_synthesizer`: `response_mode`
  - `BaseSynthesizer`
- Implementing output parsing techniques/输出解析技术
  - Extracting structured outputs using output parsers
    - `GuardrailsOutputParser`: the Guardrails library https://www.guardrailsai.com
      - RAIL: Reliable AI Markup Langauge
    - `LangchainOutputParser`
  - Extracting structured outputs using Pydantic programs
    - `OpenAIPydanticProgram`
- Building and using query engines/查询引擎
  - Exploring different methods of building query engines
  - Advanced uses of the `QueryEngine` interface
- Hands-on – building quizzes in PITS

Figure 7.1 – The role of node postprocessors in RAG

Figure 7.2 – The refine response synthesizer

`QueryEngine`
```python
CitationQueryEngine
CogniswitchQueryEngine
ComposableGraphQueryEngine
QASummaryQueryEngineBuilder
TransformQueryEngine
MultiStepQueryEngine
ToolRetrieverRouterQueryEngine
SQLJoinQueryEngine
SQLAutoVectorQueryEngine
RetryQueryEngine
RetrySourceQueryEngine
RetryGuidelineQueryEngine
PandasQueryEngine
JSONalyzeQueryEngine
KnowledgeGraphQueryEngine
FLAREInstructQueryEngine
SimpleMultiModalQueryEngine
SQLTableRetrieverQueryEngine
PGVectorSQLQueryEngine

# ...

RouterQueryEngine # Selector, QueryEngineTool
SubQuestionQueryEngine # SubQuestionGenerator
```

# 8: Building Chatbots and Agents with LlamaIndex
- Technical requirements
- Understanding chatbots/聊天机器人 and agents/智能体
  - Discovering `ChatEngine`
  - Understanding the different chat modes
    - `ChatMemoryBuffer`
    - chat store: `SimpleChatStore`, `RedisChatStore`
    - chat mode: `SimpleChatEngine`, `ContextChatEngine`, `CondenseQuestionChatEngine`/浓缩, `CondensePlusContextChatEngine`
- Implementing agentic strategies/智能策略 in our apps
  - Building tools and `ToolSpec` classes for our agents
    - `QueryEngineTool`
    - `FunctionTool`
    - ex `ToolSpec`
      - `DatabaseToolSpec`: `llama-index-tools-database`
  - Understanding reasoning loops/推理循环
  - `OpenAIAgent`
  - `ReActAgent`
  - How do we interact with agents?
    - `chat()`, `query()`
  - Enhancing our agents with the help of utility tools
    - `OnDemandLoaderTool`
    - `LoadAndSearchToolSpec`
  - Using the LLMCompiler agent for more advanced scenarios
  - Using the low-level Agent Protocol API
- Hands-on – implementing conversation tracking for PITS

Figure 8.2 – The ChatOps paradigm

Figure 8.8 – The reasoning loop in an agent

# 9: Customizing and Deploying Our LlamaIndex Project
- Technical requirements
- Customizing our RAG components
  - How **LLaMA** and **LLaMA 2** changed the open source landscape
  - Running a local LLM using **LM Studio**
  - Routing between LLMs using services such as **Neutrino** or **OpenRouter**
    - https://www.neutrinoapp.com `llama-index-llms-neutrino`
    - https://openrouter.ai
  - What about customizing embedding models?
  - Leveraging the Plug and Play convenience of using **Llama Packs**
    - example: https://developers.llamaindex.ai/python/framework-api-reference/packs/zephyr_query_engine/ `llama-index-packs-zephyr-query-engine`
  - Using the **Llama CLI**
- Using advanced tracing and evaluation techniques: 0.10.20: callbacks -> instrumentation
  - Tracing our RAG workflows using **Phoenix** https://phoenix.arize.com
  - Evaluating our RAG system
    - retrieval quality, generation quality, faithfulness, efficiency, robustness
    - the Phoenix framework evaluation features
    - Retrieval-Augmented Generation Assessment (RAGAS)
- Introduction to deployment with **Streamlit**
- HANDS-ON – a step-by-step deployment guide
  - Deploying our PITS project on Streamlit Community Cloud

Figure 9.4 – A diagram of the Neutrino smart routing feature

# 10: Prompt Engineering Guidelines and Best Practices
- Technical requirements
- Why prompts are your secret weapon
- Understanding how LlamaIndex uses prompts
- Customizing default prompts
  - Using advanced prompting techniques in LlamaIndex
- The golden rules of prompt engineering
  - Accuracy and clarity in expression/表达的准确性和清晰度
  - Directiveness/指令性
  - Context quality/上下文质量
  - Context quantity/上下文数量
  - Required output format/所需输出格式
  - Inference cost/推理成本
  - Overall system latency/系统整体延迟
  - Choosing the right LLM for the task/为任务选择合适的LLM
    - model architecture
    - model size
    - inference speed
    - chat models
    - instruct models
    - codex models
    - summarization models
    - question-answering models
  - Common methods used for creating effective prompts/创建有效提示的常用方法
    - few-shot prompting: k-shot prompting
      - Brown et al. (2020), **Language Models are Few-Shot Learners**. https://doi.org/10.48550/arXiv.2005.14165
    - chain-of-thought(CoT) prompting
      - Wei et al. (2023), **Chain-of-Thought Prompting Elicits Reasoning in Large Language Models**. https://doi.org/10.48550/arXiv.2201.11903
    - self-consistency
      - Wang et al. (2023), **Self-Consistency Improves Chain of Thought Reasoning in Language Models**. https://doi.org/10.48550/arXiv.2203.11171
    - tree of thoughts(ToT) prompting
      - Yao et al.(2023), **Tree of Thoughts: Deliberate Problem Solving with Large Language Models**. https://doi.org/10.48550/arXiv.2305.10601
    - prompt chaining 

Table 10.1 – An overview of the more advanced prompting techniques provided by LlamaIndex
- https://docs.llamaindex.ai/en/stable/examples/prompts/advanced_prompts.html

# 11: Conclusion and Additional Resources
- Other projects and further learning
  - The LlamaIndex examples collection
  - Moving forward – Replit bounties
  - The power of many – the LlamaIndex community
- Key takeaways, final words, and encouragement
  - On the future of RAG in the larger context of generative AI
  - A small philosophical nugget for you to consider

# See Also
* Lewis, Patrick et al. **Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks**. arXiv:2005.11401 [cs.CL] (https://arxiv.org/abs/2005.11401). 2020.
* LoRA: Low-Rank Adaptation of Large Language Models. https://ar5iv.labs.arxiv.org/html/2106.09685
  * https://github.com/microsoft/LoRA
* Massive Text Embedding Benchmark (MTEB) Leaderboard: https://huggingface.co/spaces/mteb/leaderboard
* Advanced Retrieval Strategies: https://developers.llamaindex.ai/python/framework/optimizing/advanced_retrieval/advanced_retrieval/
* Liu et al., **Lost in the Middle: How Language Models Use Long Contexts** (2023) – https://arxiv.org/abs/2307.03172
* [What Are the Benefits of ChatOps? - IBM](https://www.ibm.com/think/insights/benefits-of-chatops)
* Yao, S., et al. (2022), **ReAct: Synergizing Reasoning and Acting in Language Models**. https://arxiv.org/abs/2210.03629
* Kim, S., et al. (2023), **An LLM Compiler for Parallel Function Calling**. https://arxiv.org/abs/2312.04511
* Es et al. (2023), **RAGAS: Automated Evaluation of Retrieval Augmented Generation**. https://doi.org/10.48550/
arXiv.2309.15217

tools
- OpenAI API
- Streamlit
- PyPDF - https://github.com/py-pdf/pypdf
- python-docx2txt - https://github.com/ankushshah89/python-docx2txt
- wikipedia, llama-index-readers-wikipedia
- Replit

> is Agent Protocol https://agentprotocol.ai/ outdated?
```markdown
Yes, from the perspective of the current AI ecosystem, the Agent Protocol (agentprotocol.ai) is outdated.
While its website and basic spec remain online, the AI Agent infrastructure layer has underwent massive consolidation. The industry has shifted away from Agent Protocol toward more specialized, scalable, and vendor-backed communication frameworks.
------------------------------
## Why Agent Protocol Fell Behind## 1. Overly Simple Scope (Just a REST Wrapper)

* What Agent Protocol Did: It defined a very basic REST API specification (e.g., POST /agent/tasks to create a task, and GET /agent/tasks/{id}/steps to poll for updates).
* The Reality of Modern Agents: Real-world agents are no longer just simple back-and-forth web workers. They require sophisticated streaming protocols, complex state machines, event-driven loops, and multi-agent consensus, which a rigid HTTP polling schema fails to optimize.

## 2. The Rise of Dominant Competitors
The problem of "standardizing agents" has been broken down into three distinct, specialized protocols backed by major industry heavyweights:

* Anthropic’s **Model Context Protocol (MCP)**:
* The Focus: Connecting LLMs to Tools and Data.
   * The Impact: MCP has effectively become the industry standard for tool-calling interfaces. Developed by Anthropic and rapidly adopted across the ecosystem (including IDEs like Cursor, database vendors, and development frameworks), MCP allows any model to securely read local files, call enterprise APIs, and browse developer environments using a unified client-server architecture.
* Linux Foundation's **Agent2Agent (A2A) Protocol**:
* The Focus: Inter-Agent Communication.
   * The Impact: Initially spearheaded by Google and moved under the open-source governance of the Linux Foundation, the A2A protocol solves how autonomous agents from different companies securely handshake, authenticate, negotiate capabilities, and pass sub-tasks to one another.
* **The AG-UI (Agent-User Interaction) Protocol**:
* The Focus: Real-time UX and Streaming States.
   * The Impact: An event-driven WebSocket and Server-Sent Events (SSE) standard that dictates how complex, multi-step agent graphs render adaptive UI components, handle user interruptions, and maintain chat histories on frontend interfaces.

## 3. Abandonment by Major Frameworks
While popular frameworks like LangChain (LangGraph) or AutoGen originally added experimental compatibility layers for Agent Protocol, they have largely abandoned active development for it. Production systems instead use the framework's native orchestration APIs (such as the LangGraph cloud API engine), which are custom-built for complex data-routing graphs.
------------------------------
## 2026 Architectural Recommendations
If you are designing a brand-new AI Agent architecture today, do not build it around agentprotocol.ai. Instead, utilize this modern, decoupled protocol stack:

| Architectural Challenge                                            | Recommended Modern Standard                                                       |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------- |
| Connecting your agent to enterprise tools, local files, and APIs   | Implement Model Context Protocol (MCP)                                            |
| Orchestrating agent workflows and complex execution graphs         | Use LangGraph or LlamaIndex Workflows                                             |
| Enabling cross-organizational agent collaboration (Agent-to-Agent) | Follow the Linux Foundation's A2A Project[](https://github.com/a2aproject/A2A)    |
| Streaming agent tokens, thoughts, and UI cards to the browser      | Adopt the AG-UI Protocol Specification[](https://github.com/ag-ui-protocol/ag-ui) |

Are you trying to solve a tool-integration challenge (giving your agent access to databases/local environments) or an orchestration challenge (managing how multiple agents speak to each other)? I can point you toward the exact open-source boilerplate for your specific use case.
```
