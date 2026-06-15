# Terminology of Machine Learning

# Activation function/激活函数
* https://en.wikipedia.org/wiki/Activation_function

In artificial neural networks, the activation function of a node is **a function that calculates the output of the node based on its individual inputs and their weights**. Nontrivial problems can be solved using only a few nodes if the activation function is nonlinear.

TODO: list activation function and their usage scope

# Agent/智能体
* https://en.wikipedia.org/wiki/Intelligent_agent

In artificial intelligence, an intelligent agent is an entity that perceives its environment, takes actions autonomously to achieve goals, and may improve its performance through machine learning or by acquiring knowledge.

## Agent Skills/智能体技能
* https://agentskills.io/

Agent Skills are a lightweight, open format for extending AI agent capabilities with specialized knowledge and workflows/使用专门的知识和工作流扩展AI智能体能力的一个轻量级开放格式.

# Attention/注意力机制
* https://en.wikipedia.org/wiki/Attention_(machine_learning)

In machine learning, attention is **a method that determines the importance of each component in a sequence relative to the other components in that sequence**. In natural language processing, importance is represented by "soft" weights assigned to each word in a sentence. More generally, attention encodes vectors called token embeddings across a fixed-width sequence that can range from tens to millions of tokens in size.

# Autoencoder/自动编码器
* https://en.wikipedia.org/wiki/Autoencoder
* https://arxiv.org/abs/2003.05991

An autoencoder is a type of artificial neural network used to learn efficient codings of unlabeled data (unsupervised learning). An autoencoder learns two functions: an encoding function that transforms the input data, and a decoding function that recreates the input data from the encoded representation. The autoencoder learns an efficient representation (encoding) for a set of data, typically for dimensionality reduction, to generate lower-dimensional embeddings for subsequent use by other machine learning algorithms.

# AutoML: Automated machine learning/自动机器学习

[concepts/AutoML.md](./concepts/AutoML.md)

# Bias–variance tradeoff/偏差-方差权衡
* https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff

In statistics and machine learning, the bias–variance tradeoff describes the relationship between a model's complexity, the accuracy of its predictions, and how well it can make predictions on previously unseen data that were not used to train the model.

# CNN: Convolutional Neural Network

# Decision tree learning/决策树学习
* https://en.wikipedia.org/wiki/Decision_tree_learning

Decision tree learning is a supervised learning approach used in statistics, data mining and machine learning. In this formalism, a *classification* or *regression* decision tree is used as a predictive model to draw conclusions about a set of observations.

# Deep Learning/深度学习
* https://en.wikipedia.org/wiki/Deep_learning

In machine learning, deep learning focuses on utilizing multilayered neural networks to perform tasks such as classification, regression, and representation learning.

Some common deep learning network architectures include 
- fully connected networks, 
- deep belief networks, 
- RNN(recurrent neural networks): 循环神经网络, 
- CNN(convolutional neural networks): 卷积神经网络, 
- GAN(generative adversarial networks): 生成对抗网络, 
- transformers, and 
- neural radiance fields.


