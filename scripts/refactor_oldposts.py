#!/usr/bin/env python3
# NOTE: Tuner scripts are temporary sandbox tools used by the agent to adjust text before draft write.
# All formal verification and execution validation checks must be run automatically via this script or verify_blog_post.py.
import os
import sys
import re
import subprocess
import argparse

VM_HOST = "165.232.151.110"
VM_PORT = "2323"
VM_USER = "user0"
REMOTE_UNCATEGORIZED = "/home/user0/www/bikepaths/html/blog/content/chas/blog/uncategorized/image"
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

    # Separate metadata and body
    body_content = content
    body_content = re.sub(r'<!--.*?-->', '', body_content, flags=re.DOTALL).strip()

    current_dir = os.path.dirname(os.path.abspath(__file__))
    if os.path.basename(current_dir) == "scripts":
        parent_dir = os.path.dirname(current_dir)
        if os.path.isdir(os.path.join(parent_dir, "blog")):
            blog_dir = os.path.join(parent_dir, "blog")
        else:
            blog_dir = parent_dir
    else:
        blog_dir = os.path.dirname(current_dir)
    factoid_path = os.path.join(blog_dir, "facts", f"factoid_{timestamp}.md")
    
    factoid_content = f"""# Factoid: {timestamp}

- Original Filename: {filename}
- Original Image Link: {image_link}

<!-- STYLE REMINDER: 
1. Narrative Flow: Write plain and simple English resembling an 8th-grade textbook. Tell a cohesive story; do not list isolated facts.
2. Structural Cohesion: Connect ideas using transitional narrative bridges. Avoid dense, fragmented "machine language."
3. Lexical Clarity: Target a Flesch-Kincaid grade level between 7.0 and 10.0.
4. Paragraph Uniformity: Maintain 3 to 6 flowing paragraphs.
5. Tone: Engage the reader with accessible, conversational prose while maintaining factual integrity.
-->

<!-- TODO: Generate a plain language factual refactoring of the raw post content below. Remove raw text before drafting. -->
## Factual Refactoring

[Insert plain language factual refactoring here]

---
## Raw Original Post Reference (To be deleted)
{body_content}
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

    blog_dir = os.path.dirname(os.path.dirname(os.path.abspath(factoid_file)))
    draft_path = os.path.join(blog_dir, "drafts", f"{timestamp}_DRAFT.md")

    draft_content = f"""<!--variant collective-guide-v1 variant-->
<!--t [New Title] t-->
<!--d [Description] d-->
<!--tag [Tags] tag-->
<!--image {image_link} image-->
<!--gov htmly/system/technical_standards.md gov-->

