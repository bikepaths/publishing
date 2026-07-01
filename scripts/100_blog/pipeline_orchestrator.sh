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
python3 scripts/100_blog/deploy_asset.py "$FILE"
echo "--- PIPELINE COMPLETE ---"
