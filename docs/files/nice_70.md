# NICE 70期 | 可解释性论文分享 @ICML&ACL2025

## 主题

可解释性论文分享 @ICML&ACL2025

## 时间

第一场：2025.06.22 (周日) 9：00 

## 内容

论文：CKnowEdit: A New Chinese Knowledge Editing Dataset for Linguistics, Facts, and Logic Error Correction in LLMs
论文链接：https://arxiv.org/abs/2409.05806

论文介绍：汉语作为一种具有深厚文化底蕴的语言体系，其独特之处体现在古诗、谚语、成语等文化载体中。然而当前大语言模型（Large Language Models, LLMs）在这些专业领域仍存在明显局限，亟需通过针对性训练优化（targeted training optimizations）来建立能够系统评估、持续更新并逐步提升这类文化语言能力的综合数据集。为填补这一空白，我们推出首个中文知识编辑数据集CKnowEdit，专门用于修正LLMs在汉语知识中存在的语言性、事实性与逻辑性错误。我们从经典典籍、成语典故到百度贴吧"弱智吧"等多元渠道收集了七类知识，充分考虑汉语特有的多音字（polyphony）、对仗（antithesis）和逻辑结构等特征。通过对该数据集的分析，我们揭示了当前LLMs在掌握汉语知识时面临的核心挑战。此外，基于对最先进知识编辑技术的评估，我们发现了推进中文知识校正的重要改进方向。 

论文：Learning to Look at the Other Side: A Semantic Probing Study of Word Embeddings in LLMs with Enabled Bidirectional Attention
论文链接：https://github.com/Zhaoxin-Feng/semantic-probing-2025

论文介绍：自回归大语言模型（Autoregressive Large Language Models）在语言理解和生成方面展现出卓越性能。然而，由于单向注意力机制（unidirectional attention mechanism）的限制，其在文本嵌入任务中的应用进展相对缓慢，对其在探测任务中语义表征的分析也较为有限。本文旨在探讨是否在LLMs中启用双向注意力（bidirectional attention）可以克服这些限制。我们测试了经过额外训练步骤的Llama架构的不同变体，这些变体逐步实现了双向注意力机制，并进行了无监督/有监督对比学习（unsupervised/supervised contrastive learning）的训练。实验结果表明，双向注意力提高了LLMs对后续上下文的表征能力，但削弱了对先前上下文的利用能力，而对比学习训练则有助于同时保持这两种能力。 

论文：Eigenspectrum Analysis of Neural Networks without Aspect Ratio Bias 

论文介绍：近年来，通过权重矩阵的特征谱（eigenspectrum）来诊断深度神经网络（Deep Neural Networks, DNNs）已成为活跃的研究领域。从宏观来看，DNNs的特征谱分析涉及测量权重矩阵经验谱密度（Empirical Spectral Density, ESD）的重尾性（heavytailness）。这种方法能揭示模型的训练质量，并为分层训练超参数（layer-wise hyperparameters）的优化提供指导。
本文针对此类特征谱分析方法面临的一个关键挑战展开研究：权重矩阵长宽比对重尾性度量指标的估计影响。我们发现，不同尺寸的矩阵会导致重尾性度量出现不可忽略的偏差，进而引发模型诊断错误和分层超参数分配失准。为克服这一挑战，我们提出固定长宽比矩阵子采样方法（Fixed-Aspect-Ratio Matrix Subsampling, FARMS），该方法通过采样具有固定长宽比的子矩阵对权重矩阵进行标准化。我们不再直接测量原始ESD的重尾性，而是计算这些子矩阵ESD的平均重尾性。实验证明，固定长宽比的子矩阵能有效消除长宽比偏差。
我们在涉及权重特征谱分析的多种优化技术和应用场景中验证了FARMS的有效性，包括 计算机视觉（CV）模型的图像分类，科学机器学习（Scientific Machine Learning, SciML）模型训练，大语言模型剪枝
结果表明，尽管方法简单，FARMS能一致性地提升特征谱分析精度，并在上述场景中实现更有效的分层超参数分配。在LLaMA-7B模型的剪枝实验中，FARMS相较现有最优方法将困惑度（perplexity）降低了17.3%。

论文：Massive Values in Self-Attention Modules are the Key to Contextual Knowledge Understanding
项目地址：https://github.com/MingyuJ666/Rope_with_LLM

