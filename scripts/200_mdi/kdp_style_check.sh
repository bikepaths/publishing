#!/usr/bin/env bash
# kdp_style_check.sh – automated style compliance for KDP markdown chapters
# Implements the five‑pass revisions from the kdp‑manuscript‑editing skill.

set -euo pipefail

FILE=$1
if [[ -z "$FILE" ]]; then
  echo "Usage: $0 <markdown-file>"
  exit 1
fi

# PASS 1 – Replace em‑dashes with commas
sed -i $'s/\xE2\x80\x94/,/g' "$FILE"

# PASS 2 – Expand acronyms (simple static glossary, extend as needed)
declare -A ACRONYMS=(
  [EEOC]="Equal Employment Opportunity Commission"
  [PIV]="Personal Identity Verification"
  [MFA]="Multi‑Factor Authentication"
  [AWS]="Amazon Web Services"
)
for ac in "${!ACRONYMS[@]}"; do
  full="${ACRONYMS[$ac]}"
  # only replace first occurrence per file (as per style guide)
  if grep -q "\b$ac\b" "$FILE"; then
    sed -i "0,/$ac/{s/$ac/$full ($ac)/}" "$FILE"
  fi
done

# PASS 3 – Remove passive voice (simple heuristic: "was|were ... by")
# Convert "was X by Y" → "Y X"
perl -i -pe 's/\b(was|were)\s+([^\.]*?)\s+by\s+(\w+)/$3 $2/g' "$FILE"

# PASS 4 – Remove causal‑sentence endings (because, since, as, due to)
sed -i -E 's/ (because|since|as|due to)\.?$/./' "$FILE"

# PASS 5 – Enforce paragraph length 3‑7 sentences
# Split paragraphs with >7 sentences by inserting a blank line after the 7th sentence.
awk '{
  n=split($0, s, /\./);
  if (n>7) {
    for(i=1;i<=n;i++){
      printf "%s.", s[i];
      if(i%7==0) printf "\n\n"; # paragraph break after every 7 sentences
    }
    printf "\n";
  } else {
    print $0;
  }
}' "$FILE" > "$FILE.tmp" && mv "$FILE.tmp" "$FILE"

echo "Style check complete for $FILE"
