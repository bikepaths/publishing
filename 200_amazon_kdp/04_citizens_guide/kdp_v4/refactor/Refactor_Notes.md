# Refactor kdp_v3

**TARGET**

/home/user0/git/publishing/200_amazon_kdp/04_citizens_guide/kdp_v3/manuscript/full_manuscript.md

**CONTEXT**

The manuscript is *Fixing Skid Row* by Charles J. DiBella, a citizen's guide to the Material Dignity Infrastructure (MDI) model. It is complete in structure but has seven documented gaps. The agent's task is to close those gaps through research, drafting, and integration — without fabricating data, inventing citations, or overstating the evidence base where it does not yet exist.

---

**TASK 1 — Build the translation methodology**

This is the most important task. Execute it first.

Read Chapter 7 (The Capability Approach) and Chapters 9–15 (the physical specifications) in full. For each of Nussbaum's ten capabilities, construct a mapping table showing: the capability as stated, the physical/clinical condition that MDI provides to secure it, and the specific engineering parameter that operationalizes that condition. For example: Capability 2 (Bodily Health) → adequate sleep → STC 65 acoustic isolation and circadian lighting system.

For each engineering parameter, search the literature for the evidence that supports that specific value. For STC 65: search acoustic standards in psychiatric inpatient design. For 154 residents: fetch Dunbar (1992) and Dunbar (2021) and extract the specific cognitive ceiling data. For 30 days: search prefrontal cortex recovery timelines in chronic stress and sleep deprivation literature.

Draft this as a new appendix titled "Capability-to-Specification Translation: The Engineering Derivation of MDI Parameters." This is the paper still missing from the framework. It should be rigorous enough for an academic audience.

---

**TASK 2 — Validate or contextualize the 40% clearance threshold**

Search for existing validated clinical tools that measure Activities of Daily Living recovery in psychiatric populations: the Barthel Index, the Functional Independence Measure, the UCSD Performance-Based Skills Assessment. Search for clearance criteria used in medical respite programs and psychiatric step-down units.

Draft a section for Chapter 15 that: (a) acknowledges the threshold is provisional, as the manuscript already does; (b) contextualizes it against the closest existing validated tools; (c) specifies the nested RCT design that will validate it, including outcome measures, timeline, and sample size requirements; and (d) specifies what the system does during the calibration period — who has override authority, what documentation is required, and what the review schedule is.

Do not present the threshold as validated. Present it as a provisional parameter grounded in adjacent evidence, awaiting MDI-specific validation.

---

**TASK 3 — Build the comparable evidence chapter**

Search for outcome data from: Finland's Y-Foundation Housing First program (Asunto Ensin); medical respite and recuperative care programs in the United States (search the National Institute for Medical Respite Care); ACT team outcomes for chronic homelessness with psychiatric comorbidity; inpatient psychiatric stabilization outcomes as analogs for Phase Zero.

Draft a new chapter titled "What the Evidence from Comparable Models Shows." Structure it as: what each comparable model does, what outcome data it has produced, which elements of MDI it supports, and where MDI extends beyond what those models have tested. Be precise about which MDI claims are supported by comparable evidence and which are novel and untested.

This chapter answers the citizen reader's reasonable question: why should I trust a model that has never been built?

---

**TASK 4 — Specify the anosognosia diagnostic standard**

Fetch and read: Amador's SUMD (Scale to assess Unawareness of Mental Disorder); the Beck Cognitive Insight Scale; existing California legal standards for capacity determination under LPS Conservatorship (Welfare and Institutions Code Section 5008). Search for peer-reviewed literature on inter-rater reliability of anosognosia assessment.

Draft a section for Chapter 16 titled "Diagnostic Standards for Anosognosia Determination" specifying: which validated instrument(s) are used, minimum clinician qualification, required second-opinion structure, documentation standard, formal appeals pathway for the individual, and scheduled review frequency during compelled care. This section is the accountability architecture for the most ethically sensitive element of the framework.

---

**TASK 5 — Draft the international adaptation framework**

