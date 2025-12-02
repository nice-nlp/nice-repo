# NICE 27期 | 基于离散表示统一多模态理解与生成：把一种新模态当作一门外语

## 主题

基于离散表示统一多模态理解与生成：把一种新模态当作一门外语

## 时间

2024.9.14 20:00-21:00 周六

## 内容

论文：AnyGPT: Unified Multimodal LLM with Discrete Sequence Modeling
地址：https://arxiv.org/pdf/2402.12226 

大纲
1. 首个统一多模态理解与生成的模型SpeechGPT：使大语言模型具有内生的语音对话能力
2. 如何获得更适合语言模型建模的语音表示？SpeechTokenizer：语音语义信息和副语言学信息的解耦
3. 基于离散表示的Any-to-Any多模态模型AnyGPT：基于离散表示统一文本、图像、语音、音乐四种模态
4. 类GPT-4o模型 SpeechGPT2：如何基于语言模型，对多模态信息进行完整的建模

引言
大语言模型（LLM）通过Decoder Only Transformer的架构和Next Token Prediction任务，在海量文本数据上进行训练，不仅学会了各种NLP任务，并涌现出In Context Learning、Chain-of-Thought等新能力。然而，有人预测互联网上的高质量文本数据将在未来几年内用尽，而现有的LLM仍未达到我们对通用人工智能（AGI）的展望。互联网不仅包含文本，还涵盖了图像、音视频等多种模态的数据，这引出了一个问题：我们如何统一高效地训练这些多模态数据？
AnyGPT提出了一种生成式训练方案，将所有模态的数据转换为统一的离散表示，采用Next Token Prediction任务在LLM上统一训练。从压缩即智能的角度出发：当Tokenizer的质量足够高，LLM的困惑度（PPL）足够低，就有可能将互联网的海量多模态数据压缩在同一个模型中，并涌现出纯文本LLM没有的能力。基于原始的GPT结构和多模态离散化表示，AnyGPT统一了文本、语音、图像、音乐四种模态，并实现任意模态组合的相互转换。

### 入群

欢迎加入NICE每周分享交流群，可与NICEer唠嗑，以及第一时间收到后续NICE分享报告的通知。加群通过小助手认证，群内无广告。

<div align=center>
<img src="../images/nice_41_qr.png" width = "200">
<p>备注【昵称-单位-方向-NICE入群】</p>
</div>
