# Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow

- I. The Fundamentals of Machine Learning: 1-9
- II. Neural Networks and Deep Learning: 10-19

# 1. The Machine Learning Landscape/机器学习概览
- What Is Machine Learning?
- Why Use Machine Learning?
- Examples of Applications
- Types of Machine Learning Systems
  - Training Supervision
  - Batch Versus Online Learning
  - Instance-Based Versus Model-Based Learning
- Main Challenges of Machine Learning
  - Insufficient Quantity of Training Data
  - Nonrepresentative Training Data
  - Poor-Quality Data
  - Irrelevant Features
  - Overfitting the Training Data
  - Underfitting the Training Data
  - Stepping Back
- Testing and Validating
  - Hyperparameter Tuning and Model Selection
  - Data Mismatch

# 2. End-to-End Machine Learning Project/端到端机器学习项目
- Working with Real Data
- Look at the Big Picture
  - Frame the Problem
  - Select a Performance Measure
  - Check the Assumptions
- Get the Data
  - Running the Code Examples Using Google Colab
  - Saving Your Code Changes and Your Data
  - The Power and Danger of Interactivity
  - Book Code Versus Notebook Code
  - Download the Data
  - Take a Quick Look at the Data Structure
  - Create a Test Set
- Explore and Visualize the Data to Gain Insights
  - Visualizing Geographical Data
  - Look for Correlations
  - Experiment with Attribute Combinations
- Prepare the Data for Machine Learning Algorithms
  - Clean the Data
  - Handling Text and Categorical Attributes
  - Feature Scaling and Transformation
  - Custom Transformers
  - Transformation Pipelines
- Select and Train a Model
  - Train and Evaluate on the Training Set
  - Better Evaluation Using Cross-Validation
- Fine-Tune Your Model
  - Grid Search
  - Randomized Search
  - Ensemble Methods
  - Analyzing the Best Models and Their Errors
  - Evaluate Your System on the Test Set
- Launch, Monitor, and Maintain Your System
- Try It Out!

# 3. Classification/分类
- MNIST
- Training a Binary Classifier
- Performance Measures
  - Measuring Accuracy Using Cross-Validation
  - Confusion Matrices
  - Precision and Recall
  - The Precision/Recall Trade-off
  - The ROC Curve
- Multiclass Classification
- Error Analysis
- Multilabel Classification
- Multioutput Classification

# 4. Training Models/训练模型
- Linear Regression
  - The Normal Equation
  - Computational Complexity
- Gradient Descent
  - Batch Gradient Descent
  - Stochastic Gradient Descent
  - Mini-Batch Gradient Descent
- Polynomial Regression
- Learning Curves
- Regularized Linear Models
  - Ridge Regression
  - Lasso Regression
  - Elastic Net Regression
  - Early Stopping
- Logistic Regression
  - Estimating Probabilities
  - Training and Cost Function
  - Decision Boundaries
  - Softmax Regression

# 5. Support Vector Machines/支持向量机
- Linear SVM Classification
  - Soft Margin Classification
- Nonlinear SVM Classification
  - Polynomial Kernel
  - Similarity Features
  - Gaussian RBF Kernel
  - SVM Classes and Computational Complexity
- SVM Regression
- Under the Hood of Linear SVM Classifiers
- The Dual Problem
  - Kernelized SVMs

# 6. Decision Trees/决策树
- Training and Visualizing a Decision Tree
- Making Predictions
- Estimating Class Probabilities
- The CART Training Algorithm
- Computational Complexity
- Gini Impurity or Entropy?
- Regularization Hyperparameters
- Regression
- Sensitivity to Axis Orientation
- Decision Trees Have a High Variance

# 7. Ensemble Learning and Random Forests/集成学习与随机森林
- Voting Classifiers
- Bagging and Pasting
  - Bagging and Pasting in Scikit-Learn
  - Out-of-Bag Evaluation
  - Random Patches and Random Subspaces
- Random Forests
  - Extra-Trees
  - Feature Importance
- Boosting
  - AdaBoost
  - Gradient Boosting
  - Histogram-Based Gradient Boosting
- Stacking

# 8. Dimensionality Reduction/降维
- The Curse of Dimensionality
- Main Approaches for Dimensionality Reduction
  - Projection
  - Manifold Learning
- PCA
  - Preserving the Variance
  - Principal Components
  - Projecting Down to d Dimensions
  - Using Scikit-Learn
  - Explained Variance Ratio
  - Choosing the Right Number of Dimensions
  - PCA for Compression
  - Randomized PCA
  - Incremental PCA
- Random Projection
- LLE
- Other Dimensionality Reduction Techniques

# 9. Unsupervised Learning Techniques/无监督学习技术
- Clustering Algorithms: k-means and DBSCAN
  - k-means
  - Limits of k-means
  - Using Clustering for Image Segmentation
  - Using Clustering for Semi-Supervised Learning
  - DBSCAN
  - Other Clustering Algorithms
