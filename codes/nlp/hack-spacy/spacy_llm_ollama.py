from spacy_llm.util import assemble

import spacy

# from spacy import registry
# from spacy_llm.registry import registry
# from typing import Any, Iterable, List, Callable
# import requests

# ModelCallable = Callable[[Iterable[str]], Iterable[str]]


# # 注册自定义模型包装器


# @registry.llm_models("MyCustomOllamaModel.v1")
# def cache_ollama_model(name: str, base_url: str, temperature: float) -> ModelCallable:
#   # 这个内部函数就是实际执行推理的逻辑
#   def query(prompts: Iterable[str]) -> Iterable[str]:
#     responses = []
#     for prompt in prompts:
#       payload = {
#           "model": name,
#           "prompt": prompt,
#           "stream": False,
#           "options": {"temperature": temperature}
#       }
#       response = requests.post(base_url, json=payload, timeout=5)
#       response.raise_for_status()
#       # 根据 Ollama 的响应格式提取文本
#       responses.append(response.json().get("response", ""))
#     return responses
#   return query


nlp = assemble("config/llm-config.cfg")
content = """
As we saw on Chapter 6, Language Modeling is the task of
predicting the next token given the sequence of previous tokens.
[...]
Now that you know what LLMs are and how to interact with them,
let's use a spacy-llm component in a pipeline. In the next
section we're going to create a pipeline to summarize texts
using a LLM.
"""
doc = nlp(content)
print(doc._.summary)
# run 1 Output
# The text transitions from defining Language Modeling (predicting the next token) to practical application. It announces the use of the `spacy-llm` component within a pipeline, with the goal of creating a section that demonstrates how to summarize texts using an LLM.
# run 2 Output
# The text reviews Language Modeling (predicting the next token) and transitions to practical application. It announces that the next section will demonstrate how to use a `spacy-llm` component to build a pipeline for summarizing texts using a Large Language Model (LLM).
