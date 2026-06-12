# Project Handoff Instructions: The Moral Physics of Survival

This document outlines the state, constraints, and operational procedures for *The Moral Physics of Survival* publishing project.

## 1. Project Context and Objectives
The objective of this project is to publish the book *The Moral Physics of Survival* by Charles J. DiBella. The workspace is located at `/home/user0/git/publishing/200_amazon_kdp/03_survival_physics`.

## 2. Directory Structure
All manuscript files and assets are organized as follows:
- **`kdp/manuscript/`**: Root folder containing manifest, styles, and compiled files.
- **`kdp/manuscript/chapter_drafts/`**: Subfolder with the raw chapter drafts (Prologue and Chapters 1 to 13).
- **`kdp/manuscript/epub_source.md`**: Assembled source file for EPUB compilation.
- **`kdp/manuscript/full_manuscript.md`**: Assembled source file for DOCX print compilation.
- **`kdp/handoff/`**: Output directory for compiled binaries (`the_moral_physics_of_survival.epub` and `the_moral_physics_of_survival.docx`).
- **`scripts/200_amazon_kdp/03_survival_physics/`**: Contains verification scripts.

## 3. Style Guide Constraints
The manuscript must adhere strictly to the custom Style Manual. The key rules are:
- **Punctuation**: Semicolons and colons are highly restricted. Em-dashes are completely prohibited. Parenthetical phrases are completely prohibited.
- **Lexicon**: Academic clichés and simplistic transition words (e.g., *furthermore*, *mitigate*, *leverage*, *actionable*, *holistic*) are prohibited.
- **Verification**: Always run the style checker script before building the book.
  ```bash
  python3 /home/user0/git/publishing/scripts/200_amazon_kdp/03_survival_physics/check_all_styles.py
  ```

## 4. Compilation Pipeline

### EPUB Generation
1. Re-assemble the source file using the manifest:
   ```bash
   python3 /home/user0/git/publishing/_epub/epub_assembly.py --manifest manifest.yaml --output epub_source.md
   ```
2. Compile the EPUB binary via Pandoc:
   ```bash
   pandoc epub_source.md --from markdown+smart --to epub3 \
     --output ../handoff/the_moral_physics_of_survival.epub \
     --css epub_style.css \
     --epub-cover-image ../handoff/cover.jpg \
     --toc --toc-depth=1 --split-level=1 \
     --metadata title="The Moral Physics of Survival" \
     --metadata author="Charles J. DiBella" \
     --metadata lang="en-US"
   ```
3. Validate the EPUB package:
   ```bash
   python3 -c "from epubcheck import EpubCheck; result = EpubCheck('../handoff/the_moral_physics_of_survival.epub'); print('Valid:', result.valid); print('Messages:', len(result.messages))"
   ```

### DOCX Generation
1. Concatenate all source files in the manifest sequence:
   ```bash
   cat copyright.md front_matter.md chapter_drafts/prologue_the_bridge.md chapter_drafts/chapter_01_the_inventory_of_failure.md chapter_drafts/chapter_02_the_vocabulary_of_invisibility.md chapter_drafts/chapter_03_the_biological_floor.md chapter_drafts/chapter_04_what_a_person_is.md chapter_drafts/chapter_05_the_is_ought_problem_and_why_it_matters.md chapter_drafts/chapter_06_the_social_contracts_hidden_assumption.md chapter_drafts/chapter_07_natural_law_without_god.md chapter_drafts/chapter_08_the_hierarchy_of_obligation.md chapter_drafts/chapter_09_institutional_capture_and_moral_responsibility.md chapter_drafts/chapter_10_the_legitimacy_of_compelled_care.md chapter_drafts/chapter_11_john_snow_and_the_moral_physicist.md chapter_drafts/chapter_12_the_remnant_and_the_obligation.md chapter_drafts/chapter_13_a_different_starting_point.md citations.md > full_manuscript.md
   ```
2. Compile the DOCX print binary:
   ```bash
   pandoc full_manuscript.md -o ../handoff/the_moral_physics_of_survival.docx --from markdown
   ```

## 5. Recent Modifications Completed
1. Formatted book titles to uppercase italics (e.g., *After Virtue*).
2. Defined Material Dignity Infrastructure (MDI) inline in Chapter 8 as a clinical-housing model.
3. Added the DiBella (2026) Working Paper citation under Chapter 8 and Chapter 10 in `citations.md`.
4. Synchronized all modifications across `epub_source.md` and `full_manuscript.md`.
5. Built and validated the EPUB and DOCX binaries.
6. Pushed all modifications to the remote origin main branch.

## 6. Current User Context
The user has been drafting parables and message responses in `/home/user0/git/private/telegram/drafting/naiya_3.md`. This file contains drafts analyzing therapeutic considerations, childhood instability, andPositive Psychology assessments. Maintain alignment with these drafts if requested to generate related content.
