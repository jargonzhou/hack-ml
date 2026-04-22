# Graph Algorithms: Practical Examples in Apache Spark and Neo4j

action: [graph-algorithms](../codes/graph-algorithms/README.md)

# 1. Introduction
## What Are Graphs?
## What Are Graph Analytics and Algorithms?
## Graph Processing, Databases, Queries, and Algorithms
- OLTP and OLAP
## Why Should We Care About Graph Algorithms?
## Graph Analytics Use Cases

# 2. Graph Theory and Concepts/图理论和概念
## Terminology
## Graph Types and Structures/图类型和结构
- Random, Small-World, Scale-Free Structures
## Flavors of Graphs/图的种类
- Connected Versus Disconnected Graphs
- Unweighted Graphs Versus Weighted Graphs
- Undirected Graphs Versus Directed Graphs
- Acyclic Graphs Versus Cyclic Graphs
- Sparse Graphs Versus Dense Graphs
- Monopartite, Bipartite, and k-Partite Graphs
## Types of Graph Algorithms/图算法类型
- Pathfinding/路径查找
- Centrality/中心性
- Community Detection/社区检测

# 3. Graph Platforms and Processing/图平台和处理
## Graph Platform and Processing Considerations
- Platform Considerations
- Processing Considerations
## Representative Platforms
- Selecting Our Platform
- Apache Spark
- Neo4j Graph Platform

```shell
pip install pyspark graphframes

export SPARK_VERSION="spark-2.4.0-bin-hadoop2.7"
./${SPARK_VERSION}/bin/pyspark \
  --driver-memory 2g \
  --executor-memory 6g \
  --packages graphframes:graphframes:0.7.0-spark2.4-s_2.11
```

# 4. Pathfinding and Graph Search Algorithms/路径查找和图搜索算法
## Example Data: The Transport Graph
- Importing the Data into Apache Spark
- Importing the Data into Neo4j
## Breadth First Search/宽度优先搜索
- Breadth First Search with Apache Spark
## Depth First Search/深度优先搜索
## Shortest Path/最短路径
- When Should I Use Shortest Path?
- Shortest Path with Neo4j
- Shortest Path (Weighted) with Neo4j
- Shortest Path (Weighted) with Apache Spark
- Shortest Path Variation: A*
- Shortest Path Variation: Yen’s k-Shortest Paths
## All Pairs Shortest Path/所有最短路径对
- A Closer Look at All Pairs Shortest Path
- When Should I Use All Pairs Shortest Path?
- All Pairs Shortest Path with Apache Spark
- All Pairs Shortest Path with Neo4j
## Single Source Shortest Path/单源最短路径
- When Should I Use Single Source Shortest Path?
- Single Source Shortest Path with Apache Spark
- Single Source Shortest Path with Neo4j
## Minimum Spanning Tree/最小生成树
- When Should I Use Minimum Spanning Tree?
- Minimum Spanning Tree with Neo4j
## Random Walk/随机游走
- When Should I Use Random Walk?
- Random Walk with Neo4j

# 5. Centrality Algorithms/中心性算法
## Example Graph Data: The Social Graph
- Importing the Data into Apache Spark
- Importing the Data into Neo4j
## Degree Centrality/度中心性
- Reach
- When Should I Use Degree Centrality?
- Degree Centrality with Apache Spark
## Closeness Centrality/接近中心性
- When Should I Use Closeness Centrality?
- Closeness Centrality with Apache Spark
- Closeness Centrality with Neo4j
- Closeness Centrality Variation: Wasserman and Faust
- Closeness Centrality Variation: Harmonic Centrality
## Betweenness Centrality/介数中心性
- When Should I Use Betweenness Centrality?
- Betweenness Centrality with Neo4j
- Betweenness Centrality Variation: Randomized-Approximate Brandes
## PageRank
- Influence
- The PageRank Formula
- Iteration, Random Surfers, and Rank Sinks
- When Should I Use PageRank?
- PageRank with Apache Spark
- PageRank with Neo4j
- PageRank Variation: Personalized PageRank

