# 200_mdi Pre-Publication Cleanup Audit
## Status: AWAITING AUTHORIZATION
**Prepared:** May 2026 | **Scope:** /home/user0/git/publishing/200_mdi (recursive)

---

## CATEGORY A: ARCHIVE — Superseded Monolith Files

These files were the generative source at an earlier stage but are now fully superseded by the
granular chapter_drafts/ and epub_source.md pipeline. No unique content remains in them that
is not already present in the chapter files or epub_source.

| File | Size | Reason |
| :--- | :--- | :--- |
| `kdp/manuscript/full_manuscript.md` | 55KB | Superseded by epub_source.md (64KB, 430L vs 240L). epub_source is the EPUB generation source. full_manuscript is an intermediate monolith. |
| `Book_Two_Outline.md` | 4KB | Chapter outline. Fully realized in manifest.yaml + chapter_drafts/. Outline served its purpose. |

---

## CATEGORY B: ARCHIVE — Handoff Artifacts Post-Production

These files served the handoff-to-production workflow. Production directory is now staged and
these originals in handoff/ are redundant with what lives in production/.

| File | Size | Reason |
| :--- | :--- | :--- |
| `kdp/handoff/back_cover_copy.md` | 1.2KB | Copied (corrected) to production/. Original in handoff/ is stale (had $37B). |
| `kdp/handoff/metadata.yaml` | 1.7KB | Copied to production/. Handoff/ copy is the pre-staged version. |
| `kdp/handoff/the_architecture_of_survival.epub` | 541KB | Copied to production/. Handoff/ is the source. Retain ONE copy in production/ only. |
| `kdp/handoff/the_architecture_of_survival.docx` | 35KB | Not submitted to KDP (eBook-only launch). Intermediate format artifact. |
| `kdp/handoff/the_architecture_of_survival.pdf` | 217KB | Not submitted to KDP (eBook-only launch). Intermediate format artifact. |
| `kdp/handoff/cover_analysis_report.md` | 1.5KB | Analysis complete. Decision made (eBook-only). Report served its purpose. |
| `kdp/handoff/cover-image.png` | 2.9MB | Print-resolution cover. Print launch not selected. eBook cover (cover.jpg) is in production/. This file is dead weight at 2.9MB. |
| `kdp/handoff/cover.jpg` | 498KB | Copied to production/. Handoff/ copy redundant. |

---

## CATEGORY C: ARCHIVE — Pre-Engineering Research Artifacts

These files are the rhetorical and exploratory precursors that existed before the MDI engineering
language crystallized. Their content was absorbed into the manuscript. They are historical record,
not active assets.

| File | Size | Reason |
| :--- | :--- | :--- |
| `research/initial_thesis_framework.txt` | 4.9KB | Three-pillar rhetorical draft predating MDI engineering frame. Content surpassed by manuscript. |
| `research/homless_hell_article.txt` | 11.9KB | Raw article text used as inciting incident source. Cited in manuscript. Not an active asset. |
| `research/hud_encampment_evidence.txt` | 9.8KB | Raw HUD evidence notes. Incorporated into citations.md and manuscript. |
| `research/Book_Two_Thesis_Summary.md` | 2.2KB | Early thesis framing note. Superseded by full manuscript and metadata package. |
| `research/Book_Two_Narrative_Anchors.md` | 1.7KB | Location/timeline planning note from pre-draft phase. Superseded by manifest.yaml. |
| `research/academic_validation.md` | 1.2KB | 12-line stub. Content absorbed into manuscript Ch. 3 and citations.md. |

---

## CATEGORY D: RETAIN — Active Research Infrastructure

These files remain valuable as living research: citation sources, the agent initialization document
used by downstream systems, and the SSRN research series that feeds future papers.

| File | Size | Reason to Keep |
| :--- | :--- | :--- |
| `research/research.md` | 23KB | Primary MDI prose corpus. Feeds 300_survival_physics and 210_rdi. Not superseded. |
| `research/Housing_Event_Agent_Initialization.md` | 7.3KB | Active agent context document. Referenced by downstream work. |
| `research/Watchman_Analysis_Session_Handoff.md` | 9.4KB | Session context with corpus nomenclature, Google Drive IDs, publication timeline. Reference value intact. |
| `research/homelessness_thesis_findings.md` | 5.8KB | Evidence check document. Contains HUD/UCSF/USICH verified findings. Research infrastructure. |
| `research/ssrn/` (14 files) | — | Active SSRN research series. Feeds Paper 4 (RDI) and future submissions. |
| `kdp/manuscript/epub_source.md` | 64KB | AUTHORITATIVE manuscript source. EPUB generated from this. |
| `kdp/manuscript/chapter_drafts/` (15 files) | — | Granular chapter files. manifest.yaml assembles these into epub_source. |
| `kdp/manuscript/facts/` (15 files) | — | Per-chapter fact verification files. Active reference during any revision. |
| `kdp/manuscript/citations.md` | 8.6KB | Formatted citation block for all chapters. |
| `kdp/manuscript/copyright.md` | 694B | Live front matter component. |
| `kdp/manuscript/front_matter.md` | 1.9KB | Live front matter component. |
| `kdp/manuscript/manifest.yaml` | 2.4KB | EPUB assembly specification. |
| `kdp/manuscript/epub_style.css` | 4.1KB | EPUB stylesheet. |
| `kdp/manuscript/flowchart.mmd` | 2.6KB | Mermaid source for framework flowchart. |
| `kdp/handoff/framework_flowchart.png` | 198KB | Rendered flowchart. Interior asset candidate. |
| `kdp/handoff/framework_flowchart.svg` | 64KB | SVG source for flowchart. |
| `kdp/handoff/kdp_strategy.md` | 966B | Launch strategy doc. Still active (pricing, Select enrollment). |
| `kdp/MDI_Amazon_Metadata_Package.md` | 7.7KB | Master metadata document. Active. |
| `README.md` | — | Project README. |
| `production/` (6 files) | — | Staged submission assets. Do not touch. |

---

## PROPOSED ARCHIVE STRUCTURE

All Category A and B and C files move to:
`/home/user0/git/publishing/200_mdi/_archive/`

Subdirectories:
- `_archive/monolith_drafts/` — Category A
- `_archive/handoff_artifacts/` — Category B
- `_archive/pre_engineering_research/` — Category C

Nothing is deleted. Archive preserves full provenance.

---

## EXECUTION SUMMARY

| Category | Files | Action |
| :--- | :--- | :--- |
| A — Superseded Monoliths | 2 files | Move to _archive/monolith_drafts/ |
| B — Handoff Artifacts | 8 files | Move to _archive/handoff_artifacts/ |
| C — Pre-Engineering Research | 6 files | Move to _archive/pre_engineering_research/ |
| D — Retain | All others | No action |

**Total files to archive: 16**
**Largest single file removed from active tree: cover-image.png (2.9MB)**

---
*Awaiting EXECUTE authorization before any file operations.*
