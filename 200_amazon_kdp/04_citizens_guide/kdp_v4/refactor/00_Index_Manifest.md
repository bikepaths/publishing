# 00 — Index Manifest
## kdp_v4 Refactor | Material Dignity Infrastructure — *Fixing Skid Row*
**Author:** Charles J. DiBella | **Manifest Version:** 1.0 | **Date:** June 2026

---

## 1. Project Context

The source manuscript is `full_manuscript.md` — a 27-chapter citizen's guide to the MDI
framework structured in seven units. The refactor closes seven documented gaps without
altering the manuscript's voice, structure, or falsifiability clause. All deliverables are
produced as standalone files for author integration. No deliverable is embedded directly
into the source manuscript by the agent.

**Source manuscript word count (approx.):** 65,000 words  
**Source manuscript chapter range:** Chapters 1–27 across 7 Units  
**Companion framework page:** https://bikepaths.org/mdi  
**SSRN papers (cross-reference throughout):** 5968756 · 6211658 · 6579600

---

## 2. File Path Conventions

All deliverables are produced relative to:
```
200_amazon_kdp/04_citizens_guide/kdp_v4/refactor/
```

Agent working directory for drafts: `/home/claude/`  
Final output directory: `/mnt/user-data/outputs/`

Naming convention: `NN_Descriptive_Title.md` where NN is the two-digit sequence number
matching the staged plan.

---

## 3. Deliverable Registry

### 00 — Index Manifest *(this file)*
| Field | Value |
|---|---|
| **File** | `00_Index_Manifest.md` |
| **Phase** | 1 |
| **Type** | Planning document |
| **Integration location** | None — agent reference only |
| **Dependencies** | None |
| **Status** | ✅ Complete |

---

### 01 — Capability-to-Specification Translation
| Field | Value |
|---|---|
| **File** | `01_Capability_to_Specification_Translation.md` |
| **Phase** | 2 |
| **Type** | New appendix |
| **Integration location** | Insert as **Appendix A** after Chapter 27 ("What Citizens Can Do"), before the bibliography. Add a forward reference at the end of Chapter 7 ("The Capability Approach"): *"For the full derivation of engineering parameters from each capability, see Appendix A."* |
| **Dependencies** | Manuscript read (complete). Requires literature search: Dunbar (1992, 2021); STC acoustic standards in psychiatric inpatient design; Walker (2017) and Arnsten (2009) for 30-day parameter; Barthel/FIM for clearance indicator grounding. |
| **Critical constraint** | Must trace every engineering parameter to a specific capability. Must distinguish between parameters with direct literature support and those derived by clinical inference. Do not assert equivalence where only analogy exists. |
| **Target length** | 3,000–4,500 words plus mapping table |
| **Status** | 🔲 Pending |

**Mapping table schema:**

| Nussbaum Capability | Physical/Clinical Condition Required | MDI Engineering Parameter | Supporting Evidence | Confidence Level |
|---|---|---|---|---|
| 1. Life | ... | ... | ... | High / Medium / Inferred |

Confidence levels: **High** = direct peer-reviewed evidence for this parameter; **Medium** = analogous evidence from comparable settings; **Inferred** = clinical judgment, no direct evidence, awaiting MDI-specific validation.

---

### 02 — MDI Outside California: Adaptation Principles
| Field | Value |
|---|---|
| **File** | `02_MDI_Outside_California_Adaptation_Principles.md` |
| **Phase** | 5 |
| **Type** | New appendix |
| **Integration location** | Insert as **Appendix B** after Appendix A, before the bibliography. Add a single sentence at the end of Chapter 25 ("Comparative Models"): *"For adaptation of the MDI framework to legal and financial contexts outside California, see Appendix B."* |
| **Dependencies** | `07_Chapter_7_Addition_Scholarly_Context.md` should be drafted first to establish the universal vs. context-specific distinction in the main text. |
| **Research required** | UK Mental Health Act 1983 (amended 2007) — involuntary treatment provisions. Canadian provincial mental health legislation (Ontario Mental Health Act; BC Mental Health Act). Finnish Housing First financing via Y-Foundation / ARA (Housing Finance and Development Centre). EU Horizon NEB 2026 funding structure (HORIZON-NEB-2026-01-BUSINESS-01). Australian NDIS as an alternative Medicaid analog. |
| **Three-section structure** | (1) Universal elements: neuroscientific foundation, pipeline categorization, Dunbar Pod architecture, Phase Zero/Sen Phase sequence — these require no adaptation. (2) Elements requiring local translation: legal instruments for compelled care, financing mechanisms, building acquisition pathways, clinical data infrastructure. (3) Adaptation principles: for each element in section 2, state the functional principle and one or two concrete examples from non-California jurisdictions. |
| **Critical constraint** | Do not assert that MDI is directly replicable outside California. Assert that its functional logic is portable and that the adaptation principles allow local instantiation. |
| **Target length** | 2,500–3,500 words |
| **Status** | 🔲 Pending |