# 6. Community Detection Algorithms/社区检测算法
## Example Graph Data: The Software Dependency Graph
- Importing the Data into Apache Spark
- Importing the Data into Neo4j
## Triangle Count and Clustering Coefficient/三角形计数和聚类系数
- Local Clustering Coefficient
- Global Clustering Coefficient
- When Should I Use Triangle Count and Clustering Coefficient?
- Triangle Count with Apache Spark
- Triangles with Neo4j
- Local Clustering Coefficient with Neo4j
## Strongly Connected Components/强连通分量
- When Should I Use Strongly Connected Components?
- Strongly Connected Components with Apache Spark
- Strongly Connected Components with Neo4j
## Connected Components/连通分量
- When Should I Use Connected Components?
- Connected Components with Apache Spark
- Connected Components with Neo4j
## Label Propagation/标签传播
- Semi-Supervised Learning and Seed Labels
- When Should I Use Label Propagation?
- Label Propagation with Apache Spark
- Label Propagation with Neo4j
## Louvain Modularity/Louvain模块度
- When Should I Use Louvain?
- Louvain with Neo4j
- Validating Communities

# 7. Graph Algorithms in Practice/实践
## Analyzing Yelp Data with Neo4j
- Yelp Social Network
- Data Import
- Graph Model
- A Quick Overview of the Yelp Data
- Trip Planning App
- Travel Business Consulting
- Finding Similar Categories
## Analyzing Airline Flight Data with Apache Spark
- Exploratory Analysis
- Popular Airports
- Delays from ORD
- Bad Day at SFO
- Interconnected Airports by Airline

# 8. Using Graph Algorithms to Enhance Machine Learning/使用图算法增强机器学习
## Machine Learning and the Importance of Context
- Graphs, Context, and Accuracy
## Connected Feature Extraction and Selection/连通特征提取与选择
- Graphy Features
- Graph Algorithm Features
## Graphs and Machine Learning in Practice: Link Prediction/链接预测
- Tools and Data
- Importing the Data into Neo4j
- The Coauthorship Graph
- Creating Balanced Training and Testing Datasets
- How We Predict Missing Links
- Creating a Machine Learning Pipeline
- Predicting Links: Basic Graph Features
- Predicting Links: Triangles and the Clustering Coefficient
- Predicting Links: Community Detection

# A. Additional Information and Resources
- Other Algorithms
- Neo4j Bulk Data Import and Yelp
- APOC and Other Neo4j Tools
- Finding Datasets
- Assistance with the Apache Spark and Neo4j Platforms
- Training

# See Also
* Systemic Delay Propagation in the US Airport Network
* Hierarchical Structure and the Prediction of Missing Links in Network
* Graph Databases, by Ian Robinson, Jim Webber, and Emil Eifrem (O’Reilly)
* Introduction to Graph Theory, by Richard J. Trudeau (Dover)
* Introduction to Graph Theory, Fifth Ed., by Robin J. Wilson (Pearson)
* Graph Theory and Its Applications, Third Ed., by Jonathan L. Gross, Jay Yellen, and Mark Anderson (Chapman and Hall)
* Spark: The Definitive Guide, by Bill Chambers and Matei Zaharia (O’Reilly)
* A*: A Formal Basis for the Heuristic Determination of Minimum Cost Paths
* Yen’s k-Shortest Paths: Finding the K Shortest Loopless Paths in a Network
* The Problem of the Random Walk
* Centrality in Social Networks: Conceptual Clarification - Degree Centrality
* Social Network Analysis: Methods and Applications by Stanley Wasserman and Katherine Faust - Closeness Centrality Variation
* An Improved Equivalence Algorithm - Connected Components
* Near Linear Time Algorithm to Detect Community Structures in Large-Scale Networks - Label Propagation
* ArnetMiner: Extraction and Mining of Academic Social Networks by J. Tang et al

