#!/usr/bin/env bash
# sync_to_vm.sh – Synchronize local blog posts to the remote VM webroot shadow
set -euo pipefail

VM_HOST="blog-vm.local"
VM_USER="webadm"
VM_TARGET_DIR="/var/www/html/blog/content"
LOCAL_SOURCE_DIR="/home/user0/git/publishing/blog"

echo "Beginning remote sync to VM host: ${VM_HOST}"

# Execute rsync mirror synchronization excluding git metadata
rsync -avz --delete \
  --exclude ".git*" \
  --exclude "*/research/*" \
  --exclude "*/drafts/*" \
  -e ssh "${LOCAL_SOURCE_DIR}/" "${VM_USER}@${VM_HOST}:${VM_TARGET_DIR}/"

echo "Sync execution complete."
