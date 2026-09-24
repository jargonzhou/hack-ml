pytorch version history

PyTorch 自 2016 年 9 月首次发布以来，其版本演进主要经历了三个重大历史时期：从最初的探索阶段，到 1.x 时代的全面普及，再到如今 2.x 时代的编译器级别性能飞跃。 [1] 
以下是 PyTorch 核心版本的发展历史与关键技术演进：
------------------------------
## 一、 2.x 时代（2023年 至今）：编译器革命 [2] 
当前最新的稳定版本是 PyTorch 2.12.0（于 2026 年 5 月发布）。2.x 系列的核心宗旨是在完全保持“动态图（Eager Mode）”开发体验的同时，在底层引入编译器技术进行极致加速。 [1, 3, 4] 

* v2.12 (2026年5月)：大幅优化 CUDA 底层，使批量 linalg.eigh 运算速度提升高达 100 倍；推出 torch.accelerator 统一了不同硬件阵营的图捕获 API。
* v2.11 (2026年3月)：持续优化了大语言模型（LLM）推理常用的 FlexAttention 机制。
* v2.10 (2026年1月) / v2.9 (2025年10月)：强化了分布式训练（FSDP2）在大规模集群上的稳定性。
* v2.0 (2023年3月)：里程碑版本。首次引入了 torch.compile()，通过三大底层支柱（TorchDynamo, AOTAutograd, Inductor）将 Python 代码自动编译为高性能的 GPU 算子，使得模型训练和推理速度获得原生飞跃。 [3, 4, 5, 6, 7, 8, 9] 

## 二、 1.x 时代（2018年 – 2022年）：全面普及与工程化
在 1.x 时代，PyTorch 彻底击败了 TensorFlow 1.x，并逐渐在学术界与工业界占据统治地位。 [10] 

* v1.13 (2022年10月)：正式将原生的 M1/M2/M3 Mac 芯片 GPU 加速 (MPS) 引入稳定版。
* v1.10 - v1.12 (2021年 - 2022年)：大力发展 分布式训练生态 (Distributed)，引入 FullyShardedDataParallel (FSDP)，为后来的超大规模百亿/千亿参数大模型（LLM）训练奠定了基础。
* v1.5 - v1.9 (2020年 - 2021年)：强化了 C++ 前端 API 的对齐，大幅度升级了用于工业部署的 TorchScript。
* v1.0 (2018年12月)：里程碑版本。正式合并了 Caffe2 的生产部署能力。PyTorch 从此不再只是一个“好玩的学术界玩具”，而是具备了从科研到工业级落地的一体化能力。 [8, 9] 

## 三、 0.x 时代（2016年 – 2018年）：初期探索
早期的 PyTorch 还在寻找最适合 Python 开发者的数据结构和设计模式。

* v0.4 (2018年4月)：重大架构调整。在此版本之前，张量（Tensor）和带有求导功能的变量（Variable）是分开的（类似于现在的 tf.Variable）。从 0.4 开始，Variable 与 Tensor 正式合并，Tensor 原生支持 requires_grad。
* v0.1 - v0.3 (2016年 - 2018年)：由 Meta (Facebook) 的人工智能研究中心 (FAIR) 主导，基于 Lua 版本的 Torch 核心和 Chainer 的设计理念设计，迅速积累了第一批极客粉丝。 [1, 8, 11, 12] 

------------------------------
## 💡 核心版本一览表 (历史大事件)

| 主版本号 [3, 4, 5, 6, 8, 11, 12] | 发布年份    | 核心心智 / 重大改变                                           |
| -------------------------------- | ----------- | ------------------------------------------------------------- |
| 0.1 - 0.3                        | 2016 - 2017 | 初出茅庐，主打 Define-by-Run 动态图                           |
| 0.4.0                            | 2018        | Variable 与 Tensor 合并，奠定现代 API 基础                    |
| 1.0.0                            | 2018        | 合并 Caffe2，进军工业级模型部署                               |
| 1.6.0                            | 2020        | 官方内置自动混合精度训练（AMP），训练速度翻倍                 |
| 1.13.0                           | 2022        | 全面支持苹果 Apple Silicon (MPS) 硬件加速                     |
| 2.0.0                            | 2023        | 引入 torch.compile，进入深度学习编译器时代                    |
| 2.12.0                           | 2026 (最新) | 统一跨硬件图加速 API（torch.accelerator），大幅优化大模型性能 |

您目前在使用哪个版本的 PyTorch？如果是 2.0 以上的版本，强烈建议尝试在训练中加入 model = torch.compile(model)，这可以为你带来显著的硬件性能红利。如果有具体的版本不兼容报错或想了解某个特定算子的演进，可以随时告诉我。 [4, 5, 8] 

- [1] [https://en.wikipedia.org](https://en.wikipedia.org/wiki/PyTorch)
- [2] [https://pytorch.org](https://pytorch.org/get-started/pytorch-2-x/)
- [3] [https://pypi.org](https://pypi.org/project/torch/)
- [4] [https://pytorch.org](https://pytorch.org/get-started/pytorch-2-x/)
- [5] [https://pytorch.org](https://pytorch.org/blog/pytorch-2-0-release/)
- [6] [https://github.com](https://github.com/pytorch/pytorch/releases)
- [7] [https://pytorch.org](https://pytorch.org/blog/pytorch-2-11-release-blog/)
- [8] [https://github.com](https://github.com/pytorch/pytorch/wiki/PyTorch-Versions)
- [9] [https://github.com](https://github.com/pytorch/pytorch/releases)
- [10] [https://github.com](https://github.com/pytorch/pytorch/wiki/PyTorch-Versions)
- [11] [https://github.com](https://github.com/pytorch/pytorch/wiki/PyTorch-Versions)
- [12] [https://docs.pytorch.org](https://docs.pytorch.org/docs/versions.html)
