# Math and Architectures of Deep Learning


# 1 An overview of machine learning and deep learning
## 1.1 A first look at machine/deep learning: A paradigm shift in computation
## 1.2 A function approximation view of machine learning:Models and their training
## 1.3 A simple machine learning model: The cat brain
### 1.3.1 Input features
### 1.3.2 Output decisions
### 1.3.3 Model estimation
### 1.3.4 Model architecture selection
### 1.3.5 Model training
### 1.3.6 Inferencing
## 1.4 Geometrical view of machine learning
## 1.5 Regression vs. classification in machine learning
## 1.6 Linear vs. nonlinear models
## 1.7 Higher expressive power through multiple nonlinear layers: Deep neural networks


# 2 Vectors, matrices, and tensors in machine learning
## 2.1 Vectors and their role in machine learning
### 2.1.1 The geometric view of vectors and its significance in machine learning
## 2.2 PyTorch code for vector manipulations
### 2.2.1 PyTorch code for the introduction to vectors
## 2.3 Matrices and their role in machine learning
### 2.3.1 Matrix representation of digital images
## 2.4 Python code: Introducing matrices, tensors, and images via PyTorch
## 2.5 Basic vector and matrix operations in machine learning
### 2.5.1 Matrix and vector transpose
### 2.5.2 Dot product of two vectors and its role in machine learning
### 2.5.3 Matrix multiplication and machine learning
### 2.5.4 Length of a vector (L2 norm): Model error
### 2.5.5 Geometric intuitions for vector length
### 2.5.6 Geometric intuitions for the dot product: Feature similarity
## 2.6 Orthogonality of vectors and its physical significance
## 2.7 Python code: Basic vector and matrix operations via PyTorch
### 2.7.1 PyTorch code for a matrix transpose
### 2.7.2 PyTorch code for a dot product
### 2.7.3 PyTorch code for matrix vector multiplication
### 2.7.4 PyTorch code for matrix-matrix multiplication
### 2.7.5 PyTorch code for the transpose of a matrix product
## 2.8 Multidimensional line and plane equations and machine learning
### 2.8.1 Multidimensional line equation
### 2.8.2 Multidimensional planes and their role in machine learning
## 2.9 Linear combinations, vector spans, basis vectors, and collinearity preservation
### 2.9.1 Linear dependence
### 2.9.2 Span of a set of vectors
### 2.9.3 Vector spaces, basis vectors, and closure
## 2.10 Linear transforms: Geometric and algebraic interpretations
### 2.10.1 Generic multidimensional definition of linear transforms
### 2.10.2 All matrix-vector multiplications are linear transforms
## 2.11 Multidimensional arrays, multilinear transforms, and tensors
### 2.11.1 Array view: Multidimensional arrays of numbers
## 2.12 Linear systems and matrix inverse
### 2.12.1 Linear systems with zero or near-zero determinants,and ill-conditioned systems
### 2.12.2 PyTorch code for inverse, determinant, and singularity testing of matrices
### 2.12.3 Over- and under-determined linear systems in machine learning
### 2.12.4 Moore Penrose pseudo-inverse of a matrix
### 2.12.5 Pseudo-inverse of a matrix: A beautiful geometric intuition
### 2.12.6 PyTorch code to solve overdetermined systems
## 2.13 Eigenvalues and eigenvectors: Swiss Army knives of machine learning
### 2.13.1 Eigenvectors and linear independence
### 2.13.2 Symmetric matrices and orthogonal eigenvectors
### 2.13.3 PyTorch code to compute eigenvectors and eigenvalues
## 2.14 Orthogonal (rotation) matrices and their eigenvalues and eigenvectors
### 2.14.1 Rotation matrices
### 2.14.2 Orthogonality of rotation matrices
### 2.14.3 PyTorch code for orthogonality of rotation matrices
### 2.14.4 Eigenvalues and eigenvectors of a rotation matrix:Finding the axis of rotation
### 2.14.5 PyTorch code for eigenvalues and vectors of rotation matrices
## 2.15 Matrix diagonalization
### 2.15.1 PyTorch code for matrix diagonalization
### 2.15.2 Solving linear systems without inversion via diagonalization
### 2.15.3 PyTorch code for solving linear systems via diagonalization
### 2.15.4 Matrix powers using diagonalization
## 2.16 Spectral decomposition of a symmetric matrix
### 2.16.1 PyTorch code for the spectral decomposition of a matrix
## 2.17 An application relevant to machine learning: Finding the axes of a hyperellipse
### 2.17.1 PyTorch code for hyperellipses


