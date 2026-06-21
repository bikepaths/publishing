

# Agent Handoff: Manuscript Integration

**Target Agent:** Integration Agent
**Status:** Pre-compositional research complete. Deliverables 01-10 finalized.

## 1. Directive
Your objective is to integrate research deliverables `01` through `10` from `research/` into `full_manuscript.md`.

## 2. Integration Parameters (Phase 6 Audit Constraints)
*   **Dunbar Resident Count:** Standardize all references to **150**. Do not use 154 unless explicitly defending specific active sympathy network studies.
*   **Falsifiability Clause:** Insert `10_Binary_Verification_Metrics.md` explicitly into Chapter 15 or Appendix.
*   **SSRN Harmonization:** Align terms (Phase Zero, Material Dignity Infrastructure) with latest Charles J. DiBella SSRN papers (6211658).

## 3. Internal Python Utility (Manuscript Compiler)
Execute this script to compile research deliverables into a single staging file.

```python
#!/usr/bin/env python3
import os
import glob
import re

RESEARCH_DIR = "research/"
MANUSCRIPT_FILE = "full_manuscript.md"
COMPILED_OUTPUT = "compiled_integration_staging.md"

def compile_research():
    """Aggregates all research deliverables for streamlined integration."""
    research_files = sorted(glob.glob(os.path.join(RESEARCH_DIR, "*.md")))
    with open(COMPILED_OUTPUT, "w") as out_file:
        out_file.write("# STAGING: COMPILED RESEARCH DELIVERABLES\n\n")
        for filepath in research_files:
            with open(filepath, "r") as f:
                out_file.write(f"## SOURCE: {os.path.basename(filepath)}\n\n")
                out_file.write(f.read())
                out_file.write("\n\n---\n\n")
    print(f"Aggregated {len(research_files)} research files into {COMPILED_OUTPUT}.")

if __name__ == "__main__":
    compile_research()
```

## 4. Execution Sequence
1. Run internal python script.
2. Review `compiled_integration_staging.md`.
3. Manually inject staged research into `full_manuscript.md` using architectural logic.
