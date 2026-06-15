from llama_index.core import Document, SummaryIndex
from llama_index.core.node_parser import SimpleNodeParser
# from llama_index.readers.wikipedia import WikipediaReader
from app.pits.wikipedia_fixed import FixedWikipediaReader
import logging

# for side effect
from app.constants.models import llm, embed_model

logging.basicConfig(level=logging.DEBUG)

loader = FixedWikipediaReader()
documents = loader.load_data(pages=[
    "Artificial intelligence",
    # "Messi Lionel"
])
# print(documents)
parser = SimpleNodeParser.from_defaults()
nodes = parser.get_nodes_from_documents(documents)

index = SummaryIndex(nodes)
query_engine = index.as_query_engine()

# print("Ask me anything about Lionel Messi!")
# while True:
#   question = input("Your question: ")
#   if question.lower() == "exit":
#     break
# question = "What is Messi's hometown?"
question = "What are subprinciples of Artificial intelligence?"
response = query_engine.query(question)
print(response)


#
# Output
#
# **********
# Trace: query
#     |_CBEventType.QUERY -> 7.126755 seconds
#       |_CBEventType.SYNTHESIZE -> 7.124757 seconds
#         |_CBEventType.TEMPLATING -> 0.0 seconds
#         |_CBEventType.LLM -> 7.0857 seconds
# **********
# The general problem of simulating or creating intelligence has been broken into several subproblems, which are specific traits or capabilities researchers expect an intelligent system to display. These include:

# *   **Reasoning and problem-solving:** Developing algorithms that imitate human step-by-step reasoning, such as logical deductions and solving puzzles, as well as methods for dealing with incomplete or uncertain information.
# *   **Knowledge representation:** Using knowledge engineering and formal representations (like knowledge bases and ontologies) to allow programs to make deductions about real-world facts and answer questions intelligently.
# *   **Planning and decision-making:** Creating rational agents that perceive their environment and take actions to achieve specific goals or maximize "expected utility" based on preferences.
# *   **Learning:** The study of programs that automatically improve their performance on tasks, including supervised learning (classification and regression), unsupervised learning, reinforcement learning, transfer learning, and deep learning.
# *   **Natural language processing (NLP):** Enabling programs to communicate in human languages, including tasks like speech recognition, machine translation, and question answering.
# *   **Perception:** The ability to deduce aspects of the world using sensor input, which includes computer vision (analyzing visual input), facial recognition, and object tracking.
# *   **Social intelligence:** Systems that recognize, process, or simulate human emotions and moods, a field known as affective computing.
# *   **General intelligence:** The pursuit of artificial general intelligence (AGI) that can solve a wide variety of problems with versatility and breadth similar to human intelligence.
