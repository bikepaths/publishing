# Handoff Manifest — Economic Dignity Infrastructure Paper Series
Repository: bikepaths/publishing
Prepared for: handoff agent (LaTeX processing stage)
Prepared by: review session, Global Youth Learning Collective

## 1. Purpose of this manifest

This document records the complete review and revision workflow performed on Papers 1 through 5 of the Dignity Infrastructure series, so a receiving agent can pick up the work without needing the original conversation. It states what was checked, what was found, what was fixed, what was verified after fixing, and what remains open.

## 2. Source documents in scope

| Paper | Title (short) | Source path (original) | Source path (revised) |
|---|---|---|---|
| 1 | Material Dignity Infrastructure (MDI) | `/published/ssrn/ssrn-5968756/ssrn-5968756.md` | `/published/ssrn/ssrn-5968756/ssrn-5968756_Revised.md` |
| 2 | Structural Misalignment / National Stability Utility | `/published/ssrn/ssrn-6211658/ssrn-6211658.tex` | `/published/ssrn/ssrn-6211658/ssrn-6211658_Revised.md` |
| 3 | Los Angeles MDI | `/published/ssrn/ssrn-6579600/ssrn-6579600.tex` | `/published/ssrn/ssrn-6579600/ssrn-6579600_Revised.md` |
| 4 | Relational Dignity Infrastructure (RDI) | `/published/ssrn/ssrn-6881539/ssrn-6881539_Manuscript.md` | `/published/ssrn/ssrn-6881539/ssrn-6881539_Revised.md` |
| 5 | Economic Dignity Infrastructure (EDI) — draft, not yet published | `/300_working_papers/working/05_economic_dignity/01_drafts/manuscript_draft.md` | see `manuscript_draft_final.md` in this handoff package |


## 3. Workflow performed, in order

1. **Initial read of Paper 5 draft.** Establishing claims, checking citations against the bibliography, checking internal arithmetic.
2. **Read of Papers 1, 2, 4 in full**, to establish whether the foundation Paper 5 depends on was sound.
3. **Read of Paper 3 in full.** This paper surfaced the most serious issues, including a civil-liberties inconsistency and a legally risky contractual mechanism.
4. **Citation verification against external sources** (web search), not assumption. Specific citations checked and their real-world accuracy confirmed or disconfirmed:
   - Côté & Levine (2002) — confirmed real, correctly used in Paper 4; found incorrectly cited in Paper 5's original bibliography.
   - LePage et al. (2021), *Medical Care* — confirmed real; found misattributed in Paper 5's original bibliography as "O'Connell, *Psychiatric Services*, 2021," a source that could not be located.
   - Invitation Homes vacancy-rate claim in Paper 2 — checked against the company's own SEC filings; found false as originally stated (actual occupancy 97.7–97.8%, i.e., low vacancy, not high).
   - White & Cloud (2008) — confirmed real and correctly used.
   - Arnsten (2009), Khantzian (1985), Volkow/Koob (2016) — confirmed real, added to Paper 5 to support new material (see Section 5 below).
5. **Arithmetic verification**, performed independently rather than trusted from the text:
   - Paper 1 cost table: confirmed correct.
   - Paper 3 capital recovery timelines (29 / 45 / 71 months): confirmed correct.
   - Paper 5 Section V funding model: found a discrepancy — stated revenue ($1.56M) does not cover stated costs ($2.0M), leaving an undisclosed $440,000 annual gap.
6. **Compilation of revision log**, a self-contained blueprint listing every open item found in Papers 1–4, with location, problem, and required action, written so it could be executed without reference to the original conversation.
7. **Handoff and independent verification.** After a separate revision pass was performed on Papers 1–4 (by a different agent, using the revision log as the instruction set), each fix was independently re-checked against the actual revised text files before being trusted. First-pass claims of completion were not taken at face value; two papers initially had to be re-checked and were found unrevised on first inspection, then confirmed genuinely revised once the correct `_Revised.md` paths were located and read.
8. **Paper 5 finalization**, performed directly:
   - Both broken bibliography entries corrected to match verified real sources.
   - Funding gap disclosed explicitly in-text rather than left implicit.
   - New physiological/relational grounding subsection added (Section III.a), with explicit in-text attribution to Paper 4 (RDI) rather than presenting the concepts as originating in Paper 5.
   - Scattered-site housing claims reconciled with Paper 1 and Paper 3's own favorable citation of Tsemberis (2004), removing an internal contradiction identified earlier in review.

## 4. Verified-resolved items (Papers 1–4)

All items below were checked against the actual `_Revised.md` files, not assumed from a change log.

- **Paper 1:** Retention-rate figures (86%, 92%) now explicitly labeled as self-reported, not independently verified. RESOLVED.
- **Paper 2:** False Invitation Homes vacancy-rate statistic removed. RESOLVED.
- **Paper 3:** Stewardship Authority's role as petitioner/recipient-on-behalf-of-conservatee in involuntary proceedings removed; text now explicitly disclaims any active role in CARE Court, AOT, or LPS conservatorship proceedings. RESOLVED.
- **Paper 3:** FLIR thermal drone surveillance proposal removed; replaced with general aerial survey language bounded by Fourth Amendment compliance, avoiding the unaddressed *Kyllo v. United States* (2001) gap. RESOLVED.
- **Paper 3:** "Stewardship Contract" mechanism now carries an explicit Legal Risk Acknowledgment section, citing AB 1482 and stating the mechanism is legally untested pending counsel review. RESOLVED.
- **Paper 4:** No issues found across two review passes.

## 5. Paper 5 — current status

**Fixed:**
- `cote2002social` (broken) replaced with `cote2002identity` (Côté & Levine, 2002), matching Paper 4's correct citation.
- `oconnell2021randomized` (unlocatable) replaced with `lepage2021individualized` (LePage et al., 2021, *Medical Care*).
- Section V funding model now explicitly discloses the ~$440,000 annual gap between modeled costs and modeled revenue, with three unmodeled options for closing it named but not asserted as decided.
- New Section III.a added, grounding identity capital / agentive selfhood in cited neuroscience (Arnsten 2009; Khantzian 1985; Volkow, Koob & McLellan 2016), explicitly attributed to Paper 4 (RDI) rather than presented as new theory.
- Scattered-site housing framing corrected to match, not contradict, Papers 1 and 3's favorable use of Tsemberis (2004).

- Section II glucose-depletion citation: removed contested Gailliot et al. (2007) citation, rewrote relying on Mullainathan and Shafir (2013) scarcity-induced cognitive load framework. RESOLVED.
- Section III.a encampment network hypothesis: explicitly relabeled as a structural hypothesis rather than an established finding. RESOLVED.

## 6. Files included in this handoff package

- `manuscript_draft_final.md` — current full text of Paper 5, completely resolved.
- `bibliography_final.bib` — current bibliography for Paper 5, including all corrected and newly added entries.
- `README.md` — this file.

## 7. Required next steps for the receiving agent

1. Convert `manuscript_draft_final.md` and `bibliography_final.bib` to LaTeX per the group's stated output requirement.
2. Papers 1–4 are verified complete as of this handoff and do not require further revision unless new issues are identified during LaTeX conversion (e.g., citation key mismatches).
3. Any new factual or citation claims introduced during LaTeX formatting should be verified against original sources before submission, following the same standard applied throughout this review: confirm against the real source, do not assume accuracy from the draft text alone.
