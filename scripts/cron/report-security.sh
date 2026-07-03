#!/bin/bash
# report-security.sh - Specialized Security Review
# Target: hopiland@gmail.com
# Frequency: Every Day, 23:50

TO="hopiland@gmail.com"
SUBJECT="[SEC] BikePaths.org Security Review - $(date +%F)"
BASE_DIR="/home/user0/.cron_scripts"
PYTHON_BIN="/home/user0/.venv/bin/python"

if [ -f "$BASE_DIR/bot-guard.py" ]; then
    # Capture both stdout and stderr (2>&1)
    SEC_REPORT=$(sudo -n "$PYTHON_BIN" "$BASE_DIR/bot-guard.py" --review --no-color 2>&1)
    EXIT_CODE=$?
else
    SEC_REPORT="Error: bot-guard.py not found in $BASE_DIR."
    EXIT_CODE=1
fi

if [ -z "$SEC_REPORT" ]; then
    SEC_REPORT="Critical Error: Security report produced no output. Exit code: $EXIT_CODE"
fi

mail -s "$SUBJECT" "$TO" <<EOF
$SEC_REPORT
EOF
