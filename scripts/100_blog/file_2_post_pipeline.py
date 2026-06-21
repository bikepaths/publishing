#!/usr/bin/env python3
import os
import sys
import re
import subprocess
from datetime import datetime

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '-', text)
    return text.strip('-')

def main():
    if len(sys.argv) < 3:
        print("Usage: file_2_post_pipeline.py <source_file> <comma_separated_tags>")
        sys.exit(1)

    source_file = sys.argv[1]
    tags_str = sys.argv[2]

    if not os.path.exists(source_file):
        print(f"Error: Source file {source_file} not found.")
        sys.exit(1)

    tags = [t.strip() for t in tags_str.split(',') if t.strip()]
    if not tags:
        print("Error: At least one tag required.")
        sys.exit(1)

    # Read source file lines
    with open(source_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if len(lines) < 7:
        print("Error: Source file too short. Must contain title, meta description, and body.")
        sys.exit(1)

    title = lines[0].strip()

    meta_desc_raw = lines[2].strip()
    # Strip "**Meta description:**" prefix if present
    meta_desc = re.sub(r'^\*\*Meta description:\*\*\s*', '', meta_desc_raw, flags=re.IGNORECASE)

    # Body starts from line 7 (index 6)
    body_lines = lines[6:]
    body_content = "".join(body_lines).strip()

    slug = slugify(title)

    # Target post file local path
    blog_dir = "/home/user0/git/publishing/100_blog"
    posted_dir = os.path.join(blog_dir, "03_posted")

    # Check for existing post with same slug to prevent duplicate timestamps
    existing_files = []
    if os.path.exists(posted_dir):
        existing_files = [f for f in os.listdir(posted_dir) if f.endswith(f"_{slug}.md")]

    if existing_files:
        post_filename = existing_files[0]
        print(f"Reusing existing post file to prevent duplicates: {post_filename}")
    else:
        timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        post_filename = f"{timestamp}_{','.join(tags)}_{slug}.md"

    post_local_path = os.path.join(posted_dir, post_filename)

    # Image name logic (prefix with first two tags)
    prefix = "_".join(tags[:2]) if len(tags) >= 2 else tags[0]
    image_filename = f"{prefix}_{slug}.webp"
    image_url_path = f"webp/{image_filename}"

    image_local_path = os.path.join(blog_dir, "05_img", "webp", image_filename)
    os.makedirs(os.path.dirname(image_local_path), exist_ok=True)

    # Image check step
    if not os.path.exists(image_local_path):
        print("--- IMAGE GENERATION PROMPT REQUIRED ---")
        print("Local image file not found. Run generate_image with following specifications:")
        print(f"  Tool: generate_image")
        print(f"  ImageName: {prefix}_{slug}")
        print(f"  Prompt: An ancient temple dome next to modern concrete building, dramatic dusk lighting, symbolic transition, architectural contrast, professional photography")
        print(f"  Format: landscape proportional webp")
        print(f"  Move generated image to target: {image_local_path}")
        print("\nRun pipeline again after image is created.")
        sys.exit(1)

    # Create destination file
    print(f"Creating post file: {post_local_path}")
    os.makedirs(os.path.dirname(post_local_path), exist_ok=True)
    with open(post_local_path, 'w', encoding='utf-8') as f:
        f.write(f"<!--t {title} t-->\n")
        f.write(f"<!--d {meta_desc} d-->\n")
        f.write(f"<!--tag {', '.join(tags)} tag-->\n")
        f.write(f"<!--image https://bikepaths.org/blog/content/images/{image_url_path} image-->\n\n")
        f.write(body_content)
        f.write("\n")

    # VM connection parameters
    vm_host = "165.232.151.110"
    vm_port = "2323"
    vm_user = "user0"

    # Deploy to VM
    topic = tags[0]
    remote_post_dir = f"/home/user0/www/bikepaths/html/blog/content/chas/blog/{topic}/image/scheduled"
    remote_img_dir = "/home/user0/www/bikepaths/html/blog/content/images/webp"

    print("Deploying to remote VM...")
    # Create directories on remote if needed
    subprocess.run(["ssh", "-p", vm_port, f"{vm_user}@{vm_host}", f"mkdir -p {remote_post_dir} {remote_img_dir}"], check=True)

    # SCP markdown post
    subprocess.run(["scp", "-P", vm_port, post_local_path, f"{vm_user}@{vm_host}:{remote_post_dir}/{post_filename}"], check=True)

    # SCP image
    subprocess.run(["scp", "-P", vm_port, image_local_path, f"{vm_user}@{vm_host}:{remote_img_dir}/{image_filename}"], check=True)

    print("Deployment sync to VM complete.")

    # Global sync triggers
    print("Triggering global sync...")
    subprocess.run(["ssh", "-p", vm_port, f"{vm_user}@{vm_host}", "/usr/local/bin/bikepaths-sync"], check=True)

    # Pull local mirror repository
    mirror_dir = "/home/user0/git/bikepaths"
    if os.path.exists(mirror_dir):
        print(f"Updating local mirror repo at {mirror_dir}...")
        subprocess.run(["git", "pull"], cwd=mirror_dir, check=True)

    # Push local publishing repository
    scripts_dir = "/home/user0/git/publishing/scripts"
    hermes_script = os.path.join(scripts_dir, "hermes-push.sh")
    if os.path.exists(hermes_script):
        print("Pushing local publishing repository changes...")
        subprocess.run([hermes_script, f"post: {slug}"], cwd="/home/user0/git/publishing", check=True)

    print("--- POST PIPELINE PIPELINE COMPLETE ---")

if __name__ == "__main__":
    main()
