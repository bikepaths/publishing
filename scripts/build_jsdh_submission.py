import os
import re
import subprocess

def clean_citations(text):
    # Standardize or clean up text markers if needed, but the draft is already clean
    return text

def compile_docx(md_path, docx_path):
    cmd = ["pandoc", "-s", md_path, "-o", docx_path]
    subprocess.run(cmd, check=True)
    print(f"Compiled DOCX: {docx_path}")

def compile_pdf_from_tex(tex_path, out_dir):
    cmd = ["pdflatex", "-interaction=nonstopmode", "-output-directory", out_dir, tex_path]
    # Run twice for page references if needed
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)
    print(f"Compiled PDF: {tex_path.replace('.tex', '.pdf')}")

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

    # Extract Abstract
    abstract_section = re.search(r"## Abstract\n\n(.*?)\n\n", draft_content, re.DOTALL)
    abstract = abstract_section.group(1).strip() if abstract_section else ""

    # Extract Keywords
    keywords_match = re.search(r"Keywords include (.*?)\.", draft_content)
    keywords = keywords_match.group(1).strip() if keywords_match else "chronic homelessness, moral physics, cognitive agency, survival infrastructure, public utility, compelled care"

    # Extract Declarations
    declarations_section = re.search(r"## Declarations\n\n(.*?)(?=\n## References|\Z)", draft_content, re.DOTALL)
    declarations = declarations_section.group(1).strip() if declarations_section else ""

    # Word Count
    word_count = len(draft_content.split())

    # Build Title Page Markdown
    title_page_md = f"""# {title}

## {subtitle}

**Author:** Charles J. DiBella  
**Affiliation:** Director, Urban Systems Research  
**Contact:** charles.dibella@bikepaths.org  
**Submission Type:** Theoretical Paper  
**Word Count:** {word_count} words  

---

### Abstract
{abstract}

**Keywords:** {keywords}

---

### Declarations

{declarations}
"""

    title_page_path = os.path.join(jsdh_dir, "Title_Page.md")
    with open(title_page_path, "w", encoding="utf-8") as f:
        f.write(title_page_md)
    print(f"Created: {title_page_path}")

    # Build Anonymous Manuscript Markdown (removes any hypothetical author details)
    # The current manuscript_draft.md is already anonymous, so we just copy it but make sure headings are standardized.
    anonymous_md = draft_content
    anonymous_path = os.path.join(jsdh_dir, "Manuscript_Anonymous.md")
    with open(anonymous_path, "w", encoding="utf-8") as f:
        f.write(anonymous_md)
    print(f"Created: {anonymous_path}")

    # Compile DOCX versions using pandoc
    compile_docx(title_page_path, os.path.join(jsdh_dir, "Title_Page.docx"))
    compile_docx(anonymous_path, os.path.join(jsdh_dir, "Manuscript_Anonymous.docx"))

    # Compile Title Page to PDF via pandoc (using pdflatex engine)
    subprocess.run(["pandoc", title_page_path, "-o", os.path.join(jsdh_dir, "Title_Page.pdf"), "--pdf-engine=pdflatex"], check=True)
    print("Compiled PDF: Title_Page.pdf")

    # Build Anonymous Manuscript LaTeX for professional submission look
    # Double-spaced, 1-inch margins, continuous line numbers.
    # Parse sections from markdown body
    body_content = draft_content
    # Find start of body (Introduction)
    intro_idx = body_content.find("## 1. Introduction")
    if intro_idx != -1:
        body_content = body_content[intro_idx:]
    
    # Format headings for LaTeX
    # Strip the numbers from ## and ### headers to let LaTeX handle numbering natively
    body_content = re.sub(r'^## \d+\.\s+(.*)$', r'\\section{\1}', body_content, flags=re.MULTILINE)
    body_content = re.sub(r'^### \d+\.\d+\s+(.*)$', r'\\subsection{\1}', body_content, flags=re.MULTILINE)
    
    # Handle non-numbered sections
    body_content = body_content.replace("## Declarations", "\\section*{Declarations}")
    body_content = body_content.replace("### Funding", "\\subsection*{Funding}")
    body_content = body_content.replace("### Disclosure Statement", "\\subsection*{Disclosure Statement}")
    body_content = body_content.replace("### Data Availability Statement", "\\subsection*{Data Availability Statement}")

    # Parse References
    ref_idx = body_content.find("## References")
    references_latex = ""
    if ref_idx != -1:
        refs_part = body_content[ref_idx:]
        body_content = body_content[:ref_idx]
        # Clean up refs_part header
        refs_part = re.sub(r'^## References\s*', '', refs_part)
        # Separate reference items (paragraphs)
        ref_items = [r.strip() for r in refs_part.split("\n\n") if r.strip()]
        references_latex = "\\section*{References}\n\\begin{hangingpars}\n"
        for ref in ref_items:
            # Replace markdown italics with latex italics
            ref_clean = re.sub(r'\*(.*?)\*', r'\\textit{\1}', ref)
            ref_clean = ref_clean.replace("&", "\\&")
            references_latex += f"{ref_clean}\n\n"
        references_latex += "\\end{hangingpars}\n"

    # Replace formatting markers in body
    body_latex = body_content
    body_latex = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', body_latex)
    body_latex = re.sub(r'\*(.*?)\*', r'\\textit{\1}', body_latex)
    body_latex = body_latex.replace("&", "\\&")
    body_latex = body_latex.replace("%", "\\%")
    body_latex = body_latex.replace(" — ", " --- ")

    latex_document = f"""\\documentclass[12pt]{{article}}
\\usepackage[utf8]{{inputenc}}
\\usepackage[margin=1in]{{geometry}}
\\usepackage{{setspace}}
\\usepackage{{lineno}}
\\usepackage{{titlesec}}
\\usepackage{{hyperref}}
\\usepackage{{parskip}}
\\usepackage{{booktabs}}

% APA double-spacing and line numbers
\\doublespacing
\\linenumbers

% Formatting section titles
\\titleformat{{\\section}}
  {{\\normalfont\\large\\bfseries}}{{\\thesection.}}{{0.5em}}{{}}
\\titleformat{{\\subsection}}
  {{\\normalfont\\normalsize\\bfseries}}{{\\thesubsection.}}{{0.5em}}{{}}

% Hanging indent for bibliography
\\newenvironment{{hangingpars}}
  {{\\setlength{{\\parindent}}{{0pt}}
   \\setlength{{\\parskip}}{{6pt}}
   \\everypar{{\\hangindent=0.5in}}}}
  {{}}

\\hypersetup{{
  colorlinks=true,
  linkcolor=blue,
  citecolor=blue,
  urlcolor=blue,
  pdftitle={{{title}}},
  pdfauthor={{Anonymous}}
}}

\\begin{{document}}

\\begin{{center}}
\\setstretch{{1.4}}
{{\\LARGE \\textbf{{{title}}}}}\\\\[6pt]
{{\\large {subtitle}}}\\\\[1cm]
\\textbf{{Abstract}}\\\\[0.5cm]
\\end{{center}}

\\noindent
{abstract}

\\vspace{{0.5cm}}
\\noindent \\textbf{{Keywords:}} {keywords}

\\newpage

{body_latex}

{references_latex}

\\end{{document}}
"""

    tex_path = os.path.join(jsdh_dir, "Manuscript_Anonymous.tex")
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(latex_document)
    print(f"Created: {tex_path}")

    # Compile the anonymous manuscript to PDF using pdflatex
    compile_pdf_from_tex(tex_path, jsdh_dir)

if __name__ == "__main__":
    main()
