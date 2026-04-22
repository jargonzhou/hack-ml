# Learning LangChain

# my-app

Skaffold:
```shell
$ langgraph new
📂 Please specify the path to create the application [.]: my-app
🌟 Please select a template:
1. Deep Agent - An opinionated deployment template for a Deep Agent.
2. Agent - A simple agent that can be flexibly extended to many tools.
3. New LangGraph Project - A simple, minimal chatbot with memory.
Enter the number of your template choice (default is 1): 2

You selected: Agent - A simple agent that can be flexibly extended to many tools.
📥 Attempting to download repository as a ZIP archive...
URL: https://github.com/langchain-ai/simple-agent-template/archive/refs/heads/main.zip
✅ Downloaded and extracted repository to D:\workspace\github\hack-ml\codes\learning-langchain\my-app
🎉 New project created at D:\workspace\github\hack-ml\codes\learning-langchain\my-app
```

Dev
```shell
$ cd my-app
$ uv sync --dev
$ cp .env.example .env
$ uv run langgraph dev
```