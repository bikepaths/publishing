# Book 4 Refactor Plan: Architectural Triage

## Diagnostic Audit

### Word Count by Chapter (Current State)

| Chapter | File | Words | Status |
|:--------|:-----|------:|:-------|
| Preface | `00_preface.md` | 371 | Draft |
| Ch 1: Ground Floor Operations | `01_ground_floor_intake.md` | 263 | Stub |
| Ch 2: Survival Mechanics | `part_1_riverbed/chapter_01_survival_mechanics.md` | 1,120 | **Full draft** |
| Ch 3: Extraction | `part_1_riverbed/chapter_02_extraction.md` | 1,025 | **Full draft** |
| Ch 4: Silence | `part_1_riverbed/chapter_03_silence.md` | 813 | **Full draft** |
| Ch 5: Community | `part_1_riverbed/chapter_04_community.md` | 880 | **Full draft** |
| Ch 6: Graduation | `part_1_riverbed/chapter_05_graduation.md` | 804 | **Full draft** |
| Ch 7: The Concrete Loop | `part_2_urban_core/chapter_06_concrete_psychosis.md` | 303 | **Stub** |
| Ch 8: Compelled Extraction | `part_2_urban_core/chapter_07_compelled_extraction.md` | 323 | **Stub** |
| Ch 9: The Velocity of Falling | `part_3_economic/chapter_08_eviction_velocity.md` | 323 | **Stub** |
| Ch 10: Preventing the Collapse | `part_3_economic/chapter_09_rapid_stabilization.md` | 294 | **Stub** |
| **Total** | | **6,519** | |

### Structural Failures Identified

**Failure 1: Catastrophic Part Imbalance**
Part 1 (Riverbed/Arthur) runs ~4,640 narrative words across five chapters. Parts 2 and 3 combined total ~1,240 words across four chapters, all at stub depth. The reader experiences a fully rendered world in Part 1, then walks into narrative scaffolding. This asymmetry breaks the book's central argument: three demographically distinct pipelines require three equally rigorous demonstrations.

**Failure 2: Outline-Manifest Mismatch**
`research/05_chapter_outline.md` specifies a 12-chapter arc with distinct stage labels (Sally Port Handoff, Adrenal Decompression, Pod Governance, Cafe Stewardship, Clinical Integration, Municipal Yield). The current `manifest.yaml` compresses this into 10 chapters, collapsing four discrete recovery stages in Parts 2 and 3 into two stubs each. The research outline is the more granular and operationally correct document; the manifest must expand to match it.

**Failure 3: Character Identity Collision in Research Files**
`research/04_case_study_outline.md` labels the Riverbed subject "Marcus." The actual draft chapters use "Arthur" for the Riverbed pipeline and "Marcus" for Pipeline A (Economic). The research docs are stale. The draft is authoritative. Any new chapter writing must use Arthur (Pipeline B/Riverbed), Gloria (Pipeline C/Urban Core), Marcus (Pipeline A/Economic).

**Failure 4: Book 1 Specs Absent from Expansion Targets**
The manifest handoff directive requires Book 1 mechanical specifications woven into the physical descriptions. The stubs in Parts 2 and 3 carry none: no STC-65 ratings during Gloria's decompression sequence, no 154-resident Dunbar limit during pod integration, no keycard protocol detail. Per the manifest directive, every new chapter must demonstrate these protocols governing action, not merely assert they exist.

---

## Refactor Target Architecture

The 12-chapter research outline represents the correct destination. Each part requires four chapters: **Exposure → Extraction → Decompression → Reintegration**. The preface and ground floor intake chapter remain as-is (minor polish only). The graduation/municipal yield chapter closes each part.

### Revised Manifest Structure

