# Python Data Science Handbook, 2nd Edition

- I. Jupyter: Beyond Normal Python: 1-3
- II. Introduction to NumPy: 4-12
- III. Data Manipulation with Pandas: 13-24
- IV. Visualization with Matplotlib: 25-36
- V. Machine Learning: 37-50

# 1. Getting Started in IPython and Jupyter/IPython 和 Jupyter 入门
- Launching the IPython Shell
- Launching the Jupyter Notebook
- Help and Documentation in IPython
  - Accessing Documentation with `?`
  - Accessing Source Code with `??`
  - Exploring Modules with Tab Completion
- Keyboard Shortcuts in the IPython Shell
  - Navigation Shortcuts
  - Text Entry Shortcuts
  - Command History Shortcuts
  - Miscellaneous Shortcuts

# 2. Enhanced Interactive Features/增强的交互功能
- IPython Magic Commands
  - Running External Code: `%run`
  - Timing Code Execution: `%timeit`
  - Help on Magic Functions: `?`, `%magic`, and `%lsmagic`
- Input and Output History
  - IPython’s In and Out Objects
  - Underscore Shortcuts and Previous Outputs
  - Suppressing Output
  - Related Magic Commands
- IPython and Shell Commands
  - Quick Introduction to the Shell
  - Shell Commands in IPython
  - Passing Values to and from the Shell
  - Shell-Related Magic Commands

# 3. Debugging and Profiling/调试与性能分析
- Errors and Debugging
  - Controlling Exceptions: `%xmode`
    - `Plain, Context, Verbose`
  - Debugging: When Reading Tracebacks Is Not Enough
    - `ipdb`, `%debug`
    - `%pdb on`
- Profiling and Timing Code
    - Timing Code Snippets: `%timeit` and `%time`
  - Profiling Full Scripts: `%prun`
  - Line-by-Line Profiling with `%lprun`: `%load_ext line_profiler`
  - Profiling Memory Use: `%memit` and `%mprun`: ` %load_ext memory_profiler`
- More IPython Resources
  - Web Resources
  - Books

# > 4. Understanding Data Types in Python/理解 Python 中的数据类型
- A Python Integer Is More Than Just an Integer
- A Python List Is More Than Just a List
- Fixed-Type Arrays in Python: `array`
- Creating Arrays from Python Lists: `np.array`
- Creating Arrays from Scratch
```python
np.zeros
np.ones
np.full
np.arange
np.random.random
np.random.normal
np.random.randint
np.eye
np.empty
```
- NumPy Standard Data Types

# 5. The Basics of NumPy Arrays/NumPy 数组基础
- NumPy Array Attributes/数组属性
- Array Indexing: Accessing Single Elements/数组索引
- Array Slicing: Accessing Subarrays/数组切片 `x[start:stop:step]`
  - One-Dimensional Subarrays
  - Multidimensional Subarrays
  - Subarrays as No-Copy Views
  - Creating Copies of Arrays: `copy()`
- Reshaping of Arrays/调整数组形状: `reshape()`
- Array Concatenation and Splitting/数组拼接和拆分
  - Concatenation of Arrays
  - Splitting of Arrays

# 6. Computation on NumPy Arrays: Universal Functions/NumPy 数组计算：通用函数
- The Slowness of Loops
- Introducing Ufuncs
- Exploring NumPy’s Ufuncs
  - Array Arithmetic
  - Absolute Value
  - Trigonometric Functions
  - Exponents and Logarithms
  - Specialized Ufuncs
- Advanced Ufunc Features
  - Specifying Output
  - Aggregations
  - Outer Products
- Ufuncs: Learning More

```python
# arithmetic operators
+   np.add
-   np.subtract
-   np.negative
*   np.multiply
/   np.divide
//  np.floor_divide
**  np.power
%   np.mod

# absolute value
np.absolute
np.abs

# trigonometric functions
np.sin  np.arcsin
np.cos  np.arccos
np.tan  np.arctan

# exponents and logarithms
np.exp    
np.exp2
np.power
np.log
np.log2
np.log10 
np.expm1 # np.expm1(x) = np.exp(x) - 1
np.log1p # np.log1p(x) = log(1 + x)
```


