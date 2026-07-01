# 100_blog: Publishing Pipeline Root

This directory serves as the primary processing pipeline for systemic blog synthesis and deployment. 

## Directory Map
*   `01_source/`: Raw input materials, research documents, and topic seeds.
*   `02_draft/`: Active synthesis manuscripts. Must use `_DRAFT.md` suffix for pipeline targeting.
*   `03_posted/`: Local tracking repository for deployed live assets and scheduled posts.
*   `05_img/`: Local image assets mapped for deployed posts.
*   `06_data/`: System configuration data (e.g., `tags.lang`).

## Pipeline Architecture

The monolithic processing architecture has been disassembled into a decoupled, modular sequence orchestrated via `pipeline_orchestrator.sh`.

### 1. Global Orchestrator
**`scripts/100_blog/pipeline_orchestrator.sh`**
Acts as the central entry point. Enforces sequential execution, manages hard-stop validation failures, and mandates manual Sysop authorization prior to production deployment.

### 2. Transformation Layer
**`scripts/100_blog/transform_draft.py`**
Applies baseline structural and syntactic transformations to raw drafts. Executes OVP compliance modifications (e.g., merging staccato sentences, replacing prohibited framework terminology) preparing the draft for verification.

### 3. Verification Layer
*   **`scripts/100_blog/verify_syntax.py`**: Validates document readability (Flesch-Kincaid targets), sentence length ceilings (22-word limit), and style compliance.
*   **`scripts/100_blog/verify_metadata.py`**: Audits HTML metadata comment blocks ensuring taxonomy adherence, timestamp accuracy, and required schema structures.

### 4. Deployment Layer
**`scripts/100_blog/deploy_asset.py`**
Executes remote Secure Copy (SCP) transfers, creates missing remote directories, relocates local staging files into `03_posted/`, purges legacy redundant drafts, and clears the remote CMS cache directory.

### 5. Synchronization Layer
**`scripts/100_blog/sync_bikepaths_blog.sh`**
Bidirectional global synchronizer. Pushes terminal virtual machine state to GitHub origin, then pulls changes into the local working directory guaranteeing global state parity.

---

## Step-by-Step Processing Sequence

1.  **Draft Synthesis**: Place target draft into `02_draft/` ensuring filename ends with `_DRAFT.md`. Include required metadata comment blocks.
2.  **Pipeline Initialization**: Execute `./scripts/100_blog/pipeline_orchestrator.sh 100_blog/02_draft/[filename]_DRAFT.md`.
3.  **Automated Transformation**: Orchestrator triggers `transform_draft.py` modifying active file.
4.  **Automated Verification**: Orchestrator triggers `verify_syntax.py` and `verify_metadata.py`. Any failure initiates a hard stop requiring manual remediation.
5.  **Sysop Authorization Gate**: Execution halts. Orchestrator prompts: `Deploy [file] to production? (y/N)`. Sysop must manually audit and authorize.
6.  **Remote Deployment**: `deploy_asset.py` transfers file to VM, relocates local tracking asset to `03_posted/`, and purges cached web assets.
7.  **Global Synchronization**: Orchestrator triggers `sync_bikepaths_blog.sh` locking remote state into GitHub version control and mirroring to local repository.

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

*   **Tags:** Must contain exactly 1 primary category followed by up to 5 optional tags (max 6 total).
*   **Primary Categories:** `society`, `skills`, `systems`, `money`, `nature`, `technology`, `adventure`, `health`, `history`, `mind`.
