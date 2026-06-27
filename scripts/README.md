# Full Spectrum Publishing Pipeline Scripting Architecture

This directory enforces a numerically sequenced hierarchy for all publishing automation scripts. Monolithic root-level scripts are strictly prohibited.

## Directory Hierarchy

* **`100_blog/`**: Automation for static HTML/CMS deployment, HTMLy integration, Markdown batch processing, and SSH/SCP synchronization protocols.
* **`200_amazon_kdp/`**: Conversion, compilation, and metadata structuring for Amazon Kindle Direct Publishing (EPUB, PDF generation).
* **`300_academic/`**: LaTeX compilation (`.tex`), citation management, and programmatic generation of journal submissions (e.g., SSRN, JSDH).
* **`400_networking/`**: Syndication, social distribution, RSS processing, and Web Intent/API generation for external platforms (e.g., X/Twitter).
* **`500_podcasts/`**: Audio processing, transcription pipelining, and media asset packaging.
* **`600_multimodal_pedagogy/`**: Multimodal visual processing, audio synchronization, and final MP4 video compilation workflows.
* **`skills/`**: Reusable generic functional logic and programmatic skill definitions.
* **`_archive/`**: Deprecated scripts, obsolete monoliths, and decommissioned infrastructure protocols.

