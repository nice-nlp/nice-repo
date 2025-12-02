# NICE 49期 | 大模型对齐论文专题分享@ICLR2025

## 主题

大模型对齐论文专题分享@ICLR2025

## 时间

2025.3.22 10:30 am

## 内容

论文：Preference Optimization for Reasoning with Pseudo Feedback

论文简介：随着reasoning相关的技术发展，越来越多的工作意识到outcome supervision和RL/DPO在reasoning上重要性。R1的发布则进一步推动了scaling RL的边界。与此同时，一个很自然的问题是：我们显然无限制的标注数据，即使无需考虑成本，随着模型越来越强，标注问题本身的难度已经逐渐超过了绝大多数标注人员的水平。因此， 在这篇论文中我们试图探索完全由模型自己进行伪监督的可行性。在数学上，我们直接使用self-consistency来获取pseudo label构造监督信号；在竞赛编程上，我们首先使用普通的LLM合成test case input，然后让模型自行生成解题程序，并在合成的input上执行得到output，最后对output做投票得到pseudo input-output pairs用于构造监督信号。在多轮DPO的实验上，结果证明了，使用模型自身合成的弱监督信号也能够带来持续的提升。我们也进行了进一步的消融实验，发现在代码问题上，增加test case的规模可以有效地降低false positive sample的比例，从而提高监督信号的稳定性。 

论文：
(1) Steering Large Language Models between Code Execution and Textual Reasoning
(2) CodeSteer: Symbolic-Augmented Language Models via Code/Text Guidance

论文简介：大模型的 reasoning & planning 现在的趋势基本都是CoT (Chain of Thought)，比如 OpenAI o1 和 DeepSeek R1 都依赖纯文字推理来搜索答案。但很多 reasoning & planning 任务本质上需要符号计算，仅靠文字推理不仅低效，而且难以扩展。例如，让 R1 计算 24 点，它反复 textual reasoning 但仍然出错。更极端的例子是，现在 o1 还能走 5×5 迷宫，但换成 100×100 之后就完全失效。而代码 (coding) 其实是符号计算的天然载体，几乎所有 solver/planner/controller 都是基于代码实现，具备更好的完备性。像经典的 "9.11 vs 9.9"、"strawberry" 这类问题，在 prompt 里加上代码逻辑，GPT-4o 立刻能正确解答。让LLM调用人为设定的外部工具(solver)也能有效利用符号计算，但是没有LLM自主生成代码那么有泛化到不同任务的能力。
挑战在于：如何让 LLM 知道什么时候应该生成代码，什么时候用文字推理？即使 LLM 选择了代码，生成出的代码也可能只是伪代码或低效实现，并未真正结合符号计算。我们采用多轮 CodeSteer 引导，每一轮都会根据问题和已有尝试来优化下一步决策。 

论文：On a Connection Between Imitation Learning and RLHF

论文简介：本工作从模仿学习 (IL) 的视角研究了大语言模型 (LLM) 与偏好数据的对齐问题，建立了基于人类反馈的强化学习 (RLHF) 与模仿学习之间的紧密理论联系，揭示了 RLHF 的本质: 它并非传统意义上的强化学习，而是在偏好数据分布上隐式执行模仿学习。基于这一联系，我们提出了 DIL (Direct Imitation Learning)，一个直接优化模仿学习目标的理论框架。DIL 从模仿学习的角度统一了对齐问题，将现有 DPO 等主流对齐算法视作特例，并自然引出了新的变体。通过桥接模仿学习和 RLHF，DIL 为 RLHF 对齐提供了新的见解。 

论文：Jailbreaking as a Reward Misspecification Problem

论文简介：随着大语言模型的广泛应用，其安全性和可靠性问题日益突出，特别是"越狱攻击"（jailbreaking）现象引起了研究界的广泛关注。我们的研究首次从"奖励错误规约"（Reward Misspecification）的角度解释了为什么大语言模型会存在越狱漏洞。我们提出了ReGap度量方法来量化奖励错配程度，并基于此构建了ReMiss自动化红队系统，能够高效生成对抗性提示，探索模型的安全漏洞。ReMiss在AdvBench基准测试上显著优于现有方法，不仅攻击成功率高，还能保持生成提示的可读性。更重要的是，我们的方法能自动发现多样化的攻击模式（如翻译、续写、上下文示例等），并且对包括GPT-4o在内的闭源模型展现出极强的攻击迁移能力。 

### 入群

欢迎加入NICE每周分享交流群，可与NICEer唠嗑，以及第一时间收到后续NICE分享报告的通知。加群通过小助手认证，群内无广告。

<div align=center>
<img src="../images/nice_41_qr.png" width = "200">
<p>备注【昵称-单位-方向-NICE入群】</p>
</div>
