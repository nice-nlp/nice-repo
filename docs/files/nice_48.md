# NICE 48期 | 编辑/推理/可解释等分享@ICLR2025

## 主题

编辑/推理/可解释等分享@ICLR2025

## 时间

2025.3.16 10:00

## 内容

论文：Learning dynamics of LLM finetuning

1. 提出了一个微观的观察理念（模型学习xu会如何影响它对xo的预测）来理解LLM的不同finetuning算法；
2. 可证明的squeezing effect：在分布的valley region加负梯度会让模型变得很奇怪；
3. 用上述两个工具，解释了LLM在SFT，off-policy DPO等算法中的一些反直觉现象。

论文：AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models

大型语言模型（LLMs）存在输出错误或知识过时的问题。因此，模型编辑方法被提出，用于实现针对性的知识更新。目前主流的编辑范式是Locate-then-Edit方法，即先找到影响特定知识的参数，再通过施加扰动来修改。然而，这种扰动通常会不可避免地破坏模型原有的知识，尤其在连续编辑情境下更加明显。本文提出一种新方法 AlphaEdit，在扰动参数前，先将扰动投影到保留知识的零空间（null space）中，从理论上保证被保留知识的输出结果不变，从而避免知识破坏问题。在多个LLMs（如LLaMA3、GPT2-XL、GPT-J）上的大量实验表明，只需增加一行投影代码，AlphaEdit即可平均提升现有Locate-then-Edit方法性能。

论文：Expand and Compress: Exploring Tuning Principles for Continual Spatio-Temporal Graph Forecasting

流场景中的时空预测面临双重挑战：对新数据进行调优模型的低效率，以及面对长期流数据中灾难性遗忘的不利影响。为了应对这些挑战，我们提出了一种新的基于提示调优的连续预测方法，EAC，遵循以实证和理论分析为指导的两个基本调优原则：扩展和 压缩，有效地解决了上述轻量级调优参数的问题。

论文：CollabEdit: Towards Non-destructive Collaborative Knowledge Editing

LLMs的协同学习作为一种新兴范式，能够在保证隐私的前提下利用多个参与方的私有数据。然而现有研究对于协同知识剪辑这一新场景还是一片空白。本篇工作首次针对协同KE展开研究，提出了新场景下知识重叠、冲突和遗忘三大新挑战以及无损协同知识剪辑框架CollabEdit。该框架通过新颖的无损模型融合机制模拟了全局KE这一理想最优行为，保证隐私的同时阻止了性能下降。实验表明，CollabEdit在多个数据集多种模型上均实现了无损协同剪辑，也为解决和探究未来协同KE场景下的新挑战和新应用提供了新思路。

论文：RGB-Event ISP: The Dataset and Benchmark

本论文首次研究了事件引导的图像信号处理（ISP）。首先，我们构建了一个全新的事件-RAW 数据集，该数据集由一种新型传感器采集，能够记录像素级对齐的事件流和 RAW 图像。其次，我们设计了一个传统 ISP 流水线，基于白平衡、去噪、色彩空间转换等基本操作，生成高质量的 RGB 参考图像。然后，我们对现有的可学习 ISP 方法进行分类，并在新数据集上训练和评估多种方法。最后，我们提出了一个简单的事件引导 ISP 方法，并探讨 RGB-Event ISP 领域的关键挑战与未来方向。这项研究为事件相机在 ISP 领域的应用提供了重要基础，希望能推动该方向的发展。

论文：Bridging context gaps: Leveraging coreference resolution for long contextual understanding

大型语言模型（LLMs）在自然语言处理方面展现出了卓越的能力，然而，在理解长文本上下文和执行有效的问答任务时，它们仍然面临挑战。这些挑战通常源于长文本中的复杂性和歧义性。为提升LLMs在此类场景下的表现，我们提出了一种名为 长问题指代消解自适应（LQCA） 的方法。该创新框架专注于针对长文本的指代消解，使模型能够有效识别和管理指代关系。在多个LLMs和数据集上的实验评估表明，该方法取得了积极成效，尤其在 OpenAI-o1-mini 和 GPT-4o 模型上表现出显著提升。这一结果表明，利用指代消解来弥合上下文理解的鸿沟，是提升问答任务效果的有效策略。

### 入群

欢迎加入NICE每周分享交流群，可与NICEer唠嗑，以及第一时间收到后续NICE分享报告的通知。加群通过小助手认证，群内无广告。

<div align=center>
<img src="../images/nice_41_qr.png" width = "200">
<p>备注【昵称-单位-方向-NICE入群】</p>
</div>
