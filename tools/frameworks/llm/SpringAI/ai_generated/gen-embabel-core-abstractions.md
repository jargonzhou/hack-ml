# > list and group core abstractions in Embabel Agent Framework, in english for currently 0.5.0-SNAPSHOT version

The core abstractions of the Embabel Agent Framework (version 0.5.0-SNAPSHOT) are organized into four key layers. Embabel separates itself from traditional frameworks by using **Goal-Oriented Action Planning (GOAP)**, **type-safe domain models**, and **a non-LLM planning loop instead of hardcoded state machines**. [1, 2, 3, 4, 5] 

Here are the core abstractions grouped by their structural role in the framework:
## 1. Behavior & Execution Abstractions
These define what an agent can do and how it drives progress toward a target. [1, 6] 

* `Agent`: A self-contained component bundling domain logic, AI capabilities, and tool definitions. Declared via @Agent or the Kotlin DSL.
* `Goal`: The desired end state or objective that the agent needs to achieve.
* `Action`: Strongly-typed methods (annotated with @Action) that serve as individual execution steps. They define explicit input/output Java/Kotlin types.
* `Condition`: Preconditions and postconditions assessed before and after action execution to track step dependencies dynamically. [5, 7, 8, 9, 10] 

## 2. Runtime & State Abstractions
These manage state, execution loops, and environmental infrastructure during an agent's lifecycle. [1, 7] 

* `AgentPlatform`: The foundational environment that initializes the engine, manages configuration, and integrates with the Spring container.
* `AgentProcess`: A stateful runtime execution instance tracking a unique ID, step execution history, and parent-child hierarchies.
* `Blackboard`: The shared, persistent memory system that maintains state throughout the agent's process execution.
* `OperationContext` / `Ai`: Gateways providing direct, programmatic access to LLM reasoning, hyperparameters, and explicit AI capabilities without spawning full agents. [1, 7, 11] 

## 3. Intelligence & Capabilities Abstractions [3] 
These handle the "brain" and the external actions accessible to the agentic process. [1, 8] 

* `Planner`: The core execution engine utilizing a deterministic GOAP algorithm to dynamically formulate a plan toward a Goal.
* `Tools` / `ToolGroups`: External capabilities (e.g., CoreToolGroups.WEB) exposed to the LLM during planning. Version 0.5.0 emphasizes native Model Context Protocol (MCP) server consumption.
* **Domain Model**: The type-safe objects and business rules driving the agent, removing the need for loosely-typed maps. [1, 7, 9, 10, 12, 13] 

## 4. Enterprise & Flow Control Abstractions
These secure and customize the interaction between the system, the developer, and the LLM. [1] 

* `Guardrails`: Rules and safety policies enforcing strict input/output boundaries around the LLM.
* `ProcessOptions`: Configuration settings governing execution modes, timeouts, and resource allocation.
* `Interceptors` (Callbacks): Hooks providing deep observability into prompts, costs, and token tracking. [1] 

Would you like a code snippet demonstrating how an Agent connects an Action to a Goal using the annotation model or the Kotlin DSL?

- [1] [https://docs.embabel.com](https://docs.embabel.com/embabel-agent/guide/0.4.0-SNAPSHOT/)
- [2] [https://jettro.dev](https://jettro.dev/building-agents-with-embabel-a-hands-on-introduction-4f96d2edeac0)
- [3] [https://github.com](https://github.com/embabel/embabel-agent/wiki/)
- [4] [https://medium.com](https://medium.com/@springrod/embabel-year-end-update-building-the-best-agent-framework-25ed98728e79)
- [5] [https://codewiz.info](https://codewiz.info/blog/java-ai-agent-frameworks-2026/)
- [6] [https://github.com](https://github.com/embabel/embabel-agent/wiki/)
- [7] [https://docs.embabel.com](https://docs.embabel.com/embabel-agent/guide/0.1.3/)
- [8] [https://docs.embabel.com](https://docs.embabel.com/embabel-agent/guide/0.3.3-SNAPSHOT/)
- [9] [https://github.com](https://github.com/embabel)
- [10] [https://docs.embabel.com](https://docs.embabel.com/embabel-agent/guide/0.1.2-SNAPSHOT/)
- [11] [https://docs.embabel.com](https://docs.embabel.com/embabel-agent/guide/0.1.2-SNAPSHOT/)
- [12] [https://docs.embabel.com](https://docs.embabel.com/embabel-agent/guide/0.1.3/)
- [13] [https://github.com](https://github.com/embabel/embabel-agent?trk=4b29643c-e00f-4ab6-ab9c-b1fb47aa1708&sc_channel=podcast)
