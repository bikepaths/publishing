import os
import re

research_dir = "/home/user0/git/publishing/220_relational_engineering_wp5/research"
out_path = "/home/user0/git/publishing/220_relational_engineering_wp5/WP5_Working_Paper.tex"

# Read compiled mechanics
with open(f"{research_dir}/03_compiled_operational_mechanics.md", "r") as f:
    mechanics = f.read()

# Edit the 5% threshold calibration
mechanics = mechanics.replace(
    "The MDI five-percent ceiling is set more stringently than both comparators because field contact errors produce direct relational harm at the moment of contact, whereas assessment coding errors in controlled training environments do not. This is a design specification requiring prospective calibration at the prototype stage; if field data from the Singular Prototype Threshold shows that five percent is unachievable at the training duration specified, the training specification will be revised accordingly.",
    "The MDI five-percent ceiling is set more stringently than both comparators because field contact errors produce direct relational harm at the moment of contact.\\\\\n\\textbf{Epistemic Calibration:} This five-percent misclassification ceiling is a provisional design parameter requiring prospective calibration at the prototype stage. It is an asserted target, not an empirically validated constant for this workforce. If field data from the Singular Prototype Threshold shows that five percent is unachievable at the training duration specified, the specification will be revised accordingly."
)

# Edit the algorithmic weights calibration
mechanics = mechanics.replace(
    "\\caption*{Table B: Tie verification protocol and algorithmic weighting schema.}\n\\end{table}",
    "\\caption*{Table B: Tie verification protocol and provisional algorithmic weighting schema.}\n\\end{table}\n\n\\textbf{Epistemic Calibration:} The algorithmic weights assigned to verified ties (+3 for reciprocity, +2 for hub density, -5 for toxicity risk) are provisional pilot parameters. They are not derived from empirical calibration of homelessness network data. They represent a theoretical weighting of the relative impact of each tie type on housing retention. These weights require explicit calibration against real-world retention data during the Singular Prototype Threshold deployment."
)

# Grab Sections 4, 5, and References from the legacy source
with open(f"{research_dir}/99_legacy_WP5_source.tex", "r") as f:
    legacy = f.read()

legacy_tail = legacy.split("\\section{Integration with WP4 Verification Metrics}")[1]
integration_sec = "\\section{Integration with WP4 Verification Metrics}" + legacy_tail.split("\\section{Contribution and Sequence}")[0]
contribution_sec = "\\section{Contribution and Sequence}" + legacy_tail.split("\\section{Contribution and Sequence}")[1].split("\\addcontentsline{toc}{section}{References}")[0]

# Modify Contribution sec to remove objection preemption
contribution_sec = re.sub(r"It preempts the eight objection categories.*?before it becomes an obstacle\.", "", contribution_sec, flags=re.DOTALL)

# Fix the LAO attribution in the integration_sec 
integration_sec = integration_sec.replace("LAO (2024)", "California State Auditor (2024)")
integration_sec = integration_sec.replace("LAO Los Angeles County figure", "California State Auditor Los Angeles County figure")

