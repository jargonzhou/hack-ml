# Artificial Intelligence: A Modern Approach

# Part I: Artificial Intelligence/人工智能
# 1 Introduction
## What Is AI?
### 1.1.1 Acting humanly: The Turing test approach
### 1.1.2 Thinking humanly: The cognitive modeling approach
### 1.1.3 Thinking rationally: The ``laws of thought'' approach
### 1.1.4 Acting rationally: The rational agent approach
### 1.1.5 Beneficial machines
## 1.2 The Foundations of Artificial Intelligence
### 1.2.1 Philosophy
### 1.2.2 Mathematics
### 1.2.3 Economics
### 1.2.4 Neuroscience
### 1.2.5 Psychology
### 1.2.6 Computer engineering
### 1.2.7 Control theory and cybernetics
### 1.2.8 Linguistics
## 1.3 The History of Artificial Intelligence
### 1.3.1 The inception of artificial intelligence (1943--1956)
### 1.3.2 Early enthusiasm, great expectations (1952--1969)
### 1.3.3 A dose of reality (1966--1973)
### 1.3.4 Expert systems (1969--1986)
### 1.3.5 The return of neural networks (1986--present)
### 1.3.6 Probabilistic reasoning and machine learning (1987--present)
### 1.3.7 Big data (2001--present)
### 1.3.8 Deep learning (2011--present)
## 1.4 The State of the Art
## 1.5 Risks and Benefits of AI


# 2 Intelligent Agents
## 2.1 Agents and Environments
## 2.2 Good Behavior: The Concept of Rationality
### 2.2.1 Performance measures
### 2.2.2 Rationality
### 2.2.3 Omniscience, learning, and autonomy
## 2.3 The Nature of Environments
### 2.3.1 Specifying the task environment
### 2.3.2 Properties of task environments
## 2.4 The Structure of Agents
### 2.4.1 Agent programs
### 2.4.2 Simple reflex agents
### 2.4.3 Model-based reflex agents
### 2.4.4 Goal-based agents
### 2.4.5 Utility-based agents
### 2.4.6 Learning agents
### 2.4.7 How the components of agent programs work


# Part II: Problem-solving/
# 3 Solving Problems by Searching
## 3.1 Problem-Solving Agents
### 3.1.1 Search problems and solutions
### 3.1.2 Formulating problems
## 3.2 Example Problems
### 3.2.1 Standardized problems
### 3.2.2 Real-world problems
## 3.3 Search Algorithms
### 3.3.1 Best-first search
### 3.3.2 Search data structures
### 3.3.3 Redundant paths
### 3.3.4 Measuring problem-solving performance
## 3.4 Uninformed Search Strategies
### 3.4.1 Breadth-first search
### 3.4.2 Dijkstra's algorithm or uniform-cost search
### 3.4.3 Depth-first search and the problem of memory
### 3.4.4 Depth-limited and iterative deepening search
### 3.4.5 Bidirectional search
### 3.4.6 Comparing uninformed search algorithms
## 3.5 Informed (Heuristic) Search Strategies
### 3.5.1 Greedy best-first search
### 3.5.2 A* search
### 3.5.3 Search contours
### 3.5.4 Satisficing search: Inadmissible heuristics and weighted A*
### 3.5.5 Memory-bounded search
### 3.5.6 Bidirectional heuristic search
## 3.6 Heuristic Functions
### 3.6.1 The effect of heuristic accuracy on performance
### 3.6.2 Generating heuristics from relaxed problems
### 3.6.3 Generating heuristics from subproblems: Pattern databases
### 3.6.4 Generating heuristics with landmarks
### 3.6.5 Learning to search better
### 3.6.6 Learning heuristics from experience


# 4 Search in Complex Environments
## 4.1 Local Search and Optimization Problems
### 4.1.1 Hill-climbing search
### 4.1.2 Simulated annealing
### 4.1.3 Local beam search
### 4.1.4 Evolutionary algorithms
## 4.2 Local Search in Continuous Spaces
## 4.3 Search with Nondeterministic Actions
### 4.3.1 The erratic vacuum world
### 4.3.2 AND—OR search trees
### 4.3.3 Try, try again
## 4.4 Search in Partially Observable Environments
### 4.4.1 Searching with no observation
### 4.4.2 Searching in partially observable environments
### 4.4.3 Solving partially observable problems
### 4.4.4 An agent for partially observable environments
## 4.5 Online Search Agents and Unknown Environments
### 4.5.1 Online search problems
### 4.5.2 Online search agents
### 4.5.3 Online local search
### 4.5.4 Learning in online search


