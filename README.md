# AI Resume Assistant（简历证据助手）

一款把真实经历整理成经得起追问的中英文简历的 Codex Skill。它不是"把句子写漂亮"的工具，而是先分清事实、推断与缺口，再判断你与目标岗位的匹配，最后才动笔改简历。全程不编造经历、指标和结论。

## 它能做什么

- **简历审计**：把简历拆成事实、职责、行动、结果、指标与证据来源，标出可直接使用、需要确认和互相矛盾的内容。
- **JD 匹配**：将职位要求逐条映射到真实经历（强匹配 / 部分匹配 / 缺失 / 无关），不靠关键词堆砌，也不补写没做过的事。
- **能力画像与证据梳理**：把 AI 产品经理等岗位的 JD 拆成能力层（模型与 AI 系统、Agent 机制、数据与评测、产品闭环、跨职能协作、业务落地、持续学习），逐层核对证据，并区分"现在可写进简历 / 进行中 / 未来目标"。
- **进行中项目与未来目标管理**：进行中的工作可以讲，但不能写成已完成的结果；未来目标不进简历。Benchmark 未冻结前不写方向性结论。
- **运营 / 内容经历的产品化表达**：不靠改头衔，而是把重复劳动、流程改进和结果整理成可迁移的产品证据。
- **招聘信息合规与风险识别**：把岗位匹配与招聘主体可信度、劳动用工、诈骗信号、个人信息风险分开判断，给出核查清单而非武断结论。
- **单页 A4 排版**：内容控制在 1 张 A4；溢出先压缩措辞和间距再降字号，内容不足一页放宽行距字距，不填凑数内容。
- **多格式交付**：Markdown / 纯文本 / HTML / PDF 内容一致，检查链接、页数、可选中文字、打印配色与阅读顺序。

## 安装

```bash
cp -R skill/ai-resume-assistant "${CODEX_HOME:-$HOME/.codex}/skills/"
```

重启或刷新 Codex 后即可发现该 skill。

## 使用

```text
使用 $ai-resume-assistant 审计这份简历，先列出证据缺口和隐私风险，再给出修改稿。
```

```text
使用 $ai-resume-assistant 将我的经历匹配这份职位描述，不要补写未证实的经验。
```

```text
使用 $ai-resume-assistant 评估这份岗位的匹配度、招聘主体可信度、劳动用工和个人信息风险，并告诉我投递前需要核实什么。
```

```text
使用 $ai-resume-assistant 生成中英文版本，并校验两种语言的事实、职级和指标完全一致。
```

```text
使用 $ai-resume-assistant 检查这个 AI 项目是 Demo、早期产品还是完整产品闭环，并告诉我下一步应积累什么证据。
```

```text
使用 $ai-resume-assistant 对比这份公开简历与我的情况，分开评估文档质量、候选人信号和岗位匹配。
```

## 结构

```text
skill/ai-resume-assistant/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── anti-patterns.md
│   ├── asset-management.md
│   ├── capability-portrait-evidence-mapping.md
│   ├── commercial-product-thinking.md
│   ├── delivery-checklist.md
│   ├── job-legitimacy-and-labor-risk.md
│   ├── market-signals-and-benchmarking.md
│   ├── operational-work-to-product-evidence.md
│   ├── product-clarity-gate.md
│   ├── product-evidence-accumulation.md
│   ├── project-narrative.md
│   ├── quality-rubric.md
│   ├── reconstruction-and-voice.md
│   └── writing-patterns.md
└── scripts/
    └── resume_inventory.py
```

## 验证

校验 skill 结构：

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py skill/ai-resume-assistant
```

盘点简历源文件与生成产物：

```bash
python3 skill/ai-resume-assistant/scripts/resume_inventory.py
```

## 许可

[MIT License](LICENSE)
