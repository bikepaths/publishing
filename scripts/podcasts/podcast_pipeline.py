#!/usr/bin/env python3
import os
import re

MANUSCRIPT_FILE = "/home/user0/git/publishing/200_amazon_kdp/04_citizens_guide/kdp_v4/refactor/full_manuscript.md"
PODCAST_DIR = "/home/user0/git/publishing/podcasts/podcast_segments/"

def build_podcast_pipeline():
    """Chunks manuscript by headers for TTS podcast pipeline and outputs to dedicated directory."""
    print("Executing Podcast Pipeline (PP) segmentation...")
    os.makedirs(PODCAST_DIR, exist_ok=True)
    
    if not os.path.exists(MANUSCRIPT_FILE):
        print(f"Error: Target manuscript not found at {MANUSCRIPT_FILE}")
        return

    with open(MANUSCRIPT_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Split by Chapter/Unit headers (Level 1 Markdown Headers)
    segments = re.split(r'(?=\n# )', content)
    
    generated_count = 0

    for i, segment in enumerate(segments):
        if not segment.strip():
            continue

        # Extract title for filename
        match = re.search(r'^#\s+(.+)$', segment.strip(), re.MULTILINE)
        title = match.group(1).replace(" ", "_").replace("/", "-") if match else f"segment_{i}"
        title = re.sub(r'[^a-zA-Z0-9_-]', '', title)

        filename = os.path.join(PODCAST_DIR, f"{i:02d}_{title}.md")
        with open(filename, "w", encoding="utf-8") as out:
            out.write(segment.strip())
            
        generated_count += 1

    print(f"Generated {generated_count} podcast segments in {PODCAST_DIR}.")

if __name__ == "__main__":
    build_podcast_pipeline()