# 5 Adversarial Search and Games
## 5.1 Game Theory
### 5.1.1 Two-player zero-sum games
## 5.2 Optimal Decisions in Games
### 5.2.1 The minimax search algorithm
### 5.2.2 Optimal decisions in multiplayer games
### 5.2.3 Alpha--Beta Pruning
### 5.2.4 Move ordering
## 5.3 Heuristic Alpha--Beta Tree Search
### 5.3.1 Evaluation functions
### 5.3.2 Cutting off search
### 5.3.3 Forward pruning
### 5.3.4 Search versus lookup
## 5.4 Monte Carlo Tree Search
## 5.5 Stochastic Games
### 5.5.1 Evaluation functions for games of chance
## 5.6 Partially Observable Games
### 5.6.1 Kriegspiel: Partially observable chess
### 5.6.2 Card games
## 5.7 Limitations of Game Search Algorithms


# 6 Constraint Satisfaction Problems
## 6.1 Defining Constraint Satisfaction Problems
### 6.1.1 Example problem: Map coloring
### 6.1.2 Example problem: Job-shop scheduling
### 6.1.3 Variations on the CSP formalism
## 6.2 Constraint Propagation: Inference in CSPs
### 6.2.1 Node consistency
### 6.2.2 Arc consistency
### 6.2.3 Path consistency
### 6.2.4 Kconsistency
### 6.2.5 Global constraints
### 6.2.6 Sudoku
## 6.3 Backtracking Search for CSPs
### 6.3.1 Variable and value ordering
### 6.3.2 Interleaving search and inference
### 6.3.3 Intelligent backtracking: Looking backward
### 6.3.4 Constraint learning
## 6.4 Local Search for CSPs
## 6.5 The Structure of Problems
### 6.5.1 Cutset conditioning
### 6.5.2 Tree decomposition
### 6.5.3 Value symmetry


# Part III: Knowledge, reasoning, and planning
# 7 Logical Agents
## 7.1 Knowledge-Based Agents
## 7.2 The Wumpus World
## 7.3 Logic
## 7.4 Propositional Logic: A Very Simple Logic
### 7.4.1 Syntax
### 7.4.2 Semantics
### 7.4.3 A simple knowledge base
### 7.4.4 A simple inference procedure
## 7.5 Propositional Theorem Proving
### 7.5.1 Inference and proofs
### 7.5.2 Proof by resolution
- Conjunctive normal form
- A resolution algorithm
- Completeness of resolution
### 7.5.3 Horn clauses and definite clauses
### 7.5.4 Forward and backward chaining
## 7.6 Effective Propositional Model Checking
### 7.6.1 A complete backtracking algorithm
### 7.6.2 Local search algorithms
### 7.6.3 The landscape of random SAT problems
## 7.7 Agents Based on Propositional Logic
### 7.7.1 The current state of the world
### 7.7.2 A hybrid agent
### 7.7.3 Logical state estimation
### 7.7.4 Making plans by propositional inference


# 8 First-Order Logic
## 8.1 Representation Revisited
### 8.1.1 The language of thought
### 8.1.2 Combining the best of formal and natural languages
## 8.2 Syntax and Semantics of First-Order Logic
### 8.2.1 Models for first-order logic
### 8.2.2 Symbols and interpretations
### 8.2.3 Terms
### 8.2.4 Atomic sentences
### 8.2.5 Complex sentences
### 8.2.6 Quantifiers
- Universal quantification (∀)
- Existential quantification (∃)
- Nested quantifiers
- Connections between ∀ and ∃
### 8.2.7 Equality
### 8.2.8 Database semantics
## 8.3 Using First-Order Logic
### 8.3.1 Assertions and queries in first-order logic
### 8.3.2 The kinship domain
### 8.3.3 Numbers, sets, and lists
### 8.3.4 The wumpus world
## 8.4 Knowledge Engineering in First-Order Logic
### 8.4.1 The knowledge engineering process
### 8.4.2 The electronic circuits domain
- Identify the questions
- Assemble the relevant knowledge
- Decide on a vocabulary
- Encode general knowledge of the domain
- Encode the specific problem instance
- Pose queries to the inference procedure
- Debug the knowledge base


