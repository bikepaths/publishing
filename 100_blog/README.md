# 100_blog: Publishing Pipeline Root

This directory serves as the primary processing pipeline for systemic blog synthesis and deployment. 

## Directory Map
*   `01_source/`: Raw input materials, research documents, and topic seeds.
*   `02_draft/`: Active synthesis manuscripts. Must use `_DRAFT.md` suffix.
*   `05_img/`: Local image assets for deployed posts.
*   `06_data/`: System configuration data (e.g., `tags.lang`).

## Composition Authorities
**DO NOT use this README for stylistic or structural generative rules.** 
All blog synthesis is strictly governed by external knowledge items and baseline documents:
1.  **Master Manual of Style:** Located at `_styles/MoS_Systemic_Analysis.md`.
2.  **Systemic Analysis KI:** Active agent constraint parameters.

## Metadata & Verification
All draft posts must clear the automated `scripts/100_blog/verify_blog_post.py` pipeline before deployment.

Required metadata tags block (embed as HTML comments anywhere in file):
`<!--t [Exact Title] t-->`
`<!--d [Meta Description] d-->`
`<!--tag [primary_category,tag2,tag3] tag-->`
`<!--image [image_filename.jpg or URL] image-->`

*   **Tags:** Must contain exactly 1 primary category followed by up to 5 optional tags (max 6 total).
*   **Primary Categories:** `society`, `skills`, `systems`, `money`, `nature`, `technology`, `adventure`, `health`, `history`, `mind`.
*   **Filename Format (Deployment):** `YYYY-MM-DD-HH-MM-SS_tags_slug.md`.
