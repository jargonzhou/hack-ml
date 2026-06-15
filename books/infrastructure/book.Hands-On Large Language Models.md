# Hands-On Large Language Models: Language Understanding and Generation/大型语言模型实战：语言理解与生成

- I. Understanding Language Models/理解语言模型: 1-3
  - answering the question: how do large langauge model work?
- II. Using Pretrained Language Models/使用预训练语言模型: 4-9
  - using large language models across a variety of use cases.
- III. Training and Fine-Tuning Language Models/训练和微调语言模型: 10-12
  - exploring the mutifaceted components of training and fine-tuning different types of large language models.

```shell
$ hf cache list
ID                           SIZE LAST_ACCESSED LAST_MODIFIED REFS
--------------------------- ----- ------------- ------------- ----
model/google/gemma-4-E4B-it 16.0G 3 hours ago   3 hours ago   main

Found 1 repo(s) for a total of 1 revision(s) and 16.0G on disk.
```

# 1. An Introduction to Large Language Models/大语言模型导论

- What Is Language AI?/什么是语言人工智能？
- A Recent History of Language AI/语言人工智能的近期历史
	- Representing Language as a Bag-of-Words/将语言表示为词袋模型
	- Better Representations with Dense Vector Embeddings/利用稠密向量嵌入获得更好的表示
	- Types of Embeddings/嵌入的类型
	- Encoding and Decoding Context with Attention/利用注意力机制对上下文进行编码与解码
	- Attention Is All You Need/注意力就是你所需要的一切
	- **Representation Models**: Encoder-Only Models/表示模型：纯编码器模型
	- **Generative Models**: Decoder-Only Models/生成模型：纯解码器模型
	- The Year of Generative AI/生成式人工智能之年
- The Moving Definition of a “Large Language Model”/“大语言模型”不断演变的定义
	
- The Training Paradigm of Large Language Models/大语言模型的训练范式
- Large Language Model Applications: What Makes Them So Useful?/大语言模型应用：是什么让它们如此有用？
- Responsible LLM Development and Usage/负责任的大语言模型开发与使用
- Limited Resources Are All You Need/有限的资源就是你所需要的一切
- Interfacing with Large Language Models/与大语言模型进行交互
	- Proprietary, Private Models/专有且私有的模型
	- Open Models/开放模型
	- Open Source Frameworks/开源框架
- Generating Your First Text/生成你的第一段文本

# 2. Tokens and Embeddings/Token与嵌入

- LLM Tokenization/大语言模型的Token化
	- How Tokenizers Prepare the Inputs to the Language Model/Tokenizer如何准备语言模型的输入
	- Downloading and Running an LLM/下载并运行大语言模型
	- How Does the Tokenizer Break Down Text?/Tokenizer如何拆分文本？
	- Word Versus Subword Versus Character Versus Byte Tokens/单词、子词、字符与字节Token的对比
	- Comparing Trained LLM Tokenizers/对比已训练的大语言模型Tokenizer
	- Tokenizer Properties/Tokenizer的属性
- Token Embeddings/Token嵌入
	- A Language Model Holds Embeddings for the Vocabulary of Its Tokenizer/语言模型包含其Tokenizer词表对应的嵌入
	- Creating Contextualized Word Embeddings with Language Models/利用语言模型创建上下文相关的词嵌入
- Text Embeddings (for Sentences and Whole Documents)/文本嵌入（适用于句子与整篇文档）
- Word Embeddings Beyond LLMs/大语言模型之外的词嵌入
	- Using pretrained Word Embeddings/使用预训练的词嵌入
	- The Word2vec Algorithm and Contrastive Training/Word2vec算法与对比训练
- Embeddings for Recommendation Systems/推荐系统中的嵌入
	- Recommending Songs by Embeddings/通过嵌入推荐歌曲
	- Training a Song Embedding Model/训练歌曲嵌入模型

# 3. Looking Inside Large Language Models/探秘大语言模型内部

- An Overview of Transformer Models/Transformer模型概述
	- The Inputs and Outputs of a Trained Transformer LLM/已训练的Transformer大语言模型的输入与输出
	- The Components of the Forward Pass/前向传播的组成部分
	- Choosing a Single Token from the Probability Distribution (Sampling/Decoding)/从概率分布中选择单个Token（采样/解码）
	- Parallel Token Processing and Context Size/Token并行处理与上下文窗口大小
	- Speeding Up Generation by Caching Keys and Values/通过缓存Key与Value提升生成速度
	- Inside the Transformer Block/Transformer块内部结构
