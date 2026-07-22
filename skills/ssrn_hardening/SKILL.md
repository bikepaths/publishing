---
name: SSRN Hardening
description: Sequential protocol for aligning working papers with the SSRN Academic Style, purging redundancies, and synchronizing metadata.
---

# SSRN Hardening Skill

This skill enforces a zero-drift sequential hardening process for the Material Dignity Infrastructure working paper series. 

## Execution Protocol

When instructed to harden a working paper, the agent MUST execute the following steps in sequence:

1. **Structural Audit:** 
   - Enforce all rules defined in `MoS_SSRN_Academic.md`.
   - Purge all algorithmic slop and academic filler (e.g., 'however', 'utilize', 'robust').
   - Eliminate predictable tricolons (X, Y, and Z) and robotic binary foils ("X rather than Y", "Instead of X, it is Y").
   - Enforce the absolute ban on em-dashes and colons in the narrative text. Verify that comma infrastructure has been deployed to prevent run-on sentences.
   - Maintain Plain English Precision; avoid convoluted academic jargon where simple mechanical explanation suffices.

2. **Redundancy Purge:**
   - Delete inappropriate sections, explicitly including any "Executive Summary" that overlaps with the Abstract or Introduction.

3. **Metadata Trimming (`.tex` file):**
   - Reduce Target eJournals to a maximum of 3 highly relevant journals.
   - Reduce JEL Classification Codes to a maximum of 5 core codes.

4. **Metadata Synchronization (`_Metadata.md` file):**
   - Copy the finalized Abstract verbatim from the `.tex` file into the corresponding archival `_Metadata.md` file to ensure absolute sync.
   - Mirror the trimmed Target eJournals and JEL Codes into the `_Metadata.md` file.

5. **Compilation and Cleanup:**
   - Execute the proper compilation sequence to process citations: `pdflatex file.tex`, followed by `bibtex file.aux`, followed by `pdflatex file.tex` twice.
   - Clean the directory of all intermediate build files (`.aux`, `.log`, `.out`, `.toc`, `.fls`, `.fdb_latexmk`, `.bbl`, `.blg`).
   - Commit the changes and push the repository to GitHub.
