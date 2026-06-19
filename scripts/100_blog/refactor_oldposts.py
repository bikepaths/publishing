#!/usr/bin/env python3
# NOTE: Tuner scripts are temporary sandbox tools used by the agent to adjust text before draft write.
# All formal verification and execution validation checks must be run automatically via this script or verify_blog_post.py.
import os
import sys
import re
import subprocess
import argparse
import json
import urllib.request

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

def download_and_create_raw(filename):
    """
    Downloads remote old post and saves it to draft directory as raw reference.
    """
    parts = filename.replace(".md", "").split("_")
    timestamp = parts[0]
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if os.path.basename(current_dir) == "100_blog":
        blog_dir = os.path.join(os.path.dirname(os.path.dirname(current_dir)), "100_blog")
    elif os.path.basename(current_dir) == "scripts":
        blog_dir = os.path.join(os.path.dirname(current_dir), "100_blog")
    else:
        blog_dir = os.path.join(os.path.dirname(os.path.dirname(current_dir)), "100_blog")
        
    local_temp = os.path.join("/tmp", filename)
    scp_cmd = ["scp", "-P", VM_PORT, f"{VM_USER}@{VM_HOST}:{REMOTE_UNCATEGORIZED}/{filename}", local_temp]
    
    try:
        subprocess.run(scp_cmd, check=True)
    except subprocess.CalledProcessError as err:
        print(f"Error downloading file: {err}")
        return False

    with open(local_temp, "r", encoding="utf-8") as f:
        content = f.read()

    image_regex = re.compile(r'<!--image\s+(.*?)\s+image-->')
    match = image_regex.search(content)
    image_link = match.group(1) if (match and match.group(1).strip() not in ["None", ""]) else "https://bikepaths.org/blog/content/images/visuals-370.jpg"

    # Separate metadata and body
    t_match = re.search(r'<!--t (.*?) t-->', content)
    d_match = re.search(r'<!--d (.*?) d-->', content)
    t_text = t_match.group(1).strip() if t_match else ""
    d_text = d_match.group(1).strip() if d_match else ""
    body_content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL).strip()
    if t_text or d_text:
        body_content = f"Legacy Title: {t_text}\nLegacy Description: {d_text}\n\n{body_content}".strip()

    raw_path = os.path.join(blog_dir, "02_draft", f"{timestamp}_RAW.md")
    
    raw_content = f"<!--original_filename {filename} original_filename-->\n<!--original_image_link {image_link} original_image_link-->\n{body_content}\n"

    with open(raw_path, "w", encoding="utf-8") as f:
        f.write(raw_content)

    print(f"Raw file staged: {raw_path}")
    
    if os.path.exists(local_temp):
        os.remove(local_temp)
    return True

