# LangChain
* https://www.langchain.com/
* https://en.wikipedia.org/wiki/LangChain

> LangChain is a software framework that helps facilitate the integration of large language models (LLMs) into applications. As a **language model integration framework/语言模型集成框架**, LangChain's use-cases largely overlap with those of language models in general, including document analysis and summarization, chatbots, and code analysis.

# Core Components
- Agents
- Models
- Messages
- Tools
- Short-term memory
- Streaming
- Structured output


```shell
pip install langchain
pip install langchain-ollama
pip install langchain-community
pip install langchain-postgres

pip install langchain-mcp-adapters
pip install langchain-tests
pip install langchain-text-splitters
```

# Deep Agents
* https://docs.langchain.com/oss/python/deepagents/overview

Deep agents are the easiest way to **start building agents and applications powered by LLMs**—with built-in capabilities for task planning, file systems for context management, subagent-spawning, and long-term memory. You can use deep agents for any task, including complex, multi-step tasks.

# LangGraph
* https://docs.langchain.com/oss/python/langgraph/overview

LangGraph is a low-level **orchestration framework and runtime/编排框架和运行时** for building, managing, and deploying long-running, stateful agents.

# Integrations
* https://reference.langchain.com/python/integrations/overview

LangChain packages to connect with popular LLM providers, vector stores, tools, and other services.

[All LangChain Python integration providers](https://docs.langchain.com/oss/python/integrations/providers/all_providers)

# LangSmith
* https://docs.langchain.com/langsmith/home

LangSmith is a platform that helps AI teams use live production data for continuous testing and improvement. LangSmith provides:
- **Observability**: See exactly how your agent thinks and acts with detailed tracing and aggregate trend metrics.
- **Evaluation**: Test and score agent behavior on production data or offline datasets to continuously improve performance.
- **Prompt Engineering**: Iterate on prompts with version control, prompt optimization, and collaboration features.
- **Deployment**: Ship your agent in one click, using scalable infrastructure built for long-running tasks.

# MCP Adapter

Use Model Context Protocol (MCP) tools within LangChain and LangGraph applications.

# See Also
* [Awesome LangChain](https://github.com/kyrolabs/awesome-langchain): Awesome list of tools and projects with the awesome LangChain framework.
