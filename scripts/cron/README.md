# Cron Scripts Manifest

## Overview
This directory contains the automated analytics and security scripts deployed to production for BikePaths.org. 

## Files

### `bot-guard.py`
* **Purpose**: Core analytics engine and firewall manager. Parses Apache access logs generating daily human visitor metrics and identifying malicious activity.
* **Dependencies**: Requires `/var/log/apache2/bikepaths_access.log`.
* **Output**: Generates daily metrics filtering out structural noise (`.webp`, `.md`), normalizing duplicate URIs, and isolating traffic by date. Maintains historical unique visitor totals in `article_stats.json`.
* **Important Operational Parameters**: 
  - Relies on Apache `LogFormat` utilizing `%a` to correctly extract `X-Forwarded-For` IPs from reverse proxies.
  - Requires execution at 23:50 isolating 24-hour traffic prior to midnight log rotation.

### `report-security.sh`
* **Purpose**: Automated Bash runner executing `bot-guard.py`.
* **Execution**: Scheduled via Crontab (`50 23 * * *`).
* **Dependencies**: Requires passwordless `sudo` configuration for `/home/user0/.venv/bin/python` on target host.
* **Output**: Captures standard output from `bot-guard.py` transmitting final report via `mail` to `hopiland@gmail.com`.

## Deployment Protocol
Scripts within this repository directory require manual deployment to remote production environment.
* **Source**: `/home/user0/git/publishing/scripts/cron/`
* **Target**: `/home/user0/.cron_scripts/` (Remote Host: `165.232.151.110` Port `2323`)
* **Method**: SSH/SCP transfer.

## Recent System Architecture Fixes (July 2026)
* Fixed unique visitor metric inflation by inserting current date filtering logic.
* Fixed URI duplication by normalizing `/blog/blog` paths to `/blog/`.
* Excluded `.webp` and `.md` assets from human article traffic aggregation.
* Refactored bot regex filter preventing false-positive dropping of legitimate human `fetch` and `axios` browser requests.
* Resolved exact string matching bug causing false positives in IP blocklist logic.
