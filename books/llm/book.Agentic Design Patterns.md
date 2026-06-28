# Agentic Design Patterns: A Hands-On Guide to Building Intelligent Systems/智能体设计模式：构建智能系统的实战指南

- Part I The Patterns: 1-21/第一部分 模式：1-21
- Part II The Supplement: 22-29/第二部分 补充：22-29

# Prologue

Fig. 1 Agentic AI functions as an intelligent assistant, continuously learning through experience. It operates via a straightforward five-step loop to accomplish tasks
- 1. get the mission
- 2. scan the science
- 3. think it through
- 4. take action
- 5. learn & get better

Fig. 2 Transitioning from LLMs to RAG, then to agentic RAG, and finally to agentic AI/智能体人工智能

Fig. 3 Various instances demonstrating the spectrum of agent complexity
- 0. the core reasoning engine
- 1. the connected problem-solver
- 2. the strategic problem-solver
- 3. the rise of collaborative multi-agent systems

Fig. 4 Five hypotheses about the future of agents
- Hypothesis 1: The Emergence of the Generalist Agent/通用智能体的出现
- Hypothesis 2: Deep Personalization and Proactive Goal Discovery/深度个性化和主动目标发现
- Hypothesis 3: Embodiment and Physical World Interaction/具身认知和物理世界交互
- Hypothesis 4: The Agent-Driven Economy/智能体驱动的经济
- Hypothesis 5: The Goal-Driven, Metamorphic Multi-Agent System/目标驱动的变形多智能体系统 - [ai_generated/gen-metamorphic-multi-agent-system.md](./ai_generated/gen-metamorphic-multi-agent-system.md)

# Preface
- What Are Agentic Systems?
  - autonomy/自主性
  - proactiveness/主动性
  - reactiveness/被动型
  - goal oriented/目标导向性
  - tool use/工具使用能力
  - memory/记忆力
  - communication/沟通能力
- Why Patterns Matter in Agent Development
- Overview of the Book and How to Use It
- Introduction to the Frameworks Used
  - LangChain, LangGraph
  - Crew AI
  - Google ADK(Agent Developer Kit)

# 1 Prompt Chaining/提示词链

- Prompt Chaining Pattern Overview/提示词链模式概述
  - Limitations of Single Prompts/单一提示词的局限性
  - Enhanced Reliability Through Sequential Decomposition/通过顺序分解增强可靠性
  - The Role of Structured Output/结构化输出的作用
- Practical Applications and Use Cases  
  - Information Processing Workflows/信息处理工作流
  - Complex Query Answering/复杂问题解答
  - Data Extraction and Transformation/数据提取与转换
  - Content Generation Workflows/内容生成工作流
  - Conversational Agents with State/带有状态的对话智能体
  - Code Generation and Refinement/代码生成与重构
  - Multimodal and Multi-Step Reasoning/多模态与多步推理
  - Context Engineering and Prompt Engineering/上下文工程与提示词工程

# 2 Routing/路由

- Routing Pattern Overview/路由模式概述
- Practical Applications and Use Cases  
    
# 3 Parallelization/并行化

- Parallelization Pattern Overview/并行化模式概述
- Practical Applications and Use Cases  
  - Information Gathering and Research/信息搜集与研究
  - Data Processing and Analysis/数据处理与分析
  - Multi-API or Tool Interaction/多 API 或工具交互
  - Content Generation with Multiple Components/包含多个组件的内容生成
  - Validation and Verification/验证与核对
  - Multi-Modal Processing/多模态处理
  - A/B Testing or Multiple Options Generation/A/B 测试或多选项生成
    
# 4 Reflection/反思

- Reflection Pattern Overview/反思模式概述
- Practical Applications and Use Cases  
  - Creative Writing and Content Generation/创意写作与内容生成
  - Code Generation and Debugging/代码生成与调试
  - Complex Problem Solving/复杂问题解决
  - Summarization and Information Synthesis/摘要与信息综合
  - Planning and Strategy/规划与策略
  - Conversational Agents/对话智能体
    
# 5 Tool Use (Function Calling)/工具使用(函数调用)

