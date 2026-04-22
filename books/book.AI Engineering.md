# AI Engineering: Building Applications with Foundation Models

> TODO: 某个领域的咨询机器人.

# 1. Introduction to Building AI Applications with Foundation Models/使用基础模型构建AI应用介绍
## The Rise of AI Engineering
- From Language Models to Large Language Models
- From Large Language Models to Foundation Models

- From Foundation Models to AI Engineering

tools: AutoGPT, Stable Diffusion eb UI, LangChain, Ollama

## Foundation Model Use Cases
- Coding/编码
- Image and Video Production/图像和视频生成
- Writing/协作
- Education/教育
- Conversational Bots/对话机器人
- Information Aggregation/信息聚合
- Data Organization/数据组织
- Workflow Automation/工作流自动化
## Planning AI Applications
- Use Case Evaluation
- Setting Expectations
- Milestone Planning
- Maintenance
## The AI Engineering Stack
- Three Layers of the AI Stack
  - Application development/应用开发
    - AI interface
    - Prompt Engineering
    - Context construction
    - Evaluation
  - Model development/模型开发
    - Inference optimization
    - Dataset engineering
    - Modeling & training
    - Evaluation
  - Infrastructure/基础设施
    - Compute management
    - Data management
    - Serving
    - Monitoring

- AI Engineering Versus ML Engineering
  - Model adaptation techniques/模型适配技术
    - prompt-based technique
    - finetuning
  - Model development/模型开发
    - Modeling and trainning/训练模型: TensorFlow, Transformers, PyTorch
    - Dataset engineering/数据集工程
    - Inference optimization/推理优化: quantization/量化, distillation/蒸馏, parallelism/并行化
  - Application development/应用开发
    - Evaluation/评估
    - Prompt engineering and context construction/提示工程和上下文构造
    - AI interface/AI界面

- AI Engineering Versus Full-Stack Engineering

# 2. Understanding Foundation Models/理解基础模型

