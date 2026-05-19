---
name: kdp-manuscript-editing
description: Consolidated workflow for editing KDP manuscript markdown files – includes style passes, Git operations, and verification.
category: publishing
version: 1.1
trigger: "When editing chapter files in rithythul/publishing"
---

# Overview
This single skill replaces the previous three separate skills. It defines a repeatable, hardened five‑pass revision process, safe Git actions, and mandatory verification before reporting success.

## Pre‑revision checklist
1. Review `profile.md` for tone, voice, and style preferences.
2. Review `Manual_of_Style.md` for current style rules.
3. Review `Manuscript_Outline.md` to ensure chapter objectives align.
4. **Mandatory Pre-Draft Logic Block:** Output a logic block defining the Character Pivot and the Structural Pivot for the target chapter. Establish the causal relationship between the specific human action and the systemic failure before initiating revisions.

## Revision Passes (hardening)
### PASS 1 – Structural foundation
- Segment draft into logical paragraphs (3‑7 sentences each).
- Verify each sentence ends with a proper punctuation mark and is not a fragment.
- Flag paragraphs with <3 or >7 sentences.

### PASS 2 – Mechanical corrections
- Replace all em‑dashes (`—`, `–`) with commas or rephrased clauses.
- Expand every acronym/jargon at first occurrence.
- Remove bracketed notation; integrate its content or move to footnote.

### PASS 3 – Sentence quality & rhythm
- Eliminate causal‑sentence endings/beginnings (`because`, `since`, `as`, `due to`).
- Ensure no sentence exceeds 20 words; target 8‑14 words for rhythm.
- Reduce adverb density (<0.2 %); replace weak verbs with stronger ones.
- Keep passive voice <10 % of clauses.

### PASS 4 – Clarity & concreteness
- Explain every technical term or acronym with concrete detail, action, or analogy.
- Ensure each paragraph ends on a tangible image, action, or sensory detail.
- Add experiential writing (sight, sound, touch) to every paragraph.

### PASS 5 – Final verification & polish
- Reread for logical flow, transitions, and tone consistency.
- Run the compliance checklist:
  - ✅ Zero em‑dashes
  - ✅ All acronyms expanded
  - ✅ No bracketed notations
  - ✅ No sentence >20 words
  - ✅ No causal sentence endings/beginnings
  - ✅ Adverb density <0.2 %
  - ✅ Passive voice <10 %
  - ✅ All technical terms explained concretely
  - ✅ Paragraphs end with tangible detail
  - ✅ Experiential writing present
  - ✅ Paragraph segmentation 3‑7 sentences
  - ✅ Matches chapter objectives in `Manuscript_Outline.md`
  - ✅ Alternating Lens Requirement satisfied (Micro/Macro integration)
  - ✅ PACER Anchoring Rule satisfied (No speculative interiority)
  - ✅ Consistent with `profile.md`
- Optional read‑aloud test for rhythm.

## Git workflow (safe actions)
1. **Authenticate**
   ```bash
   gh auth status   # ensure logged in as rithythul
   git config --global user.email "rithythul@example.com"
   git config --global user.name "Rithy Thul"
   ```
2. **Clone / fetch**
   ```bash
   if [ ! -d publishing ]; then
       git clone https://github.com/rithythul/publishing publishing
   else
       git -C publishing fetch --all
   fi
   cd publishing
   git checkout main
   ```
3. **Edit the chapter file** (apply the five passes above).
4. **Stage & commit**
   ```bash
   git add <file>
   git commit -m "Gold‑standard edit of chapter XX"
   ```
5. **Push & verify** (operational verification guideline)
   ```bash
   git push origin main
   # Verify remote reflects local HEAD
   local_sha=$(git rev-parse HEAD)
   remote_sha=$(git ls-remote origin -h refs/heads/main | cut -f1)
   if [ "$local_sha" = "$remote_sha" ]; then
       echo "Push verified"
   else
       echo "Verification failed" && exit 1
   fi
   ```

## Pitfalls & work‑arounds
- Missing Git identity → set `user.email` / `user.name` before commit.
- Em‑dash left behind → search `git diff | grep "—"` and replace.
- Sentence length too long → use `wc -w` on the line, split at commas.
- Remote not updated → always run the SHA verification step.
- Accidental file content output → never `cat` the file; rely on push.

---
