import os
import re
import subprocess

def compile_docx(md_path, docx_path):
    cmd = ["pandoc", "-s", md_path, "-o", docx_path]
    subprocess.run(cmd, check=True)
    print(f"Compiled DOCX: {docx_path}")

def main():
    jsdh_dir = "/home/user0/git/publishing/networking/jsdh"
    draft_path = os.path.join(jsdh_dir, "manuscript_draft.md")
    
    with open(draft_path, "r", encoding="utf-8") as f:
        draft_content = f.read()

    # Extract Title and Subtitle
    title_match = re.search(r"^#\s+(.*)$", draft_content, re.MULTILINE)
    subtitle_match = re.search(r"^##\s+(?!Abstract|1\.|2\.|3\.|4\.|5\.|6\.|Declarations|References)(.*)$", draft_content, re.MULTILINE)
    
    title = title_match.group(1).strip() if title_match else "The Moral Physics of Survival"
    subtitle = subtitle_match.group(1).strip() if subtitle_match else "Thermodynamic Precarity, Cognitive Agency, and the Ethics of Compelled Stabilization"

    # Extract Abstract using a robust pattern that handles single or multiple newlines
    abstract_section = re.search(r"## Abstract\s*\n+(.*?)(?=\n+Keywords|\n+##|\Z)", draft_content, re.DOTALL)
    abstract = abstract_section.group(1).strip() if abstract_section else ""
    print(f"Extracted Abstract length: {len(abstract)} characters")

    # Extract Keywords
    keywords_match = re.search(r"Keywords include (.*?)\.", draft_content)
    keywords = keywords_match.group(1).strip() if keywords_match else "chronic homelessness, moral physics, cognitive agency, survival infrastructure, public utility, compelled care"

    # Separate Body and References
    body_content = draft_content
    # Find start of body (Introduction)
    intro_idx = body_content.find("## 1. Introduction")
    if intro_idx != -1:
        body_content = body_content[intro_idx:]

    # Build Anonymous Manuscript markdown
    anonymous_md = f"""# {title}

## {subtitle}

## Abstract
{abstract}

Keywords: {keywords}

{body_content}
"""

    # Build Full Manuscript markdown (including corrected independent scholar details)
    full_md = f"""# {title}

## {subtitle}

**Author:** Charles J. DiBella  
**Affiliation:** Independent Scholar  
**Contact:** bikepaths@duck.com  

## Abstract
{abstract}

Keywords: {keywords}

{body_content}
"""

    # Temporary paths
    anon_md_path = os.path.join(jsdh_dir, "Manuscript_Anonymous.md")
    full_md_path = os.path.join(jsdh_dir, "Manuscript_Full.md")

    # Write temporary markdown files
    with open(anon_md_path, "w", encoding="utf-8") as f:
        f.write(anonymous_md)
    with open(full_md_path, "w", encoding="utf-8") as f:
        f.write(full_md)

    # Compile to docx
    anon_docx_path = os.path.join(jsdh_dir, "Manuscript_Anonymous.docx")
    full_docx_path = os.path.join(jsdh_dir, "Manuscript_Full.docx")
    compile_docx(anon_md_path, anon_docx_path)
    compile_docx(full_md_path, full_docx_path)

    # Clean up intermediate markdown files
    if os.path.exists(anon_md_path):
        os.remove(anon_md_path)
    if os.path.exists(full_md_path):
        os.remove(full_md_path)

    # Clean up all PDF, TeX, and title page remnants
    remnants = [
        "Title_Page.md",
        "Title_Page.docx",
        "Title_Page.pdf",
        "Manuscript_Anonymous.pdf",
        "Manuscript_Anonymous.tex",
        "Manuscript_Anonymous.md"
    ]
    for filename in remnants:
        path = os.path.join(jsdh_dir, filename)
        if os.path.exists(path):
            os.remove(path)
            print(f"Removed remnant: {path}")

if __name__ == "__main__":
    main()
