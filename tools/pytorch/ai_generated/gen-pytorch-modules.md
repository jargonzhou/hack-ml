list PyTorch modules

PyTorch 的核心功能高度模块化，全部收录在 torch 命名空间下。以下是 PyTorch 最核心、最常用的顶层模块（Modules）分类清单：
## 1. 核心与张量模块 (Core & Tensors)

* torch: 核心库。包含张量（Tensor）的操作、多维数组数学运算（加减乘除、矩阵乘法等）。
* torch.Tensor: 张量对象本身。包含张量的各种就地（in-place）和非就地操作方法（如 .view(), .cuda(), .backward()）。

## 2. 神经网络与自动求导 (Neural Networks & Autograd)

* torch.nn: 神经网络的核心模块。包含所有基础网络层（如 nn.Linear, nn.Conv2d, nn.LSTM）、损失函数（如 nn.CrossEntropyLoss）以及容器（如 nn.Sequential）。
* torch.nn.functional: 包含 torch.nn 中所有层的函数式版本（通常简写为 F）。它不维护状态（没有权重参数），直接传入输入和权重，常用于激活函数（如 F.relu）和池化操作。
* torch.optim: 优化器模块。实现各种主流的梯度下降算法，如 optim.SGD, optim.Adam, optim.AdamW，以及学习率调度器（Learning Rate Schedulers）。
* torch.autograd: 自动求导引擎。负责实现前述的“基于磁带的”动态梯度计算，包含 torch.autograd.backward 和用于控制梯度追踪的上下文管理器（如 torch.no_grad()）。

## 3. 数据处理与输入 (Data Handling)

* torch.utils.data: 数据加载与预处理核心。
* Dataset: 抽象类，用于封装你自己的数据集。
   * DataLoader: 数据加载器，负责实现小批量（mini-batch）数据的自动并行加载、打乱（shuffle）和多线程处理。

## 4. 硬件加速与分布式 (Hardware & Distributed)

* torch.cuda: CUDA 硬件加速模块。用于管理英伟达 GPU（如检查可用性 is_available()、清空缓存、指定当前设备）。
* torch.mps: 苹果芯片（Apple Silicon M1/M2/M3 等）的 GPU 加速模块。
* torch.distributed: 分布式训练模块。支持多 GPU、多节点的并行训练（如 DDP - DistributedDataParallel）。

## 5. 模型序列化与部署 (Serialization & Production)

* torch.jit: Just-In-Time 编译器（即 TorchScript）。将动态的 PyTorch 代码转换为静态图，脱离 Python 环境运行，用于 C++ 生产环境的高性能部署。
* torch.export: 新一代模型导出架构。可以将模型平稳导出为图结构，用于各种端侧或硬件厂商的编译器（如 ExecuTorch）。

## 6. 领域专有官方扩展库 (Domain Ecosystem)
这些库是 PyTorch 官方独立维护的扩展包，针对特定领域进行了高度优化：

* torchvision: 计算机视觉库。包含常用的图像数据集（如 ImageNet）、经典模型架构（如 ResNet, ViT）和图像变换操作（Transforms）。
* torchaudio: 音频和语音处理库。包含音频文件的加载、I/O 操作以及常用的音频特征提取（如梅尔倒谱 STFT/MelSpectrogram）。
* torchtext: 文本与自然语言处理库（注：部分旧功能已在近年逐步迁移或精简）。

------------------------------
您目前是在编写具体的模型架构、数据加载代码，还是在准备模型部署？我可以针对您正在使用的具体模块提供代码示例。
