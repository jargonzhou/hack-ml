# Learning LangChain: Building AI and LLM Applications with LangChain and LangGraph

action: [learning-langchain](../codes/learning-langchain/README.md)

# 1. LLM Fundamentals with LangChain
## Getting Set Up with LangChain
## Using LLMs in LangChain

## Making LLM Prompts Reusable

## Getting Specific Formats out of LLMs
### JSON Output
### Other Machine-Readable Formats with Output Parsers

## Assembling the Many Pieces of an LLM Application
### Using the Runnable Interface
### Imperative Composition
### Declarative Composition

# 2. RAG Part I: Indexing Your Data
## The Goal: Picking Relevant Context for LLMs
## Embeddings: Converting Text to Numbers
### Embeddings Before LLMs
### LLM-Based Embeddings
### Semantic Embeddings Explained
## Converting Your Documents into Text
## Splitting Your Text into Chunks
## Generating Text Embeddings
## Storing Embeddings in a Vector Store
### Getting Set Up with PGVector
### Working with Vector Stores
## Tracking Changes to Your Documents
## Indexing Optimization
### MultiVectorRetriever
### RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval
### ColBERT: Optimizing Embeddings

# 3. RAG Part II: Chatting with Your Data
## Introducing Retrieval-Augmented Generation
### Retrieving Relevant Documents
### Generating LLM Predictions Using Relevant Documents

Figure 3-4. Effective strategies to optimize the accuracy of your RAG system
- 1. **query transformations**: rephrase, modify, and/or expand the question 
- 2. **routing**: route the query between datastores
- 3. **query construction**: natrual langauge to SQL/Cypher/metadata filters
- 4. **multimodal/semistructured index**: optimize docs for retrieval and/or build index to handle variable data types (images/tables)
- 5. **postprocessing**: consolidate, rank, and/or filter retrieved documents

## Query Transformation/查询转换
### Rewrite-Retrieve-Read/重写-检索-读
### Multi-Query Retrieval/多查询检索
### RAG-Fusion
### Hypothetical Document Embeddings

## Query Routing/查询路由
### Logical Routing
### Semantic Routing

## Query Construction/查询构造
### Text-to-Metadata Filter
### Text-to-SQL

# 4. Using LangGraph to Add Memory to Your Chatbot
## Building a Chatbot Memory System
## Introducing LangGraph
## Creating a StateGraph
## Adding Memory to StateGraph
## Modifying Chat History
### Trimming Messages
### Filtering Messages
### Merging Consecutive Messages

# 5. Cognitive Architectures with LangGraph

Figure 5-1. Cognitive architectures for LLM applications
- 0: Code
- 1: LLM call
- 2: Chain
- 3: Router
- 4: State machine
- 5: Autonomous

## Architecture #1: LLM Call
## Architecture #2: Chain
## Architecture #3: Router

# 6. Agent Architecture
## The Plan-Do Loop
## Building a LangGraph Agent
## Always Calling a Tool First
## Dealing with Many Tools

# 7. Agents II
## Reflection/反思

## Subgraphs in LangGraph
### Calling a Subgraph Directly
### Calling a Subgraph with a Function

## Multi-Agent Architectures/多智能体架构

Figure 7-3. Multiple strategies for coordinating multiple agents

### Supervisor Architecture

# 8. Patterns to Make the Most of LLMs

Figure 8-1. The agency-reliability trade-off

## Structured Output
### Intermediate Output
### Streaming LLM Output Token-by-Token
### Human-in-the-Loop Modalities
### Multitasking LLMs

# 9. Deployment: Launching Your AI Application into Production
## Prerequisites
### Install Dependencies
### Large Language Model
### Vector Store
### Backend API
### Create a LangSmith Account

## Understanding the LangGraph Platform API
### Data Models
### Features

## Deploying Your AI Application on LangGraph Platform
### Create a LangGraph API Config
### Test Your LangGraph App Locally
### Deploy from the LangSmith UI
### Launch LangGraph Studio

## Security

# 10. Testing: Evaluation, Monitoring, and Continuous Improvement
## Testing Techniques Across the LLM App Development Cycle

## The Design Stage: Self-Corrective RAG

## The Preproduction Stage
### Creating Datasets
### Defining Your Evaluation Criteria
### Regression Testing
### Evaluating an Agent’s End-to-End Performance

- Testing an agent’s final response
- Testing a single step of an agent
- Testing an agent’s trajectory

## Production
### Tracing
### Collect Feedback in Production
### Classification and Tagging
### Monitoring and Fixing Errors

# 11. Building with LLMs
## Interactive Chatbots

## Collaborative Editing with LLMs

## Ambient Computing

