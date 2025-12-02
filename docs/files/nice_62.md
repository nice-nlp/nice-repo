# NICE 62期 | 多模态论文分享@ICML&ACL2025

## 主题

多模态论文分享@ICML&ACL2025

## 时间

2025.06.07 周六 20:00

## 内容

论文：Subobject-level Image Tokenization [ICML 2025] 

我们所感知的视觉世界并不是由一个个固定的方块（patch）拼凑而成的，而是由丰富且连续的物体和细节构成。我们的工作Subobject-level Image Tokenization（https://arxiv.org/abs/2402.14327）提出了一种新的image tokenization方法，自适应地将图像划分成更符合视觉结构的subobject token——正如自然语言以更有语义意义的subword为单位构成一样。这有效提高了visual token的单义性（monosemanticity），与VLM结合后在多个视觉语言任务中展示了更快的收敛速度与更好的泛化性能。 

论文：Look Twice Before You Answer: Memory-Space Visual Retracing for Hallucination Mitigation inMultimodal Large Language Models [ICML 2025] 

我们提出了 MemVR 方法，解决多模态大模型（MLLMs）生成与图像内容矛盾的“幻觉”问题。受人类“遗忘时重复查看”的认知机制启发，MemVR在解码阶段动态重注视觉标记：当模型中间层不确定性超过阈值（如γ=0.75）时，将原始视觉特征作为键值对通过FFN层重注入文本解码器，增强视觉证据的实时补充。该方法无需额外训练或微调，在主流幻觉检测与综合性能基准上准确率均有提高，且推理延迟仅增加约4%（68.32ms/token vs 基线65.71ms）。实验表明，MemVR是当前唯一在降低幻觉同时提升通用能力的方法（如MME总分+32.2），兼容LLaVA、Qwen-VL等主流架构。

论文：On Path to Multimodal Generalist: General-Level and General-Bench [ICML 2025 Spotlight] 

当前的人工智能系统已能够处理文本、图像、音频等多种模态数据，但大多数多模态模型仍局限于特定任务或单一数据类型，缺乏类似人类智能的广泛适应性。此外，现有评估方法通常假设跨任务性能越高，模型的多模态能力就越强，这一标准可能存在局限性。为此，本研究提出两项创新资源：(1) General-Level 评估框架：用于衡量AI模型在跨任务、跨模态场景下的知识整合与应用能力；(2) General-Bench 基准数据集：涵盖700余项任务和32.5万条样本，专门用于测试模型的通用多模态能力。基于对100多个现有模型的系统评测，我们发现：尽管部分模型在单一任务上表现优异，但其跨任务、跨模态的知识迁移能力仍然薄弱。这一结果表明，当前多模态系统与真正通用的人工通用智能（AGI）仍存在显著差距。本研究的目标是为开发更强大的多模态AI系统提供指导，使其能够无缝理解与生成多种模态数据，从而推动人工智能向类人通用智能的方向发展。 

论文：AKRMap: Adaptive Kernel Regression for Trustworthy Visualization of Cross-modal Embeddings [ICML 2025] 

多模态高维嵌入如CLIP等在多模态任务中起到基础作用，例如可应用于跨模态生成模型的对齐评估。为增强跨模态对齐评估的透明度，降维可视化是一种重要途径。然而传统的降维可视化方法无法清晰展示大规模多模态数据集的对齐指标分布。本文提出一种核回归引导的参数化降维方法，能够更好地展示指标分布并支持交互式可视化，可用于全局展示文生图模型在基准数据集上的对齐表现，此方法亦可推广至其他跨模态任务如文生视频等。
陈德龙

论文：FIHA: Autonomous Hallucination Evaluation in Vision-Language Models with Davidson Scene Graphs [ACL 2025] 

大型视觉-语言模型（LVLM）快速发展却伴随普遍的幻觉问题，现有评估方法依赖昂贵的人工标注或额外 LLM，且难以覆盖对象属性、关系以及多种幻觉之间的依赖。针对这一痛点，本文提出零标注、零-LLM 的细粒度幻觉评估框架 FIHA（Fine-grained Hallucination evAluation）：它能在任意图像数据集上自动生成问答对，以极低成本同时评估图像和字幕中的幻觉，并显式建模不同幻觉类型的依赖关系。基于该框架，我们构建多模态基准集 FIHA-v1，涵盖 MS-COCO 和 Foggy Cityscapes 场景，并借助 Davidson Scene Graph 组织问答结构以提升评测可靠性。对多款主流 LVLM 的实验结果表明，FIHA-v1 能有效揭示模型在细粒度场景理解上的局限，为后续模型对齐和改进提供了数据与指标支持。 

论文：VideoRoPE: What Makes for Good Video Rotary Position Embedding? [ICML 2025 Spotlight]

尽管旋转位置编码（RoPE）及其变体因具备长上下文处理能力而被广泛应用，但RoPE从一维扩展到具有复杂时空结构的视频仍是一个未解决的挑战。本文首先提出一套系统分析，识别出RoPE在适应视频任务时需重点关注的四个关键特性，而这些在以往研究中往往被忽视。为验证分析，我们设计了更具干扰性的V-NIAH-D任务，在原有V-NIAH任务中引入周期性干扰项，结果表明现有RoPE变体在时间维度设计不当时容易被干扰信息误导。基于上述分析，我们提出了VideoRoPE方法，通过三维结构保留视频的时空关系。VideoRoPE具备以下核心特性：(1)低频时间分配，缓解周期性干扰；(2)对角布局，维持空间对称性；(3)可调时间间隔，实现时间与空间索引的解耦。在多个下游任务中（如长视频检索、视频理解、视频幻觉生成），VideoRoPE均显著优于现有RoPE变体。 

### 入群

欢迎加入NICE每周分享交流群，可与NICEer唠嗑，以及第一时间收到后续NICE分享报告的通知。加群通过小助手认证，群内无广告。

<div align=center>
<img src="../images/nice_41_qr.png" width = "200">
<p>备注【昵称-单位-方向-NICE入群】</p>
</div>
