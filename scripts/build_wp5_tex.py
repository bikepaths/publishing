import os
import re

wp4_tex_path = '/home/user0/git/publishing/210_relational dignity_wp4/ssrn/RDI_Working_Paper.tex'
wp5_md_path = '/home/user0/git/publishing/220_relational_engineering_wp5/ssrn/WP5_Working_Paper_Manuscript.md'
wp5_metadata_path = '/home/user0/git/publishing/220_relational_engineering_wp5/ssrn/WP5_SSRN_Metadata.md'
output_path = '/home/user0/git/publishing/220_relational_engineering_wp5/ssrn/WP5_Working_Paper.tex'

with open(wp4_tex_path, 'r') as f:
    wp4_tex = f.read()

preamble_end_marker = r'\begin{document}'
preamble = wp4_tex.split(preamble_end_marker)[0] + preamble_end_marker + '\n'
preamble = preamble.replace('RDI_Working_Paper.tex', 'WP5_Working_Paper.tex')
preamble = preamble.replace('Relational Dignity Infrastructure: The Human Layer Required to Make Material Housing Inhabitable', 'Relational Dignity Infrastructure: Engineering the Street-to-Home Transition Protocol')
preamble = preamble.replace('Material Dignity Infrastructure Working Paper 4', 'Material Dignity Infrastructure Working Paper 5')
preamble = preamble.replace('Relational Dignity Infrastructure (RDI Working Paper 4)', 'Relational Engineering Specifications (RDI Working Paper 5)')

