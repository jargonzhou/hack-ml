
################################################################################
# 2. RAG Part I: Indexing Your Data
################################################################################

from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language
from langchain_community.document_loaders import TextLoader
from app.constants.models import OLLAMA_MODEL_EMBEDDING_GEMMA, OLLAMA_BASE_URL

_base_url = OLLAMA_BASE_URL
_embedding_model = OLLAMA_MODEL_EMBEDDING_GEMMA

# text
# HTML
# # !pip install beautifulsoup4
# from langchain_community.document_loaders import WebBaseLoader
# PDF
# # !pip install pypdf
# from langchain_community.document_loaders import PyPDFLoader


# embedding
# from langchain_openai import OpenAIEmbeddings


# from langchain.retrievers.multi_vector import MultiVectorRetriever
# from langchain.docstore.document import Document
# from langchain.indexes import SQLRecordManager, index
# from langchain_core.documents import Document
# # https://github.com/pgvector/pgvector
# from langchain_postgres.vectorstores import PGVector


# #  https://reference.langchain.com/python/langchain-ollama/embeddings/OllamaEmbeddings
# from langchain_ollama import OllamaEmbeddings

# # ColBERT
# # !pip install ragatouille
# from ragatouille import RAGPretrainedModel

#
# Converting Your Documents into Text
#
text_loader = TextLoader("data/Quantum_computing.txt")
docs = text_loader.load()
# print(docs)

#
# Splitting Your Text into Chunks
#
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(docs)
print(chunks)

# split code langauge
PYTHON_CODE = """
def hello_world():
print("Hello, World!")

# Call the function
hello_world()
"""
python_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=50, chunk_overlap=0
)
python_docs = python_splitter.create_documents([PYTHON_CODE])
print(python_docs)

# markdown
markdown_text = """
# LangChain
⚡ Building applications with LLMs through composability ⚡
## Quick Install
```bash
pip install langchain
```
As an open source project in a rapidly developing field, we are extremely open
to contributions.
"""
md_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN, chunk_size=60, chunk_overlap=0
)
md_docs = md_splitter.create_documents([markdown_text],
                                       [{"source": "https://www.langchain.com"}])
print(md_docs)

#
# Generating Text Embeddings
#

print(len(chunks))
embeddings_model = OllamaEmbeddings(
    base_url=_base_url,
    model=_embedding_model)


def batch_embed(embeddings_model, documents, batch_size=10):
  all_embeddings = []
  for i in range(0, len(documents), batch_size):
    batch = documents[i: i + batch_size]
    # 提取文本内容
    texts = [doc.page_content for doc in batch]
    # 处理当前批次
    try:
      vectors = embeddings_model.embed_documents(texts)
      all_embeddings.extend(vectors)
      print(f"已完成: {i + len(batch)} / {len(documents)}")
    except Exception as e:
      print(f"批次 {i} 出错: {e}")
  return all_embeddings


# embeddings = embeddings_model.embed_documents(
#     [chunk.page_content for chunk in chunks])
embeddings = batch_embed(embeddings_model=embeddings_model, documents=chunks)
print(embeddings)

# indexing optimization

# RAPTOR: Recursive Abstrative Processing for Tree-Organized Retrieval


# RAG = RAGPretrainedModel.from_pretrained("colbert-ir/colbertv2.0")
