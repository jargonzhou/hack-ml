# Ragas
* https://github.com/vibrantlabsai/ragas

Objective metrics, intelligent test generation, and data-driven insights for LLM apps

Ragas is your ultimate toolkit for evaluating and optimizing Large Language Model (LLM) applications. Say goodbye to time-consuming, subjective assessments and hello to data-driven, efficient evaluation workflows. Don't have a test dataset ready? We also do production-aligned test set generation.

Key Features
- 🎯 Objective Metrics/客观度量指标: Evaluate your LLM applications with precision using both LLM-based and traditional metrics.
- 🧪 Test Data Generation/测试数据生成: Automatically create comprehensive test datasets covering a wide range of scenarios.
- 🔗 Seamless Integrations/无缝集成: Works flawlessly with popular LLM frameworks like LangChain and major observability tools.
- 📊 Build feedback loops/构建反馈循环: Leverage production data to continually improve your LLM applications.

```shell
$ pip install ragas
$ pip install ragas[examples]

$ ragas quickstart
```

# 🚀 Get Started
* https://docs.ragas.io/en/stable/getstarted/quickstart/

```python
from ragas import Dataset
from ragas.metrics import DiscreteMetric
from ragas.llms import llm_factory
```

Tutorials: https://github.com/vibrantlabsai/ragas/tree/main/examples
- Evaluate a prompt
```python
# python -m ragas_examples.prompt_evals.prompt

from ragas.metrics import discrete_metric
from ragas.metrics.result import MetricResult

from ragas import experiment
```
- Evaluate a simple RAG system
```python
# python -m ragas_examples.rag_eval.rag
```
- Evaluate an AI Workflow
```python
# python -m ragas_examples.workflow_eval.workflow
```
- Evaluate an AI Agent
```python
# python -m ragas_examples.agent_evals.agent
```

# 📚 Core Concepts
* https://docs.ragas.io/en/stable/concepts/


- Experimentation/实验
  - components: test dataset, application endpoint, metrics
  - executions process: setup, run, evaluate, store
  - `@experiment`, `arun(dataset, ...)`
- Datasets/数据集
  - evaluation datasets: `datasets`
    - inputs, expected outputs, metadata
  - evaluation results: `experiments`
    - dataset attributes, response from evaluated system, result of metrics, metadata
  - `from ragas import Dataset` 
- Metrics/指标
  - End-to-End Metrics/端到端指标
    - ex: Answer correctness, Citation accuracy
  - Component-Level Metrics/组件级指标
    - ex: Retrieval accuracy
  - Business Metrics/业务指标
    - ex: Ticket deflection rate
  - in Ragas
    - LLM based `MetricWithLLM`
      - single turn: faithffulness
      - multi turn: agent goal accuracy
    - Non-LLM based `Metric`
      - single turn: BLEU Score
      - multi turn
    - output type
      - discrete metrics: `from ragas.metrics import discrete_metric`
      - numeric metrics: `from ragas.metrics import numeric_metric`
      - ranking metrics: `from ragas.metrics import ranking_metric`
- Test Data Generation/测试数据生成
  - RAG
  - Agents or tool use
- Components/组件
  - General
    - Prompt
  - Evaluation
    - Evaluation Sample
    - Evaluation Dataset

## Available Metrics

RAG
- context precision/上下文精确度
- context recall/上下文召回率
- context entities recall/上下文实体召回率
- noise sensitivity/噪声敏感度
- response relevancy/响应相关性
- faithfulness/忠实度

Nvidia Metrics
- answer accuracy/答案准确率
- context relevance/上下文相关性
- response groundedness/响应接地性

Agents or Tool Use Cases
- topic adherence/主题依从性
- tool call accuracy/工具调用准确率
- tool call F1
- agent goal accuracy/智能体目标准确率

Natural Lanaguage Comparison
- factual correctness/事实正确性
- semantic similiarity/语义相似度
- Non-LLM metrics
  - string similiarity/字符串相似度
  - BLEU Score: Bilingual Evaluation Understudy/双语评估辅助工具
  - CHRF Score: Character n-gram F-score/字符n-gram F分数
  - ROUGE Score: Recall-Oriented Understudy for Gisting Evaluation/面向召回率的概要评估辅助工具
  - String Presence/字符串存在性
  - Exact match/精确匹配

SQL
- execution based
  - DataCompy Score: DataCompy, a python library that compares two pandas DataFrames.
- non-execution based
  - SQL Semantic Equivalence/SQL语义等价性

General Purpose
- aspect critic/方面评价器
- simple criteria scoring/简单评分标准
- rubrics based criteria scoring/基于评分规则的评分标准
- instance specific rubrics criteria scoring/基于实例的评分规则

Other Tasks
- summarization score/总结评分

## Test Data Generation

RAG
- query types in RAG
  - single-hop query, multi-hop query
  - specific query, abstract query
- knowledge graph creation
  - document splitter
  - extractor
  - relationship builder
  - transform
- scenario generation
  - parameters: nodes, query length, query style, persona
  - query synthesizer

Agents or tool use
- upcoming...

# 🛠️ How-to Guides
* https://docs.ragas.io/en/stable/howtos/

Customization
- General
  - customise models
  - run config
  - caching
  - cancelling tasks
- LLM Adapters: use multiple structured output backends
- Metrics
  - modify prompts in metrics
- Testset Generation
  - non-English testset generation
  - persona generation
  - custom single-hop query
  - custom multi-hop query
  - use pre-chunked data
- Optimizers
  - DSPyOptimizer: DSPy's MIPROv2(Multi-prompt Instruction Proposal with Ranked Outcomes)/带排序结果的多提示教学方案指令提案

Applications
- prompt evaluation
  - iterate and improve prompts
  - systematic prompt optimization
- metrics
  - cost analysis
  - evaluate multi-turn conversations
- testset generation
  - single-hop query testset
- benchmarking
  - evaluate a new LLM for your use case
- agent evaluation
  - evaluate a text-to-SQL agent
  - align an LLM as a Judge
- RAG evaluation
  - evaluate and import a RAG app

CLI
- RAG Evaluation
- Improve RAG
  - MLflow

Integration
- Observability
  - Arize AI's Phoenix
  - LangSmith
- LLM Prodivers
  - Amazon Bedrock
  - Google Gemini
  - OCI Gen AI
- Frameworks
  - AG-UI
  - Griptape
  - Haystack
  - LangChain
  - LangGraph
  - LlamaIndex
  - LlamaIndex Agents
  - LlamaStack
  - R2R
  - Swarm

# 📖 References
* https://docs.ragas.io/en/stable/references/

Core Components
- **Prompt**: Core prompt management and templating
- **LLMs**: Language model interfaces and configurations
- **Embeddings**: Embedding model interfaces and utilities
- **Tokenizers**: Tokenizer interfaces for text splitting
- **RunConfig**: Evaluation runtime configuration
- **Executor**: Execution engine for evaluations
- **Cache**: Caching mechanisms for LLM calls

Evaluation
- **Schemas**: Data structures for evaluation
- **Metrics**: Available metrics and their implementations
- `evaluate()`, `aevaluate()`: Main evaluation function API

Testset Generation
- **Schemas**: Data structures for test data
- **Graph**: Knowledge graph creation and management
- **Transforms**: Data transformation utilities
- **Synthesizers**: Test data generation components
- **Generation**: Test data generation API

Integrations
- **Integrations**: APIs for external tool integrations


# See Also
