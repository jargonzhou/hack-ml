"""Minimal LangChain agent graph for deployment."""

from __future__ import annotations

import ast
import os
from datetime import datetime, timezone
from typing import Any

from langchain.agents import create_agent
from langchain_core.tools import tool

DEFAULT_MODEL = os.getenv("SIMPLE_AGENT_MODEL", "anthropic:claude-sonnet-4-6")


@tool
def utc_now() -> str:
  """Return the current UTC timestamp in ISO format."""
  return datetime.now(tz=timezone.utc).isoformat()


@tool
def calculator(expression: str) -> str:
  """Evaluate a simple arithmetic expression safely.

  Supported operators: +, -, *, /, %, ** and parentheses.
  """
  parsed = ast.parse(expression, mode="eval")
  allowed_nodes = (
      ast.Expression,
      ast.BinOp,
      ast.UnaryOp,
      ast.Constant,
      ast.Add,
      ast.Sub,
      ast.Mult,
      ast.Div,
      ast.Mod,
      ast.Pow,
      ast.USub,
      ast.UAdd,
      ast.Load,
  )

  for node in ast.walk(parsed):
    if not isinstance(node, allowed_nodes):
      raise ValueError("Expression contains unsupported syntax")

  result: Any = eval(compile(parsed, "<calculator>", "eval"), {
                     "__builtins__": {}}, {})
  return str(result)


graph = create_agent(
    model=DEFAULT_MODEL,
    tools=[utc_now, calculator],
    system_prompt=(
        "You are a concise assistant. "
        "Use tools when they add factual precision, then return a direct answer."
    ),
    name="simple_agent",
)

# POST /threads
# {
#   "detail": "Thread 6b146a7e-e925-41f2-9cbb-9b4355b33ed4 was created, but there were problems updating the state: Thread '6b146a7e-e925-41f2-9cbb-9b4355b33ed4' has no assigned graph ID. This usually occurs when no runs have been made on this particular thread. This operation requires a graph ID. Please ensure a run has been made for the thread or manually update the thread metadata (by setting the 'graph_id' field) before running this operation."
# }
#
# POST /threads/{thread_id}/runs/stream
# {
#   "assistant_id": "agent",
#   "checkpoint": {
#     "thread_id": "",
#     "checkpoint_ns": "",
#     "checkpoint_id": "",
#     "checkpoint_map": {}
#   },
#   "input": {
#     "messages": [
#       {
#         "role": "user",
#         "content": "How are you?"
#       }
#     ]
#   },
#   "command": {
#     "update": null,
#     "resume": null,
#     "goto": null
#   },
#   "metadata": {},
#   "config": {
#     "tags": [
#       ""
#     ],
#     "recursion_limit": 1,
#     "configurable": {}
#   },
#   "context": {},
#   "interrupt_before": "*",
#   "interrupt_after": "*",
#   "stream_mode": [
#     "values"
#   ],
#   "stream_subgraphs": false,
#   "stream_resumable": false,
#   "on_disconnect": "continue",
#   "feedback_keys": [
#     ""
#   ],
#   "multitask_strategy": "enqueue",
#   "if_not_exists": "reject",
#   "after_seconds": 1,
#   "durability": "async"
# }
#
# ResponseError('registry.ollama.ai/library/deepseek-r1:latest does not support tools')
