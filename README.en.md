# Universal Resume Assistant Skill

[中文](README.md)

## Features

- Supports resumes and CVs for any profession, industry, seniority, or career transition.
- Audits existing resumes by separating facts, responsibilities, actions, outcomes, metrics, and evidence sources.
- Maps job requirements to `strong`, `partial`, `missing`, or `irrelevant` evidence without keyword laundering or fabricated experience.
- Co-authors, condenses, restructures, and translates content from verified or user-confirmed facts.
- Separates individual contribution from team results and checks dates, seniority, credentials, metric definitions, and causal claims.
- Synchronizes content and release checks across Markdown, DOCX, HTML, PDF, and other requested formats.
- Minimizes personal data by default; public files exclude contact details, real-person examples, secrets, internal identifiers, and confidential data.
- Includes a local privacy scanner for likely emails, phone numbers, absolute home paths, private keys, and common secret fields.

## Method

The skill uses a traceable evidence chain:

`evidence -> target -> selection -> writing -> verification -> delivery`

| Principle | Implementation |
|---|---|
| Facts first | Classify claims as `verified`, `user-confirmed`, `inferred`, `missing`, or `contradictory` |
| Role relevance | Map requirements to evidence and rank by relevance, evidence strength, distinctiveness, and recency |
| Profession neutral | Use different evidence lenses for operations, sales, education, healthcare, technology, research, creative work, public service, skilled trades, and more |
| Accurate attribution | Separate personal responsibility, team outcomes, organizational impact, and causality |
| Interview defensibility | Require important claims to have explainable scope, method, result, and support |
| Fair review | Do not infer ability or integrity from names, photos, age, address, school prestige, family status, or other protected traits and proxies |
| Privacy by default | Minimize and anonymize data, check re-identification risk, inspect archive manifests, and scan before release |
| Consistent delivery | Maintain one factual source and verify content, links, selectable text, reading order, and hidden metadata across formats |

## Installation

Copy `skill/universal-resume-assistant` into the Codex skills directory:

```bash
cp -R skill/universal-resume-assistant "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Restart or refresh Codex so it can discover the skill.

## Usage

```text
Use $universal-resume-assistant to audit this resume, list evidence gaps and privacy risks, and then produce a revision.
```

```text
Use $universal-resume-assistant to tailor my experience to this job description without adding unverified experience.
```

```text
Use $universal-resume-assistant to create Chinese and English versions and verify that facts, seniority, and metrics remain identical.
```

## Structure

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

## Validation

Validate the skill structure:

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py skill/universal-resume-assistant
```

Scan text files before public sharing:

```bash
python3 skill/universal-resume-assistant/scripts/privacy_scan.py path/to/resume-or-folder
```

The scanner supports human review; it is not a compliance, legal, or security certification.

## License

[MIT License](LICENSE)
