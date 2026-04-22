# Designing Large Language Model Applications

- I. LLM Ingredients: 1-4
- II. Utilizing LLMs: 5-9
- III. LLM Application Paradigms: 10-13

# 1. Introduction
## Defining LLMs
## A Brief History of LLMs
### Early Years
### The Modern LLM Era
## The Impact of LLMs
## LLM Usage in the Enterprise
## Prompting
### Zero-Shot Prompting
### Few-Shot Prompting
### Chain-of-Thought Prompting
### Prompt Chaining
### Adversarial Prompting
## Accessing LLMs Through an API
## Strengths and Limitations of LLMs
## Building Your First Chatbot Prototype
## From Prototype to Production

# 2. Pre-Training Data
## Ingredients of an LLM
## Pre-Training Data Requirements
## Popular Pre-Training Datasets
## Synthetic Pre-Training Data
## Training Data Preprocessing
## Data Filtering and Cleaning
### Selecting Quality Documents
### Deduplication
### Removing Personally Identifiable Information
### Training Set Decontamination
### Data Mixtures
## Effect of Pre-Training Data on Downstream Tasks
## Bias and Fairness Issues in Pre-Training Datasets

# 3. Vocabulary and Tokenization
## Vocabulary
## Tokenizers
## Tokenization Pipeline
### Normalization
### Pre-Tokenization
### Tokenization
### Byte Pair Encoding
### WordPiece
### Special Tokens

# 4. Architectures and Learning Objectives
## Preliminaries
## Representing Meaning
## The Transformer Architecture
### Self-Attention
### Positional Encoding
### Feedforward Networks
### Layer Normalization

## Loss Functions
## Intrinsic Model Evaluation

## Transformer Backbones
### Encoder-Only Architectures
### Encoder-Decoder Architectures
### Decoder-Only Architectures
### Mixture of Experts

## Learning Objectives
### Full Language Modeling
### Prefix Language Modeling
### Masked Language Modeling
### Which Learning Objectives Are Better?

## Pre-Training Models


# 5. Adapting LLMs to Your Use Case
## Navigating the LLM Landscape
### Who Are the LLM providers?
### Model Flavors
### Open Source LLMs

## How to Choose an LLM for Your Task
### Open Source Versus Proprietary LLMs
### LLM Evaluation

## Loading LLMs
### Hugging Face Accelerate
### Ollama
### LLM Inference APIs

## Decoding Strategies
### Greedy Decoding
### Beam Search
### Top-k Sampling
### Top-p Sampling

## Running Inference on LLMs
## Structured Outputs
## Model Debugging and Interpretability

# 6. Fine-Tuning
## The Need for Fine-Tuning

## Fine-Tuning: A Full Example
### Learning Algorithms Parameters
### Memory Optimization Parameters
### Regularization Parameters
### Batch Size
### Parameter-Efficient Fine-Tuning
### Working with Reduced Precision
### Putting It All Together

## Fine-Tuning Datasets
### Utilizing Publicly Available Instruction-Tuning Datasets
### LLM-Generated Instruction-Tuning Datasets

# 7. Advanced Fine-Tuning Techniques
## Continual Pre-Training
### Replay (Memory)
### Parameter Expansion

## Parameter-Efficient Fine-Tuning
### Adding New Parameters
### Subset Methods

## Combining Multiple Models
### Model Ensembling
### Model Fusion
### Adapter Merging

# 8. Alignment Training and Reasoning
## Defining Alignment Training

## Reinforcement Learning
### Types of Human Feedback
### RLHF Example

## Hallucinations

## Mitigating Hallucinations
### Self-Consistency
### Chain-of-Actions
### Recitation
### Sampling Methods for Addressing Hallucination
### Decoding by Contrasting Layers

## In-Context Hallucinations

## Hallucinations Due to Irrelevant Information

## Reasoning
### Deductive Reasoning
### Inductive Reasoning
### Abductive Reasoning
### Common Sense Reasoning

## Inducing Reasoning in LLMs
### Verifiers for Improving Reasoning
### Inference-Time Computation
### Fine-Tuning for Reasoning

# 9. Inference Optimization
## LLM Inference Challenges
## Inference Optimization Techniques

## Techniques for Reducing Compute
### K-V Caching
### Early Exit
### Knowledge Distillation

## Techniques for Accelerating Decoding
### Speculative Decoding
### Parallel Decoding

## Techniques for Reducing Storage Needs
### Symmetric Quantization
### Asymmetric Quantization


# 10. Interfacing LLMs with External Tools
## LLM Interaction Paradigms
### Passive Approach
### The Explicit Approach
### The Autonomous Approach

## Defining Agents

## Agentic Workflow

## Components of an Agentic System
### Models
### Tools
### Data Stores
### Agent Loop Prompt
### Guardrails and Verifiers
### Agent Orchestration Software

# 11. Representation Learning and Embeddings
## Introduction to Embeddings
## Semantic Search
## Similarity Measures

## Fine-Tuning Embedding Models
### Base Models
### Training Dataset
### Loss Functions

## Instruction Embeddings

## Optimizing Embedding Size
### Matryoshka Embeddings
### Binary and Integer Embeddings
### Product Quantization

## Chunking
### Sliding Window Chunking
### Metadata-Aware Chunking
### Layout-Aware Chunking
### Semantic Chunking
### Late Chunking

## Vector Databases

## Interpreting Embeddings

# 12. Retrieval-Augmented Generation
## The Need for RAG
## Typical RAG Scenarios
## Deciding When to Retrieve

## The RAG Pipeline
### Rewrite
### Retrieve
### Rerank
### Refine
### Insert
### Generate

## RAG for Memory Management
## RAG for Selecting In-Context Training Examples
## RAG for Model Training
## Limitations of RAG
## RAG Versus Long Context
## RAG Versus Fine-Tuning

# 13. Design Patterns and System Architecture
## Multi-LLM Architectures
### LLM Cascades
### Routers
### Task-Specialized LLMs

## Programming Paradigms
### DSPy
### LMQL
