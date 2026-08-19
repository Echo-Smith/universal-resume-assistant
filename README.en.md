# AI Resume Assistant

A Codex skill that turns real, verified experience into Chinese or English resumes that survive interview follow-up. It is not a sentence-polisher: it separates facts, inference, and missing proof, judges fit against the target role, and only then rewrites the resume. It never fabricates experience, metrics, or conclusions.

## What it does

- **Resume audit**: decomposes a resume into facts, responsibilities, actions, outcomes, metrics, and evidence sources, and flags what is usable, unconfirmed, or contradictory.
- **JD matching**: maps each requirement to real evidence (`strong` / `partial` / `missing` / `irrelevant`) without keyword laundering or invented experience.
- **Capability portrait and evidence mapping**: decomposes role JDs such as AI product manager into capability layers (model/AI systems, agent mechanics, data and evaluation, product loop, collaboration, business scenarios, continuous learning), checks evidence per layer, and separates what can be written now, what is in progress, and what remains a future goal.
- **In-progress work and future-goal management**: work still in progress may be discussed but never written as a completed result; future goals stay out of the resume. Directional benchmark results are not written before the benchmark is frozen.
- **Productizing operations/content experience**: turns repeated labor, process improvement, and observable outcomes into transferable product evidence without title laundering.
- **Job legitimacy and risk screening**: keeps role fit separate from employer credibility, labor compliance, fraud signals, and personal-data risk, and gives a bounded verification checklist rather than unsupported verdicts.
- **One-page A4 layout**: targets exactly one A4 page; compresses wording, hierarchy, and spacing before reducing type size, and widens line/letter spacing instead of adding filler when the page is short.
- **Multi-format delivery**: keeps Markdown, plain text, HTML, and PDF consistent, and verifies links, page count, selectable text, print colors, and reading order.

## Installation

```bash
cp -R skill/ai-resume-assistant "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Restart or refresh Codex to discover the skill.

## Usage

```text
Use $ai-resume-assistant to audit this resume, list evidence gaps and privacy risks, and then produce a revision.
```

```text
Use $ai-resume-assistant to tailor my experience to this job description without adding unverified experience.
```

```text
Use $ai-resume-assistant to assess this role's fit, recruiter credibility, labor terms, and personal-data risks before I apply.
```

```text
Use $ai-resume-assistant to create Chinese and English versions and verify that facts, seniority, and metrics remain identical.
```

```text
Use $ai-resume-assistant to determine whether this AI project is a demo, early product, or validated product loop, then identify the next evidence to collect.
```

```text
Use $ai-resume-assistant to compare this public resume with my profile, separating document quality, candidate signals, and role fit.
```

## Structure

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

## Validation

Validate the skill structure:

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py skill/ai-resume-assistant
```

Inventory resume sources and generated outputs:

```bash
python3 skill/ai-resume-assistant/scripts/resume_inventory.py
```

## License

[MIT License](LICENSE)
