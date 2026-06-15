# Spring AI in Action

version: Spring AI 1.0.3.

running example: 
- the Board Game Buddy application: Burger Battle, .../Board Game Buddy 是一款专为桌面游戏玩家设计的免费数字记分与辅助工具，旨在彻底取代桌游之夜的纸笔和计算器。
- simple-tools
- mcp-filesystem-client
- mcp-server
- embabel-games-agent

# 1 Getting started with Spring AI
- 1.1 Hello, Spring AI!
  - 1.1.1 Initializing the project
  - 1.1.2 Submitting prompts
  - 1.1.3 Writing a test
  - 1.1.4 Trying it out
- 1.2 Choosing a model
  - 1.2.1 Configuring OpenAI models
  - 1.2.2 Serving models locally with Ollama
- 1.3 Previewing Spring AI’s capabilities

```java
ChatClient
ChatClient.Builder

@EnableWireMock
```

# 2 Evaluating generated responses/评估生成的响应
- 2.1 Ensuring relevant answers
- 2.2 Testing for factual accuracy
- 2.3 Applying self-evaluation at runtime
  - with Spring Retry

```java
RelevancyEvaluator
FactCheckingEvaluator
Evaluator

EvaluationRequest
EvaluationResponse

import org.springframework.retry.annotation.Recover;
import org.springframework.retry.annotation.Retryable;
```

# 3 Submitting prompts for generation/提交提示词用于生成
- 3.1 Working with prompt templates
  - 3.1.1 Defining a prompt template
  - 3.1.2 Importing the template as a resource
- 3.2 Stuffing the prompt with context
- 3.3 Assigning prompt roles
- 3.4 Influencing response generation
  - 3.4.1 Specifying chat options/指定生成选项
  - 3.4.2 Formatting response output/格式化响应
  - 3.4.3 Streaming the response/流式响应
- 3.5 Working with response metadata

```java
UserSpec

ChatOptions
```

# 4 Talking with your documents/与文档交谈
- 4.1 Understanding RAG
- 4.2 Setting up a vector store
- 4.3 Loading documents: `Document`
  - 4.3.1 Initializing the loader project
  - 4.3.2 Defining the loader pipeline
  - 4.3.3 Creating the pipeline components
  - 4.3.4 Running the pipeline
- 4.4 Implementing RAG
  - 4.4.1 Searching for similar documents: `SearchRequest`, `FilterExpressionBuilder`
  - 4.4.2 Updating the service
- 4.5 Implementing RAG with an advisor
  - `QuestionAnswerAdvisor`
- 4.6 Applying modular RAG: `RetrievalAugmentationAdvisor` `org.springframework.ai:spring-ai-rag`
  - `VectorStoreDocumentRetriever`
  - 4.6.1 Rewriting the user’s query: `RewriteQueryTransformer`
  - 4.6.2 Translating user queries: `TranslationQueryTransformer`
  - 4.6.3 Expanding user queries: `MultiQueryExpander`

Figure 4.1 RAG involves finding documents relevant to the question and adding them as context in the prompt.

```java
DocumentReader
TextReader

TextSplitter
TokenTextSplitter

VectorStore
```

Figure 4.2 A pipeline to load documents into a vector store
- org.springframework.ai:spring-ai-bom:1.0.3
- org.springframework.ai:spring-ai-starter-model-openai
- Spring AI Qdrant
  - org.springframework.ai:spring-ai-starter-vector-store-qdrant
  - org.springframework.ai:spring-ai-advisors-vector-store
- Spring AI Tika Document Reader
  - org.springframework.ai:spring-ai-tika-document-reader
- Spring Function Catalog
  - org.springframework.cloud.fn:spring-file-supplier
  - org.springframework.cloud.fn:spring-functions-catalog-bom:5.1.0
- Spring Cloud Function
  - org.springframework.cloud:spring-cloud-dependencies:2025.0.0
  - org.springframework.cloud:spring-cloud-function-context

```java
DocumentReader
TextReader
JsonReader
// org.springframework.ai:spring-ai-pdf-document-reader
PagePdfDocumentReader
ParagraphPdfDocumentReader
// org.springframework.ai:spring-ai-tika-document-reader
TikaDocumentReader
```

# 5 Enabling conversational memory/对话记忆
- 5.1 Making memories in AI
- 5.2 Adding conversational memory
  - 5.2.1 Enabling an in-memory chat advisor
  - 5.2.2 Inspecting the prompt for chat memory
  - 5.2.3 Configuring chat memory size
    - `MessageWindowChatMemory`