# 3 Classifiers and vector calculus
## 3.1 Geometrical view of image classification
### 3.1.1 Input representation
### 3.1.2 Classifiers as decision boundaries
### 3.1.3 Modeling in a nutshell
### 3.1.4 Sign of the surface function in binary classification
## 3.2 Error, aka loss function
## 3.3 Minimizing loss functions: Gradient vectors
### 3.3.1 Gradients: A machine learning-centric introduction
### 3.3.2 Level surface representation and loss minimization
## 3.4 Local approximation for the loss function
### 3.4.1 1D Taylor series recap
### 3.4.2 Multidimensional Taylor series and the Hessian matrix
## 3.5 PyTorch code for gradient descent, error minimization,and model training
### 3.5.1 PyTorch code for linear models
### 3.5.2 Autograd: PyTorch automatic gradient computation
### 3.5.3 Nonlinear Models in PyTorch
### 3.5.4 A linear model for the cat brain in PyTorch
## 3.6 Convex and nonconvex functions, and global and local minima
## 3.7 Convex sets and functions
### 3.7.1 Convex sets
### 3.7.2 Convex curves and surfaces
### 3.7.3 Convexity and the Taylor series
### 3.7.4 Examples of convex functions


# 4 Linear algebraic tools in machine learning
## 4.1 Distribution of feature data points and true dimensionality
## 4.2 Quadratic forms and their minimization
### 4.2.1 Minimizing quadratic forms
### 4.2.2 Symmetric positive (semi)definite matrices
## 4.3 Spectral and Frobenius norms of a matrix
### 4.3.1 Spectral norms
### 4.3.2 Frobenius norms
## 4.4 Principal component analysis
### 4.4.1 Direction of maximum spread
### 4.4.2 PCA and dimensionality reduction
### 4.4.3 PyTorch code: PCA and dimensionality reduction
### 4.4.4 Limitations of PCA
### 4.4.5 PCA and data compression
## 4.5 Singular value decomposition
### 4.5.1 Informal proof of the SVD theorem
### 4.5.2 Proof of the SVD theorem
### 4.5.3 Applying SVD: PCA computation
### 4.5.4 Applying SVD: Solving arbitrary linear systems
### 4.5.5 Rank of a matrix
### 4.5.6 PyTorch code for solving linear systems with SVD
### 4.5.7 PyTorch code for PCA computation via SVD
### 4.5.8 Applying SVD: Best low-rank approximation of a matrix
## 4.6 Machine learning application: Document retrieval
### 4.6.1 Using TF-IDF and cosine similarity
### 4.6.2 Latent semantic analysis
### 4.6.3 PyTorch code to perform LSA
### 4.6.4 PyTorch code to compute LSA and SVD on a large dataset


# 5 Probability distributions in machine learning
## 5.1 Probability: The classical frequentist view
### 5.1.1 Random variables
### 5.1.2 Population histograms
## 5.2 Probability distributions
## 5.3 Basic concepts of probability theory
### 5.3.1 Probabilities of impossible and certain events
### 5.3.2 Exhaustive and mutually exclusive events
### 5.3.3 Independent events
## 5.4 Joint probabilities and their distributions
### 5.4.1 Marginal probabilities
### 5.4.2 Dependent events and their joint probability distribution
## 5.5 Geometrical view: Sample point distributions for dependent and independent variables
## 5.6 Continuous random variables and probability density
## 5.7 Properties of distributions: Expected value, variance, and covariance
### 5.7.1 Expected value (aka mean)
### 5.7.2 Variance, covariance, and standard deviation
## 5.8 Sampling from a distribution
## 5.9 Some famous probability distributions
### 5.9.1 Uniform random distributions
### 5.9.2 Gaussian (normal) distribution
### 5.9.3 Binomial distribution
### 5.9.4 Multinomial distribution
### 5.9.5 Bernoulli distribution
### 5.9.6 Categorical distribution and one-hot vectors


