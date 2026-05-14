from dotenv import load_dotenv, dotenv_values
from langchain_openai import ChatOpenAI

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

env_path = ".env/hf.env"
load_dotenv(env_path)
config = dotenv_values(env_path)

openai_model = ChatOpenAI(
    # base_url=config.get('OLLAMA_BASE_URL') or '',
    base_url='http://localhost:11434/v1',
    model=config.get('OPENAI_MODEL_GEMMA4') or '',
    api_key=lambda: config.get('OPENAI_API_KEY') or '',
    temperature=0.7)

template = '''
Question: {question}
Answer: '''

prompt = PromptTemplate(
    template=template,
    input_variables=['question']
)
llm_chain = prompt | openai_model | StrOutputParser()

message = {
    "question": "Who is Steve Jobs"
}
# print(llm_chain.invoke(message))

for chunk in llm_chain.stream(message):
  print(chunk, end="", flush=True)
