# Spring AI
* https://spring.io/projects/spring-ai
* https://docs.spring.io/spring-ai/reference/index.html
* https://github.com/spring-projects/spring-ai

> The Spring AI project aims to streamline the development of applications that incorporate artificial intelligence functionality without unnecessary complexity.
>
> The project draws inspiration from notable Python projects, such as LangChain and LlamaIndex, but Spring AI is not a direct port of those projects. The project was founded with the belief that the next wave of Generative AI applications will not be only for Python developers but will be ubiquitous across many programming languages.
>
> Spring AI addresses the fundamental challenge of AI integration: `Connecting your enterprise Data and APIs with AI Models`.

Spring AI provides the following features:
- Support for all major [AI Model providers](https://docs.spring.io/spring-ai/reference/api/index.html)/AI模型供应商 such as Anthropic, OpenAI, Microsoft, Amazon, Google, and Ollama. Supported model types/模型类型 include:
    - [Chat Completion](https://docs.spring.io/spring-ai/reference/api/chatmodel.html)
    - [Embedding](https://docs.spring.io/spring-ai/reference/api/embeddings.html)
    - [Text to Image](https://docs.spring.io/spring-ai/reference/api/imageclient.html)
    - [Audio Transcription](https://docs.spring.io/spring-ai/reference/api/audio/transcriptions.html)
    - [Text to Speech](https://docs.spring.io/spring-ai/reference/api/audio/speech.html)
    - [Moderation](https://docs.spring.io/spring-ai/reference/api/index.html#api/moderation)
- Portable API support across AI providers for both synchronous and streaming API options are supported. Access to [model-specific features](https://docs.spring.io/spring-ai/reference/api/chatmodel.html#_chat_options)/模型特定的特性 is also available.
- [Structured Outputs](https://docs.spring.io/spring-ai/reference/api/structured-output-converter.html)/结构化输出 - Mapping of AI Model output to POJOs.
- Support for all major [Vector Database providers](https://docs.spring.io/spring-ai/reference/api/vectordbs.html)/向量数据库供应商 such as _Apache Cassandra, Azure Vector Search, Chroma, Milvus, MongoDB Atlas, Neo4j, Oracle, PostgreSQL/PGVector, PineCone, Qdrant, Redis, and Weaviate_.
- Portable API across Vector Store providers, including a novel SQL-like [metadata filter API](https://docs.spring.io/spring-ai/reference/api/vectordbs.html#metadata-filters).
- [Tools/Function Calling](https://docs.spring.io/spring-ai/reference/api/functions.html)/工具和函数调用 - permits the model to request the execution of client-side tools and functions, thereby accessing necessary real-time information as required.
- [Observability](https://docs.spring.io/spring-ai/reference/observability/index.html)/可观测性 - Provides insights into AI-related operations.
- Document injection [ETL framework](https://docs.spring.io/spring-ai/reference/api/etl-pipeline.html)/文档注入ETL框架 for Data Engineering.
- [AI Model Evaluation](https://docs.spring.io/spring-ai/reference/api/testing.html)/AI模型评估 - Utilities to help evaluate generated content and protect against hallucinated response.
- [ChatClient API](https://docs.spring.io/spring-ai/reference/api/chatclient.html) - Fluent API for communicating with AI Chat Models, idiomatically similar to the WebClient and RestClient APIs.
- [Advisors API](https://docs.spring.io/spring-ai/reference/api/advisors.html) - Encapsulates recurring Generative AI patterns, transforms data sent to and from Language Models (LLMs), and provides portability across various models and use cases.
- Support for [Chat Conversation Memory](https://docs.spring.io/spring-ai/reference/api/chatclient.html#_chat_memory)/聊天对话记忆 and [Retrieval Augmented Generation (RAG)](https://docs.spring.io/spring-ai/reference/api/chatclient.html#_retrieval_augmented_generation)/检索增强生成.
- Spring Boot Auto Configuration and Starters for all AI Models and Vector Stores - use the [start.spring.io](https://start.spring.io/) to select the Model or Vector-store of choice.

This feature set lets you implement common use cases such as "Q&A over your documentation" or "Chat with your documentation."

# See Also
* [awesom-spring-ai](https://github.com/spring-ai-community/awesome-spring-ai)
* [ai_generated/gen-spring-ai-core-abstractions.md](./ai_generated/gen-spring-ai-core-abstractions.md)
* examples
  * https://github.com/spring-projects/spring-ai-examples
* [book.Spring AI in Action.md](../../../books/infrastructure/book.Spring%20AI%20in%20Action.md)