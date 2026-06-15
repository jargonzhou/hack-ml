# Deep Learning with PyTorch: Training and applying deep learning and generative AI models, 2nd Edition

action: [hack-pytorch](../../codes/hack-pytorch/README.md#deep-learning-with-pytorch-training-and-applying-deep-learning-and-generative-ai-models-2nd-edition)


- Part 1 Core PyTorch: 1-8
- Part 2 Practical deep learning applications: 9-17

# 1. Introducing deep learning and the PyTorch library
- What is deep learning?
- The shift from machine learning to deep learning
- What to expect
- Why PyTorch?
	- The deep learning competitive landscape
- How PyTorch supports deep learning projects
- Hardware and software requirements
	- Using Jupyter Notebooks

Figure 1.2 Basic, high-level structure of a PyTorch project, with data loading, training, and deployment to production

# 2. Pretrained networks/预训练网络
- A pretrained network that recognizes the subject of an image
	- Obtaining a pretrained network for image recognition
	- AlexNet
	- The Vision Transformer
	- Ready, set, almost run
	- Run!
- Generating and editing images
	- The inpainting process
	- A network that turns horses into zebras
- Model Zoo: Hugging Face
- A pretrained network that describes scenes
	- BLIP in action


# 3. It starts with a tensor/张量
- The world as floating-point numbers
- Tensors: Multidimensional arrays/多维数组
	- From Python lists to PyTorch tensors
	- Constructing our first tensors
	- The essence of tensors
- Indexing tensors/索引张量
- Broadcasting/广播
- Named tensors/命名的张量
- Tensor element types/张量的元素类型
	- Specifying the numeric type with dtype
	- A dtype for every occasion
	- Managing a tensor’s dtype attribute
- The tensor API
- Tensors: Scenic views of storage/张量存储
	- Indexing into storage
	- Modifying stored values: In-place operations
- Tensor metadata: Size, offset, and stride/张量元数据: 大小, 偏移量和步长
	- Views of another tensor’s storage
	- Transposing without copying
	- Transposing in higher dimensions
	- Contiguous tensors
- Moving tensors to the GPU/移动张量到GPU
	- Managing a tensor’s device attribute
- NumPy interoperability/NumPy互操作
- Generalized tensors/广义张量 are tensors, too
- Serializing tensors/序列化张量
	- Serializing to HDF5 with h5py


# 4. Real-world data representation using tensors/现实世界中使用张量的数据表示
- Working with images/图像
	- Adding color channels
	- Loading an image file
	- Changing the layout
	- Normalizing the data
- 3D images: Volumetric data
	- Loading a specialized format
- Representing tabular data/表格数据
	- Using a real-world dataset
	- Loading a wine data tensor
	- Representing scores
	- One-hot encoding
	- When to categorize
	- Finding thresholds
- Working with time series/时序数据
	- Adding a time dimension
	- Shaping the data by time period
	- Ready for training
- Representing text/文本
	- Converting text to numbers
	- One-hot-encoding characters
	- One-hot encoding whole words
	- Text embeddings
	- Text embeddings as a blueprint


# 5. The mechanics of learning/学习的机制
- A timeless lesson in modeling
- Learning is just parameter estimation/参数估计
	- A hot problem
	- Gathering some data
	- Visualizing the data
	- Choosing a linear model as a first try
- Less loss is what we want/小损失
	- From problem back to PyTorch
- Down along the gradient/梯度下降
	- Decreasing loss
	- Getting analytical
	- Iterating to fit the model
	- Normalizing inputs
	- Visualizing (again)
- PyTorch’s autograd: Backpropagating all things/PyTorch的自动求导
	- Computing the gradient automatically
	- Optimizers à la carte
	- Training, validation, and overfitting
	- Training set
	- Autograd nits and switching it off


# 6. Using a neural network to fit the data/使用神经网络拟合数据
- Artificial neurons
	- Composing a multilayer network
	- Understanding the error function/错误函数
	- Adding nonlinearity with activation functions/激活函数
  	- Capping The Output Range: `torch.nn.Hardtanh`
    - Compressing The Output Range: `torch.nn.Sigmoid`
	- More activation functions
  	- `Tanh`
  	- `Softplus`
  	- `Hardtanh`
  	- `ReLU`
  	- `Sigmoid`
  	- `LeakyReLU`
	- Choosing the best activation function
	- What learning means for a neural network
- The PyTorch `nn` module
	- Using `nn.Module` as a callable
	- Returning to the linear model
- Finally, a neural network
	- Replacing the linear model
	- Inspecting the parameters
	- Comparing to the linear model


# 7. Telling birds from airplanes: Learning from images/图像
- A dataset of tiny images
	- Downloading CIFAR-10
	- The `Dataset` class
	- Dataset transforms/数据集转换
  	- `ToTensor`
  	- `Normalize`
  	- `Compose`
	- Normalizing data
- Distinguishing birds from airplanes
	- Building the dataset
	- A fully connected model
	- Output of a classifier
	- Representing the output as probabilities
	- Training the classifier
	- The limits of going fully connected


# 8. Using convolutions to generalize/利用卷积进行泛化
- The case for convolutions
	- What convolutions do
- Convolutions in action: `Conv1d`, `Conv2d`, `Conv3d`
	- Padding the boundary
	- Detecting features with convolutions
	- Looking further with depth and pooling
  	- downsampling, pooling, subsampling/降采样, 池化, 子采样: `MaxPool2d`
	- Putting it all together for our network
- Subclassing `nn.Module`
	- Our network as an `nn.Module`
	- How PyTorch keeps track of parameters and submodules
	- The functional API
- Training our convolutional neural network/训练卷积神经网络
	- Measuring accuracy
	- Saving and loading our model
	- Training on the GPU
- Model design/模型设计
	- Adding memory capacity: Width/宽度
	- Helping our model to converge and generalize: Regularization/正则化
  	- weight penalties/权重惩罚
  	- dropout/丢弃
  	- batch normalization/批归一化
	- Going deeper to learn more complex structures: Depth/深度
  	- skip connection/跳过连接
  	- initialization/(权重)初始化
	- Comparing the designs from this section
	- It’s already outdated


Figure 8.12 Our baseline convolutional network architecture

# 9. How transformers work/Transformer工作原理
- A motivating example: Generating names character by character
- Self-supervised learning
	- Limits of the bigram model
- Generating our training data
- Embeddings and linear layers
	- Visualizing embeddings
- Attention
	- Dot product self-attention
	- Scaled dot product causal self-attention
- Transformers
	- The decoder
- Other Transformer architectures
	- The encoder
	- The encoder-decoder
- Tokenization
	- Generating sentences
- The Vision Transformer


# 10. Diffusion models for images/图像扩散模型
- History of VAEs and GANs
- Motivator for diffusion models
- Diffusion in detail
- Setting up the data
- The forward process
- Training
	- Loss
- Reversing diffusion (how to sample)


# 11. Using PyTorch to fight cancer/利用PyTorch对抗癌症
- Introduction to the use case
- Preparing for a large-scale project
- What is a CT scan, exactly?
- The project: An end-to-end detector for lung cancer
	- Why can’t we just throw data at a neural network until it works?
	- Our data source: The LUNA Grand Challenge
	- Downloading the LUNA data

# 12. Combining data sources into a unified dataset/将数据源合并成统一的数据集
- Raw CT data files
- Parsing LUNA’s annotation data
	- Training and validation sets
	- Unifying our annotation and candidate data
- Loading individual CT scans
	- Hounsfield Units
- Locating a nodule using the patient coordinate system
	- The patient coordinate system
	- CT scan shape and voxel sizes
	- Converting between millimeters and voxel addresses
	- Extracting a nodule from a CT scan
- Straightforward dataset implementation
	- Caching candidate arrays with the getCtRawCandidate function
	- Constructing our dataset in `LunaDataset.__init__`
	- A training/validation split
	- Rendering the data


# 13. Training a classification model to detect suspected tumors/训练分类模型以检测疑似肿瘤
- A foundational model and training loop
- The main entry point for our application
- Pretraining setup and initialization
	- Initializing the model and optimizer
	- Care and feeding of data loaders
- Our first-pass neural network design
	- The core convolutions
	- The full model
- Training and validating the model
	- The computeBatchLoss function
	- The validation loop is similar
- Outputting performance metrics
	- The logMetrics function
- Running the training script
	- Data needed for training
	- Interlude: The tqdm function
- Evaluating the model: Getting 99.7% correct means we’re done, right?
- Graphing training metrics with TensorBoard
	- Running TensorBoard
	- Adding TensorBoard support to the metrics logging function
- Why isn’t the model learning to detect nodules?


# 14. Improving training with metrics and augmentation/利用指标和增强技术改进训练
- High-level plan for improvement
- Good dogs vs. bad guys: False positives and false negatives
- Graphing the positives and negatives
	- Recall is Chirpy’s strength
	- Precision is Dozer’s forte
	- Implementing precision and recall in logMetrics
	- Our ultimate performance metric: The F1 score
	- How does our model perform with our new metrics?
- What does an ideal dataset look like?
	- Making the data look less like the actual and more like the “ideal”
	- Contrasting training with a balanced LunaDataset to previous runs
	- Recognizing the symptoms of overfitting
- Revisiting the problem of overfitting
	- An overfit face-to-age prediction model
- Preventing overfitting with data augmentation
	- Specific data augmentation techniques
	- Seeing the improvement from data augmentation


# 15. Using segmentation to find suspected nodules/利用分割查找疑似结节
- Utilizing a second model in our project
- Various types of segmentation
- Semantic segmentation: Per-pixel classification
	- The Segment Anything model (SAM)
- SAM architecture
	- Trying out an off-the-shelf model for our project
- Using the SAM model directly
- Updating the dataset for segmentation
	- Working around SAM’s limitation on 2D data
	- Building the segmentation dataset
	- Training a model to flag potential candidates
- Updating our training for fine-tuning
	- How to fine-tune a model
	- Using the AdamW optimizer
	- Designing our training loop
	- Saving our model
- Inference and results


# 16. Training models on multiple GPUs/在多个GPU上训练模型
- Introduction to parallel programming
	- Distributed computing terminology
	- Hardware requirements
	- Initializing a distributed program
- Collective communication
- Introduction to parallelisms
- Data parallelism
- Model parallelism
	- Pipeline parallelism
	- Tensor parallelism
	- Deciding between pipeline and tensor parallelism
- n-dimensional parallelism
- Fully sharded data parallelism
- Large language model–specific parallelisms
	- Context parallelism
	- Expert Parallelism
- Tying all parallelisms together


# 17. Deploying to production/部署到生产环境
- Serving PyTorch models
	- Our model served by Gradio
	- Our model behind a FastAPI server
	- What we want from deployment
	- Request batching and streaming responses
	- How to make PyTorch models even faster
- Exporting models
	- Interoperability beyond PyTorch with ONNX
	- PyTorch’s own export: torch.export
- Expanding on torch.compile
	- Full graph capture vs. disjoint graphs
- Understanding execution with torch.profiler
- Using PyTorch outside of Python
	- LibTorch: PyTorch in C++
- Going mobile: ExecuTorch


# See Also
* David MacKay. **Information Theory, Inference, and Learning Algorithms** (Cambridge University Press, 2003).
* [Natural Language Processing with PyTorch: Build Intelligent Language Applications Using Deep Learning](../nlp/book.Natural%20Language%20Processing%20with%20PyTorch.md)


DL landscape
- low level
  - Theano
  - TensorFlow, JAX
- hign level
  - Lasagne
  - Keras
- others
  - Caffe
  - Chainer
  - DyNet
  - Torch: Lua
  - MXNet
  - CNTK
  - DL4J

datasets
- ImageNet - http://imagenet.stanford.edu
- WordNet - http://wordnet.princeton.edu
- Digital Imaging and Communications in Medicine (DICOM) files (from the Cancer Imaging Archive’s CPTAC-LSCC collection: https://mng.bz/AGZg)
- The Wine Quality dataset - https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv
- data from a Washington, DC, bike-sharing system - https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset
- Jane Austen’s Pride and Prejudice from the Project Gutenberg - http://www.gutenberg.org/files/1342/1342-0.txt
- the English Corpora - https://www.english-corpora.org/
- MNIST
- CIFAR-10, CIFAR-100

models
- computer vision
  - AlexNet - http://mng.bz/lo6z
  - Inception v3 - https://arxiv.org/pdf/1512.00567.pdf
  - VisionTransformer - https://arxiv.org/pdf/2010.11929.pdf
    - vit_b_16
  - HF Diffusers
    - sd2-community/stable-diffusion-2-inpainting
	- HF BLIP: Bootstrapping LanguageImage Pre-training for Unified Vision-Language Understanding and Generation - https://arxiv.org/pdf/2201.12086.pdf
  	- Salesforce/blip-image-captioning-large

GPU support
- Nvidia CUDA-enabled GPUs
- AMD ROCm platform
- Apple Silicon Mac: MPS(Metal Performance Shaders)
- Google TPU: `torch_xla`
- Intel XPU: `intel_extension_for_pytorch`


tools
- imageio - https://github.com/imageio/imageio
