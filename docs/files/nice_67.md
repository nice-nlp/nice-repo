# NICE 67期 | Efficiency论文分享@ICML&ACL2025

## 主题

Efficiency论文分享@ICML&ACL2025

## 时间

2025.06.13 (周五) 09:00

## 内容

论文：Parrallelcomp：Parallel Long-Context Compressor for Length Extrapolation [ICML 2025] 

该论文聚焦于大语言模型在处理超长文本的长度外推（超过 128K tokens）时所面临的挑战。当前多数无需额外训练的长度外推方法，虽然理论上可以延长模型的上下文处理能力，但在实际应用中却受到严重的显存瓶颈限制，同时还存在“注意力下沉”（attention sink）问题，使得模型难以在长上下文中保持有效性与可扩展性。为了解决这一难题，作者提出了一种名为 ParallelComp 的并行长上下文压缩的长度外推方法。该方法通过将输入动态分块并重用有限的位置编码，自动驱逐低置信度块和无关 token，并引入一种并行的 KV Cache 淘汰机制，从而有效降低了显存消耗，使得一个仅有 8 亿参数、且只支持 8K 长度上下文的模型，在无需重新训练的情况下，能够在单块 A100 80GB GPU 上处理最长 128K 的输入。此外，作者还对并行注意力机制下出现的几种偏差现象（包括注意力陷阱、近期偏好、中间偏好）进行了理论与实证分析，并提出相应的 KV Cache 驱逐策略来缓解这些问题。实验显示，经过 ParallelComp 优化后，该 8B 模型在处理超长文本任务中的性能可达到 GPT-4 的 91.17%，超过了一些闭源模型如 Claude-2 和 Kimi-Chat，同时分块处理效率提升了 1.76 倍，整体预处理阶段加速高达 23.5 倍，几乎没有明显的性能损失。这项工作展示了无需额外训练即可实现大语言模型高效处理超长上下文外推的潜力，并为后续研究提供了可扩展性和鲁棒性方面的新方向。 

论文：Beyond Matryoshka: Revisiting Sparse Coding for Adaptive Representation [ICML 2025 Oral]

许多大规模系统依赖于高质量的特征来支持检索、搜索和生成式建模等任务。俄罗斯套娃表示学习（Matryoshka Representation Learning，MRL）最近作为一种自适应嵌入长度的解决方案出现，但它需要完全重新训练模型，并且在短长度下性能明显下降。在本论文中，我们表明稀疏编码为实现自适应表示提供了一种引人注目的替代方案，具有最小的额外开销和更高的保真度。我们提出对比稀疏表示（Contrastive Sparse Representation，CSR），一种将预训练嵌入稀疏化为高维但选择性激活特征空间的方法。通过利用轻量级自编码和任务感知对比目标，CSR在保持语义质量的同时，允许在不同稀疏级别上进行灵活、经济高效的推理。在图像、文本和多模态基准测试上的广泛实验表明，CSR在准确性和检索速度方面始终以较大幅度优于MRL, 同时将训练时间缩短到MRL所需时间的一小部分。我们的研究结果确立了稀疏编码作为实际应用中自适应表示学习的强大范式，尤其适用于效率和保真度都至关重要的场景。 

论文：Fast Large Language Model Collaborative Decoding via Speculation [ICML 2025]

我们知道，LLM通过next-token prediction机制来生成文本的。一种自然想法是：与其只使用一个 LLM 来预测下一个 token，不如结合多个 LLM 的预测结果，来获得更可靠的输出。我们将这类方法称为LLM collaborative decoding。然而，这类方法每预测一个token就需要运行多个模型，推理时间会变为原来的n倍，因而在实际应用中难以部署。为此，我们提出Collaborative Decoding via Speculation （CoS）。CoS 可以加速任何形式的collaborative decoding方法——如model ensemble、contrastive decoding或decoding-time realignment，同时保持输出质量不变。此外，CoS 不需要任何额外训练、额外参数或额外计算成本。这意味着它可以直接替代现有的 LLM 协同解码方式。 

论文：Unlocking General Long Chain-of-Thought Reasoning Capabilities of Large Language Models via Representation Engineering [ACL 2025]

本工作探索如何解锁大语言模型中潜在的通用长链思考推理能力。现有研究表明，通过少量样本的微调，大语言模型可以展现出长链思考（long CoT）推理的能力，并且这种能力可以迁移到其他任务上。这引起了新的猜测：长链思考推理是否是大语言模型内在的一种通用能力，而不仅仅是在特定任务上通过训练获得的。本文首先从大模型中提取表征并发现：（1）大语言模型确实将long CoT推理编码为一种通用能力：通过可视化和定量分析，我们发现long CoT的表征集中在模型参数空间中的特定区域，并且与vanilla CoT的表征有明显区分。（2）Long CoT推理的可迁移性：不同领域（如数学、物理、化学、生物）的long CoT和vanilla CoT之间存在相似的对比表征。基于上述发现，我们提出了GLoRE，一种基于表征工程的新方法，用于解锁大语言模型通用的long CoT推理能力。实验证明了该方法在领域内（数学领域）和跨领域（物理、化学和生物领域）两种场景下的有效性、高效性与可扩展性。 

论文：Data Whisperer: Efficient Data Selection for Task-Specific LLM Fine-Tuning via Few-Shot In-Context Learning [ACL 2025]

