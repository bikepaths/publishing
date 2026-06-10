import os
import re
import argparse

def get_section(header, text):
    m = re.search(rf'## {header}\n\n(.*?)(?=\n---|## |\Z)', text, re.DOTALL)
    if m:
        return m.group(1).strip()
    return ""

def main():
    parser = argparse.ArgumentParser(description="Compile Working Paper LaTeX from Markdown Manifest")
    parser.add_argument('--manuscript', required=True, help='Path to markdown manuscript')
    parser.add_argument('--metadata', required=True, help='Path to markdown metadata')
    parser.add_argument('--template', required=True, help='Path to LaTeX preamble template')
    parser.add_argument('--output', required=True, help='Path to output tex file')
    args = parser.parse_args()

    with open(args.metadata, 'r') as f:
        meta_text = f.read()

    abstract_md = get_section("Abstract", meta_text)
    abstract_tex = abstract_md.replace('\n\n', '\n\n\\vspace{0.2cm}\n')

    necessity_md = get_section("Statement of Necessity", meta_text)
    necessity_tex = necessity_md

    keywords_md = get_section("Keywords", meta_text)
    jel_md = get_section("JEL Classification Codes", meta_text)
    jel_items = [line.strip('- ').strip() for line in jel_md.split('\n') if line.strip().startswith('-')]
    jel_tex = "\\begin{itemize}[nosep, before={\\vspace{-8pt}}, leftmargin=2em]\n"
    for item in jel_items:
        item = re.sub(r'\*\*(.*?)\*\*', r'\1', item)
        jel_tex += f"    \\item {item}\n"
    jel_tex += "\\end{itemize}"

    journals_md = get_section("Target eJournals", meta_text)
    journal_items = [line.split('. ', 1)[1] for line in journals_md.split('\n') if re.match(r'\d+\.', line)]
    journals_tex = "\\begin{itemize}[nosep, before={\\vspace{-8pt}}, leftmargin=2em]\n"
    for item in journal_items:
        item_clean = item.replace('&', '\\&')
        journals_tex += f"    \\item {item_clean}\n"
    journals_tex += "\\end{itemize}"

    m_title = re.search(r'\*\*Title:\*\* (.*)', meta_text)
    title_full = m_title.group(1) if m_title else "Title"
    if ":" in title_full:
        title_main, title_sub = title_full.split(':', 1)
    else:
        title_main = title_full
        title_sub = ""

    m_author = re.search(r'\*\*Author:\*\* (.*)', meta_text)
    author_full = m_author.group(1) if m_author else "Author, Title"
    author_name, author_title = author_full.split(', ', 1)

    m_version = re.search(r'\*\*Version:\*\* .*, (.*)', meta_text)
    date_str = m_version.group(1) if m_version else "Date"

    m_series = re.search(r'\*\*Series:\*\* (.*)', meta_text)
    series_str = m_series.group(1) if m_series else "Series"

    series_context_md = get_section("Series Context", meta_text)
    authors_note = series_context_md.split('\n\n')[-1]

    filename = os.path.basename(args.output)

    with open(args.template, 'r') as f:
        preamble = f.read()

    preamble = preamble.replace('{filename}', filename)
    preamble = preamble.replace('{title_main}', title_main.strip())
    preamble = preamble.replace('{title_sub}', title_sub.strip())
    preamble = preamble.replace('{series_str}', series_str.strip())
    preamble = preamble.replace('{date_str}', date_str.strip())
    preamble = preamble.replace('{author_name}', author_name.strip())
    preamble = preamble.replace('{keywords_md}', keywords_md.strip())

    front_matter = f"""\\captionsetup[table]{{labelfont=normalfont, labelsep=period, skip=6pt}}

% ── FRONT MATTER ───
\\begin{{titlepage}}
\\begin{{center}}
\\setstretch{{1.4}}
{{\\LARGE \\textbf{{{title_main.strip()}}}}}\\\\[6pt]
{{\\large {title_sub.strip()}}}\\\\[0.5cm]
{{\\normalsize \\textbf{{{author_name.strip()}}}}}\\\\[0.01cm]
{{\\normalsize {author_title.strip()}}}\\\\[0.01cm]
{{\\normalsize Working Paper, {date_str.strip()}}}\\\\[0.3cm]
\\textbf{{ABSTRACT}}
\\vspace{{0.2cm}}
\\end{{center}}
\\begin{{minipage}}{{0.95\\textwidth}}
\\setstretch{{1.15}}
\\noindent

{abstract_tex}

\\end{{minipage}}
\\end{{titlepage}}

\\pagenumbering{{arabic}}

% ── DOCUMENT METADATA ────
\\newpage
\\section*{{Document Metadata}}

\\noindent\\textbf{{Keywords}}\\\\[1pt]
{keywords_md}

\\vspace{{8pt}}
\\noindent\\textbf{{JEL Classification}}
{jel_tex}

\\vspace{{8pt}}
\\noindent\\textbf{{Target eJournals}}
{journals_tex}

\\vspace{{8pt}}
\\noindent\\textbf{{Author's Note}}\\\\[1pt]
This paper is the fifth working paper in the Material Dignity Infrastructure series. {authors_note}

\\vspace{{8pt}}
\\noindent\\textbf{{Suggested Citation}}\\\\[1pt]
DiBella, C.J. (2026). {title_main.strip()}: {title_sub.strip()}. {series_str.strip()}, {date_str.strip()}.

\\newpage
% ── TABLE OF CONTENTS ────
\\vspace{{12pt}}
\\begingroup
\\setstretch{{1.35}}
\\setlength{{\\cftbeforesecskip}}{{2pt}}
\\setlength{{\\cftbeforesubsecskip}}{{-2pt}}
\\tableofcontents
\\endgroup
% ── BODY ────
\\setstretch{{1.35}}

"""

    with open(args.manuscript, 'r') as f:
        md_content = f.read()

    md_lines = md_content.split('\n')
    start_idx = 0
    for i, line in enumerate(md_lines):
        if line.startswith('## I.'):
            start_idx = i
            break

    md_body = '\n'.join(md_lines[start_idx:])

    tex_body = md_body
    tex_body = re.sub(r'^## ([A-Z]+)\.\s+(.*)$', r'\\section{\2}', tex_body, flags=re.MULTILINE)
    tex_body = re.sub(r'^### ([\d\.]+)\s+(.*)$', r'\\subsection{\2}', tex_body, flags=re.MULTILINE)
    tex_body = tex_body.replace('## References', '\\newpage\n\n\\addcontentsline{toc}{section}{References}\n\\section*{References}')

    tex_body = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', tex_body)
    tex_body = re.sub(r'\*(.*?)\*', r'\\textit{\1}', tex_body)

    tex_body = tex_body.replace('$', '\\$')

    table1_md = """| Domain | Question | Target Output |
| :--- | :--- | :--- |
| \\textbf{Material Security} | "When you leave your tent, who watches your gear?" | Identifies primary trust node |
| \\textbf{Metabolic Supply} | "Who do you share food or tobacco with?" | Identifies routine reciprocal nodes |
| \\textbf{Crisis Response} | "If you get sick or hurt, who do you find first?" | Identifies apex reliance node |
| \\textbf{Toxicity Flag} | "Is there anyone here you need to stay away from?" | Identifies predator or parasite nodes requiring separation |"""
    tex_body = tex_body.replace(' — ', ' --- ')
    tex_body = tex_body.replace(' - ', ' --- ')
    tex_body = tex_body.replace('−', '$-$')
    tex_body = tex_body.replace('%', '\\%')
    tex_body = tex_body.replace('&', '\\&')

    table1_tex = """\\begin{table}[H]
\\renewcommand{\\arraystretch}{1.2}
\\begin{tabularx}{\\textwidth}{@{} >{\\raggedright\\arraybackslash}p{3.5cm} >{\\raggedright\\arraybackslash}X >{\\raggedright\\arraybackslash}p{5.5cm} @{}}
\\toprule
\\textbf{Domain} & \\textbf{Question} & \\textbf{Target Output} \\\\
\\midrule
\\textbf{Material Security} & "When you leave your tent, who watches your gear?" & Identifies primary trust node \\\\
\\textbf{Metabolic Supply} & "Who do you share food or tobacco with?" & Identifies routine reciprocal nodes \\\\
\\textbf{Crisis Response} & "If you get sick or hurt, who do you find first?" & Identifies apex reliance node \\\\
\\textbf{Toxicity Flag} & "Is there anyone here you need to stay away from?" & Identifies predator or parasite nodes requiring separation \\\\
\\bottomrule
\\end{tabularx}
\\end{table}"""

    tex_body = tex_body.replace(table1_md, table1_tex)

    table2_md = """| Metric | Verification Action | Algorithmic Weight |
| :--- | :--- | :--- |
| \\textbf{Reciprocity, Verified} | Both nodes confirm the tie independently | \\textbf{+3}, Primary Cluster Anchor |
| \\textbf{Reciprocity, Unverified} | One node denies or is unavailable | \\textbf{0}, Discard |
| \\textbf{Density, Hub} | Node named by three or more individuals in the encampment | \\textbf{+2}, Central Hub |
| \\textbf{Toxicity, Risk} | Node named as threat by any verified node | \\textbf{-5}, Isolation Flag |"""

    table2_tex = """\\begin{table}[H]
\\renewcommand{\\arraystretch}{1.2}
\\begin{tabularx}{\\textwidth}{@{} >{\\raggedright\\arraybackslash}p{3.5cm} >{\\raggedright\\arraybackslash}X >{\\raggedright\\arraybackslash}p{5.5cm} @{}}
\\toprule
\\textbf{Metric} & \\textbf{Verification Action} & \\textbf{Algorithmic Weight} \\\\
\\midrule
\\textbf{Reciprocity, Verified} & Both nodes confirm the tie independently & \\textbf{+3}, Primary Cluster Anchor \\\\
\\textbf{Reciprocity, Unverified} & One node denies or is unavailable & \\textbf{0}, Discard \\\\
\\textbf{Density, Hub} & Node named by three or more individuals in the encampment & \\textbf{+2}, Central Hub \\\\
\\textbf{Toxicity, Risk} & Node named as threat by any verified node & \\textbf{$-5$}, Isolation Flag \\\\
\\bottomrule
\\end{tabularx}
\\end{table}"""

    tex_body = tex_body.replace(table2_md, table2_tex)

    tex_body = re.sub(r'(?m)^---\n?', '', tex_body)
    tex_body += "\n\\end{document}\n"

    with open(args.output, 'w') as f:
        f.write(preamble + front_matter + tex_body)

    print("success")

if __name__ == "__main__":
    main()