---

### 03 — What the Evidence from Comparable Models Shows
| Field | Value |
|---|---|
| **File** | `03_What_Evidence_from_Comparable_Models_Shows.md` |
| **Phase** | 3 |
| **Type** | New chapter |
| **Integration location** | Insert as **Chapter 25A** between Chapter 25 ("Comparative Models") and Chapter 26 ("Community, Opposition, and Democracy"). Chapter 25 critiques alternatives. Chapter 25A provides the positive evidence base for MDI-adjacent interventions. Update the table of contents accordingly. |
| **Dependencies** | None. Can be drafted in parallel with other deliverables. |
| **Research required** | Finland Y-Foundation (Asunto Ensin): housing retention rates, cost-savings data, psychiatric outcome data. Medical respite / recuperative care programs: National Institute for Medical Respite Care outcome data; Buchanan et al. studies on medical respite. ACT team outcomes for chronic homelessness with psychiatric comorbidity: Assertive Community Treatment Association data; Bond et al. (2001); Stein & Test (1980) follow-up literature. Inpatient psychiatric stabilization as Phase Zero analog: average LOS data, discharge outcome rates. Housing First RCT data (Pathways to Housing; At Home/Chez Soi Canada): retention rates, cost offsets, psychiatric outcomes. |
| **Chapter structure** | Introduction (what this chapter does and does not claim). Section per model: what the model does → what outcome data exists → which MDI claims it supports → where MDI extends beyond what the model has tested. Conclusion: summary of what is supported, what is novel and untested, and what the nested RCT in Metric 7 is designed to resolve. |
| **Critical constraint** | The chapter must not claim MDI outcome data that does not exist. It draws on adjacent evidence. Every supported claim must be traceable to a specific cited finding. Claims that are novel to MDI must be clearly marked as such. |
| **Target length** | 4,000–5,500 words |
| **Status** | 🔲 Pending |

---

### 04 — Chapter 15 Additions: Threshold Contextualization and RCT Specification
| Field | Value |
|---|---|
| **File** | `04_Chapter_15_Additions_Threshold_Contextualization.md` |
| **Phase** | 3 |
| **Type** | Section revision — additive |
| **Integration location** | Insert after the existing section "What Clearance Is and Is Not" at the end of Chapter 15 ("Metabolic Stabilization"). The existing text already acknowledges the threshold is provisional; this addition contextualizes it and specifies the validation pathway. |
| **Dependencies** | `03` should be drafted first; this section references comparable ADL tools found in that research. |
| **Research required** | Barthel Index (Mahoney & Barthel, 1965): structure, scoring, inter-rater reliability data. Functional Independence Measure (FIM): psychiatric application evidence. UCSD Performance-Based Skills Assessment (UPSA): relevance to MDI clearance indicators. Activities of Daily Living scales in medical respite literature. Nested RCT design standards: Consort 2010 extension for cluster trials; intent-to-treat methodology for housing interventions. |
| **Section structure** | (1) Comparable clinical tools: what existing ADL and capacity tools measure, how they relate to the five MDI clearance indicators, why a direct application is not appropriate and a MDI-specific validation is required. (2) RCT specification: primary outcome measure, secondary outcomes, sample size rationale, randomization unit, timeline, intent-to-treat analysis plan, data custodian. (3) Interim protocol: who holds override authority, what documentation is required, what the review schedule is during the calibration period before the RCT generates validated thresholds. |
| **Critical constraint** | Do not present existing ADL tools as validating the 40% threshold. They contextualize it. The distinction between contextualization and validation must be maintained throughout. |
| **Target length** | 1,200–1,800 words |
| **Status** | 🔲 Pending |

