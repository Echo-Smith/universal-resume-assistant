# Product clarity gate

Use this gate before releasing product, AI-product, Agent strategy, product operations, or customer-success project descriptions.

## Five-second test

Read only the title, opening line, and first bullet. A non-technical reviewer should be able to answer:

1. Who is the user or operator?
2. What concrete task are they trying to finish?
3. What was difficult or unreliable before?
4. What can they now do in the product?
5. What evidence shows use, repeat behavior, user outcome, or business outcome?

If two or more answers are missing, reconstruct the project before polishing it.

## Product-first information order

Prefer:

`user and task -> concrete functions -> mechanism and reason -> feedback-driven change -> highest defensible result`

This is an information-order test, not a sentence template. Projects should still sound different because their evidence differs.

## Technology causality test

For every framework, architecture, model, and acronym, complete:

`Used [mechanism] because [specific workflow, reliability, safety, latency, cost, or control problem].`

Delete or compress the term when the reason cannot be supported. Technology can prove depth; it cannot substitute for the product problem.

Temporarily remove framework names. If the user, task, product behavior, and result disappear, fail the section.

## Version discipline

Do not use V1 / V2 / V3 as the default story. Mention a version only when:

1. a real user or operating failure was observed;
2. the next version changed product behavior or scope materially;
3. the decision cannot be explained clearly without the distinction.

Otherwise state the iteration directly, for example: “After users reported generic wording, separated shared writing rules from user-level expression preferences.”

## Safety through observable behavior

Internal risk labels are not meaningful until the reader knows:

- which inputs count as dangerous;
- which normal flow is stopped;
- what the system displays or does instead;
- where human or professional help takes over.

Write the dangerous input and exact response first. Include internal codes only when the target role needs the taxonomy and the candidate can defend the definitions.

## Evidence ranking

Lead with the highest defensible level:

1. business outcome;
2. user outcome;
3. repeat behavior;
4. adoption or completed tasks;
5. exposure or experience volume;
6. feature completion;
7. technical activity.

A smaller number of users completing a real task is usually stronger than a larger number who only opened or tried the product. Keep exposure as context when stronger evidence exists. Do not upgrade correlation into sole causality.

## Replace abstract labels

Challenge phrases such as “converged the MVP,” “defined the boundary,” “built capabilities,” “closed the loop,” “enabled creation,” and “continuously optimized.” Replace them with:

- what the user selected, entered, reviewed, approved, corrected, or received;
- what the system blocked, returned, retried, or handed over;
- what was deliberately not built;
- which observed failure caused the change.

## Release checklist

- The product remains understandable without technology names.
- The opening identifies a user and concrete task.
- Main functions appear before architecture.
- Every major mechanism answers a stated need or constraint.
- Version labels are optional, not structural.
- Safety rules are expressed as inputs and responses.
- Results lead with the highest defensible evidence.
- The candidate can explain every line in ordinary interview language.