# 7. Aggregations: min, max, and Everything in Between/聚合操作：最小值、最大值及其他
- Summing the Values in an Array
- Minimum and Maximum
  - Multidimensional Aggregates
  - Other Aggregation Functions
- Example: What Is the Average Height of US Presidents?

```python
np.sum        np.nansum         # Compute sum of elements
np.prod       np.nanprod        # Compute product of elements
np.mean       np.nanmean        # Compute mean of elements
np.std        np.nanstd         # Compute standard deviation
np.var        np.nanvar         # Compute variance
np.min        np.nanmin         # Find minimum value
np.max        np.nanmax         # Find maximum value
np.argmin     np.nanargmin      # Find index of minimum value
np.argmax     np.nanargmax      # Find index of maximum value
np.median     np.nanmedian      # Compute median of elements
np.percentile np.nanpercentile  # Compute rank-based statistics of elements
np.any        N/A               # Evaluate whether any elements are true
np.all        N/A               # Evaluate whether all elements are true
```

# 8. Computation on Arrays: Broadcasting/数组计算：广播
- Introducing Broadcasting
- Rules of Broadcasting
  - Broadcasting Example 1
  - Broadcasting Example 2
  - Broadcasting Example 3
- Broadcasting in Practice
  - Centering an Array
  - Plotting a Two-Dimensional Function

Rules of Broadcasting
- Rule 1: If the two arrays differ in their number of **dimensions**, the shape of the one with fewer dimensions is *padded with ones on its leading (left) side*.
- Rule 2: If the **shape** of the two arrays does not match in any dimension, the array with shape equal to 1 in that dimension is stretched to match the other shape.
- Rule 3: If in any dimension the sizes disagree and neither is equal to 1, an error is raised.

# 9. Comparisons, Masks, and Boolean Logic/比较、掩码与布尔逻辑
- Example: Counting Rainy Days
- Comparison Operators as Ufuncs
- Working with Boolean Arrays
  - Counting Entries
  - Boolean Operators
- Boolean Arrays as Masks
- Using the Keywords and/or Versus the Operators `&/|`

```python
==  np.equal 
!=  np.not_equal
<   np.less 
<=  np.less_equal
>   np.greater 
>=  np.greater_equal

&   np.bitwise_and
|   np.bitwise_or
^   np.bitwise_xor
~   np.bitwise_not
```

# 10. Fancy Indexing/花式索引
- Exploring Fancy Indexing
- Combined Indexing
- Example: Selecting Random Points
- Modifying Values with Fancy Indexing
- Example: Binning Data

# 11. Sorting Arrays/数组排序
- Fast Sorting in NumPy: np.sort and np.argsort
- Sorting Along Rows or Columns
- Partial Sorts: Partitioning
- Example: k-Nearest Neighbors

# 12. Structured Data: NumPy’s Structured Arrays/结构化数据：NumPy 结构化数组
- Exploring Structured Array Creation
- More Advanced Compound Types
- Record Arrays: Structured Arrays with a Twist
- On to Pandas

# > 13. Introducing Pandas Objects/Pandas 对象简介
- The Pandas Series Object
  - Series as Generalized NumPy Array
  - Series as Specialized Dictionary
  - Constructing Series Objects
- The Pandas DataFrame Object
  - DataFrame as Generalized NumPy Array
  - DataFrame as Specialized Dictionary
  - Constructing DataFrame Objects
- The Pandas Index Object
  - Index as Immutable Array
  - Index as Ordered Set

# 14. Data Indexing and Selection/数据索引与选择
- Data Selection in Series
  - Series as Dictionary
  - Series as One-Dimensional Array
  - Indexers: `loc` and `iloc`
- Data Selection in DataFrames
  - DataFrame as Dictionary
  - DataFrame as Two-Dimensional Array
  - Additional Indexing Conventions

