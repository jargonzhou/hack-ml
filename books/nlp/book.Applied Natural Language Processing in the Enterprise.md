# Applied Natural Language Processing in the Enterprise

brief description of the algorithms (sequence modeling, NN architecture etc) of NLP tasks. - skimmed 2026-04-28

- I. Scratching the Surface/浅尝辄止: 1-3
- II. The Cogs in the Machine/机器中的齿轮: 4-8
- III. Outside the Wall/墙外: 9-12

# 1. Introduction to NLP
## What Is NLP?
- Popular Applications
- History
- Inflection Points
- A Final Word
## Basic NLP
- Defining NLP Tasks
- Set Up the Programming Environment
- spaCy, fast.ai, and Hugging Face
- Perform NLP Tasks Using spaCy

# 2. Transformers and Transfer Learning
## Training with fastai
- Using the fastai Library
- ULMFiT for Transfer Learning
- Fine-Tuning a Language Model on IMDb
- Training a Text Classifier
## Inference with Hugging Face
- Loading Models
- Generating Predictions

# 3. NLP Tasks and Applications
## Pretrained Language Models
## Transfer Learning and Fine-Tuning
## NLP Tasks
## Natural Language Dataset
- Explore the AG Dataset
## NLP Task #1: Named Entity Recognition
- Perform Inference Using the Original spaCy Model
- Custom NER
- Annotate via Prodigy: NER
- Train the Custom NER Model Using spaCy
- Custom NER Model Versus Original NER Model
## NLP Task #2: Text Classification
- Annotate via Prodigy: Text Classification
- Train Text Classification Models Using spaCy


# 4. Tokenization
## A Minimal Tokenizer
## Hugging Face Tokenizers
- Subword Tokenization
## Building Your Own Tokenizer

# 5. Embeddings: How Machines “Understand” Words
## Understanding Versus Reading Text
## Word Vectors
- Word2Vec
- Embeddings in the Age of Transfer Learning
## Embeddings in Practice
- Preprocessing
- Model
- Training
- Validation
## Embedding Things That Aren’t Words
- Making Vectorized Music
- Some General Tips for Making Custom Embeddings

# 6. Recurrent Neural Networks and Other Sequence Models
## Recurrent Neural Networks
- RNNs in PyTorch from Scratch
- Bidirectional RNN
- Sequence to Sequence Using RNNs
## Long Short-Term Memory
## Gated Recurrent Units

# 7. Transformers
## Building a Transformer from Scratch
## Attention Mechanisms
- Dot Product Attention
- Scaled Dot Product Attention
- Multi-Head Self-Attention
- Adaptive Attention Span
- Persistent Memory/All-Attention
- Product-Key Memory
## Transformers for Computer Vision

# 8. BERTology: Putting It All Together
## ImageNet
- The Power of Pretrained Models
## The Path to NLP’s ImageNet Moment
## Pretrained Word Embeddings
- The Limitations of One-Hot Encoding
- Word2Vec
- GloVe
- fastText
- Context-Aware Pretrained Word Embeddings
## Sequential Models
- Sequential Data and the Importance of Sequential Models
## RNNs
- Vanilla RNNs
- LSTM Networks
- GRUs
## Attention Mechanisms
## Transformers
- Transformer-XL
## NLP’s ImageNet Moment
- Universal Language Model Fine-Tuning
- ELMo
- BERT
- BERTology
- GPT-1, GPT-2, GPT-3


# 9. Tools of the Trade
## Deep Learning Frameworks
- PyTorch
- TensorFlow
- Jax
- Julia
## Visualization and Experiment Tracking
- TensorBoard
- Weights & Biases
- Neptune
- Comet
- MLflow
## AutoML
- H2O.ai
- Dataiku
- DataRobot
## ML Infrastructure and Compute
- Paperspace
- FloydHub
- Google Colab
- Kaggle Kernels
- Lambda GPU Cloud
## Edge/On-Device Inference
- ONNX
- Core ML
- Edge Accelerators
## Cloud Inference and Machine Learning as a Service
- AWS
- Microsoft Azure
- Google Cloud Platform
## Continuous Integration and Delivery