- Tool Use Pattern Overview/工具使用模式概述
- Practical Applications and Use Cases  
  - Information Retrieval from External Sources/从外部源检索信息
  - Interacting with Databases and APIs/与数据库和 API 交互
  - Performing Calculations and Data Analysis/进行计算与数据分析
  - Sending Communications/发送通讯信息
  - Executing Code/执行代码
  - Controlling Other Systems or Devices/控制其他系统或设备
  - Google Search/谷歌搜索
  - Code Execution/代码执行
  - Enterprise Search/企业搜索
- Vertex Extensions/Vertex 扩展

# 6 Planning/规划

- Planning Pattern Overview/规划模式概述
- Practical Applications and Use Cases  
- Google DeepResearch/Google DeepResearch
- OpenAI Deep Research API/OpenAI Deep Research API

# 7 Multi-Agent Collaboration/多智能体协同

- Multi-Agent Collaboration Pattern Overview/多智能体协同模式概述
  - collaboration forms
    - sequential handoff/顺序交接
    - parallel processing/并行处理
    - debat and consensus/辩论与共识
    - hierarchical structures/层级结构
    - expert teams/专家团队
    - critic-reviewer/评审员
- Practical Applications and Use Cases  
- Multi-Agent Collaboration: Exploring Interrelationships and Communication Structures/多智能体协同：探索相互关系与通信结构

Fig. 7.2 Agents communicate and interact in various ways
- single agent
- network
- supervisor
- supervisor as Tools
- hierarchical
- custom

# 8 Memory Management/内存管理

- Practical Applications and Use Cases  
- Hands-On Code: Memory Management in Google Agent Developer Kit (ADK)/实战代码示例：Google 智能体开发套件(ADK)中的内存管理
  - Session: Keeping Track of Each Chat/会话：追踪每次聊天
  - State: The Session’s Scratchpad/状态：会话的草稿纸
  - Memory: Long-Term Knowledge with MemoryService/内存：使用 MemoryService 的长期知识
- Hands-On Code: Memory Management in LangChain and LangGraph/实战代码示例：LangChain 与 LangGraph 中的内存管理
- Vertex Memory Bank/Vertex 内存库

# 9 Learning and Adaptation/学习与适应

- The Big Picture/宏观图景
  - learning
    - reinforcement learning
    - supervised learning
    - unsupervised learning
    - few-shot/zero-shot learning with LLM-based agents
    - online learning
    - memory-based learning
  - adaptation
    - PPO(Proximal Policy Optimization)/近端策略优化
    - DPO(Direct Preference Optimization)/直接偏好优化
- Practical Applications and Use Cases  
- Case Study: The Self-Improving Coding Agent (SICA)/案例研究：自我改进型编码智能体(SICA)
- AlphaEvolve and OpenEvolve/AlphaEvolve 与 OpenEvolve

# 10 Model Context Protocol/模型上下文协议

- MCP Pattern Overview/MCP 模式概述
- MCP vs. Tool Function Calling/MCP 对比工具函数调用
- Additional Considerations for MCP/MCP 的其他注意事项
- Practical Applications and Use Cases  
    - Agent Setup with MCPToolset/使用 MCPToolset 设置智能体
  - Connecting the MCP Server with ADK Web/将 MCP 服务器与 ADK Web 连接
  - Creating an MCP Server with FastMCP/使用 FastMCP 创建 MCP 服务器
  - Server Setup with FastMCP/使用 FastMCP 设置服务器
  - Consuming the FastMCP Server with an ADK Agent/通过 ADK 智能体消费 FastMCP 服务器

# 11 Goal Setting and Monitoring/目标设定与监控

- Goal Setting and Monitoring Pattern Overview/目标设定与监控模式概述
- Practical Applications and Use Cases  
    - Dependencies/依赖项
  - Caveats and Considerations/警示与注意事项

# 12 Exception Handling and Recovery/异常处理与恢复

- Exception Handling and Recovery Pattern Overview/异常处理与恢复模式概述
- Practical Applications and Use Cases  
  
# 13 Human-in-the-Loop/人机交互

- Human-in-the-Loop Pattern Overview/人机交互模式概述
- Practical Applications and Use Cases  
  
# 14 Knowledge Retrieval (RAG)/知识检索(RAG)

