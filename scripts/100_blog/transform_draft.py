import os
import glob
import re

replacements = {
    r'\bframeworks\b': 'systems',
    r'\bFrameworks\b': 'Systems',
    r'\bframework\b': 'system',
    r'\bFramework\b': 'System',
    r'\bAdditionally,\s*': '',
    r'\bAdditionally\b': 'Also',
    r'\bspecific\b': 'defined',
    r'\brigorous\b': 'thorough',
    r'\bensures\b': 'guarantees',
    r'\boperational\b': 'active',
    r'\bFinally,\s*': '',
    r'\bFinally\b': 'Lastly',
    r'\bComplete\b': 'Concluded',
    r'\bsimple\b': 'basic',
    r'\bexplicitly\b': 'openly',
    r'\bmere\b': 'just',
    r'\bmerely\b': 'just'
}

files = glob.glob("/home/user0/git/publishing/100_blog/02_draft/urban_survival_series/*.md")
for filepath in files:
    if "full_corpus" in filepath or "index" in filepath or "07-01" in filepath:
        continue
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    for pattern, repl in replacements.items():
        content = re.sub(pattern, repl, content, flags=re.IGNORECASE)
    
    # Fix remaining staccato sentences (merge with previous or next sentence)
    # This is a bit risky but we can try to merge sentences < 6 words by replacing their period with a comma or " and".
    # Wait, better to just let the human sysop know, or use a very targeted fix.
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
import os, glob, re

files = glob.glob("/home/user0/git/publishing/100_blog/02_draft/urban_survival_series/*.md")

for filepath in files:
    if "full_corpus" in filepath or "index" in filepath or "07-01" in filepath:
        continue
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    paragraphs = content.split('\n\n')
    new_paragraphs = []
    for p in paragraphs:
        if p.strip().startswith('<!--') or p.strip().startswith('#') or p.strip().startswith('*') or p.strip().startswith('['):
            new_paragraphs.append(p)
            continue
            
        sentences = re.split(r'(?<=[.!?])\s+', p.strip())
        merged = []
        i = 0
        while i < len(sentences):
            s = sentences[i]
            s_clean = re.sub(r'\[.*?\]\(.*?\)', '', s)
            words = re.findall(r'\b[a-zA-Z]+\b', s_clean)
            
            if 0 < len(words) < 6:
                if i + 1 < len(sentences):
                    next_s = sentences[i+1]
                    s = s.rstrip('.!?') + " and " + next_s[:1].lower() + next_s[1:]
                    i += 1
                elif merged:
                    prev = merged.pop()
                    s = prev.rstrip('.!?') + " and " + s[:1].lower() + s[1:]
            merged.append(s)
            i += 1
        new_paragraphs.append(" ".join(merged))
        
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n\n".join(new_paragraphs) + "\n")
