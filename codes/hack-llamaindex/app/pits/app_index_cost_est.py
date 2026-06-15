"""
Estimate LLM cost of indexing.
"""

import tiktoken
from llama_index.core import TreeIndex, SimpleDirectoryReader, Settings, VectorStoreIndex
from llama_index.core.llms.mock import MockLLM
from llama_index.core.embeddings.mock_embed_model import MockEmbedding
from llama_index.core.callbacks import CallbackManager, TokenCountingHandler


embed_model = MockEmbedding(embed_dim=1536)
llm = MockLLM(max_tokens=256)
token_counter = TokenCountingHandler(
    tokenizer=tiktoken.encoding_for_model("gpt-3.5-turbo").encode)
callback_manager = CallbackManager([token_counter])

Settings.callback_manager = callback_manager
Settings.embed_model = embed_model
Settings.llm = llm

documents = SimpleDirectoryReader("data").load_data()

# index = TreeIndex.from_documents(
#     documents=documents,
#     num_children=2,
#     show_progress=True)
# print("Total LLM Token Count:", token_counter.total_llm_token_count)

index = VectorStoreIndex.from_documents(
    documents=documents,
    show_progress=True)
print("Embedding Token Count:", token_counter.total_embedding_token_count)

query_engine = index.as_query_engine()
response = query_engine.query("What's NLP?")
print("Query LLM Token Count:", token_counter.total_llm_token_count)
print("Query Embedding Token Count:", token_counter.total_embedding_token_count)
# print(response)

#
# Output
#
# Embedding Token Count: 381
# Query LLM Token Count: 669
# Query Embedding Token Count: 386
