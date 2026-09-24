# Graph Neural Networks in Action

# 1 Discovering graph neural networks
- Goals of this book
	- Catching up on graph fundamentals
- Graph-based learning
	- What are graphs?
	- Different types of graphs
	- Graph-based learning
	- What is a GNN?
	- Differences between tabular and graph data
- GNN applications: Case studies
	- Recommendation engines
	- Drug discovery and molecular science
	- Mechanical reasoning
- When to use a GNN?
	- Implicit relationships and interdependencies
	- High dimensionality and sparsity
	- Complex, nonlocal interactions
- Understanding how GNNs operate
	- Mental model for training a GNN
	- Unique mechanisms of a GNN model
	- Message passing


# 2 Graph embeddings
- Creating embeddings with Node2Vec
	- Loading data, setting parameters, and creating embeddings
	- Demystifying embeddings
	- Transforming and visualizing the embeddings
	- Beyond visualization: Applications and considerations of N2V embeddings
- Creating embeddings with a GNN
	- Constructing the embeddings
	- GNN vs. N2V embeddings
- Using node embeddings
	- Data preprocessing
	- Random forest classification
	- Embeddings in an end-to-end model
- Under the Hood
	- Representations and embeddings
	- Transductive and inductive methods
	- N2V: Random walks across graphs
	- Message passing as deep learning


# 3 Graph convolutional networks and GraphSAGE
- Predicting consumer product categories
	- Loading and processing the data
	- Creating our model classes
	- Model training
	- Model performance analysis
	- Our first product bundle
- Aggregation methods
	- Neighborhood aggregation
	- Advanced aggregation tools
	- Practical considerations in applying aggregation
- Further optimizations and refinements
	- Dropout
	- Model depth
	- Improving the baseline model’s performance
	- Revisiting the Marcelina product bundle
- Under the hood
	- Convolution methods
	- Message passing
	- GCN aggregation function
	- GCN in PyTorch Geometric
	- Spectral vs. spatial convolution
	- GraphSAGE aggregation function
	- GraphSAGE in PyTorch Geometric
- Amazon Products dataset


# 4 Graph attention networks
- Detecting spam and fraudulent reviews
- Exploring the review spam dataset
	- Explaining the node features
	- Exploratory data analysis
	- Exploring the graph structure
	- Exploring the node features
- Training baseline models
	- Non-GNN baselines
	- GCN baseline
- Training GAT models
	- Neighborhood loader and GAT models
	- Addressing class imbalance in model performance
	- Deciding between GAT and XGBoost
- Under the hood
	- Explaining attention and GAT models
	- Over-smoothing
	- Overview of key GAT equations


# 5 Graph autoencoders
- Generative models: Learning how to generate
	- Generative and discriminative models
	- Synthetic data
- Graph autoencoders for link prediction
	- Review of the Amazon Products dataset from chapter 3
	- Defining a graph autoencoder
	- Training a graph autoencoder to perform link prediction
- Variational graph autoencoders
	- Building a variational graph autoencoder
	- When to use a variational graph autoencoder
- Generating graphs using GNNs
	- Molecular graphs
	- Identifying new drug candidates
	- VGAEs for generating graphs
	- Generating molecules using a GNN
- Under the hood
	- Understanding link prediction tasks
	- The inner product decoder


# 6 Dynamic graphs: Spatiotemporal GNNs
- Temporal models: Relations through time
- Problem definition: Pose estimation
	- Setting up the problem
	- Building models with memory
- Dynamic graph neural networks
	- Graph attention network for dynamic graphs
- Neural relational inference
	- Encoding pose data
	- Decoding pose data using a GRU
	- Training the NRI model
- Under the hood
	- Recurrent neural networks
	- Temporal adjacency matrices
	- Combining autoencoders with RNNs
	- Gumbel-Softmax


# 7 Learning and inference at scale
- Examples in this chapter
	- Amazon Products dataset
	- GeoGrid
- Framing problems of scale
	- Root causes
	- Symptoms
	- Crucial metrics
- Techniques for tackling problems of scale
	- Seven techniques
	- General Steps
- Choice of hardware configuration
	- Types of hardware choices
	- Choice of processor and memory size
- Choice of data representation
- Choice of GNN algorithm
	- Time and space complexity
- Batching using a sampling method
	- Two concepts: Mini-batching and sampling
	- A glance at notable PyG samplers
- Parallel and distributed processing
	- Using distributed data parallel
	- Code example for DDP
- Training with remote storage
	- Example
- Graph coarsening
	- Example


# 8 Considerations for GNN projects
- Data preparation and project planning
	- Project definition
	- Project objectives and scope
- Designing graph models
	- Get familiar with the domain and use case
	- Constructing the graph dataset and schemas
	- Creating instance models
	- Testing and refactoring
- Data pipeline example
	- Raw data
	- The ETL step
	- Data exploration and visualization
	- Preprocessing and loading data into PyG
- Where to find graph data

# A: Discovering graphs
- Graph fundamentals
	- Graph properties
	- Characteristics of nodes and edges
	- Categories of graphs
- Graph representations
	- Basic graph data structures
	- Relational databases
	- How graphs are exposed
- Graph systems
	- Graph databases
	- Graph compute engines (or graph frameworks)
	- Visualization libraries
	- GNN libraries
- Graph algorithms
	- Traversal and search algorithms
	- Shortest path
- How to read GNN literature
	- Common graph notations

# B: Installing and configuring PyTorch Geometric
- Installing PyTorch Geometric
	- On Windows/Linux
	- On MacOS
	- Compatibility issues

# See Also

tools
- pstuil: Python system and process utilities library
- pynvml: Python bindings for NVIDIA Management Library

Graph datasets and semantic models
- Open Graph Benchmark (OGB)
  - Graph datasets and benchmarks
  - Social networks, drug discovery
  - https://ogb.stanford.edu/
- GraphChallenge Datasets
  - Graph datasets
  - Network science, biology
  - https://graphchallenge.mit.edu/data-sets
- Network Repository 
  - Graph datasets 
  - Network science, bioinformatics, machine learning, data mining, physics, and social science - http://networkrepository.com/
- SNAP Datasets 
  - Graph datasets 
  - Social networks, network science, road networks, commercial networks, finance 
  - http://snap.stanford.edu/data/
- Schema.org 
  - Semantic data model 
  - Internet web pages 
  - https://schema.org/
- Wikidata 
  - Semantic data model 
  - Wikipedia pages 
  - www.wikidata.org/
