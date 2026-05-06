# spaCy: Industrial-strength NLP
* https://spacy.io/
* https://github.com/explosion/spaCy

spaCy is a library for advanced Natural Language Processing in Python and Cython. It's built on the very latest research, and was designed from day one to be used in real products.

spaCy comes with pretrained pipelines and currently supports tokenization and training for 70+ languages. It features state-of-the-art speed and neural network models for tagging, parsing, named entity recognition, text classification and more, multi-task learning with pretrained transformers like BERT, as well as a production-ready training system and easy model packaging, deployment and workflow management. spaCy is commercial open-source software, released under the MIT license.

License: MIT, Language: Python.

Features
- **Tokenization/f分词**: Segmenting text into words, punctuations marks etc.
- **Part-of-speech (POS) Tagging/词性标注**: Assigning word types to tokens, like verb or noun.
- **Dependency Parsing/依存句法分析**: Assigning syntactic dependency labels, describing the relations between individual tokens, like subject or object.
- **Lemmatization/词形还原**: Assigning the base forms of words. For example, the lemma of “was” is “be”, and the lemma of “rats” is “rat”.
- **Sentence Boundary Detection (SBD)/句子边界检测**: Finding and segmenting individual sentences.
- **Named Entity Recognition (NER)/命名实体识别**: Labelling named “real-world” objects, like persons, companies or locations.
- **Entity Linking (EL)/实体链接**: Disambiguating textual entities to unique identifiers in a knowledge base.
- **Similarity/相似性**: Comparing words, text spans and documents and how similar they are to each other.
- **Text Classification/文本分类**: Assigning categories or labels to a whole document, or parts of a document.
- **Rule-based Matching/基于规则匹配**: Finding sequences of tokens based on their texts and linguistic annotations, similar to regular expressions.
- **Training/训练**: Updating and improving a statistical model’s predictions.
- **Serialization/序列化**: Saving objects to files or byte strings.                                                                     |

Books 
- Applied Natural Language Processing in the Enterprise: Teaching Machines to Read, Write, and Understand. O'Reilly, 2021
- Mastering spaCy. Packt, 2021
- Natural Language Processing Using Python. No Starch Press, 2020
- Introduction to Machine Learning with Python: A Guide for Data Scientists. O'Reilly, 2016
- Natural Language Processing and Computational Linguistics. Packt, 2018
- Practical Machine Learning with Python. Apress, 2017
- Text Analytics with Python. Apress / Springer, 2016