# 6 Bayesian tools for machine learning
## 6.1 Conditional probability and Bayes’ theorem
### 6.1.1 Joint and marginal probability revisited
### 6.1.2 Conditional probability
### 6.1.3 Bayes’ theorem
## 6.2 Entropy
### 6.2.1 Geometrical intuition for entropy
### 6.2.2 Entropy of Gaussians
## 6.3 Cross-entropy
## 6.4 KL divergence
### 6.4.1 KLD between Gaussians
## 6.5 Conditional entropy
### 6.5.1 Chain rule of conditional entropy
## 6.6 Model parameter estimation
### 6.6.1 Likelihood, evidence, and posterior and prior probabilities
### 6.6.2 Maximum likelihood parameter estimation (MLE)
### 6.6.3 Maximum a posteriori (MAP) parameter estimation and regularization
## 6.7 Latent variables and evidence maximization
## 6.8 Maximum likelihood parameter estimation for Gaussians
### 6.8.1 Python PyTorch code for maximum likelihood estimation
### 6.8.2 Python PyTorch code for maximum likelihood estimation using gradient descent
## 6.9 Gaussian mixture models
### 6.9.1 Probability density function of the GMM
### 6.9.2 Latent variables for class selection
### 6.9.3 Classification via GMM
### 6.9.4 Maximum likelihood estimation of GMM parameters (GMM fit)


# 7 Function approximation: How neural networks model the world
## 7.1 Neural networks: A 10,000-foot view
## 7.2 Expressing real-world problems: Target functions
### 7.2.1 Logical functions in real-world problems
### 7.2.2 Classifier functions in real-world problems
### 7.2.3 General functions in real-world problems
## 7.3 The basic building block or neuron: The perceptron
### 7.3.1 The Heaviside step function
### 7.3.2 Hyperplanes
### 7.3.3 Perceptrons and classification
### 7.3.4 Modeling common logic gates with perceptrons
## 7.4 Toward more expressive power: Multilayer perceptrons (MLPs)
### 7.4.1 MLP for logical XOR
## 7.5 Layered networks of perceptrons: MLPs or neural networks
### 7.5.1 Layering
### 7.5.2 Modeling logical functions with MLPs
### 7.5.3 Cybenko’s universal approximation theorem
### 7.5.4 MLPs for polygonal decision boundaries


# 8 Training neural networks: Forward propagation and backpropagation
## 8.1 Differentiable step-like functions
### 8.1.1 Sigmoid function
### 8.1.2 Tanh function
## 8.2 Why layering?
## 8.3 Linear layers
### 8.3.1 Linear layers expressed as matrix-vector multiplication
### 8.3.2 Forward propagation and grand output functions for an MLP of linear layers
## 8.4 Training and backpropagation
### 8.4.1 Loss and its minimization: Goal of training
### 8.4.2 Loss surface and gradient descent
### 8.4.3 Why a gradient provides the best direction for descent
### 8.4.4 Gradient descent and local minima
### 8.4.5 The backpropagation algorithm
### 8.4.6 Putting it all together: Overall training algorithm
## 8.5 Training a neural network in PyTorch


# 9 Loss, optimization, and regularization
## 9.1 Loss functions
### 9.1.1 Quantification and geometrical view of loss
### 9.1.2 Regression loss
### 9.1.3 Cross-entropy loss
### 9.1.4 Binary cross-entropy loss for image and vector mismatches
### 9.1.5 Softmax
### 9.1.6 Softmax cross-entropy loss
### 9.1.7 Focal loss
### 9.1.8 Hinge loss
## 9.2 Optimization
### 9.2.1 Geometrical view of optimization
### 9.2.2 Stochastic gradient descent and minibatches
### 9.2.3 PyTorch code for SGD
### 9.2.4 Momentum
### 9.2.5 Geometric view: Constant loss contours, gradient descent, and momentum
### 9.2.6 Nesterov accelerated gradients
### 9.2.7 AdaGrad
### 9.2.8 Root-mean-squared propagation
### 9.2.9 Adam optimizer
## 9.3 Regularization
### 9.3.1 Minimum descriptor length: An Occam’s razor view of optimization
### 9.3.2 L2 regularization
### 9.3.3 L1 regularization
### 9.3.4 Sparsity: L1 vs. L2 regularization
### 9.3.5 Bayes’ theorem and the stochastic view of optimization
### 9.3.6 Dropout


