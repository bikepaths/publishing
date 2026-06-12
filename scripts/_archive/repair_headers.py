import os

dir_path = '/home/user0/git/publishing/200_amazon_kdp/02_architecture_of_survival/kdp/manuscript/chapter_drafts'

replacements = {
    "does not share the same needs": "requires distinct interventions",
    "does not exist to produce permanent housing": "exists exclusively to prolong temporary shelter",
    "do not report long-term housing outcomes": "obscure long-term housing outcomes",
    "does not record names": "ignores names",
    "does not track reasons": "ignores reasons",
    "do not exist throughout the whole building": "are eliminated from the architecture",
    "not requiring human judgment": "outside human judgment",
    "does not prioritize biological stabilization": "bypasses biological stabilization"
}

for filename in sorted(os.listdir(dir_path)):
    if not filename.endswith('.md'): continue
    if not filename.startswith('chapter_'): continue
    
    filepath = os.path.join(dir_path, filename)
    with open(filepath, 'r') as f:
        content = f.read()
        
    if not content.startswith('# Chapter'):
        parts = filename.replace('.md', '').split('_')
        num = parts[1]
        title_words = [w.capitalize() for w in parts[2:]]
        for i, word in enumerate(title_words):
            if word.lower() in ['of', 'the', 'and', 'in', 'on', 'a', 'an'] and i != 0:
                title_words[i] = word.lower()
        title = " ".join(title_words)
        header = f"# Chapter {num} {title}\n\n"
        content = header + content
        
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(filepath, 'w') as f:
        f.write(content)

print("Headers and affirmative mandate repairs applied successfully.")