# 15. Operating on Data in Pandas/Pandas 数据操作
- Ufuncs: Index Preservation
- Ufuncs: Index Alignment
  - Index Alignment in Series
  - Index Alignment in DataFrames
- Ufuncs: Operations Between DataFrames and Series

# 16. Handling Missing Data/处理缺失数据
- Trade-offs in Missing Data Conventions
- Missing Data in Pandas
  - None as a Sentinel Value
  - NaN: Missing Numerical Data
  - NaN and None in Pandas
- Pandas Nullable Dtypes
- Operating on Null Values
  - Detecting Null Values
  - Dropping Null Values
  - Filling Null Values

# 17. Hierarchical Indexing/层级索引
- A Multiply Indexed Series
  - The Bad Way
  - The Better Way: The Pandas MultiIndex
  - MultiIndex as Extra Dimension
- Methods of MultiIndex Creation
  - Explicit MultiIndex Constructors
  - MultiIndex Level Names
  - MultiIndex for Columns
- Indexing and Slicing a MultiIndex
  - Multiply Indexed Series
  - Multiply Indexed DataFrames
- Rearranging Multi-Indexes
  - Sorted and Unsorted Indices
  - Stacking and Unstacking Indices
  - Index Setting and Resetting

# 18. Combining Datasets: concat and append/合并数据集：concat 与 append
- Recall: Concatenation of NumPy Arrays
- Simple Concatenation with `pd.concat`
  - Duplicate Indices
  - Concatenation with Joins
  - The `append` Method

# 19. Combining Datasets: merge and join/合并数据集：merge 与 join
- Relational Algebra
- Categories of Joins
  - One-to-One Joins
  - Many-to-One Joins
  - Many-to-Many Joins
- Specification of the Merge Key
  - The `on` Keyword
  - The `left_on` and `right_on` Keywords
  - The `left_index` and `right_index` Keywords
- Specifying Set Arithmetic for Joins
- Overlapping Column Names: The `suffixes` Keyword
- Example: US States Data

# 20. Aggregation and Grouping/聚合与分组
- Planets Data
- Simple Aggregation in Pandas
- `groupby`: Split, Apply, Combine
  - Split, Apply, Combine
  - The GroupBy Object
  - Aggregate, Filter, Transform, Apply
  - Specifying the Split Key
  - Grouping Example

# 21. Pivot Tables/透视表
- Motivating Pivot Tables
- Pivot Tables by Hand
- Pivot Table Syntax
  - Multilevel Pivot Tables
  - Additional Pivot Table Options
- Example: Birthrate Data

# 22. Vectorized String Operations/向量化字符串操作
- Introducing Pandas String Operations
- Tables of Pandas String Methods
  - Methods Similar to Python String Methods
  - Methods Using Regular Expressions
  - Miscellaneous Methods
- Example: Recipe Database
  - A Simple Recipe Recommender
  - Going Further with Recipes

# 23. Working with Time Series/处理时间序列
- Dates and Times in Python
  - Native Python Dates and Times: `datetime` and `dateutil`
  - Typed Arrays of Times: NumPy’s `datetime64`
  - Dates and Times in Pandas: The Best of Both Worlds
- Pandas Time Series: Indexing by Time
- Pandas Time Series Data Structures
- Regular Sequences: pd.date_range
- Frequencies and Offsets
- Resampling, Shifting, and Windowing
  - Resampling and Converting Frequencies
  - Time Shifts
  - Rolling Windows
- Example: Visualizing Seattle Bicycle Counts
  - Visualizing the Data
  - Digging into the Data

# 24. High-Performance Pandas: eval and query/高性能 Pandas：eval 与 query
- Motivating query and eval: Compound Expressions
- pandas.eval for Efficient Operations
- DataFrame.eval for Column-Wise Operations
  - Assignment in `DataFrame.eval`
  - Local Variables in `DataFrame.eval`
- The DataFrame.query Method
- Performance: When to Use These Functions
- Further Resources