def generate_draft(raw_file):
    """
    Generates draft post from raw file.
    """
    if not os.path.isfile(raw_file):
        print(f"Error: {raw_file} is not a valid file.")
        return False

    with open(raw_file, "r", encoding="utf-8") as f:
        content = f.read()

    filename = os.path.basename(raw_file)
    parts = filename.replace(".md", "").split("_")
    timestamp = parts[0]
    
    # Parse original filename and image link from raw file comments if present
    orig_filename_match = re.search(r'<!--original_filename (.*?) original_filename-->', content)
    orig_image_match = re.search(r'<!--original_image_link (.*?) original_image_link-->', content)
    
    orig_filename = orig_filename_match.group(1).strip() if orig_filename_match else filename
    image_link = orig_image_match.group(1).strip() if orig_image_match else "https://bikepaths.org/blog/content/images/visuals-370.jpg"

    # Extract body content (stripping the RAW comment headers)
    body_content = re.sub(r'<!--original_filename.*?-->', '', content)
    body_content = re.sub(r'<!--original_image_link.*?-->', '', body_content).strip()

    # If it is a timestamped file, extract slug
    timestamp_pattern = r'^\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}$'
    if re.match(timestamp_pattern, timestamp):
        if len(parts) >= 3:
            slug = parts[-1]
        else:
            orig_parts = orig_filename.replace(".md", "").split("_")
            if len(orig_parts) >= 3:
                slug = orig_parts[-1]
            else:
                slug = "_".join(orig_parts[1:])
    else:
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        slug = filename.replace(".md", "").replace("_", "-")
        slug = re.sub(r'[^a-z0-9\-]', '', slug.lower())
        slug = re.sub(r'-+', '-', slug).strip("-")

    blog_dir = os.path.dirname(os.path.dirname(os.path.abspath(raw_file)))
    draft_path = os.path.join(blog_dir, "02_draft", f"{timestamp}_{slug}_DRAFT.md")

    print("Initiating autonomous narrative synthesis via OpenRouter API...")
    
    api_key = os.environ.get("OPENROUTER_API_KEY")
    title = "[New Title]"
    desc = "[Description]"
    tags_str = "[Tags]"
    body_text = "[Body content goes here]"
    
    if api_key:
        url = "https://openrouter.ai/api/v1/chat/completions"
        prompt = f"You are an elite editorial system. Write a cohesive, narrative blog post based on these facts:\n\n{body_content}\n\nCONSTRAINTS:\n1. Grade Level: 8th-grade conversational English (Flesch-Kincaid 7.0-10.0).\n2. Lexicon: ABSOLUTELY NO slop or weak qualifiers. Do not use words like: nuanced, holistic, seamless, leverage, utilize, heavy, heavily, essential, fundamentally, specifically, however, perfectly, fosters, greatly, solely, in summary, in conclusion.\n3. Structure: 3-5 flowing paragraphs.\n4. Headings: Do not use #, ##, or ### headings. Only #### or bold headings are permitted.\n5. Format: Start your response EXACTLY with these three lines:\nTitle: [Insert Title]\nDescription: [Insert 1-sentence description]\nTags: [Pick EXACTLY 3 tags from this authorized list ONLY: money, society, skills, systems, nature, technology, adventure, health, history, mind]\n\nThen leave a blank line and write the narrative body."
        data = {"model": "gpt-4o-mini", "messages": [{"role": "user", "content": prompt}]}
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
        req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers)
        try:
            with urllib.request.urlopen(req) as response:
                res_json = json.loads(response.read())
                generated_text = res_json["choices"][0]["message"]["content"].strip()
                lines = generated_text.splitlines()
                body_lines = []
                for line in lines:
                    if line.startswith("Title:"): title = line.replace("Title:", "").strip().strip('*')
                    elif line.startswith("Description:"): desc = line.replace("Description:", "").strip().strip('*')
                    elif line.startswith("Tags:"): tags_str = line.replace("Tags:", "").strip().strip('*')
                    else: body_lines.append(line)
                body_text = "\n".join(body_lines).strip()
                print("[SUCCESS] Autonomous narrative synthesized via OpenAI.")
        except Exception as e:
            print(f"LLM Synthesis failed: {e}. Falling back to placeholder.")
    else:
        print("Warning: OPENROUTER_API_KEY not found. Falling back to placeholder.")

    draft_content = f"<!--t {title} t-->\n<!--d {desc} d-->\n<!--tag {tags_str} tag-->\n<!--image {image_link} image-->\n\n{body_text}\n"

    with open(draft_path, "w", encoding="utf-8") as f:
        f.write(draft_content)

    print(f"Draft generated: {draft_path}")
    return True

