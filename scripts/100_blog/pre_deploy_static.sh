#!/usr/bin/env bash
# pre_deploy_static.sh - Phase 1 of the Static HTMLy Content Deployment
# Synchronizes state and prepares the local target for manual editing.

set -euo pipefail

if [[ "$#" -ne 2 ]]; then
  echo "Usage: $0 <local_file_path> <remote_destination_path>"
  echo "Example: $0 /home/user0/git/bikepaths/html/blog/content/static/tips.md /home/user0/www/bikepaths/html/blog/content/static/tips.md"
  exit 1
fi

LOCAL_FILE="$1"
REMOTE_DEST="$2"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
STATE_FILE="${SCRIPT_DIR}/.deploy_target"

echo "=== PHASE 1: State Synchronization ==="
if [[ -x "${SCRIPT_DIR}/sync_blog.py" ]]; then
    "${SCRIPT_DIR}/sync_blog.py"
else
    python3 "${SCRIPT_DIR}/sync_blog.py"
fi

# Write state for post-deploy
echo "${LOCAL_FILE}|${REMOTE_DEST}" > "$STATE_FILE"

echo ""
echo "=== Synchronization Complete ==="
echo "Target mapped: file://${LOCAL_FILE}"
echo "Execute your manual edits now. Use validation tools as required."
echo "When editing is complete, execute: ./post_deploy_static.sh"
