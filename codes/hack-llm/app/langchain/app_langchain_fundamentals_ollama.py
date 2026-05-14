"""
Learning LangChain - 1. LLM Fundamentals with LangChain
"""

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import CommaSeparatedListOutputParser
from pydantic import BaseModel
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, ChatMessage
from langchain_ollama import ChatOllama
from langchain_ollama import OllamaLLM

from app.constants.models import OLLAMA_MODEL_GEMMA4_CLOUD, OLLAMA_CLOUD_BASE_URL

_base_url = OLLAMA_CLOUD_BASE_URL
_model = OLLAMA_MODEL_GEMMA4_CLOUD


################################################################################
# LLM
################################################################################

# Key init args — generation params:
#     model: str/模型
#         Name of the Ollama model to use (e.g. `'llama4'`).
#     temperature: float | None/采样温度
#         Sampling temperature. Higher values make output more creative.
#     num_predict: int | None/预测token最大数量
#         Maximum number of tokens to predict.
#     top_k: int | None/下一个token的最大可能token数量
#         Limits the next token selection to the K most probable tokens.
#     top_p: float | None
#         Nucleus sampling parameter. Higher values lead to more diverse text.
#     mirostat: int | None
#         Enable Mirostat sampling for controlling perplexity.
#     seed: int | None
#         Random number seed for generation reproducibility.

# Key init args — client params:
#     base_url:
#         Base URL where Ollama server is hosted.
#     keep_alive:
#         How long the model stays loaded into memory.
#     format:
#         Specify the format of the output.

model = OllamaLLM(
    base_url=_base_url,
    model=_model,
    reasoning=False,
    temperature=0.7,
    num_predict=256,
)

res = model.invoke("Who are you?")
print(res)

################################################################################
# Chat model
################################################################################

# Key init args — completion params:
#     model: str
#         Name of Ollama model to use.
#     reasoning: bool | None
#         Controls the reasoning/thinking mode for
#         [supported models](https://ollama.com/search?c=thinking).

#         - `True`: Enables reasoning mode. The model's reasoning process will be
#             captured and returned separately in the `additional_kwargs` of the
#             response message, under `reasoning_content`. The main response
#             content will not include the reasoning tags.
#         - `False`: Disables reasoning mode. The model will not perform any reasoning,
#             and the response will not include any reasoning content.
#         - `None` (Default): The model will use its default reasoning behavior. Note
#             however, if the model's default behavior *is* to perform reasoning, think tags
#             (`<think>` and `</think>`) will be present within the main response content
#             unless you set `reasoning` to `True`.
#     temperature: float
#         Sampling temperature. Ranges from `0.0` to `1.0`.
#     num_predict: int | None
#         Max number of tokens to generate.
model = ChatOllama(
    base_url=_base_url,
    model=_model,
    reasoning=False,
    temperature=0.7,
    num_predict=256,
)

# prompt = [HumanMessage('What is the captial of France?')]
# model.invoke(prompt)

system_msg = SystemMessage(
    'You are a helpful assistant that responds to questions with three exclamation marks.')
human_msg = HumanMessage('What is the capital of France?')
res = model.invoke([system_msg, human_msg])
print(res)

################################################################################
# Prompt template
################################################################################


template = PromptTemplate.from_template("""Answer the question based on the
context below. If the question cannot be answered using the information
provided, answer with "I don't know".
Context: {context}
Question: {question}
Answer: """)

prompt = template.invoke({
    "context": """The most recent advancements in NLP are being driven by Large
Language Models (LLMs). These models outperform their smaller
counterparts and have become invaluable for developers who are creating
applications with NLP capabilities. Developers can tap into these
models through Hugging Face's `transformers` library, or by utilizing
OpenAI and Cohere's offerings through the `openai` and `cohere`
libraries, respectively.""",
    "question": "Which model providers offer LLMs?"
})

model = OllamaLLM(
    base_url=_base_url,
    model=_model,
    reasoning=False,
    temperature=0.7,
    num_predict=256,
)
print(model.invoke(prompt))

chat_template = ChatPromptTemplate.from_messages([
    ('system', '''Answer the question based on the context below. If the question cannot be answered using the information provided, answer with "I don\'t know".'''),
    ('human', 'Context: {context}'),
    ('human', 'Question: {question}'),
])
chat_prompt = chat_template.invoke({
    "context": """The most recent advancements in NLP are being driven by
Large Language Models (LLMs). These models outperform their smaller
counterparts and have become invaluable for developers who are creating
applications with NLP capabilities. Developers can tap into these 
models through Hugging Face's `transformers` library, or by utilizing
OpenAI and Cohere's offerings through the `openai` and `cohere`
libraries, respectively.""",
    "question": "Which model providers offer LLMs?"
})

model = ChatOllama(
    base_url=_base_url,
    model=_model,
    reasoning=False,
    temperature=0.7,
    num_predict=256,
)
print(model.invoke(chat_prompt))

################################################################################
# JSON output
################################################################################


class AnswerWithJustification(BaseModel):
  '''An answer to the user's question along with justification for the answer.'''
  answer: str
  '''The answer to the user's question'''
  justification: str
  '''Justification for the answer'''


llm = ChatOllama(base_url=_base_url,
                 model=_model,
                 temperature=0,
                 reasoning=False)
structured_llm = llm.with_structured_output(AnswerWithJustification)
structured_llm.invoke(
    'What weighs more, a pound of bricks or a pound of feathers')

################################################################################
# Output parsers
################################################################################

parser = CommaSeparatedListOutputParser()
parser.invoke('apple, banana, cheery')

################################################################################
# Assemble
# LECL: LangChain Expression Language
################################################################################


template = ChatPromptTemplate.from_messages([
    ('system', 'You are a helpful assistant.'),
    ('human', '{question}'),
])

model = ChatOllama(base_url=_base_url,
                   model=_model,
                   temperature=0,
                   reasoning=False)
chatbot = template | model
# sync
# alternative: stream, async
chatbot.invoke({"question": "Which model providers offer LLMs?"})
