import os
import re

research_dir = "/home/user0/git/publishing/230_political_economy_wp6/research"
out_path = "/home/user0/git/publishing/230_political_economy_wp6/WP6_Working_Paper.tex"

# Read compiled mechanics
with open(f"{research_dir}/01_compiled_deployment_mechanics.md", "r") as f:
    mechanics = f.read()

# Refactor the mechanics into the new headings
mechanics = mechanics.replace(
    "\\textbf{1. Fiscal and Efficiency Critics}", 
    "\\textbf{1. Cost Baseline Displacement (Fiscal and Efficiency Critics)}"
)

mechanics = mechanics.replace(
    "\\textbf{3. NIMBY Opposition}", 
    "\\textbf{2. Statutory Preemption (NIMBY Opposition)}"
)

mechanics = mechanics.replace(
    "\\textbf{4. Housing First Purists}", 
    "\\textbf{3. Sequencing Alignment (Housing First Purists)}"
)

mechanics = mechanics.replace(
    "\\textbf{5. Civil Libertarian Critics}", 
    "\\textbf{4. Structural Grounding (Civil Libertarian Critics)}"
)

mechanics = mechanics.replace(
    "\\textbf{6. Incumbent Service Providers}", 
    "\\textbf{5. Capital Routing (Incumbent Service Providers)}"
)

mechanics = mechanics.replace(
    "\\textbf{7. Regulatory and Permitting Critics}", 
    "\\textbf{6. Exemption Anchoring (Regulatory and Permitting Critics)}"
)

mechanics = mechanics.replace(
    "\\textbf{8. Academic and Methodological Critics}", 
    "\\textbf{7. Prototype Isolation (Academic and Methodological Critics)}"
)

# Purge Market Libertarian
market_libertarian = r"\\textbf\{2\. Market Libertarian Critics\}.*?within the same crisis\.\n\n"
mechanics = re.sub(market_libertarian, "", mechanics, flags=re.DOTALL)

# Synthesis
mechanics = mechanics.replace("\\textbf{Cross-cutting, The Deployment Problem.}", "\\section{Cross-Cutting Synthesis: The Deployment Problem}\n")

preamble = r"""% ════════════
% WP6_Working_Paper.tex
% Political Economy of Deployment: Counterpoint Frameworks and Institutional Friction
% Material Dignity Infrastructure Working Paper 6
% ════════════

\documentclass[12pt, letterpaper]{article}

\usepackage[left=0.7in, right=0.7in, top=1in, bottom=1in, headheight=14pt]{geometry}
\usepackage[expansion=false]{microtype}
\usepackage{textcomp}
\usepackage{setspace}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage[titles]{tocloft}
\usepackage{tabularray}
\usepackage{longtable}
\usepackage{array}
\usepackage{multirow}
\usepackage{hyperref}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{parskip}
\usepackage{titlesec}
\usepackage{fancyhdr}
\usepackage[table]{xcolor}
\usepackage{caption}
\usepackage{footnote}
\usepackage{enumitem}
\usepackage{needspace}
\usepackage{etoolbox}
\usepackage{float}

\definecolor{auditblue}{HTML}{003366}

\setstretch{1.4}
\setlength{\parindent}{0pt}
\setlength{\parskip}{8pt}
\hyphenpenalty=1000

\titleformat{\section}{\normalfont\large\color{auditblue}}{\thesection.}{0.5em}{}
\titleformat{\subsection}{\normalfont\normalsize\color{auditblue}}{\thesubsection.}{0.5em}{}
\titlespacing*{\section}{0pt}{18pt}{6pt}
\titlespacing*{\subsection}{0pt}{12pt}{4pt}

\pagestyle{fancy}
\fancyhf{}
\rhead{\small\textit{{Material Dignity Infrastructure Working Paper 6}}}
\lhead{\small\textit{Working Paper, June 2026}}
\cfoot{\thepage}
\renewcommand{\headrulewidth}{0.4pt}

\renewcommand{\arraystretch}{1.3}

\clubpenalty=10000
\widowpenalty=10000
\displaywidowpenalty=10000
\AtBeginEnvironment{thebibliography}{\interlinepenalty=10000}

\hypersetup{
  colorlinks=true,
  linkcolor=black,
  citecolor=black,
  urlcolor=black,
  pdftitle={{Political Economy of Deployment}},
  pdfauthor={{Charles J. DiBella}}
}
\setcounter{tocdepth}{2}

\begin{document}
\captionsetup[table]{labelfont=normalfont, labelsep=period, skip=6pt}

\begin{titlepage}
\begin{center}
\setstretch{1.4}
{\LARGE \textbf{Political Economy of Deployment}}\\[6pt]
{\large Counterpoint Frameworks and Institutional Friction}\\[0.5cm]
{\normalsize \textbf{Charles J. DiBella}}\\[0.01cm]
{\normalsize Principal Systems Architect}\\[0.01cm]
{\normalsize Working Paper, June 2026}\\[0.3cm]
\textbf{ABSTRACT}
\vspace{0.2cm}
\end{center}
\begin{minipage}{0.95\textwidth}
\setstretch{1.15}
\noindent
Provide the strategic deployment manual required to push the Material Dignity Infrastructure (MDI) architecture through a hostile institutional environment. This paper isolates the structural resistance vectors that guarantee institutional failure for unshielded public goods projects, providing a systematic counterpoint framework against the primary sources of organized opposition. Theoretical coherence and operational precision are insufficient for deployment. Well-designed public goods proposals consistently fail against concentrated incumbent resistance unless the deployment architecture explicitly maps and neutralizes each resistance mechanism. The MDI model must be defended not just on its clinical or architectural merits, but on its capacity to survive the political economy of the homeless services industry.
\end{minipage}
\end{titlepage}

\pagenumbering{arabic}

\newpage
\section*{Document Metadata}

\noindent\textbf{Keywords}\\[1pt]
Political economy, institutional friction, structural grounding, CEQA exemption, AB 2011, LPS Act, civil liberties, CalAIM billing, homelessness, public goods provision

\vspace{8pt}
\noindent\textbf{JEL Classification}
\begin{itemize}[nosep, before={\vspace{-8pt}}, leftmargin=2em]
    \item P16. Political Economy
    \item H41. Public Goods
    \item K32. Environmental, Health, and Safety Law
    \item R38. Government Policies; Regulatory Policies
\end{itemize}

\vspace{8pt}
\noindent\textbf{Target eJournals}
\begin{itemize}[nosep, before={\vspace{-8pt}}, leftmargin=2em]
    \item Political Economy: Government Expenditures \& Related Policies eJournal
    \item Law \& Society: Public Law eJournal
    \item Urban Economics \& Regional Studies eJournal
\end{itemize}

\vspace{8pt}
\noindent\textbf{Suggested Citation}\\[1pt]
DiBella, C.J. (2026). Political Economy of Deployment: Counterpoint Frameworks and Institutional Friction. Material Dignity Infrastructure Working Paper 6, June 2026.

\newpage

\vspace{8pt}
\noindent\textbf{Geographic Scope Parameter and Framing}\\[1pt]
The specific deployment mechanisms analyzed here (AB 2011, LPS Act WIC Section 5350, Medi-Cal) are California-specific. The document functions as a localized proof-of-concept for neutralizing opposition. While the categories of friction (incumbents, civil liberties, NIMBYism) are national, the exact statutory routing detailed in this paper is geographically constrained to California.

This paper serves as a manual for project architects facing institutional friction. The MDI architecture recognizes that an engineering specification is useless if the project dies in committee, fails to acquire a permit, or generates a constitutional injunction. This document transitions the MDI focus from clinical and architectural integrity toward the structural mechanics of legal and political survival.

\newpage
\begingroup
\setstretch{1.35}
\setlength{\cftbeforesecskip}{2pt}
\setlength{\cftbeforesubsecskip}{-2pt}
\tableofcontents
\endgroup

\clearpage
\setstretch{1.35}

"""

