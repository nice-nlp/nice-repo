# NICE 44期 | 迈向多语言与多任务的医疗大模型：探索医疗语境中的语言基座模型

## 主题

迈向多语言与多任务的医疗大模型：探索医疗语境中的语言基座模型

## 时间

2025.1.18 20:00-21:00

## 内容

论文1: Towards building multilingual language model for medicine （Nature Communication）
链接：https://www.nature.com/articles/s41467-024-52417-z
Github: https://github.com/MAGIC-AI4Med/MMedLM
论文2: Towards Evaluating and Building Versatile Large Language Models for Medicine （NPJ Digital Medcine(accepted) ）
链接：https://arxiv.org/abs/2408.12547
Github: https://github.com/MAGIC-AI4Med/MedS-Ins 

引言
在医疗领域，大语言模型已取得广泛研究进展。然而，这些成果主要依赖于英语基础模型，并受到多语言医疗专业数据匮乏的限制，导致当前的医疗大模型在处理非英语问题时效果不佳。为了解决这一问题，我们首先创建了一个包含25.5亿个tokens的多语言医疗语料库——MMedC。为了更好地评估模型在医疗领域的多语言能力，我们开发了一个全新的多语言医疗问答评测标准——MMedBench，涵盖了6种语言和21个医学子领域。在此基础上，我们推出了全新的医疗基础模型——MMed-Llama 3，在多项基准测试中超越了现有的开源模型，特别适合通过医学指令微调，灵活适应各种医学场景。
此外，现有的医学语言模型评价标准的单一，集中于医学考试选择题，而模型微调的数据则多为日常对话和多选题，未能充分反映大语言模型在真实临床情境中的应用。为此，我们构建了全面的医学指令微调数据集——MedS-Ins。该数据集整合了来自医学考试、临床文本、学术论文、医学知识库及日常对话的58个生物医学数据集，包含超过1350万个样本，覆盖122个临床任务。基于这一数据集，我们对医疗基础模型进行了指令微调，结果表明，该模型在多个临床任务中的表现超越了现有的领先闭源模型，如GPT-4和Claude-3.5。

大纲
1. 背景：
   - 医疗大语言模型的训练范式
   - 医学语言模型上常用的评测基准
2. MMedLM系列多语言基座模型
   - 问题与动机
   - 训练语料收集和评测基准构建
   - 实验结果与分析
3. 迈向多任务的指令微调
   - 问题与动机
   - 任务定义与数据收集
   - 实验结果与分析
4. 总结与未来规划

### 入群

欢迎加入NICE每周分享交流群，可与NICEer唠嗑，以及第一时间收到后续NICE分享报告的通知。加群通过小助手认证，群内无广告。

<div align=center>
<img src="../images/nice_41_qr.png" width = "200">
<p>备注【昵称-单位-方向-NICE入群】</p>
</div>
