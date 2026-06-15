# > list core abstraction of Spring AI

Spring AI applies Spring's Portable Service Abstraction (PSA) principle to the generative AI ecosystem, enabling developers to write cloud-agnostic, modular code. [1, 2, 3] 

The core abstractions of the Spring AI framework are divided into five distinct architectural pillars: [2] 
## 1. Clients & Models (The Interaction Layer)
This layer abstracts the foundational AI engines, letting you swap backends (e.g., OpenAI, Anthropic, Bedrock, Ollama) by changing a dependency configuration. [4, 5, 6] 

* `ChatClient`: The primary, fluent-fluent API gateway for standard interactions. It abstracts model requests, context chaining, streaming, and execution.
* `ChatModel`: The structural interface mapping raw Java payloads to specialized underlying LLM completions.
* `EmbeddingModel`: Converts textual meaning into mathematical high-dimensional vectors. Used globally for data ingestion pipelines.
* **Specialty Models**: Interfaces like ImageModel, SpeechToTextModel, and TextToSpeechModel handle multi-modal tasks using a standard data exchange contract. [2, 4, 5, 6, 7, 8] 

## 2. Message & Prompt Infrastructure (The Input Structure)
Unlike simple HTTP engines passing unstructured strings, Spring AI tracks explicit role contexts. [5] 

* `Message`: Represents chat data segments typed by distinct scopes: UserMessage, AssistantMessage, SystemMessage, and ToolResponseMessage.
* `Prompt`: A structured container wrapping compiled system instructions, input messages, and runtime specific override parameters.
* `PromptTemplate`: A template engine providing structured variables mapping into predictable, reusable static prompts. [5, 6, 9, 10, 11] 

## 3. Middleware & State Management
This layer manipulates prompts and outputs automatically during flight without cloud vendor awareness. [2, 6] 

* `ChatClient.Advisor`: An interceptor system operating as middleware. It manipulates prompts right before sending or captures metrics right after an execution.
* `ChatMemory`: Manages state across stateless API pipelines using strategies like MessageWindowChatMemory or TokenWindowChatMemory. [2, 6, 9, 12, 13] 

## 4. Retrieval-Augmented Generation (RAG) [14, 15] 
Provides standard interfaces for building grounded data integration systems across varying vector repositories. [2, 4] 

* `Document`: The standardized representation of segmented, chunked application data containing unique IDs, textual fragments, and analytical metadata maps. [9, 16] 
* `VectorStore`: A portable interface abstracting vector databases (like PgVector, Pinecone, or Chroma). It unifies multi-vendor semantic query behaviors using standard metadata filters. [4, 9, 15, 17] 

## 5. Data Bridges (Serialization & Logic) [2] 
Bridges unstructured LLM natural text formats into strongly-typed Java enterprise systems. [2, 4] 

* `StructuredOutputConverter`: An output translator that parses and deserializes natural-text LLM string responses directly into Java POJOs.
* `ToolCallback` / `ToolDefinition`: The functional calling mechanics registering standard Java enterprise services directly with the LLM context so it can execute native Java logic on-demand. [2, 4, 5, 18, 19] 

If you are interested, I can provide:

* A code example of ChatClient incorporating ToolCallback (Function Calling).
* A walkthrough of building a RAG pipeline using the VectorStore interface.
* Code showcasing StructuredOutputConverter to map responses to a Java Record. [5, 9, 20, 21] 

Let me know which abstraction you'd like to implement first.

- [1] [https://github.com](https://github.com/spring-projects/spring-ai/blob/main/README.md)
- [2] [https://springdevpro.com](https://springdevpro.com/spring-ai/spring-ai-architecture-core-concepts-guide/)
- [3] [https://www.linkedin.com](https://www.linkedin.com/pulse/springing-forward-rod-johnson-spring-generative-ai-robert-schwentker-yapnc)
- [4] [https://docs.spring.io](https://docs.spring.io/spring-ai/reference/index.html)
- [5] [https://spring.io](https://spring.io/blog/2025/04/04/spring-ai-using-snapshots-part-2)
- [6] [https://medium.com](https://medium.com/@singh.piyush/spring-ai-explained-chatclient-rag-advisors-and-every-core-component-for-java-developers-a185201c39a0)
- [7] [https://medium.com](https://medium.com/@yashovardhan6960/exploring-spring-ai-a-practical-look-at-ai-integration-in-the-spring-ecosystem-7bfb25479bdf)
- [8] [https://github.com](https://github.com/spring-projects/spring-ai/blob/main/README.md)
- [9] [https://spring.io](https://spring.io/blog/2025/04/10/spring-ai-1-0-0-m7-released/)
- [10] [https://prakashbtech87.medium.com](https://prakashbtech87.medium.com/prakashai-spring-ai-with-ollama-and-microsoft-phi-3-1f5b1a31de47)
- [11] [https://medium.com](https://medium.com/javarevisited/if-youre-a-java-developer-ignoring-spring-ai-you-re-falling-behind-337c2b468803)
- [12] [https://spring.io](https://spring.io/ai/)
- [13] [https://medium.com](https://medium.com/javarevisited/building-production-ready-ai-agents-with-spring-ai-memory-rag-architecture-day-2-c4aef7a6ef67)
- [14] [https://medium.com](https://medium.com/@anil.goyal0057/when-llms-lie-building-a-spring-ai-rag-system-that-actually-knows-the-current-railway-minister-8912edbe9dd2)
- [15] [https://javapro.io](https://javapro.io/2026/04/30/building-production-ready-ai-agents-with-java-and-spring-ai/)
- [16] [https://medium.com](https://medium.com/@andytael/getting-started-with-spring-ai-and-oracle-ai-database-vector-search-7aed12bb9365)
- [17] [https://spring.io](https://spring.io/blog/2024/11/19/why-spring-ai/)
- [18] [https://www.baeldung.com](https://www.baeldung.com/spring-ai-deepseek-cot)
- [19] [https://medium.com](https://medium.com/@naijajug.info/getting-started-with-spring-ai-bringing-llms-into-your-spring-boot-apps-73a5736a8d9e)
- [20] [https://rathod-ajay.medium.com](https://rathod-ajay.medium.com/spring-ai-genai-agentic-ai-the-java-interview-topic-you-cant-afford-to-ignore-in-2025-72750eb75f79)
- [21] [https://www.javacodegeeks.com](https://www.javacodegeeks.com/using-spring-ai-structured-output-list-map-and-bean-converters.html)
