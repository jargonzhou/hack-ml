"""
LlamaIndex with Ollama cloud models.
"""

from llama_index.core import Settings, set_global_handler
from llama_index.llms.ollama import Ollama
from llama_index.llms.lmstudio import LMStudio
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
# model_name = "gpt-oss:120b-cloud"
embed_model_name = "D:/software/huggingface/hub/models--google--embeddinggemma-300m/snapshots/57c266a740f537b4dc058e1b0cda161fd15afa75"

llm = Ollama(base_url='https://ollama.com',
             model=model_name,
             #  temperature=0.0
             )

# LM Studio
# llm = LMStudio(base_url='http://127.0.0.1:1234/v1',
#                model_name='google/gemma-4-e4b'
#                )

# embed_model = OllamaEmbedding(model_name=embed_model_name,
#                               base_url=base_url)
embed_model = HuggingFaceEmbedding(
    model_name=embed_model_name,
    device="cuda" if torch.cuda.is_available() else "cpu",
    model_kwargs={"local_files_only": True}
)

Settings.llm = llm
Settings.embed_model = embed_model
