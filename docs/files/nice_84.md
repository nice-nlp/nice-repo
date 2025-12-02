# NICE 84期 | Transformer 模型能否通过连接训练数据中的离散知识进行推理？

## 主题

Transformer 模型能否通过连接训练数据中的离散知识进行推理？

## 时间

2025.08.31 (周日) 10:00

## 内容

论文信息
标题：[ICLR 2025] Are Transformers Able to Reason by Connecting Separated Knowledge in Training Data? 
地址：https://arxiv.org/abs/2501.15857 

内容介绍
组合式推理——也就是把来自不同来源的知识整合到一起——是人类智能的标志之一。例如，如果一个人从一本书里学到 B = f(A)，又从另一本书里学到 C = g(B)，那么即使 ta 从未同时见过 A、B、C，ta 也能推理出： C = g(B) = g(f(A))。
为了研究 Transformer 是否具备组合式推理能力，我们提出了 FTCT（Fragmented at Training, Chained at Testing）这一合成任务。在该任务中，训练数据只包含彼此独立的知识片段，而测试时则要求模型能够重建完整的因果链条。
实验发现：
发现 1：Few-shot CoT（Chain of Thought，思维链）提示能够激发组合式推理能力 
从 zero-shot 到 one-shot，预测准确率出现了显著跃升。
发现 2：训练集与测试集的相似度是决定组合式推理能力出现的因素 
当训练与测试的相似度 λ ≥ 0.3 时，会出现组合式推理能力（这里 λ:= 训练时链条长度 / 测试时链条长度）。
发现 3：模型复杂度是决定组合式推理能力出现的因素 
具有足够深度 / 头数的 Transformer（≥2 层，≥2 个注意力头）在 分布内任务 和 组合式推理任务 上都能取得良好表现，而 MLP 在这两方面均表现不佳。
Transformer 的内在机制分析 ：Transformer 无法仅凭记忆训练数据达到在测试集上的优秀表现，其内部存在某种 “算法” 保证了模型的泛化性。我们运用语言模型的可解释性工具分析了 Transformer 模型实现组合式推理的内在机制，并提出并验证以下程序：
- 上下文学习（In-Context Learning）
- 父节点检索（Parent Retrieval）
上下文学习的证据：归纳头（Induction Heads） 
通过构建 Transformer 的注意力热力图，我们验证了 Transformer 模型可以通过浅层与深层的注意力机制相互配合实现对于前文关键节点信息的搜索、定位与拷贝。 
父节点检索的证据：注意力分配 
通过设计线性探针实验，我们发现了 Transformer 的隐状态能够高精度地编码父节点的取值，同时忽略非父节点的标记，形成十分有效率的记忆模式。 
结论 ：通过在合成数据上的实验，我们展示了 Transformer 具备发展 泛化推理能力 的潜力。这表明，当代大语言模型的优异表现不仅仅源于对海量数据的记忆，还体现出超越记忆的推理能力。

### 入群

欢迎加入NICE每周分享交流群，可与NICEer唠嗑，以及第一时间收到后续NICE分享报告的通知。加群通过小助手认证，群内无广告。

<div align=center>
<img src="../images/nice_41_qr.png" width = "200">
<p>备注【昵称-单位-方向-NICE入群】</p>
</div>