---

### 05 — Chapter 16 Additions: Anosognosia Diagnostic Standard
| Field | Value |
|---|---|
| **File** | `05_Chapter_16_Additions_Anosognosia_Diagnostic_Standard.md` |
| **Phase** | 4 |
| **Type** | Section revision — additive |
| **Integration location** | Insert as a new section titled **"Diagnostic Standards for Anosognosia Determination"** in Chapter 16 ("Legal Instruments for Compelled Care"), placed immediately after the existing section "Anosognosia: The Clinical Foundation" and before "California's Three Legal Instruments." |
| **Dependencies** | None. Can be drafted independently. |
| **Research required** | Scale to assess Unawareness of Mental Disorder (SUMD — Amador et al., 1993): structure, subscales, inter-rater reliability, clinical feasibility in field settings. Beck Cognitive Insight Scale (BCIS): comparison to SUMD for field application. Structured Clinical Interview for DSM (SCID) anosognosia module. California Welfare and Institutions Code Section 5008(h): legal definition of "gravely disabled" and its relationship to anosognosia as a clinical construct. Inter-rater reliability literature for anosognosia assessment in community settings. |
| **Section structure** | (1) Diagnostic instrument: which validated tool is used (specify SUMD or equivalent), minimum clinician qualification to administer, training requirement, documentation standard. (2) Second-opinion requirement: who provides the independent review, timeline, and documentation. (3) Appeals pathway: formal process by which the individual contests the determination, timeline for hearing, legal representation access, standard of evidence. (4) Scheduled review: frequency of re-assessment during compelled care, who conducts it, what triggers early termination of compulsion. (5) Decoupling statement: explicit statement that this diagnostic standard is a clinical process entirely separated from law enforcement, criminal records, and arrest. |
| **Critical constraint** | The section must make clear that anosognosia determination is a clinical act requiring documented clinical evidence, not an administrative decision. The individual's rights during the determination process must be explicit. |
| **Target length** | 1,500–2,000 words |
| **Status** | 🔲 Pending |

---

### 06 — Pipeline D Addition
| Field | Value |
|---|---|
| **File** | `06_Pipeline_D_Addition.md` |
| **Phase** | 4 |
| **Type** | Section revision — additive |
| **Integration location** | Insert as an extended concluding section of the Pipeline D description, wherever Pipeline D is currently defined in the manuscript (framework diagram places it at approximately Chapter 11 or the pipeline architecture chapter). The addition follows the existing constraint statement ("No legal instrument applies") and provides the positive account. |
| **Dependencies** | `01_Capability_to_Specification_Translation.md` — the addition grounds Pipeline D's positive offering in specific Nussbaum capabilities, so the translation table should be referenced. |
| **Content required** | What harm reduction services are specifically available without placement requirement (cite Harm Reduction International, 2022, already in bibliography). How the standing offer is communicated, maintained, and renewed over time without coercion. What non-residential MDI services engage Nussbaum's remaining capabilities for Pipeline D: play (Capability 9), practical reason (Capability 6), affiliation (Capability 7), other species (Capability 8). Connection to biophilic infrastructure that Pipeline D can access without residential placement. What the Gardien pathway offers without requiring pod placement. The explicit statement that Pipeline D's choice is recognized as a valid exercise of Sen's capability framework — not a failure of MDI engagement. |
| **Critical constraint** | Must not introduce any coercive element or implicit pressure toward placement. The standing offer must be genuinely unconditional. Do not frame outdoor living as pathological for this cohort. |
| **Target length** | 400–600 words |
| **Status** | 🔲 Pending |

---

