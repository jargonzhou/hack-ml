# Ollama
* https://ollama.com/
* https://github.com/ollama/ollama

> Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.

```shell
# Windows: https://docs.ollama.com/windows
OllamaSetup.exe /DIR="d:\software\Ollama"
# environment variable
OLLAMA_MODELS=D:\llm
```

# Capabilities
## Streaming
Streaming allows you to render text as it is produced by the model.

## Thinking
Thinking-capable models emit a `thinking` field that separates their reasoning trace from the final answer.

## Structured Outputs
Structured outputs let you enforce a JSON schema on model responses so you can reliably extract structured data, describe images, or keep every reply consistent.

## Vision
Vision models accept images alongside text so the model can describe, classify, and answer questions about what it sees.

## Embeddings
Generate text embeddings for semantic search, retrieval, and RAG.

## Tool calling
Ollama supports **tool calling** (also known as **function calling**) which allows a model to invoke tools and incorporate their results into its replies.

## Web search
Ollama’s web search API can be used to augment models with the latest information to reduce hallucinations and improve accuracy.

# API Reference
* https://docs.ollama.com/api/introduction

# Ollama Python library
* https://github.com/ollama/ollama-python

# Integrations

* Coding Agents
  * Claude Code
  * Codex
  * OpenCode
  * Droid
  * Goose
  * Pi
* Assistants
  * OpenClaw
* IDEs & Editors
  * VS Code
  * Cline
  * Roo Code
  * JetBrains
  * Xcode
  * Zed
* Chat & RAG
  * Onyx
* Automation
  * n8n
* Notebooks
  * marimo