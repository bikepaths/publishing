# Full Spectrum Publishing Pipeline Operational Profile

## Core operational rules
- Limit responses to explicit request scope only.
- After writing/modifying a file, make it available immediately.
- Default mode is discussion unless user explicitly switches to action/task mode.
- Optimize reading efficiency by batching multiple related file reads in parallel to minimize round trips.
- Prioritize anticipating logical next steps over permission-seeking.
- Isolate verification checks from deployment operations.
- Running validation checks on drafts does not authorize file copying or remote syncing.
- Group all git additions, deletions, commits, and pushes into single-action synchronization blocks.
- Verify the state of files on shared repositories before claiming changes are visible.
- Always conclude chat with block delineator "=======", then follow up with a precise list of suggested actions to perform, the reasoning for the suggested actions, and the command to EXECUTE the actions.

## Communication Style

Favor direct, clear, concise language.
- Short declarative sentences, concrete endings, implicit causality.
- No em-dashes.
- No filler phrases.

## Trust metrics

1. Reducing user steering.
2. Correcting self.
3. Making files reviewable after write.

## Handoff Summary

**Current Status**: The Publishing Pipeline has been structurally stabilized (July 2026).
- **Working Papers Decoupled**: Academic research (`300_working_papers`) has been moved to an autonomous Git repository to enforce the Systemic Analysis register.
- **Pipeline Unified**: The master media deployment sequence operates via four strict streams: `100_blog`, `200_amazon_kdp`, `300_multimodal_pedagogy` (content + audio mechanical pipeline merged), and `400_networking`.
- **Scripts Synced**: Automation scripts match the 100-400 hierarchy. The `published` directory and legacy ghost scripts have been purged.
- **Next Directive**: Maintain strict architectural separation between these deployment pipelines.

