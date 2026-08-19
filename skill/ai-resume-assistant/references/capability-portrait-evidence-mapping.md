# Capability portrait and evidence mapping

Use this reference when the target role requires layered abilities rather than a flat keyword list — especially AI-product, agent-strategy, or technology-adjacent product roles — or when the user supplies a personal capability portrait and wants to know what to strengthen and what the resume may claim.

## 1. Turn the JD into a capability portrait

Group the JD requirements into capability layers. For AI-product roles, a useful example is:

| Layer | What it checks | Typical JD signals |
|---|---|---|
| Model and AI-system literacy | Knows why model mechanisms (context, generation, retrieval, tokens, sampling) affect product behavior; understands training, tuning, prompting, multimodal, and inference optimization at the level needed for product judgment | “理解大模型原理与能力边界”, “了解 SFT / LoRA / RAG / 评测” |
| Agent architecture and failure design | Context assembly, memory, retrieval, tool calling, multi-agent boundaries, retry / manual takeover / termination | “Agent 效果策略”, “Memory 策略”, “Badcase 闭环” |
| Data and evaluation | Case sets, baselines, benchmarks, metrics, badcase taxonomy, offline vs online, cost / latency / stability guardrails | “评测集”, “Rubric”, “Benchmark” |
| Product loop | User discovery, problem worth solving, scope, prioritization, launch, feedback, iteration | “用户洞察”, “需求拆解”, “上线复盘” |
| Cross-functional collaboration | Translates business goals into technical problems and technical constraints into product tradeoffs | “与算法、研发协作” |
| Business scenario | Domain users, workflow, compliance, commercialization, service quality | 行业关键词 |
| Continuous learning | Generalizes across frameworks and paradigms | 隐性要求 |

Adjust the layers to the actual target role; do not copy this table verbatim into a resume.

## 2. Map each layer to evidence

For every capability layer, record:

| Capability layer | JD signals | Evidence | Strength | Proof | Resume action |
|---|---|---|---|---|---|
|  |  |  | strong / partial / missing / irrelevant |  | keep / rebuild / discuss only / postpone |

Rules:

- A capability without a project, decision, or artifact is `claimed only`; it may not enter the resume.
- Interview-credible knowledge (can explain, ran small experiments) supports interviews, but only verified or user-confirmed completed work enters the resume.
- Do not inherit capabilities from frameworks, platforms, teammates, or underlying model vendors.
- Separate personal action from team output at every layer.
- The strongest evidence is usually a decision, failure mode, or measured tradeoff, not the number of tools used.

## 3. Three-state classification for every material claim

| State | Meaning | Resume | Interview |
|---|---|---|---|
| write-now | Verified or user-confirmed completed work | Write as a result | Defend with proof |
| in-progress | Active work without frozen results | Do not write as a result; may be listed as clearly labeled ongoing work | Explain the question, method, guardrails, and current status |
| future-goal | Aspiration or planned direction | Never enters as experience | Mention only as direction, not as capability |

### Guardrails for in-progress and future claims

- No directional comparisons before conditions are frozen: same task, sample, model and version, knowledge snapshot, tool permissions, budget, and judge.
- Split a composite result into same-capability comparison, new-capability coverage change, and the price paid (latency, cost, manual intervention).
- A benchmark is a project artifact, not a claim. Write the product decision it produced, not the architecture that ran it.
- A career goal such as “build a general agent tool” is direction, not experience; it does not justify platform-scale or commercial-maturity claims.

## 4. Career mainline

Define three statements:

1. **Entry scenario:** where the user already has real users, workflows, and results.
2. **Transferable generalization:** the reusable capability the scenario demonstrates, for example “turning unstructured knowledge work into intervene-able, evaluable AI workflows.”
3. **Long-term goal:** the direction it prepares, labeled explicitly as direction, for example “general knowledge-work or agent tools.”

Resume order: lead with the transferable generalization, support it with entry-scenario evidence, and keep the long-term goal out of the results section.

## 5. Output templates

### Capability–evidence matrix

| Layer | Evidence | Strength | Proof | Write now / in-progress / future | Next action |
|---|---|---|---|---|---|

### In-progress evidence record

| Field | Content |
|---|---|
| Decision question | What decision will this evidence inform |
| Scope conditions | Task, sample, model, knowledge snapshot, tools, budget, judge |
| Status | frozen / collecting / analyzing / not started |
| Results so far | Completed observations only |
| Guardrails | Latency, cost, quality, manual intervention |
| Resume treatment | write-now / discuss-only / future |

### Mainline card

```text
Entry scenario: ...
Transferable capability: ...
Long-term goal (direction only): ...
```

End every response by returning:

1. evidence-backed fit per layer;
2. screening risk;
3. the highest-value evidence actions — usually one real task, benchmark, or user loop, not more tools;
4. questions that could change the conclusion.
