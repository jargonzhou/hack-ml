# Hugging Face
* https://huggingface.co/
* https://en.wikipedia.org/wiki/Hugging_Face

> Hugging Face, Inc., is an American company based in New York City that develops computation tools for building applications using machine learning. Its **transformers library** built for natural language processing applications and its platform allow users to share machine learning models and datasets and showcase their work.

# Doc
* https://huggingface.co/docs

Hub & Client Libraries/仓库和客户端库
- **Hub**: Host Git-based models, datasets, and Spaces on the HF Hub
  - Repositories
  - Models
  - Datasets
  - Spaces
  - Storage Buckets
  - Jobs
  - Agents
  - Other
- **Hub Python Library**: Python client to interact with the Hugging Face Hub
- **CLI**: Tools for agents and humans to interact with all the Hugging Face services
- **Huggingface.js**: JavaScript libraries for Hugging Face with built-in TS types
- **Tasks**: Explore demos, models, and datasets for any ML tasks
- **Dataset viewer**: API for metadata, stats, and content of HF Hub datasets

Deployment & Inference/部署和推理
- **Inference Providers**: Call 200k+ models hosted by our 10+ Inference partners
- **Inference Endpoints (dedicated)**: Deploy models on dedicated & fully managed infrastructure on HF
- **Deploying on AWS**: Train/deploy models from Hugging Face to AWS with DLCs
- **Text Generation Inference**: Serve language models with TGI optimized toolkit
- **Text Embeddings Inference**: Serve embeddings models with TEI optimized toolkit
- **Microsoft Azure**: Deploy Hugging Face models on Microsoft Azure
- **Google Cloud**: Train and Deploy Hugging Face models on Google Cloud

Core ML Libraries/核心机器学习库
- **Transformers**: State-of-the-art AI models for PyTorch
- **Diffusers**: State-of-the-art Diffusion models in PyTorch
- **Datasets**: Access & share datasets for any ML tasks
- **Transformers.js**: State-of-the-art ML running directly in your browser
- **Tokenizers**: Fast tokenizers optimized for research & production
- **Evaluate**: Evaluate and compare models performance
- **timm**: State-of-the-art vision models: layers, optimizers, and utilities
- **Sentence Transformers**: Embeddings, Retrieval, and Reranking
- **Kernels**: Load and run compute kernels from the Hugging Face Hub

Training & Optimization/训练和优化
- **PEFT**: Parameter-efficient finetuning for large language models
- **Accelerate**: Train PyTorch models with multi-GPU, TPU, mixed precision
- **Optimum**: Optimize HF Transformers for faster training/inference
- **AWS Trainium & Inferentia**: Train/deploy Transformers/Diffusers on AWS
- **Google TPUs**: Train and Deploy models on Google TPUs via Optimum.
- **TRL**: Train transformers LMs with reinforcement learning
- **Safetensors**: Safe way to store/distribute neural network weights
- **Bitsandbytes**: Optimize and quantize models with bitsandbytes
- **Lighteval**: All-in-one toolkit to evaluate LLMs across multiple backends

Collaboration & Extras/协作和其他
- **Gradio**: Build ML demos and web apps with a few lines of Python
- **Trackio**: A lightweight, local-first, and free experiment tracking Python library
- **smolagents**: Smol library to build great agents in Python
- **LeRobot**: Making AI for Robotics more accessible with end-to-end learning
- **Reachy Mini**: Open-source expressive robot SDK for hackers and AI builders
- **AutoTrain**: AutoTrain API and UI for seamless model training
- **Chat UI**: Open source chat frontend powering HuggingChat
- **Leaderboards**: Create custom Leaderboards on Hugging Face
- **Argilla**: Collaboration tool for building high-quality datasets
- **Distilabel**: Framework for synthetic data generation and AI feedback
- **Xet**: Xet Protocol Specification

## Hub & Client Libraries/仓库和客户端库
### Hub
### Hub Python Library
### CLI
### Huggingface.js
### Tasks
### Dataset viewer

## Deployment & Inference/部署和推理
### Inference Providers
* https://huggingface.co/docs/inference-providers/index

