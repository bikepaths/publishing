# 100_blog: Publishing Pipeline Root

This directory serves as the primary processing pipeline for systemic blog synthesis and deployment. 

## Directory Map
*   `01_source/`: Raw input materials, research documents, and initial topic seeds drafted by the agent or provided by the Sysop.
*   `02_draft/`: Active synthesis manuscripts. (Legacy processing directory, mostly superseded by direct scheduling deployment).
*   `03_posted/`: Local tracking repository for deployed live assets and scheduled posts.
*   `05_img/`: Local image assets mapped for deployed posts (`webp` format).
*   `06_data/`: System configuration data (e.g., `tags.lang`).

## Pipeline Architecture (Agentic AI Workflow)

The processing architecture is governed by the `blog_publication_cycle` skill. The pipeline has been fully modernized for AI-driven, dual-level communication, requiring explicit Sysop authorization to cross the air gap between drafting and deployment.

**For full operational instructions, the agent MUST read: `/home/user0/git/publishing/skills/blog_publication_cycle/SKILL.md`**

### The 5-Phase Processing Sequence

1.  **Phase 1: Remote State Discovery**: The agent scans the remote server via SSH to determine the next chronological deployment slot.
2.  **Phase 2: Post Instantiation**: The agent reads the source text from `01_source/`, constructs the correct filename, and generates any required `.webp` image assets in `05_img/webp/`.
3.  **Phase 3: Stylistic Hardening**: The agent enforces formatting and applies the strict "Smart Kitchen Table" constraints (Analytical OVP).
4.  **Phase 4: Automated Linting**: The agent runs `mos_linter.py`. The execution halts completely after this phase (Discussion Mode) to force manual Sysop review in the IDE.
5.  **Phase 5: Primary VM Deployment**: Upon explicit Sysop command, the agent executes SCP transfers, mirrors to GitHub, and invokes the bidirectional `sync_bikepaths_blog.sh` synchronizer.

*(Note: Legacy bash scripts like `01_generate.sh`, `02_verify.sh`, and `03_deploy.sh` remain in `scripts/100_blog/` as manual fallbacks but are not used in the primary agentic workflow).*

---

## Composition Authorities
**DO NOT use this README for stylistic or structural generative rules.** 
All blog synthesis is strictly governed by external knowledge items and baseline documents:
1.  **Master Manual of Style:** Located at `_styles/MoS_OVP_specification.md` (Section 3.1 — Format 1: CMS Web Post). This is the authoritative governing document for all web post generation.
2.  **Systemic Analysis KI:** Active agent constraint parameters.

## Metadata Requirements
Required metadata tags block (embed as HTML comments anywhere in file):
`<!--t [Exact Title] t-->`
`<!--d [Meta Description] d-->`
`<!--tag [primary_category,tag2,tag3] tag-->`
`<!--image [image_filename.jpg or URL] image-->`

*   **Tags:** Must contain exactly 6 tags (1 primary category followed by exactly 5 sub-tags).
*   **Primary Categories:** `society`, `skills`, `systems`, `money`, `nature`, `technology`, `adventure`, `health`, `history`, `mind`.
