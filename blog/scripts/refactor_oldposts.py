#!/usr/bin/env python3
import os
import sys
import re
import subprocess
import argparse

VM_HOST = "165.232.151.110"
VM_PORT = "2323"
VM_USER = "user0"
REMOTE_UNCATEGORIZED = "/home/user0/www/bikepaths/html/blog/content/chas/blog/uncategorized"
REMOTE_PAGES_ROOT = "/home/user0/www/bikepaths/html/blog/content/chas/blog"
REMOTE_IMAGES = "/home/user0/www/bikepaths/html/blog/content/images"
REMOTE_CACHE = "/home/user0/www/bikepaths/html/blog/content/cache"

def list_uncategorized():
    """
    Lists files in the remote uncategorized directory.
    """
    cmd = ["ssh", "-p", VM_PORT, f"{VM_USER}@{VM_HOST}", f"ls -1 {REMOTE_UNCATEGORIZED}"]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        files = [f.strip() for f in res.stdout.splitlines() if f.strip().endswith(".md")]
        print("Remote uncategorized posts found:")
        for idx, filename in enumerate(files, 1):
            print(f"{idx}: {filename}")
        return files
    except subprocess.CalledProcessError as err:
        print(f"Error listing remote directory: {err.stderr}")
        return []

def download_and_create_factoid(filename):
    """
    Downloads remote old post and extracts facts metadata.
    """
    local_temp = os.path.join("/tmp", filename)
    scp_cmd = ["scp", "-P", VM_PORT, f"{VM_USER}@{VM_HOST}:{REMOTE_UNCATEGORIZED}/{filename}", local_temp]
    
    try:
        subprocess.run(scp_cmd, check=True)
    except subprocess.CalledProcessError as err:
        print(f"Error downloading file: {err}")
        return False

    with open(local_temp, "r", encoding="utf-8") as f:
        content = f.read()

    parts = filename.replace(".md", "").split("_")
    if len(parts) >= 3:
        timestamp = parts[0]
        slug = parts[-1]
    else:
        timestamp = parts[0]
        slug = "_".join(parts[1:])

    original_timestamp_slug = f"{timestamp}_{slug}"

    image_regex = re.compile(r'<!--image\s+(.*?)\s+image-->')
    match = image_regex.search(content)
    image_link = match.group(1) if match else "None"

    blog_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    factoid_path = os.path.join(blog_dir, "facts", f"factoid_{original_timestamp_slug}.md")
    
    factoid_content = f"""# Factoid: {original_timestamp_slug}

- Original Filename: {filename}
- Original Image Link: {image_link}

## Compiled Facts
- [Insert compiled facts here]
"""

    with open(factoid_path, "w", encoding="utf-8") as f:
        f.write(factoid_content)

    print(f"Factoid created: {factoid_path}")
    
    if os.path.exists(local_temp):
        os.remove(local_temp)
    return True

def generate_draft(factoid_file):
    """
    Generates draft post from facts definition.
    """
    if not os.path.isfile(factoid_file):
        print(f"Error: {factoid_file} is not a valid file.")
        return False

    with open(factoid_file, "r", encoding="utf-8") as f:
        content = f.read()

    filename_match = re.search(r'- Original Filename:\s+(.*)', content)
    image_match = re.search(r'- Original Image Link:\s+(.*)', content)
    
    if not filename_match:
        print("Error: Could not find original filename key in factoid.")
        return False

    orig_filename = filename_match.group(1).strip()
    image_link = image_match.group(1).strip() if image_match else "None"

    parts = orig_filename.replace(".md", "").split("_")
    timestamp = parts[0]

    blog_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(factoid_file))))
    draft_path = os.path.join(blog_dir, "drafts", f"{timestamp}_DRAFT.md")

    draft_content = f"""<!--variant collective-guide-v1 variant-->
<!--t [New Title] t-->
<!--d [Description] d-->
<!--tag [Tags] tag-->
<!--image {image_link} image-->
<!--gov htmly/system/technical_standards.md gov-->

**[New Title]**

[Body content goes here]

#### Glossary
*Term* Definition.

#### Assumptions and Assertions
1. Claim assertion.

#### Reference Citations
Author. Year. Title.
"""

    with open(draft_path, "w", encoding="utf-8") as f:
        f.write(draft_content)

    print(f"Draft generated: {draft_path}")
    return True

