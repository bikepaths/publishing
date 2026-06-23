
import argparse
import os
import re
import subprocess
import datetime
from slugify import slugify

def intake(raw_content):
    """Stage 1: Accepts raw message text, strips [[POST!]] command, extracts content body, and detects/infers category.
    """
    print(f"[{datetime.datetime.now()}] Stage 1: INTAKE")
    # Strip [[POST!]] command
    post_command_pattern = r"^\s*\[\[POST\\?!\]\]\s*" # Regex to match [[POST!]] or [[POST\!]] at the beginning
    content_body = re.sub(post_command_pattern, "", raw_content, 1, flags=re.IGNORECASE).strip()

    # Basic category inference (can be expanded)
    category = "uncategorized"
    if "review" in content_body.lower():
        category = "reviews"
    elif "guide" in content_body.lower() or "how to" in content_body.lower():
        category = "guides"
    elif "news" in content_body.lower() or "update" in content_body.lower():
        category = "news"

    return content_body, category

def compose(content_body, category):
    """Stage 2: Applies style rules, generates metadata block, formats to blog_post_layout_standard, and generates filename.
    """
    print(f"[{datetime.datetime.now()}] Stage 2: COMPOSE")
    # Apply style rules
    # No em-dashes (replace with hyphens), direct language (simplify where possible, though this is hard to automate fully)
    # Dense paragraphs (remove excessive line breaks, though this also requires more advanced NLP for true 'densification')
    processed_content = content_body.replace('—', '-') # Replace em-dashes

    # Generate metadata block
    # For now, title and description are inferred or placeholders. Tags are also placeholders.
    # In a real scenario, these might be extracted from the content more intelligently or provided by the sysop.
    title = processed_content.split('\n')[0].strip() if processed_content else "Untitled Post"
    description = processed_content.split('\n')[1].strip() if len(processed_content.split('\n')) > 1 else "A new blog post."
    tags = "bikepaths,blog,new"
    image_filename = "image_filename.jpg" # Placeholder

    metadata_block = f"""<!-- t: {title} -->\n<!-- d: {description} -->\n<!-- tag: {tags} -->\n<!-- image: {image_filename} -->\n"""

    # Format to blog_post_layout_standard (prepend metadata block)
    formatted_content = metadata_block + processed_content

    # Generate proper filename with timestamp and slug
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    # Use slugify for the title to create a clean slug for the filename
    slug = slugify(title)
    filename = f"{timestamp}_{slug}.md"

    return formatted_content, filename, title, description, tags, image_filename

def hold(formatted_draft):
    """Stage 3: Returns formatted draft as a string for agent review.
    """
    print(f"[{datetime.datetime.now()}] Stage 3: HOLD")
    return formatted_draft

def stage(final_content, filename, category):
    """Stage 4: Clones/updates repo, writes file, git add/commit/push.
    """
    print(f"[{datetime.datetime.now()}] Stage 4: STAGE")
    repo_path = "/tmp/bikepaths_bikepaths"
    target_dir = os.path.join(repo_path, "blog", category, "image")
    file_path = os.path.join(target_dir, filename)

    # Clone or update repository
    if not os.path.exists(repo_path):
        print(f"[{datetime.datetime.now()}] Cloning bikepaths/bikepaths repository...")
        subprocess.run(["gh", "repo", "clone", "bikepaths/bikepaths", repo_path], check=True)
    else:
        print(f"[{datetime.datetime.now()}] Updating bikepaths/bikepaths repository...")
        subprocess.run(["git", "-C", repo_path, "pull", "origin", "main"], check=True)

    # Create target directory if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)

    # Write file
    print(f"[{datetime.datetime.now()}] Writing content to {file_path}...")
    with open(file_path, "w") as f:
        f.write(final_content)

    # Git add, commit, push
    print(f"[{datetime.datetime.now()}] Adding file to git...")
    subprocess.run(["git", "-C", repo_path, "add", file_path], check=True)

    commit_message = f"feat: Add new blog post: {filename}"
    print(f"[{datetime.datetime.now()}] Committing with message: \"{commit_message}\"...")
    subprocess.run(["git", "-C", repo_path, "commit", "-m", commit_message], check=True)

    print(f"[{datetime.datetime.now()}] Pushing to main branch...")
    subprocess.run(["git", "-C", repo_path, "push", "origin", "main"], check=True)

    print(f"[{datetime.datetime.now()}] Stage 4: STAGE completed successfully.")
    return True

def confirm(category, slug):
    """Stage 5: Returns the expected Vercel preview URL.
    """
    print(f"[{datetime.datetime.now()}] Stage 5: CONFIRM")
    base_url = "bikepaths.vercel.app"
    preview_url = f"https://{base_url}/{category}/{slug}"
    print(f"[{datetime.datetime.now()}] Stage 5: CONFIRM completed. Preview URL: {preview_url}")
    return preview_url

def main():
    parser = argparse.ArgumentParser(description="Bikepaths Blog Post Pipeline Orchestrator")
    parser.add_argument('--stage', required=True, choices=['intake', 'compose', 'hold', 'stage', 'confirm'],
                        help='Specify the pipeline stage to execute.')
    parser.add_argument('--input', help='Input content for the stage.')
    parser.add_argument('--category', help='Category for the blog post.')
    parser.add_argument('--filename', help='Filename for the blog post.')
    parser.add_argument('--slug', help='Slug for the blog post.')

    args = parser.parse_args()

    try:
        if args.stage == 'intake':
            if not args.input:
                print("Error: --input is required for intake stage.")
                return
            content_body, category = intake(args.input)
            print(f"Intake successful. Category: {category}\nContent Body:\n{content_body}")
        elif args.stage == 'compose':
            if not args.input or not args.category:
                print("Error: --input and --category are required for compose stage.")
                return
            formatted_content, filename, title, description, tags, image_filename = compose(args.input, args.category)
            print(f"Compose successful.\nFilename: {filename}\nTitle: {title}\nDescription: {description}\nTags: {tags}\nImage: {image_filename}\nFormatted Content:\n{formatted_content}")
        elif args.stage == 'hold':
            if not args.input:
                print("Error: --input is required for hold stage.")
                return
            draft = hold(args.input)
            print(f"Hold successful. Draft:\n{draft}")
        elif args.stage == 'stage':
            if not args.input or not args.filename or not args.category:
                print("Error: --input, --filename, and --category are required for stage stage.")
                return
            success = stage(args.input, args.filename, args.category)
            if success:
                print("Stage successful.")
            else:
                print("Stage failed.")
        elif args.stage == 'confirm':
            if not args.category or not args.slug:
                print("Error: --category and --slug are required for confirm stage.")
                return
            url = confirm(args.category, args.slug)
            print(f"Confirm successful. URL: {url}")
    except subprocess.CalledProcessError as e:
        print(f"Error during git operation: {e}")
        print(f"Command: {e.cmd}")
        print(f"Return Code: {e.returncode}")
        print(f"Output: {e.output}")
        print(f"Stderr: {e.stderr}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()
