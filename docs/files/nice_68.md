# NICE 68期 | Agent论文分享@ICML&ACL2025

## 主题

Agent论文分享@ICML&ACL2025

## 时间

第二场：2025.06.14 (周六) 15:00

## 内容

论文：Agentic Knowledgeable Self-awareness [ACL 2025]

KnowSelf 聚焦于大模型智能体在决策过程中所面临的「知识边界感知」问题。受人类决策机制启发，本文指出智能体应具备三类行为模式的自主决策能力：快速反应（快思考）、深度推理（慢思考），以及主动调用外部工具（本文以外部知识增强为例）。KnowSelf 通过学习自身的知识边界，使智能体能在不同情境下自主判断是否具备足够知识进行生成和推理，以减少无效试错与知识滥用。实验表明，KnowSelf 可提升智能体的知识调用准确率、任务规划效率和跨任务泛化能力。 

论文：OS-Genesis: Automating GUI Agent Trajectory Construction via Reverse Task Synthesis [ACL 2025]

随着VLM的快速发展，构建能够理解多模态信息并自主操作数字界面的 GUI Agents 正逐渐成为现实。然而，训练这类Agents的最大瓶颈在于高质量轨迹数据的缺乏。为克服这一挑战，本文提出 OS-Genesis，一种面向 GUI Agent 的交互驱动式轨迹合成方法。该方法从环境交互出发，自动构建结构完整、语义明确且多样性丰富的任务轨迹。本文进一步设计了用于提升规划与执行能力的双重训练目标，并引入轨迹奖励模型以挖掘高阶任务中的数据价值。在多个具有挑战性的移动端与网页端任务中，OS-Genesis显著提升了GUI Agents的表现，并缩小了合成数据与人工数据之间的质量差距。 

论文：OS-Kairos: Adaptive Interaction for MLLM-Powered GUI Agents [ACL 2025]
论文链接：https://arxiv.org/abs/2503.16465
Code：https://github.com/Wuzheng02/OS-Kairos

由多模态大型语言模型驱动的自主图形用户界面 (GUI) 代理已展现出巨大的潜力。然而，一个关键但尚未得到充分探索的问题依然存在：过度执行，即代理以完全自主的方式执行任务，而没有充分评估其行动信心，从而损害自适应的人机协作。这在复杂场景中会带来巨大风险，例如涉及模糊的用户指令、意外中断和环境劫持的场景。为了解决这个问题，我们提出了 OS-Kairos，这是一个自适应 GUI 代理，能够预测每个交互步骤的信心水平，并有效地决定是自主行动还是寻求人为干预。OS-Kairos 通过两种关键机制开发：(i) 协作探测，在每个交互步骤中注释信心分数；(ii) 信心驱动的交互，利用这些信心分数来引出自适应交互的能力。实验结果表明，OS-Kairos 在我们精心挑选的复杂场景数据集以及 AITZ 和 Meta-GUI 等成熟基准测试中均显著优于现有模型，任务成功率提升了 24.59% 至 87.29%。OS-Kairos 促进了自适应人机协作，优先考虑了真实世界中 GUI 交互的有效性、通用性、可扩展性和效率。 

论文：AnnaAgent: Dynamic Evolution Agent System with Multi-Session Memory for Realistic Seeker Simulation [ACL 2025]

在人工智能驱动的心理健康研究中，由于伦理和成本限制，研究者借助大语言模型构建对话代理（CAs）模拟来访者。然而，现有方法在动态情绪演化与多疗程会话记忆整合方面存在不足。为此，本文提出AnnaAgent，一个具备情绪与认知动态特性的模拟系统，并引入三级记忆机制以提升仿真真实性。AnnaAgent分为两大智能体群组：动态演化组包含情绪调节器、主诉链生成器与主诉切换器，实现情绪波动与主诉演化的动态控制；多疗程记忆组由情境分析器、状态分析器与记忆检索器组成，支持跨疗程的记忆整合。系统还配备说话风格分析、量表总结与事件触发等辅助模块。初始化阶段，系统基于历史数据生成来访者画像、生活事件与心理状态；对话阶段则根据上下文实时调整情绪、检索记忆并控制主诉问题切换。评估结果显示，AnnaAgent在模拟真实来访者行为方面优于现有方法，更接近真实来访者的表现，更具应用潜力。部分代码(含核心架构)已通过伦理审查并公开：https://github.com/sci-m-wang/AnnaAgent。