# 9 Inference in First-Order Logic
## 9.1 Propositional vs. First-Order Inference
### 9.1.1 Reduction to propositional inference
## 9.2 Unification and First-Order Inference
### 9.2.1 Unification
### 9.2.2 Storage and retrieval
## 9.3 Forward Chaining
### 9.3.1 First-order definite clauses
### 9.3.2 A simple forward-chaining algorithm
### 9.3.3 Efficient forward chaining
- Matching rules against known facts
- Incremental forward chaining
- Irrelevant facts
## 9.4 Backward Chaining
### 9.4.1 A backward-chaining algorithm
### 9.4.2 Logic programming
### 9.4.3 Redundant inference and infinite loops
### 9.4.4 Database semantics of Prolog
### 9.4.5 Constraint logic programming
## 9.5 Resolution
### 9.5.1 Conjunctive normal form for first-order logic
### 9.5.2 The resolution inference rule
### 9.5.3 Example proofs
### 9.5.4 Completeness of resolution
### 9.5.5 Equality
### 9.5.6 Resolution strategies
- Practical uses of resolution theorem provers


# 10 Knowledge Representation
## 10.1 Ontological Engineering
## 10.2 Categories and Objects
### 10.2.1 Physical composition
### 10.2.2 Measurements
### 10.2.3 Objects: Things and stuff
## 10.3 Events
### 10.3.1 Time
### 10.3.2 Fluents and objects
## 10.4 Mental Objects and Modal Logic
### 10.4.1 Other modal logics
## 10.5 Reasoning Systems for Categories
### 10.5.1 Semantic networks
### 10.5.2 Description logics
## 10.6 Reasoning with Default Information
### 10.6.1 Circumscription and default logic
### 10.6.2 Truth maintenance systems


# 11 Automated Planning
## 11.1 Definition of Classical Planning
### 11.1.1 Example domain: Air cargo transport
### 11.1.2 Example domain: The spare tire problem
### 11.1.3 Example domain: The blocks world
## 11.2 Algorithms for Classical Planning
### 11.2.1 Forward state-space search for planning
### 11.2.2 Backward search for planning
### 11.2.3 Planning as Boolean satisfiability
### 11.2.4 Other classical planning approaches
## 11.3 Heuristics for Planning
### 11.3.1 Domain-independent pruning
### 11.3.2 State abstraction in planning
## 11.4 Hierarchical Planning
### 11.4.1 High-level actions
### 11.4.2 Searching for primitive solutions
### 11.4.3 Searching for abstract solutions
## 11.5 Planning and Acting in Nondeterministic Domains
### 11.5.1 Sensorless planning
### 11.5.2 Contingent planning
### 11.5.3 Online planning
## 11.6 Time, Schedules, and Resources
### 11.6.1 Representing temporal and resource constraints
### 11.6.2 Solving scheduling problems
## 11.7 Analysis of Planning Approaches


# Part IV: Uncertain knowledge and reasoning
# 12 Quantifying Uncertainty
## 12.1 Acting under Uncertainty
### 12.1.1 Summarizing uncertainty
### 12.1.2 Uncertainty and rational decisions
## 12.2 Basic Probability Notation
### 12.2.1 What probabilities are about
### 12.2.2 The language of propositions in probability assertions
### 12.2.3 Probability axioms and their reasonableness
## 12.3 Inference Using Full Joint Distributions
## 12.4 Independence
## 12.5 Bayes' Rule and Its Use
### 12.5.1 Applying Bayes' rule: The simple case
### 12.5.2 Using Bayes' rule: Combining evidence
## 12.6 Naive Bayes Models
### 12.6.1 Text classification with naive Bayes
## 12.7 The Wumpus World Revisited


