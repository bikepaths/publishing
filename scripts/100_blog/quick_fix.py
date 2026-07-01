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
