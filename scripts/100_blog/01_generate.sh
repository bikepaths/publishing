#!/usr/bin/env bash
FILE=$1
if [ -z "$FILE" ]; then
    echo "Usage: ./01_generate.sh <RAW_file>"
    exit 1
fi
echo "--- GENERATION START ---"
python3 scripts/100_blog/deploy_asset.py --draft "$FILE" "${@:2}"
echo "--- GENERATION COMPLETE ---"
echo "Review the generated draft in your IDE."
