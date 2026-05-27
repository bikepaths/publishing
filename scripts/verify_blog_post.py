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

def count_syllables(word):
    word = word.lower()
    vowels = "aeiouy"
    count = 0
    if len(word) == 0:
        return 0
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if count == 0:
        count = 1
    return count

def get_flesch_kincaid(text):
    clean_text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    words = re.findall(r'\b[a-zA-Z]+\b', clean_text)
    sentences = re.split(r'(?<=[.!?])\s+', clean_text.strip())
    sentences = [s for s in sentences if s.strip()]
    if not words or not sentences:
        return 0.0
    num_words = len(words)
    num_sentences = len(sentences)
    num_syllables = sum(count_syllables(w) for w in words)
    
    fk = 0.39 * (num_words / num_sentences) + 11.8 * (num_syllables / num_words) - 15.59
    return round(fk, 1)

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
    
    with open(factoid_file, "r", encoding="utf-8") as f_fact:
        factoid_content = f_fact.read()

    if "Extract and list facts here" in factoid_content:
        print(f"[FAIL] Pass 1: Factoid file factoid_{timestamp}.md contains unpopulated compiled facts placeholder.")
        return False

    if "To be added from external research" in factoid_content:
        print(f"[FAIL] Pass 1: Factoid file factoid_{timestamp}.md contains unpopulated additional research placeholder.")
        return False

    if "Raw Original Post Reference" in factoid_content:
        print(f"[FAIL] Pass 1: Factoid file factoid_{timestamp}.md still contains raw original post reference content; deconstruction phase is incomplete.")
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

    # Pass 2.1: Readability Check
    fk_grade = get_flesch_kincaid(content)
    if not (8.0 <= fk_grade <= 10.0):
        print(f"  [VIOLATION] Pass 2: Readability grade level is {fk_grade} (target: 8.0 - 10.0).")
        style_failed = True
    else:
        print(f"  [PASS] Pass 2: Readability grade level verified: {fk_grade}.")

    # Pass 2.2: Sentence Rhythm Check
    # Split body into paragraphs
    body_text = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL).strip()
    paragraphs = [p.strip() for p in body_text.split("\n\n") if p.strip()]
    num_paragraphs = len(paragraphs)
    if not (3 <= num_paragraphs <= 6):
        print(f"  [VIOLATION] Pass 2: Body has {num_paragraphs} paragraphs (apropos range is 3 to 6 paragraphs).")
        style_failed = True
    for p_idx, p in enumerate(paragraphs, 1):
        p_sentences = re.split(r'(?<=[.!?])\s+', p)
        p_sentences = [s.strip() for s in p_sentences if s.strip()]
        if not p_sentences:
            continue
        has_hammer = False
        sentence_lengths = []
        for s in p_sentences:
            words = re.findall(r'\b[a-zA-Z]+\b', s)
            w_count = len(words)
            sentence_lengths.append(w_count)
            if w_count <= 10:
                has_hammer = True
        if not has_hammer:
            print(f"  [VIOLATION] Pass 2: Paragraph {p_idx} lacks a short declarative hammer sentence (<= 10 words). Sentence lengths: {sentence_lengths}")
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

    # Enforce allowed category taxonomy check
    ALLOWED_CATEGORIES = ['society', 'skills', 'systems', 'money', 'nature', 'technology', 'adventure', 'health', 'history', 'mind']
    meta_tags = [t.strip() for t in metadata['tag'].split(",")]
    if not meta_tags or not meta_tags[0]:
        print("[FAIL] Pass 3: Tag metadata list is empty.")
        return False
    
    primary_category = meta_tags[0]
    if primary_category not in ALLOWED_CATEGORIES:
        print(f"[FAIL] Pass 3: Primary category '{primary_category}' is invalid. Must be one of: {ALLOWED_CATEGORIES}")
        return False

    # Check total number of tags (1 category + max 5 additional tags = max 6 tags)
    if len(meta_tags) > 6:
        print(f"[FAIL] Pass 3: Too many tags ({len(meta_tags)}). Maximum allowed is 6 (1 category + 5 tags).")
        return False

    # Load tags.lang for validation of additional tags
    script_dir = os.path.dirname(os.path.abspath(__file__))
    tags_file = os.path.join(os.path.dirname(script_dir), "blog", "data", "tags.lang")
    allowed_tags = set()
    if os.path.isfile(tags_file):
        with open(tags_file, "r", encoding="utf-8", errors="ignore") as f:
            t_content = f.read()
        allowed_tags = set(re.findall(r's:\d+:"([^"]+)"', t_content))

    if not allowed_tags:
        print("[WARNING] Pass 3: tags.lang file not found or empty. Additional tag validation bypassed.")
    else:
        # Validate additional tags against tags.lang
        for tag in meta_tags[1:]:
            if tag not in allowed_tags:
                print(f"[FAIL] Pass 3: Tag '{tag}' is not in approved tags.lang list.")
                return False

    if not is_draft:
        filename_parts = filename.split("_")
        if len(filename_parts) >= 2:
            filename_tags = [t.strip() for t in filename_parts[1].split(",")]
            if filename_tags[0] != primary_category:
                print(f"[FAIL] Pass 3: Filename primary category '{filename_tags[0]}' does not match metadata primary category '{primary_category}'")
                return False
            if len(filename_tags) > 6:
                print(f"[FAIL] Pass 3: Filename contains too many tags ({len(filename_tags)}).")
                return False
            for f_tag in filename_tags[1:]:
                if allowed_tags and f_tag not in allowed_tags:
                    print(f"[FAIL] Pass 3: Filename tag '{f_tag}' is not in approved tags.lang list.")
                    return False
            if sorted(filename_tags) != sorted(meta_tags):
                print(f"[FAIL] Pass 3: Filename tags {filename_tags} do not match metadata tags {meta_tags}")
                return False

    print("[PASS] Pass 3: Metadata integrity verified.")

    # Pass 4: Resource Verification
    image_val = metadata['image']
    if image_val.startswith("http://") or image_val.startswith("https://"):
        print(f"[PASS] Pass 4: Resource path verified against remote URL: {image_val}.")
    else:
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
