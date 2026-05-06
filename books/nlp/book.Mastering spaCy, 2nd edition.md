# Mastering spaCy: Build structured NLP solutions with custom components and models powered by spacy-llm

- Part 1: Getting Started with spaCy: 1-2
- Part 2: Advanced Linguistic and Semantic Analysis: 3-6
- Part 3: Customizing and Integrating NLP Workflows: 7-11

# 1: Getting Started with spaCy
## Overview of spaCy
- A high-level overview of the spaCy library
## Installing spaCy
## Installing spaCy’s language models/语言模型
- Installing a language model
## Visualization/可视化 with displaCy
- Getting started with displaCy
- Entity visualizer
- Using displaCy with pure Python
- Using displaCy in Jupyter notebooks

# 2: Core Operations with spaCy
## Overview of spaCy conventions

language process pipeline: Text -> Tokenizer -> POS Tagger -> DependencyParser -> EntityRecognizer -> ... -> `Doc`

## Introducing Tokenization/分词
- Customizing the tokenizer
- Debugging the tokenizer
- Sentence segmentation
## Understanding lemmatization/词形还原
- Lemmatization in NLU
## spaCy container objects
- `Doc`
- `Token`
- `Span`
## More spaCy Token features

# 3: Extracting Linguistic Features/提取语言特征
## What is POS tagging/词性标记?
- Word-Sense Disambiguation (WSD)/词义消歧义

English
- **Verb/动词**: 表示动作或状态
- **Noun/名词**: 指人、地点或事物，或指代其中的特定部分（专有名词）
- **Pronoun/代词**: 可以代替名词或名词短语
- **Determiner/限定词**: 放在名词前，表示数量或阐明名词所指的内容 - 简而言之，是名词的引语
- **Adjective/形容词**: 修饰名词或代词
- **Adverb/副词**: 修饰动词、形容词或其他副词
- **Preposition/介词**: 连接名词/代词与句子的其他部分
- **Conjunction/连词**: 连接单词、从句和句子
- **Interjection/感叹词**: 以突然而感叹的方式表达情感

## Introduction to dependency parsing/依存句法分析
- Dependency relations
- Syntactic relations

dependency labels
- **amod**: Adjectival modifier/形容词修饰语
- **aux**: Auxiliary/助动词
- **compound**: Compound/复合词
- **dative**: Dative object/与格宾语
- **det**: Determiner/限定词
- **dobj**: Direct object/直接宾语
- **nsubj**: Nominal subject/名词性主语
- **nsubjpass**: Nominal subject, passive/名词性主语(被动语态)
- **nummod**: Numeric modifier/数词修饰语
- **poss**: Possessive modifier/所有格修饰语
- **root**: The root/根

## Introducing NER/命名实体识别

entity types
- `PERSON`: People, including fictional
- `NORP`: Nationalities or religious or political groups
- `FAC`: Buildings, airports, highways, bridges, and so on
- `ORG`: Companies, agencies, institutions, and so on
- `GPE`: Countries, cities, states
- `LOC`: Non-GPE locations, mountain ranges, bodies of water
- `PRODUCT`: Objects, vehicles, foods, and so on (not services)
- `EVENT`: Named hurricanes, battles, wars, sports events, and so on
- `WORK_OF_ART`: Titles of books, songs, and so on
- `LAW`: Named documents made into laws
- `LANGUAGE`: Any named language
- `DATE`: Absolute or relative dates or periods
- `TIME`: Times smaller than a day
- `PERCENT`: Percentage, including %
- `MONEY`: Monetary values, including unit
- `QUANTITY`: Measurements, as of weight or distance
- `ORDINAL`: first, second, and so on
- `CARDINAL`: Numerals that do not fall under another type

## Merging and splitting tokens

# 4: Mastering Rule-Based Matching/基于规则的匹配
## Token-based matching
- Extended syntax support
- Token attributes
- Regex-like operators
- Regex support
- Matcher online demo: https://demos.explosion.ai/matchers

pattern format/attribute
```json
[
  {"LOWER": "i"},
  {"LEMMA": {"IN": ["like", "love"]}},
  {"POS": "NOUN", "OP": "+"}
]
```

operator/quantifier/`OP`
```json
[
  {"POS": "ADJ", "OP": "*"},
  {"POS": "NOUN", "OP": "+"}
  {"POS": "PROPN", "OP": "{2}"}
]
```