- Gaussian Mixtures
  - Using Gaussian Mixtures for Anomaly Detection
  - Selecting the Number of Clusters
  - Bayesian Gaussian Mixture Models
  - Other Algorithms for Anomaly and Novelty Detection

# 10. Introduction to Artificial Neural Networks with Keras/Keras人工神经网络介绍
- From Biological to Artificial Neurons
  - Biological Neurons
  - Logical Computations with Neurons
  - The Perceptron
  - The Multilayer Perceptron and Backpropagation
  - Regression MLPs
  - Classification MLPs
- Implementing MLPs with Keras
  - Building an Image Classifier Using the Sequential API
  - Building a Regression MLP Using the Sequential API
  - Building Complex Models Using the Functional API
  - Using the Subclassing API to Build Dynamic Models
  - Saving and Restoring a Model
  - Using Callbacks
  - Using TensorBoard for Visualization
- Fine-Tuning Neural Network Hyperparameters
  - Number of Hidden Layers
  - Number of Neurons per Hidden Layer
  - Learning Rate, Batch Size, and Other Hyperparameters

# 11. Training Deep Neural Networks/训练深度神经网络
- The Vanishing/Exploding Gradients Problems
  - Glorot and He Initialization
  - Better Activation Functions
  - Batch Normalization
  - Gradient Clipping
- Reusing Pretrained Layers
  - Transfer Learning with Keras
  - Unsupervised Pretraining
  - Pretraining on an Auxiliary Task
- Faster Optimizers
  - Momentum
  - Nesterov Accelerated Gradient
  - AdaGrad
  - RMSProp
  - Adam
  - AdaMax
  - Nadam
  - AdamW
- Learning Rate Scheduling
- Avoiding Overfitting Through Regularization
  - ℓ1 and ℓ2 Regularization
  - Dropout
  - Monte Carlo (MC) Dropout
  - Max-Norm Regularization
- Summary and Practical Guidelines

# 12. Custom Models and Training with TensorFlow/使用TensorFlow自定义模型与训练
- A Quick Tour of TensorFlow
- Using TensorFlow like NumPy
  - Tensors and Operations
  - Tensors and NumPy
  - Type Conversions
  - Variables
  - Other Data Structures
- Customizing Models and Training Algorithms
  - Custom Loss Functions
  - Saving and Loading Models That Contain Custom Components
  - Custom Activation Functions, Initializers, Regularizers, 
  - and Constraints
  - Custom Metrics
  - Custom Layers
  - Custom Models
  - Losses and Metrics Based on Model Internals
  - Computing Gradients Using Autodiff
  - Custom Training Loops
- TensorFlow Functions and Graphs
  - AutoGraph and Tracing
  - TF Function Rules

# 13. Loading and Preprocessing Data with TensorFlow/使用TensorFlow加载与预处理数据
- The `tf.data` API
  - Chaining Transformations
  - Shuffling the Data
  - Interleaving Lines from Multiple Files
  - Preprocessing the Data
  - Putting Everything Together
  - Prefetching
  - Using the Dataset with Keras
- The `TFRecord` Format
  - Compressed TFRecord Files
  - A Brief Introduction to Protocol Buffers
  - TensorFlow Protobufs
  - Loading and Parsing Examples
  - Handling Lists of Lists Using the SequenceExample Protobuf
- Keras Preprocessing Layers
  - The Normalization Layer
  - The Discretization Layer
  - The CategoryEncoding Layer
  - The StringLookup Layer
  - The Hashing Layer
  - Encoding Categorical Features Using Embeddings
  - Text Preprocessing
  - Using Pretrained Language Model Components
  - Image Preprocessing Layers
- The TensorFlow Datasets Project

# 14. Deep Computer Vision Using Convolutional Neural Networks/基于卷积神经网络的深度计算机视觉
- The Architecture of the Visual Cortex
- Convolutional Layers
  - Filters
  - Stacking Multiple Feature Maps
  - Implementing Convolutional Layers with Keras
  - Memory Requirements
- Pooling Layers
- Implementing Pooling Layers with Keras
- CNN Architectures
  - LeNet-5
  - AlexNet
  - GoogLeNet
  - VGGNet
  - ResNet
  - Xception
  - SENet
  - Other Noteworthy Architectures
  - Choosing the Right CNN Architecture
- Implementing a ResNet-34 CNN Using Keras
- Using Pretrained Models from Keras
- Pretrained Models for Transfer Learning
- Classification and Localization
- Object Detection
  - Fully Convolutional Networks
  - You Only Look Once
- Object Tracking
- Semantic Segmentation

