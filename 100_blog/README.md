# 100_blog: Publishing Pipeline Root

This directory serves as the primary processing pipeline for systemic blog synthesis and deployment. 

## Directory Map
*   `01_source/`: Raw input materials, research documents, and topic seeds.
*   `02_draft/`: Active synthesis manuscripts. Must use `_DRAFT.md` suffix for pipeline targeting.
*   `03_posted/`: Local tracking repository for deployed live assets and scheduled posts.
*   `05_img/`: Local image assets mapped for deployed posts.
*   `06_data/`: System configuration data (e.g., `tags.lang`).

## Pipeline Architecture

The processing architecture has been fully decoupled into a modular 3-script sequence to ensure the Sysop can manually verify files in the IDE before advancing to the next stage.

### 1. Generation Layer
**`scripts/100_blog/01_generate.sh`**
Acts as the synthesis entry point. Reads a RAW file, interacts with OpenRouter API to generate the draft, automatically calculates 24-hour sequential scheduling, and optionally generates/converts WebP assets.

### 2. Verification Layer
**`scripts/100_blog/02_verify.sh`**
Runs the validation suite (`verify_syntax.py`, `verify_metadata.py`, `verify_blog_post.py`) and structural transformations on the generated `_DRAFT.md` file. The execution halts completely after this script to force manual Sysop review in the IDE.

### 3. Deployment Layer
**`scripts/100_blog/03_deploy.sh`**
Executes remote Secure Copy (SCP) transfers, creates missing remote directories, relocates local staging files into `03_posted/`, purges legacy redundant drafts, clears the remote CMS cache directory, and invokes the bidirectional `sync_bikepaths_blog.sh` synchronizer.

---

## Step-by-Step Processing Sequence

1.  **Draft Initialization**: Place target raw content into `02_draft/` ending with `_RAW.md`.
2.  **Synthesis**: Execute `./scripts/100_blog/01_generate.sh 100_blog/02_draft/[filename]_RAW.md`.
3.  **Visual Audit I**: Sysop manually inspects the newly generated `_DRAFT.md` file in the IDE, verifying the scheduled date and narrative format.
4.  **Automated Verification**: Execute `./scripts/100_blog/02_verify.sh 100_blog/02_draft/[filename]_DRAFT.md`.
5.  **Visual Audit II**: Sysop manually inspects the `_DRAFT.md` file in the IDE for any syntax changes or metadata corrections applied during verification.
6.  **Remote Deployment**: Execute `./scripts/100_blog/03_deploy.sh 100_blog/02_draft/[filename]_DRAFT.md`.
7.  **Global Synchronization**: `03_deploy.sh` automatically triggers `sync_bikepaths_blog.sh` locking remote state into GitHub version control and mirroring to local repository.

---

## Composition Authorities
**DO NOT use this README for stylistic or structural generative rules.** 
All blog synthesis is strictly governed by external knowledge items and baseline documents:
1.  **Master Manual of Style:** Located at `_styles/MoS_Systemic_Analysis.md`.
2.  **Systemic Analysis KI:** Active agent constraint parameters.

## Metadata Requirements
Required metadata tags block (embed as HTML comments anywhere in file):
`<!--t [Exact Title] t-->`
`<!--d [Meta Description] d-->`
`<!--tag [primary_category,tag2,tag3] tag-->`
`<!--image [image_filename.jpg or URL] image-->`

*   **Tags:** Must contain exactly 6 tags (1 primary category followed by exactly 5 sub-tags).
*   **Primary Categories:** `society`, `skills`, `systems`, `money`, `nature`, `technology`, `adventure`, `health`, `history`, `mind`.
