import spacy
from app.data import knowledge_base, config

if __name__ == "__main__":
  nlp = spacy.load("zh_core_web_trf", config=config)
  doc = knowledge_base[0]
  print([token.text for token in nlp(doc)])
