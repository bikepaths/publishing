#!/usr/bin/env bash
# sync_to_vm.sh – Synchronize local blog post to the remote VM via SCP port 2323
set -euo pipefail

FILE=$1
if [[ -z "$FILE" ]]; then
  echo "Usage: $0 <path_to_posted_markdown_file>"
  exit 1
fi

if [[ ! -f "$FILE" ]]; then
  echo "Error: file $FILE does not exist."
  exit 1
fi

FILENAME=$(basename "$FILE")
BLOG_DIR=$(dirname "$(dirname "$(readlink -f "$FILE")")")

IFS='_' read -r -a parts <<< "$FILENAME"
TAGS="${parts[1]}"
IFS=',' read -r -a tags_arr <<< "$TAGS"
TOPIC="${tags_arr[0]}"

IMAGE_VAL=$(grep -oP '<!--image\s+\K[^\s]+(?=\s+image-->)' "$FILE" || true)
if [[ -z "$IMAGE_VAL" ]]; then
  echo "Error: Could not extract image tag from metadata."
  exit 1
fi

IMAGE_NAME=$(basename "$IMAGE_VAL")
LOCAL_IMAGE_PATH="${BLOG_DIR}/img/${IMAGE_NAME}"

if [[ ! -f "$LOCAL_IMAGE_PATH" ]]; then
  echo "Error: local image file ${LOCAL_IMAGE_PATH} not found."
  exit 1
fi

VM_HOST="165.232.151.110"
VM_PORT="2323"
VM_USER="user0"

echo "Deploying post ${FILENAME} under topic: ${TOPIC}"

scp -P "${VM_PORT}" "${FILE}" "${VM_USER}@${VM_HOST}:/home/user0/www/bikepaths/html/blog/content/chas/blog/${TOPIC}/image/scheduled/${FILENAME}"

scp -P "${VM_PORT}" "${LOCAL_IMAGE_PATH}" "${VM_USER}@${VM_HOST}:/home/user0/www/bikepaths/html/blog/content/images/${IMAGE_NAME}"

echo "Deployment sync complete."
