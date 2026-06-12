#!/bin/bash
# Compile Book Three booklet PDF (5.5" x 8.5", duplex, 9.5pt font)
set -e

WORKSPACE_ROOT="/home/user0/git/publishing"
MANUSCRIPT_PATH="${WORKSPACE_ROOT}/200_amazon_kdp/03_survival_physics/kdp/manuscript/full_manuscript.md"
OUTPUT_PATH="${WORKSPACE_ROOT}/200_amazon_kdp/03_survival_physics/kdp/handoff/the_moral_physics_of_survival_booklet.pdf"
PUBLISHED_PATH="${WORKSPACE_ROOT}/published/the_moral_physics_of_survival_booklet.pdf"

echo "Compiling booklet PDF for Book Three..."
pandoc \
  "${MANUSCRIPT_PATH}" \
  -o "${OUTPUT_PATH}" \
  --pdf-engine=xelatex \
  -V geometry:"paperwidth=5.5in,paperheight=8.5in,inner=0.75in,outer=0.5in,top=0.6in,bottom=0.6in,twoside" \
  -V classoption=twoside \
  -V documentclass=extbook \
  -V fontsize=9.5pt \
  -V mainfont="Liberation Serif" \
  --toc \
  --toc-depth=1

echo "Booklet PDF successfully compiled to: ${OUTPUT_PATH}"
cp "${OUTPUT_PATH}" "${PUBLISHED_PATH}"
echo "Deployed copy to: ${PUBLISHED_PATH}"