论文介绍：大语言模型在上下文知识理解方面取得了显著成功。本文发现，在各种基于Transformer的现代LLMs中，这些高度集中的极值持续出现在注意力查询（query, Q）和键（key, K）的特定区域，而在值（value, V）中则未出现类似模式（Q、K、V分别代表查询层、键层和值层输出的表征）。通过大量实验，我们进一步证明这些极值在解释上下文知识（从当前上下文窗口获取的知识）而非检索模型参数中存储的参数化知识方面起着关键作用。我们对量化策略的深入研究显示，忽略这些极值会导致需要丰富上下文理解的任务性能显著下降，这与我们的分析一致。最后，我们追溯这些集中极值的出现原因，发现这种集中现象是由旋转位置编码（Rotary Positional Encoding, RoPE）引起的，且从第一层就开始出现。这些发现为理解Q和K在LLMs中的运作机制提供了新视角，并为模型设计和优化提供了实用见解。 

论文：Statistical Hypothesis Testing for Auditong Robustness in Language Models 

论文介绍：假设您基于提供的信息向一个大语言模型寻求治疗建议。随后，出于尝试心理，您修改了提示中的部分信息（例如更改性别）再次询问LLM。令人惊讶的是，您得到了不同的治疗建议。此时可能产生一个关键问题：这种差异是否源于您所修改的信息？简而言之，仅通过单次提问我们无法确定。因为语言模型对相同问题的回答本身存在随机波动。因此，我们真正需要关注的是：LLM生成的响应类型是否发生了本质变化？更进一步，我们希望能量化（赋予数值）这种变化的程度，并判断其是否具有统计显著性。这正是本研究的核心贡献——建立了响应变化的量化方法，并基于这些数值进行统计分析。该研究具有多重应用价值。例如评估模型是否对有效信息变更（"真阳性"）作出合理响应调整，检测模型是否对不应影响结果的特征（如姓名拼写错误或与诊断无关的身高变化）产生虚假差异响应（"假阳性"），若模型因这类无关特征改变治疗建议，其可信度将受质疑。反之，我们也能识别模型在面对本应改变结论的重要新信息时却维持原建议的情况。

论文：Neural Incompatibility: The Unbridgeable Gap of Cross-Scale Parametric Knowledge Transfer in Large Language Models
论文链接：https://arxiv.org/abs/2505.14436

论文介绍：大语言模型提供了一个参数透明、知识编码可访问的"透明大脑"，其内部参数可被分析、定位与迁移。因此，如何超越基于符号语言（symbolic language）的传统知识迁移范式，实现真正的参数化知识迁移（Parametric Knowledge Transfer, PKT）成为关键研究挑战。值得注意的是，探索通过参数在不同规模LLMs间迁移知识的有效方法，是一个极具价值的研究方向。本文首先论证了参数空间对齐（Alignment in parametric space）是实现跨尺度PKT的根本前提，并将既有研究中的知识迁移重新定义为后对齐PKT（Post-Align PKT, PostPKT）——该方法通过提取参数初始化LoRA（Low-Rank Adaptation），但需后续微调实现对齐。为降低微调成本，我们提出新型预对齐PKT（Pre-Align PKT, PrePKT）范式，并设计LaTen解决方案：仅需少量训练步骤即可实现跨尺度LLMs参数空间对齐，且无需后续训练。在四个基准测试上的实验表明，PostPKT与PrePKT均难以实现持续稳定的迁移效果。通过深度分析，我们发现不同规模LLMs之间存在神经不相容性（Neural Incompatibility）——即模型在行为模式与参数结构上的本质差异，这对实现有效PKT构成了根本性挑战。这些发现为LLMs参数架构研究提供了新视角，并为高效PKT的未来探索指明了方向。 

论文：Concept-Centric Token Interpretation for Vector-Quantized Generative Models
论文链接：https://arxiv.org/pdf/2506.00698

论文介绍：向量量化生成模型（Vector-Quantized Generative Models, VQGMs）已成为图像生成领域的强大工具。然而，VQGMs的核心组件——离散token的codebook——仍未被充分理解，例如：哪些token对生成特定概念的图像至关重要？本文提出概念导向的token解释方法（Concept-Oriented Token Explanation, CORTEX），通过识别概念特定的token组合来解译VQGMs。我们的框架包含两种方法：（1）样本级解释方法——分析单张图像中token的重要性分数；（2）codebook级解释方法——探索整个codebook以发现全局相关token。实验结果表明，CORTEX能有效解释生成过程中token的使用机制，在多个预训练VQGMs上超越基线方法。除提升VQGMs的可解释性外，CORTEX还可应用于定向图像编辑和捷径特征检测等场景。

### 入群

欢迎加入NICE每周分享交流群，可与NICEer唠嗑，以及第一时间收到后续NICE分享报告的通知。加群通过小助手认证，群内无广告。

<div align=center>
<img src="../images/nice_41_qr.png" width = "200">
<p>备注【昵称-单位-方向-NICE入群】</p>
</div>
