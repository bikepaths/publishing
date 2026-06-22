# Standalone Pedagogical Documents

## Purpose
This directory stores long-form chaptered explanations of complex systemic concepts written for ESL readers at CEFR B2 proficiency. These documents translate the dense academic research stored across `/100_blog/01_source/` and `/300_working_papers/` into accessible English using a restricted 5,500 common-word vocabulary.

## Target Audience
A 15-year-old gifted student with two years of ESL instruction and zero prior domain knowledge.

## Governing Style
All documents in this directory must comply with `/home/user0/git/publishing/_styles/MoS_Pedagogical_Docs.md`.

## Filename Convention
`PD_[topic-slug]_v[version].md`

Examples:
- `PD_material-dignity-infrastructure_v1.md`
- `PD_federal-medicaid-funding_v1.md`
- `PD_dunbar-pod-architecture_v1.md`

## Relationship to Blog Pipeline
Pedagogical documents do not deploy through `file_2_post_pipeline.py`. They function as structured source material from which future blog posts are extracted and adapted under the Systemic Analysis MoS.

## Verification
Each document must pass a Flesch-Kincaid grade audit confirming scores between 8.0 and 9.5 before archival.

## Document Structure
1. **Front Matter** — Title, audience statement, prerequisite chapters, estimated reading time.
2. **Numbered Chapters** — Sequential, progressive, each introducing no more than five new technical terms.
3. **Cumulative Glossary** — Running glossary appended at document end, each definition under fifteen words.