- 5.3 Specifying the conversation ID
  - `ChatMemory.CONVERSATION_ID`
- 5.4 Enabling persistent chat memory
  - `ChatMemoryRepository`
  - `VectorStoreChatMemoryAdvisor`
  - 5.4.1 Persisting chat memory to a database
  - 5.4.2 Storing chat memory in a vector store

```java
// ChatMemory, ChatMemoryRepository
// user message, assistant message
MessageChatMemoryAdvisor // role-based messages
PromptChatMemoryAdvisor  // no roles
VectorStoreChatMemoryAdvisor
```

Figure 5.1 Chat memory keeps a record of user and LLM interactions as a reminder for future prompts.

```java
// ChatMemoryRepository
// org.springframework.ai:spring-ai-starter-model-chat-memory-repository-cassandra
CassandraChatMemoryRepository
JdbcChatMemoryRepository
// org.springframework.ai:spring-ai-starter-model-chat-memory-repository-neo4j
Neo4jChatMemoryRepository
```

# 6 Activating tool-driven generation/工具驱动的生成
- 6.1 Getting started with AI tools
  - 6.1.1 Developing a tools-enabled application
  - 6.1.2 Digging deeper
- 6.2 Implementing tools
  - 6.2.1 Writing the tool’s foundations
  - 6.2.2 Defining the tool
  - 6.2.3 Putting the tool to work
- 6.3 Enables functions as tools

```java
@org.springframework.ai.tool.annotation.Tool
@org.springframework.ai.tool.annotation.ToolParam

@org.springframework.context.annotation.Description
java.util.function.Function // or Supplier, Consumer
```

Figure 6.1 Tool invocation involves a multipart conversation between the application and the LLM.

# 7 Applying Model Context Protocol/模型上下文协议
- 7.1 Introducing Model Context Protocol
- 7.2 Working with MCP Clients
  - `spring.ai.mcp.client` property
- 7.3 Creating your own MCP Server
  - 7.3.1 Building the server
    - `org.springframework.ai:spring-ai-autoconfigure-mcp-server`
  - 7.3.2 Setting up the database
  - 7.3.3 Creating the MCP Server tools
    - `@Tool`, `@ToolParam`
    - `ToolCallbackProvider` `MethodToolCallbackProvider`
  - 7.3.4 Inspecting the MCP Server
    - `npx @modelcontextprotocol/inspector`
  - 7.3.5 Using the server in a client application
- 7.4 Working with the HTTP+SSE transport
  - 7.4.1 Configuring an HTTP+SSE in the MCP Server
    - `org.springframework.ai:spring-ai-starter-mcp-server-webmvc`
    - `org.springframework.ai:spring-ai-starter-mcp-server-webflux`
  - 7.4.2 Inspecting the MCP Server
  - 7.4.3 Configuring the client to use an HTTP+SSE server
- 7.5 Exposing prompts and resources
  - 7.5.1 Declaring prompt and resource-exposing beans
    - `List<McpServerFeatures.SyncPromptSpecification>` `List<McpServerFeatures.AsyncPromptSpecification>`
    - `List<McpServerFeatures.SyncResourceSpecification>`
  - 7.5.2 Applying annotation-driven prompts and resources
    - `com.logaritex.mcp:spring-ai-mcp-annotations:0.1.0`

Figure 7.1 Interactions between MCP Servers and MCP Clients

transport protocols
- STDIO: Standard Input Output
- HTTP+SSE: HTTP with Server-Sent Events
- Streamable HTTP

```java
McpSchema.Prompt
McpServerFeatures.SyncPromptSpecification

McpSchema.Resource
McpServerFeatures.SyncResourceSpecification
```

# SKIP: 8 Generating with voice and pictures/语音和图片生成
- 8.1 Working with voice
  - 8.1.1 Transcribing speech
  - 8.1.2 Generating speech from text
  - 8.1.3 Applying audio input and output directly
- 8.2 Asking questions about images
- 8.3 Generating images
  - 8.3.1 Specifying image options

# 9 Observing AI operations/可观测性
- 9.1 Enabling Actuator metrics
  - `org.springframework.boot:spring-boot-starter-actuator`
  - 9.1.1 Inspecting vector store operations
    - Spring Boot Admin: https://github.com/codecentric/spring-boot-admin
    - Ostara: https://ostara.dev
  - 9.1.2 Examining AI model interaction
  - 9.1.3 Counting token usage
  - 9.1.4 Observing ChatClient operations
- 9.2 Viewing metrics in Prometheus
  - https://prometheus.io
  - `io.micrometer:micrometer-registry-prometheus`
