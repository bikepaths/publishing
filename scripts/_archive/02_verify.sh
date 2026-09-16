#!/usr/bin/env bash
FILE=$1
if [ -z "$FILE" ]; then
    echo "Usage: ./02_verify.sh <DRAFT_file>"
    exit 1
fi
echo "--- VERIFICATION START ---"
python3 scripts/100_blog/transform_draft.py "$FILE"
python3 scripts/100_blog/verify_syntax.py "$FILE"
python3 scripts/100_blog/verify_metadata.py "$FILE"
python3 scripts/100_blog/verify_blog_post.py "$FILE"
echo "--- VERIFICATION COMPLETE ---"
echo "Review any changes or warnings in your IDE before proceeding to deployment."
