# NICE 64期 | Reasoning论文分享@ICML&ACL2025

## 主题

Reasoning论文分享@ICML&ACL2025

## 时间

2025.06.09 (周一) 09:00-12:00

## 内容

论文：Improving Rationality in the Reasoning Process of Language Models through Self-playing Game [ICML 2025] 

当前的大语言模型在推理任务中虽然表现出色，但在理解自身推理过程方面仍存在不足，尤其难以察觉自身推理中的错误（即使模型已掌握相关知识）。为此，我们提出了一种全新的、无需监督信号的自我提升策略——Critic Discerment Game（CDG）。该方法借鉴了 AlphaGo 中的对抗性 self-play 强化学习机制，通过两组互为对手的“Prover”与“Critic”的交互博弈，逐步增强模型对自身推理过程的认知与判断能力。实验结果显示，CDG 在多个任务领域中均带来了显著且一致的性能提升，模型不仅更擅长发现和修正自身的推理错误，也展现出更强的推理理解能力。这项工作为提升大模型的“自知之明”提供了全新思路。 

论文：InductionBench: LLMs Fail in the Simplest Complexity Class [ACL 2025] 

大语言模型（LLM）的推理能力已取得显著进展，以o1和o3为代表的模型已能完全或部分解决现有大多数基准测试任务。然而，这些测试主要关注演绎推理任务，如数学和编程类问题——这类任务的规则（如数学公理或编程语法）都有明确定义，语言模型可以据此规划并应用规则来推导答案。相比之下，语言模型从观测数据中推断潜在规则的归纳推理能力仍缺乏深入研究，而这种能力正是科学发现的核心，能让研究者从经验观察中总结出普遍规律。为系统评估语言模型的归纳推理能力，我们开发了InductionBench这一全新基准测试。实验结果显示，即便是当前最先进的语言模型，也难以处理亚正则函数层次结构中最基础的复杂度类别，这表明现有LLM在归纳推理方面存在明显不足。 

论文：Aristotle: mastering logical reasoning with a logic-complete decompose-search-resolve framework [ACL 2025] 

在大语言模型（LLMs）中，尽管现有推理方法在多种任务上取得了显著进展，但在逻辑推理任务中仍面临效率和效果的双重挑战。根本原因在于现有方法未能在分解、搜索与求解等过程中充分利用逻辑任务的结构性。为此，我们提出了逻辑完备推理框架 Aristotle，包含三大核心模块：逻辑分解器、逻辑搜索路由器和逻辑求解器。该框架在推理全流程中深度融合符号表达与逻辑规则，有效缓解逻辑推理中的瓶颈，降低子任务复杂度，减少搜索误差，并解决逻辑矛盾。多项数据集实验结果表明，Aristotle 在准确性与效率上均优于现有先进方法，尤其在复杂逻辑推理场景中表现突出。 

论文：Self Reasoning Language Models [ACL 2025] 

Inference-time Scaling 备受关注，它通过增加思维链的长度显著提升了大语言模型（LLM）在复杂推理任务中的表现。这些较长的中间推理基本原理体现了人类认知中的各种元推理技能，例如反思和分解，但这些技能难以创建和习得。在本研究中，我们引入了自推理语言模型（SRLM），模型本身可以合成更长的思维链数据，并通过自我训练迭代提升性能。通过结合一些演示示例（即1,000个样本），演示如何从现有回复中展开隐藏的推理链，这些推理链充当推理催化剂，我们证明了SRLM不仅提升了模型的初始性能，还能确保后续迭代中性能更稳定、更一致的提升。我们提出的SRLMMMLU、GSM8K、ARC-C、HellaSwag和BBH五项推理任务上，基于两个骨干模型，实现了超过+2.5分的平均绝对提升。此外，随着推理采样次数的增加，其性能提升也更为显著，例如在64次采样后，其平均绝对提升达到+7.89分，这展现了SRLM在强大基线模型基础上所展现出的深度、多样性和创造性的推理路径。 

论文：Teaching Language Models to Critique via Reinforcement Learning [ICML 2025] 

迭代改进能力是实现更高级人工智能的关键。我们的研究探索LLM Critic的高效训练方法，提出CTRL（Critic Training via Reinforcement Learning）框架，旨在教会语言模型生成既能准确判别方案正误，又能提供建设性具体改进建议的批判性反馈，从而有效引导其他模型迭代优化其输出。CTRL训练的Critic模型不仅能显著提升基础生成模型在复杂代码竞赛题目基准上的通过率，还能有效缓解多轮修正中的错误累积。此外，CTRL展现了强大的“弱模型指导强模型”的能力，并通过迭代式的“批判-修正”过程实现高效的测试时性能扩展。 

论文：Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback [ICML 2025] 

本工作提出 Test-Time Preference Optimization（TPO），一种无需重新训练、即可在推理阶段对齐大语言模型（LLM）输出与人类偏好的新方法。TPO通过将奖励模型提供的数值反馈转化为可解释的文本点评（即“文本损失”）和改进建议（即“文本梯度”），引导模型逐步优化回答。实验表明，TPO不仅能在少量迭代内显著提升未对齐模型的表现，甚至可超过已通过DPO等方式对齐的模型。此外，TPO具备良好的扩展性和效率，可作为训练时偏好优化的轻量替代方案。 

### 入群

欢迎加入NICE每周分享交流群，可与NICEer唠嗑，以及第一时间收到后续NICE分享报告的通知。加群通过小助手认证，群内无广告。

<div align=center>
<img src="../images/nice_41_qr.png" width = "200">
<p>备注【昵称-单位-方向-NICE入群】</p>
</div>