# > 25. General Matplotlib Tips/Matplotlib 通用技巧
- Importing Matplotlib
- Setting Styles
- show or No show? How to Display Your Plots
  - Plotting from a Script
  - Plotting from an IPython Shell
  - Plotting from a Jupyter Notebook
  - Saving Figures to File
  - Two Interfaces for the Price of One

# 26. Simple Line Plots/简单折线图
- Adjusting the Plot: Line Colors and Styles
- Adjusting the Plot: Axes Limits
- Labeling Plots
- Matplotlib Gotchas

# 27. Simple Scatter Plots/简单散点图
- Scatter Plots with plt.plot
- Scatter Plots with plt.scatter
- plot Versus scatter: A Note on Efficiency
- Visualizing Uncertainties
  - Basic Errorbars
  - Continuous Errors

# 28. Density and Contour Plots/密度图与等高线图
- Visualizing a Three-Dimensional Function
- Histograms, Binnings, and Density
- Two-Dimensional Histograms and Binnings
  - `plt.hist2d`: Two-Dimensional Histogram
  - `plt.hexbin`: Hexagonal Binnings
  - Kernel Density Estimation

# 29. Customizing Plot Legends/自定义图例
- Choosing Elements for the Legend
- Legend for Size of Points
- Multiple Legends

# 30. Customizing Colorbars/自定义颜色条
- Customizing Colorbars
  - Choosing the Colormap
  - Color Limits and Extensions
  - Discrete Colorbars
- Example: Handwritten Digits

# 31. Multiple Subplots/多子图
- `plt.axes`: Subplots by Hand
- `plt.subplot`: Simple Grids of Subplots
- `plt.subplots`: The Whole Grid in One Go
- `plt.GridSpec`: More Complicated Arrangements

# 32. Text and Annotation/文本与注释
- Example: Effect of Holidays on US Births
- Transforms and Text Position
- Arrows and Annotation

# 33. Customizing Ticks/自定义刻度
- Major and Minor Ticks
- Hiding Ticks or Labels
- Reducing or Increasing the Number of Ticks
- Fancy Tick Formats
- Summary of Formatters and Locators

# 34. Customizing Matplotlib: Configurations and Stylesheets/自定义 Matplotlib：配置与样式表
- Plot Customization by Hand
- Changing the Defaults: rcParams
- Stylesheets
  - Default Style
  - FiveThiryEight Style
  - ggplot Style
  - Bayesian Methods for Hackers Style
  - Dark Background Style
  - Grayscale Style
  - Seaborn Style

# 35. Three-Dimensional Plotting in Matplotlib/Matplotlib 三维绘图
- Three-Dimensional Points and Lines
- Three-Dimensional Contour Plots
- Wireframes and Surface Plots
- Surface Triangulations
- Example: Visualizing a Möbius Strip

# 36. Visualization with Seaborn/使用 Seaborn 进行可视化
- Exploring Seaborn Plots
  - Histograms, KDE, and Densities
  - Pair Plots
  - Faceted Histograms
- Categorical Plots
  - Joint Distributions
  - Bar Plots
- Example: Exploring Marathon Finishing Times
- Further Resources
- Other Python Visualization Libraries

# > 37. What Is Machine Learning?/什么是机器学习?
- Categories of Machine Learning
- Qualitative Examples of Machine Learning Applications
  - Classification: Predicting Discrete Labels
  - Regression: Predicting Continuous Labels
  - Clustering: Inferring Labels on Unlabeled Data
  - Dimensionality Reduction: Inferring Structure of Unlabeled Data

# 38. Introducing Scikit-Learn/Scikit-Learn 简介
- Data Representation in Scikit-Learn
  - The Features Matrix
  - The Target Array
- The Estimator API
  - Basics of the API
  - Supervised Learning Example: Simple Linear Regression
  - Supervised Learning Example: Iris Classification
  - Unsupervised Learning Example: Iris Dimensionality
  - Unsupervised Learning Example: Iris Clustering
- Application: Exploring Handwritten Digits
  - Loading and Visualizing the Digits Data
  - Unsupervised Learning Example: Dimensionality Reduction
  - Classification on Digits