- Recent Improvements to the Transformer Architecture/Transformer架构的近期改进
	- More Efficient Attention/更高效的注意力机制
	- The Transformer Block/Transformer块
	- Positional Embeddings (RoPE)/位置嵌入（旋转位置嵌入）
	- Other Architectural Experiments and Improvements/其他架构实验与改进

# 4. Text Classification/文本分类

- The Sentiment of Movie Reviews/电影评论的情感分析
- Text Classification with Representation Models/利用表示模型进行文本分类
- Model Selection/模型选择
- Using a Task-Specific Model/使用任务特定模型
- Classification Tasks That Leverage Embeddings/利用嵌入的分类任务
	- Supervised Classification/监督分类
	- What If We Do Not Have Labeled Data?/如果我们没有标签数据该怎么办？
- Text Classification with Generative Models/利用生成模型进行文本分类
	- Using the Text-to-Text Transfer Transformer/使用文本到文本传输Transformer（T5等）
	- ChatGPT for Classification/利用ChatGPT进行分类

# 5. Text Clustering and Topic Modeling/文本聚类与主题建模

- ArXiv’s Articles: Computation and Language/ArXiv文章：计算与语言
- A Common Pipeline for Text Clustering/文本聚类的通用流水线
	- Embedding Documents/文档嵌入
	- Reducing the Dimensionality of Embeddings/降低嵌入的维度
	- Cluster the Reduced Embeddings/对降维后的嵌入进行聚类
	- Inspecting the Clusters/检查聚类结果
- From Text Clustering to Topic Modeling/从文本聚类到主题建模
	- BERTopic: A Modular Topic Modeling Framework/BERTopic：模块化主题建模框架
	- Adding a Special Lego Block/添加一个特殊的积木块
	- The Text Generation Lego Block/文本生成积木块

# 6. Prompt Engineering/提示词工程

- Using Text Generation Models/使用文本生成模型
	- Choosing a Text Generation Model/选择文本生成模型
	- Loading a Text Generation Model/加载文本生成模型
	- Controlling Model Output/控制模型输出
- Intro to Prompt Engineering/提示词工程简介
	- The Basic Ingredients of a Prompt/提示词的基本要素
	- Instruction-Based Prompting/基于指令的提示
- Advanced Prompt Engineering/高级提示词工程
	- The Potential Complexity of a Prompt/提示词的潜在复杂性
	- In-Context Learning: Providing Examples/上下文学习：提供示例
	- Chain Prompting: Breaking up the Problem/链式提示：拆解问题
- Reasoning with Generative Models/利用生成模型进行推理
	- Chain-of-Thought: Think Before Answering/思维链：作答前先思考
	- Self-Consistency: Sampling Outputs/自我一致性：对输出进行采样
	- Tree-of-Thought: Exploring Intermediate Steps/思维树：探索中间步骤
- Output Verification/输出验证
	- Providing Examples/提供示例
	- Grammar: Constrained Sampling/语法：受约束的采样

# 7. Advanced Text Generation Techniques and Tools/高级文本生成技术与工具

- Model I/O: Loading Quantized Models with LangChain/模型输入/输出：利用LangChain加载量化模型
- Chains: Extending the Capabilities of LLMs/链：扩展大语言模型的能力
	- A Single Link in the Chain: Prompt Template/链中的单个环节：提示词模板
	- A Chain with Multiple Prompts/包含多个提示词的链
- Memory: Helping LLMs to Remember Conversations/记忆：帮助大语言模型记住对话
	- Conversation Buffer/对话缓冲区
	- Windowed Conversation Buffer/窗口化对话缓冲区
	- Conversation Summary/对话摘要
- Agents: Creating a System of LLMs/智能体：构建大语言模型系统
	- The Driving Power Behind Agents: Step-by-step Reasoning/智能体背后的核心驱动力：分步推理
	- ReAct in LangChain/LangChain中的ReAct模式

# 8. Semantic Search and Retrieval-Augmented Generation/语义搜索与检索增强生成

- Overview of Semantic Search and RAG/语义搜索与RAG概述
- Semantic Search with Language Models/利用语言模型进行语义搜索
	- Dense Retrieval/稠密检索
	- Reranking/重排序
	- Retrieval Evaluation Metrics/检索评估指标