# Guides
- [Linguistic Features](https://spacy.io/usage/linguistic-features)
- [Rule-based Matching](https://spacy.io/usage/rule-based-matching)
- [Processing Pipelines](https://spacy.io/usage/processing-pipelines)
- [Embeddings & Transformers](https://spacy.io/usage/embeddings-transformers)
- [Large Language Models](https://spacy.io/usage/large-language-models)
- [Training Models](https://spacy.io/usage/training)
- [Layers & Model Architectures](https://spacy.io/usage/layers-architectures)
- [spaCy Projects](https://spacy.io/usage/projects)
- [Saving & Loading](https://spacy.io/usage/saving-loading)
- [Memory Management](https://spacy.io/usage/memory-management)
- [Visualizers](https://spacy.io/usage/visualizers)

## Linguistic Features/语言学特征
## Rule-based Matching/基于规则的匹配
## Processing Pipelines/处理流水线
## Embeddings & Transformers/嵌入和Transformer
## Large Language Models/大预言模型
## Training Models/训练模型
## Layers & Model Architectures/层和模型架构
## spaCy Projects/spaCy项目
* project template repo: https://github.com/explosion/projects

## Saving & Loading/保存和加载模型
## Memory Management/内存管理
## Visualizers/可视化

# API
* https://spacy.io/api
* glossary: https://github.com/explosion/spaCy/blob/master/spacy/glossary.py

## Library Architecture

![](https://spacy.io/images/architecture.svg)

**Container objects/容器对象**
- `Doc`/文档: A container for accessing linguistic annotations.
- `DocBin`/二进制序列化的文档: A collection of Doc objects for efficient binary serialization. Also used for training data.
- `Example`/示例: A collection of training annotations, containing two `Doc` objects: the reference data and the predictions.
- `Language`/语言: Processing class that turns text into `Doc` objects. Different languages implement their own subclasses of it. The variable is typically called `nlp`.
- `Lexeme`/词素: An entry in the vocabulary. It’s a word type with no context, as opposed to a word token. It therefore has no part-of-speech tag, dependency parse etc.
- `Span`/文档切片: A slice from a `Doc` object.
- `SpanGroup`/切片组: A named collection of spans belonging to a `Doc`.
- `Token`/词项: An individual token — i.e. a word, punctuation symbol, whitespace, etc.

**Processing pipeline/处理流水线**: The processing pipeline consists of one or more **pipeline components** that are called on the `Doc` in order. The tokenizer runs before the components. Pipeline components can be added using [`Language.add_pipe`](https://spacy.io/api/language#add_pipe). They can contain a statistical model and trained weights, or only make rule-based modifications to the `Doc`. spaCy provides a range of built-in components for different language processing tasks and also allows adding [custom components](https://spacy.io/usage/processing-pipelines#custom-components).
- `AttributeRuler`/词项属性规则: Set token attributes using matcher rules.
- `CoreferenceResolver`: Pipeline component for word-level coreference resolution.
- `CuratedTransformer`: Pipeline component for multi-task learning with Curated Transformer models.
- `DependencyParser`/依存句法解析器: Predict syntactic dependencies.
- `EditTreeLemmatizer`/词素树: Predict base forms of words.
- `EntityLinker`/实体消歧: Disambiguate named entities to nodes in a knowledge base.
- `EntityRecognizer`/实体识别: Predict named entities, e.g. persons or products.
- `EntityRuler`/实体规则: Add entity spans to the `Doc` using token-based rules or exact phrase matches.
- Large Language Models: `spacy-llm` package. featuring a modular system for fast prototyping and prompting, and turning unstructured responses into robust outputs for various NLP tasks, no training data required.
- `Lemmatizer`/词性还原器: Determine the base forms of words using rules and lookups.
- `Morphologizer`/形态学生成器: Predict morphological features and coarse-grained part-of-speech tags.
- `SentenceRecognizer`/句子识别器: Predict sentence boundaries.
- `Sentencizer`/基于规则的句子识别: Implement rule-based sentence boundary detection that doesn’t require the dependency parse.
- `SpanCategorizer`: Pipeline component for labeling potentially overlapping spans of text.
- `SpanFinder`: Pipeline component for identifying potentially overlapping spans of text.
- `SpanResolver`: Pipeline component for resolving tokens into spans.
- `SpanRuler`: Pipeline component for rule-based span and named entity recognition.
- `Tagger`/词性标注器: Predict part-of-speech tags.
- `TextCategorizer`/文本分类器: Predict categories or labels over the whole document.
- `Tok2Vec`/词项到向量转换: Apply a “token-to-vector” model and set its outputs.
- `Tokenizer`/分词器: Segment raw text and create `Doc` objects from the words.
- `TrainablePipe`/可训练的管道: Class that all trainable pipeline components inherit from.
- `Transformer`: Use a transformer model and set its outputs.
- Other functions:	Automatically apply something to the `Doc`, e.g. to merge spans of tokens.
  - `merge_noun_chunks`: Merge noun chunks into a single token.
  - `merge_entities`: Merge named entities into a single token.
  - `merge_subtokens`: Merge subtokens into a single token.
  - `token_splitter`: Split tokens longer than a minimum length into shorter tokens. Intended for use with transformer pipelines where long spaCy tokens lead to input text that exceed the transformer model max length.
  - `doc_cleaner`: Clean up `Doc` attributes. Intended for use at the end of pipelines with `tok2vec` or `transformer` pipeline components that store tensors and other values that can require a lot of memory and frequently aren’t needed after the whole pipeline has run.

**Matchers/匹配器**: Matchers help you find and extract information from `Doc` objects based on match patterns describing the sequences you’re looking for. A matcher operates on a `Doc` and gives you access to the matched tokens **in context**.
- `DependencyMatcher`/基于依存树的词项序列匹配器: Match sequences of tokens based on dependency trees using [Semgrex operators](https://nlp.stanford.edu/nlp/javadoc/javanlp/edu/stanford/nlp/semgraph/semgrex/SemgrexPattern.html).
- `Matcher`/基于模式规则的词项序列匹配器: Match sequences of tokens, based on pattern rules, similar to regular expressions.
- `PhraseMatcher`/短语匹配器: Match sequences of tokens based on phrases.

**Other classes/其他类**
- Attributes: Token attributes.
- `BaseVectors`: Abstract class for word vectors.
- `Corpus`/语料库: Class for managing annotated corpora for training and evaluation data.
- `KnowledgeBase`/知识库: Abstract base class for storage and retrieval of data for entity linking.
- `InMemoryLookupKB`/内存知识库: Implementation of `KnowledgeBase` storing all data in memory.
- `Candidate`/知识库实体关联对象: Object associating a textual mention with a specific entity contained in a `KnowledgeBase`.
- `Lookups`/查找容器: Container for convenient access to large lookup tables and dictionaries.
- `MorphAnalysis`/形态学分析: A morphological analysis.
- `Morphology`/形态学: Store morphological analyses and map them to and from hash values.
- `Scorer`/计算评估分数: Compute evaluation scores.
- `StringStore`/字符串存储: Map strings to and from hash values.
- `Vectors`/向量存储: Container class for vector data keyed by string.
- `Vocab`/词素词汇: The shared vocabulary that stores strings and gives you access to `Lexeme` objects.

## Model Architectures
## Data Formats
## Command Line Interface

```shell
$ python -m spacy --help
Usage: python -m spacy [OPTIONS] COMMAND [ARGS]...

  spaCy Command-line Interface

  DOCS: https://spacy.io/api/cli

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or
                        customize the installation.
  --help                Show this message and exit.

Commands:
  download        Download compatible trained pipeline from the default...
  apply           Apply a trained pipeline to documents to get predictions.
  assemble        Assemble a spaCy pipeline from a config file.
  convert         Convert files into json or DocBin format for training.
  evaluate        Evaluate a trained pipeline.
  find-function   Find the module, path and line number to the file the...
  find-threshold  Runs prediction trials for a trained model with varying...
  info            Print info about spaCy installation.
  package         Generate an installable Python package for a pipeline.
  pretrain        Pre-train the 'token-to-vector' (tok2vec) layer of...
  train           Train or update a spaCy pipeline.
  validate        Validate the currently installed pipeline packages and...
  project         Command-line interface for spaCy projects and templates.
  debug           Suite of helpful commands for debugging and profiling.
  benchmark       Commands for benchmarking pipelines.
  init            Commands for initializing configs and pipeline packages.
```

## Top-level Functions


# Trained Models & Pipelines

model info
```
example: en_core_web_sm
[lang]_[Type]_[Genre]_[Size]
Type: core, dep
Genre: web, news
Size: small sm, medium md, large lg, transformer trf
```
- Accuracy Evaluation
- Label Scheme


CNN/CPU pipeline design: `sm`/`md`/`lg`
- tok2vec, tagger, parser, senter, attribute_ruler, lemmatizer, ner

Transformer pipeline design: `trf`
- transformer, tagger, parser, attribute_ruler, lemmatizer, ner

# Universe
* https://github.com/explosion/spaCy/blob/master/website/UNIVERSE.md
* https://github.com/explosion/spaCy/blob/master/website/meta/universe.json

great resources developed with or for spaCy, includes standalone packages, plugins, extensions, educational materials, operational utilities and bindings for other languages.

- `TeNs`: Temporal Expressions Normalization spaCy. **[Temporal Expressions Normalization spaCy (TeNs)](https://github.com/iliedorobat/timespan-normalization-spacy)** is a powerful pipeline component for spaCy that seamlessly identifies and parses date entities in text. It leverages the **[Temporal Expressions Normalization Framework]( https://github.com/iliedorobat/timespan-normalization)** to recognize a wide variety of date formats using an extensive set of regular expressions (RegEx), ensuring robust and adaptable date extraction across diverse textual sources. Unlike conventional solutions that primarily focus on well-structured date formats, TeNs excels in handling real-world text by **identifying** not only standard date representations but also **abbreviated, informal, or even misspelled temporal expressions.** This makes it particularly effective for processing noisy or unstructured data, such as historical records, user-generated content, and scanned documents with OCR inaccuracies.
- `spacy-vscode`: spaCy Visual Studio Code Extension. The spaCy VS Code Extension provides additional tooling and features for working with spaCy's config files. Version 1.0.0 includes hover descriptions for registry functions, variables, and section names within the config as an installable extension.
- `constituent_treelib`: Constituent Treelib. Constituent Treelib (CTL) is a lightweight Python library built on top of benepar (Berkeley Neural Parser) as well as the two well-known NLP frameworks spaCy and NLTK. CTL offers you a convenient way to parse sentences into constituent trees, modify them according to their structure, as well as visualize and export them into various file formats. In addition, you can extract phrases according to their phrasal categories (which can be used e.g., as features for various NLP tasks), validate already parsed sentences in bracket notation or convert them back into sentences.
- `sayswho`: SaysWho. A Python package for identifying and attributing quotes in text. It uses a combination of spaCy functionality, logic and grammar to find quotes and their speakers, then uses the spaCy coreferencing model to better clarify who is speaking. Currently English only.
- `parsigs`: parsigs. Parsigs is an open-source project that aims to extract the relevant dosage information from prescriptions text without compromising the patient's privacy. Notice you also need to install the model in order to use the package: `pip install https://huggingface.co/royashcenazi/en_parsigs/resolve/main/en_parsigs-any-py3-none-any.whl`
- `latincy`: LatinCy. Set of trained general purpose Latin-language 'core' pipelines for use with spaCy. The models are trained on a large amount of available Latin data, including all five of the Latin Universal Dependency treebanks, which have been preprocessed to be compatible with each other.
- `odycy`: OdyCy. Academically validated modular NLP pipelines for premodern Greek. odyCy achieves state of the art performance on multiple tasks on unseen test data from the Universal Dependencies Perseus treebank, and performs second best on the PROIEL treebank’s test set on even more tasks. In addition performance also seems relatively stable across the two evaluation datasets in comparison with other NLP pipelines. OdyCy is being used at the Center for Humanities Computing for preprocessing and analyzing Ancient Greek corpora for New Testament research, meaning that you can expect consistent maintenance and improvements.
- `spacy-wasm`: spacy-wasm. Run spaCy directly in the browser with WebAssembly. Using Pyodide, the application loads the spaCy model and renders the text prompt with displaCy.
- `spacysee`: spaCysee. A project that helps you visualize your spaCy docs in Jupyter notebooks. Each of the dependency tags, POS tags and morphological features are clickable. Clicking on a tag will bring up the relevant documentation for that tag.
- `grecy`: greCy. greCy offers state-of-the-art pipelines for ancient Greek NLP. It installs language models available in various sizes, some of them containing either word vectors or the aristoBERTo transformer.
- `solipcysme`: solipCysme. __solipCysme__ is a pipeline for french language, designed for the analysis of fictions and first person point of view texts, with a focus on personal pronouns.
- `spacy-cleaner`: spacy-cleaner. **spacy-cleaner** utilises spaCy `Language` models to replace, remove, and  mutate spaCy tokens. Cleaning actions available are: Remove/replace stopwords. Remove/replace punctuation. Remove/replace numbers. Remove/replace emails. Remove/replace URLs. Perform lemmatisation. See our [docs](https://ce11an.github.io/spacy-cleaner/) for more information.
- `Zshot`: Zshot. 
- `concepcy`: concepCy. A spaCy wrapper for ConceptNet, a freely-available semantic network designed to help computers understand the meaning of words.
- `spacyfishing`: spaCy fishing. A spaCy wrapper of Entity-Fishing for named entity disambiguation and linking against a Wikidata knowledge base.
- `aim-spacy`: Aim-spaCy. Aim-spaCy helps to easily collect, store and explore training logs for spaCy, including: hyper-parameters, metrics and displaCy visualizations
- `spacy-report`: spacy-report. The goal of spacy-report is to offer static reports for spaCy models that help users make better decisions on how the models can be used.
- `scrubadub_spacy`: scrubadub_spacy. scrubadub removes personally identifiable information from text. scrubadub_spacy is an extension that uses spaCy NLP models to remove personal information from text.
- `spacy-setfit-textcat`: spacy-setfit-textcat. This project is an experiment with spaCy and few-shot text classification using SetFit
- `spacy-experimental`: spacy-experimental. This package includes experimental components and features for spaCy v3.x, for example model architectures, pipeline components and utilities.
- `spacypdfreader`: spacypdfreader. *spacypdfreader* is a Python library that allows you to convert PDF files directly into *spaCy* `Doc` objects. The library provides several built in parsers or bring your own parser. `Doc` objects are annotated with several custom attributes including: `token._.page_number`, `doc._.page_range`, `doc._.first_page`, `doc._.last_page`, `doc._.pdf_file_name`, and `doc._.page(int)`.
- `nlpcloud`: NLPCloud.io. A highly-available hosted API to easily deploy and use spaCy models in production. Supports NER, POS tagging, dependency parsing, and tokenization.
- `eMFDscore`: eMFDscore : Extended Moral Foundation Dictionary Scoring for Python. eMFDscore is a library for the fast and flexible extraction of various moral information metrics from textual input data. eMFDscore is built on spaCy for faster execution and performs minimal preprocessing consisting of tokenization, syntactic dependency parsing, lower-casing, and stopword/punctuation/whitespace removal. eMFDscore lets users score documents with multiple Moral Foundations Dictionaries, provides various metrics for analyzing moral information, and extracts moral patient, agent, and attribute words related to entities.
- `skweak`: skweak. `skweak` brings the power of weak supervision to NLP tasks, and in particular sequence labelling and text classification. Instead of annotating documents by hand, `skweak` allows you to define *labelling functions* to automatically label your documents, and then aggregate their results using a statistical model that estimates the accuracy and confusions of each labelling function.
- `numerizer`: numerizer. A SpaCy extension for Docs, Spans and Tokens that converts numerical words and quantitative named entities into numeric strings.
- `spacy-dbpedia-spotlight`: DBpedia Spotlight for SpaCy. This library links SpaCy with [DBpedia Spotlight](https://www.dbpedia-spotlight.org/). You can easily get the DBpedia entities from your documents, using the public web service or by using your own instance of DBpedia Spotlight. The `doc.ents` are populated with the entities and all their details (URI, type,...).
- `spacy-textblob`: spacytextblob. spacytextblob is a pipeline component that enables sentiment analysis using the [TextBlob](https://github.com/sloria/TextBlob) library. It will add the additional extension `._.blob` to `Doc`, `Span`, and `Token` objects.
- `spacy-sentence-bert`: spaCy - sentence-transformers. This library lets you use the embeddings from [sentence-transformers](https://github.com/UKPLab/sentence-transformers) of Docs, Spans and Tokens directly from spaCy. Most models are for the english language but three of them are multilingual.
- `spacy-streamlit`: spacy-streamlit. This package contains utilities for visualizing spaCy models and building interactive spaCy-powered apps with [Streamlit](https://streamlit.io). It includes various building blocks you can use in your own Streamlit app, like visualizers for **syntactic dependencies**, **named entities**, **text classification**, **semantic similarity** via word vectors, token attributes, and more.
- `spaczz`: spaczz. Spaczz provides fuzzy matching and multi-token regex matching functionality for spaCy. Spaczz's components have similar APIs to their spaCy counterparts and spaczz pipeline components can integrate into spaCy pipelines where they can be saved/loaded as models.
- `spacy-universal-sentence-encoder`: spaCy - Universal Sentence Encoder. This library lets you use Universal Sentence Encoder embeddings of Docs, Spans and Tokens directly from TensorFlow Hub
- `whatlies`: whatlies. This small library offers tools to make visualisation easier of both word embeddings as well as operations on them. It has support for spaCy prebuilt models as a first class citizen but also offers support for sense2vec. There's a convenient API to perform linear algebra as well as support for popular transformations like PCA/UMAP/etc.
- `bertopic`: BERTopic. BERTopic is a topic modeling technique that leverages embedding models and c-TF-IDF to create dense clusters allowing for easily interpretable topics whilst keeping important words in the topic descriptions. BERTopic supports guided, (semi-) supervised, hierarchical, and dynamic topic modeling.
- `tokenwiser`: tokenwiser. 
- `Klayers`: Klayers. A collection of Python Packages as AWS Lambda(λ) Layers
- `video-spacys-ner-model-alt`: Named Entity Recognition (NER) using spaCy. In this video, I show you how to do named entity recognition using the spaCy library for Python.
- `HuSpaCy`: HuSpaCy. HuSpaCy is a spaCy model and a library providing industrial-strength Hungarian language processing facilities.
- `spacy-stanza`: spacy-stanza. This package wraps the Stanza (formerly StanfordNLP) library, so you can use Stanford's models as a spaCy pipeline. Using this wrapper, you'll be able to use the following annotations, computed by your pretrained `stanza` model: - Statistical tokenization (reflected in the `Doc` and its tokens)  - Lemmatization (`token.lemma` and `token.lemma_`) - Part-of-speech tagging (`token.tag`, `token.tag_`, `token.pos`, `token.pos_`) - Dependency parsing (`token.dep`, `token.dep_`, `token.head`) - Named entity recognition (`doc.ents`, `token.ent_type`, `token.ent_type_`, `token.ent_iob`, `token.ent_iob_`)  - Sentence segmentation (`doc.sents`)
- `spacy-udpipe`: spacy-udpipe. This package wraps the fast and efficient UDPipe language-agnostic NLP pipeline (via its Python bindings), so you can use UDPipe pre-trained models as a spaCy pipeline for 50+ languages out-of-the-box. Inspired by spacy-stanza, this package offers slightly less accurate models that are in turn much faster.
- `spacy-server`: spaCy Server. For developers who need programming language agnostic NLP, spaCy Server is a containerized HTTP API that provides industrial-strength natural language processing. Unlike other servers, our server is fast, idiomatic, and well documented.
- `nlp-architect`: NLP Architect. 
- `Chatterbot`: ChatterBot. 
- `alibi`: alibi. 
- `spacymoji`:  spaCy extension and pipeline component for adding emoji meta data to `Doc` objects. Detects emoji consisting of one or more unicode characters, and can optionally merge multi-char emoji (combined pictures, emoji with skin tone modifiers) into one token. Human-readable emoji descriptions are added as a custom attribute, and an optional lookup table can be provided for your own descriptions. The extension sets the custom `Doc`, `Token` and `Span` attributes `._.is_emoji`, `._.emoji_desc`, `._.has_emoji` and `._.emoji`.
- `spacy-layout`:  This plugin integrates with [Docling](https://ds4sd.github.io/docling/) to bring structured processing of PDFs, Word documents and other input formats to your spaCy pipeline. It outputs clean, structured data in a text-based format and outputs spaCy's familiar `Doc` objects that let you access labelled text spans like sections, headings, or footnotes. This workflow makes it easy to apply powerful NLP techniques to your documents, including linguistic analysis, named entity recognition, text classification and more. It's also great for implementing chunking for RAG pipelines.
- `spacyopentapioca`: spaCyOpenTapioca. A spaCy wrapper of OpenTapioca for named entity linking on Wikidata
- `spacy_readability`:  spaCy v2.0 pipeline component for calculating readability scores of of text. Provides scores for Flesh-Kincaid grade level, Flesh-Kincaid reading ease, and Dale-Chall.
- `spacy_cld`: spaCy-CLD. spaCy-CLD operates on `Doc` and `Span` spaCy objects. When called on a `Doc` or `Span`, the object is given two attributes: `languages` (a list of up to 3 language codes) and `language_scores` (a dictionary mapping language codes to confidence scores between 0 and 1). spacy-cld is a little extension that wraps the [PYCLD2](https://github.com/aboSamoor/pycld2) Python library, which in turn wraps the [Compact Language Detector 2](https://github.com/CLD2Owners/cld2) C library originally built at Google for the Chromium project. CLD2 uses character n-grams as features and a Naive Bayes classifier to identify 80+ languages from Unicode text strings (or XML/HTML). It can detect up to 3 different languages in a given document, and reports a confidence score (reported in with each language.
- `spacy-iwnlp`:  This package uses the [spaCy 2.0 extensions](https://spacy.io/usage/processing-pipelines#extensions) to add [IWNLP-py](https://github.com/Liebeck/iwnlp-py) as German lemmatizer directly into your spaCy pipeline.
- `spacy-sentiws`:  This package uses the [spaCy 2.0 extensions](https://spacy.io/usage/processing-pipelines#extensions) to add [SentiWS](http://wortschatz.uni-leipzig.de/en/download) as German sentiment score directly into your spaCy pipeline.
- `spacy-lefff`:  spacy v2.0 extension and pipeline component for adding a French POS and lemmatizer based on [Lefff](https://hal.inria.fr/inria-00521242/).
- `lemmy`: Lemmy. Lemmy is a lemmatizer for Danish 🇩🇰. It comes already trained on Dansk Sprognævns (DSN) word list (‘fuldformliste’) and the Danish Universal Dependencies and is ready for use. Lemmy also supports training on your own dataset. The model currently included in Lemmy was evaluated on the Danish Universal Dependencies dev dataset and scored an accruacy > 99%. You can use Lemmy as a spaCy extension, more specifcally a spaCy pipeline component. This is highly recommended and makes the lemmas easily accessible from the spaCy tokens. Lemmy makes use of POS tags to predict the lemmas. When wired up to the spaCy pipeline, Lemmy has the benefit of using spaCy’s builtin POS tagger.
- `augmenty`: Augmenty. Augmenty is an augmentation library based on spaCy for augmenting texts. Augmenty differs from other augmentation libraries in that it corrects (as far as possible) the token, sentence and document labels under the augmentation.
- `dacy`: DaCy. DaCy is a Danish preprocessing pipeline trained in SpaCy. It has achieved State-of-the-Art performance on Named entity recognition, part-of-speech tagging and dependency parsing for Danish. This repository contains material for using the DaCy, reproducing the results and guides on usage of the package. Furthermore, it also contains a series of behavioural test for biases and robustness of Danish NLP pipelines.
- `spacy-wrap`: spaCy-wrap. spaCy-wrap is a wrapper library for spaCy for including fine-tuned transformers from Huggingface in your spaCy pipeline allowing inclusion of existing models within existing workflows.
- `asent`: Asent. Asent is a rule-based sentiment analysis library for Python made using spaCy. It is inspired by VADER, but uses a more modular ruleset, that allows the user to change e.g. the method for finding negations. Furthermore it includes visualisers to visualize the model predictions, making the model easily interpretable.
- `textdescriptives`: TextDescriptives. Pipeline component for spaCy v.3 that calculates descriptive statistics, readability metrics, and syntactic complexity (dependency distance).
- `neuralcoref`:  This coreference resolution module is based on the super fast [spaCy](https://spacy.io/) parser and uses the neural net scoring model described in [Deep Reinforcement Learning for Mention-Ranking Coreference Models](http://cs.stanford.edu/people/kevclark/resources/clark-manning-emnlp2016-deep.pdf) by Kevin Clark and Christopher D. Manning, EMNLP 2016. Since ✨Neuralcoref v2.0, you can train the coreference resolution system on your own dataset — e.g., another language than English! — **provided you have an annotated dataset**. Note that to use neuralcoref with spaCy > 2.1.0, you'll have to install neuralcoref from source.
- `neuralcoref-vizualizer`: Neuralcoref Visualizer. In short, coreference is the fact that two or more expressions in a text – like pronouns or nouns – link to the same person or thing. It is a classical Natural language processing task, that has seen a revival of interest in the past two years as several research groups applied cutting-edge deep-learning and reinforcement-learning techniques to it. It is also one of the key building blocks to building conversational Artificial intelligences.
- `matcher-explorer`: Rule-based Matcher Explorer. Test spaCy's rule-based `Matcher` by creating token patterns interactively and running them over your text. Each token can set multiple attributes like text value, part-of-speech tag or boolean flags. The token-based view lets you explore how spaCy processes your text – and why your pattern matches, or why it doesn't. For more details on rule-based matching, see the [documentation](https://spacy.io/usage/rule-based-matching).
- `displacy`: displaCy. Visualize spaCy's guess at the syntactic structure of a sentence. Arrows point from children to heads, and are labelled by their relation type.
- `displacy-ent`: displaCy ENT. Visualize spaCy's guess at the named entities in the document. You can filter the displayed types, to only show the annotations you're interested in.
- `explacy`:  
- `deplacy`:  Simple dependency visualizer for [spaCy](https://spacy.io/), [UniDic2UD](https://pypi.org/project/unidic2ud), [Stanza](https://stanfordnlp.github.io/stanza/), [NLP-Cube](https://github.com/Adobe/NLP-Cube), [Trankit](https://github.com/nlp-uoregon/trankit), etc.
- `scattertext`:  A tool for finding distinguishing terms in small-to-medium-sized corpora, and presenting them in a sexy, interactive scatter plot with non-overlapping term labels. Exploratory data analysis just got more fun.
- `rasa`: Rasa. Machine learning tools for developers to build, improve, and deploy contextual chatbots and assistants. Powered by open source.
- `mindmeld`: MindMeld - Conversational AI platform. The MindMeld Conversational AI platform is among the most advanced AI platforms for building production-quality conversational applications. It is a Python-based machine learning framework which encompasses all of the algorithms and utilities required for this purpose. (https://github.com/cisco/mindmeld)
- `torchtext`: torchtext. 
- `allennlp`: AllenNLP. AllenNLP is a new library designed to accelerate NLP research, by providing a framework that supports modern deep learning workflows for cutting-edge language understanding problems. AllenNLP uses spaCy as a preprocessing component. You can also use Allen NLP to develop spaCy pipeline components, to add annotations to the `Doc` object.
- `scispacy`: scispaCy. 
- `textacy`:  `textacy` is a Python library for performing a variety of natural language processing (NLP) tasks, built on the high-performance `spacy` library. With the fundamentals – tokenization, part-of-speech tagging, dependency parsing, etc. – delegated to another library, `textacy` focuses on the tasks that come before and follow after.
- `textpipe`:  `textpipe` is a Python package for converting raw text in to clean, readable text and extracting metadata from that text. Its functionalities include transforming raw text into readable text by removing HTML tags and extracting metadata such as the number of words and named entities from the text.
- `mordecai`:  Extract the place names from a piece of text, resolve them to the correct place, and return their coordinates and structured geographic information.
- `kindred`: Kindred. Kindred is a package for relation extraction in biomedical texts. Given some training data, it can build a model to identify relations between entities (e.g. drugs, genes, etc) in a sentence.
- `sense2vec`:  sense2vec ([Trask et. al](https://arxiv.org/abs/1511.06388), 2015) is a nice twist on [word2vec](https://en.wikipedia.org/wiki/Word2vec) that lets you learn more interesting, detailed and context-sensitive word vectors. For an interactive example of the technology, see our [sense2vec demo](https://explosion.ai/demos/sense2vec) that lets you explore semantic similarities across all Reddit comments of 2015.
- `spacyr`:  
- `cleannlp`: CleanNLP. The cleanNLP package is designed to make it as painless as possible to turn raw text into feature-rich data frames. the package offers four backends that can be used for parsing text: `tokenizers`, `udpipe`, `spacy` and `corenlp`.
- `spacy-cpp`:  The goal of spacy-cpp is to expose the functionality of spaCy to C++ applications, and to provide an API that is similar to that of spaCy, enabling rapid development in Python and simple porting to C++.
- `ruby-spacy`: ruby-spacy. ruby-spacy is a wrapper module for using spaCy from the Ruby programming language via PyCall. This module aims to make it easy and natural for Ruby programmers to use spaCy.
- `spacy_api`:  
- `spacy-api-docker`:  
- `spacy-nlp`:  
- `prodigy`: Prodigy. Prodigy is an annotation tool so efficient that data scientists can do the annotation themselves, enabling a new level of rapid iteration. Whether you're working on entity recognition, intent detection or image classification, Prodigy can help you train and evaluate your models faster. Stream in your own examples or real-world data from live APIs, update your model in real-time and chain models together to build more complex systems.
- `dragonfire`: Dragonfire. 
- `prefect`: Prefect. 
- `graphbrain`: Graphbrain. Graphbrain is an Artificial Intelligence open-source software library and scientific research tool. Its aim is to facilitate automated meaning extraction and text understanding, as well as the exploration and inference of knowledge.
- `nostarch-nlp-python`: Natural Language Processing Using Python. Natural Language Processing Using Python is an introduction to natural language processing (NLP), the task of converting human language into data that a computer can process. The book uses spaCy, a leading Python library for NLP, to guide readers through common NLP tasks related to generating and understanding human language with code. It addresses problems like understanding a user's intent, continuing a conversation with a human, and maintaining the state of a conversation.
- `oreilly-python-ds`: Introduction to Machine Learning with Python: A Guide for Data Scientists. Machine learning has become an integral part of many commercial applications and research projects, but this field is not exclusive to large companies with extensive research teams. If you use Python, even as a beginner, this book will teach you practical ways to build your own machine learning solutions. With all the data available today, machine learning applications are limited only by your imagination.
- `text-analytics-python`: Text Analytics with Python. *Text Analytics with Python* teaches you the techniques related to natural language processing and text analytics, and you will gain the skills to know which technique is best suited to solve a particular problem. You will look at each technique and algorithm with both a bird's eye view to understand how it can be used as well as with a microscopic view to understand the mathematical concepts and to implement them to solve your own problems.
- `practical-ml-python`: Practical Machine Learning with Python. Master the essential skills needed to recognize and solve complex problems with machine learning and deep learning. Using real-world examples that leverage the popular Python machine learning ecosystem, this book is your perfect companion for learning the art and science of machine learning to become a successful practitioner. The concepts, techniques, tools, frameworks, and methodologies used in this book will teach you how to think, design, build, and execute machine learning systems and projects successfully.
- `packt-nlp-computational-linguistics`: Natural Language Processing and Computational Linguistics. This book shows you how to use natural language processing, and computational linguistics algorithms, to make inferences and gain insights about data you have. These algorithms are based on statistical machine learning and artificial intelligence techniques. The tools to work with these algorithms are available to you right now - with Python, and tools like Gensim and spaCy.
- `mastering-spacy`: Mastering spaCy. This is your ultimate spaCy book. Master the crucial skills to use spaCy components effectively to create real-world NLP applications with spaCy. Explaining linguistic concepts such as dependency parsing, POS-tagging and named entity extraction with many examples, this book will help you to conquer computational linguistics with spaCy. The book further focuses on ML topics with Keras and Tensorflow. You'll cover popular topics, including intent recognition, sentiment analysis and context resolution; and use them on popular datasets and interpret the results. A special hands-on section on chatbot design is included.
- `applied-nlp-in-enterprise`: Applied Natural Language Processing in the Enterprise: Teaching Machines to Read, Write, and Understand. Natural language processing (NLP) is one of the hottest topics in AI today. Having lagged behind other deep learning fields such as computer vision for years, NLP only recently gained mainstream popularity. Even though Google, Facebook, and OpenAI have open sourced large pretrained language models to make NLP easier, many organizations today still struggle with developing and productionizing NLP applications. This hands-on guide helps you learn the field quickly.
- `introduction-into-spacy-3`: Introduction to spaCy 3. 
- `spacy-course`: Advanced NLP with spaCy. In this free interactive course, you'll learn how to use spaCy to build advanced natural language understanding systems, using both rule-based and machine learning approaches.
- `applt-course`: Applied Language Technology. These learning materials provide an introduction to applied language technology for audiences who are unfamiliar with language technology and programming. The learning materials assume no previous knowledge of the Python programming language.
- `video-spacys-ner-model`: spaCy's NER model. spaCy v2.0's Named Entity Recognition system features a sophisticated word embedding strategy using subword features and "Bloom" embeddings, a deep convolutional neural network with residual connections, and a novel transition-based approach to named entity parsing. The system is designed to give a good balance of efficiency, accuracy and adaptability. In this talk, I sketch out the components of the system, explaining the intuition behind the various choices. I also give a brief introduction to the named entity recognition problem, with an overview of what else Explosion AI is working on, and why.
- `video-new-nlp-solutions`: Building new NLP solutions with spaCy and Prodigy. In this talk, I will discuss how to address some of the most likely causes of failure for new Natural Language Processing (NLP) projects. My main recommendation is to take an iterative approach: don't assume you know what your pipeline should look like, let alone your annotation schemes or model architectures.
- `video-modern-nlp-in-python`: Modern NLP in Python. Academic and industry research in Natural Language Processing (NLP) has progressed at an accelerating pace over the last several years. Members of the Python community have been hard at work moving cutting-edge research out of papers and into open source, "batteries included" software libraries that can be applied to practical problems. We'll explore some of these tools for modern NLP in Python.
- `video-spacy-course`: Advanced NLP with spaCy · A free online course. spaCy is a modern Python library for industrial-strength Natural Language Processing. In this free and interactive online course, you'll learn how to use spaCy to build advanced natural language understanding systems, using both rule-based and machine learning approaches.
- `video-spacy-course-de`: Modernes NLP mit spaCy · Ein Gratis-Onlinekurs. spaCy ist eine moderne Python-Bibliothek für industriestarkes Natural Language Processing. In diesem kostenlosen und interaktiven Onlinekurs lernst du, mithilfe von spaCy fortgeschrittene Systeme für die Analyse natürlicher Sprache zu entwickeln und dabei sowohl regelbasierte Verfahren, als auch moderne Machine-Learning-Technologie einzusetzen.
- `video-spacy-course-es`: NLP avanzado con spaCy · Un curso en línea gratis. spaCy es un paquete moderno de Python para hacer Procesamiento de Lenguaje Natural de potencia industrial. En este curso en línea, interactivo y gratuito, aprenderás a usar spaCy para construir sistemas avanzados de comprensión de lenguaje natural usando enfoques basados en reglas y en machine learning.
- `video-intro-to-nlp-episode-1`: Intro to NLP with spaCy (1). In this new video series, data science instructor Vincent Warmerdam gets started with spaCy, an open-source library for Natural Language Processing in Python. His mission: building a system to automatically detect programming languages in large volumes of text. Follow his process from the first idea to a prototype all the way to data collection and training a statistical named entity recogntion model from scratch.
- `video-intro-to-nlp-episode-2`: Intro to NLP with spaCy (2). In this new video series, data science instructor Vincent Warmerdam gets started with spaCy, an open-source library for Natural Language Processing in Python. His mission: building a system to automatically detect programming languages in large volumes of text. Follow his process from the first idea to a prototype all the way to data collection and training a statistical named entity recogntion model from scratch.
- `video-intro-to-nlp-episode-3`: Intro to NLP with spaCy (3). In this new video series, data science instructor Vincent Warmerdam gets started with spaCy, an open-source library for Natural Language Processing in Python. His mission: building a system to automatically detect programming languages in large volumes of text. Follow his process from the first idea to a prototype all the way to data collection and training a statistical named entity recogntion model from scratch.
- `video-intro-to-nlp-episode-4`: Intro to NLP with spaCy (4). In this new video series, data science instructor Vincent Warmerdam gets started with spaCy, an open-source library for Natural Language Processing in Python. His mission: building a system to automatically detect programming languages in large volumes of text. Follow his process from the first idea to a prototype all the way to data collection and training a statistical named entity recogntion model from scratch.
- `video-intro-to-nlp-episode-5`: Intro to NLP with spaCy (5). In this new video series, data science instructor Vincent Warmerdam gets started with spaCy, an open-source library for Natural Language Processing in Python. His mission: building a system to automatically detect programming languages in large volumes of text. Follow his process from the first idea to a prototype all the way to data collection and training a statistical named entity recogntion model from scratch.
- `video-intro-to-nlp-episode-6`: Intro to NLP with spaCy (6). In this new video series, data science instructor Vincent Warmerdam gets started with spaCy, an open-source library for Natural Language Processing in Python. His mission: building a system to automatically detect programming languages in large volumes of text. Follow his process from the first idea to a prototype all the way to data collection and training a statistical named entity recogntion model from scratch.
- `video-spacy-irl-entity-linking`: Entity Linking functionality in spaCy. 
- `video-spacy-irl-lemmatization`: Rethinking rule-based lemmatization. 
- `video-spacy-irl-scispacy`: ScispaCy: A spaCy pipeline & models for scientific & biomedical text. 
- `podcast-nlp-highlights`: NLP Highlights #78: Where do corpora come from?. Most NLP projects rely crucially on the quality of annotations used for training and evaluating models. In this episode, Matt and Ines of Explosion AI tell us how Prodigy can improve data annotation and model development workflows. Prodigy is an annotation tool implemented as a python library, and it comes with a web application and a command line interface. A developer can define input data streams and design simple annotation interfaces. Prodigy can help break down complex annotation decisions into a series of binary decisions, and it provides easy integration with spaCy models. Developers can specify how models should be modified as new annotations come in in an active learning framework.
- `podcast-init`: Podcast.__init__ #87: spaCy with Matthew Honnibal. As the amount of text available on the internet and in businesses continues to increase, the need for fast and accurate language analysis becomes more prominent. This week Matthew Honnibal, the creator of spaCy, talks about his experiences researching natural language processing and creating a library to make his findings accessible to industry.
- `podcast-init2`: Podcast.__init__ #256: An Open Source Toolchain For NLP From Explosion AI. The state of the art in natural language processing is a constantly moving target. With the rise of deep learning, previously cutting edge techniques have given way to robust language models. Through it all the team at Explosion AI have built a strong presence with the trifecta of spaCy, Thinc, and Prodigy to support fast and flexible data labeling to feed deep learning models and performant and scalable text processing. In this episode founder and open source author Matthew Honnibal shares his experience growing a business around cutting edge open source libraries for the machine learning developent process.
- `talk-python-podcast`: Talk Python #202: Building a software business. One core question around open source is how do you fund it? Well, there is always that PayPal donate button. But that's been a tremendous failure for many projects. Often the go-to answer is consulting. But what if you don't want to trade time for money? You could take things up a notch and change the equation, exchanging value for money. That's what Ines Montani and her co-founder did when they started Explosion AI with spaCy as the foundation.
- `twimlai-podcast`: TWiML & AI: Practical NLP with spaCy and Prodigy. "Ines and I caught up to discuss her various projects, including the aforementioned spaCy, an open-source NLP library built with a focus on industry and production use cases. In our conversation, Ines gives us an overview of the spaCy Library, a look at some of the use cases that excite her, and the Spacy community and contributors. We also discuss her work with Prodigy, an annotation service tool that uses continuous active learning to train models, and finally, what other exciting projects she is working on."
- `analytics-vidhya`: DataHack Radio #23: The Brains behind spaCy. "What would you do if you had the chance to pick the brains behind one of the most popular Natural Language Processing (NLP) libraries of our era? A library that has helped usher in the current boom in NLP applications and nurtured tons of NLP scientists? Well – you invite the creators on our popular DataHack Radio podcast and let them do the talking! We are delighted to welcome Ines Montani and Matt Honnibal, the developers of spaCy – a powerful and advanced library for NLP."
- `practical-ai-podcast`: Practical AI: Modern NLP with spaCy. "spaCy is awesome for NLP! It’s easy to use, has widespread adoption, is open source, and integrates the latest language models. Ines Montani and Matthew Honnibal (core developers of spaCy and co-founders of Explosion) join us to discuss the history of the project, its capabilities, and the latest trends in NLP. We also dig into the practicalities of taking NLP workflows to production. You don’t want to miss this episode!"
- `video-entity-linking`: Training a custom entity linking mode with spaCy. 
- `self-attentive-parser`: Berkeley Neural Parser. A Python implementation of the parsers described in *"Constituency Parsing with a Self-Attentive Encoder"* from ACL 2018.
- `spacy-graphql`: spacy-graphql. A very simple and experimental app that lets you query spaCy's linguistic annotations using [GraphQL](https://graphql.org/). The API currently supports most token attributes, named entities, sentences and text categories (if available as `doc.cats`, i.e. if you added a text classifier to a model). The `meta` field will return the model meta data. Models are only loaded once and kept in memory.
- `spacy-js`: spacy-js. JavaScript interface for accessing linguistic annotations provided by spaCy. This project is mostly experimental and was developed for fun to play around with different ways of mimicking spaCy's Python API. The results will still be computed in Python and made available via a REST API. The JavaScript API resembles spaCy's Python API as closely as possible (with a few exceptions, as the values are all pre-computed and it's tricky to express complex recursive relationships).
- `spacy-wordnet`: spacy-wordnet. `spacy-wordnet` creates annotations that easily allow the use of WordNet and [WordNet Domains](http://wndomains.fbk.eu/) by using the [NLTK WordNet interface](http://www.nltk.org/howto/wordnet.html)
- `spacy-conll`: spacy_conll. This module allows you to parse text into CoNLL-U format or read ConLL-U into a spaCy `Doc`. You can use it as a command line tool, or embed it in your own scripts by adding it as a custom pipeline component to a `spacy`, `spacy-stanza` or `spacy-udpipe` pipeline. It also provides an easy-to-use function to quickly initialize any spaCy-wrapped parser. CoNLL-related properties are added to `Doc` elements, `Span` sentences, and `Token` objects.
- `ludwig`: Ludwig. Ludwig makes it easy to build deep learning models for many applications, including NLP ones. It uses spaCy for tokenizing text in different languages.
- `pic2phrase_bot`: pic2phrase_bot: Photo Description Generator. pic2phrase_bot runs inside Telegram messenger and can be used to generate a phrase describing a submitted photo, employing computer vision, web scraping, and syntactic dependency analysis powered by spaCy.
- `pyInflect`:  This package uses the [spaCy 2.0 extensions](https://spacy.io/usage/processing-pipelines#extensions) to add word inflections to the system.
- `lemminflect`:  LemmInflect uses a dictionary approach to lemmatize English words and inflect them into forms specified by a user supplied [Universal Dependencies](https://universaldependencies.org/u/pos/) or [Penn Treebank](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html) tag.  The library works with out-of-vocabulary (OOV) words by applying neural network techniques to classify word forms and choose the appropriate morphing rules. The system acts as a standalone module or as an extension to spaCy.
- `amrlib`:  amrlib is a python module and spaCy add-in for Abstract Meaning Representation (AMR).  The system can parse sentences to AMR graphs or generate text from existing graphs.  It includes a GUI for visualization and experimentation.
- `classyclassification`: Classy Classification. Have you ever struggled with needing a [spaCy TextCategorizer](https://spacy.io/api/textcategorizer) but didn't have the time to train one from scratch? Classy Classification is the way to go! For few-shot classification using [sentence-transformers](https://github.com/UKPLab/sentence-transformers) or [spaCy models](https://spacy.io/usage/models), provide a dictionary with labels and examples, or just provide a list of labels for zero shot-classification with [Huggingface zero-shot classifiers](https://huggingface.co/models?pipeline_tag=zero-shot-classification).
- `conciseconcepts`: Concise Concepts. When wanting to apply NER to concise concepts, it is really easy to come up with examples, but it takes some effort to train an entire pipeline. Concise Concepts uses few-shot NER based on word embedding similarity to get you going with easy!
- `crosslingualcoreference`: Crosslingual Coreference. Coreference is amazing but the data required for training a model is very scarce. In our case, the available training for non-English languages also data proved to be poorly annotated. Crosslingual Coreference therefore uses the assumption a trained model with English data and cross-lingual embeddings should work for other languages with similar sentence structure. Verified to work quite well for at least (EN, NL, DK, FR, DE).
- `adeptaugmentations`: Adept Augmentations. EntitySwapAugmenter takes either a `datasets.Dataset` or a `spacy.tokens.DocBin`. Additionally, it is optional to provide a set of labels. It initially creates a knowledge base of entities belonging to a certain label. When running `augmenter.augment()` for N runs, it then creates N new sentences with random swaps of the original entities with an entity of the same corresponding label from the knowledge base. For example, assuming that we have knowledge base for `PERSONS`, `LOCATIONS` and `PRODUCTS`. We can then create additional data for the sentence "Momofuko Ando created instant noodles in Osaka." using `augmenter.augment(N=2)`, resulting in "David created instant noodles in Madrid." or "Tom created Adept Augmentations in the Netherlands".
- `spacysetfit`: spaCy-SetFit. spaCy-SetFit is a Python library that extends spaCy's text categorization capabilities by incorporating SetFit for few-shot classification. It allows you to train a text categorizer using a intuitive dictionary. The library integrates with spaCy's pipeline architecture, enabling easy integration and configuration of the text categorizer component. You can provide a training dataset containing inlier and outlier examples, and spaCy-SetFit will use the paraphrase-MiniLM-L3-v2 model for training the text categorizer with SetFit. Once trained, you can use the categorizer to classify new text and obtain category probabilities.
- `blackstone`: Blackstone. Blackstone is a spaCy model and library for processing long-form, unstructured legal text. Blackstone is an experimental research project from the [Incorporated Council of Law Reporting for England and Wales'](https://iclr.co.uk/) research lab, [ICLR&D](https://research.iclr.co.uk/).
- `NGym`: NeuralGym. NeuralGym is a Python application for Windows with a graphical user interface to train models with spaCy. Run the application, select an output folder, a training data file in spaCy's data format, a spaCy model or blank model and press 'Start'.
- `holmes`: Holmes. Holmes is a Python 3 library that supports a number of use cases involving information extraction from English and German texts, including chatbot, structural extraction, topic matching and supervised document classification. There is a [website demonstrating intelligent search based on topic matching](https://holmes-demo.explosion.services).
- `coreferee`: Coreferee. Coreferee is a pipeline plugin that performs coreference resolution for English, French, German and Polish. It is designed so that it is easy to add support for new languages and optimised for limited training data. It uses a mixture of neural networks and programmed rules. Please note you will need to [install models](https://github.com/explosion/coreferee#getting-started) before running the code example.
- `spacy-transformers`: spacy-transformers. This package provides spaCy model pipelines that wrap [Hugging Face's `transformers`](https://github.com/huggingface/transformers) package, so you can use them in spaCy. The result is convenient access to state-of-the-art transformer architectures, such as BERT, GPT-2, XLNet, etc.
- `spacy-huggingface-hub`: spacy-huggingface-hub. This package provides a CLI command for uploading any trained spaCy pipeline packaged with [`spacy package`](https://spacy.io/api/cli#package) to the [Hugging Face Hub](https://huggingface.co). It auto-generates all meta information for you, uploads a pretty README (requires spaCy v3.1+) and handles version control under the hood.
- `spacy-clausie`: spacy-clausie. ClausIE, a novel, clause-based approach to open information extraction, which extracts relations and their arguments from natural language text
- `ipymarkup`:  Collection of NLP visualizations for NER and syntax tree markup. Similar to [displaCy](https://explosion.ai/demos/displacy) and [displaCy ENT](https://explosion.ai/demos/displacy-ent).
- `negspacy`: negspaCy. negspacy is a spaCy pipeline component that evaluates whether Named Entities are negated in text. It adds an extension to 'Span' objects.
- `ronec`: RONEC - Romanian Named Entity Corpus. The corpus holds 5127 sentences, annotated with 16 classes, with a total of 26376 annotated entities. The corpus comes into two formats: BRAT and CONLLUP.
- `Healthsea`: Healthsea. This spaCy project trains an NER model and a custom Text Classification model with Clause Segmentation and Blinding capabilities to analyze supplement reviews and their potential effects on health.
- `presidio`: Presidio. Presidio *(Origin from Latin praesidium ‘protection, garrison’)* helps to ensure sensitive text is properly managed and governed. It provides fast ***analytics*** and ***anonymization*** for sensitive text such as credit card numbers, names, locations, social security numbers, bitcoin wallets, US phone numbers and financial data. Presidio analyzes the text using predefined or custom recognizers to identify entities, patterns, formats, and checksums with relevant context.
- `presidio-research`: Presidio Research. This package features data-science related tasks for developing new recognizers for Microsoft Presidio. It is used for the evaluation of the entire system, as well as for evaluating specific PII recognizers or PII detection models. Anyone interested in evaluating an existing Microsoft Presidio instance, a specific PII recognizer or to develop new models or logic for detecting PII could leverage the preexisting work in this package. Additionally, anyone interested in generating new data based on previous datasets (e.g. to increase the coverage of entity values) for Named Entity Recognition models could leverage the data generator contained in this package.
- `python-sentence-boundary-disambiguation`: pySBD - python Sentence Boundary Disambiguation. pySBD is 'real-world' sentence segmenter which extracts reasonable sentences when the format and domain of the input text are unknown. It is a rules-based algorithm based on [The Golden Rules](https://s3.amazonaws.com/tm-town-nlp-resources/golden_rules.txt) - a set of tests to check accuracy of segmenter in regards to edge case scenarios developed by [TM-Town](https://www.tm-town.com/) dev team. pySBD is python port of ruby gem [Pragmatic Segmenter](https://github.com/diasks2/pragmatic_segmenter).
- `cookiecutter-spacy-fastapi`: cookiecutter-spacy-fastapi. Docker-based cookiecutter for easy spaCy APIs using FastAPI. The default endpoints expect batch requests with a list of Records in the Azure Search Cognitive Skill format. So out of the box, this cookiecutter can be setup as a Custom Cognitive Skill. For more on Azure Search and Cognitive Skills [see this page](https://docs.microsoft.com/en-us/azure/search/cognitive-search-custom-skill-interface).
- `dframcy`: Dframcy. DframCy is a light-weight utility module to integrate Pandas Dataframe to spaCy's linguistic annotation and training tasks.
- `spacy-pytextrank`: PyTextRank. An implementation of TextRank in Python for use in spaCy pipelines which provides fast, effective phrase extraction from texts, along with extractive summarization. The graph algorithm works independent of a specific natural language and does not require domain knowledge. See (Mihalcea 2004) https://web.eecs.umich.edu/~mihalcea/papers/mihalcea.emnlp04.pdf
- `spacy_syllables`: Spacy Syllables. Spacy Syllables is a pipeline component that adds multilingual syllable annotations to Tokens. It uses Pyphen under the hood and has support for a long list of languages.
- `sentimental-onix`: Sentimental Onix. spaCy pipeline component for sentiment analysis using onnx
- `gobbli`: gobbli. gobbli is a Python library which wraps several modern deep learning models in a uniform interface that makes it easy to evaluate feasibility and conduct analyses. It leverages the abstractive powers of Docker to hide nearly all dependency management and functional differences between models from the user. It also contains an interactive app for exploring text data and evaluating classification models. spaCy's base text classification models, as well as models integrated from `spacy-transformers`, are available in the collection of classification models. In addition, spaCy is used for data augmentation and document embeddings.
- `spacy_fastlang`: Spacy FastLang. Fast language detection using FastText and Spacy.
- `mlflow`: MLflow. MLflow is an open source platform to manage the ML lifecycle, including experimentation, reproducibility, deployment, and a central model registry. MLflow currently offers four components: Tracking, Projects, Models and Registry.
- `pyate`: PyATE. PyATE is a term extraction library written in Python using Spacy POS tagging with Basic, Combo Basic, C-Value, TermExtractor, and Weirdness.
- `contextualSpellCheck`: Contextual Spell Check. This package currently focuses on Out of Vocabulary (OOV) word or non-word error (NWE) correction using BERT model. The idea of using BERT was to use the context when correcting NWE.
- `texthero`: Texthero. Texthero is a python package to work with text data efficiently. It empowers NLP developers with a tool to quickly understand any text-based dataset and it provides a solid pipeline to clean and represent text data, from zero to hero.
- `cov-bsv`: VA COVID-19 NLP BSV. A spaCy rule-based pipeline for identifying positive cases of COVID-19 from clinical text. A version of this system was deployed as part of the US Department of Veterans Affairs biosurveillance response to COVID-19.
- `medspacy`: medspaCy. A toolkit for clinical NLP with spaCy. Features include sentence splitting, section detection, and asserting negation, family history, and uncertainty.
- `rita-dsl`: RITA DSL. A Domain Specific Language (DSL) for building language patterns. These can be later compiled into spaCy patterns, pure regex, or any other format
- `PatternOmatic`: PatternOmatic. Discover spaCy's linguistic patterns matching a given set of String samples to be used by the spaCy's Rule Based Matcher
- `SpacyDotNet`: spaCy.NET Wrapper. This projects relies on [Python.NET](http://pythonnet.github.io/) to interop with spaCy. It's not meant to be a complete and exhaustive implementation of all spaCy features and [APIs](https://spacy.io/api). Although it should be enough for basic tasks, it's considered as a starting point if you need to build a complex project using spaCy in.NET Most of the basic features in _Spacy101_ are available. All `Container` classes are present (`Doc`, `Token`, `Span` and `Lexeme`) with their basic properties/methods running and also `Vocab` and `StringStore` in a limited form. Anyway, any developer should be ready to add the missing properties or classes in a very straightforward manner.
- `ruts`: ruTS. The library allows extracting the following statistics from a text: basic statistics, readability metrics, lexical diversity metrics, morphological statistics
- `trunajod`: TRUNAJOD. With all the basic NLP capabilities provided by spaCy (dependency parsing, POS tagging, tokenizing), `TRUNAJOD` focuses on extracting measurements from texts that might be interesting for different applications and use cases.
- `lingfeat`: LingFeat. LingFeat is a feature extraction library which currently extracts 255 linguistic features from English string input. Categories include syntax, semantics, discourse, and also traditional readability formulas. Published in EMNLP 2021.
- `hmrb`: Hammurabi. Hammurabi works as a rule engine to parse input using a defined set of rules. It uses a simple and readable syntax to define complex rules to handle phrase matching. The syntax supports nested logical statements, regular expressions, reusable or side-loaded variables and match triggered callback functions to modularize your rules. The latest version works with both spaCy 2.X and 3.X. For more information check the documentation on [ReadTheDocs](https://hmrb.readthedocs.io/en/latest/).
- `forte`: Forte. Forte provides a platform to assemble state-of-the-art NLP and ML technologies in a highly-composable fashion, including a wide spectrum of tasks ranging from Information Retrieval, Natural Language Understanding to Natural Language Generation.
- `spacy-api-docker-v3`:  
- `phruzz_matcher`: phruzz-matcher. Combination of the RapidFuzz library with Spacy PhraseMatcher The goal of this component is to find matches when there were NO "perfect matches" due to typos or abbreviations between a Spacy doc and a list of phrases.
- `WordDumb`: WordDumb. A calibre plugin that generates Word Wise and X-Ray files then sends them to Kindle. Supports KFX, AZW3 and MOBI eBooks. X-Ray supports 18 languages.
- `eng_spacysentiment`: eng_spacysentiment. Sentiment analysis for simple english sentences using pre-trained spaCy pipelines
- `textnets`:  textnets represents collections of texts as networks of documents and words. This provides novel possibilities for the visualization and analysis of texts.
- `tmtoolkit`:  tmtoolkit is a set of tools for text mining and topic modeling with Python developed especially for the use in the social sciences, in journalism or related disciplines. It aims for easy installation, extensive documentation and a clear programming interface while offering good performance on large datasets by the means of vectorized operations (via NumPy) and parallel computation (using Python’s multiprocessing module and the loky package).
- `edsnlp`: EDS-NLP. EDS-NLP provides a set of rule-based spaCy components to extract information for French clinical notes. It also features _qualifier_ pipelines that detect negations, speculations and family context, among other modalities. Check out the [demo](https://aphp.github.io/edsnlp/demo/)!
- `sent-pattern`: English Interpretation Sentence Pattern. This package categorizes English sentences into one of five basic sentence patterns and identifies the subject, verb, object, and other components. The five basic sentence patterns are based on C. T. Onions's Advanced English Syntax and are frequently used when teaching English in Japan.
- `spacy-partial-tagger`: spaCy - Partial Tagger. This is a library to build a CRF tagger with a partially annotated dataset in spaCy. You can build your own tagger only from dictionary.
- `spacy-pythainlp`: spaCy-PyThaiNLP. This package wraps the PyThaiNLP library to add support for Thai to spaCy.
- `vetiver`: Vetiver. The goal of vetiver is to provide fluent tooling to version, deploy, and monitor a trained model. Functions handle creating model objects, versioning models, predicting from a remote API endpoint, deploying Dockerfiles, and more.
- `span_marker`: SpanMarker. The SpanMarker integration with spaCy allows you to seamlessly replace the default spaCy `"ner"` pipeline component with any [SpanMarker model available on the Hugging Face Hub](https://huggingface.co/models?library=span-marker). Through this, you can take advantage of the advanced Named Entity Recognition capabilities of SpanMarker within the familiar and powerful spaCy framework. By default, the `span_marker` pipeline component uses a [SpanMarker model using RoBERTa-large trained on OntoNotes v5.0](https://huggingface.co/tomaarsen/span-marker-roberta-large-ontonotes5). This model reaches a competitive 91.54 F1, notably higher than the [85.5 and 89.8 F1](https://spacy.io/usage/facts-figures#section-benchmarks) from `en_core_web_lg` and `en_core_web_trf`, respectively. A short head-to-head between this SpanMarker model and the `trf` spaCy model has been posted [here](https://github.com/tomaarsen/SpanMarkerNER/pull/12). Additionally, see [here](https://tomaarsen.github.io/SpanMarkerNER/notebooks/spacy_integration.html) for documentation on using SpanMarker with spaCy.
- `hobbit-spacy`: Hobbit spaCy. Hobbit spaCy is a custom spaCy pipeline designed specifically for working with Middle Earth and texts from the world of J.R.R. Tolkien.
- `rolegal`: A spaCy Package for Romanian Legal Document Processing. This is a spaCy language model for Romanian legal domain trained with floret 4-gram to 5-gram embeddings and `LEGAL` entity recognition. Useful for processing OCR-resulted noisy legal documents.
- `redfield-spacy-nodes`: Redfield NLP Nodes for KNIME. This extension provides nodes that make the functionality of the spaCy library available in the [KNIME Analytics Platform](https://www.knime.com/).
- `quelquhui`: quelquhui. A tokenizer for French that handles inword parentheses like in _(b)rouille_, inclusive language (won't split _relecteur.rice.s_,but will split _mais.maintenant_), hyphens (split _peut-on_, or _pouvons-vous_ but not _tubulu-pimpant_), apostrophes (split _j'arrive_ or _j'arrivons_, but not _aujourd'hui_ or _r'garder_), emoticons, text-emoji (_:happy:_), urls, mails and more.
- `gliner-spacy`: GLiNER spaCy Wrapper. GLiNER SpaCy Wrapper is a project that brings together GLiNER, a zero-shot Named Entity Recognition (NER) model, with spaCy's NLP capabilities. It provides an easy way to integrate GLiNER within the spaCy environment, thus enhancing NER tasks with GLiNER's features.
- `presque`: presque. Normalizer for French with focus on online and informal communication, _peùUUUt-èTRE_ becomes _peut-être_, _voilaaaa_ becomes _voilà_. it also harmonizes inclusive language (the user can chose how): by default, _auteur-rice-s-x et relecteur.xrices_ becomes _auteur·ricexs et relecteur·ricexs_.
- `bagpipes-spacy`: Bagpipes spaCy. Bagpipes spaCy is a versatile collection of custom spaCy pipeline components enhancing text processing capabilities. It includes functionalities such as phrase extraction, text normalization, triple detection, entity and sentence clustering, token clustering, and keyword extraction. These components augment NLP tasks with advanced processing and analysis features, offering a comprehensive toolkit for natural language data handling.
- `number-spacy`: Number spaCy. Number spaCy is a custom spaCy pipeline component that enhances the identification of number entities in text and fetches the parsed numeric values using spaCy's token extensions. It uses RegEx to identify number entities written in words and then leverages the [word2number](https://github.com/akshaynagpal/w2n) library to convert those words into structured numeric data. The output numeric value is stored in a custom entity extension: `._.number`. This lightweight component can be seamlessly added to an existing spaCy pipeline or integrated into a blank model. If using within an existing spaCy pipeline, ensure to insert it before the NER model.
- `spacy-annoy`: Spacy Annoy. Spacy Annoy offers a combination of Spacy's natural language processing (NLP) capabilities and Annoy's efficient similarity search algorithms. This Python class is tailored for analyzing and querying large text corpora, delivering results based on semantic similarity. Key features include contextual window chunking and controlled overlap with preservation of original context at the Doc level, allowing access to all original Spacy properties.
- `spacy-whisper`: spaCy Whisper. spaCy Whisper is a Python package designed for integrating Whisper transcriptions with spaCy's NLP capabilities. It provides users with the ability to process and analyze transcribed text using spaCy's features like tokenization, entity recognition, and part-of-speech tagging. Key features include word and segment level processing with custom attributes, as well as custom token, span, and document extensions, enriching the NLP analysis of transcribed texts.
- `date-spacy`: Date spaCy. Date spaCy is a spaCy pipeline component designed to identify and parse date entities in text effortlessly. It uses Regular Expressions (RegEx) to detect a wide range of date formats and leverages the 'dateparser' library for accurate conversion into structured datetime objects. Particularly useful in NLP tasks involving date information extraction, this component seamlessly integrates into existing or new spaCy pipelines. The tool assumes the current year for dates without a specified year, ensuring sensible defaults while maintaining flexibility. The parsed dates are stored in a custom entity extension, providing easy access and manipulation within spaCy's ecosystem. This makes Date spaCy a go-to solution for developers and data scientists dealing with temporal data in natural language.

# See Also
* [spaCy VSCode Extension](https://github.com/explosion/spacy-vscode): spaCy extension for Visual Studio Code.
* Eight Parts of Speech: http://www.butte.edu/departments/cas/tipsheets/grammar/parts_of_speech.html
* [Thinc](https://github.com/explosion/thinc): Thinc is a lightweight deep learning library that offers an elegant, type-checked, functional-programming API for composing models, with support for layers defined in other frameworks such as PyTorch, TensorFlow and MXNet. You can use Thinc as an interface layer, a standalone toolkit or a flexible way to develop new models.