### 07 — Chapter 7 Addition: Scholarly Context Paragraph
| Field | Value |
|---|---|
| **File** | `07_Chapter_7_Addition_Scholarly_Context.md` |
| **Phase** | 5 |
| **Type** | Section revision — additive |
| **Integration location** | Insert as a new paragraph at the end of the section "Nussbaum's Human Capabilities List" in Chapter 7 ("The Capability Approach"), before the section "The Sequential Resolution." |
| **Dependencies** | Requires fetching and reading: (1) Clark, Seager & Chester (2018), *Environment Systems and Decisions* 38(3):339–352 — available on ResearchGate and ASU repository. (2) Aguilera, Osman & Curto (2025), IJCAI 2025 — available at arxiv.org/abs/2503.18389. (3) DiBella SSRN papers 5968756, 6211658, 6579600 — check for cross-reference consistency. |
| **Content required** | One paragraph (200–350 words) situating MDI in relation to the two closest prior attempts to connect capability theory to operational systems. Clark et al. (2018): applies capability approach to infrastructure prioritization — identifies which infrastructure sectors are most critical based on which central capabilities they support. Aguilera et al. (2025): implements capability approach as a computational policy simulation for homelessness. State precisely how MDI differs from both: MDI is a physical delivery system, not a prioritization tool (Clark) or a simulation framework (Aguilera). MDI does not ask which infrastructure is most important — it answers what the infrastructure must physically be. The paragraph closes: *"For the full derivation of engineering parameters from each of Nussbaum's ten capabilities, see Appendix A."* |
| **Critical constraint** | Do not claim MDI is superior to Clark et al. or Aguilera et al. State the distinction accurately. All three occupy different positions in the same space. Do not fabricate claims about what those papers argue — read them before writing. |
| **Target length** | 200–350 words |
| **Status** | 🔲 Pending |

---

### 08 — Updated Bibliography
| Field | Value |
|---|---|
| **File** | `08_Updated_Bibliography.md` |
| **Phase** | 6 |
| **Type** | Bibliography replacement |
| **Integration location** | Replace existing bibliography section entirely. Maintain the existing chapter-by-chapter organization. Add entries under relevant chapter headings. Add new chapter headings for new deliverables (Appendix A, Appendix B, Chapter 25A). |
| **Dependencies** | All other deliverables (01–07) must be complete. All new citations used in those deliverables are collected here. |
| **New entries to add (minimum):** | Clark, Susan Spierre, Thomas P. Seager, and Mikhail V. Chester. "A Capabilities Approach to the Prioritization of Critical Infrastructure." *Environment Systems and Decisions* 38, no. 3 (2018): 339–352. |
| | Aguilera, Alba, Nardine Osman, and Georgina Curto. "Agent-based Modeling meets the Capability Approach for Human Development: Simulating Homelessness Policy-making." *Proceedings of the Thirty-Fourth International Joint Conference on Artificial Intelligence (IJCAI-25)*, 2025: 9520–9528. |
| | Amador, Xavier F., et al. "Assessment of Insight in Psychosis." *American Journal of Psychiatry* 150, no. 6 (1993): 873–879. (SUMD) |
| | Mahoney, Florence I., and Dorothea W. Barthel. "Functional Evaluation: The Barthel Index." *Maryland State Medical Journal* 14 (1965): 61–65. |
| | National Institute for Medical Respite Care. [Relevant outcome publication — agent to identify correct citation after research.] |
| | Y-Foundation (Y-Säätiö). *Housing First in Finland: Results and Learning.* Helsinki: Y-Säätiö, [agent to verify year and exact title.] |
| | European Commission / New European Bauhaus. "Structurally Addressing Homelessness through Coordinated Social Infrastructure and Services in Neighbourhoods." Horizon Europe Work Programme 2026–2027, HORIZON-NEB-2026-01-BUSINESS-01. Brussels: European Commission, 2025. |
| **Critical constraint** | Do not invent citations. If a source cannot be retrieved and verified, mark it as [VERIFICATION REQUIRED] with a note describing what it should contain. No fabricated author names, journal names, years, or page numbers. |
| **Status** | 🔲 Pending |

---

## 4. Dependency Graph

```
00_Index_Manifest
        │
        ├──► 01_Capability_to_Specification_Translation   (no upstream dependency)
        │         │
        │         └──► 06_Pipeline_D_Addition              (references 01 table)
        │
        ├──► 03_What_Evidence_from_Comparable_Models       (no upstream dependency)
        │         │
        │         └──► 04_Chapter_15_Additions             (references 03 research)
        │
        ├──► 05_Chapter_16_Additions                       (no upstream dependency)
        │
        ├──► 07_Chapter_7_Addition                         (requires fetching Clark + Aguilera)
        │         │
        │         └──► 02_MDI_Outside_California           (references 07 framing)
        │
        └──► 08_Updated_Bibliography                       (depends on ALL above)
```

