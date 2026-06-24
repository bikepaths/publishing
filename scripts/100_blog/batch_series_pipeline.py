#!/usr/bin/env python3
import os
import sys
import re
import subprocess
from datetime import datetime, timedelta

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '-', text)
    return text.strip('-')

def main():
    if len(sys.argv) < 2:
        print("Usage: batch_series_pipeline.py <source_directory> [--sysop-force-deploy]")
        sys.exit(1)

    source_dir = sys.argv[1]
    force_deploy = "--sysop-force-deploy" in sys.argv

    if not force_deploy:
        print("[INFO] Dry run mode. No remote deployment will occur.")

    if not os.path.exists(source_dir):
        print(f"Error: Source directory {source_dir} not found.")
        sys.exit(1)

    # Sort files to ensure sequential processing
    files = sorted([os.path.join(source_dir, f) for f in os.listdir(source_dir) if f.endswith('.md')])
    if not files:
        print(f"Error: No markdown files found in {source_dir}.")
        sys.exit(1)

    blog_dir = "/home/user0/git/publishing/100_blog"
    posted_dir = os.path.join(blog_dir, "03_posted", "series", "02_urban_survival")
    os.makedirs(posted_dir, exist_ok=True)

    vm_host = "165.232.151.110"
    vm_port = "2323"
    vm_user = "user0"

    base_time = datetime.strptime("2026-07-01 06:00:00", "%Y-%m-%d %H:%M:%S")
    
    local_posts = []
    local_images = []
    topics = set()

    # Pass 1: Validate all files and images before any deployment
    print("--- VALIDATION PASS ---")
    for idx, source_file in enumerate(files):
        with open(source_file, 'r', encoding='utf-8') as f:
            content = f.read()

        t_match = re.search(r'<!--t (.*?) t-->', content)
        d_match = re.search(r'<!--d (.*?) d-->', content)
        tag_match = re.search(r'<!--tag (.*?) tag-->', content)
        img_match = re.search(r'<!--image (.*?) image-->', content)

        if not (t_match and d_match and tag_match and img_match):
            print(f"Error: Missing metadata tags in {source_file}")
            sys.exit(1)

        title = t_match.group(1).strip()
        tags_str = tag_match.group(1).strip()
        tags = [t.strip() for t in tags_str.split(',') if t.strip()]
        topic = tags[0]
        topics.add(topic)

        image_url = img_match.group(1).strip()
        image_filename = os.path.basename(image_url)
        image_local_path = os.path.join(blog_dir, "05_img", "webp", image_filename)

        if not os.path.exists(image_local_path):
            print(f"Error: Image {image_filename} not found for {source_file}.")
            sys.exit(1)

        slug = slugify(title)
        
        # Stagger timestamp by 24 hours per post to maintain sequential order in CMS
        post_time = base_time + timedelta(hours=24*idx)
        timestamp_str = post_time.strftime("%Y-%m-%d-%H-%M-%S")
        
        post_filename = f"{timestamp_str}_{','.join(tags)}_{slug}.md"
        post_local_path = os.path.join(posted_dir, post_filename)
        
        body_content = content[img_match.end():].strip()
        
        local_posts.append((post_local_path, title, d_match.group(1).strip(), tags, image_url, body_content, topic))
        local_images.append(image_local_path)
        print(f"[PASS] Validated: {source_file}")

    print("\n--- GENERATION PASS ---")
    # Generate local files
    for post_local_path, title, meta_desc, tags, image_url, body_content, topic in local_posts:
        with open(post_local_path, 'w', encoding='utf-8') as f:
            f.write(f"<!--t {title} t-->\n")
            f.write(f"<!--d {meta_desc} d-->\n")
            f.write(f"<!--tag {', '.join(tags)} tag-->\n")
            f.write(f"<!--image {image_url} image-->\n\n")
            f.write(body_content)
            f.write("\n")
        print(f"[CREATED] {os.path.basename(post_local_path)}")

    if not force_deploy:
        print("\n[INFO] Dry run complete. Use --sysop-force-deploy to push to VM.")
        sys.exit(0)

    print("\n--- DEPLOYMENT PASS ---")
    # Create required remote directories
    for topic in topics:
        remote_post_dir = f"/home/user0/www/bikepaths/html/blog/content/chas/blog/{topic}/image/scheduled"
        subprocess.run(["ssh", "-p", vm_port, f"{vm_user}@{vm_host}", f"mkdir -p {remote_post_dir}"], check=True)

    remote_img_dir = "/home/user0/www/bikepaths/html/blog/content/images/webp"
    subprocess.run(["ssh", "-p", vm_port, f"{vm_user}@{vm_host}", f"mkdir -p {remote_img_dir}"], check=True)

    # Deduplicate images for transfer
    local_images = list(set(local_images))

    # SCP posts and images
    for post_local_path, _, _, _, _, _, topic in local_posts:
        post_filename = os.path.basename(post_local_path)
        remote_post_dir = f"/home/user0/www/bikepaths/html/blog/content/chas/blog/{topic}/image/scheduled"
        subprocess.run(["scp", "-P", vm_port, post_local_path, f"{vm_user}@{vm_host}:{remote_post_dir}/{post_filename}"], check=True)
        print(f"[SCP] Post: {post_filename}")

    for img_path in local_images:
        img_filename = os.path.basename(img_path)
        subprocess.run(["scp", "-P", vm_port, img_path, f"{vm_user}@{vm_host}:{remote_img_dir}/{img_filename}"], check=True)
        print(f"[SCP] Image: {img_filename}")

    print("\nDeployment sync to VM complete.")
    print("Triggering global sync...")
    subprocess.run(["ssh", "-p", vm_port, f"{vm_user}@{vm_host}", "/usr/local/bin/bikepaths-sync"], check=True)

    # Local sync triggers
    mirror_dir = "/home/user0/git/bikepaths"
    if os.path.exists(mirror_dir):
        print(f"Updating local mirror repo at {mirror_dir}...")
        subprocess.run(["git", "pull", "origin", "main"], cwd=mirror_dir, check=True)

    print("\n--- BATCH PIPELINE COMPLETE ---")

if __name__ == "__main__":
    main()
