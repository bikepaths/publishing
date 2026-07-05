# Full Spectrum Publishing Pipeline

Repository functions as unified system that consolidates three publishing streams into one master repository. Sysop operates workspace for extended re-discovery.

## Unified Directory Architecture

- **100_blog**: Micro-blogging platform that generates and deploys articles.
- **200_amazon_kdp**: Amazon Kindle Direct Publishing non-fiction series management.
- **300_working_papers**: Academic research and working papers management.

**Structural Directive**: The blogging (`100_blog`) and KDP (`200_amazon_kdp`) publishing streams operate as structurally distinct entities. They must remain separate and are not subject to consolidation or unification workflows.

## Operational Framework

- **scripts**: Directory contains pre-push verification hook. Hook intercepts and blocks commits failing remote HTTP checks before pushing changes to origin. Nested folders manage database backups, KDP synchronization workflows, and other automated routines.
- **_governance**: Directory contains operational profiles and system prompts, including `profile.md` which defines operational terminology, syntax, and punctuation constraints.
- **_styles**: Directory houses semantic registers that dictate stylistic and publication formatting rules.
## Development Cycle

Current development cycle prioritizes unified pipeline execution or new project initialization.
