#!/usr/bin/env python3
"""
epub_assembly.py
Material Dignity Press / SSRN Strategic Intelligence Stack

Assembles a validated epub_source.md from a structured book manifest.
Output is a single pandoc-compatible markdown file ready for epub3 conversion.

Usage:
    python3 epub_assembly.py --manifest manifest.yaml --output epub_source.md

Manifest format (manifest.yaml):
    title: "Book Title"
    subtitle: "Book Subtitle"
    author: "Author Full Name"
    lang: "en-US"
    files:
      - type: copyright
        path: copyright.md
      - type: frontmatter
        heading: "Author's Note"
        path: front_matter.md
        skip_lines: 6          # Skip title block lines at top of file
      - type: chapter
        heading: "Chapter One: Title"
        location: "Location — Date"
        path: chapter_drafts/chapter_01_slug.md
      - type: bibliography
        heading: "Citations and Sources"
        path: citations.md
"""

import argparse
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML not installed. Run: pip3 install pyyaml --break-system-packages")
    sys.exit(1)


def load_manifest(manifest_path: str) -> dict:
    with open(manifest_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def read_file(path: str, skip_lines: int = 0) -> str:
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    if skip_lines:
        lines = lines[skip_lines:]
    return "".join(lines).strip()


def build_yaml_header(manifest: dict) -> str:
    title = manifest.get("title", "Untitled")
    author = manifest.get("author", "Unknown Author")
    lang = manifest.get("lang", "en-US")
    return f'---\ntitle: "{title}"\nauthor: "{author}"\nlang: "{lang}"\n---\n'


def assemble(manifest: dict, output_path: str) -> None:
    base_dir = Path(manifest.get("base_dir", "."))
    blocks = []

    blocks.append(build_yaml_header(manifest))

    for item in manifest.get("files", []):
        item_type = item.get("type", "chapter")
        path = base_dir / item["path"]
        skip = item.get("skip_lines", 0)

        content = read_file(str(path), skip_lines=skip)

        if item_type == "copyright":
            blocks.append(content)

        elif item_type == "frontmatter":
            heading = item.get("heading", "Preface")
            blocks.append(f"\n\n# {heading}\n\n{content}")

        elif item_type == "chapter":
            heading = item.get("heading", "Chapter")
            location = item.get("location", "")
            location_line = f"\n*{location}*\n\n" if location else "\n\n"
            blocks.append(f"\n\n---\n\n# {heading}\n{location_line}{content}")

        elif item_type == "bibliography":
            heading = item.get("heading", "Citations and Sources")
            blocks.append(f"\n\n---\n\n# {heading}\n\n{content}")

        else:
            # Generic section
            heading = item.get("heading", "")
            if heading:
                blocks.append(f"\n\n---\n\n# {heading}\n\n{content}")
            else:
                blocks.append(f"\n\n{content}")

    assembled = "\n\n".join(blocks)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(assembled)

    print(f"Assembled: {output_path}")
    word_count = len(assembled.split())
    print(f"Word count: {word_count:,}")


def main():
    parser = argparse.ArgumentParser(
        description="Assemble epub_source.md from a book manifest."
    )
    parser.add_argument(
        "--manifest",
        required=True,
        help="Path to manifest.yaml"
    )
    parser.add_argument(
        "--output",
        default="epub_source.md",
        help="Output file path (default: epub_source.md)"
    )
    args = parser.parse_args()

    manifest = load_manifest(args.manifest)
    assemble(manifest, args.output)

    print("\nNext step:")
    print(f"  pandoc {args.output} --from markdown+smart --to epub3 \\")
    print(f"    --output ../handoff/[title].epub \\")
    print(f"    --css epub_style.css \\")
    print(f"    --epub-cover-image ../handoff/cover_concept.png \\")
    print(f"    --toc --toc-depth=1 --split-level=1 \\")
    print(f"    --metadata title=\"{manifest.get('title', 'Title')}\" \\")
    print(f"    --metadata author=\"{manifest.get('author', 'Author')}\" \\")
    print(f"    --metadata lang=\"{manifest.get('lang', 'en-US')}\"")


if __name__ == "__main__":
    main()
