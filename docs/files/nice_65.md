# NICE 65期 | 别让AI困在题海里：模型评估如何摆脱应试枷锁？

## 主题

别让AI困在题海里：模型评估如何摆脱应试枷锁？

## 时间

2025.6.10 周二 10:30

## 内容

在人工智能（AI）快速发展的今天，模型的能力已超越了传统的自然语言处理范畴，迈向了更广泛、更复杂的一般性任务。然而，评测方法的发展却未能跟上模型进步的步伐。我们正站在一个关键的转折点上：如何公平、全面、动态地评估大语言模型（LLMs）的能力？
本次报告将基于两篇文章：根据综述介绍上半场中模型评估的范式迁移，并在此基础上介绍关于AI反向评估的新方法。 
论文：Toward Generalizable Evaluation in the LLM Era：A survey beyond benchmarks
链接：https://arxiv.org/pdf/2504.18838
代码地址：https://github.com/ALEX-nlp/Benchmark-of-core-capabilities/tree/main
论文：Teach2Eval: An Indirect Evaluation Method for LLM by Judging How It Teaches
链接：https://arxiv.org/pdf/2505.12259
代码地址：https://github.com/zhiqix/Teach2Eval

上半场：评测的演变与挑战 
在过去，评测主要依赖于静态数据集和任务特定指标，如MMLU、GSM8K等经典基准。这些方法虽然有效，但也暴露出诸多问题：数据污染风险、缺乏可解释性、难以扩展以及对生成能力的评估不足。随着模型能力的提升，传统评测方式已逐渐显现出其局限性。我们不得不重新思考：评测究竟是为了衡量结果，还是为了理解模型的真正能力，并促成模型进一步发展？ 
综述文章《Toward Generalizable Evaluation in the LLM Era：A Survey Beyond Benchmarks》系统梳理了评测范式的演进趋势：
- 从任务到能力 ：评测重心由具体任务转向通用能力（如推理、知识、安全等）。
- 从人工到自动化 ：借助自动化的数据处理及将LLM-as-a-Judge，实现高效、可扩展的评测流程。
- 从静态到动态 ：引入交互式评估、实时更新机制，增强评测的适应性和实用性。
但即便如此，核心问题仍未解决：如何确保评测本身具有泛化性？如何避免模型因过度拟合训练数据而失去真实能力？评测如何为模型训练提供反馈而非仅仅排名？ 

转折点：从“评什么”转为“怎么评” 
面对这些问题，《Teach2Eval: An Indirect Evaluation Method for LLM by Judging How It Teaches》提出了一种全新的间接评测框架：Teach2Eval 。它不再直接“考”模型，而是通过观察模型是否能教会一个较弱的学生模型完成任务，来衡量其综合能力。 
这一思想灵感来源于著名的“费曼学习法”（Feynman Technique）：真正掌握一个概念的最佳方式是能够向他人清晰地解释它 。在Teach2Eval中，教师模型（即被评测的LLM）需要不断指导学生模型改进解题策略，最终通过学生模型的进步程度来反映教师模型的教学能力和认知深度
Teach2Eval具备以下优势：
- 避免数据污染与记忆效应 ：不依赖固定答案，而是通过教学过程动态生成反馈。
- 多维能力评估 ：涵盖应用、判断、引导、反思四个层次，对应Bloom教育目标分类。
- 训练反馈闭环 ：不仅用于模型排名，还能揭示模型训练中的过拟合或偏倚问题，提供优化方向。
- 高度自动化与可扩展性 ：通过将开放问题转化为标准选择题（MCQ），并保持难度，实现自动评分与大规模部署。
实验结果显示，Teach2Eval与主流榜单（如Chatbot Arena和Livebench）高度相关，保持了直接评测的成本并更具稳定性和解释力。它不仅能评估模型“会不会”，更能评估模型“能不能教会别人”。 

欢迎一起探索AI评测的下半场——这里不只是分数的游戏，更是理解智能本质的关键一步。 

### 入群

欢迎加入NICE每周分享交流群，可与NICEer唠嗑，以及第一时间收到后续NICE分享报告的通知。加群通过小助手认证，群内无广告。

<div align=center>
<img src="../images/nice_41_qr.png" width = "200">
<p>备注【昵称-单位-方向-NICE入群】</p>
</div>
