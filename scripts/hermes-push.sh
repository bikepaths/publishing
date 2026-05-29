#!/usr/bin/env bash
# Guarded push script
# Usage: ./hermes-push.sh "Commit message"
set -euo pipefail

MSG="$1"
if [[ -z "$MSG" ]]; then
  echo "Error: commit message required"
  exit 1
fi
# Commit all changes
git add -A
git commit -m "$MSG"
# Push
git push origin main
# Verify remote SHA matches local SHA
LOCAL_SHA=$(git rev-parse HEAD)
REMOTE_SHA=$(git rev-parse origin/main)
if [[ "$LOCAL_SHA" != "$REMOTE_SHA" ]]; then
  echo "ERROR: Remote SHA ($REMOTE_SHA) differs from local ($LOCAL_SHA)"
  exit 1
fi

echo "SUCCESS: Push verified. Remote SHA matches local."
