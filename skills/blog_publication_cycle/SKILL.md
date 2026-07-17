---
name: blog_publication_cycle
description: Manages the end-to-end process of scanning remote publication dates, creating a new blog post, applying formatting styles, awaiting sysop approval, and deploying via git.
---
# Blog Publication Cycle

This skill defines the complete operational cycle for deploying new blog posts. This process guarantees chronological integrity, stylistic adherence, and Sysop auditability.

## Directory Map (Context)
The agent must be aware of the following directory structure within `/home/user0/git/publishing/100_blog/`:
*   `01_source/`: Raw input materials, research documents, and initial topic seeds drafted by the agent or provided by the Sysop.
*   `02_draft/`: Legacy processing directory.
*   `03_posted/`: Local tracking repository for deployed live assets and scheduled posts.
*   `05_img/`: Local image assets mapped for deployed posts (`webp` format).
*   `06_data/`: System configuration data (e.g., `tags.lang`).

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
1. **Source Document Acquisition:** Read the source document from `/home/user0/git/publishing/100_blog/01_source/` or ask the SYSOP to provide the text that will form the basis of the new blog post. Do not proceed until the source content is secured.
2. **Filename Protocol:** Construct the filename using the format `YYYY-MM-DD-HH-MM-SS_tags_title.md`. 
   *(Example: `2026-07-16-06-00-00_society,media,psychology,economics,technology_the-political-economy-of-narcissism.md`)*
3. **Directory Routing:** Write the new markdown file directly into the appropriate local `scheduled/` subdirectory (e.g., `blog/society/image/scheduled/`).
4. **Image Asset Generation (Optional):** If a library image is unavailable or inappropriate, use the `generate_image` tool to create a new asset. 
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
     - The first tag MUST be the primary category, strictly chosen from: society, skills, systems, money, nature, technology, adventure, health, history, or mind.
     - Include up to 5 additional secondary tags from `/home/user0/git/publishing/100_blog/06_data/tags.lang` (maximum 6 tags total).
   - Image: `<!--image [absolute URL] image-->` (If a new image was generated, map this exactly to `https://bikepaths.org/blog/content/images/webp/[filename].webp`)
   - **Line Break Mandate:** You MUST insert exactly one blank line between the final metadata tag and the first line of the narrative prose body.
2. **No Initial Headers:** NEVER initiate the narrative body with markdown headers (`#`, `##`, etc.). The text body must begin immediately following the metadata block as standard prose.
3. **Format Constraints (CMS Web Post):** 
   - Governed by `/home/user0/git/publishing/_styles/Publication_Formats.md`.
   - All markdown headings (`#`, `##`, `###`, `####`) are explicitly banned. Use ONLY bold text for section breaks.
   - Do not phoneticize numbers (e.g., use "1960", not "nineteen sixty").
4. **Stylistic Voice (Analytical OVP):** 
   - Governed by `/home/user0/git/publishing/_styles/MoS_Analytical_OVP.md`.
   - Apply the Smart Kitchen Table Test: enforce a C1 vocabulary ceiling (10,000 words). There is no upper limit on sentence length.
   - Ground all abstraction. Strip heavy academic and systemic jargon (e.g., replace "epistemological relativism" with "abandoning shared reality").
   - Eliminate all em-dashes (`—`), en-dashes (`–`), and semicolons.
   - Enforce organic asymmetry (variable sentence/paragraph lengths) and chronological fluidity (observable reality before systemic abstraction).

## Phase 4: Automated Linting and The Separation of State Mandate
1. **Automated Linter Execution:** Before requesting Sysop approval or executing any version control/deployment commands, the agent MUST run the custom Python linter against the active document:
   `python3 /home/user0/git/publishing/scripts/100_blog/mos_linter.py [target_file.md]`
   The linter dynamically parses the active MoS document for its banned word and phrase lists. To lint against a different MoS, pass it as the second argument:
   `python3 /home/user0/git/publishing/scripts/100_blog/mos_linter.py [target_file.md] [mos_file.md]`
2. **Mandatory Resolution:** The agent must execute consecutive mutative hardening passes until the linter returns a clean exit code (`0`).
3. **The Air Gap (TNMA Checkpoint):** Following a clean linter pass, the agent must halt all tool execution and enter **Discussion Mode (Take No Mutative Action)**. "TNMA" means the agent is explicitly forbidden from executing any file writes, terminal commands, version control operations, or deployment scripts. The agent may only use read-only tools (view_file, list_dir, grep_search) and must present the local changes to the Sysop for review.
   - **Command Bundling Ban:** The agent is explicitly forbidden from stringing local file edits, version control commands (`git commit`), and deployment scripts together in a single execution sequence.
   - **Image Review:** If a new image asset was generated, present the locally saved `.webp` file (`/home/user0/git/publishing/100_blog/05_img/webp/[filename].webp`) for Sysop visual approval before any deployment occurs.
4. **Anti-Diff Fog Mandate:** Present mutative hardening passes clearly. Do not bundle massive structural changes without explicit authorization.

## Phase 5: Primary VM Deployment and Version Control
Version control (`git commit/push`) and remote synchronization are restricted entirely to Phase 5. The agent cannot initiate this phase without an explicit, secondary Sysop command (e.g., "Execute deployment and sync").

Upon explicit Sysop deployment approval:
1. **Asset Deployment (If Generated):** Transfer the newly generated `.webp` image directly to the VM:
   `scp -P 2323 [output.webp] user0@165.232.151.110:/home/user0/www/bikepaths/html/blog/content/images/webp/`
2. **VM Source of Truth Deployment:** Deploy the markdown file directly to the primary VM using `scp` over port 2323. This guarantees the source of truth is updated first.
   *(Example: `scp -P 2323 /path/to/local/post user0@165.232.151.110:/home/user0/www/bikepaths/html/blog/content/chas/blog/[category]/[type]/scheduled/`)*
3. **Multi-Repository Git Mirroring:** Changes often span two separate repositories. Both must be committed and pushed independently:
   - **Content repository** (`/home/user0/git/bikepaths`): Contains blog posts and server sync data.
     `cd /home/user0/git/bikepaths && git add -A && git commit -m "[Action Summary]" && git push`
   - **Publishing repository** (`/home/user0/git/publishing`): Contains SKILL definitions, MoS documents, and tooling scripts.
     `cd /home/user0/git/publishing && git add -A && git commit -m "[Action Summary]" && git push`
   Only commit to repositories that contain actual changes.
4. **Global Synchronization:** After all git pushes are complete, execute the global sync script to trigger the atomic server-to-GitHub mirror and pull the latest state back to the local machine:
   `/home/user0/git/publishing/scripts/100_blog/sync_bikepaths_blog.sh`
   This script is mandatory. Without it, the VM Source of Truth and the GitHub mirror will remain desynchronized.
