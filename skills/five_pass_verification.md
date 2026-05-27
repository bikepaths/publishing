# Skill - Five-Pass Verification Protocol

This skill governs the systematic quality control process for publishing blog posts. The procedure ensures lexical compliance, fact alignment, metadata structure, asset resolution, and syndication output.

## Phase 1: Fact Verification

We cross-reference all claims within drafts against verified facts documents.
- Target folder: `facts/` relative to the blog post directory.
- Audit rule: Every numerical metric or historical claim in the drafts folder must align with an entry in the facts folder; mismatched assertions fail the check.

## Phase 2: Style and Lexical Audit

We enforce writing specifications defined in style manuals.
- Audit rule: Validate target readability level between Grade 8.0 and Grade 10.0 to ensure accessibility for less educated audiences.
- Audit rule: Ensure unique character readability through sentence rhythm (e.g., following complex structural explanations with a brutal, five-to-ten word declarative hammer) and metaphor mapping (replacing abstract academic or policy jargon with intuitive mechanical or industrial metaphors).
- Audit rule: Confirm complete absence of em-dashes, en-dashes, and parenthetical phrases.
- Audit rule: Confirm sentence length variance; ensure no consecutive sentences share identical word counts.
- Audit rule: Verify opener rotation; check that no more than half the sentences in a paragraph start with subject nouns.
- Audit rule: Purge all forbidden vocabulary, academic clichés, and mechanical transition words.

## Phase 3: Metadata Integrity

We verify the closed tag metadata format and taxonomy mapping.
- Audit rule: Confirm all metadata tags use trailing identifiers.
- Audit rule: Check tag metadata matches filename properties exactly.
- Audit rule: Confirm the first tag is always the primary category, selected from: `society`, `skills`, `systems`, `money`, `nature`, `technology`, `adventure`, `health`, `history`, `mind`.
- Audit rule: Enforce a maximum of 6 total tags (1 category tag and at most 5 additional tags).
- Audit rule: Validate that all additional tags are selected from the approved dictionary in `tags.lang`.

## Draft Verification Gate

- Always stop and request Sysop verification of the draft in the `drafts/` folder before compiling it to the `posted/` folder or initiating VM deployment.

## Phase 4: Resource Verification

We validate path mappings and local storage of images.
- Audit rule: Confirm image URLs in metadata block point to valid absolute paths.
- Audit rule: Ensure image folder structure matches the post slug.

## Phase 5: Syndication Compilation

We compile final drafts and test RSS syndication output.
- Audit rule: Run compilation scripts to generate target XML payload.
- Audit rule: Validate generated RSS feed format using XML linting tools to prevent feed ingestion failures.
