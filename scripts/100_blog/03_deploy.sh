#!/usr/bin/env bash
FILE=$1
if [ -z "$FILE" ]; then
    echo "Usage: ./03_deploy.sh <DRAFT_file>"
    exit 1
fi
echo "--- DEPLOYMENT START ---"
python3 scripts/100_blog/deploy_asset.py --deploy "$FILE"
echo "--- INITIATING GLOBAL SYNC ---"
bash scripts/100_blog/sync_bikepaths_blog.sh
echo "--- PIPELINE COMPLETE ---"
