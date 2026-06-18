# Resume Matcher Lessons

Source studied: `Resume-Matcher学习教程-合订本.pdf`, generated June 3, 2026.

Apply these principles to the lightweight local webpage without copying the full client-server architecture.

## Single source of truth

- Treat the master resume as the complete evidence library.
- Derive tailored company-role versions from the master.
- Never let saving a tailored version overwrite the master.
- Flag skills or claims in a tailored version when no supporting text exists in the master.

## Preview and confirm

- Generate rewrite suggestions as differences, not as an immediate full replacement.
- Preserve protected facts: identity, employer, institution, dates, degree, certifications, and original skills.
- Capture a fingerprint of the source material used to create a preview.
- Refuse to apply a stale preview after the source, company, role, or job description changes.

## Enrichment

- Identify the highest-value missing evidence.
- Ask at most six questions to limit user fatigue.
- Cover scope, result, tools, individual contribution, collaboration, and duration.
- Preserve original bullets and append newly confirmed evidence.
- Do not invent metrics when the user has none; describe qualitative impact instead.

## Import quality

- Preserve PDF line structure using text coordinates instead of joining every item with spaces.
- Show extracted ATS-readable text before parsing.
- Warn when no selectable text is found, as the PDF may be an image scan.
- Validate the structured result after parsing and preserve dates found in the source.

## Matching

- Separate the master resume view from the tailored JD match view.
- Filter stop words and use case-insensitive matching.
- Show matched and missing terms transparently.
- Treat percentages as local diagnostics, never as a claim about an employer's ATS.

## Evaluation

- Test imports, source protection, preview invalidation, version isolation, section order, print controls, and mobile overflow.
- Prefer deterministic local checks for safety invariants.
- Keep failures isolated: one failed suggestion or parser field should not discard the rest of the resume.
