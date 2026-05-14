# Hack LLM

# Hugging Face in Action
Setup
```shell
$ uv add pip ipykernel jupyter

$ uv add transformers
$ uv add transformers[serving] # serving models
$ uv add datasets

$ uv add torch # torchvision torchaudio
$ uv add timm
# more: GPUtil

$ uv add huggingface_hub
$ uv add huggingface_hub[inference] # ???

# LangChain
$ uv add langchain
$ uv add langchain-huggingface
$ uv add langchain-openai
$ uv add langchain-community
$ uv add langgraph
$ uv add --dev langgraph-cli

# LLM Serving
$ uv add ollama

# LlamaIndex
$ uv add llama_index
$ uv add llama-index-embeddings-huggingface
$ uv add llama-index-llms-huggingface # "transformers[torch]>=4.37.0,<5", https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/llms/llama-index-llms-huggingface/pyproject.toml

# Agents
$ uv add smolagents
$ uv add smolagents[litellm]
$ uv add ddgs

# Gradio
$ uv add gradio

# TODO: GPT4ALL

# MCP
$ uv add "mcp[cli]" httpx PyMuPDF

$ uv add pandas
$ uv add matplotlib
$ uv add scikit-learn
$ uv add scikit-image

$ uv add python-dotenv
```

- 1. Introducing Hugging Face
- 2. Getting started
- 3. Using Hugging Face transformers and pipelines for NLP tasks
- 4. Using Hugging Face for computer vision tasks
- 5. Exploring, tokenizing, and visualizing Hugging Face datasets
- 6. Fine-tuning pretrained models and working with multimodal models
- 7. Creating LLM-based applications using LangChain and LlamaIndex
- 8. Building LangChain applications visually using Langflow
- 9. Programming agents
- 10. Building a web-based UI using Gradio
- 11. Building locally running LLM-based applications using GPT4All
- 12. Using LLMs to query your local data

- 13. Bridging LLMs to the real world with the Model Context Protocol
```shell
$ uv add "mcp[cli]" httpx PyMuPDF

$ uv run main.py

# MCP inspector
$ uv run mcp dev main.py
```

# Learning LangChain
Setup
```shell
$ uv add langchain langchain-openai langchain-community langchain-text-splitters langchain-postgres
$ uv add langchain-ollama langchain-mcp-adapters
$ uv add langgraph
```

- 1. LLM Fundamentals with LangChain: `app\langchain\app_langchain_fundamentals_ollama.py`
- 2. RAG Part I: Indexing Your Data
- 3. RAG Part II: Chatting with Your Data
- 4. Using LangGraph to Add Memory to Your Chatbot
- 5. Cognitive Architectures with LangGraph
- 6. Agent Architecture
- 7. Agents II
- 8. Patterns to Make the Most of LLMs
- 9. Deployment: Launching Your AI Application into Production

```shell
### 1. Deep Agent
$ langgraph new app_langgraph_deep_agent
🌟 Please select a template:
1. Deep Agent - An opinionated deployment template for a Deep Agent.
2. Agent - A simple agent that can be flexibly extended to many tools.
3. New LangGraph Project - A simple, minimal chatbot with memory.
Enter the number of your template choice (default is 1): 1

You selected: Deep Agent - An opinionated deployment template for a Deep Agent.
Choose language (1 for Python 🐍, 2 for JS/TS 🌐): 1
📥 Attempting to download repository as a ZIP archive...
URL: https://github.com/langchain-ai/deep-agent-template/archive/refs/heads/main.zip
✅ Downloaded and extracted repository to ...\app_langgraph_deep_agent
🎉 New project created at ...\app_langgraph_deep_agent

### 2. Agent
$ langgraph new app_langgraph_agent
🌟 Please select a template:
1. Deep Agent - An opinionated deployment template for a Deep Agent.
2. Agent - A simple agent that can be flexibly extended to many tools.
3. New LangGraph Project - A simple, minimal chatbot with memory.
Enter the number of your template choice (default is 1): 2

You selected: Agent - A simple agent that can be flexibly extended to many tools.
📥 Attempting to download repository as a ZIP archive...
URL: https://github.com/langchain-ai/simple-agent-template/archive/refs/heads/main.zip
✅ Downloaded and extracted repository to ...\app_langgraph_agent
🎉 New project created at ...\app_langgraph_agent

### 3. New LangGraph Project
$ langgraph new app_langgraph
🌟 Please select a template:
1. Deep Agent - An opinionated deployment template for a Deep Agent.
2. Agent - A simple agent that can be flexibly extended to many tools.
3. New LangGraph Project - A simple, minimal chatbot with memory.
Enter the number of your template choice (default is 1): 3

You selected: New LangGraph Project - A simple, minimal chatbot with memory.
Choose language (1 for Python 🐍, 2 for JS/TS 🌐): 1
📥 Attempting to download repository as a ZIP archive...
URL: https://github.com/langchain-ai/new-langgraph-project/archive/refs/heads/main.zip
✅ Downloaded and extracted repository to ...\app_langgraph
🎉 New project created at ...\app_langgraph

$ langgraph dev
INFO:langgraph_api.cli:

        Welcome to

╦  ┌─┐┌┐┌┌─┐╔═╗┬─┐┌─┐┌─┐┬ ┬
║  ├─┤││││ ┬║ ╦├┬┘├─┤├─┘├─┤
╩═╝┴ ┴┘└┘└─┘╚═╝┴└─┴ ┴┴  ┴ ┴

- 🚀 API: http://127.0.0.1:2024
- 🎨 Studio UI: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
- 📚 API Docs: http://127.0.0.1:2024/docs

This in-memory server is designed for development and testing.
For production use, please use LangSmith Deployment.
```

- 10. Testing: Evaluation, Monitoring, and Continuous Improvement
- 11. Building with LLMs