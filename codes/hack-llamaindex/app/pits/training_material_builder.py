"""
This constructs the learning materials (slides and narration) based on the user’s current knowledge.
It utilizes uploaded and indexed materials to generate the learning content
"""

from llama_index.core import load_index_from_storage
from llama_index.core.storage import StorageContext
from llama_index.core.extractors import KeywordExtractor
# from llama_index.program.openai import OpenAIPydanticProgram
from llama_index.core.program import LLMTextCompletionProgram
# from llama_index.program.evaporate.df import DFRowsProgram
from llama_index.core.schema import TextNode
from llama_index.core.bridge.pydantic import BaseModel, Field

import pandas as pd
import streamlit as st
from collections import Counter
from typing import List

import nest_asyncio

from app.pits.global_settings import STORAGE_PATH, INDEX_STORAGE, CACHE_FILE, SLIDES_FILE
from app.pits.logging_functions import log_action
from app.pits.document_uploader import ingest_documents
from app.pits.slides import Slide, SlideDeck

from app.constants.models import llm


class DataRow(BaseModel):
  Section: str = Field(
      description="The section title extracted from the text.")
  Topics: str = Field(
      description="The matching topics extracted as a single string, separated by ','.")


class DataFrameOutput(BaseModel):
  rows: List[DataRow] = Field(description="List of all extracted data rows.")


def generate_slides(topic):
  nest_asyncio.apply()

  # llm = OpenAI(temperature=0.5, model="gpt-4-1106-preview", max_tokens=4096)

  with st.spinner("Loading documents..."):
    # either uploads everything or uses the cached documents to return the Nodes
    embedded_nodes = ingest_documents()
    st.info("Docs loaded!")
  with st.spinner("Preparing summaries and keywords..."):
    summary_nodes = []
    for node in embedded_nodes:
      # we create another set of nodes containing just the summaries
      summary = node.metadata["section_summary"]
      summary_node = TextNode(text=summary)
      summary_nodes.append(summary_node)

    # we extract keywords from summaries
    key_extractor = KeywordExtractor(keywords=10)
    entities = key_extractor.extract(summary_nodes)
    flattened_keywords = []
    for entity in entities:
      if 'excerpt_keywords' in entity:
        excerpt_keywords = entity['excerpt_keywords']
        flattened_keywords.extend([keyword.strip()
                                  for keyword in excerpt_keywords.split(',')])
    keyword_counts = Counter(flattened_keywords)

    # We sort keywords by their occurrences in descending order
    sorted_keywords = sorted(keyword_counts.items(),
                             key=lambda x: x[1], reverse=True)
    keywords_only = [keyword for keyword,
                     count in sorted_keywords if count > 1]

    # we eliminate any generic keywords not related to topic using LLM
    specific_keywords = ""
    for i in range(0, len(keywords_only), 15):
      group = keywords_only[i:i+15]
      group_str = ', '.join(group)  # Converts the list to a string
      response = llm.complete(
          f"Eliminate any keyword which is generic and not precisely specific to the topic of {topic}. Format as comma separated. List just the remaining keywords: " + group_str)
      specific_keywords += str(response) + ','
    st.info("Keywords and summaries prepared!")

  with st.spinner("Creating the course outline..."):
    _prompt_template = f"Create a structured course outline for a course about {topic}. The outline should be divided in sections and each section should be divided in several topics. Each section should have a sufficient number of topics to cover the entire knowledge area. The outline will contain a gradual introduction of concepts, starting with a general introduction on the subject and then covering more advanced areas. Respond with one line per section using this format: <SECTION TITLE, TOPIC 1, TOPIC 2, TOPIC 3, ... TOPIC n>. Make sure the outline completely covers these keywords: {specific_keywords}"
    # we generate the course outline using the LLM
    response = llm.complete(_prompt_template)
    print(">>> DEBUG, response:\n", response)

    df_parser_template_str = """Extract rows of data from the text and format them into the requested structure.
    Text input to analyze: {input_str}"""
    # df = pd.DataFrame({"Section": pd.Series(dtype="str"),
    #                   "Topics": pd.Series(dtype="str")})

    base_pydantic_program = LLMTextCompletionProgram.from_defaults(
        output_cls=DataFrameOutput,
        llm=llm,  # 传入你的 llm 实例
        prompt_template_str=df_parser_template_str,
    )

    # df_rows_program = DFRowsProgram.from_defaults(
    #     # pydantic_program_cls=OpenAIPydanticProgram,
    #     pydantic_program_cls=base_pydantic_program,
    #     prompt_template_str=df_parser_template_str,
    #     columns=list(df.columns),
    #     df=df)
    # result_obj = df_rows_program(input_str=response)
    # outline = result_obj.to_df(existing_df=df)

    result_obj = base_pydantic_program(input_str=response)
    outline = pd.DataFrame([row.model_dump() for row in result_obj.rows])

    # outline.to_csv('course_outline.csv', sep=';', index=False) # optional. we save the outline in a CSV file
    st.info("Course outline complete!")

  with st.spinner("Creating the course slides and narration. This might take a while..."):
    # load indexes from storage
    storage_context = StorageContext.from_defaults(persist_dir=INDEX_STORAGE)
    tree_index = load_index_from_storage(storage_context, index_id="tree")

    # outline = pd.read_csv('course_outline.csv', delimiter=';')
    # we build slides and narration for each slide
    slides = []
    for _, row in outline.iterrows():
      section = row['Section']
      topics = row['Topics'].split('; ')
      for slide_topic in topics:
        print(f"Generating content for: {section} - {slide_topic}")
        query_engine = tree_index.as_query_engine(response_mode="compact")
        narration = str(query_engine.query(
            f"You are an expert {topic} trainer. You are now covering the section titled '{section}'. Introduce and explain the concept of '{slide_topic}' to your students. Respond as you are the trainer."))
        summary = llm.complete(
            f"Summarize the essential concepts from this text as maximum 7 very short slide bullets without verbs: {narration}\n The general topic of the presentation is {topic}\n The slide title is {section+'-'+slide_topic} List the bullets separated with semicolons like this: BULLET1, BULLET2, ...: ")
        bullets = str(summary).split(';')
        # Create a new Slide object and add it to the list
        slide = Slide(section, slide_topic, narration, bullets)
        slides.append(slide)
    st.info("Slides and narration generated!")

  slide_deck = SlideDeck(topic, slides)
  slide_deck.save_to_file(SLIDES_FILE)
