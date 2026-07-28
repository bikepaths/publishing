# Secondary Linter Rules

This document outlines the specific stylistic and structural rules required for document refactoring.

## 1. Em-Dash Prohibition
- **Rule**: The use of em-dashes (`—`) is strictly forbidden.
- **Transformation**: Any sentence containing an em-dash must be refactored into two or three separate, complete sentences.

## 2. Compositional Prose Transformation
- **Rule**: Bulleted or numbered lists are forbidden.
- **Transformation**: All lists must be converted into fluid, compositional prose. The resulting paragraphs should have variable sentence lengths to maintain engagement and flow.

## 3. Structural Scaffolding
- **Rule**: Maintain the original document's logical hierarchy.
- **Implementation**: Use Markdown headers and transitional sentences to preserve the "scaffolding" of the information while moving away from list-based structures.

## 4. Forbidden Words
- **List**: A lot, merely, utilized, functionality, mere, utilize, furthermore, However, Nevertheless.
- **Rule**: These words are strictly prohibited. Replace them with more precise, direct, or varied alternatives.

## 5. Forbidden Sentence Structures and Styles
- **Anaphoric Repetition**: Avoid starting three consecutive sentences in the same paragraph with the same word.
- **Vague Demonstratives**: Avoid starting sentences with "This figure...", "This information...", or "This occurs...". Be more specific about the subject.
- **Empty Statements**: Remove filler phrases that add no information, such as "It is crucial to be precise when discussing these claims."
- **Scare Quotes**: Do not use quotation marks to distance the text from a term or phrase (e.g., "harvest now, decrypt later"). Use the term directly or rephrase.
- **Direct Quotation Refutation**: Do not quote a previous text specifically to label it (e.g., quoting a claim just to say it "is misleading").
- **Reactive Refutation**: Do not frame facts as a direct refutation of a previous statement (e.g., "Framing this as... is not supported by..."). Instead, simply state the truth directly as a primary fact.

## 6. Dynamic Markdown Fine-Tuning
- **Rule**: Optimize the final output for Markdown rendering.
- **Implementation**: Apply dynamic fine-tuning to ensure the prose is readable, professional, and follows standard Markdown conventions without relying on visual shortcuts like bullets.

## 7. Core Voice (Organic Voice Protocol - OVP)
- **Principle**: The OVP metastyle employs grounded, local metaphors and treats deep physiological and social truths as accessible, shared knowledge. It relies on concrete, observable description to convey complex ideas.
- **Audience Calibration**: OVP is specifically developed for readers whose mother tongue is not English, who live close to land and physical labor, and who learn best through concrete, observable description. The register must remain calibrated to a functional ESL median using plain English vocabulary.

### 7.1 The Five Mandatory Rules

#### Rule 1 — The Grounded Metaphor
- **Rule**: OVP limits metaphors to physical, widely understood mechanics. Do not force a metaphor if direct description suffices. Metaphors serve only as tools to breach complex conceptual barriers.
- **Permitted domains**: Basic structural engineering, simple thermodynamics, agriculture, bodily anatomy.
- **Prohibited domains**: Computer science, corporate finance, abstract mathematics, highly specific sports (e.g., "moving the goalposts").

#### Rule 2 — The Eliminative Rhythm & Anti-Staccato Protocol
- **Absolute Prohibitions**: Staccato fragmentation (sentences must flow seamlessly, avoiding choppy sequences), Subject Pronoun Anaphora (never start more than two consecutive sentences with the same subject pronoun; shift the grammatical subject to physical objects, locations, or actions to maintain a dynamic rhythm), the em-dash (—) and en-dash (–) in any form, semicolons (;), and synthetic contrast phrases like "not X, but Y" or "X is not Y. It is Z."
- **Sentence Length**: There is no maximum sentence length cap. Extend sentences to fully develop causal chains and weave ideas together.