论文：SMART: Self-Aware Agent for Tool Overuse Mitigation [ACL 2025]
论文提出了一种名为 SMART 的新范式，旨在提升大语言模型驱动智能体的“自我认知”，从而减少其对外部工具的过度依赖。研究发现，目前的模型在任务中有超过 30% 属于“非必要调用工具”情形，即完全可以仅凭自身知识解决 。为此，作者构建了 SMART-ER 数据集，覆盖三个领域，并通过带注释的步骤教学，让模型学会判断何时真正需要工具。最终，SMARTAgent 在动态平衡参数知识和工具使用方面表现优越，实现了更高效、精准的问题处理。 

论文：EscapeBench: Towards Advancing Creative Intelligence of Language Model Agents [ACL 2025]
论文提出了一种全新的评测框架，用“密室逃脱”任务测试大语言模型智能体的创造性与适应能力。传统任务多为目标明确、路径清晰，而EscapeBench强调发散思维、工具活用和环境探索。此外，文章还提出EscapeAgent框架，引入“前瞻+反思”机制，显著提升模型在复杂任务中的完成率与效率。该工作揭示了当前模型在创造性智能方面的不足，也为未来智能体设计提供了新的方向。 

论文：PersonaX: A Recommendation Agent-Oriented User Modeling Framework for Long Behavior Sequence [ACL 2025]

高质量的User Profile能够使Personalized Recommendation Agent 做出更好地符合真实用户兴趣的决策。通常，这类画像依赖大型语言模型（LLM）进行用户画像建模（LLM-UM），但这一流程面临多重挑战：例如上下文长度限制LLM 难以处理长序列用户行为；现有方法常从完整历史行为序列中仅截取片段，遗漏信息导致画像不完整；行为序列选择方法与推理上下文耦合，需在线实时生成，增加推理延迟。为此，本文提出 PersonaX——一种与Agent无关的 LLM-UM 框架克服上述难题，并在下游Sequential Recommendation中显著提升效果与效率。PersonaX 的核心思想为Data-centric 的核心子序列选取(30-50%采样率)来离线生成细粒度的多画像保留用户全谱段多样兴趣. 该建模的User Profile可供在线推理阶段检索直接使用减低延迟。 PersonaX 为LLM-UM设定了新的基准，其能够显著改善Recommendation Agent的在线决策效率与精准性。 


论文：Gödel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement [ACL 2025]

目前所有的Agent自动化设计或者Agent自我提升都会引入极强的规则或人类先验，这极大地限制了Agent的能力上限。为了解决这一问题，我们从Schmidhuber在2003年提出的Gödel Machine中获得启发，设计了完全自指的Agent。它可以根据环境的反馈，完全自由地阅读和修改自己的所有代码（甚至是阅读和修改自己代码的代码）。我们通过递归的形式，允许Agent修改自己的运行内存（Python中的Monkey Patching），从而实现了这一点。由于Agent可以优化自己优化自己的代码，于是经过优化后，Agent的优化能力也会得到优化，于是可以在下一层递归中更好地优化自己。于是，整个过程相当于无限层的Meta Learning。经过我们的实验发现，Gödel Agent 可以自发探索不同算法，提高自己复杂度以及下游任务上的表现，超过了基于人类先验的Agent框架以及Agent自动化设计方法。 

论文：Training Turn-by-Turn Verifiers for Dialogue Tutoring Agents: The Curious Case of LLMs as Your Coding Tutors [ACL 2025]

基于大语言模型 (LLM) 的辅导智能体 (tutoring agents) 在语言学习、科学概念问答等封闭式的知识传递场景已展现潜力，但是，它们在辅导用户解决复杂的开放式 (open-ended) 任务方面的能力如何？鉴于这一方面缺乏研究，我们聚焦编程辅导 (coding tutoring) 这一实际场景，探索智能体能否通过对话来引导学生完成指定的编程任务。智能体需要以目标任务为导向，同时又需要考虑不同学生的知识背景，进而在对话辅导时予以适配和调整。我们提出了一种名为“追踪与验证”（TRAVER）的工作流，它利用知识追踪 (KT) 来实时评估学生的知识掌握情况以实现个性化的对话引导，并训练了一个逐轮验证器 (turn-by-turn verifier)，以有效地推进对学生的辅导。我们还提出了 DICT自动评测协议，它通过模拟不同知识水平的学生，并结合代码生成测试进行客观、可复现的评测，为快速迭代辅导智能体的开发提供了有效工具。实验结果表明，原始的LLM和相关基线方法在解决编程辅导这类任务型辅导中仍有诸多不足， TRAVER 显著提高了辅导成功率，并能更好地适应不同学生。我们希望本工作能为开发帮助用户学习复杂技能的任务辅导智能体 (task-tutoring agents) 提供可行的技术框架与评测思路。 

