# Product evidence accumulation

Use this reference when the user's project is still active, the resume lacks outcomes, an AI-built artifact may be only a demo, or the user wants to turn real work into future resume and interview evidence.

## Table of contents

- Operating principles
- Product decision ledger
- Outcome ladder
- Vibe Coding completeness check
- Gap-to-action evidence plan
- Output templates

## Operating principles

Accumulate evidence as part of product work, not as a retrospective writing exercise. Preserve what was known at the time of the decision; later success must not rewrite the original uncertainty.

Follow these rules:

- Work from a real user, workflow, or business decision.
- Keep raw evidence separate from interpretation.
- Date decisions, metrics, screenshots, logs, interview notes, and releases.
- Separate the team's result from the user's personal action and influence.
- Record rejected options and non-goals only when they were real.
- Define the metric before reading the result when possible.
- Pair an optimization metric with a quality, safety, cost, or user-control guardrail.
- Treat future experiments and intended metrics as plans, never completed evidence.
- Do not generate activity merely to create a resume number.

## Product decision ledger

Create one record for a material product decision, not one record per feature or meeting. Populate only `verified` and `user-confirmed` fields. Mark the rest `inferred`, `missing`, or `contradictory` using the skill's evidence states.

| Field | What to capture | Credibility check |
|---|---|---|
| Decision date and phase | When the decision was made; discovery, MVP, rollout, or iteration | Do not backdate a later rationale |
| User and workflow | Specific user and the task or decision being performed | Avoid “all users” or a demographic without a job |
| Trigger evidence | Quote, behavior, support ticket, log, workflow observation, or business request | One complaint is a signal, not automatically a segment-wide need |
| Existing workaround | How the user handles the task now | Include manual steps, competing tools, delay, error, or avoidance |
| Problem magnitude | Frequency, severity, affected cohort, time, money, risk, or opportunity | Use qualitative evidence when no honest count exists |
| Why now | Deadline, repeated failure, strategic change, cost, dependency, or learning value | “AI can build it quickly” is not sufficient by itself |
| Opportunity cost | What competing work would be delayed or not done | Record only choices that actually existed |
| Options considered | Plausible alternatives, including process or no-build options | Do not invent a rejected option to create drama |
| Decision and rationale | Selected approach and the constraint that made it appropriate | Link mechanism to the observed need |
| Non-goals | What the version deliberately will not solve | Distinguish deliberate scope from forgotten work |
| First-version hypothesis | Expected user behavior or result if the decision is correct | Make it falsifiable when possible |
| Success metric | Behavior or result used to test the hypothesis | Define denominator, cohort, window, and source |
| Guardrails | Quality, safety, cost, latency, error, trust, or manual-control boundary | Do not optimize speed while hiding quality loss |
| Rollout and ownership | Who built, approved, operated, or used it; environment and scope | Separate individual and team ownership |
| Observed result | What happened during the defined window | Report final attainment if no fair baseline exists |
| Feedback and bad cases | Raw feedback, failure modes, drop-offs, and exceptions | Preserve negative evidence and sample limits |
| Follow-up decision | Continue, change, stop, narrow, expand, or collect more evidence | Tie the next action to observed evidence |
| Proof and uncertainty | Artifact paths, links, screenshots, logs, definitions, and unresolved questions | A resume claim must remain within this boundary |

Do not force every field into the resume. The ledger supports later selection, interview depth, portfolio case studies, and honest omission.

## Outcome ladder

Classify the highest level actually demonstrated. A higher level is stronger only when its definition, attribution, and guardrails are credible.

| Level | Evidence type | What it proves | What it does not prove |
|---|---|---|---|
| 1. Feature completed | A prototype, page, workflow, API, or release exists | Delivery and implementation | Demand, adoption, or value |
| 2. Usage scale | Visitors, users, calls, tasks, trials, or exposed accounts | Reach or activity | Repeat value, quality, or impact |
| 3. Repeat behavior | Repeated use, retained cohort, workflow adoption, or recurring operation | Users returned or incorporated the behavior | The user's task improved |
| 4. User outcome | Time saved, error reduced, task completed, acceptance increased, decision improved, or risk controlled | The user's job or experience changed | Revenue or organizational value unless linked |
| 5. Business outcome | Revenue, cost, conversion, retention, capacity, service load, or organizational efficiency changed | Business or operating value | Sole personal causality without attribution evidence |

Apply these rules:

