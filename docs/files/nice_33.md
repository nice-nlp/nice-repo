# NICE 33期 | 大语言模型编辑中的崩溃研究

## 主题

大语言模型编辑中的崩溃研究

## 时间

2024.11.17 10:30-11:30 周日

## 内容

论文1：The Butterfly Effect of Model Editing: Few Edits Can Trigger Large Language Models Collapse
链接：https://aclanthology.org/2024.findings-acl.322.pdf
论文2：The Fall of ROME: Understanding the Collapse of LLMs in Model Editing
链接：https://aclanthology.org/2024.findings-emnlp.236.pdf
代码：https://github.com/WLYangICT/Collapse-in-Model-Editing
项目主页：https://yangwl.site/collapse-in-model-editing

引言
模型编辑（Model Editing）技术在修正大语言模型的知识中展现出极大的潜力。然而，现有工作却忽视了它对语言模型固有能力的影响。我们深入研究了这一问题，并产出了两篇论文。第一篇论文揭示了少量编辑即可能导致语言模型崩溃的现象，并提出采用困惑度（Perplexity）作为诊断工具。该工作已被ACL2024 Findings收录。第二篇论文探讨了由最先进的编辑方法ROME触发的语言模型崩溃的根本原因，并提出了一个简单有效的解决方案。该工作已被EMNLP2024 Findings收录。

分享内容大纲
- 少量编辑即可导致大语言模型崩溃
   - 模型编辑副作用初探
   - 困惑度作为代理指标
   - 单次编辑导致模型崩溃
   - 连续编辑导致模型崩溃
   - HardEdit，更具挑战的编辑数据集
- 编辑导致模型崩溃的原因探索
   - ROME简介
   - ROME导致模型崩溃原因分析
   - C-ROME，简单有效地避免模型崩溃

### 入群

欢迎加入NICE每周分享交流群，可与NICEer唠嗑，以及第一时间收到后续NICE分享报告的通知。加群通过小助手认证，群内无广告。

<div align=center>
<img src="../images/nice_41_qr.png" width = "200">
<p>备注【昵称-单位-方向-NICE入群】</p>
</div>