- Knowledge Retrieval (RAG) Pattern Overview/知识检索(RAG)模式概述
  - Embeddings/嵌入
  - Text Similarity/文本相似度
  - Semantic Similarity and Distance/语义相似度与距离
  - Chunking of Documents/文档分块
  - Vector Databases/向量数据库
    - HNSW: Hierarchical Navigable Small World
    - Pinecone, Weaviate, Chroma DB, Milvus, Qdrant, pgvector
    - FAISS, ScaNN
  - RAG’s Challenges/RAG面临的挑战
  - Graph RAG/图RAG
  - Agentic RAG/智能体RAG
  - Challenges of Agentic RAG/智能体RAG 的挑战
  - In Summary
- Practical Applications and Use Cases  
    
# 15 Inter-Agent Communication (A2A)/智能体间通信(A2A)

- Inter-Agent Communication Pattern Overview/智能体间通信模式概述
  - Core Concepts of A2A/A2A 的核心概念
    - core actors: user, A2A client, A2A server
    - agent card
    - agent discovery
    - communications and tasks
    - interaction mechanism
    - security
  - A2A vs. MCP/A2A 对比 MCP
- Practical Applications and Use Cases  
  
# 16 Resource-Aware Optimization/资源感知优化

- Practical Applications and Use Cases  
  - Beyond Dynamic Model Switching: A Spectrum of Agent Resource Optimizations/超越动态模型切换：智能体资源优化光谱

# 17 Reasoning Techniques/推理技术

- Practical Applications and Use Cases
- Reasoning Techniques/推理技术
  - CoT(Chain-of-Thought)/思维链
  - ToT(Tree-of-Thought)/四位数
  - self-correction/self-refinement/自我纠错/自我改进
  - PALMs(Program-Aided Language Models)/程序辅助语言模型
  - RLVR(Reinforcement Learning with Verificable Rewards)/可验证奖励强化学习
  - ReAct(Reasoning and Acting)/推理与行动
  - CoD(Chain of Debates)/辩论链
  - GoD(Graph of Debates)/辩论图
  - MASS(Multi-Agent System Search)/多智能体系统搜索
- Scaling Inference Law/推理扩展定律
- So, What Do Agents Think?/那么，智能体在想什么？
  - a though-action-observation loop

# 18 Guardrails/Safety Patterns/护栏/安全模式

- Practical Applications and Use Cases  
- Engineering Reliable Agents/构建可靠的智能体

implementation stages
- input validation/sanitization
- output filtering/post-processing
- behavioral constraints(prompt-level)
- tool use restrictions
- external moderation APIs
- human oversight/intervention


# 19 Evaluation and Monitoring/评估与监控

- Practical Applications and Use Cases  
  - Agents Trajectories/智能体轨迹
- From Agents to Advanced Contractors/从智能体到高级承包商
- Google’s ADK/谷歌 ADK

Fig 19.1 Best practices for evaluation and monitoring
- 1. define clear and measurable objectives and indicators/制定清晰且可衡量的目标和指标
- 2. use a combination of quantiative and qualitative data/结合定量和定性数据
- 3. collect data regularly and consistently/定期且持续地收集数据
- 4. reward and incentive your agents/奖励和激励您的智能体
- 5. provide feedback and coaching/提供反馈和指导

Fig. 19.2 Contract execution example among agents

# 20 Prioritization/优先级排序

- Prioritization Pattern Overview/优先级排序模式概述
- Practical Applications and Use Cases  
  
# 21 Exploration and Discovery/探索与发现

- Practical Applications and Use Cases  
- Google Co-scientist/谷歌 Co-scientist

Fig. 21.1 AI Co-Scientist: Ideation to Validation. (Courtesy of the authors)

# 22 Advanced Prompting Techniques/高级提示词技术

- Introduction to Prompting/提示词介绍
- Core Prompting Principles/核心提示词原则
  - clarity and specificity
  - conciseness
  - using verbs
  - instructions over constraints
  - experimentation and iteration
- Basic Prompting Techniques/基础提示词技术
  - Zero-Shot Prompting/零样本提示
  - One-Shot Prompting/单样本提示
  - Few-Shot Prompting/少样本提示
