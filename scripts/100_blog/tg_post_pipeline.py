#!/usr/bin/env python3
import argparse
import os
import re
import subprocess
import datetime
import sys

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '-', text)
    return text.strip('-')

ALLOWED_CATEGORIES = ['society', 'skills', 'systems', 'money', 'nature', 'technology', 'adventure', 'health', 'history', 'mind']

def intake(raw_content):
    """Stage 1: Accepts raw message text, strips [[POST!]] command, extracts content body.
    """
    print(f"[{datetime.datetime.now()}] Stage 1: INTAKE")
    post_command_pattern = r"^\s*\[\[POST\\?!\]\]\s*"
    content_body = re.sub(post_command_pattern, "", raw_content, 1, flags=re.IGNORECASE).strip()
    return content_body

def compose(content_body):
    """Stage 2: Extracts metadata, applies style rules, formats to blog_post_layout_standard, and generates filename.
    """
    print(f"[{datetime.datetime.now()}] Stage 2: COMPOSE")

    # Extract metadata
    t_match = re.search(r'<!--t (.*?) t-->', content_body)
    d_match = re.search(r'<!--d (.*?) d-->', content_body)
    tag_match = re.search(r'<!--tag (.*?) tag-->', content_body)
    image_match = re.search(r'<!--image (.*?) image-->', content_body)

    if not t_match or not d_match or not tag_match or not image_match:
        print("Error: Source file missing one or more required metadata tags (t, d, tag, image).")
        sys.exit(1)

    title = t_match.group(1).strip()
    description = d_match.group(1).strip()
    tags_str = tag_match.group(1).strip()
    image_url_full = image_match.group(1).strip()

    # Validate tags
    tags = [t.strip() for t in tags_str.split(',') if t.strip()]
    if not tags:
        print("Error: At least one tag required in metadata.")
        sys.exit(1)

    primary_category = tags[0]
    if primary_category not in ALLOWED_CATEGORIES:
        print(f"Error: Primary category '{primary_category}' is invalid. Must be one of: {ALLOWED_CATEGORIES}")
        sys.exit(1)

    if len(tags) > 6:
        print(f"Error: Too many tags ({len(tags)}). Maximum allowed is 6 (1 category + 5 tags).")
        sys.exit(1)

    # Extract image filename from URL
    image_filename = os.path.basename(image_url_full)
    if not image_filename.endswith('.webp'):
        print(f"Warning: Image filename '{image_filename}' does not end with .webp. Expected format.")

    # Apply style rules
    processed_content = content_body.replace('\u2014', '-')  # Replace em-dashes
    processed_content = processed_content.replace('\u2013', '-')  # Replace en-dashes
    # Remove markdown headers by replacing them with bold lines
    processed_content = re.sub(r'^#+\s*(.*)$', r'**\1**', processed_content, flags=re.MULTILINE)

    # Remove metadata block from the content body for the final post content
    content_without_metadata = re.sub(r'<!--t.*?t-->\n?', '', processed_content, flags=re.DOTALL)
    content_without_metadata = re.sub(r'<!--d.*?d-->\n?', '', content_without_metadata, flags=re.DOTALL)
    content_without_metadata = re.sub(r'<!--tag.*?tag-->\n?', '', content_without_metadata, flags=re.DOTALL)
    content_without_metadata = re.sub(r'<!--image.*?image-->\n?', '', content_without_metadata, flags=re.DOTALL).strip()

    # Reconstruct metadata block in correct format
    metadata_block = f"<!--t {title} t-->\n<!--d {description} d-->\n<!--tag {', '.join(tags)} tag-->\n<!--image {image_url_full} image-->\n\n"

    # Format to blog_post_layout_standard (prepend metadata block)
    formatted_content = metadata_block + content_without_metadata + "\n"

    # Generate proper filename with timestamp, tags, and slug
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    slug = slugify(title)
    filename = f"{timestamp}_{','.join(tags)}_{slug}.md"

    return formatted_content, filename, title, description, tags, image_url_full, primary_category

def hold(formatted_draft):
    """Stage 3: Returns formatted draft as a string for agent review.
    This is a semantic checkpoint. The sysop reviews meaning, not markup.
    """
    print(f"[{datetime.datetime.now()}] Stage 3: HOLD")
    return formatted_draft

