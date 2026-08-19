# Resume delivery checklist

Use this checklist for HTML and PDF production.

## Source synchronization

- Identify the active text source.
- Use matching basenames for Markdown, plain text, HTML, and PDF when all four are delivered.
- Compare major headings, dates, numbers, links, and project names across formats.
- Ensure the latest user correction appears everywhere.
- When the resume is intended for multiple hiring platforms, keep a plain-text version whose section order, dates, metrics, and links match the designed version.

## HTML

- Use semantic headings and selectable text.
- Keep contact details readable without depending on icons.
- Use real `href` values for portfolio and project links.
- Provide print-specific CSS.
- Prefer a restrained layout that scans horizontally from top to bottom.
- Avoid decorative English labels that do not add information.

## Print CSS

- Set A4 page size and deliberate margins.
- Preserve intended colors with `print-color-adjust`.
- Replace browser-sensitive gradients with stable print colors when necessary.
- Control page breaks around headings, project blocks, and bullet groups.
- Avoid fixed heights that create bottom whitespace or clip content.

## PDF verification

- Confirm the PDF opens.
- Confirm expected page count.
- Render every page to images.
- Inspect the top, page breaks, links, accent rules, bottom balance, and avatar.
- Confirm text extraction is possible.
- Check that no glyphs, URLs, or bullets are clipped.

## Content integrity

- Do not shrink type below comfortable reading size simply to reach one page.
- Fix redundant wording and spacing before reducing font size.
- Do not delete evidence merely to create visual symmetry.
- Do not add unsupported text to fill whitespace.

## One A4 page

- Target exactly one A4 page per deliverable unless the user explicitly requests a longer version.
- Fit order when content overflows:
  1. compress redundant wording and hierarchy;
  2. reduce section, heading, and bullet spacing;
  3. tighten line height and letter spacing within comfortable bounds;
  4. only as a last resort reduce font size, and never below a comfortable reading size.
- Fit order when content is short of one page:
  1. expand line height and letter spacing within comfortable bounds;
  2. add section spacing and breathing room;
  3. never add filler text, decorative lines, or unsupported claims to fill the page.
- Do not delete evidence, compress meaning, or drop required contact details to reach one page.
- Re-render and inspect the PDF page count and bottom balance after any spacing change.

## Handoff

Provide absolute clickable links to:

1. active text source;
2. HTML;
3. PDF.

Mention page count and visual verification. Name any remaining difference explicitly.
