---
name: blog_publication_cycle
description: Manages the end-to-end process of scanning remote publication dates, creating a new blog post, applying formatting styles, awaiting sysop approval, and deploying via git.
---
# Blog Publication Cycle

This skill defines the complete operational cycle for deploying new blog posts. This process guarantees chronological integrity, stylistic adherence, and Sysop auditability.

## Phase 1: Remote State Discovery (Date Scanning)
Before creating any new content, the agent MUST determine the current chronological deployment sequence.
1. Use `run_command` to execute a script or command to list the remote blog directory over SFTP/SSH: `sftp://[user]@[ip]:[port]/[path/to/blog]`. 
   *(Example: `sftp://user0@165.232.151.110:2323/home/user0/www/bikepaths/html/blog/content/chas/blog`)*
2. Recursively scan the target directories (e.g., `society/image/`, `society/post/`) and their `scheduled/` subdirectories.
3. Identify three critical timestamp markers:
   - **Last Published:** The most recent date in the live directories.
   - **Last Scheduled:** The furthest date in the `scheduled/` directories.
   - **Next Scheduled:** The immediate next chronological opening.
4. Calculate the target date for the new post based on the sequential schedule.

## Phase 2: Post Instantiation (File Creation and Assets)
1. **Filename Protocol:** Construct the filename using the format `YYYY-MM-DD-HH-MM-SS_tags_title.md`. 
   *(Example: `2026-07-16-06-00-00_society,media,psychology,economics,technology_the-political-economy-of-narcissism.md`)*
2. **Directory Routing:** Write the new markdown file directly into the appropriate local `scheduled/` subdirectory (e.g., `blog/society/image/scheduled/`).
3. **Image Asset Generation (Optional):** If a library image is unavailable or inappropriate, use the `generate_image` tool to create a new asset. 
   - **Prompt Protocols:** All generated visual assets must use descriptive prompts explicitly requiring wide, landscape, or 16:9 cinematic compositions to maximize horizontal interface geometry. (e.g., Include keywords: "16:9, landscape, cinematic composition").
   - **Semantic Naming:** Name the file using exactly four descriptive visual keywords separated by underscores, mapping the physical contents of the image rather than the document topic (e.g., `urban_solar_radiation_man.png`).
   - Convert and crop the generated `.png` artifact to a `.webp` landscape image using the exact parameters, saving it locally for review: 
     `cwebp -crop 0 192 1024 640 -q 80 [keyword1_keyword2_keyword3_keyword4.png] -o /home/user0/git/publishing/100_blog/05_img/webp/[keyword1_keyword2_keyword3_keyword4.webp]`

## Phase 3: Stylistic Hardening
All blog posts MUST adhere to the following strict formatting and stylistic constraints:
1. **Metadata Frontmatter:** The document must begin EXACTLY with these metadata lines, using HTML comment syntax:
   - Title: `<!--t [Title] t-->`
   - Description: `<!--d [One-sentence description] d-->`
   - Tags: `<!--tag [comma-separated tags] tag-->`
   - Image: `<!--image [absolute URL] image-->` (If a new image was generated, map this exactly to `https://bikepaths.org/blog/content/images/webp/[filename].webp`)
2. **No Initial Headers:** NEVER initiate the narrative body with markdown headers (`#`, `##`, etc.). The text body must begin immediately following the metadata block as standard prose.
3. **Format Constraints (CMS Web Post):** 
   - Governed by `/home/user0/git/publishing/_styles/Publication_Formats.md`.
   - Markdown headings `#`, `##`, and `###` are explicitly banned throughout the entire document. Use only `####` or bold text for section breaks.
   - Do not phoneticize numbers (e.g., use "1960", not "nineteen sixty").
4. **Stylistic Voice (OVP):** 
   - Governed by `/home/user0/git/publishing/_styles/MoS_OVP_Organic_Vernacular_Pedagogy.md`.
   - Apply the Kitchen Table Test: use B2+ plain spoken English. Strip all academic and systemic jargon (e.g., replace "mechanical inversion" with "flipped upside down").
   - Eliminate all em-dashes (`—`), en-dashes (`–`), and semicolons.
   - Enforce organic asymmetry (variable sentence/paragraph lengths) and chronological fluidity (observable reality before systemic abstraction).

## Phase 4: Sysop Handshake and Authorization
1. **Discussion Mode Default (TNMA):** Following the initial content generation or structural refactoring plan, the agent must pause and present the proposed text or plan to the Sysop. Take No Mutative Action (TNMA) regarding final commits or styling replacements until authorized.
   - **Image Review:** If a new image asset was generated, present the locally saved `.webp` file (`/home/user0/git/publishing/100_blog/05_img/webp/[filename].webp`) for Sysop visual approval before any deployment occurs.
2. **Anti-Diff Fog Mandate:** Present mutative hardening passes (e.g., converting Systemic Analysis to OVP) clearly. Do not bundle massive structural changes without explicit authorization.
3. **Trigger Verification:** Wait for the explicit Sysop command (e.g., "EXECUTE OVP hardening") before modifying the active document.

## Phase 5: Primary VM Deployment and Version Control
Upon Sysop approval and successful file modification:
1. **Asset Deployment (If Generated):** Transfer the newly generated `.webp` image directly to the VM:
   `scp -P 2323 [output.webp] user0@165.232.151.110:/home/user0/www/bikepaths/html/blog/content/images/webp/`
2. **VM Source of Truth Deployment:** Deploy the markdown file directly to the primary VM using `scp` over port 2323. This guarantees the source of truth is updated first.
   *(Example: `scp -P 2323 /path/to/local/post user0@165.232.151.110:/home/user0/www/bikepaths/html/blog/content/chas/blog/[category]/[type]/scheduled/`)*
2. **Secondary Git Mirroring:** Once VM deployment is confirmed, execute the git cycle in the project root to update the GitHub/Vercel mirror:
   `git add -A && git commit -m "[Action Summary]" && git push`