#### Rule 3 — Chronological Fluidity
- **Rule**: Narrative must move in a straight, logical line. Begin from the sensory or observable physical experience, then move inward to the interior or systemic process. The sequence is: Observation first, Mechanism second, Implication third.

#### Rule 4 — Structural Expansion & Causal Chains
- **Rule**: Every complex transition requires full explanation. Avoid piecemeal clause connections. Expand causal connections explicitly so ideas weave together continuously.

#### Rule 5 — Empathetic Authority
- **Rule**: The tone must carry the quiet confidence of a witness. The writing should be educational but never cold, clinical, or detached. It does not perform emotion. It speaks to a reader who is capable and present.

### 7.2 The Plain Language Protocol (ESL / CEFR B2+)

#### 7.2.1 The Kitchen Table Test (Spoken Verification Filter)
- **Rule**: Before generating any sentence, ask: "Would two normal adults actually say this out loud to each other while sitting at a kitchen table?"
- **Prohibition**: If the phrase exists only in written essays or literature (e.g., "vital fire of survival," "mismatched velocity," "symbiotic relationship"), it is strictly forbidden. Force the language down into spoken conversational reality.

#### 7.2.2 Language Register Restrictions
- **Target Audience**: English is a second language (ESL). Avoid all academic, corporate, or analytical tech-speak.
- **Vocabulary Ceiling**: CEFR B2+ common-word register. Use plain, everyday English.
- **Idioms/Colloquialisms**: No idioms, no colloquialisms, no culturally specific references without plain-prose explanation. Precision over colloquialism at all times.

#### 7.2.3 Prohibited Corporate / Analytical Words
- **List**: "utilize" (use "use"), "leverage", "fosters", "greatly", "solely", "nuanced", "holistic", "seamless", "heavy", "heavily", "essential", "fundamentally", "specifically", "perfectly", "assets", "symbiotic", "operational", "dynamic", "capacity", "velocity", "mechanisms", "exact", "exactly".

#### 7.2.4 Prohibited Filler Phrases
- **List**: "In conclusion" or "In summary", "It is important to note that", "As mentioned above" or "As stated previously", "etc." (complete the list or restructure the sentence).

## 8. The Organic Asymmetry Mandate
- **Principle**: To prevent machine-like structural uniformity, all OVP writing must enforce the following compositional rules:
- **Sentence Syncopation**: Drastically vary sentence lengths. Shatter the rhythm by following a long, winding thirty-word sentence with a blunt short sentence.
- **Paragraph Asymmetry**: Destroy uniform block geometry. Mix dense, multi-line paragraphs with isolated, single-sentence paragraphs.
- **The Anti-Pattern Rule**: Never alternate paragraph lengths or sentence lengths in a predictable sequence. True asymmetry means absolutely no mathematical pattern exists.
- **Conversational Flow**: Do not stack isolated subject-verb statements. Use natural conjunctions (and, so, because, while, but) to let ideas bleed together the way human beings actually speak.

## 9. The Anti-Preach Protocol
- **Rule**: Never use instructional commands (e.g., "We must," "You should," "It is important to"). Never lecture, moralize, or tell the reader how to feel. State the physical reality as a witness and let the facts speak for themselves.

## 10. Technical Formatting and Standards

### 10.1 Numbers
- **Rule**: Spell out one through nine. Use numerals for 10 and above.
- **Sentence Start**: Spell out any number that opens a sentence.
- **Percentages**: Use numeral + percent in prose (example: 43 percent). Do not use the % symbol.

### 10.2 Dates
- **Format**: Day Month Year (example: 22 June 2026).
- **Ordinals**: No ordinals (do not write "22nd June").

### 10.3 Attribution and Citation
- **Rule**: All empirical and factual claims require prose attribution.
- **Verification**: Do not fabricate citations. If a source cannot be verified, do not cite it.

### 10.4 Open Source Requirement
- **Rule**: All tools recommended or referenced must be open source and zero cost.
- **Prohibition**: Absolutely no proprietary software references in any published output.
