# NICE 22期 | 无矩阵乘法LLM - 一个来自线性Transformer的视角

## 主题

无矩阵乘法LLM - 一个来自线性Transformer的视角

## 时间

2024.8.17 10:30-11:30am 周六

## 内容

论文：Scalable MatMul-free Language Modeling
链接：https://arxiv.org/pdf/2406.02528

内容大纲
   1. 背景：
       - 无乘法网络
       - 线性注意力机制
   2. 无乘法语言模型组件介绍
       - 线性无乘法token mixer
       - 三值化channel mixer与fused结构
   3. 深入分析无乘法token mixer
   4. 实验
      1. Downstream benchmark
      2. Fused BitNet 的速度

引言
矩阵乘法(MatMul)通常是大型语言模型(LLMs)中计算成本最高的部分。随着LLMs的嵌入维度和上下文长度不断扩大,这一成本也在增加。本研究表明,我们可以完全消除LLMs中的MatMul运算,同时在数十亿参数规模上保持强大的性能。
我们的实验显示,所提出的无MatMul模型在至少27亿参数的规模上,其性能可以与需要更多推理内存的最先进Transformer模型相媲美。我们研究了扩展规律,发现随着模型规模增大,我们的无MatMul模型与全精度Transformer之间的性能差距在缩小。
我们还提供了这种模型的GPU高效实现,在训练过程中将内存使用减少了61%。通过在推理时使用优化的内核,我们模型的内存消耗可以比未优化的模型减少10倍以上。
为了准确量化我们架构的效率,我们在FPGA上构建了一个定制硬件解决方案,它能够利用GPU无法实现的轻量级操作。我们以13W的功耗处理了十亿参数级的模型,处理速度超过了人类可读的速度,使LLMs更接近于人脑的效率。

### 入群

欢迎加入NICE每周分享交流群，可与NICEer唠嗑，以及第一时间收到后续NICE分享报告的通知。加群通过小助手认证，群内无广告。

<div align=center>
<img src="../images/nice_41_qr.png" width = "200">
<p>备注【昵称-单位-方向-NICE入群】</p>
</div>
