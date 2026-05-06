import spacy
from app.data import entity_ruler_patterns, knowledge_base


# 1. 加载中型模型并注入纺织业专家知识
nlp = spacy.load("zh_core_web_lg")

ruler = nlp.add_pipe("entity_ruler", before="ner")
ruler.add_patterns(entity_ruler_patterns)


class SpaceyQA:
  def __init__(self, documents):
    self.kb_docs = [sent for doc in documents for sent in nlp(doc).sents]

  def ask(self, question):
    q_doc = nlp(question)

    # A. 提取问题中的实体和类型
    q_entities = [(ent.text, ent.label_) for ent in q_doc.ents]

    best_match = None
    max_score = -1

    for kb_doc in self.kb_docs:
      # 基础语义相似度
      base_similarity = q_doc.similarity(kb_doc)

      # B. NER 优化权重：检查实体覆盖
      bonus = 0
      for q_ent_text, _ in q_entities:
        # 如果知识库句子中包含了问题里的特定实体，给予权重补偿
        if any(k_ent.text == q_ent_text for k_ent in kb_doc.ents):
          bonus += 0.2  # 实体命中加分

        # 如果问题暗含某种类型需求（如问“什么工艺”），检查句子是否包含该类型
        if "工艺" in question and any(k_ent.label_ == "纺织工艺" for k_ent in kb_doc.ents):
          bonus += 0.15  # 类型匹配加分

      final_score = base_similarity + bonus

      if final_score > max_score:
        max_score = final_score
        best_match = kb_doc.text

    return best_match if max_score > 0.6 else "未找到匹配信息"


if __name__ == "__main__":
  # 初始化问答系统
  qa_system = SpaceyQA(knowledge_base)

  # 提问测试
  print(qa_system.ask("什么是涤纶？"))
  print(qa_system.ask("如何让纱线更平滑？"))
