#!/usr/bin/env bash
# post_deploy_static.sh - Phase 2 of the Static HTMLy Content Deployment
# Reads state from pre-deploy, executes direct SCP transfer, and updates the global ledger.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
STATE_FILE="${SCRIPT_DIR}/.deploy_target"

if [[ ! -f "$STATE_FILE" ]]; then
  echo "Error: Deployment state file not found. Run pre_deploy_static.sh first."
  exit 1
fi

IFS='|' read -r LOCAL_FILE REMOTE_DEST < "$STATE_FILE"

if [[ ! -f "$LOCAL_FILE" ]]; then
  echo "Error: Local file ${LOCAL_FILE} does not exist."
  exit 1
fi

VM_HOST="165.232.151.110"
VM_PORT="2323"
VM_USER="user0"

echo "=== PHASE 2: Targeted Deployment ==="
echo "Local source: ${LOCAL_FILE}"
echo "Remote target: ${REMOTE_DEST}"
echo "Executing direct SCP transfer..."
scp -P "${VM_PORT}" "${LOCAL_FILE}" "${VM_USER}@${VM_HOST}:${REMOTE_DEST}"

echo ""
echo "=== PHASE 3: Global Ledger Update ==="
echo "Re-executing remote bikepaths-sync..."
ssh -p "${VM_PORT}" "${VM_USER}@${VM_HOST}" "/usr/local/bin/bikepaths-sync"

# Clean up state file
rm -f "$STATE_FILE"

echo "=== OPERATION COMPLETE ==="
