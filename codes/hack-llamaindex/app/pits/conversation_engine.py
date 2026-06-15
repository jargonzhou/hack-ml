"""
This manages the conversational side panel, responding to user queries and providing explanations. 
It also keeps track of the context of conversations with the tutor to avoid repetition and ensure relevant assistance. 
It also retrieves summaries of previous discussions and ensures the tutor picks up where it left off
"""

# FIXME: chat history

import streamlit as st
from llama_index.core import load_index_from_storage
from llama_index.core import StorageContext
# from llama_index.core.memory import ChatMemoryBuffer # Deprecated: Please use `llama_index.core.memory.Memory` instead.
from llama_index.core.memory import Memory
from llama_index.core.tools import QueryEngineTool, ToolMetadata
# from llama_index.agent.openai import OpenAIAgent
from llama_index.core.agent.workflow import FunctionAgent

from llama_index.core.storage.chat_store import SimpleChatStore

from app.pits.global_settings import INDEX_STORAGE, CONVERSATION_FILE
from app.constants.models import llm

# import asyncio

# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)


def load_chat_store():
  try:
    chat_store = SimpleChatStore.from_persist_path(CONVERSATION_FILE)
  except FileNotFoundError:
    chat_store = SimpleChatStore()
  return chat_store


def display_messages(chat_store, container):
  with container:
    for message in chat_store.get_messages(key="0"):
      with st.chat_message(message.role):
        st.markdown(message.content)


def initialize_chatbot(user_name, study_subject,
                       chat_store: SimpleChatStore, container, context):

  # memory = ChatMemoryBuffer.from_defaults(token_limit=3000,
  #                                         chat_store=chat_store,
  #                                         chat_store_key="0")
  memory = Memory.from_defaults(token_limit=3000)
  storage_context = StorageContext.from_defaults(persist_dir=INDEX_STORAGE)
  index = load_index_from_storage(storage_context, index_id="vector")
  study_materials_engine = index.as_query_engine(similarity_top_k=3)
  study_materials_tool = QueryEngineTool(
      query_engine=study_materials_engine,
      metadata=ToolMetadata(name="study_materials",
                            description=(f"Provides official information about "
                                         f"{study_subject}. Use a detailed plain "
                                         f"text question as input to the tool."),))
  # agent = OpenAIAgent.from_tools(tools=[study_materials_tool],
  #                                memory=memory,
  #                                system_prompt=(f"Your name is PITS, a personal tutor. Your "
  #                                               f"purpose is to help {user_name} study and "
  #                                               f"better understand the topic of: "
  #                                               f"{study_subject}. We are now discussing the "
  #                                               f"slide with the following content: {context}"))
  agent = FunctionAgent(tools=[study_materials_tool],
                        llm=llm,
                        system_prompt=(f"Your name is PITS, a personal tutor. Your "
                                       f"purpose is to help {user_name} study and "
                                       f"better understand the topic of: "
                                       f"{study_subject}. We are now discussing the "
                                       f"slide with the following content: {context}"))
  display_messages(chat_store, container)
  return agent, memory


async def chat_interface(agent: FunctionAgent, memory: Memory, chat_store: SimpleChatStore, container):
  prompt = st.chat_input("Type your question here:")
  if prompt:
    with container:
      with st.chat_message("user"):
        st.markdown(prompt)
      # TODO: more agent hacking
      res = await agent.run(user_msg=prompt, memory=memory)
      response = str(res)
      with st.chat_message("assistant"):
        st.markdown(response)
    chat_store.persist(CONVERSATION_FILE)
