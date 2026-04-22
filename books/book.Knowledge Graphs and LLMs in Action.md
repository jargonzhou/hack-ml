# Knowledge Graphs and LLMs in Action

- Part 1 Foundations of hybrid intelligent systems: 1-2/混合智能系统
- Part 2 Building knowledge graphs from structured data sources: 3-4/从结构化数据源构建KG
- Part 3 Building knowledge graphs from text: 5-8/从文本构建KG
- Part 4 Machine learning on knowledge graphs: 9-12/KG上机器学习
- Part 5 Information retrieval with knowledge graphs and LLMs: 13-15/基于KG和LLM的信息检索

# 1 Knowledge graphs and LLMs: A killer combination

KG provide the explicit, verifiable and updatable knowledge representation that LLMs often lack,
LLM offer the natural language understanding and generation capabilities that make complex knowledge structures more accessible.

## 1.1 Knowledge graphs
## 1.2 Large language models

LLM building blocks and differentiating characteristics
- tokenization
- high-dim embedding
- transformers & attentionlarge dataset for pretraining
- transfer learning
- generation capacity

## 1.3 KGs and LLMs: Stronger together
## 1.4 The paradigm shift in data-driven applications
- The four pillars of knowledge graphs
## 1.5 Building data-driven applications using KGs and LLMs
- Example use case: Drug discovery and development
- Example use case: Conversational AI for customer support
- Deciding whether to use a KG
## 1.6 Knowledge graph technologies

paradigms
- RDF, SPARQL
- Labeled Property Graph(LPG), openCypher/Gremlin

organizing principle
- Taxonomies and ontologies

## 1.7 How do we teach KGs and LLMs?

# 2 Intelligent systems: A hybrid approach/智能系统: 混合方式
## 2.1 What is intelligence?

Figure 2.1 A high-level schema of an intelligent system. It is made of two component types: knowledge bases/知识库 and reasoning engines/推理引擎. Each type can have multiple instances based on the system’s tasks.
- input: Task/Question
- Knowledge acquisition
  - Environment Context
  - Data sources
- Intelligent system
  - Knowledge bases
  - Reasoning engines
- output: Action/Suggestion/Answer

## 2.2 Designing an intelligent system
- What is an intelligent system?
- Categories of intelligent systems
  - intelligent autonomous systems/智能自主系统
  - intelligent advisory systems (IASs)/智能咨询系统  <---
- Characteristics of an intelligent system
## 2.3 Knowledge acquisition and representation/知识获取和表示
## 2.4 Reasoning/推理
## 2.5 Reasoning engines
- Limitations of a pure deductive reasoning engine

Figure 2.11 The deductive reasoner/演绎推理器. The knowledge base is created by transforming data sources. The deductive reasoner uses logical statements applied to segments of the knowledge base to act or to provide suggestions.

- Using inductive reasoning and ML

Figure 2.12 An inductive reasoner/归纳推理器. Constructing the knowledge base requires more effort; it is not a simple transformation. This reasoning engine can abstract from the knowledge base and work under some level of uncertainty.

- The role of LLMs in the reasoning engine
## 2.6 A KG approach to IASs


# 3 Create your first knowledge graph from ontologies
## 3.1 Knowledge graph building: Warmup
- Business and domain understanding/业务和领域理解
- Data understanding/数据理解
## 3.2 Understanding knowledge graph technologies
- RDF or LPG? A goal-driven discussion
- Representing edge properties with RDF and LPG
  - RDF: n-ary relations
  - RDF: named graphs
  - RDF-star: add properties to edges
## 3.3 Building a knowledge graph
- Ontology ingestion and processing with neosemantics
- Annotation ingestion and processing
## 3.4 Querying the data
## 3.5 Reasoning over the KG

# 4 From simple networks to multisource integration/多源集成
## 4.1 Biomedical knowledge graphs and applications
## 4.2 Multi-omic applications of KGs
- Creating a KG from the PPI and protein-disease networks
- High-level analysis of the resulting KGs
- Domain-specific analysis of the PPI and disease KG
## 4.3 Pharmaceutical applications of KGs
- Deep analysis of the Hetionet knowledge graph
- LLM-assisted interpretation of pathway analysis results
## 4.4 Clinical applications of KGs
- LLM-guided clinical decision support analysis

# 5 Extracting domain-specific knowledge from unstructured data/从非结构化数据提取领域特定知识
## 5.1 The archives challenge
## 5.2 Key concepts of knowledge extraction
- Recognizing named entities
- Extracting relations
## 5.3 Building KGs with large language models
- Using LLMs
- Prompt engineering examples
- Prompt engineering guidelines
- KG building: Traditional NLP or LLMs?

