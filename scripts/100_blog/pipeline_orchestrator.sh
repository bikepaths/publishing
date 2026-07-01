#!/usr/bin/env bash
# Global Pipeline Orchestrator

FILE=$1
if [ -z "$FILE" ]; then
    echo "Usage: ./pipeline_orchestrator.sh <file>"
    exit 1
fi

echo "--- PIPELINE START ---"
python3 scripts/100_blog/transform_draft.py "$FILE"
python3 scripts/100_blog/verify_syntax.py "$FILE"
python3 scripts/100_blog/verify_metadata.py "$FILE"

echo ""
echo "--- MANUAL AUDIT REQUIRED ---"
echo "Target file transformed and verified. Sysop authorization required for deployment."
read -p "Deploy $FILE to production? (y/N): " auth
if [[ "$auth" != "y" && "$auth" != "Y" ]]; then
    echo "Deployment aborted by sysop."
    exit 0
fi

python3 scripts/100_blog/deploy_asset.py "$FILE"
echo "--- PIPELINE COMPLETE ---"
