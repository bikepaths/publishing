import os
import re

forbidden_patterns = [
    # adverbs and their adjective roots
    r"actuall?y", r"mere(?:ly)?", r"simpl(?:y|e|icity)?", r"fundamental(?:ly)?", r"specific(?:ally)?", r"however",
    r"complete(?:ly|s|ed|ing)?", r"absolute(?:ly)?", r"perfect(?:ly|s|ed|ing)?", r"entire(?:ly)?", r"explicit(?:ly)?", r"active(?:ly)?",
    r"smooth(?:ly|s|ed|ing)?", r"flawless(?:ly)?", r"safe(?:ly)?", r"secure(?:ly|s|ed|ing)?", r"rigorous(?:ly)?", r"violent(?:ly)?",
    r"heav(?:y|ily)?", r"essential(?:ly)?", r"direct(?:ly|s|ed|ing)?", r"certain(?:ly)?", r"of course", r"generally speaking",
    r"for the most part",
    # verbs and nouns with their inflections
    r"utiliz(?:e|es|ed|ing|ation|ations)?", r"provenance", r"nuance(?:d|s)?", r"mitigat(?:e|es|ed|ing|ion|ions)?",
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

forbidden_regex = re.compile(r'\b(' + '|'.join(forbidden_patterns) + r')\b', re.IGNORECASE)

conjunctions = ["because", "since"]
conjunctions_regex = re.compile(r'^\s*(' + '|'.join(map(re.escape, conjunctions)) + r')\b', re.IGNORECASE)

drafts_dir = "/home/user0/git/publishing/mdi/kdp/manuscript/chapter_drafts"

all_files = sorted([f for f in os.listdir(drafts_dir) if f.startswith("chapter_") and f.endswith(".md")])

print(f"Auditing {len(all_files)} files in {drafts_dir}...\n")

total_violations = 0

for filename in all_files:
    filepath = os.path.join(drafts_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    file_violations = []

    # Check for em-dashes
    if "—" in content:
        file_violations.append("Contains em-dash (—)")

    # Check for colons
    if ":" in content:
        # ignore colons in YAML-like header or URLs
        lines = content.splitlines()
        for idx, line in enumerate(lines, 1):
            if ":" in line:
                if not (line.startswith("Created At") or line.startswith("Completed At") or line.startswith("File Path") or "://" in line):
                    file_violations.append(f"Line {idx} contains colon (:): {line}")

    # Check for parentheses
    if "(" in content or ")" in content:
        # ignore if it's links like [link](file:///...)
        lines = content.splitlines()
        for idx, line in enumerate(lines, 1):
            # clean out markdown links
            clean_line = re.sub(r'\[[^\]]*\]\([^)]+\)', '', line)
            if "(" in clean_line or ")" in clean_line:
                file_violations.append(f"Line {idx} contains parenthesis: {line}")

    # Check for forbidden words
    for idx, line in enumerate(content.splitlines(), 1):
        matches = forbidden_regex.findall(line)
        if matches:
            file_violations.append(f"Line {idx} contains forbidden word(s) {set(matches)}: {line}")

    # Check sentence-starting conjunctions (because, since)
    sentences = re.split(r'(?<=[.!?])\s+', content)
    for s in sentences:
        s_clean = s.strip()
        if conjunctions_regex.match(s_clean):
            file_violations.append(f"Sentence starts with forbidden conjunction: {s_clean}")

    if file_violations:
        print(f"=== {filename} ===")
        for v in file_violations:
            print(f"  [VIOLATION] {v}")
        print()
        total_violations += len(file_violations)

print(f"Total violations found: {total_violations}")