- Retrieval-Augmented Generation (RAG)/检索增强生成（RAG）
	- From Search to RAG/从搜索到RAG
	- Example: Grounded Generation with an LLM API/示例：利用大语言模型API进行有依据的生成
	- Example: RAG with Local Models/示例：利用本地模型运行RAG
	- Advanced RAG Techniques/高级RAG技术
	- RAG Evaluation/RAG评估

# 9. Multimodal Large Language Models/多模态大语言模型

- Transformers for Vision/适用于计算机视觉的Transformer
- Multimodal Embedding Models/多模态嵌入模型
	- CLIP: Connecting Text and Images/CLIP：连接文本与图像
	- How Can CLIP Generate Multimodal Embeddings?/CLIP如何生成多模态嵌入？
	- OpenCLIP/OpenCLIP框架
- Making Text Generation Models Multimodal/让文本生成模型具备多模态能力
	- BLIP-2: Bridging the Modality Gap/BLIP-2：弥合模态间隙
	- Preprocessing Multimodal Inputs/预处理多模态输入
	- Use Case 1: Image Captioning/使用场景1：图像描述生成
	- Use Case 2: Multimodal Chat-Based Prompting/使用场景2：基于多模态对话的提示

# 10. Creating Text Embedding Models/构建文本嵌入模型

- Embedding Models/嵌入模型
- What Is Contrastive Learning?/什么是对比学习？
- SBERT/SBERT模型
- Creating an Embedding Model/构建一个嵌入模型
	- Generating Contrastive Examples/生成对比示例
	- Train Model/训练模型
	- In-Depth Evaluation/深度评估
	- Loss Functions/损失函数
- Fine-Tuning an Embedding Model/微调嵌入模型
	- Supervised/有监督微调
	- Augmented SBERT/增强型SBERT
- Unsupervised Learning/无监督学习
	- Transformer-Based Sequential Denoising Auto-Encoder/基于Transformer的序列去噪自编码器（TSDAE）
	- Using TSDAE for Domain Adaptation/利用TSDAE进行领域自适应

# 11. Fine-Tuning Representation Models for Classification/微调表示模型以用于分类任务

- Supervised Classification/监督分类
	- Fine-Tuning a Pretrained BERT Model/微调预训练的BERT模型
	- Freezing Layers/冻结模型层
- Few-Shot Classification/少样本分类
	- SetFit: Efficient Fine-Tuning with Few Training Examples/SetFit：利用极少训练示例的高效微调
	- Fine-Tuning for Few-Shot Classification/针对少样本分类进行微调
- Continued Pretraining with Masked Language Modeling/利用掩码语言建模进行持续预训练
- Named-Entity Recognition/命名实体识别
	- Preparing Data for Named-Entity Recognition/为命名实体识别准备数据
	- Fine-Tuning for Named-Entity Recognition/针对命名实体识别进行微调

# 12. Fine-Tuning Generation Models/微调生成模型

- The Three LLM Training Steps: Pretraining, Supervised Fine-Tuning, and Preference Tuning/大语言模型训练的三大步骤：预训练、有监督微调与偏好对齐微调
- Supervised Fine-Tuning (SFT)/有监督微调（SFT）
	- Full Fine-Tuning/全量微调
	- Parameter-Efficient Fine-Tuning (PEFT)/参数高效微调（PEFT）
- Instruction Tuning with QLoRA/利用QLoRA进行指令微调
	- Templating Instruction Data/制作指令数据模板
	- Model Quantization/模型量化
	- LoRA Configuration/LoRA配置
	- Training Configuration/训练配置
	- Training/训练阶段
	- Merge Weights/合并权重
- Evaluating Generative Models/评估生成模型
	- Word-Level Metrics/词级评估指标
	- Benchmarks/基准测试
	- Leaderboards/排行榜
	- Automated Evaluation/自动化评估
	- Human Evaluation/人工评估
- Preference-Tuning/Alignment/RLHF/偏好微调/对齐/基于人类反馈的强化学习
- Automating Preference Evaluation Using Reward Models/利用奖励模型自动化偏好评估
	- The Inputs and Outputs of a Reward Model/奖励模型的输入与输出
	- Training a Reward Model/训练奖励模型
	- Training No Reward Model/不使用奖励模型的训练方法
