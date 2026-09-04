# Deep Learning with Python


# 1 What is deep learning?
- Artificial intelligence, machine learning, and deep learning
    - Artificial intelligence
	- Machine learning
	- Learning rules and representations from data
	- The “deep” in “deep learning”
	- Understanding how deep learning works, in three figures
	- What deep learning has achieved so far
	- Don't believe the short-term hype
	- The promise of AI
- Before deep learning: A brief history of machine learning
	- Probabilistic modeling
	- Early neural networks
	- Kernel methods
	- Decision trees, random forests, and gradient boosting machines
	- Back to neural networks
	- What makes deep learning different
	- The modern machine learning landscape
- Why deep learning? Why now?
	- Hardware
	- Data
	- Algorithms
	- A new wave of investment
	- The democratization of deep learning
	- Will it last?

# 2 The mathematical building blocks of neural networks
- A first look at a neural network
- Data representations for neural networks
	- Scalars (rank-0 tensors)
	- Vectors (rank-1 tensors)
	- Matrices (rank-2 tensors)
	- Rank-3 and higher-rank tensors
	- Key attributes
	- Manipulating tensors in NumPy
	- The notion of data batches
	- Real-world examples of data tensors
	- Vector data
	- Timeseries data or sequence data
	- Image data
	- Video data
- The gears of neural networks: Tensor operations
	- Element-wise operations
	- Broadcasting
	- Tensor product
	- Tensor reshaping
	- Geometric interpretation of tensor operations
	- A geometric interpretation of deep learning
- The engine of neural networks: Gradient-based optimization
	- What's a derivative?
	- Derivative of a tensor operation: The gradient
	- Stochastic gradient descent
	- Chaining derivatives: The Backpropagation algorithm
- Looking back at our first example
	- Reimplementing our first example from scratch in TensorFlow
	- Running one training step
	- The full training loop
	- Evaluating the model


# 3 Introduction to Keras and TensorFlow
- What's TensorFlow?
- What's Keras?
- Keras and TensorFlow: A brief history
- Setting up a deep learning workspace
	- Jupyter notebooks: The preferred way to run deep learning experiments
	- Using Colaboratory
- First steps with TensorFlow
	- Constant tensors and variables
	- Tensor operations: Doing math in TensorFlow
	- A second look at the GradientTape API
	- An end-to-end example: A linear classifier in pure TensorFlow
- Anatomy of a neural network: Understanding core Keras APIs
	- Layers: The building blocks of deep learning
	- From layers to models
	- The “compile” step: Configuring the learning process
	- Picking a loss function
	- Understanding the fit() method
	- Monitoring loss and metrics on validation data
	- Inference: Using a model after training


# 4 Getting started with neural networks: Classification and regression
- Classifying movie reviews: A binary classification example
	- The IMDB dataset
	- Preparing the data
	- Building your model
	- Validating your approach
	- Using a trained model to generate predictions on new data
	- Further experiments
	- Wrapping up
- Classifying newswires: A multiclass classification example
	- The Reuters dataset
	- Preparing the data
	- Building your model
	- Validating your approach
	- Generating predictions on new data
	- A different way to handle the labels and the loss
	- The importance of having sufficiently large intermediate layers
	- Further experiments
	- Wrapping up
- Predicting house prices: A regression example
	- The Boston housing price dataset
	- Preparing the data
	- Building your model
	- Validating your approach using K-fold validation
	- Generating predictions on new data
	- Wrapping up


# 5 Fundamentals of machine learning
- Generalization: The goal of machine learning
	- Underfitting and overfitting
	- The nature of generalization in deep learning
- Evaluating machine learning models
	- Training, validation, and test sets
	- Beating a common-sense baseline
	- Things to keep in mind about model evaluation
- Improving model fit
	- Tuning key gradient descent parameters
	- Leveraging better architecture priors
	- Increasing model capacity
- Improving generalization
	- Dataset curation
	- Feature engineering
	- Using early stopping
	- Regularizing your model


# 6 The universal workflow of machine learning
- Define the task
	- Frame the problem
	- Collect a dataset
	- Understand your data
	- Choose a measure of success
- Develop a model
	- Prepare the data
	- Choose an evaluation protocol
	- Beat a baseline
	- Scale up: Develop a model that overfits
	- Regularize and tune your model
- Deploy the model
	- Explain your work to stakeholders and set expectations
	- Ship an inference model
	- Monitor your model in the wild
	- Maintain your model


# 7 Working with Keras: A deep dive
- A spectrum of workflows
- Different ways to build Keras models
	- The Sequential model
	- The Functional API
	- Subclassing the Model class
	- Mixing and matching different components
	- Remember: Use the right tool for the job
