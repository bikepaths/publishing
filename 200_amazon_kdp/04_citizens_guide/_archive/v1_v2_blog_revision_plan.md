# V1/V2 Blog Revision Plan: Integrating the Federal Comparative Dynamic

## 1. Architectural Baseline
The v2 manuscript (`/home/user0/git/publishing/200_amazon_kdp/04_citizens_guide/kdp_v2/manuscript/Fixing_Skid_Row_DiBella.md`) serves as the read-only master source. All mutative integration occurs within the v1 working directory. The v1 working document (`/home/user0/git/publishing/200_amazon_kdp/04_citizens_guide/kdp_v1/manuscript/Fixing_Skid_Row_DiBella.md`) is a cloned instance of the v2 master. This isolation preserves the original manuscript while allowing aggressive structural modification in the v1 environment.

## 2. Content Extraction and Mapping
The core arguments from the blog post (`100_blog/03_posted/2026-06-19-06-21-56..._trump-era-homelessness-policies.md`) require extraction and formalization for a manuscript register. The integration targets three primary vectors:
1. **The Relocation Paradigm versus the Stabilization Paradigm.** Contrast the federal proposal for exurban relocation camps with the MDI requirement for urban-core clinical towers.
2. **Punitive Action versus Medical Compulsion.** Contrast the *Grants Pass* criminalization framework with the MDI compelled care framework. Establish the boundary between law enforcement and clinical extraction.
3. **Fiscal Efficacy.** Contrast the institutional waste of remote warehousing with the thermodynamic efficiency of building reuse.

## 3. Structural Injection
The extracted arguments map directly to **Chapter 25: Comparative Models** within the v1 working document. The injection requires restructuring the chapter to position the Trump-era federal framework as the primary antagonistic model. The text must dismantle the relocation camp premise using the established thermodynamic and neurological principles (Unit Two). The argument will demonstrate that relocating neurologically degraded individuals to exurban camps without clinical stabilization infrastructure accelerates cognitive decline and guarantees system failure.

## 4. Semantic Reconciliation
Post-injection, a full semantic cross-reference audit is mandatory. The audit ensures the injected critique of federal policy harmonizes with existing critiques of municipal and state policies (e.g., the Housing First critique in Chapter 3). The distinction between MDI compelled care and conservative criminalization must remain absolute throughout the text.

## 5. Compilation Pipeline
Following semantic reconciliation, the existing compilation script (`compile_book.py`) executes against the v1 manifest. The manifest points exclusively to the modified v1 working document. The pipeline generates the final `citizens_guide.epub` output in the `kdp_v1/handoff` directory.

---

## Execution Log — 2026-06-19

### Step 1: Source Material Ingestion
- Read the blog post (`100_blog/03_posted/2026-06-19-06-21-56..._trump-era-homelessness-policies.md`) in full (89 lines, 14,804 bytes).
- Located Chapter 25 injection target at line 1143 of the v1 working document.
- Read Chapter 25 (lines 1143-1193) to map the existing structure: intro, AMFD, TDMZ, UBIV, AOPC, synthesis.
- Read Chapter 23: Ten Objections (lines 1013-1097) to verify compelled-care argument consistency.
- Confirmed the v2 master document is untouched at 30,994 words.

### Step 2: Content Extraction and Mapping
Extracted three argument vectors from the blog post:
1. **Relocation vs. Stabilization:** Federal enforcement clears encampments without clinical destination; MDI provides integrated clinical towers.
2. **Punitive vs. Medical Compulsion:** Federal AOT deployment risks compulsion without adequate infrastructure; MDI constrains compulsion behind Phase Zero destination and Chapter 16 safeguards.
3. **Fiscal Efficacy:** Federal discretionary grants expire with administrations; MDI capital stack (LIHTC, NMTC, Medicaid, private capital) operates as durable utility financing.

### Step 3: Structural Injection (3 non-contiguous edits)
**Edit 1 — Chapter introduction** (lines 1143-1147): Rewrote to establish expanded scope covering real federal policy and theoretical alternatives. Added forward reference framing the federal framework as the most politically salient model.

**Edit 2 — Trump-era section insertion** (line 1149): Inserted approximately 1,120 words of new content before the existing AMFD section. The new section covers:
- Executive order context (STREETS program, RFK Jr. Great American Recovery Initiative)
- Where federal policy helps (Pipeline A and B acceleration)
- Where it fails (Pipeline C sobriety conditions, enforcement without destination)
- Court-ordered treatment without clinical infrastructure (cross-references Chapter 16)
- Scattered-site problem (cross-references Chapter 9)
- Funding durability problem (cross-references Chapters 19-21)

**Edit 3 — Closing synthesis** (lines 1185-1191): Expanded "Why Integration Is Necessary" to incorporate the federal framework's failure mode (enforcement without destination, discretionary funding without utility-grade financing) alongside the four theoretical models.

### Step 4: Semantic Reconciliation Audit
- **Em-dash audit:** Scanned full v1 document. All em-dashes are structural (UNIT headings, pipeline labels, back-matter tool listings). Zero prose-dependent em-dashes. Clean.
- **Compelled care cross-reference:** Verified the new Chapter 25 injection against Chapter 4 (line 207), Chapter 14 (line 685), Chapter 16 (lines 735-789), and Objection 1 (lines 1023-1025). The distinction between MDI clinical compulsion and federal enforcement-driven compulsion is maintained throughout. No contradictions.
- **Pipeline terminology:** The new section uses "Pipeline A," "Pipeline B," "Pipeline C" consistently with the definitions established in Chapter 4.
- **Chapter cross-references:** The new section references Chapters 2, 3, 5, 9, 16, and 19-21. All references point to content that exists and supports the arguments made.

### Step 5: Compilation Pipeline
- Executed `compile_book.py --book 4 --format epub` against the v1 manifest.
- Pandoc assembled `epub_source.md` (32,201 words) and `full_manuscript.md` (32,189 words).
- EPUB generated, landmarks sanitized, EpubCheck validation passed: `Is valid: True`, 0 messages.
- Final output: `kdp_v1/handoff/citizens_guide.epub` (78 KB).

### Word Count Delta
| Document | Words |
| :--- | :--- |
| v2 master (read-only) | 30,994 |
| v1 working (modified) | 32,114 |
| Net injection | +1,120 |

### Artifacts Produced
- `/home/user0/git/publishing/200_amazon_kdp/04_citizens_guide/kdp_v1/handoff/citizens_guide.epub`
- `/home/user0/git/publishing/200_amazon_kdp/04_citizens_guide/kdp_v1/manuscript/Fixing_Skid_Row_DiBella.md` (modified)
- `/home/user0/git/publishing/200_amazon_kdp/04_citizens_guide/kdp_v1/manuscript/epub_source.md` (auto-generated)
- `/home/user0/git/publishing/200_amazon_kdp/04_citizens_guide/kdp_v1/manuscript/full_manuscript.md` (auto-generated)

### Files Preserved (Untouched)
- `/home/user0/git/publishing/200_amazon_kdp/04_citizens_guide/kdp_v2/manuscript/Fixing_Skid_Row_DiBella.md`
- `/home/user0/git/publishing/100_blog/03_posted/2026-06-19-06-21-56..._trump-era-homelessness-policies.md`
