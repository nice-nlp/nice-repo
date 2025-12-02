# NICE 34期 | 信任密码：探索LLM文本的长远影响

## 主题

信任密码：探索LLM文本的长远影响

## 时间

2024.11.23 10:30-11:30 周六

## 内容

论文题目：Spiral of Silence: How is Large Language Model Killing Information Retrieval?—A Case Study on Open Domain Question Answering
论文链接：https://aclanthology.org/2024.acl-long.798.pdf
项目主页：https://github.com/VerdureChen/SOS-Retrieval-Loop
相关工作列表：
1. Neural Retrievers are Biased Towards LLM-Generated content
2. Blinded by Generated Contexts: How Language Models Merge Generated and Retrieved Contexts When Knowledge Conflicts?
3. PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models
4. Homogenization Effects of Large Language Models on Human Creative Ideation
5. Generative Echo Chamber? Effect of LLM-Powered Search Systems on Diverse Information Seeking

引言
我们正身处一个算法驱动文本生成的新纪元，其中大语言模型（LLMs）的广泛应用不仅提升了内容创作的效率，也增加了虚假信息制造的简易性。随着大语言模型生成的文本数量的增加和被搜索引擎的索引，这些文本对检索增强生成（RAG）系统的影响也将开始显现，对未来信息生态的健康发展可能构成隐性挑战。
我们构建并迭代运行了一个模拟LLM生成文本不断涌入网络数据集的管道，并通过迭代运行评估其对RAG系统性能的影响。研究表明，LLM生成文本在短期内通常会改善检索效果，但从长期来看，将引起检索效果显著下降，而生成性能则保持稳定。进一步分析发现，信息检索（IR）系统对LLM生成文本存在偏好，导致其在搜索结果中持续排名靠前，进而使人类创作内容的可见性和影响力下降，形成了一种数字“沉默螺旋”效应。
这一效应揭示了LLM生成文本对信息生态系统的潜在负面影响：尽管短期内提供了更有效的检索体验，但长期来看可能导致人类创作内容的隐形、搜索结果的同质化以及某些准确信息的难以获取，从而对公共知识获取和决策产生不利影响。本报告也将对其他探究LLM生成内容影响的工作进行简要介绍。
分享内容大纲
- Neural IR中的来源偏差 
  - RAG中的“沉默螺旋” 
  - 怎样构造合理的环境来模拟LLM生成文本涌入互联网 
  - LLM生成文本对RAG系统的短期影响 
  - 短期影响是否能递推到长期 
  - 量化解释现象 
  - 其他因素探究 
- 其他相关工作简介

### 入群

欢迎加入NICE每周分享交流群，可与NICEer唠嗑，以及第一时间收到后续NICE分享报告的通知。加群通过小助手认证，群内无广告。

<div align=center>
<img src="../images/nice_41_qr.png" width = "200">
<p>备注【昵称-单位-方向-NICE入群】</p>
</div>
