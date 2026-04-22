#!/usr/bin/bash

curl -s --request POST \
  --url http://127.0.0.1:2024/threads/6b146a7e-e925-41f2-9cbb-9b4355b33ed4/runs/stream \
  --header 'Content-Type: application/json' \
  --data '{
  "assistant_id": "agent",
  "checkpoint": {
    "thread_id": "",
    "checkpoint_ns": "",
    "checkpoint_id": "",
    "checkpoint_map": {}
  },
  "input": {
    "messages": [
      {
        "role": "user",
        "content": "How are you?"
      }
    ]
  },
  "command": {
    "update": null,
    "resume": null,
    "goto": null
  },
  "metadata": {},
  "config": {
    "tags": [
      ""
    ],
    "recursion_limit": 1,
    "configurable": {}
  },
  "context": {},
  "interrupt_before": "*",
  "interrupt_after": "*",
  "stream_mode": [
    "values"
  ],
  "stream_subgraphs": false,
  "stream_resumable": false,
  "on_disconnect": "continue",
  "feedback_keys": [
    ""
  ],
  "multitask_strategy": "enqueue",
  "if_not_exists": "reject",
  "after_seconds": 1,
  "durability": "async"
}'