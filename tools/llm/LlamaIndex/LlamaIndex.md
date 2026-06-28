# LlamaIndex
* https://github.com/run-llama/llama_index
* https://developers.llamaindex.ai/python/framework/

LlamaIndex OSS (by LlamaIndex) is an open-source framework to build agentic applications.

> LlamaIndex is the framework for Context-Augmented LLM Applications

LlamaIndex imposes no restriction on how you use LLMs. You can use LLMs as auto-complete, chatbots, agents, and more. It just makes using them easier. We provide tools like:
- **Data connectors/数据连接** ingest your existing data from their native source and format. These could be APIs, PDFs, SQL, and (much) more.
- **Data indexes/数据索引** structure your data in intermediate representations that are easy and performant for LLMs to consume.
- **Engines/引擎** provide natural language access to your data. For example:
    - Query engines/查询引擎 are powerful interfaces for question-answering (e.g. a RAG flow).
    - Chat engines/聊天引擎 are conversational interfaces for multi-message, “back and forth” interactions with your data.
- **Agents/智能体** are LLM-powered knowledge workers augmented by tools, from simple helper functions to API integrations and more.
- **Observability/Evaluation/可观测性/评估** integrations that enable you to rigorously experiment, evaluate, and monitor your app in a virtuous cycle.
- **Workflows/工作流** allow you to combine all of the above into an event-driven system/事件驱动的系统 far more flexible than other, graph-based approaches.

# Components
* https://developers.llamaindex.ai/python/framework/module_guides/

Core Components
- Models/模型
  - Introduction to Models - Overview of model components
  - LLMs - Language models for text generation and reasoning
  - Embeddings - Convert text to vector representations
  - Multi Modal - Work with images, audio, and other non-text data
- Prompts/提示词
  - Introduction to Prompts - Overview of prompt engineering
  - Usage Patterns - Learn how to effectively use prompts
- Loading/加载
  - Introduction to Loading - Overview of data loading capabilities
  - Documents and Nodes - Core data structures
  - SimpleDirectoryReader - Easy document loading
  - Data Connectors - Connect to external data sources
  - Node Parsers / Text Splitters - Split documents into chunks
  - Ingestion Pipeline - End-to-end document processing
- Indexing/建索引
  - Introduction to Indexing - Overview of indexing approaches
  - Index Guide - Comprehensive guide to indices
  - Vector Store Index - Semantic search with vectors
  - Property Graph Index - Graph-based indexing
- Storing/存储操作
  - Introduction to Storing - Overview of storage components
  - Vector Stores - Store embeddings for retrieval
  - Document Stores - Persist document collections
  - Index Stores - Store index metadata
- Querying/执行查询
  - Introduction to Querying - Overview of query components
  - Query Engines - Process and answer queries
  - Chat Engines - Build conversational interfaces
  - Retrieval - Retrieve relevant context
  - Response Synthesis - Generate coherent answers

Advanced Components
- Agents/智能体
  - Introduction to Agents - Overview of agent capabilities
  - Memory - Add conversational memory to agents
  - Tools - Extend capabilities with external tools
- Workflows/工作流
  - Introduction to Workflows - Build complex, multi-step AI workflows
- Evaluation/评估
  - Introduction to Evaluation - Overview of evaluation frameworks
  - Usage Patterns - Test and improve your applications
  - LlamaDatasets - Standardized evaluation datasets
- Observability/可观测性
  - Introduction to Observability - Overview of monitoring capabilities
  - Instrumentation - Monitor and debug your applications
- Settings/设置
  - Settings Configuration - Configure global LlamaIndex settings

## Deploying/部署
- Agents
  - Memory
  - Module Guides
- Tools
  - Chat Engines
  - Module Guides
  - Usage Pattern
- Query Engine
  - Module Guides
  - Response Modes
  - Streaming
  - Supporting Modules
  - Usage Pattern
## Evaluating/评估
- Evaluating
- Contributing A `LabelledRagDataset`
- Evaluating Evaluators with `LabelledEvaluatorDataset`'s
- Evaluating With `LabelledRagDataset`'s
- Modules
- Usage Pattern (Response Evaluation)
- Usage Pattern (Retrieval)

Evaluation and benchmarking are crucial concepts in LLM development. To improve the performance of an LLM app (RAG, agents), you must have a way to measure it.

LlamaIndex offers key modules to measure the quality of generated results. We also offer key modules to measure retrieval quality.
- **Response Evaluation/响应评估**: Does the response match the retrieved context? Does it also match the query? Does it match the reference answer or guidelines?
- **Retrieval Evaluation/检索评估**: Are the retrieved sources relevant to the query?

