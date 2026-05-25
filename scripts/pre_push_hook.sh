#!/usr/bin/env bash
# Pre‑push verification script – ensures every added/modified file is present locally.
# Used by the repository’s pre‑push hook.

z40="0000000000000000000000000000000000000000"

while read local_ref local_sha remote_ref remote_sha; do
  if [[ "$local_sha" == "$z40" ]]; then
    # Branch deletion, skip check
    continue
  fi

  if [[ "$remote_sha" == "$z40" ]]; then
    # New branch, diff against parent or check all files in commit
    files=$(git diff-tree -r --no-commit-id --name-status "$local_sha" | awk '/^[AM]/ {print $2}')
  else
    files=$(git diff --name-status "$remote_sha..$local_sha" | awk '/^[AM]/ {print $2}')
  fi

  for f in $files; do
    if [[ ! -e "$f" ]]; then
      echo "[pre-push] ❌ File $f is missing locally."
      exit 1
    fi
  done
done

exit 0