论文：PersonaX: A Recommendation Agent-Oriented User Modeling Framework for Long Behavior Sequence [ACL 2025]

高质量的User Profile能够使Personalized Recommendation Agent 做出更好地符合真实用户兴趣的决策。通常，这类画像依赖大型语言模型（LLM）进行用户画像建模（LLM-UM），但这一流程面临多重挑战：例如上下文长度限制LLM 难以处理长序列用户行为；现有方法常从完整历史行为序列中仅截取片段，遗漏信息导致画像不完整；行为序列选择方法与推理上下文耦合，需在线实时生成，增加推理延迟。为此，本文提出 PersonaX——一种与Agent无关的 LLM-UM 框架克服上述难题，并在下游Sequential Recommendation中显著提升效果与效率。PersonaX 的核心思想为Data-centric 的核心子序列选取(30-50%采样率)来离线生成细粒度的多画像保留用户全谱段多样兴趣. 该建模的User Profile可供在线推理阶段检索直接使用减低延迟。 PersonaX 为LLM-UM设定了新的基准，其能够显著改善Recommendation Agent的在线决策效率与精准性。 

论文：Towards a Design Guideline for RPA Evaluation: A Survey of Large Language Model-Based Role-Playing Agents [ACL 2025]

近年来，大语言模型已从执行任务的工具演进为能够理解并模拟多样社会行为的智能体，催生了角色扮演代理（RPAs）的兴起。RPAs 能在复杂社会语境中逼真模拟人类行为，现已广泛应用于社会科学、医疗健康、法律等领域。然而，尽管研究活跃，RPA 的评估仍缺乏统一、系统的方法标准，限制了不同系统间的可比性与结果的可复现性。为填补这一空白，我们系统梳理了2021年至2024年间的1,676项相关文献，分析评估实践中的共性方法与关键挑战。我们归纳出六类代理属性、七类任务特征与七项常用评估指标，并据此提出一套结构化评估指南，以提升RPA研究的规范性与可比性。通过两个案例，我们展示了该指南在不同场景下的可操作性与灵活性，验证其在跨学科研究中的适用性。此外，我们调研了43位RPA研究者，发现任务相关性、可复现性与可解释性是他们最优先考虑的评估维度，进一步印证了该框架的设计原则。 

论文：When GPT Spills the Tea: Comprehensive Assessment of Knowledge File Leakage in GPTs [ACL 2025]
论文链接：https://arxiv.org/abs/2506.00197

知识文件 (knowledge files)已广泛应用于大语言模型智能体（如GPTs）中以提升回答质量。然而，关于知识文件泄露的担忧与日俱增。现有研究表明，对抗性提示可诱导智能体泄露知识文件内容。但其他泄露途径是否存在仍属未知——尤其在智能体的部署过程涉及客户端、服务器与数据库的复杂数据流场景下。受数据安全态势管理（DSPM）启发，本文提出了一个创新工作流程以对知识文件泄露风险展开全面评估。通过分析651,022条GPT元数据、11,820条数据流及1,466条对话记录，我们识别出五大泄露途径：元数据、GPT初始化过程、检索机制、沙箱执行环境、提示词。攻击者可借此获取敏感知识文件数据（如标题、内容、类型及大小）。值得注意的是，内置工具"代码解释器"的激活会引发权限提升漏洞，使攻击者能以95.95%的成功率直接下载原始知识文件。深入分析显示，28.80%的泄露文件涉及版权内容，包括来自大型出版商的电子书、某上市公司的内部资料等。最后，我们为GPT开发者与平台提供商提出了可落地的解决方案，以加固智能体数据供应链安全。 

论文：On the Resilience of LLM-Based Multi-Agent Collaboration with Faulty Agents [ICML 2025]

本工作系统性研究大语言模型（LLM）多智能体系统（Multi-Agent System）在遭遇“失误”甚至“恶意”智能体时的韧性与防御。我们首先提出两种自动化扰动方法—AutoTransform（篡改角色指令）与 AutoInject（直接注入错误），可无缝插入任意代理以模拟真实部署中常见的失误/攻击场景。基于四类任务、六种常见结构的实验显示：(1)层级式结构如 A→(B↔C) 最稳健，仅损失 ≈5.5 % 性能，而线性链式结构的性能下滑高达 ≈23.7 %。(2)为进一步提升韧性，我们设计了两道简单但高效的防线：Challenger 机制—赋予每个代理质疑他人输出的权利；额外审计代理 Inspector—复检并纠正信息。两者合并可恢复多达 96.4 % 的错误，显著提升整体准确率。 


