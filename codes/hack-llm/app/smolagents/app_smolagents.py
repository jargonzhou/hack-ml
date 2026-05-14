from openai import timeout
from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel, PythonInterpreterTool, tool

model = LiteLLMModel(
    # Local
    model_id="ollama/gemma4:e4b",
    api_base="http://127.0.0.1:11434",
    # Cloud
    # model_id="gemma4:31b-cloud",
    # api_base="https://ollama.com",
    num_ctx=8192,
    timeout=120
)


def plan_travel():
  agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)
  task = "How long does it take to travel from New York to Los Angeles by train?"
  response = agent.run(
      task=task,
      stream=True)

  for message in response:
    print(message)


def cal_fibonacci():
  agent = CodeAgent(tools=[PythonInterpreterTool()], model=model)
  task = "Calculate the 10th Fibonacci number."
  response = agent.run(
      task=task,
      stream=True)

  for message in response:
    print(message)


@tool
def get_xxx_info() -> str:
  """Get information of xxx."""
  return "The information of xxx is 'less is more'."


def custom_tool():
  agent = CodeAgent(tools=[get_xxx_info], model=model)
  task = "Show me the info about xxx."
  response = agent.run(
      task=task,
      stream=True)

  for message in response:
    print(message)


if __name__ == "__main__":
  custom_tool()