Hugging Face’s Inference Providers give developers access to hundreds of machine learning models, powered by world-class inference providers. They are also integrated into our client SDKs (for JS and Python), making it easy to explore serverless inference of models on your favorite providers.

### Inference Endpoints (dedicated)
* https://huggingface.co/docs/inference-endpoints/index

Inference Endpoints is a managed service to deploy your AI model to production.

### Deploying on AWS
### Text Generation Inference
* https://huggingface.co/docs/text-generation-inference/index

Text Generation Inference (TGI) is a toolkit for deploying and serving Large Language Models (LLMs). TGI enables high-performance text generation for the most popular open-source LLMs, including Llama, Falcon, StarCoder, BLOOM, GPT-NeoX, and T5.

text-generation-inference is now in maintenance mode. TGI has initiated the movement for optimized inference engines to rely on a transformers model architectures. This approach is now adopted by downstream inference engines, which we contribute to and recommend using going forward: vllm, SGLang, as well as local engines with inter-compatibility such as llama.cpp or MLX.

### Text Embeddings Inference
* https://huggingface.co/docs/text-embeddings-inference/index

Text Embeddings Inference (TEI) is a comprehensive toolkit designed for efficient deployment and serving of open source text embeddings models. It enables high-performance extraction for the most popular models, including FlagEmbedding, Ember, GTE, and E5.

### Microsoft Azure
### Google Cloud

## Core ML Libraries/核心机器学习库
### Transformers
* https://huggingface.co/docs/transformers/index

Transformers acts as the model-definition framework for state-of-the-art machine learning models in text, computer vision, audio, video, and multimodal models, for both inference and training.

### Diffusers
* https://huggingface.co/docs/diffusers/index

Diffusers is a library of state-of-the-art pretrained diffusion models/预训练扩散模型 for generating videos, images, and audio.

### Datasets
* https://huggingface.co/docs/datasets/index

🤗 Datasets is a library for easily accessing and sharing AI datasets for Audio, Computer Vision, and Natural Language Processing (NLP) tasks.

### Transformers.js
* https://huggingface.co/docs/transformers.js/index

Run 🤗 Transformers directly in your browser, with no need for a server!

### Tokenizers
* https://huggingface.co/docs/tokenizers/index

Fast State-of-the-art tokenizers, optimized for both research and production

🤗 Tokenizers provides an implementation of today’s most used tokenizers, with a focus on performance and versatility. These tokenizers are also used in 🤗 Transformers.

### Evaluate
* https://huggingface.co/docs/evaluate/index

🤗 Evaluate: A library for easily evaluating machine learning models and datasets.

### timm
* https://huggingface.co/docs/timm/index

`timm` is a library containing SOTA(State-of-the-Art) computer vision models, layers, utilities, optimizers, schedulers, data-loaders, augmentations, and training/evaluation scripts.

It comes packaged with >700 pretrained models, and is designed to be flexible and easy to use.

### Sentence Transformers
* https://sbert.net/index.html