- what does encoder and decoder mean in deep learning?
```markdown
在深度学习中，编码器（Encoder）和解码器（Decoder）是构成许多先进神经网络（如 [Transformer 架构](https://www.ibm.com/think/topics/encoder-decoder-model)和自编码器）的核心组件。它们本质上是一个双阶段的信息转换系统：编码器负责理解并压缩数据，解码器负责重建或生成新数据。 [1, 2] 
------------------------------
## 1. 核心定义与功能## 编码器 (Encoder)

* 任务：负责处理原始输入数据（如文本、图像、音频），并将其提取、压缩成一种高维的数学表示。
* 输出：生成一个特征向量，通常称为上下文向量（Context Vector）、隐藏状态或潜空间嵌入（Embedding）。
* 打个比方：就像一位精通多国语言的速记员。他听了一整段英文（输入），用只有自己看得懂的简短“符号笔记”（上下文向量）完美记录了这段话的核心意图。 [2, 3, 4] 

## 解码器 (Decoder)

* 任务：接收编码器生成的上下文向量，并以此为根据，逐步转化、恢复或生成最终的目标序列。
* 输出：生成目标任务所需的最终结果（如翻译后的文本、预测的下一词、重建的图像）。
* 打个比方：就像另一位翻译员。他看不懂最初的英文，但他能看懂速记员留下的“符号笔记”，并根据这个笔记逐字写出对应的中文（输出）。 [2, 3, 4, 5, 6] 

------------------------------
## 2. 它们如何协同工作？（以机器翻译为例）
在经典的 Sequence-to-Sequence (Seq2Seq) 任务中，两者的协作流程如下：

输入文本 -> [ 编码器 (Encoder) ] -> 上下文向量 -> [ 解码器 (Decoder) ] -> 输出文本
"Thank you" -> [ 提取语义特征 ]  ->  [0.42, -0.11,...] -> [ 逐字生成文本 ]  -> "谢谢你"


   1. 整体感知：编码器一次性读取完整的输入序列（例如："Thank you"），捕获词序和上下文语义。
   2. 信息桥梁：编码器把信息高度浓缩，传递给解码器。
   3. 逐步生成：解码器是**自回归（Autoregressive）**的。它先接收启动信号，结合上下文向量生成第一个字 "谢"；接着把 "谢" 作为自己下一步的输入，继续生成下一个字 "谢"，直到生成结束符（如 <EOS>）为止。 [2, 3, 4, 7] 

------------------------------
## 3. 两大主流应用场景
根据网络的设计目的，编码器和解码器的组合主要应用于以下两大方向：

| 应用架构类型 [1, 2, 7, 8, 9]                                                                                       | 编码器 (Encoder) 的职责                                               | 解码器 (Decoder) 的职责                                         | 典型应用任务                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------- | --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| 序列到序列模型 (如 Transformer[](https://machinelearningmastery.com/encoders-and-decoders-in-transformer-models/)) | 将源语言或媒体内容 转化为通用的语义特征                               | 将该语义特征转化为 另一种语言或形式的序列                       | 机器翻译、文本摘要、图像描述 (Image Captioning)[](https://medium.com/data-science/what-is-an-encoder-decoder-model-86b3d57c5e1a) |
| 自编码器 (Autoencoder / VAE)                                                                                       | 实施降维。消除输入中的噪声， 将其压缩至低维的潜空间（Latent Space）。 | 实施升维。尝试利用低维的特征 原封不动地“还原”或重建出原始输入。 | 图像去噪、数据降维、异常检测、生成全新样本                                                                                       |

------------------------------
## 4. 现代大语言模型（LLM）的演变
值得注意的是，在当前的 [大语言模型](https://arxiv.org/html/2510.26622v1) 时代，编码器和解码器不一定总是成对出现： [10] 

* Encoder-Only（仅编码器）：如 [BERT](https://sebastianraschka.com/books/ml-q-and-ai-chapters/ch17/)。擅长理解完整的上下文，常用于文本分类、命名实体识别和情感分析。
* Decoder-Only（仅解码器）：如 [ChatGPT (GPT 系列)](https://www.analyticsvidhya.com/blog/2024/06/why-does-chatgpt-use-only-decoder-architecture/)。没有独立的编码器，它把输入提示词（Prompt）和生成内容视作同一个序列，专门优化了单向的逐字文本流生成。 [11, 12, 13, 14, 15] 

如果想深入了解这一机制在代码中是如何落地的，可以参考 [Google 开发者技能库中关于 Encoder-Decoder 架构的配置与训练说明](https://www.skills.google/course_templates/543)。 [16] 
如果你正在研究某个具体的应用，可以告诉我：

* 你目前是在看 NLP（自然语言处理）、CV（计算机视觉） 还是 生成式 AI（如 Stable Diffusion/GPT）？
* 你需要看它在 PyTorch/TensorFlow 中的代码实现 吗？ [17, 18] 


[1] [https://www.ibm.com](https://www.ibm.com/think/topics/encoder-decoder-model)
[2] [https://medium.com](https://medium.com/@robin5002234/encoder-decoder-models-solving-sequence-to-sequence-problems-in-deep-learning-bc3cfe3be784)
[3] [https://medium.com](https://medium.com/analytics-vidhya/encoders-decoders-sequence-to-sequence-architecture-5644efbb3392)
[4] [https://www.geeksforgeeks.org](https://www.geeksforgeeks.org/nlp/encoder-decoder-models/)
[5] [https://www.quora.com](https://www.quora.com/What-is-an-Encoder-Decoder-in-Deep-Learning)
[6] [https://www.kaggle.com](https://www.kaggle.com/code/amansherjadakhan/encoder-decoder-and-attention-mechanism-theory)
[7] [https://machinelearningmastery.com](https://machinelearningmastery.com/encoders-and-decoders-in-transformer-models/)
[8] [https://medium.com](https://medium.com/data-science/what-is-an-encoder-decoder-model-86b3d57c5e1a)
[9] [https://www.scaler.com](https://www.scaler.com/topics/nlp/encoder-and-decoder/)
[10] [https://arxiv.org](https://arxiv.org/html/2510.26622v1)
[11] [https://magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-encoder-and-decoder)
[12] [https://sebastianraschka.com](https://sebastianraschka.com/books/ml-q-and-ai-chapters/ch17/)
[13] [https://www.analyticsvidhya.com](https://www.analyticsvidhya.com/blog/2024/06/why-does-chatgpt-use-only-decoder-architecture/)
[14] [https://medium.com](https://medium.com/@christianmatabaro92/mastering-language-model-architectures-a-comprehensive-guide-to-encoder-only-decoder-only-and-ed4365258405)
[15] [https://spj.science.org](https://spj.science.org/doi/10.34133/icomputing.0143)
[16] [https://www.skills.google](https://www.skills.google/course_templates/543)
[17] [https://trinesis.com](https://trinesis.com/blog)
[18] [https://news.ycombinator.com](https://news.ycombinator.com/item?id=43287821)
```