为有效部署大语言模型（LLM），针对特定任务数据进行微调至关重要。面对日益增长的数据集规模，高效选取最优训练子集以平衡性能与计算成本成为关键挑战。传统数据选择方法或需在目标数据集上微调评分模型（耗时耗资源），或依赖启发式规则（未能充分利用模型预测能力）。为此，本文提出 Data Whisperer，一种高效、免训练的注意力机制方法。它利用待微调模型本身进行少样本上下文学习来选择数据。在多种任务、模型及原始/合成数据集上的综合评估表明，Data Whisperer 性能卓越：例如在 Llama-3-8B模型上，仅使用 10% 的 GSM8K 数据即可超越全量数据训练效果，同时以 3.1 分的性能提升和 7.4 倍的加速显著优于现有方法。 

论文：EffiCoder: Enhancing Code Generation in Large Language Models through Efficiency-Aware Fine-tuning [ICML 2025]

随着LLMs在代码生成中扮演越来越重要的角色，提升代码准确性和效率已成为关键。现有方法主要关注准确性，往往忽视代码效率瓶颈。为解决这一问题，我们引入EffiCoder，通过在包含准确且高效代码示例的高质量数据集上微调LLMs，同时提升这两个方面。我们的方法涉及利用多个LLMs生成不同编程语言下各类任务的多样化候选代码解决方案。随后通过本地执行直接测量其执行时间和内存使用情况对这些解决方案进行评估。每个任务中执行时间和内存消耗最低的代码解决方案被选为最终输出。实验结果表明，使用EffiCoder进行微调可带来显著提升。例如，Qwen2.5-Coder-7B-Instruct的pass@1得分从44.8%提升至57.7%，而正确任务的平均执行时间减少了48.4%。EffiCoder为推动AI驱动的代码生成提供了可扩展且有效的解决方案，既有利于软件开发，也有助于计算问题解决。 

论文：DRPruning: Efficient Large Language Model Pruning through Distributionally Robust Optimization [ACL 2025]

针对LLM参数量过大引发的训练与推理效率瓶颈，模型剪枝成为主流解决方案之一。然而，传统剪枝方法常导致LLM在不同领域能力丧失不均。为此，我们提出领域均衡剪枝方法，DRPruning，在剪枝和能力恢复的训练过程中动态调整各领域数据配比。我们改进了分布鲁棒优化算法，根据损失变化拟合scaling law曲线以动态设定优化目标，并将被优化的分布范围向更难的方向移动，使模型在剪枝后仍能对更广泛数据分布保持鲁棒。实验验证，DRPruning在剪枝、继续预训练和指令微调任务中均展现出显著且一致的性能提升，尤其在数据分布偏移严重的场景下。进一步的分析证明DRPruning能动态为更难的领域适当分配更高的权重，实现模型在所有领域性能的均衡提升。 

论文：FlatQuant: Flatness Matters for LLM Quantization [ICML 2025]

近年来，量化技术被广泛应用于大语言模型（LLMs）的压缩与加速。然而，由于模型中存在离群值，使用等间距量化点时需尽可能平坦化权重与激活值，以减少量化误差。已有研究探索了多种量化前的变换方法来抑制离群值，例如逐通道缩放和Hadamard变换。但我们观察到，这些变换后的权重和激活值仍可能呈现陡峭且分散的分布。为此，本文提出了一种新的后训练量化方法——FlatQuant（快速且可学习的仿射变换），旨在提升权重与激活值的平坦性。我们的方法为每个线性层学习最优的仿射变换，通过轻量目标在数小时内完成校准。为了降低仿射变换的推理开销，我们基于两个小矩阵的Kronecker乘积构造了轻量的分解仿射变换，能够实现与全尺寸变换相同的平坦效果，并将FlatQuant中的变换操作和量化操作融合为高效的单个算子。大量实验证明，FlatQuant在量化精度与效率方面均达到新的SOTA。例如，LLaMA-3-70B模型的W4A4KV4量化精度损失小于1%，相比SpinQuant提升了7.5%。同时在Qwen2.5-32B和DeepSeek v3上均能实现W4A4的精度损失小于1%。此外，与16位浮点模型相比，其在预填充阶段最高加速2.3倍，在解码阶段加速1.7倍。 

论文：Streamlining the Collaborative Chain of Models into A Single Forward Pass in Generation-Based Tasks [ACL 2025 Findings]

本文提出 FTHSS 方法，旨在优化基于生成任务的模型协作链效率。针对传统 “模型链” 需独立部署多模型、重复计算隐藏状态（KV 状态）的问题，FTHSS 通过提示微调实现跨模型的 KV 隐藏状态共享，避免中间结果的冗余前向传播，减少 KV 缓存存储开销。在单轮和多轮场景中，通过调整输入顺序与注意力掩码，使下游模型直接利用上游模型的 KV 状态。实验表明，FTHSS 在四项任务上性能与传统模型链相当，但推理延迟显著降低，内存占用减少，为高效多模型协作提供了新方案。 

### 入群

欢迎加入NICE每周分享交流群，可与NICEer唠嗑，以及第一时间收到后续NICE分享报告的通知。加群通过小助手认证，群内无广告。

<div align=center>
<img src="../images/nice_41_qr.png" width = "200">
<p>备注【昵称-单位-方向-NICE入群】</p>
</div>
