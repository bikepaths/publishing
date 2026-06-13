# Skill - Standard Blog Post Layout

This skill defines the structured layout template for all blog posts. The layout prioritizes rapid cognitive ingestion, clear reading metrics, and upfront summary structures to optimize readability for researchers and busy readers.

## 1. Metadata Block

Every post begins with a closed metadata tag block enclosed in HTML comments. This block must not contain plain text outside the tags.

```markdown
<!--t [Post Title] t-->
<!--d [300 character maximum description of the post] d-->
<!--tag [Comma-separated tag list] tag-->
<!--image [Absolute image URL or local path] image-->
```

## 2. Quick Read Section

Directly following the metadata block, a summary section provides a fast overview of the article content.

### A. TL;DR Header
A level three header (`### tl;dr`) followed by a single-paragraph summary of the post. The paragraph must be dense, stating the main problem, the core mechanism, and the ultimate resolution.

### B. Reading Metrics
A level four header specifying reading time followed by word count and stylistic description:

```markdown
#### Reading time averages [X] minutes.

Word count totals [Y] words.

[Style descriptor] structure.
```

## 3. Post Body

The core essay text follows the reading metrics.

*   **Structure**: The body must consist of 3 to 6 logical paragraphs.
*   **Headers**: Level four (`####`) or bold inline markers may divide sections.
*   **Scanning Anchors**: Bold key phrases inside paragraphs to guide rapid reading.
*   **Lexical Cleanliness**: No parenthetical statements, colons in middle sentences, en-dashes, or em-dashes.

## 4. References

Posts referencing academic papers, books, or datasets must append a references section at the bottom.

*   **Header**: Level four (`#### References`).
*   **Format**: Use standard academic citation layouts.