# 15. Processing Sequences Using RNNs and CNNs/使用RNN和CNN处理序列
- Recurrent Neurons and Layers
  - Memory Cells
  - Input and Output Sequences
- Training RNNs
- Forecasting a Time Series
  - The ARMA Model Family
  - Preparing the Data for Machine Learning Models
  - Forecasting Using a Linear Model
  - Forecasting Using a Simple RNN
  - Forecasting Using a Deep RNN
  - Forecasting Multivariate Time Series
  - Forecasting Several Time Steps Ahead
  - Forecasting Using a Sequence-to-Sequence Model
- Handling Long Sequences
  - Fighting the Unstable Gradients Problem
  - Tackling the Short-Term Memory Problem

# 16. Natural Language Processing with RNNs and Attention/基于RNN和注意力机制的自然语言处理
- Generating Shakespearean Text Using a Character RNN
  - Creating the Training Dataset
  - Building and Training the Char-RNN Model
  - Generating Fake Shakespearean Text
  - Stateful RNN
- Sentiment Analysis
  - Masking
  - Reusing Pretrained Embeddings and Language Models
- An Encoder–Decoder Network for Neural Machine Translation
  - Bidirectional RNNs
  - Beam Search
- Attention Mechanisms
  - Attention Is All You Need: The Original Transformer Architecture
- An Avalanche of Transformer Models
- Vision Transformers
- Hugging Face’s Transformers Library

# 17. Autoencoders, GANs, and Diffusion Models/自动编码器, GAN与扩散模型
- Efficient Data Representations
- Performing PCA with an Undercomplete Linear Autoencoder
- Stacked Autoencoders
  - Implementing a Stacked Autoencoder Using Keras
  - Visualizing the Reconstructions
  - Visualizing the Fashion MNIST Dataset
  - Unsupervised Pretraining Using Stacked Autoencoders
  - Tying Weights
  - Training One Autoencoder at a Time
- Convolutional Autoencoders
- Denoising Autoencoders
- Sparse Autoencoders
- Variational Autoencoders
- Generating Fashion MNIST Images
- Generative Adversarial Networks
  - The Difficulties of Training GANs
  - Deep Convolutional GANs
  - Progressive Growing of GANs
  - StyleGANs
- Diffusion Models

# 18. Reinforcement Learning/强化学习
- Learning to Optimize Rewards
- Policy Search
- Introduction to OpenAI Gym
- Neural Network Policies
- Evaluating Actions: The Credit Assignment Problem
- Policy Gradients
- Markov Decision Processes
- Temporal Difference Learning
- Q-Learning
  - Exploration Policies
  - Approximate Q-Learning and Deep Q-Learning
- Implementing Deep Q-Learning
- Deep Q-Learning Variants
  - Fixed Q-value Targets
  - Double DQN
  - Prioritized Experience Replay
  - Dueling DQN
- Overview of Some Popular RL Algorithms

# 19. Training and Deploying TensorFlow Models at Scale/大规模训练与部署TensorFlow模型
- Serving a TensorFlow Model
  - Using TensorFlow Serving
  - Creating a Prediction Service on Vertex AI
  - Running Batch Prediction Jobs on Vertex AI
- Deploying a Model to a Mobile or Embedded Device
- Running a Model in a Web Page
- Using GPUs to Speed Up Computations
  - Getting Your Own GPU
  - Managing the GPU RAM
  - Placing Operations and Variables on Devices
  - Parallel Execution Across Multiple Devices
- Training Models Across Multiple Devices
  - Model Parallelism
  - Data Parallelism
  - Training at Scale Using the Distribution Strategies API
  - Training a Model on a TensorFlow Cluster
  - Running Large Training Jobs on Vertex AI
  - Hyperparameter Tuning on Vertex AI

# A. Machine Learning Project Checklist/机器学习项目清单
- Frame the Problem and Look at the Big Picture
- Get the Data
- Explore the Data
- Prepare the Data
- Shortlist Promising Models
- Fine-Tune the System
- Present Your Solution
- Launch!

# B. Autodiff/自动微分
- Manual Differentiation/手动微分
- Finite Difference Approximation/有限差分近似
- Forward-Mode Autodiff/前向模式自动微分
- Reverse-Mode Autodiff/反向模式自动微分

# C. Special Data Structures
- Strings
- Ragged Tensors
- Sparse Tensors
- Tensor Arrays
- Sets
- Queues

# D. TensorFlow Graphs
- TF Functions and Concrete Functions
- Exploring Function Definitions and Graphs
- A Closer Look at Tracing
- Using AutoGraph to Capture Control Flow
- Handling Variables and Other Resources in TF Functions
- Using TF Functions with Keras (or Not)


# See Also

code
- https://github.com/ageron/handson-ml3

tools
- NumPy, Pandas, Matplotlib
- Scikit-Learn
- TensorFlow
- Keras
