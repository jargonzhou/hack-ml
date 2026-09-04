# TensorFlow in Action

- Part 1 Foundations of TensorFlow 2 and deep learning: 1-5
- Part 2 Look ma, no hands! Deep networks in the real world: 6-10
- Part 3 Advanced deep networks for complex problems: 11-15

# 1 The amazing world of TensorFlow
- What is TensorFlow?
	- An overview of popular components of TensorFlow
	- Building and deploying a machine learning model
- GPU vs. CPU
- When and when not to use TensorFlow
	- When to use TensorFlow
	- When not to use TensorFlow
- What will this book teach you?
	- TensorFlow fundamentals
	- Deep learning algorithms
	- Monitoring and optimization
- Who is this book for?
- Should we really care about Python and TensorFlow 2?

# 2 TensorFlow 2
- First steps with TensorFlow 2
	- How does TensorFlow operate under the hood?
- TensorFlow building blocks
	- Understanding tf.Variable
	- Understanding tf.Tensor
	- Understanding tf.Operation
- Neural network-related computations in TensorFlow
	- Matrix multiplication
	- Convolution operation
	- Pooling operation

# 3 Keras and data retrieval in TensorFlow 2/Keras与数据获取
- Keras model-building APIs
	- Introducing the data set
	- The Sequential API
	- The functional API
	- The sub-classing API
- Retrieving data for TensorFlow/Keras models
	- tf.data API
	- Keras DataGenerators
	- tensorflow-datasets package

# 4 Dipping toes in deep learning/深度学习入门
- Fully connected networks
	- Understanding the data
	- Autoencoder model
- Convolutional neural networks
	- Understanding the data
	- Implementing the network
- One step at a time: Recurrent neural networks (RNNs)
	- Understanding the data
	- Implementing the model
	- Predicting future CO2 values with the trained model

# 5 State-of-the-art in deep learning: Transformers/深度学习的前沿技术: Transformer
- Representing text as numbers
- Understanding the Transformer model
	- The encoder-decoder view of the Transformer
	- Diving deeper
	- Self-attention layer
	- Understanding self-attention using scalars
	- Self-attention as a cooking competition
	- Masked self-attention layers
	- Multi-head attention
	- Fully connected layer
	- Putting everything together

# 6 Teaching machines to see: Image classification with CNNs/让机器学会看: 基于CNN的图像分裂
- Putting the data under the microscope: Exploratory data analysis
	- The folder/file structure
	- Understanding the classes in the data set
	- Computing simple statistics on the data set
- Creating data pipelines using the Keras ImageDataGenerator
- Inception net: Implementing a state-of-the-art image classifier
	- Recap on CNNs
	- Inception net v1
	- Putting everything together
	- Other Inception models
- Training the model and evaluating performance

# 7 Teaching machines to see better: Improving CNNs and making them confess/让机器看的更准: 改进CNN并探究其内部机制
- Techniques for reducing overfitting
	- Image data augmentation with Keras
	- Dropout: Randomly switching off parts of your network to improve generalizability
	- Early stopping: Halting the training process if the network starts to underperform
- Toward minimalism: Minception instead of Inception
	- Implementing the stem
	- Implementing Inception-ResNet type A block
	- Implementing the Inception-ResNet type B block
	- Implementing the reduction block
	- Putting everything together
	- Training Minception
- If you can’t beat them, join ‘em: Using pretrained networks for enhancing performance
	- Transfer learning: Reusing existing knowledge in deep neural networks
- Grad-CAM: Making CNNs confess

# 8 Telling things apart: Image segmentation/区分不同对象: 图像分割
- Understanding the data
- Getting serious: Defining a TensorFlow data pipeline
	- Optimizing tf.data pipelines
	- The final tf.data pipeline
- DeepLabv3: Using pretrained networks to segment images
	- A quick overview of the ResNet-50 model
	- Atrous convolution: Increasing the receptive field of convolution layers with holes
	- Implementing DeepLab v3 using the Keras functional API
	- Implementing the atrous spatial pyramid pooling module
	- Putting everything together
- Compiling the model: Loss functions and evaluation metrics in image segmentation
	- Loss functions
	- Evaluation metrics
- Training the model
- Evaluating the model