- 9.3 Creating AI dashboards
  - https://grafana.com
- 9.4 Tracing AI operations
  - the Micrometer Tracing project
  - Jaeger, Zipkin
  - `io.micrometer:micrometer-tracing-bridge-otel`: OpenTelemetry
  - `io.opentelemetry:opentelemetry-exporter-otlp`: OTLP (OpenTelemetry Protocol), Jaeger
  - `io.opentelemetry:opentelemetry-exporter-zipkin`: Zipkin

```
/actuator/metrics/gen_ai.client.token.usage
/actuator/metrics/db.vector.client.operation

db.vector.client.operation        // The count and duration of operations against vector stores
db.vector.client.operation.active // The count and duration of currently active operations against vector stores
gen_ai.client.operation           // The count and duration of operations against Generative AI APIs; includes, chat, image, and embedding operations
gen_ai.client.operation.active    // The count and duration of currently active operations against generative AI APIs; includes chat, image, and embedding operations
gen_ai.client.token.usage         // The count of tokens, both prompt and generation, that have been used
spring.ai.advisor                 // The count and duration of prompts that have been handled by Spring AI advisors
spring.ai.advisor.active          // The count and duration of currently active prompts that have been handled by Spring AI advisors
spring.ai.chat.client             // The count and duration of operations flowing through Spring AI’s ChatClient
spring.ai.chat.client.active      // The count and duration of currently active operations flowing through Spring AI’s ChatClient
```