def deploy_and_cleanup(posted_file):
    """
    Deploys verified post, removes remote uncategorized oldpost, and flushes cache.
    """
    if not os.path.isfile(posted_file):
        print(f"Error: {posted_file} does not exist.")
        return False

    filename = os.path.basename(posted_file)
    blog_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(posted_file))))

    parts = filename.replace(".md", "").split("_")
    if len(parts) < 3:
        print("Error: Filename requires timestamp_categories_title.md layout.")
        return False

    timestamp = parts[0]
    categories = parts[1].split(",")
    topic = categories[0]
    slug = parts[-1]

    with open(posted_file, "r", encoding="utf-8") as f:
        content = f.read()

    metadata_regex = re.compile(r'<!--(\w+)\s+(.*?)\s+\1-->')
    metadata = dict(metadata_regex.findall(content))

    if "image" not in metadata:
        print("Error: image key not found in metadata.")
        return False

    image_val = metadata["image"]
    image_filename = os.path.basename(image_val)
    local_image_path = os.path.join(blog_dir, "img", image_filename)

    if not os.path.isfile(local_image_path):
        print(f"Error: local image {local_image_path} not found.")
        return False

    remote_post_dest = f"{REMOTE_PAGES_ROOT}/{topic}/image/scheduled/{filename}"
    print(f"Uploading post to: {remote_post_dest}")
    post_cmd = ["scp", "-P", VM_PORT, posted_file, f"{VM_USER}@{VM_HOST}:{remote_post_dest}"]
    try:
        subprocess.run(post_cmd, check=True)
    except subprocess.CalledProcessError as err:
        print(f"Error uploading post: {err}")
        return False

    remote_image_dest = f"{REMOTE_IMAGES}/{image_filename}"
    print(f"Uploading image to: {remote_image_dest}")
    img_cmd = ["scp", "-P", VM_PORT, local_image_path, f"{VM_USER}@{VM_HOST}:{remote_image_dest}"]
    try:
        subprocess.run(img_cmd, check=True)
    except subprocess.CalledProcessError as err:
        print(f"Error uploading image: {err}")
        return False

    original_timestamp_slug = f"{timestamp}_{slug}"
    factoid_path = os.path.join(blog_dir, "facts", f"factoid_{original_timestamp_slug}.md")
    
    orig_filename = None
    if os.path.isfile(factoid_path):
        with open(factoid_path, "r", encoding="utf-8") as f:
            factoid_content = f.read()
        filename_match = re.search(r'- Original Filename:\s+(.*)', factoid_content)
        if filename_match:
            orig_filename = filename_match.group(1).strip()

    if not orig_filename:
        orig_filename = f"{timestamp}_uncategorized_{slug}.md"
        print(f"Factoid not found, guessing legacy filename: {orig_filename}")

    remote_old_path = f"{REMOTE_UNCATEGORIZED}/{orig_filename}"
    print(f"Removing oldpost: {remote_old_path}")
    rm_cmd = ["ssh", "-p", VM_PORT, f"{VM_USER}@{VM_HOST}", f"rm -f {remote_old_path}"]
    try:
        subprocess.run(rm_cmd, check=True)
    except subprocess.CalledProcessError as err:
        print(f"Warning: could not delete remote file: {err}")

    print("Flushing CMS cache directory...")
    cache_cmd = ["ssh", "-p", VM_PORT, f"{VM_USER}@{VM_HOST}", f"rm -rf {REMOTE_CACHE}/*"]
    try:
        subprocess.run(cache_cmd, check=True)
        print("CMS cache flush complete.")
    except subprocess.CalledProcessError as err:
        print(f"Warning: cache flush failed: {err}")

    print("\n[SUCCESS] Deployment, cleanup, and cache clear completed.")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Procedural script for refactoring oldposts.")
    parser.add_argument("--list", action="store_true", help="List remote uncategorized posts.")
    parser.add_argument("--download", type=str, help="Download post and create factoid file.")
    parser.add_argument("--draft", type=str, help="Generate draft post from factoid file.")
    parser.add_argument("--deploy", type=str, help="Deploy post and run post-upload cleanups.")

    args = parser.parse_args()

    if args.list:
        list_uncategorized()
    elif args.download:
        download_and_create_factoid(args.download)
    elif args.draft:
        generate_draft(args.draft)
    elif args.deploy:
        deploy_and_cleanup(args.deploy)
    else:
        parser.print_help()
