# Full Spectrum Publishing Pipeline

Repository functions as the master media deployment pipeline for all theoretical and pedagogical content. (Note: The original academic working papers stream has been explicitly decoupled into a sovereign repository to protect its strict academic register). 

## Unified Sequential Pipeline

- **100_blog**: Micro-blogging platform that generates and deploys short-form articles.
- **200_amazon_kdp**: Amazon Kindle Direct Publishing long-form non-fiction series management.
- **300_multimodal_pedagogy**: The audio production and theoretical translation engine (Organic Vernacular Pedagogy). Consolidates both the curriculum and the mechanical audio pipeline.
- **400_networking**: Social media, outreach strategies, and civic engagement distribution.

**Structural Directive**: The publishing streams operate as structurally distinct entities. They must remain separate and are not subject to consolidation or unification workflows.

## Operational Framework

- **scripts**: Directory contains pre-push verification hook. Hook intercepts and blocks commits failing remote HTTP checks before pushing changes to origin. Nested folders manage database backups, KDP synchronization workflows, and other automated routines.
- **_governance**: Directory contains operational profiles and system prompts, including `profile.md` which defines operational terminology, syntax, and punctuation constraints.
- **_styles**: Directory houses semantic registers that dictate stylistic and publication formatting rules.
- **_epub**, **_templates**, **published**: Global operational directories supporting the deployment and formatting of KDP and multi-platform assets.

## Development Cycle

Current development cycle prioritizes unified pipeline execution or new project initialization.