| Manifest Slot | Chapter Title | Pipeline | Status | Action |
|:-------------|:-------------|:---------|:-------|:-------|
| Preface | The Architectural Engine | — | Draft | Minimal polish |
| Ch 1 | Ground Floor Operations | — | Stub | Expand to ~900w |
| Ch 2 | Survival Mechanics | B/Riverbed/Arthur | Full | Book 1 spec weave |
| Ch 3 | Extraction | B/Riverbed/Arthur | Full | Book 1 spec weave |
| Ch 4 | Silence | B/Riverbed/Arthur | Full | Book 1 spec weave |
| Ch 5 | Community | B/Riverbed/Arthur | Full | Book 1 spec weave |
| Ch 6 | Graduation | B/Riverbed/Arthur | Full | Book 1 spec weave |
| Ch 7 | The Concrete Loop | C/Urban Core/Gloria | Stub | **Expand to ~1,000w** |
| Ch 8 | Compelled Extraction | C/Urban Core/Gloria | Stub | **Expand to ~1,000w** |
| **Ch 8b** | **Forced Decompression** | C/Urban Core/Gloria | Missing | **Write new ~900w** |
| **Ch 8c** | **Behavioral Reconstitution** | C/Urban Core/Gloria | Missing | **Write new ~900w** |
| Ch 9 | The Velocity of Falling | A/Economic/Marcus | Stub | **Expand to ~900w** |
| Ch 10 | Preventing the Collapse | A/Economic/Marcus | Stub | **Expand to ~900w** |
| **Ch 10b** | **Rapid Exit Protocol** | A/Economic/Marcus | Missing | **Write new ~800w** |
| **Ch 10c** | **The Municipal Yield** | A/Economic/Marcus | Missing | **Write new ~800w** |

> [!IMPORTANT]
> Two new chapters are required per Part 2 and Part 3. `manifest.yaml` must be updated to include these files before any expansion pass runs.

---

## Execution Plan: Four Sequential Passes

### Pass 1 — Manifest Reconciliation
**Scope**: `manifest.yaml` only.  
**Actions**:
1. Add `chapter_drafts/part_2_urban_core/chapter_08_forced_decompression.md` as Ch 8b with heading "Chapter 9: Forced Decompression."
2. Add `chapter_drafts/part_2_urban_core/chapter_09_behavioral_reconstitution.md` as Ch 8c with heading "Chapter 10: Behavioral Reconstitution."
3. Add `chapter_drafts/part_3_economic/chapter_10_rapid_exit_protocol.md` as Ch 10b with heading "Chapter 11: Rapid Exit Protocol."
4. Add `chapter_drafts/part_3_economic/chapter_11_municipal_yield.md` as Ch 10c with heading "Chapter 12: The Municipal Yield."
5. Renumber existing chapters 9 and 10 to chapters 7 and 8 in the YAML heading fields (file paths unchanged).

**Verification**: `cat manifest.yaml` confirms 14 total entries (copyright + frontmatter + preface + 10 chapters + bibliography).

### Pass 2 — Part 2 Urban Core Expansion (Gloria)
**Scope**: Four files in `part_2_urban_core/`.  
**Target word counts**: Each chapter ≥ 900 words, matching Part 1 density.

| File | Current | Target | Primary Scene |
|:-----|--------:|-------:|:-------------|
| `chapter_06_concrete_psychosis.md` | 303 | 1,000 | Gloria at Fifth/San Pedro sorting loop; outreach team documents behavioral calcification; CARE Court petition filed |
| `chapter_07_compelled_extraction.md` | 323 | 1,000 | Conservatorship order; medical extraction van; sally port arrival; physical containment sequence |
| `chapter_08_forced_decompression.md` | 0 | 900 | Gloria's STC-65 room; locked door protocol; biometric monitoring; first 72 hours of involuntary quiet |
| `chapter_09_behavioral_reconstitution.md` | 0 | 900 | Weeks 3–12; gradual environmental stimulus reintroduction; first voluntary verbal response; transition toward pod integration |

**Book 1 Specs Required in Pass 2**:
- STC-65 rating named and functionally described during decompression scenes
- Locked solid-core door and override-only keycard logic during containment
- Zero blind corners during sally port arrival sequence
- Medical transport acoustic dampening bridging to pod acoustic standards

### Pass 3 — Part 3 Economic Expansion (Marcus)
**Scope**: Four files in `part_3_economic/`.