def stage(final_content, filename, primary_category, sysop_force_deploy):
    """Stage 4: Deploys the post to bikepaths/bikepaths GitHub repo under blog/{category}/draft/.
    Uses gh CLI for git operations. No VM. No SSH.
    """
    print(f"[{datetime.datetime.now()}] Stage 4: STAGE")

    if not sysop_force_deploy:
        print("FATAL: Unauthorized remote push detected. NO DEPLOY WITHOUT EXPLICIT [--sysop-force-deploy] OVERRIDE.")
        sys.exit(1)

    repo_url = "bikepaths/bikepaths"
    repo_path = "/tmp/bikepaths_bikepaths"

    # Clone or update bikepaths/bikepaths repository
    if not os.path.exists(repo_path):
        print(f"[{datetime.datetime.now()}] Cloning {repo_url} repository...")
        subprocess.run(["gh", "repo", "clone", repo_url, repo_path], check=True)
    else:
        print(f"[{datetime.datetime.now()}] Updating {repo_url} repository...")
        subprocess.run(["git", "-C", repo_path, "pull", "origin", "main"], check=True)

    # Target directory: blog/{primary_category}/draft/
    target_dir = os.path.join(repo_path, "blog", primary_category, "draft")
    os.makedirs(target_dir, exist_ok=True)

    file_path = os.path.join(target_dir, filename)

    # Write post file
    print(f"[{datetime.datetime.now()}] Writing content to {file_path}...")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(final_content)

    # Git add, commit, push
    print(f"[{datetime.datetime.now()}] Adding file to git...")
    subprocess.run(["git", "-C", repo_path, "add", file_path], check=True)

    slug = slugify(os.path.splitext(filename)[0].split("_", 2)[-1]) if "_" in filename else filename
    commit_message = f"post: {slug}"
    print(f"[{datetime.datetime.now()}] Committing with message: \"{commit_message}\"...")
    subprocess.run(["git", "-C", repo_path, "commit", "-m", commit_message], check=True)

    print(f"[{datetime.datetime.now()}] Pushing to main branch...")
    subprocess.run(["git", "-C", repo_path, "push", "origin", "main"], check=True)

    print(f"[{datetime.datetime.now()}] Stage 4: STAGE completed successfully.")
    return True

def confirm(primary_category, slug):
    """Stage 5: Returns the expected live URL after Vercel auto-deploys.
    """
    print(f"[{datetime.datetime.now()}] Stage 5: CONFIRM")
    base_url = "bikepaths.vercel.app"
    preview_url = f"https://{base_url}/{primary_category}/{slug}"
    print(f"[{datetime.datetime.now()}] Stage 5: CONFIRM completed. Preview URL: {preview_url}")
    return preview_url

def main():
    parser = argparse.ArgumentParser(description="Bikepaths Blog Post Pipeline Orchestrator")
    parser.add_argument('--stage', required=True, choices=['intake', 'compose', 'hold', 'stage', 'confirm'],
                        help='Specify the pipeline stage to execute.')
    parser.add_argument('--input', help='Input content for the stage.')
    parser.add_argument('--sysop-force-deploy', action='store_true',
                        help='Explicit flag required for deployment in stage phase.')
    parser.add_argument('--filename', help='Filename for the blog post (used in stage).')
    parser.add_argument('--primary-category', help='Primary category for the blog post (used in stage and confirm).')
    parser.add_argument('--slug', help='Slug for the blog post (used in confirm).')

    args = parser.parse_args()

    try:
        if args.stage == 'intake':
            if not args.input:
                print("Error: --input is required for intake stage.")
                sys.exit(1)
            content_body = intake(args.input)
            print(f"Intake successful.\nContent Body:\n{content_body}")
        elif args.stage == 'compose':
            if not args.input:
                print("Error: --input is required for compose stage.")
                sys.exit(1)
            formatted_content, filename, title, description, tags, image_url_full, primary_category = compose(args.input)
            print(f"Compose successful.\nFilename: {filename}\nTitle: {title}\nDescription: {description}\nTags: {tags}\nImage URL: {image_url_full}\nPrimary Category: {primary_category}\nFormatted Content:\n{formatted_content}")
        elif args.stage == 'hold':
            if not args.input:
                print("Error: --input is required for hold stage.")
                sys.exit(1)
            draft = hold(args.input)
            print(f"Hold successful. Draft:\n{draft}")
        elif args.stage == 'stage':
            if not args.input or not args.filename or not args.primary_category:
                print("Error: --input, --filename, and --primary-category are required for stage.")
                sys.exit(1)
            success = stage(args.input, args.filename, args.primary_category, args.sysop_force_deploy)
            if success:
                print("Stage successful.")
            else:
                print("Stage failed.")
        elif args.stage == 'confirm':
            if not args.primary_category or not args.slug:
                print("Error: --primary-category and --slug are required for confirm stage.")
                sys.exit(1)
            url = confirm(args.primary_category, args.slug)
            print(f"Confirm successful. URL: {url}")
    except subprocess.CalledProcessError as e:
        print(f"Error during subprocess execution: {e}")
        print(f"Command: {e.cmd}")
        print(f"Return Code: {e.returncode}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