Sentence Transformers (a.k.a. SBERT) is the go-to Python module for using and training state-of-the-art embedding and reranker models/嵌入和重排序模型. It can be used to compute embeddings from text, images, audio, or video/从文本,图像,语音或视频计算嵌入 using **Sentence Transformer models** ([quickstart](https://sbert.net/docs/quickstart.html#sentence-transformer)), to calculate similarity scores/计算相似度分数 using **Cross-Encoder (a.k.a. reranker) models** ([quickstart](https://sbert.net/docs/quickstart.html#cross-encoder)), or to generate sparse embeddings/生成稀疏嵌入 using **Sparse Encoder models** ([quickstart](https://sbert.net/docs/quickstart.html#sparse-encoder)). This unlocks a wide range of applications, including [semantic search](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html)/语义搜索, [semantic textual similarity](https://sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html)/语义文本相似度, and [paraphrase mining](https://sbert.net/examples/sentence_transformer/applications/paraphrase-mining/README.html)/释义挖掘.

### Kernels
* https://huggingface.co/docs/kernels/index
* https://huggingface.co/kernels

**Kernels** are optimized compute modules you can load from the Hub to speed up training and inference.

The Kernel Hub allows Python libraries and applications to load compute kernels directly from the Hub. Kernels are **a first-class repository type on the Hub**, with dedicated pages that surface supported hardware and versions.

## Training & Optimization/训练和优化
### PEFT
* https://huggingface.co/docs/peft/index

🤗 PEFT (Parameter-Efficient Fine-Tuning/参数高效的微调) is a library for efficiently adapting large pretrained models to various downstream applications without fine-tuning all of a model’s parameters because it is prohibitively costly. PEFT methods only fine-tune a small number of (extra) model parameters - significantly decreasing computational and storage costs - while yielding performance comparable to a fully fine-tuned model. This makes it more accessible to train and store large language models (LLMs) on consumer hardware.

PEFT is integrated with the Transformers, Diffusers, and Accelerate libraries to provide a faster and easier way to load, train, and use large models for inference.

### Accelerate
* https://huggingface.co/docs/accelerate/index

Accelerate is a library that enables the same PyTorch code to be run across any distributed configuration by adding just four lines of code! In short, training and inference at scale made simple, efficient and adaptable.

### Optimum
* https://huggingface.co/docs/optimum/index

🤗 Optimum is an extension of Transformers that provides a set of performance optimization tools to train and run models on targeted hardware with maximum efficiency.

### AWS Trainium & Inferentia
### Google TPUs
### TRL
* https://huggingface.co/docs/trl/index

TRL(Transformers Reinforcement Learning/Transformer强化学习) is a full stack library where we provide a set of tools to train transformer language models with methods like Supervised Fine-Tuning (SFT)/监督式微调, Group Relative Policy Optimization (GRPO)/组相对策略优化, Direct Preference Optimization (DPO)/直接偏好优化, Reward Modeling/奖励模型, and more. The library is integrated with 🤗 transformers.

### Safetensors
* https://huggingface.co/docs/safetensors/index

Safetensors is a new simple format for storing tensors safely (as opposed to pickle) and that is still fast (zero-copy). Safetensors is really fast 🚀.

### Bitsandbytes
* https://huggingface.co/docs/bitsandbytes/index

bitsandbytes enables accessible large language models via k-bit quantization/量化 for PyTorch. bitsandbytes provides three main features for dramatically reducing memory consumption for inference and training:
- 8-bit optimizers uses block-wise quantization to maintain 32-bit performance at a small fraction of the memory cost.
- LLM.int8() or 8-bit quantization enables large language model inference with only half the required memory and without any performance degradation. This method is based on vector-wise quantization to quantize most features to 8-bits and separately treating outliers with 16-bit matrix multiplication.
- QLoRA/量化低秩自适应 or 4-bit quantization enables large language model training with several memory-saving techniques that don’t compromise performance. This method quantizes a model to 4-bits and inserts a small set of trainable low-rank adaptation (LoRA)/低秩自适应 weights to allow training.

### Lighteval
* https://huggingface.co/docs/lighteval/index

🤗 Lighteval is your all-in-one toolkit for evaluating Large Language Models (LLMs) across multiple backends with ease. Dive deep into your model’s performance by saving and exploring detailed, sample-by-sample results to debug and see how your models stack up.

## Collaboration & Extras/协作和其他
### Gradio
* https://github.com/gradio-app/gradio

Gradio is an open-source Python package that allows you to quickly **build** a demo or web application for your machine learning model, API, or any arbitrary Python function. You can then **share** a link to your demo or web application in just a few seconds using Gradio's built-in sharing features. No JavaScript, CSS, or web hosting experience needed!

### Trackio
* https://huggingface.co/docs/trackio/index

trackio is a lightweight, free experiment tracking Python library built on top of Hugging Face Datasets and Spaces 🤗.

### smolagents
* https://huggingface.co/docs/smolagents/index

smolagents is an open-source Python library designed to make it extremely easy to build and run agents using just a few lines of code.

### LeRobot
* https://huggingface.co/docs/lerobot/index

🤗 LeRobot aims to provide models, datasets, and tools for real-world robotics in PyTorch. The goal is to lower the barrier for entry to robotics so that everyone can contribute and benefit from sharing datasets and pretrained models.

### Reachy Mini
* https://huggingface.co/docs/reachy_mini/index

Reachy Mini is an open-source, expressive robot made for hackers and AI builders.

### AutoTrain
* https://huggingface.co/docs/autotrain/index

🤗 AutoTrain Advanced (or simply AutoTrain), developed by Hugging Face, is a robust no-code platform designed to simplify the process of training state-of-the-art models across multiple domains: Natural Language Processing (NLP), Computer Vision (CV), and even Tabular Data analysis. This tool leverages the powerful frameworks created by various teams at Hugging Face, making advanced machine learning and artificial intelligence accessible to a broader audience without requiring deep technical expertise.

This project is no longer maintained. No new features will be added and bugs will not be fixed. We recommend using [Axolotl](https://github.com/axolotl-ai-cloud/axolotl), [TRL](#trl), or [transformers.Trainer](https://huggingface.co/docs/transformers/main_classes/trainer).

### Chat UI
* https://huggingface.co/docs/chat-ui/index

Open source chat interface with support for tools, multimodal inputs, and intelligent routing across models. The app uses MongoDB and SvelteKit behind the scenes.

### Leaderboards

The Hub contains leaderboards and evaluations for machine learning models, including LLMs, chatbots, and more. There are three types of leaderboards:
- **Eval Results** from official benchmark datasets like GPQA, MMLU-Pro, or other datasets used in academic papers. When results are published in model repositories, the scores are are shown on the model page.
- **Community Managed Leaderboards** live on Spaces and are managed by the community for specific use cases.
- **Open LLM Leaderboard** was a project curated by the Hugging Face team to evaluate and rank open source LLMs and chatbots, and provide reproducible scores separating marketing fluff from actual progress in the field.

### Argilla
* https://github.com/argilla-io/argilla/

Argilla is a collaboration tool for AI engineers and domain experts to build high-quality datasets.

### Distilabel
* https://github.com/argilla-io/distilabel

Distilabel is the framework for synthetic data and AI feedback/合成数据和人工智能反馈 for engineers who need fast, reliable and scalable pipelines based on verified research papers.

### Xet
* https://huggingface.co/docs/xet/index

The Hugging Face Xet Protocol is an open-source, content-addressable storage protocol designed specifically to replace Git LFS (Large File Storage) on the Hugging Face Hub. Its primary purpose is to dramatically optimize how massive AI model weights and datasets are uploaded, stored, and downloaded by introducing chunk-level deduplication and smarter data transfer pipelines.

# Tasks
* https://huggingface.co/tasks
* https://huggingface.co/docs/transformers/main/en/task_summary

Hugging Face is the home for all Machine Learning tasks. Here you can find what you need to get started with a task: demos, use cases, models, datasets, and more!

Multimodal/多模态
- Any-to-Any/任意模态转换
- Audio-Text-to-Text/音频文本转文本
- Document Question Answering/文档问答
- Visual Document Retrieval/视觉文档检索
- Image-Text-to-Text/图像文本转文本
- Image-Text-to-Image/图像文本转图像
- Image-Text-to-Video/图像文本转视频
- Video-Text-to-Text/视频文本转文本
- Visual Question Answering/视觉问答

Natural Language Processing/自然语言处理
- Feature Extraction/特征提取
- Fill-Mask/填充掩码
- Question Answering/问答
- Sentence Similarity/句子相似度
- Summarization/文本摘要
- Table Question Answering/表格问答
- Text Classification/文本分类
- Text Generation/文本生成
- Text Ranking/文本排序
- Token Classification/词元分类
- Translation/翻译
- Zero-Shot Classification/零样本分类

Computer Vision/计算机视觉
- Depth Estimation/深度估计
- Image Classification/图像分类
- Image Feature Extraction/图像特征提取
- Image Segmentation/图像分割
- Image-to-Image/图像转图像
- Image-to-Text/图像转文本
- Image-to-Video/图像转视频
- Keypoint Detection/关键点检测
- Mask Generation/掩码生成
- Object Detection/目标检测
- Video Classification/视频分类
- Text-to-Image/文本转图像
- Text-to-Video/文本转视频
- Unconditional Image Generation/无条件图像生成
- Video-to-Video/视频到视频
- Zero-Shot Image Classification/零样本图像分类
- Zero-Shot Object Detection/零样本目标检测
- Text-to-3D/文本到3D模型
- Image-to-3D/图像到3D模型

Audio/音频
- Audio Classification/音频分类
- Audio-to-Audio/音频到音频
- Automatic Speech Recognition/自动语音识别
- Text-to-Speech/文本到语音

Tabular/表格
- Tabular Classification/表格分类
- Tabular Regression/表格回归

Reinforcement Learning/强化学习
- Reinforcement Learning


# Models
* https://huggingface.co/models

See Also
* [Hugging Face Gemma Recipes](https://github.com/huggingface/huggingface-gemma-recipes)

# Datasets
* https://huggingface.co/datasets

# Spaces: The AI App Directory
* https://huggingface.co/spaces

# Buckets
* https://huggingface.co/storage

# See Also
* [awesome-huggingface](https://github.com/huggingface/awesome-huggingface): A list of wonderful open-source projects & applications integrated with Hugging Face libraries.

papers
* [Daily Papers - HuggingFace](https://huggingface.co/papers)
* [Trending Papers - HuggingFace](https://huggingface.co/papers/trending)

# FAQ

- error message: Some parameters are on the meta device because they were offloaded to the cpu and disk.
```markdown
This error occurs because you used device_map="auto" to load a large model, but your system ran out of GPU VRAM and system RAM.
As a fallback, the Hugging Face transformers library offloaded the remaining parts of the model to your hard disk/CPU using PyTorch's virtual meta device [1]. The model cannot perform inference while its weights are stuck on this placeholder device [1].
Here are the step-by-step methods to fix this error, ranked from easiest to most robust.
------------------------------
## Solution 1: Use 8-bit or 4-bit Quantization (Recommended)
Quantization compresses the model size by 2x to 4x, allowing it to fit entirely inside your GPU VRAM without changing your hardware.

   1. Install the compression library:
   
   pip install bitsandbytes accelerate
   
   2. Modify your loading script to enable 4-bit precision:
   
   from transformers import AutoModelForCausalLM, BitsAndBytesConfigimport torch
   # Configure 4-bit loading to drastically reduce VRAM usagequantization_config = BitsAndBytesConfig(
       load_in_4bit=True,
       bnb_4bit_compute_dtype=torch.float16
   )
   model = AutoModelForCausalLM.from_pretrained(
       "your-model-name",
       quantization_config=quantization_config,
       device_map="auto"
   )
   
   
------------------------------
## Solution 2: Explicitly Enable the Disk Offload Folder
If you must run the model at full precision and have no choice but to use your hard drive as overflow memory, you must explicitly tell transformers where to write the temporary disk files and authorize their execution.
Pass an explicit offload_folder path into your loading function:

from transformers import AutoModelForCausalLM
model = AutoModelForCausalLM.from_pretrained(
    "your-model-name",
    device_map="auto",
    # Directs overflow parameters safely to a local folder instead of crashing on the meta device
    offload_folder="offload_dir" 
)

Note: While this fixes the crash, inference will be extremely slow because your hard drive is much slower than GPU memory.
------------------------------
## Solution 3: Load in Low CPU Memory Mode
If your machine has plenty of GPU VRAM but low system RAM (CPU memory), the initialization phase will fail before the weights ever reach the GPU.
Force the script to load the weights directly into the GPU, skipping the system RAM bottleneck:

from transformers import AutoModelForCausalLMimport torch
model = AutoModelForCausalLM.from_pretrained(
    "your-model-name",
    device_map="auto",
    torch_dtype=torch.float16, # Cuts the RAM required to open the files in half
    low_cpu_mem_usage=True     # Prevents loading full duplicate copies into system RAM
)

------------------------------
## Solution 4: Use a Smaller Model Sizing Tier
If your GPU VRAM is completely saturated (e.g., trying to run a 14B or 32B model on an 8GB or 12GB VRAM card), it simply will not run smoothly. Switch to a smaller model footprint tier within the same family (such as moving from a 14B model down to a 3B, 7B, or 8B variant).
To help narrow down the exact threshold, let me know:

* What is your GPU model and how much VRAM does it have?
* What is the exact name of the Hugging Face model you are trying to load?
```