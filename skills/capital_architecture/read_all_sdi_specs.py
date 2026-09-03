import os

repo_dir = "/home/user0/git/sdi-specification"
output = ""

for root, dirs, files in os.walk(repo_dir):
    if ".git" in root:
        continue
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            with open(filepath, "r") as f:
                output += f"--- {filepath} ---\n"
                output += f.read()
                output += "\n\n"

print(output)

