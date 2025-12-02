# NICE 25期 | OpenRLHF：大规模分布式RLHF训练系统介绍

## 主题

OpenRLHF：大规模分布式RLHF训练系统介绍

## 时间

2024.9.1 10:30-11:30 周日

## 内容

大纲
1. RLHF背景知识
2. RLHF性能分析
3. 基于DeepSpeed的TRLX/TRL/LMF
4. 基于Megatron的RLHF
5. 基于Ray和vLLM的OpenRLHF
6. RLHF调参细节优化

引言
随着大规模语言模型（LLMs）通过扩展定律不断增长，基于人类反馈的强化学习（RLHF）因其卓越的性能而受到广泛关注。然而，与单一模型的预训练或微调不同，将基于人类反馈的强化学习（RLHF）扩展到训练大型语言模型时，会在协调四个模型的过程中面临挑战。我们推出了OpenRLHF，一个支持70B以上模型的大规模RLHF训练的开源框架。与现有的将四个模型切分后放在相同GPU上的TRLX/TRL/LMF等框架不同，OpenRLHF重新设计了模型调度方案，利用Ray、vLLM和DeepSpeed优化资源利用率和训练性能。和基于Megatron-LM的RLHF方案相比，OpenRLHF可以无缝集成Hugging Face models和datasets，确保了用户友好性和代码的简洁性和易修改性，提供了开箱即用的解决方案。

项目：https://github.com/OpenRLHF/OpenRLHF

### 入群

欢迎加入NICE每周分享交流群，可与NICEer唠嗑，以及第一时间收到后续NICE分享报告的通知。加群通过小助手认证，群内无广告。

<div align=center>
<img src="../images/nice_41_qr.png" width = "200">
<p>备注【昵称-单位-方向-NICE入群】</p>
</div>