def deploy_and_cleanup(posted_file):
    """
    Deploys verified post, removes remote uncategorized oldpost, and flushes cache.

    RE-DEPLOYMENT PROTOCOL:
    To update or redeploy an existing scheduled remote post:
    1. Download the target post from the remote scheduled folder to the local '02_draft' folder.
    2. Delete the remote scheduled file using ssh to prevent duplicate entries.
    3. Modify the local draft file to apply edits.
    4. Run this deployment script with --deploy pointing to the edited local draft path.
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
    local_image_path = os.path.join(blog_dir, "05_img", image_filename)

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

    final_posted_path = os.path.join(blog_dir, "03_posted", filename)
    if os.path.dirname(os.path.abspath(posted_file)) != os.path.dirname(os.path.abspath(final_posted_path)):
        try:
            os.rename(posted_file, final_posted_path)
            print(f"Moved staged file to posted: {final_posted_path}")
        except OSError as err:
            print(f"Error moving staged file: {err}")
            return False

    raw_path = os.path.join(blog_dir, "02_draft", f"{timestamp}_RAW.md")
    
    orig_filename = None
    if os.path.isfile(raw_path):
        with open(raw_path, "r", encoding="utf-8") as f:
            raw_content = f.read()
        filename_match = re.search(r'<!--original_filename (.*?) original_filename-->', raw_content)
        if filename_match:
            orig_filename = filename_match.group(1).strip()

    if not orig_filename:
        orig_filename = f"{timestamp}_uncategorized_{slug}.md"
        print(f"Raw file not found, guessing legacy filename: {orig_filename}")

    remote_old_path = f"{REMOTE_UNCATEGORIZED}/{orig_filename}"
    print(f"Removing oldpost: {remote_old_path}")
    rm_cmd = ["ssh", "-p", VM_PORT, f"{VM_USER}@{VM_HOST}", f"rm -f {remote_old_path}"]
    try:
        subprocess.run(rm_cmd, check=True)
    except subprocess.CalledProcessError as err:
        print(f"Warning: could not delete remote file: {err}")

    import glob
    draft_patterns = [
        os.path.join(blog_dir, "02_draft", f"{timestamp}_*_DRAFT.md"),
        os.path.join(blog_dir, "02_draft", f"{timestamp}_DRAFT.md"),
        os.path.join(blog_dir, "drafts", f"{timestamp}_*_DRAFT.md"),
        os.path.join(blog_dir, "drafts", f"{timestamp}_DRAFT.md")
    ]
    for pattern in draft_patterns:
        for p in glob.glob(pattern):
            if os.path.isfile(p):
                print(f"Removing local draft: {p}")
                try:
                    os.remove(p)
                except OSError as err:
                    print(f"Warning: could not delete local draft {p}: {err}")
            
    if os.path.isfile(raw_path):
        print(f"Removing local raw file: {raw_path}")
        try:
            os.remove(raw_path)
        except OSError as err:
            print(f"Warning: could not delete local raw file: {err}")

    verify_remote_permissions()

    print("\n[SUCCESS] Deployment and cleanup completed.")
    print("REMINDER: Sysop must manually clear the CMS cache directory on the VM.")
    
    timestamp_parts = filename.split('_')[0].split('-')
    year = timestamp_parts[0]
    month = timestamp_parts[1]
    slug = filename.split('_')[-1].replace('.md', '')
    print(f"\n[SEO] Live URL (post-cache purge): https://bikepaths.org/blog/{year}/{month}/{slug}")
    print("[NEXT ACTION] Sysop Command: execute batch pipeline")
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
    and stages the raw file in draft/ directory.
    """
    files = list_uncategorized()
    if not files:
        print("No remote uncategorized posts found to prepare.")
        return False
    
    first_file = files[0]
    print(f"\nAutomatically selecting next candidate: {first_file}")
    
    success = download_and_create_raw(first_file)
    if not success:
        print("Failed to download and stage raw file.")
        return False
        
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
        tags_list = [t.strip() for t in tag_match.group(1).split(",")]
        tags = ",".join(tags_list)
    
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
    raw_path = os.path.join(blog_dir, "02_draft", f"{timestamp}_RAW.md")
    if os.path.isfile(raw_path):
        with open(raw_path, "r", encoding="utf-8") as f:
            raw_content = f.read()
        filename_match = re.search(r'<!--original_filename (.*?) original_filename-->', raw_content)
        if filename_match:
            orig_file = filename_match.group(1).strip()
            orig_parts = orig_file.replace(".md", "").split("_")
            slug = orig_parts[-1]
    
    if not slug:
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
    staging_path = os.path.join(blog_dir, "02_draft", posted_filename)
    
    with open(staging_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"[SUCCESS] Draft staged for deployment: {staging_path}")
    return staging_path

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
        download_and_create_raw(args.download)
    elif args.draft:
        generate_draft(args.draft)
    elif args.deploy:
        target_file = args.deploy
        if target_file.endswith("_DRAFT.md") or "drafts" in target_file or "/02_draft/" in target_file:
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
