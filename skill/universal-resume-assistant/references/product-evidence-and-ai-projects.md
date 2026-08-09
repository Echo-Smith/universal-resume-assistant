# Product evidence and AI project guide

Use this reference when a project is still active, the resume lacks outcomes, an AI-built artifact may only be a demo, or a technical project is described mainly through architecture names.

## Contents

- Evidence accumulation
- Outcome ladder
- AI and Vibe Coding completeness check
- Product and architecture narrative
- Product judgment signals
- Bounded evidence plan

## Evidence accumulation

Capture evidence during the work instead of reconstructing a perfect story afterward. Preserve:

- user and workflow;
- trigger evidence and existing workaround;
- problem frequency, severity, cost, or risk;
- options considered and the real reason for the decision;
- first-version scope and non-goals;
- success signal and quality, safety, cost, or control guardrail;
- rollout scope and personal ownership;
- observed result, negative feedback, and bad cases;
- follow-up decision and unresolved uncertainty;
- dated artifacts, notes, logs, screenshots, or links.

Do not invent rejected options, backdate rationale, or create activity solely to manufacture a resume number.

## Outcome ladder

Classify the highest level actually demonstrated:

| Level | Evidence | What it proves | What it does not prove |
|---|---|---|---|
| 1. Feature completed | Prototype, workflow, page, API, or release | Delivery | Demand or value |
| 2. Usage scale | Users, visits, calls, tasks, trials, or exposed accounts | Reach or activity | Repeat value or impact |
| 3. Repeat behavior | Retained use, recurring operation, or workflow adoption | Users returned or adopted a behavior | Improved user outcome |
| 4. User outcome | Time, errors, completion, acceptance, quality, or risk changed | The user's task changed | Business value unless linked |
| 5. Business outcome | Revenue, cost, conversion, retention, capacity, or service load changed | Operating or commercial value | Sole personal causality |

Lead with the highest defensible level. Keep the cohort, window, baseline or final attainment, source, attribution, and guardrail for surprising results.

## AI and Vibe Coding completeness check

Ask seven questions before calling an AI-built artifact a validated product loop:

1. Who performs the task or makes the decision?
2. When and in which workflow does the need arise?
3. How is the task handled now, and why is that inadequate?
4. Why is this worth solving now relative to competing work?
5. Why did the first version include these behaviors and exclude others?
6. Which behavior, outcome, and guardrail would validate the hypothesis?
7. What happened after real use, and what decision changed because of it?

Classify each answer as `complete`, `partial`, `missing`, or `contradictory`.

- Build exists but user and validation are missing: call it a demo or implementation proof.
- User evidence exists but prioritization or scope rationale is missing: call it discovery plus prototype.
- Real use exists but the result or follow-up decision is missing: report early usage and ongoing validation.
- All seven are supported and iteration follows evidence: describe a validated product loop.

Fast implementation, a polished interface, a large model, or a high share of AI-generated code is not product impact by itself.

## Product and architecture narrative

The title and opening should let a reviewer identify:

- the user;
- the concrete task or decision;
- the previous failure or workaround;
- the critical constraint;
- why the selected product or technical form was necessary.

Use the reasoning chain:

`specific need -> observed failure -> decision -> mechanism -> validation`

Do not lead with a component inventory such as Agent, RAG, memory, tools, workflow, or model names. Connect each retained mechanism to a real constraint. A rejected option is useful only when it was actually tried or seriously considered and the tradeoff is concrete.

Use one dominant role lane:

- product or application work: user workflow, task completion, failure handling, evaluation, trust, and iteration;
- infrastructure work: runtime bottleneck, state, scheduling, consistency, recovery, deployment, and adoption;
- algorithm or research work: method contribution, dataset, evaluation, baselines, ablations, and reproducibility.

## Product judgment signals

Show judgment through decisions rather than labels:

- what was deliberately not built;
- where deterministic logic was preferred to a model;
- where human confirmation or manual takeover remained;
- which metric was paired with a guardrail;
- how a bad case changed prompts, memory, routing, workflow, or interaction;
- how failure, rollback, recovery, or uncertainty was handled;
- why one interaction or architecture boundary was chosen over another.

## Bounded evidence plan

Create a short evidence plan only when the user has an active project and access to real users, workflow observations, or operating data.

1. Name one decision-critical uncertainty.
2. Define the hypothesis and the decision it will inform.
3. Select the cohort, task, observation window, evidence source, and owner.
4. Choose one primary signal and one or two guardrails.
5. Capture a fair baseline or report final attainment when no fair baseline exists.
6. Set a review point with `continue`, `change`, `stop`, or `investigate` options.
7. Keep planned evidence separate from completed resume claims.

Do not prescribe interviews, A/B tests, or numerical targets mechanically. Match the method to the decision, risk, and available scale.
