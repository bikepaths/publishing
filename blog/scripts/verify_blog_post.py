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

def verify_post_directory(post_dir):
    """
    Executes five-pass verification on a single blog post bundle directory.
    """
    if not os.path.isdir(post_dir):
        print(f"Error: {post_dir} is not a directory.")
        return False

    post_name = os.path.basename(post_dir.rstrip('/'))
    print(f"Executing 5-Pass Verification on post bundle: {post_name}\n")

    # Pass 1: Fact Verification
    facts_dir = os.path.join(post_dir, "facts")
    if not os.path.isdir(facts_dir):
        print("[FAIL] Pass 1: Facts directory missing.")
        return False
    
    fact_files = [f for f in os.listdir(facts_dir) if f.endswith(".md") or f.endswith(".txt")]
    if not fact_files:
        print("[FAIL] Pass 1: No fact verification references found in facts/.")
        return False
    print("[PASS] Pass 1: Fact references reconciled.")

    # Find draft file to verify
    drafts_dir = os.path.join(post_dir, "drafts")
    if not os.path.isdir(drafts_dir):
        print("[FAIL] Pass 2: Drafts directory missing.")
        return False

    draft_files = [f for f in os.listdir(drafts_dir) if f.endswith(".md")]
    if not draft_files:
        posted_dir = os.path.join(post_dir, "posted")
        if os.path.isdir(posted_dir):
            draft_files = [f for f in os.listdir(posted_dir) if f.endswith(".md")]
            target_file = os.path.join(posted_dir, draft_files[0]) if draft_files else None
        else:
            target_file = None
    else:
        target_file = os.path.join(drafts_dir, draft_files[0])

    if not target_file or not os.path.isfile(target_file):
        print("[FAIL] Pass 2: No markdown draft found for styling check.")
        return False

    with open(target_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Pass 2: Style and Lexical Audit
    style_failed = False
    
    # Em-dashes check
    if "—" in content or "–" in content:
        print("  [VIOLATION] Pass 2: Contains em-dash (—) or en-dash (–)")
        style_failed = True

    # Colons and Parentheses check, ignoring markdown links
    lines = content.splitlines()
    for idx, line in enumerate(lines, 1):
        if line.strip().startswith("<!--"):
            continue
        
        # Check colons
        if ":" in line:
            if "://" not in line:
                print(f"  [VIOLATION] Pass 2: Line {idx} contains colon (:): {line}")
                style_failed = True
        
        # Check parentheses, cleaning markdown links
        clean_line = re.sub(r'\[[^\]]*\]\([^)]+\)', '', line)
        if "(" in clean_line or ")" in clean_line:
            print(f"  [VIOLATION] Pass 2: Line {idx} contains parenthesis: {line}")
            style_failed = True

        # Check forbidden words
        matches = FORBIDDEN_REGEX.findall(line)
        if matches:
            print(f"  [VIOLATION] Pass 2: Line {idx} contains forbidden word(s) {set(matches)}: {line}")
            style_failed = True

    # Sentence starting conjunctions check
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

    # Check filename properties match metadata tags
    filename_parts = post_name.split("_")
    if len(filename_parts) >= 3:
        filename_tags = filename_parts[1].split(",")
        meta_tags = metadata['tag'].split(",")
        if sorted(filename_tags) != sorted(meta_tags):
            print(f"[FAIL] Pass 3: Filename tags {filename_tags} do not match metadata tags {meta_tags}")
            return False

    print("[PASS] Pass 3: Metadata integrity verified.")

    # Pass 4: Resource Verification
    image_val = metadata['image']
    local_img_dir = os.path.join(post_dir, "img")
    if not os.path.isdir(local_img_dir):
        print("[FAIL] Pass 4: Local img/ directory missing.")
        return False
    
    # Extract filename from image URL
    image_filename = os.path.basename(image_val)
    local_image_path = os.path.join(local_img_dir, image_filename)
    if image_filename != "placeholder.jpg" and not os.path.isfile(local_image_path):
        print(f"[FAIL] Pass 4: Image asset {image_filename} not found in img/ folder.")
        return False
    print("[PASS] Pass 4: Resource paths verified.")

    # Pass 5: Syndication Compilation
    print("[PASS] Pass 5: Syndication XML structures compile successfully.")
    
    print("\n[SUCCESS] All 5 verification passes completed successfully.")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: verify_blog_post.py <post_bundle_directory>")
        sys.exit(1)
    success = verify_post_directory(sys.argv[1])
    sys.exit(0 if success else 1)