# 13 Probabilistic Reasoning
## 13.1 Representing Knowledge in an Uncertain Domain
## 13.2 The Semantics of Bayesian Networks
- A method for constructing Bayesian networks
- Compactness and node ordering
### 13.2.1 Conditional independence relations in Bayesian networks
### 13.2.2 Efficient Representation of Conditional Distributions
### 13.2.3 Bayesian nets with continuous variables
### 13.2.4 Case study: Car insurance
## 13.3 Exact Inference in Bayesian Networks
### 13.3.1 Inference by enumeration
### 13.3.2 The variable elimination algorithm
- Operations on factors
- Variable ordering and variable relevance
### 13.3.3 The complexity of exact inference
### 13.3.4 Clustering algorithms
## 13.4 Approximate Inference for Bayesian Networks
### 13.4.1 Direct sampling methods
- Rejection sampling in Bayesian networks
- Importance sampling
### 13.4.2 Inference by Markov chain simulation
- Gibbs sampling in Bayesian networks
- Analysis of Markov chains
- Why Gibbs sampling works
- Complexity of Gibbs sampling
- Metropolis--Hastings sampling
### 13.4.3 Compiling approximate inference
## 13.5 Causal Networks
### 13.5.1 Representing actions: do-operator
### 13.5.2 The back-door criterion


# 14 Probabilistic Reasoning over Time
## 14.1 Time and Uncertainty
### 14.1.1 States and observations
### 14.1.2 Transition and sensor models
## 14.2 Inference in Temporal Models
### 14.2.1 Filtering and prediction
### 14.2.2 Smoothing
### 14.2.3 Finding the most likely sequence
## 14.3 Hidden Markov Models
### 14.3.1 Simplified matrix algorithms
### 14.3.2 Hidden Markov model example: Localization
## 14.4 Kalman Filters
### 14.4.1 Updating Gaussian distributions
### 14.4.2 A simple one-dimensional example
### 14.4.3 The general case
### 14.4.4 Applicability of Kalman filtering
## 14.5 Dynamic Bayesian Networks
### 14.5.1 Constructing DBNs
### 14.5.2 Exact inference in DBNs
### 14.5.3 Approximate inference in DBNs


# 15 Probabilistic Programming
## 15.1 Relational Probability Models
### 15.1.1 Syntax and semantics
### 15.1.2 Example: Rating player skill levels
### 15.1.3 Inference in relational probability models
## 15.2 Open-Universe Probability Models
### 15.2.1 Syntax and semantics
### 15.2.2 Inference in open-universe probability models
### 15.2.3 Examples
- Citation matching
- Nuclear treaty monitoring
## 15.3 Keeping Track of a Complex World
### 15.3.1 Example: Multitarget tracking
### 15.3.2 Example: Traffic monitoring
## 15.4 Programs as Probability Models
### 15.4.1 Example: Reading text
### 15.4.2 Syntax and semantics
### 15.4.3 Inference results
### 15.4.4 Improving the generative program to incorporate a Markov model
### 15.4.5 Inference in generative programs


# 16 Making Simple Decisions
## 16.1 Combining Beliefs and Desires under Uncertainty
## 16.2 The Basis of Utility Theory
### 16.2.1 Constraints on rational preferences
### 16.2.2 Rational preferences lead to utility
## 16.3 Utility Functions
### 16.3.1 Utility assessment and utility scales
### 16.3.2 The utility of money
### 16.3.3 Expected utility and post-decision disappointment
### 16.3.4 Human judgment and irrationality
## 16.4 Multiattribute Utility Functions
### 16.4.1 Dominance
### 16.4.2 Preference structure and multiattribute utility
- Preferences without uncertainty
- Preferences with uncertainty
## 16.5 Decision Networks
### 16.5.1 Representing a decision problem with a decision network
### 16.5.2 Evaluating decision networks
## 16.6 The Value of Information
### 16.6.1 A simple example
### 16.6.2 A general formula for perfect information
### 16.6.3 Properties of the value of information
### 16.6.4 Implementation of an information-gathering agent
### 16.6.5 Nonmyopic information gathering
### 16.6.6 Sensitivity analysis and robust decisions
## 16.7 Unknown Preferences
### 16.7.1 Uncertainty about one's own preferences
### 16.7.2 Deference to humans


