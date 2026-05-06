# Deep Learning for Coders with fastai and PyTorch

- I. Deep Learning in Practice: 1-3
- II. Understanding fastai’s Applications: 4-11
- III. Foundations of Deep Learning: 12-16
- IV. Deep Learning from Scratch: 17-20

# 1. Your Deep Learning Journey
## Deep Learning Is for Everyone
## Neural Networks: A Brief History
## Who We Are
## How to Learn Deep Learning
- Your Projects and Your Mindset
## The Software: PyTorch, fastai, and Jupyter (And Why It Doesn’t Matter)
## Your First Model
- Getting a GPU Deep Learning Server
- Running Your First Notebook
- What Is Machine Learning?
- What Is a Neural Network?
- A Bit of Deep Learning Jargon
- Limitations Inherent to Machine Learning
- How Our Image Recognizer Works
- What Our Image Recognizer Learned
- Image Recognizers Can Tackle Non-Image Tasks
- Jargon Recap
## Deep Learning Is Not Just for Image Classification
## Validation Sets and Test Sets
- Use Judgment in Defining Test Sets
## A Choose Your Own Adventure Moment


# 2. From Model to Production
## The Practice of Deep Learning
- Starting Your Project
- The State of Deep Learning
- The Drivetrain Approach
## Gathering Data
## From Data to DataLoaders
- Data Augmentation
## Training Your Model, and Using It to Clean Your Data
## Turning Your Model into an Online Application
- Using the Model for Inference
- Creating a Notebook App from the Model
- Turning Your Notebook into a Real App
- Deploying Your App
## How to Avoid Disaster
- Unforeseen Consequences and Feedback Loops
## Get Writing!


# 3. Data Ethics
## Key Examples for Data Ethics
- Bugs and Recourse: Buggy Algorithm Used for Healthcare Benefits
- Feedback Loops: YouTube’s Recommendation System
- Bias: Professor Latanya Sweeney “Arrested”
- Why Does This Matter?
## Integrating Machine Learning with Product Design
## Topics in Data Ethics
- Recourse and Accountability
- Feedback Loops
- Bias
- Disinformation
## Identifying and Addressing Ethical Issues
- Analyze a Project You Are Working On
- Processes to Implement
- The Power of Diversity
- Fairness, Accountability, and Transparency
## Role of Policy
- The Effectiveness of Regulation
- Rights and Policy
- Cars: A Historical Precedent


## Deep Learning in Practice: That’s a Wrap!


# 4. Under the Hood: Training a Digit Classifier
## Pixels: The Foundations of Computer Vision
## First Try: Pixel Similarity
- NumPy Arrays and PyTorch Tensors
## Computing Metrics Using Broadcasting
## Stochastic Gradient Descent
- Calculating Gradients
- Stepping with a Learning Rate
- An End-to-End SGD Example
- Summarizing Gradient Descent
## The MNIST Loss Function
- Sigmoid
- SGD and Mini-Batches
## Putting It All Together
- Creating an Optimizer
## Adding a Nonlinearity
- Going Deeper
## Jargon Recap


# 5. Image Classification
## From Dogs and Cats to Pet Breeds
## Presizing
- Checking and Debugging a DataBlock
## Cross-Entropy Loss
- Viewing Activations and Labels
- Softmax
- Log Likelihood
- Taking the log
## Model Interpretation
## Improving Our Model
- The Learning Rate Finder
- Unfreezing and Transfer Learning
- Discriminative Learning Rates
- Selecting the Number of Epochs
- Deeper Architectures



# 6. Other Computer Vision Problems
## Multi-Label Classification
- The Data
- Constructing a DataBlock
- Binary Cross Entropy
## Regression
- Assembling the Data
- Training a Model



# 7. Training a State-of-the-Art Model
## Imagenette
## Normalization
## Progressive Resizing
## Test Time Augmentation
## Mixup
## Label Smoothing



# 8. Collaborative Filtering Deep Dive
## A First Look at the Data
## Learning the Latent Factors
## Creating the DataLoaders
## Collaborative Filtering from Scratch
- Weight Decay
- Creating Our Own Embedding Module
## Interpreting Embeddings and Biases
- Using fastai.collab
- Embedding Distance
## Bootstrapping a Collaborative Filtering Model
## Deep Learning for Collaborative Filtering



