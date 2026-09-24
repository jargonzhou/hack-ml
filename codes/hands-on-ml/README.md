# Hands-On Machine Learning
* [Géron, Aurélien. **Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow: Concepts, Tools, and Techniques to Build Intelligent Systems**. 2022, 3. edition. O’Reilly](../../books/infrastructure/book.Hands-On%20Machine%20Learning%20with%20Scikit-Learn,%20Keras,%20and%20TensorFlow.md)
* [Chollet, Francois. **Deep Learning with Python**. 2021, 2. edition. Manning](../../books/infrastructure/book.Deep%20Learning%20with%20Python.md)
* [Ganegedara, Thushan. **TensorFlow in Action**. 2022. Manning](../../books/infrastructure/book.TensorFlow%20in%20Action.md)

# Dependencies

```shell
# uv new hands-on-ml
uv python install 3.12
uv python pin 3.12
uv init

uv add --dev autopep8
uv add --dev pylint
uv add scikit-learn
uv add tensorflow
uv add --dev tensorboard-plugin-profile
uv add --dev tensorflow-datasets
uv add keras
uv add --dev pydot
uv add pandas
uv add --dev pandas-stubs
uv add matplotlib
uv add jupyter
uv add Pillow
uv add seaborn
```


TensorFlow type stubs:
```shell
$ uv add tensorflow=2.18.0
# version is 2.18.0
$ uv add --dev types-tensorflow

# handle: No module named 'tensorflow'
# https://pypi.org/project/tensorflow-intel/
$ uv add tensorflow-intel=2.18.0

# tensorflow/__init__.py
# Import "distutils" could not be resolved from source Pylance reportMissingModuleSource
# If using Python 3.12 or later, distutils is no longer part of the standard library.
$ uv add --dev standard-distutils
```

TensorBoard: 
```shell
$ tensorboard --logdir=./data/tf_logs
# http://localhost:6006
```

# TODO

- can we use Bokeh to interactively visualize the hyperparameter selection effects?
- what does 'Op graph' mean in TensorBoard 'Graphs' panel.