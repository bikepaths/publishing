# ePub Production Guide
*Material Dignity Press / SSRN Strategic Intelligence Stack*
*Toolchain: Pandoc 3.x + EPUBCheck 5.x + Python 3*

---

## Overview

This guide is the canonical production runbook for generating EPUB 3.3-compliant ebook files within the publishing platform. Follow every step in sequence. Do not skip the EPUBCheck validation step. A file that has not passed EPUBCheck is not ready for KDP submission.

---

## Directory Structure

Every book project must follow this layout before epub production begins:

```
publishing/
└── [series]/
    └── kdp/
        ├── handoff/
        │   ├── cover_concept.png        # Final cover image (min 2500px tall, sRGB)
        │   ├── back_cover_copy.md
        │   ├── metadata.yaml
        │   ├── kdp_strategy.md
        │   └── [title].epub             # Final validated output
        └── manuscript/
            ├── epub_source.md           # Assembled master source (generated)
            ├── epub_style.css           # Copied from publishing/_epub/epub_template.css
            ├── front_matter.md
            ├── copyright.md
            ├── citations.md
            └── chapter_drafts/
                ├── chapter_01_[slug].md
                ├── chapter_02_[slug].md
                └── ...
```

---

## Step 1: Copy the CSS Template

Before any build, copy the canonical template into the manuscript directory:

```bash
cp /home/user0/git/publishing/_epub/epub_template.css \
   /path/to/manuscript/epub_style.css
```

Do not modify the template file. If the book requires typographic adjustments, modify only the local copy in the manuscript directory and document the changes in the handoff notes.

---

## Step 2: Prepare Source Files

Every book requires the following source files in the manuscript directory before assembly:

| File | Required | Notes |
|---|---|---|
| `copyright.md` | Yes | Copyright year, publisher, rights statement |
| `front_matter.md` | Yes | Title page block at top (lines 1–6), author statement below |
| `chapter_drafts/chapter_NN_[slug].md` | Yes | One file per chapter, no internal headers |
| `citations.md` | Yes | Chicago 17th edition, fenced div `.citations` wrapper |
| Cover image | Yes | PNG or JPG, minimum 2500px on longest side, sRGB |

Citations must use the pandoc fenced div syntax to activate CSS hanging indent:

```markdown
::: {.citations}

Author, Last. "Title." *Journal* Volume, no. Issue (Year): Pages. https://doi.org/xxx.

:::
```

---

## Step 3: Assemble the Master Source File

Run the assembly script:

```bash
python3 /home/user0/git/publishing/_epub/epub_assembly.py \
  --manifest manifest.yaml \
  --output epub_source.md
```

Or assemble manually using the Python inline method documented in `epub_assembly.py`. The assembled `epub_source.md` must begin with a YAML metadata block:

```yaml
---
title: "Book Title"
author: "Author Name"
lang: "en-US"
---
```

Each chapter must be preceded by an H1 heading and an H2 location/subtitle line:

```markdown
# Chapter One: Chapter Title

*Location — Date*

[chapter prose begins here]
```

---

## Step 3.5: Optimize Cover Image

Do not compile raw PNG covers into the EPUB. Enforce JPEG compression to reduce file sizes:

```bash
python3 -c "from PIL import Image; img = Image.open('../handoff/cover_concept.png'); img.convert('RGB').save('../handoff/cover.jpg', 'JPEG', quality=90)"
```

## Step 4: Build the ePub

Run the following pandoc command from the manuscript directory:

```bash
pandoc epub_source.md \
  --from markdown+smart \
  --to epub3 \
  --output ../handoff/[title_slug].epub \
  --css epub_style.css \
  --epub-cover-image ../handoff/cover.jpg \
  --toc \
  --toc-depth=1 \
  --split-level=1 \
  --metadata title="Full Book Title" \
  --metadata subtitle="Full Subtitle" \
  --metadata author="Author Full Name" \
  --metadata lang="en-US" \
  --metadata publisher="Material Dignity Press" \
  --metadata rights="Copyright © YEAR Author Name. All rights reserved."
```

The `--from markdown+smart` flag enables typographic quotes and em-dashes from source text. The `--split-level=1` flag splits the epub into one XHTML file per H1 heading, which is required for proper chapter navigation on Kindle devices.

---

## Step 5: Validate with EPUBCheck

Run EPUBCheck against the output file:

```bash
python3 -c "
from epubcheck import EpubCheck
result = EpubCheck('../handoff/[title_slug].epub')
print('Valid:', result.valid)
print('Messages:', len(result.messages))
for m in result.messages:
    print(m.level, m.message)
"
```

**The file is not production-ready until EPUBCheck reports `Valid: True` and zero ERROR-level messages.** WARNING-level messages from pandoc metadata fields are acceptable. Any ERROR must be resolved before KDP submission.

If EPUBCheck is not installed:

```bash
pip3 install epubcheck --break-system-packages
```

---

## Step 6: Rebuild the Compiled Flat Manuscript

After epub validation, rebuild the flat manuscript files for print and reference:

```bash
# Full flat markdown
cat copyright.md front_matter.md chapter_drafts/*.md citations.md > full_manuscript.md

# Word document for KDP print submission
pandoc full_manuscript.md -o ../handoff/[title_slug].docx --from markdown
```

---

## Step 7: Git Sync

Commit all handoff files with a descriptive message:

```bash
git add -A && git commit -m "[Series] [Book]: EPUBCheck validated epub, complete handoff package" && git push origin main
```

---

## KDP Submission Checklist

Before uploading to KDP:

- [ ] EPUBCheck passes with zero errors
- [ ] Cover image embedded inside EPUB is optimized JPEG under 1MB; raw high-resolution cover remains in handoff for dashboard upload
- [ ] All citations are Chicago 17th edition with no placeholder authors
- [ ] Author name on cover matches KDP account author name exactly
- [ ] BISAC categories confirmed in `metadata.yaml`
- [ ] Back cover copy proofread and under 4,000 characters
- [ ] eBook pre-order window set to 30 days before desired launch date
- [ ] SSRN propagation post ready for simultaneous publish

---

## Troubleshooting

**EPUBCheck reports `CSS property not supported`**: These are warnings from Kindle's CSS subset, not errors. The epub is still valid. The properties trigger fallback rendering, not failure.

**Pandoc warning `Deprecated: --epub-chapter-level`**: Replace with `--split-level`. Both flags exist in Pandoc 3.x but only `--split-level` is current.

**Citations hanging indent not rendering**: Confirm the `citations.md` file uses the fenced div `:::  {.citations}` wrapper. Without the class, the CSS rule cannot reach the content.

**Cover image rejected by KDP**: Confirm the image is sRGB (not CMYK), at least 2500px on the longest side, and saved as JPG or PNG. KDP also rejects images with text that does not match the submitted title exactly.