references = r"""
\clearpage
\addcontentsline{toc}{section}{References}
\section*{References}

Buchanan, James M., and Gordon Tullock. \textit{The Calculus of Consent: Logical Foundations of Constitutional Democracy}. Ann Arbor: University of Michigan Press, 1962.

Culhane, Dennis P., Stephen Metraux, and Trevor Hadley. "Public Service Reductions Associated with Placement of Homeless Persons with Severe Mental Illness in Supportive Housing." \textit{Housing Policy Debate} 13, no. 1 (2002): 107–163.

Hawkins, Robert L., and Craig Abrams. "Disappearing Acts: The Social Networks of Formerly Homeless Individuals with Co-occurring Disorders." \textit{Social Science and Medicine} 65, no. 10 (2007): 2031–2042.

Lee, C., and Song, S. "The Effect of Supportive Housing on Neighborhood Property Values." \textit{Urban Studies} 56, no. 14 (2019): 2933-2949.

Nguyen, Mai Thi. "Does Affordable Housing Detrimentally Affect Property Values? A Review of the Literature." \textit{Journal of Planning Literature} 20, no. 1 (2005): 15-26.

Olson, Mancur. \textit{The Logic of Collective Action: Public Goods and the Theory of Groups}. Cambridge: Harvard University Press, 1965.

Pleace, Nicholas, Riitta Culhane, Riitta Granfelt, and Marcus Knutagård. \textit{The Finnish Homelessness Strategy: An International Review}. Helsinki: Ministry of the Environment, 2015.

Porges, Stephen W. \textit{The Polyvagal Theory: Neurophysiological Foundations of Emotions, Attachment, Communication, and Self-Regulation}. New York: Norton, 2011.

Scott, James C. \textit{Seeing Like a State: How Certain Schemes to Improve the Human Condition Have Failed}. New Haven: Yale University Press, 1998.

Szasz, Thomas. \textit{The Therapeutic State: Psychiatry in the Mirror of Current Events}. Buffalo: Prometheus Books, 1984.

Tsai, Jack, Richard Stanhope, Robert A. Rosenheck, and Wesley J. Kasprow. "The Role of Housing, Substance Abuse, and Mental Illness in Community Participation and Community Integration." \textit{Psychiatric Services} 63, no. 5 (2012): 435–442.

Y-Foundation. \textit{A Home of Your Own: Housing First and Ending Homelessness in Finland}. Helsinki: Y-Foundation, 2022.

\end{document}
"""

os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, "w") as f:
    f.write(preamble)
    f.write(mechanics)
    f.write(references)
