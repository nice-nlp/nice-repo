# NICE 90期 | 能量视角下的大语言模型对齐：从训练到推理的统一理解

## 主题

能量视角下的大语言模型对齐：从训练到推理的统一理解

## 时间

2025.09.11 20:00

## 内容

论文信息
[ICLR 2025] On a Connection Between Imitation Learning and RLHF，https://arxiv.org/abs/2503.05079
Inference-time Alignment in Continuous Space，https://arxiv.org/abs/2505.20081

内容介绍
大语言模型对齐（LLM Alignment）旨在确保模型输出契合人类偏好与价值观。现有做法大致作用于两个阶段：其一于训练阶段通过更新参数实现对齐，其二于推理阶段在不改动参数的前提下通过采样策略达成对齐。本分享立足于能量模型（Energy-Based Model, EBM）的视角，提出对齐的统一框架，将对齐的核心提炼为:“从奖励模型参数化的能量分布中进行高效采样”。鉴于直接从能量模型采样的困难性，本分享将以两个互补工作为核心，分别对应训练与推理两个阶段，给出系统化的理解与方法论。
训练阶段：On a Connection Between Imitation Learning and RLHF
该工作以奖励模型参数化的能量分布为桥梁，揭示了基于人类反馈的强化学习（RLHF）与模仿学习（Imitation Learning, IL）之间的紧密联系：RLHF 的本质并非传统意义上的强化学习，而是在偏好数据分布上隐式执行的模仿学习。基于这一洞见，该工作提出 Direct Imitation Learning（DIL）框架，直接优化模仿学习目标，将 DPO 等主流对齐算法统一为特例，并自然引出一系列可扩展的变体，为对齐算法的设计提供了更为坚实的理论基础与实践指导。
推理阶段：Inference-time Alignment in Continuous Space
面向无法更新模型参数的现实推理场景，该工作直接利用奖励模型参数化的能量分布，在连续输出空间进行朗之万动力学采样，提出 Simple Energy Adaptation（SEA）。相较于传统采样策略，SEA 更有效地利用梯度信息，引导生成朝向高奖励区域，在无需额外训练的情况下显著提升对齐效果。作为一种连续空间采样方法，SEA 克服了离散采样中的自回归误差累积与传递，有效缓解浅对齐（Shallow Alignment）问题，并在前缀攻击等对抗场景下展现出更强的鲁棒性。

### 入群

欢迎加入NICE每周分享交流群，可与NICEer唠嗑，以及第一时间收到后续NICE分享报告的通知。加群通过小助手认证，群内无广告。

<div align=center>
<img src="../images/nice_41_qr.png" width = "200">
<p>备注【昵称-单位-方向-NICE入群】</p>
</div>
