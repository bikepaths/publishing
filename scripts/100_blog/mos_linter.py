#!/usr/bin/env python3
import sys
import re
import os

BANNED_WORDS = [
    "however", "utilize", "mitigate", "robust", "seamless", "comprehensive",
    "furthermore", "moreover", "additionally", "therefore", "thus", "hence",
    "absolutely", "completely", "structurally", "operational", "precisely",
    "notably", "generates", "exact", "exactly", "strict", "strictly", "strickly",
    "leverage", "fosters", "greatly", "solely", "nuanced", "holistic", "heavy",
    "heavily", "essential", "fundamentally", "specifically", "perfectly",
    "assets", "symbiotic", "dynamic", "capacity", "velocity", "mechanisms", "etc."
]

BANNED_PHRASES = [
    "in conclusion", "in summary", "it is important to note that",
    "we must", "you should", "as mentioned above", "as stated previously"
]

def lint_file(filepath):
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)

    with open(filepath, 'r', encoding='utf-8') as f:
        original_lines = f.readlines()

    in_comment = False
    in_code_block = False
    violations = []

    for i, line in enumerate(original_lines):
        line_num = i + 1
        
        # Simple state machine for comments and code blocks
        if '<!--' in line and '-->' in line:
            line = re.sub(r'<!--.*?-->', '', line)
        elif '<!--' in line:
            in_comment = True
            continue
        elif '-->' in line and in_comment:
            in_comment = False
            continue
            
        if in_comment:
            continue
            
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            continue
            
        if in_code_block:
            continue

        lower_line = line.lower()

        # Check banned words
        for word in BANNED_WORDS:
            # use regex to match whole word boundaries
            if re.search(rf'\b{re.escape(word)}\b', lower_line):
                violations.append((line_num, "Banned Word", f"Found banned word '{word}'"))

        # Check banned phrases
        for phrase in BANNED_PHRASES:
            if phrase in lower_line:
                violations.append((line_num, "Banned Phrase", f"Found banned phrase '{phrase}'"))

        # Check banned punctuation
        if '—' in line:
            violations.append((line_num, "Banned Punctuation", "Found Em-dash (—)"))
        if '–' in line:
            violations.append((line_num, "Banned Punctuation", "Found En-dash (–)"))
        if ';' in line:
            violations.append((line_num, "Banned Punctuation", "Found Semicolon (;)"))
        
        # Check parentheses, ignoring markdown links [text](url)
        clean_line = re.sub(r'\[.*?\]\(.*?\)', '', line)
        if '(' in clean_line or ')' in clean_line:
            violations.append((line_num, "Banned Punctuation", "Found Parentheses ()"))
        
        # Check colons (not part of http:// or https://)
        no_url_line = re.sub(r'https?://', '', clean_line)
        if ':' in no_url_line:
            violations.append((line_num, "Banned Punctuation", "Found Colon (:) acting as hard stop"))

        # Synthetic contrast checks
        if re.search(r'did more than.*?(;|it)', lower_line):
            violations.append((line_num, "Synthetic Contrast", "Found potential synthetic contrast pivot ('did more than... it')"))
        if re.search(r'\bnot\b.*?, \bbut\b', lower_line):
            violations.append((line_num, "Synthetic Contrast", "Found potential synthetic contrast pivot ('not X, but Y')"))

    if violations:
        print(f"--- MoS Linter Results for {filepath} ---")
        for v in violations:
            print(f"Line {v[0]} | {v[1]}: {v[2]}")
        print(f"\nTotal Violations: {len(violations)}")
        sys.exit(1)
    else:
        print(f"--- MoS Linter Results for {filepath} ---")
        print("PASS: No MoS violations found.")
        sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 mos_linter.py <file.md>")
        sys.exit(1)
    lint_file(sys.argv[1])