# Diffusion model/扩散模型
* https://en.wikipedia.org/wiki/Diffusion_model

In machine learning, diffusion models, also known as diffusion-based generative models/基于扩散的生成式模型 or score-based generative models/基于分数的生成式模型, are a class of latent variable generative models/潜在变量生成式模型. A diffusion model consists of two major components: the forward diffusion process/正向扩散过程, and the reverse sampling process/反向采样过程. The goal of diffusion models is to learn a diffusion process for a given dataset, such that the process can generate new elements that are distributed similarly as the original dataset. A diffusion model models data as generated by a diffusion process, whereby a new datum performs a random walk with drift through the space of all possible data. A trained diffusion model can be sampled in many ways, with different efficiency and quality.

See Also
* [Diffusers](https://github.com/huggingface/diffusers): Diffusers is the go-to library for state-of-the-art pretrained diffusion models for generating images, audio, and even 3D structures of molecules.

# Ensemble Learning/集成学习
* https://en.wikipedia.org/wiki/Ensemble_learning

在统计学和机器学习中, 集成学习(Ensemble learning)方法通过组合多种学习算法来获得比单独使用任何一种算法更好的预测性能.

# Evolution strategy/进化策略
* https://en.wikipedia.org/wiki/Evolution_strategy
* [Evolution Strategies as a Scalable Alternative to Reinforcement Learning](https://arxiv.org/abs/1703.03864)
* [A Visual Guide to Evolution Strategies](https://blog.otoro.net/2017/10/29/visual-evolution-strategies/)

Evolution strategy (ES) from computer science is a subclass of evolutionary algorithms(进化算法), which serves as an optimization technique. It uses the major genetic operators(遗传算子) mutation(突变), recombination(重组) and selection of parents(亲本选择).

# Evolutionary algorithm/进化算法
* https://en.wikipedia.org/wiki/Evolutionary_algorithm

Evolutionary algorithms (EA) reproduce essential elements of biological evolution in a computer algorithm in order to solve "difficult" problems, at least approximately, for which no exact or satisfactory solution methods are known. They are metaheuristics and population-based bio-inspired algorithms(元启发和基于种群的生物启发式) and evolutionary computation(进化计算), which itself are part of the field of computational intelligence. The mechanisms of biological evolution that an EA mainly imitates are reproduction(繁殖), mutation(突变), recombination(重组) and selection(选择). Candidate solutions to the optimization problem play the role of individuals in a population, and the fitness function determines the quality of the solutions (see also loss function). Evolution of the population then takes place after the repeated application of the above operators.

types:
- Genetic algorithm/遗传算法
- Genetic programming/遗传编程
- Evolutionary programming/进化规划
- Evolution strategy (ES)/进化策略
- Differential evolution/差分进化
- Coevolutionary algorithm/协同进化
- Neuroevolution/神经进化
- Learning classifier system/学习分类器系统
- Quality–Diversity algorithms/质量与多样性算法

# Exploratory Data Analysis/探索性数据分析
* https://en.wikipedia.org/wiki/Exploratory_data_analysis

See Also 
- [DataExploratory.ipynb](./theory/Data%20Exploratory.ipynb)
- Practical Statistics for Data Scientists

# Fine-tuning/微调
* https://en.wikipedia.org/wiki/Fine-tuning_(deep_learning)

In deep learning, fine-tuning is an approach to *transfer learning* in which the parameters of a pre-trained neural network model are trained on new data. 
Fine-tuning can be done on the entire neural network, or on only a subset of its layers, in which case the layers that are not being fine-tuned are "frozen" (i.e., not changed during backpropagation). 
A model may also be augmented with "adapters"—lightweight modules inserted into the model's architecture that nudge the embedding space for domain adaptation. These contain far fewer parameters than the original model and can be fine-tuned in a parameter-efficient way by tuning only their weights and leaving the rest of the model's weights frozen.


- 有哪些LLM微调技术, 各自的优势和局限性有哪些?
```markdown
在大语言模型（LLM）的调优与落地过程中，微调技术主要分为三大类：全参数微调、高效参数微调（PEFT） 以及 对齐微调。
以下是主流微调技术的分类、优势与局限性横向对比：
------------------------------
## 一、 全参数微调（Full Fine-Tuning / FFT）
直接更新模型内部所有层的全部参数。

* 优势：
* 上限最高：模型能够最彻底地吸收领域新知识，彻底改变其基调。
   * 表达自然：不会因为引入额外模块而影响推理速度或增加架构复杂度。
* 局限性：
* 算力成本极高：训练时需要存储显度（Gradients）和优化器状态（Optimizer States），显存需求是模型自身大小的 4-6倍。
   * 灾难性遗忘：过度拟合新领域数据后，模型原有的通用常识和逻辑推理能力会严重退化。

------------------------------
## 二、 高效参数微调（PEFT - Parameter-Efficient Fine-Tuning）
冻结模型主干参数，仅引入并训练极少量的附加参数（通常 $<1\%$）。
## 1. LoRA (Low-Rank Adaptation)
通过在原矩阵旁引入两个低秩（Low-Rank）分解的小矩阵来模拟参数变化。

* 优势：
* 显存骤降：大幅降低训练门槛，消费级显卡（如 4090）即可微调百亿级模型。
   * 无推理延迟：在训练完成后，可以将低秩矩阵的权重直接合并（Merge）回原模型，不增加任何推理开销。
* 局限性：
* 复杂知识吸收弱：难以建立全新的长时记忆，更适合让模型学习特定的“输出格式”或“指令风格”。

## 2. QLoRA (Quantized LoRA)
在 LoRA 的基础上，将基座模型量化为 4-bit（NF4格式）进行训练。

* 优势：
* 极致省显存：比 LoRA 还要节省近一半的显存（例如单卡 24G 显存即可训练 13B 模型）。
* 局限性：
* 训练速度变慢：因为在训练过程中需要频繁进行 4-bit 与 16-bit 之间的反量化（De-quantization）计算，时间成本增加。

## 3. Prefix Tuning / Prompt Tuning
在输入的 Embedding 层或 Transformer 的每一层前拼接一段可训练的连续虚拟 Token（前缀）。

* 优势：
* 模块化插拔：同一个基座模型可以针对不同任务训练不同前缀，推理时根据请求动态替换前缀即可。
* 局限性：
* 挤占上下文空间：前缀虚拟 Token 会占用宝贵的 Prompt 上下文长度。
   * 训练难度高：参数对初始化极度敏感，训练过程容易出现不收敛或不稳定。

------------------------------
## 三、 对齐微调（Alignment Tuning / 偏好对齐）
不以学习新知识为目的，而是调整模型的价值观，使其回答更符合人类的偏好（安全、有用、诚实）。
## 1. RLHF (基于人类反馈的强化学习)
引入奖励模型（Reward Model）引导大模型通过 PPO 算法进行策略迭代。

* 优势：
* 效果上限极高：能够精准捕捉人类难以用公式表达的微妙偏好，是 ChatGPT 等顶尖模型的核心基石。
* 局限性：
* 架构极端复杂：需要同时运行 4 个模型（演员、评论家、参考、奖励），训练成本巨大。
   * 对齐税（Alignment Tax）：过度追求安全性会导致模型变得过于保守（如频繁拒绝回答正常问题）。

<!--
PPO（Proximal Policy Optimization，近端策略优化） 是 RLHF 中最经典、应用最广的强化学习核心算法。

近两年的业界正在大量用 DPO（Direct Preference Optimization，直接偏好优化） 替代 PPO [12]。DPO 通过数学转换，直接在 SFT 模型上进行偏好损失计算，不需要显式训练 Reward 模型和 Critic 模型，显存消耗减半，训练极度稳定。
-->

## 2. DPO (Direct Preference Optimization / 直接偏好优化)
跳过奖励模型和强化学习阶段，将对齐问题直接转化为包含“好回答”和“坏回答”的二分类交叉熵损失函数。

* 优势：
* 简单且稳定：像普通监督微调（SFT）一样易于训练，算力开销和显存占用与标准微调无异。
* 局限性：
* 泛化能力略逊：在缺乏强化学习探索（Exploration）的情况下，模型容易在未见过的数据上表现出脆弱性。

------------------------------
## 🛠️ 微调技术选型指南

   1. 想让模型学习一种全新的垂类复杂语言（如医疗诊断、工业代码）：选择 FFT（全参数微调） 或 LoRA（增加 Rank 值）。
   2. 只有单张或少量消费级显卡，想快速让模型跑通特定任务：首选 QLoRA。
   3. 想解决模型胡言乱语、答非所问、价值观偏见的问题：在 SFT 之后增加 DPO 微调。

您目前计划进行的微调任务，其核心目标是让模型学习海量新业务知识，还是纯粹为了固定其输出的 JSON 格式？我们可以针对具体的场景来规划数据配比。
```

- 如何调优模型, 直接将RAG等外挂存储技术调整为模型的长时记忆?
```markdown
要将 RAG 等外挂存储技术直接调优为模型的“长时记忆”（即让模型像人类大脑一样，无需通过复杂的检索和提示词拼接，就能直接对历史或外部知识产生本能的深度理解），在技术路线上已经从单纯的“提示词工程”转向了架构级融合和针对性微调。
以下是实现这一转变的四大调优核心路径：
## 1. 训练专用检索器：将向量模型与大模型“端到端联合微调”

* 痛点：常规 RAG 的 Embedding 模型和大模型是割裂的。
* 调优方案：采用 REALM [1] 或 RA-DIT (Retrieval-Augmented Dual-Instruction Tuning) 架构。
* 步骤：在微调大模型时，同时反向传播梯度给向量检索模型。
   * 效果：模型能像控制自己的手臂一样控制检索器。大模型缺什么知识，检索器就能精准捞回什么知识，实现检索层面的“肌肉记忆”。

## 2. 长上下文微调（Long-Context Fine-Tuning）与位置编码外推

* 技术原理：不改变架构，直接扩容模型的“原生内存”，让其吞下外挂存储。
* 调优方案：
* 数据构造：将历史对话、外挂知识库打包成数十万 Token 的超长文本。
   * 位置编码微调：对 RoPE（旋转位置编码） 进行基数扩展（Base Extension）或 YARN 插值法微调。
   * 激活层优化：结合 FlashAttention-3 [2] 或 Ring Attention 进行长序列并行训练，让模型在 128k - 1M 的超长窗口内，对深埋其中的知识保持高敏感度（解决大海捞针 Needle in a Haystack 问题）。

## 3. 架构级融合调优：融入外部存储的门控机制（Memory-Augmented LLM）

* 技术原理：修改 Transformer 结构，在层与层之间直接插入非参数化的记忆模块（非简单的 Prompt 拼接）。
* 调优方案：参考 Focused Transformer (FOT) 或 MemGPT 理念。
* 交叉注意力调优（Cross-Attention Tuning）：在 Transformer Block 中引入一门特殊的注意力机制，专门用来读取长时记忆数据库。
   * 训练目标：在预训练或微调阶段，让模型学会一个触发器（Gate）。当遇到需要长时记忆的 Token 时，门控打开，直接在隐空间（Embedding Space）读取外部记忆，消除文本拼接的开销。

## 4. 基于长时记忆语义池的指令微调（LoRA / Full FT）

* 数据构造：这是最易落地的方案。改变训练集结构，将 RAG 转化为模型的内在认知。
* 调优方案：
* 构造“记忆检索-推理”三元组：训练集格式为 [Context 外部记忆] + [User 问题] -> [模型思考/检索动作] -> [最终回答]。
   * 遗忘防止调优：微调时混合 10%-20% 的通用能力通用数据集（如 Alpaca），防止模型在吃进长时记忆的同时发生灾难性遗忘（Catastrophic Forgetting）。
   * 对齐调优 (DPO/RLHF)：通过偏好对齐，惩罚模型在拥有长时记忆时依然编造谎言（幻觉）的行为。

------------------------------
## 🚀 落地选型建议

   1. 预算/算力有限：选择 方案 4 (LoRA微调)。直接用长文本+特定指令格式训练大模型，让它适应带着“记忆挂件”思考。
   2. 追求极致原生感：选择 方案 2 (长窗口微调)。配合 KV Cache 磁盘缓存技术。每次对话不丢弃历史，而是将历史 KV Cache 持久化到 NVMe 固态硬盘中。模型需要时直接异步加载 KV 状态，这是目前最接近人类“唤醒记忆”的方案。

您目前手头拥有的算力资源（如：单张消费级显卡、A100/H100集群）以及基座模型大小（如：7B、14B、70B）是怎样的？我们可以据此制定最可行的微调配置参数方案。
```

# GPT(Generative Pre-trained Transformer)/生成式预训练Transformer
* https://en.wikipedia.org/wiki/Generative_pre-trained_transformer

# Hyperparameter/超参数
* https://en.wikipedia.org/wiki/Hyperparameter_(machine_learning)

In machine learning, a hyperparameter is **a parameter that can be set in order to define any configurable part of a model's learning process**. Hyperparameters can be classified as either **model hyperparameters** (such as the topology and size of a neural network) or **algorithm hyperparameters** (such as the learning rate and the batch size of an optimizer). These are named hyperparameters in contrast to *parameters*, which are characteristics that the model learns from the data.

# Learning curve/学习曲线
* https://en.wikipedia.org/wiki/Learning_curve_(machine_learning)

In machine learning (ML), a learning curve (or training curve) is a graphical representation that shows how a model's performance on a training set (and usually a validation set) changes with the number of training iterations (epochs) or the amount of training data. Typically, the number of training epochs or training set size is plotted on the x-axis, and the value of the loss function (and possibly some other metric such as the cross-validation score) on the y-axis.

# LLM(Large Language Model)/大语言模型
* https://en.wikipedia.org/wiki/Large_Language_Model


- LLM为什么会有上下文大小限制, 是单次调用中的限制?
```markdown
LLM（大语言模型）的上下文大小限制主要是由其底层架构和硬件算力决定的。
## 为什么会有上下文限制？

* 注意力机制算力开销：Transformer核心的自注意力机制（Self-Attention）需要计算所有Token两两之间的关系。
* 计算复杂度呈平方级增长：上下文长度翻倍，计算量和内存占用会变为原来的 4倍（$O(N^2)$ 复杂度）。
* 显存硬件瓶颈：随着输入变长，显卡显存（VRAM）会迅速耗尽导致显存溢出（OOM）。
* 位置编码能力限制：模型训练时使用的位置编码（如RoPE）有固定范围，超出该范围模型无法有效理解Token的顺序。

## 是单次调用中的限制吗？

* 是的：上下文限制严格作用于单次API调用或单次交互中。
* 包含输入与输出：总上下文长度 = 单次输入的提示词（Prompt） + 历史聊天记录 + 模型单次生成的回复（Output）。
* 不具备跨调用记忆：模型本身不会记住上一次调用的内容。
* 通过拼接实现连续对话：聊天软件是通过在下一次调用时，将之前的历史记录全部拼接并再次发送给模型，才实现了有记忆的连续对话。当拼接的总长度超过限制时，最旧的记忆就会被截断丢弃。

若您想了解具体优化技术，我们可以讨论：

* 位置编码外推（如RoPE旋转位置编码延伸）
* 线性和低复杂度注意力机制（如FlashAttention、Linear Attention）
* 外挂存储技术（如RAG检索增强生成）

您对哪种长文本解决方案最感兴趣？
```

- 外挂存储技术是怎么优化这个限制的?
```markdown
外挂存储技术（通常指 RAG，检索增强生成）通过“分治法”绕过LLM单次调用的上下文限制。它不盲目将所有资料喂给模型，而是只提供最相关的片段。
## 核心运作流程

* 海量文档向量化：将千万字的长文本拆分成无数个小片段（如每段 500 字）。
* 构建向量数据库：利用 Embedding 模型将这些片段转化为数学向量，存入专门的数据库。
* 精准检索相关内容：用户提问时，系统计算问题与数据库片段的相似度，只捞取最相关的 3-5 个片段。
* 组装精准提示词：将这几个片段与用户问题拼接，作为最终的 Prompt 发送给 LLM。

## 如何优化上下文限制？

* 化无限为有限：将原本超出限制的几百万字资料，压缩成几千字的精准片段，完美容纳进单次调用的上下文窗口内。
* 计算复杂度极低：向量数据库的检索复杂度远低于 Transformer 的平方级计算（$O(N^2)$），大幅节省 GPU 算力。
* 降低接口调用成本：单次输入的 Token 数量骤降，直接减少了按 Token 计费的 API 开销。
* 实现“伪”无限记忆：模型不需要在单次调用中记住所有事，而是通过外挂的“数字大脑”随时按需查阅。

如果您想深入了解 RAG 的实际落地，我们可以探讨：

* RAG 架构中最常用的向量数据库（如 Milvus, Pinecone）
* 如何解决检索到错误/无关信息的问题（重排技术 Rerank）
* 它与长文本大模型（如支持 2M 上下文的模型）如何结合使用

您更倾向于了解技术架构还是应用场景？
```

# Model Context Protocol (MCP)/模型上下文协议
* https://modelcontextprotocol.io/docs/getting-started/intro

MCP (Model Context Protocol) is an open-source standard for connecting AI applications to external systems/连接AI应用和外部系统的开源标准.

Using MCP, AI applications like Claude or ChatGPT can connect to data sources (e.g. local files, databases), tools (e.g. search engines, calculators) and workflows (e.g. specialized prompts)—enabling them to access key information and perform tasks.

Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect electronic devices, MCP provides a standardized way to connect AI applications to external systems.

# NA

NA, stands fro **not available**. In statistics application NA data may either be data that does not exist or that exists but wat not observed.

In pandas, there are NA handling object methods:
- `dropna`
- `fillna`
- `isna`
- `notna`

# Naive Bayes classifier/朴素贝叶斯分类器
* https://en.wikipedia.org/wiki/Naive_Bayes_classifier

In statistics, naive (sometimes simple or idiot's) Bayes classifiers are a family of "probabilistic classifiers" which *assumes that the features are conditionally independent*, given the target class.

# PCA: Principle Component Analysis/主成分分析

# Prompt Engineering/提示工程
* https://en.wikipedia.org/wiki/Prompt_engineering

# RAG(Retrieval-Augmented Generation)/检索增强生成
* https://en.wikipedia.org/wiki/Retrieval-augmented_generation

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/RAG_diagram.svg/500px-RAG_diagram.svg.png" width="40%"/>

See Also
- [GraphRAG的优化相比常规RAG优化, 有哪些优化效果, 需要提供什么基本能力?](./concepts/ai_generated/gen-graphrag.md)

# Regularization/正则化
* https://en.wikipedia.org/wiki/Regularization_(mathematics)

In mathematics, statistics, finance, and computer science, particularly in machine learning and inverse problems, regularization is a process that converts the answer to a problem to a simpler one. It is often used in solving ill-posed problems(不适定问题) or to prevent overfitting(避免过拟合).

# Reinforcement Learning/强化学习
* https://en.wikipedia.org/wiki/Reinforcement_learning

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Reinforcement_learning_diagram.svg/1920px-Reinforcement_learning_diagram.svg.png" width="40%"/>

In machine learning/机器学习 and optimal control/最优控制, reinforcement learning (RL) is **concerned with how an intelligent agent should take actions in a dynamic environment in order to maximize a reward signal**. Reinforcement learning is one of the three basic machine learning paradigms, alongside supervised learning and unsupervised learning.

While supervised learning and unsupervised learning algorithms respectively attempt to *discover patterns in labeled and unlabeled data*, reinforcement learning involves **training an agent through interactions with its environment**. To learn to maximize rewards from these interactions, the agent makes decisions between trying new actions to learn more about the environment (exploration), or using current knowledge of the environment to take the best action (exploitation). The search for the optimal balance between these two strategies is known as the exploration–exploitation dilemma.

The environment is typically stated in the form of a Markov decision process/马尔可夫决策过程, as many reinforcement learning algorithms use dynamic programming techniques/动态规划技术. The main difference between classical dynamic programming methods and reinforcement learning algorithms is that the latter *do not assume knowledge of an exact mathematical model of the Markov decision process*, and they target large Markov decision processes where exact methods become infeasible.

# ROC curve: Receiver Operating Characteristic
* https://en.wikipedia.org/wiki/Receiver_operating_characteristic
* [Understanding ROC curves](http://www.navan.name/roc/)

A receiver operating characteristic curve, or ROC curve, is a graphical plot that illustrates the performance of a binary classifier model (although it can be generalized to multiple classes) at varying threshold values.

The ROC curve is the plot of the true positive rate (TPR) against the false positive rate (FPR) at each threshold setting.

# RNN(Recurrent Neural Network)/循环神经网络
* https://en.wikipedia.org/wiki/Recurrent_neural_network

两种架构: LSTM(长短期记忆网络), BRNN(双向循环神经网络)

# SGD(Stochastic gradient descent)/随机梯度下降
* https://en.wikipedia.org/wiki/Stochastic_gradient_descent

Stochastic gradient descent (often abbreviated SGD) is **an iterative method for optimizing an objective function with suitable smoothness properties** (e.g. differentiable or subdifferentiable). It can be regarded as a stochastic approximation of gradient descent optimization, since it replaces the actual gradient (calculated from the entire data set) by an estimate thereof (calculated from a randomly selected subset of the data). Especially in high-dimensional optimization problems this reduces the very high computational burden, achieving faster iterations in exchange for a lower convergence rate.

# t-SNE(t-Distributed Stochastic Neighbor Embedding)

# Transfer learning/迁移学习
* https://en.wikipedia.org/wiki/Transfer_learning

Transfer learning (TL) is a technique in machine learning (ML) in which knowledge learned from a task is re-used in order to boost performance on a related task.

# Transformers
* https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)

In deep learning, transformer is a neural network architecture based on the **multi-head attention mechanism**, in which text is converted to numerical representations called *tokens*, and each token is converted into a vector via lookup from a word embedding table.
At each layer, each token is then contextualized within the scope of the context window with other (unmasked) tokens via a parallel multi-head attention mechanism, allowing the signal for key tokens to be amplified and less important tokens to be diminished.

# Vanishing gradient problem/梯度消失问题
* https://en.wikipedia.org/wiki/Vanishing_gradient_problem

梯度消失问题: 基于梯度的学习方法中, 权重的更新是与当前权重上的错误函数的偏导成比例的. 在一些情况下, 梯度极其的小, 权重无法有效更新.

# Vibe Coding/氛围编码
* https://en.wikipedia.org/wiki/Vibe_coding

In computer programming, vibe coding is an AI-assisted software development practice/AI辅助软件开发实践. It is a chatbot-based approach to creating software where the developer describes a project or task to a large language model (LLM), which generates source code based on the prompt. The developer does not review or edit the code, but solely uses tools and execution results to evaluate it and asks the LLM for improvements. Unlike traditional AI-assisted coding or pair programming, the human developer avoids examination of the code, accepts AI-suggested completions without human review, and focuses more on iterative experimentation than on code correctness or structure.

Tools
* Cursor AI
* Claude 3.7 Sonnet
* Super Whisper
* Google AI Studio