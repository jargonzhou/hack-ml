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
- Creating virtual environments
- Starting Jupyter Notebook

## 2.2 Installing the Transformers library/Transformers库
- Support for GPU
- Using GPU in the pipeline object

## 2.3 Installing the Hugging Face Hub package/Hub包
- Downloading files
- Using the Hugging Face CLI

# 3 Using Hugging Face transformers and pipelines for NLP tasks/NLP任务
## 3.1 Introduction to the transformer architecture
- Tokenization
- Token embeddings
- Positional encoding
- Transformer block
- Softmax

## 3.2 Working with the Transformers library
- What are pretrained transformers models?
- What are transformers pipelines?
- Using a model directly
- Using a transformers pipeline

## 3.3 Using transformers for NLP tasks
- Text classification
- Text generation
- Text summarization
- Text translation
- Zero-shot classification
- Question-answering tasks

# 4 Using Hugging Face for computer vision tasks/计算机视觉任务
## 4.1 Hugging Face computer vision models
## 4.2 Object detection
- Using the model directly
- Using the transformers pipeline
- Binding to a webcam
## 4.3 Image classification
## 4.4 Image segmentation
- Using the model programmatically
- Binding to Gradio
## 4.5 Video classification
- Installing the prerequisites
- Downloading the videos for testing
- Using the transformers pipeline object

# 5 Exploring, tokenizing, and visualizing Hugging Face datasets/分词, 数据集
## 5.1 What are Hugging Face datasets?
- Getting the list of datasets available
- Validating the availability of a dataset
- Downloading a dataset
- Shuffling a dataset
- Streaming a dataset
- Getting the Parquet files of a dataset

## 5.2 Tokenization in NLP
- Types of tokenization methods
- Tokenizing datasets

## 5.3 Visualizing datasets
- Using the twitter-financial-news-topic dataset
- Using the CIFAR-10 dataset

# 6 Fine-tuning pretrained models and working with multimodal models
## 6.1 Fine-tuning pretrained models/微调预训练模型
- Loading the yelp_polarity dataset
- Filtering the yelp_polarity dataset
- Tokenizing the reduced dataset
- Setting up a pretrained model for sequence classification
- Configuring and initializing a trainer for fine-tuning a pretrained model
- Using the fine-tuned model
- Fine-tuning models for multiclass text classification

## 6.2 Working with multimodal models/多模态模型
- Single-modal models
- Multimodal models

# 7 Creating LLM-based applications using LangChain and LlamaIndex/使用LangChain和LlamaIndex创建LLM应用
## 7.1 Introducing LLMs

## 7.2 Introducing LangChain
- Installing LangChain
- Creating a prompt template
- Specifying an LLM
- Creating an LLM chain
- Running the chain
- Maintaining a conversation
- Using the RunnableWithMessageHistory class
- Using other LLMs

## 7.3 Connecting LLMs to your private data using LlamaIndex
- Installing the packages
- Preparing the documents
- Loading the documents
- Using an embedding model
- Indexing the document
- Loading the embeddings
- Using an LLM for querying
- Asking questions
- Using LlamaIndex with OpenAI
- Creating a web frontend for the app
- Holding a conversation
- Creating a chatbot UI

# 8 Building LangChain applications visually using Langflow/使用Langflow可视化构建LangChain应用
## 8.1 What is Langflow?
- Installing Langflow using the pip command
- Installing Langflow using Docker
- Running Langflow in the cloud

## 8.2 Creating a new Langflow project
- Adding a Prompt component
- Adding a Models component
- Adding a Chains component
- Adding Chat Input and Chat Output components
- Testing the project
- Maintaining a conversation using the Chat Memory component

## 8.3 Asking questions on your own data
- Loading PDF documents using the File component
- Splitting long text into smaller chunks using the Parse Data component
- Getting questions using the Prompt component
- Using the HuggingFace component
- Connecting to the Chat Output component
- Testing the project
- Using an LLM with the OpenAI component

## 8.4 Using your project programmatically
- cURL
- Python code

# 9 Programming agents/Agent编程
## 9.1 What are agents?

## 9.2 Developing agents using smolagents
- Using built-in tools: DuckDuckGoSearchTool
- Using built-in tools: PythonInterpreterTool
- Writing your own custom tools

## 9.3 Developing agents with LangChain
- Using the built-in Tool class
- Using custom tools

## 9.4 Developing agents using LangGraph
- What is LangGraph?
- LangGraph agent basics
- Using LangGraph with tools
- Using LangGraph with a custom tool
- Using LangGraph with memory

# 10 Building a web-based UI using Gradio/构建Web UI
## 10.1 Basics of Gradio
- Using Gradio’s Interface class
- Configuring flagging options
- Configuring authentication
- Customizing the server and port
- Sharing your Gradio application
- Deploying your Gradio application to Hugging Face Spaces

## 10.2 Working with widgets
- Working with Textbox
- Working with Audio
- Working with Images
- Working with selection widgets
- Layout using the TabbedInterface class

## 10.3 Creating a chatbot UI
- Creating the basic chatbot UI
- Wiring the Textbox’s submit event
- Clearing the chatbot

# 11 Building locally running LLM-based applications using GPT4All/本地运行LLM应用
## 11.1 Introducing GPT4All
## 11.2 Installing GPT4All
- Installing the GPT4All application
- Installing the gpt4all Python library
- Listing all supported models
- Loading a specific model
- Asking a question
- Binding with Gradio

# 12 Using LLMs to query your local data/查询本地数据
## 12.1 Using GPT4All to query with your own data
- Installing the required packages
- Importing the various modules from the LangChain package
- Loading the PDF documents
- Splitting the text into chunks
- Embedding
- Loading the embeddings
- Downloading the model
- Asking questions
- Loading multiple documents
- Loading CSV files
- Loading JSON files

## 12.2 Using LLMs to write code to analyze your data
- Preparing the JSON file
- Loading the JSON file
- Asking the question using the Mistral 7B model
- Asking questions using OpenAI

# 13 Bridging LLMs to the real world with the Model Context Protocol/模型上下文协议
## 13.1 What is MCP?
- The problems MCP solves
- Understanding MCP
- MCP server deployment
- Components in an MCP server

Figure 13.9 The components of an MCP server and their uses
- Tools
- Resources
- Prompts

## 13.2 Building an MCP server
- Installing uv
- Initializing the project
- Installing the packages
- Creating the MCP server
- Inspecting the MCP server
- Implementing Resources
- Implementing Tools
- Implementing a prompt
- Testing the components

## 13.3 Testing the MCP server using Claude Desktop
- Configuring Claude Desktop to use the MCP server
- Getting the weather
- Getting the content of a text file
- Getting the content of a PDF file
- Improving the MCP server

## 13.4 Trying third-party MCP servers
- Get My Location
- mcp-datetime
    