## Indexing/建索引
- Indexing
- Document Management
- How Each Index Works
- LlamaCloudIndex + LlamaCloudRetriever
- Using a Property Graph Index
- Metadata Extraction
- Module Guides
- Using VectorStoreIndex
## Loading/加载
- Loading Data
- Connector
- Data Connectors (LlamaHub)
- LlamaParse
- Module Guides
- Usage Pattern
- Documents And Nodes
- Documents / Nodes
- Defining and Customizing Documents
- Metadata Extraction Usage Pattern
- Defining and Customizing Nodes
- Ingestion Pipeline
- Ingestion Pipeline
- Transformations
- Node Parsers
- Node Parser Usage Pattern
- Node Parser Modules
- SimpleDirectoryReader
## MCP
- Model Context Protocol (MCP)
- Converting Existing LlamaIndex Workflows & Tools to MCP
- LlamaCloud MCP Servers & Tools
- Using MCP Tools with LlamaIndex
## Models/模型
- Models
- Embeddings
- Llms
- Using LLMs
- Using local models
- Available LLM integrations
- Customizing LLMs within LlamaIndex Abstractions
- Using LLMs as standalone modules
- Multi-modal models
- Prompts
- Prompts
- Prompt Usage Pattern
## Observability/可观测性
- Observability
- Callbacks
- Callbacks
- Token Counting - Migration Guide
- Instrumentation

NOTE: The `instrumentation` module (available in llama-index v0.10.20 and later) is meant to replace the legacy `callbacks` module. During the deprecation period, the llama-index library supports both modules as a means to instrument your LLM application. However, at some point after all of the existing integrations have moved over to the new `instrumentation` module, we will no longer support `callbacks` module.


## Querying/执行查询
- Querying
- Node Postprocessors
- Node Postprocessor
- Node Postprocessor Modules
- Response Synthesizers
- Response Synthesizer
- Response Synthesis Modules
- Retriever
- Retriever
- Retriever Modes
- Retriever Modules
- Router
- Routers
- Structured Outputs
- Structured Outputs
- Output Parsing Modules
- Pydantic Programs
- (Deprecated) Query Engines + Pydantic Outputs
## Storing/存储操作
- Storing
- Chat Stores
- Customizing Storage
- Document Stores
- Index Stores
- Key-Value Stores
- Persisting & Loading Data
- Vector Stores
## Supporting Modules/支持性模块
- Migrating from ServiceContext to Settings
- Configuring Settings
- Supporting Modules

# Use cases
* https://developers.llamaindex.ai/python/framework/use_cases

