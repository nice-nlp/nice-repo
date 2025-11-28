# NICE17期 | Transformer模型能否进行隐式的推理？一个关于Grokking和泛化的深入探索

## 主题

Transformer模型能否进行隐式的推理？一个关于Grokking和泛化的深入探索

## 时间

2024.7.13 上午10:30-11:30

## 内容

论文：Grokked Transformers are Implicit Reasoners: A Mechanistic Journey to the Edge of Generalization
地址：https://arxiv.org/abs/2405.15071
状态：在投 

内容
1. 背景 - Transformer语言模型隐式推理能力的欠缺
2. 我们为什么要关注隐式推理和参数化知识？
3. 研究方法与评估设计
4. Grokking现象与其背后原理的分析
5. 模型的内部电路（circuits）与系统性泛化
6. 参数知识对于复杂推理的重要性与潜力
7. 总结与展望
8. QA

研究背景
现今的大语言模型虽然能力广而出众，但许多工作发现它们依旧很难基于参数知识做隐式推理。这项缺陷会导致他们内部对知识和规则的表示冗余而难以更新，同时限制它们的泛化。在这篇工作中，我们系统性地研究Transformer是否可以获得隐式推理的能力。我们的一系列实验和对于模型内部的分析揭示了Grokking对于获得隐式推理能力的重要性，其背后的过程和原因，以及Transformer模型对于不同任务的系统性泛化能力的差异。最后，为了展示参数知识表示在复杂推理中的功能和潜力，我们设计了一个具有巨大搜索空间的推理任务，同时发现
如果基于非参数知识表示，无论提示风格或检索增强，即使目前最强的语言模型（例如GPT-4-Turbo和Gemini-1.5-Pro）都无法取得好的效果，
一个Grokking完全的Transformer可以实现接近完美的推理准确性。

### 入群

欢迎加入NICE每周分享交流群，可与NICEer唠嗑，以及第一时间收到后续NICE分享报告的通知。加群通过小助手认证，群内无广告。

<div align=center>
<img src="../images/nice_41_qr.png" width = "200">
<p>备注【昵称-单位-方向-NICE入群】</p>
</div>
