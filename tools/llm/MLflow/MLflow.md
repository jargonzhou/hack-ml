# MLflow
* https://mlflow.org/
* https://github.com/mlflow/mlflow

The open source AI engineering platform for agents, LLMs, and ML models. MLflow enables teams of all sizes to debug, evaluate, monitor, and optimize production-quality AI applications while controlling costs and managing access to models and data.

```shell
$ pip install mlflow

# Self-Hosting MLflow
$ mlflow server --port 5000
```

# LLMs & Agents

MLflow provides everything you need to build, debug, evaluate, and deploy production-quality LLM applications and AI agents. Supports Python, TypeScript/JavaScript, Java and any other programming language. MLflow also natively integrates with OpenTelemetry and MCP.
- **Observability/可观测性**: Capture complete traces of your LLM applications and agents for deep behavioral insights. Built on OpenTelemetry, supporting any LLM provider and agent framework. Monitor production quality, costs, and safety.
- **Evaluation/评估**: Run systematic evaluations, track quality metrics over time, and catch regressions before they reach production. Choose from 50+ built-in metrics and LLM judges, or define your own.
- **Prompts & Optimization/提示和优化**: Version, test, and deploy prompts with full lineage tracking. Automatically optimize prompts with state-of-the-art algorithms to improve performance.
- **AI Gateway/AI网关**: Unified API gateway for all LLM providers. Route requests, manage rate limits, handle fallbacks, and control costs through an OpenAI-compatible interface with built-in credential management, guardrails and traffic splitting for A/B testing.

# Model Training

For machine learning and deep learning model development, MLflow provides a full suite of tools to manage the ML lifecycle:
- **Experiment Tracking/实验跟踪** — Track models, parameters, metrics, and evaluation results across experiments
- **Model Evaluation/模型评估** — Automated evaluation tools integrated with experiment tracking
- **Model Registry/模型仓库** — Collaboratively manage the full lifecycle of ML models
- **Deployment/部署** — Deploy models to batch and real-time scoring on Docker, Kubernetes, Azure ML, AWS SageMaker, and more


# See Also