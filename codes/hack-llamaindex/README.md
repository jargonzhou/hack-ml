# Hack LlamaIndex

Setup
```shell
$ uv add pip ipykernel jupyter
$ uv add python-dotenv
$ uv add pandas

# LlamaIndex
$ uv add llama-index
# LlamaIndex - readers
$ uv add llama-index-readers-web
$ uv add llama-index-readers-database

# with Hugging Face
$ uv add llama-index-llms-huggingface # for local inference
$ uv add "transformers[torch]" 
$ uv add timm
# $ uv add llama-index-llms-huggingface-api # for remote inference
# $ uv add "huggingface_hub[inference]"
$ uv add llama-index-embeddings-huggingface

# with Ollama
$ uv add llama-index-llms-ollama llama-index-embeddings-ollama

# with LM Studio
$ uv add llama-index-llms-lmstudio

$ uv add streamlit
$ uv add pypdf
# $ uv add docx2txt

# Wikipedia
$ uv add wikipedia llama-index-readers-wikipedia
# YAML
$ uv add pyyaml

# Vector store
$ uv add llama-index-vector-stores-chroma

# Rank-BM25: A two line search engine
$ uv add rank_bm25
$ uv add llama-index-retrievers-bm25

# Program
$ uv add llama-index-program-evaporate
$ llama-index-program-openai

# Streamlit
$ uv add streamlit

# IngestionPipeline.run() Detected nested async
$ uv add nest_asyncio

# SQL
$ uv add sqlalchemy pyodbc

# Console
$ uv add rich
```

# Building Data-Driven Applications with LlamaIndex

- [app/pits](./app/pits/__init__.py)

# Streamlit for Web Development

- [app_st](./app_st/__init__.py)

```shell
$ streamlit version
Streamlit, version 1.58.0
```

- [c03_page_organization.py](./app_st/c03_page_organization.py)
- [c03_placeholder.py](./app_st/c03_placeholder.py)
- [c03_progress_bar.py](./app_st/c03_progress_bar.py)
- [c03_navigation.py](./app_st/c03_navigation.py): `nav/*.py`
- [social_network/main.py](./app_st/social_network/main.py)
- [c03_fragmenting.py](./app_st/c03_fragmenting.py)