# 17 Making Complex Decisions
## 17.1 Sequential Decision Problems
### 17.1.1 Utilities over time
### 17.1.2 Optimal policies and the utilities of states
### 17.1.3 Reward scales
### 17.1.4 Representing MDPs
## 17.2 Algorithms for MDPs
### 17.2.1 Value Iteration
- Convergence of value iteration
### 17.2.2 Policy iteration
### 17.2.3 Linear programming
### 17.2.4 Online algorithms for MDPs
## 17.3 Bandit Problems
### 17.3.1 Calculating the Gittins index
### 17.3.2 The Bernoulli bandit
### 17.3.3 Approximately optimal bandit policies
### 17.3.4 Non-indexable variants
## 17.4 Partially Observable MDPs
### 17.4.1 Definition of POMDPs
## 17.5 Algorithms for Solving POMDPs
### 17.5.1 Value iteration for POMDPs
### 17.5.2 Online algorithms for POMDPs


# 18 Multiagent Decision Making
## 18.1 Properties of Multiagent Environments
### 18.1.1 One decision maker
### 18.1.2 Multiple decision makers
### 18.1.3 Multiagent planning
### 18.1.4 Planning with multiple agents: Cooperation and coordination
## 18.2 Non-Cooperative Game Theory
### 18.2.1 Games with a single move: Normal form games
### 18.2.2 Social welfare
- Computing equilibria
### 18.2.3 Repeated games
### 18.2.4 Sequential games: The extensive form
- Chance and simultaneous moves
- Capturing imperfect information
### 18.2.5 Uncertain payoffs and assistance games
## 18.3 Cooperative Game Theory
### 18.3.1 Coalition structures and outcomes
### 18.3.2 Strategy in cooperative games
### 18.3.3 Computation in cooperative games
- Marginal contribution nets
- Coalition structures for maximum social welfare
## 18.4 Making Collective Decisions
### 18.4.1 Allocating tasks with the contract net
### 18.4.2 Allocating scarce resources with auctions
- Common goods
### 18.4.3 Voting
- Strategic manipulation
### 18.4.4 Bargaining
- Bargaining with the alternating offers protocol
- Impatient agents
- Negotiation in task-oriented domains
- The monotonic concession protocol
- The Zeuthen strategy


# Part V: Machine Learning
# 19 Learning from Examples
## 19.1 Forms of Learning
## 19.2 Supervised Learning
### 19.2.1 Example problem: Restaurant waiting
## 19.3 Learning Decision Trees
### 19.3.1 Expressiveness of decision trees
### 19.3.2 Learning decision trees from examples
### 19.3.3 Choosing attribute tests
### 19.3.4 Generalization and overfitting
### 19.3.5 Broadening the applicability of decision trees
## 19.4 Model Selection and Optimization
### 19.4.1 Model selection
### 19.4.2 From error rates to loss
### 19.4.3 Regularization
### 19.4.4 Hyperparameter tuning
## 19.5 The Theory of Learning
### 19.5.1 PAC learning example: Learning decision lists
## 19.6 Linear Regression and Classification
### 19.6.1 Univariate linear regression
### 19.6.2 Gradient descent
### 19.6.3 Multivariable linear regression
### 19.6.4 Linear classifiers with a hard threshold
### 19.6.5 Linear classification with logistic regression
## 19.7 Nonparametric Models
### 19.7.1 Nearest-neighbor models
### 19.7.2 Finding nearest neighbors with k-d trees
### 19.7.3 Locality-sensitive hashing
### 19.7.4 Nonparametric regression
### 19.7.5 Support vector machines
### 19.7.6 The kernel trick
## 19.8 Ensemble Learning
### 19.8.1 Bagging
### 19.8.2 Random forests
### 19.8.3 Stacking
### 19.8.4 Boosting
### 19.8.5 Gradient boosting
### 19.8.6 Online learning
## 19.9 Developing Machine Learning Systems
### 19.9.1 Problem formulation
### 19.9.2 Data collection, assessment, and management
- Feature engineering
- Exploratory data analysis and visualization
### 19.9.3 Model selection and training
### 19.9.4 Trust, interpretability, and explainability
### 19.9.5 Operation, monitoring, and maintenance


