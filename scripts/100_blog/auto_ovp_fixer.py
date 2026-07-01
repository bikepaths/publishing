import os
import glob
import json
import urllib.request
import re

api_key = os.environ.get("OPENROUTER_API_KEY")

def rewrite_paragraph(paragraph):
    prompt = f"""You are an elite OVP editor. Rewrite this paragraph to STRICTLY comply with these constraints:
1. Lexicon: NO slop or weak qualifiers. Banned words: nuanced, holistic, seamless, leverage, utilize, heavy, heavily, essential, fundamentally, specifically, however, perfectly, fosters, greatly, solely, in summary, in conclusion, actively.
2. Sentence Length: EVERY single sentence MUST be between 6 and 22 words. No sentences shorter than 6 words. No sentences longer than 22 words. Split long sentences. Merge short ones.
3. No Em-Dashes (—) or Tricolons (A, B, and C).
4. Physical Action: Use concrete physical verbs. Maintain any grounded metaphors. 

Return ONLY the rewritten paragraph text. Do not add any conversational text.

Original Paragraph:
{paragraph}
"""
    url = "https://openrouter.ai/api/v1/chat/completions"
    data = {"model": "gpt-4o-mini", "messages": [{"role": "user", "content": prompt}]}
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            res_json = json.loads(response.read())
            return res_json["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"Error: {e}")
        return paragraph

def process_file(filepath):
    print(f"Processing {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    blocks = content.split('\n\n')
    new_blocks = []
    
    for block in blocks:
        lines = block.split('\n')
        # Skip metadata, headers, pure links, or image tags
        if all(line.strip().startswith('<!--') or line.strip().startswith('#') or line.strip().startswith('*') or line.strip().startswith('[') or line.strip().startswith('***') for line in lines):
            new_blocks.append(block)
        elif not block.strip():
            new_blocks.append(block)
        else:
            # Check if block has violations
            sentences = re.split(r'(?<=[.!?])\s+', block.strip())
            has_violation = False
            for s in sentences:
                s_clean = re.sub(r'\[.*?\]\(.*?\)', '', s) # ignore links for word count
                words = re.findall(r'\b[a-zA-Z]+\b', s_clean)
                if words and (len(words) < 6 or len(words) > 22 or "—" in s or "-" in s):
                    has_violation = True
                    break
            
            if has_violation:
                rewritten = rewrite_paragraph(block)
                new_blocks.append(rewritten)
            else:
                new_blocks.append(block)
                
    with open(filepath, "w", encoding="utf-8") as f:
        f.write('\n\n'.join(new_blocks) + '\n')

files = glob.glob("/home/user0/git/publishing/100_blog/02_draft/urban_survival_series/*.md")
for f in files:
    if "full_corpus" in f or "index" in f or "07-01" in f:
        continue
    process_file(f)
