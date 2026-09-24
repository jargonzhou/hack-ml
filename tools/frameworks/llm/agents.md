# AI Agents

# The Zoo of AI Agents
## pi
* https://github.com/earendil-works/pi

Pi is a minimal terminal coding harness. Adapt pi to your workflows, not the other way around, without having to fork and modify pi internals. Extend it with TypeScript Extensions, Skills, Prompt Templates, and Themes. Put your extensions, skills, prompt templates, and themes in Pi Packages and share them with others via npm or git.

Pi ships with powerful defaults but skips features like sub agents and plan mode. Instead, you can ask pi to build what you want or install a third party pi package that matches your workflow.

Pi runs in four modes: interactive, print or JSON, RPC for process integration, and an SDK for embedding in your own apps. See openclaw/openclaw for a real-world SDK integration.

```shell
$ npm install -g @earendil-works/pi-coding-agent

# https://pi.dev/packages/pi-mcp-extension
$ pi install npm:pi-mcp-extension
# ~/.pi/agent/mcp.json (global) or .pi/mcp.json (project-level)
```

## Claude Code
* https://github.com/anthropics/claude-code

Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.

## OpenClaw
* https://github.com/openclaw/openclaw

OpenClaw is a personal AI assistant you run on your own devices. It answers you on the channels you already use (WhatsApp, Telegram, Slack, Discord, Google Chat, Signal, iMessage, BlueBubbles, IRC, Microsoft Teams, Matrix, Feishu, LINE, Mattermost, Nextcloud Talk, Nostr, Synology Chat, Tlon, Twitch, Zalo, Zalo Personal, WebChat). It can speak and listen on macOS/iOS/Android, and can render a live Canvas you control. The Gateway is just the control plane — the product is the assistant.

- [ClawHub](https://clawhub.ai/): the skill dock for sharp agents

# Skills
## Agent Skills
* https://github.com/agentskills/agentskills

Standardized way to give AI agents new capabilities.

## vercel-labs/skills
* https://github.com/vercel-labs/skills
* https://skills.sh/

The CLI for the open agent skills ecosystem.

Skills are reusable capabilities for AI agents. Install them with a single command to enhance your agents with access to procedural knowledge.

## book-to-skill
* https://github.com/virgiliojr94/book-to-skill

Turn any technical book, document folder, or collection of sources into a unified agent skill — ready to study, reference, and use while you work in GitHub Copilot CLI, Amp, Claude Code, Hermes Agent, or OpenClaw.

```shell
$ npx skills list
Need to install the following packages:
skills@1.7.0
Ok to proceed? (y) y

$ npx skills add virgiliojr94/book-to-skill -y


# pi
/book-to-skill "./Python Data Science Handbook, 2nd edition, 2022.pdf" python-ds
```

## Archify
* https://github.com/tt-a1i/archify

Turn anything you want to understand, plan, or share into an interactive visual.

Start with an idea, a question, or a plan. Describe it to your AI agent, and Archify turns it into an interactive HTML you can explore, customize, and share. From travel itineraries and learning maps to complex systems—make it your own.

```shell
$ npx skills add tt-a1i/archify -g
```

prompts
```
Use Archify to diagram a web request: Browser calls the API, the API checks Redis, and a cache miss queries PostgreSQL and fills the cache.

Add authentication

Highlight the cache-miss path

Switch to the light theme
```

## mattpocock/skills
* https://github.com/mattpocock/skills

Skills for Real Engineers. Straight from my .agents directory.

# Memory

## agentmemory
* https://github.com/rohitg00/agentmemory

Your coding agent remembers everything. No more re-explaining. Built on [iii engine](https://github.com/iii-hq/iii).

Persistent memory for Claude Code, GitHub Copilot CLI, Cursor, Gemini CLI, Codex CLI, Hermes, OpenClaw, pi, OpenCode, and any MCP client.

```shell
$ npx -y @agentmemory/agentmemory@latest -g
$ npx skills add rohitg00/agentmemory -y

# x https://github.com/rohitg00/agentmemory/tree/main/integrations/pi
# https://pi.dev/packages/@estebanforge/pi-agentmemory
$ pi install npm:@estebanforge/pi-agentmemory
```

# See Also
