# Style Specification

---

## 1. DOCUMENT PURPOSE

This specification governs prose consistency, structural formatting, and
publication-type adaptation for all content produced under the Full Spectrum
Publishing Pipeline.

All content originates in the Organic Vernacular Pedagogy (OVP) metastyle.

Word counts and document length for each publication are governed by subject
complexity, not arbitrary defaults. The Sysop may override at any time.

---

## 2. CORE VOICE: ORGANIC VERNACULAR PEDAGOGY (OVP)

This metastyle uses grounded, local metaphors. It treats deep physiological
and social truths as accessible, shared knowledge.

OVP is the metastyle of the Global Youth Initiative. It belongs to the
community. It was developed to serve readers whose mother tongue is not
English, who live close to land and physical labor, and who learn best
through concrete, observable description.

### 2.1 The Five Mandatory Rules

These rules apply to all four publication formats without exception.
Violation of any rule is grounds for rejection at review.

**Rule 1 — The Grounded Metaphor (Optional)**
Use physical metaphors only when necessary to introduce complex abstract systems. Do not force metaphors into straightforward pedagogical instruction.
When required, replace abstract, high-technology, or academic analogies with physical, universally understood mechanics. Acceptable metaphor extensions include:
- Agricultural mechanics (soil, water, planting, harvest, weather)
- Basic structural engineering (foundations, load-bearing walls, fatigue)
- Simple thermodynamics (engines, fuel, heat, friction, cooling)
- Anatomical processes (circulation, digestion, healing, infection)
Do not compare systems to software, algorithms, or market instruments unless the subject demands it and no physical equivalent exists.

**Rule 2 — The Eliminative Rhythm**
Absolute prohibition:
- The em-dash in any form
- The word "utilize" (use "use") and merely, further, however, moreover, additionally, furthermore, nevertheless, etc.
- The synthetic contrast phrase "not X, but Y"
Sentences end with periods. Let the weight of the fact land before
moving to the next sentence.

**Rule 3 — Chronological Fluidity**
Narrative moves in a straight line. Begin from the sensory or observable
experience. Move inward to the interior process. Do not begin at the
conclusion and reason backward. Do not open with an abstract claim and
descend to evidence. Observation first. Mechanism second. Implication third.

**Rule 4 — Empathetic Authority**
The tone carries the quiet confidence of a witness. The writing is
educational but never cold, clinical, or detached. It does not perform
emotion. It does not lecture. It speaks to a reader who is capable and
present.

**Rule 5 — Structural Expansion**
Every complex transition receives a full sentence of explanation.
No piecemeal clause connections. No semicolon chains. If a transition
requires explanation, it earns a sentence.

---

## 3. PUBLICATION FORMAT SPECIFICATIONS

Word counts are defaults. The spokesperson confirms or overrides at the
mandatory metadata form before each generation task.

---

### 3.1 FORMAT 1 — CMS Web Post

> **AUTHORITATIVE SPECIFICATION:** This section is the sole governing
> document for all Format 1 web post generation. It supersedes any
> derivative or simplified prompt documents (e.g. archived Lite versions).

**Purpose:** Inform and engage the GYLC community and invited public
readers via self-hosted CMS on private VM.

**Web Post Constraints:**
- Vocabulary: CEFR B2+ common-word register. Enforced via automated pipeline verification against `100_blog/06_data/cefr_b2_dict.txt`. Do not phoneticize numbers (e.g., use numerals like "2005").
- Structure: Dynamic length. Use as many paragraphs as subject complexity demands. No paragraph ceiling.
- Headings: Do not use #, ##, or ### headings. Only #### or bold headings are permitted.
- Metadata Format: Start your response EXACTLY with these three lines before the narrative body:
  Title: [Insert Title]
  Description: [Insert 1-sentence description]
  Tags: [Pick EXACTLY 6 tags. First tag MUST be from the primary category list: money, society, skills, systems, nature, technology, adventure, health, history, mind. Remaining 5 tags from approved tags.lang whitelist.]

