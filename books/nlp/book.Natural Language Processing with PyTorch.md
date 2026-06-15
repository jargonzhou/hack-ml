# Natural Language Processing with PyTorch: Build Intelligent Language Applications Using Deep Learning

supervised learning paradigm.

consistent Python class-based modeling.

# 1. Introduction
- The Supervised Learning Paradigm
- Observation and Target Encoding
  - One-Hot Representation
  - TF Representation
  - TF-IDF Representation
  - Target Encoding
- Computational Graphs
- PyTorch Basics
  - Installing PyTorch
  - Creating Tensors
  - Tensor Types and Size
  - Tensor Operations
  - Indexing, Slicing, and Joining
  - Tensors and Computational Graphs
  - CUDA Tensors
- Exercises
- Solutions


# 2. A Quick Tour of Traditional NLP
- Corpora, Tokens, and Types
- Unigrams, Bigrams, Trigrams, …, N-grams
- Lemmas and Stems
- Categorizing Sentences and Documents
- Categorizing Words: POS Tagging
- Categorizing Spans: Chunking and Named Entity Recognition
- Structure of Sentences
- Word Senses and Semantics


# 3. Foundational Components of Neural Networks
- The Perceptron: The Simplest Neural Network
- Activation Functions
  - Sigmoid
  - Tanh
  - ReLU
  - Softmax
- Loss Functions
  - Mean Squared Error Loss
  - Categorical Cross-Entropy Loss
  - Binary Cross-Entropy Loss
- Diving Deep into Supervised Training
  - Constructing Toy Data
  - Putting It Together: Gradient-Based Supervised Learning
- Auxiliary Training Concepts
  - Correctly Measuring Model Performance: Evaluation Metrics
  - Correctly Measuring Model Performance: Splitting the Dataset
  - Knowing When to Stop Training
  - Finding the Right Hyperparameters
  - Regularization
- Example: Classifying Sentiment of Restaurant Reviews
  - The Yelp Review Dataset
  - Understanding PyTorch’s Dataset Representation
  - The Vocabulary, the Vectorizer, and the DataLoader
  - A Perceptron Classifier
  - The Training Routine
  - Evaluation, Inference, and Inspection


# 4. Feed-Forward Networks for Natural Language Processing
- The Multilayer Perceptron
  - A Simple Example: XOR
  - Implementing MLPs in PyTorch
- Example: Surname Classification with an MLP
  - The Surnames Dataset
  - Vocabulary, Vectorizer, and DataLoader
  - The SurnameClassifier Model
  - The Training Routine
  - Model Evaluation and Prediction
  - Regularizing MLPs: Weight Regularization and Structural Regularization (or Dropout)
- Convolutional Neural Networks
  - CNN Hyperparameters
  - Implementing CNNs in PyTorch
- Example: Classifying Surnames by Using a CNN
  - The SurnameDataset Class
  - Vocabulary, Vectorizer, and DataLoader
  - Reimplementing the SurnameClassifier with Convolutional Networks
  - The Training Routine
  - Model Evaluation and Prediction
- Miscellaneous Topics in CNNs
  - Pooling
  - Batch Normalization (BatchNorm)
  - Network-in-Network Connections (1x1 Convolutions)
  - Residual Connections/Residual Block


# 5. Embedding Words and Types
- Why Learn Embeddings?
  - Efficiency of Embeddings
  - Approaches to Learning Word Embeddings
  - The Practical Use of Pretrained Word Embeddings
- Example: Learning the Continuous Bag of Words Embeddings
  - The Frankenstein Dataset
  - Vocabulary, Vectorizer, and DataLoader
  - The CBOWClassifier Model
  - The Training Routine
  - Model Evaluation and Prediction
- Example: Transfer Learning Using Pretrained Embeddings for Document Classification
  - The AG News Dataset
  - Vocabulary, Vectorizer, and DataLoader
  - The NewsClassifier Model
  - The Training Routine
  - Model Evaluation and Prediction
  - Evaluating on the test dataset


# 6. Sequence Modeling for Natural Language Processing
- Introduction to Recurrent Neural Networks
  - Implementing an Elman RNN
- Example: Classifying Surname Nationality Using a Character RNN
  - The SurnameDataset Class
  - The Vectorization Data Structures
  - The SurnameClassifier Model
  - The Training Routine and Results


# 7. Intermediate Sequence Modeling for Natural Language Processing
- The Problem with Vanilla RNNs (or Elman RNNs)
- Gating as a Solution to a Vanilla RNN’s Challenges
- Example: A Character RNN for Generating Surnames
  - The SurnameDataset Class
  - The Vectorization Data Structures
  - From the ElmanRNN to the GRU
  - Model 1: The Unconditioned SurnameGenerationModel
  - Model 2: The Conditioned SurnameGenerationModel
  - The Training Routine and Results
- Tips and Tricks for Training Sequence Models

# 8. Advanced Sequence Modeling for Natural Language Processing
- Sequence-to-Sequence Models, Encoder–Decoder Models, and Conditioned Generation
- Capturing More from a Sequence: Bidirectional Recurrent Models
- Capturing More from a Sequence: Attention
  - Attention in Deep Neural Networks
- Evaluating Sequence Generation Models
- Example: Neural Machine Translation
  - The Machine Translation Dataset
  - A Vectorization Pipeline for NMT
  - Encoding and Decoding in the NMT Model
  - The Training Routine and Results


# 9. Classics, Frontiers, and Next Steps
- What Have We Learned so Far?
- Timeless Topics in NLP
  - Dialogue and Interactive Systems
  - Discourse
  - Information Extraction and Text Mining
  - Document Analysis and Retrieval
- Frontiers in NLP
- Design Patterns for Production NLP Systems
- Where Next?

# See Also
* [Natural Language Processing with Transformers: Building Language Applications with Hugging Face](../nlp/book.Natural%20Language%20Processing%20with%20Transformers.md)