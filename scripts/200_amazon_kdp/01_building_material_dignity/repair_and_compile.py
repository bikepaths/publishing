import os
import subprocess
from PIL import Image
from epubcheck import EpubCheck

def repair_front_matter():
    file_path = "/home/user0/git/publishing/200_amazon_kdp/01_building_material_dignity/chapters/00_front_matter.md"
    print(f"Reading {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace <br> with <br />
    repaired = content.replace("<br>", "<br />")
    
    print(f"Writing repaired {file_path}...")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(repaired)

def reencode_cover():
    image_path = "/home/user0/git/publishing/200_amazon_kdp/01_building_material_dignity/v2_cover_material_dignity.png"
    print(f"Re-encoding and padding cover image {image_path} to 1:1.6 aspect ratio...")
    img = Image.open(image_path)
    w, h = img.size
    
    # Target height for 1:1.6 ratio
    new_h = int(w * 1.6)
    new_img = Image.new("RGB", (w, new_h))
    
    # Paste original in center
    offset_y = (new_h - h) // 2
    new_img.paste(img, (0, offset_y))
    
    # Extrude top row
    top_row = img.crop((0, 0, w, 1))
    for y in range(offset_y):
        new_img.paste(top_row, (0, y))
        
    # Extrude bottom row
    bottom_row = img.crop((0, h-1, w, h))
    for y in range(offset_y + h, new_h):
        new_img.paste(bottom_row, (0, y))
        
    new_img.save(image_path, "PNG")
    print("Cover image successfully re-encoded and padded.")

def compile_epub():
    print("Compiling EPUB with pandoc...")
    chapters = [
        "chapters/00_front_matter.md",
        "chapters/01_preface.md",
        "chapters/02_prologue.md",
        "chapters/03_introduction.md",
        "chapters/04_chapter_01.md",
        "chapters/05_chapter_02.md",
        "chapters/06_chapter_03.md",
        "chapters/07_chapter_04.md",
        "chapters/08_chapter_05.md",
        "chapters/09_chapter_06.md",
        "chapters/10_chapter_07.md",
        "chapters/11_chapter_08.md",
        "chapters/12_chapter_09.md",
        "chapters/13_chapter_10.md",
        "chapters/14_chapter_11.md",
        "chapters/15_chapter_12.md",
        "chapters/16_chapter_13.md",
        "chapters/17_chapter_14.md",
        "chapters/18_chapter_15.md",
        "chapters/19_chapter_16.md",
        "chapters/20_about_the_author.md",
        "chapters/21_bibliography.md"
    ]
    
    cmd = [
        "pandoc",
        *chapters,
        "--to", "epub3",
        "--output", "kdp_01_building_material_dignity.epub",
        "--epub-cover-image", "v2_cover_material_dignity.png",
        "--toc",
        "--toc-depth=2",
        "--split-level=1",
        "--metadata", "title=Building Material Dignity: An Urban Stabilization Blueprint for the Unhoused",
        "--metadata", "author=Charles J. DiBella",
        "--metadata", "lang=en-US"
    ]
    
    subprocess.run(cmd, check=True, cwd="/home/user0/git/publishing/200_amazon_kdp/01_building_material_dignity")
    print("EPUB compiled successfully.")

import zipfile
import re
import tempfile
import shutil

def sanitize_epub_toc():
    epub_path = "/home/user0/git/publishing/200_amazon_kdp/01_building_material_dignity/kdp_01_building_material_dignity.epub"
    print(f"Sanitizing landmarks out of EPUB: {epub_path}...")
    
    temp_dir = tempfile.mkdtemp()
    temp_epub_path = os.path.join(temp_dir, "temp.epub")
    
    try:
        with zipfile.ZipFile(epub_path, 'r') as src_zip:
            with zipfile.ZipFile(temp_epub_path, 'w', zipfile.ZIP_DEFLATED) as dest_zip:
                for item in src_zip.infolist():
                    data = src_zip.read(item.filename)
                    if item.filename == "EPUB/nav.xhtml":
                        content = data.decode("utf-8")
                        content = re.sub(
                            r'<nav epub:type="landmarks"[^>]*>.*?</nav>',
                            '',
                            content,
                            flags=re.DOTALL
                        )
                        data = content.encode("utf-8")
                    dest_zip.writestr(item, data)
        
        shutil.move(temp_epub_path, epub_path)
        print("EPUB landmarks successfully sanitized.")
    finally:
        shutil.rmtree(temp_dir)

def validate_epub():
    epub_path = "/home/user0/git/publishing/200_amazon_kdp/01_building_material_dignity/kdp_01_building_material_dignity.epub"
    print(f"Validating EPUB {epub_path}...")
    res = EpubCheck(epub_path)
    print("Is valid:", res.valid)
    print(f"Total messages: {len(res.messages)}")
    for msg in res.messages:
        print(f"[{msg.level}] {msg.message} (File: {msg.file}, Line: {msg.line})")
    
    if not res.valid:
        raise ValueError("EPUB validation failed.")

def deploy_epub():
    src = "/home/user0/git/publishing/200_amazon_kdp/01_building_material_dignity/kdp_01_building_material_dignity.epub"
    dest = "/home/user0/git/publishing/published/kdp_01_building_material_dignity.epub"
    print(f"Deploying compiled EPUB to {dest}...")
    import shutil
    shutil.copy2(src, dest)
    print("Deployment complete.")

def main():
    repair_front_matter()
    reencode_cover()
    compile_epub()
    sanitize_epub_toc()
    validate_epub()
    deploy_epub()

if __name__ == "__main__":
    main()
