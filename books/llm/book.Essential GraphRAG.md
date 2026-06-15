# Essential GraphRAG: Knowledge Graph-Enhanced RAG

# 1 Improving LLM accuracy/提升LLM准确率
- 1.1 Introduction to LLMs
- 1.2 Limitations of LLMs
  - 1.2.1 Knowledge cutoff problem
  - 1.2.2 Outdated information
  - 1.2.3 Pure hallucinations
  - 1.2.4 Lack of private information
- 1.3 Overcoming the limitations of LLMs
  - 1.3.1 Supervised finetuning
  - 1.3.2 Retrieval-augmented generation
- 1.4 Knowledge graphs as the data storage for RAG applications

# 2 Vector similarity search and hybrid search/向量相似度搜索和混合搜索
- 2.1 Components of a RAG architecture
  - 2.1.1 The retriever/检索器
  - 2.1.2 The generator/生成器
- 2.2 RAG using vector similarity search
  - 2.2.1 Application data setup
  - 2.2.2 The text corpus
    - “Einstein’s Patents and Inventions” (Caudhuri, 2017): https://arxiv.org/abs/1709.00666
  - 2.2.3 Text chunking
  - 2.2.4 Embedding model
    - OpenAI’s embedding models: `text-embedding-3-small`
    - `all-MiniLM-L12-v2` via Sentence Transformers from Hugging Face 
  - 2.2.5 Database with vector similarity search function
    - Neo4j
  - 2.2.6 Performing vector search
  - 2.2.7 Generating an answer using an LLM
- 2.3 Adding full-text search to the RAG application to enable hybrid search
  - 2.3.1 Full-text search index
  - 2.3.2 Performing hybrid search
- 2.4 Concluding thoughts

# 3 Advanced vector retrieval strategies/高级向量检索策略
- 3.1 Step-back prompting/回退式提示
- 3.2 Parent document retriever/父文档检索器
  - OpenAI `tiktoken`
  - 3.2.1 Retrieving parent document strategy data
- 3.3 Complete RAG pipeline

# 4 Generating Cypher queries from natural language questions/从自然语言问题生成Cypher查询
- 4.1 The basics of query language generation
- 4.2 Where query language generation fits in the RAG pipeline
- 4.3 Useful practices for query language generation
  - 4.3.1 Using few-shot examples for in-context learning
  - 4.3.2 Using database schema in the prompt to show the LLM the structure of the knowledge graph
  - 4.3.3 Adding terminology mapping to semantically map the user question to the schema
  - 4.3.4 Format instructions
- 4.4 Implementing a text2cypher generator using a base model
  - Neo4j Python diver, OpenAPI API
- 4.5 Specialized (finetuned) LLMs for text2cypher
  - https://huggingface.co/datasets/neo4j/text2cypher
  - https://huggingface.co/neo4j
- 4.6 What we’ve learned and what text2cypher enables

# 5 Agentic RAG/智能RAG
- GPT-3.5, GPT-4, ReAct(https://arxiv.org/abs/2210.03629)
- 5.1 What is agentic RAG?
  - 5.1.1 Retriever agents/检索器智能体
  - 5.1.2 The retriever router/检索器路由
  - 5.1.3 Answer critic/答案评论家
- 5.2 Why do we need agentic RAG?
- 5.3 How to implement agentic RAG
  - 5.3.1 Implementing retriever tools
    - `text2cypher_description`
    - `movie_info_by_title_description`
    - `movies_info_by_actor_description`
    - `answer_given_description`
  - 5.3.2 Implementing the retriever router
    - Handling tool calls/处理工具调用
    - Continuous query updating/持续的查询更新
    - Routing the questions to the relevant retrievers/路由问题到相关的检索器
  - 5.3.3 Implementing the answer critic
  - 5.3.4 Tying it all together

# 6 Constructing knowledge graphs with LLMs/使用LLM构建知识图谱
- 6.1 Extracting structured data from text
  - 6.1.1 Structured Outputs model definition
    - OpenAI Structured Output feature in API: https://developers.openai.com/api/docs/guides/structured-outputs
    - Pydantic
  - 6.1.2 Structured Outputs extraction request
  - 6.1.3 CUAD dataset
    - https://github.com/tomasonjo/kg-rag/blob/main/data/license_agreement.txt
- 6.2 Constructing the graph
  - 6.2.1 Data import
  - 6.2.2 Entity resolution
  - 6.2.3 Adding unstructured data to the graph

# 7 Microsoft’s GraphRAG implementation/微软的GraphRAG实现
- https://github.com/microsoft/graphrag
- 7.1 Dataset selection
  - The Odyssey: https://www.gutenberg.org/cache/epub/1727/pg1727.txt
- 7.2 Graph indexing/图索引
  - 7.2.1 Chunking
  - 7.2.2 Entity and relationship extraction/实体和关系抽取
    - `Instructions for entity and relationship extraction`
  - 7.2.3 Entity and relationship summarization/实体和关系汇总
    - `Instructions for entity and relationship summarization`
  - 7.2.4 Community detection and summarization/社区检测和汇总
    - `Instructions for community summarization`
- 7.3 Graph retrievers/图检索器
  - 7.3.1 Global search/全局搜索
    - `The system prompt for the map part of the retriever`
    - `The system prompt for the reduce part of the retriever`
    - `global_retriever`
  - 7.3.2 Local search/局部搜索
    - `The system prompt for the local search`
    - `local_search`

Figure 7.1 Microsoft’s GraphRAG pipeline. (Image from Edge et al., 2024, licensed under CC BY 4.0)

# 8 RAG application evaluation/RAG应用评估
- Ragas, the Movies dataset
- 8.1 Designing the benchmark dataset/设计基准数据集
  - 8.1.1 Coming up with test examples
- 8.2 Evaluation/评估
  - 8.2.1 Context recall/上下文召回
    - `Context recall evaluation`
  - 8.2.2 Faithfulness/忠实度
    - `Faithfulness statement breakdown`
    - `Faithfulness evaluation`
  - 8.2.3 Answer correctness/答案正确性
    - `Answer correctness evaluation`
  - 8.2.4 Loading the dataset/加载数据集
    - https://github.com/tomasonjo/kg-rag/blob/main/data/benchmark_data.csv
  - 8.2.5 Running evaluation/运行评估
  - 8.2.6 Observations/观察
- 8.3 Next steps

Figure 8.1 Evaluating different steps of a RAG pipeline
- User
- v 1. ask a question
- LLM
- v 2. tool selection               <- evaluate accurate tool selection
- Retrieval tools
- v 3. retrieve relevant context    <- evaluate relevancy of retrieved contxt
- Retrieved context
- v 4. generate answer              <- evaluate answer generation
- LLM

# A. The Neo4j environment
- A.1 Cypher query language
- A.2 Neo4j installation
  - A.2.1 Neo4j Desktop installation
  - A.2.2 Neo4j Docker installation
  - A.2.3 Neo4j Aura
- A.3 Neo4j Browser configuration
- A.4 Movies dataset
  - A.4.1 Loading via the Neo4j Query Guide
  - A.4.2 Trying the online version
  - A.4.3 Loading via Cypher

# See Also
