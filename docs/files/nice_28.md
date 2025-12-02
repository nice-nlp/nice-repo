# NICE 28期 | “显微镜”下的检索增强生成：通过 RAGChecker 进行细粒度诊断评估
RAG Under the Microscope: Fine-grained Diagnostic Evaluation by RAGChecker

## 主题

“显微镜”下的检索增强生成：通过 RAGChecker 进行细粒度诊断评估
RAG Under the Microscope: Fine-grained Diagnostic Evaluation by RAGChecker

## 时间

2024.9.21 10:30am 周六

## 内容

论文：RAGCHECKER: AFine-grained Framework for Diagnosing Retrieval-Augmented Generation
链接：https://arxiv.org/abs/2408.08067

大纲
- 引言
  - RAG系统概述
  - 评估RAG系统的挑战
- 背景
  - 现有RAG评估方法及其局限性
  - 细粒度RAG评估框架的需求
- 细粒度幻觉检测
  - 幻觉简介
  - RefChecker：以知识为中心的幻觉检测
  - KnowHalBench数据集
  - 实验结果
- RAGCHECKER 指标
  - 总体指标
    - 精度，召回率，F1分数
  - 检索器诊断指标
    - 声明召回率，上下文精度
  - 生成器诊断指标
    - 上下文利用率，噪声敏感性，幻觉等
- 元评估：为什么RAGChecker可靠
  - 与现有评估框架的比较
  - 与人工判断的相关性
- 实验结果分析
  - 基准数据集和基准RAG系统评估
  - RAG系统设计中的重要发现和平衡
  - RAG配置的建议
- 局限性与未来工作
  - RAGCHECKER的局限性
  - 潜在改进和未来扩展领域
- 总结与问答

引言
大型语言模型（LLMs）在文本生成方面表现出卓越的能力，但它们通常存在信息过时和幻觉的问题。面对这些问题，检索增强生成（RAG）系统成为一种有效的解决方案。RAG 通过整合外部检索到的知识来增强大模型，从而实现更精确和上下文相关的回答。
随着 RAG系统逐渐成为各种应用的核心部分，开发鲁棒且全面的评估框架显得尤为重要。然而，评估RAG系统面临若干挑战：1）模块化复杂性：RAG系统由检索器和生成器组成，设计有效的评估指标以评估整个系统以及各个模块变得困难。2）指标局限性：现有指标通常难以为检索和生成组件提供准确且可解释的结果，尤其对于较长的回答。3）指标可靠性：现有指标在RAG中的可靠性仍未得到充分探索，特别是在与人类判断的一致性方面。现有的方法往往侧重于RAG系统的特定方面，或者缺乏细粒度的评估能力。
在此背景下，RAGCHECKER框架引入了一种RAG评估的新方法。它旨在通过针对性地检查片段声明级的蕴涵关系，为检索和生成过程提供全面的评估。RAGCHECKER提供了一套指标，用于诊断RAG系统的性能，识别错误来源，并指导系统设计的改进。本次分享将深入探讨RAGCHECKER框架、实现方法，以及它对RAG系统开发和改进的潜在影响。

### 入群

欢迎加入NICE每周分享交流群，可与NICEer唠嗑，以及第一时间收到后续NICE分享报告的通知。加群通过小助手认证，群内无广告。

<div align=center>
<img src="../images/nice_41_qr.png" width = "200">
<p>备注【昵称-单位-方向-NICE入群】</p>
</div>