# 6 Building knowledge graphs with large language models/使用LLM构建KG

Figure 6.1 Path from domain-specific unstructured textual data toward KG insights. The steps rely on state-of-the-art ML models, such as optical character recognition for document digitization, named entity recognition and relation extraction systems, entity resolution, and GraphML.

## 6.1 Transforming an archive to a KG
- Graph modeling
- Creating a metagraph
- Normalization and cleansing
- Graph-based entity resolution
## 6.2 Intellectual network analysis: The value of graphs
## 6.3 Next steps in the Rockefeller Archive Center project
## 6.4 The value of knowledge graphs in the LLM era

# 7 Named entity disambiguation/命名实体消歧/NED
## 7.1 From recognition to disambiguation
## 7.2 Understanding named entity disambiguation
## 7.3 Domain-based NED and LLMs
## 7.4 Business and domain understanding
- Context
- Use case definition
## 7.5 Understanding the data
- Unstructured data
- Domain ontologies
## 7.6 Building a SoHO knowledge graph
- Defining the schema
- Processing and ingesting documents
- Disambiguating and ingesting medical entities
- Processing, loading, and mapping ontologies
- Generating entity co-occurrences
## 7.7 KG-based use cases
- Conceptual search
- Structured knowledge-based search
- KG-based interpretability and discovery
- Uncovering new knowledge

# 8 NED with open LLMs and domain ontologies
## 8.1 Understanding limitations of traditional NED systems
## 8.2 Ingesting the domain ontology
## 8.3 Setting up the model with Ollama and Llama 3.1 8B
## 8.4 End-to-end NED process
- Named entity recognition
- Candidate selection
- Candidate disambiguation
## 8.5 Conclusions


# 9 Machine learning on knowledge graphs: A primer approach
## 9.1 Machine learning on graphs: Why?
## 9.2 Machine learning on graphs: What?
- Node classification
- Link prediction (a.k.a. relationship prediction)
- Clustering and community detection
- Graph classification
## 9.3 Machine learning on graphs: How?
- Node classification and link prediction
- Graph classification
- Graph clustering

# 10 Graph feature engineering/图特征工程: Manual and semiautomated approaches
## 10.1 Manual node features
- Degree
- Triangles
- Density
- Geodesic (or shortest) path
- Closeness
- Betweenness
- PageRank
- Prediction
## 10.2 Manual relationship features
- Node-based representation
- Path-based features
## 10.3 Semiautomated feature extraction
- Performing ReFeX manually
- Performing ReFeX automatically with code

# 11 Graph representation learning/图表示学习 and graph neural networks/图神经网络/GNN
## 11.1 Embeddings in graph representation learning
- Understanding graph embeddings: From discrete to continuous
- Real-world applications and examples
## 11.2 The encoder–decoder model
- The encoder: Converting graph structure to vectors
- The decoder: Reconstructing graph properties
- The power of the framework
- Node2Vec: An example of an encoder–decoder framework
## 11.3 Shallow embeddings: A first approach to graph representation
- Understanding shallow embeddings
- Limitations of shallow embeddings
## 11.4 Embeddings in knowledge graphs
- Loss function
- Multirelationship decoder
## 11.5 Message passing and graph neural networks
- The message-passing framework: A neural conversation
- Motivation and intuition: Why message passing works
- The basic GNN model
- Message passing with self-loops
## 11.6 Generalized aggregation and update methods
- Neighborhood normalization
- Neighborhood attention
- Multihead attention and transformer connections
- Generalized update methods
## 11.7 The synergy of GNNs and LLMs

# 12 Node classification and link prediction with GNNs/节点分类, 链接预测
## 12.1 Node classification for anti-money laundering applications
- Input data
- Graph processor: Data preparation
- Graph processor: Homogeneous PyG graph
- Encoder–decoder architecture
- Evaluation and analysis
## 12.2 Link prediction for movie recommendations
- Input data
- Graph processor: Data preparation
- Graph processor: Heterogeneous PyG graph
- Encoder–decoder architecture
- Evaluation and analysis


# 13 Knowledge graph–powered retrieval-augmented generation/KG增强的RAG
## 13.1 AI agents
## 13.2 Chatting with the LLM
## 13.3 Challenges in the production environment
## 13.4 Chatting with the AI about private data
- Retrieval-augmented generation
- Vector-based RAG limitations
- Graph RAG
- Reasoning agents
- Let’s chat with our KG

