# Hugging Face in Action: Build intelligent applications with transformers, agents, and RAG

Actions
* Use Hugging Face models for NLP and computer vision tasks.
* Fine-tune and customize models for your own datasets.
* Build applications powered by LLMs using **LangChain**, **Langflow**, and **LlamaIndex**.
* Design autonomous AI agents that integrate with tools and services.
* Create web interfaces for your models with **Gradio**.
* Run lightweight LLMs locally with **GPT4All**.
* Extend your applications to the real world using MCP.

action: [hugging-face-in-action](../codes/hugging-face-in-action/README.md)

# 1 Introducing Hugging Face
## 1.1 Hugging Face Transformers library
## 1.2 Hugging Face models
## 1.3 Hugging Face Gradio Python library

## 1.4 Understanding the Hugging Face mental model

Figure 1.9 A visual mental model showing Hugging Face’s core process

- Step 1: User need
- Step 2: Model Hub discovery
- Step 3: Model card
- Step 4: Two execution paths
  - Hosted Inference API
  - Direct download
- Step 5: Results delivered

# 2 Getting started
## 2.1 Downloading Anaconda
### 2.1.1 Creating virtual environments
### 2.1.2 Starting Jupyter Notebook

## 2.2 Installing the Transformers library/Transformers库
### 2.2.1 Support for GPU
### 2.2.2 Using GPU in the pipeline object

## 2.3 Installing the Hugging Face Hub package/Hub包
### 2.3.1 Downloading files
### 2.3.2 Using the Hugging Face CLI

# 3 Using Hugging Face transformers and pipelines for NLP tasks/NLP任务
## 3.1 Introduction to the transformer architecture
### 3.1.1 Tokenization
### 3.1.2 Token embeddings
### 3.1.3 Positional encoding
### 3.1.4 Transformer block
### 3.1.5 Softmax

## 3.2 Working with the Transformers library
### 3.2.1 What are pretrained transformers models?
### 3.2.2 What are transformers pipelines?
### 3.2.3 Using a model directly
### 3.2.4 Using a transformers pipeline

## 3.3 Using transformers for NLP tasks
### 3.3.1 Text classification
### 3.3.2 Text generation
### 3.3.3 Text summarization
### 3.3.4 Text translation
### 3.3.5 Zero-shot classification
### 3.3.6 Question-answering tasks

# 4 Using Hugging Face for computer vision tasks/计算机视觉任务
## 4.1 Hugging Face computer vision models
## 4.2 Object detection
### 4.2.1 Using the model directly
### 4.2.2 Using the transformers pipeline
### 4.2.3 Binding to a webcam
## 4.3 Image classification
## 4.4 Image segmentation
### 4.4.1 Using the model programmatically
### 4.4.2 Binding to Gradio
## 4.5 Video classification
### 4.5.1 Installing the prerequisites
### 4.5.2 Downloading the videos for testing
### 4.5.3 Using the transformers pipeline object

# 5 Exploring, tokenizing, and visualizing Hugging Face datasets/分词, 数据集
## 5.1 What are Hugging Face datasets?
### 5.1.1 Getting the list of datasets available
### 5.1.2 Validating the availability of a dataset
### 5.1.3 Downloading a dataset
### 5.1.4 Shuffling a dataset
### 5.1.5 Streaming a dataset
### 5.1.6 Getting the Parquet files of a dataset

## 5.2 Tokenization in NLP
### 5.2.1 Types of tokenization methods
### 5.2.2 Tokenizing datasets

## 5.3 Visualizing datasets
### 5.3.1 Using the twitter-financial-news-topic dataset
### 5.3.2 Using the CIFAR-10 dataset

# 6 Fine-tuning pretrained models and working with multimodal models
## 6.1 Fine-tuning pretrained models/微调预训练模型
### 6.1.1 Loading the yelp_polarity dataset
### 6.1.2 Filtering the yelp_polarity dataset
### 6.1.3 Tokenizing the reduced dataset
### 6.1.4 Setting up a pretrained model for sequence classification
### 6.1.5 Configuring and initializing a trainer for fine-tuning a pretrained model
### 6.1.6 Using the fine-tuned model
### 6.1.7 Fine-tuning models for multiclass text classification

## 6.2 Working with multimodal models/多模态模型
### 6.2.1 Single-modal models
### 6.2.2 Multimodal models

# 7 Creating LLM-based applications using LangChain and LlamaIndex/使用LangChain和LlamaIndex创建LLM应用
## 7.1 Introducing LLMs

## 7.2 Introducing LangChain
### 7.2.1 Installing LangChain
### 7.2.2 Creating a prompt template
### 7.2.3 Specifying an LLM
### 7.2.4 Creating an LLM chain
### 7.2.5 Running the chain
### 7.2.6 Maintaining a conversation
### 7.2.7 Using the RunnableWithMessageHistory class
### 7.2.8 Using other LLMs

## 7.3 Connecting LLMs to your private data using LlamaIndex
### 7.3.1 Installing the packages
### 7.3.2 Preparing the documents
### 7.3.3 Loading the documents
### 7.3.4 Using an embedding model
### 7.3.5 Indexing the document
### 7.3.6 Loading the embeddings
### 7.3.7 Using an LLM for querying
### 7.3.8 Asking questions
### 7.3.9 Using LlamaIndex with OpenAI
### 7.3.10 Creating a web frontend for the app
### 7.3.11 Holding a conversation
### 7.3.12 Creating a chatbot UI