front_matter = r"""\captionsetup[table]{labelfont=normalfont, labelsep=period, skip=6pt}

% ── FRONT MATTER ───
\begin{titlepage}
\begin{center}
\setstretch{1.4}
{\LARGE \textbf{Relational Dignity Infrastructure}}\\[6pt]
{\large Engineering the Street-to-Home Transition Protocol}\\[0.5cm]
{\normalsize \textbf{Charles J. DiBella}}\\[0.01cm]
{\normalsize Principal Systems Architect}\\[0.01cm]
{\normalsize Working Paper, June 2026}\\[0.3cm]
\textbf{ABSTRACT}
\vspace{0.2cm}
\end{center}
\begin{minipage}{0.95\textwidth}
\setstretch{1.15}
\noindent

Working Paper 4 of this series defined Relational Dignity Infrastructure (RDI) as the systematically designed social environment that produces ontological security, sustains identity capital accumulation, and maintains individual recognition within the MDI tower architecture. That paper identified two integration gaps requiring specification: the Relational Intake Protocol, grounding the warm offer in Porges's polyvagal neuroception architecture, and the Social Network Transition Protocol, operationalizing Social Network Analysis methodology for pod assignment. This paper executes both specifications and appends a third contribution: a systematic political economy of opposition analysis cataloging the eight objection categories the MDI-RDI model will encounter at deployment, with sourced counterpoints derived from the empirical and theoretical literature.

\vspace{0.2cm}
The Relational Intake Protocol is specified as a three-state Autonomic Routing Matrix that determines approach vector, physical posture, and verbal script based on the observable autonomic state of the individual at the moment of contact, grounding the clinical principle that a refusal recorded in dorsal-vagal shutdown is a defense reflex, not a cognitive refusal of housing. The Social Network Transition Protocol is specified as a four-domain interview instrument, a reciprocity-weighted scoring algorithm, and a Process 4 pod assignment logic with four priority-ordered constraints. Together these specifications operationalize the two most consequential relational decisions in the street-to-home pipeline: who makes the offer and how, and who lives with whom after the offer is accepted.

\vspace{0.2cm}
The political economy analysis establishes that the eight principal objection categories, including fiscal efficiency, market libertarian, NIMBY, Housing First fidelity, civil libertarian, incumbent provider, regulatory-permitting, and academic-methodological, are each answerable from within the MDI-RDI evidence base, existing California law, and documented international operational outcomes. The cumulative architecture of the MDI model has been structured to reduce the specific friction that each objection category represents.

\end{minipage}
\end{titlepage}

\pagenumbering{arabic}

% ── DOCUMENT METADATA ────
\newpage
\section*{Document Metadata}

\noindent\textbf{Keywords}\\[1pt]
Relational intake protocol, polyvagal theory, autonomic routing, neuroception, social network analysis, pod assignment algorithm, warm offer, street-to-home pipeline, political economy of opposition, incumbent provider resistance, Housing First fidelity, compelled care, MDI, relational dignity infrastructure, Dunbar pod

\vspace{8pt}
\noindent\textbf{JEL Classification}
\begin{itemize}[nosep, before={\vspace{-8pt}}, leftmargin=2em]
    \item I14. Health and Inequality
    \item I38. Government Policy; Provision and Effects of Welfare Programs
    \item H75. State and Local Government: Health, Education, Welfare
    \item Z13. Economic Sociology; Economic Anthropology; Social and Economic Stratification
    \item R21. Urban, Rural, Regional, Real Estate, and Transportation Economics: Housing Demand
    \item D72. Political Processes: Rent-Seeking, Lobbying, Elections, Legislatures, and Voting
\end{itemize}

\vspace{8pt}
\noindent\textbf{Target eJournals}
\begin{itemize}[nosep, before={\vspace{-8pt}}, leftmargin=2em]
    \item Housing and Residential Economics eJournal
    \item Public Health Law and Policy eJournal
    \item State and Local Government eJournal
    \item Social Capital, Networks \& Trust eJournal
    \item Poverty, Income Distribution \& Social Protection eJournal
    \item Behavioral \& Experimental Economics eJournal
\end{itemize}

\vspace{8pt}
\noindent\textbf{Suggested Citation}\\[1pt]
DiBella, C.J. (2026). Relational Dignity Infrastructure: Engineering the Street-to-Home Transition Protocol. Material Dignity Infrastructure Working Paper 5. Working Paper, June 2026.

\newpage

\vspace{8pt}
\noindent\textbf{Statement of Necessity}\\[1pt]
A theoretical framework without operational specifications is a research contribution without deployment capacity. Working Paper 4 named the relational layer and established its production conditions. This paper writes the two field manuals that the relational layer requires to move from theoretical specification to operational practice. The Autonomic Routing Matrix is the manual for the outreach worker on the street. The Social Network Analysis pipeline is the manual for the Process 4 data administrator managing pod assignments. Neither document existed before this paper. Both are required before the warm offer can be executed with relational fidelity at scale.

The political economy appendix exists because a deployment-oriented paper cannot present operational specifications without acknowledging the organized opposition those specifications will face. The academic literature on public goods provision published by Olson in 1965, bureaucratic rent-seeking established by Buchanan and Tullock in 1962, and high-modernist institutional failure documented by Scott in 1998 establishes that well-designed proposals consistently fail against concentrated incumbent resistance unless the proposal's deployment architecture explicitly addresses each resistance mechanism. This paper addresses each.

The field evidence grounding the relational intake specification is drawn in part from DiBella's own longitudinal street outreach documentation, in which a fixed-schedule, needs-responsive, unconditional-regard outreach methodology produced documented trust accumulation over repeated encounters with chronically street-present individuals on Skid Row, Los Angeles. The autonomic state classification in the Routing Matrix is not a theoretical import from clinical psychology. It is a formalization of what that field practice learned empirically: that approach vector, physical posture, and verbal script must match the observable neurological state of the individual, not the institutional preference of the worker.

\vspace{8pt}
\noindent\textbf{Author's Note}\\[1pt]
This paper is the fifth working paper in the Material Dignity Infrastructure series. MDI-D established that the relational layer must be designed to specification, built into the operational architecture, and measured against defined thresholds. This paper writes the specifications. MDI-D without MDI-E is a blueprint without a build manual. This paper provides the build manual for the two operational decisions that determine whether the relational layer functions as designed from day one of tower operation.

% ── TABLE OF CONTENTS ────
\newpage
\begingroup
\setstretch{1.35}
\setlength{\cftbeforesecskip}{2pt}
\setlength{\cftbeforesubsecskip}{-2pt}
\tableofcontents
\endgroup
% ── BODY ────
\clearpage
\setstretch{1.35}

"""

with open(wp5_md_path, 'r') as f:
    md_content = f.read()

md_lines = md_content.split('\n')
start_idx = 0
for i, line in enumerate(md_lines):
    if line.startswith('## I.'):
        start_idx = i
        break

md_body = '\n'.join(md_lines[start_idx:])

tex_body = md_body
tex_body = re.sub(r'^## ([A-Z]+)\.\s+(.*)$', r'\\clearpage\n\\section{\2}', tex_body, flags=re.MULTILINE)
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


# Strip bare markdown horizontal rules that survive conversion.
# These appear as standalone ^---$ lines in the manuscript between sections.
# Mid-line --- sequences (LaTeX dashes in prose) are always flanked by spaces
# and are not affected by this line-level strip.
tex_body = re.sub(r'(?m)^---\n?', '', tex_body)

tex_body += "\n\\end{document}\n"

with open(output_path, 'w') as f:
    f.write(preamble + front_matter + tex_body)

print("success")
