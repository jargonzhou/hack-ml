# Deep Agents Template

Deployment template for a deep agent built with `create_deep_agent(...)`.

Setup
```shell
$ uv add langchain-ollama
```

Tests
- Input: HUMAN> 请帮我检索最新大模型架构趋势，并输出一份深度报告存到文件里
- Output: AI> 我已经为您检索并分析了 2024-2025 年大模型架构的最前沿趋势，并撰写了一份深度技术报告。
报告已保存至文件：/llm_architecture_trends_2025.md ...


## What this template gives you

- A deployable deep agent graph at `src/deep_agent/graph.py`.
- Explicit workflow prompt (plan, delegate, critique, finalize).
- Two predefined sub-agents (`researcher`, `critic`).
- Human-in-the-loop interrupts on `execute` and `write_file`.
- A `uv`-managed local workflow with a small `Makefile` wrapper and starter tests.

## Prerequisites

- An API key for your model provider (Anthropic by default)
- A [LangSmith](https://smith.langchain.com/) account (Plus plan or higher) to deploy

## Quickstart

1. Sync the project and configure environment:

```bash
uv sync
cp .env.example .env
```

2. Start the dev server:

```bash
uv run langgraph dev
```

3. Deploy to LangSmith:

```bash
uv run langgraph deploy
```

See the [CLI docs](https://docs.langchain.com/langsmith/cli#deploy) for deploy options.

To set up CI instead, push this repo to GitHub and configure your deployment through the LangSmith UI.

## Tests and lint

```bash
make test
make integration-tests
make lint
make format
```

Integration tests are skipped unless `ANTHROPIC_API_KEY` is set.

## Reference docs

- Deep Agents overview: https://docs.langchain.com/oss/python/deepagents/overview
- Deep Agents quickstart: https://docs.langchain.com/oss/python/deepagents/quickstart
- LangSmith CLI: https://docs.langchain.com/langsmith/cli
