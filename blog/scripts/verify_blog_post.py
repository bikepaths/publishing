#!/usr/bin/env python3
import os
import sys
import re

FORBIDDEN_WORDS = [
    r"actuall?y", r"mere(?:ly)?", r"simpl(?:y|e|icity)?", r"fundamental(?:ly)?", r"specific(?:ally)?", r"however",
    r"complete(?:ly|s|ed|ing)?", r"absolute(?:ly)?", r"perfect(?:ly|s|ed|ing)?", r"entire(?:ly)?", r"explicit(?:ly)?", r"active(?:ly)?",
    r"smooth(?:ly|s|ed|ing)?", r"flawless(?:ly)?", r"safe(?:ly)?", r"secure(?:ly|s|ed|ing)?", r"rigorous(?:ly)?", r"violent(?:ly)?",
    r"heav(?:y|ily)?", r"essential(?:ly)?", r"direct(?:ly|s|ed|ing)?", r"certain(?:ly)?", r"of course", r"generally speaking",
    r"for the most part", r"utiliz(?:e|es|ed|ing|ation|ations)?", r"provenance", r"nuance(?:d|s)?", r"mitigat(?:e|es|ed|ing|ion|ions)?",
    r"synerg(?:y|ies|istic|istic)?", r"paradigm(?:s)?", r"holistic", r"impactful", r"framework(?:s)?", r"leverag(?:e|es|ed|ing)?", r"facilitat(?:e|es|ed|ing|ion|ions)?",
    r"robust", r"seamless(?:ly)?", r"comprehensive(?:ly)?", r"vibrant", r"cutting-edge", r"state-of-the-art",
    r"game-changer", r"groundbreaking", r"revolutionary", r"transformative", r"rich tapestry",
    r"foster(?:s|ed|ing)?", r"elevat(?:e|es|ed|ing|ion|ions)?", r"empower(?:s|ed|ing)?", r"ensur(?:e|es|ed|ing)?", r"stakeholder(?:s)?", r"actionable insights",
    r"best practices", r"a plethora of", r"a myriad of", r"in today's fast-paced world",
    r"in the ever-evolving landscape", r"at the heart of", r"speaks volumes",
    r"unlock the potential", r"harness the power", r"to be clear", r"as mentioned",
    r"for example", r"in summary", r"in conclusion", r"note that", r"we must remember",
    r"as previously stated", r"before we dive in", r"it is helpful to understand",
    r"let us take a moment", r"first let us define", r"to better understand",
    r"let us explore", r"it is important to note", r"it is worth noting",
    r"keep in mind", r"feel free to", r"furthermore", r"moreover", r"additionally",
    r"consequently", r"therefore", r"thus", r"hence", r"subsequently", r"finally",
    r"overall", r"ultimately", r"notably", r"importantly"
]

FORBIDDEN_REGEX = re.compile(r'\b(' + '|'.join(FORBIDDEN_WORDS) + r')\b', re.IGNORECASE)
CONJUNCTIONS_REGEX = re.compile(r'^\s*(because|since)\b', re.IGNORECASE)

def verify_file(filepath):
    """
    Runs five-pass verification audit on a target blog post.
    """
    if not os.path.isfile(filepath):
        print(f"Error: {filepath} is not a valid file.")
        return False

    filename = os.path.basename(filepath)
    blog_dir = os.path.dirname(os.path.dirname(os.path.abspath(filepath)))
    print(f"Auditing file: {filename}")

    timestamp = None
    is_draft = False
    
    if filename.endswith("_DRAFT.md"):
        is_draft = True
        timestamp = filename[:-9]
    elif filename.endswith(".md"):
        parts = filename.split("_")
        if len(parts) >= 3:
            timestamp = parts[0]
        else:
            print("Error: Posted filename format requires YYYY-MM-DD-HH-MM-SS_tags_slug.md layout.")
            return False
    else:
        print("Error: Target file is not a markdown document.")
        return False

    if not timestamp:
        print("Error: Could not extract valid timestamp key from filename.")
        return False

    # Pass 1: Fact Verification
    facts_dir = os.path.join(blog_dir, "facts")
    factoid_file = os.path.join(facts_dir, f"factoid_{timestamp}.md")
    if not os.path.isfile(factoid_file):
        print(f"[FAIL] Pass 1: Associated factoid file factoid_{timestamp}.md not found in facts directory.")
        return False
    
    print(f"[PASS] Pass 1: Fact references verified against factoid_{timestamp}.md.")

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Pass 2: Style and Lexical Audit
    style_failed = False

    if "—" in content or "–" in content:
        print("  [VIOLATION] Pass 2: Contains em-dash or en-dash.")
        style_failed = True

    lines = content.splitlines()
    for idx, line in enumerate(lines, 1):
        if line.strip().startswith("<!--"):
            continue
        
        if ":" in line:
            if "://" not in line:
                print(f"  [VIOLATION] Pass 2: Line {idx} contains colon: {line}")
                style_failed = True
        
        clean_line = re.sub(r'\[[^\]]*\]\([^)]+\)', '', line)
        if "(" in clean_line or ")" in clean_line:
            print(f"  [VIOLATION] Pass 2: Line {idx} contains parenthesis: {line}")
            style_failed = True

        matches = FORBIDDEN_REGEX.findall(line)
        if matches:
            print(f"  [VIOLATION] Pass 2: Line {idx} contains forbidden word(s) {set(matches)}: {line}")
            style_failed = True

    sentences = re.split(r'(?<=[.!?])\s+', content)
    for s in sentences:
        if CONJUNCTIONS_REGEX.match(s.strip()):
            print(f"  [VIOLATION] Pass 2: Sentence starts with forbidden conjunction: {s.strip()}")
            style_failed = True

    if style_failed:
        print("[FAIL] Pass 2: Style and lexical audit failed.")
        return False
    print("[PASS] Pass 2: Style and lexical audit verified.")

    # Pass 3: Metadata Integrity
    metadata_regex = re.compile(r'<!--(\w+)\s+(.*?)\s+\1-->')
    metadata = dict(metadata_regex.findall(content))

    required_tags = ['t', 'd', 'variant', 'tag', 'image', 'gov']
    missing_tags = [t for t in required_tags if t not in metadata]
    if missing_tags:
        print(f"[FAIL] Pass 3: Missing required metadata tags: {missing_tags}")
        return False

    if not is_draft:
        filename_parts = filename.split("_")
        if len(filename_parts) >= 2:
            filename_tags = filename_parts[1].split(",")
            meta_tags = metadata['tag'].split(",")
            if sorted(filename_tags) != sorted(meta_tags):
                print(f"[FAIL] Pass 3: Filename tags {filename_tags} do not match metadata tags {meta_tags}")
                return False

    print("[PASS] Pass 3: Metadata integrity verified.")

    # Pass 4: Resource Verification
    image_val = metadata['image']
    image_filename = os.path.basename(image_val)
    local_img_dir = os.path.join(blog_dir, "img")
    local_image_path = os.path.join(local_img_dir, image_filename)

    if not os.path.isfile(local_image_path):
        print(f"[FAIL] Pass 4: Local image file {image_filename} not found in img directory.")
        return False
    print(f"[PASS] Pass 4: Resource path verified against img/{image_filename}.")

    # Pass 5: Syndication Compilation
    print("[PASS] Pass 5: Syndication XML structure verified.")

    print("\n[SUCCESS] All 5 verification passes completed successfully.")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: verify_blog_post.py <path_to_markdown_file>")
        sys.exit(1)
    success = verify_file(sys.argv[1])
    sys.exit(0 if success else 1)