- [Prompting](https://developers.llamaindex.ai/python/framework/use_cases/prompting): Learn advanced prompting techniques with LlamaIndex
- [Question-Answering (RAG)](https://developers.llamaindex.ai/python/framework/use_cases/q_and_a): Build retrieval-augmented generation systems
- [Chatbots](https://developers.llamaindex.ai/python/framework/use_cases/chatbots): Create conversational AI applications
- [Structured Data Extraction](https://developers.llamaindex.ai/python/framework/use_cases/extraction): Extract structured information from unstructured text
- [Agents](https://developers.llamaindex.ai/python/framework/use_cases/agents): Develop autonomous AI agents
- [Multi-Modal Applications](https://developers.llamaindex.ai/python/framework/use_cases/multimodal): Work with text, images, and other data types
- [Fine-Tuning](https://developers.llamaindex.ai/python/framework/use_cases/fine_tuning): Customize models for your specific use cases

# Examples
* https://developers.llamaindex.ai/python/examples/


Agents
- Function Calling Agent: Learn the basics of Function Calling Agents and `AgentWorkflow`
- React Agent: Use the ReAct (Reasoning and Acting) pattern with agents
- Code Act Agent: Agents that can write and execute code
- Multi-Agent Workflow: Build a multi-agent workflow with `AgentWorkflow`

Agentic Workflows
- Function Calling Agent from Scratch: Build a Function Calling agent from scratch
- React Agent: Build a ReAct agent
- CodeAct Agent from Scratch: Build a CodeAct agent from scratch
- Basic RAG: Simple RAG workflow implementation
- Advanced Text-to-SQL: Use LlamaIndex to generate SQL queries and execute them

LLM Integrations
- OpenAI: Use OpenAI models (GPT-3.5, GPT-4, etc.)
- Anthropic: Integrate with Claude models
- Bedrock: Work with Meta’s Llama 3 models
- Gemini/Vertex: Use Google’s Gemini/Vertex models
- Mistral: Integrate with Mistral AI models
- Ollama: Use Ollama models locally

Embedding Models
- OpenAI Embeddings: OpenAI’s text embedding models
- Cohere Embeddings: Cohere’s embedding models
- HuggingFace Embeddings: Use open-source embeddings from HuggingFace locally
- Jina Embeddings: Jina AI’s embedding models
- Ollama Embeddings: Ollama’s embedding models
- VoyageAI Embeddings: VoyageAI’s embedding models

Vector Stores
- Pinecone: Pinecone vector database integration
- Chroma: Chroma vector store
- Weaviate: Weaviate vector database
- Qdrant: Qdrant vector database
- MongoDB Atlas: MongoDB Atlas Vector Search
- Redis: Redis vector database
- Milvus: Milvus vector database
- Azure AI Search: Azure AI Search vector database

# Integrations

## Embeddings
-  Aleph Alpha Embeddings
-  Anyscale Embeddings
-  Baseten Embeddings
-  Bedrock Embeddings
-  Embeddings with Clarifai
-  Cloudflare Workers AI Embeddings
-  CohereAI Embeddings
-  Custom Embeddings
-  DashScope Embeddings
-  Databricks Embeddings
-  DeepInfra
-  Elasticsearch Embeddings
-  Qdrant FastEmbed Embeddings
-  Fireworks Embeddings
-  Google Gemini Embeddings
-  GigaChat
-  Google GenAI Embeddings
-  Google Palm Embeddings
-  Heroku LLM Managed Inference Embedding
-  Local Embeddings with HuggingFace
-  IBM watsonx.ai
-  Local Embeddings with IPEX-LLM on Intel CPU
-  Local Embeddings with IPEX-LLM on Intel GPU
-  Isaacus Embeddings
-  Jina 8K Context Window Embeddings
-  Jina Embeddings
-  LangChain Embeddings
-  Llamafile Embeddings
-  LLMRails Embeddings
-  MistralAI Embeddings
-  Mixedbread AI Embeddings
-  ModelScope Embeddings
-  Nebius Embeddings
-  Netmind AI Embeddings
-  Nomic Embedding
-  NVIDIA NIMs
-  Oracle Cloud Infrastructure (OCI) Data Science Service
-  Oracle Cloud Infrastructure Generative AI
-  Ollama Embeddings
-  OpenAI Embeddings
-  Local Embeddings with OpenVINO
-  Optimized Embedding Model using Optimum-Intel
-  Oracle AI Vector Search: Generate Embeddings
-  PremAI Embeddings
-  Interacting with Embeddings deployed in Amazon SageMaker Endpoint with LlamaIndex
-  Text Embedding Inference
-  TextEmbed - Embedding Inference Server
-  Together AI Embeddings
-  Upstage Embeddings
-  Interacting with Embeddings deployed in Vertex AI Endpoint with LlamaIndex
-  VoyageAI Embeddings
-  YandexGPT

## LLM
-  AI21
-  Aleph Alpha
-  Anthropic
-  Anthropic Prompt Caching
-  Anyscale
-  Apertis
-  ASI LLM
-  Azure AI model inference
-  Azure OpenAI
-  Baseten Cookbook
-  Bedrock
-  Bedrock Converse
-  Cerebras
-  Clarifai LLM
-  Cleanlab Trustworthy Language Model
-  Cohere
-  CometAPI
-  DashScope LLMS
-  Databricks
-  DeepInfra
-  DeepSeek
-  EverlyAI
-  Featherless AI LLM
-  Fireworks
-  Fireworks Function Calling Cookbook
-  Friendli
-  Gemini
-  Google GenAI
-  Grok 4
-  Groq
-  Helicone AI Gateway
-  Heroku LLM Managed Inference
-  Hugging Face LLMs
-  IBM watsonx.ai
-  IPEX-LLM on Intel CPU
-  IPEX-LLM on Intel GPU
-  Konko
-  LangChain LLM
-  LiteLLM
-  Replicate - Llama 2 13B
-  🦙 x 🦙 Rap Battle
-  Llama API
-  LlamaCPP
-  llamafile
-  LLM Predictor
-  LM Studio
-  LocalAI
-  Maritalk
-  MistralRS LLM
-  MistralAI
-  ModelScope LLMS
-  Monster API <> LLamaIndex
-  MyMagic AI LLM
-  Nebius LLMs
-  Netmind AI LLM
-  Neutrino AI
-  NVIDIA NIMs
-  NVIDIA NIMs
-  NVIDIA TensorRT-LLM
-  NVIDIA LLM Text Completion API
-  NVIDIA Triton
-  Oracle Cloud Infrastructure Data Science
-  Oracle Cloud Infrastructure Generative AI
-  OctoAI
-  Ollama LLM
-  Ollama - Gemma
-  OpenAI
-  OpenAI JSON Mode vs. Function Calling for Data Extraction
-  OpenAI Responses API
-  OpenRouter
-  OpenVINO LLMs
-  OpenVINO GenAI LLMs
-  Optimum Intel LLMs optimized with IPEX backend
-  Using Opus 4.1 with LlamaIndex
-  AlibabaCloud-PaiEas
-  PaLM
-  Perplexity
-  [Pipeshift](https://pipeshift.com)
-  Portkey
-  Predibase
-  PremAI LlamaIndex
-  Client of Baidu Intelligent Cloud's Qianfan LLM Platform
-  RunGPT
-  Interacting with LLM deployed in Amazon SageMaker Endpoint with LlamaIndex
-  SambaNova Systems
-  Together AI LLM
-  Upstage
-  Vercel AI Gateway
-  Vertex AI
-  Replicate - Vicuna 13B
-  vLLM
-  Xorbits Inference
-  Yi LLMs

## Retrievers/检索器
-  Auto Merging Retriever
-  Comparing Methods for Structured Retrieval (Auto-Retrieval vs. Recursive Retrieval)
-  Bedrock (Knowledge Bases)
-  BM25 Retriever
-  Composable Objects
-  Activeloop Deep Memory
-  Ensemble Retrieval Guide
-  Chunk + Document Hybrid Retrieval with Long-Context Embeddings (Together.ai)
-  Pathway Retriever
-  Reciprocal Rerank Fusion Retriever
-  Recursive Retriever + Node References + Braintrust
-  Recursive Retriever + Node References
-  Relative Score Fusion and Distribution-Based Score Fusion
-  Router Retriever
-  Simple Fusion Retriever
-  Auto-Retrieval from a Vectara Index
-  Vertex AI Search Retriever
-  connect to VideoDB
-  You.com Retriever

## Vector Stores/向量存储
-  Alibaba Cloud MySQL
-  Alibaba Cloud OpenSearch Vector Store
-  Google AlloyDB for PostgreSQL - `AlloyDBVectorStore`
-  Amazon Neptune - Neptune Analytics vector store
-  AnalyticDB
-  ApertureDB as a Vector Store with LlamaIndex.
-  Astra DB
-  Simple Vector Store - Async Index Creation
-  Awadb Vector Store
-  Test delete
-  Azure AI Search
-  Azure CosmosDB MongoDB Vector Store
-  Azure Cosmos DB No SQL Vector Store
-  Azure Postgres Vector Store
-  Bagel Vector Store
-  Bagel Network
-  Baidu VectorDB
-  Cassandra Vector Store
-  Auto-Retrieval from a Vector Database
-  Chroma Vector Store
-  Chroma + Fireworks + Nomic with Matryoshka embedding
-  Chroma
-  ClickHouse Vector Store
-  Google Cloud SQL for PostgreSQL - `PostgresVectorStore`
-  Couchbase Vector Store
-  DashVector Vector Store
-  Databricks Vector Search
-  IBM Db2 Vector Store and Vector Search
-  Deep Lake Vector Store Quickstart
-  DocArray Hnsw Vector Store
-  DocArray InMemory Vector Store
-  Dragonfly and Vector Store
-  DuckDB
-  Auto-Retrieval from a Vector Database
-  Elasticsearch
-  Elasticsearch Vector Store
-  Epsilla Vector Store
-  Faiss Vector Store
-  Firestore Vector Store
-  Gel Vector Store
-  Hnswlib
-  Hologres
-  Jaguar Vector Store
-  Advanced RAG with temporal filters using LlamaIndex and KDB.AI vector store
-  LanceDB Vector Store
-  Lantern Vector Store (auto-retriever)
-  Lantern Vector Store
-  Lindorm
-  Milvus Vector Store with Async API
-  Milvus Vector Store with Full-Text Search
-  Milvus Vector Store With Hybrid Search
-  Milvus Vector Store
-  Milvus Vector Store - Metadata Filter
-  MongoDB Atlas Vector Store
-  MongoDB Atlas + Fireworks AI RAG Example
-  MongoDB Atlas + OpenAI RAG Example
-  Moorcheh Vector Store Demo
-  MyScale Vector Store
-  Neo4j Vector Store - Metadata Filter
-  Neo4j vector store
-  Nile Vector Store (Multi-tenant PostgreSQL)
-  ObjectBox VectorStore Demo
-  OceanBase Vector Store
-  Opensearch Vector Store
-  Oracle AI Vector Search: Vector Store
-  pgvecto.rs
-  A Simple to Advanced Guide with Auto-Retrieval (with Pinecone + Arize Phoenix)
-  Pinecone Vector Store - Metadata Filter
-  Pinecone Vector Store
-  Pinecone Vector Store - Hybrid Search
-  Postgres Vector Store
-  Hybrid Search with Qdrant BM42
-  Qdrant Hybrid Search
-  Hybrid RAG with Qdrant: multi-tenancy, custom sharding, distributed setup
-  Qdrant Vector Store - Metadata Filter
-  Qdrant Vector Store - Default Qdrant Filters
-  Qdrant Vector Store
-  Redis Vector Store
-  Relyt
-  Rockset Vector Store
-  S3VectorStore Integration
-  Simple Vector Store
-  Local Llama2 + VectorStoreIndex
-  Llama2 + VectorStoreIndex
-  Simple Vector Stores - Maximum Marginal Relevance Retrieval
-  S3/R2 Storage
-  Supabase Vector Store
-  TablestoreVectorStore
-  Tair Vector Store
-  Tencent Cloud VectorDB
-  TiDB Vector Store
-  Timescale Vector Store (PostgreSQL)
-  txtai Vector Store
-  Typesense Vector Store
-  Upstash Vector Store
-  Google Vertex AI Vector Search
-  Google Vertex AI Vector Search v2.0
-  Vespa Vector Store demo
-  Auto-Retrieval from a Weaviate Vector Database
-  Weaviate Vector Store Metadata Filter
-  Weaviate Vector Store
-  Weaviate Vector Store - Hybrid Search
-  WordLift Vector Store
-  Zep Vector Store

# Ecosystem

- [llama_deploy](https://github.com/run-llama/llama_deploy): Deploy your agentic workflows as production microservices. - This project is deprecated. To serve workflows, use [llama-agents](https://github.com/run-llama/workflows-py) instead.
- [LlamaHub](https://llamahub.ai/): A large (and growing!) collection of custom data connectors. integrations include utilities such as Data Loaders, Agent Tools, Llama Packs, and Llama Datasets.
- [SEC Insights](https://secinsights.ai/): A LlamaIndex-powered application for financial research
- [create-llama](https://www.npmjs.com/package/create-llama): A CLI tool to quickly scaffold LlamaIndex projects

# Llama Packs
* https://developers.llamaindex.ai/python/framework/community/llama_packs/

Llama Packs are a community-driven hub of prepackaged modules/templates you can use to kickstart your LLM app.

This directly tackles a big pain point in building LLM apps; every use case requires cobbling together custom components and a lot of tuning/dev time. Our goal is to accelerate that through a community led effort.

They can be used in two ways:
- On one hand, they are **prepackaged modules** that can be initialized with parameters and run out of the box to achieve a given use case (whether that’s a full RAG flow, application template, or more). You can also import submodules (e.g. LLMs, query engines) to use directly.
- On the other hand, LlamaPacks are **templates** that you can inspect, modify, and use.

All packs are found on LlamaHub.

# LlamaAgents
* https://developers.llamaindex.ai/python/llamaagents/overview/
* https://github.com/run-llama/llama-agents

LlamaAgents is the most advanced way to build agent workflows. Author and run multi-step document agents from scratch locally using our open-source **Agent Workflows**, or build and deploy them in the cloud with our vibe-coding **Agent Builder** in LlamaCloud — without wiring up infrastructure, persistence, or deployment yourself.

Stitch together Parse, Extract, Split, Classify, and custom operations into Workflows that perform knowledge tasks on your documents. When you need full control, it’s real Python underneath: fork and extend without a rewrite. Agent Workflows give you event-driven orchestration with branching, parallelism, human-in-the-loop review, durability, and observability.

Components
- **[`llamactl` CLI](https://developers.llamaindex.ai/python/llamaagents/llamactl/getting-started/)**: Development and deployment for local workflow apps. Initialize from [starter templates](https://developers.llamaindex.ai/python/llamaagents/llamactl-reference/commands-init/), serve locally, and deploy to LlamaCloud or export for self-hosting.
- **[Agent Workflows](https://developers.llamaindex.ai/python/llamaagents/workflows/)**: The event-driven orchestration framework at the core. Use it as an async library in your own code, or let `llamactl` serve it. Built-in durability and [observability](https://developers.llamaindex.ai/python/llamaagents/workflows/observability/).
- **[Agent Builder](https://developers.llamaindex.ai/python/llamaagents/cloud/builder/)**: In [LlamaCloud](https://cloud.llamaindex.ai/?utm_source=github&utm_medium=li_github) → **Agents** → **Builder**. Natural-language, vibe-coding interface to create document workflows; the agent generates real Python you can deploy or take to GitHub.
- **[`llama-cloud-services`](https://developers.llamaindex.ai/python/cloud/)**: LlamaCloud document primitives (Parse, Extract, Classify), [Agent Data](https://developers.llamaindex.ai/python/llamaagents/cloud/agent-data-overview/) for structured storage, and vector indexes. `llamactl` handles authentication when deploying to the cloud.
- **[@llamaindex/ui](https://developers.llamaindex.ai/python/llamaagents/llamactl/ui-hooks/)**: React hooks for workflow-powered frontends. Deploy alongside your backend with `llamactl`.
- **[Workflows Client](https://developers.llamaindex.ai/python/llamaagents/workflows/deployment/#using-workflowclient-to-interact-with-servers)**: Call deployed workflows via REST API or typed Python client.

## Agent Workflows
* https://developers.llamaindex.ai/python/llamaagents/workflows/

A workflow is an event-driven, step-based way to control the execution flow of an application//工作流是一种事件驱动的, 基于步骤的控制应用执行流的方法.

Your application is divided into sections called steps. A step receives an event, does some work, and returns another event. That returned event triggers the next step whose type annotation accepts it.

That is the whole model. A step can call an LLM, run retrieval, ask for human input, update shared state, or dispatch a batch of work. The event types describe the edges of the workflow, and regular Python describes the logic inside each edge.

Other frameworks and LlamaIndex itself have attempted to solve this problem previously with directed acyclic graphs (DAGs)/有向无环图 but these have a number of limitations that workflows do not:
- Logic like loops and branches/循环和分支逻辑 needed to be encoded into the edges of graphs, which made them hard to read and understand.
- Passing data between nodes/在节点间传递数据 in a DAG created complexity around optional and default values and which parameters should be passed.
- DAGs did not feel natural to developers trying to develop complex, looping, branching AI applications.


`llama-index-workflows`
- Introduction
  - `Workflow`, `@step`, `StartEvent`, `StopEvent`
  - examples
- Branches and loops
- Concurrent execution of workflows
- Writing async workflows
- Streaming events
- Managing State
  - Each workflow run has a `Context`, and each context has a state store.
- Custom start and stop events
- Resource Objects
  - `from workflows.resource import Resource`
  - Config-backed Resources: `from workflows.resource import ResourceConfig`
  - Chaining Resources
- Workflows from unbound functions
- Error handling
  - `from workflows.retry_policy import ...`
- Human in the Loop
  - `InputRequiredEvent`, `HumanResponseEvent`
  - `ctx.wait_for_event()`
- Writing durable workflows
- DBOS Durable Execution
  - `llama-agents-dbos`
  - DBOS provides high-performance, easy-to-use durable workflows built on top of Postgres. - https://docs.dbos.dev/why-dbos
- Drawing a Workflow
  - `llama-index-utils-workflow`
  - Use the debugger UI
- Testing Workflows
  - `from workflows.testing import WorkflowTestRunner`
- Observability
  - OpenTelemetry: `llama-index-observability-otel`
  - Arize Phoenix
  - Langfuse
  - Opik
- Run Your Workflow as a Server
  - `llama-agents-server`
  - `WorkflowServer`
  - Workflow Debugger UI
- Python Client
  - `llama-agents-client`
  - `WorkflowClient`

## llamactl

llamactl is the local development and deployment CLI for LlamaAgents. It can scaffold an app, run the app server locally, and manage cloud deployments from your terminal.


```shell
# globally
uv tool install -U llamactl
# project
uv add --dev llamactl
```

# See Also
* [Building A RAG Ebook “Librarian” Using LlamaIndex](https://huggingface.co/learn/cookbook/rag_llamaindex_librarian) - Hugging Face Open-Source AI Cookbook
* [list LlamaIndex books, from introduction level to advanced level](./ai_generated/gen-llamaindex-books.md)