# Skill: Initialize Blog Post

## Primary Directives

1. **Agent Selection Matrix**: Systems must route operations based on complexity thresholds:
    - Writing / Analysis -> Claude Sonnet 4.6 (Thinking)
    - Complex / Long-document tasks -> Claude Opus 4.6 (Thinking)
    - Rapid Image/PDF/Multi-source processing -> Gemini 3.5 Flash (High)
    - Fallback -> GPT-OSS 120B (Medium)
2. **Remote Asset Verification**: When processing files containing `<!--image [URL] image-->` metadata, systems must scan local `img/` directories for matching filenames. If local files remain absent, systems must execute `wget` targeting the specific remote URL before initiating synchronization protocols. If no reference image is found, assign `/home/user0/git/publishing/100_blog/img/visuals-334.jpg` as the fallback image.
3. **Deployment Architecture**: `/usr/local/bin/bikepaths-sync` operates as the mandatory global synchronization trigger.
4. **Strict Path Routing**: The `100_blog/` directory functions as an isolated development environment containing designated partitions:
    - `draft/` serves as the active working directory.
    - `posted/` houses final compiled and deployed posts.
    - `source/` holds facts, data, and notes during development.
    - `archive/` acts as the repository for legacy monoliths and retired source materials.
    - `data/` contains tag metadata (`tags.lang`) and page views (`views.json`).
5. **State Transition Lifecycle**: Upon successfully compiling and deploying a post to `posted/`, all corresponding research, outlines, and raw materials inside `source/` must be moved to `archive/`. If a post requires revision, systems must copy the existing file from `posted/` into `draft/` with a `_DRAFT.md` suffix. Upon compilation of the revised draft, systems must move the prior posted file to `archive/revised_posts/` before promoting the new version to `posted/`.
6. **Template Supremacy**: The `skills/` directory dominates all operational processes. Generated content must map against `_template` structures while awaiting finalization of the Manual of Style (`_style`).
7. **Verification and Approval Lifecycle**: Operations must halt twice to acquire explicit Sysop validation. First, systems must secure alignment on proposed edits before making revisions. Second, final server synchronization requires visual inspection of all completed textual diffs.



