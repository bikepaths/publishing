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

## Operational Mandates
1. **View Before Touch Mandate:** The agent MUST execute `view_file` on target files prior to editing.
2. **Skill Verification Mandate:** The agent MUST execute `view_file` on this SKILL document phase immediately prior to execution.
3. **Semantic Reconciliation Mandate:** When modifying core metrics or variables, the agent MUST perform a full document semantic cross-reference audit.
4. **Level One Communication Standard:** The agent MUST use plain simple language, direct tone, and propose the next three actions.
5. **Absolute Path Mandate:** The agent MUST ALWAYS use absolute paths (`/home/user0/...`).
6. **Pipeline Push Mandate:** The agent MUST immediately execute a `git push` to the remote repository whenever modifying anything in `/home/user0/git/publishing/`.

## Phase 1: Remote State Discovery (Date Scanning)
Before creating any new content, the agent MUST determine the current chronological deployment sequence.
1. Use `run_command` to execute a script or command to list the remote blog directory over SFTP/SSH. You MUST extract and sort exclusively by the filename timestamp to avoid alphabetical path-sorting errors.
   *(Example: `ssh -p 2323 user@[ip] 'find /path/to/blog -type f -name "*.md" -exec basename {} \; | sort'`)*
2. Recursively scan the target directories across all categories.
3. Identify three critical timestamp markers:
   - **Last Published:** The most recent date in the live directories.
   - **Last Scheduled:** The furthest date in the `scheduled/` directories.
   - **Next Scheduled:** The immediate next chronological opening.
4. Calculate the target date for the new post based on the sequential schedule. Compare this generated date against the current system date. If the remote date is in the past, the current system date must become the baseline.

## Phase 1.5: Source Document Analysis
1. **MoS Mapping:** The agent MUST analyze the source text against all available styles in `_styles/` to determine the closest stylistic match.
2. **MoS Query Mandate:** The agent MUST query the Sysop with the suggested best-fit MoS and await explicit authorization before proceeding to file creation.

## Phase 2: Generative Synthesis and Asset Creation
1. **Source Document Acquisition:** Read the source document from `/home/user0/git/publishing/100_blog/01_source/` or ask the SYSOP to provide the text. Do not proceed until the source content is secured.
2. **Generative Rewrite:** The agent MUST execute a comprehensive generative rewrite of the source text. The source document is RAW MATERIAL, not a template. Do NOT passively copy, paraphrase, or lightly rearrange the source text. The agent must:
   - **Determine authorial intent:** Before writing, identify the core thesis the author is attempting to convey to the reader. The rewrite must optimally express that thesis.
   - **Write in the third person:** All blog posts use a third-person objective voice. Never use "you" or "your" to address the reader. Never use first person ("I", "we").
   - **Subordinate framing devices:** If the source uses a character, avatar, or narrative framing device (e.g., "imagine you are a student"), that device must be subordinated. The systemic argument carries the post. The character appears sparingly as a lens, not as the protagonist of every paragraph.
   - **Reference Post (Gold Standard):** Before writing, the agent MUST read the most recent file in `/home/user0/git/publishing/100_blog/03_posted/` and use its voice, register, paragraph geometry, and sentence variance as the structural model for the new post.
3. **Filename Protocol:** Construct the filename using the format `YYYY-MM-DD-HH-MM-SS_tags_semantic-seo-slug.md`.
   - **Semantic SEO Slug:** The filename slug MUST contain semantic SEO terms related to the topic and title (e.g., `urban-homelessness-infrastructure-systems-failure-infinite-loop.md`), rather than just a literal lowercase copy of the title. This optimizes for search discovery.
4. **Directory Routing:** Write the newly synthesized markdown file into the `/home/user0/git/publishing/100_blog/02_draft/` directory. Do not write directly to `03_posted/`.
5. **Image Asset Generation (Optional):** If a library image is unavailable or inappropriate, use the `generate_image` tool to create a new asset.
   - **Prompt Protocols:** The prompt MUST specify: "The image must be a real-world photograph of full-scale architecture, actual humans, or real environments. The subject must be perfectly centered on both axes, and the top 30% and bottom 30% of the image must be dead blur." You MUST explicitly forbid adding uncentered environmental elements (like ground landscapes or skies) that shift the vertical center of mass away from the exact geometric center. You MUST explicitly forbid scale models, miniatures, dioramas, blueprints, abstract graphics, and 3D renders.
   - **Asset Cleanup Mandate:** If an image generation is rejected by the Sysop or aborted, the agent MUST immediately delete the rejected `.webp` and `.png` files from the local directories before continuing.
   - **Semantic Naming:** Name the file using exactly four descriptive visual keywords separated by underscores (e.g., `urban_solar_radiation_man.png`).
   - **Image Processing:** Convert and crop the generated `.png` artifact to a 956x444 centered `.webp` image. For a 1024x1024 source image, use these exact parameters:
     `cwebp -crop 34 290 956 444 -q 60 -m 6 [keyword1_keyword2_keyword3_keyword4.png] -o /home/user0/git/publishing/100_blog/05_img/webp/[keyword1_keyword2_keyword3_keyword4.webp]`