# 9. Tabular Modeling Deep Dive
## Categorical Embeddings
## Beyond Deep Learning
## The Dataset
- Kaggle Competitions
- Look at the Data
## Decision Trees
- Handling Dates
- Using TabularPandas and TabularProc
- Creating the Decision Tree
- Categorical Variables
## Random Forests
- Creating a Random Forest
- Out-of-Bag Error
## Model Interpretation
- Tree Variance for Prediction Confidence
- Feature Importance
- Removing Low-Importance Variables
- Removing Redundant Features
- Partial Dependence
- Data Leakage
- Tree Interpreter
## Extrapolation and Neural Networks
- The Extrapolation Problem
- Finding Out-of-Domain Data
- Using a Neural Network
## Ensembling
- Boosting
- Combining Embeddings with Other Methods



# 10. NLP Deep Dive: RNNs
## Text Preprocessing
- Tokenization
- Word Tokenization with fastai
- Subword Tokenization
- Numericalization with fastai
- Putting Our Texts into Batches for a Language Model
## Training a Text Classifier
- Language Model Using DataBlock
- Fine-Tuning the Language Model
- Saving and Loading Models
- Text Generation
- Creating the Classifier DataLoaders
- Fine-Tuning the Classifier
## Disinformation and Language Models



# 11. Data Munging with fastai’s Mid-Level API
## Going Deeper into fastai’s Layered API
- Transforms
- Writing Your Own Transform
- Pipeline
## TfmdLists and Datasets: Transformed Collections
- TfmdLists
- Datasets
## Applying the Mid-Level Data API: SiamesePair


## Understanding fastai’s Applications: Wrap Up

# 12. A Language Model from Scratch
## The Data
## Our First Language Model from Scratch
- Our Language Model in PyTorch
- Our First Recurrent Neural Network
## Improving the RNN
- Maintaining the State of an RNN
- Creating More Signal
## Multilayer RNNs
- The Model
- Exploding or Disappearing Activations
## LSTM
- Building an LSTM from Scratch
- Training a Language Model Using LSTMs
## Regularizing an LSTM
- Dropout
- Activation Regularization and Temporal Activation Regularization
- Training a Weight-Tied Regularized LSTM



# 13. Convolutional Neural Networks
## The Magic of Convolutions
- Mapping a Convolutional Kernel
- Convolutions in PyTorch
- Strides and Padding
- Understanding the Convolution Equations
## Our First Convolutional Neural Network
- Creating the CNN
- Understanding Convolution Arithmetic
- Receptive Fields
- A Note About Twitter
## Color Images
## Improving Training Stability
- A Simple Baseline
- Increase Batch Size
- 1cycle Training
- Batch Normalization



# 14. ResNets
## Going Back to Imagenette
## Building a Modern CNN: ResNet
- Skip Connections
- A State-of-the-Art ResNet
- Bottleneck Layers



# 15. Application Architectures Deep Dive
## Computer Vision
- cnn_learner
- unet_learner
- A Siamese Network
## Natural Language Processing
## Tabular



# 16. The Training Process
## Establishing a Baseline
## A Generic Optimizer
## Momentum
## RMSProp
## Adam
## Decoupled Weight Decay
## Callbacks
- Creating a Callback
- Callback Ordering and Exceptions


## Foundations of Deep Learning: Wrap Up

# 17. A Neural Net from the Foundations
## Building a Neural Net Layer from Scratch
- Modeling a Neuron
- Matrix Multiplication from Scratch
- Elementwise Arithmetic
- Broadcasting
- Einstein Summation
## The Forward and Backward Passes
- Defining and Initializing a Layer
- Gradients and the Backward Pass
- Refactoring the Model
- Going to PyTorch



# 18. CNN Interpretation with CAM
## CAM and Hooks
## Gradient CAM



# 19. A fastai Learner from Scratch
## Data
- Dataset
## Module and Parameter
- Simple CNN
## Loss
## Learner
- Callbacks
- Scheduling the Learning Rate



# 20. Concluding Thoughts

# A. Creating a Blog
- Blogging with GitHub Pages
- Creating the Repository
- Setting Up Your Home Page
- Creating Posts
- Synchronizing GitHub and Your Computer
- Jupyter for Blogging

# B. Data Project Checklist
- Data Scientists
- Strategy
- Data
- Analytics
- Implementation
- Maintenance
- Constraints

# See Also

