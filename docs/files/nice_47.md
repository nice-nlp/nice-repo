# NICE 47期 | 多模态论文分享@ICLR2025

## 主题

多模态论文分享@ICLR2025

## 时间

2025.3.15 19:00

## 内容

论文：Towards Semantic Equivalence of Tokenization in Multimodal LLM

多模态大语言模型（MLLMs）在视觉-语言任务中表现卓越，其核心组件vision tokenization旨在将视觉信号高效转换为对大语言模型（LLM）有利的特征表示。然而，现有vision tokenizers在实现视觉与语言语义对齐方面存在挑战，固定分块方法破坏了视觉语义完整性，影响LLM理解。为此，本文提出动态语义等效视觉分词器（SeTok），采用动态聚类算法将视觉特征划分为语义单元，并根据图像复杂度自适应调整token数量，保持语义完整性的同时更合理表达视觉信息。基于SeTok的增强型MLLM Setokim在多项任务中表现显著提升，实验验证了其在视觉语义建模和跨模态理解方面的优越性。

论文：reconstructive visual instruction tuning

我们提出了重建引导的多模态大模型（ROSS），利用以视觉为中心的监督信号，实现细粒度理解能力的显著提升。与传统的仅对文本输出进行监督的方法不同，ROSS引导模型重建输入图像来实现对视觉输出的监督。这种方法充分利用了那些在纯文本监督中容易丢失的，输入图像中本身固有的丰富细节。由于视觉信号的空间冗余较大，ROSS采用了一种去噪目标来重构输入图像的潜在表示。实验表明，ROSS在不同的视觉编码器和语言模型上均能持续带来显著改进。相较于集成多个视觉专家的最先进的方案，ROSS仅使用单一的SigLIP视觉编码器就能提供具有竞争力的表现。

论文：F3Set: Towards Analyzing Fast, Frequent, and Fine-grained Events from Videos

主要研究视频分析中的 快速、高频、细粒度 (F3) 事件检测 问题。现有方法难以同时满足这三个标准，主要受运动模糊和微小视觉差异的影响。为此，本文提出 F3Set，一个新的基准数据集，包含超过 1000 种事件类型，并提供精确的时间戳和多层次粒度。基于 F3Set，我们评估了现有的时间动作理解方法，并提出 F3ED，一种新模型，能够在单张 GPU 上高效训练并实现领先性能。该数据集和模型可用于体育分析等多个领域，并可能扩展至其他应用场景。

论文：Zigzag Diffusion Sampling: Diffusion Models Can Self-lmprove via Self-Reflection

Zigzag Diffusion Sampling（Z-Sampling）提出了一种新的扩散模型采样方法，通过在去噪和反转过程中交替进行自我反射，利用去噪和反转之间的指导间隙逐步累积语义信息，从而可以提高图像生成质量和文本-图像对齐度。

论文：Temporal Reasoning Transfer from Text to Video 

时序信息的理解是视频理解任务中的关键能力。我们发现，当前视频大语言模型（Video LLMs）在时序理解上的瓶颈主要在于其LLM部分，而非视觉编码模块。基于这一洞见，我们提出了一种全新的方法——Textual Temporal Transfer（T3），通过引入纯文本的时序理解数据来提升Video LLMs的视频时序理解能力。实验结果表明，在完全未使用任何视频训练数据的情况下，T3显著提升了LongVA-7B在多个视频理解基准中的表现，其效果甚至超过了采用大量视频训练数据的模型以及拥有20-40B参数规模的模型。 

论文：MLLM can see? Dynamic Correction Decoding for Hallycination Mitigatior

多模态大语言模型（MLLMs）常出现幻觉现象，原因尚不明确。本文通过实证分析发现，MLLMs在最终输出中可能错误生成物体，但在前置层中能正确识别图像内容。推测语言模型的强知识先验可能压制了视觉信息，导致幻觉。为此，我们提出动态修正解码方法——DeCo，自适应选择前置层并按比例整合知识到最终层，调整输出logits。DeCo与模型无关，可结合多种经典解码策略，适用于不同MLLMs。实验表明，DeCo在基准测试中显著减少幻觉频率，展现了其在缓解幻觉问题上的潜力。

### 入群

欢迎加入NICE每周分享交流群，可与NICEer唠嗑，以及第一时间收到后续NICE分享报告的通知。加群通过小助手认证，群内无广告。

<div align=center>
<img src="../images/nice_41_qr.png" width = "200">
<p>备注【昵称-单位-方向-NICE入群】</p>
</div>
