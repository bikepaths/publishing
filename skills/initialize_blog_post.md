# Skill: Initialize Blog Post

## Primary Directives

1. **Agent Selection Matrix**: Systems must route operations based on complexity thresholds:
    - Writing / Analysis -> Claude Sonnet 4.6 (Thinking)
    - Complex / Long-document tasks -> Claude Opus 4.6 (Thinking)
    - Rapid Image/PDF/Multi-source processing -> Gemini 3.5 Flash (High)
    - Fallback -> GPT-OSS 120B (Medium)
2. **Remote Asset Verification**: When processing files containing `<!--image [URL] image-->` metadata, systems must scan local `img/` directories for matching filenames. If local files remain absent, systems must execute `wget` targeting the specific remote URL before initiating synchronization protocols.
3. **Deployment Architecture**: `/usr/local/bin/bikepaths-sync` operates as the mandatory global synchronization trigger.
4. **Strict Path Routing**: The `100_blog/` directory functions as an isolated development environment. 
    - Active drafts remain in the designated development area.
    - Compilations target `posted/` environments.
    - Legacy monolithic documents require mandatory transfer into `archive/`.
5. **Template Supremacy**: The `skills/` directory dominates all operational processes. Generated content must map against `_template` structures while awaiting finalization of the Manual of Style (`_style`).