preamble = r"""% ════════════
% WP5_Working_Paper.tex
% Relational Engineering Specifications: Operational Protocols for Outreach Contact and Pod Assignment
% Material Dignity Infrastructure Working Paper 5
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
\rhead{\small\textit{{Material Dignity Infrastructure Working Paper 5}}}
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
  pdftitle={{Relational Engineering Specifications}},
  pdfauthor={{Charles J. DiBella}}
}
\setcounter{tocdepth}{2}

\begin{document}
\captionsetup[table]{labelfont=normalfont, labelsep=period, skip=6pt}

\begin{titlepage}
\begin{center}
\setstretch{1.4}
{\LARGE \textbf{Relational Engineering Specifications}}\\[6pt]
{\large Operational Protocols for Outreach Contact and Pod Assignment}\\[0.5cm]
{\normalsize \textbf{Charles J. DiBella}}\\[0.01cm]
{\normalsize Principal Systems Architect}\\[0.01cm]
{\normalsize Working Paper, June 2026}\\[0.3cm]
\textbf{ABSTRACT}
\vspace{0.2cm}
\end{center}
\begin{minipage}{0.95\textwidth}
\setstretch{1.15}
\noindent
Convert the theoretical construct of ``relational dignity'' into a field-executable engineering specification. This paper bridges the ethnographic bedrock of street-level trust formation with the neurobiological architecture of the autonomic nervous system to produce a standardized, scalable operational manual for the Material Dignity Infrastructure (MDI) street-to-home pipeline. Relational dignity is a measurable production output requiring precise structural preconditions. Sustainable transition requires replacing vertical compliance with horizontal, needs-responsive engagement grounded in consistency of return and unconditional regard. This paper operationalizes the Relational Intake Protocol through a three-state Autonomic Routing Matrix, and the Social Network Transition Protocol through a reciprocity-weighted pod assignment algorithm. The protocol's assignment weights and misclassification ceilings are explicit design parameters requiring prospective calibration through the Singular Prototype Threshold, isolating what must be built from what must be proven.
\end{minipage}
\end{titlepage}

\pagenumbering{arabic}

\newpage
\section*{Document Metadata}

\noindent\textbf{Keywords}\\[1pt]
Relational intake protocol, polyvagal theory, autonomic routing, neuroception, social network analysis, pod assignment algorithm, warm offer, street-to-home pipeline, MDI, relational dignity infrastructure, Dunbar pod

\vspace{8pt}
\noindent\textbf{JEL Classification}
\begin{itemize}[nosep, before={\vspace{-8pt}}, leftmargin=2em]
    \item I14. Health and Inequality
    \item I38. Government Policy; Provision and Effects of Welfare Programs
    \item H75. State and Local Government: Health, Education, Welfare
    \item Z13. Economic Sociology; Economic Anthropology; Social and Economic Stratification
\end{itemize}

\vspace{8pt}
\noindent\textbf{Target eJournals}
\begin{itemize}[nosep, before={\vspace{-8pt}}, leftmargin=2em]
    \item Housing and Residential Economics eJournal
    \item Public Health Law and Policy eJournal
    \item Social Capital, Networks \& Trust eJournal
    \item Behavioral \& Experimental Economics eJournal
\end{itemize}

\vspace{8pt}
\noindent\textbf{Suggested Citation}\\[1pt]
DiBella, C.J. (2026). Relational Engineering Specifications: Operational Protocols for Outreach Contact and Pod Assignment. Material Dignity Infrastructure Working Paper 5, June 2026.

\newpage

\vspace{8pt}
\noindent\textbf{Author's Note and Statement of Necessity}\\[1pt]
Working Paper 4 (SSRN 6881539) of this series established that the relational layer must be designed to specification, built into the operational architecture, and measured against defined thresholds. A theoretical framework without operational specifications is a research contribution without deployment capacity. This paper provides the build manual for the two operational decisions that determine whether the relational layer functions from day one of tower operation: who makes the offer and how, and who lives with whom after the offer is accepted. The Autonomic Routing Matrix is the manual for the outreach worker on the street. The Social Network Analysis pipeline is the manual for the Process 4 data administrator managing pod assignments.

The Material Dignity Infrastructure series operates as a cumulative preprint architecture in which each working paper builds on prior papers in the sequence. Citations to prior MDI working papers operate as citations to the developing theoretical framework they establish, not as citations to peer-reviewed empirical findings. Those internal assumptions await external validation through the Singular Prototype Threshold.

\newpage
\begingroup
\setstretch{1.35}
\setlength{\cftbeforesecskip}{2pt}
\setlength{\cftbeforesubsecskip}{-2pt}
\tableofcontents
\endgroup

\clearpage
\setstretch{1.35}

\clearpage
\section{The Ethnographic Bedrock and Theoretical Grounding}

The Autonomic Routing Matrix is a theoretical formalization of Porges's polyvagal architecture, applied to the specific contact conditions of street outreach. Longitudinal street outreach practice on Skid Row, Los Angeles provided the motivating context for this formalization. Field methodology dictates that trust is built through fixed-schedule, non-contingent material offerings (food, tobacco) that signal unconditional regard rather than incentivize behavior. The operative field protocol replaces institutional intake questions with a single inquiry: \textit{do you need anything?}

This foundational field data is partial. It systematically documents successful contact initiation rates and material exchange patterns, but lacks longitudinal tracking of autonomic state shifts and physiological baselines. It serves as the motivating context that demands the protocol, not its empirical validation. The foundation of the protocol relies on the polyvagal literature. The field observations confirm the practical necessity of applying that literature to this population: a fixed-schedule, needs-responsive methodology produced observable affective shifts across repeated encounters with chronically street-present individuals, a pattern consistent with the autonomic state-transition dynamics polyvagal theory predicts.

The critical applied finding is that approach vector, physical posture, and verbal script cannot be fixed across all contact attempts. They must match the observable neurological state of the individual at the moment of contact. Asking ``do you want to come inside?'' to an individual in dorsal-vagal shutdown is a category error because the question requires prefrontal processing capacity that the shutdown state has suspended. The offer fails not because the individual rejects housing but because the offer was made to a nervous system that cannot receive it. Polyvagal theory explains this mechanism. The Autonomic Routing Matrix operationalizes it.

\clearpage
"""

