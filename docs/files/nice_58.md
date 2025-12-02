# NICE 58期 | Test time scaling 综述! 从what, how, where 和how well帮你系统解构！

## 主题

Test time scaling 综述! 从what, how, where 和how well帮你系统解构！

## 时间

2025.5.3 10:30

## 内容

论文：What, How, Where, and How Well? A Survey on Test-Time Scaling in Large Language Models
链接：https://arxiv.org/pdf/2503.24235

当大模型的训练成本飙升、优质数据趋于枯竭，我们是否还有新的路径激发大模型的潜能？💡 OpenAI o1和DeepSeek R1的爆火让推理阶段扩展Test-Time Scaling（TTS）迅速成为后预训练时代的研究热点。TTS 不再“堆数据、堆参数”，而是在推理阶段动态加算力，让模型临场更聪明、更高效。
它不仅在数学、编程等“硬核任务”中表现亮眼，在开放问答、多模态理解甚至复杂规划等任务中，也展现出巨大潜力。而截止到现在，推理扩展的探索已经有一段时间，已有大量工作开始探索 CoT、Self-Consistency、Search、Verification 等策略，但现阶段依然缺乏一套系统性的综述来统一这些方法的研究视角与评估框架。
🔍 论文亮点概览： 本篇Survey首次提出了一个覆盖全面、多层次、可扩展的四维正交分析框架
1. What to scale：扩什么？CoT长度、样本数、路径深度还是内在状态？
2. How to scale：怎么扩？Prompt、Search、RL，还是Mixture-of-Models？
3. Where to scale：在哪扩？数学、代码、开放问答、多模态……
4. How well to scale：扩得怎样？准确率、效率、控制性、可扩展性……
在这个框架下，作者系统梳理了当前的主流TTS技术路线，包括：
- 并行策略（Self-Consistency / Best-of-N）
- 逐步演化（STaR / Self-Refine）
- 搜索推理（Tree-of-Thought / MCTS）
- 内在优化（DeepSeek-R1/OpenAI-o1）
在此基础上，作者展示了如何借助该框架对已有文献进行快速结构化解析，从而帮助我们清晰地理解、定位它们的贡献；由此，作者从中提炼出推理阶段扩展的主要发展路径。值得一提的是，这篇调研更强调在实践性上对研究者的帮助，因此，将不断总结针对不同场景的操作指南。最后，作者也给出了他们对于推理阶段扩展未来发展的思考和预测。

### 入群

欢迎加入NICE每周分享交流群，可与NICEer唠嗑，以及第一时间收到后续NICE分享报告的通知。加群通过小助手认证，群内无广告。

<div align=center>
<img src="../images/nice_41_qr.png" width = "200">
<p>备注【昵称-单位-方向-NICE入群】</p>
</div>
