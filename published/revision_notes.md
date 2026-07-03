# Revision Notes and Blueprint — Papers 1 through 4
Handoff document for redrafting agent. Output format: LaTeX. Papers 1–4 must be finalized and internally consistent before Paper 5 is reconstructed on top of them.

Each item below is self-contained: location, problem, and required action. Confidence level is marked because not all items carry the same certainty — some are verified factual errors, some are internal-consistency fixes, some are advisory (legal/framing risk that the group must consciously accept or address, not a fact that is simply "wrong").

Status key: [OPEN] not yet fixed — [DECIDED] approach chosen, text not yet edited — [CLEAR] no revision needed

---

## PAPER 1 — Material Dignity Infrastructure (source: ssrn-5968756)

**Verified sound, no structural issues.** Core citations confirmed accurate: Sen (1999), Nussbaum (2011), Jacobs (1961), Dear & Wolch (1987), Tsemberis et al. (2004), Larimer et al. (2009), *South Dakota v. Dole* (1987). Cost table arithmetic in Section 5.2.1 independently recomputed and confirmed correct ($11,600 gross direct cost; $13,600 net public cost after $10,000 tax credit and $8,000 emergency offset).

### Item 1.1 [OPEN] — Confidence: HIGH (sourcing problem, not a factual error)
- **Location:** Retention-rate statistics — 86% figure for Community First! Village, 92% figure for Grace Marketplace.
- **Problem:** Sourced to a Substack post and a nonprofit's self-reported figures (via CauseIQ) rather than independent or peer-reviewed evaluation.
- **Required action:** Search for an independently verified/peer-reviewed source for these retention rates. If none exists, retain the figures but add an explicit qualifier in-text (e.g., "self-reported, not independently verified") and flag the same in a footnote or limitations section.

---

## PAPER 2 — Structural Misalignment / National Stability Utility (source: ssrn-6211658)

**Verified sound in its theoretical core.** Citations to Beer, Ashby, and Wiener (cybernetics), and to Aalbers (2016), Rothstein (2017), and Desmond (2016) are confirmed real and correctly used. Paper explicitly discloses its own scope limits (no cost model, no legislative roadmap) — retain this disclosure as-is.

### Item 2.1 [OPEN] — Confidence: HIGH (factually disproven, not just unverified)
- **Location:** Claim that "Invitation Homes maintains vacancy rates 40 percent higher than traditional landlords," attributed to Christophers (2023).
- **Problem:** Directly contradicted by Invitation Homes' own SEC filings, which report average occupancy of 97.7%–97.8% across 2023 (implied vacancy of roughly 2–3%, which is low, not high). Large corporate landlords have strong financial incentive to minimize vacancy. The claim as stated is false.
- **Required action:** Delete this claim. Do not attempt to soften it — the specific "40 percent higher" figure has no support in available data and should not appear in the resubmitted paper. If the underlying argument (corporate landlords behave differently from small landlords) still needs a supporting statistic, a new, independently verified figure must be sourced — do not reuse this one.

---

## PAPER 3 — Los Angeles MDI (source: ssrn-6579600)

**Financial model verified.** Capital recovery timelines (29/45/71 months under best/probable/worst case) independently recomputed and confirmed correct. Citation to *City of Grants Pass v. Johnson* (2024) confirmed accurate and relevant.

### Item 3.1 [DECIDED] — Confidence: HIGH (internal contradiction, confirmed group intent)
- **Location:** Section 4 ("Legal Lever System"), specifically the description of the Stewardship Authority as an active petitioner in CARE Court proceedings, and the passage describing a conservator "accepting the ALMU unit on the individual's behalf."
- **Problem:** Contradicts Section 2.2's "voluntary residency" framing and the "Anti-Detention Covenant." The group has confirmed (this session) that the intended design is: **MDI stays fully outside the involuntary system.**
- **Required action:** Rewrite Section 4 so that the Stewardship Authority has no active role in initiating, petitioning for, or participating in any involuntary commitment or conservatorship proceeding. MDI units may still be one housing option that a court or conservator selects independently, through normal, existing channels — but the Authority itself must not file petitions, act as petitioner, or receive a unit on a conservatee's behalf. Any language implying an active institutional role in compelling entry must be removed.

### Item 3.2 [OPEN] — Confidence: HIGH (missing controlling precedent)
- **Location:** Section 1.1, FLIR thermal drone surveillance proposal. Currently cites "Supreme Court of the United States, 1986, 1989" (likely referring to older aerial-surveillance cases).
- **Problem:** Does not cite or address *Kyllo v. United States* (2001), the controlling modern precedent holding that warrantless use of thermal-imaging technology to observe inside a space constitutes a Fourth Amendment search.
- **Required action:** Either (a) add a legal analysis section addressing *Kyllo* directly and explaining how the proposed drone surveillance would or would not comply with it, or (b) remove or substantially rescope the FLIR drone surveillance proposal if compliance cannot be demonstrated.

### Item 3.3 [OPEN] — Confidence: MEDIUM (advisory / legal risk, not a factual error)
- **Location:** "Stewardship Contract" mechanism, framed as a "non-property interest" intended to place residents outside housing court jurisdiction and standard eviction protections.
- **Problem:** This is a legal design choice, not a factual claim, so it cannot be "fact-checked" the way Item 2.1 was. However, it carries real, foreseeable legal risk: courts generally examine the substance of a living arrangement rather than the label a contract assigns it, and many jurisdictions restrict a landlord's ability to contract away statutory tenant protections.
- **Required action:** The redrafting agent should not simply delete this mechanism (that is a policy decision for the authors, not a correction of fact). Instead, add a section directly acknowledging this legal risk, citing real precedent on contractual tenancy classification, and stating explicitly whether the proposal is offered as legally tested or as a legally untested design requiring further legal review before implementation. This item is independent of Item 3.1 — it applies even to fully voluntary residents.

---

## PAPER 4 — Relational Dignity Infrastructure / RDI (source: ssrn-6881539)

**[CLEAR — no revision needed.]** Passed two full review passes. "Identity capital" and "agentive selfhood" are correctly defined and cited to Côté and Levine (2002), *Identity Formation, Agency, and Culture*. "Recovery capital" is correctly cited to White & Cloud (2008), *Counselor*, 9(5), 22–27. No factual, arithmetic, or internal-consistency issues found.

---

## CROSS-CUTTING NOTE FOR PAPER 5 (not yet submitted — for awareness only, not part of the 1–4 handoff)
Paper 5 is not in scope for this revision pass, but the redrafting agent should be aware of two items that will need to be resolved before Paper 5 can build on Papers 1–4:
- Paper 5's bibliography.bib contains two citation errors: the "cote2002social" entry conflates two unrelated real papers under one incorrect title/author combination (correct citation should match Paper 4's Côté and Levine 2002 entry); the "oconnell2021randomized" entry does not match any locatable source (the real, matching study is LePage et al., 2021, *Medical Care* — not "O'Connell, *Psychiatric Services*, 2021").
- Paper 5 Section V's funding model has an unexplained $440,000 annual gap between stated total costs ($2.0M) and stated total revenue ($1.56M combined from internal cooperative recapture and Medi-Cal billing).

---

## OUTPUT FORMAT REQUIREMENT
Final deliverables for Papers 1–4 must be produced in LaTeX.
