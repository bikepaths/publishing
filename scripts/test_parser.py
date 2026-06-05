import re

wp5_metadata_path = '/home/user0/git/publishing/220_relational_engineering_wp5/ssrn/WP5_SSRN_Metadata.md'

with open(wp5_metadata_path, 'r') as f:
    meta_text = f.read()

def get_section(header, text):
    m = re.search(rf'## {header}\n\n(.*?)(?=\n---|## |\Z)', text, re.DOTALL)
    if m:
        return m.group(1).strip()
    return ""

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

m_version = re.search(r'\*\*Version:\*\* .*— (.*)', meta_text)
date_str = m_version.group(1) if m_version else "Date"

m_series = re.search(r'\*\*Series:\*\* (.*)', meta_text)
series_str = m_series.group(1) if m_series else "Series"

series_context_md = get_section("Series Context", meta_text)
authors_note = series_context_md.split('\n\n')[-1]

front_matter = f"""\\captionsetup[table]{{labelfont=normalfont, labelsep=period, skip=6pt}}

% ── FRONT MATTER ───
\\begin{{titlepage}}
\\begin{{center}}
\\setstretch{{1.4}}
{{\\LARGE \\textbf{{{title_main}}}}}\\\\[6pt]
{{\\large {title_sub.strip()}}}\\\\[0.5cm]
{{\\normalsize \\textbf{{{author_name}}}}}\\\\[0.01cm]
{{\\normalsize {author_title}}}\\\\[0.01cm]
{{\\normalsize Working Paper, {date_str}}}\\\\[0.3cm]
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
\\noindent\\textbf{{Suggested Citation}}\\\\[1pt]
DiBella, C.J. (2026). {title_main}: {title_sub.strip()}. {series_str}. Working Paper, {date_str}.

\\newpage

\\vspace{{8pt}}
\\noindent\\textbf{{Statement of Necessity}}\\\\[1pt]
{necessity_tex}

\\vspace{{8pt}}
\\noindent\\textbf{{Author's Note}}\\\\[1pt]
This paper is the fifth working paper in the Material Dignity Infrastructure series. {authors_note}

"""

print(front_matter)
