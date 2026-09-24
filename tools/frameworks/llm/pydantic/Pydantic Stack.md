# Pydantic Stack
* https://pydantic.dev/
* https://github.com/pydantic

# Meet the Pydantic Stack

- Pydantic AI
  - Agent Framework, Graphs, MCP
- Pydantic Validation
  - Data Validation, Type Hints
- Pydantic Evals
  - Evals, Assertions, Code-first
- Pydantic Logfire
  - OpenTelemetry, Logs, Traces, Metrics
- Pydantic AI Gateway
  - LLM Routing, FinOps, BYOK, OpenTelemetry

# Pydantic AI
* https://pydantic.dev/pydantic-ai
* https://pydantic.dev/docs/ai/overview/

Pydantic AI is a Python agent framework designed to help you quickly, confidently, and painlessly build production grade applications and workflows with Generative AI.
We built Pydantic AI with one simple aim: to bring that FastAPI feeling to GenAI app and agent development.

Why use Pydantic AI
1. **Built by the Pydantic Team**: [Pydantic Validation](https://docs.pydantic.dev/latest/) is the validation layer of the OpenAI SDK, the Google ADK, the Anthropic SDK, LangChain, LlamaIndex, AutoGPT, Transformers, CrewAI, Instructor and many more. _Why use the derivative when you can go straight to the source?_ 😃
2. **Model-agnostic**: Supports virtually every [model](https://pydantic.dev/docs/ai/models/overview) and provider: OpenAI, Anthropic, Gemini, DeepSeek, Grok, Cohere, Mistral, and Perplexity; Azure AI Foundry, Amazon Bedrock, Google Cloud, Ollama, LiteLLM, Groq, OpenRouter, Together AI, Fireworks AI, Cerebras, Hugging Face, GitHub, Heroku, Vercel, Nebius, OVHcloud, Alibaba Cloud, and SambaNova. If your favorite model or provider is not listed, you can easily implement a [custom model](https://pydantic.dev/docs/ai/models/overview#custom-models).
3. **Seamless Observability**: Tightly [integrates](https://pydantic.dev/docs/ai/integrations/logfire) with [Pydantic Logfire](https://pydantic.dev/logfire), our general-purpose OpenTelemetry observability platform, for real-time debugging, evals-based performance monitoring, and behavior, tracing, and cost tracking. If you already have an observability platform that supports OTel, you can [use that too](https://pydantic.dev/docs/ai/integrations/logfire#alternative-observability-backends).
4. **Fully Type-safe**: Designed to give your IDE or AI coding agent as much context as possible for auto-completion and [type checking](https://pydantic.dev/docs/ai/core-concepts/agent#static-type-checking), moving entire classes of errors from runtime to write-time for a bit of that Rust “if it compiles, it works” feel.
5. **Powerful Evals**: Enables you to systematically test and [evaluate](https://pydantic.dev/docs/ai/evals/) the performance and accuracy of the agentic systems you build, and monitor the performance over time in Pydantic Logfire.
6. **Extensible by Design**: Build agents from composable [capabilities](https://pydantic.dev/docs/ai/core-concepts/capabilities) that bundle tools, hooks, instructions, and model settings into reusable units. Use built-in capabilities for [web search](https://pydantic.dev/docs/ai/core-concepts/capabilities#provider-adaptive-tools), [thinking](https://pydantic.dev/docs/ai/core-concepts/capabilities#thinking), and [MCP](https://pydantic.dev/docs/ai/core-concepts/capabilities#provider-adaptive-tools), pick from the [Pydantic AI Harness](https://pydantic.dev/docs/ai/harness/overview) capability library, build your own, or install [third-party capability packages](https://pydantic.dev/docs/ai/guides/extensibility). Define agents entirely in [YAML/JSON](https://pydantic.dev/docs/ai/core-concepts/agent-spec) — no code required.
7. **MCP, A2A, and UI**: Integrates the [Model Context Protocol](https://pydantic.dev/docs/ai/mcp/overview), [Agent2Agent](https://pydantic.dev/docs/ai/integrations/a2a), and various [UI event stream](https://pydantic.dev/docs/ai/integrations/ui/overview) standards to give your agent access to external tools and data, let it interoperate with other agents, and build interactive applications with streaming event-based communication.
8. **Human-in-the-Loop Tool Approval**: Easily lets you flag that certain tool calls [require approval](https://pydantic.dev/docs/ai/tools-toolsets/deferred-tools#human-in-the-loop-tool-approval) before they can proceed, possibly depending on tool call arguments, conversation history, or user preferences.
9. **Durable Execution**: Enables you to build [durable agents](https://pydantic.dev/docs/ai/integrations/durable_execution/overview) that can preserve their progress across transient API failures and application errors or restarts, and handle long-running, asynchronous, and human-in-the-loop workflows with production-grade reliability.
10. **Streamed Outputs**: Provides the ability to [stream](https://pydantic.dev/docs/ai/core-concepts/output#streamed-results) structured output continuously, with immediate validation, ensuring real time access to generated data.
11. **Graph Support**: Provides a powerful way to define [graphs](https://pydantic.dev/docs/ai/graph/) using type hints, for use in complex applications where standard control flow can degrade to spaghetti code.


# Pydantic Validation
* https://pydantic.dev/docs/validation/latest/get-started/

Pydantic is the most widely used data validation library for Python.

Why use Pydantic?
- **Powered by type hints**: with Pydantic, schema validation and serialization are controlled by type annotations; less to learn, less code to write, and integration with your IDE and static analysis tools.
- **Speed**: Pydantic’s core validation logic is written in Rust. As a result, Pydantic is among the fastest data validation libraries for Python.
- **JSON Schema**: Pydantic models can emit JSON Schema, allowing for easy integration with other tools.
- **Strict and Lax mode**: Pydantic can run in either strict mode (where data is not converted) or lax mode where Pydantic tries to coerce data to the correct type where appropriate.
- **Dataclasses, TypedDicts and more**: Pydantic supports validation of many standard library types including `dataclass` and `TypedDict`.
- **Customisation**: Pydantic allows custom validators and serializers to alter how data is processed in many powerful ways.
- **Ecosystem**: around 8,000 packages on PyPI use Pydantic, including massively popular libraries like FastAPI, huggingface, Django Ninja, SQLModel, & LangChain.
- **Battle tested**: Pydantic is downloaded over 550M times/month and is used by all FAANG companies and 20 of the 25 largest companies on NASDAQ. If you’re trying to do something with Pydantic, someone else has probably already done it.

```shell
pip install pydantic
```

# Pydantic Evals
* https://pydantic.dev/docs/ai/evals/evals/

Pydantic Evals is a powerful evaluation framework for systematically testing and evaluating AI systems, from simple LLM calls to complex multi-agent applications.

data model
```
Dataset (1) ──────────── (Many) Case
│                        │
│                        │
└─── (Many) Experiment ──┴─── (Many) Case results
     │
     └─── (1) Task
     │
     └─── (Many) Evaluator
```

```shell
pip install pydantic-evals
```

# Pydantic Logfire
* https://pydantic.dev/logfire
* https://pydantic.dev/docs/logfire/get-started/

Monitor your entire AI application stack, not just the LLM calls. 
Logfire is a production-grade observability platform for AI and general applications. 
See LLM interactions, agent behavior, API requests, and database queries in one unified trace. 
With SDKs for Python, JavaScript/TypeScript, and Rust, Logfire works with all OpenTelemetry-compatible languages.

```shell
pip install logfire
```

# Pydantic AI Gateway
* https://pydantic.dev/ai-gateway
* https://pydantic.dev/docs/ai/overview/gateway/

Pydantic AI Gateway is a unified interface for accessing multiple AI providers with a single key, managed through Pydantic Logfire. Features include built-in OpenTelemetry observability, real-time cost monitoring, failover management, and native integration with the other tools in the Pydantic stack.

```shell
pip install pydantic-ai
```

# See Also