Draft a new appendix titled "MDI Outside California: Adaptation Principles." Structure it as three sections. First: the elements of MDI that are universal and require no adaptation (the neuroscientific foundation, the pipeline categorization, the Dunbar Pod architecture, the Phase Zero/Sen Phase sequence). Second: the elements that require local translation (legal instruments for compelled care, financing mechanisms, building acquisition pathways, data infrastructure). Third: for each element requiring translation, provide the principle that should govern its adaptation and one or two concrete examples from other legal systems. Research UK Mental Health Act provisions, Canadian provincial mental health legislation, and Finnish social housing financing as examples.

This appendix transforms MDI from a California model into a portable framework.

---

**TASK 6 — Develop the Pipeline D section**

The current manuscript tells the reader what MDI does not do to Pipeline D. Draft an addition to the Pipeline D section that states what MDI does for them: what harm reduction services are available, how the standing offer is maintained and communicated over time, what the Gardien pathway offers without requiring placement, and how Pipeline D individuals connect to Nussbaum's remaining capabilities (play, practical reason, affiliation, other species) through non-residential MDI services. This should be approximately 400 words, matching the depth given to other pipelines.

---

**TASK 7 — Integrate the existing scholarly literature**

Fetch the following papers in full or in maximum available excerpt:

Clark, Seager, and Chester (2018), "A capabilities approach to the prioritization of critical infrastructure," *Environment Systems and Decisions* 38(3). Available on ResearchGate.

Aguilera, Osman, and Curto (2025), "Agent-based Modeling meets the Capability Approach for Human Development: Simulating Homelessness Policy-making," IJCAI 2025. Available at arxiv.org/abs/2503.18389.

Fetch the three DiBella SSRN papers at papers.ssrn.com: abstract IDs 5968756, 6211658, 6579600. Read for cross-referencing and consistency.

Add citations to Clark et al. and Aguilera et al. in Chapter 7, with a paragraph in that chapter situating MDI in relation to these prior attempts. The paragraph should acknowledge that the capability-to-infrastructure translation has been attempted in critical infrastructure prioritization (Clark et al.) and in computational policy modeling (Aguilera et al.), and state precisely how MDI differs: it is a physical delivery system rather than a prioritization tool or a simulation framework.

Update the bibliography accordingly.

---

**TASK 8 — Internal consistency check**

After completing Tasks 1–7, perform the following checks before finalizing:

Verify that the Dunbar Pod resident count is consistent throughout the manuscript and with the framework diagram (154 vs 150 — Dunbar's published range is 100–230; the manuscript should settle on one number and defend it).

Verify that the five Phase Zero clearance indicators in Chapter 15 are consistent with the clearance indicators in the framework diagram.

Verify that the eight binary verification metrics on the framework page at bikepaths.org/mdi are all addressed in the manuscript, either in the main text or in the falsifiability appendix. Metric 7 (nested RCT requirement) should now reference the validation protocol drafted in Task 2.

Verify that no claim in the new sections overstates the evidence base. Every empirical claim must be traceable to a cited source. Every provisional claim must be labeled as such.

---

**CONSTRAINTS**

Do not fabricate citations. If a paper cannot be retrieved, note that it could not be accessed and describe what it would need to contain to support the claim.

Do not remove the falsifiability clause or soften it. It is the manuscript's most important intellectual commitment.

Do not resolve the 40% threshold by claiming it is validated. It is not. The task is to contextualize it and specify how it will be validated.

Do not extend Pipeline D into compelled care territory. The manuscript's constraint on Pipeline D is correct and must be preserved.

---

**OUTPUTS**

Produce the following files, ready for integration into the manuscript:

One appendix document: "Capability-to-Specification Translation"

One appendix document: "MDI Outside California: Adaptation Principles"

One new chapter document: "What the Evidence from Comparable Models Shows"

One revised section: Chapter 15 additions (threshold contextualization and RCT specification)

One revised section: Chapter 16 additions (anosognosia diagnostic standard)

One revised section: Pipeline D addition

One revised section: Chapter 7 addition (scholarly context paragraph and citations)

One updated bibliography

Deliver each as a separate file. Do not embed them in the manuscript directly — the author integrates them.

Deliverables ...

/home/user0/git/publishing/200_amazon_kdp/04_citizens_guide/kdp_v4/refactor/00_Index_Manifest.md

/home/user0/git/publishing/200_amazon_kdp/04_citizens_guide/kdp_v4/refactor/01_Capability_to_Specification_Translation.md

/home/user0/git/publishing/200_amazon_kdp/04_citizens_guide/kdp_v4/refactor/02_ continue ...


