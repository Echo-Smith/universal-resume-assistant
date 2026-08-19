# Resume asset management

Use this reference when organizing, renaming, archiving, or locating resume files.

## Goals

- One obvious active text source per target role.
- One matching basename for HTML and PDF deliverables.
- Historical versions remain recoverable.
- The manifest explains where current and archived material lives.
- No path changes silently break links, scripts, or documentation.

## Recommended structure

```text
resume/
  README.md
  current/
  evidence/
  archive/
output/
  html/
  pdf/
  archive/
```

Adapt to an existing repository rather than forcing this structure when another documented convention already works.

## Naming

Use:

`姓名-公司或方向-岗位-版本类型.ext`

Keep company and role names consistent across formats. Use the product's current public name, not an obsolete codename, unless history requires both.

Good:

- `[姓名]-[目标公司]-[目标岗位]-定向简历.html`
- `[姓名]-[目标公司]-[目标岗位]-定向简历.pdf`
- `[姓名]-[目标公司]-[目标岗位]-文字稿.md`

Avoid:

- `final-final-v3.pdf`;
- unexplained dates as the only version signal;
- English and Chinese names for the same project across active files;
- several “current” PDFs with no declared authority.

## Safe reorganization workflow

1. List all likely resume, review, image, HTML, and PDF assets.
2. Identify path references in Markdown, HTML, scripts, and manifests.
3. Classify each file as active source, active deliverable, evidence, review, or archive.
4. Resolve basename collisions before moving.
5. Move; do not delete.
6. Update path references and the manifest.
7. Check that every active text source has the expected outputs.
8. Report duplicates or ambiguous authority instead of guessing.

## Archive policy

Archive when a file is:

- superseded by a clearly named active version;
- an intermediate rendering;
- an earlier company-specific draft;
- a duplicate with an older modification time and no unique content;
- a review artifact no longer used as the active source.

Keep evidence and factual evaluations distinguishable from resume drafts.

## Manifest minimum

The manifest should state:

- current target resumes;
- source, HTML, and PDF paths;
- naming convention;
- archive locations;
- image or avatar source;
- generation or verification notes when useful.