pattern in dictionary of properties/attributes
```json
[
  {"LEMMA": {"IN": ["like", "love", "enjoy"]}},
  {"POS": "PROPN", "LENGTH": {">=": 10}},
]
```


## Creating patterns with `PhraseMatcher`

`attr`
- `LOWER`
- `SHAPE`

## Creating patterns with `SpanRuler`

`config`
- `annotate_ents`
- `overwrite`

## Combining spaCy models and matchers
- Extracting an IBAN
- Extracting phone numbers
- Extracting mentions
- Hashtag extraction
- Expanding named entities

# 5: Extracting Semantic Representations/语义表示 with spaCy Pipelines
## Extracting named entities with SpanRuler
- Getting to know the ATIS dataset
- Defining LOCATION entities
- Adding the SpanRuler component to our processing pipeline
## Extracting dependency relations with DependencyMatcher
- Linguistic primer
- Matching patterns with the DependencyMatcher component
## Creating a pipeline component using extension attributes
## Running the pipeline with large datasets

# 6: Utilizing spaCy with Transformers
## Transformers and transfer learning/迁移学习
- From LSTMs to Transformers
## Text classification with spaCy
- Training the TextCategorizer component
## Using Hugging Face transformers in spaCy
- The Transformer component
- spaCy’s configuration system
- Training the TextCategorizer with a config file
- BERT and RoBERTa
- Training the TextCategorizer with a transformer

# 7: Enhancing NLP Tasks Using LLMs with spacy-llm
## LLMs and prompt engineering basics
## Text summarization with LLMs and spacy-llm
## Creating custom spacy-llm tasks

# 8: Training an NER Component with Your Own Data
## Getting started with data preparation
- Do spaCy models perform well enough on your data?
- Does your domain include many labels that are absent in spaCy models?
- Annotating and preparing data
## Training an NER pipeline component
- Evaluating the accuracy of the NER component
- Training an NER component optimized for accuracy
## Combining multiple NER components in the same pipeline
- Creating a package for the trained pipeline
- Creating a pipeline with different NER components

# 9: Creating End-to-End spaCy Workflows with Weasel
## Cloning and running a project template with Weasel
## Modifying a project template for a different use case
- Uploading and downloading project outputs to remote storage
## Managing models with the DVC model registry
- What is GitOps?
- How DVC addresses common data science and ML challenges
- From Weasel to DVC

# 10: Training an Entity Linker Model with spaCy
## Understanding the entity linking task
## Best practices for creating a good NLP corpus
## Training an EntityLinker component with spaCy
## Training with a custom corpus reader
- Testing the entity linking model

# 11: Integrating spaCy with Third-Party Libraries
## Building spaCy-powered Apps with Streamlit
- Building NLP apps with spacy-streamlit
## Building APIs for NLP models using FastAPI
- Python type hinting 101
- Creating an API for the spaCy model with FastAPI

# See Also
* **Linguistic Fundamentals for Natural Language Processing** by Emily Bender
* **Attention Is All You Need** by Vaswani et al
* BERT(Bidirectional Encoder Representations Transformers): Google 2018 - https://arxiv.org/pdf/1810.04805.pdf
* RoBERTa - https://arxiv.org/abs/1907.11692
* GitOps - https://opengitops.dev/
* Hash Embeddings for Efficient Word Representations - https://arxiv.org/pdf/1709.03933

tools
- spaCy
- displaCy: official part of the core library - https://spacy.io/usage/visualizers
- pandas
- wget
- spacy-llm, spacy-transformers, spacy-huggingface-pipelines
- annotate data
  - Prodigy
  - nertk - https://github.com/johnsmithm/nertk
- srsly: jsonl format
- [Weasel](https://github.com/explosion/weasel): A small and easy workflow system
- [DVC(Data Version Control)](https://github.com/treeverse/dvc): Data Versioning and ML Experiments.  DVC is your "Git for data"!
  - [Introducing DVC Studio](https://dvc.org/blog/introducing-dvc-studio/)
- cloudpathlib
- Streamlit: spacy-streamlit
- FastAPI

datasets
- ATIS(Airline Travel Information System): for intent classification - https://www.kaggle.com/datasets/hassanamin/atis-airlinetravelinformationsystem
- Amazon Fine Food Reviews dataset - https://www.kaggle.com/snap/amazon-fine-food-reviews
