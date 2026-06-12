#!/bin/bash
# Convert any input file (Markdown, EPUB, DOCX) to a 2-up imposed Letter booklet PDF
set -e

if [ "$#" -lt 1 ]; then
  echo "Usage: $0 <input_file> [output_base_name]"
  echo "Example: $0 manuscript.md my_book"
  exit 1
fi

INPUT_FILE="$1"
INPUT_DIR="$(dirname "$(realpath "${INPUT_FILE}")")"
INPUT_BASE="$(basename "${INPUT_FILE}")"

if [ -n "$2" ]; then
  OUT_BASE="$2"
else
  OUT_BASE="${INPUT_BASE%.*}"
fi

OUTPUT_PDF="${INPUT_DIR}/${OUT_BASE}_booklet.pdf"
IMPOSED_PDF="${INPUT_DIR}/${OUT_BASE}_booklet-book.pdf"

echo "Compiling ${INPUT_FILE} to booklet PDF (${OUTPUT_PDF})..."
pandoc \
  "${INPUT_FILE}" \
  -o "${OUTPUT_PDF}" \
  --pdf-engine=xelatex \
  -V geometry:"paperwidth=5.5in,paperheight=8.5in,inner=0.75in,outer=0.5in,top=0.6in,bottom=0.6in,twoside" \
  -V classoption="openany,twoside" \
  -V documentclass=extbook \
  -V fontsize=9.5pt \
  -V mainfont="Liberation Serif" \
  -V header-includes="\let\cleardoublepage\clearpage" \
  --toc \
  --toc-depth=1

echo "Booklet PDF successfully compiled."

echo "Generating imposed Letter booklet PDF for printing..."
pdfbook2 \
  --paper=letterpaper \
  --short-edge \
  --no-crop \
  -o 0 -i 0 -t 0 -b 0 \
  "${OUTPUT_PDF}"
echo "Imposed print-ready PDF generated at: ${IMPOSED_PDF}"

# Clean up intermediate single-page PDF
rm "${OUTPUT_PDF}"
echo "Cleaned up intermediate reader PDF."