## Training Data/训练数据
[Common Crawl](https://commoncrawl.org/): Common Crawl maintains a free, open repository of web crawl data that can be used by anyone.
[C4](https://arxiv.org/abs/1910.10683v4): Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer

- Multilingual Models
  - Chinese: ChatGLM, YAYI, Llama-Chinese, ...
- Domain-Specific Models

## Modeling/模型训练
- Model Architecture
  - Transformer architecture: 2017-?
  - Seq2seq: 2014-2018
  - GANs(Generative Adversarial Networks): 2014-2019
  - RWKV
  - SSMs(State Space Models)
- Model Size

## Post-Training/后训练
- Supervised Finetuning(SFT)/有监督的微调: 高质量指令数据
- Preference Finetuning/偏好微调: reinforcement learning
  - RLHF: Reinforcement Learning form Human Feedback
  - DPO: Direct Preference Optimization
  - RLAIF: Reinforcement Learning from AI Feedback
## Sampling/采样
- Sampling Fundamentals
- Sampling Strategies
  - Temperature
  - top-k
  - top-p, min-p
- Test Time Compute
- Structured Outputs
- The Probabilistic Nature of AI

# 3. Evaluation Methodology/评估方法论
## Challenges of Evaluating Foundation Models
## Understanding Language Modeling Metrics
- Entropy
- Cross Entropy
- Bits-per-Character and Bits-per-Byte
- Perplexity
- Perplexity Interpretation and Use Cases
## Exact Evaluation
- Functional Correctness
- Similarity Measurements Against Reference Data
- Introduction to Embedding
## AI as a Judge
- Why AI as a Judge?
- How to Use AI as a Judge
- Limitations of AI as a Judge
- What Models Can Act as Judges?
## Ranking Models with Comparative Evaluation
- Challenges of Comparative Evaluation
- The Future of Comparative Evaluation

# 4. Evaluate AI Systems/评估AI系统
## Evaluation Criteria
- Domain-Specific Capability
- Generation Capability
- Instruction-Following Capability
- Cost and Latency
## Model Selection
- Model Selection Workflow
- Model Build Versus Buy
- Navigate Public Benchmarks
## Design Your Evaluation Pipeline
- Step 1. Evaluate All Components in a System
- Step 2. Create an Evaluation Guideline 
- Step 3. Define Evaluation Methods and Data

# 5. Prompt Engineering/提示工程
## Introduction to Prompting
- In-Context Learning: Zero-Shot and Few-Shot
- System Prompt and User Prompt
- Context Length and Context Efficiency
## Prompt Engineering Best Practices
- Write Clear and Explicit Instructions/编写清晰明确的指令
- Provide Sufficient Context/提供充分的背景信息
- Break Complex Tasks into Simpler Subtasks/将复杂任务分解为更简单的子任务
- Give the Model Time to Think/给模型一些思考时间
- Iterate on Your Prompts/不断迭代你的提示
- Evaluate Prompt Engineering Tools/评估提示设计工具
- Organize and Version Prompts/整理并版本化提示
## Defensive Prompt Engineering/防御性提示工程
- Proprietary Prompts and Reverse Prompt Engineering
- Jailbreaking and Prompt Injection
- Information Extraction
- Defenses Against Prompt Attacks

# 6. RAG and Agents/检索增强生成和智能体

上下文构造
- RAG: 允许模型从外部数据源检索相关信息
- Agent: 允许模型使用工具(如Web搜索和API)收集信息

## RAG
- RAG Architecture
- Retrieval Algorithms
  - term-based retrieval
  - embedding-based retrieval
  - hybrid search
- Retrieval Optimization
  - chunking strategy/分块策略
  - reranking/重排序
  - query rewriting/查询重写
  - contextual retrieval/上下文检索
- RAG Beyond Texts
## Agents
- Agent Overview
- Tools/工具
- Planning/规划
- Agent Failure Modes and Evaluation
## Memory

memory refers to mechanisms that allow a model to retain and utilize information.

# 7. Finetuning/微调
## Finetuning Overview
## When to Finetune
- Reasons to Finetune
- Reasons Not to Finetune
- Finetuning and RAG
## Memory Bottlenecks
- Backpropagation and Trainable Parameters
- Memory Math
- Numerical Representations
- Quantization
## Finetuning Techniques
- Parameter-Efficient Finetuning
- Model Merging and Multi-Task Finetuning
- Finetuning Tactics

# TODO 8. Dataset Engineering/数据集工程
## Data Curation/数据整理
- Data Quality
- Data Coverage
- Data Quantity
- Data Acquisition and Annotation
## Data Augmentation and Synthesis/数据增强和合成
- Why Data Synthesis
- Traditional Data Synthesis Techniques
- AI-Powered Data Synthesis
- Model Distillation
## Data Processing/数据处理
- Inspect Data
- Deduplicate Data
- Clean and Filter Data
- Format Data

# 9. Inference Optimization/推理优化
## Understanding Inference Optimization
- Inference Overview
- Inference Performance Metrics
- AI Accelerators
## Inference Optimization
- Model Optimization/模型优化
  - Model compression
  - Overcomming the autoregressive decoding bottleneck
    - speculative decoding
    - Inference with reference
    - Parallel decoding
  - Attention mechanism optimization
    - Redesigning the attention mechanism
    - Optimizing the KV cache size
    - Writing kernels for attention computation
- Inference Service Optimization/推理服务优化
  - Batching
  - Decoupling prefill and decode: prefill is compute-bound, decode is memory bandwidth-bound
  - Prompt caching
  - Parallelism

# 10. AI Engineering Architecture and User Feedback/AI工程架构和用户反馈
## AI Engineering Architecture
- Step 0. Simplest form
  - Model API: Generation
- Step 1. Enhance Context/增强上下文
  - Context construction
  - Read-only actions
  - Databases
- Step 2. Put in Guardrails/放在护栏中
  - Input guardrails
  - Output guardrails
  - Scoring
- Step 3. Add Model Router and Gateway/添加模型路由和网关
  - Model gateway: Routing
- Step 4. Reduce Latency with Caches/使用缓存减少延迟
  - Cache: exact caching, semantic caching
- Step 5. Add Agent Patterns/添加智能体模式
  - Write actions
- Monitoring and Observability/监控和可观测性
- AI Pipeline Orchestration/AI流水线编排
  - Components definition
  - Chaining
  - tools: LangChain, LlamaIndex, Flowise, Langflow, Haystack

![](https://raw.githubusercontent.com/chiphuyen/aie-book/refs/heads/main/assets/aie-architecture.png)

## User Feedback
- Extracting Conversational Feedback
- Feedback Design
- Feedback Limitations

# See Also
* [LLM Leaderboard](https://llm-stats.com/leaderboards/llm-leaderboard)