# 20 Learning Probabilistic Models
## 20.1 Statistical Learning
## 20.2 Learning with Complete Data
### 20.2.1 Maximum-likelihood parameter learning: Discrete models
### 20.2.2 Naive Bayes models
### 20.2.3 Generative and discriminative models
### 20.2.4 Maximum-likelihood parameter learning: Continuous models
### 20.2.5 Bayesian parameter learning
### 20.2.6 Bayesian linear regression
### 20.2.7 Learning Bayes net structures
### 20.2.8 Density estimation with nonparametric models
## 20.3 Learning with Hidden Variables: The EM Algorithm
### 20.3.1 Unsupervised clustering: Learning mixtures of Gaussians
### 20.3.2 Learning Bayes net parameter values for hidden variables
### 20.3.3 Learning hidden Markov models
### 20.3.4 The general form of the EM algorithm
### 20.3.5 Learning Bayes net structures with hidden variables


# 21 Deep Learning
## 21.1 Simple Feedforward Networks
### 21.1.1 Networks as complex functions
### 21.1.2 Gradients and learning
## 21.2 Computation Graphs for Deep Learning
### 21.2.1 Input encoding
### 21.2.2 Output layers and loss functions
### 21.2.3 Hidden layers
## 21.3 Convolutional Networks
### 21.3.1 Pooling and downsampling
### 21.3.2 Tensor operations in CNNs
### 21.3.3 Residual networks
## 21.4 Learning Algorithms
### 21.4.1 Computing gradients in computation graphs
### 21.4.2 Batch normalization
## 21.5 Generalization
### 21.5.1 Choosing a network architecture
### 21.5.2 Neural architecture search
### 21.5.3 Weight decay
### 21.5.4 Dropout
## 21.6 Recurrent Neural Networks
### 21.6.1 Training a basic RNN
### 21.6.2 Long short-term memory RNNs
## 21.7 Unsupervised Learning and Transfer Learning
### 21.7.1 Unsupervised learning
- Probabilistic PCA: A simple generative model
- Autoencoders
- Deep autoregressive models
- Generative adversarial networks
- Unsupervised translation
### 21.7.2 Transfer learning and multitask learning
## 21.8 Applications
### 21.8.1 Vision
### 21.8.2 Natural language processing
### 21.8.3 Reinforcement learning


# 22 Reinforcement Learning
## 22.1 Learning from Rewards
## 22.2 Passive Reinforcement Learning
### 22.2.1 Direct utility estimation
### 22.2.2 Adaptive dynamic programming
### 22.2.3 Temporal-difference learning
## 22.3 Active Reinforcement Learning
### 22.3.1 Exploration
### 22.3.2 Safe exploration
### 22.3.3 Temporal-difference Q-learning
## 22.4 Generalization in Reinforcement Learning
### 22.4.1 Approximating direct utility estimation
### 22.4.2 Approximating temporal-difference learning
### 22.4.3 Deep reinforcement learning
### 22.4.4 Reward shaping
### 22.4.5 Hierarchical reinforcement learning
## 22.5 Policy Search
## 22.6 Apprenticeship and Inverse Reinforcement Learning
## 22.7 Applications of Reinforcement Learning
### 22.7.1 Applications in game playing
### 22.7.2 Application to robot control


# Part VI: Communicating, perceiving, and acting
# 23 Natural Language Processing
## 23.1 Language Models
### 23.1.1 The bag-of-words model
### 23.1.2 N-gram word models
### 23.1.3 Other n-gram models
### 23.1.4 Smoothing n-gram models
### 23.1.5 Word representations
### 23.1.6 Part-of-speech (POS) tagging
### 23.1.7 Comparing language models
## 23.2 Grammar
### 23.2.1 The lexicon of E0
## 23.3 Parsing
### 23.3.1 Dependency parsing
### 23.3.2 Learning a parser from examples
## 23.4 Augmented Grammars
### 23.4.1 Semantic interpretation
### 23.4.2 Learning semantic grammars
## 23.5 Complications of Real Natural Language
## 23.6 Natural Language Tasks


# 24 Deep Learning for Natural Language Processing
## 24.1 Word Embeddings
## 24.2 Recurrent Neural Networks for NLP
### 24.2.1 Language models with recurrent neural networks
### 24.2.2 Classification with recurrent neural networks
### 24.2.3 LSTMs for NLP tasks
## 24.3 Sequence-to-Sequence Models
### 24.3.1 Attention
### 24.3.2 Decoding
## 24.4 The Transformer Architecture
### 24.4.1 Self-attention
### 24.4.2 From self-attention to transformer
## 24.5 Pretraining and Transfer Learning
### 24.5.1 Pretrained word embeddings
### 24.5.2 Pretrained contextual representations
### 24.5.3 Masked language models
## 24.6 State of the art


