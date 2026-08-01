# Privacy and evidence standard

Use this reference when handling source material, resolving conflicts, anonymizing content, or preparing files for public sharing.

## Source authority

Prefer evidence in this order:

1. the user's latest explicit correction;
2. current official records or primary artifacts;
3. a maintained evidence ledger;
4. older resumes, profiles, and portfolios;
5. third-party summaries;
6. assistant inference.

Record the source location and the exact scope it supports. A source may verify that an event occurred without proving personal ownership, causality, or a particular metric.

## Claim checks

For each important claim, verify:

- **subject**: who did the work;
- **scope**: individual, team, department, organization, or community;
- **time**: when and for how long;
- **action**: what the candidate actually did;
- **result**: what changed;
- **attribution**: what portion can reasonably be linked to the action;
- **measurement**: baseline, unit, method, time window, and conditions;
- **proof**: artifact, record, reference, or user confirmation;
- **sensitivity**: whether the detail may be shared.

One contradiction can block a claim. A surprising claim is not false by itself; ask for corroboration and use conservative wording until confirmed.

## Personal and sensitive data

Treat the following as sensitive unless the user explicitly needs it in a private final resume:

- personal phone numbers and email addresses;
- home addresses and precise personal locations;
- government, tax, insurance, banking, or account identifiers;
- dates of birth, family details, medical information, and protected attributes;
- private profile links, unpublished portfolios, and access tokens;
- customer names, internal project names, contract terms, security details, and non-public metrics;
- hidden document metadata, comments, tracked changes, and revision history.

Do not retain sensitive data in examples, test fixtures, logs, public repositories, or reusable packages.

## Anonymization protocol

1. Determine whether the detail is necessary for the hiring claim.
2. Remove it if it adds no decision value.
3. Replace it with a neutral category if the category matters, such as `regional hospital`, `public secondary school`, or `consumer services company`.
4. Generalize a metric only with approval, using a truthful range or relative description.
5. Re-read the result for re-identification through combinations of rare role, location, date, client, award, or metric.
6. Confirm that the anonymized text has not increased ownership or certainty.

Use placeholders such as `[Candidate Name]`, `[Organization]`, `[Location]`, `[Email]`, and `[Portfolio URL]` in templates.

## Fairness boundary

Assess evidence of job performance and requirements. Do not infer competence, honesty, motivation, culture fit, salary expectations, or employability from protected traits or proxies such as name, photo, age, nationality, disability, address, family status, school prestige, email domain, or an unexplained employment gap.

Identify a legal or credential requirement only when it is relevant to the target role and jurisdiction. Do not provide legal conclusions from memory.

## Public-release checklist

- Search all text files for emails, phone numbers, absolute home paths, secrets, access keys, real names, and private URLs.
- Inspect generated archives with a file listing before sharing.
- Exclude caches, temporary files, previews, operating-system metadata, editor settings, and version-control secrets.
- Inspect office-document metadata, comments, notes, and tracked changes when those formats are included.
- Confirm examples use synthetic placeholders.
- Confirm repository history does not contain removed sensitive data.