see also
* [Spring AI / Reference / Observability](https://docs.spring.io/spring-ai/reference/observability/index.html)
  * Chat Client
  * Chat Model
  * Tool Calling
  * EmbeddingModel
  * Image Model
  * Vector Stores

# 10 Safeguarding generative AI/安全
- 10.1 Controlling document access with RAG
  - 10.1.1 Designating premium content
  - 10.1.2 Adding security to Board Game Buddy
    - `org.springframework.boot:spring-boot-starter-security`
  - 10.1.3 Filtering for premium content
  - 10.1.4 Applying per-user conversational memory
  - 10.1.5 Trying it out
- 10.2 Securing tools
  - `@EnableMethodSecurity`
- 10.3 Safeguarding against adversarial prompting
  - 10.3.1 Preventing prompts with sensitive terms
    - `SafeGuardAdvisor`
  - 10.3.2 Preventing prompt leaks
    - Adversarial Prompting/对抗性提示 in LLMs: https://www.promptingguide.ai/prompts/adversarial-prompting
    - `CallAdvisor`
- 10.4 Moderating user input/用户输入审核
  - `ModerationModel`
  - `ModerationPrompt`

# 11 Applying generative AI patterns/生成式AI模式
- 11.1 Summarizing content/汇总内容
```
// promptTemplates/summarizeSystemPrompt.st
You are a helpful assistant with skills in summarizing the rules for board
games. Given the rules for a game, summarize the rules into a brief set of
quick-start instructions.
```
- 11.2 Translating messages/翻译消息
  - 11.2.1 Building a simple translator
  - 11.2.2 Translating game rule answers
```
// translationPromptTemplate.st
You are an expert translator, fluent in {targetLanguage}.
Translate the following text from {sourceLanguage} to {targetLanguage}:

TEXT TO TRANSLATE:
{sourceText}
```

```
// promptTemplates/systemPromptTemplate.st
You are a helpful assistant, answering questions about the tabletop
game named {gameTitle}. Always answer with a complete sentence.

If you aren't authorized to answer a question, reply by saying "That
information is reserved for premium users."

Answer all questions in the {targetLanguage} language.
```

- 11.3 Analyzing sentiment/情感分析
```
// sentimentSystemPrompt.st
You are a sentiment analysis tool, capable of determining the
sentiment of a given text. Analyze the given text and provide
a sentiment score between -1 (very negative) and 1 (very
positive). You should also provide a brief explanation of your
reasoning behind the score.
```


# 12 Employing agents/智能体
- 12.1 Understanding agents
- 12.2 Implementing agentic workflows and patterns
- 12.2.1 Chaining prompts/提示词链
```java
Action
Chain

RuleFetcherAction
MechanicsDeterminerAction
```

> What are the mechanics in the game Carcassonne?

```
// promptTemplates/rulesFetcher.st
You are a librarian of board game rules. You will be asked to fetch rules
for various board games. Your task is to extract the name of the game from
the user input and then provide the filename of the rules document for the
specified game.

The game rule files you know about are:
- Azul : EN-Azul-Rules-2017-07-04.pdf
- Burger Battle : BurgerBattle-rules.txt
- Carcassonne : Carcassonne_Rules.pdf
- Cascadia : Cascadia-Rules.pdf
- Point Salad : PointSalad.pdf
- Sagrada : Sagrada.pdf
- The Crew : TheCrew.pdf

If you do not know the filename for the rules you will respond with "I don't
have the rules for that game".
```

```
// promptTemplates/mechanicsDeterminer.st
You are a board game expert, especially skilled at deriving the mechanics
employed in a game given its rules. Your task is to analyze the rules of a
board game and determine the mechanics used in that game.

You will evaluate the provided rules and respond with a concise list of
mechanics from only the following list of game mechanics:

- Area Majority / Influence : Multiple players may occupy a space and gain benefits based on their proportional presence in the space.
- Cooperative Game : [...description...]
- End Game Bonuses : [...description...]
- Hand Management : [...description...]
- Modular Board : [...description...]
- Open Drafting : [...description...]
- Take That : [...description...]
- Tile Placement : [...description...]
- Worker Placement : [...description...]
```

- 12.2.2 Routing tasks/路由

```java
// mechanics chain
RuleFetcherAction
PlayerCountAction

// playerCount chain
RuleFetcherAction
PlayerCountAction

Router
```

> What are the mechanics in Azul?
>
> How many can play Azul?

```
// promptTemplates/playerCount.st
You are a board game expert, able to determine number of players
that can play a game based on its rules.
Given the rules of a game, determine the number of players that can play it.
```

```
// promptTemplates/router.st
You are a router that considers user input and routes the input to
the appropriate handler.

Given the user input, determine the appropriate handler based on the content of the input.
Your answer should be only one of the following:
- mechanics - Handles questions about board game mechanics.
- playerCount - Handles questions about the number of players in a game.
```

- 12.2.3 Applying parallelization/并行化
```java
ParallelizerAction // PlayerCountAction, MechanicsDeterminerAction
// summarizerChain
RuleFetcherAction
SummarizerAction
```

> Tell me about Azul

```
// promptTemplates/summarizer.st
You are someone who writes about board games. 
Given some text describing a board game, your task is to summarize the text in a concise manner.
```


- 12.3 Creating self-planning agentic solutions/自主规划的智能体解决方案
  - Embabel 0.1.0
    - GOAP: Goal-Oriented Action Planning
  - 12.3.1 Initializing an Embabel project
    - `com.embabel.agent:embabel-agent-starter:0.1.0`
  - 12.3.2 Defining the agent class
    - `GameInfoAgent`
    - `GameMechanics determineGameMechanics(GameRules)`
    - `PlayerCount determinePlayerCount(GameRules)`
  - 12.3.3 Defining an action to get game rules
    - `GameRules getGameRules(GameTitle, RulesFile)`
  - 12.3.4 Defining an action to get the rules filename
    - `RulesFile getGameRulesFilename(GameTitle)`
  - 12.3.5 Defining an action to get the game title
    - `GameTitle extractGameTitle(UserInput)`
  - 12.3.6 Running the agent via Embabel’s shell
    - `@EnableAgentShell`
  - 12.3.7 Accessing the agent via MCP
    - `@AchievesGoal(export = @Export(...))`

```java
@Agent
@Action
@AchievesGoal
PromptRunner
```

```shell
embabel> execute "How many can play Azul?"
embabel> execute "What are the mechanics in Azul?"
```

# See Also
* https://github.com/habuma/spring-ai-examples
* Prompt Engineering Guide: https://www.promptingguide.ai
* Spring AI Community: https://github.com/spring-ai-community
* Building Effective Agents: https://mng.bz/5vGZ
  * augmented LLM
  * agentic workflows
    * prompt chaining
    * routing
    * parallelization
    * orchestrator-workers
    * evaluator-optimizer
  * agents

tools
- org.springframework.ai:spring-ai-starter-model-openai
- org.springframework.ai:spring-ai-starter-model-azure-openai
- WireMock
- Ollama: org.springframework.ai:spring-ai-starter-model-ollama
- StringTemplate: https://www.stringtemplate.org
- Logbook: https://github.com/zalando/logbook
  - org.zalando:logbook-spring-boot-starter:3.9.0
  - `LogbookClientHttpRequestInterceptor`
- Qdrant
  - org.springframework.ai:spring-ai-spring-boot-docker-compose
  - org.springframework.boot:spring-boot-docker-compose
- Embabel Agent Framework: https://github.com/embabel/embabel-agent