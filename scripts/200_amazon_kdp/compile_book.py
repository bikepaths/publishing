#!/usr/bin/env python3
"""
compile_book.py
Material Dignity Press / SSRN Strategic Intelligence Stack

Centralized compilation pipeline for KDP book production.
Handles manifest assembly, square cover padding (edge extrusion),
pandoc compilation (EPUB3 & DOCX), EPUB TOC landmarks sanitization,
and EpubCheck validation.

Usage:
    python3 compile_book.py --book [1|2|3] --format [epub|docx|both]
"""

import os
import sys
import argparse
import re
import zipfile
import shutil
import tempfile
import subprocess
from pathlib import Path
from PIL import Image

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML not installed. Run: pip3 install pyyaml --break-system-packages")
    sys.exit(1)


# Book directories mapping
BOOKS = {
    1: {
        "dir_name": "01_building_material_dignity",
        "output_name": "kdp_01_building_material_dignity",
        "epub_title": "Building Material Dignity: An Urban Stabilization Blueprint for the Unhoused"
    },
    2: {
        "dir_name": "02_architecture_of_survival",
        "output_name": "the_architecture_of_survival",
        "epub_title": "The Architecture of Survival"
    },
    3: {
        "dir_name": "03_survival_physics",
        "output_name": "the_moral_physics_of_survival",
        "epub_title": "The Moral Physics of Survival"
    },
    4: {
        "dir_name": "04_graduating_the_streets",
        "output_name": "graduating_the_streets",
        "epub_title": "Graduating the Streets: A Phase Zero Case Study in Material Dignity"
    }
}


