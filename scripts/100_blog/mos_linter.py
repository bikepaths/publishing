#!/usr/bin/env python3
"""
MoS Linter — Dynamically parses the active Manual of Style document
to extract banned words, phrases, and punctuation rules, then lints
a target markdown file against those constraints.

Usage:
  python3 mos_linter.py <target_file.md> [mos_file.md]

If no MoS file is specified, defaults to:
  /home/user0/git/publishing/_styles/MoS_Analytical_OVP.md
"""
import sys
import re
import os

DEFAULT_MOS = "/home/user0/git/publishing/_styles/MoS_Analytical_OVP.md"

def parse_mos(mos_path):
    """Dynamically extract banned words and phrases from the MoS document."""
    if not os.path.exists(mos_path):
        print(f"Error: MoS file '{mos_path}' not found.")
        sys.exit(1)

    with open(mos_path, 'r', encoding='utf-8') as f:
        content = f.read()

    banned_words = []
    banned_phrases = []

    # Extract banned words: look for a line containing "Banned Words" followed by
    # a comma-separated list of plain words (possibly on the same line after a colon/label)
    # Format: "**The Global 42 Banned Words:** word1, word2, word3, etc."
    words_match = re.search(r'[Bb]anned [Ww]ords[:\*]*\s*(.+)', content)
    if words_match:
        raw = words_match.group(1).strip().rstrip('.')
        # Also handle the italicized format: *word1, word2, word3.*
        raw = raw.strip('*').rstrip('.')
        for w in raw.split(','):
            cleaned = w.strip().lower()
            if cleaned and cleaned != 'etc':
                banned_words.append(cleaned)

    # Extract banned phrases: look for quoted strings in Filler Phrases lines
    # Format: '**Filler Phrases:** "In conclusion", "In summary"'
    phrases_match = re.search(r'[Ff]iller [Pp]hrases[:\*]*\s*(.+)', content)
    if phrases_match:
        raw = phrases_match.group(1)
        phrase_items = re.findall(r'"([^"]+)"', raw)
        for p in phrase_items:
            banned_phrases.append(p.strip().lower())

    exemptions = set()
    exempt_match = re.search(r'\*\*Linter Exemptions:\*\*\s*(.+)', content)
    if exempt_match:
        raw = exempt_match.group(1)
        for e in raw.split(','):
            exemptions.add(e.strip().lower())

    return banned_words, banned_phrases, exemptions


def lint_file(filepath, mos_path):
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)

    banned_words, banned_phrases, exemptions = parse_mos(mos_path)

    print(f"--- MoS Linter ---")
    print(f"Target: {filepath}")
    print(f"MoS Source: {mos_path}")
    print(f"Loaded {len(banned_words)} banned words, {len(banned_phrases)} banned phrases.")
    print(f"Loaded {len(exemptions)} exemptions.")
    print()

    with open(filepath, 'r', encoding='utf-8') as f:
        original_lines = f.readlines()

    in_comment = False
    in_code_block = False
    in_html_code_block = False
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
            if 'ban_markdown_code_blocks' in exemptions:
                violations.append((line_num, "Formatting Constraint", "Markdown code blocks (```) are banned by this MoS. Use <pre><code> instead."))
            in_code_block = not in_code_block
            continue

        if in_code_block:
            continue

        if '<pre><code>' in line:
            in_html_code_block = True
            
        if '</code></pre>' in line:
            in_html_code_block = False
            continue
            
        if in_html_code_block:
            continue

        lower_line = line.lower()

        # Check banned words
        for word in banned_words:
            if re.search(rf'\b{re.escape(word)}\b', lower_line):
                violations.append((line_num, "Banned Word", f"Found banned word '{word}'"))

        # Check banned phrases
        for phrase in banned_phrases:
            if phrase in lower_line:
                violations.append((line_num, "Banned Phrase", f"Found banned phrase '{phrase}'"))

        # Check banned punctuation
        if '\u2014' in line and 'allow_em_dash' not in exemptions:
            violations.append((line_num, "Banned Punctuation", "Found Em-dash (\u2014)"))
        if '\u2013' in line and 'allow_en_dash' not in exemptions:
            violations.append((line_num, "Banned Punctuation", "Found En-dash (\u2013)"))
        if ';' in line and 'allow_semicolons' not in exemptions:
            violations.append((line_num, "Banned Punctuation", "Found Semicolon (;)"))

        # Check parentheses, ignoring markdown links [text](url)
        clean_line = re.sub(r'\[.*?\]\(.*?\)', '', line)
        is_structural_line = clean_line.strip().startswith('#') or clean_line.strip().startswith('**')
        
        if not is_structural_line and ('(' in clean_line or ')' in clean_line) and 'allow_parentheses' not in exemptions:
            violations.append((line_num, "Banned Punctuation", "Found Parentheses ()"))

        # Check colons (not part of http:// or https://)
        no_url_line = re.sub(r'https?://', '', clean_line)
        if ':' in no_url_line and not is_structural_line and 'allow_colons' not in exemptions:
            violations.append((line_num, "Banned Punctuation", "Found Colon (:) acting as hard stop"))

        # Synthetic contrast checks
        if re.search(r'did more than.*?(;|it)', lower_line):
            violations.append((line_num, "Synthetic Contrast", "Found potential synthetic contrast pivot ('did more than... it')"))
        if re.search(r'\bnot\b.*?, \bbut\b', lower_line):
            violations.append((line_num, "Synthetic Contrast", "Found potential synthetic contrast pivot ('not X, but Y')"))

    if violations:
        print(f"--- Results ---")
        for v in violations:
            print(f"Line {v[0]} | {v[1]}: {v[2]}")
        print(f"\nTotal Violations: {len(violations)}")
        sys.exit(1)
    else:
        print(f"--- Results ---")
        print("PASS: No MoS violations found.")
        sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 mos_linter.py <file.md> [mos_file.md]")
        sys.exit(1)
    target = sys.argv[1]
    mos = sys.argv[2] if len(sys.argv) >= 3 else DEFAULT_MOS
    lint_file(target, mos)