# 14 Asking a KG questions with natural language/自然语言提问
## 14.1 Querying a knowledge graph in the policing domain
- Enabling domain experts with knowledge graphs
## 14.2 RAG for KG querying: Capabilities and challenges
- RAG effectiveness with complete context
- RAG fragility with incomplete retrieval
## 14.3 Schema-based approach for querying KGs
- Understanding and using graph schemas
## 14.4 Think like an expert: Using metadata for enhanced querying
## 14.5 Intent detection: Understanding user expectations
- Classifying by visualization type
- Is it data, documentation, or just complaining?
## 14.6 From schema to LLM-ready context
- Schema extraction and representation
- Enriching schemas with descriptive annotations
- A practical approach to schema representation
## 14.7 It’s time to think: Understanding LLM reasoning
- The order matters: Answer first vs. reasoning first
- Thinking in queries: From text to Cypher
- Structuring output for reliable query generation
## 14.8 Response summarization: From results to insights

# 15 Building a QA agent with LangGraph/QA智能体
## 15.1 Building the LangGraph pipeline
- System architecture overview
- Configuring pipeline components
- Schema translation service
- State management design
- Pipeline agent implementation
- Pipeline integration layer
## 15.2 Streamlit application
- Application overview
- LangGraph integration
## 15.3 Expert-emulating investigation
- Identifying the initial case
- Spatial analysis of surveillance coverage
- Vehicle pattern detection
- Context-aware request refinement
- Historical record analysis
## 15.4 Future directions and enhancements
- Learning from use
- Enhancing core capabilities
- Advanced evolution paths

# A: Introduction to graphs
## A.1 What is a graph?
## A.2 Graphs as models of networks
## A.3 Representing graphs

# B: Neo4j
## B.1 Introduction to Neo4j
## B.2 Installing Neo4j
- Installing a Neo4j server
- Neo4j Desktop installation
## B.3 Cypher
## B.4 Installing plugins
- Installing APOC Core
- GDS installation
## B.5 Cleaning

# C: Building knowledge graphs from structured sources
## C.1 MicroRNA–disease association: Warmup
- Key concepts
- Business understanding
- Data understanding
## C.2 Building the miRNA knowledge graph
- Importing known miRNA–disease connections
- Importing the disease ontology
- Importing miRNA information
## C.3 Exploring and analyzing the miRNA KG

# See Also
* Graph-Powered Machine Learning
* Wirth, Rüdiger, and Jochen Hipp. 2000. “CRISP-DM: Towards a Standard Process Model for Data Mining.”

tools
- Python 3.8+
- Neo4j Enterprise Edition 5.20.0
  - Neo4j Desktop 1.6.1
  - APOC library 5.20.0
  - Neosemantics plugin 5.20.0
- NetworkX
- transformers
- LangChain
- Streamlit
- OpenAPI
- Claude.ai
- [rdflib](https://github.com/RDFLib/rdflib): RDFLib is a Python library for working with RDF, a simple yet powerful language for representing information.
- [scispaCy](https://github.com/allenai/scispacy): A full spaCy pipeline and models for scientific/biomedical documents.
- Amazon Textract
- Ollama, Llama 3.1 8B

datasets, ontologies
- [Human Phenotype Ontology (HPO)](https://hpo.jax.org/app/) annotated dataset
- [Open Biological and Biomedical Ontology Foundry](https://obofoundry.org/)
- [Ubergraph](https://github.com/INCATools/ubergraph): Integrated OBO ontology store
- miRNA–disease connections
  - [Human miRNA Disease Database (HMDD](http://www.cuilab.cn/hmdd)
  - [Database of Differentially Expressed miRNAs in Human Cancers (dbDEMC)](https://www.biosino.org/dbDEMC)
  - [miR2Disease](www.mir2disease.org)
  - [Unified Medical Language System (UMLS)](https://www.nlm.nih.gov/research/umls) ontology
  - [miRBase dataset](www.mirbase.org)
  - [miRDB dataset](https://mirdb.org)
- [Hetionet(heterogeneous network)](https://het.io/)
- [The Clinical Knowledge Graph (CKG)](https://github.com/MannLabs/CKG) from Albertos Santos et al
- [DOID](www.diseaseontology.org): the disease ontology identifier
- [Unified Medical Language System (UMLS)](https://www.nlm.nih.gov/research/umls/index.html): The UMLS, or Unified Medical Language System, is a set of files and software that brings together many health and biomedical vocabularies and standards.
- SNOMED: Systematized Nomenclature Of MEDicine