# 39. Hyperparameters and Model Validation/超参数与模型验证
- Thinking About Model Validation
  - Model Validation the Wrong Way
  - Model Validation the Right Way: Holdout Sets
  - Model Validation via Cross-Validation
- Selecting the Best Model
  - The Bias-Variance Trade-off
  - Validation Curves in Scikit-Learn
- Learning Curves
- Validation in Practice: Grid Search

# 40. Feature Engineering/特征工程
- Categorical Features
- Text Features
- Image Features
- Derived Features
- Imputation of Missing Data
- Feature Pipelines

# 41. In Depth: Naive Bayes Classification/深入解析：朴素贝叶斯分类
- Bayesian Classification
- Gaussian Naive Bayes
- Multinomial Naive Bayes
  - Example: Classifying Text
- When to Use Naive Bayes

# 42. In Depth: Linear Regression/深入解析：线性回归
- Simple Linear Regression
- Basis Function Regression
  - Polynomial Basis Functions
  - Gaussian Basis Functions
- Regularization
  - Ridge Regression (L2 Regularization)
  - Lasso Regression (L1 Regularization)
- Example: Predicting Bicycle Traffic

# 43. In Depth: Support Vector Machines/深入解析：支持向量机
- Motivating Support Vector Machines
- Support Vector Machines: Maximizing the Margin
  - Fitting a Support Vector Machine
  - Beyond Linear Boundaries: Kernel SVM
  - Tuning the SVM: Softening Margins
- Example: Face Recognition

# 44. In Depth: Decision Trees and Random Forests/深入解析：决策树与随机森林
- Motivating Random Forests: Decision Trees
  - Creating a Decision Tree
  - Decision Trees and Overfitting
- Ensembles of Estimators: Random Forests
- Random Forest Regression
- Example: Random Forest for Classifying Digits

# 45. In Depth: Principal Component Analysis/深入解析：主成分分析
- Introducing Principal Component Analysis
  - PCA as Dimensionality Reduction
  - PCA for Visualization: Handwritten Digits
  - What Do the Components Mean?
  - Choosing the Number of Components
- PCA as Noise Filtering
- Example: Eigenfaces

# 46. In Depth: Manifold Learning/深入解析：流形学习
- Manifold Learning: “HELLO”
- Multidimensional Scaling
  - MDS as Manifold Learning
  - Nonlinear Embeddings: Where MDS Fails
- Nonlinear Manifolds: Locally Linear Embedding
- Some Thoughts on Manifold Methods
- Example: Isomap on Faces
- Example: Visualizing Structure in Digits

# 47. In Depth: k-Means Clustering/深入解析：k-Means 聚类
- Introducing k-Means
- Expectation–Maximization
- Examples
  - Example 1: k-Means on Digits
  - Example 2: k-Means for Color Compression

# 48. In Depth: Gaussian Mixture Models/深入解析：高斯混合模型
- Motivating Gaussian Mixtures: Weaknesses of k-Means
- Generalizing E–M: Gaussian Mixture Models
- Choosing the Covariance Type
- Gaussian Mixture Models as Density Estimation
- Example: GMMs for Generating New Data

# 49. In Depth: Kernel Density Estimation/深入解析：核密度估计
- Motivating Kernel Density Estimation: Histograms
- Kernel Density Estimation in Practice
- Selecting the Bandwidth via Cross-Validation
- Example: Not-so-Naive Bayes
  - Anatomy of a Custom Estimator
  - Using Our Custom Estimator

# 50. Application: A Face Detection Pipeline/应用：人脸检测流水线
- HOG Features
- HOG in Action: A Simple Face Detector
  - 1. Obtain a Set of Positive Training Samples
  - 2. Obtain a Set of Negative Training Samples
  - 3. Combine Sets and Extract HOG Features
  - 4. Train a Support Vector Machine
  - 5. Find Faces in a New Image
- Caveats and Improvements
- Further Machine Learning Resources

# See Also

tools
- NumPy 1.21.2

datasets
- https://github.com/altair-viz/vega_datasets -> https://github.com/vega/altair