- Using built-in training and evaluation loops
	- Writing your own metrics
	- Using callbacks
	- Writing your own callbacks
	- Monitoring and visualization with TensorBoard
- Writing your own training and evaluation loops
	- Training versus inference
	- Low-level usage of metrics
	- A complete training and evaluation loop
	- Make it fast with tf.function
	- Leveraging fit() with a custom training loop


# 8 Introduction to deep learning for computer vision
- Introduction to convnets
	- The convolution operation
	- The max-pooling operation
- Training a convnet from scratch on a small dataset
	- The relevance of deep learning for small-data problems
	- Downloading the data
	- Building the model
	- Data preprocessing
	- Using data augmentation
- Leveraging a pretrained model
	- Feature extraction with a pretrained model
	- Fine-tuning a pretrained model


# 9 Advanced deep learning for computer vision
- Three essential computer vision tasks
- An image segmentation example
- Modern convnet architecture patterns
	- Modularity, hierarchy, and reuse
	- Residual connections
	- Batch normalization
	- Depthwise separable convolutions
	- Putting it together: A mini Xception-like model
- Interpreting what convnets learn
	- Visualizing intermediate activations
	- Visualizing convnet filters
	- Visualizing heatmaps of class activation


# 10 Deep learning for timeseries
- Different kinds of timeseries tasks
- A temperature-forecasting example
	- Preparing the data
	- A common-sense, non-machine learning baseline
	- Let's try a basic machine learning model
	- Let's try a 1D convolutional model
	- A first recurrent baseline
- Understanding recurrent neural networks
	- A recurrent layer in Keras
- Advanced use of recurrent neural networks
	- Using recurrent dropout to fight overfitting
	- Stacking recurrent layers
	- Using bidirectional RNNs
	- Going even further


# 11 Deep learning for text
- Natural language processing: The bird's eye view
- Preparing text data
	- Text standardization
	- Text splitting (tokenization)
	- Vocabulary indexing
	- Using the TextVectorization layer
- Two approaches for representing groups of words: Sets and sequences
	- Preparing the IMDB movie reviews data
	- Processing words as a set: The bag-of-words approach
	- Processing words as a sequence: The sequence model approach
- The Transformer architecture
	- Understanding self-attention
	- Multi-head attention
	- The Transformer encoder
	- When to use sequence models over bag-of-words models
- Beyond text classification: Sequence-to-sequence learning
	- A machine translation example
	- Sequence-to-sequence learning with RNNs
	- Sequence-to-sequence learning with Transformer


# 12 Generative deep learning
- Text generation
	- A brief history of generative deep learning for sequence generation
	- How do you generate sequence data?
	- The importance of the sampling strategy
	- Implementing text generation with Keras
	- A text-generation callback with variable-temperature sampling
	- Wrapping up
- DeepDream
	- Implementing DeepDream in Keras
	- Wrapping up
- Neural style transfer
	- The content loss
	- The style loss
	- Neural style transfer in Keras
	- Wrapping up
- Generating images with variational autoencoders
	- Sampling from latent spaces of images
	- Concept vectors for image editing
	- Variational autoencoders
	- Implementing a VAE with Keras
	- Wrapping up
- Introduction to generative adversarial networks
	- A schematic GAN implementation
	- A bag of tricks
	- Getting our hands on the CelebA dataset
	- The discriminator
	- The generator
	- The adversarial network
	- Wrapping up


# 13 Best practices for the real world
- Getting the most out of your models
	- Hyperparameter optimization
	- ensembling
- Scaling-up model training
	- Speeding up training on GPU with mixed precision
	- Multi-GPU training
	- TPU training


# 14 Conclusions
- Key concepts in review
	- Various approaches to AI
	- What makes deep learning special within the field of machine learning
	- How to think about deep learning
	- Key enabling technologies
	- The universal machine learning workflow
	- Key network architectures
	- The space of possibilities
- The limitations of deep learning
	- The risk of anthropomorphizing machine learning models
	- Automatons vs. intelligent agents
	- Local generalization vs. extreme generalization
	- The purpose of intelligence
	- Climbing the spectrum of generalization
- Setting the course toward greater generality in AI
	- On the importance of setting the right objective: The shortcut rule
	- A new target
- Implementing intelligence: The missing ingredients
	- Intelligence as sensitivity to abstract analogies
	- The two poles of abstraction
	- The missing half of the picture
- The future of deep learning
	- Models as programs
	- Blending together deep learning and program synthesis
	- Lifelong learning and modular subroutine reuse
	- The long-term vision
- Staying up to date in a fast-moving field
	- Practice on real-world problems using Kaggle
	- Read about the latest developments on arXiv
	- Explore the Keras ecosystem

# See Also