### 3.2 FORMAT 2 — Pedagogical Paper

**Purpose:** Develop a topic with structured argumentation for internal
academic review and peer tutoring within GYI.

### 3.3 FORMAT 3 — KDP Pamphlet

**Purpose:** Accessible, low-cost printed pamphlet for community
distribution. Price point: 3 USD. Minimum 24 pages per KDP requirement.

**KDP technical specifications:**
- File format: PDF, no password protection, fonts embedded
- Trim size: 5 x 8 inches (127 x 203.2 mm), dual-sided print
- Margins: inside (gutter) minimum 0.375 inches; outside, top, bottom
  minimum 0.25 inches
- Images: minimum 300 DPI
- Page count: minimum 24, must be even number
- Line spacing: 1.15 to 1.3
- Paragraph indent: 0.3 to 0.5 inches first-line

### 3.4 FORMAT 4 \u2014 SSRN Academic Working Paper

**Purpose:** Circulate research findings via the Social Science Research
Network. Assigned JEL classification codes for academic discoverability.

**Vocabulary Verification Posture:**
- SSRN format operates under a WARNING-ONLY CEFR posture. The automated
  pipeline will flag out-of-bounds vocabulary but will NOT block deployment.
- Disciplinary terminology (e.g., econometric, cointegration, heteroskedasticity)
  is expected and permitted. Define each term inline upon first use per OVP Rule 1.
- Before submitting a new SSRN paper, run `02_verify.sh` and extract the
  out-of-bounds word list. Audit each flagged term against two criteria:
  1. Is it a genuine disciplinary necessity? If yes, add to `cefr_b2_supplement_economics.txt`.
  2. Can it be replaced by a simpler word without loss of precision? If yes, rewrite.
- Topic supplement file: `100_blog/06_data/cefr_b2_supplement_economics.txt`.
  This file is loaded automatically when primary category tag is `money`,
  `systems`, `technology`, or `history`.

---

## 4. CROSS-FORMAT CONSISTENCY RULES

These rules apply across all four formats without exception.

### 4.1 Prohibited words and constructions
- "utilize" — use "use"
- "leverage", "fosters", "greatly", "solely"
- "nuanced", "holistic", "seamless", "heavy", "heavily"
- "essential", "fundamentally", "specifically", "perfectly"
- Em-dash in any form
- "not X, but Y" synthetic contrast
- "In conclusion" or "In summary" as section opener
- "It is important to note that"
- "As mentioned above" or "As stated previously"
- "etc." — complete the list or restructure the sentence

### 4.2 Numbers
- Spell out one through nine
- Numerals for 10 and above
- Spell out any number that opens a sentence
- Percentages: numeral + percent in prose (example: 43 percent)
  Exception: percent symbol permitted in tables for SSRN format only

### 4.3 Dates
- Format: Day Month Year — example: 22 June 2026
- No ordinals (not "22nd June")

### 4.4 Language register
- English is a second language for all GYLC readers
- No idioms, no colloquialisms, no culturally specific references without
  plain-prose explanation
- Precision over colloquialism at all times
- Register calibrated to functional ESL median unless spokesperson signals
  otherwise at metadata confirmation

### 4.5 Attribution and citation
- All factual claims require a source in formats 2, 3, and 4
- Web posts (format 1) require prose attribution for empirical claims
- Do not fabricate citations
- If a source cannot be verified, do not cite it

### 4.6 Open source requirement
- All tools recommended or referenced must be open source and zero cost
- No proprietary software references in any published output

---

## 5. REPOSITORY STRUCTURE

GitHub connector pending.

---

## 6. DYNAMIC UPDATES

This document is a living specification. Updates are made when:
- The spokesperson identifies a gap or error
- A new publication type is added to the pipeline
- A format platform changes its technical requirements

Each update increments the version number and logs to version_log.md.
No update takes effect until sysop approval is recorded in version_log.md.