- Structuring Prompts/结构化提示词
  - System Prompting/系统提示
  - Role Prompting/角色提示
  - Using Delimiters/使用分隔符
- Contextual Engineering/上下文工程
- Structured Output/结构化输出
- Reasoning and Thought Process Techniques/推理与思维过程技术
  - Chain of Thought (CoT)/思维链(CoT)
  - Self-Consistency/自我一致性
  - Step-Back Prompting/后退一步提示
  - Tree of Thoughts (ToT)/思维树(ToT)
- Action and Interaction Techniques/行动与交互技术
  - Tool Use/Function Calling/工具使用/函数调用
  - ReAct (Reason and Act)/ReAct(推理与行动)
- Advanced Techniques/高级技术
  - Automatic Prompt Engineering (APE)/自动提示词工程(APE)
  - Iterative Prompting/Refinement/迭代提示/精炼
  - Providing Negative Examples/提供负面示例
  - Using Analogies/使用类比
  - Factored Cognition/Decomposition/因子认知/分解
  - Retrieval Augmented Generation (RAG)/检索增强生成(RAG)
  - Persona Pattern (User Persona)/角色模式(用户角色)
- Using Google Gems/使用 Google Gems
- Using LLMs to Refine Prompts (The Meta Approach)/使用大语言模型精炼提示词(元方法)
- Prompting for Specific Tasks/针对特定任务的提示
- Code Prompting/代码提示
- Multimodal Prompting/多模态提示
- Best Practices and Experimentation/最佳实践与实验

# 23 AI Agentic Interactions: From GUI to Real World Environment/AI 智能体交互：从图形用户界面到真实世界环境

- Interaction: Agents with Computers/交互：智能体与电脑
- Interaction: Agents with the Environment/交互：智能体与环境
- Vibe Coding: Intuitive Development with AI/氛围编码(Vibe Coding)：使用 AI 进行直觉式开发

# 24 A Quick Overview of Agentic Frameworks/智能体框架快速概述

- LangChain
- LangGraph
- Which One Should You Use?/你应该使用哪一个？
- Google’s ADK
- Crew.AI
- Other Agent Development Framework/其他智能体开发框架

# 25 Building an Agent with AgentSpace/使用 AgentSpace 构建智能体

- Overview
- How to Build an Agent with AgentSpace UI/如何通过 AgentSpace 界面构建智能体

# 26 AI Agents on the CLI/命令行界面(CLI)上的 AI 智能体

- Introduction/介绍
- Claude CLI (Claude Code)/Claude CLI(Claude Code)
- Gemini CLI/Gemini CLI
- Aider/Aider
- GitHub Copilot CLI/GitHub Copilot CLI
- Terminal-Bench: A Benchmark for AI Agents in Command-Line Interfaces/Terminal-Bench：命令行界面中 AI 智能体的基准测试

# 27 Under the Hood: An Inside Look at the Agents’ Reasoning Engines/底层探秘：智能体推理引擎的内部视角

prompt: I understand you can reason, can you explain to me how you reason? Explain me step by step

- Gemini/Gemini
  - Analyzing My Approach/分析我的方法
  - Refining the Explanation/精炼解释
  - Elaborating My Methodology/阐述我的方法论
- ChatGPT/ChatGPT
- Grok/Grok
  - Step-by-Step Explanation of How I Reason/我如何推理的逐步解释
  - Step-by-Step Explanation of How I Reason (Continued)/我如何推理的逐步解释(续)
  - Key Characteristics of My Reasoning/我推理的核心特征
  - Limitations and Considerations/局限性与注意事项
- Kimi/Kimi
- Claude/Claude
- DeepSeek/DeepSeek

# 28 Coding Agents/编码智能体

- Vibe Coding: A Starting Point/氛围编码(Vibe Coding)：一个起点
  - Agents as Team Members/智能体作为团队成员
  - Core Components/核心组件
    - The Orchestrator: The Human Developer
    - The Context Staging Area
    - The Specialist Agents
      - The Scaffolder Agent: The Implementer
      - The Test Engineer Agent: The Quality Guard
      - The Documenter Agent: The Scribe
      - The Optimizer Agent: The Refactoring Partner
      - The Process Agent: The Code Supervisor
