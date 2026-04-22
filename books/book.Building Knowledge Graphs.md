# Building Knowledge Graphs

# 1. Introducing Knowledge Graphs (KGs)

labeled property graph model/带标签的属性图模型
- node: properties, labels
- relationship: type, direction, properties

Knowledge graphs are a specific type of graph with an emphasis on **contextual understanding**. 
Knowledge graphs are interlinked sets of **facts** that describe real-world entities, events, or things and their interrelations in a human- and machine-understandable format.

Critically, knowledge graphs must have an **organizing principle/组织原则** so that a user (or a computer system) can reason about the underlying data.

# 2. Organizing Principles for Building Knowledge Graphs

taxonomy, ontology
- RDS Schema
- OWL(Web Ontology Langauge)
- SKOS(Simple Knowledge Organization System)

# 3. Graph Databases

Neo4j, Cypher Query Language
- nodes: `()`
- labels on nodes: `:Person`, `:Place`
- relationships: `-[:LIVES_IN]->`
- key-value properties: `{name: 'Rosa'}`, `{city:'Berlin', country:'DE'}`

```cypher
CREATE
MATCH
MERGE

WHERE SET/REMOVE
```

- graph local queries
- graph global queries
- calling functions and procedures: `CALL`, APOC (Awesome Procedures on Cypher)
- `EXPLAIN`, `PROFILE`

Neo4j Internals
- query processing: index-free-adjacency
  - fixed-length records for nodes and relationships, multiply the record ID by its size goves its offset in file.
- ACID transactions: Raft

# 4. Loading Knowledge Graph Data

- Neo4j Data Importer: CSV
- Cypher `LOAD CSV`
- `neo4j-admin import`

# 5. Integrating Knowledge Graphs with Information Systems/与信息系统集成

- data fabrics/数据架构
- Neo4j driver
- graph federation with composite databases: Neo4j Enterprise Edition `CREATE COMPOSITE DATABASE`
- server-side procedures: APOC
```cypher
apoc.load.driver
apoc.mongodb.find
apoc.load.json
```
- data virtualization: `apoc.dv.*`
- custom functions and procedures: `@Procedure`, `@UserFunction` - see 'The Neo4j Java Reference'
- other tools
  - GraphQL
  - Kafka Connect Neo4j Connector
  - Nro4j Spark Connector
  - Apache Hop for ETL

# 6. Enriching Knowledge Graphs with Data Science/数据科学增强

graph data science
- graph alogorithms
  - Neo4j Graph Data Science (GDS)
- production considerations: primary/secondary servers, causal barrier/因果屏障 for reading latest write
- enrich the knowledge graph: `mutate`, `write`

# 7. Graph-Native Machine Learning/图原生机器学习

integrate graphs and ML
- in-graph maching learning/在图机器学习: predict how a graph will evolve over time
```cypher
gds.alpha.linkprediction.preferentialAttachment
gds.beta.pipeline.linkPrediction
```
- graph feature engineering/图特征工程: extract features from the graph to build a high-quality external predictive model


# 8. Mapping Data with Metadata Knowledge Graphs/元数据

distributed data stewardship/分布式数据管理
- datasets connected to data platform
- tasks and data pipelines
- data sinks
- use relationships to connect data and metadata

# 9. Identity Knowledge Graphs/身份

entity resolution/master data management: 实体消解
- KYC: Knowing Your Customer
- steps
  - data preparation
  - entity matching
  - build/update a persisted record of master entities

```cypher
gds.nodeSimilarity
apoc.text.jaroWinklerDistance
```

# 10. Pattern Detection Knowledge Graphs/模式检测

- fraud detection
  - the community detection algorithms
  - the fraud-ring pattern
```cypher
gds.louvain
```
- skills matching

# 11. Dependency Knowledge Graphs/依赖

dependency modeling
- dependencies as a graph
- qualified dependencies
- semantics of multidependency: additive/aggregate, redundant/protection
- impact progagation with Cypher
- validation
  - no cycles
  - aggregate multidependencies add up to the expected total
  - consumption does not exceed production
  - redundant dependency configuration aligns with threshold definitions
- complex dependency processing
  - SPOF (Single-Point-of-Failure) analysis
  - Root cause analysis

# 12. Semantic Search and Similarity/语义搜索和相似性

- from strings to things: annotate documents with entities
  - text annotation
  - NER: Named-Entity Recognition/命名实体识别
- document similarity for recommendations
  - content-based: you may also like X
  - collaborative filtering: customer like you also bought/read/watch X
  - the cold start problem
- making the annotation semantic with an organizing principle
  - entity disambiguation/实体消歧

# 13. Talking to Your Knowledge Graph

- natural language as input to KG
  - fact extraction/事实提取
  - question answering
- natural language as output
  - conversational interface/对话接口
    - rule-based
  - natural language query
  - natural langauge generation from KGs
    - subject-predicate-object
    - apply to node properties
    - annotate KGs' organizing principle: ontology of the KG
- KG as a tool providing structured context for NLP tasks, at lexical or conceptual level
  - custom entity extractor which has specialized domain knowledge/特殊领域知识的事实提取
  - lexical database: WordNet - semantic relationships between lexical concepts
- graph-based semantic similarity
  - path similarity
  - Leacock-Chodorow similarity
  - Wu and Palmer similarity

# 14. From Knowledge Graphs to Knowledge Lakes/知识湖

A knowledge lake is an architecture and usage pattern that is itself a knowledge graph and can subsume other knowledge graphs and nongraph data.

# See Also
*  Knowledge Graphs: Data in Context for Responsive Businesses.
*  Graph Databases by Ian Robinson, Jim Webber, and Emil Eifrem (O’Reilly)
*  The Graph Traversal Pattern by Marko A. Rodriguez and Peter Neubauer
*  Graph Data Science for Dummies by Dr. Alicia Frame and Zach Blumenfeld (Wiley)
*  Wikidata, DBPedia
*  Graph Algorithms

tools
- Neo4j Bloom, APOC
- Linkurious
- Hugging Face - Token Classification subtasks
- Google Cloud Platform (GCP) Natural Langauge API
- Diffbot Natural Langauge API
- spaCy
- NLTK

ontologies
- SNOMED CT: for clinical documentation and reporting
- Library of Congress Classification (LCC): widely used in academia
- Financial Industry Business Ontology (FIBO): for finance and business
- Schema.org: a collaborative effort to create a shared ontology for the web
- Dublin Core Metadata Initiative (DCMI): which has many schemas used for describing web resources and more
