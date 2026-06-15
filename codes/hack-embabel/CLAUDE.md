# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A demo/learning project ("hack") built on the **Embabel Agent Framework** (`com.embabel.agent`, v0.5.0-SNAPSHOT) — a JVM agent framework that uses **GOAP (Goal-Oriented Action Planning)** to plan and execute multi-step LLM workflows. The app is a Spring Boot **interactive shell**. The single working example is `StarNewsFinderAgent`, which combines a person's horoscope with relevant news into an amusing writeup.

## Build & run

- **Requires JDK 21.** The pom targets Java 21 (`maven.compiler.source/target=21`), but the default `JAVA_HOME`/Maven on this machine is Java 17 (via sdkman). Compilation fails under 17 — switch first, e.g. `sdk use java 21.x.y` (or point `JAVA_HOME` at a 21 JDK) before any `mvn` command.
- **Compile:** `mvn compile`
- **Package:** `mvn package` (produces a plain jar — see caveat below)
- **Tests:** `mvn test` — there is currently **no `src/test`**, so this is a no-op until tests are added. Single test (once tests exist): `mvn test -Dtest=ClassName#methodName`. The `embabel-agent-test` dependency is already on the test classpath.
- **Run:** There is **no `spring-boot-maven-plugin`**, so `mvn spring-boot:run` and `java -jar` will not work. Run the `main` method in `EmbabelApplication` from the IDE (IntelliJ project is set up), or from CLI: `mvn exec:java -Dexec.mainClass=com.spike.ml.embabel.EmbabelApplication`.

There is no CLI linter wired into the build; Checkstyle exists only as an IDE config (`.idea/checkstyle-idea.xml`).

## Configuration & secrets

- **Models** are configured in `src/main/resources/application.yaml`. The **active** model provider is an OpenAI-compatible endpoint at `https://ollama.com` (`embabel.agent.platform.models.openai.custom`), with `default-llm: gemma4:31b-cloud` (also `gpt-oss:120b-cloud`). A **local LM Studio** config (`http://127.0.0.1:1234`, gemma/embeddinggemma models) is present but commented out — swap the commented blocks to use it.
- **API key:** the endpoint needs `OPENAI_CUSTOM_API_KEY`. It lives in `.env`, but **Spring Boot does not auto-load `.env`** — you must export it into the environment (or inject it via the IDE run config). Without it the yaml falls back to `your-dev-key`, which will not authenticate.
- Only the `com.spike.ml.embabel.agent` package is scanned for agents (`embabel.agent.scan-packages`). Autonomy confidence cut-offs are set very low (0.05), making the planner permissive about which goal/agent to select.

## The planning model (the key concept)

You do **not** write an imperative pipeline. You declare typed steps and the framework's planner chains them by matching **input types to output types** to reach a goal. Reading any single `@Action` method in isolation is misleading — understand the whole agent as a graph.

Annotations (`com.embabel.agent.api.annotation`):
- `@Agent` — a class whose `@Action` methods form a planning graph.
- `@Action` — one planning step: typed params in, typed object out. Optional `cost` biases the planner away from a step. `canRerun`, `trigger` control re-execution.
- `@AchievesGoal` — marks the action that completes the goal; the run ends when its output type is produced. `@Export(remote=true, ...)` exposes the goal for remote/A2A invocation.

Worked example — `StarNewsFinderAgent` (goal: produce `Writeup`):
- `writeup(StarPerson, RelevantNewsStories, Horoscope) → Writeup` `@AchievesGoal`
- `RelevantNewsStories ← findNewsStories(StarPerson, Horoscope)` — uses WEB tools
- `Horoscope ← retrieveHoroscope(StarPerson)` — calls `HoroscopeService` (freehoroscopeapi.com)
- `StarPerson` has **two competing paths**, and this is the part that requires reading multiple files:
  - **Direct/cheap:** `extractStarPerson(UserInput) → StarPerson` using `createObjectIfPossible` — returns null when the sign can't be extracted, which lets the planner fall back.
  - **Fallback/costly:** `extractPerson(UserInput) → Person`, then `makeStarry(Person) → Starry` (`cost = 100.0`, a **human-in-the-loop form** via `WaitFor.formSubmission`), then `assembleStarPerson(Person, Starry) → StarPerson`. The high cost means the planner only takes this route when the direct path yields nothing.

`createObject` vs `createObjectIfPossible` matters for planning: the "ifPossible" variant returning null is the signal that drives the cost-based fallback above.

## How actions talk to the LLM, tools, and the user

- **LLM access** is via an injected `Ai` param: `ai.withDefaultLlm().createObject(prompt, Type.class)`. Also `.withLlm(LlmOptions...)` (e.g. temperature), `.withId(...)`, `.withSystemPrompt(...)`, `.respond(messages)`.
- **Built-in tool groups:** `.withToolGroup(CoreToolGroups.WEB)` adds web search/fetch.
- **Custom tools:** plain methods annotated `@LlmTool` (see `support/ContextDiagnosticTools`), attached with `.withTool(Tool.fromInstance(obj).getFirst())`.
- **ToolCallContext:** tool methods can receive a `ToolCallContext` param (framework-injected) carrying metadata (tenant IDs, auth tokens) set via `ProcessOptions.withToolCallContext()` / the shell's `set-context key=value`. `ContextDiagnosticTools.checkContext` exists specifically to verify this propagation end-to-end — `findNewsStories`' prompt instructs the LLM to call it first.
- **HITL:** `WaitFor.formSubmission(label, FormType.class)` suspends the run for user input; the form type (e.g. `Starry`) uses `@Text` field annotations from `com.embabel.ux.form`.
- **Domain I/O types** come from `com.embabel.agent.domain.library` (`UserInput`, `Person`/`PersonImpl`, `RelevantNewsStories`, `HasContent`). Output records use Jackson annotations (`@JsonClassDescription`, `@JsonPropertyDescription`) so the LLM knows how to populate them.

## Running agents from the shell

The app boots into a Spring Shell (`embabel-agent-starter-shell`). Common commands (see `spring-shell.log` for real session history):
- `execute "<request>"` (alias `x`) — plan and run an agent autonomously from natural language, e.g. `execute "write a story about Gemini and Cristiano Ronaldo."`. Flags seen: `-p -r`, `-d`.
- `chat "<msg>"` / `chat` — conversational mode.
- `agents`, `models`, `help` — list registered agents, available LLMs/embeddings, and commands.
- `set-context key=value` — populate `ToolCallContext` for the next run.

## Observability

OpenTelemetry tracing is on (`management.tracing`, sampling 1.0) and exported to **Langfuse** via the `opentelemetry-exporter-langfuse` (quantpulsar) dependency. Default endpoint is a **local Langfuse** at `http://127.0.0.1:3000/api/public/otel` (keys in `application.yaml`); switch to `https://cloud.langfuse.com/api/public/otel` for cloud.

## Notable wiring

- `EmbabelApplication` excludes Spring Security auto-config (`SecurityAutoConfiguration`, `OAuth2ResourceServerAutoConfiguration`) and sets a STAR_WARS logging personality.
- A2A starter is included and the StarNews goal is exported with `remote=true`. The **MCP server** starter is deliberately excluded/commented out (in both pom and config).
- `ChatActions` and `EmbabelApplicationConfig` are present but fully commented out — scaffolding, not active code.
