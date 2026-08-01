# Quality and delivery checklist

Use this reference for final review, scoring, rendering, file synchronization, and cleanup.

## Diagnostic rubric

Score each dimension from 0 to 4 and cite evidence for the score.

| Dimension | 0 | 2 | 4 |
|---|---|---|---|
| Truthfulness | Material contradictions or invented claims | Some unsupported wording | Claims are traceable and calibrated |
| Target clarity | Target is unclear | Target is inferable | Role and level are immediately clear |
| Relevance | Mostly unrelated detail | Mixed relevance | Strongest target evidence leads |
| Ownership | Individual contribution is obscured | Scope is partly clear | Personal and team contributions are precise |
| Evidence quality | Duties or adjectives only | Some observable support | Results, records, or scope support important claims |
| Structure | Legacy template controls content | Generally readable | Hierarchy reflects evidence and target |
| Concision | Repetitive or generic | Minor redundancy | Each line adds distinct decision value |
| Consistency | Dates and terms conflict | Minor inconsistencies | Dates, tense, units, and terms agree |
| Privacy | Sensitive data is unnecessarily exposed | Some review remains | Data is minimized and release-safe |
| Defensibility | Major claims cannot be explained | Most claims are explainable | Important claims support credible discussion |

Treat the score as a diagnostic, not a hiring prediction. A zero in truthfulness, privacy, or defensibility is a release blocker regardless of the total.

## Content review

1. Read only headings, titles, and first lines to test the hiring thesis.
2. Check every ownership verb against the evidence ledger.
3. Check every number for definition, arithmetic, conditions, and attribution.
4. Check every credential, tool, method, and regulated activity for actual use and current wording.
5. Remove duplication, unsupported superlatives, generic self-praise, and irrelevant detail.
6. Verify chronology, employment type, concurrent work, and planned versus completed activity.
7. Generate interview questions for the strongest claims; qualify any claim the user cannot defend.
8. Run the privacy review after content is final.

## ATS and accessibility

- Use recognizable headings appropriate to the destination language.
- Keep critical text selectable and searchable.
- Do not place essential information only in headers, footers, images, icons, charts, or text boxes.
- Use a simple reading order and meaningful link text.
- Prefer common fonts, adequate contrast, and restrained layout.
- Do not optimize for an imagined universal ATS score. Preserve clarity and truthful terminology.
- When a portal has explicit field or file requirements, follow those requirements.

## Format synchronization

Choose one active text source and one shared basename. After any factual correction, update every active format.

For Markdown, DOCX, HTML, and PDF outputs, verify:

- name, target, dates, titles, facts, and links match;
- headings and bullets do not split awkwardly;
- page count and margins fit the user's requirement;
- text remains selectable after rendering;
- print colors and contrast remain readable;
- hyperlinks work and display appropriate text;
- no comments, tracked changes, hidden sheets, notes, or metadata reveal private information.

Inspect the rendered artifact, not only its source.

## Asset and archive hygiene

Before packaging:

1. list every included path;
2. remove temporary renders, previews, caches, lock files, system metadata, editor files, and unrelated artifacts;
3. exclude source evidence unless the user explicitly requests it and privacy review passes;
4. scan text content for personal data and secrets;
5. create the archive;
6. list the archive contents and extract it into a fresh temporary directory;
7. rerun structural and privacy checks on the extracted copy;
8. compare checksums when a remote copy is published.

Cleanup must not delete user-owned history unless the user explicitly requested deletion.