## Phase 3: Stylistic Hardening
All blog posts MUST adhere to the formatting and stylistic constraints of the authorized MoS.
1. **Metadata Frontmatter:** The document must begin EXACTLY with these metadata lines, using HTML comment syntax:
   - Title: `<!--t [Title] t-->`
   - Description: `<!--d [One-sentence description] d-->`
   - Tags: `<!--tag [comma-separated tags] tag-->`
     - The first tag MUST be the primary category, strictly chosen from: society, skills, systems, money, nature, technology, adventure, health, history, or mind.
     - Include exactly 5 additional secondary tags from `/home/user0/git/publishing/100_blog/06_data/tags.lang` (exactly 6 tags total).
   - Image: `<!--image [absolute URL] image-->` (If a new image was generated, map this exactly to `https://bikepaths.org/blog/content/images/webp/[filename].webp`)
   - **Line Break Mandate:** You MUST insert exactly one blank line between the final metadata tag and the first line of the narrative prose body.
2. **No Initial Headers:** NEVER initiate the narrative body with markdown headers (`#`, `##`, etc.). The text body must begin immediately following the metadata block as standard prose.
3. **Format Constraints (CMS Web Post):**
   - Governed by `/home/user0/git/publishing/_styles/Publication_Formats.md`.
   - All markdown headings (`#`, `##`, `###`, `####`) are explicitly banned. Use ONLY bold text for section breaks.
   - **Header Spacing Mandate:** Bold headers MUST be isolated by exactly one blank line above and one blank line below. Text must never stack directly against a header.
   - Do not phoneticize numbers (e.g., use "1960", not "nineteen sixty").
   - **No Glossary:** Blog posts do not include glossary sections. Define terms inline within the prose.
   - **No Chapters:** The document is a singular blog post, not a book. Never use the word "Chapter" in headers.
4. **Stylistic Voice (Dynamic OVP):**
   - Governed dynamically by the Sysop-authorized MoS document from `_styles/`.
   - The agent MUST strictly enforce the constraints of the authorized MoS (e.g., vocabulary ceilings, punctuation bans, avatar permissions).
   - Apply the Smart Kitchen Table Test: enforce a C1 vocabulary ceiling (10,000 words). There is no upper limit on sentence length.
   - Ground all abstraction. Strip heavy academic and systemic jargon (e.g., replace "epistemological relativism" with "abandoning shared reality").
   - Eliminate all em-dashes (`—`), en-dashes (`–`), and semicolons.
   - **Professional Metadata:** Titles and descriptions must function as compelling intellectual hooks, not lazy, literal summaries.
     - BAD TITLE: "A Robotics Student Analyzes Homelessness" (lazy, literal)
     - GOOD TITLE: "The Infinite Loop: Why Cities Keep Crashing on Homelessness" (intellectual hook)
     - BAD DESCRIPTION: "An analysis of urban policy failures." (vague, generic)
     - GOOD DESCRIPTION: "Urban homelessness operates as a sequential dependency failure, and the fix requires an engineering specification that most politicians refuse to follow." (specific, provocative)
   - **Organic Asymmetry (Human Composition):** The text MUST read like a human wrote it. This means:
     - **Shatter formulaic loops.** Never repeat the same structural pattern across sections. If one section opens with a short declarative statement, the next must open with a long flowing thought or a counterargument.
     - BAD PATTERN (machine-like): Every section follows Header → single-sentence thesis → explanatory block → single-sentence closer. This is robotic.
     - GOOD PATTERN (human-like): One section opens mid-argument. The next opens with data. Another opens by refuting a common assumption. The reader cannot predict the next paragraph's shape.
     - **Vary sentence length aggressively.** Bridge long, flowing thoughts using subordinating conjunctions ("Although", "Because", "While") and abruptly punctuate them with short, hard declarative statements. Consecutive sentences must rarely share the same length or identical subject-verb opening structures.
     - **Vary paragraph length.** Mix short two-sentence paragraphs with longer four-sentence blocks. Never stack identically-sized paragraphs consecutively.

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
   - The path format is: `/home/user0/www/bikepaths/html/blog/content/chas/blog/[category]/[type]/scheduled/`
   - **`[type]` Routing Rule:** If the markdown file contains an image tag (`<!--image ... image-->`), `[type]` MUST be `image`. If it does not contain an image, `[type]` MUST be `post`.
   - *(Example: `scp -P 2323 /path/to/local/post user0@165.232.151.110:/home/user0/www/bikepaths/html/blog/content/chas/blog/systems/image/scheduled/`)*
3. **Multi-Repository Git Mirroring:** Changes often span two separate repositories. Both must be committed and pushed independently:
   - **Content repository** (`/home/user0/git/bikepaths`): Contains blog posts and server sync data.
     `cd /home/user0/git/bikepaths && git add -A && git commit -m "[Action Summary]" && git push`
   - **Publishing repository** (`/home/user0/git/publishing`): Contains SKILL definitions, MoS documents, and tooling scripts.
     `cd /home/user0/git/publishing && git add -A && git commit -m "[Action Summary]" && git push`
   Only commit to repositories that contain actual changes.
4. **Global Synchronization:** After all git pushes are complete, execute the global sync script to trigger the atomic server-to-GitHub mirror and pull the latest state back to the local machine:
   `/home/user0/git/publishing/scripts/100_blog/sync_bikepaths_blog.sh`
   This script is mandatory. Without it, the VM Source of Truth and the GitHub mirror will remain desynchronized.
