import spacy
from app.data import entity_ruler_patterns, knowledge_base, config

nlp = spacy.load("zh_core_web_trf", config=config)
ruler = nlp.add_pipe("entity_ruler", before="ner")
ruler.add_patterns(entity_ruler_patterns)


class SpaceyNER:
  def __init__(self, documents):
    self.kb_docs = [sent for doc in documents for sent in nlp(doc).sents]

  def collect(self):
    res = []
    for kb_doc in self.kb_docs:
      res.extend([(ent.text, ent.label_) for ent in kb_doc.ents])
      # TODO: zero-shot NER
      # print(list(kb_doc.vocab.strings))
    return res


if __name__ == "__main__":
  ner_system = SpaceyNER(knowledge_base)
  print(ner_system.collect())