tools:
- Neo4j
  - the Neo4j Graph Algorithms library
  - the Neo4j Awesome Procedures on Cypher (APOC) library
  - Neo4j Desktop
  - py2neo
- Apache Spark: spark-2.4.0-binhadoop2.7
  - [GraphFrames](https://github.com/graphframes/graphframes): succeeded [GraphX](https://spark.apache.org/docs/latest/graphx-programming-guide.html)
  - PySpark
  - the Spark Graph project
  - Spark MLlib
    - https://github.com/julioasotodv/spark-tree-plotting
- Graph compute engines: Pregel, PACT, Giraph, GraphLab, Graph-Engine, Apache Spark
- Graph databases
- pandas

other libraries
```markdown
> 图算法支持库有哪些, 特定语言: Python, Java, Scala, Go

针对您提到的编程语言，以下是目前主流的图算法支持库，涵盖了单机计算和分布式处理两大场景：
## 1. Python
Python 拥有最活跃的数据科学生态，主要库包括：

* NetworkX: 最知名的通用图论库。包含大量经典的图算法（路径查找、中心性、社区检测等），适合中小规模图的分析和原型开发。
* igraph (python-igraph): 以 C 语言为核心，性能显著优于 NetworkX，尤其是在处理大规模图结构时。
* Graph-tool: 使用 C++ 和 Boost 库实现，利用多线程并行处理，是目前单机性能最强的 Python 图库之一。
* PyTorch Geometric (PyG) & DGL: 专门用于图神经网络 (GNN) 和图机器学习的库，支持深度学习框架。
* Neo4j GDS Python Client: 专门用于在 Python 环境中远程调用 Neo4j GDS 引擎的高性能算法。 [1, 2, 3, 4, 5, 6] 

## 2. Java
Java 库通常在生产级稳定性和大规模内存处理上有优势：

* JGraphT: 逻辑最严密、功能最丰富的 Java 图论库，支持各种有向/无向图、超图，并内置了极广的算法集。
* Neo4j Graph Data Science (GDS): 虽然通常作为数据库插件使用，但其核心是用 Java 编写的，并提供 Java API（如 Pregel API）用于自定义算法开发。
* Apache Commons Graph: Apache 基金会的开源项目，专注于提供轻量级的图结构和基本算法。
* JUNG (Java Universal Network/Graph Framework): 经典的图库，特别强调图的视觉化表现。 [7, 8] 

## 3. Scala
由于 Scala 与大数据生态（尤其是 Spark）紧密结合，其图计算主要集中在分布式领域：

* Apache Spark GraphX: Spark 生态中最主流的分布式图计算框架，基于 Pregel 模型，适合处理包含数十亿节点的超大规模图数据。
* Graph for Scala: 旨在无缝集成到 Scala 集合库中的内存图库，提供函数式风格的图操作，适合中小型单机任务。
* GraphFrames: 在 Spark DataFrame 基础上构建，支持类似 SQL (Cypher) 的模式匹配查询，比 GraphX 更易用。 [2, 9, 10, 11, 12] 

## 4. Go
Go 的库通常更注重并发性能和轻量化：

* Gonum/graph: Gonum 科学计算套件的一部分，提供了一套干净的接口和常用算法（如 Dijkstra、A*、拓扑排序等）。
* Cayley: 本质上是一个图数据库，但它提供了强大的内置图处理引擎，常用于构建知识图谱。
* Dominik Braun / Graph: 一个现代、零依赖的泛型图库，利用 Go 1.18+ 的泛型特性实现。 [13] 

总结建议：

* 科研与快速原型：选 Python (NetworkX/igraph)。
* 企业级后端/高性能分析：选 Java (JGraphT)。
* TB 级超大规模分布式计算：选 Scala (Spark GraphX)。
* 云原生/高并发微服务：选 Go (Gonum)。

您是否需要我为您演示其中某个特定库（例如 NetworkX 或 JGraphT）的算法调用代码示例？

[1] [https://blog.tomsawyer.com](https://blog.tomsawyer.com/python-graph-visualization-libraries)
[2] [https://github.com](https://github.com/graphgeeks-lab/awesome-graph-universe)
[3] [https://github.com](https://github.com/CodeGraphContext/CodeGraphContext/issues/488)
[4] [https://medium.com](https://medium.com/data-science/graphs-with-python-overview-and-best-libraries-a92aa485c2f8)
[5] [https://juejin.cn](https://juejin.cn/post/7483364968659238948)
[6] [https://neo4j.com.cn](http://neo4j.com.cn/public/docs/graph-data-science-client/current/index.html#:~:text=%E4%B8%BA%E4%BA%86%E5%B8%AE%E5%8A%A9%E9%82%A3%E4%BA%9B%E4%BB%A5Python%20%E4%BD%9C%E4%B8%BA%E4%B8%BB%E8%A6%81%E8%AF%AD%E8%A8%80%E5%92%8C%E7%8E%AF%E5%A2%83%E7%9A%84Neo4j%20%E5%9B%BE%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%20%E7%94%A8%E6%88%B7%EF%BC%8C%E6%88%91%E4%BB%AC%E6%8F%90%E4%BE%9B%E4%BA%86%E5%90%8D%E4%B8%BA%20graphdatascience%20%E7%9A%84%E5%AE%98%E6%96%B9%E5%9B%BE%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%28GDS%29%20Python,%E6%AD%A4%E5%A4%96%EF%BC%8C%E5%AE%A2%E6%88%B7%E7%AB%AF%E7%89%B9%E5%AE%9A%E7%9A%84%E5%9B%BE%E3%80%81%E6%A8%A1%E5%9E%8B%E5%92%8C%E7%AE%A1%E9%81%93%E5%AF%B9%E8%B1%A1%E6%8F%90%E4%BE%9B%E4%BA%86%E6%96%B9%E4%BE%BF%E7%9A%84%E5%87%BD%E6%95%B0%EF%BC%8C%E5%A4%A7%E5%A4%A7%E5%87%8F%E5%B0%91%E4%BA%86%E4%BD%BF%E7%94%A8Cypher%20%E8%AE%BF%E9%97%AE%E5%92%8C%E6%93%8D%E4%BD%9C%E8%BF%99%E4%BA%9BGDS%20%E8%B5%84%E6%BA%90%E7%9A%84%E9%9C%80%E8%A6%81%E3%80%82%20GDS%20Python%20%E5%AE%A2%E6%88%B7%E7%AB%AF%E7%9A%84%E6%BA%90%E4%BB%A3%E7%A0%81%E5%8F%AF%E5%9C%A8GitHub%20%E8%8E%B7%E5%8F%96%E3%80%82%E5%A6%82%E6%9E%9C%E6%82%A8%E5%AF%B9%E5%A6%82%E4%BD%95%E6%94%B9%E8%BF%9B%E8%AF%A5%E5%BA%93%E6%9C%89%E5%BB%BA%E8%AE%AE%E6%88%96%E6%83%B3%E6%8A%A5%E5%91%8A%E9%97%AE%E9%A2%98%EF%BC%8C%E5%8F%AF%E4%BB%A5)
[7] [https://codemia.io](https://codemia.io/knowledge-hub/path/good_java_graph_algorithm_library_closed_1)
[8] [https://zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/681199537)
[9] [https://spark.apache.org](https://spark.apache.org/docs/latest/)
[10] [https://www.icertglobal.com](https://www.icertglobal.com/blog/graphx-graph-processing-in-apache-spark-with-scala-blog)
[11] [https://www.scala-graph.org](https://www.scala-graph.org/guides/core/index.html)
[12] https://www.scala-graph.org
[13] [https://www.geeksforgeeks.org](https://www.geeksforgeeks.org/blogs/open-source-graph-databases/)

```