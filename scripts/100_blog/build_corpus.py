import os
import re

CORPUS_FILE = "/home/user0/git/publishing/100_blog/02_draft/urban_survival_series/full_corpus.md"
SOURCE_DIR = "/home/user0/git/publishing/100_blog/02_draft/urban_survival_series/"

# Files corresponding to Parts 2 through 11
FILES = [
    "2026-07-02_the_spiral_that_nobody_stops.md",
    "2026-07-03_why_the_usual_answers_fail.md",
    "2026-07-04_not_one_crisis_five.md",
    "2026-07-05_what_the_body_needs_before_the_key.md",
    "2026-07-06_what_a_real_offer_looks_like.md",
    "2026-07-07_when_persuasion_cannot_reach.md",
    "2026-07-08_the_people_nobody_counted.md",
    "2026-07-09_the_building_that_rebuilds_people.md",
    "2026-07-10_what_it_costs_to_do_nothing.md",
    "2026-07-11_how_we_know_if_it_works.md"
]

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract <!--t ... t--> and <!--d ... d-->
    t_match = re.search(r'<!--t.*?t-->', content, re.DOTALL)
    d_match = re.search(r'<!--d.*?d-->', content, re.DOTALL)
    
    t_xml = t_match.group(0) if t_match else ""
    d_xml = d_match.group(0) if d_match else ""

    # Remove all XML metadata blocks
    body = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    
    # Remove standard navigational footers without destroying the document
    lines = body.split('\n')
    cleaned_lines = []
    for line in lines:
        if "***Series: [" in line:
            continue
        cleaned_lines.append(line)
        
    body = '\n'.join(cleaned_lines)
    
    # Trim excess whitespace
    body = body.strip()

    # Construct the finalized text block per the Sysop's pattern
    block = f"{t_xml}\n{d_xml}\n\n{body}\n\n---\n\n"
    return block

def main():
    # Keep lines 1-45 from full_corpus.md representing Part 1
    with open(CORPUS_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    part_1 = "".join(lines[:45])
    
    with open(CORPUS_FILE, 'w', encoding='utf-8') as out:
        out.write(part_1 + "\n")
        for filename in FILES:
            filepath = os.path.join(SOURCE_DIR, filename)
            block = process_file(filepath)
            out.write(block)
    print(f"Successfully reconstructed full_corpus.md appending {len(FILES)} complete document bodies.")

if __name__ == "__main__":
    main()
