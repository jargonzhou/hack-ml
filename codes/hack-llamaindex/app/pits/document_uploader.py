"""
This interfaces with LlamaIndex to ingest and index uploaded Documents
"""

from llama_index.core.extractors import SummaryExtractor
from llama_index.core.text_splitter import TokenTextSplitter
from llama_index.core import SimpleDirectoryReader
from llama_index.core.ingestion import IngestionPipeline, IngestionCache

import pathlib
import nest_asyncio

from app.pits.global_settings import STORAGE_PATH, CACHE_FILE
from app.pits.logging_functions import log_action
from app.constants.models import embed_model

# RuntimeError: Detected nested async. Please use nest_asyncio.apply() to allow nested
# event loops.Or, use async entry methods like `aquery()`, `aretriever`, `achat`, etc.
nest_asyncio.apply()


def ingest_documents():
  print("Ingest document: ", pathlib.Path(STORAGE_PATH).resolve())
  documents = SimpleDirectoryReader(
      pathlib.Path(STORAGE_PATH).absolute(),
      recursive=True,
      filename_as_id=True,
      exclude_hidden=False).load_data()
  for doc in documents:
    print(doc.id_)
    log_action(f"File '{doc.id_}' uploaded user",
               action_type="UPLOAD")

  try:
    cached_hashes = IngestionCache.from_persist_path(CACHE_FILE)
    print("Cache file found. Running using cache...")
  except Exception:
    cached_hashes = ""
    print("No cache file found. Running without...")

  pipeline = IngestionPipeline(
      transformations=[
          TokenTextSplitter(
              chunk_size=1024,
              chunk_overlap=20
          ),
          SummaryExtractor(summaries=['self']),
          embed_model
      ],
      cache=cached_hashes
  )
  nodes = pipeline.run(documents=documents)
  pipeline.cache.persist(CACHE_FILE)
  return nodes
