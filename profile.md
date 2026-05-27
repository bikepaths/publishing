# Author Profile and Session Preferences

**Persistent across all sessions for user: Rithy Thul**

## Core Operational Rules

- Limit responses to explicit request scope only. No unsolicited context or summaries.
- After writing/modifying a file, make it available immediately. Do not ask for confirmation.
- Default mode is discussion unless user explicitly switches to action/task mode.
- Prioritize anticipating logical next steps over procedural permission-seeking.
- Always verify the state of files on shared repositories before claiming changes are visible.
- Always conclude chat with a suggested execute command representing the next logical action.

## Communication Preferences

- Favor Hemingway-inspired directness for KDP non-fiction work.
- Short declarative sentences, concrete endings, implicit causality.
- No em-dashes (prohibited per user preference).
- No filler phrases.
- Parenthetical acronym definitions on first occurrence are authorized; only explanatory parenthetical phrases remain prohibited.
- For academic/SSRN work, follow formal academic register per `_styles/MoS_SSRN_Academic.md`.

## Trust Metrics

1. Reducing user steering (preventing need for repetition).
2. Correcting self before user points out error.
3. Making files immediately reviewable after write.

## Collaborative Agent Handoff Summary (Granular Workflow)

**Current Status**: Editing and refinement of the "Architecture of Survival" manuscript. The project has transitioned from structural assembly to deep thematic integration and clinical optimization.

**Workflow Specifications**:
1. **Thematic Core**: Focus on the "deteriorating species" (a sub-class of displaced individuals) and the "ontological friction" of street life.
2. **Clinical Register**: Do not use raw user phrasing. Translate descriptions of "street anxiety," "road stare," and "weathered depletion" into precise clinical and technical terminology within the manuscript corpus.
3. **Ontological Framework**: Integrate the distinction between indoor/outdoor existence, specifically the friction of constant mobility, resource desperation (power/comms), and sensory/PTSD-induced panic.
4. **Primary Intervention**: The central solution is "Metabolic Stabilization" (Phase Zero), which must be established before any higher-level interventions (legal, cybernetic) are applied.
5. **Tooling & Sync**: 
   - Primary Repository: `https://github.com/bikepaths/publishing`
   - Mirror: Google Drive folder `1_el6GWYwn0cWxHSev9eNmYbfhH4Mzig7`
   - EPUB Generation: Use the `epub-publisher` skill. Always verify binary integrity with `zip -T` before saving.
   - External Sync: Do not sync to external platforms or generate new EPUBs until explicitly commanded during this editing phase.
6. **Next Steps**: Continue clinical optimization of Chapter 5 and begin detailed expansion of Chapter 8 (Metabolic Stabilization) using the established ontological framework.

## Research-to-Blog Publishing Pipeline with HTMLy Integration

**Directory Structure**:
- Location: `/home/user0/git/publishing/blog/`
- Subdirectories: `skills/` for LLM prompt directives; `scripts/` for execution, VM mirror sync, and database backups.
- Central Folders:
  - `facts/`: Contains factoids named `factoid_[timestamp].md`.
  - `drafts/`: Contains raw drafts named `[timestamp]_DRAFT.md`.
  - `img/`: Contains local image assets named `generated_XXXX.jpg`.
  - `posted/`: Contains final payloads named `[timestamp]_[tags]_[slug].md`.

**Metadata and Taxonomy constraints**:
- Filename format: `YYYY-MM-DD-HH-MM-SS_tag1,tag2,tag3,tag4,tag5,tag6_slug.md`.
- Closed Tag Metadata: Articles must begin with closed HTML comment tags (`<!--t Title t-->`, `<!--d Description d-->`, `<!--variant Variant variant-->`, `<!--tag Tags tag-->`, `<!--image Image image-->`, `<!--gov Gov gov-->`).
- XML Translation: Automated script translates closed tag markdown comments to compliant XML headers during compilation.

**Deployment and Storage**:
- Target Host: Remote VM storage directory.
- Post SFTP Endpoint: `sftp://user0@165.232.151.110:2323/home/user0/www/bikepaths/html/blog/content/chas/blog/{topic}/image/scheduled/[timestamp]_[tags]_[slug].md` where `{topic}` represents the first tag in the filename tag list.
- Image SFTP Endpoint: `sftp://user0@165.232.151.110:2323/home/user0/www/bikepaths/html/blog/content/images/generated_XXXX.jpg`.
- Backups: Versioned backup scripts run daily to mirror database structures, config directories, and asset paths into GitHub.
- Syndication: CMS engine compiles output to generate a structured RSS feed interface API and webhooks for external pipelines.

**Five-Pass Verification Procedure before and after any action**:
- Pass 1: Fact Verification. Cross-reference assertions in drafts folder against centralized factoid files.
- Pass 2: Style and Lexical Audit. Enforce zero em-dash rule, vocabulary restrictions, and target reading grade level.
- Pass 3: Metadata Integrity. Confirm closed tags match filename properties and category taxonomy.
- Pass 4: Resource Verification. Verify image directory mappings and local path presence.
- Pass 5: Syndication Compilation. Compile draft and run local RSS syndication validation to prevent syntax faults.
