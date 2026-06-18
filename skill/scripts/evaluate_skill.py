#!/usr/bin/env python3
from pathlib import Path
import sys


def find_webpage(skill_dir: Path) -> Path | None:
    candidates = [
        skill_dir.parent / "index.html",
        skill_dir.parent / "resume-polish-webpage.html",
    ]
    return next((path for path in candidates if path.exists()), None)


def main() -> int:
    skill_dir = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    skill_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    webpage = find_webpage(skill_dir)
    html = webpage.read_text(encoding="utf-8") if webpage else ""

    checks = {
        "skill frontmatter": skill_text.startswith("---\nname: resume-polish-webpage\n"),
        "file import workflow": "PDF, DOCX, or TXT" in skill_text,
        "traceable rewrite workflow": "original and rewritten" in skill_text,
        "master and variant workflow": "master resume" in skill_text and "company-role versions" in skill_text,
        "overflow workflow": "one-page overflow" in skill_text,
        "webpage located": webpage is not None,
        "PDF import control": 'id="resumeFile"' in html and "extractPdfText" in html,
        "DOCX parser": "mammoth.extractRawText" in html,
        "ATS preview": 'id="atsPreview"' in html,
        "rewrite comparison": 'id="originalCompare"' in html and 'id="polishedCompare"' in html,
        "section ordering": "sectionOrder" in html and "moveSection" in html,
        "overflow detection": 'id="pageIndicator"' in html and "checkPageOverflow" in html,
        "master storage": "resume-polish-library-v2" in html and "saveMaster" in html,
        "structural validation": "renderValidation" in html,
    }

    failed = [name for name, passed in checks.items() if not passed]
    for name, passed in checks.items():
        print(f"{'PASS' if passed else 'FAIL'}  {name}")
    if failed:
        print(f"\n{len(failed)} check(s) failed.")
        return 1
    print(f"\nAll {len(checks)} checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