references = r"""
\clearpage
\addcontentsline{toc}{section}{References}
\section*{References}

Community Guide. "Housing First: Community Living for Adults Experiencing Homelessness." \textit{The Community Preventive Services Task Force}, 2020.

Culhane, Dennis P., Stephen Metraux, and Trevor Hadley. "Public Service Reductions Associated with Placement of Homeless Persons with Severe Mental Illness in Supportive Housing." \textit{Housing Policy Debate} 13, no. 1 (2002): 107–163.

DiBella, Charles J. \textit{Material Dignity Infrastructure: A Distributed Stewardship Model for Homelessness Resolution}. SSRN Working Paper 5968756. 2025.

DiBella, Charles J. \textit{Material Dignity Infrastructure: Structural Misalignment and the Activation of Surplus Shelter Capacity}. SSRN Working Paper 6211658. February 2026.

DiBella, Charles J. \textit{Material Dignity Infrastructure: Los Angeles Metropolitan Stabilization: A Street-to-Home Pipeline Analysis}. SSRN Working Paper 6579600. May 2026.

DiBella, Charles J. \textit{Relational Dignity Infrastructure: The Human Layer Required to Make Material Housing Inhabitable}. SSRN Working Paper 6881539. June 2026.

Dunbar, Robin I.M. "Neocortex Size as a Constraint on Group Size in Primates." \textit{Journal of Human Evolution} 22, no. 6 (1992): 469--493.

Dunbar, Robin I.M. \textit{Grooming, Gossip, and the Evolution of Language}. Cambridge: Harvard University Press, 1998.

Grossman, Peter, and Edwin W. Taylor. "A Clarification and Defense of the Theory of Polyvagal Control." \textit{Biological Psychology} 74, no. 2 (2007): 260–268.

Hawkins, Robert L., and Craig Abrams. "Disappearing Acts: The Social Networks of Formerly Homeless Individuals with Co-occurring Disorders." \textit{Social Science and Medicine} 65, no. 10 (2007): 2031–2042.

Pleace, Nicholas, Riitta Culhane, Riitta Granfelt, and Marcus Knutagård. \textit{The Finnish Homelessness Strategy: An International Review}. Helsinki: Ministry of the Environment, 2015.

Porges, Stephen W. \textit{The Polyvagal Theory: Neurophysiological Foundations of Emotions, Attachment, Communication, and Self-Regulation}. New York: Norton, 2011.

Tsai, Jack, Richard Stanhope, Robert A. Rosenheck, and Wesley J. Kasprow. "The Role of Housing, Substance Abuse, and Mental Illness in Community Participation and Community Integration." \textit{Psychiatric Services} 63, no. 5 (2012): 435–442.

Wasserman, Stanley, and Katherine Faust. \textit{Social Network Analysis: Methods and Applications}. Cambridge: Cambridge University Press, 1994.

Y-Foundation. \textit{A Home of Your Own: Housing First and Ending Homelessness in Finland}. Helsinki: Y-Foundation, 2022.

\end{document}
"""

with open(out_path, "w") as f:
    f.write(preamble)
    f.write(mechanics)
    f.write("\n\\clearpage\n")
    f.write(integration_sec)
    f.write("\n\\clearpage\n")
    f.write(contribution_sec)
    f.write(references)
