# FSPP (Full Spectrum Publishing Pipeline)

Repository functions as unified system that consolidates three publishing streams into one master repository. Sysop operates workspace for extended re-discovery.

## Unified Directory Architecture

- **100_blog**: Micro-blogging platform that generates and deploys articles.
- **200_amazon_kdp**: Amazon Kindle Direct Publishing non-fiction series management.
- **300_working_papers**: Academic research and working papers management.

## Operational Framework

- **scripts**: Directory contains pre-push verification hook. Hook intercepts and blocks commits failing remote HTTP checks before pushing changes to origin. Nested folders manage database backups, KDP synchronization workflows, and other automated routines.
- **_styles**: Directory houses semantic registers that dictate style and formatting rules.
- **profile.md**: File defines operational parameters that enforce specified terminology, syntax, and punctuation rules.

## Development Cycle

Current development cycle prioritizes unified pipeline execution or new project initialization.