# 9 Natural language processing with TensorFlow: Sentiment analysis/基于TF的自然语言处理: 情感分析
- What the text? Exploring and processing text
- Getting text ready for the model
	- Splitting training/validation and testing data
	- Analyze the vocabulary
	- Analyzing the sequence length
	- Text to words and then to numbers with Keras
- Defining an end-to-end NLP pipeline with TensorFlow
- Happy reviews mean happy customers: Sentiment analysis
	- LSTM Networks
	- Defining the final model
- Training and evaluating the model
- Injecting semantics with word vectors
	- Word embeddings
	- Defining the final model with word embeddings
	- Training and evaluating the model

# 10 Natural language processing with TensorFlow: Language modeling/基于TF的自然语言处理: 语言建模
- Processing the data
	- What is language modeling?
	- Downloading and playing with data
	- Too large vocabulary? N-grams to the rescue
	- Tokenizing text
	- Defining a tf.data pipeline
- GRUs in Wonderland: Generating text with deep learning
- Measuring the quality of the generated text
- Training and evaluating the language model
- Generating new text from the language model: Greedy decoding
- Beam search: Enhancing the predictive power of sequential models

# 11 Sequence-to-sequence learning: - Part 1/序列到序列学习-1
- Understanding the machine translation data
- Writing an English-German seq2seq machine translator
	- The TextVectorization layer
	- Defining the TextVectorization layers for the seq2seq model
	- Defining the encoder
	- Defining the decoder and the final model
	- Compiling the model
- Training and evaluating the model
- From training to inference: Defining the inference model

# 12 Sequence-to-sequence learning: - Part 2/序列到序列学习-2
- Eyeballing the past: Improving our model with attention
	- Implementing Bahdanau attention in TensorFlow
	- Defining the final model
	- Training the model
- Visualizing the attention

# 13 Transformers
- Transformers in more detail
	- Revisiting the basic components of the Transformer
	- Embeddings in the Transformer
	- Residuals and normalization
- Using pretrained BERT for spam classification
	- Understanding BERT
	- Classifying spam with BERT in TensorFlow
- Question answering with Hugging Face’s Transformers
	- Understanding the data
	- Processing data
	- Defining the DistilBERT model
	- Training the model
	- Ask BERT a question

# 14 TensorBoard: Big brother of TensorFlow
- Visualize data with TensorBoard
- Tracking and monitoring models with TensorBoard
- Using tf. to write custom metrics during model training
- Profiling models to detect performance bottlenecks
	- Optimizing the input pipeline
	- Mixed precision training
- Visualizing word vectors with the TensorBoard

# 15 TFX: MLOps and deploying models with TensorFlow/实现MLOps与模型部署
- Writing a data pipeline with TFX
	- Loading data from CSV files
	- Generating basic statistics from the data
	- Inferring the schema from data
	- Converting data to features
- Training a simple regression neural network: TFX Trainer API
	- Defining a Keras model
	- Defining the model training
	- SignatureDefs: Defining how models are used outside TensorFlow
	- Training the Keras model with TFX Trainer
- Setting up Docker to serve a trained model
- Deploying the model and serving it through an API
	- Validating the infrastructure
	- Resolving the correct model
	- Evaluating the model
	- Pushing the final model
	- Predicting with the TensorFlow serving API


# A: Setting up the environment
- In a Unix-based environment
	- Creating a virtual Python environment with Anaconda distribution (Ubuntu)
	- Prerequisites for GPU support (Ubuntu)
	- Notes on MacOS
- In Windows Environments
	- Creating a Virtual Python Environment (Anaconda)
	- Prerequisites for GPU support
- Activating and deactivating the conda environment
- Running the Jupyter Notebook server and creating notebooks
- Miscellaneous notes
# B: Computer vision
- Grad-CAM: Interpreting computer vision models
- Image segmentation: U-Net model
	- Understanding and defining the U-Net model
	- What’s better than an encoder? A pretrained encoder
# C: Natural language processing
- Touring around the zoo: Meeting other Transformer models
	- Generative pre-training (GPT) model (2018)
	- DistilBERT (2019)
	- RoBERT/ToBERT (2019)
	- BART (2019)
	- XLNet (2020)
	- Albert (2020)
	- Reformer (2020)

# See Also

