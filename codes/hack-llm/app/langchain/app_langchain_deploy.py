
################################################################################
# 9. Deployment: Launching Your AI Application into Production
################################################################################
# !pip install "langgraph-cli[inmem]"
# !bash langchain_runs.sh


# Client SDK
from langgraph_sdk import get_client
# only pass the url argument to get_client() if you changed the default port
# when calling langgraph up
client = get_client(url='http://127.0.0.1:2024')
# Using the graph deployed with the name "agent"
assistant_id = "agent"
thread = await client.threads.create()
# 如何调试失败???
input = {"messages": [
    {
        "role": "user",
        "content": "1 + 1 = ?"
        # "content": "What's the time now?"
    }
]}
async for chunk in client.runs.stream(
    thread["thread_id"],
    assistant_id,
    input=input,
    stream_mode="updates",
):
  print(f"Receiving new event of type: {chunk.event}...")
  print(chunk.data)
  print("\n\n")
