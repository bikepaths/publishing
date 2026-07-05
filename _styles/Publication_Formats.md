# Publication Formats

This document governs the technical formatting constraints for specific publishing endpoints. Formatting rules apply independently of the active stylistic voice (MoS).

## FORMAT 1 — CMS Web Post

> **AUTHORITATIVE SPECIFICATION:** This section is the sole governing document for all Format 1 web post generation. It supersedes any derivative or simplified prompt documents.

**Purpose:** Inform and engage the GYLC community and invited public readers via self-hosted CMS on private VM.

**Web Post Constraints:**
- Vocabulary: CEFR B2+ common-word register. Enforced via automated pipeline verification against `100_blog/06_data/cefr_b2_dict.txt`. Do not phoneticize numbers (e.g., use numerals like "2005").
- Structure: Dynamic length. Use as many paragraphs as subject complexity demands. No paragraph ceiling.
- Headings: Do not use #, ##, or ### headings. Only #### or bold headings are permitted.
- Metadata Format: Start your response EXACTLY with these three lines before the narrative body:
  Title: [Insert Title]
  Description: [Insert 1-sentence description]
  Tags: [Pick EXACTLY 6 tags. First tag MUST be from the primary category list: money, society, skills, systems, nature, technology, adventure, health, history, mind. Remaining 5 tags from approved tags.lang whitelist.]

## FORMAT 2 — Pedagogical Paper

**Purpose:** Develop a topic with structured argumentation for internal academic review and peer tutoring within GYI.

## FORMAT 3 — KDP Pamphlet

**Purpose:** Accessible, low-cost printed pamphlet for community distribution. Price point: 3 USD. Minimum 24 pages per KDP requirement.

**KDP technical specifications:**
- File format: PDF, no password protection, fonts embedded
- Trim size: 5 x 8 inches (127 x 203.2 mm), dual-sided print
- Margins: inside (gutter) minimum 0.375 inches; outside, top, bottom minimum 0.25 inches
- Images: minimum 300 DPI
- Page count: minimum 24, must be even number
- Line spacing: 1.15 to 1.3
- Paragraph indent: 0.3 to 0.5 inches first-line

## FORMAT 4 — SSRN Academic Working Paper

**Purpose:** Circulate research findings via the Social Science Research Network. Assigned JEL classification codes for academic discoverability.

**Vocabulary Verification Posture:**
- SSRN format operates under a WARNING-ONLY CEFR posture. The automated pipeline will flag out-of-bounds vocabulary but will NOT block deployment.
- Disciplinary terminology (e.g., econometric, cointegration, heteroskedasticity) is expected and permitted. Define each term inline upon first use.
- Before submitting a new SSRN paper, run `02_verify.sh` and extract the out-of-bounds word list. Audit each flagged term against two criteria:
  1. Is it a genuine disciplinary necessity? If yes, add to `cefr_b2_supplement_economics.txt`.
  2. Can it be replaced by a simpler word without loss of precision? If yes, rewrite.
- Topic supplement file: `100_blog/06_data/cefr_b2_supplement_economics.txt`. This file is loaded automatically when primary category tag is `money`, `systems`, `technology`, or `history`.
