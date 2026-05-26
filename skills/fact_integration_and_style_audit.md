# Skill - Fact Integration and Style Audit

This skill governs the integration of new factual metrics into existing manuscript baselines and to maintain strict compliance with the manual of style. By filtering out structural deviations, the process guarantees that updates do not compromise the stylistic purity of the text.

## Phase 1: Fact Mapping and Reconciliation

The agent must identify new facts from external research databases and map them to their corresponding chapters. Across all documents, this phase reconciles numerical discrepancies to prevent contradictions and structurally.

### Mapping Rules

1. **Locate Target Files**: Identify the chapter facts files in the facts directory.
2. **Inject Atomic Statements**: Add the new facts as dry, independent bullet points.
3. **Verify Values**: Cross-reference numerical values across all documents.
4. **Remove Formatting Violations**: Clean out parentheses, colons, or em-dashes within the updated text.

## Phase 2: Narrative Integration

The agent must update the main chapter drafts to incorporate the newly added facts. To weave the new metrics into the paragraph flow, writers rewrite surrounding sentences to make them flow and in style.

### Writing and Formatting Rules

1. **Active Integration**: Rewrite surrounding sentences to weave the new facts into the paragraph flow.
2. **Voice Control**: Maintain active voice throughout the text.
3. **Punctuation Compliance**: Do not use em-dashes or parenthetical phrases.
4. **Sentence Variance**: Verify that sentence lengths vary within paragraphs.
5. **Opener Rotation**: Rotate sentence openings to avoid subject-first repetitions.
6. **Vocabulary Cleanliness**: Avoid forbidden qualifiers, academic clichés, and mechanical transition words.
7. **Controlled Non-Parallelism**: Introduce one controlled departure from parallel structure per paragraph.

## Phase 3: Automated Verification

The agent must run the style verification compiler to audit all modified files before completing any integration. By executing the automated verification script, the agent identifies style regressions before checking in drafts and to prevent issues.

### Audit Steps

1. **Execute Verification Script**: Run the python script on the modified files.
2. **Resolve Violations**: Fix any flagged occurrences of colons, parentheses, em-dashes, or forbidden words.
