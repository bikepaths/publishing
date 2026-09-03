#!/usr/bin/env python3
import sys
import os
import re
import nltk
from nltk.corpus import cmudict

# Ensure NLTK data path includes our updated location
nltk.data.path.append(os.path.expanduser('~/.nltk_data'))

try:
    cmu_dict = cmudict.dict()
except LookupError:
    nltk.download('cmudict', download_dir=os.path.expanduser('~/.nltk_data'))
    cmu_dict = cmudict.dict()

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt_tab', download_dir=os.path.expanduser('~/.nltk_data'))
    nltk.download('punkt', download_dir=os.path.expanduser('~/.nltk_data'))
    
def count_syllables(word):
    word = word.lower()
    if word in cmu_dict:
        # CMUdict returns a list of phonetic transcriptions. 
        # We take the first one and count the vowels (which carry stress marks).
        return len([p for p in cmu_dict[word][0] if p[-1].isdigit()])
    else:
        # Fallback heuristic for words not in CMUdict
        count = 0
        vowels = 'aeiouy'
        if word[0] in vowels:
            count += 1
        for index in range(1, len(word)):
            if word[index] in vowels and word[index - 1] not in vowels:
                count += 1
        if word.endswith('e'):
            count -= 1
        if count == 0:
            count += 1
        return count

def calculate_flesch_kincaid(text):
    sentences = nltk.sent_tokenize(text)
    words = nltk.word_tokenize(text)
    # Filter out punctuation
    words = [w for w in words if w.isalpha()]
    
    if not sentences or not words:
        return 0
        
    num_sentences = len(sentences)
    num_words = len(words)
    num_syllables = sum(count_syllables(w) for w in words)
    
    fk_grade = 0.39 * (num_words / num_sentences) + 11.8 * (num_syllables / num_words) - 15.59
    return fk_grade

def extract_frontmatter_target(text):
    match = re.search(r'^---\n(.*?)\n---', text, re.DOTALL)
    if not match:
        return None
    frontmatter = match.group(1)
    target_match = re.search(r'audience_target:\s*([a-zA-Z]+)', frontmatter)
    if target_match:
        return target_match.group(1).lower()
    return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 cmu_validation.py <markdown_file>")
        sys.exit(1)
        
    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        sys.exit(1)
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    target = extract_frontmatter_target(content)
    if not target:
        print(f"ERROR: {file_path} missing 'audience_target' in YAML frontmatter.")
        sys.exit(1)
        
    fk_grade = calculate_flesch_kincaid(content)
    print(f"Flesch-Kincaid Grade Level: {fk_grade:.2f}")
    
    if target == 'pedagogical':
        if 8.0 <= fk_grade <= 9.5:
            print("PASS: Pedagogical document meets Grade 8.0 - 9.5 constraint.")
            sys.exit(0)
        else:
            print(f"FAIL: Pedagogical document must be Grade 8.0 - 9.5. Score: {fk_grade:.2f}")
            sys.exit(1)
    elif target == 'systemic':
        if 10.0 <= fk_grade <= 12.0:
            print("PASS: Systemic document meets Grade 10.0 - 12.0 constraint.")
            sys.exit(0)
        else:
            print(f"FAIL: Systemic document must be Grade 10.0 - 12.0. Score: {fk_grade:.2f}")
            sys.exit(1)
    else:
        print(f"ERROR: Unknown audience_target '{target}'")
        sys.exit(1)

if __name__ == "__main__":
    main()
