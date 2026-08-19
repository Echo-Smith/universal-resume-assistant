# Product clarity gate for product and AI-product resumes

Use this reference before releasing a project section when the candidate is targeting product management, product operations, AI product, Agent strategy, customer success, or another role where technology must be translated into user value.

The gate exists to prevent a common failure: the draft contains real work and impressive implementation detail, but a recruiter still cannot tell what product was built, who needed it, or why the mechanism mattered.

## 1. Run the five-second test

Read only the project title, opening line, and first bullet. A non-technical recruiter should be able to answer:

1. Who is the user or operator?
2. What task are they trying to finish?
3. What was difficult or unreliable before?
4. What can they now do in the product?
5. What evidence shows use, repeat behavior, user outcome, or business outcome?

If two or more answers are missing, stop polishing and reconstruct the project.

An opening such as “built a dual-mode Agent with memory, RAG, MCP, and multi-Agent orchestration” fails. It inventories implementation without defining a product.

## 2. Use the product-first sequence

For the main project, prefer this sequence:

`user and task → concrete product functions → why a mechanism was necessary → feedback-driven change → highest defensible result`

The sequence is not a rigid sentence template. It is an information-order test.

- **User and task:** name the user and the job they are trying to complete.
- **Concrete functions:** describe what the user selects, enters, reviews, edits, approves, receives, or exports.
- **Mechanism and reason:** connect each material technical choice to an observed failure, constraint, or error cost.
- **Feedback-driven change:** show what evidence changed product behavior, not merely what was “optimized.”
- **Result:** lead with the highest evidence level actually reached.

## 3. Require a reason for every technical term

Highlight every framework, architecture, model, and acronym. For each one, finish this sentence:

`We used [technology or mechanism] because [specific user, workflow, reliability, safety, latency, or cost problem].`

Delete or move the term to a compact stack line when the sentence cannot be completed with confirmed evidence.

Good logic:

`Sources could not be audited → record retrieval sources and preserve citations → reviewers can inspect the basis before approval.`

Weak logic:

`Used RAG, Memory, ReAct, MCP, and a four-agent architecture.`

Technology may prove depth, but it cannot substitute for the product problem.

## 4. Keep versions subordinate to decisions

Do not use V1 / V2 / V3 as the default story. Version labels often create a release log instead of a product narrative and encourage duplicated descriptions.

Keep version history in the evidence ledger. Mention a version in the resume only when all three are true:

1. a real user or operating failure was observed;
2. the later version changed product behavior or scope materially;
3. the decision cannot be explained clearly without the version distinction.

Otherwise write the iteration directly:

`After users reported generic wording, separated shared writing rules from user-level expression preferences.`

This shows iteration without making the reader decode version history.

## 5. Define safety through observable behavior

Internal labels such as S0–S4, P0–P3, red/yellow/green, or high/medium/low are meaningless unless the reader knows:

- which inputs count as dangerous;
- what ordinary flow is stopped;
- what the system shows or does instead;
- where a human, specialist, or emergency channel takes over.

Write the behavior first. A generalized pattern is:

`Defined urgent-risk inputs such as explicit self-harm or acute physical symptoms; when detected, stopped the normal recommendation flow and displayed professional-help guidance.`

Only add internal grading when the target role specifically requires policy taxonomy and the definition is interview-defensible.

## 6. Rank evidence before choosing numbers

Classify evidence as:

1. business outcome;
2. user outcome;
3. repeat behavior;
4. adoption or completed tasks;
5. exposure or experience volume;
6. feature completion;
7. technical activity.

Lead with the highest defensible level. For example, a small number of users completing a real workflow is usually stronger than a much larger number who only opened or tried the product. Keep the larger exposure count as context, not the headline.

Do not combine levels into a stronger causal claim. “Users completed a task with the product” does not automatically mean the product caused every downstream result.

## 7. Replace abstract labels with product behavior

Challenge these phrases:

- 收敛 MVP
- 划定安全边界
- 搭建能力
- 打通闭环
- 持续验证
- 赋能创作
- 提升体验
- 优化策略

For each phrase, ask:

`What did the user do, what did the system do, what changed, or what was deliberately not built?`

Examples of stronger evidence:

- “Removed open-ended personalization from the first release and used six explicit state choices so first-time users could start without writing a prompt.”
- “When a delete or high-value edit was requested, showed the parsed fields and required confirmation before execution.”
- “After failed long-running tasks, added resumable steps and a user takeover point instead of retrying the entire flow.”

## 8. Preserve human voice without becoming conversational

Human writing is not casual filler. It is wording that the candidate would naturally use to explain the project in an interview.

- Prefer familiar product verbs: chose, entered, reviewed, approved, returned, corrected, published.
- Use architecture terms only where they carry explanatory weight.
- Let different projects emphasize different evidence; do not reuse identical four-part bullet templates.
- Avoid defensive disclaimers in the resume. Preserve attribution through precise wording and keep caveats in the evidence ledger or interview notes unless omission would mislead.

## 9. Release checklist

Fail the project section when any answer is “no”:

- Can a recruiter describe the product without reading the technology terms?
- Does the opening identify a user and concrete task?
- Are the main functions visible before the architecture?
- Does every major technical choice answer a stated problem?
- Are version labels optional rather than structural?
- Are safety rules expressed as inputs and responses?
- Does the result lead with the highest defensible evidence level?
- Can the candidate explain each line in ordinary interview language?
