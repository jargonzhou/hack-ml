"""
LlamaIndex with Ollama cloud models.
"""

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings, set_global_handler
from llama_index.llms.ollama import Ollama
# from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.callbacks import CallbackManager, LlamaDebugHandler
import torch

from dotenv import load_dotenv
# import os
env_path = ".env/ollama.env"
load_dotenv(dotenv_path=env_path, override=True)

# print(os.environ['OLLAMA_API_KEY'])

# Bind globally BEFORE any index loading
debug_handler = LlamaDebugHandler(print_trace_on_end=True)
Settings.callback_manager = CallbackManager([debug_handler])
set_global_handler("simple")

model_name = "gemma4:31b-cloud"
embed_model_name = "D:/software/huggingface/hub/models--google--embeddinggemma-300m/snapshots/57c266a740f537b4dc058e1b0cda161fd15afa75"
base_url = "https://ollama.com"

llm = Ollama(model=model_name,
             base_url=base_url)

# embed_model = OllamaEmbedding(model_name=embed_model_name,
#                               base_url=base_url)
embed_model = HuggingFaceEmbedding(
    model_name=embed_model_name,
    device="cuda" if torch.cuda.is_available() else "cpu",
    model_kwargs={"local_files_only": True}
)

Settings.llm = llm
Settings.embed_model = embed_model

# indexig
documents = SimpleDirectoryReader('data').load_data()
index = VectorStoreIndex.from_documents(documents)

# query
query_engine = index.as_query_engine()
response = query_engine.query(
    "summarize each document in a few sentences"
)
print(response)

#
# Output
#
# **********
# Trace: index_construction
#     |_CBEventType.NODE_PARSING -> 0.003175 seconds
#       |_CBEventType.CHUNKING -> 0.000526 seconds
#       |_CBEventType.CHUNKING -> 0.0 seconds
#     |_CBEventType.EMBEDDING -> 0.812644 seconds
# **********
# **********
# Trace: query
#     |_CBEventType.QUERY -> 1.831965 seconds
#       |_CBEventType.RETRIEVE -> 0.12418 seconds
#         |_CBEventType.EMBEDDING -> 0.12116 seconds
#       |_CBEventType.SYNTHESIZE -> 1.705783 seconds
#         |_CBEventType.TEMPLATING -> 0.0 seconds
#         |_CBEventType.LLM -> 1.681772 seconds
# **********
# **nlp.txt**: Natural language processing is a subfield of computer science and artificial intelligence focused on the computer processing of natural language information. It is related to linguistics, knowledge representation, and information retrieval, with primary tasks including text classification, speech recognition, natural language generation, and natural language understanding.

# **cv.txt**: Computer vision is a discipline concerned with the theory and application of artificial systems that extract, analyze, and understand information from digital images or high-dimensional real-world data. This process transforms visual data into symbolic descriptions to elicit action using models based on learning theory, physics, geometry, and statistics. Subdisciplines include object detection, scene reconstruction, video tracking, and image restoration, among others.
