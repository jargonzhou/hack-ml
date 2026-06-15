import streamlit as st
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.core import SQLDatabase
from llama_index.core.query_engine import NLSQLTableQueryEngine
import asyncio
from llama_index.core.workflow import Context
from llama_index.core.agent.workflow import AgentStream, ToolCallResult, AgentOutput
from llama_index.core.callbacks import CallbackManager, LlamaDebugHandler
from llama_index.core import Settings

from dotenv import dotenv_values
from sqlalchemy import create_engine

from app.constants.models import llm
from app.tool.sql import sql_schema_tool

# --- STAGE 1: APP CONFIG & INITIALIZATION ---
st.set_page_config(page_title="SQL Server Agent", page_icon="🛢️")
st.title("SQL Server Agent")


# Cache data loading so it doesn't re-run on every user click/interaction


@st.cache_resource(show_spinner="Initializing engine and loading data...")
def initialize_agent():
  env_path = ".env/db.env"
  config = dotenv_values(env_path)
  connection_string = config.get('connection_string') or ''
  scheme = config.get('scheme') or ''
  # print(connection_string)
  debug_handler = LlamaDebugHandler(print_trace_on_end=True)
  Settings.callback_manager = CallbackManager([debug_handler])

  engine = create_engine(connection_string)
  sql_database = SQLDatabase(engine=engine, schema=scheme)
  sql_query_engine = NLSQLTableQueryEngine(sql_database=sql_database, llm=llm)
  print("SQL Query Engine initialized.", sql_query_engine)

  sql_tool_description = """Useful for querying the corporate SQL Server database for business objects and metrics."""
  sql_tool = QueryEngineTool(
      query_engine=sql_query_engine,
      metadata=ToolMetadata(
          name="sql_server_tool",
          description=sql_tool_description,
      ),
  )

  # 4. Initialize the LLM and the ReActAgent
  return ReActAgent(tools=[sql_schema_tool, sql_tool],
                    llm=llm,
                    verbose=True)


# Instantiate or retrieve the cached agent
agent = initialize_agent()

# --- STAGE 2: MANAGING SESSION STATE CHAT HISTORY ---
if "messages" not in st.session_state:
  st.session_state.messages = [
      {"role": "assistant",
       "content": "Hello! I am a ReAct agent hooked up to your tools. Ask me anything!"}
  ]

# Render existing chat history from past turns
for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.write(message["content"])

# --- STAGE 3: CHAT INPUT & AGENT EXECUTION ---

# --- ASYNC GENERATOR INTEGRATING WITH WORKFLOW EVENTS ---


async def get_agent_stream(query: str):
  """
  Executes the workflow agent and yields beautifully formatted text 
  chunks and tool execution cards directly into the UI stream.
  """
  ctx = Context(workflow=agent)
  handler = agent.run(user_msg=query, ctx=ctx)

  async for event in handler.stream_events():
    print(f">>> {type(event)}: {event}")
    # Captures the ReAct loop's background planning steps ("Thought: I need to check the schema first")
    if isinstance(event, AgentOutput):
      # Extract the raw reasoning content
      raw_text = getattr(event.response, "content", "")
      if raw_text:
        # Strip out duplicate trailing details and keep it inside a clean card
        clean_thought = str(raw_text).strip()
        yield f"\n\n> 🧠 *{clean_thought}*\n\n"

    # Capture standard text streaming tokens
    if isinstance(event, AgentStream):
      yield event.delta

    # Capture and format tool execution results beautifully
    elif isinstance(event, ToolCallResult):
      # Clean up the output to prevent massive blocks from crashing the layout
      output_preview = str(event.tool_output).strip()
      if len(output_preview) > 1500:
        output_preview = output_preview[:1500] + \
            "\n... [Output truncated for readability] ..."

      # Choose appropriate syntax highlighting based on the tool used
      code_language = "sql" if "sql" in event.tool_name.lower() else "markdown"

      # Create a clean, visually distinct blockquote card for the UI stream
      tool_ui_card = (
          f"\n\n"
          f"> 🛠️ **Tool Executed:** `{event.tool_name}`\n"
          f"> * **Arguments passed:** `{event.tool_kwargs}`\n"
          f">\n"
          f"> ```{code_language}\n"
          f"> {output_preview}\n"
          f"> ```\n\n"
      )
      yield tool_ui_card


def streamlit_stream_wrapper(query: str):
  """Bridges the async stream into Streamlit's sync context."""
  loop = asyncio.new_event_loop()
  asyncio.set_event_loop(loop)

  async_gen = get_agent_stream(query)

  while True:
    try:
      chunk = loop.run_until_complete(async_gen.__anext__())
      yield chunk
    except StopAsyncIteration:
      break
  loop.close()


if user_query := st.chat_input("What would you like to know?"):

  # Display user message instantly
  st.session_state.messages.append({"role": "user", "content": user_query})
  with st.chat_message("user"):
    st.write(user_query)

  # Generate agent response inside an assistant layout bubble
  with st.chat_message("assistant"):
    # Optional: Add a spinner to give visual feedback during the ReAct reasoning loops
    with st.spinner("Thinking and executing tools..."):
      try:
        # Execute agent logic (using chat to maintain conversational history within the agent instance)
        # response = asyncio.run(agent.run(user_msg=user_query))
        # final_response = response.response
        # # Output final response to the UI
        # st.write(final_response)

        final_response = st.write_stream(streamlit_stream_wrapper(user_query))

        # Save to session state history
        st.session_state.messages.append(
            {"role": "assistant", "content": final_response})

      except Exception as e:
        st.error(f"An error occurred: {str(e)}")
