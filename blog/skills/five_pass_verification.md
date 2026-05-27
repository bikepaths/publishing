# Skill - Five-Pass Verification Protocol

This skill governs the systematic quality control process for publishing blog posts. The procedure ensures lexical compliance, fact alignment, metadata structure, asset resolution, and syndication output.

## Phase 1: Fact Verification

We cross-reference all claims within drafts against verified facts documents.
- Target folder: `facts/` relative to the blog post directory.
- Audit rule: Every numerical metric or historical claim in the drafts folder must align with an entry in the facts folder; mismatched assertions fail the check.

## Phase 2: Style and Lexical Audit

We enforce writing specifications defined in style manuals.
- Audit rule: Validate target readability level between Grade 11.0 and Grade 11.4.
- Audit rule: Confirm complete absence of em-dashes, en-dashes, and parenthetical phrases.
- Audit rule: Confirm sentence length variance; ensure no consecutive sentences share identical word counts.
- Audit rule: Verify opener rotation; check that no more than half the sentences in a paragraph start with subject nouns.
- Audit rule: Purge all forbidden vocabulary, academic clichés, and mechanical transition words.

## Phase 3: Metadata Integrity

We verify the closed tag metadata format and taxonomy mapping.
- Audit rule: Confirm all metadata tags use trailing identifiers.
- Audit rule: Check tag metadata matches filename properties exactly.
- Audit rule: Verify category taxonomy maps to approved topics list.

## Phase 4: Resource Verification

We validate path mappings and local storage of images.
- Audit rule: Confirm image URLs in metadata block point to valid absolute paths.
- Audit rule: Ensure image folder structure matches the post slug.

## Phase 5: Syndication Compilation

We compile final drafts and test RSS syndication output.
- Audit rule: Run compilation scripts to generate target XML payload.
- Audit rule: Validate generated RSS feed format using XML linting tools to prevent feed ingestion failures.