- Preference Tuning with DPO/利用直接偏好优化（DPO）进行偏好微调
	- Templating Alignment Data/制作对齐数据模板
	- Model Quantization/模型量化
	- Training Configuration/训练配置
	- Training/训练阶段

# See Also
* Tomas Mikolov et al. **Efficient estimation of word representations in vector space**. arXiv preprint arXiv:1301.3781 (2013).
* Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Bengio. **Neural machine translation by jointly learning to align and translate**. arXiv preprint arXiv:1409.0473 (2014). - attention
* Ashish Vaswani et al. **Attention is all you need**. Advances in Neural Information Processing Systems 30 (2017). - Transformer
* Designing Large Language Model Applications - https://www.oreilly.com/library/view/designing-large-language/9781098150495/
* Natural Language Processing with Transformers, Revised Edition
* The word2vec algorithm
  * [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781)
  * [The Illustrated Word2vec](https://jalammar.github.io/illustrated-word2vec/)
* noise-contrastive estimation: detect positive examples from randomly generated examples - https://proceedings.mlr.press/v9/gutmann10a/gutmann10a.pdf

tools
- Google Colab
- OpenAI
- Cohere
- Hugging Face

models
- representation models
  - BERT
- generative models
  - GPT
- Mamba - Albert Gu and Tri Dao. **Mamba: Linear-time sequence modeling with selective state spaces**. arXiv preprint arXiv:2312.00752 (2023).
- RWKV - Bo Peng et al. **RWKV: Reinventing RNNs for the transformer era**. arXiv preprint arXiv:2305.13048 (2023).
- Llama 2 - Hugo Touvron et al. **Llama 2: Open foundation and fine-tuned chat models**. arXiv preprint arXiv:2307.09288 (2023).
- Phi-3-mini - Marah Abdin et al. **Phi-3 technical report: A highly capable language model locally on your phone**. arXiv preprint arXiv:2404.14219 (2024).
- DeBERTa v3 - microsoft/deberta-v3-xsmall: with tokenizer microsoft/deberta-base

tokenizers
- https://huggingface.co/google-bert/bert-base-uncased - WordPiece
- https://huggingface.co/google-bert/bert-base-cased - WordPiece
- https://huggingface.co/openai-community/gpt2 - Byte pair encoding (BPE)
- https://huggingface.co/google/flan-t5-xxl - SentencePiece
- GPT-4 - Byte pair encoding (BPE)
- https://huggingface.co/bigcode/starcoder2-15b - Byte pair encoding (BPE)
- https://huggingface.co/facebook/galactica-1.3b - Byte pair encoding (BPE)
- https://huggingface.co/microsoft/Phi-3-mini-4k-instruct - Byte pair encoding (BPE)
- see also: https://huggingface.co/docs/transformers/tokenizer_summary

embeddings
- token embeddings
- contextualized word embeddings
  - microsoft/deberta-base
- text embeddings
  - sentence-transformers/all-mpnet-base-v2
- word embeddings
  - Gensim library: word2vec, GloVe - https://radimrehurek.com/gensim/
    - glove-wiki-gigaword-50


datasets
* Playlist Dataset: This datasets are collected by Shuo Chen from Dept. of Computer Science, Cornell University. - https://www.cs.cornell.edu/~shuochen/lme/data_page.html

## Bonus Material
* https://github.com/HandsOnLLM/Hands-On-Large-Language-Models/tree/main/bonus

1. [**Hands-On Large Language Models**](https://www.amazon.com/Hands-Large-Language-Models-Understanding/dp/1098150961)
2. [How **Transformer LLMs** Work](https://www.deeplearning.ai/short-courses/how-transformer-llms-work/?utm_campaign=handsonllm-launch&utm_medium=partner)
3. [A Visual Guide to **Quantization**](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization)
4. [A Visual Guide to **Mamba and State Space Models**](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mamba-and-state)
5. [A Visual Guide to **Mixture of Experts** (MoE)](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts)
6. [The Illustrated **Stable Diffusion**](https://jalammar.github.io/illustrated-stable-diffusion/)
7. [A Visual Guide to **Reasoning LLMs**](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-reasoning-llms)
8. [The Illustrated **DeepSeek-R1**](https://newsletter.languagemodels.co/p/the-illustrated-deepseek-r1)
9. [A Visual Guide to **LLM Agents**](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-llm-agents)

