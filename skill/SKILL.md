---
name: resume-polish-webpage
description: Generate a polished, job-application-ready resume webpage and resume text from a user's raw experience, target company, and target role. Use when the user asks to beautify, package, rewrite, polish, or tailor a resume, work experience, project experience, internship experience, career story, or personal pitch into a professional web page or deliverable resume for job applications, especially in Chinese workplace contexts.
---

# Resume Polish Webpage

## Overview

Turn raw career experience into a tailored resume webpage with professional visual styling and application-ready copy. Require the user to provide their experience, target company, and target role before producing the final resume.

When extending the tool's data model, privacy behavior, matching logic, imports, versioning, or rewrite safety, read `references/github-benchmarks.md`, `references/resume-data-contract.md`, and `references/resume-matcher-lessons.md`.

## Required Inputs

Ask for missing information before final generation if any of these are absent:

- Raw experience: education, work/project/internship history, achievements, tools, metrics, responsibilities, constraints, and preferred facts to include.
- Target company: company name, business/domain, values, product line, job location if relevant.
- Target role: role title, level, job description, requirements, keywords, and preferred language.

If the user gives only a brief experience, ask up to five focused follow-up questions about measurable results, scope, tools, collaboration, and role relevance. If the user wants speed, proceed with clearly labeled assumptions.

## Workflow

1. Accept pasted text or extract text locally from PDF, DOCX, or TXT input. Show the extracted text before transforming it so the user can check ATS readability and parser omissions.
2. Parse the user's raw experience into evidence units: responsibility, action, tool/method, result, metric, domain, collaboration, leadership, and transferable skill.
3. Normalize the material into the structure in `references/resume-data-contract.md`. Preserve original wording alongside rewritten content so every modification remains traceable.
4. Infer the target role's hiring signals from the company, role, and supplied job description: hard skills, tools, soft skills, domain terms, responsibilities, and seniority.
5. Compare the job description with the resume using transparent exact and normalized keyword matching. Report matched terms, missing terms, evidence coverage, and information completeness. Never present a heuristic score as the target company's real ATS score.
6. Read `references/aesthetic-effects-library.md` and choose one workplace-appropriate aesthetic profile. Prefer restrained, credible, scan-friendly styles over decorative or consumer-brand styles.
7. Rewrite the resume content in a factual, evidence-first way. Generate changes against an immutable source snapshot, present original and rewritten lines side by side, and invalidate the preview if the source changes before confirmation. Never allow rewrite operations to modify identity, employer, institution, dates, degrees, or other protected facts.
8. When material is weak, ask no more than six high-value questions about scope, measurable result, tools, individual contribution, collaboration, and duration. Preserve the original bullet and append confirmed evidence instead of silently replacing it.
9. Run a credibility, structural, master-alignment, and privacy audit. Validate required contact fields, dates, section completeness, unsupported superlatives, unverified metrics, personal contribution, unnecessary sensitive data, and any skill absent from the master evidence.
10. Generate a single-page responsive HTML resume website unless the user asks for a different format. Detect likely one-page overflow, allow section reordering, and keep editing controls out of print output.
11. Maintain one master resume with the user's complete evidence library. Derive and save independent company-role versions without overwriting the master.
12. Keep resume data local by default. Include local persistence and JSON import/export so the user owns and can reuse their data.
13. Run `scripts/evaluate_skill.py` after changing the skill or webpage and fix all failed checks.
14. Save the webpage as an output artifact when working in a filesystem environment. Use a clear filename such as `resume-<company>-<role>.html`.
15. Provide a concise summary of the positioning, selected visual style, match gaps, validation warnings, and any facts that need user confirmation.

## Resume Content Rules

Use this structure by default:

- Header: candidate name or placeholder, target title, contact placeholders, location/availability if provided.
- Target summary: 2-4 lines tailored to the company and role.
- Core strengths: 4-6 keyword-rich strengths aligned with the target job.
- Experience: bullet points using action + scope + method + outcome.
- Projects: emphasize business problem, personal contribution, technical/process method, and measurable or observable result.
- Skills: group by relevance, not by an exhaustive inventory.
- Education/certifications: include only provided facts.

Prefer concrete verbs such as built, led, optimized, analyzed, coordinated, launched, migrated, designed, negotiated, automated, researched, and delivered. Avoid inflated wording such as "visionary", "world-class", "unparalleled", and "revolutionary" unless the evidence truly supports it.

## Webpage Requirements

Build a polished, professional page suitable for sending as a link or exporting to PDF:

- First viewport must immediately communicate candidate positioning and target role.
- Do not generate a standalone cover page, title page, or "MY RESUME" opening page. Start directly with the resume body: name, target role, contact information, and sections.
- Use a clean information hierarchy with dense but readable sections.
- Keep styling workplace-appropriate: calm color system, restrained accents, ample alignment, printable contrast, and no playful visual gimmicks.
- Include `@media print` styles so the page prints cleanly to A4 or Letter.
- Make the page responsive from mobile to desktop.
- Parse imported files locally and disclose when scanned PDFs cannot produce selectable text.
- Keep the master resume separate from company-specific variants.
- Provide a reversible original-versus-rewritten review step.
- Warn when the printable resume is likely to exceed one page.
- Keep ATS-facing content in ordinary text and standard section headings; do not encode essential information only in icons, charts, progress bars, or decorative canvases.
- Do not add visible instructions explaining how to use the page.
- Do not use fake logos from the target company unless the user provides brand assets or explicitly asks for text-only mention.
- Do not include decorative stock photos unless they directly support the professional context.

## Quality Bar

Before final delivery, check:

- The content is tailored to the target company and role instead of being generic.
- All strong claims are grounded in user-provided facts or marked for confirmation.
- Match analysis is explainable: show which supplied JD terms were found or missing and remind the user not to add skills they do not possess.
- Imported PDF or DOCX text can be previewed before recognition.
- Original text and rewritten text remain visibly traceable.
- A rewrite preview becomes invalid if its source content changes before confirmation.
- Enrichment asks at most six targeted questions and does not silently replace original evidence.
- Saved company versions do not mutate the master resume.
- Skills added to a tailored version are checked against the master evidence.
- Structural validation and the deterministic skill evaluation pass.
- Sensitive personal data is excluded or explicitly flagged.
- The page looks credible in a workplace setting and can be scanned by a recruiter within 30 seconds.
- Text does not overflow buttons, cards, section headers, or mobile containers.
- The final answer tells the user where the HTML file was saved and lists any assumptions.