# 8 Building LangChain applications visually using Langflow/使用Langflow可视化构建LangChain应用
## 8.1 What is Langflow?
### 8.1.1 Installing Langflow using the pip command
### 8.1.2 Installing Langflow using Docker
### 8.1.3 Running Langflow in the cloud

## 8.2 Creating a new Langflow project
### 8.2.1 Adding a Prompt component
### 8.2.2 Adding a Models component
### 8.2.3 Adding a Chains component
### 8.2.4 Adding Chat Input and Chat Output components
### 8.2.5 Testing the project
### 8.2.6 Maintaining a conversation using the Chat Memory component

## 8.3 Asking questions on your own data
### 8.3.1 Loading PDF documents using the File component
### 8.3.2 Splitting long text into smaller chunks using the Parse Data component
### 8.3.3 Getting questions using the Prompt component
### 8.3.4 Using the HuggingFace component
### 8.3.5 Connecting to the Chat Output component
### 8.3.6 Testing the project
### 8.3.7 Using an LLM with the OpenAI component

## 8.4 Using your project programmatically
### 8.4.1 cURL
### 8.4.2 Python code

# 9 Programming agents/Agent编程
## 9.1 What are agents?

## 9.2 Developing agents using smolagents
### 9.2.1 Using built-in tools: DuckDuckGoSearchTool
### 9.2.2 Using built-in tools: PythonInterpreterTool
### 9.2.3 Writing your own custom tools

## 9.3 Developing agents with LangChain
### 9.3.1 Using the built-in Tool class
### 9.3.2 Using custom tools

## 9.4 Developing agents using LangGraph
### 9.4.1 What is LangGraph?
### 9.4.2 LangGraph agent basics
### 9.4.3 Using LangGraph with tools
### 9.4.4 Using LangGraph with a custom tool
### 9.4.5 Using LangGraph with memory

# 10 Building a web-based UI using Gradio/构建Web UI
## 10.1 Basics of Gradio
### 10.1.1 Using Gradio’s Interface class
### 10.1.2 Configuring flagging options
### 10.1.3 Configuring authentication
### 10.1.4 Customizing the server and port
### 10.1.5 Sharing your Gradio application
### 10.1.6 Deploying your Gradio application to Hugging Face Spaces

## 10.2 Working with widgets
### 10.2.1 Working with Textbox
### 10.2.2 Working with Audio
### 10.2.3 Working with Images
### 10.2.4 Working with selection widgets
### 10.2.5 Layout using the TabbedInterface class

## 10.3 Creating a chatbot UI
### 10.3.1 Creating the basic chatbot UI
### 10.3.2 Wiring the Textbox’s submit event
### 10.3.3 Clearing the chatbot

# 11 Building locally running LLM-based applications using GPT4All/本地运行LLM应用
## 11.1 Introducing GPT4All
## 11.2 Installing GPT4All
### 11.2.1 Installing the GPT4All application
### 11.2.2 Installing the gpt4all Python library
### 11.2.3 Listing all supported models
### 11.2.4 Loading a specific model
### 11.2.5 Asking a question
### 11.2.6 Binding with Gradio

# 12 Using LLMs to query your local data/查询本地数据
## 12.1 Using GPT4All to query with your own data
### 12.1.1 Installing the required packages
### 12.1.2 Importing the various modules from the LangChain package
### 12.1.3 Loading the PDF documents
### 12.1.4 Splitting the text into chunks
### 12.1.5 Embedding
### 12.1.6 Loading the embeddings
### 12.1.7 Downloading the model
### 12.1.8 Asking questions
### 12.1.9 Loading multiple documents
### 12.1.10 Loading CSV files
### 12.1.11 Loading JSON files

## 12.2 Using LLMs to write code to analyze your data
### 12.2.1 Preparing the JSON file
### 12.2.2 Loading the JSON file
### 12.2.3 Asking the question using the Mistral 7B model
### 12.2.4 Asking questions using OpenAI

# 13 Bridging LLMs to the real world with the Model Context Protocol/模型上下文协议
## 13.1 What is MCP?
### 13.1.1 The problems MCP solves
### 13.1.2 Understanding MCP
### 13.1.3 MCP server deployment
### 13.1.4 Components in an MCP server

Figure 13.9 The components of an MCP server and their uses
- Tools
- Resources
- Prompts

## 13.2 Building an MCP server
### 13.2.1 Installing uv
### 13.2.2 Initializing the project
### 13.2.3 Installing the packages
### 13.2.4 Creating the MCP server
### 13.2.5 Inspecting the MCP server
### 13.2.6 Implementing Resources
### 13.2.7 Implementing Tools
### 13.2.8 Implementing a prompt
### 13.2.9 Testing the components

## 13.3 Testing the MCP server using Claude Desktop
### 13.3.1 Configuring Claude Desktop to use the MCP server
### 13.3.2 Getting the weather
### 13.3.3 Getting the content of a text file
### 13.3.4 Getting the content of a PDF file
### 13.3.5 Improving the MCP server

## 13.4 Trying third-party MCP servers
### 13.4.1 Get My Location
### 13.4.2 mcp-datetime
    