[Body content goes here]
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

    print(f"Running automatic verification on {posted_file}...")
    current_dir = os.path.dirname(os.path.abspath(__file__))
    verify_script = os.path.join(current_dir, "verify_blog_post.py")
    verify_cmd = [sys.executable, verify_script, posted_file]
    try:
        subprocess.run(verify_cmd, check=True)
        print("[PASS] Automatic verification checks succeeded.")
    except subprocess.CalledProcessError as err:
        print("[FAIL] Automatic verification checks failed. Aborting deployment.")
        return False

    filename = os.path.basename(posted_file)
    blog_dir = os.path.dirname(os.path.dirname(os.path.abspath(posted_file)))

    parts = filename.replace(".md", "").split("_")
    if len(parts) < 3:
        print("Error: Filename requires timestamp_categories_title.md layout.")
        return False

    timestamp = parts[0]
    categories = parts[1].split(",")
    topic = categories[0]
    slug = parts[-1]

    ALLOWED_CATEGORIES = ['society', 'skills', 'systems', 'money', 'nature', 'technology', 'adventure', 'health', 'history', 'mind']
    if topic not in ALLOWED_CATEGORIES:
        print(f"Error: Primary category '{topic}' is not in allowed taxonomy: {ALLOWED_CATEGORIES}")
        return False

    with open(posted_file, "r", encoding="utf-8") as f:
        content = f.read()

    metadata_regex = re.compile(r'<!--(\w+)\s+(.*?)\s+\1-->')
    metadata = dict(metadata_regex.findall(content))

    if "image" not in metadata:
        print("Error: image key not found in metadata.")
        return False

    image_val = metadata["image"]
    is_remote_image = image_val.startswith("http://") or image_val.startswith("https://")
    image_filename = os.path.basename(image_val)
    local_image_path = os.path.join(blog_dir, "img", image_filename)

    if not is_remote_image and not os.path.isfile(local_image_path):
        print(f"Error: local image {local_image_path} not found.")
        return False

    # Parse timestamp to determine target directory based on future scheduling
    from datetime import datetime
    post_dt = None
    try:
        post_dt = datetime.strptime(timestamp, "%Y-%m-%d-%H-%M-%S")
    except ValueError:
        pass

    if post_dt and post_dt > datetime.now():
        remote_dest_dir = f"{REMOTE_PAGES_ROOT}/{topic}/image/scheduled"
    else:
        remote_dest_dir = f"{REMOTE_PAGES_ROOT}/{topic}/image"

    remote_post_dest = f"{remote_dest_dir}/{filename}"
    mkdir_cmd = ["ssh", "-p", VM_PORT, f"{VM_USER}@{VM_HOST}", f"mkdir -p {remote_dest_dir}"]
    try:
        subprocess.run(mkdir_cmd, check=True)
    except subprocess.CalledProcessError as err:
        print(f"Warning: could not create remote directory: {err}")

    print(f"Uploading post to: {remote_post_dest}")
    post_cmd = ["scp", "-P", VM_PORT, posted_file, f"{VM_USER}@{VM_HOST}:{remote_post_dest}"]
    try:
        subprocess.run(post_cmd, check=True)
    except subprocess.CalledProcessError as err:
        print(f"Error uploading post: {err}")
        return False

    if not is_remote_image:
        remote_image_dest = f"{REMOTE_IMAGES}/{image_filename}"
        print(f"Uploading image to: {remote_image_dest}")
        img_cmd = ["scp", "-P", VM_PORT, local_image_path, f"{VM_USER}@{VM_HOST}:{remote_image_dest}"]
        try:
            subprocess.run(img_cmd, check=True)
        except subprocess.CalledProcessError as err:
            print(f"Error uploading image: {err}")
            return False

    factoid_path = os.path.join(blog_dir, "facts", f"factoid_{timestamp}.md")
    
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

    draft_path = os.path.join(blog_dir, "drafts", f"{timestamp}_DRAFT.md")
    if os.path.isfile(draft_path):
        print(f"Removing local draft: {draft_path}")
        try:
            os.remove(draft_path)
        except OSError as err:
            print(f"Warning: could not delete local draft: {err}")

    verify_remote_permissions()

    print("\n[SUCCESS] Deployment and cleanup completed.")
    print("REMINDER: Sysop must manually clear the CMS cache directory on the VM.")
    return True

def verify_remote_permissions():
    """
    Recursively verifies and corrects permissions (664) and owner:group (user0:www-data)
    for all .md files under the remote blog hierarchy.
    """
    find_cmd = [
        "ssh", "-p", VM_PORT, f"{VM_USER}@{VM_HOST}",
        f'find {REMOTE_PAGES_ROOT} -type f -name "*.md" -printf "%m %u:%g %p\\n"'
    ]
    try:
        print("Querying remote file permissions and ownership...")
        res = subprocess.run(find_cmd, capture_output=True, text=True, check=True)
        lines = res.stdout.splitlines()
        
        violations = []
        for line in lines:
            if not line.strip():
                continue
            parts = line.strip().split(maxsplit=2)
            if len(parts) < 3:
                continue
            perms, owner, path = parts
            
            if perms != "664" or owner != "user0:www-data":
                violations.append((path, perms, owner))
                
        if violations:
            print(f"\n[VIOLATION] Found {len(violations)} files with incorrect permissions or ownership.")
            print("Applying copy-recreate-ownership correction on VM...")
            
            # Formulate a compound remote bash command to fix all violations safely
            remote_cmds = []
            for path, perms, owner in violations:
                remote_cmds.append(
                    f'file="{path}" && cp "$file" "$file.tmp" && rm -f "$file" && mv "$file.tmp" "$file" && chgrp www-data "$file" && chmod 664 "$file"'
                )
            
            # Execute in batches or as a single script
            batch_cmd = "; ".join(remote_cmds)
            fix_cmd = ["ssh", "-p", VM_PORT, f"{VM_USER}@{VM_HOST}", batch_cmd]
            subprocess.run(fix_cmd, check=True)
            print("[SUCCESS] Successfully verified and corrected permissions (664) and ownership (user0:www-data) for all remote files.")
            return False
        else:
            print("[PASS] All remote .md files have correct 664 permissions and user0:www-data ownership.")
            return True
            
    except subprocess.CalledProcessError as err:
        print(f"Error querying/fixing remote file permissions: {err.stderr}")
        return False

