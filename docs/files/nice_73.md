# NICE 73期 | 视觉智能驱动的多模态对齐与推理

## 主题

视觉智能驱动的多模态对齐与推理

## 时间

2025.07.04 周五 10:30

## 内容

论文分享
- [NAACL 2025] Safe Inputs but Unsafe Output: Benchmarking Cross-modality Safety Alignment of Large Vision-Language Models, https://aclanthology.org/2025.findings-naacl.198.pdf 
- [ACL 2025] VisuoThink: Empowering LVLM Reasoning with Multimodal Tree Search, https://arxiv.org/pdf/2504.09130 
- [ACL 2025] World Modeling Makes a Better Planner: Dual Preference Optimization for Embodied Task Planning, https://arxiv.org/pdf/2503.10480 

内容介绍
在大语言模型展现强大能力的同时，多模态大模型正成为通往通用人工智能的关键路径。然而，当前的主流范式中，视觉往往只是被动接入语言模型的一个模态输入，其语义潜力和认知价值仍未被充分发挥。在漫长的人类进化中，我们依赖视觉去感知世界、思考交流、行动交互。我们思考“视觉是否只是大模型的输入接口，还是可以成为其认知结构的重要部分？” 本次分享将围绕“视觉智能驱动的多模态对齐与推理”这一主题，介绍我们近期在多模态大模型方面的探索性研究，内容将围绕以下三个关键问题展开： 
在模态对齐方面，如何理解跨模态的组合语义？ 我们首先关注模型“看懂”输入的能力。通过构建 SIUO 跨模态安全对齐数据集，我们揭示当前多模态大模型在组合语境下的风险盲区——即使在视觉和语言各自“看似安全”的前提下，也可能做出不当响应，推动对齐安全从简单单一模态向跨模态跃迁。 
在思维构建方面，如何让视觉参与推理过程？ 在实现基础对齐后，我们进一步思考模型“如何思考”。面对复杂的视觉推理任务，传统语言链式思维往往难以有效利用视觉信息。我们提出视觉-语言交错的多模态树搜索框架 VisuoThink，使模型能够在视觉与语言空间交替思考，实现基于视觉推理路径的test-time scaling。 
在行动规划方面，如何基于视觉建模世界并完成行动？ 具备推理能力之后，下一步就是“如何行动”。仅凭静态图文难以支持认知与决策的闭环，尤其在多步交互任务中，模型需要具备预测未来状态的能力。我们研究了视觉驱动的世界建模机制，使模型具备“看到之后能想象”的能力，从而在环境中实现更高效可泛化的行为规划能力。 

### 入群

欢迎加入NICE每周分享交流群，可与NICEer唠嗑，以及第一时间收到后续NICE分享报告的通知。加群通过小助手认证，群内无广告。

<div align=center>
<img src="../images/nice_41_qr.png" width = "200">
<p>备注【昵称-单位-方向-NICE入群】</p>
</div>
