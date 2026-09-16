#!/usr/bin/env bash
if [[ "$1" == "--static" ]]; then
    if [ -z "$2" ] || [ -z "$3" ]; then
        echo "Usage: ./03_deploy.sh --static <local_file> <remote_destination>"
        exit 1
    fi
    LOCAL_FILE="$2"
    REMOTE_DEST="$3"
    VM_HOST="165.232.151.110"
    VM_PORT="2323"
    VM_USER="user0"
    
    if [[ ! -f "$LOCAL_FILE" ]]; then
      echo "Error: Local file ${LOCAL_FILE} does not exist."
      exit 1
    fi
    
    echo "--- STATIC DEPLOYMENT START ---"
    echo "Executing direct SCP transfer for static asset..."
    scp -P "${VM_PORT}" "${LOCAL_FILE}" "${VM_USER}@${VM_HOST}:${REMOTE_DEST}"
else
    FILE=$1
    if [ -z "$FILE" ]; then
        echo "Usage: ./03_deploy.sh <DRAFT_file>"
        echo "       ./03_deploy.sh --static <local_file> <remote_destination>"
        exit 1
    fi
    echo "--- DEPLOYMENT START ---"
    python3 scripts/100_blog/deploy_asset.py --deploy "$FILE"
fi

echo "--- INITIATING GLOBAL SYNC ---"
bash scripts/100_blog/sync_bikepaths_blog.sh
echo "--- PIPELINE COMPLETE ---"
