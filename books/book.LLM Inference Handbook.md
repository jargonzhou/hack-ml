# LLM Inference Handbook
* https://bentoml.com/llm/

LLM Inference Handbook is your technical glossary, guidebook, and reference - all in one. 
It covers everything you need to know about LLM inference, from core concepts and performance metrics (e.g., Time to First Token and Tokens per Second), to optimization techniques (e.g., continuous batching and prefix caching) and deployment patterns like BYOC and on-prem.


# LLM inference basics
## What is LLM inference?
## Training vs. inference/训练与推理
## How does LLM inference work?
## Where is LLM inference run?
## What is distributed inference?/分布式对立
## Serverless vs. self-hosted LLM inference
## OpenAI-compatible API

# Getting started
## Choosing the right model
## Choosing the right GPU
## Calculating GPU memory for serving LLMs
## LLM fine-tuning/微调
## LLM quantization/量化
## LLM distillation/蒸馏
## Prompt engineering/提示工程
## Choosing the right inference framework

high-throughput, low-latency applications:
- vLLM
- SGLang
- Max
- LMDeploy
- TensorRT-LLM
- Hugging Face TGI

edge devices:
- llama.cpp
- MLC-LLM
- Ollama


## Tool integration/工具集成
### Structured outputs/结构化输出
### Function calling/函数调用
### Model Context Protocol/模型上下文协议


# Infrastructure and operations
## What is LLM inference infrastructure?/推理基础设施
## Challenges in building infrastructure for LLM inference
### Fast scaling
### Build and maintenance cost
### LLM observability
## Multi-cloud and cross-region inference
## On-prem LLM deployments
## Bring Your Own Cloud (BYOC)
## InferenceOps and management

# Inference optimization/推理优化
## Key metrics for LLM inference
## LLM performance benchmarks
## Static, dynamic and continuous batching
## FlashAttention
## PagedAttention
## Speculative decoding
## Prefill-decode disaggregation
## Prefix caching
## Prefix-aware routing
## KV cache utilization-aware load balancing
## KV cache offloading
## Data, tensor, pipeline, expert and hybrid parallelisms
## Offline batch inference
