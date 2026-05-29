#!/bin/bash
# scripts/sync_bikepaths_blog.sh
# Local Orchestrator: Triggers Server-to-GitHub Push, then Pulls locally.

REMOTE_USER="user0"
REMOTE_HOST="165.232.151.110"
REMOTE_PORT="2323"
LOCAL_REPO_PATH="/home/user0/git/bikepaths"

echo "--- STARTING GLOBAL SYNC ---"

# 1. Trigger Remote Sync (Server -> GitHub)
echo "[1/2] Triggering Remote Push-Sync..."
ssh -p "$REMOTE_PORT" "$REMOTE_USER@$REMOTE_HOST" "/usr/local/bin/bikepaths-sync"

if [ $? -ne 0 ]; then
    echo "❌ Error: Remote sync failed."
    exit 1
fi

# 2. Local Sync (GitHub -> Local)
echo "[2/2] Pulling latest from GitHub to Local..."
cd "$LOCAL_REPO_PATH" || exit 1
git pull origin main

echo "--- GLOBAL SYNC COMPLETE ---"
echo "Local repository is now a perfect reflection of GitHub (and the Server SOT)."