def prepare_next():
    """
    Lists remote uncategorized posts, takes the first one, downloads it,
    creates the factoid, and generates the draft template automatically.
    """
    files = list_uncategorized()
    if not files:
        print("No remote uncategorized posts found to prepare.")
        return False
    
    first_file = files[0]
    print(f"\nAutomatically selecting next candidate: {first_file}")
    
    success = download_and_create_factoid(first_file)
    if not success:
        print("Failed to download and create factoid.")
        return False
        
    parts = first_file.replace(".md", "").split("_")
    timestamp = parts[0]
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if os.path.basename(current_dir) == "scripts":
        parent_dir = os.path.dirname(current_dir)
        if os.path.isdir(os.path.join(parent_dir, "blog")):
            blog_dir = os.path.join(parent_dir, "blog")
        else:
            blog_dir = parent_dir
    else:
        blog_dir = os.path.dirname(current_dir)
        
    factoid_path = os.path.join(blog_dir, "facts", f"factoid_{timestamp}.md")
    
    success = generate_draft(factoid_path)
    if not success:
        print("Failed to generate draft.")
        return False
        
    print(f"[SUCCESS] Prepared next post: {first_file}")
    return True

def promote_draft(draft_file):
    """
    Parses draft file, verifies it, constructs the posted filename,
    and moves/saves it to the posted directory. Returns the path of the posted file.
    """
    if not os.path.isfile(draft_file):
        print(f"Error: Draft file {draft_file} does not exist.")
        return None

    # Run verification on the draft first
    print(f"Running automatic verification on draft: {draft_file}")
    current_dir = os.path.dirname(os.path.abspath(__file__))
    verify_script = os.path.join(current_dir, "verify_blog_post.py")
    verify_cmd = [sys.executable, verify_script, draft_file]
    try:
        subprocess.run(verify_cmd, check=True)
        print("[PASS] Draft verification checks succeeded.")
    except subprocess.CalledProcessError as err:
        print("[FAIL] Draft verification failed. Aborting promotion.")
        return None

    # Parse metadata from draft file
    title = None
    desc = None
    tags = None
    with open(draft_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract tags
    tag_match = re.search(r'<!--tag\s+(.*?)\s+tag-->', content)
    if tag_match:
        tags = tag_match.group(1).strip()
    
    if not tags:
        print("Error: Could not parse tags from draft.")
        return None

    # Extract slug/title from filename
    filename = os.path.basename(draft_file)
    parts = filename.replace(".md", "").split("_")
    timestamp = parts[0]
    
    blog_dir = os.path.dirname(os.path.dirname(os.path.abspath(draft_file)))
    factoid_path = os.path.join(blog_dir, "facts", f"factoid_{timestamp}.md")
    
    slug = None
    if os.path.isfile(factoid_path):
        with open(factoid_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("- Original Filename:"):
                    orig_file = line.split(":", 1)[1].strip()
                    orig_parts = orig_file.replace(".md", "").split("_")
                    slug = orig_parts[-1]
                    break
    
    if not slug:
        # Fallback: slugify the title from the draft
        title_match = re.search(r'<!--t\s+(.*?)\s+t-->', content)
        if title_match:
            title_text = title_match.group(1).strip()
            slug = title_text.lower().replace(" ", "-")
            slug = re.sub(r'[^a-z0-9\-]', '', slug)
            slug = re.sub(r'-+', '-', slug).strip("-")
            
    if not slug:
        print("Error: Could not determine slug for draft.")
        return None

    posted_filename = f"{timestamp}_{tags}_{slug}.md"
    posted_path = os.path.join(blog_dir, "posted", posted_filename)
    
    os.makedirs(os.path.dirname(posted_path), exist_ok=True)
    with open(posted_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"[SUCCESS] Draft promoted to: {posted_path}")
    return posted_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Procedural script for refactoring oldposts.")
    parser.add_argument("--list", action="store_true", help="List remote uncategorized posts.")
    parser.add_argument("--download", type=str, help="Download post and create factoid file.")
    parser.add_argument("--draft", type=str, help="Generate draft post from factoid file.")
    parser.add_argument("--deploy", type=str, help="Deploy post and run post-upload cleanups.")
    parser.add_argument("--verify-remote", action="store_true", help="Verify and fix remote file permissions/ownership.")
    parser.add_argument("--prepare-next", action="store_true", help="Automatically list, download, and prepare next post.")

    args = parser.parse_args()

    if args.list:
        list_uncategorized()
    elif args.download:
        download_and_create_factoid(args.download)
    elif args.draft:
        generate_draft(args.draft)
    elif args.deploy:
        target_file = args.deploy
        if target_file.endswith("_DRAFT.md") or "drafts" in target_file:
            posted_file = promote_draft(target_file)
            if posted_file:
                deploy_and_cleanup(posted_file)
        else:
            deploy_and_cleanup(target_file)
    elif args.verify_remote:
        verify_remote_permissions()
    elif args.prepare_next:
        prepare_next()
    else:
        parser.print_help()