# 25 Computer Vision
## 25.1 Introduction
## 25.2 Image Formation
### 25.2.1 Images without lenses: The pinhole camera
### 25.2.2 Lens systems
### 25.2.3 Scaled orthographic projection
### 25.2.4 Light and shading
### 25.2.5 Color
## 25.3 Simple Image Features
### 25.3.1 Edges
### 25.3.2 Texture
### 25.3.3 Optical flow
### 25.3.4 Segmentation of natural images
## 25.4 Classifying Images
### 25.4.1 Image classification with convolutional neural networks
### 25.4.2 Why convolutional neural networks classify images well
## 25.5 Detecting Objects
## 25.6 The 3D World
### 25.6.1 3D cues from multiple views
### 25.6.2 Binocular stereopsis
### 25.6.3 3D cues from a moving camera
### 25.6.4 3D cues from one view
## 25.7 Using Computer Vision
### 25.7.1 Understanding what people are doing
### 25.7.2 Linking pictures and words
### 25.7.3 Reconstruction from many views
### 25.7.4 Geometry from a single view
### 25.7.5 Making pictures
### 25.7.6 Controlling movement with vision


# 26 Robotics
## 26.1 Robots
## 26.2 Robot Hardware
### 26.2.1 Types of robots from the hardware perspective
### 26.2.2 Sensing the world
### 26.2.3 Producing motion
## 26.3 What kind of problem is robotics solving?
## 26.4 Robotic Perception
### 26.4.1 Localization and mapping
### 26.4.2 Other types of perception
### 26.4.3 Supervised and unsupervised learning in robot perception
## 26.5 Planning and Control
### 26.5.1 Configuration space
### 26.5.2 Motion planning
- Visibility graphs
- Voronoi diagrams
- Cell decomposition
- Randomized motion planning
- Rapidly-exploring random trees
- Trajectory optimization for kinematic planning
### 26.5.3 Trajectory tracking control
- Plans versus policies
### 26.5.4 Optimal control
## 26.6 Planning Uncertain Movements
## 26.7 Reinforcement Learning in Robotics
### 26.7.1 Exploiting models
### 26.7.2 Exploiting other information
## 26.8 Humans and Robots
### 26.8.1 Coordination
- Humans as approximately rational agents
- Predicting human action
- Human predictions about the robot
- Humans as black box agents
### 26.8.2 Learning to do what humans want
- Preference learning: Learning cost functions
- Learning policies directly via imitation
## 26.9 Alternative Robotic Frameworks
### 26.9.1 Reactive controllers
### 26.9.2 Subsumption architectures
## 26.10 Application Domains


# Part VII: Conclusions
# 27 Philosophy, Ethics, and Safety of AI
## 27.1 The Limits of AI
### 27.1.1 The argument from informality
### 27.1.2 The argument from disability
### 27.1.3 The mathematical objection
### 27.1.4 Measuring AI
## 27.2 Can Machines Really Think?
### 27.2.1 The Chinese room
### 27.2.2 Consciousness and qualia
## 27.3 The Ethics of AI
### 27.3.1 Lethal autonomous weapons
### 27.3.2 Surveillance, security, and privacy
### 27.3.3 Fairness and bias
### 27.3.4 Trust and transparency
### 27.3.5 The future of work
### 27.3.6 Robot rights
### 27.3.7 AI Safety


# 28 The Future of AI
## 28.1 AI Components
- Sensors and actuators
- Representing the state of the world
- Selecting actions
- Deciding what we want
- Learning
- Resources
## 28.2 AI Architectures
- General AI
- AI engineering
- The future

# Appendix A: Mathematical Background
## A.1 Complexity Analysis and O() Notation
### A.1.1 Asymptotic analysis
### A.1.2 NP and inherently hard problems
## A.2 Vectors, Matrices, and Linear Algebra
## A.3 Probability Distributions

# Appendix B: Notes on Languages and Algorithms
## B.1 Defining Languages with Backus--Naur Form (BNF)
## B.2 Describing Algorithms with Pseudocode
## B.3 Online Supplemental Material