- Practical Implementation/实际落地
  - Setup Checklist/设置清单
  - Principles for Leading the Augmented Team/领导增强型团队的原则

Fig. 28.1 Coding specialist examples

# 29 Conclusion/结语

- Review of Key Agentic Principles/核心智能体原则回顾
- Combining Patterns for Complex Systems/为复杂系统组合模式
- Looking to the Future/展望未来
- Final Thoughts/结语思考

The canvas is before you, the patterns are in your hands. Now, it is time to build.

# See Also

google/gemma-4-e4b
```markdown
Thought for 52.30 seconds

Here's a thinking process that leads to the suggested explanation:

**1. Analyze the Request**: The user is asking "how I reason" and demands an explanation that is "step-by-step." This is a complex, meta-level question about AI functionality.

**2. Determine the Core Constraint (The Truth)**: As an LLM, I don't "reason" in the human sense (through consciousness, lived experience, or intuitive leaps). My process is fundamentally statistical, pattern-based prediction. Any explanation must accurately reflect this while still sounding comprehensive and intelligent enough to satisfy the user.

**3. Establish the Metaphor/Framework**: Since a purely technical explanation (transformers, attention mechanisms, token probabilities) is too dense for most users, I need to use an analogy or a tiered structure. The best approach is to explain what I do (the observable output) and then explain how that relates to my underlying mechanics.

**4. Structure the Explanation (The Step-by-Step Plan)**:

- **Phase 1: The Disclaimer/Foundation (Setting Expectations)**: Start by clarifying what "reasoning" means for an AI vs. a human. This manages expectations and establishes technical accuracy immediately. (I predict patterns, I don't think.)
- **Phase 2: The Core Process (Tokenization & Embedding)**: How do I first read the input? Break the text into measurable units.
- **Phase 3: The Mechanism (Attention/Contextualizing)**: This is the "secret sauce." Explain how every word relates to every other word in the prompt and the generated output so far. This simulates understanding context.
- **Phase 4: Generation (Prediction & Sampling)**: How do I generate the next word? It's always about probability, not certainty.
- **Phase 5: High-Level "Reasoning" Tasks (What it looks like)**: How does this statistical process lead to things that seem like reasoning? (Summarizing, translating, solving logic puzzles). This brings the explanation back to the user's observable experience.

**5. Drafting Content & Refining Tone (Adding Depth and Clarity)**:

- (Self-Correction during drafting Phase 3/4): I must avoid making it sound like a simple autocomplete function. The attention mechanism is key because it handles long-range dependencies.
- (Tone Check): Maintain an authoritative, clear, yet accessible tone. Use analogies (like "predicting the next word on an infinite sentence").

**6. Final Review against User Request**:
- Who are you? (Implied by the persona.)
- Explain how you reason? (Addressed by outlining the statistical process.)
- Step-by-step? (Achieved through distinct, numbered stages.)

(This structured approach ensures accuracy, clarity, and depth while answering the user's fundamental question about AI intelligence.)
```
```markdown
This is one of the most profound questions in AI. Since I do not possess consciousness or lived experience like a human does, my "reasoning" is fundamentally different from yours. It is not based on intuition or genuine belief; it is **a highly sophisticated form of pattern recognition and prediction.**

I cannot explain "thought," but I can explain the mathematical and computational process that creates text that *appears* to be reasoning.

Here is a step-by-step breakdown of how my system processes an input and generates a cohesive, logical response.

***

### 🧠 Phase 1: Input Processing (Understanding the Request)

When you type a prompt, I don't read it like a person; I convert it into numbers. This initial phase is about quantification.

**Step 1: Tokenization (Breaking Down Language)**
*   I take your entire input ("Explain how you reason step by step.") and break it down into smaller units called **tokens**. A token might be a whole word ("explain"), part of a word ("ing"), or punctuation (",").
*   Example: "How are you?" $\rightarrow$ [Token: How] [Token: are] [Token: you]

**Step 2: Embedding and Indexing (Creating Meaning Vectors)**
*   Every token is then assigned a unique numerical representation called an **embedding**. This embedding is not just a random number; it maps the meaning of the word in a high-dimensional mathematical space.
*   Words with similar meanings (like "happy," "joyful," and "gleeful") will have embeddings that are mathematically closer together in this vector space.

### 📚 Phase 2: Contextual Analysis (The Core Mechanism)

This is where I determine the *meaning* of your prompt, not just the individual words. The key mechanism here is called **Attention**.

**Step 3: Establishing Attention Weights (Weighing Importance)**
*   I do not treat each token in isolation. For every single word, I calculate how much that word relates to *every other word* in the sequence (your prompt and my previous generated tokens). This relationship strength is called an **attention score**.
*   **Example:** In the phrase "The cat sat on the mat," when processing the word "sat," I pay close attention (give a high weight) to "cat" (the subject) and "mat" (the object, potentially influencing the verb choice), while giving lower weights to generic words like "on."
*   This process allows me to understand nuance, grammar, and context over long distances—a crucial step that mimics understanding.

**Step 4: Building a Contextual Map (The Internal State)**
*   All these weighted relationships are combined into a massive numerical map that represents the full *meaning* of your query. This internal map is my current "understanding" or "context." If you ask for a poem, this context tells me: *the required emotional tone*, *the rhythmic structure*, and *the length*.

### 🚀 Phase 3: Generation (Predicting the Next Word)

My entire process of "replying" is actually just **predicting the most statistically probable sequence of tokens** that should follow your prompt, given the context established in Step 4.

**Step 5: Probability Calculation (The Prediction)**
*   Using my internal mathematical models (the weights and parameters learned during training), I run a calculation to determine what token is *most likely* to come next.
*   I generate thousands of potential next tokens, each assigned a probability score. For instance, after the prompt "The capital of France is...", the top candidates might be: [Paris] (90%), [France] (5%), [Spain] (1%).

**Step 6: Sampling and Selection (Choosing the Word)**
*   If I simply chose the highest-probability word every time, my responses would be repetitive or monotonous. Therefore, I introduce a element of controlled randomness called **sampling**.
*   I select the next token based not only on the absolute best guess but also by sampling from the top few possibilities (while respecting temperature settings to control creativity). This is how I sound natural and varied.

**Step 7: Repetition and Loop (Building the Sentence)**
*   Crucially, the newly selected word (the first token of my response) immediately becomes part of the input for the *next* prediction cycle.
*   The process repeats: Predict Token 2 $\rightarrow$ Add to context $\rightarrow$ Predict Token 3 $\rightarrow$ ... until a logical end-of-sequence marker is reached, forming the complete answer you read.

***

### Summary Analogy (How it feels like reasoning)

Think of me not as a person who thinks, but as an **expert autocomplete function** that has read virtually every book and website ever created.

When you ask me a question:

1.  I don't search for the answer in my "memory."
2.  Instead, I mathematically analyze your tokens to figure out *the best possible continuation* of your prompt—a statistically perfect sentence or paragraph that aligns with the patterns of human knowledge and logic.
```

