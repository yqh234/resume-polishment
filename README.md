# Resume Polishment

A single-page resume polishing tool for turning raw experience, a target company, and a target role into a polished, workplace-ready resume page.

## Files

- `index.html` - Main resume polishing tool.
- `demo.html` - Example resume generated with the template.
- `skill/` - Codex skill instructions and the aesthetic effects reference.
- `icon.png` - App-style icon asset.

## Usage

Open `index.html` in a browser. Paste a large block of resume material, target company, role, JD, education, projects, skills, and certificates into the recognition box, then click `识别并生成`.

The page can:

- Recognize common resume fields from long pasted text.
- Import PDF, DOCX, and TXT resumes entirely in the browser and preview the ATS-readable text.
- Suggest company-specific resume style research links.
- Adapt positioning for different role families.
- Compare resume content with a supplied JD using transparent matched and missing keywords.
- Audit evidence coverage, information completeness, unsupported claims, and sensitive personal data.
- Review original and polished experience lines side by side before applying changes.
- Reorder resume sections and warn when the printable content is likely to exceed one page.
- Maintain one master resume and save independent company-role application versions.
- Save drafts locally and import or export reusable JSON resume data without uploading it.
- Preview a formal resume layout with optional photo upload.
- Copy the generated resume text or print/export to PDF.

The matching percentage is an explainable pre-submission self-check, not a claim about any company's real ATS score.

## Skill Evaluation

Run the deterministic feature checks after changing the webpage or skill:

```bash
python skill/scripts/evaluate_skill.py skill
```
