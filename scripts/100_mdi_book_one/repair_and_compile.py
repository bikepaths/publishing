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
    print(f"Re-encoding cover image {image_path} to true PNG...")
    img = Image.open(image_path)
    img.save(image_path, "PNG")
    print("Cover image successfully re-encoded.")

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
    validate_epub()
    deploy_epub()

if __name__ == "__main__":
    main()