| File | Current | Target | Primary Scene |
|:-----|--------:|-------:|:-------------|
| `chapter_08_eviction_velocity.md` | 323 | 900 | Marcus in supermarket parking lot; physiological onset of cortisol flooding; outreach van approach; cognitive-intact voluntary intake |
| `chapter_09_rapid_stabilization.md` | 294 | 900 | Marcus drives into Tower One parking garage; rapid-exit floor routing; 48-hour employment intervention; no Phase Zero decompression required |
| `chapter_10_rapid_exit_protocol.md` | 0 | 800 | County transit dispatch position; lease signing; Tower One pod vacancy freed for next arrival; cost-avoidance math stated explicitly |
| `chapter_11_municipal_yield.md` | 0 | 800 | Fiscal audit scene; HSH demand for CalAIM performance metrics; $3,000 intervention vs $80,000 chronic street casualty calculus; budget hearing framing |

**Book 1 Specs Required in Pass 3**:
- 154-resident pod limit named when Marcus first enters the rapid-exit floor (contrast with his cognitive-intact state requiring no full decompression protocol)
- Keycard dignity framing: Marcus receives keycard same night; emphasize agency restoration as biological intervention
- Digital intake tablet replaces paper forms; zero congregate dormitory experience for Pipeline A

### Pass 4 — Book 1 Spec Weave Into Existing Part 1 Chapters
**Scope**: The five Arthur/Riverbed chapters that are already fully drafted.  
**Method**: Targeted inline insertions, not rewrites. Each chapter needs one to two sentences anchored to a named Book 1 specification.

| Chapter | Missing Spec | Insertion Point |
|:--------|:------------|:----------------|
| `chapter_03_silence.md` | STC-65 is described but the "STC-65" label is present—verify 154-resident limit is absent | Add when Arthur first moves to the residential floor; contrast his pod's 154-person ceiling against the shelter gymnasiums he feared |
| `chapter_04_community.md` | Dunbar/154-resident limit present but keycard protocol absent | Weave keycard into the scene where Arthur realizes nobody can walk into his room |
| `chapter_05_graduation.md` | Zero blind corners absent from ground floor description; cost figures present but unpinned to specific Book 1 protocol | Add one line naming the architectural ground-floor spec during the administrative office graduation scene |
| `chapter_01_survival_mechanics.md` | No Tower spec needed yet (pre-Tower scene)—verify no anachronistic MDI references exist | Audit only |
| `chapter_02_extraction.md` | Veterinary transport crate is described; verify pet policy framing aligns with Book 1 zero-separation spec | Confirm language; add explicit policy name if absent |

---

## Quality Gates Before Compilation

1. **Character audit**: `grep -r "Marcus" part_1_riverbed/` must return zero matches. `grep -r "Arthur" part_2_urban_core/ part_3_economic/` must return zero matches.
2. **Spec coverage**: Each of the five Book 1 specs (154-resident limit, STC-65, keycard, zero blind corners, zero congregate dormitories) must appear in at least two chapters across the manuscript.
3. **Word floor**: `wc -w` on all chapter files; no chapter may fall below 750 words post-expansion.
4. **Compile check**: Run the Python compile script; EPUB output must produce zero errors.

---

## Decisions Requiring Sysop Input Before Execution

> [!WARNING]
> Three structural decisions must be resolved before Pass 1 begins:

1. **Chapter heading numbering**: The current manifest numbers chapters 1–10 using the sequential slot, not part-internal numbering. With two new chapters per Part 2 and Part 3, the final chapter count reaches 12 narrative chapters plus preface, matching the research outline. Confirm: use global sequential numbering (Ch 1–12) or part-internal numbering (Part 2: Chapters 1–4)?

2. **Gloria arc resolution**: The current stubs bring Gloria only through forced intake. The research outline (`05_chapter_outline.md`) does not specify a Gloria graduation chapter equivalent to Arthur's. Confirm: does Gloria require a graduation/discharge chapter, or does Part 2 close at behavioral reconstitution, leaving her arc open-ended as a narrative contrast to Arthur's clean graduation?

3. **Expand Ground Floor (Ch 1) now or in a separate pass?**: Chapter 1 currently sits at 263 words (stub). It introduces the sally port and triage logic that both Gloria and Marcus will experience in subsequent chapters. Expanding it during Pass 2/3 creates a logical dependency where the ground floor chapter must precede the parts it describes. Confirm: expand Ch 1 first as a standalone pass, or defer to post-Part-3 as a retroactive anchor?
