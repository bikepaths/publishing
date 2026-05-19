import os

DIR = '/home/user0/files/SSRN_Strategic_Intelligence_Stack/publishing/nyt-cyber-expose/kdp/manuscript/'
OUT = os.path.join(DIR, 'full_manuscript.md')

front_matter_path = os.path.join(DIR, 'front_matter.md')
drafts_dir = os.path.join(DIR, 'chapter_drafts')

chapters = sorted([f for f in os.listdir(drafts_dir) if f.startswith('chapter_') and f.endswith('.md')])

with open(OUT, 'w') as outfile:
    # 1. Front Matter (no ToC file needed, Pandoc handles it)
    if os.path.exists(front_matter_path):
        with open(front_matter_path, 'r') as infile:
            outfile.write(infile.read() + '\n\n')

    # 2. Chapters with hard page breaks
    for chapter in chapters:
        with open(os.path.join(drafts_dir, chapter), 'r') as infile:
            outfile.write('\\newpage\n\n' + infile.read() + '\n\n')
            
print(f"Compiled front matter and {len(chapters)} chapters into full_manuscript.md with hard page breaks.")