# 10 Convolutions in neural networks
## 10.1 One-dimensional convolution: Graphical and algebraical view
### 10.1.1 Curve smoothing via 1D convolution
### 10.1.2 Curve edge detection via 1D convolution
### 10.1.3 One-dimensional convolution as matrix multiplication
### 10.1.4 PyTorch- One-dimensional convolution with custom weights
## 10.2 Convolution output size
## 10.3 Two-dimensional convolution: Graphical and algebraic view
### 10.3.1 Image smoothing via 2D convolution
### 10.3.2 Image edge detection via 2D convolution
### 10.3.3 PyTorch- 2D convolution with custom weights
### 10.3.4 Two-dimensional convolution as matrix multiplication
## 10.4 Three-dimensional convolution
### 10.4.1 Video motion detection via 3D convolution
### 10.4.2 PyTorch- Three-dimensional convolution with custom weights
## 10.5 Transposed convolution or fractionally strided convolution
### 10.5.1 Application of transposed convolution: Autoencoders and embeddings
### 10.5.2 Transposed convolution output size
### 10.5.3 Upsampling via transpose convolution
## 10.6 Adding convolution layers to a neural network
### 10.6.1 PyTorch- Adding convolution layers to a neural network
## 10.7 Pooling


# 11 Neural networks for image classification and object detection
## 11.1 CNNs for image classification: LeNet
### 11.1.1 PyTorch- Implementing LeNet for image classification on MNIST
## 11.2 Toward deeper neural networks
### 11.2.1 VGG (Visual Geometry Group) Net
### 11.2.2 Inception: Network-in-network paradigm
### 11.2.3 ResNet: Why stacking layers to add depth does not scale
### 11.2.4 PyTorch Lightning
## 11.3 Object detection: A brief history
### 11.3.1 R-CNN
### 11.3.2 Fast R-CNN
### 11.3.3 Faster R-CNN
## 11.4 Faster R-CNN: A deep dive
### 11.4.1 Convolutional backbone
### 11.4.2 Region proposal network
### 11.4.3 Fast R-CNN
### 11.4.4 Training the Faster R-CNN
### 11.4.5 Other object-detection paradigms


# 12 Manifolds, homeomorphism, and neural networks
## 12.1 Manifolds
### 12.1.1 Hausdorff property
### 12.1.2 Second countable property
## 12.2 Homeomorphism
## 12.3 Neural networks and homeomorphism between manifolds


# 13 Fully Bayes model parameter estimation
## 13.1 Fully Bayes estimation: An informal introduction
### 13.1.1 Parameter estimation and belief injection
## 13.2 MLE for Gaussian parameter values recap)
## 13.3 Fully Bayes parameter estimation: Gaussian, unknown mean, known precision
## 13.4 Small and large volumes of training data, and strong and weak priors
## 13.5 Conjugate priors
## 13.6 Fully Bayes parameter estimation: Gaussian, unknown precision, known mean
### 13.6.1 Estimating the precision parameter
## 13.7 Fully Bayes parameter estimation: Gaussian, unknown mean, unknown precision
### 13.7.1 Normal-gamma distribution
### 13.7.2 Estimating the mean and precision parameters
## 13.8 Example: Fully Bayesian inferencing
### 13.8.1 Maximum likelihood estimation
### 13.8.2 Bayesian inference
## 13.9 Fully Bayes parameter estimation: Multivariate Gaussian, unknown mean, known precision
## 13.10 Fully Bayes parameter estimation: Multivariate, unknown precision, known mean
### 13.10.1 Wishart distribution
### 13.10.2 Estimating precision


# 14 Latent space and generative modeling, autoencoders, and variational autoencoders
## 14.1 Geometric view of latent spaces
## 14.2 Generative classifiers
## 14.3 Benefits and applications of latent-space modeling
## 14.4 Linear latent space manifolds and PCA
### 14.4.1 PyTorch code for dimensionality reduction using PCA
## 14.5 Autoencoders
### 14.5.1 Autoencoders and PCA
## 14.6 Smoothness, continuity, and regularization of latent spaces
## 14.7 Variational autoencoders
### 14.7.1 Geometric overview of VAEs
### 14.7.2 VAE training, losses, and inferencing
### 14.7.3 VAEs and Bayes’ theorem
### 14.7.4 Stochastic mapping leads to latent-space smoothness
### 14.7.5 Direct minimization of the posterior requires prohibitively expensive normalization
### 14.7.6 ELBO and VAEs
### 14.7.7 Choice of prior: Zero-mean, unit-covariance Gaussian
### 14.7.8 Reparameterization trick


# Appendix A
## A.1 Dot product and cosine of the angle between two vectors
## A.2 Determinants
## A.3 Computing the variance of a Gaussian distribution
## A.4 Two theorems in statistics
### A.4.1 Jensen’s Inequality
### A.4.2 Log sum inequality
## A.5 Gamma functions and distribution
### A.5.1 Gamma function
### A.5.2 Gamma distribution
