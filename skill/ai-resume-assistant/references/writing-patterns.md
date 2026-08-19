# Coaching prompts for technical resume writing

Use this reference to draft or revise evidence-backed resume text. Old-resume wording is source material, not automatic final wording. In audit mode, use the prompts to diagnose and ask questions. In co-author mode, use the patterns to draft from verified or user-confirmed facts without inventing missing links.

## Table of contents

- Local-edit protocol
- Project-positioning prompts
- Outcome–action–evidence check
- Achievement prompts
- Metric prompts
- Depth prompts
- Translation and style

## Drafting and local-edit protocol

For local editing, work on one claim at a time:

1. Identify the line's current claim.
2. Identify one missing link: task, need, ownership, mechanism, scope, or result.
3. Ask for that fact if it is not already confirmed.
4. Make the smallest revision that incorporates confirmed evidence.
5. Explain the change and request confirmation.

For full drafting, apply the same checks across the section and vary structure according to the evidence. Do not replace the user's voice with a standard formula or add an achievement merely because a line looks short. Read [reconstruction-and-voice.md](reconstruction-and-voice.md) when the text follows the old framework or sounds mechanically generated.

## Project-positioning prompts

Ask:

- Who uses the project?
- What concrete task or decision does it support?
- What was inadequate before?
- What source, workflow, or constraint makes it non-trivial?
- Why is this an application, infrastructure, or algorithm project?

Offer only this empty scaffold when needed:

`[user/task] + [unmet need] + [key constraint] + [solution category]`

Fail the opening if it only names `Multi-Agent`, `RAG`, `platform`, or `framework`. Read [project-narrative.md](project-narrative.md) for architecture-heavy work.

## Outcome–action–evidence check

Use `Accomplished X by doing Y, demonstrated by Z` as an evidence-completeness check when a result is mature enough:

- **X — outcome:** the highest defensible change, completed capability, or safeguarded behavior at the project's actual maturity;
- **Y — action:** the candidate's bounded decision, intervention, or mechanism that plausibly contributed to X;
- **Z — evidence:** an observed behavior, release record, artifact, evaluation, defined metric, publication, adoption, or other proof that directly supports X.

Do not turn this into a universal sentence order. Product and AI-project narratives still need the user, task, or observed failure before the mechanism becomes meaningful. Distribute the chain across a project opening and supporting bullets when that reads more naturally.

Calibrate X to the evidence:

| Project state | Defensible X | Typical Y | Useful Z |
|---|---|---|---|
| Shipped product or operation | user, business, or operating outcome | product decision, workflow change, or coordinated delivery | task completion, repeat use, release/adoption record, defined metric, or documented feedback |
| Early prototype | completed capability or validated task path | scoped build, interaction choice, or technical decision | end-to-end test, demo, sample result, or working artifact |
| Safety or reliability work | defined risky behavior routed, contained, recovered, or prevented | rule, gate, fallback, rollback, or human escalation | bounded test set, incident record, coverage result, or recovery evidence |
| Research or evaluation | finding, decision, or evaluation capability produced | method, rubric, sampling, or analysis | corpus/sample conditions, reproducible artifact, review, or publication |
| Team or operational contribution | shared delivery or service result | the candidate's attributed coordination or execution | accepted deliverable, operating record, stakeholder confirmation, or measured service result |

Guardrails:

- Raw user counts, API calls, lines of code, tool counts, or sample volume are scope evidence, not automatic proof of usefulness.
- A technology name is not Y unless the draft explains the failure, constraint, or decision it addressed.
- Do not attribute a team or downstream result wholly to one person without evidence of ownership and causality.
- If X, Y, or Z is missing, ask for the fact or downgrade the claim instead of filling the gap with rhetoric.
- Vary sentence structure. A responsibility line, direct result, or tradeoff may be clearer than a compressed XYZ sentence.

Examples are diagnostic only:

- Mature product: `Enabled a defined user group to complete [task] by introducing [decision/mechanism], demonstrated by [repeat behavior or outcome within a stated cohort and window].`
- Early prototype: `Delivered an end-to-end [task path] by combining [interaction or mechanism] with [human confirmation], demonstrated by successful completion in tested samples.`
- Safety strategy: `Implemented a separate response path for defined high-risk inputs through [gate/escalation], demonstrated by results on a bounded safety test set.`

## Achievement prompts

### Application or Agent work

Ask which user failure or workflow problem led to the routing, retrieval, tool, fallback, memory, or evaluation decision. Ask how task completion was validated.

Use only this schematic:

`need/observed failure → personal decision → mechanism → validation`

### Architecture or platform work

Ask what runtime, state, scheduling, consistency, recovery, deployment, or adoption bottleneck existed. Ask what alternative was considered and why the final boundary fit.

Use only this schematic:

`platform bottleneck → ownership boundary → tradeoff → mechanism → operating result`

### Performance work

Ask for workload, hardware/model, bottleneck evidence, intervention, before/after conditions, and quality guardrail.

Use only this schematic:

`conditions + bottleneck → intervention → comparable measurement + guardrail`

### Reliability and operations

Ask for the concrete failure mode, detection method, recovery or prevention mechanism, affected scope, and resulting incident or recovery metric.

### Developer productivity

Ask which repeated manual steps or integration delays existed, what was standardized or automated, who adopted it, and how lead time changed.

### Open-source or cross-team influence

Ask which contribution was personal, what was accepted or adopted, and which public artifact supports it. Keep code volume, PR count, rankings, awards, and stars as scope evidence rather than automatic impact.

## Metric prompts

For every user-provided number, ask:

1. What exactly was measured?
2. What was the usable baseline?
3. Were before and after measured under comparable conditions?
4. What hardware, traffic, model, dataset, sample, or window applied?
5. Was it an individual, team, or organization result?
6. What quality or correctness guardrail was preserved?

When no defensible number exists, help the user identify rollout scope, eliminated failure mode, adoption, release, or validated behavior. Do not invent a placeholder value.

## Depth prompts

Across a major project, seek several of these layers without forcing all into one bullet:

- user or business task;
- problem constraint;
- component personally owned;
- design choice and rejected alternative;
- implementation mechanism;
- scale or operating condition;
- validation method;
- result and guardrail.

If the user's text only lists technologies, ask which actual decision or failure each important technology addressed.

## Translation and style

- Translate only approved text or text drafted from verified and user-confirmed evidence.
- Preserve ownership qualifiers, metric conditions, and uncertainty.
- Use past tense for completed work and present tense for ongoing work.
- Prefer precise verbs over inflated labels.
- Keep conventional technology names unchanged.
- Do not expand terse source text into achievements the user did not write and confirm.
