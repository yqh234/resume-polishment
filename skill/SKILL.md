---
name: resume-polish-webpage
description: Generate a polished, job-application-ready resume webpage and resume text from a user's raw experience, target company, and target role. Use when the user asks to beautify, package, rewrite, polish, or tailor a resume, work experience, project experience, internship experience, career story, or personal pitch into a professional web page or deliverable resume for job applications, especially in Chinese workplace contexts.
---

# Resume Polish Webpage

## Overview

Turn raw career experience into a tailored resume webpage with professional visual styling and application-ready copy. Require the user to provide their experience, target company, and target role before producing the final resume.

## Required Inputs

Ask for missing information before final generation if any of these are absent:

- Raw experience: education, work/project/internship history, achievements, tools, metrics, responsibilities, constraints, and preferred facts to include.
- Target company: company name, business/domain, values, product line, job location if relevant.
- Target role: role title, level, job description, requirements, keywords, and preferred language.

If the user gives only a brief experience, ask up to five focused follow-up questions about measurable results, scope, tools, collaboration, and role relevance. If the user wants speed, proceed with clearly labeled assumptions.

## Workflow

1. Parse the user's raw experience into evidence units: responsibility, action, tool/method, result, metric, domain, collaboration, leadership, and transferable skill.
2. Infer the target role's hiring signals from the company and role: required skills, seniority, domain vocabulary, behavioral traits, and likely ATS keywords.
3. Read `references/aesthetic-effects-library.md` and choose one workplace-appropriate aesthetic profile. Prefer restrained, credible, scan-friendly styles over decorative or consumer-brand styles.
4. Rewrite the resume content in a factual, evidence-first way. Do not fabricate degrees, employers, dates, certifications, revenue, awards, or metrics. If a strong metric is missing, phrase the impact qualitatively or mark a placeholder for user confirmation.
5. Generate a single-page responsive HTML resume website unless the user asks for a different format. Include embedded CSS and no external build step unless the surrounding project already uses one.
6. Save the webpage as an output artifact when working in a filesystem environment. Use a clear filename such as `resume-<company>-<role>.html`.
7. Provide a concise summary of the positioning, selected visual style, and any facts that need user confirmation.

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
- Do not add visible instructions explaining how to use the page.
- Do not use fake logos from the target company unless the user provides brand assets or explicitly asks for text-only mention.
- Do not include decorative stock photos unless they directly support the professional context.

## Quality Bar

Before final delivery, check:

- The content is tailored to the target company and role instead of being generic.
- All strong claims are grounded in user-provided facts or marked for confirmation.
- The page looks credible in a workplace setting and can be scanned by a recruiter within 30 seconds.
- Text does not overflow buttons, cards, section headers, or mobile containers.
- The final answer tells the user where the HTML file was saved and lists any assumptions.
