from typing import List, Dict
import spacy
from spacy.language import Language
from fastapi import FastAPI
from pydantic import BaseModel


class TextToExtractEntities(BaseModel):
  record_id: str
  text: str


class TextsRequest(BaseModel):
  values: List[TextToExtractEntities]


class EntityExtractor:
  def __init__(
      self, nlp: Language, record_id_col_key: str = "record_id", record_text_col_key: str = "text"
  ):
    self.nlp = nlp
    self.record_id_col_key = record_id_col_key
    self.record_text_col_key = record_text_col_key

  def extract_entities(self, records: List[Dict[str, str]]):
    ids = (item[self.record_id_col_key] for item in records)
    texts = (item[self.record_text_col_key] for item in records)

    response = []

    for doc_id, spacy_doc in zip(ids, self.nlp.pipe(texts)):
      entities = {}
      for ent in spacy_doc.ents:
        ent_name = ent.text

        if ent_name not in entities:
          entities[ent_name] = {
              "name": ent_name,
              "label": ent.label_,
              "matches": [],
          }

        entities[ent_name]["matches"].append(
            {"char_start": ent.start_char, "char_end": ent.end_char, "text": ent.text}
        )

      response.append(
          {"record_id": doc_id, "entities": list(entities.values())})
    return response


app = FastAPI()

spacy_model = "../../pipelines/ner_fashion_brands_with_base_entities"
app_nlp = spacy.load(spacy_model)
extractor = EntityExtractor(app_nlp)


@app.get("/")
def root():
  return {"message": "Hello World"}


@app.post("/entities")
def extract_entities(body: TextsRequest):
  """Extract Named Entities from a batch of Records."""
  documents = []

  for item in body.values:
    documents.append({"record_id": item.record_id, "text": item.text})

  entities_result = extractor.extract_entities(documents)

  response = [
      {"record_id": er["record_id"], "data": {"entities": er["entities"]}}
      for er in entities_result
  ]

  return {"values": response}
