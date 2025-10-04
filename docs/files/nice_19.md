# NICE19期 | 脆弱的不确定性：大模型的可信度如何被操控

## 主题

脆弱的不确定性：大模型的可信度如何被操控

## 时间

2024.7.27 10:30-11:30 周六

## 内容

论文：Uncertainty is Fragile: Manipulating Uncertainty in Large Language Models 

大纲
1. 介绍uncertainty这个领域和两种常见的衡量方法 entropy计算和conformal prediction
2. 介绍backdoor的作用和一些指标比如asr
3. 如何用backdoor来操控uncertainty
4. 实验
5. 总结

引言
这项研究探讨了大型语言模型（LLMs）在不确定性估计方面的脆弱性，展示了攻击者如何在不改变实际输出的情况下操纵模型对其预测的信心。通过后门攻击实现这一点，该攻击根据特定触发器修改模型的输出概率分布，使其与攻击者预设的分布一致，同时保持顶级预测不变。研究发现在不同模型和触发策略中达到了100%的攻击成功率。这突出了LLM可靠性面临的重大威胁，并强调了针对此类攻击需要防御机制的必要性。 

### 入群

欢迎加入NICE每周分享交流群，可与NICEer唠嗑，以及第一时间收到后续NICE分享报告的通知。加群通过小助手认证，群内无广告。

<div align=center>
<img src="../images/nice_41_qr.png" width = "200">
<p>备注【昵称-单位-方向-NICE入群】</p>
</div>
