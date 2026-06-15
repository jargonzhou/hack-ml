# Natural Language Processing with Transformers: Building Language Applications with Hugging Face


# 1. Hello Transformers
- The Encoder-Decoder Framework/编码器-解码器框架
- Attention Mechanisms/注意力机制
- Transfer Learning in NLP/NLP中的迁移学习
- Hugging Face Transformers: Bridging the Gap
- A Tour of Transformer Applications
  - Text Classification
  - Named Entity Recognition
  - Question Answering
  - Summarization
  - Translation
  - Text Generation
- The Hugging Face Ecosystem
  - The Hugging Face Hub
  - Hugging Face Tokenizers
  - Hugging Face Datasets
  - Hugging Face Accelerate
- Main Challenges with Transformers

# 2. Text Classification/文本分类
- The Dataset
  - A First Look at Hugging Face Datasets
  - From Datasets to DataFrames
  - Looking at the Class Distribution
  - How Long Are Our Tweets?
- From Text to Tokens
  - Character Tokenization
  - Word Tokenization
  - Subword Tokenization
  - Tokenizing the Whole Dataset
- Training a Text Classifier
  - Transformers as Feature Extractors
  - Fine-Tuning Transformers

# 3. Transformer Anatomy/Transformer剖析
- The Transformer Architecture
- The Encoder
  - Self-Attention
  - The Feed-Forward Layer
  - Adding Layer Normalization
  - Positional Embeddings
  - Adding a Classification Head
- The Decoder
- Meet the Transformers
  - The Transformer Tree of Life
  - The Encoder Branch
  - The Decoder Branch
  - The Encoder-Decoder Branch

# 4. Multilingual Named Entity Recognition/多语种命名实体识别
- The Dataset
- Multilingual Transformers
- A Closer Look at Tokenization
  - The Tokenizer Pipeline
  - The SentencePiece Tokenizer
- Transformers for Named Entity Recognition
- The Anatomy of the Transformers Model Class
  - Bodies and Heads
  - Creating a Custom Model for Token Classification
  - Loading a Custom Model
- Tokenizing Texts for NER
- Performance Measures
- Fine-Tuning XLM-RoBERTa
- Error Analysis
- Cross-Lingual Transfer
  - When Does Zero-Shot Transfer Make Sense?
  - Fine-Tuning on Multiple Languages at Once
- Interacting with Model Widgets

# 5. Text Generation/文本生成
- The Challenge with Generating Coherent Text
- Greedy Search Decoding
- Beam Search Decoding
- Sampling Methods
- Top-k and Nucleus Sampling
- Which Decoding Method Is Best?

# 6. Summarization/摘要
- The CNN/DailyMail Dataset
- Text Summarization Pipelines
  - Summarization Baseline
  - GPT-2
  - T5
  - BART
  - PEGASUS
- Comparing Different Summaries
- Measuring the Quality of Generated Text
  - BLEU
  - ROUGE
- Evaluating PEGASUS on the CNN/DailyMail Dataset
- Training a Summarization Model
  - Evaluating PEGASUS on SAMSum
  - Fine-Tuning PEGASUS
  - Generating Dialogue Summaries

# 7. Question Answering/问答
- Building a Review-Based QA System
  - The Dataset
  - Extracting Answers from Text
  - Using Haystack to Build a QA Pipeline
- Improving Our QA Pipeline
  - Evaluating the Retriever
  - Evaluating the Reader
  - Domain Adaptation
  - Evaluating the Whole QA Pipeline
- Going Beyond Extractive QA

# 8. Making Transformers Efficient in Production/提升生产环境中效率
- Intent Detection as a Case Study
- Creating a Performance Benchmark
- Making Models Smaller via Knowledge Distillation
  - Knowledge Distillation for Fine-Tuning
  - Knowledge Distillation for Pretraining
  - Creating a Knowledge Distillation Trainer
  - Choosing a Good Student Initialization
  - Finding Good Hyperparameters with Optuna
  - Benchmarking Our Distilled Model
- Making Models Faster with Quantization
- Benchmarking Our Quantized Model
- Optimizing Inference with ONNX and the ONNX Runtime
- Making Models Sparser with Weight Pruning
  - Sparsity in Deep Neural Networks
  - Weight Pruning Methods

# 9. Dealing with Few to No Labels/处理标签少和无标签的情况
- Building a GitHub Issues Tagger
  - Getting the Data
  - Preparing the Data
  - Creating Training Sets
  - Creating Training Slices
- Implementing a Naive Bayesline
- Working with No Labeled Data
- Working with a Few Labels
  - Data Augmentation
  - Using Embeddings as a Lookup Table
  - Fine-Tuning a Vanilla Transformer
  - In-Context and Few-Shot Learning with Prompts
- Leveraging Unlabeled Data
  - Fine-Tuning a Language Model
  - Fine-Tuning a Classifier
  - Advanced Methods

# 10. Training Transformers from Scratch/从零开始训练Transformer
- Large Datasets and Where to Find Them
  - Challenges of Building a Large-Scale Corpus
  - Building a Custom Code Dataset
  - Working with Large Datasets
  - Adding Datasets to the Hugging Face Hub
- Building a Tokenizer
  - The Tokenizer Model
  - Measuring Tokenizer Performance
  - A Tokenizer for Python
  - Training a Tokenizer
  - Saving a Custom Tokenizer on the Hub
- Training a Model from Scratch
  - A Tale of Pretraining Objectives
  - Initializing the Model
  - Implementing the Dataloader
  - Defining the Training Loop
  - The Training Run
- Results and Analysis

# 11. Future Directions/未来的方向
- Scaling Transformers
  - Scaling Laws
  - Challenges with Scaling
  - Attention Please!
  - Sparse Attention
  - Linearized Attention
- Going Beyond Text
  - Vision
  - Tables
- Multimodal Transformers
  - Speech-to-Text
  - Vision and Text
- Where to from Here?

# See Also

