# Hugging Face in Action

# 1 Introducing Hugging Face
# 2 Getting started
# 3 Using Hugging Face transformers and pipelines for NLP tasks
# 4 Using Hugging Face for computer vision tasks
# 5 Exploring, tokenizing, and visualizing Hugging Face datasets
# 6 Fine-tuning pretrained models and working with multimodal models
# 7 Creating LLM-based applications using LangChain and LlamaIndex
# 8 Building LangChain applications visually using Langflow
# 9 Programming agents
# 10 Building a web-based UI using Gradio
# 11 Building locally running LLM-based applications using GPT4All
# 12 Using LLMs to query your local data

# 13 Bridging LLMs to the real world with the Model Context Protocol
```shell
$ uv init c13_mcp
$ cd c13_mcp
$ uv add "mcp[cli]" httpx PyMuPDF

$ uv run main.py

# MCP inspector
$ uv run mcp dev main.py
```