- Lead with the highest defensible level; use lower levels as scope or supporting context.
- Do not convert users, calls, tasks, traffic, followers, awards, or code volume into user or business impact.
- A qualitative user outcome can be stronger than a large activity count when the evidence and attribution are clearer.
- State the cohort, window, baseline or final attainment, data source, and preserved guardrail for surprising results.
- When results conflict across cohorts, report the segmentation instead of averaging away the failure.
- If the next level is missing, describe the gap as future evidence work, not a resume wording problem.

## Vibe Coding completeness check

Ask seven questions before calling an AI-built artifact a validated product loop:

1. **User:** Who performs the task or makes the decision?
2. **Scenario:** When and in which workflow does the need arise?
3. **Existing solution:** How is the problem handled now, and why is that inadequate?
4. **Priority:** Why is this worth solving now relative to competing work?
5. **First-version boundary:** Why did the first version include these behaviors and exclude others?
6. **Validation:** Which behavior, result, and guardrail would show whether the hypothesis is correct?
7. **Observed result:** What happened after real use, and what decision changed because of it?

Classify each answer:

- `complete`: supported by verified or user-confirmed evidence;
- `partial`: plausible evidence exists but scope, definition, or attribution is incomplete;
- `missing`: no evidence yet;
- `contradictory`: sources cannot all be true.

Interpret the result:

| Pattern | Honest classification | Resume treatment |
|---|---|---|
| Build exists; user and validation missing | Demo or implementation proof | Use for engineering or learning evidence; do not claim product closure |
| User problem exists; prioritization or scope rationale missing | Discovery plus prototype | Show the observed need and current hypothesis |
| Real use exists; result or follow-up decision missing | Early product usage | Report adoption accurately and state that outcome validation is in progress |
| All seven are supported and iteration follows evidence | Validated product loop | Write the decision, mechanism, result, limitation, and next action |

Hard rules:

- Fast implementation is not product impact.
- A working interface is not proof that the problem was understood.
- AI-generated-code share is not a result without human-owned requirements, review, testing, rework, and operating evidence.
- “先做出来看看” still requires a learning question, bounded cost, success signal, and stop condition.
- Do not fill missing pre-build judgment with a post-hoc story.

## Gap-to-action evidence plan

Create a 30-day plan only when the user has an active real project and access to the relevant users, workflow, or operating data. Choose one decision-critical uncertainty. Do not attempt to repair every resume gap at once.

### Plan construction

1. Name the missing outcome level or decision field.
2. State the product hypothesis and the decision it will inform.
3. Define the cohort, task, observation window, evidence source, and owner.
4. Select one primary signal and one or two guardrails.
5. Capture a baseline or use final attainment when a fair baseline does not exist.
6. Schedule a review point with explicit continue, change, stop, or investigate options.
7. Preserve privacy, consent, confidentiality, and attribution boundaries.

### Suggested cadence

| Period | Purpose | Typical evidence |
|---|---|---|
| Days 1–3 | Define the question and baseline | Workflow map, current workaround, cohort, metric definition, existing logs |
| Week 1 | Observe real behavior | Task traces, drop-offs, repeated complaints, user language, failure samples |
| Week 2 | Ship or compare one bounded change | Release note, alternative considered, non-goals, instrumentation, test conditions |
| Week 3 | Measure behavior and guardrails | Repeat use, completion, edits, time, errors, quality, cost, manual intervention |
| Week 4 | Make and document the decision | Result summary, limitations, continue/change/stop decision, next hypothesis |

Do not prescribe interviews, A/B tests, or quantitative targets mechanically. A small set of traceable workflow observations can be appropriate for an early B2B tool; a consumer growth claim usually needs broader behavioral data. Match the method to the decision and available scale.

## Output templates

### Product decision record

```markdown
# [Decision title]

- Date and phase:
- User and workflow:
- Trigger evidence:
- Existing workaround:
- Problem magnitude:
- Why now / opportunity cost:
- Options considered:
- Decision and rationale:
- First-version scope / non-goals:
- Hypothesis:
- Success metric / guardrails:
- Rollout and ownership:
- Observed result:
- Feedback / bad cases:
- Follow-up decision:
- Proof / uncertainty:
```

### Vibe Coding audit

| Question | Evidence | Status | Gap | Next evidence action |
|---|---|---|---|---|
| User |  |  |  |  |
| Scenario |  |  |  |  |
| Existing solution |  |  |  |  |
| Priority |  |  |  |  |
| First-version boundary |  |  |  |  |
| Validation |  |  |  |  |
| Observed result |  |  |  |  |

### Thirty-day evidence plan

| Date | Decision question | Evidence action | Primary signal | Guardrail | Artifact | Review decision |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

End every accumulation-mode response by distinguishing:

- what can be written now;
- what can be discussed only as in-progress work;
- what remains a future plan and must not enter the resume as a result.