def load_manifest(manifest_path: Path) -> dict:
    with open(manifest_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def find_cover_image(kdp_dir: Path) -> Path:
    # Look for cover images in standard subfolders, prioritizing custom padded covers
    search_paths = [
        "production/cover_padded.png",
        "production/cover_padded.jpg",
        "production/cover.png",
        "production/cover.jpg",
        "handoff/cover_padded.png",
        "handoff/cover_padded.jpg",
        "handoff/cover.png",
        "handoff/cover.jpg",
        "handoff/cover_concept.png"
    ]
    for rel_path in search_paths:
        path = kdp_dir / rel_path
        if path.exists():
            return path
    # Check parent/root folder
    for ext in ["png", "jpg", "jpeg"]:
        for path in kdp_dir.glob(f"*.{ext}"):
            if "cover" in path.name.lower():
                return path
    return None


def pad_cover_image(image_path: Path) -> Path:
    img = Image.open(image_path)
    width, height = img.size
    
    # If image is square, pad to standard vertical 1:1.5 aspect ratio
    if width == height:
        print(f"Detected square cover: {width}x{height}. Padding to 1:1.5...")
        new_height = int(width * 1.5)
        
        # Create new vertical canvas
        padded_img = Image.new("RGB", (width, new_height))
        y_offset = (new_height - height) // 2
        padded_img.paste(img, (0, y_offset))
        
        # Extrude top pixel row seamlessly
        top_row = img.crop((0, 0, width, 1))
        for y in range(y_offset):
            padded_img.paste(top_row, (0, y))
            
        # Extrude bottom pixel row seamlessly
        bottom_row = img.crop((0, height - 1, width, height))
        for y in range(y_offset + height, new_height):
            padded_img.paste(bottom_row, (0, y))
            
        # Output padded file path
        output_path = image_path.parent / f"{image_path.stem}_padded{image_path.suffix}"
        padded_img.save(output_path, quality=95)
        print(f"Padded cover saved: {output_path}")
        return output_path
        
    return image_path


def assemble_markdown(manifest: dict, base_dir: Path, include_yaml_header: bool = True) -> str:
    blocks = []
    
    if include_yaml_header:
        title = manifest.get("title", "Untitled")
        author = manifest.get("author", "Unknown Author")
        lang = manifest.get("lang", "en-US")
        blocks.append(f'---\ntitle: "{title}"\nauthor: "{author}"\nlang: "{lang}"\n---\n')
    
    for item in manifest.get("files", []):
        item_type = item.get("type", "chapter")
        path = base_dir / item["path"]
        skip = item.get("skip_lines", 0)
        
        if not path.exists():
            print(f"ERROR: File not found: {path}")
            sys.exit(1)
            
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        if skip:
            lines = lines[skip:]
        content = "".join(lines).strip()
        
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
            heading = item.get("heading", "")
            if heading:
                blocks.append(f"\n\n---\n\n# {heading}\n\n{content}")
            else:
                blocks.append(f"\n\n{content}")
                
    return "\n\n".join(blocks)


def sanitize_epub_toc(epub_path: Path):
    print(f"Sanitizing landmarks out of EPUB TOC...")
    temp_dir = epub_path.parent / "epub_temp"
    if temp_dir.exists():
        shutil.rmtree(temp_dir)
    temp_dir.mkdir()
    
    with zipfile.ZipFile(epub_path, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)
        
    nav_files = list(temp_dir.glob("**/nav.xhtml"))
    if not nav_files:
        print("WARNING: nav.xhtml not found. Skipping landmark sanitization.")
        shutil.rmtree(temp_dir)
        return
        
    nav_file = nav_files[0]
    with open(nav_file, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Regex to strip landmarks block
    cleaned_content = re.sub(
        r'<nav\s+epub:type="landmarks"[^>]*>.*?</nav>',
        '',
        content,
        flags=re.DOTALL
    )
    
    with open(nav_file, "w", encoding="utf-8") as f:
        f.write(cleaned_content)
        
    # Re-zip keeping mimetype uncompressed first
    with zipfile.ZipFile(epub_path, 'w') as zip_ref:
        mimetype_path = temp_dir / "mimetype"
        if mimetype_path.exists():
            zip_ref.write(mimetype_path, "mimetype", compress_type=zipfile.ZIP_STORED)
            
        for file_path in temp_dir.rglob("*"):
            if file_path.is_file() and file_path.name != "mimetype":
                arcname = file_path.relative_to(temp_dir)
                zip_ref.write(file_path, arcname, compress_type=zipfile.ZIP_DEFLATED)
                
    shutil.rmtree(temp_dir)
    print("Sanitization completed successfully.")


def validate_epub(epub_path: Path):
    try:
        from epubcheck import EpubCheck
        print("Validating EPUB with EpubCheck...")
        result = EpubCheck(str(epub_path))
        print(f"Is valid: {result.valid}")
        print(f"Validation Messages: {len(result.messages)}")
        for msg in result.messages[:5]:
            print(f" - [{msg.get('level', 'WARNING')}] {msg.get('message')}")
        if len(result.messages) > 5:
            print(f" - ... and {len(result.messages) - 5} more.")
        return result.valid
    except ImportError:
        print("WARNING: python-epubcheck library not installed. Validation skipped.")
        return True


def main():
    parser = argparse.ArgumentParser(description="Compile books from SSRN publishing stack.")
    parser.add_argument("--book", type=int, choices=[1, 2, 3, 4], required=True, help="Book number to compile (1, 2, 3, or 4)")
    parser.add_argument("--format", choices=["epub", "docx", "both"], default="both", help="Target output format")
    args = parser.parse_args()

    book_info = BOOKS[args.book]
    workspace_root = Path("/home/user0/git/publishing")
    book_root = workspace_root / "200_amazon_kdp" / book_info["dir_name"]
    kdp_dir = book_root / "kdp"
    
    # Support Book One flat directory structure if it is not yet fully migrated to kdp/ subfolders
    if not kdp_dir.exists():
        kdp_dir = book_root
        
    manuscript_dir = kdp_dir / "manuscript"
    handoff_dir = kdp_dir / "handoff"
    
    if not manuscript_dir.exists():
        print(f"ERROR: Manuscript directory not found: {manuscript_dir}")
        sys.exit(1)
        
    handoff_dir.mkdir(parents=True, exist_ok=True)
    
    manifest_path = manuscript_dir / "manifest.yaml"
    if not manifest_path.exists():
        print(f"ERROR: manifest.yaml not found at {manifest_path}")
        sys.exit(1)
        
    print(f"--- Compiling Book {args.book}: {book_info['epub_title']} ---")
    manifest = load_manifest(manifest_path)
    
    # 1. Assemble Markdowns
    print("Assembling source markdown files...")
    epub_source_content = assemble_markdown(manifest, manuscript_dir, include_yaml_header=True)
    epub_source_path = manuscript_dir / "epub_source.md"
    with open(epub_source_path, "w", encoding="utf-8") as f:
        f.write(epub_source_content)
        
    docx_source_content = assemble_markdown(manifest, manuscript_dir, include_yaml_header=False)
    docx_source_path = manuscript_dir / "full_manuscript.md"
    with open(docx_source_path, "w", encoding="utf-8") as f:
        f.write(docx_source_content)
        
    print(f"Assembled epub_source.md ({len(epub_source_content.split()):,} words)")
    print(f"Assembled full_manuscript.md ({len(docx_source_content.split()):,} words)")
    
    # 2. Cover processing (for EPUB target only)
    cover_path = find_cover_image(kdp_dir)
    padded_cover_path = None
    if cover_path:
        print(f"Cover image found: {cover_path}")
        try:
            padded_cover_path = pad_cover_image(cover_path)
        except Exception as e:
            print(f"WARNING: Cover padding failed: {e}")
            padded_cover_path = cover_path
    else:
        print("WARNING: No cover image detected.")
        
    # 3. EPUB Compilation
    if args.format in ["epub", "both"]:
        epub_out_path = handoff_dir / f"{book_info['output_name']}.epub"
        print(f"Compiling EPUB: {epub_out_path}...")
        
        css_file = manuscript_dir / "epub_style.css"
        if not css_file.exists():
            # Try workspace styles fallback
            css_file = workspace_root / "_styles" / "MoS_NYT_Magazine.md"  # placeholder or fallback
            
        cmd = [
            "pandoc",
            str(epub_source_path),
            "--to", "epub3",
            "--output", str(epub_out_path),
            "--toc",
            "--toc-depth=1",
            "--split-level=1",
            "--metadata", f"title={book_info['epub_title']}",
            "--metadata", f"author={manifest.get('author', 'Charles J. DiBella')}",
            "--metadata", f"lang={manifest.get('lang', 'en-US')}"
        ]
        
        if css_file.exists() and css_file.suffix == ".css":
            cmd.extend(["--css", str(css_file)])
        if padded_cover_path:
            cmd.extend(["--epub-cover-image", str(padded_cover_path)])
            
        subprocess.run(cmd, check=True, cwd=str(manuscript_dir))
        print("EPUB generated.")
        
        # Sanitize Landmarks
        sanitize_epub_toc(epub_out_path)
        
        # Validate EPUB
        validate_epub(epub_out_path)
        

    # 4. DOCX Compilation
    if args.format in ["docx", "both"]:
        docx_out_path = handoff_dir / f"{book_info['output_name']}.docx"
        print(f"Compiling DOCX: {docx_out_path}...")
        
        cmd = [
            "pandoc",
            str(docx_source_path),
            "-o", str(docx_out_path),
            "--from", "markdown"
        ]
        
        subprocess.run(cmd, check=True, cwd=str(manuscript_dir))
        print("DOCX compiled successfully.")
        


if __name__ == "__main__":
    main()
