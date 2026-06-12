# Booklet Printing Standard

Standardized workflows for converting KDP manuscript source files into imposed, print-on-demand booklet formats.

## 1. Automated Booklet Compilation

Use the generic compilation script to process Markdown, EPUB, or DOCX files into 2-up landscape imposed PDFs ready for printing.

```bash
# Usage
scripts/200_amazon_kdp/compile_any_booklet.sh <input_file> [output_base_name]

# Example
scripts/200_amazon_kdp/compile_any_booklet.sh 200_amazon_kdp/03_survival_physics/kdp/manuscript/full_manuscript.md the_moral_physics_of_survival
```

This script:
1. Compiles the input to a Statement-sized (5.5" x 8.5") duplex PDF using XeLaTeX.
2. Applies layout overrides (`openany`, custom margin geometry, page clearance redefinitions) to eliminate blank spacer pages.
3. Imposes the pages side-by-side onto standard Letter paper using `pdfbook2`.
4. Pads the document signature to a multiple of 4 pages automatically.
5. Deletes intermediate single-page targets to keep directories clean.

## 2. Print-on-Demand Execution

To print the generated `*_booklet-book.pdf` file as a double-sided folded booklet:

### Command-Line Print Execution (CUPS)
Send print requests directly to the system queue using the command-line interface.

```bash
# Print first sheet (Pages 1 & 2) for testing duplex and margin alignment
lp -d Brother_HL_L2395DW_series -o page-ranges=1-2 -o Duplex=DuplexTumble /absolute/path/to/output_booklet-book.pdf

# Print remaining booklet sheets
lp -d Brother_HL_L2395DW_series -o page-ranges=3-28 -o Duplex=DuplexTumble /absolute/path/to/output_booklet-book.pdf

# Print entire booklet sequence in one job
lp -d Brother_HL_L2395DW_series -o Duplex=DuplexTumble /absolute/path/to/output_booklet-book.pdf
```

### Critical Printer Driver Directives
* **Landscape Orientation**: Automatically handled by the landscape layout of the imposed PDF.
* **Duplexing (`DuplexTumble`)**: Landscape booklets must flip along the short edge to prevent back sides from printing upside down.
* **Actual Scale (100%)**: Prevent scaling or page-fitting options to preserve the safety gutters and margins.
* **Binding**: Fold the finished sheet stack in half along the center crease and saddle-stitch (staple) down the spine.
