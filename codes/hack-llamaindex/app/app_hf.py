"""
LlamaIndex with Hugging Face local models.
"""

# LlamaIndex Framework > Integrations > Llm > Hugging Face LLMs
# https://developers.llamaindex.ai/python/framework/integrations/llm/huggingface/

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings, set_global_handler
from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.callbacks import CallbackManager, LlamaDebugHandler
import torch

from dotenv import load_dotenv

env_path = ".env/hf.env"
load_dotenv(env_path)

# Bind globally BEFORE any index loading
debug_handler = LlamaDebugHandler(print_trace_on_end=True)
Settings.callback_manager = CallbackManager([debug_handler])
set_global_handler("simple")

# model_name = "google/gemma-4-E4B-it"
model_name = "google/gemma-3n-E4B-it"
# embed_model_name = "google/embeddinggemma-300m"
embed_model_name = "D:/software/huggingface/hub/models--google--embeddinggemma-300m/snapshots/57c266a740f537b4dc058e1b0cda161fd15afa75"

llm = HuggingFaceLLM(
    model_name=model_name,
    tokenizer_name=model_name,
    # trust_remote_code=True,
    model_kwargs={
        "dtype": torch.bfloat16,
        # "device_map": "auto",
        # "trust_remote_code": True,
    })
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

# asyncio version
#
# async def stream_main():
#   response = await query_engine.query(
#     "summarize each document in a few sentences"
#     )
#   async for token in response.response_gen:
#         print(token, end="", flush=True)
#   print()

# await stream_main()


#
# Output
#
# **********
# Trace: index_construction
#     |_CBEventType.NODE_PARSING -> 0.002976 seconds
#       |_CBEventType.CHUNKING -> 0.001032 seconds
#       |_CBEventType.CHUNKING -> 0.0 seconds
#     |_CBEventType.EMBEDDING -> 0.884317 seconds
# **********
# **********
# Trace: query
#     |_CBEventType.QUERY -> 174.220206 seconds
#       |_CBEventType.RETRIEVE -> 0.157818 seconds
#         |_CBEventType.EMBEDDING -> 0.153315 seconds
#       |_CBEventType.SYNTHESIZE -> 174.059388 seconds
#         |_CBEventType.TEMPLATING -> 0.0 seconds
#         |_CBEventType.LLM -> 174.045979 seconds
# **********
#
# The NLP document describes natural language processing as the processing of natural language information by computers, a subfield of computer science and artificial intelligence. It covers tasks like speech recognition, text classification, natural language understanding, and natural language generation. The document also mentions its relation to other fields like information retrieval and computational linguistics.
#
# The CV document describes computer vision as the extraction of information from digital images and understanding the world through visual data. It involves methods for acquiring, processing, analyzing, and understanding images to produce numerical or symbolic information.  Key areas within computer vision include scene reconstruction, object detection, and image restoration.
