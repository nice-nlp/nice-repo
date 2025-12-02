# NICE 75期 | 高效LLM：从训练加速、推理优化，到Agent自主任务

## 主题

高效LLM：从训练加速、推理优化，到Agent自主任务

## 时间

2025.07.20 (周日) 10:00

## 内容

论文列表
- [ACL 2024 Findings] STAR: Constraint LoRA with Dynamic Active Learning for Data-Efficient Fine-Tuning of Large Language Models， https://arxiv.org/pdf/2403.01165
- [COLING 2025] SEED: Accelerating Reasoning Tree Construction via Scheduled Speculative Decoding，https://arxiv.org/pdf/2406.18200
- [ACL 2025] SCOPE: Optimizing Key-Value Cache Compression in Long-context Generation，https://arxiv.org/pdf/2412.13649
- [ACL 2025] WebWalker: Benchmarking LLMs in Web Traversal，https://arxiv.org/pdf/2501.07572
- [ACL 2025] PROPER: A Progressive Learning Framework for Personalized Large Language Models with Group-Level Adaptation，https://arxiv.org/pdf/2503.01303
- WebDancer: Towards Autonomous Information Seeking Agency，https://arxiv.org/pdf/2505.22648

内容介绍
在大语言模型（LLM）能力不断跃升的今天，如何实现真正意义上的“高效智能”，成为当前研究的核心命题。本次分享将围绕“高效”这一关键词，介绍在三个LLM阶段的探索成果：训练、推理与任务执行。 
Part 1 高效训练：面对大模型参数量庞大、标注数据稀缺的挑战，提出结合低秩适配（LoRA）与动态主动学习的 STAR 框架，实现参数与数据双重高效的微调机制；在用户个性化场景下，通过 PROPER 框架引入渐进式个性化学习，提升模型在用户定制场景下的适应能力解决用户级别数据稀疏的问题。 
Part 2 高效推理：为了突破传统自回归生成中速度慢、内存高的瓶颈，我们分别在 KV Cache 压缩和投机两个角度进行推理优化策略：包括利用 SCOPE 框架进行 prefill-decoding 分离的 KV-cache 压缩应对长输出问题，提出 SEED 进行 draft model 的调度提升多路径推理的调度效率应对多路输出问题。 
Part 3 高效任务执行：训练与推理的高效只是基础，目标是让模型真正走向高效执行。用 Agent 来独立完成复杂任务的能力，为模型代替人类高效完成高价值任务奠定了基础。在 Deep Research 场景下， WebWalker 和 WebDancer 两大系统，实现在真实网页环境下的信息获取与任务执行，显著降低人工干预需求，实现真正能够代替人的高效任务执行。 
本次分享将了解如何从“训练-推理-执行”三位一体出发，构建更高效、更实用的大模型智能系统。 

### 入群

欢迎加入NICE每周分享交流群，可与NICEer唠嗑，以及第一时间收到后续NICE分享报告的通知。加群通过小助手认证，群内无广告。

<div align=center>
<img src="../images/nice_41_qr.png" width = "200">
<p>备注【昵称-单位-方向-NICE入群】</p>
</div>