# 10. Visualization
## Our First Streamlit App
- Build the Streamlit App
- Deploy the Streamlit App
- Explore the Streamlit Web App
- Build and Deploy a Streamlit App for Custom NER
- Build and Deploy a Streamlit App for Text Classification on 
  - AG News Dataset
- Build and Deploy a Streamlit App for Text Classification on 
- Custom Text

# 11. Productionization
## Data Scientists, Engineers, and Analysts
- Prototyping, Deployment, and Maintenance
- Notebooks and Scripts
## Databricks: Your Unified Data Analytics Platform
- Support for Big Data
- Support for Multiple Programming Languages
- Support for ML Frameworks
- Support for Model Repository, Access Control, 
- Data Lineage, and Versioning
## Databricks Setup
- Set Up Access to S3 Bucket
- Set Up Libraries
- Create Cluster
- Create Notebook
- Enable Init Script and Restart Cluster
- Run Speed Test: Inference on NER Using spaCy
## Machine Learning Jobs
- Production Pipeline Notebook
- Scheduled Machine Learning Jobs
- Event-Driven Machine Learning Pipeline
## MLflow
- Log and Register Model
- MLflow Model Serving
## Alternatives to Databricks
- Amazon SageMaker
- Saturn Cloud

# 12. Conclusion
## Ten Final Lessons
- Lesson 1: Start with Simple Approaches First/先从简单的方法入手
- Lesson 2: Leverage the Community/利用社区资源
- Lesson 3: Do Not Create from Scratch, When Possible/尽可能避免从零开始
- Lesson 4: Intuition and Experience Trounces Theory/直觉和经验胜过理论
- Lesson 5: Fight Decision Fatigue/克服决策疲劳
- Lesson 6: Data Is King/数据为王
- Lesson 7: Lean on Humans/依靠人
- Lesson 8: Pair Yourself with Really Great Engineers/与优秀的工程师合作
- Lesson 9: Ensemble/集成学习
- Lesson 10: Have Fun/享受过程

## Final Word

# A. Scaling
- Multi-GPU Training
- Distributed Training
- What Makes Deep Training Fast?
# B. CUDA
- Threads and Thread Blocks
- Writing CUDA Kernels
- CUDA in Practice

# See Also

tools
- spaCy
- [fastai](https://github.com/fastai/fastai)
- Hugging Face
- [Prodigy](https://prodi.gy/): not free
- Streamlit
  - [spacy-streamlit](https://github.com/explosion/spacy-streamlit)
  - [pyngrok](https://github.com/alexdlaird/pyngrok): pyngrok is a Python wrapper for ngrok that manages its own binary, making ngrok available via a convenient Python API and the command line. ngrok is a reverse proxy that opens secure tunnels from public URLs to localhost.
- Databricks: the unified data analytics platform
- visualization and experiment tracking
  - TensorBoard
  - [Weights & Biases](https://github.com/wandb/wandb): The AI developer platform. Use Weights & Biases to train and fine-tune models, and manage models from experimentation to production.
  - [Neptune](https://docs.neptune.ai/): Following its acquisition by OpenAI, Neptune services will be permanently discontinued. - March 5, 2026.
  - [Comet](https://www.comet.com/): An End-to-End Model Evaluation Platform.
  - MLflow: a free open source technology to track machine learning experiments, register models, and deploy models.
- AutoML
  - H2O.ai: since 2012
  - Dataiku: since 2013
  - DataRobot: since 2012
- ML infrastructure
  - Paperspace: since 2014
  - FloydHub
  - Google Colab
  - Kaggle Kernels
  - Lambda Labs
- Edge/On-Device Inference
  - ONNX: Open Neural Network Exchange
  - Core ML
  - Edge accelerators: Intel Movidius compute stick, Google Edge TPU, Nvidia Jetson
- Cloud Inference
  - AWS
  - Azure
  - GCP
- CI/CD
  - GitHub Actions

datasets
- the WikiText-103 dataset
- the AG News Classification Dataset - https://www.kaggle.com/datasets/amananandrai/ag-news-classification-dataset