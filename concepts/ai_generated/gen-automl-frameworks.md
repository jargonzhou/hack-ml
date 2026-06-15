# > list auto machine learning frameworks

Automated Machine Learning (AutoML) frameworks automate the end-to-end process of applying machine learning to real-world problems, covering tasks like data preprocessing, feature engineering, model selection, and hyperparameter tuning. [1] 
The most popular open-source and commercial AutoML frameworks are categorized below by their primary focus: [2] 
## General-Purpose & Tabular Frameworks [3] 

* AutoGluon: Developed by AWS, it excels at tabular, text, and image data using multi-layer model stacking instead of searching for a single best model.
* [Auto-sklearn](https://github.com/automl/auto-sklearn): A drop-in replacement for scikit-learn estimators that uses Bayesian optimization, meta-learning, and automated ensemble construction.
* [PyCaret](https://github.com/pycaret/pycaret): A low-code machine learning library that acts as a wrapper around several frameworks, allowing you to train and compare dozens of models with just a few lines of code.
* [H2O AutoML](https://github.com/h2oai/h2o-3): A highly scalable, enterprise-ready platform that automates data prep, tuning, and training of complex stacked ensembles.
* [TPOT](https://github.com/EpistasisLab/tpot): A "data science assistant" that utilizes genetic programming to optimize entire machine learning pipelines, including feature selection and preprocessing.
* [FLAML](https://github.com/microsoft/FLAML): A lightweight library from Microsoft designed to find accurate models quickly and economically with minimal computational resources.
* [MLJAR](https://github.com/mljar/mljar-supervised): An abstract, feature-dense framework built for tabular data that automatically generates markdown documentation and explanations for every trained model.
* MLBox: A powerful framework split into three clean steps: highly optimized preprocessing, state-of-the-art hyperparameter optimization, and robust prediction. [4, 5, 6, 7, 8, 9, 10, 11, 12] 

## Deep Learning & Neural Architecture Search (NAS)

* [AutoKeras](https://github.com/keras-team/autokeras): Built on top of Keras, it simplifies Neural Architecture Search (NAS) for deep learning tasks involving images, text, and structured data.
* [Microsoft NNI](https://github.com/microsoft/qlib): Neural Network Intelligence automates feature engineering, neural architecture search, hyperparameter tuning, and model compression.
* Ludwig: A declarative deep learning framework that allows users to build and train complete architectures using simple configuration files instead of code.
* Auto-PyTorch: Focuses on automating neural architecture search and hyperparameter tuning specifically for PyTorch architectures. [4, 11, 13] 

## Cloud & Enterprise Ecosystems

* [Google Cloud AutoML](https://cloud.google.com/automl): A fully managed, commercial suite specializing in zero-code model generation for Vision, Natural Language, Translation, and Tables.
* Amazon SageMaker Autopilot: Automatically inspects raw source datasets, applies the best feature combinations, and trains model candidates within AWS.
* Azure Automated Machine Learning: Microsoft's enterprise cloud offering that automatically picks algorithms, handles feature engineering, and tunes hyperparameters. [1, 10, 14, 15, 16] 

If you are trying to pick one for your project, tell me:

* What type of data are you working with? (e.g., Tabular, Images, Text, Time Series)
* Will you deploy this locally or in the cloud?
* Do you prefer a no-code/low-code tool or a pure Python script setup? [4, 9, 16] 

I can recommend the absolute best framework for your specific scenario.

- [1] [https://www.sabrepc.com](https://www.sabrepc.com/blog/Deep-Learning-and-AI/10-github-repositories-for-automl)
- [2] [https://logz.io](https://logz.io/blog/open-source-machine-learning/)
- [3] [https://pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC12886369/)
- [4] [https://github.com](https://github.com/askery/automl-list)
- [5] [https://www.automl.org](https://www.automl.org/automl/)
- [6] [https://medium.com](https://medium.com/analytics-vidhya/6-open-source-automated-machine-learning-tools-every-data-scientist-should-know-49960c1397c9)
- [7] [https://www.kaggle.com](https://www.kaggle.com/general/196539)
- [8] [https://techninjahere.medium.com](https://techninjahere.medium.com/best-opensource-automl-frameworks-4e40820e2d79)
- [9] [https://moez-62905.medium.com](https://moez-62905.medium.com/top-automl-python-libraries-in-2022-2d306cf7acf0)
- [10] [https://www.esparkinfo.com](https://www.esparkinfo.com/blog/top-machine-learning-frameworks)
- [11] [https://github.com](https://github.com/oskar-j/awesome-auto-ml)
- [12] [https://mljar.com](https://mljar.com/blog/python-automl/)
- [13] [https://github.com](https://github.com/hibayesian/awesome-automl-papers)
- [14] [https://www.geeksforgeeks.org](https://www.geeksforgeeks.org/python/top-automl-python-libraries/)
- [15] [https://www.igmguru.com](https://www.igmguru.com/blog/machine-learning-frameworks)
- [16] [https://mljar.com](https://mljar.com/blog/automl-software-list/)

# > especially with PyTorch

If you want to use PyTorch as your primary backend, your options narrow down to frameworks that natively generate, train, and optimize PyTorch models.
The top AutoML frameworks built specifically for or tightly integrated with PyTorch are structured below:
## Dedicated PyTorch AutoML Frameworks

* Auto-PyTorch: Automatically searches for deep learning architectures and tunes hyperparameters specifically for PyTorch models.
* Ludwig: Uses PyTorch under the hood. You define data features in a YAML file, and it automatically builds, trains, and optimizes the PyTorch neural network.
* Ray Tune: A powerful, industry-standard library for distributed hyperparameter tuning that includes first-class, seamless integrations for PyTorch and PyTorch Lightning.

## Multi-Framework Libraries with Strong PyTorch Support

* AutoGluon: Uses PyTorch as the core backend for all text, image, and multi-modal tasks, and relies on it heavily for tabular deep learning models.
* [AutoKeras](https://github.com/keras-team/autokeras): Traditionally TensorFlow-only, it now supports the Keras 3 ecosystem, allowing you to run its automated neural architecture search directly on a PyTorch backend.
* [Microsoft NNI](https://github.com/microsoft/qlib): Features extensive, built-in tools for PyTorch to automate Neural Architecture Search (NAS), hyperparameter tuning, and model pruning/compression.

To help narrow this down, let me know:

* What is your specific machine learning task? (e.g., Image Classification, Text NLP, Tabular data, Time Series)
* Do you need Neural Architecture Search (NAS) to find new network structures, or just Hyperparameter Tuning for an existing PyTorch model?

I can guide you to the exact library that fits your workflow.