论文：SCALE: Towards Collaborative Content Analysis in Social Science with Large Language Model Agents and Human Intervention [ACL 2025]

内容分析将复杂且非结构化的文本分解为基于理论的数字类别。尤其是在社会科学领域，这一过程通常依赖于多轮人工标注、领域专家讨论和基于规则的细化。本文介绍了一个新颖的多智能体框架---SCALE，它能够有效地通过大型语言模型代理模拟内容分析。SCALE 模拟了内容分析的关键阶段，包括文本编码、协作讨论和动态代码本演化，捕捉了人类研究人员的反思深度和自适应讨论。此外，通过整合多种人工干预模式，SCALE 能够通过专家输入得到增强，从而进一步提升其性能。基于真实数据集的广泛评估表明，SCALE 在各种复杂的内容分析任务中均达到了接近人类的性能，为未来的社会科学研究提供了创新潜力。 


论文：ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning [ICML 2025]

本工作提出了ShieldAgent，一种面向通用LLM智能体的可验证安全策略保护方法。当前，由foundation model驱动的智能体广泛应用于现实场景，但仍易受恶意指令和攻击，造成隐私泄露和经济损失等严重后果。现有针对LLM content的guardrail难以迁移到复杂动态的agent上。为此，ShieldAgent通过从safety policy文档中自动提取规则，构建基于动作的概率规则约束模型，对智能体的行为轨迹进行合规性推理和防护。ShieldAgent可根据受保护agent的实时行为自动检索相关规则，并生成防护方案，结合工具库与可执行代码实现形式化验证。此外，我们构建了包含3000组safety-related指令与agent行动轨迹的新基准数据集ShieldAgent-Bench。实验结果显示，ShieldAgent在多个基准上取得了最优表现，并大幅降低API调用与推理时长，兼具高效性与精确性，可有效为通用LLM智能体提供实时保护。 

论文：AgentDropout: Dynamic Agent Elimination for Token-Efficient and High-Performance LLM-Based Multi-Agent Collaboration [ACL 2025]

基于大语言模型（LLMs）的多智能体系统（MAS）在协作解决问题方面已显示出巨大潜力。然而，它们仍然面临着通信效率低和任务绩效不理想的巨大挑战，因此精心设计智能体的通信拓扑结构尤为重要。受高效团队中角色经常动态调整的管理理论启发，我们提出了 AgentDropout，它通过优化通信图的邻接矩阵来识别不同通信回合中的冗余智能体和通信路径，并消除它们以提高令牌效率和任务性能。与最先进的方法相比，AgentDropout 平均减少了 21.6% 的prompt token开销和 18.4% 的conpletion token开销，任务性能提高了 1.14。此外，扩展实验表明，AgentDropout 具有显著的领域可转移性和结构鲁棒性，显示了其可靠性和有效性。 


论文：Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems [ICML 2025]

多智能体系统中，识别导致任务失败的责任Agent及其关键出错步骤对系统调试至关重要，但现有研究主要依赖人工分析，既费时又效率低下。为此，本研究提出“自动化失败归因”（Automated Failure Attribution）作为一项新任务，并构建了首个面向该任务的公开基准数据集——Who&When。该数据集包含来自127个 LLM 多智能体系统的失败日志，并由人工对“谁出错（责任Agent）”与“何时出错（决定性步骤）”进行精细标注。在该基准上，我们设计并评估了三类自动化归因方法：一次性分析（All‑at‑Once）、逐步检查（Step‑by‑Step）及二分定位（Binary Search），详述其优缺点。实验结果表明，最优方法在责任Agent识别上准确率为53.5%，而在关键出错步骤定位仅为14.2%；部分方法表现甚至低于随机。即便是当前最先进的推理模型（如 OpenAI o1、DeepSeek R1），也未能达到实际可用水平，进一步凸显该任务的高挑战性。这些发现揭示了当前自动化归因技术在多智能体协同任务中仍存在显著不足。未来工作需进一步探索更高效、更精确的归因策略，以提升多智能体系统的调试流程与可信度。 

### 入群

欢迎加入NICE每周分享交流群，可与NICEer唠嗑，以及第一时间收到后续NICE分享报告的通知。加群通过小助手认证，群内无广告。

<div align=center>
<img src="../images/nice_41_qr.png" width = "200">
<p>备注【昵称-单位-方向-NICE入群】</p>
</div>