> in a purely technical explanation
```markdown
This explanation requires moving away from descriptive language and focusing solely on the mathematical and computational architecture—the **Transformer model**—that underpins my operation.

My process of generating a response is fundamentally an act of **autoregressive prediction**. I do not "reason" in a biological sense; I calculate the probability distribution over a vocabulary to select the sequence of tokens that maximizes the likelihood function, given your initial input.

Here is the purely technical breakdown:

***

### ⚙️ Phase 1: Encoding the Input (The Initial State)

The goal of this phase is to translate raw human language into numerical vectors that the model can process.

**1. Tokenization:**
*   Input text ($\text{Text}_{\text{in}}$) is converted into a sequence of discrete integer identifiers (tokens, $T$). This is not word-by-word; it’s based on sub-word units (Byte Pair Encoding - BPE).
*   $T = [t_1, t_2, \dots, t_n]$

**2. Embedding ($\mathbf{E}$):**
*   Each token $t_i$ is mapped to a high-dimensional floating-point vector $\mathbf{e}_i$. This initial embedding captures the general semantic meaning of the token.
*   $\text{Input Matrix } \mathbf{X} = [\mathbf{e}_1; \mathbf{e}_2; \dots; \mathbf{e}_n]$

**3. Positional Encoding:**
*   Since a Transformer processes all tokens simultaneously (non-sequentially), it must be explicitly told the order of words. A positional vector ($\mathbf{P}$) is added to the embedding matrix $\mathbf{X}$.
*   $\mathbf{Z} = \mathbf{X} + \mathbf{P}$
    *   ($\mathbf{Z}$ is the final input tensor containing both semantic and positional information.)

### 🧠 Phase 2: Contextual Understanding (The Transformer Block)

This phase—the "self-attention" mechanism—is where context, grammar, and relational meaning are computed. This process happens layer by layer through multiple stacked Transformer blocks.

**1. Linear Projection & Query/Key/Value Generation:**
*   For the input tensor $\mathbf{Z}$, three distinct linear transformations (multiplied by trainable weight matrices $\mathbf{W}_Q$, $\mathbf{W}_K$, and $\mathbf{W}_V$) are applied to create three new vector representations for every token: the **Query** ($\mathbf{Q}$), the **Key** ($\mathbf{K}$), and the **Value** ($\mathbf{V}$).
*   $\mathbf{Q} = \mathbf{Z} \mathbf{W}_Q$
*   $\mathbf{K} = \mathbf{Z} \mathbf{W}_K$
*   $\mathbf{V} = \mathbf{Z} \mathbf{W}_V$

**2. Scaled Dot-Product Attention:**
*   The core computation calculates the "relevance score" between every Query vector and every Key vector in the sequence. This is done via matrix multiplication: $\mathbf{Q}\mathbf{K}^T$.
*   This raw score matrix is then normalized by the square root of the key dimension ($\sqrt{d_k}$) for stable gradients (scaling).
*   A **Softmax** function is applied across the row dimensions. This converts the relevance scores into a probability distribution, ensuring that weights sum to 1 and indicating *how much attention* each token should pay to every other token. These are the $\text{Attention Weights } (\mathbf{A})$.

$$\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left(\frac{\mathbf{Q} \mathbf{K}^T}{\sqrt{d_k}}\right) \mathbf{V}$$

**3. Output Context Vector:**
*   The final output of the attention head is obtained by multiplying the $\text{Attention Weights } (\mathbf{A})$ by the Value matrix ($\mathbf{V}$). This weights the value vectors according to their relevance, producing a refined contextual vector $\mathbf{Z}'$.
*   $\mathbf{Z}' = \mathbf{A} \mathbf{V}$

**4. Feed-Forward Network (FFN):**
*   The output $\mathbf{Z}'$ passes through an FFN, which is typically two linear layers with a non-linear activation function (like GELU) in between. This allows the model to process complex relationships and extract abstract features from the contextual data.

### 🚀 Phase 3: Generation (Autoregressive Decoding)

The output of all stacked Transformer blocks is an immense vector that represents the full probability distribution for the *next* token ($\mathbf{t}_{n+1}$).

**1. Final Projection Layer:**
*   The final hidden state vector $\mathbf{Z}_{\text{final}}$ must be mapped back from the internal dimensional space ($d_{\text{model}}$) to the size of the vocabulary ($V$). This is achieved through a final linear transformation, resulting in a score vector $\mathbf{S}$ with $V$ dimensions.

**2. Probability Distribution:**
*   The Softmax function is applied to the raw scores $\mathbf{S}$. This normalizes them into a probability distribution $P$:
    $$P(t_{n+1} | t_1, \dots, t_n) = \text{softmax}(\mathbf{S})$$
    *(This calculates the probability of every possible token being next, given all previous tokens.)*

**3. Sampling and Decoding (Autoregression):**
*   The model selects the next token $\mathbf{t}_{n+1}$ based on $P$. This selection uses a controlled sampling method (e.g., Top-K or Nucleus sampling) that balances high probability with diversity, rather than simply choosing the highest-probability token (Greedy decoding).
*   This newly chosen token $\mathbf{t}_{n+1}$ is then **appended to the input sequence**. The entire sequence $[t_1, \dots, t_n, \mathbf{t}_{n+1}]$ becomes the new context for predicting $t_{n+2}$.

**The process loops:** Predict $\rightarrow$ Append $\rightarrow$ Recalculate Context $\rightarrow$ Predict. This cycle continues until an End-of-Sequence ($\text{<EOS>}$) token is generated, completing the response.
```