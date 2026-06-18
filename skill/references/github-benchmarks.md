# GitHub Benchmarks

Use these projects as design references, not as code to copy blindly.

## Reactive Resume

Source: https://github.com/amruthpillai/reactive-resume

Adopt:

- Real-time editing and preview.
- User-owned data with local or self-hosted control.
- Structured import and export.
- A4 and Letter-aware print output.

Avoid importing its account, database, or deployment complexity into a single-file resume tool.

## JSON Resume Schema

Source: https://github.com/jsonresume/resume-schema

Adopt the stable conceptual sections:

- basics
- work
- projects
- education
- skills
- certificates

Keep target company, target role, job description, evidence status, and rewrite traceability as local extensions.

## MatchMyJD

Source: https://github.com/mugunthank7/MatchMyJD

Adopt:

- Separate job-description and resume analysis.
- Skill normalization.
- Transparent matched and missing categories.
- Category-level feedback instead of one unexplained number.

For an offline webpage, use deterministic exact and normalized matching. Clearly label the result as a self-check rather than a real ATS prediction. Never encourage keyword stuffing or fabrication.
