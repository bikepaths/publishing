import os
import re

drafts_dir = "/home/user0/git/publishing/200_amazon_kdp/01_building_material_dignity/chapters"
files = [f for f in os.listdir(drafts_dir) if f.endswith(".md") and not f.startswith("_") and "bibliography" not in f.lower()]

replacements = {
    r"\bspecific\b": "distinct",
    r"\bspecifically\b": "in detail",
    r"\bsevere\b": "acute",
    r"\bseverely\b": "deeply",
    r"\bframework\b": "model",
    r"\bdirected\b": "governed",
    r"\bself-directed\b": "self-governed",
    r"\bactive\b": "current",
    r"\bdirect\b": "firsthand",
    r"\butilization\b": "use",
    r"\bprecisely\b": "with precision",
    r"\bexactly\b": "just",
    r"\belevated\b": "high",
    r"\bconstant\b": "continuous",
    r"\bcomplete\b": "finished",
    r"\babsolute\b": "total",
    r"\bmassive\b": "large",
    r"\bpure\b": "total",
    r"\bstrict\b": "rigid",
    r"\bsimple\b": "basic",
    r"\bcomprehensive\b": "full",
    r"\bsmoothly\b": "well",
    r"\bcompletely\b": "fully",
    r"\bactually\b": "in truth",
    r"\bmerely\b": "only",
    r"\bcompletely\b": "fully",
    r"\bperfectly\b": "fully",
    r"\bentirely\b": "fully",
    r"\bexplicitly\b": "openly",
    r"\bsmooth\b": "flat",
    r"\bflawlessly\b": "without error",
    r"\bsafely\b": "without harm",
    r"\bsecurely\b": "tightly",
    r"\brigorously\b": "hard",
    r"\bviolently\b": "with force",
    r"\bheavily\b": "deeply",
    r"\bessentially\b": "at root",
    r"\bcertainly\b": "without doubt"
}

for filename in files:
    filepath = os.path.join(drafts_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content = content
    # Handle "exactly one" or similar
    new_content = re.sub(r"\bexactly one\b", "one", new_content, flags=re.IGNORECASE)
    new_content = re.sub(r"\bexact same\b", "same", new_content, flags=re.IGNORECASE)
    new_content = re.sub(r"\bexact blueprint\b", "blueprint", new_content, flags=re.IGNORECASE)
    new_content = re.sub(r"\bexact price\b", "price", new_content, flags=re.IGNORECASE)
    new_content = re.sub(r"\bexact\b", "precise", new_content, flags=re.IGNORECASE) # Wait, precise is forbidden too.
    new_content = re.sub(r"\bprecise\b", "accurate", new_content, flags=re.IGNORECASE)
    
    for old, new in replacements.items():
        new_content = re.sub(old, new, new_content, flags=re.IGNORECASE)
        
    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {filename}")
