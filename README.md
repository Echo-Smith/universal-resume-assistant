# Universal Resume Assistant Skill

[English](README.en.md)

## 功能

- 适配任意职业、行业、资历阶段与转型路径的简历或 CV。
- 审计现有简历，拆分事实、职责、行动、结果、指标与证据来源。
- 将职位要求映射为 `强匹配 / 部分匹配 / 缺失 / 无关`，避免关键词拼接和经历虚构。
- 基于已验证或用户确认的事实协作撰写、压缩、重组和翻译内容。
- 区分个人贡献与团队成果，校验日期、职级、证书、指标口径与因果关系。
- 支持 Markdown、DOCX、HTML、PDF 等交付格式的内容同步与发布检查。
- 默认执行隐私最小化，公开文件不保留个人联系方式、真实样例、密钥、内部标识和机密数据。
- 提供本地隐私扫描脚本，辅助发现邮箱、电话、绝对用户路径、私钥和常见密钥字段。

## 方法依据

Skill 以可追溯证据链为核心：

`证据 -> 目标 -> 取舍 -> 写作 -> 验证 -> 交付`

| 原则 | 实现方式 |
|---|---|
| 事实优先 | 将主张标记为 `verified`、`user-confirmed`、`inferred`、`missing` 或 `contradictory` |
| 职位相关 | 建立要求与证据映射，按相关性、证据强度、独特性和时效性排序 |
| 职业通用 | 对运营、销售、教育、医疗、技术、研究、创意、公共服务、技工等采用不同证据视角，不套用单一成功模型 |
| 署名准确 | 分离个人职责、团队成果、组织影响和因果归属 |
| 可面试验证 | 每个重要表述都应能说明范围、方法、结果与证据 |
| 公平审查 | 不依据姓名、照片、年龄、地址、学校声望、家庭状态等推断能力或诚信 |
| 隐私优先 | 数据最小化、匿名化、重识别检查、压缩包清单检查和发布前扫描 |
| 交付一致 | 设定单一事实源，检查多格式内容、链接、可选文本、阅读顺序和隐藏元数据 |

## 安装

将 `skill/universal-resume-assistant` 复制到 Codex skills 目录：

```bash
cp -R skill/universal-resume-assistant "${CODEX_HOME:-$HOME/.codex}/skills/"
```

重启或刷新 Codex 后即可发现该 skill。

## 使用

```text
使用 $universal-resume-assistant 审计这份简历，先列出证据缺口和隐私风险，再给出修改稿。
```

```text
使用 $universal-resume-assistant 将我的经历匹配这份职位描述，不要补写未证实的经验。
```

```text
使用 $universal-resume-assistant 生成中英文版本，并校验两种语言的事实、职级和指标完全一致。
```

## 结构

```text
skill/universal-resume-assistant/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── privacy-and-evidence.md
│   ├── quality-and-delivery.md
│   └── tailoring-and-writing.md
└── scripts/privacy_scan.py
```

## 验证

校验 skill 结构：

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py skill/universal-resume-assistant
```

扫描待公开的文本文件：

```bash
python3 skill/universal-resume-assistant/scripts/privacy_scan.py path/to/resume-or-folder
```

扫描器用于提示人工复核，不代表合规、法律或安全认证。

## 许可

[MIT License](LICENSE)
