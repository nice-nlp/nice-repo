# NICE 59期 | Agent进入下一篇章！Alita：不靠人工预设，自己造MCP自我进化的AI

## 主题

Agent进入下一篇章！Alita：不靠人工预设，自己造MCP自我进化的AI

## 时间

2025.6.1 周日 10:30-11:30

## 内容

论文信息
标题：Alita: Generalist Agent Enabling Scalable Agentic Reasoning with Minimal Predefinition and Maximal Self-Evolution 
地址：https://arxiv.org/pdf/2505.20286 
Blog ：https://github.com/CharlesQ9/Alita 

内容介绍
这篇论文提出了一个非常有趣且实用的想法：让 Agent 主动创造用于解决 MCP 的工具，实现自我进化。这些工具既可以是从网上检索的开源工具，也可以是 Agent 借助代码生成能力自主编写的。 
相比之下，传统冲 GAIA 榜单的方法通常是手动构造大量特定 Agent，或者为了实现完全自动化，又堆叠出繁复的 workflow。虽然这些系统可以在榜单上取得好成绩，但在实际应用中效果往往不佳。 
Alita 的做法则更具通用性与实效性：通过试错让 Agent 自主探索并创造工具，持续扩充其工具库，从而将原本依赖多次尝试（pass@k）的任务，转化为一次成功（pass@1）。随着工具的积累和使用，Agent 的能力不断增强，达到“越做越熟练”的效果。 
此外，Alita 还提出了“Agent 蒸馏”的思想：由大模型构建高质量工具，再由小模型调用这些工具。这种方式类似于“用大号装备小号”，不仅提升了小模型的实用能力，也使其在特定领域具备更强的任务完成能力。 
值得一提的是，Alita 在 GAIA 榜单中生成的 MCP 也已被应用于历史版本的 “manus” 中作为历史影像理解模块(论文详见：On Path to Multimodal Historical Reasoning: HistBench and HistAgent（https://arxiv.org/abs/2505.20246）代码已开源)，证明了智能体能力迁移的可能性，相关内容将在下周分享。 

### 入群

欢迎加入NICE每周分享交流群，可与NICEer唠嗑，以及第一时间收到后续NICE分享报告的通知。加群通过小助手认证，群内无广告。

<div align=center>
<img src="../images/nice_41_qr.png" width = "200">
<p>备注【昵称-单位-方向-NICE入群】</p>
</div>
