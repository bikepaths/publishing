# Skill: Initialize Blog Post

## Primary Directives

1. **Remote Asset Verification**: When processing files containing `<!--image [URL] image-->` metadata, systems must actively scan local `img/` directories for matching filenames. If local files remain absent, systems must execute `wget` targeting the specific remote URL before initiating synchronization protocols.
2. **Deployment Architecture**: `/usr/local/bin/bikepaths-sync` operates as the mandatory global synchronization trigger.
3. **Strict Path Routing**: The `100_blog/` directory functions strictly as an isolated development environment. 
    - Active drafts remain in the designated development area.
    - Compilations target exclusively `posted/` environments.
    - Legacy monolithic documents require mandatory transfer into `archive/`.
4. **Template Supremacy**: The `skills/` directory dominates all operational processes. Generated content must strictly map against `_template` structures while awaiting finalization of the Manual of Style (`_style`).
