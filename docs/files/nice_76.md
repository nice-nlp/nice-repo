# NICE 76期 | LLM Agent的“Windows”来了！AIOS如何构建LLM Agent的生态底座？

## 主题

LLM Agent的“Windows”来了！AIOS如何构建LLM Agent的生态底座？

## 时间

2025.07.26 (周六) 10:00

## 内容

论文列表
- [COLM 2025] AIOS: LLM Agent Operating System，https://arxiv.org/pdf/2403.16971
- OmniRouter: Budget and Performance Controllable Multi-LLM Routing，https://arxiv.org/abs/2502.20576

内容介绍 
核心架构：针对大规模 LLM Agent 部署和管理面临的资源冲突、调度低效和系统协调复杂等挑战，我们提出了 AIOS 架构。该架构的核心动机是将资源调用与 Agent 应用逻辑解耦，通过设计专用的 AIOS 内核来统一抽象和管理 Agent 所需的系统资源。AIOS 内核提供调度、上下文管理、记忆管理、文件访问管理等核心服务，实现了多Agent环境下的高效资源管理和分配。 
多核 LLM 请求调度：为了提升 AIOS 的服务效率和吞吐量，我们将其扩展为多核 LLM 架构。在多请求路由场景下，现有框架通常采用局部最优策略，为每个查询单独选择最佳模型，忽略全局预算约束，导致资源分配低效。为此，我们提出 OmniRouter，将路由问题重新建模为约束优化任务。通过混合检索增强预测器预测 LLM 能力和成本，OmniRouter 在满足性能要求的同时最小化总成本进行全局最优调度。 
上下文化系统软件：为了在 AIOS 架构上为 agent 提供更便捷的 computer-use 服务，我们识别出关键挑战在于 agent 环境的自然语言上下文化。基于此，我们对 AIOS 基础架构进行了优化：利用 MCP 协议和虚拟化技术，将计算机软件操作环境抽象为 LLM 可直接理解的上下文环境。通过这种架构优化，我们发现，即使是简单的 computer-use agent 设计也能获得显著的能力提升。

### 入群

欢迎加入NICE每周分享交流群，可与NICEer唠嗑，以及第一时间收到后续NICE分享报告的通知。加群通过小助手认证，群内无广告。

<div align=center>
<img src="../images/nice_41_qr.png" width = "200">
<p>备注【昵称-单位-方向-NICE入群】</p>
</div>