**Recommended execution sequence for parallel efficiency:**
- Batch A (no dependencies, start immediately): 01, 03, 05, 07
- Batch B (after Batch A): 06 (after 01), 04 (after 03), 02 (after 07)
- Batch C (final): 08 (after all above)

---

## 5. Internal Consistency Checks (Phase 6 Audit)

The following inconsistencies were identified during manuscript analysis and must be
resolved before the bibliography is finalized:

**Dunbar Pod resident count:** The manuscript uses 154. The framework diagram at
bikepaths.org/mdi uses 154. Dunbar's published neocortex-group-size data identifies
a range of approximately 100–230, with 150 as the most frequently cited point estimate.
The agent must: (a) read Dunbar (1992) and identify the exact figure and its derivation;
(b) confirm whether 154 is DiBella's deliberate specification above Dunbar's 150, and
if so, note the rationale; (c) ensure the number is identical across all deliverables and
the manuscript. If 154 requires a brief defense, add one sentence to Appendix A.

**Five clearance indicators vs. framework diagram:** Manuscript Chapter 15 lists five
indicators. The framework diagram lists five indicators. Verify they are identical in
wording. If any discrepancy exists, flag it for the author's resolution — do not resolve
it independently.

**Eight binary verification metrics:** Verify all eight metrics listed on bikepaths.org/mdi
appear somewhere in the manuscript. Metric 7 (nested RCT) is the one most requiring
expansion — it is addressed in deliverable 04. Confirm Metrics 1–6 and 8 are present
in the main text or in the falsifiability clause.

**SSRN cross-reference:** Fetch papers 5968756, 6211658, and 6579600. Identify any
claims in those papers that are not present in the manuscript and flag them for the author.
Identify any claims in the manuscript that contradict the SSRN papers and flag them.
Do not resolve contradictions — flag only.

---

## 6. Global Constraints (Apply to All Deliverables)

1. **No fabricated citations.** If a source cannot be retrieved, mark [VERIFICATION
   REQUIRED] and describe what it needs to contain.

2. **No overstatement of evidence.** Where evidence is analogous rather than direct,
   say so. Where a claim is novel to MDI and untested, say so.

3. **Do not alter the falsifiability clause.** It appears in Chapter 23 / the framework
   diagram. No deliverable weakens, softens, or removes it.

4. **Do not introduce coercive elements into Pipeline D.** The constraint is correct
   and must be preserved across all deliverables.

5. **Do not resolve the 40% threshold by presenting it as validated.** It is provisional.
   Deliverable 04 contextualizes it and specifies its validation pathway. That is the
   limit of what the evidence supports.

6. **Maintain the manuscript's voice.** The book is addressed to citizens, not academics.
   New sections must match the existing register: precise, direct, without academic
   hedging, but also without overpromising.

7. **Deliver each file separately.** Do not embed deliverables into the source manuscript.
   The author integrates them.

---

## 7. Status Summary

| File | Phase | Type | Status |
|---|---|---|---|
| `00_Index_Manifest.md` | 1 | Planning | ✅ Complete |
| `01_Capability_to_Specification_Translation.md` | 2 | New Appendix | 🔲 Pending |
| `02_MDI_Outside_California_Adaptation_Principles.md` | 5 | New Appendix | 🔲 Pending |
| `03_What_Evidence_from_Comparable_Models_Shows.md` | 3 | New Chapter | 🔲 Pending |
| `04_Chapter_15_Additions_Threshold_Contextualization.md` | 3 | Section Revision | 🔲 Pending |
| `05_Chapter_16_Additions_Anosognosia_Diagnostic_Standard.md` | 4 | Section Revision | 🔲 Pending |
| `06_Pipeline_D_Addition.md` | 4 | Section Revision | 🔲 Pending |
| `07_Chapter_7_Addition_Scholarly_Context.md` | 5 | Section Revision | 🔲 Pending |
| `08_Updated_Bibliography.md` | 6 | Bibliography | 🔲 Pending |

---

*Material Dignity Infrastructure · Charles J. DiBella · kdp_v4 Refactor*  
*Manifest produced June 2026*
