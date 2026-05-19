import os
import re

DIR = '/home/user0/files/SSRN_Strategic_Intelligence_Stack/publishing/nyt-cyber-expose/kdp/manuscript/chapter_drafts/'

replacements = [
    (r'(?i)\bentirely \b', ''),
    (r'(?i)\bcompletely \b', ''),
    (r'(?i)\bactively \b', ''),
    (r'(?i)\bexplicitly \b', ''),
    (r'(?i)\bheavily \b', ''),
    (r'(?i)\bdirectly \b', ''),
    (r'(?i)\bspecifically \b', ''),
    (r'(?i)\bactually \b', ''),
    (r'(?i)\bmerely \b', ''),
    (r'(?i)\butilized\b', 'used'),
    (r'(?i)\butilizing\b', 'using'),
    (r'(?i)\butilize\b', 'use'),
    (r'(?i)\bframework\b', 'architecture'),
    (r'(?i)\bsynergy\b', 'coordination')
]

for filename in os.listdir(DIR):
    if filename.endswith('.md'):
        path = os.path.join(DIR, filename)
        with open(path, 'r') as f:
            content = f.read()
        
        new_content = content
        for pattern, replacement in replacements:
            new_content = re.sub(pattern, replacement, new_content)
            
        if new_content != content:
            with open(path, 'w') as f:
                f.write(new_content)
            print(f"Updated {filename}")
