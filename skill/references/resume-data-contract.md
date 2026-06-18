# Resume Data Contract

Store resume data as UTF-8 JSON. Keep user facts separate from presentation.

## Required fields

- `version`: schema version number.
- `raw`: original imported or pasted material.
- `candidate`: candidate name.
- `company`: target company for a tailored version.
- `role`: target role.
- `contact`: phone, email, and city in readable text.
- `jd`: supplied job description.
- `education`: education evidence.
- `work`: work or internship evidence.
- `projects`: project evidence.
- `skills`: skills, languages, certificates, and awards.
- `polished`: user-reviewed rewritten experience lines.
- `sectionOrder`: ordered section identifiers.
- `updatedAt`: ISO 8601 timestamp.

## Storage rules

- Store one `master` record containing the complete evidence library.
- Store tailored records under `variants`, keyed by a stable local identifier.
- Never replace the master automatically when saving a company version.
- Preserve `raw` and `polished` together for traceability.
- Reject or flag unknown schema versions instead of silently dropping fields.

## Validation rules

- Require a plausible name, target company, target role, phone, and email before final export.
- Require at least one dated education, work, or project entry.
- Require each strong result claim to retain supporting evidence from the source.
- Flag sensitive identity, banking, family, marital, and exact-address information.
- Keep all ATS-facing fields as selectable text.
