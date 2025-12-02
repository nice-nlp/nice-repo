# NICE 61期 | 推理模型的“过思考”现象与高效推理Panel，深度探讨与分析

## 主题

推理模型的“过思考”现象与高效推理Panel，深度探讨与分析

## 时间

2025年6月6日15:00-17:30

## 内容

论文：Dynamic Early Exit in Reasoning Models
链接：https://arxiv.org/abs/2504.15895
github：https://github.com/iie-ycx/DEER
依托于测试时扩展定律（test-time scaling law），当前的大语言模型通过延长生成长度在多项推理任务中实现了显著的性能提升。然而，这类模型在推理过程中普遍存在“过思考”（overthinking）问题，不仅显著降低了生成效率，还可能引入冗余的自我验证和思路切换，导致原本能够正确回答的问题反而被修改为错误答案。为此，我们提出了 DEER 方法，在模型思维切换的关键节点提示其生成中间答案，并在置信度足够高时提前终止推理过程。DEER 以简单有效的方式缓解了“过思考”问题，在涵盖 10 个基准任务和 11 个推理模型的实验中，推理长度平均减少了 19.1% 至 80.1%，同时准确率提升了 0.3% 至 5.0%。 

论文：Reasoning Beyond Language: A Comprehensive Survey on Latent Chain-of-Thought Reasoning
链接：https://arxiv.org/abs/2505.16782
github：https://github.com/EIT-NLP/Awesome-Latent-CoT
传统思维链（CoT）推理依赖自然语言显式表达推理步骤，导致计算效率低下且难以支持抽象认知过程。本文针对新兴的潜在思维链推理（Latent CoT）范式，首次提出系统性综述与多维分析框架。通过解耦推理过程与语言表达，潜在CoT在隐式空间中进行类思维运算，显著提升推理速度并支持非语言化认知表征。我们从方法创新（Token-wise strategies, internal mechanisms）可解释性分析与应用实践构建分类体系，期望为推动 LLM 推理领域的这一新方向提供结构化的理论与实践基础。

论文：Optimizing Anytime Reasoning via Budget Relative Policy Optimization
链接：https://arxiv.org/pdf/2505.13438
github：https://github.com/sail-sg/AnytimeReasoner
目前主流的RL with verifiable rewards范式只优化在最大的token budget下的推理性能，导致训练和推理效率比较低下。我们提出了AnytimeReasoner，来优化LLM在任意thinking budget下的表现。通过从一个先验分布中采样thinking budget，我们可以很自然的将verifiable dense rewards引入到RL之中，同时我们提出了一个新的variance reduction技术（BRPO）来提高训练稳定性和效率。实验表明AnytimeReasoner在所有的thinking budget下都显著优于GRPO，并大幅提升了训练和推理效率。

近年来，以OpenAI o1、DeepSeek-R1等为代表的大语言模型在链式推理能力上取得了显著突破，使其在数学推导、代码生成等复杂任务中展现出卓越性能。然而，目前的推理模型普遍存在“过思考”（Overthinking）现象，即模型在面对简单问题时仍可能生成冗长的推理步骤，产生大量冗余中间字符。这不仅显著增加推理延迟，还带来不必要的计算资源消耗，制约了大语言模型的实际部署效率。本次分享简要分析引起“过思考现象”的潜在因素，并总结目前大模型高效推理的相关研究思路。

论文：Understanding R1-Zero-Like Training: A Critical Perspective
链接：https://arxiv.org/pdf/2503.20783
github：https://github.com/sail-sg/understand-r1-zero
GRPO是PPO的一种特殊形式，它不学习critic model而是利用多次采样进行value估计。这种方法因为计算和内存高效，近来收到大量的关注。本质上，GRPO属于Monte Carlo policy gradient方法，但他的原始形式却带有optimization bias。我们对这种bias进行了分析，并且修正它，提出Dr. GRPO (GRPO Done Right)。进一步，我们在R1-Zero 这种训练范式下，对一些topic进行了探究，得到了一些有趣的结论。 

### 入群

欢迎加入NICE每周分享交流群，可与NICEer唠嗑，以及第一时间收到后续NICE分享报告的通知。加群通过小助手认证，群内无广告。

<div align=center>
<img src="../images/nice_41_qr.png" width = "200">
<p>备注【昵称-单位-方向-NICE入群】</p>
</div>
